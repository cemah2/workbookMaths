# R9 · Géométrie du plan, vecteurs et trigonométrie — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R9.Q1 — Coordonnées et distance
1. En haut à gauche : abscisse négative, ordonnée positive.
2. $\left(\frac{-4 + 2}{2} ; \frac{7 + (-1)}{2}\right) = (-1 ; 3)$.
3. 8 : les deux points ont la même abscisse, la distance est l'écart des ordonnées, $\lvert -3 - 5 \rvert$.
4. **Vrai** : les écarts sont élevés au carré, leur signe ne compte pas.
5. **Faux** : c'est la distance L1 (fiche §3) ; la distance usuelle est $\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$.
6. **Oui** : $OM = \sqrt{2} \approx 1{,}414$, et $ON = 1{,}5$.

### R9.Q2 — Vecteurs : vrai ou faux
1. **Vrai** : c'est la caractérisation du parallélogramme $ABCD$ (fiche §2), éventuellement aplati si les quatre points sont alignés.
2. **Vrai** : $(2 ; -6) = -2 \times (-1 ; 3)$ ; le déterminant $2 \times 3 - (-1) \times (-6) = 0$.
3. **Faux** : l'égalité n'a lieu que si l'un des deux vecteurs est nul, ou s'ils ont la même direction et le même sens ; en général, $\lVert \vec{u} + \vec{v} \rVert \le \lVert \vec{u} \rVert + \lVert \vec{v} \rVert$.
4. **Vrai** : $\lVert -0{,}5\,\vec{u} \rVert = \lvert -0{,}5 \rvert\,\lVert \vec{u} \rVert = 0{,}5\,\lVert \vec{u} \rVert$ ; une norme n'est jamais négative, d'où la valeur absolue.
5. **Vrai** : la relation de Chasles.
6. **Faux** : c'est sa **norme** qui vaut 1 ; $(1 ; 1)$ a pour norme $\sqrt{2}$, et $(0{,}6 ; 0{,}8)$ est unitaire.

### R9.Q3 — Pente et vecteur directeur
1. $-2$.
2. $(1 ; 3)$, ou tout multiple non nul.
3. **Vrai** : pour $ax + by + c = 0$, $(-b ; a) = (5 ; 2)$ est directeur.
4. **Non** : elle est verticale ; elle n'a pas d'équation réduite, mais une équation cartésienne $x - 4 = 0$.
5. **Oui** : $6x + 2y - 1 = 0$ donne $y = -3x + 0{,}5$, de même pente $-3$ (et d'ordonnée à l'origine différente : elles ne sont pas confondues).
6. **Oui** : $3 \times 1 - 2 - 1 = 0$.

### R9.Q4 — Le signe du produit scalaire
1. **Aigu** : le cosinus de l'angle est positif.
2. $1 \times (-2) + 2 \times 1 = 0$ : les deux vecteurs sont orthogonaux.
3. **Faux** : $\vec{u} \cdot \vec{u} = \lVert \vec{u} \rVert^2 \ge 0$.
4. **Faux** : le produit scalaire est un **nombre**, $xx' + yy'$, pas un vecteur.
5. **Vrai** : la linéarité du produit scalaire.
6. **Faux** : $\vec{v}$ peut être n'importe quel vecteur orthogonal à $\vec{u}$, comme $(-2 ; 1)$ pour $(1 ; 2)$.

### R9.Q5 — Radians et valeurs remarquables
1. $\frac{\pi}{2}$.
2. 45°.
3. $\cos 0 = 1$ et $\sin 0 = 0$ (le point $I(1 ; 0)$).
4. 1 (le point le plus haut du cercle).
5. **Faux** : un cosinus est toujours entre $-1$ et $1$ (c'est l'abscisse d'un point d'un cercle de rayon 1).
6. $\cos\frac{\pi}{3} = \frac{1}{2}$ (et $\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$).

### R9.Q6 — Le cosinus de deux vecteurs
1. Ils sont **orthogonaux**.
2. Ils ont la même direction et des **sens contraires** (l'un est un multiple négatif de l'autre).
3. **Vrai** : par définition, et c'est ce que rend `math.acos`.
4. Un angle **petit** : $\arccos 0{,}9 \approx 26°$.
5. $\frac{\pi}{2}$.
6. **Non** : le vecteur nul n'a pas de direction, et la formule diviserait par sa norme, 0.

### R9.Q7 — Combien de composantes ?
1. Trois.
2. $\sqrt{1 + 1 + 1 + 1} = 2$.
3. **Non** : les deux vecteurs n'ont pas la même dimension.
4. $10 \times 10 \times 3 = 300$.
5. 100 multiplications (une par coordonnée), suivies de 99 additions.
6. $\sqrt{1 + 1 + 0} = \sqrt{2}$.

<a id="rappels"></a>

## 🔁 Rappels

### R9.R1 — Fonctions affines (R3)
1. $\frac{4 - (-2)}{3 - 0} = 2$. 2. $f(5) = -2{,}5 + 4 = 1{,}5$. 3. **Oui** : même pente 2 (et des ordonnées à l'origine différentes). 4. Décroissante : sa pente, $-0{,}5$, est négative.

### R9.R2 — Racines carrées (R1)
1. $\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt{2}$. 2. $\sqrt{36} = 6$. 3. $\frac{\sqrt{2}}{2}$. 4. $\sqrt{2} \approx 1{,}41$, alors que $\sqrt{1} + \sqrt{1} = 2$ : la racine d'une somme n'est pas la somme des racines.

### R9.R3 — Dériver une composée (R7)
1. $2 \times 3 \times (3x + 1) = 6(3x + 1)$. 2. $-2e^{-2x}$. 3. $g'(t) = 5f'(5t)$. 4. $4\cos(4t)$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R9.1 — Coordonnées et distance

**Réponses** : a) `[1.5, 8]` · b) `15` · c) `2.5` · d) `15.21` · e) `True` · f) `15.23` · g) `"73/6"` · h) `[15, 26]`.

