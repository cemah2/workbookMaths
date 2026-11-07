# M05b · Fonctions de plusieurs variables et gradient — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 📈 🗣️ Pont, lecture, graphique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M05b.Q1 — Lire des lignes de niveau
1. **Non** : en un point commun aux deux lignes, $f$ aurait deux valeurs différentes. Une fonction n'a qu'une valeur en chaque point.
2. $f$ varie **vite** à cet endroit : on change de niveau en peu de distance, la pente est forte (le gradient est long, fiche §4).
3. Les droites $x + y = c$, c'est-à-dire $y = -x + c$ : des droites **parallèles**, de pente $-1$, régulièrement espacées.
4. Le **cercle** de centre $(0, 0)$ et de rayon 3.
5. **Vrai** : la ligne de niveau $-1$ de $x^2 + y^2$ est vide, car $x^2 + y^2 \ge 0$.
6. Un **sommet** (un maximum local), comme le sommet d'une colline sur une carte de randonnée.

### M05b.Q2 — Dérivées partielles : vrai ou faux
1. **Vrai** : $y^3$ est une constante quand on dérive par rapport à $x$.
2. **Vrai** : $x^2$ est une constante quand on dérive par rapport à $y$.
3. **Vrai** : l'expression ne dépend pas de $x$.
4. **Vrai** : c'est la définition (fiche §2, « Figer une variable »).
5. **Faux** : $f$ ne dépend pas de $x$, mais elle peut dépendre de $y$ ; par exemple $f(x, y) = y^2$.
6. **Faux** : par la règle de la chaîne, $\frac{\partial}{\partial x}\big(e^{xy}\big) = y\,e^{xy}$.

### M05b.Q3 — Où pointe le gradient ?
1. Dans la direction de **plus grande montée** de $f$ en $\mathbf{p}$.
2. Un **angle droit** : le gradient est orthogonal à la ligne de niveau.
3. $\|\nabla f(\mathbf{p})\|$, la plus grande pente possible en $\mathbf{p}$.
4. $\nabla f = (-2x, -2y)$, donc $\nabla f(1, 0) = (-2, 0)$ : il pointe vers l'**origine**, le sommet de ce dôme rond. (Sur un dôme allongé, il ne viserait pas le sommet, fiche §4.)
5. **Vrai** : un sommet lisse est un maximum local, donc un point critique.
6. La direction ne change pas, la norme double : $\nabla(2f) = 2\,\nabla f$ (toutes les pentes doublent).

### M05b.Q4 — La dérivée directionnelle
1. $D_{\mathbf{u}} f(\mathbf{p}) = \nabla f(\mathbf{p}) \cdot \mathbf{u}$, avec $\|\mathbf{u}\| = 1$.
2. $(3, -1) \cdot (0, 1) = -1$.
3. $\frac{(2, 2) \cdot (1, 1)}{\sqrt{2}} = \frac{4}{\sqrt{2}} = 2\sqrt{2} \approx 2{,}83$ (et non 4 : le vecteur $(1, 1)$ n'est pas unitaire).
4. **Vrai** : $\nabla f \cdot (-\mathbf{u}) = -\nabla f \cdot \mathbf{u}$. Faire demi-tour change le signe de la pente.
5. $\|(5, 12)\| = \sqrt{25 + 144} = 13$.
6. $\big(\frac{12}{13}, -\frac{5}{13}\big)$ et $\big(-\frac{12}{13}, \frac{5}{13}\big)$, les deux vecteurs unitaires orthogonaux à $(5, 12)$.

### M05b.Q5 — Le plan tangent
1. $z = f(a, b) + \frac{\partial f}{\partial x}(a, b)\,(x - a) + \frac{\partial f}{\partial y}(a, b)\,(y - b)$.
2. $f(1, 1) = 2$, $f_x = 2x = 2$, $f_y = 1$ : $z = 2 + 2(x - 1) + (y - 1)$, soit $z = 2x + y - 1$.
3. $2{,}2 + 0{,}9 - 1 = 2{,}1$, contre la valeur exacte $1{,}21 + 0{,}9 = 2{,}11$.
4. **Vrai** : une fonction affine $z = Ax + By + C$ est un plan, son propre plan tangent en tout point.
5. **Faux** : en $(0, 0)$, le cône a une pointe ; aucun plan ne l'y touche (fiche §5).
6. **Horizontal** : $f_x = f_y = 0$, donc $z = f(a, b)$.

### M05b.Q6 — Minimum, maximum ou selle ?
1. $D = 2 \times 3 - 1 = 5 > 0$ et $f_{xx} > 0$ : **minimum local**.
2. $D = (-4)(-1) - 1 = 3 > 0$ et $f_{xx} < 0$ : **maximum local**.
3. $D = 1 - 9 = -8 < 0$ : **point selle**, alors que $f_{xx}$ et $f_{yy}$ sont positifs (le terme croisé l'emporte).
4. $D = 16 - 16 = 0$ : le test **ne conclut pas**.
5. **Vrai** : un point selle est, par définition, un point critique qui n'est ni un minimum ni un maximum local.
6. **Faux** : $f_{xx} = 2$, $f_{yy} = 12y^2 = 0$ et $f_{xy} = 0$ en $(0, 0)$, donc $D = 0$. Le test ne voit pas ce minimum.

### M05b.Q7 — Descendre ou monter
1. $\mathbf{x}_{k+1} = \mathbf{x}_k - \eta\,\nabla f(\mathbf{x}_k)$, avec $\eta > 0$.
2. Un pas de **montée**, $\mathbf{x} + \eta\,\nabla f(\mathbf{x})$ ; ou, ce qui revient au même, un pas de descente sur $-\ln$ de la vraisemblance.
3. $\nabla f = (2x, 8y) = (2, 8)$ : $(1, 1) - 0{,}1 \times (2, 8) = (0{,}8 ;\ 0{,}2)$.
4. Le pas vaut $\eta\,\|\nabla f(\mathbf{x})\|$ : près d'un minimum (un point critique), le gradient tend vers $\mathbf{0}$, et les pas raccourcissent d'eux-mêmes.
5. De $\eta\,\|\nabla f(\mathbf{x})\|^2$ environ.
6. $\arg\min f = (-2, 1)$ et $\min f = 0$ : une somme de carrés, nulle seulement en ce point.

<a id="rappels"></a>

## 🔁 Rappels

### M05b.R1 — Dériver une composée (R7)
1. $5(3x^2 + 1)^4 \times 6x = 30x\,(3x^2 + 1)^4$.
2. $(6x - 1)\,e^{3x^2 - x}$.
3. $\frac{2x}{1 + x^2}$.
4. $-\frac{1}{2\sqrt{4 - x}}$.
5. $2\cos(2x + 1)$.

### M05b.R2 — Produit scalaire et norme (R9)
1. $6 - 4 = 2$.
2. $\sqrt{4 + 1} = \sqrt{5} \approx 2{,}236$.
3. $\frac{(8, 15)}{17} \approx (0{,}471 ;\ 0{,}882)$ ($\sqrt{64 + 225} = 17$).
4. $\cos\theta = \frac{1}{1 \times \sqrt{2}}$, donc $\theta = 45°$.
5. $(5, -2)$, ou tout multiple non nul : $2 \times 5 + 5 \times (-2) = 0$.

### M05b.R3 — Dérivée seconde et convexité (M05a)
1. $f''(x) = 6x \ge 0 \iff x \ge 0$ : sur $[0, +\infty[$.
2. $c$ est un **minimum local** (test de la dérivée seconde, M05a §2).
3. **Oui** : $(e^{2x})'' = 4e^{2x} > 0$ partout.
4. $f'(x) = -\sin x + x$ et $f''(x) = 1 - \cos x$ valent 0 en 0 : le test **ne conclut pas**. (En fait, $\cos x \ge 1 - \frac{x^2}{2}$ pour tout $x$ : $f \ge 1 = f(0)$, un minimum.)
5. La façon dont la courbe tourne : $f'' > 0$, elle tourne vers le haut (convexe, une cuvette) ; $f'' < 0$, vers le bas (concave). Le §6 de la fiche en fait une courbure **dans une direction**.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M05b.1 — Les lignes de niveau de trois fonctions

**Réponses** : a) `3` · b) `3` · c) `6` · d) `2` · e) `13` · f) `-2` · g) `True` · h) `False`.

**Démarche.**
- a) $3 \times 2 - y + 2 = 5$, donc $y = 3$.
- b) $3x - y + 2 = c \iff y = 3x + 2 - c$ : quel que soit $c$, une droite de pente 3. Les lignes de niveau d'une fonction affine sont des droites parallèles.
- c) et d) Sur l'axe des $x$ ($y = 0$) : $x^2 = 36$, $x = 6$ ; sur l'axe des $y$ ($x = 0$) : $9y^2 = 36$, $y^2 = 4$, $y = 2$. La ligne $f_2 = 36$ est une ellipse, allongée selon $x$.
- e) $f_2(2, 1) = 4 + 9 = 13$.
- f) $y - x^2 = -2 \iff y = x^2 - 2$ : une parabole tournée vers le haut, dont le point le plus bas est $(0, -2)$.
- g) $4 - (-2)^2 = 0$ : oui.
- h) $x^2 + 9y^2 \ge 0 > -1$ : la ligne est vide.

