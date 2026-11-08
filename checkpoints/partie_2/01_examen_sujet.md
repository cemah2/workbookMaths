# CP2 · Examen blanc de la partie II (M07 à M11)

| | |
|---|---|
| **Durée** | 117 minutes (environ 2 heures), d'une traite |
| **Note** | sur 20 points |
| **Chapitres** | M07 à M11 : vecteurs et géométrie de ℝⁿ, tests statistiques, matrices et systèmes, moindres carrés et régularisation, séparabilité et convexité, logique et inégalités de concentration |
| **Ta copie** | `04_mes_reponses.md` (ta copie, dans `mon_travail/checkpoints/partie_2/`), ou une feuille de papier |
| **Après** | le notebook `02_examen_notebook.ipynb` vérifie tes réponses chiffrées ; `03_examen_corrige.md` donne le corrigé détaillé, le barème et la remédiation |

## Règles

- **Fiches, notes, flashcards, annexes et corrigés fermés.** Pas d'assistant IA, pas de recherche sur le web.
- **Calculatrice autorisée**, ou Python comme simple calculatrice (`+`, `*`, `/`, `**`, `math.sqrt`, `math.exp`, `math.log`, `math.comb`) ; ni NumPy, ni SciPy, ni SymPy, ni `mymath`, ni les notebooks des chapitres.
- Donne le nombre de décimales demandé. **N'arrondis qu'à la fin** du calcul : garde au moins 4 décimales dans les calculs intermédiaires.
- Écris ta démarche : la moitié des points d'une question de calcul vont à la méthode. Quand une question dit « justifie », une réponse sans justification ne rapporte qu'une partie des points.
- Les durées sont indicatives : commence par ce que tu sais faire ; si tu bloques, passe à la question suivante et reviens-y à la fin.

| Question | Type | Sujet | Points | ⏱️ |
|---|---|---|---|---|
| CP2.Q1 | 🧠 | Dix affirmations sur la partie II : vrai ou faux | 1,5 | 10 min |
| CP2.1 | ✏️ | Normes, cosinus, projection et distance à un hyperplan | 1,75 | 10 min |
| CP2.2 | ✏️ | Un test binomial et un intervalle de Wilson | 1,75 | 10 min |
| CP2.3 | ✏️ | Comparaisons multiples, AIC et BIC | 1,5 | 8 min |
| CP2.4 | ✏️ | Pivot de Gauss, rang et inverse | 1,75 | 10 min |
| CP2.5 | ✏️ | Les équations normales d'un petit modèle, avec et sans ridge | 1,75 | 10 min |
| CP2.6 | ✏️ | Biais, variance et erreur quadratique d'un estimateur | 1,5 | 8 min |
| CP2.7 | ✏️ | Convexité, enveloppe convexe et marge | 1,5 | 8 min |
| CP2.8 | ✏️ | Markov, Tchebychev et Hoeffding | 1,5 | 9 min |
| CP2.9 | ∂ | Une démonstration courte, au choix parmi deux | 2 | 12 min |
| CP2.10 | 🐛 | Corriger une copie : cinq erreurs | 1,25 | 8 min |
| CP2.11 | 🔗 | Problème de synthèse : ajuster un modèle, mesurer son erreur, décider | 2,25 | 14 min |
| | | **Total** | **20** | **117 min** |

Le barème de chaque sous-question est entre crochets. Sauf mention contraire, une sous-question vaut 0,25 point ; une justification demandée « sur ta copie » compte dans les points de la sous-question à laquelle elle se rattache.

---

### CP2.Q1 — Dix affirmations sur la partie II : vrai ou faux 🧠 ★ ⏱️ 10 min · 1,5 point

Pour chaque affirmation, réponds **Vrai** ou **Faux**, puis justifie en une phrase : une règle, un calcul ou un contre-exemple. Chaque affirmation vaut 0,15 point : 0,05 pour le verdict, 0,1 pour la justification.

