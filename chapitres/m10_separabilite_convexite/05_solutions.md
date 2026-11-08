# M10 · Séparabilité linéaire et convexité — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M10.Q1 — Convexe ou non ?
1. **Convexe** : un triangle plein est l'intersection de trois demi-plans (fiche §1).
2. **Non convexe** : deux points diamétralement opposés du cercle ont pour milieu le centre, qui n'est pas sur la courbe.
3. **Convexe** : c'est la région au-dessus de la courbe de $|x|$, une fonction convexe ; c'est aussi l'intersection des demi-plans $y \ge x$ et $y \ge -x$.
4. **Non convexe** : c'est la réunion de deux quarts de plan opposés ; $(2, 1)$ et $(-1, -3)$ en font partie, mais pas le milieu $(0{,}5 ;\ -1)$, où $xy < 0$.
5. **Non convexe** : deux points de la droite, de part et d'autre du point retiré, ont un segment qui passe par lui.
6. **Convexe** : c'est une boule de la norme L1, un losange plein (M07).

### M10.Q2 — L'enveloppe convexe : vrai ou faux
1. **Vrai** (une combinaison avec un seul poids égal à 1).
2. **Vrai** : $S$ est alors lui-même le plus petit convexe qui contient $S$.
3. **Faux** : les points intérieurs, et ceux au milieu d'un côté, ne sont pas des sommets.
4. **Faux** : c'est le segment qui joint les deux points extrêmes.
5. **Vrai** : le barycentre est une combinaison convexe, de poids tous égaux à $\frac{1}{n}$.
6. **Faux** : un point ajouté loin du nuage peut faire disparaître plusieurs sommets d'un coup (M10.2 g en fait disparaître un, sans en changer le nombre).

### M10.Q3 — Séparable ou non ?
1. **Oui** : le seuil $x = 3$ sépare $\{1, 2\}$ de $\{4, 7\}$.
2. **Non** : $3$ est dans l'intervalle $[0, 6] = \operatorname{conv}(\{0, 6\})$.
3. **Non** : $(1, 2)$ vérifie $x \ge 0$, $y \ge 0$ et $x + y \le 4$ : il est dans le triangle de la classe $+1$.
4. **Non** : le centre est dans le polygone formé par les huit points du cercle (c'est par exemple le milieu de deux points diamétralement opposés, si les huit points sont régulièrement espacés).
5. **Oui** : $d + 1 = 3$ points en position générale sont séparables quels que soient leurs labels (fiche §3).
6. **Non** : ce point est dans les deux enveloppes ; aucun hyperplan ne peut le mettre des deux côtés.

### M10.Q4 — Marge et astuce du biais
1. La marge géométrique **ne change pas** ; les marges fonctionnelles sont **multipliées par 3**.
2. C'est le même hyperplan, avec les deux côtés échangés : chaque point se retrouve du mauvais côté, et la marge devient **négative** (elle vaut moins le plus grand des $\frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$).
3. $\tilde{\mathbf{x}} = (1, 2, -1)$, $\tilde{\mathbf{w}} = (-3, 1, 4)$, $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}} = -3 + 2 - 4 = -5$, la même valeur que $\mathbf{w} \cdot \mathbf{x} + b$.
4. **Vrai** : $\tilde{\mathbf{w}} \cdot \mathbf{0} = 0$.
5. Le point le plus mal placé est **exactement sur l'hyperplan** : le couple ne sépare pas au sens strict (et aucun point n'est du mauvais côté).
6. **3**, la moitié de la distance entre les enveloppes.

<a id="rappels"></a>

## 🔁 Rappels

### M10.R1 — Hyperplans et distance à un hyperplan (M07)
1. $\mathbf{w} = (2, -1, 2)$ (ou tout multiple non nul), de norme $\sqrt{4 + 1 + 4} = 3$.
2. $\frac{|b|}{\lVert \mathbf{w} \rVert} = \frac{3}{3} = 1$.
3. $\frac{4 - 1 + 2 - 3}{3} = \frac{2}{3}$.
4. **Non** : l'origine donne $-3 < 0$, le point donne $2 > 0$ ; ils sont de part et d'autre.
5. $\mathbf{0} - \frac{-3}{9}(2, -1, 2) = \big(\frac{2}{3}, -\frac{1}{3}, \frac{2}{3}\big)$ ; vérification : $\frac{4}{3} + \frac{1}{3} + \frac{4}{3} - 3 = 0$.

### M10.R2 — L'inégalité de Cauchy-Schwarz (M07)
1. $|\mathbf{u} \cdot \mathbf{v}| \le \lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert$.
2. $\mathbf{u} \cdot \mathbf{v} = 6 + 0 - 8 = -2$, $\lVert \mathbf{u} \rVert = 5$, $\lVert \mathbf{v} \rVert = 3$ : $2 \le 15$.
3. Quand $\mathbf{u}$ et $\mathbf{v}$ sont colinéaires (l'un est un multiple de l'autre).
4. $\mathbf{e} \cdot \mathbf{v} \le |\mathbf{e} \cdot \mathbf{v}| \le \lVert \mathbf{e} \rVert\,\lVert \mathbf{v} \rVert = \lVert \mathbf{v} \rVert$ ; égalité pour $\mathbf{e} = \frac{\mathbf{v}}{\lVert \mathbf{v} \rVert}$ (si $\mathbf{v} \ne \mathbf{0}$).
5. $3a + 4c = (3, 0, 4) \cdot (a, b, c) \le 5 \times 2 = \mathbf{10}$, atteint pour $(a, b, c) = \frac{2}{5}(3, 0, 4) = (1{,}2 ;\ 0 ;\ 1{,}6)$.

### M10.R3 — La sigmoïde et tanh (R6)
1. $\sigma(0) = \frac{1}{2}$ ; $\sigma(z) \to 0$ en $-\infty$ et $\to 1$ en $+\infty$.
2. $\sigma(-z) = \frac{1}{1 + e^{z}} = \frac{e^{-z}}{e^{-z} + 1} = 1 - \frac{1}{1 + e^{-z}} = 1 - \sigma(z)$.
3. $\sigma(\ln 3) = \frac{1}{1 + \frac{1}{3}} = \frac{3}{4}$.
4. $\tanh\big(\frac{\ln 3}{2}\big) = 2\sigma(\ln 3) - 1 = \frac{1}{2}$.
5. $\sigma(u) = \frac{1}{2}$ si et seulement si $u = 0$ : $2x - 1 = 0$, $x = \frac{1}{2}$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M10.1 — Convexe ou non : segments, demi-plans, intersections

