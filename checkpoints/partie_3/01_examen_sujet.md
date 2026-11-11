# CP3 · Examen blanc de la partie III (M12a à M14)

| | |
|---|---|
| **Durée** | 110 minutes (environ 2 heures), d'une traite |
| **Note** | sur 20 points |
| **Chapitres** | M12a à M14 : espaces vectoriels, orthogonalité et QR, valeurs propres et Cholesky, SVD et ACP, vraisemblance et régression logistique, Lagrange et SVM, queues binomiales et poids exponentiels |
| **Ta copie** | `04_mes_reponses.md` (ta copie, dans `mon_travail/checkpoints/partie_3/`), ou une feuille de papier |
| **Après** | le notebook `02_examen_notebook.ipynb` vérifie tes réponses chiffrées ; `03_examen_corrige.md` donne le corrigé détaillé, le barème et la remédiation |

## Règles

- **Fiches, notes, flashcards, annexes et corrigés fermés.** Pas d'assistant IA, pas de recherche sur le web.
- **Calculatrice autorisée**, ou Python comme simple calculatrice (`+`, `*`, `/`, `**`, `math.sqrt`, `math.exp`, `math.log`, `math.log2`, `math.comb`) ; ni NumPy, ni SciPy, ni SymPy, ni `mymath`, ni les notebooks des chapitres.
- Donne le nombre de décimales demandé. **N'arrondis qu'à la fin** du calcul : enchaîne les calculs à la calculatrice, ou garde au moins 6 chiffres significatifs dans les résultats intermédiaires (4 décimales ne suffisent pas sous une racine carrée, dans une exponentielle ou avant une soustraction).
- Écris ta démarche : la moitié des points d'une question de calcul vont à la méthode. Quand une question dit « justifie », une réponse sans justification ne rapporte qu'une partie des points.
- Les durées sont indicatives : commence par ce que tu sais faire ; si tu bloques, passe à la question suivante et reviens-y à la fin.

| Question | Type | Sujet | Points | ⏱️ |
|---|---|---|---|---|
| CP3.Q1 | 🧠 | Dix affirmations sur la partie III : vrai ou faux | 1,5 | 10 min |
| CP3.1 | ✏️ | Indépendance, base, rang et noyau | 2 | 10 min |
| CP3.2 | ✏️ | Gram-Schmidt, projection et moindres carrés | 2 | 10 min |
| CP3.3 | ✏️ | Valeurs propres, matrice définie positive et Cholesky | 2 | 10 min |
| CP3.4 | ✏️ | SVD, rang faible et variance expliquée | 2 | 10 min |
| CP3.5 | ✏️ | Maximum de vraisemblance, log-loss et entropie | 1,75 | 9 min |
| CP3.6 | ✏️ | Lagrange, hinge loss et noyau | 1,75 | 9 min |
| CP3.7 | ✏️ | Queue binomiale et borne de Chernoff, limite et poids exponentiels | 1,5 | 8 min |
| CP3.8 | ∂ | Une démonstration courte, au choix parmi deux | 2 | 12 min |
| CP3.9 | 🐛 | Corriger une copie : cinq erreurs | 1,25 | 8 min |
| CP3.10 | 🔗 | Problème de synthèse : des données centrées, leurs axes principaux, un modèle sur les scores | 2,25 | 14 min |
| | | **Total** | **20** | **110 min** |

Le barème de chaque sous-question est entre crochets. Sauf mention contraire, une sous-question vaut 0,25 point ; une justification demandée « sur ta copie » compte dans les points de la sous-question à laquelle elle se rattache.

---

### CP3.Q1 — Dix affirmations sur la partie III : vrai ou faux 🧠 ★ ⏱️ 10 min · 1,5 point

Pour chaque affirmation, réponds **Vrai** ou **Faux**, puis justifie en une phrase : une règle, un calcul ou un contre-exemple. Chaque affirmation vaut 0,15 point : 0,05 pour le verdict, 0,1 pour la justification.

