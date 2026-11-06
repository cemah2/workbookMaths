# R9 · Géométrie du plan, vecteurs et trigonométrie — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r9_geometrie_vecteurs/06_mes_reponses.md` (créée par `python tools/start_chapter.py R9`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂ et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Dessine chaque point et chaque vecteur sur papier quadrillé avant de calculer, et garde les valeurs exactes ($\sqrt{13}$, $\frac{\sqrt{3}}{2}$, $\frac{3\pi}{4}$) jusqu'au bout.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R9.Q1 — Coordonnées et distance 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Dans quel quadrant se trouve le point $(-3 ; 2)$ : en haut à droite, en haut à gauche, en bas à gauche ou en bas à droite ?
2. Quelles sont les coordonnées du milieu de $[AB]$, avec $A(-4 ; 7)$ et $B(2 ; -1)$ ?
3. Quelle est la distance entre $(2 ; 5)$ et $(2 ; -3)$ ?
4. Vrai ou faux : la distance de $A$ à $B$ est égale à celle de $B$ à $A$.
5. Vrai ou faux : $AB = \lvert x_B - x_A \rvert + \lvert y_B - y_A \rvert$.
6. Le point $M(1 ; 1)$ est-il plus proche de l'origine que le point $N(0 ; 1{,}5)$ ?

### R9.Q2 — Vecteurs : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §2 et §3 · parcours C, E*

Vrai ou faux ?
1. Si $\overrightarrow{AB} = \overrightarrow{DC}$, alors $ABCD$ est un parallélogramme.
2. $(2 ; -6)$ et $(-1 ; 3)$ sont colinéaires.
3. $\lVert \vec{u} + \vec{v} \rVert = \lVert \vec{u} \rVert + \lVert \vec{v} \rVert$ pour tous vecteurs $\vec{u}$ et $\vec{v}$.
4. $\lVert -3\vec{u} \rVert = -3\,\lVert \vec{u} \rVert$.
5. $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ pour tous points $A$, $B$ et $C$.
6. Un vecteur unitaire a toutes ses coordonnées égales à 1.

### R9.Q3 — Pente et vecteur directeur 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Quelle est la pente de la droite $y = -2x + 5$ ?
2. Donne un vecteur directeur de la droite $y = 3x - 1$.
3. Vrai ou faux : $(5 ; 2)$ est un vecteur directeur de la droite $2x - 5y + 1 = 0$.
4. La droite $x = 4$ a-t-elle une pente ?
5. Les droites $y = 2x + 1$ et $4x - 2y + 7 = 0$ sont-elles parallèles ?
6. Le point $(1 ; 2)$ est-il sur la droite $3x - y - 1 = 0$ ?

### R9.Q4 — Le signe du produit scalaire 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Si $\vec{u} \cdot \vec{v} > 0$, l'angle entre $\vec{u}$ et $\vec{v}$ est-il aigu ou obtus ?
2. Que vaut $(1 ; 2) \cdot (-2 ; 1)$ ? Que peut-on en dire ?
3. Vrai ou faux : $\vec{u} \cdot \vec{u}$ peut être négatif.
4. Le produit scalaire de deux vecteurs est-il un nombre ou un vecteur ?
5. Vrai ou faux : $(3\vec{u}) \cdot \vec{v} = 3\,(\vec{u} \cdot \vec{v})$.
6. Vrai ou faux : si $\vec{u} \cdot \vec{v} = 0$ et $\vec{u} \ne \vec{0}$, alors $\vec{v} = \vec{0}$.

### R9.Q5 — Radians et valeurs remarquables 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Combien vaut 90° en radians ?
2. Combien vaut $\frac{\pi}{4}$ radian en degrés ?
3. Que valent $\cos 0$ et $\sin 0$ ?
4. Que vaut $\sin\frac{\pi}{2}$ ?
5. Vrai ou faux : il existe un angle $\theta$ tel que $\cos\theta = 1{,}5$.
6. Lequel vaut $\frac{1}{2}$ : $\cos\frac{\pi}{3}$ ou $\sin\frac{\pi}{3}$ ?