**Réponses** : a) `[-1, 1]` · b) `0.75` · c) `"ACEF"` · d) `[3, 2]` · e) `4` · f) `"PS"` · g) `[2.9, 1.3]`.

**Démarche.**
- a) $\mathbf{b} - \mathbf{a} = (8, -4)$, et $\mathbf{a} + 0{,}25\,(8, -4) = (-3 + 2,\ 2 - 1) = (-1, 1)$.
- b) $(-3 + 8t,\ 2 - 4t) = (3, -1)$ donne $t = 0{,}75$ par les deux coordonnées (si elles donnaient deux $t$ différents, le point ne serait pas sur la droite).
- c) $A$ est une boule, $C$ la région au-dessus de la courbe convexe $x^2$, $E$ une boule d'une norme (un losange), $F$ la région au-dessus de la courbe de $\frac{1}{x}$, convexe sur $]0, +\infty[$. $B$ a un trou : $(-1, 0)$ et $(1, 0)$ en font partie, pas leur milieu. $D$ : $(-1, 1)$ et $(1, 1)$ en font partie, pas $(0, 1)$. $G$ : $(3, 0)$ et $(0, 3)$ en font partie, pas $(1{,}5 ;\ 1{,}5)$.
- d) $2x + y = 8$ et $x + 2y = 7$ : en retranchant deux fois la seconde de la première, $-3y = -6$, $y = 2$, puis $x = 3$. Ce point vérifie bien $x \ge 0$ et $y \ge 0$.
- e) Les sommets sont $(0, 0)$, $(4, 0)$, $(3, 2)$ et $(0 ;\ 3{,}5)$ : chacun est l'intersection de deux des quatre droites, et vérifie les deux autres inégalités.
- f) $P$ : $7 \le 8$ et $6{,}5 \le 7$. $Q$ : $1 + 6{,}4 = 7{,}4 > 7$. $R$ : $7{,}6 + 0{,}5 = 8{,}1 > 8$. $S$ : $0 + 7 = 7$, sur le bord, donc dans $K$ (les inégalités sont larges).
- g) $(2 + 0{,}9 + 0,\ 0 + 0{,}6 + 0{,}7) = (2{,}9 ;\ 1{,}3)$.

Pour la copie : le point de g) est une combinaison convexe de trois sommets de $K$, qui est convexe : il est dans $K$ (fiche §1), ce que confirment $2 \times 2{,}9 + 1{,}3 = 7{,}1 \le 8$ et $2{,}9 + 2{,}6 = 5{,}5 \le 7$.

**Erreurs fréquentes.** En a), partir de $\mathbf{b}$ au lieu de $\mathbf{a}$ (on obtient $(3, -1)$, le point de b) ; en c), garder $G$ (« deux bandes convexes ») ou rejeter $F$ ; en f), exclure $S$, qui est sur le bord.

**Variante.** Le point de $[\mathbf{a}, \mathbf{b}]$ pour $t = 0{,}6$ ? *Réponse* : $(-3 + 4{,}8 ;\ 2 - 2{,}4) = (1{,}8 ;\ -0{,}4)$.

### Ex M10.2 — L'enveloppe convexe de huit points, à la main

**Réponses** : a) `5` · b) `[[-3, 1], [0, -2], [5, 0], [4, 3], [3, 5]]` · c) `7` · d) `1` · e) `30` · f) `False` · g) `5`.

**Démarche.** Trié : $P_3 = (-3, 1)$, $P_7 = (-2, 0)$, $P_2 = (-1, 2)$, $P_8 = (0, -2)$, $P_5 = (3, 3)$, $P_1 = (3, 5)$, $P_6 = (4, 3)$, $P_4 = (5, 0)$. La chaîne du bas :
- $P_2$ : $(1, -1) \times (2, 1) = 3 > 0$, garder ; puis $P_8$ : $(1, 2) \times (2, -2) = -6$, retirer $P_2$, et $(1, -1) \times (3, -3) = 0$, retirer $P_7$ (aligné : au milieu du côté $P_3P_8$) ;
- $P_5$ et $P_1$ entrent ; $P_6$ les fait sortir ($-2$, puis $-5$) ; $P_4$ fait sortir $P_6$ ($-17$) ; la chaîne du bas est $P_3$, $P_8$, $P_4$.

La chaîne du haut, de droite à gauche, finit en $P_4$, $P_6$, $P_1$, $P_3$. Bout à bout : $(-3, 1)$, $(0, -2)$, $(5, 0)$, $(4, 3)$, $(3, 5)$.
- c) $P_7$ : $(P_8 - P_3) \times (P_7 - P_3) = (3, -3) \times (1, -1) = -3 + 3 = 0$, et $P_7$ est entre $P_3$ et $P_8$.
- d) $(P_6 - P_4) \times (P_1 - P_4) = (-1, 3) \times (-2, 5) = -5 + 6 = 1 > 0$ : le chemin $P_4 \to P_6 \to P_1$ tourne à gauche, de justesse ; $P_6$ est bien un sommet.
- e) Depuis $P_3$ : $(3, -3) \times (8, -1) = 21$, $(8, -1) \times (7, 2) = 23$, $(7, 2) \times (6, 4) = 16$ ; aire $\frac{21 + 23 + 16}{2} = 30$.
- f) Pour le côté $P_6 \to P_1$ : $(-1, 2) \times (Q - P_6) = (-1, 2) \times (0, 1) = -1 < 0$ : $Q$ est à droite de ce côté, donc dehors.
- g) Avec $Q$, le chemin $P_4 \to P_6 \to Q$ donne $(-1, 3) \times (-1, 4) = -4 + 3 = -1 < 0$ : $P_6$ cesse d'être un sommet. Les sommets deviennent $(-3, 1)$, $(0, -2)$, $(5, 0)$, $(4, 4)$, $(3, 5)$ : toujours 5.

Pour la copie : le signe de d) dit que $P_6$ dépasse (de peu) la droite $P_4P_1$ ; un point ajouté au-dessus de lui le fait rentrer à l'intérieur.

**Erreurs fréquentes.** Compter $P_7$ comme un sommet (6 sommets) ; tourner dans le sens des aiguilles d'une montre ; oublier de diviser par 2 l'aire des triangles (60) ; en g), ajouter un sommet sans vérifier que les autres le restent.

