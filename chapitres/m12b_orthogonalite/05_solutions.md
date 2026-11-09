# M12b · Orthogonalité et projections — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12b.Q1 — Produit scalaire ou pas ? Symétrie et positivité
1. **Oui** : la matrice est $\operatorname{diag}(2, 5)$, et $2x_1^2 + 5x_2^2 > 0$ pour $\mathbf{x} \ne \mathbf{0}$.
2. **Non** : bilinéaire et symétrique, mais pas défini positif : $\langle (1, -1), (1, -1) \rangle = -2$.
3. **Oui** : la matrice $\begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}$ a $a = 1 > 0$ et $ac - b^2 = 2 > 0$ ; $\langle \mathbf{x}, \mathbf{x} \rangle = (x_1 + x_2)^2 + 2x_2^2$.
4. **Non** : pas symétrique : $\langle \mathbf{e}_1, \mathbf{e}_2 \rangle = 2$ mais $\langle \mathbf{e}_2, \mathbf{e}_1 \rangle = 0$.
5. **Non** : bilinéaire et symétrique, mais $\langle (1, -1), (1, -1) \rangle = 0$ pour un vecteur non nul.
6. **Non** : pas bilinéaire : $\langle -\mathbf{x}, \mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$, au lieu de $-\langle \mathbf{x}, \mathbf{y} \rangle$ (avec $\mathbf{x} = \mathbf{y} = \mathbf{e}_1$ : $1$ au lieu de $-1$).

### M12b.Q2 — Orthogonale, orthonormée, matrice orthogonale
1. **Orthogonaux** ($10 - 10 = 0$), **pas orthonormés** (normes $\sqrt{29}$).
2. **Oui** : $(0, 1)$ et $(-1, 0)$ sont unitaires et orthogonaux ; c'est la rotation d'un quart de tour.
3. **Non** : ses colonnes sont orthogonales, mais de normes 2 et $\frac{1}{2}$ ; elle ne conserve pas les longueurs.
4. $\mathbf{Q}^{-1} = \mathbf{Q}^\top$.
5. **Vrai** : $\lVert \mathbf{Q}\mathbf{x} - \mathbf{Q}\mathbf{y} \rVert = \lVert \mathbf{Q}(\mathbf{x} - \mathbf{y}) \rVert = \lVert \mathbf{x} - \mathbf{y} \rVert$.
6. $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}_2$ ; **non**, $\mathbf{Q}\mathbf{Q}^\top$ est de rang 2, c'est la projection sur le plan des colonnes, pas $\mathbf{I}_3$.

### M12b.Q3 — Gram-Schmidt : ce que chaque étape retire
1. Ses projections sur $\mathbf{q}_1, \ldots, \mathbf{q}_{k-1}$ : la partie de $\mathbf{a}_k$ qui est déjà dans $\operatorname{Vect}(\mathbf{a}_1, \ldots, \mathbf{a}_{k-1})$.
2. Pour que $\mathbf{q}_k$ soit unitaire : les projections des étapes suivantes s'écrivent alors $\langle \mathbf{a}, \mathbf{q}_k \rangle\,\mathbf{q}_k$, sans division.
3. $\mathbf{v}_k = \mathbf{0}$ : on ne peut pas le normer ; la famille est liée (`gram_schmidt` lève une erreur).
4. $\mathbf{q}_1 = (1, 0)$, puis $\mathbf{v}_2 = (1, 2) - 1 \cdot (1, 0) = (0, 2)$ et $\mathbf{q}_2 = (0, 1)$ : la base canonique.
5. **Faux** : en commençant par $(1, 2)$, on obtiendrait $\mathbf{q}_1 = \frac{1}{\sqrt{5}}(1, 2)$, une autre base.
6. **Vrai** : c'est même le but du procédé.

### M12b.Q4 — Le complément orthogonal : vrai ou faux
1. **Vrai** : dimension $3 - 2 = 1$, la droite de son vecteur normal.
2. **Vrai** : tout vecteur est orthogonal à $\mathbf{0}$ ; seul $\mathbf{0}$ est orthogonal à tout $\mathbb{R}^n$.
3. **Faux** : $U^\perp$ est un sous-espace (il contient $\mathbf{0}$) ; un vecteur hors de $U$ n'est pas forcément orthogonal à $U$.
4. **Faux** : $(\operatorname{Im}\mathbf{A})^\perp = \ker\mathbf{A}^\top$ (les formes ne collent même pas : $\ker\mathbf{A}$ vit dans $\mathbb{R}^n$, $\operatorname{Im}\mathbf{A}$ dans $\mathbb{R}^m$).
5. **Vrai** : $5 - 3 = 2$.
6. **Vrai** (en dimension finie).

### M12b.Q5 — Une matrice de projection : sur quoi, et quelles propriétés ?
1. Sur le plan $\operatorname{Vect}(\mathbf{e}_1, \mathbf{e}_2)$, le plan $z = 0$ : elle annule la troisième coordonnée.
2. $\mathbf{P}^2 = \mathbf{P}$ et $\mathbf{P}^\top = \mathbf{P}$.
3. Trace 2, rang 2 : la dimension du plan.
4. Sur la droite $\operatorname{Vect}\big((1, 1)\big)$ : c'est $\mathbf{u}\mathbf{u}^\top$ avec $\mathbf{u} = \frac{1}{\sqrt{2}}(1, 1)$.
5. **Faux** : son noyau, $U^\perp$, n'est pas $\{\mathbf{0}\}$.
6. **Vrai** : c'est la projection orthogonale sur $U^\perp$ ($(\mathbf{I} - \mathbf{P})^2 = \mathbf{I} - 2\mathbf{P} + \mathbf{P}^2 = \mathbf{I} - \mathbf{P}$, et elle est symétrique).

### M12b.Q6 — Moindres carrés et projection
1. Le projeté de $\mathbf{y}$ sur $\operatorname{Im}\mathbf{X}$, l'espace des colonnes.
2. À chaque colonne de $\mathbf{X}$, donc à tout $\operatorname{Im}\mathbf{X}$ : $\mathbf{X}^\top(\mathbf{y} - \hat{\mathbf{y}}) = \mathbf{0}$.
3. 0 : le résidu est orthogonal à la colonne de 1.
4. $\mathbf{0}$ : $\mathbf{y}$ est son propre projeté.
5. **Vrai** : $\operatorname{Im}\mathbf{X}$ grandit, et le point le plus proche ne peut qu'être aussi proche ou plus proche (sur les données d'entraînement).
6. **Faux** : ils sont verticaux ; l'angle droit est dans $\mathbb{R}^n$.

### M12b.Q7 — QR : formes et propriétés
1. $\mathbf{Q}$ de forme $(5, 3)$, $\mathbf{R}$ de forme $(3, 3)$.
2. $\mathbf{I}_3$.
3. Triangulaire supérieure, de diagonale positive (avec la convention de Gram-Schmidt).
4. $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$, résolu en remontant.
5. **Faux** : par Householder, des $r_{kk}$ peuvent être négatifs (M12b.27).
6. **Faux** : $\mathbf{Q}\mathbf{Q}^\top$ est de rang 3, la projection sur $\operatorname{Im}\mathbf{A}$.

### M12b.Q8 — Des fonctions orthogonales
1. **Oui** : $\int_{-1}^1 x\,dx = 0$.
2. **Non** : $\int_{-1}^1 x^4\,dx = \frac{2}{5}$.
3. **Oui** : leur produit est impair, d'intégrale nulle sur un intervalle symétrique.
4. $\sqrt{2}$ : $\int_{-1}^1 1\,dx = 2$.
5. **Non** : $\int_0^1 x\,dx = \frac{1}{2}$.
6. $f^2$ est continue, positive, et strictement positive en un point $x_0$ où $f(x_0) \ne 0$ ; par continuité, elle reste supérieure à $\frac{f(x_0)^2}{2}$ sur un petit intervalle autour de $x_0$, ce qui donne une intégrale strictement positive.

<a id="rappels"></a>

## 🔁 Rappels

### M12b.R1 — La projection sur une droite (M07)
1. $1 + 3 + 8 = 12$.
2. $1 + 1 + 4 = 6$.
3. $\frac{12}{6}\,\mathbf{u} = (2, 2, 4)$.
4. $(-1, 1, 0)$, et $(-1, 1, 0) \cdot (1, 1, 2) = -1 + 1 + 0 = 0$.
5. $\lVert (-1, 1, 0) \rVert = \sqrt{2} \approx 1{,}414$.
6. $(6, 6, 12)$ : la projection est linéaire.

### M12b.R2 — Les équations normales et la matrice chapeau (M09b)
1. $\begin{pmatrix} 3 & 0 \\ 0 & 8 \end{pmatrix}$ : les abscisses sont centrées, la matrice est diagonale.
2. $(9, 6)$.
3. $\mathbf{w}^* = (3 ;\ 0{,}75)$.
4. $\hat{\mathbf{y}} = (1{,}5 ;\ 3 ;\ 4{,}5)$, résidu $(-0{,}5 ;\ 1 ;\ -0{,}5)$, de somme nulle.
5. 2 : le nombre de colonnes de $\mathbf{X}$.
6. $\mathbf{H}^2 = \mathbf{H}$ et $\mathbf{H}^\top = \mathbf{H}$ : ce chapitre (§5 et §6) explique pourquoi.

### M12b.R3 — Base, rang et noyau (M12a)
1. 2 : la forme réduite est $\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & -1 \end{pmatrix}$.
2. $4 - 2 = 2$.
3. $(-2, 1, 0, 0)$ et $(-1, 0, 1, 1)$.
4. Les colonnes 1 et 3 de $\mathbf{A}$ : $(1, 2)$ et $(0, 1)$.
5. **Oui** : rang 2 dans $\mathbb{R}^2$.
6. Aux **lignes** de $\mathbf{A}$ : $\mathbf{A}\mathbf{x} = \mathbf{0}$ dit que chaque ligne a un produit scalaire nul avec $\mathbf{x}$ (fiche §4).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12b.1 — Un produit scalaire défini par une matrice 2 × 2 : normes, angles, orthogonalité

**Réponses** : a) `True` · b) `1` · c) `1.732` · d) `0.577` · e) `3` · f) `True` · g) `-2` · h) `False`.

**Démarche.**
- a) $\mathbf{M}$ est symétrique, $a = 3 > 0$ et $ac - b^2 = 3 - 1 = 2 > 0$. En effet, $\mathbf{x}^\top\mathbf{M}\mathbf{x} = 3x_1^2 + 2x_1x_2 + x_2^2 = (x_1 + x_2)^2 + 2x_1^2$.
- b) $\langle \mathbf{e}_1, \mathbf{e}_2 \rangle_{\mathbf{M}} = M_{12} = 1$.
- c) $\lVert \mathbf{e}_1 \rVert_{\mathbf{M}} = \sqrt{M_{11}} = \sqrt{3}$.
- d) $\frac{1}{\sqrt{3} \times \sqrt{1}} = \frac{1}{\sqrt{3}} \approx 0{,}577$ : environ $54{,}7°$ (et non $90°$).
- e) $(2, -1)^\top\mathbf{M}(2, -1) = (2, -1) \cdot (5, 1) = 9$ : la norme vaut 3 (la norme usuelle vaut $\sqrt{5}$).
- f) $(1, -1)^\top\mathbf{M}\,\mathbf{e}_2 = (1, -1) \cdot (1, 1) = 0$.
- g) $\mathbf{M}(1, 1) = (4, 2)$, et $(1, k) \cdot (4, 2) = 4 + 2k = 0$ donne $k = -2$.
- h) $ac - b^2 = 8 - 9 = -1 < 0$ : pour $\mathbf{x} = (3, -2)$, $\mathbf{x}^\top\mathbf{N}\mathbf{x} = 18 - 36 + 16 = -2 < 0$.

Pour la copie : f) avec le produit usuel donne $-1$ : les mêmes vecteurs ne sont orthogonaux que pour $\langle \cdot, \cdot \rangle_{\mathbf{M}}$. $\lVert \mathbf{e}_2 \rVert_{\mathbf{M}} = 1$ et $\lVert (1, -1) \rVert_{\mathbf{M}}^2 = 0 + 2 = 2$ : $\big(\mathbf{e}_2,\ \frac{1}{\sqrt{2}}(1, -1)\big)$ est une base orthonormée pour $\langle \cdot, \cdot \rangle_{\mathbf{M}}$.

