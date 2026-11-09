# M12a · Espaces vectoriels et applications linéaires — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12a.Q1 — Sous-espace ou pas ?
1. **Oui** : une droite par l'origine, $\{t\,(1, 3)\}$.
2. **Non** : $(0, 0)$ ne vérifie pas $0 = 3 \times 0 + 1$.
3. **Oui** : l'ensemble des solutions d'un système homogène (deux équations de second membre nul) ; c'est l'intersection de deux plans par l'origine, une droite.
4. **Non** : $(1, 0)$ y est, mais $(-1) \times (1, 0) = (-1, 0)$ n'y est pas.
5. **Non** : $(1, 0)$ et $(0, 1)$ y sont (sur les axes), leur somme $(1, 1)$ non ($1 \times 1 \ne 0$). C'est la réunion des deux axes (M12a.14).
6. **Non** : le polynôme nul n'est pas de degré 2 ; et $x^2 + x$ et $-x^2$ sont de degré 2, mais leur somme $x$ ne l'est pas. Les polynômes de degré **au plus** 2 forment, eux, un sous-espace.

### M12a.Q2 — Combinaison linéaire et famille génératrice
1. **Oui** : $(-6, 4) = -2\,(3, -2)$.
2. **Non** : $(-6, 3) = -3\,(2, -1)$, les deux vecteurs sont colinéaires et n'engendrent qu'une droite.
3. **Quatre** : une famille génératrice de $\mathbb{R}^4$ a au moins $\dim\mathbb{R}^4 = 4$ vecteurs.
4. Le **plan** $z = 0$ : les vecteurs $(x, y, 0)$.
5. **Vrai** : la combinaison dont tous les coefficients sont nuls.
6. **Vrai** : $\mathbf{u} + \mathbf{v}$ et $\mathbf{u} - \mathbf{v}$ sont dans le plan, et réciproquement $\mathbf{u} = \frac{1}{2}\big((\mathbf{u} + \mathbf{v}) + (\mathbf{u} - \mathbf{v})\big)$ et $\mathbf{v} = \frac{1}{2}\big((\mathbf{u} + \mathbf{v}) - (\mathbf{u} - \mathbf{v})\big)$ : les deux familles engendrent le même plan.

### M12a.Q3 — Libre ou liée ?
1. **Liée** : $(4, -10) = -2\,(-2, 5)$.
2. **Libre** : la matrice des trois vecteurs est triangulaire avec des 1 sur la diagonale, trois pivots.
3. **Liée**, toujours : plus de 3 vecteurs de $\mathbb{R}^3$.
4. **Liée** : $1 \cdot \mathbf{0} = \mathbf{0}$ est une combinaison nulle non triviale.
5. **Libre** : un vecteur non nul seul ($\lambda\mathbf{v} = \mathbf{0}$ impose $\lambda = 0$).
6. **Vrai** : une combinaison nulle de $\mathbf{u}$ et $\mathbf{v}$ est une combinaison nulle des trois, avec 0 devant $\mathbf{w}$ ; ses coefficients sont donc nuls.

### M12a.Q4 — Base et dimension : vrai ou faux
1. **Vrai** : $n$ vecteurs libres d'un espace de dimension $n$ forment une base.
2. **Faux** : $(1, x, x^2, x^3, x^4)$ est une base, de 5 vecteurs ; la dimension est 5.
3. **Faux** : un plan est de dimension 2, une base en a deux vecteurs.
4. **Vrai** (M12a.15).
5. **Faux** : il en a une infinité ; $(2\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3)$ en est une autre.
6. **Vrai** : $2 \times 3 = 6$ matrices à un seul 1 forment une base.

### M12a.Q5 — Le rang d'une matrice, d'une transposée, d'un produit
1. **4** : $\operatorname{rg} \le \min(4, 7)$.
2. **3** : $\operatorname{rg}(\mathbf{A}^\top) = \operatorname{rg}(\mathbf{A})$.
3. **2** : $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \min(2, 4)$.
4. **1** : toutes les colonnes de $\mathbf{u}\mathbf{v}^\top$ sont des multiples de $\mathbf{u}$, et l'une au moins n'est pas nulle.
5. **2** : multiplier par une matrice inversible ne change pas le rang.
6. **5** : les 6 lignes centrées ont une somme nulle, donc $\operatorname{rg} \le 6 - 1 = 5$ (et $\le 10$).

### M12a.Q6 — Linéaire, affine, ou ni l'un ni l'autre ?
1. **Linéaire** : de matrice $\begin{pmatrix} 3 & -1 \\ 0 & 2 \end{pmatrix}$.
2. **Affine** : la translation de vecteur $(1, 0)$ ; pas linéaire, car $g(0, 0) = (1, 0) \ne \mathbf{0}$.
3. **Ni l'un ni l'autre** : $h(2) = 4 \ne 2\,h(1)$, et ce n'est pas une droite.
4. **Linéaire** : $(\lambda P + \mu Q)' = \lambda P' + \mu Q'$.
5. **Ni l'un ni l'autre** : $\lVert -\mathbf{x} \rVert = \lVert \mathbf{x} \rVert \ne -\lVert \mathbf{x} \rVert$ ; et, le long de la droite $t\,\mathbf{x}$, elle vaut $|t|\,\lVert \mathbf{x} \rVert$, qui n'est pas affine en $t$.
6. **Affine** : partie linéaire $z \mapsto 4z$, translation $-7$.

### M12a.Q7 — Noyau et image : qui vit où ?
1. $\mathbb{R}^5$ : l'espace de départ, celui des $\mathbf{x}$ (5 colonnes).
2. $\mathbb{R}^3$ : l'espace d'arrivée (3 lignes).
3. **2** : $\operatorname{rg}(\mathbf{A}) \le 3$, donc $\dim\ker\mathbf{A} = 5 - \operatorname{rg}(\mathbf{A}) \ge 2$.
4. **Non** : son noyau n'est jamais réduit à $\{\mathbf{0}\}$.
5. $\mathbb{R}^3$ tout entier : $\mathbf{A}$ est surjective.
6. Les vecteurs $\mathbf{x}_p + \mathbf{h}$, avec $\mathbf{h} \in \ker\mathbf{A}$.

### M12a.Q8 — Changer de base : ce qui change et ce qui reste
1. $\mathbf{S}^{-1}\mathbf{x}$ (car $\mathbf{x} = \mathbf{S}\mathbf{x}'$).
2. $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$.
3. Le **même** : $\mathbf{S}$ et $\mathbf{S}^{-1}$ sont inversibles.
4. **Faux** en général ; vrai par exemple si $\mathbf{A} = \lambda\mathbf{I}$ (plus généralement si $\mathbf{A}\mathbf{S} = \mathbf{S}\mathbf{A}$).
5. $\mathbf{I}$ : l'identité a la même matrice dans toutes les bases.
6. $(5, 0, \ldots, 0)$ : $\mathbf{S}^{-1}\mathbf{A}\mathbf{s}_1 = \mathbf{S}^{-1}(5\,\mathbf{s}_1) = 5\,\mathbf{e}_1$, car $\mathbf{S}^{-1}\mathbf{s}_1 = \mathbf{e}_1$ (les coordonnées de $\mathbf{s}_1$ dans la base).

<a id="rappels"></a>

## 🔁 Rappels

### M12a.R1 — Le pivot de Gauss et la forme échelonnée réduite (M09a)
1. $L_1 \leftarrow \frac{1}{2}L_1$ donne $(1, 2, 1)$ ; $L_2 \leftarrow L_2 - L_1$ et $L_3 \leftarrow L_3 - L_1$ donnent $(0, 1, 1)$ et $(0, -1, -1)$ ; $L_3 \leftarrow L_3 + L_2$ annule la dernière ligne ; $L_1 \leftarrow L_1 - 2L_2$ donne $(1, 0, -1)$. Forme réduite : $\begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.
2. Les colonnes 1 et 2.
3. **2**.
4. $x_3$.
5. $x_3 = t$, $x_1 = t$, $x_2 = -t$ : les vecteurs $t\,(1, -1, 1)$, $t \in \mathbb{R}$. Vérification : $2 - 4 + 2 = 0$, $1 - 3 + 2 = 0$, $1 - 1 = 0$.
6. Échanger deux lignes ; multiplier une ligne par un nombre non nul ; ajouter à une ligne un multiple d'une autre ligne.

### M12a.R2 — Produit matriciel et formes (M09a)
1. $(2, 2)$.
2. $\begin{pmatrix} 2 + 0 - 2 & 1 + 0 + 0 \\ 6 + 0 + 1 & 3 - 1 + 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 7 & 2 \end{pmatrix}$.
3. $(3, 3)$.
4. $(0, 1)$ : la deuxième colonne de $\mathbf{A}$.
5. $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ : l'ordre s'inverse.

### M12a.R3 — Combinaisons linéaires et produit scalaire dans ℝⁿ (M07)
1. $(2 - 3,\ -4 - 0,\ 4 + 1) = (-1, -4, 5)$.
2. $3 + 0 - 2 = 1$.
3. $\sqrt{1 + 4 + 4} = 3$.
4. **Non** : $(\mathbf{u} + \mathbf{v}) \cdot (\mathbf{u} - \mathbf{v}) = \lVert \mathbf{u} \rVert^2 - \lVert \mathbf{v} \rVert^2 = 9 - 10 = -1 \ne 0$.
5. $\alpha = 2$, $\beta = 1$ : la troisième coordonnée donne $2\alpha - \beta = 3$, la première $\alpha + 3\beta = 5$ ; d'où $\beta = 1$, $\alpha = 2$ ; la deuxième se vérifie, $-4 + 0 = -4$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12a.1 — Reconnaître des sous-espaces de ℝ³ et de l'espace des polynômes

**Réponses** : a) `True` · b) `False` · c) `True` · d) `False` · e) `False` · f) `True` · g) `False` · h) `[4, -2, 6]`.

**Démarche.**
- a) $(0, 0, 0)$ vérifie $2x - y + 4z = 0$ ; si $\mathbf{u}$ et $\mathbf{v}$ la vérifient, $2(\lambda u_1 + \mu v_1) - (\lambda u_2 + \mu v_2) + 4(\lambda u_3 + \mu v_3) = \lambda \cdot 0 + \mu \cdot 0 = 0$. Un plan par l'origine.
- b) $(0, 0, 0)$ donne $0 - 0 = 0 \ne 1$ : pas de vecteur nul.
- c) $U_3 = \operatorname{Vect}\big((2, -1, 3)\big)$ : $t = 0$ donne $\mathbf{0}$, et $\lambda\,t\,\mathbf{d} + \mu\,s\,\mathbf{d} = (\lambda t + \mu s)\,\mathbf{d}$.
- d) $(1, 0, 1)$ et $(0, 1, 1)$ sont dans $U_4$ ($1 + 0 = 1$), pas leur somme $(1, 1, 2)$ ($1 + 1 = 2 \ne 4$). La multiplication ne pose pas de problème : $(\lambda x)^2 + (\lambda y)^2 = \lambda^2(x^2 + y^2) = \lambda^2 z^2 = (\lambda z)^2$. C'est un cône, pas un plan.
- e) $(0, 1, 0)$ y est ($0 \le 1$), mais $-1 \times (0, 1, 0) = (0, -1, 0)$ non ($0 > -1$) : un demi-espace (M07 §5).
- f) Le polynôme nul s'annule en 1 ; et $(\lambda P + \mu Q)(1) = \lambda P(1) + \mu Q(1) = 0$.
- g) Le polynôme nul vaut 0 en 0, pas 1.
- h) $2t = 4$, donc $t = 2$ : $(4, -2, 6)$.

