# CP5 · Examen blanc de la partie V (M21 et M22)

| | |
|---|---|
| **Durée** | 112 minutes (environ 2 heures), d'une traite |
| **Note** | sur 20 : un point par minute prévue (112 points en tout), puis ton total divisé par 5,6 |
| **Chapitres** | M21 et M22 : convolution et corrélation croisée, matrices de Toeplitz et circulantes, équivariance, positions d'une fenêtre et convolution transposée, canaux et champ récepteur, pire cas d'une perturbation bornée ; récurrences avec entrée et réponse impulsionnelle, valeurs propres complexes, rayon spectral, normes induites, produits de matrices et de jacobiennes, sensibilité à un paramètre utilisé à chaque pas, vecteurs faits de blocs |
| **Ta copie** | `04_mes_reponses.md` (dans `mon_travail/checkpoints/partie_5/`), ou une feuille de papier |
| **Après** | le notebook `02_examen_notebook.ipynb` vérifie tes réponses chiffrées ; le quiz CP5.Q1, la démonstration CP5.8, les corrections de CP5.9 b) et les justifications « sur ta copie » se notent avec le corrigé `03_examen_corrige.md`, qui donne aussi le barème et la remédiation |

## Règles

- **Fiches, notes, flashcards, annexes et corrigés fermés.** Pas d'assistant IA, pas de recherche sur le web.
- **Calculatrice autorisée**, ou Python comme simple calculatrice (`+`, `*`, `/`, `**`, `math.sqrt`, `math.exp`, `math.log`, `math.cos`, `math.acos`) ; ni NumPy, ni SciPy, ni SymPy, ni `mymath`, ni les notebooks des chapitres. Quand une question nomme une fonction de NumPy (CP5.1), c'est à toi de calculer ce qu'elle rendrait.
- **Décimales.** Quand la colonne « Réponse attendue » dit « valeur exacte », la réponse est un nombre décimal qui n'a que quelques décimales : donne-les toutes, sans arrondir. Quand elle dit « 4 décimales » (ou 3), arrondis à ce nombre de décimales, et **à la fin** du calcul seulement : enchaîne les calculs à la calculatrice, ou garde au moins 6 chiffres significatifs dans les résultats intermédiaires (4 décimales ne suffisent pas sous une racine carrée, dans un logarithme ou avant une soustraction).
- Écris ta démarche : une partie des points d'une question de calcul va à la méthode. Quand une question dit « justifie », une réponse sans justification ne rapporte qu'une partie des points.
- Les durées sont indicatives : commence par ce que tu sais faire ; si tu bloques, passe à la question suivante et reviens-y à la fin.

**Barème.** Chaque question vaut autant de points que de minutes prévues, et ces points sont partagés également entre ses sous-questions (ou ses affirmations, ou ses étapes). L'examen compte donc 112 points, et ta note sur 20 est ton total divisé par 5,6 : chaque question pèse dans la note en proportion de sa durée. Le poids de chaque sous-question est donné dans le titre de la question (ou entre crochets pour CP5.8 et CP5.9) ; une justification demandée « sur ta copie » compte dans les points de la sous-question à laquelle elle se rattache.

| Question | Type | Sujet | Points | ⏱️ |
|---|---|---|---|---|
| CP5.Q1 | 🧠 | Dix affirmations sur la partie V : vrai ou faux | 10 | 10 min |
| CP5.1 | ✏️ | Convolution de deux suites, corrélation croisée et matrice de Toeplitz | 10 | 10 min |
| CP5.2 | ✏️ | Positions d'une fenêtre, pas, dilatation, et la convolution transposée d'un signal | 10 | 10 min |
| CP5.3 | ✏️ | Une grille filtrée par un noyau séparable : paramètres, coût et champ récepteur | 10 | 10 min |
| CP5.4 | ✏️ | Équivariance, matrice circulante et le pire cas d'une perturbation bornée | 9 | 9 min |
| CP5.5 | ✏️ | Une récurrence avec entrée : solution et réponse impulsionnelle | 10 | 10 min |
| CP5.6 | ✏️ | Valeurs propres complexes, rayon spectral, normes et croissance transitoire | 10 | 10 min |
| CP5.7 | ✏️ | Produits de jacobiennes le long d'une trajectoire, et sensibilité à un paramètre utilisé à chaque pas | 9 | 9 min |
| CP5.8 | ∂ | Une démonstration au choix : une convolution pleine est injective, ou la série I + A + A² + … quand ‖A‖ < 1 | 12 | 12 min |
| CP5.9 | 🐛 | Corriger une copie : cinq erreurs | 8 | 8 min |
| CP5.10 | 🔗 | Problème de synthèse : un filtre récursif et un filtre à réponse finie, du signal à la stabilité | 14 | 14 min |
| | | **Total** (note sur 20 = total ÷ 5,6) | **112** | **112 min** |

