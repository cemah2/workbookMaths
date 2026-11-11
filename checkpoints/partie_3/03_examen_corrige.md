# CP3 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Barème par sous-question**, entre crochets ; sauf mention contraire, une sous-question vaut 0,25 point. Une justification demandée « sur ta copie » compte dans la sous-question à laquelle elle se rattache.
- **Crédit partiel** sur une sous-question de 0,25 point : 0,1 pour une réponse juste sans la démarche demandée, ou pour une méthode juste avec une erreur de calcul. **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois (par exemple un $\mathbf{R}$ faux en CP3.2 d, réutilisé en f) et g), ou des scores faux en CP3.10 b, réutilisés en c) à i)).
- **Arrondis** : une décimale de moins coûte au plus 0,05 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi. Des décimales en plus ne coûtent rien (le notebook les accepte).
- **Questions rédigées** (CP3.Q1, CP3.8, CP3.9 b, les phrases demandées « sur ta copie ») : les critères sont listés ; une idée juste formulée autrement compte autant.
- **Logarithmes** : $\ln$ est le logarithme népérien (`math.log` en Python), et $\log_2$ celui de base 2 (`math.log2`) ; les entropies de CP3.5 c) et e) sont en bits, les log-loss, la KL et les bornes en nats.

---

## CP3.Q1 — Dix affirmations sur la partie III 🧠 · 1,5 point

0,15 par affirmation : 0,05 pour le verdict, 0,1 pour la justification.

**a) Vrai** (M12a, M12c). Si une colonne est combinaison des autres, il existe $\mathbf{c} \ne \mathbf{0}$ avec $\mathbf{X}\mathbf{c} = \mathbf{0}$ (le noyau de $\mathbf{X}$ n'est pas réduit à $\mathbf{0}$). Alors $\mathbf{c}^\top\mathbf{X}^\top\mathbf{X}\,\mathbf{c} = \lVert \mathbf{X}\mathbf{c} \rVert^2 = 0$ pour un $\mathbf{c}$ non nul : $\mathbf{X}^\top\mathbf{X}$ est seulement semi-définie positive, et singulière.

**b) Vrai** (M12b, M12c). Tout vecteur du sous-espace (dimension 2) est inchangé, $\mathbf{P}\mathbf{x} = \mathbf{x}$ : la valeur propre 1, deux fois ; tout vecteur de son orthogonal (dimension $4 - 2 = 2$) est envoyé sur $\mathbf{0}$ : la valeur propre 0, deux fois. Vérification : la trace d'une projection vaut son rang, ici $1 + 1 + 0 + 0 = 2$.

**c) Faux** (M12b, M12c). La rotation d'un quart de tour $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ est orthogonale (ses colonnes sont orthonormées), mais son polynôme caractéristique, $\lambda^2 + 1$ (trace 0, déterminant 1), n'a pas de racine réelle : aucune direction n'est conservée. Seules les symétries orthogonales du plan ont des valeurs propres réelles (1 et −1).

**d) Faux** (M12d). Les variances le long des axes sont proportionnelles aux **carrés** des valeurs singulières, $\lambda_j = \frac{s_j^2}{n - 1}$ : la part du premier axe vaut $\frac{25}{25 + 4} = \frac{25}{29} \approx 86$ %. Les 71 % viennent de $\frac{5}{5 + 2}$, sans les carrés.

**e) Vrai** (M13a). $2\mathbf{w} \cdot \mathbf{x} + 2b = 0$ équivaut à $\mathbf{w} \cdot \mathbf{x} + b = 0$ : même frontière. Un point de score $z \ne 0$ reçoit $\sigma(2z)$ au lieu de $\sigma(z)$ ; comme $\sigma$ est strictement croissante et $\sigma(0) = 0{,}5$, $\sigma(2z)$ est plus loin de 0,5 que $\sigma(z)$, du même côté (par exemple $\sigma(1) \approx 0{,}731$ et $\sigma(2) \approx 0{,}881$). Le modèle devient plus sûr de lui sans changer aucune décision.

**f) Faux** (M13b). $\nabla f + \lambda\nabla g = \mathbf{0}$ s'écrit $(2x, 2y) + \lambda(1, 2) = \mathbf{0}$, donc $(x, y) = \left(-\frac{\lambda}{2}, -\lambda\right)$, et la contrainte donne $-\frac{5\lambda}{2} = 5$ : $\lambda = -2$, au point $(1, 2)$ (le point de la droite le plus proche de l'origine). Un multiplicateur nul voudrait dire que le minimum libre, $(0, 0)$, vérifie déjà la contrainte : ce n'est pas le cas.

**g) Faux** (M12a, M13b). La matrice de Gram vaut $\mathbf{K} = \mathbf{X}\mathbf{X}^\top$, où $\mathbf{X}$ a les trois points en lignes, de forme $(3, 2)$ : son rang est au plus 2, et $\mathbf{K}$, de taille $3 \times 3$, n'est pas inversible (trois vecteurs de $\mathbb{R}^2$ sont toujours liés).

**h) Vrai** (M14). Comme $0{,}45 > 0{,}35$, la borne de Chernoff donne $P(X \ge 0{,}45\,n) \le e^{-n\,\mathrm{KL}(0{,}45 \Vert 0{,}35)}$, avec $\mathrm{KL}(0{,}45 \Vert 0{,}35) \approx 0{,}0212 > 0$ : une décroissance exponentielle en $n$, et $n^k e^{-cn} \to 0$ pour tout $k$ quand $c > 0$.

**i) Faux** (M14). Pour $u > -1$, $u \ne 0$ : $\ln(1 + u) < u$. Avec $u = -\frac{0{,}3}{n}$ : $n\ln\left(1 - \frac{0{,}3}{n}\right) < -0{,}3$, donc $\left(1 - \frac{0{,}3}{n}\right)^n < e^{-0{,}3}$ pour tout $n \ge 1$ : la suite approche sa limite **par en dessous**. Exemple : $n = 1$ donne $0{,}7 < e^{-0{,}3} \approx 0{,}741$.

**j) Vrai** (M14). Les poids sont proportionnels à $e^{-\eta L_k}$ : le rapport du poids de cet expert à celui du meilleur vaut $e^{-0{,}5 \times 4} = e^{-2} \approx 0{,}135 < 0{,}2$.

**Erreurs fréquentes** : en a), répondre « Faux » parce que $\mathbf{X}^\top\mathbf{X}$ reste semi-définie positive (la question dit « définie ») ; en b), croire que toutes les valeurs propres valent 1 ; en c), oublier les rotations, qui n'ont pas de valeur propre réelle ; en d), oublier les carrés ; en e), croire que les probabilités ne changent pas avec la frontière ; en f), confondre avec une contrainte d'inégalité inactive ; en g), penser au noyau RBF, dont la matrice de Gram de points distincts est inversible ; en i), croire que la suite dépasse sa limite.
**Remédiation** : a) M12a.20, M12c.17 ; b) M12b.8, M12c.7 ; c) M12c.6, M12b.3 ; d) M12d.10, M12d.11 ; e) M13a.5, M13a.7 ; f) M13b.1, M13b.2 ; g) M12a.6, M13b.19 ; h) M14.8 ; i) M14.3, M14.6 ; j) M14.4.

## CP3.1 — Indépendance, base, rang et noyau ✏️ · 2 points

**Réponses** : a) `2` · b) `3` · c) `[-2, 3, 1, 0, 0]` · d) `[-1, 4]` · e) `[2, -1, -1]` · f) `False` · g) `1` · h) `[7, 2]`.

