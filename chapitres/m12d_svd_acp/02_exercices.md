# M12d · SVD et analyse en composantes principales — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m12d_svd_acp/06_mes_reponses.md` (créée par `python tools/start_chapter.py M12d`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, les valeurs singulières, les valeurs propres et les variances se donnent **par ordre décroissant** ; un vecteur singulier à droite $\mathbf{v}_i$, un vecteur propre unitaire ou un axe principal se donne avec la **convention de la fiche** (sa coordonnée de plus grande valeur absolue est positive ; en cas d'égalité, la première), et le vecteur singulier à gauche qui va avec est $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i/s_i$ ; la matrice de covariance de données se calcule avec $\frac{1}{n - 1}$ ; l'**erreur de reconstruction moyenne** est la moyenne, sur les exemples, de $\lVert \mathbf{x}_i - \hat{\mathbf{x}}_i \rVert^2$.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M12d.Q1 — La SVD : formes et propriétés 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

$\mathbf{A}$ est de forme $(5, 3)$ et de rang 2.
1. Les formes de $\mathbf{U}$, $\mathbf{S}$ et $\mathbf{V}$ dans la SVD complète ? Dans la SVD compacte ?
2. Combien $\mathbf{A}$ a-t-elle de valeurs singulières non nulles ? Combien de vecteurs $\mathbf{v}_i$ engendrent son noyau ?
3. Vrai ou faux : une valeur singulière peut être négative.
4. Que vaut $\mathbf{A}\mathbf{v}_1$ ? Et $\mathbf{A}^\top\mathbf{u}_1$ ?
5. La SVD de $\operatorname{diag}(3, -5)$ : ses valeurs singulières, dans l'ordre, et où passe le signe moins ?
6. `U, s, Vt = np.linalg.svd(A, full_matrices=False)` : où lis-tu $\mathbf{v}_2$ ? Quelle est la forme de `U` ?

### M12d.Q2 — Valeurs singulières et valeurs propres 🧠 ★ ⏱️ 4 min
*Fiche §1 et §2 · parcours C, E*

Vrai ou faux ?
1. Les valeurs singulières de $\mathbf{A}$ sont les valeurs propres de $\mathbf{A}^\top\mathbf{A}$.
2. Pour une matrice symétrique définie positive, les valeurs singulières sont les valeurs propres.
3. Pour une matrice symétrique quelconque, $s_i = \lvert\lambda_i\rvert$ (rangées autrement).
4. $\mathbf{A}^\top\mathbf{A}$ et $\mathbf{A}\mathbf{A}^\top$ ont les mêmes valeurs propres non nulles, même si $\mathbf{A}$ n'est pas carrée.
5. Pour une matrice carrée, la plus grande valeur propre en module est le plus grand étirement $\max \lVert \mathbf{A}\mathbf{x} \rVert / \lVert \mathbf{x} \rVert$.
6. Une matrice orthogonale a toutes ses valeurs singulières égales à 1.
7. Pour une matrice carrée, $\lvert\det\mathbf{A}\rvert$ est le produit des valeurs singulières.
8. $\mathbf{A}$ et $\mathbf{A}^\top$ ont les mêmes valeurs singulières.

### M12d.Q3 — Rang faible : ce qu'on garde, ce qu'on perd 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Une matrice $\mathbf{A}$ de forme $(100, 80)$ a pour valeurs singulières non nulles $12, 9, 4, 2, 1$.
1. Son rang ? Que vaut $\lVert \mathbf{A} \rVert_F^2$ ?
2. L'erreur de la meilleure approximation de rang 2, en norme de Frobenius ? En norme spectrale ?
3. La part d'énergie gardée par $\mathbf{A}_2$ ?
4. Combien de nombres pour stocker $\mathbf{A}_2$, contre combien pour $\mathbf{A}$ ?
5. Vrai ou faux : si l'on oublie la couche de valeur singulière 9 au lieu de celle de valeur 4, l'erreur au carré augmente de $81 - 16$.
6. Pourquoi retire-t-on le niveau de gris moyen d'une image avant de juger l'énergie gardée par un rang faible ?

### M12d.Q4 — Pseudo-inverse et conditionnement 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Si $\mathbf{A}$ est carrée et inversible, que vaut $\mathbf{A}^+$ ?
2. $\mathbf{D} = \operatorname{diag}(4, 0, 2)$ : que vaut $\mathbf{D}^+$ ?
3. Si $\mathbf{A}$ est de forme $(3, 5)$, quelle est la forme de $\mathbf{A}^+$ ?
4. Le conditionnement de $\mathbf{D}$ ? De $\operatorname{diag}(5, -2)$ ? De $7\,\mathbf{I}_4$ ?
5. Vrai ou faux : un déterminant de $10^{-6}$ prouve que le système est mal conditionné.
6. $\kappa(\mathbf{A}) = 10^4$ : combien de chiffres significatifs peut-on perdre sur la solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$ ? Et en passant par les équations normales $\mathbf{A}^\top\mathbf{A}\mathbf{x} = \mathbf{A}^\top\mathbf{b}$ ?
7. $\mathbf{A}\mathbf{A}^+$ est la projection orthogonale sur quel sous-espace ?

### M12d.Q5 — Ce que maximise un axe principal 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Pour une direction unitaire $\mathbf{u}$, quelle est la variance des coordonnées $t_i = \mathbf{u}^\top(\mathbf{x}_i - \boldsymbol{\mu})$ ?
2. Le maximum de cette variance sur la sphère unité, et où est-il atteint ?
3. Vrai ou faux : le premier axe principal est toujours la direction de la feature de plus grande variance.
4. $\mathbf{C} = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 2 & 2 \\ 0 & 2 & 5 \end{pmatrix}$ : les axes principaux et les variances le long des axes ?
5. Que vaut la somme des variances le long des $p$ axes ?
6. Pourquoi les axes principaux sont-ils orthogonaux deux à deux ?
7. Deux logiciels rendent des premiers axes opposés : l'un des deux se trompe-t-il ?

### M12d.Q6 — Centrer et standardiser avant une ACP ? 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Que devient le premier axe si l'on oublie de centrer un nuage loin de l'origine ?
2. Deux features : une distance en kilomètres et un prix en euros. Centrer seulement, ou standardiser ? Pourquoi ?
3. Des températures relevées en °C par dix capteurs identiques : centrer, standardiser ? Pourquoi ?
4. Vrai ou faux : l'ACP de données standardisées est l'ACP de leur matrice de corrélation.
5. Les scores sur deux axes principaux différents sont-ils de moyenne nulle ? Corrélés ?
6. Que donne la reconstruction d'un exemple avec $k = p$ composantes ?

### M12d.Q7 — Variance expliquée et nombre de composantes 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Un nuage de $n = 11$ exemples de $\mathbb{R}^3$ a pour variances le long de ses axes $5$, $4$ et $1$ (covariance en $\frac{1}{n-1}$).
1. Les parts de variance expliquée ? Combien de composantes pour garder au moins 85 % ?
2. Pourquoi divise-t-on par la somme de **toutes** les variances ?
3. L'erreur de reconstruction moyenne avec $k = 1$ ?
4. Vrai ou faux : avec $n = 11$ exemples dans $\mathbb{R}^{50}$, au plus 10 variances sont non nulles.
5. Qu'est-ce que le « coude » d'une courbe de variances ?
6. Pourquoi l'erreur de reconstruction mesurée sur les données d'entraînement est-elle optimiste ?