Pour la copie : les lignes 9, 36 et 81 de $f_2$ coupent l'axe des $x$ en 3, 6, 9 et l'axe des $y$ en 1, 2, 3. Elles sont trois fois plus serrées dans la direction de $y$ : $f_2$ y varie plus vite, à cause du coefficient 9.

**Erreurs fréquentes.** Une erreur de signe en isolant $y$ ($-3$ en a) ou b)) ; s'arrêter à $x^2 = 36$ ou $y^2 = 4$ (c et d) ; oublier le carré de $x$ en e) ($2 + 9 = 11$) ; répondre `True` en h) sans regarder le signe de $f_2$.

**Variante.** Où la ligne de niveau 16 de $x^2 + 4y^2$ coupe-t-elle les axes ? *Réponse* : en $x = \pm 4$ et en $y = \pm 2$ : une ellipse deux fois plus longue que haute.

### Ex M05b.2 — Dérivées partielles

**Réponses** : a) `"12*x**2*y + 7"` · b) `"4*x**3 - 2*y"` · c) `-17` · d) `8` · e) `2` · f) `-1` · g) `6` · h) `-4`.

**Démarche.**
- a) $y$ est une constante : $\frac{\partial}{\partial x}(4x^3 y) = 12x^2 y$, $\frac{\partial}{\partial x}(-y^2) = 0$, $\frac{\partial}{\partial x}(7x) = 7$.
- b) $x$ est une constante : $\frac{\partial}{\partial y}(4x^3 y) = 4x^3$, $\frac{\partial}{\partial y}(-y^2) = -2y$, et $7x$ disparaît.
- c) $12 \times 1 \times (-2) + 7 = -17$ ; d) $4 + 4 = 8$.
- e) et f) Par la règle de la chaîne (R7), $\frac{\partial g}{\partial x} = 2\,e^{2x - y}$ et $\frac{\partial g}{\partial y} = -e^{2x - y}$. En $(0{,}5 ;\ 1)$, $2x - y = 0$ : 2 et $-1$.
- g) $\frac{\partial h}{\partial z} = 3x\,y^2 z^2 = 3 \times 2 \times 1 \times 1 = 6$ ; h) $\frac{\partial h}{\partial y} = 2x\,y\,z^3 = 2 \times 2 \times 1 \times (-1) = -4$.

Pour la copie : la tranche $x \mapsto f(x, -2) = -8x^3 - 4 + 7x$ a pour dérivée $-24x^2 + 7$, qui vaut $-17$ en 1 : c'est bien c). Les deux dérivées de $g$ ont le facteur $e^{2x - y}$ parce que la dérivée de $e^{u}$ est $e^{u}$ fois la dérivée de $u$ ; seul ce dernier facteur change (2 ou $-1$).

**Erreurs fréquentes.** Dériver aussi la variable figée ($12x^2$ au lieu de $12x^2 y$ en a)), ou ne pas dériver $4x^3 y$ par rapport à $y$ en b) (le garder tel quel) ; garder $7$ en b) ou supprimer $-y^2$ à tort ; oublier le facteur de la règle de la chaîne (e et f) ; perdre le signe de $z$ en h).

**Variante.** $\frac{\partial}{\partial y}\big(x\,e^{xy}\big)$ ? *Réponse* : $x \times x\,e^{xy} = x^2 e^{xy}$.

### Ex M05b.3 — Le gradient en un point et sa norme

**Réponses** : a) `[12, 1]` · b) `12.0416` · c) `[0, -3]` · d) `[-1.732, 1.732]` · e) `[0.9965, 0.083]` · f) `2.8284`.

**Démarche.** $f_x = 2xy$ et $f_y = x^2 - 3$.
- a) $\nabla f(2, 3) = (12, 4 - 3) = (12, 1)$ ; b) $\sqrt{144 + 1} = \sqrt{145} \approx 12{,}0416$.
- c) $\nabla f(0, 5) = (0, -3)$.
- d) $2xy = 0$ et $x^2 = 3$ : $x = \pm\sqrt{3}$, donc $x \ne 0$ et $y = 0$. Deux points critiques, $(-\sqrt{3}, 0)$ et $(\sqrt{3}, 0)$.
- e) $\frac{(12, 1)}{\sqrt{145}} \approx (0{,}9965 ;\ 0{,}0830)$ : presque la direction de l'axe des $x$.
- f) $\nabla f(1, 1) = (2, -2)$, de norme $\sqrt{8} = 2\sqrt{2} \approx 2{,}8284$.

Pour la copie : aux deux points de d), $f = 0 - 0 + 1 = 1$.

**Erreurs fréquentes.** Oublier la dérivée de $-3y$ dans $f_y$ (a : `[12, 4]`) ; donner $\|\nabla f\|^2$ au lieu de $\|\nabla f\|$ (b, f) ; oublier la solution négative en d) ; donner le gradient lui-même en e).

**Variante.** $\nabla(x y^2)$ en $(1, 2)$ et sa norme ? *Réponse* : $(y^2, 2xy) = (4, 4)$, de norme $4\sqrt{2} \approx 5{,}657$.

### Ex M05b.4 — La dérivée directionnelle dans plusieurs directions

**Réponses** : a) `10` · b) `2` · c) `0.88` · d) `5.6569` · e) `-5.7` · f) `10.198` · g) `56.31`.

**Démarche.** $f_x = 6x - 2y$ et $f_y = -2x + 2y$, donc $\nabla f(2, 1) = (10, -2)$.
- a) $(10, -2) \cdot (1, 0) = 10$ ; b) $(10, -2) \cdot (0, -1) = 2$.
- c) $\|(7, 24)\| = 25$, donc $\mathbf{u} = (0{,}28 ;\ 0{,}96)$ : $2{,}8 - 1{,}92 = 0{,}88$.
- d) $\frac{10 - 2}{\sqrt{2}} = 4\sqrt{2} \approx 5{,}6569$.
- e) $Q - P = (-5, 12)$, de norme 13 : $\frac{-50 - 24}{13} = -\frac{74}{13} \approx -5{,}7$. $f$ descend quand on va vers $Q$.
- f) $\|\nabla f(P)\| = \sqrt{104} = 2\sqrt{26} \approx 10{,}198$.
- g) $\cos\theta = \frac{(10, -2) \cdot (1, 1)}{\sqrt{104}\,\sqrt{2}} = \frac{8}{\sqrt{208}} \approx 0{,}5547$, donc $\theta \approx 56{,}31°$.

Pour la copie : $\|\nabla f\|\cos\theta = 10{,}198 \times 0{,}5547 \approx 5{,}657$, c'est d). La pente est nulle dans les deux directions orthogonales au gradient, $\pm\frac{(1, 5)}{\sqrt{26}} \approx \pm(0{,}1961 ;\ 0{,}9806)$ : celles de la ligne de niveau qui passe par $P$.

**Erreurs fréquentes.** Ne pas diviser par la norme (c : 22 ; d : 8 ; e : $-74$) ; prendre $P - Q$ au lieu de $Q - P$ (e : 5,7) ; donner l'angle en radians (g : 0,98).

**Variante.** La pente de $x^2 + y^2$ en $(1, 2)$ dans la direction du vecteur $(1, -1)$ ? *Réponse* : $\frac{(2, 4) \cdot (1, -1)}{\sqrt{2}} = -\sqrt{2} \approx -1{,}414$.

### Ex M05b.5 — Monter le plus vite : la direction et la valeur de la plus grande pente

**Réponses** : a) `[-5, -3]` · b) `5.831` · c) `210.96` · d) `5.692` · e) `12.53` · f) `"-5/3"`.

**Démarche.** $T_x = -2x + y$ et $T_y = -6y + x$, donc $\nabla T(3, 1) = (-5, -3)$.
- b) La plus grande pente vaut $\|\nabla T(P)\| = \sqrt{34} \approx 5{,}831$ °C/cm.
- c) Le gradient $(-5, -3)$ pointe vers le bas et vers la gauche (troisième quadrant). L'angle aigu avec l'axe vaut $\arctan\frac{3}{5} \approx 30{,}96°$, donc l'angle cherché vaut $180° + 30{,}96° \approx 210{,}96°$.
- d) $O - P = (-3, -1)$, de norme $\sqrt{10}$ : $\frac{(-5, -3) \cdot (-3, -1)}{\sqrt{10}} = \frac{18}{\sqrt{10}} \approx 5{,}692$ °C/cm.
- e) $\cos\theta = \frac{18}{\sqrt{34}\,\sqrt{10}} = \frac{18}{\sqrt{340}} \approx 0{,}9762$, donc $\theta \approx 12{,}53°$.
- f) La tangente à l'isotherme est orthogonale au gradient : elle est dirigée par $(3, -5)$ (produit scalaire $-15 + 15 = 0$), de pente $\frac{-5}{3}$. Avec l'équation de M05b.12, $-5(x - 3) - 3(y - 1) = 0$, soit $y = -\frac{5}{3}x + 6$.

