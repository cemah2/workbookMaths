# M09b · Moindres carrés et régularisation — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M09b.Q1 — MSE, RMSE, MAE, R² : ce que mesure chacune
1. La MSE en **kilogrammes carrés** ; la RMSE et la MAE en **kilogrammes**, l'unité de la cible.
2. La MSE par $1\,000^2 = 10^6$, la MAE par $1\,000$, et le $R^2$ par 1 : c'est un rapport de deux sommes de carrés, sans unité.
3. La **MSE** : elle élève chaque résidu au carré, et un résidu dix fois plus grand y pèse cent fois plus.
4. **Vrai** : la moyenne des carrés est au moins le carré de la moyenne, donc $\mathrm{MSE} \ge \mathrm{MAE}^2$, et l'on prend la racine. L'égalité a lieu quand tous les $|r_i|$ sont égaux.
5. La moyenne $\bar{y}$ pour chaque exemple : $\mathrm{SCR} = \mathrm{SCT}$ veut dire que le meilleur modèle ne fait pas mieux que la constante $\bar{y}$, qui fait partie des modèles possibles ; la pente est nulle.
6. **Vrai** : sur de nouvelles données, rien n'empêche un modèle de faire pire que la moyenne (fiche §1, et M09b.30).

### M09b.Q2 — Gradients matriciels : associer chaque fonction à son gradient
1 → c, 2 → f, 3 → a, 4 → e, 5 → b, 6 → d (fiche §2). 7. **6** coordonnées : une par poids, comme $\mathbf{w}$ ($\mathbf{X}^\top$ est de forme $(6, 200)$). 8. Le **vecteur nul** : le minimum est un point critique, et ses coordonnées vérifient les équations normales.

### M09b.Q3 — Équations normales : quand la solution est-elle unique ?
1. **Une** : $\mathbf{X}$ est de rang 4, et $\mathbf{X}^\top\mathbf{X}$ est inversible.
2. Une **infinité** : le rang de $\mathbf{X}$ est au plus 3, pour 5 colonnes ; des colonnes combinent les autres.
3. Une **infinité** : avec $\mathbf{v}$ qui vaut 3 en position de l'une et $-1$ en position de l'autre, $\mathbf{X}\mathbf{v} = \mathbf{0}$.
4. Une **infinité** : la somme des trois colonnes du one-hot est la colonne de 1 (M09a.18).
5. **Oui** : toutes donnent la projection de $\mathbf{y}$ sur l'espace des colonnes (M09b.14, question 6).
6. **Vrai** : le minimum de $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ existe toujours (c'est le pied de la perpendiculaire), et il annule le gradient. Seule l'unicité peut manquer.

### M09b.Q4 — Linéaire en x ou linéaire en w ?
1. **Oui** : colonnes $1, x, x^2$. 2. **Oui** : colonnes $1, \sin x, \cos x$. 3. **Non** : $w_1$ est dans une exponentielle. 4. **Oui** : colonnes $x_1x_2$ et $\ln x_3$. 5. **Non** : $w_2$ est au dénominateur. 6. **Non** : le développement contient $w_0w_1$, $w_0^2$ et $w_1^2$, des produits de poids.

### M09b.Q5 — Ridge : vrai ou faux sur la pénalité L2
1. **Vrai** : $\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}$ est inversible pour $\lambda > 0$ (M09b.16).
2. **Vrai** : $\mathbf{w} \approx \frac{1}{\lambda}\mathbf{X}^\top\mathbf{y}$ pour $\lambda$ grand (M09b.8, question g).
3. **Faux** : les poids rétrécissent, mais un poids n'est presque jamais exactement nul ; c'est le lasso qui en annule (fiche §6).
4. **Vrai** : les moindres carrés minimisent la somme des carrés ; ridge minimise autre chose, et ne peut pas faire mieux sur ce critère.
5. **Faux** : la pénalité dépend de l'unité de chaque feature (fiche §5, M09b.21) ; il faut standardiser.
6. **Vrai** : $\mathbf{w} \leftarrow (1 - 2\eta\lambda)\mathbf{w} - \eta\nabla L(\mathbf{w})$, le *weight decay*.

### M09b.Q6 — Lasso ou ridge : qui annule des poids ?
1. **L1**, le lasso.
2. **0** pour $w^2$ (sa dérivée $2w$ s'annule en 0) ; **1** pour $|w|$ juste à droite de 0 (et $-1$ juste à gauche).
3. **Ridge** : $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$ ; le lasso se résout par une méthode itérative.
4. $S(3 ;\ 1) = 2$ ; $S(-0{,}4 ;\ 0{,}5) = 0$, car $0{,}4 < 0{,}5$.
5. Que $\lambda$ (fiche §6 : le gain $g\varepsilon$ ne dépasse pas le coût $\lambda\varepsilon$).
6. **4** coins, sur les axes : $(1, 0)$, $(-1, 0)$, $(0, 1)$, $(0, -1)$.

### M09b.Q7 — Bruit gaussien et moindres carrés
1. Une loi **normale** centrée, $\mathcal{N}(0, \sigma^2)$, la même pour tous les exemples.
2. Une loi de **Laplace** centrée (fiche §7).
3. $\hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$.
4. **Faux** : à $\sigma^2$ fixé, maximiser la vraisemblance revient à minimiser la somme des carrés, quel que soit $\sigma^2$ (M09b.17).
5. Les poids ont été choisis pour rendre les résidus de **ces** données les plus petits possible : ils sont en moyenne plus petits que les bruits eux-mêmes.
6. Par $n - p$ (le nombre d'exemples moins le nombre de poids).

### M09b.Q8 — Biais, variance, bruit : ce qui change quand le modèle se complique
1. Le biais² **baisse** en général : la famille de modèles s'élargit.
2. La variance **monte** : le modèle épouse davantage chaque dataset.
3. **Rien** : $\sigma^2$ ne dépend que des données, pas du modèle.
4. Elle **baisse** (ou reste égale) : un polynôme de degré $d + 1$ peut toujours faire au moins aussi bien qu'un polynôme de degré $d$ sur les mêmes points.
5. Le biais² **monte** et la variance **baisse** (fiche §8).
6. **Non** : les trois termes sont positifs ou nuls, et le bruit est un plancher.

<a id="rappels"></a>

## 🔁 Rappels

### M09b.R1 — Le pivot de Gauss et l'inverse (M09a)
1. $\mathbf{x} = (2, 1)$ : $L_1 \leftrightarrow L_2$, puis $L_2 \leftarrow L_2 - 3L_1$ donne $-5y = -5$, $y = 1$, puis $x = 4 - 2 = 2$. Vérification : $6 + 1 = 7$, $2 + 2 = 4$.
2. $\frac{1}{5}\begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix}$ (le déterminant vaut $6 - 1 = 5$).
3. Le **pivot de Gauss** : moins d'opérations et moins d'erreurs d'arrondi que le calcul de l'inverse suivi d'un produit (M09a §7).
4. **Non** : une colonne combine les autres (M09a.18).
5. **1** : la seconde colonne vaut $-2$ fois la première.

### M09b.R2 — Maximum de vraisemblance et MAP (M04)
1. $\hat{\theta} = \frac{13}{20} = 0{,}65$.
2. Le mode du posterior $\mathrm{Beta}(13 + 3, 7 + 3)$ : $\frac{16 - 1}{16 + 10 - 2} = \frac{15}{24} = 0{,}625$.
3. Le log transforme le produit en somme (plus simple à dériver, et sans underflow) ; comme il est croissant, il a le même point de maximum.
4. L'écart tend vers 0 : les données finissent par dominer le prior.
5. Vers $\frac{1}{2}$, le centre du prior : $\mathrm{Beta}(3, 3)$ fait comme si l'on avait déjà vu 2 piles et 2 faces. C'est l'effet d'une régularisation : tirer l'estimation vers une valeur « raisonnable » choisie d'avance.

### M09b.R3 — Gradient et point critique (M05b)
1. $\nabla f(x, y) = (2x - 2y - 4,\ 6y - 2x)$.
2. $6y = 2x$ donne $x = 3y$, puis $6y - 2y - 4 = 0$ : $y = 1$, $x = 3$. Le point critique est $(3, 1)$.
3. $f(3, 1) = 9 + 3 - 6 - 12 = -6$.
4. La direction de $-\nabla f(0, 0) = (4, 0)$ : vers les $x$ croissants.
5. $(x - y - 2)^2 + 2(y - 1)^2 - 6 = x^2 + y^2 + 4 - 2xy - 4x + 4y + 2y^2 - 4y + 2 - 6 = x^2 + 3y^2 - 2xy - 4x$. Une somme de carrés est positive ou nulle, et nulle seulement si $y = 1$ et $x = y + 2 = 3$ : $f \ge -6$, avec égalité seulement en $(3, 1)$. C'est un **minimum global**. Les équations normales ont la même structure : une fonction quadratique « en bol ».

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M09b.1 — MSE, RMSE, MAE et loss de Huber de quatre résidus

**Réponses** : a) `[2, -1, -0.5, 4]` · b) `5.3125` · c) `2.3049` · d) `1.875` · e) `1.40625` · f) `2.65625` · g) `9.1875`.

**Démarche.**
- a) $r = (12 - 10,\ 7 - 8,\ 9 - 9{,}5,\ 15 - 11)$.
- b) $\sum r_i^2 = 4 + 1 + 0{,}25 + 16 = 21{,}25$, et $\frac{21{,}25}{4} = 5{,}3125$.
- c) $\sqrt{5{,}3125} \approx 2{,}3049$.
- d) $\frac{2 + 1 + 0{,}5 + 4}{4} = 1{,}875$.
- e) Avec $\delta = 1$ : $|r| = 2$ donne $1 \times (2 - 0{,}5) = 1{,}5$ ; $|r| = 1$ est au seuil, $\frac{1}{2}$ ; $0{,}5$ donne $0{,}125$ ; $4$ donne $3{,}5$. La moyenne vaut $\frac{5{,}625}{4} = 1{,}40625$.
- f) Avec $\delta = 5$, tous les résidus sont sous le seuil : la loss vaut $\frac{r^2}{2}$ partout, et sa moyenne $\frac{\mathrm{MSE}}{2}$.
- g) $\bar{y} = 10{,}75$ ; les écarts $1{,}25$, $-3{,}75$, $-1{,}75$, $4{,}25$ ont pour carrés $1{,}5625$, $14{,}0625$, $3{,}0625$, $18{,}0625$, de somme $36{,}75$ : $\frac{36{,}75}{4} = 9{,}1875$.

Pour la copie : la MSE et la loss de Huber en minutes carrées, la RMSE et la MAE en minutes. $R^2 = 1 - \frac{5{,}3125}{9{,}1875} \approx 0{,}42$ : le modèle fait disparaître 42 % de la variation des durées. Le résidu de 4 compte pour 8 dans la moyenne des $\frac{r^2}{2}$, mais pour 3,5 seulement dans la loss de Huber avec $\delta = 1$, qui le compte linéairement.

**Erreurs fréquentes.** Des résidus $\hat{y} - y$ (sans effet sur la MSE, mais faux en a) ; oublier de diviser par $n$ ; une MAE avec les résidus signés (1,125) ; $r^2$ au lieu de $\frac{r^2}{2}$ sous le seuil de Huber ; prendre $|r|$ au lieu de $\delta(|r| - \frac{\delta}{2})$ au-dessus.

**Variante.** La loss de Huber moyenne avec $\delta = 2$ ? *Réponse* : $2$, $0{,}5$, $0{,}125$ et $2 \times (4 - 1) = 6$, de moyenne $\frac{8{,}625}{4} = 2{,}15625$.

### Ex M09b.2 — La décomposition SCT = SCE + SCR et le R² d'un ajustement donné

**Réponses** : a) `4` · b) `18` · c) `3.6` · d) `14.4` · e) `0.8` · f) `[4, 10]` · g) `"7/9"`.

