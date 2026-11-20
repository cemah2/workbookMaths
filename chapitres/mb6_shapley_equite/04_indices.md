# MB6 · Shapley, intégrales de chemin et équité — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB6.Q1 — Jeux coopératifs : ordres ou coalitions, poids d'une coalition, et ce que garantit chaque axiome

<details><summary>Indice 1</summary>

Fiche §1 : « Un gain créé ensemble », « Les poids des coalitions », « Estimer par des ordres tirés au hasard » et « Voter avec des poids » ; §2 : « Quatre règles de partage ».

</details>
<details><summary>Indice 2</summary>

Un ordre de 7 joueurs : combien de façons de les ranger ? Si $i$ est premier, il reste à ranger les 6 autres. Le poids d'**une** coalition de taille $s$ est $w(s) = \frac{s!\,(n - 1 - s)!}{n!}$, et il y a $\binom{n-1}{s}$ coalitions de taille $s$ sans $i$. Pour 4, cherche un petit conseil où un membre de 2 voix n'est jamais plus utile qu'un membre d'une voix. Pour 5, dans un même ordre, que donne la somme des contributions ?

</details>
<details><summary>Indice 3</summary>

1. $7!$, puis $6!$. 2. $\frac{2!\,4!}{7!}$, puis multiplie par $\binom62 = 15$. 3. Les quatre noms : efficacité, symétrie, joueur nul, additivité. 4. Essaie $[5 ;\ 4, 2, 1, 1]$ : compte les ordres où le membre de 2 voix est pivot, puis ceux d'un membre d'une voix. 5. Les contributions d'un ordre se télescopent : de $v(\varnothing)$ à $v(N)$.

</details>

### MB6.Q2 — Fixer une variable : moyenne marginale ou conditionnelle, courbes ICE parallèles ou non

<details><summary>Indice 1</summary>