Pour la copie : vers $O$, la pente vaut $\|\nabla T\|\cos 12{,}53° = 5{,}831 \times 0{,}9762 \approx 5{,}692$, un peu moins que la plus grande pente. Le gradient ne vise pas le point le plus chaud : il suit la montée la plus raide **sur le moment**, à angle droit de l'isotherme, et l'isotherme, une ellipse inclinée, n'est pas un cercle centré en $O$ (fiche §4).

**Erreurs fréquentes.** Oublier le terme $xy$ en dérivant (a : `[-6, -6]`) ; donner $\|\nabla T\|^2$ en b) ; en c), donner l'angle aigu $30{,}96°$ sans regarder le quadrant, ou un angle négatif ; ne pas normaliser $O - P$ (d : 18), partir de $O$ vers $P$, ou calculer le taux moyen $\frac{T(O) - T(P)}{\|OP\|}$ au lieu du taux en $P$ ; en f), prendre la pente de la droite dirigée par le gradient ($\frac{3}{5}$) au lieu de celle de la tangente.

**Variante.** En $(1, 2)$ ? *Réponse* : $\nabla T(1, 2) = (0, -11)$ : la montée la plus rapide suit $(0, -1)$, d'angle 270°, au taux de 11 °C/cm, et la tangente à l'isotherme est horizontale.

### Ex M05b.6 — Le plan tangent et l'approximation d'une valeur

**Réponses** : a) `18` · b) `12` · c) `2.25` · d) `-27` · e) `18.975` · f) `18.9782` · g) `0.0032`.

**Démarche.**
- a) $9 \times 2 = 18$.
- b) $f_x = 2x\sqrt{y} = 2 \times 3 \times 2 = 12$ ; c) $f_y = \frac{x^2}{2\sqrt{y}} = \frac{9}{4} = 2{,}25$.
- d) $z = 18 + 12(x - 3) + 2{,}25(y - 4) = 12x + 2{,}25y + 18 - 36 - 9$, donc $C = -27$.
- e) $18 + 12 \times 0{,}1 + 2{,}25 \times (-0{,}1) = 18{,}975$.
- f) $3{,}1^2 \times \sqrt{3{,}9} = 9{,}61 \times 1{,}97484 \approx 18{,}9782$ ; g) $18{,}9782 - 18{,}975 \approx 0{,}0032$.

Pour la copie : avec un déplacement de $(0{,}2 ;\ -0{,}2)$, l'erreur vaut environ $0{,}0114$, à peu près 4 fois plus (3,54 exactement) : l'erreur est d'ordre 2, elle se comporte comme le carré du déplacement (fiche §5). L'écart à 4 vient du terme d'ordre 3, encore visible ici parce que, dans cette direction, les termes d'ordre 2 se compensent en partie ($f_{xx}\,\Delta x^2$ et $2f_{xy}\,\Delta x\,\Delta y$ sont de signes opposés).

**Erreurs fréquentes.** Oublier la racine en a) (36) ; dériver $\sqrt{y}$ quand on dérive par rapport à $x$ ; oublier le facteur $x^2$, ou écrire $\frac{1}{\sqrt{y}}$ au lieu de $\frac{1}{2\sqrt{y}}$ en c) ; donner $C = f(3, 4) = 18$ en d), sans développer ; un déplacement en $y$ de $+0{,}1$ en e).

**Variante.** Le plan tangent à $z = x y^2$ en $(2, 1)$ ? *Réponse* : $f = 2$, $f_x = y^2 = 1$, $f_y = 2xy = 4$ : $z = 2 + (x - 2) + 4(y - 1)$, soit $z = x + 4y - 4$.

### Ex M05b.7 — Dérivées secondes croisées : le théorème de Schwarz vérifié

**Réponses** : a) `"6*x**2*y - exp(x*y) - x*y*exp(x*y)"` · b) `"2*x**3 - x**2*exp(x*y)"` · c) `1.0878` · d) `0.5269` · e) `0.3513` · f) `1.246` · g) `0.193`.

**Démarche.** $f_x = 3x^2 y^2 - y\,e^{xy}$ et $f_y = 2x^3 y - x\,e^{xy}$.
- a) $f_{xy} = \frac{\partial}{\partial y}(3x^2 y^2) - \frac{\partial}{\partial y}(y\,e^{xy}) = 6x^2 y - \big(e^{xy} + y \times x\,e^{xy}\big)$ : $y\,e^{xy}$ est un produit de deux fonctions de $y$.
- b) $f_{yy} = 2x^3 - x \times x\,e^{xy} = 2x^3 - x^2 e^{xy}$.
- c) $f_{xx} = 6xy^2 - y^2 e^{xy}$ : $1{,}5 - 0{,}25\,e^{0{,}5} \approx 1{,}0878$.
- d) $3 - e^{0{,}5} - 0{,}5\,e^{0{,}5} = 3 - 1{,}5\,e^{0{,}5} \approx 0{,}5269$ ; e) $2 - e^{0{,}5} \approx 0{,}3513$.
- f) Avec $\mathbf{u} = \frac{(1, 1)}{\sqrt{2}}$, $u_1^2 = u_2^2 = u_1 u_2 = \frac{1}{2}$ : $\frac{f_{xx} + 2f_{xy} + f_{yy}}{2} \approx 1{,}24647$, soit 1,246 (avec les valeurs arrondies de c), d) et e), on trouve $1{,}24645$ : c'est pourquoi la question ne demande que 3 décimales).
- g) Avec $\mathbf{u} = \frac{(1, -1)}{\sqrt{2}}$, $u_1 u_2 = -\frac{1}{2}$ : $\frac{f_{xx} - 2f_{xy} + f_{yy}}{2} \approx 0{,}19263$, soit 0,193.

Pour la copie : $f_{yx} = \frac{\partial}{\partial x}(2x^3 y - x\,e^{xy}) = 6x^2 y - e^{xy} - xy\,e^{xy}$, la même expression qu'en a) (Schwarz). Les deux courbures diffèrent par le terme croisé $2f_{xy}u_1u_2$, qui change de signe avec la direction : la courbure d'une surface dépend de la direction.

**Erreurs fréquentes.** Un seul des deux termes de la dérivée de $y\,e^{xy}$ en a) ; oublier le facteur $x$ de la règle de la chaîne en b) ; ne pas normaliser la direction en f) et g) (le double) ; oublier le facteur 2 du terme croisé.

**Variante.** Vérifie Schwarz sur $x^2 y^3$. *Réponse* : $f_x = 2xy^3$, $f_{xy} = 6xy^2$ ; $f_y = 3x^2y^2$, $f_{yx} = 6xy^2$.

### Ex M05b.8 — Les points critiques et leur nature (test du second ordre)

**Réponses** : a) `-24` · b) `"A"` · c) `"C"` · d) `-20` · e) `4` · f) `2` · g) `28` · h) `"D"`.

**Démarche.**
- a) à d) $f_x = 3x^2 - 12$ et $f_y = 2y - 4$ s'annulent en $x = \pm 2$ et $y = 2$ : deux points critiques. $f_{xx} = 6x$, $f_{yy} = 2$, $f_{xy} = 0$. En $(-2, 2)$ : $D = (-12) \times 2 - 0 = -24 < 0$, un point selle. En $(2, 2)$ : $D = 12 \times 2 = 24 > 0$ et $f_{xx} = 12 > 0$, un minimum local, où $f = 8 - 24 + 4 - 8 = -20$.
- e) à g) $g_x = 3x^2 + 3y^2 - 15$ et $g_y = 6xy - 12$ : le système se ramène à $x^2 + y^2 = 5$ et $xy = 2$. Alors $(x + y)^2 = 9$ et $(x - y)^2 = 1$, d'où quatre points : $(1, 2)$, $(2, 1)$, $(-1, -2)$, $(-2, -1)$. Avec $g_{xx} = g_{yy} = 6x$ et $g_{xy} = 6y$, $D = 36(x^2 - y^2)$ :

| point | $g_{xx}$ | $g_{yy}$ | $g_{xy}$ | $D$ | nature |
|---|---|---|---|---|---|
| $(1, 2)$ | 6 | 6 | 12 | $-108$ | selle |
| $(2, 1)$ | 12 | 12 | 6 | 108 | minimum local, $g = -28$ |
| $(-1, -2)$ | $-6$ | $-6$ | $-12$ | $-108$ | selle |
| $(-2, -1)$ | $-12$ | $-12$ | $-6$ | 108 | maximum local, $g = 28$ |