a) Si $\mathbf{u}$ et $\mathbf{v}$ sont deux vecteurs non nuls tels que $\mathbf{u} \cdot \mathbf{v} = 0$, alors $\lVert \mathbf{u} + \mathbf{v} \rVert = \lVert \mathbf{u} - \mathbf{v} \rVert$.
b) La similarité cosinus de deux vecteurs non nuls ne change pas quand on multiplie l'un d'eux par $-3$.
c) Une p-valeur de 0,03 veut dire que l'hypothèse nulle a une probabilité de 0,03 d'être vraie.
d) On fait 15 tests indépendants au seuil de 5 %, et l'hypothèse nulle de chacun est vraie : la probabilité d'obtenir au moins un faux positif dépasse $\frac{1}{2}$.
e) Si $\mathbf{A}$ est une matrice de forme $(3, 4)$, le système $\mathbf{A}\mathbf{x} = \mathbf{0}$ a une infinité de solutions.
f) Si $\mathbf{A}\mathbf{B} = \mathbf{A}\mathbf{C}$ avec $\mathbf{A}$ non nulle, alors $\mathbf{B} = \mathbf{C}$.
g) Dans une régression par moindres carrés avec ordonnée à l'origine, ajouter une feature ne peut pas faire baisser le $R^2$ d'entraînement.
h) Les features polynomiales de degré au plus 2 en 3 variables, constante comprise, sont au nombre de 9.
i) L'ensemble des points du plan situés à une distance au moins 1 de l'origine est convexe.
j) Une variable aléatoire $X \ge 0$ de moyenne 2 peut vérifier $P(X \ge 10) = 0{,}25$.

### CP2.1 — Normes, cosinus, projection et distance à un hyperplan ✏️ ★★ ⏱️ 10 min · 1,75 point

Dans $\mathbb{R}^4$, on pose $\mathbf{u} = (2, -1, 2, 4)$ et $\mathbf{v} = (3, 1, 0, 2)$. L'hyperplan $H$ a pour équation $x_1 - 2x_2 + 2x_3 + 4x_4 - 7 = 0$, c'est-à-dire $\mathbf{w} \cdot \mathbf{x} + b = 0$ avec $\mathbf{w} = (1, -2, 2, 4)$ et $b = -7$ ; le point $P$ a pour coordonnées $(2, 0, 1, 3)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les trois normes de $\mathbf{u}$ : $[\lVert \mathbf{u} \rVert_1, \lVert \mathbf{u} \rVert_2, \lVert \mathbf{u} \rVert_\infty]$ | une liste |
| b | le produit scalaire $\mathbf{u} \cdot \mathbf{v}$ | un nombre |
| c | la similarité cosinus de $\mathbf{u}$ et $\mathbf{v}$ | un nombre (3 décimales) |
| d | la projection orthogonale de $\mathbf{v}$ sur la droite dirigée par $\mathbf{u}$ | une liste (2 décimales) |
| e | la distance de $\mathbf{v}$ à cette droite | un nombre (3 décimales) |
| f | la distance signée de $P$ à $H$, $\frac{\mathbf{w} \cdot P + b}{\lVert \mathbf{w} \rVert}$ | un nombre |
| g | le point de $H$ le plus proche de $P$ | une liste (2 décimales) |

### CP2.2 — Un test binomial et un intervalle de Wilson ✏️ ★★ ⏱️ 10 min · 1,75 point

Le générateur aléatoire d'un jeu en ligne doit déclarer une partie « gagnante » avec la probabilité $p = \frac{1}{2}$, indépendamment d'une partie à l'autre. Sur 15 parties, 12 sont déclarées gagnantes. On note $K$ le nombre de parties gagnantes sur 15 ; l'hypothèse nulle est $H_0 : p = \frac{1}{2}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(K = 12)$ sous $H_0$ | un nombre (4 décimales) |
| b | la p-valeur unilatérale $P(K \ge 12)$ sous $H_0$ | un nombre (4 décimales) |
| c | la p-valeur bilatérale | un nombre (4 décimales) |
| d | au seuil de 5 %, avec le test bilatéral, rejette-t-on $H_0$ ? | `True` ou `False` |
| e | le plus petit nombre de parties gagnantes sur 15 qui fait rejeter $H_0$ au seuil de 5 % avec le test unilatéral ($H_1 : p > \frac{1}{2}$) | un entier |
| f | l'intervalle de Wilson à 95 % de $p$ (quantile $z = 1{,}96$) | la liste [bas, haut] (4 décimales) |
| g | la borne haute de l'intervalle de Wald à 95 % de $p$ | un nombre (4 décimales) |

Sur ta copie, pour g) : que dit cette borne, et pourquoi l'intervalle de Wilson est-il préférable ici ?

