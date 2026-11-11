# M13b · Optimisation sous contraintes et SVM — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M13b.Q1 — Lagrange : ce que dit ∇f = λ ∇g
1. $\nabla f(\mathbf{x}^*)$ est orthogonal à la courbe $g = 0$ en $\mathbf{x}^*$ : il est colinéaire à $\nabla g(\mathbf{x}^*)$. La ligne de niveau de $f$ qui passe par $\mathbf{x}^*$ y est tangente à la contrainte.
2. **Faux** : la condition est nécessaire, pas suffisante. Le point peut être un maximum sous contrainte, ou ni l'un ni l'autre.
3. $\lambda = 0$ : $\nabla f(\mathbf{x}^*) = \mathbf{0}$ convient, la contrainte ne coûte rien.
4. Cinq : trois coordonnées et deux multiplicateurs.
5. $\frac{df^*}{dc} = -\lambda = 5$ : le minimum **monte** d'environ $5 \times 0{,}1 = 0{,}5$.
6. Si $\nabla g(\mathbf{x}^*) = \mathbf{0}$, la courbe peut avoir un point anguleux ou se réduire à un point, et il n'existe pas toujours de $\lambda$ (∂ M13b.14, question 4).

### M13b.Q2 — Contrainte active ou inactive ?
1. Elle est atteinte avec égalité : $g(\mathbf{x}^*) = 0$.
2. **Vrai** : c'est la complémentarité, $\mu\,g(\mathbf{x}^*) = 0$ avec $g(\mathbf{x}^*) < 0$.
3. **Faux** : une contrainte peut être atteinte avec $\mu = 0$, quand le minimum libre tombe exactement sur son bord (minimiser $x^2$ sous $x \le 0$ : $x^* = 0$, $\mu = 0$).
4. Sous $x \le 5$ : le minimum libre $x = 3$ est admissible, la contrainte est inactive ($\mu = 0$). Sous $x \le 1$ : active, $x^* = 1$, et $2(1 - 3) + \mu = 0$ donne $\mu = 4$.
5. La contrainte ne devrait pas être active : un multiplicateur d'inégalité négatif n'est pas un point KKT. On recommence avec cette contrainte inactive ($\mu = 0$).
6. $4 - x_1 - x_2 \le 0$.

### M13b.Q3 — Primal, dual, dualité faible
1. $D(\boldsymbol{\mu}) = \min_{\mathbf{x}} \mathcal{L}(\mathbf{x}, \boldsymbol{\mu})$ (une borne inférieure, $\inf$, si le minimum n'est pas atteint), pour $\boldsymbol{\mu} \ge \mathbf{0}$.
2. **Vrai** : c'est un minimum de fonctions affines des multiplicateurs.
3. 8 est impossible : la dualité faible impose $D \le f^* = 7$. 5 est possible.
4. $\min f - \max D \ge 0$ ; il est nul quand la dualité est forte, par exemple pour un problème convexe qui vérifie la condition de Slater.
5. **Faux** : une variable par **contrainte**.
6. Ils sont optimaux tous les deux : $\mathbf{x}$ est un minimum du primal, $\boldsymbol{\mu}$ un maximum du dual (∂ M13b.15, question 5).

### M13b.Q4 — Problème convexe ou pas ?
1. **Convexe** : objectif convexe, égalité affine.
2. **Non** : l'égalité $x^2 - y = 0$ n'est pas affine (une parabole n'est pas un ensemble convexe).
3. **Non** : on **maximise** une fonction convexe.
4. **Convexe** : $e^x$ et $e^{-y}$ sont convexes, les deux inégalités sont affines.
5. **Convexe** : objectif quadratique convexe, contraintes affines en $(\mathbf{w}, b)$.
6. **Faux** : il peut n'avoir aucun minimum ($\min e^x$ sur $\mathbb{R}$) ou une infinité ($\min \max(0, x)$, atteint pour tout $x \le 0$) ; l'unicité demande la stricte convexité.

### M13b.Q5 — Ce que maximise une SVM, ce que minimise son problème
1. La marge $\rho$ : la distance de la frontière à l'exemple le plus proche.
2. Le même minimiseur (les trois quantités varient dans le même sens ou en sens inverse avec $\lVert\mathbf{w}\rVert$), mais $\frac{1}{2}\lVert\mathbf{w}\rVert^2$ est quadratique, convexe et dérivable : le problème devient un programme quadratique convexe. Maximiser $1/\lVert\mathbf{w}\rVert$ n'est pas un problème convexe.
3. Deux au moins : un de chaque classe (∂ M13b.17, question 4) ; la condition $\sum_i \alpha_i y_i = 0$ le dit aussi.
4. $\rho = 4$, bande de largeur 8.
5. **Faux** : $\mathbf{w}$ est unique (objectif strictement convexe en $\mathbf{w}$).
6. On a fixé l'échelle de $(\mathbf{w}, b)$ (la forme canonique) : la plus petite marge fonctionnelle vaut 1, et la marge géométrique est alors $1/\lVert\mathbf{w}\rVert$.

### M13b.Q6 — La hinge loss : vrai ou faux
1. **Vrai** : maximum de deux fonctions affines.
2. **Faux** : elle a un coude en $t = 1$.
3. **Faux** : un exemple bien classé mais dans la bande ($0 < t < 1$) coûte $1 - t > 0$.
4. **Vrai** : pour $t \le 0$, $1 - t \ge 1$ ; pour $t > 0$, la hinge est positive ou nulle.
5. $-1$ et $0$ (toute valeur entre les deux convient).
6. **Faux** : $\lVert\mathbf{w}\rVert$ grandit (ou reste égal) avec $C$, donc la bande **rétrécit**, et pas proportionnellement.

### M13b.Q7 — Noyau valide ou pas ?
1. **Oui** : un noyau (le produit scalaire) multiplié par une constante positive, $\varphi(\mathbf{x}) = \sqrt{3}\,\mathbf{x}$.
2. **Oui** : la somme du noyau linéaire et d'une constante positive ($\varphi(\mathbf{x}) = (\mathbf{x}, \sqrt{5})$).
3. **Non** : $k(\mathbf{x}, \mathbf{x}) = -\lVert\mathbf{x}\rVert^2 < 0$ pour $\mathbf{x} \ne \mathbf{0}$, alors qu'une matrice de Gram a une diagonale positive ou nulle.
4. **Oui** : $(\mathbf{x} \cdot \mathbf{z})^3$ est un produit de trois noyaux linéaires, le RBF est un noyau, et une somme de noyaux en est un.
5. **Non** : elle n'est pas symétrique ($k(\mathbf{x}, \mathbf{z}) \ne k(\mathbf{z}, \mathbf{x})$ en général).
6. **Vrai** : $k(\mathbf{x}, \mathbf{x}) = e^0 = 1$.

### M13b.Q8 — Primal ou dual : lequel résoudre, et quand ?
1. Primal : $p + 1 + n$ ($\mathbf{w}$, $b$ et les $\xi_i$), ou $p + 1$ sous la forme avec la hinge (§7), sans variables d'écart ; dual : $n$ (les $\alpha_i$).
2. Le primal : $n$ est énorme et $p$ petit ; une matrice de Gram de $4 \times 10^{12}$ nombres est hors de question, alors qu'une descente de sous-gradient (ou un solveur linéaire) ne manipule que 31 nombres.
3. Le dual : un noyau RBF n'a pas de $\varphi$ calculable, et une matrice de Gram de $9 \times 10^6$ nombres tient en mémoire.
4. La matrice de Gram $\mathbf{K}$, de taille $n \times n$.
5. **Vrai** : la décision $\sum_i \alpha_i y_i k(\mathbf{x}_i, \mathbf{x}) + b$ les utilise.
6. **Faux** : son $\varphi$ a une infinité de coordonnées ; on ne peut s'en servir dans le primal qu'à travers une approximation de $\varphi$ par un nombre fini de features.

<a id="rappels"></a>

## 🔁 Rappels

### M13b.R1 — La marge géométrique et l'astuce du biais (M10)
1. $9$, $7$, $10$, $8$ (pour $(0, 3)$ : le score vaut $-10$ et le label $-1$).
2. $\min_i \frac{t_i}{\lVert\mathbf{w}\rVert} = \frac{7}{5} = 1{,}4$, avec $\lVert(3, -4)\rVert = 5$.
3. On divise par 7 : $\mathbf{w} = (\frac{3}{7}, -\frac{4}{7})$, $b = \frac{2}{7}$, $\lVert\mathbf{w}\rVert = \frac{5}{7}$, et $1/\lVert\mathbf{w}\rVert = 1{,}4$.
4. $\tilde{\mathbf{w}} = (2, 3, -4)$, avec $\tilde{\mathbf{x}} = (1, x_1, x_2)$.
5. Non : M10 donne la plus grande marge par les enveloppes convexes, et ce séparateur n'a aucune raison d'être la médiatrice du segment le plus court.

### M13b.R2 — Gradient et lignes de niveau (M05b)
1. $\nabla f = (2x - y,\ -x + 4y)$.
2. $(4, -9)$.
3. $(9, 4)$ (orthogonal au gradient).
4. Dans la direction du gradient, $\frac{1}{\sqrt{97}}(4, -9)$.
5. Le long d'une ligne de niveau, $f$ est constante : sa dérivée dans la direction tangente, $\nabla f \cdot \mathbf{v}$, est nulle (M05b.12).

### M13b.R3 — Matrices définies positives (M12c)
1. Oui : trace 6 et déterminant 1 sont positifs, donc les deux valeurs propres le sont.
2. Non : le déterminant vaut $-5 < 0$, une valeur propre est négative.
3. $\begin{pmatrix} 5 & 2 & 7 \\ 2 & 2 & 4 \\ 7 & 4 & 11 \end{pmatrix}$.
4. Semi-définie positive mais pas définie positive : le troisième vecteur est la somme des deux premiers, donc $\mathbf{v} = (1, 1, -1)$ donne $\mathbf{v}^\top\mathbf{G}\mathbf{v} = \lVert\mathbf{v}_1 + \mathbf{v}_2 - \mathbf{v}_3\rVert^2 = 0$.
5. $\mathbf{v}^\top\mathbf{G}\mathbf{v} = \lVert\sum_i v_i\mathbf{v}_i\rVert^2 \ge 0$ (M12c.17).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M13b.1 — Lagrange à la main : un produit maximal sous une contrainte linéaire

**Réponses** : a) `[8, 4, 2]` · b) `64` · c) `8` · d) `72` · e) `15625/216` · f) `8` · g) `48`.