### M12d.Q8 — ACP, t-SNE ou UMAP : qui garde quoi ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. Laquelle des trois méthodes garde les grandes distances ? Lesquelles gardent les voisinages ?
2. Vrai ou faux : t-SNE, comme l'ACP, définit une fonction de $\mathbb{R}^p$ dans $\mathbb{R}^2$.
3. Que veut dire une perplexité de 5 pour un point ?
4. Calcule $p\log_2(p/q)$ pour un couple de voisins ($p = 0{,}04$) que la carte place trop loin ($q = 0{,}005$), puis pour un couple lointain ($p = 0{,}000\,5$) qu'elle place trop près ($q = 0{,}004$). Lequel coûte le plus ?
5. Pourquoi t-SNE mesure-t-il les voisinages de la carte avec une loi de Student plutôt qu'une gaussienne ?
6. Que dit la divergence de l'écart entre deux groupes bien séparés d'une carte t-SNE ?

<a id="rappels"></a>

## 🔁 Rappels

### M12d.R1 — Valeurs propres et théorème spectral (M12c) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

$\mathbf{K} = \begin{pmatrix} -2 & 5 \\ 5 & 22 \end{pmatrix}$.
1. Sa trace, son déterminant, puis ses valeurs propres.
2. Ses vecteurs propres unitaires (convention de la fiche).
3. Écris $\mathbf{K} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ et vérifie $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$.
4. D'après la fiche §1, quelles sont les valeurs singulières de $\mathbf{K}$ ? Que deviennent $\mathbf{u}_i$ et $\mathbf{v}_i$ ?
5. $\mathbf{K}$ est-elle définie positive ?

### M12d.R2 — La projection orthogonale (M12b) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

$\mathbf{u} = \frac{1}{17}(8, 9, 12)$ et $\mathbf{x} = (11, 9, 10)$.
1. Vérifie que $\mathbf{u}$ est unitaire.
2. La coordonnée $t = \mathbf{u}^\top\mathbf{x}$ de $\mathbf{x}$ le long de $\mathbf{u}$.
3. La projection $\mathbf{p} = t\,\mathbf{u}$, et le résidu $\mathbf{r} = \mathbf{x} - \mathbf{p}$. Vérifie $\mathbf{r} \perp \mathbf{u}$.
4. Vérifie $\lVert \mathbf{x} \rVert^2 = t^2 + \lVert \mathbf{r} \rVert^2$.
5. La matrice $\mathbf{P} = \mathbf{u}\mathbf{u}^\top$ : son rang ? Que vaut $\mathbf{P}^2$ ?

### M12d.R3 — Moyenne, covariance et standardisation (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

Quatre exemples à deux features : $(2, 35)$, $(4, 55)$, $(6, 40)$, $(8, 50)$.
1. Le point moyen, puis les données centrées.
2. Les deux variances et la covariance, avec $\frac{1}{n - 1}$.
3. La corrélation des deux features.
4. Les valeurs standardisées du premier exemple.
5. On exprime la deuxième feature dans une unité dix fois plus petite (ses valeurs sont multipliées par 10) : que deviennent sa variance, la covariance et la corrélation ?

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12d.1 — La SVD d'une matrice 2 × 2 à la main, par AᵀA ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la SVD d'une matrice carrée non symétrique par les valeurs et vecteurs propres de $\mathbf{A}^\top\mathbf{A}$, avec la convention de signe.
**Prérequis :** fiche §1 ; M12c §3 et §6 · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 10 & 10 \\ 5 & 2 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{A}^\top\mathbf{A}$ | une matrice |
| b | les valeurs propres de $\mathbf{A}^\top\mathbf{A}$ | une liste de 2 nombres |
| c | les valeurs singulières $s_1$, $s_2$ | une liste de 2 nombres |
| d | $\mathbf{v}_1$ | une liste de 2 nombres (4 décimales) |
| e | $\mathbf{v}_2$ | une liste de 2 nombres (4 décimales) |
| f | $\mathbf{u}_1 = \mathbf{A}\mathbf{v}_1/s_1$ | une liste de 2 nombres (4 décimales) |
| g | $\det\mathbf{A}$ | un nombre |
| h | les valeurs propres de $\mathbf{A}$ elle-même | une liste de 2 nombres (4 décimales) |

Dans ta copie : calcule $\mathbf{u}_2$ et vérifie $s_1\mathbf{u}_1\mathbf{v}_1^\top + s_2\mathbf{u}_2\mathbf{v}_2^\top = \mathbf{A}$ (les racines carrées disparaissent). Relie g) à c). Pourquoi h) n'a-t-il rien à voir avec c) ?

### Ex M12d.2 — La SVD compacte d'une matrice 3 × 2 de rang 1 ✏️ ★★ ⏱️ 15 min
**Objectif :** reconnaître une matrice de rang 1, écrire sa SVD compacte, et y appliquer la convention de signe.
**Prérequis :** fiche §1 ; M12a §5 · **Parcours :** C

$\mathbf{A} = \begin{pmatrix} 2 & -10 \\ 10 & -50 \\ 11 & -55 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le rang de $\mathbf{A}$ | un entier |
| b | $\mathbf{A}^\top\mathbf{A}$ | une matrice |
| c | les valeurs propres de $\mathbf{A}^\top\mathbf{A}$ | une liste de 2 nombres |
| d | $s_1$ | un nombre (4 décimales) |
| e | $\mathbf{v}_1$ | une liste de 2 nombres (4 décimales) |
| f | $\mathbf{u}_1 = \mathbf{A}\mathbf{v}_1/s_1$ | une liste de 3 nombres (4 décimales) |
| g | $\lVert \mathbf{A} \rVert_F^2$ | un nombre |
| h | le vecteur unitaire $\mathbf{v}_2$ qui engendre le noyau de $\mathbf{A}$ (convention de la fiche) | une liste de 2 nombres (4 décimales) |

Dans ta copie : écris $\mathbf{A} = \mathbf{a}\mathbf{b}^\top$ avec des vecteurs entiers, et déduis-en $s_1 = \lVert \mathbf{a} \rVert\,\lVert \mathbf{b} \rVert$ sans calculer $\mathbf{A}^\top\mathbf{A}$. Écris la SVD compacte $\mathbf{U}_1\mathbf{S}_1\mathbf{V}_1^\top$ : combien de nombres contient-elle, contre combien pour la SVD complète ? Pourquoi $\mathbf{u}_1$ a-t-il des coordonnées négatives ?

### Ex M12d.3 — Le cercle unité devient une ellipse : axes et demi-axes ✏️ ★ ⏱️ 15 min
**Objectif :** lire sur la SVD l'image du cercle unité : les demi-axes, leurs directions, les points du cercle qui y arrivent, l'aire.
**Prérequis :** fiche §2 · **Parcours :** C, E

$\mathbf{B} = \begin{pmatrix} 1 & 8 \\ 4 & -4 \end{pmatrix}$ envoie le cercle unité sur une ellipse.

| | Question | Réponse attendue |
|---|---|---|
| a | les longueurs des demi-axes de l'ellipse, du grand au petit | une liste de 2 nombres |
| b | un vecteur unitaire porté par le grand axe, de première coordonnée positive | une liste de 2 nombres (4 décimales) |
| c | les deux vecteurs $\pm\mathbf{x}$ du cercle unité envoyés aux deux bouts du grand axe : celui qui suit la convention de la fiche | une liste de 2 nombres (4 décimales) |
| d | l'aire de l'ellipse divisée par $\pi$ | un nombre |
| e | $\lVert \mathbf{B}\mathbf{e}_1 \rVert$ | un nombre (4 décimales) |
| f | $\lVert \mathbf{B}\mathbf{e}_2 \rVert$ | un nombre (4 décimales) |
| g | le rapport du grand demi-axe au petit | un nombre (2 décimales) |
| h | vrai ou faux : $\mathbf{B}$ conserve l'orientation du plan | `True` ou `False` |