Fiche §3 : « Deux façons de fixer une variable » et « Les courbes ICE » ; M25a (la loi conditionnelle d'un couple gaussien).

</details>
<details><summary>Indice 2</summary>

$\operatorname{PD}_j(v)$ moyenne $f$ sur la loi **marginale** des autres variables ; $M_j(v)$ sur leur loi **sachant** $X_j = v$. Elles coïncident quand cette loi conditionnelle est la loi marginale. Pour une fonction linéaire, la moyenne passe à l'intérieur. Les courbes ICE de $x_1$ sont des translatées les unes des autres quand la dérivée croisée est nulle.

</details>
<details><summary>Indice 3</summary>

1. (C) ne garde qu'un point. 3. Avec des moyennes nulles et des variances 1, $\mathbb{E}[X_2 \mid X_1 = v] = \rho\,v$ ; $\operatorname{PD}_1(v) = v - 4\,\mathbb{E}[X_2]$ et $M_1(v) = v - 4\,\mathbb{E}[X_2 \mid X_1 = v]$. 4. Calcule $\frac{\partial^2f}{\partial x_1\,\partial x_2}$ pour chaque fonction. 5. L'estimation de la fiche : $\frac1n\sum_if(v, \mathbf{x}_{i,-j})$.

</details>

### MB6.Q3 — Intégrales de chemin : boucle fermée, chemin parcouru à l'envers, champ qui n'est pas un gradient, fonction homogène

<details><summary>Indice 1</summary>

Fiche §4 : « Un chemin et une intégrale » (le théorème du gradient, le chemin parcouru à l'envers, le test de Schwarz), « Partager une variation entre les coordonnées » et « Les fonctions homogènes ».

</details>
<details><summary>Indice 2</summary>

Le théorème du gradient : $\int\nabla f\cdot\mathrm{d}\boldsymbol\gamma = f(\text{fin}) - f(\text{début})$. Parcourir un chemin à l'envers change le signe de la vitesse, pour tout champ. Un gradient de classe $C^1$ a $\frac{\partial F_1}{\partial y} = \frac{\partial F_2}{\partial x}$. Euler : $\sum_ix_i\,\partial_if = k\,f$ ; depuis $\mathbf{r} = \mathbf{0}$, la part de $x_i$ le long du segment est $\frac{x_i\,\partial_if(\mathbf{x})}{k}$.

</details>
<details><summary>Indice 3</summary>

3. Compare $\frac{\partial F_1}{\partial y}$ et $\frac{\partial F_2}{\partial x}$ pour chacun des trois champs. 4. $\partial_xf = 3x\sqrt{x^2 + y^2}$ et $\partial_yf = 3y\sqrt{x^2 + y^2}$ ; en $(3, 4)$, la racine vaut 5 ; divise $x\,\partial_xf$ et $y\,\partial_yf$ par 3, et vérifie que la somme fait $f(3, 4)$. 5. Le théorème de la fiche §4 suppose $f$ multilinéaire.

</details>

### MB6.Q4 — Grilles et rangs : interpolation bilinéaire, centres ou coins alignés, ex aequo et transformation strictement croissante

<details><summary>Indice 1</summary>

Fiche §5 : « Interpoler sur une case » et « Agrandir une grille : deux conventions » ; §6 : « Des rangs au lieu des valeurs ».

</details>
<details><summary>Indice 2</summary>

Les poids bilinéaires sont $(1 - s)(1 - t)$, $s(1 - t)$, $(1 - s)\,t$ et $s\,t$. Centres alignés : $\xi(u) = (u + \frac12)\frac hH - \frac12$ ; coins alignés : $\xi(u) = u\,\frac{h - 1}{H - 1}$. Les rangs : trie, numérote à partir de 1, et donne aux ex aequo la moyenne de leurs places. $\rho_S$ ne dépend que de l'ordre de chaque échantillon.

</details>
<details><summary>Indice 3</summary>

1. $s = t = \frac12$. 2. $h = 4$ et $H = 10$ : $\xi(0) = \frac12 \times 0{,}4 - \frac12$ et $\xi(9) = 9{,}5 \times 0{,}4 - \frac12$ ; coins : $u \times \frac39$. 3. Trie : $2{,}9$ ; $3{,}8$ ; $5{,}2$ ; $5{,}2$ ; $7{,}1$ ; puis remets les rangs dans l'ordre de départ. 4. $\ln$ garde l'ordre ; $x \mapsto -x$ l'inverse : le rang $r_i$ devient $n + 1 - r_i$.

</details>

### MB6.Q5 — Indépendance, séparation, suffisance : quel critère pour quelle phrase, et lesquels se contredisent

<details><summary>Indice 1</summary>

Fiche §7 : « Trois critères » et « Ce qui est incompatible ».

</details>
<details><summary>Indice 2</summary>

Indépendance : $\hat Y \perp G$ (le taux de rejet de chaque ligne). Séparation : $\hat Y \perp G \mid Y$ (les taux par ligne parmi les pièces défectueuses, puis parmi les bonnes). Suffisance : $Y \perp G \mid \hat Y$ (la part de défectueuses parmi les rejetées, puis parmi les acceptées). Pour un score, la suffisance devient la calibration dans chaque groupe.

</details>
<details><summary>Indice 3</summary>

1 à 4 : demande-toi **sachant quoi** on compare les deux lignes : rien, $Y$, $\hat Y$ ou le score. 5. Sous la séparation, le taux de rejet de la ligne $g$ vaut $f + (t - f)\,p_g$ ; l'indépendance l'égale sur les deux lignes, avec $p_1 \ne p_2$.

</details>

### MB6.Q6 — Tirer au sort entre deux seuils, repondérer, lire l'écart de deux taux : vrai ou faux

<details><summary>Indice 1</summary>

Fiche §8 : « Tirer au sort entre deux seuils », « Repondérer » et « L'écart de deux taux ».

</details>
<details><summary>Indice 2</summary>

Le seuil tiré est indépendant du label : les probabilités totales. Le tirage fait une moyenne pondérée des deux points ROC. La repondération $\frac{P(g)\,P(y)}{P(g, y)}$ garde les deux marges. Les **variances** de deux estimations indépendantes s'ajoutent.

</details>
<details><summary>Indice 3</summary>

1. $P(\hat Y = 1 \mid Y = 1) = q\,P(\hat Y = 1 \mid Y = 1, A) + (1 - q)\,P(\hat Y = 1 \mid Y = 1, B)$. 2. Le point $(\mathrm{FPR}, \mathrm{TPR})$ du tirage, quand $q$ va de 0 à 1. 3. Somme les probabilités pondérées d'un groupe : $\sum_yP(g)\,P(y) = \ ?$ 4. Compare $\sqrt{a^2 + b^2}$ et $a + b$. 5. Seul le terme $\frac{\theta(1 - \theta)}{n}$ de ce groupe est divisé par 4.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### MB6.R1 — Parties d'un ensemble, factorielles et combinaisons (R4, R8)

<details><summary>Indice 1</summary>

R4 (les parties d'un ensemble) et R8 (factorielles, combinaisons, la somme d'une ligne du triangle de Pascal).

</details>
<details><summary>Indice 2</summary>

Une partie : chaque élément y est ou n'y est pas. $\binom nk = \frac{n!}{k!\,(n - k)!}$. Ranger $n$ objets : $n!$ façons. $\sum_k\binom nk = (1 + 1)^n$.

</details>
<details><summary>Indice 3</summary>

1. $2^9$ ; pour celles qui contiennent un élément donné, choisis librement les 8 autres. 2. $\frac{9 \times 8 \times 7}{3 \times 2 \times 1}$. 3. $5 \times 4 \times 3 \times 2 \times 1$. 4. Choisir les $k$ qu'on prend, c'est choisir les $n - k$ qu'on laisse. 5. Le binôme pour $(1 + 1)^8$.

</details>

### MB6.R2 — La dérivée d'une fonction le long d'une courbe : gradient, vitesse et règle de la chaîne (M05b, M17)

<details><summary>Indice 1</summary>

M05b (gradient, dérivée directionnelle, Schwarz) et M17 (la règle de la chaîne).

</details>
<details><summary>Indice 2</summary>

$(f\circ\boldsymbol\gamma)'(t) = \nabla f(\boldsymbol\gamma(t))\cdot\boldsymbol\gamma'(t)$. La dérivée directionnelle selon un vecteur **unitaire** $\mathbf{u}$ est $\nabla f\cdot\mathbf{u}$ : normalise $(1, 1)$ d'abord. Schwarz : pour $f$ de classe $C^2$, les deux dérivées croisées sont égales.

</details>
<details><summary>Indice 3</summary>

1. $\partial_xf = 6x^2y$ et $\partial_yf = 2x^3 - 3y^2$. 2. $\boldsymbol\gamma(1) = (2, 1)$ et $\boldsymbol\gamma'(t) = (1, -1)$. 3. Le produit scalaire de $\nabla f(2, 1)$ et de $(1, -1)$. 4. $\nabla f(2, 1)\cdot\frac{(1, 1)}{\sqrt2}$. 5. Dérive $6x^2y$ par $y$, puis $2x^3 - 3y^2$ par $x$.

</details>

### MB6.R3 — La loi conditionnelle d'un couple gaussien : une moyenne affine en la valeur observée (M25a)

<details><summary>Indice 1</summary>

M25a : la loi conditionnelle d'un couple gaussien.

</details>
<details><summary>Indice 2</summary>

$\operatorname{Cov}(X, Y) = \rho\,\sigma_X\sigma_Y$. $\mathbb{E}[Y \mid X = x] = \mu_Y + \rho\,\frac{\sigma_Y}{\sigma_X}(x - \mu_X)$ et $\mathbb{V}(Y \mid X = x) = \sigma_Y^2(1 - \rho^2)$.

</details>
<details><summary>Indice 3</summary>

1. $0{,}3 \times 4 \times 10$. 2. La pente $0{,}3 \times \frac{10}{4}$. 3. $x - 20 = 6$. 4. $100 \times (1 - 0{,}09)$ ; $x$ n'y figure pas. 5. Avec $\rho = 0$, la pente est nulle.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB6.1 — Un conseil de quatre membres à vote pondéré : l'indice de Shapley-Shubik par les 24 ordres, un membre nul, deux membres de poids différents et de même pouvoir, et le nombre d'ordres tirés au hasard qui suffit (Hoeffding)

<details><summary>Indice 1</summary>

Fiche §1 : « Voter avec des poids » (le pivot, l'indice de Shapley-Shubik) et « Estimer par des ordres tirés au hasard » ; M11 §6 (Hoeffding).

</details>
<details><summary>Indice 2</summary>

Liste d'abord les coalitions gagnantes : au moins 11 voix. Dans un ordre, le pivot est le membre dont l'arrivée fait passer les voix déjà réunies de moins de 11 à au moins 11. Pour chaque membre, compte les ordres où il est pivot position par position (deuxième, troisième, dernier), sans écrire les 24 ordres : derrière quels membres l'est-il ? Pour d), Hoeffding pour la moyenne de $m$ variables à valeurs dans $[0, 1]$ : $P(\lvert\hat\varphi - \varphi\rvert \ge \varepsilon) \le 2e^{-2m\varepsilon^2}$.

</details>
<details><summary>Indice 3</summary>

a) A est pivot en deuxième position derrière B ou derrière C (pas derrière D) ; en troisième derrière deux des membres B, C, D (lesquels ?) ; en dernier, derrière BCD ? Chaque début d'ordre fixé laisse 2 ou 1 façons de finir. B est pivot juste après A, ou après A et D ; C de même. Vérifie que les quatre comptes font 24. b) Divise par 24. c) Recommence avec 2 voix pour D : BCD a maintenant 11 voix. d) $2e^{-2m \times 0{,}05^2} \le 0{,}04$, soit $m \ge \frac{\ln 50}{2 \times 0{,}0025}$ ; arrondis vers le haut.

</details>

### Ex MB6.2 — Trois hameaux partagent une conduite d'eau : la valeur de Shapley par les ordres, les dividendes de Harsanyi, le partage tronçon par tronçon, et les quatre axiomes vérifiés

<details><summary>Indice 1</summary>

Fiche §1 : « Partager un coût » ; §2 : « Quatre règles de partage » et « Les jeux d'unanimité et les dividendes ».

</details>
<details><summary>Indice 2</summary>

Dans un ordre, un hameau paie ce qu'il ajoute : le prolongement de la conduite au-delà du plus éloigné des hameaux déjà raccordés, ou 0 s'il est en deçà. Les dividendes : $d_T = \sum_{S \subseteq T}(-1)^{\lvert T\rvert - \lvert S\rvert}c(S)$ ; pour un hameau seul, $d_{\{i\}} = c(\{i\})$. Pour d), l'additivité : le nouveau coût est l'ancien plus 8 fois le jeu « payer le tronçon de H1 à H2 ».

</details>
<details><summary>Indice 3</summary>

a) Ordre H1 H2 H3 : $(30, 21, 17)$ ; un ordre où H3 arrive le premier : H3 paie 68, les autres rien. Fais les six ordres, puis la moyenne de chaque hameau. b) $d_{\{1, 2\}} = c(\{1, 2\}) - c(\{1\}) - c(\{2\})$. c) $c(N)$, moins la somme des paires, plus la somme des hameaux seuls. d) Quels hameaux utilisent le tronçon de H1 à H2 ?