**Conventions de la partie V.**
- **Suites et noyaux.** Les indices commencent à 0 ; une suite est nulle hors de ses indices. La **convolution** retourne le noyau, $(\mathbf{a} * \mathbf{b})_m = \sum_i a_i\,b_{m-i}$, en mode plein sauf mention contraire (c'est `np.convolve`). La **corrélation croisée** (la somme glissante des bibliothèques) ne le retourne pas, $(\mathbf{w} \star \mathbf{x})_i = \sum_u w_u\,x_{i+u}$, en mode valide. Le mode « même taille » est celui de NumPy : les valeurs de la convolution pleine à partir de l'indice $\big\lfloor\frac{\min(n, k) - 1}{2}\big\rfloor$, soit $\big\lfloor\frac{k - 1}{2}\big\rfloor$ quand $k \le n$. La matrice de $\mathbf{x} \mapsto \mathbf{x} * \mathbf{w}$ (mode plein) est la matrice de Toeplitz $T_{ij} = w_{i-j}$. La **convolution circulaire** de deux suites de longueur $n$ est $(\mathbf{a} \circledast \mathbf{b})_m = \sum_i a_i\,b_{(m-i) \bmod n}$, de matrice $\operatorname{circ}(\mathbf{h})$, de coefficients $h_{(i-j) \bmod n}$.
- **Fenêtres.** Un padding $p$ ajoute $p$ zéros de chaque côté ; le pas est $s$, la dilatation $d$, et la fenêtre numéro $i$ lit les cases $si, si + d, \ldots, si + d(k - 1)$ du signal complété. Le **champ récepteur** d'une sortie d'une pile est la plage des cases du signal d'origine que lisent ses calculs, de la première à la dernière, trous compris. Une grille à plusieurs canaux a la forme $(C, H, W)$, ses poids la forme $(C_{\text{out}}, C_{\text{in}}, k_h, k_w)$, et le coût se compte en multiplications-additions, une par poids et par position de sortie.
- **Récurrences.** Convention **colonne** : $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t$, l'entrée $\mathbf{u}_t$ servant à calculer $\mathbf{x}_{t+1}$ ; sortie $y_t = \mathbf{C}\mathbf{x}_t$ ; réponse impulsionnelle $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$, et, pour $\mathbf{x}_0 = \mathbf{0}$, $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$. $\rho(\mathbf{A})$ est le rayon spectral ; $\lVert\mathbf{A}\rVert_1$, $\lVert\mathbf{A}\rVert_\infty$ et $\lVert\mathbf{A}\rVert_2 = s_{\max}(\mathbf{A})$ sont les normes induites par les normes L1, L∞ et L2 des vecteurs. Une jacobienne a une ligne par coordonnée de sortie ; un produit de matrices s'écrit avec la matrice du dernier pas à gauche.
- **Comportement des puissances** d'une matrice carrée, codé 1 (elles tendent vers $\mathbf{0}$), 2 (elles restent bornées sans tendre vers $\mathbf{0}$) ou 3 (elles ne sont pas bornées).
- **Listes.** Une réponse en liste se donne dans l'ordre de la question : les coordonnées ou les termes dans l'ordre de leurs indices, et les éléments annoncés par « puis » dans cet ordre. Quand l'ordre ne compte pas, la question le dit (« dans n'importe quel ordre »).
- Dans le notebook, une matrice s'écrit comme la liste de ses **lignes**, un nombre complexe $a + ib$ comme la liste `[a, b]`, et un angle exact en radians entre guillemets, comme `"pi/5"`.
- Dans les tableaux, « données 1 », « données 2 »… renvoient aux situations numérotées au-dessus du tableau.

---

### CP5.Q1 — Dix affirmations sur la partie V : vrai ou faux 🧠 ★ ⏱️ 10 min · 10 points (1 par affirmation)

Pour chaque affirmation, réponds **Vrai** ou **Faux**, puis justifie en une phrase : une règle, un calcul ou un contre-exemple. Chaque affirmation vaut 1 point : 0,4 pour le verdict, 0,6 pour la justification. Ce quiz se note avec le corrigé.