- h) Pour $(x + y)^2$ en $(0, 0)$ : $f_{xx} = f_{yy} = f_{xy} = 2$, donc $D = 4 - 4 = 0$ : le test ne conclut pas. Pourtant $(x + y)^2 \ge 0 = f(0, 0)$ : c'est un minimum (global, mais pas strict : $f$ vaut 0 sur toute la droite $y = -x$, un fond de vallée plat), que l'on voit sur la fonction elle-même.

**Erreurs fréquentes.** Oublier le signe de $f_{xx}(-2, 2)$ (a : 24) ; conclure d'après le seul signe de $f_{xx}$ en $(-2, 2)$ (B) au lieu de calculer $D$ ; ne garder que les solutions positives du système de $g$ (e : 2) ; donner la valeur du minimum local en g) ($-28$) ; répondre « minimum » en h) : c'est la vraie nature, mais pas la réponse du test.

**Variante.** La nature de $(0, 0)$ pour $x^2 - 4xy + y^2$ ? *Réponse* : $D = 2 \times 2 - 16 = -12 < 0$ : un point selle (le long de $y = x$, $f = -2x^2$ ; le long de $y = -x$, $f = 6x^2$).

### Ex M05b.9 — Pourquoi un petit pas contre le gradient fait baisser f : le calcul au premier ordre

**Réponses** : a) `[2, 3]` · b) `[0.9, 0.85]` · c) `1.411` · d) `1.35` · e) `0.589` · f) `2.714` · g) `"1/130"`.

**Démarche.** $\nabla f = (2xy,\ x^2 + 2y)$, donc $\nabla f(1, 1) = (2, 3)$ et $\|\nabla f(P)\|^2 = 13$.
- b) $(1, 1) - 0{,}05 \times (2, 3) = (0{,}9 ;\ 0{,}85)$ ; c) $0{,}81 \times 0{,}85 + 0{,}85^2 = 0{,}6885 + 0{,}7225 = 1{,}411$.
- d) $2 - 0{,}05 \times 13 = 1{,}35$ ; e) $2 - 1{,}411 = 0{,}589$.
- f) $(1{,}1 ;\ 1{,}15)$ : $1{,}21 \times 1{,}15 + 1{,}15^2 = 1{,}3915 + 1{,}3225 = 2{,}714$.
- g) $13\,\eta = 0{,}1$, donc $\eta = \frac{1}{130}$.

Pour la copie : la baisse réelle (0,589) est un peu plus petite que la prévision (0,65), et la hausse de f) (0,714) un peu plus grande. L'écart vient du terme d'ordre 2, positif ici dans la direction du gradient (environ 0,06 dans les deux cas : la courbure de $f$ dans cette direction est positive). Le développement : $f(P + \mathbf{h}) \approx f(P) + \nabla f(P) \cdot \mathbf{h}$ avec $\mathbf{h} = -\eta\,\nabla f(P)$ donne $f(P) - \eta\,\|\nabla f(P)\|^2$.

**Erreurs fréquentes.** Oublier le terme $2y$ dans $f_y$ (a : `[2, 1]`) ; ajouter le gradient au lieu de le retirer (b) ; prévoir avec $\|\nabla f\|$ au lieu de $\|\nabla f\|^2$ (d) ; viser une baisse de 1 au lieu de 0,1 en g).

**Variante.** Même calcul pour $x^2 + 3y^2$ depuis $(1, 1)$ avec $\eta = 0{,}05$. *Réponse* : $\nabla f = (2, 6)$, le point $(0{,}9 ;\ 0{,}7)$, où $f = 0{,}81 + 1{,}47 = 2{,}28$ ; la prévision donnait $4 - 0{,}05 \times 40 = 2$.

### Ex M05b.10 — argmin et argmax sur un segment

**Réponses** : a) `0.4` · b) `[1.6, 1.2]` · c) `0.8` · d) `[4, 0]` · e) `8` · f) `[1, 0]` · g) `-1` · h) `0`.

**Démarche.** $g(t) = 16t^2 + (2 - 2t)^2 - 8t = 20t^2 - 16t + 4$, de dérivée $40t - 16$, nulle en $t = 0{,}4$.

| $t$ | 0 | | 0,4 | | 1 |
|---|---|---|---|---|---|
| $g'(t)$ | | $-$ | 0 | $+$ | |
| $g$ | 4 | ↘ | 0,8 | ↗ | 8 |

- b) et c) En $t = 0{,}4$ : le point $(1{,}6 ;\ 1{,}2)$, où $f = 2{,}56 + 1{,}44 - 3{,}2 = 0{,}8$.
- d) et e) Le maximum est à une extrémité : $g(0) = 4$ (en $A$), $g(1) = 8$ (en $B$), donc $\arg\max = (4, 0)$ et $\max = 8$.
- f) et g) $f = (x - 1)^2 + y^2 - 1$ : $\arg\min f = (1, 0)$ et $\min f = -1$ sur tout le plan, un point qui n'est pas sur le segment.
- h) $\nabla f = (2x - 2,\ 2y) = (1{,}2 ;\ 2{,}4)$ en $(1{,}6 ;\ 1{,}2)$, et $(1{,}2 ;\ 2{,}4) \cdot (4, -2) = 4{,}8 - 4{,}8 = 0$.

Pour la copie : h) dit qu'au minimum sur le segment, le gradient est orthogonal au segment ; autrement dit, la ligne de niveau de $f$ qui passe par ce point (un cercle de centre $(1, 0)$) y est **tangente** au segment. C'est le point du segment le plus proche de $(1, 0)$.

**Erreurs fréquentes.** Une erreur en développant $(2 - 2t)^2$ ; donner $t$ au lieu du point en b), ou au lieu de $f$ en c) ; oublier de comparer les deux extrémités pour le maximum ; confondre le minimum sur le segment et le minimum sur le plan.

**Variante.** Le minimum de $x^2 + y^2$ sur le segment de $(0, 2)$ à $(2, 0)$ ? *Réponse* : $g(t) = 8t^2 - 8t + 4$, minimal en $t = \frac{1}{2}$ : au point $(1, 1)$, où $f = 2$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M05b.11 — La dérivée directionnelle vaut ∇f · u, et la plus grande pente