**Variante.** Le nombre de sommets si l'on ajoute plutôt $(-4, 4)$ ? *Réponse* : 6 ; $(-4, 4)$ devient le plus petit point, et tous les anciens sommets le restent.

### Ex M10.3 — Une droite qui sépare deux petits nuages, et sa marge

**Réponses** : a) `[16, 15, 8, -2, -5, -2]` · b) `0.8944` · c) `[4, 6]` · d) `"]-12 ; -2["` · e) `-7` · f) `2.2361` · g) `2.5`.

**Démarche.**
- a) $\mathbf{w} \cdot P_i = 2x_1 + x_2$ vaut $20, 19, 12$ sur la classe $+1$ et $2, -1, 2$ sur la classe $-1$ ; on retranche 4.
- b) Les $y_i(\mathbf{w} \cdot P_i + b)$ valent $16, 15, 8, 2, 5, 2$ : le minimum est 2, et $\frac{2}{\sqrt{5}} \approx 0{,}8944$.
- c) $P_4$ et $P_6$, de marge fonctionnelle 2 tous les deux.
- d) Il faut $12 + b > 0$ (le plus petit $\mathbf{w} \cdot \mathbf{x}$ de la classe $+1$) et $2 + b < 0$ (le plus grand de la classe $-1$) : $b \in\ ]-12, -2[$.
- e) Le milieu, $b = -7$ : la droite est à égale distance des deux nuages.
- f) Les marges fonctionnelles valent alors $12 - 7 = 5$ et $-2 + 7 = 5$ : $\frac{5}{\sqrt{5}} = \sqrt{5} \approx 2{,}2361$.
- g) Les deux enveloppes sont les triangles $P_1P_2P_3$ et $P_4P_5P_6$. Le couple de points le plus proche est $P_3 = (3, 6)$ et $P_4 = (0, 2)$, à la distance $\lVert (3, 4) \rVert = 5$ : la plus grande marge vaut $2{,}5$.

Pour la copie : la droite de plus grande marge est la médiatrice de $[P_4, P_3]$, de normale $(3, 4)$, qui passe par le milieu $(1{,}5 ;\ 4)$ : $3x_1 + 4x_2 - 20{,}5 = 0$. Ses marges fonctionnelles valent $24{,}5$ ; $20{,}5$ ; $12{,}5$ sur la classe $+1$ et $12{,}5$ ; $14{,}5$ ; $17{,}5$ sur l'autre : le minimum, $12{,}5$, divisé par 5, redonne $2{,}5$. Il faut vérifier que les autres couples sont plus loin : $P_3$ et le côté $P_4P_5$, par exemple, ou $P_2$ et $P_6$.

**Erreurs fréquentes.** Oublier $b$ dans les scores ; diviser par $\lVert \mathbf{w} \rVert^2 = 5$ au lieu de $\sqrt{5}$ ; prendre la marge sur une seule classe ; un intervalle fermé en d) (aux bornes, un point est sur la droite) ; en g), répondre $\sqrt{5}$, la meilleure marge pour la seule direction $(2, 1)$.

**Variante.** Avec $\mathbf{w} = (1, 1)$, l'intervalle des $b$ qui séparent, et la meilleure marge ? *Réponse* : le plus petit $x_1 + x_2$ de la classe $+1$ vaut 9, le plus grand de la classe $-1$ vaut 2 ; $b \in\ ]-9, -2[$, et $b = -5{,}5$ donne $\frac{3{,}5}{\sqrt{2}} \approx 2{,}4749$, mieux que $(2, 1)$ mais moins que $2{,}5$.

### Ex M10.4 — L'astuce du biais : une droite du plan devient un plan de ℝ³ passant par l'origine

**Réponses** : a) `[4, 3, -2]` · b) `[1, 1, 2]` · c) `[3, -4, -2]` · d) `1.1094` · e) `[3, 2]` · f) `True` · g) `[-2, 1, 2]`.

**Démarche.**
- a) et b) Le biais, puis les poids ; la coordonnée 1, puis le point.
- c) $4 + 3 - 4 = 3$ ; $4 - 6 - 2 = -4$ ; $4 + 0 - 6 = -2$ : exactement les $\mathbf{w} \cdot \mathbf{x} + b$.
- d) $\frac{|-4|}{\lVert (3, -2) \rVert} = \frac{4}{\sqrt{13}} \approx 1{,}1094$.
- e) Au niveau 1, $-6 + 2x_1 + 3x_2 = 0$ : $x_1 = 3$ quand $x_2 = 0$, et $x_2 = 2$ quand $x_1 = 0$.
- f) Au niveau 1, l'équation devient $v_1x_1 + v_2x_2 = 0$, une droite qui passe par $(0, 0)$.
- g) $\tilde{\mathbf{u}} \cdot (1, 2, 0) = -2 + 2u_1 = 0$ donne $u_1 = 1$ ; $\tilde{\mathbf{u}} \cdot (1, 0, 1) = -2 + u_2 = 0$ donne $u_2 = 2$ : c'est la droite $x_1 + 2x_2 - 2 = 0$, qui passe bien par $(2, 0)$ et $(0, 1)$.

Pour la copie : $\mathbf{p}$ est du côté positif de $\Delta$, $\mathbf{q}$ et $\mathbf{r}$ du côté négatif. Pour un point du plan, $\tilde{\mathbf{v}} \cdot (1, x_1, x_2) = -6 + 2x_1 + 3x_2$ : il est nul exactement sur la droite $2x_1 + 3x_2 = 6$. Le biais est la seule chose qui écarte une droite de l'origine : avec $v_0 = 0$, il n'y en a plus.

**Erreurs fréquentes.** Le biais ou la coordonnée 1 à la fin (`[3, -2, 4]`, `[1, 2, 1]`) : la convention de l'énoncé, celle de la fiche, les place en tête ; oublier le terme $b \times 1$ dans le score ; en d), diviser par la norme de $\tilde{\mathbf{w}}$ (dans $\mathbb{R}^3$) au lieu de celle de $\mathbf{w}$.

**Variante.** Le vecteur $\tilde{\mathbf{u}}$, de première coordonnée $-1$, d'un plan par l'origine qui contient les points relevés de $(1, 0)$ et de $(0, 1)$ ? *Réponse* : $(-1, 1, 1)$, la droite $x_1 + x_2 = 1$.

### Ex M10.5 — Borner une norme pas à pas : ‖v_{k+1}‖² ≤ ‖v_k‖² + c