**Erreurs fréquentes.** Vérifier seulement la stabilité par addition (en e), la somme de deux vecteurs qui vérifient $x \le y$ la vérifie encore) ; répondre `True` en d) parce que l'équation « a l'air » d'un plan ; en h), prendre $t = 4$.

**Variante.** $\{(x, y, z) : x = 2y \text{ et } z = 0\}$ est-il un sous-espace ? *Réponse* : oui, l'intersection de deux plans par l'origine (M12a.14) : la droite $\operatorname{Vect}\big((2, 1, 0)\big)$.

### Ex M12a.2 — Écrire un vecteur comme combinaison linéaire : un système à résoudre

**Réponses** : a) `[2, -1]` · b) `False` · c) `1` · d) `[-1, 5, 3]` · e) `True` · f) `1`.

**Démarche.**
- a) $\lambda_1(1, -1, 2) + \lambda_2(3, 0, 1) = (-1, -2, 3)$ : la deuxième coordonnée donne $-\lambda_1 = -2$, donc $\lambda_1 = 2$ ; la première, $2 + 3\lambda_2 = -1$, donc $\lambda_2 = -1$ ; la troisième se vérifie : $4 - 1 = 3$.
- b) La deuxième coordonnée donne $\lambda_1 = -1$, la première $\lambda_2 = \frac{2}{3}$, et la troisième vaudrait $-2 + \frac{2}{3} = -\frac{4}{3} \ne 1$.
- c) La troisième coordonnée donne $2\lambda_1 + \lambda_2 = 0$, la première $\lambda_1 + 3\lambda_2 = 5$ : $\lambda_2 = -2\lambda_1$, puis $-5\lambda_1 = 5$, $\lambda_1 = -1$, $\lambda_2 = 2$. La deuxième coordonnée est $-\lambda_1 = 1$.
- d) $\mathbf{n} \cdot \mathbf{u}_1 = a - b + 6 = 0$ et $\mathbf{n} \cdot \mathbf{u}_2 = 3a + 3 = 0$ : $a = -1$, $b = 5$.
- e) $\mathbf{b} = 2\mathbf{u}_1 - \mathbf{u}_2$, donc $\mathbf{u}_2 = 2\mathbf{u}_1 - \mathbf{b}$ : chaque famille est faite de combinaisons de l'autre, et les deux engendrent le même plan.
- f) $\mathbf{u}_1$ et $\mathbf{u}_2$ ne sont pas colinéaires : ils engendrent un plan ; un vecteur hors du plan suffit pour engendrer $\mathbb{R}^3$.

Pour la copie : $\operatorname{Vect}(\mathbf{u}_1, \mathbf{u}_2) = \{(x, y, z) : -x + 5y + 3z = 0\}$. Pour b), $-1 + 5 + 3 = 7 \ne 0$ ; pour c), $-5 + 5k = 0$ donne $k = 1$. En a), trois équations pour deux inconnues : deux suffisent à trouver $\lambda_1$ et $\lambda_2$, et la troisième dit si $\mathbf{b}$ est vraiment dans le plan.

**Erreurs fréquentes.** Résoudre deux équations et oublier de vérifier la troisième (b semble alors avoir une solution) ; inverser l'ordre de $\lambda_1$ et $\lambda_2$ ; un signe en c), où la deuxième coordonnée est $-\lambda_1$.

**Variante.** $(2, -2, 4)$ est-il dans le plan ? *Réponse* : oui, c'est $2\mathbf{u}_1$, coefficients $(2, 0)$ ; et $-2 - 10 + 12 = 0$.

### Ex M12a.3 — L'indépendance de trois vecteurs de ℝ³ par le pivot de Gauss

**Réponses** : a) `2` · b) `False` · c) `[2, -1]` · d) `[-2, 1, 1]` · e) `-7` · f) `True`.

**Démarche.**
- a) $\begin{pmatrix} 1 & 0 & 2 \\ 2 & 1 & 3 \\ -1 & 3 & -5 \end{pmatrix}$ : $L_2 \leftarrow L_2 - 2L_1$ et $L_3 \leftarrow L_3 + L_1$ donnent $(0, 1, -1)$ et $(0, 3, -3)$ ; $L_3 \leftarrow L_3 - 3L_2$ annule la dernière ligne ; $L_1$ reste $(1, 0, 2)$. Forme réduite $\begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$ : deux pivots.
- b) La troisième colonne n'a pas de pivot : liée.
- c) La troisième colonne de la forme réduite, $(2, -1)$ : $\mathbf{v}_3 = 2\mathbf{v}_1 - \mathbf{v}_2$ ; vérification : $(2 - 0,\ 4 - 1,\ -2 - 3) = (2, 3, -5)$.
- d) $2\mathbf{v}_1 - \mathbf{v}_2 - \mathbf{v}_3 = \mathbf{0}$, et avec $x_3 = 1$ : $(-2, 1, 1)$.
- e) $(1, 0, k) = a\mathbf{v}_1 + b\mathbf{v}_2$ : la première coordonnée donne $a = 1$, la deuxième $2 + b = 0$, $b = -2$ ; la troisième, $k = -1 - 6 = -7$.
- f) Avec $(2, 3, -4)$, la dernière ligne devient $(0, 0, 1)$ : trois pivots.

Pour la copie : non, « deux à deux non colinéaires » ne suffisait pas : les trois vecteurs sont dans un même **plan** par l'origine ($\operatorname{Vect}(\mathbf{v}_1, \mathbf{v}_2)$), et $\mathbf{v}_3$ combine les deux autres. Trois vecteurs liés de $\mathbb{R}^3$ sont dans un même plan (ou une même droite).

**Erreurs fréquentes.** Conclure « libre » parce qu'aucun vecteur n'est multiple d'un autre ; lire la relation dans une forme échelonnée non réduite ; un signe en d).

**Variante.** $(\mathbf{v}_1, \mathbf{v}_2, \mathbf{e}_3)$ est-elle libre ? *Réponse* : oui : $a\mathbf{v}_1 + b\mathbf{v}_2 = (a, 2a + b, -a + 3b) = (0, 0, 1)$ imposerait $a = 0$, puis $b = 0$, puis $0 = 1$.

### Ex M12a.4 — Extraire une base d'une famille génératrice, compléter une famille libre

**Réponses** : a) `3` · b) `[1, 3, 5]` · c) `[1, 1]` · d) `2` · e) `[1, -2]` · f) `2`.

**Démarche.**
- a) et b) $\mathbf{a}_2 = 2\mathbf{a}_1$ (pas de pivot), $\mathbf{a}_3$ n'est pas un multiple de $\mathbf{a}_1$ (pivot), $\mathbf{a}_4 = \mathbf{a}_1 + \mathbf{a}_3$ (pas de pivot), $\mathbf{a}_5$ n'est pas dans le plan $\operatorname{Vect}(\mathbf{a}_1, \mathbf{a}_3)$ : $x\mathbf{a}_1 + y\mathbf{a}_3 = (x, y, 2x + y)$ vaudrait $(1, -1, 1)$, pas $(1, -1, 0)$ (pivot). Forme réduite : $\begin{pmatrix} 1 & 2 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix}$.
- c) La quatrième colonne de la forme réduite, $(1, 1, 0)$ : $\mathbf{a}_4 = \mathbf{a}_1 + \mathbf{a}_3$.
- d) $\operatorname{Vect}(\mathbf{a}_1, \ldots, \mathbf{a}_4) = \operatorname{Vect}(\mathbf{a}_1, \mathbf{a}_3)$ : un plan.
- e) $\alpha = 1$ (première coordonnée), $2 + \beta = 0$, $\beta = -2$ ; vérification : $-2 + 2 = 0$.
- f) Par e), $\mathbf{e}_1 = \mathbf{u} - 2\mathbf{v}$ est dans le plan $\operatorname{Vect}(\mathbf{u}, \mathbf{v})$, donc $(\mathbf{u}, \mathbf{v}, \mathbf{e}_1)$ est liée ; $\mathbf{e}_2$ n'y est pas : $\alpha\mathbf{u} + \beta\mathbf{v} = (\alpha, 2\alpha + \beta, -2\alpha - \beta) = (0, 1, 0)$ imposerait $\alpha = 0$, $\beta = 1$, puis $-1 = 0$.

Pour la copie : $(\mathbf{a}_1, \mathbf{a}_3, \mathbf{a}_5)$ est libre (trois pivots) et a $3 = \dim\mathbb{R}^3$ vecteurs : c'est une base de $\mathbb{R}^3$, sans qu'il faille vérifier qu'elle engendre (fiche §3). e) montre que $\mathbf{e}_1$ est déjà dans le plan engendré par $\mathbf{u}$ et $\mathbf{v}$ : il n'ajoute aucune direction, et f) commence donc à $\mathbf{e}_2$.

**Erreurs fréquentes.** Numéroter les colonnes à partir de 0 ; garder les premières colonnes au lieu des colonnes à pivot ; répondre $d = 4$ en comptant les vecteurs ; compléter par $\mathbf{e}_1$ sans vérifier.

**Variante.** Avec quel vecteur de la base canonique compléter $(\mathbf{a}_1, \mathbf{a}_3)$ ? *Réponse* : $\mathbf{e}_1$ convient : $x\mathbf{a}_1 + y\mathbf{a}_3 = (x, y, 2x + y) = (1, 0, 0)$ imposerait $2 = 0$.

### Ex M12a.5 — Les coordonnées d'un vecteur dans une base qui n'est pas la base canonique

**Réponses** : a) `[-2, 3, 1]` · b) `[1, 0, 3]` · c) `[0.5, 0.5, -0.5]` · d) `[2, 3]` · e) `False` · f) `[1, -2, 3]`.

**Démarche.**
- a) $c_1 + c_2 = 1$, $c_2 + c_3 = 4$, $c_1 + c_3 = -1$. En additionnant, $2(c_1 + c_2 + c_3) = 4$, donc $c_1 + c_2 + c_3 = 2$, puis $c_3 = 2 - 1 = 1$, $c_1 = 2 - 4 = -2$, $c_2 = 2 - (-1) = 3$. Vérification : $-2(1, 0, 1) + 3(1, 1, 0) + (0, 1, 1) = (1, 4, -1)$.
- b) $2\mathbf{b}_1 - \mathbf{b}_2 + \mathbf{b}_3 = (2 - 1 + 0,\ 0 - 1 + 1,\ 2 - 0 + 1) = (1, 0, 3)$.
- c) Même méthode avec $(1, 0, 0)$ : la somme vaut $\frac{1}{2}$, d'où $c_3 = -\frac{1}{2}$, $c_1 = \frac{1}{2}$, $c_2 = \frac{1}{2}$.
- d) $\alpha\mathbf{p}_1 + \beta\mathbf{p}_2 = (\alpha, 2\alpha + \beta, -\beta) = (2, 7, -3)$ : $\alpha = 2$, $\beta = 3$, et la deuxième se vérifie, $4 + 3 = 7$.
- e) $\alpha = 3$, $\beta = 0$, mais $2\alpha + \beta = 6 \ne 1$.
- f) Les mêmes nombres, dans l'ordre de la nouvelle base : $c_3$, puis $c_1$, puis $c_2$.

