# R3 · Fonctions — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ 📈 Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R3.Q1 — Image, antécédent, ensemble de définition
1. **Vrai** : $(-3)^2 - 5 = 9 - 5 = 4$.
2. **Vrai** : $x^2 - 5 = 4 \iff x^2 = 9 \iff x = -3$ ou $x = 3$.
3. **Faux** : $x^2 - 5 = -6$ donnerait $x^2 = -1$, impossible.
4. **Faux** : c'est la définition même d'une fonction, une seule image par nombre.
5. **Faux** : seule la valeur $-1$ est interdite ; l'ensemble de définition est $\mathbb{R} \setminus \{-1\}$, qui contient aussi les nombres plus petits que $-1$.
6. **Vrai** : $x - 2 \ge 0 \iff x \ge 2$.

### R3.Q2 — Lire un graphique
1. **Vrai** : au-dessus de $x = 1$, la courbe est à la hauteur 1 (c'est son point le plus haut sur $[0 \;;\; 3]$).
2. **Vrai** : la droite $y = 1$ touche la courbe en $x = 1$ et la recoupe en $x = 4$ ; à gauche de 1, la courbe est en dessous.
3. **Faux** : $f$ est croissante sur $[0 \;;\; 1]$, puis décroissante sur $[1 \;;\; 3]$.
4. **Vrai** : $f(0) = -1$ et $f(3) = -1$, et la courbe ne descend jamais plus bas sur $[0 \;;\; 4]$.
5. **Faux** : sur $[0 \;;\; 4]$, $f$ ne descend pas sous $-1$.
6. **Vrai** : $f(2) = 0$ et $f(3) = -1$.

### R3.Q3 — Pente et ordonnée à l'origine
1. **Vrai** : $f(0) = 5$.
2. **Faux** : $3 - x = -x + 3$ a pour pente $-1$ ; la droite descend.
3. **Vrai** : $\frac{8 - 2}{3 - 1} = 3$.
4. **Faux** : une droite de pente 0 est **horizontale**. Une droite verticale n'est pas la courbe d'une fonction.
5. **Vrai** : $4x = 4x + 0$, une fonction linéaire, cas particulier de fonction affine.
6. **Vrai** : la pente vaut $\frac{7 - 1}{2 - 0} = 3$, donc $f(x) = 3x + 1$ et $f(1) = 4$ (le milieu, pour une droite).

### R3.Q4 — Fonctions de référence : allure et variations
1. **Faux** : décroissante sur $]-\infty \;;\; 0]$, croissante sur $[0 \;;\; +\infty[$.
2. **Vrai** : l'inverse est décroissant sur $]0 \;;\; +\infty[$ : il retourne l'ordre.
3. **Faux** : $\sqrt{x}$ demande $x \ge 0$.
4. **Faux** : $\sqrt{(-3)^2} = 3 \ne -3$ ; en général, $\sqrt{x^2} = |x|$.
5. **Vrai** : sur $]-\infty \;;\; 0]$, $|x| = -x$, une fonction affine de pente $-1$.
6. **Vrai** : pour $x \ge 0$, $\max(0, x) = x$.
7. **Faux** : $9 > 1$. Le carré est décroissant sur les négatifs : il retourne l'ordre.

### R3.Q5 — Discriminant : combien de racines ?
1. **Deux** : $\Delta = 16 - 12 = 4 > 0$ (racines 1 et 3).
2. **Aucune** : $\Delta = 4 - 20 = -16 < 0$.
3. **Une** : $\Delta = 16 - 16 = 0$ ; c'est $(2x - 1)^2$, racine double $\frac{1}{2}$.
4. **Deux** : $\Delta = 1 + 8 = 9 > 0$.
5. **Aucune** : $x^2 + 7 \ge 7$ pour tout $x$.
6. **Deux** : un « U » dont le point le plus bas est sous l'axe ($\beta = -2 < 0$) coupe forcément l'axe deux fois.
7. **Deux** : $\Delta = b^2 - 4 \times 3 \times (-5) = b^2 + 60 > 0$ quel que soit $b$. Quand $a$ et $c$ ont des signes contraires, il y a toujours deux racines.

### R3.Q6 — Croissante, décroissante, extremum
1. **Vrai** : forme canonique, $a = 1 > 0$, sommet $(1, 2)$.
2. **Faux** : $-(x + 3)^2 + 4 = -(x - (-3))^2 + 4$ : le maximum 4 est atteint en $x = -3$.
3. **Faux** : le carré est croissant sur $[1 \;;\; 5]$, son minimum y vaut $1^2 = 1$. Le 0 est atteint en $x = 0$, hors de l'intervalle.
4. **Vrai** : $f(b) - f(a) = -2(b - a) < 0$ pour $a < b$ (R3.14).
5. **Faux** : le maximum est une valeur de $f$, l'argmax une valeur de $x$.
6. **Vrai** : pour tout $x$ de $[0 \;;\; 4]$, $x \le 4$ donc $f(x) \le f(4)$.

### R3.Q7 — f∘g ou g∘f ?
1. **Vrai** : $g(0) = 9$, puis $f(9) = 3$.
2. **Faux** : $f(0) = 0$, puis $g(0) = 9$.
3. **Faux** : $(f \circ g)(x) = \sqrt{x + 9}$ ; $\sqrt{x} + 9$ est $(g \circ f)(x)$.
4. **Vrai** : $g(-5) = 4$ et $\sqrt{4} = 2$.
5. **Faux** : il faudrait calculer $f(-5) = \sqrt{-5}$ en premier.
6. **Faux** : ce quiz en est un contre-exemple.