**Réponses** : a) `5` · b) `-1` · c) `13` · d) `15` · e) `22.47` · f) `44` · g) `11`.

**Démarche.**
- a) $1 + 4 = 5$.
- b) $\mathbf{v}_1 = (3, 1)$, et $(3, 1) \cdot (-1, 2) = -3 + 2 = -1$.
- c) $\mathbf{v}_2 = (2, 3)$, de carré de norme 13 ; ou bien $\lVert \mathbf{v}_1 \rVert^2 + 2\,\mathbf{v}_1 \cdot \mathbf{d}_1 + \lVert \mathbf{d}_1 \rVert^2 = 10 - 2 + 5 = 13$.
- d) Le lemme avec $c = 5$ : $\lVert \mathbf{v}_2 \rVert^2 \le 5 + 2 \times 5 = 15$.
- e) $\lVert \mathbf{v}_{100} \rVert^2 \le 5 + 100 \times 5 = 505$, donc $\lVert \mathbf{v}_{100} \rVert \le \sqrt{505} \approx 22{,}47$.
- f) La progression : $\mathbf{e} \cdot \mathbf{v}_k \ge -2 + 0{,}5k$. La norme : $\lVert \mathbf{v}_k \rVert^2 \le 4 + 9k$. Cauchy-Schwarz : $\mathbf{e} \cdot \mathbf{v}_k \le \lVert \mathbf{v}_k \rVert$. Pour $k \ge 4$, $-2 + 0{,}5k \ge 0$, et l'on peut élever au carré : $0{,}25k^2 - 2k + 4 \le 4 + 9k$, soit $0{,}25k^2 \le 11k$, soit $k \le 44$. Au plus 44 pas.
- g) $\mathbf{v}_{k+1} = \mathbf{v}_k\big(1 + \frac{1}{\lVert \mathbf{v}_k \rVert}\big)$ : la norme gagne exactement 1 à chaque pas, $\lVert \mathbf{v}_{10} \rVert = 1 + 10 = 11$.

Pour la copie : $\mathbf{v}_0 \cdot \mathbf{d}_0 = 2 - 2 = 0$ et $\lVert \mathbf{v}_1 \rVert^2 = 5 + 0 + 5 = 10$ : la borne est atteinte au premier pas, perpendiculaire, mais pas au second, où le terme $2\,\mathbf{v}_1 \cdot \mathbf{d}_1 = -2$ est strictement négatif. En g), $\mathbf{v}_k \cdot \mathbf{d}_k = \lVert \mathbf{v}_k \rVert > 0$ : l'hypothèse du lemme n'est pas vérifiée, et la norme croît linéairement, bien au-delà de $\sqrt{1 + 10} \approx 3{,}3$.

**Erreurs fréquentes.** En c), donner la borne au lieu de la valeur exacte ; en e), oublier $\lVert \mathbf{v}_0 \rVert^2$ ou la racine ; en f), partir de $\mathbf{e} \cdot \mathbf{v}_0 = 0$ (on trouve 36) ou oublier $\lVert \mathbf{v}_0 \rVert^2 = 4$ (on trouve 52) ; élever au carré une inégalité dont un côté peut être négatif.

**Variante.** Avec les hypothèses de e), une borne de $\lVert \mathbf{v}_{20} \rVert$ ? *Réponse* : $\sqrt{5 + 100} = \sqrt{105} \approx 10{,}25$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M10.6 — Un demi-espace est convexe, et une intersection de convexes aussi

**Réponse modèle.**
1. $s\big((1 - t)\mathbf{a} + t\mathbf{b}\big) = (1 - t)\,\mathbf{w} \cdot \mathbf{a} + t\,\mathbf{w} \cdot \mathbf{b} + b = (1 - t)(\mathbf{w} \cdot \mathbf{a} + b) + t(\mathbf{w} \cdot \mathbf{b} + b)$, en écrivant $b = (1 - t)b + tb$.
2. Si $s(\mathbf{a}) \ge 0$ et $s(\mathbf{b}) \ge 0$, alors, pour $t \in [0, 1]$, $1 - t \ge 0$ et $t \ge 0$, donc $s\big((1 - t)\mathbf{a} + t\mathbf{b}\big) \ge 0$ : le segment reste dans le demi-espace. Pour l'inégalité stricte, l'un des deux poids est strictement positif, et l'on obtient $> 0$.
3. Si $\mathbf{a}, \mathbf{b} \in C_1 \cap C_2$, le segment est dans $C_1$ (convexe) et dans $C_2$ (convexe), donc dans l'intersection. Par récurrence : $C_1 \cap \cdots \cap C_{m+1} = (C_1 \cap \cdots \cap C_m) \cap C_{m+1}$, intersection de deux convexes.
4. $|x| \le 1$ et $|y| \le 1$ équivalent à $x \le 1$, $-x \le 1$, $y \le 1$, $-y \le 1$ : quatre demi-plans fermés, donc une intersection de convexes.
5. Les points étant fixés, $(\mathbf{w}, b) \mapsto y_i(\mathbf{w} \cdot \mathbf{x}_i + b) - 1$ est une fonction affine des paramètres : chaque contrainte définit un demi-espace de $\mathbb{R}^{d+1}$, et l'ensemble des séparateurs est leur intersection (éventuellement vide).
6. Les demi-plans $x \ge 1$ et $y \ge 1$ : $(2, -2)$ est dans le premier, $(-2, 2)$ dans le second, et leur milieu $(0, 0)$ n'est dans aucun des deux. (Avec $x \ge 0$ et $y \ge 0$, ce milieu serait dans la réunion : un contre-exemple se vérifie.)

**Grille.** (1) l'identité affine, avec le $b$ réparti ; (2) les poids positifs, et le cas strict ; (3) l'intersection, puis la récurrence ; (4) le carré écrit avec quatre inégalités linéaires ; (5) la remarque que les contraintes sont affines **en les paramètres** ; (6) un contre-exemple vérifié (le milieu doit vraiment sortir des deux demi-plans).

### Ex M10.7 — Deux nuages séparés par un hyperplan ont des enveloppes convexes disjointes

