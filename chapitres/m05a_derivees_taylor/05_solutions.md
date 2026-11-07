# M05a · Dérivées, Taylor et calcul numérique — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, estimation et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M05a.Q1 — Le signe de la dérivée seconde
1. $f'$ est **croissante** : la pente augmente, la courbe tourne vers le haut, comme une cuvette (elle est convexe).
2. **Faux** : $e^{-x}$ est convexe et décroissante, $x^2$ est convexe et ni croissante ni décroissante sur $\mathbb{R}$. La convexité parle de la variation de la **pente**, pas de celle de $f$.
3. $(-\ln x)'' = \frac{1}{x^2} > 0$ : **convexe**.
4. **Faux** : il faut que $f''$ **change de signe** en 2. Contre-exemple : $(x - 2)^4$, dont la dérivée seconde $12(x - 2)^2$ s'annule en 2 sans changer de signe.
5. **Vrai** : $(f + g)'' = f'' + g'' \ge 0$ (et, sans dérivée, les deux inégalités de la corde s'additionnent).
6. $(x^3)'' = 6x \le 0$ sur $]-\infty, 0]$ : concave sur **$]-\infty, 0]$**.

### M05a.Q2 — Local ou global ?
1. $f$ est croissante sur $[0, 3]$ : son maximum global est au **bord droit**, en 3, où $f'$ n'a aucune raison de s'annuler.
2. $f'(x) = 2x + 2 > 0$ sur $[0, 5]$ : $f$ est croissante, son minimum global est en **0**, et vaut **0**. Le point $-1$ est hors de l'intervalle.
3. **Faux** : $x^2 e^{-x}$ a un maximum local en 2 qui n'est pas global sur $[-1, 4]$ (fiche §2).
4. $c$ est un **minimum global** de $f$ (fiche §2 : la tangente en $c$ est horizontale et la courbe est au-dessus).
5. **Non** : $e^x > 0$ pour tout $x$ et tend vers 0 en $-\infty$, mais ne l'atteint jamais ; il n'y a pas de minimum.
6. **On ne peut rien conclure** : $x^3$ (ni l'un ni l'autre), $x^4$ (minimum) et $-x^4$ (maximum) vérifient tous $f'(0) = f''(0) = 0$. Il faut étudier le signe de $f'$ autour de $c$.

### M05a.Q3 — Taylor : quel ordre, quelle précision ?
1. La **tangente** à la courbe en $a$ : $P_1(x) = f(a) + f'(a)(x - a)$.
2. $1 + x + \frac{x^2}{2}$.
3. $-\frac{1}{6}$ : $\sin x = x - \frac{x^3}{6} + \cdots$.
4. **Vrai** : c'est même ce qui le définit.
5. $\frac{M}{3!}|x|^3 = \frac{2}{6} \times 0{,}1^3 = \frac{1}{3000} \approx 3{,}3 \times 10^{-4}$.
6. **Faux** : la série de $\ln(1 + x)$ ne converge que pour $-1 < x \le 1$ ; pour $x = 2$, ses termes $\frac{2^k}{k}$ grandissent sans limite.

### M05a.Q4 — Newton converge-t-il ?
1. $x_1 = 4 - \frac{16 - 9}{8} = 4 - 0{,}875 = $ **3,125**.
2. Le pas n'est pas défini (division par 0) : la tangente est **horizontale** et ne coupe pas l'axe.
3. **Faux** : depuis un mauvais point, la suite peut cycler ou s'éloigner (fiche §4, M05a.24).
4. L'erreur est à peu près élevée au carré : environ $10^{-4}$, puis $10^{-8}$.
5. Elle **cycle** : $0 \to 1 \to 0 \to 1 \ldots$, sans jamais approcher la racine (vers $-1{,}77$).
6. La racine 1 est **double** : $f'(1) = 0$ aussi, et la convergence n'est plus que linéaire, l'erreur divisée par 2 à chaque pas ($x_{k+1} - 1 = \frac{x_k - 1}{2}$).

### M05a.Q5 — Différence avant ou centrée ?
1. Avant : **ordre 1** (erreur en $h$) ; centrée : **ordre 2** (erreur en $h^2$).
2. Par environ **100** ($10^2$).
3. Dans $f(x + h) - f(x - h)$, les termes de Taylor de degré pair en $h$ ($f(x)$ et $\frac{h^2}{2}f''(x)$) s'annulent ; l'erreur commence au terme en $h^2 f'''$ après division par $2h$. La différence avant garde le terme $\frac{h}{2}f''(x)$.
4. **Vrai** : $\frac{(x + h)^2 - (x - h)^2}{2h} = \frac{4xh}{2h} = 2x$, car $f''' = 0$.
5. $\frac{4D(h/2) - D(h)}{3}$, d'**ordre 4**.
6. **Vrai** : $f'' = 0$, donc le terme d'erreur est nul (la sécante d'une droite est la droite elle-même).

### M05a.Q6 — Les flottants : vrai ou faux
1. **Faux** : $\varepsilon = 2^{-52}$ est l'écart entre 1 et le flottant suivant ; le plus petit `float64` positif normal vaut environ $2{,}2 \times 10^{-308}$ (et les sous-normaux descendent jusqu'à environ $5 \times 10^{-324}$).
2. **Faux** : entre $2^{53}$ et $2^{54}$, les flottants sont espacés de 2 ; $2^{53} + 1$ est arrondi à $2^{53}$.
3. **Vrai** : $0{,}5 = 2^{-1}$.
4. **Faux** : `(1e16 + 1) + 1` donne `1e16` (chaque 1 est absorbé), alors que `1e16 + (1 + 1)` donne $10^{16} + 2$.
5. **Vrai** : $\varepsilon = 2^{-23} \approx 1{,}2 \times 10^{-7}$, soit environ 7 chiffres.
6. **Vrai** : $\frac{\varepsilon}{2} = 2^{-53} \approx 1{,}1 \times 10^{-16}$.

### M05a.Q7 — Overflow, underflow, log-sum-exp
1. `math.exp(720)` lève une `OverflowError` ; `np.exp(720)` renvoie `inf`, avec un avertissement (720 dépasse 709,78).
2. $\ln(2e^3) = 3 + \ln 2 \approx $ **3,693**.
3. Entre $\max_i v_i$ et $\max_i v_i + \ln n$.
4. Avec le maximum, tous les exposants $v_i - m$ sont négatifs ou nuls : aucune exponentielle ne déborde, et le plus grand terme vaut $e^0 = 1$, donc la somme est au moins 1 (pas de $\ln 0$). Avec le minimum, les exposants sont positifs, et les grands peuvent déborder.
5. La même : $\text{softmax}(\mathbf{v} + c) = \text{softmax}(\mathbf{v})$ ($e^c$ se simplifie).
6. $\ln \text{softmax}(\mathbf{v})_i = v_i - \text{LSE}(\mathbf{v})$.

<a id="rappels"></a>

## 🔁 Rappels

### M05a.R1 — Dérivées et variations (R7)
1. $f'(x) = \ln x + x \cdot \frac{1}{x} - 1 = \ln x$.
2. En $x = 1$.
3. $f$ décroît sur $]0, 1]$ ($\ln x < 0$) et croît sur $[1, +\infty[$ : minimum $f(1) = $ **$-1$**.
4. $f(e) = e - e = 0$ et $f'(e) = 1$ : $y = x - e$.
5. $g'(x) = 4(3x - 2)^3 \times 3 = 12(3x - 2)^3$.

### M05a.R2 — Suites définies par récurrence (R5)
1. $u_1 = 2 + 1{,}2 = 3{,}2$ ; $u_2 = 1{,}28 + 1{,}2 = 2{,}48$.
2. $0{,}6\,\ell = 1{,}2$ : $\ell = 2$.
3. $u_{n+1} - 2 = 0{,}4\,u_n + 1{,}2 - 2 = 0{,}4\,(u_n - 2)$ : la suite $u_n - 2$ est géométrique de raison 0,4, donc $u_n - 2 = 3 \times 0{,}4^n$.
4. $3 \times 0{,}4^6 \approx 0{,}0123$ et $3 \times 0{,}4^7 \approx 0{,}0049$ : **$n = 7$**.
5. Une convergence **linéaire** (ou géométrique) : chaque pas gagne le même nombre de décimales (ici $\log_{10} 2{,}5 \approx 0{,}4$). Newton près d'une racine simple est **quadratique** : le nombre de décimales justes double à chaque pas.

### M05a.R3 — Log-probabilités et log-sum-exp (M04)
1. $-600 \ln 10 \approx $ **$-1381{,}55$**.
2. **Non** : $10^{-600}$ est bien en dessous du plus petit `float64` positif (environ $5 \times 10^{-324}$) : le produit vaut 0.
3. $\frac{e^{-5}}{e^{-5} + e^{-6}} = \frac{1}{1 + e^{-1}} \approx $ **0,7311** et **0,2689**.
4. $-5 + \ln(1 + e^{-1}) \approx $ **$-4{,}6867$**.
5. Les log-vraisemblances étaient très négatives ($-1000$…) : leurs exponentielles valaient toutes 0 (underflow), et la normalisation donnait $\frac{0}{0}$. Soustraire le maximum ramène le plus grand terme à $e^0 = 1$ sans changer les probabilités normalisées : c'est le log-sum-exp de la fiche §8.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M05a.1 — Dérivées secondes et convexité

**Réponses** : a) `4` · b) `"[-1 ; 1]"` · c) `[-1, 1]` · d) `16.3097` · e) `False` · f) `0.5` · g) `-6` · h) `1.4762`.

