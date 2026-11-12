# CP4 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Barème par sous-question**, entre crochets ; sauf mention contraire, une sous-question vaut 0,25 point. Une justification demandée « sur ta copie » compte dans la sous-question à laquelle elle se rattache.
- **Crédit partiel** sur une sous-question de 0,25 point : 0,1 pour une réponse juste sans la démarche demandée, ou pour une méthode juste avec une erreur de calcul. **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois (par exemple une jacobienne fausse en CP4.2 b, réutilisée en d) à h), ou un gradient faux en CP4.10 c, réutilisé en d) et e)).
- **Arrondis** : une décimale de moins coûte au plus 0,05 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi. Des décimales en plus ne coûtent rien (le notebook les accepte).
- **Questions rédigées** (CP4.Q1, CP4.8, CP4.9 b, les phrases demandées « sur ta copie ») : les critères sont listés ; une idée juste formulée autrement compte autant.
- **Conventions** : $\ln$ est le logarithme népérien (`math.log`) ; une jacobienne a une ligne par sortie ; un gradient par rapport à une matrice a la forme de la matrice ; en coordonnées homogènes, les points sont des lignes (M16).

---

## CP4.Q1 — Dix affirmations sur la partie IV 🧠 · 1,5 point

0,15 par affirmation : 0,05 pour le verdict, 0,1 pour la justification.

**a) Vrai** (M17, M12a). Par la règle de la chaîne, $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$, de formes $(3, 2) \times (2, 3)$ : une matrice $3 \times 3$. Le rang d'un produit est au plus celui de chaque facteur, donc au plus 2 : la matrice n'est pas inversible, son déterminant est nul, en tout point. (L'image de $\mathbf{g} \circ \mathbf{f}$ passe par $\mathbb{R}^2$ : elle ne peut pas « remplir » un volume.)

**b) Vrai** (M16). $\operatorname{tr}(\mathbf{A}^k) = \sum_i (\mathbf{A}^k)_{ii}$ compte les chemins de longueur $k$ qui reviennent à leur départ. Un cycle qui ne repasse par aucun sommet a au plus 6 arêtes ; s'il en a $\ell$, il donne $(\mathbf{A}^\ell)_{ii} \ge 1$ pour chacun de ses sommets, donc $\operatorname{tr}(\mathbf{A}^\ell) > 0$. Toutes les traces jusqu'à 6 sont nulles : aucun cycle.

**c) Faux** (M17). $\mathbf{f}(x, y) = (x^3, y)$ a pour jacobienne $\operatorname{diag}(3x^2, 1)$, de déterminant nul en $\mathbf{0}$ ; pourtant $\mathbf{f}$ est injective sur tout $\mathbb{R}^2$ ($x \mapsto x^3$ est strictement croissante). Un déterminant nul dit seulement que l'approximation linéaire écrase une direction, pas que la fonction elle-même n'est pas injective.

**d) Faux** (M18). C'est le gradient de $\ln\det\mathbf{X}$. Pour $\det\mathbf{X}$ lui-même, $d(\det\mathbf{X}) = \det\mathbf{X}\,\operatorname{tr}(\mathbf{X}^{-1}d\mathbf{X})$, donc $\nabla\det\mathbf{X} = \det(\mathbf{X})\,\mathbf{X}^{-\top}$ (la comatrice). Contre-exemple : $\mathbf{X} = 2\mathbf{I}_2$, $\det\mathbf{X} = 4$, gradient $4 \times \frac12\mathbf{I} = 2\mathbf{I}$, pas $\frac12\mathbf{I}$.

**e) Vrai** (M19). $\nabla f = \big(2(x - 2y),\ -4(x - 2y) + 4y^3\big)$ s'annule en $(0, 0)$, où la hessienne vaut $\begin{pmatrix} 2 & -4 \\ -4 & 8 \end{pmatrix}$ : déterminant nul, valeurs propres 0 et 10, le test ne conclut pas. Mais $f = (x - 2y)^2 + y^4 \ge 0 = f(0, 0)$, avec égalité seulement si $y = 0$ et $x = 2y$, c'est-à-dire en $(0, 0)$ : c'est un minimum strict (global, même). La direction plate de la hessienne, $(2, 1)$, est celle où le terme $y^4$ décide. Le test de la hessienne est une condition suffisante, pas nécessaire.

**f) Vrai** (M19, M12a). Un point fixe vérifie $(\mathbf{I} - \mathbf{M})\mathbf{x} = \mathbf{c}$, et $\mathbf{I} - \mathbf{M}$ a pour valeurs propres $0{,}1$ et 0 : elle n'est pas inversible. Si $\mathbf{c}$ n'est pas dans son image (la droite propre de $0{,}9$), il n'y a aucune solution ; s'il y est, les solutions forment une droite (on peut ajouter n'importe quel vecteur du noyau, la droite propre de 1) : une infinité de points fixes.

**g) Faux** (M19). Les valeurs propres de $\mathbf{A} + 4\mathbf{I}$ sont 6 et 12 : son pas critique est $\frac{2}{12} = \frac16$, **plus petit** que $\frac28 = \frac14$. Le conditionnement, lui, s'améliore ($\kappa = 2$ au lieu de 4) : un pas plus petit, mais moins d'itérations au pas optimal.

**h) Faux** (M20). Les deux tableaux ont la même forme $(4,)$, mais `einsum` **somme** sur les indices qui disparaissent ($i$ et $k$) : c'est `T.sum(axis=(0, 2))`, 30 fois `T.mean(axis=(0, 2))` ($6 \times 5$ valeurs par case).

**i) Vrai** (M20). $\mathbb{E}[\hat Y] = \sum_i \frac{y_i}{\pi_i}\,\mathbb{E}[I_i] = \sum_i \frac{y_i}{\pi_i}\,\pi_i = \sum_i y_i$, par linéarité de l'espérance, pour **tout** plan de tirage où les $\pi_i$ sont $> 0$, à taille fixe ou non. Ce qui change avec le plan, c'est la variance (la formule $\sum_i y_i^2\,\frac{1 - \pi_i}{\pi_i}$ suppose des tirages indépendants).

**j) Faux** (M16). $X$ uniforme sur $\{-1, 0, 1\}$ et $Y = X^2$ : $\operatorname{Cov}(X, Y) = \mathbb{E}[X^3] - \mathbb{E}[X]\,\mathbb{E}[X^2] = 0$, mais $X^2$ et $Y^2 = X^4 = X^2$ sont la même variable, de variance $\frac23 - \frac49 = \frac29 \ne 0$ : $\operatorname{Cov}(X^2, Y^2) = \frac29$. Une covariance nulle ne dit rien des fonctions de $X$ et de $Y$ ; l'indépendance, si.

**Erreurs fréquentes** : en a), conclure sur la forme sans voir le rang ; en b), ne penser qu'aux cycles de longueur 6 ; en c), confondre l'approximation linéaire et la fonction ; en d), oublier le facteur $\det\mathbf{X}$ ; en e), croire que le test de la hessienne est nécessaire ; en f), oublier que $\mathbf{I} - \mathbf{M}$ peut être singulière ; en g), confondre le pas critique et le conditionnement ; en h), ne regarder que les formes ; en i), croire que l'absence de biais demande des tirages indépendants ; en j), croire que covariance nulle veut dire indépendance.
**Remédiation** : a) M17.3, M17.Q1 ; b) M16.3, M16.7, M16.8 ; c) M17.1, M17.E1 ; d) M18.8, M18.14 ; e) M19.2, M19.Q2 ; f) M19.3, M19.Q3 ; g) M19.4, M19.Q4, M19.Q5 ; h) M20.2, M20.Q2, M20.Q3 ; i) M20.4, M20.7, M20.Q4 ; j) M16.6, M16.Q4.

## CP4.1 — Coordonnées homogènes, chemins d'un graphe et variance d'un produit ✏️ · 2 points

**Réponses** : a) `[[1, -5, 0], [0, 3, 0], [1, 4, 1]]` · b) `[0, 18]` · c) `[-1, -3, 1]` · d) `3` · e) `4` · f) `-12` · g) `7.5` · h) `0.4534`.