### CP2.3 — Comparaisons multiples, AIC et BIC ✏️ ★★ ⏱️ 8 min · 1,5 point

Une étude teste 12 features, une par une, pour savoir si chacune est liée à la cible. Ses 12 p-valeurs, rangées dans l'ordre croissant : 0,0008 ; 0,0039 ; 0,011 ; 0,018 ; 0,027 ; 0,044 ; 0,07 ; 0,13 ; 0,21 ; 0,38 ; 0,55 ; 0,83.

Ensuite, trois modèles sont ajustés sur les mêmes $n = 80$ exemples. Le modèle 1 a $k = 2$ paramètres et une log-vraisemblance maximale $\ln L = -152{,}3$ ; le modèle 2, $k = 4$ et $\ln L = -148{,}1$ ; le modèle 3, $k = 7$ et $\ln L = -145{,}9$.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de features significatives au seuil de 5 %, sans correction | un entier |
| b | le nombre de features significatives avec la correction de Bonferroni, pour un risque global de 5 % | un entier |
| c | la p-valeur ajustée de Bonferroni de la troisième plus petite p-valeur | un nombre (3 décimales) |
| d | les AIC des trois modèles | une liste (1 décimale) |
| e | les BIC des trois modèles | une liste (1 décimale) |
| f | le numéro du modèle choisi par l'AIC, puis par le BIC | la liste [AIC, BIC] |

### CP2.4 — Pivot de Gauss, rang et inverse ✏️ ★★ ⏱️ 10 min · 1,75 point

On résout le système $(S)$ par le pivot de Gauss, en éliminant d'abord $x$ ($L_2 \leftarrow L_2 - 2L_1$ et $L_3 \leftarrow L_3 + L_1$), puis $y$ dans la troisième ligne :

$$(S) \quad \begin{cases} x + 2y - z = 3 \\ 2x + 5y + z = 14 \\ -x + y + 4z = 9 \end{cases}$$

Ensuite : $\mathbf{B} = \begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix}$ et $\mathbf{C} = \begin{pmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 1 & 7 \\ 3 & 6 & 1 & 10 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la troisième ligne de la matrice augmentée $[\mathbf{A} \mid \mathbf{b}]$ de $(S)$ après l'élimination de $x$ | une liste de 4 nombres |
| b | la troisième ligne de la forme échelonnée, après l'élimination de $y$ | une liste de 4 nombres |
| c | la solution de $(S)$ | la liste $[x, y, z]$ |
| d | l'inverse de $\mathbf{B}$, ligne par ligne | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| e | la solution de $\mathbf{B}\mathbf{x} = (1, 2)$, avec d) | une liste de 2 nombres |
| f | le rang de $\mathbf{C}$ | un entier |
| g | la valeur de $k$ pour laquelle le système $x + 2y = 3$, $2x + ky = 7$ n'a aucune solution | un nombre |

### CP2.5 — Les équations normales d'un petit modèle, avec et sans ridge ✏️ ★★ ⏱️ 10 min · 1,75 point

Un modèle à deux features, sans ordonnée à l'origine, $\hat{y} = w_1 x_1 + w_2 x_2$, est ajusté sur quatre exemples :

$$\mathbf{X} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 2 \\ 2 & 1 \end{pmatrix}, \qquad \mathbf{y} = \begin{pmatrix} 2 \\ 3 \\ 4 \\ 3 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice $\mathbf{X}^\top\mathbf{X}$, ligne par ligne | la liste $[[\cdot, \cdot], [\cdot, \cdot]]$ |
| b | le vecteur $\mathbf{X}^\top\mathbf{y}$ | une liste de 2 nombres |
| c | les poids $\mathbf{w}$ des moindres carrés | une liste (4 décimales) |
| d | le vecteur des résidus $\mathbf{r} = \mathbf{y} - \mathbf{X}\mathbf{w}$ | une liste (4 décimales) |
| e | la somme des carrés des résidus (SCR) | un nombre (4 décimales) |
| f | les poids ridge pour $\lambda = 3$ (on minimise $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 + \lambda \lVert \mathbf{w} \rVert^2$, les deux poids pénalisés) | une liste (4 décimales) |
| g | la SCR d'entraînement du modèle ridge de f) | un nombre (2 décimales) |

Sur ta copie : vérifie avec d) que $\mathbf{X}^\top\mathbf{r} = \mathbf{0}$, et dis pourquoi g) est plus grand que e).