**Démarche.**
- a) $\left(\frac{-3 + 6}{2} ; \frac{2 + 14}{2}\right) = (1{,}5 ; 8)$.
- b) $\overrightarrow{AB} = (9 ; 12)$ : $\sqrt{81 + 144} = \sqrt{225} = 15$.
- c) $\overrightarrow{AC} = (2 ; -1{,}5)$ : $\sqrt{4 + 2{,}25} = \sqrt{6{,}25} = 2{,}5$.
- d) $\overrightarrow{BC} = (-7 ; -13{,}5)$ : $\sqrt{49 + 182{,}25} = \sqrt{231{,}25} \approx 15{,}21$.
- e) $AB^2 + AC^2 = 225 + 6{,}25 = 231{,}25 = BC^2$ : par la réciproque du théorème de Pythagore, le triangle est rectangle en $A$ (le sommet opposé au plus grand côté). Autre preuve, avec le §5 : $\overrightarrow{AB} \cdot \overrightarrow{AC} = 18 - 18 = 0$.
- f) $OB = \sqrt{6^2 + 14^2} = \sqrt{232} \approx 15{,}23$.
- g) $M(x ; 0)$ : $MA^2 = MB^2$ s'écrit $(x + 3)^2 + 4 = (x - 6)^2 + 196$, soit $x^2 + 6x + 13 = x^2 - 12x + 232$, donc $18x = 219$ et $x = \frac{219}{18} = \frac{73}{6}$.
- h) $B$ est le milieu de $[AA']$ : $x_{A'} = 2x_B - x_A = 15$ et $y_{A'} = 2y_B - y_A = 26$.

**Erreurs fréquentes.** Additionner les écarts au lieu de leurs carrés (21 en b, 3,5 en c) ; oublier la racine (225) ; prendre la moitié de l'écart pour le milieu ($(4{,}5 ; 6)$) ; en h, donner le milieu de $[AB]$.

**Variante.** Le point $N$ de l'axe des ordonnées tel que $NA = NB$ ? *Réponse* : $N(0 ; y)$ avec $9 + (y - 2)^2 = 36 + (y - 14)^2$, soit $24y = 219$, $y = \frac{73}{8}$.

### Ex R9.2 — Vecteurs : somme, différence, produit par un nombre

**Réponses** : a) `[2, 2]` · b) `[6, -4]` · c) `[16, -9]` · d) `[-4, 3]` · e) `[5, 1]` · f) `[9, -2]` · g) `True` · h) `-2.5`.

**Démarche.**
- a) à c) Coordonnée par coordonnée : $(4 - 2 ; -1 + 3)$, $(4 + 2 ; -1 - 3)$, $(12 + 4 ; -3 - 6)$.
- d) Arrivée moins départ : $(-3 - 1 ; 5 - 2) = (-4 ; 3)$.
- e) $C = A + \vec{u} = (1 + 4 ; 2 - 1) = (5 ; 1)$.
- f) $ABCD$ est un parallélogramme quand $\overrightarrow{AB} = \overrightarrow{DC}$, c'est-à-dire $D = C - \overrightarrow{AB} = (5 + 4 ; 1 - 3) = (9 ; -2)$.
- g) Déterminant : $4 \times 1{,}5 - (-6) \times (-1) = 6 - 6 = 0$ ; en effet $\vec{w} = -1{,}5\,\vec{u}$.
- h) $k \times (-2) = 5$ et $k \times 3 = -7{,}5$ : $k = -2{,}5$, qui convient pour les deux coordonnées.

**Erreurs fréquentes.** Départ moins arrivée en d ; $-2 \times (-2) = -4$ en c ; en f, construire $ABDC$ au lieu de $ABCD$ (les sommets d'un parallélogramme se lisent dans l'ordre du tour).

**Variante.** Le point $E$ tel que $\overrightarrow{AE} = \vec{u} + \vec{v}$ ? *Réponse* : $E = A + (2 ; 2) = (3 ; 4)$.

### Ex R9.3 — Normes (euclidienne, avec un aperçu de L1 et L∞) et vecteurs unitaires

**Réponses** : a) `5.83` · b) `[-3, 3]` · c) `11.66` · d) `[0.45, -0.89]` · e) `12.4` · f) `8` · g) `5` · h) `[2.57, -1.54]`.

**Démarche.**
- a) $\sqrt{25 + 9} = \sqrt{34} \approx 5{,}83$.
- b) $t^2 + 4 = 13$, donc $t^2 = 9$ et $t = -3$ ou $t = 3$.
- c) $\lVert -2\vec{u} \rVert = 2\sqrt{34} \approx 11{,}66$.
- d) $\lVert (1 ; -2) \rVert = \sqrt{5}$, donc $\frac{1}{\sqrt{5}}(1 ; -2) \approx (0{,}45 ; -0{,}89)$. Vérification : $\frac{1}{5} + \frac{4}{5} = 1$.
- e) $\vec{u} + \vec{v} = (-3 ; 12)$ : $\sqrt{9 + 144} = \sqrt{153} \approx 12{,}4$, bien moins que $\lVert \vec{u} \rVert + \lVert \vec{v} \rVert = \sqrt{34} + 17 \approx 22{,}8$.
- f) et g) $\lvert 5 \rvert + \lvert -3 \rvert = 8$ ; $\max(5, 3) = 5$.
- h) On rend $\vec{u}$ unitaire, puis on multiplie par 3 : $\frac{3}{\sqrt{34}}(5 ; -3) \approx (2{,}57 ; -1{,}54)$.

**Erreurs fréquentes.** $(-3)^2 = -9$ ; une seule solution en b ; diviser par la norme L1 en d ($3$ au lieu de $\sqrt{5}$) ; oublier la valeur absolue en f ; en h, répondre $3\vec{u}$, dont la norme est $3\sqrt{34}$ et non 3.

**Variante.** La norme L∞ de $\vec{u} + \vec{v}$ ? *Réponse* : $\max(3, 12) = 12$.

### Ex R9.4 — Équations de droites

**Réponses** : a) `-1.5` · b) `2` · c) `[2, -3]` · d) `[3, 2, -4]` · e) `"2/3"` · f) `4` · g) `[0.8, 0.8]` · h) `[1, 0, 2]`.

