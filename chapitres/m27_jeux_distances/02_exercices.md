# M27 · Jeux et distances entre lois — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m27_jeux_distances/06_mes_reponses.md` (créée par `python tools/start_chapter.py M27`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : $\mathbf{G} = (g_{ij})$ est la matrice des gains d'un jeu à somme nulle, $g_{ij}$ est ce que gagne le joueur des lignes (qui maximise) et ce que paie le joueur des colonnes (qui minimise) ; dans le texte, les stratégies sont numérotées à partir de 1, dans le code à partir de 0 ; dans un jeu $2 \times 2$, $p$ et $q$ sont les probabilités de la première ligne et de la première colonne, et $\kappa = a - b - c + d$ ; au §4, le joueur $\mathbf{x}$ **minimise** et le joueur $\mathbf{y}$ maximise, comme dans MML (7.23), et $\eta > 0$ est un pas ; $\ln$ est le logarithme népérien, et JS, KL et PSI sont en **nats** ; $W_p$ est la distance et $W_p^p$ le coût minimal ; la distance de Fréchet de deux gaussiennes est $W_2$, et la formule de la fiche en donne le carré ; $F(x) = P(X \le x)$ et $F^{-1}(u) = \inf\{x : F(x) \ge u\}$. Dans le notebook, une matrice s'écrit comme la liste de ses lignes, et un vecteur comme une liste ou un tableau **1-D**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 ou 5 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M27.Q1 — Maximin, minimax et point selle : qui annonce son coup en premier, et qui y gagne ? 🧠 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. Pour $\mathbf{G} = \begin{pmatrix} 2 & 9 & 1 \\ 6 & 5 & 7 \end{pmatrix}$, que valent le maximin et le minimax ?
2. Le joueur des lignes doit annoncer sa ligne avant que l'autre choisisse : quelle ligne joue-t-il, et quel gain s'assure-t-il ?
3. C'est au contraire le joueur des colonnes qui annonce d'abord : quelle colonne joue-t-il, et combien paie-t-il ?
4. Vrai ou faux : dans tout jeu à somme nulle, un joueur qui annonce son coup en second ne fait jamais moins bien que s'il l'annonçait en premier.
5. Vrai ou faux : une case qui est la plus grande de sa ligne et la plus petite de sa colonne est un point selle.

### M27.Q2 — Stratégies mixtes, gain espéré et valeur d'un jeu : vrai ou faux 🧠 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

1. Vrai ou faux : contre une stratégie mixte fixée de l'adversaire, il existe toujours une meilleure réponse pure.
2. $\mathbf{G} = \begin{pmatrix} 6 & -1 \\ 2 & 3 \end{pmatrix}$ ; le joueur des lignes joue la première ligne avec la probabilité 0,25, celui des colonnes la première colonne avec la probabilité 0,5. Quel est le gain espéré du joueur des lignes ?
3. Vrai ou faux : la valeur d'un jeu (en stratégies mixtes) est toujours comprise entre le maximin et le minimax en stratégies pures.
4. Vrai ou faux : dans un jeu $2 \times 2$ sans point selle, $p^\star$ est choisie pour que le joueur des lignes soit indifférent entre ses deux lignes.
5. Vrai ou faux : une stratégie strictement dominée peut recevoir une probabilité positive dans une stratégie optimale.

### M27.Q3 — Équilibres de Nash, arbres de jeu et descente-montée : unique ou non, le meilleur pour tous ou non, converger ou tourner ? 🧠 ★ ⏱️ 4 min
*Fiche §3 et §4 · parcours C, E*

1. Vrai ou faux : dans un équilibre de Nash, chaque joueur obtient le plus grand gain que le jeu peut lui donner.
2. Vrai ou faux : un jeu fini peut avoir plusieurs équilibres de Nash, de gains différents.
3. Un arbre de jeu à somme nulle : le premier joueur choisit G ou D, puis le second choisit une feuille. Après G, le gain du premier joueur vaut 3 ou 7 selon le choix du second ; après D, 5 ou 2. Quelle est la valeur du jeu ?
4. Vrai ou faux : sur $f(x, y) = xy$, la descente-montée simultanée converge vers $(0, 0)$ si le pas $\eta$ est assez petit.
5. Vrai ou faux : sur $f(x, y) = xy$, avec un pas $0 < \eta < 2$, les itérés alternés partis d'un point autre que $(0, 0)$ restent bornés mais ne convergent pas vers $(0, 0)$.

### M27.Q4 — La probabilité a posteriori et la log-loss ; Jensen-Shannon et KL quand les supports se séparent 🧠 ★ ⏱️ 5 min
*Fiche §5 et §6 · parcours C, E*

1. Une machine fabrique 20 % des pièces d'un atelier (la classe 1), une autre les 80 % restants (la classe 0). Pour la mesure $x$ d'une pièce, $p_1(x) = 0{,}5$ et $p_0(x) = 0{,}1$. Que vaut $t^\star(x)$ ?
2. Vrai ou faux : annoncer, pour chaque $x$, une probabilité plus tranchée que $t^\star(x)$ (plus près de 0 ou de 1, du même côté de ½) fait baisser la log-loss espérée.
3. Vrai ou faux : sans aucune observation, la constante qui minimise la log-loss espérée est $P(Y = 1)$.
4. Deux lois $p$ et $q$ ont des supports disjoints. Que valent $\mathrm{JS}(p, q)$, en nats puis en bits, et $\mathrm{KL}(p \,\|\, q)$ ?
5. Vrai ou faux : si l'on éloigne encore l'une de l'autre deux lois dont les supports sont déjà disjoints, JS augmente.

### M27.Q5 — Couplages et distances de Wasserstein : marges, translation, dilatation, et W₁ ≤ W₂ 🧠 ★ ⏱️ 5 min
*Fiche §7 et §8 · parcours C, E*

