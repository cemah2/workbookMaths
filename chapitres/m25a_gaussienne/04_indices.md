# M25a · Gaussienne multivariée, conditionnement et divergence KL — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M25a.Q1 — Lire une densité gaussienne multivariée : det Σ, distance de Mahalanobis et point le plus probable

<details><summary>Indice 1</summary>

Relis la densité du §1 et « Ce que disent det Σ et la distance de Mahalanobis ».

</details>
<details><summary>Indice 2</summary>

Le facteur est $\frac{1}{(2\pi)^{d/2}\sqrt{\det\boldsymbol{\Sigma}}}$ ; l'exponentielle vaut 1 en $\boldsymbol{\mu}$ et ne dépend que de $\Delta$. $\det(c\boldsymbol{\Sigma}) = c^d\det\boldsymbol{\Sigma}$ en dimension $d$.

</details>
<details><summary>Indice 3</summary>

1. Identifie l'exposant de $2\pi$, puis $\sqrt{\det\boldsymbol{\Sigma}} = 6$. 5. $\sqrt{9^3}$. 7. Pour une $\boldsymbol{\Sigma}$ diagonale, $\Delta^2 = \sum_i\frac{(x_i - \mu_i)^2}{\sigma_i^2}$, et $\ln p = \ln p(\boldsymbol{\mu}) - \frac12\Delta^2$.

</details>

### M25a.Q2 — Ce qui reste gaussien : images affines, sommes, produits et normes ; deux marginales gaussiennes ne suffisent pas

<details><summary>Indice 1</summary>

Relis la définition d'un vecteur gaussien (§1), puis le §2 : « Les transformations affines restent gaussiennes », « Sommes » et « Ce qui ne reste pas gaussien ».

</details>
<details><summary>Indice 2</summary>

Un vecteur est gaussien si **toute** combinaison linéaire de ses coordonnées est normale (une constante compte). Une différence $\mathbf{x} - \mathbf{y}$ est une image linéaire du vecteur $(\mathbf{x}, \mathbf{y})$.

</details>
<details><summary>Indice 3</summary>

2. Pense au signe aléatoire de la fiche. 3. Calcule la covariance de $\begin{pmatrix} \mathbf{I} & -\mathbf{I} \end{pmatrix}\begin{pmatrix} \mathbf{x} \\ \mathbf{y} \end{pmatrix}$. 5. Écris $\alpha_1x_1 + \alpha_2x_2$ en fonction de $z$, puis calcule le déterminant de la covariance.

</details>

### M25a.Q3 — Ellipses de niveau et masse : quel axe, quel demi-axe, quelle proportion, en dimension 2 et au-delà

<details><summary>Indice 1</summary>

Relis « Les ellipses de niveau » et « La masse d'une ellipse en dimension 2 » (§3).

</details>
<details><summary>Indice 2</summary>

Demi-axes $c\sqrt{\lambda_i}$ le long des vecteurs propres de $\boldsymbol{\Sigma}$ ; aire $\pi c^2\sqrt{\det\boldsymbol{\Sigma}}$ ; masse $1 - e^{-c^2/2}$ en dimension 2 seulement ; mode de la norme $\sqrt{d - 1}$.

</details>
<details><summary>Indice 3</summary>

2. $c = 2$, $\lambda = 25$ et 4. 4. $e^{-\frac12 \cdot 2\ln 4} = e^{-\ln 4}$. 5. En dimension 5, la masse est une valeur de la loi du khi-deux à 5 degrés. 6. Que devient l'ellipse de niveau $c$ quand $\boldsymbol{\Sigma}$ est multipliée par 4 ? Et sa masse ?

</details>

### M25a.Q4 — Complément de Schur, loi marginale ou loi conditionnelle : quel bloc, quelle moyenne, quelle variance ?

<details><summary>Indice 1</summary>

Relis « Les lois marginales », « Décorrélé équivaut à indépendant », « La loi conditionnelle » et « La matrice de précision » (§4).

</details>
<details><summary>Indice 2</summary>

Marginale : garder les sous-blocs. Conditionnelle : $\boldsymbol{\Sigma}_{aa} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}$, qui ne dépend pas de la valeur lue. $\det\mathbf{M} = \det\mathbf{M}_{bb}\cdot\det(\mathbf{M}/\mathbf{M}_{bb})$.

</details>
<details><summary>Indice 3</summary>

3. $a = \{1\}$, $b = \{2\}$ : $4 - \frac{2 \times 2}{3}$. 4. Prends $a = \{1, 3\}$, $b = \{2\}$ et calcule le coefficient hors diagonale du complément de Schur. 7. Calcule $(\boldsymbol{\Sigma}^{-1})_{11}$ par le cofacteur, ou comme l'inverse de la variance de $x_1$ sachant $x_2$ et $x_3$.

</details>

### M25a.Q5 — Fusionner des mesures et mettre à jour un a priori gaussien : précisions, moyennes pondérées et prédictive

<details><summary>Indice 1</summary>

Relis « Le produit de deux densités », « Fusionner des mesures », « Le modèle linéaire gaussien » et « Prédire : la prédictive » (§5).

</details>
<details><summary>Indice 2</summary>

Les précisions $\frac1{\sigma^2}$ s'additionnent ; la moyenne est pondérée par les précisions. Pour $y = Ax + w$ : $\mathbb{V}(y) = A^2\mathbb{V}(x) + \mathbb{V}(w)$ et $\operatorname{Cov}(x, y) = A\,\mathbb{V}(x)$.

</details>
<details><summary>Indice 3</summary>

1. Précision $\frac14 + \frac1{12}$, puis moyenne $\sigma_3^2\big(\frac{10}{4} + \frac{14}{12}\big)$. 5. Écris les deux parts de la variance de la prédictive. 6. $\lambda = \frac{\sigma^2}{\tau^2}$.

</details>

### M25a.Q6 — Le maximum de vraisemblance de μ et Σ : diviser par n, et une covariance singulière quand n ≤ d

<details><summary>Indice 1</summary>

Relis « Les estimations », « Diviser par n » et « Quand n ≤ d » (§6), et le 💻 sur `np.cov`.

</details>
<details><summary>Indice 2</summary>

$\mathbf{S}$ est une somme de $n$ matrices de rang 1 dont les vecteurs ont une somme nulle : son rang est au plus $n - 1$ ; c'est aussi une matrice $d \times d$. $\mathbb{E}[\hat{\boldsymbol{\Sigma}}] = \frac{n - 1}{n}\boldsymbol{\Sigma}$.

</details>
<details><summary>Indice 3</summary>