**Démarche.** Le système : $yz = \lambda$, $xz = 2\lambda$, $xy = 4\lambda$, $x + 2y + 4z = 24$. Les deux premières donnent $\frac{x}{y} = 2$, les deux dernières $\frac{y}{z} = 2$ : $x = 2y = 4z$, donc $3x = 24$, $(x, y, z) = (8, 4, 2)$, $P^* = 64$ et $\lambda = yz = 8$. Pour un second membre $c$ : $x = \frac{c}{3}$, $y = \frac{c}{6}$, $z = \frac{c}{12}$, $P^*(c) = \frac{c^3}{216}$, de dérivée $\frac{c^2}{72} = 8$ en $c = 24$ ; $P^*(25) = \frac{25^3}{216} = \frac{15\,625}{216} \approx 72{,}34$, bien estimé par $64 + 8 = 72$.

Pour la copie : la condition de Lagrange donne des candidats. Ici, sur la partie admissible où $x, y, z \ge 0$ (un triangle fermé et borné), $P$ est continu et atteint un maximum ; il vaut 0 sur les bords et 64 en l'unique point critique intérieur, qui est donc le maximum. g) le confirme sur un point : 48 < 64.

**Erreurs fréquentes.** Diviser des équations par une variable nulle ; oublier les coefficients 2 et 4 de la contrainte ; prendre $\lambda = -8$ (l'autre convention de signe : l'énoncé fixe la sienne).

**Variante.** Sous $x + y + z = 12$ ? *Réponse* : $(4, 4, 4)$, $P^* = 64$, $\lambda = 16$.

### Ex M13b.2 — La distance d'un point à un plan, retrouvée par Lagrange

**Réponses** : a) `2/3` · b) `[11/3, 7/3, 2/3]` · c) `9` · d) `3` · e) `37` · f) `9`.

**Démarche.** Stationnarité : $2(\mathbf{x} - \mathbf{x}_0) + \lambda\mathbf{n} = \mathbf{0}$, donc $\mathbf{x} = \mathbf{x}_0 - \frac{\lambda}{2}\mathbf{n}$. La contrainte : $\mathbf{n} \cdot \mathbf{x}_0 - \frac{\lambda}{2}\lVert\mathbf{n}\rVert^2 = 10$, soit $37 - \frac{81}{2}\lambda = 10$ : $\lambda = \frac{2}{3}$. D'où $\mathbf{x} = (5, 1, 3) - \frac{1}{3}(4, -4, 7)$ et $\lVert\mathbf{x} - \mathbf{x}_0\rVert^2 = \frac{1}{9} \times 81 = 9$.

Pour la copie : $\mathbf{x} - \mathbf{x}_0 = -\frac{\lambda}{2}\mathbf{n}$ est colinéaire à $\mathbf{n}$, et la contrainte donne $\frac{\lambda}{2} = \frac{\mathbf{n} \cdot \mathbf{x}_0 - d}{\lVert\mathbf{n}\rVert^2}$, d'où la distance $\frac{\lvert\mathbf{n} \cdot \mathbf{x}_0 - d\rvert}{\lVert\mathbf{n}\rVert} = \frac{27}{9}$, la formule de M07. Lagrange se généralise à une surface $g(\mathbf{x}) = 0$ quelconque, en remplaçant $\mathbf{n}$ par $\nabla g(\mathbf{x})$ (qui dépend alors du point).

**Erreurs fréquentes.** Projeter du mauvais côté ($\mathbf{x}_0 + \frac{\lambda}{2}\mathbf{n}$) ; oublier le facteur 2 de la dérivée du carré ; ne pas diviser par $\lVert\mathbf{n}\rVert$ (27).

**Variante.** La distance de l'origine à $\Pi$ ? *Réponse* : $\frac{10}{9}$.

### Ex M13b.3 — Un problème quadratique sous deux contraintes linéaires : le système de Lagrange

**Réponses** : a) `5` · b) `[3/2, 1, 1/2]` · c) `[-7/2, -3/2]` · d) `19/4` · e) `10` · f) `[1, 1, 1]` · g) `4` · h) `-23/28`.

**Démarche.** Le système par blocs :
$$\begin{pmatrix} 4 & 1 & 0 & 1 & 1 \\ 1 & 2 & 0 & 1 & 0 \\ 0 & 0 & 2 & 1 & -1 \\ 1 & 1 & 1 & 0 & 0 \\ 1 & 0 & -1 & 0 & 0 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ \lambda_1 \\ \lambda_2 \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \\ -1 \\ 3 \\ 1 \end{pmatrix}.$$
Vérification : $\mathbf{Q}\mathbf{x}^* + \mathbf{c} = (5 ;\ 3{,}5 ;\ 2)$ et $\mathbf{A}^\top\boldsymbol{\lambda} = (-5 ;\ -3{,}5 ;\ -2)$ ; $f(\mathbf{x}^*) = \frac{1}{2}(10{,}5 + 3{,}5 + 0{,}5) - 2{,}5 = 4{,}75$. Avec la seule première contrainte, le système $4 \times 4$ donne $(1, 1, 1)$ et $f = 4$. Sans contrainte, $\mathbf{x} = -\mathbf{Q}^{-1}\mathbf{c} = (\frac{4}{7}, -\frac{2}{7}, -\frac{1}{2})$ et $f = -\frac{23}{28}$.