</details>

### Ex MB6.3 — Le rendement d'une parcelle selon la pluie et l'engrais : courbes ICE et dérivée croisée de deux modèles, puis la moyenne marginale et la moyenne conditionnelle quand pluie et engrais sont corrélés

<details><summary>Indice 1</summary>

Fiche §3 : « Les courbes ICE » (parallèles ou non, la dérivée croisée) et « Deux façons de fixer une variable » ; M25a pour $\mathbb{E}[P \mid E = v]$.

</details>
<details><summary>Indice 2</summary>

Le gain est $f(p, 2) - f(p, 1)$, parcelle par parcelle. Pour le modèle 2, la différence de deux carrés se factorise. $\frac{\partial^2f}{\partial p\,\partial e}$ : dérive par $e$, puis par $p$. $\operatorname{PD}(2) = \mathbb{E}[f_1(P, 2)]$ : $f_1$ est affine en $p$, remplace $P$ par sa moyenne. $M(2)$ : remplace $P$ par $\mathbb{E}[P \mid E = 2] = \mu_P + \rho\,\frac{\sigma_P}{\sigma_E}(2 - \mu_E)$.

</details>
<details><summary>Indice 3</summary>

a) $2{,}4 \times (2 - 1) - 0{,}4 \times (2^2 - 1^2)$ : $p$ n'y figure pas. b) $f_2(p, 2) - f_2(p, 1) = -0{,}5\big[(p - 5)^2 - (p - 4)^2\big]$, une fonction affine de $p$. c) $\partial_ef_2 = p - e - 3$. d) $\mathbb{E}[P \mid E = 2] = 5{,}5 + 0{,}35 \times \frac{1{,}2}{0{,}5} \times 0{,}5$. e) $M(v) - \operatorname{PD}(v) = 0{,}6\,\big(\mathbb{E}[P \mid E = v] - 5{,}5\big)$.

</details>

### Ex MB6.4 — Le travail de deux forces entre deux points : un champ de gradient le long de trois chemins, puis un champ qui n'en est pas un (Schwarz) le long de deux chemins

<details><summary>Indice 1</summary>

Fiche §4 : « Un chemin et une intégrale » (le théorème du gradient, le test de Schwarz) ; M17 (la règle de la chaîne).

</details>
<details><summary>Indice 2</summary>

Pour chaque chemin : un paramétrage $\boldsymbol\gamma(t)$, sa vitesse $\boldsymbol\gamma'(t)$, puis $\int_0^1\mathbf{F}(\boldsymbol\gamma(t))\cdot\boldsymbol\gamma'(t)\,\mathrm{d}t$. Sur un morceau horizontal, il ne reste que $F_1\,\mathrm{d}x$ ; sur un vertical, $F_2\,\mathrm{d}y$. $\mathbf{F} = \nabla f$ : $f(B) - f(A)$ contrôle a), b) et c).