1. Vrai ou faux : $\boldsymbol{\Gamma} = \begin{pmatrix} 0{,}2 & 0{,}3 \\ 0{,}1 & 0{,}4 \end{pmatrix}$ est un couplage de $\mathbf{a} = (0{,}5 ;\ 0{,}5)$ et $\mathbf{b} = (0{,}4 ;\ 0{,}6)$.
2. $X$ a une loi quelconque (de moment d'ordre 2 fini) et $Y = X - 2{,}5$. Que valent $W_1$ et $W_2$ entre leurs lois ?
3. $X$ suit $\mathcal{N}(0, 2^2)$ et $Y = 3X$. Que vaut $W_2$ entre leurs lois ?
4. Vrai ou faux : $W_1 \le W_2$ pour deux lois quelconques de la droite (de moment d'ordre 2 fini).
5. Vrai ou faux : $W_1 = \lvert\mathbb{E}[X] - \mathbb{E}[Y]\rvert$ pour deux lois quelconques.

### M27.Q6 — La distance de Fréchet et son estimation : rotation commune, covariances, taille des échantillons 🧠 ★ ⏱️ 4 min
*Fiche §9 · parcours C, E*

1. Vrai ou faux : tourner deux gaussiennes par une même rotation ne change pas leur distance de Fréchet.
2. Vrai ou faux : $(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)^{1/2}$ se calcule en prenant la racine de chaque coefficient de $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2$.
3. Deux gaussiennes de $\mathbb{R}^3$ ont la même covariance et des moyennes qui diffèrent de $(2, 3, 6)$. Que vaut $W_2$ ?
4. Deux échantillons indépendants de 30 points chacun suivent une même loi de $\mathbb{R}^d$, de covariance $\boldsymbol{\Sigma}$ avec $\operatorname{tr}\boldsymbol{\Sigma} = 12$. Que vaut $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2$ ?
5. Vrai ou faux : doubler la taille des deux échantillons de la question 4 divise ce nombre par deux.

### M27.Q7 — Mesurer une dérive : PSI, KS ou W₁, leurs unités, et ce que chacun ne voit pas 🧠 ★ ⏱️ 5 min
*Fiche §10 · parcours C, E*

1. On convertit des températures de degrés Celsius en degrés Fahrenheit ($F = 1{,}8\,C + 32$) dans les deux périodes comparées. Que deviennent KS et $W_1$ ?
2. Vrai ou faux : le PSI convient à une variable sans ordre (un mode de paiement), alors que KS et $W_1$ n'y ont pas de sens.
3. Une loi vit dans $[0 ; 1]$, l'autre est sa translatée de 5. Que valent KS et $W_1$ ?
4. Deux lois vivent dans $[-5 ; 25]$, et leur KS vaut 0,15. Quelle majoration de $W_1$ en tires-tu ?
5. Vrai ou faux : si le PSI entre deux périodes d'une variable numérique, découpée en classes, est nul, la variable a la même loi dans les deux périodes.

<a id="rappels"></a>

## 🔁 Rappels

### M27.R1 — Le maximum de vraisemblance d'une loi de Bernoulli (des comptes entiers), et la log-loss quand la probabilité prédite tend vers 0 (M04, M13a) 🔁 ★ ⏱️ 8 min
*Fiche §5 · parcours C, E*

Sur $n = 50$ essais indépendants d'une même loi de Bernoulli, $k = 23$ réussissent.
1. Écris la log-vraisemblance $\ell(p) = k\ln p + (n - k)\ln(1 - p)$, et donne le $p$ qui la maximise (∂ M04.12).
2. Vrai ou faux : la constante $t$ qui minimise la log-loss moyenne de ces 50 observations est le $p$ de la question 1.
3. Un prédicteur annonce la probabilité $t = 10^{-5}$ pour une observation qui vaut 1. Que vaut sa log-loss sur cette observation ? Que devient-elle quand $t$ tend vers 0 ?
4. Ce même prédicteur a une log-loss presque nulle sur les 49 autres observations. Quelle borne inférieure peux-tu donner à sa log-loss moyenne sur les 50 ?

### M27.R2 — Les valeurs propres complexes d'une matrice réelle 2 × 2, leur module et les puissances (M22) 🔁 ★ ⏱️ 7 min
*Fiche §4 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 1 & -3 \\ 1 & 1 \end{pmatrix}$.
1. Les valeurs propres de $\mathbf{A}$ ?
2. Leur module et leur argument ?
3. Que vaut $\mathbf{A}^6$ ?
4. Vrai ou faux : $\lVert\mathbf{A}^k\mathbf{x}\rVert = 2^k\lVert\mathbf{x}\rVert$ pour tout vecteur $\mathbf{x}$ et tout entier $k$.

### M27.R3 — La racine carrée d'une matrice symétrique positive, et la trace comme somme des valeurs propres (M12c) 🔁 ★ ⏱️ 6 min
*Fiche §9 · parcours C, E*

$\mathbf{R} = \begin{pmatrix} 5 & 1 \\ 1 & 3 \end{pmatrix}$ et $\mathbf{S} = \mathbf{R}^2$.
1. Calcule $\mathbf{S}$.
2. Vrai ou faux : $\mathbf{R}$ est la racine carrée symétrique positive $\mathbf{S}^{1/2}$ de $\mathbf{S}$.
3. Que valent $\operatorname{tr}\mathbf{S}$ et la somme des valeurs propres de $\mathbf{S}$ ?
4. Que vaut $\sum_i\sqrt{\lambda_i(\mathbf{S})}$ ? Réponds sans calculer les $\lambda_i$.
5. Vrai ou faux : $\begin{pmatrix} \sqrt{26} & \sqrt{8} \\ \sqrt{8} & \sqrt{10} \end{pmatrix}$ est $\mathbf{S}^{1/2}$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- `True` ou `False` pour un vrai ou faux.

« Valeur exacte » veut dire : tous les chiffres, sans arrondir (ces calculs tombent juste). Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M27.1 — Deux enseignes se partagent un marché : réduire une matrice 3 × 4 par dominance, trouver ses deux points selles et vérifier qu'ils ont la même valeur, et ce que la réduction ne change pas (maximin, minimax) ✏️ ★ ⏱️ 30 min
**Objectif :** lire le maximin, le minimax et les points selles d'une matrice de gains, réduire le jeu par dominances successives, et justifier ce que la réduction conserve.
**Prérequis :** fiche §1 · **Parcours :** C, E

Deux enseignes, A et B, se partagent les clients d'une ville. Pour la saison, A choisit une stratégie parmi A1 (des promotions), A2 (une carte de fidélité) et A3 (de la publicité locale) ; B, parmi B1 (des prix bas), B2 (la livraison gratuite), B3 (des horaires étendus) et B4 (des bons d'achat). Chacune choisit sans connaître le choix de l'autre. Une étude estime, pour chaque paire, le nombre de points de part de marché que A prend à B (ce que B perd) :

| | B1 | B2 | B3 | B4 |
|---|---|---|---|---|
| **A1** | 5 | 2 | 6 | 1 |
| **A2** | 4 | 3 | 7 | 3 |
| **A3** | 0 | 1 | 4 | 0 |

| | Question | Réponse attendue |
|---|---|---|
| a | le maximin et le minimax de $\mathbf{G}$ | une liste de 2 nombres |
| b | les points selles, chacun écrit (ligne, colonne) avec des numéros à partir de 1, dans l'ordre des lignes puis des colonnes | une liste de paires, comme `[[1, 2], [3, 1]]` |
| c | vrai ou faux : dans $\mathbf{G}$, la colonne B1 est strictement dominée | `True` ou `False` |
| d | la matrice qui reste quand on a rayé, l'une après l'autre, toutes les stratégies strictement dominées | une matrice |

Dans ta copie : écris les minimums des lignes et les maximums des colonnes ; donne l'ordre des éliminations, en disant chaque fois par quelle stratégie la ligne ou la colonne rayée est dominée ; justifie, pour une matrice quelconque, que rayer une ligne strictement dominée ne change ni le maximin ni le minimax, puis de même pour une colonne ; vérifie que les deux points selles ont la même valeur.

### Ex M27.2 — Tirs au but : la probabilité de tirer à gauche par indifférence, la réponse du gardien et la valeur du jeu ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer les stratégies optimales et la valeur d'un jeu $2 \times 2$ sans point selle, puis ce que rapporte une stratégie qui s'en écarte.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

À chaque tir au but, le tireur tire à gauche ou à droite (vu du gardien), et le gardien plonge à gauche ou à droite, en même temps. Les statistiques de l'équipe donnent la probabilité de marquer, en %, pour chaque paire :

| | gardien à gauche | gardien à droite |
|---|---|---|
| **tir à gauche** | 55 | 95 |
| **tir à droite** | 85 | 60 |

Le tireur maximise, le gardien minimise ; $p$ est la probabilité de tirer à gauche, $q$ celle de plonger à gauche.

| | Question | Réponse attendue |
|---|---|---|
| a | $p^\star$, la probabilité optimale de tirer à gauche | une fraction irréductible, entre guillemets |
| b | $q^\star$, la probabilité optimale de plonger à gauche | une fraction irréductible, entre guillemets |
| c | la valeur du jeu (en %) | un nombre (2 décimales) |
| d | le gardien plonge à gauche avec la probabilité 0,65 : la probabilité de marquer du meilleur tir pur contre lui (en %) | un nombre (2 décimales) |
| e | ce que s'assure un tireur qui tire à gauche avec la probabilité 0,55, quoi que fasse le gardien (en %) | un nombre (2 décimales) |

Dans ta copie : vérifie qu'il n'y a pas de point selle ; écris, en fonction de $p$, les deux droites que le tireur obtient contre chaque plongeon, et dessine leur minimum ; dis quel tir pur est le meilleur en d), et retrouve d) par l'identité $E(p, q) = v + \kappa\,(p - p^\star)(q - q^\star)$.

### Ex M27.3 — Les équilibres de Nash d'un dilemme du prisonnier et d'un jeu de coordination (purs et mixte), puis la valeur d'un jeu d'allumettes par induction arrière ✏️ ★★ ⏱️ 30 min
**Objectif :** trouver les équilibres de Nash de deux jeux à somme non nulle, dont un équilibre mixte asymétrique, et résoudre un petit jeu par induction arrière.
**Prérequis :** fiche §3 · **Parcours :** C, E

1. **Le dilemme.** Deux boulangeries voisines choisissent chaque semaine de maintenir leurs prix (M) ou de les baisser (B). Leurs bénéfices, en centaines d'euros, le premier nombre pour la boulangerie des lignes : (M, M) donne $(7, 7)$, (M, B) donne $(1, 10)$, (B, M) donne $(10, 1)$, (B, B) donne $(2, 2)$.
2. **La coordination.** Deux équipes d'une entreprise choisissent chacune, de son côté, un logiciel de gestion de projet, X ou Y. Si elles ne prennent pas le même, rien ne marche : chacune gagne 0. L'équipe des lignes préfère X : elle gagne 5 si les deux prennent X, et 3 si les deux prennent Y ; l'équipe des colonnes préfère Y : elle gagne 3 avec X, et 4 avec Y.
3. **Les allumettes.** Des allumettes sont sur la table ; chacun à son tour en retire 1 ou 2 ; celui qui prend la dernière **perd**.

| | Question | Réponse attendue |
|---|---|---|
| a | le dilemme : les gains (boulangerie des lignes, boulangerie des colonnes) à son équilibre de Nash | une liste de 2 nombres |
| b | le dilemme : vrai ou faux, (M, M) est un équilibre de Nash | `True` ou `False` |
| c | la coordination : $x$, la probabilité que l'équipe des lignes choisisse X dans l'équilibre mixte | une fraction irréductible, entre guillemets |
| d | la coordination : $y$, la probabilité que l'équipe des colonnes choisisse X dans l'équilibre mixte | une fraction irréductible, entre guillemets |
| e | la coordination : les gains moyens (lignes, colonnes) dans l'équilibre mixte | une liste de 2 nombres (3 décimales) |
| f | les allumettes : les nombres d'allumettes de 1 à 12 qui sont des positions perdantes pour le joueur qui doit jouer | une liste d'entiers, dans l'ordre croissant |
| g | les allumettes : avec 11 allumettes, le nombre que le premier joueur doit retirer pour être sûr de gagner | un entier |

Dans ta copie : montre que B domine strictement M pour chaque boulangerie ; écris les deux équilibres purs de la coordination, puis, pour l'équilibre mixte, la probabilité que les deux équipes tombent d'accord, et compare les gains moyens à ceux des deux équilibres purs ; pour les allumettes, fais l'induction arrière de 1 à 12 (perdante ou gagnante, pour le joueur qui doit jouer ; avec 1 allumette, il doit prendre la dernière), et énonce la règle qui apparaît.

### Ex M27.4 — Descente-montée sur f(x, y) = xy : la matrice d'un pas simultané puis alterné, leurs valeurs propres et leurs modules, et deux pas différents pour x et y ✏️ ★★ ⏱️ 30 min
**Objectif :** prévoir par les valeurs propres d'un pas ce que fait la descente-montée sur $xy$, et montrer que des pas différents pour les deux joueurs n'y changent rien d'essentiel.
**Prérequis :** fiche §4 ; M22 · **Parcours :** C, E