a) Pivot de Gauss : $L_3 \leftarrow L_3 - 2L_1$ donne $(0, -1, 3, -2, -4)$, puis $L_3 \leftarrow L_3 + L_2$ donne une ligne nulle. Il reste deux pivots (colonnes 1 et 2) : le rang vaut 2. **[0,25]**
b) Théorème du rang : $\dim\ker\mathbf{A} = 5 - 2 = 3$ (5 est le nombre de **colonnes**, la dimension de l'espace de départ). **[0,25]**
c) $x_1\mathbf{c}_1 + x_2\mathbf{c}_2 + \mathbf{c}_3 = \mathbf{0}$ : la première ligne donne $x_1 + 2 = 0$, la deuxième $x_2 - 3 = 0$ ; la troisième se vérifie : $2 \times (-2) - 3 + 7 = 0$. Donc $(-2, 3, 1, 0, 0)$, qui dit $\mathbf{c}_3 = 2\mathbf{c}_1 - 3\mathbf{c}_2$. **[0,25]**
d) $\mathbf{c}_5 = a\,\mathbf{c}_1 + b\,\mathbf{c}_2$ : $a = -1$ (première ligne), $b = 4$ (deuxième ligne), et la troisième se vérifie : $-2 - 4 = -6$. Les deux colonnes pivots $\mathbf{c}_1$ et $\mathbf{c}_2$ forment une base de l'image (de dimension 2). **[0,25]**
e) La troisième ligne de $\mathbf{A}$ vaut $2L_1 - L_2$ : tout $\mathbf{b} = \mathbf{A}\mathbf{x}$ vérifie donc $b_3 = 2b_1 - b_2$, soit $2b_1 - b_2 - b_3 = 0$, et cette équation définit un plan, de dimension 2, comme l'image : c'est elle. Vérification sur $\mathbf{c}_1$ : $2 - 0 - 2 = 0$ ; sur $\mathbf{c}_2$ : $0 - 1 + 1 = 0$. **[0,25]**
f) $2 \times 3 - 1 - 4 = 1 \ne 0$ : $(3, 1, 4)$ n'est pas dans l'image, le système n'a **aucune** solution. **[0,25]**
g) Pour $P = a + bX + cX^2$ : $P(2) = a + 2b + 4c$ et $P(-1) = a - b + c$, donc $P \in V \iff 3b + 3c = 0 \iff b = -c$. Dans $W$, en plus, $P(0) = a = 0$ : $W = \{c\,(X^2 - X)\}$, de dimension 1. **[0,25]**
h) $P = 7 - 2X + 2X^2$ a $b = -2 = -c$ : il est dans $V$, et $P = 7 \times 1 + 2\,(X^2 - X)$. **[0,25]**

Sur ta copie : le **théorème du rang** ($\dim\ker\mathbf{A} + \mathrm{rg}\,\mathbf{A} = $ nombre de colonnes) ; $V = \{a + c\,(X^2 - X)\}$ est engendré par $1$ et $X^2 - X$, qui sont libres (de degrés différents) : c'est une base, et $\dim V = 2$ (on le retrouve par le théorème du rang : $P \mapsto P(2) - P(-1)$ est une forme linéaire non nulle sur $\mathbb{R}_2[X]$, de dimension 3).

**Erreurs fréquentes** : en a), répondre 3 parce qu'il y a trois lignes ; en b), retrancher le rang du nombre de lignes ; en c), un signe faux (la vérification sur la première ligne l'attrape) ; en d), inverser l'ordre des coordonnées ; en e), écrire une équation qui ne s'annule pas sur toutes les colonnes ; en f), conclure sans tester l'équation de l'image ; en g), oublier que $W$ ajoute une condition à $V$ ; en h), lire $-2X$ comme le coefficient de $X^2 - X$.
**Remédiation** : M12a.3, M12a.4, M12a.5, M12a.9, M12a.10, M12a.13, M12a.17.

## CP3.2 — Gram-Schmidt, projection et moindres carrés ✏️ · 2 points

**Réponses** : a) `6` · b) `6` · c) `[5, -1, 7, -5]` · d) `[[6, 6], [0, 10]]` · e) `[6, -10]` · f) `[2, -1]` · g) `[-4, 2, -4, 10]` · h) `36`.

a) $\lVert \mathbf{v}_1 \rVert = \sqrt{1 + 1 + 9 + 25} = 6$, donc $\mathbf{q}_1 = \frac{1}{6}(1, 1, 3, 5)$ et $r_{11} = 6$. **[0,25]**
b) $r_{12} = \mathbf{q}_1 \cdot \mathbf{v}_2 = \frac{6 + 0 + 30 + 0}{6} = 6$. **[0,25]**
c) $\mathbf{v}_2 - 6\,\mathbf{q}_1 = \mathbf{v}_2 - \mathbf{v}_1 = (5, -1, 7, -5)$ : la part de $\mathbf{v}_2$ orthogonale à $\mathbf{v}_1$ (vérification : $5 - 1 + 21 - 25 = 0$). **[0,25]**
d) $r_{22} = \lVert (5, -1, 7, -5) \rVert = \sqrt{25 + 1 + 49 + 25} = 10$, donc $\mathbf{q}_2 = (0{,}5 ;\ -0{,}1 ;\ 0{,}7 ;\ -0{,}5)$ et $\mathbf{R} = \begin{pmatrix} 6 & 6 \\ 0 & 10 \end{pmatrix}$. **[0,25]**
e) $\mathbf{q}_1 \cdot \mathbf{y} = \frac{1 + 1 - 21 + 55}{6} = 6$ et $\mathbf{q}_2 \cdot \mathbf{y} = \frac{5 - 1 - 49 - 55}{10} = -10$. **[0,25]**
f) On remonte : $10\,\hat{x}_2 = -10$ donne $\hat{x}_2 = -1$, puis $6\,\hat{x}_1 + 6\,\hat{x}_2 = 6$ donne $\hat{x}_1 = 2$. **[0,25]**
g) $\hat{\mathbf{y}} = 2\mathbf{v}_1 - \mathbf{v}_2 = (-4, 2, -4, 10)$ ; on le retrouve par $\hat{\mathbf{y}} = \mathbf{Q}\mathbf{Q}^\top\mathbf{y} = 6\,\mathbf{q}_1 - 10\,\mathbf{q}_2 = (1, 1, 3, 5) - (5, -1, 7, -5)$. **[0,25]**
h) $\mathbf{y} - \hat{\mathbf{y}} = (5, -1, -3, 1)$, de norme au carré $25 + 1 + 9 + 1 = 36$. **[0,25]**

Sur ta copie : $\mathbf{v}_1 \cdot (5, -1, -3, 1) = 5 - 1 - 9 + 5 = 0$ et $\mathbf{v}_2 \cdot (5, -1, -3, 1) = 30 - 30 = 0$ : le résidu est orthogonal au plan, ce sont les équations normales $\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\hat{\mathbf{x}}) = \mathbf{0}$. Pythagore : $\lVert \mathbf{y} \rVert^2 = 1 + 1 + 49 + 121 = 172$, $\lVert \hat{\mathbf{y}} \rVert^2 = 16 + 4 + 16 + 100 = 136$ (aussi $6^2 + 10^2$, la norme de $\mathbf{Q}^\top\mathbf{y}$), et $136 + 36 = 172$.