Dans ta copie : dessine le cercle, l'ellipse, ses deux demi-axes et les images de $\mathbf{e}_1$ et $\mathbf{e}_2$. Pourquoi e) et f) sont-ils compris entre les deux longueurs de a) ? Quel point du cercle est envoyé au bout du **petit** axe ?

### Ex M12d.4 — L'approximation de rang 1 d'une matrice 3 × 3 et son erreur ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une SVD $3 \times 3$ quand $\mathbf{A}^\top\mathbf{A}$ est par blocs, en déduire la meilleure approximation de rang 1 et son erreur (Eckart-Young).
**Prérequis :** fiche §1 et §3 · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 4 & 2 & 1 \\ 4 & 2 & -1 \\ 1 & 4 & 0 \end{pmatrix}$ (trois clients, trois produits : une note de $-5$ à $5$ par case).

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert \mathbf{A} \rVert_F^2$ | un nombre |
| b | $\mathbf{A}^\top\mathbf{A}$ | une matrice |
| c | les valeurs singulières | une liste de 3 nombres (4 décimales) |
| d | $\mathbf{v}_1$ | une liste de 3 nombres (4 décimales) |
| e | $\mathbf{u}_1$ | une liste de 3 nombres (4 décimales) |
| f | $\mathbf{A}_1 = s_1\mathbf{u}_1\mathbf{v}_1^\top$ | une matrice (4 décimales) |
| g | $\lVert \mathbf{A} - \mathbf{A}_1 \rVert_F$ | un nombre (4 décimales) |
| h | la part d'énergie gardée par $\mathbf{A}_1$ | un nombre (4 décimales) |

Dans ta copie : pourquoi la troisième colonne de $\mathbf{A}$ donne-t-elle à elle seule une valeur singulière ? Vérifie g) en calculant $\mathbf{A} - \mathbf{A}_1$ élément par élément. Que vaut l'erreur en norme spectrale ? Que « raconte » $\mathbf{A}_1$ sur les goûts des trois clients ?

### Ex M12d.5 — Compter les nombres stockés : une image en rang k ✏️ ★ ⏱️ 10 min
**Objectif :** compter ce que coûte une approximation de rang $k$, et trouver le rang au-delà duquel elle ne fait plus rien gagner.
**Prérequis :** fiche §3 · **Parcours :** C

Une photo en niveaux de gris a $900 \times 1\,600$ pixels. On la stocke par son approximation de rang $k$ : les $k$ vecteurs $\mathbf{u}_i$, les $k$ vecteurs $\mathbf{v}_i$ et les $k$ valeurs singulières.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de nombres de l'image entière | un entier |
| b | le nombre de nombres pour $k = 40$ | un entier |
| c | la part que cela représente | un nombre (4 décimales) |
| d | le plus grand $k$ pour lequel le stockage de rang $k$ est plus petit que l'image | un entier |
| e | le plus grand $k$ qui tient dans 2 % des nombres de l'image | un entier |
| f | une photo **couleur** de même taille (trois canaux de $900 \times 1\,600$), chaque canal stocké en rang 40 : le nombre total | un entier |
| g | la même photo, les trois canaux mis côte à côte en une matrice $900 \times 4\,800$ stockée en rang 40 | un entier |

Dans ta copie : f) et g) gardent-ils la même information ? Lequel serait, à ton avis, le meilleur à nombre égal, et pourquoi (les trois canaux d'une photo se ressemblent-ils) ? Pourquoi un vrai format d'image compte-t-il des bits plutôt que des nombres ?

### Ex M12d.6 — La pseudo-inverse d'une matrice non inversible et la solution de norme minimale ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la pseudo-inverse d'une matrice de rang 1, la solution de norme minimale d'un système qui en a une infinité, et la solution des moindres carrés d'un système qui n'en a pas.
**Prérequis :** fiche §4 ; M09b §3 ; M12b §5 · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 2 & -8 & 16 \\ 5 & -20 & 40 \end{pmatrix}$, $\mathbf{y} = (18, 45)$, $\mathbf{y}' = (1, 0)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le rang de $\mathbf{A}$ | un entier |
| b | $s_1$ | un nombre (4 décimales) |
| c | $\lVert \mathbf{A} \rVert_F^2$ | un nombre |
| d | $1\,000\,\mathbf{A}^+$ | une matrice (4 décimales) |
| e | $\mathbf{x}^+ = \mathbf{A}^+\mathbf{y}$ | une liste de 3 nombres (4 décimales) |
| f | $\lVert \mathbf{x}^+ \rVert$ | un nombre |
| g | la norme de la solution $\mathbf{x} = (9, 0, 0)$ de $\mathbf{A}\mathbf{x} = \mathbf{y}$ | un nombre |
| h | $\mathbf{A}\mathbf{A}^+\mathbf{y}'$ | une liste de 2 nombres (4 décimales) |

Dans ta copie : écris $\mathbf{A} = \mathbf{a}\mathbf{b}^\top$ et montre que $\mathbf{A}^+ = \mathbf{A}^\top/\lVert \mathbf{A} \rVert_F^2$ pour une matrice de rang 1. Décris l'ensemble des solutions de $\mathbf{A}\mathbf{x} = \mathbf{y}$ : pourquoi $\mathbf{x}^+$ est-il le plus proche de l'origine ? Pour $\mathbf{y}'$, que représente h), et que vaut la distance $\lVert \mathbf{A}\mathbf{x} - \mathbf{y}' \rVert$ minimale ?

### Ex M12d.7 — Le conditionnement de trois matrices, et l'erreur relative sur une solution ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer des conditionnements, en tirer la borne sur l'erreur relative d'une solution, et constater que le déterminant ne dit rien de la sensibilité.
**Prérequis :** fiche §2 et §4 · **Parcours :** C, E

$\mathbf{P} = \begin{pmatrix} 0 & 5 \\ -2 & 0 \end{pmatrix}$, $\mathbf{Q} = \frac{1}{13}\begin{pmatrix} 5 & -12 \\ 12 & 5 \end{pmatrix}$, $\mathbf{R} = \begin{pmatrix} 8 & 3 \\ 5 & 2 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\kappa(\mathbf{P})$ | un nombre (1 décimale) |
| b | $\kappa(\mathbf{Q})$ | un nombre |
| c | $\kappa(\mathbf{R})$ | un nombre (4 décimales) |
| d | la borne sur l'erreur relative de $\mathbf{x}$, solution de $\mathbf{R}\mathbf{x} = \mathbf{b}$, quand $\mathbf{b}$ est connu à 0,1 % près (en fraction : 0,1 % = 0,001) | un nombre (4 décimales) |
| e | la solution de $\mathbf{R}\mathbf{x} = (14, 9)$ | une liste de 2 nombres |
| f | pour $\delta\mathbf{b} = (0{,}01 ;\ 0)$, le rapport $\dfrac{\lVert \delta\mathbf{x} \rVert / \lVert \mathbf{x} \rVert}{\lVert \delta\mathbf{b} \rVert / \lVert \mathbf{b} \rVert}$ | un nombre (2 décimales) |
| g | $\kappa(\mathbf{R}^\top\mathbf{R})$ | un nombre (1 décimale) |
| h | vrai ou faux : $\kappa(1\,000\,\mathbf{R}) = \kappa(\mathbf{R})$ | `True` ou `False` |

Dans ta copie : pour c), utilise $s_1^2 + s_2^2 = \lVert \mathbf{R} \rVert_F^2$ et $s_1 s_2 = \lvert\det\mathbf{R}\rvert$ : pourquoi $\kappa + \frac{1}{\kappa} = 102$ ici ? Compare f) à c). Quelle perturbation $\delta\mathbf{b}$ (de quelle direction) atteindrait la borne ? $\det\mathbf{R} = 1$ et $\det\mathbf{P} = 10$ : qu'en conclure ?