3. Les trois points sont-ils alignés ? 4. Sans argument, `np.cov` prend chaque ligne pour une variable et chaque colonne pour une observation. 7. $\hat{\boldsymbol{\Sigma}}^{-1}\mathbf{S} = n\,\hat{\boldsymbol{\Sigma}}^{-1}\hat{\boldsymbol{\Sigma}}$.

</details>

### M25a.Q7 — La divergence KL continue en situations : deux supports qui ne se couvrent pas, deux lois exponentielles, une loi produit, et les deux sens

<details><summary>Indice 1</summary>

Relis la définition de la KL continue, « Supports, asymétrie : deux exemples » et « Additivité sur des lois produits » (§7).

</details>
<details><summary>Indice 2</summary>

La KL est infinie dès que la **première** loi met de la masse là où la seconde est nulle. Pour deux lois uniformes emboîtées, le logarithme du rapport des densités est constant sur le support de la première.

</details>
<details><summary>Indice 3</summary>

1. Sur $[0, 30]$, $\ln\frac{p}{q} = \ln\frac{1/30}{1/50}$ ; dans l'autre sens, regarde $[-10, 0[$. 3. Une loi exponentielle met une masse positive au-delà de toute durée : laquelle des deux lois couvre l'autre ? 6. Que vaut $\ln\frac pq$ là où $q > p$ ?

</details>

### M25a.Q8 — Ligne droite ou arc de grand cercle : extrémités, norme et angle parcouru

<details><summary>Indice 1</summary>

Relis « Pourquoi pas la ligne droite », la définition du slerp et ses propriétés, et « Les cas limites » (§8).

</details>
<details><summary>Indice 2</summary>

Le milieu de la ligne droite entre deux vecteurs unitaires a pour norme $\cos\frac\Omega2$ ; le slerp tourne de $t\Omega$ et garde la norme commune.

</details>
<details><summary>Indice 3</summary>

2. $\cos 50°$. 3. $0{,}3 \times 100°$. 6. Entre $t = 0{,}2$ et $t = 0{,}7$, le point tourne de $(0{,}7 - 0{,}2)\,\Omega$ ; convertis en radians. 7. Regarde la figure du §8, panneau de droite.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M25a.R1 — Le changement de variable en dimension 1 et les coordonnées polaires (M02b)

<details><summary>Indice 1</summary>

M02b §7 (coordonnées polaires) et §8 (changement de variable) ; le §2 de la fiche les rappelle.

</details>
<details><summary>Indice 2</summary>

$f_Y(y) = f_X\big(g^{-1}(y)\big)\,\lvert(g^{-1})'(y)\rvert$ ; en coordonnées polaires, $x = r\cos\theta$, $y = r\sin\theta$ et l'élément d'aire gagne un facteur $r$.

</details>
<details><summary>Indice 3</summary>

1. $g^{-1}(y) = \frac{y + 2}{3}$. 2. $g^{-1}(y) = e^{-y}$, pour $y \ge 0$. 5. Une primitive de $r\,e^{-r^2/2}$ est $-e^{-r^2/2}$.

</details>

### M25a.R2 — Le théorème spectral, Cholesky et la covariance AΣAᵀ (M12c)

<details><summary>Indice 1</summary>

M12c §6 (théorème spectral), §7 (Cholesky) et §8 (covariance d'une image linéaire, blanchiment).

</details>
<details><summary>Indice 2</summary>

$l_{11} = \sqrt{\Sigma_{11}}$, $l_{21} = \frac{\Sigma_{21}}{l_{11}}$, $l_{22} = \sqrt{\Sigma_{22} - l_{21}^2}$ ; valeurs propres par la trace et le déterminant ; $\mathbb{V}(\mathbf{a}^\top\mathbf{x}) = \mathbf{a}^\top\boldsymbol{\Sigma}\mathbf{a}$.

</details>
<details><summary>Indice 3</summary>

1. $l_{11} = 5$. 3. $\lambda^2 - 15\lambda + 50 = 0$. 5. Pense à $\mathbf{x} = (z, 2z)$. 6. Écris $\mathbf{z}^\top\mathbf{L}\mathbf{L}^\top\mathbf{z}$ comme le carré d'une norme.

</details>

### M25a.R3 — Les gradients de ln det X et de tr(AX) par rapport à une matrice (M18)

<details><summary>Indice 1</summary>

M18 §7, rappelé au §6 de la fiche.

</details>
<details><summary>Indice 2</summary>

$\nabla_{\mathbf{X}}\ln\det\mathbf{X} = \mathbf{X}^{-\top}$ (pour $\det\mathbf{X} > 0$) et $\nabla_{\mathbf{X}}\operatorname{tr}(\mathbf{A}\mathbf{X}) = \mathbf{A}^\top$ ; la trace est invariante par permutation circulaire.

</details>
<details><summary>Indice 3</summary>

1. Calcule $\mathbf{X}^{-1}$, puis transpose. 4. Un nombre est égal à sa trace, puis $\operatorname{tr}(\mathbf{u}^\top\mathbf{v}) = \operatorname{tr}(\mathbf{v}\mathbf{u}^\top)$. 5. $\det(c\mathbf{X}) = c^n\det\mathbf{X}$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M25a.1 — La densité d'un couple gaussien (température et humidité d'une serre) en deux points : distance de Mahalanobis contre distance euclidienne

<details><summary>Indice 1</summary>

Fiche §1 : la densité, la log-densité par Cholesky, et l'exemple du GPS.

</details>
<details><summary>Indice 2</summary>

$\boldsymbol{\Sigma}^{-1} = \frac{1}{\det\boldsymbol{\Sigma}}\begin{pmatrix} \Sigma_{22} & -\Sigma_{12} \\ -\Sigma_{12} & \Sigma_{11} \end{pmatrix}$ ; $\ln p = -\ln(2\pi) - \frac12\ln\det\boldsymbol{\Sigma} - \frac12\Delta^2$ en dimension 2. Le rapport de deux densités de la même loi est $e^{-(\Delta_Q^2 - \Delta_P^2)/2}$.

</details>
<details><summary>Indice 3</summary>

c) $l_{11} = 2$, $l_{21} = -3$, puis $l_{22}$. d) Pour $\mathbf{x}_P$ : $\mathbf{L}\mathbf{y} = (2, 3)$ donne $y_1 = 1$ et $y_2 = \frac{3 + 3}{5}$ ; fais de même pour $\mathbf{x}_Q$. e) $\frac{1}{2\pi\sqrt{\det\boldsymbol{\Sigma}}}$. h) Racine de $2^2 + 5^2$.

</details>

### Ex M25a.2 — Trois mesures corrélées : la loi d'une somme pondérée et d'une différence, puis un tirage μ + Lε par Cholesky et sa covariance

<details><summary>Indice 1</summary>