**Erreurs fréquentes** : en b), utiliser $\mathbf{v}_1$ au lieu de $\mathbf{q}_1$ ($r_{12} = 36$) ; en c), retrancher $r_{12}\,\mathbf{v}_1$ ; en d), placer $r_{12}$ sous la diagonale, ou mettre $r_{22}^2$ ; en e), calculer $\mathbf{X}^\top\mathbf{y}$ ; en f), résoudre de haut en bas ; en g), donner le résidu au lieu de la projection ; en h), oublier le carré.
**Remédiation** : M12b.4, M12b.7, M12b.9, M12b.10, M12b.11, M12b.17.

## CP3.3 — Valeurs propres, matrice définie positive et Cholesky ✏️ · 2 points

**Réponses** : a) `[2, 36]` · b) `[0.5145, 0.8575]` · c) `0.5` · d) `1` · e) `[[3, 0, 0], [1, 2, 0], [-2, 1, 2]]` · f) `144` · g) `5` · h) `"]-4 ; 4["`.

a) $\mathrm{tr}\,\mathbf{S} = 38$ et $\det\mathbf{S} = 297 - 225 = 72$ : $\lambda^2 - 38\lambda + 72 = (\lambda - 2)(\lambda - 36)$. **[0,25]**
b) $\mathbf{S} - 36\,\mathbf{I} = \begin{pmatrix} -25 & 15 \\ 15 & -9 \end{pmatrix}$ : $-25x + 15y = 0$ donne la direction $(3, 5)$, de norme $\sqrt{34}$, d'où $\frac{(3, 5)}{\sqrt{34}} \approx (0{,}5145 ;\ 0{,}8575)$. **[0,25]**
c) $\mathbf{S}^{-1}$ a les mêmes vecteurs propres et les valeurs propres inverses, $\frac{1}{2}$ et $\frac{1}{36}$ : la plus grande vaut $0{,}5$ (elle vient de la **plus petite** valeur propre de $\mathbf{S}$). **[0,25]**
d) $\mathbf{S} - 2\,\mathbf{I} = \begin{pmatrix} 9 & 15 \\ 15 & 25 \end{pmatrix}$ : déterminant $225 - 225 = 0$, mais la matrice n'est pas nulle, donc de rang 1. Ses deux lignes sont des multiples de $(3, 5)$ : son image est la droite propre de 36 (en fait $\mathbf{S} - 2\,\mathbf{I} = 34\,\mathbf{u}\mathbf{u}^\top$ avec le $\mathbf{u}$ de b)). **[0,25]**
e) $l_{11} = \sqrt{9} = 3$ ; $l_{21} = \frac{3}{3} = 1$ ; $l_{31} = \frac{-6}{3} = -2$ ; $l_{22} = \sqrt{5 - 1^2} = 2$ ; $l_{32} = \frac{0 - (-2) \times 1}{2} = 1$ ; $l_{33} = \sqrt{9 - 4 - 1} = 2$. **[0,25]**
f) $\det\mathbf{B} = \det\mathbf{L} \times \det\mathbf{L}^\top = (3 \times 2 \times 2)^2 = 144$. **[0,25]**
g) $\mathbf{L}^\top\mathbf{x} = \begin{pmatrix} 3 & 1 & -2 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = (0, -1, 2)$, de norme au carré $0 + 1 + 4 = 5$. Vérification directe : $\mathbf{B}\mathbf{x} = (0, -2, 3)$ et $\mathbf{x} \cdot (0, -2, 3) = 5$. **[0,25]**
h) Une matrice symétrique $2 \times 2$ est définie positive si et seulement si son coefficient en haut à gauche et son déterminant sont strictement positifs : $2 > 0$ et $16 - a^2 > 0$, soit $-4 < a < 4$. **[0,25]**

Sur ta copie, pour e) : la troisième ligne de $\mathbf{L}\mathbf{L}^\top$ vaut $(-2 \times 3,\ -2 \times 1 + 1 \times 2,\ 4 + 1 + 4) = (-6, 0, 9)$, la troisième ligne de $\mathbf{B}$.

**Erreurs fréquentes** : en a), une erreur de signe sur la trace dans le polynôme ; en b), un vecteur non normalisé, ou celui de l'autre valeur propre ; en c), répondre 36 ; en d), répondre 0 parce que la matrice est singulière ; en e), écrire $\mathbf{L}^\top$ (triangulaire supérieure), ou oublier la racine sur la diagonale ; en g), appliquer $\mathbf{L}$ au lieu de $\mathbf{L}^\top$ ; en h), des inégalités larges (une matrice de déterminant nul n'est pas définie positive), ou oublier les $a$ négatifs.
**Remédiation** : M12c.3, M12c.7, M12c.10, M12c.11, M12c.16.

## CP3.4 — SVD, rang faible et variance expliquée ✏️ · 2 points

**Réponses** : a) `[[85, 42], [42, 72]]` · b) `[11, 6]` · c) `[0.759, 0.651]` · d) `[0.976, -0.217]` · e) `[[8.15, 6.99], [-1.81, -1.55]]` · f) `6` · g) `0.771` · h) `1.833`.

a) $\mathbf{A}^\top\mathbf{A} = \begin{pmatrix} 81 + 4 & 54 - 12 \\ 54 - 12 & 36 + 36 \end{pmatrix} = \begin{pmatrix} 85 & 42 \\ 42 & 72 \end{pmatrix}$. **[0,25]**
b) Trace 157, déterminant $85 \times 72 - 42^2 = 6\,120 - 1\,764 = 4\,356$ : $\lambda = \frac{157 \pm \sqrt{157^2 - 4 \times 4\,356}}{2} = \frac{157 \pm 85}{2}$, soit 121 et 36, et $s_1 = 11$, $s_2 = 6$. **[0,25]**
c) $\mathbf{A}^\top\mathbf{A} - 121\,\mathbf{I} = \begin{pmatrix} -36 & 42 \\ 42 & -49 \end{pmatrix}$ : $-36x + 42y = 0$ donne la direction $(7, 6)$, de norme $\sqrt{85}$ : $\mathbf{v}_1 \approx (0{,}759 ;\ 0{,}651)$. **[0,25]**
d) $\mathbf{A}\,(7, 6) = (63 + 36,\ 14 - 36) = (99, -22) = 11\,(9, -2)$ : $\mathbf{u}_1 = \frac{(9, -2)}{\sqrt{85}} \approx (0{,}976 ;\ -0{,}217)$, bien unitaire. **[0,25]**
e) $\mathbf{A}_1 = 11 \times \frac{(9, -2)}{\sqrt{85}}\,\frac{(7, 6)^\top}{\sqrt{85}} = \frac{11}{85}\begin{pmatrix} 63 & 54 \\ -14 & -12 \end{pmatrix} \approx \begin{pmatrix} 8{,}15 & 6{,}99 \\ -1{,}81 & -1{,}55 \end{pmatrix}$. **[0,25]**
f) Eckart-Young : $\mathbf{A} - \mathbf{A}_1 = s_2\,\mathbf{u}_2\mathbf{v}_2^\top$, de norme de Frobenius $s_2 = 6$. **[0,25]**
g) $\lVert \mathbf{A} \rVert_F^2 = 81 + 36 + 4 + 36 = 157 = 11^2 + 6^2$ ; $\mathbf{A}_1$ en garde $\frac{121}{157} \approx 0{,}771$. **[0,25]**
h) $\kappa_2(\mathbf{A}) = \frac{s_1}{s_2} = \frac{11}{6} \approx 1{,}833$ : une matrice bien conditionnée. **[0,25]**