### Ex M12d.8 — Les axes principaux d'un nuage de ℝ³ : covariance, polynôme caractéristique, variances et axes ✏️ ★★ ⏱️ 35 min
**Objectif :** calculer la matrice de covariance d'un petit nuage, factoriser son polynôme caractéristique grâce à sa structure par blocs, et en tirer les variances le long des axes et les axes principaux.
**Prérequis :** fiche §5 et §6 ; M12c §3 ; M02c · **Parcours :** C, E

Sept objets, trois mesures chacun (dans la même unité), en lignes :
$$\mathbf{X} = \begin{pmatrix} 10 & 8 & 3 \\ 9 & 14 & 7 \\ 15 & 4 & 9 \\ 10 & 6 & 4 \\ 16 & 11 & 6 \\ 18 & 10 & 6 \\ 20 & 10 & 7 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | le point moyen $\boldsymbol{\mu}$ | une liste de 3 nombres |
| b | la matrice de covariance $\mathbf{C}$ | une matrice |
| c | la variance totale | un nombre |
| d | $\det\mathbf{C}$ | un nombre |
| e | les variances $\lambda_1 \ge \lambda_2 \ge \lambda_3$ le long des axes | une liste de 3 nombres |
| f | le premier axe principal $\mathbf{u}_1$ | une liste de 3 nombres (4 décimales) |
| g | le troisième axe principal $\mathbf{u}_3$ | une liste de 3 nombres (4 décimales) |
| h | la variance des coordonnées le long de $\frac{1}{\sqrt{2}}(1, 0, 1)$ | un nombre (1 décimale) |

Dans ta copie : écris $\det(\mathbf{C} - \lambda\mathbf{I})$ en développant selon la deuxième ligne, et factorise-le. Vérifie que la somme et le produit des variances de e) sont c) et d). Quel est le deuxième axe, sans calcul ? Pourquoi h) est-il inférieur à $\lambda_1$, alors que $(1, 0, 1)$ « mélange » les deux mesures corrélées entre elles ?

### Ex M12d.9 — Scores, reconstruction et erreur de reconstruction moyenne avec deux composantes sur trois ✏️ ★★ ⏱️ 20 min
**Objectif :** projeter un nuage sur ses deux premiers axes, reconstruire un exemple, et relier l'erreur de reconstruction moyenne aux variances oubliées.
**Prérequis :** fiche §6 et §7 ; Ex M12d.8 · **Parcours :** C, E

Le nuage de M12d.8, avec ses trois axes principaux. On garde $k = 2$ composantes.

| | Question | Réponse attendue |
|---|---|---|
| a | les scores $(t_{71}, t_{72})$ du septième objet sur $\mathbf{u}_1$ et $\mathbf{u}_2$ | une liste de 2 nombres (4 décimales) |
| b | la reconstruction $\hat{\mathbf{x}}_7$ du septième objet | une liste de 3 nombres (4 décimales) |
| c | les sept scores sur $\mathbf{u}_1$, multipliés par $\sqrt{17}$ (des entiers), dans l'ordre des objets | une liste de 7 nombres |
| d | leur variance (avec $\frac{1}{n - 1}$) | un nombre |
| e | la covariance des scores sur $\mathbf{u}_1$ avec la première mesure $x_1$ | un nombre (4 décimales) |
| f | l'erreur de reconstruction moyenne avec $k = 2$ | un nombre (4 décimales) |
| g | l'erreur de reconstruction moyenne avec $k = 1$ | un nombre (4 décimales) |
| h | la part de variance gardée avec $k = 2$ | un nombre (4 décimales) |

Dans ta copie : vérifie que les scores de c) sont de moyenne nulle, et que leur covariance avec ceux de $\mathbf{u}_2$ est nulle. Montre que e) vaut $\lambda_1$ fois la première coordonnée de $\mathbf{u}_1$ (écris la covariance comme $\mathbf{u}_1^\top\mathbf{C}\,\mathbf{e}_1$). Vérifie f) directement, en calculant les sept scores sur $\mathbf{u}_3$ (multipliés par $\sqrt{17}$, ce sont des entiers) et la moyenne de leurs carrés. D'où vient le facteur $\frac{n-1}{n}$ ? Compare $\hat{\mathbf{x}}_7$ à $\mathbf{x}_7$ : quelle mesure n'a pas bougé, et pourquoi ?

### Ex M12d.10 — La variance expliquée cumulée : combien de composantes pour 95 % ? ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des parts de variance expliquée, choisir un nombre de composantes par un seuil, et le comparer au coude de la courbe.
**Prérequis :** fiche §7 · **Parcours :** C, E

Une ACP de $n = 51$ exemples à 8 features donne les variances le long des axes (covariance en $\frac{1}{n-1}$) : $9{,}6$ ; $4{,}8$ ; $2{,}4$ ; $1{,}1$ ; $0{,}7$ ; $0{,}6$ ; $0{,}5$ ; $0{,}3$.

| | Question | Réponse attendue |
|---|---|---|
| a | la variance totale | un nombre |
| b | la part de variance expliquée par le premier axe | un nombre (4 décimales) |
| c | les parts cumulées des trois premiers axes | une liste de 3 nombres (4 décimales) |
| d | le plus petit $k$ qui garde au moins 90 % de la variance | un entier |
| e | le plus petit $k$ qui garde au moins 95 % | un entier |
| f | la somme des variances oubliées avec $k = 3$ | un nombre (4 décimales) |
| g | l'erreur de reconstruction moyenne avec $k = 3$ | un nombre (4 décimales) |

Dans ta copie : trace la courbe des variances et celle des parts cumulées. Où est le coude ? Les seuils de d) et e) disent-ils la même chose que le coude ? Si ces données préparent un modèle, comment trancherais-tu ?

### Ex M12d.11 — L'ACP par la SVD de la matrice centrée : s² / (n − 1) donne les variances ✏️ ★★ ⏱️ 20 min
**Objectif :** faire une ACP par la SVD de la matrice centrée, sans former la covariance : valeurs singulières, variances, axes et scores.
**Prérequis :** fiche §1 et §6 · **Parcours :** C

Quatre exemples de $\mathbb{R}^3$, en lignes : $\mathbf{X} = \begin{pmatrix} 3 & 1 & 3 \\ 3 & 4 & 6 \\ 9 & 4 & 8 \\ 9 & 7 & 3 \end{pmatrix}$. On note $\mathbf{X}_c$ la matrice centrée et $\mathbf{X}_c = \mathbf{U}\mathbf{S}\mathbf{V}^\top$ sa SVD compacte. Les vecteurs $(5, 3, 1)$, $(0, -1, 3)$ et $(-2, 3, 1)$ sont orthogonaux deux à deux.

| | Question | Réponse attendue |
|---|---|---|
| a | le point moyen | une liste de 3 nombres |
| b | $\mathbf{X}_c^\top\mathbf{X}_c$ | une matrice |
| c | les valeurs propres de $\mathbf{X}_c^\top\mathbf{X}_c$ pour $(5, 3, 1)$, $(0, -1, 3)$ et $(-2, 3, 1)$, dans cet ordre | une liste de 3 nombres |
| d | les valeurs singulières de $\mathbf{X}_c$ | une liste de 3 nombres (4 décimales) |
| e | les variances le long des axes | une liste de 3 nombres |
| f | le premier axe principal $\mathbf{v}_1$ | une liste de 3 nombres (4 décimales) |
| g | la première colonne $\mathbf{u}_1$ de $\mathbf{U}$ | une liste de 4 nombres (4 décimales) |
| h | les scores des quatre exemples sur le premier axe | une liste de 4 nombres (4 décimales) |