### CP2.6 — Biais, variance et erreur quadratique d'un estimateur ✏️ ★★ ⏱️ 8 min · 1,5 point

On observe $n = 8$ essais indépendants qui réussissent chacun avec la probabilité $p$ ; $K$ est le nombre de succès. Deux estimateurs de $p$ : $\hat{p} = \frac{K}{n}$ et $\tilde{p} = \frac{K + 1}{n + 2}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le biais de $\tilde{p}$ quand $p = 0{,}2$ | un nombre (2 décimales) |
| b | la variance de $\tilde{p}$ quand $p = 0{,}2$ | un nombre (4 décimales) |
| c | l'erreur quadratique moyenne de $\tilde{p}$ quand $p = 0{,}2$ | un nombre (4 décimales) |
| d | l'erreur quadratique moyenne de $\hat{p}$ quand $p = 0{,}2$ | un nombre (4 décimales) |
| e | l'erreur quadratique moyenne de $\tilde{p}$ quand $p = 0{,}05$ | un nombre (4 décimales) |
| f | quand $p = 0{,}05$, l'estimateur de plus petite erreur quadratique moyenne : 1. $\hat{p}$ ; 2. $\tilde{p}$ | le numéro 1 ou 2 |

Sur ta copie : la formule de l'erreur quadratique moyenne en fonction du biais et de la variance, et ce que montrent c), d) et f) ensemble.

### CP2.7 — Convexité, enveloppe convexe et marge ✏️ ★★ ⏱️ 8 min · 1,5 point

Six points du plan : $(0, 0)$, $(4, 0)$, $(5, 3)$, $(2, 5)$, $(1, 2)$, $(3, 2)$. Pour d) à f), deux nuages labellisés : la classe $+1$, $\{(4, 4), (5, 6), (6, 4)\}$, et la classe $-1$, $\{(1, 1), (2, 3), (0, 3)\}$. La marge géométrique d'un séparateur $(\mathbf{w}, b)$ est $\min_i \frac{y_i\,(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$.

| | Question | Réponse attendue |
|---|---|---|
| a | les sommets de l'enveloppe convexe des six points, dans le sens direct (contraire des aiguilles d'une montre), en partant de $(0, 0)$ | la liste $[[x, y], \ldots]$ |
| b | l'aire de cette enveloppe | un nombre |
| c | le point $(1, 3)$ est-il dans l'enveloppe ? (justifie sur ta copie par un calcul) | `True` ou `False` |
| d | la marge géométrique du séparateur $\mathbf{w} = (1, 1)$, $b = -6{,}5$ | un nombre (3 décimales) |
| e | la plus grande marge possible entre les deux nuages | un nombre (3 décimales) |
| f | le séparateur de marge maximale, écrit sous forme canonique ($\min_i y_i\,(\mathbf{w} \cdot \mathbf{x}_i + b) = 1$) | la liste $[w_1, w_2, b]$ |

### CP2.8 — Markov, Tchebychev et Hoeffding ✏️ ★★ ⏱️ 9 min · 1,5 point

Le temps de réponse $T$ d'un service, en millisecondes, est positif, de moyenne 120 et d'écart-type 30. Pour d) à f), un modèle est évalué sur des exemples de test tirés indépendamment ; chaque exemple vaut 1 s'il est mal classé, 0 sinon, et $\hat{p}$ est le taux d'erreur observé, une estimation du vrai taux $p$.

| | Question | Réponse attendue |
|---|---|---|
| a | la borne de Markov sur $P(T \ge 300)$ | un nombre |
| b | la borne de Tchebychev sur $P(T \ge 300)$ | un nombre (4 décimales) |
| c | le plus petit nombre $n$ de mesures indépendantes de $T$ pour lequel Tchebychev garantit que leur moyenne $\bar{T}$ vérifie $P(\lvert \bar{T} - 120 \rvert \ge 5) \le 0{,}05$ | un entier |
| d | avec $n = 1\,200$ exemples de test et $\delta = 0{,}02$, le rayon de Hoeffding (bilatéral) du taux d'erreur | un nombre (4 décimales) |
| e | avec $n = 1\,200$, la borne de Hoeffding sur $P(\lvert \hat{p} - p \rvert \ge 0{,}05)$ | un nombre (4 décimales) |
| f | le plus petit $n$ qui garantit un rayon de Hoeffding d'au plus 0,025 avec $\delta = 0{,}02$ | un entier |

