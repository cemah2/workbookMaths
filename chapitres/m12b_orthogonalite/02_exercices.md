# M12b · Orthogonalité et projections — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m12b_orthogonalite/06_mes_reponses.md` (créée par `python tools/start_chapter.py M12b`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, une famille de vecteurs se range dans les **colonnes** d'une matrice ; sans autre précision, le produit scalaire est le produit usuel $\mathbf{x} \cdot \mathbf{y}$, et Gram-Schmidt traite les vecteurs dans l'ordre donné, avec $\langle \mathbf{a}_k, \mathbf{q}_k \rangle > 0$ (fiche §3).

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M12b.Q1 — Produit scalaire ou pas ? Symétrie et positivité 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Sur $\mathbb{R}^2$, lesquelles de ces formules définissent un produit scalaire ? Réponds par oui ou non, et justifie chaque non par la propriété qui manque et un exemple.
1. $\langle \mathbf{x}, \mathbf{y} \rangle = 2x_1y_1 + 5x_2y_2$.
2. $\langle \mathbf{x}, \mathbf{y} \rangle = x_1y_2 + x_2y_1$.
3. $\langle \mathbf{x}, \mathbf{y} \rangle = x_1y_1 + x_1y_2 + x_2y_1 + 3x_2y_2$.
4. $\langle \mathbf{x}, \mathbf{y} \rangle = x_1y_1 + 2x_1y_2 + x_2y_2$.
5. $\langle \mathbf{x}, \mathbf{y} \rangle = (x_1 + x_2)(y_1 + y_2)$.
6. $\langle \mathbf{x}, \mathbf{y} \rangle = |x_1y_1| + |x_2y_2|$.

### M12b.Q2 — Orthogonale, orthonormée, matrice orthogonale 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. $(2, -5)$ et $(5, 2)$ sont-ils orthogonaux ? orthonormés ?
2. Les colonnes de $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ forment-elles une base orthonormée de $\mathbb{R}^2$ ?
3. $\begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix}$ est-elle orthogonale ?
4. Si $\mathbf{Q}$ est orthogonale, que vaut $\mathbf{Q}^{-1}$ ?
5. Vrai ou faux : une matrice orthogonale conserve les distances entre points.
6. $\mathbf{Q}$ a la forme $(3, 2)$ et des colonnes orthonormées. Que vaut $\mathbf{Q}^\top\mathbf{Q}$ ? A-t-on $\mathbf{Q}\mathbf{Q}^\top = \mathbf{I}_3$ ?

### M12b.Q3 — Gram-Schmidt : ce que chaque étape retire 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. À l'étape $k$, que retire-t-on de $\mathbf{a}_k$ ?
2. Pourquoi divise-t-on $\mathbf{v}_k$ par sa norme ?
3. Que se passe-t-il si $\mathbf{a}_k$ est une combinaison de $\mathbf{a}_1, \ldots, \mathbf{a}_{k-1}$ ?
4. Le résultat de Gram-Schmidt sur $\big((3, 0), (1, 2)\big)$ ?
5. Vrai ou faux : changer l'ordre des vecteurs ne change pas la base orthonormée obtenue.
6. Vrai ou faux : $\operatorname{Vect}(\mathbf{q}_1, \mathbf{q}_2) = \operatorname{Vect}(\mathbf{a}_1, \mathbf{a}_2)$.

### M12b.Q4 — Le complément orthogonal : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Le complément orthogonal d'un plan de $\mathbb{R}^3$ est une droite.
2. $\{\mathbf{0}\}^\perp = \mathbb{R}^n$ et $(\mathbb{R}^n)^\perp = \{\mathbf{0}\}$.
3. $U^\perp$ contient tous les vecteurs qui ne sont pas dans $U$.
4. $(\operatorname{Im}\mathbf{A})^\perp = \ker\mathbf{A}$.
5. Si $U$ est un sous-espace de dimension 3 de $\mathbb{R}^5$, alors $\dim U^\perp = 2$.
6. $(U^\perp)^\perp = U$.

### M12b.Q5 — Une matrice de projection : sur quoi, et quelles propriétés ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

$\mathbf{P} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.
1. Sur quel sous-espace $\mathbf{P}$ projette-t-elle ?
2. Que valent $\mathbf{P}^2$ et $\mathbf{P}^\top$ ?
3. Sa trace et son rang ?
4. Sur quoi projette $\frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ ?
5. Vrai ou faux : une matrice de projection orthogonale autre que $\mathbf{I}$ est inversible.
6. Vrai ou faux : si $\mathbf{P}$ est une projection orthogonale, $\mathbf{I} - \mathbf{P}$ en est une aussi.

### M12b.Q6 — Moindres carrés et projection 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w}^*$ est le projeté de quel vecteur, sur quel sous-espace ?
2. Le résidu $\mathbf{y} - \hat{\mathbf{y}}$ est orthogonal à quoi ?
3. Le modèle a une colonne de 1. Que vaut la somme des résidus ?
4. Si $\mathbf{y} \in \operatorname{Im}\mathbf{X}$, que vaut le résidu ?
5. Vrai ou faux : ajouter une colonne à $\mathbf{X}$ ne peut pas augmenter $\lVert \mathbf{y} - \hat{\mathbf{y}} \rVert$.
6. Vrai ou faux : dans le plan $(x, y)$ des données, les résidus sont perpendiculaires à la droite ajustée.

### M12b.Q7 — QR : formes et propriétés 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

$\mathbf{A}$ a la forme $(5, 3)$ et des colonnes libres ; $\mathbf{A} = \mathbf{Q}\mathbf{R}$ est sa décomposition QR réduite.
1. Les formes de $\mathbf{Q}$ et de $\mathbf{R}$ ?
2. $\mathbf{Q}^\top\mathbf{Q}$ ?
3. Quelle forme particulière a $\mathbf{R}$, et quel signe ont ses éléments diagonaux ?
4. À quel système se ramènent les moindres carrés $\min \lVert \mathbf{y} - \mathbf{A}\mathbf{w} \rVert$ ?
5. Vrai ou faux : `np.linalg.qr` rend toujours une diagonale de $\mathbf{R}$ positive.
6. Vrai ou faux : $\mathbf{Q}\mathbf{Q}^\top = \mathbf{I}_5$.

### M12b.Q8 — Des fonctions orthogonales 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

Avec $\langle f, g \rangle = \int_{-1}^{1} f(x)\,g(x)\,dx$ :
1. $1$ et $x$ sont-elles orthogonales ?
2. $x$ et $x^3$ ?
3. Une fonction paire et une fonction impaire ?
4. $\lVert 1 \rVert$ ?
5. Et avec $\langle f, g \rangle = \int_0^1 f(x)\,g(x)\,dx$, $1$ et $x$ sont-elles orthogonales ?
6. Pourquoi $\int_{-1}^1 f^2 > 0$ pour une fonction continue $f$ non nulle ?

<a id="rappels"></a>

## 🔁 Rappels

### M12b.R1 — La projection sur une droite (M07) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

$\mathbf{u} = (1, 1, 2)$ et $\mathbf{x} = (1, 3, 4)$.
1. $\mathbf{x} \cdot \mathbf{u}$ ?
2. $\lVert \mathbf{u} \rVert^2$ ?
3. Le projeté $\mathbf{p}$ de $\mathbf{x}$ sur la droite $\operatorname{Vect}(\mathbf{u})$ ?
4. $\mathbf{x} - \mathbf{p}$, et vérifie qu'il est orthogonal à $\mathbf{u}$.
5. La distance de $\mathbf{x}$ à la droite ?
6. Le projeté de $3\mathbf{x}$ sur la même droite ?