a) Si une colonne d'une matrice $\mathbf{X}$ de forme $(n, p)$ est une combinaison linéaire des autres colonnes, alors $\mathbf{X}^\top\mathbf{X}$ n'est pas définie positive.
b) Une matrice de projection orthogonale de $\mathbb{R}^4$ sur un sous-espace de dimension 2 a pour valeurs propres 1, 1, 0 et 0.
c) Toute matrice orthogonale de taille $2 \times 2$ a au moins une valeur propre réelle.
d) La matrice centrée $\mathbf{X}_c$ d'un nuage de points de $\mathbb{R}^2$ a pour valeurs singulières 5 et 2 : le premier axe principal explique environ 71 % de la variance du nuage.
e) Si deux exemples ont les mêmes features mais des labels différents, la log-loss moyenne d'une régression logistique sur ces données est strictement positive, quels que soient $\mathbf{w}$ et $b$.
f) Le minimum de $x^2 + y^2$ sous la contrainte $x + 2y = 5$ a un multiplicateur de Lagrange nul.
g) La matrice de Gram du noyau linéaire $k(\mathbf{x}, \mathbf{z}) = \mathbf{x} \cdot \mathbf{z}$ sur trois points distincts de $\mathbb{R}^2$ est inversible.
h) Pour $X$ de loi $\mathcal{B}(n ;\ 0{,}35)$, la probabilité $P(X \ge 0{,}45\,n)$ tend vers 0, quand $n \to +\infty$, plus vite que toute puissance de $\frac{1}{n}$.
i) Pour tout entier $n \ge 1$, $\left(1 - \frac{0{,}3}{n}\right)^n > e^{-0{,}3}$.
j) Avec l'algorithme Hedge et $\eta = 0{,}4$, un expert dont la loss cumulée dépasse de 5 celle du meilleur expert reçoit moins du cinquième du poids du meilleur.

### CP3.1 — Indépendance, base, rang et noyau ✏️ ★★ ⏱️ 10 min · 2 points

On note $\mathbf{c}_1, \ldots, \mathbf{c}_5$ les colonnes de la matrice

$$\mathbf{A} = \begin{pmatrix} 1 & 0 & 2 & 3 & -1 \\ 0 & 1 & -3 & 2 & 4 \\ 2 & -1 & 7 & 4 & -6 \end{pmatrix}.$$

Pour g) et h), $\mathbb{R}_2[X]$ est l'espace des polynômes de degré au plus 2, $V = \{P \in \mathbb{R}_2[X] : P(2) = P(-1)\}$ et $W = \{P \in V : P(0) = 0\}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le rang de $\mathbf{A}$ | un entier |
| b | la dimension du noyau de $\mathbf{A}$ | un entier |
| c | les réels $\alpha$ et $\beta$ tels que $\mathbf{c}_3 = \alpha\,\mathbf{c}_1 + \beta\,\mathbf{c}_2$ | la liste $[\alpha, \beta]$ |
| d | les coordonnées de $\mathbf{c}_5$ dans la base $(\mathbf{c}_1, \mathbf{c}_2)$ de l'image | une liste de 2 nombres |
| e | un vecteur $\mathbf{z} = (z_1, z_2, z_3)$ non nul tel que $\mathbf{A}^\top\mathbf{z} = \mathbf{0}$, avec $z_1 = 2$ | une liste de 3 nombres |
| f | le système $\mathbf{A}\mathbf{x} = (3, 1, 4)$ a-t-il au moins une solution ? | `True` ou `False` |
| g | la dimension de $W$ | un entier |
| h | les coordonnées de $P = 7 - 2X + 2X^2$ dans la base $(1,\ X^2 - X)$ de $V$ | une liste de 2 nombres |

Sur ta copie : nomme le théorème qui relie a) et b) ; pour f), dis comment le vecteur $\mathbf{z}$ de e) permet de répondre ; pour h), vérifie que $P$ est dans $V$ et justifie que $(1,\ X^2 - X)$ est une base de $V$.