**Démarche.**
- a) et b) $\bar{y} = \frac{20}{5} = 4$ ; les écarts $-2, -2, 1, 0, 3$ donnent $\mathrm{SCT} = 4 + 4 + 1 + 0 + 9 = 18$.
- c) $\hat{y} = 1{,}6 ;\ 2{,}8 ;\ 4 ;\ 5{,}2 ;\ 6{,}4$, résidus $0{,}4 ;\ -0{,}8 ;\ 1 ;\ -1{,}2 ;\ 0{,}6$, carrés de somme $3{,}6$.
- d) $\hat{y} - \bar{y} = -2{,}4 ;\ -1{,}2 ;\ 0 ;\ 1{,}2 ;\ 2{,}4$ : $\mathrm{SCE} = 2 \times (5{,}76 + 1{,}44) = 14{,}4$.
- e) $1 - \frac{3{,}6}{18} = 0{,}8$, et aussi $\frac{14{,}4}{18}$.
- f) $\hat{y} = 2, 3, 4, 5, 6$ : résidus $0, -1, 1, -1, 1$, $\mathrm{SCR} = 4$ ; écarts à $\bar{y}$ : $-2, -1, 0, 1, 2$, $\mathrm{SCE} = 10$.
- g) $1 - \frac{4}{18} = \frac{7}{9}$.

Pour la copie : $14{,}4 + 3{,}6 = 18$, mais $10 + 4 = 14 \ne 18$. Les deux droites ont des résidus de somme nulle (la seconde passe aussi par le point moyen $(2, 4)$) ; mais $\sum x_ir_i$ vaut $0$ pour la première et $0 - 1 + 2 - 3 + 4 = 2$ pour la seconde : ses résidus ne sont pas orthogonaux à la colonne $x$. Le double produit $2\sum_i(\hat{y}_i - \bar{y})r_i = 2 \times 1 \times 2 = 4$ ne s'annule pas, et c'est lui qui manque : $10 + 4 + 4 = 18$. Pour cette droite, $\frac{\mathrm{SCE}}{\mathrm{SCT}} = \frac{5}{9}$ et $1 - \frac{\mathrm{SCR}}{\mathrm{SCT}} = \frac{7}{9}$ : les deux définitions du $R^2$ ne coïncident que pour les moindres carrés avec ordonnée à l'origine.

**Erreurs fréquentes.** Diviser les sommes par $n$ (ce sont des **sommes**) ; écrire $\mathrm{SCR}/\mathrm{SCT}$ pour le $R^2$ ; croire que la décomposition vaut pour toute droite.

**Variante.** La droite $\hat{y} = 1 + 1{,}5x$ : $\mathrm{SCR}$ ? *Réponse* : prédictions $1 ;\ 2{,}5 ;\ 4 ;\ 5{,}5 ;\ 7$, résidus $1 ;\ -0{,}5 ;\ 1 ;\ -1{,}5 ;\ 0$, $\mathrm{SCR} = 4{,}5$, plus que 3,6, comme toute droite autre que celle des moindres carrés.

### Ex M09b.3 — Les gradients de aᵀw, wᵀAw et ‖y − Xw‖², composante par composante en dimension 2

**Réponses** : a) `11` · b) `[4, -3]` · c) `5` · d) `[3, -4]` · e) `[3, 2, -1]` · f) `14` · g) `[-4, -18]`.

**Démarche.**
- a) et b) $4 \times 2 + (-3) \times (-1) = 11$ ; la fonction $4w_1 - 3w_2$ a pour dérivées partielles 4 et $-3$.
- c) $\mathbf{w}^\top\mathbf{A}\mathbf{w} = w_1^2 + 2w_1w_2 - w_2w_1 + 3w_2^2 = w_1^2 + w_1w_2 + 3w_2^2$, qui vaut $4 - 2 + 3 = 5$.
- d) $\frac{\partial}{\partial w_1} = 2w_1 + w_2 = 3$ et $\frac{\partial}{\partial w_2} = w_1 + 6w_2 = -4$ ; et $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w} = \begin{pmatrix} 2 & 1 \\ 1 & 6 \end{pmatrix}\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ -4 \end{pmatrix}$, alors que $2\mathbf{A}\mathbf{w} = (0, -10)$.
- e) et f) $\mathbf{X}\mathbf{w} = (0, -1, 3)$, $\mathbf{r} = (3, 2, -1)$, $\lVert \mathbf{r} \rVert^2 = 14$.
- g) $\mathbf{X}^\top\mathbf{r} = (3 + 0 - 1,\ 6 + 2 + 1) = (2, 9)$, et $-2\mathbf{X}^\top\mathbf{r} = (-4, -18)$.

Pour la copie : $L(\mathbf{w}) = (3 - w_1 - 2w_2)^2 + (1 - w_2)^2 + (2 - w_1 + w_2)^2$ ; $\frac{\partial L}{\partial w_1} = -2(3 - w_1 - 2w_2) - 2(2 - w_1 + w_2) = -2 \times 3 - 2 \times (-1) = -4$ au point $\mathbf{w}$. La dérivée de chaque carré fait apparaître le résidu, multiplié par $-2$ et par le coefficient de $w_1$ dans la ligne : c'est $-2\mathbf{X}^\top\mathbf{r}$, coordonnée par coordonnée.

**Erreurs fréquentes.** $2\mathbf{A}\mathbf{w}$ pour une matrice non symétrique ; oublier le terme croisé $w_1w_2$ dans le développement ; oublier le signe moins du gradient des moindres carrés.

**Variante.** Le gradient de $\mathbf{w}^\top\mathbf{A}^\top\mathbf{w}$ en $\mathbf{w}$ ? *Réponse* : le même, $(3, -4)$ : $\mathbf{w}^\top\mathbf{A}^\top\mathbf{w} = \mathbf{w}^\top\mathbf{A}\mathbf{w}$ (un nombre est égal à sa transposée).

### Ex M09b.4 — Les équations normales d'un modèle à deux features, sans ordonnée à l'origine

**Réponses** : a) `[2, 2]` · b) `[[6, 4], [4, 6]]` · c) `[12, 11]` · d) `[1.4, 0.9]` · e) `[-0.2, 0.3, -0.4, 0.1]` · f) `[0, 0]` · g) `0.3`.

**Démarche.**
- b) Les produits scalaires des colonnes : $1 + 4 + 1 + 0 = 6$, $2 + 2 + 0 + 0 = 4$, $4 + 1 + 0 + 1 = 6$.
- c) $3 + 8 + 1 + 0 = 12$ et $6 + 4 + 0 + 1 = 11$.
- d) Le déterminant vaut $36 - 16 = 20$ : $\mathbf{w} = \frac{1}{20}\begin{pmatrix} 6 & -4 \\ -4 & 6 \end{pmatrix}\begin{pmatrix} 12 \\ 11 \end{pmatrix} = \frac{1}{20}\begin{pmatrix} 28 \\ 18 \end{pmatrix}$.
- e) $\hat{\mathbf{y}} = (3{,}2 ;\ 3{,}7 ;\ 1{,}4 ;\ 0{,}9)$.
- f) $(-0{,}2 + 0{,}6 - 0{,}4 + 0,\ -0{,}4 + 0{,}3 + 0 + 0{,}1) = (0, 0)$.
- g) $0{,}04 + 0{,}09 + 0{,}16 + 0{,}01 = 0{,}3$.

Pour la copie : f) dit que le vecteur des résidus est **orthogonal** aux deux colonnes de $\mathbf{X}$ : $\hat{\mathbf{y}}$ est la projection de $\mathbf{y}$ sur le plan des colonnes. La somme des résidus vaut $-0{,}2$ : elle n'est nulle que si le vecteur $(1, 1, 1, 1)$ est une combinaison des colonnes, ce qui est garanti avec une colonne de 1, pas ici.

**Erreurs fréquentes.** Former $\mathbf{X}\mathbf{X}^\top$, de forme $(4, 4)$ ; se tromper de signe dans l'inverse ; croire que les résidus sont toujours de somme nulle.

**Variante.** Avec $\mathbf{y} = (5, 4, 1, 3)$ ? *Réponse* : $\mathbf{X}^\top\mathbf{y} = (14, 17)$, $\mathbf{w} = \frac{1}{20}(84 - 68,\ -56 + 102) = (0{,}8 ;\ 2{,}3)$.

### Ex M09b.5 — La colonne de 1 : l'ordonnée à l'origine et des résidus de moyenne nulle

**Réponses** : a) `[[4, 12], [12, 50]]` · b) `[16, 69]` · c) `[-0.5, 1.5]` · d) `[-1, 0.5, 1, -0.5]` · e) `4` · f) `[3, 4]` · g) `[4, 1.5]`.

**Démarche.**
- a) Le nombre de points, $\sum x = 12$, $\sum x^2 = 1 + 4 + 9 + 36 = 50$.
- b) $\sum y = 16$, $\sum xy = 0 + 6 + 15 + 48 = 69$.
- c) Le déterminant vaut $200 - 144 = 56$ : $\mathbf{w} = \frac{1}{56}\begin{pmatrix} 50 & -12 \\ -12 & 4 \end{pmatrix}\begin{pmatrix} 16 \\ 69 \end{pmatrix} = \frac{1}{56}\begin{pmatrix} -28 \\ 84 \end{pmatrix}$.
- d) $\hat{y} = 1 ;\ 2{,}5 ;\ 4 ;\ 8{,}5$.
- e) $\frac{16}{4} = 4 = \bar{y}$.
- g) Avec $x - 3 = (-2, -1, 0, 3)$ : $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 4 & 0 \\ 0 & 14 \end{pmatrix}$, $\mathbf{X}^\top\mathbf{y} = (16, 21)$, donc $w_0 = 4$ et $w_1 = 1{,}5$.

Pour la copie : $-0{,}5 + 1{,}5 \times 3 = 4$ : la droite passe par le point moyen. Après centrage, la somme des $x - \bar{x}$ est nulle : les deux nombres hors de la diagonale de $\mathbf{X}^\top\mathbf{X}$ s'annulent, et la première équation devient $4w_0 = \sum y_i$, soit $w_0 = \bar{y}$. La pente ne change pas : centrer ne fait que déplacer l'origine de l'axe des $x$.

**Erreurs fréquentes.** $(\sum x)^2$ au lieu de $\sum x^2$ ; inverser l'ordre de $w_0$ et $w_1$ ; croire que centrer change la pente.

**Variante.** Avec $y = (1, 3, 5, 7)$ ? *Réponse* : $\mathbf{X}^\top\mathbf{y} = (16, 1 + 6 + 15 + 42) = (16, 64)$ ; $\mathbf{w} = \frac{1}{56}(800 - 768,\ -192 + 256) = \frac{1}{56}(32, 64) = (\frac{4}{7}, \frac{8}{7})$.

### Ex M09b.6 — La matrice chapeau d'un petit tableau : H² = H et sa trace

**Réponses** : a) `[[3, 4], [4, 10]]` · b) `[[10, -4], [-4, 3]]` · c) `[[10, 6, -2], [6, 5, 3], [-2, 3, 13]]` · d) `2` · e) `3` · f) `[8, 16, 32]` · g) `True`.

**Démarche.**
- a) et b) Le déterminant vaut $30 - 16 = 14$, et $(\mathbf{X}^\top\mathbf{X})^{-1} = \frac{1}{14}\begin{pmatrix} 10 & -4 \\ -4 & 3 \end{pmatrix}$.
- c) $h_{ij} = \frac{1}{14}(1, x_i)\begin{pmatrix} 10 & -4 \\ -4 & 3 \end{pmatrix}\begin{pmatrix} 1 \\ x_j \end{pmatrix} = \frac{10 - 4x_i - 4x_j + 3x_ix_j}{14}$ : par exemple $h_{33} = \frac{10 - 24 + 27}{14} = \frac{13}{14}$.
- d) $\frac{10 + 5 + 13}{14} = 2$, le nombre de colonnes.
- e) Le point $x = 3$, de levier $\frac{13}{14}$.
- f) $14\,\mathbf{H}\mathbf{y} = (20 + 6 - 10,\ 12 + 5 + 15,\ -4 + 3 + 65) = (16, 32, 64)$, donc $7\hat{\mathbf{y}} = (8, 16, 32)$. C'est la droite $\hat{y} = \frac{8}{7}(1 + x)$.
- g) Première ligne de $\mathbf{H}\mathbf{H}$ : $\frac{1}{196}(100 + 36 + 4,\ 60 + 30 - 6,\ -20 + 18 - 26) = \frac{1}{196}(140, 84, -28) = \frac{1}{14}(10, 6, -2)$, la première ligne de $\mathbf{H}$.