### M12b.R2 — Les équations normales et la matrice chapeau (M09b) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

Trois points d'abscisses $-2$, $0$, $2$ ; une droite avec biais, donc $\mathbf{X} = \begin{pmatrix} 1 & -2 \\ 1 & 0 \\ 1 & 2 \end{pmatrix}$, et $\mathbf{y} = (1, 4, 4)$.
1. $\mathbf{X}^\top\mathbf{X}$ ?
2. $\mathbf{X}^\top\mathbf{y}$ ?
3. Les poids $\mathbf{w}^*$ ?
4. Les prédictions $\hat{\mathbf{y}}$ et le résidu ?
5. La trace de la matrice chapeau $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$ ?
6. Que valent $\mathbf{H}^2$ et $\mathbf{H}^\top$ ?

### M12b.R3 — Base, rang et noyau (M12a) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 1 \end{pmatrix}$.
1. $\operatorname{rg}(\mathbf{A})$ ?
2. $\dim\ker\mathbf{A}$ ?
3. Une base de $\ker\mathbf{A}$ (avec la convention de M12a : une colonne libre à 1, les autres à 0) ?
4. Une base de $\operatorname{Im}\mathbf{A}$ ?
5. $\operatorname{Im}\mathbf{A} = \mathbb{R}^2$ ?
6. Les vecteurs de $\ker\mathbf{A}$ sont orthogonaux à certains vecteurs liés à $\mathbf{A}$ : lesquels ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets pour un vecteur, comme `[0, -2, 5]` ; une matrice comme une liste de lignes, `[[1, 0], [-2, 3]]` ; vrai ou faux par `True` ou `False`.

### Ex M12b.1 — Un produit scalaire défini par une matrice 2 × 2 : normes, angles, orthogonalité ✏️ ★ ⏱️ 15 min
**Objectif :** vérifier qu'une matrice symétrique définit un produit scalaire, et y calculer normes, angles et orthogonalité.
**Prérequis :** fiche §1 ; M07 §3 et §4 · **Parcours :** C, E

Sur $\mathbb{R}^2$, on pose $\langle \mathbf{x}, \mathbf{y} \rangle_{\mathbf{M}} = \mathbf{x}^\top\mathbf{M}\mathbf{y}$, avec $\mathbf{M} = \begin{pmatrix} 3 & 1 \\ 1 & 1 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | vrai ou faux : $\langle \cdot, \cdot \rangle_{\mathbf{M}}$ est un produit scalaire | `True` ou `False` |
| b | $\langle \mathbf{e}_1, \mathbf{e}_2 \rangle_{\mathbf{M}}$ | un nombre |
| c | $\lVert \mathbf{e}_1 \rVert_{\mathbf{M}}$ | un nombre (3 décimales) |
| d | le cosinus de l'angle entre $\mathbf{e}_1$ et $\mathbf{e}_2$ pour $\langle \cdot, \cdot \rangle_{\mathbf{M}}$ | un nombre (3 décimales) |
| e | $\lVert (2, -1) \rVert_{\mathbf{M}}$ | un nombre |
| f | vrai ou faux : $(1, -1)$ et $\mathbf{e}_2$ sont orthogonaux pour $\langle \cdot, \cdot \rangle_{\mathbf{M}}$ | `True` ou `False` |
| g | le nombre $k$ tel que $(1, k)$ soit orthogonal à $(1, 1)$ pour $\langle \cdot, \cdot \rangle_{\mathbf{M}}$ | un nombre |
| h | vrai ou faux : $\mathbf{N} = \begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ définit aussi un produit scalaire | `True` ou `False` |

Dans ta copie : écris $\mathbf{x}^\top\mathbf{M}\mathbf{x}$ comme une somme de deux carrés. Compare f) avec le produit scalaire usuel de ces deux vecteurs. Avec f), écris une base orthonormée pour $\langle \cdot, \cdot \rangle_{\mathbf{M}}$ qui contient $\mathbf{e}_2$. Pour h), donne un vecteur précis qui empêche $\mathbf{N}$ de convenir.

### Ex M12b.2 — Les coordonnées dans une base orthonormée : des produits scalaires au lieu d'un système ✏️ ★ ⏱️ 15 min
**Objectif :** vérifier qu'une base est orthonormée, y lire des coordonnées par des produits scalaires, et revenir aux coordonnées canoniques.
**Prérequis :** fiche §2 ; M12a §3 · **Parcours :** C, E

Dans $\mathbb{R}^4$ : $\mathbf{u}_1 = \frac{1}{5}(1, 2, 2, 4)$, $\mathbf{u}_2 = \frac{1}{5}(2, -1, -4, 2)$, $\mathbf{u}_3 = \frac{1}{5}(2, 4, -1, -2)$, $\mathbf{u}_4 = \frac{1}{5}(4, -2, 2, -1)$, et $\mathbf{x} = (1, 2, 3, 1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{u}_1 \cdot \mathbf{u}_2$ | un nombre |
| b | $\lVert \mathbf{u}_3 \rVert$ | un nombre |
| c | les coordonnées de $\mathbf{x}$ dans la base $(\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4)$ | une liste de 4 nombres |
| d | $\lVert \mathbf{x} \rVert^2$, calculé avec les seules coordonnées de c) | un nombre |
| e | le vecteur dont les coordonnées dans cette base sont $(1, 0, -1, 2)$ | une liste de 4 nombres (1 décimale) |
| f | les coordonnées de $\mathbf{x}$ dans la base **orthogonale** $(\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, 2\mathbf{u}_4)$ | une liste de 4 nombres (1 décimale) |

Dans ta copie : vérifie au moins deux autres paires orthogonales et une autre norme. Vérifie c) en recombinant les vecteurs de base. Compare f) et c) : quelles coordonnées changent, et dans quel rapport ? Combien d'opérations aurait demandées la résolution d'un système $4 \times 4$ pour c) ?

### Ex M12b.3 — Une matrice orthogonale 3 × 3 conserve normes et angles ✏️ ★ ⏱️ 15 min
**Objectif :** reconnaître une matrice orthogonale, vérifier qu'elle conserve normes et produits scalaires, et l'inverser en la transposant.
**Prérequis :** fiche §2 · **Parcours :** C, E

$$\mathbf{Q} = \frac{1}{7}\begin{pmatrix} 2 & 6 & 3 \\ 3 & 2 & -6 \\ 6 & -3 & 2 \end{pmatrix}, \qquad \mathbf{x} = (1, 0, 1), \qquad \mathbf{y} = (0, 1, -1).$$

| | Question | Réponse attendue |
|---|---|---|
| a | vrai ou faux : $\mathbf{Q}$ est orthogonale | `True` ou `False` |
| b | $\mathbf{Q}\mathbf{x}$ | une liste de 3 nombres (4 décimales) |
| c | $\lVert \mathbf{Q}\mathbf{x} \rVert$ | un nombre (4 décimales) |
| d | $(\mathbf{Q}\mathbf{x}) \cdot (\mathbf{Q}\mathbf{y})$ | un nombre |
| e | la solution $\mathbf{z}$ de $\mathbf{Q}\mathbf{z} = (7, 0, 0)$ | une liste de 3 nombres |
| f | vrai ou faux : $2\mathbf{Q}$ est orthogonale | `True` ou `False` |
| g | vrai ou faux : $\mathbf{Q}\mathbf{P}$ est orthogonale, avec $\mathbf{P} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ | `True` ou `False` |