Pour la copie : la matrice $[\mathbf{b}_1\ \mathbf{b}_2\ \mathbf{b}_3]$ a trois pivots (le pivot de Gauss le montre ; M12c dira que son déterminant vaut 2) : c'est une base. La matrice dont les colonnes sont les coordonnées de $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$ est $\mathbf{B}^{-1}$, puisque $\mathbf{B}\mathbf{B}^{-1} = \mathbf{I}$.

**Erreurs fréquentes.** Résoudre $\mathbf{B}^\top\mathbf{c} = \mathbf{v}$ (en rangeant les vecteurs de base en lignes) : on trouve $(3, 1, -2)$ en a) ; confondre a) et b) (coordonnées → vecteur, ou vecteur → coordonnées) ; en f), garder l'ordre de a).

**Variante.** Les coordonnées de $(2, 2, 2)$ dans la base $(\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3)$ ? *Réponse* : $(1, 1, 1)$.

### Ex M12a.6 — Le rang par les colonnes et par les lignes, celui d'un produit, et celui d'un tableau centré

**Réponses** : a) `2` · b) `2` · c) `2` · d) `3` · e) `1` · f) `3` · g) `2`.

**Démarche.**
- a) La ligne 3 est la somme des lignes 1 et 2, et les lignes 1 et 2 ne sont pas proportionnelles : rang 2. Côté colonnes : $\mathbf{a}_2 = 2\mathbf{a}_1$, et la forme réduite $\begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ a deux pivots.
- b) $\operatorname{rg}(\mathbf{A}^\top) = \operatorname{rg}(\mathbf{A})$.
- c) $\operatorname{rg}(\mathbf{A}^\top\mathbf{A}) = \operatorname{rg}(\mathbf{A})$ (fiche §4 et §6), même si $\mathbf{A}^\top\mathbf{A}$ a la forme $(4, 4)$.
- d) Les deux premières colonnes de $\mathbf{C}$, $(-2, 1, 0, 0)$ et $(1, 0, -3, 1)$, ne sont pas proportionnelles, et la troisième, $(1, 0, 0, 0)$, n'est pas dans leur plan (sa dernière coordonnée est nulle, ce qui forcerait le coefficient de la deuxième à 0, puis celui de la première à 0 par la deuxième coordonnée). Trois pivots.
- e) Les deux premières colonnes de $\mathbf{C}$ sont dans le noyau de $\mathbf{A}$ : $\mathbf{A}(-2, 1, 0, 0) = -2\mathbf{a}_1 + \mathbf{a}_2 = \mathbf{0}$, et $\mathbf{A}(1, 0, -3, 1) = \mathbf{a}_1 - 3\mathbf{a}_3 + \mathbf{a}_4 = (1 - 0 - 1,\ 2 - 3 + 1,\ 3 - 3 + 0) = \mathbf{0}$. Donc $\mathbf{A}\mathbf{C} = [\mathbf{0}\ \ \mathbf{0}\ \ \mathbf{a}_1]$, de rang 1, sous la borne $\min(2, 3) = 2$.
- f) Le pivot de Gauss donne trois pivots (M12c dira que le déterminant vaut 33, non nul).
- g) Les moyennes des colonnes sont $(3, 1, 3)$ ; $\mathbf{X}_c = \begin{pmatrix} -1 & 0 & 2 \\ 1 & -1 & 0 \\ 0 & 1 & -2 \end{pmatrix}$, dont la troisième ligne est l'opposée de la somme des deux autres, et les deux premières ne sont pas proportionnelles : rang 2.

Pour la copie : $L_3 = L_1 + L_2$. Pour un tableau centré de $n$ exemples, la somme des $n$ lignes est nulle (chaque colonne a une moyenne nulle) : les lignes sont liées, $\operatorname{rg}(\mathbf{X}_c) \le n - 1$ ; centrer a fait perdre un rang au tableau de f).

**Erreurs fréquentes.** Prendre la borne $\min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{C}) = 2$ pour la valeur de e) ; répondre 4 en c), la taille de $\mathbf{A}^\top\mathbf{A}$ ; centrer les lignes au lieu des colonnes.

**Variante.** Le rang du tableau centré d'un tableau de 4 exemples dont les quatre lignes sont égales ? *Réponse* : 0 : chaque ligne est égale à la moyenne, et le tableau centré est nul.

### Ex M12a.7 — La matrice d'une application linéaire : les images des vecteurs de base

**Réponses** : a) `[[1, -2, 1], [3, 0, 1]]` · b) `[-2, 0]` · c) `[-1, 5]` · d) `[2, 5]` · e) `[[2, 1], [-1, 2]]` · f) `[[0.5, 0.5], [0.5, 0.5]]` · g) `False`.

**Démarche.**
- a) $f(\mathbf{e}_1) = (1, 3)$, $f(\mathbf{e}_2) = (-2, 0)$, $f(\mathbf{e}_3) = (1, 1)$, rangés en colonnes : une matrice de forme $(2, 3)$.
- b) La deuxième colonne.
- c) $(2 - 2 - 1,\ 6 - 1) = (-1, 5)$.
- d) $(2, 5)$ : 2 lignes pour l'arrivée, 5 colonnes pour le départ.
- e) $\mathbf{e}_1 = \frac{1}{2}\big((1, 1) + (1, -1)\big)$ et $\mathbf{e}_2 = \frac{1}{2}\big((1, 1) - (1, -1)\big)$, donc, par linéarité, $g(\mathbf{e}_1) = \frac{1}{2}\big((3, 1) + (1, -3)\big) = (2, -1)$ et $g(\mathbf{e}_2) = \frac{1}{2}\big((3, 1) - (1, -3)\big) = (1, 2)$.
- f) La projection sur la droite dirigée par $\mathbf{u} = (1, 1)$ (M07 §4) : $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert^2}\,\mathbf{u}$ ; pour $\mathbf{e}_1$ et pour $\mathbf{e}_2$, $\frac{1}{2}(1, 1)$.
- g) $h(0, 0) = (0, 1) \ne \mathbf{0}$.

Pour la copie : la projection garde $(1, 1)$, qui est sur la droite, et envoie $(1, -1)$, perpendiculaire, sur $\mathbf{0}$.

**Erreurs fréquentes.** Ranger $f(\mathbf{e}_j)$ en lignes (on obtient la transposée, de forme $(3, 2)$) ; en e), prendre $g(1, 1)$ et $g(1, -1)$ pour les colonnes ; en d), $(5, 2)$.

**Variante.** La matrice de la projection orthogonale sur l'axe des ordonnées ? *Réponse* : $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.

### Ex M12a.8 — Composer deux applications du plan, c'est multiplier leurs matrices

**Réponses** : a) `[[3, 2], [0, 1]]` · b) `[[3, 6], [0, 1]]` · c) `[5, 1]` · d) `False` · e) `[[1, 4], [0, 1]]` · f) `[[1, -2], [0, 1]]` · g) `[[0.3333, -2], [0, 1]]`.

**Démarche.** $\mathbf{A} = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$, $\mathbf{B} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
- a) « $a$, puis $b$ » : $\mathbf{B}\mathbf{A} = \begin{pmatrix} 3 & 2 \\ 0 & 1 \end{pmatrix}$.
- b) $\mathbf{A}\mathbf{B} = \begin{pmatrix} 3 & 6 \\ 0 & 1 \end{pmatrix}$.
- c) $a(1, 1) = (3, 1)$, puis $b(3, 1) = (3 + 2, 1) = (5, 1)$.
- d) Les deux matrices diffèrent.
- e) Deux cisaillements de 2 font un cisaillement de 4.
- f) Défaire $(x, y) \mapsto (x + 2y, y)$ : $(u, v) \mapsto (u - 2v, v)$.
- g) $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} \frac{1}{3} & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{3} & -2 \\ 0 & 1 \end{pmatrix}$.

Pour la copie : $(b \circ a)(\mathbf{x}) = \mathbf{B}(\mathbf{A}\mathbf{x}) = (\mathbf{B}\mathbf{A})\mathbf{x}$ : la matrice appliquée en premier est la plus proche de $\mathbf{x}$, à droite. $b^{-1}$ cisaille dans l'autre sens : il déplace chaque point horizontalement de $-2$ fois son ordonnée.

**Erreurs fréquentes.** Écrire $\mathbf{A}\mathbf{B}$ pour « $a$ puis $b$ » ; en g), $\mathbf{A}^{-1}\mathbf{B}^{-1} = \begin{pmatrix} \frac{1}{3} & -\frac{2}{3} \\ 0 & 1 \end{pmatrix}$.

**Variante.** $(a \circ b)(1, 1)$ ? *Réponse* : $b(1, 1) = (3, 1)$, puis $a(3, 1) = (9, 1)$.

### Ex M12a.9 — Noyau et image d'une matrice 3 × 4, et le théorème du rang

**Réponses** : a) `2` · b) `[1, 2]` · c) `2` · d) `[1, -2, 1, 0]` · e) `[-2, -1, 0, 1]` · f) `[[1, 1], [2, 1], [1, -1]]` · g) `[3, -2, 1]` · h) `True`.

**Démarche.**
- a) et b) $L_2 \leftarrow L_2 - 2L_1$ et $L_3 \leftarrow L_3 - L_1$ donnent $(0, -1, -2, -1)$ et $(0, -2, -4, -2)$, proportionnelles : la troisième s'annule. Puis $L_2 \leftarrow -L_2$ et $L_1 \leftarrow L_1 - L_2$ : forme réduite $\begin{pmatrix} 1 & 0 & -1 & 2 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$, pivots dans les colonnes 1 et 2.
- c) $4 - 2 = 2$.
- d) $x_3 = 1$, $x_4 = 0$ : $x_1 = -R_{13} = 1$, $x_2 = -R_{23} = -2$.
- e) $x_3 = 0$, $x_4 = 1$ : $x_1 = -2$, $x_2 = -1$.
- f) Les colonnes 1 et 2 de $\mathbf{A}$ : $(1, 2, 1)$ et $(1, 1, -1)$.
- g) $a + 2b + 1 = 0$ et $a + b - 1 = 0$ : $b = -2$, $a = 3$.
- h) $3 \times 2 - 2 \times 1 + 1 \times (-4) = 0$.

Pour la copie : d) dit $\mathbf{a}_1 - 2\mathbf{a}_2 + \mathbf{a}_3 = \mathbf{0}$, soit $\mathbf{a}_3 = 2\mathbf{a}_2 - \mathbf{a}_1$ ; e) dit $\mathbf{a}_4 = 2\mathbf{a}_1 + \mathbf{a}_2$. $2 + 2 = 4$ colonnes : le théorème du rang. $\mathbf{A}$ n'est ni injective (noyau de dimension 2) ni surjective (image de dimension 2 dans $\mathbb{R}^3$).

**Erreurs fréquentes.** Le signe de $-R_{ij}$ ; prendre les colonnes de la forme réduite pour f), ou écrire cette base vecteur par vecteur, en lignes (la transposée) ; chercher le noyau dans $\mathbb{R}^3$.

**Variante.** La solution de $\mathbf{A}\mathbf{x} = (2, 1, -4)$ de la forme $(s, t, 0, 0)$ ? *Réponse* : $s(1, 2, 1) + t(1, 1, -1) = (2, 1, -4)$ donne $s = -1$, $t = 3$ : $(-1, 3, 0, 0)$.

### Ex M12a.10 — Toutes les solutions de A x = b : une solution particulière plus le noyau

**Réponses** : a) `[4, -1, 0, 0]` · b) `2` · c) `[-2, 1, 1, 0]` · d) `[1, -3, 0, 1]` · e) `[-1, 4, 2, -1]` · f) `True` · g) `3` · h) `0`.