### CP3.2 — Gram-Schmidt, projection et moindres carrés ✏️ ★★ ⏱️ 10 min · 2 points

Dans $\mathbb{R}^4$ : $\mathbf{v}_1 = (1, 1, 3, 5)$, $\mathbf{v}_2 = (6, 0, 10, 0)$ et $\mathbf{y} = (11, -6, 17, -4)$. La matrice $\mathbf{X} = [\mathbf{v}_1\ \mathbf{v}_2]$ a pour colonnes $\mathbf{v}_1$ et $\mathbf{v}_2$. Gram-Schmidt sur $(\mathbf{v}_1, \mathbf{v}_2)$ donne $\mathbf{q}_1, \mathbf{q}_2$ et la factorisation $\mathbf{X} = \mathbf{Q}\mathbf{R}$, où $\mathbf{Q} = [\mathbf{q}_1\ \mathbf{q}_2]$ a des colonnes orthonormées et $\mathbf{R}$ est triangulaire supérieure à diagonale positive. On cherche $\hat{\mathbf{x}}$ qui rend $\lVert \mathbf{y} - \mathbf{X}\mathbf{x} \rVert$ le plus petit possible.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert \mathbf{v}_1 \rVert$ | un nombre |
| b | le coefficient $r_{12} = \mathbf{q}_1 \cdot \mathbf{v}_2$ | un nombre |
| c | le vecteur $\mathbf{v}_2 - r_{12}\,\mathbf{q}_1$, avant normalisation | une liste de 4 nombres |
| d | la matrice $\mathbf{R}$, ligne par ligne | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| e | le vecteur $\mathbf{Q}^\top\mathbf{y}$ | une liste de 2 nombres |
| f | la projection orthogonale $\hat{\mathbf{y}} = \mathbf{Q}\mathbf{Q}^\top\mathbf{y}$ de $\mathbf{y}$ sur le plan engendré par $\mathbf{v}_1$ et $\mathbf{v}_2$ | une liste de 4 nombres |
| g | la solution $\hat{\mathbf{x}}$ de $\mathbf{R}\hat{\mathbf{x}} = \mathbf{Q}^\top\mathbf{y}$ | une liste de 2 nombres |
| h | $\lVert \mathbf{y} - \hat{\mathbf{y}} \rVert^2$ | un nombre |

Sur ta copie : vérifie que $\hat{\mathbf{y}} = \mathbf{X}\hat{\mathbf{x}}$, puis que $\lVert \mathbf{y} \rVert^2 = \lVert \hat{\mathbf{y}} \rVert^2 + \lVert \mathbf{y} - \hat{\mathbf{y}} \rVert^2$.

### CP3.3 — Valeurs propres, matrice définie positive et Cholesky ✏️ ★★ ⏱️ 10 min · 2 points

$$\mathbf{S} = \begin{pmatrix} 11 & 15 \\ 15 & 27 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 9 & 3 & -6 \\ 3 & 5 & 0 \\ -6 & 0 & 9 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\mathbf{S}$, dans l'ordre croissant | une liste de 2 nombres |
| b | le vecteur propre unitaire de $\mathbf{S}$ pour sa plus grande valeur propre, de première coordonnée positive | une liste (4 décimales) |
| c | la plus grande valeur propre de $\mathbf{S}^{-1}$ | un nombre |
| d | le rang de $\mathbf{S} - 2\mathbf{I}$ | un entier |
| e | le facteur de Cholesky $\mathbf{L}$ de $\mathbf{B}$ (triangulaire inférieur, diagonale positive, $\mathbf{B} = \mathbf{L}\mathbf{L}^\top$), ligne par ligne | une liste de 3 listes |
| f | $\det \mathbf{B}$, à partir de e) | un nombre |
| g | $\mathbf{x}^\top\mathbf{B}\mathbf{x}$ pour $\mathbf{x} = (1, -1, 1)$, calculé comme $\lVert \mathbf{L}^\top\mathbf{x} \rVert^2$ | un nombre |
| h | l'ensemble des réels $a$ pour lesquels $\begin{pmatrix} 2 & a \\ a & 8 \end{pmatrix}$ est définie positive | un intervalle, écrit comme `"]-1 ; 2["` |