### R3.Q8 — Réciproque et inverse : ne pas confondre
1. **Vrai** : $y = 2x + 6 \iff x = \frac{y - 6}{2}$.
2. **Faux** : c'est l'inverse $\frac{1}{f(x)}$, pas la réciproque.
3. **Vrai** : c'est la définition de la réciproque.
4. **Faux** : 4 a deux antécédents, $-2$ et $2$.
5. **Vrai** : sur les positifs, le carré et la racine se défont l'un l'autre.
6. **Faux** : elles sont symétriques par rapport à la droite $y = x$.

<a id="rappels"></a>

## 🔁 Rappels

### R3.R1 — Identités remarquables (R2)
1. $x^2 - 14x + 49$.
2. $9x^2 + 12x + 4$.
3. $(x + 5)^2$.
4. $(4x - 3)(4x + 3)$.
5. 16 : $x^2 - 8x + 16 = (x - 4)^2$. C'est exactement le geste de la forme canonique (fiche §5).

### R3.R2 — Inéquations et intervalles (R2)
1. $3x > 9 \iff x > 3$ : $]3 \;;\; +\infty[$.
2. $-2x \ge -4 \iff x \le 2$ (le sens change) : $]-\infty \;;\; 2]$.
3. $]2 \;;\; 4]$.
4. $]-\infty \;;\; 3[ \;\cup\; ]3 \;;\; +\infty[$, c'est-à-dire $\mathbb{R} \setminus \{3\}$.
5. Les points à moins de 4 de 1 : $]-3 \;;\; 5[$.

### R3.R3 — Puissances et racines (R1)
1. 7.
2. $\frac{3}{4}$.
3. $-8$.
4. $4\sqrt{3}$ ($48 = 16 \times 3$).
5. $-a$ : $\sqrt{a^2} = |a|$, et $|a| = -a$ quand $a < 0$ (par exemple $\sqrt{(-5)^2} = 5 = -(-5)$).

<a id="papier"></a>

## ✏️ 📈 Papier-crayon

### Ex R3.1 — Images, antécédents et ensemble de définition

**Réponses** : a) `10` · b) `"-4/5"` · c) `[-3, 3]` · d) `[]` · e) `3` · f) `"]-oo ; 4[ U ]4 ; +oo["` · g) `"]-oo ; 3]"` · h) `"[-2 ; 1[ U ]1 ; +oo["`.

**Démarche.**
- a) $f(-2) = 3 \times (-2)^2 - (-2) - 4 = 12 + 2 - 4 = 10$.
- b) $g\left(\frac{1}{2}\right) = \frac{2 \times \frac{1}{2} + 1}{\frac{1}{2} - 3} = \frac{2}{-\frac{5}{2}} = 2 \times \left(-\frac{2}{5}\right) = -\frac{4}{5}$.
- c) $x^2 + 1 = 10 \iff x^2 = 9 \iff x = -3$ ou $x = 3$.
- d) $x^2 + 1 = -3 \iff x^2 = -4$ : aucune solution, la liste vide.
- e) $4x - 5 = 7 \iff 4x = 12 \iff x = 3$.
- f) $x - 4 \ne 0 \iff x \ne 4$.
- g) $6 - 2x \ge 0 \iff -2x \ge -6 \iff x \le 3$ (on divise par $-2$ : le sens change).
- h) deux conditions : $x + 2 \ge 0$, soit $x \ge -2$, **et** $x \ne 1$. On garde $[-2 \;;\; +\infty[$ privé de 1.

**Erreurs fréquentes.**
- a) $3 \times -2^2 = -12$ : sans parenthèses, le carré ne porte que sur 2.
- c) Calculer $h(10) = 101$ au lieu de résoudre $h(x) = 10$ ; ou oublier l'antécédent négatif.
- e) Calculer $k(7) = 23$.
- g) Garder le sens en divisant par $-2$.
- h) Oublier une des deux conditions, ou exclure $-2$ alors que $\sqrt{0} = 0$ existe.

**Variante.** L'ensemble de définition de $x \mapsto \frac{1}{\sqrt{x - 1}}$ ? *Réponse* : $x - 1 > 0$ (strictement : la racine est au dénominateur), soit $]1 \;;\; +\infty[$.

### Ex R3.2 — Lire des valeurs, des solutions et des variations sur un graphique

**Réponses** : a) `4` · b) `0` · c) `[-3, -1, 4]` · d) `[-4, 0, 3]` · e) `4` · f) `[-2, 5]` · g) `"[1 ; 5]"` · h) `"[-3 ; -1] U [4 ; 5]"`.

**Démarche.** La courbe relie les points $(-4, 0)$, $(-2, 4)$, $(1, -2)$, $(3, 0)$ et $(5, 4)$.
- a) Au-dessus de $x = -2$, la courbe est à la hauteur 4.
- b) Le segment de $(-2, 4)$ à $(1, -2)$ descend de 2 par unité : en $x = 0$, il est à $4 - 2 \times 2 = 0$ (la courbe passe par l'origine).
- c) La droite $y = 2$ coupe le premier segment en $x = -3$, le deuxième en $x = -1$ et le dernier en $x = 4$.
- d) La courbe est sur l'axe horizontal à son extrémité gauche ($x = -4$), en $x = 0$ et au point anguleux $(3, 0)$.
- e) et f) La plus grande hauteur est 4, atteinte en $x = -2$ **et** en $x = 5$ (l'extrémité droite).
- g) La courbe monte de $x = 1$ à $x = 3$, puis continue de monter, plus vite, jusqu'à $x = 5$ : elle est croissante sur tout $[1 \;;\; 5]$. Elle monte aussi sur $[-4 \;;\; -2]$, mais cet intervalle est plus court.
- h) La courbe est au-dessus de $y = 2$ (ou dessus) de $-3$ à $-1$, puis de 4 à 5.

**Erreurs fréquentes.** Oublier les extrémités et les points anguleux (d, f) ; donner une ordonnée pour une question sur les $x$ (f) ; en g), s'arrêter au point anguleux $x = 3$ alors que la courbe continue de monter ; exclure des bornes où l'égalité $f(x) = 2$ a lieu (h).