Dans ta copie : vérifie que h) est $s_1\mathbf{u}_1$, que sa moyenne est nulle et que sa variance est la première de e). Pourquoi $\mathbf{X}_c$ a-t-elle au plus trois valeurs singulières non nulles, alors qu'elle a quatre lignes ? Quelle erreur donnerait $s_j^2/n$ ?

### Ex M12d.12 — L'ACP quand n < p : passer par la petite matrice XXᵀ ✏️ ★★ ⏱️ 20 min
**Objectif :** faire l'ACP de trois exemples de $\mathbb{R}^5$ par la matrice $3 \times 3$ $\mathbf{X}_c\mathbf{X}_c^\top$, et remonter aux axes principaux.
**Prérequis :** fiche §1 et §7 · **Parcours :** C

Trois exemples de $\mathbb{R}^5$, en lignes : $\mathbf{X} = \begin{pmatrix} 8 & 8 & 4 & 6 & 5 \\ 3 & 8 & 3 & 2 & 7 \\ 4 & 2 & 2 & 4 & 9 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le point moyen | une liste de 5 nombres |
| b | $\mathbf{G} = \mathbf{X}_c\mathbf{X}_c^\top$ | une matrice |
| c | les valeurs propres de $\mathbf{G}$ | une liste de 3 nombres |
| d | les variances non nulles le long des axes | une liste de 2 nombres |
| e | le nombre de variances nulles parmi les 5 | un entier |
| f | le premier axe principal $\mathbf{v}_1$ | une liste de 5 nombres (4 décimales) |
| g | les scores des trois exemples sur $\mathbf{v}_1$ | une liste de 3 nombres (4 décimales) |

Dans ta copie : vérifie que $(1, 0, -1)$, $(1, -2, 1)$ et $(1, 1, 1)$ sont des vecteurs propres de $\mathbf{G}$, et explique pourquoi la valeur propre de $(1, 1, 1)$ est nulle. Calcule le deuxième axe de la même façon. Combien d'opérations pour diagonaliser $\mathbf{G}$, contre la matrice $5 \times 5$ $\mathbf{X}_c^\top\mathbf{X}_c$ ? Et pour 500 images de $10^4$ pixels ?

### Ex M12d.13 — Les probabilités de voisinage de t-SNE sur quatre points, et leur perplexité 2^H ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des probabilités de voisinage de t-SNE, leur entropie en bits et leur perplexité, puis les symétriser.
**Prérequis :** fiche §8 ; M06 §2 et §8 · **Parcours :** C, E

Quatre points de $\mathbb{R}^3$ : $\mathbf{x}_1 = (0, 0, 0)$, $\mathbf{x}_2 = (1, 0, 0)$, $\mathbf{x}_3 = (1, 1, 0)$, $\mathbf{x}_4 = (1, 1, 1)$. Tous les points ont la même largeur $\sigma$, choisie pour que $2\sigma^2 = \frac{1}{\ln 2}$ (soit $\sigma \approx 0{,}85$) : alors $\exp\big(-\frac{d^2}{2\sigma^2}\big) = 2^{-d^2}$.

| | Question | Réponse attendue |
|---|---|---|
| a | les carrés des distances de $\mathbf{x}_1$ à $\mathbf{x}_2$, $\mathbf{x}_3$ et $\mathbf{x}_4$ | une liste de 3 nombres |
| b | $p_{2 \mid 1}$, $p_{3 \mid 1}$, $p_{4 \mid 1}$ | une liste de 3 nombres (4 décimales) |
| c | l'entropie $H(P_1)$, en bits | un nombre (4 décimales) |
| d | la perplexité $2^{H(P_1)}$ | un nombre (4 décimales) |
| e | $p_{1 \mid 2}$ | un nombre (4 décimales) |
| f | la probabilité symétrisée $p_{12}$ (formule de la fiche §8, avec $n = 4$) | un nombre (4 décimales) |
| g | la limite de la perplexité de $P_1$ quand $\sigma \to +\infty$ | un nombre |

Dans ta copie : écris c) sous forme exacte ($\log_2 7$ y apparaît). Que devient la perplexité de $P_1$ quand $\sigma \to 0$ ? Entre quelles valeurs varie-t-elle donc ici, et pourquoi faut-il une dichotomie pour atteindre une perplexité fixée ? Pourquoi $p_{2 \mid 1} \ne p_{1 \mid 2}$ ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion (R4). La grille de relecture de `05_solutions.md` dit ce qu'une démonstration correcte doit contenir.

### Ex M12d.14 — Les valeurs singulières sont les racines des valeurs propres de AᵀA ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer le lien entre la SVD et les valeurs propres de $\mathbf{A}^\top\mathbf{A}$ et de $\mathbf{A}\mathbf{A}^\top$, dans les deux sens.
**Prérequis :** fiche §1 ; M12c §6 et §7 · **Parcours :** C, E

$\mathbf{A}$ est de forme $(m, n)$.
1. Montre que $\mathbf{A}^\top\mathbf{A}$ est symétrique et que $\mathbf{x}^\top\mathbf{A}^\top\mathbf{A}\mathbf{x} = \lVert \mathbf{A}\mathbf{x} \rVert^2$. Déduis-en que ses valeurs propres sont réelles et positives ou nulles.
2. Si $\mathbf{A} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$ (SVD complète), calcule $\mathbf{A}^\top\mathbf{A}$. Déduis-en que les $s_i^2$ (complétés par des zéros) sont les valeurs propres de $\mathbf{A}^\top\mathbf{A}$, de vecteurs propres les $\mathbf{v}_i$.
3. Réciproquement, soit $\mathbf{v}_1, \ldots, \mathbf{v}_n$ une base orthonormée de vecteurs propres de $\mathbf{A}^\top\mathbf{A}$, de valeurs propres $\lambda_i$. Montre que les vecteurs $\mathbf{A}\mathbf{v}_i/\sqrt{\lambda_i}$, pour $\lambda_i > 0$, sont orthonormés.
4. Montre que $\mathbf{A}\mathbf{A}^\top$ a les mêmes valeurs propres non nulles que $\mathbf{A}^\top\mathbf{A}$ : si $\mathbf{A}^\top\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ avec $\lambda \ne 0$, que vaut $\mathbf{A}\mathbf{A}^\top(\mathbf{A}\mathbf{v})$, et pourquoi $\mathbf{A}\mathbf{v} \ne \mathbf{0}$ ? Montre aussi que $\mathbf{v} \mapsto \mathbf{A}\mathbf{v}$ est injective sur l'espace propre de $\lambda$ : les multiplicités sont les mêmes.
5. Déduis de la trace de $\mathbf{A}^\top\mathbf{A}$ que $\lVert \mathbf{A} \rVert_F^2 = \sum_i s_i^2$.

### Ex M12d.15 — La plus grande valeur singulière est le plus grand étirement : ‖A x‖ ≤ s₁ ‖x‖ ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'encadrement de $\lVert \mathbf{A}\mathbf{x} \rVert$ par les valeurs singulières extrêmes, et en tirer une propriété de la norme spectrale.
**Prérequis :** fiche §2 ; M12b §2 · **Parcours :** C