### CP2.9 — Une démonstration courte, au choix parmi deux ∂ ★★★ ⏱️ 12 min · 2 points

Traite **un seul** des deux sujets. Rédige en phrases : ce que tu supposes, chaque étape et la règle qui la justifie, ce que tu conclus.

**Sujet A — La loss des moindres carrés est convexe.** Pour $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ et $t \in [0, 1]$ :
1. Développe les deux membres pour montrer l'identité $\lVert (1 - t)\,\mathbf{u} + t\,\mathbf{v} \rVert^2 = (1 - t)\,\lVert \mathbf{u} \rVert^2 + t\,\lVert \mathbf{v} \rVert^2 - t\,(1 - t)\,\lVert \mathbf{u} - \mathbf{v} \rVert^2$. **[0,5]**
2. Déduis-en que la fonction $g(\mathbf{z}) = \lVert \mathbf{z} \rVert^2$ est convexe sur $\mathbb{R}^n$, et qu'elle l'est strictement : l'inégalité est stricte dès que $\mathbf{u} \ne \mathbf{v}$ et $0 < t < 1$. **[0,5]**
3. Soit $\mathbf{X}$ une matrice de forme $(n, p)$ et $\mathbf{y} \in \mathbb{R}^n$. Montre que $f(\mathbf{w}) = \lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ est convexe sur $\mathbb{R}^p$ (écris $\mathbf{y} - \mathbf{X}\big((1 - t)\,\mathbf{a} + t\,\mathbf{b}\big)$ comme une combinaison de $\mathbf{y} - \mathbf{X}\mathbf{a}$ et $\mathbf{y} - \mathbf{X}\mathbf{b}$). **[0,5]**
4. Déduis-en que, pour $\lambda > 0$, la loss ridge $f(\mathbf{w}) + \lambda \lVert \mathbf{w} \rVert^2$ est strictement convexe, puis qu'elle a **au plus un** minimum : suppose deux minimums distincts $\mathbf{a}$ et $\mathbf{b}$, et regarde leur milieu. **[0,5]**

**Sujet B — La méthode de Chernoff pour une somme de pièces.** $S = X_1 + \cdots + X_n$, où les $X_i$ sont indépendantes, et valent chacune 0 ou 1 avec la probabilité $\frac{1}{2}$.
1. Pour tout $\lambda > 0$ et tout réel $a$, montre que $P(S \ge a) \le e^{-\lambda a}\,\mathbb{E}\big[e^{\lambda S}\big]$, en nommant l'inégalité utilisée et en justifiant qu'elle s'applique. **[0,5]**
2. Montre que $\mathbb{E}\big[e^{\lambda S}\big] = \left(\frac{1 + e^\lambda}{2}\right)^n$ ; dis où sert l'indépendance. **[0,5]**
3. On prend $a = \frac{3n}{4}$. Montre que la borne vaut $h(\lambda)^n$ avec $h(\lambda) = e^{-3\lambda/4}\,\frac{1 + e^\lambda}{2}$, puis trouve le $\lambda > 0$ qui la rend la plus petite (étudie $\ln h$), et la valeur de $h$ en ce point (4 décimales). **[0,75]**
4. Compare à la borne unilatérale de Hoeffding pour le même écart, $P\left(\frac{S}{n} - \frac{1}{2} \ge \frac{1}{4}\right) \le e^{-n/8}$ : laquelle est la plus petite, et que valent les deux pour $n = 40$ (4 décimales) ? **[0,25]**

### CP2.10 — Corriger une copie : cinq erreurs 🐛 ★★ ⏱️ 8 min · 1,25 point

Voici huit lignes extraites de la copie d'un élève. **Cinq** sont fausses.

