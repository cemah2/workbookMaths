# Glossaire français ↔ anglais

Les termes mathématiques sont en français dans les fiches, avec l'anglais en glose à leur première apparition : c'est l'anglais que tu liras dans MML. Les termes du machine learning gardent l'usage de workbookIA (loss, learning rate, batch, feature… restent en anglais). Chaque chapitre ajoute ses termes ; la colonne « Chapitre » renvoie à celui qui le définit. Quelques entrées renvoient déjà à un chapitre à venir (M12a, M12c, M17…) : elles servent à reconnaître le mot dans MML ou dans workbookIA, et ce chapitre le définira.

| Français | Anglais | Définition courte | Chapitre |
|---|---|---|---|
| a priori conjugué | conjugate prior | un a priori dont l'a posteriori est de la même famille ; la loi Beta pour la binomiale : $\mathrm{Beta}(a, b) \to \mathrm{Beta}(a + k,\ b + n - k)$ | M04 |
| a priori, a posteriori | prior, posterior | la loi d'un paramètre ou d'une hypothèse avant de voir les données ; après, sachant les données | M04 |
| absorption | absorption (swamping) | un petit nombre ajouté à un grand disparaît à l'arrondi : $10^{16} + 1$ donne $10^{16}$ en `float64` | M05a |
| accuracy | accuracy | $P(\hat{Y} = Y)$ : la proportion de prédictions justes ; trompeuse quand une classe est rare | M03 |
| activation (fonction d') | activation function | une fonction d'une variable appliquée au score $z = \mathbf{w} \cdot \mathbf{x} + b$ d'un classifieur linéaire : seuil, sigmoïde, tanh, ReLU | M10 |
| actualiser, valeur actuelle | discount, present value | ramener une somme future à sa valeur d'aujourd'hui : la diviser par $(1 + t)^n$ | R5 |
| affirmer le conséquent | affirming the consequent | le sophisme formel « $P \Rightarrow Q$ ; $Q$ ; donc $P$ » : non valide, la ligne « $P$ faux, $Q$ vrai » le réfute | M11 |
| AIC, BIC (critères d'information) | Akaike information criterion, Bayesian information criterion | $\mathrm{AIC} = 2k - 2\ln L$, $\mathrm{BIC} = k\ln n - 2\ln L$ ; le plus petit gagne ; le BIC pénalise davantage chaque paramètre dès $n \ge 8$ | M08 |
| aire algébrique | signed area | aire comptée positivement au-dessus de l'axe, négativement en dessous : c'est ce que mesure une intégrale | M02a |
| angle entre deux vecteurs | angle between two vectors | l'angle $\theta \in [0 ; \pi]$ tel que $\vec{u} \cdot \vec{v} = \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert\cos\theta$ | R9, M07 |
| annulation (catastrophique) | catastrophic cancellation | la perte de chiffres justes quand on soustrait deux nombres presque égaux : l'erreur relative explose | M05a |
| antécédent, image | preimage, image | $f(x)$ est l'image de $x$ ; un antécédent de $y$ est un $x$ tel que $f(x) = y$ | R3 |
| application affine | affine mapping | $\varphi(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}$ : une partie linéaire suivie d'une translation ; bijective si et seulement si $\mathbf{A}$ est inversible, et alors $\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$ | M12a |
| application linéaire | linear map, linear mapping | $f(\lambda\mathbf{x} + \mu\mathbf{y}) = \lambda f(\mathbf{x}) + \mu f(\mathbf{y})$ ; de $\mathbb{R}^n$ dans $\mathbb{R}^m$, c'est $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$, la colonne $j$ de $\mathbf{A}$ étant $f(\mathbf{e}_j)$ | M12a |
| approximation affine | linear approximation | $f(a + h) \approx f(a) + f'(a)\,h$ : la courbe remplacée par sa tangente près de $a$ | R7 |
| arbre pondéré | probability tree | arbre des étapes d'une expérience, chaque branche portant sa probabilité : on multiplie le long d'un chemin, on additionne les chemins | R8 |
| arccosinus | arccosine, arccos | la réciproque du cosinus sur $[0 ; \pi]$ : l'unique angle de $[0 ; \pi]$ qui a un cosinus donné | R9 |
| argmax, argmin | argmax, argmin | la valeur de $x$ où une fonction atteint son maximum (son minimum), pas la valeur de ce maximum | R3, M05b |
| argument, prémisse | argument, premise | une suite de phrases, les prémisses, suivie d'une conclusion qu'elles sont censées justifier | M11 |
| arrangement | k-permutation | choix ordonné de $k$ objets distincts parmi $n$ : $\frac{n!}{(n - k)!}$ possibilités | R8 |
| arrondi, troncature | rounding, truncation | arrondir garde le nombre le plus proche ; tronquer coupe sans regarder la suite | R1 |
| astuce de reparamétrisation | reparameterization trick | écrire $X = \mu + \sigma Z$ avec $Z \sim \mathcal{N}(0, 1)$ : le hasard est dans $Z$, et $\mu$, $\sigma$ deviennent des paramètres qu'on peut ajuster par gradient | M02b |
| astuce du biais | bias trick | ajouter une coordonnée constante 1 en tête : $\tilde{\mathbf{x}} = (1, \mathbf{x})$, $\tilde{\mathbf{w}} = (b, \mathbf{w})$, $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}} = \mathbf{w} \cdot \mathbf{x} + b$ : un hyperplan affine devient un hyperplan par l'origine | M10 |
| asymptote | asymptote | droite dont la courbe se rapproche indéfiniment : horizontale ($y = L$) ou verticale ($x = a$) | R7 |
| AUC (aire sous la courbe ROC) | area under the curve | $\int_0^1 \text{TPR}\,d(\text{FPR})$ : 1/2 pour le hasard, 1 pour un classement parfait | M02a, M03 |
| average precision | average precision (AP) | $\sum_j (R_j - R_{j-1})\,P_j$ : l'aire, en rectangles, sous la courbe precision-recall | M03 |
| balanced accuracy | balanced accuracy | la moyenne des recalls des classes ; 0,5 pour un modèle qui prédit toujours la même classe | M03 |
| bandit manchot | multi-armed bandit | choisir pas à pas entre $K$ options (des bras) de récompenses moyennes inconnues, pour en accumuler le plus possible : le compromis entre exploration et exploitation | M11 |
| barrières de Tukey | (Tukey's) fences | les bornes $Q_1 - 1{,}5\,\text{EI}$ et $Q_3 + 1{,}5\,\text{EI}$ (EI : l'écart interquartile) ; une valeur hors de ces bornes est signalée comme aberrante | M02c |
| barycentre, centroïde | centroid, mean (of a point cloud) | $\bar{\mathbf{x}} = \frac{1}{m}\sum_i \mathbf{x}_i$, la moyenne coordonnée par coordonnée d'un nuage de points ; pondéré : $\frac{\sum_i \omega_i \mathbf{x}_i}{\sum_i \omega_i}$ | M07 |
| base (d'un espace vectoriel) | basis | une famille libre et génératrice : tout vecteur s'y écrit d'une seule façon, et ses coefficients sont ses coordonnées | M12a |
| base canonique | standard basis | les vecteurs $\mathbf{e}_1, \ldots, \mathbf{e}_n$ de $\mathbb{R}^n$ (un 1 à la place $i$, des 0 ailleurs) : $\mathbf{x} = \sum_i x_i\,\mathbf{e}_i$ | M07 |
| biais (d'un estimateur) | bias | $\mathbb{E}[\hat{\theta}] - \theta$ : l'erreur systématique d'un estimateur, en moyenne sur tous les échantillons | M02c |
| biais (d'un neurone) | bias | nombre $b$ ajouté à la somme pondérée d'un neurone, appris comme les poids | R1 |
| biais d'échantillonnage | sampling bias | un échantillon qui ne représente pas la population visée, à cause de la façon dont il a été collecté ; plus de données ne le corrigent pas | M02c |
| biais de sélection | selection bias | les individus observés ne sont pas tirés au hasard dans la population visée (taux de réponse inégaux, filtre) : l'estimation converge vers une mauvaise valeur, quelle que soit la taille | M11 |
| biais du survivant | survivorship bias | n'observer que ce qui a passé un filtre (les avions rentrés de mission, les prêts accordés), et conclure comme si c'était tout | M02c |
| Bienaymé-Tchebychev (inégalité de) | Chebyshev's inequality | $P(\lvert X - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$, pour toute loi de variance finie | M02c, M11 |
| bit, nat | bit, nat | unités d'information : un événement de probabilité $p$ apporte $-\log_2 p$ bits, ou $-\ln p$ nats ; 1 bit ≈ 0,693 nat | R6, M06 |
| boîte à moustaches | boxplot, box-and-whisker plot | dessin d'une série : une boîte de $Q_1$ à $Q_3$ coupée par la médiane, des moustaches jusqu'aux valeurs non aberrantes les plus extrêmes | M02c |
| Bonferroni (correction de) | Bonferroni correction | chaque test au seuil $\frac{\alpha}{m}$, ou les p-valeurs ajustées $\min(1, m\,p_i)$ comparées à $\alpha$ : la probabilité d'au moins un faux positif reste sous $\alpha$, sans hypothèse d'indépendance | M08 |
| bootstrap | bootstrap | estimer la dispersion d'une statistique en la recalculant sur des milliers de rééchantillons tirés avec remise dans les données | M02c |
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
| chiffres significatifs | significant figures | les chiffres d'un nombre à partir du premier chiffre non nul | R1 |
| classe positive | positive class | la classe que l'on cherche à détecter (la panne, le défaut), codée 1 | M03 |
| code de longueur fixe, de longueur variable | fixed-length code, variable-length code | un code dont tous les mots ont la même longueur ($\lceil \log_2 N \rceil$ bits pour $N$ issues) ; un code qui donne des mots plus courts aux issues fréquentes | M06 |
| code préfixe | prefix code, prefix-free code | un code où aucun mot n'est le début d'un autre : des mots écrits bout à bout se découpent sans ambiguïté | M06 |
| coefficient | coefficient | nombre qui multiplie la partie littérale d'un terme : 7 dans $7x^2$ | R2 |
| coefficient binomial | binomial coefficient | $\binom{n}{k}$, « k parmi n » : le nombre de façons de choisir $k$ objets parmi $n$, sans ordre | R8 |
| coefficient de détermination ($R^2$) | coefficient of determination | $1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$ : la part de la variation des cibles que le modèle fait disparaître ; 1 s'il est parfait, négatif possible sur de nouvelles données | M09b |
| coefficient multiplicateur | multiplier, growth factor | nombre $1 + t$ par lequel une évolution de taux $t$ multiplie une valeur | R1 |
| colinéaires (vecteurs) | collinear vectors | l'un est un multiple de l'autre : $xy' - x'y = 0$ | R9 |
| combinaison affine | affine combination | une combinaison linéaire dont les coefficients ont une somme égale à 1 (un barycentre) ; une application affine la conserve | M12a |
| combinaison convexe | convex combination | $\sum_i t_i\mathbf{x}_i$ avec $t_i \ge 0$ et $\sum_i t_i = 1$ ; le segment, le barycentre en sont | M10 |
| combinaison linéaire | linear combination | somme de vecteurs multipliés par des nombres | M07, M12a |
| comparaisons multiples | multiple comparisons, multiple testing | faire beaucoup de tests, ou essayer beaucoup de modèles : $m\alpha$ faux positifs en moyenne si aucun effet n'existe | M08 |
| complémentaire (d'un ensemble) | complement | $\bar{A}$ : les éléments de l'univers qui ne sont pas dans $A$ | R4 |
| composée (de deux fonctions) | composition, composite function | $(f \circ g)(x) = f(g(x))$ : on applique $g$, puis $f$ | R3 |
| compromis biais-variance | bias-variance trade-off | un modèle plus souple a moins de biais et plus de variance ; une pénalité comme ridge règle cet équilibre | M09b |
| concave | concave | dont toute corde est au-dessous de la courbe ; pour $f$ deux fois dérivable, $f'' \le 0$ | M05a |
| concentration (de la norme) | concentration of measure | en grande dimension, une quantité qui dépend de beaucoup de coordonnées indépendantes varie peu autour de sa valeur typique : la norme d'un vecteur gaussien de $\mathbb{R}^n$ vaut $\sqrt{n}$ à environ 0,7 près | M07 |
| condition nécessaire, suffisante | necessary, sufficient condition | dans $P \Rightarrow Q$, P est suffisante pour Q et Q nécessaire pour P | R4 |
| conservateur (test) | conservative test | un test dont le risque de type I réel est plus petit que le seuil annoncé, comme un test à statistique discrète | M08 |
| continuité | continuity | $f$ est continue en $a$ si $\lim_{x \to a} f(x) = f(a)$ : pas de saut | R7 |
| contraposée | contrapositive | $\text{non } Q \Rightarrow \text{non } P$, de même valeur que $P \Rightarrow Q$ | R4 |
| contre-exemple | counterexample | un cas qui rend fausse une phrase « pour tout » | R4 |
| convergence linéaire, quadratique | linear, quadratic convergence | l'erreur est multipliée par une constante $< 1$ à chaque pas (linéaire), ou à peu près élevée au carré (quadratique : les décimales justes doublent) | M05a |
| convergent (estimateur) | consistent estimator | estimateur dont l'erreur tend vers 0 quand la taille de l'échantillon grandit | M02c |
| converger, diverger (suite) | converge, diverge | une suite converge si elle a une limite finie ; sinon elle diverge (vers $\pm\infty$, ou sans limite) | R5 |
| convexe | convex | un ensemble l'est s'il contient le segment entre deux quelconques de ses points ; une fonction l'est si chaque corde est au-dessus de sa courbe (c'est-à-dire si son épigraphe est un ensemble convexe) | M05a, M10 |
| coordonnées dans une base | coordinates, coordinate vector | les coefficients $(c_1, \ldots, c_n)$ de l'écriture unique $\mathbf{v} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n$ : la solution de $\mathbf{B}\mathbf{c} = \mathbf{v}$ | M12a |
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
| croissances comparées | orders of growth, comparative growth rates | pour $x$ très grand, $\ln x \ll x^k \ll a^x$ ($k > 0$, $a > 1$) | R6 |
| croissante, décroissante | increasing, decreasing | qui conserve (retourne) l'ordre sur un intervalle : $a < b \Rightarrow f(a) \le f(b)$ ($\ge$) | R3 |
| cross-entropy | cross-entropy | $H(p, q) = -\sum p \log_2 q$ : la longueur moyenne d'un code fait pour la loi $q$, sur des données de loi $p$ ; la log loss en est une | M06 |
| ddof | ddof (delta degrees of freedom) | le nombre retranché à $n$ au dénominateur d'une variance : `ddof=0` divise par $n$, `ddof=1` par $n - 1$ | M02c |
| débordement, underflow | overflow, underflow | un résultat trop grand pour un flottant, que NumPy rend `inf` ; trop petit, il est arrondi à 0 (*dépassement par le bas*) ; on garde souvent les mots anglais | M04, M05a |
| décade, échelle logarithmique | decade, logarithmic scale | sur un axe logarithmique, des écarts égaux sont des rapports égaux ; une décade est un facteur 10 | R6 |
| décibel | decibel (dB) | un rapport $R$ exprimé par $10 \log_{10} R$ ; le PSNR se mesure en décibels | R6 |
| décomposition biais-variance | bias-variance decomposition | l'erreur quadratique attendue sur une nouvelle mesure vaut biais² + variance + bruit $\sigma^2$ | M09b |
| déduction, induction | deduction, induction | raisonner des prémisses à une conclusion certaine si elles sont vraies ; généraliser des exemples à une conclusion seulement probable (le raisonnement par récurrence est une déduction) | M11 |
| degrés de liberté | degrees of freedom | le nombre de valeurs libres : les $n$ écarts à la moyenne ont une somme nulle, donc $n - 1$ degrés de liberté | M02c |
| demi-espace | half-space | l'un des deux côtés d'un hyperplan : les $\mathbf{x}$ tels que $\mathbf{w} \cdot \mathbf{x} + b > 0$ (ou $< 0$) | M07 |
| démonstration par l'absurde | proof by contradiction | supposer la conclusion fausse et aboutir à une contradiction | R4 |
| dénombrement | counting | l'art de compter des possibilités sans les lister : principe multiplicatif, factorielles, combinaisons | R8 |
| densité de probabilité | probability density function (pdf) | fonction positive d'aire totale 1 : $P(a \le X \le b) = \int_a^b f$ ; une probabilité par unité de longueur, qui peut dépasser 1 | M02a |
| densité jointe | joint density | fonction $f(x, y) \ge 0$ d'intégrale double 1, telle que $P((X, Y) \in D) = \iint_D f$ | M02b |
| dérivée directionnelle | directional derivative | la pente de $f$ en un point quand on avance dans la direction d'un vecteur unitaire $\mathbf{u}$ : $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$ | M05b |
| dérivée partielle | partial derivative | dérivée par rapport à une variable, les autres fixées | M05b |
| dérivée seconde | second derivative | la dérivée de $f'$, notée $f''$ : son signe dit si la pente augmente (courbe convexe) ou diminue (concave) | M05a |
| dérivée, fonction dérivée | derivative | la pente de la tangente, taux de variation instantané ; la fonction $x \mapsto f'(x)$ qui la donne en chaque point | R7 |
| dérivées partielles secondes, dérivée croisée | second partial derivatives, mixed partial derivative | $f_{xx}$, $f_{yy}$, et $f_{xy}$, la dérivée de $f_x$ par rapport à $y$ | M05b |
| désabonnement | churn | le départ d'un client à la fin de son abonnement ; une cible courante des modèles de classification | M03 |
| descente de gradient, montée de gradient | gradient descent, gradient ascent | $\mathbf{x}_{k+1} = \mathbf{x}_k - \eta\,\nabla f(\mathbf{x}_k)$ : de petits pas dans la direction de plus grande descente, pour minimiser ; avec $+$, pour maximiser | M05b |
| déterminant | determinant | le nombre $ad - bc$ d'un système 2 × 2, non nul exactement quand il a une seule solution (R2) ; facteur de changement d'aire ou de volume d'une application linéaire (M12c) | R2, M12c |
| développer, factoriser | expand, factor | transformer un produit en somme ; transformer une somme en produit | R2 |
| diagramme de fiabilité | reliability diagram | pour des paquets de scores, la probabilité moyenne annoncée contre la fréquence observée ; la diagonale si le modèle est calibré | M03 |
| diagramme de Venn | Venn diagram | chaque ensemble dessiné comme une région du plan : une inclusion dit qu'une région est vide, « au moins un » qu'elle contient un élément | M11 |
| dichotomie | bisection | trouver un zéro en coupant l'intervalle en deux et en gardant la moitié où le signe change | R7 |
| différence finie (avant, centrée) | finite difference (forward, central) | une approximation de $f'(x)$ par $\frac{f(x + h) - f(x)}{h}$ (ordre 1) ou $\frac{f(x + h) - f(x - h)}{2h}$ (ordre 2) | M05a |
| dimension | dimension | le nombre de vecteurs de n'importe quelle base : $\dim\mathbb{R}^n = n$, $\dim\mathbb{R}_d[x] = d + 1$ | M12a |
| direction de plus grande pente | steepest ascent direction | $\frac{\nabla f}{\lVert \nabla f \rVert}$, la direction où $f$ monte le plus vite, avec la pente $\lVert \nabla f \rVert$ ; l'opposée est celle de plus grande descente | M05b |
| discriminant | discriminant | $\Delta = b^2 - 4ac$ ; son signe donne le nombre de racines de $ax^2 + bx + c$ | R3 |
| disjonction de cas | proof by cases | découper en cas qui couvrent toutes les possibilités, et traiter chacun | R4 |
| distance (entre deux points) | distance | $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$, la norme du vecteur $\overrightarrow{AB}$ | R9 |
| distance cosinus | cosine distance | $1 - \cos\theta$, entre 0 et 2 : ce que renvoie `scipy.spatial.distance.cosine` | M07 |
| distance euclidienne, de Manhattan, de Tchebychev | Euclidean, Manhattan (city block), Chebyshev distance | la norme L2, L1 ou L∞ de la différence de deux points | M07 |
| divergence de Jensen-Shannon | Jensen-Shannon divergence | $\frac{1}{2}\mathrm{KL}(p \parallel m) + \frac{1}{2}\mathrm{KL}(q \parallel m)$ avec $m = \frac{p + q}{2}$ : une divergence symétrique et toujours finie | M06 |
| divergence KL (de Kullback-Leibler) | KL divergence, Kullback-Leibler divergence, relative entropy | $\mathrm{KL}(p \parallel q) = \sum p \log_2 \frac{p}{q} = H(p, q) - H(p)$ : les bits perdus par symbole ; positive, nulle si $p = q$, pas symétrique | M06 |
| division euclidienne | Euclidean division, integer division | $a = bq + r$ avec $0 \le r < b$ ; en Python, `a // b` donne $q$ et `a % b` donne $r$ | R0 |
| double descente | double descent | l'erreur de test culmine près de $p = n$ (poids instables), puis peut redescendre au-delà avec la solution de plus petite norme | M09b |
| écart (d'une option) | gap | $\Delta_k = \mu^\star - \mu_k$ : ce que coûte, en moyenne, un choix de l'option $k$ au lieu de la meilleure | M11 |
| écart interquartile | interquartile range (IQR) | $Q_3 - Q_1$ : la dispersion de la moitié centrale d'une série, insensible aux valeurs extrêmes | M02c |
| écart-type | standard deviation | racine carrée de la variance | R8 |
| échangeabilité | exchangeability | sous $H_0$, toutes les répartitions des valeurs entre les groupes sont aussi probables : ce qui justifie un test par permutation | M08 |
| échantillon i.i.d. | i.i.d. sample | variables $X_1, \ldots, X_n$ indépendantes et de même loi : le modèle de base des données en statistique et en ML | M02c |
| échantillonnage de Thompson | Thompson sampling | choisir à chaque essai l'option dont un tirage dans l'a posteriori est le plus grand : explorer et exploiter à la fois | M04, M11 |
| effectif attendu | expected count | l'effectif d'une case d'un tableau de contingence si les variables étaient indépendantes : $\frac{\text{total de la ligne} \times \text{total de la colonne}}{\text{total}}$ | M03 |
| effet de masque | masking effect | une valeur aberrante gonfle l'écart-type et cache ainsi son propre z-score | M02c |
| égalité des taux d'erreur | equalized odds | critère d'équité : le même recall et le même taux de faux positifs dans chaque groupe | M03 |
| embedding (table d') | embedding (table) | une matrice d'une ligne par mot (ou par catégorie) : l'embedding du mot $k$ est la ligne $k$, le produit de son vecteur one-hot par la table | M09a |
| empreinte | hash | code calculé à partir d'une donnée, d'où l'on ne peut pas la retrouver ; sert à comparer sans stocker | R0 |
| ensemble | set | collection d'éléments distincts | R4 |
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
| erreur de type I, de type II | type I error (false positive), type II error (false negative) | rejeter $H_0$ alors qu'elle est vraie (probabilité $\alpha$) ; ne pas la rejeter alors que l'effet existe (probabilité $\beta$) | M08 |
| erreur quadratique moyenne (d'un estimateur) | mean squared error (MSE) | $\mathbb{E}[(\hat{\theta} - \theta)^2] = \text{biais}^2 + \text{variance}$ | M02c |
| erreur type | standard error (SE) | l'écart-type d'un estimateur ; pour une moyenne, $\frac{s}{\sqrt{n}}$ ; pour une proportion, $\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$ | M02c |
| espace d'arrivée | target space | l'ensemble des valeurs que peut prendre une variable aléatoire ($\mathcal{T}$ dans MML) : $\mathbb{R}$, un ensemble de classes ou de vecteurs | M02b |
| espace des colonnes, espace des lignes | column space, row space | le sous-espace engendré par les colonnes de $\mathbf{A}$ (son image), ou par ses lignes ; tous deux ont pour dimension le rang | M12a |
| espace probabilisé | probability space | le triplet (univers, événements, probabilité) d'une expérience aléatoire | M02b |
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
| faux positif, faux négatif | false positive, false negative (FP, FN) | un négatif prédit positif (fausse alerte) ; un positif prédit négatif (cas manqué) | M03 |
| features polynomiales | polynomial features | les monômes des features jusqu'à un degré $d$, interactions comprises : $\binom{p + d}{d}$ colonnes, constante comprise | M09b |
| flottant (nombre à virgule flottante) | floating-point number, float | nombre à virgule rangé avec un nombre fixe de chiffres binaires, donc souvent arrondi | R0, M05a |
| fonction | function | règle qui associe à chaque élément de son ensemble de définition une seule image | R3 |
| fonction affine, linéaire | affine function, linear function | $x \mapsto mx + c$ ; linéaire quand $c = 0$ | R3 |
| fonction Beta, fonction Gamma | Beta function, Gamma function | $B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)}$ ; $\Gamma(n) = (n - 1)!$ pour un entier $n \ge 1$ | M04 |
| fonction d'erreur | error function, erf | $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$, un nom donné à cette intégrale sans primitive usuelle | M02a |
| fonction de masse | probability mass function (pmf) | $p(x) = P(X = x)$ pour une variable discrète : positive, de somme 1 | M02b |
| fonction de plusieurs variables | multivariate function, function of several variables | une fonction qui prend plusieurs nombres et en renvoie un, comme $f(x, y)$ ; son graphe est une surface | M05b |
| fonction de répartition | cumulative distribution function (cdf) | $F(x) = P(X \le x)$ : croissante de 0 à 1, et $F' = f$ pour une densité $f$ | M02a |
| fonction définie par morceaux | piecewise function | une formule sur chaque partie de l'ensemble de définition : $\max(0, x)$, la marche, $\lvert x \rvert$ | R3 |
| fonction quantile | quantile function | la réciproque $F^{-1}$ de la fonction de répartition : $F^{-1}(u) = q_u$ | M02a, M02b |
| fonction signe | sign function | $\operatorname{sign}(x)$ vaut $-1$, 0 ou 1 selon que $x$ est négatif, nul ou positif | R2 |
| forme canonique | vertex form, completed-square form | $a(x - \alpha)^2 + \beta$, qui montre le sommet d'une parabole | R3 |
| forme canonique (d'un séparateur) | canonical form | un séparateur dont la plus petite marge fonctionnelle vaut 1 ; sa marge géométrique est alors $\frac{1}{\lVert \mathbf{w} \rVert}$ | M10 |
| forme d'une matrice | shape | le couple (nombre de lignes, nombre de colonnes), lignes d'abord : $(n, p)$ pour un dataset de $n$ exemples à $p$ features | M09a |
| forme échelonnée, forme échelonnée réduite | row echelon form, reduced row echelon form | un escalier : les lignes nulles en bas, chaque pivot à droite de celui du dessus ; réduite : chaque pivot vaut 1 et est seul dans sa colonne (elle est unique) | M09a |
| forme indéterminée | indeterminate form | $\infty - \infty$, $\frac{\infty}{\infty}$, $0 \times \infty$, $\frac{0}{0}$ : une limite qui ne se décide pas d'avance | R7 |
| forme quadratique | quadratic form | $\mathbf{w}^\top\mathbf{A}\mathbf{w} = \sum_{i,j} a_{ij}w_iw_j$, de gradient $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ | M09b |
| formule d'Al-Kashi | law of cosines | $c^2 = a^2 + b^2 - 2ab\cos\hat{C}$ dans un triangle quelconque : Pythagore corrigé par l'angle | R9 |
| formule de Bayes | Bayes' theorem | $P(H \mid O) = \frac{P(O \mid H)\,P(H)}{P(O)}$ : a posteriori = vraisemblance × a priori / évidence | M04 |
| formule de Cramer | Cramer's rule | la solution d'un système de déterminant non nul, écrite comme quotients de déterminants | R2 |
| fraction irréductible | irreducible fraction, fraction in lowest terms | fraction dont numérateur et dénominateur n'ont plus d'autre diviseur commun que 1 | R1 |
| fréquence | (relative) frequency | nombre de fois où un événement se réalise, divisé par le nombre d'essais | R8 |
| fréquentiste, bayésien | frequentist, Bayesian | deux lectures des probabilités : une fréquence à long terme, le paramètre étant fixe ; un degré de croyance sur le paramètre | M04 |
| frontière de décision linéaire | linear decision boundary | l'hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ qui sépare les points classés 1 de ceux classés 0 par un score linéaire | M07 |
| Gauss-Jordan (méthode de) | Gauss-Jordan elimination | réduire $[\mathbf{A} \mid \mathbf{I}]$ en forme échelonnée réduite : on obtient $[\mathbf{I} \mid \mathbf{A}^{-1}]$, ou une ligne nulle à gauche si $\mathbf{A}$ est singulière | M09a |
| générateur pseudo-aléatoire, graine | pseudo-random number generator, seed | programme qui calcule une suite d'apparence aléatoire à partir d'une graine ; la même graine redonne la même suite | R8 |
| gradient | gradient | vecteur des dérivées partielles | M05b |
| grand O | big O | $f = O(g)$ : $f$ ne croît pas plus vite que $g$, à une constante près ; mesure le coût d'un algorithme | R7 |
| Hadamard (produit de) | Hadamard product, element-wise product | $\mathbf{A} \odot \mathbf{B}$, les produits des éléments de même position (`A * B` en NumPy) ; même forme, commutatif | M09a |
| hérédité, initialisation | inductive step, base case | les deux étapes d'une récurrence : $P(n) \Rightarrow P(n + 1)$, et $P(n_0)$ | R4 |
| hessienne | Hessian | matrice des dérivées secondes | M05b, M19 |
| Hoeffding (inégalité de) | Hoeffding's inequality | pour $n$ variables indépendantes à valeurs dans $[a, b]$ : $P(\lvert \bar{X} - \mu \rvert \ge t) \le 2e^{-2nt^2/(b - a)^2}$ | M11 |
| homogénéité (d'une norme) | absolute homogeneity | $\lVert \lambda\mathbf{x} \rVert = \lvert \lambda \rvert\,\lVert \mathbf{x} \rVert$ : multiplier un vecteur par $\lambda$ multiplie sa longueur par $\lvert \lambda \rvert$ | M07 |
| hyperplan | hyperplane | les $\mathbf{x}$ de $\mathbb{R}^n$ tels que $\mathbf{w} \cdot \mathbf{x} + b = 0$, avec $\mathbf{w} \ne \mathbf{0}$ (le vecteur normal) : une droite du plan, un plan de l'espace | M07 |
| hyperplan séparateur | separating hyperplane | un hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ tel que chaque classe est dans l'un des deux demi-espaces ouverts : $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) > 0$ pour tout $i$ | M10 |
| hypothèse nulle, hypothèse alternative | null hypothesis, alternative hypothesis | $H_0$, souvent « pas d'effet », que le test cherche à mettre en défaut ; $H_1$, ce qu'on veut montrer ; toutes deux fixées avant de voir les données | M08 |
| idempotente (matrice) | idempotent matrix | $\mathbf{H}\mathbf{H} = \mathbf{H}$ : l'appliquer deux fois ne change rien, comme une projection | M09b |
| identité remarquable | special product, algebraic identity | égalité vraie pour tous $a$ et $b$, comme $(a + b)^2 = a^2 + 2ab + b^2$ | R2 |
| image (d'une application linéaire) | image, range | $\operatorname{Im} f = \{f(\mathbf{x})\}$, un sous-espace de l'espace d'arrivée ; pour une matrice, l'espace de ses colonnes | M12a |
| implication | implication, conditional | $P \Rightarrow Q$, fausse seulement si P est vraie et Q fausse | R4 |
| importance par permutation | permutation importance | le score d'un modèle entraîné, moins son score quand on mélange la colonne d'une feature, sur un jeu de validation | M08 |
| imputation | imputation | remplacer une valeur manquante par une valeur choisie (la moyenne, la médiane de la colonne…) | M02c |
| inclusion | inclusion, subset | $A \subset B$ : tout élément de $A$ est dans $B$ | R4 |
| indépendance (de variables aléatoires) | independence | la loi jointe est le produit des marginales : $P(X = x, Y = y) = P(X = x)\,P(Y = y)$ pour toutes les valeurs | M02b |
| indépendance deux à deux, mutuelle | pairwise, mutual independence | chaque paire d'événements est indépendante ; ou tous ensemble le sont : $P(A \cap B \cap C) = P(A)P(B)P(C)$ en plus. La première n'entraîne pas la seconde | M03 |
| indicatrice | indicator (variable) | variable qui vaut 1 si un événement se produit, 0 sinon (une Bernoulli) | M02b |
| indice (d'une somme) | index (of a sum) | la variable muette de $\sum_{k=m}^{n}$, qui va de $m$ à $n$ | R4 |
| inégalité de Cauchy-Schwarz | Cauchy-Schwarz inequality | $\lvert \vec{u} \cdot \vec{v} \rvert \le \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert$ | R9, M07 |
| inégalité de Gibbs | Gibbs' inequality | $\mathrm{KL}(p \parallel q) \ge 0$, avec égalité si et seulement si $p = q$ ; d'où $H(p, q) \ge H(p)$ | M06 |
| inégalité de Jensen | Jensen's inequality | pour $f$ convexe, $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$ ; l'inverse pour $f$ concave | M06 |
| inégalité de Kraft | Kraft inequality, Kraft-McMillan inequality | les longueurs $\ell_i$ d'un code préfixe binaire vérifient $\sum 2^{-\ell_i} \le 1$, et des longueurs qui la vérifient sont celles d'un code préfixe | M06 |
| inégalité triangulaire | triangle inequality | $\lVert \vec{u} + \vec{v} \rVert \le \lVert \vec{u} \rVert + \lVert \vec{v} \rVert$ : un côté d'un triangle est plus court que la somme des deux autres | R9, M07 |
| inégalité, inéquation | inequality | comparaison avec $<$, $\le$, $>$ ou $\ge$ ; une inéquation est une inégalité qui contient une inconnue | R2 |
| inertie (d'un nuage de points) | inertia, within-cluster sum of squares | $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2$ : la plus petite au barycentre ; ce que k-means fait baisser | M07 |
| information (de Shannon), surprise | self-information, surprisal, information content | $-\log_2 p$ bits : ce qu'apprend un événement de probabilité $p$ ; s'additionne pour des événements indépendants | M06 |
| information mutuelle | mutual information | $I(X ; Y) = H(X) - H(X \mid Y)$ : ce que l'une des variables apprend sur l'autre ; symétrique, nulle seulement pour des variables indépendantes | M06 |
| injective, surjective, bijective | injective, surjective, bijective | deux vecteurs distincts ont des images distinctes ($\ker f = \{\mathbf{0}\}$) ; tout vecteur d'arrivée est atteint ($\operatorname{Im} f = W$) ; les deux | M12a |
| intégrale | integral | $\int_a^b f(x)\,dx$ : l'aire algébrique entre la courbe et l'axe, limite des sommes de Riemann | M02a |
| intégrale de Gauss | Gaussian integral | $\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt{\pi}$ | M02a |
| intégrale double | double integral | le volume sous une surface $z = f(x, y)$ au-dessus d'une région ; sur un rectangle, on intègre une variable après l'autre | M02b |
| intégrale impropre | improper integral | intégrale sur un intervalle infini, ou d'une fonction non bornée, définie comme une limite ; elle converge ou diverge | M02a |
| intégration par parties | integration by parts | $\int_a^b u\,v' = [uv]_a^b - \int_a^b u'\,v$ | M02a |
| intérêts composés | compound interest | les intérêts de chaque période rapportent à leur tour : $C_n = C_0\,(1 + t)^n$ | R5 |
| intersection, réunion | intersection, union | $A \cap B$ : les éléments à la fois dans $A$ et dans $B$ ; $A \cup B$ : ceux qui sont dans l'un ou dans l'autre | R2, R4 |
| intervalle de confiance | confidence interval | intervalle calculé sur les données qui contient la vraie valeur pour 95 % (le niveau) des échantillons : $\bar{x} \pm 1{,}96\,\frac{s}{\sqrt{n}}$ | M02c |
| intervalle de crédibilité | credible interval | un intervalle qui contient le paramètre avec une probabilité donnée, selon l'a posteriori | M04 |
| intervalle de prédiction | prediction interval | intervalle où tombera une **nouvelle** observation ; plus large qu'un intervalle de confiance de la moyenne | M02c |
| intervalle de Wald, de Wilson | Wald interval, Wilson (score) interval | deux intervalles d'une proportion : $\hat{p} \pm z\sqrt{\hat{p}(1 - \hat{p})/n}$, faux avec peu de succès ; celui de Wilson, qui inverse un test, reste dans $[0, 1]$ | M08 |
| inverse d'une matrice | inverse matrix | la matrice $\mathbf{A}^{-1}$ telle que $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$ ; unique quand elle existe, seulement pour une matrice carrée | M09a |
| issue | outcome | un résultat possible d'une expérience aléatoire | R8 |
| jacobienne | Jacobian | matrice des dérivées partielles d'une fonction à valeurs vectorielles | M17 |
| k-means, k-means++ | k-means, k-means++ | regrouper des points en $k$ clusters en alternant l'affectation au centre le plus proche et le remplacement de chaque centre par le barycentre de son cluster ; k-means++ tire les centres de départ avec une probabilité proportionnelle à $D^2$ | M07 |
| König-Huygens (formule de) | König-Huygens theorem | $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2 + m\,\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$ | M07 |
| lasso | lasso | les moindres carrés pénalisés par $\lambda\lVert \mathbf{w} \rVert_1$ : des poids exactement nuls, pas de solution explicite en général | M09b |
| levier | leverage | $h_{ii}$, le nombre de la diagonale de la matrice chapeau : le poids de $y_i$ dans sa propre prédiction ; grand pour un point isolé | M09b |
| ligne de niveau | level curve, contour line | l'ensemble des points où $f(x, y)$ prend une valeur donnée $c$ ; une carte de lignes de niveau est une carte topographique de la surface | M05b |
| limite à droite, à gauche | right-hand, left-hand limit | limite quand $x$ s'approche de $a$ en restant plus grand (plus petit) que $a$ | R7 |
| limite d'une fonction | limit of a function | la valeur dont $f(x)$ s'approche quand $x$ tend vers $a$ ou vers $\pm\infty$ | R7 |
| limite d'une suite | limit of a sequence | le nombre $\ell$ dont les termes finissent par rester aussi près qu'on veut | R5 |
| linéairement séparable | linearly separable | deux classes qu'un hyperplan sépare ; pour des nuages finis, c'est équivalent à des enveloppes convexes disjointes | M10 |
| linéarité de l'espérance | linearity of expectation | $\mathbb{E}[aX + bY + c] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y] + c$, même pour des variables dépendantes | R8, M02b |
| lissage de Laplace | Laplace smoothing, additive smoothing | $\frac{k + 1}{n + 2}$, ou $\frac{n_j + 1}{n + K}$ : la moyenne a posteriori sous un a priori uniforme ; plus de probabilité nulle | M04 |
| log-probabilité, log-vraisemblance | log-probability, log-likelihood | le logarithme d'une probabilité, d'une vraisemblance : un produit devient une somme | R6, M06 |
| log-sum-exp | log-sum-exp | $\ln\sum_j e^{\ell_j} = m + \ln\sum_j e^{\ell_j - m}$ avec $m = \max_j \ell_j$ : normaliser des log-probabilités sans underflow | M04, M05a |
| logarithme décimal, binaire | common logarithm, binary logarithm | $\log_{10}$ (compte les chiffres), $\log_2$ (compte les doublements, les bits) | R6 |
| logarithme népérien | natural logarithm | $\ln$, la réciproque de exp : $\ln x$ est l'exposant $y$ tel que $e^y = x$ ; « log » en ML et en Python | R6 |
| logit | logit | $\ln \frac{p}{1 - p}$, la réciproque de la sigmoïde ; en deep learning, les scores avant la sigmoïde ou le softmax | R6 |
| loi (de probabilité) | (probability) distribution | façon dont une variable aléatoire répartit ses valeurs | R8, M02b |
| loi Beta | Beta distribution | la loi sur $[0, 1]$ de densité $\frac{\theta^{a - 1}(1 - \theta)^{b - 1}}{B(a, b)}$, de moyenne $\frac{a}{a + b}$ : la loi d'une proportion | M04 |
| loi binomiale | binomial distribution | le nombre de succès en $n$ essais indépendants de probabilité $p$ : $\binom{n}{k}p^k(1-p)^{n-k}$ | M02b |
| loi catégorielle (multinoulli) | categorical distribution | une classe parmi $K$, de probabilités $p_1, \ldots, p_K$ de somme 1 | M02b |
| loi de Bernoulli | Bernoulli distribution | vaut 1 avec la probabilité $p$, 0 sinon ; espérance $p$, variance $p(1 - p)$ | M02b |
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
| MAE | mean absolute error (MAE) | $\frac{1}{n}\sum \lvert r_i \rvert$, l'erreur absolue moyenne d'une régression, dans l'unité de la cible | M09b |
| mal conditionné | ill-conditioned | se dit d'un problème dont la solution change beaucoup quand les données changent un peu | R2 |
| malédiction de la dimension | curse of dimensionality | les surprises de la grande dimension : le volume se concentre près du bord, les distances se ressemblent | M02c, M07 |
| mantisse | significand, mantissa | le nombre $m$ de la notation scientifique $m \times 10^k$, avec $1 \le |m| < 10$ | R1 |
| MAP (maximum a posteriori) | maximum a posteriori (MAP) estimate | la valeur du paramètre qui maximise l'a posteriori : son mode | M04 |
| marche (fonction de Heaviside) | step function, Heaviside function | vaut 0 avant 0 et 1 après ; la valeur en 0 est une convention ; voir aussi « seuil (fonction) » | R3 |
| marge fonctionnelle | functional margin | $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ pour un point ; elle est multipliée par $c$ quand on multiplie $(\mathbf{w}, b)$ par $c$ | M10 |
| marge géométrique | geometric margin | $\min_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$ : la distance signée du point le plus mal placé à l'hyperplan ; la plus grande possible vaut la moitié de la distance entre les enveloppes convexes | M10 |
| Markov (inégalité de) | Markov's inequality | $P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$ pour une variable $X \ge 0$ et $a > 0$ | M02c, M11 |
| matrice | matrix | tableau de nombres à lignes et colonnes | M09a |
| matrice augmentée | augmented matrix | $[\mathbf{A} \mid \mathbf{b}]$, la matrice des coefficients suivie de la colonne des seconds membres, sur laquelle on fait le pivot de Gauss | M09a |
| matrice chapeau | hat matrix | $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, qui envoie $\mathbf{y}$ sur $\hat{\mathbf{y}}$ : symétrique, idempotente, de trace $p$ | M09b |
| matrice d'une application linéaire | transformation matrix | la matrice dont la colonne $j$ contient les coordonnées de $f(\mathbf{b}_j)$ dans la base de l'arrivée ; dans les bases canoniques, $f(\mathbf{e}_j)$ | M12a |
| matrice de confusion | confusion matrix | le tableau de contingence de la vérité et de la prédiction d'un classifieur (TP, FN, FP, TN en binaire) | M03 |
| matrice de corrélation | correlation matrix | la matrice des corrélations $\rho_{ij} = \frac{\Sigma_{ij}}{\sigma_i\sigma_j}$, avec des 1 sur la diagonale | M02c |
| matrice de covariance | covariance matrix | $\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$ : les variances sur la diagonale, symétrique, et $\sum_i\sum_j w_iw_j\Sigma_{ij} \ge 0$ | M02c |
| matrice des features | feature matrix, design matrix | le tableau $\mathbf{X}$ de forme $(n, p)$ : une ligne par exemple, une colonne par feature ($\mathbf{X}$, ou $\boldsymbol{\Phi}$ après une transformation des features, dans MML) | M09b |
| matrice diagonale | diagonal matrix | une matrice carrée dont les nombres hors de la diagonale sont nuls ; elle s'inverse nombre par nombre | M09a |
| matrice identité | identity matrix | $\mathbf{I}_n$ : des 1 sur la diagonale, des 0 ailleurs ; $\mathbf{I}\mathbf{A} = \mathbf{A}\mathbf{I} = \mathbf{A}$ | M09a |
| matrice inversible, singulière | invertible (regular, nonsingular) matrix, singular matrix | une matrice carrée qui a une inverse, ou qui n'en a pas (quand une colonne combine les autres, ou que le rang est plus petit que la taille) | M09a |
| matrice symétrique | symmetric matrix | une matrice égale à sa transposée : $a_{ij} = a_{ji}$ ; $\mathbf{X}^\top\mathbf{X}$ l'est toujours | M09a |
| matrices semblables, équivalentes | similar matrices, equivalent matrices | $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$, ou $\mathbf{T}^{-1}\mathbf{A}\mathbf{S}$ : la même application linéaire dans d'autres bases ; le rang ne change pas | M12a |
| maximum de vraisemblance (estimation du) | maximum likelihood estimate (MLE) | la valeur du paramètre qui rend les données observées les plus probables ; pour une proportion, la fréquence | M04 |
| maximum, minimum, extremum | maximum, minimum, extremum (extrema) | la plus grande (petite) valeur d'une fonction sur un ensemble | R3 |
| MCC (coefficient de Matthews) | Matthews correlation coefficient | la corrélation entre la vérité et la prédiction codées 0 et 1, entre $-1$ et 1 | M03 |
| médiane | median | la valeur du milieu d'une série triée (la moyenne des deux du milieu si $n$ est pair) ; robuste aux valeurs extrêmes | M02c |
| médiane géométrique | geometric median | le point qui minimise la somme des distances euclidiennes (non au carré) à des points ; sans formule, l'algorithme de Weiszfeld la calcule | M07 |
| mesures appariées | paired measurements | deux mesures de la même unité (avant et après) : on travaille sur leurs différences, et la variabilité entre unités disparaît | M08 |
| méthode de Chernoff | Chernoff method | appliquer Markov à $e^{\lambda X}$, puis choisir le meilleur $\lambda$ : d'où les bornes exponentielles, comme celle de Hoeffding | M11 |
| méthode de Monte-Carlo | Monte Carlo method | estimer une probabilité, une espérance ou une intégrale par la moyenne d'un grand nombre de tirages au hasard | M02a |
| méthode de Newton | Newton's method, Newton-Raphson | $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$ : suivre la tangente jusqu'à l'axe pour approcher une racine | M05a |
| méthode de Simpson | Simpson's rule | intégration numérique par des paraboles : $\frac{h}{3}(f_0 + 4f_1 + 2f_2 + \cdots + 4f_{n-1} + f_n)$, $n$ pair ; erreur en $h^4$ | M02a |
| méthode des trapèzes | trapezoidal rule | intégration numérique par des segments : $h\big(\frac{f_0}{2} + f_1 + \cdots + \frac{f_n}{2}\big)$ ; erreur en $h^2$ | M02a |
| milieu (d'un segment) | midpoint | le point dont les coordonnées sont les moyennes de celles des extrémités | R9 |
| mise à jour séquentielle | sequential updating | l'a posteriori d'une observation devient l'a priori de la suivante | M04 |
| mise en équation | setting up an equation, translating a word problem | traduire un énoncé en équation (ou en système) en choisissant les inconnues | R2 |
| mode | mode | la valeur la plus fréquente d'une série, ou le maximum d'une densité | M02c |
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
| négation | negation | la proposition « non P », vraie quand P est fausse | R4 |
| nier l'antécédent | denying the antecedent | le sophisme formel « $P \Rightarrow Q$ ; non $P$ ; donc non $Q$ » : non valide | M11 |
| nombre décimal | decimal number, terminating decimal | nombre qui s'écrit avec un nombre fini de chiffres après la virgule (ensemble 𝔻) | R1 |
| nombre dérivé | derivative at a point | $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$, la pente de la tangente en $a$ | R7 |
| nombre e | Euler's number | $e = \lim (1 + \frac{1}{n})^n \approx 2{,}718$, la base de l'exponentielle et de $\ln$ | R6 |
| nombre rationnel, irrationnel | rational, irrational number | quotient de deux entiers (ℚ) ; un réel qui n'en est pas un, comme $\sqrt{2}$ ou $\pi$ | R1 |
| normalisation min-max | min-max scaling | la fonction affine $\frac{x - \min}{\max - \min}$, qui ramène des données entre 0 et 1 | R3 |
| norme | norm | longueur d'un vecteur | R9, M07 |
| norme Lp | Lp norm, p-norm | $\big(\sum_i \lvert x_i \rvert^p\big)^{1/p}$, une norme pour $p \ge 1$ seulement ; elle diminue quand $p$ augmente, vers la norme L∞ | M07 |
| normes L1 et L∞ | L1 norm, infinity norm | $\sum \lvert x_i \rvert$ (un trajet fait seulement de pas horizontaux et verticaux) et $\max \lvert x_i \rvert$ ; sans indice, $\lVert \mathbf{x} \rVert$ est la norme euclidienne (L2) | R9, M07 |
| noyau (d'un notebook) | kernel | la mémoire qui exécute les cellules et garde leurs variables | R0 |
| noyau (d'une application linéaire) | kernel, null space | $\ker\mathbf{A} = \{\mathbf{x} : \mathbf{A}\mathbf{x} = \mathbf{0}\}$, un sous-espace de l'espace de départ : les directions que l'application écrase | M12a |
| numérateur, dénominateur | numerator, denominator | le nombre du haut et celui du bas d'une fraction | R1 |
| octet | byte | 8 bits ; 1 ko = $10^3$ octets, 1 Mo = $10^6$, 1 Go = $10^9$ | R1 |
| opérations élémentaires sur les lignes | elementary row operations | échanger deux lignes, multiplier une ligne par un nombre non nul, ajouter à une ligne un multiple d'une autre : elles ne changent pas les solutions | M09a |
| optimisme face à l'incertitude | optimism in the face of uncertainty | agir comme si chaque option valait le haut de son intervalle de confiance : le principe des stratégies UCB | M11 |
| oracle (d'un test) | test oracle | bibliothèque de confiance à laquelle un test compare ta fonction | R0 |
| ordre d'une méthode numérique | order of a numerical method | l'exposant $k$ d'une erreur proportionnelle à $h^k$ : diviser le pas par 2 divise l'erreur par $2^k$ | M02a |
| ordre de grandeur | order of magnitude | la puissance de 10 la plus proche d'un nombre | R1 |
| orthogonaux (vecteurs) | orthogonal vectors | de directions perpendiculaires : leur produit scalaire est nul | R9, M07 |
| overfitting, underfitting | overfitting, underfitting | un modèle trop souple, qui colle au bruit des données d'entraînement (grande variance) ; un modèle trop simple, qui rate la forme des données (grand biais) | M09b |
| p-valeur | p-value | la probabilité, calculée en supposant $H_0$ vraie, d'une statistique au moins aussi extrême que celle observée ; pas la probabilité que $H_0$ soit vraie | M08 |
| par colonne, par ligne | featurewise, samplewise | une opération sur chaque feature (la moyenne de chaque colonne, la standardisation) ; sur chaque exemple (la norme de chaque ligne) | M09a |
| parabole, sommet | parabola, vertex | la courbe d'un second degré ; son sommet $(\alpha, \beta)$ est son point le plus bas (ou le plus haut) | R3 |
| paradoxe de Simpson | Simpson's paradox | une tendance présente dans chaque groupe s'inverse quand on réunit les groupes, à cause de leurs poids différents | M03 |
| parcimonieux (modèle) | sparse model | un modèle dont beaucoup de poids sont exactement nuls, comme ceux du lasso | M09b |
| partie entière, plancher, plafond | floor, ceiling | $\lfloor x \rfloor$, le plus grand entier $\le x$ ; $\lceil x \rceil$, le plus petit entier $\ge x$ | R1 |
| partition (de l'univers) | partition | des événements deux à deux incompatibles dont la réunion est l'univers entier | M03 |
| pente, ordonnée à l'origine | slope, intercept | dans $mx + c$, $m$ est la variation pour $x + 1$, et $c = f(0)$ | R3 |
| percentile, quartile | percentile, quartile | le percentile $k$ est le quantile d'ordre $\frac{k}{100}$ ; les quartiles, les quantiles d'ordre 0,25, 0,5 et 0,75 | M02a |
| périodique, période | periodic, period | une fonction qui se répète : $f(x + T) = f(x)$ ; cos et sin ont pour période $2\pi$ | R9 |
| perplexité | perplexity | $2^{H(p, q)}$ (en bits) : le nombre de choix également probables entre lesquels un modèle hésite en moyenne | M06 |
| PGCD, PPCM | GCD (greatest common divisor), LCM (least common multiple) | plus grand diviseur commun, plus petit multiple commun de deux entiers | R1 |
| pivot | pivotal quantity | une fonction des données et du paramètre dont la loi ne dépend pas du paramètre ($\frac{\bar{X}}{\mu}$ pour une loi exponentielle) | M02c |
| pivot d'une forme échelonnée | pivot, leading coefficient | le premier nombre non nul d'une ligne ; le rang est le nombre de pivots | M09a |
| pivot de Gauss (élimination de Gauss) | Gaussian elimination | annuler les inconnues colonne par colonne par des opérations élémentaires (une forme échelonnée), puis remonter de la dernière équation à la première | M09a |
| pivot partiel | partial pivoting | prendre pour pivot, dans chaque colonne, l'élément de plus grande valeur absolue (en échangeant les lignes) : évite d'amplifier les erreurs d'arrondi | M09a |
| plan tangent | tangent plane | $z = f(a, b) + f_x(a, b)\,(x - a) + f_y(a, b)\,(y - b)$ : le plan qui touche la surface en un point, avec les mêmes pentes | M05b |
| plus proche voisin | nearest neighbor | le point d'un ensemble le plus proche d'un point donné ; il dépend de la distance choisie et des unités des features | M07 |
| point critique | critical point, stationary point | un point où la dérivée s'annule (en plusieurs variables : où le gradient s'annule) | M05a, M05b |
| point d'inflexion | inflection point | un point où la courbe passe de convexe à concave, ou l'inverse : $f''$ y change de signe | M05a |
| point de pourcentage | percentage point | écart entre deux pourcentages, obtenu en les soustrayant (de 4 % à 5 % : un point) | R1 |
| point fixe | fixed point | un $\ell$ tel que $f(\ell) = \ell$ : la limite possible d'une suite $u_{n+1} = f(u_n)$ | R5 |
| point selle | saddle point | un point critique où $f$ monte dans certaines directions et descend dans d'autres, comme un col de montagne | M05b |
| polynôme de Taylor, série de Taylor | Taylor polynomial, Taylor series | $\sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k$, le polynôme qui a les mêmes $n$ premières dérivées que $f$ en $a$ ; la série, quand $n \to \infty$ | M05a |
| polynôme, degré | polynomial, degree | somme de puissances entières de $x$ multipliées par des coefficients ; le degré est la plus grande puissance | R3 |
| population | population | l'ensemble (ou la loi) dont les données sont tirées, et dont on veut connaître les paramètres | M02c |
| position générale | general position | des points sans alignement particulier : dans le plan, jamais trois sur une même droite ; $d + 1$ points de $\mathbb{R}^d$ en position générale sont séparables quels que soient leurs labels | M10 |
| precision (valeur prédictive positive) | precision, positive predictive value (PPV) | $P(Y = 1 \mid \hat{Y} = 1)$ : la part des alertes justifiées ; elle dépend de la prévalence | M03 |
| prédicat | predicate | une phrase qui dépend d'une variable, comme « $x > 3$ » | R4 |
| prévalence | prevalence, base rate | $P(Y = 1)$ : la proportion de positifs dans la population ; voir aussi « taux de base » | M03 |
| primitive | antiderivative | une fonction $F$ telle que $F' = f$ ; deux primitives sur un intervalle diffèrent d'une constante | M02a |
| principe multiplicatif | rule of product | $a$ choix puis $b$ choix donnent $a \times b$ possibilités | R8 |
| probabilité conditionnelle | conditional probability | $P(A \mid B)$ : la probabilité de $A$ sachant que $B$ s'est réalisé | R8, M03 |
| probabilité jointe | joint probability | $P(A \cap B)$, ou $P(X = x, Y = y)$ : la probabilité que deux choses arrivent ensemble | M03 |
| probabilité marginale | marginal probability | la probabilité d'un événement sur une seule variable, en oubliant l'autre : un total de ligne ou de colonne divisé par le total | M03 |
| probabilités totales (formule des) | law of total probability | $P(A) = \sum_k P(A \mid B_k)\,P(B_k)$ pour une partition $B_1, \ldots, B_K$ | M03 |
| produit cartésien, couple | Cartesian product, ordered pair | $A \times B$ : les couples $(a, b)$ avec $a \in A$, $b \in B$ | R4 |
| produit matrice-vecteur | matrix-vector product | $\mathbf{A}\mathbf{x}$ : un produit scalaire par ligne de $\mathbf{A}$, ou la combinaison des colonnes de $\mathbf{A}$ de coefficients les $x_j$ | M09a |
| produit matriciel | matrix product, matrix multiplication | $(\mathbf{A}\mathbf{B})_{ij} = \sum_k a_{ik}b_{kj}$, pour $(n, p) \times (p, m) \to (n, m)$ ; associatif, pas commutatif, $n\,p\,m$ multiplications | M09a |
| produit nul (règle du) | zero-product property | un produit est nul si et seulement si l'un au moins de ses facteurs est nul | R2 |
| produit scalaire | dot product, inner product | $\sum_i x_i y_i$ ; mesure d'alignement de deux vecteurs | R9, M07 |
| produit vectoriel (du plan) | cross product (2-D) | $\mathbf{u} \times \mathbf{v} = u_1v_2 - u_2v_1$ : positif si $\mathbf{v}$ est à gauche de $\mathbf{u}$ ; sa valeur absolue est l'aire du parallélogramme | M10 |
| programme linéaire | linear program | une optimisation d'une fonction linéaire sous des contraintes linéaires ; de faisabilité quand on cherche seulement un point qui les vérifie toutes (`scipy.optimize.linprog`) | M10 |
| projection (sur une direction) | projection | l'ombre de $\vec{v}$ sur la direction de $\vec{u}$ : $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert^2}\vec{u}$ | R9, M07, M12b |
| projection orthogonale (sur un sous-espace) | orthogonal projection | le point d'un sous-espace (une droite en M07) le plus proche d'un vecteur : l'écart est orthogonal au sous-espace ; les moindres carrés projettent $\mathbf{y}$ sur l'espace des colonnes | M07, M09b |
| proposition | proposition, statement | une phrase qui est soit vraie, soit fausse | R4 |
| pseudo-observations | pseudo-counts | les paramètres $a$ et $b$ d'un a priori Beta, lus comme des succès et des échecs déjà vus | M04 |
| puissance | power | $a^n$, produit de $n$ facteurs égaux à $a$ | R1 |
| puissance d'un test | power (of a test) | $1 - \beta$, la probabilité de rejeter $H_0$ quand l'effet existe ; elle grandit avec l'effet, avec $n$ et avec $\alpha$ | M08 |
| quantificateur | quantifier | « pour tout » ($\forall$) ou « il existe » ($\exists$) | R4 |
| quantile | quantile | le plus petit $x$ tel que $F(x) \ge p$ ; la médiane est le quantile d'ordre 0,5 | M02a |
| quantité conjuguée | conjugate | multiplier $\sqrt{A} - \sqrt{B}$ par $\sqrt{A} + \sqrt{B}$ pour obtenir $A - B$ | R7 |
| queue (d'une loi), queue empirique | tail probability, empirical tail | $P(X \ge a)$ ; sur un échantillon, la proportion des valeurs $x_i \ge a$ | M11 |
| quotient, reste | quotient, remainder | les deux résultats de la division euclidienne | R0 |
| racine (d'une fonction) | root, zero | un $x$ tel que $f(x) = 0$ | R3 |
| racine carrée | square root | nombre positif ou nul dont le carré vaut $a$ | R1 |
| radian | radian | unité d'angle : la longueur de l'arc sur le cercle de rayon 1 ; $180° = \pi$ rad | R9 |
| raison (d'une suite) | common difference, common ratio | ce qu'on ajoute (suite arithmétique) ou ce par quoi on multiplie (suite géométrique) à chaque pas | R5 |
| rang | rank | le nombre de pivots, la dimension de l'espace des colonnes (et de celui des lignes) : $\operatorname{rg}(\mathbf{A}) = \operatorname{rg}(\mathbf{A}^\top) \le \min(m, n)$ | M09a, M12a |
| rang numérique | numerical rank | le rang calculé en virgule flottante, où « nul » veut dire « sous une tolérance » ; il dépend de la tolérance, et de l'échelle des nombres si elle est absolue | M12a |
| rang plein, rang déficient | full rank, rank deficient | $\operatorname{rg}(\mathbf{A}) = \min(m, n)$, ou moins | M12a |
| rasoir d'Occam | Occam's razor | à ajustement égal, préférer le modèle le plus simple ; l'évidence bayésienne le fait d'elle-même | M08 |
| rayon de confiance | confidence radius | la demi-largeur $r$ d'un intervalle $\bar{X} \pm r$ ; Hoeffding, au risque $\delta$ : $r = (b - a)\sqrt{\frac{\ln(2/\delta)}{2n}}$ | M11 |
| réalisation, tirage | realization, sample, draw | une valeur obtenue d'une variable aléatoire, à distinguer de la variable elle-même | M02b |
| recall (sensibilité) | recall, sensitivity, true positive rate (TPR) | $P(\hat{Y} = 1 \mid Y = 1)$ : la part des positifs détectés | M03 |
| réciproque (d'une implication) | converse | $Q \Rightarrow P$ pour l'implication $P \Rightarrow Q$ : une autre phrase | R4 |
| réciproque (fonction) | inverse function | la fonction $f^{-1}$ qui défait $f$ : $f^{-1}(f(x)) = x$ ; ce n'est pas $\frac{1}{f}$ | R3 |
| récurrence (raisonnement par) | (proof by) induction | démontrer $P(n_0)$, puis $P(n) \Rightarrow P(n + 1)$ pour tout $n \ge n_0$ | R4 |
| récurrence (suite définie par) | recursively defined sequence, recurrence relation | un premier terme et une règle $u_{n+1} = f(u_n)$ | R5 |
| rééchantillon | resample | $n$ valeurs tirées avec remise parmi les $n$ données (bootstrap) | M02c |
| règle de la chaîne | chain rule | $(g(u(x)))' = g'(u(x)) \times u'(x)$ : on dérive chaque étage d'une composée et on multiplie | R7, M05b |
| règle de la chaîne (de l'entropie) | chain rule for entropy | $H(X, Y) = H(X) + H(Y \mid X)$ : l'incertitude d'un couple, c'est celle de l'un plus ce qui reste sur l'autre | M06 |
| règle de la somme | sum rule | on obtient une marginale en sommant la loi jointe sur l'autre variable | M02b, M03 |
| règle de trois | rule of three | aucun événement en $n$ essais indépendants : à 95 %, sa probabilité est inférieure à environ $\frac{3}{n}$ | M11 |
| règle du produit (probabilités) | product rule | $P(A \cap B) = P(A \mid B)\,P(B)$ ; MML : $p(\mathbf{x}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{x})\,p(\mathbf{x})$ | M03 |
| règle du produit, du quotient | product rule, quotient rule | $(uv)' = u'v + uv'$ ; $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$ | R7 |
| régression ridge | ridge regression | les moindres carrés pénalisés par $\lambda\lVert \mathbf{w} \rVert^2$ : $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, toujours soluble pour $\lambda > 0$ ; le MAP d'un prior gaussien | M09b |
| regret | regret | $R_T = \sum_k \Delta_k\,\mathbb{E}[N_k(T)]$ : ce qu'une stratégie gagne en moins, en moyenne, que la meilleure option choisie à chaque pas | M11 |
| régularisation | regularization | ajouter à la loss une pénalité sur les poids (ridge, lasso) pour préférer les modèles simples | M09b |
| relation de Chasles | Chasles' relation | $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ | R9 |
| ReLU | rectified linear unit | $\max(0, z)$, l'activation la plus utilisée dans les réseaux | M10 |
| résidu | residual | $r_i = y_i - \hat{y}_i$ : la cible moins la prédiction | M09b |
| reste de Lagrange | Lagrange remainder | $f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - a)^{n+1}$ pour un $\xi$ entre $a$ et $x$ : il borne l'erreur d'un polynôme de Taylor | M05a |
| risque d'erreur de la famille | family-wise error rate (FWER) | la probabilité d'au moins un faux positif dans une famille de tests ; la correction de Bonferroni le garde sous $\alpha$ | M08 |
| risque empirique | empirical risk | la moyenne d'une loss sur les exemples d'entraînement ; apprendre, c'est choisir les paramètres qui le minimisent | M09b |
| sans biais (estimateur) | unbiased estimator | estimateur dont l'espérance est la vraie valeur du paramètre | M02c |
| sans mémoire | memoryless | $P(T > s + t) = P(T > s)\,P(T > t)$ : avoir attendu ne rapproche pas l'événement (lois géométrique et exponentielle) | M02b |
| schéma de Horner | Horner's method | évaluer un polynôme en multipliant par $x$ et en ajoutant le coefficient suivant, sans puissances | R3 |
| score de Brier | Brier score | $\frac{1}{n}\sum (p_i - y_i)^2$ : l'erreur quadratique moyenne des probabilités annoncées | M03 |
| sécante | secant line | droite qui passe par deux points de la courbe ; sa pente est le taux d'accroissement | R7 |
| second degré (polynôme du) | quadratic (polynomial, function) | $ax^2 + bx + c$ avec $a \ne 0$ | R3 |
| sens direct | counterclockwise | le sens inverse des aiguilles d'une montre ; les sommets d'une enveloppe convexe sont rangés dans ce sens | M10 |
| seuil (fonction) | step function | $H(z) = 1$ si $z > 0$, 0 sinon (la convention en 0 varie) ; l'activation d'un classifieur linéaire qui répond oui ou non ; c'est la fonction marche de R3 | M10 |
| seuil d'un test | significance level | $\alpha$, le risque de type I accepté : on rejette $H_0$ quand la p-valeur est au plus $\alpha$ (souvent 0,05) | M08 |
| seuil de décision | decision threshold | le score à partir duquel on déclare un exemple positif ; $\frac{c_{FP}}{c_{FP} + c_{FN}}$ minimise le coût pour des probabilités calibrées | M03 |
| seuillage doux | soft thresholding | $S(z, \gamma) = \operatorname{signe}(z)\max(\lvert z \rvert - \gamma, 0)$ : rapprocher $z$ de 0 de $\gamma$, ou le mettre à 0 ; la solution du lasso en dimension 1 | M09b |
| sigmoïde (fonction logistique) | sigmoid, logistic function | $\sigma(x) = \frac{1}{1 + e^{-x}}$, à valeurs dans $]0 \;;\; 1[$ | R6 |
| silhouette | silhouette (coefficient) | $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$, entre $-1$ et 1 : positive quand le point est en moyenne plus près des points de son cluster que de ceux du cluster voisin, négative quand il est plus près de ceux du cluster voisin, nulle à égalité | M07 |
| similarité cosinus | cosine similarity | $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert\,\lVert \vec{v} \rVert}$, le cosinus de l'angle entre deux vecteurs : compare leurs directions | R9, M07 |
| simulation par inversion | inverse transform sampling | si $U$ est uniforme sur $[0 ; 1]$, $F^{-1}(U)$ suit la loi de fonction de répartition $F$ | M02b |
| softmax, log-softmax | softmax, log-softmax | $\frac{e^{v_i}}{\sum_j e^{v_j}}$, calculée stablement avec $e^{v_i - m}$ ; son logarithme $v_i - \text{LSE}(\mathbf{v})$, qui reste fini | M05a |
| solution particulière, solution générale | particular solution, general solution | une solution d'un système ; toutes ses solutions, une solution particulière plus n'importe quelle solution du système homogène | M09a |
| somme de Riemann | Riemann sum | somme des aires de $n$ rectangles de largeur $h = \frac{b - a}{n}$, de hauteur lue à gauche, à droite ou au milieu | M02a |
| somme harmonique | harmonic number (harmonic series pour la série infinie) | $\sum_{t=1}^{T} \frac{1}{t}$, qui croît comme $\ln T$ : elle reste entre $\ln T$ et $1 + \ln T$ | M11 |
| somme infinie, série | infinite sum, series | la limite des sommes partielles ; $\sum_{k=0}^{+\infty} u_0\,q^k = \frac{u_0}{1 - q}$ si $\lvert q \rvert < 1$ | R5 |
| somme partielle | partial sum | la somme des $n$ premiers termes d'une suite | R5 |
| somme pondérée | weighted sum | $\sum w_i x_i + b$, sans division ; le calcul d'un neurone | R1 |
| somme télescopique | telescoping sum | $\sum (b_{k+1} - b_k) = b_{n+1} - b_1$ | R4 |
| sommes de carrés (totale, expliquée, résiduelle) | total, explained, residual sum of squares (SST, SSE, SSR) | $\mathrm{SCT} = \sum (y_i - \bar{y})^2$, $\mathrm{SCE} = \sum (\hat{y}_i - \bar{y})^2$, $\mathrm{SCR} = \sum r_i^2$ ; $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$ pour les moindres carrés avec ordonnée à l'origine | M09b |
| sommet (d'une enveloppe convexe) | vertex | un point du nuage qui n'est pas combinaison convexe des autres : un coin du polygone | M10 |
| sophisme formel | formal fallacy | une forme d'argument qui a l'air valide sans l'être : affirmer le conséquent, nier l'antécédent | M11 |
| sous-espace affine | affine subspace | un sous-espace vectoriel déplacé, $\mathbf{x}_0 + U$ : une droite ou un plan qui ne passe pas par l'origine, les solutions de $\mathbf{A}\mathbf{x} = \mathbf{b}$ | M12a |
| sous-espace engendré | span | $\operatorname{Vect}(\mathbf{v}_1, \ldots, \mathbf{v}_k)$ : l'ensemble des combinaisons linéaires de ces vecteurs, le plus petit sous-espace qui les contient | M12a |
| sous-espace vectoriel | vector subspace | une partie qui contient $\mathbf{0}$ et est stable par combinaison linéaire ; elle est elle-même un espace vectoriel | M12a |
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
| système homogène | homogeneous system | un système de second membre nul, $\mathbf{A}\mathbf{x} = \mathbf{0}$ ; il a toujours la solution $\mathbf{0}$ | M09a |
| système linéaire | system of linear equations, linear system | plusieurs équations du premier degré à résoudre ensemble ; leurs solutions communes | R2, M09a |
| table de vérité | truth table | la valeur d'une proposition pour chaque combinaison des valeurs de ses propositions | R4 |
| tableau de contingence | contingency table | le tableau des effectifs de deux variables catégorielles observées ensemble, avec ses totaux dans les marges | M03 |
| tableau de variations | variation table (sign chart) | tableau du signe de $f'$ et du sens de variation de $f$, avec les valeurs aux points où $f'$ s'annule | R7 |
| taille d'échantillon (calcul de) | sample size calculation | le nombre d'observations qui donne une puissance voulue : $n \ge \big(\frac{(z_{1-\alpha} + z_{1-\beta})\,\sigma}{\delta}\big)^2$ pour une moyenne | M08 |
| taille de l'effet | effect size | l'ampleur de l'écart mesuré, que la p-valeur ne mesure pas : avec beaucoup de données, un effet minuscule devient significatif | M08 |
| taille du pas, learning rate | step size, learning rate | le nombre $\eta > 0$ qui règle la longueur d'un pas de descente de gradient | M05b |
| tangente | tangent line | droite qui touche la courbe en un point avec la même pente : $y = f(a) + f'(a)(x - a)$ | R7 |
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
| test du second ordre | second-derivative test | en un point critique, le signe de $D = f_{xx}f_{yy} - f_{xy}^2$ (et celui de $f_{xx}$) dit minimum, maximum ou point selle ; $D = 0$ : il ne conclut pas | M05b |
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
| tirage avec remise, sans remise | sampling with replacement, without replacement | avec remise, l'objet tiré est remis avant le tirage suivant (les tirages sont i.i.d.) ; sans remise, la composition change et les tirages sont dépendants | R8, M02c |
| tranche (d'une surface) | slice, cross-section | la courbe obtenue en figeant une variable, comme $x \mapsto f(x, b)$ ; $\frac{\partial f}{\partial x}(a, b)$ est sa pente en $a$ | M05b |
| transposée | transpose | $\mathbf{A}^\top$, les lignes devenues colonnes : $(\mathbf{A}^\top)_{ij} = a_{ji}$, et $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ | M09a |
| triangle de Pascal | Pascal's triangle | les coefficients binomiaux rangés en triangle : chaque nombre est la somme des deux au-dessus | R8 |
| unilatéral, bilatéral (test) | one-sided, two-sided test | l'alternative dans un seul sens, fixé à l'avance, ou dans les deux | M08 |
| unité d'arrondi | unit roundoff | l'erreur relative maximale d'une opération en flottants, $u = \frac{\varepsilon}{2}$ ($2^{-53}$ en `float64`) | M05a |
| univers | sample space | $\Omega$, l'ensemble des issues d'une expérience aléatoire | R8 |
| valeur aberrante | outlier | valeur très éloignée des autres ; signalée par $\lvert z \rvert > 3$ ou par la règle de Tukey | M02c |
| valeur absolue | absolute value | $\lvert x \rvert$, le nombre sans son signe ; $\lvert a - b \rvert$ est la distance entre $a$ et $b$ | R2 |
| valeur interdite | excluded value | valeur de l'inconnue qui annule un dénominateur | R2 |
| valeur moyenne d'une fonction | mean value of a function | $\frac{1}{b - a}\int_a^b f$ : la hauteur du rectangle de même aire | M02a |
| valeur prédictive négative | negative predictive value (NPV) | $P(Y = 0 \mid \hat{Y} = 0)$ : la part des « négatif » prédits qui le sont vraiment | M03 |
| valeur propre, vecteur propre | eigenvalue, eigenvector | $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ : une direction que $\mathbf{A}$ ne fait qu'étirer | M12c |
| validation croisée imbriquée | nested cross-validation | une boucle intérieure choisit le modèle, une boucle extérieure estime la performance de toute la procédure, choix compris | M08 |
| valide, solide (argument) | valid, sound | valide : la conclusion est vraie partout où les prémisses le sont toutes ; solide : valide et à prémisses vraies | M11 |
| variable aléatoire | random variable | grandeur dont la valeur dépend du hasard | R8 |
| variable de base, variable libre | basic variable, free variable | une inconnue dont la colonne porte un pivot, ou n'en porte pas ; on choisit les libres, les autres s'en déduisent | M09a |
| variable de confusion | confounder, confounding variable | une troisième grandeur qui fait varier deux autres, et crée entre elles une corrélation sans causalité | M02c |
| variance | variance | moyenne des carrés des écarts à l'espérance | R8 |
| variance d'échantillon | sample variance | $s^2 = \frac{1}{n - 1}\sum (x_i - \bar{x})^2$, estimateur sans biais de $\sigma^2$ ; $s_n^2$ divise par $n$ | M02c |
| vecteur | vector | un déplacement (une direction, un sens, une longueur), donné par ses coordonnées ; en ML, une liste de nombres | R9 |
| vecteur de support | support vector | un point à la distance exactement $\gamma^\star$ de l'hyperplan de plus grande marge : il touche un bord de la bande, et ce sont ces points qui fixent l'hyperplan | M10, M13b |
| vecteur directeur, vecteur normal | direction vector, normal vector | un vecteur qui a la direction d'une droite ; un vecteur qui lui est perpendiculaire | R9, M07 |
| vecteur one-hot | one-hot vector | le codage d'une catégorie : un 1 à sa place, des 0 ailleurs (un vecteur de la base canonique) | M07 |
| vecteur unitaire | unit vector | un vecteur de norme 1 ; $\frac{\vec{u}}{\lVert \vec{u} \rVert}$ normalise $\vec{u}$ | R9, M07 |
| vrai positif, vrai négatif | true positive, true negative (TP, TN) | un positif prédit positif ; un négatif prédit négatif | M03 |
| vraisemblance | likelihood | probabilité des données, vue comme fonction des paramètres | M04 |
| weight decay | weight decay | la pénalité L2 vue dans une descente de gradient : $\mathbf{w} \leftarrow (1 - 2\eta\lambda)\mathbf{w} - \eta\nabla L(\mathbf{w})$ | M09b |
| z-score (score standard) | standard score, z-score | $z = \frac{x - \bar{x}}{s}$ : le nombre d'écarts-types entre une valeur et la moyenne | M02c |