Pour la copie : le point $x = 3$ est loin des deux autres (la moyenne des abscisses vaut $\frac{4}{3}$) ; la droite doit presque passer par lui : $h_{33} = \frac{13}{14}$ veut dire que $\hat{y}_3$ dépend surtout de $y_3$. $\mathbf{H}(1, 1, 1) = \frac{1}{14}(14, 14, 14)$ et $\mathbf{H}(0, 1, 3) = \frac{1}{14}(0, 14, 42)$ : un vecteur déjà dans l'espace des colonnes est sa propre projection ($\mathbf{H}\mathbf{X} = \mathbf{X}$, M09b.15).

**Erreurs fréquentes.** Une erreur de signe dans l'inverse ; calculer $\mathbf{X}^\top(\ldots)\mathbf{X}$, de forme $(2, 2)$, au lieu de $\mathbf{X}(\ldots)\mathbf{X}^\top$ ; une trace égale à $n = 3$.

**Variante.** Que vaut $\mathbf{H}\mathbf{y}$ pour $\mathbf{y} = (1, 3, 7)$ ? *Réponse* : $\mathbf{y} = 1 + 2x$ est déjà dans l'espace des colonnes : $\hat{\mathbf{y}} = \mathbf{y}$, et les résidus sont nuls.

### Ex M09b.7 — Compter les monômes des features polynomiales

**Réponses** : a) `4` · b) `10` · c) `20` · d) `34` · e) `21` · f) `15` · g) `6`.

**Démarche.**
- a) $u^3, u^2v, uv^2, v^3$ : $\binom{3 + 1}{3} = 4$.
- b) $1 + 2 + 3 + 4 = 10 = \binom{5}{3}$.
- c) $\binom{7}{2} - 1 = 20$.
- d) $\binom{7}{4} - 1 = 34$.
- e) $\binom{2 + 5}{2} = 21$ : 6 carrés et 15 produits de deux variables différentes.
- f) $\binom{6}{2} = 15$.
- g) Sans constante, en 7 variables : 7, 35, 119, 329, 791, puis 1 715 pour $d = 6$.

Pour la copie : 6 carrés $+ 15$ interactions $= 21$. Le nombre de colonnes est multiplié par un peu plus de 2 à chaque degré : au degré 6, il y a déjà plus de 1 700 colonnes pour 7 variables, et $\mathbf{X}^\top\mathbf{X}$ a près de 3 millions de cases.

**Erreurs fréquentes.** Oublier les produits croisés ; compter ou non la constante à contresens ; utiliser $\binom{p}{d}$ (combinaisons sans répétition, qui oublient les carrés).

**Variante.** Le nombre de monômes de degré exactement 3 en 4 variables ? *Réponse* : $\binom{3 + 3}{3} = 20$.

### Ex M09b.8 — Ridge en dimension 2 : résoudre (XᵀX + λI)w = Xᵀy pour trois valeurs de λ

**Réponses** : a) `[[2, 1, 3], [1, 2, 0]]` · b) `[2, -1]` · c) `[1.125, -0.375]` · d) `[0.8, -0.2]` · e) `[2.2361, 1.1859, 0.8246]` · f) `[3, 5.24]` · g) `[0, 0]`.

**Démarche.**
- a) $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $\mathbf{X}^\top\mathbf{y} = (2 + 1,\ 2 - 2) = (3, 0)$.
- b) $\frac{1}{3}\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 3 \\ 0 \end{pmatrix} = (2, -1)$.
- c) $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, de déterminant 8 : $\frac{1}{8}(9, -3)$.
- d) $\begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix}$, de déterminant 15 : $\frac{1}{15}(12, -3)$.
- e) $\sqrt{5}$, $\frac{\sqrt{90}}{8}$, $\sqrt{0{,}68}$.
- f) Pour $\lambda = 0$ : $\mathbf{X}\mathbf{w} = (1, 2, -1)$, résidus $(1, -1, -1)$. Pour $\lambda = 2$ : $\mathbf{X}\mathbf{w} = (0{,}6 ;\ 0{,}8 ;\ -0{,}2)$, résidus $(1{,}4 ;\ 0{,}2 ;\ -1{,}8)$, $\mathrm{SCR} = 1{,}96 + 0{,}04 + 3{,}24 = 5{,}24$.
- g) $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{w} = \mathbf{X}^\top\mathbf{y}$ donne $\mathbf{w} = \frac{1}{\lambda}(\mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{X}\mathbf{w})$, qui tend vers $\mathbf{0}$.

Pour la copie : $\lambda\mathbf{w} = \mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{X}\mathbf{w}$ tend vers $\mathbf{X}^\top\mathbf{y} = (3, 0)$ : pour $\lambda$ grand, les poids sont presque $\frac{1}{\lambda}\mathbf{X}^\top\mathbf{y}$. La somme des carrés d'entraînement monte avec $\lambda$, car les moindres carrés sont, par définition, le minimum de ce critère ; ridge échange un peu d'erreur d'entraînement contre des poids plus petits, qui varient moins d'un dataset à l'autre (fiche §8). Il peut être meilleur **sur de nouvelles données**.

**Erreurs fréquentes.** Ajouter $\lambda$ à toutes les cases de $\mathbf{X}^\top\mathbf{X}$ ; compter la pénalité dans la $\mathrm{SCR}$ ; croire que l'erreur d'entraînement baisse avec $\lambda$.

**Variante.** $\mathbf{w}$ pour $\lambda = 7$ ? *Réponse* : $\begin{pmatrix} 9 & 1 \\ 1 & 9 \end{pmatrix}$, de déterminant 80 : $\frac{1}{80}(27, -3) = (0{,}3375 ;\ -0{,}0375)$.

### Ex M09b.9 — Ridge comme MAP : un prior gaussien et λ = σ²/τ²

**Réponses** : a) `16` · b) `2` · c) `[0.6667, 0.3333]` · d) `[0.8889, 0.5556]` · e) `8` · f) `0.6325` · g) `True`.

**Démarche.**
- a) $\frac{4}{0{,}25} = 16$. b) $\frac{1}{0{,}5} = 2$.
- c) $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 5 & 1 \\ 1 & 2 \end{pmatrix}$, $\mathbf{X}^\top\mathbf{y} = (5, 2)$ ; avec $\lambda = 2$, $\begin{pmatrix} 7 & 1 \\ 1 & 4 \end{pmatrix}$, de déterminant 27 : $\mathbf{w} = \frac{1}{27}(20 - 2,\ -5 + 14) = (\frac{2}{3}, \frac{1}{3})$.
- d) Sans prior ($\lambda = 0$), le déterminant vaut 9 : $\frac{1}{9}(10 - 2,\ -5 + 10) = (\frac{8}{9}, \frac{5}{9})$.
- e) $\frac{2^2}{0{,}5} = 8$.
- f) $\tau^2 = \frac{1}{2{,}5} = 0{,}4$, $\tau = \sqrt{0{,}4} \approx 0{,}6325$.
- g) $\frac{100\sigma^2}{100\tau^2} = \frac{\sigma^2}{\tau^2}$.

Pour la copie : $\log p(\mathbf{w} \mid \mathbf{y}) = -\frac{1}{2}\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 - \frac{1}{2 \times 0{,}5}\lVert \mathbf{w} \rVert^2 + \text{cte} = -\frac{1}{2}\big(\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 + 2\lVert \mathbf{w} \rVert^2\big) + \text{cte}$ : le maximum est le minimum de ridge avec $\lambda = 2$, dont le gradient s'annule au point de c). Quand $\tau \to +\infty$, le prior devient plat (il ne préfère plus aucun poids), $\lambda \to 0$, et l'on retrouve le maximum de vraisemblance d).

**Erreurs fréquentes.** $\lambda = \frac{\sigma}{\tau}$ (sans les carrés) ; $\lambda = \frac{\tau^2}{\sigma^2}$ (à l'envers : un prior large doit affaiblir la pénalité) ; oublier que $\sigma$ double fait quadrupler $\sigma^2$.

**Variante.** Le MAP avec $\sigma = 1$ et $\tau = 1$ ? *Réponse* : $\lambda = 1$, $\begin{pmatrix} 6 & 1 \\ 1 & 3 \end{pmatrix}$, de déterminant 17 : $\frac{1}{17}(15 - 2,\ -5 + 12) = (\frac{13}{17}, \frac{7}{17}) \approx (0{,}7647 ;\ 0{,}4118)$.

### Ex M09b.10 — Les pénalités L1 et L2 de trois vecteurs de poids, et leurs boules

**Réponses** : a) `[3, 3, 3]` · b) `[9, 3, 5]` · c) `"v"` · d) `"ABD"` · e) `[1, 0.7071]` · f) `6` · g) `[0.4, 0.65]`.

**Démarche.**
- a) $3$, $1 + 1 + 1$, $2 + 1 + 0$. b) $9$, $3$, $4 + 1$.
- d) $|0{,}5| + |0{,}5| = 1$ ; $1 + 0 = 1$ ; $0{,}6 + 0{,}6 = 1{,}2$ ; $0{,}25 + 0{,}75 = 1$.
- e) Sur le bord du losange, $\lVert \mathbf{w} \rVert$ est le plus grand aux coins (1) et le plus petit au milieu des côtés, comme $(\frac{1}{2}, \frac{1}{2})$ : $\frac{1}{\sqrt{2}} \approx 0{,}7071$.
- f) Les 6 points $(\pm 1, 0, 0)$, $(0, \pm 1, 0)$, $(0, 0, \pm 1)$ : la boule L1 de $\mathbb{R}^3$ est un octaèdre.
- g) $0{,}1 \times (0{,}5 + 2 + 0 + 1{,}5) = 0{,}4$ et $0{,}1 \times (0{,}25 + 4 + 0 + 2{,}25) = 0{,}65$.

Pour la copie : la boule L1 de $\mathbb{R}^2$ est le losange de sommets $(\pm 1, 0)$, $(0, \pm 1)$, la boule L2 le disque unité ; le losange est à l'intérieur du disque, et ne le touche qu'en ses 4 coins. A, B et D sont sur les côtés du losange ; C est dehors (mais dans le disque). Les trois vecteurs ont la même pénalité L1 : elle ne distingue pas un poids concentré sur une feature d'un poids réparti. La pénalité L2, elle, préfère nettement le vecteur réparti $\mathbf{v}$ (3 contre 9) : ridge étale le poids entre des features semblables.

**Erreurs fréquentes.** Oublier les valeurs absolues dans la norme L1 ; prendre la racine dans la pénalité L2 (c'est le **carré** de la norme) ; confondre la boule L1 avec un carré.

**Variante.** Un point de la boule L2 unité qui n'est pas dans la boule L1 ? *Réponse* : C $(0{,}6 ;\ 0{,}6)$ : $0{,}36 + 0{,}36 \le 1$, mais $0{,}6 + 0{,}6 > 1$.

### Ex M09b.11 — La log-vraisemblance gaussienne d'un modèle linéaire et l'estimation de σ²

**Réponses** : a) `0.72` · b) `1.2` · c) `-6.2734` · d) `-6.3947` · e) `0.2` · f) `1.2214` · g) `[4, 4]`.

**Démarche.**
- a) $\frac{3{,}6}{5} = 0{,}72$. b) $\frac{3{,}6}{5 - 2} = 1{,}2$.
- c) $\ln L = -\frac{5}{2}\ln(2\pi \times 0{,}72) - \frac{3{,}6}{2 \times 0{,}72} = -2{,}5 \times 1{,}5094 - 2{,}5 \approx -6{,}2734$.
- d) $-\frac{5}{2}\ln(2\pi) - \frac{3{,}6}{2} \approx -4{,}5947 - 1{,}8 = -6{,}3947$.
- e) Seul le terme des résidus change : $-\frac{3{,}6}{2} - \big(-\frac{4}{2}\big) = 0{,}2$.
- f) $e^{0{,}2} \approx 1{,}2214$.
- g) $0{,}4 + 0{,}8 + 1 + 1{,}2 + 0{,}6 = 4$ et $0 + 1 + 1 + 1 + 1 = 4$.