**Variante.** Sur la même courbe, les solutions de $f(x) < 0$ ? *Réponse* : la courbe est sous l'axe entre $x = 0$ et $x = 3$, soit $]0 \;;\; 3[$.

### Ex R3.3 — La fonction affine qui passe par deux points

**Réponses** : a) `[2, -3]` · b) `[-2, 1]` · c) `[0.4, 4]` · d) `0.5` · e) `45` · f) `True` · g) `[1.2, 5]`.

**Démarche.**
- a) $m = \frac{9 - 1}{6 - 2} = 2$, $c = 1 - 2 \times 2 = -3$. Vérification : $2 \times 6 - 3 = 9$.
- b) $m = \frac{-1 - 7}{1 - (-3)} = \frac{-8}{4} = -2$, $c = -1 - (-2) \times 1 = 1$. Vérification : $-2 \times (-3) + 1 = 7$.
- c) $m = \frac{6 - 4}{5 - 0} = 0{,}4$, et $c = f(0) = 4$ se lit directement.
- d) $-2x + 1 = 0 \iff x = \frac{1}{2}$.
- e) $m = \frac{35 - 25}{30 - 10} = 0{,}5$, donc $f(50) = f(30) + 0{,}5 \times 20 = 45$.
- f) $2 \times 4 - 3 = 5$ : oui.
- g) $m = \frac{19{,}40 - 11}{12 - 5} = \frac{8{,}40}{7} = 1{,}20$ € par kilomètre, et $c = 11 - 1{,}2 \times 5 = 5$ € de prise en charge.

**Erreurs fréquentes.** Calculer $\frac{\Delta x}{\Delta y}$ ; mélanger l'ordre des points ; en e), croire $f$ proportionnelle ($5 \times 25 = 125$) ; en d), donner l'ordonnée à l'origine au lieu de la racine.

**Variante.** La fonction affine qui passe par $(1, -2)$ et $(4, 7)$ ? *Réponse* : $m = 3$, $c = -5$.

### Ex R3.4 — Ramener des données entre 0 et 1 avec une fonction affine (min-max)

**Réponses** : a) `[0.01, -0.2]` · b) `0.45` · c) `[100, 20]` · d) `100` · e) `[0.1, -2]`.

**Démarche.**
- a) $N(x) = \frac{x - 20}{120 - 20} = \frac{x - 20}{100} = 0{,}01\,x - 0{,}2$. Vérification : $N(20) = 0$, $N(120) = 1$.
- b) $N(65) = \frac{45}{100} = 0{,}45$.
- c) $y = \frac{x - 20}{100} \iff x = 100y + 20$.
- d) $100 \times 0{,}8 + 20 = 100$ m².
- e) $S(x) = 10 \times (0{,}01x - 0{,}2) = 0{,}1x - 2$.

**Erreurs fréquentes.** Diviser par le maximum au lieu de l'étendue (b : $\frac{65}{120}$) ; oublier d'ajouter le minimum en revenant en arrière (d : 80) ; en e), ne multiplier que la pente par 10.

**Variante.** Des notes de 40 à 90 ramenées entre 0 et 1 : que devient 65 ? *Réponse* : $\frac{65 - 40}{50} = 0{,}5$.

### Ex R3.5 — Variations et signe des fonctions de référence

**Réponses** : a) `"]-oo ; 0]"` · b) `"]-3 ; 3["` · c) `"]0 ; 0.5["` · d) `"[0 ; 9]"` · e) `"]-oo ; -2] U [2 ; +oo["` · f) `"[0 ; 4]"` · g) `True`.

**Démarche.**
- b) Le carré vaut 9 en $-3$ et en 3, et il est plus petit entre les deux.
- c) Pour $x < 0$, $\frac{1}{x} < 0 < 2$ : aucune solution. Pour $x > 0$, l'inverse est décroissant et vaut 2 en $\frac{1}{2}$ : $\frac{1}{x} > 2 \iff x < \frac{1}{2}$.
- d) Il faut $x \ge 0$, puis $\sqrt{x} \le 3 \iff x \le 9$ (la racine est croissante).
- e) Les points à au moins 2 de 0.
- f) Quand $x$ va de $-2$ à 1, $x^2$ descend de 4 à 0 (en $x = 0$), puis remonte à 1 : les valeurs prises vont de 0 à 4.
- g) $\frac{1}{-0{,}3} \approx -3{,}33$ et $\frac{1}{-0{,}2} = -5$ : oui, $-3{,}33 > -5$. L'inverse est décroissant sur les négatifs : $-0{,}3 < -0{,}2$ donne $\frac{1}{-0{,}3} > \frac{1}{-0{,}2}$.

**Erreurs fréquentes.** b) Oublier les négatifs ; c) inclure les négatifs, ou garder l'ordre ; f) répondre $[1 \;;\; 4]$ en ne calculant que les images des bornes.

**Variante.** L'ensemble des valeurs de $x^2$ pour $x \in [-4 \;;\; 2]$ ? *Réponse* : $[0 \;;\; 16]$ (le plus grand carré est en $x = -4$).

### Ex R3.6 — Forme canonique et sommet d'une parabole

**Réponses** : a) `[1, -3, -7]` · b) `[2, 3, -5]` · c) `[-1, 2, 5]` · d) `[-1, -5]` · e) `[2, 8, 11]` · f) `2`.

