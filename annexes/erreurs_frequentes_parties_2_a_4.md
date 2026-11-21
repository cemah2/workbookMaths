# Erreurs de calcul fréquentes · parties II, III et IV

*Une partie de [Erreurs de calcul fréquentes](erreurs_frequentes.md) : l'index donne les autres.*

## Vecteurs et géométrie de ℝⁿ (M07)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier la racine d'une distance euclidienne | `np.sum((a - b) ** 2)` pris pour $\lVert \mathbf{a} - \mathbf{b} \rVert$ | c'est son **carré** : `np.sqrt(np.sum((a - b) ** 2))` ; le carré suffit pour comparer des distances, pas pour les additionner |
| Diviser par une seule norme dans un cosinus | `(u @ v) / np.sqrt(u @ u)` | diviser par les **deux** normes : $\frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert\thinspace\lVert \mathbf{v} \rVert}$ |
| Projeter avec $\lVert \mathbf{u} \rVert$ au lieu de $\lVert \mathbf{u} \rVert^2$ | $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert}\thinspace\mathbf{u}$ avec $\mathbf{u}$ non unitaire | $\frac{\mathbf{x} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\thinspace\mathbf{u}$ ; $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert}$ est la **composante** (une longueur), $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert^2}$ le **coefficient** |
| Croire qu'un cosinus de 1 veut dire des vecteurs égaux | $\mathbf{u}$ et $2\mathbf{u}$ « identiques » car de cosinus 1 | même direction, longueurs différentes : à la distance $\lVert \mathbf{u} \rVert$ |
| Prendre le score pour la distance à l'hyperplan | la distance de $\mathbf{x}$ à $\mathbf{w} \cdot \mathbf{x} + b = 0$ vaut « $\lvert \mathbf{w} \cdot \mathbf{x} + b \rvert$ » | diviser par $\lVert \mathbf{w} \rVert$ ; sinon multiplier $\mathbf{w}$ et $b$ par 10 changerait la distance |
| Croire que $(-\mathbf{w}, -b)$ garde le même côté positif | « même hyperplan, donc mêmes côtés » | même hyperplan, mais les côtés sont échangés |
| Additionner des distances au lieu de leurs carrés pour l'inertie | $\sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert$ | l'inertie est $\sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2$ ; c'est elle que minimise le barycentre |
| Oublier le facteur $m$ dans König-Huygens | $\sum \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2 + \lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$ | $+\thinspace m\thinspace\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$ (ou $\Omega$ avec des poids) : chaque point compte |
| Compter le point lui-même dans $a(i)$ | $a(i)$ divisé par la taille du cluster, avec une distance nulle | la moyenne sur les **autres** points du cluster |
| Comparer des distances avec des features d'unités différentes | puissance en chevaux et masse en tonnes dans la même distance | standardiser chaque feature (avec les statistiques du jeu d'entraînement) avant de calculer des distances |
| Coder des catégories par des entiers | vélo 1, bus 2, métro 3, marche 4 | un vecteur one-hot : sinon on invente un ordre et des distances entre catégories |
| Oublier `axis` ou `keepdims` | `X / np.sqrt(np.sum(X ** 2, axis=1))` | `keepdims=True` (forme `(n, 1)`) pour diviser chaque **ligne** ; sans lui, NumPy divise les colonnes quand `X` est carré |
| Croire que l'intuition de la dimension 2 vaut en dimension 1 000 | « deux vecteurs au hasard font un angle quelconque » | en grande dimension, ils sont presque orthogonaux, et toutes les distances se ressemblent |

## Tests statistiques (M08)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Lire la p-valeur comme la probabilité que $H_0$ soit vraie | « $p = 0{,}03$ : 3 % de chances que le changement soit inutile » | elle se calcule **en supposant** $H_0$ vraie : la probabilité d'un écart au moins aussi grand, si rien ne changeait |
| Conclure à l'absence d'effet après un test non significatif | « $p = 0{,}4$, donc la mise à jour ne change rien » | « pas d'effet détecté » ; regarder la puissance et l'intervalle de confiance, qui peut contenir de grands effets |
| Confondre significatif et important | « $p = 10^{-6}$, donc un gain énorme » | une p-valeur mélange la taille de l'effet et la quantité de données : donner l'effet et son intervalle |
| Choisir le sens du test après avoir vu les données | un test unilatéral dans le sens observé, sans l'avoir prévu | fixer $H_1$ avant ; sinon le risque de type I réel est le double du seuil annoncé |
| Doubler une p-valeur binomiale unilatérale pour une loi dissymétrique | $2P(K \ge 5)$ pour $p_0 = 0{,}1$ | additionner les issues au plus aussi probables que l'observation, des deux côtés |
| Annoncer une p-valeur nulle après un test par permutation | « aucune des 999 permutations n'atteint l'écart : $p = 0$ » | $\frac{C + 1}{B + 1}$ : la répartition observée compte ; $p \ge \frac{1}{B + 1}$ |
| Rebattre des mesures appariées comme deux groupes | mélanger les serveurs « avant » et « après » | échanger les deux mesures **dans** chaque paire (changer le signe des différences) |
| Traiter des mesures appariées comme indépendantes | l'erreur type $\sqrt{s_a^2/n + s_b^2/n}$ pour des mesures avant et après | travailler sur les différences : $\frac{s_d}{\sqrt{n}}$, bien plus petite |
| Prendre 1,96 avec peu de mesures | $\bar{d} \pm 1{,}96\thinspace\frac{s_d}{\sqrt{5}}$ | le quantile de Student à $n - 1$ degrés de liberté (2,776 pour 5 mesures) |
| Utiliser l'intervalle de Wald avec peu de succès | $[0, 0]$ après 0 succès sur 10, ou une borne négative | l'intervalle de Wilson, toujours dans $[0, 1]$ |
| Diviser les p-valeurs par $m$ au lieu de les multiplier | p-valeur ajustée $\frac{p}{m}$ | $\min(1, m\thinspace p)$ ; ou garder $p$ et comparer au seuil $\frac{\alpha}{m}$ |
| Prendre pour $m$ le nombre de résultats montrés | Bonferroni avec les 3 plus petites p-valeurs sur 50 tests faits | $m$ = le nombre de tests **faits** |
| Arrondir au-dessous une taille d'échantillon | $n = 68{,}7$ arrondi à 68 | arrondir au-dessus : avec moins de mesures, la puissance n'est pas atteinte |
| Préférer le plus grand AIC, ou prendre $\log_{10}$ dans le BIC | « AIC = 464,8 contre 461,8 : le premier gagne » | le plus **petit** critère gagne ; $\ln$ népérien |
| Ne publier que le test le plus significatif | 25 indicateurs testés, seul celui de p-valeur 0,02 est publié | compter les 25 tests (Bonferroni), ou confirmer sur de nouvelles données |

