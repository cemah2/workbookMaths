# MB6 · Shapley, intégrales de chemin et équité — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture, qui accepte toute démonstration correcte. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB6.Q1 — Jeux coopératifs : ordres ou coalitions, poids d'une coalition, et ce que garantit chaque axiome

1. $7! = 5\,040$ ordres ; $6! = 720$ où $i$ arrive le premier, soit $\frac17$ : chaque place est également probable (fiche §1).
2. $w(2) = \frac{2!\,4!}{7!} = \frac{48}{5\,040} = \frac{1}{105}$. Il y a $\binom62 = 15$ coalitions de 2 joueurs sans $i$ : ensemble, $\frac{15}{105} = \frac17$. Chaque taille, de 0 à 6, pèse $\frac17$ : le nombre de joueurs arrivés avant $i$ est uniforme (fiche §1).
3. (a) le joueur nul ; (b) la symétrie ; (c) l'additivité ; (d) l'efficacité.
4. Faux. Dans $[5 ;\ 4, 2, 1, 1]$, le membre de 4 voix est pivot dès qu'il n'arrive pas le premier (18 ordres sur 24) ; chacun des trois autres n'est pivot que s'il arrive juste après lui, en deuxième position (2 ordres) : le membre de 2 voix a le pouvoir d'un membre d'une voix. Le pouvoir ne suit pas les voix (MB6.1 en donne un autre exemple).
5. Vrai : les contributions d'un même ordre se télescopent en $v(N) - v(\varnothing)$, donc leur moyenne sur $m$ ordres aussi (fiche §1).

### MB6.Q2 — Fixer une variable : moyenne marginale ou conditionnelle, courbes ICE parallèles ou non

1. (A). (B) est la moyenne conditionnelle $M_j(v)$ ; (C) est la courbe ICE d'un seul point ; la dépendance partielle en est la moyenne, sur la loi de $\mathbf{X}_{-j}$ (fiche §3).
2. Quand $X_j$ est indépendante de $\mathbf{X}_{-j}$ : la loi de $\mathbf{X}_{-j}$ sachant $X_j = v$ est alors sa loi marginale.
3. $\operatorname{PD}_1(v) = v - 4\,\mathbb{E}[X_2] = v$ : pente 1. $\mathbb{E}[X_2 \mid X_1 = v] = 0{,}6\,v$ (M25a), donc $M_1(v) = v - 4 \times 0{,}6\,v = -1{,}4\,v$ : pente $-1{,}4$. La moyenne conditionnelle prête à $x_1$ l'effet de $x_2$, qui l'accompagne : elle change même de sens.
4. Oui : $f$ est une fonction de $x_1$ plus une fonction de $x_2$, et deux courbes ICE diffèrent de $x_2^2 - x_2'^2$. Non : $\frac{\partial^2f}{\partial x_1\partial x_2} = -e^{x_1 - x_2} \ne 0$ ; les courbes $v \mapsto e^{v}e^{-x_2}$ sont des multiples les unes des autres, pas des translatées.
5. Vrai : c'est la définition de la fiche §3, la moyenne des $f(v, \mathbf{x}_{i,-j})$.

### MB6.Q3 — Intégrales de chemin : boucle fermée, chemin parcouru à l'envers, champ qui n'est pas un gradient, fonction homogène

1. 0, par le théorème du gradient : $f(\text{fin}) - f(\text{début}) = 0$ pour une boucle.
2. $-2{,}5$, pour **tout** champ : parcourir le chemin à l'envers change le signe de la vitesse.
3. (A) et (C) : (A) est le gradient de $x^2 - y^3$, (C) celui de $x^4y + y$. (B) n'en est pas un : $\frac{\partial F_1}{\partial y} = 1 \ne \frac{\partial F_2}{\partial x} = 2$.
4. $f(3, 4) = 125$ ; $\partial_xf = 3x\sqrt{x^2 + y^2}$, donc $x\,\partial_xf = 3 \times 9 \times 5 = 135$, et $y\,\partial_yf = 3 \times 16 \times 5 = 240$ ; leur somme $375 = 3 \times 125$ (Euler). Parts : $\frac{135}{3} = 45$ et $\frac{240}{3} = 80$, de somme $125 = f(3, 4) - f(0, 0)$.
5. Faux : les deux partages coïncident pour une fonction multilinéaire (et pour une somme d'une telle fonction et de fonctions d'une seule coordonnée), pas en général : la fiche §4 en montre une qui n'est pas multilinéaire et dont les deux partages diffèrent.

### MB6.Q4 — Grilles et rangs : interpolation bilinéaire, centres ou coins alignés, ex aequo et transformation strictement croissante

1. Vrai : en $(s, t) = (\frac12, \frac12)$, les quatre poids valent $\frac14$.
2. Centres alignés : $\xi(u) = (u + \frac12)\frac{4}{10} - \frac12$, donc $\xi(0) = -0{,}3$ (ramené à 0) et $\xi(9) = 3{,}3$ (ramené à 3). Coins alignés : $\xi(u) = u\,\frac{3}{9} = \frac u3$, donc $\xi(0) = 0$ et $\xi(9) = 3$. Avant le retour au bord, l'écart vaut $0{,}3 = \frac12\big(1 - \frac{4}{10}\big)$ aux deux bords.
3. $(3{,}5 ;\ 2 ;\ 3{,}5 ;\ 5 ;\ 1)$ : les deux $5{,}2$ occupent les places 3 et 4.
4. $\rho_S(\ln x, y) = 0{,}7$ : $\ln$ est strictement croissante et garde les rangs. $\rho_S(-x, y) = -0{,}7$ : $x \mapsto -x$ renverse l'ordre, le rang $r_i$ devient $n + 1 - r_i$, et la corrélation change de signe.

### MB6.Q5 — Indépendance, séparation, suffisance : quel critère pour quelle phrase, et lesquels se contredisent

1. L'indépendance, $\hat Y \perp G$.
2. La séparation, $\hat Y \perp G \mid Y$ : mêmes taux de détection et de fausses alertes.
3. La suffisance, $Y \perp G \mid \hat Y$.
4. La calibration dans chaque groupe, qui est la suffisance pour le score : $Y \perp G \mid S$.
5. Ils sont égaux, sur chaque ligne : le contrôle rejette une pièce défectueuse aussi souvent qu'une bonne ; il ne regarde pas le défaut (∂ MB6.10).

### MB6.Q6 — Tirer au sort entre deux seuils, repondérer, lire l'écart de deux taux : vrai ou faux

1. Vrai : la formule des probabilités totales, en conditionnant par le seuil tiré, indépendant du label (fiche §8).
2. Vrai : le point $(\mathrm{FPR}, \mathrm{TPR})$ vaut $q\,(\mathrm{FPR}_A, \mathrm{TPR}_A) + (1 - q)\,(\mathrm{FPR}_B, \mathrm{TPR}_B)$, et décrit la corde quand $q$ va de 0 à 1.
3. Faux : la loi pondérée garde les deux marges, $P(g)$ et $P(y)$ (∂ MB6.10).
4. Faux : ce sont les **variances** qui s'ajoutent ; l'erreur type est la racine de la somme des carrés des deux erreurs types, plus petite que leur somme.
5. Faux : seul le terme de ce groupe est divisé par 4 ; l'erreur type de l'écart baisse moins que de moitié, sauf si l'autre terme est nul (🔗 MB6.11 d).

<a id="rappels"></a>

## 🔁 Rappels

### MB6.R1 — Parties d'un ensemble, factorielles et combinaisons (R4, R8)