**Erreurs fréquentes.** Calculer normes et angles avec le produit usuel (en d), on trouve 0) ; en g), écrire $(1, k) \cdot (1, 1) = 0$ ; croire qu'une matrice symétrique à coefficients positifs (h) définit toujours un produit scalaire.

**Variante.** $\lVert (1, 1) \rVert_{\mathbf{M}}$ ? *Réponse* : $(1, 1) \cdot (4, 2) = 6$, donc $\sqrt{6} \approx 2{,}449$.

### Ex M12b.2 — Les coordonnées dans une base orthonormée : des produits scalaires au lieu d'un système

**Réponses** : a) `0` · b) `1` · c) `[3, -2, 1, 1]` · d) `15` · e) `[1.4, -1.2, 1.4, 0.8]` · f) `[3, -2, 1, 0.5]`.

**Démarche.**
- a) $\frac{1}{25}(2 - 2 - 8 + 8) = 0$.
- b) $\frac{1}{5}\sqrt{4 + 16 + 1 + 4} = 1$.
- c) $\mathbf{x} \cdot \mathbf{u}_1 = \frac{1}{5}(1 + 4 + 6 + 4) = 3$, $\mathbf{x} \cdot \mathbf{u}_2 = \frac{1}{5}(2 - 2 - 12 + 2) = -2$, $\mathbf{x} \cdot \mathbf{u}_3 = \frac{1}{5}(2 + 8 - 3 - 2) = 1$, $\mathbf{x} \cdot \mathbf{u}_4 = \frac{1}{5}(4 - 4 + 6 - 1) = 1$.
- d) Parseval : $9 + 4 + 1 + 1 = 15 = 1 + 4 + 9 + 1$.
- e) $\mathbf{u}_1 - \mathbf{u}_3 + 2\mathbf{u}_4 = \frac{1}{5}(1 - 2 + 8,\ 2 - 4 - 4,\ 2 + 1 + 4,\ 4 + 2 - 2) = \frac{1}{5}(7, -6, 7, 4)$.
- f) Les trois premières ne changent pas ; la dernière vaut $\frac{\mathbf{x} \cdot 2\mathbf{u}_4}{\lVert 2\mathbf{u}_4 \rVert^2} = \frac{2}{4} = 0{,}5$.

Pour la copie : $3\mathbf{u}_1 - 2\mathbf{u}_2 + \mathbf{u}_3 + \mathbf{u}_4 = \frac{1}{5}(3 - 4 + 2 + 4,\ 6 + 2 + 4 - 2,\ 6 + 8 - 1 + 2,\ 12 - 4 - 2 - 1) = (1, 2, 3, 1)$. En f), le vecteur de base est deux fois plus long : la coordonnée est deux fois plus petite. Résoudre un système $4 \times 4$ par le pivot de Gauss demande de l'ordre de $\frac{2}{3}n^3 \approx 40$ opérations ; quatre produits scalaires, $4 \times 7 = 28$, et surtout aucune élimination.

**Erreurs fréquentes.** Oublier le facteur $\frac{1}{5}$ (on trouve 15, −10, 5, 5) ; en e), calculer $\mathbf{U}^\top\mathbf{c}$ au lieu de $\mathbf{U}\mathbf{c}$ ; en f), garder la formule $c_i = \mathbf{x} \cdot \mathbf{u}_i$ pour un vecteur qui n'est plus unitaire.

**Variante.** Les coordonnées de $\mathbf{e}_1$ dans la base ? *Réponse* : les premières coordonnées des $\mathbf{u}_i$, $(0{,}2 ;\ 0{,}4 ;\ 0{,}4 ;\ 0{,}8)$.

### Ex M12b.3 — Une matrice orthogonale 3 × 3 conserve normes et angles

**Réponses** : a) `True` · b) `[0.7143, -0.4286, 1.1429]` · c) `1.4142` · d) `-1` · e) `[2, 6, 3]` · f) `False` · g) `True`.

**Démarche.**
- a) Les colonnes $\frac{1}{7}(2, 3, 6)$, $\frac{1}{7}(6, 2, -3)$, $\frac{1}{7}(3, -6, 2)$ sont de norme $\frac{7}{7} = 1$ ($4 + 9 + 36 = 49$), et deux à deux orthogonales : $12 + 6 - 18 = 0$, $6 - 18 + 12 = 0$, $18 - 12 - 6 = 0$.
- b) $\mathbf{Q}\mathbf{x}$ = colonne 1 + colonne 3 $= \frac{1}{7}(5, -3, 8)$.
- c) $\frac{1}{7}\sqrt{25 + 9 + 64} = \frac{\sqrt{98}}{7} = \sqrt{2}$.
- d) $\mathbf{Q}\mathbf{y}$ = colonne 2 − colonne 3 $= \frac{1}{7}(3, 8, -5)$, et $\frac{1}{49}(15 - 24 - 40) = -1$.
- e) $\mathbf{z} = \mathbf{Q}^\top(7, 0, 0)$ : 7 fois la première **ligne** de $\mathbf{Q}$, $(2, 6, 3)$.
- f) $(2\mathbf{Q})^\top(2\mathbf{Q}) = 4\mathbf{I}$.
- g) $\mathbf{P}$ échange les deux premières coordonnées : elle est orthogonale, et le produit aussi ($\mathbf{Q}\mathbf{P}$ échange les deux premières colonnes de $\mathbf{Q}$).

Pour la copie : $\lVert \mathbf{x} \rVert = \sqrt{2}$ et $\mathbf{x} \cdot \mathbf{y} = -1$ : égaux à c) et d). L'angle : $\cos\theta = \frac{-1}{\sqrt{2}\,\sqrt{2}} = -\frac{1}{2}$, soit $120°$, avant comme après. e) Inverser une matrice orthogonale, c'est la transposer. $\mathbf{Q}$ n'est pas symétrique ($Q_{12} = \frac{6}{7}$, $Q_{21} = \frac{3}{7}$) : $\mathbf{Q}(7, 0, 0) = (2, 3, 6)$ serait faux.

**Erreurs fréquentes.** En b), combiner les **lignes** de $\mathbf{Q}$ ; en e), résoudre par $\mathbf{Q}(7, 0, 0)$ ; en f), croire qu'un multiple d'une matrice orthogonale l'est encore.

**Variante.** $\lVert \mathbf{Q}(1, 1, 1) \rVert$ ? *Réponse* : $\sqrt{3}$, sans calcul (et $\mathbf{Q}(1, 1, 1) = \frac{1}{7}(11, -1, 5)$ le confirme : $\frac{\sqrt{147}}{7} = \sqrt{3}$).

### Ex M12b.4 — Gram-Schmidt sur trois vecteurs de ℝ³

**Réponses** : a) `9` · b) `-3` · c) `[2.3333, 1.3333, -1.3333]` · d) `3` · e) `[0.7778, 0.4444, -0.4444]` · f) `[-1, 1]` · g) `[-0.4444, 0.8889, 0.1111]` · h) `True`.

**Démarche.**
- a) $\sqrt{16 + 1 + 64} = 9$, et $\mathbf{q}_1 = \frac{1}{9}(4, 1, 8)$.
- b) $\frac{1}{9}(4 + 1 - 32) = -3$.
- c) $\mathbf{v}_2 = \mathbf{a}_2 + 3\mathbf{q}_1 = (1, 1, -4) + \frac{1}{3}(4, 1, 8) = \frac{1}{3}(7, 4, -4)$.
- d) $\frac{1}{3}\sqrt{49 + 16 + 16} = \frac{9}{3} = 3$.
- e) $\mathbf{q}_2 = \frac{1}{9}(7, 4, -4)$.
- f) $\mathbf{a}_3 \cdot \mathbf{q}_1 = \frac{1}{9}(-4 + 3 - 8) = -1$ et $\mathbf{a}_3 \cdot \mathbf{q}_2 = \frac{1}{9}(-7 + 12 + 4) = 1$.
- g) $\mathbf{v}_3 = \mathbf{a}_3 + \mathbf{q}_1 - \mathbf{q}_2 = (-1, 3, -1) + \frac{1}{9}(-3, -3, 12) = \frac{1}{3}(-4, 8, 1)$, de norme $\frac{9}{3} = 3$ : $\mathbf{q}_3 = \frac{1}{9}(-4, 8, 1)$.
- h) Vrai, c'est le résultat de M12b.15.

Pour la copie : $\mathbf{q}_1 \cdot \mathbf{q}_2 = \frac{1}{81}(28 + 4 - 32) = 0$, $\mathbf{q}_1 \cdot \mathbf{q}_3 = \frac{1}{81}(-16 + 8 + 8) = 0$, $\mathbf{q}_2 \cdot \mathbf{q}_3 = \frac{1}{81}(-28 + 32 - 4) = 0$ ; les trois normes valent $\frac{9}{9}$. $\mathbf{a}_2 = -3\mathbf{q}_1 + 3\mathbf{q}_2$ et $\mathbf{a}_3 = -\mathbf{q}_1 + \mathbf{q}_2 + 3\mathbf{q}_3$ : ce sont les colonnes de $\mathbf{R}$ (§7). Le procédé modifié retire d'abord $-\mathbf{q}_1$, donnant $\mathbf{a}_3 + \mathbf{q}_1 = \frac{1}{9}(-5, 28, -1)$, puis son produit scalaire avec $\mathbf{q}_2$, $\frac{1}{81}(-35 + 112 + 4) = 1$ : le même $\mathbf{v}_3$, en calcul exact.

**Erreurs fréquentes.** Soustraire $-3\mathbf{q}_1$ comme si c'était $3\mathbf{q}_1$ (le signe de b) ; retirer la projection sur $\mathbf{a}_1$ au lieu de $\mathbf{q}_1$ ; oublier de normer $\mathbf{v}_2$ et $\mathbf{v}_3$.

**Variante.** Les coordonnées de $\mathbf{a}_3$ dans la base $(\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3)$ ? *Réponse* : $(-1, 1, 3)$ ; la troisième est $\mathbf{a}_3 \cdot \mathbf{q}_3 = \frac{1}{9}(4 + 24 - 1) = 3 = \lVert \mathbf{v}_3 \rVert$.

### Ex M12b.5 — Gram-Schmidt pour un produit scalaire qui n'est pas l'usuel

**Réponses** : a) `-2` · b) `2` · c) `[0.5, 0.5, -0.5]` · d) `[2.5, -0.5, 1.5]` · e) `3` · f) `[0.8333, -0.1667, 0.5]` · g) `[1, 3]` · h) `[3, 0, 1]`.

**Démarche.**
- a) $2 + 2 \times (1 \times (-1)) + (-1) \times 2 = 2 - 2 - 2 = -2$.
- b) $\sqrt{1 + 2 + 1} = 2$, donc $\mathbf{q}_1 = \frac{1}{2}(1, 1, -1)$ (c).
- d) $\langle \mathbf{a}_2, \mathbf{q}_1 \rangle_{\mathbf{D}} = \frac{1}{2}(-2) = -1$, donc $\mathbf{v}_2 = \mathbf{a}_2 + \mathbf{q}_1 = (2{,}5 ;\ -0{,}5 ;\ 1{,}5)$.
- e) $6{,}25 + 2 \times 0{,}25 + 2{,}25 = 9$ : $\lVert \mathbf{v}_2 \rVert_{\mathbf{D}} = 3$, et $\mathbf{q}_2 = \frac{1}{6}(5, -1, 3)$ (f).
- g) $\langle \mathbf{x}, \mathbf{q}_1 \rangle_{\mathbf{D}} = \frac{1}{2}(4 - 4 + 2) = 1$ et $\langle \mathbf{x}, \mathbf{q}_2 \rangle_{\mathbf{D}} = \frac{1}{6}(20 + 4 - 6) = 3$.
- h) $\mathbf{q}_1 + 3\mathbf{q}_2 = (0{,}5 + 2{,}5 ;\ 0{,}5 - 0{,}5 ;\ -0{,}5 + 1{,}5) = (3, 0, 1)$ : c'est $\mathbf{a}_1 + \mathbf{a}_2$.