</details>
<details><summary>Indice 3</summary>

a) $\boldsymbol\gamma(t) = (1 + t, t)$ et $\boldsymbol\gamma' = (1, 1)$ : intègre $2(1 + t)t^2 + 5 + 2(1 + t)^2t$. b) Horizontal : $y = 0$, $F_1 = 5$, de $x = 1$ à 2 ; vertical : $x = 2$, $F_2 = 8y$, de $y = 0$ à 1. c) $\boldsymbol\gamma' = (1, 2t)$. d) $G_1 = 2y$ et $G_2 = 3x^2$. e) Segment : $\mathbf{G}\cdot(1, 1) = 2t + 3(1 + t)^2$ ; escalier : $G_1$ sur $y = 0$, puis $G_2$ sur $x = 2$.

</details>

### Ex MB6.5 — La variation d'un coût à trois facteurs (prix, quantité, taux de change) partagée entre les facteurs : le long du segment, puis par la moyenne des six chemins en escalier, et pourquoi les deux partages coïncident

<details><summary>Indice 1</summary>

Fiche §4 : « Partager une variation entre les coordonnées » (les parts le long du segment, les chemins en escalier, le théorème multilinéaire) ; ✏️ MB6.2 (Shapley par les ordres) ; M02a (intégrer un polynôme).

</details>
<details><summary>Indice 2</summary>

Le long du segment $\mathbf{r} + t\,\mathbf{h}$, avec $\mathbf{h} = \mathbf{x} - \mathbf{r}$, la part de $p$ est $h_p\int_0^1q(t)\,\tau(t)\,\mathrm{d}t$, l'intégrale d'un polynôme de degré 2 en $t$ ; de même pour $q$ et $\tau$. Dans un chemin en escalier, un facteur passe de sa valeur du premier trimestre à celle du second quand vient son tour : sa contribution est sa variation fois le produit des deux autres, à leurs valeurs de ce moment.

</details>
<details><summary>Indice 3</summary>

a) $13{,}5 \times 590 \times 0{,}87 - 11{,}5 \times 680 \times 0{,}93$. b) $\mathbf{h} = (2 ;\ -90 ;\ -0{,}06)$ ; développe $(680 - 90t)(0{,}93 - 0{,}06t)$ et intègre terme à terme, avec $\int_0^1t^2\,\mathrm{d}t = \frac13$. c) $\tau$ en dernier : $p$ et $q$ valent déjà $13{,}5$ et 590 ; $\tau$ en premier : $11{,}5$ et 680. d) Dans les six ordres, $\tau$ est premier deux fois, dernier deux fois, deuxième après $p$ une fois, après $q$ une fois.

</details>

### Ex MB6.6 — Des relevés de capteurs sur une grille 3 × 4 : la dérivée d'un indice régional par un réchauffement uniforme, puis la grille agrandie deux fois par interpolation bilinéaire, centres ou coins alignés

<details><summary>Indice 1</summary>

Fiche §5 : « La moyenne d'un gradient », « Interpoler sur une case » et « Agrandir une grille : deux conventions ».

</details>
<details><summary>Indice 2</summary>

$\max(0, T - 10)$ est nul sous 10 °C et vaut $T - 10$ au-dessus : seules les cases au-dessus de 10 °C comptent, chacune avec sa surface. Un réchauffement $\delta$ ajoute $\delta$ à chaque $T_{ij}$ ; la dérivée en $\delta = 0$ ne vaut que tant qu'aucune case ne franchit 10 °C. Agrandir : $h = 3$ lignes deviennent $H = 6$, $w = 4$ colonnes deviennent $W = 8$ ; une case d'arrivée lit la grille d'origine en $(\xi(u), \xi(v))$.

</details>
<details><summary>Indice 3</summary>

a) Huit cases sont au-dessus de 10 °C : $11{,}8$ ; $13{,}2$ ; $10{,}8$ ; $12{,}5$ ; $14{,}1$ ; $10{,}3$ ; $12{,}0$ ; $11{,}4$. b) Leurs surfaces. c) Après $+1$ °C, quelles cases passent au-dessus de 10 ? d) $(u + \frac12)\frac36 - \frac12$. e) $u\,\frac25$. f) La ligne $\xi(4)$ et la colonne $\xi(5)$ (avec $\frac48$ pour les colonnes en centres alignés, $\frac37$ en coins alignés) tombent entre les lignes 1 et 2 et les colonnes 2 et 3 : interpole sur chaque ligne, puis entre les deux lignes.

</details>

### Ex MB6.7 — Un contrôle de pièces sur deux lignes de production aux taux de défauts différents : les taux de rejet sous la séparation, un tirage au sort entre deux seuils pour atteindre un taux de détection, et les poids qui rendent ligne et défaut indépendants

<details><summary>Indice 1</summary>

Fiche §7 : « Ce qui est incompatible » ; §8 : « Tirer au sort entre deux seuils » et « Repondérer » ; M03 §7 et §8.

</details>
<details><summary>Indice 2</summary>

Taux de rejet d'une ligne $= \mathrm{TPR}\times p_g + \mathrm{FPR}\times(1 - p_g)$. Le tirage donne $\mathrm{TPR} = q\,\mathrm{TPR}_A + (1 - q)\,\mathrm{TPR}_B$, et le FPR avec le **même** $q$. $w(g, y) = \frac{P(g)\,P(y)}{P(g, y)}$, avec les probabilités lues sur toute la table (2 400 pièces). Le taux de défauts pondéré d'une ligne : ses défectueuses pondérées divisées par ses pièces pondérées.

</details>
<details><summary>Indice 3</summary>

