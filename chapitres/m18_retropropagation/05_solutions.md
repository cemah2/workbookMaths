# M18 · Différentiation automatique et calcul matriciel — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Ponts, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M18.Q1 — Lire un graphe de calcul : nœuds, arêtes, ordre d'évaluation
1. 5 nœuds ($r_1$, $r_2$, $u_1$, $u_2$, $R$) et 6 arêtes : $r_1 \to u_1$, $r_2 \to u_1$, $r_1 \to u_2$, $r_2 \to u_2$, $u_1 \to R$, $u_2 \to R$.
2. $r_1$ et $r_2$ (les entrées) n'ont aucun prédécesseur ; $R$ (la sortie) n'a aucun successeur.
3. Deux : vers $u_1$ et vers $u_2$.
4. Vrai : $u_1$ et $u_2$ ne dépendent que des entrées.
5. Par exemple $(r_1, r_2, u_1, u_2, R)$ et $(r_2, r_1, u_2, u_1, R)$ : toute numérotation où chaque arête va vers un nœud calculé plus tard.
6. Faux : chaque affectation crée un **nouveau** nœud (la nouvelle valeur de `x`), calculé à partir de l'ancien ; le graphe des valeurs reste sans cycle.

### M18.Q2 — Combien de chemins, et quelle somme ?
1. Trois : $x \to a \to y$, $x \to a \to c \to y$ et $x \to b \to c \to y$.
2. $3 \times 4 + 3 \times 2 \times (-1) + (-2) \times 1 \times (-1) = 12 - 6 + 2 = 8$.
3. $4 + 2 \times (-1) = 2$ : les deux chemins de $a$ à $y$.
4. $\binom{8}{4} = 70$ : un chemin fait 4 pas dans chaque direction, et il suffit de choisir lesquels des 8 pas vont vers $i$ (R8).
5. Faux : on range la somme nœud par nœud (§3 et §4 de la fiche), une multiplication et une addition par arête.
6. 0 : le produit le long de ces chemins contient un facteur nul.

### M18.Q3 — Calculer avec ε² = 0
1. $3 - 3\varepsilon + 2\varepsilon - 2\varepsilon^2 = 3 - \varepsilon$.
2. $1 + 5\varepsilon$ (binôme : les termes en $\varepsilon^2$ et au-delà disparaissent).
3. $\frac12 - \frac14\varepsilon$ (multiplie par $2 - \varepsilon$ : $\frac{2 - \varepsilon}{4}$).
4. $1 + 3\varepsilon$ ($e^0 + e^0 \times 3\,\varepsilon$).
5. $\sin\pi + \cos\pi \times \varepsilon = -\varepsilon$.
6. Vrai, pour une fonction écrite avec les opérations usuelles (∂ M18.12).
7. Faux : $\varepsilon$ est un symbole, non nul, dont le carré est nul. La matrice $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ en est un modèle (une matrice nilpotente, M16) : $a + b\varepsilon$ se calcule comme $\begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$.

### M18.Q4 — Le mode inverse : dans quel ordre visiter les nœuds ?
1. $R$, puis $u_2$ et $u_1$ (dans n'importe quel ordre), puis $r_2$ et $r_1$ : l'ordre inverse d'un ordre de calcul, par exemple $(R, u_2, u_1, r_2, r_1)$.
2. $\bar{R} = 1$.
3. Faux : $\bar{r}_1$ reçoit des contributions de $u_1$ et de $u_2$, dont il faut d'abord les adjoints.
4. $u_1$ et $u_2$ (pour $\frac{\partial R}{\partial u_1} = \frac{1}{u_2}$ et $\frac{\partial R}{\partial u_2} = -\frac{u_1}{u_2^2}$), et $r_1$, $r_2$ (pour $\frac{\partial u_1}{\partial r_1} = r_2$ et $\frac{\partial u_1}{\partial r_2} = r_1$).
5. Deux : l'une de $u_1$, l'autre de $u_2$.
6. Vrai : la passe arrière donne l'adjoint de toutes les entrées.

### M18.Q5 — Direct ou inverse, pour n entrées et m sorties ?
1. 500 passes en mode direct (une par entrée), une seule en mode inverse.
2. 2 passes en mode direct, 300 en mode inverse.
3. Le mode direct : il ne garde, comme le calcul de $f$, que les valeurs encore utiles (avec leurs tangentes), alors que le mode inverse garde toute la passe avant.
4. Vrai : les dérivées locales de la passe arrière en ont besoin.
5. Faux : il coûte un petit multiple du calcul de la fonction, **indépendant** du nombre de variables (le principe du gradient bon marché).
6. Une seule, avec la graine $\mathbf{v}$ : elle donne le produit jacobienne-vecteur $\mathbf{J}\mathbf{v}$.

### M18.Q6 — La forme d'un gradient par rapport à une matrice
1. $(3, 5)$, la forme de $\mathbf{X}$ ; 15 dérivées partielles.
2. La matrice $\mathbf{E}_{23}$ : un 1 en $(2, 3)$, des 0 ailleurs.
3. La matrice pleine de 1, de la forme de $\mathbf{X}$.
4. $\sum_{ij}G_{ij}H_{ij}$, c'est-à-dire $\operatorname{tr}(\mathbf{G}^\top\mathbf{H})$.
5. Faux : ce sont deux matrices différentes (sauf si $\mathbf{G}$ est symétrique), et l'erreur ne se voit pas à la forme.
6. $(4, 2, 3)$.

### M18.Q7 — Identités de trace : vrai ou faux
1. Vrai : $\mathbf{A}\mathbf{B}$ est $2 \times 2$, $\mathbf{B}\mathbf{A}$ est $3 \times 3$, mais leurs traces valent toutes deux $\sum_{i,j}A_{ij}B_{ji}$.
2. Faux en général : seules les permutations **cycliques** sont permises ($\operatorname{tr}(\mathbf{A}\mathbf{B}\mathbf{C}) = \operatorname{tr}(\mathbf{B}\mathbf{C}\mathbf{A}) = \operatorname{tr}(\mathbf{C}\mathbf{A}\mathbf{B})$). Contre-exemple : $\mathbf{A} = \mathbf{E}_{12}$, $\mathbf{B} = \mathbf{E}_{21}$, $\mathbf{C} = \mathbf{E}_{11}$ donnent 1 et 0.
3. Faux : pour $\mathbf{A} = \mathbf{B} = \mathbf{I}_2$, $2 \ne 4$.
4. Vrai : un nombre est sa propre trace, puis la cyclicité.
5. Vrai.
6. Faux : $\nabla_{\mathbf{X}}f = \mathbf{M}^\top$.

### M18.Q8 — Gradient d'une moyenne, moyenne des gradients
1. $\frac14\big((1, 0) + (3, 2) + (-1, 4) + (1, -2)\big) = (1, 1)$.
2. Vrai : la dérivation est linéaire.
3. Le centroïde des deux points est $(2, 1)$, donc $\nabla F(0, 0) = 2\big((0, 0) - (2, 1)\big) = (-4, -2)$.
4. Au centroïde $(2, 1)$.
5. Faux : $\mathbf{I}$ est symétrique, et laisse passer un gradient transposé ; elle ne teste que la somme de la diagonale de $\mathbf{G}$.
6. 2 évaluations, quelle que soit la taille de $\mathbf{X}$. Aucun nombre de directions symétriques ne suffit : le long de chacune, $\mathbf{G}^\top$ donne la même pente que $\mathbf{G}$ (fiche §8).

<a id="rappels"></a>

## 🔁 Rappels

### M18.R1 — La jacobienne d'une composée (M17)
1. $(2, 3)$.
2. $\begin{pmatrix} 1 & -1 \\ y & x \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix}$.
3. $\mathbf{J}_g(u, v) = \begin{pmatrix} v & u + 2v \end{pmatrix}$, en $(2, 3)$ : $\begin{pmatrix} 3 & 8 \end{pmatrix}$.
4. $\begin{pmatrix} 3 & 8 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 11 & 21 \end{pmatrix}$.
5. $h = (x - y)xy + x^2y^2 = x^2y - xy^2 + x^2y^2$ : $\frac{\partial h}{\partial x} = 2xy - y^2 + 2xy^2 = 11$ et $\frac{\partial h}{\partial y} = x^2 - 2xy + 2x^2y = 21$ en $(3, 1)$.