**Démarche.**
- a) $m = \frac{-1 - 5}{2 - (-2)} = \frac{-6}{4} = -1{,}5$.
- b) $p = 5 - (-1{,}5) \times (-2) = 5 - 3 = 2$ : $(AB) : y = -1{,}5x + 2$.
- c) $(1 ; -1{,}5)$ est directeur, donc aussi $2 \times (1 ; -1{,}5) = (2 ; -3)$.
- d) $y = -1{,}5x + 2$ donne $1{,}5x + y - 2 = 0$, puis, multiplié par 2, $3x + 2y - 4 = 0$. Vérification : $A$ donne $-6 + 10 - 4 = 0$, $B$ donne $6 - 2 - 4 = 0$.
- e) $6y = 4x + 9$, donc $y = \frac{2}{3}x + \frac{3}{2}$ : la pente vaut $\frac{2}{3}$ (en général, $-\frac{a}{b}$).
- f) Même pente $-1{,}5$, et $1 = -1{,}5 \times 2 + p$, donc $p = 4$.
- g) $-1{,}5x + 2 = x$ donne $2{,}5x = 2$, donc $x = 0{,}8$, puis $y = 0{,}8$.
- h) Les deux points ont l'abscisse $-2$ : la droite est verticale, $x = -2$, soit $x + 2 = 0$.

**Erreurs fréquentes.** $\frac{\Delta x}{\Delta y}$ au lieu de $\frac{\Delta y}{\Delta x}$ ; mélanger l'ordre des points ; en e, oublier le signe en isolant $y$ ; en f, garder l'ordonnée à l'origine de $(AB)$.

**Variante.** L'équation cartésienne de la perpendiculaire à $(AB)$ qui passe par $A$, avec $a = 2$ ? *Réponse* : un vecteur directeur de $(AB)$, $(2 ; -3)$, est normal à la perpendiculaire : $2x - 3y + c = 0$, et $A$ donne $-4 - 15 + c = 0$, soit $c = 19$ : $[2, -3, 19]$.

### Ex R9.5 — Le produit scalaire en coordonnées

**Réponses** : a) `-1` · b) `27` · c) `-15` · d) `29` · e) `12` · f) `6` · g) `-10` · h) `True`.

**Démarche.**
- a) $-6 + 5 = -1$. b) $12 + 15 = 27$. c) $-18 + 3 = -15$. d) $4 + 25 = 29 = \lVert \vec{u} \rVert^2$.
- e) Par la linéarité, $\vec{u} \cdot \vec{w} + \vec{v} \cdot \vec{w} = 27 - 15 = 12$ ; ou directement, $(-1 ; 6) \cdot (6 ; 3) = -6 + 18 = 12$.
- f) $2 \times (-3) \times (\vec{u} \cdot \vec{v}) = -6 \times (-1) = 6$.
- g) $2t + 5 \times 4 = 0$, donc $t = -10$.
- h) $\vec{u} \cdot \vec{w} = 27 > 0$ : l'angle est aigu.

**Erreurs fréquentes.** $-6 - 5$ en a (un signe perdu) ; prendre la racine en d ; oublier le signe du facteur $-3$ en f.

**Variante.** $\vec{v} \cdot (\vec{u} - \vec{w})$ ? *Réponse* : $\vec{v} \cdot \vec{u} - \vec{v} \cdot \vec{w} = -1 + 15 = 14$.

### Ex R9.6 — Orthogonalité et projections simples

**Réponses** : a) `True` · b) `[4, 10]` · c) `-0.4` · d) `True` · e) `6.32` · f) `[6, 2]` · g) `[-1, 3]` · h) `True`.

**Démarche.**
- a) $42 - 42 = 0$.
- b) $5 \times 4 + (-2) \times y = 0$, donc $y = 10$.
- c) $3k + 2(k + 1) = 5k + 2 = 0$, donc $k = -0{,}4$.
- d) $\overrightarrow{AB} = (4 ; 2)$ et $\overrightarrow{AC} = (-1 ; 2)$ : $-4 + 4 = 0$, rectangle en $A$.
- e) $\vec{u} \cdot \vec{v} = 15 + 5 = 20$ et $\lVert \vec{u} \rVert = \sqrt{10}$ : $\frac{20}{\sqrt{10}} = 2\sqrt{10} \approx 6{,}32$.
- f) $\vec{p} = \frac{20}{10}\vec{u} = (6 ; 2)$ ; sa norme est bien $\sqrt{40} = 2\sqrt{10}$.
- g) $(5 - 6 ; 5 - 2) = (-1 ; 3)$.
- h) Les vecteurs directeurs $(1 ; 3)$ et $\left(1 ; -\frac{1}{3}\right)$ ont pour produit scalaire $1 - 1 = 0$ (le produit des pentes vaut $-1$).

Dans ta copie : $(-1 ; 3) \cdot (3 ; 1) = -3 + 3 = 0$. C'était prévisible : $\vec{p}$ est justement le multiple de $\vec{u}$ choisi pour que le reste soit orthogonal à $\vec{u}$ (fiche §5).

**Erreurs fréquentes.** Diviser par $\lVert \vec{u} \rVert^2$ pour la longueur (2 en e) ou par $\lVert \vec{u} \rVert$ pour le vecteur ; $p - v$ au lieu de $v - p$ ; en c, oublier de développer $2(k + 1)$.

**Variante.** La projection de $\vec{v} = (5 ; 5)$ sur la direction de $(1 ; 0)$ ? *Réponse* : $(5 ; 0)$, l'ombre sur l'axe des abscisses.

### Ex R9.7 — Degrés et radians, cosinus et sinus remarquables

**Réponses** : a) `"7*pi/12"` · b) `210` · c) `57.3` · d) `"-sqrt(3)/2"` · e) `"-sqrt(2)/2"` · f) `"0"` · g) `"-1/2"` · h) `"1"`.