**Démarche.**
- a) $f'(x) = e^{2x} + 2x e^{2x} = (1 + 2x)e^{2x}$, puis $f''(x) = 2e^{2x} + 2(1 + 2x)e^{2x} = (4 + 4x)e^{2x}$, et $f''(0) = 4$.
- b) et c) $g''(x) = 12x^2 - 12 = 12(x - 1)(x + 1)$ :

| $x$ | | $-1$ | | $1$ | |
|---|---|---|---|---|---|
| $g''(x)$ | $+$ | 0 | $-$ | 0 | $+$ |
| $g$ | convexe | | concave | | convexe |

  $g$ est concave sur $[-1, 1]$ (aux bornes, $g'' = 0$ ne gêne pas), et $g''$ change de signe en $-1$ et en 1 : ce sont les deux points d'inflexion.
- d) $w'(x) = 2x\,e^{x^2}$, puis, par la règle du produit, $w''(x) = 2e^{x^2} + 2x \cdot 2x\,e^{x^2} = (2 + 4x^2)e^{x^2}$, donc $w''(1) = 6e \approx 16{,}3097$ (et $w'' > 0$ partout : $w$ est convexe).
- e) $v(x) = \frac{1}{1 + x^2}$ : $v'(x) = -\frac{2x}{(1 + x^2)^2}$, puis $v''(x) = \frac{6x^2 - 2}{(1 + x^2)^3}$. En 0, $v''(0) = -2 < 0$ : $v$ est concave près de 0, donc pas convexe sur $\mathbb{R}$ (elle ne l'est que pour $|x| \ge \frac{1}{\sqrt{3}}$). Sa courbe est une bosse : une corde entre $-1$ et 1 passe sous le sommet.
- f) $h'(x) = \ln x + 1$, $h''(x) = \frac{1}{x}$ : $h''(2) = 0{,}5$.
- g) $(x^3 + kx^2 + 1)'' = 6x + 2k$ ; elle s'annule en 2 si $12 + 2k = 0$, soit $k = -6$, et elle change alors bien de signe (c'est une fonction affine).
- h) $\frac{1 + e^2}{2} - e = \frac{(e - 1)^2}{2} \approx 1{,}4762 > 0$ : le milieu de la corde est au-dessus de la courbe, comme pour toute fonction convexe.

Pour la copie : avec $\ln$ et les points 1 et 3, $\frac{\ln 1 + \ln 3}{2} - \ln 2 \approx 0{,}5493 - 0{,}6931 = -0{,}1438 < 0$ : pour une fonction concave, la corde est au-dessous.

**Erreurs fréquentes.** Oublier le facteur 2 de la dérivée de $e^{2x}$ (a) ; donner l'intervalle où $g'' > 0$ en b) ; prendre les points critiques de $g$ ($0$, $\pm\sqrt{3}$) pour ses points d'inflexion ; oublier un des deux termes de la dérivée du produit $2x\,e^{x^2}$ en d) ; répondre `True` en e) parce que $\frac{1}{1 + x^2}$ est positive ; écrire $h''(2) = \ln 2 + 1$ (c'est $h'(2)$) ; annuler $f'$ au lieu de $f''$ en g) ($k = -3$).

**Variante.** Sur quel intervalle $x^3 - 6x^2 + 2$ est-elle convexe ? *Réponse* : $f''(x) = 6x - 12 \ge 0 \iff x \ge 2$ : sur $[2, +\infty[$, avec un point d'inflexion en 2.

### Ex M05a.2 — Extrema locaux et globaux sur un intervalle fermé

**Réponses** : a) `[-1, 0, 2]` · b) `[0, 5, -27]` · c) `0` · d) `37` · e) `-2` · f) `-27` · g) `6.6875` · h) `False`.

**Démarche.** $f'(x) = 12x^3 - 12x^2 - 24x = 12x(x^2 - x - 2) = 12x(x + 1)(x - 2)$ et $f''(x) = 36x^2 - 24x - 24$ : $f''(-1) = 36 > 0$ (minimum local), $f''(0) = -24 < 0$ (maximum local), $f''(2) = 72 > 0$ (minimum local).

| $x$ | $-2$ | | $-1$ | | $0$ | | $2$ | | $3$ |
|---|---|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | 0 | $+$ | 0 | $-$ | 0 | $+$ | |
| $f$ | 37 | ↘ | 0 | ↗ | 5 | ↘ | $-27$ | ↗ | 32 |

- d) à f) Les candidats sont les trois points critiques et les deux bords : le plus grand est $f(-2) = 37$, le plus petit $f(2) = -27$.
- g) Sur $[-1{,}5 ;\ 1{,}5]$, les candidats sont $f(-1{,}5) = 6{,}6875$, $f(-1) = 0$, $f(0) = 5$ et $f(1{,}5) = -20{,}3125$ : le maximum est au bord gauche.
- h) $f(x) \approx 3x^4$ pour $|x|$ grand : $f$ n'est pas majorée sur $\mathbb{R}$.

Pour la copie : le maximum global de d) est atteint au **bord** $-2$, où $f'(-2) = -96 \ne 0$ : la règle « un extremum annule $f'$ » ne vaut qu'**à l'intérieur** de l'intervalle.

**Erreurs fréquentes.** Oublier la racine $x = 0$ en factorisant $f'$ ; oublier les bords et répondre 5 (le maximum local) en d) ; répondre 32 en d) en ne regardant que le bord droit ; en g), oublier que les bords ont changé.

**Variante.** Le minimum global de $f$ sur $[-1{,}5 ;\ 1{,}5]$ ? *Réponse* : $f(1{,}5) = -20{,}3125$, au bord droit (le point critique 2 est hors de l'intervalle).

### Ex M05a.3 — Points d'inflexion et test de la dérivée seconde

**Réponses** : a) `[0, 4]` · b) `320` · c) `0` · d) `"A"` · e) `[3]` · f) `-162` · g) `False`.

**Démarche.** $p'(x) = 5x^4 - 20x^3 = 5x^3(x - 4)$ et $p''(x) = 20x^3 - 60x^2 = 20x^2(x - 3)$.

| $x$ | | $0$ | | $3$ | | $4$ | |
|---|---|---|---|---|---|---|---|
| $p'(x)$ | $+$ | 0 | $-$ | | $-$ | 0 | $+$ |
| $p''(x)$ | $-$ | 0 | $-$ | 0 | $+$ | | $+$ |

- b) $p''(4) = 20 \times 16 \times 1 = 320 > 0$ : minimum local en 4 ($p(4) = -256$).
- c) et d) $p''(0) = 0$ : le test ne conclut pas. Mais $p'$ passe de $+$ à $-$ en 0 : $p$ croît puis décroît, c'est un **maximum local**.
- e) $p''$ a le signe de $x - 3$ (car $x^2 \ge 0$) : elle ne change de signe qu'en 3.
- f) $p(3) = 243 - 405 = -162$.
- g) $(x^4)'' = 12x^2 \ge 0$ : nul en 0, mais sans changement de signe ; $x^4$ est convexe sur $\mathbb{R}$.

Pour la copie : $p''(0) = 0$ parce que $p''$ a le facteur $x^2$, qui s'annule sans changer de signe : la courbe est concave juste avant **et** juste après 0.

**Erreurs fréquentes.** Conclure « ni maximum ni minimum » dès que $p''(0) = 0$ ; compter 0 comme point d'inflexion ; oublier le point critique 0 en factorisant.

**Variante.** $q(x) = x^4 - 4x^3$ : nature de ses points critiques et ses points d'inflexion ? *Réponse* : $q'(x) = 4x^2(x - 3)$ : en 0, ni maximum ni minimum ($q' \le 0$ des deux côtés), en 3 un minimum ; $q''(x) = 12x(x - 2)$ : inflexions en 0 et en 2. En 0, c'est un point d'inflexion à tangente horizontale.

### Ex M05a.4 — Polynômes de Taylor de trois fonctions usuelles

**Réponses** : a) `"1 - x**2/2"` · b) `"x - x**2/2 + x**3/3"` · c) `"1 + x + x**2 + x**3"` · d) `3.0037` · e) `0.09533` · f) `"1/24"` · g) `0.955` · h) `1`.

