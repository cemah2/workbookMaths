# MB6 · Shapley, intégrales de chemin et équité — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/mb6_shapley_equite/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB6`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et du 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les joueurs d'un jeu sont nommés par des lettres ou numérotés de 1 à $n$ sur papier, de 0 à $n - 1$ dans le code ; $N$ est le grand groupe, $S$ une coalition de taille $s$, $\bar S$ son complément ; $v(\varnothing)$ n'est pas forcément nul, et l'efficacité s'écrit $\sum_i\varphi_i = v(N) - v(\varnothing)$ ($c$ pour un coût). $w(s) = \frac{s!\,(n - 1 - s)!}{n!}$ est le poids d'**une** coalition de taille $s$ ; un vote pondéré s'écrit $[q ;\ \omega_1, \ldots, \omega_n]$ (quota $q$, voix $\omega_i$) ; $d_T$ est le dividende de Harsanyi de $T$, $u_T$ son jeu d'unanimité. Au §3, $\operatorname{PD}_j(v) = \mathbb{E}[f(v, \mathbf{X}_{-j})]$ est la moyenne marginale et $M_j(v) = \mathbb{E}[f(\mathbf{X}) \mid X_j = v]$ la moyenne conditionnelle. Au §4, un chemin $\boldsymbol\gamma$ a pour paramètre $t \in [0, 1]$, $\mathbf{r}$ est la référence d'un partage et $\mathbf{h} = \mathbf{x} - \mathbf{r}$. Au §5, une grille de $h$ lignes devient une grille de $H$ lignes ; la case d'arrivée $u$ a la coordonnée d'origine $c(u)$, et les lignes et les colonnes sont numérotées à partir de 0. Au §6, $\rho_S$ est la corrélation de rangs de Spearman. Aux §7 et §8, $G$ est le groupe, $Y$ le label (1 : l'événement a lieu), $\hat Y$ la décision, $S$ le score, $p_g$ le taux de base du groupe $g$ ; le taux de détection est le TPR, le taux de fausses alertes le FPR ; $q$ est la probabilité de tirer un seuil, $w(g, y)$ un poids de repondération. Les logarithmes sont népériens.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 à 5 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### MB6.Q1 — Jeux coopératifs : ordres ou coalitions, poids d'une coalition, et ce que garantit chaque axiome 🧠 ★ ⏱️ 5 min
*Fiche §1 et §2 · parcours C, E*

1. Un jeu a 7 joueurs. Combien y a-t-il d'ordres d'arrivée ? Combien de coalitions ne contiennent pas un joueur $i$ donné ?
2. Dans la formule par les coalitions, quel poids porte **une** coalition de 2 joueurs qui ne contient pas $i$ ? Et toutes les coalitions de 2 joueurs ensemble ?
3. Quel axiome garantit chacune de ces phrases ? (a) Un membre qui ne change jamais la valeur d'une coalition reçoit 0. (b) Deux membres interchangeables reçoivent la même part. (c) Si l'on additionne deux jeux, les parts s'additionnent. (d) Les parts somment à $v(N) - v(\varnothing)$.
4. Vrai ou faux : dans un conseil à vote pondéré, un membre qui a deux fois plus de voix qu'un autre a deux fois plus de pouvoir.
5. Vrai ou faux : des parts estimées par $m$ ordres tirés au hasard somment exactement à $v(N) - v(\varnothing)$, quel que soit le tirage.

### MB6.Q2 — Fixer une variable : moyenne marginale ou conditionnelle, courbes ICE parallèles ou non 🧠 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Laquelle de ces quantités est la dépendance partielle $\operatorname{PD}_j(v)$ : (A) $\mathbb{E}[f(v, \mathbf{X}_{-j})]$ ; (B) $\mathbb{E}[f(\mathbf{X}) \mid X_j = v]$ ; (C) $f\big(v, \mathbb{E}[\mathbf{X}_{-j}]\big)$ ?
2. À quelle condition sur la loi de $\mathbf{X}$ les fonctions $\operatorname{PD}_j$ et $M_j$ sont-elles égales, quelle que soit $f$ ?
3. $f(x_1, x_2) = 3x_1 - 2x_2$, et $(X_1, X_2)$ est un couple gaussien de moyennes nulles, de variances 1 et de corrélation $0{,}6$. Quelles sont les pentes de $\operatorname{PD}_1$ et de $M_1$ ?
4. Les courbes ICE de $x_1$ sont-elles parallèles pour $f(x_1, x_2) = \sin x_1 + x_2^2$ ? Pour $f(x_1, x_2) = e^{x_1 - x_2}$ ?
5. Vrai ou faux : sur un échantillon, la dépendance partielle estimée est la moyenne des courbes ICE.

### MB6.Q3 — Intégrales de chemin : boucle fermée, chemin parcouru à l'envers, champ qui n'est pas un gradient, fonction homogène 🧠 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

1. $\mathbf{F} = \nabla f$ pour une fonction $f$ de classe $C^1$. Que vaut l'intégrale de $\mathbf{F}$ le long d'une boucle ?
2. L'intégrale d'un champ le long d'un chemin de $A$ à $B$ vaut $2{,}5$. Que vaut-elle le long du même chemin parcouru de $B$ vers $A$ ? Faut-il que le champ soit un gradient ?
3. Lesquels de ces champs sont des gradients : (A) $(3x^2, -2y)$ ; (B) $(x + y, 2x)$ ; (C) $(4x^3y, x^4 + 1)$ ?
4. $f(x, y) = (x^2 + y^2)^{3/2}$ est homogène de degré 3. En $(3, 4)$, depuis la référence $\mathbf{r} = \mathbf{0}$, quelles sont les parts de $x$ et de $y$ le long du segment ?
5. Vrai ou faux : pour toute fonction dérivable, la moyenne des chemins en escalier et le partage le long du segment donnent les mêmes parts.

### MB6.Q4 — Grilles et rangs : interpolation bilinéaire, centres ou coins alignés, ex aequo et transformation strictement croissante 🧠 ★ ⏱️ 4 min
*Fiche §5 et §6 · parcours C, E*

1. Vrai ou faux : au centre d'une case, l'interpolation bilinéaire donne la moyenne des quatre coins.
2. On agrandit une ligne de 4 cases en 10. Quelle est la coordonnée d'origine de la case d'arrivée 0 avec les centres alignés (avant le retour au bord), puis avec les coins alignés ? Et celle de la case 9 ?
3. Les rangs (rangs moyens aux ex aequo) de $(5{,}2 ;\ 3{,}8 ;\ 5{,}2 ;\ 7{,}1 ;\ 2{,}9)$.
4. Des valeurs $x_i > 0$ ont $\rho_S(x, y) = 0{,}7$. Que valent $\rho_S(\ln x, y)$ et $\rho_S(-x, y)$ ?

