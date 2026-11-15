# M28 · Matrice de Gram, montée sur l'entrée et lois tronquées — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m28_gram_echantillonnage/06_mes_reponses.md` (créée par `python tools/start_chapter.py M28`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les $n$ points (ou vecteurs) sont les **lignes** de $\mathbf{X}$, de forme $(n, d)$, numérotés à partir de 1, et $\mathbf{G} = \mathbf{X}\mathbf{X}^\top$ ; $\mathbf{D}^{(2)}$ est la matrice des **carrés** des distances et $\mathbf{J} = \mathbf{I} - \frac1n\mathbf{1}\mathbf{1}^\top$ la matrice de centrage ; au §3, les coordonnées de $\mathbf{x}$ sont numérotées à partir de 1, $\operatorname{clip}$ projette coordonnée par coordonnée sur le pavé ; au §4, les cases d'un signal ou d'une grille sont numérotées à partir de 0, $\mathrm{VT}$ est la somme des **carrés** des différences entre voisins (la version avec des valeurs absolues est toujours nommée « en valeur absolue »), et $\omega = 2\pi f$ est en radians par case ; au §5, une loi est un vecteur de probabilités, ses issues sont numérotées à partir de 0, entre deux probabilités égales la plus petite issue passe d'abord, $m$ est le seuil d'un top-p, et les divergences KL sont en **nats** ; au §6, $\mu$ est la prépériode et $\lambda$ la période. Dans le notebook, une matrice s'écrit comme la liste de ses lignes, un vecteur comme une liste ou un tableau **1-D**, et un ensemble d'issues comme la liste de leurs numéros.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M28.Q1 — Matrice de Gram : XXᵀ ou XᵀX, laquelle former, sa diagonale, et les distances qu'on y lit 🧠 ★ ⏱️ 4 min
*Fiche §1 et §2 · parcours C, E*

1. Une station enregistre 30 grandeurs (température, pression, humidité…) à $10^5$ instants : $\mathbf{X}$ a 30 lignes, les grandeurs, et $10^5$ colonnes, les instants. Tu veux les valeurs propres non nulles des deux matrices de Gram de $\mathbf{X}$. Laquelle formes-tu, et combien de multiplications coûte-t-elle, en ordre de grandeur ?
2. Deux vecteurs ont $G_{11} = 9$, $G_{22} = 16$ et $G_{12} = 6$. Que valent la distance entre eux et l'angle qu'ils forment ?
3. Vrai ou faux : translater tous les points d'un nuage d'un même vecteur ne change pas leur matrice de Gram.
4. Vrai ou faux : toute matrice symétrique dont les coefficients sont tous positifs est une matrice de Gram. Si c'est faux, donne un contre-exemple $2 \times 2$.
5. Trois capteurs relèvent chacun 200 valeurs : $\mathbf{X}$ a 3 lignes, les capteurs, et 200 colonnes, les relevés. Par quel nombre divises-tu $\mathbf{X}\mathbf{X}^\top$ pour obtenir la matrice des moments d'ordre 2 des trois capteurs ?

### M28.Q2 — Monter sur l'entrée : pas normalisé, projection sur un pavé, coordonnées gelées, point d'arrivée 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Pour $\mathbf{g} = (-2, 0, 6, 3)$, écris $\mathbf{g}/\lVert\mathbf{g}\rVert$, $\mathbf{g}/\operatorname{rms}(\mathbf{g})$ et $\operatorname{sign}(\mathbf{g})$. Lesquels ont la direction de $\mathbf{g}$ ?
2. Sur le pavé $[0, 1]^3$, depuis $\mathbf{x} = (0{,}88 ;\ 0{,}2 ;\ 1)$, on fait un pas de montée projetée de pas $\eta = 0{,}5$, avec $\mathbf{g} = (0{,}4 ;\ -0{,}6 ;\ 0{,}2)$. Où arrive-t-on ?
3. Quatre coordonnées, dont seules la première et la troisième sont libres, et $\mathbf{g} = (2, 5, -1, 4)$. Quel vecteur la montée suit-elle ? Vrai ou faux : parmi les directions qui ne bougent pas les coordonnées gelées, c'est celle de la plus grande pente.
4. Vrai ou faux : une montée projetée sur une fonction convexe s'arrête toujours sur le sommet du pavé où la fonction est la plus grande.
5. Vrai ou faux : avec un pas normalisé $\mathbf{g}/\lVert\mathbf{g}\rVert$ de longueur $\eta$ fixe, une montée sur une fonction concave finit par s'arrêter exactement en son maximum.

### M28.Q3 — Variation totale et fréquences spatiales : quel motif coûte le plus, lequel traverse un flou ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Pour le signal $\mathbf{x} = (2, 5, 4, 4, 1)$, que valent la variation totale et la variation totale en valeur absolue ?
2. Sur un anneau, trois motifs cosinus ont la même énergie $\lVert\mathbf{x}\rVert^2$, et des périodes de 2, 4 et 10 cases. Lequel a la plus grande variation totale, et lequel la plus petite ?
3. Lequel des trois traverse le mieux une moyenne mobile de trois cases, c'est-à-dire a le gain le plus grand en valeur absolue ?
4. Un motif de fréquence $\frac58$ de cycle par case est relevé une fois par case. De quel motif de fréquence comprise entre 0 et $\frac12$ ne se distingue-t-il pas, et quelle est la période de celui-ci ?
5. Vrai ou faux : la variation totale d'une grille et la distance en variation totale entre deux lois mesurent la même chose.

### M28.Q4 — Température, top-k et top-p : ce qui change l'ensemble gardé, ce qui ne change que les probabilités 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Vrai ou faux : pour $0 < T < \infty$, changer la température change l'ensemble gardé par un top-k.
2. $\mathbf{p} = (0{,}12 ;\ 0{,}38 ;\ 0 ;\ 0{,}19 ;\ 0{,}31)$. Vers quelle loi tend $\mathbf{p}^{(T)}$ quand $T \to \infty$ ? Quel ensemble garde le top-3 pour $0 < T < \infty$, et quel ensemble à la limite $T = \infty$ ?
3. Vrai ou faux : à seuil $m$ fixé, quand $T$ monte, l'ensemble du top-p grandit ou garde sa taille, mais ne rétrécit jamais.
4. Vrai ou faux : tronquer une loi par un top-k change le rapport $p_i/p_j$ de deux issues gardées.
5. Vrai ou faux : le top-p de seuil $m = 1$ garde toutes les issues, celles de probabilité nulle comprises.

### M28.Q5 — Une itération sur un ensemble fini : prépériode, période, et ce qui empêche de boucler 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Sur $E = \{0, 1, 2, 3, 4, 5\}$, $f$ est donnée par $f(0) = 3$, $f(1) = 0$, $f(2) = 4$, $f(3) = 5$, $f(4) = 2$, $f(5) = 4$. Depuis $u_0 = 1$, que valent la prépériode $\mu$ et la période $\lambda$ ? Compare $\mu + \lambda$ au nombre $N$ d'éléments de $E$.
2. Vrai ou faux : si $f$ est une bijection de $E$, toute suite $u_{t+1} = f(u_t)$ est périodique dès $u_0$.
3. Vrai ou faux : une suite $u_{t+1} = f(u_t)$ dans un ensemble de 500 éléments peut avoir une période de 1 000.
4. Un générateur écrit des symboles en tirant chacun au hasard, selon une loi qui dépend des 3 derniers symboles écrits. Vrai ou faux : sa suite de symboles finit forcément par être périodique.
5. Un générateur glouton écrit des symboles d'un alphabet de 3 symboles, et son état est fait des 4 derniers symboles écrits. Quelle borne le théorème de la fiche donne-t-il pour $\mu + \lambda$ ?

<a id="rappels"></a>

## 🔁 Rappels