**Démarche.** La ligne 3 de $[\mathbf{A} \mid \mathbf{b}]$ est la somme des deux autres ($1 + 0 = 1$, …, $4 - 1 = 3$) : elle s'annule, et la forme réduite est $\left(\begin{array}{cccc|c} 1 & 0 & 2 & -1 & 4 \\ 0 & 1 & -1 & 3 & -1 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right)$.
- a) $x_3 = x_4 = 0$ : $x_1 = 4$, $x_2 = -1$.
- b) Deux variables libres, $x_3$ et $x_4$.
- c) et d) $x_p = -R_{ij}$ : $(-2, 1, 1, 0)$ et $(1, -3, 0, 1)$.
- e) $\mathbf{x}_p + 2\mathbf{k}_1 - \mathbf{k}_2 = (4 - 4 - 1,\ -1 + 2 + 3,\ 2,\ -1)$.
- f) $\mathbf{A}(2, 0, 1, 0) = (2 + 2,\ 0 - 1,\ 2 + 1) = (4, -1, 3)$.
- g) La troisième ligne de $\mathbf{A}$ est la somme des deux autres : il faut $c = 4 + (-1)$.
- h) $5 \ne 3$ : $\mathbf{b}$ n'est pas dans l'image, aucune solution.

Pour la copie : les solutions sont $(4, -1, 0, 0) + s\,(-2, 1, 1, 0) + t\,(1, -3, 0, 1)$. f) est $\mathbf{x}_p + \mathbf{k}_1$ ($s = 1$, $t = 0$) : une autre solution particulière ; n'importe laquelle convient pour décrire l'ensemble. g) : la ligne 3 de $\mathbf{A}$ est la somme des deux autres, donc $c$ doit être la somme des deux premiers nombres du second membre.

**Erreurs fréquentes.** Oublier la solution particulière en e) ; répondre « une infinité » en h) parce qu'il y a des variables libres (il faut d'abord que le système soit compatible) ; un signe dans le noyau.

**Variante.** La solution telle que $x_3 = x_4 = 1$ ? *Réponse* : $\mathbf{x}_p + \mathbf{k}_1 + \mathbf{k}_2 = (3, -3, 1, 1)$.

### Ex M12a.11 — Une base adaptée qui rend diagonale la matrice d'une application : S⁻¹AS

**Réponses** : a) `[2, 2]` · b) `[6, 3]` · c) `[[-1, 2], [1, -1]]` · d) `[[2, 0], [0, 3]]` · e) `[1, 2]` · f) `[2, 6]` · g) `[14, 8]` · h) `[[3, 0], [0, 2]]`.

**Démarche.**
- a) $(4 - 2,\ 1 + 1) = (2, 2) = 2\,\mathbf{s}_1$.
- b) $(8 - 2,\ 2 + 1) = (6, 3) = 3\,\mathbf{s}_2$.
- c) $\det\mathbf{S} = 1 - 2 = -1$ : $\mathbf{S}^{-1} = \frac{1}{-1}\begin{pmatrix} 1 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$.
- d) Colonne $j$ : les coordonnées de $\mathbf{A}\mathbf{s}_j$, soit $(2, 0)$ et $(0, 3)$ par a) et b). Par le calcul : $\mathbf{A}\mathbf{S} = \begin{pmatrix} 2 & 6 \\ 2 & 3 \end{pmatrix}$, puis $\mathbf{S}^{-1}\mathbf{A}\mathbf{S} = \begin{pmatrix} -2 + 4 & -6 + 6 \\ 2 - 2 & 6 - 3 \end{pmatrix}$.
- e) $\mathbf{S}^{-1}(5, 3) = (-5 + 6,\ 5 - 3) = (1, 2)$.
- f) $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}(1, 2) = (2, 6)$.
- g) $\mathbf{S}(2, 6) = (2 + 12,\ 2 + 6)$.
- h) Les vecteurs de base échangés : les nombres de la diagonale aussi.

Pour la copie : $\mathbf{A}$ ne fait que multiplier $\mathbf{s}_1$ par 2 et $\mathbf{s}_2$ par 3 ; dans la base $(\mathbf{s}_1, \mathbf{s}_2)$, sa matrice est diagonale. $\mathbf{A}\mathbf{x} = (20 - 6,\ 5 + 3) = (14, 8)$. Appliquer $\mathbf{A}$ dix fois : en coordonnées, $(2^{10} \times 1,\ 3^{10} \times 2)$, puis on revient par $\mathbf{S}$. M12c fera de cette idée une méthode.

**Erreurs fréquentes.** $\mathbf{S}\mathbf{A}\mathbf{S}^{-1}$ au lieu de $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ ; oublier le signe du déterminant dans c) ; $\mathbf{S}\mathbf{x}$ au lieu de $\mathbf{S}^{-1}\mathbf{x}$ en e) ; rendre f) comme réponse de g).

**Variante.** $\mathbf{A}^2\mathbf{x}$ par la nouvelle base ? *Réponse* : coordonnées $(4 \times 1,\ 9 \times 2) = (4, 18)$, puis $\mathbf{S}(4, 18) = (40, 22)$ ; et directement, $\mathbf{A}(14, 8) = (56 - 16,\ 14 + 8)$.

### Ex M12a.12 — Une application affine du plan : partie linéaire, translation, inverse

**Réponses** : a) `[[2, 3], [1, 2]]` · b) `[-1, 4]` · c) `[-2, 3]` · d) `[[2, -3], [-1, 2]]` · e) `[14, -9]` · f) `[8, -4]` · g) `[4, 7]` · h) `False`.

**Démarche.**
- a) et b) $\varphi(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}$ avec les coefficients de $x$ et $y$ dans $\mathbf{A}$, et $\mathbf{b} = \varphi(0, 0)$.
- c) $(2 - 3 - 1,\ 1 - 2 + 4)$.
- d) $\det\mathbf{A} = 4 - 3 = 1$ : $\mathbf{A}^{-1} = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$.
- e) $-\mathbf{A}^{-1}\mathbf{b} = -\big(2 \times (-1) - 3 \times 4,\ -1 \times (-1) + 2 \times 4\big) = -(-14, 9) = (14, -9)$.
- f) $\mathbf{A}^{-1}\big((3, 4) - (-1, 4)\big) = \mathbf{A}^{-1}(4, 0) = (8, -4)$.
- g) $(2 + 3 - 1,\ 1 + 2 + 4)$.
- h) $\varphi(0, 0) = (-1, 4) \ne \mathbf{0}$.

Pour la copie : $\varphi(8, -4) = (16 - 12 - 1,\ 8 - 8 + 4) = (3, 4)$. $\varphi(0, 0) = (-1, 4)$ et $\varphi(2, 2) = (9, 10)$ ont pour milieu $(4, 7) = \varphi(1, 1)$ : une application affine conserve les milieux (les combinaisons affines, fiche §8).

**Erreurs fréquentes.** $\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}\mathbf{y} - \mathbf{b}$ (en f) : $(-5, 1)$) ; une translation de $\varphi^{-1}$ égale à $-\mathbf{b}$ (en e) : $(1, -4)$) ; un signe dans $\mathbf{b}$.

**Variante.** $\varphi^{-1}(0, 0)$ ? *Réponse* : $\mathbf{A}^{-1}(1, -4) = (14, -9)$ : la translation de $\varphi^{-1}$, comme toujours pour l'image de $\mathbf{0}$.

### Ex M12a.13 — La dérivation sur les polynômes de degré au plus 3 : matrice, noyau, image

**Réponses** : a) `[[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]]` · b) `[2, -1, 4, 1]` · c) `[-1, 8, 3, 0]` · d) `3` · e) `1` · f) `False` · g) `[[0, 0, 2, 0], [0, 0, 0, 6], [0, 0, 0, 0], [0, 0, 0, 0]]` · h) `4`.

**Démarche.**
- a) $D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$, $D(x^3) = 3x^2$ : leurs coordonnées $(0, 0, 0, 0)$, $(1, 0, 0, 0)$, $(0, 2, 0, 0)$, $(0, 0, 3, 0)$ en colonnes.
- c) $P' = -1 + 8x + 3x^2$ ; et la matrice fois $(2, -1, 4, 1)$ donne $(-1, 8, 3, 0)$.
- d) Trois colonnes non nulles, chacune avec un pivot dans une ligne différente.
- e) $4 - 3 = 1$ : les polynômes constants.
- f) Les dérivées sont de degré au plus 2.
- g) Le carré de la matrice : $D^2(x^2) = 2$, $D^2(x^3) = 6x$.
- h) $D^3(x^3) = 6 \ne 0$, $D^4 = 0$.

Pour la copie : $\ker D$ = les constantes, $\operatorname{Im} D = \mathbb{R}_2[x]$ ; $1 + 3 = 4$. $D$ n'est pas inversible, car pas injective : $P$ et $P + 5$ ont la même dérivée. « Prendre une primitive » ne défait $D$ qu'à une constante près : il faut choisir laquelle, et l'information perdue est exactement le noyau.

**Erreurs fréquentes.** Ranger les dérivées en lignes (la transposée) ; mettre le coefficient de $x^3$ en premier ; répondre 4 en d) (la taille).

**Variante.** La matrice de $P \mapsto xP'(x)$ ? *Réponse* : $1 \mapsto 0$, $x \mapsto x$, $x^2 \mapsto 2x^2$, $x^3 \mapsto 3x^3$ : la matrice diagonale $\operatorname{diag}(0, 1, 2, 3)$, de rang 3.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12a.14 — L'intersection de deux sous-espaces en est un ; la réunion, presque jamais

**Réponse modèle.**
1. $\mathbf{0} \in U$ et $\mathbf{0} \in W$, donc $\mathbf{0} \in U \cap W$. Si $\mathbf{x}, \mathbf{y} \in U \cap W$ et $\lambda, \mu \in \mathbb{R}$ : $\lambda\mathbf{x} + \mu\mathbf{y} \in U$ ($U$ est un sous-espace) et $\in W$ (de même), donc $\in U \cap W$.
2. $x = z$ et $x + y + z = 0$ donnent $y = -2x$ : les vecteurs $x\,(1, -2, 1)$. L'intersection est la droite $\operatorname{Vect}\big((1, -2, 1)\big)$.
3. Si $U \subseteq W$, alors $U \cup W = W$, un sous-espace ; de même si $W \subseteq U$.
4. Supposons $\mathbf{u} + \mathbf{w} \in U \cup W$. S'il est dans $U$, alors $\mathbf{w} = (\mathbf{u} + \mathbf{w}) - \mathbf{u} \in U$ (différence de deux vecteurs de $U$) : contradiction. S'il est dans $W$, alors $\mathbf{u} = (\mathbf{u} + \mathbf{w}) - \mathbf{w} \in W$ : contradiction. Donc $\mathbf{u} + \mathbf{w} \notin U \cup W$, et $U \cup W$ n'est pas stable par addition. Conclusion : $U \cup W$ est un sous-espace **si et seulement si** l'un des deux contient l'autre.
5. Aucun des deux axes ne contient l'autre : avec $\mathbf{u} = (1, 0)$ et $\mathbf{w} = (0, 1)$, $(1, 1)$ n'est sur aucun axe.

**Grille.** (1) les trois conditions, chacune justifiée par les deux sous-espaces ; (2) le système résolu et un vecteur directeur ; (3) l'inclusion qui ramène la réunion à l'un des deux ; (4) les deux cas de l'absurde, chacun avec une différence de deux vecteurs du même sous-espace, et la conclusion « si et seulement si » ; (5) l'application avec deux vecteurs précis.

