# CP2 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Barème par sous-question**, entre crochets ; sauf mention contraire, une sous-question vaut 0,25 point. Une justification demandée « sur ta copie » compte dans la sous-question à laquelle elle se rattache.
- **Crédit partiel** sur une sous-question de 0,25 point : 0,1 pour une réponse juste sans la démarche demandée, ou pour une méthode juste avec une erreur de calcul. **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois (par exemple des poids faux en CP2.5 c, réutilisés en d) et e), ou des coefficients faux en CP2.11 b, réutilisés en c) à f)).
- **Arrondis** : une décimale de moins coûte au plus 0,05 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi. Des décimales en plus ne coûtent rien (le notebook les accepte).
- **Questions rédigées** (CP2.Q1, CP2.9, CP2.10 b, les phrases demandées « sur ta copie ») : les critères sont listés ; une idée juste formulée autrement compte autant.
- **Logarithmes** : $\ln$ est le logarithme népérien (`math.log` en Python) ; les AIC, BIC et bornes de Hoeffding l'utilisent tous.

---

## CP2.Q1 — Dix affirmations sur la partie II 🧠 · 1,5 point

Chaque affirmation : **[0,05]** pour le verdict, **[0,1]** pour une justification juste (0,05 si elle est incomplète).

**a) Vrai** (M07). $\lVert \mathbf{u} \pm \mathbf{v} \rVert^2 = \lVert \mathbf{u} \rVert^2 \pm 2\,\mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{v} \rVert^2$ ; avec $\mathbf{u} \cdot \mathbf{v} = 0$, les deux valent $\lVert \mathbf{u} \rVert^2 + \lVert \mathbf{v} \rVert^2$ (Pythagore). Les deux diagonales d'un rectangle ont la même longueur.

**b) Faux** (M07). $(1, 0)$ et $(0, 1)$ ont un cosinus nul ; en leur ajoutant $(1, 1)$, on obtient $(2, 1)$ et $(1, 2)$, de cosinus $\frac{2 + 2}{\sqrt{5}\,\sqrt{5}} = 0{,}8$. Le cosinus mesure l'angle vu depuis l'origine : une translation le change (la distance entre les deux points, elle, ne change pas).

**c) Faux** (M08). Il y a $\binom{8}{2} = 28$ façons de choisir les 2 mesures du petit groupe parmi les 8, équiprobables sous $H_0$. La répartition observée compte toujours parmi celles « au moins aussi extrêmes » qu'elle : la p-valeur vaut au moins $\frac{1}{28} \approx 0{,}036$. Avec si peu de mesures, aucun test de ce type ne peut descendre à 0,01.

**d) Vrai** (M08). Les tests sont indépendants et chacun ne se trompe pas avec la probabilité 0,95 : $P(\text{aucun faux positif}) = 0{,}95^{15} \approx 0{,}463$, donc $P(\text{au moins un}) \approx 0{,}537 > \frac{1}{2}$.

**e) Vrai** (M09a). Le système homogène a toujours la solution $\mathbf{0}$, et le rang de $\mathbf{A}$ est au plus 3 (trois lignes) pour 4 inconnues : il reste au moins une inconnue libre, donc une infinité de solutions.

**f) Vrai** (M09a). Par exemple $x = 1$, $y = 2$, $z = 3$, $x + y = 3$, $y + z = 5$ : les trois premières équations fixent $x$, $y$ et $z$, et les deux autres sont vérifiées par ce triplet. Un système qui a plus d'équations que d'inconnues n'a en général **aucune** solution, mais il en a une seule quand il est compatible et de rang égal au nombre d'inconnues.

**g) Vrai** (M09b). Le modèle est **linéaire en ses poids** : avec les colonnes $1$, $\sqrt{x_i}$ et $2^{x_i}$, il s'écrit $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w}$, et les moindres carrés donnent les équations normales $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, un système $3 \times 3$ (de solution unique si les trois colonnes sont indépendantes). Que les features soient des fonctions non linéaires de $x$ ne change rien, comme pour les features polynomiales.

**h) Faux** (M09b). Il y a $\binom{p + d}{d} = \binom{6}{2} = 15$ monômes de degré au plus 2 en 4 variables : la constante, 4 termes de degré 1, et 10 de degré 2 (4 carrés et 6 produits croisés).

**i) Faux** (M10). $(0, 0)$ et $(4, 2)$ y sont ($0 \ge \sqrt{0}$ et $2 \ge \sqrt{4}$), mais pas le milieu du segment qui les joint, $(2, 1)$, car $1 < \sqrt{2} \approx 1{,}414$. La région au-dessus de la courbe d'une fonction **concave** se creuse : elle n'est pas convexe (c'est la région au-dessus d'une fonction convexe qui l'est).

**j) Faux** (M11). Markov : $P(X \ge 10) \le \frac{\mathbb{E}[X]}{10} = 0{,}2 < 0{,}25$.

**Erreurs fréquentes** : en b), confondre cosinus et distance ; en c), oublier que la répartition observée compte dans la p-valeur ; en d), multiplier $15 \times 0{,}05 = 0{,}75$ (c'est la borne de l'union, pas la probabilité) ; en e), confondre avec $\mathbf{A}\mathbf{x} = \mathbf{b}$, qui peut n'avoir aucune solution ; en f), répondre « jamais » ; en g), croire qu'un modèle non linéaire en $x$ échappe aux moindres carrés ; en i), confondre fonction concave et fonction convexe ; en h), oublier la constante ou les produits croisés.
**Remédiation** : a) M07.2 ; b) M07.4 ; c) M08.2 ; d) M08.7 ; e) et f) M09a.9, M09a.13 ; g) et h) M09b.4, M09b.7 ; i) M10.1 ; j) M11.5.

## CP2.1 — Normes, cosinus, projection et distance à un hyperplan ✏️ · 1,75 point

**Réponses** : a) `[10, 6, 5]` · b) `7` · c) `0.255` · d) `[0.58, -0.19, 0.19, 0.97]` · e) `4.432` · f) `-2.0` · g) `[2.44, 0.11, 4.11, 2.33]`.