### M28.R1 — Le quotient de Rayleigh et la méthode de la puissance (M12c) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 9 & 2 \\ 2 & 6 \end{pmatrix}$ et $R(\mathbf{x}) = \dfrac{\mathbf{x}^\top\mathbf{A}\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}$ pour $\mathbf{x} \ne \mathbf{0}$.
1. Les valeurs propres de $\mathbf{A}$, et un vecteur propre de chacune.
2. $R(1, 0)$ et $R(1, 1)$.
3. Le maximum de $R$, et les $\mathbf{x}$ où il est atteint.
4. Deux pas de la méthode de la puissance depuis $(1, 0)$, sans normaliser : $\mathbf{A}(1, 0)$, puis $\mathbf{A}^2(1, 0)$. Vers quelle direction la suite tourne-t-elle, et par quel facteur le rapport de sa composante sur $(1, -2)$ à sa composante sur $(2, 1)$ est-il multiplié à chaque pas ?
5. Vrai ou faux : la méthode de la puissance converge vers la direction du vecteur propre dominant depuis tout départ non nul.

### M28.R2 — Le laplacien discret et la moyenne mobile d'un signal (M21) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

Le signal $\mathbf{x} = (1, 4, 2, 6, 3)$ occupe les cases 0 à 4.
1. Les différences secondes $x_{j-1} - 2x_j + x_{j+1}$ aux cases intérieures 1, 2 et 3 (le pochoir du laplacien discret de M21, pour un pas de 1).
2. La moyenne mobile de trois cases, $y_j = \frac13(x_{j-1} + x_j + x_{j+1})$, aux mêmes cases.
3. Vérifie que $y_j - x_j$ vaut le tiers de la différence seconde en $j$. Que fait donc la moyenne mobile à un pic du signal ?
4. Vrai ou faux : la moyenne mobile de trois cases est une convolution par le noyau $(\frac13, \frac13, \frac13)$.

### M28.R3 — La loi de Boltzmann et ses limites en température (M17) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

Quatre niveaux ont les énergies $\mathbf{E} = (0 ;\ \ln 2 ;\ \ln 2 ;\ \ln 4)$, et la loi de Boltzmann $p_i \propto e^{-E_i/T}$.
1. Les quatre probabilités à $T = 1$, en fractions.
2. La loi limite quand $T \to 0$, puis quand $T \to \infty$.
3. Vrai ou faux : deux niveaux de même énergie ont la même probabilité à toute température.
4. On ajoute un cinquième niveau, interdit (d'énergie infinie). Que vaut sa probabilité à toute température $T > 0$ ? Quelle est la loi limite des cinq niveaux quand $T \to \infty$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ; un ensemble d'issues comme la liste de leurs numéros, dans l'ordre demandé, comme `[4, 0, 2]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- un intervalle entre guillemets, en notation française, avec des points décimaux, comme `"]2.5 ; 4]"` ;
- `True` ou `False` pour un vrai ou faux.

Quand la réponse attendue est « un nombre » sans décimales précisées, le calcul tombe juste : donne la valeur exacte. Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M28.1 — Quatre points du plan : leur matrice de Gram 4 × 4, leur matrice des moments d'ordre 2, et les distances lues dans la Gram ✏️ ★★ ⏱️ 20 min
**Objectif :** former la matrice de Gram d'une famille de points dans les deux sens et la matrice des moments d'ordre 2, puis lire des distances et un angle dans la matrice de Gram.
**Prérequis :** fiche §1 et §2 ; M09a, M12c · **Parcours :** C, E

Quatre balises sont posées sur un terrain plat. Leurs positions, en mètres dans un repère orthonormé, sont $\mathbf{x}_1 = (3, 1)$, $\mathbf{x}_2 = (1, 3)$, $\mathbf{x}_3 = (-2, 0)$ et $\mathbf{x}_4 = (0, -2)$ ; on les range en lignes de $\mathbf{X}$, de forme $(4, 2)$. On lit aussi les quatre balises comme quatre échantillons d'un point aléatoire du plan.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice de Gram $\mathbf{G} = \mathbf{X}\mathbf{X}^\top$ (m²) | une matrice $4 \times 4$ |
| b | la matrice des moments d'ordre 2 des deux coordonnées, les quatre balises étant quatre échantillons (m²) | une matrice $2 \times 2$ |
| c | les valeurs propres non nulles de $\mathbf{G}$, par ordre décroissant | une liste de 2 nombres |
| d | les carrés des distances de $\mathbf{x}_1$ à $\mathbf{x}_2$, à $\mathbf{x}_3$ et à $\mathbf{x}_4$, lus dans $\mathbf{G}$, dans cet ordre (m²) | une liste de 3 nombres |
| e | l'angle entre les vecteurs $\mathbf{x}_1$ et $\mathbf{x}_2$, en degrés | un nombre (1 décimale) |

Dans ta copie : écris la forme de chaque matrice avant de la calculer ; dis pourquoi, avec les échantillons en lignes, la matrice des moments est $\frac14\mathbf{X}^\top\mathbf{X}$ et non $\frac14\mathbf{X}\mathbf{X}^\top$ ; trouve les valeurs propres de c) avec la plus petite des deux matrices de Gram, en disant pourquoi c'est permis ; vérifie $\operatorname{tr}\mathbf{G} = \operatorname{tr}\mathbf{X}^\top\mathbf{X}$, et dis quelle somme vaut cette trace ; donne le rang de $\mathbf{G}$, avec sa raison ; vérifie l'un des carrés de distance de d) sur les coordonnées ; dis ce que vaut $G_{34}$, et ce qu'il dit des vecteurs $\mathbf{x}_3$ et $\mathbf{x}_4$.

### Ex M28.2 — Quatre villes aux sommets d'un losange : le double centrage des carrés des distances, puis une carte à une isométrie près ✏️ ★★ ⏱️ 25 min
**Objectif :** retrouver la matrice de Gram de points centrés à partir des seules distances (double centrage), puis des positions par le théorème spectral, et reconnaître des distances qui ne sont celles d'aucun nuage de points.
**Prérequis :** fiche §2 ; M12c, M20 · **Parcours :** C, E

Quatre villes A, B, C et D sont aux sommets d'un losange, dans cet ordre. On ne connaît que leurs distances à vol d'oiseau, en km : $\mathrm{AB} = \mathrm{BC} = \mathrm{CD} = \mathrm{DA} = 29$, $\mathrm{AC} = 40$ et $\mathrm{BD} = 42$. Les villes sont rangées dans l'ordre A, B, C, D, et $\mathbf{D}^{(2)}$ est la matrice $4 \times 4$ des carrés de leurs distances. La carte se construit comme dans la fiche : $\mathbf{G} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ avec $\lambda_1 \ge \lambda_2 \ge \cdots$, la colonne $k$ de la carte est $\sqrt{\lambda_k}\,\mathbf{q}_k$, avec $\mathbf{q}_k$ unitaire, on garde autant de colonnes que de valeurs propres non nulles, et, dans chaque colonne, la première coordonnée non nulle (en lisant de A vers D) est positive.

| | Question | Réponse attendue |
|---|---|---|
| a | $s$, la moyenne des seize coefficients de $\mathbf{D}^{(2)}$ (km²) | un nombre |
| b | la matrice de Gram $\mathbf{G} = -\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ des villes centrées, lignes et colonnes dans l'ordre A, B, C, D (km²) | une matrice $4 \times 4$ |
| c | les quatre valeurs propres de $\mathbf{G}$, par ordre décroissant | une liste de 4 nombres |
| d | la carte : une ligne par ville (A, B, C, D), avec la construction et la convention de signe ci-dessus (km) | une matrice $4 \times 2$ |
| e | vrai ou faux : si l'on avait mesuré $\mathrm{AC} = 50$ km, les cinq autres distances restant les mêmes, ces six distances seraient celles de quatre points d'un espace euclidien (de dimension quelconque) | `True` ou `False` |