a) En lignes, $f(\mathbf{x}) = \mathbf{x}\mathbf{W}_f + \mathbf{b}_f$ avec $(x, y)\mathbf{W}_f = (2x - y,\ x)$ : $\mathbf{W}_f = \begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix}$ et $\mathbf{b}_f = (1, 3)$. De même $\mathbf{W}_g = \begin{pmatrix} 0 & -3 \\ 1 & 1 \end{pmatrix}$, $\mathbf{b}_g = (-2, 4)$. Faire $f$ puis $g$, c'est multiplier par $\mathbf{H}_f\mathbf{H}_g$ :
$$\mathbf{H}_f\mathbf{H}_g = \begin{pmatrix} 2 & 1 & 0 \\ -1 & 0 & 0 \\ 1 & 3 & 1 \end{pmatrix}\begin{pmatrix} 0 & -3 & 0 \\ 1 & 1 & 0 \\ -2 & 4 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -5 & 0 \\ 0 & 3 & 0 \\ 1 & 4 & 1 \end{pmatrix},$$
soit $(g \circ f)(x, y) = (x + 1,\ -5x + 3y + 4)$. **[0,25]**
b) $[-1, 3, 1]\,\mathbf{H}_f\mathbf{H}_g = [-1 + 1,\ 5 + 9 + 4,\ 1] = [0, 18, 1]$. Vérification en deux temps : $f(-1, 3) = (-4, 2)$, puis $g(-4, 2) = (0, 18)$. **[0,25]**
c) La partie linéaire $\mathbf{W} = \begin{pmatrix} 1 & -5 \\ 0 & 3 \end{pmatrix}$ a pour inverse $\begin{pmatrix} 1 & 5/3 \\ 0 & 1/3 \end{pmatrix}$ ; la réciproque de $\mathbf{x} \mapsto \mathbf{x}\mathbf{W} + \mathbf{b}$ est $\mathbf{y} \mapsto (\mathbf{y} - \mathbf{b})\mathbf{W}^{-1}$, de translation $-\mathbf{b}\mathbf{W}^{-1} = -(1, 4)\mathbf{W}^{-1} = (-1, -3)$. La dernière ligne de $\mathbf{H}^{-1}$ est $[-1, -3, 1]$. **[0,25]**
d) Les chemins de 2 arêtes de 5 à 1 : $5 \to 4 \to 1$, $5 \to 3 \to 1$ et $5 \to 2 \to 1$, donc $(\mathbf{A}^2)_{51} = 3$. **[0,25]**
e) Toutes les arêtes vont vers un numéro plus **petit** : $\mathbf{A}$ est strictement triangulaire inférieure, le graphe est sans cycle (en renumérotant $i \mapsto 6 - i$, elle devient triangulaire supérieure). Le plus long chemin a 3 arêtes ($5 \to 4 \to 2 \to 1$, ou $5 \to 3 \to 2 \to 1$) : $\mathbf{A}^3 \ne \mathbf{0}$ et $\mathbf{A}^4 = \mathbf{0}$, donc $k = 4$. **[0,25]**
f) Les cinq chemins de 5 à 1 : $5 \to 4 \to 1$ ($2 \times 1 = 2$), $5 \to 3 \to 1$ ($-4$), $5 \to 2 \to 1$ ($-2$), $5 \to 4 \to 2 \to 1$ ($2 \times 3 \times (-2) = -12$), $5 \to 3 \to 2 \to 1$ ($(-1) \times 2 \times (-2) = 4$) ; somme : $2 - 4 - 2 - 12 + 4 = -12$. **[0,25]**
g) $D$ et $T$ sont indépendants : $\mathbb{E}[V] = 5 \times 1{,}5 = 7{,}5$ m³. **[0,25]**
h) $\mathbb{V}(V) = \sigma_D^2\sigma_T^2 + \sigma_D^2\,\mathbb{E}[T]^2 + \sigma_T^2\,\mathbb{E}[D]^2 = 0{,}09 \times 0{,}01 + 0{,}09 \times 2{,}25 + 0{,}01 \times 25 = 0{,}0009 + 0{,}2025 + 0{,}25 = 0{,}4534$ (en m⁶). **[0,25]**

Sur ta copie : $[0, 18, 1]\,\mathbf{H}^{-1} = [0 + 0 - 1,\ 0 + 6 - 3,\ 1] = [-1, 3, 1]$, on revient bien sur $P$ ; f) est le coefficient $(5, 1)$ de $(\mathbf{I} - \mathbf{W})^{-1} = \mathbf{I} + \mathbf{W} + \mathbf{W}^2 + \mathbf{W}^3$ (la série s'arrête, car $\mathbf{W}^4 = \mathbf{0}$) ; $\mathbb{V}(D)\,\mathbb{V}(T) = 0{,}0009$, 500 fois trop petit : l'essentiel vient des termes en moyennes (un écart-type du volume d'environ 0,67 m³, pour 7,5 m³).

**Erreurs fréquentes** : en a), multiplier dans l'ordre des colonnes ($\mathbf{H}_g\mathbf{H}_f$), ou écrire la translation dans la dernière colonne ; en b), appliquer $g$ d'abord ; en c), prendre $-\mathbf{b}$ pour la translation de la réciproque ; en d), compter les chemins de 3 arêtes, ou tous les chemins, ou lire le coefficient $(1, 5)$ (les chemins de 1 à 5 : il n'y en a aucun) ; en e), répondre 5 (« $\mathbf{A}^n = \mathbf{0}$ ») sans chercher la plus petite puissance ; en f), oublier les chemins de longueur 3 ou les signes ; en h), $\mathbb{V}(D)\,\mathbb{V}(T)$, ou les écarts-types à la place des variances.
**Remédiation** : M16.2, M16.3, M16.4, M16.5, M16.12, M16.13, M16.14.

## CP4.2 — Jacobienne d'une composée et produit vecteur-jacobienne ✏️ · 2 points

**Réponses** : a) `[-4, -2, 1]` · b) `[[-2, 2], [1, 2], [1, 1]]` · c) `[[1, -4, -4], [8, 1, 0]]` · d) `[[-10, -10], [-15, 18]]` · e) `[20, -46]` · f) `[12, 16]` · g) `[-0.5, -20.4]` · h) `[[-96, 96], [12, 24], [3, 3]]`.

a) $\mathbf{f}(2, -2) = (-4,\ 2 - 4,\ e^0) = (-4, -2, 1)$. **[0,25]**
b) $\mathbf{J}_{\mathbf{f}} = \begin{pmatrix} y & x \\ 1 & 2 \\ e^{x + y} & e^{x + y} \end{pmatrix}$, en $\mathbf{p}$ : $\begin{pmatrix} -2 & 2 \\ 1 & 2 \\ 1 & 1 \end{pmatrix}$, de forme $(3, 2)$. **[0,25]**
c) $\mathbf{J}_{\mathbf{g}} = \begin{pmatrix} c & 2b & a \\ -2a & 1 & 0 \end{pmatrix}$, au point **intermédiaire** $(a, b, c) = (-4, -2, 1)$ : $\begin{pmatrix} 1 & -4 & -4 \\ 8 & 1 & 0 \end{pmatrix}$. **[0,25]**
d) $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{p}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{p}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{p})$, de forme $(2, 3) \times (3, 2) = (2, 2)$ : $\begin{pmatrix} -2 - 4 - 4 & 2 - 8 - 4 \\ -16 + 1 + 0 & 16 + 2 + 0 \end{pmatrix} = \begin{pmatrix} -10 & -10 \\ -15 & 18 \end{pmatrix}$. **[0,25]**
e) $\mathbf{u}^\top\mathbf{J} = 1 \times (-10, -10) - 2 \times (-15, 18) = (20, -46)$. **[0,25]**
f) On compte toutes les multiplications, même par 0. $\mathbf{u}^\top\mathbf{J}_{\mathbf{g}}$ : $(1, 2) \times (2, 3)$, $2 \times 3 = 6$ multiplications ; puis $(1, 3) \times (3, 2)$ : 6 ; en tout **12**. $\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}$ : $2 \times 3 \times 2 = 12$ ; puis $(1, 2) \times (2, 2)$ : 4 ; en tout **16**. **[0,25]**
g) $(\mathbf{g} \circ \mathbf{f})(\mathbf{p}) = \mathbf{g}(-4, -2, 1) = (-4 + 4,\ -2 - 16) = (0, -18)$ et $\mathbf{h} = (0{,}1 ;\ -0{,}05)$ : $\mathbf{J}\mathbf{h} = (-1 + 0{,}5,\ -1{,}5 - 0{,}9) = (-0{,}5 ;\ -2{,}4)$, d'où $(-0{,}5 ;\ -20{,}4)$. **[0,25]**
h) $\boldsymbol{\varphi}$ agit coordonnée par coordonnée : $\mathbf{J}_{\boldsymbol{\varphi}} = \operatorname{diag}(3t_1^2, 3t_2^2, 3t_3^2)$, en $\mathbf{f}(\mathbf{p})$ : $\operatorname{diag}(48, 12, 3)$. Multiplier à gauche par une diagonale multiplie les **lignes** de $\mathbf{J}_{\mathbf{f}}$ : $\begin{pmatrix} -96 & 96 \\ 12 & 24 \\ 3 & 3 \end{pmatrix}$. **[0,25]**