Dans ta copie : compare c) avec $\lVert \mathbf{x} \rVert$ et d) avec $\mathbf{x} \cdot \mathbf{y}$ ; calcule l'angle entre $\mathbf{x}$ et $\mathbf{y}$, puis entre $\mathbf{Q}\mathbf{x}$ et $\mathbf{Q}\mathbf{y}$. Pourquoi e) ne demande-t-il aucun pivot de Gauss ? $\mathbf{Q}$ est-elle symétrique, et cela changerait-il e) ?

### Ex M12b.4 — Gram-Schmidt sur trois vecteurs de ℝ³ ✏️ ★★ ⏱️ 20 min
**Objectif :** orthonormaliser trois vecteurs pas à pas, en contrôlant chaque étape.
**Prérequis :** fiche §3 · **Parcours :** C, E

$\mathbf{a}_1 = (4, 1, 8)$, $\mathbf{a}_2 = (1, 1, -4)$, $\mathbf{a}_3 = (-1, 3, -1)$. On note $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$ la famille orthonormée obtenue par Gram-Schmidt, dans cet ordre.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert \mathbf{a}_1 \rVert$ | un nombre |
| b | $\mathbf{a}_2 \cdot \mathbf{q}_1$ | un nombre |
| c | $\mathbf{v}_2 = \mathbf{a}_2 - (\mathbf{a}_2 \cdot \mathbf{q}_1)\,\mathbf{q}_1$ | une liste de 3 nombres (4 décimales) |
| d | $\lVert \mathbf{v}_2 \rVert$ | un nombre |
| e | $\mathbf{q}_2$ | une liste de 3 nombres (4 décimales) |
| f | les produits scalaires $(\mathbf{a}_3 \cdot \mathbf{q}_1,\ \mathbf{a}_3 \cdot \mathbf{q}_2)$ | une liste de 2 nombres |
| g | $\mathbf{q}_3$ | une liste de 3 nombres (4 décimales) |
| h | vrai ou faux : $\operatorname{Vect}(\mathbf{q}_1, \mathbf{q}_2) = \operatorname{Vect}(\mathbf{a}_1, \mathbf{a}_2)$ | `True` ou `False` |

Dans ta copie : garde les vecteurs sous forme de fractions jusqu'au bout. Vérifie les trois orthogonalités et les trois normes. Écris $\mathbf{a}_2$ et $\mathbf{a}_3$ comme combinaisons de $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$, en lisant les coefficients dans tes calculs. Refais l'étape 3 avec le procédé modifié : obtiens-tu le même $\mathbf{v}_3$ ?

### Ex M12b.5 — Gram-Schmidt pour un produit scalaire qui n'est pas l'usuel ✏️ ★★ ⏱️ 20 min
**Objectif :** appliquer Gram-Schmidt et la projection avec un produit scalaire pondéré, et voir que l'orthogonalité change avec le produit scalaire.
**Prérequis :** fiche §1, §3 et §5 · **Parcours :** C

Sur $\mathbb{R}^3$, on pondère la deuxième coordonnée par 2 (comme un exemple compté deux fois) : $\langle \mathbf{x}, \mathbf{y} \rangle_{\mathbf{D}} = x_1y_1 + 2x_2y_2 + x_3y_3 = \mathbf{x}^\top\mathbf{D}\mathbf{y}$, avec $\mathbf{D} = \operatorname{diag}(1, 2, 1)$. On orthonormalise $\mathbf{a}_1 = (1, 1, -1)$ puis $\mathbf{a}_2 = (2, -1, 2)$ pour ce produit scalaire, et l'on projette $\mathbf{x} = (4, -2, -2)$ sur $U = \operatorname{Vect}(\mathbf{a}_1, \mathbf{a}_2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\langle \mathbf{a}_1, \mathbf{a}_2 \rangle_{\mathbf{D}}$ | un nombre |
| b | $\lVert \mathbf{a}_1 \rVert_{\mathbf{D}}$ | un nombre |
| c | $\mathbf{q}_1$ | une liste de 3 nombres (1 décimale) |
| d | $\mathbf{v}_2 = \mathbf{a}_2 - \langle \mathbf{a}_2, \mathbf{q}_1 \rangle_{\mathbf{D}}\,\mathbf{q}_1$ | une liste de 3 nombres (1 décimale) |
| e | $\lVert \mathbf{v}_2 \rVert_{\mathbf{D}}$ | un nombre |
| f | $\mathbf{q}_2$ | une liste de 3 nombres (4 décimales) |
| g | les coordonnées $\big(\langle \mathbf{x}, \mathbf{q}_1 \rangle_{\mathbf{D}},\ \langle \mathbf{x}, \mathbf{q}_2 \rangle_{\mathbf{D}}\big)$ | une liste de 2 nombres |
| h | le projeté de $\mathbf{x}$ sur $U$ pour $\langle \cdot, \cdot \rangle_{\mathbf{D}}$ | une liste de 3 nombres |

Dans ta copie : vérifie $\langle \mathbf{q}_1, \mathbf{q}_2 \rangle_{\mathbf{D}} = 0$ et $\lVert \mathbf{q}_2 \rVert_{\mathbf{D}} = 1$, puis calcule $\mathbf{q}_1 \cdot \mathbf{q}_2$ pour le produit usuel. Vérifie que $\mathbf{x}$ moins h) est orthogonal à $\mathbf{a}_1$ et à $\mathbf{a}_2$ pour $\langle \cdot, \cdot \rangle_{\mathbf{D}}$ ; l'est-il pour le produit usuel ?

### Ex M12b.6 — Une base du complément orthogonal d'un plan de ℝ⁴ ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un complément orthogonal comme un noyau, et s'en servir pour tester l'appartenance à un sous-espace.
**Prérequis :** fiche §4 ; M12a §6 · **Parcours :** C, E

Dans $\mathbb{R}^4$, $U = \operatorname{Vect}(\mathbf{a}, \mathbf{b})$ avec $\mathbf{a} = (1, 0, 3, -1)$ et $\mathbf{b} = (0, 1, -2, 2)$. On écrit $\mathbf{x} = (x_1, x_2, x_3, x_4)$, et l'on prend $x_3$ et $x_4$ comme coordonnées libres.

| | Question | Réponse attendue |
|---|---|---|
| a | $\dim U^\perp$ | un entier |
| b | le vecteur de $U^\perp$ avec $(x_3, x_4) = (1, 0)$ | une liste de 4 nombres |
| c | le vecteur de $U^\perp$ avec $(x_3, x_4) = (0, 1)$ | une liste de 4 nombres |
| d | vrai ou faux : $\mathbf{v} = (3, 1, -1, 0) \in U^\perp$ | `True` ou `False` |
| e | les coordonnées de $\mathbf{w} = (-1, -2, 1, 2)$, un vecteur de $U^\perp$, dans la base de $U^\perp$ formée des vecteurs de b) et c) | une liste de 2 nombres |
| f | vrai ou faux : les vecteurs de b) et c) sont orthogonaux | `True` ou `False` |
| g | vrai ou faux : $(1, -1, 5, -3) \in U$ | `True` ou `False` |