$\mathbf{A} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$ est de forme $(m, n)$, de valeurs singulières $s_1 \ge \cdots \ge s_n \ge 0$ (complétées par des zéros si le rang est plus petit que $n$) ; on suppose $n \le m$.
1. Écris $\mathbf{x} = \sum_i c_i\mathbf{v}_i$ dans la base orthonormée des $\mathbf{v}_i$. Exprime $\lVert \mathbf{x} \rVert^2$, puis $\mathbf{A}\mathbf{x}$ et $\lVert \mathbf{A}\mathbf{x} \rVert^2$, avec les $c_i$ et les $s_i$.
2. Déduis-en $s_n\lVert \mathbf{x} \rVert \le \lVert \mathbf{A}\mathbf{x} \rVert \le s_1\lVert \mathbf{x} \rVert$, et les cas d'égalité.
3. Retrouve le résultat autrement : $\lVert \mathbf{A}\mathbf{x} \rVert^2/\lVert \mathbf{x} \rVert^2$ est un quotient de Rayleigh. De quelle matrice ?
4. Montre que $\lVert \mathbf{A}\mathbf{B} \rVert_2 \le \lVert \mathbf{A} \rVert_2\,\lVert \mathbf{B} \rVert_2$ (en appliquant deux fois l'inégalité de droite de 2., qui vaut pour toute forme, sans l'hypothèse $n \le m$).
5. Une matrice orthogonale $\mathbf{Q}$ : que valent $\lVert \mathbf{Q} \rVert_2$ et $\lVert \mathbf{Q}\mathbf{A} \rVert_2$ ?

### Ex M12d.16 — L'erreur de l'approximation de rang k vaut la somme des s² oubliés (Frobenius) ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer l'égalité d'Eckart-Young pour l'erreur de $\mathbf{A}_k$ (la minimalité restant admise), en norme de Frobenius et en norme spectrale.
**Prérequis :** fiche §3 ; M12c §2 · **Parcours :** C

$\mathbf{A} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$, de rang $r$, et $\mathbf{A}_k = \sum_{i \le k} s_i\mathbf{u}_i\mathbf{v}_i^\top$ pour $k < r$.
1. Montre que $\lVert \mathbf{M} \rVert_F^2 = \operatorname{tr}(\mathbf{M}^\top\mathbf{M})$, puis que $\lVert \mathbf{Q}\mathbf{M} \rVert_F = \lVert \mathbf{M} \rVert_F$ pour toute matrice orthogonale $\mathbf{Q}$.
2. Montre aussi $\lVert \mathbf{M}\mathbf{Q} \rVert_F = \lVert \mathbf{M} \rVert_F$ (par $\operatorname{tr}(\mathbf{X}\mathbf{Y}) = \operatorname{tr}(\mathbf{Y}\mathbf{X})$, M12c).
3. Écris $\mathbf{A} - \mathbf{A}_k = \mathbf{U}\mathbf{D}\mathbf{V}^\top$ avec une matrice $\mathbf{D}$ que tu préciseras. Conclus : $\lVert \mathbf{A} - \mathbf{A}_k \rVert_F^2 = s_{k+1}^2 + \cdots + s_r^2$.
4. Montre que $\lVert \mathbf{A} - \mathbf{A}_k \rVert_2 = s_{k+1}$ (avec M12d.15).
5. Montre que $\lVert \mathbf{A}_k \rVert_F^2 + \lVert \mathbf{A} - \mathbf{A}_k \rVert_F^2 = \lVert \mathbf{A} \rVert_F^2$ : quel théorème reconnais-tu, et quelles deux matrices sont orthogonales **entre elles** pour le produit scalaire $\langle \mathbf{X}, \mathbf{Y} \rangle = \operatorname{tr}(\mathbf{X}^\top\mathbf{Y})$ ?

### Ex M12d.17 — La pseudo-inverse donne la solution des moindres carrés de plus petite norme ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer, par un changement de base orthonormée, que $\mathbf{A}^+\mathbf{b}$ minimise $\lVert \mathbf{A}\mathbf{x} - \mathbf{b} \rVert$, et qu'il est, parmi les minimiseurs, de plus petite norme.
**Prérequis :** fiche §4 ; M09b §3 ; M12b §2 · **Parcours :** C