Pour la copie : chaque contrainte de plus réduit l'ensemble admissible, donc le minimum ne peut que monter : $-\frac{23}{28} < 4 < \frac{19}{4}$. Les mineurs principaux de $\mathbf{Q}$ (4, 7, 14) sont positifs : $\mathbf{Q}$ est définie positive, la solution est unique et c'est le minimum (§5).

**Erreurs fréquentes.** Mettre $+\mathbf{c}$ au second membre ; oublier le bloc nul ; des multiplicateurs de signes opposés (la convention $f - \boldsymbol{\lambda}^\top(\mathbf{A}\mathbf{x} - \mathbf{b})$).

**Variante.** Avec $\mathbf{b} = (3, 0)$ ? *Réponse* : $\mathbf{x}^* = (1, 1, 1)$ et $\boldsymbol{\lambda} = (-3, 0)$ : la solution sous la seule première contrainte vérifie déjà $x_1 = x_3$, la deuxième contrainte ne coûte rien.

### Ex M13b.4 — Relire l'ACP par Lagrange : maximiser uᵀCu sous ‖u‖ = 1

**Réponses** : a) `13` · b) `[-0.2673, 0.8018, -0.5345]` · c) `13` · d) `0` · e) `6` · f) `13/20` · g) `19/20` · h) `2`.

**Démarche.** Le polynôme caractéristique a pour racines 13, 6 et 1 (somme 20 = la trace, produit 78 = le déterminant). Pour 13 : $\mathbf{C}(1, -3, 2) = (13, -39, 26)$ ; normalisé ($\sqrt{14}$) et orienté par la convention (la coordonnée $-3$ devient positive), $\mathbf{u}_1 = \frac{1}{\sqrt{14}}(-1, 3, -2)$. Pour 6 : $(-1, 3, 5)$ ; pour 1 : $(3, 1, 0)$. h) $C_{11} = 2$, entre la plus petite et la plus grande valeur propre, comme tout $\mathbf{u}^\top\mathbf{C}\mathbf{u}$ avec $\lVert\mathbf{u}\rVert = 1$.

Pour la copie : la stationnarité de $\mathbf{u}^\top\mathbf{C}\mathbf{u} - \lambda(\mathbf{u}^\top\mathbf{u} - 1)$ donne $\mathbf{C}\mathbf{u} = \lambda\mathbf{u}$, et en un tel point $\mathbf{u}^\top\mathbf{C}\mathbf{u} = \lambda$. Pour le deuxième axe, $2\mathbf{C}\mathbf{u} - 2\lambda\mathbf{u} - \nu\mathbf{u}_1 = \mathbf{0}$ ; multiplié par $\mathbf{u}_1^\top$ : $2\mathbf{u}_1^\top\mathbf{C}\mathbf{u} - 2\lambda\,\mathbf{u}_1 \cdot \mathbf{u} - \nu = 0$, avec $\mathbf{u}_1^\top\mathbf{C}\mathbf{u} = (\mathbf{C}\mathbf{u}_1) \cdot \mathbf{u} = 13\,\mathbf{u}_1 \cdot \mathbf{u} = 0$ : $\nu = 0$, et $\mathbf{u}$ est un vecteur propre orthogonal à $\mathbf{u}_1$, le meilleur étant celui de 6. La plus petite valeur propre est aussi un point critique : c'est le **minimum** de $\mathbf{u}^\top\mathbf{C}\mathbf{u}$ sur la sphère ; celle du milieu est un col.

**Erreurs fréquentes.** Oublier la normalisation ; le signe de la convention ; maximiser $\mathbf{u}^\top\mathbf{C}\mathbf{u}$ sans contrainte (elle n'a pas de maximum) ; prendre la plus petite valeur propre.

**Variante.** La part de variance du dernier axe ? *Réponse* : $\frac{1}{20}$.

### Ex M13b.5 — Une contrainte d'inégalité : active ou non, les conditions KKT à la main

**Réponses** : a) `False` · b) `4/3` · c) `[2/3, 5/3]` · d) `-10` · e) `-12` · f) `-4/3` · g) `-4/3`.

**Démarche.** Le minimum libre est $(2, 2)$, où $2x + y = 6 > 3$ : non admissible, la contrainte est active. Stationnarité : $2x - 4 + 2\mu = 0$ et $4y - 8 + \mu = 0$, donc $x = 2 - \mu$, $y = 2 - \frac{\mu}{4}$ ; la contrainte : $6 - \frac{9\mu}{4} = 3$, $\mu = \frac{4}{3}$. $f(\frac{2}{3}, \frac{5}{3}) = \frac{4}{9} + \frac{50}{9} - \frac{8}{3} - \frac{40}{3} = -10$. Pour $c = 8$ : $(2, 2)$ est admissible, $\mu = 0$, $f^* = -12$. g) Avec $3 - 2x - y \le 0$ supposée active : $2x - 4 - 2\mu = 0$ et $4y - 8 - \mu = 0$, d'où $6 + \frac{9\mu}{4} = 3$ et $\mu = -\frac{4}{3}$.

Pour la copie : pour $c = 3$, faisabilité ($\frac{4}{3} + \frac{5}{3} = 3$), stationnarité, signe ($\mu > 0$), complémentarité ($g = 0$). En g), le signe négatif dit que la contrainte ne doit pas être active : sous $2x + y \ge 3$, le minimum libre $(2, 2)$ est admissible, et c'est la solution, avec $\mu = 0$ et $f^* = -12$.

**Erreurs fréquentes.** Oublier de tester l'admissibilité du minimum libre ; accepter $\mu < 0$ ; le signe de la sensibilité.

**Variante.** Pour $c = 6$ ? *Réponse* : $(2, 2)$ est sur le bord, $\mu = 0$ : contrainte active de multiplicateur nul, $f^* = -12$.

### Ex M13b.6 — La fonction duale d'un petit problème quadratique, et la dualité faible

**Réponses** : a) `6*mu - 3*mu**2/8` · b) `18` · c) `8` · d) `24` · e) `[4, 2]` · f) `24` · g) `18`.

**Démarche.** $\mathcal{L} = x^2 + 2y^2 + \mu(6 - x - y)$ est minimal en $x = \frac{\mu}{2}$, $y = \frac{\mu}{4}$ : $D(\mu) = \frac{\mu^2}{4} + \frac{\mu^2}{8} + 6\mu - \frac{\mu^2}{2} - \frac{\mu^2}{4} = 6\mu - \frac{3}{8}\mu^2$, maximal en $\mu = 8$, où il vaut 24. Le primal : $x = 2y$ (Lagrange), $3y = 6$, $(4, 2)$ et $f^* = 16 + 8 = 24$.

Pour la copie : b) et g) sont des valeurs de $D$, donc des minorants (dualité faible). KKT en $(4, 2)$ : $\nabla f = (8, 8) = 8\,(1, 1)$, soit $\nabla f + \mu\nabla g = \mathbf{0}$ avec $\nabla g = (-1, -1)$ et $\mu = 8 \ge 0$, contrainte active. Le saut est nul, comme prévu : le problème est convexe et $(10, 10)$ est strictement admissible (Slater).

**Erreurs fréquentes.** Minimiser $\mathcal{L}$ en $\mu$ au lieu de $(x, y)$ ; une erreur de signe dans $\mu(6 - x - y)$ ; croire que $D$ peut dépasser $f^*$.

**Variante.** Sous $x + y \ge 3$ ? *Réponse* : $\mu^* = 4$, $f^* = D(4) = 6$, en $(2, 1)$.

### Ex M13b.7 — Reconnaître un problème convexe : fonctions, contraintes, ensembles

**Réponse** : a) `"ADFH"`.

**Démarche.** (A) objectif convexe, inégalité affine. (D) $e^x + y^2$ convexe, égalité affine. (F) $-\ln$ convexe, inégalité affine ; le domaine $x > 0$, $y > 0$ n'est pas une contrainte $g \le 0$, mais un ouvert convexe sur lequel l'objectif est défini : le problème reste convexe. (H) hinge (maximum de deux fonctions affines) plus des carrés : convexe, sans contrainte.