a) $\lVert \mathbf{u} \rVert_1 = 3 + 1 + 1 + 5 = 10$ ; $\lVert \mathbf{u} \rVert_2 = \sqrt{9 + 1 + 1 + 25} = 6$ ; $\lVert \mathbf{u} \rVert_\infty = 5$. **[0,25]**
b) $\mathbf{u} \cdot \mathbf{v} = 6 - 4 + 0 + 5 = 7$. **[0,25]**
c) $\lVert \mathbf{v} \rVert = \sqrt{4 + 16 + 0 + 1} = \sqrt{21}$, donc $\cos = \frac{7}{6\sqrt{21}} \approx 0{,}255$. **[0,25]**
d) $\frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert^2}\,\mathbf{u} = \frac{7}{36}\,\mathbf{u} \approx (0{,}58 ;\ -0{,}19 ;\ 0{,}19 ;\ 0{,}97)$. **[0,25]**
e) Par Pythagore, $\lVert \mathbf{v} - \mathbf{p} \rVert^2 = \lVert \mathbf{v} \rVert^2 - \lVert \mathbf{p} \rVert^2 = 21 - \frac{49}{36} \approx 19{,}6389$, donc la distance vaut $\approx 4{,}432$. **[0,25]**
f) $\mathbf{w} \cdot P + b = 4 - 4 + 15 + 6 - 39 = -18$ et $\lVert \mathbf{w} \rVert = \sqrt{4 + 16 + 25 + 36} = 9$ : la distance signée vaut $\frac{-18}{9} = -2$ ; $P$ est du côté où $\mathbf{w} \cdot \mathbf{x} + b < 0$. **[0,25]**
g) $P$ est à la distance 2 du côté négatif : on avance de 2 dans le sens du vecteur unitaire $\frac{\mathbf{w}}{9}$, soit $P - \frac{-18}{81}\,\mathbf{w} = P + \frac{2}{9}\,\mathbf{w} \approx (2{,}44 ;\ 0{,}11 ;\ 4{,}11 ;\ 2{,}33)$. Vérification : $2 \times \frac{22}{9} - 4 \times \frac{1}{9} + 5 \times \frac{37}{9} + 6 \times \frac{21}{9} = \frac{44 - 4 + 185 + 126}{9} = 39$, le point est bien sur $H$. **[0,25]**

**Erreurs fréquentes** : en a), additionner les coordonnées avec leur signe (8) ou oublier la racine (36) ; en c), diviser par $\lVert \mathbf{u} \rVert^2$ ; en d), diviser par $\lVert \mathbf{u} \rVert$ au lieu de $\lVert \mathbf{u} \rVert^2$, ou projeter $\mathbf{u}$ sur $\mathbf{v}$ ; en f), diviser par $\lVert \mathbf{w} \rVert^2$, perdre le signe, ou oublier le signe de $b$ ; en g), reculer au lieu d'avancer.
**Remédiation** : M07.3, M07.4, M07.5, M07.6, M07.17.

## CP2.2 — Un test binomial et un intervalle de Wilson ✏️ · 1,75 point

**Réponses** : a) `0.0022` · b) `0.0044` · c) `True` · d) `14` · e) `[0.624, 0.945]` · f) `1.006`.

Sous $H_0$, $K$ suit la loi binomiale $\mathcal{B}(19 ;\ \frac{1}{2})$ : $P(K = j) = \binom{19}{j}\,2^{-19}$, avec $2^{19} = 524\,288$, $\binom{19}{13} = 27\,132$, $\binom{19}{14} = 11\,628$, $\binom{19}{15} = 3\,876$, $\binom{19}{16} = 969$, $\binom{19}{17} = 171$, $\binom{19}{18} = 19$, $\binom{19}{19} = 1$.

a) $P(K \ge 16) = \frac{969 + 171 + 19 + 1}{524\,288} = \frac{1\,160}{524\,288} \approx 0{,}0022$. **[0,25]**
b) La loi est symétrique autour de 9,5 : le côté opposé, $P(K \le 3)$, a la même probabilité, et la p-valeur bilatérale vaut $2 \times 0{,}0022125 \approx 0{,}0044$. **[0,25]**
c) **Vrai** : $0{,}0044 \le 0{,}05$, on rejette $H_0$ au seuil de 5 %. **[0,25]**
d) $P(K \ge 13) = \frac{27\,132 + 11\,628 + 3\,876 + 1\,160}{524\,288} = \frac{43\,796}{524\,288} \approx 0{,}0835 > 0{,}05$, alors que $P(K \ge 14) = \frac{16\,664}{524\,288} \approx 0{,}0318 \le 0{,}05$ : il faut au moins **14** parties gagnantes. **[0,25]**
e) $\hat{p} = \frac{16}{19} \approx 0{,}842105$, $z^2 = 3{,}8416$, $\frac{z^2}{n} \approx 0{,}202189$. Centre : $\frac{\hat{p} + z^2/(2n)}{1 + z^2/n} \approx \frac{0{,}943200}{1{,}202189} \approx 0{,}784569$ ; demi-largeur : $\frac{z}{1 + z^2/n}\sqrt{\frac{\hat{p}(1 - \hat{p})}{n} + \frac{z^2}{4n^2}} \approx 1{,}630349 \times \sqrt{0{,}0069981 + 0{,}0026604} \approx 1{,}630349 \times 0{,}098278 \approx 0{,}160227$. Intervalle : $[0{,}624 ;\ 0{,}945]$. **[0,5]**
f) $\hat{p} + 1{,}96\sqrt{\frac{\hat{p}(1 - \hat{p})}{19}} \approx 0{,}842105 + 1{,}96 \times 0{,}083655 \approx 1{,}006$. **[0,25]**

Sur la copie, pour f) : une probabilité ne dépasse pas 1, et l'intervalle de Wald la fait pourtant monter à 1,006. Avec peu d'observations et une proportion loin de $\frac{1}{2}$, l'approximation normale centrée sur $\hat{p}$ est mauvaise ; l'intervalle de Wilson, obtenu en inversant le test de la proportion, reste dans $[0 ; 1]$ et couvre mieux la vraie valeur. Les deux conclusions concordent : $\frac{1}{2}$ n'est pas dans l'intervalle de Wilson, comme le test l'a dit.