**Démarche.**
- a) $\cos 0 = 1$, $\cos'(0) = -\sin 0 = 0$, $\cos''(0) = -\cos 0 = -1$ : $1 - \frac{x^2}{2}$.
- b) $f = \ln(1 + x)$ : $f' = \frac{1}{1 + x}$, $f'' = -\frac{1}{(1 + x)^2}$, $f''' = \frac{2}{(1 + x)^3}$, soit $0, 1, -1, 2$ en 0 : $x - \frac{x^2}{2} + \frac{2}{6}x^3$.
- c) La dérivée $k$-ième de $(1 - x)^{-1}$ est $k!\,(1 - x)^{-k-1}$, qui vaut $k!$ en 0 : tous les coefficients valent 1.
- d) En $a = 1$, toutes les dérivées de $e^x$ valent $e$ : $e\,(1 + 0{,}1 + \frac{0{,}01}{2}) = 1{,}105\,e \approx 3{,}0037$, contre $e^{1{,}1} \approx 3{,}0042$.
- e) $0{,}1 - 0{,}005 + 0{,}000333 \approx 0{,}09533$, contre $\ln 1{,}1 \approx 0{,}09531$.
- f) $\cos^{(4)} = \cos$, qui vaut 1 en 0 : $\frac{1}{4!} = \frac{1}{24}$.
- g) $\sin\frac{\pi}{2} = 1$, $\cos\frac{\pi}{2} = 0$, $-\sin\frac{\pi}{2} = -1$ : $1 - \frac{0{,}3^2}{2} = 0{,}955$, contre $\sin(\frac{\pi}{2} + 0{,}3) = \cos 0{,}3 \approx 0{,}9553$.
- h) $q(1) = 0$, $q'(1) = 3 - 4 = -1$, $q''(1) = 6 - 4 = 2$, $q''' = 6$ : $P_3(x) = -(x - 1) + (x - 1)^2 + (x - 1)^3$.

Pour la copie : en développant h), $-x + 1 + x^2 - 2x + 1 + x^3 - 3x^2 + 3x - 1 = x^3 - 2x^2 + 1$ : on retrouve $q$. Un polynôme de degré 3 est égal à son polynôme de Taylor d'ordre 3, en n'importe quel point : ses dérivées d'ordre 4 et plus sont nulles, donc le reste aussi. Les erreurs de d), e) et g) sont de l'ordre de $5 \times 10^{-4}$, $2 \times 10^{-5}$ et $3 \times 10^{-4}$, comme le prévoit le premier terme négligé.

**Erreurs fréquentes.** Oublier les factorielles ($1 - x^2$) ; oublier l'alternance des signes de $\ln(1 + x)$ ; en d), évaluer le polynôme **en 0** ; en g), écrire un terme d'ordre 1 alors que $\cos\frac{\pi}{2} = 0$.

**Variante.** Le polynôme de Taylor d'ordre 2 de $\sqrt{x}$ en 4, évalué en 4,2 ? *Réponse* : $2 + \frac{0{,}2}{4} - \frac{1}{32} \cdot \frac{0{,}04}{2} = 2{,}049375$, contre $\sqrt{4{,}2} \approx 2{,}049390$.

### Ex M05a.5 — Le reste de Taylor : borner l'erreur d'une approximation

**Réponses** : a) `0.479167` · b) `0.0002589` · c) `0.0002604` · d) `9` · e) `0.000333` · f) `0.0000667` · g) `0.1817`.

**Démarche.**
- a) $0{,}5 - \frac{0{,}125}{6} \approx 0{,}479167$ ; b) $\sin 0{,}5 \approx 0{,}4794255$, d'où une erreur d'environ $0{,}0002589$.
- c) Le coefficient de $x^4$ est nul ($\sin^{(4)}(0) = \sin 0 = 0$), donc $P_3 = P_4$ et l'on peut utiliser le reste d'ordre 4 : $\frac{0{,}5^5}{5!} \approx 0{,}0002604$, à peine au-dessus de l'erreur vraie. Le reste d'ordre 3 donnerait $\frac{0{,}5^4}{4!} \approx 0{,}0026$, dix fois trop large.
- d) Il faut $(n + 1)! > 3 \times 10^6$ : $9! = 362\,880$ ne suffit pas, $10! = 3\,628\,800$ suffit, donc $n + 1 = 10$, **$n = 9$**.
- e) $\frac{2}{3!} \times 0{,}1^3 \approx 0{,}000333$ (l'erreur vraie : $|\ln 1{,}1 - 0{,}095| \approx 0{,}000310$).
- f) $P_2 = P_3$ pour $\cos$, et $|\cos^{(4)}| \le 1$ : $\frac{0{,}2^4}{4!} \approx 0{,}0000667$ (le reste d'ordre 2 donnerait $\frac{0{,}2^3}{3!} \approx 0{,}0013$, vingt fois plus large).
- g) $\frac{x^3}{6} \le 0{,}001 \iff x^3 \le 0{,}006 \iff x \le 0{,}006^{1/3} \approx 0{,}1817$ : au-delà, la borne dépasse 0,001.

Pour la copie : en b) et c), la borne est très proche de l'erreur vraie (0,0002604 contre 0,0002589), parce que $|\sin^{(5)}| = |\cos|$ reste proche de 1 entre 0 et 0,5. Ce n'est pas toujours le cas : une borne est une garantie, pas une estimation.

**Erreurs fréquentes.** Utiliser $\frac{|x|^{n}}{n!}$ au lieu de $\frac{|x|^{n+1}}{(n + 1)!}$ ; répondre 10 en d) (confondre $n$ et $n + 1$) ; prendre une racine carrée en g).

**Variante.** Une borne de l'erreur de $1 + x + \frac{x^2}{2} + \frac{x^3}{6}$ pour $e^{0{,}5}$, avec $e^{\xi} < 2$ ? *Réponse* : $\frac{2 \times 0{,}5^4}{24} \approx 0{,}0052$ ; l'erreur vraie vaut environ 0,0029.

### Ex M05a.6 — Newton à la main : une racine carrée en trois pas

**Réponses** : a) `"19/6"` · b) `"721/228"` · c) `3.1622776602` · d) `3.04` · e) `0.158` · f) `-3.1623` · g) `False` · h) `2.6137`.

**Démarche.** Avec $f(x) = x^2 - 10$ et $f'(x) = 2x$ : $x_{k+1} = x_k - \frac{x_k^2 - 10}{2x_k} = \frac{x_k^2 + 10}{2x_k} = \frac{1}{2}\big(x_k + \frac{10}{x_k}\big)$ (la méthode de Héron, fiche §4).
- a) $\frac{1}{2}(3 + \frac{10}{3}) = \frac{19}{6}$ ; b) $\frac{1}{2}(\frac{19}{6} + \frac{60}{19}) = \frac{361 + 360}{228} = \frac{721}{228}$ ; c) $x_3 \approx 3{,}1622776602$ (avec $\sqrt{10} \approx 3{,}16227766017$, l'erreur est d'environ $1{,}5 \times 10^{-12}$).
- d) $\frac{721}{228} \approx 3{,}1622807018$, soit $3{,}04 \times 10^{-6}$ au-dessus de $\sqrt{10}$.
- e) $x_1 - \sqrt{10} \approx 0{,}004389$ : $\frac{3{,}04 \times 10^{-6}}{0{,}004389^2} \approx 0{,}158$.
- f) Depuis un point négatif, la suite reste négative et converge vers $-\sqrt{10}$.
- g) $f'(0) = 0$ : la tangente en 0 est horizontale.
- h) $g'(x) = \frac{1}{x}$ : $x_1 = 2 - \frac{\ln 2 - 1}{1/2} = 4 - 2\ln 2 \approx 2{,}6137$ ; la suite cherche la racine $e \approx 2{,}7183$.

Pour la copie : $x_{k+1} - \sqrt{10} = \frac{x_k^2 + 10 - 2\sqrt{10}\,x_k}{2x_k} = \frac{(x_k - \sqrt{10})^2}{2x_k}$ exactement. Le rapport e) vaut donc $\frac{1}{2x_1} = \frac{3}{19} \approx 0{,}158$, très proche de la constante $\frac{f''}{2f'} = \frac{1}{2\sqrt{10}} \approx 0{,}158$ de la fiche (§4). L'erreur passe de 0,16 à 0,0044, puis $3 \times 10^{-6}$, puis $1{,}5 \times 10^{-12}$ : les décimales justes doublent.

**Erreurs fréquentes.** Un signe dans le pas ($x_1 = \frac{17}{6}$) ; repartir de $x_0$ pour calculer $x_2$ ; en h), diviser par $g'(2) = \frac{1}{2}$ comme si l'on multipliait.

**Variante.** Deux pas de Newton pour $\sqrt{5}$ depuis 2 ? *Réponse* : $x_1 = \frac{9}{4}$, $x_2 = \frac{161}{72} \approx 2{,}236111$, contre $\sqrt{5} \approx 2{,}236068$.

### Ex M05a.7 — L'erreur d'une différence avant et d'une différence centrée, par Taylor

**Réponses** : a) `"1/4"` · b) `0.24695` · c) `-0.00305` · d) `-0.003125` · e) `0.250078` · f) `"1/12800"` · g) `4` · h) `-0.03127`.

