# M25a · Gaussienne multivariée, conditionnement et divergence KL — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m25a_gaussienne/06_mes_reponses.md` (créée par `python tools/start_chapter.py M25a`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les vecteurs sont des **colonnes** ; $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ a pour second paramètre une **covariance** ; $\Delta(\mathbf{x})$ est la distance de Mahalanobis à $\boldsymbol{\mu}$, $\Delta^2(\mathbf{x}) = (\mathbf{x} - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})$, et $d$ la dimension ; $\mathbf{L}$ est le facteur de Cholesky de $\boldsymbol{\Sigma}$ (triangulaire inférieur, de diagonale positive, $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$) ; $\boldsymbol{\varepsilon}$ suit $\mathcal{N}(\mathbf{0}, \mathbf{I})$ ; les blocs s'indexent $a$ (les coordonnées cherchées) et $b$ (les coordonnées lues), et $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ est la matrice de précision ; $\mathrm{KL}(p \,\|\, q) = \mathbb{E}_p[\ln p - \ln q]$, en nats ; $\ln$ est le logarithme népérien. Dans le notebook, une matrice s'écrit comme la liste de ses **lignes**, et plusieurs vecteurs sont les lignes d'un tableau de forme $(n, d)$.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun (6 pour M25a.Q4). Réponds vite, puis vérifie dans `05_solutions.md`.

### M25a.Q1 — Lire une densité gaussienne multivariée : det Σ, distance de Mahalanobis et point le plus probable 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Une densité s'écrit $p(\mathbf{x}) = \frac{1}{(2\pi)^{3/2} \times 6}\exp\big(-\frac12\Delta^2(\mathbf{x})\big)$. Quelle est la dimension $d$, et que vaut $\det\boldsymbol{\Sigma}$ ?
2. Une loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ du plan a $\det\boldsymbol{\Sigma} = 25$. En quel point sa densité est-elle maximale, et que vaut-elle en ce point ?
3. Vrai ou faux : deux points à la même distance de Mahalanobis de $\boldsymbol{\mu}$ ont la même densité.
4. Vrai ou faux : de deux points, celui qui est le plus proche de $\boldsymbol{\mu}$ en distance euclidienne a toujours la plus grande densité.
5. En dimension 3, on multiplie $\boldsymbol{\Sigma}$ par 9. Par combien la hauteur du pic est-elle divisée ?
6. Vrai ou faux : une densité gaussienne peut prendre des valeurs plus grandes que 1.
7. $\boldsymbol{\Sigma} = \operatorname{diag}(4, 9)$ et $\mathbf{x} - \boldsymbol{\mu} = (2, -3)$ : que vaut $\Delta^2(\mathbf{x})$, et de combien $\ln p(\mathbf{x})$ est-il plus petit que $\ln p(\boldsymbol{\mu})$ ?

### M25a.Q2 — Ce qui reste gaussien : images affines, sommes, produits et normes ; deux marginales gaussiennes ne suffisent pas 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ dans $\mathbb{R}^3$, $\mathbf{A}$ de forme $(2, 3)$ et $\mathbf{b} \in \mathbb{R}^2$ : la loi de $\mathbf{A}\mathbf{x} + \mathbf{b}$, et la forme de sa covariance ?
2. Vrai ou faux : si $x_1$ et $x_2$ suivent chacune une loi normale, $x_1 + x_2$ suit une loi normale.
3. Vrai ou faux : si $\mathbf{x}$ et $\mathbf{y}$ sont deux vecteurs gaussiens indépendants de même dimension, $\mathbf{x} - \mathbf{y} \sim \mathcal{N}(\boldsymbol{\mu}_{\mathbf{x}} - \boldsymbol{\mu}_{\mathbf{y}},\ \boldsymbol{\Sigma}_{\mathbf{x}} + \boldsymbol{\Sigma}_{\mathbf{y}})$.
4. Vrai ou faux : si $x_1$ et $x_2$ sont indépendantes, de loi $\mathcal{N}(0, 1)$, le produit $x_1x_2$ suit une loi normale.
5. $z \sim \mathcal{N}(0, 1)$ et $\mathbf{x} = (z,\ 3 - z)$. Est-ce un vecteur gaussien ? Sa covariance ? A-t-il une densité ?
6. Vrai ou faux : la norme $\lVert\mathbf{x}\rVert$ d'un vecteur gaussien non constant n'est jamais une variable normale.
7. $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, de facteur de Cholesky $\mathbf{L}$ : la loi de $\mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ ?

### M25a.Q3 — Ellipses de niveau et masse : quel axe, quel demi-axe, quelle proportion, en dimension 2 et au-delà 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

$\boldsymbol{\Sigma} = \begin{pmatrix} 14{,}5 & 10{,}5 \\ 10{,}5 & 14{,}5 \end{pmatrix}$ a pour valeurs propres 25 et 4, de vecteurs propres $\frac{1}{\sqrt2}(1, 1)$ et $\frac{1}{\sqrt2}(1, -1)$.

1. La direction du grand axe des ellipses de niveau ?
2. Les demi-axes de l'ellipse $\Delta(\mathbf{x}) = 2$ ?
3. L'aire de cette ellipse ?
4. La part des tirages qui tombent dans l'ellipse de niveau $c = \sqrt{2\ln 4}$ ?
5. Vrai ou faux : en dimension 5, l'ellipsoïde de même niveau $c$ contient la même part des tirages.
6. Vrai ou faux : si l'on multiplie $\boldsymbol{\Sigma}$ par 4, l'ellipse de niveau $c = \sqrt{2\ln 4}$ (pour la nouvelle loi) contient toujours la même part des tirages.
7. En dimension 10, le mode de la norme d'un tirage de $\mathcal{N}(\mathbf{0}, \mathbf{I}_{10})$ ?

### M25a.Q4 — Complément de Schur, loi marginale ou loi conditionnelle : quel bloc, quelle moyenne, quelle variance ? 🧠 ★ ⏱️ 6 min
*Fiche §4 · parcours C, E*

$\mathbf{x} = (x_1, x_2, x_3) \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec $\boldsymbol{\mu} = (1, 2, 3)$ et $\boldsymbol{\Sigma} = \begin{pmatrix} 4 & 2 & 0 \\ 2 & 3 & 1 \\ 0 & 1 & 2 \end{pmatrix}$.

1. La loi marginale de $(x_1, x_3)$ ?
2. Vrai ou faux : $x_1$ et $x_3$ sont indépendantes.
3. La variance de $x_1$ sachant $x_2$ ?
4. Vrai ou faux : $x_1$ et $x_3$ restent indépendantes sachant $x_2$.
5. Vrai ou faux : la variance de $x_1$ sachant $x_2$ est plus grande quand la valeur lue de $x_2$ est loin de sa moyenne.
6. $\det\boldsymbol{\Sigma}$, par le complément de Schur du bloc $\Sigma_{22} = (3)$ ?
7. Vrai ou faux : $(\boldsymbol{\Sigma}^{-1})_{11} = \frac{1}{\Sigma_{11}}$.

### M25a.Q5 — Fusionner des mesures et mettre à jour un a priori gaussien : précisions, moyennes pondérées et prédictive 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Deux mesures indépendantes d'une même longueur : 10 cm (erreur de variance 4 cm²) et 14 cm (variance 12 cm²). La longueur fusionnée et sa variance ?
2. Vrai ou faux : la variance fusionnée est plus petite que chacune des deux variances.
3. On ajoute une troisième mesure, de variance infinie. Que change-t-elle ?
4. $x \sim \mathcal{N}(4, 2)$ et $y = 3x + w$, avec $w \sim \mathcal{N}(0, 7)$ indépendant de $x$ : la loi de $y$, et $\operatorname{Cov}(x, y)$ ?
5. Vrai ou faux : dans une régression linéaire bayésienne, la variance de la prédictive tend vers 0 quand le nombre de données tend vers l'infini.
6. $\mathbf{m}_0 = \mathbf{0}$, $\mathbf{S}_0 = 2\,\mathbf{I}$ et $\sigma^2 = 0{,}5$ : de quelle régression ridge (quelle pénalité) $\mathbf{m}_N$ est-il la solution ?

### M25a.Q6 — Le maximum de vraisemblance de μ et Σ : diviser par n, et une covariance singulière quand n ≤ d 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

1. $n = 5$ vecteurs de $\mathbb{R}^3$ : le rang maximal de la matrice de dispersion $\mathbf{S}$ ? $\hat{\boldsymbol{\Sigma}}$ peut-elle être inversible ?
2. $n = 3$ vecteurs de $\mathbb{R}^3$ : que dire de $\hat{\boldsymbol{\Sigma}}$ ?
3. Vrai ou faux : dès que $n > d$, $\hat{\boldsymbol{\Sigma}}$ est inversible. (Pense aux trois points $(1, 0)$, $(3, 2)$, $(5, 4)$.)
4. `X` est un tableau de forme $(n, d)$, une donnée par ligne. Quelle forme a `np.cov(X)`, et par quoi divise-t-il ?
5. Pour $n = 10$ données, $\mathbb{E}[\hat{\boldsymbol{\Sigma}}] = c\,\boldsymbol{\Sigma}$ : que vaut $c$ ?
6. Vrai ou faux : la moyenne qui maximise la vraisemblance est $\bar{\mathbf{x}}$, quelle que soit $\boldsymbol{\Sigma}$.
7. Au maximum, que vaut $\operatorname{tr}(\hat{\boldsymbol{\Sigma}}^{-1}\mathbf{S})$ ?

### M25a.Q7 — La divergence KL continue en situations : deux supports qui ne se couvrent pas, deux lois exponentielles, une loi produit, et les deux sens 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Un capteur de température mesure toujours entre −10 °C et 40 °C. Un modèle $p$ dit « uniforme sur $[0, 30]$ », un modèle $q$ dit « uniforme sur $[-10, 40]$ ». Que valent $\mathrm{KL}(p \,\|\, q)$ et $\mathrm{KL}(q \,\|\, p)$ ?
2. La durée de vie d'un composant suit $p$, exponentielle de moyenne 1 000 h ; on la modélise par $q$, exponentielle de moyenne 800 h. $\mathrm{KL}(p \,\|\, q)$ est-elle finie ?
3. Même $p$, mais $q$ est maintenant la loi uniforme sur $[0, 5\,000]$ h. $\mathrm{KL}(p \,\|\, q)$ est-elle finie ? Et $\mathrm{KL}(q \,\|\, p)$ ?
4. Une station mesure une température et une pression, indépendantes sous $p$ comme sous $q$. Sur la température seule, la KL de $p$ à $q$ vaut $0{,}12$ nat ; sur la pression seule, $0{,}05$ nat. Et sur le couple ?
5. Vrai ou faux : si, sous $q$, la température et la pression sont corrélées, la réponse précédente reste toujours juste.
6. Vrai ou faux : la fonction qu'on intègre, $p\ln\frac pq$, est positive en tout point.
7. Vrai ou faux : quand $\mathrm{KL}(p \,\|\, q)$ est finie, $\mathrm{KL}(q \,\|\, p)$ l'est aussi.

### M25a.Q8 — Ligne droite ou arc de grand cercle : extrémités, norme et angle parcouru 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

$\mathbf{u}$ et $\mathbf{v}$ sont deux vecteurs unitaires d'angle $\Omega = 100°$.

1. $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; 0)$ et $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; 1)$ ?
2. La norme du milieu de la ligne droite, $\frac12(\mathbf{u} + \mathbf{v})$ ?
3. L'angle entre $\mathbf{u}$ et $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; 0{,}3)$ ?
4. La norme de $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; 0{,}3)$ ?
5. Vrai ou faux : entre deux vecteurs de normes 2 et 5, le slerp garde une norme constante.
6. Sur la sphère unité, quelle longueur d'arc le point $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; t)$ parcourt-il quand $t$ passe de 0,2 à 0,7 ?
7. Vrai ou faux : si l'on ramène sur la sphère chaque point de la ligne droite (en le divisant par sa norme), on parcourt le même arc que le slerp, mais pas à vitesse angulaire constante.