### MB6.Q5 — Indépendance, séparation, suffisance : quel critère pour quelle phrase, et lesquels se contredisent 🧠 ★ ⏱️ 5 min
*Fiche §7 · parcours C, E*

Une usine contrôle ses pièces sur deux lignes ($G$) : le contrôle rejette une pièce ($\hat Y = 1$), et $Y = 1$ pour une pièce défectueuse. Quel critère (indépendance, séparation ou suffisance) dit chacune des phrases 1 à 4 ?
1. Le contrôle rejette la même part des pièces sur les deux lignes.
2. Parmi les pièces défectueuses, le contrôle en rejette la même part sur les deux lignes ; parmi les bonnes aussi.
3. Parmi les pièces rejetées, la part de pièces défectueuses est la même sur les deux lignes ; parmi les pièces acceptées aussi.
4. Un score de $0{,}3$ correspond à 30 % de pièces défectueuses, sur chacune des deux lignes.
5. Les deux lignes ont des taux de défauts différents, et le contrôle vérifie à la fois l'indépendance et la séparation. Que peut-on dire de son taux de détection et de son taux de fausses alertes ?

### MB6.Q6 — Tirer au sort entre deux seuils, repondérer, lire l'écart de deux taux : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

Vrai ou faux ?
1. Tirer le seuil A avec la probabilité $q$, et le seuil B sinon, donne le taux de détection $q\,\mathrm{TPR}_A + (1 - q)\,\mathrm{TPR}_B$.
2. En faisant varier $q$, ce tirage atteint tous les points du segment qui joint les points ROC de A et de B.
3. Repondérer par $w(g, y) = \frac{P(g)\,P(y)}{P(g, y)}$ change la part des exemples de chaque groupe.
4. L'erreur type de l'écart de deux taux estimés sur des échantillons indépendants est la somme de leurs erreurs types.
5. Quadrupler l'effectif d'un seul des deux groupes divise par 2 l'erreur type de l'écart.

<a id="rappels"></a>

## 🔁 Rappels

### MB6.R1 — Parties d'un ensemble, factorielles et combinaisons (R4, R8) 🔁 ★ ⏱️ 6 min
*Fiche §1 · parcours C, E*

1. Combien de parties a un ensemble de 9 éléments ? Combien d'entre elles contiennent un élément donné ?
2. Combien de parties à 3 éléments a cet ensemble ?
3. De combien de façons peut-on ranger 5 livres sur une étagère ?
4. Vrai ou faux : $\binom{n}{k} = \binom{n}{n - k}$ pour $0 \le k \le n$.
5. Que vaut $\sum_{k=0}^{8}\binom{8}{k}$ ?

### MB6.R2 — La dérivée d'une fonction le long d'une courbe : gradient, vitesse et règle de la chaîne (M05b, M17) 🔁 ★ ⏱️ 6 min
*Fiche §4 · parcours C, E*

$f(x, y) = x^3y^2 - 2y$ et le chemin $\boldsymbol\gamma(t) = (1 + t,\ 2 - t)$.
1. $\nabla f(x, y)$, puis $\nabla f(2, 1)$.
2. $\boldsymbol\gamma(1)$ et $\boldsymbol\gamma'(t)$.
3. $(f\circ\boldsymbol\gamma)'(1)$ par la règle de la chaîne ; vérifie en dérivant $t \mapsto f(\boldsymbol\gamma(t))$ directement.
4. La dérivée directionnelle de $f$ en $(2, 1)$ dans la direction unitaire de $(1, 1)$ (3 décimales).
5. $\frac{\partial^2f}{\partial x\,\partial y}$ et $\frac{\partial^2f}{\partial y\,\partial x}$ en $(2, 1)$ : que dit le théorème de Schwarz ?

### MB6.R3 — La loi conditionnelle d'un couple gaussien : une moyenne affine en la valeur observée (M25a) 🔁 ★ ⏱️ 6 min
*Fiche §3 · parcours C, E*

$(X, Y)$ est un couple gaussien : $X \sim \mathcal{N}(20, 4^2)$, $Y \sim \mathcal{N}(50, 10^2)$, de corrélation $\rho = 0{,}3$.
1. La covariance de $X$ et $Y$.
2. $\mathbb{E}[Y \mid X = x]$, en fonction de $x$.
3. $\mathbb{E}[Y \mid X = 26]$.
4. $\mathbb{V}(Y \mid X = 26)$. Dépend-elle de la valeur observée ?
5. Que devient $\mathbb{E}[Y \mid X = x]$ si $\rho = 0$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les logarithmes et les racines), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex MB6.1 — Un conseil de quatre membres à vote pondéré : l'indice de Shapley-Shubik par les 24 ordres, un membre nul, deux membres de poids différents et de même pouvoir, et le nombre d'ordres tirés au hasard qui suffit (Hoeffding) ✏️ ★★ ⏱️ 30 min
**Objectif :** compter les pivots d'un vote pondéré sur tous les ordres, voir qu'un poids n'est pas un pouvoir, et dire combien d'ordres tirés au hasard suffisent.
**Prérequis :** fiche §1 ; R8 (factorielle), M11 §6 (Hoeffding) · **Parcours :** C, E

Un conseil de quartier a quatre membres, A, B, C et D, qui ont 8, 6, 3 et 1 voix (18 en tout). Une décision passe quand ses partisans réunissent au moins 11 voix : c'est le jeu $[11 ;\ 8, 6, 3, 1]$, où $v(S) = 1$ si la coalition $S$ gagne, 0 sinon.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre d'ordres, sur les 24, où chaque membre est pivot (A, B, C, D) | une liste de 4 entiers |
| b | l'indice de Shapley-Shubik de chaque membre (A, B, C, D) | une liste de 4 nombres (4 décimales) |
| c | D obtient une voix de plus (2 voix ; le quota reste 11) : les nouveaux comptes de pivots | une liste de 4 entiers |
| d | on estime l'indice d'un membre par la part des ordres où il est pivot, sur $m$ ordres tirés au hasard : le plus petit $m$ qui garantit, par l'inégalité de Hoeffding, une erreur d'au plus $0{,}05$ avec une probabilité au moins $0{,}96$ | un entier |