Sur ta copie, pour e) : vérifie ton facteur en recalculant une ligne de $\mathbf{L}\mathbf{L}^\top$.

### CP3.4 — SVD, rang faible et variance expliquée ✏️ ★★ ⏱️ 10 min · 2 points

$$\mathbf{A} = \begin{pmatrix} 9 & 6 \\ 2 & -6 \end{pmatrix} = s_1\,\mathbf{u}_1\mathbf{v}_1^\top + s_2\,\mathbf{u}_2\mathbf{v}_2^\top \qquad (s_1 \ge s_2 \ge 0,\ \text{SVD}).$$

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice $\mathbf{A}^\top\mathbf{A}$, ligne par ligne | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| b | les valeurs singulières $[s_1, s_2]$ | une liste de 2 nombres |
| c | le vecteur singulier à droite $\mathbf{v}_1$, unitaire, de première coordonnée positive | une liste (3 décimales) |
| d | $\mathbf{u}_1 = \frac{\mathbf{A}\mathbf{v}_1}{s_1}$ | une liste (3 décimales) |
| e | la solution de $\mathbf{A}\mathbf{x} = (99, -22)$, en écrivant $(99, -22)$ à l'aide de $\mathbf{u}_1$ | une liste de 2 nombres |
| f | l'erreur $\lVert \mathbf{A} - \mathbf{A}_1 \rVert_F$ de la meilleure approximation de rang 1, $\mathbf{A}_1 = s_1\,\mathbf{u}_1\mathbf{v}_1^\top$ | un nombre |
| g | la part de $\lVert \mathbf{A} \rVert_F^2$ gardée par $\mathbf{A}_1$ | un nombre (3 décimales) |
| h | le conditionnement $\kappa_2(\mathbf{A})$ | un nombre (3 décimales) |

Sur ta copie : vérifie que $\lvert \det \mathbf{A} \rvert = s_1 s_2$.

### CP3.5 — Maximum de vraisemblance, log-loss et entropie ✏️ ★★ ⏱️ 9 min · 1,75 point

Quatre petites situations.

1. Un générateur tire des nombres indépendamment selon la loi uniforme sur $[0, \theta]$, où $\theta$ est inconnu. Six tirages : 3,2 ; 0,7 ; 6,1 ; 4,4 ; 2,9 ; 5,3.
2. Une variable $X$ prend les valeurs 0, 1 et 2 avec $P(X = 0) = \theta$, $P(X = 1) = 2\theta$ et $P(X = 2) = 1 - 3\theta$, où $0 < \theta < \frac{1}{3}$. Sur 30 observations indépendantes : 4 fois 0, 10 fois 1 et 16 fois 2.
3. Une variable $Y$ prend quatre valeurs, avec les probabilités $\mathbf{p} = (0{,}4 ;\ 0{,}25 ;\ 0{,}2 ;\ 0{,}15)$ ; $\mathbf{u}$ est la loi uniforme sur ces quatre valeurs.
4. Une régression logistique donne les scores $z = \mathbf{w} \cdot \mathbf{x} + b$ de cinq exemples : 1,3 ; −1,2 ; −0,5 ; 2,2 ; 0,9, pour les labels 1, 0, 1, 1, 0. On note $s(z) = \ln(1 + e^z)$ la softplus.