Sur ta copie : $\frac{\partial(\mathbf{g} \circ \mathbf{f})_1}{\partial x} = \frac{\partial g_1}{\partial a}\frac{\partial f_1}{\partial x} + \frac{\partial g_1}{\partial b}\frac{\partial f_2}{\partial x} + \frac{\partial g_1}{\partial c}\frac{\partial f_3}{\partial x} = 1 \times (-2) + (-4) \times 1 + (-4) \times 1 = -10$ ; e) est le gradient (en ligne) de $\mathbf{u} \cdot (\mathbf{g} \circ \mathbf{f}) = (\mathbf{g} \circ \mathbf{f})_1 - 2\,(\mathbf{g} \circ \mathbf{f})_2$ en $\mathbf{p}$ ; pour g), l'écart vaut environ 0,03 et 0,13 : il est d'ordre $\lVert \mathbf{h} \rVert^2$ (ici $\lVert \mathbf{h} \rVert \approx 0{,}11$, $\lVert \mathbf{h} \rVert^2 \approx 0{,}0125$), multiplié par des dérivées secondes de l'ordre de 10 ; l'approximation linéaire néglige exactement ces termes d'ordre 2 (Taylor), alors que les variations d'ordre 1 valent $0{,}5$ et $2{,}4$.

**Erreurs fréquentes** : en b) et c), transposer (une colonne par sortie) ; en c), évaluer $\mathbf{J}_{\mathbf{g}}$ au mauvais point (avec les coordonnées de $\mathbf{p}$ au lieu de celles de $\mathbf{f}(\mathbf{p})$) ; en d), multiplier dans l'ordre $\mathbf{J}_{\mathbf{f}}\mathbf{J}_{\mathbf{g}}$ (une matrice $3 \times 3$ !) ; en e), calculer $\mathbf{J}\mathbf{u}$ ; en g), oublier $(\mathbf{g} \circ \mathbf{f})(\mathbf{p})$ ; en h), prendre $\varphi(t_i)$ au lieu de $\varphi'(t_i)$, ou multiplier les colonnes.
**Remédiation** : M17.1, M17.2, M17.3, M17.5, M17.Q3, M17.Q5, M17.16.

## CP4.3 — Mode direct et mode inverse sur un graphe de calcul ✏️ · 2 points

**Réponses** : a) `98.8751` · b) `3` · c) `[1, 14, 0.1111]` · d) `35.761` · e) `[45, 2.1972]` · f) `15.9861` · g) `-63.9445` · h) `[6, 25]`.

a) $v_1 = 5 + 4 = 9$, $v_2 = 5 \times 9 = 45$, $v_3 = \ln 9$, $f = 45\ln 9 \approx 98{,}8751$. **[0,25]**
b) $x$ sert deux fois (dans $v_1$ et dans $v_2$) et $v_1$ aussi (dans $v_2$ et dans $v_3$) : $x \to v_1 \to v_2 \to f$, $x \to v_1 \to v_3 \to f$ et $x \to v_2 \to f$, soit **3** chemins. **[0,25]**
c) $\dot{v}_1 = \dot{x} + 2y\,\dot{y} = 1$ ; $\dot{v}_2 = \dot{x}\,v_1 + x\,\dot{v}_1 = 9 + 5 = 14$ ; $\dot{v}_3 = \frac{\dot{v}_1}{v_1} = \frac19 \approx 0{,}1111$. **[0,25]**
d) $\dot{f} = \dot{v}_2\,v_3 + v_2\,\dot{v}_3 = 14\ln 9 + \frac{45}{9} = 14\ln 9 + 5 \approx 35{,}761$. **[0,25]**
e) Dans l'ordre inverse : $\bar{f} = 1$ ; $\bar{v}_3 = \bar{f}\,\frac{\partial f}{\partial v_3} = v_2 = 45$ ; $\bar{v}_2 = \bar{f}\,v_3 = \ln 9 \approx 2{,}1972$. **[0,25]**
f) $v_1$ sert deux fois, dans $v_2$ et dans $v_3$ : $\bar{v}_1 = \bar{v}_2\,\frac{\partial v_2}{\partial v_1} + \bar{v}_3\,\frac{\partial v_3}{\partial v_1} = x\ln 9 + \frac{45}{9} = 5\ln 9 + 5 \approx 15{,}9861$. **[0,25]**
g) $y$ n'entre que dans $v_1$, avec la dérivée locale $2y = -4$ : $\bar{y} = -4\,\bar{v}_1 = -20\ln 9 - 20 \approx -63{,}9445$. **[0,25]**
h) Le mode direct donne une **colonne** de la jacobienne $(25, 6)$ par passage (une graine par entrée) : 6 passages ; le mode inverse une **ligne** par passage (une par sortie) : 25. Ici, avec plus de sorties que d'entrées, le mode direct gagne. **[0,25]**

Sur ta copie : les dérivées locales sur les arêtes : $x \to v_1$ : 1 ; $y \to v_1$ : $2y = -4$ ; $x \to v_2$ : $v_1 = 9$ ; $v_1 \to v_2$ : $x = 5$ ; $v_1 \to v_3$ : $\frac{1}{v_1} = \frac19$ ; $v_2 \to f$ : $v_3 = \ln 9$ ; $v_3 \to f$ : $v_2 = 45$. (Pour aller plus loin, non noté : par le mode inverse, $\bar{x} = \bar{v}_1 \times 1 + \bar{v}_2 \times v_1 = 5\ln 9 + 5 + 9\ln 9 = 14\ln 9 + 5$, c'est d).) Avec les nombres duaux, $\ln(a + b\varepsilon) = \ln a + \frac{b}{a}\,\varepsilon$ : $\ln(9 + \varepsilon) = \ln 9 + \frac19\,\varepsilon$, c'est le nœud $v_3$ (valeur $\ln 9$, tangente $\dot{v}_3 = \frac19$), car $v_1 = 9 + \varepsilon$ quand $x = 5 + \varepsilon$.

**Erreurs fréquentes** : en b) et d), oublier l'arête directe $x \to v_2$ (d) devient $5\ln 9 + 5 \approx 15{,}986$) ; en c) et d), un seul terme dans la dérivée d'un produit ; en e), échanger $\bar{v}_2$ et $\bar{v}_3$ ; en f), oublier l'une des deux contributions ($5\ln 9$ ou 5) ; en g), oublier la dérivée locale $2y$, ou son signe ; en h), inverser les deux nombres.
**Remédiation** : M18.1, M18.2, M18.3, M18.4, M18.5, M18.Q4, M18.Q5, M18.20.

## CP4.4 — Gradients par rapport à une matrice ✏️ · 1,75 point

**Réponses** : a) `[[6, 15], [-2, -5]]` · b) `[[-1, 2], [4, 1]]` · c) `[[4, 2], [4, 4]]` · d) `[[4, -5], [-3, 4]]` · e) `-0.15` · f) `[[1.5, 0.75], [0.75, 2.5]]` · g) `[[87, 22], [112, 25]]`.