Pour la copie : en $\sigma^2 = \hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$, le terme des résidus vaut $\frac{\mathrm{SCR}}{2\,\mathrm{SCR}/n} = \frac{n}{2}$, d'où $-\frac{n}{2}\big(\ln(2\pi\hat{\sigma}^2) + 1\big)$. Avec un bruit de Laplace, la log-vraisemblance est $-\frac{1}{b}\sum_i |r_i|$ à une constante près : les deux droites ont la même somme des valeurs absolues, donc la **même** vraisemblance. Le choix du bruit change la « meilleure » droite.

**Erreurs fréquentes.** Le logarithme décimal ; oublier le facteur $\frac{1}{2}$ du terme des résidus ; diviser par $n - p$ pour l'estimateur du maximum de vraisemblance.

**Variante.** La log-vraisemblance de la droite $\hat{y} = 2 + x$ en son propre $\hat{\sigma}^2$ ? *Réponse* : $\hat{\sigma}^2 = \frac{4}{5} = 0{,}8$ et $-2{,}5\big(\ln(2\pi \times 0{,}8) + 1\big) \approx -6{,}5368$, plus petite que c).

### Ex M09b.12 — L'estimateur rétréci c·x̄ : biais, variance et erreur quadratique

**Réponses** : a) `-1` · b) `0.25` · c) `1.25` · d) `1` · e) `0.8` · f) `0.8` · g) `0.2`.

**Démarche.**
- a) $\mathbb{E}[c\,\bar{x}] - \mu = (c - 1)\mu = -0{,}5 \times 2$.
- b) $c^2\frac{\sigma^2}{n} = 0{,}25 \times 1$.
- c) $(-1)^2 + 0{,}25$.
- d) $\bar{x}$ est sans biais, de variance $\frac{9}{9} = 1$.
- e) $E(c) = 4(c - 1)^2 + c^2$, $E'(c) = 8(c - 1) + 2c = 0$ donne $c = 0{,}8$.
- f) $4 \times 0{,}04 + 0{,}64 = 0{,}8$.
- g) $\frac{0{,}25}{0{,}25 + 1} = 0{,}2$.

Pour la copie : $E(c) = (c - 1)^2\mu^2 + c^2\frac{\sigma^2}{n}$, $E'(c) = 2(c - 1)\mu^2 + 2c\frac{\sigma^2}{n}$, d'où $c^* = \frac{\mu^2}{\mu^2 + \sigma^2/n}$. Il dépend de $\mu$, justement ce qu'on cherche : en pratique, on règle la force du rétrécissement autrement (par validation, ou avec un prior). Quand $n$ grandit, $\frac{\sigma^2}{n} \to 0$ et $c^* \to 1$ : avec beaucoup de données, il ne faut presque plus rétrécir. g) montre l'inverse : quand le signal $\mu$ est petit devant le bruit, il faut rétrécir fort.

**Erreurs fréquentes.** $c\,\frac{\sigma^2}{n}$ au lieu de $c^2\frac{\sigma^2}{n}$ ; additionner le biais (au lieu de son carré) et la variance ; oublier de diviser $\sigma^2$ par $n$.

**Variante.** Le $c^*$ et l'erreur avec $n = 36$ (mêmes $\mu$ et $\sigma^2$) ? *Réponse* : $\frac{\sigma^2}{n} = 0{,}25$, $c^* = \frac{4}{4{,}25} \approx 0{,}941$, et $E(c^*) = c^*\frac{\sigma^2}{n} \approx 0{,}235$, contre $0{,}25$ pour $\bar{x}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M09b.13 — Le gradient de wᵀAw vaut (A + Aᵀ)w

**Réponse modèle.**
1. $f(\mathbf{w}) = \mathbf{w}^\top(\mathbf{A}\mathbf{w}) = \sum_{i=1}^{p} w_i(\mathbf{A}\mathbf{w})_i = \sum_{i=1}^{p}\sum_{j=1}^{p} a_{ij}w_iw_j$.
2. Si $i = j = k$ : $\frac{\partial}{\partial w_k}w_k^2 = 2w_k$. Si $i = k \ne j$ : $w_j$. Si $j = k \ne i$ : $w_i$. Si $i \ne k$ et $j \ne k$ : 0.
3. Dans la double somme, ne restent que les termes où $i = k$ ou $j = k$. Les termes $i = k$ donnent $\sum_{j \ne k} a_{kj}w_j$, les termes $j = k$ donnent $\sum_{i \ne k} a_{ik}w_i$, et le terme $i = j = k$ donne $2a_{kk}w_k$, qu'on partage entre les deux sommes : $\frac{\partial f}{\partial w_k} = \sum_j a_{kj}w_j + \sum_i a_{ik}w_i$.
4. $\sum_j a_{kj}w_j = (\mathbf{A}\mathbf{w})_k$, et $\sum_i a_{ik}w_i = \sum_i (\mathbf{A}^\top)_{ki}w_i = (\mathbf{A}^\top\mathbf{w})_k$. Donc $\nabla f(\mathbf{w}) = \mathbf{A}\mathbf{w} + \mathbf{A}^\top\mathbf{w} = (\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$.
5. Si $\mathbf{S}^\top = \mathbf{S}$, $(\mathbf{S} + \mathbf{S}^\top)\mathbf{w} = 2\mathbf{S}\mathbf{w}$. Avec $\mathbf{S} = \mathbf{I}$ : $\lVert \mathbf{w} \rVert^2 = \mathbf{w}^\top\mathbf{I}\mathbf{w}$ a pour gradient $2\mathbf{w}$.
6. $\mathbf{a}^\top\mathbf{w} = \sum_j a_jw_j$, et $\frac{\partial}{\partial w_k}(a_jw_j)$ vaut $a_k$ si $j = k$, 0 sinon : $\frac{\partial}{\partial w_k}(\mathbf{a}^\top\mathbf{w}) = a_k$, donc $\nabla(\mathbf{a}^\top\mathbf{w}) = \mathbf{a}$.

**Grille.** (1) la double somme ; (2) les quatre cas, dont le $2w_k$ du carré ; (3) le partage du terme diagonal entre les deux sommes (sinon il est compté deux fois ou oublié) ; (4) la reconnaissance de $(\mathbf{A}\mathbf{w})_k$ et de $(\mathbf{A}^\top\mathbf{w})_k$, et la conclusion vectorielle ; (5) les deux cas particuliers ; (6) le gradient d'une fonction linéaire.

### Ex M09b.14 — Les équations normales en dimension n, par le gradient

**Réponse modèle.**
1. $L(\mathbf{w}) = (\mathbf{y} - \mathbf{X}\mathbf{w})^\top(\mathbf{y} - \mathbf{X}\mathbf{w}) = \mathbf{y}^\top\mathbf{y} - \mathbf{y}^\top\mathbf{X}\mathbf{w} - \mathbf{w}^\top\mathbf{X}^\top\mathbf{y} + \mathbf{w}^\top\mathbf{X}^\top\mathbf{X}\mathbf{w}$, en utilisant $(\mathbf{X}\mathbf{w})^\top = \mathbf{w}^\top\mathbf{X}^\top$. Le nombre $\mathbf{w}^\top\mathbf{X}^\top\mathbf{y}$ est une matrice $1 \times 1$, égale à sa transposée $\mathbf{y}^\top\mathbf{X}\mathbf{w}$. Donc $L(\mathbf{w}) = \mathbf{y}^\top\mathbf{y} - 2(\mathbf{X}^\top\mathbf{y})^\top\mathbf{w} + \mathbf{w}^\top(\mathbf{X}^\top\mathbf{X})\mathbf{w}$.
2. Par M09b.13, avec $\mathbf{a} = -2\mathbf{X}^\top\mathbf{y}$ et la matrice symétrique $\mathbf{X}^\top\mathbf{X}$ : $\nabla L(\mathbf{w}) = -2\mathbf{X}^\top\mathbf{y} + 2\mathbf{X}^\top\mathbf{X}\mathbf{w}$. Un point critique vérifie $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$.
3. $\mathbf{y} - \mathbf{X}(\mathbf{w}^* + \mathbf{v}) = \mathbf{r}^* - \mathbf{X}\mathbf{v}$, donc $L(\mathbf{w}^* + \mathbf{v}) = \lVert \mathbf{r}^* \rVert^2 - 2(\mathbf{X}\mathbf{v})^\top\mathbf{r}^* + \lVert \mathbf{X}\mathbf{v} \rVert^2$. Or $(\mathbf{X}\mathbf{v})^\top\mathbf{r}^* = \mathbf{v}^\top\mathbf{X}^\top\mathbf{r}^* = \mathbf{v}^\top(\mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{X}\mathbf{w}^*) = 0$. D'où $L(\mathbf{w}^* + \mathbf{v}) = L(\mathbf{w}^*) + \lVert \mathbf{X}\mathbf{v} \rVert^2$.
4. Tout $\mathbf{w}$ s'écrit $\mathbf{w}^* + \mathbf{v}$ avec $\mathbf{v} = \mathbf{w} - \mathbf{w}^*$, et $\lVert \mathbf{X}\mathbf{v} \rVert^2 \ge 0$ : $L(\mathbf{w}) \ge L(\mathbf{w}^*)$ pour tout $\mathbf{w}$. C'est un minimum global.
5. $L(\mathbf{w}) = L(\mathbf{w}^*)$ exige $\mathbf{X}\mathbf{v} = \mathbf{0}$, donc $\mathbf{v} = \mathbf{0}$ si les colonnes sont indépendantes : le minimum est atteint en un seul point.
6. Si $\mathbf{w}$ est un autre minimum, $\lVert \mathbf{X}(\mathbf{w} - \mathbf{w}^*) \rVert^2 = 0$, donc $\mathbf{X}\mathbf{w} = \mathbf{X}\mathbf{w}^*$ : les mêmes prédictions.

**Grille.** (1) le développement, avec la justification de l'égalité des deux termes croisés ; (2) le gradient par M09b.13 (dont la symétrie de $\mathbf{X}^\top\mathbf{X}$) et les équations normales ; (3) le calcul de $L(\mathbf{w}^* + \mathbf{v})$ et l'annulation du double produit par les équations normales ; (4) l'argument « pour tout $\mathbf{w}$ » (pas seulement un point critique) ; (5) l'unicité par l'indépendance des colonnes ; (6) les mêmes prédictions sans l'unicité.

### Ex M09b.15 — Le résidu est orthogonal aux colonnes de X ; H est symétrique et idempotente

**Réponse modèle.**
1. $\mathbf{X}^\top\mathbf{r} = \mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y} = \mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{y} = \mathbf{0}$. La coordonnée $j$ de $\mathbf{X}^\top\mathbf{r}$ est le produit scalaire de la colonne $j$ avec $\mathbf{r}$ : tous sont nuls.
2. $\mathbf{H}^\top = (\mathbf{X}^\top)^\top\big((\mathbf{X}^\top\mathbf{X})^{-1}\big)^\top\mathbf{X}^\top = \mathbf{X}\big((\mathbf{X}^\top\mathbf{X})^\top\big)^{-1}\mathbf{X}^\top = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top = \mathbf{H}$, car $\mathbf{X}^\top\mathbf{X}$ est symétrique.
3. $\mathbf{H}\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}(\mathbf{X}^\top\mathbf{X})(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top = \mathbf{H}$. Et $\mathbf{H}\mathbf{X} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}(\mathbf{X}^\top\mathbf{X}) = \mathbf{X}$ : chaque colonne de $\mathbf{X}$, déjà dans l'espace des colonnes, est sa propre projection.
4. $(\mathbf{I} - \mathbf{H})^\top = \mathbf{I} - \mathbf{H}^\top = \mathbf{I} - \mathbf{H}$ ; $(\mathbf{I} - \mathbf{H})^2 = \mathbf{I} - 2\mathbf{H} + \mathbf{H}^2 = \mathbf{I} - \mathbf{H}$ ; $\mathbf{H}(\mathbf{I} - \mathbf{H}) = \mathbf{H} - \mathbf{H}^2 = \mathbf{0}$.
5. $\operatorname{tr}\mathbf{H} = \operatorname{tr}\big(\mathbf{X}\,[(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top]\big) = \operatorname{tr}\big((\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{X}\big) = \operatorname{tr}\mathbf{I}_p = p$.
6. La première coordonnée de $\mathbf{X}^\top\mathbf{r} = \mathbf{0}$ est $\mathbf{1} \cdot \mathbf{r} = \sum_i r_i = 0$. Alors $\bar{\hat{y}} = \bar{y}$, et $\mathbf{y} - \bar{y}\mathbf{1} = (\hat{\mathbf{y}} - \bar{y}\mathbf{1}) + \mathbf{r}$. Le vecteur $\hat{\mathbf{y}} - \bar{y}\mathbf{1} = \mathbf{X}\mathbf{w} - \bar{y}\mathbf{1}$ est une combinaison des colonnes de $\mathbf{X}$ (la colonne de 1 en fait partie), donc orthogonal à $\mathbf{r}$ par 1. Par Pythagore, $\lVert \mathbf{y} - \bar{y}\mathbf{1} \rVert^2 = \lVert \hat{\mathbf{y}} - \bar{y}\mathbf{1} \rVert^2 + \lVert \mathbf{r} \rVert^2$ : $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$.

**Grille.** (1) le calcul de $\mathbf{X}^\top\mathbf{r}$ et sa lecture colonne par colonne ; (2) la transposée d'un produit de trois facteurs, l'échange transposée-inverse, la symétrie de $\mathbf{X}^\top\mathbf{X}$ ; (3) la simplification $(\mathbf{X}^\top\mathbf{X})^{-1}(\mathbf{X}^\top\mathbf{X}) = \mathbf{I}$, deux fois ; (4) les trois égalités pour $\mathbf{I} - \mathbf{H}$ ; (5) le déplacement du produit dans la trace, et $\operatorname{tr}\mathbf{I}_p = p$ ; (6) la somme des résidus par la colonne de 1, l'orthogonalité, Pythagore.

### Ex M09b.16 — XᵀX + λI est inversible pour tout λ > 0

**Réponse modèle.**
1. $\mathbf{v}^\top\mathbf{X}^\top\mathbf{X}\mathbf{v} = (\mathbf{X}\mathbf{v})^\top(\mathbf{X}\mathbf{v}) = \lVert \mathbf{X}\mathbf{v} \rVert^2$.
2. $0 = \mathbf{v}^\top(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{v} = \lVert \mathbf{X}\mathbf{v} \rVert^2 + \lambda\lVert \mathbf{v} \rVert^2$. Les deux termes sont positifs ou nuls et leur somme est nulle : $\lambda\lVert \mathbf{v} \rVert^2 = 0$, et comme $\lambda > 0$, $\mathbf{v} = \mathbf{0}$.
3. Le système homogène $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ n'a que la solution $\mathbf{0}$ : la matrice carrée est de rang $p$, donc inversible (M09a §8).
4. $\nabla L_\lambda(\mathbf{w}) = -2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w}) + 2\lambda\mathbf{w}$ (M09b.13 et M09b.14). Il s'annule si et seulement si $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, qui a une seule solution par 3. (Comme en M09b.14, $L_\lambda(\mathbf{w}^* + \mathbf{v}) = L_\lambda(\mathbf{w}^*) + \lVert \mathbf{X}\mathbf{v} \rVert^2 + \lambda\lVert \mathbf{v} \rVert^2$ : c'est le minimum global.)
5. $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 5 & 15 \\ 15 & 45 \end{pmatrix}$, de déterminant $225 - 225 = 0$ : pas inversible (la seconde colonne de $\mathbf{X}$ est le triple de la première). Avec $\lambda = 1$ : $\begin{pmatrix} 6 & 15 \\ 15 & 46 \end{pmatrix}$, de déterminant $276 - 225 = 51 \ne 0$.
6. $\det(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}) = (5 + \lambda)(45 + \lambda) - 225 = \lambda^2 + 50\lambda = \lambda(\lambda + 50)$ : $\lambda = -50$ la rend singulière. En effet, $\mathbf{X}^\top\mathbf{X}(1, 3) = (50, 150) = 50 \times (1, 3)$, donc $(\mathbf{X}^\top\mathbf{X} - 50\,\mathbf{I})(1, 3) = \mathbf{0}$ : l'argument de la question 2 tombe, car $\lambda\lVert \mathbf{v} \rVert^2$ peut compenser $\lVert \mathbf{X}\mathbf{v} \rVert^2$ quand $\lambda < 0$.