<a id="rappels"></a>

## 🔁 Rappels

### M25a.R1 — Le changement de variable en dimension 1 et les coordonnées polaires (M02b) 🔁 ★ ⏱️ 6 min
*Fiche §2 et §3 · parcours C, E*

1. $X \sim \mathcal{N}(0, 1)$ et $Y = 3X - 2$ : la densité de $Y$ par la formule du changement de variable, puis sa loi ?
2. $X$ suit la loi uniforme sur $]0, 1]$ et $Y = -\ln X$ : la densité de $Y$ ?
3. En coordonnées polaires, par quoi remplace-t-on $\mathrm{d}x\,\mathrm{d}y$ ?
4. $\iint_{\mathbb{R}^2}e^{-(x^2 + y^2)/2}\,\mathrm{d}x\,\mathrm{d}y$ ?
5. $\int_0^{+\infty}r\,e^{-r^2/2}\,\mathrm{d}r$ ?
6. Vrai ou faux : pour $g$ strictement décroissante, $f_Y(y) = f_X\big(g^{-1}(y)\big)\,(g^{-1})'(y)$.

### M25a.R2 — Le théorème spectral, Cholesky et la covariance AΣAᵀ (M12c) 🔁 ★ ⏱️ 6 min
*Fiche §2 et §3 · parcours C, E*

1. Le facteur de Cholesky de $\boldsymbol{\Sigma} = \begin{pmatrix} 25 & 10 \\ 10 & 5 \end{pmatrix}$ ?
2. $\det\boldsymbol{\Sigma}$, à partir de $\mathbf{L}$ ?
3. Les valeurs propres de $\begin{pmatrix} 6 & 2 \\ 2 & 9 \end{pmatrix}$, et un vecteur propre pour chacune ?
4. $\mathbf{x}$ a pour covariance la matrice $\boldsymbol{\Sigma}$ de la question 1 : la variance de $x_1 - x_2$ ?
5. Vrai ou faux : toute matrice de covariance est définie positive.
6. Pourquoi $\mathbf{L}\mathbf{L}^\top$ est-elle symétrique et définie positive quand $\mathbf{L}$ est une matrice carrée inversible ?

### M25a.R3 — Les gradients de ln det X et de tr(AX) par rapport à une matrice (M18) 🔁 ★ ⏱️ 6 min
*Fiche §6 · parcours C*

1. $\nabla_{\mathbf{X}}\ln\det\mathbf{X}$ en $\mathbf{X} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$ ?
2. $\nabla_{\mathbf{X}}\operatorname{tr}(\mathbf{A}\mathbf{X})$ pour $\mathbf{A} = \begin{pmatrix} 0 & 5 \\ -2 & 1 \end{pmatrix}$ ?
3. Que devient $\nabla_{\mathbf{X}}\ln\det\mathbf{X}$ pour $\mathbf{X}$ symétrique définie positive ?
4. Écris $\mathbf{z}^\top\mathbf{A}\mathbf{z}$ comme une trace.
5. $\ln\det(c\,\mathbf{X})$, pour $\mathbf{X}$ de taille $n \times n$ et $c > 0$ ?
6. Vrai ou faux : $\nabla_{\mathbf{X}}\operatorname{tr}(\mathbf{X}\mathbf{A}) = \mathbf{A}^\top$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- une valeur exacte entre guillemets, écrite avec des entiers, des fractions, `sqrt`, `pi`, `ln` et `exp`, comme `"sqrt(5)/3"` ou `"2*ln(7)"` ;
- une expression entre guillemets, comme `"x*exp(-x)"` ;
- une forme comme NumPy l'affiche, comme `(7, 2)` ;
- `True` ou `False` pour un vrai ou faux.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M25a.1 — La densité d'un couple gaussien (température et humidité d'une serre) en deux points : distance de Mahalanobis contre distance euclidienne ✏️ ★ ⏱️ 25 min
**Objectif :** évaluer une densité gaussienne de dimension 2 et sa log-densité par Cholesky, et voir que la distance de Mahalanobis, pas la distance euclidienne, décide de la densité.
**Prérequis :** fiche §1 ; M12c · **Parcours :** C, E

Dans une serre, la température $T$ (en °C) et l'humidité relative $H$ (en %) relevées à midi forment un vecteur $\mathbf{x} = (T, H) \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec
$$\boldsymbol{\mu} = \begin{pmatrix} 21 \\ 65 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 4 & -6 \\ -6 & 34 \end{pmatrix}.$$
Deux relevés : $\mathbf{x}_P = (23, 68)$ (chaud et humide) et $\mathbf{x}_Q = (23, 60)$ (chaud et sec).

| | Question | Réponse attendue |
|---|---|---|
| a | $\det\boldsymbol{\Sigma}$ | un entier |
| b | $\boldsymbol{\Sigma}^{-1}$ | une matrice (ses coefficients sont des décimaux exacts) |
| c | le facteur de Cholesky $\mathbf{L}$ | une matrice |
| d | $\Delta^2(\mathbf{x}_P)$ et $\Delta^2(\mathbf{x}_Q)$, dans cet ordre | une liste de 2 nombres |
| e | la densité au point le plus probable, $p(\boldsymbol{\mu})$ | une valeur exacte, entre guillemets |
| f | $\ln p(\mathbf{x}_P)$ et $\ln p(\mathbf{x}_Q)$, dans cet ordre | une liste de 2 nombres (2 décimales) |
| g | le rapport $\frac{p(\mathbf{x}_Q)}{p(\mathbf{x}_P)}$ | un nombre (4 décimales) |
| h | la distance euclidienne de $\mathbf{x}_Q$ à $\boldsymbol{\mu}$ | une valeur exacte, entre guillemets |
| i | vrai ou faux : $\mathbf{x}_Q$, plus loin de $\boldsymbol{\mu}$ que $\mathbf{x}_P$ en distance euclidienne, a pourtant une densité plus grande | `True` ou `False` |

Dans ta copie : calcule la corrélation de $T$ et $H$ et dis ce qu'elle veut dire dans la serre. Calcule $\Delta^2$ deux fois, par $\boldsymbol{\Sigma}^{-1}$ et par le système triangulaire $\mathbf{L}\mathbf{y} = \mathbf{x} - \boldsymbol{\mu}$. Pourquoi la distance euclidienne entre deux relevés n'a-t-elle pas de sens physique ici ? Explique, sans formule, pourquoi le relevé sec est plus typique que le relevé humide à la même température.

### Ex M25a.2 — Trois mesures corrélées : la loi d'une somme pondérée et d'une différence, puis un tirage μ + Lε par Cholesky et sa covariance ✏️ ★★ ⏱️ 35 min
**Objectif :** calculer la loi d'images linéaires d'un vecteur gaussien, tirer un vecteur par Cholesky, et voir ce que donne une matrice mal transposée.
**Prérequis :** fiche §2 ; M12c · **Parcours :** C, E

Une machine pose un revêtement de route en trois couches. Leurs épaisseurs $\mathbf{x} = (x_1, x_2, x_3)$, en millimètres, varient d'un mètre de route à l'autre et suivent $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec
$$\boldsymbol{\mu} = \begin{pmatrix} 40 \\ 60 \\ 30 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 9 & 3 & -9 \\ 3 & 10 & 0 \\ -9 & 0 & 11 \end{pmatrix}.$$
La pose coûte 2 €, 1 € et 3 € par millimètre et par mètre carré pour les couches 1, 2 et 3 : le coût est $c = 2x_1 + x_2 + 3x_3$, en euros par mètre carré. On note $\delta = x_2 - x_1$ l'écart d'épaisseur entre les deux premières couches.

| | Question | Réponse attendue |
|---|---|---|
| a | le facteur de Cholesky $\mathbf{L}$ de $\boldsymbol{\Sigma}$ | une matrice $3 \times 3$ |
| b | $\det\boldsymbol{\Sigma}$ | un entier |
| c | la moyenne et la variance de $c$ | une liste de 2 nombres |
| d | la moyenne et la variance de $\delta$ | une liste de 2 nombres |
| e | la matrice de covariance du couple $(c, \delta)$ | une matrice $2 \times 2$ |
| f | le tirage $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ pour $\boldsymbol{\varepsilon} = (1 ;\ -0{,}5 ;\ 1{,}5)$ | une liste de 3 nombres |
| g | un collègue tire $\boldsymbol{\mu} + \mathbf{L}^\top\boldsymbol{\varepsilon}$ : la covariance de ses tirages | une matrice $3 \times 3$ |
| h | vrai ou faux : $c$ et $\delta$ sont indépendants | `True` ou `False` |

Dans ta copie : vérifie $\mathbf{L}\mathbf{L}^\top = \boldsymbol{\Sigma}$. Écris $(c, \delta)$ sous la forme $\mathbf{A}\mathbf{x}$ avec une matrice $\mathbf{A}$ de forme $(2, 3)$, et retrouve c), d) et e) d'un seul calcul $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$. Calcule la corrélation de $c$ et $\delta$, et la probabilité que le coût dépasse 245 € par mètre carré (table de la loi normale, M02b). Pourquoi le tirage de f) a-t-il la bonne loi, et pas celui du collègue ?

### Ex M25a.3 — Les ellipses à 90 % et à 95 % des composantes du vent sur un site : axes, demi-axes, aire, et la part des relevés dans l'ellipse de niveau c ✏️ ★★ ⏱️ 30 min
**Objectif :** tracer les ellipses de niveau d'une gaussienne de covariance pleine et calculer leur masse.
**Prérequis :** fiche §3 ; M12c · **Parcours :** C, E

