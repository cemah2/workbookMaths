# M27 · Jeux et distances entre lois — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M27.Q1 — Maximin, minimax et point selle : qui annonce son coup en premier, et qui y gagne ?

<details><summary>Indice 1</summary>

Fiche §1 : « Le maximin et le minimax », les propriétés, puis « L'ordre des coups compte ».

</details>
<details><summary>Indice 2</summary>

Maximin : le plus grand des minimums des lignes. Minimax : le plus petit des maximums des colonnes. Celui qui annonce d'abord subit la meilleure réponse de l'autre.

</details>
<details><summary>Indice 3</summary>

1. Minimums des lignes : 1 et 5 ; maximums des colonnes : 6, 8, 7. 4. Relie l'avantage du second à l'inégalité maximin $\le$ minimax. 5. Relis la définition d'un point selle : le plus petit de quoi, le plus grand de quoi ?

</details>

### M27.Q2 — Stratégies mixtes, gain espéré et valeur d'un jeu : vrai ou faux

<details><summary>Indice 1</summary>

Fiche §2 : la définition du gain espéré, la meilleure réponse, le principe d'indifférence, le théorème de von Neumann.

</details>
<details><summary>Indice 2</summary>

$E(\mathbf{p}, \mathbf{q}) = \mathbf{p}^\top\mathbf{G}\mathbf{q}$ ; contre $\mathbf{q}$ fixé, c'est une moyenne des $(\mathbf{G}\mathbf{q})_i$. $p^\star$ se calcule avec les colonnes de $\mathbf{G}$.

</details>
<details><summary>Indice 3</summary>

2. Calcule d'abord $\mathbf{G}\mathbf{q}$, le gain de chaque ligne pure contre $q = 0{,}5$, puis sa moyenne pondérée par $(0{,}25 ;\ 0{,}75)$. 5. Fiche §2, juste après le théorème de von Neumann.

</details>

### M27.Q3 — Équilibres de Nash, arbres de jeu et descente-montée : unique ou non, le meilleur pour tous ou non, converger ou tourner ?

<details><summary>Indice 1</summary>