a) Une récurrence $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}u_t$, avec $\rho(\mathbf{A}) < 1$, part de $\mathbf{x}_0 = \mathbf{0}$ et ne reçoit plus que des entrées nulles à partir d'un pas $T$. Alors sa sortie $y_t = \mathbf{C}\mathbf{x}_t$ est nulle à partir d'un certain pas.
b) Toute matrice circulante $\mathbf{M} = \operatorname{circ}(\mathbf{h})$ vérifie $\lVert\mathbf{M}^t\rVert_2 = \rho(\mathbf{M})^t$ pour tout $t \ge 1$.
c) Si les coefficients de $\mathbf{h} = (h_0, \ldots, h_{n-1})$ sont tous positifs ou nuls, et pas tous nuls, alors $\rho\big(\operatorname{circ}(\mathbf{h})\big) = \lVert\operatorname{circ}(\mathbf{h})\rVert_1 = h_0 + h_1 + \cdots + h_{n-1}$.
d) Pour le noyau $\mathbf{w} = (0, 2, -1)$ et des signaux de longueur $n \ge 3$, la matrice carrée formée des $n$ premières lignes de la matrice de $\mathbf{x} \mapsto \mathbf{x} * \mathbf{w}$ (mode plein) est nilpotente.
e) La matrice $\mathbf{A} = \begin{pmatrix} 0 & 4 \\ -1 & 0 \end{pmatrix}$ a deux valeurs propres complexes conjuguées, et $\lVert\mathbf{A}\rVert_2 = \sqrt{\det\mathbf{A}}$.
f) Pour $\mathbf{A} = \operatorname{diag}(0{,}5 ;\ 0{,}25)$, dont les valeurs propres sont réelles et dans $]0, 1[$, $\mathbf{B} = (1, 1)^\top$ et $\mathbf{C} = (1, -3)$, la réponse impulsionnelle $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$ garde le même signe pour tous les $k$.
g) On enchaîne deux sommes glissantes sans padding, la première de pas 4, la seconde de pas 2. Loin des bords, décaler l'entrée de 8 cases décale la sortie finale d'une case.
h) Deux matrices carrées vérifient $\lVert\mathbf{A}_1\rVert_2 < 1$ et $\lVert\mathbf{A}_2\rVert_2 < 1$ ; leur produit $\mathbf{A}_2\mathbf{A}_1$ peut pourtant avoir un rayon spectral supérieur à 1.
i) La suite $h_k = 0{,}5^k\cos\frac{k\pi}{3}$ ($k \ge 0$) est la réponse impulsionnelle d'une récurrence à état de dimension 2.
j) Pour $\mathbf{a} = (2, -5)$ et $\mathbf{b} = (1, 4, 3)$, la matrice de rang 1 $\mathbf{a}\mathbf{b}^\top$ vérifie $\lVert\mathbf{a}\mathbf{b}^\top\rVert_2 = \lVert\mathbf{a}\rVert_2\lVert\mathbf{b}\rVert_2$ et $\lVert\mathbf{a}\mathbf{b}^\top\rVert_1 = \lVert\mathbf{a}\rVert_1\lVert\mathbf{b}\rVert_1$.

### CP5.1 — Convolution de deux suites, corrélation croisée et matrice de Toeplitz ✏️ ★★ ⏱️ 10 min · 10 points (10/7 ≈ 1,43 par sous-question)

1. Deux polynômes, $P(X) = 2 + 3X - X^2$ et $Q(X) = 1 - 2X^2 + X^3$, ont pour coefficients $\mathbf{a} = (2, 3, -1)$ et $\mathbf{b} = (1, 0, -2, 1)$, du terme constant au terme de plus haut degré.
2. Un capteur donne le signal $\mathbf{x} = (3, -2, 4, 1, 0, -1)$ ($n = 6$), que l'on filtre par le noyau $\mathbf{w} = (3, 0, -2, 1)$ ($k = 4$).

| | Question | Réponse attendue |
|---|---|---|
| a | données 1 : les coefficients de $PQ$, c'est-à-dire $\mathbf{a} * \mathbf{b}$ | une liste de 6 entiers |
| b | données 1 : la somme alternée $\sum_m (-1)^m\,(\mathbf{a} * \mathbf{b})_m$ | un entier |
| c | données 2 : la corrélation croisée $\mathbf{w} \star \mathbf{x}$, en mode valide | une liste de 3 entiers |
| d | données 2 : la convolution $\mathbf{x} * \mathbf{w}$, en mode plein | une liste de 9 entiers |
| e | données 2 : ce que rend `np.convolve(x, w, "same")` | une liste de 6 entiers |
| f | données 2 : la matrice $\mathbf{T}$ de $\mathbf{y} \mapsto \mathbf{y} * \mathbf{w}$, en mode plein, pour des signaux $\mathbf{y}$ de longueur 3 | une matrice $6 \times 3$ |
| g | données 2 : le nombre de coefficients non nuls de la matrice de $\mathbf{y} \mapsto \mathbf{y} * \mathbf{w}$, en mode plein, pour des signaux de longueur 40 | un entier |

Sur ta copie : pour b), en quelle valeur de $X$ évalue-t-on $PQ$, et retrouve b) à partir de $P$ et $Q$ seuls ; pour e), à quel indice de d) commence-t-il ; pour f), pourquoi une ligne de $\mathbf{T}$ lit-elle le noyau retourné.

### CP5.2 — Positions d'une fenêtre, pas, dilatation, et la convolution transposée d'un signal ✏️ ★★ ⏱️ 10 min · 10 points (10/7 ≈ 1,43 par sous-question)

1. Un accéléromètre enregistre $n = 472$ échantillons, que l'on parcourt par une fenêtre de $k = 9$ poids (une somme glissante). Une position existe quand toute la fenêtre tient dans le signal complété. Sauf mention contraire, $p = 0$ et $d = 1$.
2. La convolution transposée de $\mathbf{y} = (1, -2, 3, 2)$ associée au noyau $\mathbf{w} = (3, -2, 2)$, avec un pas $s = 2$, sans padding ni padding de sortie.