Dans ta copie : vérifie que $v(S \cup \{B\}) = v(S \cup \{C\})$ pour les quatre coalitions $S \subseteq \{A, D\}$ ; dis pourquoi D est nul en a).

### Ex MB6.2 — Trois hameaux partagent une conduite d'eau : la valeur de Shapley par les ordres, les dividendes de Harsanyi, le partage tronçon par tronçon, et les quatre axiomes vérifiés ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer une valeur de Shapley par les ordres et par les dividendes, et retrouver la règle de l'aéroport par les axiomes.
**Prérequis :** fiche §1 et §2 ; R4 (parties d'un ensemble) · **Parcours :** C, E

Trois hameaux, H1, H2 et H3, s'alignent dans une vallée, dans cet ordre depuis une source. Une conduite qui part de la source coûte 30 k€ jusqu'à H1, 21 k€ de plus jusqu'à H2, et 17 k€ de plus jusqu'à H3. Une coalition de hameaux paie la conduite jusqu'au plus éloigné d'entre eux : $c(S) = \max_{i \in S}c_i$, avec $c_1 = 30$, $c_2 = 51$, $c_3 = 68$ (k€), et $c(\varnothing) = 0$.

| | Question | Réponse attendue |
|---|---|---|
| a | la part de chaque hameau (H1, H2, H3), par les six ordres | une liste de 3 nombres (1 décimale) |
| b | les dividendes des trois paires $\{H1, H2\}$, $\{H1, H3\}$, $\{H2, H3\}$ | une liste de 3 nombres |
| c | le dividende des trois hameaux ensemble | un nombre |
| d | le devis du tronçon de H1 à H2 augmente de 8 k€ : les nouvelles parts | une liste de 3 nombres (1 décimale) |

Dans ta copie : écris $c$ comme la somme de trois jeux de tronçon, et dis ce que la symétrie, le joueur nul et l'efficacité imposent dans chacun ; retrouve a) par $\varphi_i = \sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$.

### Ex MB6.3 — Le rendement d'une parcelle selon la pluie et l'engrais : courbes ICE et dérivée croisée de deux modèles, puis la moyenne marginale et la moyenne conditionnelle quand pluie et engrais sont corrélés ✏️ ★★ ⏱️ 30 min
**Objectif :** lire des interactions sur des courbes ICE et une dérivée croisée, puis opposer la moyenne marginale et la moyenne conditionnelle d'un modèle quand ses variables sont corrélées.
**Prérequis :** fiche §3 ; M05b (dérivées croisées), M25a (loi conditionnelle d'un couple gaussien) · **Parcours :** C, E

Le rendement d'une parcelle de blé (en t/ha) dépend de la pluie du printemps $p$ (en centaines de mm) et de l'engrais $e$ (en centaines de kg/ha). Deux modèles écrits :
- modèle 1 : $f_1(p, e) = 1{,}5 + 0{,}6\,p + 2{,}4\,e - 0{,}4\,e^2$ ;
- modèle 2 : $f_2(p, e) = 7{,}5 - 0{,}5\,(p - e - 3)^2$, où le rendement dépend de l'écart entre la pluie et l'engrais.

Trois parcelles reçoivent $p = 4$ ; $5{,}5$ et $7$. Puis, sur toute la région, (pluie, engrais) est un couple gaussien $(P, E)$ : $P \sim \mathcal{N}(5{,}5 ;\ 1{,}2^2)$, $E \sim \mathcal{N}(1{,}5 ;\ 0{,}5^2)$, de corrélation $0{,}35$.

| | Question | Réponse attendue |
|---|---|---|
| a | modèle 1 : le gain de rendement quand l'engrais passe de 1 à 2, pour les trois parcelles | une liste de 3 nombres (1 décimale) |
| b | modèle 2 : le même gain, pour les trois parcelles | une liste de 3 nombres (1 décimale) |
| c | la dérivée croisée $\frac{\partial^2f}{\partial p\,\partial e}$ du modèle 1, puis du modèle 2 | une liste de 2 nombres |
| d | modèle 1 : la moyenne marginale $\operatorname{PD}(2) = \mathbb{E}[f_1(P, 2)]$, puis la moyenne conditionnelle $M(2) = \mathbb{E}[f_1(P, E) \mid E = 2]$ | une liste de 2 nombres (3 décimales) |
| e | modèle 1 : la pente de l'écart $M(v) - \operatorname{PD}(v)$ | un nombre (3 décimales) |

Dans ta copie : esquisse les trois courbes ICE de l'engrais pour chaque modèle ; écris $M(v) - \operatorname{PD}(v)$ et dis d'où vient l'écart.

### Ex MB6.4 — Le travail de deux forces entre deux points : un champ de gradient le long de trois chemins, puis un champ qui n'en est pas un (Schwarz) le long de deux chemins ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer l'intégrale d'un champ le long de plusieurs chemins, reconnaître un champ de gradient, et voir qu'un champ qui n'en est pas un dépend du chemin.
**Prérequis :** fiche §4 ; M05b (gradient, Schwarz), M17 (règle de la chaîne) · **Parcours :** C, E

Un petit robot va de $A = (1, 0)$ à $B = (2, 1)$ (en m), sous deux forces (en N) : $\mathbf{F} = \nabla f$, avec $f(x, y) = x^2y^2 + 3x$, et $\mathbf{G}(x, y) = (2y,\ 3x^2)$. Trois chemins : le segment $[AB]$ ; l'escalier $A \to (2, 0) \to B$ ; l'arc de parabole $\boldsymbol\gamma(t) = (1 + t,\ t^2)$, $t \in [0, 1]$. Le travail d'une force le long d'un chemin est son intégrale le long de ce chemin (fiche §4) ; calcule chaque intégrale.

| | Question | Réponse attendue |
|---|---|---|
| a | le travail de $\mathbf{F}$ le long du segment | un nombre |
| b | le travail de $\mathbf{F}$ sur les deux morceaux de l'escalier, horizontal puis vertical | une liste de 2 nombres |
| c | le travail de $\mathbf{F}$ le long de l'arc de parabole | un nombre |
| d | les dérivées croisées $\frac{\partial G_1}{\partial y}$ et $\frac{\partial G_2}{\partial x}$ au point $A$ | une liste de 2 nombres |
| e | le travail de $\mathbf{G}$ le long du segment, puis de l'escalier | une liste de 2 nombres |

Dans ta copie : compare a), b) et c) à $f(B) - f(A)$ ; dis ce que d) prouve sur $\mathbf{G}$, et ce qu'il ne garantit pas pour deux chemins donnés.

