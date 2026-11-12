# CP4 · Examen blanc de la partie IV (M16 à M20)

| | |
|---|---|
| **Durée** | 110 minutes (environ 2 heures), d'une traite |
| **Note** | sur 20 points |
| **Chapitres** | M16 à M20 : applications affines, graphes et variance d'un produit, jacobiennes, graphes de calcul et gradients par rapport à une matrice, hessienne et convergence des itérations, tableaux à plusieurs axes et estimateur de Horvitz-Thompson |
| **Ta copie** | `04_mes_reponses.md` (dans `mon_travail/checkpoints/partie_4/`), ou une feuille de papier |
| **Après** | le notebook `02_examen_notebook.ipynb` vérifie tes réponses chiffrées ; `03_examen_corrige.md` donne le corrigé détaillé, le barème et la remédiation |

## Règles

- **Fiches, notes, flashcards, annexes et corrigés fermés.** Pas d'assistant IA, pas de recherche sur le web.
- **Calculatrice autorisée**, ou Python comme simple calculatrice (`+`, `*`, `/`, `**`, `math.sqrt`, `math.exp`, `math.log`) ; ni NumPy, ni SciPy, ni SymPy, ni `mymath`, ni les notebooks des chapitres. Quand une question nomme une fonction de NumPy (CP4.Q1, CP4.7, CP4.9), c'est à toi de calculer ce qu'elle rendrait.
- Donne le nombre de décimales demandé. **N'arrondis qu'à la fin** du calcul : enchaîne les calculs à la calculatrice, ou garde au moins 6 chiffres significatifs dans les résultats intermédiaires (4 décimales ne suffisent pas sous une racine carrée, dans une exponentielle ou avant une soustraction).
- Écris ta démarche : la moitié des points d'une question de calcul vont à la méthode. Quand une question dit « justifie », une réponse sans justification ne rapporte qu'une partie des points.
- Les durées sont indicatives : commence par ce que tu sais faire ; si tu bloques, passe à la question suivante et reviens-y à la fin.

| Question | Type | Sujet | Points | ⏱️ |
|---|---|---|---|---|
| CP4.Q1 | 🧠 | Dix affirmations sur la partie IV : vrai ou faux | 1,5 | 10 min |
| CP4.1 | ✏️ | Coordonnées homogènes, chemins d'un graphe et variance d'un produit | 2 | 10 min |
| CP4.2 | ✏️ | Jacobienne d'une composée et produit vecteur-jacobienne | 2 | 10 min |
| CP4.3 | ✏️ | Mode direct et mode inverse sur un graphe de calcul | 2 | 10 min |
| CP4.4 | ✏️ | Gradients par rapport à une matrice | 1,75 | 9 min |
| CP4.5 | ✏️ | Hessienne, Taylor d'ordre 2 et nature d'un point critique | 2 | 10 min |
| CP4.6 | ✏️ | Itération de Richardson et récurrence d'ordre 2 | 1,75 | 9 min |
| CP4.7 | ✏️ | Moments le long d'axes, einsum et estimateur de Horvitz-Thompson | 1,5 | 8 min |
| CP4.8 | ∂ | Une démonstration au choix : une matrice qui raccourcit les vecteurs, ou Var(XY) ≥ Var X · Var Y | 2 | 12 min |
| CP4.9 | 🐛 | Corriger une copie : cinq erreurs | 1,25 | 8 min |
| CP4.10 | 🔗 | Problème de synthèse : ajuster une loi exponentielle, du graphe de calcul au pas critique | 2,25 | 14 min |
| | | **Total** | **20** | **110 min** |

Le barème de chaque sous-question est entre crochets. Sauf mention contraire, une sous-question vaut 0,25 point ; une justification demandée « sur ta copie » compte dans les points de la sous-question à laquelle elle se rattache.

**Conventions de la partie IV.** Une jacobienne a une ligne par sortie et une colonne par entrée. Un gradient par rapport à une matrice $\mathbf{X}$ a la forme de $\mathbf{X}$ : son coefficient $(i, j)$ est $\partial f / \partial X_{ij}$. En coordonnées homogènes, un point du plan est une **ligne** $[x, y, 1]$ (M16) : $[\mathbf{x}, 1]\,\mathbf{H} = [f(\mathbf{x}), 1]$. Les axes d'un tableau sont numérotés à partir de 0.