**Réponse modèle.**
1. $g(t) = f(\mathbf{p} + t\,\mathbf{u})$ est la valeur de $f$ quand on avance de $t$ en ligne droite depuis $\mathbf{p}$ dans la direction $\mathbf{u}$, et $g(0) = f(\mathbf{p})$. Par définition, $D_{\mathbf{u}} f(\mathbf{p}) = \lim_{t \to 0} \frac{f(\mathbf{p} + t\mathbf{u}) - f(\mathbf{p})}{t} = \lim_{t \to 0} \frac{g(t) - g(0)}{t}$, qui est la définition de $g'(0)$.
2. Avec $x(t) = a + t u_1$ et $y(t) = b + t u_2$, on a $x'(t) = u_1$ et $y'(t) = u_2$. La règle de la chaîne donne $g'(t) = f_x(x(t), y(t))\,u_1 + f_y(x(t), y(t))\,u_2$, et en $t = 0$ : $g'(0) = f_x(\mathbf{p})\,u_1 + f_y(\mathbf{p})\,u_2 = \nabla f(\mathbf{p}) \cdot \mathbf{u}$.
3. Par l'inégalité de Cauchy-Schwarz (ou avec $\nabla f \cdot \mathbf{u} = \|\nabla f\|\,\|\mathbf{u}\|\cos\theta$, R9) : $|\nabla f(\mathbf{p}) \cdot \mathbf{u}| \le \|\nabla f(\mathbf{p})\|\,\|\mathbf{u}\| = \|\nabla f(\mathbf{p})\|$, car $\|\mathbf{u}\| = 1$.
4. Pour $\mathbf{u}^* = \frac{\nabla f(\mathbf{p})}{\|\nabla f(\mathbf{p})\|}$ (unitaire) : $\nabla f \cdot \mathbf{u}^* = \frac{\|\nabla f\|^2}{\|\nabla f\|} = \|\nabla f\|$. Unicité : si $\mathbf{u}$ est unitaire et $\nabla f \cdot \mathbf{u} = \|\nabla f\|$, alors $\mathbf{u} \cdot \mathbf{u}^* = 1$, et $\|\mathbf{u} - \mathbf{u}^*\|^2 = \|\mathbf{u}\|^2 - 2\,\mathbf{u} \cdot \mathbf{u}^* + \|\mathbf{u}^*\|^2 = 1 - 2 + 1 = 0$ : $\mathbf{u} = \mathbf{u}^*$. (Avec l'angle : $\cos\theta = 1$ impose $\theta = 0$.)
5. Notons $\nabla f(\mathbf{p}) = (A, B) \ne (0, 0)$. On cherche $\mathbf{u} = (u_1, u_2)$ avec $A u_1 + B u_2 = 0$ et $u_1^2 + u_2^2 = 1$. Les vecteurs orthogonaux à $(A, B)$ sont les multiples $\lambda\,(B, -A)$ (si $A \ne 0$, $u_1 = -\frac{B}{A}u_2$, donc $\mathbf{u} = -\frac{u_2}{A}(B, -A)$ ; de même si $B \ne 0$). La condition $\|\lambda (B, -A)\| = 1$ donne $|\lambda| = \frac{1}{\|\nabla f\|}$ : exactement deux vecteurs, $\pm\frac{(B, -A)}{\sqrt{A^2 + B^2}}$.
6. $g(t) = (1 + 0{,}28t)\,e^{0{,}96t}$, donc $g'(t) = 0{,}28\,e^{0{,}96t} + 0{,}96\,(1 + 0{,}28t)\,e^{0{,}96t}$ et $g'(0) = 0{,}28 + 0{,}96 = 1{,}24$. Par la formule : $\nabla f = (e^y, x\,e^y) = (1, 1)$ en $(1, 0)$, et $(1, 1) \cdot (0{,}28 ;\ 0{,}96) = 1{,}24$.

**Grille.** (1) le lien entre la définition de $D_{\mathbf{u}} f$ et celle de $g'(0)$ ; (2) la règle de la chaîne avec $x' = u_1$, $y' = u_2$, évaluée en $t = 0$ ; (3) Cauchy-Schwarz (ou le cosinus) et l'usage de $\|\mathbf{u}\| = 1$ ; (4) la valeur atteinte **et** l'unicité ; (5) la droite des vecteurs orthogonaux, coupée par le cercle unité : deux vecteurs ; (6) le calcul direct de $g'(0)$ et la comparaison.

### Ex M05b.12 — Le gradient est orthogonal aux lignes de niveau

**Réponse modèle.**
1. La fonction $h(t) = f(\boldsymbol{\gamma}(t))$ est constante, égale à $c$ : $h'(t) = 0$. Par la règle de la chaîne, $h'(t) = f_x(\boldsymbol{\gamma}(t))\,x'(t) + f_y(\boldsymbol{\gamma}(t))\,y'(t) = \nabla f(\boldsymbol{\gamma}(t)) \cdot \boldsymbol{\gamma}'(t)$. Donc $\nabla f(\boldsymbol{\gamma}(t)) \cdot \boldsymbol{\gamma}'(t) = 0$ : le gradient est orthogonal au vecteur vitesse $\boldsymbol{\gamma}'(t)$, qui est tangent à la ligne de niveau. Le gradient est perpendiculaire à la ligne de niveau en chacun de ses points.
2. $f(\boldsymbol{\gamma}(t)) = \frac{8\cos^2 t}{4} + 2\sin^2 t = 2$ : la courbe est bien sur la ligne de niveau 2. $\boldsymbol{\gamma}'(t) = (-2\sqrt{2}\sin t,\ \sqrt{2}\cos t)$ et $\nabla f = \big(\frac{x}{2}, 2y\big) = (\sqrt{2}\cos t,\ 2\sqrt{2}\sin t)$ : le produit scalaire vaut $-4\sin t\cos t + 4\sin t\cos t = 0$.
3. Par l'hypothèse admise, la ligne de niveau est, près de $(a, b)$, une courbe $\boldsymbol{\gamma}$ avec $\boldsymbol{\gamma}(t_0) = (a, b)$ : sa tangente passe par $(a, b)$, dirigée par $\boldsymbol{\gamma}'(t_0)$, qui est orthogonal à $\nabla f(a, b) \ne \mathbf{0}$ (question 1). Dans le plan, les vecteurs orthogonaux à un vecteur non nul forment une droite : la direction de la tangente est donc déterminée. Un point $(x, y)$ est sur la tangente si et seulement si $(x - a, y - b)$ est orthogonal à $\nabla f(a, b)$, c'est-à-dire $f_x(a, b)\,(x - a) + f_y(a, b)\,(y - b) = 0$.
4. $k_x = 2xy = 2$ et $k_y = x^2 + 3y^2 = 4$ en $(1, 1)$ : $2(x - 1) + 4(y - 1) = 0$, soit $y = -\frac{1}{2}x + \frac{3}{2}$.
5. Partons de $\mathbf{p}$, sur la ligne $c$, et avançons d'une distance $s$ dans la direction d'un vecteur unitaire $\mathbf{u}$. Au premier ordre, $f(\mathbf{p} + s\mathbf{u}) \approx c + s\,\nabla f(\mathbf{p}) \cdot \mathbf{u}$. On atteint la ligne $c + \Delta c$ quand $s\,\nabla f \cdot \mathbf{u} = \Delta c$, soit $s = \frac{\Delta c}{\nabla f \cdot \mathbf{u}}$. Dans la direction du gradient, $\nabla f \cdot \mathbf{u} = \|\nabla f\|$ et $s = \frac{\Delta c}{\|\nabla f\|}$. Dans une autre direction qui monte, $\nabla f \cdot \mathbf{u} = \|\nabla f\|\cos\theta < \|\nabla f\|$ (M05b.11) : $s$ est plus grand. Le gradient donne le chemin le plus court entre deux lignes voisines, d'où « lignes serrées, gradient long ».

**Grille.** (1) $h$ constante, la règle de la chaîne, et l'interprétation de $\boldsymbol{\gamma}'$ comme vecteur tangent ; (2) la vérification que $\boldsymbol{\gamma}$ est sur la ligne **et** le produit scalaire nul ; (3) l'équation obtenue par l'orthogonalité, avec l'hypothèse $\nabla f \ne \mathbf{0}$ ; (4) la tangente sous la forme $y = mx + p$ ; (5) l'approximation linéaire, la distance $\frac{\Delta c}{\nabla f \cdot \mathbf{u}}$ et la comparaison avec le cosinus.

### Ex M05b.13 — Le test du second ordre pour ax² + bxy + cy²

**Réponse modèle.**
1. $q_x = 2ax + by$ et $q_y = bx + 2cy$ s'annulent en $(0, 0)$. $q_{xx} = 2a$, $q_{yy} = 2c$, $q_{xy} = b$, donc $q_{xx}q_{yy} - q_{xy}^2 = 4ac - b^2$.
2. $(2ax + by)^2 + (4ac - b^2)\,y^2 = 4a^2x^2 + 4abxy + b^2y^2 + 4acy^2 - b^2y^2 = 4a\,(ax^2 + bxy + cy^2) = 4a\,q(x, y)$.
3. Supposons $4ac - b^2 > 0$ et $(x, y) \ne (0, 0)$. Si $y \ne 0$, le second terme est strictement positif et le premier positif ou nul : $4a\,q > 0$. Si $y = 0$, alors $x \ne 0$ et $q = ax^2$, du signe de $a$, donc encore $4a\,q = 4a^2x^2 > 0$. Ainsi $4a\,q(x, y) > 0$ : si $a > 0$, $q(x, y) > 0 = q(0, 0)$, un minimum strict ; si $a < 0$, $q(x, y) < 0$, un maximum strict.
4. En $(1, 0)$ : $q = a$, du signe de $a$. En $\big(-\frac{b}{2a}, 1\big)$ : le carré s'annule et $4a\,q = 4ac - b^2 < 0$, donc $q$ a le signe opposé à celui de $a$. Comme $q(tx, ty) = t^2 q(x, y)$, ces deux signes se retrouvent en des points aussi proches que l'on veut de $(0, 0)$ (prendre $t$ petit) : $q$ prend, tout près de l'origine, des valeurs plus grandes et plus petites que $q(0, 0) = 0$. C'est un point selle.
5. $q = bxy + cy^2 = y\,(bx + cy)$. Sur la droite $x = k\,y$ : $q = y^2\,(bk + c)$. Comme $b \ne 0$, on peut choisir $k$ avec $bk + c > 0$ et $k$ avec $bk + c < 0$ : près de l'origine, $q$ prend les deux signes, c'est un point selle (et $D = -b^2 < 0$, comme le test l'annonce).
6. Avec $a = f_{xx}$, $b = 2f_{xy}$ et $c = f_{yy}$ (les dérivées prises en $\mathbf{p}$), $q(\Delta x, \Delta y)$ est la parenthèse de la fiche, et $4ac - b^2 = 4\,(f_{xx}f_{yy} - f_{xy}^2) = 4D$, du signe de $D$. Les questions 3 à 5 donnent : $D > 0$ et $f_{xx} > 0$, le terme d'ordre 2 est positif dans toutes les directions (minimum local) ; $D > 0$ et $f_{xx} < 0$, négatif partout (maximum local) ; $D < 0$, des deux signes (selle).
7. Pour $x^2 + y^4$ et $x^2 - y^4$ : $f_{xx} = 2$, $f_{xy} = 0$, $f_{yy} = \pm 12y^2 = 0$ en $(0, 0)$, donc $D = 0$. $x^2 + y^4 \ge 0$ : minimum. $x^2 - y^4$ vaut $x^2 > 0$ sur l'axe des $x$ et $-y^4 < 0$ sur l'axe des $y$ : point selle. Les deux fonctions ont le même terme d'ordre 2, $x^2$, nul dans la direction de $y$ : tout se joue au terme d'ordre 4 ($\pm y^4$), que les dérivées secondes ne voient pas. Le test, qui n'utilise que les dérivées secondes, ne peut donc pas trancher.

**Grille.** (1) le point critique et $D = 4ac - b^2$ ; (2) le développement de l'identité ; (3) les deux cas $y \ne 0$ et $y = 0$, et la conclusion selon le signe de $a$ ; (4) deux points explicites de signes opposés, et l'argument $q(tx, ty) = t^2 q$ pour s'approcher de l'origine ; (5) la factorisation et le choix de $k$ ; (6) la correspondance $a, b, c$, le facteur 4 (ce n'est pas encore une démonstration complète du test pour $f$ : le « $\approx$ » néglige un reste, qu'il faudrait majorer ; la question 7 montre justement où cela peut échouer) ; (7) $D = 0$ pour les deux, deux natures différentes, et l'idée que l'ordre 2 ne voit pas le terme qui décide.

<a id="reflexion"></a>

## 🔗 📖 📈 🗣️ Pont, lecture, graphique et explication

### Ex M05b.14 — La loss d'un neurone à deux poids sur deux exemples : son gradient

**Réponses** : a) `0.625` · b) `-2.5` · c) `2.0` · d) `[0.75, 0.3]` · e) `0.0625` · f) `[0.7143, 0.1429]`.