Sur un site, les deux composantes horizontales du vent à 10 m de hauteur, $\mathbf{x} = (u, v)$ en m/s ($u$ vers l'est, $v$ vers le nord), suivent $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec
$$\boldsymbol{\mu} = \begin{pmatrix} 2{,}5 \\ 1 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 14 & 3 \\ 3 & 6 \end{pmatrix}.$$
On appelle « ellipse à 90 % » l'ellipse $\Delta(\mathbf{x}) \le c$ qui contient 90 % des relevés.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\boldsymbol{\Sigma}$, de la plus grande à la plus petite | une liste de 2 nombres |
| b | la pente du grand axe (le rapport $\frac{v}{u}$ le long de cet axe) | une fraction irréductible, entre guillemets |
| c | les niveaux $c^2$ des ellipses à 90 % et à 95 %, dans cet ordre | une liste de 2 nombres (4 décimales) |
| d | les demi-axes de l'ellipse à 90 %, le grand puis le petit (en m/s) | une liste de 2 nombres (4 décimales) |
| e | les demi-axes de l'ellipse à 95 %, le grand puis le petit | une liste de 2 nombres (4 décimales) |
| f | les aires des ellipses à 90 % et à 95 % (en m²/s²) | une liste de 2 nombres (2 décimales) |
| g | la part des relevés dans l'ellipse de niveau $c = 1{,}4$ | un nombre (4 décimales) |
| h | $\Delta^2$ du relevé $(8{,}5 ;\ 0)$ | une fraction irréductible, entre guillemets |
| i | vrai ou faux : ce relevé est dans l'ellipse à 90 % | `True` ou `False` |

Dans ta copie : donne les deux vecteurs propres unitaires et l'angle du grand axe avec l'est, en degrés. Esquisse les deux ellipses autour de $\boldsymbol{\mu}$. Pourquoi l'aire fait-elle intervenir $\sqrt{\det\boldsymbol{\Sigma}}$, et pas $\det\boldsymbol{\Sigma}$ ? Le relevé de h) est à $\sqrt{37} \approx 6{,}08$ m/s de $\boldsymbol{\mu}$, plus que le petit demi-axe de l'ellipse à 90 % : comment peut-il être dedans ? Calcule ses coordonnées dans la base des vecteurs propres.

### Ex M25a.4 — Un capteur en panne estimé par ses deux voisins : complément de Schur, loi conditionnelle en dimension 3, et l'écart-type gagné ✏️ ★★ ⏱️ 35 min
**Objectif :** calculer une loi conditionnelle sachant deux coordonnées corrélées entre elles, par le complément de Schur, et lire ce que la mesure apporte.
**Prérequis :** fiche §4 ; M09a · **Parcours :** C, E

Trois capteurs de température sont alignés le long d'un mur d'entrepôt. Leurs mesures $\mathbf{x} = (x_1, x_2, x_3)$, en °C, suivent $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec
$$\boldsymbol{\mu} = \begin{pmatrix} 18 \\ 17 \\ 15 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 4 & 3 & 1 \\ 3 & 4 & 2 \\ 1 & 2 & 4 \end{pmatrix}.$$
Le capteur 2 tombe en panne ; ses voisins lisent $x_1 = 19{,}5$ et $x_3 = 14$. On cherche $a = \{2\}$ sachant $b = \{1, 3\}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\boldsymbol{\Sigma}_{bb}^{-1}$ | une matrice (4 décimales) |
| b | les deux poids $\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}$ des voisins | une liste de 2 nombres (4 décimales) |
| c | la variance de $x_2$ sachant $x_1$ et $x_3$ (le complément de Schur) | une fraction irréductible, entre guillemets |
| d | la moyenne de $x_2$ sachant $x_1 = 19{,}5$ et $x_3 = 14$ | un nombre (2 décimales) |
| e | l'écart-type gagné : l'écart-type de $x_2$ avant la lecture moins celui après | un nombre (4 décimales) |
| f | si seul le capteur 1 avait été lu ($x_1 = 19{,}5$) : la moyenne et la variance de $x_2$ | une liste de 2 nombres (3 décimales) |
| g | $\det\boldsymbol{\Sigma}$ | un entier |
| h | la précision $\Lambda_{22}$, le coefficient $(2, 2)$ de $\boldsymbol{\Sigma}^{-1}$ | une fraction irréductible, entre guillemets |
| i | vrai ou faux : si $x_3$ avait lu 16 °C, la variance de $x_2$ sachant $x_1$ et $x_3$ aurait été différente | `True` ou `False` |

Dans ta copie : vérifie $\det\boldsymbol{\Sigma} = \det\boldsymbol{\Sigma}_{bb} \times (\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{bb})$. Pourquoi le capteur 1 pèse-t-il deux fois plus que le capteur 3 ? Si l'on ignorait la corrélation des deux voisins entre eux ($\Sigma_{13} = 0$), quels poids et quelle variance trouverait-on, et pourquoi est-ce trop optimiste ? Donne un intervalle qui contient $x_2$ avec la probabilité 0,95.

### Ex M25a.5 — Fusionner trois mesures d'une même distance : le produit de densités gaussiennes, des précisions qui s'additionnent, un ordre sans importance ✏️ ★ ⏱️ 20 min
**Objectif :** fusionner des mesures gaussiennes par le produit de leurs densités, et vérifier que l'ordre des fusions ne change rien.
**Prérequis :** fiche §5 · **Parcours :** C, E

On mesure la distance entre deux bornes, d'environ 48 m, avec trois instruments. Chacun donne la distance sous la forme 48 m $+\ x$, avec $x$ en centimètres, et une erreur gaussienne centrée, indépendante des autres : le mètre ruban lit $x = 31$ cm (écart-type 3 cm), le télémètre laser $x = 27$ cm (écart-type 2 cm), la roue de mesure $x = 36$ cm (écart-type 6 cm). Sans autre information, on fusionne les mesures en multipliant leurs densités (fiche §5).

| | Question | Réponse attendue |
|---|---|---|
| a | après la fusion du mètre ruban et du télémètre : la moyenne et la variance (en cm et cm²) | une liste de 2 nombres (4 décimales) |
| b | après la fusion du résultat de a) et de la roue | une liste de 2 nombres (4 décimales) |
| c | dans l'autre ordre : la fusion de la roue et du mètre ruban, d'abord | une liste de 2 nombres (2 décimales) |
| d | vrai ou faux : fusionner ensuite c) et le télémètre redonne b) | `True` ou `False` |
| e | le poids du télémètre dans la moyenne finale | une fraction irréductible, entre guillemets |
| f | l'écart-type final (en cm) | un nombre (4 décimales) |
| g | vrai ou faux : ajouter la roue, l'instrument le moins précis, a augmenté l'incertitude | `True` ou `False` |

Dans ta copie : écris le produit des deux premières densités comme $\kappa\,\mathcal{N}(x \mid \mu_3, \sigma_3^2)$ et calcule $\kappa$ ; que dit-il de l'accord des deux instruments ? Écris la formule qui fusionne les trois mesures d'un coup, et explique avec elle pourquoi l'ordre ne compte pas. Que deviendrait la moyenne finale si l'on faisait la moyenne simple des trois lectures ?

### Ex M25a.6 — Étalonner un thermomètre par la régression linéaire bayésienne : loi jointe, évidence, posterior de (a, b), et prédictive près et loin des points d'étalonnage ✏️ ★★ ⏱️ 45 min
**Objectif :** dérouler une régression linéaire bayésienne à deux paramètres : loi jointe, évidence, loi a posteriori et prédictives.
**Prérequis :** fiche §5 ; M09b · **Parcours :** C

Un thermomètre électronique est étalonné dans deux bains de référence, à $T = 0$ °C (glace fondante) et à $T = 100$ °C (eau bouillante). Son erreur $e = y - T$ (la lecture moins la vraie température) suit le modèle
$$e = a + b\,\frac{T}{100} + w, \qquad w \sim \mathcal{N}(0, \sigma^2), \quad \sigma^2 = 0{,}04,$$
où $a$ est le décalage, $b$ l'erreur de pente sur 100 °C et $w$ le bruit de lecture (dans cet exercice, $a$ et $b$ sont ces deux paramètres, pas des indices de blocs). Les features sont $\boldsymbol{\phi}(T) = (1, \frac{T}{100})$, donc $\boldsymbol{\Phi} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$. A priori, $\boldsymbol{\theta} = (a, b) \sim \mathcal{N}(\mathbf{0}, \mathbf{S}_0)$, avec $\mathbf{S}_0 = \operatorname{diag}(0{,}25 ;\ 1)$. Le thermomètre lit 0,3 °C dans la glace et 99,4 °C dans l'eau bouillante : $\mathbf{e} = (0{,}3 ;\ -0{,}6)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la covariance des deux erreurs $\mathbf{e}$ avant l'étalonnage (celle de l'évidence) | une matrice $2 \times 2$ |
| b | la covariance croisée $\operatorname{Cov}(\boldsymbol{\theta}, \mathbf{e})$ | une matrice $2 \times 2$ |
| c | le logarithme de l'évidence, $\ln p(\mathbf{e})$ | un nombre (4 décimales) |
| d | la covariance a posteriori $\mathbf{S}_N$ | une matrice (4 décimales) |
| e | la moyenne a posteriori $\mathbf{m}_N$ | une liste de 2 nombres (4 décimales) |
| f | la prédictive de l'erreur d'une lecture à $T_\star = 50$ °C : sa moyenne et sa variance | une liste de 2 nombres (4 décimales) |
| g | la même à $T_\star = 200$ °C | une liste de 2 nombres (4 décimales) |
| h | la corrélation a posteriori de $a$ et $b$ | un nombre (4 décimales) |
| i | vrai ou faux : à 200 °C, la variance de la prédictive après l'étalonnage est plus petite que celle d'avant | `True` ou `False` |

Dans ta copie : écris la loi jointe de $(a, b, e_1, e_2)$, une gaussienne de dimension 4. Quels blocs de cette matrice as-tu déjà calculés en a) et b) ? Pourquoi $a$ et $b$, indépendants a priori, sont-ils corrélés négativement après l'étalonnage ? Pour quelle température la variance prédictive est-elle la plus petite, et pourquoi n'est-ce pas exactement au milieu des deux bains ?

### Ex M25a.7 — La divergence KL continue entre deux lois exponentielles et entre deux lois uniformes : les deux sens, une KL infinie, et deux durées de vie indépendantes ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer des KL continues par leur définition, dans les deux sens, repérer une KL infinie et appliquer l'additivité.
**Prérequis :** fiche §7 ; M02a, M02b · **Parcours :** C, E

La loi exponentielle de paramètre $\lambda > 0$ a pour densité $\lambda e^{-\lambda x}$ sur $[0, +\infty[$, et pour moyenne $\frac1\lambda$. La durée de vie d'une batterie, en années, suit une loi exponentielle de moyenne 3 ans chez un fournisseur (la loi $p$) ; la fiche technique annonce une loi exponentielle de moyenne 8 ans (la loi $q$).

| | Question | Réponse attendue |
|---|---|---|
| a | la KL de la loi exponentielle de paramètre $a$ à celle de paramètre $b$, en fonction de $a$ et $b$ (ici, $a$ et $b$ sont des paramètres) | une expression en `a` et `b`, entre guillemets |
| b | $\mathrm{KL}(p \,\|\, q)$ pour les batteries | un nombre (3 décimales) |
| c | $\mathrm{KL}(q \,\|\, p)$ | un nombre (3 décimales) |
| d | un temps d'attente, en minutes, suit la loi uniforme sur $[2, 5]$ (la loi $p'$) ; un modèle propose la loi uniforme sur $[0, 10]$ (la loi $q'$) : $\mathrm{KL}(p' \,\|\, q')$ | un nombre (3 décimales) |
| e | vrai ou faux : $\mathrm{KL}(q' \,\|\, p')$ est finie | `True` ou `False` |
| f | le moteur du même appareil dure, en années, une loi exponentielle de moyenne 6 ans ($p_2$) ; la fiche technique annonce une moyenne de 10 ans ($q_2$) : $\mathrm{KL}(p_2 \,\|\, q_2)$ | un nombre (3 décimales) |
| g | la batterie et le moteur sont indépendants sous la loi réelle comme sous la fiche technique : la KL de la loi réelle du couple (batterie, moteur) à celle de la fiche | un nombre (3 décimales) |
| h | vrai ou faux : si, d'après la fiche technique, les deux durées de vie dépendaient l'une de l'autre, g) serait toujours égal à la somme de b) et de f) | `True` ou `False` |

Dans ta copie : établis a) par la définition, avec $\mathbb{E}_p[x] = \frac1a$ ; vérifie que a) est positive ou nulle, avec $\ln u \le u - 1$, et nulle seulement pour $a = b$. Pour e), dis sur quelle région la loi de la première place pèse sans que celle de la seconde place la couvre. Pourquoi b) et c) diffèrent-ils ?

### Ex M25a.8 — Deux réglages d'une machine de découpe, deux gaussiennes en dimension 2 des erreurs de position : la KL dans les deux sens, et le cas de même covariance ✏️ ★★ ⏱️ 30 min
**Objectif :** appliquer la formule de la KL entre deux gaussiennes de covariances pleines, dans les deux sens, et lire ses trois termes.
**Prérequis :** fiche §7 · **Parcours :** C, E