**Démarche.**
- a) $105 \times \frac{\pi}{180} = \frac{105\pi}{180} = \frac{7\pi}{12}$.
- b) $\frac{7\pi}{6} \times \frac{180}{\pi} = 210$.
- c) $\frac{180}{\pi} \approx 57{,}3$.
- d) $\frac{5\pi}{6} = \pi - \frac{\pi}{6}$ : $\cos\frac{5\pi}{6} = -\cos\frac{\pi}{6} = -\frac{\sqrt{3}}{2}$.
- e) $\frac{7\pi}{4} = 2\pi - \frac{\pi}{4}$, l'angle $-\frac{\pi}{4}$ : $\sin = -\frac{\sqrt{2}}{2}$.
- f) $\frac{3\pi}{2}$ est le point le plus bas du cercle, $(0 ; -1)$ : son abscisse vaut 0.
- g) $\frac{11\pi}{6} = 2\pi - \frac{\pi}{6}$ : $\sin = -\sin\frac{\pi}{6} = -\frac{1}{2}$.
- h) $\frac{5\pi}{2} = \frac{\pi}{2} + 2\pi$ : $\sin = \sin\frac{\pi}{2} = 1$.

**Erreurs fréquentes.** Convertir dans le mauvais sens ($\frac{12\pi}{7}$ en a) ; confondre les valeurs de $\frac{\pi}{6}$ et $\frac{\pi}{3}$ ; oublier le signe d'un angle qui n'est pas dans le premier quart du cercle.

**Variante.** $\cos\frac{4\pi}{3}$ ? *Réponse* : $\frac{4\pi}{3} = \pi + \frac{\pi}{3}$ : $-\frac{1}{2}$.

### Ex R9.8 — Les courbes de cos et de sin : période, symétries, et arccos sur [0, π]

**Réponses** : a) `"2*pi/3"` · b) `[90, 270]` · c) `2` · d) `"pi/4"` · e) `"pi/3"` · f) `True` · g) `5` · h) `2`.

**Démarche.**
- a) $\cos(3(t + T)) = \cos(3t + 3T)$ redonne $\cos(3t)$ dès que $3T = 2\pi$ : $T = \frac{2\pi}{3}$.
- b) Le cosinus, abscisse du point, s'annule en haut et en bas du cercle : 90° et 270°.
- c) La droite horizontale d'ordonnée 0,3 coupe le cercle en deux points, l'un dans le premier quart, l'autre dans le deuxième.
- d) $\frac{\pi}{4}$ est dans $[0 ; \pi]$ et a pour cosinus $\frac{\sqrt{2}}{2}$.
- e) $\cos\frac{5\pi}{3} = \cos\left(-\frac{\pi}{3}\right) = \frac{1}{2}$, et l'angle de $[0 ; \pi]$ de cosinus $\frac{1}{2}$ est $\frac{\pi}{3}$ (pas $\frac{5\pi}{3}$, hors de l'intervalle).
- f) **Vrai** : $\pi - x$ est le symétrique de $x$ par rapport à l'axe vertical, même ordonnée.
- g) $\cos x \le 1$, donc $3 + 2\cos x \le 5$, atteint pour $x = 0$.
- h) La dérivée est $2\cos(2x)$ (règle de la chaîne), qui vaut 2 en 0.

**Erreurs fréquentes.** Multiplier la période par 3 au lieu de la diviser ; donner les zéros du sinus en b ; croire que $\arccos(\cos\theta) = \theta$ toujours ; oublier le facteur 2 en h.

**Variante.** La période de $t \mapsto \sin\left(\frac{t}{2}\right)$ ? *Réponse* : $4\pi$ : diviser l'angle par 2 fait tourner deux fois moins vite.

### Ex R9.9 — L'angle entre deux vecteurs

**Réponses** : a) `0.2169` · b) `77.5` · c) `135` · d) `150` · e) `"pi"` · f) `71.6` · g) `45` · h) `63.4`.

**Démarche.**
- a) $\frac{-2 + 4}{\sqrt{5}\sqrt{17}} = \frac{2}{\sqrt{85}} \approx 0{,}2169$. b) $\arccos 0{,}2169 \approx 77{,}5°$.
- c) $\frac{0 - 3}{\sqrt{2} \times 3} = -\frac{\sqrt{2}}{2}$ : 135°.
- d) $\frac{-\sqrt{3} - \sqrt{3}}{2 \times 2} = -\frac{\sqrt{3}}{2}$ : 150° (les deux normes valent $\sqrt{1 + 3} = 2$).
- e) $(-2 ; 2) = -2 \times (1 ; -1)$ : même direction, sens contraires, l'angle vaut $\pi$.
- f) $\overrightarrow{AB} = (4 ; 0)$, $\overrightarrow{AC} = (1 ; 3)$ : $\cos = \frac{4}{4\sqrt{10}} = \frac{1}{\sqrt{10}}$, environ 71,6°.
- g) $\overrightarrow{BA} = (-4 ; 0)$, $\overrightarrow{BC} = (-3 ; 3)$ : $\cos = \frac{12}{4 \times 3\sqrt{2}} = \frac{\sqrt{2}}{2}$, 45°.
- h) $\overrightarrow{CA} = (-1 ; -3)$, $\overrightarrow{CB} = (3 ; -3)$ : $\cos = \frac{-3 + 9}{\sqrt{10}\sqrt{18}} = \frac{6}{\sqrt{180}} \approx 0{,}447$, environ 63,4°.

Dans ta copie : $71{,}6 + 45 + 63{,}4 = 180$.

**Erreurs fréquentes.** Oublier de diviser par les normes (2 en a) ; donner l'angle en radians ; prendre $\overrightarrow{AB}$ au lieu de $\overrightarrow{BA}$ pour l'angle en $B$ (135° au lieu de 45°).

**Variante.** L'angle entre $(1 ; 1)$ et $(0 ; 2)$, en radians ? *Réponse* : $\cos = \frac{2}{2\sqrt{2}} = \frac{\sqrt{2}}{2}$, donc $\frac{\pi}{4}$.

### Ex R9.10 — Distances et produits scalaires dans ℝ³ et ℝ⁴

**Réponses** : a) `9` · b) `3` · c) `7` · d) `0.089` · e) `True` · f) `5.2` · g) `9` · h) `"4/3"`.