### Ex MB6.5 — La variation d'un coût à trois facteurs (prix, quantité, taux de change) partagée entre les facteurs : le long du segment, puis par la moyenne des six chemins en escalier, et pourquoi les deux partages coïncident ✏️ ★★ ⏱️ 30 min
**Objectif :** partager la variation d'un produit de trois facteurs le long du segment et par les chemins en escalier, et voir pourquoi les deux partages coïncident.
**Prérequis :** fiche §4 ; M02a (intégrale d'un polynôme), MB6.2 · **Parcours :** C

Une entreprise achète des pièces en dollars et paie en euros : $C = p\,q\,\tau$, avec le prix unitaire $p$ (en \$), la quantité $q$ et le taux de change $\tau$ (en €/\$). Au premier trimestre (la référence $\mathbf{r}$) : $p = 11{,}50$ \$, $q = 680$, $\tau = 0{,}93$ €/\$ ; au second (le point $\mathbf{x}$) : $p = 13{,}50$ \$, $q = 590$, $\tau = 0{,}87$ €/\$.

| | Question | Réponse attendue |
|---|---|---|
| a | la variation $C(\mathbf{x}) - C(\mathbf{r})$ (en €) | un nombre (2 décimales) |
| b | les parts du prix, de la quantité et du taux de change le long du segment | une liste de 3 nombres (2 décimales) |
| c | la contribution du taux de change dans l'ordre $(p, q, \tau)$, puis dans l'ordre $(\tau, p, q)$ | une liste de 2 nombres (2 décimales) |
| d | la moyenne des contributions sur les six chemins en escalier, pour $p$, $q$ et $\tau$ | une liste de 3 nombres (2 décimales) |

Dans ta copie : dis pourquoi b) et d) coïncident.

### Ex MB6.6 — Des relevés de capteurs sur une grille 3 × 4 : la dérivée d'un indice régional par un réchauffement uniforme, puis la grille agrandie deux fois par interpolation bilinéaire, centres ou coins alignés ✏️ ★★ ⏱️ 25 min
**Objectif :** lire la moyenne d'un gradient sur une grille comme la dérivée par un décalage uniforme, puis agrandir une grille par interpolation bilinéaire dans les deux conventions.
**Prérequis :** fiche §5 ; R3 (fonction affine par deux points), M05b (dérivée directionnelle) · **Parcours :** C, E

Douze capteurs couvrent une région en 3 lignes et 4 colonnes ; ils relèvent la température moyenne de mars $T$ (en °C), et chaque case a une surface cultivée $a$ (en centaines d'hectares) :
$$\mathbf{T} = \begin{pmatrix} 11{,}8 & 9{,}4 & 13{,}2 & 10{,}8 \\ 8{,}7 & 12{,}5 & 14{,}1 & 9{,}9 \\ 10{,}3 & 7{,}6 & 12{,}0 & 11{,}4 \end{pmatrix}, \qquad \mathbf{a} = \begin{pmatrix} 2 & 1 & 3 & 1 \\ 1 & 2 & 2 & 1 \\ 3 & 1 & 1 & 2 \end{pmatrix}.$$
L'indice régional est $y = \sum_{i, j}a_{ij}\max(0,\ T_{ij} - 10)$ (des degrés au-dessus de 10 °C, pondérés par les surfaces). Puis on agrandit la grille $\mathbf{T}$ en $6 \times 8$ par interpolation bilinéaire.

| | Question | Réponse attendue |
|---|---|---|
| a | l'indice $y$ | un nombre (1 décimale) |
| b | la dérivée de $y$ par un réchauffement uniforme de $\delta$ °C, en $\delta = 0$ | un entier |
| c | l'indice après un réchauffement uniforme de 1 °C | un nombre (1 décimale) |
| d | centres alignés : la coordonnée d'origine $c(u)$ des 6 lignes de la grille agrandie, avant le retour au bord | une liste de 6 nombres (2 décimales) |
| e | coins alignés : la coordonnée d'origine des 6 lignes | une liste de 6 nombres (2 décimales) |
| f | la valeur de la case (ligne 4, colonne 5) de la grille agrandie, centres alignés puis coins alignés | une liste de 2 nombres (2 décimales) |

Dans ta copie : écris la moyenne des 12 dérivées partielles $\frac{\partial y}{\partial T_{ij}}$ et relie-la à b) ; dis pourquoi c) n'est pas $y + $ b).

### Ex MB6.7 — Un contrôle de pièces sur deux lignes de production aux taux de défauts différents : les taux de rejet sous la séparation, un tirage au sort entre deux seuils pour atteindre un taux de détection, et les poids qui rendent ligne et défaut indépendants ✏️ ★★ ⏱️ 30 min
**Objectif :** voir que la séparation impose des taux de rejet différents, atteindre un taux de détection en tirant au sort entre deux seuils, et repondérer une table.
**Prérequis :** fiche §7 et §8 ; M03 §7 et §8 (courbe ROC, taux par groupe) · **Parcours :** C, E

Une usine fabrique la même pièce sur deux lignes : 6 % des pièces de la ligne 1 sont défectueuses, 14 % de celles de la ligne 2. Un contrôle automatique rejette une pièce ($\hat Y = 1$) ; $Y = 1$ pour une pièce défectueuse. Sur les deux lignes, il a le même taux de détection, $0{,}92$, et le même taux de fausses alertes, $0{,}04$ : il vérifie la séparation.

Sur la ligne 2, le contrôle repose sur un score : le seuil A donne (taux de fausses alertes, taux de détection) $= (0{,}03 ;\ 0{,}74)$, le seuil B $(0{,}09 ;\ 0{,}96)$. Pour détecter 90 % des pièces défectueuses, on tire au sort, pièce par pièce, le seuil A avec la probabilité $q$, le seuil B sinon.

Enfin, une table de comptes : ligne 1, 1 300 pièces dont 78 défectueuses ; ligne 2, 1 100 pièces dont 154 défectueuses.