Pour la copie : $\langle \mathbf{q}_1, \mathbf{q}_2 \rangle_{\mathbf{D}} = \frac{1}{12}(5 - 2 - 3) = 0$ et $\lVert \mathbf{q}_2 \rVert_{\mathbf{D}}^2 = \frac{1}{36}(25 + 2 + 9) = 1$ ; mais $\mathbf{q}_1 \cdot \mathbf{q}_2 = \frac{1}{12}(5 - 1 - 3) = \frac{1}{12} \ne 0$ : orthonormés pour $\langle \cdot, \cdot \rangle_{\mathbf{D}}$, pas pour le produit usuel. Le résidu $\mathbf{x} - \mathbf{p} = (1, -2, -3)$ vérifie $\langle \cdot, \mathbf{a}_1 \rangle_{\mathbf{D}} = 1 - 4 + 3 = 0$ et $\langle \cdot, \mathbf{a}_2 \rangle_{\mathbf{D}} = 2 + 4 - 6 = 0$ ; pour le produit usuel, $(1, -2, -3) \cdot \mathbf{a}_1 = 1 - 2 + 3 = 2 \ne 0$ : la projection dépend du produit scalaire.

**Erreurs fréquentes.** Oublier le poids 2 dans un produit ou une norme ; normer avec la norme usuelle ($\sqrt{3}$ en b) ; en d), retrancher $\mathbf{q}_1$ au lieu de l'ajouter.

**Variante.** Le projeté de $\mathbf{x}$ sur le même plan pour le produit **usuel** ? *Réponse* : la normale usuelle du plan est $\mathbf{a}_1 \times \mathbf{a}_2 = (1, -4, -3)$, $\mathbf{x} \cdot \mathbf{n} = 18$, $\lVert \mathbf{n} \rVert^2 = 26$, donc $\mathbf{p} = \mathbf{x} - \frac{9}{13}\mathbf{n} \approx (3{,}31 ;\ 0{,}77 ;\ 0{,}08)$ : un autre point.

### Ex M12b.6 — Une base du complément orthogonal d'un plan de ℝ⁴

**Réponses** : a) `2` · b) `[-3, 2, 1, 0]` · c) `[1, -2, 0, 1]` · d) `False` · e) `[1, 2]` · f) `False` · g) `True`.

**Démarche.** $U^\perp = \ker\begin{pmatrix} 1 & 0 & 3 & -1 \\ 0 & 1 & -2 & 2 \end{pmatrix}$, déjà réduite : $x_1 = -3x_3 + x_4$ et $x_2 = 2x_3 - 2x_4$.
- a) $4 - 2 = 2$.
- b) $(x_3, x_4) = (1, 0)$ : $(-3, 2, 1, 0)$. c) $(0, 1)$ : $(1, -2, 0, 1)$.
- d) $\mathbf{v} \cdot \mathbf{a} = 3 + 0 - 3 + 0 = 0$, mais $\mathbf{v} \cdot \mathbf{b} = 0 + 1 + 2 + 0 = 3 \ne 0$ : $\mathbf{v}$ est orthogonal à $\mathbf{a}$ seulement.
- e) $\mathbf{w} \cdot \mathbf{a} = -1 + 0 + 3 - 2 = 0$ et $\mathbf{w} \cdot \mathbf{b} = 0 - 2 - 2 + 4 = 0$ ; ses coordonnées libres $(x_3, x_4) = (1, 2)$ : $\mathbf{w} = \mathbf{k}_1 + 2\mathbf{k}_2$.
- f) $\mathbf{k}_1 \cdot \mathbf{k}_2 = -3 - 4 + 0 + 0 = -7$.
- g) $(1, -1, 5, -3) = \mathbf{a} - \mathbf{b}$ ; et, autre façon, il est orthogonal à $\mathbf{k}_1$ ($-3 - 2 + 5 + 0 = 0$) et à $\mathbf{k}_2$ ($1 + 2 + 0 - 3 = 0$), donc dans $(U^\perp)^\perp = U$.

Pour la copie : vérifie $\mathbf{k}_1 \cdot \mathbf{a} = -3 + 3 = 0$, $\mathbf{k}_1 \cdot \mathbf{b} = 2 - 2 = 0$, $\mathbf{k}_2 \cdot \mathbf{a} = 1 - 1 = 0$, $\mathbf{k}_2 \cdot \mathbf{b} = -2 + 2 = 0$. La base du noyau n'est pas orthogonale (f) : pour une base orthonormée, Gram-Schmidt sur $(\mathbf{k}_1, \mathbf{k}_2)$.

**Erreurs fréquentes.** Les signes de $x_1$ et $x_2$ en fonction des variables libres ; chercher $U^\perp$ dans $\mathbb{R}^2$ ; en d), ne tester que $\mathbf{a}$ ; en e), inverser l'ordre des coordonnées.

**Variante.** Une base orthonormée de $U^\perp$ ? *Réponse* : $\mathbf{q}_1 = \frac{1}{\sqrt{14}}(-3, 2, 1, 0)$, puis $\mathbf{k}_2 - \frac{\mathbf{k}_2 \cdot \mathbf{k}_1}{14}\mathbf{k}_1 = \mathbf{k}_2 + \frac{1}{2}\mathbf{k}_1 = \frac{1}{2}(-1, -2, 1, 2)$, de norme $\frac{\sqrt{10}}{2}$ : $\mathbf{q}_2 = \frac{1}{\sqrt{10}}(-1, -2, 1, 2)$, la direction de $\mathbf{w}$.

### Ex M12b.7 — Projeter sur un plan de ℝ³ : avec une base quelconque, puis orthonormée

**Réponses** : a) `[[5, 2], [2, 17]]` · b) `[8, -13]` · c) `[2, -1]` · d) `[2, 4, 3]` · e) `[5, -2]` · f) `[8, -1, -4]` · g) `True`.

**Démarche.**
- a) $\lVert \mathbf{a}_1 \rVert^2 = 5$, $\mathbf{a}_1 \cdot \mathbf{a}_2 = 0 + 0 + 2 = 2$, $\lVert \mathbf{a}_2 \rVert^2 = 16 + 1 = 17$.
- b) $\mathbf{a}_1 \cdot \mathbf{v} = 10 - 2 = 8$, $\mathbf{a}_2 \cdot \mathbf{v} = -12 - 1 = -13$.
- c) $\det = 85 - 4 = 81$, $\mathbf{c} = \frac{1}{81}\begin{pmatrix} 17 & -2 \\ -2 & 5 \end{pmatrix}(8, -13) = \frac{1}{81}(162, -81) = (2, -1)$.
- d) $2\mathbf{a}_1 - \mathbf{a}_2 = (2, 4, 3)$.
- e) $\mathbf{v} \cdot \mathbf{q}_1 = \frac{1}{9}(40 + 12 - 7) = 5$ et $\mathbf{v} \cdot \mathbf{q}_2 = \frac{1}{9}(10 - 24 - 4) = -2$.
- f) $(10 - 2,\ 3 - 4,\ -1 - 3)$.
- g) $(8, -1, -4) \cdot \mathbf{a}_1 = 8 - 8 = 0$ et $\cdot\,\mathbf{a}_2 = 4 - 4 = 0$.

Pour la copie : $5\mathbf{q}_1 - 2\mathbf{q}_2 = \frac{1}{9}(20 - 2,\ 20 + 16,\ 35 - 8) = (2, 4, 3)$. $\mathbf{q}_1 = \frac{1}{9}(4\mathbf{a}_1 - \mathbf{a}_2)$ et $\mathbf{q}_2 = \frac{1}{9}(\mathbf{a}_1 + 2\mathbf{a}_2)$ : ils sont dans $U$ ; $\mathbf{q}_1 \cdot \mathbf{q}_2 = \frac{1}{81}(4 - 32 + 28) = 0$, normes $\frac{9}{9}$. Une fois $\mathbf{q}_1$, $\mathbf{q}_2$ connus, chaque projection ne demande que deux produits scalaires, sans système à résoudre : c'est la méthode à préférer pour dix vecteurs.

**Erreurs fréquentes.** Calculer $\mathbf{A}\mathbf{A}^\top$ (de forme $(3, 3)$) au lieu de $\mathbf{A}^\top\mathbf{A}$ ; confondre le projeté et le résidu ; oublier le facteur $\frac{1}{9}$ en e).

**Variante.** Le projeté de $\mathbf{e}_1$ sur $U$ ? *Réponse* : $\frac{4}{9}\mathbf{q}_1 + \frac{1}{9}\mathbf{q}_2 = \frac{1}{81}(17, 8, 32)$.

### Ex M12b.8 — La matrice de projection : P² = P, Pᵀ = P, trace et rang

**Réponses** : a) `True` · b) `True` · c) `[0, 0, 0]` · d) `[1, 0, 1]` · e) `2` · f) `2` · g) `[1, 1, -1]` · h) `False`.

**Démarche.**
- a) $\mathbf{P}$ est symétrique.
- b) $\mathbf{P}^2 = \frac{1}{9}\begin{pmatrix} 6 & -3 & 3 \\ -3 & 6 & 3 \\ 3 & 3 & 6 \end{pmatrix} = \mathbf{P}$ (par exemple, le coin vaut $\frac{1}{9}(4 + 1 + 1) = \frac{6}{9}$).
- c) $\frac{1}{3}(2 - 1 - 1,\ -1 + 2 - 1,\ 1 + 1 - 2) = \mathbf{0}$ : $(1, 1, -1)$ est dans le noyau.
- d) $\frac{1}{3}(2 + 1,\ -1 + 1,\ 1 + 2) = (1, 0, 1)$ : ce vecteur est inchangé.
- e) $\frac{1}{3}(2 + 2 + 2) = 2$. f) Rang 2 : le noyau contient la droite de c), et la colonne 3 est la somme des deux autres.
- g) $(3, 0, 0) - \mathbf{P}(3, 0, 0) = (3, 0, 0) - (2, -1, 1) = (1, 1, -1)$.
- h) $\mathbf{M}^2 = \mathbf{M}$, mais $\mathbf{M}^\top \ne \mathbf{M}$ : une projection **oblique**.

Pour la copie : symétrique et idempotente, $\mathbf{P}$ est la matrice d'une projection orthogonale. Elle annule $\mathbf{n} = (1, 1, -1)$, donc $U = \mathbf{n}^\perp$, le plan $x + y - z = 0$ ; $(1, 0, 1)$ vérifie cette équation, il est dans $U$ et reste fixe. La trace et le rang valent tous deux $\dim U = 2$. $\mathbf{I} - \mathbf{P} = \frac{1}{3}\mathbf{n}\mathbf{n}^\top$ projette sur la droite $\operatorname{Vect}(\mathbf{n})$. $\mathbf{P}$ n'est pas inversible : son noyau n'est pas nul. $\mathbf{M}(x, y) = (x, x)$ : elle envoie sur la droite $\operatorname{Vect}\big((1, 1)\big)$, le long de la direction $(0, 1)$ (qu'elle annule), pas perpendiculairement.

**Erreurs fréquentes.** Oublier le facteur $\frac{1}{3}$ dans la trace ; confondre $(\mathbf{I} - \mathbf{P})\mathbf{v}$ et $\mathbf{P}\mathbf{v}$ ; conclure « projection orthogonale » de la seule idempotence.

**Variante.** $\mathbf{P}(0, 0, 3)$ ? *Réponse* : $(1, 1, 2)$, la troisième colonne de $\mathbf{P}$ fois 3.

### Ex M12b.9 — La distance d'un point à un sous-espace, et le résidu orthogonal

**Réponses** : a) `True` · b) `2` · c) `1` · d) `[3, 1, 4, 0]` · e) `[-1, -1, 1, 1]` · f) `2` · g) `3.7417` · h) `26`.