**Réponse modèle.**
1. $\sum_i t_i s(\mathbf{x}_i) = \mathbf{w} \cdot \sum_i t_i\mathbf{x}_i + b\sum_i t_i = s\big(\sum_i t_i\mathbf{x}_i\big)$, la dernière égalité parce que $\sum_i t_i = 1$ (sinon le terme constant serait $b\sum_i t_i \ne b$).
2. Pour $\mathbf{p} = \sum_i t_i\mathbf{a}_i \in \operatorname{conv}(A)$ : $s(\mathbf{p}) = \sum_i t_i s(\mathbf{a}_i)$, une somme de termes $\ge 0$ (car $t_i \ge 0$ et $s(\mathbf{a}_i) > 0$), dont un au moins est $> 0$ (les $t_i$ ne sont pas tous nuls). Donc $s(\mathbf{p}) > 0$. De même $s < 0$ sur $\operatorname{conv}(B)$.
3. Un point commun aurait un score à la fois $> 0$ et $< 0$ : impossible.
4. Contraposée : **si les enveloppes convexes ont un point commun, aucun hyperplan ne sépare $A$ et $B$.** Avec $t_1(0, 0) + t_2(6, 0) + t_3(2, 6) = (2, 2)$ : $6t_3 = 2$ donne $t_3 = \frac{1}{3}$ ; $6t_2 + 2t_3 = 2$ donne $t_2 = \frac{2}{9}$ ; $t_1 = 1 - \frac{1}{3} - \frac{2}{9} = \frac{4}{9}$. Ces poids sont positifs, de somme 1 : $(2, 2) \in \operatorname{conv}(A) \cap \operatorname{conv}(B)$, et les deux nuages ne sont pas séparables.
5. Un barycentre est une combinaison convexe (poids $\frac{1}{n}$) : celui de $A$ est dans $\operatorname{conv}(A)$, où $s > 0$ ; celui de $B$ dans $\operatorname{conv}(B)$, où $s < 0$.
6. $\operatorname{conv}(A) = [\min A, \max A]$ et $\operatorname{conv}(B) = [\min B, \max B]$. Disjoints : l'un est entièrement à gauche de l'autre, disons $\max A < \min B$. Avec $c = \frac{\max A + \min B}{2}$, $w = -1$ et $b = c$ : $-x + c > 0$ sur $A$ et $< 0$ sur $B$.

**Grille.** (1) le calcul et l'usage de $\sum t_i = 1$ ; (2) le signe d'une combinaison à poids positifs, avec la stricte positivité ; (3) la conclusion ; (4) la contraposée bien formulée, des poids explicites, positifs, de somme 1 ; (5) le barycentre comme combinaison convexe ; (6) un séparateur explicite et vérifié en dimension 1.

### Ex M10.8 — La marge géométrique ne change pas quand on multiplie (w, b) par un réel positif

**Réponse modèle.**
1. $\frac{y_i(c\mathbf{w} \cdot \mathbf{x}_i + cb)}{\lVert c\mathbf{w} \rVert} = \frac{c\,y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{c\,\lVert \mathbf{w} \rVert}$ car $c > 0$ ; chaque terme est inchangé, donc le minimum aussi.
2. $\gamma(-\mathbf{w}, -b) = \min_i \frac{-y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert} = -\max_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$. Si $(\mathbf{w}, b)$ sépare, tous les $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ sont $> 0$, leur maximum aussi, et $\gamma(-\mathbf{w}, -b) < 0$.
3. Elles sont multipliées par $c$. Si $(\mathbf{w}, b)$ sépare, $m = \min_i y_i(\mathbf{w} \cdot \mathbf{x}_i + b) > 0$ ; avec $c = \frac{1}{m}$, le nouveau minimum vaut 1, et l'hyperplan (comme la marge géométrique, par 1) n'a pas changé.
4. $\gamma = \min_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert} = \frac{1}{\lVert \mathbf{w} \rVert}\min_i y_i(\mathbf{w} \cdot \mathbf{x}_i + b) = \frac{1}{\lVert \mathbf{w} \rVert}$. Tout séparateur a une forme canonique, de même marge ; les formes canoniques sont exactement les couples qui vérifient les contraintes avec au moins une égalité. Pour un couple qui vérifie les contraintes $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$, la marge vaut au moins $\frac{1}{\lVert \mathbf{w} \rVert}$, avec égalité pour une forme canonique : la plus grande marge est donc $\frac{1}{\min \lVert \mathbf{w} \rVert}$, le minimum portant sur les couples qui vérifient les contraintes.
5. Un minimum pris sur un terme de plus est plus petit ou égal. Il ne change pas si et seulement si $\frac{y(\mathbf{w} \cdot \mathbf{x} + b)}{\lVert \mathbf{w} \rVert} \ge \gamma(\mathbf{w}, b)$ pour le nouvel exemple : il est du bon côté, au moins aussi loin que le plus mal placé.

**Grille.** (1) la simplification par $c > 0$ (et pourquoi $c < 0$ ne marche pas) ; (2) le minimum d'opposés comme opposé du maximum, puis le signe ; (3) la remise à l'échelle par la plus petite marge fonctionnelle ; (4) $\gamma = \frac{1}{\lVert \mathbf{w} \rVert}$ et l'équivalence avec le problème de minimisation ; (5) l'argument « minimum sur plus de termes », et la condition.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M10.9 — Pont : seuil, sigmoïde, tanh et ReLU appliqués à un même score linéaire

**Réponses** : a) `[0, 2.5, -2]` · b) `[0, 1, 0]` · c) `[0.5, 0.9241, 0.1192]` · d) `[0.0, 0.9866, -0.964]` · e) `[0, 2.5, 0]` · f) `1.3863` · g) `0.62`.

**Démarche.**
- a) $-1{,}5 + 1 + 0{,}5 = 0$ ; $0 + 2 + 0{,}5 = 2{,}5$ ; $-3 + 0{,}5 + 0{,}5 = -2$.
- b) $H(0) = 0$ (le seuil exige $z > 0$), $H(2{,}5) = 1$, $H(-2) = 0$.
- c) $\sigma(0) = 0{,}5$, $\sigma(2{,}5) = \frac{1}{1 + e^{-2{,}5}} \approx 0{,}9241$, $\sigma(-2) = 1 - \sigma(2) \approx 0{,}1192$.
- d) $\tanh(0) = 0$, $\tanh(2{,}5) \approx 0{,}9866$, $\tanh(-2) \approx -0{,}9640$ ; ou $2\sigma(2z) - 1$.
- e) $\max(0, z)$ : $0$, $2{,}5$, $0$.
- f) $1 + e^{-z} = \frac{1}{0{,}8} = 1{,}25$, $e^{-z} = 0{,}25$, $z = \ln 4 \approx 1{,}3863$.
- g) La ligne de niveau est la droite $\mathbf{w} \cdot \mathbf{x} + b = \ln 4$, à la distance $\frac{\ln 4}{\lVert \mathbf{w} \rVert} = \frac{1{,}3863}{\sqrt{5}} \approx 0{,}6200$ de la frontière.