**Démarche.**
- a) $x^2 + 6x + 2 = (x + 3)^2 - 9 + 2 = (x + 3)^2 - 7$, donc $\alpha = -3$, $\beta = -7$.
- b) $2(x^2 - 6x) + 13 = 2\big[(x - 3)^2 - 9\big] + 13 = 2(x - 3)^2 - 5$.
- c) $-(x^2 - 4x) + 1 = -\big[(x - 2)^2 - 4\big] + 1 = -(x - 2)^2 + 5$.
- d) $\alpha = -\frac{6}{2 \times 3} = -1$ et $\beta = 3 - 6 - 2 = -5$.
- e) $2(x + 2)^2 + 3 = 2(x^2 + 4x + 4) + 3 = 2x^2 + 8x + 11$.
- f) $12 = a(3 - 1)^2 + 4 \iff 4a = 8 \iff a = 2$.

**Vérifier en redéveloppant** : pour b), $2(x^2 - 6x + 9) - 5 = 2x^2 - 12x + 13$.

**Erreurs fréquentes.** Prendre $\alpha$ avec le signe de la parenthèse ($(x + 3)^2$ donne $\alpha = -3$) ; oublier de multiplier par $a$ le carré retiré (b) ; se tromper de signe avec $a = -1$ (c).

**Variante.** La forme canonique de $x^2 - 10x + 18$ ? *Réponse* : $(x - 5)^2 - 7$.

### Ex R3.7 — Racines par le discriminant et factorisation

**Réponses** : a) `49` · b) `[-1/3, 2]` · c) `[3, -1/3, 2]` · d) `[3]` · e) `[]` · f) `[-2, 4]` · g) `"]-1/3 ; 2["`.

**Démarche.**
- a) $\Delta = (-5)^2 - 4 \times 3 \times (-2) = 25 + 24 = 49$.
- b) $x = \frac{5 \pm 7}{6}$ : $\frac{12}{6} = 2$ et $\frac{-2}{6} = -\frac{1}{3}$.
- c) $3\left(x + \frac{1}{3}\right)(x - 2)$, qu'on écrit aussi $(3x + 1)(x - 2)$.
- d) $\Delta = 36 - 36 = 0$ : racine double $\frac{6}{2} = 3$ ($x^2 - 6x + 9 = (x - 3)^2$).
- e) $\Delta = 1 - 40 = -39 < 0$ : aucune racine.
- f) $\Delta = 4 + 32 = 36$, $x = \frac{-2 \pm 6}{-2}$ : $\frac{4}{-2} = -2$ et $\frac{-8}{-2} = 4$.
- g) $a = 3 > 0$ : le polynôme est négatif strictement entre ses racines.

**Erreurs fréquentes.** $(-5)^2 = -25$ ; $-4ac$ avec $c < 0$ compté négatif ; $-b = -5$ au lieu de 5 ; en f), oublier que $2a = -2$ change les signes ; en g), prendre l'extérieur des racines.

**Variante.** Les racines de $2x^2 - x - 6$ ? *Réponse* : $\Delta = 1 + 48 = 49$, $x = \frac{1 \pm 7}{4}$ : 2 et $-1{,}5$.

### Ex R3.8 — Trouver le maximum d'une aire ou d'un bénéfice

**Réponses** : a) `200` · b) `10` · c) `[5, 15]` · d) `25` · e) `2500`.

**Démarche.**
- a) et b) Les deux côtés perpendiculaires au mur mesurent $x$, le troisième $40 - 2x$. L'aire vaut $A(x) = x(40 - 2x) = -2x^2 + 40x$, une parabole tournée vers le bas : son maximum est au sommet, $\alpha = -\frac{40}{2 \times (-2)} = 10$, et $A(10) = 10 \times 20 = 200$ m².
- c) $-2x^2 + 40x = 150 \iff x^2 - 20x + 75 = 0$, $\Delta = 400 - 300 = 100$, $x = \frac{20 \pm 10}{2}$ : 5 ou 15 (de part et d'autre du sommet, par symétrie).
- d) et e) La recette est $R(p) = p(200 - 4p) = -4p^2 + 200p$ ; sommet en $p = -\frac{200}{-8} = 25$ €, et $R(25) = 25 \times 100 = 2\,500$ €.

**Erreurs fréquentes.** Écrire l'aire $x(40 - x)$ ou $x(20 - x)$ (le mur ne compte pas) ; confondre la valeur de $x$ et l'aire ; ne garder qu'une solution en c).

**Variante.** Avec 60 m de grillage, l'aire maximale ? *Réponse* : $A(x) = x(60 - 2x)$, sommet en $x = 15$, aire 450 m².

### Ex R3.9 — Composer deux fonctions dans les deux ordres

**Réponses** : a) `5` · b) `9` · c) `[2, 0, -3]` · d) `[2, -16, 33]` · e) `[1, -8]` · f) `[-5, 4]` · g) `[9/4]` · h) `[-3, 13]`.

**Démarche.**
- a) $g(2) = 9$, puis $f(9) = 5$. b) $f(2) = -2$, puis $g(-2) = 9$.
- c) $f(g(x)) = (2x^2 + 1) - 4 = 2x^2 - 3$.
- d) $g(f(x)) = 2(x - 4)^2 + 1 = 2(x^2 - 8x + 16) + 1 = 2x^2 - 16x + 33$.
- e) $f(f(x)) = (x - 4) - 4 = x - 8$.
- f) L'intérieur, calculé en premier, est $v(x) = 4 - 5x = -5x + 4$ : pente $-5$, ordonnée à l'origine 4.
- g) $2x^2 - 16x + 33 = 2x^2 - 3 \iff 16x = 36 \iff x = \frac{9}{4}$.
- h) $p(q(x)) = 3(-x + 5) - 2 = -3x + 13$ : encore une fonction affine, de pente $3 \times (-1)$. **Une composée de fonctions affines est affine** : c'est pourquoi un réseau de neurones a besoin d'activations non linéaires (fiche §7).

**Erreurs fréquentes.** Appliquer $f$ d'abord pour $f \circ g$ ; oublier le double produit de $(x - 4)^2$ ; prendre $f \circ f$ pour $f(x) \times f(x)$.