a) $0{,}88 \times 0{,}06 + 0{,}04 \times 0{,}94$, puis la ligne 2. b) $0{,}74\,q + 0{,}96\,(1 - q) = 0{,}90$. c) $q \times 0{,}03 + (1 - q) \times 0{,}09$, avec le $q$ de b) gardé en fraction. d) 232 pièces défectueuses en tout ; par exemple $w(1, \text{défaut}) = \frac{1\,300}{2\,400} \times \frac{232}{2\,400} \Big/ \frac{78}{2\,400}$. e) $\frac{78\,w(1, \text{défaut})}{78\,w(1, \text{défaut}) + 1\,222\,w(1, \text{sans défaut})}$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB6.8 — Unicité de la valeur de Shapley : les jeux d'unanimité forment une base, et les quatre axiomes imposent φ_i = Σ_{T ∋ i} d_T / |T|

<details><summary>Indice 1</summary>

Fiche §2 : « Quatre règles de partage » et « Les jeux d'unanimité et les dividendes » ; M02b §2 (la formule du binôme) ; M12a (base d'un espace vectoriel).

</details>
<details><summary>Indice 2</summary>

1. Remplace $d_T$ par sa définition et échange les deux sommes : pour $R \subseteq S$, compte les $T$ entre $R$ et $S$, avec leur signe. 2. $2^n$ jeux qui engendrent un espace de dimension $2^n$. 3. Dans $c\,u_T$ : quels joueurs sont nuls, lesquels sont symétriques ? Puis l'efficacité. 4. L'additivité sur la somme finie $v = \sum_Td_T\,u_T$.

</details>
<details><summary>Indice 3</summary>

1. Avec $m = \lvert S\rvert - \lvert R\rvert$, la somme intérieure vaut $\sum_k\binom mk(-1)^k = (1 - 1)^m$ : nulle sauf si $R = S$. 2. Évalue $\sum_Td_T\,u_T$ en $S$. 3. Pour $i \notin T$ : $S \cup \{i\}$ contient $T$ si et seulement si $S$ le contient. Pour $i, j \in T$ et $S$ sans $i$ ni $j$ : ni $S \cup \{i\}$ ni $S \cup \{j\}$ ne contient $T$. La somme des parts vaut $c\,u_T(N) - c\,u_T(\varnothing)$. Le jeu constant $c\,u_\varnothing$ : tous les joueurs sont nuls. 4. $\varphi_i(v) = \sum_T\varphi_i(d_T\,u_T)$. 5. L'existence et l'unicité.

</details>

### Ex MB6.9 — Un score calibré dans un groupe vérifie p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; si deux groupes ont les mêmes moyennes de scores chez leurs positifs et chez leurs négatifs, leurs taux de base sont égaux ou le score est parfait

<details><summary>Indice 1</summary>

Fiche §7 : « Ce qui est incompatible » (l'identité d'un score calibré) ; M25b §2 (l'espérance totale).

</details>
<details><summary>Indice 2</summary>

1. Conditionne par $S$ : $\mathbb{E}[S] = \sum_ss\,P(S = s)$, et la calibration remplace $s$ par $P(Y = 1 \mid S = s)$. 2. Conditionne par $Y$ : $\mathbb{E}[S] = p\,a + (1 - p)\,b$. 3. Isole $p$ ; pour le cas $1 - a + b = 0$, $0 \le S \le 1$ donne $a \le 1$ et $b \ge 0$. 4. Calibré : à chaque valeur du score, la part de pièces défectueuses égale cette valeur.

</details>
<details><summary>Indice 3</summary>

3. $p\,(1 - a + b) = b$. Si $1 - a + b = 0$ : $1 - a \ge 0$ et $b \ge 0$ ont une somme nulle, donc $a = 1$ et $b = 0$ ; une variable positive d'espérance nulle est nulle presque sûrement : applique-le à $S$ sachant $Y = 0$, puis à $1 - S$ sachant $Y = 1$. 4. $a = \frac{15 \times 0{,}02 + 15 \times 0{,}1 + 30 \times 0{,}3}{60}$ ; $b$ sur les 940 bonnes pièces (735, 135 et 70) ; puis $\frac{b}{1 - a + b}$.

</details>

### Ex MB6.10 — Indépendance et séparation ne tiennent ensemble, quand les taux de base diffèrent, que pour une décision qui ignore le label ; la repondération P(g)P(y)/P(g, y) rend groupe et label indépendants sans changer leurs marges

<details><summary>Indice 1</summary>

Fiche §7 : « Ce qui est incompatible » ; §8 : « Repondérer » ; M03 (probabilités totales, indépendance).

</details>
<details><summary>Indice 2</summary>

1. $P(\hat Y = 1 \mid G = g) = t_g\,p_g + f_g\,(1 - p_g)$. Sous la séparation, c'est $f + (t - f)\,p_g$ : égal pour $g = 1$ et 2 si et seulement si $(t - f)(p_1 - p_2) = 0$. 2. Écris $Q(g, y) = P(g)\,P(y)$, puis sa somme et ses deux marges.

</details>
<details><summary>Indice 3</summary>

1. $t = f$ se lit $P(\hat Y = 1 \mid Y = 1, G = g) = P(\hat Y = 1 \mid Y = 0, G = g)$. Pour la réciproque, prends une décision qui ignore le label mais rejette plus souvent sur une ligne que sur l'autre : vérifie-t-elle l'indépendance ? 2. $\sum_yP(g)\,P(y) = P(g)$ ; et $Q$ est le produit de ses marges.

</details>

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB6.11 — Pont : l'écart des taux de détection de deux laboratoires et son intervalle, par l'erreur type d'une différence de deux proportions, qui se lit avec le nombre d'échantillons positifs de chacun

<details><summary>Indice 1</summary>

Fiche §8 : « L'écart de deux taux » ; M02b (variance d'une différence) ; M08 §5 (l'intervalle de Wald).

</details>
<details><summary>Indice 2</summary>

Un taux de détection se calcule sur les prélèvements contaminés seulement. L'erreur type d'une proportion estimée sur $n$ cas est $\sqrt{\frac{\theta(1 - \theta)}{n}}$, avec $n$ le nombre de prélèvements contaminés. Les deux laboratoires sont indépendants : les variances s'ajoutent. Wald à 95 % : l'écart $\pm\ 1{,}96$ erreur type.

</details>
<details><summary>Indice 3</summary>

a) $\frac{20}{28}$ et $\frac{448}{520}$. b) $\sqrt{\frac{\hat\theta_A(1 - \hat\theta_A)}{28} + \frac{\hat\theta_B(1 - \hat\theta_B)}{520}}$, avec tous les chiffres. c) $(\hat\theta_B - \hat\theta_A) \pm 1{,}96 \times$ b). d) Seul le premier terme change : 112 au lieu de 28.