Fiche §2 : « Les transformations affines restent gaussiennes » et « La loi de μ + Lε, et tirer par Cholesky » ; M12c §7 pour la factorisation de Cholesky $3 \times 3$.

</details>
<details><summary>Indice 2</summary>

Colonne par colonne : $l_{11} = \sqrt{\Sigma_{11}}$, $l_{i1} = \frac{\Sigma_{i1}}{l_{11}}$, $l_{22} = \sqrt{\Sigma_{22} - l_{21}^2}$, $l_{32} = \frac{\Sigma_{32} - l_{31}l_{21}}{l_{22}}$, $l_{33} = \sqrt{\Sigma_{33} - l_{31}^2 - l_{32}^2}$. Pour une combinaison $\mathbf{w}^\top\mathbf{x}$ : moyenne $\mathbf{w}^\top\boldsymbol{\mu}$, variance $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$.

</details>
<details><summary>Indice 3</summary>

a) $l_{11} = 3$, $l_{21} = 1$, $l_{31} = -3$, $l_{22} = \sqrt{10 - 1}$. c) $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w} = \sum_iw_i^2\Sigma_{ii} + 2\sum_{i<j}w_iw_j\Sigma_{ij}$. e) $\operatorname{Cov}(c, \delta) = \mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{v}$ avec $\mathbf{v} = (-1, 1, 0)$. g) La covariance de $\mathbf{M}\boldsymbol{\varepsilon}$ est $\mathbf{M}\mathbf{M}^\top$ ; ici $\mathbf{M} = \mathbf{L}^\top$.

</details>

### Ex M25a.3 — Les ellipses à 90 % et à 95 % des composantes du vent sur un site : axes, demi-axes, aire, et la part des relevés dans l'ellipse de niveau c

<details><summary>Indice 1</summary>

Fiche §3 : « Les ellipses de niveau », « La masse d'une ellipse en dimension 2 », et l'exemple du GPS.

</details>
<details><summary>Indice 2</summary>

L'ellipse de masse $1 - \beta$ a pour niveau $c^2 = -2\ln\beta$ ; ses demi-axes valent $c\sqrt{\lambda_i}$ et son aire $\pi c^2\sqrt{\det\boldsymbol{\Sigma}}$.

</details>
<details><summary>Indice 3</summary>

a) Trace 20, déterminant 75. b) Résous $(\boldsymbol{\Sigma} - 15\mathbf{I})\mathbf{q} = \mathbf{0}$. c) À 90 %, $\beta = 0{,}1$. g) $1 - e^{-1{,}4^2/2}$. h) Calcule $\boldsymbol{\Sigma}^{-1}$ et l'écart $(8{,}5 - 2{,}5 ;\ 0 - 1)$.

</details>

### Ex M25a.4 — Un capteur en panne estimé par ses deux voisins : complément de Schur, loi conditionnelle en dimension 3, et l'écart-type gagné

<details><summary>Indice 1</summary>

Fiche §4 : « Découper un vecteur en deux blocs », « La loi conditionnelle » et l'exemple du bus (mais ici, ce sont deux coordonnées qu'on lit).

</details>
<details><summary>Indice 2</summary>

$\boldsymbol{\Sigma}_{bb}$ est le bloc des capteurs 1 et 3 (lignes et colonnes 1 et 3) ; $\boldsymbol{\Sigma}_{ab}$ est la ligne 2, colonnes 1 et 3. Moyenne : $\mu_2 + \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}(\mathbf{x}_b - \boldsymbol{\mu}_b)$ ; variance : $\Sigma_{22} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}$.

</details>
<details><summary>Indice 3</summary>

a) $\boldsymbol{\Sigma}_{bb} = \begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix}$, de déterminant 15. b) $(3, 2)$ fois $\boldsymbol{\Sigma}_{bb}^{-1}$. d) Les écarts lus sont $19{,}5 - 18$ et $14 - 15$. f) Avec un seul voisin, le poids est $\frac{\Sigma_{21}}{\Sigma_{11}}$. h) $\Lambda_{22}$ est l'inverse de la variance de $x_2$ sachant toutes les autres.

</details>

### Ex M25a.5 — Fusionner trois mesures d'une même distance : le produit de densités gaussiennes, des précisions qui s'additionnent, un ordre sans importance

<details><summary>Indice 1</summary>

Fiche §5 : « Le produit de deux densités » et « Fusionner des mesures ».

</details>
<details><summary>Indice 2</summary>

Précision fusionnée : la somme des précisions $\frac1{\sigma_i^2}$ ; moyenne fusionnée : $\sigma^2\sum_i\frac{x_i}{\sigma_i^2}$. Un résultat de fusion se fusionne avec la mesure suivante de la même façon.

</details>
<details><summary>Indice 3</summary>

a) Les précisions $\frac19$ et $\frac14$ font $\frac{13}{36}$. b) Fusionne $\mathcal{N}\big(\frac{367}{13}, \frac{36}{13}\big)$ avec la roue, de précision $\frac1{36}$. e) La précision du laser divisée par la précision totale.

</details>

### Ex M25a.6 — Étalonner un thermomètre par la régression linéaire bayésienne : loi jointe, évidence, posterior de (a, b), et prédictive près et loin des points d'étalonnage

<details><summary>Indice 1</summary>

Fiche §5 : « Le modèle linéaire gaussien », « La régression linéaire bayésienne », « Prédire : la prédictive » et « La vraisemblance marginale ».

</details>
<details><summary>Indice 2</summary>

Évidence : $\mathcal{N}(\boldsymbol{\Phi}\mathbf{m}_0, \boldsymbol{\Phi}\mathbf{S}_0\boldsymbol{\Phi}^\top + \sigma^2\mathbf{I})$ ; covariance croisée $\mathbf{S}_0\boldsymbol{\Phi}^\top$ ; $\mathbf{S}_N^{-1} = \mathbf{S}_0^{-1} + \sigma^{-2}\boldsymbol{\Phi}^\top\boldsymbol{\Phi}$, $\mathbf{m}_N = \mathbf{S}_N\sigma^{-2}\boldsymbol{\Phi}^\top\mathbf{e}$ ici ($\mathbf{m}_0 = \mathbf{0}$) ; prédictive $\mathcal{N}(\boldsymbol{\phi}_\star^\top\mathbf{m}_N, \boldsymbol{\phi}_\star^\top\mathbf{S}_N\boldsymbol{\phi}_\star + \sigma^2)$.

</details>
<details><summary>Indice 3</summary>