On joue la descente-montée sur $f(x, y) = xy$ : le joueur $x$ minimise, le joueur $y$ maximise, comme dans la fiche ; les itérés partent d'un point autre que $(0, 0)$. Avec deux pas, $a > 0$ pour $x$ et $b > 0$ pour $y$, le pas simultané est $x_{k+1} = x_k - a\,y_k$, $y_{k+1} = y_k + b\,x_k$, et le pas alterné $x_{k+1} = x_k - a\,y_k$, $y_{k+1} = y_k + b\,x_{k+1}$ ; la fiche est le cas $a = b = \eta$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\eta = 0{,}6$, pas simultané : le module des valeurs propres de $\mathbf{M}_s$ | un nombre (4 décimales) |
| b | $\eta = 0{,}6$ : l'angle dont un pas simultané fait tourner le vecteur $(x, y)$, en degrés | un nombre (1 décimale) |
| c | $\eta = 0{,}6$ : le plus petit nombre de pas simultanés après lequel la distance à l'équilibre a au moins doublé | un entier |
| d | $\eta = 0{,}6$, pas alterné : l'argument des valeurs propres de $\mathbf{M}_a$, en degrés (en moyenne, l'angle dont les itérés tournent autour de l'équilibre à chaque pas) | un nombre (1 décimale) |
| e | $a = 1{,}5$ et $b = 0{,}6$ : le module des valeurs propres du pas simultané, puis celui des valeurs propres du pas alterné | une liste de 2 nombres (4 décimales) |
| f | $a = 4$ et $b = 1{,}5$, pas alterné : le rayon spectral (la plus grande valeur absolue d'une valeur propre) | un nombre (2 décimales) |

Dans ta copie : écris $\mathbf{M}_s$ et $\mathbf{M}_a$ pour $\eta = 0{,}6$ ; pour deux pas $a$ et $b$, écris les matrices d'un pas simultané et d'un pas alterné, et montre que leurs déterminants valent $1 + ab$ et $1$, et que la trace du pas alterné vaut $2 - ab$ ; conclus que des pas différents ne font jamais converger le pas simultané, et que le pas alterné reste borné quand $ab < 4$ et ne l'est plus quand $ab > 4$ (sauf pour un départ sur la droite propre de la valeur propre de valeur absolue $< 1$).

### Ex M27.5 — Deux fournisseurs et un défaut noté sur quatre niveaux : la probabilité a posteriori, et la log-loss moyenne de trois prédicteurs (a priori, a posteriori, trop sûr de lui) ✏️ ★★ ⏱️ 35 min
**Objectif :** calculer une probabilité a posteriori à priors inégaux, et comparer par leur log-loss espérée trois façons de prédire.
**Prérequis :** fiche §5 ; M04, M13a · **Parcours :** C, E

Une usine achète une même pièce à deux fournisseurs : A en livre 68 %, B 32 %. Un contrôle note chaque pièce sur une échelle de défauts de 0 (aucun) à 3 (grave). Chez A, les niveaux 0, 1, 2 et 3 ont les probabilités 0,45, 0,30, 0,20 et 0,05 ; chez B, 0,05, 0,20, 0,30 et 0,45. D'après le niveau $X$ d'une pièce, on veut prédire la probabilité $t(X)$ qu'elle vienne de B ($Y = 1$), et l'on juge un prédicteur par sa log-loss espérée $R(t) = \mathbb{E}\big[\ell(t(X), Y)\big]$, en nats, la moyenne sur le couple $(X, Y)$. Trois prédicteurs : le prédicteur **a priori**, qui annonce 0,32 quel que soit le niveau ; la probabilité **a posteriori** $t^\star(x)$ ; un prédicteur **trop sûr de lui**, qui annonce 0,02, 0,08, 0,15 et 0,96 pour les niveaux 0, 1, 2 et 3.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X = 0)$, la probabilité qu'une pièce n'ait aucun défaut | un nombre (3 décimales) |
| b | $t^\star(x)$ pour $x = 0, 1, 2, 3$ | une liste de 4 nombres (3 décimales) |
| c | la log-loss espérée du prédicteur a priori (nats) | un nombre (4 décimales) |
| d | la log-loss espérée de $t^\star$ (nats) | un nombre (4 décimales) |
| e | la log-loss espérée du prédicteur trop sûr de lui (nats) | un nombre (4 décimales) |

Dans ta copie : le tableau des probabilités jointes $P(X = x, Y = y)$ ; vérifie que le prédicteur trop sûr de lui est, à chaque niveau, plus loin de ½ que $t^\star$, et du même côté ; range les trois log-loss, et dis ce que montre ce classement.

### Ex M27.6 — Deux lois uniformes de même largeur, translatées : JS en fonction du décalage, la KL, et ce que le décalage lui-même mesure ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer JS entre deux lois continues qui se recouvrent en partie, voir sa pente disparaître quand elles se séparent, et la comparer à $W_1$.
**Prérequis :** fiche §6 et §8 (« Une translation ») ; M06, M25a · **Parcours :** C, E

Un bus passe à un arrêt à une heure uniforme dans une fenêtre de 5 minutes : la loi $p$ de son heure de passage, en minutes après 8 h, est $\mathcal{U}([0 ; 5])$. Après un changement d'horaire, elle devient $q = \mathcal{U}([\theta ; \theta + 5])$ : la même fenêtre, décalée de $\theta > 0$ minutes.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathrm{JS}(p, q)$ pour $\theta = 1$ (nats) | un nombre (3 décimales) |
| b | $\mathrm{JS}(p, q)$ pour $\theta = 3$ (nats) | un nombre (3 décimales) |
| c | $\mathrm{JS}(p, q)$ pour $\theta = 8$, puis pour $\theta = 80$ (nats) | une liste de 2 nombres (3 décimales) |
| d | vrai ou faux : $\mathrm{KL}(p \,\|\, q)$ est finie pour $\theta = 1$ | `True` ou `False` |
| e | $W_1(p, q)$ pour $\theta = 8$, puis pour $\theta = 80$ (minutes) | une liste de 2 nombres |

Dans ta copie : pour $0 < \theta < 5$, découpe l'axe en trois morceaux, écris $m = \frac{p + q}{2}$ sur chacun, calcule $\mathrm{KL}(p \,\|\, m)$ et $\mathrm{KL}(q \,\|\, m)$, et déduis-en $\mathrm{JS}$ en fonction de $\theta$ ; fais de même pour $\theta \ge 5$ ; trace $\mathrm{JS}$ et $W_1$ en fonction de $\theta$ sur $[0 ; 12]$, et dis ce que le décalage lui-même mesure.

### Ex M27.7 — Trois dépôts et trois magasins le long d'une route : vérifier des couplages, leur coût, le couplage indépendant et le plan monotone (coin nord-ouest) ✏️ ★★ ⏱️ 30 min
**Objectif :** reconnaître un plan de transport par ses marges, calculer son coût, et construire le plan monotone par la règle du coin nord-ouest.
**Prérequis :** fiche §7 et §8 · **Parcours :** C, E

Le long d'une route, trois dépôts stockent un engrais : aux kilomètres 1, 4 et 6, avec 20, 50 et 30 tonnes. Trois magasins en commandent : aux kilomètres 2, 3 et 8, 40, 35 et 25 tonnes. Transporter une tonne sur un kilomètre coûte 1 : le coût d'un plan est en t·km. Un plan $\boldsymbol{\Gamma} = (\gamma_{ij})$ donne les tonnes envoyées du dépôt $i$ (ligne) au magasin $j$ (colonne). Deux plans proposés :
$$\boldsymbol{\Gamma}_2 = \begin{pmatrix} 10 & 10 & 0 \\ 30 & 20 & 0 \\ 0 & 5 & 25 \end{pmatrix}, \qquad \boldsymbol{\Gamma}_3 = \begin{pmatrix} 0 & 20 & 0 \\ 40 & 10 & 0 \\ 0 & 0 & 30 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | vrai ou faux : $\boldsymbol{\Gamma}_3$ est un plan de transport | `True` ou `False` |
| b | le coût de $\boldsymbol{\Gamma}_2$ (t·km) | un nombre |
| c | le coût du couplage indépendant, où chaque dépôt répartit son stock entre les magasins au prorata de leurs commandes (t·km) | un nombre |
| d | le plan du coin nord-ouest | une matrice $3 \times 3$ |
| e | $W_1$ entre la loi des stocks et celle des commandes, chacune ramenée à une masse totale de 1 (km) | un nombre (2 décimales) |

Dans ta copie : la matrice des distances $\lvert x_i - y_j\rvert$ ; la marge que $\boldsymbol{\Gamma}_3$ ne respecte pas ; la matrice du couplage indépendant ; les étapes du coin nord-ouest ; vérifie e) par l'aire entre les fonctions de répartition des deux lois (fiche §8).

### Ex M27.8 — W₁ et W₂ par l'aire entre les fonctions de répartition et par les quantiles : deux lois uniformes, puis W₂ de deux gaussiennes (et W₁ quand elles ont le même écart-type) ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer $W_1$ de deux façons et $W_2$ par les quantiles, sur deux lois uniformes, puis appliquer la formule de deux gaussiennes.
**Prérequis :** fiche §8 ; M02a · **Parcours :** C, E