Sur ta copie : $\det\mathbf{A} = -54 - 12 = -66$, et $\lvert \det\mathbf{A} \rvert = 66 = 11 \times 6$ ; en norme spectrale aussi, $\lVert \mathbf{A} - \mathbf{A}_1 \rVert_2 = s_2 = 6$ (pour une matrice $2 \times 2$, l'erreur de rang 1 n'a qu'une valeur singulière).

**Erreurs fréquentes** : en a), calculer $\mathbf{A}\mathbf{A}^\top$ ; en b), donner 121 et 36 sans les racines ; en c), prendre le vecteur de la valeur propre 36 ; en d), oublier de diviser par $s_1$ ; en e), arrondir $\mathbf{u}_1$ et $\mathbf{v}_1$ à 3 décimales avant le produit (l'erreur se voit sur la deuxième décimale) ; en f), donner $s_1$ ou $s_2^2$ ; en g), $\frac{11}{17}$, sans les carrés ; en h), $\frac{121}{36}$, le conditionnement de $\mathbf{A}^\top\mathbf{A}$.
**Remédiation** : M12d.1, M12d.4, M12d.7, M12d.16, et le quiz M12d.Q3.

## CP3.5 — Maximum de vraisemblance, log-loss et entropie ✏️ · 1,75 point

**Réponses** : a) `5.6` · b) `"7/45"` · c) `1.513` · d) `0.635` · e) `0.340` · f) `0.565` · g) `0.673`.

a) La densité de la loi uniforme vaut $\frac{1}{\theta}$ sur $[0, \theta]$, 0 ailleurs : $L(\theta) = \frac{1}{\theta^5}$ si $\theta \ge 5{,}6$ (toutes les observations sont dans $[0, \theta]$), et $L(\theta) = 0$ si $\theta < 5{,}6$. Sur $[5{,}6 ;\ +\infty[$, $L$ décroît : son maximum est en $\hat{\theta} = 5{,}6$, la plus grande observation. **[0,25]**
b) $\ell(\theta) = 4\ln\theta + 10\ln(2\theta) + 16\ln(1 - 3\theta)$, de dérivée $\frac{14}{\theta} - \frac{48}{1 - 3\theta}$, nulle quand $14\,(1 - 3\theta) = 48\,\theta$, soit $\theta = \frac{14}{90} = \frac{7}{45} \approx 0{,}156$, bien dans $\left]0, \frac{1}{3}\right[$ ; la dérivée passe du positif au négatif, c'est un maximum. **[0,25]**
c) $H = 0{,}45 \log_2\frac{1}{0{,}45} + 0{,}35 \log_2\frac{1}{0{,}35} + 0{,}2 \log_2\frac{1}{0{,}2} \approx 0{,}45 \times 1{,}152003 + 0{,}35 \times 1{,}514573 + 0{,}2 \times 2{,}321928 \approx 1{,}512888$, soit 1,513 bit. **[0,25]**
d) $G = 1 - (0{,}45^2 + 0{,}35^2 + 0{,}2^2) = 1 - 0{,}365 = 0{,}635$. **[0,25]**
e) Groupe $(4, 1, 4)$, 9 exemples : $H = 2 \times \frac{4}{9}\log_2\frac{9}{4} + \frac{1}{9}\log_2 9 \approx 1{,}392147$. Groupe $(5, 6, 0)$, 11 exemples : $H = \frac{5}{11}\log_2\frac{11}{5} + \frac{6}{11}\log_2\frac{11}{6} \approx 0{,}994030$. Moyenne pondérée : $\frac{9}{20} \times 1{,}392147 + \frac{11}{20} \times 0{,}994030 \approx 1{,}173183$. Gain : $1{,}512888 - 1{,}173183 \approx 0{,}340$ bit. **[0,25]**
f) Les cinq termes $s(z) - yz$ : $s(1{,}3) - 1{,}3 = s(-1{,}3) \approx 0{,}241008$ ; $s(-1{,}2) \approx 0{,}263282$ ; $s(-0{,}5) + 0{,}5 = s(0{,}5) \approx 0{,}974077$ ; $s(-2{,}2) \approx 0{,}105083$ ; $s(0{,}9) \approx 1{,}241154$. Somme $\approx 2{,}824605$, moyenne $\approx 0{,}565$ nat. **[0,25]**
g) Trois labels sur cinq valent 1 : la meilleure probabilité constante est la fréquence, $q = 0{,}6$, et sa log-loss vaut $-(0{,}6\ln 0{,}6 + 0{,}4\ln 0{,}4) \approx 0{,}673$ nat. **[0,25]**

Sur ta copie : pour a), $L$ n'est pas dérivable en 5,6 (elle saute de 0 à $5{,}6^{-5}$), et sur $]5{,}6 ;\ +\infty[$ sa dérivée, $-\frac{5}{\theta^6}$, ne s'annule jamais : le maximum est au **bord** du domaine où $L > 0$, pas en un point de dérivée nulle. Pour g), la log-loss moyenne d'une probabilité constante $q$ est la cross-entropy $H(\pi) + \mathrm{KL}(\pi \Vert q)$ avec $\pi = 0{,}6$ la fréquence observée : elle est minimale quand la KL est nulle, en $q = \pi$, et vaut alors l'entropie $H(0{,}6)$ en nats. Le modèle de f), à 0,565, fait mieux que toute constante : ses scores apportent de l'information.

**Erreurs fréquentes** : en a), prendre la moyenne, ou deux fois la moyenne (l'estimateur des moments, 6,84) ; en b), ne garder que la fréquence des 0 ($\frac{4}{30}$), ou oublier le facteur 2 qui disparaît dans la dérivée ; en c), utiliser $\ln$ (1,049 nat) ; en d), oublier le « 1 − » ; en e), ne pas pondérer les groupes par leurs effectifs, ou rendre la moyenne pondérée sans la soustraire ; en f), oublier le terme $-yz$, ou rendre la somme ; en g), rendre $\ln 2 \approx 0{,}693$ (la probabilité 0,5), ou l'entropie en bits (0,971).
**Remédiation** : M13a.1, M13a.3, M13a.6, M13a.10, M13a.14, et la fiche M13a §1 (vraisemblance) ; pour a), la loi uniforme de M02b.

## CP3.6 — Lagrange, hinge loss et noyau ✏️ · 1,75 point

**Réponses** : a) `[2, 1]` · b) `4` · c) `-2` · d) `3.5` · e) `6` · f) `[3, 0.5, 0]` · g) `-2`.