a) $\boldsymbol{\Phi}\mathbf{S}_0\boldsymbol{\Phi}^\top = \begin{pmatrix} 0{,}25 & 0{,}25 \\ 0{,}25 & 1{,}25 \end{pmatrix}$, puis ajoute le bruit. c) La log-densité en dimension 2 de $\mathbf{e}$, de moyenne nulle. d) $\sigma^{-2} = 25$ et $\boldsymbol{\Phi}^\top\boldsymbol{\Phi} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$. f) $\boldsymbol{\phi}_\star = (1 ;\ 0{,}5)$ ; g) $\boldsymbol{\phi}_\star = (1, 2)$.

</details>

### Ex M25a.7 — La divergence KL continue entre deux lois exponentielles et entre deux lois uniformes : les deux sens, une KL infinie, et deux durées de vie indépendantes

<details><summary>Indice 1</summary>

Fiche §7 : la définition de la KL continue, les exemples sur $[0, 1]$ et sur des supports différents, l'additivité.

</details>
<details><summary>Indice 2</summary>

Écris $\ln p(x) - \ln q(x)$, une fonction affine de $x$ pour deux lois exponentielles, puis prends son espérance sous $p$. Le paramètre est l'inverse de la moyenne.

</details>
<details><summary>Indice 3</summary>

a) $\ln\frac{ae^{-ax}}{be^{-bx}} = \ln\frac ab - (a - b)x$, et $\mathbb{E}_p[x] = \frac1a$. b) $a = \frac13$, $b = \frac18$. d) Sur $[2, 5]$, le rapport des densités vaut $\frac{1/3}{1/10}$. g) Les deux durées sont indépendantes sous les deux lois.

</details>

### Ex M25a.8 — Deux réglages d'une machine de découpe, deux gaussiennes en dimension 2 des erreurs de position : la KL dans les deux sens, et le cas de même covariance

<details><summary>Indice 1</summary>

Fiche §7 : le théorème de la KL entre deux gaussiennes et ses exemples.

</details>
<details><summary>Indice 2</summary>

$\mathrm{KL}(p_0 \,\|\, p_1) = \frac12\big[\operatorname{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0) + \boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta} - d + \ln\frac{\det\boldsymbol{\Sigma}_1}{\det\boldsymbol{\Sigma}_0}\big]$ ; dans l'autre sens, on échange les indices 0 et 1 partout (et $\boldsymbol{\delta}$ change de signe).

</details>
<details><summary>Indice 3</summary>

a) $\boldsymbol{\Sigma}_1^{-1} = \frac1{11}\begin{pmatrix} 2 & 1 \\ 1 & 6 \end{pmatrix}$ ; pour deux matrices symétriques, $\operatorname{tr}(\mathbf{A}\mathbf{B})$ est la somme des produits des coefficients de même position. b) $\boldsymbol{\delta} = (1, -1)$. h) Même covariance $\boldsymbol{\Sigma}_0$ : $\frac12\boldsymbol{\delta}^\top\boldsymbol{\Sigma}_0^{-1}\boldsymbol{\delta}$.

</details>

### Ex M25a.9 — La route orthodromique entre deux villes : angle au centre, point au tiers du trajet par le slerp, et profondeur du milieu de la corde

<details><summary>Indice 1</summary>

Fiche §8 : « Arc et corde » (le vecteur d'une latitude et d'une longitude) et la définition du slerp.

</details>
<details><summary>Indice 2</summary>

$\cos\Omega = \mathbf{u}^\top\mathbf{v}$ pour deux vecteurs unitaires ; arc $R\Omega$ ($\Omega$ en radians), corde $2R\sin\frac\Omega2$ ; le point au tiers est $\frac{\sin(2\Omega/3)}{\sin\Omega}\mathbf{u} + \frac{\sin(\Omega/3)}{\sin\Omega}\mathbf{v}$. La latitude d'un vecteur unitaire $\mathbf{p}$ est $\arcsin p_3$, sa longitude l'angle de $(p_1, p_2)$.

</details>
<details><summary>Indice 3</summary>

a) $\mathbf{u} = (\cos 48{,}39°\cos(-4{,}49°),\ \cos 48{,}39°\sin(-4{,}49°),\ \sin 48{,}39°)$ ; calculatrice en degrés. c) $\arccos(\mathbf{u}^\top\mathbf{v})$, en radians. g) Pour la longitude, $\arctan\frac{p_2}{p_1}$ convient ici car $p_1 > 0$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M25a.10 — Le changement de variable multivarié : la densité de μ + Lε est celle de N(μ, LLᵀ), et AX + b reste gaussien pour A inversible

<details><summary>Indice 1</summary>

Fiche §2 : le théorème du changement de variable et le cas affine $U(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}$, puis « La loi de μ + Lε ».

</details>
<details><summary>Indice 2</summary>

Trois ingrédients : l'antécédent $U^{-1}(\mathbf{x})$, le déterminant de la jacobienne de $U^{-1}$, et la densité de départ en l'antécédent. Puis $(\mathbf{L}\mathbf{L}^\top)^{-1} = \mathbf{L}^{-\top}\mathbf{L}^{-1}$ et $\det(\mathbf{L}\mathbf{L}^\top) = (\det\mathbf{L})^2$.

</details>
<details><summary>Indice 3</summary>

1. $U^{-1}(\mathbf{x}) = \mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})$, de jacobienne $\mathbf{L}^{-1}$. 3. Pose $\boldsymbol{\nu} = \mathbf{A}\boldsymbol{\mu} + \mathbf{b}$ et montre que l'antécédent moins $\boldsymbol{\mu}$ vaut $\mathbf{A}^{-1}(\mathbf{y} - \boldsymbol{\nu})$. 5. Résous $\mathbf{L}\boldsymbol{\varepsilon} = (3, 1)$.

</details>

### Ex M25a.11 — La masse d'une ellipse de Mahalanobis en dimension 2 vaut 1 − e^{−c²/2} ; la densité de la norme en dimension d, et son mode √(d − 1)

<details><summary>Indice 1</summary>

Fiche §3 : « La masse d'une ellipse en dimension 2 » et « En dimension d : le khi-deux, et la loi de la norme » ; M02b §7 pour les coordonnées polaires.

</details>
<details><summary>Indice 2</summary>

Après blanchiment, l'ellipse devient un disque ; en polaires, l'intégrande devient $\frac{1}{2\pi}e^{-r^2/2}r$. La densité d'une variable est la dérivée de sa fonction de répartition. Pour le mode, étudie le signe de la dérivée de $\ln f_d$.

</details>
<details><summary>Indice 3</summary>