| | Question | Réponse attendue |
|---|---|---|
| a | le taux de rejet de chaque ligne, avec le contrôle qui vérifie la séparation | une liste de 2 nombres (4 décimales) |
| b | la probabilité $q$ | un nombre (4 décimales) |
| c | le taux de fausses alertes obtenu par le tirage | un nombre (4 décimales) |
| d | les poids $w(1, \text{défaut})$, $w(1, \text{sans défaut})$, $w(2, \text{défaut})$, $w(2, \text{sans défaut})$ qui rendent ligne et défaut indépendants | une liste de 4 nombres (4 décimales) |
| e | le taux de défauts pondéré de chaque ligne | une liste de 2 nombres (4 décimales) |

Dans ta copie : dis pourquoi a) montre que l'indépendance ne tient pas ; vérifie que les poids gardent les deux marges.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex MB6.8 — Unicité de la valeur de Shapley : les jeux d'unanimité forment une base, et les quatre axiomes imposent φ_i = Σ_{T ∋ i} d_T / |T| ∂ ★★★ ⏱️ 35 min
**Objectif :** démontrer l'inversion de Möbius des dividendes, puis que les quatre axiomes ne laissent qu'une règle de partage.
**Prérequis :** fiche §2 ; R4 (parties d'un ensemble, formule du binôme), M12a (base d'un espace vectoriel) · **Parcours :** C

On fixe $n$ joueurs. Un jeu est une fonction $v$ des $2^n$ coalitions dans $\mathbb{R}$ ; les jeux forment un espace vectoriel de dimension $2^n$. Pour $T \ne \varnothing$, $u_T$ vaut 1 sur les coalitions qui contiennent $T$, 0 ailleurs ; $u_\varnothing$ vaut 1 partout.
1. Pour un jeu $v$, pose $d_T = \sum_{S \subseteq T}(-1)^{\lvert T\rvert - \lvert S\rvert}v(S)$. Montre que $v(S) = \sum_{T \subseteq S}d_T$ pour toute coalition $S$.
2. Déduis-en que les $2^n$ jeux $u_T$ forment une base de l'espace des jeux.
3. Soit une règle de partage $\varphi$ qui vérifie l'efficacité, la symétrie et le joueur nul. Pour $T \ne \varnothing$ et un réel $c$, montre que $\varphi_i(c\,u_T) = \frac{c}{\lvert T\rvert}$ si $i \in T$, et 0 sinon. Que vaut $\varphi(c\,u_\varnothing)$ ?
4. On ajoute l'additivité. Montre que $\varphi_i(v) = \sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$ pour tout jeu $v$.
5. La valeur de Shapley vérifie les quatre axiomes (fiche §2). Conclus.

### Ex MB6.9 — Un score calibré dans un groupe vérifie p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; si deux groupes ont les mêmes moyennes de scores chez leurs positifs et chez leurs négatifs, leurs taux de base sont égaux ou le score est parfait ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer l'identité d'un score calibré par l'espérance totale, puis l'impossibilité de Kleinberg, Mullainathan et Raghavan.
**Prérequis :** fiche §7 ; M25b §2 (espérance totale) · **Parcours :** C, E

Dans un groupe, un score $S$ à valeurs dans $[0, 1]$ (en nombre fini) est **calibré** : $P(Y = 1 \mid S = s) = s$ pour chaque valeur $s$ qu'il prend. On note $p = P(Y = 1)$, avec $0 < p < 1$, $a = \mathbb{E}[S \mid Y = 1]$ et $b = \mathbb{E}[S \mid Y = 0]$.
1. Montre que $\mathbb{E}[S] = p$.
2. En écrivant $\mathbb{E}[S]$ par l'espérance totale sachant $Y$, déduis-en $p\,(1 - a) = (1 - p)\,b$.
3. Deux groupes ont des scores calibrés de mêmes $a$ et $b$. Montre que, si $1 - a + b \ne 0$, leurs taux de base sont égaux. Montre que $1 - a + b = 0$ impose $S = Y$ presque sûrement.
4. Contrôle. Sur la ligne 1 de MB6.7, un score annonce pour chaque pièce une probabilité d'être défectueuse ; sur 1 000 pièces : 750 pièces à $0{,}02$, dont 15 défectueuses ; 150 à $0{,}1$, dont 15 ; 100 à $0{,}3$, dont 30. Vérifie la calibration, calcule $p$, $a$ et $b$, puis l'identité de 2. Si la ligne 2 (14 % de défauts) avait un score calibré de mêmes $a$ et $b$, quel serait son taux de base ?

### Ex MB6.10 — Indépendance et séparation ne tiennent ensemble, quand les taux de base diffèrent, que pour une décision qui ignore le label ; la repondération P(g)P(y)/P(g, y) rend groupe et label indépendants sans changer leurs marges ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer en quelques lignes l'incompatibilité de l'indépendance et de la séparation, puis ce que fait la repondération.
**Prérequis :** fiche §7 et §8 ; M03 (probabilités totales, indépendance) · **Parcours :** C, E

1. Deux groupes ont des taux de base $p_1 \ne p_2$ ; une décision a, dans le groupe $g$, le taux de détection $t_g$ et le taux de fausses alertes $f_g$. Écris $P(\hat Y = 1 \mid G = g)$ avec $p_g$, $t_g$ et $f_g$. Montre que la séparation ($t_1 = t_2 = t$ et $f_1 = f_2 = f$) et l'indépendance ensemble imposent $t = f$, puis que $t = f$ signifie $\hat Y \perp Y$ dans chaque groupe. La réciproque est-elle vraie ?
2. Toutes les cases d'une table $(g, y)$ ont $P(g, y) > 0$, et $w(g, y) = \frac{P(g)\,P(y)}{P(g, y)}$. Montre que $Q(g, y) = w(g, y)\,P(g, y)$ est une loi de probabilité, qu'elle a les marges $P(g)$ et $P(y)$, et que $G$ et $Y$ y sont indépendants.

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB6.11 — Pont : l'écart des taux de détection de deux laboratoires et son intervalle, par l'erreur type d'une différence de deux proportions, qui se lit avec le nombre d'échantillons positifs de chacun 🔗 ★ ⏱️ 15 min
**Objectif :** chiffrer l'incertitude de l'écart de deux taux de détection, et voir lequel des deux effectifs la fixe.
**Prérequis :** fiche §8 ; M02b (variance d'une différence), M08 §5 (Wald) · **Parcours :** C, E

Deux laboratoires analysent des prélèvements d'eau et signalent une contamination. Le laboratoire A a reçu 900 prélèvements, dont 28 contaminés, et en a signalé 20 ; le laboratoire B en a reçu 4 000, dont 520 contaminés, et en a signalé 448. Les deux échantillons sont indépendants.

| | Question | Réponse attendue |
|---|---|---|
| a | les taux de détection de A et de B | une liste de 2 nombres (4 décimales) |
| b | l'erreur type de l'écart $\mathrm{TPR}_B - \mathrm{TPR}_A$ | un nombre (4 décimales) |
| c | l'intervalle de Wald à 95 % de cet écart | une liste de 2 nombres (3 décimales) |
| d | l'erreur type de l'écart si A avait analysé quatre fois plus de prélèvements contaminés (112), au même taux de détection | un nombre (4 décimales) |

Dans ta copie : dis ce que c) permet de conclure, puis, en une phrase, comment un bootstrap stratifié estimerait cet intervalle.

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB6.12 — Expliquer avec trois amis qui partagent un taxi pourquoi on moyenne l'apport de chacun sur tous les ordres d'arrivée 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule pourquoi la valeur de Shapley fait la moyenne des apports sur tous les ordres.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