Dans ta copie : écris $\mathbf{D}^{(2)}$ et les moyennes $r_i$ de ses lignes, puis calcule $\mathbf{G}$ par $G_{ij} = -\frac12\big(D^{(2)}_{ij} - r_i - r_j + s\big)$ ; vérifie $\mathbf{G}\mathbf{1} = \mathbf{0}$ ; range les villes dans l'ordre A, C, B, D pour voir deux blocs $2 \times 2$, et diagonalise chacun ; dis pourquoi les colonnes de la carte sont ici uniques au signe près, et ce qui changerait si le losange était un carré ; vérifie trois distances sur ta carte ; dis quelle sorte d'isométrie peut séparer ta carte de la vraie ; pour e), justifie ta réponse sans calculer de valeurs propres, en regardant où sont A et C par rapport au milieu du segment [BD].

### Ex M28.3 — Régler quatre émetteurs entre 0 et 1 : le maximum d'une réponse linéaire sur la boule et sur le pavé, d'une énergie quadratique sur la sphère, et deux pas de montée projetée ✏️ ★★ ⏱️ 25 min
**Objectif :** prévoir où s'arrête une montée pour une forme linéaire (sur une boule, sur un pavé) et pour une forme quadratique (sur la sphère, sur un pavé), et faire des pas de montée projetée à la main.
**Prérequis :** fiche §3 ; M07, M12c, M19 · **Parcours :** C, E

Quatre émetteurs sont réglés par leurs puissances relatives $\mathbf{x} = (x_1, x_2, x_3, x_4)$, chacune entre 0 et 1. Le signal reçu par une antenne est la réponse linéaire $f(\mathbf{x}) = \mathbf{w}^\top\mathbf{x}$, avec $\mathbf{w} = (2, -1, 2, 4)$ : le deuxième émetteur brouille l'antenne. Les émetteurs déposent aussi dans une zone voisine une énergie parasite $E(\mathbf{x}) = \mathbf{x}^\top\mathbf{A}\mathbf{x}$, avec
$$\mathbf{A} = \begin{pmatrix} 5 & -1 & 0 & 0 \\ -1 & 5 & 0 & 0 \\ 0 & 0 & 6 & -2 \\ 0 & 0 & -2 & 3 \end{pmatrix}.$$
La montée projetée sur $f$ s'écrit $\mathbf{x}_{t+1} = \operatorname{clip}(\mathbf{x}_t + \eta\,\nabla f(\mathbf{x}_t),\ 0,\ 1)$, depuis $\mathbf{x}_0 = (0{,}3 ;\ 0{,}3 ;\ 0{,}6 ;\ 0{,}92)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le maximum de $\mathbf{w}^\top\mathbf{x}$ sur la boule $\lVert\mathbf{x}\rVert \le 1$, sans la contrainte du pavé | un nombre |
| b | le réglage du pavé $[0, 1]^4$ qui maximise $\mathbf{w}^\top\mathbf{x}$ | une liste de 4 nombres |
| c | avec $\eta = 0{,}2$ : le nombre de pas après lequel la montée projetée est sur ce réglage pour la première fois | un entier |
| d | le plus petit pas $\eta$ qui amène la montée projetée de $\mathbf{x}_0$ sur ce réglage en un seul pas | un nombre |
| e | le maximum de $E(\mathbf{x})$ sur la sphère $\lVert\mathbf{x}\rVert = 1$ | un nombre |
| f | le maximum de $E(\mathbf{x})$ sur le pavé $[0, 1]^4$ | un nombre |

Dans ta copie : écris le point de la boule qui atteint a), et dis pourquoi ce n'est pas un réglage permis ; écris $\mathbf{x}_1$ et $\mathbf{x}_2$ pour $\eta = 0{,}2$, et dis quelle coordonnée touche sa borne par en bas, et à quel pas ; pour d), écris, coordonnée par coordonnée, le pas qu'il faut pour atteindre sa borne ; diagonalise les deux blocs de $\mathbf{A}$, donne un vecteur unitaire qui atteint e), et dis si c'est un réglage permis ; pour f), dis pourquoi le maximum est atteint en un sommet du pavé (fiche §3, ∂ M28.9), puis trouve-le en traitant chaque bloc à part, sans essayer les 16 sommets un par un.

### Ex M28.4 — Les températures le long d'une barre : la variation totale xᵀLx, son gradient 2Lx, un pas de lissage, et une marche étalée sur n pas, au carré ou en valeur absolue ✏️ ★★ ⏱️ 25 min
**Objectif :** écrire la variation totale d'un signal comme une forme quadratique, calculer son gradient, un pas de lissage et le pas critique, et comparer le carré et la valeur absolue sur une marche.
**Prérequis :** fiche §4 ; M12c, M18, M19 · **Parcours :** C, E

Cinq sondes, aux cases 0 à 4, relèvent les températures d'une barre métallique, en °C : $\mathbf{x} = (8, 6, 7, 3, 1)$. Les deux bouts de la barre sont libres : la case 0 n'a pour voisine que la case 1, et la case 4 que la case 3. On admet que les valeurs propres du laplacien $\mathbf{L}$ d'une barre de $n$ cases à bouts libres sont $4\sin^2\frac{k\pi}{2n}$, pour $k = 0, \ldots, n - 1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathrm{VT}(\mathbf{x})$ (°C²) | un nombre |
| b | le gradient $2\mathbf{L}\mathbf{x}$ | une liste de 5 nombres |
| c | $\mathbf{x}$ après un pas de descente sur $\mathrm{VT}$, de pas $\eta = 0{,}15$ (°C) | une liste de 5 nombres |
| d | $\mathrm{VT}$ après ce pas (°C²) | un nombre (2 décimales) |
| e | le pas critique $\eta^\star = 1/\lambda_{\max}(\mathbf{L})$ de cette barre | un nombre (4 décimales) |
| f | la variation totale au carré, puis la variation totale en valeur absolue, d'une marche de $h = 6$ °C étalée régulièrement sur $n = 4$ pas | une liste de 2 nombres |
| g | le plus petit nombre de pas $n$ pour lequel cette marche de 6 °C a une variation totale au carré inférieure à 1 °C² | un entier |

Dans ta copie : écris $\mathbf{L}$ ($5 \times 5$) et vérifie $\mathbf{x}^\top\mathbf{L}\mathbf{x} = \mathrm{VT}(\mathbf{x})$ ; vérifie que la somme des coordonnées de $\mathbf{L}\mathbf{x}$ est nulle, et déduis-en que la moyenne des températures ne change pas au pas c) ; écris la nouvelle valeur d'une case intérieure comme une moyenne pondérée de la case et de ses deux voisines, et dis pour quels $\eta$ les poids sont positifs ; vérifie la formule admise pour $n = 3$, en calculant à la main les valeurs propres du laplacien d'une barre de trois cases ; dis ce qui arrive à la descente au-delà de $\eta^\star$ ; dis laquelle des deux variations totales de f) garde un bord net quand les mesures en montrent un.

### Ex M28.5 — Des étoffes rayées : période, fréquence, fréquence de Nyquist, repliement, variation totale rapportée à l'énergie 4 sin²(ω/2), et gain d'une moyenne mobile ✏️ ★★ ⏱️ 25 min
**Objectif :** lire la fréquence et la période d'un motif, en dimension 1 et 2, situer la fréquence de Nyquist et le repliement, et calculer ce qu'en font la variation totale et un flou.
**Prérequis :** fiche §4 ; R9, M21 · **Parcours :** C, E

Une manufacture relève ses étoffes rayées au scanner, une valeur par case d'une grille de $36 \times 36$ cases, $i$ la ligne et $j$ la colonne. Pour éviter les bords, on traite la grille comme **refermée** dans les deux directions (la case 35 est voisine de la case 0, le long des lignes comme le long des colonnes) : les relations de la fiche y sont exactes. Sur l'étoffe réelle, à bords libres, elles ne valent qu'aux cases qui ne touchent pas le bord, et les rapports ne sont qu'approchés. Trois motifs :
- A : $x_{ij} = \cos\frac{2\pi j}{6}$, des rayures de période 6 cases le long des lignes ;
- B : $x_{ij} = \cos\frac{2\pi j}{12}$ ;
- C : $x_{ij} = \cos\big(2\pi(\frac{i}{12} + \frac{j}{6})\big)$, des rayures obliques.