a) $\mathbf{a}^\top\mathbf{X}\mathbf{b} = \sum_{i, j} a_iX_{ij}b_j$, donc $\frac{\partial}{\partial X_{ij}} = a_ib_j$ : le gradient est $\mathbf{a}\mathbf{b}^\top = \begin{pmatrix} 6 & 15 \\ -2 & -5 \end{pmatrix}$. **[0,25]**
b) $\operatorname{tr}(\mathbf{A}\mathbf{X}) = \sum_{i, j} A_{ji}X_{ij}$, donc le gradient est $\mathbf{A}^\top = \begin{pmatrix} -1 & 2 \\ 4 & 1 \end{pmatrix}$. **[0,25]**
c) Le gradient de $\operatorname{tr}(\mathbf{X}^\top\mathbf{B}\mathbf{X}) = \sum_j \mathbf{x}_j^\top\mathbf{B}\mathbf{x}_j$ (les colonnes $\mathbf{x}_j$ de $\mathbf{X}$) est $(\mathbf{B} + \mathbf{B}^\top)\mathbf{X}$ : $\begin{pmatrix} 6 & -4 \\ -4 & 4 \end{pmatrix}\begin{pmatrix} 4 & 3 \\ 5 & 4 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 4 & 4 \end{pmatrix}$. **[0,25]**
d) $\det\mathbf{X} = 16 - 15 = 1$, $\mathbf{X}^{-1} = \begin{pmatrix} 4 & -3 \\ -5 & 4 \end{pmatrix}$, et le gradient de $\ln\det\mathbf{X}$ est $\mathbf{X}^{-\top} = \begin{pmatrix} 4 & -5 \\ -3 & 4 \end{pmatrix}$. **[0,25]**
e) Au premier ordre, la variation vaut $\operatorname{tr}(\mathbf{G}^\top\mathbf{H}) = \sum_{i, j} G_{ij}H_{ij} = G_{21} \times 0{,}05 = -3 \times 0{,}05 = -0{,}15$. **[0,25]**
f) Le gradient d'une moyenne est la moyenne des gradients, et celui de $\mathbf{z}^\top\mathbf{X}\mathbf{z}$ est $\mathbf{z}\mathbf{z}^\top$ (c'est a) avec $\mathbf{a} = \mathbf{b} = \mathbf{z}$) : $\frac14\left[\begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 4 \end{pmatrix} + \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} + \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}\right] = \frac14\begin{pmatrix} 6 & 3 \\ 3 & 10 \end{pmatrix}$. **[0,25]**
g) $X$ apparaît deux fois : $d\big((\mathbf{X}\mathbf{a}) \cdot (\mathbf{X}\mathbf{b})\big) = (d\mathbf{X}\,\mathbf{a}) \cdot (\mathbf{X}\mathbf{b}) + (\mathbf{X}\mathbf{a}) \cdot (d\mathbf{X}\,\mathbf{b}) = (\mathbf{X}\mathbf{b})^\top d\mathbf{X}\,\mathbf{a} + (\mathbf{X}\mathbf{a})^\top d\mathbf{X}\,\mathbf{b}$ : deux formes bilinéaires, dont les gradients sont donnés par a). $\mathbf{X}\mathbf{a} = (9, 11)$ et $\mathbf{X}\mathbf{b} = (23, 30)$ : $\mathbf{G} = (\mathbf{X}\mathbf{b})\,\mathbf{a}^\top + (\mathbf{X}\mathbf{a})\,\mathbf{b}^\top = \begin{pmatrix} 69 & -23 \\ 90 & -30 \end{pmatrix} + \begin{pmatrix} 18 & 45 \\ 22 & 55 \end{pmatrix} = \begin{pmatrix} 87 & 22 \\ 112 & 25 \end{pmatrix}$, c'est-à-dire $\mathbf{X}(\mathbf{a}\mathbf{b}^\top + \mathbf{b}\mathbf{a}^\top)$. **[0,25]**

Sur ta copie : pour c), $\mathbf{x}^\top\mathbf{B}\mathbf{x} = \mathbf{x}^\top\frac{\mathbf{B} + \mathbf{B}^\top}{2}\mathbf{x}$ ne voit que la partie symétrique de $\mathbf{B}$ ; le gradient $2\mathbf{B}\mathbf{x}$ ne vaut que pour $\mathbf{B}$ symétrique ; pour e), $\det(\mathbf{X} + \mathbf{H}) = 16 - 3 \times 5{,}05 = 0{,}85$ et $\ln 0{,}85 \approx -0{,}1625$ : l'approximation $-0{,}15$ est à 0,0125 près, l'ordre 2 de $\mathbf{H}$ ; pour g), $d(\mathbf{a}^\top\mathbf{X}^\top\mathbf{X}\mathbf{b}) = \operatorname{tr}\big((\mathbf{a}\,(\mathbf{X}\mathbf{b})^\top + \mathbf{b}\,(\mathbf{X}\mathbf{a})^\top)\,d\mathbf{X}\big) = \operatorname{tr}(\mathbf{G}^\top d\mathbf{X})$, d'où $\mathbf{G}$.

**Erreurs fréquentes** : en a), $\mathbf{b}\mathbf{a}^\top$ ; en b) et d), oublier la transposée ; en c), $2\mathbf{B}\mathbf{X}$ avec $\mathbf{B}$ non symétrique ; en e), lire le coefficient de $\mathbf{X}^{-1}$ au lieu de $\mathbf{X}^{-\top}$ ($-0{,}25$) ; en f), la somme au lieu de la moyenne ; en g), un seul des deux termes, ou $(\mathbf{a}\mathbf{b}^\top + \mathbf{b}\mathbf{a}^\top)\mathbf{X}$, le facteur à gauche de $\mathbf{X}$ au lieu de la droite.
**Remédiation** : M18.6, M18.7, M18.8, M18.10, M18.Q6, M18.Q8, M18.22.

## CP4.5 — Hessienne, Taylor d'ordre 2 et nature d'un point critique ✏️ · 2 points

**Réponses** : a) `[-24, 5, -5]` · b) `[[6, 0, 0], [0, 6, 1], [0, 1, 6]]` · c) `-24.74` · d) `0.001` · e) `[[-3, 0, 0], [3, 0, 0]]` · f) `[5, 7, 18]` · g) `1` · h) `3`.

a) $\nabla f = (3x^2 - 27,\ 6y + z,\ y + 6z)$, en $P$ : $(3 - 27,\ 6 - 1,\ 1 - 6) = (-24, 5, -5)$. **[0,25]**
b) $\mathbf{H}_f = \begin{pmatrix} 6x & 0 & 0 \\ 0 & 6 & 1 \\ 0 & 1 & 6 \end{pmatrix}$, en $P$ ($x = 1$) : $\begin{pmatrix} 6 & 0 & 0 \\ 0 & 6 & 1 \\ 0 & 1 & 6 \end{pmatrix}$. **[0,25]**
c) $f(P) = 1 - 27 + 3 - 1 + 3 = -21$ ; $\nabla f(P) \cdot \mathbf{h} = -2{,}4 - 0{,}5 - 1 = -3{,}9$ ; $\mathbf{h}^\top\mathbf{H}\mathbf{h} = 6 \times 0{,}01 + 6 \times 0{,}01 + 2 \times 1 \times (-0{,}1) \times 0{,}2 + 6 \times 0{,}04 = 0{,}32$. $T_2 = -21 - 3{,}9 + 0{,}16 = -24{,}74$. **[0,25]**
d) $f(1{,}1 ;\ 0{,}9 ;\ -0{,}8) = 1{,}331 - 29{,}7 + 2{,}43 - 0{,}72 + 1{,}92 = -24{,}739$, donc l'erreur vaut $-24{,}739 + 24{,}74 = 0{,}001$. **[0,25]**
e) $\nabla f = \mathbf{0}$ : $x^2 = 9$, et le système $6y + z = 0$, $y + 6z = 0$ (de déterminant $35 \ne 0$) donne $y = z = 0$. Deux points critiques : $(-3, 0, 0)$ et $(3, 0, 0)$. **[0,25]**
f) En $(3, 0, 0)$ : $\mathbf{H} = \begin{pmatrix} 18 & 0 & 0 \\ 0 & 6 & 1 \\ 0 & 1 & 6 \end{pmatrix}$, diagonale par blocs : 18, et le bloc $\begin{pmatrix} 6 & 1 \\ 1 & 6 \end{pmatrix}$, de valeurs propres $6 \pm 1$. Dans l'ordre croissant : $[5, 7, 18]$. **[0,25]**
g) Les trois valeurs propres sont strictement positives : la hessienne est définie positive, c'est un **minimum** local (strict), le numéro 1. **[0,25]**
h) En $(-3, 0, 0)$, les valeurs propres sont $-18$, 5 et 7 : de signes opposés, c'est un **point selle**, le numéro 3. **[0,25]**