Une machine de découpe laser positionne sa tête ; l'erreur de position $(x, y)$, en centièmes de millimètre, suit la loi $p_0 = \mathcal{N}(\boldsymbol{\mu}_0, \boldsymbol{\Sigma}_0)$ avec le réglage A et la loi $p_1 = \mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)$ avec le réglage B :
$$\boldsymbol{\mu}_0 = \begin{pmatrix} 2 \\ -1 \end{pmatrix}, \quad \boldsymbol{\Sigma}_0 = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}, \qquad \boldsymbol{\mu}_1 = \begin{pmatrix} 3 \\ -2 \end{pmatrix}, \quad \boldsymbol{\Sigma}_1 = \begin{pmatrix} 6 & -1 \\ -1 & 2 \end{pmatrix}.$$
On note $\boldsymbol{\delta} = \boldsymbol{\mu}_1 - \boldsymbol{\mu}_0$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0)$ | une fraction irréductible, entre guillemets |
| b | $\boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta}$ | une fraction irréductible, entre guillemets |
| c | $\ln\frac{\det\boldsymbol{\Sigma}_1}{\det\boldsymbol{\Sigma}_0}$ | une valeur exacte, entre guillemets |
| d | $\mathrm{KL}(p_0 \,\|\, p_1)$ | un nombre (4 décimales) |
| e | $\operatorname{tr}(\boldsymbol{\Sigma}_0^{-1}\boldsymbol{\Sigma}_1)$ | une fraction irréductible, entre guillemets |
| f | $\boldsymbol{\delta}^\top\boldsymbol{\Sigma}_0^{-1}\boldsymbol{\delta}$ | une fraction irréductible, entre guillemets |
| g | $\mathrm{KL}(p_1 \,\|\, p_0)$ | un nombre (4 décimales) |
| h | un réglage C a la covariance $\boldsymbol{\Sigma}_0$ du réglage A et la moyenne $\boldsymbol{\mu}_1$ du réglage B : la KL de la loi du réglage A à celle du réglage C | une fraction irréductible, entre guillemets |
| i | la différence des entropies différentielles $h(p_1) - h(p_0)$, en nats | un nombre (4 décimales) |

Dans ta copie : pour d) et g), écris les trois termes de la formule et dis ce que chacun compare. Vérifie que la KL de h) est la même dans les deux sens. Lequel des deux réglages a l'erreur la plus dispersée, au sens de l'entropie ? Retrouve i) par la formule de l'entropie différentielle de la fiche §7.

### Ex M25a.9 — La route orthodromique entre deux villes : angle au centre, point au tiers du trajet par le slerp, et profondeur du milieu de la corde ✏️ ★★ ⏱️ 30 min
**Objectif :** appliquer le slerp à un trajet sur la sphère terrestre : passer des coordonnées géographiques aux vecteurs, puis calculer l'angle, l'arc, la corde et un point du trajet.
**Prérequis :** fiche §8 ; R9, M07 · **Parcours :** C, E

Un avion va de Brest (48,39° N ; 4,49° O) à New York (40,71° N ; 74,01° O) par le plus court chemin à la surface de la Terre, une route **orthodromique** (un arc de grand cercle). On prend la Terre pour une sphère de rayon $R = 6\,371$ km, et le repère de la fiche (§8, « Arc et corde ») : le point de latitude $\varphi$ et de longitude $\lambda$ a pour vecteur unitaire $(\cos\varphi\cos\lambda,\ \cos\varphi\sin\lambda,\ \sin\varphi)$, une longitude ouest étant négative. On note $\mathbf{u}$ le vecteur unitaire de Brest, $\mathbf{v}$ celui de New York, et $\Omega$ leur angle.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{u}$ | une liste de 3 nombres (4 décimales) |
| b | $\mathbf{v}$ | une liste de 3 nombres (4 décimales) |
| c | l'angle au centre $\Omega$, en radians | un nombre (4 décimales) |
| d | la longueur de la route, en km | un nombre entier |
| e | la longueur de la corde, le tunnel droit qui joindrait les deux villes, en km | un nombre entier |
| f | le vecteur unitaire du point situé au tiers du trajet, $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; \frac13)$ | une liste de 3 nombres (4 décimales) |
| g | la latitude et la longitude de ce point, en degrés (longitude ouest négative) | une liste de 2 nombres (2 décimales) |
| h | la profondeur du milieu de la corde sous la surface, $R\big(1 - \cos\frac\Omega2\big)$, en km | un nombre entier |
| i | vrai ou faux : le point situé au tiers de la corde, ramené sur la sphère, est à l'angle $\frac\Omega3$ de $\mathbf{u}$ | `True` ou `False` |

Dans ta copie : vérifie que f) est de norme 1 et fait l'angle $\frac\Omega3$ avec $\mathbf{u}$. La latitude trouvée en g) est plus grande que celles des deux villes : qu'en déduis-tu sur la forme de la route sur une carte où les parallèles sont horizontaux ? Calcule l'angle avec $\mathbf{u}$ du point de i).

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M25a.10 — Le changement de variable multivarié : la densité de μ + Lε est celle de N(μ, LLᵀ), et AX + b reste gaussien pour A inversible ∂ ★★ ⏱️ 30 min
**Objectif :** démontrer, par le théorème du changement de variable, la densité d'une image affine inversible d'un vecteur gaussien.
**Prérequis :** fiche §1 et §2 ; M12c, M17 · **Parcours :** C, E

$\boldsymbol{\varepsilon}$ suit $\mathcal{N}(\mathbf{0}, \mathbf{I}_d)$, de densité $(2\pi)^{-d/2}\exp\big(-\frac12\lVert\boldsymbol{\varepsilon}\rVert^2\big)$ (fiche §1). $\mathbf{L}$ est une matrice $d \times d$ triangulaire inférieure, de diagonale strictement positive, et $\boldsymbol{\mu} \in \mathbb{R}^d$. On admet le théorème du changement de variable (fiche §2, MML Théorème 6.16).