## Matrices (M09a et suite)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Croire que le produit est commutatif | $\mathbf{AB} = \mathbf{BA}$ | en général $\mathbf{AB} \ne \mathbf{BA}$ : l'ordre compte |
| Transposer un produit sans inverser l'ordre | $(\mathbf{AB})^\top = \mathbf{A}^\top\mathbf{B}^\top$ | $(\mathbf{AB})^\top = \mathbf{B}^\top\mathbf{A}^\top$ |
| Multiplier des matrices de formes incompatibles | $(2 \times 3)$ fois $(2 \times 3)$ | le nombre de colonnes de la première doit égaler le nombre de lignes de la seconde |
| Lire $a_{ij}$ colonne d'abord | $a_{32}$ lu à la ligne 2, colonne 3 | la ligne d'abord, puis la colonne ; en Python, `A[i - 1, j - 1]` |
| Écrire `*` pour un produit matriciel | `X * W` pour une couche dense | `X @ W` ; `*` multiplie élément par élément, et le broadcasting peut cacher l'erreur |
| Ajouter le biais d'une couche à une seule ligne, ou dans le mauvais sens | $b_1$ ajouté à l'exemple 1 et $b_2$ à l'exemple 2 | $b_j$ s'ajoute à la colonne $j$ (le neurone $j$), sur chaque ligne |
| Calculer $\mathbf{X}\mathbf{X}^\top$ au lieu de $\mathbf{X}^\top\mathbf{X}$ | `X @ X.T` pour la matrice des features | `X.T @ X`, de forme $(p, p)$ ; `X @ X.T` est $(n, n)$, une case par paire d'exemples |
| Choisir les parenthèses au hasard dans un produit de trois matrices | $\mathbf{A}(\mathbf{B}\mathbf{C})$ avec $\mathbf{B}\mathbf{C}$ énorme | compter $n\thinspace p\thinspace m$ pour chaque ordre ; devant un vecteur, multiplier de droite à gauche |
| Simplifier $\mathbf{A}\mathbf{B} = \mathbf{A}\mathbf{C}$ en $\mathbf{B} = \mathbf{C}$ | $\mathbf{A}$ singulière, $\mathbf{B} \ne \mathbf{C}$ | on ne simplifie que par une matrice inversible : multiplier à gauche par $\mathbf{A}^{-1}$ |
| Inverser un produit ou une somme terme à terme | $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{A}^{-1}\mathbf{B}^{-1}$, $(\mathbf{A} + \mathbf{B})^{-1} = \mathbf{A}^{-1} + \mathbf{B}^{-1}$ | $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$ ; pas de règle pour une somme |
| Oublier le second membre dans une opération sur les lignes | $L_2 - 2L_1$ appliqué aux seuls coefficients | travailler sur la matrice augmentée : chaque opération porte sur toute la ligne |
| Faire deux opérations en même temps, ou multiplier une ligne par 0 | $L_1 \leftarrow L_1 - L_2$ et $L_2 \leftarrow L_2 - L_1$ d'un coup | une opération à la fois, avec une **autre** ligne, et un facteur non nul |
| S'arrêter à la forme échelonnée quand on veut la réduite | un nombre non nul au-dessus d'un pivot | annuler aussi au-dessus de chaque pivot, et diviser chaque ligne par son pivot |
| Garder un pivot minuscule | éliminer avec $\varepsilon = 10^{-18}$ comme pivot | le pivot partiel : la plus grande valeur absolue de la colonne |
| Lire une ligne nulle comme « pas de solution » | $(0 \mkern5mu \mkern5mu  0 \mkern5mu \mkern5mu  0 \mid 0)$ : « impossible » | $0 = 0$ est toujours vrai : une équation de moins ; seule $(0 \cdots 0 \mid c)$ avec $c \ne 0$ est impossible |
| Compter les lignes non nulles pour le rang avant l'élimination | rang 3 pour trois lignes dont l'une est la somme des deux autres | échelonner d'abord, puis compter les pivots |
| Résoudre un système par l'inverse | `np.linalg.inv(A) @ b` | `np.linalg.solve(A, b)` : moins de calculs et moins d'arrondis |

## Moindres carrés et régularisation (M09b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Calculer un $R^2$ sans centrer | $1 - \frac{\sum r_i^2}{\sum y_i^2}$ | $1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$, avec $\mathrm{SCT} = \sum (y_i - \bar{y})^2$ |
| Comparer une MSE à une MAE | « MSE 25, MAE 4 : la MAE est meilleure » | la MSE est dans l'unité au carré : comparer la RMSE (5) et la MAE |
| Croire que $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$ pour toute droite | la décomposition appliquée à une droite tracée à la main | elle ne vaut que pour les moindres carrés avec une colonne de 1 |
| Prendre $2\mathbf{A}\mathbf{w}$ pour le gradient de $\mathbf{w}^\top\mathbf{A}\mathbf{w}$ | $\mathbf{A}$ non symétrique | $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ |
| Oublier le signe moins du gradient des moindres carrés | $\nabla\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 = 2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ | $-2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ : un pas de descente ajoute $2\eta\mathbf{X}^\top\mathbf{r}$ |
| Inverser $\mathbf{X}^\top\mathbf{X}$ pour résoudre | `np.linalg.inv(X.T @ X) @ X.T @ y` | `np.linalg.solve(X.T @ X, X.T @ y)`, ou `np.linalg.lstsq(X, y)` |
| Oublier la colonne de 1 | une droite forcée à passer par l'origine | ajouter une colonne de 1 (ou centrer $\mathbf{X}$ et $\mathbf{y}$) |
| Croire qu'un modèle polynomial n'est pas linéaire | « $w_0 + w_1x + w_2x^2$ ne se résout pas par les équations normales » | il est linéaire en $\mathbf{w}$ : les colonnes $1, x, x^2$, mêmes équations |
| Combiner des puissances non standardisées | $x$ entre 0 et 20, colonnes $x, \ldots, x^6$ | ramener $x$ à $[-1, 1]$, ou standardiser : sinon $\mathbf{X}^\top\mathbf{X}$ est presque singulière |
| Appliquer ridge sans standardiser | une distance en mètres à côté d'une feature sans unité | standardiser les colonnes : la pénalité dépend de l'unité |
| Pénaliser l'ordonnée à l'origine sans le vouloir | ridge sur $\mathbf{X}$ avec sa colonne de 1 | centrer, résoudre sans colonne de 1, puis $b = \bar{y} - \bar{\mathbf{x}} \cdot \mathbf{w}$ |
| Écrire $\lambda = \frac{\sigma}{\tau}$ ou $\frac{\tau^2}{\sigma^2}$ | un prior large qui renforce la pénalité | $\lambda = \frac{\sigma^2}{\tau^2}$ : des variances, bruit au numérateur |
| Prendre $\frac{\mathrm{SCR}}{n}$ pour un estimateur sans biais de $\sigma^2$ | « $\hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$ est sans biais » | il sous-estime ; $\frac{\mathrm{SCR}}{n - p}$ est sans biais |
| Juger un modèle à son $R^2$ d'entraînement | ajouter des features de bruit, et voir le $R^2$ monter | le $R^2$ d'entraînement ne baisse jamais : mesurer sur des données de validation |
| Oublier le signe dans le seuillage doux | $S(-1{,}4 ;\ 0{,}3) = -1{,}7$ | rapprocher de 0 : $\operatorname{signe}(z)\max(\lvert z \rvert - \gamma, 0) = -1{,}1$ |

## Séparabilité linéaire et convexité (M10)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Croire qu'une réunion de convexes est convexe | « deux disques convexes, donc leur réunion aussi » | seule l'intersection garde la convexité : un segment entre les deux disques sort de la réunion |
| Prendre la courbe d'une fonction convexe pour un ensemble convexe | « la parabole $y = x^2$ est convexe » | c'est la région au-dessus d'elle (l'épigraphe) qui est un ensemble convexe |
| Garder un point au milieu d'un côté comme sommet | chaîne monotone avec le test $< 0$ | retirer le dernier sommet quand le produit vectoriel est $\le 0$ |
| Inverser le produit vectoriel | $u_2v_1 - u_1v_2$ | $u_1v_2 - u_2v_1$ : positif quand on tourne à gauche ; sinon l'enveloppe sort dans le sens des aiguilles d'une montre |
| Conclure « non séparable » sur des droites dessinées | « aucune des dix droites tracées ne marche » | il en reste une infinité : écrire un témoin, un point dont on montre (poids positifs, de somme 1) qu'il est dans les deux enveloppes, ou lancer le programme linéaire |
| Tester la séparabilité avec $\ge 0$ | le programme linéaire $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 0$ | exiger $\ge 1$ : avec $\ge 0$, $\mathbf{w} = \mathbf{0}$ et $b = 0$ conviennent toujours |
| Laisser les bornes par défaut de `linprog` | des inconnues forcées à être positives | `bounds=(None, None)` : les poids et le biais sont libres |
| Chercher un séparateur sans terme constant | $\mathbf{w} \cdot \mathbf{x} > 0$ sur une classe, $< 0$ sur l'autre | seuls les hyperplans par l'origine sont alors essayés : ajouter la coordonnée constante 1, en tête (astuce du biais) |
| Prendre la marge fonctionnelle pour une distance | marge $\min_i y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ | diviser par $\lVert \mathbf{w} \rVert$ ; doubler $(\mathbf{w}, b)$ ne doit rien changer |
| Une marge en valeur absolue | $\min_i \frac{\lvert \mathbf{w} \cdot \mathbf{x}_i + b \rvert}{\lVert \mathbf{w} \rVert}$ | multiplier par le label $y_i$ : la marge est négative quand un point est du mauvais côté |
| Confondre la borne triangulaire et la borne pas à pas | $\lVert \mathbf{v}_k \rVert \le \sqrt{\lVert \mathbf{v}_0 \rVert^2 + kL^2}$ pour des pas quelconques | sans condition, seulement $\lVert \mathbf{v}_0 \rVert + kL$ ; la borne en $\sqrt{k}$ demande $\mathbf{v}_k \cdot \mathbf{d}_k \le 0$ à chaque pas |
| Croire qu'une activation change la frontière | « avec une sigmoïde, la frontière se courbe » | une activation croissante garde l'hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ |

## Logique, induction et inégalités de concentration (M11)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Juger un argument sur la vérité de sa conclusion | « si $f$ est continue en 0, elle est dérivable en 0 ; $\lvert x \rvert$ est continue en 0 ; donc $\lvert x \rvert$ est dérivable en 0 » déclaré non valide | il est valide (*modus ponens*) mais pas solide : c'est la première prémisse qui est fausse ($\lvert x \rvert$ fait un coin en 0) |
| Affirmer le conséquent | « si la batterie est vide, l'ordinateur ne démarre pas ; il ne démarre pas ; donc la batterie est vide » | non valide : la ligne « $P$ faux, $Q$ vrai » (une autre cause) le réfute |
| Prouver une phrase en « pour tout » par des exemples | « $n^2 + n + 41$ est premier pour $n = 0$ à 39, donc pour tout $n$ » | $n = 40$ donne $41^2$ : il faut un raisonnement pour tout $n$, et un contre-exemple suffit à réfuter |
| Enchaîner deux phrases en « au moins un » | « $4 \in A \cap B$ et $10 \in B \cap C$, donc $A \cap C \ne \varnothing$ » | les témoins peuvent différer ; seules les inclusions se transmettent ($A \subset B \subset C$) |
| Lire $P(\text{signal} \mid \text{cas})$ comme $P(\text{cas} \mid \text{signal})$ | « le détecteur repère 95 % des plagiats, donc une copie signalée est plagiée à 95 % » | Bayes, avec le taux de base (2 %) : environ 0,39 |
| Croire qu'un grand échantillon efface un biais de sélection | 10 000 notes d'examen saisies par les inscrits eux-mêmes, ceux qui ont 8 les saisissant quatre fois plus que ceux qui ont 4 | la moyenne des notes saisies tend vers 7,2 au lieu de 6 : changer la façon de recueillir les notes (un tirage au hasard des inscrits, des relances) |
| Conclure « probabilité nulle » après zéro événement | « aucune panne en 150 essais, donc le taux de panne est nul » | règle de trois : seulement $p < 2$ % environ, à 95 % |
| Appliquer Markov à une variable qui peut être négative | $X = \pm 10$ avec $\mathbb{E}[X] = 0$ : « $P(X \ge 5) \le 0$ » | se ramener à une variable positive : $\lvert X \rvert$, $(X - \mu)^2$ ou $X - m$ si $X \ge m$ |
| Tchebychev avec $t$ au lieu de $t^2$ | « $P(\lvert N - 40 \rvert \ge 160) \le \frac{100}{160}$ » | $\frac{\sigma^2}{t^2} = \frac{100}{160^2} \approx 0{,}0039$ ; contrôle : diviser $t$ par 2 multiplie $n$ par 4 |
| Appliquer Hoeffding sans bornes connues, ou sans indépendance | un revenu par client sans plafond, des mesures successives d'une série temporelle | vérifier un intervalle $[a, b]$ fixé à l'avance et des tirages indépendants ; sinon, Tchebychev (avec une variance) ou rien |
| Un rayon sans racine carrée, ou sans le facteur 2 du bilatéral | $n = 500$, $\delta = 0{,}05$ : « $r = \frac{\ln 40}{1\thinspace000} \approx 0{,}0037$ » | $r = \sqrt{\frac{\ln 40}{1\thinspace000}} \approx 0{,}061$ ; pour un seul côté, $\ln(1/\delta)$ |
| Le rayon du meilleur de $K$ modèles calculé comme pour un seul | le meilleur de 20 modèles évalués sur le même jeu de test, rayon au risque 5 % | chaque rayon au risque $\frac{\delta}{K}$ (borne de l'union) |
| Croire qu'une partie chanceuse a un regret négatif | « on a gagné plus que la meilleure moyenne fois $T$, donc $R_T < 0$ » | $R_T = \sum_k \Delta_k\thinspace\mathbb{E}[N_k(T)] \ge 0$ : une espérance qui compare des moyennes, pas les récompenses tirées |
| Croire qu'un ε fixé finit par ne plus coûter | « ε-greedy trouve la meilleure option, donc son regret se stabilise » | chaque option reste choisie avec la probabilité $\frac{\varepsilon}{K}$ : regret au moins linéaire ; faire décroître $\varepsilon$ |

## Espaces vectoriels et applications linéaires (M12a)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre pour un sous-espace un ensemble qui ne contient pas $\mathbf{0}$ | « le plan $x + y - z = 2$ est un sous-espace de $\mathbb{R}^3$ » | tester d'abord $\mathbf{0}$ : c'est un sous-espace **affine**, un sous-espace déplacé |
| Vérifier seulement la stabilité par addition | « le demi-plan $x \ge 0$ est stable par somme, donc c'est un sous-espace » | tester aussi la multiplication, par $-1$ en particulier |
| Conclure « libre » parce qu'aucun vecteur n'est multiple d'un autre | $(1, 2, 0)$, $(0, 1, 3)$, $(1, 3, 3)$ « deux à deux non colinéaires, donc libres » | calculer le rang : le troisième est la somme des deux premiers |
| Ranger une base en lignes pour calculer des coordonnées | résoudre $\mathbf{B}^\top\mathbf{c} = \mathbf{v}$ | les vecteurs de base dans les **colonnes** : $\mathbf{B}\mathbf{c} = \mathbf{v}$, puis vérifier $c_1\mathbf{b}_1 + \cdots = \mathbf{v}$ |
| Oublier le terme constant dans une dimension | « les polynômes de degré au plus 3 forment un espace de dimension 3 » | $1, x, x^2, x^3$ : dimension 4 |
| Prendre la borne du rang d'un produit pour sa valeur | « $\operatorname{rg}(\mathbf{A}) = 2$, $\operatorname{rg}(\mathbf{B}) = 3$, donc $\operatorname{rg}(\mathbf{A}\mathbf{B}) = 2$ » | ce n'est qu'un maximum : le produit perd les directions de $\operatorname{Im}\mathbf{B}$ qui tombent dans $\ker\mathbf{A}$ |
| Ranger $f(\mathbf{e}_j)$ dans la ligne $j$ | la matrice de $(x, y) \mapsto (x + y, x - y, 2x)$ écrite de forme $(2, 3)$ | $f(\mathbf{e}_j)$ est la **colonne** $j$ ; la forme est (arrivée, départ) |
| Écrire la matrice de « $f$, puis $g$ » dans l'ordre de lecture | $\mathbf{A}\mathbf{B}$ pour « appliquer $\mathbf{A}$, puis $\mathbf{B}$ » | $\mathbf{B}\mathbf{A}$ : la dernière appliquée est à gauche, la plus proche de $\mathbf{x}$ à droite |
| Chercher le noyau dans l'espace d'arrivée | pour $\mathbf{A}$ de forme $(2, 4)$, un vecteur du noyau à 2 coordonnées | le noyau vit au départ : 4 coordonnées ; l'image, à l'arrivée |
| Prendre la base de l'image dans la forme réduite | $(1, 0, 0)$ et $(0, 1, 0)$ comme base de l'image | les colonnes **de $\mathbf{A}$** dont l'indice porte un pivot |
| Oublier le signe moins dans un vecteur du noyau | $x_p = R_{ij}$ | $x_p = -R_{ij}$ ; vérifier toujours $\mathbf{A}\mathbf{x} = \mathbf{0}$ |
| Conclure « une infinité de solutions » dès qu'il y a une variable libre | $\mathbf{A}$ de rang 2 à 4 colonnes, $\mathbf{b}$ quelconque | vérifier d'abord que $\mathbf{b} \in \operatorname{Im}\mathbf{A}$ ; sinon, aucune solution |
| Écrire $\mathbf{S}\mathbf{A}\mathbf{S}^{-1}$ pour la matrice dans la base $\mathbf{S}$ | `S @ A @ np.linalg.inv(S)` | $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$, `np.linalg.solve(S, A @ S)` ; vérifier sur $\mathbf{A}'\mathbf{e}_1$ |
| Inverser une application affine en oubliant que la translation est transformée | $\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}\mathbf{y} - \mathbf{b}$ | $\mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$ : retirer $\mathbf{b}$ d'abord ; vérifier $\varphi^{-1}(\mathbf{b}) = \mathbf{0}$ |
| Croire qu'un rang calculé en flottants est exact | « `matrix_rank` dit 3, donc aucune colonne n'est redondante » | dire la tolérance ; une relation vraie à $10^{-12}$ près est redondante pour des mesures ; mettre les colonnes à la même échelle |