### R9.Q6 — Le cosinus de deux vecteurs 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Si la similarité cosinus de $\vec{u}$ et $\vec{v}$ vaut 0, que dire des deux vecteurs ?
2. Et si elle vaut $-1$ ?
3. Vrai ou faux : l'angle entre deux vecteurs non nuls est toujours compris entre 0 et $\pi$.
4. La similarité cosinus de deux vecteurs vaut 0,9 : leur angle est-il petit, ou proche de 90° ?
5. Combien vaut $\arccos 0$, en radians ?
6. Peut-on calculer l'angle entre un vecteur et le vecteur nul ?

### R9.Q7 — Combien de composantes ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

1. Combien de coordonnées a un point de l'espace ?
2. Quelle est la norme de $(1, 1, 1, 1)$ ?
3. Peut-on calculer le produit scalaire de $(1, 2, 3)$ et $(4, 5)$ ?
4. Une image en niveaux de gris de 20 × 30 pixels, mise à plat, est un vecteur de combien de coordonnées ?
5. Vrai ou faux : dans $\mathbb{R}^5$, deux vecteurs de produit scalaire nul sont dits orthogonaux.
6. Quelle est la distance entre $(1, 0, 0)$ et $(0, 1, 0)$ ?

<a id="rappels"></a>

## 🔁 Rappels

### R9.R1 — Fonctions affines (R3) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

La droite $d$ passe par $(-1 ; 1)$ et $(2 ; 7)$.
1. Sa pente ?
2. Son ordonnée à l'origine ?
3. L'abscisse du point où elle coupe l'axe des abscisses ?
4. La fonction affine $f(x) = 0{,}5x - 3$ est-elle croissante ou décroissante ?

### R9.R2 — Racines carrées (R1) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Écris $\sqrt{50}$ sous la forme $a\sqrt{b}$, avec $b$ le plus petit possible.
2. $\sqrt{12} \times \sqrt{3}$ ?
3. Écris $\frac{1}{\sqrt{2}}$ sans racine au dénominateur.
4. Compare $\sqrt{49 + 576}$ et $\sqrt{49} + \sqrt{576}$.

### R9.R3 — Dériver une composée (R7) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C*

1. La dérivée de $x \mapsto (3x + 1)^2$ ?
2. La dérivée de $x \mapsto e^{-2x}$ ?
3. Si $g(t) = f(5t)$, que vaut $g'(t)$, en fonction de $f'$ ?
4. Sachant que la dérivée de $\sin$ est $\cos$, quelle est la dérivée de $t \mapsto \sin(4t)$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/9"` ;
- une valeur exacte entre guillemets, avec `sqrt` et `pi`, comme `"sqrt(5)/3"` ou `"2*pi/5"` ;
- des coordonnées, une liste ou une équation par une liste entre crochets, comme `[-1.25, 1]` ; vrai ou faux par `True` ou `False`.

### Ex R9.1 — Coordonnées et distance ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des distances et des milieux dans un repère, et reconnaître un triangle rectangle.
**Prérequis :** fiche §1 ; R1 (racines carrées) · **Parcours :** C, E

On donne $A(-3 ; 2)$, $B(6 ; 14)$ et $C(5 ; -4)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les coordonnées du milieu de $[AB]$ | une liste |
| b | $AB$ | un entier |
| c | $AC$ | un entier |
| d | $BC$ | un nombre (2 décimales) |
| e | le triangle $ABC$ est-il rectangle en $A$ ? | vrai ou faux |
| f | la distance de l'origine $O$ au point $B$ | un nombre (2 décimales) |
| g | l'abscisse du point $M$ de l'axe des abscisses tel que $MA = MB$ | une fraction irréductible |
| h | les coordonnées du point $A'$ tel que $B$ soit le milieu de $[AA']$ | une liste |

### Ex R9.2 — Vecteurs : somme, différence, produit par un nombre ✏️ ★ ⏱️ 15 min
**Objectif :** calculer avec les coordonnées de vecteurs, et s'en servir pour placer des points.
**Prérequis :** fiche §2 · **Parcours :** C, E