1. Soit $U(\boldsymbol{\varepsilon}) = \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$. Montre que $U$ est inversible, donne $U^{-1}$, la jacobienne de $U^{-1}$ et son déterminant.
2. Applique le théorème : écris la densité de $\mathbf{x} = U(\boldsymbol{\varepsilon})$. Montre que $\lVert\mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})\rVert^2 = (\mathbf{x} - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ et $\det\mathbf{L} = \sqrt{\det\boldsymbol{\Sigma}}$, avec $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$. Conclus : $\mathbf{x}$ a la densité de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ de la fiche §1.
3. Plus généralement, $\mathbf{x}$ a la densité de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec $\boldsymbol{\Sigma}$ définie positive, et $\mathbf{A}$ est une matrice carrée inversible. Montre que $\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{b}$ a la densité de $\mathcal{N}(\mathbf{A}\boldsymbol{\mu} + \mathbf{b}, \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top)$ : il te faudra $\det(\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top)$ et $(\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top)^{-1}$, et justifier que $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$ est définie positive.
4. Pour $\mathbf{A}$ de forme $(k, d)$ avec $k < d$, pourquoi ce théorème ne s'applique-t-il pas tel quel ? Par quel autre chemin la fiche (§2) obtient-elle quand même la loi de $\mathbf{A}\mathbf{x} + \mathbf{b}$ ?
5. Avec tes propres nombres : $d = 2$, $\mathbf{L} = \begin{pmatrix} 3 & 0 \\ -1 & 2 \end{pmatrix}$, $\boldsymbol{\mu} = (1, 0)$. Calcule la densité de $\mathbf{x} = \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ au point $(4, 1)$ par l'antécédent de ce point (question 2), puis par la densité de $\mathcal{N}(\boldsymbol{\mu}, \mathbf{L}\mathbf{L}^\top)$, et compare.

### Ex M25a.11 — La masse d'une ellipse de Mahalanobis en dimension 2 vaut 1 − e^{−c²/2} ; la densité de la norme en dimension d, et son mode √(d − 1) ∂ ★★ ⏱️ 30 min
**Objectif :** démontrer la masse d'une ellipse de niveau en dimension 2, en déduire la loi de la norme d'un tirage, et étudier cette loi en dimension $d$.
**Prérequis :** fiche §3 ; M02a, M02b · **Parcours :** C, E

1. $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ dans $\mathbb{R}^2$, $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$, et $\boldsymbol{\varepsilon} = \mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})$. Montre que $\boldsymbol{\varepsilon}$ suit $\mathcal{N}(\mathbf{0}, \mathbf{I}_2)$ (∂ M25a.10) et que $\Delta(\mathbf{x}) = \lVert\boldsymbol{\varepsilon}\rVert$. Déduis-en que $P\big(\Delta(\mathbf{x}) \le c\big) = P\big(\lVert\boldsymbol{\varepsilon}\rVert \le c\big)$.
2. Calcule $P\big(\lVert\boldsymbol{\varepsilon}\rVert \le c\big)$, l'intégrale de la densité de $\mathcal{N}(\mathbf{0}, \mathbf{I}_2)$ sur le disque de rayon $c$, en coordonnées polaires (M02b §7). Conclus que la masse de l'ellipse $\Delta \le c$ vaut $1 - e^{-c^2/2}$, puis que l'ellipse de masse $1 - \beta$ a pour niveau $c^2 = -2\ln\beta$.
3. Déduis de 2 la densité de $r = \lVert\boldsymbol{\varepsilon}\rVert$ en dimension 2.
4. En dimension 3, on admet que $P(\lVert\boldsymbol{\varepsilon}\rVert \le \rho) = \int_0^\rho 4\pi r^2\,(2\pi)^{-3/2}e^{-r^2/2}\,\mathrm{d}r$ (la densité de $\boldsymbol{\varepsilon}$, constante sur chaque sphère de rayon $r$, multipliée par l'aire $4\pi r^2$ de cette sphère). Déduis-en la densité $f_3$ de la norme, et vérifie que son intégrale vaut 1, avec $\int_0^{+\infty}r^2e^{-r^2/2}\,\mathrm{d}r = \sqrt{\pi/2}$, que tu démontreras par une intégration par parties (M02a §3) et l'intégrale de Gauss.
5. En dimension $d \ge 2$, on admet que la densité de la norme est $f_d(r) = C_d\,r^{d-1}e^{-r^2/2}$ sur $[0, +\infty[$, pour une constante $C_d > 0$. Montre que $f_d$ est maximale en $r = \sqrt{d - 1}$, sans connaître $C_d$.
6. En dimension 17 : le mode de la norme ; le rapport $\frac{f_{17}(4)}{f_{17}(1)}$ entre la densité de la norme en $r = 4$ et en $r = 1$ ; et le rapport entre la densité de $\boldsymbol{\varepsilon}$ en un point de norme 1 et en un point de norme 4. Explique en deux phrases pourquoi les deux rapports vont en sens contraires.

### Ex M25a.12 — Le maximum de vraisemblance d'une gaussienne multivariée : μ̂ = x̄ et Σ̂ = S/n, par les gradients de ln det et de la trace ∂ ★★ ⏱️ 40 min
**Objectif :** démontrer les estimateurs du maximum de vraisemblance de $\boldsymbol{\mu}$ et $\boldsymbol{\Sigma}$, et justifier qu'il s'agit d'un maximum.
**Prérequis :** fiche §6 ; M05a, M09b, M12c, M18 · **Parcours :** C

$\mathbf{x}_1, \ldots, \mathbf{x}_n$ sont $n$ vecteurs de $\mathbb{R}^d$, $\bar{\mathbf{x}}$ leur moyenne et $\mathbf{S} = \sum_i(\mathbf{x}_i - \bar{\mathbf{x}})(\mathbf{x}_i - \bar{\mathbf{x}})^\top$ leur matrice de dispersion, supposée définie positive. $\ell(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ est la log-vraisemblance de la fiche §6, définie pour $\boldsymbol{\Sigma}$ symétrique définie positive.

1. À $\boldsymbol{\Sigma}$ fixée, calcule le gradient de $\ell$ par rapport à $\boldsymbol{\mu}$ (M09b §2), et montre qu'il s'annule seulement en $\boldsymbol{\mu} = \bar{\mathbf{x}}$.
2. Montre que $\sum_i(\mathbf{x}_i - \boldsymbol{\mu})(\mathbf{x}_i - \boldsymbol{\mu})^\top = \mathbf{S} + n(\bar{\mathbf{x}} - \boldsymbol{\mu})(\bar{\mathbf{x}} - \boldsymbol{\mu})^\top$. Déduis-en, avec l'astuce de la trace, que $\ell(\boldsymbol{\mu}, \boldsymbol{\Sigma}) \le \ell(\bar{\mathbf{x}}, \boldsymbol{\Sigma})$ pour toute $\boldsymbol{\Sigma}$ : 1 donne bien un maximum en $\boldsymbol{\mu}$.
3. Écris $\ell(\bar{\mathbf{x}}, \boldsymbol{\Sigma})$ en fonction de la précision $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$, sous la forme $\text{constante} + \frac n2\ln\det\boldsymbol{\Lambda} - \frac12\operatorname{tr}(\boldsymbol{\Lambda}\mathbf{S})$. Calcule son gradient par rapport à $\boldsymbol{\Lambda}$ avec les formules de M18 (rappelées au §6 de la fiche), et montre qu'il s'annule seulement en $\boldsymbol{\Lambda}^{-1} = \frac{\mathbf{S}}{n}$.
4. Montre que c'est un maximum. Avec $\hat{\boldsymbol{\Sigma}} = \frac{\mathbf{S}}{n} = \mathbf{C}\mathbf{C}^\top$ (Cholesky) et, pour une autre $\boldsymbol{\Sigma}$ définie positive, $\mathbf{B} = \mathbf{C}^\top\boldsymbol{\Sigma}^{-1}\mathbf{C}$, de valeurs propres $b_1, \ldots, b_d$ : montre que $\mathbf{B}$ est symétrique définie positive, que $\ell(\bar{\mathbf{x}}, \boldsymbol{\Sigma}) - \ell(\bar{\mathbf{x}}, \hat{\boldsymbol{\Sigma}}) = \frac n2\sum_j(\ln b_j - b_j + 1)$, puis conclus avec $\ln b \le b - 1$ (M05a), égalité seulement pour $b = 1$.
5. Donne la valeur de $\ell$ au maximum.
6. Avec tes propres nombres : quatre relevés de deux grandeurs, $(-1, 2)$, $(0, 0)$, $(3, 1)$ et $(2, 5)$. Calcule $\bar{\mathbf{x}}$, $\mathbf{S}$, $\hat{\boldsymbol{\Sigma}}$ et $\ell(\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Sigma}})$. Avec la formule de 2, calcule ce que perd la log-vraisemblance si l'on garde $\hat{\boldsymbol{\Sigma}}$ mais qu'on prend $\boldsymbol{\mu} = \mathbf{0}$ (un appareil supposé sans biais), puis vérifie-le en calculant $\ell(\mathbf{0}, \hat{\boldsymbol{\Sigma}})$ directement.

### Ex M25a.13 — L'inégalité de Jensen pour une variable continue, la positivité de la KL continue, et l'additivité de la KL sur des lois produits ∂ ★★ ⏱️ 35 min
**Objectif :** démontrer Jensen par une tangente, en déduire la positivité de la KL continue, et démontrer son additivité.
**Prérequis :** fiche §7 ; M05a, M06 · **Parcours :** C, E

1. $f$ est convexe et dérivable sur un intervalle $I$, $X$ une variable à valeurs dans $I$, d'espérance finie $m$ (on admet que $m \in I$), et $f(X)$ a une espérance. Avec la tangente à $f$ en $m$ (M05a §1), démontre $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$. Dis pourquoi l'inégalité change de sens pour $f$ concave.
2. Si de plus $f$ est strictement convexe, montre que l'égalité force $X = m$ avec la probabilité 1 (on admet qu'une variable positive ou nulle d'espérance nulle est nulle avec la probabilité 1).
3. $p$ et $q$ sont deux densités sur $\mathbb{R}^d$, et $q > 0$ partout où $p > 0$. Applique 1 au logarithme et à la variable $\frac{q(\mathbf{x})}{p(\mathbf{x})}$, avec $\mathbf{x} \sim p$, pour démontrer $\mathrm{KL}(p \,\|\, q) \ge 0$. Où sers-tu de $\int q \le 1$ sur le support de $p$ ? Que dire si $q$ s'annule sur une région où $p$ a une masse positive ?
4. Montre que $\mathrm{KL}(p \,\|\, q) = 0$ entraîne $p = q$ (sauf sur une région de volume nul), avec 2.
5. $p(\mathbf{x}, \mathbf{y}) = p_1(\mathbf{x})\,p_2(\mathbf{y})$ et $q(\mathbf{x}, \mathbf{y}) = q_1(\mathbf{x})\,q_2(\mathbf{y})$. Démontre $\mathrm{KL}(p \,\|\, q) = \mathrm{KL}(p_1 \,\|\, q_1) + \mathrm{KL}(p_2 \,\|\, q_2)$.
6. Sur le carré $[0, 1]^2$, $p$ est la loi uniforme et $q$ la loi de densité $q(x, y) = 1 + c\,(2x - 1)(2y - 1)$, avec $0 < \lvert c\rvert < 1$. Montre que $q$ est bien une densité, que ses deux marginales sont uniformes sur $[0, 1]$, puis que $\mathrm{KL}(p \,\|\, q) > \mathrm{KL}(p_1 \,\|\, q_1) + \mathrm{KL}(p_2 \,\|\, q_2)$. Quelle hypothèse de 5 manque ?

### Ex M25a.14 — La KL entre N(μ₀, Σ₀) et N(μ₁, Σ₁) en dimension d, par le lemme de la trace ; l'entropie différentielle de N(μ, Σ) ∂ ★★★ ⏱️ 45 min
**Objectif :** démontrer le lemme de la trace, la formule de la KL entre deux gaussiennes générales et l'entropie différentielle d'une gaussienne.
**Prérequis :** fiche §1 et §7 ; M12c · **Parcours :** C, E

$p_0 = \mathcal{N}(\boldsymbol{\mu}_0, \boldsymbol{\Sigma}_0)$ et $p_1 = \mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)$ sont deux lois de $\mathbb{R}^d$, de covariances définies positives, et $\boldsymbol{\delta} = \boldsymbol{\mu}_1 - \boldsymbol{\mu}_0$.

1. **Le lemme de la trace.** $\mathbf{x}$ a pour moyenne $\boldsymbol{\mu}$ et pour covariance $\boldsymbol{\Sigma}$ (gaussien ou non), $\mathbf{A}$ est une matrice $d \times d$ et $\mathbf{m} \in \mathbb{R}^d$. Démontre $\mathbb{E}\big[(\mathbf{x} - \mathbf{m})^\top\mathbf{A}(\mathbf{x} - \mathbf{m})\big] = \operatorname{tr}(\mathbf{A}\boldsymbol{\Sigma}) + (\boldsymbol{\mu} - \mathbf{m})^\top\mathbf{A}(\boldsymbol{\mu} - \mathbf{m})$.
2. Écris $\ln p_0(\mathbf{x}) - \ln p_1(\mathbf{x})$ avec la log-densité de la fiche §1.
3. Prends l'espérance sous $p_0$ avec le lemme, et démontre la formule de la KL de la fiche §7.
4. Montre que si $\boldsymbol{\Sigma}_0 = \boldsymbol{\Sigma}_1 = \boldsymbol{\Sigma}$, la KL vaut $\frac12\boldsymbol{\delta}^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\delta}$, et qu'elle est alors symétrique.
5. Démontre $h\big(\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})\big) = \frac12\ln\big((2\pi e)^d\det\boldsymbol{\Sigma}\big)$. Vérifie sur la formule de 3 la relation $\mathrm{KL}(p_0 \,\|\, p_1) = -h(p_0) - \mathbb{E}_{p_0}[\ln p_1(\mathbf{x})]$.
6. Montre que la formule donne 0 quand $\boldsymbol{\mu}_0 = \boldsymbol{\mu}_1$ et $\boldsymbol{\Sigma}_0 = \boldsymbol{\Sigma}_1$.
7. Sans passer par Jensen, montre que $\operatorname{tr}(\mathbf{M}) - d - \ln\det\mathbf{M} \ge 0$ pour $\mathbf{M} = \boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0$, avec égalité seulement si $\boldsymbol{\Sigma}_0 = \boldsymbol{\Sigma}_1$ (écris $\boldsymbol{\Sigma}_1 = \mathbf{L}_1\mathbf{L}_1^\top$, regarde la matrice symétrique $\mathbf{L}_1^{-1}\boldsymbol{\Sigma}_0\mathbf{L}_1^{-\top}$, et sers-toi de $\ln b \le b - 1$). Déduis-en, à partir de la formule, que la KL entre deux gaussiennes est positive ou nulle.

### Ex M25a.15 — Le slerp entre deux vecteurs de même norme reste sur la sphère et avance d'un angle constant ; sa limite quand l'angle tend vers 0 ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer les quatre propriétés du slerp de la fiche §8.
**Prérequis :** fiche §8 ; R7, R9, M12b, M22 · **Parcours :** C, E

$\mathbf{u}$ et $\mathbf{v}$ sont deux vecteurs de $\mathbb{R}^n$ de même norme $R > 0$, d'angle $\Omega \in\, ]0, \pi[$.

1. Construis, par Gram-Schmidt à partir de $\mathbf{u}$ (M12b §3), une base orthonormée $(\mathbf{e}_1, \mathbf{e}_2)$ du plan de $\mathbf{u}$ et $\mathbf{v}$, et montre que $\mathbf{u} = R\,\mathbf{e}_1$ et $\mathbf{v} = R(\cos\Omega\,\mathbf{e}_1 + \sin\Omega\,\mathbf{e}_2)$.
2. Avec la formule de soustraction de $\sin(\gamma - \psi)$ (fiche §8), montre que $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; t) = R\big(\cos(t\Omega)\,\mathbf{e}_1 + \sin(t\Omega)\,\mathbf{e}_2\big)$.
3. Déduis-en les propriétés 1, 2 et 3 de la fiche : les extrémités, la norme $R$ pour tout $t$, et l'angle $t\Omega$ entre $\mathbf{u}$ et $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; t)$, pour $t \in [0, 1]$.
4. Démontre la propriété 4 : la limite des deux coefficients quand $\Omega \to 0$, $t$ fixé.
5. Montre que le milieu de la corde, $\frac12(\mathbf{u} + \mathbf{v})$, est à la distance $R\cos\frac\Omega2$ du centre, et que la corde mesure $2R\sin\frac\Omega2$.
6. Pour deux vecteurs non nuls $\mathbf{u}$ et $\mathbf{v}$ de normes $a$ et $b$, d'angle $\Omega \in\, ]0, \pi[$, montre que $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; \frac12) = \frac{\mathbf{u} + \mathbf{v}}{2\cos(\Omega/2)}$, puis que le carré de sa norme vaut $ab + \frac{(a - b)^2}{2(1 + \cos\Omega)}$. Retrouve la propriété 2 pour $a = b$. Où la démonstration de 2 utilise-t-elle l'égalité des normes ?

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M25a.16 — Pont : des vecteurs rangés en lignes (n, d) comme dans les bibliothèques : tirer n points d'un coup par E Lᵀ + μ, la log-densité de chaque ligne, et la moyenne en nats par coordonnée 🔗 ★ ⏱️ 25 min
**Objectif :** passer des vecteurs colonnes de la fiche aux tableaux de lignes des bibliothèques, pour tirer et évaluer plusieurs points d'un coup.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