**Grille.** (1) la forme quadratique écrite comme un carré de norme ; (2) la somme de deux termes positifs nulle, et l'usage de $\lambda > 0$ ; (3) le lien « seul $\mathbf{0}$ est envoyé sur $\mathbf{0}$ » $\Rightarrow$ inversible ; (4) le gradient et l'unicité du point critique ; (5) les deux déterminants ; (6) une valeur négative qui annule le déterminant (une seule suffit).

### Ex M09b.17 — Un bruit gaussien mène aux moindres carrés : le maximum de vraisemblance

**Réponse modèle.**
1. $y_i \sim \mathcal{N}(\mathbf{x}_i \cdot \mathbf{w}, \sigma^2)$, de densité $\frac{1}{\sqrt{2\pi\sigma^2}}\exp\big(-\frac{(y_i - \mathbf{x}_i \cdot \mathbf{w})^2}{2\sigma^2}\big)$. Les observations étant indépendantes, $L(\mathbf{w}, \sigma^2) = \prod_{i=1}^{n}\frac{1}{\sqrt{2\pi\sigma^2}}\exp\big(-\frac{(y_i - \mathbf{x}_i \cdot \mathbf{w})^2}{2\sigma^2}\big)$.
2. Le log d'un produit est la somme des logs : $\ln L = \sum_i\big(-\frac{1}{2}\ln(2\pi\sigma^2) - \frac{(y_i - \mathbf{x}_i \cdot \mathbf{w})^2}{2\sigma^2}\big) = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2}\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$.
3. Le premier terme ne dépend pas de $\mathbf{w}$ ; le second est $-\frac{1}{2\sigma^2}$ (un nombre négatif fixé) fois $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ : il est maximal exactement quand cette somme est minimale. Le résultat, la solution des moindres carrés, ne dépend pas de $\sigma^2$.
4. Avec $S = \mathrm{SCR}$ fixé, $g(s) = -\frac{n}{2}\ln(2\pi s) - \frac{S}{2s}$, $g'(s) = -\frac{n}{2s} + \frac{S}{2s^2} = \frac{S - ns}{2s^2}$ : positive pour $s < \frac{S}{n}$, négative après. Le maximum est en $\hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$.
5. $\ln L = -n\ln(2b) - \frac{1}{b}\sum_i |y_i - \mathbf{x}_i \cdot \mathbf{w}|$ : à $b$ fixé, il faut minimiser la **somme des valeurs absolues** des résidus.

**Grille.** (1) la densité et le produit, avec l'indépendance ; (2) le passage au log, terme à terme ; (3) l'argument « le seul terme qui dépend de $\mathbf{w}$, multiplié par un nombre négatif », et l'indépendance vis-à-vis de $\sigma^2$ ; (4) la dérivée en $s = \sigma^2$ (pas en $\sigma$, ou alors bien faite) et l'étude du signe ; (5) la somme des valeurs absolues.

### Ex M09b.18 — La décomposition biais² + variance + bruit, démontrée

**Réponse modèle.**
1. Avec $m = \mathbb{E}[\hat{\theta}]$ : $(\hat{\theta} - \theta)^2 = (\hat{\theta} - m)^2 + 2(\hat{\theta} - m)(m - \theta) + (m - \theta)^2$. En espérance : $\mathbb{E}[(\hat{\theta} - m)^2] = \mathbb{V}(\hat{\theta})$ ; le double produit vaut $2(m - \theta)\,\mathbb{E}[\hat{\theta} - m] = 0$, car $m - \theta$ est un nombre fixé ; et $(m - \theta)^2$ est le biais². D'où la formule.
2. $y - \hat{f}_D(x) = \varepsilon + \big(f(x) - \bar{f}(x)\big) + \big(\bar{f}(x) - \hat{f}_D(x)\big)$.
3. Le carré donne trois carrés et trois doubles produits. $\mathbb{E}\big[\varepsilon\,(f - \bar{f})\big] = (f - \bar{f})\,\mathbb{E}[\varepsilon] = 0$ ($f - \bar{f}$ est fixé, $\mathbb{E}[\varepsilon] = 0$) ; $\mathbb{E}\big[\varepsilon\,(\bar{f} - \hat{f}_D)\big] = \mathbb{E}[\varepsilon]\,\mathbb{E}[\bar{f} - \hat{f}_D] = 0$ (indépendance de $\varepsilon$ et de $D$) ; $\mathbb{E}\big[(f - \bar{f})(\bar{f} - \hat{f}_D)\big] = (f - \bar{f})\,\mathbb{E}_D[\bar{f} - \hat{f}_D] = 0$ (définition de $\bar{f}$).
4. Il reste $\mathbb{E}[\varepsilon^2] + (f - \bar{f})^2 + \mathbb{E}_D[(\hat{f}_D - \bar{f})^2] = \sigma^2 + \text{biais}^2 + \text{variance}$ (car $\mathbb{E}[\varepsilon^2] = \mathbb{V}(\varepsilon) = \sigma^2$, la moyenne étant nulle).
5. $\mathbb{E}[c\,\bar{x}] = c\mu$ et $\mathbb{V}(c\,\bar{x}) = c^2\frac{\sigma^2}{n}$ : $E(c) = (c - 1)^2\mu^2 + c^2\frac{\sigma^2}{n}$, et $E'(c) = 0$ donne $c^* = \frac{\mu^2}{\mu^2 + \sigma^2/n}$.

**Grille.** (1) l'ajout et le retrait de $\mathbb{E}[\hat{\theta}]$, et le double produit nul ; (2) la décomposition en trois termes ; (3) les trois doubles produits, chacun avec **sa** raison (moyenne nulle du bruit, indépendance, définition de $\bar{f}$) ; (4) la conclusion, avec $\mathbb{E}[\varepsilon^2] = \sigma^2$ ; (5) l'application à $c\,\bar{x}$.

### Ex M09b.19 — Le nombre de monômes de degré au plus d en p variables : C(p + d, d)

**Réponse modèle.**
1. Un monôme $x_1^{k_1}\cdots x_p^{k_p}$ est déterminé par ses exposants, et deux suites d'exposants différentes donnent deux monômes différents ; son degré est $k_1 + \cdots + k_p$.
2. On écrit $k_1$ étoiles, une barre, $k_2$ étoiles, une barre, …, $k_p$ étoiles : $k$ étoiles et $p - 1$ barres, $k + p - 1$ symboles. Réciproquement, une suite de $k$ étoiles et $p - 1$ barres se lit d'une seule façon (les étoiles avant la première barre, entre la première et la deuxième, …). C'est une bijection, et une suite est déterminée par les positions de ses $k$ étoiles parmi $k + p - 1$ : $\binom{k + p - 1}{k}$ monômes.
3. On pose $k_0 = d - (k_1 + \cdots + k_p) \ge 0$ (le degré « manquant ») : $(k_0, k_1, \ldots, k_p)$ est un $(p+1)$-uplet d'entiers positifs ou nuls de somme $d$, et réciproquement. Par 2, avec $p + 1$ variables : $\binom{d + p}{d}$.
4. $1, x_1, x_2, x_1^2, x_1x_2, x_2^2$ : 6, et $\binom{4}{2} = 6$.
5. Les monômes de degré au plus $d$ sont ceux de degré exactement $0, 1, \ldots, d$ : en comptant de deux façons, $\sum_{k=0}^{d}\binom{k + p - 1}{k} = \binom{p + d}{d}$.
6. $\binom{p + d}{d} = \frac{(p + d)(p + d - 1)\cdots(p + 1)}{d!}$ : un produit de $d$ facteurs, chacun équivalent à $p$ quand $p$ est grand devant $d$. Il est donc de l'ordre de $\frac{p^d}{d!}$.