Dans ta copie : écris $U^\perp$ comme le noyau d'une matrice (laquelle ?), vérifie b) et c) par leurs produits scalaires avec $\mathbf{a}$ et $\mathbf{b}$, et vérifie que $\mathbf{w}$ est bien dans $U^\perp$. Réponds à g) de deux façons : avec $\mathbf{a}$ et $\mathbf{b}$, puis avec la base de $U^\perp$. Que faudrait-il faire pour avoir une base **orthonormée** de $U^\perp$ ?

### Ex M12b.7 — Projeter sur un plan de ℝ³ : avec une base quelconque, puis orthonormée ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un projeté par les équations normales, puis par une base orthonormée, et comparer les deux méthodes.
**Prérequis :** fiche §5 · **Parcours :** C, E

$U = \operatorname{Vect}(\mathbf{a}_1, \mathbf{a}_2)$ avec $\mathbf{a}_1 = (1, 0, 2)$ et $\mathbf{a}_2 = (0, -4, 1)$ ; $\mathbf{A} = [\mathbf{a}_1\ \mathbf{a}_2]$ ; $\mathbf{v} = (10, 3, -1)$. On admet que $\mathbf{q}_1 = \frac{1}{9}(4, 4, 7)$ et $\mathbf{q}_2 = \frac{1}{9}(1, -8, 4)$ forment une base orthonormée de $U$ (tu le vérifieras).

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{A}^\top\mathbf{A}$ | une matrice |
| b | $\mathbf{A}^\top\mathbf{v}$ | une liste de 2 nombres |
| c | les coefficients $(c_1, c_2)$ du projeté, $\mathbf{p} = c_1\mathbf{a}_1 + c_2\mathbf{a}_2$ | une liste de 2 nombres |
| d | le projeté $\mathbf{p}$ | une liste de 3 nombres |
| e | $(\mathbf{v} \cdot \mathbf{q}_1,\ \mathbf{v} \cdot \mathbf{q}_2)$ | une liste de 2 nombres |
| f | le résidu $\mathbf{v} - \mathbf{p}$ | une liste de 3 nombres |
| g | vrai ou faux : $\mathbf{v} - \mathbf{p}$ est orthogonal à $\mathbf{a}_1$ et à $\mathbf{a}_2$ | `True` ou `False` |

Dans ta copie : retrouve d) avec e). Vérifie que $\mathbf{q}_1$ et $\mathbf{q}_2$ sont dans $U$ (écris-les comme combinaisons de $\mathbf{a}_1$ et $\mathbf{a}_2$) et qu'ils sont orthonormés. Une fois la base orthonormée connue, quelle méthode demande le moins de calcul pour projeter dix vecteurs ?

### Ex M12b.8 — La matrice de projection : P² = P, Pᵀ = P, trace et rang ✏️ ★★ ⏱️ 15 min
**Objectif :** reconnaître une matrice de projection orthogonale à ses propriétés, et retrouver le sous-espace sur lequel elle projette.
**Prérequis :** fiche §5 ; M12a §4 · **Parcours :** C

$$\mathbf{P} = \frac{1}{3}\begin{pmatrix} 2 & -1 & 1 \\ -1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$

On veut savoir si $\mathbf{P}$ est la matrice d'une projection orthogonale de $\mathbb{R}^3$, et, si oui, sur quel sous-espace.

| | Question | Réponse attendue |
|---|---|---|
| a | vrai ou faux : $\mathbf{P}^\top = \mathbf{P}$ | `True` ou `False` |
| b | vrai ou faux : $\mathbf{P}^2 = \mathbf{P}$ | `True` ou `False` |
| c | $\mathbf{P}(1, 1, -1)$ | une liste de 3 nombres |
| d | $\mathbf{P}(1, 0, 1)$ | une liste de 3 nombres |
| e | $\operatorname{tr}\mathbf{P}$ | un nombre |
| f | $\operatorname{rg}\mathbf{P}$ | un entier |
| g | $(\mathbf{I} - \mathbf{P})(3, 0, 0)$ | une liste de 3 nombres |
| h | vrai ou faux : $\mathbf{M} = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ est la matrice d'une projection orthogonale | `True` ou `False` |

Dans ta copie : écris le calcul de $\mathbf{P}^2$. Que concluent a) et b) ensemble ? Déduis de c) le sous-espace $U$ sur lequel $\mathbf{P}$ projette (une équation), et explique pourquoi d) était prévisible. Relie e) et f) à la dimension de $U$. Sur quelle droite projette $\mathbf{I} - \mathbf{P}$ ? $\mathbf{P}$ est-elle inversible ? Pour h), calcule $\mathbf{M}^2$ et $\mathbf{M}^\top$, puis dessine ce que fait $\mathbf{M}$ : vers quelle droite, et le long de quelle direction ?

### Ex M12b.9 — La distance d'un point à un sous-espace, et le résidu orthogonal ✏️ ★ ⏱️ 15 min
**Objectif :** projeter avec une base orthogonale, calculer une distance à un sous-espace, et vérifier Pythagore.
**Prérequis :** fiche §5 · **Parcours :** C, E

Dans $\mathbb{R}^4$ : $\mathbf{u}_1 = (1, 1, 1, 1)$, $\mathbf{u}_2 = (1, -1, 2, -2)$, $U = \operatorname{Vect}(\mathbf{u}_1, \mathbf{u}_2)$ et $\mathbf{v} = (2, 0, 5, 1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | vrai ou faux : $\mathbf{u}_1$ et $\mathbf{u}_2$ sont orthogonaux | `True` ou `False` |
| b | le coefficient de $\mathbf{u}_1$ dans le projeté de $\mathbf{v}$ sur $U$ | un nombre |
| c | le coefficient de $\mathbf{u}_2$ | un nombre |
| d | le projeté $\mathbf{p}$ | une liste de 4 nombres |
| e | le résidu $\mathbf{v} - \mathbf{p}$ | une liste de 4 nombres |
| f | la distance de $\mathbf{v}$ à $U$ | un nombre |
| g | la distance de $\mathbf{v}$ à la droite $\operatorname{Vect}(\mathbf{u}_1)$ | un nombre (4 décimales) |
| h | $\lVert \mathbf{p} \rVert^2$ | un nombre |

Dans ta copie : vérifie que e) est orthogonal à $\mathbf{u}_1$ et à $\mathbf{u}_2$. Vérifie Pythagore avec $\lVert \mathbf{v} \rVert^2$, h) et f). Compare g) et f) : lequel est le plus grand, et pouvait-il en être autrement ?

### Ex M12b.10 — Des moindres carrés comme une projection : y, son projeté et le résidu ✏️ ★★ ⏱️ 20 min
**Objectif :** ajuster une droite par les équations normales, et lire le résultat comme une projection : résidu orthogonal, Pythagore.
**Prérequis :** fiche §5 et §6 ; M09b §3 · **Parcours :** C, E