Pour la copie : la sortie ne dépend que du score, et $\{\mathbf{x} : \mathbf{w} \cdot \mathbf{x} + b = c\}$ est une droite parallèle à la frontière (même normale $\mathbf{w}$). En $\mathbf{p}_1$, sur la frontière, les sorties valent $0$, $0{,}5$, $0$ et $0$ ; un seuil qui donnerait 1 en $z = 0$ (convention $z \ge 0$) répondrait autrement. La région « sortie $> \frac{1}{2}$ » est le demi-plan $z > 0$ pour la sigmoïde ; pour le seuil, c'est aussi $z > 0$ ; pour tanh, c'est $z > \operatorname{artanh}(0{,}5) \approx 0{,}55$ (le niveau neutre de tanh est 0, pas $\frac{1}{2}$) ; pour ReLU, $z > \frac{1}{2}$.

**Erreurs fréquentes.** Oublier $b$ dans les scores ; $H(0) = 1$ ; $\tanh(z) = 2\sigma(z) - 1$ (le facteur 2 dans l'argument manque) ; en g), oublier de diviser par $\lVert \mathbf{w} \rVert$.

**Variante.** Le score pour lequel $\tanh(z) = 0{,}5$ ? *Réponse* : $z = \frac{1}{2}\ln 3 \approx 0{,}5493$ (par R3 de ce chapitre : $\tanh(z) = 2\sigma(2z) - 1 = 0{,}5$ donne $\sigma(2z) = \frac{3}{4}$, donc $2z = \ln 3$).

### Ex M10.10 — MML §12.1 : les hyperplans séparateurs, en anglais

**Réponse attendue** (avec tes mots).
1. La **classification binaire** : prédire, pour chaque exemple, l'une de deux classes. Les labels valent $+1$ (exemples « positifs ») et $-1$ (« négatifs »). Ce choix permet d'écrire « bien classé » en une seule condition, le produit du label par le score positif.
2. Une fonction affine $f(\mathbf{x}) = \langle \mathbf{w}, \mathbf{x} \rangle + b$, avec $\mathbf{w} \in \mathbb{R}^D$ et $b \in \mathbb{R}$ ; dans la fiche, $\mathbf{w} \cdot \mathbf{x} + b$. L'hyperplan est l'ensemble des $\mathbf{x}$ où $f$ s'annule.
3. Pour deux points $\mathbf{x}_a$ et $\mathbf{x}_b$ de l'hyperplan, $f(\mathbf{x}_a) - f(\mathbf{x}_b) = \langle \mathbf{w}, \mathbf{x}_a - \mathbf{x}_b \rangle = 0$ : $\mathbf{w}$ est orthogonal à tout vecteur de l'hyperplan. Avec $(1, 3)$ et $(-1, -2)$, sur $5x_1 - 2x_2 + 1 = 0$ : la différence $(2, 5)$ vérifie $(5, -2) \cdot (2, 5) = 10 - 10 = 0$.
4. Les exemples positifs du côté où $f \ge 0$, les négatifs du côté où $f < 0$, ce que le livre réunit en $y_n(\langle \mathbf{w}, \mathbf{x}_n \rangle + b) \ge 0$ : une inégalité **large**. Un exemple posé exactement sur l'hyperplan y est donc accepté (et, à la prédiction, un point où $f = 0$ est rangé du côté $+1$). La fiche exige une inégalité stricte, puis une marge de 1 : c'est ce qui donne un test de séparabilité qui a un sens (M10.13), et la marge du §12.2.
5. L'hyperplan dans l'espace et vu de dessus, avec le vecteur $\mathbf{w}$ perpendiculaire à lui et qui pointe vers le côté positif.
6. Par exemple : *binary classification* (classification binaire), *separating hyperplane* (hyperplan séparateur), *orthogonal* (orthogonal), *training example* (exemple d'entraînement), *intercept* (le biais, appelé aussi ordonnée à l'origine).

**Grille.** (1) les labels $\pm 1$ et leur intérêt ; (2) la fonction affine traduite ; (3) l'argument des deux points refait avec des nombres ; (4) l'inégalité large du livre, comparée à la séparation stricte et à la marge de la fiche ; (5) la figure décrite ; (6) trois termes traduits ; rien de recopié.

### Ex M10.11 — Expliquer la convexité et l'enveloppe convexe avec un élastique

**Réponse modèle.**

> Une forme est convexe quand on peut aller en ligne droite de n'importe quel point à n'importe quel autre sans en sortir : une assiette, une pièce de monnaie ; un croissant ou un anneau ne le sont pas, car la ligne droite traverse le creux. Plante des clous dans une planche, puis lâche un élastique tendu autour de tous : il se resserre et ne touche que les clous « du bord ». La forme qu'il entoure est la plus petite forme convexe qui contient tous les clous : leur enveloppe convexe. Prends maintenant des clous rouges et des clous bleus, avec un élastique autour de chaque couleur. Si les deux élastiques se touchent ou se croisent, un même morceau de planche est entouré par les deux ; une règle posée à plat, qui laisse les rouges d'un côté et les bleus de l'autre, devrait laisser ce morceau des deux côtés à la fois : c'est impossible. Si les élastiques sont séparés, on peut glisser la règle entre eux.

**Grille.** (1) la ligne droite qui ne sort pas, un exemple et un contre-exemple ; (2) l'élastique et les clous qu'il touche ; (3) le plus petit convexe ; (4) deux élastiques qui se croisent, donc pas de règle droite, avec la raison ; (5) huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M10.E1 — « Que veut dire « linéairement séparable », et comment le vérifier ? »

**Réponse modèle (60 secondes).**

> Deux classes sont linéairement séparables s'il existe un hyperplan, une droite en dimension 2, qui laisse toute une classe d'un côté et toute l'autre de l'autre : un $\mathbf{w}$ et un $b$ avec $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) > 0$ pour chaque exemple. Géométriquement, c'est équivalent à : les enveloppes convexes des deux classes ne se touchent pas ; un seul point commun suffit à prouver qu'aucun classifieur linéaire ne fera zéro erreur. Pour le vérifier, on écrit un programme linéaire de faisabilité : existe-t-il $(\mathbf{w}, b)$ avec $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ ? Le « 1 » compte : avec « $\ge 0$ », la solution nulle passerait toujours. Un SVM à marge dure qui atteint 100 % sur l'entraînement le prouve aussi, avec en prime la plus grande marge. Attention à la dimension : avec $n \le d + 1$ points en position générale, n'importe quels labels sont séparables, et vers $n = 2(d + 1)$, des labels tirés au hasard le sont encore une fois sur deux. Donc séparer parfaitement l'entraînement ne garantit rien sur de nouvelles données : il faut une marge, assez de données, et une évaluation sur un jeu de test.