a) $\nabla f + \lambda\nabla g = \mathbf{0}$ s'écrit $1 + \frac{\lambda x}{4} = 0$ et $2 + \lambda y = 0$, soit $x = -\frac{4}{\lambda}$ et $y = -\frac{2}{\lambda}$. La contrainte donne $\frac{16}{8\lambda^2} + \frac{4}{2\lambda^2} = \frac{4}{\lambda^2} = 1$, donc $\lambda = \pm 2$ : deux candidats, $(2, 1)$ (avec $\lambda = -2$), où $f = 4$, et $(-2, -1)$ (avec $\lambda = 2$), où $f = -4$. Le maximum est en $(2, 1)$. **[0,25]**
b) $f(2, 1) = 2 + 2 = 4$. **[0,25]**
c) $\lambda = -2$ (avec la convention $\nabla f + \lambda\nabla g = \mathbf{0}$ ; la convention $\nabla f = \lambda\nabla g$ donnerait $+2$). Sensibilité : sur l'ellipse $\frac{x^2}{8} + \frac{y^2}{2} = c$, le maximum vaut $4\sqrt{c}$, de dérivée 2 en $c = 1$, c'est $-\lambda$. **[0,25]**
d) Les marges $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ : $P_1$ : $2 + 2 - 3 = 1$ ; $P_2$ : $-(4 - 3) = -1$ ; $P_3$ : $2 + 0{,}5 - 3 = -0{,}5$. Les hinges : $0$, $2$ et $1{,}5$, de somme $3{,}5$. **[0,25]**
e) $J = \frac{1}{2}(4 + 1) + 1 \times 3{,}5 = 6$. **[0,25]**
f) Seuls $P_2$ et $P_3$ ont une marge strictement inférieure à 1 ; chacun apporte $(-y_i\mathbf{x}_i, -y_i)$, et $\frac{1}{2}\lVert \mathbf{w} \rVert^2$ apporte $(\mathbf{w}, 0)$ : $\mathbf{g}_{\mathbf{w}} = (2, 1) + (2, 0) - (1 ;\ 0{,}5) = (3 ;\ 0{,}5)$ et $g_b = -(-1) - 1 = 0$. **[0,25]**
g) $\mathbf{K} = \begin{pmatrix} 0 & 1 & 3 \\ 1 & 0 & 2 \\ 3 & 2 & 0 \end{pmatrix}$ et $\mathbf{v}^\top\mathbf{K}\mathbf{v} = K_{11} - 2K_{12} + K_{22} = 0 - 2 + 0 = -2$. **[0,25]**

Sur ta copie : pour a), l'ellipse est fermée et bornée et $f$ est continue, donc $f$ y atteint un maximum et un minimum ; $\nabla g = \left(\frac{x}{4}, y\right)$ ne s'annule pas sur l'ellipse, donc ces extrema sont parmi les points de Lagrange : on compare $f$ aux deux candidats. Pour g), la matrice de Gram d'un noyau est toujours semi-définie positive ($\mathbf{v}^\top\mathbf{K}\mathbf{v} = \lVert \sum_i v_i\,\varphi(x_i) \rVert^2 \ge 0$) : $-2 < 0$ prouve que $\lvert x - z \rvert$ n'est **pas** un noyau. (Plus simplement encore : une diagonale nulle avec des coefficients non nuls hors de la diagonale est impossible pour une matrice semi-définie positive.)

**Erreurs fréquentes** : en a), garder un seul candidat, ou ne pas justifier lequel est le maximum ; en c), le signe (la convention de l'énoncé est celle de M13b) ; en d), oublier le label $-1$ de $P_2$ dans la marge ; en e), mettre $\lVert \mathbf{w} \rVert^2$ au lieu de sa moitié ; en f), oublier le terme $\mathbf{w}$, compter $P_1$ (sa marge vaut exactement 1, l'énoncé dit d'y prendre 0), ou écrire $+y_i\mathbf{x}_i$ ; en g), oublier que les termes croisés comptent deux fois.
**Remédiation** : M13b.1, M13b.2, M13b.9, M13b.10, M13b.13, M13b.19.

## CP3.7 — Queue binomiale et borne de Chernoff, limite et poids exponentiels ✏️ · 1,5 point

**Réponses** : a) `0.0107` · b) `0.038` · c) `0.3470` · d) `0.1134` · e) `-0.074` · f) `[0.1101, 0.4465, 0.2217, 0.2217]`.

a) $P(X \ge 3) = 1 - P(X = 0) - P(X = 1) - P(X = 2)$, avec $P(X = 0) = 0{,}96^{12} \approx 0{,}612710$, $P(X = 1) = 12 \times 0{,}04 \times 0{,}96^{11} \approx 0{,}306355$ et $P(X = 2) = 66 \times 0{,}04^2 \times 0{,}96^{10} \approx 0{,}070206$ : $P(X \ge 3) \approx 0{,}010729$. **[0,25]**
b) $\mathrm{KL}(0{,}25 \Vert 0{,}04) = 0{,}25\ln\frac{0{,}25}{0{,}04} + 0{,}75\ln\frac{0{,}75}{0{,}96} \approx 0{,}458145 - 0{,}185145 = 0{,}273000$ ; $12 \times 0{,}273000 \approx 3{,}276004$ et $e^{-3{,}276004} \approx 0{,}038$. **[0,25]**
c) $2 \times 12 \times 0{,}21^2 = 1{,}0584$ et $e^{-1{,}0584} \approx 0{,}3470$. **[0,25]**
d) $0{,}93^{30} = e^{30\ln 0{,}93} \approx e^{-2{,}177121} \approx 0{,}1134$. **[0,25]**
e) $e^{-2{,}1} \approx 0{,}122456$ ; $\frac{0{,}113367 - 0{,}122456}{0{,}122456} \approx -0{,}074$ : à $n = 30$, la suite est encore à 7,4 % sous sa limite. **[0,25]**
f) On retranche la plus petite perte cumulée (1) : $\eta\,(L - 1) = 0{,}7 \times (2, 0, 1, 1) = (1{,}4 ;\ 0 ;\ 0{,}7 ;\ 0{,}7)$, puis $e^{-1{,}4} \approx 0{,}246597$, $e^{0} = 1$, $e^{-0{,}7} \approx 0{,}496585$ (deux fois), de somme $\approx 2{,}239768$ : les poids valent $\approx (0{,}1101 ;\ 0{,}4465 ;\ 0{,}2217 ;\ 0{,}2217)$. **[0,25]**

Sur ta copie : $0{,}0107 < 0{,}038 < 0{,}347$. La queue exacte est la plus petite, une borne la majore ; Chernoff utilise toute la loi (par la KL), Hoeffding seulement le fait que chaque $X_i$ est dans $[0, 1]$, et $\mathrm{KL}(a \Vert p) \ge 2(a - p)^2$ (Pinsker) : Chernoff est toujours au moins aussi bonne, et beaucoup meilleure quand $p$ est petit, comme ici ($0{,}273$ contre $0{,}0882$ dans l'exposant, par colis). Pour e), $-\frac{x^2}{2n} = -\frac{2{,}1^2}{60} = -0{,}0735$ : très proche de $-0{,}0742$ ; le terme suivant du développement de $n\ln\left(1 + \frac{x}{n}\right)$ explique le reste.

**Erreurs fréquentes** : en a), calculer $P(X > 3)$ ou $P(X = 3)$ seulement ; en b), inverser les arguments de la KL (la KL n'est pas symétrique), ou la calculer en bits ; en c), oublier le facteur 2 ; en e), un signe faux (la suite est sous sa limite, l'erreur est négative) ; en f), $e^{+\eta L}$, oublier $\eta$, ou ne pas normaliser.
**Remédiation** : M14.1, M14.3, M14.4, M14.8, et les quiz M14.Q1 et M14.Q3.

## CP3.8 — Une démonstration courte, au choix parmi deux ∂ · 2 points

### Sujet A — Le système de Lagrange d'un problème quadratique est inversible