**Démarche.**
- a) $1 - 1 + 2 - 2 = 0$.
- b) $\frac{\mathbf{v} \cdot \mathbf{u}_1}{\lVert \mathbf{u}_1 \rVert^2} = \frac{8}{4} = 2$. c) $\frac{\mathbf{v} \cdot \mathbf{u}_2}{\lVert \mathbf{u}_2 \rVert^2} = \frac{2 + 10 - 2}{10} = 1$.
- d) $2\mathbf{u}_1 + \mathbf{u}_2 = (3, 1, 4, 0)$. e) $(2 - 3,\ 0 - 1,\ 5 - 4,\ 1 - 0)$.
- f) $\lVert (-1, -1, 1, 1) \rVert = 2$.
- g) Sur la droite seule : $\lVert \mathbf{v} \rVert^2 - \frac{(\mathbf{v} \cdot \mathbf{u}_1)^2}{\lVert \mathbf{u}_1 \rVert^2} = 30 - 16 = 14$, d'où $\sqrt{14} \approx 3{,}742$.
- h) $9 + 1 + 16 + 0 = 26$.

Pour la copie : $\mathbf{r} \cdot \mathbf{u}_1 = 0$ et $\mathbf{r} \cdot \mathbf{u}_2 = -1 + 1 + 2 - 2 = 0$. Pythagore : $\lVert \mathbf{v} \rVert^2 = 4 + 0 + 25 + 1 = 30 = 26 + 4$. La droite est contenue dans le plan : le point le plus proche dans le plan est au moins aussi proche que dans la droite, donc g) ≥ f), jamais plus petit.

**Erreurs fréquentes.** Oublier de diviser par $\lVert \mathbf{u}_i \rVert^2$ (la base n'est qu'orthogonale) ; donner $\lVert \mathbf{p} \rVert$ ou $\lVert \mathbf{r} \rVert^2$ comme distance.

**Variante.** La distance de $\mathbf{v}$ à la droite $\operatorname{Vect}(\mathbf{u}_2)$ ? *Réponse* : $\sqrt{30 - \frac{100}{10}} = \sqrt{20} \approx 4{,}472$.

### Ex M12b.10 — Des moindres carrés comme une projection : y, son projeté et le résidu

**Réponses** : a) `[[5, 20], [20, 110]]` · b) `[11, 59]` · c) `[0.2, 0.5]` · d) `[0.7, 1.2, 2.2, 2.7, 4.2]` · e) `[-0.7, 0.8, -0.2, 0.3, -0.2]` · f) `[0, 0]` · g) `1.3` · h) `31.7`.

**Démarche.**
- a) $n = 5$, $\sum x_i = 20$, $\sum x_i^2 = 1 + 4 + 16 + 25 + 64 = 110$. b) $\sum y_i = 11$, $\sum x_iy_i = 0 + 4 + 8 + 15 + 32 = 59$.
- c) $\det = 550 - 400 = 150$ ; $\mathbf{w}^* = \frac{1}{150}\begin{pmatrix} 110 & -20 \\ -20 & 5 \end{pmatrix}(11, 59) = \frac{1}{150}(30, 75) = (0{,}2 ;\ 0{,}5)$.
- d) $0{,}2 + 0{,}5\,x_i$. e) $y_i - \hat{y}_i$. f) $\sum r_i = 0$ et $\sum x_ir_i = -0{,}7 + 1{,}6 - 0{,}8 + 1{,}5 - 1{,}6 = 0$.
- g) $0{,}49 + 0{,}64 + 0{,}04 + 0{,}09 + 0{,}04 = 1{,}3$. h) $0{,}49 + 1{,}44 + 4{,}84 + 7{,}29 + 17{,}64 = 31{,}7$.

Pour la copie : la somme des résidus est nulle (f), parce que le résidu est orthogonal à la colonne de 1. $\lVert \mathbf{y} \rVert^2 = 0 + 4 + 4 + 9 + 16 = 33 = 31{,}7 + 1{,}3$. Avec la base orthogonale $\mathbf{1}$, $\mathbf{x} - 4 \cdot \mathbf{1} = (-3, -2, 0, 1, 4)$, de carré de norme 30 : $\frac{\mathbf{y} \cdot \mathbf{1}}{5} = 2{,}2$ et $\frac{\mathbf{y} \cdot (\mathbf{x} - 4)}{30} = \frac{0 - 4 + 0 + 3 + 16}{30} = 0{,}5$ : $\hat{\mathbf{y}} = 2{,}2 + 0{,}5\,(x_i - 4)$, la même droite, écrite autour de la moyenne.

**Erreurs fréquentes.** Inverser le biais et la pente ; prendre $\sum r_i$ pour $\lVert \mathbf{r} \rVert^2$ ; écrire $\mathbf{r} = \hat{\mathbf{y}} - \mathbf{y}$.

**Variante.** La prédiction pour $x = 10$ ? *Réponse* : $0{,}2 + 0{,}5 \times 10 = 5{,}2$.

### Ex M12b.11 — La décomposition QR d'une matrice 3 × 2, puis les moindres carrés par R w = Qᵀy

**Réponses** : a) `11` · b) `2` · c) `3` · d) `[0.5455, 0.6364, -0.5455]` · e) `[[11, 2], [0, 3]]` · f) `[20, -3]` · g) `[2, -1]` · h) `[9, -6, 2]`.

**Démarche.**
- a) $\sqrt{4 + 36 + 81} = 11$, $\mathbf{q}_1 = \frac{1}{11}(2, 6, 9)$.
- b) $\frac{1}{11}(4 + 18 + 0) = 2$.
- c) $\mathbf{v}_2 = (2, 3, 0) - \frac{2}{11}(2, 6, 9) = \frac{1}{11}(18, 21, -18)$, de norme $\frac{33}{11} = 3$.
- d) $\mathbf{q}_2 = \frac{1}{11}(6, 7, -6)$. e) $\mathbf{R} = \begin{pmatrix} 11 & 2 \\ 0 & 3 \end{pmatrix}$.
- f) $\mathbf{q}_1 \cdot \mathbf{y} = \frac{1}{11}(22 + 18 + 180) = 20$, $\mathbf{q}_2 \cdot \mathbf{y} = \frac{1}{11}(66 + 21 - 120) = -3$.
- g) Dernière ligne : $3w_2 = -3$, $w_2 = -1$ ; puis $11w_1 + 2 \times (-1) = 20$, $w_1 = 2$.
- h) $\mathbf{A}\mathbf{w}^* = (2, 9, 18)$, résidu $(9, -6, 2)$.

Pour la copie : $11\mathbf{q}_1 = \mathbf{a}_1$ et $2\mathbf{q}_1 + 3\mathbf{q}_2 = \frac{1}{11}(4 + 18,\ 12 + 21,\ 18 - 18) = (2, 3, 0) = \mathbf{a}_2$. Équations normales : $\mathbf{A}^\top\mathbf{A} = \begin{pmatrix} 121 & 22 \\ 22 & 13 \end{pmatrix}$, $\mathbf{A}^\top\mathbf{y} = (220, 31)$, et $(2, -1)$ les vérifie : $242 - 22 = 220$, $44 - 13 = 31$. Le résidu est orthogonal aux colonnes : $18 - 36 + 18 = 0$ et $18 - 18 + 0 = 0$ ; c'est $11$ fois le troisième vecteur $\frac{1}{11}(9, -6, 2)$ d'une base orthonormée. On commence par la dernière ligne, la seule qui n'ait qu'une inconnue.

**Erreurs fréquentes.** Placer $r_{12}$ sous la diagonale ; résoudre depuis la première ligne en oubliant $r_{12}w_2$ (on trouve $w_1 = \frac{20}{11}$) ; ne pas normer $\mathbf{v}_2$.

**Variante.** Avec $\mathbf{y}' = (9, -6, 2)$ ? *Réponse* : $\mathbf{Q}^\top\mathbf{y}' = \mathbf{0}$, donc $\mathbf{w}^* = \mathbf{0}$ : $\mathbf{y}'$ est orthogonal aux colonnes, son projeté est nul.

### Ex M12b.12 — Le produit scalaire de fonctions sur [−1 ; 1] : orthogonaliser 1, x et x²

**Réponses** : a) `2` · b) `0.6667` · c) `0` · d) `-0.3333` · e) `0.1778` · f) `0.1667` · g) `[0.1875, 0, 0.9375]`.

**Démarche.**
- a) $\int_{-1}^1 1\,dx = 2$. b) $\int_{-1}^1 x^2\,dx = \frac{2}{3}$. c) $\int_{-1}^1 x^3\,dx = 0$ (impaire).
- d) $\langle x, 1 \rangle = 0$, donc $p_1 = x$ ; puis $p_2 = x^2 - \frac{2/3}{2} \cdot 1 - 0 \cdot x = x^2 - \frac{1}{3}$ : $c = -\frac{1}{3}$.
- e) $\int_{-1}^1 \big(x^4 - \frac{2}{3}x^2 + \frac{1}{9}\big)dx = \frac{2}{5} - \frac{4}{9} + \frac{2}{9} = \frac{8}{45} \approx 0{,}1778$.
- f) $\int_{-1}^1 |x|\,x^2\,dx - \frac{1}{3}\int_{-1}^1 |x|\,dx = 2 \times \frac{1}{4} - \frac{1}{3} \times 1 = \frac{1}{6}$.
- g) Coefficients sur la base orthogonale : $\frac{\langle |x|, 1 \rangle}{\langle 1, 1 \rangle} = \frac{1}{2}$, $\frac{\langle |x|, x \rangle}{\langle x, x \rangle} = 0$ (le produit est impair), $\frac{\langle |x|, p_2 \rangle}{\lVert p_2 \rVert^2} = \frac{1/6}{8/45} = \frac{15}{16}$. Le projeté est $\frac{1}{2} + \frac{15}{16}\big(x^2 - \frac{1}{3}\big) = \frac{3}{16} + \frac{15}{16}x^2$.

Pour la copie : $\langle x, 1 \rangle = \int_{-1}^1 x\,dx = 0$, donc rien à retirer. Le projeté vaut $\frac{3}{16}$ en 0, au lieu de 0 : c'est en 0, là où $|x|$ a un coin, que l'approximation est la moins bonne. Sur $\operatorname{Vect}(1, x)$ seul, le projeté est la constante $\frac{1}{2}$, bien moins proche.

**Erreurs fréquentes.** Intégrer sur $[0 ; 1]$ au lieu de $[-1 ; 1]$ ; oublier de diviser par $\langle 1, 1 \rangle = 2$ ; en g), oublier que $p_2$ contient une constante, qui modifie le coefficient de 1.

**Variante.** $\lVert p_1 \rVert^2$ ? *Réponse* : $\int_{-1}^1 x^2\,dx = \frac{2}{3}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12b.13 — L'inégalité de Cauchy-Schwarz pour tout produit scalaire

**Réponse modèle.**
1. Par bilinéarité et symétrie : $\lVert \mathbf{x} - t\mathbf{y} \rVert^2 = \langle \mathbf{x}, \mathbf{x} \rangle - 2t\langle \mathbf{x}, \mathbf{y} \rangle + t^2\langle \mathbf{y}, \mathbf{y} \rangle$.
2. $\langle \mathbf{x} - t\mathbf{y}, \mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle - t\lVert \mathbf{y} \rVert^2 = 0$ : $t\mathbf{y}$ est le projeté de $\mathbf{x}$ sur la droite de $\mathbf{y}$. En reportant $t$ dans 1 : $\lVert \mathbf{x} - t\mathbf{y} \rVert^2 = \lVert \mathbf{x} \rVert^2 - 2\frac{\langle \mathbf{x}, \mathbf{y} \rangle^2}{\lVert \mathbf{y} \rVert^2} + \frac{\langle \mathbf{x}, \mathbf{y} \rangle^2}{\lVert \mathbf{y} \rVert^2} = \lVert \mathbf{x} \rVert^2 - \frac{\langle \mathbf{x}, \mathbf{y} \rangle^2}{\lVert \mathbf{y} \rVert^2}$. Ce nombre est $\ge 0$ (positivité), d'où $\langle \mathbf{x}, \mathbf{y} \rangle^2 \le \lVert \mathbf{x} \rVert^2\lVert \mathbf{y} \rVert^2$, et l'inégalité en prenant les racines. Si $\mathbf{y} = \mathbf{0}$, les deux membres sont nuls ($\langle \mathbf{x}, \mathbf{0} \rangle = 0$ par linéarité).
3. Pour $\mathbf{y} \ne \mathbf{0}$ : égalité $\iff \lVert \mathbf{x} - t\mathbf{y} \rVert = 0 \iff \mathbf{x} = t\mathbf{y}$ (défini positif). Réciproquement, si $\mathbf{x} = \lambda\mathbf{y}$, les deux membres valent $|\lambda|\,\lVert \mathbf{y} \rVert^2$. Si $\mathbf{y} = \mathbf{0}$, il y a égalité et les vecteurs sont colinéaires.
4. $\lVert \mathbf{x} + \mathbf{y} \rVert^2 = \lVert \mathbf{x} \rVert^2 + 2\langle \mathbf{x}, \mathbf{y} \rangle + \lVert \mathbf{y} \rVert^2 \le \lVert \mathbf{x} \rVert^2 + 2\lVert \mathbf{x} \rVert\lVert \mathbf{y} \rVert + \lVert \mathbf{y} \rVert^2 = (\lVert \mathbf{x} \rVert + \lVert \mathbf{y} \rVert)^2$.
5. $\langle f, 1 \rangle = \int_0^1 f$ et $\lVert 1 \rVert^2 = \int_0^1 1 = 1$ : $\left(\int_0^1 f\right)^2 \le \int_0^1 f^2$. Égalité si et seulement si $f$ est colinéaire à 1 : constante. Le carré de la moyenne d'une fonction est au plus la moyenne de son carré ; l'écart entre les deux est une variance, positive.