**Erreurs fréquentes** : en a), ne compter que $K = 16$, ou que $K > 16$, ou oublier les coefficients binomiaux ; en b), donner l'unilatérale, ou la diviser par 2 ; en d), répondre 13 sans calculer $P(K \ge 13)$ ; en e), donner l'intervalle de Wald, ou arrondir trop tôt sous la racine ; en f), couper la borne à 1.
**Remédiation** : M08.1, M08.3, M08.5, M08.12.

## CP2.3 — Comparaisons multiples, AIC et BIC ✏️ · 1,5 point

**Réponses** : a) `7` · b) `2` · c) `0.087` · d) `[408.8, 402.0, 397.8]` · e) `[415.1, 412.5, 414.6]` · f) `[3, 2]`.

a) Sept p-valeurs sont au plus 0,05 : de 0,0021 à 0,047 ; la suivante, 0,058, dépasse le seuil. **[0,25]**
b) Bonferroni compare chaque p-valeur à $\frac{0{,}05}{14} \approx 0{,}00357$ : seules 0,0021 et 0,0034 passent. **[0,25]**
c) $\min(1,\ 14 \times 0{,}0062) = 0{,}0868 \approx 0{,}087$ : plus grande que 0,05, cette question n'est plus significative après correction. **[0,25]**
d) $\mathrm{AIC} = 2k - 2\ln L$ : $6 + 402{,}8 = 408{,}8$ ; $10 + 392{,}0 = 402{,}0$ ; $16 + 381{,}8 = 397{,}8$. **[0,25]**
e) $\mathrm{BIC} = k \ln n - 2\ln L$, avec $\ln 60 \approx 4{,}09434$ : $12{,}283 + 402{,}8 \approx 415{,}1$ ; $20{,}472 + 392{,}0 \approx 412{,}5$ ; $32{,}755 + 381{,}8 \approx 414{,}6$. **[0,25]**
f) Le plus petit AIC est celui du modèle 3, le plus petit BIC celui du modèle 2 : `[3, 2]`. Du modèle 2 au modèle 3, $\ln L$ gagne 5,1, soit 10,2 sur $-2\ln L$, pour trois paramètres de plus : assez pour l'AIC (pénalité $2 \times 3 = 6$), pas pour le BIC (pénalité $3 \ln 60 \approx 12{,}3$). **[0,25]**

**Erreurs fréquentes** : en a), oublier 0,047 ou compter 0,058 ; en b), ne pas corriger, ou changer de seuil selon le rang ; en c), diviser la p-valeur au lieu de la multiplier, ou multiplier par le rang ; en d) et e), oublier le facteur $-2$ ou prendre $\log_{10}$ ; en f), retenir le plus **grand** critère.
**Remédiation** : M08.7, M08.8, M08.11.

## CP2.4 — Pivot de Gauss, rang et inverse ✏️ · 1,75 point

**Réponses** : a) `[0, 3, 7, 4]` · b) `[0, 0, 10, 10]` · c) `[2, -1, 1]` · d) `[[2, -2.5], [-1, 1.5]]` · e) `[-3, 2]` · f) `2` · g) `4`.

a) $L_2 \leftarrow L_2 - 3L_1$ donne $(0, 1, -1 \mid -2)$ ; $L_3 \leftarrow L_3 + 2L_1$ donne $(0, 3, 7 \mid 4)$. **[0,25]**
b) $L_3 \leftarrow L_3 - 3L_2$ : $(0, 3 - 3, 7 + 3 \mid 4 + 6) = (0, 0, 10 \mid 10)$. **[0,25]**
c) Remontée : $10z = 10$, donc $z = 1$ ; $y - z = -2$, donc $y = -1$ ; $x + y + 2z = 3$, donc $x = 2$. Vérification dans la troisième équation : $-4 - 1 + 3 = -2$. **[0,25]**
d) $\det \mathbf{B} = 3 \times 4 - 5 \times 2 = 2$, et $\mathbf{B}^{-1} = \frac{1}{2}\begin{pmatrix} 4 & -5 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -2{,}5 \\ -1 & 1{,}5 \end{pmatrix}$ ; on vérifie $\mathbf{B}\mathbf{B}^{-1} = \mathbf{I}$. **[0,25]**
e) $\mathbf{x} = \mathbf{B}^{-1}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 - 5 \\ -1 + 3 \end{pmatrix} = \begin{pmatrix} -3 \\ 2 \end{pmatrix}$ ; vérification : $3 \times (-3) + 5 \times 2 = 1$ et $2 \times (-3) + 4 \times 2 = 2$. **[0,25]**
f) La troisième ligne est la somme des deux premières ($1 + 2 = 3$, $2 + 4 = 6$, $0 + 1 = 1$, $3 + 7 = 10$), et les deux premières ne sont pas proportionnelles : le rang vaut 2. Par le pivot : $L_2 \leftarrow L_2 - 2L_1$ et $L_3 \leftarrow L_3 - 3L_1$ donnent $(0, 0, 1, 1)$ deux fois, puis une ligne nulle. **[0,25]**
g) Les membres de gauche sont proportionnels quand $\frac{2}{1} = \frac{k}{2}$, soit $k = 4$ ; le système devient $x + 2y = 3$ et $2x + 4y = 7$, c'est-à-dire $x + 2y = 3{,}5$ : contradictoire, aucune solution. Pour $k \ne 4$, le déterminant $k - 4$ n'est pas nul et la solution est unique. **[0,25]**

**Erreurs fréquentes** : en a), retrancher $2L_1$ au lieu de l'ajouter, ou oublier le second membre ; en b), ajouter $3L_2$ ; en d), oublier de diviser par le déterminant, transposer, ou oublier un changement de signe ; en e), calculer $\mathbf{B}\,(1, 2)$ au lieu de $\mathbf{B}^{-1}(1, 2)$ ; en f), répondre 3 parce qu'il y a trois lignes.
**Remédiation** : M09a.8, M09a.9, M09a.10, M09a.11, M09a.13.

## CP2.5 — Les équations normales d'un petit modèle, avec et sans ridge ✏️ · 1,75 point

**Réponses** : a) `[[6, 3], [3, 6]]` · b) `[11, 14]` · c) `[0.8889, 1.8889]` · d) `[1.1111, 0.2222, 0.2222, -0.6667]` · e) `1.7778` · f) `[0.7917, 1.2917]` · g) `[2.375, 3.875]`.