1. $2^9 = 512$ ; $2^8 = 256$ contiennent un élément donné (on choisit librement parmi les 8 autres).
2. $\binom93 = \frac{9 \times 8 \times 7}{6} = 84$.
3. $5! = 120$.
4. Vrai : choisir les $k$ éléments qu'on prend, c'est choisir les $n - k$ qu'on laisse.
5. $2^8 = 256$ : la formule du binôme pour $(1 + 1)^8$, ou le nombre de parties d'un ensemble de 8 éléments.

### MB6.R2 — La dérivée d'une fonction le long d'une courbe : gradient, vitesse et règle de la chaîne (M05b, M17)

1. $\nabla f(x, y) = (6x^2y,\ 2x^3 - 3y^2)$, et $\nabla f(2, 1) = (24, 13)$.
2. $\boldsymbol\gamma(1) = (2, 1)$ et $\boldsymbol\gamma'(t) = (1, -1)$.
3. $(f\circ\boldsymbol\gamma)'(1) = \nabla f(2, 1)\cdot(1, -1) = 24 - 13 = 11$.
4. $\nabla f(2, 1)\cdot\frac{(1, 1)}{\sqrt2} = \frac{37}{\sqrt2} \approx 26{,}163$.
5. $\frac{\partial^2f}{\partial x\,\partial y} = \frac{\partial^2f}{\partial y\,\partial x} = 6x^2$, soit 24 en $(2, 1)$ : égales, comme le garantit Schwarz pour une fonction de classe $C^2$.

### MB6.R3 — La loi conditionnelle d'un couple gaussien : une moyenne affine en la valeur observée (M25a)

1. $\operatorname{Cov}(X, Y) = \rho\,\sigma_X\sigma_Y = 0{,}3 \times 4 \times 10 = 12$.
2. $\mathbb{E}[Y \mid X = x] = 50 + 0{,}3 \times \frac{10}{4}(x - 20) = 50 + 0{,}75\,(x - 20)$ : affine en $x$ (M25a).
3. $50 + 0{,}75 \times 6 = 54{,}5$.
4. $\sigma_Y^2(1 - \rho^2) = 100 \times 0{,}91 = 91$, quelle que soit la valeur observée.
5. $\mathbb{E}[Y \mid X = x] = 50$ : un couple gaussien non corrélé est indépendant, et observer $X$ ne dit rien de $Y$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB6.1 — Un conseil de quatre membres à vote pondéré : l'indice de Shapley-Shubik par les 24 ordres, un membre nul, deux membres de poids différents et de même pouvoir, et le nombre d'ordres tirés au hasard qui suffit (Hoeffding)

**Réponses.** a) `[16, 4, 4, 0]` · b) `[0.6667, 0.1667, 0.1667, 0.0000]` · c) `[10, 6, 6, 2]` · d) `783`.

**Démarche.** Gagnent (au moins 11 voix) : AB (14), AC (11), ABC, ABD (15), ACD (12) et ABCD ; AD (9) et BCD (10) perdent, comme les membres seuls et les autres paires. Dans un ordre, le pivot est le membre dont l'arrivée fait passer les voix déjà réunies sous 11 à au moins 11.
- a) A est pivot dès qu'il arrive après B ou C : en deuxième position derrière B ou C (2 × 2 = 4 ordres) ; en troisième derrière deux membres de BCD (9, 7 ou 4 voix, puis 8 de plus : 6 ordres) ; en dernier derrière BCD (10 voix : 6 ordres) ; derrière D seul (1 + 8 = 9), il ne l'est pas. Total 16. B est pivot juste après A (2 ordres) ou après A et D (9 voix, 2 ordres) : 4 ; C de même (8 + 3 = 11 et 9 + 3 = 12) : 4. D ne l'est jamais. Total 24.
- b) Chaque compte divisé par 24 : $\frac23$, $\frac16$, $\frac16$, 0.
- c) Avec $[11 ;\ 8, 6, 3, 2]$, BCD a 11 voix et gagne : A perd son veto. A : 4 ordres en deuxième position (derrière B ou C ; derrière D, $2 + 8 = 10$ ne suffit pas), 6 en troisième (BC, BD ou CD, puis A), 0 en dernier : 10. B : après A, après AD (10 voix), après CD (5 voix) : 6. C : après A, après AD, après BD (8 voix) : 6. D : après BC (9 voix) : 2.
- d) L'indicateur « le membre est pivot dans un ordre tiré au hasard » vaut 0 ou 1 ; Hoeffding (M11 §6) : $P(\lvert\hat\varphi - \varphi\rvert \ge 0{,}05) \le 2e^{-2m \times 0{,}0025} \le 0{,}04$ dès que $m \ge \frac{\ln 50}{0{,}005} = 200\ln 50 \approx 782{,}4$, soit $m = 783$, quel que soit le nombre de membres.

Dans ta copie : pour $S = \varnothing$, $\{A\}$, $\{D\}$, $\{A, D\}$, on trouve $v(S \cup \{B\}) = v(S \cup \{C\}) = 0, 1, 0, 1$ : B et C sont symétriques, malgré 6 et 3 voix. D est nul : sans D, les totaux possibles sont 0, 3, 6, 8, 9, 11, 14 et 17, jamais 10, et sa voix ne fait jamais passer de 10 à 11.

**Erreurs fréquentes.** Ne compter une motion gagnante qu'au-delà du quota (AC, avec 11 voix exactement, gagne) ; prendre pour pivot le dernier arrivé ; prendre la part des voix pour le pouvoir ($\frac{8}{18} \approx 0{,}444$ pour A) ; compter les coalitions gagnantes où un membre figure, au lieu de celles qu'il fait basculer ; en d), oublier le facteur 2 de la borne bilatérale (644), arrondir vers le bas (782), écrire $\varepsilon$ au lieu de $\varepsilon^2$ (40), prendre un logarithme décimal (340), prendre $\delta = 0{,}96$ (147), ou oublier le 2 du dénominateur (1 565).

**Variante.** Un cinquième membre E de 2 voix, quota 11 : sur les 120 ordres, les comptes de pivots valent $(54, 24, 24, 4, 14)$ ; D n'est plus nul, et B et C restent symétriques.

### Ex MB6.2 — Trois hameaux partagent une conduite d'eau : la valeur de Shapley par les ordres, les dividendes de Harsanyi, le partage tronçon par tronçon, et les quatre axiomes vérifiés

**Réponses.** a) `[10.0, 20.5, 37.5]` · b) `[-30, -30, -51]` · c) `30` · d) `[10.0, 24.5, 41.5]`.

**Démarche.**
- a) Les coûts marginaux de (H1, H2, H3) dans chaque ordre : H1 H2 H3 : $(30, 21, 17)$ ; H1 H3 H2 : $(30, 0, 38)$ ; H2 H1 H3 : $(0, 51, 17)$ ; H2 H3 H1 : $(0, 51, 17)$ ; H3 H1 H2 : $(0, 0, 68)$ ; H3 H2 H1 : $(0, 0, 68)$. Moyennes : $\frac{60}{6} = 10$, $\frac{123}{6} = 20{,}5$, $\frac{225}{6} = 37{,}5$ ; somme 68.
- b) $d_{\{1, 2\}} = c(\{1, 2\}) - c(\{1\}) - c(\{2\}) + c(\varnothing) = 51 - 30 - 51 = -30$ ; $d_{\{1, 3\}} = 68 - 30 - 68 = -30$ ; $d_{\{2, 3\}} = 68 - 51 - 68 = -51$.
- c) $d_N = 68 - (51 + 68 + 68) + (30 + 51 + 68) - 0 = 30$. Les dividendes alternent : $+$ pour un hameau seul, $-$ pour une paire, $+$ pour les trois. Contrôle : $\varphi_1 = 30 - 15 - 15 + 10 = 10$ ; $\varphi_2 = 51 - 15 - 25{,}5 + 10 = 20{,}5$ ; $\varphi_3 = 68 - 15 - 25{,}5 + 10 = 37{,}5$.
- d) Par l'additivité : le nouveau coût est l'ancien plus 8 fois le jeu du tronçon 2, que H2 et H3 utilisent ; chacun paie 4 de plus, H1 rien : $(10 ;\ 24{,}5 ;\ 41{,}5)$.