$\mathbf{A} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$ (SVD complète) est de forme $(m, n)$ et de rang $r$ ; $\mathbf{b} \in \mathbb{R}^m$.
1. On pose $\mathbf{y} = \mathbf{V}^\top\mathbf{x}$ et $\mathbf{c} = \mathbf{U}^\top\mathbf{b}$. Montre que $\lVert \mathbf{A}\mathbf{x} - \mathbf{b} \rVert^2 = \lVert \mathbf{S}\mathbf{y} - \mathbf{c} \rVert^2 = \sum_{i \le r}(s_iy_i - c_i)^2 + \sum_{i > r} c_i^2$, et $\lVert \mathbf{x} \rVert = \lVert \mathbf{y} \rVert$.
2. Quels $\mathbf{y}$ minimisent cette quantité ? Lesquelles de leurs coordonnées sont libres ?
3. Parmi eux, lequel est de plus petite norme ? Déduis-en $\mathbf{x}^+ = \mathbf{V}\mathbf{S}^+\mathbf{U}^\top\mathbf{b}$, avec une matrice $\mathbf{S}^+$ que tu préciseras, puis $\mathbf{x}^+ = \mathbf{A}^+\mathbf{b}$.
4. Que vaut le résidu minimal $\lVert \mathbf{A}\mathbf{x}^+ - \mathbf{b} \rVert^2$ ? Quand est-il nul ?
5. Si les colonnes de $\mathbf{A}$ sont libres, montre que $\mathbf{A}^+ = (\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top$ (M09b).

### Ex M12d.18 — L'erreur de reconstruction moyenne est la somme des variances oubliées ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule de l'erreur de reconstruction moyenne d'une ACP à $k$ composantes, et le partage de la variance totale entre ce que l'on garde et ce que l'on perd.
**Prérequis :** fiche §5 à §7 ; M12b §2 · **Parcours :** C, E

$n$ exemples $\mathbf{x}_i$ de $\mathbb{R}^p$, de moyenne $\boldsymbol{\mu}$ et de covariance $\mathbf{C}$ (en $\frac{1}{n-1}$), d'axes principaux $\mathbf{u}_1, \ldots, \mathbf{u}_p$ et de variances $\lambda_1 \ge \cdots \ge \lambda_p$ ; $t_{ij} = \mathbf{u}_j^\top(\mathbf{x}_i - \boldsymbol{\mu})$ et $\hat{\mathbf{x}}_i = \boldsymbol{\mu} + \sum_{j \le k} t_{ij}\mathbf{u}_j$.
1. Montre que $\mathbf{x}_i - \boldsymbol{\mu} = \sum_{j \le p} t_{ij}\mathbf{u}_j$, puis que $\lVert \mathbf{x}_i - \hat{\mathbf{x}}_i \rVert^2 = \sum_{j > k} t_{ij}^2$.
2. Les scores $t_{ij}$ sont de moyenne nulle, et leur variance vaut $\mathbf{u}_j^\top\mathbf{C}\,\mathbf{u}_j$ (la règle $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$ de M12c §8, avec la ligne $\mathbf{A} = \mathbf{u}_j^\top$). Déduis-en $\frac{1}{n - 1}\sum_i t_{ij}^2 = \lambda_j$.
3. Conclus : $\frac{1}{n}\sum_i \lVert \mathbf{x}_i - \hat{\mathbf{x}}_i \rVert^2 = \frac{n - 1}{n}\sum_{j > k}\lambda_j$.
4. Montre de même que $\frac{1}{n}\sum_i \lVert \hat{\mathbf{x}}_i - \boldsymbol{\mu} \rVert^2 = \frac{n-1}{n}\sum_{j \le k}\lambda_j$, et déduis-en que la dispersion gardée et l'erreur ont pour somme $\frac{n-1}{n}\operatorname{tr}\mathbf{C}$.
5. Pourquoi, à $k$ fixé, prendre les $k$ **premiers** axes rend-il cette erreur la plus petite parmi les choix de $k$ axes principaux ? (La minimalité parmi **tous** les sous-espaces est admise, fiche §7.)

### Ex M12d.19 — Les scores de deux composantes principales sont décorrélés ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer que les scores sur deux axes principaux distincts ont une covariance nulle, et que ce n'est pas vrai pour deux directions orthogonales quelconques.
**Prérequis :** fiche §5 et §6 ; M12c §6 et §8 · **Parcours :** C

Mêmes notations que M12d.18 ; $\mathbf{t}_j = \mathbf{X}_c\mathbf{u}_j$ est la colonne des scores sur l'axe $j$, et $\mathbf{Z} = \mathbf{X}_c\mathbf{W}_k$, avec $\mathbf{W}_k = (\mathbf{u}_1 \mid \cdots \mid \mathbf{u}_k)$, la matrice des scores sur les $k$ premiers axes. Les scores d'un exemple, $\mathbf{z}_i = \mathbf{W}_k^\top(\mathbf{x}_i - \boldsymbol{\mu})$, sont une transformation affine de $\mathbf{x}_i$ : par la règle de M12c §8, ils sont de moyenne nulle et de covariance $\mathbf{W}_k^\top\mathbf{C}\,\mathbf{W}_k$.
1. Lis le coefficient $(j, l)$ de cette matrice : $\operatorname{Cov}(\mathbf{t}_j, \mathbf{t}_l) = \mathbf{u}_j^\top\mathbf{C}\,\mathbf{u}_l$. Montre qu'il vaut $\lambda_j$ si $j = l$, et 0 si $j \ne l$ ; écris la matrice de covariance de $\mathbf{Z}$.
2. Un score combiné $c_i = \mathbf{a}^\top\mathbf{z}_i$, avec $\mathbf{a} \in \mathbb{R}^k$ : sa variance ? Pourquoi est-elle si simple ?
3. Contre-exemple : avec $\mathbf{C} = \operatorname{diag}(4, 1)$, calcule la covariance des coordonnées le long des deux directions orthogonales $\frac{1}{13}(5, 12)$ et $\frac{1}{13}(-12, 5)$. Qu'est-ce qui, dans 1., a servi en plus de l'orthogonalité ?

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12d.20 — Pont : détecter une anomalie par son erreur de reconstruction 🔗 ★ ⏱️ 15 min
**Objectif :** calculer l'erreur de reconstruction d'exemples nouveaux, la comparer à celles des données d'entraînement, et voir ce que ce score ne voit pas.
**Prérequis :** fiche §7 ; Ex M12d.8 et M12d.9 · **Parcours :** C, E

On garde l'ACP à $k = 2$ composantes du nuage de M12d.8 (sa moyenne et ses axes, calculés sur les sept objets). Trois objets nouveaux arrivent : $\mathbf{r}_1 = (18, 12, 7)$, $\mathbf{r}_2 = (13, 9, 9)$ et $\mathbf{r}_3 = (30, 9, 10)$. On signale un objet si son erreur de reconstruction dépasse la plus grande erreur des sept objets d'origine.

| | Question | Réponse attendue |
|---|---|---|
| a | l'erreur de reconstruction $\lVert \mathbf{r}_1 - \hat{\mathbf{r}}_1 \rVert^2$ | un nombre |
| b | celle de $\mathbf{r}_2$ | un nombre (4 décimales) |
| c | la plus grande erreur de reconstruction des sept objets d'origine | un nombre (4 décimales) |
| d | vrai ou faux : $\mathbf{r}_2$ est signalé | `True` ou `False` |
| e | le score $t_1$ de $\mathbf{r}_3$ sur le premier axe | un nombre (4 décimales) |
| f | la plus grande valeur absolue des scores $t_1$ des sept objets d'origine | un nombre (4 décimales) |
| g | vrai ou faux : $\mathbf{r}_3$ est signalé | `True` ou `False` |

Dans ta copie : chaque mesure de $\mathbf{r}_2$ est dans la plage des sept objets ; qu'a-t-il donc d'inhabituel ? Pourquoi $\mathbf{r}_3$ n'est-il pas signalé, alors qu'il est loin de tous les autres ? Propose un second score, calculé sur les scores $t_1$ et $t_2$, qui le signalerait. Pourquoi faudrait-il fixer le seuil sur des données que l'ACP n'a pas vues ?

### Ex M12d.21 — Pont : un changement d'unités diagonal D change Σ en DΣD, et les axes principaux avec ; la standardisation non 🔗 ★★ ⏱️ 15 min
**Objectif :** calculer l'effet d'un changement d'unités sur la covariance et les axes principaux, et vérifier que la matrice de corrélation, elle, n'en dépend pas.
**Prérequis :** fiche §6 ; M12c §8 ; Ex M12d.8 · **Parcours :** C

Un changement d'unités multiplie chaque feature $j$ par un nombre $d_j > 0$ : les données deviennent $\mathbf{X}\mathbf{D}$, avec $\mathbf{D} = \operatorname{diag}(d_1, \ldots, d_p)$, et la covariance $\boldsymbol{\Sigma}$ (notée $\mathbf{C}$ dans la fiche) devient $\mathbf{D}\boldsymbol{\Sigma}\mathbf{D}$. Dans le nuage de M12d.8, on exprime la troisième mesure dans une unité trois fois plus petite : ses valeurs sont multipliées par 3.

| | Question | Réponse attendue |
|---|---|---|
| a | la nouvelle matrice de covariance $\mathbf{D}\boldsymbol{\Sigma}\mathbf{D}$ | une matrice |
| b | ses variances le long des axes | une liste de 3 nombres (4 décimales) |
| c | son premier axe principal | une liste de 3 nombres (4 décimales) |
| d | la part de variance expliquée par ce premier axe | un nombre (4 décimales) |
| e | la corrélation des mesures 1 et 3, avant le changement | un nombre (4 décimales) |
| f | l'angle entre le premier axe de M12d.8 et celui de c), en degrés | un nombre (1 décimale) |
| g | la matrice de covariance des données standardisées (après le changement) | une matrice (4 décimales) |
| h | vrai ou faux : pour toute matrice diagonale $\mathbf{D}$ à éléments strictement positifs, la covariance des données standardisées est la même pour $\mathbf{X}$ et pour $\mathbf{X}\mathbf{D}$ | `True` ou `False` |

Dans ta copie : calcule la corrélation des mesures 1 et 3 après le changement. Montre que $(\mathbf{D}\boldsymbol{\Sigma}\mathbf{D})_{ij} = d_id_j\Sigma_{ij}$, puis que la corrélation $\Sigma_{ij}/\sqrt{\Sigma_{ii}\Sigma_{jj}}$ ne change pas : c'est h) en général. Compare c) au premier axe de M12d.8 : qui a « décidé » de la direction ?

### Ex M12d.22 — MML §4.5 à §4.7 : SVD, approximation de rang faible, phylogénie des matrices 📖 ★★ ⏱️ 45 min
**Objectif :** lire en anglais la SVD, sa géométrie, sa construction et l'approximation de rang faible, et situer les décompositions de M12a à M12d.
**Prérequis :** fiche §1 à §4 · **Parcours :** C

Lis MML §4.5, §4.6 et §4.7. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Au §4.5, comment le livre énonce-t-il le théorème de la SVD ? Quelles notations utilise-t-il pour la matrice des valeurs singulières, et quelle forme lui donne-t-il quand la matrice n'est pas carrée ? Relie-les à la fiche (📐 Notations).
2. Comment le livre décrit-il l'intuition géométrique (changement de base, mise à l'échelle, changement de base) ? Refais son raisonnement avec la matrice de M12d.3.
3. Comment construit-il la SVD ? Quelle matrice diagonalise-t-il d'abord, et comment obtient-il les vecteurs singuliers à gauche ? Compare avec la recette de la fiche §1.
4. Quelles différences entre décomposition en éléments propres et SVD le livre relève-t-il ? Note-en au moins trois.
5. Le livre illustre la SVD sur des notes de films données par quelques personnes : que représentent, dans son interprétation, les vecteurs singuliers à gauche, à droite, et les valeurs singulières ? Refais l'interprétation avec la matrice de M12d.4.
6. Au §4.6, comment le livre définit-il la norme spectrale, et comment énonce-t-il le théorème d'Eckart-Young ? Quelle norme utilise-t-il, et que dit la fiche §3 pour l'autre ?
7. Au §4.7, parcours l'arbre des familles de matrices. Place-y les matrices rencontrées de M12a à M12d (inversibles, symétriques, définies positives, orthogonales, diagonalisables) et les décompositions vues (Cholesky, décomposition spectrale, SVD).
8. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12d.23 — MML §10.1 à §10.6 : l'ACP du livre (la dérivation par Lagrange de §10.2 se survole : M13b la relit) 📖 ★★ ⏱️ 50 min
**Objectif :** lire en anglais l'ACP du livre sous ses deux points de vue (variance maximale, projection), en grande dimension et en pratique, et traduire ses notations.
**Prérequis :** fiche §5 à §7 · **Parcours :** C