a) $\mathbf{X}^\top\mathbf{X}$ a pour coefficients les produits scalaires des colonnes : $1 + 1 + 0 + 4 = 6$, $0 + 1 + 0 + 2 = 3$, $0 + 1 + 4 + 1 = 6$. **[0,25]**
b) $\mathbf{X}^\top\mathbf{y} = (2 + 3 + 0 + 6 ;\ 0 + 3 + 8 + 3) = (11 ;\ 14)$. **[0,25]**
c) $\det = 36 - 9 = 27$, $(\mathbf{X}^\top\mathbf{X})^{-1} = \frac{1}{27}\begin{pmatrix} 6 & -3 \\ -3 & 6 \end{pmatrix}$, donc $\mathbf{w} = \frac{1}{27}(66 - 42 ;\ -33 + 84) = \left(\frac{8}{9} ;\ \frac{17}{9}\right) \approx (0{,}8889 ;\ 1{,}8889)$. **[0,25]**
d) $\mathbf{X}\mathbf{w} = \left(\frac{8}{9} ;\ \frac{25}{9} ;\ \frac{34}{9} ;\ \frac{33}{9}\right)$, donc $\mathbf{r} = \left(\frac{10}{9} ;\ \frac{2}{9} ;\ \frac{2}{9} ;\ -\frac{6}{9}\right)$. Sur la copie : $\mathbf{X}^\top\mathbf{r} = \left(\frac{10 + 2 + 0 - 12}{9} ;\ \frac{0 + 2 + 4 - 6}{9}\right) = (0 ;\ 0)$, comme le disent les équations normales. **[0,25]**
e) $\frac{100 + 4 + 4 + 36}{81} = \frac{144}{81} = \frac{16}{9} \approx 1{,}7778$. **[0,25]**
f) $\mathbf{X}^\top\mathbf{X} + 3\mathbf{I} = \begin{pmatrix} 9 & 3 \\ 3 & 9 \end{pmatrix}$, de déterminant 72 : $\mathbf{w}_{\text{ridge}} = \frac{1}{72}(99 - 42 ;\ -33 + 126) = \left(\frac{19}{24} ;\ \frac{31}{24}\right) \approx (0{,}7917 ;\ 1{,}2917)$. **[0,25]**
g) Les résidus du modèle ridge valent $\mathbf{y} - \mathbf{X}\mathbf{w}_{\text{ridge}} = (1{,}2083 ;\ 0{,}9167 ;\ 1{,}4167 ;\ 0{,}125)$, et $\mathbf{X}^\top$ fois ce vecteur donne $(1{,}2083 + 0{,}9167 + 0 + 0{,}25 ;\ 0 + 0{,}9167 + 2{,}8333 + 0{,}125) = (2{,}375 ;\ 3{,}875)$. Sur la copie : ce vecteur n'est pas nul, et c'est exactement $3 \times \left(\frac{19}{24} ;\ \frac{31}{24}\right) = \lambda\,\mathbf{w}_{\text{ridge}}$. En effet, $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$ se réécrit $\mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \lambda\,\mathbf{w}$, soit $\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w}) = \lambda\,\mathbf{w}$ : le résidu de ridge n'est plus orthogonal aux colonnes, l'écart est $\lambda\,\mathbf{w}$ (pour $\lambda = 0$, on retrouve $\mathbf{X}^\top\mathbf{r} = \mathbf{0}$ des moindres carrés). **[0,25]**

**Erreurs fréquentes** : en a), calculer $\mathbf{X}\mathbf{X}^\top$ (une matrice $4 \times 4$) ; en c), oublier de diviser par le déterminant ; en d), écrire $\mathbf{X}\mathbf{w} - \mathbf{y}$ ; en f), ajouter $\lambda$ à tous les coefficients au lieu de la diagonale seule, ou $2\lambda$ sur la diagonale ; en g), prendre les poids des moindres carrés (on trouve alors $\mathbf{0}$).
**Remédiation** : M09b.4, M09b.5, M09b.8, M09b.15.

## CP2.6 — Biais, variance et erreur quadratique d'un estimateur ✏️ · 1,5 point

**Réponses** : a) `0.06` · b) `0.0128` · c) `0.0164` · d) `0.02` · e) `0.0119` · f) `1`.

$K$ suit la loi binomiale $\mathcal{B}(8 ;\ p)$ : $\mathbb{E}[K] = 8p$ et $\mathbb{V}(K) = 8p(1 - p)$.

a) $\mathbb{E}[\tilde{p}] = \frac{8p + 1}{10}$ ; pour $p = 0{,}2$, $\frac{2{,}6}{10} = 0{,}26$, donc le biais vaut $0{,}26 - 0{,}2 = 0{,}06$. **[0,25]**
b) $\mathbb{V}(\tilde{p}) = \frac{\mathbb{V}(K + 1)}{10^2} = \frac{\mathbb{V}(K)}{100} = \frac{8 \times 0{,}2 \times 0{,}8}{100} = 0{,}0128$ (ajouter 1 ne change pas la variance ; diviser par 10 la divise par 100). **[0,25]**
c) $\mathrm{EQM} = \text{biais}^2 + \text{variance} = 0{,}0036 + 0{,}0128 = 0{,}0164$. **[0,25]**
d) $\hat{p}$ est sans biais, et $\mathbb{V}(\hat{p}) = \frac{p(1 - p)}{8} = 0{,}02$. **[0,25]**
e) Pour $p = 0{,}05$ : $\mathbb{E}[\tilde{p}] = \frac{1{,}4}{10} = 0{,}14$, biais $0{,}09$, variance $\frac{8 \times 0{,}05 \times 0{,}95}{100} = 0{,}0038$, donc $\mathrm{EQM} = 0{,}0081 + 0{,}0038 = 0{,}0119$. **[0,25]**
f) Pour $p = 0{,}05$, $\hat{p}$ a une erreur quadratique $\frac{0{,}05 \times 0{,}95}{8} \approx 0{,}0059$, plus petite : réponse **1**. **[0,25]**

Sur la copie : $\mathbb{E}[(\tilde{p} - p)^2] = \big(\mathbb{E}[\tilde{p}] - p\big)^2 + \mathbb{V}(\tilde{p})$. Ensemble, c), d) et f) montrent qu'aucun des deux estimateurs n'est meilleur pour tout $p$ : $\tilde{p}$, qui tire l'estimation vers $\frac{1}{2}$, gagne quand $p$ est proche de $\frac{1}{2}$ (moins de variance) et perd quand $p$ est près de 0 ou de 1 (trop de biais). C'est le compromis biais-variance d'un estimateur rétréci.