## Orthogonalité et projections (M12b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre une matrice symétrique à coefficients positifs pour un produit scalaire | « $`\begin{pmatrix} 2 & 3 \cr 3 & 4 \end{pmatrix}`$ définit un produit scalaire » | vérifier $a > 0$ et $ac - b^2 > 0$ ; ici $ac - b^2 = -1$, et $(3, -2)$ donne $-2$ |
| Dire « orthogonaux » sans préciser le produit scalaire | « $(1, -1)$ et $(0, 1)$ ne sont jamais orthogonaux » | pour $`\mathbf{M} = \begin{pmatrix} 3 & 1 \cr 1 & 1 \end{pmatrix}`$, ils le sont ; l'orthogonalité dépend du produit scalaire |
| Appeler orthogonale une matrice à colonnes seulement orthogonales | $`\begin{pmatrix} 2 & 0 \cr 0 & 1/2 \end{pmatrix}`$ « orthogonale, donc son inverse est sa transposée » | il faut des colonnes **orthonormées** : $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$ |
| Lire des coordonnées par produits scalaires dans une base non orthonormée | $c_4 = \mathbf{x} \cdot (2\mathbf{u}_4)$ | diviser par $\lVert 2\mathbf{u}_4 \rVert^2$, ou résoudre le système |
| Oublier de normer dans Gram-Schmidt | $\mathbf{q}_2 = \mathbf{a}_2 - (\mathbf{a}_2 \cdot \mathbf{q}_1)\thinspace\mathbf{q}_1$ | diviser $\mathbf{v}_2$ par sa norme, puis vérifier $\lVert \mathbf{q}_2 \rVert = 1$ |
| Projeter sur les $\mathbf{a}_j$ au lieu des $\mathbf{q}_j$ | $\mathbf{v}_2 = \mathbf{a}_2 - (\mathbf{a}_2 \cdot \mathbf{q}_1)\thinspace\mathbf{a}_1$ | retirer la projection sur le vecteur **unitaire** $\mathbf{q}_1$ |
| Confondre $U^\perp$ et le complémentaire de $U$ | « $U^\perp$ contient tous les vecteurs hors du plan » | $U^\perp$ est un sous-espace (un noyau), de dimension $n - \dim U$ |
| Former la projection avec une base non orthonormée | `P = A @ A.T` | `Q = gram_schmidt(A)` puis `Q @ Q.T`, ou $\mathbf{A}(\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top$ |
| Prendre $\lVert \mathbf{p} \rVert$ pour la distance à $U$ | la distance de $\mathbf{v}$ au plan égale à la longueur du projeté | $\lVert \mathbf{v} - \mathbf{p} \rVert$, la norme du résidu |
| Conclure « projection orthogonale » de la seule idempotence | $`\begin{pmatrix} 1 & 1 \cr 0 & 0 \end{pmatrix}`$ « vérifie $\mathbf{M}^2 = \mathbf{M}$, donc projette orthogonalement » | vérifier aussi $\mathbf{M}^\top = \mathbf{M}$ ; sinon, c'est une projection oblique |
| Voir les résidus des moindres carrés perpendiculaires à la droite | dessiner les écarts à angle droit de la droite ajustée | ils sont verticaux ; l'angle droit est dans $\mathbb{R}^n$, entre $\mathbf{y} - \hat{\mathbf{y}}$ et les colonnes de $\mathbf{X}$ |
| Résoudre $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$ depuis la première ligne | `for i in range(p): w[i] = (z[i] - R[i, :i] @ w[:i]) / R[i, i]` | $\mathbf{R}$ est triangulaire supérieure : remonter depuis la dernière ligne |
| Comparer directement sa QR à celle de NumPy | « `np.linalg.qr` donne $r_{11} < 0$, ma fonction est fausse » | QR est unique au signe près : comparer après $\mathbf{D} = \operatorname{diag}(\operatorname{signe}(r_{kk}))$ |
| Faire confiance à Gram-Schmidt classique sur des colonnes presque dépendantes | des features polynomiales de degré 10 : $\mathbf{Q}^\top\mathbf{Q}$ « vaut $\mathbf{I}$ » | mesurer $\max \lvert \mathbf{Q}^\top\mathbf{Q} - \mathbf{I} \rvert$ ; procédé modifié, ou orthogonaliser deux fois |
| Croire qu'une orthogonalité de fonctions ne dépend pas de l'intervalle | « $x$ et $x^2$ sont orthogonales » | vrai sur $[-1 ; 1]$, faux sur $[0 ; 1]$ ($\int_0^1 x^3\thinspace dx = \frac{1}{4}$) |

## Valeurs propres et matrices symétriques (M12c)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Croire le déterminant additif | « $\det(\mathbf{A} + \mathbf{B}) = \det\mathbf{A} + \det\mathbf{B}$ » | il est multiplicatif, pas additif : calculer $\det(\mathbf{A} + \mathbf{B})$ ; et $\det(c\mathbf{A}) = c^n\det\mathbf{A}$ |
| Oublier le signe des échanges de lignes | un déterminant calculé par élimination avec un échange, sans changer le signe | compter les échanges : $(-1)^{\text{échanges}} \times$ le produit des pivots |
| Lire un petit déterminant comme « presque singulière » | « $\det = 10^{-9}$, la matrice est presque non inversible » | $\det(0{,}1\thinspace\mathbf{I}_9) = 10^{-9}$ : regarder le conditionnement (M12d) |
| Lire les valeurs propres sur la diagonale d'une matrice non triangulaire | $`\begin{pmatrix} 5 & 2 \cr 1 & 4 \end{pmatrix}`$ « a pour valeurs propres 5 et 4 » | résoudre $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ (ici 6 et 3) ; la diagonale suffit seulement pour une matrice triangulaire |
| Prendre la trace d'un produit pour le produit des traces | « $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}\mathbf{A}\thinspace\operatorname{tr}\mathbf{B}$ » | seule $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$ est vraie |
| Accepter un vecteur propre nul | `np.linalg.solve(A - lam * np.eye(n), np.zeros(n))` rend le vecteur nul | un vecteur propre est non nul : prendre un vecteur du noyau de $\mathbf{A} - \lambda\mathbf{I}$ (à la main, ou `np.linalg.eig`) |
| Conclure « diagonalisable » d'une valeur propre double, ou l'inverse | « $`\begin{pmatrix} 5 & 1 \cr 0 & 5 \end{pmatrix}`$ a la valeur propre 5, donc $\mathbf{P} = \mathbf{I}$ convient » ; « une valeur propre double empêche la diagonalisation » | comparer la dimension de l'espace propre à la multiplicité : ici 1 contre 2, défective ; $\mathbf{I}$, elle, est diagonale |
| Calculer $\mathbf{A}^k$ terme à terme | « $\mathbf{A}^{10}$ = la matrice des puissances dixièmes des éléments » | $\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$ ; seule une matrice diagonale se met à la puissance élément par élément |
| Oublier la convention de signe de la méthode de la puissance | avec $\lambda_1 < 0$, $\mathbf{x}_k$ change de signe à chaque pas et l'arrêt n'arrive jamais | fixer le signe (la coordonnée de plus grande valeur absolue positive) avant de comparer deux itérés |
| Rendre $\lVert \mathbf{A}\mathbf{x} \rVert$ comme valeur propre | `value = np.linalg.norm(A @ x)` : toujours positive | le quotient de Rayleigh $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ pour $\mathbf{x}$ unitaire, qui garde le signe |
| Croire « valeurs propres réelles » équivalent à « symétrique » | « $`\begin{pmatrix} 2 & 1 \cr 0 & 4 \end{pmatrix}`$ a des valeurs propres réelles, donc ses vecteurs propres sont orthogonaux » | le théorème spectral demande la symétrie ; ici $(1, 0)$ et $(1, 2)$ ne sont pas orthogonaux |
| Juger « définie positive » sur la diagonale ou sur le signe des éléments | « $`\begin{pmatrix} 4 & 6 \cr 6 & 7 \end{pmatrix}`$ est définie positive » | les mineurs principaux : $28 - 36 < 0$, indéfinie |
| Prendre le plus grand élément pour le maximum de $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ sur la sphère | « le maximum de $\mathbf{x}^\top\mathbf{A}\mathbf{x}$, $\lVert \mathbf{x} \rVert = 1$, est $\max a_{ij}$ » | c'est $\lambda_{\max}$, atteint au vecteur propre ; un élément diagonal n'est qu'un quotient de Rayleigh parmi d'autres |
| Allonger l'ellipse le long de la grande valeur propre | « $\mathbf{x}^\top\mathbf{A}\mathbf{x} = c$ est la plus allongée selon $\mathbf{q}_{\max}$ » | les demi-axes valent $\sqrt{c/\lambda_i}$ : la plus allongée selon le vecteur propre de la **plus petite** valeur propre |
| Rendre $\mathbf{L}^\top$ au lieu de $\mathbf{L}$ | un facteur de Cholesky triangulaire supérieur | $\mathbf{L}$ est triangulaire **inférieure**, $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$ |
| Faire confiance à `np.linalg.cholesky` sur une matrice non symétrique | `np.linalg.cholesky([[9, 3], [-6, 5]])` rend un facteur, sans erreur | elle ne lit que le triangle inférieur : vérifier la symétrie avant |
| Prendre la racine carrée d'une matrice élément par élément | `np.sqrt(Sigma)` comme $\boldsymbol{\Sigma}^{1/2}$ | $\mathbf{Q}\thinspace\operatorname{diag}(\sqrt{\lambda_i})\thinspace\mathbf{Q}^\top$ (`eigh`), ou `scipy.linalg.sqrtm` |
| Oublier les covariances dans la variance d'une somme | « $\mathbb{V}(x_1 + x_2) = \mathbb{V}(x_1) + \mathbb{V}(x_2)$ » pour des features corrélées | $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ : ajouter $2\operatorname{Cov}(x_1, x_2)$ |
| Blanchir sans regarder les petites valeurs propres | $\lambda_i = 10^{-4}$ : la coordonnée sur cet axe est multipliée par 100, et le bruit de mesure pèse autant que le reste | regarder le spectre avant de blanchir ; une valeur propre minuscule signale du bruit ou des features presque identiques |
| Confondre les blanchiments | $\mathbf{W} = \mathbf{L}$, ou $\mathbf{L}^{-\top}$, ou $\boldsymbol{\Sigma}^{1/2}$ | vérifier $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ : $\mathbf{L}^{-1}$, $\boldsymbol{\Sigma}^{-1/2}$ ou $\boldsymbol{\Lambda}^{-1/2}\mathbf{Q}^\top$ |

## SVD et analyse en composantes principales (M12d)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre les valeurs propres de $\mathbf{A}$ pour ses valeurs singulières | « $`\begin{pmatrix} 0 & 2 \cr -2 & 0 \end{pmatrix}`$ n'a pas de valeur singulière réelle » | les valeurs singulières sont les racines des valeurs propres de $\mathbf{A}^\top\mathbf{A}$, toujours positives : ici 2 et 2 |
| Oublier la racine carrée | « $\mathbf{A}^\top\mathbf{A}$ a pour valeurs propres 25 et 4, donc $s = 25$ et $4$ » | $s_i = \sqrt{\lambda_i}$ : 5 et 2 |
| Ne pas diviser $\mathbf{A}\mathbf{v}_i$ par $s_i$ | $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i$, de norme $s_i$ | $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i/s_i$, unitaire |
| Lire les $\mathbf{v}_i$ en colonnes de `Vt` | `Vt[:, 0]` pris pour $\mathbf{v}_1$ | `np.linalg.svd` rend $\mathbf{V}^\top$ : $\mathbf{v}_1$ est la ligne `Vt[0]` |
| Changer le signe d'un seul vecteur singulier | $\mathbf{v}_1 \to -\mathbf{v}_1$ sans toucher à $\mathbf{u}_1$ | changer $\mathbf{u}_i$ et $\mathbf{v}_i$ ensemble ; fixer une convention avant de comparer deux SVD |
| Calculer l'erreur de rang $k$ avec les $s_i$ | « $\lVert \mathbf{A} - \mathbf{A}_1 \rVert_F = s_2 + s_3$ » | $\sqrt{s_2^2 + s_3^2}$ (Eckart-Young) |
| Mesurer l'énergie d'une image non centrée | « le rang 1 garde 95 % de l'énergie, la compression est excellente » | retirer d'abord le niveau moyen ; regarder aussi l'image |
| Transposer la pseudo-inverse | $\mathbf{A}^+$ de la forme de $\mathbf{A}$ | $\mathbf{A}^+ = \mathbf{V}\mathbf{S}^{-1}\mathbf{U}^\top$ est de forme $(n, m)$ |
| Inverser une valeur singulière minuscule | `1 / s` avec $s = 10^{-12}$ (du bruit) | tronquer sous un seuil relatif (`rcond`) ou régulariser (ridge) |
| Juger le conditionnement par le déterminant | « $\det = 1$, le système est bien posé » | $\kappa = s_{\max}/s_{\min}$ : une matrice de déterminant 1 peut avoir $\kappa = 10^4$ |
| Former $\mathbf{A}^\top\mathbf{A}$ pour une matrice mal conditionnée | les équations normales avec $\kappa = 10^7$ | $\kappa(\mathbf{A}^\top\mathbf{A}) = \kappa^2$ : QR ou SVD sur $\mathbf{A}$ |
| Une ACP sans centrer | les vecteurs propres de $\mathbf{X}^\top\mathbf{X}$ | centrer : sinon le premier axe pointe vers la moyenne |
| Prendre le premier vecteur de `eigh` pour le premier axe | `axes = vectors[:, 0]` | `eigh` range par ordre **croissant** : la dernière colonne, ou retourner l'ordre |
| Lire les axes en lignes | `vectors[order]` pour réordonner les axes | les vecteurs propres sont les **colonnes** : `vectors[:, order]` (et `components_` de scikit-learn les range en lignes) |
| Mélanger $n$ et $n - 1$ | des variances de scores avec `np.var` (en $n$) comparées à une covariance en $n - 1$ | dire la convention, et la garder partout : `np.var(..., ddof=1)`, $\lambda_j = s_j^2/(n - 1)$ |
| Oublier `rowvar=False` | `np.cov(X)` avec les exemples en lignes : une matrice $n \times n$ | `np.cov(X, rowvar=False)` |
| Calculer les parts sur les $k$ premières variances | « avec 2 axes sur 5, les parts sont 70 % et 30 % » | diviser par la somme de **toutes** les variances |
| Standardiser sans y penser, ou ne pas standardiser | des pixels réduits à variance 1 ; des euros et des kilomètres seulement centrés | standardiser si les unités diffèrent ; sinon centrer seulement |
| Juger l'erreur de reconstruction sur l'entraînement | un seuil d'anomalie fixé sur les données qui ont servi aux axes | calculer les axes sur l'entraînement, mesurer et fixer les seuils sur d'autres données |
| Lire des distances sur une carte t-SNE | « ces deux groupes sont deux fois plus éloignés que ceux-là » | la divergence KL ne contraint presque pas l'écart entre deux groupes séparés : une carte montre des voisinages, elle ne mesure pas |

## Vraisemblance et régression logistique (M13a)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Dériver la vraisemblance au lieu de la log-vraisemblance | dériver $p^{12}(1 - p)^{30}$ par la règle du produit | passer au logarithme : $12\ln p + 30\ln(1 - p)$, même maximum |
| Diviser par $n - 1$ le maximum de vraisemblance d'une variance | `np.var(x, ddof=1)` pour $\hat{\sigma}^2$ | $\frac{1}{n}$ pour le maximum de vraisemblance (`np.var(x)`), $\frac{1}{n-1}$ pour l'estimation sans biais |
| Une probabilité 0 pour une valeur jamais vue | $\hat{p}_k = \frac{0}{N}$, puis $\ln 0 = -\infty$ sur une observation nouvelle | lisser : $\frac{n_k + \alpha}{N + K\alpha}$ |
| Lisser le numérateur seulement | $\frac{n_k + 1}{N}$ | $\frac{n_k + 1}{N + K}$ : les probabilités doivent sommer à 1 |
| $-\ln\hat{p}$ pour un label 0 | le terme de $(y, \hat{p}) = (0 ;\ 0{,}3)$ pris égal à $-\ln 0{,}3$ | $-\ln(1 - \hat{p}) = -\ln 0{,}7$ |
| Mélanger nats et bits | une log-loss de `sklearn` comparée à une entropie de M06 | les bibliothèques sont en nats ; diviser par $\ln 2$ pour des bits |
| Calculer $\ln(1 + e^z)$ tel quel | `np.log(1 + np.exp(900))` donne `inf` | $\max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$, avec `np.log1p` |
| Calculer la log-loss à partir de $\sigma(z)$ arrondi | $\sigma(45)$ arrondi à 1, puis $\ln(1 - 1) = -\infty$ | écrire le terme avec le score : $s(z) - yz$ |
| Lire un poids logistique comme un effet sur la probabilité | « $w_j = 0{,}5$ : la probabilité monte de 0,5 » | la log-cote monte de $w_j$, la cote est multipliée par $e^{w_j}$ |
| Confondre indépendance et indépendance conditionnelle | « Naïve Bayes suppose les features indépendantes » | indépendantes **sachant la classe** |
| Oublier les proportions des classes | comparer seulement $p(\mathbf{x} \mid k)$ entre les classes | comparer $\pi_k\thinspace p(\mathbf{x} \mid k)$ (en logarithmes) |
| Moyenner des impuretés sans pondérer | la moyenne simple des entropies de deux groupes de 2 et 98 exemples | pondérer par les tailles des groupes |
| Prendre le taux d'erreur pour l'indice de Gini | « $(0{,}9 ;\ 0{,}05 ;\ 0{,}05)$ a un Gini de 0,1 » | $G = 1 - \sum_k p_k^2 = 0{,}185$ ; $1 - \max_k p_k$ est le taux d'erreur |
| Mélanger $\frac{1}{n}$ et $\frac{1}{n - 1}$ dans la décomposition de la variance | la variance totale en $\frac{1}{n-1}$, celles des groupes en $\frac{1}{n}$ | la même convention partout ($\frac{1}{n}$) pour que total = intra + inter |

## Optimisation sous contraintes et SVM (M13b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre un point de Lagrange pour un minimum | « $\nabla f + \lambda\nabla g = \mathbf{0}$, donc c'est le minimum » | la condition est nécessaire : comparer les candidats, ou invoquer la convexité |
| Oublier de tester le minimum libre | supposer une inégalité active alors que le minimum libre est admissible | regarder d'abord le minimum libre ; s'il est admissible, $\mu = 0$ |
| Accepter un multiplicateur d'inégalité négatif | « $\mu = -\frac43$ : la solution est sur le bord » | $\mu < 0$ dit que la contrainte ne doit pas être active : changer d'ensemble actif |
| Mélanger les conventions de signe | lagrangien $f - \lambda g$ dans un calcul, $f + \lambda g$ dans l'autre | fixer la convention ($g \le 0$, $f + \sum_i \mu_i g_i$, $\mu_i \ge 0$) et s'y tenir |
| Croire que la fonction duale peut dépasser le minimum | « $D(12) = 30 > f^\ast$ » | $D \le f^\ast$ toujours (dualité faible) : une valeur plus grande signale une erreur de calcul |
| Juger la convexité sur l'objectif seul | « $\min x$ sous $x^2 + y^2 = 4$ est convexe : l'objectif est linéaire » | vérifier aussi chaque contrainte : une égalité doit être affine |
| Confondre marge et largeur de la bande | « $\lVert\mathbf{w}\rVert = 0{,}5$ : marge de 4 » | $\rho = \frac{1}{\lVert\mathbf{w}\rVert} = 2$ ; la bande a une largeur $2\rho$ |
| $C$ fois la moyenne des hinges au lieu de la somme | $J = \frac12\lVert\mathbf{w}\rVert^2 + C \cdot \frac1n\sum_i \ell_i$ | $J = \frac12\lVert\mathbf{w}\rVert^2 + C\sum_i \ell_i$, ou la forme moyenne avec $\lambda = \frac{1}{nC}$ |
| Compter dans le sous-gradient les exemples bien au-delà de la marge | soustraire $C y_i\mathbf{x}_i$ pour tous les exemples | seuls les exemples de marge fonctionnelle strictement inférieure à 1 comptent |
| Lire $b$ sur un vecteur de support borné | $b = y_i - \mathbf{w} \cdot \mathbf{x}_i$ avec $\alpha_i = C$ | le lire sur un vecteur libre ($0 < \alpha_i < C$), qui est exactement sur le bord |
| Oublier les labels dans $\mathbf{w}$ | $\mathbf{w} = \sum_i \alpha_i\mathbf{x}_i$ | $\mathbf{w} = \sum_i \alpha_i y_i\mathbf{x}_i$ |
| Oublier le carré dans le noyau RBF | $e^{-\gamma\lVert\mathbf{x} - \mathbf{z}\rVert}$ | $e^{-\gamma\lVert\mathbf{x} - \mathbf{z}\rVert^2}$ (`sklearn` aussi) |
| Oublier les monômes de bas degré du noyau polynomial | « $(1 + \mathbf{x} \cdot \mathbf{z})^2$ en dimension $p$ : $\binom{p + 1}{2}$ coordonnées » | $\binom{p + 2}{2}$ : les monômes de degré **au plus** 2, constante comprise |
| Prendre n'importe quelle fonction de deux points pour un noyau | « $\lVert\mathbf{x} - \mathbf{z}\rVert^2$ compare deux points : c'est un noyau » | un noyau est symétrique et a des matrices de Gram semi-définies positives ; ce n'est pas le cas ici |

## Les maths des ensembles (M14)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre $P(X > k)$ pour $P(X \ge k)$ | « au moins 7 sur 9 » : `binom.sf(7, 9, p)` | `binom.sf(k - 1, n, p)`, car `sf(m)` rend $P(X > m)$ |
| Inverser la divergence de Chernoff | $e^{-n\thinspace\mathrm{KL}(p \Vert a)}$ | $\mathrm{KL}(a \Vert p)$ : la proportion de l'événement d'abord, le paramètre de la loi ensuite |
| Croire qu'une borne pour $a \le p$ dit quelque chose | « Chernoff donne 1, donc l'événement est sûr » | pour $a \le p$, la borne vaut 1 : elle ne dit rien, et l'événement n'est pas rare |
| Oublier les covariances dans la variance d'une moyenne | $\mathbb{V}\big(\sum_i w_iX_i\big) = \sum_i w_i^2\thinspace\mathbb{V}(X_i)$ pour des variables corrélées | $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$, toutes les cases de la matrice |
| Diviser par $M$ des modèles corrélés | « 50 modèles de variance 2 : variance 0,04 » | le terme en $\frac{1}{M}$ ne porte que sur les parts propres ; les covariances laissent un plancher |
| Croire $(1 + x/n)^n \approx e^x$ dès que $n$ est « grand » | $n = 30$ pour $x = 3$ : « à 1 % près » | l'erreur relative vaut environ $-\frac{x^2}{2n}$ : il faut $n$ grand devant $x^2$ |
| Oublier de renormaliser les poids de Hedge | $w_t[k] = e^{-\eta L_t[k]}$ | diviser par la somme ; les poids sont une loi sur les experts |
| Laisser déborder l'exponentielle | `np.exp(-eta * L)` avec $\eta L$ de l'ordre de 1 000 : $\frac{0}{0}$ | retrancher $\min_j L_t[j]$ avant l'exponentielle (log-somme-exp) |
| Se tromper de signe dans les poids exponentiels | $w \propto e^{+\eta L}$ | une grande loss donne un **petit** poids : $e^{-\eta L}$ |
| Utiliser la loss du tour au lieu de la loss cumulée | $w_t[k] \propto e^{-\eta\ell_{t-1}[k]}$ | $L_t[k] = \sum_{s < t}\ell_s[k]$, la somme des tours précédents |
| Confondre le gradient par rapport aux prédictions et aux paramètres | « le gradient de la loss exponentielle a autant de coordonnées que le modèle a de coefficients » | $\nabla_{\mathbf{F}}\mathcal{L}$ a une coordonnée par exemple ; la règle de la chaîne mène aux paramètres |
| Ne pas couper le gradient de Huber | $-(y - F)$ pour un résidu de 2,7 avec $\delta = 0{,}8$ | $-\operatorname{clip}(y - F, -\delta, \delta)$ : au plus $\delta$ en valeur absolue |

## Applications affines, graphes et variance d'un produit (M16)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Ranger $\mathbf{W}$ dans la mauvaise convention | une application de $\mathbb{R}^3$ dans $\mathbb{R}^3$ écrite en colonnes et calculée par `x @ W` : aucune erreur, mais c'est l'application de $\mathbf{W}^\top$ | en lignes, $\mathbf{W}$ a la forme (entrées, sorties) ; vérifier une sortie sur un point connu, comme $(1, 0, \ldots, 0)$ |
| Mélanger les rangements d'une matrice homogène | la translation dans la dernière colonne, puis $[\mathbf{x}, 1]\thinspace\mathbf{H}$ | en lignes, $\mathbf{b}$ sur la dernière **ligne** et $(0, \ldots, 0, 1)$ en dernière colonne ; en colonnes, l'inverse |
| Multiplier les matrices homogènes dans le mauvais ordre | $f_1$ puis $f_2$ en lignes : $\mathbf{H}_2\mathbf{H}_1$ | en lignes, la première appliquée est à gauche : $\mathbf{H}_1\mathbf{H}_2$ (à droite avec des colonnes) |
| Lire $(\mathbf{A}^k)_{ij}$ comme « il existe un chemin » | « $(\mathbf{A}^2)_{14} = 0$, donc 4 est inaccessible depuis 1 » | $(\mathbf{A}^k)_{ij}$ compte les chemins d'exactement $k$ arêtes ; regarder toutes les longueurs |
| Confondre ligne et colonne de la matrice d'adjacence | le degré entrant de $j$ lu sur la ligne $j$ | ligne $i$ : les arêtes qui partent de $i$ ; colonne $j$ : celles qui arrivent en $j$ |
| Calculer $(\mathbf{I} - \mathbf{A})^{-1}$ sur un graphe qui a un cycle | `np.linalg.inv(np.eye(n) - A)` appelé « somme sur les chemins » | vérifier d'abord l'absence de cycle (puissances de $\mathbf{A}$, ou une numérotation triangulaire) |
| Oublier deux termes de la variance d'un produit | $\mathbb{V}(XY) = \mathbb{V}(X)\thinspace\mathbb{V}(Y)$ pour des variables non centrées | $\mathbb{V}(X)\thinspace\mathbb{V}(Y) + \mathbb{V}(X)\thinspace\mathbb{E}[Y]^2 + \mathbb{V}(Y)\thinspace\mathbb{E}[X]^2$, pour des variables **indépendantes** |
| Mettre $\mathbb{V}(x_i)$ à la place de $\mathbb{E}[x_i^2]$ | $\mathbb{V}(\varepsilon x) = \mathbb{V}(x)$ pour $x$ de moyenne 2 | $\mathbb{V}(\varepsilon x) = \mathbb{V}(\varepsilon)\thinspace\mathbb{E}[x^2]$ quand $\varepsilon$ est centré et indépendant de $x$ |
| Croire que décorrélées veut dire indépendantes | « covariance nulle, donc $\mathbb{E}[X^2Y^2] = \mathbb{E}[X^2]\thinspace\mathbb{E}[Y^2]$ » | décorrélées suffit pour additionner des variances, pas pour factoriser n'importe quelle espérance |
| Additionner des écarts-types | 25 termes indépendants d'écart-type 1 : « écart-type 25 » | les variances s'ajoutent : écart-type $\sqrt{25} = 5$ ; 25 seulement si les termes sont égaux |

## Jacobienne et règle de la chaîne (M17)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Transposer la jacobienne | une ligne par **entrée** : $(n, m)$ pour une application de $\mathbb{R}^n$ dans $\mathbb{R}^m$ | une ligne par sortie, une colonne par entrée : $(m, n)$ |
| Prendre $\mathbf{W}$ pour la jacobienne de $\mathbf{x} \mapsto \mathbf{x}\mathbf{W} + \mathbf{b}$ | « la jacobienne d'une application en lignes est $\mathbf{W}$ » | c'est $\mathbf{W}^\top$ : la sortie $k$ est $\sum_jx_jW_{jk}$ |
| Multiplier les jacobiennes dans l'ordre d'application | $\mathbf{J} _{\mathbf{f}}\mathbf{J} _{\mathbf{g}}$ pour $\mathbf{g} \circ \mathbf{f}$ | $\mathbf{J} _{\mathbf{g}}\mathbf{J} _{\mathbf{f}}$ : la dernière appliquée à gauche |
| Évaluer une jacobienne au mauvais point | $\mathbf{J} _{\mathbf{g}}(\mathbf{x})\thinspace\mathbf{J} _{\mathbf{f}}(\mathbf{x})$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))$ : au point intermédiaire ; calculer d'abord tous les points intermédiaires |
| Oublier la transposée du gradient en colonne | $\nabla_{\mathbf{x}}(L \circ \mathbf{f}) = \mathbf{J} _{\mathbf{f}}\nabla _{\mathbf{y}}L$ | $\mathbf{J}  _{\mathbf{f}}^\top\nabla  _{\mathbf{y}}L$ (en colonne) ou $\nabla _{\mathbf{y}}L\thinspace\mathbf{J} _{\mathbf{f}}$ (en ligne) |
| Utiliser le raccourci diagonal sur une application quelconque | $\frac{\mathbf{A}(\mathbf{x} + h\mathbf{1}) - \mathbf{A}(\mathbf{x} - h\mathbf{1})}{2h}$ pris pour la diagonale de $\mathbf{A}$ | il donne $\mathbf{A}\mathbf{1}$ ; il ne vaut que pour une fonction appliquée coordonnée par coordonnée |
| Former la jacobienne pour un produit par un vecteur | `numerical_jacobian(f, x) @ v` pour $n = 10^4$ | `jacobian_vector_product(f, x, v)` : 2 évaluations au lieu de $2n$ |
| Donner une seule dérivée en un point anguleux | « la dérivée de l'impôt en 30 k€ vaut 0,3 » | deux dérivées latérales, 0,2 et 0,4 ; des sous-gradients seulement pour une fonction convexe |
| Évaluer toutes les dérivées d'une longue composition au départ | $\frac{\mathrm{d}x_L}{\mathrm{d}x_0} = \varphi'(x_0)^L$ | $\prod_k\varphi'(x_k)$, le long de la trajectoire |
| Oublier la normalisation d'une loi de Boltzmann | $p_i = e^{-E_i/T}$ | diviser par $Z = \sum_je^{-E_j/T}$ ; seuls les rapports se passent de $Z$ |
| Confondre $\mathbf{p}^\top\mathbf{p}$ et $\mathbf{p}\thinspace\mathbf{p}^\top$ pour une ligne $\mathbf{p}$ | $\operatorname{diag}(\mathbf{p}) - \sum_ip_i^2$ | $\mathbf{p}^\top\mathbf{p}$ est la matrice $K \times K$ des produits $p_ip_j$ |