### Ex M12a.15 — Les coordonnées dans une base sont uniques

**Réponse modèle.**
1. $\sum_i c_i\mathbf{b}_i - \sum_i d_i\mathbf{b}_i = \sum_i (c_i - d_i)\,\mathbf{b}_i = \mathbf{0}$. La famille est libre : tous les coefficients sont nuls, $c_i = d_i$.
2. Le vecteur $\mathbf{0}$ s'écrit $0\,\mathbf{b}_1 + \cdots + 0\,\mathbf{b}_n$. Si $\lambda_1\mathbf{b}_1 + \cdots + \lambda_n\mathbf{b}_n = \mathbf{0}$, c'est une autre écriture de $\mathbf{0}$ ; par unicité, tous les $\lambda_i$ sont nuls : la famille est libre.
3. $\mathbf{v} = \sum_i c_i(\mathbf{v})\,\mathbf{b}_i$ et $\mathbf{w} = \sum_i c_i(\mathbf{w})\,\mathbf{b}_i$, donc $\lambda\mathbf{v} + \mu\mathbf{w} = \sum_i \big(\lambda c_i(\mathbf{v}) + \mu c_i(\mathbf{w})\big)\,\mathbf{b}_i$ : c'est une écriture de $\lambda\mathbf{v} + \mu\mathbf{w}$ dans la base, donc **la** sienne, par unicité.
4. $\mathbf{u}_3 = 0\,\mathbf{u}_1 + 0\,\mathbf{u}_2 + 1\,\mathbf{u}_3$ et $\mathbf{u}_3 = -2\,\mathbf{u}_1 + \mathbf{u}_2 + 0\,\mathbf{u}_3$. La question 2 : une famille où un vecteur a une seule écriture est libre ; celle-ci est liée, donc certaines écritures ne peuvent pas être uniques.

**Grille.** (1) la différence des deux écritures, la libre famille invoquée ; (2) l'écriture triviale de $\mathbf{0}$, et l'unicité appliquée à $\mathbf{0}$ ; (3) l'écriture de la combinaison, et l'unicité pour conclure (pas seulement « c'est linéaire ») ; (4) deux écritures différentes vérifiées, et le lien avec la question 2.

### Ex M12a.16 — Le noyau est un sous-espace, et une application linéaire est injective si et seulement si son noyau est {0}

**Réponse modèle.**
1. $f(\mathbf{0}) = f(0 \cdot \mathbf{0}) = 0 \cdot f(\mathbf{0}) = \mathbf{0}$ (ou : $f(\mathbf{0}) = f(\mathbf{0} + \mathbf{0}) = 2f(\mathbf{0})$).
2. $\mathbf{0} \in \ker f$ par 1. Si $f(\mathbf{x}) = f(\mathbf{y}) = \mathbf{0}$, alors $f(\lambda\mathbf{x} + \mu\mathbf{y}) = \lambda f(\mathbf{x}) + \mu f(\mathbf{y}) = \mathbf{0}$.
3. $\mathbf{0} = f(\mathbf{0}) \in \operatorname{Im} f$. Si $\mathbf{y} = f(\mathbf{x})$ et $\mathbf{y}' = f(\mathbf{x}')$, alors $\lambda\mathbf{y} + \mu\mathbf{y}' = f(\lambda\mathbf{x} + \mu\mathbf{x}') \in \operatorname{Im} f$.
4. Si $\mathbf{x} \in \ker f$, alors $f(\mathbf{x}) = \mathbf{0} = f(\mathbf{0})$, et l'injectivité donne $\mathbf{x} = \mathbf{0}$.
5. Si $f(\mathbf{x}) = f(\mathbf{y})$, alors $f(\mathbf{x} - \mathbf{y}) = \mathbf{0}$, donc $\mathbf{x} - \mathbf{y} \in \ker f = \{\mathbf{0}\}$, et $\mathbf{x} = \mathbf{y}$.
6. $\mathbf{A}\mathbf{x} = \mathbf{0}$ a $n$ inconnues et au plus $m < n$ pivots : il reste au moins $n - m \ge 1$ variable libre, d'où une solution non nulle (une variable libre à 1). Le noyau n'est pas $\{\mathbf{0}\}$, et par 4, $\mathbf{A}$ n'est pas injective.

**Grille.** (1) un calcul qui utilise la linéarité ; (2) et (3) les trois conditions de sous-espace, l'espace où chacun vit ; (4) le recours à $f(\mathbf{0}) = \mathbf{0}$ ; (5) le passage par $\mathbf{x} - \mathbf{y}$ ; (6) le comptage des pivots et la variable libre.

### Ex M12a.17 — Le théorème du rang : dim ker + rang = nombre de colonnes

**Réponse modèle.**
1. $\mathbf{R}$ s'obtient par des opérations élémentaires sur les lignes, qui ne changent pas les solutions (M09a §6) ; ici le second membre est $\mathbf{0}$ et le reste.
2. La ligne $i$ de $\mathbf{R}$ (une ligne à pivot, de pivot dans la colonne $p_i$) a un 1 en $p_i$, des 0 dans les autres colonnes à pivot, et des nombres $R_{ij'}$ dans les colonnes libres $j'$. Donc $(\mathbf{R}\mathbf{k}_j)_i = 1 \times (\mathbf{k}_j)_{p_i} + \sum_{j' \text{ libre}} R_{ij'}\,(\mathbf{k}_j)_{j'} = -R_{ij} + R_{ij} \times 1 = 0$ (seule la colonne libre $j$ a une coordonnée non nulle). Les lignes nulles de $\mathbf{R}$ donnent 0. Par 1, $\mathbf{k}_j \in \ker\mathbf{A}$.
3. Si $\sum_j \lambda_j\mathbf{k}_j = \mathbf{0}$, regardons la coordonnée d'une colonne libre $j_0$ : seul $\mathbf{k}_{j_0}$ y a un 1, les autres un 0 ; elle vaut donc $\lambda_{j_0} = 0$. Tous les $\lambda_j$ sont nuls.
4. Dans chaque colonne libre $j_0$, $\mathbf{y}$ a pour coordonnée $x_{j_0} - x_{j_0} \times 1 = 0$. $\mathbf{y} \in \ker\mathbf{A}$ (différence de vecteurs du noyau), donc $\mathbf{R}\mathbf{y} = \mathbf{0}$ ; la ligne $i$ donne $y_{p_i} + \sum_{j' \text{ libre}} R_{ij'}\,y_{j'} = y_{p_i} = 0$. Toutes les coordonnées de $\mathbf{y}$ sont nulles : $\mathbf{x} = \sum_j x_j\,\mathbf{k}_j$.
5. Les $\mathbf{k}_j$ forment une base de $\ker\mathbf{A}$ ; il y en a un par colonne libre, soit $n - r$, et $r = \operatorname{rg}(\mathbf{A})$.
6. Pour $\mathbf{A}$ carrée de taille $n$ : injective $\iff$ $\dim\ker = 0$ $\iff$ $\operatorname{rg} = n$ $\iff$ $\operatorname{Im}\mathbf{A} = \mathbb{R}^n$ (un sous-espace de dimension $n$ de $\mathbb{R}^n$ est $\mathbb{R}^n$) $\iff$ surjective.

**Grille.** (1) l'invariance des solutions par les opérations élémentaires ; (2) le calcul de la ligne $i$, avec les rôles des colonnes à pivot et libres ; (3) la lecture des coordonnées libres ; (4) les deux temps (coordonnées libres nulles, puis coordonnées de base nulles par $\mathbf{R}\mathbf{y} = \mathbf{0}$) ; (5) le comptage $n - r$ ; (6) la chaîne d'équivalences, avec l'argument de dimension pour la surjectivité.

### Ex M12a.18 — rg(AB) ≤ min(rg A, rg B)

**Réponse modèle.**
1. La colonne $j$ de $\mathbf{A}\mathbf{B}$ est $\mathbf{A}\mathbf{b}_j$, un vecteur de $\operatorname{Im}\mathbf{A}$. Donc $\operatorname{Im}(\mathbf{A}\mathbf{B}) \subseteq \operatorname{Im}\mathbf{A}$ (un sous-espace contient les combinaisons de ses vecteurs), et la dimension d'un sous-espace est au plus celle de l'espace qui le contient : $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \operatorname{rg}(\mathbf{A})$.
2. $\operatorname{rg}(\mathbf{A}\mathbf{B}) = \operatorname{rg}\big((\mathbf{A}\mathbf{B})^\top\big) = \operatorname{rg}(\mathbf{B}^\top\mathbf{A}^\top) \le \operatorname{rg}(\mathbf{B}^\top) = \operatorname{rg}(\mathbf{B})$, par 1 appliqué à $\mathbf{B}^\top$ et $\mathbf{A}^\top$.
3. Si $\mathbf{B}\mathbf{x} = \mathbf{0}$, alors $\mathbf{A}\mathbf{B}\mathbf{x} = \mathbf{0}$ : $\ker\mathbf{B} \subseteq \ker(\mathbf{A}\mathbf{B})$, donc $\dim\ker\mathbf{B} \le \dim\ker(\mathbf{A}\mathbf{B})$. Par le théorème du rang, $\operatorname{rg}(\mathbf{B}) = p - \dim\ker\mathbf{B} \ge p - \dim\ker(\mathbf{A}\mathbf{B}) = \operatorname{rg}(\mathbf{A}\mathbf{B})$.
4. $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \operatorname{rg}(\mathbf{B})$ par 2 ; et $\mathbf{B} = \mathbf{A}^{-1}(\mathbf{A}\mathbf{B})$ donne, par 2 encore, $\operatorname{rg}(\mathbf{B}) \le \operatorname{rg}(\mathbf{A}\mathbf{B})$.
5. Par exemple $\mathbf{A} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ et $\mathbf{B} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ : $\mathbf{A}\mathbf{B} = \mathbf{0}$, de rang 0, alors que $\min(1, 1) = 1$. La borne n'est pas toujours atteinte : l'image de $\mathbf{B}$ (l'axe des ordonnées) est ici le noyau de $\mathbf{A}$.

**Grille.** (1) la colonne $j$ de $\mathbf{A}\mathbf{B}$, l'inclusion des images, et la comparaison des dimensions ; (2) la transposition et $\operatorname{rg}(\mathbf{M}^\top) = \operatorname{rg}(\mathbf{M})$, cités ; (3) l'inclusion des noyaux, puis le théorème du rang avec le bon nombre de colonnes ; (4) les deux inégalités ; (5) un exemple **vérifié**, et l'explication par image et noyau. D'autres exemples sont justes.

### Ex M12a.19 — L'inverse d'une application affine bijective est affine

**Réponse modèle.**
1. $\varphi(\mathbf{x}) - \varphi(\mathbf{y}) = \mathbf{A}\mathbf{x} + \mathbf{b} - \mathbf{A}\mathbf{y} - \mathbf{b} = \mathbf{A}(\mathbf{x} - \mathbf{y})$ : il est nul si et seulement si $\mathbf{x} - \mathbf{y} \in \ker\mathbf{A}$. Donc $\varphi$ est injective si et seulement si $\mathbf{x} - \mathbf{y} \in \ker\mathbf{A}$ entraîne $\mathbf{x} = \mathbf{y}$, c'est-à-dire $\ker\mathbf{A} = \{\mathbf{0}\}$.
2. $\varphi(\mathbf{x}) = \mathbf{y} \iff \mathbf{A}\mathbf{x} = \mathbf{y} - \mathbf{b}$ : $\mathbf{y}$ est atteint si et seulement si $\mathbf{y} - \mathbf{b} \in \operatorname{Im}\mathbf{A}$. Tous les $\mathbf{y}$ le sont si et seulement si $\operatorname{Im}\mathbf{A} = \mathbb{R}^n$ (quand $\mathbf{y}$ parcourt $\mathbb{R}^n$, $\mathbf{y} - \mathbf{b}$ aussi).
3. $\varphi$ bijective $\iff$ $\ker\mathbf{A} = \{\mathbf{0}\}$ et $\operatorname{Im}\mathbf{A} = \mathbb{R}^n$ ; pour une matrice carrée, ces deux conditions sont équivalentes (théorème du rang, M12a.17), et équivalent à « $\mathbf{A}$ inversible » (M09a §8).
4. $\mathbf{A}\mathbf{x} + \mathbf{b} = \mathbf{y} \iff \mathbf{x} = \mathbf{A}^{-1}(\mathbf{y} - \mathbf{b}) = \mathbf{A}^{-1}\mathbf{y} + (-\mathbf{A}^{-1}\mathbf{b})$ : une application affine, de partie linéaire $\mathbf{A}^{-1}$ et de translation $-\mathbf{A}^{-1}\mathbf{b}$.
5. Si $\sum_i \lambda_i = 1$ : $\varphi\big(\sum_i \lambda_i\mathbf{x}_i\big) = \sum_i \lambda_i\mathbf{A}\mathbf{x}_i + \mathbf{b} = \sum_i \lambda_i\mathbf{A}\mathbf{x}_i + \big(\sum_i \lambda_i\big)\mathbf{b} = \sum_i \lambda_i\,\varphi(\mathbf{x}_i)$. Avec une somme $s \ne 1$, il reste $\sum_i \lambda_i\,\varphi(\mathbf{x}_i) = \varphi\big(\sum_i \lambda_i\mathbf{x}_i\big) + (s - 1)\,\mathbf{b}$, différent dès que $\mathbf{b} \ne \mathbf{0}$ : par exemple $\varphi(2\mathbf{x}) \ne 2\varphi(\mathbf{x})$.

**Grille.** (1) la différence $\varphi(\mathbf{x}) - \varphi(\mathbf{y})$ et les deux sens de l'équivalence ; (2) la réécriture $\mathbf{A}\mathbf{x} = \mathbf{y} - \mathbf{b}$ ; (3) le théorème du rang pour une matrice carrée, cité ; (4) la résolution, puis la partie linéaire et la translation nommées ; (5) le calcul avec $\sum_i \lambda_i = 1$ utilisé à l'endroit précis, et un contre-exemple.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12a.20 — Pont : une feature somme de deux autres rend XᵀX singulière, et le noyau dit laquelle

**Réponses** : a) `2` · b) `2` · c) `[-1, -1, 1]` · d) `1` · e) `[36.0, 27.5, 54.0, 30.0]` · f) `True`.