Cinq exemples : $x = (1, 2, 4, 5, 8)$ et $y = (0, 2, 2, 3, 4)$. On ajuste une droite avec biais : $\mathbf{X} = [\mathbf{1} \mid \mathbf{x}]$, de forme $(5, 2)$, et $\mathbf{w}^* = (w_0, w_1)$ (biais, puis pente).

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{X}^\top\mathbf{X}$ | une matrice |
| b | $\mathbf{X}^\top\mathbf{y}$ | une liste de 2 nombres |
| c | $\mathbf{w}^*$ | une liste de 2 nombres (1 décimale) |
| d | les prédictions $\hat{\mathbf{y}}$ | une liste de 5 nombres (1 décimale) |
| e | le résidu $\mathbf{r} = \mathbf{y} - \hat{\mathbf{y}}$ | une liste de 5 nombres (1 décimale) |
| f | $\mathbf{X}^\top\mathbf{r}$ | une liste de 2 nombres |
| g | $\lVert \mathbf{r} \rVert^2$ | un nombre (1 décimale) |
| h | $\lVert \hat{\mathbf{y}} \rVert^2$ | un nombre (1 décimale) |

Dans ta copie : que dit la première coordonnée de f) des résidus, et pourquoi était-ce prévisible ? Vérifie Pythagore avec $\lVert \mathbf{y} \rVert^2$. Les vecteurs $\mathbf{1}$ et $\mathbf{x} - \bar{x}\mathbf{1}$ forment une base orthogonale de $\operatorname{Im}\mathbf{X}$ : projette $\mathbf{y}$ sur chacun, additionne, et compare avec d).

### Ex M12b.11 — La décomposition QR d'une matrice 3 × 2, puis les moindres carrés par R w = Qᵀy ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer une décomposition QR par Gram-Schmidt, puis résoudre des moindres carrés par un système triangulaire.
**Prérequis :** fiche §3 et §7 · **Parcours :** C

$$\mathbf{A} = \begin{pmatrix} 2 & 2 \\ 6 & 3 \\ 9 & 0 \end{pmatrix}, \qquad \mathbf{y} = (11, 3, 20).$$

| | Question | Réponse attendue |
|---|---|---|
| a | $r_{11} = \lVert \mathbf{a}_1 \rVert$ | un nombre |
| b | $r_{12} = \mathbf{q}_1 \cdot \mathbf{a}_2$ | un nombre |
| c | $r_{22}$ | un nombre |
| d | $\mathbf{q}_2$ | une liste de 3 nombres (4 décimales) |
| e | $\mathbf{R}$ | une matrice |
| f | $\mathbf{Q}^\top\mathbf{y}$ | une liste de 2 nombres |
| g | les poids $\mathbf{w}^*$ des moindres carrés, par $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$ | une liste de 2 nombres (4 décimales) |
| h | le résidu $\mathbf{y} - \mathbf{A}\mathbf{w}^*$ | une liste de 3 nombres |

Dans ta copie : vérifie $\mathbf{A} = \mathbf{Q}\mathbf{R}$ colonne par colonne. Résous aussi les équations normales $\mathbf{A}^\top\mathbf{A}\,\mathbf{w} = \mathbf{A}^\top\mathbf{y}$ et compare. Vérifie que h) est orthogonal aux colonnes de $\mathbf{A}$. Quelle ligne de $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$ as-tu résolue en premier, et pourquoi ?

### Ex M12b.12 — Le produit scalaire de fonctions sur [−1 ; 1] : orthogonaliser 1, x et x² ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer des produits scalaires de fonctions, orthogonaliser des polynômes, et projeter une fonction sur les polynômes de degré au plus 2.
**Prérequis :** fiche §3, §5 et §8 ; M02a (intégrales) · **Parcours :** C

Sur les fonctions continues de $[-1 ; 1]$, $\langle f, g \rangle = \int_{-1}^{1} f(x)\,g(x)\,dx$. On orthogonalise $1, x, x^2$ par Gram-Schmidt **sans normer** : $p_0 = 1$, $p_1 = x - \frac{\langle x, p_0 \rangle}{\langle p_0, p_0 \rangle}\,p_0$, puis $p_2 = x^2 - \frac{\langle x^2, p_0 \rangle}{\langle p_0, p_0 \rangle}\,p_0 - \frac{\langle x^2, p_1 \rangle}{\langle p_1, p_1 \rangle}\,p_1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\langle 1, 1 \rangle$ | un nombre |
| b | $\langle 1, x^2 \rangle$ | un nombre (4 décimales) |
| c | $\langle x, x^2 \rangle$ | un nombre |
| d | le nombre $c$ tel que $p_2 = x^2 + c$ | un nombre (4 décimales) |
| e | $\lVert p_2 \rVert^2$ | un nombre (4 décimales) |
| f | $\langle \lvert x \rvert, p_2 \rangle$ | un nombre (4 décimales) |
| g | le projeté de $\lvert x \rvert$ sur $\operatorname{Vect}(1, x, x^2)$, écrit $\alpha + \beta x + \gamma x^2$ : la liste $(\alpha, \beta, \gamma)$ | une liste de 3 nombres (4 décimales) |

Dans ta copie : pourquoi $p_1 = x$ (que vaut $\langle x, 1 \rangle$) ? Pour f) et g), découpe les intégrales en $0$ ou utilise la parité. Dessine $\lvert x \rvert$ et son projeté sur $[-1 ; 1]$ : où l'approximation est-elle la moins bonne ? Compare avec le projeté de $\lvert x \rvert$ sur $\operatorname{Vect}(1, x)$ seul.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M12b.13 — L'inégalité de Cauchy-Schwarz pour tout produit scalaire ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer Cauchy-Schwarz et son cas d'égalité pour un produit scalaire quelconque, par une projection, et l'appliquer à des fonctions.
**Prérequis :** fiche §1 et §5 ; M07.14 · **Parcours :** C

$\langle \cdot, \cdot \rangle$ est un produit scalaire sur un espace $V$, et $\lVert \mathbf{x} \rVert = \sqrt{\langle \mathbf{x}, \mathbf{x} \rangle}$. M07.14 démontrait l'inégalité pour le produit usuel par un discriminant ; on la démontre ici par une projection, en n'utilisant que les trois propriétés de la fiche (§1).
1. Soit $\mathbf{y} \ne \mathbf{0}$ et $t$ un réel. Développe $\lVert \mathbf{x} - t\,\mathbf{y} \rVert^2$ par bilinéarité et symétrie.
2. Prends $t = \frac{\langle \mathbf{x}, \mathbf{y} \rangle}{\lVert \mathbf{y} \rVert^2}$. Montre que $\mathbf{x} - t\,\mathbf{y}$ est orthogonal à $\mathbf{y}$, puis que $\lVert \mathbf{x} - t\,\mathbf{y} \rVert^2 = \lVert \mathbf{x} \rVert^2 - \frac{\langle \mathbf{x}, \mathbf{y} \rangle^2}{\lVert \mathbf{y} \rVert^2}$. Déduis-en $|\langle \mathbf{x}, \mathbf{y} \rangle| \le \lVert \mathbf{x} \rVert\,\lVert \mathbf{y} \rVert$. Traite aussi le cas $\mathbf{y} = \mathbf{0}$.
3. Montre qu'il y a égalité si et seulement si $\mathbf{x}$ et $\mathbf{y}$ sont colinéaires.
4. Déduis-en l'inégalité triangulaire $\lVert \mathbf{x} + \mathbf{y} \rVert \le \lVert \mathbf{x} \rVert + \lVert \mathbf{y} \rVert$.
5. Avec le produit scalaire de fonctions sur $[0 ; 1]$ et $g = 1$, montre que $\left(\int_0^1 f(x)\,dx\right)^2 \le \int_0^1 f(x)^2\,dx$ pour toute fonction continue $f$. Pour quelles fonctions y a-t-il égalité ? Que dit cette inégalité de la moyenne et de la moyenne des carrés d'une fonction ?