2. $\int_0^{2\pi}\mathrm{d}\theta = 2\pi$, puis une primitive de $r\,e^{-r^2/2}$. 4. $\frac{4\pi}{(2\pi)^{3/2}} = \sqrt{\frac2\pi}$ ; par parties, $u = r$ et $v' = r\,e^{-r^2/2}$. 5. $\frac{\mathrm{d}}{\mathrm{d}r}\ln f_d = \frac{d - 1}{r} - r$. 6. Dans le rapport $\frac{f_{17}(4)}{f_{17}(1)}$, la constante $C_{17}$ se simplifie.

</details>

### Ex M25a.12 — Le maximum de vraisemblance d'une gaussienne multivariée : μ̂ = x̄ et Σ̂ = S/n, par les gradients de ln det et de la trace

<details><summary>Indice 1</summary>

Fiche §6 : la log-vraisemblance et les idées de la démonstration ; M18 §7 pour les gradients ; M05a pour $\ln b \le b - 1$.

</details>
<details><summary>Indice 2</summary>

Écris $\mathbf{x}_i - \boldsymbol{\mu} = (\mathbf{x}_i - \bar{\mathbf{x}}) + (\bar{\mathbf{x}} - \boldsymbol{\mu})$. En $\boldsymbol{\Lambda}$ : $\ell = \text{const} + \frac n2\ln\det\boldsymbol{\Lambda} - \frac12\operatorname{tr}(\boldsymbol{\Lambda}\mathbf{S})$. Pour le maximum, exprime $\operatorname{tr}(\boldsymbol{\Sigma}^{-1}\hat{\boldsymbol{\Sigma}})$ et $\ln\det\boldsymbol{\Sigma}$ avec $\mathbf{B} = \mathbf{C}^\top\boldsymbol{\Sigma}^{-1}\mathbf{C}$.

</details>
<details><summary>Indice 3</summary>

1. $\nabla_{\boldsymbol{\mu}}(\mathbf{x}_i - \boldsymbol{\mu})^\top\boldsymbol{\Lambda}(\mathbf{x}_i - \boldsymbol{\mu}) = -2\boldsymbol{\Lambda}(\mathbf{x}_i - \boldsymbol{\mu})$. 3. Le gradient est $\frac n2\boldsymbol{\Lambda}^{-1} - \frac12\mathbf{S}$. 4. $\operatorname{tr}(\boldsymbol{\Sigma}^{-1}\mathbf{C}\mathbf{C}^\top) = \operatorname{tr}(\mathbf{C}^\top\boldsymbol{\Sigma}^{-1}\mathbf{C})$ et $\det\mathbf{B} = \frac{\det\hat{\boldsymbol{\Sigma}}}{\det\boldsymbol{\Sigma}}$. 6. $\bar{\mathbf{x}} = (1, 2)$, et $\det\hat{\boldsymbol{\Sigma}} = \frac{131}{16}$.

</details>

### Ex M25a.13 — L'inégalité de Jensen pour une variable continue, la positivité de la KL continue, et l'additivité de la KL sur des lois produits

<details><summary>Indice 1</summary>

Fiche §7 : l'encadré de Jensen, la positivité et l'additivité ; M05a §1 pour la tangente.

</details>
<details><summary>Indice 2</summary>

$f(x) \ge f(m) + f'(m)(x - m)$, puis l'espérance. Pour la KL, $\mathrm{KL} = -\mathbb{E}_p\big[\ln\frac qp\big]$ et $\ln$ est concave. Pour l'additivité, le logarithme d'un produit est une somme.

</details>
<details><summary>Indice 3</summary>

3. $\mathbb{E}_p\big[\frac qp\big] = \int_{p > 0}q$. 5. $\iint p_1(\mathbf{x})p_2(\mathbf{y})h(\mathbf{x})\,\mathrm{d}\mathbf{x}\,\mathrm{d}\mathbf{y} = \int p_1h$. 6. $\int_0^1(2y - 1)\,\mathrm{d}y = 0$ ; pour la KL, utilise la question 4.

</details>

### Ex M25a.14 — La KL entre N(μ₀, Σ₀) et N(μ₁, Σ₁) en dimension d, par le lemme de la trace ; l'entropie différentielle de N(μ, Σ)

<details><summary>Indice 1</summary>

Fiche §7 : le lemme de la trace et son idée, le théorème, l'entropie différentielle ; §1 pour la log-densité.

</details>
<details><summary>Indice 2</summary>

Lemme : développe avec $\mathbf{x} - \mathbf{m} = (\mathbf{x} - \boldsymbol{\mu}) + (\boldsymbol{\mu} - \mathbf{m})$, puis l'astuce de la trace sur le premier terme. Pour la KL, applique le lemme deux fois sous $p_0$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbb{E}\big[(\mathbf{x} - \boldsymbol{\mu})^\top\mathbf{A}(\mathbf{x} - \boldsymbol{\mu})\big] = \operatorname{tr}\big(\mathbf{A}\,\mathbb{E}[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^\top]\big)$. 3. Avec $\mathbf{A} = \boldsymbol{\Sigma}_0^{-1}$, $\mathbf{m} = \boldsymbol{\mu}_0$, on trouve $d$. 5. $\mathbb{E}[\Delta^2] = d$. 7. $\mathbf{L}_1^{-1}\boldsymbol{\Sigma}_0\mathbf{L}_1^{-\top}$ a la même trace et le même déterminant que $\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0$.

</details>

### Ex M25a.15 — Le slerp entre deux vecteurs de même norme reste sur la sphère et avance d'un angle constant ; sa limite quand l'angle tend vers 0

<details><summary>Indice 1</summary>

Fiche §8 : les formules de soustraction et l'idée de la démonstration ; M12b §3 pour Gram-Schmidt.

</details>
<details><summary>Indice 2</summary>

$\mathbf{e}_1 = \frac{\mathbf{u}}{R}$, $\mathbf{w} = \mathbf{v} - (\mathbf{v}^\top\mathbf{e}_1)\mathbf{e}_1$, $\mathbf{e}_2 = \frac{\mathbf{w}}{\lVert\mathbf{w}\rVert}$. Puis $\sin((1 - t)\Omega) = \sin(\Omega - t\Omega)$.

</details>
<details><summary>Indice 3</summary>

1. $\lVert\mathbf{w}\rVert = R\sin\Omega$. 2. Le coefficient de $\mathbf{e}_1$ est $\frac{R}{\sin\Omega}\big(\sin((1 - t)\Omega) + \sin(t\Omega)\cos\Omega\big)$ : développe le premier sinus. 4. Écris $\frac{\sin(t\Omega)}{\sin\Omega} = t\cdot\frac{\sin(t\Omega)}{t\Omega}\cdot\frac{\Omega}{\sin\Omega}$. 5. $1 + \cos\Omega = 2\cos^2\frac\Omega2$. 6. $\sin\Omega = 2\sin\frac\Omega2\cos\frac\Omega2$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M25a.16 — Pont : des vecteurs rangés en lignes (n, d) comme dans les bibliothèques : tirer n points d'un coup par E Lᵀ + μ, la log-densité de chaque ligne, et la moyenne en nats par coordonnée