**Démarche.**
- a) La troisième colonne est la somme des deux premières, qui ne sont pas proportionnelles : rang 2.
- b) $\operatorname{rg}(\mathbf{X}^\top\mathbf{X}) = \operatorname{rg}(\mathbf{X})$.
- c) trajet + sur place − total $= 0$ : $\mathbf{X}(-1, -1, 1) = \mathbf{0}$.
- d) $\ker(\mathbf{X}^\top\mathbf{X}) = \ker\mathbf{X} = \operatorname{Vect}(\mathbf{d})$, de dimension $3 - 2 = 1$ : $\mathbf{X}^\top\mathbf{X}$, de forme $(3, 3)$ et de rang 2, est singulière.
- e) $\mathbf{w}' = (0{,}5 - 2,\ 1 - 2,\ 0 + 2) = (-1{,}5 ;\ -1 ;\ 2)$ ; première prédiction : $-18 - 30 + 84 = 36$ ; de même $(27{,}5 ;\ 54 ;\ 30)$, exactement $\mathbf{X}\mathbf{w}$.
- f) Les colonnes trajet et sur place sont libres : $\mathbf{X}^\top\mathbf{X}$, de forme $(2, 2)$, est inversible (fiche §6).

Pour la copie : $\mathbf{X}\mathbf{w}' = \mathbf{X}\mathbf{w} + 2\,\mathbf{X}\mathbf{d} = \mathbf{X}\mathbf{w}$. Les coordonnées non nulles de $\mathbf{d}$ désignent les trois features liées. $\mathbf{X}^\top\mathbf{X}$ n'est pas inversible (d). Les données ne voient que les prédictions : deux poids qui donnent les mêmes prédictions sur tous les exemples ne se distinguent pas (il faut une règle de plus : la plus petite norme, ou une pénalité ridge, workbookIA 9). Une colonne « total » chronométrée ne serait égale à la somme qu'à quelques secondes près : le rang serait 3 en exact, mais $\mathbf{X}^\top\mathbf{X}$ serait **presque** singulière, et les poids instables (M12a.31, M12d).

**Erreurs fréquentes.** $(1, 1, -1)$ et $(-1, -1, 1)$ sont tous deux dans le noyau ; la vérification demande celui dont la dernière coordonnée vaut 1. En e), oublier $\mathbf{w}$ (on trouve $\mathbf{X}(2\mathbf{d}) = \mathbf{0}$).

**Variante.** Un autre tableau a une colonne de 1 et trois colonnes indicatrices d'une équipe (matin, après-midi, nuit), avec un seul 1 par ligne parmi les trois : un vecteur de son noyau ? *Réponse* : $(1, -1, -1, -1)$ : la colonne de 1 est la somme des trois indicatrices (fiche §6).

### Ex M12a.21 — Pont : projeter sur un plan puis revenir, ce que la transformation inverse ne peut pas rendre

**Réponses** : a) `2` · b) `[-1, 1, 1]` · c) `[3, 2]` · d) `False` · e) `[[1, 0, 1], [0, 1, -1], [0, 0, 0]]` · f) `[1, 2, 0]` · g) `[-1, 1, 1]`.

**Démarche.**
- a) Deux lignes non proportionnelles.
- b) La forme réduite $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & -1 \end{pmatrix}$ ($L_1 \leftarrow L_1 - L_2$) : $x_3 = 1$, $x_1 = -1$, $x_2 = 1$.
- c) $(0 + 3,\ 3 - 1)$.
- d) $\operatorname{rg}(\mathbf{D}'\mathbf{E}) \le \operatorname{rg}(\mathbf{E}) = 2 < 3 = \operatorname{rg}(\mathbf{I}_3)$.
- e) $\mathbf{D}\mathbf{E}$, ligne par ligne : $(1, 1, 0) - (0, 1, -1)$, puis $(0, 1, -1)$, puis $\mathbf{0}$.
- f) $(0 + 0 + 1,\ 3 - 1,\ 0)$.
- g) $(0, 3, 1) - (1, 2, 0)$.

Pour la copie : $\mathbf{E}(1, 2, 0) = (3, 2)$, comme $\mathbf{E}(0, 3, 1)$ : les deux vecteurs diffèrent de $(-1, 1, 1)$, un vecteur du noyau, et l'encodeur ne peut pas les distinguer. $\mathbf{E}\mathbf{D} = \mathbf{I}_2$, donc $\mathbf{E}(\mathbf{x} - \mathbf{D}\mathbf{E}\mathbf{x}) = \mathbf{E}\mathbf{x} - \mathbf{E}\mathbf{x} = \mathbf{0}$ : l'erreur est toujours dans $\ker\mathbf{E}$. Les vecteurs reconstruits exactement sont ceux de $\operatorname{Im}\mathbf{D}$, le plan $x_3 = 0$ ; $\mathbf{D}\mathbf{E}$ projette sur ce plan parallèlement au noyau de $\mathbf{E}$. Un autre décodeur changerait le plan, jamais le fait qu'une direction est perdue.

**Erreurs fréquentes.** Calculer $\mathbf{E}\mathbf{D}$ (de forme $(2, 2)$) au lieu de $\mathbf{D}\mathbf{E}$ ; l'erreur dans le mauvais sens, $\mathbf{D}\mathbf{E}\mathbf{x} - \mathbf{x}$.

**Variante.** L'erreur de reconstruction de $(2, 1, 1)$ ? *Réponse* : $\mathbf{D}\mathbf{E}(2, 1, 1) = (3, 0, 0)$, erreur $(-1, 1, 1)$ : pour ce décodeur, l'erreur vaut toujours $x_3\,(-1, 1, 1)$.

### Ex M12a.22 — MML §2.4 et §2.5 : espaces vectoriels, sous-espaces et indépendance, en anglais

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. Un ensemble muni d'une opération qui vérifie quatre propriétés : le résultat reste dans l'ensemble (*closure*), l'opération est associative, il existe un élément neutre, et chaque élément a un inverse. Si l'opération est de plus commutative, le groupe est dit abélien. $(\mathbb{R}^n, +)$ est un groupe abélien ; les réels non nuls avec la multiplication aussi (sans le 0, qui n'a pas d'inverse).
2. L'addition des vecteurs est l'opération « intérieure » (*inner operation*), et la multiplication par un réel l'opération « extérieure » (*outer operation*, *multiplication by scalars*). Exemples : $\mathbb{R}^n$, les matrices $\mathbb{R}^{m \times n}$, les nombres complexes. Le vecteur nul est l'élément neutre de l'addition (*neutral element*, *zero vector*).
3. Une partie non vide (elle contient $\mathbf{0}$) stable par les deux opérations (*closure*). Parmi les parties de $\mathbb{R}^2$ dessinées, une seule est un sous-espace : les autres ne contiennent pas l'origine ou ne sont pas stables par addition ou par multiplication. Le livre note aussi que les solutions d'un système homogène forment un sous-espace, et celles d'un système de second membre non nul, non.
4. Une famille est libre si la seule combinaison nulle est la combinaison triviale (*trivial linear combination*). Méthode : ranger les vecteurs en colonnes, faire le pivot de Gauss ; les colonnes à pivot sont indépendantes des colonnes à leur gauche, chaque colonne sans pivot est une combinaison des colonnes à pivot à sa gauche ; la famille est libre si et seulement si toutes les colonnes sont à pivot.
5. Oui : le test de la fiche (§2) est exactement cette méthode ; « toutes les colonnes à pivot » veut dire « pas de variable libre dans $\mathbf{V}\boldsymbol{\lambda} = \mathbf{0}$ », donc « seule la combinaison triviale est nulle ».
6. Par exemple : *closure* (stabilité), *neutral element* (élément neutre), *Abelian group* (groupe commutatif), *trivial linear combination* (combinaison triviale).

**Grille.** (1) les quatre propriétés, les deux exemples tranchés ; (2) les deux opérations nommées, des exemples, le vecteur nul ; (3) les conditions et le tri des exemples, avec une raison ; (4) la définition et la méthode par les pivots ; (5) l'équivalence justifiée ; (6) trois mots traduits. Les réponses sont écrites avec tes mots, pas recopiées.

### Ex M12a.23 — MML §2.6 à §2.8 : base, rang, applications linéaires, changement de base, espaces affines