**Démarche.**
- a) $\sqrt{1 + 16 + 64} = \sqrt{81} = 9$. b) $3 - 8 + 8 = 3$. c) $\overrightarrow{PQ} = (2 ; 6 ; 3)$ : $\sqrt{4 + 36 + 9} = 7$.
- d) $\lVert \vec{v} \rVert = \sqrt{14}$ : $\frac{3}{9\sqrt{14}} \approx 0{,}089$, un angle d'environ 85° : presque orthogonaux.
- e) $3 - 1 - 2 + 0 = 0$.
- f) $\sqrt{9 + 1 + 1 + 16} = \sqrt{27} \approx 5{,}20$. g) $3 + 1 + 1 + 4 = 9$.
- h) $2 + 3t - 2 - 4 = 0$, donc $3t = 4$ et $t = \frac{4}{3}$.

**Erreurs fréquentes.** Oublier la troisième (ou la quatrième) coordonnée ; diviser par une seule norme en d ; un signe perdu en h.

**Variante.** La distance entre $\mathbf{x}$ et $\mathbf{y}$ ? *Réponse* : $\mathbf{x} - \mathbf{y} = (-2, -2, 3, -4)$, donc $\sqrt{4 + 4 + 9 + 16} = \sqrt{33} \approx 5{,}74$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R9.11 — Démontrer cos² + sin² = 1 avec Pythagore

**Réponse modèle.**
1. $M = (\cos\theta ; \sin\theta)$ et $H = (\cos\theta ; 0)$. Pour $\theta$ dans $\left]0 ; \frac{\pi}{2}\right[$, les deux coordonnées sont positives : $OH = \cos\theta$ et $HM = \sin\theta$. Le triangle $OHM$ est rectangle en $H$ et $OM = 1$ (le rayon), donc, par Pythagore, $OH^2 + HM^2 = OM^2$, soit $\cos^2\theta + \sin^2\theta = 1$.
2. Pour tout $\theta$, $M(\theta) = (\cos\theta ; \sin\theta)$ est sur le cercle de centre $O$ et de rayon 1, donc $OM = 1$. La formule de la distance (§1) donne $OM = \sqrt{(\cos\theta - 0)^2 + (\sin\theta - 0)^2}$, d'où $\cos^2\theta + \sin^2\theta = 1$. Cette preuve ne demande aucun triangle : quand $M$ est sur un axe ($\theta = 0$, $\frac{\pi}{2}$, $\pi$…), le triangle $OHM$ est aplati, mais la formule de la distance reste vraie (l'une des coordonnées est nulle), et les carrés effacent les signes.
3. $\sin^2\theta = 1 - \frac{1}{9} = \frac{8}{9}$, donc $\sin\theta = \frac{2\sqrt{2}}{3}$ ou $-\frac{2\sqrt{2}}{3}$. Comme $\theta$ est dans $[0 ; \pi]$, le point est dans la moitié haute du cercle et $\sin\theta \ge 0$ : $\sin\theta = \frac{2\sqrt{2}}{3} \approx 0{,}943$. Sans l'intervalle, deux réponses seraient possibles.
4. En développant : $(\cos\theta + \sin\theta)^2 + (\cos\theta - \sin\theta)^2 = (\cos^2\theta + 2\cos\theta\sin\theta + \sin^2\theta) + (\cos^2\theta - 2\cos\theta\sin\theta + \sin^2\theta) = 2(\cos^2\theta + \sin^2\theta) = 2$.
5. Non : $\theta = \frac{\pi}{3}$ et $\theta = \frac{2\pi}{3}$ ont le même $\cos^2$, $\frac{1}{4}$, mais des cosinus opposés. La relation ne donne que des carrés, donc les valeurs au signe près.

**Grille.** Une bonne démonstration : (1) identifie les longueurs $OH$ et $HM$ et justifie que le triangle est rectangle ; (2) passe par les coordonnées et la distance pour couvrir tous les angles, et dit pourquoi les cas aplatis ne posent pas de problème ; (3) choisit le signe du sinus grâce à l'intervalle ; (4) développe avec les identités remarquables (R2) et utilise la relation ; (5) donne un contre-exemple chiffré.

### Ex R9.12 — La formule d'Al-Kashi par la hauteur du triangle et Pythagore

**Réponse modèle.**
1. Le triangle $AHC$ est rectangle en $H$, d'hypoténuse $AC = b$ : $CH = b\cos\hat{C}$ et $AH = b\sin\hat{C}$.
2. $H$ est sur $[BC]$, donc $BH = BC - CH = a - b\cos\hat{C}$. Pythagore dans $ABH$, rectangle en $H$ : $c^2 = AH^2 + BH^2 = b^2\sin^2\hat{C} + (a - b\cos\hat{C})^2 = b^2\sin^2\hat{C} + a^2 - 2ab\cos\hat{C} + b^2\cos^2\hat{C}$. Avec $\sin^2\hat{C} + \cos^2\hat{C} = 1$ : $c^2 = a^2 + b^2 - 2ab\cos\hat{C}$.
3. Si $\hat{C}$ est obtus, l'angle $\widehat{ACH}$ vaut $\pi - \hat{C}$, aigu : $CH = b\cos(\pi - \hat{C}) = -b\cos\hat{C}$ (un nombre positif, car $\cos\hat{C} < 0$) et $AH = b\sin(\pi - \hat{C}) = b\sin\hat{C}$. Comme $H$ est au-delà de $C$, $BH = BC + CH = a - b\cos\hat{C}$ : la même expression qu'en 2, et le calcul de Pythagore se termine de la même façon.
4. Si $\hat{C}$ est droit, $H = C$ : le triangle $ABC$ est lui-même rectangle en $C$, et le théorème de Pythagore donne $c^2 = a^2 + b^2$, ce que donne aussi la formule, puisque $\cos\hat{C} = 0$. Si $\hat{B}$ est obtus, $\hat{C}$ est aigu et $CH = b\cos\hat{C}$, comme en 1 ; mais $H$ est au-delà de $B$, donc $CH = CB + BH$, soit $BH = b\cos\hat{C} - a$. Pythagore dans $ABH$ : $c^2 = AH^2 + BH^2 = b^2\sin^2\hat{C} + (b\cos\hat{C} - a)^2$, et $(b\cos\hat{C} - a)^2 = (a - b\cos\hat{C})^2$ : le calcul se termine comme en 2.
5. Avec $c = 7$ (le côté opposé à l'angle cherché), $a = 5$ et $b = 8$ : $49 = 25 + 64 - 80\cos\hat{C}$, donc $\cos\hat{C} = \frac{40}{80} = \frac{1}{2}$ et $\hat{C} = \frac{\pi}{3}$ (60°).

**Grille.** Une bonne démonstration : (1) exprime $CH$ et $AH$ dans le triangle rectangle, avec la bonne hypoténuse ; (2) écrit $BH$, développe le carré (R2) et utilise $\cos^2 + \sin^2 = 1$ ; (3) traite le cas obtus en justifiant la position de $H$ et le signe de $\cos\hat{C}$ ; (4) traite les deux cas restants, l'angle droit ($H = C$) et $H$ au-delà de $B$, en remarquant qu'un carré ne change pas quand on change le signe de ce qu'il contient ; (5) isole $\cos\hat{C}$ et conclut par un angle exact.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R9.13 — Deux recettes, deux vecteurs d'ingrédients : la similarité cosinus

**Réponses** : a) `35` · b) `11.27` · c) `8.66` · d) `0.359` · e) `0.907` · f) `0.803` · g) `"q"` · h) `69.0`.