**Grille.** (1) le développement, avec le double produit ; (2) l'orthogonalité de $\mathbf{x} - t\mathbf{y}$ et $\mathbf{y}$, le calcul, la positivité invoquée, le cas $\mathbf{y} = \mathbf{0}$ ; (3) les deux sens du cas d'égalité, avec « défini positif » ; (4) Cauchy-Schwarz appliqué au double produit ; (5) le bon produit scalaire, $\lVert 1 \rVert = 1$, le cas d'égalité, l'interprétation.

### Ex M12b.14 — Une famille orthogonale de vecteurs non nuls est libre

**Réponse modèle.**
1. $\langle \sum_i \lambda_i\mathbf{u}_i, \mathbf{u}_j \rangle = \sum_i \lambda_i\langle \mathbf{u}_i, \mathbf{u}_j \rangle = \lambda_j\lVert \mathbf{u}_j \rVert^2$, et $\langle \mathbf{0}, \mathbf{u}_j \rangle = 0$. Comme $\mathbf{u}_j \ne \mathbf{0}$, $\lVert \mathbf{u}_j \rVert^2 > 0$, donc $\lambda_j = 0$, pour chaque $j$ : la famille est libre.
2. Pour diviser par $\lVert \mathbf{u}_j \rVert^2$. La famille $(\mathbf{0}, \mathbf{e}_1)$ est orthogonale ($\mathbf{0} \cdot \mathbf{e}_1 = 0$) mais liée.
3. Elle est libre et a $n = \dim\mathbb{R}^n$ vecteurs : c'est une base (M12a §3).
4. Le produit scalaire de $\mathbf{v} = \sum_i c_i\mathbf{u}_i$ avec $\mathbf{u}_j$ donne $\langle \mathbf{v}, \mathbf{u}_j \rangle = c_j\lVert \mathbf{u}_j \rVert^2$.
5. $\lVert \mathbf{v} \rVert^2 = \langle \sum_i c_i\mathbf{q}_i, \sum_j c_j\mathbf{q}_j \rangle = \sum_{i,j} c_ic_j\langle \mathbf{q}_i, \mathbf{q}_j \rangle = \sum_i c_i^2$, seuls les termes $i = j$ restant.

**Grille.** (1) la bilinéarité, le seul terme qui reste, la division justifiée par « non nul » ; (2) un contre-exemple avec le vecteur nul ; (3) le nombre de vecteurs égal à la dimension ; (4) le même calcul qu'en 1 ; (5) le double développement et les termes croisés nuls.

### Ex M12b.15 — Gram-Schmidt donne une base orthonormée du même sous-espace

**Réponse modèle.**
1. $\mathbf{a}_1 \ne \mathbf{0}$ (une famille libre ne contient pas $\mathbf{0}$), donc $\mathbf{q}_1 = \mathbf{a}_1/\lVert \mathbf{a}_1 \rVert$ est défini, unitaire, et $\operatorname{Vect}(\mathbf{q}_1) = \operatorname{Vect}(\mathbf{a}_1)$.
2. Si $\mathbf{v}_j = \mathbf{0}$, alors $\mathbf{a}_j = \sum_{i<j} \langle \mathbf{a}_j, \mathbf{q}_i \rangle\,\mathbf{q}_i \in \operatorname{Vect}(\mathbf{q}_1, \ldots, \mathbf{q}_{j-1}) = \operatorname{Vect}(\mathbf{a}_1, \ldots, \mathbf{a}_{j-1})$ par $(H_{j-1})$ : $\mathbf{a}_j$ combinerait les précédents, contre l'hypothèse de liberté.
3. Pour $i < j$ : $\langle \mathbf{v}_j, \mathbf{q}_i \rangle = \langle \mathbf{a}_j, \mathbf{q}_i \rangle - \sum_{l<j} \langle \mathbf{a}_j, \mathbf{q}_l \rangle\langle \mathbf{q}_l, \mathbf{q}_i \rangle = \langle \mathbf{a}_j, \mathbf{q}_i \rangle - \langle \mathbf{a}_j, \mathbf{q}_i \rangle = 0$, car $\langle \mathbf{q}_l, \mathbf{q}_i \rangle$ vaut 1 si $l = i$ et 0 sinon ($H_{j-1}$). Donc $\mathbf{q}_j = \mathbf{v}_j/\lVert \mathbf{v}_j \rVert$ est unitaire et orthogonal aux précédents.
4. $\mathbf{q}_j$ est une combinaison de $\mathbf{a}_j$ et de $\mathbf{q}_1, \ldots, \mathbf{q}_{j-1}$, donc de $\mathbf{a}_1, \ldots, \mathbf{a}_j$ : $\operatorname{Vect}(\mathbf{q}_1, \ldots, \mathbf{q}_j) \subseteq \operatorname{Vect}(\mathbf{a}_1, \ldots, \mathbf{a}_j)$. Les deux familles sont libres (orthonormée d'un côté, M12b.14 ; par hypothèse de l'autre), de $j$ vecteurs : deux sous-espaces de même dimension $j$, l'un dans l'autre, sont égaux. $(H_j)$ est démontrée ; par récurrence, $(H_k)$.
5. $\mathbf{a}_k \in \operatorname{Vect}(\mathbf{q}_1, \ldots, \mathbf{q}_k)$ : ses coordonnées $r_{jk} = \langle \mathbf{q}_j, \mathbf{a}_k \rangle$ sur les $\mathbf{q}_j$ avec $j > k$ sont nulles, d'où $\mathbf{R}$ triangulaire supérieure. Et $r_{kk} = \langle \mathbf{q}_k, \mathbf{a}_k \rangle = \langle \mathbf{q}_k, \mathbf{v}_k + \sum_{i<k} \langle \mathbf{a}_k, \mathbf{q}_i \rangle\mathbf{q}_i \rangle = \langle \mathbf{q}_k, \mathbf{v}_k \rangle = \lVert \mathbf{v}_k \rVert > 0$.

**Grille.** (1) $\mathbf{a}_1 \ne \mathbf{0}$ justifié ; (2) l'absurde, avec l'hypothèse de récurrence ; (3) le calcul de $\langle \mathbf{v}_j, \mathbf{q}_i \rangle$, avec l'orthonormalité des précédents ; (4) une inclusion, puis l'égalité par les dimensions ; la conclusion par récurrence ; (5) les zéros sous la diagonale et le signe de $r_{kk}$.

### Ex M12b.16 — L'orthogonal de l'image de A est le noyau de Aᵀ

**Réponse modèle.**
1. Les colonnes engendrent $\operatorname{Im}\mathbf{A}$ ; par bilinéarité, $\mathbf{y}$ est orthogonal à tout $\operatorname{Im}\mathbf{A}$ si et seulement s'il l'est à chaque colonne. Or $\mathbf{a}_j \cdot \mathbf{y}$ est la $j$-ième coordonnée de $\mathbf{A}^\top\mathbf{y}$ : $\mathbf{y} \in (\operatorname{Im}\mathbf{A})^\perp \iff \mathbf{A}^\top\mathbf{y} = \mathbf{0}$.
2. La $i$-ième coordonnée de $\mathbf{A}\mathbf{x}$ est le produit scalaire de la ligne $i$ avec $\mathbf{x}$ ; les lignes de $\mathbf{A}$ sont les colonnes de $\mathbf{A}^\top$. Donc $\mathbf{A}\mathbf{x} = \mathbf{0} \iff \mathbf{x}$ est orthogonal à chaque ligne $\iff \mathbf{x} \in (\operatorname{Im}\mathbf{A}^\top)^\perp$.
3. $\mathbf{A}^\top$ a $m$ colonnes : $\dim\ker\mathbf{A}^\top = m - \operatorname{rg}\mathbf{A}^\top = m - \operatorname{rg}\mathbf{A}$. Si $U$ est un sous-espace de $\mathbb{R}^m$, on range une base de $U$ dans les colonnes de $\mathbf{A}$ : $\operatorname{rg}\mathbf{A} = \dim U$, et $\dim U^\perp = m - \dim U$.
4. Si $\mathbf{A}\mathbf{x} = \mathbf{b}$ et $\mathbf{A}^\top\mathbf{y} = \mathbf{0}$, alors $\mathbf{y} \cdot \mathbf{b} = \mathbf{y}^\top\mathbf{A}\mathbf{x} = (\mathbf{A}^\top\mathbf{y})^\top\mathbf{x} = 0$.
5. $\mathbf{A}^\top = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 4 & 1 \end{pmatrix}$ : $x + 2y = 0$ et $2x + 4y + z = 0$ donnent $z = 0$, $x = -2y$ ; $\ker\mathbf{A}^\top = \operatorname{Vect}\big((-2, 1, 0)\big)$. Le système a une solution si et seulement si $(1, t, 0) \cdot (-2, 1, 0) = t - 2 = 0$ : $t = 2$.

**Grille.** (1) la réduction aux colonnes et la lecture de $\mathbf{A}^\top\mathbf{y}$ ; (2) les lignes comme colonnes de $\mathbf{A}^\top$ ; (3) le théorème du rang pour $\mathbf{A}^\top$ (avec ses $m$ colonnes), $\operatorname{rg}\mathbf{A}^\top = \operatorname{rg}\mathbf{A}$, puis le cas général ; (4) le calcul en une ligne ; (5) le noyau, puis la condition.

### Ex M12b.17 — Le projeté orthogonal est le point le plus proche (Pythagore)