</details>

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB6.12 — Expliquer avec trois amis qui partagent un taxi pourquoi on moyenne l'apport de chacun sur tous les ordres d'arrivée

<details><summary>Indice 1</summary>

Fiche §1 : « Un gain créé ensemble » et « Partager un coût » ; §2 : « Quatre règles de partage ».

</details>
<details><summary>Indice 2</summary>

Ce que Léa ajoute au prix quand Sam est déjà dans le taxi, et ce qu'elle ajoute quand elle est seule. Un seul ordre fait payer cher le premier monté. La moyenne sur tous les ordres : chaque ordre paie tout le prix, donc la moyenne aussi ; deux amis au même endroit jouent le même rôle dans chaque ordre.

</details>
<details><summary>Indice 3</summary>

Plan : (1) l'apport de Léa avec ou sans Sam ; (2) un ordre favorise ceux qui montent les derniers ; (3) tous les ordres, et la moyenne ; (4) tout est payé, et deux amis au même endroit paient autant ; (5) chaque bout du trajet se partage entre ceux qui vont au-delà : Sam paie le plus. Aucune formule.

</details>

<a id="entretien"></a>

## 💼 Entretien

### MB6.E1 — « La valeur de Shapley est la seule répartition qui respecte quatre règles simples : lesquelles, et pourquoi suffisent-elles ? »

<details><summary>Indice 1</summary>

Fiche §2 : « Quatre règles de partage » et « Les jeux d'unanimité et les dividendes » ; ∂ MB6.8.

</details>
<details><summary>Indice 2</summary>

Nomme l'efficacité, la symétrie, le joueur nul et l'additivité. L'argument en deux temps : sur un jeu d'unanimité, trois règles imposent le partage ; tout jeu est une combinaison de jeux d'unanimité (les dividendes), et l'additivité étend le partage. L'existence : la moyenne sur les ordres vérifie les quatre règles.

</details>
<details><summary>Indice 3</summary>

Plan en 60 secondes : les quatre règles, une phrase chacune ; un jeu d'unanimité (nuls hors du groupe, symétriques dedans, efficacité) ; la décomposition par les dividendes et l'additivité ; l'existence par les ordres ; une limite (l'additivité, ou une symétrie qui ne dit rien de joueurs presque semblables).

</details>

<a id="notebook"></a>

## Notebook

### MB6.13 — Les poids des coalitions dans la valeur de Shapley, exacts ou en flottants : `coalition_weights`

<details><summary>Indice 1</summary>

Fiche §1 : « Les poids des coalitions » ; la docstring de `coalition_weights`, qui dit chaque contrôle.

</details>
<details><summary>Indice 2</summary>

Les contrôles d'abord : `isinstance(n_players, bool)` avant tout, puis un entier (`int` ou `np.integer`) $\ge 1$ ; `exact` un booléen. Puis, pour $s$ de 0 à $n - 1$, `Fraction(math.factorial(s) * math.factorial(n - 1 - s), math.factorial(n))`, et `float` sinon, dans un `np.array`. a) $n = 9$ ; b) $n = 25$, le rapport du premier poids et de celui de taille 12.

</details>
<details><summary>Indice 3</summary>

$w(s) = \frac{1}{n\binom{n-1}{s}}$, donc $\frac{w(0)}{w(s)} = \binom{n-1}{s}$ : b) est $\binom{24}{12}$. Contrôle : $\sum_s\binom{n-1}{s}\,w(s) = 1$ et $w(s) = w(n - 1 - s)$. Ce qu'il faut regarder : chaque taille pèse $\frac1n$ en tout, partagé entre ses $\binom{n-1}{s}$ coalitions.

</details>

### MB6.14 — Les dividendes de Harsanyi d'un jeu donné par sa fonction caractéristique : `harsanyi_dividends`

<details><summary>Indice 1</summary>

Fiche §2 : « Les jeux d'unanimité et les dividendes » ; la docstring de `harsanyi_dividends` (l'ordre des clés).

</details>
<details><summary>Indice 2</summary>

Les contrôles ; puis `for size in range(n + 1): for c in itertools.combinations(range(n), size):` et `worth[frozenset(c)] = v(frozenset(c))`, en contrôlant chaque valeur (un réel fini, pas un booléen). Ensuite, pour chaque $T$ dans le même ordre, la somme sur ses parties $S$ de $(-1)^{\lvert T\rvert - \lvert S\rvert}$ `worth[S]`. b) `lambda S: TABLE_14[S]`, puis $\varphi_i = \sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$. d) $v(S) = 1$ si les voix de $S$ atteignent 11, 0 sinon.

</details>
<details><summary>Indice 3</summary>

```python
d = {}
for T in worth:                       # déjà dans le bon ordre
    total = 0.0
    for k in range(len(T) + 1):
        for S in itertools.combinations(sorted(T), k):
            total += (-1) ** (len(T) - k) * worth[frozenset(S)]
    d[T] = float(total)
```
b) `sum(x / len(T) for T, x in d.items() if i in T)` ; contrôle : les quatre parts somment à $v(N) - v(\varnothing)$.

</details>

### MB6.15 — L'intégrale d'un champ de vecteurs le long d'une ligne brisée, par la méthode de Simpson sur chaque segment : `line_integral`

<details><summary>Indice 1</summary>

Fiche §4 : « Un chemin et une intégrale » ; M02a (la règle de Simpson) ; la docstring de `line_integral`.

</details>
<details><summary>Indice 2</summary>