### Ex M12b.14 — Une famille orthogonale de vecteurs non nuls est libre ∂ ★ ⏱️ 15 min
**Objectif :** démontrer qu'une famille orthogonale de vecteurs non nuls est libre, et en tirer les coordonnées et l'égalité de Parseval.
**Prérequis :** fiche §2 ; M12a §2 et §3 · **Parcours :** C, E

$\mathbf{u}_1, \ldots, \mathbf{u}_k$ sont des vecteurs **non nuls**, deux à deux orthogonaux pour un produit scalaire $\langle \cdot, \cdot \rangle$.
1. On suppose $\sum_i \lambda_i\mathbf{u}_i = \mathbf{0}$. Calcule le produit scalaire des deux membres avec $\mathbf{u}_j$, et déduis-en $\lambda_j = 0$. Conclus.
2. Où as-tu utilisé l'hypothèse « non nuls » ? Donne une famille orthogonale qui n'est pas libre.
3. Déduis de 1 que $n$ vecteurs non nuls deux à deux orthogonaux de $\mathbb{R}^n$ forment une base.
4. Si $\mathbf{v} = \sum_i c_i\mathbf{u}_i$, montre que $c_j = \frac{\langle \mathbf{v}, \mathbf{u}_j \rangle}{\lVert \mathbf{u}_j \rVert^2}$.
5. Si de plus la famille est orthonormée, montre que $\lVert \mathbf{v} \rVert^2 = \sum_i c_i^2$ (Parseval).

### Ex M12b.15 — Gram-Schmidt donne une base orthonormée du même sous-espace ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer par récurrence que Gram-Schmidt est bien défini, rend une famille orthonormée, et engendre les mêmes sous-espaces, et en déduire la forme de R.
**Prérequis :** fiche §3 et §7 ; Ex M12b.14 ; R4 (récurrence) · **Parcours :** C

$\mathbf{a}_1, \ldots, \mathbf{a}_k$ sont libres. On construit $\mathbf{v}_j$ et $\mathbf{q}_j$ par les formules de la fiche (§3). On note $(H_j)$ : « $\mathbf{q}_1, \ldots, \mathbf{q}_j$ sont bien définis, orthonormés, et $\operatorname{Vect}(\mathbf{q}_1, \ldots, \mathbf{q}_j) = \operatorname{Vect}(\mathbf{a}_1, \ldots, \mathbf{a}_j)$ ».
1. Démontre $(H_1)$.
2. On suppose $(H_{j-1})$. Montre que $\mathbf{v}_j \ne \mathbf{0}$ (raisonne par l'absurde : que serait $\mathbf{a}_j$ ?).
3. Montre que $\langle \mathbf{v}_j, \mathbf{q}_i \rangle = 0$ pour $i < j$, puis que $\mathbf{q}_1, \ldots, \mathbf{q}_j$ sont orthonormés.
4. Montre que $\operatorname{Vect}(\mathbf{q}_1, \ldots, \mathbf{q}_j) = \operatorname{Vect}(\mathbf{a}_1, \ldots, \mathbf{a}_j)$ (une inclusion, puis les dimensions). Conclus par récurrence.
5. Déduis-en que la matrice $\mathbf{R}$ telle que $\mathbf{A} = \mathbf{Q}\mathbf{R}$ est triangulaire supérieure, et que $r_{jj} = \lVert \mathbf{v}_j \rVert > 0$.

### Ex M12b.16 — L'orthogonal de l'image de A est le noyau de Aᵀ ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer le lien entre complément orthogonal, noyau et transposée, en tirer la dimension du complément, et un critère d'existence de solutions.
**Prérequis :** fiche §4 ; M12a §4 et §6 · **Parcours :** C, E

$\mathbf{A}$ a la forme $(m, n)$ ; le produit scalaire est le produit usuel.
1. Montre que $\mathbf{y} \in (\operatorname{Im}\mathbf{A})^\perp$ si et seulement si $\mathbf{y}$ est orthogonal à chaque colonne de $\mathbf{A}$. Déduis-en $(\operatorname{Im}\mathbf{A})^\perp = \ker\mathbf{A}^\top$.
2. De la même façon, montre que $\ker\mathbf{A} = (\operatorname{Im}\mathbf{A}^\top)^\perp$ : le noyau est l'orthogonal des lignes.
3. Avec le théorème du rang et $\operatorname{rg}\mathbf{A}^\top = \operatorname{rg}\mathbf{A}$, montre que $\dim(\operatorname{Im}\mathbf{A})^\perp = m - \operatorname{rg}\mathbf{A}$. Déduis-en, pour tout sous-espace $U$ de $\mathbb{R}^m$, $\dim U + \dim U^\perp = m$.
4. Montre que si $\mathbf{A}\mathbf{x} = \mathbf{b}$ a une solution, alors $\mathbf{b}$ est orthogonal à $\ker\mathbf{A}^\top$. (La réciproque est vraie aussi, admise ici : elle découle de 3.)
5. Application : $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 0 & 1 \end{pmatrix}$. Calcule $\ker\mathbf{A}^\top$, puis dis pour quels $t$ le système $\mathbf{A}\mathbf{x} = (1, t, 0)$ a une solution.

### Ex M12b.17 — Le projeté orthogonal est le point le plus proche (Pythagore) ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'existence et l'unicité du projeté, qu'il est le point le plus proche, et en déduire les équations normales sans dérivée.
**Prérequis :** fiche §5 et §6 ; M07.17 · **Parcours :** C, E

$U$ est un sous-espace de $\mathbb{R}^m$, de base orthonormée $\mathbf{q}_1, \ldots, \mathbf{q}_k$, et $\mathbf{v} \in \mathbb{R}^m$. On pose $\mathbf{p} = \sum_i \langle \mathbf{v}, \mathbf{q}_i \rangle\,\mathbf{q}_i$.
1. Montre que $\mathbf{p} \in U$ et que $\mathbf{v} - \mathbf{p}$ est orthogonal à chaque $\mathbf{q}_j$, donc à tout $U$.
2. Démontre Pythagore : si $\mathbf{a} \perp \mathbf{b}$, alors $\lVert \mathbf{a} + \mathbf{b} \rVert^2 = \lVert \mathbf{a} \rVert^2 + \lVert \mathbf{b} \rVert^2$.
3. Soit $\mathbf{u} \in U$. En écrivant $\mathbf{v} - \mathbf{u} = (\mathbf{v} - \mathbf{p}) + (\mathbf{p} - \mathbf{u})$, montre que $\lVert \mathbf{v} - \mathbf{u} \rVert \ge \lVert \mathbf{v} - \mathbf{p} \rVert$, avec égalité si et seulement si $\mathbf{u} = \mathbf{p}$.
4. Montre l'unicité : si $\mathbf{p}' \in U$ vérifie aussi $\mathbf{v} - \mathbf{p}' \perp U$, alors $\mathbf{p}' = \mathbf{p}$ (que peut-on dire de $\mathbf{p} - \mathbf{p}'$ ?).
5. Application aux moindres carrés : $U = \operatorname{Im}\mathbf{X}$, colonnes libres (une base orthonormée de $U$ existe : M12b.15). Déduis de 1, 3 et 4 que $\mathbf{w}^*$ minimise $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert$ si et seulement si $\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w}^*) = \mathbf{0}$, sans calculer de gradient.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12b.18 — Pont : retirer d'une feature ce qu'explique une autre, une projection puis un résidu 🔗 ★ ⏱️ 15 min
**Objectif :** retirer d'une feature sa partie expliquée par une autre, et voir ce que le résidu dit du poids de cette feature dans une régression.
**Prérequis :** fiche §3, §5 et §6 ; M09b §3 · **Parcours :** C, E