Pour la copie : (B) la région $x^2 + y^2 \ge 1$ (l'extérieur d'un disque) n'est pas convexe ; (C) on maximise une fonction convexe ; (E) l'égalité $x^2 + y^2 = 4$ n'est pas affine ; (G) $x^2 - y^2$ n'est pas convexe (un col). (E) se résout quand même : $\mathcal{L} = x + \lambda(x^2 + y^2 - 4)$ donne $1 + 2\lambda x = 0$ et $2\lambda y = 0$, donc $y = 0$, $x = \pm 2$ : le minimum est en $(-2, 0)$.

**Erreurs fréquentes.** Juger seulement l'objectif ; croire qu'une égalité $g = 0$ avec $g$ convexe définit un ensemble convexe ; oublier qu'un maximum de fonction convexe n'est pas un problème convexe.

**Variante.** (B) avec $\le$ au lieu de $\ge$ ? *Réponse* : convexe (un disque), de minimum $(0, 0)$.

### Ex M13b.8 — Une SVM à marge dure sur trois points, résolue par les conditions KKT

**Réponses** : a) `[-0.2, 0.4]` · b) `-0.4` · c) `[0.05, 0.05, 0.1]` · d) `0.1` · e) `2.2361` · f) `2.8` · g) `3` · h) `0.1`.

**Démarche.** $\mathbf{x}_1$ et $\mathbf{x}_2$ sont tous deux sur le bord $\mathbf{w} \cdot \mathbf{x} + b = 1$ : $\mathbf{w} \cdot (\mathbf{x}_2 - \mathbf{x}_1) = \mathbf{w} \cdot (4, 2) = 0$, donc $\mathbf{w} = k(-1, 2)$. Avec $\mathbf{w} \cdot (\mathbf{x}_1 - \mathbf{x}_3) = 2$ : $k\,(-1, 2) \cdot (-4, 3) = 10k = 2$, $k = 0{,}2$ ; $b = 1 - \mathbf{w} \cdot \mathbf{x}_1 = 1 - 1{,}4 = -0{,}4$. Les multiplicateurs : $\alpha_3 = \alpha_1 + \alpha_2$ et $\alpha_1(3, 5) + \alpha_2(7, 7) - \alpha_3(7, 2) = (-0{,}2 ;\ 0{,}4)$ ; la première coordonnée donne $-4\alpha_1 = -0{,}2$, la seconde $3\alpha_1 + 5\alpha_2 = 0{,}4$ : $\alpha_1 = \alpha_2 = 0{,}05$, $\alpha_3 = 0{,}1$.

Pour la copie : les quatre conditions KKT tiennent (contraintes respectées, toutes à 1 ; $\alpha_i > 0$ ; complémentarité ; stationnarité). La marge vaut $1/\sqrt{0{,}2} = \sqrt{5}$. Le quatrième exemple a une marge fonctionnelle de 2,8 : avec $\alpha_4 = 0$, toutes les conditions KKT restent vraies, et le problème est convexe : la solution ne change pas. Le dual vaut $0{,}2 - 0{,}1 = 0{,}1$, le primal aussi.

**Erreurs fréquentes.** Oublier $\sum_i \alpha_i y_i = 0$ ; un signe de $y_3$ ; donner la largeur de la bande ($2\sqrt{5}$) ou $\lVert\mathbf{w}\rVert$ à la place de la marge.

**Variante.** Si $\mathbf{x}_3$ était $(10, 4)$ ? *Réponse* : supposer les trois contraintes actives donne $\alpha_1 < 0$ ; seuls $\mathbf{x}_2$ et $\mathbf{x}_3$ sont des vecteurs de support ($\alpha = \frac{1}{9}$ chacun), $\mathbf{w} = (-\frac{1}{3}, \frac{1}{3})$, $b = 1$, et $\mathbf{x}_1$ a une marge fonctionnelle de $\frac{5}{3}$.

### Ex M13b.9 — La hinge loss et l'objectif régularisé de quelques points

**Réponses** : a) `[3.5, 1.5, 0.2, 1, -1.6, 1.7]` · b) `[0, 0, 0.8, 0, 2.6, 0]` · c) `0.5667` · d) `0.625` · e) `7.425` · f) `1/12` · g) `2` · h) `1`.

**Démarche.** Les scores $s = x_1 - 0{,}5x_2 + 0{,}5$ valent $3{,}5$ ; $1{,}5$ ; $0{,}2$ ; $-1$ ; $1{,}6$ ; $-1{,}7$, et les marges fonctionnelles les multiplient par le label. La somme des hinges vaut $3{,}4$, la moyenne $\frac{17}{30}$, et $J = 0{,}625 + 2 \times 3{,}4 = 7{,}425$. $\lambda = \frac{1}{nC} = \frac{1}{12}$.

Pour la copie : hors de la bande et bien classés : $(3, 0)$, $(1, 0)$, $(-2 ;\ 0{,}4)$ ; dans la bande ou sur un bord : $(0 ;\ 0{,}6)$ (dans la bande, $t = 0{,}2$) et $(-1, 1)$ (sur un bord, $t = 1$) ; du mauvais côté : $(2 ;\ 1{,}8)$. Et $nC\big(\frac{17}{30} + \frac{1}{24} \times 1{,}25\big) = 12 \times 0{,}61875 = 7{,}425$.

**Erreurs fréquentes.** $C$ fois la moyenne au lieu de la somme ; oublier le label ; compter le point de marge exactement 1 parmi ceux « strictement sous 1 ».

**Variante.** Avec $C = 0{,}5$ ? *Réponse* : $J = 0{,}625 + 1{,}7 = 2{,}325$, $\lambda = \frac{1}{3}$.

### Ex M13b.10 — Un pas de sous-gradient sur l'objectif d'une SVM linéaire

**Réponses** : a) `[1, -2, 1.5, 0.5]` · b) `2.375` · c) `[1, 1.5]` · d) `0` · e) `[0.3, 0.7]` · f) `2.165` · g) `[-0.5, 1.25]`.

**Démarche.** Scores : $1$ ; $2$ ; $-1{,}5$ ; $0{,}5$. Comptent $(0, 3)$ ($t = -2$) et $(-1, 2)$ ($t = 0{,}5$) ; $(3 ;\ 0{,}5)$ est au coude ($t = 1$). $J = \frac{1}{2}(0{,}25 + 1) + 0{,}5\,(3 + 0{,}5) = 2{,}375$. $\mathbf{g}_{\mathbf{w}} = (0{,}5 ;\ 1) - 0{,}5\,[(-1)(0, 3) + (+1)(-1, 2)] = (1 ;\ 1{,}5)$, $g_b = -0{,}5\,(-1 + 1) = 0$. Après le pas, les marges deviennent $0{,}25$ ; $-1{,}1$ ; $1{,}4$ ; $0{,}1$, et $J = 0{,}29 + 0{,}5 \times 3{,}75 = 2{,}165$.

Pour la copie : au coude, la hinge admet toute pente entre $-1$ et $0$ ; compter le point revient à prendre la pente $-1$, ce qui donne un autre sous-gradient valide. $J$ a baissé ici, mais rien ne le garantit : avec $\eta = 2$, par exemple, le pas mène à $\mathbf{w} = (-1{,}5 ;\ -2)$, et $J$ remonte à $9{,}375$.

**Erreurs fréquentes.** Le signe de $-C y_i\mathbf{x}_i$ ; compter les exemples bien au-delà de la marge ; oublier le terme $\mathbf{w}$ du sous-gradient.

**Variante.** $J$ au point de départ avec $C = 1$ ? *Réponse* : $0{,}625 + 3{,}5 = 4{,}125$.

### Ex M13b.11 — Le dual d'une SVM : lire les vecteurs de support et retrouver w

**Réponses** : a) `0` · b) `[0.7, -0.1]` · c) `-1.9` · d) `[1, 2, 4, 6]` · e) `[1, -0.5, 2.6, -0.8, 1.7, 1]` · f) `3.55` · g) `3.55`.