## Différentiation automatique et calcul matriciel (M18)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier un chemin dans un graphe de calcul | $\frac{\partial y}{\partial t}$ calculé par le seul chemin $t \to u_2 \to u_3 \to y$, quand $t$ sert aussi dans $u_4 = t^2$ | sommer sur **tous** les chemins ; un nœud qui sert deux fois a deux arêtes sortantes |
| Une seule arête pour $t \cdot t$ | dérivée locale $t$ pour $u = t \cdot t$ | $2t$ : une opération qui prend deux fois le même argument a deux arêtes vers lui |
| Mettre la graine sur deux entrées pour une dérivée partielle | $x = 2 + \varepsilon$, $y = -1 + \varepsilon$ pour $\frac{\partial f}{\partial x}$ | une graine par passe ($y = -1$) ; deux graines donnent la dérivée dans la direction $(1, 1)$ |
| Ne garder qu'une contribution à un adjoint | $\bar{t} = \bar{u}_2\thinspace v$, en oubliant $\bar{u}_4 \times 2t$ quand $t$ sert aussi dans $u_4 = t^2$ | sommer les contributions de **tous** les successeurs du nœud |
| Utiliser un adjoint incomplet | calculer $\bar{u}_1$ avant d'avoir $\bar{u}_2$, alors que $u_1 \to u_2$ | visiter les nœuds dans l'ordre inverse du calcul |
| Choisir le mode direct pour un gradient de beaucoup de variables | $n = 10^4$ passes directes pour une fonction réelle | une passe arrière (le gradient bon marché) |
| Rendre la transposée d'un gradient matriciel | $\nabla_{\mathbf{X}}\operatorname{tr}(\mathbf{A}\mathbf{X}) = \mathbf{A}$ ; $\nabla\ln\det\mathbf{X} = \mathbf{X}^{-1}$ | $\mathbf{A}^\top$ et $\mathbf{X}^{-\top}$ : $\mathrm{d}f = \operatorname{tr}(\mathbf{M}\thinspace\mathrm{d}\mathbf{X})$ donne $\mathbf{G} = \mathbf{M}^\top$ |
| Écrire $2\mathbf{A}\mathbf{X}$ pour $\mathbf{A}$ quelconque | $\nabla\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X}) = 2\mathbf{A}\mathbf{X}$ | $(\mathbf{A} + \mathbf{A}^\top)\mathbf{X}$ |
| Changer l'ordre des facteurs dans une différentielle | $\mathrm{d}(\mathbf{X}^2) = 2\mathbf{X}\thinspace\mathrm{d}\mathbf{X}$ | $\mathrm{d}\mathbf{X}\thinspace\mathbf{X} + \mathbf{X}\thinspace\mathrm{d}\mathbf{X}$ : les matrices ne commutent pas |
| Vérifier un gradient avec une direction symétrique | $\mathbf{H} = \mathbf{I}$ ou la matrice pleine de 1 : un gradient transposé passe | une direction tirée au hasard, non symétrique, et plusieurs |
| Vérifier avec un pas trop petit | $h = 10^{-13}$ : les arrondis divisés par $2h$ font croire à une erreur | $h$ de l'ordre de $10^{-5}$ pour une différence centrée en `float64` |
| Sommer au lieu de faire la moyenne | $\nabla\frac1N\sum_kf_k = \sum_k\nabla f_k$ | $\frac1N\sum_k\nabla f_k$ |