**Grille.** (1) la correspondance monôme-exposants ; (2) le codage, la bijection (dans les deux sens), le choix des positions ; (3) la variable d'écart $k_0$ et la réduction au cas 2 ; (4) la vérification par la liste ; (5) le double dénombrement ; (6) le produit de $d$ facteurs.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09b.20 — Pont : la loss d'un modèle linéaire et son gradient pour un batch, prêts pour la descente de gradient

**Réponses** : a) `[1.5, 1.5, -1.5, -0.5]` · b) `[1.5, -1.5, 2.5, 1.5]` · c) `3.25` · d) `[4, 4, 10.5]` · e) `[-2, -2, -5.25]` · f) `[0.7, 1.2, -0.475]` · g) `1.0117`.

**Démarche.**
- a) $0{,}5 + 2 - 1$, $0{,}5 + 0 + 1$, $0{,}5 + 1 - 3$, $0{,}5 - 1 + 0$.
- c) $\frac{2{,}25 + 2{,}25 + 6{,}25 + 2{,}25}{4} = \frac{13}{4}$.
- d) $(1{,}5 - 1{,}5 + 2{,}5 + 1{,}5,\ 3 + 0 + 2{,}5 - 1{,}5,\ 1{,}5 + 1{,}5 + 7{,}5 + 0)$.
- e) $-\frac{2}{4}\mathbf{X}^\top\mathbf{r}$.
- f) $\mathbf{w} - 0{,}1 \times (-2, -2, -5{,}25) = (0{,}5 + 0{,}2 ;\ 1 + 0{,}2 ;\ -1 + 0{,}525)$.
- g) Les nouvelles prédictions $(2{,}625 ;\ 1{,}175 ;\ 0{,}475 ;\ -0{,}5)$ laissent les résidus $(0{,}375 ;\ -1{,}175 ;\ 0{,}525 ;\ 1{,}5)$, de carrés de somme $4{,}046875$ : $\frac{4{,}046875}{4} \approx 1{,}0117$.

Pour la copie : $\mathbf{X}$ $(4, 3)$, $\mathbf{w}$ $(3,)$, $\hat{\mathbf{y}}$ et $\mathbf{r}$ $(4,)$, $\mathbf{X}^\top$ $(3, 4)$, le gradient $(3,)$ comme $\mathbf{w}$. Le gradient coûte deux produits matrice-vecteur, $\mathbf{X}\mathbf{w}$ et $\mathbf{X}^\top\mathbf{r}$ : environ $2Bp$ multiplications. Diviser par $n$ rend la loss et son gradient indépendants de la taille du batch : sans cette division, doubler le batch doublerait le gradient, et il faudrait diviser $\eta$ par deux pour garder les mêmes pas.

**Erreurs fréquentes.** Un gradient sans le signe moins (le pas monte au lieu de descendre) ; oublier le facteur $\frac{2}{n}$ ; ajouter $\eta \times$ gradient.

**Variante.** Avec un pas $\eta = 0{,}05$, les nouveaux poids ? *Réponse* : $(0{,}6 ;\ 1{,}1 ;\ -0{,}7375)$.

### Ex M09b.21 — Pont : pourquoi standardiser les colonnes avant ridge

**Réponses** : a) `[0.9, -0.5]` · b) `[0.75, -0.3333]` · c) `[0.8333, 0.6667]` · d) `0.0009` · e) `1.0` · f) `"2/3"` · g) `True`.

**Démarche.**
- a) $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 10 & 0 \\ 0 & 4 \end{pmatrix}$ et $\mathbf{X}^\top\mathbf{y} = (6 - 1 + 0 + 4,\ -3 - 1 + 0 + 2) = (9, -2)$ : $\mathbf{w} = (\frac{9}{10}, \frac{-2}{4})$.
- b) $\begin{pmatrix} 12 & 0 \\ 0 & 6 \end{pmatrix}\mathbf{w} = (9, -2)$ : $(\frac{9}{12}, -\frac{2}{6})$.
- c) $\frac{10}{12}$ et $\frac{4}{6}$.
- d) En mètres, la colonne vaut $1\,000\,x_1$ : $\lVert \cdot \rVert^2 = 10^7$, le produit avec $\mathbf{y}$ vaut $9\,000$, et le poids $\frac{9\,000}{10^7} = 0{,}0009$.
- e) $\frac{10^7}{10^7 + 2} \approx 0{,}9999998$, soit $1{,}0000$ à 4 décimales.
- f) L'écart-type de $x_1$ vaut $\sqrt{\frac{10}{4}}$, celui de $x_2$ vaut 1 : après standardisation, chaque colonne a $\lVert \mathbf{x}_j \rVert^2 = n = 4$, et le facteur vaut $\frac{4}{4 + 2} = \frac{2}{3}$.

Pour la copie : avec $\mathbf{X}^\top\mathbf{X}$ diagonale, le système ridge se sépare en deux équations, $(\lVert \mathbf{x}_j \rVert^2 + \lambda)\,w_j = \mathbf{x}_j \cdot \mathbf{y}$, et le poids des moindres carrés est $\frac{\mathbf{x}_j \cdot \mathbf{y}}{\lVert \mathbf{x}_j \rVert^2}$ : le rapport vaut $\frac{\lVert \mathbf{x}_j \rVert^2}{\lVert \mathbf{x}_j \rVert^2 + \lambda}$. Une feature exprimée dans une petite unité a de grands nombres, donc un grand $\lVert \mathbf{x}_j \rVert^2$ devant $\lambda$ : son facteur est presque 1, ridge ne la touche presque pas. Dans une grande unité, au contraire, elle est écrasée. Après standardisation, toutes les colonnes ont la même norme, et ridge les traite de la même façon, quelle que soit l'unité.

**Erreurs fréquentes.** Le facteur à l'envers (moindres carrés sur ridge) ; croire qu'une unité plus petite rend la feature plus pénalisée ; standardiser avec $\mathrm{ddof} = 1$ (le facteur devient $\frac{3}{5}$ : on peut le faire, mais ce n'est pas l'énoncé).

**Variante.** Le facteur de rétrécissement de $x_1$ mesuré en hectomètres ($1$ km $= 10$ hm), pour $\lambda = 2$ ? *Réponse* : la colonne vaut $10\,x_1$, $\lVert \cdot \rVert^2 = 1\,000$, et le facteur vaut $\frac{1\,000}{1\,002} \approx 0{,}998$.