Fiche §3 (le dilemme, la coordination, l'induction arrière) et §4 (les modules des valeurs propres de $\mathbf{M}_s$ et de $\mathbf{M}_a$).

</details>
<details><summary>Indice 2</summary>

Un arbre se résout des feuilles vers la racine : minimum aux nœuds du second joueur, maximum à ceux du premier.

</details>
<details><summary>Indice 3</summary>

3. Après G, le second choisit $\min(3, 7)$ ; après D, $\min(5, 2)$ ; puis le premier prend le plus grand. 4. Quel est le module de $1 \pm i\eta$ ? 5. Que vaut le déterminant de $\mathbf{M}_a$ ?

</details>

### M27.Q4 — La probabilité a posteriori et la log-loss ; Jensen-Shannon et KL quand les supports se séparent

<details><summary>Indice 1</summary>

Fiche §5 (le théorème et la règle de score propre) et §6 (les propriétés de JS, les deux masses ponctuelles).

</details>
<details><summary>Indice 2</summary>

$t^\star(x) = \frac{\pi_1p_1(x)}{\pi_1p_1(x) + \pi_0p_0(x)}$. Pour des supports disjoints, $m = \frac{p + q}{2}$ vaut la moitié de chaque loi sur son support.

</details>
<details><summary>Indice 3</summary>

1. $\pi_1 = 0{,}2$ et $\pi_0 = 0{,}8$ : $\frac{0{,}1}{0{,}1 + 0{,}08}$. 4. Chaque $\mathrm{KL}(\cdot \,\|\, m)$ vaut $\ln\frac{1}{1/2}$ ; en bits, divise par $\ln 2$. Pour $\mathrm{KL}(p \,\|\, q)$, regarde un point où $p > 0$ et $q = 0$.

</details>

### M27.Q5 — Couplages et distances de Wasserstein : marges, translation, dilatation, et W₁ ≤ W₂

<details><summary>Indice 1</summary>

Fiche §7 (la définition d'un couplage, $W_1 \le W_2$, la dualité) et §8 (« Deux gaussiennes, une translation »).

</details>
<details><summary>Indice 2</summary>

Un couplage a pour sommes des lignes $\mathbf{a}$ et pour sommes des colonnes $\mathbf{b}$. Une translation de $\theta$ : $W_p = \lvert\theta\rvert$. Deux gaussiennes : $W_2^2 = (\Delta\mu)^2 + (\Delta\sigma)^2$.

</details>
<details><summary>Indice 3</summary>

1. Additionne les colonnes de $\boldsymbol{\Gamma}$. 3. Quelle est la loi de $3X$ si $X$ suit $\mathcal{N}(0, 2^2)$ ? 5. Pense à la terre de Monge du §7 : un déplacement moyen de 1, et $W_1 = 1{,}2$.

</details>

### M27.Q6 — La distance de Fréchet et son estimation : rotation commune, covariances, taille des échantillons

<details><summary>Indice 1</summary>

Fiche §9 : la formule, l'invariance par une rotation commune, le biais d'une distance estimée.

</details>
<details><summary>Indice 2</summary>

Avec des covariances égales, la part des covariances est nulle. $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 = \lVert\Delta\boldsymbol{\mu}\rVert^2 + \frac{\operatorname{tr}\boldsymbol{\Sigma}_1}{n_1} + \frac{\operatorname{tr}\boldsymbol{\Sigma}_2}{n_2}$.

</details>
<details><summary>Indice 3</summary>

3. $\sqrt{4 + 9 + 36}$. 4. Ici $\Delta\boldsymbol{\mu} = \mathbf{0}$. 5. Que devient $\frac{1}{n_1} + \frac{1}{n_2}$ quand on double $n_1$ et $n_2$ ?

</details>

### M27.Q7 — Mesurer une dérive : PSI, KS ou W₁, leurs unités, et ce que chacun ne voit pas

<details><summary>Indice 1</summary>

Fiche §10, « Ce que chacun mesure », et la borne $W_1 \le (b - a)\,\mathrm{KS}$.

</details>
<details><summary>Indice 2</summary>

KS ne voit que l'ordre des valeurs ; $W_1$ a l'unité de la variable ; le PSI ne voit que les proportions des classes.

</details>
<details><summary>Indice 3</summary>

1. Une même fonction croissante appliquée aux deux lois, puis un facteur 1,8 sur toutes les distances. 3. Toute la masse de l'une est à gauche de toute la masse de l'autre. 4. $b - a = 30$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M27.R1 — Le maximum de vraisemblance d'une loi de Bernoulli (des comptes entiers), et la log-loss quand la probabilité prédite tend vers 0 (M04, M13a)

<details><summary>Indice 1</summary>

Fiche §5, « Rappel : la meilleure constante » ; ∂ M04.12 et ✏️ M13a.1.

</details>
<details><summary>Indice 2</summary>

Le maximum de vraisemblance d'une loi de Bernoulli est la fréquence $\frac{k}{n}$. La log-loss d'une observation qui vaut 1 est $-\ln t$.

</details>
<details><summary>Indice 3</summary>

2. La log-loss moyenne d'une constante $t$ vaut $-\frac{1}{n}\big[k\ln t + (n - k)\ln(1 - t)\big]$. 3. $-\ln(10^{-5}) = 5\ln 10$. 4. Une moyenne de nombres positifs est au moins un de ses termes divisé par leur nombre.

</details>

### M27.R2 — Les valeurs propres complexes d'une matrice réelle 2 × 2, leur module et les puissances (M22)

<details><summary>Indice 1</summary>

M22 : valeurs propres d'une matrice $2 \times 2$ par la trace et le déterminant, forme exponentielle.

</details>
<details><summary>Indice 2</summary>

Trace 2, déterminant 4 : $\lambda^2 - 2\lambda + 4 = 0$. Le module d'un complexe conjugué au carré est le déterminant.

</details>
<details><summary>Indice 3</summary>

3. Calcule $\mathbf{A}^2$, puis $\mathbf{A}^3$ : tu tomberas sur un multiple de $\mathbf{I}$. 4. Essaie $\mathbf{x} = (1, 0)$.

</details>

### M27.R3 — La racine carrée d'une matrice symétrique positive, et la trace comme somme des valeurs propres (M12c)

<details><summary>Indice 1</summary>

M12c §8 (la racine carrée d'une matrice symétrique positive, unique) et M12c §2 (la trace, somme des valeurs propres).

</details>
<details><summary>Indice 2</summary>

Les valeurs propres de $\mathbf{R}^2$ sont les carrés de celles de $\mathbf{R}$.

</details>
<details><summary>Indice 3</summary>

2. $\mathbf{R}$ est-elle symétrique ? Ses valeurs propres sont-elles positives (regarde sa trace et son déterminant) ? 4. $\sum_i\sqrt{\lambda_i(\mathbf{S})} = \sum_i\lambda_i(\mathbf{R})$. 5. Élève la matrice au carré.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M27.1 — Deux enseignes se partagent un marché : réduire une matrice 3 × 4 par dominance, trouver ses deux points selles et vérifier qu'ils ont la même valeur, et ce que la réduction ne change pas (maximin, minimax)

<details><summary>Indice 1</summary>

Fiche §1 : le maximin et le minimax, le point selle, « Les stratégies dominées » (et le ⚠️ : une colonne est dominée quand elle coûte **plus**).

</details>
<details><summary>Indice 2</summary>

Écris les minimums des lignes à droite du tableau et les maximums des colonnes en dessous. Un point selle est un minimum de ligne qui est aussi un maximum de colonne : un minimum peut être atteint dans plusieurs cases.

</details>
<details><summary>Indice 3</summary>

Commence par comparer A3 aux deux autres lignes, et B3 aux trois autres colonnes. Pour c), regarde la ligne A3 dans les colonnes B1, B2 et B4. Pour la justification générale, compare le minimum de la ligne rayée à celui de la ligne qui la domine.

</details>

### Ex M27.2 — Tirs au but : la probabilité de tirer à gauche par indifférence, la réponse du gardien et la valeur du jeu

<details><summary>Indice 1</summary>

Fiche §2 : le principe d'indifférence, l'exemple du volley et le théorème $2 \times 2$.

</details>
<details><summary>Indice 2</summary>

$a = 55$, $b = 95$, $c = 85$, $d = 60$, $\kappa = a - b - c + d$. $p^\star = \frac{d - c}{\kappa}$ rend le gardien indifférent, $q^\star = \frac{d - b}{\kappa}$ rend le tireur indifférent.

</details>
<details><summary>Indice 3</summary>

d) Le gain espéré de chaque tir pur contre $q = 0{,}65$ : $0{,}65 \times (\text{gain contre un plongeon à gauche}) + 0{,}35 \times (\text{gain contre un plongeon à droite})$. e) Le gain espéré de $p = 0{,}55$ contre chaque plongeon, puis le plus petit des deux.

