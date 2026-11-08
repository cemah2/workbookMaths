# M09b · Moindres carrés et régularisation — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m09b_moindres_carres/06_mes_reponses.md` (créée par `python tools/start_chapter.py M09b`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : $\mathbf{X}$ a la forme $(n, p)$, une ligne par exemple et une colonne par feature ; $\mathbf{y}$ contient les $n$ cibles, $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w}$ les prédictions et $\mathbf{r} = \mathbf{y} - \hat{\mathbf{y}}$ les résidus ; $\mathrm{SCT}$, $\mathrm{SCE}$ et $\mathrm{SCR}$ sont les sommes de carrés totale, expliquée et résiduelle (fiche §1). « Avec ordonnée à l'origine » veut dire que la première colonne de $\mathbf{X}$ ne contient que des 1.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M09b.Q1 — MSE, RMSE, MAE, R² : ce que mesure chacune 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Une régression prédit des masses en kilogrammes.
1. Dans quelle unité s'expriment la MSE, la RMSE et la MAE ?
2. On exprime cibles et prédictions en grammes (tout est multiplié par 1 000). Par combien sont multipliées la MSE, la MAE et le $R^2$ ?
3. Laquelle, de la MSE et de la MAE, un seul point très mal prédit fait-il le plus monter ?
4. Vrai ou faux : on a toujours $\mathrm{RMSE} \ge \mathrm{MAE}$.
5. Un modèle obtenu par moindres carrés, avec ordonnée à l'origine, a $R^2 = 0$ sur ses données d'entraînement. Que prédit-il ?
6. Vrai ou faux : un $R^2$ calculé sur des données de test peut être négatif.

### M09b.Q2 — Gradients matriciels : associer chaque fonction à son gradient 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Associe chaque fonction de $\mathbf{w} \in \mathbb{R}^p$ (de 1 à 6) à son gradient (de a à f) ; $\mathbf{a}$, $\mathbf{y}$, $\mathbf{X}$, $\lambda$ sont fixés, $\mathbf{A}$ est carrée et $\mathbf{S}$ est symétrique.

| Fonction | | Gradient |
|---|---|---|
| 1. $\mathbf{a}^\top\mathbf{w}$ | | a. $2\mathbf{S}\mathbf{w}$ |
| 2. $\mathbf{w}^\top\mathbf{w}$ | | b. $-2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ |
| 3. $\mathbf{w}^\top\mathbf{S}\mathbf{w}$ | | c. $\mathbf{a}$ |
| 4. $\mathbf{w}^\top\mathbf{A}\mathbf{w}$ | | d. $2\lambda\mathbf{w}$ |
| 5. $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ | | e. $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ |
| 6. $\lambda\lVert \mathbf{w} \rVert^2$ | | f. $2\mathbf{w}$ |

Puis : 7. $\mathbf{X}$ a la forme $(200, 6)$ ; combien de coordonnées a le gradient de la fonction 5 ? 8. Que vaut ce gradient au minimum ?

### M09b.Q3 — Équations normales : quand la solution est-elle unique ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Combien de solutions ont les équations normales $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$ (une, ou une infinité) quand :
1. $\mathbf{X}$ a la forme $(50, 4)$ et des colonnes indépendantes ?
2. $\mathbf{X}$ a la forme $(3, 5)$ ?
3. une colonne de $\mathbf{X}$ est le triple d'une autre ?
4. $\mathbf{X}$ a une colonne de 1 et les trois colonnes du one-hot complet d'une feature à trois catégories ?
5. Quand il y en a une infinité, donnent-elles toutes les mêmes prédictions $\mathbf{X}\mathbf{w}$ ?
6. Vrai ou faux : les équations normales ont toujours au moins une solution, quels que soient $\mathbf{X}$ et $\mathbf{y}$.

### M09b.Q4 — Linéaire en x ou linéaire en w ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Lesquels de ces modèles sont linéaires **en leurs poids** $w_0, w_1, w_2$, et s'ajustent donc par les équations normales ?
1. $\hat{y} = w_0 + w_1x + w_2x^2$
2. $\hat{y} = w_0 + w_1\sin x + w_2\cos x$
3. $\hat{y} = w_0 + e^{w_1x}$
4. $\hat{y} = w_1x_1x_2 + w_2\ln x_3$
5. $\hat{y} = w_0 + \frac{w_1x}{1 + w_2x}$
6. $\hat{y} = (w_0 + w_1x)^2$

### M09b.Q5 — Ridge : vrai ou faux sur la pénalité L2 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Pour $\lambda > 0$, le problème ridge a toujours une solution unique.
2. Quand $\lambda \to +\infty$, tous les poids tendent vers 0.
3. Pour $\lambda$ assez grand, ridge met des poids exactement à 0.
4. La somme des carrés des résidus d'entraînement de ridge est au moins celle des moindres carrés.
5. Mesurer une feature en kilomètres plutôt qu'en mètres ne change pas les prédictions de ridge.
6. Avec la pénalité L2, un pas de descente de gradient commence par multiplier les poids par $1 - 2\eta\lambda$.

### M09b.Q6 — Lasso ou ridge : qui annule des poids ? 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

1. Laquelle des deux pénalités peut donner des poids exactement nuls ?
2. Quelle est la pente de $w \mapsto w^2$ en $w = 0$ ? Et celle de $w \mapsto |w|$, juste à droite de 0 ?
3. Laquelle des deux a une solution en formule close ?
4. Le seuillage doux : $S(3 ;\ 1)$ ? $S(-0{,}4 ;\ 0{,}5)$ ?
5. Avec le lasso, un poids nul reste nul si la pente avec laquelle la somme des carrés descend dans sa direction est plus petite que quoi ?
6. Combien de « coins » a la boule unité de la norme L1 dans $\mathbb{R}^2$ ? Où sont-ils ?

### M09b.Q7 — Bruit gaussien et moindres carrés 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

On suppose $y_i = \mathbf{x}_i \cdot \mathbf{w} + \varepsilon_i$, avec des bruits indépendants.
1. Pour quelle loi du bruit le maximum de vraisemblance donne-t-il exactement les moindres carrés ?
2. Et pour quelle loi donne-t-il la somme des valeurs absolues des résidus ?
3. L'estimateur du maximum de vraisemblance de $\sigma^2$, en fonction de $\mathrm{SCR}$ et de $n$ ?
4. Vrai ou faux : la valeur de $\sigma^2$ change les poids $\hat{\mathbf{w}}$ du maximum de vraisemblance.
5. Pourquoi $\frac{\mathrm{SCR}}{n}$ sous-estime-t-il $\sigma^2$, en moyenne ?
6. Par quoi divise-t-on $\mathrm{SCR}$ pour un estimateur sans biais ?