**Démarche.** $f'(x) = \frac{1}{2\sqrt{x}}$, $f''(x) = -\frac{1}{4x^{3/2}}$, $f'''(x) = \frac{3}{8x^{5/2}}$ ; en 4 : $\frac{1}{4}$, $-\frac{1}{32}$ et $\frac{3}{256}$.
- b) et c) $\sqrt{4{,}2} \approx 2{,}0493902$ : $\frac{0{,}0493902}{0{,}2} \approx 0{,}24695$, soit une erreur de $-0{,}00305$.
- d) $\frac{0{,}2}{2} \times (-\frac{1}{32}) = -0{,}003125$ : la prévision est bonne à 2 % près.
- e) $\sqrt{3{,}8} \approx 1{,}9493589$ : $\frac{2{,}0493902 - 1{,}9493589}{0{,}4} \approx 0{,}250078$, une erreur de $7{,}82 \times 10^{-5}$.
- f) $\frac{0{,}04}{6} \times \frac{3}{256} = \frac{1}{12\,800} \approx 7{,}81 \times 10^{-5}$ : la prévision colle à l'erreur vraie.
- g) L'erreur est proportionnelle à $h^2$ : diviser $h$ par 2 la divise par 4.
- h) $\frac{2{,}0493902 - 4 + 1{,}9493589}{0{,}04} \approx -0{,}03127$ : elle approche $f''(4) = -0{,}03125$ à l'ordre 2 (M05a.11, question 5).

**Erreurs fréquentes.** Oublier de diviser par $h$ ; donner l'erreur avec le mauvais signe ; en e), diviser par $h$ au lieu de $2h$ ; confondre la différence seconde h) avec $f''(4)$ lui-même.

**Variante.** La différence avant de $\cos$ en 0,5 avec $h = 0{,}1$, son erreur et la prévision de Taylor ? *Réponse* : $\frac{\cos 0{,}6 - \cos 0{,}5}{0{,}1} \approx -0{,}52247$, contre $-\sin 0{,}5 \approx -0{,}47943$ : erreur $-0{,}0430$ ; prévision $\frac{0{,}1}{2} \times (-\cos 0{,}5) \approx -0{,}0439$.

### Ex M05a.8 — Les flottants : 0,1 en binaire, epsilon machine, nombres représentables

**Réponses** : a) `"101"` · b) `"C"` · c) `"1001"` · d) `-54` · e) `-42` · f) `16777217` · g) `"1/2"` · h) `-24`.

**Démarche.**
- a) $0{,}625 \times 2 = 1{,}25$ (chiffre 1), $0{,}25 \times 2 = 0{,}5$ (chiffre 0), $0{,}5 \times 2 = 1$ (chiffre 1, fin) : $0{,}101$, soit les trois chiffres `"101"` ; en effet $\frac{1}{2} + \frac{1}{8} = 0{,}625$.
- b) $0{,}2 = \frac{1}{5}$, $0{,}3 = \frac{3}{10}$, $0{,}6 = \frac{3}{5}$ ont le facteur 5 au dénominateur ; $0{,}4375 = \frac{7}{16}$ a pour dénominateur $2^4$ : $(0{,}0111)_2$. Seules les fractions dont le dénominateur (irréductible) est une puissance de 2 ont un développement binaire fini.
- c) $0{,}3 \to 0{,}6$ (chiffre 0) $\to 1{,}2$ (1, on garde 0,2) $\to 0{,}4$ (0) $\to 0{,}8$ (0) $\to 1{,}6$ (1, on garde 0,6) $\to 1{,}2$ (1) $\to \ldots$ : les chiffres $0, 1, 0, 0, 1, 1, 0, 0, 1, \ldots$, soit $0{,}0\,1001\,1001\ldots$
- d) $0{,}25 = 2^{-2} \le 0{,}3 < 2^{-1}$ : l'écart vaut $2^{-2} \times 2^{-52} = 2^{-54}$.
- e) $1024 = 2^{10}$ : entre $2^{10}$ et $2^{11}$, l'écart vaut $2^{10} \times 2^{-52} = 2^{-42}$.
- f) `float32` garde 23 bits après la virgule, donc 24 bits significatifs : tous les entiers jusqu'à $2^{24}$ sont exacts ; le suivant, $2^{24} + 1 = 16\,777\,217$, demanderait 25 bits.
- g) $512 = 2^9 \le 1000 < 2^{10}$, et $\varepsilon = 2^{-10}$ en `float16` : l'écart vaut $2^9 \times 2^{-10} = \frac{1}{2}$. En `float16`, 1 000,25 n'existe pas.
- h) $\frac{2^{-23}}{2} = 2^{-24}$.

Pour la copie : entre $2^e$ et $2^{e+1}$, les flottants sont $(1 + \frac{m}{2^{52}}) \times 2^e$ pour $m = 0, \ldots, 2^{52} - 1$ : autant de nombres dans chaque intervalle, qui est deux fois plus long que le précédent ; l'écart double donc (figure du §6). Dans $[1, 2[$, il y a $2^{52} \approx 4{,}5 \times 10^{15}$ `float64`.

**Erreurs fréquentes.** Croire que l'écart est toujours $\varepsilon$ (d, e, g) ; prendre la puissance de 2 juste **au-dessus** du nombre ; confondre $\varepsilon$ et $\frac{\varepsilon}{2}$ (h) ; en f), répondre $2^{24}$, qui est représentable, ou la valeur de `float64`.

**Variante.** 0,8125 en binaire ? *Réponse* : $0{,}8125 = \frac{1}{2} + \frac{1}{4} + \frac{1}{16}$, soit $0{,}1101$.

### Ex M05a.9 — Le meilleur pas par le calcul : minimiser une borne d'erreur

**Réponses** : a) `1.414` · b) `2.828` · c) `0.01` · d) `1.5` · e) `0.1` · f) `0.01` · g) `0.0447` · h) `True`.

**Démarche.**
- a) $E'_{\text{avant}}(h) = \frac{M_2}{2} - \frac{2\delta}{h^2} = 0 \iff h^2 = \frac{4\delta}{M_2}$, donc $h^* = 2\sqrt{\frac{\delta}{M_2}} = 2\sqrt{5 \times 10^{-7}} \approx 1{,}414 \times 10^{-3}$. $E'$ est négative avant $h^*$ et positive après : c'est un minimum.
- b) Au meilleur pas, les deux termes sont égaux : $E = 2 \times \frac{M_2}{2}h^* = 2\sqrt{M_2\delta} = 2\sqrt{2 \times 10^{-6}} \approx 2{,}828 \times 10^{-3}$.
- c) $E'_{\text{centrée}}(h) = \frac{M_3}{3}h - \frac{\delta}{h^2} = 0 \iff h^3 = \frac{3\delta}{M_3} = 10^{-6}$, donc $h^* = 0{,}01$.
- d) $E = \frac{3}{6} \times 10^{-4} + \frac{10^{-6}}{10^{-2}} = 0{,}5 \times 10^{-4} + 10^{-4} = 1{,}5 \times 10^{-4}$.
- e) $h^* = \big(\frac{3\delta}{M_3}\big)^{1/3}$ est proportionnel à $\delta^{1/3}$ : $(10^{-3})^{1/3} = 0{,}1$.
- f) En remplaçant : $E(h^*) = \frac{M_3}{6}h^{*2} + \frac{\delta}{h^*} = \frac{3}{2}\big(\frac{M_3}{3}\big)^{1/3}\delta^{2/3}$, proportionnel à $\delta^{2/3}$ : $(10^{-3})^{2/3} = 0{,}01$.
- g) $E'(h) = 2h - \frac{8\delta}{h^3} = 0 \iff h^4 = 4\delta = 4 \times 10^{-6}$, donc $h^* \approx 0{,}0447$.
- h) $1{,}5 \times 10^{-4}$ contre $2{,}8 \times 10^{-3}$ : environ 19 fois plus précise.

**Erreurs fréquentes.** Oublier le facteur 2 du bruit de la différence avant ; ne garder qu'un terme de la borne en b) ou d) ; croire que l'erreur au meilleur pas est proportionnelle à $\delta$ (f) ; prendre une racine carrée au lieu d'une racine quatrième en g).

**Variante.** La différence avant avec $\delta = 10^{-8}$ et $M_2 = 2$ : meilleur pas et erreur ? *Réponse* : $h^* = 2\sqrt{5 \times 10^{-9}} \approx 1{,}41 \times 10^{-4}$, $E = 2\sqrt{2 \times 10^{-8}} \approx 2{,}83 \times 10^{-4}$ : un capteur 100 fois plus précis ne divise l'erreur que par 10 ($\sqrt{\delta}$).

### Ex M05a.10 — log-sum-exp à la main : la softmax stable de trois scores

**Réponses** : a) `True` · b) `802` · c) `802.1277` · d) `[0.8801, 0.1191, 0.0008]` · e) `-2.1277` · f) `7.1277` · g) `803.0986`.

**Démarche.**
- a) 802 dépasse $\ln(1{,}8 \times 10^{308}) \approx 709{,}78$ : `math.exp(802)` lève une `OverflowError`.
- c) Moins le maximum : $(0, -2, -7)$ ; exponentielles $1$, $e^{-2} \approx 0{,}135335$, $e^{-7} \approx 0{,}000912$ ; somme $1{,}136247$ ; logarithme $0{,}127731$ ; plus le maximum : $802{,}1277$.
- d) Chaque exponentielle divisée par la somme : $0{,}8801$, $0{,}1191$, $0{,}0008$.
- e) $800 - 802{,}1277 = -2{,}1277$ ; f) $-(795 - 802{,}1277) = 7{,}1277$.
- g) $\ln(3e^{802}) = 802 + \ln 3 \approx 803{,}0986$.