**Démarche.** Avec $\mathbf{w} = (0{,}5 ;\ 0{,}5)$ : $\hat{y}^{(1)} = 0{,}5 + 1 = 1{,}5$ (erreur $0{,}5$) et $\hat{y}^{(2)} = 1{,}5 - 0{,}5 = 1$ (erreur $-1$).
- a) $L = \frac{1}{2}(0{,}25 + 1) = 0{,}625$.
- b) et c) La dérivée de $\frac{1}{2}(\hat{y} - y)^2$ par rapport à $w_j$ est $(\hat{y} - y)\,x_j$ (règle de la chaîne ; le $\frac{1}{2}$ compense le 2). Donc $\frac{\partial L}{\partial w_1} = 0{,}5 \times 1 + (-1) \times 3 = -2{,}5$ et $\frac{\partial L}{\partial w_2} = 0{,}5 \times 2 + (-1) \times (-1) = 2$.
- d) $(0{,}5 ;\ 0{,}5) - 0{,}1 \times (-2{,}5 ;\ 2) = (0{,}75 ;\ 0{,}3)$.
- e) $\hat{y}^{(1)} = 0{,}75 + 0{,}6 = 1{,}35$ (erreur 0,35), $\hat{y}^{(2)} = 2{,}25 - 0{,}3 = 1{,}95$ (erreur $-0{,}05$) : $L = \frac{1}{2}(0{,}1225 + 0{,}0025) = 0{,}0625$, dix fois moins.
- f) Les deux erreurs s'annulent si $w_1 + 2w_2 = 1$ et $3w_1 - w_2 = 2$ : $w_2 = 3w_1 - 2$, puis $7w_1 = 5$, soit $\big(\frac{5}{7}, \frac{1}{7}\big) \approx (0{,}7143 ;\ 0{,}1429)$. Le gradient y est nul, puisque chaque terme contient une erreur.

Pour la copie : chaque exemple pèse dans le gradient en proportion de **son erreur** fois son entrée : un exemple bien prédit ne pousse presque pas les poids. Aux poids de f), $L = 0$ : deux équations, deux inconnues, le neurone prédit les deux exemples exactement, et c'est le minimum global ($L \ge 0$). Avec trois exemples incompatibles, aucun poids n'annule toutes les erreurs : le minimum de $L$ est strictement positif (c'est la méthode des moindres carrés, M09b).

**Erreurs fréquentes.** Oublier le $\frac{1}{2}$ (a : 1,25) ou garder le 2 de la dérivée (b : $-5$, c : 4) ; ajouter le gradient au lieu de le retirer (d : `[0.25, 0.7]`) ; inverser l'ordre des poids en f).

**Variante.** $\nabla L$ en $\mathbf{w} = (0, 0)$ ? *Réponse* : les erreurs valent $-1$ et $-2$ : $\nabla L = (-1 - 6,\ -2 + 2) = (-7, 0)$.

### Ex M05b.15 — MML §5.2 : dérivées partielles et gradient, la convention en ligne (lecture guidée)

**Réponse modèle.**
1. Une dérivée partielle est la limite du taux d'accroissement quand on ne fait varier qu'**une** coordonnée, les autres restant fixées. Le gradient rassemble les $n$ dérivées partielles dans un vecteur **ligne** : une matrice $1 \times n$ (le livre l'appelle aussi jacobienne de $f$).
2. Avec $u = x - 3y^2$ : $\frac{\partial f}{\partial x} = 2(x - 3y^2)$ et $\frac{\partial f}{\partial y} = 2(x - 3y^2) \times (-6y) = -12y\,(x - 3y^2)$.
3. $\frac{\partial f}{\partial x_1} = 3x_1^2 x_2 - x_2^2$ et $\frac{\partial f}{\partial x_2} = x_1^3 - 2x_1x_2$ ; en $(1, 2)$ : $6 - 4 = 2$ et $1 - 4 = -3$, soit la ligne $\begin{pmatrix} 2 & -3 \end{pmatrix}$.
4. Par la règle du produit : $2x\,(x - y) + (x^2 + y) \times 1 = 3x^2 - 2xy + y$. En développant d'abord, $x^3 - x^2y + xy - y^2$, dont la dérivée par rapport à $x$ est aussi $3x^2 - 2xy + y$.
5. Par la règle : $\frac{df}{dt} = 2x_1 \times e^t + (-1) \times 2t = 2e^{2t} - 2t$. En remplaçant d'abord : $f = e^{2t} - t^2$, de dérivée $2e^{2t} - 2t$. Les deux calculs concordent.
6. En ligne, la règle de la chaîne s'écrit comme un **produit de matrices** (des jacobiennes), dans le bon ordre et avec les bonnes dimensions, ce qui se généralise aux fonctions à valeurs vectorielles (M17, M18). Avec $\mathbf{x}$ en colonne, le pas de descente demande de transposer : $\mathbf{x} - \eta\,(\nabla f)^\top$. Ce dépôt, comme la plupart des codes, écrit le gradient en colonne, de la même forme que $\mathbf{x}$.
7. Par exemple *partial derivative* (dérivée partielle), *row vector* (vecteur ligne), *chain rule* (règle de la chaîne), *product rule* (règle du produit).

**Grille.** (1) la définition (une seule coordonnée varie) et la forme $1 \times n$ ; (2) à (5) les calculs justes, avec la comparaison demandée en 4 et 5 ; (6) la raison (la règle de la chaîne comme produit de matrices) et la transposition dans le pas de descente ; (7) trois mots traduits. Les réponses sont écrites avec tes mots, pas recopiées.

### Ex M05b.16 — Lire une carte de lignes de niveau : estimer une dérivée partielle

**Réponses** : a) `3` · b) `6` · c) `3` · d) `5` · e) `2` · f) `6`.

**Démarche.** On lit sur la carte $f(A) = 3$, $f(B) = 6$ et $f(C) = 5$. c) $\frac{6 - 3}{2 - 1} = 3$ ; e) $\frac{5 - 3}{2 - 1} = 2$. f) $P$ est entre les lignes $-2$ et $-1$, $Q$ entre les lignes 4 et 5 : le segment traverse les lignes $-1$, 0, 1, 2, 3 et 4, une fois chacune.

Pour la copie : le long de $[PQ]$, les lignes se resserrent quand on va vers $Q$, c'est-à-dire quand $x$ grandit : $\frac{\partial f}{\partial x}$ grandit avec $x$. Dans la direction de $y$, les lignes sont régulièrement espacées (une ligne tous les 0,5 en $y$) : $\frac{\partial f}{\partial y}$ semble constante, égale à 2. Dans la direction de $x$, elles se resserrent quand $|x|$ grandit, et sont horizontales sur l'axe des $y$, où $\frac{\partial f}{\partial x}$ s'annule. La fonction $f(x, y) = x^2 + 2y$ a ces lignes de niveau (les paraboles $y = \frac{c - x^2}{2}$) : $f(1, 1) = 3$ et $f(2, 1) = 6$ ; $f(P) = -1{,}5$ et $f(Q) = 4{,}5$.

**Erreurs fréquentes.** Lire la valeur de la ligne voisine ; diviser par la différence des valeurs au lieu de la distance ; en f), oublier la ligne 0 ou compter une ligne que le segment ne fait que frôler.