---

### CP4.Q1 — Dix affirmations sur la partie IV : vrai ou faux 🧠 ★ ⏱️ 10 min · 1,5 point

Pour chaque affirmation, réponds **Vrai** ou **Faux**, puis justifie en une phrase : une règle, un calcul ou un contre-exemple. Chaque affirmation vaut 0,15 point : 0,05 pour le verdict, 0,1 pour la justification.

a) Pour $\mathbf{f} : \mathbb{R}^3 \to \mathbb{R}^2$ et $\mathbf{g} : \mathbb{R}^2 \to \mathbb{R}^3$ différentiables, la jacobienne de $\mathbf{g} \circ \mathbf{f}$ est une matrice $3 \times 3$ de déterminant nul en tout point.
b) Un graphe orienté à 6 sommets dont la matrice d'adjacence vérifie $\operatorname{tr}(\mathbf{A}^k) = 0$ pour $k = 1, \ldots, 6$ n'a pas de cycle.
c) Si la jacobienne de $\mathbf{f} : \mathbb{R}^2 \to \mathbb{R}^2$ a un déterminant nul en $\mathbf{p}$, alors $\mathbf{f}$ n'est injective sur aucun voisinage de $\mathbf{p}$.
d) Pour toute matrice carrée inversible $\mathbf{X}$, le gradient de $f(\mathbf{X}) = \det\mathbf{X}$ est $\mathbf{X}^{-\top}$.
e) $(0, 0)$ est un minimum local de $f(x, y) = (x - 2y)^2 + y^4$, alors que le test de la hessienne n'y permet pas de conclure.
f) Si $\mathbf{M}$ est symétrique de valeurs propres $0{,}9$ et 1, l'itération $\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$ peut, selon $\mathbf{c}$, n'avoir aucun point fixe, ou en avoir une infinité.
g) Si $\mathbf{A}$ est symétrique définie positive de valeurs propres 2 et 8, l'itération de Richardson a un pas critique plus grand pour $\mathbf{A} + 4\mathbf{I}$ que pour $\mathbf{A}$.
h) Si $\mathbf{T}$ est un tableau de forme $(6, 4, 5)$, `np.einsum("ijk->j", T)` et `T.mean(axis=(0, 2))` donnent le même tableau.
i) L'estimateur de Horvitz-Thompson d'un total reste sans biais quand l'échantillon a une taille fixée à l'avance, pourvu que chaque probabilité d'inclusion $\pi_i$ soit $> 0$.
j) Si $\operatorname{Cov}(X, Y) = 0$, alors $X^2$ et $Y^2$ sont décorrélées.

### CP4.1 — Coordonnées homogènes, chemins d'un graphe et variance d'un produit ✏️ ★★ ⏱️ 10 min · 2 points