**Variante.** Avec $f(x) = x + 2$ et $g(x) = x^2 - 1$, $(g \circ f)(x)$ ? *Réponse* : $(x + 2)^2 - 1 = x^2 + 4x + 3$.

### Ex R3.10 — Trouver une réciproque et son ensemble de définition

**Réponses** : a) `[0.25, 0.75]` · b) `3` · c) `1.5` · d) `"]-oo ; 0[ U ]0 ; +oo["` · e) `"[3 ; +oo["` · f) `2` · g) `False`.

**Démarche.**
- a) $y = 4x - 3 \iff x = \frac{y + 3}{4} = 0{,}25y + 0{,}75$.
- b) $f^{-1}(9) = \frac{12}{4} = 3$ ; vérification : $f(3) = 9$.
- c) $y = \frac{2}{x - 1} \iff x - 1 = \frac{2}{y} \iff x = 1 + \frac{2}{y}$ (pour $y \ne 0$), donc $g^{-1}(4) = 1{,}5$ ; vérification : $g(1{,}5) = \frac{2}{0{,}5} = 4$.
- d) $g$ ne prend jamais la valeur 0 (une fraction de numérateur 2 n'est jamais nulle), et elle prend toutes les autres : pour $y \ne 0$, $x = 1 + \frac{2}{y}$ existe, est différent de 1, et vérifie $g(x) = y$. Les valeurs prises par $g$ sont donc tous les réels non nuls, et $g^{-1}$ est définie pour $y \ne 0$.
- e) Pour $x \ge 0$, $x^2 + 3$ prend toutes les valeurs à partir de 3.
- f) $x^2 + 3 = 7$ avec $x \ge 0$ : $x = 2$.
- g) Non : 4 a deux antécédents, $-2$ et $2$.

**Erreurs fréquentes.** Confondre $f^{-1}(9)$ et $f(9)$ ; prendre l'ensemble de définition de $g$ pour celui de $g^{-1}$ ; oublier la restriction $x \ge 0$ en f) (qui élimine $-2$).

**Variante.** La réciproque de $f(x) = \frac{x - 1}{3}$ ? *Réponse* : $f^{-1}(y) = 3y + 1$.

### Ex R3.11 — Fonctions par morceaux et argmax : max(0, x), |x|, la marche, et où une fonction atteint son maximum

**Réponses** : a) `0` · b) `3` · c) `"]-oo ; 0]"` · d) `1` · e) `"abs(x)"` (ou `"|x|"`) · f) `2` · g) `3` · h) `2`.

**Démarche.**
- a) $-2{,}5 < 0$, donc $r(-2{,}5) = 0$. b) $3 + 0 = 3$.
- c) $r(x) = 0$ pour tous les $x \le 0$, 0 compris.
- d) $H(0) = 1$ par convention, $H(-0{,}1) = 0$ : la somme vaut 1.
- e) Pour $x \ge 0$ : $x + 0 = x$ ; pour $x < 0$ : $0 + (-x) = -x$. C'est la définition de $|x|$.
- f) et g) $q$ a son sommet en $x = 2$ ($a = -1 < 0$, un maximum), hors de $[3 \;;\; 6]$. À droite du sommet, $q$ est décroissante : sur $[3 \;;\; 6]$, son maximum est en $x = 3$, et vaut $q(3) = -1 + 3 = 2$.
- h) Le maximum 9 est aux positions 2 et 4 ; NumPy rend la première, 2.

**Erreurs fréquentes.** f) répondre 3, le maximum de $q$ sur $\mathbb{R}$ (atteint hors de l'intervalle) ; g) répondre 2, l'abscisse du sommet ; h) compter à partir de 1, ou donner la valeur 9.

**Variante.** Le maximum de $q$ sur $[0 \;;\; 1]$ ? *Réponse* : $q$ est croissante sur $[0 \;;\; 1]$ (à gauche du sommet) : maximum $q(1) = 2$, atteint en $x = 1$.

### Ex R3.12 — Évaluer un polynôme par le schéma de Horner

**Réponses** : a) `7` · b) `[2, 1, 6, 7]` · c) `-5` · d) `4`.