### Ex M09b.22 — MML §5.5, §8.1 et §8.2 : identités de gradients et minimisation du risque empirique

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. Un modèle comme une **fonction** (un prédicteur qui associe une sortie à une entrée) et un modèle comme une **loi de probabilité** (qui dit aussi à quel point chaque sortie est plausible). La fiche §1 à §6 suit le premier point de vue ; le §7 (le maximum de vraisemblance) suit le second.
2. Une **classe d'hypothèses** (*hypothesis class*), par exemple les fonctions affines de paramètres $\boldsymbol{\theta}$. Le livre prend la loss quadratique, $(y_n - \hat{y}_n)^2$, et définit le risque empirique comme la moyenne des losses sur les $N$ exemples d'entraînement.
3. L'**overfitting** : un prédicteur trop flexible colle aux données d'entraînement et généralise mal. Le livre ajoute une pénalité sur la taille des paramètres, $\lambda\lVert \boldsymbol{\theta} \rVert^2$ : la régularisation de **Tikhonov**.
4. La **validation croisée** à $K$ parts : on découpe les données en $K$ morceaux, on entraîne sur $K - 1$ et l'on évalue sur le dernier, à tour de rôle, puis on moyenne les $K$ erreurs.
5. Le livre donne $\frac{\partial \mathbf{a}^\top\mathbf{x}}{\partial \mathbf{x}} = \mathbf{a}^\top$ et $\frac{\partial \mathbf{x}^\top\mathbf{B}\mathbf{x}}{\partial \mathbf{x}} = \mathbf{x}^\top(\mathbf{B} + \mathbf{B}^\top)$ : des vecteurs **lignes**, la transposée de ceux de la fiche. Il donne aussi une identité pour $(\mathbf{x} - \mathbf{A}\mathbf{s})^\top\mathbf{W}(\mathbf{x} - \mathbf{A}\mathbf{s})$ avec $\mathbf{W}$ symétrique ; avec $\mathbf{W} = \mathbf{I}$, c'est le gradient des moindres carrés de la fiche §2, écrit en ligne.
6. Par exemple : *empirical risk* (risque empirique), *hypothesis class* (classe d'hypothèses), *regularizer* (terme de régularisation), *cross-validation* (validation croisée), *overfitting* (le mot reste en anglais, comme dans workbookIA).

**Grille.** (1) les deux points de vue, reliés aux sections de la fiche ; (2) la classe d'hypothèses, la loss quadratique, le risque empirique comme moyenne ; (3) l'overfitting, la pénalité et le nom de Tikhonov ; (4) la validation croisée, en une phrase ; (5) les deux identités, la convention ligne/colonne ; (6) trois mots traduits. Les réponses sont écrites avec tes mots, pas recopiées.

### Ex M09b.23 — MML §9.1 et §9.2 : régression linéaire, maximum de vraisemblance et MAP

**Réponse modèle** (avec tes mots).
1. $y = f(\mathbf{x}) + \varepsilon$ avec un bruit gaussien $\varepsilon \sim \mathcal{N}(0, \sigma^2)$ ; pour un modèle linéaire, $p(y \mid \mathbf{x}, \boldsymbol{\theta}) = \mathcal{N}(y \mid \mathbf{x}^\top\boldsymbol{\theta}, \sigma^2)$. Les paramètres s'écrivent $\boldsymbol{\theta}$, la variance du bruit $\sigma^2$.
2. $\boldsymbol{\theta}_{\text{ML}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ (avec $\mathbf{X}$ de forme $(N, D)$) : la solution des équations normales, $\mathbf{w}$ dans la fiche.
3. On remplace $\mathbf{x}$ par un vecteur de features $\boldsymbol{\phi}(\mathbf{x})$, par exemple les puissances $1, x, \ldots, x^{K-1}$ ; le modèle reste linéaire en $\boldsymbol{\theta}$, et la solution s'écrit avec $\boldsymbol{\Phi}$, la **matrice des features** (*feature matrix*, ou *design matrix*), à la place de $\mathbf{X}$.
4. $\sigma^2_{\text{ML}} = \frac{1}{N}\sum_n (y_n - \boldsymbol{\phi}^\top(\mathbf{x}_n)\boldsymbol{\theta})^2$ : la somme des carrés des résidus divisée par $N$, comme $\hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$ (fiche §7).
5. Il ajuste des polynômes de degrés croissants et compare l'erreur d'entraînement et celle de données de test, avec la **RMSE** : l'erreur d'entraînement baisse toujours, celle de test remonte au-delà d'un certain degré.
6. Avec un prior $p(\boldsymbol{\theta}) = \mathcal{N}(\mathbf{0}, b^2\mathbf{I})$, $\boldsymbol{\theta}_{\text{MAP}} = (\boldsymbol{\Phi}^\top\boldsymbol{\Phi} + \frac{\sigma^2}{b^2}\mathbf{I})^{-1}\boldsymbol{\Phi}^\top\mathbf{y}$ : ce sont les moindres carrés régularisés, avec $\lambda = \frac{\sigma^2}{b^2}$ (notre $\frac{\sigma^2}{\tau^2}$).

**Grille.** (1) le modèle et les notations ; (2) la formule, traduite dans les notations de la fiche ; (3) les features et le nom de $\boldsymbol{\Phi}$ ; (4) l'estimation de $\sigma^2$, comparée ; (5) l'expérience des degrés et la RMSE ; (6) le MAP et $\lambda$ dans les deux notations.

### Ex M09b.24 — Fermi : la taille de XᵀX pour des features polynomiales de degré 3 sur 100 variables

**Réponse modèle.**
1. $\binom{103}{3} - 1 = 176\,850 \approx 1{,}8 \times 10^5$ colonnes.
2. $(1{,}8 \times 10^5)^2 \approx 3 \times 10^{10}$ nombres, soit environ $2{,}5 \times 10^{11}$ octets : **250 Go** (la moitié en ne gardant qu'un triangle, puisque la matrice est symétrique). La matrice $\mathbf{X}$ elle-même a $10^6 \times 1{,}8 \times 10^5 \approx 1{,}8 \times 10^{11}$ nombres, environ 1,4 To.
3. $n\,p^2 \approx 10^6 \times 3 \times 10^{10} = 3 \times 10^{16}$ multiplications (deux fois moins par symétrie).
4. $\frac{(1{,}8 \times 10^5)^3}{3} \approx 2 \times 10^{15}$ multiplications, environ 2 000 s, une demi-heure ; former $\mathbf{X}^\top\mathbf{X}$ prendrait, lui, environ $3 \times 10^4$ s, plus de 8 heures.
5. Ne pas former $\mathbf{X}^\top\mathbf{X}$ : une descente de gradient stochastique par mini-batches (workbookIA 19), qui ne garde que les poids ; garder le degré 2 ou choisir quelques interactions ; réduire d'abord la dimension (une ACP, M12d) ; passer par la matrice de Gram des exemples (M28), dont la taille dépend de $n$, pas du nombre de colonnes.

**Grille.** (1) le bon nombre de colonnes, sans la constante ou avec ; (2) le carré, puis les octets ; (3) $n\,p^2$ ; (4) $\frac{p^3}{3}$ et un temps ; (5) deux pistes justifiées.

### Ex M09b.25 — Expliquer la matrice chapeau : ce que veut dire « projeter y »

**Réponse modèle.**

> Range les $n$ cibles dans un seul vecteur : un point d'un espace à $n$ dimensions. Un modèle linéaire, quels que soient ses poids, produit aussi un vecteur de $n$ prédictions ; tous ceux qu'il peut produire forment un « plan » (un sous-espace) de cet espace, de dimension égale au nombre de colonnes. En général, le vecteur des cibles n'est pas dans ce plan : aucun choix de poids ne prédit tout exactement. Les moindres carrés cherchent le point du plan le plus proche des cibles, comme on cherche le point d'un sol le plus proche d'une lampe : c'est le pied de la perpendiculaire, et l'erreur restante (les résidus) est perpendiculaire au plan. La matrice chapeau est l'opération « prendre le pied de la perpendiculaire » : elle transforme les cibles en prédictions. L'appliquer une seconde fois ne change rien, car un point déjà dans le plan est son propre pied.

**Grille.** (1) les cibles comme un seul vecteur ; (2) les prédictions possibles comme un plan ; (3) le plus proche, le pied de la perpendiculaire, les résidus perpendiculaires ; (4) la matrice chapeau comme cette opération ; (5) pourquoi deux fois ne change rien ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M09b.E1 — « Pourquoi ne pas inverser XᵀX, et que faire si des features sont colinéaires ? »

**Réponse modèle (60 secondes).**

> On n'a jamais besoin de l'inverse : on veut résoudre $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$. Une élimination de Gauss (ou une factorisation de Cholesky, la matrice étant symétrique) le fait en moins d'opérations et avec moins d'erreurs d'arrondi qu'une inverse suivie d'un produit. Mieux encore, `lstsq` résout le problème sans même former $\mathbf{X}^\top\mathbf{X}$, par une factorisation de $\mathbf{X}$ : former ce produit élève le conditionnement au carré, et fait perdre deux fois plus de chiffres. Quand des features sont colinéaires, $\mathbf{X}^\top\mathbf{X}$ est singulière : il y a une infinité de solutions, toutes avec les mêmes prédictions, mais des poids arbitraires. Presque colinéaires, la solution existe mais est instable : les poids deviennent énormes et changent avec le moindre bruit. Remèdes : ridge, qui ajoute $\lambda$ sur la diagonale et rend le système toujours soluble ; retirer ou regrouper les features redondantes (le one-hot complet avec une colonne de 1, par exemple) ; prendre la solution de plus petite norme avec `lstsq` ; ou réduire la dimension avec une ACP.

**Grille.** (1) résoudre plutôt qu'inverser, avec la raison (coût, précision) ; (2) `lstsq` et le conditionnement au carré ; (3) colinéaires : une infinité de solutions, mêmes prédictions ; (4) presque colinéaires : des poids instables ; (5) deux remèdes au moins, dont ridge.

### M09b.E2 — « Quel lien entre la régularisation L2 et un prior gaussien ? »

**Réponse modèle (60 secondes).**

> On suppose que les cibles sont la prédiction linéaire plus un bruit gaussien de variance $\sigma^2$, et l'on met sur chaque poids un prior gaussien centré de variance $\tau^2$ : avant de voir les données, on croit que les poids sont petits. Le MAP maximise le posterior, c'est-à-dire la vraisemblance fois le prior. En prenant le log, la vraisemblance donne $-\frac{1}{2\sigma^2}$ fois la somme des carrés des résidus, et le prior $-\frac{1}{2\tau^2}$ fois la somme des carrés des poids. Maximiser revient donc à minimiser la somme des carrés plus $\frac{\sigma^2}{\tau^2}$ fois la norme au carré des poids : c'est exactement ridge, avec $\lambda = \frac{\sigma^2}{\tau^2}$. Un $\lambda$ grand veut dire un bruit fort, donc des données peu fiables, ou un prior étroit, une forte croyance que les poids sont petits. Avec un prior de Laplace, le log du prior est la somme des valeurs absolues : on obtient le lasso.

**Grille.** (1) le modèle de bruit et le prior ; (2) le MAP comme maximum du posterior ; (3) le passage au log et les deux termes ; (4) $\lambda = \frac{\sigma^2}{\tau^2}$ et son interprétation ; (5) le prior de Laplace et le lasso.

<a id="notebook"></a>

## Notebook

### Ex M09b.26 — Équations normales et résolution, avec ou sans ridge · `normal_equations, solve_least_squares`

**Réponses** : a) `[[4.0, 4.0], [4.0, 14.0]]` · b) `[11.0, 23.0]` · c) `[1.55, 1.2]` · d) `[1.05, 1.175]` · e) `"ValueError"` · f) `[0.1986, 0.3972]` · g) `"ValueError"` · h) `"ndarray"`.

**Démarche.** `X = np.array(X, dtype=float)` (une copie), une `ValueError` si `X.ndim != 2` ; `y = np.array(y, dtype=float)`, une `ValueError` si `y.ndim != 1` ou `y.size != X.shape[0]` ; `return X.T @ X, X.T @ y`. `solve_least_squares` : `ridge = float(ridge)` et une `ValueError` si `not ridge >= 0` (ce test refuse aussi `nan`) ; `XtX, Xty = normal_equations(X, y)` ; puis, dans un `try`, `np.linalg.solve(XtX + ridge * np.eye(XtX.shape[0]), Xty)`, et `except np.linalg.LinAlgError: raise ValueError(...)`. Pour la copie : c) $\frac{1}{40}\begin{pmatrix} 14 & -4 \\ -4 & 4 \end{pmatrix}\begin{pmatrix} 11 \\ 23 \end{pmatrix}$. e) La seconde colonne est le double de la première : $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 14 & 28 \\ 28 & 56 \end{pmatrix}$, de déterminant nul. f) Avec $\lambda > 0$, la matrice est inversible ; $\mathbf{X}^\top\mathbf{y} = (14, 28)$ est proportionnel à $(1, 2)$, comme chaque colonne de $\mathbf{X}^\top\mathbf{X}$, donc la solution aussi. Parmi toutes les solutions des moindres carrés ($w_1 + 2w_2 = 1$), ridge choisit un petit vecteur dans la direction $(1, 2)$.

**Erreurs fréquentes.** `ridge * np.ones(...)` au lieu de `np.eye` ; ne pas pénaliser la colonne de 1, contrairement à la docstring ; laisser passer la `LinAlgError` ; tester `ridge < 0` (qui laisse passer `nan`) ; modifier les tableaux reçus.

### Ex M09b.27 — La matrice chapeau et les trois sommes de carrés · `hat_matrix, residual_decomposition`

**Réponses** : a) `[0.7, 0.3, 0.3, 0.7]` · b) `2.0` · c) `[-0.1, 1.3, 2.7, 4.1]` · d) `[14.0, 9.8, 4.2]` · e) `0.7` · f) `"ValueError"` · g) `"float"` · h) `"ValueError"`.

**Démarche.** `hat_matrix` : la copie 2-D, puis `M = np.linalg.solve(X.T @ X, X.T)` dans un `try` (une `ValueError` sur `LinAlgError`), et `return X @ M`. `residual_decomposition` : les deux entrées en tableaux à une dimension (`.reshape(-1)`), une `ValueError` si les tailles diffèrent ou sont nulles, `m = y.mean()`, puis `float(np.sum((y - m) ** 2))`, `float(np.sum((y_hat - m) ** 2))`, `float(np.sum((y - y_hat) ** 2))`. Pour la copie : $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 4 & 6 \\ 6 & 14 \end{pmatrix}$ et $h_{ij} = \frac{14 - 6x_i - 6x_j + 4x_ix_j}{20}$. Les deux points extrêmes sont loin de la moyenne des abscisses : ils pèsent le plus sur leur propre prédiction. La droite ajustée est $\hat{y} = -0{,}1 + 1{,}4x$ ; $14 = 9{,}8 + 4{,}2$ est garanti par la colonne de 1 (fiche §3).

**Erreurs fréquentes.** `np.linalg.inv` (interdit, et inutile) ; `X.T @ np.linalg.solve(X.T @ X, X)` (des formes qui ne vont pas) ; centrer $\hat{\mathbf{y}}$ sur sa propre moyenne au lieu de celle de $\mathbf{y}$ ; rendre des `np.float64`.

### Ex M09b.28 — Compter les monômes, et la loss de Huber · `count_monomials, huber_loss`

**Réponses** : a) `83` · b) `84` · c) `0` · d) `46375` · e) `2.78625` · f) `0.025` · g) `"ValueError"` · h) `"int"`.

**Démarche.** `count_monomials` : les deux `ValueError`, puis `count = math.comb(p + degree, degree)` et `return int(count if include_constant else count - 1)`. `huber_loss` : `r = np.array(residuals, dtype=float).reshape(-1)`, une `ValueError` si `r.size == 0` ou si `not delta > 0`, puis `a = np.abs(r)`, `np.where(a <= delta, r ** 2 / 2, delta * (a - delta / 2))`, et la moyenne en `float`. Pour la copie : e) $1{,}125 + 0{,}02 + 4 + 6 = 11{,}145$, divisé par 4. c) Le seul monôme de degré 0 est la constante : sans elle, il n'en reste aucun. d) 46 375 colonnes, donc $\mathbf{X}^\top\mathbf{X}$ a environ $2{,}2 \times 10^9$ nombres (17 Go en `float64`).

**Erreurs fréquentes.** Une boucle sur les monômes (juste, mais très lente pour d) ; oublier `int(...)` (un `np.int64` si l'on passe par NumPy) ; la somme au lieu de la moyenne des losses ; `r ** 2` sans le facteur $\frac{1}{2}$.

### Ex M09b.29 — `np.linalg.lstsq` et scikit-learn contre tes équations normales

**Réponses** : a) `[3.1218, 0.3636, -1.2796]` · b) `[3.1218, 0.3636, -1.2796]` · c) `3` · d) `[3.0472, 0.3532, -1.2559]` · e) `[1.5892, 0.4663, -1.131]` · f) `True`.