**Démarche.** $\mathbf{w} = 0{,}9(5, 6) + (3, 7) - (5, 8) - 0{,}9(2, 5) = (0{,}7 ;\ -0{,}1)$. Sur le vecteur libre $\mathbf{x}_1$ : $b = 1 - (3{,}5 - 0{,}6) = -1{,}9$ ; sur $\mathbf{x}_6$ : $b = -1 - (1{,}4 - 0{,}5) = -1{,}9$. $J = \frac{1}{2}(0{,}49 + 0{,}01) + (1{,}5 + 1{,}8) = 3{,}55$ ; dual : $3{,}8 - 0{,}25 = 3{,}55$.

Pour la copie : libres, 1 et 6 ($0 < \alpha_i < 1$), sur un bord ; bornés, 2 et 4 ($\alpha_i = C$), du mauvais côté ; 3 et 5 ont $\alpha_i = 0$ et une marge au-delà de 1 : tout est cohérent avec le tableau de la fiche. L'égalité du primal et du dual certifie que $(\mathbf{w}, b)$ et $\boldsymbol{\alpha}$ sont optimaux.

**Erreurs fréquentes.** Lire $b$ sur un vecteur borné ; oublier les labels dans $\mathbf{w}$ ; compter les exemples de $\alpha_i = 0$ parmi les vecteurs de support.

**Variante.** Si l'on retirait les exemples 3 et 5 ? *Réponse* : la même solution (leurs $\alpha_i$ sont nuls).

### Ex M13b.12 — Le noyau (1 + x · z)² en dimension 2 : sa fonction φ à six coordonnées

**Réponses** : a) `-13` · b) `144` · c) `[1, 5.66, -4.24, 16, -16.97, 9]` · d) `144` · e) `509` · f) `55` · g) `220`.

**Démarche.** $(1 + x_1z_1 + x_2z_2)^2 = 1 + 2x_1z_1 + 2x_2z_2 + x_1^2z_1^2 + 2x_1x_2z_1z_2 + x_2^2z_2^2$ : chaque terme est un produit d'une fonction de $\mathbf{x}$ par la même fonction de $\mathbf{z}$, d'où $\varphi$ ; les $\sqrt{2}$ répartissent les coefficients 2 des termes croisés. $\varphi(\mathbf{x}) = (1, 4\sqrt{2}, -3\sqrt{2}, 16, -12\sqrt{2}, 9)$. e) $k(\mathbf{x}, \mathbf{x}) - 2k(\mathbf{x}, \mathbf{z}) + k(\mathbf{z}, \mathbf{z}) = 676 - 288 + 121$.

Pour la copie : `count_monomials(9, 2, include_constant=True)` $= \binom{11}{2} = 55$ et `count_monomials(9, 3, include_constant=True)` $= \binom{12}{3} = 220$. Le noyau coûte 9 multiplications, 9 additions et un cube ; le produit $\varphi(\mathbf{x}) \cdot \varphi(\mathbf{z})$, 220 multiplications, sans compter le calcul des deux $\varphi$.

**Erreurs fréquentes.** Oublier les $\sqrt{2}$ ; oublier le monôme constant ou ceux de degré 1 (le noyau inhomogène les contient) ; compter les monômes de degré exactement $d$.

**Variante.** $k(\mathbf{x}, \mathbf{z})$ pour $\mathbf{x} = (4, -3)$ et $\mathbf{z} = (1, 1)$ ? *Réponse* : $(1 + 1)^2 = 4$.

### Ex M13b.13 — La matrice de Gram d'un noyau RBF sur trois points, et l'effet de γ

**Réponses** : a) `[9, 4, 13]` · b) `0.1653` · c) `[[1, 0.1653, 0.4493], [0.1653, 1, 0.0743], [0.4493, 0.0743, 1]]` · d) `0.7763` · e) `1.2921` · f) `-18` · g) `1` · h) `3`.

**Démarche.** $k = e^{-0{,}2 d^2}$ : $e^{-1{,}8} \approx 0{,}1653$, $e^{-0{,}8} \approx 0{,}4493$, $e^{-2{,}6} \approx 0{,}0743$. e) $\sqrt{2 - 2 \times 0{,}1653}$. f) $-\gamma\,d^2 = -2 \times 9$.

Pour la copie : $\det\mathbf{K} > 0$, et ses mineurs aussi : $\mathbf{K}$ est définie positive. Les distances relevées valent $\sqrt{2 - 2k}$, avec $k > 0$ : toutes inférieures à $\sqrt{2}$. Avec la matrice pleine de 1, tous les exemples ont la même image : la SVM ne peut produire qu'une décision constante. Avec l'identité, chaque exemple ne ressemble qu'à lui-même : la SVM peut apprendre n'importe quels labels d'entraînement et ne rien prédire ailleurs.

**Erreurs fréquentes.** Oublier le carré de la distance ($e^{-0{,}2 \times 3}$) ; diviser par $\gamma$ ; une matrice non symétrique.

**Variante.** $k(\mathbf{x}_2, \mathbf{x}_3)$ pour $\gamma = 0{,}1$ ? *Réponse* : $e^{-1{,}3} \approx 0{,}2725$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M13b.14 — Au point optimal sous une contrainte d'égalité, ∇f est colinéaire à ∇g

**Réponse modèle.**
1. $g(\mathbf{c}(t)) = 0$ pour tout $t$ : sa dérivée, par la règle de la chaîne (M05b), $\nabla g(\mathbf{c}(t)) \cdot \mathbf{c}'(t)$, est nulle ; en $t = 0$, $\nabla g(\mathbf{x}^*) \cdot \mathbf{c}'(0) = 0$.
2. Les points $\mathbf{c}(t)$ sont admissibles, et $\mathbf{x}^* = \mathbf{c}(0)$ minimise $f$ parmi eux : $t \mapsto f(\mathbf{c}(t))$ a un minimum en 0, sa dérivée y est nulle : $\nabla f(\mathbf{x}^*) \cdot \mathbf{c}'(0) = 0$.
3. $\nabla f(\mathbf{x}^*)$ et $\nabla g(\mathbf{x}^*)$ sont orthogonaux au vecteur non nul $\mathbf{c}'(0)$ ; en dimension 2, les vecteurs orthogonaux à $\mathbf{c}'(0)$ forment une droite, engendrée par $\nabla g(\mathbf{x}^*) \ne \mathbf{0}$ : $\nabla f(\mathbf{x}^*) = -\lambda\nabla g(\mathbf{x}^*)$ pour un $\lambda$.
4. À la question 3 (pour que $\nabla g$ engendre la droite) et pour l'existence de la courbe. Exemple : minimiser $x$ sous $g(x, y) = y^2 - x^3 = 0$ ; le minimum est $(0, 0)$, où $\nabla g = (0, 0)$ et $\nabla f = (1, 0)$ : aucun $\lambda$ ne convient.
5. $\nabla f(\mathbf{x}^*)$ est orthogonal à toutes les directions tangentes à la contrainte, qui forment l'hyperplan orthogonal à $\nabla g(\mathbf{x}^*)$ : il est donc colinéaire à $\nabla g(\mathbf{x}^*)$.

**Grille.** (1) la règle de la chaîne sur $g \circ \mathbf{c}$ ; (2) le minimum de $f \circ \mathbf{c}$ en 0 et sa dérivée nulle ; (3) l'argument de dimension avec $\nabla g \ne \mathbf{0}$ ; (4) le rôle de l'hypothèse et un contre-exemple ; (5) la généralisation par l'espace tangent.

### Ex M13b.15 — La dualité faible : la fonction duale minore le minimum du primal