**Réponse modèle.**
1. $\mathbf{p}$ est une combinaison des $\mathbf{q}_i$, donc dans $U$. $\langle \mathbf{v} - \mathbf{p}, \mathbf{q}_j \rangle = \langle \mathbf{v}, \mathbf{q}_j \rangle - \sum_i \langle \mathbf{v}, \mathbf{q}_i \rangle\langle \mathbf{q}_i, \mathbf{q}_j \rangle = 0$ ; par bilinéarité, $\mathbf{v} - \mathbf{p}$ est orthogonal à toute combinaison des $\mathbf{q}_j$, donc à $U$.
2. $\lVert \mathbf{a} + \mathbf{b} \rVert^2 = \lVert \mathbf{a} \rVert^2 + 2\langle \mathbf{a}, \mathbf{b} \rangle + \lVert \mathbf{b} \rVert^2$, et $\langle \mathbf{a}, \mathbf{b} \rangle = 0$.
3. $\mathbf{p} - \mathbf{u} \in U$, donc orthogonal à $\mathbf{v} - \mathbf{p}$ (1) ; Pythagore donne $\lVert \mathbf{v} - \mathbf{u} \rVert^2 = \lVert \mathbf{v} - \mathbf{p} \rVert^2 + \lVert \mathbf{p} - \mathbf{u} \rVert^2 \ge \lVert \mathbf{v} - \mathbf{p} \rVert^2$, avec égalité si et seulement si $\lVert \mathbf{p} - \mathbf{u} \rVert = 0$, c'est-à-dire $\mathbf{u} = \mathbf{p}$.
4. $\mathbf{p} - \mathbf{p}' \in U$ (deux vecteurs de $U$), et $\mathbf{p} - \mathbf{p}' = (\mathbf{v} - \mathbf{p}') - (\mathbf{v} - \mathbf{p}) \in U^\perp$ (deux vecteurs de $U^\perp$). Il est orthogonal à lui-même : $\lVert \mathbf{p} - \mathbf{p}' \rVert^2 = 0$, donc $\mathbf{p}' = \mathbf{p}$.
5. $U = \operatorname{Im}\mathbf{X}$ a une base orthonormée (M12b.15), donc un projeté $\mathbf{p}$ (1). Quand $\mathbf{w}$ parcourt $\mathbb{R}^p$, $\mathbf{X}\mathbf{w}$ parcourt $U$. Par 3, $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert$ est minimal si et seulement si $\mathbf{X}\mathbf{w} = \mathbf{p}$, le projeté ; par 4 (et 1), c'est le seul point de $U$ dont l'écart à $\mathbf{y}$ est orthogonal à $U$. Donc $\mathbf{w}^*$ minimise si et seulement si $\mathbf{y} - \mathbf{X}\mathbf{w}^* \perp \operatorname{Im}\mathbf{X}$, c'est-à-dire $\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w}^*) = \mathbf{0}$ (M12b.16).

**Grille.** (1) l'appartenance et le calcul d'orthogonalité ; (2) le développement ; (3) la décomposition, Pythagore, le cas d'égalité ; (4) $\mathbf{p} - \mathbf{p}'$ dans $U$ et dans $U^\perp$ ; (5) le passage de $\mathbf{w}$ à $\mathbf{X}\mathbf{w}$, l'équivalence dans les deux sens, l'écriture matricielle.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12b.18 — Pont : retirer d'une feature ce qu'explique une autre, une projection puis un résidu

**Réponses** : a) `1` · b) `[2, 2, 1, 1]` · c) `[-1, 1, -1, 1]` · d) `0` · e) `0.7143` · f) `1.5` · g) `[0.8, 1.5]`.

**Démarche.**
- a) $\mathbf{x}_2 \cdot \mathbf{x}_1 = 2 + 6 + 0 + 2 = 10$ et $\lVert \mathbf{x}_1 \rVert^2 = 4 + 4 + 1 + 1 = 10$.
- b) $1 \cdot \mathbf{x}_1$. c) $\mathbf{x}_2 - \mathbf{x}_1$. d) $-2 + 2 - 1 + 1 = 0$.
- e) $\frac{10}{14} = \frac{5}{7} \approx 0{,}7143$ : $x_1$ « explique » environ 71 % de $\lVert \mathbf{x}_2 \rVert^2$.
- f) $\mathbf{y} \cdot \mathbf{r} = -3 + 6 - 1 + 4 = 6$ et $\lVert \mathbf{r} \rVert^2 = 4$ : $1{,}5$.
- g) $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 10 & 10 \\ 10 & 14 \end{pmatrix}$, $\mathbf{X}^\top\mathbf{y} = (23, 29)$, $\det = 40$ : $\mathbf{w} = \frac{1}{40}(14 \times 23 - 10 \times 29,\ -10 \times 23 + 10 \times 29) = (0{,}8 ;\ 1{,}5)$.

Pour la copie : f) et g) donnent **le même** poids pour $\mathbf{x}_2$. En effet, $\mathbf{r} = \mathbf{x}_2 - \mathbf{x}_1$ et $\mathbf{x}_2 = \mathbf{x}_1 + \mathbf{r}$ : les deux familles engendrent le même plan. Les prédictions s'écrivent $w_1\mathbf{x}_1 + w_2\mathbf{x}_2 = (w_1 + w_2)\,\mathbf{x}_1 + w_2\,\mathbf{r}$, et, $(\mathbf{x}_1, \mathbf{r})$ étant orthogonale, le coefficient du projeté sur $\mathbf{r}$ se calcule seul : $w_2 = \frac{\mathbf{y} \cdot \mathbf{r}}{\lVert \mathbf{r} \rVert^2} = 1{,}5$ ; celui sur $\mathbf{x}_1$ vaut $\frac{\mathbf{y} \cdot \mathbf{x}_1}{10} = 2{,}3 = w_1 + w_2$, d'où $w_1 = 0{,}8$. Le poids d'une feature dans une régression multiple ne mesure que ce qu'elle apporte **de plus** que les autres : sa partie orthogonale, $\mathbf{r}$ (c'est le théorème de Frisch-Waugh-Lovell). Si $\mathbf{r}$ était presque nul, $w_2 = \frac{\mathbf{y} \cdot \mathbf{r}}{\lVert \mathbf{r} \rVert^2}$ diviserait par un nombre minuscule : un poids énorme et instable, la multicolinéarité.

**Erreurs fréquentes.** Prendre le rapport des normes en e) ($0{,}845$) ; croire que $w_1$ est le poids de $\mathbf{x}_1$ seul (2,3) ; écrire $\mathbf{r} = \mathbf{x}_1 - \mathbf{x}_2$.

**Variante.** Avec $\mathbf{y} = \mathbf{x}_1 + \mathbf{x}_2$ ? *Réponse* : $\mathbf{w} = (1, 1)$, et $\frac{\mathbf{y} \cdot \mathbf{r}}{\lVert \mathbf{r} \rVert^2} = \frac{0 + 4}{4} = 1$.

### Ex M12b.19 — Pont : projeter sur k directions orthonormées, reconstruire, et l'erreur par Pythagore

**Réponses** : a) `True` · b) `[4, 3]` · c) `[3.5, 0.5, 3.5, 0.5]` · d) `[0.5, 1.5, -0.5, -1.5]` · e) `[0, 0]` · f) `5` · g) `[2, -1]` · h) `False`.

**Démarche.**
- a) $\mathbf{u}_1 \cdot \mathbf{u}_2 = \frac{1}{4}(1 - 1 + 1 - 1) = 0$, normes 1.
- b) $\frac{1}{2}(4 + 2 + 3 - 1) = 4$ et $\frac{1}{2}(4 - 2 + 3 + 1) = 3$.
- c) $4\mathbf{u}_1 + 3\mathbf{u}_2 = (2, 2, 2, 2) + (1{,}5 ;\ -1{,}5 ;\ 1{,}5 ;\ -1{,}5)$.
- d) $\mathbf{x} - \hat{\mathbf{x}}$. e) $\frac{1}{2}(0{,}5 + 1{,}5 - 0{,}5 - 1{,}5) = 0$ et $\frac{1}{2}(0{,}5 - 1{,}5 - 0{,}5 + 1{,}5) = 0$.
- f) $0{,}25 + 2{,}25 + 0{,}25 + 2{,}25 = 5$.
- g) $\frac{1}{2}(4 + 2 - 3 + 1) = 2$ et $\frac{1}{2}(4 - 2 - 3 - 1) = -1$.
- h) $\mathbf{U}\mathbf{U}^\top$ est de rang 2.

Pour la copie : $2^2 + (-1)^2 = 5$ = f) ; $\lVert \mathbf{x} \rVert^2 = 16 + 4 + 9 + 1 = 30 = 25 + 5$. Démonstration : $\mathbf{x} = \sum_{i=1}^n z_i\mathbf{u}_i$ avec $z_i = \mathbf{u}_i \cdot \mathbf{x}$ ; $\mathbf{U}\mathbf{U}^\top\mathbf{x} = \sum_{i \le k} z_i\mathbf{u}_i$, donc l'erreur vaut $\sum_{i > k} z_i\mathbf{u}_i$, et Parseval (M12b.14) donne $\lVert \mathbf{e} \rVert^2 = \sum_{i > k} z_i^2$ : l'erreur de reconstruction est faite des coordonnées écartées, et elle est orthogonale aux directions gardées. $\mathbf{U}\mathbf{U}^\top$ est la projection sur $\operatorname{Vect}(\mathbf{u}_1, \mathbf{u}_2)$ : elle laisse $\mathbf{u}_1$ et $\mathbf{u}_2$ inchangés, mais annule $\mathbf{u}_3$ et $\mathbf{u}_4$ ; ce n'est pas l'identité.

**Erreurs fréquentes.** Oublier le facteur $\frac{1}{2}$ ; donner $\lVert \mathbf{e} \rVert$ ($\sqrt{5}$) au lieu de $\lVert \mathbf{e} \rVert^2$ ; croire que $\mathbf{U}^\top\mathbf{U} = \mathbf{I}$ entraîne $\mathbf{U}\mathbf{U}^\top = \mathbf{I}$.

**Variante.** En gardant $k = 3$ directions ($\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$) ? *Réponse* : $\lVert \mathbf{e} \rVert^2 = (-1)^2 = 1$.