**Réponse modèle** (avec tes mots).
1. Une famille est génératrice si tout vecteur en est une combinaison ; une base est une famille génératrice minimale, ou de façon équivalente une famille libre maximale, ou une famille dans laquelle tout vecteur s'écrit d'une seule façon. Pour une base d'un sous-espace engendré : ranger les vecteurs en colonnes, chercher une forme échelonnée, garder les vecteurs des colonnes à pivot (fiche §3).
2. Le rang compte les colonnes libres, et c'est aussi le nombre de lignes libres ($\operatorname{rk}(\mathbf{A}) = \operatorname{rk}(\mathbf{A}^\top)$) ; l'espace des colonnes a pour dimension le rang ; une matrice carrée est inversible si et seulement si son rang est sa taille ; le noyau a pour dimension $n - \operatorname{rk}(\mathbf{A})$ ; une matrice est de rang plein si son rang est le plus grand possible. Énoncés aussi dans la fiche : $\operatorname{rg}(\mathbf{A}) = \operatorname{rg}(\mathbf{A}^\top)$ (§4), la dimension du noyau (§6). Non énoncé sous cette forme dans la fiche : le critère de compatibilité $\operatorname{rk}(\mathbf{A}) = \operatorname{rk}([\mathbf{A} \mid \mathbf{b}])$ (M09a §8 le donnait par les pivots).
3. La colonne $j$ de la matrice contient les coordonnées de $\Phi(\mathbf{b}_j)$ dans la base de l'arrivée : comme la fiche (§5).
4. $\mathbf{S}$ fait passer des coordonnées dans la nouvelle base du départ aux coordonnées dans l'ancienne ; $\mathbf{T}$ fait de même à l'arrivée ; la nouvelle matrice est $\mathbf{T}^{-1}\mathbf{A}\mathbf{S}$. Deux matrices sont *equivalent* s'il existe $\mathbf{S}$ et $\mathbf{T}$ inversibles avec $\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{S}$, et *similar* si l'on peut prendre $\mathbf{T} = \mathbf{S}$ (une application d'un espace dans lui-même, la même base au départ et à l'arrivée) : semblables entraîne équivalentes, pas l'inverse.
5. *Kernel* ou *null space*, *image* ou *range*, et *rank-nullity theorem* : $\dim\ker + \dim\operatorname{Im} = \dim$ du départ. Pour la matrice $\mathbf{A}$ du §4 : $2 + 2 = 4$.
6. Un sous-espace affine est un point (*support point*) plus un sous-espace vectoriel (sa direction) ; on le décrit par des équations paramétriques. Une application affine est une application linéaire suivie d'une translation ; la composée de deux applications affines est affine, et une application affine bijective conserve la structure géométrique (dimensions, parallélisme).
7. Par exemple : *ordered basis* (base ordonnée, la base avec son ordre), *transformation matrix* (matrice de l'application), *support point* (point d'appui), *rank deficient* (de rang déficient).

**Grille.** (1) les définitions et la méthode des colonnes à pivot ; (2) au moins quatre propriétés, deux retrouvées dans la fiche et une qui n'y est pas ; (3) la colonne $j$, et la comparaison ; (4) les rôles de $\mathbf{S}$ et $\mathbf{T}$, les deux mots, et le sens de l'implication ; (5) les noms et la vérification chiffrée ; (6) les deux définitions et des propriétés conservées ; (7) trois mots traduits.

### Ex M12a.24 — Fermi : les paramètres d'une application linéaire, puis affine, d'images 32 × 32 en couleurs vers 100 classes

**Réponse modèle.**
1. $32 \times 32 \times 3 = 3\,072$ nombres par image (M09a.23) : de $\mathbb{R}^{3\,072}$ dans $\mathbb{R}^{100}$, une matrice de forme $(100, 3\,072)$ (ou $(3\,072, 100)$ dans la convention des lignes, $\mathbf{x}\mathbf{W}$).
2. $3\,072 \times 100 = 307\,200 \approx 3 \times 10^5$ paramètres ; l'application affine en ajoute 100 : $307\,300$.
3. Le rang est au plus $\min(100, 3\,072) = 100$ ; le noyau a une dimension au moins $3\,072 - 100 = 2\,972$. Un vecteur du noyau est une « image » (un motif de pixels) qu'on peut ajouter à n'importe quelle image sans changer **aucun** des 100 scores : le classifieur ne voit que 100 combinaisons des pixels et ignore toutes les autres directions.
4. $3 \times 10^5 \times 4 \approx 1{,}2 \times 10^6$ octets, environ 1,2 Mo.
5. $\mathbf{B}$ de forme $(100, 16)$ et $\mathbf{C}$ de forme $(16, 3\,072)$ : $16 \times (100 + 3\,072) = 50\,752 \approx 5 \times 10^4$ paramètres, environ 6 fois moins. Le rang de $\mathbf{B}\mathbf{C}$ est au plus 16 : les 100 scores ne dépendent plus que de 16 combinaisons des pixels.

**Grille.** (1) 3 072 et la forme de la matrice ; (2) le produit, puis les biais ; (3) la borne du rang, la dimension du noyau par le théorème du rang, et son sens ; (4) la multiplication par 4 octets ; (5) le nouveau compte, le facteur, et la borne du rang d'un produit.

### Ex M12a.25 — Expliquer la dimension et le rang sans une seule formule

**Réponse modèle.**

> La dimension, c'est le nombre de directions indépendantes dans lesquelles on peut bouger : sur une route, une seule (avancer ou reculer) ; sur un terrain plat, deux ; dans un avion, trois. Une direction qu'on peut obtenir en combinant les autres n'en ajoute pas. Le rang d'un tableau, c'est le nombre de colonnes qui apportent vraiment une information nouvelle : si une colonne est le distance en kilomètres et une autre la même distance en miles, ou si une colonne est la somme de deux autres, elles ne comptent que pour une. Dire qu'un tableau de 1 000 lignes et 50 colonnes est de rang 12, c'est dire que 12 colonnes bien choisies suffisent à recalculer exactement les 38 autres. Le rang ne peut pas dépasser 50 : il n'y a que 50 colonnes ; ni 1 000, le nombre de lignes. Les 50 colonnes ne décrivent en réalité que 12 directions : beaucoup de redondance, ou une structure simple cachée.

**Grille.** (1) la dimension comme nombre de directions indépendantes, avec un exemple ; (2) le rang comme nombre de colonnes non redondantes, avec un exemple de redondance ; (3) la borne par le nombre de colonnes (et de lignes) ; (4) ce que dit « rang 12 » des 50 colonnes ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M12a.E1 — « Que veut dire qu'une matrice est de rang plein, et pourquoi s'en soucier ? »

**Réponse modèle (60 secondes).**

> Le rang d'une matrice est le nombre de ses colonnes linéairement indépendantes, et c'est aussi le nombre de ses lignes indépendantes. Il ne peut pas dépasser le plus petit des deux nombres, lignes ou colonnes ; une matrice est de rang plein quand elle atteint cette borne. Pour une matrice carrée, rang plein veut dire inversible : un système a alors une solution unique. Pour une matrice de données $\mathbf{X}$ plus haute que large, rang plein en colonnes veut dire qu'aucune feature n'est une combinaison des autres ; alors $\mathbf{X}^\top\mathbf{X}$ est inversible, et les poids d'une régression linéaire sont uniques. Sinon, par exemple avec une feature égale à la somme de deux autres, ou la même mesure en deux unités, il y a une infinité de poids qui donnent les mêmes prédictions, et l'on doit ajouter une règle, comme une pénalité ridge. Une précaution : en virgule flottante, on ne mesure qu'un rang numérique, qui dépend d'une tolérance ; une matrice de rang plein mais presque déficiente pose les mêmes problèmes en pratique, c'est le conditionnement.

**Grille.** (1) la définition par les colonnes (et les lignes), et la borne ; (2) carrée : inversible, solution unique ; (3) données : $\mathbf{X}^\top\mathbf{X}$ inversible, poids uniques ; (4) un exemple de rang déficient et sa conséquence ; (5) le rang numérique et la tolérance (ou le conditionnement).

### M12a.E2 — « Qu'est-ce que le noyau d'une matrice, et où le croise-t-on en ML ? »

**Réponse modèle (60 secondes).**

> Le noyau d'une matrice $\mathbf{A}$, c'est l'ensemble des vecteurs $\mathbf{x}$ tels que $\mathbf{A}\mathbf{x} = \mathbf{0}$ : les directions de l'espace de départ que $\mathbf{A}$ écrase. C'est un sous-espace, et sa dimension plus le rang donne le nombre de colonnes : c'est le théorème du rang. Il mesure la non-unicité : si $\mathbf{x}$ résout $\mathbf{A}\mathbf{x} = \mathbf{b}$, toutes les solutions sont $\mathbf{x}$ plus un vecteur du noyau. En machine learning, on le croise d'abord avec des features redondantes : un vecteur du noyau de la matrice des données est une combinaison de features toujours nulle, et l'on peut l'ajouter aux poids sans changer une seule prédiction. On le croise aussi dans toute réduction de dimension, une couche linéaire qui a plus d'entrées que de sorties ou une projection : ce qui tombe dans le noyau est perdu, et aucune transformation inverse ne le rend. Attention au vocabulaire : en machine learning, « noyau » désigne aussi la fonction noyau des SVM, et le filtre d'une convolution ; ce n'est pas le même objet.

**Grille.** (1) la définition, et l'espace de départ ; (2) le théorème du rang ; (3) la non-unicité des solutions ; (4) deux situations de machine learning (features redondantes, réduction de dimension ou couche plus étroite) ; (5) le piège de vocabulaire.

<a id="notebook"></a>

## Notebook

### Ex M12a.26 — Tester l'indépendance et extraire une base de l'espace des colonnes · `is_independent, column_space_basis`

**Réponses** : a) `True` · b) `False` · c) `False` · d) `[[1.0, 2.0], [0.0, 1.0], [3.0, 1.0], [2.0, -1.0]]` · e) `[[1.0], [2.0]]` · f) `"ValueError"` · g) `True`.

**Démarche.** Une fonction privée `_rref(A, tol)` : `R = np.array(A, dtype=float)` (une copie), une `ValueError` si `R.ndim != 2`, puis la boucle de M09a : pour chaque colonne, la ligne de plus grande valeur absolue à partir de la ligne courante ; si elle vaut au plus `tol`, la colonne n'a pas de pivot ; sinon échange, division par le pivot, élimination dans toutes les autres lignes, et la colonne est ajoutée à la liste des pivots. `is_independent` : `len(pivots) == M.shape[1]`, un `bool` de Python. `column_space_basis` : `M[:, list(pivots)]`, avec `M` la copie en flottants de **A** (pas `R`). Pour la copie : en b), la colonne 3 vaut $2\mathbf{a}_1 + \mathbf{a}_2$ ; c) a trois vecteurs de $\mathbb{R}^2$ ; en e), les deux premières colonnes sont nulles et n'ont pas de pivot.

**Erreurs fréquentes.** Rendre les colonnes de la forme réduite ; comparer le nombre de pivots au nombre de **lignes** ; rendre `np.True_` (le résultat d'une comparaison de NumPy) au lieu d'un `bool` ; modifier la matrice reçue (`np.asarray` ne copie pas un tableau de flottants).

### Ex M12a.27 — Une base du noyau, colonne libre par colonne libre · `null_space_basis`

**Réponses** : a) `[[1.0, -2.0], [1.0, 0.0], [0.0, 3.0], [0.0, 1.0]]` · b) `[[-2.0], [1.0]]` · c) `[3, 0]` · d) la matrice identité de taille 3 · e) `[8, 3]` · f) `True` · g) `"ValueError"`.