1. Deux applications affines du plan : $f(x, y) = (2x - y + 1,\ x + 3)$ et $g(x, y) = (y - 2,\ -3x + y + 4)$. On applique $f$, puis $g$.
2. Un graphe orienté a 5 sommets et 8 arêtes, chacune avec un poids : $5 \to 4$ (poids 2), $5 \to 3$ ($-1$), $5 \to 2$ (1), $4 \to 2$ (3), $4 \to 1$ (1), $3 \to 2$ (2), $3 \to 1$ (4), $2 \to 1$ ($-2$). $\mathbf{A}$ est sa matrice d'adjacence ($A_{ij} = 1$ s'il y a une arête $i \to j$, 0 sinon) et $\mathbf{W}$ celle des poids ($W_{ij}$ = le poids de l'arête $i \to j$, 0 sinon). Le poids d'un chemin est le produit des poids de ses arêtes.
3. Une pompe remplit une citerne pendant une durée $T$ (en heures), avec un débit $D$ (en m³/h) ; le volume pompé est $V = DT$. $D$ et $T$ sont aléatoires et **indépendants** : $\mathbb{E}[D] = 5$ et $\sigma_D = 0{,}3$ ; $\mathbb{E}[T] = 1{,}5$ et $\sigma_T = 0{,}1$.

| | Question | Réponse attendue |
|---|---|---|
| a | (1) la matrice homogène $3 \times 3$ de $g \circ f$, ligne par ligne | une liste de 3 listes |
| b | (1) l'image du point $P = (-1, 3)$ par $g \circ f$ | une liste de 2 nombres |
| c | (1) la dernière ligne de la matrice homogène de $(g \circ f)^{-1}$ | une liste de 3 nombres |
| d | (2) le nombre de chemins de longueur 2 (de 2 arêtes) du sommet 5 au sommet 1 | un entier |
| e | (2) le plus petit entier $k \ge 1$ tel que $\mathbf{A}^k = \mathbf{0}$ | un entier |
| f | (2) la somme des poids de **tous** les chemins du sommet 5 au sommet 1 | un nombre |
| g | (3) le volume moyen $\mathbb{E}[V]$, en m³ | un nombre |
| h | (3) la variance du volume, $\mathbb{V}(V)$ | un nombre (4 décimales) |

Sur ta copie : pour c), vérifie que la réciproque renvoie l'image de b) sur $P$ ; pour f), le coefficient de quelle matrice donne cette somme ; pour h), compare avec $\mathbb{V}(D)\,\mathbb{V}(T)$.

### CP4.2 — Jacobienne d'une composée et produit vecteur-jacobienne ✏️ ★★ ⏱️ 10 min · 2 points

$\mathbf{f}(x, y) = (xy,\ x + 2y,\ e^{x + y})$, de $\mathbb{R}^2$ dans $\mathbb{R}^3$, et $\mathbf{g}(a, b, c) = (ac + b^2,\ b - a^2)$, de $\mathbb{R}^3$ dans $\mathbb{R}^2$, au point $\mathbf{p} = (2, -2)$. Pour h), $\boldsymbol{\varphi}(t_1, t_2, t_3) = (t_1^3,\ t_2^3,\ t_3^3)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{f}(\mathbf{p})$ | une liste de 3 nombres |
| b | $\mathbf{J}_{\mathbf{f}}(\mathbf{p})$, ligne par ligne | une liste de 3 listes |
| c | $\mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{p}))$, ligne par ligne | une liste de 2 listes |
| d | $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{p})$ | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| e | le produit vecteur-jacobienne $\mathbf{u}^\top\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{p})$, pour $\mathbf{u} = (1, -2)$ | une liste de 2 nombres |
| f | le nombre de multiplications de deux nombres (même par 0) pour calculer $\mathbf{u}^\top\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}$ à partir de $\mathbf{u}$, $\mathbf{J}_{\mathbf{g}}$ et $\mathbf{J}_{\mathbf{f}}$ : d'abord en calculant $(\mathbf{u}^\top\mathbf{J}_{\mathbf{g}})\,\mathbf{J}_{\mathbf{f}}$, puis en calculant $\mathbf{u}^\top(\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}})$ | une liste de 2 entiers |
| g | l'approximation linéaire de $(\mathbf{g} \circ \mathbf{f})(2{,}1 ;\ -2{,}05)$ | une liste de 2 nombres |
| h | la jacobienne de $\boldsymbol{\varphi} \circ \mathbf{f}$ en $\mathbf{p}$, ligne par ligne | une liste de 3 listes |

Sur ta copie : pour d), retrouve un coefficient comme une somme sur les trois variables intermédiaires ; pour e), dis de quelle fonction ce produit est le gradient ; pour g), la valeur exacte est environ $(-0{,}5257 ;\ -20{,}5330)$ : de quel ordre est l'écart, et pourquoi ?

### CP4.3 — Mode direct et mode inverse sur un graphe de calcul ✏️ ★★ ⏱️ 10 min · 2 points