Deux machines coupent des barres. L'excès de longueur d'une barre, en mm, suit $\mathcal{U}([0 ; 4])$ pour la première machine et $\mathcal{U}([1 ; 2])$ pour la seconde. Sur une ligne d'ensachage, l'excès de masse d'un sachet, en grammes au-dessus des 500 g annoncés, suit $\mathcal{N}(20 ;\ 1{,}5^2)$ avant un réglage et $\mathcal{N}(21{,}2 ;\ 1^2)$ après ; sur une seconde ligne, il suit $\mathcal{N}(20 ;\ 1{,}5^2)$ puis $\mathcal{N}(21{,}2 ;\ 1{,}5^2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $W_1$ entre les deux lois uniformes (mm) | une fraction irréductible, entre guillemets |
| b | $W_2$ entre les deux lois uniformes (mm) | un nombre (4 décimales) |
| c | $W_2$ entre $\mathcal{N}(20 ;\ 1{,}5^2)$ et $\mathcal{N}(21{,}2 ;\ 1^2)$ (g) | un nombre (4 décimales) |
| d | $W_1$ entre $\mathcal{N}(20 ;\ 1{,}5^2)$ et $\mathcal{N}(21{,}2 ;\ 1{,}5^2)$ (g) | un nombre (4 décimales) |

Dans ta copie : $F$ et $G$, et l'aire entre elles, morceau par morceau (le signe de $F - G$ change une fois) ; $F^{-1}$ et $G^{-1}$, puis $\int_0^1\lvert F^{-1} - G^{-1}\rvert$, qui doit redonner a) ; vérifie $W_1 \le W_2$, et compare $W_1$ à l'écart des moyennes ; pour d), dis pourquoi $W_1$ et $W_2$ y sont égaux.

### Ex M27.9 — La distance de Fréchet de deux gaussiennes du plan à covariances diagonales, puis tournées ensemble : la part des moyennes et celle des covariances ✏️ ★★ ⏱️ 30 min
**Objectif :** reconnaître deux covariances diagonales dans une même base tournée, et calculer leur distance de Fréchet par la formule et par le cas commutatif.
**Prérequis :** fiche §9 ; M12c · **Parcours :** C, E

Deux perceuses percent des trous dans des plaques. La position d'un trou, en centièmes de millimètre par rapport à la cote, suit $\mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)$ pour la première perceuse et $\mathcal{N}(\boldsymbol{\mu}_2, \boldsymbol{\Sigma}_2)$ pour la seconde, avec
$$\boldsymbol{\Sigma}_1 = \begin{pmatrix} 52 & 36 \\ 36 & 73 \end{pmatrix}, \qquad \boldsymbol{\Sigma}_2 = \begin{pmatrix} 145 & 60 \\ 60 & 180 \end{pmatrix}, \qquad \boldsymbol{\mu}_1 = (0, 0), \qquad \boldsymbol{\mu}_2 = (5, -2).$$

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\boldsymbol{\Sigma}_1$, puis celles de $\boldsymbol{\Sigma}_2$, chacune dans l'ordre décroissant | une liste de 2 listes de 2 nombres |
| b | $\sum_i\sqrt{\lambda_i(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)}$ | un nombre |
| c | la part des covariances dans $W_2^2$, $\operatorname{tr}\boldsymbol{\Sigma}_1 + \operatorname{tr}\boldsymbol{\Sigma}_2 - 2\sum_i\sqrt{\lambda_i(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)}$ | un nombre |
| d | la part des moyennes dans $W_2^2$ | un nombre |
| e | la distance de Fréchet $W_2$ (centièmes de mm) | un nombre (2 décimales) |

Dans ta copie : un vecteur propre pour chaque valeur propre ; vérifie que $\boldsymbol{\Sigma}_1$ et $\boldsymbol{\Sigma}_2$ ont les mêmes vecteurs propres, et donne les écarts-types de chaque loi le long de ces deux axes ; montre que $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2 = \boldsymbol{\Sigma}_2\boldsymbol{\Sigma}_1$ ; retrouve c) par la formule du cas commutatif ; écris $\boldsymbol{\Sigma}_1$ et $\boldsymbol{\Sigma}_2$ après la rotation qui amène le premier vecteur propre sur l'axe des abscisses, et dis ce que devient $W_2$.

### Ex M27.10 — Une dérive en deux mois d'une variable à trois catégories : la divergence de Jeffreys (le PSI) et JS, puis l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage ; enfin KS et W₁ entre deux petits échantillons de températures de même taille ✏️ ★★ ⏱️ 30 min
**Objectif :** mesurer une dérive d'une variable à catégories par le PSI, JS et leur approximation, puis celle d'une variable numérique par KS et $W_1$, avec leurs unités.
**Prérequis :** fiche §6, §8 et §10 ; M05a · **Parcours :** C, E

Un site de vente propose trois modes de livraison : à domicile, en point relais, en magasin. En mars (la référence), les commandes se répartissaient en $q = (0{,}62 ;\ 0{,}26 ;\ 0{,}12)$ ; en avril, en $p = (0{,}55 ;\ 0{,}29 ;\ 0{,}16)$. Par ailleurs, un capteur de température extérieure a donné, à cinq jours tirés au hasard en janvier, 0,7 ; −1,5 ; 3,6 ; −0,2 ; 3,2 °C, et à cinq jours de février, 2,3 ; 4,1 ; 1,2 ; 2,8 ; 1,9 °C.

| | Question | Réponse attendue |
|---|---|---|
| a | la divergence de Jeffreys (le PSI) entre mars et avril (nats) | un nombre (4 décimales) |
| b | $\mathrm{JS}(p, q)$ (nats) | un nombre (5 décimales) |
| c | l'approximation $\sum_k(p_k - q_k)^2/q_k$ | un nombre (4 décimales) |
| d | KS entre les deux échantillons de températures | un nombre (2 décimales) |
| e | $W_1$ entre les deux échantillons (°C) | un nombre (2 décimales) |

Dans ta copie : dis pourquoi KS et $W_1$ n'auraient pas de sens pour le mode de livraison ; dessine les deux fonctions de répartition empiriques sur un même graphique et marque l'endroit où leur écart est le plus grand ; écris l'appariement trié qui donne $W_1$ ; vérifie $W_1 \le (b - a)\,\mathrm{KS}$, avec $[a ; b]$ le plus petit intervalle qui contient les dix valeurs ; dis pourquoi $W_1$ dépasse ici l'écart des moyennes.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M27.11 — Le maximin est au plus le minimax ; ils sont égaux si et seulement si le jeu a un point selle, et deux points selles ont la même valeur ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer les propriétés du §1 pour une matrice de gains quelconque.
**Prérequis :** fiche §1 · **Parcours :** C, E

$\mathbf{G}$ est une matrice $m \times n$ quelconque ; $i_0$ est une ligne où le maximin est atteint ($\min_j g_{i_0j} = \max_i\min_j g_{ij}$) et $j_0$ une colonne où le minimax est atteint.
1. Montre que $\max_i\min_j g_{ij} \le g_{i_0j_0} \le \min_j\max_i g_{ij}$.
2. On suppose que $(i, j)$ est un point selle. Montre que le maximin est au moins $g_{ij}$ et que le minimax est au plus $g_{ij}$ ; déduis-en que maximin $=$ minimax $= g_{ij}$.
3. Réciproquement, on suppose maximin $=$ minimax. Montre que $(i_0, j_0)$ est un point selle.
4. Soit $(i, j)$ et $(k, l)$ deux points selles. Montre que $g_{ij} = g_{kl}$, puis que $(i, l)$ et $(k, j)$ sont aussi des points selles.

### Ex M27.12 — La log-loss espérée est minimale pour la probabilité a posteriori : une preuve par l'inégalité de Gibbs ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer le théorème du §5, sans aucune dérivée, en écrivant l'écart à l'optimum comme une moyenne de divergences KL.
**Prérequis :** fiche §5 ; M04, M06 · **Parcours :** C, E