Pour la copie : $802 \le 802{,}1277 \le 802 + \ln 3 \approx 803{,}0986$ ; g) touche la borne de droite, parce que les trois scores sont égaux (M05a.13).

**Erreurs fréquentes.** Oublier de rajouter $m$ (c = 0,1277) ; oublier de normaliser en d) ; un signe en e) ou f).

**Variante.** $\mathbf{v} = (5, 5, 1)$ : LSE et softmax ? *Réponse* : $5 + \ln(2 + e^{-4}) \approx 5{,}7023$ ; softmax $(0{,}4955 ;\ 0{,}4955 ;\ 0{,}0091)$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M05a.11 — La différence centrée est d'ordre 2 : le calcul par Taylor (cas général)

**Réponse modèle.**
1. Par la formule de Taylor-Lagrange à l'ordre 2 : $f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(\xi_+)$ avec $\xi_+ \in\ ]x, x + h[$, et $f(x - h) = f(x) - hf'(x) + \frac{h^2}{2}f''(x) - \frac{h^3}{6}f'''(\xi_-)$ avec $\xi_- \in\ ]x - h, x[$.
2. En soustrayant, $f(x)$ et $\frac{h^2}{2}f''(x)$ disparaissent : $f(x + h) - f(x - h) = 2hf'(x) + \frac{h^3}{6}\big(f'''(\xi_+) + f'''(\xi_-)\big)$. On divise par $2h$ : $D_0(h) - f'(x) = \frac{h^2}{12}\big(f'''(\xi_+) + f'''(\xi_-)\big)$.
3. $\xi_+$ et $\xi_-$ sont dans $[x - h, x + h]$, où $|f'''| \le M_3$ : $|D_0(h) - f'(x)| \le \frac{h^2}{12} \times 2M_3 = \frac{M_3}{6}h^2$.
4. $f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(\xi)$ avec $\xi \in\ ]x, x + h[$, donc $D_+(h) - f'(x) = \frac{h}{2}f''(\xi)$, et $|D_+(h) - f'(x)| \le \frac{M_2}{2}h$.
5. À l'ordre 3 : $f(x \pm h) = f(x) \pm hf'(x) + \frac{h^2}{2}f''(x) \pm \frac{h^3}{6}f'''(x) + \frac{h^4}{24}f^{(4)}(\eta_\pm)$. En **additionnant**, les termes impairs disparaissent : $f(x + h) - 2f(x) + f(x - h) = h^2 f''(x) + \frac{h^4}{24}\big(f^{(4)}(\eta_+) + f^{(4)}(\eta_-)\big)$. On divise par $h^2$ : l'erreur vaut $\frac{h^2}{24}(\ldots)$, majorée par $\frac{h^2}{24} \times 2M_4 = \frac{M_4}{12}h^2$.
6. $\frac{D_0(h) - f'(x)}{h^2} = \frac{f'''(\xi_+) + f'''(\xi_-)}{12}$. Quand $h \to 0$, $\xi_\pm \to x$ (ils sont coincés entre $x - h$ et $x + h$), et $f'''$ est continue : la limite vaut $\frac{2f'''(x)}{12} = \frac{f'''(x)}{6}$. Donc, pour $h$ petit, l'erreur vaut à peu près $\frac{f'''(x)}{6}h^2$ ; avec $\frac{h}{2}$, à peu près $\frac{f'''(x)}{6} \cdot \frac{h^2}{4}$ : le rapport tend vers 4 (si $f'''(x) \ne 0$ ; sinon, il faut un terme de plus).
7. $D_0(\frac{h}{2}) = f'(x) + \frac{c_2}{4}h^2 + \frac{c_4}{16}h^4 + O(h^6)$, donc $4D_0(\frac{h}{2}) - D_0(h) = 3f'(x) + (c_2 - c_2)h^2 + (\frac{c_4}{4} - c_4)h^4 + O(h^6) = 3f'(x) - \frac{3c_4}{4}h^4 + O(h^6)$. En divisant par 3 : $f'(x) - \frac{c_4}{4}h^4 + O(h^6)$, une erreur d'ordre 4.