$f(x, y) = x\,(x + y^2)\,\ln(x + y^2)$ se calcule par le graphe
$$v_1 = x + y^2, \qquad v_2 = x\,v_1, \qquad v_3 = \ln v_1, \qquad f = v_2\,v_3,$$
au point $(x, y) = (5, -2)$ (le carré $y^2$ est une opération à un argument, qui n'est pas un nœud à part). En mode direct, $\dot{v}$ est la tangente d'un nœud, avec la graine sur $x$ ($\dot{x} = 1$, $\dot{y} = 0$) ; en mode inverse, $\bar{v} = \partial f / \partial v$ est son adjoint, en partant de $\bar{f} = 1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $f(5, -2)$ | un nombre (4 décimales) |
| b | le nombre de chemins de $x$ à $f$ dans le graphe | un entier |
| c | les tangentes $[\dot{v}_1, \dot{v}_2, \dot{v}_3]$ (graine sur $x$) | une liste (4 décimales) |
| d | $\frac{\partial f}{\partial x}(5, -2)$, par le mode direct | un nombre (3 décimales) |
| e | les adjoints $[\bar{v}_3, \bar{v}_2]$ | une liste (4 décimales) |
| f | l'adjoint $\bar{v}_1$ | un nombre (4 décimales) |
| g | $\frac{\partial f}{\partial y}(5, -2)$, par le mode inverse | un nombre (4 décimales) |
| h | pour une application de $\mathbb{R}^6$ dans $\mathbb{R}^{25}$, le nombre de passages du mode direct, puis du mode inverse, qu'il faut pour obtenir toute sa jacobienne | une liste de 2 entiers |

Sur ta copie : dessine le graphe, avec la dérivée locale sur chaque arête ; calcule $\ln(9 + \varepsilon)$ avec les nombres duaux, et dis à quel nœud ce calcul correspond.

### CP4.4 — Gradients par rapport à une matrice ✏️ ★★ ⏱️ 9 min · 1,75 point

$$\mathbf{X} = \begin{pmatrix} 4 & 3 \\ 5 & 4 \end{pmatrix}, \quad \mathbf{a} = (3, -1), \quad \mathbf{b} = (2, 5), \quad \mathbf{A} = \begin{pmatrix} -1 & 4 \\ 2 & 1 \end{pmatrix}, \quad \mathbf{B} = \begin{pmatrix} 3 & 1 \\ -5 & 2 \end{pmatrix}.$$
Chaque gradient a la forme de $\mathbf{X}$ ; ses coefficients se donnent ligne par ligne.

| | Question | Réponse attendue |
|---|---|---|
| a | le gradient de $\mathbf{a}^\top\mathbf{X}\mathbf{b}$ | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| b | le gradient de $\operatorname{tr}(\mathbf{A}\mathbf{X})$ | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| c | le gradient de $\operatorname{tr}(\mathbf{X}^\top\mathbf{B}\mathbf{X})$, en ce $\mathbf{X}$ | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| d | le gradient de $\ln\det\mathbf{X}$, en ce $\mathbf{X}$ | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| e | l'approximation au premier ordre de $\ln\det(\mathbf{X} + \mathbf{H}) - \ln\det\mathbf{X}$, pour $\mathbf{H} = \begin{pmatrix} 0 & 0 \\ 0{,}05 & 0 \end{pmatrix}$ | un nombre |
| f | le gradient de $F(\mathbf{X}) = \frac{1}{4}\sum_{i=1}^4 \mathbf{z}_i^\top\mathbf{X}\mathbf{z}_i$, avec $\mathbf{z}_1 = (2, 1)$, $\mathbf{z}_2 = (0, 2)$, $\mathbf{z}_3 = (1, -1)$, $\mathbf{z}_4 = (1, 2)$ | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| g | le gradient de $\mathbf{a}^\top\mathbf{X}^\top\mathbf{X}\mathbf{b} = (\mathbf{X}\mathbf{a}) \cdot (\mathbf{X}\mathbf{b})$, en ce $\mathbf{X}$ | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |

Sur ta copie : pour c), pourquoi $\mathbf{B} + \mathbf{B}^\top$ et pas $2\mathbf{B}$ ; pour e), compare avec la valeur exacte (calcule $\det(\mathbf{X} + \mathbf{H})$) ; pour g), écris la différentielle $d(\mathbf{a}^\top\mathbf{X}^\top\mathbf{X}\mathbf{b})$ et lis le gradient dans $\operatorname{tr}(\mathbf{G}^\top d\mathbf{X})$.