</details>

### Ex M27.3 — Les équilibres de Nash d'un dilemme du prisonnier et d'un jeu de coordination (purs et mixte), puis la valeur d'un jeu d'allumettes par induction arrière

<details><summary>Indice 1</summary>

Fiche §3 : la définition de l'équilibre de Nash, le dilemme, la coordination, et l'exemple des allumettes (avec une autre règle).

</details>
<details><summary>Indice 2</summary>

Dans un équilibre mixte, chaque probabilité rend l'**autre** équipe indifférente : elle s'écrit avec les gains de l'autre. Pour les allumettes, une position est perdante si tous les coups mènent à une position gagnante pour l'adversaire.

</details>
<details><summary>Indice 3</summary>

c) L'équipe des colonnes gagne en moyenne $3x$ avec X et $4(1 - x)$ avec Y. d) L'équipe des lignes gagne $5y$ avec X et $3(1 - y)$ avec Y. f) Avec 1 allumette, on doit prendre la dernière : 1 est perdante ; remonte jusqu'à 12.

</details>

### Ex M27.4 — Descente-montée sur f(x, y) = xy : la matrice d'un pas simultané puis alterné, leurs valeurs propres et leurs modules, et deux pas différents pour x et y

<details><summary>Indice 1</summary>

Fiche §4 : $\mathbf{M}_s = \sqrt{1 + \eta^2}\,\mathbf{R}_\theta$, puis $\mathbf{M}_a$, son déterminant et sa trace ; M22 pour les valeurs propres complexes.

</details>
<details><summary>Indice 2</summary>

Le module de $1 \pm i\eta$ est $\sqrt{1 + \eta^2}$, son argument $\arctan\eta$. Pour deux valeurs propres conjuguées de module 1, $2\cos\theta$ est la trace.

</details>
<details><summary>Indice 3</summary>

c) Cherche le plus petit $k$ avec $1{,}36^{k/2} \ge 2$. e) Écris $y_{k+1} = y_k + b\,x_{k+1}$ en fonction de $x_k$ et $y_k$ pour obtenir la seconde ligne de la matrice alternée. f) La trace vaut $2 - ab = -4$ et le déterminant 1 : résous $\lambda^2 + 4\lambda + 1 = 0$.

</details>

### Ex M27.5 — Deux fournisseurs et un défaut noté sur quatre niveaux : la probabilité a posteriori, et la log-loss moyenne de trois prédicteurs (a priori, a posteriori, trop sûr de lui)

<details><summary>Indice 1</summary>

Fiche §5 : le théorème, l'exemple des pommes et la définition de $R(t)$.

</details>
<details><summary>Indice 2</summary>

Commence par le tableau des probabilités jointes $P(X = x, Y = 1) = 0{,}32\,p_1(x)$ et $P(X = x, Y = 0) = 0{,}68\,p_0(x)$ ; tout le reste s'en déduit.

</details>
<details><summary>Indice 3</summary>

b) $t^\star(x) = \frac{P(X = x, Y = 1)}{P(X = x)}$. c) à e) $R(t) = -\sum_x\big[P(x, 1)\ln t(x) + P(x, 0)\ln(1 - t(x))\big]$, une somme de huit termes ; pour le prédicteur a priori, $t(x) = 0{,}32$ partout.

</details>

### Ex M27.6 — Deux lois uniformes de même largeur, translatées : JS en fonction du décalage, la KL, et ce que le décalage lui-même mesure

<details><summary>Indice 1</summary>

Fiche §6 (la définition de JS, les supports disjoints) et §8 (« Une translation »).

</details>
<details><summary>Indice 2</summary>

Pour $0 < \theta < 5$, $p$ et $q$ valent $\frac15$ sur leur fenêtre ; sur la partie commune, $m = \frac15$, et ailleurs $m = \frac{1}{10}$ là où l'une des deux est positive.

</details>
<details><summary>Indice 3</summary>

$\mathrm{KL}(p \,\|\, m) = \int p\ln\frac{p}{m}$ : seule la partie où $p$ est seule compte, de longueur $\theta$, et l'intégrand y vaut $\frac15\ln 2$. Pour $\theta \ge 5$, toute la fenêtre de $p$ est dans ce cas.

</details>

### Ex M27.7 — Trois dépôts et trois magasins le long d'une route : vérifier des couplages, leur coût, le couplage indépendant et le plan monotone (coin nord-ouest)