## Hessienne, conditionnement et convergence (M19)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier le $\frac12$ du terme d'ordre 2 | $f(\mathbf{x} + \mathbf{h}) \approx f + \nabla f^\top\mathbf{h} + \mathbf{h}^\top\mathbf{H}\mathbf{h}$ | $\frac12\mathbf{h}^\top\mathbf{H}\mathbf{h}$, comme le $\frac12f''h^2$ d'une variable |
| Calculer $H_{ij}$ et $H_{ji}$ séparément dans une hessienne numérique | deux formules qui diffèrent par les arrondis, puis `np.linalg.eigvalsh`, qui ne lit qu'un triangle | calculer chaque case au-dessus de la diagonale une fois, puis la recopier |
| Classer un point critique par la diagonale de la hessienne | $`\begin{pmatrix} 1 & 2 \cr 2 & 1 \end{pmatrix}`$ « positive », donc un minimum | les signes des **valeurs propres** ($3$ et $-1$ : une selle) |
| Conclure par le déterminant en dimension 3 | $\det\mathbf{H} = 6 > 0$, donc un minimum, pour des valeurs propres $(-1, -2, 3)$ | regarder toutes les valeurs propres |
| Regarder la plus grande valeur propre signée | valeurs propres $0{,}5$ et $-1{,}2$ : « tout est sous 1, ça converge » | le plus grand **module** : $1{,}2 > 1$, l'itération diverge |
| Régler le pas sur la plus petite valeur propre | $\omega = 2/\lambda_{\min}$ | $\omega < 2/\lambda_{\max}$ : c'est la plus grande valeur propre qui fixe le pas critique |
| Croire qu'un facteur près de 1 suffit | $\rho = 0{,}99$ « converge vite » | environ 230 itérations par décimale gagnée : regarder $\frac{\ln 10}{-\ln\rho}$ |
| Croire que multiplier le système change le conditionnement | multiplier $\mathbf{A}$ et $\mathbf{b}$ par 100 « pour aller plus vite » | le pas critique est divisé par 100, $\kappa$ et le nombre d'itérations ne changent pas ; mettre les **inconnues** à l'échelle peut le changer |
| Se tromper de signe sur $q$ | $u_{k+2} = 1{,}5\thinspace u_{k+1} + u_k$ écrit $r^2 - 1{,}5r + 1$ | $u_{k+2} = a\thinspace u_{k+1} + b\thinspace u_k$ donne $r^2 - ar - b$ |
| Prendre la partie réelle pour le module | racines $0{,}4 \pm 0{,}4\sqrt3\thinspace i$ « de module $0{,}4$ » | $\sqrt{0{,}4^2 + 0{,}48} = 0{,}8 = \sqrt q$ |
| Diviser l'erreur type par $B$ | estimation sur $B = 4$ termes : erreur type $\sigma/4$ | $\sigma/\sqrt B = \sigma/2$ ; la **variance** est divisée par $B$ |
| Projeter sur la boule en coupant les coordonnées | $(15, -8)$ sur la boule de rayon $3{,}4$ : $(3{,}4 ;\ -3{,}4)$ | $\mathbf{x}\min(1, r/\lVert\mathbf{x}\rVert) = (3 ;\ -1{,}6)$ ; couper les coordonnées projette sur un pavé |