**Démarche.**
- a) $25 + 5 + 5 + 0 = 35$. b) $\sqrt{25 + 1 + 1 + 100} = \sqrt{127} \approx 11{,}27$. c) $\sqrt{75} \approx 8{,}66$.
- d) $\frac{35}{\sqrt{127}\sqrt{75}} \approx 0{,}359$ : deux recettes assez différentes (les crêpes sont surtout du lait).
- e) $\mathbf{q} \cdot \mathbf{s} = 30 + 10 + 15 = 55$ et $\lVert \mathbf{s} \rVert = \sqrt{49} = 7$ : $\frac{55}{7\sqrt{75}} \approx 0{,}907$.
- f) $\mathbf{c} \cdot \mathbf{p} = 50 + 1 + 1 + 50 = 102$ et $\lVert \mathbf{p} \rVert = \sqrt{127}$ : $\frac{102}{127} \approx 0{,}803$.
- g) Pour les sablés : $\cos(\mathbf{s}, \mathbf{c}) = \frac{35}{7\sqrt{127}} \approx 0{,}444$, $\cos(\mathbf{s}, \mathbf{q}) \approx 0{,}907$ (e) et $\cos(\mathbf{s}, \mathbf{p}) = \frac{65}{7\sqrt{127}} \approx 0{,}824$ : le quatre-quarts.
- h) $\arccos 0{,}3586 \approx 69{,}0°$.

Dans ta copie : le quatre-quarts, avec $\cos(\mathbf{c}, \mathbf{q}) \approx 0{,}359$ (d), contre environ 0,444 pour les sablés et 0,803 pour le pain au lait (f). Les crêpes sont surtout du lait (10 unités sur 17), et le quatre-quarts n'en contient pas du tout : la plus grande coordonnée de $\mathbf{c}$ est multipliée par 0 dans le produit scalaire. À l'inverse, le sucre et le beurre, qui font les deux tiers du quatre-quarts, sont presque absents des crêpes.

**Erreurs fréquentes.** Oublier de diviser par les normes (35 en d) ; choisir la recette du plus grand produit scalaire en g ; donner l'angle en radians en h.

**Variante.** La similarité cosinus entre une recette sans lait, $(4, 2, 2, 0)$, et du lait seul, $(0, 0, 0, 3)$ ? *Réponse* : leur produit scalaire est nul : 0, deux recettes sans ingrédient commun sont orthogonales.

### Ex R9.14 — Un neurone trace une droite : w₁x₁ + w₂x₂ + b = 0

**Réponses** : a) `3` · b) `-5` · c) `[0, 2]` · d) `[6, 0]` · e) `[3, -1]` · f) `True` · g) `[12, 0]` · h) `3`.

**Démarche.**
- a) $3 + 6 - 6 = 3$. b) $4 - 3 - 6 = -5$.
- c) Sur l'axe des $x_2$, $x_1 = 0$ : $3x_2 - 6 = 0$, donc $x_2 = 2$. d) Sur l'axe des $x_1$, $x_2 = 0$ : $x_1 = 6$.
- e) Pour $x_1 + 3x_2 - 6 = 0$, $(-b ; a) = (-3 ; 1)$ est directeur (fiche §4), et son opposé $(3 ; -1)$ aussi. Vérification : de $(0 ; 2)$ à $(6 ; 0)$, on se déplace de $(6 ; -2) = 2 \times (3 ; -1)$.
- f) $1 \times 3 + 3 \times (-1) = 0$ : $\mathbf{w}$ est un vecteur normal de la frontière (fiche §4 et §5).
- g) $z = 6$ s'écrit $x_1 + 3x_2 - 12 = 0$ ; avec $x_2 = 0$, $x_1 = 12$.
- h) $z$ vaut $-6$, $3$, $3$, $-8$ et $2$ : trois points sont du côté où $z > 0$, $(3 ; 2)$, $(6 ; 1)$ et $(2 ; 2)$.

Dans ta copie : les deux droites sont parallèles. Leurs équations $x_1 + 3x_2 - 6 = 0$ et $x_1 + 3x_2 - 12 = 0$ ne diffèrent que par la constante : elles ont le même vecteur normal $\mathbf{w} = (1 ; 3)$. Les points où $z$ prend une valeur donnée forment toujours une droite perpendiculaire à $\mathbf{w}$, et $z$ augmente quand on se déplace dans le sens de $\mathbf{w}$ : la droite $z = 6$ est du côté où $z > 0$.