<details><summary>Indice 1</summary>

Fiche §7 (couplage, coût d'un plan, couplage indépendant) et §8 (la règle du coin nord-ouest, la terre de Monge).

</details>
<details><summary>Indice 2</summary>

Écris d'abord la matrice des distances $\lvert x_i - y_j\rvert$ ; le coût d'un plan est la somme des produits coefficient par coefficient. Le couplage indépendant, avec des masses de total 100 t : $\gamma_{ij} = \frac{a_ib_j}{100}$.

</details>
<details><summary>Indice 3</summary>

Coin nord-ouest : en (1, 1), mets $\min(20, 40)$ ; le dépôt 1 est vide, descends ; puis continue, en allant à droite chaque fois qu'un magasin est plein. e) Divise le coût optimal par la masse totale.

</details>

### Ex M27.8 — W₁ et W₂ par l'aire entre les fonctions de répartition et par les quantiles : deux lois uniformes, puis W₂ de deux gaussiennes (et W₁ quand elles ont le même écart-type)

<details><summary>Indice 1</summary>

Fiche §8 : le couplage des quantiles, les deux formules de $W_1$, $W_2$ de deux gaussiennes, une translation.

</details>
<details><summary>Indice 2</summary>

$F(x) = \frac{x}{4}$ sur $[0 ; 4]$, $G(x) = x - 1$ sur $[1 ; 2]$. Les quantiles : $F^{-1}(u) = 4u$ et $G^{-1}(u) = 1 + u$.

</details>
<details><summary>Indice 3</summary>

a) Sur $[1 ; 2]$, $F - G = 1 - \frac{3x}{4}$ change de signe en $x = \frac43$ : coupe l'intégrale en ce point. Ou bien $\int_0^1\lvert 3u - 1\rvert\,\mathrm{d}u$, coupée en $u = \frac13$. b) $\int_0^1(3u - 1)^2\,\mathrm{d}u$. c) $\Delta\mu = 1{,}2$ et $\Delta\sigma = 0{,}5$.

</details>

### Ex M27.9 — La distance de Fréchet de deux gaussiennes du plan à covariances diagonales, puis tournées ensemble : la part des moyennes et celle des covariances

<details><summary>Indice 1</summary>

Fiche §9 : la formule, la propriété $\sum_i\sqrt{\lambda_i(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)}$, le cas commutatif et l'invariance par une rotation commune.

</details>
<details><summary>Indice 2</summary>

Valeurs propres par $\lambda^2 - (\operatorname{tr}\boldsymbol{\Sigma})\lambda + \det\boldsymbol{\Sigma} = 0$, puis un vecteur propre par une ligne de $\boldsymbol{\Sigma} - \lambda\mathbf{I}$.

</details>
<details><summary>Indice 3</summary>

Les deux matrices ont les vecteurs propres $(3, 4)$ et $(4, -3)$ : sur chacun, les valeurs propres de $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2$ sont les produits des valeurs propres de $\boldsymbol{\Sigma}_1$ et de $\boldsymbol{\Sigma}_2$ sur ce même vecteur. Les écarts-types sont les racines des valeurs propres.

</details>

### Ex M27.10 — Une dérive en deux mois d'une variable à trois catégories : la divergence de Jeffreys (le PSI) et JS, puis l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage ; enfin KS et W₁ entre deux petits échantillons de températures de même taille

<details><summary>Indice 1</summary>

Fiche §10 (le PSI, son approximation, KS et $W_1$, les unités) et §6 (JS).

</details>
<details><summary>Indice 2</summary>

$\mathrm{PSI} = \sum_k(p_k - q_k)\ln\frac{p_k}{q_k}$ ; pour JS, $m = \frac{p + q}{2}$. Pour les températures, trie les deux échantillons.

</details>
<details><summary>Indice 3</summary>

d) Parcours les dix valeurs triées ensemble ; à chaque valeur, la fonction de répartition de son mois monte de 0,2 ; note l'écart après chaque valeur. e) La moyenne des écarts absolus entre la $k$-ième valeur de janvier et la $k$-ième de février, une fois triées. f) Que fait $C \mapsto 1{,}8\,C + 32$ à l'écart entre deux valeurs, et à leur ordre ?

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M27.11 — Le maximin est au plus le minimax ; ils sont égaux si et seulement si le jeu a un point selle, et deux points selles ont la même valeur

<details><summary>Indice 1</summary>

Fiche §1 : l'idée de l'inégalité (la case où se croisent la ligne du maximin et la colonne du minimax).

</details>
<details><summary>Indice 2</summary>

Un point selle $(i, j)$ : $g_{ij} = \min_lg_{il}$ et $g_{ij} = \max_kg_{kj}$. Le maximin est au moins le minimum de **chaque** ligne, et le minimax au plus le maximum de **chaque** colonne.

</details>
<details><summary>Indice 3</summary>

3. Si maximin $=$ minimax, les deux inégalités de la question 1 deviennent des égalités. 4. Encadre $g_{il}$ : par le point selle $(i, j)$, il est au moins le minimum de la ligne $i$ ; par le point selle $(k, l)$, il est au plus le maximum de la colonne $l$.

</details>