**Réponse modèle.**
1. $\mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_i \mu_i g_i(\mathbf{x}) + \sum_j \lambda_j h_j(\mathbf{x})$, avec $\mu_i \ge 0$ et $g_i(\mathbf{x}) \le 0$ (chaque terme est $\le 0$) et $h_j(\mathbf{x}) = 0$ : $\mathcal{L} \le f(\mathbf{x})$.
2. $D(\boldsymbol{\mu}, \boldsymbol{\lambda}) = \inf_{\mathbf{y}} \mathcal{L}(\mathbf{y}, \boldsymbol{\mu}, \boldsymbol{\lambda}) \le \mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda}) \le f(\mathbf{x})$ ; vrai pour tout $\mathbf{x}$ admissible et tous les multiplicateurs autorisés, donc $\sup D \le \inf f$.
3. À $\mathbf{x}$ fixé, $\mathcal{L}$ est affine en $(\boldsymbol{\mu}, \boldsymbol{\lambda})$ : $\mathcal{L}(\mathbf{x}, \theta\mathbf{m}_1 + (1 - \theta)\mathbf{m}_2) = \theta\mathcal{L}(\mathbf{x}, \mathbf{m}_1) + (1 - \theta)\mathcal{L}(\mathbf{x}, \mathbf{m}_2) \ge \theta D(\mathbf{m}_1) + (1 - \theta)D(\mathbf{m}_2)$ ; en prenant l'infimum en $\mathbf{x}$ : $D(\theta\mathbf{m}_1 + (1 - \theta)\mathbf{m}_2) \ge \theta D(\mathbf{m}_1) + (1 - \theta)D(\mathbf{m}_2)$.
4. Pour que $\mu_i g_i(\mathbf{x}) \le 0$ sur tout point admissible ; $h_j(\mathbf{x}) = 0$ rend le signe de $\lambda_j$ indifférent.
5. Pour tout $\mathbf{y}$ admissible, $f(\mathbf{y}) \ge D(\boldsymbol{\mu}, \boldsymbol{\lambda}) = f(\mathbf{x})$ : $\mathbf{x}$ est un minimum ; pour tous multiplicateurs autorisés, $D(\mathbf{m}) \le f(\mathbf{x}) = D(\boldsymbol{\mu}, \boldsymbol{\lambda})$ : ils maximisent $D$.

**Grille.** (1) le signe de chaque terme ; (2) l'infimum et le passage aux bornes ; (3) l'affinité en les multiplicateurs et l'infimum de fonctions affines ; (4) le rôle du signe ; (5) le certificat.

### Ex M13b.16 — Pour un problème convexe, un minimum local est global

**Réponse modèle.**
1. $K$ est convexe et contient $\mathbf{x}^*$ et $\mathbf{y}$ : il contient tout le segment.
2. $f(\mathbf{x}_\theta) \le (1 - \theta)f(\mathbf{x}^*) + \theta f(\mathbf{y}) < (1 - \theta)f(\mathbf{x}^*) + \theta f(\mathbf{x}^*) = f(\mathbf{x}^*)$, car $\theta > 0$ et $f(\mathbf{y}) < f(\mathbf{x}^*)$.
3. $\lVert\mathbf{x}_\theta - \mathbf{x}^*\rVert = \theta\lVert\mathbf{y} - \mathbf{x}^*\rVert < r$ dès que $\theta < r/\lVert\mathbf{y} - \mathbf{x}^*\rVert$ : un point de $K$ aussi près qu'on veut de $\mathbf{x}^*$ fait mieux, contradiction. Aucun $\mathbf{y}$ ne fait mieux : $\mathbf{x}^*$ est un minimum global.
4. Si $\mathbf{x}^* \ne \mathbf{y}^*$ sont deux minima, de valeur $m$, leur milieu est dans $K$ et $f\big(\frac{\mathbf{x}^* + \mathbf{y}^*}{2}\big) < \frac{1}{2}m + \frac{1}{2}m = m$ : contradiction.
5. Chaque $\{g_i \le 0\}$ est convexe (pour $\mathbf{x}, \mathbf{y}$ dedans, $g_i$ convexe donne $g_i(\mathbf{x}_\theta) \le 0$), chaque $\{h_j = 0\}$ est un hyperplan, et une intersection de convexes est convexe. Pour une fonction convexe qu'on **maximise**, l'inégalité de 2 va dans le mauvais sens : rien n'empêche un maximum local de ne pas être global, et les maxima sont souvent au bord.

**Grille.** (1) le segment dans $K$ ; (2) l'inégalité stricte grâce à $\theta > 0$ ; (3) le choix de $\theta$ et la contradiction ; (4) l'unicité par le milieu ; (5) la convexité de l'ensemble admissible et le cas du maximum.

### Ex M13b.17 — Maximiser la marge revient à minimiser ½ ‖w‖²

**Réponse modèle.**
1. La marge ne change pas quand on multiplie $(\mathbf{w}, b)$ par $c > 0$ ; on choisit l'échelle où la plus petite marge fonctionnelle vaut 1 ; la marge vaut alors $1/\lVert\mathbf{w}\rVert$, et la maximiser revient à minimiser $\lVert\mathbf{w}\rVert$ sous $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ (M10.8).
2. $u \mapsto \frac{1}{2}u^2$ est strictement croissante sur $[0, +\infty[$ : $\lVert\mathbf{w}\rVert \le \lVert\mathbf{w}'\rVert$ équivaut à $\frac{1}{2}\lVert\mathbf{w}\rVert^2 \le \frac{1}{2}\lVert\mathbf{w}'\rVert^2$, donc les minimiseurs sont les mêmes.
3. $\frac{1}{2}\lVert\mathbf{w}\rVert^2$ a pour hessienne l'identité (définie positive) : stricte convexité. Chaque contrainte est un demi-espace de $(\mathbf{w}, b)$, convexe, et l'intersection l'est. Deux solutions de $\mathbf{w}$ distincts auraient un milieu admissible de valeur strictement plus petite (∂ M13b.16, question 4).
4. Si aucun exemple $+1$ n'était à 1, toutes leurs marges fonctionnelles dépasseraient $1 + \varepsilon$ ; en diminuant $b$ de $\frac{\varepsilon}{2}$, toutes les contraintes deviennent strictes (celles des $-1$ s'améliorent) ; on peut alors multiplier $(\mathbf{w}, b)$ par un $c < 1$ proche de 1 en gardant toutes les contraintes, et $\lVert\mathbf{w}\rVert$ baisse : contradiction. Même raisonnement pour les $-1$.
5. Un exemple $\mathbf{x}_s$ de marge fonctionnelle 1 donne $b = y_s - \mathbf{w} \cdot \mathbf{x}_s$, avec $\mathbf{w}$ unique : $b$ est unique.

**Grille.** (1) l'invariance d'échelle et la forme canonique, citées ; (2) la monotonie du carré ; (3) la stricte convexité, la convexité de l'ensemble et l'argument du milieu ; (4) le déplacement de $b$ puis la réduction d'échelle ; (5) l'unicité de $b$.

### Ex M13b.18 — Marge souple : la formulation avec des variables d'écart et celle avec la hinge loss sont équivalentes

**Réponse modèle.**
1. Les deux contraintes disent $\xi_i \ge 1 - y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ et $\xi_i \ge 0$, donc $\xi_i \ge \max(0, 1 - t_i)$, et cette valeur est admissible : c'est la plus petite.
2. À $(\mathbf{w}, b)$ fixés, l'objectif de (P) est croissant en chaque $\xi_i$ ($C > 0$) : son minimum prend chaque $\xi_i$ le plus petit possible, et vaut $\frac{1}{2}\lVert\mathbf{w}\rVert^2 + C\sum_i \max(0, 1 - t_i) = J(\mathbf{w}, b)$.
3. $\min_{\mathbf{w}, b, \boldsymbol{\xi}} = \min_{\mathbf{w}, b}\min_{\boldsymbol{\xi}} = \min_{\mathbf{w}, b} J$ : même valeur, et un $(\mathbf{w}, b)$ est optimal pour l'un si et seulement s'il l'est pour l'autre (avec les $\xi_i$ de la question 1).
4. $(\mathbf{w}_{\mathrm{dure}}, b_{\mathrm{dure}}, \boldsymbol{\xi} = \mathbf{0})$ est admissible pour (P), de valeur $\frac{1}{2}\lVert\mathbf{w}_{\mathrm{dure}}\rVert^2$ : l'optimum fait au moins aussi bien.
5. À l'optimum, $C\sum_i \xi_i \le$ (objectif optimal) $\le \frac{1}{2}\lVert\mathbf{w}_{\mathrm{dure}}\rVert^2$, d'où $\sum_i \xi_i \le \frac{\lVert\mathbf{w}_{\mathrm{dure}}\rVert^2}{2C}$ : la somme des écarts tend vers 0 quand $C \to \infty$, et la solution se rapproche de la marge dure.

**Grille.** (1) les deux contraintes réunies en un maximum ; (2) la croissance de l'objectif en $\xi_i$ ; (3) l'échange des minimisations ; (4) un point admissible tiré de la marge dure ; (5) la borne et la limite.

### Ex M13b.19 — La somme et le produit de deux noyaux sont des noyaux ; une matrice de Gram est semi-définie positive

**Réponse modèle.**
1. $\mathbf{v}^\top\mathbf{K}\mathbf{v} = \sum_{i,j} v_iv_j\,\varphi(\mathbf{x}_i) \cdot \varphi(\mathbf{x}_j) = \big(\sum_i v_i\varphi(\mathbf{x}_i)\big) \cdot \big(\sum_j v_j\varphi(\mathbf{x}_j)\big) \ge 0$ ; $\mathbf{K}$ est symétrique : semi-définie positive. C'est M12c.17 avec les vecteurs $\varphi(\mathbf{x}_i)$ en lignes.
2. $\sqrt{c}\,\varphi$.
3. $\varphi(\mathbf{x}) = (\varphi_1(\mathbf{x}), \varphi_2(\mathbf{x})) \in \mathbb{R}^{q_1 + q_2}$ : $\varphi(\mathbf{x}) \cdot \varphi(\mathbf{z}) = k_1(\mathbf{x}, \mathbf{z}) + k_2(\mathbf{x}, \mathbf{z})$.
4. $\sum_{a,b}\varphi_{1,a}(\mathbf{x})\varphi_{2,b}(\mathbf{x})\,\varphi_{1,a}(\mathbf{z})\varphi_{2,b}(\mathbf{z}) = \big(\sum_a \varphi_{1,a}(\mathbf{x})\varphi_{1,a}(\mathbf{z})\big)\big(\sum_b \varphi_{2,b}(\mathbf{x})\varphi_{2,b}(\mathbf{z})\big) = k_1k_2$.
5. $\mathbf{x} \cdot \mathbf{z}$ est un noyau ; la constante $c$ aussi : pour $c > 0$, c'est $c$ fois le noyau constant égal à 1 (question 2), et $c = 0$ n'ajoute rien ; leur somme en est un (question 3), et la puissance $d$ est un produit de $d$ copies de ce noyau (question 4).
6. Pour un point $\mathbf{x}$ et un point $\mathbf{z}$ à distance 1, la matrice de Gram vaut $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, de valeur propre $-1$ ; ou plus simplement : $\mathbf{v} = (1, -1)$ donne $\mathbf{v}^\top\mathbf{K}\mathbf{v} = -2 < 0$.

**Grille.** (1) le développement de la forme quadratique et la symétrie ; (2) à (4) une $\varphi$ explicite pour chaque construction ; (5) l'assemblage sans écrire $\varphi$ ; (6) un contre-exemple chiffré.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13b.20 — Pont : la décision d'une SVM à noyau, une somme pondérée sur les vecteurs de support

**Réponses** : a) `0` · b) `0.1056` · c) `1` · d) `-0.2584` · e) `-0.1` · f) `3`.