**Erreurs fréquentes** : en a), le biais à l'envers ($p - \mathbb{E}[\tilde{p}]$) ou $\mathbb{E}[\tilde{p}]$ seul ; en b), diviser la variance par $n + 2$ au lieu de $(n + 2)^2$ ; en c) et e), ajouter le biais sans le mettre au carré ; en d), oublier le $\frac{1}{n}$.
**Remédiation** : M09b.12, M09b.18.

## CP2.7 — Convexité, enveloppe convexe et marge ✏️ · 1,5 point

**Réponses** : a) `[[0, 0], [4, 0], [5, 3], [2, 5]]` · b) `True` · c) `1.213` · d) `1.581` · e) `[0.6, -0.2, -1.2]`.

a) Les points $(1, 2)$ et $(3, 2)$ sont à l'intérieur : par exemple, pour le côté qui va de $(2, 5)$ à $(0, 0)$, le produit vectoriel $\big((0, 0) - (2, 5)\big) \times \big((1, 2) - (2, 5)\big) = (-2)(-3) - (-5)(-1) = 1 > 0$ : $(1, 2)$ est à gauche du côté, du côté de l'intérieur. Les quatre autres points font des virages à gauche, dans l'ordre $(0, 0)$, $(4, 0)$, $(5, 3)$, $(2, 5)$. (L'aire de l'enveloppe, par la formule du lacet, vaut 15,5.) **[0,25]**
b) **Vrai** : en parcourant les côtés dans le sens direct, les produits vectoriels « côté × (point − origine du côté) » valent $(4, 0) \times (3, 4) = 16$, $(1, 3) \times (-1, 4) = 7$, $(-3, 2) \times (-2, 1) = 1$ et $(-2, -5) \times (1, -1) = 7$ : tous positifs, le point $(3, 4)$ est à gauche de chaque côté, donc dedans (de justesse pour le côté de $(5, 3)$ à $(2, 5)$). **[0,25]**
c) Les scores $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ valent 7, 9, 22 pour la classe $+1$, et 5, 11, 11 pour la classe $-1$ : le plus petit vaut 5, et $\lVert \mathbf{w} \rVert = \sqrt{17}$, donc la marge vaut $\frac{5}{\sqrt{17}} \approx 1{,}213$. **[0,25]**
d) La marge maximale est la moitié de la distance entre les deux enveloppes convexes (deux triangles). Ici, la paire la plus proche n'est pas faite de deux sommets : c'est le sommet $(2, 5)$ face au côté $[(4, 1), (6, 7)]$, porté par la droite $3x - y - 11 = 0$. La distance de $(2, 5)$ à cette droite vaut $\frac{\lvert 6 - 5 - 11 \rvert}{\sqrt{10}} = \sqrt{10}$, et son pied, $(5, 4)$, tombe bien entre $(4, 1)$ et $(6, 7)$. Les autres paires sont plus loin (les sommets les plus proches sont à $\sqrt{20}$ : plusieurs paires sont à cette distance, par exemple $(2, 5)$ et $(4, 1)$). La marge maximale vaut $\frac{\sqrt{10}}{2} \approx 1{,}581$. **[0,5]**
e) Le séparateur est parallèle au côté $[(4, 1), (6, 7)]$, à mi-chemin de $(2, 5)$ : il passe par le milieu $(3{,}5 ;\ 4{,}5)$ de $(2, 5)$ et $(5, 4)$, soit $3x - y - 6 = 0$. Les scores $y_i(3x_i - y_i - 6)$ valent au moins 5 (atteint en $(4, 1)$, $(6, 7)$ et $(2, 5)$) ; en divisant par 5 : $\mathbf{w} = (0{,}6 ;\ -0{,}2)$, $b = -1{,}2$. Vérification : $\frac{1}{\lVert \mathbf{w} \rVert} = \frac{1}{\sqrt{0{,}4}} \approx 1{,}581$. Sur la copie : les points les plus proches des deux enveloppes sont $(2, 5)$ et $(5, 4)$, et le second n'est pas un point des nuages ; le séparateur n'est la médiatrice d'aucun couple de points des nuages, et trois points sont sur le bord de la marge. **[0,25]**

**Erreurs fréquentes** : en a), garder un point intérieur ou tourner dans le mauvais sens ; en b), juger « à l'œil » ; en c), oublier de diviser par $\lVert \mathbf{w} \rVert$ ; en d), ne regarder que les distances entre sommets ($\frac{\sqrt{20}}{2} \approx 2{,}236$, trop grand), ou donner la distance au lieu de la moitié ; en e), ne pas normaliser, ou orienter $\mathbf{w}$ vers la classe $-1$.
**Remédiation** : M10.1, M10.2, M10.3, M10.8.

## CP2.8 — Markov, Tchebychev et Hoeffding ✏️ · 1,5 point

**Réponses** : a) `0.4` · b) `0.0278` · c) `720` · d) `0.044` · e) `0.0155` · f) `3685`.

a) $T \ge 0$ : $P(T \ge 300) \le \frac{120}{300} = 0{,}4$. **[0,25]**
b) $T \ge 300$ entraîne $\lvert T - 120 \rvert \ge 180$ : $P(T \ge 300) \le \frac{30^2}{180^2} = \frac{900}{32\,400} \approx 0{,}0278$. Connaître l'écart-type divise la borne par plus de 14. **[0,25]**
c) $\mathbb{V}(\bar{T}) = \frac{900}{n}$, et Tchebychev donne $P(\lvert \bar{T} - 120 \rvert \ge 5) \le \frac{900}{25\,n}$ ; c'est au plus 0,05 dès que $n \ge \frac{900}{25 \times 0{,}05} = 720$. **[0,25]**
d) $r = \sqrt{\frac{\ln(2/0{,}02)}{2 \times 1\,200}} = \sqrt{\frac{\ln 100}{2\,400}} = \sqrt{0{,}0019188} \approx 0{,}0438$, soit 0,044. **[0,25]**
e) $2\exp(-2 \times 1\,200 \times 0{,}045^2) = 2e^{-4{,}86} \approx 0{,}0155$. **[0,25]**
f) $n \ge \frac{\ln 100}{2 \times 0{,}025^2} = \frac{4{,}60517}{0{,}00125} \approx 3\,684{,}1$, donc $n = 3\,685$. **[0,25]**