### Ex M27.12 — La log-loss espérée est minimale pour la probabilité a posteriori : une preuve par l'inégalité de Gibbs

<details><summary>Indice 1</summary>

Fiche §5 (l'idée de la preuve) ; M04 (Bayes, probabilités totales) ; M06 (l'inégalité de Gibbs et son cas d'égalité).

</details>
<details><summary>Indice 2</summary>

$R(t) = \sum_x\sum_yP(X = x, Y = y)\,\ell(t(x), y)$, et $P(X = x, Y = y) = P(X = x)\,P(Y = y \mid X = x)$.

</details>
<details><summary>Indice 3</summary>

2. À $x$ fixé, regroupe les termes en $t^\star\ln$ et en $(1 - t^\star)\ln$ : $-t^\star\ln t + t^\star\ln t^\star = t^\star\ln\frac{t^\star}{t}$. 3. Chaque poids $P(X = x)$ est strictement positif. 4. Une constante ignore $X$ : refais 1 et 2 avec une seule valeur de $X$.

</details>

### Ex M27.13 — 0 ≤ JS ≤ ln 2, et JS = ln 2 si et seulement si les deux lois ont des supports disjoints

<details><summary>Indice 1</summary>

Fiche §6 (l'idée : $m \ge \frac{p}{2}$) ; M06 (Gibbs).

</details>
<details><summary>Indice 2</summary>

Pour $p_k > 0$, $\frac{p_k}{m_k} \le 2$. $\mathrm{KL}(p \,\|\, m)$ est une moyenne de $\ln\frac{p_k}{m_k}$, pondérée par les $p_k$.

</details>
<details><summary>Indice 3</summary>

3. Une moyenne à poids strictement positifs de nombres $\le \ln 2$ vaut $\ln 2$ si et seulement si chacun vaut $\ln 2$. 4. Écris les deux cas d'égalité, pour $p$ et pour $q$, puis traduis-les sur les supports ; n'oublie pas la réciproque.

</details>

### Ex M27.14 — L'appariement trié est optimal : un argument d'échange sur deux paires, puis sur n paires, pour les coûts |x − y| et (x − y)²

<details><summary>Indice 1</summary>

Fiche §8 : « L'appariement trié » et son idée, l'argument d'échange.

</details>
<details><summary>Indice 2</summary>

1. Développe : les carrés $x_i^2$ et $y_j^2$ s'en vont. 2. Les deux écarts de l'appariement trié sont compris entre $x_1 - y_2$ et $x_2 - y_1$, et ont la même somme qu'eux ; la valeur absolue est convexe.

</details>
<details><summary>Indice 3</summary>

3. Si $\sigma$ n'est pas l'identité, il existe un $i$ avec $\sigma(i) > \sigma(i + 1)$ ; échange ces deux valeurs et applique 1 et 2 aux deux paires concernées. 4. Essaie deux $x$ tous les deux à gauche des deux $y$.

</details>

### Ex M27.15 — E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ : une distance estimée sur deux échantillons est biaisée vers le haut

<details><summary>Indice 1</summary>

Fiche §9 (l'idée) ; M02c (la variance d'une moyenne, la matrice de covariance).

</details>
<details><summary>Indice 2</summary>

1. $\lVert\mathbf{v}\rVert^2 = \sum_kv_k^2$ et $\mathbb{E}[v_k^2] = \mathbb{V}(v_k) + (\mathbb{E}v_k)^2$. 2. La covariance d'une somme de vecteurs indépendants est la somme des covariances.

</details>
<details><summary>Indice 3</summary>

2. $\operatorname{Cov}\big(\frac{1}{n}\sum_i\mathbf{x}_i\big) = \frac{1}{n^2}\sum_i\operatorname{Cov}(\mathbf{x}_i)$. 4. Retire à $\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2$ ce que la question 3 ajoute en moyenne.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M27.16 — Pont : la distance de Fréchet en dimension 1, W₂² = (Δμ)² + (Δσ)², entre deux lois résumées par leur moyenne et leur écart-type (deux séries d'une machine, avant et après réglage) : la part de la moyenne et celle de l'écart-type, et pourquoi workbookIA 27 l'écrit avec des covariances et en rend le carré

<details><summary>Indice 1</summary>

Fiche §8 ($W_2$ de deux gaussiennes) et §9 (la formule de Fréchet, et la convention : la distance est $W_2$, la formule en donne le carré).

</details>
<details><summary>Indice 2</summary>

$\Delta\mu = 0{,}28$ mm et $\Delta\sigma = 0{,}07$ mm. En dimension 1, $\boldsymbol{\Sigma}_k = [[\sigma_k^2]]$ et $(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)^{1/2} = [[\sigma_1\sigma_2]]$.

</details>
<details><summary>Indice 3</summary>

d) $\sigma_1^2 + \sigma_2^2 - 2\sigma_1\sigma_2$. e) Remplace $\sigma_k^2$ par $\sigma_k$ dans la formule, sans oublier la part des moyennes.

</details>

### Ex M27.17 — MML §7.2 relu : l'inégalité minimax (7.23) et sa preuve, la dualité faible (7.27) lue comme un jeu, et l'inégalité vérifiée sur une matrice de gains choisie

<details><summary>Indice 1</summary>

Le guide de lecture de MML de la fiche, et la fin du §1, « La dualité faible, un jeu ».

</details>
<details><summary>Indice 2</summary>

Dans (7.23), le max est dehors à gauche et le min dehors à droite. Pour la matrice : $\min_lg_{il} \le g_{ij} \le \max_kg_{kj}$.

</details>
<details><summary>Indice 3</summary>

4. La contrainte s'écrit $g(x) = x + 1 \le 0$, donc $\mathcal{L} = (x - 2)^2 + \lambda(x + 1)$ avec $\lambda \ge 0$. Pour $D(\lambda)$, annule la dérivée en $x$ à $\lambda$ fixé. Pour une matrice $2 \times 3$ sans point selle, vérifie qu'aucun minimum de ligne n'est un maximum de colonne.

</details>

### Ex M27.18 — Expliquer avec une partie de cache-cache pourquoi jouer au hasard peut être la meilleure stratégie, et ce que le hasard garantit

<details><summary>Indice 1</summary>

Fiche §2 : « Jouer au hasard », le principe d'indifférence, et la phrase sur l'attaquant de gauche du volley.

</details>
<details><summary>Indice 2</summary>

Ce que fait le chercheur s'il connaît l'habitude ; ce qu'il fait si les deux cachettes lui semblent aussi bonnes l'une que l'autre.

</details>
<details><summary>Indice 3</summary>

Le dosage rend le chercheur indifférent : c'est ce qui rend la garantie indépendante de sa stratégie. Une garantie en moyenne, pas une partie gagnée d'avance.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M27.E1 — « Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se recouvrent pas, et pas Jensen-Shannon ? »

<details><summary>Indice 1</summary>

Fiche §6, « Aveugle quand les supports se séparent », et la figure de JS en fonction du décalage.

</details>
<details><summary>Indice 2</summary>

Deux masses ponctuelles en 0 et en $\theta$ : que valent JS, la KL et $W_1$, et comment varient-elles avec $\theta$ ?

</details>
<details><summary>Indice 3</summary>

Une réponse en trois temps : ce que JS ne voit pas (le plafond et la pente nulle), ce que $W_1$ mesure (un transport), une limite de $W_1$.

</details>

### M27.E2 — « Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et comment comparer deux mesures ? »

<details><summary>Indice 1</summary>

Fiche §9, « Le biais d'une distance estimée », et §10 (la p-valeur de KS).

</details>
<details><summary>Indice 2</summary>

Le biais $\operatorname{tr}\boldsymbol{\Sigma}\,\big(\frac{1}{n_1} + \frac{1}{n_2}\big)$ dépend des tailles.

</details>
<details><summary>Indice 3</summary>

Trois remèdes : comparer à tailles égales, retirer une estimation du biais, et comparer à la distance entre deux moitiés de la référence ; un test donne une p-valeur.

</details>

<a id="notebook"></a>

## Notebook

### M27.19 — Les valeurs d'un jeu en stratégies pures : maximin, minimax et coups prudents, points selles compris : `pure_strategy_values`

<details><summary>Indice 1</summary>

La docstring de `pure_strategy_values` et son TODO ; la fiche §1.

</details>
<details><summary>Indice 2</summary>

`G = np.array(G, dtype=float)` (une copie ; une entrée qui n'est pas un nombre lève une erreur à convertir en `ValueError`) ; contrôle `G.ndim == 2`, `G.size > 0` et `np.isfinite(G).all()`.

</details>
<details><summary>Indice 3</summary>

`rows = G.min(axis=1)`, `cols = G.max(axis=0)`, `row = int(np.argmax(rows))`, `col = int(np.argmin(cols))`, `return float(rows[row]), float(cols[col]), row, col`. Pour b), `mymath.distances.pure_strategy_values(-G.T)`.

</details>

### M27.20 — Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle : `mixed_strategy_value_2x2`

<details><summary>Indice 1</summary>

La docstring de `mixed_strategy_value_2x2` et son TODO ; la fiche §2 (le théorème $2 \times 2$ et le ⚠️ sur le point selle).

</details>
<details><summary>Indice 2</summary>

Contrôle `G.shape == (2, 2)` avant tout ; puis `maximin, minimax, row, col = pure_strategy_values(G)` (le contrôle des nombres finis y est déjà).

</details>
<details><summary>Indice 3</summary>

`if maximin == minimax: return (1.0 if row == 0 else 0.0), (1.0 if col == 0 else 0.0), maximin` ; sinon `(a, b), (c, d) = G.tolist()`, `k = a - b - c + d`, et les trois formules en `float`. Pour c), `p_star = np.array([p, 1 - p])`, puis `(p_star @ G).min()` ; de même `(G @ q_star).max()`.