Trois amis rentrent d'un concert dans le même taxi. Le taxi suit une seule route : il dépose d'abord Léa, puis Max, puis Sam, qui habite le plus loin. Ils veulent partager la course équitablement, et Max propose : « chacun paie ce que sa présence ajoute au prix ».

Réponds-lui en 5 à 8 phrases, sans formule ni calcul : pourquoi « ce que sa présence ajoute » dépend de qui est déjà dans le taxi ; pourquoi imaginer les amis monter dans un ordre ou dans un autre change ce partage ; pourquoi on fait la moyenne sur tous les ordres ; ce que cette moyenne garantit (tout le prix est payé, et deux amis qui habiteraient au même endroit paieraient autant) ; et qui paie le plus.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### MB6.E1 — « La valeur de Shapley est la seule répartition qui respecte quatre règles simples : lesquelles, et pourquoi suffisent-elles ? » 💼 ★ ⏱️ 10 min
*Fiche §2 · parcours C*

« La valeur de Shapley est la seule répartition qui respecte quatre règles simples : lesquelles, et pourquoi suffisent-elles ? »

Ta réponse doit nommer les quatre règles et dire en une phrase ce que garantit chacune ; donner l'argument en deux temps (des jeux simples sur lesquels les règles imposent le partage, puis l'additivité) ; dire pourquoi la valeur de Shapley existe ; et nommer la règle la plus discutable.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/mb6_shapley_equite/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| MB6.13 | Les poids des coalitions dans la valeur de Shapley, exacts ou en flottants · `coalition_weights` | 🔨 | ★ | 10 | C, E |
| MB6.14 | Les dividendes de Harsanyi d'un jeu donné par sa fonction caractéristique · `harsanyi_dividends` | 🔨 | ★★ | 25 | C |
| MB6.15 | L'intégrale d'un champ de vecteurs le long d'une ligne brisée, par la méthode de Simpson sur chaque segment · `line_integral` | 🔨 | ★★ | 25 | C, E |
| MB6.16 | La corrélation de rangs de Spearman, ex aequo compris · `spearman_rho` | 🔨 | ★ | 20 | C, E |
| MB6.17 | Prédire l'intégrale d'un champ de gradient et d'un champ tournant le long d'une boucle triangulaire, dans un sens, dans l'autre et deux fois, puis vérifier | 🔮 | ★ | 15 | C |
| MB6.18 | Deux mesures corrélées : la moyenne marginale (dépendance partielle) et la moyenne conditionnelle d'une même fonction, simulées pour plusieurs corrélations et comparées aux formules gaussiennes | 🔬 | ★★ | 25 | C, E |
| MB6.19 | Les lignes de niveau d'une fonction de deux variables, deux chemins entre les mêmes points, et l'intégrale du gradient cumulée le long de chacun | 🎨 | ★ | 20 | C |
| MB6.20 | Chasse à l'erreur : des poids de coalition sans le facteur 1/n, des ex aequo classés dans l'ordre d'apparition, une interpolation linéaire aux poids échangés | 🐛 | ★ | 20 | C, E |
| MB6.21 | Un test de propriété sur des lignes brisées tirées au hasard : le chemin inversé change le signe, un segment coupé en deux ne change rien, un champ de gradient donne f(fin) − f(début) | 🛠️ | ★ | 20 | C |
| MB6.22 | Défi : les indices de Shapley-Shubik exacts d'un conseil de 25 membres, sans parcourir ses coalitions une à une, en comptant par taille et par poids celles où chaque membre est pivot | 🏆 | ★★★ | 40 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les quatre 🔨 complètent ta copie `mon_travail/mymath/attribution.py` (**mymath :** `attribution.py`), dont la docstring du module dit ce qui est permis : NumPy et les modules `math`, `fractions` et `itertools` ; ni SciPy (`rankdata`, `spearmanr`, `pearsonr`, `scipy.integrate`), ni `np.corrcoef`, ni `np.cov`, ni le module `statistics`, ni pandas : les tests comparent tes résultats avec `math.comb`, `fractions`, `scipy.integrate.quad` et `scipy.stats.spearmanr` ; les imports relatifs de tes propres modules sont permis (`from .integrate import simpson`, M02a) ; ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de sa fonction dans `tests/test_mb6_attribution.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.attribution.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier sont recopiées dans une cellule du notebook.

**MB6.13 · 🔨 `coalition_weights(n_players, exact=False)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments (`n_players` un entier $\ge 1$, pas un booléen ni un flottant ; `exact` un booléen), puis rends les $n$ poids $w(0), \ldots, w(n - 1)$, en `Fraction` ou en flottants. Lance le groupe de tests. Ensuite : a) les 9 poids pour $n = 9$, exacts (une liste de 9 fractions) ; b) pour $n = 25$, le conseil du 🏆, le rapport $\frac{w(0)}{w(12)}$ (un entier). Ce qu'il faut regarder : pourquoi une coalition de taille moyenne pèse-t-elle si peu, alors que chaque taille pèse $\frac1n$ en tout ?

**MB6.14 · 🔨 `harsanyi_dividends(v, n_players)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments ; appelle `v` une fois par coalition (taille par taille, avec `itertools.combinations`) et garde les valeurs ; puis, pour chaque $T$, la somme alternée sur ses parties ; rends le dictionnaire dans l'ordre de la docstring. Lance le groupe de tests. Ensuite : a) les hameaux de MB6.2 (numérotés 0, 1, 2, besoins 30, 51 et 68) : $d_{\{0, 1\}}$, $d_{\{0, 2\}}$, $d_{\{1, 2\}}$, $d_{\{0, 1, 2\}}$ (une liste de 4 nombres, à comparer à ta copie) ; b) quatre maraîchers partagent un stand au marché ; le notebook fournit `TABLE_14`, le bénéfice hebdomadaire $v(S)$ de chaque coalition (en centaines d'euros), un dictionnaire indexé par des `frozenset` : leurs valeurs de Shapley par $\varphi_i = \sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$ (une liste de 4 nombres) ; c) $d_{\{1, 2\}}$ et $d_{\{0, 1, 3\}}$ (une liste de 2 nombres) ; d) le conseil de MB6.1 (A, B, C, D numérotés 0 à 3) : $d_{\{0, 1\}}$, $d_{\{0, 2\}}$, $d_{\{0, 1, 2\}}$ (une liste de 3 nombres). Ce qu'il faut regarder : quel dividende du stand est négatif, et que dit-il des maraîchers 1 et 2 ? Dans le conseil, pourquoi $d_{\{0, 1, 2\}}$ est-il négatif ?