1. **[0,5]** Le gradient du lagrangien par rapport à $\mathbf{x}$ vaut $\mathbf{Q}\mathbf{x} + \mathbf{c} + \mathbf{A}^\top\boldsymbol{\lambda}$ ($\mathbf{Q}$ est symétrique, et le gradient de $\boldsymbol{\lambda}^\top\mathbf{A}\mathbf{x}$ est $\mathbf{A}^\top\boldsymbol{\lambda}$) ; ses dérivées par rapport à $\boldsymbol{\lambda}$ redonnent la contrainte $\mathbf{A}\mathbf{x} - \mathbf{b}$. Les annuler : $\mathbf{Q}\mathbf{x} + \mathbf{A}^\top\boldsymbol{\lambda} = -\mathbf{c}$ et $\mathbf{A}\mathbf{x} = \mathbf{b}$, exactement les deux blocs de lignes de $\mathbf{M}\begin{pmatrix} \mathbf{x} \\ \boldsymbol{\lambda} \end{pmatrix} = \begin{pmatrix} -\mathbf{c} \\ \mathbf{b} \end{pmatrix}$.
2. **[0,5]** Les deux blocs de $\mathbf{M}\begin{pmatrix} \mathbf{u} \\ \boldsymbol{\mu} \end{pmatrix} = \mathbf{0}$ disent $\mathbf{Q}\mathbf{u} + \mathbf{A}^\top\boldsymbol{\mu} = \mathbf{0}$ et $\mathbf{A}\mathbf{u} = \mathbf{0}$. On multiplie le premier à gauche par $\mathbf{u}^\top$ : $\mathbf{u}^\top\mathbf{Q}\mathbf{u} + \mathbf{u}^\top\mathbf{A}^\top\boldsymbol{\mu} = \mathbf{u}^\top\mathbf{Q}\mathbf{u} + (\mathbf{A}\mathbf{u})^\top\boldsymbol{\mu} = \mathbf{u}^\top\mathbf{Q}\mathbf{u} + 0 = 0$.
3. **[0,5]** $\mathbf{Q}$ est définie positive : $\mathbf{u}^\top\mathbf{Q}\mathbf{u} > 0$ pour tout $\mathbf{u} \ne \mathbf{0}$, donc $\mathbf{u} = \mathbf{0}$. Le premier bloc devient $\mathbf{A}^\top\boldsymbol{\mu} = \mathbf{0}$, c'est-à-dire $\sum_j \mu_j\,\mathbf{a}_j = \mathbf{0}$ où les $\mathbf{a}_j$ sont les lignes de $\mathbf{A}$ ; $\mathbf{A}$ est de rang $m$, ses $m$ lignes sont indépendantes, donc tous les $\mu_j$ sont nuls. Le noyau de la matrice carrée $\mathbf{M}$ est réduit à $\mathbf{0}$ : elle est inversible, et le système de Lagrange a une solution unique, quels que soient $\mathbf{c}$ et $\mathbf{b}$. (Le problème est convexe, avec des contraintes affines : cette solution est le minimum.)
4. **[0,5]** Avec $\mathbf{A} = (1\ \ 0)$ : $\mathbf{M} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$, et $(u_1, u_2, \mu) = (0, 1, 0)$ est un vecteur non nul de son noyau ($\mathbf{Q}\mathbf{u} = \mathbf{0}$ et $\mathbf{A}\mathbf{u} = 0$) : $\mathbf{M}$ n'est pas inversible. Avec $\mathbf{A} = (0\ \ 1)$ : $\mathbf{M} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$, de déterminant $1 \times (0 - 1) = -1 \ne 0$ : inversible. Dans la démonstration, l'étape 3 n'utilise $\mathbf{u}^\top\mathbf{Q}\mathbf{u} = 0 \Rightarrow \mathbf{u} = \mathbf{0}$ que pour des $\mathbf{u}$ du noyau de $\mathbf{A}$ (étape 2). Dans le premier cas, ce noyau est la droite de $(0, 1)$, où la forme $\mathbf{u}^\top\mathbf{Q}\mathbf{u} = u_1^2$ s'annule ; dans le second, c'est la droite de $(1, 0)$, où elle vaut $u_1^2 > 0$. Ce qu'il faut vraiment, c'est que $\mathbf{Q}$ soit définie positive **sur le noyau de** $\mathbf{A}$.

**Grille de relecture.** (1) les deux familles de dérivées, et le bon bloc $\mathbf{A}^\top$ ; (2) la multiplication par $\mathbf{u}^\top$ et l'usage de $\mathbf{A}\mathbf{u} = \mathbf{0}$ ; (3) la définie positivité pour $\mathbf{u}$, puis l'indépendance des lignes pour $\boldsymbol{\mu}$, et « noyau nul ⇒ inversible » pour une matrice carrée ; (4) les deux exemples et la condition sur le noyau de $\mathbf{A}$. C'est ce système que résolvent les solveurs de problèmes quadratiques ; une contrainte écrite deux fois rend $\mathbf{A}$ de rang trop petit, et c'est l'étape 3 qui échoue (les multiplicateurs ne sont plus uniques).

### Sujet B — Les poids de Hedge minimisent une perte régularisée par l'entropie