**Démarche.** `w, _, rank, _ = np.linalg.lstsq(X1_29, y_29, rcond=None)` ; `LinearRegression().fit(X_29, y_29)` puis `[intercept_, *coef_]` ; de même avec `Ridge(alpha=5)` ; `mymath.linreg.solve_least_squares(X1_29, y_29, ridge=5)`. Pour f) : `mx, my = X_29.mean(axis=0), y_29.mean()`, `w = solve_least_squares(X_29 - mx, y_29 - my, ridge=5)`, `[my - mx @ w, *w]`, et `np.allclose(..., d, atol=1e-8)`. Pour la copie : a) et b) sont la même solution des moindres carrés ; `LinearRegression` ajoute la colonne de 1 lui-même. d) et e) diffèrent : `Ridge` ne pénalise pas l'ordonnée à l'origine, `solve_least_squares` la tire vers 0 (de 3,05 à 1,59), et les autres poids compensent. Après centrage, l'ordonnée à l'origine ne sert plus pendant la résolution, et on la retrouve ensuite : f). `lstsq` ne forme pas $\mathbf{X}^\top\mathbf{X}$, dont le conditionnement est le carré de celui de $\mathbf{X}$ (M09b.32).

**Erreurs fréquentes.** Oublier `rcond=None` (un avertissement) ; `coef_` seul, sans l'ordonnée à l'origine ; centrer `X1_29` avec sa colonne de 1 (qui devient nulle).

### Ex M09b.30 — Prédire : le R² d'entraînement quand on ajoute une feature de pur bruit

**Réponses** : a) `2` · b) `3` · c) `3`.

**Démarche.** a) Ajouter une colonne ne retire aucun modèle possible : le poids 0 sur la nouvelle colonne redonne l'ancien ajustement. Le minimum de la somme des carrés ne peut que baisser ou rester égal, et le $R^2$ d'entraînement monter. b) Avec 18 colonnes de bruit, $\mathbf{X}$ a $1 + 1 + 18 = 20$ colonnes pour 20 exemples : carrée, inversible pour un tirage au hasard ; $\mathbf{X}\mathbf{w} = \mathbf{y}$ a une solution exacte, les résidus sont nuls et $R^2 = 1$. c) Les poids des colonnes de bruit ont appris le bruit des 20 exemples : sur de nouvelles données, ils ajoutent des erreurs, et le $R^2$ de test devient négatif (environ $-2$ dans l'expérience). C'est la variance (fiche §8). Un $R^2$ d'entraînement ne permet pas de comparer des modèles qui n'ont pas le même nombre de colonnes.

### Ex M09b.31 — Simuler l'estimateur rétréci c·x̄ : le c qui minimise l'erreur quadratique

**Réponses** : a) `True` · b) `True` · c) `0.3571` · d) `2.8`.

**Démarche.** `rng = np.random.default_rng(seed)`, `means = rng.normal(mu, sigma, size=(reps, n)).mean(axis=1)` **une seule fois**, puis `np.array([np.mean((c * means - mu) ** 2) for c in cs])`. `formula_mse` : `(c - 1) ** 2 * mu ** 2 + c ** 2 * sigma ** 2 / n`. Pour la copie : $c^* = \frac{1}{1 + 9/5} = \frac{5}{14} \approx 0{,}357$ ; $E(c^*) = c^*\frac{\sigma^2}{n} \approx 0{,}643$, contre $E(1) = 1{,}8$ : 2,8 fois moins. Le rétrécissement paie quand la variance $\frac{\sigma^2}{n}$ de $\bar{x}$ est grande devant $\mu^2$. C'est ce que fait ridge sur des poids : un peu de biais contre beaucoup moins de variance.

**Erreurs fréquentes.** Tirer de nouveaux échantillons pour chaque $c$ (la courbe devient bruitée, et son minimum saute) ; la forme `(n, reps)` avec une moyenne sur le mauvais axe ; $\sigma$ au lieu de $\sigma^2$ dans la formule.

### Ex M09b.32 — Le conditionnement de XᵀX avec des puissances non standardisées

**Réponses** : a) `14` · b) `3` · c) `6` · d) `True`.

**Démarche.** `np.column_stack([x ** k for k in range(degree + 1)])`, puis `float(np.linalg.cond(X.T @ X))`. Pour la copie : sur $[0, 20]$, les colonnes $x^4$ et $x^5$ pointent presque dans la même direction (fiche §4) : $\mathbf{X}^\top\mathbf{X}$ est presque singulière, avec un conditionnement d'environ $5 \times 10^{13}$ au degré 5 et $4 \times 10^{16}$ au degré 6. Ramener l'abscisse à $[-1, 1]$ le fait tomber à $2 \times 10^3$. Dans l'expérience, une modification des cibles de $10^{-8}$ change les poids bruts de $5 \times 10^{-6}$ en valeur relative, plus de cent fois plus qu'avec l'abscisse ramenée à $[-1, 1]$, mais les prédictions de moins de $10^{-8}$ dans les deux cas : beaucoup de combinaisons de colonnes presque dépendantes donnent presque les mêmes prédictions. C'est grave quand on lit les poids, quand on extrapole, ou quand le conditionnement atteint $10^{16}$ : `solve` peut alors rendre n'importe quoi.

**Erreurs fréquentes.** Le conditionnement de $\mathbf{X}$ (environ la racine) au lieu de celui de $\mathbf{X}^\top\mathbf{X}$ ; commencer les puissances à 1 au lieu de 0 (pas de colonne de 1).

### Ex M09b.33 — Les lignes de niveau de la loss des moindres carrés en dimension 2, et son gradient

**Démarche.** Une grille de poids `W0, W1 = np.meshgrid(...)` ; $L$ sur la grille, sans boucle : `residuals = y[None, None, :] - (W0[..., None] * X[:, 0] + W1[..., None] * X[:, 1])`, puis `np.sum(residuals ** 2, axis=-1)` ; le minimum par les équations normales ; `ax.contour(W0, W1, L, levels=L_min + np.geomspace(0.05, 50, 10))` ; `ax.plot(w0, w1, "*")` ; enfin, sur une grille de $6 \times 6$ points, les vecteurs $2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ et `ax.quiver(..., angles="xy")`. Pour la copie : $L$ est un polynôme du second degré en $(w_0, w_1)$, de partie quadratique $\mathbf{w}^\top\mathbf{X}^\top\mathbf{X}\mathbf{w}$ : ses lignes de niveau sont des ellipses centrées au minimum $(0{,}6 ;\ 0{,}8)$. Avec $x$ brut, $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 5 & 15 \\ 15 & 55 \end{pmatrix}$ a un terme croisé : les ellipses sont penchées, et très allongées (le rapport de leurs axes est d'environ 8). Avec $x$ centré, $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 5 & 0 \\ 0 & 10 \end{pmatrix}$ : les axes des ellipses sont ceux du repère, et le minimum devient $(3 ;\ 0{,}8)$, la même pente. Les flèches sont perpendiculaires aux lignes de niveau, pas dirigées vers le minimum : dans une vallée étroite, une descente de gradient zigzague d'un bord à l'autre et avance lentement (M19). Centrer et standardiser arrondit la vallée.

**Erreurs fréquentes.** Des niveaux réguliers (`levels=10`) : presque toutes les lignes tombent loin du minimum, et la vallée ne se voit pas ; les flèches de $+\nabla L$ (vers le haut) ; `ax.quiver` sans `angles="xy"`, qui déforme les directions quand les axes n'ont pas la même échelle.

### Ex M09b.34 — Chasse à l'erreur : XXᵀ au lieu de XᵀX, un gradient de mauvais signe, un R² sans centrer

**Réponses** : a) `"ACE"` · b) `[1.0, 1.0, -5.0, 1.0, 0.5179, 0.75]`.

**Démarche.** (A) `X @ X.T` est de forme $(3, 3)$, la matrice des produits scalaires des exemples, et son élément $(1, 2)$ existe, d'où l'absence d'erreur ; $\mathbf{X}^\top\mathbf{X}$ s'écrit `X.T @ X`, et son élément $(1, 2)$ vaut $\sum_i x_i = 1$. (B) Juste : $\hat{\mathbf{y}} = (2 ;\ 0{,}5 ;\ 1)$, $r_1 = 1$. (C) Il manque le signe moins : $-2\mathbf{X}^\top\mathbf{r} = -2(1{,}5 ;\ 2{,}5) = (-3, -5)$. (D) Juste : $\mathbf{w} - \eta\nabla L = \mathbf{w} + 2\eta\mathbf{X}^\top\mathbf{r}$, et $0{,}5 + 0{,}2 \times 2{,}5 = 1$. (E) $\sum y_i^2 = 13$ compare à la prédiction 0 ; avec $\bar{y} = \frac{5}{3}$, $\mathrm{SCT} = \frac{42}{9}$ et $R^2 = 1 - \frac{2{,}25}{42/9} \approx 0{,}5179$, au lieu de $0{,}8269$. (F) Juste : $\frac{2{,}25}{3}$.

**Erreurs fréquentes.** Citer (D) : ajouter n'est pas une erreur quand le gradient a déjà son signe moins dans $-2\mathbf{X}^\top\mathbf{r}$ ; ne pas voir (A), qui s'exécute sans erreur.

### Ex M09b.35 — Vérifier un gradient matriciel avec SymPy et par différences finies

**Démarche.** `numerical_gradient` : pour chaque $k$, un vecteur `step` nul sauf `step[k] = h`, puis `(f(w + step) - f(w - step)) / (2 * h)`. `gradient_error` : `approx = numerical_gradient(f, w)`, puis `np.max(np.abs(approx - grad(w))) / max(1.0, np.max(np.abs(approx)))`. `symbolic_check` : `w = sympy.Matrix(sympy.symbols(f"w1:{p + 1}"))`, `A = sympy.Matrix(p, p, sympy.symbols(f"a1:{p * p + 1}"))`, `f = (w.T * A * w)[0, 0]`, le gradient par `sympy.diff` sur chaque $w_k$, et `bool(sympy.expand(gradient - (A + A.T) * w) == sympy.zeros(p, 1))`. Pour la copie : la différence centrée a une erreur d'ordre $h^2$ (les termes en $h$ du développement de Taylor se compensent, M05a), contre $h$ pour la différence avant. Un $h$ trop petit fait perdre des chiffres : les deux valeurs de $f$ sont presque égales, et leur différence est dominée par les arrondis (environ $\frac{10^{-16}}{h}$). Diviser par la taille du gradient rend la mesure indépendante de l'échelle de $f$. Un gradient numérique coûte $2p$ évaluations de $f$ : pour un réseau à un million de poids, deux millions de passes avant par pas, alors que la rétropropagation (M18) donne le gradient exact pour environ le coût de deux passes.

**Erreurs fréquentes.** Modifier `w` en place sans le rétablir ; un pas `h` entier sur un tableau d'entiers (`np.zeros_like` d'un tableau d'entiers) ; comparer des expressions SymPy sans les développer.

### Ex M09b.36 — Défi : approcher une fonction par un polynôme de degré au plus 5, avec une erreur maximale sous 1e−3

**Réponse** : `True`.

**Démarche.** Les moindres carrés sur les 4 001 points de la grille donnent une erreur maximale d'environ $1{,}3 \times 10^{-3}$, atteinte en $x = 0$ : ils minimisent la **somme** des carrés, où les bords comptent peu, et l'erreur s'y concentre. Il faut donner plus de poids aux bords : des points plus serrés près de $t = -1$ et $t = 1$, comme les **points de Tchebychev** $t_k = \cos\frac{(2k + 1)\pi}{2m}$ (30 points donnent environ $5{,}8 \times 10^{-4}$) ; ou des poids plus grands près des bords (multiplier les lignes de $\mathbf{X}$ et de $\mathbf{y}$ par $\sqrt{\text{poids}}$) ; ou des passes successives qui augmentent le poids des points mal approchés. Curieusement, **moins** de points uniformes marchent aussi : 11 points donnent environ $8{,}5 \times 10^{-4}$, car chaque bord pèse alors plus lourd dans la somme. Pour la copie : un degré 4 ne suffit pas, même le meilleur polynôme de degré 4 a une erreur maximale d'environ $1{,}7 \times 10^{-3}$ ; en degré 5, la meilleure erreur maximale possible est d'environ $4{,}6 \times 10^{-4}$ (le polynôme « minimax », que des passes successives approchent).

**Erreurs fréquentes.** Les puissances de $x$ au lieu de $t$ (le défi demande les coefficients en $t$, et `evaluate_36` les lit ainsi) ; ajouter des points uniformes (l'erreur maximale ne baisse pas : elle remonte un peu) ; un degré 6 (refusé : 7 coefficients).