### M09b.Q8 — Biais, variance, bruit : ce qui change quand le modèle se complique 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

On ajuste des polynômes de degré croissant à des datasets de même taille, tirés au hasard. Que deviennent en général, quand le degré augmente :
1. le biais² ?
2. la variance ?
3. le terme de bruit $\sigma^2$ ?
4. l'erreur d'entraînement ?
5. Et quand on augmente le $\lambda$ de ridge, à degré fixé : le biais² et la variance ?
6. Un modèle peut-il avoir une erreur attendue sur de nouvelles mesures plus petite que $\sigma^2$ ?

<a id="rappels"></a>

## 🔁 Rappels

### M09b.R1 — Le pivot de Gauss et l'inverse (M09a) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Résous $\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}\mathbf{x} = \begin{pmatrix} 7 \\ 4 \end{pmatrix}$.
2. Donne l'inverse de $\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$.
3. Pour résoudre ce système, vaut-il mieux calculer l'inverse ou faire le pivot de Gauss ? Pourquoi, en une phrase ?
4. Une matrice carrée dont une colonne est la somme de deux autres est-elle inversible ?
5. Le rang de $\begin{pmatrix} 1 & -2 \\ 3 & -6 \\ -2 & 4 \end{pmatrix}$ ?

### M09b.R2 — Maximum de vraisemblance et MAP (M04) 🔁 ★ ⏱️ 5 min
*Fiche §5 et §7 · parcours C, E*

Une pièce donne 13 piles sur 20 lancers.
1. L'estimation du maximum de vraisemblance de la probabilité $\theta$ de pile ?
2. Avec un prior $\mathrm{Beta}(3, 3)$, l'estimation MAP ?
3. Pourquoi maximise-t-on le **log** de la vraisemblance plutôt que la vraisemblance ?
4. Quand le nombre de lancers devient très grand, que devient l'écart entre l'estimation MAP et celle du maximum de vraisemblance ?
5. Dans quel sens le prior de la question 2 a-t-il déplacé l'estimation, et pourquoi ?

### M09b.R3 — Gradient et point critique (M05b) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