Lis MML §10.1 à §10.6 ; au §10.2, survole la dérivation par les multiplicateurs de Lagrange (M13b la relira). Réponds dans ta copie, avec tes mots.
1. Au §10.1, quel problème le livre pose-t-il ? Comment range-t-il les données ($\mathbf{X}$ de forme $D \times N$), avec quelle normalisation pour la covariance, et comment traduis-tu ses formules dans les conventions de la fiche ($n$ exemples en lignes, $\frac{1}{n-1}$) ?
2. Au §10.2, quel est le point de vue de la variance maximale ? Quelle équation la dérivation obtient-elle à la fin, et quel résultat de la fiche (§5) donne la même conclusion sans multiplicateur ?
3. Comment le livre obtient-il les axes suivants (le deuxième, puis le $m$-ième) ? Compare avec la fiche §5.
4. Au §10.3, quel est le point de vue de la projection ? Quelle erreur minimise-t-on, et quel résultat retrouve-t-on sur les variances oubliées (relie-le à M12d.18) ?
5. Au §10.4, comment le livre relie-t-il l'ACP à la SVD de la matrice des données et à l'approximation de rang faible (§4.6) ?
6. Au §10.5, comment le livre traite-t-il le cas où il y a moins d'exemples que de dimensions ? Relie-le à M12d.12.
7. Au §10.6, quelles étapes pratiques le livre énumère-t-il ? Compare-les à la fiche §6, en particulier sur la standardisation.
8. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12d.24 — Fermi : la mémoire et le temps d'une ACP sur un million de clients et 250 features 🧮 ★ ⏱️ 10 min
**Objectif :** estimer la mémoire et le temps des étapes d'une ACP sur de grandes données, et repérer l'étape qui coûte.
**Prérequis :** fiche §6 et §7 · **Parcours :** C

Ordres de grandeur seulement. Un tableau de $n = 10^6$ clients et $p = 250$ features, en `float64` (8 octets par nombre) ; une machine fait environ $10^{10}$ opérations par seconde sur des produits de matrices.
1. La mémoire du tableau ? En `float32` ?
2. Former $\mathbf{X}_c^\top\mathbf{X}_c$ demande environ $np^2$ multiplications-additions. Combien, et combien de temps ?
3. La mémoire de la matrice de covariance, et le coût de sa diagonalisation (de l'ordre de $10\,p^3$ opérations) ?
4. La SVD compacte de $\mathbf{X}_c$ coûte quelques $np^2$ : pourquoi la préférer quand même à la covariance (fiche §4 et §6) ?
5. La mémoire des scores avec $k = 20$ composantes ?
6. Si le tableau ne tient pas en mémoire, comment calculer $\boldsymbol{\mu}$ et $\mathbf{C}$ en le lisant par morceaux de $10^4$ lignes ?

### Ex M12d.25 — Expliquer la SVD comme « rotation, étirement, rotation » 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer en mots, sans formule, ce que fait une matrice d'après sa SVD.
**Prérequis :** fiche §2 · **Parcours :** C, E

Une amie graphiste, qui n'a jamais fait d'algèbre linéaire, te demande ce que veut dire « toute matrice est une rotation, un étirement et une rotation ». Explique-lui, **en huit lignes au plus**, sans formule, avec une image concrète (un dessin sur une feuille de caoutchouc, un logo qu'on déforme…) : ce que fait chacune des trois étapes, ce que deviennent un cercle et ses deux diamètres privilégiés, ce que mesurent les valeurs singulières, et ce qui se passe quand l'une d'elles est nulle.

<a id="entretien"></a>

## 💼 Entretien

### M12d.E1 — « Comment choisissez-vous le nombre de composantes d'une ACP ? » 💼 ★ ⏱️ 10 min
*Fiche §7 · parcours C*

« Comment choisissez-vous le nombre de composantes d'une ACP ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire ce que mesure la variance expliquée, citer au moins deux critères (un seuil sur la part cumulée, le coude) et leurs limites, dire ce que l'on fait quand l'ACP prépare un modèle (choisir $k$ en validation), rappeler qu'on calcule les axes sur l'entraînement seulement, et dire un mot de l'erreur de reconstruction. Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M12d.E2 — « Que dit le conditionnement d'une matrice ? » 💼 ★ ⏱️ 10 min
*Fiche §4 · parcours C*

« Que dit le conditionnement d'une matrice ? »

Prépare une réponse orale de **60 secondes**. Elle doit donner la définition (par les valeurs singulières), dire ce que l'on perd en chiffres significatifs, expliquer pourquoi le déterminant ne le mesure pas, citer le piège des équations normales ($\kappa^2$), et un exemple en machine learning (des features presque redondantes, la régularisation ridge, la vitesse d'une descente de gradient). Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m12d_svd_acp/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M12d.26 | La SVD par les valeurs propres de AᵀA · `svd` | 🔨 | ★★ | 40 | C, E |
| M12d.27 | Approximation de rang faible et conditionnement · `low_rank_approximation, condition_number` | 🔨 | ★ | 20 | C, E |
| M12d.28 | La pseudo-inverse · `pinv` | 🔨 | ★ | 15 | C |
| M12d.29 | Les axes principaux d'une matrice de covariance, et la variance expliquée · `principal_axes, explained_variance_ratio` | 🔨 | ★★ | 25 | C, E |
| M12d.30 | `np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA` contre tes fonctions : les signes | 📦 | ★ | 15 | C, E |
| M12d.31 | Prédire l'allure des valeurs singulières d'une image, et le rang qui suffit | 🔮 | ★ | 10 | C, E |
| M12d.32 | Compresser une image du domaine public : l'erreur en fonction du rang | 🔬 | ★★ | 20 | C |
| M12d.33 | La SVD par AᵀA contre `np.linalg.svd` : ce qu'on perd quand κ est grand | 🔬 | ★★ | 20 | C |
| M12d.34 | La SVD en images : Vᵀ, Σ puis U appliqués au cercle unité, étape par étape | 🎨 | ★ | 20 | C, E |
| M12d.35 | Chasse à l'erreur : une ACP sans centrer, n et n − 1 mélangés, des axes lus en lignes au lieu de colonnes | 🐛 | ★ | 15 | C |
| M12d.36 | Un test : la reconstruction de rang plein redonne X, et l'erreur décroît avec k | 🛠️ | ★ | 15 | C |
| M12d.37 | Défi : compresser une image centrée en gardant 93,5 % de son énergie avec au plus 5 % des nombres | 🏆 | ★★★ | 30 | C |