| | Question | Réponse attendue |
|---|---|---|
| a | données 1 : le nombre de positions avec un pas $s = 4$ | un entier |
| b | données 1 : le nombre de positions avec $s = 4$, un padding $p = 5$ et une dilatation $d = 3$ | un entier |
| c | données 1 : toutes les longueurs de fenêtre $k$ qui donnent exactement 110 positions avec $n = 472$ et $s = 4$ (sans padding ni dilatation) | une liste d'entiers, dans n'importe quel ordre |
| d | données 1 : la règle « même taille » avec un pas $s = 4$ (celle de TensorFlow et de Keras, fiche M21 §5), pour $n = 472$ et $k = 9$ : le nombre de positions, puis le nombre de zéros ajoutés au début, puis à la fin | une liste de 3 entiers |
| e | données 2 : le résultat de la convolution transposée | une liste de 9 entiers |
| f | la taille d'une convolution transposée de $m = 50$ valeurs d'entrée, de noyau de longueur $k = 5$, de pas $s = 3$, avec un padding $p = 2$ et un padding de sortie $p_{\text{out}} = 1$ | un entier |
| g | une convolution transposée de noyau de longueur $k = 10$ et de pas $s = 3$ : les différentes valeurs que prend le nombre de tampons qui couvrent une case intérieure (loin des deux bords) | une liste d'entiers, dans n'importe quel ordre |

Sur ta copie : pour d), le nombre total de zéros, et pourquoi un zéro de moins ne suffirait pas ; pour e), les quatre tampons et les cases qui en reçoivent deux.

### CP5.3 — Une grille filtrée par un noyau séparable : paramètres, coût et champ récepteur ✏️ ★★ ⏱️ 10 min · 10 points (1,25 par sous-question)

1. Des épaisseurs de neige (en cm) relevées sur une grille de 4 lignes et 5 colonnes, filtrées par le noyau $\mathbf{K}$, en corrélation croisée (sans retournement, comme les bibliothèques), en mode valide, avec un pas de 1 :
$$\mathbf{G} = \begin{pmatrix} 3 & 1 & 0 & 2 & 4 \\ 1 & 4 & 2 & 0 & 1 \\ 2 & 0 & 3 & 1 & 2 \\ 0 & 2 & 1 & 3 & 1 \end{pmatrix}, \qquad \mathbf{K} = \begin{pmatrix} 2 & -2 & 6 \\ 1 & -1 & 3 \\ -1 & 1 & -3 \end{pmatrix}, \qquad Y_{i,j} = \sum_{u=0}^{2}\sum_{v=0}^{2}K_{u,v}\,G_{i+u,\,j+v}.$$
2. Une caméra thermique fournit des images de $96 \times 144$ pixels à $C_{\text{in}} = 5$ canaux, filtrées vers $C_{\text{out}} = 12$ canaux par des noyaux $3 \times 5$ (3 lignes, 5 colonnes), avec un biais par sortie, un padding de 1 en hauteur et de 2 en largeur, et un pas $s = 2$ selon les deux axes.
3. Une pile de quatre sommes glissantes, de réglages $(k, s, d) = (2, 1, 1)$, puis $(4, 3, 1)$, puis $(2, 1, 3)$, puis $(3, 4, 1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | données 1 : les deux facteurs $\mathbf{a}$, puis $\mathbf{b}$, tels que $\mathbf{K} = \mathbf{a}\mathbf{b}^\top$ (soit $K_{u,v} = a_u\,b_v$), avec $b_0 = 1$ | une liste de 2 listes, $[\mathbf{a}, \mathbf{b}]$ |
| b | données 1 : la sortie $\mathbf{Y}$ | une matrice $2 \times 3$ |
| c | données 1 : le nombre total de multiplications pour toute la sortie $\mathbf{Y}$, en deux passes chacune en mode valide, en commençant par la passe horizontale (par $\mathbf{b}$, sur chaque ligne de $\mathbf{G}$), puis la passe verticale (par $\mathbf{a}$) ; compte toutes les multiplications, même par 1 ou par $-1$ | un entier |
| d | données 2 : la forme $(C, H, W)$ de la sortie | une liste de 3 entiers |
| e | données 2 : le nombre de paramètres | un entier |
| f | données 2 : le nombre de multiplications-additions pour une image | un entier |
| g | données 2 : le nombre de paramètres d'une convolution séparable par canal qui la remplace : une convolution par canal $3 \times 5$ (5 sorties, un biais chacune), suivie d'une convolution $1 \times 1$ de 5 vers 12 canaux (un biais par sortie) | un entier |
| h | données 3 : le champ récepteur d'une sortie de la pile, puis son pas total | une liste de 2 entiers |

Sur ta copie : pourquoi $\mathbf{K}$ est de rang 1 ; la sortie de la passe horizontale, et le nombre de multiplications du calcul direct.

### CP5.4 — Équivariance, matrice circulante et le pire cas d'une perturbation bornée ✏️ ★★ ⏱️ 9 min · 9 points (1,5 par sous-question)

Cinq jauges de déformation sont collées sur les cinq pales d'un rotor, une par pale : les indices se lisent modulo 5 (la pale 5 est la pale 0), et $\mathbf{P}$ est le décalage circulaire, $(\mathbf{P}\mathbf{x})_i = x_{(i-1) \bmod 5}$. Leurs écarts à la déformation de référence valent $\mathbf{x} = (1, 3, -2, 0, 2)$ (en µm/m). On les filtre par la convolution circulaire de noyau $\mathbf{h} = (1, -4, 2, 3, -2)$ : $\mathbf{z} = \mathbf{x} \circledast \mathbf{h}$.
Pour d) à f), chaque jauge est juste à $\varepsilon = 0{,}2$ µm/m près : la vraie valeur est $\mathbf{x} + \boldsymbol{\delta}$, avec $\lvert\delta_i\rvert \le 0{,}2$ pour tout $i$, et l'on regarde de combien $\boldsymbol{\delta}$ peut **augmenter** la sortie $z_1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{z} = \mathbf{x} \circledast \mathbf{h}$ | une liste de 5 entiers |
| b | la première ligne de la matrice $\operatorname{circ}(\mathbf{h})$ | une liste de 5 entiers |
| c | $(\mathbf{P}^2\mathbf{x}) \circledast \mathbf{h}$ | une liste de 5 entiers |
| d | le vecteur $\boldsymbol{\delta}$ qui augmente le plus $z_1$ | une liste de 5 nombres (valeurs exactes) |
| e | cette plus grande augmentation de $z_1$ | un nombre (valeur exacte) |
| f | la plus grande augmentation de $z_1$ si l'on sait seulement que $\lVert\boldsymbol{\delta}\rVert_2 \le 0{,}2$ | un nombre (3 décimales) |