Dans ta copie : $c = c^{(1)} + c^{(2)} + c^{(3)}$, où $c^{(1)}(S) = 30$ si $S \ne \varnothing$, $c^{(2)}(S) = 21$ si $S$ contient H2 ou H3, et $c^{(3)}(S) = 17$ si $S$ contient H3 (0 sinon). Dans $c^{(1)}$, les trois hameaux sont symétriques, et l'efficacité donne 10 à chacun ; dans $c^{(2)}$, H1 est nul, H2 et H3 symétriques : $10{,}5$ chacun ; dans $c^{(3)}$, H3 paie 17 seul. L'additivité donne $(10 ;\ 20{,}5 ;\ 37{,}5)$ : la règle de l'aéroport.

**Erreurs fréquentes.** Partager au prorata des besoins (13,7 ; 23,3 ; 31,0) ; faire payer le tronçon $k$ par les hameaux H1 à H$k$, au lieu de ceux qui l'utilisent, H$k$ à H3 ; ne faire payer à chaque hameau que sa part du dernier tronçon ; trois parts égales ; en b), ne retirer qu'un des deux hameaux seuls, se tromper de signe, ou donner les coûts des paires ; en c), soustraire les coûts des hameaux seuls au lieu de les ajouter, oublier les paires, ou donner $c(N)$ ; en d), répartir le surcoût entre les trois hameaux, ou le donner tout à H2.

**Variante.** Un quatrième hameau H4, raccordé au même point que H2 : le tronçon 1 se partage en quatre, le tronçon 2 en trois (H2, H3, H4) : $(7{,}5 ;\ 14{,}5 ;\ 31{,}5 ;\ 14{,}5)$ ; H2 et H4 sont symétriques.

### Ex MB6.3 — Le rendement d'une parcelle selon la pluie et l'engrais : courbes ICE et dérivée croisée de deux modèles, puis la moyenne marginale et la moyenne conditionnelle quand pluie et engrais sont corrélés

**Réponses.** a) `[1.2, 1.2, 1.2]` · b) `[-0.5, 1.0, 2.5]` · c) `[0, 1]` · d) `[8.000, 8.252]` · e) `0.504`.

**Démarche.**
- a) $f_1(p, 2) - f_1(p, 1) = 2{,}4 - 0{,}4 \times (4 - 1) = 1{,}2$, quel que soit $p$ : les courbes ICE de l'engrais du modèle 1 sont translatées les unes des autres (de $0{,}6\,\Delta p$).
- b) $f_2(p, 2) - f_2(p, 1) = -0{,}5\big[(p - 5)^2 - (p - 4)^2\big] = p - 4{,}5$ : $-0{,}5$, $1$ et $2{,}5$.
- c) $\partial_ef_1 = 2{,}4 - 0{,}8\,e$ ne dépend pas de $p$ : 0. $\partial_ef_2 = p - e - 3$, de dérivée 1 par rapport à $p$.
- d) $f_1$ est affine en $p$ : $\operatorname{PD}(2) = 1{,}5 + 0{,}6 \times 5{,}5 + 4{,}8 - 1{,}6 = 8$. Sachant $E = 2$, $\mathbb{E}[P \mid E = 2] = 5{,}5 + 0{,}35 \times \frac{1{,}2}{0{,}5}(2 - 1{,}5) = 5{,}92$ (M25a), donc $M(2) = 1{,}5 + 0{,}6 \times 5{,}92 + 4{,}8 - 1{,}6 = 8{,}252$.
- e) $M(v) - \operatorname{PD}(v) = 0{,}6\big(\mathbb{E}[P \mid E = v] - 5{,}5\big) = 0{,}6 \times 0{,}35 \times 2{,}4\,(v - 1{,}5) = 0{,}504\,(v - 1{,}5)$.

Dans ta copie : modèle 1, trois paraboles décalées verticalement ; modèle 2, trois paraboles de sommets en $e = p - 3$ (1, 2,5 et 4), décalées horizontalement, qui se croisent. L'écart vient de la corrélation, pas d'une interaction : là où l'on met plus d'engrais, il pleut aussi plus, et la moyenne conditionnelle prête à l'engrais l'effet de cette pluie.

**Erreurs fréquentes.** Donner la dérivée en $e = 1$ au lieu de la différence, ou $f(p, 2)$ au lieu du gain, ou oublier le terme $-0{,}4\,e^2$ dans la différence ; développer $(p - e - 3)^2$ sans ses doubles produits ; dériver deux fois par $e$ ; un signe faux sur la dérivée croisée ; oublier la corrélation dans $M$, ou arrondir $\mathbb{E}[P \mid E = 2]$ trop tôt ; prendre $\rho\frac{\sigma_E}{\sigma_P}$, ou $\rho$ seul, pour la pente de $\mathbb{E}[P \mid E = v]$ ; oublier le coefficient $0{,}6$ de la pluie en e).

**Variante.** Avec une corrélation $-0{,}35$ (plus d'engrais là où il pleut moins) : $M(2) = 7{,}748$, sous $\operatorname{PD}(2)$.

### Ex MB6.4 — Le travail de deux forces entre deux points : un champ de gradient le long de trois chemins, puis un champ qui n'en est pas un (Schwarz) le long de deux chemins

**Réponses.** a) `9` · b) `[5, 4]` · c) `9` · d) `[2, 6]` · e) `[8, 12]`.

**Démarche.** $\mathbf{F} = (2xy^2 + 5,\ 2x^2y)$.
- a) $\boldsymbol\gamma(t) = (1 + t, t)$, $\boldsymbol\gamma' = (1, 1)$ : $\mathbf{F}\cdot\boldsymbol\gamma' = 2(1 + t)t^2 + 5 + 2(1 + t)^2t = 5 + 2t + 6t^2 + 4t^3$, d'intégrale $5 + 1 + 2 + 1 = 9$.
- b) Horizontal ($y = 0$) : $F_1 = 5$, $\int_1^25\,\mathrm{d}x = 5$. Vertical ($x = 2$) : $F_2 = 8y$, $\int_0^18y\,\mathrm{d}y = 4$.
- c) $\boldsymbol\gamma' = (1, 2t)$ : $\big(2(1 + t)t^4 + 5\big) + 2(1 + t)^2t^2 \times 2t = 5 + 4t^3 + 10t^4 + 6t^5$, d'intégrale $5 + 1 + 2 + 1 = 9$.
- d) $\frac{\partial G_1}{\partial y} = 2$ et $\frac{\partial G_2}{\partial x} = 6x$, qui vaut 6 en $A$.
- e) Segment : $\mathbf{G}\cdot(1, 1) = 2t + 3(1 + t)^2$, d'intégrale $1 + 7 = 8$. Escalier : $G_1 = 0$ sur le morceau horizontal ($y = 0$), $G_2 = 12$ sur le vertical ($x = 2$) : $0 + 12 = 12$.

Dans ta copie : a), b) et c) valent $f(B) - f(A) = (4 + 10) - 5 = 9$, le théorème du gradient. d) prouve que $\mathbf{G}$ n'est pas un gradient (la contraposée de Schwarz) ; mais deux chemins donnés pourraient encore donner la même valeur : seule une valeur différente, comme en e), montre la dépendance du chemin.

**Erreurs fréquentes.** Calculer $f(A) - f(B)$ ; ne garder que la première composante du produit scalaire ; prendre $(1, t)$ pour la vitesse de $(1 + t, t^2)$, ou calculer en c) le travail de $\mathbf{G}$ au lieu de celui de $\mathbf{F}$ ; échanger les deux morceaux de l'escalier, ou passer par le coin $(1, 1)$ ; échanger les dérivées croisées, ou les calculer en $B$ ; en e), donner l'escalier avant le segment.