<details><summary>Indice 1</summary>

Fiche §2, l'encadré 📐 sur les vecteurs en lignes ; §1 pour la log-densité et la moyenne par coordonnée.

</details>
<details><summary>Indice 2</summary>

La ligne $i$ de $\mathbf{X}$ est $\boldsymbol{\mu}^\top + \boldsymbol{\varepsilon}_i^\top\mathbf{L}^\top$ ; l'écart de cette ligne à $\boldsymbol{\mu}$, blanchi par $\mathbf{L}^{-1}$, redonne $\boldsymbol{\varepsilon}_i$.

</details>
<details><summary>Indice 3</summary>

b) $(1, 0)\mathbf{L}^\top = (2, -1)$, puis ajoute $(7, 4)$ ; fais de même pour les deux autres lignes. c) $\Delta^2 = \lVert\boldsymbol{\varepsilon}_i\rVert^2$. d) $\det\boldsymbol{\Sigma} = 36$. e) Divise la somme par $3 \times 2$.

</details>

### Ex M25a.17 — MML §6.5 et la fin de §6.7.2 : densité, marginales et conditionnelles, produit, sommes et transformations, échantillonnage et changement de variable multivarié, en anglais

<details><summary>Indice 1</summary>

Suis le guide de lecture de la fiche, morceau par morceau, et garde ouvert l'encadré 📐 des notations.

</details>
<details><summary>Indice 2</summary>

Pour chaque formule du livre, écris la formule correspondante de la fiche à côté. Pour le produit (§6.5.2), le livre emploie les lettres de deux densités, $\mathbf{a}, \mathbf{A}$ et $\mathbf{b}, \mathbf{B}$ ; repère où apparaît le scalaire et où apparaît le vecteur moyen du résultat.

</details>
<details><summary>Indice 3</summary>

6. Une densité est positive, un déterminant peut être négatif. 7. Choisis une matrice $2 \times 2$ simple dont le déterminant $ad - bc$ est négatif, et un point $\mathbf{y} = \mathbf{A}\mathbf{x}$ pour un $\mathbf{x}$ entier (l'antécédent est alors facile) ; compare $\frac{1}{2\pi}e^{-\lVert\mathbf{x}\rVert^2/2}\lvert\det\mathbf{A}\rvert^{-1}$ à la densité de $\mathcal{N}(\mathbf{0}, \mathbf{A}\mathbf{A}^\top)$ en $\mathbf{y}$.

</details>

### Ex M25a.18 — MML §9.3 : régression linéaire bayésienne, prédictions a priori et a posteriori, vraisemblance marginale, en anglais

<details><summary>Indice 1</summary>

Suis le guide de lecture de la fiche, et l'encadré 📐 du §5 sur les notations de MML §9.3.

</details>
<details><summary>Indice 2</summary>

Pour 3, ne garde que les termes qui dépendent de $\boldsymbol{\theta}$, et range-les en un terme quadratique $\boldsymbol{\theta}^\top\mathbf{A}\boldsymbol{\theta}$ et un terme linéaire $-2\mathbf{a}^\top\boldsymbol{\theta}$. Pour 4, compare la matrice de (9.52) à celle de (9.48a).

</details>
<details><summary>Indice 3</summary>

7. Relis le §2 de la fiche, « Ce qui ne reste pas gaussien ». 8. Écris la loss minimisée dans (9.32), puis multiplie la log-vraisemblance par $-2\sigma^2$. 9. Moyenne $\mathbf{X}m_0$, covariance $s_0^2\mathbf{X}\mathbf{X}^\top + \sigma^2\mathbf{I}$, puis la log-densité de dimension 2.

</details>

### Ex M25a.19 — Expliquer avec deux thermomètres voisins pourquoi lire l'un resserre l'estimation de l'autre, et pourquoi la valeur lue ne change pas cette incertitude

<details><summary>Indice 1</summary>

Fiche §4 : « Comment le lire », et l'exemple du bus (« on le comprend sans formule »).

</details>
<details><summary>Indice 2</summary>

Sépare ce que fait le thermomètre en panne en deux parts : ce qu'il a en commun avec l'autre, et ce qui lui est propre. La lecture révèle la première, pas la seconde.

</details>
<details><summary>Indice 3</summary>

La taille de la part propre dépend de la force du lien entre les deux appareils, qui ne change pas d'une lecture à l'autre. Pour la réserve : que penserais-tu d'un thermomètre qui afficherait une valeur impossible ?

</details>

<a id="entretien"></a>

## 💼 Entretien

### M25a.E1 — « Comment tirer un vecteur gaussien de covariance donnée à partir de tirages indépendants, et pourquoi Cholesky ? »

<details><summary>Indice 1</summary>

Fiche §2 : « La loi de μ + Lε, et tirer par Cholesky », « Pourquoi Cholesky ? » et l'encadré 📐 sur les lignes.

</details>
<details><summary>Indice 2</summary>

Recette, preuve (moyenne, covariance, loi), autres racines possibles, avantages de Cholesky, cas semi-défini, convention NumPy, chemin inverse : sept points, une ou deux phrases chacun.

</details>
<details><summary>Indice 3</summary>

Pour le cas semi-défini : que fait-on quand la factorisation de Cholesky échoue sur une matrice qui devrait être une covariance (une petite valeur sur la diagonale, ou les valeurs propres) ?

</details>

<a id="notebook"></a>

## Notebook

### M25a.20 — La log-densité d'une loi normale multivariée, par Cholesky : `mvn_logpdf`

<details><summary>Indice 1</summary>

Fiche §1, « La log-densité, par Cholesky », et la docstring : les formes acceptées (`x` de forme `(d,)` ou `(n, d)`) et les refus.

</details>
<details><summary>Indice 2</summary>

Convertis avec `np.asarray(…, dtype=float)`, contrôle les formes, puis `L = np.linalg.cholesky(cov)` dans un `try` (une `np.linalg.LinAlgError` devient une `ValueError` « pas définie positive »). Mets les écarts en lignes, `dev = np.atleast_2d(x) - mean`, et résous `np.linalg.solve(L, dev.T)` : chaque colonne du résultat est un $\mathbf{y}$.

</details>
<details><summary>Indice 3</summary>

$\ln\det\boldsymbol{\Sigma}$ = `2 * np.log(np.diag(L)).sum()` ; $\Delta^2$ = la somme des carrés de chaque colonne de `y` (`(y ** 2).sum(axis=0)`). Contrôle la symétrie avec la règle de la docstring avant Cholesky (`np.linalg.cholesky` ne lit qu'un triangle). Rends `float(...)` pour un `x` 1-D, un tableau sinon. Ensuite, dans le notebook : c) `cov = 0.3 ** np.abs(np.subtract.outer(np.arange(600), np.arange(600)))`, puis `mymath.gaussian.mvn_logpdf(x, np.zeros(600), cov)`.

</details>

### M25a.21 — Tirer des vecteurs de loi N(μ, Σ) par Cholesky : `sample_mvn`

<details><summary>Indice 1</summary>

Fiche §2 : « La loi de μ + Lε, et tirer par Cholesky » et l'encadré 📐 ; la docstring dit les contrôles de `n` et de `seed` (un entier NumPy est accepté, un booléen refusé).

</details>
<details><summary>Indice 2</summary>

`rng = np.random.default_rng(seed)`, puis **un seul** appel `E = rng.standard_normal((n, d))`, puis `mean + E @ L.T`.

</details>
<details><summary>Indice 3</summary>

Pour refuser un booléen : `isinstance(n, bool)` avant `isinstance(n, numbers.Integral)` (`True` est un entier pour Python). Ensuite : a) `X = mymath.gaussian.sample_mvn(mean, cov, 20000, seed=5921)`, `X.mean(axis=0)` et `np.cov(X, rowvar=False, bias=True)` ; b) `cost = X @ np.array([2.0, 1.0, 3.0])` ; c) `W = np.linalg.solve(L, (X - mean).T).T`.