Sur ta copie : obtiens c) à partir de a), sans nouveau calcul, et nomme la propriété utilisée ; quel noyau est la première ligne de $\operatorname{circ}(\mathbf{h})$ ; pourquoi e) serait le même pour n'importe quelle sortie $z_m$.

### CP5.5 — Une récurrence avec entrée : solution et réponse impulsionnelle ✏️ ★★ ⏱️ 10 min · 10 points (1,25 par sous-question)

Un médicament se répartit entre le sang et les tissus. Chaque heure, le sang garde 50 % du médicament qu'il contient, en passe 30 % aux tissus et en élimine 20 % (par les reins) ; les tissus en gardent 70 %, en rendent 10 % au sang et en éliminent 20 %. Une perfusion apporte $u_t$ mg dans le sang pendant l'heure $t$, et l'on mesure la quantité $y_t$ dans les tissus. Avec $\mathbf{x}_t$ = (mg dans le sang, mg dans les tissus) :
$$\mathbf{x}_{t+1} = \underbrace{\begin{pmatrix} 0{,}5 & 0{,}1 \\ 0{,}3 & 0{,}7 \end{pmatrix}}_{\mathbf{A}}\mathbf{x}_t + \underbrace{\begin{pmatrix} 1 \\ 0 \end{pmatrix}}_{\mathbf{B}}u_t, \qquad y_t = \underbrace{\begin{pmatrix} 0 & 1 \end{pmatrix}}_{\mathbf{C}}\mathbf{x}_t,$$
avec $\mathbf{x}_0 = (20, 4)$, $u_0 = 6$, $u_1 = 0$ et $u_2 = 2$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{x}_2$ | une liste de 2 nombres (valeurs exactes) |
| b | $\mathbf{x}_3$ | une liste de 2 nombres (valeurs exactes) |
| c | les valeurs propres de $\mathbf{A}$ | une liste de 2 nombres (valeurs exactes), dans n'importe quel ordre |
| d | la réponse impulsionnelle $h_0, h_1, h_2, h_3$ | une liste de 4 nombres (valeurs exactes) |
| e | on admet que $h_k = \alpha\,\lambda_2^k + \beta\,\lambda_1^k$ pour tout $k \ge 0$, où $\lambda_1 < \lambda_2$ sont les deux valeurs propres de $\mathbf{A}$ : $\alpha$, puis $\beta$ | une liste de 2 nombres (valeurs exactes) |
| f | la part de $y_3$ due à la perfusion (la sortie de la réponse forcée de $\mathbf{x}_3$) | un nombre (valeur exacte) |
| g | l'équilibre $\mathbf{x}^\star$ pour une perfusion constante de $u_t = 4$ mg par heure | une liste de 2 nombres (valeurs exactes) |
| h | sans perfusion, la quantité totale $x_{t,1} + x_{t,2}$ est multipliée chaque heure par un même nombre, quel que soit $\mathbf{x}_t$ : lequel ? | un nombre (valeur exacte) |

Sur ta copie : pour e), les deux équations qui donnent $\alpha$ et $\beta$ ; pour h), ce que voient les sommes des colonnes de $\mathbf{A}$.