### M18.R2 — Le gradient de wᵀAw (M09b)
1. $\mathbf{A}\mathbf{w} = (5, 0)$, donc $\mathbf{w}^\top\mathbf{A}\mathbf{w} = 10$.
2. $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w} = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix}\begin{pmatrix} 2 \\ 1 \end{pmatrix} = (6, 8)$.
3. Faux : $2\mathbf{A}\mathbf{w} = (10, 0)$ ; la formule $2\mathbf{A}\mathbf{w}$ ne vaut que pour $\mathbf{A}$ symétrique.
4. $\mathbf{a} = (4, -3)$.
5. $\frac12(\mathbf{A} + \mathbf{A}^\top) = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.

### M18.R3 — Différences centrées et choix du pas (M05a)
1. $\frac{f(x + h) - f(x - h)}{2h}$ ; erreur de troncature d'ordre $h^2$ (environ $\frac{h^2}{6}f'''(x)$).
2. $\frac{1{,}1^3 - 0{,}9^3}{0{,}2} = \frac{1{,}331 - 0{,}729}{0{,}2} = 3{,}01$ ; l'erreur vaut $0{,}01 = h^2$ (ici $f''' = 6$).
3. Vers $10^{-5}$ (de l'ordre de $\sqrt[3]{\varepsilon_{\text{machine}}}$).
4. Faux : en dessous du meilleur pas, les arrondis divisés par $2h$ grandissent.
5. D'ordre $h$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M18.1 — Le graphe de calcul d'une formule de physique

**Réponses.** a) `[0.25, 16, 4, 8, 4, 0.5, 0.5, 1, 10, 5]` · b) `9` · c) `16` · d) `2` · e) `5`.

**Démarche.** a) $u_1 = 0{,}25$, $u_2 = 16$, $u_3 = 4$, $u_4 = 8$, $u_5 = 4$ (l'énergie cinétique), $u_6 = \cos\frac{\pi}{3} = 0{,}5$, $u_7 = 0{,}5$, $u_8 = 1$, $u_9 = 10$, $u_{10} = 5$ (l'énergie potentielle). b) $E = 4 + 5 = 9$ J. c) Une arête par argument de chaque opération : $u_1$, $u_2$, $u_5$, $u_6$, $u_7$, $u_9$ en ont une, $u_3$, $u_4$, $u_8$, $u_{10}$ et $E$ deux : $6 + 10 = 16$. d) $m$ (vers $u_4$ et $u_8$) et $\ell$ (vers $u_1$ et $u_8$) ; chaque autre nœud ne sert qu'une fois. e) Étape 1 : $u_1$, $u_2$, $u_6$, $u_8$ ; étape 2 : $u_3$, $u_7$, $u_9$ ; étape 3 : $u_4$, $u_{10}$ ; étape 4 : $u_5$ ; étape 5 : $E$. C'est la longueur du plus long chemin, par exemple $\ell \to u_1 \to u_3 \to u_4 \to u_5 \to E$ (5 arêtes).

Dans ta copie : deux ordres valides, l'ordre de l'énoncé et $(u_6, u_7, u_8, u_9, u_{10}, u_1, u_2, u_3, u_4, u_5, E)$. Le graphe n'a pas de cycle : chaque nœud est calculé à partir de nœuds déjà calculés, donc chaque arête va vers un numéro plus grand (M16 §4).

**Erreurs fréquentes.** Compter $u_1 = \ell^2$ avec deux arêtes (ici, le carré est une opération à un argument). Confondre nœuds (15) et arêtes (16). Calculer $\cos\frac{\pi}{3}$ en degrés. Répondre 11 à e) : c'est le nombre d'opérations faites une à une.

**Variante.** Avec $\theta = \frac{\pi}{2}$ et $\omega = 2$ : $u_2 = 4$, $u_3 = 1$, $u_4 = 2$, $u_5 = 1$, $u_6 = 0$, $u_7 = 1$, $u_{10} = 10$, et $E = 11$.

### Ex M18.2 — Dériver par la somme sur les chemins

**Réponses.** a) `16` · b) `4` · c) `"-16/3"` · d) `"-4/3"` · e) `"8/3"` · f) `"-16/3"` · g) `2`.

**Démarche.** Les valeurs : $u_1 = 144$, $u_2 = 6$, $u_3 = 36$, $u_4 = 576$, $P = 16$. Les dérivées locales : $\frac{\partial u_1}{\partial E} = 2E = 24$ ; $\frac{\partial u_2}{\partial R} = \frac{\partial u_2}{\partial r} = 1$ ; $\frac{\partial u_3}{\partial u_2} = 2u_2 = 12$ ; $\frac{\partial u_4}{\partial u_1} = R = 4$ ; $\frac{\partial u_4}{\partial R} = u_1 = 144$ ; $\frac{\partial P}{\partial u_4} = \frac{1}{u_3} = \frac{1}{36}$ ; $\frac{\partial P}{\partial u_3} = -\frac{u_4}{u_3^2} = -\frac49$. b) $144 \times \frac{1}{36} = 4$. c) $1 \times 12 \times (-\frac49) = -\frac{16}{3}$. d) $4 - \frac{16}{3} = -\frac43$. e) Un seul chemin, $E \to u_1 \to u_4 \to P$ : $24 \times 4 \times \frac{1}{36} = \frac83$. f) Un seul chemin, $r \to u_2 \to u_3 \to P$ : $-\frac{16}{3}$. g) Pour $R$ quelconque, $\frac{\partial P}{\partial R} = \frac{E^2(r - R)}{(R + r)^3}$ : positive pour $R < r$, négative pour $R > r$, d'où un maximum en $R = r = 2$.

Dans ta copie : $R$ sert deux fois (au numérateur, dans $u_4$, et au dénominateur, dans $u_2$), $E$ une seule fois. Dérivée directe : $P(R) = \frac{144R}{(R + 2)^2}$, $P'(R) = 144\,\frac{(R + 2) - 2R}{(R + 2)^3} = \frac{144(2 - R)}{(R + 2)^3}$, qui vaut $-\frac{288}{216} = -\frac43$ en 4. La puissance reçue est maximale quand la résistance branchée égale la résistance interne du générateur (l'**adaptation d'impédance** des électroniciens) ; elle vaut alors $\frac{E^2}{4r} = 18$ W.

**Erreurs fréquentes.** Ne garder qu'un chemin ($4$, ou $-\frac{16}{3}$). Oublier le signe de $\frac{\partial P}{\partial u_3}$. Oublier le facteur $2u_2$ du carré.

**Variante.** $E = 6$, $R = 1$, $r = 2$ : $P = 4$ et $\frac{\partial P}{\partial R} = \frac{36 \times 1}{27} = \frac43$.

### Ex M18.3 — Le mode direct à la main

**Réponses.** a) `[4, 4]` · b) `[-4, -4]` · c) `[0, 1]` · d) `[-4, -3]` · e) `[-4, 5]` · f) `[-4, 7]` · g) `[3, 5]`.