Sur ta copie : $f$ est un polynôme de degré 3 ; son développement de Taylor en $P$ s'arrête à l'ordre 3, et le seul terme de degré 3 est $x^3$, de dérivée troisième 6 : $f(P + \mathbf{h}) = T_2(P + \mathbf{h}) + \frac{6}{3!}h_1^3 = T_2(P + \mathbf{h}) + h_1^3$, avec $h_1 = 0{,}1$. Pour h), $f$ descend le long de l'axe des $x$ (la direction propre de $-18$) : $f(-3 + t, 0, 0) = f(-3, 0, 0) - 9t^2 + t^3$, plus petit que $f(-3, 0, 0) = 54$ pour $t$ petit, de chaque côté ; elle monte le long de $(0, 1, 1)$ et $(0, 1, -1)$. Le minimum g) est local, pas global : $f(x, 0, 0) \to -\infty$ quand $x \to -\infty$.

**Erreurs fréquentes** : en b), un 2 pour la dérivée croisée de $yz$ ; en c), oublier le $\frac12$ ($-24{,}58$) ; en d), le signe ; en e), oublier $x = -3$ ; en f), ne pas voir que la hessienne est diagonale par blocs ; en g), croire le minimum global ; en h), conclure « maximum » (2) parce qu'une valeur propre est négative, ou « on ne peut pas conclure » (4).
**Remédiation** : M19.1, M19.2, M19.Q1, M19.Q2, M19.19.

## CP4.6 — Itération de Richardson et récurrence d'ordre 2 ✏️ · 1,75 point

**Réponses** : a) `[-0.1, 1]` · b) `[0.27, 1.26]` · c) `"2/11"` · d) `0.7` · e) `17` · f) `[-0.6, 0.8]` · g) `0.6403`.

a) $\mathbf{x}_1 = \mathbf{0} + 0{,}1\,(\mathbf{b} - \mathbf{0}) = (-0{,}1 ;\ 1)$. **[0,25]**
b) $\mathbf{A}\mathbf{x}_1 = (-0{,}7 - 4 ;\ 0{,}4 + 7) = (-4{,}7 ;\ 7{,}4)$, résidu $\mathbf{b} - \mathbf{A}\mathbf{x}_1 = (3{,}7 ;\ 2{,}6)$, et $\mathbf{x}_2 = (-0{,}1 + 0{,}37 ;\ 1 + 0{,}26) = (0{,}27 ;\ 1{,}26)$. **[0,25]**
c) Les valeurs propres de $\mathbf{I} - \omega\mathbf{A}$ sont $1 - 3\omega$ et $1 - 11\omega$ ; toutes deux sont dans $]-1, 1[$ si et seulement si $0 < \omega < \frac{2}{11}$. **[0,25]**
d) $\lvert 1 - 0{,}3 \rvert = 0{,}7$ et $\lvert 1 - 1{,}1 \rvert = 0{,}1$ : le facteur est le plus grand, $0{,}7$. **[0,25]**
e) $\kappa = \frac{11}{3}$, $\frac{\kappa - 1}{\kappa + 1} = \frac{8}{14} = \frac47$. Il faut $\left(\frac47\right)^k \le 10^{-4}$, soit $k \ge \frac{\ln 10^4}{\ln(7/4)} = \frac{9{,}2103}{0{,}5596} \approx 16{,}46$ : $k = 17$. **[0,25]**
f) $u_{k+2} = 0{,}2\,u_{k+1} + 0{,}48\,u_k$ donne $r^2 - 0{,}2\,r - 0{,}48 = 0$ (dans les notations de M19, $p = 0{,}2$ et $q = -0{,}48$) : $\Delta = 0{,}04 + 1{,}92 = 1{,}96$, racines $\frac{0{,}2 \pm 1{,}4}{2}$, soit $-0{,}6$ et $0{,}8$ (somme $0{,}2$, produit $-0{,}48$). **[0,25]**
g) $r^2 - r + 0{,}41 = 0$ : $\Delta = 1 - 1{,}64 = -0{,}64$, racines $0{,}5 \pm 0{,}4\,i$, de module $\sqrt{0{,}25 + 0{,}16} = \sqrt{0{,}41} \approx 0{,}6403$ (le module des deux racines conjuguées est la racine de leur produit, $q = 0{,}41$). **[0,25]**

Sur ta copie : $\mathbf{x}^\star = (1, 2)$ ($7 - 8 = -1$ et $-4 + 14 = 10$). (Pour aller plus loin, non noté : les erreurs de $\mathbf{x}_0$, $\mathbf{x}_1$, $\mathbf{x}_2$ ont pour normes $2{,}236$, $1{,}487$ et $1{,}039$ ; chaque pas les multiplie par moins de 0,7, et l'erreur s'aligne sur la direction propre $(1, 1)$ de la valeur propre 3, la plus lente.) $(R_1)$ : $u_k = \alpha\,0{,}8^k + \beta\,(-0{,}6)^k$, avec $\alpha + \beta = 2$ et $0{,}8\alpha - 0{,}6\beta = 0{,}2$, d'où $\alpha = \beta = 1$ : $u_k = 0{,}8^k + (-0{,}6)^k \to 0$. $(R_2)$ : le module $0{,}64 < 1$ (le critère : $\lvert q \rvert = 0{,}41 < 1$ et $\lvert p \rvert = 1 < 1{,}41$) : $w_k \to 0$ depuis tout départ, en **oscillant** (racines complexes), l'amplitude multipliée par 0,64 à chaque pas.

**Erreurs fréquentes** : en b), réutiliser le résidu de $\mathbf{x}_0$ ; en c), régler le pas sur $\lambda_{\min}$ ($\frac23$), ou donner le pas optimal $\frac{2}{3 + 11} = \frac17$ ; en d), prendre le plus petit des deux facteurs ; en e), arrondir vers le bas, ou utiliser le facteur 0,7 de $\omega = 0{,}1$ (26 pas) ; en f), écrire $r^2 + 0{,}2\,r + 0{,}48$ ou $r^2 + 0{,}2\,r - 0{,}48$ (une erreur de signe) ; en g), donner la partie réelle 0,5, ou $q = 0{,}41$ au lieu de $\sqrt q$.
**Remédiation** : M19.3, M19.4, M19.5, M19.6, M19.7, M19.11, M19.12, M19.Q4, M19.Q6.

## CP4.7 — Moments le long d'axes, einsum et estimateur de Horvitz-Thompson ✏️ · 1,5 point

**Réponses** : a) `"(2, 3)"` · b) `[4, 4.5]` · c) `[[2, 4.5, 12.5], [12.5, 0.5, 4.5]]` · d) `[[-1, 10], [15, 25]]` · e) `160` · f) `1565`.

a) Réduire l'axe 1 (les étages) le fait disparaître : $(2, 2, 3) \to (2, 3)$. **[0,25]**
b) Pour chaque bâtiment, la moyenne de ses $2 \times 3 = 6$ valeurs : $\frac{4 + 7 + 1 + 2 + 4 + 6}{6} = 4$ et $\frac{3 + 0 + 6 + 8 + 1 + 9}{6} = 4{,}5$. **[0,25]**
c) Pour chaque bâtiment et chaque allée, la variance des deux étages, avec `ddof=1` : $\frac{(a - b)^2}{2}$. Bâtiment 0 : $(4, 2) \to 2$, $(7, 4) \to 4{,}5$, $(1, 6) \to 12{,}5$ ; bâtiment 1 : $(3, 8) \to 12{,}5$, $(0, 1) \to 0{,}5$, $(6, 9) \to 4{,}5$. **[0,25]**
d) $\sum_k T_{ijk}w_k = T_{ij0} - T_{ij1} + 2T_{ij2}$ : $4 - 7 + 2 = -1$ ; $2 - 4 + 12 = 10$ ; $3 - 0 + 12 = 15$ ; $8 - 1 + 18 = 25$. **[0,25]**
e) $\hat Y = \frac{50}{1} + \frac{14}{0{,}35} + \frac{7}{0{,}1} = 50 + 40 + 70 = 160$. **[0,25]**
f) $\mathbb{V}(\hat Y) = \sum_{i=1}^5 y_i^2\,\frac{1 - \pi_i}{\pi_i} = 0 + 676 \times \frac{7}{13} + 196 \times \frac{13}{7} + 484 \times \frac{9}{11} + 49 \times 9 = 0 + 364 + 364 + 396 + 441 = 1\,565$. **[0,25]**