**Variante.** La boucle $A \to (2, 0) \to B \to A$ : 0 pour $\mathbf{F}$ ; $12 - 8 = 4$ pour $\mathbf{G}$.

### Ex MB6.5 — La variation d'un coût à trois facteurs (prix, quantité, taux de change) partagée entre les facteurs : le long du segment, puis par la moyenne des six chemins en escalier, et pourquoi les deux partages coïncident

**Réponses.** a) `-343.05` · b) `[1143.90, -1011.60, -475.35]` · c) `[-477.90, -469.20]` · d) `-475.35`.

**Démarche.** $C(\mathbf{r}) = 11{,}5 \times 680 \times 0{,}93 = 7\,272{,}60$ et $C(\mathbf{x}) = 13{,}5 \times 590 \times 0{,}87 = 6\,929{,}55$ : a) $-343{,}05$. Avec $\mathbf{h} = (2 ;\ -90 ;\ -0{,}06)$, le long du segment :
- prix : $2\int_0^1(680 - 90t)(0{,}93 - 0{,}06t)\,\mathrm{d}t = 2\big(632{,}4 - \frac{40{,}8 + 83{,}7}{2} + \frac{5{,}4}{3}\big) = 2 \times 571{,}95 = 1\,143{,}90$ ;
- quantité : $-90\int_0^1(11{,}5 + 2t)(0{,}93 - 0{,}06t)\,\mathrm{d}t = -90\big(10{,}695 + \frac{1{,}86 - 0{,}69}{2} - \frac{0{,}12}{3}\big) = -90 \times 11{,}24 = -1\,011{,}60$ ;
- taux : $-0{,}06\int_0^1(11{,}5 + 2t)(680 - 90t)\,\mathrm{d}t = -0{,}06\big(7\,820 + \frac{1\,360 - 1\,035}{2} - \frac{180}{3}\big) = -0{,}06 \times 7\,922{,}5 = -475{,}35$ ;

de somme $-343{,}05$. c) Dans l'ordre $(p, q, \tau)$, $\tau$ change en dernier : $13{,}5 \times 590 \times (-0{,}06) = -477{,}90$ ; dans l'ordre $(\tau, p, q)$, en premier : $11{,}5 \times 680 \times (-0{,}06) = -469{,}20$. d) Pour $\tau$ : premier dans deux ordres ($-469{,}20$), dernier dans deux ($-477{,}90$), deuxième après $p$ ($13{,}5 \times 680 \times (-0{,}06) = -550{,}80$) ou après $q$ ($11{,}5 \times 590 \times (-0{,}06) = -407{,}10$) : la moyenne vaut $\frac{-2\,852{,}1}{6} = -475{,}35$, la part du taux le long du segment ; le même calcul pour $p$ et $q$ redonne $1\,143{,}90$ et $-1\,011{,}60$.

Dans ta copie : $C = p\,q\,\tau$ est affine en chaque facteur quand les deux autres sont fixés : elle est multilinéaire, et le théorème de la fiche §4 dit que la part de chaque facteur le long du segment est sa valeur de Shapley dans le jeu $v(S) = C(\mathbf{x}_S, \mathbf{r}_{\bar S})$. Le prix monte (part positive) ; la quantité et le taux baissent (parts négatives).

**Erreurs fréquentes.** Le sens de la variation ; le produit des variations au lieu de la variation du produit ; oublier le terme en $t^2$ du produit des deux autres facteurs, ou l'intégrer en $\frac12$ au lieu de $\frac13$ ; en c), garder pour $p$ et $q$ leurs valeurs du premier trimestre quand $\tau$ change en dernier ; en d), prendre le tiers de la variation, ou oublier que la contribution d'un taux qui baisse est négative.

**Variante.** Du second trimestre vers le premier (la référence et le point échangés), chaque part change de signe : $(-1\,143{,}90 ;\ 1\,011{,}60 ;\ 475{,}35)$.

### Ex MB6.6 — Des relevés de capteurs sur une grille 3 × 4 : la dérivée d'un indice régional par un réchauffement uniforme, puis la grille agrandie deux fois par interpolation bilinéaire, centres ou coins alignés

**Réponses.** a) `32.9` · b) `16` · c) `50.2` · d) `[-0.25, 0.25, 0.75, 1.25, 1.75, 2.25]` · e) `[0.00, 0.40, 0.80, 1.20, 1.60, 2.00]` · f) `[12.15, 12.55]`.

**Démarche.**
- a) Les huit cases au-dessus de 10 °C : $2 \times 1{,}8 + 3 \times 3{,}2 + 1 \times 0{,}8 + 2 \times 2{,}5 + 2 \times 4{,}1 + 3 \times 0{,}3 + 1 \times 2{,}0 + 2 \times 1{,}4 = 32{,}9$ ; les quatre autres comptent 0.
- b) $\frac{\partial y}{\partial T_{ij}} = a_{ij}$ si $T_{ij} > 10$, 0 si $T_{ij} < 10$ ; la dérivée par un décalage uniforme est leur somme : $2 + 3 + 1 + 2 + 2 + 3 + 1 + 2 = 16$.
- c) Les cases déjà au-dessus de 10 ajoutent 16 ; celles à $9{,}4$ et $9{,}9$ passent au-dessus et ajoutent $0{,}4 + 0{,}9$ ; celles à $8{,}7$ et $7{,}6$ restent à 0 : $32{,}9 + 16 + 1{,}3 = 50{,}2$.
- d) $\xi(u) = (u + \frac12)\frac36 - \frac12 = \frac u2 - \frac14$. e) $\xi(u) = u\,\frac25$.
- f) Ligne 4 : $1{,}75$ (centres), $1{,}6$ (coins). Colonne 5 : $(5 + \frac12)\frac48 - \frac12 = 2{,}25$ (centres), $5 \times \frac37 = \frac{15}{7} \approx 2{,}1429$ (coins). Centres : sur la case des lignes 1 et 2, colonnes 2 et 3, avec $s = 0{,}75$ et $t = 0{,}25$ : ligne 1, $14{,}1 + 0{,}25 \times (9{,}9 - 14{,}1) = 13{,}05$ ; ligne 2, $12{,}0 + 0{,}25 \times (11{,}4 - 12{,}0) = 11{,}85$ ; puis $13{,}05 + 0{,}75 \times (11{,}85 - 13{,}05) = 12{,}15$. Coins, avec $s = 0{,}6$ et $t = \frac17$ : $13{,}5$ et $\approx 11{,}9143$, puis $13{,}5 + 0{,}6 \times (11{,}9143 - 13{,}5) \approx 12{,}5486$.

Dans ta copie : la moyenne des 12 dérivées partielles vaut $\frac{16}{12} \approx 1{,}333$, la dérivée de b) divisée par $HW = 12$ (fiche §5). $y$ est affine par morceaux en $\delta$ : la dérivée ne vaut que tant qu'aucune case ne franchit 10 °C, et deux cases le franchissent avant $\delta = 1$.

**Erreurs fréquentes.** Compter les cases sous 10 °C avec un écart négatif (28,5) ; oublier les surfaces (16,1) ; en b), sommer toutes les surfaces, ou compter les cases au lieu des surfaces ; en c), prolonger la dérivée (48,9) ; en d), oublier le $-\frac12$, lire la case $u$ en $u$ au lieu de $u + \frac12$, ou ramener déjà les cases extrêmes au bord ; en e), un facteur $\frac hH$ ou $\frac{h - 1}{H}$ au lieu de $\frac{h - 1}{H - 1}$ ; en f), donner le plus grand poids au voisin le plus éloigné, ou prendre pour les colonnes le facteur des lignes.