| | Question | Réponse attendue |
|---|---|---|
| a | (situation 1) l'estimation du maximum de vraisemblance de $\theta$ | un nombre |
| b | (situation 2) l'estimation du maximum de vraisemblance de $\theta$ | une fraction irréductible, comme `"3/8"` |
| c | (situation 3) l'entropie $H(\mathbf{p})$, en bits | un nombre (3 décimales) |
| d | (situation 3) l'indice de Gini de $\mathbf{p}$ | un nombre (3 décimales) |
| e | (situation 3) la divergence $\mathrm{KL}(\mathbf{p} \Vert \mathbf{u})$, en bits | un nombre (3 décimales) |
| f | (situation 4) la log-loss moyenne, en nats, calculée terme à terme comme $s(z) - yz$ | un nombre (3 décimales) |
| g | (situation 4) la plus petite log-loss moyenne (en nats) que peut atteindre un modèle qui annonce la **même** probabilité $q$ pour les cinq exemples | un nombre (3 décimales) |

Sur ta copie : pour a), écris la vraisemblance $L(\theta)$ et explique pourquoi son maximum n'est pas en un point où sa dérivée s'annule ; pour g), donne le $q$ optimal.

### CP3.6 — Lagrange, hinge loss et noyau ✏️ ★★ ⏱️ 9 min · 1,75 point

1. On cherche le maximum de $f(x, y) = x + 2y$ sur l'ellipse $\frac{x^2}{8} + \frac{y^2}{2} = 1$. On pose $g(x, y) = \frac{x^2}{8} + \frac{y^2}{2} - 1$ et le lagrangien $\mathcal{L} = f + \lambda g$ (la convention de M13b : $\nabla f + \lambda \nabla g = \mathbf{0}$).
2. Une SVM à marge souple a pour paramètres $\mathbf{w} = (2, 1)$, $b = -3$ et $C = 1$ ; son objectif est $J(\mathbf{w}, b) = \frac{1}{2}\lVert \mathbf{w} \rVert^2 + C\sum_i \max\big(0,\ 1 - y_i(\mathbf{w} \cdot \mathbf{x}_i + b)\big)$, sur trois exemples : $P_1 = (1, 3)$ de label $+1$, $P_2 = (2, 0)$ de label $-1$, $P_3 = (1 ;\ 0{,}5)$ de label $+1$.
3. On se demande si $k(x, z) = (x + z)^2$, pour $x, z \in \mathbb{R}$, est un noyau. On prend les trois points 1, 2 et 3.

| | Question | Réponse attendue |
|---|---|---|
| a | (1) le point où le maximum est atteint | la liste $[x, y]$ |
| b | (1) la valeur du maximum | un nombre |
| c | (1) le multiplicateur $\lambda$ en ce point | un nombre |
| d | (2) la somme des trois hinge losses | un nombre |
| e | (2) la valeur de $J(\mathbf{w}, b)$ | un nombre |
| f | (2) un sous-gradient de $J$ en $(\mathbf{w}, b)$ | la liste $[g_{w_1}, g_{w_2}, g_b]$ |
| g | (3) $\mathbf{v}^\top\mathbf{K}\mathbf{v}$ pour $\mathbf{v} = (2, -1, 0)$, où $\mathbf{K}$ est la matrice de Gram de $k$ sur les trois points | un nombre |

Sur ta copie : pour a), pourquoi le maximum existe et comment tu choisis entre les candidats ; pour g), ce que tu conclus sur $k$, et pourquoi.

### CP3.7 — Queue binomiale et borne de Chernoff, limite et poids exponentiels ✏️ ★★ ⏱️ 8 min · 1,5 point