| | Question | Réponse attendue |
|---|---|---|
| a | le rapport $\mathrm{VT}(\mathbf{x})/\lVert\mathbf{x}\rVert^2$ de A, puis de B | une liste de 2 nombres (3 décimales) |
| b | le gain de la moyenne mobile de trois cases le long des lignes, pour A, puis pour B | une liste de 2 nombres (4 décimales) |
| c | la période de C, mesurée dans la direction $(f_1, f_2)$ de ses fréquences (en cases) | un nombre (2 décimales) |
| d | le rapport $\mathrm{VT}(\mathbf{x})/\lVert\mathbf{x}\rVert^2$ de C | un nombre (3 décimales) |
| e | le gain du flou $3 \times 3$ (la moyenne des neuf cases autour d'une case) sur C | un nombre (3 décimales) |
| f | un fil de l'étoffe varie avec une fréquence de $\frac{11}{12}$ de cycle par case ; relevé une fois par case, il ressemble à un motif de quelle période (en cases) ? | un nombre |

Dans ta copie : donne $f$ et $\omega$ pour A et B, et vérifie que leurs périodes divisent 36 (sinon, le motif ne se refermerait pas sur la grille) ; compare le rapport de B à $\omega^2$, et dis pourquoi ils sont proches ; donne la fréquence de Nyquist et la plus petite période sans repliement ; pour C, donne $(f_1, f_2)$ et la direction perpendiculaire aux rayures ; justifie e) par les gains le long des lignes et le long des colonnes ; dis lequel des trois motifs le flou atténue le plus ; pour f), dis sur quelle fréquence de $[0, \frac12]$ se replie $\frac{11}{12}$, et pourquoi le scanner ne peut pas faire la différence.

### Ex M28.6 — La prévision d'un météorologue en six catégories : la refroidir, garder les trois plus probables, garder le plus petit ensemble de masse donnée, et le coût de chaque troncature ✏️ ★★ ⏱️ 25 min
**Objectif :** tempérer une loi catégorielle, la tronquer par un top-k et par un top-p, calculer et comparer le coût des deux troncatures, et trouver les seuils d'un top-p qui gardent un nombre d'issues donné.
**Prérequis :** fiche §5 ; M03, M06 · **Parcours :** C, E

Pour demain après-midi, un météorologue donne sa prévision en six catégories, numérotées de 0 à 5 (0 grand soleil, 1 éclaircies, 2 nuageux, 3 averses, 4 pluie continue, 5 orage) :
$$\mathbf{p} = (0{,}04 ;\ 0{,}19 ;\ 0{,}33 ;\ 0{,}26 ;\ 0{,}10 ;\ 0{,}08).$$
Pour un bulletin plus tranché, la station la refroidit à $T = \frac13$ ; pour une carte simplifiée, elle ne garde que quelques catégories, avec la loi conditionnelle.

| | Question | Réponse attendue |
|---|---|---|
| a | la loi refroidie $\mathbf{p}^{(1/3)}$, dans l'ordre des catégories 0 à 5 | une liste de 6 nombres (3 décimales) |
| b | la loi du top-3 de $\mathbf{p}$, $\mathbf{p}_S$, dans l'ordre des catégories 0 à 5 | une liste de 6 nombres (4 décimales) |
| c | $\mathrm{KL}(\mathbf{p}_S \,\|\, \mathbf{p})$, puis $\frac12\lVert\mathbf{p}_S - \mathbf{p}\rVert_1$, pour ce top-3 | une liste de 2 nombres (4 décimales) |
| d | l'ensemble gardé par le top-p de $\mathbf{p}$ de seuil $m = 0{,}87$, par probabilité décroissante | une liste d'entiers |
| e | $\mathrm{KL}(\mathbf{p}_S \,\|\, \mathbf{p})$, puis $\frac12\lVert\mathbf{p}_S - \mathbf{p}\rVert_1$, pour ce top-p | une liste de 2 nombres (4 décimales) |
| f | l'intervalle des seuils $m \in\ ]0, 1]$ pour lesquels le top-p de $\mathbf{p}$ garde exactement trois catégories | un intervalle entre guillemets |

Dans ta copie : écris les six cubes et leur somme ; dis pourquoi le top-3 de la loi refroidie garde les mêmes catégories que celui de $\mathbf{p}$ ; vérifie la divergence KL de c) par la somme $\sum_ip_{S,i}\ln\frac{p_{S,i}}{p_i}$, pas seulement par la formule de la fiche ; dis pourquoi $\mathrm{KL}(\mathbf{p} \,\|\, \mathbf{p}_S)$ est infinie ; compare les coûts de c) et de e), et dis d'où vient l'écart ; dis combien de catégories garde le top-p de seuil 0,87 de la loi refroidie, et en quoi c'est cohérent avec la fiche.

### Ex M28.7 — Les décimales de a/n et l'itération x ↦ x² + c modulo n : prépériode et période à la main, et la borne du principe des tiroirs ✏️ ★ ⏱️ 15 min
**Objectif :** trouver à la main la prépériode et la période d'une suite dans un ensemble fini, et appliquer la borne $\mu + \lambda \le N$.
**Prérequis :** fiche §6 ; R0 (division euclidienne), M16 · **Parcours :** C, E

Les décimales de $\frac an$, pour $1 \le a < n$, s'obtiennent par la division posée : avec $r_0 = a$, chaque pas écrit le chiffre $\lfloor 10r_t/n\rfloor$ et garde le reste $r_{t+1} = 10r_t \bmod n$. La suite des restes vit dans $\{0, \ldots, n - 1\}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $[\mu, \lambda]$ pour la suite des restes de $\frac{5}{26}$ | une liste de 2 entiers |
| b | $[\mu, \lambda]$ pour la suite $u_{t+1} = (u_t^2 + 2) \bmod 17$, depuis $u_0 = 0$ | une liste de 2 entiers |
| c | vrai ou faux : pour toute fraction $\frac an$ avec $1 \le a < n$, la période de la suite des restes est au plus $n - 1$ | `True` ou `False` |

Dans ta copie : écris les restes et les chiffres de $\frac{5}{26}$ jusqu'à la première répétition d'un reste, puis le développement décimal avec sa partie périodique ; écris les termes de b) jusqu'à la première répétition, et donne les indices $i < j$ de la fiche ; vérifie $\mu + \lambda \le N$ dans les deux cas, en disant ce que vaut $N$ ; justifie c), en traitant à part le cas où un reste nul apparaît ; pour aller plus loin, montre qu'en b), dès $u_1$, la suite ne prend que des valeurs de la forme $x^2 + 2 \bmod 17$, qui sont au plus 9, et déduis-en $\mu + \lambda \le 10$ quel que soit $u_0$.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M28.8 — Deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie ∂ ★★★ ⏱️ 30 min
**Objectif :** démontrer la réciproque énoncée au §2 : la matrice de Gram détermine une famille de vecteurs à une transformation orthogonale près.
**Prérequis :** fiche §2 ; M12a (application linéaire, dimension), M12b (bases orthonormées, Gram-Schmidt, matrices orthogonales) · **Parcours :** C