**Variante.** Un réchauffement de $0{,}5$ °C : seule la case à $9{,}9$ °C franchit 10 : $y = 32{,}9 + 8 + 0{,}4 = 41{,}3$.

### Ex MB6.7 — Un contrôle de pièces sur deux lignes de production aux taux de défauts différents : les taux de rejet sous la séparation, un tirage au sort entre deux seuils pour atteindre un taux de détection, et les poids qui rendent ligne et défaut indépendants

**Réponses.** a) `[0.0904, 0.1576]` · b) `0.2727` · c) `0.0736` · d) `[1.6111, 0.9610, 0.6905, 1.0504]` · e) `[0.0967, 0.0967]`.

**Démarche.**
- a) $P(\hat Y = 1 \mid G = g) = 0{,}88\,p_g + 0{,}04\,(1 - p_g) = 0{,}04 + 0{,}84\,p_g$ : $0{,}0904$ et $0{,}1576$.
- b) $0{,}74\,q + 0{,}96\,(1 - q) = 0{,}90$ donne $q = \frac{0{,}06}{0{,}22} = \frac{3}{11} \approx 0{,}2727$.
- c) $\frac{3}{11} \times 0{,}03 + \frac{8}{11} \times 0{,}09 = \frac{0{,}81}{11} \approx 0{,}0736$.
- d) 2 400 pièces, dont 232 défectueuses : $P(G = 1) = \frac{1\,300}{2\,400}$, $P(G = 2) = \frac{1\,100}{2\,400}$, $P(\text{défaut}) = \frac{232}{2\,400}$. $w(1, \text{défaut}) = \frac{1\,300 \times 232}{2\,400 \times 78} = \frac{29}{18} \approx 1{,}6111$ ; $w(1, \text{sans défaut}) = \frac{1\,300 \times 2\,168}{2\,400 \times 1\,222} \approx 0{,}9610$ ; $w(2, \text{défaut}) = \frac{1\,100 \times 232}{2\,400 \times 154} = \frac{29}{42} \approx 0{,}6905$ ; $w(2, \text{sans défaut}) = \frac{1\,100 \times 2\,168}{2\,400 \times 946} \approx 1{,}0504$.
- e) Ligne 1 : $\frac{78 \times 1{,}6111}{78 \times 1{,}6111 + 1\,222 \times 0{,}9610} = \frac{125{,}67}{1\,300} \approx 0{,}0967$ ; de même pour la ligne 2 : les deux valent $P(\text{défaut}) = \frac{232}{2\,400}$.

Dans ta copie : sous la séparation, le taux de rejet suit le taux de défauts ; avec $p_1 \ne p_2$, il diffère d'une ligne à l'autre, et l'indépendance $\hat Y \perp G$ ne tient pas (∂ MB6.10). Les comptes pondérés valent $125{,}67$ et $1\,174{,}33$ (ligne 1), $106{,}33$ et $993{,}67$ (ligne 2) : toujours 1 300 et 1 100 pièces, et 232 défectueuses.

**Erreurs fréquentes.** Oublier les fausses alertes ; échanger les poids des deux taux (le taux de détection pèse la part des pièces défectueuses, le taux de fausses alertes celle des bonnes) ; en b), la probabilité de tirer B au lieu de A, ou diviser par l'écart entre la cible et $\mathrm{TPR}_A$ au lieu de $\mathrm{TPR}_B - \mathrm{TPR}_A$ ; en c), échanger les poids des deux seuils, ou garder le taux de fausses alertes du seuil B ; en d), diviser par $P(y \mid g)$ au lieu de $P(g, y)$, ou ne pas diviser du tout ; en e), échanger les poids des deux lignes, ou garder les taux bruts.

**Variante.** Pour détecter 85 % des pièces défectueuses : $q = \frac12$, et un taux de fausses alertes de $0{,}06$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB6.8 — Unicité de la valeur de Shapley : les jeux d'unanimité forment une base, et les quatre axiomes imposent φ_i = Σ_{T ∋ i} d_T / |T|

**Démonstration.**
1. En remplaçant $d_T$ : $\sum_{T \subseteq S}d_T = \sum_{T \subseteq S}\sum_{R \subseteq T}(-1)^{\lvert T\rvert - \lvert R\rvert}v(R) = \sum_{R \subseteq S}v(R)\sum_{T : R \subseteq T \subseteq S}(-1)^{\lvert T\rvert - \lvert R\rvert}$. Les $T$ entre $R$ et $S$ s'écrivent $R \cup U$, $U \subseteq S \setminus R$ ; avec $m = \lvert S\rvert - \lvert R\rvert$, la somme intérieure vaut $\sum_{k=0}^m\binom mk(-1)^k = (1 - 1)^m$ : 1 si $R = S$, 0 sinon. Il reste $v(S)$.
2. Comme $u_T(S) = 1$ exactement quand $T \subseteq S$, 1 s'écrit $v = \sum_Td_T\,u_T$ : les $2^n$ jeux $u_T$ engendrent l'espace des jeux, de dimension $2^n$ ; ils en forment donc une base (et les $d_T$ sont les seules coordonnées possibles).
3. Soit $T \ne \varnothing$ et $c$ réel. Pour $i \notin T$, $S \cup \{i\}$ contient $T$ si et seulement si $S$ le contient : $i$ est nul, $\varphi_i = 0$. Pour $i, j \in T$ et $S$ sans $i$ ni $j$, ni $S \cup \{i\}$ ni $S \cup \{j\}$ ne contient $T$ : les deux valeurs sont nulles, $i$ et $j$ sont symétriques, et leurs parts sont égales. L'efficacité donne $\sum_i\varphi_i = c\,u_T(N) - c\,u_T(\varnothing) = c$, partagé entre les $\lvert T\rvert$ membres : $\frac{c}{\lvert T\rvert}$ chacun. Pour $c\,u_\varnothing$, un jeu constant, tous les joueurs sont nuls : $\varphi = 0$.
4. Chaque $d_T\,u_T$ est un jeu ($d_T$ peut être négatif : la question 3 vaut pour tout réel $c$). L'additivité, appliquée à la somme finie $v = \sum_Td_T\,u_T$, donne $\varphi_i(v) = \sum_T\varphi_i(d_T\,u_T) = \sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$.
5. La valeur de Shapley vérifie les quatre axiomes, donc, par 4, elle vaut $\sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$ ; toute règle qui les vérifie vaut la même chose. Il en existe une, et une seule : la valeur de Shapley.