**Erreurs fréquentes** : en a), inverser le quotient ; en b), diviser par $t$ au lieu de $t^2$, ou prendre 300 comme écart ; en c), mettre l'écart-type au lieu de la variance ; en d), $\ln(1/\delta)$ (unilatéral) ou diviser par $n$ au lieu de $2n$ ; en e), oublier le facteur 2 ; en f), arrondir $\ln 100$ trop tôt (4,605 donne 3 684) ou arrondir $n$ au-dessous.
**Remédiation** : M11.5, M11.6, M11.7, M11.14.

## CP2.9 — Une démonstration courte, au choix parmi deux ∂ · 2 points

### Sujet A — La loss des moindres carrés est convexe

1. **[0,5]** Avec $\lVert \mathbf{a} \rVert^2 = \mathbf{a} \cdot \mathbf{a}$ et la bilinéarité du produit scalaire : le membre de gauche vaut $(1 - t)^2\lVert \mathbf{u} \rVert^2 + 2t(1 - t)\,\mathbf{u} \cdot \mathbf{v} + t^2\lVert \mathbf{v} \rVert^2$. Le membre de droite vaut $(1 - t)\lVert \mathbf{u} \rVert^2 + t\lVert \mathbf{v} \rVert^2 - t(1 - t)\big(\lVert \mathbf{u} \rVert^2 - 2\,\mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{v} \rVert^2\big)$ ; le coefficient de $\lVert \mathbf{u} \rVert^2$ y est $(1 - t) - t(1 - t) = (1 - t)^2$, celui de $\lVert \mathbf{v} \rVert^2$ est $t - t(1 - t) = t^2$, celui de $\mathbf{u} \cdot \mathbf{v}$ est $2t(1 - t)$ : les deux membres sont égaux.
2. **[0,5]** Pour $t \in [0, 1]$, $t(1 - t) \ge 0$ et $\lVert \mathbf{u} - \mathbf{v} \rVert^2 \ge 0$ : le terme retranché est positif, donc $g\big((1 - t)\mathbf{u} + t\mathbf{v}\big) \le (1 - t)\,g(\mathbf{u}) + t\,g(\mathbf{v})$, la définition de la convexité. Si $0 < t < 1$ et $\mathbf{u} \ne \mathbf{v}$, $t(1 - t) > 0$ et $\lVert \mathbf{u} - \mathbf{v} \rVert^2 > 0$ : l'inégalité est stricte.
3. **[0,5]** Pour $\mathbf{a}, \mathbf{b} \in \mathbb{R}^p$ et $t \in [0, 1]$ : $\mathbf{y} - \mathbf{X}\big((1 - t)\mathbf{a} + t\mathbf{b}\big) = (1 - t)(\mathbf{y} - \mathbf{X}\mathbf{a}) + t(\mathbf{y} - \mathbf{X}\mathbf{b})$, car $\mathbf{y} = (1 - t)\mathbf{y} + t\mathbf{y}$ et $\mathbf{X}$ est linéaire. Avec $\mathbf{u} = \mathbf{y} - \mathbf{X}\mathbf{a}$ et $\mathbf{v} = \mathbf{y} - \mathbf{X}\mathbf{b}$, la question 2 donne $f\big((1 - t)\mathbf{a} + t\mathbf{b}\big) = g\big((1 - t)\mathbf{u} + t\mathbf{v}\big) \le (1 - t)f(\mathbf{a}) + t f(\mathbf{b})$ : $f$ est convexe. (Elle n'est pas forcément strictement convexe : si $\mathbf{X}\mathbf{a} = \mathbf{X}\mathbf{b}$ avec $\mathbf{a} \ne \mathbf{b}$, les deux résidus sont égaux.)
4. **[0,5]** $\lambda\lVert \mathbf{w} \rVert^2$ est strictement convexe (question 2, avec $\lambda > 0$), $f$ est convexe, et une somme d'une fonction convexe et d'une fonction strictement convexe est strictement convexe (on additionne les deux inégalités, dont l'une est stricte). Si la loss était minimale en deux points distincts $\mathbf{a}$ et $\mathbf{b}$, de valeur commune $m$, leur milieu donnerait une valeur strictement plus petite que $\frac{1}{2}m + \frac{1}{2}m = m$ : contradiction. Le minimum est donc atteint en au plus un point (il l'est en un point, la solution de $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, mais ce n'était pas demandé).

**Grille de relecture.** (1) le développement des deux membres, avec les trois coefficients ; (2) le signe du terme retranché, et le cas strict ($t(1 - t) > 0$ **et** $\mathbf{u} \ne \mathbf{v}$) ; (3) l'écriture du résidu comme combinaison convexe des deux résidus ; (4) l'argument du milieu, qui conclut à l'unicité. C'est ce qui garantit, en ML, qu'une descente de gradient sur la loss ridge ne peut pas rester coincée dans un minimum local qui ne serait pas le bon.

### Sujet B — La méthode de Chernoff pour une somme de pièces

1. **[0,5]** La fonction $s \mapsto e^{\lambda s}$ est strictement croissante pour $\lambda > 0$ : l'événement $S \ge a$ est le même que $e^{\lambda S} \ge e^{\lambda a}$. La variable $e^{\lambda S}$ est positive et $e^{\lambda a} > 0$ : l'inégalité de **Markov** s'applique, $P(e^{\lambda S} \ge e^{\lambda a}) \le \frac{\mathbb{E}[e^{\lambda S}]}{e^{\lambda a}}$.
2. **[0,5]** $e^{\lambda S} = \prod_{i=1}^n e^{\lambda X_i}$. Les $X_i$ sont **indépendantes**, donc les $e^{\lambda X_i}$ aussi, et l'espérance d'un produit de variables indépendantes est le produit des espérances : $\mathbb{E}[e^{\lambda S}] = \prod_i \mathbb{E}[e^{\lambda X_i}] = \left(\frac{1}{2}e^0 + \frac{1}{2}e^\lambda\right)^n = \left(\frac{1 + e^\lambda}{2}\right)^n$.
3. **[0,75]** Avec $a = \frac{3n}{4}$ : $e^{-\lambda a}\left(\frac{1 + e^\lambda}{2}\right)^n = \left(e^{-3\lambda/4}\,\frac{1 + e^\lambda}{2}\right)^n = h(\lambda)^n$. On minimise $\ln h(\lambda) = -\frac{3\lambda}{4} + \ln(1 + e^\lambda) - \ln 2$ ; sa dérivée $-\frac{3}{4} + \frac{e^\lambda}{1 + e^\lambda}$ s'annule quand $\frac{e^\lambda}{1 + e^\lambda} = \frac{3}{4}$, soit $e^\lambda = 3$, $\lambda = \ln 3$ ; elle est négative avant et positive après (la fonction $\frac{e^\lambda}{1 + e^\lambda}$ croît), c'est donc un minimum. Alors $h(\ln 3) = 3^{-3/4} \times \frac{1 + 3}{2} = 2 \times 3^{-3/4} \approx 0{,}8774$.
4. **[0,25]** $e^{-1/8} \approx 0{,}8825 > 0{,}8774$ : la borne de Chernoff est la plus petite, pour tout $n$. Pour $n = 40$ : Chernoff $0{,}8774^{40} \approx 0{,}0053$, Hoeffding $e^{-5} \approx 0{,}0067$. (La vraie valeur, $P(S \ge 30)$, vaut environ 0,0011 : les deux sont des bornes, valables pour tout $n$.)

**Grille de relecture.** (1) la croissance de l'exponentielle et la positivité, pour appliquer Markov ; (2) l'indépendance, pour factoriser l'espérance ; (3) la dérivée de $\ln h$, son signe et la valeur $e^\lambda = 3$ ; (4) la comparaison chiffrée. Hoeffding est la même méthode, appliquée avec une majoration de $\mathbb{E}[e^{\lambda X_i}]$ valable pour toute variable bornée : elle perd un peu sur une pièce, mais elle ne demande pas la loi exacte.

**Erreurs fréquentes** (deux sujets) : en A, développer un seul membre, oublier le cas $\mathbf{u} = \mathbf{v}$ dans la stricte convexité, ou conclure à l'unicité sans l'argument du milieu. En B, appliquer Markov à $S$ au lieu de $e^{\lambda S}$, factoriser l'espérance sans citer l'indépendance, ou ne pas vérifier que le point critique est un minimum.
**Remédiation** : A : M07.2, M05a.1, la fiche M10 §1 (fonctions convexes), M09b.16 ; B : M11.11, M11.12, et l'encadré « D'où vient l'exponentielle » de la fiche M11 §6.

## CP2.10 — Corriger une copie : cinq erreurs 🐛 · 1,25 point

**Réponse de a)** : `"BCEGH"`. **[0,5]** (0,1 par lettre juste, −0,1 par lettre en trop, sans descendre sous 0)

b) Une ligne par erreur **[0,15 chacune]** :
- **(B)** $(1, 2) \cdot (-2, 1) = -2 + 2 = 0$ : les vecteurs sont **orthogonaux**, et leur similarité cosinus vaut 0, pas $-1$. Deux vecteurs opposés seraient l'un un multiple négatif de l'autre, comme $(1, 2)$ et $(-2, -4)$.
- **(C)** Le test bilatéral additionne les deux queues, de même probabilité ici (loi symétrique) : la p-valeur bilatérale vaut $2 \times 0{,}11 = 0{,}22$, pas la moitié.
- **(E)** Le déterminant vaut $6 \times 1 - 4 \times 1 = 2$ : il faut diviser par lui, et l'inverse est $\begin{pmatrix} 0{,}5 & -2 \\ -0{,}5 & 3 \end{pmatrix}$ (on vérifie que le produit donne $\mathbf{I}$).
- **(G)** Le disque et le demi-plan $y \ge 1$ sont convexes, et une **intersection** de convexes est convexe : l'ensemble est convexe (c'est une réunion qui peut ne pas l'être).
- **(H)** Chaque intervalle peut se tromper avec la probabilité 0,05 ; par la borne de l'union, la probabilité qu'**au moins un** des dix se trompe est au plus $10 \times 0{,}05 = 0{,}5$ : on garantit seulement que les dix sont justes ensemble avec une probabilité d'au moins 50 %. Pour 95 % ensemble, il suffit d'intervalles à $1 - \frac{0{,}05}{10} = 99{,}5$ % chacun.