</details>

### M27.21 — Les itérés de la descente-montée simultanée ou alternée sur un jeu bilinéaire xᵀAy : `descent_ascent_iterates`

<details><summary>Indice 1</summary>

La docstring de `descent_ascent_iterates` et son TODO ; la fiche §4 (les deux pas, les deux propriétés).

</details>
<details><summary>Indice 2</summary>

`x = np.array(x0, dtype=float)` doit avoir la forme `(n,)` exactement, `y` la forme `(m,)` ; `eta` : `isinstance(eta, numbers.Real) and not isinstance(eta, (bool, np.bool_))`, fini, $> 0$ ; `n_steps` : `numbers.Integral`, ni `bool` ni `np.bool_`, $\ge 0$.

</details>
<details><summary>Indice 3</summary>

`xs = np.empty((n_steps + 1, n))`, `ys = np.empty((n_steps + 1, m))`, `xs[0], ys[0] = x, y` ; puis `x_new = x - eta * (A @ y)`, `y = y + eta * (A.T @ (x_new if alternating else x))`, `x = x_new`, et `xs[k + 1], ys[k + 1] = x, y`. Pour b), `Q = xs[:, 0]**2 + ys[:, 0]**2 - eta * xs[:, 0] * ys[:, 0]`. Pour c), `np.einsum("ki,ij,kj->k", xs, A, ys)` donne les $\mathbf{x}_k^\top\mathbf{A}\mathbf{y}_k$.