1. **[0,5]** Lagrangien : $G(\mathbf{w}, \nu) = \eta\sum_k w_k L_k + \sum_k w_k\ln w_k + \nu\left(\sum_k w_k - 1\right)$. Sa dérivée par rapport à $w_k$ : $\eta L_k + \ln w_k + 1 + \nu = 0$, donc $w_k = e^{-1 - \nu}\,e^{-\eta L_k}$. La contrainte impose $e^{-1 - \nu}\sum_j e^{-\eta L_j} = 1$, ce qui fixe $\nu$ : le seul point critique est $w_k = \frac{e^{-\eta L_k}}{\sum_j e^{-\eta L_j}}$. Ses coordonnées sont strictement positives : il est dans $\Delta$, la positivité ignorée est respectée d'elle-même.
2. **[0,5]** $\frac{\partial^2 F}{\partial w_k^2} = \frac{1}{w_k} > 0$ et les dérivées croisées sont nulles : la hessienne est diagonale à coefficients strictement positifs, définie positive en tout point où les $w_k > 0$, donc $F$ est strictement convexe sur $\Delta$. $\Delta$ est convexe : si $\mathbf{w}$ et $\mathbf{w}'$ y sont, $(1 - t)\mathbf{w} + t\mathbf{w}'$ a des coordonnées positives et de somme $(1 - t) + t = 1$. Un objectif convexe sous une contrainte d'égalité affine est un problème convexe, et les conditions de Lagrange y suffisent (M13b §5 : pour un problème convexe, tout minimum local est global, ∂ M13b.16, et les conditions KKT suffisent). Directement : en $\mathbf{w}^*$, $\nabla F(\mathbf{w}^*) = -\nu\,(1, \ldots, 1)$, donc pour $\mathbf{w}' \in \Delta$, $F(\mathbf{w}') \ge F(\mathbf{w}^*) + \nabla F(\mathbf{w}^*) \cdot (\mathbf{w}' - \mathbf{w}^*) = F(\mathbf{w}^*) - \nu\left(\sum_k w'_k - \sum_k w^*_k\right) = F(\mathbf{w}^*)$, avec inégalité stricte si $\mathbf{w}' \ne \mathbf{w}^*$ (stricte convexité) : $\mathbf{w}^*$ est l'unique minimum.
3. **[0,5]** Avec $Z = \sum_j e^{-\eta L_j}$ : $\ln w^*_k = -\eta L_k - \ln Z$, donc $F(\mathbf{w}^*) = \sum_k w^*_k\,(\eta L_k + \ln w^*_k) = \sum_k w^*_k\,(-\ln Z) = -\ln Z$, puisque $\sum_k w^*_k = 1$.
4. **[0,5]** Chaque terme de $Z$ vaut au plus $e^{-\eta L_{\min}}$ (car $L_k \ge L_{\min}$ et $\eta > 0$), et l'un d'eux lui est égal : $e^{-\eta L_{\min}} \le Z \le K\,e^{-\eta L_{\min}}$. La fonction $-\ln$ est décroissante : $\eta L_{\min} - \ln K \le m(\eta) \le \eta L_{\min}$. En divisant par $\eta > 0$ : $L_{\min} - \frac{\ln K}{\eta} \le \frac{m(\eta)}{\eta} \le L_{\min}$. $\frac{m(\eta)}{\eta}$ est un **minimum adouci** des pertes cumulées : elle est proche de la perte du meilleur expert, à au plus $\frac{\ln K}{\eta}$ près, et la rejoint quand $\eta \to +\infty$. Ce $\frac{\ln K}{\eta}$ est le premier terme de la borne du regret de Hedge (M14 §4) : le prix de partir des poids uniformes.

**Grille de relecture.** (1) les dérivées du lagrangien et la normalisation qui fixe $\nu$ ; (2) la hessienne, la convexité de $\Delta$ et le résultat de M13b cité (ou l'inégalité de la tangente) ; (3) le calcul de la valeur, par $\ln w^*_k$ ; (4) l'encadrement de $Z$ et son interprétation. Le calcul est celui d'une famille entière de méthodes : les poids softmax (M13a, LSE) sont la solution d'un compromis entre suivre la meilleure perte et garder de l'entropie.

**Erreurs fréquentes** (deux sujets) : en A, oublier le transposé dans $\mathbf{A}^\top\boldsymbol{\lambda}$, conclure $\mathbf{u} = \mathbf{0}$ sans la définie positivité, ou $\boldsymbol{\mu} = \mathbf{0}$ sans le rang de $\mathbf{A}$ ; dans l'exemple, chercher un déterminant non nul au lieu d'un vecteur du noyau. En B, oublier le $+1$ de la dérivée de $w\ln w$ (sans conséquence sur les poids, mais la dérivée est fausse), affirmer le minimum sans la convexité, ou encadrer $Z$ dans le mauvais sens.
**Remédiation** : A : M13b.3, M12c.19, M12a.17 et le 🔨 M13b.25 ; B : M13b.14, M13b.16, M13a.15, M14.4.

## CP3.9 — Corriger une copie : cinq erreurs 🐛 · 1,25 point

**Réponse de a)** : `"ACDFH"`. **[0,5]** (0,1 par lettre juste, −0,1 par lettre en trop, sans descendre sous 0)

b) Une ligne par erreur **[0,15 chacune]** :
- **(A)** $\mathbf{w} = 2\mathbf{u}$, donc $\mathbf{u}\mathbf{v}^\top + \mathbf{w}\mathbf{z}^\top = \mathbf{u}\,(\mathbf{v} + 2\mathbf{z})^\top = \mathbf{u}\,(3, 3)^\top$ : rang **1**. Une somme de deux matrices de rang 1 est de rang au plus 2 ; elle vaut 2 seulement si les deux colonnes ($\mathbf{u}$, $\mathbf{w}$) sont indépendantes, et les deux lignes ($\mathbf{v}$, $\mathbf{z}$) aussi.
- **(C)** La formule $(\mathbf{a} \cdot \mathbf{v})\,\mathbf{a}$ suppose $\mathbf{a}$ unitaire ; ici $\lVert \mathbf{a} \rVert^2 = 3$, et la projection vaut $\frac{\mathbf{a} \cdot \mathbf{v}}{\lVert \mathbf{a} \rVert^2}\,\mathbf{a} = (1, 1, 1)$.
- **(D)** Les valeurs propres ne s'additionnent pas (les deux matrices n'ont pas les mêmes vecteurs propres) : $\begin{pmatrix} 5 & 5 \\ 5 & 5 \end{pmatrix}$, de trace 10 et de déterminant 0, a pour valeurs propres **10 et 0**. La trace est une vérification nécessaire, pas suffisante : il faut aussi le déterminant ($7 \times 3 = 21 \ne 0$).
- **(F)** La hinge vaut $\max(0, 1 - 2) = 0$ : un exemple bien classé au-delà de la marge ne coûte rien, et une hinge n'est jamais négative.
- **(H)** $\det = 6 - 16 = -10 < 0$ : les deux valeurs propres sont de signes opposés, la matrice est indéfinie ; par exemple $\mathbf{x} = (1, -1)$ donne $\mathbf{x}^\top\mathbf{M}\mathbf{x} = 3 - 8 + 2 = -3 < 0$. Des coefficients positifs ne suffisent pas : il faut les valeurs propres (ou les mineurs).

Les lignes justes : (B) les valeurs singulières de $2\mathbf{A}$ sont celles de $\mathbf{A}$ multipliées par 2, et leur rapport ne change pas ; (E) le score $\mathbf{w} \cdot \mathbf{x} + b$ est la log-cote, qui augmente de 0,7, et la cote est multipliée par $e^{0{,}7} \approx 2{,}014$ ; (G) $\mathrm{KL}(0{,}4 \Vert 0{,}2) = 0{,}4\ln 2 + 0{,}6\ln 0{,}75 \approx 0{,}27726 - 0{,}17261 = 0{,}10465$, dans le bon ordre des arguments.

**Erreurs fréquentes** : laisser passer (D) parce que la trace est juste ; croire (B) fausse (le conditionnement est un rapport, insensible à l'échelle) ; croire (G) fausse en inversant mentalement les arguments de la KL.
**Remédiation** : M12a.6, M12b.7, M12c.3, M12c.10, M12c.34, M12d.7, M13a.5, M13b.9, M14.8.

## CP3.10 — Problème de synthèse : des données centrées, leurs axes principaux, un modèle sur les scores 🔗 · 2,25 points

**Réponses** : a) `[12, 8, 15]` · b) `[7, -9, 1]` · c) `[58.8, 50.4, 16.8]` · d) `0.867` · e) `[0.143, 0.333]` · f) `0.279` · g) `1` · h) `0.967` · i) `[23, 25]`.