Les lignes justes : (A) $\sqrt{9 + 16 + 144} = \sqrt{169} = 13$ ; (D) le nombre de colonnes de la première (3) égale le nombre de lignes de la seconde, et le produit a les lignes de la première et les colonnes de la seconde ; (F) l'équation normale de la colonne de 1 dit exactement $\sum_i r_i = 0$.

**Erreurs fréquentes** : croire (F) fausse (elle ne vaut qu'avec une ordonnée à l'origine, ce que dit la ligne) ; laisser passer (G) parce qu'un disque « coupé » semble moins régulier ; croire (H) juste en confondant chaque intervalle et tous ensemble.
**Remédiation** : M07.4, M08.1, M09a.11, M09b.5, M10.1, M10.6, M11.14.

## CP2.11 — Problème de synthèse : ajuster un modèle, mesurer son erreur, décider 🔗 · 2,25 points

**Réponses** : a) `[216, 579]` · b) `[5.22727, 1.95455]` · c) `1.86` · d) `0.993` · e) `-3.0` · f) `1` · g) `0.799` · h) `False`.

a) $\sum x_i^2 = 1 + 4 + 16 + 25 + 49 + 121 = 216$ et $\sum x_i y_i = 7 + 18 + 56 + 75 + 126 + 297 = 579$ ; avec $n = 6$, $\sum x_i = 30$ et $\sum y_i = 90$ : $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 6 & 30 \\ 30 & 216 \end{pmatrix}$ et $\mathbf{X}^\top\mathbf{y} = \begin{pmatrix} 90 \\ 579 \end{pmatrix}$. **[0,25]**
b) $\det = 6 \times 216 - 30^2 = 396$ ; $a = \frac{216 \times 90 - 30 \times 579}{396} = \frac{2\,070}{396} = \frac{115}{22} \approx 5{,}22727$ et $b = \frac{6 \times 579 - 30 \times 90}{396} = \frac{774}{396} = \frac{43}{22} \approx 1{,}95455$. **[0,25]**
c) Les résidus valent $-0{,}1818$ ; $-0{,}1364$ ; $0{,}9545$ ; $0$ ; $-0{,}9091$ ; $0{,}2727$ (la droite passe par $(\bar{x}, \bar{y}) = (5, 15)$, un des points), et leur somme des carrés $\approx 1{,}8636$, soit 1,86. (Par la formule $\mathrm{SCT} - b \sum (x_i - \bar{x})(y_i - \bar{y}) = 254 - 129\,b$, il faut garder $b$ assez précis : avec $b = 1{,}95455$, on trouve 1,863, soit 1,86 ; avec $b$ arrondi à 1,9545, la soustraction donnerait 1,87.) **[0,25]**
d) $\mathrm{SCT} = \sum (y_i - 15)^2 = 64 + 36 + 1 + 0 + 9 + 144 = 254$, donc $R^2 = 1 - \frac{1{,}8636}{254} \approx 0{,}993$. **[0,25]**
e) $6\ln\frac{1{,}8636}{6} + 2 \times 2 \approx 6 \times (-1{,}16923) + 4 \approx -3{,}0$. **[0,25]**
f) $\mathrm{AIC}_0 = 6\ln\frac{254}{6} + 2 \approx 24{,}5$ ; $\mathrm{AIC}_1 \approx -3{,}0$ ; $\mathrm{AIC}_2 = 6\ln\frac{1{,}85}{6} + 6 \approx -1{,}1$. Le plus petit est celui de la droite : réponse **1**. Sur la copie : de la constante à la droite, la SCR passe de 254 à 1,86, un gain énorme ($6\ln\frac{1{,}86}{254} \approx -29{,}5$) pour un coefficient de plus (+2) ; de la droite au polynôme, elle ne passe que de 1,864 à 1,85 ($6\ln\frac{1{,}85}{1{,}864} \approx -0{,}04$), alors que le coefficient de plus coûte encore 2 : le gain d'ajustement ne paie pas le paramètre, et il viendrait sans doute du bruit des six nuits. **[0,5]**
g) $\hat{p} = \frac{344}{400} = 0{,}86$ ; le rayon unilatéral vaut $\sqrt{\frac{\ln(1/0{,}05)}{2 \times 400}} = \sqrt{\frac{2{,}995732}{800}} \approx 0{,}061194$ ; la borne basse vaut $0{,}86 - 0{,}061194 \approx 0{,}7988$, soit 0,799. **[0,25]**
h) **Faux** : la borne basse, 0,7988, est juste sous 0,80. Avec une confiance de 95 %, les 400 traitements garantissent une proportion d'au moins 79,9 %, pas 80 %. Il faudrait plus de traitements (ou une proportion observée un peu plus haute). **[0,25]**