**Démarche.**
- a) et b) $2$ ; $2 \times 2 - 3 = 1$ ; $1 \times 2 + 4 = 6$ ; $6 \times 2 - 5 = 7$. Vérification : $16 - 12 + 8 - 5 = 7$.
- c) Coefficients $[1, 0, -2, 3, -1]$ : $1$ ; $1 \times (-1) + 0 = -1$ ; $-1 \times (-1) - 2 = -1$ ; $-1 \times (-1) + 3 = 4$ ; $4 \times (-1) - 1 = -5$. Vérification : $1 - 2 - 3 - 1 = -5$.
- d) Une multiplication par étape après le premier coefficient : 4 (contre $4 + 3 + 2 + 1 = 10$ si l'on calcule chaque puissance en multipliant).

**Erreurs fréquentes.** Oublier le coefficient nul de $x^3$ (on trouve $-7$) ; ajouter sans multiplier.

**Variante.** $p(-1)$ par Horner ? *Réponse* : $2$ ; $-5$ ; $9$ ; $-14$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R3.13 — Démontrer la formule des racines du second degré

**Démonstration.**
1. On développe le membre de droite : $\left(x + \frac{b}{2a}\right)^2 = x^2 + \frac{b}{a}x + \frac{b^2}{4a^2}$, donc le crochet vaut $x^2 + \frac{b}{a}x + \frac{b^2 - \Delta}{4a^2} = x^2 + \frac{b}{a}x + \frac{4ac}{4a^2} = x^2 + \frac{b}{a}x + \frac{c}{a}$. Multiplié par $a$, il donne $ax^2 + bx + c$.
2. Si $\Delta < 0$, alors $-\frac{\Delta}{4a^2} > 0$ ($4a^2 > 0$). Le crochet est la somme d'un carré ($\ge 0$) et d'un nombre strictement positif : il est strictement positif, donc jamais nul. Comme $a \ne 0$, le produit $a \times [\ldots]$ n'est jamais nul : aucune racine réelle.
3. Si $\Delta = 0$, alors $ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2$, nul si et seulement si $x + \frac{b}{2a} = 0$ (car $a \ne 0$) : une seule solution, $x = -\frac{b}{2a}$.
4. Si $\Delta > 0$, $\sqrt{\Delta}$ existe et $\frac{\Delta}{4a^2} = \left(\frac{\sqrt{\Delta}}{2a}\right)^2$. Avec $u = x + \frac{b}{2a}$ et $v = \frac{\sqrt{\Delta}}{2a}$, le crochet vaut $u^2 - v^2 = (u - v)(u + v) = \left(x - \frac{-b + \sqrt{\Delta}}{2a}\right)\left(x - \frac{-b - \sqrt{\Delta}}{2a}\right)$. Donc $ax^2 + bx + c = a(x - x_1)(x - x_2)$, nul si et seulement si $x = x_1$ ou $x = x_2$ (produit nul, R2 §4) ; ces deux nombres sont distincts car $\sqrt{\Delta} \ne 0$.
5. $x_1 + x_2 = \frac{-b - \sqrt{\Delta} - b + \sqrt{\Delta}}{2a} = -\frac{b}{a}$ et $x_1 x_2 = \frac{(-b)^2 - (\sqrt{\Delta})^2}{4a^2} = \frac{b^2 - \Delta}{4a^2} = \frac{4ac}{4a^2} = \frac{c}{a}$. Pour R3.7 b : $-\frac{1}{3} + 2 = \frac{5}{3} = -\frac{-5}{3}$ et $-\frac{1}{3} \times 2 = -\frac{2}{3} = \frac{-2}{3}$ : les deux relations sont vérifiées.

**Grille de relecture.**
- 1 est un calcul complet, qui fait apparaître $b^2 - \Delta = 4ac$.
- 2 dit **pourquoi** le crochet est strictement positif (un carré plus un nombre strictement positif) et utilise $a \ne 0$.
- 3 et 4 concluent avec la règle du produit nul ; 4 cite l'identité $u^2 - v^2$ et justifie l'écriture $\frac{\Delta}{4a^2}$ comme un carré.
- 5 calcule la somme et le produit, puis les **utilise** comme contrôle.

**Erreurs fréquentes.** Partir de la formule des racines pour la « démontrer » ; écrire $\sqrt{\frac{\Delta}{4a^2}} = \frac{\sqrt{\Delta}}{2a}$ sans remarquer qu'il suffit d'écrire $\frac{\Delta}{4a^2}$ comme le carré de $\frac{\sqrt{\Delta}}{2a}$ (le signe de $a$ n'a pas d'importance pour un carré).

**Variante.** Deux nombres ont pour somme 7 et pour produit 10 : lesquels ? *Réponse* : ce sont les racines de $x^2 - 7x + 10$, soit 2 et 5.

### Ex R3.14 — Une fonction affine de pente positive est croissante

**Démonstration.**
1. $f(b) - f(a) = (mb + c) - (ma + c) = m(b - a)$. Avec $m > 0$ et $b - a > 0$, ce produit est strictement positif : $f(a) < f(b)$. Donc $f$ est strictement croissante sur $\mathbb{R}$.
2. Si $m < 0$, $m(b - a) < 0$ : $f(a) > f(b)$, $f$ est strictement décroissante. Si $m = 0$, $f(b) - f(a) = 0$ : $f$ est constante.
3. Si $f$ est croissante, $0 < 1$ donne $f(0) \le f(1)$, soit $c \le m + c$, donc $m \ge 0$.
4. Pour $0 \le a < b$ : $b > 0$, donc $\sqrt{b} > 0$ et $\sqrt{b} + \sqrt{a} > 0$ (on peut diviser). Et $(\sqrt{b} - \sqrt{a})(\sqrt{b} + \sqrt{a}) = b - a$ (identité remarquable), d'où $\sqrt{b} - \sqrt{a} = \frac{b - a}{\sqrt{b} + \sqrt{a}}$, quotient de deux nombres strictement positifs : $\sqrt{a} < \sqrt{b}$.
5. Soient $a < b$. Si $g$ est croissante, $g(a) \le g(b)$. Deux cas : si $g(a) = g(b)$, alors $f(g(a)) = f(g(b))$ ; si $g(a) < g(b)$, $f$ croissante donne $f(g(a)) \le f(g(b))$. Dans les deux cas, $f(g(a)) \le f(g(b))$ : $f \circ g$ est croissante. Si $g$ est décroissante, $g(a) \ge g(b)$, et le même raisonnement (égalité, ou inégalité stricte que $f$ croissante conserve au sens large) donne $f(g(a)) \ge f(g(b))$ : $f \circ g$ est décroissante.

**Grille de relecture.**
- Chaque question part de la **définition** (deux nombres $a < b$ quelconques) et étudie un signe ou un ordre.
- 1 factorise $f(b) - f(a)$ par $m$ et cite la règle des signes.
- 3 choisit deux valeurs précises et en déduit une condition sur $m$.
- 4 justifie que le dénominateur n'est pas nul **avant** de diviser.
- 5 enchaîne les deux comparaisons dans le bon ordre, $g$ d'abord puis $f$, et traite le cas où $g(a) = g(b)$ (la définition de « croissante » ne parle que de nombres distincts).

**Erreurs fréquentes.** Vérifier sur deux exemples au lieu de prendre $a$ et $b$ quelconques ; oublier le cas $a = 0$ en 4 (alors $\sqrt{a} = 0$, et c'est $\sqrt{b} > 0$ qui empêche la division par 0).

**Variante.** Montre que $x \mapsto \frac{1}{x}$ est strictement décroissante sur $]0 \;;\; +\infty[$. *Réponse* : pour $0 < a < b$, $\frac{1}{b} - \frac{1}{a} = \frac{a - b}{ab}$, négatif sur positif : $\frac{1}{b} < \frac{1}{a}$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R3.15 — Une fonction de coût donnée par une formule : une parabole et son sommet

**Réponses** : a) `15` · b) `30` · c) `7` · d) `"[0 ; 30]"` · e) `"[20 ; 40]"`.