### CP5.6 — Valeurs propres complexes, rayon spectral, normes et croissance transitoire ✏️ ★★ ⏱️ 10 min · 10 points (1,25 par sous-question)

$$\mathbf{M} = \begin{pmatrix} 0 & -1 \\ 0{,}75 & 1{,}5 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la valeur propre $\lambda$ de $\mathbf{M}$ de partie imaginaire positive, comme `[a, b]` pour $a + ib$ | une liste de 2 nombres (4 décimales) |
| b | $\rho(\mathbf{M})$ | un nombre (4 décimales) |
| c | l'argument principal de $\lambda$ (dans $]-\pi, \pi]$) | un angle exact, entre guillemets |
| d | $\mathbf{M}^3$ | une matrice (valeurs exactes) |
| e | $\mathbf{M}^6$ | une matrice (valeurs exactes) |
| f | $\lVert\mathbf{M}\rVert_1$, puis $\lVert\mathbf{M}\rVert_\infty$ | une liste de 2 nombres (valeurs exactes) |
| g | $\lVert\mathbf{M}\rVert_2$ | un nombre (4 décimales) |
| h | le comportement des puissances de $\mathbf{M}$, puis celui des puissances de $\frac{2}{\sqrt3}\,\mathbf{M}$, codé 1, 2 ou 3 | une liste de 2 entiers |

Sur ta copie : un vecteur que $\mathbf{M}$ allonge, alors que $\rho(\mathbf{M}) < 1$.

### CP5.7 — Produits de jacobiennes le long d'une trajectoire, et sensibilité à un paramètre utilisé à chaque pas ✏️ ★★ ⏱️ 9 min · 9 points (1,5 par sous-question)