**Grille.** (1) la définition, avec l'inégalité stricte ; (2) le critère des enveloppes convexes ; (3) un test effectif (programme linéaire, avec le « $\ge 1$ » et sa raison ; ou un SVM à marge dure) ; (4) la grande dimension : $d + 1$ points toujours séparables, $2(d + 1)$ comme capacité ; (5) la mise en garde sur la généralisation.

<a id="notebook"></a>

## Notebook

### Ex M10.12 — L'enveloppe convexe dans le plan : la chaîne monotone d'Andrew · `convex_hull_2d`

**Réponses** : a) `[[-1.0, 3.0], [0.0, 0.0], [2.0, -1.0], [6.0, 0.0], [7.0, 4.0], [3.0, 6.0]]` · b) `11` · c) `[[-2.0, 3.0], [4.0, -3.0]]` · d) `"ValueError"` · e) `"ValueError"` · f) `"ndarray"`.

**Démarche.** `P = np.array(points, dtype=float)` (une copie), une `ValueError` si `P.ndim != 2`, si `P.shape[1] != 2` ou si `P` est vide ; `pts = np.unique(P, axis=0)` (les points distincts, triés par $x$ puis par $y$) ; un seul point distinct : le rendre tel quel. Une fonction `half(sequence)` construit une demi-chaîne : pour chaque point `p`, `while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0: chain.pop()`, puis `chain.append(p)`. Enfin `lower, upper = half(pts), half(pts[::-1])` et `np.array(lower[:-1] + upper[:-1], dtype=float)`. Pour la copie : $(4 ;\ -0{,}5)$ est au milieu du côté qui joint $(2, -1)$ à $(6, 0)$ ; le test $\le 0$ l'écarte (produit vectoriel nul) ; avec $< 0$, il resterait comme un faux sommet.

**Erreurs fréquentes.** Le test `< 0` (des points alignés restent) ; le signe du produit vectoriel inversé (sens des aiguilles d'une montre) ; trier par $x$ seulement (un mauvais premier sommet quand plusieurs points ont le plus petit $x$) ; `lower + upper` (les extrémités répétées) ; rendre une liste de tuples ; oublier le cas d'un seul point distinct.

### Ex M10.13 — Séparabilité par programmation linéaire, et marge géométrique · `is_linearly_separable, margin_of_separator`

**Réponses** : a) `True` · b) `False` · c) `False` · d) `1.4142` · e) `-4.9497` · f) `"ValueError"` · g) `"ValueError"` · h) `True`.

**Démarche.** `is_linearly_separable` : `X` en tableau 2-D, `y` en tableau d'une valeur par ligne, une `ValueError` si un label n'est ni $-1$ ni $+1$ (`np.all((y == 1) | (y == -1))`) ; puis `A_ub = -y[:, None] * np.hstack([X, np.ones((n, 1))])` (une ligne $(-y_i\mathbf{x}_i, -y_i)$ par point), `res = linprog(np.zeros(d + 1), A_ub=A_ub, b_ub=-np.ones(n), bounds=(None, None), method="highs")` et `return bool(res.status == 0)`. `margin_of_separator` : les mêmes contrôles, plus la longueur de `w` et `w` non nul, puis `float(np.min(y * (X @ w + b))) / norme`. Pour la copie : b) $(2{,}5 ;\ 5{,}5)$ est le milieu de $(1, 5)$ et $(4, 6)$ ; d) le point $(3, 4)$, de score 2, à la distance $\frac{2}{\sqrt{2}} = \sqrt{2}$ ; e) multiplier $(\mathbf{w}, b)$ par $-2$ échange les côtés : la marge devient moins le **maximum** des distances signées, $-\frac{7}{\sqrt{2}}$, atteint en $(8, 0)$, pas $-\sqrt{2}$. Avec « $\ge 0$ », $\mathbf{w} = \mathbf{0}$, $b = 0$ vérifie tout : `True` pour n'importe quelles données.

**Erreurs fréquentes.** Oublier la colonne de 1 (pas de biais) ; laisser les bornes par défaut de `linprog`, qui imposent des inconnues positives ($\mathbf{w} \ge 0$, $b \ge 0$) ; `b_ub = 0` ; rendre `res.success` sans `bool(...)` (un `np.bool_`) ; une marge en valeur absolue (jamais négative) ; diviser par $\lVert \mathbf{w} \rVert^2$ ; rendre un `np.float64`.

### Ex M10.14 — Prédire : n points aux labels tirés au hasard en dimension d sont-ils séparables ?

**Réponses** : a) `2` · b) `3` · c) `3` · d) `4`.

**Démarche.** L'expérience donne environ 88 %, 54 %, 49 % et 0 %. Le compte exact (T. M. Cover, 1965) : pour $n$ points en position générale de $\mathbb{R}^d$, avec un biais, la proportion d'étiquetages séparables vaut $P(n, d) = 2^{1-n}\sum_{k=0}^{d}\binom{n-1}{k}$. a) $P(4, 2) = \frac{7}{8}$ : sur les 16 étiquetages de 4 points, exactement 2 échouent. Si un point est dans le triangle des trois autres, ce sont les deux où il est seul de sa classe : il est dans l'enveloppe de l'autre classe. (Si les quatre points sont les sommets d'un quadrilatère convexe, deux étiquetages échouent aussi : Cover a montré que leur nombre ne dépend pas de la configuration, tant que les points sont en position générale.) b) et c) $n = 2(d + 1)$ donne exactement $\frac{1}{2}$, quelle que soit la dimension. d) $P(30, 2) \approx 8 \times 10^{-7}$. Pour la copie : en dimension $d$, il faut nettement plus de $2(d + 1)$ points pour que des labels au hasard ne soient presque jamais séparables ; inversement, quand $d$ est grand devant $n$, un classifieur linéaire sépare **n'importe quels** labels, et une précision de 100 % sur l'entraînement ne dit rien de sa valeur.

**Erreurs fréquentes de prédiction.** a) 1 (100 %), par extrapolation de « $d + 1$ points sont toujours séparables » ; b) 4, en croyant que 6 points du plan ne sont presque jamais séparables ; c) 1 ou 2, en croyant que la grande dimension rend tout séparable, sans regarder le rapport $\frac{n}{d + 1}$.