**MB6.15 · 🔨 `line_integral(field, points, n_sub=20)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments (des points 2-D finis, au moins deux lignes ; `n_sub` un entier pair $\ge 2$ ; ce que rend `field`) ; pour chaque segment de $\mathbf{a}$ à $\mathbf{b}$, la règle de Simpson (M02a) sur les $n_{\text{sub}} + 1$ valeurs de $t \mapsto \mathbf{F}(\mathbf{a} + t(\mathbf{b} - \mathbf{a}))\cdot(\mathbf{b} - \mathbf{a})$, en appelant `field` point par point ; la somme sur les segments. Lance le groupe de tests. Ensuite : a) $\mathbf{F}$ de MB6.4 le long du segment $[AB]$, puis de l'escalier $A \to (2, 0) \to B$ (une liste de 2 nombres) ; b) $\mathbf{G}$ de MB6.4 le long des deux mêmes chemins (une liste de 2 nombres) ; c) $\mathbf{G}$ le long de lignes brisées qui suivent l'arc $\boldsymbol\gamma(t) = (1 + t, t^2)$, avec 4, 16 et 64 segments de même pas en $t$ (une liste de 3 nombres). Ce qu'il faut regarder : l'intégrale de $\mathbf{G}$ le long de l'arc vaut $\frac{55}{6}$ ; par combien l'écart est-il divisé quand le nombre de segments est multiplié par 4 ? Pourquoi $\mathbf{F}$ donne-t-il la même valeur pour toutes ces lignes brisées ?

**MB6.16 · 🔨 `spearman_rho(x, y)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments ; les rangs de chaque échantillon (`np.argsort`, puis le rang moyen de chaque groupe de valeurs égales, comptés à partir de 1) ; la formule de Pearson sur les rangs centrés ; `nan` quand une somme de carrés est nulle. Lance le groupe de tests. Ensuite : le notebook fournit `MOHS_16` et `VICKERS_16`, la dureté de neuf échantillons de minéraux sur l'échelle de Mohs (des degrés et des demi-degrés, avec un ex aequo) et par un essai de Vickers (en HV) : a) $\rho_S$(Mohs, Vickers) (un nombre) ; b) $\rho_S$(Mohs, $\frac{1}{\text{Vickers}}$) (un nombre). Ce qu'il faut regarder : pourquoi la formule $1 - \frac{6\sum d_i^2}{n(n^2 - 1)}$ n'est-elle ici qu'une approximation ? Pourquoi b) se déduit-il de a) sans calcul ?

**MB6.17 · 🔮 Une boucle triangulaire.** Le triangle $A = (1, 0)$, $B = (4, 1)$, $C = (2, 3)$, et deux champs : $\mathbf{F}$ de MB6.4 (un gradient) et le champ tournant $\mathbf{R}(x, y) = (-y, x)$. **Avant d'exécuter**, prédis (une lettre chacune) : a) l'intégrale de $\mathbf{F}$ le long de la boucle $A \to B \to C \to A$ : (A) 0 ; (B) l'aire du triangle ; (C) elle dépend du triangle choisi ; b) celle de $\mathbf{R}$ le long de $A \to B \to C \to A$ : (A) 0 ; (B) l'aire du triangle ; (C) deux fois l'aire du triangle ; c) celle de $\mathbf{R}$ le long de $A \to C \to B \to A$ : (A) la même qu'en b) ; (B) l'opposée de b) ; (C) 0 ; d) celle de $\mathbf{R}$ quand on fait deux fois le tour $A \to B \to C \to A$ : (A) la même qu'en b) ; (B) le double de b) ; (C) le carré de b). Puis mesure avec `line_integral` : e) les quatre intégrales de a) à d) (une liste de 4 nombres). Ce qu'il faut regarder (après l'expérience) : l'aire du triangle vaut-elle ce que tu pensais ? Qu'est-ce qui, dans $\mathbf{R}$, tourne avec la boucle ? Une boucle d'intégrale nulle suffirait-elle à prouver qu'un champ est un gradient ?