**Démarche.** Pour $(0{,}5 ;\ 0{,}5)$, les distances au carré aux trois vecteurs de support valent $2{,}5$ ; $4{,}5$ ; $6{,}5$, et les noyaux $e^{-0{,}75} \approx 0{,}4724$, $e^{-1{,}35} \approx 0{,}2592$, $e^{-1{,}95} \approx 0{,}1423$ : $s = 0{,}3779 - 0{,}1296 - 0{,}0427 - 0{,}1 \approx 0{,}1056$. Pour $(2, 2)$ : distances au carré 10, 9 et 2, d'où $s = 0{,}8\,e^{-3} - 0{,}5\,e^{-2{,}7} - 0{,}3\,e^{-0{,}6} - 0{,}1 \approx -0{,}2584$.

Pour la copie : $\sum_i \alpha_i y_i = 0$ est la stationnarité du lagrangien en $b$ (fiche §6). Loin de tous les vecteurs de support, chaque noyau tend vers 0 et la décision vers $b = -0{,}1$ : la classe $-1$, celle que favorise le biais. Le coût d'une prédiction est un noyau par vecteur de support : c'est leur nombre, qui grandit en général avec les données, qui le décide.

**Erreurs fréquentes.** Oublier le biais ; oublier les labels ; la distance non élevée au carré.

**Variante.** $s(-1, 1)$ ? *Réponse* : $0{,}8 - 0{,}5\,e^{-3{,}9} - 0{,}3\,e^{-2{,}4} - 0{,}1 \approx 0{,}6627$.

### Ex M13b.21 — MML §7.2 et §7.3 : Lagrange, dualité et optimisation convexe, en anglais

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. Une fonction qui vaut 0 quand la contrainte est respectée et $+\infty$ sinon, ajoutée à l'objectif : le problème contraint devient un problème sans contrainte, mais l'objectif est discontinu. Le lagrangien remplace cette marche infinie par une fonction linéaire de $g_i$, de pente $\lambda_i \ge 0$, qui la minore.
2. L'inégalité du minimax : le maximum (en $\mathbf{y}$) d'un minimum (en $\mathbf{x}$) est au plus le minimum d'un maximum. Appliquée au lagrangien, elle donne $\max_{\boldsymbol{\lambda}} D \le \min_{\mathbf{x}} \max_{\boldsymbol{\lambda}} \mathcal{L} = \min f$ : c'est la dualité faible de ∂ M13b.15, démontrée autrement.
3. Une égalité est remplacée par deux inégalités, $h \le 0$ et $-h \le 0$ ; la différence de leurs deux multiplicateurs positifs peut prendre n'importe quel signe : d'où un multiplicateur libre.
4. Un objectif et des inégalités convexes, et des égalités $h_j = 0$ qui définissent des ensembles convexes. Une fonction dérivable est convexe si et seulement si elle est au-dessus de ses tangentes ; deux fois dérivable, si et seulement si sa hessienne est semi-définie positive. La fiche §5 demande des égalités affines : c'est le cas courant, et une égalité affine définit toujours un ensemble convexe.
5. Pour $\min \frac{1}{2}\mathbf{x}^\top\mathbf{Q}\mathbf{x} + \mathbf{c}^\top\mathbf{x}$ sous $\mathbf{A}\mathbf{x} \le \mathbf{b}$, le dual se calcule en minimisant le lagrangien en $\mathbf{x}$ : $\mathbf{x} = -\mathbf{Q}^{-1}(\mathbf{c} + \mathbf{A}^\top\boldsymbol{\lambda})$. Pour M13b.6 : $\mathbf{Q} = \operatorname{diag}(2, 4)$, $\mathbf{c} = \mathbf{0}$, $\mathbf{A} = (-1 \ \ -1)$, $b = -6$ : $D(\mu) = -\frac{1}{2}\mu^2\,(1, 1)\mathbf{Q}^{-1}(1, 1)^\top + 6\mu = 6\mu - \frac{3}{8}\mu^2$.
6. Par exemple : *constrained optimization* (optimisation sous contraintes), *weak duality* (dualité faible), *convex set* (ensemble convexe).

**Grille.** (1) l'indicatrice et la relaxation ; (2) le minimax et le lien avec ∂ M13b.15 ; (3) les égalités ; (4) les caractérisations ; (5) le calcul refait ; (6) trois mots.

### Ex M13b.22 — MML §12.2 à §12.5 : marge, primal, dual et noyaux (§12.1 a été lu en M10)