</details>

### M25a.22 — Le complément de Schur d'un bloc, et la loi conditionnelle d'un vecteur gaussien : `schur_complement`, `condition_gaussian`

<details><summary>Indice 1</summary>

Fiche §4 : le complément de Schur (et l'encadré 📐 sur les lettres de la docstring) et la loi conditionnelle ; le 💻 du §4 sur `np.ix_`.

</details>
<details><summary>Indice 2</summary>

`rest = [i for i in range(m) if i not in idx]` ; les blocs `M[np.ix_(rest, rest)]`, `M[np.ix_(rest, idx)]`, `M[np.ix_(idx, rest)]`, `M[np.ix_(idx, idx)]` ; puis `A - B @ np.linalg.solve(D, C)`. Pour la loi conditionnelle, la même chose avec `cov`, et la moyenne `mean[rest] + S_ab @ np.linalg.solve(S_bb, values - mean[idx])`.

</details>
<details><summary>Indice 3</summary>

Contrôle `idx` avant tout : une liste ou un tuple d'entiers (pas de booléen), distincts, entre 0 et $m - 1$, au moins un et moins de $m$ ; `values` doit être 1-D, de longueur `len(idx)`. `values[j]` va avec `idx[j]` : garde cet ordre pour `mean[idx]`. Ensuite : a) `mymath.gaussian.condition_gaussian(mean, cov, [0, 2], [19.5, 14.0])` ; c) `np.linalg.det(cov[np.ix_([0, 2], [0, 2])]) * np.linalg.det(schur)`.

</details>

### M25a.23 — Le posterior d'une régression linéaire bayésienne : `linreg_posterior`

<details><summary>Indice 1</summary>

Fiche §5 : le théorème de MML (Théorème 9.1) sous la forme « précisions », et la docstring (un `Phi` de forme `(0, p)` est permis : sans données, l'a priori).

</details>
<details><summary>Indice 2</summary>

`P0 = np.linalg.solve(S0, np.eye(p))` (la précision a priori), `prec = P0 + Phi.T @ Phi / noise_var`, `S_N = np.linalg.solve(prec, np.eye(p))`, puis `m_N = S_N @ (P0 @ m0 + Phi.T @ y / noise_var)`.

</details>
<details><summary>Indice 3</summary>

Refuse `noise_var` booléen, non fini ou $\le 0$ ; contrôle que $\mathbf{S}_0$ est symétrique et définie positive (Cholesky). Ensuite : b) une boucle sur les deux lignes de `Phi`, chaque loi a posteriori servant d'a priori, avec `Phi[i:i + 1]` et `e[i:i + 1]` ; d) pour le tracé, dans l'axe reçu : `ts = np.linspace(-0.5, 2.5, 301)`, `F = np.column_stack([np.ones_like(ts), ts])`, la moyenne `F @ m_N`, la variance `np.einsum("ij,jk,ik->i", F, S_N, F) + 0.04`, puis `ax.fill_between(100 * ts, …)` et `ax.plot`.

</details>

### M25a.24 — `scipy.stats.multivariate_normal`, `np.cov` et `scipy.integrate` : tes log-densités, le maximum de vraisemblance, et la KL de M25a.8 par une intégrale double

<details><summary>Indice 1</summary>

Fiche §1, §6 et §7 : les trois 💻 (`multivariate_normal`, `np.cov`, `dblquad`).

</details>
<details><summary>Indice 2</summary>

`p0 = scipy.stats.multivariate_normal(mu0, Sigma0)` ; `p0.logpdf(X)` accepte un tableau de lignes. `scipy.integrate.dblquad(f, a, b, c, d)` intègre `f(y, x)` (attention à l'ordre des arguments) pour $x$ de $a$ à $b$ et $y$ de $c$ à $d$.

</details>
<details><summary>Indice 3</summary>

d) `f = lambda y, x: p0.pdf([x, y]) * (p0.logpdf([x, y]) - p1.logpdf([x, y]))`, puis `dblquad(f, mu0[0] - 25, mu0[0] + 25, mu0[1] - 25, mu0[1] + 25)[0]`. e) `terms = p0.logpdf(X) - p1.logpdf(X)`, puis `terms.mean()` et `terms.std() / np.sqrt(len(terms))`. b) `Xc = X - X.mean(axis=0)`, puis `Xc.T @ Xc / len(X)`.

</details>

### M25a.25 — Prédire la part des tirages dans l'ellipsoïde de Mahalanobis de même niveau quand la dimension passe de 2 à 10, puis mesurer

<details><summary>Indice 1</summary>

Fiche §3 : « En dimension d : le khi-deux, et la loi de la norme ». Fais tes prédictions avant de lire la suite.

</details>
<details><summary>Indice 2</summary>

Après blanchiment, $\Delta^2$ est une somme de $d$ carrés de variables $\mathcal{N}(0, 1)$ indépendantes : que deviennent sa loi et sa moyenne quand on ajoute des coordonnées, alors que le niveau reste fixé ?

</details>
<details><summary>Indice 3</summary>