**Démarche.** a) $4 + 4\varepsilon + \varepsilon^2 = 4 + 4\varepsilon$. b) $(4 + 4\varepsilon)(-1) = -4 - 4\varepsilon$. c) $x + y = 1 + \varepsilon$, et $\ln(1 + \varepsilon) = \ln 1 + \frac11\varepsilon = \varepsilon$. d) $-4 - 4\varepsilon + \varepsilon = -4 - 3\varepsilon$. e) $x^2 = 4$, $x^2y = -4 + 4\varepsilon$, $\ln(1 + \varepsilon) = \varepsilon$ : $-4 + 5\varepsilon$. f) $x^2y = (4 + 4\varepsilon)(-1 + 2\varepsilon) = -4 + 8\varepsilon - 4\varepsilon = -4 + 4\varepsilon$, $x + y = 1 + 3\varepsilon$, $\ln(1 + 3\varepsilon) = 3\varepsilon$ : $-4 + 7\varepsilon$. g) $\frac{3}{1} + \frac{2 \times 1 - 3 \times (-1)}{1^2}\varepsilon = 3 + 5\varepsilon$ ; en multipliant haut et bas par $1 + \varepsilon$ : $\frac{(3 + 2\varepsilon)(1 + \varepsilon)}{1 - \varepsilon^2} = 3 + 5\varepsilon$.

Dans ta copie : $\nabla f(2, -1) = (-3, 5)$, en deux passes (une par variable). Directement : $\frac{\partial f}{\partial x} = 2xy + \frac{1}{x + y} = -4 + 1$ et $\frac{\partial f}{\partial y} = x^2 + \frac{1}{x + y} = 4 + 1$. La partie en $\varepsilon$ de f) est le produit jacobienne-vecteur $\mathbf{J}\mathbf{v} = \nabla f \cdot (1, 2) = -3 + 10 = 7$ (M17 §5) : une graine quelconque donne la dérivée dans sa direction, sans la normaliser.

**Erreurs fréquentes.** Mettre la graine 1 sur les deux variables à la fois et croire obtenir une dérivée partielle (on obtient leur somme, 2). Écrire $\ln(1 + \varepsilon) = 1 + \varepsilon$. Inverser la règle du quotient ($\frac{ad - bc}{c^2}$ donne $-5$).

**Variante.** En $(1, 1)$, avec la graine sur $x$ : $f(1 + \varepsilon, 1) = (1 + \ln 2) + 2{,}5\,\varepsilon$.

### Ex M18.4 — Le mode inverse à la main

**Réponses.** a) `[3, 4, 2, 6]` · b) `[3, 0.75]` · c) `2.75` · d) `[2.75, 9]` · e) `-0.175` · f) `-0.188`.

**Démarche.** Passe avant : $u_1 = 3$, $u_2 = 4$, $u_3 = 2$, $f = 6$. Passe arrière, dans l'ordre $f, u_3, u_2, u_1, q, p$ : $\bar{f} = 1$ ; $\bar{u}_3 = \bar{f} \times u_1 = 3$ ; $\bar{u}_2 = \bar{u}_3 \times \frac{1}{2\sqrt{u_2}} = 3 \times \frac14 = 0{,}75$ ; $\bar{u}_1 = \bar{f} \times u_3 + \bar{u}_2 \times 1 = 2 + 0{,}75 = 2{,}75$ ; $\bar{q} = \bar{u}_2 \times 1 + \bar{u}_1 \times p = 0{,}75 + 8{,}25 = 9$ ; $\bar{p} = \bar{u}_1 \times q = 2{,}75$. e) $2{,}75 \times 0{,}1 + 9 \times (-0{,}05) = -0{,}175$. f) $u_1 = 2{,}945$, $u_2 = 3{,}895$, $f = 2{,}945 \times 1{,}973575\ldots \approx 5{,}81218$, d'où $-0{,}188$.

Dans ta copie : $u_1$ reçoit deux contributions ($f$ l'utilise directement, et à travers $u_2$), $q$ aussi (à travers $u_1$ et $u_2$). Dérivée directe : $\frac{\partial f}{\partial p} = q\sqrt{pq + q} + \frac{pq \cdot q}{2\sqrt{pq + q}} = 2 + 0{,}75$ et $\frac{\partial f}{\partial q} = p\sqrt{pq + q} + \frac{pq\,(p + 1)}{2\sqrt{pq + q}} = 6 + 3$. L'écart entre e) et f), environ $0{,}013$, vient des termes d'ordre 2 que l'approximation linéaire néglige ; pour un déplacement dix fois plus petit, il serait environ cent fois plus petit.

**Erreurs fréquentes.** $\bar{u}_1 = 2$ (la contribution de $u_2$ oubliée), qui donne $\bar{p} = 2$ et $\bar{q} = 6{,}75$. Utiliser $\bar{u}_1$ avant d'avoir calculé $\bar{u}_2$. Prendre $\sqrt{u_2}$ pour la dérivée locale de la racine au lieu de $\frac{1}{2\sqrt{u_2}}$.

**Variante.** En $(p, q) = (2, 1)$ : $f = 2\sqrt3$ et $\nabla f = (\frac{4}{\sqrt3} ;\ 3\sqrt3) \approx (2{,}3094 ;\ 5{,}1962)$.

### Ex M18.5 — Le même gradient par les deux modes

**Réponses.** a) `60` · b) `[35, 32, 27]` · c) `[4, 15]` · d) `[20, 12]` · e) `[35, 32, 27]` · f) `[3, 1]` · g) `[30, 10]`.

**Démarche.** Valeurs : $u_1 = 3$, $u_2 = 5$, $u_3 = 4$, $u_4 = 15$, $f = 60$. Dérivées locales : 1 sur les six arêtes des sommes ; $\frac{\partial u_4}{\partial u_1} = u_2 = 5$, $\frac{\partial u_4}{\partial u_2} = u_1 = 3$, $\frac{\partial f}{\partial u_4} = u_3 = 4$, $\frac{\partial f}{\partial u_3} = u_4 = 15$. Mode direct, graine $\mathbf{e}_1$ : $\dot{u}_1 = 1$, $\dot{u}_2 = 0$, $\dot{u}_3 = 1$, $\dot{u}_4 = 5$, $\dot{f} = 4 \times 5 + 15 \times 1 = 35$ ; graine $\mathbf{e}_2$ : $\dot{u}_4 = 5 + 3 = 8$, $\dot{f} = 32$ ; graine $\mathbf{e}_3$ : $\dot{u}_4 = 3$, $\dot{f} = 12 + 15 = 27$. Mode inverse : $\bar{u}_4 = 4$, $\bar{u}_3 = 15$, $\bar{u}_1 = 4 \times 5 = 20$, $\bar{u}_2 = 4 \times 3 = 12$, $\bar{x}_1 = \bar{u}_1 + \bar{u}_3 = 35$, $\bar{x}_2 = \bar{u}_1 + \bar{u}_2 = 32$, $\bar{x}_3 = \bar{u}_2 + \bar{u}_3 = 27$. g) Chaque passe directe utilise chacune des dix arêtes une fois : $3 \times 10 = 30$ ; la passe arrière aussi, une seule fois : 10.

Dans ta copie : pour 100 variables et 1 000 arêtes, $100 \times 1\,000 = 100\,000$ produits en mode direct, contre 1 000 en mode inverse : le rapport est le nombre d'entrées.

**Erreurs fréquentes.** Oublier que $x_1$ sert dans $u_1$ **et** $u_3$ (même chose pour $x_2$ et $x_3$). Ne donner à $\bar{x}_2$ que $\bar{u}_1$.

**Variante.** En $(1, 1, 1)$ : $f = 8$ et $\nabla f = (8, 8, 8)$.

### Ex M18.6 — Le gradient de aᵀXb, de la forme de X