Sur ta copie : pour deux valeurs, la moyenne est $\frac{a + b}{2}$ et les écarts sont $\pm\frac{a - b}{2}$ ; la somme de leurs carrés vaut $\frac{(a - b)^2}{2}$, et `ddof=1` divise par $n - 1 = 1$. $\mathbb{E}[\hat Y] = Y = 50 + 26 + 14 + 22 + 7 = 119$ : l'estimateur est sans biais (l'échantillon tiré ici donne 160, un autre donnerait moins) ; son écart-type, $\sqrt{1\,565} \approx 39{,}6$, vaut le tiers de 119 : une estimation peu précise. La plus grande part vient du rucher 5 (441 sur 1 565), qui a la plus petite récolte mais aussi la plus petite probabilité : quand il est tiré, il compte pour $\frac{1}{0{,}1} = 10$ ruchers, et le facteur $\frac{1 - \pi_5}{\pi_5} = 9$ est le plus grand. Le rucher 1, toujours tiré, n'apporte rien.

**Erreurs fréquentes** : en a), garder l'axe réduit, $(2, 1, 3)$ (c'est `keepdims=True`) ; en b), la somme au lieu de la moyenne, ou les axes $(0, 2)$ (la moyenne par étage, $[3{,}5 ;\ 5]$) ; en c), `ddof=0` (la moitié) ; en d), oublier les poids ; en e), additionner les $y_i$ sans les diviser, ou multiplier par $\pi_i$ ; en f), ne sommer que sur l'échantillon tiré (805), ou diviser par $\pi_i^2$.
**Remédiation** : M20.1, M20.2, M20.4, M20.11, M20.12, M20.Q2, M20.Q3.

## CP4.8 — Une démonstration au choix ∂ · 2 points

### Sujet A — Une matrice symétrique qui raccourcit tous les vecteurs

1. **[0,5]** Si $\mathbf{M}\mathbf{v} = \lambda\mathbf{v}$ avec $\lambda$ réel et $\mathbf{v} \ne \mathbf{0}$ réel, alors $\lVert \mathbf{M}\mathbf{v} \rVert = \lvert \lambda \rvert\,\lVert \mathbf{v} \rVert$, et l'hypothèse donne $\lvert \lambda \rvert\,\lVert \mathbf{v} \rVert < \lVert \mathbf{v} \rVert$, donc $\lvert \lambda \rvert < 1$ (on divise par $\lVert \mathbf{v} \rVert > 0$). La symétrie n'a pas servi.
2. **[0,5]** $\lVert \mathbf{M}\mathbf{x} \rVert^2 = (\mathbf{M}\mathbf{x})^\top(\mathbf{M}\mathbf{x}) = \mathbf{x}^\top\mathbf{M}^\top\mathbf{M}\mathbf{x} = \mathbf{x}^\top\mathbf{M}^2\mathbf{x}$, puisque $\mathbf{M}^\top = \mathbf{M}$. $\mathbf{M}^2$ est symétrique, de valeurs propres $\lambda_i^2$ (si $\mathbf{M}\mathbf{q} = \lambda\mathbf{q}$, $\mathbf{M}^2\mathbf{q} = \lambda^2\mathbf{q}$, et le théorème spectral donne une base de tels $\mathbf{q}$). Le quotient de Rayleigh (M12c) borne $\mathbf{x}^\top\mathbf{M}^2\mathbf{x} \le \max_i \lambda_i^2\,\lVert \mathbf{x} \rVert^2$ ; comme $\max_i \lambda_i^2 < 1$, $\lVert \mathbf{M}\mathbf{x} \rVert^2 < \lVert \mathbf{x} \rVert^2$ pour $\mathbf{x} \ne \mathbf{0}$.
3. **[0,5]** Pour $\mathbf{x} \ne \mathbf{0}$ : si $\mathbf{N}\mathbf{x} = \mathbf{0}$, $\lVert \mathbf{M}\mathbf{N}\mathbf{x} \rVert = 0 < \lVert \mathbf{x} \rVert$ ; sinon $\lVert \mathbf{M}(\mathbf{N}\mathbf{x}) \rVert < \lVert \mathbf{N}\mathbf{x} \rVert < \lVert \mathbf{x} \rVert$. Donc $\mathbf{M}\mathbf{N}$ raccourcit les vecteurs. Avec les matrices données ($\mathbf{M}$ diagonale de valeurs propres $0{,}8$ et $0{,}2$, $\mathbf{N}$ de valeurs propres $0{,}9$ et $0{,}1$ : toutes deux raccourcissent les vecteurs, par la question 2), $\mathbf{M}\mathbf{N} = \begin{pmatrix} 0{,}4 & 0{,}32 \\ 0{,}08 & 0{,}1 \end{pmatrix}$, qui n'est pas symétrique ($(\mathbf{M}\mathbf{N})^\top = \mathbf{N}\mathbf{M} \ne \mathbf{M}\mathbf{N}$). La question 1, qui ne demandait pas la symétrie, s'applique : ses valeurs propres réelles sont dans $]-1, 1[$ (ici environ $0{,}469$ et $0{,}031$).
4. **[0,5]** $\mathbf{B}$ est triangulaire : sa seule valeur propre est $0{,}2$ (double), dans $]-1, 1[$. Mais $\mathbf{B}(1, 0) = (0{,}2 ;\ 1{,}5)$, de norme $\sqrt{2{,}29} \approx 1{,}51 > 1$ : $\mathbf{B}$ allonge $(1, 0)$. $\mathbf{B}^\top\mathbf{B} = \begin{pmatrix} 2{,}29 & 0{,}3 \\ 0{,}3 & 0{,}04 \end{pmatrix}$ n'est pas $\mathbf{B}^2 = \begin{pmatrix} 0{,}04 & 0 \\ 0{,}6 & 0{,}04 \end{pmatrix}$ : c'est l'égalité $\mathbf{M}^\top\mathbf{M} = \mathbf{M}^2$ de la question 2 qui tombe. Les valeurs propres de $\mathbf{B}^\top\mathbf{B}$ (environ $2{,}33$ et $0{,}0007$) ne sont pas les carrés de celles de $\mathbf{B}$ : la plus grande dépasse 1, et c'est elle qui décide de l'allongement.

**Grille de relecture.** (1) un vecteur propre réel et la division par sa norme, sans symétrie ; (2) $\mathbf{M}^\top\mathbf{M} = \mathbf{M}^2$, ses valeurs propres $\lambda_i^2$, le quotient de Rayleigh et l'inégalité stricte ; (3) les deux inégalités enchaînées (avec le cas $\mathbf{N}\mathbf{x} = \mathbf{0}$), le produit calculé et non symétrique, la question 1 réutilisée ; (4) la valeur propre de $\mathbf{B}$, le vecteur allongé, $\mathbf{B}^\top\mathbf{B} \ne \mathbf{B}^2$. Ce qui décide de l'allongement d'une matrice quelconque, ce sont les valeurs propres de $\mathbf{M}^\top\mathbf{M}$, les carrés de ses valeurs singulières (M12d) ; pour une matrice symétrique, ce sont les carrés de ses valeurs propres.

### Sujet B — La variance d'un produit dépasse le produit des variances

1. **[0,5]** $(U + \mu_X)(V + \mu_Y) - \mu_X\mu_Y = UV + \mu_Y U + \mu_X V$. $\mathbb{E}[U] = \mathbb{E}[V] = 0$ ; $U$ et $V$ sont des fonctions de $X$ seule et de $Y$ seule, donc indépendantes, et $\mathbb{E}[UV] = \mathbb{E}[U]\,\mathbb{E}[V] = 0$.
2. **[0,5]** $\mathbb{E}[UV \cdot U] = \mathbb{E}[U^2V] = \mathbb{E}[U^2]\,\mathbb{E}[V] = 0$, $\mathbb{E}[UV \cdot V] = \mathbb{E}[U]\,\mathbb{E}[V^2] = 0$, $\mathbb{E}[U \cdot V] = 0$ : les trois termes sont centrés, leurs covariances deux à deux sont ces espérances (multipliées par des constantes), toutes nulles. $\mathbb{V}(UV) = \mathbb{E}[U^2V^2] = \mathbb{E}[U^2]\,\mathbb{E}[V^2] = \sigma_X^2\sigma_Y^2$. L'indépendance sert à chaque factorisation $\mathbb{E}[g(X)\,h(Y)] = \mathbb{E}[g(X)]\,\mathbb{E}[h(Y)]$ (avec $g$ et $h$ des puissances).
3. **[0,5]** M16 §6 : la variance d'une somme de variables deux à deux **décorrélées** est la somme de leurs variances. Donc $\mathbb{V}(XY) = \mathbb{V}(UV) + \mu_Y^2\mathbb{V}(U) + \mu_X^2\mathbb{V}(V) = \sigma_X^2\sigma_Y^2 + \mu_Y^2\sigma_X^2 + \mu_X^2\sigma_Y^2$ (une constante ajoutée ne change pas la variance). Les deux derniers termes sont $\ge 0$ : $\mathbb{V}(XY) \ge \sigma_X^2\sigma_Y^2$. Égalité si et seulement si $\mu_Y\sigma_X = 0$ **et** $\mu_X\sigma_Y = 0$ : les deux variables sont centrées ($\mu_X = \mu_Y = 0$) ; ou les deux sont constantes ($\sigma_X = \sigma_Y = 0$) ; ou l'une est la constante 0 (par exemple $\sigma_X = 0$ et $\mu_X = 0$), l'autre quelconque.
4. **[0,5]** $\mathbb{E}[X] = 1{,}5$, $\mathbb{E}[X^2] = 2{,}5$, $\mathbb{V}(X) = 0{,}25$ ; $Y = 2/X$ vaut 2 ou 1 avec probabilité $\frac12$ chacun : $\mathbb{V}(Y) = 0{,}25$. Mais $XY = 2$ est constant : $\mathbb{V}(XY) = 0 < 0{,}0625 = \mathbb{V}(X)\,\mathbb{V}(Y)$. Les factorisations de l'étape 2 tombent : ici $U = X - 1{,}5$ et $V = -U$ (car $Y = 3 - X$ sur $\{1, 2\}$), donc $\mathbb{E}[UV] = -\mathbb{E}[U^2] = -0{,}25 \ne 0$, et les trois termes ne sont plus décorrélés.

**Grille de relecture.** (1) le développement et les espérances nulles ; (2) les trois covariances nulles, $\mathbb{V}(UV)$, et où sert l'indépendance ; (3) la règle des variables décorrélées citée, la formule, la positivité et **tous** les cas d'égalité ; (4) les trois variances et l'étape qui tombe. Le message de M16 : la variance d'un produit n'est pas le produit des variances, sauf si les deux moyennes sont nulles ; et ce découpage en trois morceaux décorrélés montre d'où viennent les deux termes en plus.

**Erreurs fréquentes** (deux sujets) : en A, oublier que la question 1 n'a besoin que d'un vecteur propre **réel**, écrire $\lVert \mathbf{M}\mathbf{x} \rVert^2 = \mathbf{x}^\top\mathbf{M}\mathbf{x}$ (sans le carré), oublier le cas $\mathbf{N}\mathbf{x} = \mathbf{0}$, ou chercher en 4 une valeur propre de module $\ge 1$ ; en B, affirmer les covariances nulles sans les calculer, oublier des cas d'égalité, ou chercher un contre-exemple avec des variables indépendantes.
**Remédiation** : A : M19.R1, M19.10, M12c.8, M12c.18, M12d.15 ; B : M16.R2, M16.6, M16.9, M16.11.

## CP4.9 — Corriger une copie : cinq erreurs 🐛 · 1,25 point

**Réponse de a)** : `"ACDGH"`. **[0,5]** (0,1 par lettre juste, −0,1 par lettre en trop, sans descendre sous 0)