**Réponse modèle** (avec tes mots).
1. La lettre $r$. Le §12.2.1 suppose $\lVert\mathbf{w}\rVert = 1$ et maximise $r$ ; la dérivation « traditionnelle » du §12.2.2 fixe plutôt à 1 la marge fonctionnelle des points les plus proches, et minimise $\lVert\mathbf{w}\rVert$. Le §12.2.3 montre que les deux problèmes ont les mêmes solutions, par un changement d'échelle.
2. Géométriquement : des variables d'écart $\xi_n$ laissent un exemple entrer dans la bande, ou passer du mauvais côté, en payant $C\xi_n$. Par une loss : la hinge plus un terme de régularisation. Leur équivalence est ∂ M13b.18.
3. $\mathbf{w} = \sum_n \alpha_n y_n\mathbf{x}_n$ et $\sum_n \alpha_n y_n = 0$ ; le dual est un programme quadratique en $\boldsymbol{\alpha}$, sous $\sum_n y_n\alpha_n = 0$ et $0 \le \alpha_n \le C$. Le livre l'écrit comme une **minimisation** de l'opposé de l'objectif de la fiche : même solution, signe changé.
4. Pour la marge dure, résoudre le dual revient à chercher les deux points les plus proches des enveloppes convexes des deux classes ; la frontière est la médiatrice de leur segment : le théorème de la plus grande marge de M10. Pour la marge souple, on remplace les enveloppes par des enveloppes « réduites ».
5. Le noyau remplace le produit scalaire dans le dual ; ses matrices doivent être symétriques et semi-définies positives ; le livre cite le noyau polynomial, le RBF gaussien et le noyau rationnel quadratique, et signale les autres sens du mot « noyau ». Le §12.5 écrit le primal et le dual comme des programmes quadratiques standard, et résout la version sans contrainte (la hinge) par sous-gradient.
6. Par exemple : *support vector* (vecteur de support), *slack variable* (variable d'écart), *kernel trick* (astuce du noyau).

**Grille.** (1) les deux normalisations et leur équivalence ; (2) les deux vues de la marge souple ; (3) le dual, la boîte et le signe ; (4) les enveloppes convexes et M10 ; (5) les noyaux et la résolution numérique ; (6) trois mots.

### Ex M13b.23 — Fermi : la taille de la matrice de Gram d'une SVM à noyau sur 100 000 exemples

**Réponse modèle.**
1. $n^2 = 10^{10}$ nombres ; par symétrie, $\frac{n(n+1)}{2} \approx 5 \times 10^9$.
2. $8 \times 10^{10}$ octets, 80 Go, en `float64` (40 Go en n'en gardant que la moitié) ; 40 Go en `float32`. Cinq fois la mémoire d'un ordinateur portable de 16 Go, au moins.
3. Chaque distance demande environ $2p = 100$ opérations : $10^{10} \times 100 = 10^{12}$ opérations (la moitié par symétrie), soit de l'ordre de 1 000 secondes, un quart d'heure.
4. $200 \times 10^6 / 4 = 5 \times 10^7$ nombres en `float32`, soit 0,5 % de la matrice : le solveur recalcule les valeurs du noyau au fur et à mesure.
5. $8n^2 \le 1{,}6 \times 10^{10}$ donne $n \le 4{,}5 \times 10^4$ environ : au-delà de quelques dizaines de milliers d'exemples, la matrice entière ne tient plus, et le temps (au moins en $n^2$) devient prohibitif. Pour de très gros datasets : une SVM linéaire par le primal, ou un $\varphi$ approché de petite dimension.

### Ex M13b.24 — Expliquer un multiplicateur de Lagrange comme un prix

**Réponse modèle** (6 à 10 phrases).
> Quand on optimise sous une contrainte, on fait moins bien que si l'on était libre : la contrainte a un coût. Le multiplicateur de Lagrange mesure ce coût à la marge : c'est ce que gagnerait l'objectif si l'on desserrait la contrainte d'une unité. Par exemple, tu veux maximiser tes ventes avec un budget publicitaire de 10 000 € ; si le multiplicateur de la contrainte de budget vaut 3, chaque euro de budget en plus rapporterait environ 3 € de ventes, et il est rentable de l'augmenter tant que ce prix dépasse ce que coûte l'euro. Si, au contraire, tu ne dépenses pas tout ton budget parce qu'au-delà d'un certain niveau la publicité ne sert plus à rien, la contrainte ne gêne pas : son multiplicateur vaut 0, et un euro de plus ne changerait rien. Le multiplicateur dit donc quelles contraintes coûtent cher, et combien. Enfin, on peut remplacer une contrainte par une pénalité, en faisant payer chaque unité au-delà de la limite à ce prix : on retrouve la même solution. C'est ce que font les régularisations en machine learning.

En 3 phrases : « Le multiplicateur d'une contrainte est son prix : ce que l'objectif gagnerait si on la desserrait d'une unité. Une contrainte qui ne gêne pas a un prix nul. Faire payer ce prix à la place de la contrainte donne la même solution : c'est le lien entre une contrainte et une pénalité. »

**Grille.** (1) le coût d'une contrainte ; (2) le gain par unité de contrainte desserrée ; (3) un exemple chiffré ; (4) la contrainte qui ne gêne pas ; (5) le lien avec une pénalité ; (6) une version en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M13b.E1 — « Qu'est-ce qu'un problème d'optimisation convexe, et pourquoi est-ce une bonne nouvelle ? »

**Réponse modèle (60 secondes).**

> Un problème d'optimisation est convexe quand on minimise une fonction convexe sur un ensemble convexe, ce qui revient à demander des contraintes d'inégalité convexes et des contraintes d'égalité affines. C'est une bonne nouvelle pour quatre raisons. D'abord, tout minimum local est global : un algorithme qui ne trouve plus de direction de descente a fini, il ne s'est pas arrêté dans un creux secondaire. Ensuite, si la fonction est strictement convexe, la solution est unique. Troisièmement, les conditions KKT sont suffisantes : une solution candidate se vérifie, on n'a pas à croire l'algorithme sur parole. Enfin, sous une hypothèse légère, la condition de Slater, la dualité est forte : le problème dual donne la même valeur et un certificat d'optimalité. En machine learning, la régression ridge, la régression logistique régularisée et les SVM sont convexes. Un réseau de neurones ne l'est pas : on y vit sans ces garanties, avec des initialisations et des pas bien choisis, et l'on juge le résultat sur des données de validation.

**Grille.** (1) la définition (objectif, inégalités, égalités affines) ; (2) local = global ; (3) l'unicité ; (4) les KKT suffisantes ; (5) la dualité forte ; (6) des exemples et un contre-exemple.

### M13b.E2 — « Hinge loss ou log-loss : quelles différences ? »

**Réponse modèle (60 secondes).**

> Les deux s'écrivent en fonction de la marge fonctionnelle $t = y\,s$ d'un exemple : la hinge vaut $\max(0, 1 - t)$, la log-loss $\ln(1 + e^{-t})$. Elles ont beaucoup en commun : convexes, décroissantes, presque linéaires pour un exemple très mal classé, et, après une mise à l'échelle, des majorants de l'erreur de classification. Trois différences comptent. La log-loss est dérivable partout, la hinge a un coude en $t = 1$, d'où le sous-gradient. La hinge vaut exactement 0 dès que $t \ge 1$ : les exemples bien classés avec de la marge ne comptent plus du tout, et la solution ne dépend que des vecteurs de support ; la log-loss ne s'annule jamais, tous les exemples tirent un peu sur les paramètres. Enfin, la log-loss est une log-vraisemblance : le modèle sort une probabilité ; la hinge ne donne qu'un score, qu'il faudrait calibrer après coup. Sur des données séparables, la hinge atteint 0 avec des poids finis, alors que la log-loss non régularisée continue de baisser quand les poids grandissent. On choisit la log-loss quand on veut des probabilités, la hinge quand on veut une frontière qui ne dépend que des exemples difficiles.

**Grille.** (1) les deux formules en fonction de $y\,s$ ; (2) les points communs ; (3) la dérivabilité ; (4) le zéro et les vecteurs de support ; (5) score ou probabilité ; (6) un critère de choix.

<a id="notebook"></a>

## Notebook

*(complété avec les exercices M13b.25 à M13b.34)*