- **(A)** $\lVert (3, -4, 12) \rVert_2 = 13$.
- **(B)** La similarité cosinus de $(1, 2)$ et $(-2, 1)$ vaut $-1$ : les deux vecteurs vont dans des sens opposés.
- **(C)** Pour une statistique de test de loi symétrique sous $H_0$, la p-valeur unilatérale du côté observé vaut 0,03 : la p-valeur bilatérale vaut donc 0,015.
- **(D)** Le produit d'une matrice de forme $(2, 3)$ par une matrice de forme $(3, 4)$ est une matrice de forme $(2, 4)$.
- **(E)** L'inverse de $\begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}$ est $\begin{pmatrix} 3 & -1 \\ -4 & 2 \end{pmatrix}$.
- **(F)** Dans une régression par moindres carrés avec une colonne de 1 (une ordonnée à l'origine), la somme des résidus d'entraînement est nulle.
- **(G)** L'ensemble des points $(x, y)$ tels que $x^2 + y^2 \le 4$ et $y \ge 1$ n'est pas convexe, parce qu'on y a coupé un disque par une droite.
- **(H)** Dix modèles ont chacun un intervalle de confiance à 95 % de leur accuracy : la probabilité que les dix intervalles contiennent tous la vraie accuracy est d'au moins 95 %.

a) Les lettres des cinq lignes fausses, dans l'ordre alphabétique (un texte, comme `"ABCDE"`). **[0,5]**
b) Pour chaque ligne fausse, écris le résultat juste et la règle oubliée, en une ligne. **[0,75]** (0,15 par ligne)

### CP2.11 — Problème de synthèse : ajuster un modèle, mesurer son erreur, décider 🔗 ★★ ⏱️ 14 min · 2,25 points

Une équipe prédit le temps $y$ (en secondes) d'un traitement nocturne à partir de la taille $x$ (en gigaoctets) des fichiers à traiter. Six nuits ont donné :

| $x$ | 1 | 2 | 4 | 5 | 7 | 11 |
|---|---|---|---|---|---|---|
| $y$ | 7 | 9 | 14 | 15 | 18 | 27 |

Le modèle $\hat{y} = a + b\,x$ s'ajuste par les moindres carrés, avec la matrice $\mathbf{X}$ dont la première colonne ne contient que des 1 et la seconde les valeurs de $x$. Pour comparer des modèles linéaires à bruit gaussien, on utilise ici $\mathrm{AIC} = n \ln\left(\frac{\mathrm{SCR}}{n}\right) + 2k$, où $k$ est le nombre de coefficients du modèle (la constante commune à tous les modèles est omise).

| | Question | Réponse attendue |
|---|---|---|
| a | les deux sommes qui manquent dans $\mathbf{X}^\top\mathbf{X}$ et $\mathbf{X}^\top\mathbf{y}$ : $\left[\sum x_i^2, \sum x_i y_i\right]$ | une liste de 2 nombres |
| b | les coefficients des moindres carrés, par les équations normales | la liste $[a, b]$ (4 décimales) |
| c | la prédiction du modèle pour $x = 9$ | un nombre (2 décimales) |
| d | la SCR du modèle | un nombre (3 décimales) |
| e | le $R^2$ du modèle | un nombre (4 décimales) |
| f | l'AIC du modèle | un nombre (1 décimale) |
| g | le modèle retenu par l'AIC parmi trois : 0. la constante $\hat{y} = \bar{y}$ ($k = 1$, sa SCR est la somme des carrés totale) ; 1. la droite de b) ($k = 2$) ; 2. le polynôme de degré 2 ajusté sur les mêmes nuits ($k = 3$), dont la SCR vaut 1,85 | le numéro 0, 1 ou 2 |
| h | le modèle retenu prédit les traitements du mois suivant : sur 400 traitements tirés au hasard, son erreur absolue est inférieure à 2 secondes pour 344 d'entre eux. La borne basse de Hoeffding **unilatérale** à 95 % de la proportion des traitements prédits à moins de 2 secondes | un nombre (4 décimales) |
| i | ces 400 traitements permettent-ils de garantir, avec une confiance de 95 %, que cette proportion est d'au moins 80 % ? | `True` ou `False` |

Sur ta copie, pour g) : pourquoi le polynôme de degré 2, qui a la plus petite SCR, n'est-il pas retenu ? Pour h) : quelles hypothèses de Hoeffding faut-il vérifier avant de croire cette borne ?

---

**Fin de l'examen.** Note l'heure, relis ta copie, puis passe à la vérification : le notebook `02_examen_notebook.ipynb` (ta copie), puis le corrigé `03_examen_corrige.md`.