**Grille de relecture.** 1 : la substitution, l'échange des deux sommes, l'identité $\sum_k\binom mk(-1)^k = (1 - 1)^m$, et le cas $R = S$. 2 : la décomposition $v = \sum_Td_Tu_T$, et la dimension (ou l'unicité des coefficients). 3 : les joueurs hors de $T$ nuls, ceux de $T$ symétriques, l'efficacité (avec $u_T(\varnothing) = 0$ pour $T \ne \varnothing$), le jeu constant, et $c$ réel quelconque. 4 : l'additivité sur une somme finie de jeux, sans axiome d'homogénéité (chaque $d_T\,u_T$ est traité par 3). 5 : l'existence (la valeur de Shapley) et l'unicité. Une preuve qui montre en 2 l'indépendance des $u_T$ directement (en évaluant une combinaison nulle sur les coalitions par taille croissante) est correcte aussi.

**Variante.** Sans l'axiome du joueur nul, la règle « $\varphi_i = \frac{v(N) - v(\varnothing)}{n}$ » vérifie l'efficacité, la symétrie et l'additivité : les quatre axiomes sont nécessaires à l'unicité.

### Ex MB6.9 — Un score calibré dans un groupe vérifie p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; si deux groupes ont les mêmes moyennes de scores chez leurs positifs et chez leurs négatifs, leurs taux de base sont égaux ou le score est parfait

**Démonstration.**
1. Par l'espérance totale en conditionnant par $S$ : $\mathbb{E}[S] = \sum_s s\,P(S = s) = \sum_sP(Y = 1 \mid S = s)\,P(S = s) = P(Y = 1) = p$.
2. En conditionnant par $Y$ : $\mathbb{E}[S] = p\,a + (1 - p)\,b$. Avec 1, $p = pa + (1 - p)b$, soit $p\,(1 - a) = (1 - p)\,b$.
3. La relation s'écrit $p\,(1 - a + b) = b$. Si $1 - a + b \ne 0$, $p = \frac{b}{1 - a + b}$ ne dépend que de $a$ et $b$ : deux groupes de mêmes $a$ et $b$ ont le même taux de base. Si $1 - a + b = 0$ : comme $0 \le S \le 1$, $a \le 1$ et $b \ge 0$, donc $1 - a \ge 0$ et $b \ge 0$ ont une somme nulle : $a = 1$ et $b = 0$. Alors $\mathbb{E}[S \mid Y = 0] = 0$ avec $S \ge 0$ : $S = 0$ presque sûrement quand $Y = 0$ ; et $\mathbb{E}[1 - S \mid Y = 1] = 0$ avec $1 - S \ge 0$ : $S = 1$ presque sûrement quand $Y = 1$. Donc $S = Y$ presque sûrement : le score est parfait.
4. $\frac{15}{750} = 0{,}02$, $\frac{15}{150} = 0{,}1$, $\frac{30}{100} = 0{,}3$ : calibré. $p = \frac{60}{1\,000} = 0{,}06$ ; $a = \frac{15 \times 0{,}02 + 15 \times 0{,}1 + 30 \times 0{,}3}{60} = \frac{10{,}8}{60} = 0{,}18$ ; $b = \frac{735 \times 0{,}02 + 135 \times 0{,}1 + 70 \times 0{,}3}{940} = \frac{49{,}2}{940} \approx 0{,}0523$. $p\,(1 - a) = 0{,}06 \times 0{,}82 = 0{,}0492$ et $(1 - p)\,b = 0{,}94 \times \frac{49{,}2}{940} = 0{,}0492$. Avec les mêmes $a$ et $b$, la ligne 2 aurait le taux de base $\frac{b}{1 - a + b} = 0{,}06$, pas 14 % : impossible.

**Grille de relecture.** 1 : l'espérance totale (ou la propriété de la tour) et la calibration utilisée valeur par valeur. 2 : la décomposition sachant $Y$, avec $0 < p < 1$. 3 : la relation $p(1 - a + b) = b$, le cas $1 - a + b \ne 0$, puis le cas nul traité avec les bornes $0 \le S \le 1$ (un argument d'espérance d'une variable positive), pas seulement affirmé. 4 : la calibration vérifiée sur les trois valeurs, $p$, $a$, $b$, l'identité, et la contradiction pour la ligne 2.

### Ex MB6.10 — Indépendance et séparation ne tiennent ensemble, quand les taux de base diffèrent, que pour une décision qui ignore le label ; la repondération P(g)P(y)/P(g, y) rend groupe et label indépendants sans changer leurs marges

**Démonstration.**
1. Par les probabilités totales, $P(\hat Y = 1 \mid G = g) = t_g\,p_g + f_g\,(1 - p_g)$. Si $p_1 = p_2$ et $(t_1, f_1) = (t_2, f_2)$, les deux taux sont égaux : la séparation entraîne l'indépendance. Sous la séparation, c'est $f + (t - f)\,p_g$ ; l'indépendance impose l'égalité pour $g = 1$ et 2 : $(t - f)(p_1 - p_2) = 0$, donc $t = f$ puisque $p_1 \ne p_2$. Et $t = f$ dit $P(\hat Y = 1 \mid Y = 1, G = g) = P(\hat Y = 1 \mid Y = 0, G = g)$ : $\hat Y \perp Y$ dans chaque groupe. Réciproquement, pas toujours : une décision telle que $\hat Y \perp Y$ dans chaque groupe a, dans le groupe $g$, un seul taux $t_g = f_g$ ; si ce taux est le même dans les deux groupes, elle vérifie l'indépendance et la séparation ; s'il diffère, elle ne vérifie ni l'une ni l'autre.
2. $Q(g, y) = P(g)\,P(y) \ge 0$, et $\sum_{g, y}Q(g, y) = \sum_gP(g)\sum_yP(y) = 1$ : c'est une loi. Ses marges : $\sum_yQ(g, y) = P(g)$ et $\sum_gQ(g, y) = P(y)$. Et $Q(g, y)$ est le produit de ses marges : $G$ et $Y$ sont indépendants sous $Q$.

**Grille de relecture.** 1 : la formule des probabilités totales et le cas $p_1 = p_2$ ; la factorisation par $p_1 - p_2$, qui exige $p_1 \ne p_2$ ; la traduction de $t = f$ en indépendance conditionnelle ; la réciproque, avec la condition d'un même taux. 2 : la positivité et la somme 1, les deux marges calculées, l'indépendance comme produit des marges ; l'hypothèse $P(g, y) > 0$ (le poids doit être défini).

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB6.11 — Pont : l'écart des taux de détection de deux laboratoires et son intervalle, par l'erreur type d'une différence de deux proportions, qui se lit avec le nombre d'échantillons positifs de chacun

**Réponses.** a) `[0.7143, 0.8615]` · b) `0.0867` · c) `[-0.023, 0.317]` · d) `0.0453`.

**Démarche.** a) Un taux de détection se calcule sur les prélèvements contaminés : $\frac{20}{28} \approx 0{,}7143$ et $\frac{448}{520} \approx 0{,}8615$. b) $\frac{0{,}7143 \times 0{,}2857}{28} \approx 0{,}0072886$ et $\frac{0{,}8615 \times 0{,}1385}{520} \approx 0{,}0002294$ ; erreur type $\sqrt{0{,}0075180} \approx 0{,}0867$. c) $0{,}1473 \pm 1{,}96 \times 0{,}0867 = 0{,}1473 \pm 0{,}1699$ : $[-0{,}023 ;\ 0{,}317]$. d) Le premier terme est divisé par 4 : $\sqrt{0{,}0018222 + 0{,}0002294} \approx 0{,}0453$.

Dans ta copie : l'intervalle contient 0 : ces données ne tranchent pas (ce qui ne veut pas dire « aucun écart ») ; le laboratoire A, avec ses 28 prélèvements contaminés, fait 97 % de la variance. Un bootstrap stratifié tire avec remise 28 prélèvements contaminés de A et 520 de B, recalcule l'écart, recommence, et lit l'intervalle sur les centiles des écarts obtenus.

**Erreurs fréquentes.** Un pourcentage au lieu d'une proportion ; l'ordre A, B ; additionner les erreurs types au lieu des variances, ou ne garder que celle du laboratoire A (en b et en c) ; un taux commun aux deux laboratoires, qui sert à un test, pas à cet intervalle ; une seule erreur type de chaque côté, ou 1,645 au lieu de 1,96 ; en d), diviser toute l'erreur type par 2, ou la variance du terme de A par 16.

**Variante.** À 99 % ($2{,}576$ erreurs types), avec A quadruplé : $0{,}1473 \pm 0{,}1167$, soit $[0{,}031 ;\ 0{,}264]$, qui exclut encore 0.

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB6.12 — Expliquer avec trois amis qui partagent un taxi pourquoi on moyenne l'apport de chacun sur tous les ordres d'arrivée