$\mathbf{x}_1, \ldots, \mathbf{x}_n$ et $\mathbf{y}_1, \ldots, \mathbf{y}_n$ sont deux familles de vecteurs de $\mathbb{R}^d$ telles que $\mathbf{x}_i^\top\mathbf{x}_j = \mathbf{y}_i^\top\mathbf{y}_j$ pour tous $i, j$ ; $U$ est le sous-espace engendré par les $\mathbf{x}_i$, $V$ celui des $\mathbf{y}_i$.
1. Montre que, pour tous réels $a_1, \ldots, a_n$, $\big\lVert\sum_ia_i\mathbf{x}_i\big\rVert^2 = \big\lVert\sum_ia_i\mathbf{y}_i\big\rVert^2$. Déduis-en que $\sum_ia_i\mathbf{x}_i = \mathbf{0}$ si et seulement si $\sum_ia_i\mathbf{y}_i = \mathbf{0}$.
2. On pose $T\big(\sum_ia_i\mathbf{x}_i\big) = \sum_ia_i\mathbf{y}_i$. Montre que $T$ est bien définie sur $U$ (le résultat ne dépend pas des coefficients choisis pour écrire un même vecteur), qu'elle est linéaire, qu'elle conserve la norme, puis le produit scalaire, et que $T(\mathbf{x}_i) = \mathbf{y}_i$.
3. Montre que $T$ est une bijection de $U$ sur $V$, et que $\dim U = \dim V$.
4. Soit $r = \dim U$ et $(\mathbf{e}_1, \ldots, \mathbf{e}_r)$ une base orthonormée de $U$. Montre que $(T\mathbf{e}_1, \ldots, T\mathbf{e}_r)$ est une base orthonormée de $V$. Complète chacune en une base orthonormée de $\mathbb{R}^d$ (M12b), et définis $\mathbf{R}$ par $\mathbf{R}\mathbf{e}_k = \mathbf{f}_k$ pour $k = 1, \ldots, d$, où $\mathbf{f}_k = T\mathbf{e}_k$ pour $k \le r$. Montre que $\mathbf{R}$ est orthogonale et que $\mathbf{R}\mathbf{x}_i = \mathbf{y}_i$ pour tout $i$.
5. Deux nuages de $n$ points de $\mathbb{R}^d$ ont les mêmes distances deux à deux. Déduis de 4 et du double centrage (fiche §2) qu'il existe $\mathbf{R}$ orthogonale et $\mathbf{t} \in \mathbb{R}^d$ tels que l'un s'obtient à partir de l'autre par $\mathbf{x} \mapsto \mathbf{R}\mathbf{x} + \mathbf{t}$.

### Ex M28.9 — Le maximum d'une fonction convexe sur un pavé est atteint en un sommet ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer la propriété du §3, coordonnée par coordonnée, et voir ce qu'elle ne dit pas.
**Prérequis :** fiche §3 ; M05a, M10 (fonctions convexes) · **Parcours :** C

$f$ est une fonction convexe et continue sur le pavé $P = [l_1, u_1] \times \cdots \times [l_n, u_n]$, avec $l_k < u_k$ ; un **sommet** de $P$ est un point dont chaque coordonnée vaut $l_k$ ou $u_k$.
1. On fixe $\mathbf{x} \in P$ et une coordonnée $k$, et l'on pose $\varphi(t) = f(\mathbf{x}$ où la $k$-ième coordonnée est remplacée par $t)$, pour $t \in [l_k, u_k]$. Montre que $\varphi$ est convexe, puis que $\varphi(t) \le \max\big(\varphi(l_k), \varphi(u_k)\big)$ pour tout $t$ de $[l_k, u_k]$.
2. Déduis-en que, pour tout $\mathbf{x} \in P$, il existe un sommet $\mathbf{v}$ tel que $f(\mathbf{v}) \ge f(\mathbf{x})$ (traite les coordonnées l'une après l'autre).
3. Conclus : le maximum de $f$ sur $P$ existe, et il est atteint en au moins un sommet ; il suffit de comparer les $2^n$ sommets.
4. Donne une fonction convexe dont le maximum sur $[0, 1]^2$ est atteint aussi en un point qui n'est pas un sommet, puis une fonction concave dont le maximum sur $[0, 1]^2$ n'est atteint en aucun sommet. Pourquoi une montée projetée sur une fonction convexe peut-elle s'arrêter sur un sommet qui n'est pas le maximum ?

### Ex M28.10 — Les issues les plus probables, prises jusqu'à atteindre la masse p, forment un plus petit ensemble de masse au moins p, et la loi tronquée est à −ln P(S) de la loi de départ en divergence KL ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer la propriété du top-p par un argument d'échange, puis calculer le coût d'une troncature.
**Prérequis :** fiche §5 ; M03, M06 · **Parcours :** C, E

$\mathbf{p}$ est une loi sur $K$ issues ; on range ses issues par probabilité décroissante (entre deux probabilités égales, la plus petite issue d'abord), $p_{(1)} \ge p_{(2)} \ge \cdots \ge p_{(K)}$ ; pour un seuil $m \in\ ]0, 1]$ (la lettre $p$ du titre), $k^\star$ est le plus petit $k$ tel que $p_{(1)} + \cdots + p_{(k)} \ge m$, et $S^\star$ est l'ensemble des $k^\star$ premières issues. Pour un ensemble $A$ d'issues, $P(A) = \sum_{i \in A}p_i$.
1. Montre que tout ensemble $A$ de $j$ issues vérifie $P(A) \le p_{(1)} + \cdots + p_{(j)}$.
2. Déduis-en qu'aucun ensemble de moins de $k^\star$ issues n'a une masse au moins $m$, et que $S^\star$ est un plus petit ensemble de masse au moins $m$.
3. Montre que, parmi les ensembles de $k^\star$ issues, $S^\star$ a la plus grande masse, par un argument d'échange : si un ensemble $A$ de $k^\star$ issues n'est pas $S^\star$, échange une issue de $A$ hors de $S^\star$ contre une issue de $S^\star$ hors de $A$, et regarde ce que devient la masse.
4. Soit $S$ un ensemble de masse $P(S) > 0$, et $\mathbf{p}_S$ la loi conditionnelle sachant $S$. Montre que $\mathrm{KL}(\mathbf{p}_S \,\|\, \mathbf{p}) = -\ln P(S)$.
5. Déduis de 3 et 4 qu'un top-p de seuil $m$ coûte au plus $-\ln m$ en divergence KL, et que, parmi les ensembles de $k^\star$ issues de masse au moins $m$, $S^\star$ est le moins coûteux.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M28.11 — Pont : diviser des scores par T avant la softmax, ou élever les probabilités à la puissance 1/T, la même loi ; et le même top-k 🔗 ★ ⏱️ 15 min
**Objectif :** relier la température sur des scores, telle que workbookIA l'applique, à la température sur des probabilités de la fiche, et voir ce qu'elle fait à un top-k.
**Prérequis :** fiche §5 ; M17 (softmax, loi de Boltzmann) · **Parcours :** C, E

Un classifieur reconnaît cinq espèces d'arbres sur la photo d'une feuille, numérotées de 0 à 4 (0 chêne, 1 hêtre, 2 érable, 3 tilleul, 4 frêne). Pour une photo, il sort les scores $\mathbf{z} = (1{,}1 ;\ 2{,}4 ;\ 0{,}1 ;\ 2{,}1 ;\ -0{,}5)$ et les probabilités $\mathbf{p} = \operatorname{softmax}(\mathbf{z})$. L'application de terrain ne reçoit que $\mathbf{p}$. Un collègue, qui a les scores, propose d'adoucir la loi en les divisant par $T = 3$ avant la softmax.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{p} = \operatorname{softmax}(\mathbf{z})$, dans l'ordre des espèces 0 à 4 | une liste de 5 nombres (4 décimales) |
| b | $\operatorname{softmax}(\mathbf{z}/3)$ | une liste de 5 nombres (4 décimales) |
| c | la loi du top-3 à $T = 3$, calculée à partir de $\mathbf{p}$ seul | une liste de 5 nombres (4 décimales) |
| d | vrai ou faux : pour tout $T > 0$, le top-3 de $\operatorname{softmax}(\mathbf{z}/T)$ garde les mêmes trois espèces | `True` ou `False` |
| e | vrai ou faux : pour un top-k, tronquer puis tempérer donne la même loi que tempérer puis tronquer | `True` ou `False` |

Dans ta copie : montre, pour des scores et un $T > 0$ quelconques, que $\operatorname{softmax}(\mathbf{z}/T)_i = p_i^{1/T}\big/\sum_jp_j^{1/T}$, en écrivant $p_i = e^{z_i}/\sum_je^{z_j}$ ; calcule $\mathbf{p}^{(3)}$ à partir de ta réponse a), et compare-la à b) : l'application n'a pas besoin des scores ; justifie d) et e) ; dis si la température peut changer l'ensemble gardé par un top-p, et pourquoi.