**Grille.** (1) les deux développements, avec le reste de Lagrange et la place de $\xi_\pm$ ; (2) la soustraction, qui élimine les termes pairs ; (3) la majoration par $M_3$ ; (4) l'ordre 1 de la différence avant ; (5) l'addition, qui élimine les termes impairs, et la majoration par $M_4$ ; (6) la limite par continuité de $f'''$, et le rapport 4 ; (7) la combinaison qui annule $c_2$.

### Ex M05a.12 — Newton double les décimales justes : l'erreur au carré (racine simple)

**Réponse modèle.**
1. $f(r) = f(x_k) + f'(x_k)(r - x_k) + \frac{f''(\xi_k)}{2}(r - x_k)^2$, avec $\xi_k$ entre $x_k$ et $r$.
2. $f(r) = 0$ ; on divise par $f'(x_k) \ne 0$ : $\frac{f(x_k)}{f'(x_k)} + r - x_k = -\frac{f''(\xi_k)}{2f'(x_k)}e_k^2$. Or $\frac{f(x_k)}{f'(x_k)} = x_k - x_{k+1}$ (définition de Newton), donc le membre de gauche vaut $r - x_{k+1} = -e_{k+1}$, d'où $e_{k+1} = \frac{f''(\xi_k)}{2f'(x_k)}e_k^2$.
3. $\xi_k$ et $x_k$ sont dans $I$ : $|f''(\xi_k)| \le M$ et $|f'(x_k)| \ge m$, donc $|e_{k+1}| \le \frac{M}{2m}e_k^2 = C\,e_k^2$.
4. Avec $d_k = C|e_k|$ : $d_{k+1} \le C \cdot C e_k^2 = d_k^2$. Par récurrence, si $d_k \le d_0^{2^k}$, alors $d_{k+1} \le d_k^2 \le d_0^{2^{k+1}}$ (et c'est vrai pour $k = 0$). Avec $d_0 = 0{,}1$ : $d_k \le 10^{-2^k}$, et $10^{-2^k} \le 10^{-16} \iff 2^k \ge 16 \iff k \ge 4$ : **quatre pas**.
5. $x_{k+1} = x_k - \frac{x_k^2 - c}{2x_k} = \frac{x_k^2 + c}{2x_k}$, donc $e_{k+1} = \frac{x_k^2 + c - 2\sqrt{c}\,x_k}{2x_k} = \frac{(x_k - \sqrt{c})^2}{2x_k}$. Si $x_k > 0$, alors $e_{k+1} \ge 0$, c'est-à-dire $x_{k+1} \ge \sqrt{c} > 0$. Depuis $x_0 > 0$, on obtient $x_1 \ge \sqrt{c}$, puis, par récurrence, $x_k \ge \sqrt{c}$ pour tout $k \ge 1$ : la suite reste au-dessus de $\sqrt{c}$ (et elle décroît vers lui).
6. $f'(x) = 2(x - r)$, donc $x_{k+1} = x_k - \frac{(x_k - r)^2}{2(x_k - r)} = x_k - \frac{x_k - r}{2}$ et $e_{k+1} = \frac{e_k}{2}$ : une convergence **linéaire**, de rapport $\frac{1}{2}$. Gagner une décimale, c'est diviser l'erreur par 10 : $\log_2 10 \approx 3{,}3$ pas par décimale.
7. $g'(x) = 2ax + b$ et $g''(x) = 2a$ : $x_1 = x_0 - \frac{2ax_0 + b}{2a} = -\frac{b}{2a}$, le sommet de la parabole, qui est son minimum puisque $a > 0$. La tangente à $g'$ (une droite) est $g'$ elle-même.

**Grille.** (1) le développement en $x_k$ évalué en $r$, avec $\xi_k$ ; (2) l'utilisation de $f(r) = 0$ et de la définition de $x_{k+1}$ ; (3) la majoration avec $M$ et $m$ ; (4) la récurrence sur $d_k$ et le calcul $k = 4$ ; (5) l'identité exacte pour $x^2 - c$ et la conséquence $x_k \ge \sqrt{c}$ ; (6) le rapport $\frac{1}{2}$ et le nom « linéaire » ; (7) un pas suffit pour une quadratique.

### Ex M05a.13 — Encadrer le log-sum-exp : max ≤ LSE ≤ max + ln n

**Réponse modèle.**
1. Un des termes vaut $e^m$ et les autres sont positifs : $e^m \le \sum_i e^{v_i}$. Chaque terme est au plus $e^m$ ($\exp$ est croissante) : $\sum_i e^{v_i} \le n\,e^m$. Le logarithme, croissant, donne $m \le \text{LSE}(\mathbf{v}) \le m + \ln n$.
2. À droite, l'égalité demande que chaque $e^{v_i}$ vaille $e^m$ : **tous les $v_i$ égaux**. À gauche, il faudrait que les $n - 1$ autres termes soient nuls, impossible puisque $e^{v} > 0$ : jamais pour $n \ge 2$ (avec des valeurs finies).
3. $\text{LSE}(\mathbf{v} + c) = \ln\sum_i e^{v_i}e^c = \ln\big(e^c\sum_i e^{v_i}\big) = c + \text{LSE}(\mathbf{v})$. Et $\frac{e^{v_i + c}}{\sum_j e^{v_j + c}} = \frac{e^c e^{v_i}}{e^c \sum_j e^{v_j}} = \text{softmax}(\mathbf{v})_i$.
4. $v_i \le w_i$ donne $e^{v_i} \le e^{w_i}$, puis en sommant $\sum_i e^{v_i} \le \sum_i e^{w_i}$, puis $\ln$ croissante.
5. Si $t \ge 0$ : $\ln(e^t + 1) - t = \ln(1 + e^{-t})$. Si $t < 0$ : $\ln(e^t + 1) - 0 = \ln(1 + e^{t})$. Dans les deux cas, $\ln(1 + e^{-|t|})$. Comme $e^{-|t|} \in\ ]0, 1]$, l'écart est au plus $\ln 2$ (atteint en $t = 0$), et il tend vers $\ln 1 = 0$ quand $|t| \to +\infty$.
6. $\text{LSE}(\mathbf{v}) - m = \ln\big(1 + \sum_{i \ne i^*} e^{v_i - m}\big)$, où $i^*$ est l'indice du maximum. Chacun des $n - 1$ autres scores vérifie $v_i \le m - g$, donc $e^{v_i - m} \le e^{-g}$, et $\ln(1 + u) \le u$ donne $\text{LSE}(\mathbf{v}) - m \le (n - 1)e^{-g}$. Pour $(10, 3, 2)$ : $g = 7$, borne $2e^{-7} \approx 0{,}00182$, écart vrai $\ln(1 + e^{-7} + e^{-8}) \approx 0{,}00125$.

**Grille.** (1) les deux inégalités sur la somme, puis le logarithme croissant ; (2) les cas d'égalité ; (3) la factorisation par $e^c$, et la simplification dans la softmax ; (4) la monotonie, en trois temps ; (5) les deux cas selon le signe de $t$, et les deux conséquences ; (6) l'écriture avec $1 + \ldots$, la majoration de chaque terme et $\ln(1 + u) \le u$, puis l'application numérique.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, estimation et explication

### Ex M05a.14 — Pourquoi les bibliothèques de ML calculent log(softmax) d'un seul coup

**Réponses** : a) `780.0` · b) `-760.0` · c) `True` · d) `760.0` · e) `False` · f) `-3.1698`.

**Démarche.**
- a) $780 + \ln(1 + e^{-760} + e^{-810})$ : les deux exponentielles sont si petites que la somme vaut 1 à la précision des flottants, d'où $780{,}00$.
- b) $20 - 780 = -760$, sans aucune exponentielle.
- c) $e^{-760}$ est plus petit que le plus petit `float64` positif (environ $5 \times 10^{-324} \approx e^{-744{,}4}$) : il vaut exactement 0.
- d) $-(-760) = 760$.
- e) `-np.log(0.0)` donne `inf` (avec un avertissement) : une loss infinie, puis des gradients `nan`. Et `-math.log(0.0)` ne renvoie même pas de nombre : il lève une `ValueError` (*math domain error*).
- f) $\text{LSE}(2, 0, -1) = 2 + \ln(1 + e^{-2} + e^{-3}) \approx 2{,}1698$, donc $-1 - 2{,}1698 = -3{,}1698$.

Pour la copie : la loss est énorme parce que le modèle est sûr de lui et se trompe : il donne à la bonne classe une probabilité de $e^{-760}$. C'est justement l'exemple dont il doit le plus apprendre ; une loss finie (760) garde ce signal, alors qu'une loss infinie ou `nan` casse l'entraînement. Les bibliothèques prennent donc les **scores** en entrée et calculent $z_y - \text{LSE}(\mathbf{z})$ d'un seul coup (le log-softmax), sans jamais former la probabilité qui s'efface.

**Erreurs fréquentes.** Répondre $780 + \ln 3$ en a) (les autres termes ne valent pas 1) ; un signe en b) ou d) ; croire que la probabilité de c) est « très petite mais non nulle ».

**Variante.** Avec $\mathbf{z} = (30, 20, -30)$ et la bonne classe 2 : la loss ? *Réponse* : $\text{LSE} = 30 + \ln(1 + e^{-10} + e^{-60}) \approx 30{,}0000454$, loss $\approx 10{,}0000454$ ; ici, la probabilité $e^{-10{,}00005} \approx 4{,}5 \times 10^{-5}$ est représentable, et les deux calculs s'accordent.

### Ex M05a.15 — MML §5.1 : dérivée d'une fonction d'une variable et série de Taylor (lecture guidée)

**Réponse modèle.**
1. Le quotient différentiel est la pente de la **sécante** entre les points d'abscisses $x$ et $x + \delta x$ ; la dérivée est sa limite quand l'écart tend vers 0, et la sécante devient la **tangente**.
2. $T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$ ; la série de Taylor est la somme infinie, que le livre définit pour une fonction **infiniment dérivable** (« lisse », $f \in \mathcal{C}^\infty$) ; en $x_0 = 0$, on parle de série de Maclaurin.
3. $f(2) = 8$, $f'(2) = 12$, $f''(2) = 12$, $f'''(2) = 6$, $f^{(4)} = 0$ : $T_1 = 8 + 12(x - 2)$, $T_2 = T_1 + 6(x - 2)^2$, $T_3 = T_2 + (x - 2)^3$, qui se développe en $x^3$ ; $T_4 = T_3$. À partir du degré 3, le polynôme de Taylor **est** $f$ : ses dérivées d'ordre 4 et plus sont nulles (Ex M05a.4 h).
4. Les dérivées en 0 valent $1, -1, -1, 1, 1$ : $1 - x - \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24}$.
5. $\big(\frac{x}{1 + x^2}\big)' = \frac{(1 + x^2) - 2x^2}{(1 + x^2)^2} = \frac{1 - x^2}{(1 + x^2)^2}$, la moitié de $g''$ (fiche §1). En effet $g'(x) = \frac{2x}{1 + x^2}$ : $\frac{x}{1 + x^2} = \frac{g'}{2}$, et sa dérivée est $\frac{g''}{2}$.
6. Une fonction égale à sa série de Taylor (au voisinage d'un point) est dite **analytique** ; ce n'est pas automatique. Exemple de la fiche : la série de $\ln(1 + x)$ n'est égale à la fonction que pour $-1 < x \le 1$ (Ex M05a.25).
7. Par exemple *difference quotient* (quotient différentiel), *smooth* (lisse, ici infiniment dérivable), *chain rule* (règle de la chaîne).

**Grille.** (1) sécante, limite, tangente ; (2) la formule avec $x_0$ et la condition $\mathcal{C}^\infty$ ; (3) les quatre polynômes et l'explication par les dérivées nulles ; (4) les cinq coefficients ; (5) la règle du quotient et le lien avec $g'$ ; (6) le mot « analytique » et un exemple d'égalité limitée à un intervalle ; (7) trois mots traduits. Les réponses sont écrites avec tes mots, pas recopiées.

### Ex M05a.16 — Fermi : l'erreur d'arrondi d'une somme d'un million de nombres

**Réponse modèle.**
1. La somme finale vaut environ $n \times 1 = 10^6$ ; une somme partielle typique, environ la moitié, $5 \times 10^5$.
2. Chaque addition fait une erreur d'au plus $u$ fois la somme partielle, donc au plus $u \times 10^6$. Sur $10^6$ additions, au pire $10^6 \times u \times 10^6$, soit une erreur relative d'au plus $n\,u$ (environ $\frac{n\,u}{2}$ avec la somme partielle moyenne) : en `float64`, $10^6 \times 1{,}1 \times 10^{-16} \approx 10^{-10}$ ; en `float32`, $10^6 \times 6 \times 10^{-8} = 0{,}06$, soit **6 %**.
3. Avec des signes au hasard : $\sqrt{n}\,u$, soit $10^3 \times 1{,}1 \times 10^{-16} \approx 10^{-13}$ en `float64`, et $10^3 \times 6 \times 10^{-8} = 6 \times 10^{-5}$ en `float32`.
4. En `float32`, sur environ 7 chiffres : au pire **un seul** chiffre juste (6 %), dans le cas typique environ **quatre**.
5. Chaque nombre ne traverse qu'environ $\log_2 10^6 \approx 20$ additions : la borne du pire cas devient $20\,u$, soit $1{,}2 \times 10^{-6}$ en `float32` et $2 \times 10^{-15}$ en `float64`.
6. Une somme courante de losses en `float32` perd des chiffres à mesure qu'elle grandit, et un terme plus petit que $2^{-24}$ fois la somme (environ $6 \times 10^{-8}$) est entièrement absorbé (fiche §6). Les frameworks accumulent donc en `float64`, additionnent par paires, ou font des moyennes par batch avant de les combiner.

**Grille.** (1) l'ordre de grandeur de la somme ; (2) le raisonnement « $n$ erreurs de taille $u \times$ somme » et les deux valeurs ; (3) $\sqrt{n}$ et les deux valeurs ; (4) le nombre de chiffres justes ; (5) $\log_2 n$ ; (6) une conséquence concrète (absorption, accumulateur en `float64`). Un facteur 2 ou 3 près ne compte pas : c'est l'ordre de grandeur qui est demandé.

### Ex M05a.17 — Expliquer la convexité et pourquoi elle rassure quand on minimise

**Réponse modèle.**

> Une fonction convexe a la forme d'une cuvette : si tu tends une corde entre deux points de sa courbe, la corde reste au-dessus de la courbe ; autre image, chaque tangente reste au-dessous. Conséquence : une cuvette n'a pas de « faux fond ». Là où la pente est nulle, on est au minimum global, et toute descente qui suit la pente finit au même endroit, quel que soit le point de départ. C'est pour ça que la log-loss de la régression logistique est une bonne nouvelle : l'optimiseur ne peut pas se coincer dans un mauvais minimum. Contre-exemple : une courbe en W, comme $x^4 - 3x^2 + x$, a deux creux de profondeurs différentes ; une descente partie du mauvais côté de la bosse s'arrête dans le creux le moins profond, et la loss d'un réseau de neurones ressemble à cela, en bien pire.

**Grille.** (1) une image juste de la convexité (corde au-dessus, cuvette ou tangente au-dessous) ; (2) la garantie : un point où la pente s'annule est un minimum global, la descente ne se trompe pas de creux ; (3) un contre-exemple non convexe avec plusieurs creux ; (4) huit lignes au plus, sans formule compliquée.

<a id="entretien"></a>

## 💼 Entretien

### M05a.E1 — Pourquoi soustraire le maximum avant de calculer une softmax ?

**Réponse modèle (60 secondes).**

> Pour éviter un overflow. En `float64`, l'exponentielle déborde au-delà de 709 environ : un score de 1 000, qui n'a rien d'extraordinaire pour des logits, donne `inf`, et la softmax devient `inf / inf`, c'est-à-dire `nan`. En soustrayant le maximum, tous les exposants sont négatifs ou nuls : aucune exponentielle ne déborde, et le plus grand terme vaut exactement 1. Le résultat ne change pas, parce que la softmax est invariante par translation : le facteur $e^{-m}$ apparaît en haut et en bas, et se simplifie. Côté petites valeurs, une probabilité minuscule peut encore valoir 0 après la soustraction, mais la somme du dénominateur vaut au moins 1, donc jamais de division par zéro. Et pour la loss, on ne prend pas le logarithme de cette probabilité : on calcule le log-softmax, $z_i - \text{LSE}(\mathbf{z})$, avec le même maximum, ce qui donne une loss finie même quand la probabilité s'efface. C'est ce que font les fonctions de cross-entropy qui prennent des logits en entrée.

**Grille.** (1) l'overflow, avec le seuil d'environ 709 (ou $10^{308}$) ; (2) l'invariance par translation, qui garantit le même résultat ; (3) le dénominateur au moins 1, et ce qui reste des petites valeurs ; (4) le lien avec le log-softmax et la cross-entropy calculée à partir des logits.

<a id="notebook"></a>

## Notebook

### Ex M05a.18 — Évaluer un polynôme de Taylor · `taylor_polynomial`

**Réponses** : a) `0.717397` · b) `0.541667` · c) `0.416667` · d) `"ValueError"` · e) `"float"` · f) `4.0` · g) `148.4132`.