</details>

### M27.22 — W₂ de deux gaussiennes en dimension 1, à partir des moyennes et des écarts-types : `w2_gaussians_1d`

<details><summary>Indice 1</summary>

La docstring de `w2_gaussians_1d` et son TODO ; la fiche §8.

</details>
<details><summary>Indice 2</summary>

Pour chaque argument : `isinstance(v, numbers.Real) and not isinstance(v, (bool, np.bool_))`, puis `math.isfinite(v)` ; les écarts-types $\ge 0$.

</details>
<details><summary>Indice 3</summary>

`return float(math.hypot(mu1 - mu2, sigma1 - sigma2))`. Pour b), `mymath.distances.w2_gaussians_1d(50.30, 0.12, 50.02, 0.05)`.

</details>

### M27.23 — `scipy.optimize.linprog` : le transport optimal entre deux lois discrètes de la droite comme programme linéaire, comparé au plan monotone et à l'aire entre les fonctions de répartition

<details><summary>Indice 1</summary>

Fiche §7 (« Un programme linéaire ») et §8 (la règle du coin nord-ouest) ; la documentation de `scipy.optimize.linprog` (arguments `c`, `A_eq`, `b_eq`, `bounds`).

</details>
<details><summary>Indice 2</summary>

Avec les inconnues rangées ligne par ligne (`plan.ravel()`), la contrainte « ligne $i$ » a des 1 aux positions $in$ à $in + n - 1$, et la contrainte « colonne $j$ » aux positions $j, j + n, j + 2n, \ldots$ : `np.kron(np.eye(m), np.ones(n))` et `np.kron(np.ones(m), np.eye(n))`, empilées par `np.vstack`.

</details>
<details><summary>Indice 3</summary>

`res = linprog(C.ravel(), A_eq=A_eq, b_eq=np.concatenate([a, b]), bounds=(0, None), method="highs")`, puis `res.x.reshape(m, n)` et `res.fun`. Le coin nord-ouest : deux indices `i`, `j`, des copies des masses, `t = min(a[i], b[j])`, et l'on avance `i` si le dépôt est vide, `j` sinon. c) `C = np.linalg.norm(X[:, None, :] - Y[None, :, :], axis=2)`.

</details>

### M27.24 — Prédire la trajectoire de la descente-montée simultanée puis alternée sur xy, puis la tracer : spirale qui s'éloigne ou courbe fermée ?

<details><summary>Indice 1</summary>

Fiche §4 ; ✏️ M27.4 (le module, l'angle, et le pas alterné quand $ab > 4$).

</details>
<details><summary>Indice 2</summary>

a) La distance est multipliée par $\sqrt{1 + \eta^2}$ à chaque pas : calcule $1{,}09^{20}$. b) Chaque pas tourne de $\arctan\eta$. c) Le pas alterné avec $a = b = \eta$ : borné si et seulement si $\eta^2 < 4$.

</details>
<details><summary>Indice 3</summary>

`xs, ys = mymath.distances.descent_ascent_iterates([[1.0]], np.array([1.0]), np.array([0.0]), eta, n_steps, alternating)`, puis `ax.plot(xs[:, 0], ys[:, 0], "-o", ms=3)`, `ax.plot(0, 0, "k*")`, `ax.set_aspect("equal")`. e) `ang = np.unwrap(np.arctan2(ys[:, 0], xs[:, 0]))`, puis `(ang[-1] - ang[0]) / (2 * np.pi)`.

</details>

### M27.25 — Le biais d'une distance estimée : ‖x̄₁ − x̄₂‖² entre deux échantillons d'une même loi de ℝ³, selon leurs tailles, contre tr Σ₁/n₁ + tr Σ₂/n₂

<details><summary>Indice 1</summary>

Fiche §9, « Le biais d'une distance estimée » ; ∂ M27.15.

</details>
<details><summary>Indice 2</summary>

Respecte l'ordre des tirages de l'énoncé : un seul `rng`, la série 1 puis la série 2 à chaque appel, et les appels dans l'ordre donné. `x1` a la forme `(n_rep, n1, 3)`.