On donne $\vec{u} = (4 ; -1)$, $\vec{v} = (-2 ; 3)$, et les points $A(1 ; 2)$ et $B(-3 ; 5)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\vec{u} + \vec{v}$ | une liste |
| b | $\vec{u} - \vec{v}$ | une liste |
| c | $3\vec{u} - 2\vec{v}$ | une liste |
| d | $\overrightarrow{AB}$ | une liste |
| e | le point $C$ tel que $\overrightarrow{AC} = \vec{u}$ | une liste |
| f | le point $D$ tel que $ABCD$ soit un parallélogramme | une liste |
| g | $\vec{u}$ et $\vec{w} = (-6 ; 1{,}5)$ sont-ils colinéaires ? | vrai ou faux |
| h | le nombre $k$ tel que $k\vec{v} = (5 ; -7{,}5)$ | un nombre |

### Ex R9.3 — Normes (euclidienne, avec un aperçu de L1 et L∞) et vecteurs unitaires ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des normes, normaliser un vecteur, et comparer la norme euclidienne aux normes L1 et L∞.
**Prérequis :** fiche §3 · **Parcours :** C, E

On donne $\vec{u} = (5 ; -3)$ et $\vec{v} = (-7 ; 24)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert \vec{u} \rVert$ | un nombre (2 décimales) |
| b | $\lVert \vec{u} \rVert_1$ | un entier |
| c | $\lVert \vec{u} \rVert_\infty$ | un entier |
| d | $\lVert -2\vec{u} \rVert$ | un nombre (2 décimales) |
| e | le vecteur unitaire de même direction et de même sens que $\vec{v}$ | une liste (2 décimales) |
| f | les valeurs de $t$ telles que $\lVert (t ; 2) \rVert = \sqrt{13}$ | une liste, dans l'ordre croissant |
| g | $\lVert \vec{u} + \vec{v} \rVert$ | un nombre (1 décimale) |
| h | la distance L1 (la norme L1 de $\overrightarrow{PQ}$) entre $P(-1 ; 4)$ et $Q(3 ; -2)$ | un entier |

### Ex R9.4 — Équations de droites ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire l'équation réduite et une équation cartésienne d'une droite, et s'en servir.
**Prérequis :** fiche §4 ; R3 (fonctions affines) · **Parcours :** C, E

On donne $A(-1 ; 4)$ et $B(3 ; -2)$. Une équation cartésienne $ax + by + c = 0$ se donne par la liste $[a, b, c]$.

| | Question | Réponse attendue |
|---|---|---|
| a | la pente $m$ de la droite $(AB)$ | un nombre |
| b | son ordonnée à l'origine $p$ | un nombre |
| c | le vecteur directeur de $(AB)$ dont la première coordonnée vaut 2 | une liste |
| d | l'équation cartésienne de $(AB)$ dont le coefficient $a$ vaut 3 | une liste $[a, b, c]$ |
| e | la pente de la droite $4x - 6y + 9 = 0$ | une fraction irréductible |
| f | l'ordonnée à l'origine de la parallèle à $(AB)$ qui passe par $C(2 ; 1)$ | un nombre |
| g | le point commun à $(AB)$ et à la droite $y = x$ | une liste |
| h | l'équation cartésienne de la droite qui passe par $D(-2 ; 5)$ et $E(-2 ; -1)$, avec $a = 1$ | une liste $[a, b, c]$ |

### Ex R9.5 — Le produit scalaire en coordonnées ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des produits scalaires et utiliser leurs règles de calcul.
**Prérequis :** fiche §5 · **Parcours :** C, E