**Démarche.** `derivatives = list(derivatives)` (pour accepter un tuple ou un array), une `ValueError` si la liste est vide, puis une boucle qui garde à jour le terme $\frac{(x - a)^k}{k!}$ : `term = 1.0`, puis, pour $k \ge 1$, `term *= (x - a) / k`, et `total += derivative * term`. On renvoie `float(total)`. Pour la copie : a) est $\sin$ d'ordre 5 (contre $\sin 0{,}8 \approx 0{,}717356$), b) est $\cos$ d'ordre 4 ($\frac{13}{24}$, contre $\cos 1 \approx 0{,}5403$), c) est $\ln$ en 1 d'ordre 3 ($\frac{5}{12}$, contre $\ln 1{,}5 \approx 0{,}4055$).

**Erreurs fréquentes.** `derivative * (x - a) ** k / math.factorial(k)` : juste pour 30 termes, mais une `OverflowError` pour 200 (le test `with_many_terms`) ; oublier $k!$ ; écrire `x ** k` au lieu de `(x - a) ** k` (c) ; renvoyer l'entier 11 en e).

### Ex M05a.19 — La méthode de Newton, avec ses cas d'échec · `newton`

**Réponses** : a) `2.6457513111` · b) `0.5671432904` · c) `"ValueError"` · d) `"RuntimeError"` · e) `"aucune"` · f) `2.6458333` · g) `"float"`.

**Démarche.** `x = float(x0)`, puis `for _ in range(max_iter)` : si `f(x) == 0`, renvoyer `x` ; sinon, si `fprime(x) == 0`, lever la `ValueError` ; sinon calculer `x_new`, le renvoyer si `abs(x_new - x) < tol`, et continuer avec `x = x_new`. Après la boucle, lever la `RuntimeError`. Pour la copie : a) $3 \to \frac{8}{3} \to \frac{127}{48} \to 2{,}6457513$ ; b) résout $e^{-x} = x$ ; c) $f'(1) = 0$, et $x^2 - 2x + 5 = (x - 1)^2 + 4$ n'a pas de racine réelle ; e) $f(2) = f'(2) = 0$ : tester la pente avant $f(x) = 0$ lèverait une erreur sur un zéro déjà trouvé.

**Erreurs fréquentes.** Tester la pente avant $f(x) == 0$ (e) ; renvoyer l'ancienne valeur au lieu de la nouvelle (f : 2,6666667) ; une boucle `while` sans limite ; oublier `float(x0)` (g).

### Ex M05a.20 — L'extrapolation de Richardson : annuler le terme d'erreur en h² · `richardson_derivative`

**Réponses** : a) `-0.56464236` · b) `0.3333333333` · c) `"ValueError"` · d) `32.0` · e) `16.0` · f) `"float"` · g) `1.18`.

**Démarche.** `if not h > 0: raise ValueError(...)` (refuse aussi `nan`), une fonction interne `centred(step)`, puis `float((4 * centred(h / 2) - centred(h)) / 3)`. Pour la copie : la dérivée exacte de a) est $-\sin 0{,}6 \approx -0{,}56464247$ ; $D(0{,}1)$ se trompe d'environ $9{,}4 \times 10^{-4}$, Richardson d'environ $1{,}2 \times 10^{-7}$, 8 000 fois moins. d) Pour un polynôme de degré 4, $D(h) = f'(x) + c_2h^2$ exactement : la combinaison donne $4 \times 2^3 = 32$, alors que $D(0{,}5) = 34$. e) Un rapport de 16 : l'erreur est en $h^4$, la méthode d'ordre 4.

**Erreurs fréquentes.** Diviser chaque différence centrée par $h$ au lieu de $2h$ (le résultat vaut alors le double de la dérivée : b) donne $\frac{2}{3}$) ; mettre le poids 4 sur $D(h)$ au lieu de $D(\frac{h}{2})$ ; refuser seulement $h = 0$ et accepter un $h$ négatif (c) ; renvoyer le `numpy.float64` que donne `np.sin` (f).

### Ex M05a.21 — L'epsilon machine, en float64, float32 et float16 · `machine_epsilon`

**Réponses** : a) `True` · b) `-23.0` · c) `0.0009765625` · d) `"float"` · e) `True` · f) `9.0`.

**Démarche.** `one, two, eps = dtype(1), dtype(2), dtype(1)`, puis `while dtype(one + dtype(eps / two)) != one: eps = dtype(eps / two)`, et `return float(eps)`. La boucle tourne 52, 23 et 10 fois. Pour la copie : e) $1 + \frac{\varepsilon}{2}$ est exactement au milieu de 1 et du flottant suivant ; l'arrondi « au plus proche, à égalité vers le chiffre pair » donne 1. f) $2^9 = 512 \le 1000 < 1024$ : l'écart après 1 000 vaut $2^9\,\varepsilon$.

**Erreurs fréquentes.** Mélanger les types (`1 + eps / 2` avec un `1` de Python peut calculer dans un autre type selon les versions de NumPy) ; renvoyer `eps / 2` (b : $-24$) ; renvoyer un `numpy.float32` (d).

### Ex M05a.22 — Un log-sum-exp stable · `logsumexp`

**Réponses** : a) `2.241311` · b) `1200.313262` · c) `-1499.873072` · d) `0.0` · e) `True` · f) `"ValueError"` · g) `"float"` · h) `11.907755`.

**Démarche.** `values = [float(v) for v in values]`, une `ValueError` si la liste est vide, `m = max(values)`, `-math.inf` tout de suite si `m` est infini, sinon `float(m + math.log(math.fsum(math.exp(v - m) for v in values)))`. Pour la copie : le calcul direct lève une `OverflowError` en b) (`math.exp(1200)`) et une `ValueError` en c) ($\ln 0$, les deux exponentielles s'effacent) ; b) est entre 1 200 et $1200 + \ln 2$, h) atteint $5 + \ln 1000$.

**Erreurs fréquentes.** Oublier de rajouter $m$ ; ne pas traiter le cas où tout vaut $-\infty$ (`nan`) ; renvoyer un `numpy.float64` quand l'entrée est un array (g).

### Ex M05a.23 — SymPy `series` et `numpy.finfo` contre tes fonctions

**Réponses** : a) `"2/15"` · b) `"1/16"` · c) `-14.0` · d) `-307.65` · e) `True` · f) `1.34399`.