$f(x, y) = x^2 + 3y^2 - 2xy - 4x$.
1. Le gradient $\nabla f(x, y)$ ?
2. Le point critique ?
3. La valeur de $f$ en ce point ?
4. Dans quelle direction $f$ descend-elle le plus vite en $(0, 0)$ ?
5. Vérifie que $f(x, y) = (x - y - 2)^2 + 2(y - 1)^2 - 6$, et déduis-en la nature du point critique.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"7/9"` ;
- une liste entre crochets pour un vecteur ou une forme, comme `[2, -1, 0]` ; une matrice comme une liste de lignes, `[[1, 0], [-2, 3]]` ; vrai ou faux par `True` ou `False` ; une ou plusieurs lettres entre guillemets, comme `"AC"`.

### Ex M09b.1 — MSE, RMSE, MAE et loss de Huber de quatre résidus ✏️ ★ ⏱️ 15 min
**Objectif :** calculer les mesures d'erreur d'une régression, et voir comment chacune traite un grand résidu.
**Prérequis :** fiche §1 · **Parcours :** C, E

Un modèle prédit la durée (en minutes) de quatre trajets. Les durées réelles sont $\mathbf{y} = (12, 7, 9, 15)$ et les prédictions $\hat{\mathbf{y}} = (10, 8, 9{,}5, 11)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les résidus $r_i = y_i - \hat{y}_i$ | une liste de 4 nombres |
| b | la MSE | un nombre (4 décimales) |
| c | la RMSE | un nombre (4 décimales) |
| d | la MAE | un nombre (3 décimales) |
| e | la loss de Huber moyenne avec $\delta = 1$ | un nombre (5 décimales) |
| f | la loss de Huber moyenne avec $\delta = 5$ | un nombre (5 décimales) |
| g | la MSE du modèle constant qui prédit toujours la moyenne $\bar{y}$ des durées réelles | un nombre (4 décimales) |

Dans ta copie : dans quelle unité s'exprime chaque résultat ? Pourquoi f) vaut-il exactement la moitié de b) ? Quel $R^2$ déduis-tu de b) et de g) ?

### Ex M09b.2 — La décomposition SCT = SCE + SCR et le R² d'un ajustement donné ✏️ ★ ⏱️ 20 min
**Objectif :** calculer les trois sommes de carrés d'un ajustement, vérifier la décomposition, et voir qu'elle tombe en défaut pour une droite qui ne vient pas des moindres carrés.
**Prérequis :** fiche §1 et §3 · **Parcours :** C

Cinq points : $x = 0, 1, 2, 3, 4$ et $y = 2, 2, 5, 4, 7$. La droite des moindres carrés (avec ordonnée à l'origine) est $\hat{y} = 1{,}6 + 1{,}2x$ ; un collègue propose aussi, à main levée, la droite $\hat{y} = 2 + x$.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne $\bar{y}$ | un nombre |
| b | $\mathrm{SCT}$ | un nombre |
| c | $\mathrm{SCR}$ de la droite des moindres carrés | un nombre (2 décimales) |
| d | $\mathrm{SCE}$ de la droite des moindres carrés | un nombre (2 décimales) |
| e | le $R^2$ de la droite des moindres carrés | un nombre (2 décimales) |
| f | $\mathrm{SCR}$ et $\mathrm{SCE}$ de la droite $\hat{y} = 2 + x$ | une liste de 2 nombres |
| g | le $R^2 = 1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$ de la droite $\hat{y} = 2 + x$ | une fraction irréductible |

Dans ta copie : vérifie que $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$ pour la première droite, et pas pour la seconde. Pour chaque droite, calcule $\sum_i r_i$ et $\sum_i x_ir_i$ : laquelle des deux conditions d'orthogonalité de la fiche §3 manque à la seconde droite ? Pour la seconde droite, compare $1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$ et $\frac{\mathrm{SCE}}{\mathrm{SCT}}$.

### Ex M09b.3 — Les gradients de aᵀw, wᵀAw et ‖y − Xw‖², composante par composante en dimension 2 ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer trois gradients en dérivant coordonnée par coordonnée, et vérifier les trois identités de la fiche.
**Prérequis :** fiche §2 ; M05b (dérivées partielles) · **Parcours :** C, E

$$\mathbf{a} = (4, -3), \qquad \mathbf{A} = \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix}, \qquad \mathbf{X} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 1 & -1 \end{pmatrix}, \qquad \mathbf{y} = (3, 1, 2), \qquad \mathbf{w} = (2, -1).$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{a}^\top\mathbf{w}$ | un nombre |
| b | le gradient de $\mathbf{w} \mapsto \mathbf{a}^\top\mathbf{w}$ en $\mathbf{w}$ | une liste de 2 nombres |
| c | $\mathbf{w}^\top\mathbf{A}\mathbf{w}$ | un nombre |
| d | le gradient de $\mathbf{w} \mapsto \mathbf{w}^\top\mathbf{A}\mathbf{w}$ en $\mathbf{w}$ | une liste de 2 nombres |
| e | les résidus $\mathbf{r} = \mathbf{y} - \mathbf{X}\mathbf{w}$ | une liste de 3 nombres |
| f | $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ | un nombre |
| g | le gradient de $\mathbf{w} \mapsto \lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ en $\mathbf{w}$ | une liste de 2 nombres |

Dans ta copie : développe $\mathbf{w}^\top\mathbf{A}\mathbf{w}$ en un polynôme de $w_1$ et $w_2$, et calcule d) par les dérivées partielles ; compare avec $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ et avec $2\mathbf{A}\mathbf{w}$. Pour g), écris $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ comme une somme de trois carrés et dérive-la par rapport à $w_1$.

### Ex M09b.4 — Les équations normales d'un modèle à deux features, sans ordonnée à l'origine ✏️ ★★ ⏱️ 20 min
**Objectif :** former et résoudre les équations normales, puis vérifier que les résidus sont orthogonaux aux colonnes.
**Prérequis :** fiche §3 ; M09a (inverse d'une matrice 2 × 2) · **Parcours :** C, E

Un modèle sans ordonnée à l'origine, $\hat{y} = w_1x_1 + w_2x_2$, sur quatre exemples :

$$\mathbf{X} = \begin{pmatrix} 1 & 2 \\ 2 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \mathbf{y} = (3, 4, 1, 1).$$

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{X}^\top\mathbf{X}$ | une liste de 2 entiers |
| b | $\mathbf{X}^\top\mathbf{X}$ | une matrice |
| c | $\mathbf{X}^\top\mathbf{y}$ | une liste de 2 nombres |
| d | la solution $\mathbf{w}$ des équations normales | une liste de 2 nombres (2 décimales) |
| e | les résidus $\mathbf{r}$ | une liste de 4 nombres (2 décimales) |
| f | $\mathbf{X}^\top\mathbf{r}$ | une liste de 2 nombres (2 décimales) |
| g | $\mathrm{SCR}$ | un nombre (2 décimales) |

Dans ta copie : que veut dire f) géométriquement ? La somme des résidus est-elle nulle ici ? Pourquoi ce n'est pas garanti ?

### Ex M09b.5 — La colonne de 1 : l'ordonnée à l'origine et des résidus de moyenne nulle ✏️ ★★ ⏱️ 20 min
**Objectif :** ajuster une droite avec ordonnée à l'origine par les équations normales, vérifier les conséquences de la colonne de 1, et voir ce que change le centrage.
**Prérequis :** fiche §3 · **Parcours :** C, E

Quatre points : $x = 1, 2, 3, 6$ et $y = 0, 3, 5, 8$. On ajuste $\hat{y} = w_0 + w_1x$ ; la première colonne de $\mathbf{X}$ contient des 1, la seconde les $x$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{X}^\top\mathbf{X}$ | une matrice |
| b | $\mathbf{X}^\top\mathbf{y}$ | une liste de 2 nombres |
| c | $\mathbf{w} = (w_0 ;\ w_1)$ | une liste de 2 nombres (2 décimales) |
| d | les résidus | une liste de 4 nombres (2 décimales) |
| e | la moyenne des prédictions $\hat{y}_i$ | un nombre (2 décimales) |
| f | le point moyen $(\bar{x}, \bar{y})$ | une liste de 2 nombres |
| g | les poids $(w_0 ;\ w_1)$ quand on remplace $x$ par $x - \bar{x}$ | une liste de 2 nombres (2 décimales) |

Dans ta copie : vérifie que la droite de c) passe par le point de f). Écris $\mathbf{X}^\top\mathbf{X}$ après centrage : pourquoi est-elle diagonale ? Quelle équation donne alors directement $w_0$ ?

### Ex M09b.6 — La matrice chapeau d'un petit tableau : H² = H et sa trace ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une matrice chapeau à la main et vérifier ses propriétés de projection.
**Prérequis :** fiche §3 ; M09a (inverse d'une matrice 2 × 2) · **Parcours :** C

Trois points d'abscisses $x = 0, 1, 3$ ; on ajuste une droite avec ordonnée à l'origine, donc $\mathbf{X} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 3 \end{pmatrix}$, et $\mathbf{y} = (2, 1, 5)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{X}^\top\mathbf{X}$ | une matrice |
| b | $14\,(\mathbf{X}^\top\mathbf{X})^{-1}$ (des entiers) | une matrice |
| c | $14\,\mathbf{H}$, avec $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$ (des entiers) | une matrice |
| d | la trace de $\mathbf{H}$ | un nombre |
| e | le numéro (de 1 à 3) du point de plus grand levier $h_{ii}$ | un entier |
| f | $7\,\hat{\mathbf{y}}$, avec $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$ (des entiers) | une liste de 3 nombres |
| g | vrai ou faux : $\mathbf{H}\mathbf{H} = \mathbf{H}$ | `True` ou `False` |

Dans ta copie : vérifie g) en calculant au moins une ligne de $\mathbf{H}\mathbf{H}$. Pourquoi le point de e) est-il celui-là ? Vérifie que $\mathbf{H}$ laisse inchangés la colonne de 1 et le vecteur $(0, 1, 3)$ : pourquoi ?

### Ex M09b.7 — Compter les monômes des features polynomiales ✏️ ★ ⏱️ 15 min
**Objectif :** compter les colonnes des features polynomiales par les combinaisons avec répétition, et voir leur nombre exploser.
**Prérequis :** fiche §4 ; R8 (combinaisons) · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de monômes de degré **exactement** 3 en deux variables $u, v$ | un entier |
| b | le nombre de monômes de degré au plus 3 en deux variables, constante comprise | un entier |
| c | le nombre de colonnes des features polynomiales de degré 2 de 5 variables, sans la constante | un entier |
| d | le nombre de colonnes des features polynomiales de degré 4 de 3 variables, sans la constante | un entier |
| e | le nombre de monômes de degré exactement 2 en 6 variables | un entier |
| f | parmi eux, le nombre de produits de deux variables **différentes** (les interactions) | un entier |
| g | le plus petit degré $d$ pour lequel les features polynomiales de 7 variables (sans constante) ont plus de 1 000 colonnes | un entier |

Dans ta copie : écris la liste des monômes de a). Pour e), vérifie que les carrés et les interactions font bien le total. Pour g), écris le nombre de colonnes pour chaque degré jusqu'à la réponse.

### Ex M09b.8 — Ridge en dimension 2 : résoudre (XᵀX + λI)w = Xᵀy pour trois valeurs de λ ✏️ ★★ ⏱️ 20 min
**Objectif :** résoudre un problème ridge à la main, et suivre la taille des poids et l'erreur d'entraînement quand $\lambda$ grandit.
**Prérequis :** fiche §5 ; M09a (inverse d'une matrice 2 × 2) · **Parcours :** C, E

$$\mathbf{X} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \mathbf{y} = (2, 1, -2).$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{X}^\top\mathbf{X}$ et $\mathbf{X}^\top\mathbf{y}$, côte à côte : la matrice $(\mathbf{X}^\top\mathbf{X} \mid \mathbf{X}^\top\mathbf{y})$ | une matrice |
| b | $\mathbf{w}$ pour $\lambda = 0$ (les moindres carrés) | une liste de 2 nombres |
| c | $\mathbf{w}$ pour $\lambda = 1$ | une liste de 2 nombres (3 décimales) |
| d | $\mathbf{w}$ pour $\lambda = 2$ | une liste de 2 nombres (2 décimales) |
| e | $\lVert \mathbf{w} \rVert$ pour $\lambda = 0$, $1$ et $2$ | une liste de 3 nombres (4 décimales) |
| f | $\mathrm{SCR}$ pour $\lambda = 0$ et pour $\lambda = 2$ | une liste de 2 nombres (2 décimales) |
| g | la limite de $\mathbf{w}$ quand $\lambda \to +\infty$ | une liste de 2 nombres |

Dans ta copie : quelle est la limite de $\lambda\,\mathbf{w}$ quand $\lambda \to +\infty$ ? Pourquoi f) augmente-t-il avec $\lambda$, alors que ridge est « meilleur » ?

### Ex M09b.9 — Ridge comme MAP : un prior gaussien et λ = σ²/τ² ✏️ ★★ ⏱️ 20 min
**Objectif :** traduire un bruit et un prior gaussiens en une pénalité ridge, et calculer l'estimation MAP.
**Prérequis :** fiche §5 et §7 ; M04 (MAP) · **Parcours :** C

Le modèle : $y_i = \mathbf{x}_i \cdot \mathbf{w} + \varepsilon_i$, avec $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$, et un prior $w_j \sim \mathcal{N}(0, \tau^2)$, tous indépendants. Pour c) à e), le dataset est

$$\mathbf{X} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \mathbf{y} = (2, 1, 1).$$

| | Question | Réponse attendue |
|---|---|---|
| a | le $\lambda$ de ridge qui correspond à $\sigma = 2$ et $\tau = 0{,}5$ | un nombre |
| b | le $\lambda$ qui correspond à $\sigma = 1$ et $\tau^2 = 0{,}5$ | un nombre |
| c | l'estimation MAP de $\mathbf{w}$, avec $\sigma = 1$ et $\tau^2 = 0{,}5$ | une liste de 2 nombres (4 décimales) |
| d | l'estimation du maximum de vraisemblance de $\mathbf{w}$ (sans prior) | une liste de 2 nombres (4 décimales) |
| e | le $\lambda$ quand le bruit passe à $\sigma = 2$, avec le même prior que c) | un nombre |
| f | l'écart-type $\tau$ du prior qui donne $\lambda = 2{,}5$ quand $\sigma = 1$ | un nombre (4 décimales) |
| g | vrai ou faux : multiplier $\sigma$ et $\tau$ par 10 ne change pas l'estimation MAP | `True` ou `False` |

Dans ta copie : écris le log du posterior de c) à une constante près, et montre qu'il est maximal au point de c). Quand $\tau \to +\infty$, que devient le prior, et que retrouve-t-on ?

### Ex M09b.10 — Les pénalités L1 et L2 de trois vecteurs de poids, et leurs boules ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des pénalités L1 et L2, et lire les boules des deux normes.
**Prérequis :** fiche §6 ; M07 (normes) · **Parcours :** C

Trois vecteurs de poids : $\mathbf{u} = (3, 0, 0)$, $\mathbf{v} = (1, 1, 1)$ et $\mathbf{t} = (2, -1, 0)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert \mathbf{u} \rVert_1$, $\lVert \mathbf{v} \rVert_1$ et $\lVert \mathbf{t} \rVert_1$ | une liste de 3 nombres |
| b | $\lVert \mathbf{u} \rVert^2$, $\lVert \mathbf{v} \rVert^2$ et $\lVert \mathbf{t} \rVert^2$ | une liste de 3 nombres |
| c | la lettre du vecteur de plus petite pénalité L2 : `"u"`, `"v"` ou `"t"` | une lettre |
| d | parmi A $(0{,}5 ;\ 0{,}5)$, B $(1 ;\ 0)$, C $(0{,}6 ;\ 0{,}6)$ et D $(-0{,}25 ;\ 0{,}75)$, les points du bord de la boule unité L1 de $\mathbb{R}^2$ (où $\lVert \mathbf{w} \rVert_1 = 1$) | des lettres |
| e | sur ce bord, la plus grande et la plus petite valeur de $\lVert \mathbf{w} \rVert$ | une liste de 2 nombres (4 décimales) |
| f | le nombre de coins de la boule unité L1 de $\mathbb{R}^3$ | un entier |
| g | les pénalités $0{,}1\,\lVert \mathbf{w} \rVert_1$ et $0{,}1\,\lVert \mathbf{w} \rVert^2$ pour $\mathbf{w} = (0{,}5 ;\ -2 ;\ 0 ;\ 1{,}5)$ | une liste de 2 nombres (2 décimales) |

Dans ta copie : dessine la boule unité L1 et la boule unité L2 de $\mathbb{R}^2$ sur la même figure, et place les points de d). Où sont les points de e) ? Que disent a) et b) sur la façon dont chaque pénalité juge un poids concentré sur une feature ou réparti sur plusieurs ?

### Ex M09b.11 — La log-vraisemblance gaussienne d'un modèle linéaire et l'estimation de σ² ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une log-vraisemblance gaussienne, estimer la variance du bruit, et comparer deux droites par leur vraisemblance.
**Prérequis :** fiche §7 ; M04 (vraisemblance) ; Ex M09b.2 · **Parcours :** C

On reprend les cinq points de M09b.2, la droite des moindres carrés $\hat{y} = 1{,}6 + 1{,}2x$ (sa $\mathrm{SCR}$ est 3,6) et la droite $\hat{y} = 2 + x$, avec le modèle $y_i = w_0 + w_1x_i + \varepsilon_i$, $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$ indépendants.

| | Question | Réponse attendue |
|---|---|---|
| a | l'estimation du maximum de vraisemblance $\hat{\sigma}^2$ | un nombre (2 décimales) |
| b | l'estimation sans biais $\frac{\mathrm{SCR}}{n - p}$ | un nombre (2 décimales) |
| c | la log-vraisemblance maximale, au point $(1{,}6 ;\ 1{,}2)$ et $\sigma^2 = \hat{\sigma}^2$ (logarithme népérien) | un nombre (4 décimales) |
| d | la log-vraisemblance de la droite des moindres carrés avec $\sigma^2 = 1$ | un nombre (4 décimales) |
| e | la différence des log-vraisemblances des deux droites, avec $\sigma^2 = 1$ (la droite des moindres carrés moins l'autre) | un nombre (2 décimales) |
| f | le rapport de leurs vraisemblances, avec $\sigma^2 = 1$ | un nombre (4 décimales) |
| g | les sommes $\sum_i |r_i|$ des valeurs absolues des résidus des deux droites | une liste de 2 nombres (2 décimales) |

Dans ta copie : montre que c) vaut $-\frac{n}{2}\big(\ln(2\pi\hat{\sigma}^2) + 1\big)$. Que dit g) sur ces deux droites si le bruit suit une loi de Laplace ?

### Ex M09b.12 — L'estimateur rétréci c·x̄ : biais, variance et erreur quadratique ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer le biais, la variance et l'erreur quadratique d'un estimateur rétréci, et trouver le facteur de rétrécissement optimal.
**Prérequis :** fiche §8 ; M02c (moyenne empirique) · **Parcours :** C

On observe $n = 9$ valeurs indépendantes d'une loi de moyenne $\mu = 2$ et de variance $\sigma^2 = 9$, et l'on estime $\mu$ par $c\,\bar{x}$, avec $0 < c \le 1$.

| | Question | Réponse attendue |
|---|---|---|
| a | le biais de $c\,\bar{x}$ pour $c = 0{,}5$ | un nombre |
| b | la variance de $c\,\bar{x}$ pour $c = 0{,}5$ | un nombre (2 décimales) |
| c | l'erreur quadratique moyenne de $c\,\bar{x}$ pour $c = 0{,}5$ | un nombre (2 décimales) |
| d | l'erreur quadratique moyenne de $\bar{x}$ ($c = 1$) | un nombre |
| e | le $c$ qui minimise l'erreur quadratique moyenne | un nombre (2 décimales) |
| f | l'erreur quadratique moyenne en ce $c$ | un nombre (2 décimales) |
| g | le $c$ optimal si la moyenne était $\mu = 0{,}5$ (même $\sigma^2$, même $n$) | un nombre (2 décimales) |

Dans ta copie : écris l'erreur quadratique moyenne comme une fonction $E(c)$, dérive-la, et donne la formule du $c$ optimal en fonction de $\mu$, $\sigma^2$ et $n$. Pourquoi ne peut-on pas utiliser ce $c$ tel quel en pratique ? Que devient-il quand $n$ grandit ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M09b.13 — Le gradient de wᵀAw vaut (A + Aᵀ)w ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'identité du gradient d'une forme quadratique à partir des dérivées partielles, et en déduire les autres identités de la fiche.
**Prérequis :** fiche §2 ; M05b (dérivées partielles) ; R4 (le symbole $\sum$) · **Parcours :** C, E

Soit $\mathbf{A} = (a_{ij})$ une matrice carrée de taille $p$, et $f(\mathbf{w}) = \mathbf{w}^\top\mathbf{A}\mathbf{w}$ pour $\mathbf{w} \in \mathbb{R}^p$.
1. Écris $f(\mathbf{w})$ comme une double somme.
2. Pour un indice $k$ fixé, calcule $\frac{\partial}{\partial w_k}(w_iw_j)$ dans les quatre cas : $i = j = k$ ; $i = k \ne j$ ; $j = k \ne i$ ; $i \ne k$ et $j \ne k$.
3. Déduis-en $\frac{\partial f}{\partial w_k} = \sum_j a_{kj}w_j + \sum_i a_{ik}w_i$.
4. Reconnais dans ces deux sommes les coordonnées $k$ de $\mathbf{A}\mathbf{w}$ et de $\mathbf{A}^\top\mathbf{w}$, et conclus.
5. Déduis-en $\nabla(\mathbf{w}^\top\mathbf{S}\mathbf{w}) = 2\mathbf{S}\mathbf{w}$ pour $\mathbf{S}$ symétrique, puis $\nabla\lVert \mathbf{w} \rVert^2 = 2\mathbf{w}$.
6. Démontre de la même façon $\nabla(\mathbf{a}^\top\mathbf{w}) = \mathbf{a}$.

### Ex M09b.14 — Les équations normales en dimension n, par le gradient ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer que le minimum de $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ est atteint exactement aux solutions des équations normales, et à quelle condition il est unique.
**Prérequis :** fiche §2 et §3 ; Ex M09b.13 ; M09a (transposée d'un produit) · **Parcours :** C, E

Soit $\mathbf{X}$ de forme $(n, p)$, $\mathbf{y} \in \mathbb{R}^n$ et $L(\mathbf{w}) = \lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$.
1. Développe $L(\mathbf{w})$, en justifiant $\mathbf{w}^\top\mathbf{X}^\top\mathbf{y} = \mathbf{y}^\top\mathbf{X}\mathbf{w}$.
2. Calcule $\nabla L(\mathbf{w})$ avec M09b.13, et écris les équations d'un point critique.
3. Soit $\mathbf{w}^*$ une solution des équations normales et $\mathbf{v} \in \mathbb{R}^p$. Montre que $L(\mathbf{w}^* + \mathbf{v}) = L(\mathbf{w}^*) + \lVert \mathbf{X}\mathbf{v} \rVert^2$ (indication : $\mathbf{y} - \mathbf{X}(\mathbf{w}^* + \mathbf{v}) = \mathbf{r}^* - \mathbf{X}\mathbf{v}$, avec $\mathbf{X}^\top\mathbf{r}^* = \mathbf{0}$).
4. Déduis-en que $\mathbf{w}^*$ est un minimum global de $L$ (pas seulement un point critique).
5. Montre que, si les colonnes de $\mathbf{X}$ sont indépendantes ($\mathbf{X}\mathbf{v} = \mathbf{0} \Rightarrow \mathbf{v} = \mathbf{0}$), ce minimum est unique.
6. Sinon, montre que tous les minimums donnent les mêmes prédictions $\mathbf{X}\mathbf{w}$.

### Ex M09b.15 — Le résidu est orthogonal aux colonnes de X ; H est symétrique et idempotente ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer les propriétés de projection des moindres carrés, et en déduire la décomposition $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$.
**Prérequis :** fiche §3 ; M09a (transposée, inverse) ; M07 (Pythagore) · **Parcours :** C

$\mathbf{X}$ a la forme $(n, p)$ et des colonnes indépendantes, $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$ et $\mathbf{r} = \mathbf{y} - \hat{\mathbf{y}}$.
1. Montre que $\mathbf{X}^\top\mathbf{r} = \mathbf{0}$ : le résidu est orthogonal à chaque colonne de $\mathbf{X}$.
2. Montre que $\mathbf{H}$ est symétrique (utilise $(\mathbf{A}\mathbf{B}\mathbf{C})^\top = \mathbf{C}^\top\mathbf{B}^\top\mathbf{A}^\top$ et $(\mathbf{A}^{-1})^\top = (\mathbf{A}^\top)^{-1}$).
3. Montre que $\mathbf{H}\mathbf{H} = \mathbf{H}$, puis que $\mathbf{H}\mathbf{X} = \mathbf{X}$. Que veut dire cette dernière égalité ?
4. Montre que $\mathbf{I} - \mathbf{H}$ est symétrique et idempotente, et que $\mathbf{H}(\mathbf{I} - \mathbf{H}) = \mathbf{0}$.
5. On admet que $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$ dès que les deux produits existent. Montre que $\operatorname{tr}\mathbf{H} = p$.
6. On suppose que la première colonne de $\mathbf{X}$ ne contient que des 1. Montre que $\sum_i r_i = 0$, puis que $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$.

### Ex M09b.16 — XᵀX + λI est inversible pour tout λ > 0 ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que ridge a toujours une solution unique, et voir pourquoi la condition $\lambda > 0$ compte.
**Prérequis :** fiche §5 ; M09a (inverse, rang) ; M09b.14 · **Parcours :** C, E

Soit $\mathbf{X}$ de forme $(n, p)$, quelconque, et $\lambda > 0$.
1. Montre que $\mathbf{v}^\top\mathbf{X}^\top\mathbf{X}\mathbf{v} = \lVert \mathbf{X}\mathbf{v} \rVert^2$ pour tout $\mathbf{v} \in \mathbb{R}^p$.
2. Soit $\mathbf{v}$ tel que $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$. En multipliant à gauche par $\mathbf{v}^\top$, montre que $\mathbf{v} = \mathbf{0}$.
3. Conclus que $\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}$ est inversible (M09a : une matrice carrée dont le seul vecteur envoyé sur $\mathbf{0}$ est $\mathbf{0}$ est inversible).
4. Calcule le gradient de $L_\lambda(\mathbf{w}) = \lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 + \lambda\lVert \mathbf{w} \rVert^2$ et montre que son unique point critique est la solution de ridge.
5. Avec $\mathbf{X} = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix}$, montre que $\mathbf{X}^\top\mathbf{X}$ n'est pas inversible, et que $\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}$ l'est pour $\lambda = 1$.
6. Trouve, pour cette matrice, une valeur de $\lambda < 0$ pour laquelle $\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}$ n'est pas inversible.

### Ex M09b.17 — Un bruit gaussien mène aux moindres carrés : le maximum de vraisemblance ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que le maximum de vraisemblance d'un modèle linéaire à bruit gaussien est la solution des moindres carrés, et trouver l'estimateur de $\sigma^2$.
**Prérequis :** fiche §7 ; M02b (loi normale) ; M04 (vraisemblance) · **Parcours :** C, E

On suppose $y_i = \mathbf{x}_i \cdot \mathbf{w} + \varepsilon_i$ pour $i = 1, \ldots, n$, avec des $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$ indépendants.
1. Donne la densité de $y_i$, puis la vraisemblance $L(\mathbf{w}, \sigma^2)$ des $n$ observations.
2. Montre que $\ln L(\mathbf{w}, \sigma^2) = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2}\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$.
3. À $\sigma^2$ fixé, montre que maximiser $\ln L$ revient à minimiser $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$. Le résultat dépend-il de $\sigma^2$ ?
4. Les poids étant fixés à cette solution, dérive $\ln L$ par rapport à $s = \sigma^2$ et montre que le maximum est atteint en $\hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$.
5. Reprends 1 à 3 avec un bruit de Laplace, de densité $\frac{1}{2b}e^{-|\varepsilon|/b}$ : quelle somme faut-il minimiser ?

### Ex M09b.18 — La décomposition biais² + variance + bruit, démontrée ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer la décomposition de l'erreur quadratique d'un estimateur, puis celle de l'erreur de prédiction d'un modèle.
**Prérequis :** fiche §8 ; M02b (espérance, variance, indépendance) · **Parcours :** C

1. Soit $\hat{\theta}$ un estimateur de $\theta$. Montre que $\mathbb{E}[(\hat{\theta} - \theta)^2] = (\mathbb{E}[\hat{\theta}] - \theta)^2 + \mathbb{V}(\hat{\theta})$.
2. On suppose $y = f(x) + \varepsilon$ en un point $x$ fixé, avec $\mathbb{E}[\varepsilon] = 0$, $\mathbb{V}(\varepsilon) = \sigma^2$, et $\varepsilon$ indépendant du dataset $D$ qui a servi à apprendre $\hat{f}_D$. On note $\bar{f}(x) = \mathbb{E}_D[\hat{f}_D(x)]$. Écris $y - \hat{f}_D(x)$ comme la somme de trois termes : le bruit, l'écart du modèle moyen à $f$, l'écart de $\hat{f}_D$ au modèle moyen.
3. Développe le carré de cette somme, et montre que l'espérance de chacun des trois doubles produits est nulle (dis quelle hypothèse sert pour chacun).
4. Conclus : $\mathbb{E}[(y - \hat{f}_D(x))^2] = \text{biais}^2 + \text{variance} + \sigma^2$.
5. Applique la question 1 à l'estimateur $c\,\bar{x}$ de M09b.12, et retrouve la formule du $c$ optimal.

### Ex M09b.19 — Le nombre de monômes de degré au plus d en p variables : C(p + d, d) ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer la formule du nombre de features polynomiales, par un dénombrement d'étoiles et de barres.
**Prérequis :** fiche §4 ; R8 (combinaisons) · **Parcours :** C

1. Explique pourquoi les monômes $x_1^{k_1}\cdots x_p^{k_p}$ de degré exactement $k$ correspondent aux $p$-uplets d'entiers $(k_1, \ldots, k_p) \ge 0$ de somme $k$.
2. Représente un tel $p$-uplet par une suite de $k$ étoiles et de $p - 1$ barres (par exemple, pour $p = 3$ et $k = 4$, $\star\star|\,|\star\star$ code $(2, 0, 2)$). Montre que c'est une bijection, et déduis-en qu'il y a $\binom{k + p - 1}{k}$ monômes de degré exactement $k$.
3. Un monôme de degré **au plus** $d$ en $p$ variables correspond à un $(p+1)$-uplet $(k_0, k_1, \ldots, k_p)$ de somme exactement $d$ : lequel ? Déduis-en qu'il y en a $\binom{p + d}{d}$.
4. Vérifie la formule pour $p = 2$ et $d = 2$ en écrivant tous les monômes.
5. Déduis de 2 et 3 l'identité $\sum_{k=0}^{d}\binom{k + p - 1}{k} = \binom{p + d}{d}$.
6. Montre que, pour $d$ fixé et $p$ grand, $\binom{p + d}{d}$ est de l'ordre de $\frac{p^d}{d!}$.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09b.20 — Pont : la loss d'un modèle linéaire et son gradient pour un batch, prêts pour la descente de gradient 🔗 ★ ⏱️ 15 min
**Objectif :** calculer la MSE d'un batch et son gradient sous forme matricielle, puis faire un pas de descente de gradient.
**Prérequis :** fiche §2 ; M05b (descente de gradient) · **Parcours :** C, E

Un modèle linéaire avec ordonnée à l'origine, $\hat{y} = w_0 + w_1x_1 + w_2x_2$, reçoit un batch de quatre exemples :

$$\mathbf{X} = \begin{pmatrix} 1 & 2 & 1 \\ 1 & 0 & -1 \\ 1 & 1 & 3 \\ 1 & -1 & 0 \end{pmatrix}, \qquad \mathbf{y} = (3, 0, 1, 1), \qquad \mathbf{w} = (0{,}5 ;\ 1 ;\ -1).$$

| | Question | Réponse attendue |
|---|---|---|
| a | les prédictions $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w}$ | une liste de 4 nombres |
| b | les résidus $\mathbf{r}$ | une liste de 4 nombres |
| c | la MSE du batch | un nombre (2 décimales) |
| d | $\mathbf{X}^\top\mathbf{r}$ | une liste de 3 nombres |
| e | le gradient de la MSE en $\mathbf{w}$ | une liste de 3 nombres (2 décimales) |
| f | les poids après un pas de descente de gradient, de pas $\eta = 0{,}1$ | une liste de 3 nombres (3 décimales) |
| g | la MSE du batch avec ces nouveaux poids | un nombre (4 décimales) |

Dans ta copie : vérifie les formes de chaque étape. Combien de multiplications coûte le calcul du gradient pour un batch de $B$ exemples à $p$ colonnes ? Pourquoi divise-t-on par $n$ (ici 4) dans la MSE, et quel serait l'effet de ne pas le faire sur le choix de $\eta$ ?

### Ex M09b.21 — Pont : pourquoi standardiser les colonnes avant ridge 🔗 ★ ⏱️ 15 min
**Objectif :** mesurer, sur un exemple à colonnes orthogonales, comment l'unité d'une feature change le rétrécissement de ridge, et comment la standardisation l'égalise.
**Prérequis :** fiche §5 ; M02c (standardisation) ; Ex M09b.8 · **Parcours :** C

Deux features centrées, et des cibles centrées (pas besoin d'ordonnée à l'origine) : une distance $x_1 = (-2, -1, 1, 2)$ en **kilomètres**, une feature $x_2 = (1, -1, -1, 1)$, et $\mathbf{y} = (-3, 1, 0, 2)$. Les deux colonnes sont orthogonales, donc $\mathbf{X}^\top\mathbf{X}$ est diagonale. On appelle **facteur de rétrécissement** d'un poids le rapport du poids ridge au poids des moindres carrés.

| | Question | Réponse attendue |
|---|---|---|
| a | les poids des moindres carrés | une liste de 2 nombres (2 décimales) |
| b | les poids ridge pour $\lambda = 2$ | une liste de 2 nombres (4 décimales) |
| c | les facteurs de rétrécissement des deux poids, pour $\lambda = 2$ | une liste de 2 nombres (4 décimales) |
| d | le poids des moindres carrés de $x_1$ quand la distance est mesurée en **mètres** | un nombre (4 décimales) |
| e | le facteur de rétrécissement de ce poids pour $\lambda = 2$, en mètres | un nombre (4 décimales) |
| f | le facteur de rétrécissement de chaque poids pour $\lambda = 2$, après standardisation des deux colonnes (écart-type avec $\mathrm{ddof} = 0$) | une fraction irréductible |
| g | vrai ou faux : après standardisation, le facteur ne dépend plus de l'unité choisie pour la distance | `True` ou `False` |

Dans ta copie : montre que, pour des colonnes orthogonales, le facteur de rétrécissement du poids $j$ vaut $\frac{\lVert \mathbf{x}_j \rVert^2}{\lVert \mathbf{x}_j \rVert^2 + \lambda}$. Pourquoi une feature mesurée dans une petite unité (de grands nombres) est-elle presque épargnée par ridge ?

### Ex M09b.22 — MML §5.5, §8.1 et §8.2 : identités de gradients et minimisation du risque empirique 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la mise en place de l'apprentissage par minimisation du risque empirique, et retrouver dans la liste d'identités du livre celles de la fiche.
**Prérequis :** fiche §1 et §2 · **Parcours :** C

Lis MML §8.1 et §8.2, puis survole §5.5. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Au §8.1, quelles sont les deux façons de voir un modèle que le livre distingue ? Laquelle correspond aux §1 à §6 de la fiche, et laquelle au §7 ?
2. Au §8.2, comment le livre appelle-t-il l'ensemble des fonctions parmi lesquelles on choisit ? Quelle loss prend-il pour exemple, et comment écrit-il le risque empirique ?
3. Toujours au §8.2, quel problème la régularisation doit-elle éviter ? Quel terme le livre ajoute-t-il, et quel nom lui donne-t-il ?
4. Que propose le livre pour estimer l'erreur de généralisation, et en quoi consiste cette méthode ?
5. Au §5.5, retrouve les identités qui donnent le gradient de $\mathbf{a}^\top\mathbf{x}$ et celui de $\mathbf{x}^\top\mathbf{B}\mathbf{x}$. Sous quelle forme les écrit le livre (ligne ou colonne), et qu'est-ce qui change par rapport à la fiche ?
6. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M09b.23 — MML §9.1 et §9.2 : régression linéaire, maximum de vraisemblance et MAP 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais le traitement de la régression linéaire par le maximum de vraisemblance et le MAP, et relier ses notations à celles de la fiche.
**Prérequis :** fiche §3, §5 et §7 · **Parcours :** C

Lis MML §9.1 et §9.2. Réponds dans ta copie, **avec tes mots**.
1. Au §9.1, quel modèle probabiliste le livre pose-t-il pour les cibles ? Quels symboles utilise-t-il pour les paramètres et pour la variance du bruit ?
2. Au début du §9.2, quelle expression le livre obtient-il pour l'estimation du maximum de vraisemblance des paramètres ? Écris-la avec les notations de la fiche.
3. Comment le livre construit-il un modèle polynomial avec la même méthode ? Comment appelle-t-il la matrice $\boldsymbol{\Phi}$ ?
4. Quelle estimation de la variance du bruit le livre obtient-il ? Compare avec la fiche (§7).
5. Comment le livre met-il en évidence l'overfitting quand le degré augmente ? Quelle mesure d'erreur utilise-t-il ?
6. Comment écrit-il l'estimation MAP avec un prior gaussien, et quel lien fait-il avec la régularisation ? Écris le $\lambda$ de ridge avec ses notations.

### Ex M09b.24 — Fermi : la taille de XᵀX pour des features polynomiales de degré 3 sur 100 variables 🧮 ★ ⏱️ 10 min
**Objectif :** estimer la mémoire et le temps que demandent les équations normales quand les features polynomiales explosent.
**Prérequis :** fiche §4 ; M09a (coût d'un produit, du pivot de Gauss) · **Parcours :** C

Un dataset a $10^6$ exemples et 100 variables ; on veut une régression polynomiale de degré 3. Ordres de grandeur seulement (une puissance de 10 suffit, sauf en 1).
1. Combien de colonnes ont les features polynomiales (fiche §4) ?
2. Combien de nombres contient $\mathbf{X}^\top\mathbf{X}$ ? Quelle mémoire en `float64` (8 octets par nombre) ?
3. Combien de multiplications coûte le calcul de $\mathbf{X}^\top\mathbf{X}$ ?
4. Le pivot de Gauss d'une matrice carrée de taille $m$ coûte environ $\frac{m^3}{3}$ multiplications (M09a). Combien pour ce système ? Combien de temps à $10^{12}$ multiplications par seconde ?
5. Que pourrait-on faire à la place ? Donne deux pistes.

### Ex M09b.25 — Expliquer la matrice chapeau : ce que veut dire « projeter y » 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, sans formule, ce que fait la matrice chapeau et pourquoi les moindres carrés sont une projection.
**Prérequis :** fiche §3 · **Parcours :** C, E

Une collègue a lu que « la régression linéaire projette $\mathbf{y}$ sur l'espace des colonnes de $\mathbf{X}$ », et ne voit pas le rapport avec une droite qui passe au milieu des points. Explique-lui, **en huit lignes au plus**, sans formule : ce qu'est un vecteur de $n$ cibles, ce que sont toutes les prédictions possibles d'un modèle linéaire, pourquoi la meilleure est le pied d'une perpendiculaire, ce que fait la matrice chapeau, et pourquoi l'appliquer deux fois ne change rien.

<a id="entretien"></a>

## 💼 Entretien

### M09b.E1 — « Pourquoi ne pas inverser XᵀX, et que faire si des features sont colinéaires ? » 💼 ★ ⏱️ 10 min
*Fiche §3 et §5 · parcours C*

« Pourquoi ne pas inverser XᵀX, et que faire si des features sont colinéaires ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire ce qui coûte et ce qui est imprécis dans le calcul d'une inverse, ce qu'on fait à la place (`solve`, ou mieux `lstsq`), ce qui arrive aux équations normales quand des colonnes sont dépendantes ou presque, et deux remèdes. Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M09b.E2 — « Quel lien entre la régularisation L2 et un prior gaussien ? » 💼 ★ ⏱️ 10 min
*Fiche §5 et §7 · parcours C*

« Quel lien entre la régularisation L2 et un prior gaussien ? »

Prépare une réponse orale de **60 secondes**. Elle doit poser le modèle (bruit et prior), dire ce que maximise le MAP, montrer d'où viennent les deux termes de la loss de ridge, donner la formule de $\lambda$ et l'interpréter (ce que veut dire un $\lambda$ grand), et dire ce que donne un prior de Laplace. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m09b_moindres_carres/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M09b.26 | Équations normales et résolution, avec ou sans ridge · `normal_equations, solve_least_squares` | 🔨 | ★ | 25 | C, E |
| M09b.27 | La matrice chapeau et les trois sommes de carrés · `hat_matrix, residual_decomposition` | 🔨 | ★ | 20 | C, E |
| M09b.28 | Compter les monômes, et la loss de Huber · `count_monomials, huber_loss` | 🔨 | ★ | 15 | C |
| M09b.29 | `np.linalg.lstsq` et scikit-learn contre tes équations normales | 📦 | ★ | 15 | C, E |
| M09b.30 | Prédire : le R² d'entraînement quand on ajoute une feature de pur bruit | 🔮 | ★ | 10 | C, E |
| M09b.31 | Simuler l'estimateur rétréci c·x̄ : le c qui minimise l'erreur quadratique | 🔬 | ★★ | 20 | C |
| M09b.32 | Le conditionnement de XᵀX avec des puissances non standardisées | 🔬 | ★★ | 20 | C |
| M09b.33 | Les lignes de niveau de la loss des moindres carrés en dimension 2, et son gradient | 🎨 | ★ | 20 | C |
| M09b.34 | Chasse à l'erreur : XXᵀ au lieu de XᵀX, un gradient de mauvais signe, un R² sans centrer | 🐛 | ★ | 15 | C |
| M09b.35 | Vérifier un gradient matriciel avec SymPy et par différences finies | 🛠️ | ★ | 15 | C |
| M09b.36 | Défi : approcher une fonction par un polynôme de degré au plus 5, avec une erreur maximale sous 1e−3 | 🏆 | ★★★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