Les bibliothèques rangent $n$ vecteurs de $\mathbb{R}^d$ dans les **lignes** d'un tableau de forme $(n, d)$. On prend
$$\boldsymbol{\mu} = \begin{pmatrix} 7 \\ 4 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 4 & -2 \\ -2 & 10 \end{pmatrix}, \qquad \mathbf{L} = \begin{pmatrix} 2 & 0 \\ -1 & 3 \end{pmatrix}, \qquad \mathbf{E} = \begin{pmatrix} 1 & 0 \\ 0{,}5 & -1 \\ -1 & 2 \end{pmatrix},$$
où chaque ligne de $\mathbf{E}$ est un tirage de $\mathcal{N}(\mathbf{0}, \mathbf{I}_2)$, et $\mathbf{X} = \mathbf{1}\boldsymbol{\mu}^\top + \mathbf{E}\mathbf{L}^\top$ (fiche §2, 📐).

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{E}\mathbf{L}^\top$ | une forme |
| b | $\mathbf{X}$ | une matrice $3 \times 2$ |
| c | $\Delta^2$ de chaque ligne de $\mathbf{X}$, dans l'ordre des lignes | une liste de 3 nombres |
| d | la log-densité de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ en chaque ligne de $\mathbf{X}$ | une liste de 3 nombres (4 décimales) |
| e | la log-vraisemblance moyenne en nats par coordonnée, la somme des trois log-densités divisée par $nd$ | un nombre (4 décimales) |
| f | avec $\mathbf{D} = \mathbf{X} - \mathbf{1}\boldsymbol{\mu}^\top$, la forme de $\mathbf{D}\boldsymbol{\Sigma}^{-1}\mathbf{D}^\top$ | une forme |
| g | vrai ou faux : $(\mathbf{L}\mathbf{E}^\top)^\top + \mathbf{1}\boldsymbol{\mu}^\top$ donne le même tableau que $\mathbf{X}$ | `True` ou `False` |

Dans ta copie : écris la ligne $i$ de $\mathbf{X}$ en fonction de la ligne $i$ de $\mathbf{E}$ et justifie $\mathbf{L}^\top$. Calcule c) sans former $\boldsymbol{\Sigma}^{-1}$ (que valent les lignes de $\mathbf{L}^{-1}$ appliqué aux écarts ?). Quels coefficients de $\mathbf{D}\boldsymbol{\Sigma}^{-1}\mathbf{D}^\top$ sont les $\Delta^2$, et pourquoi ne forme-t-on pas cette matrice quand $n$ vaut un million ? Que donnerait `E @ L` au lieu de `E @ L.T` pour la première ligne ? Pourquoi diviser par $nd$ pour comparer des lois de dimensions différentes ?

### Ex M25a.17 — MML §6.5 et la fin de §6.7.2 : densité, marginales et conditionnelles, produit, sommes et transformations, échantillonnage et changement de variable multivarié, en anglais 📖 ★★ ⏱️ 45 min
**Objectif :** relire MML §6.5 et la fin de §6.7.2 avec les outils du chapitre : notations, formules admises par le livre, et refaire l'Exemple 6.17 avec ses propres nombres.
**Prérequis :** fiche §1, §2, §4 et §5 · **Parcours :** C

Lis MML §6.5 (*Gaussian Distribution*) en entier, puis la fin de §6.7.2 (*Change of Variables*), du Théorème 6.16 à la remarque qui suit l'Exemple 6.17, en suivant le guide de lecture de la fiche. Réponds dans ta copie, en français.
1. Écris (6.63) avec les notations de la fiche ($d$, $\det$, $\Delta^2$). Que désigne le livre par *standard normal distribution* ?
2. En §6.5.1, le livre appelle les deux blocs $\mathbf{x}$ et $\mathbf{y}$. Récris (6.66) et (6.67) avec les blocs $a$ et $b$ de la fiche. Le livre renvoie à un autre ouvrage pour la démonstration : où et comment la fiche la fait-elle ? Explique la phrase qui dit que, dans (6.66), la valeur de $\mathbf{y}$ n'est plus aléatoire, et dis ce qu'elle implique pour (6.67).
3. En §6.5.2, (6.74) à (6.76) emploient les lettres $\mathbf{a}$, $\mathbf{A}$, $\mathbf{b}$, $\mathbf{B}$, $c$, $\mathbf{c}$, $\mathbf{C}$. Fais la correspondance avec $\boldsymbol{\mu}_1$, $\boldsymbol{\Sigma}_1$, $\boldsymbol{\mu}_2$, $\boldsymbol{\Sigma}_2$, $\kappa$, $\boldsymbol{\mu}_3$, $\boldsymbol{\Sigma}_3$ de la fiche. Une même lettre y désigne deux objets différents : laquelle ? Que veut dire « *inflated* covariance matrix » ?
4. En §6.5.3, l'Exemple 6.7 écrit $a^2\boldsymbol{\Sigma}_x + b^2\boldsymbol{\Sigma}_y$ : pourquoi des carrés ? Que devient la formule si $a$ et $b$ sont remplacés par deux matrices $\mathbf{A}$ et $\mathbf{B}$ ? Relève la phrase qui affirme qu'une transformation affine d'un vecteur gaussien est gaussienne, et dis sur quelle justification de la fiche (§2) elle repose. Que démontrent (6.86) et (6.87), et que n'établissent-elles pas à elles seules ?
5. En §6.5.4, le livre écrit $\mathbf{y} = \mathbf{A}\mathbf{x} + \boldsymbol{\mu}$ avec $\mathbf{A}\mathbf{A}^\top = \boldsymbol{\Sigma}$ : quelle lettre la fiche emploie-t-elle pour ce $\mathbf{A}$, et quelle convention de forme ? Pourquoi la note en marge exige-t-elle une matrice symétrique définie positive ? Des trois étapes décrites, lesquelles `rng.standard_normal` fait-il pour toi ?
6. Que désignent les barres verticales autour du déterminant dans (6.144), et pourquoi sont-elles nécessaires (fiche §2) ? (6.150) donne le déterminant de la jacobienne sans ces barres : où réapparaissent-elles dans la suite de l'Exemple 6.17, et que se passerait-il sans elles pour une matrice de déterminant négatif ? Dans (6.148), le membre de droite est-il déjà la densité de $\mathbf{y}$ ?
7. Refais l'Exemple 6.17 avec tes propres nombres : choisis une matrice $\mathbf{A}$ inversible de **déterminant négatif** et un point $\mathbf{y}$, calcule l'antécédent $\mathbf{A}^{-1}\mathbf{y}$, la densité de $\mathbf{y} = \mathbf{A}\mathbf{x}$ en ce point par (6.151b), puis la densité de $\mathcal{N}(\mathbf{0}, \mathbf{A}\mathbf{A}^\top)$ au même point, et compare.
8. Relève six expressions anglaises des deux passages et leur traduction dans la fiche.

### Ex M25a.18 — MML §9.3 : régression linéaire bayésienne, prédictions a priori et a posteriori, vraisemblance marginale, en anglais 📖 ★★ ⏱️ 45 min
**Objectif :** relire MML §9.3 avec la fiche : refaire la complétion du carré du Théorème 9.1, comparer prédictive et vraisemblance marginale, et repérer deux pièges de notation.
**Prérequis :** fiche §5 ; M09b · **Parcours :** C

Lis MML §9.3 en entier (§9.3.1 à §9.3.5), en suivant le guide de lecture de la fiche ; les Exemples 9.7 et 9.8 et leurs figures se regardent sans être refaits. Réponds dans ta copie, en français.
1. Dans le modèle (9.35), identifie $\boldsymbol{\theta}$, $\boldsymbol{\phi}$, $\mathbf{m}_0$, $\mathbf{S}_0$ et $\sigma^2$. Comment le livre note-t-il le bruit, et comment la fiche ?
2. La prédictive a priori (9.38) : d'où vient chacun des deux termes de la variance ? Quelle hypothèse justifie (9.39) ? En quoi (9.40) diffère-t-elle de (9.38), et pourquoi ?
3. Refais en détail le passage de (9.45b) à (9.50b) : développe, sépare les termes quadratiques et linéaires en $\boldsymbol{\theta}$, et identifie $\mathbf{S}_N$ et $\mathbf{m}_N$. Relie (9.49a) à la règle « les précisions s'additionnent » de la fiche.
4. La remarque (9.51) à (9.54) : dans (9.52), quel rôle joue la matrice notée $\boldsymbol{\Sigma}$ — une covariance ou une précision ? Pourquoi est-ce un piège de notation ? Vérifie la valeur de $\text{const}_2$ en développant (9.52).
5. Compare (9.57c) à la prédictive de la fiche. Pourquoi la moyenne de la prédictive coïncide-t-elle avec la prédiction du MAP, comme le dit la note en marge ?
6. La remarque qui rapproche vraisemblance marginale et prédictive a posteriori cite deux différences : lesquelles ?
7. Au point 1 de §9.3.5, le livre dit que le produit de deux variables aléatoires gaussiennes est une gaussienne non normalisée : qu'aurait-il fallu écrire, et pourquoi la phrase, prise à la lettre, est-elle fausse (fiche §2) ? Quelle lettre §9.3.5 emploie-t-il pour la matrice $\boldsymbol{\Phi}$ ?
8. (9.33) et (9.34) relient ridge au MAP avec deux valeurs de $\lambda$ : $\frac{1}{2b^2}$, puis $\frac{\sigma^2}{b^2}$. Explique l'écart (la loss contient-elle un facteur $\frac12$, est-elle divisée par $\sigma^2$ ?), et relie la seconde à la pénalité $\frac{\sigma^2}{\tau^2}$ de la fiche.
9. Applique (9.64b) avec tes propres nombres : un modèle à un seul poids, $y = \theta x + w$, deux points, un a priori $\mathcal{N}(m_0, s_0^2)$ et un bruit $\sigma^2$ de ton choix. Donne la moyenne et la covariance de l'évidence, puis son logarithme.

### Ex M25a.19 — Expliquer avec deux thermomètres voisins pourquoi lire l'un resserre l'estimation de l'autre, et pourquoi la valeur lue ne change pas cette incertitude 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule ce que fait le conditionnement gaussien : la moyenne bouge avec la mesure, l'incertitude ne dépend que de la corrélation.
**Prérequis :** fiche §4 · **Parcours :** C, E

Une amie surveille deux thermomètres voisins dans un hangar ; l'un tombe en panne. Elle constate que lire celui qui marche l'aide à deviner l'autre. Un collègue lui affirme : « Quelle que soit la valeur que tu lis, ton incertitude sur le thermomètre en panne sera la même. » Elle n'y croit pas : « Si je lis une valeur bizarre, je devrais être moins sûre, non ? »

Réponds-lui en 6 à 10 phrases, sans formule, avec une image de la vie courante (deux amis qui arrivent souvent ensemble, deux villes voisines sous la même météo, ou une autre de ton choix) : pourquoi la lecture déplace l'estimation de l'autre thermomètre, et dans quel sens ; ce qui décide de l'ampleur de ce déplacement ; pourquoi l'incertitude qui reste est plus petite qu'avant ; pourquoi elle ne dépend pas de la valeur lue, dans ce modèle ; et la réserve à faire si une valeur lue est vraiment invraisemblable. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M25a.E1 — « Comment tirer un vecteur gaussien de covariance donnée à partir de tirages indépendants, et pourquoi Cholesky ? » 💼 ★ ⏱️ 10 min
*Fiche §2 · parcours C*

« Comment tirer un vecteur gaussien de covariance donnée à partir de tirages indépendants, et pourquoi Cholesky ? »