1. Une application du plan, $f(x, y) = (0{,}5\,x + y^2,\ x - 0{,}5\,y)$, et la trajectoire $\mathbf{p}_{t+1} = f(\mathbf{p}_t)$, partie de $\mathbf{p}_0 = (2, 1)$.
2. Un réservoir se vide par un orifice (débit proportionnel à la racine carrée de la hauteur d'eau, loi de Torricelli) et reçoit 1 cm d'eau à chaque pas : la hauteur $x_t$ (en cm) vérifie
$$x_{t+1} = f(x_t, \beta) = x_t - \beta\sqrt{x_t} + 1, \qquad x_0 = 36, \qquad \beta = 2 .$$
Le coefficient $\beta$ de l'orifice sert à chaque pas ; $s_t = \frac{\partial x_t}{\partial\beta}$, $J_t = \frac{\partial f}{\partial x}(x_t, \beta)$ et $b_t = \frac{\partial f}{\partial\beta}(x_t, \beta)$ (fiche M22 §7).

| | Question | Réponse attendue |
|---|---|---|
| a | données 1 : $\mathbf{p}_2$ | une liste de 2 nombres (valeurs exactes) |
| b | données 1 : $\frac{\partial\mathbf{p}_2}{\partial\mathbf{p}_0}$ | une matrice (valeurs exactes) |
| c | données 1 : le produit des normes $\lVert\mathbf{J}_f(\mathbf{p}_1)\rVert_\infty\,\lVert\mathbf{J}_f(\mathbf{p}_0)\rVert_\infty$, puis $\big\lVert\frac{\partial\mathbf{p}_2}{\partial\mathbf{p}_0}\big\rVert_\infty$ | une liste de 2 nombres (valeurs exactes) |
| d | données 2 : les trois termes de la somme sur le temps qui donne $s_3$, de celui du pas 0 à celui du pas 2 | une liste de 3 nombres (valeurs exactes) |
| e | données 2 : $s_3$ | un nombre (valeur exacte) |
| f | données 2 : au premier ordre, le changement de $x_3$ quand $\beta$ passe de 2 à 2,1 | un nombre (valeur exacte) |

Sur ta copie : $x_1$, $x_2$, $x_3$, puis les $J_t$ et les $b_t$ ; $\frac{\partial x_3}{\partial x_0} = J_2J_1J_0$, et, au premier ordre, le changement de $x_3$ quand $x_0$ passe de 36 à 37 (avec $\beta = 2$).

### CP5.8 — Une démonstration au choix ∂ ★★★ ⏱️ 12 min · 12 points (3 par étape)

Traite **un seul** des deux sujets. Rédige en phrases : ce que tu supposes, chaque étape et la règle qui la justifie, ce que tu conclus. Cette question se note avec le corrigé.

**Sujet A — Une convolution pleine par un noyau non nul est injective.** Soit $\mathbf{w} = (w_0, \ldots, w_{k-1})$ un noyau non nul, et $\mathcal{C} : \mathbb{R}^n \to \mathbb{R}^{n+k-1}$, $\mathbf{x} \mapsto \mathbf{x} * \mathbf{w}$ (mode plein).
1. Montre que $\mathcal{C}$ est linéaire, et qu'elle est injective si et seulement si $\mathbf{x} * \mathbf{w} = \mathbf{0}$ entraîne $\mathbf{x} = \mathbf{0}$. **[3]**
2. Soit $\mathbf{x} \ne \mathbf{0}$ ; on note $p$ le plus grand indice tel que $x_p \ne 0$, et $q$ le plus grand tel que $w_q \ne 0$. Montre que $(\mathbf{x} * \mathbf{w})_{p+q} = x_p\,w_q$. Conclus que $\mathcal{C}$ est injective, et donne le rang de sa matrice. **[3]**
3. Pour $\mathbf{w} = (4, 1, -2)$, trouve le signal $\mathbf{x}$ de longueur 3 tel que $\mathbf{x} * \mathbf{w} = (12, 3, -10, -1, 2)$, en le calculant à partir de son dernier coefficient. Pourquoi est-il le seul ? **[3]**
4. En convolution circulaire, la conclusion tombe : pour $n = 4$ et $\mathbf{h} = (1, 0, -1, 0)$, trouve $\mathbf{x} \ne \mathbf{0}$ tel que $\mathbf{x} \circledast \mathbf{h} = \mathbf{0}$, et dis quelle étape de la question 2 ne tient plus. **[3]**

**Sujet B — La série $\mathbf{I} + \mathbf{A} + \mathbf{A}^2 + \cdots$ quand $\lVert\mathbf{A}\rVert < 1$.** $\lVert\cdot\rVert$ est l'une des trois normes induites $\lVert\cdot\rVert_1$, $\lVert\cdot\rVert_2$, $\lVert\cdot\rVert_\infty$, et $\mathbf{A}$ est une matrice carrée réelle telle que $\lVert\mathbf{A}\rVert < 1$.
1. Montre que 1 n'est pas une valeur propre de $\mathbf{A}$ (utilise $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert$, M22 §4), et déduis-en que $\mathbf{I} - \mathbf{A}$ est inversible. **[3]**
2. Pour $\mathbf{y}$ quelconque, soit $\mathbf{x} = (\mathbf{I} - \mathbf{A})^{-1}\mathbf{y}$. Montre que $\lVert\mathbf{x}\rVert \le \frac{\lVert\mathbf{y}\rVert}{1 - \lVert\mathbf{A}\rVert}$, et déduis-en $\lVert(\mathbf{I} - \mathbf{A})^{-1}\rVert \le \frac{1}{1 - \lVert\mathbf{A}\rVert}$. **[3]**
3. On note $\mathbf{M} = (\mathbf{I} - \mathbf{A})^{-1}$ et $\mathbf{S}_N = \mathbf{I} + \mathbf{A} + \cdots + \mathbf{A}^N$. Montre que $\mathbf{M} = \mathbf{I} + \mathbf{A}\mathbf{M}$ et $\mathbf{S}_N = \mathbf{I} + \mathbf{A}\mathbf{S}_{N-1}$, puis que l'écart $\mathbf{E}_N = \mathbf{M} - \mathbf{S}_N$ vérifie $\mathbf{E}_N = \mathbf{A}\mathbf{E}_{N-1}$. Conclus : $\lVert\mathbf{M} - \mathbf{S}_N\rVert \le \frac{\lVert\mathbf{A}\rVert^{N+1}}{1 - \lVert\mathbf{A}\rVert}$, donc $(\mathbf{I} - \mathbf{A})^{-1} = \mathbf{I} + \mathbf{A} + \mathbf{A}^2 + \cdots$ **[3]**
4. Pour $\mathbf{A} = \begin{pmatrix} 0{,}5 & 0{,}3 \\ 0{,}2 & -0{,}4 \end{pmatrix}$ : calcule $\lVert\mathbf{A}\rVert_1$ et $\lVert\mathbf{A}\rVert_\infty$, dis pourquoi les questions 1 à 3 s'appliquent, calcule $(\mathbf{I} - \mathbf{A})^{-1}$ et compare sa norme $\lVert\cdot\rVert_\infty$ à la borne de la question 2. Enfin, pour $\mathbf{A} = 2\,\mathbf{I}$, $\mathbf{I} - \mathbf{A}$ est inversible : que devient la série ? **[3]**

### CP5.9 — Corriger une copie : cinq erreurs 🐛 ★★ ⏱️ 8 min · 8 points

Voici huit lignes extraites de la copie d'un élève. **Cinq** sont fausses.

- **(A)** Le pooling par le maximum, par blocs de 2, est linéaire : pour $(5, 2, 1, 3) + (2, 6, 4, 0)$, il donne $(5, 3) + (6, 4) = (11, 7)$.
- **(B)** La matrice de $\mathbf{x} \mapsto \mathbf{x} * (-3, 1, 5)$, en mode valide, pour des signaux de longueur 7, a 5 lignes et 7 colonnes ; elle est de rang 7.
- **(C)** La convolution transposée de 7 valeurs, de pas 2, par un noyau de longueur 5, sans padding ni padding de sortie, a $(7 - 1) \times 2 + 5 = 17$ valeurs.
- **(D)** Passer de noyaux $3 \times 3$ à des noyaux $6 \times 6$, sans changer les canaux ni la taille de la sortie, double le nombre de multiplications-additions.
- **(E)** $\mathbf{P} = \begin{pmatrix} 1 & 3 \\ 0 & 0 \end{pmatrix}$ a pour norme $\lVert\mathbf{P}\rVert_2 = \sqrt{10}$, donc $\lVert\mathbf{P}^{10}\rVert_2 = (\sqrt{10})^{10} = 10^5$.
- **(F)** $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ -0{,}5 & -0{,}6 \end{pmatrix}$ a $\rho(\mathbf{A}) = \sqrt{0{,}4} \approx 0{,}63$ : ses puissances tendent vers $\mathbf{0}$, bien que $\lVert\mathbf{A}\rVert_\infty = 3$.
- **(G)** Un vecteur fait de trois blocs, de normes 2, 5 et 14, a pour norme globale 21 ; pour le ramener tout entier sous $c = 9$, on multiplie chaque bloc par $\frac{9}{21} = \frac37$.
- **(H)** $\mathbf{B} = \begin{pmatrix} 0{,}25 & -0{,}6 \\ 0{,}6 & 0{,}25 \end{pmatrix}$ vérifie $\lVert\mathbf{B}^t\mathbf{x}\rVert_2 = 0{,}65^t\,\lVert\mathbf{x}\rVert_2$ pour tout $\mathbf{x}$ et tout $t$.

a) Les lettres des cinq lignes fausses, dans n'importe quel ordre (un texte, comme `"ABCDE"`). **[4]**
b) Pour chaque ligne fausse, écris le résultat juste et la règle oubliée, en une ligne. **[4]** (0,8 par ligne ; se note avec le corrigé)