On donne $\vec{u} = (2 ; 5)$, $\vec{v} = (-3 ; 1)$ et $\vec{w} = (6 ; 3)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\vec{u} \cdot \vec{v}$ | un entier |
| b | $\vec{u} \cdot \vec{w}$ | un entier |
| c | $\vec{v} \cdot \vec{w}$ | un entier |
| d | $\vec{u} \cdot \vec{u}$ | un entier |
| e | $(\vec{u} + \vec{v}) \cdot \vec{w}$ | un entier |
| f | $(2\vec{u}) \cdot (-3\vec{v})$ | un entier |
| g | le nombre $t$ tel que $(t ; 4)$ soit orthogonal à $\vec{u}$ | un nombre |
| h | l'angle entre $\vec{u}$ et $\vec{w}$ est-il aigu ? | vrai ou faux |

### Ex R9.6 — Orthogonalité et projections simples ✏️ ★★ ⏱️ 20 min
**Objectif :** reconnaître des vecteurs orthogonaux, et projeter un vecteur sur une direction.
**Prérequis :** fiche §5 · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | $(6 ; -4)$ et $(2 ; 3)$ sont-ils orthogonaux ? | vrai ou faux |
| b | le vecteur orthogonal à $(5 ; -2)$ dont la première coordonnée vaut 4 | une liste |
| c | le nombre $k$ tel que $(k ; 2)$ et $(3 ; k + 1)$ soient orthogonaux | un nombre |
| d | avec $A(1 ; 1)$, $B(5 ; 3)$ et $C(0 ; 3)$, le triangle $ABC$ est-il rectangle en $A$ ? | vrai ou faux |
| e | la longueur de la projection de $\vec{v} = (5 ; 5)$ sur la direction de $\vec{u} = (3 ; 1)$ | un nombre (2 décimales) |
| f | le vecteur projeté $\vec{p}$ de $\vec{v}$ sur la direction de $\vec{u}$ | une liste |
| g | le reste $\vec{v} - \vec{p}$ | une liste |
| h | les droites $y = 2x + 1$ et $y = -0{,}5x + 3$ sont-elles perpendiculaires ? | vrai ou faux |

Dans ta copie : vérifie que le reste de g est orthogonal à $\vec{u}$, et explique pourquoi c'était prévisible.

### Ex R9.7 — Degrés et radians, cosinus et sinus remarquables ✏️ ★ ⏱️ 15 min
**Objectif :** convertir des angles, et lire des cosinus et des sinus exacts sur le cercle trigonométrique.
**Prérequis :** fiche §6 · **Parcours :** C, E

Dessine chaque angle sur le cercle trigonométrique avant de répondre.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre $k$ tel que 135° $= k\pi$ radians | une fraction irréductible |
| b | $\frac{7\pi}{6}$ radians, en degrés | un entier |
| c | 1 radian, en degrés | un nombre (1 décimale) |
| d | $\cos\frac{5\pi}{6}$ | une valeur exacte |
| e | $\sin\frac{7\pi}{4}$ | une valeur exacte |
| f | $\cos\frac{3\pi}{2}$ | une valeur exacte |
| g | $\sin\frac{11\pi}{6}$ | une valeur exacte |
| h | $\sin\frac{5\pi}{2}$ | une valeur exacte |