### Ex M28.12 — Expliquer avec une structure de barres rigides ce que la matrice de Gram d'une famille de vecteurs fixe, et ce qu'elle laisse libre 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule ce qu'une matrice de Gram connaît d'une famille de vecteurs, et ce qu'elle ignore.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

Un ami charpentier a lu qu'« une matrice de Gram fixe une famille de vecteurs à une isométrie près », et te demande ce que cela veut dire.

Réponds-lui en 6 à 10 phrases, sans formule, avec une structure de barres rigides qui partent toutes d'un même nœud, chacune représentant un vecteur : ce que connaît la matrice de Gram (les longueurs des barres, les angles entre elles) ; ce que cela fixe (la forme de la structure, donc les écarts entre les bouts des barres) ; ce que cela laisse libre (tourner la structure autour de son nœud, la retourner en miroir) ; ce que l'on perd en plus si l'on ne connaît que les écarts entre les bouts des barres, sans le nœud ; et pourquoi deux structures qui ont les mêmes longueurs et les mêmes angles se superposent. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M28.E1 — « Que perd-on, en divergence KL, à ne garder que les issues les plus probables d'une loi avant de tirer ? » 💼 ★ ⏱️ 10 min
*Fiche §5 · parcours C*

« Que perd-on, en divergence KL, à ne garder que les issues les plus probables d'une loi avant de tirer ? »