Sur la copie, pour g) : les 400 traitements doivent être **tirés indépendamment**, dans la même loi que ceux dont on veut connaître la proportion (pas les 400 plus faciles, ni des traitements d'une même nuit, qui se ressemblent) ; chaque variable « erreur < 2 s » vaut 0 ou 1, elle est donc bornée dans $[0, 1]$ ; et le modèle ne doit pas avoir été choisi en regardant ces 400 traitements (sinon, il faut la borne de l'union sur les modèles essayés).

Le lien avec workbookIA : ajuster un modèle, comparer des modèles sans se laisser tromper par l'erreur d'entraînement, puis garantir une performance sur des données nouvelles avec un nombre d'exemples connu, c'est le cycle de tout projet de ML ; ici, chaque étape se fait à la main.

**Erreurs fréquentes** : en a), écrire $(\sum x_i)^2 = 900$ au lieu de $\sum x_i^2$ ; en b), inverser $a$ et $b$ ; en c), donner la SCT, ou soustraire avec un $b$ arrondi ; en d), donner $\frac{\mathrm{SCR}}{\mathrm{SCT}}$ ; en e), oublier de diviser la SCR par $n$, ou le terme $2k$ ; en f), retenir le polynôme parce que sa SCR est la plus petite ; en g), utiliser $\ln(2/\delta)$, ou diviser par $n$ au lieu de $2n$ ; en h), arrondir 0,7988 à 0,80 avant de comparer.
**Remédiation** : M09b.2, M09b.4, M09b.5, M09b.11, M08.8, M11.7, M11.14.

## Barème récapitulatif et remédiation

| Question | Points | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP2.Q1 | 1,5 | M07 à M11 | les exercices cités au CP2.Q1, puis les quiz et les flashcards des chapitres concernés |
| CP2.1 | 1,75 | M07 | M07.3, M07.4, M07.5, M07.6, M07.17 |
| CP2.2 | 1,75 | M08 | M08.1, M08.3, M08.5, M08.12 |
| CP2.3 | 1,5 | M08 | M08.7, M08.8, M08.11 |
| CP2.4 | 1,75 | M09a | M09a.8, M09a.9, M09a.10, M09a.11, M09a.13 |
| CP2.5 | 1,75 | M09b | M09b.4, M09b.5, M09b.8, M09b.15 |
| CP2.6 | 1,5 | M09b | M09b.12, M09b.18 |
| CP2.7 | 1,5 | M10 | M10.1, M10.2, M10.3, M10.8 |
| CP2.8 | 1,5 | M11 | M11.5, M11.6, M11.7, M11.14 |
| CP2.9 | 2 | M07, M09b, M10 ou M11 | A : M07.2, M05a.1, M09b.16 ; B : M11.11, M11.12 |
| CP2.10 | 1,25 | M07 à M11 | M07.4, M08.1, M09a.11, M09b.5, M10.1, M10.6, M11.14 |
| CP2.11 | 2,25 | M09b, M08, M11 | M09b.2, M09b.4, M09b.5, M09b.11, M08.8, M11.7, M11.14 |
| **Total** | **20** | | |

**Lire ta note**
- **16 à 20** : la partie II est solide. Passe au checkpoint II de workbookIA ; garde les flashcards de la partie II dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe au checkpoint II de workbookIA.
- **8 à moins de 12** : avant le checkpoint II de workbookIA, fais la remédiation, relis ta synthèse et les fiches des chapitres concernés.
- **Moins de 8** : reprends les exercices ★★ des chapitres où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