**Réponses.** a) `1` · b) `-4` · c) `[[2, 0.5], [-4, -1], [6, 1.5]]` · d) `[3, 2]` · e) `-1.3` · f) `-0.3`.

**Démarche.** $\mathbf{X}\mathbf{b} = (2 ;\ 3{,}5 ;\ 2)$ et $\mathbf{a}^\top\mathbf{X}\mathbf{b} = 2 - 7 + 6 = 1$. Chaque terme $a_iX_{ij}b_j$ ne contient $X_{ij}$ qu'une fois : $\frac{\partial f}{\partial X_{ij}} = a_ib_j$. b) $a_2b_1 = -4$. c) Le tableau des $a_ib_j$, de la forme de $\mathbf{X}$ : $\mathbf{a}\mathbf{b}^\top$. e) $\sum_{ij}G_{ij}H_{ij} = (-1) \times 0{,}1 + 6 \times (-0{,}2) = -1{,}3$. f) $1 - 1{,}3 = -0{,}3$ ; directement, $(\mathbf{X} + \mathbf{H})\mathbf{b} = (2 ;\ 3{,}55 ;\ 1{,}6)$ et $2 - 7{,}1 + 4{,}8 = -0{,}3$.

Dans ta copie : le gradient ne dépend pas de $\mathbf{X}$ parce que $f$ est **linéaire** en $\mathbf{X}$ ; pour la même raison, la prévision e) n'a pas de terme d'ordre 2 et elle est exacte.

**Erreurs fréquentes.** Écrire $\mathbf{b}\mathbf{a}^\top$, de forme $(2, 3)$ : la transposée. Mélanger les indices ($a_jb_i$).

**Variante.** $\mathbf{a} = (1, 1, 0)$, $\mathbf{b} = (0, 2)$ : $\nabla f = \begin{pmatrix} 0 & 2 \\ 0 & 2 \\ 0 & 0 \end{pmatrix}$.

### Ex M18.7 — Les gradients de tr(AX) et de tr(XᵀAX)

**Réponses.** a) `-3` · b) `[[2, -1], [1, 3]]` · c) `-1` · d) `13` · e) `[[4, 8], [0, -6]]` · f) `12`.

**Démarche.** $\mathbf{A}\mathbf{X} = \begin{pmatrix} 2 & 3 \\ -1 & -5 \end{pmatrix}$, de trace $-3$. $\operatorname{tr}(\mathbf{A}\mathbf{X}) = \sum_{i,j}A_{ji}X_{ij}$, donc $\frac{\partial}{\partial X_{ij}} = A_{ji}$ : le gradient est $\mathbf{A}^\top$, et c) vaut $A_{21} = -1$. d) $\mathbf{X}^\top\mathbf{A}\mathbf{X} = \begin{pmatrix} 2 & 3 \\ 5 & 11 \end{pmatrix}$, de trace 13. e) $\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X}) = \sum_k\sum_{i,j}X_{ik}A_{ij}X_{jk}$ ; dériver par rapport à $X_{pq}$ donne $\sum_jA_{pj}X_{jq} + \sum_iX_{iq}A_{ip} = (\mathbf{A}\mathbf{X})_{pq} + (\mathbf{A}^\top\mathbf{X})_{pq}$ : le gradient est $(\mathbf{A} + \mathbf{A}^\top)\mathbf{X} = \begin{pmatrix} 4 & 0 \\ 0 & 6 \end{pmatrix}\mathbf{X}$. f) $\sum_{ij}G_{ij}H_{ij} = 4 \times 1 + 8 \times 1 = 12$ ; un gradient transposé donnerait $4 + 0 = 4$ : la direction, non symétrique, le démasque.

Dans ta copie : $2\mathbf{A}\mathbf{X}$ serait faux parce que $\mathbf{A}$ n'est pas symétrique (seule sa partie symétrique compte). Pour une seule colonne $\mathbf{X} = \mathbf{w}$, on retrouve $\nabla(\mathbf{w}^\top\mathbf{A}\mathbf{w}) = (\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ de M09b.

**Erreurs fréquentes.** Rendre $\mathbf{A}$ au lieu de $\mathbf{A}^\top$ pour $\operatorname{tr}(\mathbf{A}\mathbf{X})$. Écrire $2\mathbf{A}\mathbf{X}$. Oublier l'un des deux termes de la dérivée du produit.

**Variante.** Pour $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$, symétrique, $\nabla\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X}) = 2\mathbf{A}\mathbf{X}$.

### Ex M18.8 — Le gradient de log det X sur une matrice 2 × 2

**Réponses.** a) `10` · b) `[[3, -2], [-1, 4]]` · c) `[[0.3, -0.2], [-0.1, 0.4]]` · d) `[[0.3, -0.1], [-0.2, 0.4]]` · e) `-0.5` · f) `-0.00502`.

**Démarche.** $\det\mathbf{X} = x_{11}x_{22} - x_{12}x_{21} = 12 - 2 = 10$, et ses dérivées partielles se rangent en $\begin{pmatrix} x_{22} & -x_{21} \\ -x_{12} & x_{11} \end{pmatrix}$ : la comatrice. c) Par la règle de la chaîne avec $\ln$ : b) divisé par 10. d) $\mathbf{X}^{-1} = \frac{1}{10}\begin{pmatrix} 3 & -1 \\ -2 & 4 \end{pmatrix}$. e) $\sum_{ij}G_{ij}H_{ij} = 0{,}3 \times 1 + (-0{,}2) \times 2 + (-0{,}1) \times 0 + 0{,}4 \times (-1) = -0{,}5$. f) $\det(\mathbf{X} + 0{,}01\,\mathbf{H}) = 4{,}01 \times 2{,}99 - 1{,}02 \times 2 = 9{,}9499$, et $\ln\frac{9{,}9499}{10} = \ln 0{,}99499 \approx -0{,}0050226$. Avec $\ln 9{,}9499 - \ln 10$ et des logarithmes arrondis à 5 décimales ($2{,}29756 - 2{,}30259$), on trouverait $-0{,}00503$ : la différence de deux nombres voisins perd des chiffres.

Dans ta copie : c) est la transposée de d) : $\nabla\ln\det\mathbf{X} = \mathbf{X}^{-\top}$, parce que la comatrice vaut $\det\mathbf{X}\,\mathbf{X}^{-\top}$ (fiche §7). f) est proche de $0{,}01 \times$ e) $= -0{,}005$ : c'est l'approximation linéaire, et l'écart, environ $2 \times 10^{-5}$, est d'ordre 2.

**Erreurs fréquentes.** Rendre $\mathbf{X}^{-1}$ au lieu de $\mathbf{X}^{-\top}$ (e) vaudrait alors $-0{,}3$). Oublier les signes moins des cofacteurs. Prendre le logarithme décimal.

**Variante.** $\mathbf{X} = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$ : $\det\mathbf{X} = 6$ et $\nabla\ln\det\mathbf{X} = \begin{pmatrix} 0{,}5 & -\frac16 \\ 0 & \frac13 \end{pmatrix}$.

### Ex M18.9 — Le gradient d'une moyenne de distances

**Réponses.** a) `4.584` · b) `[0.9487, 0.3162]` · c) `[0.040, -0.263]` · d) `[0, 0]` · e) `4.3574` · f) `0.032`.