### CP4.5 — Hessienne, Taylor d'ordre 2 et nature d'un point critique ✏️ ★★ ⏱️ 10 min · 2 points

$$f(x, y, z) = x^3 - 27x + 3y^2 + yz + 3z^2, \qquad P = (1, 1, -1), \qquad \mathbf{h} = (0{,}1 ;\ -0{,}1 ;\ 0{,}2).$$
On note $T_2$ le développement de Taylor d'ordre 2 de $f$ en $P$ : $T_2(P + \mathbf{h}) = f(P) + \nabla f(P) \cdot \mathbf{h} + \frac12\mathbf{h}^\top\mathbf{H}_f(P)\,\mathbf{h}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\nabla f(P)$ | une liste de 3 nombres |
| b | la hessienne $\mathbf{H}_f(P)$, ligne par ligne | une liste de 3 listes |
| c | $T_2(P + \mathbf{h})$ | un nombre |
| d | l'erreur $f(P + \mathbf{h}) - T_2(P + \mathbf{h})$ | un nombre |
| e | les points critiques de $f$, rangés par $x$ croissant | une liste de points $[x, y, z]$ |
| f | les valeurs propres de la hessienne au point critique d'abscisse $x > 0$, dans l'ordre croissant | une liste de 3 nombres |
| g | la nature de ce point critique : 1 minimum local, 2 maximum local, 3 point selle, 4 le test de la hessienne ne permet pas de conclure | un entier : 1, 2, 3 ou 4 |
| h | la nature de l'autre point critique, avec les mêmes numéros | un entier : 1, 2, 3 ou 4 |

Sur ta copie : pourquoi l'erreur d) vaut-elle exactement $h_1^3$ ? Pour h), donne les valeurs propres de la hessienne et une direction le long de laquelle $f$ descend depuis ce point.

### CP4.6 — Itération de Richardson et récurrence d'ordre 2 ✏️ ★★ ⏱️ 9 min · 1,75 point

1. On résout $\mathbf{A}\mathbf{x} = \mathbf{b}$, avec $\mathbf{A} = \begin{pmatrix} 7 & -4 \\ -4 & 7 \end{pmatrix}$ (de valeurs propres 3 et 11) et $\mathbf{b} = (-1, 10)$, par l'itération de Richardson $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega(\mathbf{b} - \mathbf{A}\mathbf{x}_k)$, depuis $\mathbf{x}_0 = \mathbf{0}$.
2. $(R_1)$ : $u_{k+2} = 0{,}2\,u_{k+1} + 0{,}48\,u_k$, avec $u_0 = 2$ et $u_1 = 0{,}2$. $(R_2)$ : $w_{k+2} = w_{k+1} - 0{,}41\,w_k$.

| | Question | Réponse attendue |
|---|---|---|
| a | (1) $\mathbf{x}_1$, pour $\omega = 0{,}1$ | une liste de 2 nombres |
| b | (1) $\mathbf{x}_2$, pour $\omega = 0{,}1$ | une liste de 2 nombres |
| c | (1) le pas critique : la borne supérieure des $\omega$ pour lesquels l'itération converge depuis tout départ | une fraction irréductible, comme `"3/8"` |
| d | (1) pour $\omega = 0{,}1$, le facteur $\max_i \lvert 1 - \omega\lambda_i \rvert$ par lequel la norme de l'erreur est au plus multipliée à chaque pas | un nombre |
| e | (1) au pas optimal $\omega^* = \frac{2}{\lambda_{\min} + \lambda_{\max}}$, l'erreur est multipliée à chaque pas par au plus $\frac{\kappa - 1}{\kappa + 1}$, où $\kappa = \frac{\lambda_{\max}}{\lambda_{\min}}$ : le plus petit nombre de pas $k$ qui garantit une erreur divisée par $10^4$ | un entier |
| f | (2) les racines du polynôme caractéristique de $(R_1)$, dans l'ordre croissant | une liste de 2 nombres |
| g | (2) le module des racines du polynôme caractéristique de $(R_2)$ | un nombre (4 décimales) |