**Démarche.**
- a) $E(10) = 0{,}02 \times 100 - 12 + 25 = 15$ %.
- b) et c) $\alpha = -\frac{-1{,}2}{2 \times 0{,}02} = \frac{1{,}2}{0{,}04} = 30$ epochs, et $E(30) = 18 - 36 + 25 = 7$ %.
- d) $a > 0$ : $E$ décroît jusqu'au sommet, puis croît : $[0 \;;\; 30]$.
- e) $E(t) \le 9 \iff 0{,}02t^2 - 1{,}2t + 16 \le 0 \iff t^2 - 60t + 800 \le 0$ (en multipliant par 50). $\Delta = 3600 - 3200 = 400$, racines $\frac{60 \pm 20}{2}$ : 20 et 40. Le polynôme est négatif entre ses racines : $[20 \;;\; 40]$.

**Ce que dit la remontée.** Après 30 epochs, l'erreur de validation augmente alors que l'entraînement continue : le modèle commence à apprendre des détails propres aux données d'entraînement, qui ne se retrouvent pas sur de nouvelles données (l'overfitting, chapitre 9 de workbookIA). Une ingénieure arrêterait l'entraînement vers le minimum, ou garderait la version du modèle qui l'atteint (l'early stopping). Sur des mesures réelles, la courbe est bruitée : la parabole n'en est qu'un modèle simplifié.

**Erreurs fréquentes.** Confondre l'argmin (30) et le minimum (7) ; en e), prendre l'extérieur des racines, ou exclure les bornes (« ne dépasse pas » veut dire $\le$).

**Variante.** Pour quels $t$ l'erreur est-elle inférieure à 15 % ? *Réponse* : $t^2 - 60t + 500 < 0$, racines 10 et 50 : $]10 \;;\; 50[$.

### Ex R3.16 — Expliquer ce qu'est une fonction à quelqu'un qui n'aime pas les maths

**Exemple de réponse.**

> Une fonction, c'est une machine : tu mets quelque chose dedans, elle te rend un résultat, toujours le même pour la même entrée. Le tarif d'une lettre en est une : un poids donne un prix. Ta taille à chaque anniversaire aussi : un âge donne une taille. La seule règle, c'est qu'une entrée donne **une seule** sortie. « À chaque date, la personne née ce jour-là » n'est pas une fonction, puisque beaucoup de gens sont nés le même jour. Et un antécédent, c'est le chemin inverse : connaissant le prix payé, retrouver le poids de la lettre (il peut y avoir plusieurs poids pour un même prix).

**Grille.** Une bonne réponse : (1) une image concrète (machine, tarif, recette) ; (2) un exemple de la vie courante ; (3) la règle « une seule sortie par entrée » **et** un contre-exemple ; (4) l'antécédent comme chemin inverse, qui peut avoir plusieurs réponses ; (5) huit lignes au plus, sans jargon.

<a id="notebook"></a>

## Notebook

### Ex R3.21 — Tracer et lire les fonctions de référence

**Réponses** : a) `"]0 ; 1["` · b) `"]-oo ; 0[ U ]1 ; +oo["` · c) `[-1, 1]`.

**Démarche.** a) Pour $x > 0$ : $\sqrt{x} > x \iff x > x^2$ (on élève au carré deux nombres positifs) $\iff x(1 - x) > 0 \iff 0 < x < 1$. b) $x^2 - x = x(x - 1) > 0$ quand les deux facteurs ont le même signe : $x < 0$ ou $x > 1$. c) $\frac{1}{x} = x \iff x^2 = 1$ ($x \ne 0$) : $x = -1$ ou $x = 1$.

**Erreurs fréquentes.** Relier les deux branches de $\frac{1}{x}$ par un trait vertical (un seul tracé sur $[-3 \;;\; 3]$) ; répondre b) d'après la seule figure de gauche, qui ne montre pas les négatifs.

### Ex R3.26 — Un graphique propre : titre, axes, légende

**Ce qu'on attend.** La parabole $C$ sur $[0 \;;\; 40]$, la droite du budget, le minimum $(20 \;;\; 100)$ marqué et annoté, un titre, des axes nommés **avec unités** (tonnes, milliers d'euros), une légende et une grille. Le budget est respecté de 10 à 30 tonnes : $q^2 - 40q + 300 \le 0$ entre les racines 10 et 30.

**Erreurs fréquentes.** Dessiner avec `plt.plot` dans une autre figure au lieu de l'axe `ax` donné ; oublier les unités ; une légende sans `label=` dans les tracés.

### Ex R3.18 — La fonction affine qui passe par deux points · `affine_from_points`

**Réponses** : `affine_from_points((-1, 4), (3, -4))` vaut `(-2.0, 2.0)` ; deux points de même abscisse lèvent `ValueError`.

**Démarche.** $m = \frac{-4 - 4}{3 - (-1)} = -2$, $c = 4 - (-2) \times (-1) = 2$. En code : le test `x1 == x2` **avant** la division, puis `return (float(m), float(y1 - m * x1))`.

**Erreurs fréquentes.** Diviser avant de tester (`ZeroDivisionError`) ; rendre `(c, m)` ; rendre des entiers quand le calcul tombe juste (les tests demandent des flottants).