**Démarche.** a) `sp.series(sp.tan(x), x, 0, 7).removeO().coeff(x, 5)` ; b) de même avec `sp.sqrt(1 + x)` et `coeff(x, 3)` ; c) `math.log2(np.finfo(np.float16).tiny)` : le plus petit `float16` normal vaut $2^{-14} \approx 6{,}1 \times 10^{-5}$ ; d) `math.log10(np.finfo(float).tiny)` ; f) les dérivées de $e^{\sin x}$ en 0 valent $1, 1, 1, 0, -3$, et `mymath.approx.taylor_polynomial(derivatives, 0, 0.3)` donne $1{,}3439875$, contre $e^{\sin 0{,}3} \approx 1{,}34383$. Pour la copie : `float16` n'a que 5 bits d'exposant, d'où un maximum de $(2 - 2^{-10}) \times 2^{15} = 65\,504$ ; entre 0 et `tiny`, les nombres sous-normaux perdent peu à peu leurs chiffres significatifs.

**Erreurs fréquentes.** Lire le coefficient du mauvais degré ; confondre `tiny` et le plus petit sous-normal ($-24$ en c), $-323{,}31$ en d)) ou l'epsilon ; donner $e^{\sin 0{,}3}$ au lieu du polynôme en f).

### Ex M05a.24 — Prédire : Newton depuis un mauvais point de départ

**Réponses** : a) `1` · b) `2` · c) `3` · d) `3` · e) `2`.

**Démarche.** a) Depuis 1 : $-0{,}57$, $0{,}12$, $-0{,}001$ : convergence vers 0. b) Depuis 1,5, la courbe de $\arctan$ est déjà aplatie : la tangente renvoie en $-1{,}69$, puis $2{,}32$, $-5{,}11$, $32{,}3$ : la suite s'éloigne (le seuil est vers 1,39). c) $0 \to 1 \to 0 \to \ldots$ : un cycle. d) $\frac{f(x)}{f'(x)} = \frac{x^{1/3}}{\frac{1}{3}x^{-2/3}} = 3x$, donc $x_{k+1} = -2x_k$ : la distance double. e) $x_{k+1} = x_k - \frac{x_k^2}{2x_k} = \frac{x_k}{2}$ : convergence linéaire, la racine est double.

### Ex M05a.25 — Taylor de plus en plus loin : où le polynôme décroche

**Réponses** : a) `0.001827` · b) `1.54` · c) `0.8368` · d) `97.7` · e) `28` · f) `0.004975`.

**Démarche.** `float(sum((-1) ** (k + 1) * x ** k / k for k in range(1, n + 1)))`. Pour $0 < x < 1$, l'erreur est plus petite que le premier terme négligé $\frac{|x|^{n+1}}{n + 1}$ (série alternée) et décroît géométriquement ; en $x = 1$, elle ne décroît que comme $\frac{1}{2n}$ environ (quelque 500 000 termes pour $10^{-6}$) ; en $x = 1{,}5$, le terme $\frac{1{,}5^k}{k}$ grandit sans limite : la somme oscille de plus en plus fort et la série diverge.

**Erreurs fréquentes.** Oublier l'alternance des signes ; `range(1, n)` ($n - 1$ termes : e) donne 29) ; croire qu'ajouter des termes améliore toujours l'approximation.

### Ex M05a.26 — Une fonction et ses polynômes de Taylor d'ordre 1, 2 et 3

**Démarche.** Une grille `xs = np.linspace(a - 2, a + 2, 401)`, `ax.plot(xs, f(xs), label=...)`, puis pour chaque ordre la liste des valeurs `taylor_polynomial(derivatives[:order + 1], a, x)`, tracée avec un label, le point `ax.plot(a, f(a), "o")` et `ax.legend()`. Pour la copie : près de $\frac{\pi}{4}$, la zone où l'écart reste invisible s'élargit avec l'ordre (environ $\pm 0{,}3$, $\pm 0{,}6$, $\pm 1$) ; la tangente est au-dessus de la courbe, qui est concave près de $\frac{\pi}{4}$ ($\sin'' = -\sin < 0$) ; le polynôme d'ordre 2 traverse la courbe en $\frac{\pi}{4}$ : $\sin x - P_2(x)$ commence par $-\frac{\sqrt{2}}{12}(x - a)^3$, positif à gauche (le polynôme est au-dessous) et négatif à droite (il est au-dessus) ; loin de $a$, chaque polynôme part vers l'infini alors que $\sin$ reste bornée : l'approximation est locale.

**Erreurs fréquentes.** Prendre toutes les dérivées pour chaque ordre (`derivatives` au lieu de `derivatives[:order + 1]`) ; ouvrir une nouvelle figure dans la fonction ; oublier le point de contact ou la légende.

### Ex M05a.27 — Chasse à l'erreur : une softmax qui renvoie `nan`

**Réponses** : a) `"ACEF"` · b) `[1000, 1.368, 1000.313, 0.731, -800.313, 1.0]`.

**Démarche.** (A) retire le minimum au lieu du maximum : `math.exp(1000 - 200)` lève une `OverflowError` (en NumPy, `inf`, puis `inf / inf` donne `nan`). (B) est juste : $1 + e^{-1} + e^{-800} \approx 1{,}368$. (C) oublie de rajouter $m$ : $1000 + \ln 1{,}368 \approx 1000{,}313$. (D) est juste : $\frac{1}{1{,}368} \approx 0{,}731$. (E) a la bonne formule sur le papier, mais $e^{-800}$ s'efface en `float64` : la ligne calcule `math.log(0.0)` et lève une `ValueError` ; le log-softmax se calcule directement, $200 - 1000{,}313 = -800{,}313$. (F) divise par $n$ au lieu du total : la somme des probabilités vaut 1.

**Erreurs fréquentes.** Accuser (B) ou (D), justes ; ne pas voir que (E) échoue à l'exécution ; en b), donner $-800$ pour (E) (le maximum au lieu du log-sum-exp).

### Ex M05a.28 — Erreur relative ou absolue : choisir la tolérance d'un test

**Démarche.** Une `ValueError` si une tolérance est négative ; `True` si `got == expected` (ce qui couvre deux infinis égaux) ; `False` si l'un des deux est infini ou `nan` ; sinon l'inégalité, avec $\max(|\text{got}|, |\text{expected}|)$, ce qui rend la fonction symétrique. Pour la copie : une tolérance relative ($10^{-12}$, par exemple) pour `logsumexp([1000, 1000])` ; une tolérance absolue, choisie selon l'échelle des nombres soustraits, pour une valeur qui devrait être nulle. `numpy.isclose(a, b)` multiplie `rtol` par $|b|$ seulement (pas symétrique), et son `atol=1e-8` par défaut déclare « proches » $10^{-10}$ et $10^{-20}$ : pour de petites grandeurs, il faut le baisser.

**Erreurs fréquentes.** Ne pas traiter les infinis à part : pour `(math.inf, 1e308)` avec `rel_tol=0.5`, la formule seule compare `inf <= inf` et répond `True` ; multiplier `rel_tol` par $|\text{expected}|$ seulement (le cas `(1.1, 1.0)`) ; oublier la `ValueError` des tolérances négatives.

### Ex M05a.29 — Défi : une racine cubique à 10⁻¹² en le moins d'itérations possible

**Réponse** : `3.6840314986`.

**Démarche.** `m, e = math.frexp(a)`, `q, r = divmod(e, 3)`, puis le départ $x_0 = (0{,}6 + 0{,}4\,m) \times 2^{r/3} \times 2^q$ (les trois valeurs $2^{r/3}$ calculées une fois) ; $0{,}6 + 0{,}4\,m$ approche $\sqrt[3]{m}$ à moins de 1 % près sur $[0{,}5 ;\ 1[$. Puis `x_new = (2 * x + a / (x * x)) / 3` jusqu'à `abs(x_new - x) <= 1e-15 * x_new`, en comptant les pas. Pour la copie : l'erreur relative est à peu près élevée au carré à chaque pas : $10^{-2} \to 10^{-4} \to 10^{-8} \to 10^{-16}$, trois pas, plus un quatrième qui constate que la valeur ne bouge plus. Depuis $x_0 = 1$ et pour $a = 10^{30}$, il en faut 118 : tant que $x^3 \gg a$, le pas vaut à peu près $x \leftarrow \frac{2x}{3}$, une décroissance géométrique lente, et la convergence quadratique ne commence qu'une fois arrivé près de $10^{10}$.

**Erreurs fréquentes.** Partir de $x_0 = a$ ou $x_0 = 1$ (plus de cent pas pour les nombres extrêmes, et même une `ZeroDivisionError` pour $a = 5 \times 10^{-300}$, où `x * x` s'efface à 0 : la vraie correction est le point de départ, pas un test de plus) ; un critère d'arrêt absolu (`abs(x_new - x) < 1e-12`), jamais atteint pour $a = 10^{300}$ (des racines de l'ordre de $10^{100}$, espacées de bien plus que $10^{-12}$) et trop lâche pour $a = 10^{-30}$ ; compter les pas de travers.