**Erreurs fréquentes.** Oublier le biais (9 en a) ; échanger les deux coordonnées en c ou en d ; prendre la direction de $\mathbf{w}$, un vecteur normal, pour un vecteur directeur en e ; compter $z \ge 0$ au lieu de $z > 0$ en h (aucun point ici n'est sur la frontière, mais la règle compte).

**Variante.** Le point de la droite $z = -3$ situé sur l'axe des $x_2$ ? *Réponse* : $x_1 + 3x_2 - 3 = 0$ avec $x_1 = 0$ donne $x_2 = 1$ : $(0 ; 1)$.

### Ex R9.15 — Expliquer ce que mesure un produit scalaire

**Exemple de réponse.**

> On multiplie les coordonnées deux à deux et on additionne : $\vec{u} \cdot \vec{v} = xx' + yy'$. Ce nombre combine trois choses : la longueur de chaque vecteur et l'angle entre eux. Il dit à quel point les deux vecteurs vont dans le même sens. Positif, ils vont plutôt dans la même direction ; négatif, plutôt en sens contraires ; nul, ils sont perpendiculaires. Une image : éclaire un vecteur par une lumière perpendiculaire à l'autre ; son ombre sur l'autre, multipliée par la longueur de l'autre, c'est le produit scalaire. Ou encore : si tu tires une valise avec une sangle, l'effort qui la fait vraiment avancer est la part de ta force dans la direction du chemin. Plus les vecteurs sont longs, plus il est grand : pour comparer seulement les directions, on le divise par les deux longueurs (le cosinus).

**Grille.** Une bonne réponse : (1) le calcul en coordonnées, une seule formule ; (2) il dépend des longueurs et de l'angle ; (3) le signe : même sens, sens contraires ; (4) zéro : perpendiculaires ; (5) une image concrète (ombre, effort, projection) ; (6) huit lignes au plus.

<a id="notebook"></a>

## Notebook

### Ex R9.16 — Le vecteur entre deux points et sa norme · `vector`, `norm`

**Réponses** : a) `[7, -6]` · b) `[-1, -2, -3]` · c) `"ValueError"` · d) `[25.0, 2.0, 0.0]` · e) `"float"` · f) `29.0`.

**Démarche.** `vector` : comparer `len(A)` et `len(B)` (une `ValueError` sinon), puis `tuple(b - a for a, b in zip(A, B))`. `norm` : additionner les carrés des coordonnées dans une boucle, puis `math.sqrt` du total, qui est un flottant. f) La distance est la norme du vecteur : $\sqrt{20^2 + 21^2} = 29$. Pour la copie : en dimension 1, la boucle n'a qu'un tour, et $\sqrt{x^2} = \lvert x \rvert$.

**Erreurs fréquentes.** `a - b` au lieu de `b - a` ; renvoyer une liste au lieu d'un tuple ; oublier la racine ; ne pas tester les dimensions, et laisser `zip` s'arrêter sans rien dire.

### Ex R9.17 — Produit scalaire et angle · `dot`, `angle_between`

**Réponses** : a) `0` · b) `"int"` · c) `"ValueError"` · d) `2.0344` · e) `"aucune"` · f) `3.1416` · g) `"ValueError"` · h) `100.3048`.

**Démarche.** `dot` : vérifier les dimensions, puis additionner les produits `x * y` dans une boucle (un total qui part de l'entier 0 reste entier). `angle_between` : calculer les deux normes, lever la `ValueError` si l'une vaut 0, puis `cosine = dot(u, v) / (norm_u * norm_v)`, `cosine = max(-1.0, min(1.0, cosine))` et `math.acos(cosine)`. d) $\arccos\left(-\frac{1}{\sqrt{5}}\right) \approx 2{,}0344$. f) Deux vecteurs de sens contraires : l'angle plat, $\pi$. Pour la copie : $\sqrt{37}$ et $\sqrt{148}$ sont arrondies, et leur produit ne redonne pas exactement 74 ; le quotient tombe à −1,0000000000000002, juste sous $-1$.

**Erreurs fréquentes.** Oublier de ramener le cosinus dans $[-1 ; 1]$ (`ValueError: math domain error` en e) ; convertir en degrés dans la fonction ; diviser par zéro au lieu de lever une `ValueError` pour un vecteur nul.

### Ex R9.18 — La droite qui passe par deux points, et les radians · `line_through`, `deg_to_rad`

**Réponses** : a) `[1.0, -0.3333, -1.3333]` · b) `[1.0, 0.0, -4.0]` · c) `"ValueError"` · d) `"int"` · e) `[3.1416, 1.5708, 0.7854, -0.5236]`.

**Démarche.** `line_through` : `dx, dy = xb - xa, yb - ya`, une `ValueError` si les deux sont nuls, puis `a, b = -dy, dx` et `c = -(a * xa + b * ya)`. Aucune division : les coefficients restent entiers. `deg_to_rad` : `degrees * math.pi / 180`. Pour la copie : deux points de même abscisse donnent $(d_x ; d_y) = (0 ; d_y)$, puis $(a ; b) = (-d_y ; 0)$ : une équation sans $y$, celle d'une droite verticale ; la méthode ne divise jamais par $d_x$, contrairement au calcul de la pente.

**Erreurs fréquentes.** Prendre le vecteur directeur pour $(a ; b)$ ; calculer la pente, qui divise par zéro pour une droite verticale ; multiplier par $\frac{180}{\pi}$ dans `deg_to_rad`.

### Ex R9.19 — Les mêmes calculs avec NumPy (`np.linalg.norm`, `@`)

**Réponses** : a) `5.0` · b) `-4.0` · c) `9.0` · d) `4.0` · e) `-0.2385` · f) `6.6521` · g) `103.8`.

**Démarche.** `np.linalg.norm(x)`, `x @ y`, `np.linalg.norm(x, ord=1)`, `np.linalg.norm(x, ord=np.inf)`, puis `x @ y / (np.linalg.norm(x) * np.linalg.norm(y))`, `np.linalg.norm(x - y)` et `np.degrees(np.arccos(cos))`. Pour la copie : le produit scalaire de b) est négatif, donc l'angle est obtus, avant même de le calculer.