## Tenseurs, axes et estimateurs pondérés (M20)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Remodeler pour réordonner des axes | `img.reshape(3, 480, 640)` pour mettre les canaux d'une image $(480, 640, 3)$ en premier | `img.transpose(2, 0, 1)` ; `reshape` garde l'ordre de la file et mélange les canaux |
| Se tromper d'axe | `N.mean(axis=0)` pour la moyenne de chaque élève d'un tableau (élèves, matières) | l'axe nommé **disparaît** : `N.mean(axis=1)` |
| Oublier `keepdims` avant de soustraire | `T - T.mean(axis=2)` pour un tableau (stations, jours, heures) | `T - T.mean(axis=2, keepdims=True)` |
| La diffusion silencieuse | `u - v` avec `u` de forme $(5,)$ et `v` de forme $(5, 1)$ : un tableau $(5, 5)$, sans erreur | vérifier la forme ; `u - v.ravel()` |
| Composer des variances | la variance sur deux axes calculée comme la variance des variances | la variance sur les deux axes d'un coup, `x.var(axis=(1, 2))` ; ou, pour des groupes de même taille, la moyenne des variances plus la variance des moyennes |
| Mélanger les ddof | `np.var` (divise par $N$) comparé à `pd.Series.var` (divise par $N - 1$) | écrire `ddof` explicitement |
| Oublier qu'une lettre absente du résultat est sommée | `np.einsum("ij,jk->ijk", A, B)` pour un produit matriciel | `"ij,jk->ik"` ; et toujours la forme explicite, avec `->` |
| Croire que la standardisation gomme tout changement | ajouter 10 à une seule valeur « ne change pas les z-scores » | seule une transformation $a\mathbf{x} + b\mathbf{1}$ de **toute** la série, $a > 0$, les laisse inchangés |
| Croire qu'un estimateur sans biais est exact | une estimation de Horvitz-Thompson à deux écarts types du total « est fausse » | sans biais = juste **en moyenne** sur les échantillons possibles |
| Multiplier toutes les valeurs par les indicatrices | `np.sum(y * included / pi)` quand les valeurs non tirées sont des `nan` | `np.sum(y[included] / pi[included])` |
| La moyenne naïve avec des probabilités inégales | `N * y[S].mean()` quand les grandes unités sont tirées plus souvent : biaisée | $\sum_{i \in S} y_i/\pi_i$ |
| Multiplier les jacobiennes dans le mauvais ordre | $\mathbf{J}(\mathbf{x}_0)\thinspace\mathbf{J}(\mathbf{x}_1)$ pour deux pas | $\mathbf{J}(\mathbf{x}_1)\thinspace\mathbf{J}(\mathbf{x}_0)$ : le dernier pas à gauche |