Pour la mesure : `Sd = 0.6 ** np.abs(np.subtract.outer(np.arange(d), np.arange(d)))`, `X = mymath.gaussian.sample_mvn(np.zeros(d), Sd, 100000, seed=5925)`, `d2 = (X * np.linalg.solve(Sd, X.T).T).sum(axis=1)`, puis `(d2 <= 2 * np.log(10)).mean()`.

</details>

### M25a.26 — Conditionner par simulation : garder les tirages dont une mesure tombe près d'une valeur, et comparer à la loi conditionnelle exacte

<details><summary>Indice 1</summary>

Fiche §4 : la loi conditionnelle, et le 💻 qui parle de conditionner par simulation.

</details>
<details><summary>Indice 2</summary>

a) `mymath.gaussian.condition_gaussian(mean, cov, [0], [23.0])` (la température est la coordonnée 0). Pour chaque $h$, un masque `keep = np.abs(X[:, 0] - 23) < h`, puis `X[keep, 1]`.

</details>
<details><summary>Indice 3</summary>

Range, pour chaque $h$, `keep.sum()`, `X[keep, 1].mean()` et `X[keep, 1].var()`. Pour le tracé, dans les axes reçus : `ax.set_xscale("log")`, les points contre `hs`, et `ax.axhline` aux valeurs exactes.

</details>

### M25a.27 — Les ellipses de niveau d'une gaussienne en dimension 2, une tranche (la loi conditionnelle) et une projection (la loi marginale), selon la corrélation

<details><summary>Indice 1</summary>

Fiche §3 (le 💻 sur le tracé d'une ellipse) et §4 (« En dimension 2, avec la corrélation »).

</details>
<details><summary>Indice 2</summary>

Une ellipse de niveau $c$ : `t = np.linspace(0, 2 * np.pi, 200)`, `circle = c * np.vstack([np.cos(t), np.sin(t)])`, puis `points = mean[:, None] + L @ circle`. Les niveaux à 75 % et à 90 % : $c^2 = 2\ln 4$ et $2\ln 10$.

</details>
<details><summary>Indice 3</summary>

Dans `ax_joint` : `ax_joint.plot(points[0], points[1])` pour chaque niveau, `ax_joint.axvline(x1_value)`, la droite $x_2 = \mu_2 + \frac{\Sigma_{21}}{\Sigma_{11}}(x_1 - \mu_1)$, et `ax_joint.set_aspect("equal")`. Dans `ax_cut` : la densité de `scipy.stats.norm(m, np.sqrt(v))` pour la marginale ($\mu_2$, $\Sigma_{22}$) et pour la conditionnelle (rendue par `mymath.gaussian.condition_gaussian(mean, cov, [0], [x1_value])`), puis `ax_cut.legend()`. N'ouvre pas de figure dans la fonction : la cellule d'appel crée `fig, axes = plt.subplots(2, 3)` et passe `axes[0, k]` et `axes[1, k]`.

</details>

### M25a.28 — Chasse à l'erreur : un tirage par E L au lieu de E Lᵀ, ln det Σ sans le facteur 2, et une covariance conditionnelle qui dépend de la valeur observée

<details><summary>Indice 1</summary>

Les trois ⚠️ de la fiche, aux §1, §2 et §4. Pour chaque fonction, demande-toi ce que la vérification du collègue ne pouvait pas voir.

</details>
<details><summary>Indice 2</summary>

(1) Quelle covariance a $\mathbf{E}\mathbf{L}$, ligne par ligne ? Pour quelles matrices $\mathbf{L} = \mathbf{L}^\top$ ? (2) Dans une **différence** de deux log-densités de la même loi, que deviennent les termes qui ne dépendent pas de $\mathbf{x}$ ? (3) Que vaut le terme ajouté quand les voisins lisent leur moyenne ?

</details>
<details><summary>Indice 3</summary>

(1) La covariance des lignes de `E @ L` est $\mathbf{L}^\top\mathbf{L}$ ; corrige en `E @ L.T`. (2) $\ln\det\boldsymbol{\Sigma} = 2\sum_i\ln L_{ii}$. (3) Garde $\boldsymbol{\Sigma}_{bb}$ telle quelle, dans la moyenne comme dans la covariance. a) Calcule `L.T @ L` avec `L = np.linalg.cholesky(cov)` pour le vent.

</details>

### M25a.29 — Un test de propriété : la moyenne et la covariance empiriques de tes tirages, à une tolérance fixée par l'erreur type

<details><summary>Indice 1</summary>

Fiche §2 (la loi de $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$) et M02c (l'erreur type d'une moyenne). L'énoncé donne les deux erreurs types.

</details>
<details><summary>Indice 2</summary>

a) Une comparaison échoue à tort avec la probabilité $2(1 - \Phi(k))$ ; la borne de la réunion pour 5 comparaisons demande $5 \times 2(1 - \Phi(k)) \le 0{,}01$. e) Un écart de $0{,}02\,\Sigma_{jj}$ doit dépasser $k\,\Sigma_{jj}\sqrt{2/n}$.

</details>
<details><summary>Indice 3</summary>

a) `k = scipy.stats.norm.ppf(1 - 0.01 / 10)`. Dans le test : `se_m = np.sqrt(np.diag(cov) / n)` et `se_S = np.sqrt((np.outer(np.diag(cov), np.diag(cov)) + cov ** 2) / n)`, puis compare `np.abs(S - cov)` à `k * se_S` coefficient par coefficient, et lève `AssertionError(f"expected … within …, got …")` au premier écart. b) Compte les échecs dans un `try`/`except AssertionError`, graine par graine.

</details>

### M25a.30 — Défi : reconstruire les températures manquantes le long d'une route par la loi conditionnelle d'une gaussienne, sous une erreur quadratique moyenne fixée

<details><summary>Indice 1</summary>

Fiche §4 : la loi conditionnelle et le 💻 sur les processus gaussiens ; §5 : une mesure bruitée est une valeur vraie plus un bruit indépendant.

</details>
<details><summary>Indice 2</summary>

Forme le vecteur des 31 valeurs « vraies températures aux positions en panne, mesures aux autres » : sa moyenne est $m(s)$, et sa covariance est $\mathbf{K}$ plus la variance du bruit **sur la diagonale des positions mesurées seulement** (un bruit indépendant ne change aucune covariance entre deux positions différentes, ni la vraie température d'une position en panne).

</details>
<details><summary>Indice 3</summary>

`C = K + 0.16 * np.diag([0.0 if i in miss else 1.0 for i in range(31)])`, puis `mymath.gaussian.condition_gaussian(m, C, list(obs), y_obs)` : la moyenne et la covariance conditionnelles des positions `miss`, dans l'ordre croissant ; les écarts-types sont `np.sqrt(np.diag(cov))`. Passe `obs` comme une liste d'entiers.

</details>