**Erreurs fréquentes.** `x * y` (un array, case par case) au lieu de `x @ y` ; oublier `np.degrees` ; `np.linalg.norm(x) - np.linalg.norm(y)` pour la distance.

### Ex R9.20 — Prédire : multiplier ou décaler deux vecteurs change-t-il leur similarité cosinus ?

**Réponses** : a) `2` · b) `3` · c) `2`.

**Démarche.** a) $\mathbf{u} \cdot (2\mathbf{v}) = 2\,(\mathbf{u} \cdot \mathbf{v})$ et $\lVert 2\mathbf{v} \rVert = 2\lVert \mathbf{v} \rVert$ : le facteur 2 se simplifie dans le quotient, la similarité reste environ 0,098. c) $(-\mathbf{u}) \cdot (-\mathbf{v}) = \mathbf{u} \cdot \mathbf{v}$, et les normes ne changent pas : la même. b) Ajouter 10 à chaque coordonnée donne $(13, 9, 14, 11, 5)$ et $(12, 12, 9, 13, 10)$ : deux vecteurs aux coordonnées toutes positives et proches les unes des autres, qui penchent tous deux vers la direction de $(1, 1, 1, 1, 1)$ ; leur similarité monte à environ 0,949. Plus le nombre ajouté est grand, plus les deux directions se rapprochent de celle de $(1, 1, 1, 1, 1)$, et plus la similarité s'approche de 1.

**Erreurs fréquentes.** Croire que la similarité double quand un vecteur double ; croire qu'ajouter un même nombre à toutes les coordonnées ne change rien, comme une multiplication.

### Ex R9.21 — Dessiner des vecteurs, leur somme et un angle

**Démarche.** `ax.quiver([0, 0, 0], [0, 0, 0], [u[0], v[0], s[0]], [u[1], v[1], s[1]], angles="xy", scale_units="xy", scale=1)` avec `s = u + v`, des pointillés pour les deux autres côtés du parallélogramme, des limites qui contiennent les quatre sommets, `ax.set_aspect("equal")`, puis l'angle calculé dans la fonction (produit scalaire, normes, `math.acos`, `math.degrees`) et écrit dans le titre avec `:.1f`. Pour la copie : sans la même unité sur les deux axes, matplotlib étire la figure, et les angles dessinés ne sont plus les vrais (un angle droit n'a plus l'air droit).

**Erreurs fréquentes.** Oublier `angles="xy", scale_units="xy", scale=1` (les flèches n'ont plus la longueur des vecteurs) ; écrire l'angle en dur dans le titre ; ouvrir une figure dans la fonction au lieu de dessiner dans l'axe reçu.

### Ex R9.22 — Le cercle trigonométrique : cos et sin d'un angle qui tourne

**Réponses** : a) `True` · b) `45.5` · c) `90` · d) `0.540298`.

**Démarche.** `theta = np.radians(degrees)` ; a) `np.max(np.abs(np.cos(theta) ** 2 + np.sin(theta) ** 2 - 1)) < 1e-12` (l'écart est de l'ordre de $10^{-16}$) ; b) `degrees[np.argmax(np.sin(theta) > np.cos(theta))]`, le premier angle où le tableau de booléens vaut `True` ; c) `whole[np.argmax(np.sin(np.radians(whole)))]` ; d) le taux d'accroissement, environ 0,540298, tout près de $\cos 1 \approx 0{,}540302$. Pour la copie : $\cos\theta > \sin\theta$ entre $-135°$ et $45°$ (soit $[0° ; 45°[$ et $]225° ; 360°[$), la moitié du cercle sous la droite $y = x$ ; d) montre que la pente de $\sin$ en 1 vaut $\cos 1$.

**Erreurs fréquentes.** Passer des degrés à `np.sin` (1,5 en b, 322 en c) ; donner la position au lieu de l'angle (45 en b) ; oublier de diviser par $h$ en d, ou répondre $\cos 1$ lui-même.

### Ex R9.23 — Chasse à l'erreur : radians et degrés

**Réponses** : a) `"ADE"` · b) `[0.7071, 0.7071, 60.0, 60.0, 0.5236]`.

**Démarche.** (A) `math.sin` attend des radians : `math.sin(45)` est le sinus de 45 radians (environ 0,851) ; le sinus de 45° vaut $\frac{\sqrt{2}}{2} \approx 0{,}7071$. (D) `math.acos` rend des radians : $\frac{\pi}{3} \approx 1{,}0472$, qui vaut bien 60°, mais pas le nombre 60 ; il fallait `math.degrees(math.acos(0.5))`. (E) La conversion est à l'envers : $30 \times \frac{\pi}{180} = \frac{\pi}{6} \approx 0{,}5236$, alors que $30 \times \frac{180}{\pi} \approx 1\,718{,}9$. (B) convertit avant d'appeler `math.sin`, et (C) multiplie bien par $\frac{180}{\pi}$ pour aller vers les degrés (60, aux arrondis près) : justes. Les cinq bonnes valeurs : $\frac{\sqrt{2}}{2}$ deux fois, 60 deux fois, et $\frac{\pi}{6}$.

**Erreurs fréquentes.** Accuser (C), qui multiplie par $\frac{180}{\pi}$ comme (E), mais dans le bon sens ; croire (D) juste parce que l'angle vaut « 60 degrés ».

### Ex R9.24 — Comparer deux flottants : `np.isclose`

**Démarche.** `dot = sum(a * b for a, b in zip(u, v))`, puis `return math.isclose(dot, 0, abs_tol=tol)` (ou `abs(dot) <= tol`, ou `bool(np.isclose(dot, 0, atol=tol))`). Pour la copie : `math.isclose(1e-17, 0)` vaut `False`, car sa tolérance par défaut est relative (« à un milliardième de la plus grande des deux valeurs près ») : comparée à 0, elle n'accepte que 0 exactement. Pour comparer à 0, il faut une tolérance absolue.

**Erreurs fréquentes.** Tester `dot == 0` ; utiliser `math.isclose` sans `abs_tol` ; ignorer le paramètre `tol`.