b) Une ligne par erreur **[0,15 chacune]** :
- **(A)** $X^2$ et $Y$ sont indépendantes : $\mathbb{E}[X^2Y] = \mathbb{E}[X^2]\,\mathbb{E}[Y] = (\mathbb{V}(X) + \mathbb{E}[X]^2)\,\mathbb{E}[Y] = (1 + 4) \times 3 = 15$ : $\mathbb{E}[X^2]$ n'est pas $\mathbb{E}[X]^2$.
- **(C)** $\mathbf{J}_{\mathbf{f}}(\mathbf{p})$ est de forme $(2, 3)$ (une ligne par sortie) : $\mathbf{u}^\top\mathbf{J}_{\mathbf{f}}$ demande un $\mathbf{u}$ de $\mathbb{R}^2$ (une pondération des sorties) et rend une ligne de 3 coordonnées, dans $\mathbb{R}^3$, de la forme de l'entrée.
- **(D)** $\lVert \mathbf{X} \rVert_F^2 = \sum_{i, j} X_{ij}^2$ : la dérivée par rapport à $X_{ij}$ vaut $2X_{ij}$, le gradient est $2\mathbf{X}$.
- **(G)** Au pas optimal, le facteur est $\frac{\kappa - 1}{\kappa + 1}$ avec $\kappa = 9$ : $\frac{8}{10} = 0{,}8$, pas $\frac19$ (qui serait $\frac{1}{\kappa}$).
- **(H)** `keepdims=True` garde l'axe réduit, de longueur 1 : la forme est $(1, 3)$ ; c'est sans `keepdims` qu'elle vaut $(3,)$.

Les lignes justes : (B) $[x, y, 1]\,\mathbf{H} = [x + 3,\ y - 2,\ 1]$, et $\mathbf{H}^2$ a pour dernière ligne $[6, -4, 1]$ : deux translations s'ajoutent ; (E) avec $v = e^u$ et $y = u\,v$, $u$ a deux arêtes sortantes : $\bar{u} = \bar{y}\,v + \bar{v}\,e^u = \bar{y}\,e^u + \bar{y}\,u\,e^u$ ; (F) la valeur propre 5 donne une direction où $f$ monte à l'ordre 2, la valeur propre $-2$ une direction où elle descend : c'est un point selle, malgré la valeur propre nulle (elle n'empêche de conclure que quand les autres sont toutes de même signe).

**Erreurs fréquentes** : laisser passer (A) parce que les variables sont indépendantes ; laisser passer (C) en confondant $\mathbf{u}^\top\mathbf{J}$ et $\mathbf{J}\mathbf{v}$ ; croire (E) fausse en oubliant que les contributions s'additionnent ; croire (F) fausse à cause de la valeur propre nulle ; laisser passer (G) en confondant le facteur et $\frac{1}{\kappa}$.
**Remédiation** : M16.18, M17.21, M18.27, M19.26, M20.16.

## CP4.10 — Problème de synthèse : ajuster une loi exponentielle, du graphe de calcul au pas critique 🔗 · 2,25 points

**Réponses** : a) `4.625` · b) `[0.5, 0, -3]` · c) `[-2.5, -6.5]` · d) `[0.25, 0.65]` · e) `0.308` · f) `[0, 0.693]` · g) `[[17.25, 31.75], [31.75, 64.25]]` · h) `[1.249, 80.251]` · i) `0.0249`.