Sur ta copie : la solution $\mathbf{x}^\star$ ; le terme général de $(R_1)$ et sa limite ; $(R_2)$ tend-elle vers 0 depuis tout départ, et comment ?

### CP4.7 — Moments le long d'axes, einsum et estimateur de Horvitz-Thompson ✏️ ★★ ⏱️ 8 min · 1,5 point

1. Un entrepôt a 2 bâtiments, 2 étages par bâtiment et 3 allées par étage. Le tableau `T`, de forme $(2, 2, 3)$, donne le nombre de palettes de chaque allée : `T[0] = [[4, 7, 1], [2, 4, 6]]` et `T[1] = [[3, 0, 6], [8, 1, 9]]` (`T[i, j, k]` : bâtiment `i`, étage `j`, allée `k`).
2. Une coopérative veut estimer la récolte totale de miel de ses 5 ruchers. Le rucher $i$ entre dans l'échantillon avec la probabilité $\pi_i$, indépendamment des autres (tirage de Poisson) ; $\hat Y = \sum_{i \in S} y_i / \pi_i$.

| rucher $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| récolte $y_i$ (kg) | 50 | 26 | 14 | 22 | 7 |
| $\pi_i$ | 1 | 0,65 | 0,35 | 0,55 | 0,1 |

| | Question | Réponse attendue |
|---|---|---|
| a | (1) la forme de `T.sum(axis=1)` | un texte, comme `"(4, 5)"` |
| b | (1) `T.mean(axis=(1, 2))` | une liste de 2 nombres |
| c | (1) `T.var(axis=1, ddof=1)` | une liste de 2 listes de 3 nombres |
| d | (1) `np.einsum("ijk,k->ij", T, w)`, avec `w = [1, -1, 2]` | une liste de 2 listes de 2 nombres |
| e | (2) l'estimation $\hat Y$ quand l'échantillon tiré est $S = \{1, 3, 5\}$ | un nombre |
| f | (2) la variance $\mathbb{V}(\hat Y)$ | un nombre |

Sur ta copie : pour c), pourquoi la variance de deux valeurs $a$ et $b$, avec `ddof=1`, vaut-elle $\frac{(a - b)^2}{2}$ ? Pour la situation 2, $\mathbb{E}[\hat Y]$, et quel rucher apporte la plus grande part de la variance, et pourquoi.

### CP4.8 — Une démonstration au choix ∂ ★★★ ⏱️ 12 min · 2 points

Traite **un seul** des deux sujets. Rédige en phrases : ce que tu supposes, chaque étape et la règle qui la justifie, ce que tu conclus.