Ta réponse doit dire la recette, pourquoi le résultat a la bonne moyenne, la bonne covariance et une loi gaussienne, qu'une autre racine de $\boldsymbol{\Sigma}$ conviendrait aussi, ce que Cholesky apporte de plus (son coût comparé à une décomposition en valeurs propres, sa stabilité, le test de définie positivité qu'il donne au passage, $\ln\det\boldsymbol{\Sigma}$ gratuit), ce qu'on fait quand $\boldsymbol{\Sigma}$ n'est que semi-définie, la convention des tableaux en lignes, et le chemin inverse.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m25a_gaussienne/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M25a.20 | La log-densité d'une loi normale multivariée, par Cholesky · `mvn_logpdf` | 🔨 | ★★ | 40 | C, E |
| M25a.21 | Tirer des vecteurs de loi N(μ, Σ) par Cholesky · `sample_mvn` | 🔨 | ★ | 20 | C, E |
| M25a.22 | Le complément de Schur d'un bloc, et la loi conditionnelle d'un vecteur gaussien · `schur_complement`, `condition_gaussian` | 🔨 | ★★ | 40 | C, E |
| M25a.23 | Le posterior d'une régression linéaire bayésienne · `linreg_posterior` | 🔨 | ★★ | 35 | C |
| M25a.24 | `scipy.stats.multivariate_normal`, `np.cov` et `scipy.integrate` : tes log-densités, le maximum de vraisemblance, et la KL de M25a.8 par une intégrale double | 📦 | ★ | 30 | C, E |
| M25a.25 | Prédire la part des tirages dans l'ellipsoïde de Mahalanobis de même niveau quand la dimension passe de 2 à 10, puis mesurer | 🔮 | ★ | 15 | C, E |
| M25a.26 | Conditionner par simulation : garder les tirages dont une mesure tombe près d'une valeur, et comparer à la loi conditionnelle exacte | 🔬 | ★★ | 25 | C |
| M25a.27 | Les ellipses de niveau d'une gaussienne en dimension 2, une tranche (la loi conditionnelle) et une projection (la loi marginale), selon la corrélation | 🎨 | ★ | 25 | C, E |
| M25a.28 | Chasse à l'erreur : un tirage par E L au lieu de E Lᵀ, ln det Σ sans le facteur 2, et une covariance conditionnelle qui dépend de la valeur observée | 🐛 | ★ | 25 | C, E |
| M25a.29 | Un test de propriété : la moyenne et la covariance empiriques de tes tirages, à une tolérance fixée par l'erreur type | 🛠️ | ★★ | 30 | C |
| M25a.30 | Défi : reconstruire les températures manquantes le long d'une route par la loi conditionnelle d'une gaussienne, sous une erreur quadratique moyenne fixée | 🏆 | ★★★ | 35 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les quatre 🔨 complètent ta copie `mon_travail/mymath/gaussian.py` (**mymath :** `gaussian.py`), dont la docstring du module dit ce qui est permis : NumPy, mais, de `np.linalg`, seulement `cholesky` et `solve` (et `np.linalg.LinAlgError` pour attraper un échec), ni `multivariate_normal` (ni celui de NumPy, ni la méthode d'un `Generator`), et aucune fonction de SciPy. Chaque 🔨 lance ensuite le groupe de tests de sa fonction dans `tests/test_m25a_gaussian.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.gaussian.<nom>(…)`. Les indices d'un bloc se donnent par une **liste** (`[0, 2]`, jamais un entier nu), numérotés à partir de 0 : le capteur 1 de M25a.4 est la coordonnée 0. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy.

**M25a.20 · 🔨 `mvn_logpdf(x, mean, cov)`.** Écris la log-densité de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ en un point de forme $(d,)$ ou en $n$ points rangés en lignes $(n, d)$, par le facteur de Cholesky : $\ln\det\boldsymbol{\Sigma} = 2\sum_i\ln L_{ii}$ et $\Delta^2 = \lVert\mathbf{y}\rVert^2$ où $\mathbf{y}$ résout $\mathbf{L}\mathbf{y} = \mathbf{x} - \boldsymbol{\mu}$, jamais par `det` ni par une inverse (la docstring fixe les formes et les refus) ; lance le groupe de tests `mvn_logpdf`. Ensuite, avec ta fonction : a) $\ln p(\mathbf{x}_P)$ et $\ln p(\mathbf{x}_Q)$ pour la serre de M25a.1, à comparer à ta réponse f) ; b) les trois log-densités des lignes de $\mathbf{X}$ du 🔗 M25a.16, d'un seul appel avec un `x` de forme $(3, 2)$, à comparer à ta réponse d) ; c) en dimension 600, la loi de moyenne nulle et de covariance $\Sigma_{ij} = 0{,}3^{\lvert i - j\rvert}$, au point $\mathbf{x} = \mathbf{L}\boldsymbol{\varepsilon}$ où $\mathbf{L}$ = `np.linalg.cholesky(cov)` et $\boldsymbol{\varepsilon}$ = `np.random.default_rng(5920).standard_normal(600)` : $\ln p(\mathbf{x})$ (2 décimales) ; d) vrai ou faux : `np.exp` de cette valeur vaut exactement `0.0` ; e) $\ln\det\boldsymbol{\Sigma}$ par $2\sum_i\ln L_{ii}$, à comparer à la valeur exacte $599\ln(1 - 0{,}3^2)$ (2 décimales). Ce qu'il faut observer : en grande dimension, la densité d'un point tout à fait ordinaire sort des flottants, son logarithme non.

**M25a.21 · 🔨 `sample_mvn(mean, cov, n, seed=0)`.** Écris le tirage de $n$ vecteurs de loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, rangés en lignes : un seul appel `rng.standard_normal((n, d))` avec `rng = np.random.default_rng(seed)`, puis `mean + E @ L.T` ; lance le groupe de tests `sample_mvn`. Ensuite : a) 20 000 tirages des épaisseurs de route de M25a.2 (`seed=5921`) : leur moyenne empirique (3 décimales) et leur covariance empirique `np.cov(X, rowvar=False, bias=True)` (2 décimales), à comparer à $\boldsymbol{\mu}$ et $\boldsymbol{\Sigma}$ ; b) le coût $c = 2x_1 + x_2 + 3x_3$ de chaque tirage : sa moyenne et sa variance empiriques (2 décimales), à comparer à ta réponse c) de M25a.2 ; c) les tirages blanchis, $\mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ pour chaque ligne (par `np.linalg.solve`) : leur covariance empirique (3 décimales) ; d) vrai ou faux : la première ligne est $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$, où $\boldsymbol{\varepsilon}$ est la première ligne de `np.random.default_rng(5921).standard_normal((20000, 3))`. Ce qu'il faut observer : les moments empiriques s'approchent de $\boldsymbol{\mu}$ et $\boldsymbol{\Sigma}$ à l'erreur type près (de l'ordre de $\frac{1}{\sqrt n}$), et le blanchiment rend un nuage de covariance proche de $\mathbf{I}$.

**M25a.22 · 🔨 `schur_complement(M, idx)` et `condition_gaussian(mean, cov, idx, values)`.** Écris le complément de Schur du bloc `M[idx, idx]`, $\mathbf{A} - \mathbf{B}\mathbf{D}^{-1}\mathbf{C}$ avec la docstring (fiche §4, 📐), par `np.linalg.solve`, puis la loi conditionnelle des coordonnées hors de `idx` sachant `x[idx] = values` ; lance les groupes de tests `schur_complement` et `condition_gaussian`. Ensuite, pour le capteur en panne de M25a.4 (coordonnées 0, 1, 2) : a) la loi de la coordonnée 1 sachant les coordonnées `[0, 2]` égales à 19,5 et 14 (la moyenne et la variance conditionnelles, sans arrondir), à comparer à tes réponses c) et d) ; b) vrai ou faux : `schur_complement(cov, [0, 2])` est la covariance conditionnelle de a) ; c) vrai ou faux : $\det\boldsymbol{\Sigma}$ (par `np.linalg.det`, hors de `mymath`) est égal à $\det\boldsymbol{\Sigma}_{bb}$ fois le déterminant du complément de Schur, à $10^{-12}$ près ; d) vrai ou faux : l'inverse du coefficient $(1, 1)$ de `np.linalg.inv(cov)` est égal à la variance conditionnelle ; e) les voisins lisent maintenant 21 °C et 12 °C : la nouvelle moyenne conditionnelle, et vrai ou faux, la variance conditionnelle est inchangée ; f) vrai ou faux : `idx = [2, 0]` avec les valeurs dans l'ordre 14 et 19,5 donne la même loi qu'en a). Ce qu'il faut observer : la moyenne conditionnelle suit les valeurs lues, la covariance conditionnelle n'en dépend pas, et c'est l'inverse du bloc de la précision.

**M25a.23 · 🔨 `linreg_posterior(Phi, y, prior_mean, prior_cov, noise_var)`.** Écris la loi a posteriori $\mathcal{N}(\mathbf{m}_N, \mathbf{S}_N)$ des poids d'une régression linéaire bayésienne, par la forme « précisions » de la fiche §5 et `np.linalg.solve` (sans données, elle rend l'a priori) ; lance le groupe de tests `linreg_posterior`. Ensuite, pour le thermomètre de M25a.6 : a) $\mathbf{m}_N$ et $\mathbf{S}_N$, à comparer à tes réponses d) et e) ; b) vrai ou faux : en traitant les deux bains l'un après l'autre (la loi a posteriori après le premier sert d'a priori pour le second), on retrouve a) à $10^{-12}$ près ; c) avec l'a priori $\mathcal{N}(\mathbf{0}, 0{,}5\,\mathbf{I})$ : $\mathbf{m}_N$ (4 décimales), et vrai ou faux, il est égal à la solution ridge `np.linalg.solve(Phi.T @ Phi + lam * np.eye(2), Phi.T @ e)` de pénalité $\lambda = \frac{\sigma^2}{\tau^2}$ ; d) avec l'a priori de M25a.6, la température $T$ (en °C) où la variance de la prédictive est la plus petite, par la formule $-100\,\frac{(\mathbf{S}_N)_{12}}{(\mathbf{S}_N)_{22}}$ (1 décimale), puis trace, sur les axes fournis, la moyenne de la prédictive de l'erreur et sa bande à deux écarts-types pour $T$ de −50 à 250 °C, avec les deux points d'étalonnage. Ce qu'il faut observer : les données s'ajoutent une à une sans rien changer au résultat ; l'incertitude est la plus petite entre les bains et grandit vite en extrapolation.

**M25a.24 · 📦 `scipy.stats.multivariate_normal`, `np.cov` et `scipy.integrate`.** a) Tire 1 000 vecteurs des épaisseurs de route de M25a.2 avec ta `sample_mvn` (`seed=5924`) : vrai ou faux, ta `mvn_logpdf` et `scipy.stats.multivariate_normal(mean, cov).logpdf` diffèrent de moins de $10^{-10}$ sur les 1 000 lignes ; b) 50 tirages de la serre de M25a.1 (`sample_mvn(mean, cov, 50, seed=5924)`) : l'estimation du maximum de vraisemblance $\hat{\boldsymbol{\Sigma}} = \frac1n(\mathbf{X} - \bar{\mathbf{x}})^\top(\mathbf{X} - \bar{\mathbf{x}})$, calculée à la main en NumPy (3 décimales), et vrai ou faux, elle est égale à `np.cov(X, rowvar=False, bias=True)` ; c) le rapport entre `np.cov(X, rowvar=False)` (sans `bias`) et $\hat{\boldsymbol{\Sigma}}$ (4 décimales) ; d) la KL $\mathrm{KL}(p_0 \,\|\, p_1)$ de M25a.8 par `scipy.integrate.dblquad`, en intégrant $p_0\ln\frac{p_0}{p_1}$ sur le carré $[\mu_{0,1} - 25,\ \mu_{0,1} + 25] \times [\mu_{0,2} - 25,\ \mu_{0,2} + 25]$ (4 décimales), à comparer à ta réponse d) ; e) la même KL estimée par une moyenne sur 200 000 tirages de $p_0$ (`sample_mvn(mu0, Sigma0, 200000, seed=5924)`) de $\ln p_0 - \ln p_1$, puis l'erreur type de cette moyenne, l'écart-type des 200 000 termes divisé par $\sqrt{200\,000}$ (4 décimales chacune). Ce qu'il faut observer : la formule fermée, l'intégrale double et la moyenne sur des tirages donnent la même KL, cette dernière à son erreur type près ; et, sans `bias=True`, `np.cov(X, rowvar=False)` divise par $n - 1$.