**MB6.18 · 🔬 Deux mesures corrélées d'une serre.** La température $T$ (°C) et l'humidité $U$ (%) d'une serre forment un couple gaussien : $T \sim \mathcal{N}(22, 3^2)$, $U \sim \mathcal{N}(70, 8^2)$, de corrélation $\rho$. Une fonction écrite donne la croissance relative d'une moisissure : $f(T, U) = \exp\big(0{,}1\,(T - 22) + 0{,}05\,(U - 70)\big)$. On fixe $T = 26$. Pour $\rho = 0$ ; $0{,}5$ et $0{,}9$ : a) calcule par les formules $\operatorname{PD}(26) = \mathbb{E}[f(26, U)]$ et $M(26) = \mathbb{E}[f(T, U) \mid T = 26]$ (une liste de 4 nombres : $\operatorname{PD}(26)$, puis $M(26)$ pour les trois $\rho$) ; tu peux utiliser $\mathbb{E}[e^{cZ}] = e^{c\mu + c^2\sigma^2/2}$ pour $Z \sim \mathcal{N}(\mu, \sigma^2)$ ; b) tire 200 000 couples pour chaque $\rho$ (le notebook fournit le générateur) ; estime $\operatorname{PD}(26)$ par la moyenne des $f(26, U_i)$, et $M(26)$ par la moyenne des $f(T_i, U_i)$ sur les points où $\lvert T_i - 26\rvert \le 0{,}25$ (une liste de 6 nombres : pour chaque $\rho$, l'estimation de $\operatorname{PD}$ puis celle de $M$). Ce qu'il faut regarder : pour quel $\rho$ les deux moyennes sont-elles égales ? Pourquoi l'estimation de $M$ est-elle plus dispersée que celle de $\operatorname{PD}$ ? Que deviendrait-elle avec une fenêtre dix fois plus étroite ?

**MB6.19 · 🎨 Deux chemins dans un paysage.** Le notebook fournit `f_19(x, y)` $= 3e^{-((x - 1)^2 + (y - 1)^2)} - 2e^{-((x + 1)^2 + y^2)/2} + 0{,}2\,x$ et son gradient `grad_19`. Écris `draw_19(ax_map, ax_cum)`, qui trace : dans `ax_map`, les lignes de niveau de $f$ sur $[-3, 3]^2$ et deux chemins de $A = (-2{,}5 ;\ -1)$ à $B = (2, 2)$, le segment et la ligne brisée $A \to (0, -2) \to (2{,}5 ;\ 0) \to B$, avec une légende ; dans `ax_cum`, pour chaque chemin, l'intégrale du gradient de $f$ depuis $A$ jusqu'au point courant, en fonction de la longueur parcourue (avec `line_integral` sur le début du chemin), avec des noms d'axes ; la fonction rend les deux tableaux de cumuls tracés. Relève : a) $f(B) - f(A)$ (un nombre) ; b) le plus grand cumul le long du segment, puis le long de la ligne brisée (une liste de 2 nombres). Ce qu'il faut regarder : où chaque chemin monte-t-il et descend-il ? Pourquoi les deux cumuls finissent-ils au même nombre ?

**MB6.20 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `weights_bad(n)` doit rendre les poids $w(s)$ de la valeur de Shapley ; elle divise $s!\,(n - 1 - s)!$ par $(n - 1)!$ au lieu de $n!$. Il l'a vérifiée pour $n = 1$.
- (2) `ranks_bad(x)` doit rendre les rangs, rangs moyens aux ex aequo ; elle donne aux ex aequo des rangs différents, dans l'ordre où ils apparaissent. Il l'a vérifiée sur un échantillon sans ex aequo.
- (3) `lerp_bad(a, b, t)` doit interpoler entre $a$ (en $t = 0$) et $b$ (en $t = 1$) ; elle rend $(1 - t)\,b + t\,a$. Il l'a vérifiée en $t = \frac12$.

Trouve et corrige chaque erreur dans le code du collègue lui-même : les fonctions corrigées s'appellent `weights_fixed`, `ranks_fixed` et `lerp_fixed`, avec les mêmes arguments, et n'appellent **pas** `mymath` (la vérification le contrôle). Puis réponds : a) pour $n = 7$, $\sum_s\binom{6}{s}w(s)$ avec la fonction corrigée, puis avec la fonction fautive (une liste de 2 nombres) ; b) $\rho_S$ des deux échantillons `X_20` et `Y_20` du notebook (avec des ex aequo), calculée par Pearson sur les rangs de la fonction corrigée, puis sur ceux de la fonction fautive (une liste de 2 nombres) ; c) l'interpolation en $t = 0{,}3$ entre 12 et 20, corrigée puis fautive (une liste de 2 nombres). Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés.

**MB6.21 · 🛠️ Un test de propriété.** Écris trois fonctions qui testent une méthode qu'on leur passe, de la même signature que `line_integral(field, points)`, et rendent `True` si la propriété tient, `False` sinon : `reversed_changes_sign_21(method)`, qui vérifie, sur plusieurs lignes brisées tirées au hasard dans le plan et un champ qui n'est pas un gradient, que parcourir la ligne à l'envers change le signe ; `split_changes_nothing_21(method)`, qui vérifie qu'ajouter un sommet à l'intérieur d'un segment (en un point tiré au hasard sur ce segment) ne change pas le résultat ; `gradient_gives_difference_21(method)`, qui vérifie, pour le gradient d'une fonction dont tu connais l'expression, que le résultat vaut $f(\text{fin}) - f(\text{début})$. Chaque comparaison se fait à $10^{-9}$ près en valeur relative, plus finement que la tolérance par défaut de `np.allclose` (`rtol=1e-5`, `atol=1e-8`). Prends des champs qui ne sont pas polynomiaux de degré au plus 3 en $t$ sur un segment (la règle de Simpson y serait exacte, et une méthode grossière passerait). La vérification lance tes trois tests sur `line_integral` de la référence, puis sur des méthodes fausses cachées, passées sous un nom neutre, une par clause de l'énoncé, que chaque test doit refuser quand sa propriété est fausse. Relève : a) les résultats de tes trois tests sur `line_integral` de la référence (une liste de 3 booléens). Ce qu'il faut regarder : pourquoi un champ polynomial de bas degré laisserait-il passer une méthode fausse ? Pourquoi tirer les lignes brisées au hasard, et plusieurs fois ?

**MB6.22 · 🏆 Défi : un conseil de 25 membres.** Le notebook fournit `WEIGHTS_22`, les voix des 25 membres d'un conseil (des entiers de 1 à 12, 98 voix en tout), et `QUOTA_22` $= 66$. Écris `shapley_shubik_22(weights, quota)`, qui rend les indices de Shapley-Shubik de tous les membres, exacts (des flottants), sans parcourir les coalitions une à une : pour chaque membre $i$, compte les coalitions des autres membres par taille et par poids total (un tableau rempli membre par membre), garde celles où $i$ est pivot, et pondère par `coalition_weights`. **Critère de réussite :** pour le conseil du notebook et pour trois séries de cinq conseils cachés de 30 à 50 membres, tirés à nouveau à chaque exécution (une majorité simple, une majorité qualifiée, un membre au veto, quelques grands et beaucoup de petits, des poids presque égaux), chaque indice est à $10^{-9}$ près celui de la référence, et ta fonction traite les quinze conseils cachés en moins d'une minute. Elle ne doit pas exécuter le code du module caché du défi (`solutions/challenges/mb6_22.py`) : la vérification le contrôle. Relève : a) l'indice du membre 0, qui a 12 voix (un nombre) ; b) les 25 indices (une liste de 25 nombres). Point de départ : pour un conseil de 30 membres, les coalitions sans un membre sont $2^{29}$, plus de 500 millions ; mais leurs poids totaux sont des entiers de 0 à quelques centaines.