$Y$ vaut 1 avec la probabilité $\pi_1 \in\ ]0, 1[$ et 0 avec $\pi_0 = 1 - \pi_1$ ; sachant $Y = k$, l'observation $X$ suit une loi discrète $p_k$ sur un ensemble fini, avec $p_0(x) > 0$ et $p_1(x) > 0$ pour chaque valeur $x$. Un prédicteur est une fonction $t$ à valeurs dans $]0, 1[$, et $R(t) = \mathbb{E}\big[\ell(t(X), Y)\big]$, avec $\ell(t, y) = -\big[y\ln t + (1 - y)\ln(1 - t)\big]$. Pour $a, b \in\ ]0, 1[$, on note $\mathrm{KL}(a \,\|\, b) = a\ln\frac{a}{b} + (1 - a)\ln\frac{1 - a}{1 - b}$ la divergence KL entre les lois de Bernoulli de paramètres $a$ et $b$.
1. Montre que $P(Y = 1 \mid X = x) = t^\star(x) = \frac{\pi_1p_1(x)}{\pi_1p_1(x) + \pi_0p_0(x)}$, puis, en conditionnant sur $X$, que $R(t) = \sum_xP(X = x)\big[-t^\star(x)\ln t(x) - (1 - t^\star(x))\ln(1 - t(x))\big]$.
2. Montre que $R(t) - R(t^\star) = \sum_xP(X = x)\,\mathrm{KL}\big(t^\star(x) \,\|\, t(x)\big)$.
3. Conclus avec l'inégalité de Gibbs (M06) : $R(t) \ge R(t^\star)$, avec égalité si et seulement si $t(x) = t^\star(x)$ pour chaque valeur $x$.
4. Un prédicteur sans observation est une constante $t$. Montre que la meilleure constante est $\pi_1$.

### Ex M27.13 — 0 ≤ JS ≤ ln 2, et JS = ln 2 si et seulement si les deux lois ont des supports disjoints ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer les bornes de Jensen-Shannon et caractériser le cas où elle atteint $\ln 2$.
**Prérequis :** fiche §6 ; M06 · **Parcours :** C

$p$ et $q$ sont deux lois sur un ensemble fini, $m = \frac{p + q}{2}$, $\mathrm{JS}(p, q) = \frac12\mathrm{KL}(p \,\|\, m) + \frac12\mathrm{KL}(q \,\|\, m)$, avec la convention $0\ln 0 = 0$ (et $0 \ln\frac{0}{0} = 0$).
1. Montre que $\mathrm{JS}(p, q)$ est toujours finie, alors que $\mathrm{KL}(p \,\|\, q)$ peut être infinie (donne un exemple).
2. Montre que $\mathrm{JS}(p, q) \ge 0$, avec égalité si et seulement si $p = q$.
3. Montre que $\mathrm{KL}(p \,\|\, m) \le \ln 2$, avec égalité si et seulement si $q_k = 0$ pour tout $k$ tel que $p_k > 0$.
4. Conclus : $\mathrm{JS}(p, q) \le \ln 2$, avec égalité si et seulement si $p$ et $q$ ont des supports disjoints (démontre les deux sens).

### Ex M27.14 — L'appariement trié est optimal : un argument d'échange sur deux paires, puis sur n paires, pour les coûts |x − y| et (x − y)² ∂ ★★ ⏱️ 40 min
**Objectif :** démontrer par un argument d'échange que trier les deux échantillons, puis apparier dans l'ordre, minimise le coût de transport sur la droite.
**Prérequis :** fiche §8 ; R4 (récurrence) · **Parcours :** C

1. Soit $x_1 \le x_2$ et $y_1 \le y_2$. Montre que $(x_1 - y_1)^2 + (x_2 - y_2)^2 \le (x_1 - y_2)^2 + (x_2 - y_1)^2$ (développe la différence).
2. Avec les mêmes hypothèses, montre que $\lvert x_1 - y_1\rvert + \lvert x_2 - y_2\rvert \le \lvert x_1 - y_2\rvert + \lvert x_2 - y_1\rvert$.
3. Soit $x_1 < \cdots < x_n$ et $y_1 < \cdots < y_n$, et $\sigma$ une permutation de $\{1, \ldots, n\}$ ; on appelle **croisement** une paire $i < j$ avec $\sigma(i) > \sigma(j)$. Montre qu'échanger $\sigma(i)$ et $\sigma(j)$ pour un croisement n'augmente ni $\sum_k\lvert x_k - y_{\sigma(k)}\rvert$ ni $\sum_k(x_k - y_{\sigma(k)})^2$, et diminue le nombre de croisements. Conclus : l'appariement trié ($\sigma$ l'identité) minimise les deux coûts.
4. Trouve $x_1 < x_2$ et $y_1 < y_2$ pour lesquels l'appariement croisé coûte autant que l'appariement trié pour le coût $\lvert x - y\rvert$. Montre que, pour le coût $(x - y)^2$, l'appariement trié est strictement meilleur dès que $x_1 < x_2$ et $y_1 < y_2$.

### Ex M27.15 — E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ : une distance estimée sur deux échantillons est biaisée vers le haut ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer la formule du biais du §9 et en tirer une correction.
**Prérequis :** fiche §9 ; M02c · **Parcours :** C, E

$\mathbf{x}_1, \ldots, \mathbf{x}_{n_1}$ sont indépendants, de même loi, de moyenne $\boldsymbol{\mu}_1$ et de covariance $\boldsymbol{\Sigma}_1$ dans $\mathbb{R}^d$ ; $\mathbf{y}_1, \ldots, \mathbf{y}_{n_2}$ sont indépendants entre eux et des $\mathbf{x}_i$, de moyenne $\boldsymbol{\mu}_2$ et de covariance $\boldsymbol{\Sigma}_2$ ; $\bar{\mathbf{x}}_1$ et $\bar{\mathbf{x}}_2$ sont les deux moyennes empiriques.
1. Pour un vecteur aléatoire $\mathbf{v}$ de moyenne $\mathbf{m}$ et de covariance $\mathbf{C}$, montre que $\mathbb{E}\lVert\mathbf{v}\rVert^2 = \lVert\mathbf{m}\rVert^2 + \operatorname{tr}\mathbf{C}$.
2. Montre que $\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2$ a pour moyenne $\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2$ et pour covariance $\frac{\boldsymbol{\Sigma}_1}{n_1} + \frac{\boldsymbol{\Sigma}_2}{n_2}$ ; dis où servent les deux indépendances.
3. Conclus, et explique pourquoi la distance estimée $\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2$ est biaisée vers le haut.
4. On suppose $\operatorname{tr}\boldsymbol{\Sigma}_1$ et $\operatorname{tr}\boldsymbol{\Sigma}_2$ connues. Propose un estimateur sans biais de $\lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2$. Peut-il être négatif ? Pourquoi deux distances estimées ne se comparent-elles qu'à tailles égales ?

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M27.16 — Pont : la distance de Fréchet en dimension 1, W₂² = (Δμ)² + (Δσ)², entre deux lois résumées par leur moyenne et leur écart-type (deux séries d'une machine, avant et après réglage) : la part de la moyenne et celle de l'écart-type, et pourquoi workbookIA 27 l'écrit avec des covariances et en rend le carré 🔗 ★ ⏱️ 20 min
**Objectif :** passer de la distance $W_2$ de la fiche à la convention des bibliothèques (des matrices de covariance, et un carré), et lire la part de chaque paramètre.
**Prérequis :** fiche §8 et §9 · **Parcours :** C, E

Une machine tourne des axes. Avant un réglage, le diamètre d'un axe suit $\mathcal{N}(50{,}30 ;\ 0{,}12^2)$, en mm ; après, $\mathcal{N}(50{,}02 ;\ 0{,}05^2)$. Au chapitre 27 de workbookIA, la distance de Fréchet entre deux gaussiennes se calcule à partir des moyennes et des **matrices de covariance**, et la fonction rend son **carré** ; en dimension 1, une matrice de covariance est la matrice $1 \times 1$ $[[\sigma^2]]$.

| | Question | Réponse attendue |
|---|---|---|
| a | $W_2^2$ entre les deux lois (mm², valeur exacte) | un nombre |
| b | $W_2$ (mm) | un nombre (4 décimales) |
| c | la part de la moyenne dans $W_2^2$ (en %) | un nombre (1 décimale) |
| d | le terme $\operatorname{tr}\big(\boldsymbol{\Sigma}_1 + \boldsymbol{\Sigma}_2 - 2(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)^{1/2}\big)$, avec les matrices $1 \times 1$ de covariance (mm², valeur exacte) | un nombre |
| e | ce que rend une fonction qui attend les moyennes et les matrices de covariance quand on lui passe les bonnes moyennes, mais, par erreur, les écarts-types $[[0{,}12]]$ et $[[0{,}05]]$ à la place des covariances (« mm² ») | un nombre (4 décimales) |

Dans ta copie : vérifie que d) est la part de l'écart-type, $(\sigma_1 - \sigma_2)^2$ ; dis ce que le réglage a surtout corrigé ; explique pourquoi on compare une tolérance en mm à $W_2$, et pas à $W_2^2$ ; dis enfin ce qu'il faut regarder avant d'appeler une fonction de distance d'une bibliothèque (ce qu'elle prend, ce qu'elle rend).

### Ex M27.17 — MML §7.2 relu : l'inégalité minimax (7.23) et sa preuve, la dualité faible (7.27) lue comme un jeu, et l'inégalité vérifiée sur une matrice de gains choisie 📖 ★★ ⏱️ 35 min
**Objectif :** relire en anglais l'inégalité minimax et la dualité faible de MML, en pensant aux jeux du §1, et les vérifier sur tes propres nombres.
**Prérequis :** fiche §1 ; M13b · **Parcours :** C

Relis MML §7.2, en suivant le guide de lecture de la fiche : la remarque qui suit la Définition 7.1, puis (7.25) à (7.27). Réponds dans ta copie, en français, avec tes mots (ne recopie pas le livre).
1. Dans (7.23), quelle variable minimise, laquelle maximise ? Réécris (7.23) pour une matrice de gains $\mathbf{G}$ avec les conventions de la fiche (le joueur des lignes maximise), en disant à quoi correspondent $\mathbf{x}$ et $\mathbf{y}$.
2. (7.24) est écrite « pour tous $\mathbf{x}, \mathbf{y}$ » : de quelle variable dépend chacun de ses deux membres ? Refais les deux étapes de la preuve du livre pour une matrice : l'inégalité de départ pour une ligne $i$ et une colonne $j$, puis le passage au maximum d'un côté et au minimum de l'autre. Pourquoi chaque passage garde-t-il l'inégalité ?
3. Choisis une matrice de gains $2 \times 3$ sans point selle (ni celles de la fiche, ni celles des exercices) : vérifie l'inégalité de départ de la question 2 pour ses six cases, puis que son maximin est strictement inférieur à son minimax.
4. Le livre part de (7.26) et en tire (7.27). On veut minimiser $f(x) = (x - 2)^2$ sous la contrainte $x \le -1$. Écris le lagrangien. Si $x$ annonce d'abord, que vaut $\max_{\lambda \ge 0}\mathcal{L}(x, \lambda)$ pour $x = -2$, puis pour $x = 0$ ? Si $\lambda$ annonce d'abord, calcule $D(\lambda) = \min_x\mathcal{L}(x, \lambda)$ et son maximum sur $\lambda \ge 0$. Compare au minimum de $f$ sous la contrainte, et dis quel joueur annonce en second dans chacun des deux problèmes.
5. Relève quatre expressions anglaises du passage et leur traduction dans la fiche.