**Sujet A — Une matrice symétrique qui raccourcit tous les vecteurs.** Une matrice carrée réelle $\mathbf{M}$ **raccourcit** les vecteurs si $\lVert \mathbf{M}\mathbf{x} \rVert < \lVert \mathbf{x} \rVert$ pour tout $\mathbf{x} \neq \mathbf{0}$ (norme euclidienne).
1. Montre que si $\mathbf{M}$ raccourcit les vecteurs, toute valeur propre **réelle** de $\mathbf{M}$ est dans $]-1, 1[$ (sans supposer $\mathbf{M}$ symétrique). **[0,5]**
2. Réciproquement, $\mathbf{M}$ est **symétrique**, de valeurs propres $\lambda_1, \ldots, \lambda_n$ toutes dans $]-1, 1[$. Écris $\lVert \mathbf{M}\mathbf{x} \rVert^2$ comme une forme quadratique en $\mathbf{x}$, donne les valeurs propres de la matrice symétrique qui y apparaît, et conclus avec le quotient de Rayleigh (M12c) que $\mathbf{M}$ raccourcit les vecteurs. **[0,5]**
3. $\mathbf{M}$ et $\mathbf{N}$ sont symétriques et raccourcissent les vecteurs. Montre que $\mathbf{M}\mathbf{N}$ raccourcit les vecteurs. Avec $\mathbf{M} = \begin{pmatrix} 0{,}8 & 0 \\ 0 & 0{,}2 \end{pmatrix}$ et $\mathbf{N} = \begin{pmatrix} 0{,}5 & 0{,}4 \\ 0{,}4 & 0{,}5 \end{pmatrix}$, calcule $\mathbf{M}\mathbf{N}$ : est-elle symétrique ? Que dit la question 1 de ses valeurs propres réelles ? **[0,5]**
4. Sans symétrie, la réciproque est fausse : pour $\mathbf{B} = \begin{pmatrix} 0{,}2 & 0 \\ 1{,}5 & 0{,}2 \end{pmatrix}$, donne les valeurs propres et un vecteur que $\mathbf{B}$ allonge. Calcule $\mathbf{B}^\top\mathbf{B}$, et dis quelle égalité de la question 2 n'est plus vraie. **[0,5]**

**Sujet B — La variance d'un produit dépasse le produit des variances.** $X$ et $Y$ sont deux variables aléatoires **indépendantes**, qui ont des moments d'ordre 2 ; on note $\mu_X = \mathbb{E}[X]$, $\sigma_X^2 = \mathbb{V}(X)$, de même pour $Y$, et $U = X - \mu_X$, $V = Y - \mu_Y$. On démontre $\mathbb{V}(XY) \ge \mathbb{V}(X)\,\mathbb{V}(Y)$ en découpant le produit en trois morceaux.
1. Montre que $XY - \mu_X\mu_Y = UV + \mu_Y\,U + \mu_X\,V$, et que les trois termes de droite sont d'espérance nulle. **[0,5]**
2. Montre que ces trois termes sont deux à deux décorrélés (calcule $\mathbb{E}[UV \cdot U]$, $\mathbb{E}[UV \cdot V]$ et $\mathbb{E}[U \cdot V]$), et que $\mathbb{V}(UV) = \sigma_X^2\sigma_Y^2$ ; dis où sert l'indépendance. **[0,5]**
3. Déduis-en $\mathbb{V}(XY) = \sigma_X^2\sigma_Y^2 + \mu_Y^2\sigma_X^2 + \mu_X^2\sigma_Y^2$ (cite la règle de M16 que tu utilises), puis $\mathbb{V}(XY) \ge \mathbb{V}(X)\,\mathbb{V}(Y)$, et trouve tous les cas d'égalité (des conditions sur $\mu_X$, $\mu_Y$, $\sigma_X$ et $\sigma_Y$). **[0,5]**
4. L'indépendance ne peut pas être retirée : $X$ suit la loi uniforme sur $\{1, 2\}$ et $Y = 2/X$. Calcule $\mathbb{V}(X)$, $\mathbb{V}(Y)$ et $\mathbb{V}(XY)$, et conclus. Dis quelle étape de la démonstration ne tient plus. **[0,5]**

### CP4.9 — Corriger une copie : cinq erreurs 🐛 ★★ ⏱️ 8 min · 1,25 point

Voici huit lignes extraites de la copie d'un élève. **Cinq** sont fausses.

- **(A)** $X$ et $Y$ sont indépendantes, avec $\mathbb{E}[X] = 2$, $\mathbb{V}(X) = 1$ et $\mathbb{E}[Y] = 3$ : $\mathbb{E}[X^2Y] = \mathbb{E}[X]^2\,\mathbb{E}[Y] = 12$.
- **(B)** En coordonnées homogènes (points en lignes), la translation de vecteur $(3, -2)$ du plan a pour matrice $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 3 & -2 & 1 \end{pmatrix}$ ; son carré est la matrice homogène de la translation de vecteur $(6, -4)$.
- **(C)** Pour $\mathbf{f} : \mathbb{R}^3 \to \mathbb{R}^2$, le produit vecteur-jacobienne $\mathbf{u}^\top\mathbf{J}_{\mathbf{f}}(\mathbf{p})$ prend un vecteur $\mathbf{u}$ de $\mathbb{R}^3$ et rend un vecteur de $\mathbb{R}^2$.
- **(D)** Le gradient de $\lVert \mathbf{X} \rVert_F^2 = \operatorname{tr}(\mathbf{X}^\top\mathbf{X})$ par rapport à $\mathbf{X}$ est $\mathbf{X}$.
- **(E)** Pour $y = u\,e^{u}$ avec $u = x^2$, le mode inverse donne $\bar{u} = \bar{y}\,(e^u + u\,e^u)$ : $u$ sert deux fois (dans le produit et dans l'exponentielle), et les deux contributions s'additionnent.
- **(F)** En un point critique où la hessienne a pour valeurs propres 5, 0 et $-2$, la fonction a un point selle.
- **(G)** Pour une matrice $\mathbf{A}$ symétrique définie positive de valeurs propres 1 et 9, l'itération de Richardson au pas optimal multiplie la norme de l'erreur au plus par $\frac19$ à chaque pas.
- **(H)** Pour un tableau `T` de forme $(4, 3)$, `T.mean(axis=0, keepdims=True)` a la forme $(3,)$.

a) Les lettres des cinq lignes fausses, dans l'ordre alphabétique (un texte, comme `"ABCDE"`). **[0,5]**
b) Pour chaque ligne fausse, écris le résultat juste et la règle oubliée, en une ligne. **[0,75]** (0,15 par ligne)