Ta réponse doit dire ce qu'est la loi tronquée (la loi conditionnelle sachant l'ensemble gardé $S$), ce que vaut $\mathrm{KL}(\mathbf{p}_S \,\|\, \mathbf{p})$ ($-\ln P(S)$, qui ne dépend que de la masse gardée), la borne qu'en tire un top-p de seuil $m$ ($-\ln m$), ce que vaut la divergence dans l'autre sens et pourquoi (infinie : des issues possibles deviennent impossibles), ce que dit la distance en variation totale ($1 - P(S)$), et un exemple chiffré.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m28_gram_echantillonnage/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M28.13 | Une configuration de points de matrice de Gram donnée, par le théorème spectral · `points_from_gram` | 🔨 | ★★ | 25 | C |
| M28.14 | Tempérer une loi donnée par ses probabilités, et le plus petit ensemble de masse donnée · `temper`, `smallest_mass_set` | 🔨 | ★★ | 30 | C, E |
| M28.15 | Prédire ce que deviennent un pas η∇f et un pas normalisé quand la fonction est multipliée par 1 000, puis vérifier | 🔮 | ★ | 15 | C, E |
| M28.16 | Des motifs rayés de fréquence croissante jusqu'au damier : leur variation totale, et ce qu'en laissent un flou 3 × 3 et dix pas de descente sur la variation totale | 🎨 | ★ | 20 | C, E |
| M28.17 | Chasse à l'erreur : un double centrage fait sur les distances au lieu de leurs carrés, une montée qui coupe le gradient au lieu du point, une prépériode comptée dans la période | 🐛 | ★ | 20 | C, E |
| M28.18 | Un test de propriété : la configuration rendue redonne la matrice de Gram et les distances, pour des points tirés au hasard | 🛠️ | ★ | 15 | C |
| M28.19 | Défi : redessiner la carte de 30 villes quand un quart des distances manquent, à moins de 1 km en moyenne après alignement | 🏆 | ★★★ | 30 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les deux 🔨 complètent ta copie `mon_travail/mymath/sampling.py` (**mymath :** `sampling.py`), dont la docstring du module dit ce qui est permis : NumPy, mais de `np.linalg` seulement `eigh` (dans `points_from_gram`), et aucune fonction de SciPy ni de scikit-learn (`scipy.special.softmax` donnerait `temper`) ; des probabilités, jamais des scores ; rien n'est tiré au hasard ; ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de ses fonctions dans `tests/test_m28_sampling.py`, puis s'en sert ; dans le notebook, tu les appelles par `mymath.sampling.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier (les balises, le losange, la prévision du météorologue) sont recopiées dans une cellule du notebook.

**M28.13 · 🔨 `points_from_gram(G, dim=None, tol=1e-9)`.** Écris la fonction, en suivant sa docstring : contrôle `G` (une matrice carrée non vide de nombres finis, symétrique au seuil $s = \texttt{tol}\cdot\max(1, \max\lvert G_{ij}\rvert)$ près), `dim` (un entier entre 1 et $n$, pas un booléen) et `tol` ($\ge 0$) ; diagonalise par `np.linalg.eigh`, qui range les valeurs propres par ordre **croissant** (retourne l'ordre) ; refuse une valeur propre sous $-s$ (une `ValueError` : $\mathbf{G}$ n'est pas une matrice de Gram) ; compte comme nulles celles de $[-s, s]$ ; garde `dim` colonnes, par défaut autant que de valeurs propres $> s$ (au moins une) ; multiplie chaque vecteur propre unitaire par la racine de sa valeur propre ; puis rends positive, dans chaque colonne, la première coordonnée de valeur absolue $> 10^{-8}$ ; rends un tableau de flottants de forme $(n, \texttt{dim})$. Lance le groupe de tests. Ensuite : a) le losange de M28.2 : forme $\mathbf{G} = -\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ à partir des distances, puis la carte, à comparer à ta réponse d) ; b) les balises de M28.1 : la carte $\mathbf{Y}$ rendue pour $\mathbf{G} = \mathbf{X}\mathbf{X}^\top$, le plus grand écart $\max\lvert\mathbf{Y}\mathbf{Y}^\top - \mathbf{G}\rvert$, puis la matrice $\mathbf{R}$, de forme $(2, 2)$, telle que $\mathbf{y}_i = \mathbf{R}\mathbf{x}_i$ pour les quatre balises ($\mathbf{R} = \mathbf{Y}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}$), son déterminant, et vrai ou faux : $\mathbf{R}$ est orthogonale ; c) le losange avec $\mathrm{AC} = 50$ km (M28.2 e)) : ce que fait ta fonction, et la plus petite valeur propre de $-\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ (par `np.linalg.eigvalsh`, hors de `mymath`) ; d) le losange avec `dim=1` : la carte à une colonne, et $\lVert\mathbf{G} - \mathbf{X}\mathbf{X}^\top\rVert_F$. Ce qu'il faut observer : la carte ne retrouve les vraies positions qu'à une isométrie près, ici une symétrie ($\det\mathbf{R} = -1$) ; des distances impossibles donnent une valeur propre négative, que la fonction refuse ; une colonne de moins, c'est la meilleure matrice de Gram de rang 1 (Eckart-Young), à une distance égale à la valeur propre laissée de côté.

**M28.14 · 🔨 `temper(p, temperature)` et `smallest_mass_set(p, mass)`.** Écris les deux fonctions, en suivant leurs docstrings. `temper` : contrôle la loi (1-D, non vide, des nombres finis $\ge 0$ de somme 1 à $10^{-9}$ près) et la température ($\ge 0$, `np.inf` permis, ni `nan` ni booléen) ; traite d'abord $T = 0$ (la loi uniforme sur les issues les plus probables) et $T = \infty$ (la loi uniforme sur les issues de probabilité non nulle) ; sinon, calcule par les logarithmes des seuls $p_i > 0$, moins leur maximum, divisés par $T$, puis l'exponentielle et la division par la somme, et laisse les zéros à 0. `smallest_mass_set` : contrôle la loi et la masse ($0 < \texttt{mass} \le 1$) ; range les issues par probabilité décroissante avec un tri **stable** (`np.argsort(-p, kind="stable")` : à égalité, la plus petite issue d'abord) ; cumule jusqu'à ce que le total atteigne `mass` $- 10^{-9}$ ; rends les indices gardés, dans cet ordre, en tableau d'entiers. Lance les deux groupes de tests. Ensuite : a) la prévision de M28.6 : `temper(p, 1/3)` et `smallest_mass_set(p, 0.87)`, à comparer à tes réponses a) et d) ; b) pour $\mathbf{q} = (0{,}3 ;\ 0 ;\ 0{,}3 ;\ 0{,}25 ;\ 0{,}15)$ : `temper(q, 0)` et `temper(q, np.inf)` ; c) pour la prévision de M28.6, la liste des tailles de l'ensemble du top-p de seuil 0,87 de la loi tempérée, pour $T = \frac13$, 1, 3 et $\infty$, dans cet ordre ; d) les entropies, en nats, de la prévision tempérée à $T = \frac13$, 1 et 3 (calculées hors de `mymath`, sans compter les issues de probabilité nulle), et vrai ou faux : elles croissent. Ce qu'il faut observer : refroidir rétrécit l'ensemble du top-p, réchauffer l'agrandit ; à $T = \infty$, les zéros restent nuls ; l'entropie croît avec $T$ vers $\ln 6$.

**M28.15 · 🔮 Prédire ce que deviennent un pas η∇f et un pas normalisé quand la fonction est multipliée par 1 000.** Deux réglages $\mathbf{x} \in [0, 1]^2$ commandent un capteur, dont le signal $f(\mathbf{x}) = -\lVert\mathbf{x} - \mathbf{c}\rVert^2$, en watts, est maximal en $\mathbf{c} = (0{,}33 ;\ 0{,}58)$, à l'intérieur du pavé. On fait 20 pas de montée projetée, $\mathbf{x}_{t+1} = \operatorname{clip}(\mathbf{x}_t + \eta\,\mathbf{s}_t,\ 0,\ 1)$, de pas $\eta = 0{,}08$, depuis $\mathbf{x}_0 = (0{,}83 ;\ 0{,}13)$, avec le pas ordinaire $\mathbf{s}_t = \nabla f(\mathbf{x}_t)$ ou le pas normalisé $\mathbf{s}_t = \nabla f(\mathbf{x}_t)/\lVert\nabla f(\mathbf{x}_t)\rVert$. Puis on exprime le signal en milliwatts : la fonction devient $1\,000f$, et l'on recommence avec le même $\eta$. **Avant d'exécuter**, prédis : a) avec $1\,000f$ et le pas ordinaire, les itérés : (A) vont au maximum, plus vite qu'avec $f$ ; (B) s'arrêtent sur un sommet du pavé et y restent ; (C) sautent d'un sommet à un autre sans jamais s'arrêter ; (D) sortent du pavé ; b) le point $\mathbf{x}_1$ avec $1\,000f$ et le pas ordinaire (une liste de 2 nombres, que tu calcules à la main) ; c) avec le pas normalisé, les itérés de $1\,000f$ : (A) sont ceux de $f$ ; (B) font des pas 1 000 fois plus longs ; d) avec le pas normalisé, le premier pas $k$ où $\lVert\mathbf{x}_k - \mathbf{c}\rVert < 0{,}1$ (un entier). Puis écris `ascent_15(scale, normalized, n_steps=20)`, qui rend le tableau des itérés, de forme $(\texttt{n\_steps} + 1, 2)$, ligne 0 le départ, pour la fonction $\texttt{scale}\cdot f$ ; la vérification l'essaie aussi sur un départ caché. Relève : e) les distances $\lVert\mathbf{x}_{20} - \mathbf{c}\rVert$ des quatre montées, dans l'ordre ($f$, pas ordinaire), ($1\,000f$, pas ordinaire), ($f$, pas normalisé), ($1\,000f$, pas normalisé) (4 décimales) ; f) vrai ou faux : avec le pas normalisé, les 21 itérés de $f$ et de $1\,000f$ sont les mêmes. Ce qu'il faut observer : multiplier la fonction par 1 000 multiplie le pas ordinaire par 1 000, et la projection transforme ces sauts démesurés en allers-retours entre deux sommets, alors que le maximum est à l'intérieur ; le pas normalisé ne voit pas l'unité, mais, de longueur fixe, il oscille près du maximum sans s'y poser.

**M28.16 · 🎨 Des motifs rayés jusqu'au damier, un flou 3 × 3 et dix pas de descente.** Sur une grille de $48 \times 48$ cases à **bords libres** (une case du bord a moins de quatre voisines), cinq motifs : A $\cos\frac{2\pi j}{16}$, B $\cos\frac{2\pi j}{6}$, C $\cos\frac{2\pi j}{3}$, D $(-1)^j$ et E $(-1)^{i+j}$, le damier. Le notebook fournit `blur3_16(x)`, la moyenne des neuf cases autour de chaque case intérieure (un tableau $46 \times 46$). Écris `grid_laplacian_16(x)`, qui rend $\mathbf{L}\mathbf{x}$ pour la grille à bords libres (en chaque case, son nombre de voisines fois sa valeur, moins la somme de ses voisines ; sans boucle sur les cases), puis `draw_stripes_16(axes, motifs, eta, n_steps)`, qui reçoit une grille d'axes de forme $(5, 3)$ et, pour chaque motif (une ligne d'axes), dessine (`imshow`, une même échelle de couleurs de $-1$ à 1 pour les trois images) le motif, son flou, et la grille après `n_steps` pas de descente $\mathbf{x} \leftarrow \mathbf{x} - \eta\cdot 2\mathbf{L}\mathbf{x}$ ; chaque image a un titre qui donne la valeur mesurée. La fonction rend un dictionnaire de trois listes, dans l'ordre des motifs : `"ratio"`, $\mathrm{VT}(\mathbf{x})/\lVert\mathbf{x}\rVert^2$ sur toute la grille (avec $\mathrm{VT}(\mathbf{x}) = \mathbf{x}^\top\mathbf{L}\mathbf{x}$) ; `"gain"`, $\langle\text{flou}, \mathbf{x}_{\text{int}}\rangle/\lVert\mathbf{x}_{\text{int}}\rVert^2$, où $\mathbf{x}_{\text{int}}$ est le motif sur les cases intérieures ; `"decay"`, $\lVert\mathbf{y}_c\rVert/\lVert\mathbf{x}_c\rVert$ après les pas de descente, sur le bloc central `[12:36, 12:36]`. Écris aussi `draw_decay_curve_16(ax, eta, n_steps, freqs, decays)`, qui trace la courbe $\big(1 - 8\eta\sin^2(\pi f)\big)^{n}$ pour $f$ de 0 à $\frac12$, et place les points mesurés des rayures A à D (`freqs` $= (\frac{1}{16}, \frac16, \frac13, \frac12)$), avec une échelle logarithmique en ordonnée, des noms d'axes, et en titre la valeur théorique du damier, $(1 - 16\eta)^{n}$. La vérification appelle les deux fonctions avec $\eta = 0{,}05$ et 10 pas, affiche les figures, et compare tes trois listes à celles de la référence. Relève : a) les cinq rapports (3 décimales) ; b) les cinq gains (4 décimales) ; c) le logarithme décimal des cinq atténuations (2 décimales) ; d) vrai ou faux : les rapports mesurés sont un peu sous les valeurs $4\sin^2(\pi f)$ (et 8 pour le damier) de la grille refermée ; e) vrai ou faux : sur le bloc central, les atténuations sont exactement celles de la courbe pour A à D, et la valeur du titre pour le damier. Ce qu'il faut observer : plus le motif est rapide, plus il coûte en variation totale et plus le flou et la descente l'effacent ; le flou rend la période 3 nulle et le damier divisé par 9 ; sur une grille à bords libres, les cases du bord ont moins de voisines, ce qui fait baisser les rapports ; mais un pas ne mélange que des voisines, et, après 10 pas, une case à plus de 10 cases du bord n'a pas encore « vu » le bord : au centre, la courbe est exacte.

**M28.17 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `map_from_distances(D, dim=2)` doit rendre une carte (une ligne par lieu) dont les distances sont celles de la matrice `D` ; elle forme $\mathbf{J}$, calcule `G = -0.5 * J @ D @ J`, puis rend `points_from_gram(G, dim)`. Il l'a vérifiée sur un triangle équilatéral de côté 1 : les trois distances de la carte valent 1.
- (2) `tune_emitters(x0, grad, eta=0.05, n_steps=120, lower=0.0, upper=1.0)` doit faire `n_steps` pas de montée projetée sur le pavé $[\texttt{lower}, \texttt{upper}]^n$, le gradient étant donné par la fonction `grad` ; elle répète `x = x + eta * np.clip(grad(x), lower, upper)`. Il l'a vérifiée sur $f(\mathbf{x}) = -\lVert\mathbf{x} - \mathbf{c}\rVert^2$ avec $\mathbf{c} = (0{,}45 ;\ 0{,}62 ;\ 0{,}88)$, depuis $(0{,}15 ;\ 0{,}25 ;\ 0{,}05)$, avec les réglages par défaut : la montée arrive en $\mathbf{c}$, à $10^{-5}$ près, à l'intérieur du pavé $[0, 1]^3$.
- (3) `cycle_of(f, x0)` doit rendre `(mu, lam)`, la prépériode et la période de la suite $u_{t+1} = f(u_t)$ ; elle note dans un dictionnaire l'indice où chaque valeur apparaît, et, à la première valeur déjà vue, d'indice $j$, rend l'indice $i$ de sa première apparition et `j`. Il l'a vérifiée sur $x \mapsto (x + 3) \bmod 10$ depuis 0 : `(0, 10)`.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `map_from_distances_fixed`, `tune_emitters_fixed` et `cycle_of_fixed`, avec les mêmes arguments), puis réponds : a) pour le losange de M28.2, les distances AB, AC et BD de la carte de `map_from_distances_fixed`, puis de celle de `map_from_distances` ; b) pour quatre émetteurs, $f(\mathbf{x}) = -\lVert\mathbf{x} - \mathbf{c}\rVert^2$ avec $\mathbf{c} = (1{,}3 ;\ -0{,}2 ;\ 0{,}6 ;\ 0{,}35)$, depuis $\mathbf{x}_0 = (0{,}2 ;\ 0{,}7 ;\ 0{,}78 ;\ 0{,}1)$, avec les réglages par défaut : le réglage final de `tune_emitters_fixed`, puis celui de `tune_emitters` ; c) pour le générateur jouet $x \mapsto (x^2 + 3) \bmod 22$, depuis 2 : `cycle_of_fixed`, puis `cycle_of`. Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés.

**M28.18 · 🛠️ Un test de propriété.** Écris `gram_property_test_18(n_trials, rng, func=None, rtol=1e-9)` ; quand `func` vaut `None`, le test prend `mymath.sampling.points_from_gram` **au moment de l'appel**. Pour chacun des `n_trials` essais, dans cet ordre : `n = int(rng.integers(2, 9))`, `d = int(rng.integers(1, 5))`, `scale = 10.0 ** rng.uniform(-2, 3)`, `P = scale * rng.standard_normal((n, d))`, puis, si `rng.random() < 0.3`, `P[-1] = P[0]` (un point répété), puis `t = scale * rng.standard_normal(d)` ; ensuite `G = P @ P.T`, $s = \max(1, \max\lvert G_{ij}\rvert)$ et `X = func(G)`. La fonction rend un dictionnaire de quatre compteurs d'essais : `"shape"`, si `X` n'a pas la forme $(n, r)$, avec $r$ le rang de `P` (`np.linalg.matrix_rank`), ou contient un nombre non fini ; `"gram"`, si $\max\lvert\mathbf{X}\mathbf{X}^\top - \mathbf{G}\rvert > \texttt{rtol}\cdot s$ (ou `X` non fini) ; `"distances"`, si les carrés des distances des lignes de `X` s'écartent de ceux de `P` de plus de $4\,\texttt{rtol}\cdot s$ (ou `X` non fini) ; `"translation"`, si la carte `func(Gc)` de la matrice doublement centrée `Gc` $= -\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ des points translatés `P + t` a des carrés de distances qui s'écartent de ceux de `P` de plus de $4\,\texttt{rtol}\cdot\max(1, \max\lvert(\mathbf{G}_c)_{ij}\rvert)$ (ou n'est pas finie). Les carrés des distances se calculent dans le test, avec NumPy, sans appeler `mymath`. Le notebook fournit cinq versions fausses de `points_from_gram` : `no_sqrt` (les colonnes $\lambda_k\mathbf{q}_k$), `ascending` (l'ordre croissant de `eigh`, non retourné), `all_columns` ($n$ colonnes, sans mettre à 0 les petites valeurs propres : la racine d'une valeur propre de $-10^{-15}$ donne `nan`), `rotated` (la bonne carte, tournée) et `no_sign` (la bonne carte, sans la convention de signe). a) Pourquoi une tolérance relative à $s$ ? Combien de fois sur 300 essais une tolérance absolue de $10^{-9}$ sur $\mathbf{X}\mathbf{X}^\top - \mathbf{G}$ refuserait-elle la bonne fonction (avec `np.random.default_rng(6618)`) ? b) Avec `rng = np.random.default_rng(6618)` et 300 essais, avec ta fonction : vrai ou faux, les quatre compteurs sont nuls ; c) avec le même départ et chacune des cinq versions fausses : les quatre compteurs (un nouveau `default_rng(6618)` chaque fois, dans l'ordre `no_sqrt`, `ascending`, `all_columns`, `rotated`, `no_sign`) ; d) lesquelles passent le test, et pourquoi c'est normal : qu'est-ce qui, dans le dépôt, vérifie ce qu'elles ont de faux ? Pourquoi `ascending` n'est-elle attrapée que par une partie des essais ? La vérification compare aussi tes compteurs à ceux de la référence sur deux départs cachés, et remplace un instant `mymath.sampling.points_from_gram` par une version fausse : tes compteurs doivent alors compter. Ce qu'il faut retenir : ce test ajoute à ceux de `tests/test_m28_sampling.py` des points répétés et une translation suivie d'un double centrage ; il attrape trois versions fausses, et ne peut pas voir une isométrie, puisque la matrice de Gram et les distances n'en dépendent pas ; un test se juge aux erreurs qu'il attrape, et à celles qu'il ne peut pas attraper.

**M28.19 · 🏆 Défi : redessiner la carte de 30 villes quand un quart des distances manquent.** Le notebook fournit la matrice `D_19`, de forme $(30, 30)$, des distances entre 30 villes d'une région de $200 \times 150$ km : symétrique, de diagonale nulle, mesurée avec une erreur d'environ 300 m (des écarts gaussiens d'écart-type 0,3 km), et dont un quart des 435 paires, tirées au hasard, manquent (`np.nan`). Il fournit aussi `procrustes_error_19(Y, P)`, qui centre la carte `Y` et les vraies positions `P`, trouve la transformation orthogonale qui aligne au mieux `Y` sur `P` (le problème de Procrustes orthogonal, Borg et Groenen, ch. 19 *Procrustes Procedures*) et rend la distance moyenne, en km, entre les villes alignées et leurs vraies positions. Écris `map_from_partial_distances_19(D)`, qui reçoit une telle matrice et rend une carte de forme $(n, 2)$. Tout NumPy et SciPy sont permis, et ta `points_from_gram`. **Critère de réussite :** une erreur après alignement de moins de 1 km en moyenne pour la région du notebook, et pour trois régions cachées de la vérification (d'autres villes, d'autres paires manquantes, une autre graine à chaque exécution), en moins de 10 secondes par région. Relève : a) ton erreur après alignement pour la région du notebook (km, 3 décimales) ; b) l'erreur qu'on obtient en remplaçant chaque distance manquante par la moyenne des distances connues, puis en faisant un seul positionnement multidimensionnel classique (km, 1 décimale). Point de départ : un seul double centrage d'une matrice complétée au hasard ne suffit pas, mais une carte donne des distances pour toutes les paires.