Un logiciel de transcription automatique transcrit une phrase de 18 mots ; chaque mot est mal transcrit avec la probabilité 0,06, indépendamment des autres. $X$ est le nombre de mots mal transcrits. Pour b) et c), $n = 18$, $p = 0{,}06$ et $a = \frac{5}{18}$ ; la KL est en nats.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X \ge 5)$ | un nombre (5 décimales) |
| b | l'exposant $n\,\mathrm{KL}(a \Vert p)$ de la borne de Chernoff $P(X \ge 5) \le e^{-n\,\mathrm{KL}(a \Vert p)}$ | un nombre (3 décimales) |
| c | la borne de Hoeffding $e^{-2n(a - p)^2}$ de $P(X \ge 5)$ | un nombre (3 décimales) |
| d | $\left(1 - \frac{2{,}4}{45}\right)^{45}$ | un nombre (4 décimales) |
| e | l'écart des logarithmes entre d) et sa limite $e^{-2{,}4}$, c'est-à-dire $45\ln\left(1 - \frac{2{,}4}{45}\right) + 2{,}4$ | un nombre (4 décimales) |
| f | l'algorithme Hedge suit $K = 4$ experts avec $\eta = 0{,}7$ ; avant le tour qui vient, leurs losses cumulées valent $(3, 1, 2, 2)$. Les poids normalisés (de somme 1) des quatre experts | une liste (4 décimales) |

Sur ta copie : calcule le rapport $\frac{\mathrm{KL}(a \Vert p)}{2(a - p)^2}$ des exposants de Chernoff et de Hoeffding (par mot), et dis ce qu'il montre sur les deux bornes.

### CP3.8 — Une démonstration courte, au choix parmi deux ∂ ★★★ ⏱️ 12 min · 2 points

Traite **un seul** des deux sujets. Rédige en phrases : ce que tu supposes, chaque étape et la règle qui la justifie, ce que tu conclus.

**Sujet A — Le système de Lagrange d'un problème quadratique est inversible.** On minimise $\frac{1}{2}\mathbf{x}^\top\mathbf{Q}\mathbf{x} + \mathbf{c}^\top\mathbf{x}$ sous $\mathbf{A}\mathbf{x} = \mathbf{b}$, où $\mathbf{Q}$ est symétrique définie positive de taille $n \times n$ et $\mathbf{A}$ de forme $(m, n)$, de rang $m$. On pose $\mathbf{M} = \begin{pmatrix} \mathbf{Q} & \mathbf{A}^\top \\ \mathbf{A} & \mathbf{0} \end{pmatrix}$, de taille $(n + m) \times (n + m)$.
1. Avec le lagrangien $\frac{1}{2}\mathbf{x}^\top\mathbf{Q}\mathbf{x} + \mathbf{c}^\top\mathbf{x} + \boldsymbol{\lambda}^\top(\mathbf{A}\mathbf{x} - \mathbf{b})$, montre que les conditions de Lagrange s'écrivent $\mathbf{M}\begin{pmatrix} \mathbf{x} \\ \boldsymbol{\lambda} \end{pmatrix} = \begin{pmatrix} -\mathbf{c} \\ \mathbf{b} \end{pmatrix}$. **[0,5]**
2. Soit $(\mathbf{u}, \boldsymbol{\mu})$, avec $\mathbf{u} \in \mathbb{R}^n$ et $\boldsymbol{\mu} \in \mathbb{R}^m$, tel que $\mathbf{M}\begin{pmatrix} \mathbf{u} \\ \boldsymbol{\mu} \end{pmatrix} = \mathbf{0}$. Montre que $\mathbf{A}\mathbf{u} = \mathbf{0}$, puis que $\mathbf{u}^\top\mathbf{Q}\mathbf{u} = 0$. **[0,5]**
3. Déduis-en $\mathbf{u} = \mathbf{0}$, puis $\boldsymbol{\mu} = \mathbf{0}$ (dis à quoi sert le rang de $\mathbf{A}$), et conclus : $\mathbf{M}$ est inversible et le système de Lagrange a une solution unique. **[0,5]**
4. L'hypothèse « $\mathbf{Q}$ définie positive » ne peut pas être remplacée par « $\mathbf{Q}$ semi-définie positive ». Avec $n = 2$, $m = 1$ et $\mathbf{Q} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ : pour $\mathbf{A} = (1\ \ 0)$, donne un vecteur non nul du noyau de $\mathbf{M}$ ; pour $\mathbf{A} = (0\ \ 1)$, montre que $\mathbf{M}$ est inversible. Dis ce qui, dans la démonstration, distingue les deux cas. **[0,5]**