**Démarche.** a) Les distances de $(3, 1)$ aux villes : $\sqrt{10}$, $\sqrt{26}$, $\sqrt{34}$, $\sqrt{18}$, de moyenne $4{,}5837$. b) $\frac{(3, 1)}{\sqrt{10}}$. c) La moyenne des quatre vecteurs unitaires $\frac{\mathbf{p} - \mathbf{x}_k}{\lVert\mathbf{p} - \mathbf{x}_k\rVert}$ : $(0{,}9487 ;\ 0{,}3162)$, $(-0{,}9806 ;\ 0{,}1961)$, $(-0{,}5145 ;\ -0{,}8575)$, $(0{,}7071 ;\ -0{,}7071)$, de moyenne $(0{,}0402 ;\ -0{,}2631)$. d) Les diagonales $y = x$ et $y = 4 - \frac{x}{2}$ se coupent en $(\frac83, \frac83)$. Ce point est **sur** le segment $[AC]$, entre $A$ et $C$ : les vecteurs unitaires vers $A$ et vers $C$ sont opposés ; de même pour $B$ et $D$ ; leur somme est nulle. e) En ce point, $F = \frac{AC + BD}{4} = \frac{6\sqrt2 + 4\sqrt5}{4} \approx 4{,}3574$. f) Le centroïde est $(3{,}5 ;\ 2{,}5)$, où $F \approx 4{,}3895$ : l'écart vaut $0{,}032$.

Dans ta copie : c'est bien le minimum, et pas seulement un point où le gradient s'annule : pour tout $\mathbf{p}$, l'inégalité triangulaire donne $\lVert\mathbf{p} - A\rVert + \lVert\mathbf{p} - C\rVert \ge AC$ et $\lVert\mathbf{p} - B\rVert + \lVert\mathbf{p} - D\rVert \ge BD$, avec égalité sur les deux diagonales à la fois. Le centroïde minimise la moyenne des **carrés** des distances ; les carrés donnent plus de poids aux villes lointaines, et le centroïde s'y rapproche de $B$, la plus éloignée.

**Erreurs fréquentes.** Sommer les gradients au lieu d'en faire la moyenne (c) donnerait $(0{,}161 ;\ -1{,}052)$). Oublier de normaliser (on obtient le gradient des carrés, divisé par 2). Croire que le centroïde est le meilleur point.

**Variante.** Les quatre coins d'un carré $(0, 0)$, $(4, 0)$, $(4, 4)$, $(0, 4)$ : le minimum est au centre $(2, 2)$, et vaut $2\sqrt2 \approx 2{,}8284$.

### Ex M18.10 — La différentielle d'une fonction de matrice

**Réponses.** a) `6` · b) `[[2, -2], [4, 6]]` · c) `-2` · d) `8` · e) `[[2, 4], [0, 2]]` · f) `-6`.

**Démarche.** $\mathbf{X}^2 = \begin{pmatrix} -1 & 8 \\ -4 & 7 \end{pmatrix}$, de trace 6. $\mathrm{d}f = \operatorname{tr}(\mathrm{d}\mathbf{X}\,\mathbf{X} + \mathbf{X}\,\mathrm{d}\mathbf{X}) = 2\operatorname{tr}(\mathbf{X}\,\mathrm{d}\mathbf{X})$ (cyclicité), donc $\nabla f = (2\mathbf{X})^\top = 2\mathbf{X}^\top$. c) $\operatorname{tr}(\mathbf{X}^2) = \sum_{i,j}X_{ij}X_{ji}$ contient $X_{12}$ dans les deux termes $X_{12}X_{21}$ et $X_{21}X_{12}$ : $\frac{\partial f}{\partial X_{12}} = 2X_{21} = -2$. d) $g(\mathbf{X}) = (\mathbf{X}^2)_{12} = 8$. e) $\mathrm{d}g = \mathbf{a}^\top(\mathrm{d}\mathbf{X}\,\mathbf{X} + \mathbf{X}\,\mathrm{d}\mathbf{X})\mathbf{b} = \operatorname{tr}(\mathbf{X}\mathbf{b}\mathbf{a}^\top\mathrm{d}\mathbf{X}) + \operatorname{tr}(\mathbf{b}\mathbf{a}^\top\mathbf{X}\,\mathrm{d}\mathbf{X})$, donc $\nabla g = \mathbf{a}\mathbf{b}^\top\mathbf{X}^\top + \mathbf{X}^\top\mathbf{a}\mathbf{b}^\top = \begin{pmatrix} 2 & 3 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ 0 & 2 \end{pmatrix}$. Vérification : $g = X_{11}X_{12} + X_{12}X_{22}$ a pour dérivées $X_{12} = 2$, $X_{11} + X_{22} = 4$, $0$ et $X_{12} = 2$. f) $\sum_{ij}G_{ij}H_{ij} = 2 - 2 + 0 - 6 = -6$.