</details>
<details><summary>Indice 3</summary>

`d = x1.mean(axis=1) - x2.mean(axis=1)` (forme `(n_rep, 3)`), puis `(d**2).sum(axis=1).mean()`. Pour la figure, `ax.loglog(ns, means, "o")` et `ax.loglog(ns, 2 * trace / np.array(ns), "-")`.

</details>

### M27.26 — Deux fonctions de répartition sur une même figure : l'aire entre elles (W₁) et leur plus grand écart vertical (KS), pour une translation puis une dilatation

<details><summary>Indice 1</summary>

Fiche §8 ($W_1 = \int\lvert F - G\rvert$) et §10 (KS, les unités) ; la documentation de `ax.fill_between` et de `np.trapezoid`.

</details>
<details><summary>Indice 2</summary>

`Fa, Fb = cdf_a(grid), cdf_b(grid)`, `gap = np.abs(Fa - Fb)`, `w1 = np.trapezoid(gap, grid)`, `k = np.argmax(gap)`, `ks = gap[k]`.

</details>
<details><summary>Indice 3</summary>

`ax.plot(grid, Fa, label=label_a)`, de même pour `Fb` ; `ax.fill_between(grid, Fa, Fb, alpha=0.3)` ; `ax.vlines(grid[k], min(Fa[k], Fb[k]), max(Fa[k], Fb[k]))` ; un titre comme `f"W1 = {w1:.3f} {unit}, KS = {ks:.3f}"` ; `return float(w1), float(ks)`.

</details>

### M27.27 — Chasse à l'erreur : une stratégie d'indifférence calculée sur ses propres gains, W₂ de deux gaussiennes avec des variances, des échantillons appariés sans être triés

<details><summary>Indice 1</summary>

Les ⚠️ des §2 et §8 de la fiche ; ∂ M27.14.

</details>
<details><summary>Indice 2</summary>

Pour chaque vérification du collègue, demande-toi quelle propriété particulière de ses données rend l'erreur invisible : un jeu symétrique ($b = c$) ? des écarts-types égaux à 0 ou 1 ? des axes déjà dans l'ordre ?

</details>
<details><summary>Indice 3</summary>

(1) $p^\star$ s'écrit avec $d - c$. (2) $(\sigma_1 - \sigma_2)^2$, pas $(\sigma_1^2 - \sigma_2^2)^2$. (3) `partner = np.empty(len(shafts), dtype=int)` puis `partner[np.argsort(shafts)] = np.argsort(sleeves)` : le $k$-ième plus petit axe reçoit la $k$-ième plus petite bague.

</details>

### M27.28 — Un test de propriété : la valeur d'un jeu 2 × 2 tiré au hasard est entre maximin et minimax, et devient v + c pour G + c et k v pour k G (k > 0)

<details><summary>Indice 1</summary>

Fiche §2 (le théorème $2 \times 2$) ; pour $-\mathbf{G}^\top$, le joueur des lignes devient celui des colonnes ; pour les lignes échangées, la première ligne devient la seconde.

</details>
<details><summary>Indice 2</summary>

Dans la fonction : `if solver is None: solver = mymath.distances.mixed_strategy_value_2x2` (au moment de l'appel, pas à la définition) ; un dictionnaire de cinq compteurs à 0 ; les trois tirages de chaque essai, dans l'ordre de l'énoncé, même pour un jeu avec point selle.

</details>
<details><summary>Indice 3</summary>

`np.allclose(solver(G + c), (p, q, v + c), atol=tol, rtol=0)` ; `lo, hi = G.min(axis=1).max(), G.max(axis=0).min()` ; `if lo < hi:` pour `"transpose"` (`solver(-G.T)` contre `(q, p, -v)`) et `"swap_rows"` (`solver(G[::-1])` contre `(1 - p, q, v)`).

</details>

### M27.29 — Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂, et cette distance, à 10⁻³ près

<details><summary>Indice 1</summary>

Fiche §8 : $W_2^2 = \int_0^1\lvert F^{-1}(u) - G^{-1}(u)\rvert^2\,\mathrm{d}u$, et la fonction quantile $\mu + \sigma\Phi^{-1}(u)$ d'une loi normale.

</details>
<details><summary>Indice 2</summary>

$W_2^2(\mu, \sigma)$ est un problème de moindres carrés : approcher la fonction $F^{-1}$ par une combinaison de 1 et de $\Phi^{-1}$ sur $]0, 1[$. Que valent $\int_0^1\Phi^{-1}(u)\,\mathrm{d}u$ et $\int_0^1\Phi^{-1}(u)^2\,\mathrm{d}u$ ?

</details>
<details><summary>Indice 3</summary>

Les fonctions 1 et $\Phi^{-1}$ sont orthogonales : $\mu = \int_0^1F^{-1}$, $\sigma = \int_0^1F^{-1}\Phi^{-1}$, puis $W_2^2 = \int_0^1(F^{-1})^2 - \mu^2 - \sigma^2$, trois intégrales par `scipy.integrate.quad(..., 0, 1, limit=200)`. Contrôle en recalculant $W_2^2$ directement à $(\mu, \sigma)$.

</details>