**Réponse modèle (5 à 8 phrases).** Ce que la présence d'un ami ajoute au prix dépend de qui est déjà dans le taxi : si Sam y est, le taxi fait de toute façon tout le trajet, et Léa n'ajoute presque rien ; si Léa est seule, sa présence coûte toute sa course. Si l'on imagine les amis monter l'un après l'autre et que chacun paie ce qu'il ajoute en montant, le premier paie beaucoup et les suivants peu : le partage dépend de l'ordre qu'on a choisi, et cet ordre n'a rien de juste. On imagine donc tous les ordres possibles, et chacun paie la moyenne de ce qu'il ajoute sur tous ces ordres. Dans chaque ordre, les ajouts font exactement le prix de la course, donc la moyenne aussi : tout est payé. Deux amis qui habiteraient au même endroit ajouteraient toujours la même chose à la même place dans l'ordre, et paieraient donc autant. Au bout du compte, le premier bout de trajet est partagé entre les trois, le deuxième entre Max et Sam, et le dernier est payé par Sam seul : celui qui habite le plus loin paie le plus.

**Grille.** Un apport qui dépend de qui est déjà là ; le partage selon un seul ordre, qui avantage les derniers ; la moyenne sur tous les ordres ; tout le prix est payé (chaque ordre fait le total) ; deux amis au même endroit paient autant ; qui paie le plus ; aucune formule. En plus, non exigé : le partage tronçon par tronçon (la règle de l'aéroport).

<a id="entretien"></a>

## 💼 Entretien

### MB6.E1 — « La valeur de Shapley est la seule répartition qui respecte quatre règles simples : lesquelles, et pourquoi suffisent-elles ? »

**Réponse modèle (60 secondes).** « Les quatre règles : l'efficacité, tout le gain est réparti ; la symétrie, deux joueurs qui apportent la même chose à toute coalition reçoivent la même part ; le joueur nul, un joueur qui n'apporte rien à aucune coalition reçoit zéro ; l'additivité, les parts de la somme de deux jeux sont la somme des parts. Pourquoi elles suffisent : on regarde d'abord les jeux d'unanimité, qui valent un quand une coalition contient un groupe donné et zéro sinon ; dans un tel jeu, les joueurs hors du groupe sont nuls, ceux du groupe sont symétriques, et l'efficacité force à donner à chacun une part égale. Ensuite, tout jeu s'écrit comme une combinaison de jeux d'unanimité, avec les dividendes de Harsanyi pour coefficients, et l'additivité force les parts : chaque interaction est partagée également entre ses membres. Il y a donc au plus une règle, et la moyenne des contributions sur tous les ordres d'arrivée en est une : c'est la valeur de Shapley. La règle la plus discutable est l'additivité, qui n'a pas de sens évident pour un seul jeu ; et la symétrie ne dit rien de joueurs qui se ressemblent sans être interchangeables. »

**Grille.** Les quatre règles nommées et expliquées ; les jeux d'unanimité et ce que trois règles y imposent ; la décomposition de tout jeu (dividendes) et le rôle de l'additivité ; l'existence par les ordres ; une limite d'au moins une règle.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **MB6.13 🔨** `coalition_weights` : les contrôles (un entier $n \ge 1$, ni booléen ni flottant ; `exact` booléen), puis `Fraction(math.factorial(s) * math.factorial(n - 1 - s), math.factorial(n))`, converti par `float` si `exact` est faux. a) $\big(\frac19, \frac1{72}, \frac1{252}, \frac1{504}, \frac1{630}, \frac1{504}, \frac1{252}, \frac1{72}, \frac19\big)$. b) $\binom{24}{12} = 2\,704\,156$. Ce qu'il faut observer : chaque taille pèse $\frac1n$ en tout, partagé entre $\binom{n-1}{s}$ coalitions ; les tailles moyennes ont le plus de coalitions, donc les plus petits poids : une coalition de 12 membres sur 24 pèse 2,7 millions de fois moins que la coalition vide.
- **MB6.14 🔨** `harsanyi_dividends` : les valeurs dans un dictionnaire, taille par taille ; puis, pour chaque $T$, la somme de $(-1)^{\lvert T\rvert - \lvert S\rvert}v(S)$ sur les $S \subseteq T$. a) $(-30, -30, -51, 30)$, comme MB6.2. b) $(4{,}5 ;\ 6 ;\ 3 ;\ 6)$, de somme $19{,}5 = v(N)$. c) $(-1 ;\ 1{,}5)$. d) $(1, 1, -1)$. Ce qu'il faut observer : $d_{\{1, 2\}} = -1$ : les maraîchers 1 et 2 vendent moins ensemble que séparément (ils se font concurrence), et ce dividende de $-1$ (100 € de bénéfice en moins par semaine) est partagé entre eux deux. Dans le conseil, A gagne avec B ou avec C : $d_{\{0, 1\}} = d_{\{0, 2\}} = 1$ ; mais ABC ne gagne qu'une fois, pas deux, d'où $d_{\{0, 1, 2\}} = -1$ ; et $\varphi_A = \frac12 + \frac12 - \frac13 = \frac23$, comme MB6.1.
- **MB6.15 🔨** `line_integral` : pour chaque segment, `ts = np.linspace(0, 1, n_sub + 1)`, les produits scalaires `np.dot(field(a + t * (b - a)), b - a)` point par point, et les poids de Simpson $1, 4, 2, \ldots, 4, 1$ fois $\frac{h}{3}$. a) $(9, 9)$. b) $(8, 12)$. c) $(9{,}093750 ;\ 9{,}162109 ;\ 9{,}166382)$. Ce qu'il faut observer : l'écart à $\frac{55}{6}$ ($0{,}0729$, $0{,}0046$, $0{,}00028$) diminue : la ligne brisée s'approche de l'arc. Pour $\mathbf{F}$, toutes les lignes brisées de $A$ à $B$ donnent $f(B) - f(A) = 9$ : le chemin ne compte pas.
- **MB6.16 🔨** `spearman_rho` : les rangs par `np.argsort`, puis la moyenne des places de chaque groupe de valeurs égales ; Pearson sur les rangs centrés ; `nan` si une somme de carrés est nulle. a) $\approx 0{,}8787$. b) $\approx -0{,}8787$. Ce qu'il faut observer : l'ex aequo de l'échelle de Mohs (deux minéraux à 3) rend la formule en $\sum d_i^2$ approchée ; $v \mapsto \frac1v$ est strictement décroissante sur les duretés positives : elle renverse l'ordre, et $\rho_S$ change de signe.
- **MB6.17 🔮** Prédictions attendues : a) (A) ; b) (C) ; c) (B) ; d) (B). Mesures : e) $(0 ;\ 8 ;\ -8 ;\ 16)$ (à $10^{-14}$ près pour le premier). Ce qu'il faut observer (après l'expérience) : l'aire du triangle vaut 4, et $\mathbf{R}$ donne $8$, deux fois l'aire ; sur chaque côté, $\mathbf{R}\cdot\boldsymbol\gamma'$ est le double de l'aire balayée par le rayon depuis l'origine, si bien que la boucle donne deux fois l'aire enfermée, avec un signe qui dit le sens du parcours. Une boucle d'intégrale nulle ne suffit pas : $\mathbf{R}$ donne 0 sur un aller et retour, sans être un gradient.
- **MB6.18 🔬** a) $\operatorname{PD}(26) = e^{0{,}4 + 0{,}08} \approx 1{,}6161$ ; $M(26) \approx 1{,}6161$ ($\rho = 0$), $2{,}0682$ ($\rho = 0{,}5$), $2{,}4478$ ($\rho = 0{,}9$), par $\mathbb{E}[U \mid T = 26] = 70 + \rho\frac83 \times 4$ et $\mathbb{V}(U \mid T = 26) = 64(1 - \rho^2)$. b) La fenêtre garde environ $2{,}7$ % des points, soit 8 200 environ pour chaque $\rho$ ; avec la graine de la correction, les estimations de $\operatorname{PD}$ sont à $0{,}001$ près, celles de $M$ à $0{,}015$ près. Ce qu'il faut observer : pour $\rho = 0$, les deux moyennes sont égales ; plus la corrélation est forte, plus la moyenne conditionnelle prête à la température l'effet du phosphore qui l'accompagne. $\operatorname{PD}$ se moyenne sur 300 000 points, $M$ sur ceux de la fenêtre seulement : son estimation est plus dispersée, et une fenêtre dix fois plus étroite garderait dix fois moins de points (environ $\sqrt{10}$ fois plus de dispersion), pour un biais plus petit.
- **MB6.19 🎨** a) $f(B) - f(A) \approx 1{,}6968$. b) Le plus grand cumul vaut environ $3{,}694$ le long du segment (qui passe près du sommet de la bosse), $2{,}014$ le long de la ligne brisée. Ce qu'il faut observer : le segment descend d'abord dans le creux puis monte sur la bosse, la ligne brisée la contourne ; les deux cumuls finissent à $f(B) - f(A)$, parce que le cumul jusqu'au point $\boldsymbol\gamma(t)$ vaut $f(\boldsymbol\gamma(t)) - f(A)$ (théorème du gradient) : il ne dépend que du point atteint.
- **MB6.20 🐛** (1) Diviser par $n!$ : `math.factorial(s) * math.factorial(n - 1 - s) / math.factorial(n)`. a) $(1, 7)$ : la somme pondérée fautive vaut $n$. Pour $n = 1$, $0!\,0! / 0! = 0!\,0! / 1! = 1$ : l'erreur ne se voit pas. (2) Donner aux valeurs égales la moyenne de leurs places. b) $\approx (0{,}5988 ;\ 0{,}5357)$. Sans ex aequo, les deux rangements coïncident. (3) `(1 - t) * a + t * b`. c) $(14{,}4 ;\ 17{,}6)$. En $t = \frac12$, les deux poids valent $\frac12$ : l'échange ne se voit pas. Il ne se verrait pas non plus à l'intérieur d'une intégrale le long d'un segment (les points et les poids de Simpson sont symétriques) : c'est en lisant une valeur intermédiaire qu'il change le résultat. Des corrections fausses ne rendent pas juste : des rangs « min », « max » ou « denses » aux ex aequo donnent encore d'autres valeurs, que la vérification refuse.
- **MB6.21 🛠️** Une correction possible : `reversed_changes_sign_21` tire cinq lignes brisées de 2 à 5 segments et compare `method(F, P)` à `-method(F, P[::-1])` pour $\mathbf{F}(x, y) = (\sin x + y^2,\ x\cos y)$, qui n'est pas un gradient ; `split_changes_nothing_21` insère un sommet en un point tiré au hasard d'un segment, pour $\mathbf{F}(x, y) = (x^3 - 2y,\ x^2 + y^3)$ ; `gradient_gives_difference_21` prend le gradient de $f(x, y) = x^3 - 4y^3 + 5xy$ et compare à $f(\text{fin}) - f(\text{début})$ ; chaque comparaison à $10^{-9}$ près en valeur relative. a) `[True, True, True]`. Ce qu'il faut observer : pour un champ non polynomial, la règle de Simpson à 20 intervalles fait une erreur d'environ $10^{-5}$, qui change quand on coupe un segment : le deuxième test refuserait la référence elle-même. Avec des coordonnées de degré 2 ou 3, la règle de Simpson est exacte et les propriétés tiennent à $10^{-13}$ près ; la méthode des trapèzes, exacte seulement pour un champ affine, est alors refusée par les deux derniers tests, mais passe le premier : ses points aussi sont symétriques. Des lignes tirées au hasard, plusieurs fois, évitent un cas particulier où une erreur s'annulerait (un segment parallèle à un axe, une ligne symétrique) ; et une ligne brisée fixe dont les segments vont tous vers la droite et vers le haut laisse passer la méthode $\mathbf{F}\cdot\lvert\mathbf{b} - \mathbf{a}\rvert$ (n° 11 ci-dessous), alors que des lignes tirées au hasard vont dans toutes les directions.
  Les onze méthodes fausses cachées de la vérification, et le test qui doit refuser chacune (ces trois tests refusent chacune à chaque exécution) :
  - `reversed_changes_sign_21` : (1) des sommes de Riemann à gauche, 64 intervalles (points non symétriques : il faut un champ dont $\mathbf{F}\cdot\boldsymbol\gamma'$ varie le long d'un segment ; le champ tournant $(-y, x)$ le garde constant) ; (2) la valeur absolue de l'intégrale ; (3) le premier segment seul ; (4) l'intégrale plus $2 \cdot 10^{-9} + 2 \cdot 10^{-8}\,\lvert\text{intégrale}\rvert$ ;
  - `split_changes_nothing_21` : (5) les trapèzes, 20 intervalles ; (6) l'intégrale multipliée par $1 + 2 \cdot 10^{-8}(k - 2)$, pour $k$ sommets ;
  - `gradient_gives_difference_21` : (7) les trapèzes, 20 intervalles ; (8) le premier segment seul ; (9) les composantes du champ échangées (il faut une fonction dont les deux dérivées partielles diffèrent, comme $x^3y$) ; (10) le décalage du n° 4 ; (11) $\mathbf{F}\cdot\lvert\mathbf{b} - \mathbf{a}\rvert$ au lieu de $\mathbf{F}\cdot(\mathbf{b} - \mathbf{a})$, juste seulement sur un segment qui va vers la droite et vers le haut.

  Les décalages des n° 4, 6 et 10 sont de l'ordre de $10^{-8}$ en valeur relative : une tolérance plus large que $10^{-9}$, comme celle de `np.allclose` par défaut (`rtol=1e-5`, `atol=1e-8`), les laisse passer. Avant tout verdict, la vérification refuse un test qui lit la méthode ou la pile d'appels (son code, sa fermeture, `inspect`…) au lieu de l'exécuter, ou qui appelle `line_integral` de la référence : un test compare la méthode à $-$valeur, à la valeur sans le sommet ajouté, ou à $f(\text{fin}) - f(\text{début})$.