### Ex M12b.20 — MML §3.2, §3.5 à §3.7 : produits scalaires, orthogonalité, fonctions, en anglais

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. Une application de $V \times V$ dans $\mathbb{R}$ est bilinéaire si elle est linéaire en chacun de ses deux arguments ; elle est symétrique si l'ordre ne compte pas, définie positive si $\Omega(\mathbf{x}, \mathbf{x}) > 0$ pour tout $\mathbf{x} \ne \mathbf{0}$. Un produit scalaire est une application bilinéaire symétrique définie positive. Un espace muni d'un produit scalaire est un *inner product space* ; muni du produit usuel, un *Euclidean vector space*.
2. Le livre prend $\langle \mathbf{x}, \mathbf{y} \rangle = x_1y_1 - (x_1y_2 + x_2y_1) + 2x_2y_2$, de matrice $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$ : $a = 1 > 0$ et $ac - b^2 = 2 - 1 = 1 > 0$, elle est définie positive.
3. Dans une base, tout produit scalaire s'écrit $\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$ avec les coordonnées et la matrice $A_{ij} = \langle \mathbf{b}_i, \mathbf{b}_j \rangle$, et une telle formule est un produit scalaire si et seulement si $\mathbf{A}$ est symétrique définie positive. Propriétés : le noyau de $\mathbf{A}$ est $\{\mathbf{0}\}$, et ses éléments diagonaux sont positifs. Justification : $a_{ii} = \mathbf{e}_i^\top\mathbf{A}\mathbf{e}_i > 0$ (fiche §1, avec $\mathbf{x} = \mathbf{e}_i$) ; et si $\mathbf{A}\mathbf{x} = \mathbf{0}$ avec $\mathbf{x} \ne \mathbf{0}$, $\mathbf{x}^\top\mathbf{A}\mathbf{x} = 0$, impossible.
4. Une base est orthonormée si ses vecteurs sont deux à deux orthogonaux et de norme 1 (orthogonale si seule la première condition tient). Le livre signale qu'on peut construire une base orthonormée à partir de vecteurs quelconques par le pivot de Gauss sur une matrice augmentée, et que ce procédé constructif est celui de Gram-Schmidt (§3.8.3).
5. Le complément orthogonal d'un plan de $\mathbb{R}^3$ est une droite, engendrée par un vecteur orthogonal au plan, son **vecteur normal** (*normal vector*) ; en général, si $U$ est de dimension $M$ dans un espace de dimension $D$, $U^\perp$ est de dimension $D - M$, et $U \cap U^\perp = \{\mathbf{0}\}$.
6. $\langle u, v \rangle = \int_a^b u(x)\,v(x)\,dx$. Exemple : $\sin$ et $\cos$ sur $[-\pi ; \pi]$ ; leur produit est une fonction impaire, d'intégrale nulle sur un intervalle symétrique. Le livre cite la famille $1, \cos x, \cos 2x, \cos 3x, \ldots$, orthogonale sur $[-\pi ; \pi]$ (le point de départ des séries de Fourier).
7. Par exemple : *positive definite* (défini positif), *inner product space* (espace muni d'un produit scalaire), *normal vector* (vecteur normal), *orthonormal basis* (base orthonormée).

**Grille.** (1) les trois propriétés et les deux noms ; (2) la matrice et le critère appliqué ; (3) le lien matrice-produit scalaire, deux propriétés, une justifiée ; (4) la définition et le lien avec Gram-Schmidt ; (5) le vecteur normal et la dimension ; (6) l'intégrale, l'exemple, la raison (imparité), la famille infinie ; (7) trois mots traduits. Les réponses sont écrites avec tes mots.

### Ex M12b.21 — MML §3.8 et §9.4 : projections, Gram-Schmidt et moindres carrés

**Réponse modèle** (avec tes mots).
1. Une application linéaire $\pi$ d'un espace dans un sous-espace est une projection si $\pi \circ \pi = \pi$ ; sa matrice vérifie $\mathbf{P}^2 = \mathbf{P}$ (idempotente).
2. Trois étapes : trouver la coordonnée $\lambda$ du projeté sur la droite (par la condition d'orthogonalité, $\lambda = \frac{\mathbf{b}^\top\mathbf{x}}{\mathbf{b}^\top\mathbf{b}}$), puis le point $\lambda\mathbf{b}$, puis la matrice $\mathbf{P} = \frac{\mathbf{b}\mathbf{b}^\top}{\mathbf{b}^\top\mathbf{b}}$. C'est la formule de M07, écrite avec une matrice ; la fiche (§5) la retrouve avec $\mathbf{Q} = \mathbf{b}/\lVert \mathbf{b} \rVert$.
3. Avec une base $\mathbf{B}$ du sous-espace, la condition d'orthogonalité donne $\mathbf{B}^\top\mathbf{B}\boldsymbol{\lambda} = \mathbf{B}^\top\mathbf{x}$, l'**équation normale** (*normal equation*), d'où $\boldsymbol{\lambda} = (\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\mathbf{x}$ et $\mathbf{P} = \mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$. Si la base est orthonormée, $\mathbf{B}^\top\mathbf{B} = \mathbf{I}$ : $\boldsymbol{\lambda} = \mathbf{B}^\top\mathbf{x}$ et $\mathbf{P} = \mathbf{B}\mathbf{B}^\top$.
4. Quand $\mathbf{A}\mathbf{x} = \mathbf{b}$ n'a pas de solution, on cherche une solution approchée : le vecteur de l'espace des colonnes le plus proche de $\mathbf{b}$, c'est-à-dire son projeté ; c'est la solution des moindres carrés. L'écart $\lVert \mathbf{x} - \pi_U(\mathbf{x}) \rVert$ est appelé l'erreur de reconstruction (*reconstruction error*).
5. Le livre orthogonalise d'abord, en retirant de $\mathbf{b}_k$ sa projection sur le sous-espace engendré par les vecteurs déjà construits, et ne normalise qu'**à la fin** ; la fiche normalise à chaque étape, ce qui écrit les projections sans division. Le résultat, une fois normé, est le même.
6. On translate : $\pi_L(\mathbf{x}) = \mathbf{x}_0 + \pi_U(\mathbf{x} - \mathbf{x}_0)$. Pour le plan $x + y + z = 3$, $\mathbf{x}_0 = (1, 1, 1)$ et $U$ est le plan $x + y + z = 0$ ; $(3, 3, 3) - \mathbf{x}_0 = (2, 2, 2)$ est normal à $U$, de projeté nul : $\pi_L(3, 3, 3) = (1, 1, 1)$, à la distance $\lVert (2, 2, 2) \rVert = 2\sqrt{3}$.
7. Les prédictions du maximum de vraisemblance, $\mathbf{X}\boldsymbol{\theta}_{\mathrm{ML}} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$, sont la projection orthogonale de $\mathbf{y}$ sur le sous-espace engendré par les colonnes de $\mathbf{X}$ : le point de ce sous-espace le plus proche des observations. La matrice $\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$ est la matrice chapeau de M09b.
8. Par exemple : *idempotent* (idempotent), *normal equation* (équation normale), *reconstruction error* (erreur de reconstruction), *affine subspace* (sous-espace affine).

**Grille.** (1) la définition par $\pi^2 = \pi$ ; (2) les trois étapes et la matrice, comparées ; (3) l'équation normale et le cas orthonormé ; (4) le lien avec les systèmes sans solution et le nom de l'erreur ; (5) la différence de normalisation ; (6) la règle et l'application chiffrée ; (7) le résultat et la matrice chapeau ; (8) trois mots traduits.

### Ex M12b.22 — Fermi : le coût de Gram-Schmidt sur une matrice 100 000 × 50

**Réponse modèle.**
1. $k - 1$ produits scalaires et $k - 1$ mises à jour pour la colonne $k$ (plus une norme et une division) ; en tout, $\frac{n(n-1)}{2} \approx 1\,225$ de chaque, soit environ $\frac{n^2}{2}$.
2. $2 \times \frac{n^2}{2} \times 2m = 2mn^2 = 2 \times 10^5 \times 2\,500 = 5 \times 10^8$ opérations.
3. Environ $0{,}5$ s à $10^9$ opérations par seconde (de 0,1 à quelques secondes en pratique, selon la machine et le code).
4. $10^5 \times 50 \times 8 = 4 \times 10^7$ octets, 40 Mo pour $\mathbf{X}$, autant pour $\mathbf{Q}$.
5. Former $\mathbf{X}^\top\mathbf{X}$ coûte $mn^2 \approx 2{,}5 \times 10^8$ (moitié moins en profitant de la symétrie) : QR coûte environ 2 fois plus, le même ordre de grandeur, pour bien plus de précision. Avec $n = 5\,000$, $2mn^2 = 5 \times 10^{12}$ : plus d'une heure à $10^9$ opérations par seconde, et 4 Go par matrice ; le coût croît comme le **carré** du nombre de features.

**Grille.** (1) le décompte par colonne et le total en $n^2/2$ ; (2) le calcul jusqu'à $5 \times 10^8$ ; (3) le temps ; (4) la mémoire ; (5) la comparaison avec $\mathbf{X}^\top\mathbf{X}$ et l'effet du carré de $n$.

### Ex M12b.23 — Expliquer pourquoi le projeté est le point le plus proche

**Réponse modèle.**

> Imagine un point au-dessus d'un sol plat. Pour l'atteindre au plus court depuis le sol, on se place juste en dessous, là où le fil à plomb touche le sol : c'est la projection orthogonale, le pied de la perpendiculaire. Prends n'importe quel autre point du sol : le point au-dessus, le pied du fil à plomb et cet autre point forment un triangle rectangle, dont l'angle droit est au pied du fil. Le chemin vers l'autre point en est le grand côté, l'hypoténuse, toujours plus long que chacun des deux autres : il est donc plus long que le fil à plomb. Plus on s'éloigne du pied, plus il s'allonge. Même idée quand on remplace une courbe compliquée par un polynôme de petit degré : parmi tous les polynômes permis (le « sol »), on prend le plus proche de la courbe, et ce qui reste est « perpendiculaire » à tous ces polynômes.

**Grille.** (1) la projection comme pied de la perpendiculaire ; (2) le triangle rectangle et son hypoténuse plus longue ; (3) la conclusion « tout autre point est plus loin » ; (4) un exemple de « plus proche dans un ensemble permis » ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M12b.E1 — « Pourquoi résoudre des moindres carrés par QR plutôt que par les équations normales ? »

**Réponse modèle (60 secondes).**

> Les moindres carrés cherchent les poids qui minimisent la somme des carrés des erreurs. Les équations normales forment la matrice $X^\top X$ et résolvent un système carré ; la méthode QR écrit $X = QR$, avec $Q$ à colonnes orthonormées et $R$ triangulaire, puis résout $Rw = Q^\top y$ en remontant. Le problème des équations normales, c'est que former $X^\top X$ revient à mettre le problème « au carré » : quand des features sont presque dépendantes, des erreurs d'arrondi de l'ordre de $10^{-16}$ deviennent énormes sur les poids, et l'on perd deux fois plus de chiffres que le problème ne l'impose. QR n'élève rien au carré : multiplier par $Q$ conserve les longueurs, donc n'amplifie pas les erreurs. En pratique, les bibliothèques comme LAPACK, derrière NumPy, calculent QR par des réflexions de Householder, encore plus stables que Gram-Schmidt, ou passent par la SVD, comme `lstsq`. Les équations normales restent acceptables, et plus rapides, quand les features sont peu corrélées et bien mises à l'échelle.

**Grille.** (1) les deux méthodes en une phrase chacune ; (2) l'effet de $\mathbf{X}^\top\mathbf{X}$ sur les arrondis quand les features sont presque dépendantes ; (3) pourquoi QR l'évite (normes conservées, système triangulaire) ; (4) Householder, LAPACK ou la SVD ; (5) le cas où les équations normales suffisent.

### M12b.E2 — « Qu'est-ce qu'une matrice orthogonale, et pourquoi est-elle agréable en calcul numérique ? »

**Réponse modèle (60 secondes).**

> Une matrice carrée est orthogonale quand ses colonnes forment une base orthonormée : des vecteurs de longueur 1, deux à deux perpendiculaires. Autrement dit, $Q^\top Q = I$ : son inverse est sa transposée, on l'inverse sans rien calculer. Géométriquement, c'est une rotation ou une symétrie : elle conserve les longueurs, les angles, les distances et les produits scalaires. En calcul numérique, c'est précieux : multiplier par $Q$ ne grossit pas les erreurs d'arrondi, puisque les normes sont conservées ; c'est pour cela que les algorithmes stables, QR, la SVD, la diagonalisation des matrices symétriques, sont construits avec des matrices orthogonales. En machine learning, on en rencontre dans l'ACP, qui fait tourner les données vers de nouveaux axes orthonormés, dans l'initialisation orthogonale de certains réseaux, et dans tout changement de base qui ne doit pas déformer les distances, par exemple pour un kNN. Attention : des colonnes seulement orthogonales, pas unitaires, ne suffisent pas.

**Grille.** (1) la définition, avec des colonnes orthonormées ; (2) ce qu'elle conserve, et l'inverse égale à la transposée ; (3) deux exemples géométriques ; (4) la raison numérique ; (5) un usage en machine learning ; (6) le piège « orthogonales mais pas unitaires ».

<a id="notebook"></a>

## Notebook

### Ex M12b.24 — Gram-Schmidt, classique et modifié · `gram_schmidt`

**Réponses** : a) `[[0.545455, 0.818182], [0.545455, -0.181818], [0.636364, -0.545455]]` · b) `True` · c) `True` · d) `[[-1.0, 0.0], [0.0, -1.0]]` · e) `"ValueError"` · f) `"ValueError"` · g) `True`.

**Démarche.** `A = np.array(A, dtype=float)` (une copie), une `ValueError` si `A.ndim != 2`, `Q = np.zeros_like(A)`. Pour chaque colonne `k` : `a = A[:, k]`, `v = a.copy()`, puis pour `j < k` : `coefficient = Q[:, j] @ (v if modified else a)` et `v -= coefficient * Q[:, j]` ; si `norm(v) <= tol * norm(a)` ou `norm(v) == 0`, une `ValueError` ; sinon `Q[:, k] = v / norm(v)`. Pour la copie : $\mathbf{Q} = \frac{1}{11}\begin{pmatrix} 6 & 9 \\ 6 & -2 \\ 7 & -6 \end{pmatrix}$ ; en d), $\mathbf{q}_k$ a le sens de $\mathbf{a}_k$, donc des $-1$ ; en e), la deuxième colonne est le double de la première et $\mathbf{v}_2 = \mathbf{0}$, aux arrondis près.

**Erreurs fréquentes.** Utiliser `a` (la colonne d'origine) dans les deux procédés, ce qui rend le modifié classique ; modifier `A` sur place (`np.asarray` ne copie pas un tableau de flottants) ; comparer la norme de `v` à `tol` en absolu (une colonne petite mais libre serait refusée) ; prendre la valeur absolue pour « fixer » le signe.

### Ex M12b.25 — La projection orthogonale sur un sous-espace · `project`

**Réponses** : a) `[0.4, 1.2, 2.8, 3.6]` · b) `[1.3, 3.9]` · c) `True` · d) `True` · e) `True` · f) `"ValueError"` · g) `"ValueError"`.