**Sujet B — Les poids de Hedge minimisent une loss régularisée par l'entropie.** $K$ experts ont des losses cumulées $L_1, \ldots, L_K$ ; $\eta > 0$. Sur l'ensemble $\Delta = \{\mathbf{w} \in \mathbb{R}^K : w_k > 0 \text{ pour tout } k,\ \sum_k w_k = 1\}$, on pose
$$F(\mathbf{w}) = \eta \sum_{k=1}^K w_k L_k + \sum_{k=1}^K w_k \ln w_k .$$
1. Écris le lagrangien de la contrainte $\sum_k w_k = 1$ (sans t'occuper de la positivité), et montre que son unique point critique est $w_k = \frac{e^{-\eta L_k}}{\sum_j e^{-\eta L_j}}$ : les poids de Hedge. **[0,5]**
2. Montre que $F$ est strictement convexe sur $\Delta$ (calcule sa hessienne), que $\Delta$ est convexe, et déduis-en que ce point est l'unique minimum de $F$ sur $\Delta$ ; cite le résultat de M13b que tu utilises. **[0,5]**
3. Montre que la valeur du minimum est $m(\eta) = -\ln \sum_{k=1}^K e^{-\eta L_k}$. **[0,5]**
4. On note $L_{\min} = \min_k L_k$. Montre que $\eta L_{\min} - \ln K \le m(\eta) \le \eta L_{\min}$, puis interprète $\frac{m(\eta)}{\eta}$ : de quelle quantité est-elle proche, et à quelle distance au plus ? **[0,5]**

### CP3.9 — Corriger une copie : cinq erreurs 🐛 ★★ ⏱️ 8 min · 1,25 point

Voici huit lignes extraites de la copie d'un élève. **Cinq** sont fausses.

- **(A)** Avec $\mathbf{u} = (1, 2, 0)$, $\mathbf{v} = (3, 1)$, $\mathbf{w} = (2, 4, 0)$ et $\mathbf{z} = (0, 1)$, la matrice $\mathbf{u}\mathbf{v}^\top + \mathbf{w}\mathbf{z}^\top$, de forme $(3, 2)$, est de rang 2 : c'est la somme de deux matrices de rang 1.
- **(B)** Pour toute matrice carrée inversible $\mathbf{A}$, $\kappa_2(\mathbf{A}^{-1}) = \kappa_2(\mathbf{A})$.
- **(C)** La projection orthogonale de $\mathbf{v} = (2, 1, 0)$ sur la droite dirigée par $\mathbf{a} = (1, 1, 1)$ est $(\mathbf{a} \cdot \mathbf{v})\,\mathbf{a} = (3, 3, 3)$.
- **(D)** $\begin{pmatrix} 3 & 5 \\ 0 & 1 \end{pmatrix}$ a pour valeurs propres 3 et 1, $\begin{pmatrix} 2 & 0 \\ 5 & 4 \end{pmatrix}$ a pour valeurs propres 2 et 4 ; leur somme a donc pour valeurs propres $3 + 4 = 7$ et $1 + 2 = 3$, et $7 + 3 = 10$ est bien sa trace.
- **(E)** Dans une régression logistique où le poids de $x_j$ vaut 0,7, augmenter $x_j$ de 1, les autres features fixées, multiplie la cote $\frac{p}{1 - p}$ par $e^{0{,}7} \approx 2{,}01$.
- **(F)** Un exemple de marge $y\,(\mathbf{w} \cdot \mathbf{x} + b) = 2$ a une hinge loss de $1 - 2 = -1$ : il fait baisser l'objectif de la SVM.
- **(G)** Pour $X$ de loi $\mathcal{B}(n ;\ 0{,}2)$, la borne de Chernoff de $P(X \ge 0{,}4\,n)$ vaut $e^{-n\,\mathrm{KL}(0{,}4 \Vert 0{,}2)}$, avec $\mathrm{KL}(0{,}4 \Vert 0{,}2) \approx 0{,}10465$ nat.
- **(H)** $\begin{pmatrix} 3 & 4 \\ 4 & 2 \end{pmatrix}$ est symétrique et tous ses coefficients sont positifs : elle est définie positive.

a) Les lettres des cinq lignes fausses, dans l'ordre alphabétique (un texte, comme `"ABCDE"`). **[0,5]**
b) Pour chaque ligne fausse, écris le résultat juste et la règle oubliée, en une ligne. **[0,75]** (0,15 par ligne)