**Variante.** Le taux d'accroissement entre $B$ et le point $(2, 2)$ ? *Réponse* : $f(2, 2) = 8$, donc $\frac{8 - 6}{1} = 2$ : la même estimation de $\frac{\partial f}{\partial y}$ qu'entre $A$ et $C$.

### Ex M05b.17 — Expliquer ce que disent des lignes de niveau serrées

**Réponse modèle.**

> Deux courbes voisines sont à des altitudes qui diffèrent toujours de la même quantité, disons 10 mètres. Là où elles sont collées, on monte de 10 mètres en quelques pas : la pente est raide. Là où elles sont espacées, il faut marcher longtemps pour monter autant : c'est presque plat. Le gradient, en chaque point, c'est une flèche qui pointe vers la montée la plus raide : elle traverse les courbes à angle droit, jamais le long d'elles. Sa longueur, c'est la pente dans cette direction : grande là où les courbes sont serrées, petite là où elles s'écartent. Et un sentier qui ne monte ni ne descend, c'est une courbe de niveau elle-même : on la suit, toujours à angle droit de la flèche du gradient, et l'altitude ne change pas.

**Grille.** (1) l'écart entre deux courbes lié à la pente (serré = raide) ; (2) le gradient perpendiculaire aux courbes, vers la montée ; (3) sa longueur grande où les courbes sont serrées ; (4) le sentier plat qui suit une courbe de niveau, à angle droit du gradient ; (5) huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M05b.E1 — Pourquoi le gradient est-il la direction de plus grande pente ?

**Réponse modèle (60 secondes).**

> La pente d'une fonction dans une direction donnée par un vecteur unitaire $\mathbf{u}$, c'est la dérivée directionnelle, et elle vaut le produit scalaire du gradient avec $\mathbf{u}$ : c'est la règle de la chaîne appliquée le long d'une droite. Or un produit scalaire, c'est la norme du gradient fois la norme de $\mathbf{u}$, qui vaut 1, fois le cosinus de l'angle entre eux. Le cosinus est au plus 1, et il vaut 1 quand l'angle est nul : la pente est donc maximale quand on part dans la direction du gradient, et cette pente maximale vaut la norme du gradient. À angle droit, le cosinus est nul : la fonction ne change pas, c'est la direction de la ligne de niveau, d'où le fait que le gradient lui est orthogonal. Et dans la direction opposée, le cosinus vaut $-1$ : c'est la plus forte baisse. La descente de gradient fait donc un petit pas dans la direction de moins le gradient : au premier ordre, la loss baisse du pas fois le carré de la norme du gradient, ce qui est positif tant qu'on n'est pas à un point critique.

**Grille.** (1) la pente dans une direction comme produit scalaire avec un vecteur unitaire ; (2) le cosinus, maximal pour un angle nul, et la valeur maximale $\|\nabla f\|$ ; (3) l'angle droit et les lignes de niveau ; (4) la descente : $-\nabla f$, et la baisse $\eta\,\|\nabla f\|^2$ au premier ordre.

<a id="notebook"></a>

## Notebook

### Ex M05b.18 — Une dérivée partielle par différence centrée · `partial_derivative`

**Réponses** : a) `3.0` · b) `2.25` · c) `-2.0` · d) `"ValueError"` · e) `"ValueError"` · f) `0.8` · g) `"float"`.

**Démarche.** `p = np.array(point, dtype=float)` (la copie que demande le commentaire `TODO`), puis les vérifications **avant** tout calcul : `if not 0 <= i < p.size: raise ValueError(...)` et `if not h > 0: raise ValueError(...)` (ce test refuse aussi `nan`). Ensuite `step = np.zeros_like(p)`, `step[i] = h`, et `return float((f(p + step) - f(p - step)) / (2 * h))`. Pour la copie : a) $2x\,e^y = 3$ ; b) $x^2 e^y = 2{,}25$ ; c) $\frac{\partial}{\partial z}(xyz) = xy = -2$ ; f) $\frac{2y}{x + y^2} = \frac{4}{5}$. Sans les vérifications faites d'abord, d) lève une `IndexError` (l'indice 3 n'existe pas) et e) une `ZeroDivisionError`.

**Erreurs fréquentes.** Une différence avant au lieu d'une différence centrée (a : 3,00001) ; déplacer toutes les coordonnées (c : 2, la somme des trois dérivées partielles) ; compter les indices à partir de 1 (c : 8 ; f : 0,2) ; vérifier `i` après s'en être servi (d : `IndexError`) ; diviser avant de vérifier `h` (e : `ZeroDivisionError`) ; modifier le point de l'appelant ; renvoyer le `numpy.float64` de `f` (g).

### Ex M05b.19 — Dérivée directionnelle et direction de plus grande pente · `directional_derivative, steepest_ascent_direction`

**Réponses** : a) `6.0` · b) `6.364` · c) `0.0` · d) `[0.8944, 0.4472]` · e) `"ValueError"` · f) `"ValueError"` · g) `"ndarray"` · h) `1.0`.

**Démarche.** `directional_derivative` : `p` et `d` en flottants, une `ValueError` si `p.shape != d.shape`, si `np.linalg.norm(d) == 0` ou si `h <= 0`, puis `u = d / norm` et `float((f(p + h * u) - f(p - h * u)) / (2 * h))`. `steepest_ascent_direction` : le gradient, une coordonnée à la fois avec `partial_derivative`, une `ValueError` si sa norme est inférieure à $10^{-8}$, puis `grad / norm`. Pour la copie : $\nabla f(1, 3) = (2xy,\ x^2 + 2) = (6, 3)$ ; a) 6 ; b) $\frac{18}{2\sqrt{2}} \approx 6{,}3640$ ; c) $(6, 3) \cdot (-1, 2) = 0$ : $(-1, 2)$ dirige la ligne de niveau de $f$ qui passe par $(1, 3)$. f) $(0, 0)$ est un minimum local de $x^2 + 2y^2 + y^3$ : le gradient y est nul, aucune direction ne monte plus qu'une autre. Numériquement, les différences centrées donnent $(0, h^2) \approx (0, 10^{-10})$ : un test `norm == 0` laisserait passer ce point, d'où la tolérance $10^{-8}$.

**Erreurs fréquentes.** Oublier de normaliser la direction (b : 18) ; renvoyer le gradient au lieu du vecteur unitaire (d : `[6, 3]` ; h : la norme du gradient) ; tester `norm == 0` au lieu de `norm < 1e-8` (f : aucune erreur) ; diviser par une norme nulle sans lever d'erreur (e : des `nan`, ou une `ZeroDivisionError`) ; renvoyer une liste (g).

### Ex M05b.20 — Le plan tangent · `tangent_plane`

**Réponses** : a) `[1.0, 2.0, 0.0]` · b) `[1.0, 1.0, -1.3069]` · c) `"ValueError"` · d) `0.01034` · e) `True`.

**Démarche.** `p = np.array(point, dtype=float)`, une `ValueError` si `p.shape != (2,)` ou si `h <= 0` ; `a` et `b` les deux dérivées partielles, `c = float(f(p)) - a * p[0] - b * p[1]`, et `return (float(a), float(b), float(c))`. Pour la copie : a) $z = 2 + (x - 2) + 2y = x + 2y$ ; b) $z = \ln 2 + (x - 1) + (y - 1)$, donc $C = \ln 2 - 2 \approx -1{,}3069$ ; d) $2\,e^{0{,}1} \approx 2{,}210342$ contre $2 + 0{,}2 = 2{,}2$ : un écart positif d'environ $0{,}01034$. Dans la direction de $y$, la tranche $y \mapsto 2e^y$ est convexe ($f_{yy} = 2 > 0$) : la surface est au-dessus de son plan, avec un écart proche de $\frac{1}{2}f_{yy}\,\Delta y^2 = 0{,}01$. Mais $D = f_{xx}f_{yy} - f_{xy}^2 = 0 \times 2 - 1 = -1 < 0$ : dans d'autres directions, comme $(2, -1)$, la surface passe au-dessous de son plan ; elle le traverse, comme une selle.

**Erreurs fréquentes.** $C = f(x_0, y_0)$, sans développer le plan (a : `[1.0, 2.0, 2.0]`) ; accepter un point de trois coordonnées (c) ; l'écart pris dans l'autre sens, plan moins $f$ (d) ; renvoyer des `numpy.float64` (e).

### Ex M05b.21 — SymPy : dérivées partielles, gradient, points critiques

**Réponses** : a) `3` · b) `"-1/4"` · c) `-4` · d) `6` · e) `[4, 5]` · f) `"x**2 + 2*y - 1"`.

**Démarche.** `x, y = sp.symbols("x y")`, `k = x**2*y + y**2 - y`, `sp.solve([sp.diff(k, x), sp.diff(k, y)], [x, y], dict=True)` donne les trois points, `sp.hessian(k, (x, y))` la matrice $\begin{pmatrix} 2y & 2x \\ 2x & 2 \end{pmatrix}$. Pour la copie :