**Démarche.** Convertir en flottants, vérifier `v.ndim == 1`, `A.ndim == 2` et `A.shape[0] == v.shape[0]` (sinon `ValueError`), puis `Q = gram_schmidt(A)` et rendre `Q @ (Q.T @ v)`. Pour la copie : a) donne les prédictions de la droite $0{,}4 + 0{,}8\,x$ ajustée aux points $(0, 1), (1, 0), (3, 4), (4, 3)$ ; b) $\frac{13}{10}(1, 3)$ ; e) la projection ne dépend que du sous-espace, et $\mathbf{A}\mathbf{M}$ a les mêmes colonnes engendrées.

**Erreurs fréquentes.** `A @ (A.T @ v)` sans orthonormaliser ; attraper la `ValueError` de `gram_schmidt` pour rendre autre chose ; oublier le test des formes ($\mathbf{v}$ de longueur 2 et $\mathbf{A}$ à 3 lignes).

### Ex M12b.26 — La décomposition QR et les moindres carrés par QR · `qr, least_squares_qr`

**Réponses** : a) `[[13.0, 6.0], [0.0, 2.0]]` · b) `True` · c) `True` · d) `[1.3, 1.1]` · e) `True` · f) `"ValueError"` · g) `"ValueError"`.

**Démarche.** `qr` : `Q = gram_schmidt(A)`, `R = np.triu(Q.T @ A)`, rendre `(Q, R)`. `least_squares_qr` : formes, `Q, R = qr(X)`, `z = Q.T @ y`, puis pour `i` de `p - 1` à `0` : `w[i] = (z[i] - R[i, i + 1:] @ w[i + 1:]) / R[i, i]`. Pour la copie : a) $\mathbf{Q} = \frac{1}{13}\begin{pmatrix} 12 & 3 \\ 3 & 4 \\ 4 & -12 \end{pmatrix}$ ; d) $\mathbf{R} = \begin{pmatrix} 2 & 4 \\ 0 & \sqrt{10} \end{pmatrix}$ et $\mathbf{Q}^\top\mathbf{y} = (7, 11/\sqrt{10})$, d'où $w_1 = 1{,}1$ puis $w_0 = \frac{7 - 4 \times 1{,}1}{2} = 1{,}3$ ; c) $\mathbf{Q}^\top\mathbf{A}$ n'a, sous sa diagonale, que des arrondis de l'ordre de $10^{-16}$ : `np.triu` les met exactement à 0.

**Erreurs fréquentes.** Remonter depuis la première ligne ; résoudre avec `np.linalg.solve(R, z)` (la docstring le permet, mais l'exercice fait écrire la boucle) ; oublier `np.triu`.

### Ex M12b.27 — `np.linalg.qr` et `lstsq` contre ta projection et ta QR : les signes de Q et de R

**Réponses** : a) `[[5, 3], [3, 3]]` · b) `[5, 5]` · c) `True` · d) `True` · e) `3` · f) `True` · g) `3` · h) `"ValueError"`.

**Démarche.** `Q_np, R_np = np.linalg.qr(A)`, `np.linalg.qr(A, mode="complete")[0].shape`, `np.allclose(np.abs(R_np), np.abs(R_me))`, `D = np.diag(np.sign(np.diag(R_np)))` puis les deux comparaisons, `np.linalg.lstsq(A, y, rcond=None)[2]` pour le rang. Pour la copie : NumPy (Householder) rend ici une diagonale de $\mathbf{R}$ négative ; changer le signe de la colonne $k$ de $\mathbf{Q}$ et de la ligne $k$ de $\mathbf{R}$ ne change pas le produit, et la décomposition à diagonale positive est unique : d'où c) et d). Avec $\mathbf{A}_4$, une infinité de poids donnent les mêmes prédictions (M12a §6) : `lstsq` rend celui de plus petite norme (M12d), tandis que `least_squares_qr` refuse.

**Erreurs fréquentes.** Comparer $\mathbf{Q}$ et $\mathbf{R}$ sans tenir compte des signes ; lire le deuxième objet de `lstsq` comme les résidus eux-mêmes (c'est leur somme de carrés) ; oublier `rcond=None` (un avertissement de NumPy).

### Ex M12b.28 — Prédire : Gram-Schmidt classique sur des vecteurs presque colinéaires, QᵀQ vaut-il encore I ?

**Réponses** : a) `3` · b) `2` · c) `1` · d) `1`.

a) L'écart vaut environ 1 : $\mathbf{q}_2 \cdot \mathbf{q}_3 \approx -0{,}9995$, les deux dernières colonnes de $\mathbf{Q}$ pointent presque dans la même direction. Les $\mathbf{v}_k$ sont de l'ordre de $10^{-9}$, faits de différences de nombres presque égaux, et leurs erreurs d'arrondi, de l'ordre de $10^{-16}$, sont énormes à cette échelle ; le classique calcule les coefficients de $\mathbf{a}_3$ avec un $\mathbf{q}_2$ déjà faux et n'efface pas cette erreur. b) Le modifié retire la projection sur $\mathbf{q}_2$ du vecteur courant, ce qui corrige en passant l'erreur de la première étape : environ $10^{-7}$. c) $10^{-16}$ sur des colonnes bien séparées. d) Chaque colonne est normée : les normes valent 1, c'est l'orthogonalité qui se perd.

### Ex M12b.29 — Gram-Schmidt classique contre modifié : l'orthogonalité perdue quand les colonnes sont presque dépendantes

**Réponses** : a) `9` · b) `True` · c) `True` · d) `True`.

**Démarche.** `loss_table` : pour chaque `d`, `A = polynomial_features(d)`, puis `orthogonality_loss` de `gram_schmidt(A, modified=False)`, de `gram_schmidt(A)` et de `gram_schmidt(gram_schmidt(A, modified=False), modified=False)`. Pour la copie : l'écart du classique est multiplié par environ 100 à chaque degré, celui du modifié par environ 10 : le classique perd l'orthogonalité comme le carré de la « presque dépendance », le modifié seulement comme elle. Orthogonaliser une seconde fois des colonnes déjà presque orthogonales ne retire que de petites projections, calculées avec précision : l'écart retombe vers $10^{-15}$. Pour une régression polynomiale de degré 10 : ni les monômes ni les équations normales, mais une base de polynômes orthogonaux, ou QR.

**Erreurs fréquentes.** Lire le dernier degré sous le seuil au lieu du premier au-dessus ; appliquer deux fois le procédé à la matrice d'origine (`gram_schmidt(A)` deux fois sur `A`) au lieu de l'appliquer à son résultat.

### Ex M12b.30 — Projeter un nuage de ℝ³ sur un plan : les résidus orthogonaux en image

**Démarche.** `P = np.array([mymath.orthogonal.project(x, A) for x in X])`, deux `ax.scatter`, puis, pour chaque couple, `ax.plot([x[0], p[0]], [x[1], p[1]], [x[2], p[2]])` ; le plan, en option, par `ax.plot_surface` sur la grille $s\,\mathbf{a}_1 + t\,\mathbf{a}_2$. Pour la copie : tous les segments sont parallèles à la normale $(1, -1, 1)$ du plan engendré par $(1, 1, 0)$ et $(0, 1, 1)$ ; la perspective en cache l'angle droit sous certains points de vue. Le point le plus loin du plan maximise $\frac{|\mathbf{x} \cdot \mathbf{n}|}{\lVert \mathbf{n} \rVert}$ (M07). Une autre base du même plan donne exactement la même figure.

**Erreurs fréquentes.** Projeter tout le nuage d'un coup avec `project(X, A)` (la fonction attend un vecteur) ; tracer les segments avec un seul `ax.plot` qui relie tous les points ; ouvrir une figure dans la fonction.

### Ex M12b.31 — Chasse à l'erreur : une normalisation oubliée, QQᵀ sur une base non orthonormée, R w = Qᵀy résolu dans le mauvais sens

**Réponses** : a) `"ABD"` · b) `[1, 0.8889, 0.3333, 1.6667, 0, 3]`.

(A) $\mathbf{v}_2 = (0, 3, 3) - 3 \cdot \frac{1}{3}(2, 1, 2) = (-2, 2, 1)$, de norme 3 : il manque la division par la norme ; un vecteur d'une base orthonormée a pour norme 1. (B) $\mathbf{A}\mathbf{A}^\top$ n'est pas une projection : il faut $\mathbf{Q}\mathbf{Q}^\top$, dont le coin vaut $\frac{4}{9} + \frac{4}{9} = \frac{8}{9}$ (le code donne 4). (C) Juste : le résidu de $(3, 0, 0)$ est sa composante sur la normale $\frac{1}{3}(1, 2, -2)$, soit $\frac{1}{3}(1, 2, -2)$. (D) La boucle descend et ignore $r_{12}$ : elle rend $w_0 = \frac{7}{3}$ ; en remontant, $w_1 = \frac{2}{3}$, puis $w_0 = \frac{7 - 3 \times 2/3}{3} = \frac{5}{3}$. C'est la plus dangereuse : elle s'exécute et rend des poids plausibles. (E) Juste : 0 aux arrondis près. (F) Juste : $\mathbf{a}_2 = 3\mathbf{q}_1 + 3\mathbf{q}_2$.

### Ex M12b.32 — Un test de propriétés pour la projection : idempotente, symétrique, résidu orthogonal

**Démarche.** Voir `05_solutions.ipynb` : trois `assert`, chacun avec un message qui dit ce qui était attendu. La projection oblique est idempotente : (1) la laisse passer, (2) et (3) l'attrapent. $\mathbf{A}\mathbf{A}^\top\mathbf{v}$ est symétrique : (2) la laisse passer, (1) et (3) l'attrapent. Pour $k = m$, $\operatorname{Im}\mathbf{A} = \mathbb{R}^m$ et toute projection sur $\mathbb{R}^m$ est l'identité : la copie oblique serait juste, et le test ne pourrait pas la distinguer. Une fonction qui passe (1) et (2) est une projection orthogonale ; (3) vérifie en plus qu'elle projette sur le bon sous-espace (avec $\mathbf{p} \in \operatorname{Im}\mathbf{A}$, les trois propriétés caractérisent la bonne réponse).

**Erreurs fréquentes.** Comparer des flottants avec `==` ; tirer $k = m$ ; tester la symétrie avec un seul vecteur ($\mathbf{P}\mathbf{v} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{P}\mathbf{v}$ est toujours vrai).

### Ex M12b.33 — Défi : des colonnes presque dépendantes, des moindres carrés à 1e−8 près de `lstsq` par l'orthogonalisation de [X | y]

**Réponse** : `True`.

**Démarche.** `V = np.column_stack([X, y])` (une copie), puis Gram-Schmidt modifié en gardant `R[j, k] = V[:, j] @ V[:, k]` au moment où l'on retire chaque projection, `R[k, k] = norm(V[:, k])` ; enfin la remontée sur `R[:p, :p]` avec le second membre `R[:p, p]`. Les écarts à `lstsq` tombent vers $10^{-11}$, contre $10^{-5}$ à $10^{-3}$ pour les équations normales et `least_squares_qr`. Pour la copie : le $\mathbf{Q}$ du procédé modifié a perdu un peu d'orthogonalité ; recalculer $\mathbf{R} = \mathbf{Q}^\top\mathbf{X}$ mélange cet écart au petit élément $r_{66} \approx 10^{-5}$ qui mesure la presque dépendance, alors que les coefficients gardés pendant le procédé vérifient $\mathbf{X} = \mathbf{Q}\mathbf{R}$ aux arrondis près, et que $\mathbf{y}$, traité comme une colonne de plus, reçoit un second membre cohérent avec eux (Björck, 1967). $r_{p+1,p+1}$ est la norme du résidu, $\lVert \mathbf{y} - \mathbf{X}\mathbf{w}^* \rVert$. Autre voie : orthogonaliser deux fois (M12b.29), puis $\mathbf{Q}^\top\mathbf{X}$ et $\mathbf{Q}^\top\mathbf{y}$.

**Erreurs fréquentes.** Garder les coefficients mais recalculer le second membre par $\mathbf{Q}^\top\mathbf{y}$ (l'écart reste de l'ordre de $10^{-4}$) ; centrer ou standardiser les colonnes (on ne résout plus le même problème) ; appeler `lstsq` (interdit, et la cellule du défi compare à elle).