Les contrôles : `np.asarray(points, dtype=float)`, deux dimensions, au moins deux lignes et une colonne, des nombres finis ; `n_sub` un entier pair $\ge 2$ (pas un booléen) ; `field` appelable, et chaque valeur rendue de forme $(d,)$, finie. Pour chaque segment de $\mathbf{a}$ à $\mathbf{b}$ : $\mathbf{b} - \mathbf{a}$, les $n_{\text{sub}} + 1$ valeurs de $t$, les produits scalaires, et les poids $1, 4, 2, \ldots, 2, 4, 1$ fois $\frac h3$. c) Les sommets $(1 + t_k, t_k^2)$ pour $t_k = \frac kN$.

</details>
<details><summary>Indice 3</summary>

```python
w = np.ones(n_sub + 1); w[1:-1:2] = 4; w[2:-1:2] = 2
total = 0.0
for a, b in zip(pts[:-1], pts[1:]):
    g = [np.dot(value(a + t * (b - a)), b - a) for t in np.linspace(0, 1, n_sub + 1)]
    total += np.dot(w, g) / (3 * n_sub)
```
(`value` : ta fonction qui appelle `field` sur un point et contrôle ce qu'il rend.) c) `[[1 + t, t ** 2] for t in np.linspace(0, 1, N + 1)]`, puis compare chaque valeur à $\frac{55}{6}$.

</details>

### MB6.16 — La corrélation de rangs de Spearman, ex aequo compris : `spearman_rho`

<details><summary>Indice 1</summary>

Fiche §6 : « Des rangs au lieu des valeurs » ; M02c (la corrélation de Pearson) ; la docstring de `spearman_rho`.

</details>
<details><summary>Indice 2</summary>

Les contrôles. Les rangs : `order = np.argsort(x, kind="stable")` et les valeurs triées `xs = x[order]` ; parcours-les par groupes de valeurs égales : les places $i$ à $j$ (comptées à partir de 0) reçoivent toutes $\frac{i + j}{2} + 1$. Puis centre les deux vecteurs de rangs et applique la formule de Pearson ; `nan` si une somme de carrés est nulle. b) `[1 / v for v in VICKERS_16]`.

</details>
<details><summary>Indice 3</summary>

```python
r = np.empty(n)
i = 0
while i < n:
    j = i
    while j + 1 < n and xs[j + 1] == xs[i]:
        j += 1
    r[order[i:j + 1]] = (i + j) / 2 + 1
    i = j + 1
```
b) $v \mapsto \frac1v$ est strictement décroissante pour $v > 0$ : que deviennent les rangs, puis $\rho_S$ ?

</details>

### MB6.17 — Prédire l'intégrale d'un champ de gradient et d'un champ tournant le long d'une boucle triangulaire, dans un sens, dans l'autre et deux fois, puis vérifier

<details><summary>Indice 1</summary>

Fiche §4 : « Un chemin et une intégrale » (le théorème du gradient, le chemin parcouru à l'envers). Écris tes quatre prédictions avant d'ouvrir l'indice 2.

</details>
<details><summary>Indice 2</summary>

$\mathbf{F}$ est un gradient : que vaut $f(\text{fin}) - f(\text{début})$ pour une boucle ? $\mathbf{R} = (-y, x)$ n'en est pas un ($\frac{\partial R_1}{\partial y} = -1$, $\frac{\partial R_2}{\partial x} = 1$). Le long d'un segment de $\mathbf{a}$ à $\mathbf{b}$, calcule $\mathbf{R}(\mathbf{a} + t(\mathbf{b} - \mathbf{a}))\cdot(\mathbf{b} - \mathbf{a})$ : dépend-il de $t$ ?

</details>
<details><summary>Indice 3</summary>

Ta prédiction, raisonnée : a) le théorème du gradient. b) Sur un segment, $\mathbf{R}\cdot(\mathbf{b} - \mathbf{a}) = a_1b_2 - a_2b_1$ : quel lien avec l'aire du triangle $(\mathbf{0}, \mathbf{a}, \mathbf{b})$ ? Somme sur les trois côtés, et compare à l'aire $\frac12\lvert(B - A)\times(C - A)\rvert$. c) Chaque côté parcouru à l'envers. d) Deux tours repassent deux fois sur les mêmes segments. Pour mesurer : `line_integral` sur `[A, B, C, A]`, `[A, C, B, A]` et `[A, B, C, A, B, C, A]`.

</details>

### MB6.18 — Deux mesures corrélées : la moyenne marginale (dépendance partielle) et la moyenne conditionnelle d'une même fonction, simulées pour plusieurs corrélations et comparées aux formules gaussiennes

<details><summary>Indice 1</summary>

Fiche §3 : « Deux façons de fixer une variable » ; M25a (la loi conditionnelle d'un couple gaussien) ; M11 (la dispersion d'une moyenne).

</details>
<details><summary>Indice 2</summary>

$\operatorname{PD}(26) = e^{0{,}4}\,\mathbb{E}\big[e^{0{,}05(U - 70)}\big]$ avec $U \sim \mathcal{N}(70, 64)$. Pour $M(26)$, sachant $T = 26$, $U \sim \mathcal{N}\big(70 + \rho\frac83(26 - 22),\ 64(1 - \rho^2)\big)$. Puis $\mathbb{E}[e^{cZ}] = e^{c\mu + c^2\sigma^2/2}$. Pour b), la fenêtre $\lvert T_i - 26\rvert \le 0{,}25$ garde peu de points : compte-les.

</details>
<details><summary>Indice 3</summary>

a) $\operatorname{PD}(26) = \exp\big(0{,}4 + \frac12 \times 0{,}05^2 \times 64\big)$ et $M(26) = \exp\big(0{,}4 + 0{,}05\,(m_\rho - 70) + \frac12 \times 0{,}05^2 \times 64(1 - \rho^2)\big)$, avec $m_\rho = 70 + \frac{32}{3}\rho$. b) `keep = np.abs(T - 26) <= 0.25`, puis la moyenne de `f(T[keep], U[keep])` ; pour PD, la moyenne de `f(26, U)`. Compare `keep.sum()` à 300 000.