### CP4.10 — Problème de synthèse : ajuster une loi exponentielle, du graphe de calcul au pas critique 🔗 ★★ ⏱️ 14 min · 2,25 points

Une grandeur croît de façon exponentielle. On l'a mesurée trois fois :

| $x$ | $-1$ | 0 | 2 |
|---|---|---|---|
| $y$ | 0,5 | 1 | 4 |

On l'ajuste par le modèle $\hat y = e^{a + bx}$, en minimisant
$$L(a, b) = \frac12\sum_{i=1}^3 \left(e^{a + bx_i} - y_i\right)^2 .$$
Le graphe de calcul : $u_i = a + b\,x_i$, puis $v_i = e^{u_i}$, puis $r_i = v_i - y_i$, et $L = \frac12\sum_i r_i^2$. En mode inverse, $\bar{u}_i = \partial L / \partial u_i$.

| | Question | Réponse attendue |
|---|---|---|
| a | $L(0, 0)$ | un nombre |
| b | les adjoints $[\bar{u}_1, \bar{u}_2, \bar{u}_3]$ en $(a, b) = (0, 0)$ | une liste de 3 nombres |
| c | le gradient $\left[\frac{\partial L}{\partial a}, \frac{\partial L}{\partial b}\right]$ en $(0, 0)$ | une liste de 2 nombres |
| d | le point $[a_1, b_1]$ atteint par un pas de descente de gradient de pas $\eta = 0{,}1$ depuis $(0, 0)$ | une liste de 2 nombres |
| e | $L(a_1, b_1)$ | un nombre (3 décimales) |
| f | le minimum $(a^\star, b^\star)$ de $L$ : les trois mesures sont exactement sur une courbe du modèle | une liste (3 décimales) |
| g | la hessienne de $L$ en $(a^\star, b^\star)$, calculée avec les valeurs exactes (pas avec $b^\star$ arrondi) | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| h | les valeurs propres de cette hessienne, dans l'ordre croissant | une liste (3 décimales) |
| i | le pas critique de la descente de gradient près de $(a^\star, b^\star)$ | un nombre (4 décimales) |

Sur ta copie : écris la hessienne de $L$ en un point $(a, b)$ quelconque, et explique pourquoi une partie de ses termes disparaît en $(a^\star, b^\star)$. La descente de gradient de pas $0{,}1$ converge-t-elle près de $(a^\star, b^\star)$ ? Son premier pas a pourtant fait baisser $L$ : pourquoi n'est-ce pas contradictoire ?

---

**Fin de l'examen.** Note l'heure, relis ta copie, puis passe à la vérification : le notebook `02_examen_notebook.ipynb` (ta copie), puis le corrigé `03_examen_corrige.md`.