**M25a.25 · 🔮 Prédire la part des tirages dans l'ellipsoïde de Mahalanobis de même niveau quand la dimension passe de 2 à 10, puis mesurer.** On garde le niveau de l'ellipse à 90 % du plan, $c^2 = 2\ln 10$, et l'on regarde, en dimension $d$, la part des tirages de $\mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma}_d)$ tels que $\Delta^2 \le c^2$, avec $(\boldsymbol{\Sigma}_d)_{ij} = 0{,}6^{\lvert i - j\rvert}$. **Avant d'exécuter**, prédis : a) en dimension 10, cette part est (A) encore de l'ordre de 90 % ; (B) nettement plus petite ; (C) nettement plus grande ; b) la première dimension où elle passe sous 50 % : (A) 3 ou 4 ; (B) entre 5 et 7 ; (C) 8 ou plus ; c) vrai ou faux : pour une dimension donnée, cette part dépend de la matrice $\boldsymbol{\Sigma}_d$ choisie. Puis mesure, pour $d = 2, \ldots, 10$, la part sur 100 000 tirages (`sample_mvn(np.zeros(d), Sigma_d, 100000, seed=5925)`, $\Delta^2$ par `np.linalg.solve`), compare-la à `scipy.stats.chi2(d).cdf(2 * np.log(10))`, et relève : d) la part mesurée en dimension 10 (3 décimales) ; e) la première dimension où la part mesurée passe sous 50 %. Ce qu'il faut observer : $\Delta^2$ suit la loi du khi-deux à $d$ degrés quelle que soit $\boldsymbol{\Sigma}_d$ ; à niveau fixé, la masse de l'ellipsoïde dépend seulement de la dimension.

**M25a.26 · 🔬 Conditionner par simulation.** Pour la serre de M25a.1, on cherche la loi de l'humidité $H$ sachant que la température vaut $T = 23$ °C. a) Calcule-la exactement avec ta `condition_gaussian` (la moyenne et la variance). Puis tire 200 000 relevés (`sample_mvn(mean, cov, 200000, seed=5926)`) et, pour chaque demi-largeur $h = 2$, 1, 0,5, 0,2 et 0,05 °C, garde ceux où $\lvert T - 23\rvert < h$ : relève leur nombre, et la moyenne et la variance empiriques de leur humidité. Trace la moyenne et la variance empiriques contre $h$ (abscisse logarithmique), avec les valeurs exactes. Relève : b) le nombre de relevés gardés pour $h = 0{,}05$ ; c) la moyenne empirique de l'humidité pour $h = 2$ (2 décimales) ; d) vrai ou faux : pour $h = 2$, la variance empirique dépasse la variance exacte de plus de 1. Ce qu'il faut conclure : une fenêtre large garde beaucoup de relevés mais biaise la moyenne et gonfle la variance (elle mélange des températures différentes) ; une fenêtre étroite est presque sans biais mais garde peu de relevés (leur nombre est à peu près proportionnel à $h$) ; la loi conditionnelle exacte évite ce compromis.

**M25a.27 · 🎨 Les ellipses de niveau, une tranche et une projection, selon la corrélation.** Écris `draw_gaussian_27(ax_joint, ax_cut, mean, cov, x1_value)`, qui dessine sur les **axes reçus** (sans ouvrir de figure) : dans `ax_joint`, les ellipses à 75 % et à 90 % de la loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ du plan, obtenues en appliquant $\boldsymbol{\varepsilon} \mapsto \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ au cercle de rayon $c$ (fiche §3, 💻), la droite verticale $x_1 = $ `x1_value` et la droite des moyennes conditionnelles de $x_2$ sachant $x_1$ ; dans `ax_cut`, la densité de la loi marginale de $x_2$ et celle de la loi conditionnelle de $x_2$ sachant $x_1 = $ `x1_value` (par ta `condition_gaussian`), avec une légende. Appelle-la pour $\boldsymbol{\mu} = (0, 1)$, des écarts-types 1 et 2, des corrélations $\rho = 0$, $0{,}5$ et $0{,}9$, et $x_1 = 1{,}5$ : trois colonnes de deux panneaux, avec des axes à la même échelle dans les panneaux du haut. Ce qu'il faut observer : la tranche est une loi normale décalée de $\rho\frac{\sigma_2}{\sigma_1}(x_1 - \mu_1)$ et plus étroite (variance multipliée par $1 - \rho^2$), la projection garde la variance $\sigma_2^2$ ; pour $\rho = 0$, les deux courbes se confondent.

**M25a.28 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `draw_correlated(mean, cov, n, seed)` doit rendre $n$ tirages de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ rangés en lignes ; elle calcule `L = np.linalg.cholesky(cov)` et `E = np.random.default_rng(seed).standard_normal((n, d))`, puis rend `mean + E @ L`. Il l'a vérifiée sur la loi de moyenne nulle et de covariance $\operatorname{diag}(4, 9)$ : la covariance empirique de 50 000 tirages est bien proche de $\boldsymbol{\Sigma}$. Il l'applique au vent de M25a.3.
- (2) `log_density(x, mean, cov)` doit rendre la log-densité de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ en un point ; elle calcule $\mathbf{L}$, résout $\mathbf{L}\mathbf{y} = \mathbf{x} - \boldsymbol{\mu}$, puis rend $-\frac12\big[d\ln(2\pi) + \sum_i\ln L_{ii} + \lVert\mathbf{y}\rVert^2\big]$. Il l'a vérifiée en trois points d'une loi de dimension 2 : `log_density(x, mean, cov) - log_density(mean, mean, cov)` vaut bien $-\frac12\Delta^2(\mathbf{x})$. Il l'applique à la serre de M25a.1.
- (3) `conditional_law(mean, cov, idx, values)` doit rendre la moyenne et la covariance des coordonnées hors de `idx` sachant `x[idx] = values` ; pour « tenir compte de l'écart observé », elle remplace $\boldsymbol{\Sigma}_{bb}$ par la dispersion de $\mathbf{x}_b$ autour de la valeur lue, $\boldsymbol{\Sigma}_{bb} + (\mathbf{v} - \boldsymbol{\mu}_b)(\mathbf{v} - \boldsymbol{\mu}_b)^\top$ (avec $\mathbf{v}$ = `values`), dans la moyenne comme dans la covariance. Il l'a vérifiée sur le capteur en panne de M25a.4, en supposant que les deux voisins lisaient leur moyenne. Il l'applique aux vraies lectures, 19,5 °C et 14 °C.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `draw_correlated_fixed`, `log_density_fixed` et `conditional_law_fixed`, avec les mêmes arguments), puis réponds : a) la covariance théorique des tirages que rend la version fausse de `draw_correlated` pour le vent (4 décimales) ; b) vrai ou faux : la covariance empirique de 50 000 tirages de la version corrigée (`seed=5928`) est à moins de 0,3 de $\boldsymbol{\Sigma}$, coefficient par coefficient ; c) la valeur que rend la version fausse de `log_density` en $\mathbf{x}_P$ (4 décimales) ; d) celle de la version corrigée (4 décimales) ; e) la moyenne et la variance conditionnelles que rend la version fausse de `conditional_law` (4 décimales) ; f) celles de la version corrigée (4 décimales). Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas.

**M25a.29 · 🛠️ Un test de propriété.** Écris une fonction `moment_test_29(sampler, mean, cov, n, seed, k)` qui tire `X = sampler(mean, cov, n, seed)` et vérifie que chaque moyenne empirique est à moins de $k$ erreurs types de $\mu_j$, l'erreur type valant $\sqrt{\Sigma_{jj}/n}$, et que chaque coefficient de la covariance empirique (`bias=True`) est à moins de $k$ erreurs types de $\Sigma_{jk}$, l'erreur type valant $\sqrt{(\Sigma_{jj}\Sigma_{kk} + \Sigma_{jk}^2)/n}$ ; un échec lève `AssertionError` avec un message qui dit d'abord ce qui était attendu, puis le coefficient fautif. On prend la loi du vent de M25a.3 et $n = 2\,000$. a) Choisis $k$ pour que la probabilité qu'une fonction juste échoue soit au plus 1 % : en dimension 2, le test fait 5 comparaisons (2 moyennes et 3 coefficients de covariance) ; partage les 1 % entre elles (une borne de la réunion) et lis $k$ dans `scipy.stats.norm.ppf` (4 décimales). b) Lance ton test sur ta `sample_mvn` pour 300 graines tirées par `np.random.default_rng(5929).integers(0, 2**31, size=300)` : le nombre d'échecs, à comparer à ce que garantit a) (sur 300 répétitions, une proportion fluctue d'environ ± 0,6 %). c) Sur ces 300 répétitions, mesure l'écart-type (`np.std`) du coefficient $(0, 1)$ de la covariance empirique (`bias=True`, comme dans le test), et compare-le à la formule de l'erreur type (4 décimales chacun). d) Le notebook fournit quatre versions fausses : `sampler_EL` (qui rend `mean + E @ L`), `sampler_sigma` (`mean + E @ cov`), `sampler_diag` (qui ignore les covariances : chaque coordonnée a la bonne variance, sans corrélation) et `sampler_inflated` (qui tire $\mathcal{N}(\boldsymbol{\mu}, 1{,}02\,\boldsymbol{\Sigma})$) ; lance ton test sur chacune avec la graine 5929 : lesquelles attrape-t-il ? e) Combien de tirages faudrait-il pour qu'un écart de 2 % sur une variance dépasse $k$ erreurs types (l'erreur type d'une variance empirique vaut $\Sigma_{jj}\sqrt{2/n}$) ? Vérifie que ton test attrape `sampler_inflated` avec $n = 300\,000$. Ce qu'il faut retenir : la tolérance d'un test statistique se choisit par l'erreur type et un risque d'échec annoncé, pas au hasard ; un tel test attrape les erreurs grossières à petit $n$, et une erreur fine seulement si $n$ est assez grand pour elle.

**M25a.30 · 🏆 Défi : reconstruire les températures manquantes le long d'une route.** Une route est équipée d'un capteur de température par kilomètre, aux positions $s = 0, 1, \ldots, 30$ km. Les vraies températures (en °C) suivent une loi normale de moyenne $m(s) = 14 - 0{,}15\,s$ (la route monte) et de covariance $K_{ij} = 4\exp\big(-\frac{\lvert s_i - s_j\rvert}{6}\big)$, exponentielle de la distance. Douze capteurs sont en panne, aux positions 0, 1, 2, 13 à 17, et 27 à 30 ; les 19 autres mesurent la vraie température avec une erreur gaussienne indépendante d'écart-type 0,4 °C. La cellule de données tire les vraies températures et les mesures avec `rng = np.random.default_rng(5930)` (les vraies températures $m + \mathbf{L}\,$`rng.standard_normal(31)`, $\mathbf{L}$ étant le facteur de Cholesky de $\mathbf{K}$, puis les 19 mesures, vraies températures plus $0{,}4\,$`rng.standard_normal(19)`) ; elle ne te donne que les mesures, et la cellule de vérification garde les vraies températures des positions en panne. Écris `fill_missing_30(s, y_obs, obs, miss)`, qui rend les moyennes et les écarts-types de la loi conditionnelle des vraies températures aux positions `miss` sachant les mesures aux positions `obs`. Le bruit ne touche que les positions mesurées : à toi de construire la covariance du vecteur formé des vraies températures aux positions en panne et des mesures aux autres positions. **Critère de réussite :** la cellule de vérification calcule l'erreur quadratique moyenne de tes douze moyennes contre les vraies températures, et réussit si elle est au plus 1,0 °C. Puis relève : a) ton erreur quadratique moyenne (affichée par la vérification) ; b) celle de l'interpolation linéaire des mesures, `np.interp(s[miss], s[obs], y_obs)` (affichée aussi) ; c) combien des douze vraies températures tombent à moins de deux de tes écarts-types de tes moyennes (affiché aussi). Trace les mesures, tes moyennes avec leur bande à deux écarts-types, la moyenne $m(s)$ et l'interpolation linéaire. Pour aller plus loin : la longueur 6 km de la covariance est supposée connue ; trace, en fonction de cette longueur, le logarithme de l'évidence des 19 mesures (ta `mvn_logpdf`), et regarde où il est maximal.
