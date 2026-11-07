# Glossaire français ↔ anglais

Les termes mathématiques sont en français dans les fiches, avec l'anglais en glose à leur première apparition : c'est l'anglais que tu liras dans MML. Les termes du machine learning gardent l'usage de workbookIA (loss, learning rate, batch, feature… restent en anglais). Chaque chapitre ajoute ses termes ; la colonne « Chapitre » renvoie à celui qui le définit.

| Français | Anglais | Définition courte | Chapitre |
|---|---|---|---|
| a priori conjugué | conjugate prior | un a priori dont l'a posteriori est de la même famille ; la loi Beta pour la binomiale : $\mathrm{Beta}(a, b) \to \mathrm{Beta}(a + k,\ b + n - k)$ | M04 |
| a priori, a posteriori | prior, posterior | la loi d'un paramètre ou d'une hypothèse avant de voir les données ; après, sachant les données | M04 |
| absorption | absorption (swamping) | un petit nombre ajouté à un grand disparaît à l'arrondi : $10^{16} + 1$ donne $10^{16}$ en `float64` | M05a |
| accuracy | accuracy | $P(\hat{Y} = Y)$ : la proportion de prédictions justes ; trompeuse quand une classe est rare | M03 |
| actualiser, valeur actuelle | discount, present value | ramener une somme future à sa valeur d'aujourd'hui : la diviser par $(1 + t)^n$ | R5 |
| aire algébrique | signed area | aire comptée positivement au-dessus de l'axe, négativement en dessous : c'est ce que mesure une intégrale | M02a |
| angle entre deux vecteurs | angle between two vectors | l'angle $\theta \in [0 ; \pi]$ tel que $\vec{u} \cdot \vec{v} = \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert\cos\theta$ | R9 |
| annulation (catastrophique) | catastrophic cancellation | la perte de chiffres justes quand on soustrait deux nombres presque égaux : l'erreur relative explose | M05a |
| antécédent, image | preimage, image | $f(x)$ est l'image de $x$ ; un antécédent de $y$ est un $x$ tel que $f(x) = y$ | R3 |
| application linéaire | linear map, linear mapping | fonction entre espaces vectoriels qui respecte sommes et multiplications par un nombre | M12a |
| approximation affine | linear approximation | $f(a + h) \approx f(a) + f'(a)\,h$ : la courbe remplacée par sa tangente près de $a$ | R7 |
| arbre pondéré | probability tree | arbre des étapes d'une expérience, chaque branche portant sa probabilité : on multiplie le long d'un chemin, on additionne les chemins | R8 |
| arccosinus | arccosine, arccos | la réciproque du cosinus sur $[0 ; \pi]$ : l'unique angle de $[0 ; \pi]$ qui a un cosinus donné | R9 |
| argmax, argmin | argmax, argmin | la valeur de $x$ où une fonction atteint son maximum (son minimum), pas la valeur de ce maximum | R3, M05b |
| arrangement | k-permutation | choix ordonné de $k$ objets distincts parmi $n$ : $\frac{n!}{(n - k)!}$ possibilités | R8 |
| arrondi, troncature | rounding, truncation | arrondir garde le nombre le plus proche ; tronquer coupe sans regarder la suite | R1 |
| astuce de reparamétrisation | reparameterization trick | écrire $X = \mu + \sigma Z$ avec $Z \sim \mathcal{N}(0, 1)$ : le hasard est dans $Z$, et $\mu$, $\sigma$ deviennent des paramètres qu'on peut ajuster par gradient | M02b |
| asymptote | asymptote | droite dont la courbe se rapproche indéfiniment : horizontale ($y = L$) ou verticale ($x = a$) | R7 |
| AUC (aire sous la courbe ROC) | area under the curve | $\int_0^1 \text{TPR}\,d(\text{FPR})$ : 1/2 pour le hasard, 1 pour un classement parfait | M02a, M03 |
| average precision | average precision (AP) | $\sum_j (R_j - R_{j-1})\,P_j$ : l'aire, en rectangles, sous la courbe precision-recall | M03 |
| balanced accuracy | balanced accuracy | la moyenne des recalls des classes ; 0,5 pour un modèle qui prédit toujours la même classe | M03 |
| base (d'un espace vectoriel) | basis | famille de vecteurs indépendants qui engendre tout l'espace | M12a |
| biais (d'un estimateur) | bias | $\mathbb{E}[\hat{\theta}] - \theta$ : l'erreur systématique d'un estimateur, en moyenne sur tous les échantillons | M02c |
| biais (d'un neurone) | bias | nombre $b$ ajouté à la somme pondérée d'un neurone, appris comme les poids | R1 |
| biais d'échantillonnage | sampling bias | un échantillon qui ne représente pas la population visée, à cause de la façon dont il a été collecté ; plus de données ne le corrigent pas | M02c |
| biais du survivant | survivorship bias | n'observer que ce qui a passé un filtre (les avions rentrés de mission, les prêts accordés), et conclure comme si c'était tout | M02c |
| Bienaymé-Tchebychev (inégalité de) | Chebyshev's inequality | $P(\lvert X - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$, pour toute loi de variance finie | M02c |
| bit, nat | bit, nat | unités d'information : un événement de probabilité $p$ apporte $-\log_2 p$ bits, ou $-\ln p$ nats ; 1 bit ≈ 0,693 nat | R6 |
| boîte à moustaches | boxplot, box-and-whisker plot | dessin d'une série : une boîte de $Q_1$ à $Q_3$ coupée par la médiane, des moustaches jusqu'aux valeurs non aberrantes les plus extrêmes | M02c |
| bootstrap | bootstrap | estimer la dispersion d'une statistique en la recalculant sur des milliers de rééchantillons tirés avec remise dans les données | M02c |
| borne, intervalle | bound, interval | ensemble des réels compris entre deux bornes, incluses (crochet fermé) ou non (crochet ouvert) ; une borne peut être infinie | R2 |
| calcul symbolique | symbolic computation | calcul exact sur des expressions avec des lettres (SymPy), sans valeurs approchées | R0 |
| calibration | calibration | un modèle est calibré si $P(Y = 1 \mid \text{score} = p) = p$ : ses probabilités sont honnêtes | M03 |
| cardinal | cardinality | le nombre d'éléments d'un ensemble fini, noté $\lvert A \rvert$ | R4 |
| cellule (d'un notebook) | cell | bloc de code ou de texte qu'on exécute d'un coup | R0 |
| cercle trigonométrique | unit circle | le cercle de centre $O$ et de rayon 1, parcouru dans le sens inverse des aiguilles d'une montre | R9 |
| changement de base (formule de) | change of base formula | $\log_b x = \frac{\ln x}{\ln b}$ | R6 |
| changement de variable | change of variables, substitution | $\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$ | M02a |
| chiffres significatifs | significant figures | les chiffres d'un nombre à partir du premier chiffre non nul | R1 |
| classe positive | positive class | la classe que l'on cherche à détecter (la panne, le défaut), codée 1 | M03 |
| coefficient | coefficient | nombre qui multiplie la partie littérale d'un terme : 7 dans $7x^2$ | R2 |
| coefficient binomial | binomial coefficient | $\binom{n}{k}$, « k parmi n » : le nombre de façons de choisir $k$ objets parmi $n$, sans ordre | R8 |
| coefficient multiplicateur | multiplier, growth factor | nombre $1 + t$ par lequel une évolution de taux $t$ multiplie une valeur | R1 |
| colinéaires (vecteurs) | collinear vectors | l'un est un multiple de l'autre : $xy' - x'y = 0$ | R9 |
| combinaison linéaire | linear combination | somme de vecteurs multipliés par des nombres | M12a |
| complémentaire (d'un ensemble) | complement | $\bar{A}$ : les éléments de l'univers qui ne sont pas dans $A$ | R4 |
| composée (de deux fonctions) | composition, composite function | $(f \circ g)(x) = f(g(x))$ : on applique $g$, puis $f$ | R3 |
| concave | concave | dont toute corde est au-dessous de la courbe ; pour $f$ deux fois dérivable, $f'' \le 0$ | M05a |
| condition nécessaire, suffisante | necessary, sufficient condition | dans $P \Rightarrow Q$, P est suffisante pour Q et Q nécessaire pour P | R4 |
| continuité | continuity | $f$ est continue en $a$ si $\lim_{x \to a} f(x) = f(a)$ : pas de saut | R7 |
| contraposée | contrapositive | $\text{non } Q \Rightarrow \text{non } P$, de même valeur que $P \Rightarrow Q$ | R4 |
| contre-exemple | counterexample | un cas qui rend fausse une phrase « pour tout » | R4 |
| convergence linéaire, quadratique | linear, quadratic convergence | l'erreur est multipliée par une constante $< 1$ à chaque pas (linéaire), ou à peu près élevée au carré (quadratique : les décimales justes doublent) | M05a |
| convergent (estimateur) | consistent estimator | estimateur dont l'erreur tend vers 0 quand la taille de l'échantillon grandit | M02c |
| converger, diverger (suite) | converge, diverge | une suite converge si elle a une limite finie ; sinon elle diverge (vers $\pm\infty$, ou sans limite) | R5 |
| convexe | convex | dont tout segment entre deux points reste au-dessus de la courbe (fonction) ou dans l'ensemble | M05a, M10 |
| coordonnées polaires | polar coordinates | repérer un point du plan par sa distance $r$ à l'origine et son angle $\theta$ ; dans une intégrale double, $dx\,dy$ devient $r\,dr\,d\theta$ | M02b |
| coordonnées, repère orthonormé | coordinates, orthonormal frame | un repère a une origine et deux axes perpendiculaires de même unité ; un point y est repéré par $(x ; y)$ | R9 |
| corrélation (coefficient de) | correlation coefficient (Pearson) | $r = \frac{\operatorname{Cov}(x, y)}{s_x s_y}$, entre $-1$ et 1 : la force d'une relation **linéaire** ; le cosinus de l'angle entre les vecteurs d'écarts | M02c |
| cosinus, sinus | cosine, sine | l'abscisse et l'ordonnée du point d'angle $\theta$ du cercle trigonométrique | R9 |
| cote, log-cote | odds, log-odds | la cote d'une probabilité $p$ est $\frac{p}{1 - p}$ ; la log-cote, son logarithme | R6 |
| couple de variables aléatoires | pair of random variables, random vector | deux variables définies sur le même univers, étudiées ensemble par leur loi jointe | M02b |
| courbe precision-recall | precision-recall curve | pour chaque seuil, le point (recall, precision) ; elle dépend de la prévalence | M03 |
| courbe représentative | graph (of a function) | l'ensemble des points $(x, f(x))$ | R3 |
| courbe ROC | ROC curve (receiver operating characteristic) | pour chaque seuil, le point (taux de faux positifs, recall) : un escalier de (0, 0) à (1, 1) | M03 |
| couverture | coverage | proportion des échantillons pour lesquels un intervalle de confiance contient la vraie valeur | M02c |
| covariance empirique | empirical (sample) covariance | $\frac{1}{n}\sum (x_i - \bar{x})(y_i - \bar{y})$ (ou divisée par $n - 1$) : la moyenne des produits des écarts | M02c |
| croissances comparées | growth rates comparison | pour $x$ très grand, $\ln x \ll x^k \ll a^x$ ($k > 0$, $a > 1$) | R6 |
| croissante, décroissante | increasing, decreasing | qui conserve (retourne) l'ordre sur un intervalle : $a < b \Rightarrow f(a) \le f(b)$ ($\ge$) | R3 |
| ddof | ddof (delta degrees of freedom) | le nombre retranché à $n$ au dénominateur d'une variance : `ddof=0` divise par $n$, `ddof=1` par $n - 1$ | M02c |
| débordement, sous-dépassement | overflow, underflow | un résultat trop grand (ou trop petit) pour un flottant ; NumPy rend `inf` (ou 0) | R6, M05a |
| décade, échelle logarithmique | decade, logarithmic scale | sur un axe logarithmique, des écarts égaux sont des rapports égaux ; une décade est un facteur 10 | R6 |
| décibel | decibel (dB) | un rapport $R$ exprimé par $10 \log_{10} R$ ; le PSNR se mesure en décibels | R6 |
| degrés de liberté | degrees of freedom | le nombre de valeurs libres : les $n$ écarts à la moyenne ont une somme nulle, donc $n - 1$ degrés de liberté | M02c |
| démonstration par l'absurde | proof by contradiction | supposer la conclusion fausse et aboutir à une contradiction | R4 |
| dénombrement | counting | l'art de compter des possibilités sans les lister : principe multiplicatif, factorielles, combinaisons | R8 |
| densité de probabilité | probability density function (pdf) | fonction positive d'aire totale 1 : $P(a \le X \le b) = \int_a^b f$ ; une probabilité par unité de longueur, qui peut dépasser 1 | M02a |
| densité jointe | joint density | fonction $f(x, y) \ge 0$ d'intégrale double 1, telle que $P((X, Y) \in D) = \iint_D f$ | M02b |
| dérivée | derivative | pente de la tangente, taux de variation instantané | R7 |
| dérivée partielle | partial derivative | dérivée par rapport à une variable, les autres fixées | M05b |
| dérivée seconde | second derivative | la dérivée de $f'$, notée $f''$ : son signe dit si la pente augmente (courbe convexe) ou diminue (concave) | M05a |
| dérivée, fonction dérivée | derivative | la fonction $x \mapsto f'(x)$ qui donne la pente de la tangente en chaque point | R7 |
| déterminant | determinant | le nombre $ad - bc$ d'un système 2 × 2, non nul exactement quand il a une seule solution (R2) ; facteur de changement d'aire ou de volume d'une application linéaire (M12c) | R2, M12c |
| développer, factoriser | expand, factor | transformer un produit en somme ; transformer une somme en produit | R2 |
| diagramme de fiabilité | reliability diagram | pour des paquets de scores, la probabilité moyenne annoncée contre la fréquence observée ; la diagonale si le modèle est calibré | M03 |
| dichotomie | bisection | trouver un zéro en coupant l'intervalle en deux et en gardant la moitié où le signe change | R7 |
| différence finie (avant, centrée) | finite difference (forward, central) | une approximation de $f'(x)$ par $\frac{f(x + h) - f(x)}{h}$ (ordre 1) ou $\frac{f(x + h) - f(x - h)}{2h}$ (ordre 2) | M05a |
| discriminant | discriminant | $\Delta = b^2 - 4ac$ ; son signe donne le nombre de racines de $ax^2 + bx + c$ | R3 |
| disjonction de cas | proof by cases | découper en cas qui couvrent toutes les possibilités, et traiter chacun | R4 |
| distance (entre deux points) | distance | $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$, la norme du vecteur $\overrightarrow{AB}$ | R9 |
| division euclidienne | Euclidean division, integer division | $a = bq + r$ avec $0 \le r < b$ ; en Python, `a // b` donne $q$ et `a % b` donne $r$ | R0 |
| écart interquartile | interquartile range (IQR) | $Q_3 - Q_1$ : la dispersion de la moitié centrale d'une série, insensible aux valeurs extrêmes | M02c |
| écart-type | standard deviation | racine carrée de la variance | R8 |
| échantillon i.i.d. | i.i.d. sample | variables $X_1, \ldots, X_n$ indépendantes et de même loi : le modèle de base des données en statistique et en ML | M02c |
| échantillonnage de Thompson | Thompson sampling | choisir à chaque essai l'option dont un tirage dans l'a posteriori est le plus grand : explorer et exploiter à la fois | M04 |
| effectif attendu | expected count | l'effectif d'une case d'un tableau de contingence si les variables étaient indépendantes : $\frac{\text{total de la ligne} \times \text{total de la colonne}}{\text{total}}$ | M03 |
| effet de masque | masking effect | une valeur aberrante gonfle l'écart-type et cache ainsi son propre z-score | M02c |
| égalité des taux d'erreur | equalized odds | critère d'équité : le même recall et le même taux de faux positifs dans chaque groupe | M03 |
| empreinte | hash | code calculé à partir d'une donnée, d'où l'on ne peut pas la retrouver ; sert à comparer sans stocker | R0 |
| ensemble | set | collection d'éléments distincts | R4 |
| ensemble de définition | domain | l'ensemble des $x$ pour lesquels $f(x)$ a un sens | R3 |
| ensemble des solutions | solution set | l'ensemble de toutes les valeurs qui rendent une équation (ou une inéquation) vraie | R2 |
| entier naturel, entier relatif | natural number, integer | ℕ = {0, 1, 2…} ; ℤ ajoute les entiers négatifs | R1 |
| epsilon machine | machine epsilon | l'écart entre 1 et le flottant suivant : $2^{-52} \approx 2{,}2 \times 10^{-16}$ en `float64` | M05a |
| équation | equation | égalité qui contient une inconnue ; la résoudre, c'est trouver toutes ses solutions | R2 |
| équation cartésienne, équation réduite | Cartesian equation, slope-intercept form | $ax + by + c = 0$, qui convient à toute droite ; $y = mx + p$, pour une droite non verticale | R9 |
| équations équivalentes | equivalent equations | équations qui ont exactement les mêmes solutions | R2 |
| équiprobabilité | equally likely outcomes | toutes les issues ont la même probabilité : $P(A) = \frac{\lvert A \rvert}{\lvert \Omega \rvert}$ | R8 |
| équivalence (logique) | equivalence, if and only if | $P \Leftrightarrow Q$ : $P \Rightarrow Q$ et $Q \Rightarrow P$ | R4 |
| erreur d'arrondi, erreur de troncature | rounding error, truncation error | l'erreur due à la précision finie des flottants ; l'erreur due à une formule approchée (un développement coupé, un pas $h$ non nul) | M05a |
| erreur quadratique moyenne (d'un estimateur) | mean squared error (MSE) | $\mathbb{E}[(\hat{\theta} - \theta)^2] = \text{biais}^2 + \text{variance}$ | M02c |
| erreur type | standard error (SE) | l'écart-type d'un estimateur ; pour une moyenne, $\frac{s}{\sqrt{n}}$ ; pour une proportion, $\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$ | M02c |
| espace probabilisé | probability space | le triplet (univers, événements, probabilité) d'une expérience aléatoire | M02b |
| espace vectoriel | vector space | ensemble où l'on peut additionner des vecteurs et les multiplier par des nombres | M12a |
| espérance | expected value, expectation | moyenne théorique d'une variable aléatoire | R8 |
| estimateur | estimator | formule qui estime un paramètre à partir de données | M02c |
| estimation (valeur) | estimate | la valeur d'un estimateur calculée sur les données observées | M02c |
| estimation de Fermi | Fermi estimate | ordre de grandeur obtenu en découpant une question en facteurs faciles à estimer | R1 |
| événement | event | partie de l'univers : les issues pour lesquelles une phrase est vraie | R8 |
| événements incompatibles | mutually exclusive events, disjoint events | événements sans issue commune : $A \cap B = \varnothing$ | R8 |
| événements indépendants | independent events | $P(A \cap B) = P(A)\,P(B)$ : savoir que l'un s'est réalisé ne change pas la probabilité de l'autre | R8 |
| évidence (vraisemblance marginale) | evidence, marginal likelihood | $P(O) = \sum_j P(O \mid H_j)\,P(H_j)$ : le dénominateur de la formule de Bayes | M04 |
| exponentielle (fonction) | exponential function | $x \mapsto a^x$ ($a > 0$) ; la fonction exponentielle est $\exp(x) = e^x$ | R6 |
| exposant | exponent | le nombre $n$ de $a^n$ ; en notation scientifique, la puissance de 10 | R1 |
| expression littérale, variable | algebraic expression, variable | expression où des lettres, les variables, représentent des nombres | R2 |
| extrapolation de Richardson | Richardson extrapolation | combiner deux approximations de pas $h$ et $\frac{h}{2}$ pour annuler le premier terme d'erreur : $\frac{4D(h/2) - D(h)}{3}$ | M05a |
| extremum local, global | local, global extremum | maximum ou minimum au voisinage d'un point (local) ou sur tout le domaine (global) | R7, M05a |
| F-beta | F-beta score | $\frac{(1 + \beta^2)PR}{\beta^2 P + R}$ : moyenne harmonique pondérée de la precision et du recall ; $\beta > 1$ favorise le recall | M03 |
| facteur de correction de population finie | finite population correction | $\frac{N - n}{N - 1}$ : le facteur de la variance de la moyenne pour des tirages sans remise | M02c |
| factorielle | factorial | $n! = n \times (n - 1) \times \cdots \times 1$, le nombre de rangements de $n$ objets ; $0! = 1$ | R8 |
| famille exponentielle | exponential family | les lois de la forme $h(x)\exp(\eta\,T(x) - A(\eta))$ : Bernoulli, gaussienne, Beta, Poisson… | M04 |
| faux positif, faux négatif | false positive, false negative (FP, FN) | un négatif prédit positif (fausse alerte) ; un positif prédit négatif (cas manqué) | M03 |
| flottant (nombre à virgule flottante) | floating-point number, float | nombre à virgule rangé avec un nombre fixe de chiffres binaires, donc souvent arrondi | R0, M05a |
| fonction | function | règle qui associe à chaque élément de son ensemble de définition une seule image | R3 |
| fonction affine, linéaire | affine function, linear function | $x \mapsto mx + c$ ; linéaire quand $c = 0$ | R3 |
| fonction Beta, fonction Gamma | Beta function, Gamma function | $B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)}$ ; $\Gamma(n) = (n - 1)!$ pour un entier $n \ge 1$ | M04 |
| fonction d'erreur | error function, erf | $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$, un nom donné à cette intégrale sans primitive usuelle | M02a |
| fonction de masse | probability mass function (pmf) | $p(x) = P(X = x)$ pour une variable discrète : positive, de somme 1 | M02b |
| fonction de répartition | cumulative distribution function (cdf) | $F(x) = P(X \le x)$ : croissante de 0 à 1, et $F' = f$ pour une densité $f$ | M02a |
| fonction définie par morceaux | piecewise function | une formule sur chaque partie de l'ensemble de définition : $\max(0, x)$, la marche, $\lvert x \rvert$ | R3 |
| fonction quantile | quantile function | la réciproque $F^{-1}$ de la fonction de répartition : $F^{-1}(u) = q_u$ | M02a, M02b |
| fonction signe | sign function | $\operatorname{sign}(x)$ vaut $-1$, 0 ou 1 selon que $x$ est négatif, nul ou positif | R2 |
| forme canonique | vertex form, completed-square form | $a(x - \alpha)^2 + \beta$, qui montre le sommet d'une parabole | R3 |
| forme indéterminée | indeterminate form | $\infty - \infty$, $\frac{\infty}{\infty}$, $0 \times \infty$, $\frac{0}{0}$ : une limite qui ne se décide pas d'avance | R7 |
| formule d'Al-Kashi | law of cosines | $c^2 = a^2 + b^2 - 2ab\cos\hat{C}$ dans un triangle quelconque : Pythagore corrigé par l'angle | R9 |
| formule de Bayes | Bayes' theorem | $P(H \mid O) = \frac{P(O \mid H)\,P(H)}{P(O)}$ : a posteriori = vraisemblance × a priori / évidence | M04 |
| formule de Cramer | Cramer's rule | la solution d'un système de déterminant non nul, écrite comme quotients de déterminants | R2 |
| fraction irréductible | irreducible fraction, fraction in lowest terms | fraction dont numérateur et dénominateur n'ont plus d'autre diviseur commun que 1 | R1 |
| fréquence | (relative) frequency | nombre de fois où un événement se réalise, divisé par le nombre d'essais | R8 |
| fréquentiste, bayésien | frequentist, Bayesian | deux lectures des probabilités : une fréquence à long terme, le paramètre étant fixe ; un degré de croyance sur le paramètre | M04 |
| générateur pseudo-aléatoire, graine | pseudo-random number generator, seed | programme qui calcule une suite d'apparence aléatoire à partir d'une graine ; la même graine redonne la même suite | R8 |
| gradient | gradient | vecteur des dérivées partielles | M05b |
| grand O | big O | $f = O(g)$ : $f$ ne croît pas plus vite que $g$, à une constante près ; mesure le coût d'un algorithme | R7 |
| hérédité, initialisation | inductive step, base case | les deux étapes d'une récurrence : $P(n) \Rightarrow P(n + 1)$, et $P(n_0)$ | R4 |
| hessienne | Hessian | matrice des dérivées secondes | M19 |
| identité remarquable | special product, algebraic identity | égalité vraie pour tous $a$ et $b$, comme $(a + b)^2 = a^2 + 2ab + b^2$ | R2 |
| implication | implication, conditional | $P \Rightarrow Q$, fausse seulement si P est vraie et Q fausse | R4 |
| imputation | imputation | remplacer une valeur manquante par une valeur choisie (la moyenne, la médiane de la colonne…) | M02c |
| inclusion | inclusion, subset | $A \subset B$ : tout élément de $A$ est dans $B$ | R4 |
| indépendance (de variables aléatoires) | independence | la loi jointe est le produit des marginales : $P(X = x, Y = y) = P(X = x)\,P(Y = y)$ pour toutes les valeurs | M02b |
| indépendance deux à deux, mutuelle | pairwise, mutual independence | chaque paire d'événements est indépendante ; ou tous ensemble le sont : $P(A \cap B \cap C) = P(A)P(B)P(C)$ en plus. La première n'entraîne pas la seconde | M03 |
| indicatrice | indicator (variable) | variable qui vaut 1 si un événement se produit, 0 sinon (une Bernoulli) | M02b |
| indice (d'une somme) | index (of a sum) | la variable muette de $\sum_{k=m}^{n}$, qui va de $m$ à $n$ | R4 |
| inégalité de Cauchy-Schwarz | Cauchy-Schwarz inequality | $\lvert \vec{u} \cdot \vec{v} \rvert \le \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert$ | R9, M07 |
| inégalité triangulaire | triangle inequality | $\lVert \vec{u} + \vec{v} \rVert \le \lVert \vec{u} \rVert + \lVert \vec{v} \rVert$ : un côté d'un triangle est plus court que la somme des deux autres | R9 |
| inégalité, inéquation | inequality | comparaison avec $<$, $\le$, $>$ ou $\ge$ ; une inéquation est une inégalité qui contient une inconnue | R2 |
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
| issue | outcome | un résultat possible d'une expérience aléatoire | R8 |
| jacobienne | Jacobian | matrice des dérivées partielles d'une fonction à valeurs vectorielles | M17 |
| limite à droite, à gauche | right-hand, left-hand limit | limite quand $x$ s'approche de $a$ en restant plus grand (plus petit) que $a$ | R7 |
| limite d'une fonction | limit of a function | la valeur dont $f(x)$ s'approche quand $x$ tend vers $a$ ou vers $\pm\infty$ | R7 |
| limite d'une suite | limit of a sequence | le nombre $\ell$ dont les termes finissent par rester aussi près qu'on veut | R5 |
| linéarité de l'espérance | linearity of expectation | $\mathbb{E}[aX + bY + c] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y] + c$, même pour des variables dépendantes | R8, M02b |
| lissage de Laplace | Laplace smoothing, additive smoothing | $\frac{k + 1}{n + 2}$, ou $\frac{n_j + 1}{n + K}$ : la moyenne a posteriori sous un a priori uniforme ; plus de probabilité nulle | M04 |
| log-probabilité, log-vraisemblance | log-probability, log-likelihood | le logarithme d'une probabilité, d'une vraisemblance : un produit devient une somme | R6 |
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
| loi géométrique | geometric distribution | le rang du premier succès : $(1 - p)^{k-1}p$ pour $k \ge 1$, d'espérance $\frac{1}{p}$ | M02b |
| loi jointe | joint distribution | la loi d'un couple : $P(X = x, Y = y)$ pour toutes les paires de valeurs | M02b |
| loi marginale | marginal distribution | la loi d'une seule variable d'un couple, obtenue en sommant (ou en intégrant) l'autre | M02b |
| loi normale (gaussienne) | normal (Gaussian) distribution | loi en cloche $\mathcal{N}(\mu, \sigma^2)$, de centre $\mu$ et d'écart-type $\sigma$ (le second paramètre est la variance) | M02b |
| loi normale centrée réduite | standard normal distribution | $\mathcal{N}(0, 1)$, de densité $\varphi$ et de fonction de répartition $\Phi$ | M02b |
| loi prédictive (a posteriori) | posterior predictive distribution | la loi des prochaines observations, sachant les données, en moyennant sur le paramètre | M04 |
| loi uniforme | uniform distribution | densité constante $\frac{1}{b - a}$ sur $[a ; b]$ : une probabilité proportionnelle à la longueur | M02b |
| lois de De Morgan | De Morgan's laws | non (P et Q) = (non P) ou (non Q) ; non (P ou Q) = (non P) et (non Q) | R4 |
| mal conditionné | ill-conditioned | se dit d'un problème dont la solution change beaucoup quand les données changent un peu | R2 |
| malédiction de la dimension | curse of dimensionality | les surprises de la grande dimension : le volume se concentre près du bord, les distances se ressemblent | M02c |
| mantisse | significand, mantissa | le nombre $m$ de la notation scientifique $m \times 10^k$, avec $1 \le |m| < 10$ | R1 |
| MAP (maximum a posteriori) | maximum a posteriori (MAP) estimate | la valeur du paramètre qui maximise l'a posteriori : son mode | M04 |
| marche (fonction de Heaviside) | step function, Heaviside function | vaut 0 avant 0 et 1 après ; la valeur en 0 est une convention | R3 |
| Markov (inégalité de) | Markov's inequality | $P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$ pour une variable $X \ge 0$ et $a > 0$ | M02c |
| matrice | matrix | tableau de nombres à lignes et colonnes | M09a |
| matrice de confusion | confusion matrix | le tableau de contingence de la vérité et de la prédiction d'un classifieur (TP, FN, FP, TN en binaire) | M03 |
| matrice de corrélation | correlation matrix | la matrice des corrélations $\rho_{ij} = \frac{\Sigma_{ij}}{\sigma_i\sigma_j}$, avec des 1 sur la diagonale | M02c |
| matrice de covariance | covariance matrix | $\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$ : les variances sur la diagonale, symétrique, et $\sum_i\sum_j w_iw_j\Sigma_{ij} \ge 0$ | M02c |
| maximum de vraisemblance (estimation du) | maximum likelihood estimate (MLE) | la valeur du paramètre qui rend les données observées les plus probables ; pour une proportion, la fréquence | M04 |
| maximum, minimum, extremum | maximum, minimum, extremum (extrema) | la plus grande (petite) valeur d'une fonction sur un ensemble | R3 |
| MCC (coefficient de Matthews) | Matthews correlation coefficient | la corrélation entre la vérité et la prédiction codées 0 et 1, entre $-1$ et 1 | M03 |
| médiane | median | la valeur du milieu d'une série triée (la moyenne des deux du milieu si $n$ est pair) ; robuste aux valeurs extrêmes | M02c |
| méthode de Monte-Carlo | Monte Carlo method | estimer une probabilité, une espérance ou une intégrale par la moyenne d'un grand nombre de tirages au hasard | R8, M02a |
| méthode de Newton | Newton's method, Newton-Raphson | $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$ : suivre la tangente jusqu'à l'axe pour approcher une racine | M05a |
| méthode de Simpson | Simpson's rule | intégration numérique par des paraboles : $\frac{h}{3}(f_0 + 4f_1 + 2f_2 + \cdots + 4f_{n-1} + f_n)$, $n$ pair ; erreur en $h^4$ | M02a |
| méthode des trapèzes | trapezoidal rule | intégration numérique par des segments : $h\big(\frac{f_0}{2} + f_1 + \cdots + \frac{f_n}{2}\big)$ ; erreur en $h^2$ | M02a |
| milieu (d'un segment) | midpoint | le point dont les coordonnées sont les moyennes de celles des extrémités | R9 |
| mise à jour séquentielle | sequential updating | l'a posteriori d'une observation devient l'a priori de la suivante | M04 |
| mise en équation | setting up an equation, translating a word problem | traduire un énoncé en équation (ou en système) en choisissant les inconnues | R2 |
| mode | mode | la valeur la plus fréquente d'une série, ou le maximum d'une densité | M02c |
| moindres carrés | least squares | méthode qui minimise la somme des carrés des écarts | M09b |
| moyenne exponentielle | exponential moving average (EMA) | $v_t = \beta\,v_{t-1} + (1 - \beta)\,x_t$ : une moyenne qui oublie le passé progressivement | R5 |
| moyenne harmonique | harmonic mean | inverse de la moyenne des inverses ; vitesse moyenne, score F1 | R1 |
| moyenne macro, micro, pondérée | macro, micro, weighted average | moyenne simple des classes ; mesure calculée sur les comptages additionnés ; moyenne pondérée par les effectifs | M03 |
| moyenne mobile | moving average | la moyenne des $k$ dernières valeurs, recalculée à chaque instant | R5 |
| moyenne pondérée | weighted mean, weighted average | $\frac{\sum w_i x_i}{\sum w_i}$ : chaque valeur compte selon son poids | R1 |
| négation | negation | la proposition « non P », vraie quand P est fausse | R4 |
| nombre décimal | decimal number, terminating decimal | nombre qui s'écrit avec un nombre fini de chiffres après la virgule (ensemble 𝔻) | R1 |
| nombre dérivé | derivative at a point | $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$, la pente de la tangente en $a$ | R7 |
| nombre e | Euler's number | $e = \lim (1 + \frac{1}{n})^n \approx 2{,}718$, la base de l'exponentielle et de $\ln$ | R6 |
| nombre rationnel, irrationnel | rational, irrational number | quotient de deux entiers (ℚ) ; un réel qui n'en est pas un, comme $\sqrt{2}$ ou $\pi$ | R1 |
| normalisation min-max | min-max scaling | la fonction affine $\frac{x - \min}{\max - \min}$, qui ramène des données entre 0 et 1 | R3 |
| norme | norm | longueur d'un vecteur | R9, M07 |
| normes L1 et L∞ | L1 norm, infinity norm | $\sum \lvert x_i \rvert$ (un trajet fait seulement de pas horizontaux et verticaux) et $\max \lvert x_i \rvert$ ; sans indice, $\lVert \mathbf{x} \rVert$ est la norme euclidienne (L2) | R9, M07 |
| noyau (d'un notebook) | kernel | la mémoire qui exécute les cellules et garde leurs variables | R0 |
| noyau (d'une application linéaire) | kernel, null space | vecteurs envoyés sur zéro | M12a |
| numérateur, dénominateur | numerator, denominator | le nombre du haut et celui du bas d'une fraction | R1 |
| octet | byte | 8 bits ; 1 ko = $10^3$ octets, 1 Mo = $10^6$, 1 Go = $10^9$ | R1 |
| oracle (d'un test) | test oracle | bibliothèque de confiance à laquelle un test compare ta fonction | R0 |
| ordre d'une méthode numérique | order of a numerical method | l'exposant $k$ d'une erreur proportionnelle à $h^k$ : diviser le pas par 2 divise l'erreur par $2^k$ | M02a |
| ordre de grandeur | order of magnitude | la puissance de 10 la plus proche d'un nombre | R1 |
| orthogonaux (vecteurs) | orthogonal vectors | de directions perpendiculaires : leur produit scalaire est nul | R9 |
| parabole, sommet | parabola, vertex | la courbe d'un second degré ; son sommet $(\alpha, \beta)$ est son point le plus bas (ou le plus haut) | R3 |
| paradoxe de Simpson | Simpson's paradox | une tendance présente dans chaque groupe s'inverse quand on réunit les groupes, à cause de leurs poids différents | M03 |
| partie entière, plancher, plafond | floor, ceiling | $\lfloor x \rfloor$, le plus grand entier $\le x$ ; $\lceil x \rceil$, le plus petit entier $\ge x$ | R1 |
| partition (de l'univers) | partition | des événements deux à deux incompatibles dont la réunion est l'univers entier | M03 |
| pente, ordonnée à l'origine | slope, intercept | dans $mx + c$, $m$ est la variation pour $x + 1$, et $c = f(0)$ | R3 |
| percentile, quartile | percentile, quartile | le percentile $k$ est le quantile d'ordre $\frac{k}{100}$ ; les quartiles, les quantiles d'ordre 0,25, 0,5 et 0,75 | M02a |
| périodique, période | periodic, period | une fonction qui se répète : $f(x + T) = f(x)$ ; cos et sin ont pour période $2\pi$ | R9 |
| PGCD, PPCM | GCD (greatest common divisor), LCM (least common multiple) | plus grand diviseur commun, plus petit multiple commun de deux entiers | R1 |
| pivot | pivotal quantity | une fonction des données et du paramètre dont la loi ne dépend pas du paramètre ($\frac{\bar{X}}{\mu}$ pour une loi exponentielle) | M02c |
| point critique | critical point, stationary point | un point où la dérivée s'annule | M05a |
| point d'inflexion | inflection point | un point où la courbe passe de convexe à concave, ou l'inverse : $f''$ y change de signe | M05a |
| point de pourcentage | percentage point | écart entre deux pourcentages, obtenu en les soustrayant (de 4 % à 5 % : un point) | R1 |
| point fixe | fixed point | un $\ell$ tel que $f(\ell) = \ell$ : la limite possible d'une suite $u_{n+1} = f(u_n)$ | R5 |
| polynôme de Taylor, série de Taylor | Taylor polynomial, Taylor series | $\sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k$, le polynôme qui a les mêmes $n$ premières dérivées que $f$ en $a$ ; la série, quand $n \to \infty$ | M05a |
| polynôme, degré | polynomial, degree | somme de puissances entières de $x$ multipliées par des coefficients ; le degré est la plus grande puissance | R3 |
| population | population | l'ensemble (ou la loi) dont les données sont tirées, et dont on veut connaître les paramètres | M02c |
| precision (valeur prédictive positive) | precision, positive predictive value (PPV) | $P(Y = 1 \mid \hat{Y} = 1)$ : la part des alertes justifiées ; elle dépend de la prévalence | M03 |
| prédicat | predicate | une phrase qui dépend d'une variable, comme « $x > 3$ » | R4 |
| prévalence | prevalence, base rate | $P(Y = 1)$ : la proportion de positifs dans la population | M03 |
| primitive | antiderivative | une fonction $F$ telle que $F' = f$ ; deux primitives sur un intervalle diffèrent d'une constante | M02a |
| principe multiplicatif | rule of product | $a$ choix puis $b$ choix donnent $a \times b$ possibilités | R8 |
| probabilité conditionnelle | conditional probability | $P(A \mid B)$ : la probabilité de $A$ sachant que $B$ s'est réalisé | R8, M03 |
| probabilité jointe | joint probability | $P(A \cap B)$, ou $P(X = x, Y = y)$ : la probabilité que deux choses arrivent ensemble | M03 |
| probabilité marginale | marginal probability | la probabilité d'un événement sur une seule variable, en oubliant l'autre : un total de ligne ou de colonne divisé par le total | M03 |
| probabilités totales (formule des) | law of total probability | $P(A) = \sum_k P(A \mid B_k)\,P(B_k)$ pour une partition $B_1, \ldots, B_K$ | M03 |
| produit cartésien, couple | Cartesian product, ordered pair | $A \times B$ : les couples $(a, b)$ avec $a \in A$, $b \in B$ | R4 |
| produit nul (règle du) | zero-product property | un produit est nul si et seulement si l'un au moins de ses facteurs est nul | R2 |
| produit scalaire | dot product, inner product | $\sum_i x_i y_i$ ; mesure d'alignement de deux vecteurs | R9, M07 |
| projection (sur une direction) | projection | l'ombre de $\vec{v}$ sur la direction de $\vec{u}$ : $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert^2}\vec{u}$ | R9, M12b |
| proposition | proposition, statement | une phrase qui est soit vraie, soit fausse | R4 |
| pseudo-observations | pseudo-counts | les paramètres $a$ et $b$ d'un a priori Beta, lus comme des succès et des échecs déjà vus | M04 |
| puissance | power | $a^n$, produit de $n$ facteurs égaux à $a$ | R1 |
| quantificateur | quantifier | « pour tout » ($\forall$) ou « il existe » ($\exists$) | R4 |
| quantile | quantile | le plus petit $x$ tel que $F(x) \ge p$ ; la médiane est le quantile d'ordre 0,5 | M02a |
| quantité conjuguée | conjugate | multiplier $\sqrt{A} - \sqrt{B}$ par $\sqrt{A} + \sqrt{B}$ pour obtenir $A - B$ | R7 |
| quotient, reste | quotient, remainder | les deux résultats de la division euclidienne | R0 |
| racine (d'une fonction) | root, zero | un $x$ tel que $f(x) = 0$ | R3 |
| racine carrée | square root | nombre positif ou nul dont le carré vaut $a$ | R1 |
| radian | radian | unité d'angle : la longueur de l'arc sur le cercle de rayon 1 ; $180° = \pi$ rad | R9 |
| raison (d'une suite) | common difference, common ratio | ce qu'on ajoute (suite arithmétique) ou ce par quoi on multiplie (suite géométrique) à chaque pas | R5 |
| rang | rank | nombre de directions indépendantes d'une matrice | M12a |
| réalisation, tirage | realization, sample, draw | une valeur obtenue d'une variable aléatoire, à distinguer de la variable elle-même | M02b |
| recall (sensibilité) | recall, sensitivity, true positive rate (TPR) | $P(\hat{Y} = 1 \mid Y = 1)$ : la part des positifs détectés | M03 |
| réciproque (d'une implication) | converse | $Q \Rightarrow P$ pour l'implication $P \Rightarrow Q$ : une autre phrase | R4 |
| réciproque (fonction) | inverse function | la fonction $f^{-1}$ qui défait $f$ : $f^{-1}(f(x)) = x$ ; ce n'est pas $\frac{1}{f}$ | R3 |
| récurrence (raisonnement par) | (proof by) induction | démontrer $P(n_0)$, puis $P(n) \Rightarrow P(n + 1)$ pour tout $n \ge n_0$ | R4 |
| récurrence (suite définie par) | recursively defined sequence, recurrence relation | un premier terme et une règle $u_{n+1} = f(u_n)$ | R5 |
| rééchantillon | resample | $n$ valeurs tirées avec remise parmi les $n$ données (bootstrap) | M02c |
| règle de la chaîne | chain rule | $(g(u(x)))' = g'(u(x)) \times u'(x)$ : on dérive chaque étage d'une composée et on multiplie | R7 |
| règle de la somme | sum rule | on obtient une marginale en sommant la loi jointe sur l'autre variable | M02b, M03 |
| règle du produit (probabilités) | product rule | $P(A \cap B) = P(A \mid B)\,P(B)$ ; MML : $p(\mathbf{x}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{x})\,p(\mathbf{x})$ | M03 |
| règle du produit, du quotient | product rule, quotient rule | $(uv)' = u'v + uv'$ ; $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$ | R7 |
| relation de Chasles | Chasles' relation | $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ | R9 |
| reste de Lagrange | Lagrange remainder | $f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - a)^{n+1}$ pour un $\xi$ entre $a$ et $x$ : il borne l'erreur d'un polynôme de Taylor | M05a |
| sans biais (estimateur) | unbiased estimator | estimateur dont l'espérance est la vraie valeur du paramètre | M02c |
| sans mémoire | memoryless | $P(T > s + t) = P(T > s)\,P(T > t)$ : avoir attendu ne rapproche pas l'événement (lois géométrique et exponentielle) | M02b |
| schéma de Horner | Horner's method | évaluer un polynôme en multipliant par $x$ et en ajoutant le coefficient suivant, sans puissances | R3 |
| score de Brier | Brier score | $\frac{1}{n}\sum (p_i - y_i)^2$ : l'erreur quadratique moyenne des probabilités annoncées | M03 |
| sécante | secant line | droite qui passe par deux points de la courbe ; sa pente est le taux d'accroissement | R7 |
| second degré (polynôme du) | quadratic (polynomial, function) | $ax^2 + bx + c$ avec $a \ne 0$ | R3 |
| seuil de décision | decision threshold | le score à partir duquel on déclare un exemple positif ; $\frac{c_{FP}}{c_{FP} + c_{FN}}$ minimise le coût pour des probabilités calibrées | M03 |
| sigmoïde (fonction logistique) | sigmoid, logistic function | $\sigma(x) = \frac{1}{1 + e^{-x}}$, à valeurs dans $]0 \;;\; 1[$ | R6 |
| similarité cosinus | cosine similarity | $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert\,\lVert \vec{v} \rVert}$, le cosinus de l'angle entre deux vecteurs : compare leurs directions | R9 |
| simulation par inversion | inverse transform sampling | si $U$ est uniforme sur $[0 ; 1]$, $F^{-1}(U)$ suit la loi de fonction de répartition $F$ | M02b |
| softmax, log-softmax | softmax, log-softmax | $\frac{e^{v_i}}{\sum_j e^{v_j}}$, calculée stablement avec $e^{v_i - m}$ ; son logarithme $v_i - \text{LSE}(\mathbf{v})$, qui reste fini | M05a |
| somme de Riemann | Riemann sum | somme des aires de $n$ rectangles de largeur $h = \frac{b - a}{n}$, de hauteur lue à gauche, à droite ou au milieu | M02a |
| somme infinie, série | infinite sum, series | la limite des sommes partielles ; $\sum_{k=0}^{+\infty} u_0\,q^k = \frac{u_0}{1 - q}$ si $\lvert q \rvert < 1$ | R5 |
| somme partielle | partial sum | la somme des $n$ premiers termes d'une suite | R5 |
| somme pondérée | weighted sum | $\sum w_i x_i + b$, sans division ; le calcul d'un neurone | R1 |
| somme télescopique | telescoping sum | $\sum (b_{k+1} - b_k) = b_{n+1} - b_1$ | R4 |
| spécificité | specificity, true negative rate | $P(\hat{Y} = 0 \mid Y = 0)$ : la part des négatifs bien reconnus | M03 |
| standardiser | standardize | passer de $X \sim \mathcal{N}(\mu, \sigma^2)$ à $Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$ | M02b, M02c |
| statistique | statistic | une fonction de l'échantillon (moyenne, médiane, maximum) : une variable aléatoire | M02c |
| statistique suffisante | sufficient statistic | un résumé des données qui contient toute leur information sur le paramètre ; pour $n$ essais de Bernoulli, le nombre de succès | M04 |
| Student (loi de) | Student's t distribution | loi qui remplace la loi normale pour la moyenne standardisée de peu de données normales, quand $\sigma$ est estimé (quantile 2,262 pour $n = 10$ à 95 %) | M02c |
| substituer | substitute, plug in | remplacer une lettre par une valeur (ou par une expression) | R2 |
| suite | sequence | liste infinie de nombres $u_0, u_1, \dots$ | R5 |
| suite arithmétique | arithmetic sequence, arithmetic progression | on ajoute la même raison $r$ à chaque pas : $u_n = u_0 + n\,r$ | R5 |
| suite géométrique | geometric sequence, geometric progression | on multiplie par la même raison $q$ à chaque pas : $u_n = u_0\,q^n$ | R5 |
| support (d'une loi) | support | l'ensemble des valeurs où la densité n'est pas nulle | M02a |
| surdispersion | overdispersion | des comptages dont la variance dépasse nettement la moyenne : la loi de Poisson ne convient pas | M02b |
| système linéaire | system of linear equations, linear system | plusieurs équations du premier degré à résoudre ensemble ; leurs solutions communes | R2 |
| table de vérité | truth table | la valeur d'une proposition pour chaque combinaison des valeurs de ses propositions | R4 |
| tableau de contingence | contingency table | le tableau des effectifs de deux variables catégorielles observées ensemble, avec ses totaux dans les marges | M03 |
| tableau de variations | variation table | tableau du signe de $f'$ et du sens de variation de $f$, avec les valeurs aux points où $f'$ s'annule | R7 |
| tangente | tangent line | droite qui touche la courbe en un point avec la même pente : $y = f(a) + f'(a)(x - a)$ | R7 |
| tangente hyperbolique | hyperbolic tangent | $\tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}}$, à valeurs dans $]-1 \;;\; 1[$ | R6 |
| taux d'accroissement | rate of change, difference quotient | $\frac{f(a + h) - f(a)}{h}$ : la pente de la sécante, une vitesse moyenne | R7 |
| taux d'évolution | rate of change, percentage change | $\frac{V_a - V_d}{V_d}$, la variation rapportée à la valeur de départ | R1 |
| taux de faux positifs | false positive rate (FPR) | $P(\hat{Y} = 1 \mid Y = 0) = 1 - \text{spécificité}$ : l'abscisse de la courbe ROC | M03 |
| temps de doublement, demi-vie | doubling time, half-life | la durée au bout de laquelle une grandeur double (ou est divisée par 2) : $\frac{\ln 2}{\ln(1 + r)}$ | R6 |
| terme, rang (d'une suite) | term, index | $u_n$ est le terme de rang (ou d'indice) $n$ | R5 |
| termes semblables, réduire | like terms, collect like terms | termes de même partie littérale ; réduire, c'est les additionner en additionnant leurs coefficients | R2 |
| théorème central limite | central limit theorem (CLT) | pour $n$ grand, la moyenne de $n$ variables i.i.d. suit à peu près $\mathcal{N}\big(\mu, \frac{\sigma^2}{n}\big)$, quelle que soit leur loi | M02c |
| théorème de Fubini | Fubini's theorem | une intégrale double sur un rectangle se calcule en intégrant une variable après l'autre, dans n'importe quel ordre | M02b |
| théorème de transfert | law of the unconscious statistician (LOTUS) | $\mathbb{E}[g(X)] = \sum g(x)\,P(X = x)$ ou $\int g(x)\,f(x)\,dx$, sans chercher la loi de $g(X)$ | M02b |
| théorème des valeurs intermédiaires | intermediate value theorem | une fonction continue sur $[a ; b]$ prend toutes les valeurs entre $f(a)$ et $f(b)$ | R7 |
| théorème fondamental de l'analyse | fundamental theorem of calculus | $\int_a^b f = F(b) - F(a)$ pour une primitive $F$ ; la fonction aire a pour dérivée $f$ | M02a |
| tirage avec / sans remise | sampling with / without replacement | remettre ou non chaque valeur tirée : avec remise, les tirages sont i.i.d. ; sans remise, ils sont dépendants | M02c |
| tirage avec remise, sans remise | sampling with replacement, without replacement | avec remise, l'objet tiré est remis avant le tirage suivant ; sans remise, la composition change | R8 |
| triangle de Pascal | Pascal's triangle | les coefficients binomiaux rangés en triangle : chaque nombre est la somme des deux au-dessus | R8 |
| unité d'arrondi | unit roundoff | l'erreur relative maximale d'une opération en flottants, $u = \frac{\varepsilon}{2}$ ($2^{-53}$ en `float64`) | M05a |
| univers | sample space | $\Omega$, l'ensemble des issues d'une expérience aléatoire | R8 |
| valeur aberrante | outlier | valeur très éloignée des autres ; signalée par $\lvert z \rvert > 3$ ou par la règle de Tukey | M02c |
| valeur absolue | absolute value | $\lvert x \rvert$, le nombre sans son signe ; $\lvert a - b \rvert$ est la distance entre $a$ et $b$ | R2 |
| valeur interdite | excluded value | valeur de l'inconnue qui annule un dénominateur | R2 |
| valeur moyenne d'une fonction | mean value of a function | $\frac{1}{b - a}\int_a^b f$ : la hauteur du rectangle de même aire | M02a |
| valeur prédictive négative | negative predictive value (NPV) | $P(Y = 0 \mid \hat{Y} = 0)$ : la part des « négatif » prédits qui le sont vraiment | M03 |
| valeur propre, vecteur propre | eigenvalue, eigenvector | $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ : une direction que $\mathbf{A}$ ne fait qu'étirer | M12c |
| variable aléatoire | random variable | grandeur dont la valeur dépend du hasard | R8 |
| variable de confusion | confounder, confounding variable | une troisième grandeur qui fait varier deux autres, et crée entre elles une corrélation sans causalité | M02c |
| variance | variance | moyenne des carrés des écarts à l'espérance | R8 |
| variance d'échantillon | sample variance | $s^2 = \frac{1}{n - 1}\sum (x_i - \bar{x})^2$, estimateur sans biais de $\sigma^2$ ; $s_n^2$ divise par $n$ | M02c |
| vecteur | vector | un déplacement (une direction, un sens, une longueur), donné par ses coordonnées ; en ML, une liste de nombres | R9 |
| vecteur directeur, vecteur normal | direction vector, normal vector | un vecteur qui a la direction d'une droite ; un vecteur qui lui est perpendiculaire | R9 |
| vecteur unitaire | unit vector | un vecteur de norme 1 ; $\frac{\vec{u}}{\lVert \vec{u} \rVert}$ normalise $\vec{u}$ | R9 |
| vrai positif, vrai négatif | true positive, true negative (TP, TN) | un positif prédit positif ; un négatif prédit négatif | M03 |
| vraisemblance | likelihood | probabilité des données, vue comme fonction des paramètres | M04 |
| z-score (score standard) | standard score, z-score | $z = \frac{x - \bar{x}}{s}$ : le nombre d'écarts-types entre une valeur et la moyenne | M02c |