| point | $k_{xx}$ | $k_{yy}$ | $k_{xy}$ | $D$ | nature |
|---|---|---|---|---|---|
| $(0, \frac{1}{2})$ | 1 | 2 | 0 | 2 | minimum local, $k = -\frac{1}{4}$ |
| $(1, 0)$ | 0 | 2 | 2 | $-4$ | selle |
| $(-1, 0)$ | 0 | 2 | $-2$ | $-4$ | selle |

$\nabla k = (2xy,\ x^2 + 2y - 1)$ s'annule si $x = 0$ (et alors $y = \frac{1}{2}$) ou si $y = 0$ (et alors $x = \pm 1$). Le minimum local n'est pas global : $k(x, -1) = 2 - x^2$ tend vers $-\infty$.

**Erreurs fréquentes.** Oublier une des solutions de $2xy = 0$ (a : 1 ou 2) ; donner $k$ en un point selle (b : 0) ; ajouter $k_{xy}^2$ au lieu de le retrancher (c : 4), ou oublier son carré (c : $-2$) ; inverser l'ordre du gradient (e) ; donner $\frac{\partial k}{\partial x}$ en f).

### Ex M05b.22 — Prédire : la dérivée directionnelle le long d'une ligne de niveau

**Réponses** : a) `2` · b) `2` · c) `2` · d) `3`.

**Démarche.** a) $\nabla f(P) \cdot \mathbf{u} = \frac{6 - 6}{\sqrt{2}} = 0$ : la direction de la ligne de niveau est orthogonale au gradient, dans les deux sens. b) $f(P + t\,\mathbf{u}) = 12 + 0 \times t + 2t^2$ : la pente est nulle, mais la droite tangente sort de l'ellipse, vers des valeurs plus grandes ($f = 12{,}5$ en $t = 0{,}5$), car la surface est un bol. c) La plus grande pente, $\|\nabla f(P)\| = 6\sqrt{2} \approx 8{,}49$. d) Les deux vecteurs unitaires orthogonaux au gradient, $\pm\mathbf{u}$. Pour une fonction affine, b) deviendrait (1) : sa ligne de niveau est une droite, confondue avec sa tangente.

### Ex M05b.23 — L'erreur du plan tangent quand on s'éloigne du point

**Réponses** : a) `0.005171` · b) `4.14` · c) `2.01` · d) `0.0` · e) `0.010489`.

**Démarche.** `u = direction / np.linalg.norm(direction)`, `q = p + r * u`, les coefficients `a, b, c = mymath.multivar.tangent_plane(f, p)`, et `float(abs(f(q) - (a * q[0] + b * q[1] + c)))`. Pour la copie : c) une pente de 2 en échelle log-log, l'erreur est en $r^2$ (ordre 2) ; d) le long de $y = x$, $f = e^0 = 1$ et le plan vaut $1 + x - x = 1$ : la surface et le plan s'y confondent, même loin du point. e) Dans la direction $(1, -1)$, $s = x - y = r\sqrt{2}$, et $e^s - 1 - s \approx \frac{s^2}{2} = r^2 = 0{,}01$ ; dans la direction $(1, 0)$, $s = r$ et $\frac{s^2}{2} = 0{,}005$ : environ deux fois moins.

**Erreurs fréquentes.** Mesurer l'écart avec $f(\text{point})$ au lieu du plan tangent (a : 0,1052) ; ne pas normaliser la direction (e : 0,0214) ; oublier la valeur absolue.

### Ex M05b.24 — Lignes de niveau et flèches du gradient sur la même figure

**Démarche.** Une grille fine `X, Y = np.meshgrid(np.linspace(*xlim, 200), np.linspace(*ylim, 200))`, `contours = ax.contour(X, Y, f(X, Y), levels=10)` et `ax.clabel(contours)` ; une grille grossière de $13 \times 13$ points, `U, V = grad(XA, YA)` et `ax.quiver(XA, YA, U, V)` ; enfin `ax.set_aspect("equal")`. Pour la copie : sur $[-4, 4]^2$, $\sin x + \cos y$ a un maximum en $\big(\frac{\pi}{2}, 0\big)$ ($f = 2$), deux minima en $\big(-\frac{\pi}{2}, \pm\pi\big)$ ($f = -2$), et trois points selles, en $\big(-\frac{\pi}{2}, 0\big)$ et $\big(\frac{\pi}{2}, \pm\pi\big)$ ($f = 0$). Les flèches convergent vers le maximum, s'éloignent des minima et, près d'une selle, arrivent de deux côtés et repartent des deux autres. Elles coupent toutes les lignes à angle droit, et sont les plus longues là où les lignes se serrent : $\|\nabla f\|^2 = \cos^2 x + \sin^2 y$.

**Erreurs fréquentes.** Les flèches sur la grille fine (des milliers de flèches qui se recouvrent) ; oublier `ax.clabel` ou `set_aspect("equal")` (les angles sont déformés) ; appeler `plt.figure()` dans la fonction au lieu de dessiner dans `ax`.

### Ex M05b.25 — Chasse à l'erreur : la mauvaise variable dérivée, une direction non unitaire

**Réponses** : a) `"BDF"` · b) `[9, -11, 14.213, -3.4, -0.02, 0.1]`.

**Démarche.** (B) déplace $x$ au lieu de $y$ : elle calcule $\frac{\partial f}{\partial x} = 9$ ; il faut `(f(x, y + h) - f(x, y - h)) / (2 * h)`, qui vaut $x^3 - 4y = -11$. (D) oublie de diviser $(3, 4)$ par sa norme : $\frac{27 - 44}{5} = -3{,}4$, et non $-17$. (F) monte au lieu de descendre : $x - 0{,}1 \times 9 = 0{,}1$. (A), (C) et (E) sont justes : $\|\nabla f\| = \sqrt{81 + 121} = \sqrt{202} \approx 14{,}213$, et (E) est l'approximation linéaire du §5, $\nabla f \cdot (0{,}01 ;\ 0{,}01) = -0{,}02$ (la vraie variation vaut environ $-0{,}019$).

**Erreurs fréquentes.** Croire (E) fausse parce qu'elle n'est qu'approchée : son commentaire dit « à peu près » ; ne pas voir que (B) déplace la mauvaise coordonnée, parce que la formule a la bonne forme.

### Ex M05b.26 — Vectoriser : une fonction de deux variables sur une grille (`np.meshgrid`)

**Démarche.** `X, Y = np.meshgrid(xs, ys)`, puis `return np.asarray(f(X, Y), dtype=float)`. Pour la copie : sur une grille carrée, `Z` et sa transposée ont la même forme, et une inversion de $x$ et $y$ passerait inaperçue pour une fonction symétrique ; des tailles différentes la révèlent. Une fonction écrite avec `math.sin` refuse un tableau (`TypeError`) : il faut les fonctions de NumPy, qui s'appliquent élément par élément. Sur la grille de $600 \times 400$, la version vectorisée est en général des dizaines à des centaines de fois plus rapide que la double boucle.

**Erreurs fréquentes.** `np.meshgrid(ys, xs)` ou `indexing="ij"` (la forme `(len(xs), len(ys))`) ; une double boucle dans `grid_values` (juste, mais lente) ; renvoyer une liste.

### Ex M05b.27 — Défi : retrouver une fonction du second degré à partir de son gradient

**Réponse** : `[1.5, -2.0, 3.0, 0.5, -4.0]`.

**Démarche.** $\nabla f = (2ax + by + d,\ bx + 2cy + e)$. En $(0, 0)$ : $(d, e)$ ; en $(1, 0)$ : $(2a + d,\ b + e)$ ; en $(0, 1)$ : $(b + d,\ 2c + e)$. Trois appels donnent six nombres pour cinq inconnues (avec une vérification gratuite : $b$ apparaît deux fois) ; deux appels n'en donnent que quatre, c'est trop peu. Pour la copie : $f = 1{,}5x^2 - 2xy + 3y^2 + 0{,}5x - 4y + g$ ; son point critique résout $3x - 2y = -0{,}5$ et $-2x + 6y = 4$, soit $\big(\frac{5}{14}, \frac{11}{14}\big) \approx (0{,}357 ;\ 0{,}786)$. Avec $f_{xx} = 3$, $f_{yy} = 6$, $f_{xy} = -2$ : $D = 18 - 4 = 14 > 0$ et $f_{xx} > 0$, un minimum (global : la fonction est un bol).

**Erreurs fréquentes.** Lire $a$ directement comme le coefficient de $x$ dans $f_x$ (il vaut $2a$ : `[3.0, -2.0, 6.0, …]`) ; partir de points quelconques et résoudre un système (juste, mais plus fragile) ; appeler `grad` une fois par coefficient (5 appels).
