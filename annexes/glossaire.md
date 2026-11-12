# Glossaire français ↔ anglais

Les termes mathématiques sont en français dans les fiches, avec l'anglais en glose à leur première apparition : c'est l'anglais que tu liras dans MML. Les termes du machine learning gardent l'usage de workbookIA (loss, learning rate, batch, feature… restent en anglais). Chaque chapitre ajoute ses termes ; la colonne « Chapitre » renvoie à celui qui le définit. Quelques entrées renvoient déjà à un chapitre à venir (M12a, M12c, M17…) : elles servent à reconnaître le mot dans MML ou dans workbookIA, et ce chapitre le définira.

| Français | Anglais | Définition courte | Chapitre |
|---|---|---|---|
| a priori conjugué | conjugate prior | un a priori dont l'a posteriori est de la même famille ; la loi Beta pour la binomiale : $\mathrm{Beta}(a, b) \to \mathrm{Beta}(a + k,\ b + n - k)$ | M04 |
| a priori, a posteriori | prior, posterior | la loi d'un paramètre ou d'une hypothèse avant de voir les données ; après, sachant les données | M04 |
| absorption | absorption (swamping) | un petit nombre ajouté à un grand disparaît à l'arrondi : $10^{16} + 1$ donne $10^{16}$ en `float64` | M05a |
| accuracy | accuracy | $P(\hat{Y} = Y)$ : la proportion de prédictions justes ; trompeuse quand une classe est rare | M03 |
| ACP (analyse en composantes principales) | principal component analysis (PCA) | centrer les données, les projeter sur les $k$ premiers axes principaux (les scores $\mathbf{Z} = \mathbf{X}_c\mathbf{W}_k$), et reconstruire $\hat{\mathbf{X}} = \mathbf{Z}\mathbf{W}_k^\top + \boldsymbol{\mu}$ : le sous-espace de dimension $k$ qui garde le plus de variance, et rend l'erreur de reconstruction la plus petite ; en pratique, par la SVD des données centrées, ou en diagonalisant la covariance quand $n \gg p$ | M12d |
| activation (fonction d') | activation function | une fonction d'une variable appliquée au score $z = \mathbf{w} \cdot \mathbf{x} + b$ d'un classifieur linéaire : seuil, sigmoïde, tanh, ReLU | M10 |
| actualiser, valeur actuelle | discount, present value | ramener une somme future à sa valeur d'aujourd'hui : la diviser par $(1 + t)^n$ | R5 |
| adjoint (d'un nœud) | adjoint | $\bar{u} = \frac{\partial y}{\partial u}$ : la dérivée de la sortie d'un calcul par rapport à un nœud ; le mode inverse les calcule de la sortie vers les entrées, $\bar{u} = \sum_{u \to w}\bar{w}\,\frac{\partial w}{\partial u}$ | M18 |
| affirmer le conséquent | affirming the consequent | le sophisme formel « $P \Rightarrow Q$ ; $Q$ ; donc $P$ » : non valide, la ligne « $P$ faux, $Q$ vrai » le réfute | M11 |
| AIC, BIC (critères d'information) | Akaike information criterion, Bayesian information criterion | $\mathrm{AIC} = 2k - 2\ln L$, $\mathrm{BIC} = k\ln n - 2\ln L$ ; le plus petit gagne ; le BIC pénalise davantage chaque paramètre dès $n \ge 8$ | M08 |
| aire algébrique | signed area | aire comptée positivement au-dessus de l'axe, négativement en dessous : c'est ce que mesure une intégrale | M02a |
| angle entre deux vecteurs | angle between two vectors | l'angle $\theta \in [0 ; \pi]$ tel que $\vec{u} \cdot \vec{v} = \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert\cos\theta$ | R9, M07 |
| annulation (catastrophique) | catastrophic cancellation | la perte de chiffres justes quand on soustrait deux nombres presque égaux : l'erreur relative explose | M05a |
| antécédent, image | preimage, image | $f(x)$ est l'image de $x$ ; un antécédent de $y$ est un $x$ tel que $f(x) = y$ | R3 |
| application affine | affine mapping | $\varphi(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}$ : une partie linéaire suivie d'une translation (en lignes, $\mathbf{x}\mathbf{W} + \mathbf{b}$ avec $\mathbf{W} = \mathbf{A}^\top$) ; la composée de deux applications affines est affine ; bijective si et seulement si $\mathbf{A}$ est inversible, et alors $\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$ | M12a, M16 |
| application linéaire | linear map, linear mapping | $f(\lambda\mathbf{x} + \mu\mathbf{y}) = \lambda f(\mathbf{x}) + \mu f(\mathbf{y})$ ; de $\mathbb{R}^n$ dans $\mathbb{R}^m$, c'est $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$, la colonne $j$ de $\mathbf{A}$ étant $f(\mathbf{e}_j)$ | M12a |
| approximation affine | linear approximation | $f(a + h) \approx f(a) + f'(a)\,h$ : la courbe remplacée par sa tangente près de $a$ | R7 |
| approximation de rang faible | low-rank approximation | $\mathbf{A}_k = \sum_{i \le k} s_i\mathbf{u}_i\mathbf{v}_i^\top$, les $k$ premières couches de la SVD : la matrice de rang $k$ la plus proche de $\mathbf{A}$ (Eckart-Young), stockée avec $k(m + n + 1)$ nombres au lieu de $mn$ | M12d |
| arbre pondéré | probability tree | arbre des étapes d'une expérience, chaque branche portant sa probabilité : on multiplie le long d'un chemin, on additionne les chemins | R8 |
| arccosinus | arccosine, arccos | la réciproque du cosinus sur $[0 ; \pi]$ : l'unique angle de $[0 ; \pi]$ qui a un cosinus donné | R9 |
| arête, nœud (d'un graphe) | edge, node (vertex) | un graphe relie des nœuds (ou sommets) par des arêtes ; dans un graphe orienté, l'arête $i \to j$ a un sens, $i$ est un prédécesseur (ou parent) de $j$ et $j$ un successeur (ou enfant) de $i$ ; les nœuds d'où part un chemin vers $j$ sont ses ancêtres, ceux où arrive un chemin parti de $i$ ses descendants | M16 |
| argmax, argmin | argmax, argmin | la valeur de $x$ où une fonction atteint son maximum (son minimum), pas la valeur de ce maximum | R3, M05b |
| argument, prémisse | argument, premise | une suite de phrases, les prémisses, suivie d'une conclusion qu'elles sont censées justifier | M11 |
| arrangement | k-permutation | choix ordonné de $k$ objets distincts parmi $n$ : $\frac{n!}{(n - k)!}$ possibilités | R8 |
| arrondi, troncature | rounding, truncation | arrondir garde le nombre le plus proche ; tronquer coupe sans regarder la suite | R1 |
| astuce de reparamétrisation | reparameterization trick | écrire $X = \mu + \sigma Z$ avec $Z \sim \mathcal{N}(0, 1)$ : le hasard est dans $Z$, et $\mu$, $\sigma$ deviennent des paramètres qu'on peut ajuster par gradient | M02b |
| astuce du biais | bias trick | ajouter une coordonnée constante 1 en tête : $\tilde{\mathbf{x}} = (1, \mathbf{x})$, $\tilde{\mathbf{w}} = (b, \mathbf{w})$, $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}} = \mathbf{w} \cdot \mathbf{x} + b$ : un hyperplan affine devient un hyperplan par l'origine | M10 |
| astuce du noyau | kernel trick | remplacer chaque produit scalaire $\mathbf{x}_i \cdot \mathbf{x}_j$ du dual d'une SVM par $k(\mathbf{x}_i, \mathbf{x}_j) = \varphi(\mathbf{x}_i) \cdot \varphi(\mathbf{x}_j)$ : une SVM linéaire dans l'espace des $\varphi$, une frontière non linéaire au départ, sans jamais calculer $\varphi$ | M13b |
| asymptote | asymptote | droite dont la courbe se rapproche indéfiniment : horizontale ($y = L$) ou verticale ($x = a$) | R7 |
| AUC (aire sous la courbe ROC) | area under the curve | $\int_0^1 \text{TPR}\,d(\text{FPR})$ : 1/2 pour le hasard, 1 pour un classement parfait | M02a, M03 |
| average precision | average precision (AP) | $\sum_j (R_j - R_{j-1})\,P_j$ : l'aire, en rectangles, sous la courbe precision-recall | M03 |
| axe principal, composante principale | principal axis, principal component | un vecteur propre unitaire de la matrice de covariance d'un nuage, rangé par valeur propre décroissante : la direction de plus grande variance, puis la plus grande orthogonalement aux précédentes ; « composante principale » désigne selon les auteurs l'axe ou les coordonnées sur l'axe | M12d |
| balanced accuracy | balanced accuracy | la moyenne des recalls des classes ; 0,5 pour un modèle qui prédit toujours la même classe | M03 |
| bandit manchot | multi-armed bandit | choisir pas à pas entre $K$ options (des bras) de récompenses moyennes inconnues, pour en accumuler le plus possible : le compromis entre exploration et exploitation | M11 |
| barrières de Tukey | (Tukey's) fences | les bornes $Q_1 - 1{,}5\,\text{EI}$ et $Q_3 + 1{,}5\,\text{EI}$ (EI : l'écart interquartile) ; une valeur hors de ces bornes est signalée comme aberrante | M02c |
| barycentre, centroïde | centroid, mean (of a point cloud) | $\bar{\mathbf{x}} = \frac{1}{m}\sum_i \mathbf{x}_i$, la moyenne coordonnée par coordonnée d'un nuage de points ; pondéré : $\frac{\sum_i \omega_i \mathbf{x}_i}{\sum_i \omega_i}$ | M07 |
| base (d'un espace vectoriel) | basis | une famille libre et génératrice : tout vecteur s'y écrit d'une seule façon, et ses coefficients sont ses coordonnées | M12a |
| base canonique | standard basis | les vecteurs $\mathbf{e}_1, \ldots, \mathbf{e}_n$ de $\mathbb{R}^n$ (un 1 à la place $i$, des 0 ailleurs) : $\mathbf{x} = \sum_i x_i\,\mathbf{e}_i$ | M07 |
| base orthonormée | orthonormal basis | une base de vecteurs unitaires deux à deux orthogonaux ; les coordonnées s'y lisent par des produits scalaires, $c_i = \langle \mathbf{v}, \mathbf{q}_i \rangle$ | M12b |
| biais (d'un estimateur) | bias | $\mathbb{E}[\hat{\theta}] - \theta$ : l'erreur systématique d'un estimateur, en moyenne sur tous les échantillons | M02c |
| biais (d'un neurone) | bias | nombre $b$ ajouté à la somme pondérée d'un neurone, appris comme les poids | R1 |
| biais d'échantillonnage | sampling bias | un échantillon qui ne représente pas la population visée, à cause de la façon dont il a été collecté ; plus de données ne le corrigent pas | M02c |
| biais de sélection | selection bias | les individus observés ne sont pas tirés au hasard dans la population visée (taux de réponse inégaux, filtre) : l'estimation converge vers une mauvaise valeur, quelle que soit la taille | M11 |
| biais du survivant | survivorship bias | n'observer que ce qui a passé un filtre (les avions rentrés de mission, les prêts accordés), et conclure comme si c'était tout | M02c |
| Bienaymé-Tchebychev (inégalité de) | Chebyshev's inequality | $P(\lvert X - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$, pour toute loi de variance finie | M02c, M11 |
| bit, nat | bit, nat | unités d'information : un événement de probabilité $p$ apporte $-\log_2 p$ bits, ou $-\ln p$ nats ; 1 bit ≈ 0,693 nat | R6, M06 |
| blanchiment | whitening | une transformation $\mathbf{z} = \mathbf{W}(\mathbf{x} - \boldsymbol{\mu})$ qui rend la covariance égale à l'identité, $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ : ZCA ($\boldsymbol{\Sigma}^{-1/2}$, symétrique), par l'ACP ($\boldsymbol{\Lambda}^{-1/2}\mathbf{Q}^\top$) ou par Cholesky ($\mathbf{L}^{-1}$) ; deux blanchiments diffèrent d'une matrice orthogonale | M12c |
| boîte à moustaches | boxplot, box-and-whisker plot | dessin d'une série : une boîte de $Q_1$ à $Q_3$ coupée par la médiane, des moustaches jusqu'aux valeurs non aberrantes les plus extrêmes | M02c |
| Bonferroni (correction de) | Bonferroni correction | chaque test au seuil $\frac{\alpha}{m}$, ou les p-valeurs ajustées $\min(1, m\,p_i)$ comparées à $\alpha$ : la probabilité d'au moins un faux positif reste sous $\alpha$, sans hypothèse d'indépendance | M08 |
| bootstrap | bootstrap | estimer la dispersion d'une statistique en la recalculant sur des milliers de rééchantillons tirés avec remise dans les données | M02c |
| borne de Chernoff | Chernoff bound | pour $X$ de loi $\mathcal{B}(n, p)$ et $a > p$ : $P(X \ge na) \le e^{-n\,\mathrm{KL}(a \Vert p)}$, obtenue par la méthode de Chernoff avec le meilleur $\lambda$ ; toujours au moins aussi bonne que la borne de Hoeffding | M14 |
| borne de l'union, inégalité de Boole | union bound, Boole's inequality | $P(A_1 \cup \cdots \cup A_K) \le \sum_k P(A_k)$ ; pour $K$ rayons de confiance valables ensemble au risque $\delta$, chacun au risque $\frac{\delta}{K}$ | M08, M11 |
| borne supérieure de confiance (UCB) | upper confidence bound | la borne haute d'un intervalle de confiance d'une moyenne ; UCB1 choisit l'option de plus grande $\hat{\mu}_k + \sqrt{\frac{2\ln t}{N_k}}$ | M11 |
| borne, intervalle | bound, interval | ensemble des réels compris entre deux bornes, incluses (crochet fermé) ou non (crochet ouvert) ; une borne peut être infinie | R2 |
| boule unité | unit ball | les vecteurs de norme au plus 1 ; dans le plan, un losange pour L1, un disque pour L2, un carré pour L∞ ; toujours convexe | M07 |
| bras | arm | une option d'un problème de bandit : chaque choix donne une récompense aléatoire, de moyenne inconnue | M11 |
| broadcasting | broadcasting | NumPy répète un tableau le long des axes qui lui manquent : `X - X.mean(axis=0)` retire le vecteur des moyennes à chaque ligne | M09a |
| calcul symbolique | symbolic computation | calcul exact sur des expressions avec des lettres (SymPy), sans valeurs approchées | R0 |
| calibration | calibration | un modèle est calibré si $P(Y = 1 \mid \text{score} = p) = p$ : ses probabilités sont honnêtes | M03 |
| cardinal | cardinality | le nombre d'éléments d'un ensemble fini, noté $\lvert A \rvert$ | R4 |
| cellule (d'un notebook) | cell | bloc de code ou de texte qu'on exécute d'un coup | R0 |
| centroïde le plus proche (classifieur du) | nearest centroid classifier | classer un point dans la classe dont le barycentre est le plus proche | M07 |
| cercle trigonométrique | unit circle | le cercle de centre $O$ et de rayon 1, parcouru dans le sens inverse des aiguilles d'une montre | R9 |
| chaîne de caractères | string | du texte entre guillemets, comme `"abc"` : Python le garde tel quel, sans le calculer | R0 |
| chaîne monotone d'Andrew | monotone chain (Andrew's algorithm) | l'enveloppe convexe d'un nuage du plan : trier, puis construire la chaîne du bas et celle du haut en ne gardant que les virages strictement à gauche | M10 |
| champ de vecteurs | vector field | une flèche en chaque point du plan (ou de l'espace) ; le gradient d'une fonction en est un | M05b |
| changement de base (d'une application linéaire) | basis change | la matrice de $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$ dans la base des colonnes de $\mathbf{S}$ : $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ ; entre deux espaces, $\mathbf{T}^{-1}\mathbf{A}\mathbf{S}$ | M12a |
| changement de base (formule de) | change of base formula | $\log_b x = \frac{\ln x}{\ln b}$ | R6 |
| changement de variable | change of variables, substitution | $\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$ | M02a |
| chemin (dans un graphe) | walk, path | une suite de $k$ arêtes consécutives (sa longueur), de $i$ à $j$ ; dans un graphe orienté de matrice d'adjacence $\mathbf{A}$, il y en a $(\mathbf{A}^k)_{ij}$ ; un même nœud peut y revenir (en anglais, *walk* ; *path* exige souvent des nœuds distincts) | M16 |
| chiffres significatifs | significant figures | les chiffres d'un nombre à partir du premier chiffre non nul | R1 |
| Cholesky (décomposition de), facteur de Cholesky | Cholesky decomposition, Cholesky factor | $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$, $\mathbf{L}$ triangulaire inférieure à diagonale strictement positive, unique ; elle existe si et seulement si $\mathbf{A}$ est symétrique définie positive, ce qui en fait le test pratique ; elle sert à résoudre des systèmes, à calculer $\det\mathbf{A} = \prod_i l_{ii}^2$, à tirer des vecteurs de covariance donnée | M12c |
| classe positive | positive class | la classe que l'on cherche à détecter (la panne, le défaut), codée 1 | M03 |
| code de longueur fixe, de longueur variable | fixed-length code, variable-length code | un code dont tous les mots ont la même longueur ($\lceil \log_2 N \rceil$ bits pour $N$ issues) ; un code qui donne des mots plus courts aux issues fréquentes | M06 |
| code préfixe | prefix code, prefix-free code | un code où aucun mot n'est le début d'un autre : des mots écrits bout à bout se découpent sans ambiguïté | M06 |
| coefficient | coefficient | nombre qui multiplie la partie littérale d'un terme : 7 dans $7x^2$ | R2 |
| coefficient binomial | binomial coefficient | $\binom{n}{k}$, « k parmi n » : le nombre de façons de choisir $k$ objets parmi $n$, sans ordre | R8 |
| coefficient de détermination ($R^2$) | coefficient of determination | $1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$ : la part de la variation des cibles que le modèle fait disparaître ; 1 s'il est parfait, négatif possible sur de nouvelles données | M09b |
| coefficient de variation | coefficient of variation | l'écart-type relatif $c_X = \frac{\sigma_X}{\lvert\mathbb{E}[X]\rvert}$ ; pour un produit de variables indépendantes de moyennes non nulles, $1 + c_{XY}^2 = (1 + c_X^2)(1 + c_Y^2)$ | M16 |
| coefficient multiplicateur | multiplier, growth factor | nombre $1 + t$ par lequel une évolution de taux $t$ multiplie une valeur | R1 |
| colinéaires (vecteurs) | collinear vectors | l'un est un multiple de l'autre : $xy' - x'y = 0$ | R9 |
| comatrice | cofactor matrix (sa transposée : adjugate) | la matrice des cofacteurs $C_{ij}$, $(-1)^{i+j}$ fois le déterminant de la matrice privée de la ligne $i$ et de la colonne $j$ ; $\mathbf{X}\operatorname{com}(\mathbf{X})^\top = \det\mathbf{X}\;\mathbf{I}$, et c'est le gradient de $\det\mathbf{X}$ | M18 |
| combinaison affine | affine combination | une combinaison linéaire dont les coefficients ont une somme égale à 1 (un barycentre) ; une application affine la conserve | M12a |
| combinaison convexe | convex combination | $\sum_i t_i\mathbf{x}_i$ avec $t_i \ge 0$ et $\sum_i t_i = 1$ ; le segment, le barycentre en sont | M10 |
| combinaison linéaire | linear combination | somme de vecteurs multipliés par des nombres | M07, M12a |
| comparaisons multiples | multiple comparisons, multiple testing | faire beaucoup de tests, ou essayer beaucoup de modèles : $m\alpha$ faux positifs en moyenne si aucun effet n'existe | M08 |
| complément orthogonal | orthogonal complement | $U^\perp$, les vecteurs orthogonaux à tout $U$ : un sous-espace de dimension $n - \dim U$ ; $(\operatorname{Im}\mathbf{A})^\perp = \ker\mathbf{A}^\top$ | M12b |
| complémentaire (d'un ensemble) | complement | $\bar{A}$ : les éléments de l'univers qui ne sont pas dans $A$ | R4 |
| complémentarité | complementary slackness | la condition KKT $\mu_i\,g_i(\mathbf{x}^*) = 0$ : une contrainte inactive a un multiplicateur nul | M13b |
| composée (de deux fonctions) | composition, composite function | $(f \circ g)(x) = f(g(x))$ : on applique $g$, puis $f$ | R3 |
| compromis biais-variance | bias-variance trade-off | un modèle plus souple a moins de biais et plus de variance ; une pénalité comme ridge règle cet équilibre | M09b |
| concave | concave | dont toute corde est au-dessous de la courbe ; pour $f$ deux fois dérivable, $f'' \le 0$ | M05a |
| concentration (de la norme) | concentration of measure | en grande dimension, une quantité qui dépend de beaucoup de coordonnées indépendantes varie peu autour de sa valeur typique : la norme d'un vecteur gaussien de $\mathbb{R}^n$ vaut $\sqrt{n}$ à environ 0,7 près | M07 |
| condition de Slater | Slater's condition | l'existence d'un point strictement admissible ($g_i(\mathbf{x}) < 0$ pour les inégalités non affines) ; avec la convexité, elle donne la dualité forte | M13b |
| condition nécessaire, suffisante | necessary, sufficient condition | dans $P \Rightarrow Q$, P est suffisante pour Q et Q nécessaire pour P | R4 |
| conditionnement | condition number | $\kappa(\mathbf{A}) = s_{\max}/s_{\min} \ge 1$ (infini si $\mathbf{A}$ n'est pas de rang plein) : l'amplification maximale d'une erreur relative, $\frac{\lVert \delta\mathbf{x} \rVert}{\lVert \mathbf{x} \rVert} \le \kappa\,\frac{\lVert \delta\mathbf{b} \rVert}{\lVert \mathbf{b} \rVert}$ ; on perd environ $\log_{10}\kappa$ chiffres ; $\kappa(\mathbf{A}^\top\mathbf{A}) = \kappa^2$ ; le déterminant ne le mesure pas ; pour une matrice symétrique définie positive, $\lambda_{\max}/\lambda_{\min}$, qui fixe le nombre d'itérations des méthodes itératives (M19) | M12d, M19 |
| conditions KKT | Karush-Kuhn-Tucker conditions | pour $\min f$ sous $g_i \le 0$ et $h_j = 0$ : admissibilité, stationnarité du lagrangien, $\mu_i \ge 0$ et complémentarité ; nécessaires sous qualification, suffisantes pour un problème convexe | M13b |
| conjugué (d'un nombre complexe) | complex conjugate | $\overline{a + ib} = a - ib$ ; $z\bar z = \lvert z\rvert^2$ ; les racines non réelles d'un trinôme réel sont conjuguées | M19 |
| conservateur (test) | conservative test | un test dont le risque de type I réel est plus petit que le seuil annoncé, comme un test à statistique discrète | M08 |
| continuité | continuity | $f$ est continue en $a$ si $\lim_{x \to a} f(x) = f(a)$ : pas de saut | R7 |
| contrainte active, inactive | active, inactive constraint | une contrainte d'inégalité atteinte avec égalité à la solution ($g(\mathbf{x}^*) = 0$), ou non ($g(\mathbf{x}^*) < 0$, et son multiplicateur est nul) | M13b |
| contraposée | contrapositive | $\text{non } Q \Rightarrow \text{non } P$, de même valeur que $P \Rightarrow Q$ | R4 |
| contre-exemple | counterexample | un cas qui rend fausse une phrase « pour tout » | R4 |
| convergence linéaire, quadratique | linear, quadratic convergence | l'erreur est multipliée par une constante $< 1$ à chaque pas (linéaire), ou à peu près élevée au carré (quadratique : les décimales justes doublent) | M05a |
| convergent (estimateur) | consistent estimator | estimateur dont l'erreur tend vers 0 quand la taille de l'échantillon grandit | M02c |
| converger, diverger (suite) | converge, diverge | une suite converge si elle a une limite finie ; sinon elle diverge (vers $\pm\infty$, ou sans limite) | R5 |
| convexe | convex | un ensemble l'est s'il contient le segment entre deux quelconques de ses points ; une fonction l'est si chaque corde est au-dessus de sa courbe (c'est-à-dire si son épigraphe est un ensemble convexe) | M05a, M10 |
| coordonnée par coordonnée (fonction appliquée) | elementwise | $\mathbf{f}(\mathbf{x}) = (g(x_1), \ldots, g(x_n))$ pour une fonction $g$ d'une variable (`np.sin(x)`) ; sa jacobienne est diagonale, $\mathrm{diag}(g'(x_i))$, et $\mathbf{J}\mathbf{v} = g'(\mathbf{x}) \odot \mathbf{v}$ | M17 |
| coordonnées dans une base | coordinates, coordinate vector | les coefficients $(c_1, \ldots, c_n)$ de l'écriture unique $\mathbf{v} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n$ : la solution de $\mathbf{B}\mathbf{c} = \mathbf{v}$ | M12a |
| coordonnées homogènes, matrice homogène | homogeneous coordinates, augmented matrix | on ajoute une coordonnée 1 au point : en lignes, $[\mathbf{x}, 1]\,\mathbf{H} = [\mathbf{x}\mathbf{W} + \mathbf{b}, 1]$ avec $\mathbf{H} = \begin{pmatrix} \mathbf{W} & \mathbf{0} \\ \mathbf{b} & 1 \end{pmatrix}$ ; une application affine devient un produit, et composer devient multiplier les matrices homogènes | M16 |
| coordonnées polaires | polar coordinates | repérer un point du plan par sa distance $r$ à l'origine et son angle $\theta$ ; dans une intégrale double, $dx\,dy$ devient $r\,dr\,d\theta$ | M02b |
| coordonnées, repère orthonormé | coordinates, orthonormal frame | un repère a une origine et deux axes perpendiculaires de même unité ; un point y est repéré par $(x ; y)$ | R9 |
| corrélation (coefficient de) | correlation coefficient (Pearson) | $r = \frac{\operatorname{Cov}(x, y)}{s_x s_y}$, entre $-1$ et 1 : la force d'une relation **linéaire** ; le cosinus de l'angle entre les vecteurs d'écarts | M02c |
| cosinus, sinus | cosine, sine | l'abscisse et l'ordonnée du point d'angle $\theta$ du cercle trigonométrique | R9 |
| cote, log-cote | odds, log-odds | la cote d'une probabilité $p$ est $\frac{p}{1 - p}$ ; la log-cote, son logarithme | R6 |
| couche dense (linéaire) | dense (fully connected, linear) layer | $\mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}$ : une ligne par exemple, une colonne de $\mathbf{W}$ par neurone, un biais par neurone ajouté à chaque ligne | M09a |
| couple de variables aléatoires | pair of random variables, random vector | deux variables définies sur le même univers, étudiées ensemble par leur loi jointe | M02b |
| courbe precision-recall | precision-recall curve | pour chaque seuil, le point (recall, precision) ; elle dépend de la prévalence | M03 |
| courbe représentative | graph (of a function) | l'ensemble des points $(x, f(x))$ | R3 |
| courbe ROC | ROC curve (receiver operating characteristic) | pour chaque seuil, le point (taux de faux positifs, recall) : un escalier de (0, 0) à (1, 1) | M03 |
| couverture | coverage | proportion des échantillons pour lesquels un intervalle de confiance contient la vraie valeur | M02c |
| covariance empirique | empirical (sample) covariance | $\frac{1}{n}\sum (x_i - \bar{x})(y_i - \bar{y})$ (ou divisée par $n - 1$) : la moyenne des produits des écarts | M02c |
| critère d'arrêt | stopping criterion | la règle qui arrête une méthode itérative : en général le résidu relatif $\lVert\mathbf{b} - \mathbf{A}\mathbf{x}_k\rVert/\lVert\mathbf{b}\rVert$ sous une tolérance, avec un nombre maximal d'itérations | M19 |
| croissances comparées | orders of growth, comparative growth rates | pour $x$ très grand, $\ln x \ll x^k \ll a^x$ ($k > 0$, $a > 1$) | R6 |
| croissante, décroissante | increasing, decreasing | qui conserve (retourne) l'ordre sur un intervalle : $a < b \Rightarrow f(a) \le f(b)$ ($\ge$) | R3 |
| cross-entropy | cross-entropy | $H(p, q) = -\sum p \log_2 q$ : la longueur moyenne d'un code fait pour la loi $q$, sur des données de loi $p$ ; la log loss en est une | M06 |
| cycle (d'un graphe), boucle | cycle, loop | un chemin qui revient à son point de départ ; une arête $i \to i$ est un cycle de longueur 1 ; un graphe orienté sans cycle est un DAG | M16 |
| ddof | ddof (delta degrees of freedom) | le nombre retranché à $n$ au dénominateur d'une variance : `ddof=0` divise par $n$, `ddof=1` par $n - 1$ | M02c |
| débordement, underflow | overflow, underflow | un résultat trop grand pour un flottant, que NumPy rend `inf` ; trop petit, il est arrondi à 0 (*dépassement par le bas*) ; on garde souvent les mots anglais | M04, M05a |
| décade, échelle logarithmique | decade, logarithmic scale | sur un axe logarithmique, des écarts égaux sont des rapports égaux ; une décade est un facteur 10 | R6 |
| décibel | decibel (dB) | un rapport $R$ exprimé par $10 \log_{10} R$ ; le PSNR se mesure en décibels | R6 |
| décomposition biais-variance | bias-variance decomposition | l'erreur quadratique attendue sur une nouvelle mesure vaut biais² + variance + bruit $\sigma^2$ | M09b |
| décomposition en valeurs singulières (SVD) | singular value decomposition (SVD) | $\mathbf{A} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$, pour toute matrice réelle : $\mathbf{U}$ et $\mathbf{V}$ orthogonales, $\mathbf{S}$ « diagonale » de valeurs singulières positives décroissantes ; une rotation, un étirement des axes, une rotation | M12d |
| décomposition QR | QR decomposition | $\mathbf{A} = \mathbf{Q}\mathbf{R}$, colonnes de $\mathbf{Q}$ orthonormées (Gram-Schmidt), $\mathbf{R}$ triangulaire supérieure à diagonale positive ; les moindres carrés deviennent $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$ | M12b |
| décomposition spectrale | spectral decomposition, eigendecomposition | pour une matrice symétrique, $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top = \sum_i \lambda_i\mathbf{q}_i\mathbf{q}_i^\top$ : une somme de projections orthogonales sur les directions propres, pondérées par les valeurs propres | M12c |
| décorrélées (variables) | uncorrelated | de covariance nulle ; les variances s'ajoutent alors ; indépendantes implique décorrélées, pas l'inverse ($X$ uniforme sur $\{-1, 0, 1\}$ et $X^2$) | M16 |
| déduction, induction | deduction, induction | raisonner des prémisses à une conclusion certaine si elles sont vraies ; généraliser des exemples à une conclusion seulement probable (le raisonnement par récurrence est une déduction) | M11 |
| défective (matrice) | defective matrix | une matrice $n \times n$ qui a moins de $n$ vecteurs propres libres : une valeur propre a une multiplicité géométrique inférieure à sa multiplicité algébrique ; elle n'est pas diagonalisable (le cisaillement $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$) | M12c |
| déflation | deflation | remplacer $\mathbf{A}$ symétrique par $\mathbf{A} - \lambda_1\mathbf{q}_1\mathbf{q}_1^\top$, qui a les mêmes valeurs propres sauf $\lambda_1$, remplacée par 0, pour trouver la suivante par la méthode de la puissance | M12c |
| degré entrant, degré sortant | in-degree, out-degree | le nombre d'arêtes qui arrivent en un nœud, qui en partent : la somme d'une colonne, d'une ligne de la matrice d'adjacence ; dans un réseau de calculs, on dit *fan-in* et *fan-out* | M16 |
| degrés de liberté | degrees of freedom | le nombre de valeurs libres : les $n$ écarts à la moyenne ont une somme nulle, donc $n - 1$ degrés de liberté | M02c |
| demi-espace | half-space | l'un des deux côtés d'un hyperplan : les $\mathbf{x}$ tels que $\mathbf{w} \cdot \mathbf{x} + b > 0$ (ou $< 0$) | M07 |
| démonstration par l'absurde | proof by contradiction | supposer la conclusion fausse et aboutir à une contradiction | R4 |
| dénombrement | counting | l'art de compter des possibilités sans les lister : principe multiplicatif, factorielles, combinaisons | R8 |
| densité de probabilité | probability density function (pdf) | fonction positive d'aire totale 1 : $P(a \le X \le b) = \int_a^b f$ ; une probabilité par unité de longueur, qui peut dépasser 1 | M02a |
| densité jointe | joint density | fonction $f(x, y) \ge 0$ d'intégrale double 1, telle que $P((X, Y) \in D) = \iint_D f$ | M02b |
| dérivée à gauche, dérivée à droite | left derivative, right derivative (one-sided derivatives) | les limites de $\frac{f(a + h) - f(a)}{h}$ quand $h \to 0$ par valeurs négatives, positives : en un point anguleux, les pentes des deux morceaux ; $f$ est dérivable en $a$ si elles sont égales | M17 |
| dérivée directionnelle | directional derivative | la pente de $f$ en un point quand on avance dans la direction d'un vecteur unitaire $\mathbf{u}$ : $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$ | M05b |
| dérivée locale | local derivative | sur l'arête $u \to w$ d'un graphe de calcul, $\frac{\partial w}{\partial u}$ : la dérivée de la seule opération qui calcule $w$, évaluée aux valeurs de la passe avant | M18 |
| dérivée partielle | partial derivative | dérivée par rapport à une variable, les autres fixées | M05b |
| dérivée seconde | second derivative | la dérivée de $f'$, notée $f''$ : son signe dit si la pente augmente (courbe convexe) ou diminue (concave) | M05a |
| dérivée, fonction dérivée | derivative | la pente de la tangente, taux de variation instantané ; la fonction $x \mapsto f'(x)$ qui la donne en chaque point | R7 |
| dérivées partielles secondes, dérivée croisée | second partial derivatives, mixed partial derivative | $f_{xx}$, $f_{yy}$, et $f_{xy}$, la dérivée de $f_x$ par rapport à $y$ | M05b |
| désabonnement | churn | le départ d'un client à la fin de son abonnement ; une cible courante des modèles de classification | M03 |
| descente de gradient, montée de gradient | gradient descent, gradient ascent | $\mathbf{x}_{k+1} = \mathbf{x}_k - \eta\,\nabla f(\mathbf{x}_k)$ : de petits pas dans la direction de plus grande descente, pour minimiser ; avec $+$, pour maximiser | M05b |
| déterminant | determinant | le nombre $ad - bc$ d'un système 2 × 2, non nul exactement quand il a une seule solution (R2) ; en toute dimension, le facteur (signé) par lequel une application linéaire multiplie les aires ou les volumes, non nul exactement quand la matrice est inversible ; il se calcule par élimination (le produit des pivots, au signe des échanges près) | R2, M12c |
| développement par cofacteurs | Laplace expansion, cofactor expansion | calculer un déterminant selon une ligne ou une colonne : $\det\mathbf{A} = \sum_j (-1)^{i+j}a_{ij}\det\mathbf{A}_{ij}$, où $\mathbf{A}_{ij}$ est la matrice privée de la ligne $i$ et de la colonne $j$ ; de l'ordre de $n!$ opérations, utile seulement à la main | M12c |
| développer, factoriser | expand, factor | transformer un produit en somme ; transformer une somme en produit | R2 |
| diagonalisable | diagonalizable | $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ avec $\mathbf{D}$ diagonale (les valeurs propres) et les colonnes de $\mathbf{P}$ des vecteurs propres ; possible si et seulement si les vecteurs propres forment une base ; toujours vrai pour une matrice symétrique, avec $\mathbf{P}$ orthogonale | M12c |
| diagramme de fiabilité | reliability diagram | pour des paquets de scores, la probabilité moyenne annoncée contre la fréquence observée ; la diagonale si le modèle est calibré | M03 |
| diagramme de Venn | Venn diagram | chaque ensemble dessiné comme une région du plan : une inclusion dit qu'une région est vide, « au moins un » qu'elle contient un élément | M11 |
| dichotomie | bisection | trouver un zéro en coupant l'intervalle en deux et en gardant la moitié où le signe change | R7 |
| différence finie (avant, centrée) | finite difference (forward, central) | une approximation de $f'(x)$ par $\frac{f(x + h) - f(x)}{h}$ (ordre 1) ou $\frac{f(x + h) - f(x - h)}{2h}$ (ordre 2) | M05a |
| différentiation automatique | automatic differentiation (AD, autodiff) | appliquer les règles de dérivation aux nombres, opération par opération, pendant le calcul : une dérivée exacte aux arrondis près, en mode direct ou en mode inverse | M18 |
| différentielle | differential | le changement d'une fonction au premier ordre ; pour une fonction réelle d'une matrice, $\mathrm{d}f = \operatorname{tr}(\mathbf{G}^\top\mathrm{d}\mathbf{X})$, où l'on lit le gradient $\mathbf{G}$ | M18 |
| dimension | dimension | le nombre de vecteurs de n'importe quelle base : $\dim\mathbb{R}^n = n$, $\dim\mathbb{R}_d[x] = d + 1$ | M12a |
| direction de plus grande pente | steepest ascent direction | $\frac{\nabla f}{\lVert \nabla f \rVert}$, la direction où $f$ monte le plus vite, avec la pente $\lVert \nabla f \rVert$ ; l'opposée est celle de plus grande descente | M05b |
| discriminant | discriminant | $\Delta = b^2 - 4ac$ ; son signe donne le nombre de racines de $ax^2 + bx + c$ | R3 |
| disjonction de cas | proof by cases | découper en cas qui couvrent toutes les possibilités, et traiter chacun | R4 |
| distance (entre deux points) | distance | $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$, la norme du vecteur $\overrightarrow{AB}$ | R9 |
| distance cosinus | cosine distance | $1 - \cos\theta$, entre 0 et 2 : ce que renvoie `scipy.spatial.distance.cosine` | M07 |
| distance de Mahalanobis | Mahalanobis distance | $\sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})}$ : la distance usuelle après un blanchiment, quel qu'il soit ; un écart mesuré en écarts-types, en tenant compte des corrélations | M12c |
| distance euclidienne, de Manhattan, de Tchebychev | Euclidean, Manhattan (city block), Chebyshev distance | la norme L2, L1 ou L∞ de la différence de deux points | M07 |
| divergence de Jensen-Shannon | Jensen-Shannon divergence | $\frac{1}{2}\mathrm{KL}(p \parallel m) + \frac{1}{2}\mathrm{KL}(q \parallel m)$ avec $m = \frac{p + q}{2}$ : une divergence symétrique et toujours finie | M06 |
| divergence KL (de Kullback-Leibler) | KL divergence, Kullback-Leibler divergence, relative entropy | $\mathrm{KL}(p \parallel q) = \sum p \log_2 \frac{p}{q} = H(p, q) - H(p)$ : les bits perdus par symbole ; positive, nulle si $p = q$, pas symétrique | M06 |
| division euclidienne | Euclidean division, integer division | $a = bq + r$ avec $0 \le r < b$ ; en Python, `a // b` donne $q$ et `a % b` donne $r$ | R0 |
| double descente | double descent | l'erreur de test culmine près de $p = n$ (poids instables), puis peut redescendre au-delà avec la solution de plus petite norme | M09b |
| dualité faible, dualité forte | weak, strong duality | la fonction duale minore toujours le minimum du primal ($\max D \le \min f$) ; pour un problème convexe qui vérifie la condition de Slater, $\max D = \min f$ | M13b |
| écart (d'une option) | gap | $\Delta_k = \mu^\star - \mu_k$ : ce que coûte, en moyenne, un choix de l'option $k$ au lieu de la meilleure | M11 |
| écart interquartile | interquartile range (IQR) | $Q_3 - Q_1$ : la dispersion de la moitié centrale d'une série, insensible aux valeurs extrêmes | M02c |
| écart-type | standard deviation | racine carrée de la variance | R8 |
| échangeabilité | exchangeability | sous $H_0$, toutes les répartitions des valeurs entre les groupes sont aussi probables : ce qui justifie un test par permutation | M08 |
| échantillon i.i.d. | i.i.d. sample | variables $X_1, \ldots, X_n$ indépendantes et de même loi : le modèle de base des données en statistique et en ML | M02c |
| échantillonnage de Thompson | Thompson sampling | choisir à chaque essai l'option dont un tirage dans l'a posteriori est le plus grand : explorer et exploiter à la fois | M04, M11 |
| Eckart-Young (théorème d') | Eckart-Young theorem | aucune matrice de rang $k$ n'est plus proche de $\mathbf{A}$ que $\mathbf{A}_k$, en norme de Frobenius comme en norme spectrale ; $\lVert \mathbf{A} - \mathbf{A}_k \rVert_F^2 = \sum_{i > k} s_i^2$ et $\lVert \mathbf{A} - \mathbf{A}_k \rVert_2 = s_{k+1}$ | M12d |
| effectif attendu | expected count | l'effectif d'une case d'un tableau de contingence si les variables étaient indépendantes : $\frac{\text{total de la ligne} \times \text{total de la colonne}}{\text{total}}$ | M03 |
| effet de masque | masking effect | une valeur aberrante gonfle l'écart-type et cache ainsi son propre z-score | M02c |
| égalité des taux d'erreur | equalized odds | critère d'équité : le même recall et le même taux de faux positifs dans chaque groupe | M03 |
| embedding (table d') | embedding (table) | une matrice d'une ligne par mot (ou par catégorie) : l'embedding du mot $k$ est la ligne $k$, le produit de son vecteur one-hot par la table | M09a |
| empreinte | hash | code calculé à partir d'une donnée, d'où l'on ne peut pas la retrouver ; sert à comparer sans stocker | R0 |
| ensemble | set | collection d'éléments distincts | R4 |
| ensemble (de modèles) | ensemble (of models) | un prédicteur qui en combine plusieurs : il les fait voter, moyenne leurs prédictions, pondère leurs avis, ou les ajoute l'un après l'autre | M14 |
| ensemble de définition | domain | l'ensemble des $x$ pour lesquels $f(x)$ a un sens | R3 |
| ensemble des événements | event space | $\mathcal{A}$, les parties de l'univers auxquelles on donne une probabilité | M02b |
| ensemble des solutions | solution set | l'ensemble de toutes les valeurs qui rendent une équation (ou une inéquation) vraie | R2 |
| entier naturel, entier relatif | natural number, integer | ℕ = {0, 1, 2…} ; ℤ ajoute les entiers négatifs | R1 |
| entropie | entropy | $H(p) = -\sum p_i \log_2 p_i$, la surprise moyenne d'une loi ; entre 0 (loi certaine) et $\log_2 n$ (loi uniforme sur $n$ issues) | M06 |
| entropie conditionnelle | conditional entropy | $H(Y \mid X) = \sum_x p(x)\,H(Y \mid X = x)$ : l'incertitude qui reste sur $Y$ quand on connaît $X$, en moyenne | M06 |
| entropie conjointe | joint entropy | $H(X, Y) = -\sum p(x, y) \log_2 p(x, y)$, l'entropie de la loi jointe d'un couple | M06 |
| enveloppe convexe | convex hull | $\operatorname{conv}(S)$ : l'ensemble des combinaisons convexes de points de $S$, le plus petit convexe qui contient $S$ | M10 |
| épigraphe | epigraph | la région au-dessus de la courbe d'une fonction, $\{(x, y) : y \ge f(x)\}$ ; convexe si et seulement si $f$ l'est | M10 |
| epsilon machine | machine epsilon | l'écart entre 1 et le flottant suivant : $2^{-52} \approx 2{,}2 \times 10^{-16}$ en `float64` | M05a |
| epsilon-greedy, ε-greedy | epsilon-greedy | avec la probabilité $\varepsilon$, une option tirée au hasard, sinon celle de meilleure moyenne observée ; à $\varepsilon$ fixé, son regret croît linéairement | M11 |
| équation | equation | égalité qui contient une inconnue ; la résoudre, c'est trouver toutes ses solutions | R2 |
| équation cartésienne, équation réduite | Cartesian equation, slope-intercept form | $ax + by + c = 0$, qui convient à toute droite ; $y = mx + p$, pour une droite non verticale | R9 |
| équations équivalentes | equivalent equations | équations qui ont exactement les mêmes solutions | R2 |
| équations normales | normal equations | $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$ : les poids qui annulent le gradient de la somme des carrés des résidus ; une seule solution si $\mathbf{X}$ est de rang $p$ | M09b |
| équiprobabilité | equally likely outcomes | toutes les issues ont la même probabilité : $P(A) = \frac{\lvert A \rvert}{\lvert \Omega \rvert}$ | R8 |
| équivalence (logique) | equivalence, if and only if | $P \Leftrightarrow Q$ : $P \Rightarrow Q$ et $Q \Rightarrow P$ | R4 |
| erreur d'arrondi, erreur de troncature | rounding error, truncation error | l'erreur due à la précision finie des flottants ; l'erreur due à une formule approchée (un développement coupé, un pas $h$ non nul) | M05a |
| erreur de reconstruction | reconstruction error | $\lVert \mathbf{x} - \hat{\mathbf{x}} \rVert^2$, l'écart entre un exemple et sa reconstruction par une ACP (ou un autoencodeur) ; en moyenne sur les données d'une ACP à $k$ composantes, $\frac{n-1}{n}$ fois la somme des variances oubliées ; elle sert de score d'anomalie | M12d |
| erreur de type I, de type II | type I error (false positive), type II error (false negative) | rejeter $H_0$ alors qu'elle est vraie (probabilité $\alpha$) ; ne pas la rejeter alors que l'effet existe (probabilité $\beta$) | M08 |
| erreur quadratique moyenne (d'un estimateur) | mean squared error (MSE) | $\mathbb{E}[(\hat{\theta} - \theta)^2] = \text{biais}^2 + \text{variance}$ | M02c |
| erreur type | standard error (SE) | l'écart-type d'un estimateur ; pour une moyenne, $\frac{s}{\sqrt{n}}$ ; pour une proportion, $\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$ | M02c |
| espace d'arrivée | target space | l'ensemble des valeurs que peut prendre une variable aléatoire ($\mathcal{T}$ dans MML) : $\mathbb{R}$, un ensemble de classes ou de vecteurs | M02b |
| espace des colonnes, espace des lignes | column space, row space | le sous-espace engendré par les colonnes de $\mathbf{A}$ (son image), ou par ses lignes ; tous deux ont pour dimension le rang | M12a |
| espace probabilisé | probability space | le triplet (univers, événements, probabilité) d'une expérience aléatoire | M02b |
| espace propre | eigenspace | $\ker(\mathbf{A} - \lambda\mathbf{I})$ : les vecteurs propres de $\lambda$ et le vecteur nul ; sa dimension est la multiplicité géométrique de $\lambda$ | M12c |
| espace vectoriel | vector space | un ensemble où l'on additionne des vecteurs et où on les multiplie par des réels, avec les règles de calcul habituelles : $\mathbb{R}^n$, les polynômes, les matrices d'une forme donnée | M12a |
| espérance | expected value, expectation | moyenne théorique d'une variable aléatoire | R8 |
| estimateur | estimator | formule qui estime un paramètre à partir de données | M02c |
| estimateur plug-in (de l'entropie) | plug-in estimator | l'entropie des fréquences observées ; elle sous-estime l'entropie, surtout sur de petits échantillons (correction de Miller-Madow : $+\frac{k - 1}{2n\ln 2}$ bit) | M06 |
| estimation (valeur) | estimate | la valeur d'un estimateur calculée sur les données observées | M02c |
| estimation de Fermi | Fermi estimate | ordre de grandeur obtenu en découpant une question en facteurs faciles à estimer | R1 |
| événement | event | partie de l'univers : les issues pour lesquelles une phrase est vraie | R8 |
| événements incompatibles | mutually exclusive events, disjoint events | événements sans issue commune : $A \cap B = \varnothing$ | R8 |
| événements indépendants | independent events | $P(A \cap B) = P(A)\,P(B)$ : savoir que l'un s'est réalisé ne change pas la probabilité de l'autre | R8 |
| évidence (vraisemblance marginale) | evidence, marginal likelihood | $P(O) = \sum_j P(O \mid H_j)\,P(H_j)$ : le dénominateur de la formule de Bayes | M04, M08 |
| experts (prédiction avec des) | prediction with expert advice | à chaque tour, $K$ experts donnent un avis ; on les combine, puis on voit la loss de **chacun** ; on mesure le regret contre le meilleur expert, sans rien supposer sur l'origine des losses | M14 |
| exponentielle (fonction) | exponential function | $x \mapsto a^x$ ($a > 0$) ; la fonction exponentielle est $\exp(x) = e^x$ | R6 |
| exposant | exponent | le nombre $n$ de $a^n$ ; en notation scientifique, la puissance de 10 | R1 |
| expression littérale, variable | algebraic expression, variable | expression où des lettres, les variables, représentent des nombres | R2 |
| extrapolation de Richardson | Richardson extrapolation | combiner deux approximations de pas $h$ et $\frac{h}{2}$ pour annuler le premier terme d'erreur : $\frac{4D(h/2) - D(h)}{3}$ | M05a |
| extremum local, global | local, global extremum | maximum ou minimum au voisinage d'un point (local) ou sur tout le domaine (global) | R7, M05a |
| F-beta | F-beta score | $\frac{(1 + \beta^2)PR}{\beta^2 P + R}$ : moyenne harmonique pondérée de la precision et du recall ; $\beta > 1$ favorise le recall | M03 |
| facteur de Bayes | Bayes factor | $\mathrm{BF}_{12} = \frac{p(\mathcal{D} \mid M_1)}{p(\mathcal{D} \mid M_2)}$, le rapport des évidences de deux modèles ; cote a posteriori = facteur de Bayes × cote a priori | M08 |
| facteur de correction de population finie | finite population correction | $\frac{N - n}{N - 1}$ : le facteur de la variance de la moyenne pour des tirages sans remise | M02c |
| factorielle | factorial | $n! = n \times (n - 1) \times \cdots \times 1$, le nombre de rangements de $n$ objets ; $0! = 1$ | R8 |
| faisabilité (problème de) | feasibility problem | chercher seulement un point qui vérifie toutes les contraintes, sans rien optimiser ; décider si un nuage est linéairement séparable en est un | M10 |
| famille exponentielle | exponential family | les lois de la forme $h(x)\exp(\eta\,T(x) - A(\eta))$ : Bernoulli, gaussienne, Beta, Poisson… | M04 |
| famille génératrice | generating set, spanning set | une famille dont tout vecteur de l'espace est une combinaison linéaire : $\operatorname{Vect}(\mathbf{v}_1, \ldots, \mathbf{v}_k) = V$ | M12a |
| famille libre, famille liée | linearly independent, linearly dependent | libre : seule la combinaison de coefficients tous nuls donne $\mathbf{0}$ (chaque colonne porte un pivot) ; liée : l'un des vecteurs combine les autres | M12a |
| famille orthogonale, famille orthonormée | orthogonal set, orthonormal set | des vecteurs deux à deux orthogonaux ; orthonormée s'ils sont en plus unitaires ($\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$) ; une famille orthogonale de vecteurs non nuls est libre | M12b |
| faux positif, faux négatif | false positive, false negative (FP, FN) | un négatif prédit positif (fausse alerte) ; un positif prédit négatif (cas manqué) | M03 |
| features polynomiales | polynomial features | les monômes des features jusqu'à un degré $d$, interactions comprises : $\binom{p + d}{d}$ colonnes, constante comprise | M09b |
| flottant (nombre à virgule flottante) | floating-point number, float | nombre à virgule rangé avec un nombre fixe de chiffres binaires, donc souvent arrondi | R0, M05a |
| fonction | function | règle qui associe à chaque élément de son ensemble de définition une seule image | R3 |
| fonction affine, linéaire | affine function, linear function | $x \mapsto mx + c$ ; linéaire quand $c = 0$ | R3 |
| fonction Beta, fonction Gamma | Beta function, Gamma function | $B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)}$ ; $\Gamma(n) = (n - 1)!$ pour un entier $n \ge 1$ | M04 |
| fonction d'erreur | error function, erf | $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$, un nom donné à cette intégrale sans primitive usuelle | M02a |
| fonction de lien | link function | dans un modèle linéaire généralisé, la fonction qui relie la moyenne de la cible au score linéaire : le logit pour la régression logistique, l'identité pour la régression linéaire | M13a |
| fonction de masse | probability mass function (pmf) | $p(x) = P(X = x)$ pour une variable discrète : positive, de somme 1 | M02b |
| fonction de partition | partition function | $Z = \sum_j e^{-E_j/T}$, la constante qui normalise une loi de Boltzmann | M17 |
| fonction de plusieurs variables | multivariate function, function of several variables | une fonction qui prend plusieurs nombres et en renvoie un, comme $f(x, y)$ ; son graphe est une surface | M05b |
| fonction de répartition | cumulative distribution function (cdf) | $F(x) = P(X \le x)$ : croissante de 0 à 1, et $F' = f$ pour une densité $f$ | M02a |
| fonction définie par morceaux | piecewise function | une formule sur chaque partie de l'ensemble de définition : $\max(0, x)$, la marche, $\lvert x \rvert$ | R3 |
| fonction duale | dual function | $D(\boldsymbol{\mu}, \boldsymbol{\lambda}) = \inf_{\mathbf{x}} \mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda})$ pour $\boldsymbol{\mu} \ge \mathbf{0}$ : toujours concave, elle minore le minimum du problème | M13b |
| fonction quantile | quantile function | la réciproque $F^{-1}$ de la fonction de répartition : $F^{-1}(u) = q_u$ | M02a, M02b |
| fonction signe | sign function | $\operatorname{sign}(x)$ vaut $-1$, 0 ou 1 selon que $x$ est négatif, nul ou positif | R2 |
| forme canonique | vertex form, completed-square form | $a(x - \alpha)^2 + \beta$, qui montre le sommet d'une parabole | R3 |
| forme canonique (d'un séparateur) | canonical form | un séparateur dont la plus petite marge fonctionnelle vaut 1 ; sa marge géométrique est alors $\frac{1}{\lVert \mathbf{w} \rVert}$ | M10 |
| forme d'une matrice | shape | le couple (nombre de lignes, nombre de colonnes), lignes d'abord : $(n, p)$ pour un dataset de $n$ exemples à $p$ features | M09a |
| forme échelonnée, forme échelonnée réduite | row echelon form, reduced row echelon form | un escalier : les lignes nulles en bas, chaque pivot à droite de celui du dessus ; réduite : chaque pivot vaut 1 et est seul dans sa colonne (elle est unique) | M09a |
| forme indéterminée | indeterminate form | $\infty - \infty$, $\frac{\infty}{\infty}$, $0 \times \infty$, $\frac{0}{0}$ : une limite qui ne se décide pas d'avance | R7 |
| forme quadratique | quadratic form | $\mathbf{w}^\top\mathbf{A}\mathbf{w} = \sum_{i,j} a_{ij}w_iw_j$, de gradient $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ ; on l'écrit avec une matrice symétrique, et dans la base de ses vecteurs propres elle devient $\sum_i \lambda_iy_i^2$ : ses lignes de niveau sont des ellipses quand $\mathbf{A}$ est définie positive | M09b, M12c |
| formule d'Al-Kashi | law of cosines | $c^2 = a^2 + b^2 - 2ab\cos\hat{C}$ dans un triangle quelconque : Pythagore corrigé par l'angle | R9 |
| formule de Bayes | Bayes' theorem | $P(H \mid O) = \frac{P(O \mid H)\,P(H)}{P(O)}$ : a posteriori = vraisemblance × a priori / évidence | M04 |
| formule de Cramer | Cramer's rule | la solution d'un système de déterminant non nul, écrite comme quotients de déterminants | R2 |
| fraction irréductible | irreducible fraction, fraction in lowest terms | fraction dont numérateur et dénominateur n'ont plus d'autre diviseur commun que 1 | R1 |
| fréquence | (relative) frequency | nombre de fois où un événement se réalise, divisé par le nombre d'essais | R8 |
| fréquentiste, bayésien | frequentist, Bayesian | deux lectures des probabilités : une fréquence à long terme, le paramètre étant fixe ; un degré de croyance sur le paramètre | M04 |
| frontière de décision linéaire | linear decision boundary | l'hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ qui sépare les points classés 1 de ceux classés 0 par un score linéaire | M07 |
| gain d'information | information gain | la baisse moyenne d'entropie de la classe $Y$ quand on apprend une variable $X$ : $H(Y) - H(Y \mid X)$, l'information mutuelle de $X$ et $Y$ ; un arbre de décision choisit la question qui la rend la plus grande | M13a |
| Gauss-Jordan (méthode de) | Gauss-Jordan elimination | réduire $[\mathbf{A} \mid \mathbf{I}]$ en forme échelonnée réduite : on obtient $[\mathbf{I} \mid \mathbf{A}^{-1}]$, ou une ligne nulle à gauche si $\mathbf{A}$ est singulière | M09a |
| générateur pseudo-aléatoire, graine | pseudo-random number generator, seed | programme qui calcule une suite d'apparence aléatoire à partir d'une graine ; la même graine redonne la même suite | R8 |
| génératif, discriminant (modèle) | generative, discriminative model | un modèle génératif modélise la loi des features dans chaque classe et la proportion des classes, puis applique la formule de Bayes (Naïve Bayes) ; un modèle discriminant modélise directement la classe sachant les features (régression logistique) | M13a |
| gradient | gradient | vecteur des dérivées partielles | M05b |
| gradient bon marché (principe du) | cheap gradient principle | le gradient d'une fonction réelle coûte, en mode inverse, un petit multiple du coût de la fonction, quel que soit le nombre de variables (Baur et Strassen, 1983) | M18 |
| gradient conjugué | conjugate gradient | méthode itérative pour $\mathbf{A}\mathbf{x} = \mathbf{b}$, $\mathbf{A}$ symétrique définie positive (Hestenes et Stiefel, 1952) : au plus $n$ itérations en arithmétique exacte, de l'ordre de $\sqrt\kappa$ en pratique (`scipy.sparse.linalg.cg`) | M19 |
| gradient estimé sur un échantillon | stochastic gradient estimate | $\frac1B\sum_j\nabla f_{K_j}$, avec $B$ indices tirés au hasard parmi les $N$ termes d'une moyenne : sans biais, de variance $\sigma^2/B$ (le gradient d'un mini-batch) | M19 |
| gradient fonctionnel | functional gradient | le gradient d'une loss par rapport au vecteur $\mathbf{F}$ des prédictions sur les exemples (une coordonnée par exemple) ; ajouter à l'ensemble $\alpha\,h$, avec $\mathbf{h}$ d'angle aigu avec $-\nabla_{\mathbf{F}}\mathcal{L}$ et $\alpha$ petit, fait baisser la loss au premier ordre | M14 |
| gradient par rapport à une matrice | gradient with respect to a matrix | le tableau des $\frac{\partial f}{\partial X_{ij}}$, de la forme de $\mathbf{X}$ (NumPy, workbookIA) ; $f(\mathbf{X} + \mathbf{H}) \approx f(\mathbf{X}) + \sum_{ij}G_{ij}H_{ij}$ | M18 |
| graine | seed | la tangente donnée aux entrées au départ d'une passe directe ($\dot{x}_i = 1$, les autres 0), ou l'adjoint donné à la sortie au départ d'une passe arrière ($\bar{y} = 1$) | M18 |
| Gram-Schmidt (procédé de) | Gram-Schmidt orthogonalization | retirer de chaque vecteur ses projections sur les vecteurs déjà construits, puis normer : une base orthonormée du même sous-espace ; classique ou modifié selon que l'on projette le vecteur d'origine ou le vecteur courant | M12b |
| grand O | big O | $f = O(g)$ : $f$ ne croît pas plus vite que $g$, à une constante près ; mesure le coût d'un algorithme | R7 |
| graphe de calcul | computation graph | un nœud par entrée et par résultat d'opération élémentaire, une arête $u \to w$ quand l'opération qui calcule $w$ utilise $u$ ; il est sans cycle | M18 |
| graphe orienté, graphe orienté sans cycle (DAG) | directed graph, directed acyclic graph (DAG) | des nœuds reliés par des arêtes qui ont un sens ; sans cycle si aucun chemin ne revient à son départ, ce qui équivaut à une matrice d'adjacence nilpotente | M16 |
| Hadamard (produit de) | Hadamard product, element-wise product | $\mathbf{A} \odot \mathbf{B}$, les produits des éléments de même position (`A * B` en NumPy) ; même forme, commutatif | M09a |
| Hedge (algorithme) | Hedge, exponential weights algorithm | les poids $w_t[k] \propto e^{-\eta L_t[k]}$ sur $K$ experts, $L_t[k]$ leur loss cumulée ; regret au plus $\frac{\ln K}{\eta} + \frac{\eta T}{8}$, soit $\sqrt{T\ln K/2}$ avec le meilleur $\eta$ | M14 |
| hérédité, initialisation | inductive step, base case | les deux étapes d'une récurrence : $P(n) \Rightarrow P(n + 1)$, et $P(n_0)$ | R4 |
| hessienne | Hessian | matrice des dérivées secondes, $H_{ij} = \frac{\partial^2 f}{\partial x_i\partial x_j}$, la jacobienne du gradient ; symétrique, elle a des valeurs propres réelles, les courbures extrêmes : définie positive en un point critique, c'est un minimum local ; semi-définie positive partout, la fonction est convexe | M05b, M12c, M19 |
| hinge loss | hinge loss | $\max(0, 1 - t)$, avec $t = y\,s$ la marge fonctionnelle : convexe, nulle dès $t \ge 1$, au moins égale à l'erreur 0-1 ; la loss de la SVM à marge souple | M13b |
| Hoeffding (inégalité de) | Hoeffding's inequality | pour $n$ variables indépendantes à valeurs dans $[a, b]$ : $P(\lvert \bar{X} - \mu \rvert \ge t) \le 2e^{-2nt^2/(b - a)^2}$ | M11 |
| homogénéité (d'une norme) | absolute homogeneity | $\lVert \lambda\mathbf{x} \rVert = \lvert \lambda \rvert\,\lVert \mathbf{x} \rVert$ : multiplier un vecteur par $\lambda$ multiplie sa longueur par $\lvert \lambda \rvert$ | M07 |
| hyperplan | hyperplane | les $\mathbf{x}$ de $\mathbb{R}^n$ tels que $\mathbf{w} \cdot \mathbf{x} + b = 0$, avec $\mathbf{w} \ne \mathbf{0}$ (le vecteur normal) : une droite du plan, un plan de l'espace | M07 |
| hyperplan séparateur | separating hyperplane | un hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ tel que chaque classe est dans l'un des deux demi-espaces ouverts : $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) > 0$ pour tout $i$ | M10 |
| hypothèse nulle, hypothèse alternative | null hypothesis, alternative hypothesis | $H_0$, souvent « pas d'effet », que le test cherche à mettre en défaut ; $H_1$, ce qu'on veut montrer ; toutes deux fixées avant de voir les données | M08 |
| idempotente (matrice) | idempotent matrix | $\mathbf{H}\mathbf{H} = \mathbf{H}$ : l'appliquer deux fois ne change rien, comme une projection ; idempotente et symétrique, c'est une projection orthogonale | M09b, M12b |
| identité remarquable | special product, algebraic identity | égalité vraie pour tous $a$ et $b$, comme $(a + b)^2 = a^2 + 2ab + b^2$ | R2 |
| image (d'une application linéaire) | image, range | $\operatorname{Im} f = \{f(\mathbf{x})\}$, un sous-espace de l'espace d'arrivée ; pour une matrice, l'espace de ses colonnes | M12a |
| implication | implication, conditional | $P \Rightarrow Q$, fausse seulement si P est vraie et Q fausse | R4 |
| importance par permutation | permutation importance | le score d'un modèle entraîné, moins son score quand on mélange la colonne d'une feature, sur un jeu de validation | M08 |
| impureté | impurity | une mesure du mélange des classes d'un groupe : nulle si une seule classe est présente, maximale pour des classes en proportions égales ; l'entropie et l'indice de Gini en sont deux | M13a |
| imputation | imputation | remplacer une valeur manquante par une valeur choisie (la moyenne, la médiane de la colonne…) | M02c |
| inclusion | inclusion, subset | $A \subset B$ : tout élément de $A$ est dans $B$ | R4 |
| indépendance (de variables aléatoires) | independence | la loi jointe est le produit des marginales : $P(X = x, Y = y) = P(X = x)\,P(Y = y)$ pour toutes les valeurs | M02b |
| indépendance conditionnelle | conditional independence | $X$ et $Y$ sont indépendantes sachant $Z$ si $P(X, Y \mid Z) = P(X \mid Z)\,P(Y \mid Z)$ ; des variables très corrélées peuvent l'être (deux thermomètres sachant la température) | M13a |
| indépendance deux à deux, mutuelle | pairwise, mutual independence | chaque paire d'événements est indépendante ; ou tous ensemble le sont : $P(A \cap B \cap C) = P(A)P(B)P(C)$ en plus. La première n'entraîne pas la seconde | M03 |
| indicatrice | indicator (variable) | variable qui vaut 1 si un événement se produit, 0 sinon (une Bernoulli) | M02b |
| indice (d'un point selle) | index (of a critical point) | le nombre de valeurs propres négatives de la hessienne : le nombre de directions indépendantes où la fonction descend | M19 |
| indice (d'une somme) | index (of a sum) | la variable muette de $\sum_{k=m}^{n}$, qui va de $m$ à $n$ | R4 |
| indice de Gini | Gini impurity, Gini index | $G(\mathbf{p}) = 1 - \sum_k p_k^2 = \sum_k p_k(1 - p_k)$, la somme des variances des indicatrices de classe ; entre 0 (une classe) et $1 - \frac{1}{K}$ (loi uniforme), concave | M13a |
| inégalité de Cauchy-Schwarz | Cauchy-Schwarz inequality | $\lvert \vec{u} \cdot \vec{v} \rvert \le \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert$ | R9, M07 |
| inégalité de Gibbs | Gibbs' inequality | $\mathrm{KL}(p \parallel q) \ge 0$, avec égalité si et seulement si $p = q$ ; d'où $H(p, q) \ge H(p)$ | M06 |
| inégalité de Jensen | Jensen's inequality | pour $f$ convexe, $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$ ; l'inverse pour $f$ concave | M06 |
| inégalité de Kraft | Kraft inequality, Kraft-McMillan inequality | les longueurs $\ell_i$ d'un code préfixe binaire vérifient $\sum 2^{-\ell_i} \le 1$, et des longueurs qui la vérifient sont celles d'un code préfixe | M06 |
| inégalité de Pinsker | Pinsker's inequality | pour deux lois de Bernoulli, $\mathrm{KL}(a \Vert p) \ge 2(a - p)^2$ (en nats) : la borne de Chernoff fait au moins aussi bien que celle de Hoeffding | M14 |
| inégalité triangulaire | triangle inequality | $\lVert \vec{u} + \vec{v} \rVert \le \lVert \vec{u} \rVert + \lVert \vec{v} \rVert$ : un côté d'un triangle est plus court que la somme des deux autres | R9, M07 |
| inégalité, inéquation | inequality | comparaison avec $<$, $\le$, $>$ ou $\ge$ ; une inéquation est une inégalité qui contient une inconnue | R2 |
| inertie (d'un nuage de points) | inertia, within-cluster sum of squares | $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2$ : la plus petite au barycentre ; ce que k-means fait baisser | M07 |
| information (de Shannon), surprise | self-information, surprisal, information content | $-\log_2 p$ bits : ce qu'apprend un événement de probabilité $p$ ; s'additionne pour des événements indépendants | M06 |
| information complète | full information | le cadre où l'on voit, après chaque tour, la loss de **toutes** les options (les experts de Hedge) ; un bandit ne voit que celle de l'option choisie | M14 |
| information mutuelle | mutual information | $I(X ; Y) = H(X) - H(X \mid Y)$ : ce que l'une des variables apprend sur l'autre ; symétrique, nulle seulement pour des variables indépendantes | M06 |
| injective, surjective, bijective | injective, surjective, bijective | deux vecteurs distincts ont des images distinctes ($\ker f = \{\mathbf{0}\}$) ; tout vecteur d'arrivée est atteint ($\operatorname{Im} f = W$) ; les deux | M12a |
| intégrale | integral | $\int_a^b f(x)\,dx$ : l'aire algébrique entre la courbe et l'axe, limite des sommes de Riemann | M02a |
| intégrale de Gauss | Gaussian integral | $\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt{\pi}$ | M02a |
| intégrale double | double integral | le volume sous une surface $z = f(x, y)$ au-dessus d'une région ; sur un rectangle, on intègre une variable après l'autre | M02b |
| intégrale impropre | improper integral | intégrale sur un intervalle infini, ou d'une fonction non bornée, définie comme une limite ; elle converge ou diverge | M02a |
| intégration par parties | integration by parts | $\int_a^b u\,v' = [uv]_a^b - \int_a^b u'\,v$ | M02a |
| intérêts composés | compound interest | les intérêts de chaque période rapportent à leur tour : $C_n = C_0\,(1 + t)^n$ ; versés $n$ fois par an au taux annuel $r$, le capital est multiplié en un an par $\left(1 + \frac{r}{n}\right)^n$, au plus $e^r$ (les intérêts composés en continu, *continuous compounding*) | R5, R6, M14 |
| intersection, réunion | intersection, union | $A \cap B$ : les éléments à la fois dans $A$ et dans $B$ ; $A \cup B$ : ceux qui sont dans l'un ou dans l'autre | R2, R4 |
| intervalle de confiance | confidence interval | intervalle calculé sur les données qui contient la vraie valeur pour 95 % (le niveau) des échantillons : $\bar{x} \pm 1{,}96\,\frac{s}{\sqrt{n}}$ | M02c |
| intervalle de crédibilité | credible interval | un intervalle qui contient le paramètre avec une probabilité donnée, selon l'a posteriori | M04 |
| intervalle de prédiction | prediction interval | intervalle où tombera une **nouvelle** observation ; plus large qu'un intervalle de confiance de la moyenne | M02c |
| intervalle de Wald, de Wilson | Wald interval, Wilson (score) interval | deux intervalles d'une proportion : $\hat{p} \pm z\sqrt{\hat{p}(1 - \hat{p})/n}$, faux avec peu de succès ; celui de Wilson, qui inverse un test, reste dans $[0, 1]$ | M08 |
| inverse d'une matrice | inverse matrix | la matrice $\mathbf{A}^{-1}$ telle que $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$ ; unique quand elle existe, seulement pour une matrice carrée | M09a |
| issue | outcome | un résultat possible d'une expérience aléatoire | R8 |
| itération de Richardson | Richardson iteration | $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega(\mathbf{b} - \mathbf{A}\mathbf{x}_k)$ pour résoudre $\mathbf{A}\mathbf{x} = \mathbf{b}$ ; converge pour $0 < \omega < 2/\lambda_{\max}$ si $\mathbf{A}$ est symétrique définie positive ; une descente de gradient sur $\frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$ | M19 |
| itération linéaire | linear (affine) iteration, fixed-point iteration | $\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$ ; l'écart au point fixe est multiplié par $\mathbf{M}$ ; pour $\mathbf{M}$ symétrique, elle converge depuis tout départ si et seulement si toutes les valeurs propres sont de module $< 1$ | M19 |
| Jacobi (méthode de) | Jacobi method | résoudre chaque équation $i$ en $x_i$, les autres inconnues gardant leur ancienne valeur : $\mathbf{x} \leftarrow \mathbf{x} + \mathbf{D}^{-1}(\mathbf{b} - \mathbf{A}\mathbf{x})$ ; c'est Richardson après le préconditionnement diagonal | M19 |
| jacobienne | Jacobian | la matrice $(m, n)$ des dérivées partielles d'une application de $\mathbb{R}^n$ dans $\mathbb{R}^m$, $J_{ij} = \frac{\partial f_i}{\partial x_j}$ : une ligne par sortie, une colonne par entrée (*numerator layout*) ; la meilleure approximation linéaire, $\mathbf{f}(\mathbf{x} + \mathbf{h}) \approx \mathbf{f}(\mathbf{x}) + \mathbf{J}\mathbf{h}$ ; $\lvert\det\mathbf{J}\rvert$ est le facteur local de changement d'aire | M17 |
| k-means, k-means++ | k-means, k-means++ | regrouper des points en $k$ clusters en alternant l'affectation au centre le plus proche et le remplacement de chaque centre par le barycentre de son cluster ; k-means++ tire les centres de départ avec une probabilité proportionnelle à $D^2$ | M07 |
| König-Huygens (formule de) | König-Huygens theorem | $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2 + m\,\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$ | M07 |
| lagrangien | Lagrangian | $\mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_i \mu_i g_i(\mathbf{x}) + \sum_j \lambda_j h_j(\mathbf{x})$, l'objectif plus chaque contrainte multipliée par son multiplicateur | M13b |
| lasso | lasso | les moindres carrés pénalisés par $\lambda\lVert \mathbf{w} \rVert_1$ : des poids exactement nuls, pas de solution explicite en général | M09b |
| levier | leverage | $h_{ii}$, le nombre de la diagonale de la matrice chapeau : le poids de $y_i$ dans sa propre prédiction ; grand pour un point isolé | M09b |
| ligne de niveau | level curve, contour line | l'ensemble des points où $f(x, y)$ prend une valeur donnée $c$ ; une carte de lignes de niveau est une carte topographique de la surface | M05b |
| limite à droite, à gauche | right-hand, left-hand limit | limite quand $x$ s'approche de $a$ en restant plus grand (plus petit) que $a$ | R7 |
| limite d'une fonction | limit of a function | la valeur dont $f(x)$ s'approche quand $x$ tend vers $a$ ou vers $\pm\infty$ | R7 |
| limite d'une suite | limit of a sequence | le nombre $\ell$ dont les termes finissent par rester aussi près qu'on veut | R5 |
| linéairement séparable | linearly separable | deux classes qu'un hyperplan sépare ; pour des nuages finis, c'est équivalent à des enveloppes convexes disjointes | M10 |
| linéarité de l'espérance | linearity of expectation | $\mathbb{E}[aX + bY + c] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y] + c$, même pour des variables dépendantes | R8, M02b |
| lissage de Laplace | Laplace smoothing, additive smoothing | $\frac{k + 1}{n + 2}$, ou $\frac{n_j + 1}{n + K}$ : la moyenne a posteriori sous un a priori uniforme ; plus de probabilité nulle | M04 |
| log-loss | log-loss, binary cross-entropy | $-\frac{1}{n}\sum_i\big[y_i\ln\hat{p}_i + (1 - y_i)\ln(1 - \hat{p}_i)\big]$, moins la log-vraisemblance des labels divisée par $n$ ; avec les scores, la moyenne des $s(z_i) - y_iz_i$ ; elle est la plus petite, en moyenne, quand le modèle annonce les vraies probabilités | M06, M13a |
| log-probabilité, log-vraisemblance | log-probability, log-likelihood | le logarithme d'une probabilité, d'une vraisemblance : un produit devient une somme | R6, M06 |
| log-sum-exp | log-sum-exp | $\ln\sum_j e^{\ell_j} = m + \ln\sum_j e^{\ell_j - m}$ avec $m = \max_j \ell_j$ : normaliser des log-probabilités sans underflow ; un maximum lisse, convexe (sur une droite, sa dérivée seconde est une variance) | M04, M05a, M13a |
| logarithme décimal, binaire | common logarithm, binary logarithm | $\log_{10}$ (compte les chiffres), $\log_2$ (compte les doublements, les bits) | R6 |
| logarithme népérien | natural logarithm | $\ln$, la réciproque de exp : $\ln x$ est l'exposant $y$ tel que $e^y = x$ ; « log » en ML et en Python | R6 |
| logit | logit | $\ln \frac{p}{1 - p}$, la réciproque de la sigmoïde ; en deep learning, les scores avant la sigmoïde ou le softmax | R6 |
| loi (de probabilité) | (probability) distribution | façon dont une variable aléatoire répartit ses valeurs | R8, M02b |
| loi Beta | Beta distribution | la loi sur $[0, 1]$ de densité $\frac{\theta^{a - 1}(1 - \theta)^{b - 1}}{B(a, b)}$, de moyenne $\frac{a}{a + b}$ : la loi d'une proportion | M04 |
| loi binomiale | binomial distribution | le nombre de succès en $n$ essais indépendants de probabilité $p$ : $\binom{n}{k}p^k(1-p)^{n-k}$ | M02b |
| loi catégorielle (multinoulli) | categorical distribution | une classe parmi $K$, de probabilités $p_1, \ldots, p_K$ de somme 1 | M02b |
| loi de Bernoulli | Bernoulli distribution | vaut 1 avec la probabilité $p$, 0 sinon ; espérance $p$, variance $p(1 - p)$ | M02b |
| loi de Boltzmann | Boltzmann distribution | $p_i = \frac{e^{-E_i/T}}{Z}$ pour des niveaux d'énergie $E_i$ à la température $T$ : l'origine des énergies est arbitraire ; tout sur le niveau le plus bas quand $T \to 0$, uniforme quand $T \to \infty$ | M17 |
| loi de Poisson | Poisson distribution | le nombre d'événements rares sur une durée : $e^{-\lambda}\frac{\lambda^k}{k!}$, d'espérance et de variance $\lambda$ | M02b |
| loi des grands nombres | law of large numbers | sur des répétitions indépendantes, la fréquence d'un événement se rapproche de sa probabilité | R8, M02c |
| loi empirique | empirical distribution | la loi qui met la probabilité $\frac{1}{n}$ sur chacune des $n$ valeurs observées | M02c |
| loi exponentielle | exponential distribution | densité $\lambda e^{-\lambda t}$ sur $[0 ; +\infty[$ : une durée d'attente sans mémoire, d'espérance $\frac{1}{\lambda}$ | M02b |
| loi faible des grands nombres | weak law of large numbers | pour tout $t > 0$, $P(\lvert \bar{X}_n - \mu \rvert \ge t) \to 0$ ; Tchebychev la démontre : $\le \frac{\sigma^2}{nt^2}$ | M02c, M11 |
| loi géométrique | geometric distribution | le rang du premier succès : $(1 - p)^{k-1}p$ pour $k \ge 1$, d'espérance $\frac{1}{p}$ | M02b |
| loi jointe | joint distribution | la loi d'un couple : $P(X = x, Y = y)$ pour toutes les paires de valeurs | M02b |
| loi marginale | marginal distribution | la loi d'une seule variable d'un couple, obtenue en sommant (ou en intégrant) l'autre | M02b |
| loi normale (gaussienne) | normal (Gaussian) distribution | loi en cloche $\mathcal{N}(\mu, \sigma^2)$, de centre $\mu$ et d'écart-type $\sigma$ (le second paramètre est la variance) | M02b |
| loi normale centrée réduite | standard normal distribution | $\mathcal{N}(0, 1)$, de densité $\varphi$ et de fonction de répartition $\Phi$ | M02b |
| loi nulle | null distribution | la loi de la statistique de test quand $H_0$ est vraie | M08 |
| loi prédictive (a posteriori) | posterior predictive distribution | la loi des prochaines observations, sachant les données, en moyennant sur le paramètre | M04 |
| loi uniforme | uniform distribution | densité constante $\frac{1}{b - a}$ sur $[a ; b]$ : une probabilité proportionnelle à la longueur | M02b |
| lois de De Morgan | De Morgan's laws | non (P et Q) = (non P) ou (non Q) ; non (P ou Q) = (non P) et (non Q) | R4 |
| longueur moyenne (d'un code) | expected code length | $\bar{L} = \sum p_i \ell_i$ ; pour un code préfixe, $\bar{L} \ge H$, et le meilleur code vérifie $\bar{L} < H + 1$ | M06 |
| loss de Huber | Huber loss | $\frac{r^2}{2}$ si $\lvert r \rvert \le \delta$, $\delta(\lvert r \rvert - \frac{\delta}{2})$ sinon : quadratique pour les petits résidus, linéaire pour les grands, dérivable partout | M09b |
| loss exponentielle | exponential loss | $e^{-yF}$ pour un label $y \in \{-1, +1\}$ et un score $F$ ; sa dérivée en $F$ vaut $-y\,e^{-yF}$, et ses valeurs normalisées sont des poids exponentiels sur les exemples | M14 |
| MAE | mean absolute error (MAE) | $\frac{1}{n}\sum \lvert r_i \rvert$, l'erreur absolue moyenne d'une régression, dans l'unité de la cible | M09b |
| mal conditionné | ill-conditioned | se dit d'un problème dont la solution change beaucoup quand les données changent un peu | R2 |
| malédiction de la dimension | curse of dimensionality | les surprises de la grande dimension : le volume se concentre près du bord, les distances se ressemblent | M02c, M07 |
| mantisse | significand, mantissa | le nombre $m$ de la notation scientifique $m \times 10^k$, avec $1 \le |m| < 10$ | R1 |
| MAP (maximum a posteriori) | maximum a posteriori (MAP) estimate | la valeur du paramètre qui maximise l'a posteriori : son mode | M04 |
| marche (fonction de Heaviside) | step function, Heaviside function | vaut 0 avant 0 et 1 après ; la valeur en 0 est une convention ; voir aussi « seuil (fonction) » | R3 |
| marge dure, marge souple | hard margin, soft margin | la SVM qui exige $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ pour tous les exemples, ou celle qui relâche chaque contrainte en $\ge 1 - \xi_i$ ($\xi_i \ge 0$) et ajoute $C\sum_i \xi_i$ à l'objectif (forme équivalente : la hinge loss) | M13b |
| marge fonctionnelle | functional margin | $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ pour un point ; elle est multipliée par $c$ quand on multiplie $(\mathbf{w}, b)$ par $c$ | M10 |
| marge géométrique | geometric margin | $\min_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$ : la distance signée du point le plus mal placé à l'hyperplan ; la plus grande possible vaut la moitié de la distance entre les enveloppes convexes | M10 |
| Markov (inégalité de) | Markov's inequality | $P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$ pour une variable $X \ge 0$ et $a > 0$ | M02c, M11 |
| matrice | matrix | tableau de nombres à lignes et colonnes | M09a |
| matrice augmentée | augmented matrix | $[\mathbf{A} \mid \mathbf{b}]$, la matrice des coefficients suivie de la colonne des seconds membres, sur laquelle on fait le pivot de Gauss | M09a |
| matrice chapeau | hat matrix | $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, qui envoie $\mathbf{y}$ sur $\hat{\mathbf{y}}$ : symétrique, idempotente, de trace $p$ | M09b |
| matrice compagnon | companion matrix | $\begin{pmatrix} p & -q \\ 1 & 0 \end{pmatrix}$ pour $u_{k+2} = p\,u_{k+1} - q\,u_k$ : elle fait passer de $(u_{k+1}, u_k)$ à $(u_{k+2}, u_{k+1})$, et son polynôme caractéristique est celui de la récurrence | M19 |
| matrice d'adjacence | adjacency matrix | $A_{ij} = 1$ s'il y a une arête $i \to j$, 0 sinon (ou le poids de l'arête) ; ses puissances comptent les chemins | M16 |
| matrice d'une application linéaire | transformation matrix | la matrice dont la colonne $j$ contient les coordonnées de $f(\mathbf{b}_j)$ dans la base de l'arrivée ; dans les bases canoniques, $f(\mathbf{e}_j)$ | M12a |
| matrice de confusion | confusion matrix | le tableau de contingence de la vérité et de la prédiction d'un classifieur (TP, FN, FP, TN en binaire) | M03 |
| matrice de corrélation | correlation matrix | la matrice des corrélations $\rho_{ij} = \frac{\Sigma_{ij}}{\sigma_i\sigma_j}$, avec des 1 sur la diagonale | M02c |
| matrice de covariance | covariance matrix | $\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$ : les variances sur la diagonale, symétrique, et $\sum_i\sum_j w_iw_j\Sigma_{ij} = \mathbb{V}(\mathbf{w}^\top\mathbf{X}) \ge 0$ : semi-définie positive ; ses valeurs propres sont les variances le long de ses axes propres, leur somme la variance totale | M02c, M12c |
| matrice de Gram (d'un noyau) | Gram matrix, kernel matrix | la matrice $n \times n$ des $k(\mathbf{x}_i, \mathbf{x}_j)$ des exemples, symétrique et semi-définie positive ; pour le noyau linéaire, $\mathbf{X}\mathbf{X}^\top$ (M12c appelait matrice de Gram $\mathbf{X}^\top\mathbf{X}$, celle des colonnes) | M12c, M13b |
| matrice des features | feature matrix, design matrix | le tableau $\mathbf{X}$ de forme $(n, p)$ : une ligne par exemple, une colonne par feature ($\mathbf{X}$, ou $\boldsymbol{\Phi}$ après une transformation des features, dans MML) | M09b |
| matrice diagonale | diagonal matrix | une matrice carrée dont les nombres hors de la diagonale sont nuls ; elle s'inverse nombre par nombre | M09a |
| matrice identité | identity matrix | $\mathbf{I}_n$ : des 1 sur la diagonale, des 0 ailleurs ; $\mathbf{I}\mathbf{A} = \mathbf{A}\mathbf{I} = \mathbf{A}$ | M09a |
| matrice inversible, singulière | invertible (regular, nonsingular) matrix, singular matrix | une matrice carrée qui a une inverse, ou qui n'en a pas (quand une colonne combine les autres, ou que le rang est plus petit que la taille) | M09a |
| matrice orthogonale | orthogonal matrix | une matrice carrée à colonnes orthonormées : $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$, $\mathbf{Q}^{-1} = \mathbf{Q}^\top$ ; elle conserve produits scalaires, normes et distances (rotations, symétries, permutations) | M12b |
| matrice symétrique | symmetric matrix | une matrice égale à sa transposée : $a_{ij} = a_{ji}$ ; $\mathbf{X}^\top\mathbf{X}$ l'est toujours | M09a |
| matrice symétrique définie positive | symmetric positive definite matrix | $\mathbf{M}^\top = \mathbf{M}$ et $\mathbf{x}^\top\mathbf{M}\mathbf{x} > 0$ pour $\mathbf{x} \ne \mathbf{0}$ : exactement les matrices des produits scalaires de $\mathbb{R}^n$ ; en dimension 2, $a > 0$ et $ac - b^2 > 0$ ; ses valeurs propres sont toutes strictement positives, ses mineurs principaux aussi, et elle a une décomposition de Cholesky | M12b, M12c |
| matrices semblables, équivalentes | similar matrices, equivalent matrices | $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$, ou $\mathbf{T}^{-1}\mathbf{A}\mathbf{S}$ : la même application linéaire dans d'autres bases ; le rang ne change pas, et deux matrices semblables ont aussi le même déterminant, la même trace et les mêmes valeurs propres | M12a, M12c |
| maximum de vraisemblance (estimation du) | maximum likelihood estimate (MLE) | la valeur du paramètre qui rend les données observées les plus probables, en maximisant la log-vraisemblance $\ell(\theta) = \sum_i \ln p(x_i \mid \theta)$ : la proportion pour une loi de Bernoulli, les fréquences pour une loi catégorielle, la moyenne et la variance en $\frac{1}{n}$ (biaisée) pour une loi normale | M04, M13a |
| maximum, minimum, extremum | maximum, minimum, extremum (extrema) | la plus grande (petite) valeur d'une fonction sur un ensemble | R3 |
| MCC (coefficient de Matthews) | Matthews correlation coefficient | la corrélation entre la vérité et la prédiction codées 0 et 1, entre $-1$ et 1 | M03 |
| médiane | median | la valeur du milieu d'une série triée (la moyenne des deux du milieu si $n$ est pair) ; robuste aux valeurs extrêmes | M02c |
| médiane géométrique | geometric median | le point qui minimise la somme des distances euclidiennes (non au carré) à des points ; sans formule, l'algorithme de Weiszfeld la calcule | M07 |
| mesures appariées | paired measurements | deux mesures de la même unité (avant et après) : on travaille sur leurs différences, et la variabilité entre unités disparaît | M08 |
| méthode de Chernoff | Chernoff method | appliquer Markov à $e^{\lambda X}$, puis choisir le meilleur $\lambda$ : d'où les bornes exponentielles, comme celle de Hoeffding | M11 |
| méthode de la puissance | power iteration, power method | $\mathbf{x}_{k+1} = \mathbf{A}\mathbf{x}_k/\lVert \mathbf{A}\mathbf{x}_k \rVert$ : converge vers le vecteur propre de la valeur propre de plus grand module, l'écart étant multiplié par $\lvert\lambda_2/\lambda_1\rvert$ à chaque pas ; seulement des produits matrice-vecteur | M12c |
| méthode de Monte-Carlo | Monte Carlo method | estimer une probabilité, une espérance ou une intégrale par la moyenne d'un grand nombre de tirages au hasard | M02a |
| méthode de Newton | Newton's method, Newton-Raphson | $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$ : suivre la tangente jusqu'à l'axe pour approcher une racine | M05a |
| méthode de Simpson | Simpson's rule | intégration numérique par des paraboles : $\frac{h}{3}(f_0 + 4f_1 + 2f_2 + \cdots + 4f_{n-1} + f_n)$, $n$ pair ; erreur en $h^4$ | M02a |
| méthode des trapèzes | trapezoidal rule | intégration numérique par des segments : $h\big(\frac{f_0}{2} + f_1 + \cdots + \frac{f_n}{2}\big)$ ; erreur en $h^2$ | M02a |
| milieu (d'un segment) | midpoint | le point dont les coordonnées sont les moyennes de celles des extrémités | R9 |
| mineurs principaux (critère de Sylvester) | leading principal minors (Sylvester's criterion) | les déterminants des sous-matrices en haut à gauche, $1 \times 1$ à $n \times n$ ; une matrice symétrique est définie positive si et seulement si ils sont tous strictement positifs | M12c |
| mise à jour séquentielle | sequential updating | l'a posteriori d'une observation devient l'a priori de la suivante | M04 |
| mise en équation | setting up an equation, translating a word problem | traduire un énoncé en équation (ou en système) en choisissant les inconnues | R2 |
| mode | mode | la valeur la plus fréquente d'une série, ou le maximum d'une densité | M02c |
| mode direct, mode inverse | forward mode, reverse mode | deux façons de faire passer un vecteur à travers une suite de jacobiennes sans les multiplier entre elles : de droite à gauche par des produits jacobienne-vecteur, de gauche à droite par des produits vecteur-jacobienne (la rétropropagation, M18) ; sur un graphe de calcul, le mode direct pousse des tangentes des entrées vers la sortie, le mode inverse des adjoints de la sortie vers les entrées | M17, M18 |
| modèle linéaire généralisé | generalized linear model (GLM) | une combinaison linéaire des features suivie d'une fonction fixée, $\varphi(\boldsymbol{\theta}^\top\mathbf{x})$, avec une loi de la cible adaptée : la régression linéaire (bruit gaussien) et la régression logistique (labels de Bernoulli) en sont | M13a |
| module (d'un nombre complexe) | modulus | $\lvert a + ib\rvert = \sqrt{a^2 + b^2}$ ; multiplicatif, $\lvert z^k\rvert = \lvert z\rvert^k$ ; les racines complexes de $r^2 - pr + q$ ont pour module $\sqrt q$ | M19 |
| modus ponens, modus tollens | modus ponens, modus tollens | les formes valides « $P \Rightarrow Q$ ; $P$ ; donc $Q$ » et « $P \Rightarrow Q$ ; non $Q$ ; donc non $P$ » | M11 |
| moindres carrés | least squares | choisir les poids qui minimisent la somme des carrés des résidus, $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ : la solution des équations normales, et le maximum de vraisemblance d'un bruit gaussien | M09b |
| monôme | monomial | un produit de puissances de variables, $x_1^{k_1}\cdots x_p^{k_p}$, de degré $k_1 + \cdots + k_p$ | M09b |
| moyenne (arithmétique) | mean | $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ : la somme des valeurs divisée par leur nombre | R1, M02c |
| moyenne exponentielle | exponential moving average (EMA) | $v_t = \beta\,v_{t-1} + (1 - \beta)\,x_t$ : une moyenne qui oublie le passé progressivement | R5 |
| moyenne harmonique | harmonic mean | inverse de la moyenne des inverses ; vitesse moyenne, score F1 | R1 |
| moyenne macro, micro, pondérée | macro, micro, weighted average | moyenne simple des classes ; mesure calculée sur les comptages additionnés ; moyenne pondérée par les effectifs | M03 |
| moyenne mobile | moving average | la moyenne des $k$ dernières valeurs, recalculée à chaque instant | R5 |
| moyenne pondérée | weighted mean, weighted average | $\frac{\sum w_i x_i}{\sum w_i}$ : chaque valeur compte selon son poids | R1 |
| MSE, RMSE (d'une régression) | mean squared error, root mean squared error | $\frac{1}{n}\sum r_i^2$ (dans l'unité de la cible au carré) et sa racine (dans l'unité de la cible) | M09b |
| multiplicateur de Lagrange | Lagrange multiplier | le coefficient d'une contrainte dans le lagrangien ; à l'optimum, le prix d'une unité de contrainte : $\frac{df^*}{dc} = -\lambda$ pour le lagrangien $f + \lambda(g - c)$ | M13b |
| multiplicité algébrique, multiplicité géométrique | algebraic multiplicity, geometric multiplicity | la multiplicité de $\lambda$ comme racine du polynôme caractéristique ; la dimension de son espace propre, toujours entre 1 et la multiplicité algébrique | M12c |
| Naïve Bayes | naive Bayes | un classifieur génératif qui suppose les features indépendantes sachant la classe : $P(Y = k \mid \mathbf{x}) \propto \pi_k\prod_j p(x_j \mid k)$, chaque loi estimée par maximum de vraisemblance (avec lissage), la décision en log-probabilités | M13a |
| négation | negation | la proposition « non P », vraie quand P est fausse | R4 |
| nier l'antécédent | denying the antecedent | le sophisme formel « $P \Rightarrow Q$ ; non $P$ ; donc non $Q$ » : non valide | M11 |
| nilpotente (matrice) | nilpotent matrix | une matrice carrée dont une puissance est nulle ; une matrice strictement triangulaire $n \times n$ vérifie $\mathbf{N}^n = \mathbf{0}$ ; ses valeurs propres sont toutes nulles | M16 |
| nombre complexe | complex number | $z = a + ib$ avec $i^2 = -1$ ; $a$ et $b$ sont ses parties réelle et imaginaire | M19 |
| nombre décimal | decimal number, terminating decimal | nombre qui s'écrit avec un nombre fini de chiffres après la virgule (ensemble 𝔻) | R1 |
| nombre dérivé | derivative at a point | $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$, la pente de la tangente en $a$ | R7 |
| nombre dual | dual number | $a + b\varepsilon$ avec $\varepsilon^2 = 0$ ; $f(a + \varepsilon) = f(a) + f'(a)\,\varepsilon$ : le mode direct de la différentiation automatique | M18 |
| nombre e | Euler's number | $e = \lim (1 + \frac{1}{n})^n \approx 2{,}718$, la base de l'exponentielle et de $\ln$ | R6 |
| nombre rationnel, irrationnel | rational, irrational number | quotient de deux entiers (ℚ) ; un réel qui n'en est pas un, comme $\sqrt{2}$ ou $\pi$ | R1 |
| normalisation min-max | min-max scaling | la fonction affine $\frac{x - \min}{\max - \min}$, qui ramène des données entre 0 et 1 | R3 |
| norme | norm | longueur d'un vecteur | R9, M07 |
| norme de Frobenius | Frobenius norm | $\lVert \mathbf{A} \rVert_F = \sqrt{\sum_{i,j} a_{ij}^2} = \sqrt{\operatorname{tr}(\mathbf{A}^\top\mathbf{A})}$, et $\lVert \mathbf{A} \rVert_F^2 = \sum s_i^2$ : l'« énergie » de la matrice | M12d |
| norme Lp | Lp norm, p-norm | $\big(\sum_i \lvert x_i \rvert^p\big)^{1/p}$, une norme pour $p \ge 1$ seulement ; elle diminue quand $p$ augmente, vers la norme L∞ | M07 |
| norme spectrale | spectral norm | $\lVert \mathbf{A} \rVert_2 = \max_{\mathbf{x} \ne \mathbf{0}}\lVert \mathbf{A}\mathbf{x} \rVert/\lVert \mathbf{x} \rVert = s_1$, le plus grand étirement ; pas la plus grande valeur propre en module, sauf pour une matrice symétrique | M12d |
| normes L1 et L∞ | L1 norm, infinity norm | $\sum \lvert x_i \rvert$ (un trajet fait seulement de pas horizontaux et verticaux) et $\max \lvert x_i \rvert$ ; sans indice, $\lVert \mathbf{x} \rVert$ est la norme euclidienne (L2) | R9, M07 |
| noyau (d'un notebook) | kernel | la mémoire qui exécute les cellules et garde leurs variables | R0 |
| noyau (d'une application linéaire) | kernel, null space | $\ker\mathbf{A} = \{\mathbf{x} : \mathbf{A}\mathbf{x} = \mathbf{0}\}$, un sous-espace de l'espace de départ : les directions que l'application écrase | M12a |
| noyau (d'une SVM) | kernel | une fonction $k(\mathbf{x}, \mathbf{z}) = \varphi(\mathbf{x}) \cdot \varphi(\mathbf{z})$ : symétrique, de matrices de Gram semi-définies positives ; linéaire, polynomial ou RBF | M13b |
| noyau polynomial | polynomial kernel | $(\mathbf{x} \cdot \mathbf{z} + c)^d$, avec $c \ge 0$ : le produit scalaire des monômes de degré au plus $d$ (pondérés), soit $\binom{p + d}{d}$ coordonnées pour $c > 0$ | M13b |
| noyau RBF, gaussien | RBF kernel, Gaussian kernel | $e^{-\gamma\lVert\mathbf{x} - \mathbf{z}\rVert^2}$, dans $]0, 1]$, fonction décroissante de la distance ; $1/\sqrt{\gamma}$ fixe son échelle de longueur ; son $\varphi$ a une infinité de coordonnées | M13b |
| numérateur, dénominateur | numerator, denominator | le nombre du haut et celui du bas d'une fraction | R1 |
| octet | byte | 8 bits ; 1 ko = $10^3$ octets, 1 Mo = $10^6$, 1 Go = $10^9$ | R1 |
| opérations élémentaires sur les lignes | elementary row operations | échanger deux lignes, multiplier une ligne par un nombre non nul, ajouter à une ligne un multiple d'une autre : elles ne changent pas les solutions | M09a |
| optimisme face à l'incertitude | optimism in the face of uncertainty | agir comme si chaque option valait le haut de son intervalle de confiance : le principe des stratégies UCB | M11 |
| oracle (d'un test) | test oracle | bibliothèque de confiance à laquelle un test compare ta fonction | R0 |
| ordre d'une méthode numérique | order of a numerical method | l'exposant $k$ d'une erreur proportionnelle à $h^k$ : diviser le pas par 2 divise l'erreur par $2^k$ | M02a |
| ordre de grandeur | order of magnitude | la puissance de 10 la plus proche d'un nombre | R1 |
| ordre topologique | topological order | une numérotation des nœuds d'un graphe sans cycle où chaque arête va d'un numéro à un plus grand ; la matrice d'adjacence renumérotée est strictement triangulaire supérieure | M16 |
| orthogonaux (vecteurs) | orthogonal vectors | de directions perpendiculaires : leur produit scalaire est nul | R9, M07 |
| overfitting, underfitting | overfitting, underfitting | un modèle trop souple, qui colle au bruit des données d'entraînement (grande variance) ; un modèle trop simple, qui rate la forme des données (grand biais) | M09b |
| p-valeur | p-value | la probabilité, calculée en supposant $H_0$ vraie, d'une statistique au moins aussi extrême que celle observée ; pas la probabilité que $H_0$ soit vraie | M08 |
| par colonne, par ligne | featurewise, samplewise | une opération sur chaque feature (la moyenne de chaque colonne, la standardisation) ; sur chaque exemple (la norme de chaque ligne) | M09a |
| parabole, sommet | parabola, vertex | la courbe d'un second degré ; son sommet $(\alpha, \beta)$ est son point le plus bas (ou le plus haut) | R3 |
| paradoxe de Simpson | Simpson's paradox | une tendance présente dans chaque groupe s'inverse quand on réunit les groupes, à cause de leurs poids différents | M03 |
| parcimonieux (modèle) | sparse model | un modèle dont beaucoup de poids sont exactement nuls, comme ceux du lasso | M09b |
| Parseval (égalité de) | Parseval's identity | dans une base orthonormée, $\lVert \mathbf{v} \rVert^2 = \sum_i c_i^2$, la somme des carrés des coordonnées | M12b |
| partie entière, plancher, plafond | floor, ceiling | $\lfloor x \rfloor$, le plus grand entier $\le x$ ; $\lceil x \rceil$, le plus petit entier $\ge x$ | R1 |
| partition (de l'univers) | partition | des événements deux à deux incompatibles dont la réunion est l'univers entier | M03 |
| pas critique | critical step size | $2/\lambda_{\max}$ : le plus grand pas pour lequel Richardson converge vers la solution depuis tout départ | M19 |
| pas optimal (de Richardson) | optimal step size | $\omega^\star = \frac{2}{\lambda_{\min} + \lambda_{\max}}$, qui donne le facteur $\frac{\kappa - 1}{\kappa + 1}$ par itération | M19 |
| passe avant, passe arrière | forward pass, backward pass | en mode inverse : le calcul des valeurs, qu'on garde, puis celui des adjoints, de la sortie vers les entrées | M18 |
| pavé | box | un produit d'intervalles $[l_1, u_1] \times \cdots \times [l_n, u_n]$ ; projeter dessus, c'est couper chaque coordonnée (`np.clip`), ce qui change la direction en général | M19 |
| pente, ordonnée à l'origine | slope, intercept | dans $mx + c$, $m$ est la variation pour $x + 1$, et $c = f(0)$ | R3 |
| percentile, quartile | percentile, quartile | le percentile $k$ est le quantile d'ordre $\frac{k}{100}$ ; les quartiles, les quantiles d'ordre 0,25, 0,5 et 0,75 | M02a |
| périodique, période | periodic, period | une fonction qui se répète : $f(x + T) = f(x)$ ; cos et sin ont pour période $2\pi$ | R9 |
| perplexité | perplexity | $2^{H}$, avec $H$ une entropie en bits : un nombre effectif de choix également probables ; pour un modèle de langue, $2^{H(p, q)}$, le nombre de mots entre lesquels il hésite en moyenne (M06) ; en t-SNE, $2^{H(P_i)}$ des probabilités de voisinage d'un point, un nombre effectif de voisins, que l'on fixe en réglant $\sigma_i$ (M12d) | M06, M12d |
| PGCD, PPCM | GCD (greatest common divisor), LCM (least common multiple) | plus grand diviseur commun, plus petit multiple commun de deux entiers | R1 |
| pivot | pivotal quantity | une fonction des données et du paramètre dont la loi ne dépend pas du paramètre ($\frac{\bar{X}}{\mu}$ pour une loi exponentielle) | M02c |
| pivot d'une forme échelonnée | pivot, leading coefficient | le premier nombre non nul d'une ligne ; le rang est le nombre de pivots | M09a |
| pivot de Gauss (élimination de Gauss) | Gaussian elimination | annuler les inconnues colonne par colonne par des opérations élémentaires (une forme échelonnée), puis remonter de la dernière équation à la première | M09a |
| pivot partiel | partial pivoting | prendre pour pivot, dans chaque colonne, l'élément de plus grande valeur absolue (en échangeant les lignes) : évite d'amplifier les erreurs d'arrondi | M09a |
| plan tangent | tangent plane | $z = f(a, b) + f_x(a, b)\,(x - a) + f_y(a, b)\,(y - b)$ : le plan qui touche la surface en un point, avec les mêmes pentes | M05b |
| plancher de variance | variance floor | la part de la variance d'une moyenne de $M$ prédictions qui ne baisse pas quand $M$ grandit ; avec $X_i = a_iZ + E_i$, elle vaut $\bar{a}^2\,\mathbb{V}(Z)$, et seules les covariances la fixent | M14 |
| plus proche voisin | nearest neighbor | le point d'un ensemble le plus proche d'un point donné ; il dépend de la distance choisie et des unités des features | M07 |
| poids exponentiels, poids multiplicatifs | exponential weights, multiplicative weights | des poids proportionnels à $e^{-\eta L}$ ; à chaque tour, chacun est multiplié par $e^{-\eta\ell}$ (ou par $1 - \eta\ell$, presque pareil pour $\eta$ petit), puis tous sont renormalisés | M14 |
| point anguleux | kink, corner | un point où une fonction continue change brusquement de pente : elle y a une dérivée à gauche et une dérivée à droite différentes | M17 |
| point critique | critical point, stationary point | un point où la dérivée s'annule (en plusieurs variables : où le gradient s'annule) | M05a, M05b |
| point d'inflexion | inflection point | un point où la courbe passe de convexe à concave, ou l'inverse : $f''$ y change de signe | M05a |
| point de pourcentage | percentage point | écart entre deux pourcentages, obtenu en les soustrayant (de 4 % à 5 % : un point) | R1 |
| point fixe | fixed point | un $\ell$ tel que $f(\ell) = \ell$ : la limite possible d'une suite $u_{n+1} = f(u_n)$ | R5 |
| point selle | saddle point | un point critique où $f$ monte dans certaines directions et descend dans d'autres, comme un col de montagne ; en dimension $n$, la hessienne y a des valeurs propres des deux signes (M19) | M05b, M19 |
| polynôme caractéristique | characteristic polynomial | $p_{\mathbf{A}}(\lambda) = \det(\mathbf{A} - \lambda\mathbf{I})$, de degré $n$, dont les racines sont les valeurs propres ; en dimension 2, $\lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A}$ | M12c |
| polynôme de Taylor, série de Taylor | Taylor polynomial, Taylor series | $\sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k$, le polynôme qui a les mêmes $n$ premières dérivées que $f$ en $a$ ; la série, quand $n \to \infty$ | M05a |
| polynôme, degré | polynomial, degree | somme de puissances entières de $x$ multipliées par des coefficients ; le degré est la plus grande puissance | R3 |
| pondération par l'inverse de la variance | inverse-variance weighting | pour des mesures indépendantes de variances $\sigma_i^2$, les poids $w_i \propto \frac{1}{\sigma_i^2}$ donnent la moyenne pondérée de plus petite variance, $\frac{1}{\sum_i 1/\sigma_i^2}$ ; avec des covariances, $\mathbf{w}^* \propto \boldsymbol{\Sigma}^{-1}\mathbf{1}$ | CP1, M14 |
| population | population | l'ensemble (ou la loi) dont les données sont tirées, et dont on veut connaître les paramètres | M02c |
| position générale | general position | des points sans alignement particulier : dans le plan, jamais trois sur une même droite ; $d + 1$ points de $\mathbb{R}^d$ en position générale sont séparables quels que soient leurs labels | M10 |
| precision (valeur prédictive positive) | precision, positive predictive value (PPV) | $P(Y = 1 \mid \hat{Y} = 1)$ : la part des alertes justifiées ; elle dépend de la prévalence | M03 |
| préconditionnement | preconditioning | remplacer un système par un système équivalent mieux conditionné ; le plus simple, diagonal (de Jacobi) : $\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$, qui met chaque inconnue à l'échelle | M19 |
| prédicat | predicate | une phrase qui dépend d'une variable, comme « $x > 3$ » | R4 |
| prévalence | prevalence, base rate | $P(Y = 1)$ : la proportion de positifs dans la population ; voir aussi « taux de base » | M03 |
| primitive | antiderivative | une fonction $F$ telle que $F' = f$ ; deux primitives sur un intervalle diffèrent d'une constante | M02a |
| principe multiplicatif | rule of product | $a$ choix puis $b$ choix donnent $a \times b$ possibilités | R8 |
| probabilité conditionnelle | conditional probability | $P(A \mid B)$ : la probabilité de $A$ sachant que $B$ s'est réalisé | R8, M03 |
| probabilité jointe | joint probability | $P(A \cap B)$, ou $P(X = x, Y = y)$ : la probabilité que deux choses arrivent ensemble | M03 |
| probabilité marginale | marginal probability | la probabilité d'un événement sur une seule variable, en oubliant l'autre : un total de ligne ou de colonne divisé par le total | M03 |
| probabilités totales (formule des) | law of total probability | $P(A) = \sum_k P(A \mid B_k)\,P(B_k)$ pour une partition $B_1, \ldots, B_K$ | M03 |
| problème d'optimisation convexe | convex optimization problem | minimiser une fonction convexe sous des inégalités $g_i \le 0$ convexes et des égalités affines : tout minimum local est global, et les conditions KKT sont suffisantes | M13b |
| problème primal, problème dual | primal, dual problem | le problème de départ, et le maximum de la fonction duale sous $\boldsymbol{\mu} \ge \mathbf{0}$ : une variable par contrainte ; pour une SVM, une par exemple | M13b |
| produit cartésien, couple | Cartesian product, ordered pair | $A \times B$ : les couples $(a, b)$ avec $a \in A$, $b \in B$ | R4 |
| produit jacobienne-vecteur | Jacobian-vector product (JVP) | $\mathbf{J}_{\mathbf{f}}(\mathbf{x})\,\mathbf{v}$ : la dérivée de toutes les sorties dans la direction $\mathbf{v}$ ; 2 évaluations de $\mathbf{f}$ par différences, sans former la matrice | M17 |
| produit matrice-vecteur | matrix-vector product | $\mathbf{A}\mathbf{x}$ : un produit scalaire par ligne de $\mathbf{A}$, ou la combinaison des colonnes de $\mathbf{A}$ de coefficients les $x_j$ | M09a |
| produit matriciel | matrix product, matrix multiplication | $(\mathbf{A}\mathbf{B})_{ij} = \sum_k a_{ik}b_{kj}$, pour $(n, p) \times (p, m) \to (n, m)$ ; associatif, pas commutatif, $n\,p\,m$ multiplications | M09a |
| produit nul (règle du) | zero-product property | un produit est nul si et seulement si l'un au moins de ses facteurs est nul | R2 |
| produit scalaire | dot product, inner product | $\sum_i x_i y_i$, le produit usuel, mesure d'alignement de deux vecteurs ; plus généralement, une application bilinéaire, symétrique et définie positive, comme $\mathbf{x}^\top\mathbf{M}\mathbf{y}$ | R9, M07, M12b |
| produit scalaire de fonctions | inner product of functions | $\langle f, g \rangle = \int_a^b f(x)\,g(x)\,dx$ ; l'orthogonalité dépend de l'intervalle ; projeter sur des polynômes, ce sont des moindres carrés continus | M12b |
| produit vecteur-jacobienne | vector-Jacobian product (VJP) | $\mathbf{u}^\top\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ : le gradient (une ligne) de $\mathbf{x} \mapsto \mathbf{u} \cdot \mathbf{f}(\mathbf{x})$ ; pour une fonction à une seule sortie, un seul produit donne tout le gradient | M17 |
| produit vectoriel (du plan) | cross product (2-D) | $\mathbf{u} \times \mathbf{v} = u_1v_2 - u_2v_1$ : positif si $\mathbf{v}$ est à gauche de $\mathbf{u}$ ; sa valeur absolue est l'aire du parallélogramme | M10 |
| programme linéaire | linear program | une optimisation d'une fonction linéaire sous des contraintes linéaires ; de faisabilité quand on cherche seulement un point qui les vérifie toutes (`scipy.optimize.linprog`) | M10 |
| programme quadratique | quadratic program | une optimisation d'une fonction quadratique sous des contraintes linéaires ; convexe si la matrice de la forme quadratique est semi-définie positive (la SVM et son dual en sont) | M13b |
| projection (sur une direction) | projection | l'ombre de $\vec{v}$ sur la direction de $\vec{u}$ : $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert^2}\vec{u}$ | R9, M07, M12b |
| projection oblique | oblique projection | une matrice idempotente non symétrique : elle envoie sur un sous-espace, mais pas perpendiculairement | M12b |
| projection orthogonale (sur un sous-espace) | orthogonal projection | le point d'un sous-espace le plus proche d'un vecteur : l'écart est orthogonal au sous-espace ; $\mathbf{Q}\mathbf{Q}^\top\mathbf{v}$ avec une base orthonormée, $\mathbf{A}(\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top\mathbf{v}$ sinon ; les moindres carrés projettent $\mathbf{y}$ sur l'espace des colonnes | M07, M09b, M12b |
| projection sur une boule | projection onto a ball | $\mathbf{x}\min(1, r/\lVert\mathbf{x}\rVert)$ : un point trop loin est ramené sur la sphère le long du rayon, sans changer de direction | M19 |
| proposition | proposition, statement | une phrase qui est soit vraie, soit fausse | R4 |
| pseudo-inverse (de Moore-Penrose) | pseudo-inverse, Moore-Penrose inverse | $\mathbf{A}^+ = \sum_{i \le r}\frac{1}{s_i}\mathbf{v}_i\mathbf{u}_i^\top$, de forme $(n, m)$ ; $\mathbf{A}^+\mathbf{b}$ est la solution des moindres carrés de plus petite norme ; $\mathbf{A}^{-1}$ si $\mathbf{A}$ est inversible, $(\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top$ si ses colonnes sont libres | M12d |
| pseudo-observations | pseudo-counts | les paramètres $a$ et $b$ d'un a priori Beta, lus comme des succès et des échecs déjà vus | M04 |
| puissance | power | $a^n$, produit de $n$ facteurs égaux à $a$ | R1 |
| puissance d'un test | power (of a test) | $1 - \beta$, la probabilité de rejeter $H_0$ quand l'effet existe ; elle grandit avec l'effet, avec $n$ et avec $\alpha$ | M08 |
| quantificateur | quantifier | « pour tout » ($\forall$) ou « il existe » ($\exists$) | R4 |
| quantile | quantile | le plus petit $x$ tel que $F(x) \ge p$ ; la médiane est le quantile d'ordre 0,5 | M02a |
| quantité conjuguée | conjugate | multiplier $\sqrt{A} - \sqrt{B}$ par $\sqrt{A} + \sqrt{B}$ pour obtenir $A - B$ | R7 |
| queue (d'une loi), queue empirique | tail probability, empirical tail | $P(X \ge a)$ ; sur un échantillon, la proportion des valeurs $x_i \ge a$ ; pour une loi binomiale, `binom.sf(k - 1, n, p)` $= P(X \ge k)$ | M11, M14 |
| quotient de Rayleigh | Rayleigh quotient | $R(\mathbf{x}) = \frac{\mathbf{x}^\top\mathbf{A}\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}$ ; pour $\mathbf{A}$ symétrique, une moyenne pondérée des valeurs propres, entre $\lambda_{\min}$ et $\lambda_{\max}$, atteintes aux vecteurs propres ; pour une covariance, la variance le long de $\mathbf{x}$ normé, maximale sur le premier axe principal | M12c, M12d |
| quotient, reste | quotient, remainder | les deux résultats de la division euclidienne | R0 |
| racine (d'une fonction) | root, zero | un $x$ tel que $f(x) = 0$ | R3 |
| racine carrée | square root | nombre positif ou nul dont le carré vaut $a$ | R1 |
| racine carrée d'une matrice | matrix square root | pour $\mathbf{A}$ symétrique semi-définie positive, l'unique matrice symétrique semi-définie positive $\mathbf{A}^{1/2} = \mathbf{Q}\boldsymbol{\Lambda}^{1/2}\mathbf{Q}^\top$ de carré $\mathbf{A}$ ; pas la racine des éléments | M12c |
| radian | radian | unité d'angle : la longueur de l'arc sur le cercle de rayon 1 ; $180° = \pi$ rad | R9 |
| raison (d'une suite) | common difference, common ratio | ce qu'on ajoute (suite arithmétique) ou ce par quoi on multiplie (suite géométrique) à chaque pas | R5 |
| rang | rank | le nombre de pivots, la dimension de l'espace des colonnes (et de celui des lignes) : $\operatorname{rg}(\mathbf{A}) = \operatorname{rg}(\mathbf{A}^\top) \le \min(m, n)$ | M09a, M12a |
| rang numérique | numerical rank | le rang calculé en virgule flottante, où « nul » veut dire « sous une tolérance » : le nombre de valeurs singulières au-dessus d'un seuil ; il dépend du seuil, et de l'échelle des nombres si le seuil est absolu | M12a, M12d |
| rang plein, rang déficient | full rank, rank deficient | $\operatorname{rg}(\mathbf{A}) = \min(m, n)$, ou moins | M12a |
| rasoir d'Occam | Occam's razor | à ajustement égal, préférer le modèle le plus simple ; l'évidence bayésienne le fait d'elle-même | M08 |
| rayon de confiance | confidence radius | la demi-largeur $r$ d'un intervalle $\bar{X} \pm r$ ; Hoeffding, au risque $\delta$ : $r = (b - a)\sqrt{\frac{\ln(2/\delta)}{2n}}$ | M11 |
| rayon spectral | spectral radius | $\rho(\mathbf{M}) = \max_i\lvert\lambda_i\rvert$ : pour $\mathbf{M}$ symétrique, le facteur par lequel l'écart d'une itération linéaire est multiplié au pire à chaque pas | M19, M22 |
| réalisation, tirage | realization, sample, draw | une valeur obtenue d'une variable aléatoire, à distinguer de la variable elle-même | M02b |
| recall (sensibilité) | recall, sensitivity, true positive rate (TPR) | $P(\hat{Y} = 1 \mid Y = 1)$ : la part des positifs détectés | M03 |
| réciproque (d'une implication) | converse | $Q \Rightarrow P$ pour l'implication $P \Rightarrow Q$ : une autre phrase | R4 |
| réciproque (fonction) | inverse function | la fonction $f^{-1}$ qui défait $f$ : $f^{-1}(f(x)) = x$ ; ce n'est pas $\frac{1}{f}$ | R3 |
| recuit simulé | simulated annealing | chercher un minimum en tirant des configurations selon une loi de Boltzmann dont l'énergie est le coût, et en baissant peu à peu la température ; une configuration plus coûteuse de $\Delta$ est acceptée avec la probabilité $e^{-\Delta/T}$ | M17 |
| récurrence (raisonnement par) | (proof by) induction | démontrer $P(n_0)$, puis $P(n) \Rightarrow P(n + 1)$ pour tout $n \ge n_0$ | R4 |
| récurrence (suite définie par) | recursively defined sequence, recurrence relation | un premier terme et une règle $u_{n+1} = f(u_n)$ | R5 |
| récurrence linéaire d'ordre 2 | second-order linear recurrence | $u_{k+2} = p\,u_{k+1} - q\,u_k$, de polynôme caractéristique $r^2 - pr + q$ ; elle tend vers 0 depuis tout départ si et seulement si $\lvert q\rvert < 1$ et $\lvert p\rvert < 1 + q$ | M19 |
| réduction de variance | variance reduction | la baisse de la variance des cibles quand on coupe un groupe en deux : la variance inter-groupes ; le critère des arbres de régression | M13a |
| rééchantillon | resample | $n$ valeurs tirées avec remise parmi les $n$ données (bootstrap) | M02c |
| règle de la chaîne | chain rule | $(g(u(x)))' = g'(u(x)) \times u'(x)$ : on dérive chaque étage d'une composée et on multiplie ; pour plusieurs variables, $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$, une somme sur les variables intermédiaires | R7, M05b, M17 |
| règle de la chaîne (de l'entropie) | chain rule for entropy | $H(X, Y) = H(X) + H(Y \mid X)$ : l'incertitude d'un couple, c'est celle de l'un plus ce qui reste sur l'autre | M06 |
| règle de la somme | sum rule | on obtient une marginale en sommant la loi jointe sur l'autre variable | M02b, M03 |
| règle de score propre | proper scoring rule | une façon de noter des probabilités dont la note moyenne est la meilleure quand on annonce les vraies probabilités ; la log-loss en est une, le taux d'erreur non | M13a |
| règle de trois | rule of three | aucun événement en $n$ essais indépendants : à 95 %, sa probabilité est inférieure à environ $\frac{3}{n}$ | M11 |
| règle du produit (probabilités) | product rule | $P(A \cap B) = P(A \mid B)\,P(B)$ ; MML : $p(\mathbf{x}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{x})\,p(\mathbf{x})$ | M03 |
| règle du produit, du quotient | product rule, quotient rule | $(uv)' = u'v + uv'$ ; $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$ | R7 |
| régression logistique | logistic regression | $P(Y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w} \cdot \mathbf{x} + b)$ : un score affine, lu comme la log-cote de la classe 1 ; ajustée par maximum de vraisemblance, en minimisant la log-loss, convexe en $(\mathbf{w}, b)$ | M13a |
| régression ridge | ridge regression | les moindres carrés pénalisés par $\lambda\lVert \mathbf{w} \rVert^2$ : $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, toujours soluble pour $\lambda > 0$ ; le MAP d'un prior gaussien | M09b |
| regret | regret | ce qu'une stratégie perd par rapport à la meilleure option : pour un bandit, $R_T = \sum_k \Delta_k\,\mathbb{E}[N_k(T)]$ (M11) ; avec des experts, en information complète, sa loss totale moins celle du meilleur expert choisi après coup (M14) | M11, M14 |
| régularisation | regularization | ajouter à la loss une pénalité sur les poids (ridge, lasso) pour préférer les modèles simples ; une contrainte sur la norme des poids donne la même solution pour la bonne valeur du paramètre (le multiplicateur de Lagrange) | M09b, M13b |
| relation de Chasles | Chasles' relation | $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ | R9 |
| ReLU | rectified linear unit | $\max(0, z)$, l'activation la plus utilisée dans les réseaux | M10 |
| remontée (substitution) | back substitution | résoudre un système triangulaire supérieur en partant de la dernière ligne, qui n'a qu'une inconnue | M12b |
| résidu | residual | $r_i = y_i - \hat{y}_i$ : la cible moins la prédiction | M09b |
| reste de Lagrange | Lagrange remainder | $f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - a)^{n+1}$ pour un $\xi$ entre $a$ et $x$ : il borne l'erreur d'un polynôme de Taylor | M05a |
| rétropropagation | backpropagation | le mode inverse de la différentiation automatique, appliqué au graphe d'un réseau de neurones (workbookIA 18) | M18 |
| risque d'erreur de la famille | family-wise error rate (FWER) | la probabilité d'au moins un faux positif dans une famille de tests ; la correction de Bonferroni le garde sous $\alpha$ | M08 |
| risque empirique | empirical risk | la moyenne d'une loss sur les exemples d'entraînement ; apprendre, c'est choisir les paramètres qui le minimisent | M09b |
| sans biais (estimateur) | unbiased estimator | estimateur dont l'espérance est la vraie valeur du paramètre | M02c |
| sans mémoire | memoryless | $P(T > s + t) = P(T > s)\,P(T > t)$ : avoir attendu ne rapproche pas l'événement (lois géométrique et exponentielle) | M02b |
| saturation | saturation | une fonction sature loin de l'origine quand elle y devient presque plate : sa dérivée tend vers 0 ($\arctan'(t) = \frac{1}{1 + t^2}$) | M17 |
| saut de dualité | duality gap | $\min f - \max D \ge 0$, l'écart entre le minimum du primal et le maximum du dual ; nul pour un problème convexe qui vérifie la condition de Slater | M13b |
| schéma de Horner | Horner's method | évaluer un polynôme en multipliant par $x$ et en ajoutant le coefficient suivant, sans puissances | R3 |
| score (d'une ACP) | score | la coordonnée $t_{ij} = \mathbf{u}_j^\top(\mathbf{x}_i - \boldsymbol{\mu})$ d'un exemple sur un axe principal ; les scores sur un axe sont de moyenne nulle et de variance $\lambda_j$, et deux axes donnent des scores non corrélés | M12d |
| score de Brier | Brier score | $\frac{1}{n}\sum (p_i - y_i)^2$ : l'erreur quadratique moyenne des probabilités annoncées | M03 |
| sécante | secant line | droite qui passe par deux points de la courbe ; sa pente est le taux d'accroissement | R7 |
| second degré (polynôme du) | quadratic (polynomial, function) | $ax^2 + bx + c$ avec $a \ne 0$ | R3 |
| semi-définie positive, définie négative, indéfinie | positive semidefinite, negative definite, indefinite | pour une matrice symétrique : $\mathbf{x}^\top\mathbf{A}\mathbf{x} \ge 0$ pour tout $\mathbf{x}$ (valeurs propres positives ou nulles) ; $< 0$ pour tout $\mathbf{x} \ne \mathbf{0}$ (valeurs propres strictement négatives) ; des valeurs des deux signes (valeurs propres des deux signes) | M12c |
| sens direct | counterclockwise | le sens inverse des aiguilles d'une montre ; les sommets d'une enveloppe convexe sont rangés dans ce sens | M10 |
| série de Taylor (à plusieurs variables) | multivariate Taylor series | $f(\mathbf{x} + \mathbf{h}) = f(\mathbf{x}) + \nabla f^\top\mathbf{h} + \frac12\mathbf{h}^\top\nabla^2 f\,\mathbf{h} + \cdots$ ; MML écrit le terme d'ordre $k$ avec le tableau $D^k_{\mathbf{x}}f$ | M19 |
| seuil (fonction) | step function | $H(z) = 1$ si $z > 0$, 0 sinon (la convention en 0 varie) ; l'activation d'un classifieur linéaire qui répond oui ou non ; c'est la fonction marche de R3 | M10 |
| seuil d'un test | significance level | $\alpha$, le risque de type I accepté : on rejette $H_0$ quand la p-valeur est au plus $\alpha$ (souvent 0,05) | M08 |
| seuil de décision | decision threshold | le score à partir duquel on déclare un exemple positif ; $\frac{c_{FP}}{c_{FP} + c_{FN}}$ minimise le coût pour des probabilités calibrées | M03 |
| seuillage doux | soft thresholding | $S(z, \gamma) = \operatorname{signe}(z)\max(\lvert z \rvert - \gamma, 0)$ : rapprocher $z$ de 0 de $\gamma$, ou le mettre à 0 ; la solution du lasso en dimension 1 | M09b |
| sigmoïde (fonction logistique) | sigmoid, logistic function | $\sigma(x) = \frac{1}{1 + e^{-x}}$, à valeurs dans $]0 \;;\; 1[$ | R6 |
| signe aléatoire, variable de Rademacher | random sign, Rademacher variable | $\varepsilon = \pm 1$ avec la probabilité $\frac12$ chacun : centrée, de variance 1 ; multipliés par des signes indépendants, des termes corrélés deviennent décorrélés | M16 |
| silhouette | silhouette (coefficient) | $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$, entre $-1$ et 1 : positive quand le point est en moyenne plus près des points de son cluster que de ceux du cluster voisin, négative quand il est plus près de ceux du cluster voisin, nulle à égalité | M07 |
| similarité cosinus | cosine similarity | $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert\,\lVert \vec{v} \rVert}$, le cosinus de l'angle entre deux vecteurs : compare leurs directions | R9, M07 |
| simulation par inversion | inverse transform sampling | si $U$ est uniforme sur $[0 ; 1]$, $F^{-1}(U)$ suit la loi de fonction de répartition $F$ | M02b |
| softmax, log-softmax | softmax, log-softmax | $\frac{e^{v_i}}{\sum_j e^{v_j}}$, calculée stablement avec $e^{v_i - m}$ ; son logarithme $v_i - \text{LSE}(\mathbf{v})$, qui reste fini | M05a |
| softplus | softplus | $s(z) = \ln(1 + e^z)$ : positive, au-dessus de $\max(z, 0)$, asymptotes $y = 0$ et $y = z$, $s(z) - s(-z) = z$, convexe ; $-\ln\sigma(z) = s(-z)$ ; se calcule $\max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$ | M13a |
| solution de norme minimale | minimum-norm solution | parmi les solutions (ou les solutions des moindres carrés) d'un système, celle qui est la plus proche de l'origine : $\mathbf{A}^+\mathbf{b}$, orthogonale au noyau | M12d |
| solution particulière, solution générale | particular solution, general solution | une solution d'un système ; toutes ses solutions, une solution particulière plus n'importe quelle solution du système homogène | M09a |
| somme de Riemann | Riemann sum | somme des aires de $n$ rectangles de largeur $h = \frac{b - a}{n}$, de hauteur lue à gauche, à droite ou au milieu | M02a |
| somme harmonique | harmonic number (harmonic series pour la série infinie) | $\sum_{t=1}^{T} \frac{1}{t}$, qui croît comme $\ln T$ : elle reste entre $\ln T$ et $1 + \ln T$ | M11 |
| somme infinie, série | infinite sum, series | la limite des sommes partielles ; $\sum_{k=0}^{+\infty} u_0\,q^k = \frac{u_0}{1 - q}$ si $\lvert q \rvert < 1$ | R5 |
| somme partielle | partial sum | la somme des $n$ premiers termes d'une suite | R5 |
| somme pondérée | weighted sum | $\sum w_i x_i + b$, sans division ; le calcul d'un neurone | R1 |
| somme sur les chemins | sum over paths | dans un graphe sans cycle pondéré, la somme, sur les chemins de $i$ à $j$, des produits des poids : le coefficient $(i, j)$ de $\mathbf{A} + \cdots + \mathbf{A}^{n-1}$, ou de $(\mathbf{I} - \mathbf{A})^{-1}$ pour $i \ne j$ | M16 |
| somme télescopique | telescoping sum | $\sum (b_{k+1} - b_k) = b_{n+1} - b_1$ | R4 |
| sommes de carrés (totale, expliquée, résiduelle) | total, explained, residual sum of squares (SST, SSE, SSR) | $\mathrm{SCT} = \sum (y_i - \bar{y})^2$, $\mathrm{SCE} = \sum (\hat{y}_i - \bar{y})^2$, $\mathrm{SCR} = \sum r_i^2$ ; $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$ pour les moindres carrés avec ordonnée à l'origine | M09b |
| sommet (d'une enveloppe convexe) | vertex | un point du nuage qui n'est pas combinaison convexe des autres : un coin du polygone | M10 |
| sonde linéaire | linear probe | une régression logistique entraînée sur les représentations figées d'un réseau déjà entraîné, pour savoir si une propriété y est linéairement lisible | M13a |
| sophisme formel | formal fallacy | une forme d'argument qui a l'air valide sans l'être : affirmer le conséquent, nier l'antécédent | M11 |
| sous-espace affine | affine subspace | un sous-espace vectoriel déplacé, $\mathbf{x}_0 + U$ : une droite ou un plan qui ne passe pas par l'origine, les solutions de $\mathbf{A}\mathbf{x} = \mathbf{b}$ | M12a |
| sous-espace engendré | span | $\operatorname{Vect}(\mathbf{v}_1, \ldots, \mathbf{v}_k)$ : l'ensemble des combinaisons linéaires de ces vecteurs, le plus petit sous-espace qui les contient | M12a |
| sous-espace vectoriel | vector subspace | une partie qui contient $\mathbf{0}$ et est stable par combinaison linéaire ; elle est elle-même un espace vectoriel | M12a |
| sous-gradient, sous-différentiel | subgradient, subdifferential | $\mathbf{g}$ tel que $f(\mathbf{v}) \ge f(\mathbf{u}) + \mathbf{g} \cdot (\mathbf{v} - \mathbf{u})$ pour tout $\mathbf{v}$ ; leur ensemble $\partial f(\mathbf{u})$ ; à un coude il y en a plusieurs, et $\mathbf{0} \in \partial f(\mathbf{u})$ caractérise un minimum | M13b |
| spécificité | specificity, true negative rate | $P(\hat{Y} = 0 \mid Y = 0)$ : la part des négatifs bien reconnus | M03 |
| standardiser | standardize | passer de $X \sim \mathcal{N}(\mu, \sigma^2)$ à $Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$ | M02b, M02c |
| statistique | statistic | une fonction de l'échantillon (moyenne, médiane, maximum) : une variable aléatoire | M02c |
| statistique de test | test statistic | un nombre calculé sur les données qui mesure l'écart à $H_0$ (un nombre de succès, un écart de moyennes) | M08 |
| statistique suffisante | sufficient statistic | un résumé des données qui contient toute leur information sur le paramètre ; pour $n$ essais de Bernoulli, le nombre de succès | M04 |
| strictement convexe | strictly convex | une fonction dont l'inégalité de convexité $f\big((1 - t)\mathbf{a} + t\mathbf{b}\big) \le (1 - t)f(\mathbf{a}) + tf(\mathbf{b})$ est stricte dès que $\mathbf{a} \ne \mathbf{b}$ et $0 < t < 1$ ; une fonction affine ne l'est pas | M10 |
| Student (loi de) | Student's t distribution | loi qui remplace la loi normale pour la moyenne standardisée de peu de données normales, quand $\sigma$ est estimé (quantile 2,262 pour $n = 10$ à 95 %) | M02c, M08 |
| substituer | substitute, plug in | remplacer une lettre par une valeur (ou par une expression) | R2 |
| suite | sequence | liste infinie de nombres $u_0, u_1, \dots$ | R5 |
| suite arithmétique | arithmetic sequence, arithmetic progression | on ajoute la même raison $r$ à chaque pas : $u_n = u_0 + n\,r$ | R5 |
| suite géométrique | geometric sequence, geometric progression | on multiplie par la même raison $q$ à chaque pas : $u_n = u_0\,q^n$ | R5 |
| support (d'une loi) | support | l'ensemble des valeurs où la densité n'est pas nulle | M02a |
| surdispersion | overdispersion | des comptages dont la variance dépasse nettement la moyenne : la loi de Poisson ne convient pas | M02b |
| SVD compacte, SVD réduite | compact SVD, thin SVD | $\mathbf{A} = \mathbf{U}_r\mathbf{S}_r\mathbf{V}_r^\top = \sum_{i \le r} s_i\mathbf{u}_i\mathbf{v}_i^\top$, en ne gardant que les $r$ valeurs singulières non nulles (compacte) ; la SVD réduite de `np.linalg.svd(A, full_matrices=False)` en garde $\min(m, n)$, nulles comprises | M12d |
| SVM (machine à vecteurs de support) | support vector machine | le classifieur linéaire de plus grande marge : $\min \frac12\lVert\mathbf{w}\rVert^2$ sous $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$, ou sa version à marge souple ; avec un noyau, une frontière non linéaire | M13b |
| système homogène | homogeneous system | un système de second membre nul, $\mathbf{A}\mathbf{x} = \mathbf{0}$ ; il a toujours la solution $\mathbf{0}$ | M09a |
| système linéaire | system of linear equations, linear system | plusieurs équations du premier degré à résoudre ensemble ; leurs solutions communes | R2, M09a |
| système « k parmi n » | k-out-of-n system | un système qui fonctionne tant qu'au moins $k$ de ses $n$ composants fonctionnent ; avec des composants indépendants de fiabilité $p$, sa fiabilité est la queue $P(X \ge k)$ de la loi $\mathcal{B}(n, p)$ | M14 |
| t-SNE | t-SNE (t-distributed stochastic neighbor embedding) | une carte en 2D (ou 3D) d'un nuage de grande dimension, qui garde les voisinages : des probabilités de voisinage gaussiennes dans l'espace d'origine, d'une loi de Student sur la carte, rapprochées par descente de gradient sur leur divergence KL ; pour voir, pas pour mesurer | M12d |
| table de vérité | truth table | la valeur d'une proposition pour chaque combinaison des valeurs de ses propositions | R4 |
| tableau de contingence | contingency table | le tableau des effectifs de deux variables catégorielles observées ensemble, avec ses totaux dans les marges | M03 |
| tableau de variations | variation table (sign chart) | tableau du signe de $f'$ et du sens de variation de $f$, avec les valeurs aux points où $f'$ s'annule | R7 |
| taille d'échantillon (calcul de) | sample size calculation | le nombre d'observations qui donne une puissance voulue : $n \ge \big(\frac{(z_{1-\alpha} + z_{1-\beta})\,\sigma}{\delta}\big)^2$ pour une moyenne | M08 |
| taille de l'effet | effect size | l'ampleur de l'écart mesuré, que la p-valeur ne mesure pas : avec beaucoup de données, un effet minuscule devient significatif | M08 |
| taille du pas, learning rate | step size, learning rate | le nombre $\eta > 0$ qui règle la longueur d'un pas de descente de gradient | M05b |
| tangente | tangent line | droite qui touche la courbe en un point avec la même pente : $y = f(a) + f'(a)(x - a)$ | R7 |
| tangente (d'un nœud) | tangent | en mode direct, $\dot{u} = \frac{\partial u}{\partial x_i}$, la dérivée d'un nœud par rapport à l'entrée choisie ; la partie en $\varepsilon$ d'un nombre dual | M18 |
| tangente hyperbolique | hyperbolic tangent | $\tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}}$, à valeurs dans $]-1 \;;\; 1[$ | R6 |
| taux d'accroissement | rate of change, difference quotient | $\frac{f(a + h) - f(a)}{h}$ : la pente de la sécante, une vitesse moyenne | R7 |
| taux d'évolution | percentage change, relative change | $\frac{V_a - V_d}{V_d}$, la variation rapportée à la valeur de départ | R1 |
| taux de base | base rate | la proportion d'un cas dans la population, avant tout indice (la prévalence) ; l'oublier fait lire $P(\text{indice} \mid \text{cas})$ comme $P(\text{cas} \mid \text{indice})$ | M03, M11 |
| taux de faux positifs | false positive rate (FPR) | $P(\hat{Y} = 1 \mid Y = 0) = 1 - \text{spécificité}$ : l'abscisse de la courbe ROC | M03 |
| temps de doublement, demi-vie | doubling time, half-life | la durée au bout de laquelle une grandeur double (ou est divisée par 2) : $\frac{\ln 2}{\ln(1 + r)}$ | R6 |
| terme, rang (d'une suite) | term, index | $u_n$ est le terme de rang (ou d'indice) $n$ | R5 |
| termes semblables, réduire | like terms, collect like terms | termes de même partie littérale ; réduire, c'est les additionner en additionnant leurs coefficients | R2 |
| test binomial exact | exact binomial test | test de $H_0 : p = p_0$ par la loi $\mathcal{B}(n, p_0)$ du nombre de succès ; bilatéral : la somme des issues au plus aussi probables que l'observation | M08 |
| test d'orientation | orientation test | le signe de $(\mathbf{a} - \mathbf{o}) \times (\mathbf{b} - \mathbf{o})$ : à gauche, à droite ou aligné | M10 |
| test du second ordre | second-derivative test | en un point critique, le signe de $D = f_{xx}f_{yy} - f_{xy}^2$ (et celui de $f_{xx}$) dit minimum, maximum ou point selle ; $D = 0$ : il ne conclut pas ; en dimension $n$, les signes des valeurs propres de la hessienne (M19) | M05b, M19 |
| test par permutation | permutation test | la loi nulle obtenue en rebattant les valeurs entre les groupes ; p-valeur $\frac{C + 1}{B + 1}$ avec $B$ permutations tirées au hasard | M08 |
| théorème central limite | central limit theorem (CLT) | pour $n$ grand, la moyenne de $n$ variables i.i.d. suit à peu près $\mathcal{N}\big(\mu, \frac{\sigma^2}{n}\big)$, quelle que soit leur loi | M02c |
| théorème de Cover | Cover's theorem | la proportion des étiquetages séparables de $n$ points en position générale de $\mathbb{R}^d$, $2^{1-n}\sum_{k=0}^{d}\binom{n-1}{k}$ : 1 jusqu'à $d + 1$ points, $\frac{1}{2}$ pour $2(d + 1)$ | M10 |
| théorème de Fubini | Fubini's theorem | une intégrale double sur un rectangle se calcule en intégrant une variable après l'autre, dans n'importe quel ordre | M02b |
| théorème de l'hyperplan séparateur | separating hyperplane theorem | deux convexes compacts disjoints sont strictement séparés par un hyperplan (la médiatrice de leur couple de points le plus proche) | M10 |
| théorème de Schwarz | Schwarz's theorem, symmetry of second derivatives | les dérivées croisées sont égales, $f_{xy} = f_{yx}$, quand les dérivées secondes sont continues | M05b |
| théorème de transfert | law of the unconscious statistician (LOTUS) | $\mathbb{E}[g(X)] = \sum g(x)\,P(X = x)$ ou $\int g(x)\,f(x)\,dx$, sans chercher la loi de $g(X)$ | M02b |
| théorème des valeurs intermédiaires | intermediate value theorem | une fonction continue sur $[a ; b]$ prend toutes les valeurs entre $f(a)$ et $f(b)$ | R7 |
| théorème du rang | rank-nullity theorem | $\dim\ker\mathbf{A} + \operatorname{rg}(\mathbf{A}) = n$, le nombre de colonnes (la dimension de l'espace de départ) | M12a |
| théorème fondamental de l'analyse | fundamental theorem of calculus | $\int_a^b f = F(b) - F(a)$ pour une primitive $F$ ; la fonction aire a pour dérivée $f$ | M02a |
| théorème spectral | spectral theorem | une matrice symétrique réelle a des valeurs propres réelles et une base orthonormée de vecteurs propres : $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ | M12c |
| tirage avec remise, sans remise | sampling with replacement, without replacement | avec remise, l'objet tiré est remis avant le tirage suivant (les tirages sont i.i.d.) ; sans remise, la composition change et les tirages sont dépendants | R8, M02c |
| trace | trace | $\operatorname{tr}\mathbf{A} = \sum_i a_{ii}$ ; linéaire, $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$, indépendante de la base, égale à la somme des valeurs propres ; pour une covariance, la variance totale ; $\sum_{ij}G_{ij}H_{ij} = \operatorname{tr}(\mathbf{G}^\top\mathbf{H})$ (M18) | M12c |
| tranche (d'une surface) | slice, cross-section | la courbe obtenue en figeant une variable, comme $x \mapsto f(x, b)$ ; $\frac{\partial f}{\partial x}(a, b)$ est sa pente en $a$ | M05b |
| transposée | transpose | $\mathbf{A}^\top$, les lignes devenues colonnes : $(\mathbf{A}^\top)_{ij} = a_{ji}$, et $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ | M09a |
| triangle de Pascal | Pascal's triangle | les coefficients binomiaux rangés en triangle : chaque nombre est la somme des deux au-dessus | R8 |
| UMAP | UMAP (uniform manifold approximation and projection) | une carte en 2D qui préserve le graphe des $k$ plus proches voisins (le réglage `n_neighbors`) en minimisant une cross-entropy ; plus rapide que t-SNE, elle place un point nouveau sur une carte existante | M12d |
| unilatéral, bilatéral (test) | one-sided, two-sided test | l'alternative dans un seul sens, fixé à l'avance, ou dans les deux | M08 |
| unité d'arrondi | unit roundoff | l'erreur relative maximale d'une opération en flottants, $u = \frac{\varepsilon}{2}$ ($2^{-53}$ en `float64`) | M05a |
| univers | sample space | $\Omega$, l'ensemble des issues d'une expérience aléatoire | R8 |
| valeur aberrante | outlier | valeur très éloignée des autres ; signalée par $\lvert z \rvert > 3$ ou par la règle de Tukey | M02c |
| valeur absolue | absolute value | $\lvert x \rvert$, le nombre sans son signe ; $\lvert a - b \rvert$ est la distance entre $a$ et $b$ | R2 |
| valeur interdite | excluded value | valeur de l'inconnue qui annule un dénominateur | R2 |
| valeur moyenne d'une fonction | mean value of a function | $\frac{1}{b - a}\int_a^b f$ : la hauteur du rectangle de même aire | M02a |
| valeur prédictive négative | negative predictive value (NPV) | $P(Y = 0 \mid \hat{Y} = 0)$ : la part des « négatif » prédits qui le sont vraiment | M03 |
| valeur propre, vecteur propre | eigenvalue, eigenvector | $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ avec $\mathbf{v} \ne \mathbf{0}$ : une direction que $\mathbf{A}$ ne fait qu'étirer, écraser ou retourner, du facteur $\lambda$ ; les valeurs propres sont les racines de $\det(\mathbf{A} - \lambda\mathbf{I})$, leur somme est la trace, leur produit le déterminant | M12c |
| valeur singulière, vecteurs singuliers | singular value, left and right singular vectors | $s_i = \sqrt{\lambda_i(\mathbf{A}^\top\mathbf{A})} \ge 0$ ; les $\mathbf{v}_i$ (à droite, vecteurs propres de $\mathbf{A}^\top\mathbf{A}$) et les $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i/s_i$ (à gauche, vecteurs propres de $\mathbf{A}\mathbf{A}^\top$), avec $\mathbf{A}\mathbf{v}_i = s_i\mathbf{u}_i$ | M12d |
| validation croisée imbriquée | nested cross-validation | une boucle intérieure choisit le modèle, une boucle extérieure estime la performance de toute la procédure, choix compris | M08 |
| valide, solide (argument) | valid, sound | valide : la conclusion est vraie partout où les prémisses le sont toutes ; solide : valide et à prémisses vraies | M11 |
| variable aléatoire | random variable | grandeur dont la valeur dépend du hasard | R8 |
| variable d'écart | slack variable | $\xi_i \ge 0$ dans $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1 - \xi_i$ : la violation autorisée pour l'exemple $i$ ; à l'optimum, la hinge loss de l'exemple | M13b |
| variable de base, variable libre | basic variable, free variable | une inconnue dont la colonne porte un pivot, ou n'en porte pas ; on choisit les libres, les autres s'en déduisent | M09a |
| variable de confusion | confounder, confounding variable | une troisième grandeur qui fait varier deux autres, et crée entre elles une corrélation sans causalité | M02c |
| variable intermédiaire | intermediate variable | le résultat d'une opération élémentaire d'un calcul : un nœud de son graphe de calcul | M18 |
| variance | variance | moyenne des carrés des écarts à l'espérance | R8 |
| variance d'échantillon | sample variance | $s^2 = \frac{1}{n - 1}\sum (x_i - \bar{x})^2$, estimateur sans biais de $\sigma^2$ ; $s_n^2$ divise par $n$ | M02c |
| variance d'un produit | variance of a product | pour $X$ et $Y$ indépendantes : $\mathbb{V}(XY) = \mathbb{V}(X)\,\mathbb{V}(Y) + \mathbb{V}(X)\,\mathbb{E}[Y]^2 + \mathbb{V}(Y)\,\mathbb{E}[X]^2$, toujours au moins $\mathbb{V}(X)\,\mathbb{V}(Y)$ | M16 |
| variance expliquée (part de) | explained variance ratio | $\lambda_j/\sum_l\lambda_l$ : la part de la variance totale que garde l'axe principal $j$ ; la somme des $k$ premières est la part gardée par une ACP à $k$ composantes | M12d |
| variance intra-groupes, inter-groupes | within-group, between-group variance | la moyenne pondérée des variances des groupes, et la moyenne pondérée des carrés des écarts des moyennes des groupes à la moyenne générale ; leur somme est la variance totale | M13a |
| vecteur | vector | un déplacement (une direction, un sens, une longueur), donné par ses coordonnées ; en ML, une liste de nombres | R9 |
| vecteur de support | support vector | un exemple de multiplicateur $\alpha_i > 0$ dans le dual d'une SVM : de marge fonctionnelle exactement 1 (marge dure), ou de marge fonctionnelle $t_i \le 1$ (marge souple) ; $\mathbf{w}$ ne dépend que d'eux | M10, M13b |
| vecteur directeur, vecteur normal | direction vector, normal vector | un vecteur qui a la direction d'une droite ; un vecteur perpendiculaire à une droite ou à un plan (il engendre son complément orthogonal) | R9, M07, M12b |
| vecteur one-hot | one-hot vector | le codage d'une catégorie : un 1 à sa place, des 0 ailleurs (un vecteur de la base canonique) | M07 |
| vecteur unitaire | unit vector | un vecteur de norme 1 ; $\frac{\vec{u}}{\lVert \vec{u} \rVert}$ normalise $\vec{u}$ | R9, M07 |
| vote pondéré, vote souple | weighted vote, soft voting | avec des poids positifs de somme 1 : la classe la plus probable quand on tire un modèle selon ces poids ; le vote souple moyenne, coordonnée par coordonnée, les vecteurs de probabilités des modèles | M14 |
| vrai positif, vrai négatif | true positive, true negative (TP, TN) | un positif prédit positif ; un négatif prédit négatif | M03 |
| vraisemblance | likelihood | probabilité des données, vue comme fonction des paramètres | M04 |
| weight decay | weight decay | la pénalité L2 vue dans une descente de gradient : $\mathbf{w} \leftarrow (1 - 2\eta\lambda)\mathbf{w} - \eta\nabla L(\mathbf{w})$ | M09b |
| z-score (score standard) | standard score, z-score | $z = \frac{x - \bar{x}}{s}$ : le nombre d'écarts-types entre une valeur et la moyenne | M02c |