Un tableau de 4 exemples a deux features, $\mathbf{x}_1 = (2, 2, 1, 1)$ et $\mathbf{x}_2 = (1, 3, 0, 2)$, et une cible $\mathbf{y} = (3, 6, 1, 4)$. On ajuste un modèle linéaire sans biais.

| | Question | Réponse attendue |
|---|---|---|
| a | le coefficient $t = \frac{\mathbf{x}_2 \cdot \mathbf{x}_1}{\lVert \mathbf{x}_1 \rVert^2}$ | un nombre |
| b | le projeté de $\mathbf{x}_2$ sur $\operatorname{Vect}(\mathbf{x}_1)$ | une liste de 4 nombres |
| c | le résidu $\mathbf{r} = \mathbf{x}_2 - t\,\mathbf{x}_1$ | une liste de 4 nombres |
| d | $\mathbf{r} \cdot \mathbf{x}_1$ | un nombre |
| e | la part de $\lVert \mathbf{x}_2 \rVert^2$ expliquée par $\mathbf{x}_1$ : $\frac{\lVert t\,\mathbf{x}_1 \rVert^2}{\lVert \mathbf{x}_2 \rVert^2}$ | un nombre (4 décimales) |
| f | $\frac{\mathbf{y} \cdot \mathbf{r}}{\lVert \mathbf{r} \rVert^2}$ | un nombre (2 décimales) |
| g | les poids $(w_1, w_2)$ de la régression de $\mathbf{y}$ sur $\mathbf{x}_1$ et $\mathbf{x}_2$ | une liste de 2 nombres (2 décimales) |

Dans ta copie : compare f) et g). Pourquoi $\operatorname{Vect}(\mathbf{x}_1, \mathbf{x}_2) = \operatorname{Vect}(\mathbf{x}_1, \mathbf{r})$ ? Écris les prédictions du modèle avec $\mathbf{x}_1$ et $\mathbf{r}$, et retrouve la comparaison de f) et g). Que voudrait dire, sur ces données, « l'effet de $\mathbf{x}_2$ à $\mathbf{x}_1$ fixé » ? Que deviendrait le poids de $\mathbf{x}_2$ si $\mathbf{r}$ était presque nul ?

### Ex M12b.19 — Pont : projeter sur k directions orthonormées, reconstruire, et l'erreur par Pythagore 🔗 ★★ ⏱️ 15 min
**Objectif :** résumer un vecteur par ses coordonnées sur quelques directions orthonormées, le reconstruire, et montrer que l'erreur de reconstruction est faite des coordonnées écartées.
**Prérequis :** fiche §2 et §5 · **Parcours :** C, E

Dans $\mathbb{R}^4$, $\mathbf{u}_1 = \frac{1}{2}(1, 1, 1, 1)$, $\mathbf{u}_2 = \frac{1}{2}(1, -1, 1, -1)$, $\mathbf{u}_3 = \frac{1}{2}(1, 1, -1, -1)$, $\mathbf{u}_4 = \frac{1}{2}(1, -1, -1, 1)$ forment une base orthonormée. On garde $k = 2$ directions : $\mathbf{U} = [\mathbf{u}_1\ \mathbf{u}_2]$, de forme $(4, 2)$. Un vecteur $\mathbf{x}$ est **résumé** par ses coordonnées $\mathbf{z} = \mathbf{U}^\top\mathbf{x}$ (2 nombres) et **reconstruit** par $\hat{\mathbf{x}} = \mathbf{U}\mathbf{z}$. On prend $\mathbf{x} = (4, 2, 3, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | vrai ou faux : $\mathbf{U}^\top\mathbf{U} = \mathbf{I}_2$ | `True` ou `False` |
| b | les coordonnées $\mathbf{z}$ | une liste de 2 nombres |
| c | la reconstruction $\hat{\mathbf{x}}$ | une liste de 4 nombres (1 décimale) |
| d | l'erreur $\mathbf{e} = \mathbf{x} - \hat{\mathbf{x}}$ | une liste de 4 nombres (1 décimale) |
| e | $\mathbf{U}^\top\mathbf{e}$ | une liste de 2 nombres |
| f | $\lVert \mathbf{e} \rVert^2$ | un nombre (2 décimales) |
| g | les coordonnées écartées $(\mathbf{u}_3 \cdot \mathbf{x},\ \mathbf{u}_4 \cdot \mathbf{x})$ | une liste de 2 nombres |
| h | vrai ou faux : $\mathbf{U}\mathbf{U}^\top = \mathbf{I}_4$ | `True` ou `False` |

Dans ta copie : compare f) avec la somme des carrés de g), et $\lVert \mathbf{x} \rVert^2$ avec $\lVert \mathbf{z} \rVert^2 + \lVert \mathbf{e} \rVert^2$. Puis démontre, pour une base orthonormée quelconque $(\mathbf{u}_1, \ldots, \mathbf{u}_n)$ de $\mathbb{R}^n$ et $k$ directions gardées, que $\lVert \mathbf{x} - \mathbf{U}\mathbf{U}^\top\mathbf{x} \rVert^2$ est la somme des carrés des coordonnées écartées (écris $\mathbf{x}$ dans la base complète). Que fait $\mathbf{U}\mathbf{U}^\top$ à $\mathbf{u}_1$, puis à $\mathbf{u}_3$ ? Compare avec h).

### Ex M12b.20 — MML §3.2, §3.5 à §3.7 : produits scalaires, orthogonalité, fonctions, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais les définitions générales du produit scalaire, des bases orthonormées, du complément orthogonal et du produit scalaire de fonctions, et les relier à la fiche.
**Prérequis :** fiche §1, §2, §4 et §8 · **Parcours :** C

Lis MML §3.2 (en survolant le §3.2.1), puis §3.5, §3.6 et §3.7. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Au §3.2.2, comment le livre définit-il une application bilinéaire, puis un produit scalaire ? Quels noms donne-t-il à un espace muni d'un produit scalaire, et à celui muni du produit usuel ?
2. Le livre donne un produit scalaire de $\mathbb{R}^2$ qui n'est pas le produit usuel. Écris sa matrice et vérifie, avec le critère de la fiche (§1), qu'elle est définie positive.
3. Au §3.2.3, quel lien le livre établit-il entre produits scalaires de $\mathbb{R}^n$ et matrices ? Quelles propriétés d'une matrice symétrique définie positive énonce-t-il (sur son noyau, sur sa diagonale) ? Justifie l'une d'elles avec la fiche.
4. Au §3.5, comment le livre définit-il une base orthonormée ? Quel procédé mentionne-t-il pour en construire une, et quel lien fait-il avec le pivot de Gauss ?
5. Au §3.6, comment le livre décrit-il le complément orthogonal d'un plan de $\mathbb{R}^3$ ? Quel nom donne-t-il au vecteur qui l'engendre, et quelle dimension donne-t-il à $U^\perp$ en général ?
6. Au §3.7, comment le livre définit-il le produit scalaire de deux fonctions ? Quel exemple de fonctions orthogonales donne-t-il, et pourquoi l'intégrale de leur produit est-elle nulle ? Quelle famille infinie de fonctions orthogonales cite-t-il ?
7. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12b.21 — MML §3.8 et §9.4 : projections, Gram-Schmidt et moindres carrés 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la construction des projections orthogonales, de Gram-Schmidt et de la lecture géométrique des moindres carrés, et la comparer avec la fiche.
**Prérequis :** fiche §3, §5 et §6 · **Parcours :** C