</details>

### MB6.19 — Les lignes de niveau d'une fonction de deux variables, deux chemins entre les mêmes points, et l'intégrale du gradient cumulée le long de chacun

<details><summary>Indice 1</summary>

Fiche §4 : « Un chemin et une intégrale » (le théorème du gradient) ; ton `line_integral` (MB6.15).

</details>
<details><summary>Indice 2</summary>

Une grille `np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))`, `ax_map.contour(X, Y, f_19(X, Y), levels=20)`, et les deux chemins par `ax_map.plot`, avec `label=`. Pour le cumul, place des points le long de chaque chemin (par exemple 50 par segment) et, pour chacun, `line_integral(grad_19, …)` sur le début du chemin jusqu'à ce point. La longueur parcourue : la somme cumulée des distances entre points successifs.

</details>
<details><summary>Indice 3</summary>

Le début d'un chemin jusqu'au point $\mathbf{q}$ de son segment $k$ : les sommets 0 à $k$, puis $\mathbf{q}$. a) `f_19(*B) - f_19(*A)`. b) Le maximum de chaque tableau de cumuls. Pour lire le graphique, compare le cumul au point courant avec $f(\text{point}) - f(A)$.

</details>

### MB6.20 — Chasse à l'erreur : des poids de coalition sans le facteur 1/n, des ex aequo classés dans l'ordre d'apparition, une interpolation linéaire aux poids échangés

<details><summary>Indice 1</summary>

Fiche §1 : « Les poids des coalitions » ; §6 : « Des rangs au lieu des valeurs » ; §5 : « Interpoler sur une case ».

</details>
<details><summary>Indice 2</summary>

Pour chaque fonction, cherche pourquoi l'entrée choisie par le collègue cache l'erreur : $n = 1$, un échantillon sans ex aequo, $t = \frac12$. Corrige le code du collègue lui-même, sans appeler `mymath`. Contrôle (1) par $\sum_s\binom{n-1}{s}\,w(s) = 1$, et (3) par les valeurs en $t = 0$ et $t = 1$.

</details>
<details><summary>Indice 3</summary>

(1) `math.factorial(n)` au dénominateur. (2) Les places de chaque groupe de valeurs égales, puis leur moyenne pour chacune, comme dans `spearman_rho`. (3) $(1 - t)\,a + t\,b$. a) `sum(math.comb(6, s) * w[s] for s in range(7))` avec chaque fonction. b) Pearson sur `ranks_fixed(X_20)` et `ranks_fixed(Y_20)`, puis sur les rangs fautifs. c) $t = 0{,}3$, $a = 12$, $b = 20$.

</details>

### MB6.21 — Un test de propriété sur des lignes brisées tirées au hasard : le chemin inversé change le signe, un segment coupé en deux ne change rien, un champ de gradient donne f(fin) − f(début)

<details><summary>Indice 1</summary>

Fiche §4 : « Un chemin et une intégrale » (le chemin parcouru à l'envers, le théorème du gradient) ; M02a (la règle de Simpson, exacte pour un polynôme de degré au plus 3).

</details>
<details><summary>Indice 2</summary>

Chaque test tire plusieurs lignes brisées (`rng.normal(size=(k, 2))`, $k$ de 3 à 6), appelle `method(field, points)` et compare : à l'envers, `points[::-1]` ; coupé, `np.insert(points, j + 1, a + lam * (b - a), axis=0)`, avec `lam` tiré dans $]0, 1[$ ; pour un gradient, $f(\text{fin}) - f(\text{début})$. Compare à $10^{-9}$ près en valeur relative : `abs(u - v) <= 1e-9 * max(1, abs(u))`. Rends un booléen Python.

</details>
<details><summary>Indice 3</summary>

Les champs : pour le premier test, un champ qui n'est pas un gradient (un sinus convient : les points de Simpson d'un segment parcouru à l'envers sont les mêmes) ; pour les deux autres, des coordonnées polynomiales de degré 2 ou 3, par exemple le gradient d'un polynôme de degré 3 : la règle de Simpson y est exacte, et la propriété tient à l'arrondi près. Avec un champ affine, la méthode des trapèzes passerait ; avec un champ non polynomial, la référence elle-même échouerait au deuxième test. a) Tes trois tests sur `line_integral`.

</details>

### MB6.22 — Défi : les indices de Shapley-Shubik exacts d'un conseil de 25 membres, sans parcourir ses coalitions une à une, en comptant par taille et par poids celles où chaque membre est pivot

<details><summary>Indice 1</summary>

Fiche §1 : « Voter avec des poids » et « Les poids des coalitions » ; ✏️ MB6.1 (le pivot) ; 🔨 MB6.13 (`coalition_weights`).

</details>
<details><summary>Indice 2</summary>

Le membre $i$ est pivot après une coalition $S$ des autres membres si son poids total $t$ vérifie $q - \omega_i \le t \le q - 1$. Donc $\varphi_i = \sum_sw(s)\,N_i(s)$, où $N_i(s)$ compte les coalitions de $s$ autres membres de poids total dans cette fenêtre. Ne les liste pas : compte-les dans un tableau indexé par la taille et le poids total, rempli membre par membre. Un poids total $\ge q$ ne sert jamais : $n \times q$ cases suffisent.

</details>
<details><summary>Indice 3</summary>

Ajouter un membre de poids $\omega$ au tableau $c$ donne $c'[s][t] = c[s][t] + c[s - 1][t - \omega]$ : les coalitions sans lui, plus celles avec lui. Pars de `table[0, 0] = 1`, ajoute tous les membres sauf $i$ (avec NumPy, une tranche décalée de $\omega$ en poids et de 1 en taille ; attention à ne pas réutiliser une ligne déjà mise à jour), puis somme les colonnes $\max(q - \omega_i, 0)$ à $q - 1$ et pondère par `coalition_weights(n)`. Contrôles : les indices somment à 1, deux membres de mêmes voix ont le même indice, et un petit conseil donne les valeurs de l'énumération.

</details>