**Erreurs fréquentes.** Rendre $2\mathbf{X}$ au lieu de $2\mathbf{X}^\top$ (f) vaudrait alors 0). Écrire $\mathrm{d}(\mathbf{X}^2) = 2\mathbf{X}\,\mathrm{d}\mathbf{X}$ : faux pour des matrices (l'ordre des facteurs compte), même si la trace le rattrape pour $f$ ; pour $g$, il donnerait un gradient faux.

**Variante.** Pour $\mathbf{X} = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$, symétrique, $\nabla\operatorname{tr}(\mathbf{X}^2) = 2\mathbf{X}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M18.11 — La règle de la chaîne sur un graphe sans cycle : la somme sur les chemins

**Démonstration.**
1. Pour $k > n$, $u_k = \varphi_k(u_j,\ j \text{ prédécesseur de } k)$, et chaque $u_j$ est une fonction dérivable de $x$ (par récurrence sur le numéro). La règle de la chaîne de M17 (une sortie, plusieurs variables intermédiaires) donne $\dot{u}_k = \sum_j\frac{\partial\varphi_k}{\partial u_j}\,\dot{u}_j = \sum_{j < k}D_{jk}\,\dot{u}_j$ ($D_{jk} = 0$ quand $u_j$ n'est pas un argument de $\varphi_k$). Pour les entrées : $\dot{u}_i = 1$ et $\dot{u}_j = 0$ pour les autres entrées, qui restent fixes.
2. Récurrence forte sur $k$. Pour une entrée : il n'y a que le chemin vide de $x$ à lui-même, donc $S_i = 1 = \dot{u}_i$ ; aucun chemin ne mène de $x$ à une autre entrée (une entrée n'a pas de prédécesseur), donc $S_j = 0 = \dot{u}_j$. Pour $k > n$, supposons $\dot{u}_j = S_j$ pour tout $j < k$. Un chemin de $x$ à $u_k$ n'est pas vide ; sa dernière arête est $u_j \to u_k$ avec $j < k$, et le reste est un chemin de $x$ à $u_j$. Inversement, tout chemin de $x$ à $u_j$ prolongé par une arête $u_j \to u_k$ est un chemin de $x$ à $u_k$. Donc $S_k = \sum_{j < k}D_{jk}\,S_j = \sum_{j < k}D_{jk}\,\dot{u}_j = \dot{u}_k$.
3. Avec $k = N$ : $\frac{\partial y}{\partial x} = \dot{u}_N = S_N$, la somme sur les chemins de $x$ à $y$.
4. La numérotation garantit que tous les prédécesseurs de $u_k$ ont un numéro plus petit : l'hypothèse de récurrence les couvre, et chaque $\dot{u}_j$ est connu quand on calcule $\dot{u}_k$. Avec un cycle, aucun ordre de calcul n'existe, $u_k$ dépendrait de lui-même, et il y aurait une infinité de chemins.
5. La coordonnée $k$ de $\mathbf{e}_i + \mathbf{D}^\top\dot{\mathbf{u}}$ vaut $\delta_{ik} + \sum_jD_{jk}\,\dot{u}_j$ : pour $k > n$, c'est la formule de la question 1 ($\delta_{ik} = 0$ puisque $i \le n < k$) ; pour une entrée, la somme est vide et il reste $\delta_{ik}$. Donc $(\mathbf{I} - \mathbf{D}^\top)\dot{\mathbf{u}} = \mathbf{e}_i$. $\mathbf{D}$ est strictement triangulaire supérieure, donc nilpotente (M16), et $\mathbf{I} - \mathbf{D}^\top$ est inversible : $\dot{\mathbf{u}} = \big((\mathbf{I} - \mathbf{D})^{-1}\big)^\top\mathbf{e}_i$, dont la coordonnée $N$ est le coefficient $(i, N)$ de $(\mathbf{I} - \mathbf{D})^{-1}$.

**Grille de relecture.** La règle de la chaîne de M17 est citée pour l'étape 1, avec la dérivabilité des $u_j$. La récurrence est forte, et son initialisation traite les entrées autres que $x$. L'hérédité classe les chemins par leur dernière arête, dans les deux sens (tout chemin s'écrit ainsi, et tout prolongement est un chemin). Le rôle de la numérotation est dit.

**Variante.** La même récurrence, avec $\mathbf{D}$ remplacée par la matrice des parts d'eau, redonne la somme sur les chemins du réseau d'eau de M16 §4.

### Ex M18.12 — Les nombres duaux calculent la dérivée

**Démonstration.**
1. $(a + b\varepsilon)(c + d\varepsilon) = ac + ad\varepsilon + bc\varepsilon + bd\varepsilon^2 = ac + (ad + bc)\varepsilon$. Et $(c + d\varepsilon)\big(\frac{a}{c} + \frac{bc - ad}{c^2}\varepsilon\big) = a + \big(\frac{ad}{c} + \frac{bc - ad}{c}\big)\varepsilon = a + b\varepsilon$ : c'est bien le quotient.
2. $x \mapsto x$ : $a + b\varepsilon = a + b \times 1 \times \varepsilon$. Une constante $c$ : $c = c + b \times 0 \times \varepsilon$. Si $f$ et $g$ sont compatibles : $(f + g)(a + b\varepsilon) = f(a) + g(a) + b\,(f'(a) + g'(a))\,\varepsilon$ ; $(fg)(a + b\varepsilon) = \big(f(a) + bf'(a)\varepsilon\big)\big(g(a) + bg'(a)\varepsilon\big) = f(a)g(a) + b\,\big(f'(a)g(a) + f(a)g'(a)\big)\varepsilon$, la règle du produit ; et, par 1., $\frac{f}{g}(a + b\varepsilon) = \frac{f(a)}{g(a)} + b\,\frac{f'(a)g(a) - f(a)g'(a)}{g(a)^2}\,\varepsilon$, la règle du quotient.
3. $g\big(f(a + b\varepsilon)\big) = g\big(f(a) + bf'(a)\,\varepsilon\big) = g(f(a)) + bf'(a)\,g'(f(a))\,\varepsilon$, en appliquant la compatibilité de $g$ au point $f(a)$ avec la partie en $\varepsilon$ égale à $bf'(a)$ : c'est $(g \circ f)(a) + b\,(g \circ f)'(a)\,\varepsilon$.
4. Par récurrence sur la construction de $f$ (sur les nœuds de son graphe de calcul, dans l'ordre du calcul) : chaque nœud est une fonction compatible de $x$, d'après 2. et 3. ; donc $f$ aussi. Avec $b = 1$ : $f(a + \varepsilon) = f(a) + f'(a)\,\varepsilon$.
5. $(a + b\varepsilon)^n = \sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^k\varepsilon^k = a^n + na^{n-1}b\,\varepsilon$, car $\varepsilon^k = 0$ pour $k \ge 2$.
6. $e^{b\varepsilon} = \sum_k\frac{(b\varepsilon)^k}{k!} = 1 + b\varepsilon$ : la série s'arrête. Donc $e^{a + b\varepsilon} = e^a(1 + b\varepsilon)$ : la définition n'est pas arbitraire, c'est la seule compatible avec $e^{u + w} = e^ue^w$.

**Grille de relecture.** Le calcul de 1. utilise $\varepsilon^2 = 0$ et vérifie le quotient. Chaque règle de 2. et 3. est rapprochée de la règle de dérivation correspondante. La conclusion 4. est une récurrence (sur la construction), pas un « et ainsi de suite ». Le cas $g(a) \ne 0$ est noté pour le quotient.

**Variante.** Le modèle matriciel : $a + b\varepsilon \mapsto \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$ transforme les sommes et les produits de nombres duaux en sommes et produits de matrices ; $\varepsilon$ devient la matrice nilpotente $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

### Ex M18.13 — Le mode inverse calcule tout le gradient en un passage

**Démonstration.**
1. Pour $j < N$, un chemin de $u_j$ à $y$ n'est pas vide ; sa première arête est $u_j \to u_k$ avec $k > j$, et le reste est un chemin de $u_k$ à $y$ ; inversement, une arête $u_j \to u_k$ suivie d'un chemin de $u_k$ à $y$ est un chemin de $u_j$ à $y$. Donc $T_j = \sum_{k > j}D_{jk}T_k$.
2. En décroissant de $N$ à 1, tous les $T_k$ avec $k > j$ sont déjà calculés quand on arrive à $j$.
3. Pour une entrée $x_i = u_i$, $T_i$ est la somme sur les chemins de $x_i$ à $y$, c'est-à-dire $S_N$ de M18.11 avec $x = x_i$ : $T_i = \frac{\partial y}{\partial x_i}$. La même passe donne $T_i$ pour **toutes** les entrées.
4. Considérons un nouveau calcul dont les entrées sont $u_1, \ldots, u_j$ (déjà numérotées en tête) : $u_j$ y devient une entrée libre, les arêtes qui y arrivent disparaissent, et tout ce qui vient après est recalculé à partir de ces entrées. Les chemins de $u_j$ à $y$ sont les mêmes dans ce nouveau graphe, et M18.11 donne $\frac{\partial y}{\partial u_j} = T_j$ : c'est l'adjoint $\bar{u}_j$.
5. La coordonnée $j$ de $\mathbf{e}_N + \mathbf{D}\mathbf{t}$ vaut $\delta_{jN} + \sum_kD_{jk}T_k = T_j$. Donc $(\mathbf{I} - \mathbf{D})\mathbf{t} = \mathbf{e}_N$ et $\mathbf{t} = (\mathbf{I} - \mathbf{D})^{-1}\mathbf{e}_N$ : la **colonne** $N$. Une passe directe de graine $\mathbf{e}_i$ donne la **ligne** $i$ (M18.11). Les deux se croisent au coefficient $(i, N)$, $\frac{\partial y}{\partial x_i}$ : le mode direct obtient les $n$ coefficients utiles en $n$ passes, le mode inverse en une.
6. Chaque arête $u_j \to u_k$ sert une fois, dans le calcul de $T_j$ : le coût est proportionnel au nombre d'arêtes, quel que soit le nombre d'entrées. Les dérivées locales $D_{jk}$ dépendent des valeurs des arguments de $\varphi_k$ : il faut avoir gardé toute la passe avant.

**Grille de relecture.** L'étape 1 classe les chemins par leur première arête (symétrique de M18.11). L'ordre décroissant est justifié. Le lien avec M18.11 est explicite pour les entrées. L'interprétation de $T_j$ comme $\frac{\partial y}{\partial u_j}$ précise ce qui est recalculé. Le coût et la mémoire sont dits.

**Variante.** Pour $m$ sorties, on fait $m$ passes arrière, de graines $\mathbf{e}_{N_1}, \ldots, \mathbf{e}_{N_m}$ : les $m$ lignes de la jacobienne.

### Ex M18.14 — ∇ log det X = X⁻ᵀ, par le développement selon une ligne

**Démonstration.**
1. $C_{ij}$ est $(-1)^{i+j}$ fois le déterminant de la matrice obtenue en retirant la ligne $i$ et la colonne $j$ de $\mathbf{X}$ : aucun coefficient de la ligne $i$ n'y reste.
2. Dans $\det\mathbf{X} = \sum_jX_{ij}C_{ij}$, les $C_{ij}$ ne dépendent pas de la ligne $i$ : le déterminant est une fonction **affine** des coefficients de cette ligne, et $\frac{\partial\det\mathbf{X}}{\partial X_{ij}} = C_{ij}$. Comme $i$ est quelconque, $\nabla_{\mathbf{X}}\det\mathbf{X} = \operatorname{com}(\mathbf{X})$.
3. $\mathbf{X}\operatorname{com}(\mathbf{X})^\top = \det\mathbf{X}\;\mathbf{I}$ donne $\mathbf{X}^{-1} = \frac{\operatorname{com}(\mathbf{X})^\top}{\det\mathbf{X}}$, donc $\operatorname{com}(\mathbf{X}) = \det\mathbf{X}\,(\mathbf{X}^{-1})^\top = \det\mathbf{X}\;\mathbf{X}^{-\top}$.
4. Règle de la chaîne avec $\ln$ : $\frac{\partial\ln\det\mathbf{X}}{\partial X_{ij}} = \frac{C_{ij}}{\det\mathbf{X}}$, donc $\nabla\ln\det\mathbf{X} = \frac{\operatorname{com}(\mathbf{X})}{\det\mathbf{X}} = \mathbf{X}^{-\top}$. Si $\det\mathbf{X} < 0$, $\ln\lvert\det\mathbf{X}\rvert = \ln(-\det\mathbf{X})$ a pour dérivées $\frac{-C_{ij}}{-\det\mathbf{X}}$ : le même $\mathbf{X}^{-\top}$.
5. $\operatorname{com}\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}$, ce que donnent les dérivées de $ad - bc$ ; et $\mathbf{X}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, dont la transposée est bien $\frac{\operatorname{com}(\mathbf{X})}{ad - bc}$.
6. $\mathrm{d}(\det\mathbf{X}) = \sum_{ij}C_{ij}\,\mathrm{d}X_{ij} = \operatorname{tr}\big(\operatorname{com}(\mathbf{X})^\top\mathrm{d}\mathbf{X}\big) = \det\mathbf{X}\,\operatorname{tr}(\mathbf{X}^{-1}\mathrm{d}\mathbf{X})$.

**Grille de relecture.** L'indépendance de $C_{ij}$ par rapport à la ligne $i$ est justifiée avant de dériver. L'identité admise sert à passer de la comatrice à l'inverse, avec la transposée au bon endroit. Le cas $\det\mathbf{X} < 0$ est traité. La vérification $2 \times 2$ est faite.

**Variante.** Pour $\mathbf{X}$ symétrique définie positive (une matrice de covariance, M12c), $\nabla\ln\det\mathbf{X} = \mathbf{X}^{-1}$, et $\ln\det\mathbf{X}$ est la somme des logarithmes de ses valeurs propres.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M18.15 — Pont : combien de passages dans chaque mode ?

**Réponses.** a) `[3, 2000]` · b) `[2000, 3]` · c) `[2000, 1]` · d) `1` · e) `1` · f) `8`.