### Ex M27.18 — Expliquer avec une partie de cache-cache pourquoi jouer au hasard peut être la meilleure stratégie, et ce que le hasard garantit 🗣️ ★ ⏱️ 15 min
**Objectif :** expliquer sans formule l'idée d'une stratégie mixte, de l'indifférence et de la garantie qu'elle donne.
**Prérequis :** fiche §2 · **Parcours :** C, E

Une amie joue souvent à cache-cache avec son neveu, dans une maison qui n'a que deux bonnes cachettes : le grenier, plus sûr, et la cave, plus proche. Elle te demande pourquoi on dit que « le mieux est de tirer sa cachette au hasard ».

Réponds-lui en 6 à 10 phrases, sans formule : ce qui arrive à qui se cache toujours au même endroit ; pourquoi le hasard empêche le chercheur d'en profiter ; pourquoi les deux cachettes ne doivent pas forcément être tirées à pile ou face ; à quel dosage le chercheur n'a plus de préférence ; ce que ce dosage garantit (en moyenne, quoi que fasse le chercheur), et ce qu'il ne garantit pas (une partie donnée). Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M27.E1 — « Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se recouvrent pas, et pas Jensen-Shannon ? » 💼 ★ ⏱️ 10 min
*Fiche §6 et §8 · parcours C, E*

« Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se recouvrent pas, et pas Jensen-Shannon ? »