### CP5.10 — Problème de synthèse : un filtre récursif et un filtre à réponse finie, du signal à la stabilité 🔗 ★★ ⏱️ 14 min · 14 points (2 par sous-question)

Le signal $u_t$ d'un capteur de pression est lissé par un **filtre récursif** à deux états (une récurrence avec entrée) :
$$\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}u_t, \quad y_t = \mathbf{C}\mathbf{x}_t, \quad \mathbf{x}_0 = \mathbf{0}, \qquad \mathbf{A} = \begin{pmatrix} 0{,}6 & -0{,}5 \\ 0{,}4 & 0{,}6 \end{pmatrix}, \quad \mathbf{B} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \mathbf{C} = \begin{pmatrix} 0 & 1 \end{pmatrix}.$$
Sa réponse impulsionnelle est $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$, et $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$. On l'approche aussi par un **filtre à réponse finie** de longueur $K$ : la convolution $z_{t+1} = (\mathbf{g} * \mathbf{u})_t$ par les $K$ premiers termes $\mathbf{g} = (h_0, \ldots, h_{K-1})$. On admet que $\lvert h_k\rvert \le \lVert\mathbf{A}^k\rVert$ pour chacune des trois normes induites (un coefficient d'une matrice est au plus sa norme induite).

| | Question | Réponse attendue |
|---|---|---|
| a | $h_0, h_1, h_2, h_3, h_4$ | une liste de 5 nombres (valeurs exactes) |
| b | les sorties $y_1, \ldots, y_5$ pour les entrées $\mathbf{u} = (4, -2, 0, 3)$, puis des entrées nulles | une liste de 5 nombres (valeurs exactes) |
| c | $\rho(\mathbf{A})$ | un nombre (4 décimales) |
| d | $\lVert\mathbf{A}\rVert_1$, puis $\lVert\mathbf{A}\rVert_\infty$, puis $\lVert\mathbf{A}\rVert_2$ | une liste de 3 nombres (valeurs exactes) |
| e | avec la norme de d) qui est plus petite que 1 : le plus petit $K$ pour lequel la majoration $\sum_{k \ge K}\lvert h_k\rvert \le \frac{\lVert\mathbf{A}\rVert^K}{1 - \lVert\mathbf{A}\rVert}$ garantit $\lvert y_t - z_t\rvert \le 0{,}01$ pour toutes entrées telles que $\lvert u_t\rvert \le 1$ | un entier |
| f | pour $K = 5$ : la plus grande valeur possible de $\lvert z_t\rvert$ quand $\lvert u_t\rvert \le 1$ pour tout $t$ | un nombre (valeur exacte) |
| g | la limite de $y_t$ quand l'entrée vaut $u_t = 1$ à chaque pas | une fraction irréductible, entre guillemets |

Sur ta copie : les valeurs propres de $\mathbf{A}$ ; pourquoi $\lVert\mathbf{A}\rVert_1$ et $\lVert\mathbf{A}\rVert_\infty$ ne permettent pas e).

---

**Fin de l'examen.** Note l'heure, relis ta copie, puis passe à la vérification : le notebook `02_examen_notebook.ipynb` (ta copie), puis le corrigé `03_examen_corrige.md`.