**Démarche.** La jacobienne a une ligne par sortie et une colonne par entrée : $(3, 2\,000)$. Le mode direct en donne une colonne par passe (2 000 passes), le mode inverse une ligne (3 passes arrière, après une seule passe avant) ; pour un seul polluant, une seule ligne : 1 passe arrière. d) Faire augmenter toutes les émissions de 1 %, c'est une seule direction $\mathbf{v} = 0{,}01\,\mathbf{x}$ : une passe directe, de graine $\mathbf{v}$, donne $\mathbf{J}\mathbf{v}$. e) Le gradient de la somme des sorties est le produit vecteur-jacobienne $(1, 1, 1)\,\mathbf{J}$ : une passe arrière, de graine $(1, 1, 1)$. f) $10^6 \times 8$ octets $= 8 \times 10^6$ octets, soit 8 Mo.

Dans ta copie : le mode inverse, de loin. Le chapitre 18 de workbookIA dérive une fonction de très nombreuses entrées et d'une seule sortie : une seule passe arrière lui suffit, au prix de la mémoire de toute la passe avant.

**Erreurs fréquentes.** La forme transposée $(2\,000, 3)$. Répondre 2 000 à d) ou 3 à e) : une seule direction (ou une seule combinaison des sorties) ne demande qu'une passe. Donner f) en octets.

**Variante.** Une simulation de $\mathbb{R}^5$ dans $\mathbb{R}^{1\,000}$ : 5 passes directes contre 1 000 passes arrière pour la jacobienne entière.

### Ex M18.16 — Pont : de la convention de MML à celle de NumPy

**Réponses.** a) `[[7, 13]]` · b) `[2]` · c) `[[3, 4], [1, 12]]` · d) `[0.65, 1.35]` · e) `[5, 3, 2]`.

**Démarche.** $\mathbf{A} + \mathbf{A}^\top = \begin{pmatrix} 2 & 2 \\ 2 & 6 \end{pmatrix}$, $\mathbf{x}^\top(\mathbf{A} + \mathbf{A}^\top) = (6, 14)$, plus $\mathbf{b}^\top$ : $(7, 13)$, en ligne. En colonne, les mêmes nombres. d) $(1, 2) - 0{,}05\,(7, 13) = (0{,}65 ;\ 1{,}35)$.

Dans ta copie : le pas soustrait un multiple du gradient à $\mathbf{x}$ : il faut qu'il ait la forme de $\mathbf{x}$, d'où la transposée de la ligne de MML. La vérification simple : écrire la forme de chaque facteur d'une formule de gradient et contrôler que le résultat a **la forme de la variable** ; une transposée oubliée donne en général une forme impossible (sauf pour une matrice carrée, où il faut un autre contrôle, comme la direction au hasard du §8).

**Erreurs fréquentes.** Oublier $\mathbf{b}$ ($(6, 14)$). Écrire $2\mathbf{A}\mathbf{x}$ alors que $\mathbf{A}$ n'est pas symétrique ($(11, 11)$ avec $\mathbf{b}$).

**Variante.** $\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $\mathbf{b} = \mathbf{0}$, $\mathbf{x} = (1, 1)$ : le gradient vaut $(6, 6)$, en ligne `[[6, 6]]`.

### Ex M18.17 — MML §5.4 et §5.5

**Ce qu'il faut avoir relevé.**
1. La dérivée d'une matrice $m \times n$ par rapport à une matrice $p \times q$ est un tableau à **quatre** indices, de forme $(m \times n) \times (p \times q)$, dont chaque coefficient est la dérivée d'un coefficient de la première par rapport à un coefficient de la seconde. Deux façons de la calculer : dériver coefficient par coefficient et ranger les résultats ; ou **aplatir** les matrices en vecteurs de $mn$ et $pq$ coordonnées, calculer une jacobienne ordinaire $mn \times pq$, puis lui rendre sa forme.
2. Pour une fonction réelle d'une matrice, les identités du §5.5 donnent un gradient de la forme de la matrice (par exemple $\mathbf{a}\mathbf{b}^\top$ pour $\mathbf{a}^\top\mathbf{X}\mathbf{b}$) : la convention de la fiche. Pour une fonction d'un vecteur, le livre garde la ligne.
3. Le §5.5 rassemble des identités sur la transposée, la trace, le déterminant, l'inverse et des formes bilinéaires ou quadratiques. Celle de l'**inverse** n'est pas démontrée dans la fiche : en différentiant $\mathbf{X}\mathbf{X}^{-1} = \mathbf{I}$, $\mathrm{d}\mathbf{X}\,\mathbf{X}^{-1} + \mathbf{X}\,\mathrm{d}(\mathbf{X}^{-1}) = \mathbf{0}$, donc $\mathrm{d}(\mathbf{X}^{-1}) = -\mathbf{X}^{-1}\,\mathrm{d}\mathbf{X}\,\mathbf{X}^{-1}$ ; et pour $f(\mathbf{X}) = \mathbf{a}^\top\mathbf{X}^{-1}\mathbf{b}$, $\mathrm{d}f = -\operatorname{tr}(\mathbf{X}^{-1}\mathbf{b}\mathbf{a}^\top\mathbf{X}^{-1}\mathrm{d}\mathbf{X})$, d'où $\nabla f = -\mathbf{X}^{-\top}\mathbf{a}\mathbf{b}^\top\mathbf{X}^{-\top}$.
4. Ton exemple, refait avec tes nombres et vérifié dans le notebook (par exemple avec `gradient_from_differential`).
5. Par exemple : *gradient of a matrix* (gradient par rapport à une matrice), *tensor* (tableau à plusieurs indices), *reshape* ou *flatten* (aplatir), *trace* (trace), *determinant* (déterminant).