Ta réponse doit dire ce que vaut JS pour deux lois de supports disjoints ($\ln 2$, quelle que soit leur distance), ce que cela fait à qui ajuste un paramètre en suivant sa pente, ce que fait la KL (infinie), ce que mesure $W_1$ (le coût d'un transport : $\lvert\theta\rvert$ pour une translation, une pente de 1), l'exemple de deux masses ponctuelles, et une limite de $W_1$ (un programme linéaire en dimension $d \ge 2$, une estimation sur des échantillons).

### M27.E2 — « Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et comment comparer deux mesures ? » 💼 ★ ⏱️ 10 min
*Fiche §9 et §10 · parcours C*

« Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et comment comparer deux mesures ? »

Ta réponse doit dire d'où vient la distance non nulle (le hasard de l'échantillonnage), de combien elle est biaisée pour une distance entre moyennes ($\operatorname{tr}\boldsymbol{\Sigma}\,(\frac{1}{n_1} + \frac{1}{n_2})$), pourquoi deux distances estimées ne se comparent qu'à tailles égales, une façon de s'en sortir quand les tailles diffèrent (retirer une estimation du biais), et quel outil donne une p-valeur (un test, comme celui de Kolmogorov-Smirnov ou un test par permutation, M08).

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m27_jeux_distances/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M27.19 | Les valeurs d'un jeu en stratégies pures : maximin, minimax et coups prudents, points selles compris · `pure_strategy_values` | 🔨 | ★ | 15 | C, E |
| M27.20 | Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle · `mixed_strategy_value_2x2` | 🔨 | ★★ | 20 | C, E |
| M27.21 | Les itérés de la descente-montée simultanée ou alternée sur un jeu bilinéaire xᵀAy · `descent_ascent_iterates` | 🔨 | ★★ | 20 | C |
| M27.22 | W₂ de deux gaussiennes en dimension 1, à partir des moyennes et des écarts-types · `w2_gaussians_1d` | 🔨 | ★ | 10 | C, E |
| M27.23 | `scipy.optimize.linprog` : le transport optimal entre deux lois discrètes de la droite comme programme linéaire, comparé au plan monotone et à l'aire entre les fonctions de répartition | 📦 | ★★ | 25 | C |
| M27.24 | Prédire la trajectoire de la descente-montée simultanée puis alternée sur xy, puis la tracer : spirale qui s'éloigne ou courbe fermée ? | 🔮 | ★ | 15 | C |
| M27.25 | Le biais d'une distance estimée : ‖x̄₁ − x̄₂‖² entre deux échantillons d'une même loi de ℝ³, selon leurs tailles, contre tr Σ₁/n₁ + tr Σ₂/n₂ | 🔬 | ★★ | 20 | C |
| M27.26 | Deux fonctions de répartition sur une même figure : l'aire entre elles (W₁) et leur plus grand écart vertical (KS), pour une translation puis une dilatation | 🎨 | ★ | 20 | C, E |
| M27.27 | Chasse à l'erreur : une stratégie d'indifférence calculée sur ses propres gains, W₂ de deux gaussiennes avec des variances, des échantillons appariés sans être triés | 🐛 | ★ | 25 | C |
| M27.28 | Un test de propriété : la valeur d'un jeu 2 × 2 tiré au hasard est entre maximin et minimax, et devient v + c pour G + c et k v pour k G (k > 0) | 🛠️ | ★ | 20 | C |
| M27.29 | Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂, et cette distance, à 10⁻³ près | 🏆 | ★★★ | 30 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les quatre 🔨 complètent ta copie `mon_travail/mymath/distances.py` (**mymath :** `distances.py`), dont la docstring du module dit ce qui est permis : NumPy et le module `math`, mais rien de `np.linalg` et aucune fonction de SciPy (`scipy.optimize` résout un jeu) ; ne jamais modifier les tableaux reçus ; rendre des nombres `float`, des indices `int` et des itérés en tableaux NumPy de flottants. Chaque 🔨 lance le groupe de tests de sa fonction dans `tests/test_m27_distances.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.distances.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier (le marché, les tirs au but, les dépôts et les magasins, les sachets, la machine du 🔗) sont recopiées dans une cellule du notebook.

**M27.19 · 🔨 `pure_strategy_values(G)`.** Écris la fonction : contrôle `G` (un tableau 2-D, non vide, de nombres finis ; sinon une `ValueError`) ; calcule le minimum de chaque ligne (`axis=1`) et le maximum de chaque colonne (`axis=0`), puis le maximin, le minimax, et les plus petits indices `row` et `col` où ils sont atteints (`np.argmax` et `np.argmin` rendent le premier en cas d'égalité) ; rends `(maximin, minimax, row, col)`, deux `float` et deux `int` Python ; lance le groupe de tests. Ensuite : a) le marché de M27.1, à comparer à tes réponses a) et b) (les indices partent de 0) ; b) le même jeu vu par l'enseigne B, `-G.T` (ses lignes sont les stratégies de B, qui maximise ce que A perd) : le résultat, et pourquoi le maximin de `-G.T` est l'opposé du minimax de `G` ; c) les tirs au but de M27.2, et vrai ou faux : `(row, col)` y est un point selle. Ce qu'il faut observer : la fonction rend un point selle quand il en existe un ; sans point selle, `row` et `col` ne sont que des coups prudents, que l'adversaire exploite s'il les connaît.

**M27.20 · 🔨 `mixed_strategy_value_2x2(G)`.** Écris la fonction : contrôle la forme $(2, 2)$, puis appelle ta `pure_strategy_values` ; s'il y a un point selle (`maximin == minimax`, une comparaison exacte), rends les stratégies pures, `p = 1.0` si `row == 0` et `p = 0.0` sinon, de même pour `q` avec `col`, et `value = maximin` ; sinon, rends les trois formules d'indifférence de la fiche ; lance le groupe de tests. Ensuite : a) les tirs au but de M27.2, à comparer à tes réponses a) à c) ; b) pour $\mathbf{G} = \begin{pmatrix} 4 & 7 \\ 1 & 3 \end{pmatrix}$ : ce que donneraient les formules de $p^\star$ et de $q^\star$, et ce que rend ta fonction ; c) pour les tirs au but, le plus petit gain espéré de $p^\star$ contre les deux plongeons, $\min_j(\mathbf{p}^{\star\top}\mathbf{G})_j$, et le plus grand de $q^\star$ contre les deux tirs, $\max_i(\mathbf{G}\mathbf{q}^\star)_i$. Ce qu'il faut observer : avec un point selle, les formules d'indifférence sortent de $[0, 1]$ ; sans point selle, $p^\star$ et $q^\star$ garantissent la même valeur, chacun de son côté.

**M27.21 · 🔨 `descent_ascent_iterates(A, x0, y0, eta, n_steps=10, alternating=False)`.** Écris les itérés de la descente-montée sur $\mathbf{x}^\top\mathbf{A}\mathbf{y}$ : le joueur $\mathbf{x}$ (les lignes de $\mathbf{A}$) minimise, comme dans MML (7.23). Contrôle `A` (2-D, non vide, de nombres finis), `x0` et `y0` (des tableaux **1-D** de $n$ et de $m$ coordonnées : `np.array([1.0])`, pas `np.array([[1.0]])`), `eta` (un nombre fini $> 0$, pas un booléen) et `n_steps` (un entier $\ge 0$, ni un booléen ni un flottant) ; prépare deux tableaux de formes $(N + 1, n)$ et $(N + 1, m)$, de lignes 0 les départs ; à chaque pas, calcule le nouveau $\mathbf{x}$ à partir de l'ancien $\mathbf{y}$, puis le nouveau $\mathbf{y}$ à partir de l'ancien $\mathbf{x}$ (simultané) ou du nouveau (alterné) ; lance le groupe de tests. Ensuite, sur $xy$ (`A = [[1.0]]`, depuis $x_0 = 1$ et $y_0 = 0$, avec $\eta = 0{,}6$) : a) en simultané, la distance à l'équilibre après 4 pas et après 5 pas, à comparer à ta réponse c) de M27.4 ; b) en alterné, sur 200 pas : le plus grand écart $\lvert Q(x_k, y_k) - Q(x_0, y_0)\rvert$, avec $Q(x, y) = x^2 + y^2 - \eta xy$, et vrai ou faux, la distance à l'équilibre ne dépasse jamais $1/\sqrt{0{,}7}$, le demi-grand axe de l'ellipse $Q = 1$. Enfin c) sur le jeu de matrice $\mathbf{A} = \begin{pmatrix} 1 & -2 & 0 \\ 0{,}5 & 1 & -1 \end{pmatrix}$ ($\mathbf{x} \in \mathbb{R}^2$, $\mathbf{y} \in \mathbb{R}^3$), avec $\eta = 0{,}3$, depuis $\mathbf{x}_0 = (1, 0)$ et $\mathbf{y}_0 = (0, 1, 0)$ : vrai ou faux, en simultané, $\lVert\mathbf{x}_k\rVert^2 + \lVert\mathbf{y}_k\rVert^2$ ne diminue jamais sur 50 pas ; et, en alterné, le plus grand écart de $\lVert\mathbf{x}_k\rVert^2 + \lVert\mathbf{y}_k\rVert^2 - \eta\,\mathbf{x}_k^\top\mathbf{A}\mathbf{y}_k$ à sa valeur de départ sur 100 pas. Les deux écarts demandés sont des erreurs d'arrondi : toute valeur sous $10^{-12}$ est acceptée. Ce qu'il faut observer : les deux propriétés de la fiche, vérifiées aux arrondis près, l'une qui éloigne de l'équilibre, l'autre qui garde une quantité constante.

**M27.22 · 🔨 `w2_gaussians_1d(mu1, sigma1, mu2, sigma2)`.** Écris $W_2$ entre $\mathcal{N}(\mu_1, \sigma_1^2)$ et $\mathcal{N}(\mu_2, \sigma_2^2)$ à partir des **écarts-types** : contrôle les quatre nombres (des réels finis, pas des booléens) et le signe des écarts-types (un écart-type nul est permis : la loi est alors une masse ponctuelle) ; rends $W_2$, pas son carré, en `float` Python (`math.hypot`) ; lance le groupe de tests. Ensuite : a) les sachets de M27.8, à comparer à ta réponse c) ; b) la machine du 🔗 M27.16, à comparer à ta réponse b) ; c) $\mathcal{N}(10 ;\ 3^2)$ contre $\mathcal{N}(10 ;\ 1^2)$. Ce qu'il faut observer : $W_2$ est la distance euclidienne entre les points (moyenne, écart-type).

**M27.23 · 📦 Le transport optimal comme programme linéaire.** Écris `transport_lp_23(C, a, b)`, qui résout le programme linéaire du transport (fiche §7) par `scipy.optimize.linprog(..., method="highs")` : les $mn$ inconnues $\gamma_{ij}$ rangées ligne par ligne, le coût $\sum\gamma_{ij}c_{ij}$, les $m + n$ contraintes d'égalité des marges (l'une est redondante : `linprog` s'en accommode) et $\gamma_{ij} \ge 0$ ; elle rend `(plan, cost)`, le plan de forme $(m, n)$ et son coût. Écris aussi `northwest_23(a, b)`, qui rend le plan du coin nord-ouest (fiche §8) pour deux tableaux de masses de même somme, les points étant supposés rangés dans l'ordre croissant ; la vérification essaie les deux fonctions sur des cas cachés. Avec les dépôts et les magasins de M27.7 (masses en tonnes) : a) pour le coût $c_{ij} = \lvert x_i - y_j\rvert$, le coût optimal (t·km) et $W_1$ (km), et vrai ou faux, le plan du coin nord-ouest a le même coût ; b) pour le coût $(x_i - y_j)^2$, le coût optimal (t·km²) et $W_2$ (km), et vrai ou faux, le plan de `linprog` est le plan du coin nord-ouest ; c) on quitte la route : les dépôts sont aux points $(1, 0)$, $(4, 3)$ et $(6, -2)$ d'une carte, les magasins aux points $(2, -3)$, $(3, 4)$ et $(8, 1)$ (en km), avec les mêmes masses et le coût $\lVert\mathbf{x}_i - \mathbf{y}_j\rVert$ : le coût optimal, et le coût du plan du coin nord-ouest pris dans l'ordre des abscisses (t·km, 2 décimales). Compare enfin a) à ton $W_1$ de M27.7, obtenu aussi par l'aire entre les fonctions de répartition. Ce qu'il faut observer : sur la droite, le plan monotone est optimal pour les deux coûts, et l'aire entre les fonctions de répartition donne $W_1$ sans programme linéaire ; pour le coût $\lvert x - y\rvert$, l'optimum n'est pas toujours unique, et `linprog` peut rendre un autre plan de même coût ; dans le plan, l'ordre ne veut plus rien dire, et il faut le programme linéaire.

**M27.24 · 🔮 Prédire la trajectoire de la descente-montée sur xy, puis la tracer.** On joue la descente-montée sur $xy$ depuis $(x_0, y_0) = (1, 0)$, pendant 40 pas. **Avant d'exécuter**, prédis : a) avec $\eta = 0{,}3$, en simultané, la distance à l'équilibre après 40 pas vaut environ : (A) 1 ; (B) 1,5 ; (C) 5,6 ; (D) 40 ; b) avec $\eta = 0{,}3$, en simultané, le nombre de tours que font les itérés autour de l'équilibre en 40 pas : (A) moins d'un ; (B) entre 1 et 2 ; (C) entre 3 et 4 ; (D) aucun, ils partent en ligne droite ; c) avec $\eta = 2{,}5$, en alterné : (A) une courbe fermée ; (B) des itérés qui s'éloignent ; (C) des itérés qui convergent vers $(0, 0)$. Puis écris `draw_paths_24(ax, eta, n_steps, alternating)`, qui dessine sur l'**axe reçu** (sans ouvrir de figure), avec ta `descent_ascent_iterates`, les itérés depuis $(1, 0)$ reliés dans l'ordre, l'équilibre marqué par un point, des axes de même échelle (`ax.set_aspect("equal")`), un titre qui donne $\eta$ et le mode, et des noms d'axes ; la vérification l'appelle pour $\eta = 0{,}3$ (simultané, puis alterné) et pour $\eta = 2{,}5$ (alterné), et affiche la figure. Relève : d) la distance à l'équilibre après 40 pas simultanés avec $\eta = 0{,}3$ ; e) le nombre de tours de ces 40 pas (l'angle total parcouru, `np.unwrap(np.arctan2(y, x))`, divisé par $2\pi$) ; f) $\log_{10}$ de la distance après 40 pas alternés avec $\eta = 2{,}5$. Ce qu'il faut observer : la spirale est réglée par le module et l'argument de $1 \pm i\eta$ ; le pas alterné ne reste sur une courbe fermée que pour $\eta < 2$.

**M27.25 · 🔬 Le biais d'une distance estimée.** Une machine fabrique des cales ; on mesure trois cotes de chacune (en mm), de moyenne $\boldsymbol{\mu} = (80, 25, 6)$ et de covariance
$$\boldsymbol{\Sigma} = \begin{pmatrix} 0{,}09 & 0{,}03 & 0 \\ 0{,}03 & 0{,}04 & 0{,}01 \\ 0 & 0{,}01 & 0{,}01 \end{pmatrix}, \qquad \operatorname{tr}\boldsymbol{\Sigma} = 0{,}14\ \text{mm}^2 .$$
Écris `distance_bias_25(mu1, mu2, Sigma, n1, n2, n_rep, rng)`, qui simule `n_rep` paires de séries indépendantes, toutes à la fois avec des tableaux, dans cet ordre : `L = np.linalg.cholesky(Sigma)`, puis la série 1, `mu1 + rng.standard_normal((n_rep, n1, 3)) @ L.T`, puis la série 2, `mu2 + rng.standard_normal((n_rep, n2, 3)) @ L.T` ; elle rend la moyenne, sur les `n_rep` paires, de $\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2$. Avec `rng = np.random.default_rng(6425)`, `n_rep = 4000` et ce même `rng` pour tous les appels, dans l'ordre : deux séries de la même machine (`mu1 = mu2 = mu`) pour $(n_1, n_2) = (5, 5)$, $(20, 20)$, $(80, 80)$, $(5, 80)$ et $(80, 5)$ ; puis, avec `mu2 = mu + (0.05, 0, 0)` (un vrai décalage de la première cote), pour $(5, 5)$ et $(80, 80)$. Relève : a) les cinq moyennes, les cinq valeurs $\operatorname{tr}\boldsymbol{\Sigma}\,(\frac{1}{n_1} + \frac{1}{n_2})$, et leurs rapports (3 décimales) ; b) vrai ou faux : les cinq rapports sont à moins de 5 % de 1 ; c) avec le décalage, les deux moyennes, puis les mêmes moins $\operatorname{tr}\boldsymbol{\Sigma}\,(\frac{1}{n_1} + \frac{1}{n_2})$, à comparer à $\lVert\boldsymbol{\delta}\rVert^2 = 0{,}0025$ ; d) vrai ou faux : avec 5 cales par série, la distance estimée moyenne dépasse vingt fois la vraie distance $\lVert\boldsymbol{\delta}\rVert^2$. Écris aussi `draw_bias_25(ax, ns, means, trace)`, qui trace dans l'axe reçu, en échelles logarithmiques, les moyennes des séries de même taille $n$ contre $n$ (des points) et la droite $2\operatorname{tr}\boldsymbol{\Sigma}/n$ sur toute l'étendue de `ns`, avec des noms d'axes et une légende ; la vérification l'appelle sur les trois tailles égales et affiche la figure. Ce qu'il faut conclure : la distance estimée entre deux séries d'une même machine n'est pas nulle, elle suit $\operatorname{tr}\boldsymbol{\Sigma}\,(\frac{1}{n_1} + \frac{1}{n_2})$ ; un petit décalage réel se noie dans ce biais sur de petites séries ; deux distances estimées ne se comparent qu'à tailles égales, ou après avoir retiré le biais.

**M27.26 · 🎨 Deux fonctions de répartition sur une même figure.** Écris `draw_cdf_gaps_26(ax, cdf_a, cdf_b, grid, label_a, label_b, unit)`, qui dessine sur l'**axe reçu** les deux fonctions de répartition évaluées sur `grid`, colore l'aire entre elles (`ax.fill_between`), trace un segment vertical là où leur écart $\lvert F - G\rvert$ est le plus grand sur la grille, et met une légende (`label_a`, `label_b`), et en titre les deux nombres $W_1$ (l'aire, par la méthode des trapèzes, `np.trapezoid`) et KS (le plus grand écart sur la grille), avec l'unité de $W_1$ ; elle rend `(w1, ks)`. La vérification l'appelle trois fois et affiche les figures : une **translation**, la température d'un local, $\mathcal{N}(20 ;\ 2^2)$ contre $\mathcal{N}(21{,}2 ;\ 2^2)$ en °C, sur `np.linspace(10, 32, 4401)` ; une **dilatation**, une attente à un guichet, la loi exponentielle de moyenne 2 contre celle de moyenne 5, en minutes, sur `np.linspace(0, 80, 16001)` (`scipy.stats.expon(scale=2).cdf`) ; la même translation en °F, $\mathcal{N}(68 ;\ 3{,}6^2)$ contre $\mathcal{N}(70{,}16 ;\ 3{,}6^2)$, sur la grille $1{,}8 \times$ `grid` $+ 32$. Relève : a) `(w1, ks)` pour la translation ; b) pour la dilatation ; c) en °F (3 décimales). Ce qu'il faut observer : pour la translation, l'aire vaut le décalage, et l'écart vertical est le plus grand au milieu ; pour la dilatation, les deux courbes partent du même point et s'écartent, puis se rejoignent ; un changement d'unité multiplie $W_1$ et laisse KS intact.

**M27.27 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `penalty_kick_mix(G)` doit rendre $p^\star$, la probabilité optimale de la première ligne d'un jeu $2 \times 2$ sans point selle ; elle rend `(d - b) / (a - b - c + d)`. Il l'a vérifiée sur le jeu $\begin{pmatrix} 50 & 90 \\ 90 & 60 \end{pmatrix}$ : $p$ est entre 0 et 1, et les deux colonnes coûtent alors autant au joueur des colonnes, $50p + 90(1 - p) = 90p + 60(1 - p)$. Il l'applique aux tirs au but de M27.2.
- (2) `w2_settings(mu1, sd1, mu2, sd2)` doit rendre $W_2$ entre deux réglages d'une machine, résumés par leur moyenne et leur écart-type ; elle rend `math.sqrt((mu1 - mu2) ** 2 + (sd1 ** 2 - sd2 ** 2) ** 2)`. Il l'a vérifiée par `w2_settings(0, 1, 3, 1) == 3` et `w2_settings(2, 0, 2, 1) == 1`.
- (3) `pair_parts(shafts, sleeves)` doit apparier $n$ axes et $n$ bagues, dont on a mesuré les diamètres (en mm), pour que les jeux bague − axe soient aussi réguliers que possible : elle rend un tableau d'entiers `partner`, où `partner[i]` est l'indice de la bague montée sur l'axe `i`, qui minimise $\sum_i(\text{bague} - \text{axe})^2$ (la fiche, §8, et ∂ M27.14 : trier puis apparier). Elle rend `np.argsort(sleeves)`. Il l'a vérifiée avec les axes `[10.00, 10.02, 10.05]` et les bagues `[10.09, 10.06, 10.11]` : elle rend `[1, 0, 2]`, et les jeux valent 0,06 ; 0,07 ; 0,06.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `penalty_kick_mix_fixed`, `w2_settings_fixed` et `pair_parts_fixed`, avec les mêmes arguments ; `pair_parts_fixed` rend aussi un tableau d'entiers), puis réponds : a) $p^\star$ pour les tirs au but par `penalty_kick_mix_fixed`, et ce que rend `penalty_kick_mix` ; b) $W_2$ par `w2_settings_fixed` et par `w2_settings`, pour la machine du 🔗 M27.16, puis pour $\mathcal{N}(100 ;\ 5^2)$ contre $\mathcal{N}(100 ;\ 2^2)$ ; c) pour les axes `[20.03, 19.98, 20.01, 19.96, 20.05]` et les bagues `[20.10, 20.04, 20.13, 20.07, 20.06]` : ce que rend `pair_parts_fixed`, et $\sum_i(\text{bague} - \text{axe})^2$ (mm²) pour l'appariement corrigé, puis pour celui du collègue. Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas.

**M27.28 · 🛠️ Un test de propriété.** Le notebook fournit quatre versions fausses de `mixed_strategy_value_2x2` : `swapped_pq` (elle rend $(q, p, v)$), `formulas_always` (les formules d'indifférence même quand il y a un point selle, sauf si $\kappa = 0$), `maximin_as_value` (les bonnes stratégies, mais le maximin comme valeur) et `rounded_value` (la valeur arrondie à l'entier). Écris `game_property_test_28(n_trials, rng, solver=None, tol=1e-9)` ; quand `solver` vaut `None`, le test prend `mymath.distances.mixed_strategy_value_2x2` **au moment de l'appel**. Pour chacun des `n_trials` essais, dans cet ordre : `G = rng.integers(-9, 10, size=(2, 2)).astype(float)`, `c = float(rng.integers(-5, 6))`, `k = float(rng.integers(2, 6))` ; puis `p, q, v = solver(G)`, et le maximin et le minimax de `G`, calculés dans le test par `G.min(axis=1).max()` et `G.max(axis=0).min()`, sans appeler `mymath`. La fonction rend un dictionnaire de cinq compteurs d'essais : `"bounds"`, si $v$ sort de $[\text{maximin} - \text{tol} ;\ \text{minimax} + \text{tol}]$, ou si $p$ ou $q$ sort de $[-\text{tol} ;\ 1 + \text{tol}]$ ; `"shift"`, si `solver(G + c)` s'écarte de $(p, q, v + c)$ de plus de `tol` en une coordonnée ; `"scale"`, si `solver(k * G)` s'écarte de $(p, q, kv)$ ; et, **seulement pour les jeux sans point selle** (maximin $<$ minimax), `"transpose"`, si `solver(-G.T)` s'écarte de $(q, p, -v)$, et `"swap_rows"`, si `solver(G[::-1])` s'écarte de $(1 - p, q, v)$. a) Pourquoi des gains entiers, et des $c$ et $k$ entiers ? Pourquoi les deux dernières propriétés seulement sans point selle (essaie $\mathbf{G} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$) ? b) Avec `rng = np.random.default_rng(6428)` et 400 essais, avec ta fonction : vrai ou faux, les cinq compteurs sont nuls ; c) avec le même départ et chacune des quatre versions fausses : les cinq compteurs (la vérification les affiche) ; d) lesquelles des versions fausses passent les trois propriétés du titre (`"bounds"`, `"shift"` et `"scale"`) ? La vérification compare aussi tes compteurs à ceux de la référence sur deux départs cachés, et remplace un instant `mymath.distances.mixed_strategy_value_2x2` par une version fausse : tes compteurs doivent alors compter. Ce qu'il faut retenir : les propriétés du titre, déjà vérifiées par `tests/test_m27_distances.py`, laissent passer des versions fausses ; l'échange des rôles et l'échange des lignes, qui ne valent que si les stratégies optimales sont uniques, les attrapent ; un test se juge aux erreurs qu'il attrape.

**M27.29 · 🏆 Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂.** Le temps d'attente à un guichet suit la loi exponentielle de moyenne 2 minutes : $F(x) = 1 - e^{-x/2}$ pour $x \ge 0$, de fonction quantile $F^{-1}(u) = -2\ln(1 - u)$. On cherche la loi normale $\mathcal{N}(\mu, \sigma^2)$, $\sigma \ge 0$, la plus proche de cette loi au sens de $W_2$, et cette distance. Écris `closest_gaussian_29(quantile)`, qui reçoit la fonction quantile d'une loi de moment d'ordre 2 fini (une fonction NumPy de $u \in\ ]0, 1[$, qui accepte un tableau) et rend `(mu, sigma, w2)`. Tout NumPy et SciPy sont permis (`scipy.integrate.quad`, `scipy.optimize`, `scipy.stats.norm.ppf`), mais la fonction ne reçoit que la fonction quantile : aucune formule propre à la loi exponentielle. **Critère de réussite :** `mu`, `sigma` et `w2` à moins de $10^{-3}$ des valeurs exactes pour l'attente au guichet, et pour deux lois cachées de la vérification, en moins de 10 secondes par loi. Relève : a) `(mu, sigma, w2)` pour l'attente au guichet (3 décimales) ; b) vrai ou faux : $\mu$ est la moyenne de la loi exponentielle ; c) $W_2^2$ divisé par la variance de la loi exponentielle (4) : la part de la variance que la meilleure gaussienne ne peut pas rendre (en %, 1 décimale). Point de départ : $W_2^2(\mu, \sigma) = \int_0^1\big(F^{-1}(u) - \mu - \sigma\Phi^{-1}(u)\big)^2\,\mathrm{d}u$ (fiche §8) ; une somme sur une grille régulière de $u$ converge lentement, à cause des queues.