**Variante.** `affine_from_points((0, 1), (4, 0))` ? *Réponse* : `(-0.25, 1.0)`.

### Ex R3.19 — Racines et sommet d'un polynôme du second degré · `quadratic_roots`, `quadratic_vertex`

**Réponses** : `quadratic_roots(-2, 7, -3)` vaut `[0.5, 3.0]` (avec `a` négatif, les racines doivent quand même être triées) ; `quadratic_roots(1, 2, 3)` vaut `[]` ; `quadratic_vertex(-1, 6, -5)` vaut `(3.0, 4.0)`.

**Démarche.** $\Delta = 49 - 24 = 25$, racines $\frac{7 \pm 5}{4}$ : 0,5 et 3. Pour $x^2 + 2x + 3$, $\Delta = 4 - 12 < 0$. Pour $-x^2 + 6x - 5$ : $\alpha = -\frac{6}{-2} = 3$ et $\beta = -5 - \frac{36}{-4} = 4$.

**Erreurs fréquentes.** Écrire `-b + root / 2 * a` (priorités : c'est `(-b + root) / (2 * a)`) ; ne pas trier les racines quand `a < 0` ; comparer le discriminant à 0 avec une tolérance au lieu de `==` (les tests de la racine double utilisent des entiers) ; oublier `import math`.

**Variante.** `quadratic_roots(4, -4, 1)` ? *Réponse* : `[0.5]`, une racine double.

### Ex R3.22 — Faire varier a, b et c : déformer une parabole

**Ce qu'on attend.** $a$ ouvre ou ferme la parabole, et la retourne s'il est négatif ; $c$ la translate verticalement ; $h$ la translate horizontalement (vers la droite quand $h > 0$). Donc $y = 2(x - 3)^2 - 1$ est la parabole $y = x^2$ resserrée d'un facteur 2, décalée de 3 vers la droite et de 1 vers le bas, de sommet $(3 \;;\; -1)$. Le coefficient $b$ ne se lit pas directement : il déplace le sommet en biais, en changeant à la fois $\alpha = -\frac{b}{2a}$ et $\beta$. C'est l'intérêt de la forme canonique.

### Ex R3.24 — Combien de racines ? Le signe du discriminant sur une grille de paramètres

**Réponses** : a) `[85, 5, 31]` · b) `"b**2/4"`.

**Démarche.** Pour $a = 1$, $\Delta = b^2 - 4c$. Une racine quand $c = \frac{b^2}{4}$ est entier, donc pour $b$ pair : $(-4, 4)$, $(-2, 1)$, $(0, 0)$, $(2, 1)$, $(4, 4)$, soit 5 polynômes. Sous la parabole $c = \frac{b^2}{4}$ : deux racines (85) ; au-dessus : aucune (31).

**Erreurs fréquentes.** `range(-5, 5)`, qui oublie 5 ; la frontière $c = b^2$ (oublier le 4).

### Ex R3.20 — Composer deux fonctions · `compose`

**Réponse** : `[9, 15]` : $(4 - 1)^2 = 9$ et $4^2 - 1 = 15$.

**Démarche.** `def composite(x): return f(g(x))`, puis `return composite`. La fonction intérieure « se souvient » de `f` et de `g` : c'est une fermeture.

**Erreurs fréquentes.** Rendre `f(g)` ou `composite(x)` ; appliquer `f` d'abord (on obtient `[15, 9]`).

### Ex R3.23 — Prédire f∘g et g∘f pour « valeur absolue » et « moins 3 »

**Réponses** : a) `2` · b) `-2` · c) `5` · d) `-1`.

**Démarche.** $(f \circ g)(x) = |x - 3|$ et $(g \circ f)(x) = |x| - 3$ : $|1 - 3| = 2$, $|1| - 3 = -2$, $|-2 - 3| = 5$, $|-2| - 3 = -1$. Les deux composées coïncident pour $x \ge 3$.

### Ex R3.25 — Chasse à l'erreur : composition, réciproque et racines

**Réponses** : a) `"ABCFG"` · b) `[5, 0, -1]` · c) `[-3, 5]` · d) `41` · e) `[-0.5, 1.5]`.

**Démarche.**
- A : $f(g(x)) = 5x^2 - 1$ ; $(5x - 1)^2$ est $(g \circ f)(x)$.
- B : $f^{-1}(x) = \frac{x + 1}{5}$ ; $\frac{1}{5x - 1}$ est l'inverse.
- C : $\Delta = 4 + 60 = 64$, racines $\frac{2 \pm 8}{2}$ : 5 et $-3$ (les signes ont été inversés).
- D est juste : $3(x^2 + 2x + 1) - 2 = 3x^2 + 6x + 1$.
- E est juste : une fonction affine de pente $-1$.
- F : $\Delta = 9 - 4 \times 2 \times (-4) = 9 + 32 = 41$.
- G : $\frac{4 \pm 8}{8}$, soit 1,5 et $-0{,}5$ : c'est tout le numérateur qui est divisé par $2a = 8$.

### Ex R3.17 — Évaluer un polynôme par Horner · `polyval`

**Réponses** : `polyval([1, -2, 0, 3], -2)` vaut `-13` ; `polyval([0.5, 1], 4)` vaut `3.0`.

**Démarche.** $1$ ; $1 \times (-2) - 2 = -4$ ; $-4 \times (-2) + 0 = 8$ ; $8 \times (-2) + 3 = -13$. En code : `result = 0`, puis `result = result * x + coefficient` pour chaque coefficient.

**Erreurs fréquentes.** Parcourir les coefficients à l'envers (on calcule un autre polynôme) ; partir de `result = 1` ; calculer des puissances avec `**` (juste, mais ce n'est plus Horner).

**Variante.** `polyval([3, 0, 0, -1], 2)` ? *Réponse* : $3 \times 8 - 1 = 23$.