Lis MML §3.8, puis §9.4. Réponds dans ta copie, **avec tes mots**.
1. Au début du §3.8, comment le livre définit-il une projection ? Quelle propriété de sa matrice en découle ?
2. Au §3.8.1, en quelles étapes le livre construit-il la projection sur une droite ? Quelle matrice de projection obtient-il ? Compare avec M07 et avec la fiche (§5).
3. Au §3.8.2, quel système le livre résout-il pour projeter sur un sous-espace, et quel nom lui donne-t-il ? Quelle simplification signale-t-il quand la base est orthonormée ?
4. Quel lien le livre fait-il entre la projection et un système $\mathbf{A}\mathbf{x} = \mathbf{b}$ sans solution ? Comment appelle-t-il l'écart $\lVert \mathbf{x} - \pi_U(\mathbf{x}) \rVert$ ?
5. Au §3.8.3, comment le livre écrit-il le procédé de Gram-Schmidt ? En quoi diffère-t-il de la fiche (§3) : normalise-t-il au même moment ?
6. Au §3.8.4, comment projette-t-on sur un sous-espace affine $L = \mathbf{x}_0 + U$ ? Applique la règle au plan $x + y + z = 3$ de $\mathbb{R}^3$ et au point $(3, 3, 3)$.
7. Au §9.4, quel résultat le livre énonce-t-il sur les prédictions de la régression linéaire au maximum de vraisemblance ? Relie-le à la matrice chapeau de M09b.
8. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12b.22 — Fermi : le coût de Gram-Schmidt sur une matrice 100 000 × 50 🧮 ★ ⏱️ 10 min
**Objectif :** estimer le nombre d'opérations et la mémoire de Gram-Schmidt sur une matrice de données réaliste, et le comparer aux équations normales.
**Prérequis :** fiche §3 et §7 · **Parcours :** C

Une matrice de données $\mathbf{X}$ a $m = 100\,000$ lignes et $n = 50$ colonnes. Ordres de grandeur seulement.
1. Pour la colonne $k$, combien de produits scalaires de vecteurs de $\mathbb{R}^m$ et combien de mises à jour $\mathbf{v} \leftarrow \mathbf{v} - c\,\mathbf{q}$ fait Gram-Schmidt ? Combien en tout, pour les 50 colonnes ?
2. Un produit scalaire ou une mise à jour de longueur $m$ coûte environ $2m$ opérations (une multiplication et une addition par coordonnée). Combien d'opérations pour Gram-Schmidt ? Retrouve la formule $\approx 2mn^2$.
3. À $10^9$ opérations par seconde, combien de temps ?
4. Combien de mémoire occupent $\mathbf{X}$ et $\mathbf{Q}$ en `float64` (8 octets par nombre) ?
5. Former $\mathbf{X}^\top\mathbf{X}$ coûte environ $mn^2$ opérations. QR est-elle beaucoup plus chère ? Que se passe-t-il pour Gram-Schmidt si $n$ passe à 5 000 ?

### Ex M12b.23 — Expliquer pourquoi le projeté est le point le plus proche 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer en mots, sans calcul, pourquoi la projection orthogonale donne le point le plus proche.
**Prérequis :** fiche §5 · **Parcours :** C, E

Un ami qui a oublié ses cours de géométrie te demande pourquoi, pour trouver le point d'un plan le plus proche d'un point de l'espace, « on descend à angle droit ». Explique-lui, **en huit lignes au plus**, sans formule : ce qu'est la projection orthogonale, pourquoi tout autre point du plan est plus loin (pense au triangle rectangle et à son côté le plus long), et un exemple de la vie courante ou du machine learning où l'on cherche ainsi « le plus proche dans un ensemble permis ».

<a id="entretien"></a>

## 💼 Entretien

### M12b.E1 — « Pourquoi résoudre des moindres carrés par QR plutôt que par les équations normales ? » 💼 ★ ⏱️ 10 min
*Fiche §6 et §7 · parcours C*

« Pourquoi résoudre des moindres carrés par QR plutôt que par les équations normales ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit donner les deux méthodes en une phrase chacune, ce que fait $\mathbf{X}^\top\mathbf{X}$ aux erreurs d'arrondi quand des features sont presque dépendantes, pourquoi QR évite ce problème, ce qu'utilisent les bibliothèques (Householder, LAPACK, ou la SVD), et le cas où les équations normales restent acceptables. Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M12b.E2 — « Qu'est-ce qu'une matrice orthogonale, et pourquoi est-elle agréable en calcul numérique ? » 💼 ★ ⏱️ 10 min
*Fiche §2 · parcours C*

« Qu'est-ce qu'une matrice orthogonale, et pourquoi est-elle agréable en calcul numérique ? »

Prépare une réponse orale de **60 secondes**. Elle doit donner la définition, ce qu'elle conserve, son inverse, deux exemples géométriques, une raison numérique (les erreurs d'arrondi), et un endroit du machine learning où l'on en rencontre. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m12b_orthogonalite/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M12b.24 | Gram-Schmidt, classique et modifié · `gram_schmidt` | 🔨 | ★★ | 25 | C, E |
| M12b.25 | La projection orthogonale sur un sous-espace · `project` | 🔨 | ★ | 15 | C, E |
| M12b.26 | La décomposition QR et les moindres carrés par QR · `qr, least_squares_qr` | 🔨 | ★★ | 25 | C |
| M12b.27 | `np.linalg.qr` et `lstsq` contre ta projection et ta QR : les signes de Q et de R | 📦 | ★ | 15 | C |
| M12b.28 | Prédire : Gram-Schmidt classique sur des vecteurs presque colinéaires, QᵀQ vaut-il encore I ? | 🔮 | ★ | 10 | C, E |
| M12b.29 | Gram-Schmidt classique contre modifié : l'orthogonalité perdue quand les colonnes sont presque dépendantes | 🔬 | ★★ | 20 | C |
| M12b.30 | Projeter un nuage de ℝ³ sur un plan : les résidus orthogonaux en image | 🎨 | ★ | 20 | C, E |
| M12b.31 | Chasse à l'erreur : une normalisation oubliée, QQᵀ sur une base non orthonormée, R w = Qᵀy résolu dans le mauvais sens | 🐛 | ★ | 15 | C |
| M12b.32 | Un test de propriétés pour la projection : idempotente, symétrique, résidu orthogonal | 🛠️ | ★ | 15 | C |
| M12b.33 | Défi : des colonnes presque dépendantes, des moindres carrés à 1e−8 près de `lstsq` par l'orthogonalisation de [X \| y] | 🏆 | ★★★ | 30 | C |