a) $\bar{\mathbf{x}} = \left(\frac{72}{6}, \frac{48}{6}, \frac{90}{6}\right) = (12, 8, 15)$. **[0,25]**
b) $\mathbf{x}_1 - \bar{\mathbf{x}} = (5, 5, -9)$ ; $t_{11} = \frac{95 - 20 + 72}{21} = 7$, $t_{12} = \frac{20 - 65 - 144}{21} = -9$, $t_{13} = \frac{40 + 80 - 99}{21} = 1$. **[0,25]**
c) Les scores sont centrés (leur somme est nulle sur chaque axe) : $\lambda_1 = \frac{6 \times 49}{5} = \frac{294}{5} = 58{,}8$ ; $\lambda_2 = \frac{81 + 9 + 36 + 81 + 9 + 36}{5} = \frac{252}{5} = 50{,}4$ ; $\lambda_3 = \frac{1 + 25 + 16 + 1 + 25 + 16}{5} = \frac{84}{5} = 16{,}8$. **[0,25]**
d) $\frac{58{,}8 + 50{,}4}{58{,}8 + 50{,}4 + 16{,}8} = \frac{109{,}2}{126} = \frac{13}{15} \approx 0{,}867$. **[0,25]**
e) $\bar{y} = \frac{120}{6} = 20$ et $\mathbf{y} - \bar{y} = (-2, -2, 7, 0, 4, -7)$. Les colonnes de scores sont centrées et orthogonales deux à deux (par exemple $\mathbf{t}_1 \cdot \mathbf{t}_2 = 7(-9 + 3 + 6) - 7(9 - 3 - 6) = 0$) : les équations normales du modèle sur $(1, t_1, t_2)$ sont diagonales, la constante vaut $\bar{y}$ et $w_j = \frac{\mathbf{t}_j \cdot (\mathbf{y} - \bar{y})}{\lVert \mathbf{t}_j \rVert^2}$. $\mathbf{t}_1 \cdot (\mathbf{y} - \bar{y}) = 7 \times 3 - 7 \times (-3) = 42$, donc $w_1 = \frac{42}{294} = \frac{1}{7} \approx 0{,}143$ ; $\mathbf{t}_2 \cdot (\mathbf{y} - \bar{y}) = 18 - 6 + 42 + 0 - 12 + 42 = 84$, donc $w_2 = \frac{84}{252} = \frac{1}{3} \approx 0{,}333$. **[0,25]**
f) $\mathrm{SCT} = 4 + 4 + 49 + 0 + 16 + 49 = 122$. Chaque axe explique $w_j^2\,\lVert \mathbf{t}_j \rVert^2 = \frac{(\mathbf{t}_j \cdot (\mathbf{y} - \bar{y}))^2}{\lVert \mathbf{t}_j \rVert^2}$ : $\frac{42^2}{294} = 6$ et $\frac{84^2}{252} = 28$. $R^2 = \frac{6 + 28}{122} = \frac{34}{122} \approx 0{,}279$. **[0,25]**
g) $\mathbf{t}_3 \cdot (\mathbf{y} - \bar{y}) = -2 + 10 + 28 + 0 + 20 + 28 = 84$, donc $w_3 = \frac{84}{84} = 1$. **[0,25]**
h) Le troisième axe explique $\frac{84^2}{84} = 84$ : $R^2 = \frac{6 + 28 + 84}{122} = \frac{118}{122} \approx 0{,}967$. **[0,25]**
i) $\mathbf{x} - \bar{\mathbf{x}} = (14, -3, -2)$, de scores $\left(\frac{266 + 12 + 16}{21}, \frac{56 + 39 - 32}{21}, \frac{112 - 48 - 22}{21}\right) = (14, 3, 2)$. À deux axes : $20 + \frac{14}{7} + \frac{3}{3} = 23$ ; à trois axes : $23 + 1 \times 2 = 25$. **[0,25]**

Sur ta copie :
- Les équations normales ont pour matrice $\mathbf{T}^\top\mathbf{T}$ (avec la colonne de 1) ; les colonnes de scores sont centrées (orthogonales à la colonne de 1) et décorrélées (orthogonales entre elles, ∂ M12d.19), donc cette matrice est diagonale, et chaque poids se calcule seul : ajouter $t_3$ ajoute une équation, sans toucher aux deux autres. $w_1$ et $w_2$ ne changent pas.
- d), f) et h) : les deux premiers axes gardent 87 % de la variance de $\mathbf{x}$, mais n'expliquent que 28 % de celle de $y$ ; le troisième axe, 13 % de la variance de $\mathbf{x}$, en explique à lui seul $\frac{84}{122} \approx 69$ %. L'ACP range les axes selon la variance des features, sans regarder la cible : un axe de petite variance peut être le plus utile pour prédire. Choisir $k$ par la part de variance de $\mathbf{x}$ ne garantit rien pour la prédiction ; il faut juger sur $y$ (par validation).
- Avec les trois axes, $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$ forment une base orthonormée de $\mathbb{R}^3$ : les scores sont des combinaisons linéaires inversibles de $x_1 - \bar{x}_1, x_2 - \bar{x}_2, x_3 - \bar{x}_3$, et les colonnes $(1, t_1, t_2, t_3)$ engendrent le même sous-espace que $(1, x_1, x_2, x_3)$. Les moindres carrés projettent $\mathbf{y}$ sur ce sous-espace (M12b) : mêmes prédictions, même $R^2$. Le modèle s'écrit dans les unités d'origine avec $\boldsymbol{\beta} = w_1\mathbf{u}_1 + w_2\mathbf{u}_2 + w_3\mathbf{u}_3$.

Le lien avec workbookIA : réduire la dimension avant d'ajuster un modèle, dans un pipeline, est un réflexe courant ; ce problème montre ce qu'il coûte quand l'information utile est dans une direction de faible variance, et pourquoi le nouvel exemple se centre avec la moyenne d'**entraînement** avant d'être projeté.

**Erreurs fréquentes** : en b), oublier de centrer, ou de diviser par 21 ; en c), diviser par $n = 6$ ; en d), donner la part du premier axe seul ; en e), diviser $\mathbf{t}_j \cdot \mathbf{y}$ par la variance $\lambda_j$ au lieu de $\lVert \mathbf{t}_j \rVert^2 = (n - 1)\lambda_j$ ; en f), calculer le $R^2$ sans retrancher $\bar{y}$ dans la SCT ; en g), croire qu'il faut tout recalculer ; en i), centrer le nouvel exemple avec sa propre valeur, ou ne pas le centrer.
**Remédiation** : M12d.8, M12d.9, M12d.11, M12d.19, M12b.10, M12b.19, et les équations normales de M09b.

## Barème récapitulatif et remédiation

| Question | Points | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP3.Q1 | 1,5 | M12a à M14 | les exercices cités au CP3.Q1, puis les quiz et les flashcards des chapitres concernés |
| CP3.1 | 2 | M12a | M12a.3, M12a.4, M12a.5, M12a.9, M12a.10, M12a.13, M12a.17 |
| CP3.2 | 2 | M12b | M12b.4, M12b.7, M12b.9, M12b.10, M12b.11, M12b.17 |
| CP3.3 | 2 | M12c | M12c.3, M12c.7, M12c.10, M12c.11, M12c.16 |
| CP3.4 | 2 | M12d | M12d.1, M12d.4, M12d.7, M12d.16 |
| CP3.5 | 1,75 | M13a | M13a.1, M13a.3, M13a.6, M13a.10, M13a.14 |
| CP3.6 | 1,75 | M13b | M13b.1, M13b.2, M13b.9, M13b.10, M13b.13, M13b.19 |
| CP3.7 | 1,5 | M14 | M14.1, M14.3, M14.4, M14.8 |
| CP3.8 | 2 | M13b, M12c ou M14 | A : M13b.3, M12c.19, M12a.17 ; B : M13b.14, M13b.16, M13a.15, M14.4 |
| CP3.9 | 1,25 | M12a à M14 | M12a.6, M12b.7, M12c.3, M12c.10, M12d.7, M13a.5, M13b.9, M14.8 |
| CP3.10 | 2,25 | M12d, M12b, M09b | M12d.8, M12d.9, M12d.11, M12d.19, M12b.10, M12b.19 |
| **Total** | **20** | | |

**Lire ta note**
- **16 à 20** : la partie III est solide. Passe au checkpoint III de workbookIA ; garde les flashcards de la partie III dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe au checkpoint III de workbookIA.
- **8 à moins de 12** : avant le checkpoint III de workbookIA, fais la remédiation, relis ta synthèse et les fiches des chapitres concernés.
- **Moins de 8** : reprends les exercices ★★ des chapitres où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