**Grille.** Le tableau à quatre indices et les deux méthodes ; la forme du gradient d'une fonction réelle d'une matrice ; au moins une identité nouvelle démontrée par la différentielle ; un exemple refait ; trois mots traduits.

### Ex M18.18 — MML §5.6

**Ce qu'il faut avoir relevé.**
1. Le livre appelle les nœuds intermédiaires des **variables intermédiaires** (*intermediate variables*) et dessine le **graphe de calcul** (*computation graph*) de son exemple : une fonction d'une seule variable, faite de carrés, d'une exponentielle, d'une racine et d'un cosinus.
2. Le **mode direct** (*forward mode*) suit les données, des entrées vers la sortie ; le **mode inverse** (*reverse mode*) remonte de la sortie vers les entrées. La rétropropagation (*backpropagation*) est le mode inverse appliqué à un réseau.
3. Ton graphe a un nœud par variable intermédiaire du livre, et l'une d'elles sert deux fois : son adjoint reçoit deux contributions, qui s'additionnent. Les adjoints, calculés de la sortie vers l'entrée avec les valeurs de la passe avant, donnent en $\bar{x}$ un nombre qui doit coïncider (à l'arrondi près) avec la dérivée de la formule, calculée directement par la règle de la chaîne de R7 ; vérifie-le aussi avec `dual_derivative` dans le notebook.
4. Chaque dérivée locale réutilise une valeur de la passe avant, et chaque arête ne sert qu'une fois : le gradient coûte un petit multiple du calcul de la fonction, comme le dit le principe du gradient bon marché (§5).
5. Avec $x$ remplacé par ton point plus $\varepsilon$, chaque nœud porte sa tangente (sa dérivée par rapport à $x$) au lieu de son adjoint (la dérivée de la sortie par rapport à lui) ; la partie en $\varepsilon$ de la sortie est la même dérivée qu'en 3. : les deux modes rangent différemment la même somme sur les chemins.
6. Par exemple : *intermediate variable* (variable intermédiaire), *computation graph* (graphe de calcul), *forward mode*, *reverse mode* (modes direct et inverse), *backpropagation* (rétropropagation).

**Grille.** Le vocabulaire des nœuds et du graphe ; le sens de chaque mode ; l'exemple refait par les adjoints et vérifié ; le coût relié au §5 ; la passe duale ; trois mots traduits.

### Ex M18.19 — Expliquer le mode inverse

**Réponse modèle (6 à 10 phrases).** Imagine une rivière qui reçoit des affluents, eux-mêmes alimentés par des ruisseaux, jusqu'à un barrage qui mesure le débit final. Pour chaque point du réseau, on veut savoir de combien le débit au barrage bougerait si le débit en ce point bougeait un peu : c'est son « adjoint ». Au barrage, la réponse est évidente : 1. Pour un affluent, il suffit de savoir quelle part de son eau arrive dans la rivière, et l'adjoint de la rivière : on multiplie, comme dans la règle de la chaîne en une variable. Pour un ruisseau qui se partage entre deux affluents, on additionne ce qui passe par l'un et par l'autre. On remonte ainsi du barrage vers les sources, chaque point ne demandant que les adjoints des points situés en aval, déjà calculés. Pour connaître les parts au bon moment, il faut avoir noté les débits pendant l'aller : c'est la mémoire du calcul. Une seule remontée donne l'adjoint de **toutes** les sources à la fois, alors qu'il faudrait autrement refaire un calcul complet par source.

**En 3 phrases.** On part du résultat et on remonte le calcul, en multipliant le long de chaque étape et en additionnant quand une étape en alimente plusieurs. Il faut avoir gardé les valeurs de l'aller pour connaître chaque petite dérivée. Une seule remontée donne la sensibilité du résultat à toutes les entrées.

**Grille.** L'adjoint comme sensibilité du résultat ; le départ à 1 à la fin ; la multiplication le long d'un chemin et l'addition entre les chemins ; la mémoire de l'aller ; une seule remontée pour toutes les entrées.

<a id="entretien"></a>

## 💼 Entretien

### M18.E1 — « Différentiation automatique, symbolique ou numérique : quelles différences ? »

**Réponse modèle (60 secondes).** « La différentiation symbolique, comme celle de SymPy, manipule des formules : elle applique les règles de dérivation à l'expression et rend une nouvelle expression, exacte, mais qui peut gonfler énormément et ne s'applique pas directement à un programme avec des boucles et des tests. La différentiation numérique approche la dérivée par des différences finies : elle est simple, mais c'est une approximation, dont l'erreur dépend du pas, entre la troncature quand il est grand et les arrondis quand il est petit. La différentiation automatique applique les règles de dérivation aux **nombres**, opération par opération, pendant le calcul : elle rend une dérivée exacte aux arrondis près, même pour un programme avec des boucles. Elle a deux modes : le mode direct, une passe par entrée, et le mode inverse, une passe par sortie, qui doit garder les valeurs de l'aller. Un code qui dérive un seul nombre par rapport à des milliers d'entrées, comme la traînée d'une aile d'avion en fonction des milliers de points qui décrivent sa forme, choisit le mode inverse : une seule passe arrière lui donne toutes les dérivées, pour un petit multiple du coût du calcul. »

**Grille.** Les trois méthodes et ce que chacune rend ; leurs défauts (gonflement, pas $h$, mémoire) ; les deux modes ; la raison du mode inverse pour un seul nombre et beaucoup d'entrées.

### M18.E2 — « Quand le mode direct est-il préférable au mode inverse ? »

**Réponse modèle (60 secondes).** « Pour une fonction de $n$ entrées et $m$ sorties, une passe du mode direct donne une colonne de la jacobienne, les dérivées de toutes les sorties par rapport à une entrée ; une passe du mode inverse en donne une ligne, le gradient d'une sortie. Le mode direct gagne donc quand il y a peu d'entrées et beaucoup de sorties : par exemple, la trajectoire complète d'une sonde, échantillonnée en des milliers d'instants, en fonction de sa seule vitesse de départ, se dérive en une passe directe. Il gagne aussi en mémoire : il ne garde, comme le calcul lui-même, que les valeurs encore utiles, alors que le mode inverse doit garder toute la passe avant, ce qui pèse pour un très long calcul. Et quand on ne veut la dérivée que dans une seule direction, un produit jacobienne-vecteur, une passe directe suffit. Pour un gradient, une seule sortie et beaucoup d'entrées, c'est le mode inverse. »

**Grille.** Colonne contre ligne ; la règle de choix ; un exemple concret de chaque côté ; la mémoire ; le produit jacobienne-vecteur.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

*(résumé à compléter)*