### CP3.10 — Problème de synthèse : des données centrées, leurs axes principaux, un modèle sur les scores 🔗 ★★ ⏱️ 14 min · 2,25 points

Six exemples, trois features $(x_1, x_2, x_3)$ et une cible $y$ :

| exemple | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $x_1$ | 17 | 17 | 21 | 7 | 7 | 3 |
| $x_2$ | 13 | 1 | 6 | 3 | 15 | 10 |
| $x_3$ | 6 | 12 | 19 | 24 | 18 | 11 |
| $y$ | 18 | 18 | 27 | 20 | 24 | 13 |

Une ACP (données centrées, covariance avec $n - 1$) a rendu les trois axes principaux, orthonormés (tu n'as pas à le vérifier) :
$$\mathbf{u}_1 = \tfrac{1}{21}(19, -4, -8), \qquad \mathbf{u}_2 = \tfrac{1}{21}(4, -13, 16), \qquad \mathbf{u}_3 = \tfrac{1}{21}(8, 16, 11).$$
Le **score** de l'exemple $i$ sur l'axe $j$ est $t_{ij} = \mathbf{u}_j \cdot (\mathbf{x}_i - \bar{\mathbf{x}})$. Voici les scores des exemples 2 à 6 :

| exemple | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $t_1$ | ? | 7 | 7 | −7 | −7 | −7 |
| $t_2$ | ? | 3 | 6 | 9 | −3 | −6 |
| $t_3$ | ? | −5 | 4 | −1 | 5 | −4 |

La **régression sur composantes principales** à $k$ axes ajuste par les moindres carrés $\hat{y} = \bar{y} + w_1 t_1 + \cdots + w_k t_k$ : les features sont les scores des $k$ premiers axes.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne $\bar{\mathbf{x}}$ | une liste de 3 nombres |
| b | les scores $[t_{11}, t_{12}, t_{13}]$ de l'exemple 1 | une liste de 3 nombres |
| c | les variances des scores le long des trois axes (avec $n - 1$) | une liste (1 décimale) |
| d | la part de la variance totale gardée par les deux premiers axes | un nombre (3 décimales) |
| e | les poids $[w_1, w_2]$ de la régression sur les deux premiers axes | une liste (3 décimales) |
| f | le $R^2$ de cette régression à deux axes | un nombre (3 décimales) |
| g | le poids $w_3$ quand on ajoute le troisième axe | un nombre |
| h | le $R^2$ de la régression sur les trois axes | un nombre (3 décimales) |
| i | les prédictions, à deux axes puis à trois axes, pour le nouvel exemple $\mathbf{x} = (26, 5, 13)$ | une liste de 2 nombres |

Sur ta copie : pourquoi les équations normales sont-elles diagonales, et pourquoi $w_1$ et $w_2$ ne changent-ils pas en g) ? Que montrent d), f) et h) ensemble sur le choix des axes à garder ?

---

**Fin de l'examen.** Note l'heure, relis ta copie, puis passe à la vérification : le notebook `02_examen_notebook.ipynb` (ta copie), puis le corrigé `03_examen_corrige.md`.