- **MB6.22 🏆** `shapley_shubik_22` : pour chaque membre $i$, un tableau `table[s, t]` des coalitions des autres membres de taille $s$ et de poids total $t < q$, rempli membre par membre (`table[1:, w:] += table[:-1, :q - w]`, avec une copie) ; puis `counts = table[:, max(q - w_i, 0):q].sum(axis=1)` (les coalitions qui perdent et que $i$ fait gagner) et $\varphi_i = \sum_sw(s)\,\mathrm{counts}[s]$, avec `coalition_weights(n)`. a) $\varphi_0 \approx 0{,}131430$. b) Les 25 indices, de $0{,}131430$ (12 voix) à $0{,}009681$ (une voix) ; somme 1. Ce qu'il faut observer : les membres de mêmes voix ont le même indice (symétrie) ; le pouvoir n'est pas proportionnel aux voix (12 voix sur 98, soit 12,2 %, donnent 13,1 % du pouvoir). La vérification tire trois séries de cinq conseils cachés de 30 à 50 membres : la programmation dynamique les traite en une fraction de seconde, alors que l'énumération de leurs $2^{29}$ à $2^{49}$ coalitions est impossible. Échouent à chaque exécution : les voix prises pour le pouvoir, les voix normalisées, des parts égales, un tirage de 20 000 ordres, la fenêtre de poids qui inclut $q$, le poids de taille décalé d'un rang, des comptes en `float32`, les poids de 24 joueurs au lieu de 25, et les indices du conseil du notebook recopiés.