a) En $(0, 0)$, $u_i = 0$, $v_i = 1$, $r_i = 1 - y_i = (0{,}5 ;\ 0 ;\ -3)$ : $L = \frac12(0{,}25 + 0 + 9) = 4{,}625$. **[0,25]**
b) Dans l'ordre inverse : $\bar{L} = 1$, $\bar{r}_i = r_i$, $\bar{v}_i = \bar{r}_i$, puis $\bar{u}_i = \bar{v}_i\,e^{u_i} = r_iv_i$ : $(0{,}5 ;\ 0 ;\ -3)$. **[0,25]**
c) $a$ et $b$ servent à chaque $u_i$ : $\bar{a} = \sum_i \bar{u}_i = -2{,}5$ et $\bar{b} = \sum_i \bar{u}_i\,x_i = -0{,}5 + 0 - 6 = -6{,}5$. **[0,25]**
d) $(0, 0) - 0{,}1\,(-2{,}5 ;\ -6{,}5) = (0{,}25 ;\ 0{,}65)$. **[0,25]**
e) $u = 0{,}25 + 0{,}65\,x = (-0{,}4 ;\ 0{,}25 ;\ 1{,}55)$, $v = (0{,}670320 ;\ 1{,}284025 ;\ 4{,}711470)$, $r = (0{,}170320 ;\ 0{,}284025 ;\ 0{,}711470)$ : $L = \frac12(0{,}029009 + 0{,}080670 + 0{,}506190) \approx 0{,}308$. **[0,25]**
f) $\ln y = (-\ln 2 ;\ 0 ;\ 2\ln 2) = \ln 2 \times x$ : les mesures vérifient $y = e^{0 + x\ln 2} = 2^x$. Avec $a^\star = 0$ et $b^\star = \ln 2 \approx 0{,}693$, $L = 0$ ; comme $L \ge 0$ partout, c'est le minimum. **[0,25]**
g) $\frac{\partial L}{\partial a} = \sum_i r_iv_i$ et $\frac{\partial(r_iv_i)}{\partial a} = v_i \cdot v_i + r_i \cdot v_i$ : $\frac{\partial^2 L}{\partial a^2} = \sum_i v_i(v_i + r_i)$, $\frac{\partial^2 L}{\partial a\,\partial b} = \sum_i x_iv_i(v_i + r_i)$, $\frac{\partial^2 L}{\partial b^2} = \sum_i x_i^2v_i(v_i + r_i)$. En $(a^\star, b^\star)$, $r_i = 0$ et $v_i = y_i$ : $\sum y_i^2 = 0{,}25 + 1 + 16 = 17{,}25$, $\sum x_iy_i^2 = -0{,}25 + 0 + 32 = 31{,}75$, $\sum x_i^2y_i^2 = 0{,}25 + 0 + 64 = 64{,}25$. **[0,25]**
h) Trace $81{,}5$, déterminant $17{,}25 \times 64{,}25 - 31{,}75^2 = 1\,108{,}3125 - 1\,008{,}0625 = 100{,}25$ : $\lambda = 40{,}75 \pm \sqrt{40{,}75^2 - 100{,}25} = 40{,}75 \pm 39{,}5008$, soit $1{,}249$ et $80{,}251$. **[0,25]**
i) Près du minimum, $L$ est presque la forme quadratique de hessienne $\mathbf{H}$, et la descente de gradient y est une itération de Richardson (énoncé admis, M19 §4) : le pas critique est $\frac{2}{\lambda_{\max}} = \frac{2}{80{,}251} \approx 0{,}0249$. **[0,25]**

Sur ta copie :
- La hessienne générale est $\sum_i v_i^2\begin{pmatrix} 1 & x_i \\ x_i & x_i^2 \end{pmatrix} + \sum_i r_iv_i\begin{pmatrix} 1 & x_i \\ x_i & x_i^2 \end{pmatrix}$ ; le second terme contient les résidus, nuls en $(a^\star, b^\star)$ puisque l'ajustement est exact. Il reste le premier, une somme de matrices semi-définies positives.
- (Pour aller plus loin, non noté : les deux valeurs propres sont strictement positives, la hessienne est définie positive, $(a^\star, b^\star)$ est un minimum local strict, et global, puisque $L \ge 0 = L(a^\star, b^\star)$.)
- Avec $\eta = 0{,}1 > 0{,}0249$, les facteurs $1 - \eta\lambda$ valent $0{,}875$ et $1 - 8{,}025 = -7{,}025$ : près du minimum, l'écart le long de la direction raide est multiplié par environ $-7$ à chaque pas, la descente diverge. Le premier pas a fait baisser $L$ (de 4,625 à 0,308) parce que, loin du minimum, la courbure n'est pas la même : en $(0, 0)$, la hessienne vaut $\begin{pmatrix} 0{,}5 & -5{,}5 \\ -5{,}5 & -6{,}5 \end{pmatrix}$ (les résidus ne sont pas nuls ; elle n'est même pas définie positive). Le pas critique est une propriété **locale**, près du minimum. (En continuant avec $\eta = 0{,}1$, $L$ vaut 5,01, puis 0,158, puis 11, puis 403 : la descente diverge.)
- Pour aller plus loin (non noté) : le graphe a trois branches, une par mesure, qui se rejoignent en $L$, et $a$, $b$ servent trois fois chacun (leurs adjoints sont des sommes) ; $\kappa = \frac{80{,}251}{1{,}249} \approx 64$ : un pas qui converge est sous $0{,}0249$, et la direction lente, de courbure $1{,}249$, n'est alors réduite que d'un facteur au mieux $\frac{\kappa - 1}{\kappa + 1} \approx 0{,}969$ par pas : il faut environ 300 pas pour gagner 4 décimales.

**Erreurs fréquentes** : en a), oublier le $\frac12$ ; en b) et c), le signe des résidus, ou oublier les $x_i$ dans $\partial L / \partial b$ ; en d), monter au lieu de descendre ; en f), donner $b^\star = 2$ (le facteur de croissance au lieu de son logarithme) ; en g), garder le terme des résidus, calculer la hessienne en $(0, 0)$, ou utiliser $b^\star$ arrondi à 0,693 ($\lambda_{\max}$ devient environ 80,20) ; en i), $\frac{2}{\lambda_{\min}}$, ou le pas optimal $\frac{2}{\lambda_{\min} + \lambda_{\max}}$.
**Remédiation** : M18.2, M18.4, M18.9, M19.1, M19.2, M19.4, M19.5, M19.14.

## Barème récapitulatif et remédiation

| Question | Points | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP4.Q1 | 1,5 | M16 à M20 | les exercices cités au CP4.Q1, puis les quiz et les flashcards des chapitres concernés |
| CP4.1 | 2 | M16 | M16.2, M16.3, M16.4, M16.5, M16.12, M16.13, M16.14 |
| CP4.2 | 2 | M17 | M17.1, M17.2, M17.3, M17.5, M17.Q3, M17.Q5, M17.16 |
| CP4.3 | 2 | M18 | M18.1, M18.2, M18.3, M18.4, M18.5, M18.Q4, M18.Q5, M18.20 |
| CP4.4 | 1,75 | M18 | M18.6, M18.7, M18.8, M18.10, M18.Q6, M18.Q8, M18.22 |
| CP4.5 | 2 | M19 | M19.1, M19.2, M19.Q1, M19.Q2, M19.19 |
| CP4.6 | 1,75 | M19 | M19.3, M19.4, M19.5, M19.6, M19.7, M19.11, M19.12, M19.Q4, M19.Q6 |
| CP4.7 | 1,5 | M20 | M20.1, M20.2, M20.4, M20.11, M20.12, M20.Q2, M20.Q3 |
| CP4.8 | 2 | M19, M12c ou M16 | A : M19.R1, M19.10, M12c.8, M12c.18, M12d.15 ; B : M16.R2, M16.6, M16.9, M16.11 |
| CP4.9 | 1,25 | M16 à M20 | M16.18, M17.21, M18.27, M19.26, M20.16 |
| CP4.10 | 2,25 | M18, M19 | M18.2, M18.4, M18.9, M19.1, M19.2, M19.4, M19.5, M19.14 |
| **Total** | **20** | | |

**Lire ta note**
- **16 à 20** : la partie IV est solide. Passe au checkpoint IV de workbookIA ; garde les flashcards de la partie IV dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe au checkpoint IV de workbookIA.
- **8 à moins de 12** : avant le checkpoint IV de workbookIA, fais la remédiation, relis ta synthèse et les fiches des chapitres concernés.
- **Moins de 8** : reprends les exercices ★★ des chapitres où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