**Démarche.** `R, pivots = _rref(A, tol)`, `free = [j for j in range(n) if j not in pivots]`, `N = np.zeros((n, len(free)))`, puis pour chaque colonne libre `j`, d'indice `c` dans `free` : `N[j, c] = 1.0`, et pour chaque pivot `p` de la ligne `i`, `N[p, c] = -R[i, j]`. Le cas « noyau $\{\mathbf{0}\}$ » est automatique : `free` est vide et `N` a la forme $(n, 0)$. Pour la copie : a) dit $\mathbf{c}_1 + \mathbf{c}_2 = \mathbf{0}$ et $-2\mathbf{c}_1 + 3\mathbf{c}_3 + \mathbf{c}_4 = \mathbf{0}$ ; c) : l'identité est injective ; d) : la matrice nulle envoie tout sur $\mathbf{0}$, toutes les colonnes sont libres ; e) : rang 5, donc $8 - 5 = 3$.

**Erreurs fréquentes.** Oublier le signe moins ; ranger les vecteurs en lignes (forme $(n - r, n)$) ; indexer `R` par le numéro de la colonne de pivot au lieu du numéro de sa ligne ; rendre une liste vide au lieu d'un tableau $(n, 0)$.

### Ex M12a.28 — Coordonnées dans une base et changement de base · `coordinates, change_of_basis`

**Réponses** : a) `[1.0, 2.0]` · b) `[3.0, 2.0]` · c) `"ValueError"` · d) `[[3.0, 0.0], [0.0, 2.0]]` · e) `[[0.5, 1.5, 0.5], [0.5, 0.5, -0.5]]` · f) `"ValueError"`.

**Démarche.** `coordinates` : les copies, les formes (`v` à une dimension, autant de coordonnées que `B` a de lignes), `is_independent(B, tol)`, puis `c = np.linalg.solve(B.T @ B, B.T @ v)` et la vérification `np.linalg.norm(B @ c - v) <= tol * max(1.0, np.linalg.norm(v))`. `change_of_basis` : `T = S` si `T is None`, les formes $(n, n)$ et $(m, m)$, puis `is_independent(S)` et `is_independent(T)`, et enfin `np.linalg.solve(T, A @ S)`. Pour la copie : a) $(1, 1) + 2(2, 3) = (5, 7)$ ; c) : $(1, 1, 1)$ n'est pas dans le plan engendré ; d) : $\mathbf{A}(1, 0) = 3(1, 0)$ et $\mathbf{A}(1, -1) = 2(1, -1)$, d'où une matrice diagonale.

**Erreurs fréquentes.** `np.linalg.solve(B, v)`, qui refuse une matrice non carrée ; une vérification absolue (`<= tol`), qui rejette à tort un grand vecteur du sous-espace ; ne tester que `T` (une `S` singulière passe alors quand `T` est donnée) ; calculer $\mathbf{S}\mathbf{A}\mathbf{S}^{-1}$.

### Ex M12a.29 — `sympy.Matrix.nullspace`, `columnspace` et `rank` contre tes fonctions

**Réponses** : a) `2` · b) `2` · c) `[-3, 1, 0, 0]` · d) `[[1, 0], [2, 1], [-1, 2]]` · e) `True` · f) `2`.

**Démarche.** `P = sympy.Matrix(...)`, puis `P.rank()`, `len(P.nullspace())`, `list(P.nullspace()[0])`, `sympy.Matrix.hstack(*P.columnspace()).tolist()`, la comparaison `np.allclose(null_space_basis(P), np.array(sympy.Matrix.hstack(*P.nullspace()).tolist(), dtype=float))`, et `np.linalg.matrix_rank(np.array(P).T)`. Pour la copie : la forme réduite est $\begin{pmatrix} 1 & 3 & 0 & 2 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ ; le noyau dit « colonne 2 = 3 × colonne 1 » et « colonne 4 = 2 × colonne 1 − colonne 3 ». f) donne 2 comme a) : $\operatorname{rg}(\mathbf{P}^\top) = \operatorname{rg}(\mathbf{P})$.

**Erreurs fréquentes.** Mettre les vecteurs de `columnspace()` en lignes ; comparer avec `scipy.linalg.null_space`, qui rend une base orthonormée (d'autres vecteurs du même noyau).

### Ex M12a.30 — Prédire le rang : matrices aléatoires, produits, colonnes répétées

**Réponses** : a) `1` · b) `2` · c) `1` · d) `3` · e) `3`.

a) Rang 4 : une relation exacte entre des nombres tirés d'une loi continue a une probabilité nulle, et la matrice atteint $\min(4, 6)$. b) Rang 2 : $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le 2$, atteint. c) Rang 3 : la colonne ajoutée ne crée aucune direction. d) Rang 2 : trois lignes centrées de somme nulle. e) Rang 2 : la ligne $i$ vaut $i\,(1, \ldots, 1) + (1, 2, \ldots, 6)$, une combinaison de deux vecteurs fixes.

### Ex M12a.31 — Le rang numérique : une colonne presque redondante et le choix de la tolérance

**Réponses** : a) `14` · b) `11` · c) `3` · d) `2` · e) `7`.

**Démarche.** `rank_table` : pour chaque $k$ de `KS_31`, `X = make_almost_redundant(k, scale)`, puis `int(np.linalg.matrix_rank(X))` et `mymath.linmaps.column_space_basis(X, tol=tol).shape[1]`. Le pivot résiduel de la troisième colonne vaut environ $10^{-k}$ fois quelques unités : la tolérance $10^{-10}$ le voit jusqu'à $k = 10$, la tolérance $10^{-6}$ jusqu'à $k = 6$. `matrix_rank` utilise une tolérance relative, de l'ordre de $10^{-16}$ fois le plus grand nombre de la décomposition fois la taille : il voit la colonne libre jusqu'à $k = 13$. À l'échelle $10^6$, les arrondis du calcul dépassent la tolérance absolue $10^{-10}$ : tes pivots trouvent 3 partout, même pour $k = 16$ ; `matrix_rank`, relatif, ne change pas. Pour la copie : aucun des deux rangs n'est « le bon » pour $k = 12$, c'est la précision des données qui tranche ; avec 4 chiffres significatifs, on divise chaque colonne par sa norme et l'on prend une tolérance vers $10^{-4}$.

**Erreurs fréquentes.** Lire le dernier $k$ où le rang vaut 3 au lieu du premier où il vaut 2 ; croire que `matrix_rank` est exact ; oublier `tol=tol` dans l'appel (le troisième réglage redonne alors le premier).

### Ex M12a.32 — Une application linéaire du plan : l'image du carré unité, et ce qu'elle écrase quand son noyau n'est pas nul

**Démarche.** Le carré : `np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) @ M.T`, puis `ax.add_patch(Polygon(..., closed=True))`. `N = mymath.linmaps.null_space_basis(M)` : si `N.shape[1] == 0`, la matrice est inversible, et l'on s'arrête. Sinon `k = N[:, 0]`, `ax.plot(t * k[0], t * k[1], label="noyau")` pour `t` de $-2$ à 2 ; une colonne non nulle `c` de `M`, `ax.plot(s * c[0], s * c[1], label="image")` ; pour chaque sommet `p`, le segment `p + t k` en pointillés et le point `M @ p`. Pour la copie : par la matrice de rang 1, le carré devient un segment de la droite image ; chaque segment $\mathbf{p} + t\,\mathbf{k}$ est envoyé sur $\mathbf{M}\mathbf{p} + t\,\mathbf{M}\mathbf{k} = \mathbf{M}\mathbf{p}$, un seul point de l'image ; ces points ne peuvent plus être séparés, donc aucune application ne défait $\mathbf{M}$.

**Erreurs fréquentes.** `P @ M` au lieu de `P @ M.T` ; tracer le noyau pour une matrice inversible (un vecteur nul) ; prendre une colonne nulle pour diriger l'image ; ouvrir une figure dans la fonction.

### Ex M12a.33 — Chasse à l'erreur : une « base » liée, un noyau faux, S⁻¹AS écrit à l'envers

**Réponses** : a) `"ABD"` · b) `[3, -2, -1, 0, 1, 1]`.

(A) $\mathbf{u} + \mathbf{v}$ est dans $\operatorname{Vect}(\mathbf{u}, \mathbf{v})$ : la « base » est liée, de rang 2 ; il faut un vecteur hors du plan, $\mathbf{e}_1$ par exemple, et une vraie base de $\mathbb{R}^3$ a pour rang 3. (B) Le signe : $x_1 = -R_{12} = -2$ ; $(2, 1, 0)$ n'est pas dans le noyau, $\mathbf{A}(2, 1, 0) = (4, 8)$. (C) Juste : $c_1 = 2$, $c_2 = 3$, $c_3 = 4 - 2 - 3 = -1$. (D) $\mathbf{S}\mathbf{M}\mathbf{S}^{-1} = \begin{pmatrix} 2 & 2 \\ 0 & 3 \end{pmatrix}$, alors que $\mathbf{S}^{-1}\mathbf{M}\mathbf{S} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ ; c'est la plus dangereuse : elle s'exécute et rend une matrice plausible. (E) Juste : $3 - 2 = 1$. (F) Juste : $\mathbf{M}^{-1}(4, 6) = (1, 2)$.

### Ex M12a.34 — Un test de propriété : A fois une base du noyau donne 0, et le théorème du rang sur des matrices aléatoires

**Démarche.** Voir `05_solutions.ipynb` : trois `assert`, chacun avec un message qui dit ce qui était attendu. Le noyau fait de zéros vérifie $\mathbf{A}\mathbf{N} = \mathbf{0}$ et a la bonne forme ; seule l'indépendance des colonnes l'attrape. L'image faite de toutes les colonnes a $n$ colonnes : avec un noyau non nul, le théorème du rang l'attrape. Une base du noyau multipliée par 2 passe les trois propriétés : elle n'a pas la convention de SymPy, mais c'est encore une base du noyau. Un test de propriétés vérifie des conséquences de la bonne réponse ; pour la réponse elle-même, il faut un oracle.

**Erreurs fréquentes.** Comparer `A @ N` à 0 avec `==` (des flottants) ; tirer toujours des matrices de rang plein (l'image fausse passe alors) ; appeler `np.linalg.matrix_rank` sur un tableau sans colonne (il lève une erreur).

### Ex M12a.35 — Défi : retrouver les relations linéaires exactes cachées entre les colonnes d'un tableau, sans en inventer

**Réponse** : `True`.

**Démarche.** `norms = np.linalg.norm(X, axis=0)` ; `Y = mymath.linmaps.null_space_basis(X / norms, tol=1e-9)` ; rendre `Y / norms[:, None]`. Sur les colonnes brutes, la tolérance absolue $10^{-10}$ manque des relations (les arrondis d'une colonne de l'ordre de $10^6$ font des pivots de l'ordre de $10^{-10}$) et peut en inventer (le bruit d'une colonne de l'ordre de $10^{-4}$ passe sous la tolérance). Une fois chaque colonne ramenée à la norme 1, les pivots résiduels des relations exactes valent environ $10^{-15}$, celui de la relation approchée environ $10^{-7}$ : toute tolérance entre $10^{-12}$ et $10^{-8}$ les sépare. Pour la copie : avec $10^{-5}$, la relation à $10^{-6}$ près est prise pour exacte (une de trop) ; sur des données mesurées, la tolérance se règle sur la précision des mesures, après mise à l'échelle.

**Erreurs fréquentes.** Changer d'échelle sans revenir aux relations du tableau de départ (oublier de diviser par les normes) ; standardiser en **centrant** les colonnes (une relation affine devient linéaire, et l'on invente des relations) ; choisir la tolérance en regardant le nombre de relations attendu.