### Ex R9.8 — Les courbes de cos et de sin : période, symétries, et arccos sur [0, π] ✏️ ★★ ⏱️ 20 min
**Objectif :** utiliser la périodicité et les symétries de cos et de sin, et calculer un arccosinus.
**Prérequis :** fiche §6 et §7 ; R7 (règle de la chaîne) · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la période de la fonction $t \mapsto \cos(3t)$ | une valeur exacte |
| b | les solutions de $\cos x = 0$ pour $x$ entre 0° (compris) et 360° (exclu), en degrés | une liste, dans l'ordre croissant |
| c | le nombre de solutions de $\sin x = 0{,}3$ pour $x$ dans $[0 ; 2\pi[$ | un entier |
| d | $\arccos\frac{\sqrt{2}}{2}$, en radians | une valeur exacte |
| e | $\arccos\left(\cos\frac{5\pi}{3}\right)$, en radians | une valeur exacte |
| f | $\sin(\pi - x) = \sin x$ pour tout nombre $x$ | vrai ou faux |
| g | la plus grande valeur de $3 + 2\cos x$ | un entier |
| h | la dérivée de $x \mapsto \sin(2x)$ en $x = 0$ | un entier |

### Ex R9.9 — L'angle entre deux vecteurs ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un angle à partir du produit scalaire et des normes, dans des cas exacts et approchés.
**Prérequis :** fiche §7 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la similarité cosinus de $(1 ; 2)$ et $(3 ; -1)$ | un nombre (4 décimales) |
| b | l'angle entre ces deux vecteurs, en degrés | un nombre (1 décimale) |
| c | l'angle entre $(1 ; 1)$ et $(0 ; -3)$, en degrés | un entier |
| d | l'angle entre $(\sqrt{3} ; 1)$ et $(-4 ; 0)$, en degrés | un entier |
| e | l'angle entre $(1 ; -1)$ et $(-2 ; 2)$, en radians | une valeur exacte |

Le triangle $ABC$ a pour sommets $A(0 ; 0)$, $B(4 ; 0)$ et $C(1 ; 3)$. L'angle en $A$ est l'angle entre $\overrightarrow{AB}$ et $\overrightarrow{AC}$.

| | Question | Réponse attendue |
|---|---|---|
| f | l'angle en $A$, en degrés | un nombre (1 décimale) |
| g | l'angle en $B$, en degrés | un entier |
| h | l'angle en $C$, en degrés | un nombre (1 décimale) |

Dans ta copie : vérifie que la somme des trois angles du triangle vaut 180°.

### Ex R9.10 — Distances et produits scalaires dans ℝ³ et ℝ⁴ ✏️ ★★ ⏱️ 20 min
**Objectif :** refaire les calculs de norme, de distance, de produit scalaire et d'angle avec trois et quatre coordonnées.
**Prérequis :** fiche §8 · **Parcours :** C, E

On donne $\vec{u} = (1 ; 4 ; 8)$ et $\vec{v} = (3 ; -2 ; 1)$ dans l'espace, et $\mathbf{x} = (1, -1, 2, 0)$ et $\mathbf{y} = (3, 1, -1, 4)$ dans $\mathbb{R}^4$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert \vec{u} \rVert$ | un entier |
| b | $\vec{u} \cdot \vec{v}$ | un entier |
| c | la distance entre $P(1 ; 0 ; -2)$ et $Q(3 ; 6 ; 1)$ | un entier |
| d | la similarité cosinus de $\vec{u}$ et $\vec{v}$ | un nombre (3 décimales) |
| e | $\mathbf{x}$ et $\mathbf{y}$ sont-ils orthogonaux ? | vrai ou faux |
| f | $\lVert \mathbf{y} \rVert$ | un nombre (2 décimales) |
| g | $\lVert \mathbf{y} \rVert_1$ | un entier |
| h | le nombre $t$ tel que $(1, t, 2, -1) \cdot (2, 3, -1, 4) = 0$ | une fraction irréductible |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex R9.11 — Démontrer cos² + sin² = 1 avec Pythagore ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la relation fondamentale de la trigonométrie, puis s'en servir pour calculer un sinus.
**Prérequis :** fiche §1 et §6 · **Parcours :** C

1. Soit $\theta$ un angle de $\left]0 ; \frac{\pi}{2}\right[$, $M$ le point du cercle trigonométrique d'angle $\theta$ et $H$ le pied de la perpendiculaire à l'axe des abscisses passant par $M$. Dans le triangle $OHM$, exprime $OH$ et $HM$ à l'aide de $\theta$, puis démontre que $\cos^2\theta + \sin^2\theta = 1$.
2. Pour un angle $\theta$ quelconque, démontre la même relation à partir des coordonnées de $M(\theta)$ et de la formule de la distance du §1. Pourquoi cette preuve couvre-t-elle aussi les angles où le triangle $OHM$ est aplati ?
3. On sait que $\cos\theta = -\frac{1}{3}$ et que $\theta$ est dans $[0 ; \pi]$. Calcule la valeur exacte de $\sin\theta$. Pourquoi faut-il savoir dans quel intervalle se trouve $\theta$ ?
4. Démontre que $(\cos\theta + \sin\theta)^2 + (\cos\theta - \sin\theta)^2 = 2$ pour tout $\theta$.
5. La relation permet-elle de retrouver $\cos\theta$ et $\sin\theta$ à partir de $\cos^2\theta$ seul ? Explique avec deux angles différents qui ont le même $\cos^2$.

### Ex R9.12 — La formule d'Al-Kashi par la hauteur du triangle et Pythagore ∂ ★★ ⏱️ 35 min
**Objectif :** démontrer la formule d'Al-Kashi, généralisation du théorème de Pythagore, et s'en servir pour calculer des côtés et des angles.
**Prérequis :** fiche §1, §6 et §7 · **Parcours :** C

Soit $ABC$ un triangle, $a = BC$, $b = CA$, $c = AB$, et $\hat{C}$ l'angle en $C$. On veut démontrer que $c^2 = a^2 + b^2 - 2ab\cos\hat{C}$.
1. On suppose d'abord l'angle $\hat{C}$ aigu, et le pied $H$ de la hauteur issue de $A$ situé sur le segment $[BC]$. Dans le triangle rectangle $AHC$, exprime $CH$ et $AH$ à l'aide de $b$ et de $\hat{C}$.
2. Exprime $BH$ à l'aide de $a$, $b$ et $\cos\hat{C}$, puis applique le théorème de Pythagore dans le triangle $ABH$ et conclus, avec $\cos^2 + \sin^2 = 1$.
3. On suppose maintenant l'angle $\hat{C}$ obtus : $H$ est sur la droite $(BC)$, au-delà de $C$. Que valent $CH$ et $BH$ ? Montre que la formule reste vraie (pense à $\cos(\pi - \hat{C}) = -\cos\hat{C}$).
4. Que devient la formule quand $\hat{C}$ est droit ? Et quand $\hat{C}$ est aigu, $c$ est-il plus court ou plus long que $\sqrt{a^2 + b^2}$ ?
5. Un triangle a des côtés de longueurs 5, 7 et 8. Calcule, avec la formule, l'angle opposé au côté de longueur 7 (une valeur exacte).

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R9.13 — Deux recettes, deux vecteurs d'ingrédients : la similarité cosinus 🔗 ★★ ⏱️ 20 min
**Objectif :** représenter des objets par des vecteurs, et comparer leurs directions par la similarité cosinus.
**Prérequis :** fiche §7 et §8 · **Parcours :** C, E

Chaque recette est décrite par le vecteur de ses quantités de farine, de sucre, de beurre et de lait, dans cet ordre, en unités de 50 g (ou 50 ml) : les crêpes $\mathbf{c} = (5, 1, 1, 10)$, le quatre-quarts $\mathbf{q} = (5, 5, 5, 0)$, les sablés $\mathbf{s} = (6, 2, 3, 0)$ et le pain au lait $\mathbf{p} = (10, 1, 1, 5)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{c} \cdot \mathbf{q}$ | un entier |
| b | $\lVert \mathbf{c} \rVert$ | un nombre (2 décimales) |
| c | $\lVert \mathbf{q} \rVert$ | un nombre (2 décimales) |
| d | la similarité cosinus de $\mathbf{c}$ et $\mathbf{q}$ | un nombre (3 décimales) |
| e | la similarité cosinus de $\mathbf{q}$ et $\mathbf{s}$ | un nombre (3 décimales) |
| f | la similarité cosinus de $\mathbf{c}$ et $\mathbf{p}$ | un nombre (3 décimales) |
| g | parmi $\mathbf{c}$, $\mathbf{q}$ et $\mathbf{p}$, la recette la plus semblable aux sablés au sens de la similarité cosinus | une lettre entre guillemets : c, q ou p |
| h | l'angle entre $\mathbf{c}$ et $\mathbf{q}$, en degrés | un nombre (1 décimale) |

Dans ta copie : calcule aussi $\mathbf{s} \cdot \mathbf{p}$ et $\mathbf{s} \cdot \mathbf{q}$. Le plus grand produit scalaire désigne-t-il la même recette que g ? Pourquoi la similarité cosinus ne change-t-elle pas si l'on double toutes les quantités d'une recette ?

### Ex R9.14 — Un neurone trace une droite : w₁x₁ + w₂x₂ + b = 0 🔗 ★ ⏱️ 15 min
**Objectif :** relier le calcul d'un neurone à deux entrées à une droite du plan et à son vecteur normal.
**Prérequis :** fiche §4 et §5 · **Parcours :** C, E

Un neurone à deux entrées, de poids $\mathbf{w} = (1 ; 3)$ et de biais $b = -6$, calcule $z = w_1 x_1 + w_2 x_2 + b$ pour un point $\mathbf{x} = (x_1 ; x_2)$, et répond 1 si $z > 0$, 0 sinon.

| | Question | Réponse attendue |
|---|---|---|
| a | $z$ pour $\mathbf{x} = (3 ; 2)$ | un entier |
| b | $z$ pour $\mathbf{x} = (0 ; 1)$ | un entier |
| c | la frontière $z = 0$ s'écrit $x_2 = m x_1 + p$ : la pente $m$ | une fraction irréductible |
| d | l'ordonnée à l'origine $p$ | un entier |
| e | $\mathbf{w}$ est-il orthogonal au vecteur directeur $(3 ; -1)$ de la frontière ? | vrai ou faux |
| f | le point de la frontière situé sur l'axe des $x_1$ | une liste |
| g | si l'on multiplie $w_1$, $w_2$ et $b$ par 5, la frontière change-t-elle ? | vrai ou faux |
| h | parmi les points $(0 ; 0)$, $(3 ; 2)$, $(6 ; 1)$, $(1 ; -1)$ et $(2 ; 2)$, combien reçoivent la réponse 1 ? | un entier |

Dans ta copie : dessine la frontière, le vecteur $\mathbf{w}$ posé sur elle, et les cinq points de h. De quel côté de la droite pointe $\mathbf{w}$ ?

### Ex R9.15 — Expliquer ce que mesure un produit scalaire 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement ce que mesure un produit scalaire, et ce que dit son signe.
**Prérequis :** fiche §5 et §7 · **Parcours :** C, E

Une amie te demande : « Le produit scalaire, c'est quoi ? On multiplie deux vecteurs et on obtient un nombre, mais ce nombre veut dire quoi ? »

Réponds-lui **en huit lignes au plus, avec une seule formule**. Ta réponse doit dire : ce qu'on calcule en coordonnées, ce que ce nombre mesure (les longueurs et l'angle), ce que disent son signe et la valeur 0, et une image concrète (une ombre, un effort dans une direction…).

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r9_geometrie_vecteurs/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R9.16 | Le vecteur entre deux points et sa norme · `vector`, `norm` | 🔨 | ★ | 15 | C, E |
| R9.17 | Produit scalaire et angle · `dot`, `angle_between` | 🔨 | ★ | 20 | C, E |
| R9.18 | La droite qui passe par deux points, et les radians · `line_through`, `deg_to_rad` | 🔨 | ★ | 15 | C |
| R9.19 | Les mêmes calculs avec NumPy (`np.linalg.norm`, `@`) | 📦 | ★ | 15 | C, E |
| R9.20 | Prédire le cosinus entre un vecteur et son double, puis son opposé | 🔮 | ★ | 10 | C, E |
| R9.21 | Dessiner des vecteurs, leur somme et un angle | 🎨 | ★★ | 20 | C, E |
| R9.22 | Le cercle trigonométrique : cos et sin d'un angle qui tourne | 🔬 | ★★ | 20 | C |
| R9.23 | Chasse à l'erreur : radians et degrés | 🐛 | ★ | 15 | C, E |
| R9.24 | Comparer deux flottants : `np.isclose` | 🛠️ | ★ | 10 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