### Ex M10.15 — Deux nuages, leurs enveloppes convexes et un hyperplan séparateur avec sa marge

**Réponse** : la figure, et les vérifications automatiques au vert.

**Démarche.** Pour chaque classe, `ax.scatter`, puis `hull = convex_hull_2d(cloud)` et `ax.plot` sur `np.vstack([hull, hull[:1]])` (le premier sommet répété ferme le polygone) ; `gamma = margin_of_separator(X, y, w, b)` ; trois droites $\mathbf{w} \cdot \mathbf{x} + b = c$, pour $c = 0$ et $c = \pm\gamma\lVert \mathbf{w} \rVert$, tracées sur deux abscisses par $x_2 = \frac{c - b - w_1x_1}{w_2}$. Pour la copie : le bord du côté $+1$ passe par $(3, 4)$ ; aucun point de la classe $-1$ ne touche l'autre bord ; la bande ne contient aucun point, puisque la marge est la plus petite distance signée. En gardant la direction, le meilleur $b$ (M10.3 e) est $0{,}5$, de marge $\frac{2{,}5}{\sqrt{2}} \approx 1{,}77$.

**Erreurs fréquentes.** Un polygone non fermé (le dernier côté manque) ; les bords de la marge à $\pm\gamma$ dans l'équation, au lieu de $\pm\gamma\lVert \mathbf{w} \rVert$ ; ouvrir une nouvelle figure dans la fonction.

### Ex M10.16 — Chasse à l'erreur : un produit vectoriel de signe inversé, une marge non normalisée

**Réponses** : a) `"AF"` · b) `[[0, 3], [3, 4], [4, 1], [1, 0]]` · c) `3` · d) `1.3416`.

**Démarche.** (A) calcule $u_2v_1 - u_1v_2$, l'opposé du produit vectoriel ; (B) à (E) sont justes ; (F) rend la plus petite marge fonctionnelle, sans diviser par $\lVert \mathbf{w} \rVert$. b) Avec le signe inversé, chaque demi-chaîne garde les virages à droite : la chaîne « du bas » construit le haut, et l'on obtient les bons sommets dans le sens des aiguilles d'une montre. c) Les marges fonctionnelles valent $4, 8, 3, 3$ : le code rend 3. d) $\frac{3}{\sqrt{5}} \approx 1{,}3416$. Pour la copie : `return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])` et `return min(scores) / np.linalg.norm(w)`. Les tests de M10.12 qui comparent l'ordre des sommets à `ConvexHull` et vérifient une aire signée positive attrapent (A) ; ceux de M10.13 qui comparent la marge à des distances attrapent (F).

**Erreurs fréquentes.** Citer (B) (le test $\le 0$ est juste) ou (D) ; en b), donner l'enveloppe juste au lieu de ce que rend le code ; en d), diviser par 5.

### Ex M10.17 — Des tests de propriétés pour l'enveloppe convexe

**Réponse** : les vérifications automatiques au vert : une liste vide sur les 20 enveloppes justes, et la bonne liste pour chacune des cinq fausses.

**Démarche.** Quatre tests, dans l'ordre : chaque sommet est une ligne de `points` (`np.array_equal`) ; `cross(H[i - 1], H[i], H[(i + 1) % h]) > 0` pour tout $i$ ; `cross(H[i], H[(i + 1) % h], p) >= -1e-9` pour tout côté et tout point ; `tuple(H[0]) == min(map(tuple, points))`. Pour la copie : une enveloppe dans le mauvais sens tourne à droite partout (« gauche ») et laisse les points intérieurs à droite de ses côtés (« dedans ») ; un point au milieu d'un côté donne un virage nul, que seul le « strictement » attrape. Les quatre propriétés ensemble caractérisent l'enveloppe (un polygone convexe dont les sommets sont des points du nuage et qui contient tous les points, à partir du bon point) ; chacune seule laisse passer des erreurs.

**Erreurs fréquentes.** Oublier le dernier virage (le dernier sommet suivi du premier) ; un test « gauche » avec $\ge 0$ (le point au milieu d'un côté passe) ; un test « dedans » sans tolérance (des arrondis) ou avec $> 0$ (les points des côtés échouent) ; rendre les noms dans un autre ordre.

### Ex M10.18 — Défi : la plus grande marge possible entre deux nuages donnés, à 1 % près

**Réponse** : `True` (défi réussi).

**Démarche.** La médiatrice des barycentres ne fait que 49 à 86 % de la plus grande marge : les barycentres résument mal les bords des nuages, qui seuls comptent. Deux méthodes passent. (1) **À direction fixée**, le meilleur $b$ met la droite à égale distance des deux nuages (fiche §3), et la marge vaut $\frac{\min_A \mathbf{u} \cdot \mathbf{x} - \max_B \mathbf{u} \cdot \mathbf{x}}{2}$ pour $\mathbf{u} = (\cos\theta, \sin\theta)$ : il suffit de balayer $\theta$ (720 angles donnent plus de 99,7 %). (2) **La géométrie** (le corrigé) : la plus grande marge est la moitié de la distance entre les enveloppes convexes, atteinte par la médiatrice du plus court segment qui les joint ; entre deux polygones convexes disjoints, ce segment va d'un sommet de l'un à un point d'un côté de l'autre (projeté avec un $t$ ramené dans $[0, 1]$), et `convex_hull_2d` réduit la recherche à quelques dizaines de couples ; on retrouve exactement `BEST_18`. On peut aussi minimiser $\lVert \mathbf{w} \rVert^2$ sous les contraintes $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ avec `scipy.optimize.minimize` (méthode SLSQP) : c'est le SVM à marge dure de M13b.

**Erreurs fréquentes.** Une direction trouvée, mais un $b$ qui n'est pas au milieu ; un balayage d'angles trop grossier ; le couple de sommets le plus proche seulement (sans les côtés), qui peut rester à plusieurs % de l'optimum ; une droite qui ne sépare pas (un rapport négatif).
