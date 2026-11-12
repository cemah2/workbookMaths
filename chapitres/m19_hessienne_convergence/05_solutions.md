# M19 · Hessienne, conditionnement et convergence — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Ponts, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M19.Q1 — La hessienne : de quelle taille, symétrique, de quoi ?
1. $(5, 5)$ ; au plus $5 + 4 + 3 + 2 + 1 = 15$ dérivées distinctes (la diagonale et un triangle), grâce à Schwarz.
2. Vrai : la ligne $i$ de la hessienne est le gradient de $\frac{\partial f}{\partial x_i}$.
3. $\begin{pmatrix} 0 & z & y \\ z & 0 & x \\ y & x & 0 \end{pmatrix} = \begin{pmatrix} 0 & 3 & 2 \\ 3 & 0 & 1 \\ 2 & 1 & 0 \end{pmatrix}$.
4. $\mathbf{A}$, constante.
5. Vrai : les dérivées d'ordre 3 sont nulles, le reste aussi.
6. $2 \times 0{,}36 - 4 \times 0{,}64 = -1{,}84$ : la fonction tourne vers le bas dans cette direction.

### M19.Q2 — Minimum, maximum, selle ou direction plate ?
1. Minimum local (toutes positives).
2. Maximum local (toutes négatives).
3. Point selle (des deux signes).
4. Le test ne conclut pas (une valeur propre nulle, les autres positives) : c'est l'ordre suivant qui décide.
5. Point selle : $\det = 1 - 4 = -3 < 0$, le produit des deux valeurs propres est négatif, elles sont de signes contraires (ce sont $3$ et $-1$).
6. Faux : $(-1, -2, 3)$ donne $\det = 6 > 0$, et c'est une selle.

### M19.Q3 — Converge ou pas : lire les valeurs propres de M
1. Oui ; facteur $0{,}9$ au pire.
2. Non : la composante de valeur propre $1{,}1$ grandit.
3. Non : la composante de valeur propre $-1$ change de signe à chaque pas sans diminuer.
4. $\rho = 0{,}5$ et $2^{10} = 1\,024 \ge 1\,000$ : 10 pas ($2^9 = 512$ ne suffit pas).
5. Oui : l'écart reste un vecteur propre, multiplié par $0{,}2$ à chaque pas (en arithmétique exacte ; sur ordinateur, les arrondis créent une petite composante sur l'autre direction, qui finit par grandir).
6. Faux : la limite est l'unique point fixe, quel que soit le départ.

### M19.Q4 — Le pas de Richardson : lire la convergence sur les valeurs propres de I − ωA
1. $1 - 0{,}15 = 0{,}85$ et $1 - 0{,}3 = 0{,}7$ : converge, facteur $0{,}85$.
2. $\frac{2}{4} = 0{,}5$.
3. $1 - 1{,}2 = -0{,}2$ et $1 - 2{,}4 = -1{,}4$ : diverge (la composante de la valeur propre 4).
4. $1{,}2$ et $1{,}4$ : diverge ; un pas négatif monte au lieu de descendre.
5. $\omega^\star = \frac{2}{2 + 4} = \frac13$, et le facteur $\frac{\kappa - 1}{\kappa + 1} = \frac13$, avec $\kappa = 2$.
6. Vrai : $0 < \omega\lambda_i \le \omega\lambda_{\max} < 2$ donne $-1 < 1 - \omega\lambda_i < 1$.

### M19.Q5 — Le conditionnement : ce qui ralentit, ce qui ne change rien
1. $\kappa = 100$.
2. Le conditionnement ne change pas, le pas critique est divisé par 10, le nombre d'itérations au meilleur pas ne change pas.
3. $\frac{99}{101} \approx 0{,}980$.
4. (C) : $\frac{6\ln 10}{-\ln(99/101)} \approx 691$ ; l'approximation $1{,}15\,\kappa\,d$ donne 690.
5. $\tilde{\mathbf{A}} = \begin{pmatrix} 1 & 0{,}3 \\ 0{,}3 & 1 \end{pmatrix}$ ($\frac{0{,}9}{\sqrt{9 \times 1}} = 0{,}3$), de valeurs propres $1{,}3$ et $0{,}7$ : $\kappa = \frac{13}{7} \approx 1{,}86$, contre $\frac{9{,}1}{0{,}9} \approx 10{,}1$ pour $\mathbf{A}$.
6. Faux : $\mathbf{Q}^\top\mathbf{A}\mathbf{Q}$ a les mêmes valeurs propres que $\mathbf{A}$.

### M19.Q6 — Module d'un nombre complexe et racines d'un trinôme
1. $\sqrt{64 + 225} = 17$.
2. $2 - 7i$ ; $4 + 49 = 53$.
3. $\Delta = -36$ : $2 \pm 3i$ ; somme 4, produit 13, module $\sqrt{13} \approx 3{,}61$ pour les deux.
4. $\lvert 0{,}6 + 0{,}8i\rvert = 1$, donc 1.
5. Vrai.
6. $\Delta = 0{,}04 - 1{,}96 < 0$ : racines complexes, de module $\sqrt{0{,}49} = 0{,}7$.

### M19.Q7 — Un gradient estimé sur un échantillon : vrai ou faux
1. Vrai.
2. Vrai : $\sigma^2/B$.
3. Faux : l'erreur type est divisée par $\sqrt2$.
4. Vrai : $\sqrt{100} = 10$.
5. Vrai : on tire tous les termes, la moyenne est la vraie.
6. Faux : une estimation isolée peut pointer dans l'autre sens, surtout près d'un minimum ; seule sa moyenne sur les tirages est le vrai gradient.

### M19.Q8 — Boule ou pavé : la direction est-elle gardée ?
1. $(0, 3)$.
2. $(2 ;\ 1{,}2)$ : non, $(7 ;\ 1{,}2)$ et $(2 ;\ 1{,}2)$ ne sont pas proportionnels.
3. $(2, -2)$ : oui, c'est $0{,}4 \times (5, -5)$ (les deux coordonnées ont la même valeur absolue).
4. $(2 ;\ -1{,}5)$ lui-même : sa norme vaut $2{,}5 < 4$.
5. Vrai : le premier résultat est dans la boule.
6. Faux : c'est la projection sur le pavé $[-r, r]^n$ ; $(r, r)$ y reste, de norme $r\sqrt2 > r$.

<a id="rappels"></a>

## 🔁 Rappels

### M19.R1 — Le théorème spectral et les valeurs propres d'une matrice symétrique (M12c)
1. $\lambda^2 - 9\lambda + 14 = 0$ : $7$ et $2$.
2. $\frac{1}{\sqrt5}(2, 1)$ pour 7 ($\mathbf{S}(2, 1) = (14, 7)$) et $\frac{1}{\sqrt5}(1, -2)$ pour 2 ($\mathbf{S}(1, -2) = (2, -4)$).
3. Vrai : des vecteurs propres de valeurs propres distinctes d'une matrice symétrique sont orthogonaux (pour une valeur propre double, comme pour $\mathbf{I}$, il faut les **choisir** orthogonaux ; le théorème spectral dit qu'on le peut).
4. $343$ et $8$.
5. Oui : ses deux valeurs propres sont positives.
6. $7y_1^2 + 2y_2^2$.

### M19.R2 — Suites géométriques et récurrences d'ordre 1 (R5)
1. $4 \times 0{,}343 = 1{,}372$.
2. Vers 0.
3. $\ell = 6$ ; $v_k = 6 + (v_0 - 6)\,0{,}5^k$.
4. $13$ ($0{,}7^{12} \approx 0{,}0138$, $0{,}7^{13} \approx 0{,}0097$).
5. Faux : l'écart au point fixe $\frac{1}{2{,}2}$ est multiplié par $-1{,}2$, de module $> 1$ ; seul le départ au point fixe ne bouge pas.

### M19.R3 — Le conditionnement par la SVD (M12d)
1. $16$.
2. $\mathbf{A}^\top\mathbf{A} = \mathbf{A}^2$ a pour valeurs propres les $\lambda_i^2$ ; les valeurs singulières sont leurs racines, $\lvert\lambda_i\rvert = \lambda_i$ puisque les $\lambda_i$ sont positives.
3. Le même : les valeurs singulières sont toutes multipliées par 3.
4. 1 : toutes ses valeurs singulières valent 1.
5. $\kappa = 3/0{,}5 = 6$ au sens de la SVD ; mais Richardson diverge pour tout $\omega > 0$ : la valeur propre $-0{,}5$ donne $1 + 0{,}5\,\omega > 1$. La matrice n'est pas définie positive, et le conditionnement seul ne dit pas si Richardson converge.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M19.1 — La hessienne d'une fonction de trois variables, et son développement de Taylor d'ordre 2

**Réponses.** a) `[2, 0, 5]` · b) `[[5, -4, 2], [-4, 1, 4], [2, 4, 2]]` · c) `4.7` · d) `4.775` · e) `4.779` · f) `5` · g) `-11` · h) `False`.

**Démarche.** En $\mathbf{p} = (1, 1, 2)$, $e^{x - y} = 1$ et $f(\mathbf{p}) = 2 + 4 - 3 + 1 = 4$. Le gradient : $\frac{\partial f}{\partial x} = 2xz - 3y + e^{x-y} = 4 - 3 + 1 = 2$, $\frac{\partial f}{\partial y} = z^2 - 3x - e^{x-y} = 4 - 3 - 1 = 0$, $\frac{\partial f}{\partial z} = x^2 + 2yz = 5$. Les dérivées secondes : $f_{xx} = 2z + e^{x-y} = 5$, $f_{xy} = -3 - e^{x-y} = -4$, $f_{xz} = 2x = 2$, $f_{yy} = e^{x-y} = 1$, $f_{yz} = 2z = 4$, $f_{zz} = 2y = 2$. Avec $\mathbf{h} = (0{,}1 ;\ -0{,}2 ;\ 0{,}1)$ : $\nabla f^\top\mathbf{h} = 0{,}2 + 0{,}5 = 0{,}7$, d'où c) $4{,}7$ ; $\mathbf{H}\mathbf{h} = (1{,}5 ;\ -0{,}2 ;\ -0{,}4)$, $\mathbf{h}^\top\mathbf{H}\mathbf{h} = 0{,}15 + 0{,}04 - 0{,}04 = 0{,}15$, d'où d) $4{,}7 + 0{,}075 = 4{,}775$. e) $1{,}21 \times 2{,}1 + 0{,}8 \times 4{,}41 - 3 \times 0{,}88 + e^{0{,}3} = 2{,}541 + 3{,}528 - 2{,}64 + 1{,}349859 = 4{,}778859$. f) $\mathbf{H}(2, -1, 2) = (18, -1, 4)$, produit scalaire avec $(2, -1, 2)$ : $36 + 1 + 8 = 45$, divisé par 9 : 5. g) $5 \times 1 - 16 = -11$.

Dans ta copie : l'erreur de c) vaut environ $0{,}079$, celle de d) $0{,}0039$ ; avec $\lVert\mathbf{h}\rVert = \sqrt{0{,}06} \approx 0{,}245$, la première est de l'ordre de $\lVert\mathbf{h}\rVert^2$, la seconde de $\lVert\mathbf{h}\rVert^3$. h) Un mineur principal négatif suffit à exclure « définie positive » (Sylvester) ; directement, la courbure vaut $f_{xx} = 5 > 0$ le long de $\mathbf{e}_1$, et, le long de $(1, 1, 0)/\sqrt2$, $\frac{5 - 8 + 1}{2} = -1 < 0$ : la hessienne est indéfinie (ses valeurs propres sont environ $7{,}52$ ; $5$ ; $-4{,}52$). $\mathbf{H}\mathbf{u} = \frac13(18, -1, 4)$ n'est pas proportionnel à $\mathbf{u}$ : ce n'est pas un vecteur propre. La courbure dans une direction unitaire est toujours entre $\lambda_{\min}$ et $\lambda_{\max}$ (le quotient de Rayleigh).

**Erreurs fréquentes.** Oublier le $\frac12$ (d) donnerait $4{,}85$). Dériver $e^{x - y}$ par rapport à $y$ sans le signe moins ($f_{xy} = -2$). Arrondir $e^{0{,}3}$ trop tôt : la valeur $4{,}778859$ est tout près de $4{,}77885$, et quatre décimales basculeraient avec $e^{0{,}3} \approx 1{,}34985$ (d'où les trois décimales demandées).

**Variante.** Au point $(0, 0, 1)$ : $f = 1$, $\nabla f = (1, 0, 0)$ et $\nabla^2 f = \begin{pmatrix} 3 & -4 & 0 \\ -4 & 1 & 2 \\ 0 & 2 & 0 \end{pmatrix}$.

### Ex M19.2 — Classer les points critiques d'une fonction de trois variables

**Réponses.** a) `4` · b) `[[-2, -1, 1], [-1, -2, 1], [1, 2, 1], [2, 1, 1]]` · c) `[2, 6, 18]` · d) `[-18, -6, 2]` · e) `[2, 1, 1, 0]` · f) `-29` · g) `False`.

**Démarche.** Le gradient $(3x^2 + 3y^2 - 15,\ 6xy - 12,\ 2z - 2)$ s'annule pour $z = 1$, $x^2 + y^2 = 5$ et $xy = 2$. Alors $(x + y)^2 = 9$ et $(x - y)^2 = 1$ : $x + y = \pm3$, $x - y = \pm1$, d'où les quatre points $(2, 1)$, $(1, 2)$, $(-1, -2)$, $(-2, -1)$. La hessienne vaut $\begin{pmatrix} 6x & 6y & 0 \\ 6y & 6x & 0 \\ 0 & 0 & 2 \end{pmatrix}$ ; le bloc a pour valeurs propres $6(x + y)$ (vecteur $(1, 1)$) et $6(x - y)$ (vecteur $(1, -1)$), et la troisième vaut 2. En $(2, 1, 1)$ : $18$, $6$, $2$, minimum local, $f = 8 + 6 - 30 - 12 + 1 - 2 = -29$. En $(1, 2, 1)$ : $18$, $-6$, $2$. En $(-1, -2, 1)$ : $-18$, $6$, $2$. En $(-2, -1, 1)$ : $-18$, $-6$, $2$.

Dans ta copie : la valeur propre 2 (la direction $z$) est positive partout : aucun point ne peut avoir trois valeurs propres négatives, donc aucun maximum local. Directions de descente : $(1, 1, 0)$ en $(-2, -1, 1)$ et en $(-1, -2, 1)$, $(1, -1, 0)$ en $(1, 2, 1)$ et en $(-2, -1, 1)$. Le minimum n'est pas global : $f(x, 0, 1) = x^3 - 15x - 1 \to -\infty$ quand $x \to -\infty$.

**Erreurs fréquentes.** Oublier deux des quatre solutions (ne garder que $x, y > 0$). Classer $(-2, -1, 1)$ comme maximum parce que le bloc $(x, y)$ est défini négatif : la direction $z$ monte. Conclure par le seul déterminant : en $(-2, -1, 1)$, il vaut $(-18)(-6)(2) = 216 > 0$.

**Variante.** Avec $-z^2 + 2z$ à la place de $z^2 - 2z$, la troisième valeur propre devient $-2$ : $(-2, -1, 1)$ est alors un maximum local ($f = 29$), et $(2, 1, 1)$ une selle.

### Ex M19.3 — Une itération linéaire 2 × 2 : point fixe, erreur, et convergence par les valeurs propres

**Réponses.** a) `[4, 2]` · b) `[[1.6, 0.8], [2.56, 1.28]]` · c) `[0.6, 0.1]` · d) `[1, -2]` · e) `[4.43, 2.22]` · f) `14` · g) `True`.

**Démarche.** a) $(\mathbf{I} - \mathbf{M})\mathbf{x}^\star = \mathbf{c}$ : $0{,}5x - 0{,}2y = 1{,}6$ et $-0{,}2x + 0{,}8y = 0{,}8$, d'où $(4, 2)$. b) $\mathbf{x}_1 = \mathbf{c}$, puis $\mathbf{x}_2 = \mathbf{M}\mathbf{c} + \mathbf{c} = (0{,}96 + 1{,}6 ;\ 0{,}48 + 0{,}8)$. c) $\mathbf{M}\mathbf{q}_1 = (1{,}2 ;\ 0{,}6) = 0{,}6\,\mathbf{q}_1$ et $\mathbf{M}\mathbf{q}_2 = (0{,}1 ;\ -0{,}2) = 0{,}1\,\mathbf{q}_2$. d) $\mathbf{e}_0 = (0, 5) = \mathbf{q}_1 - 2\mathbf{q}_2$. e) $\mathbf{x}_3 = (4, 2) + 0{,}216\,(2, 1) - 2 \times 0{,}001\,(1, -2) = (4{,}43 ;\ 2{,}22)$. f) $0{,}6^{13} \approx 0{,}0013$, $0{,}6^{14} \approx 0{,}00078$. g) $\mathbf{e}_0 = (1, -2) = \mathbf{q}_2$, multiplié par $0{,}1$ à chaque pas.

Dans ta copie : depuis $\mathbf{0}$, $\mathbf{e}_0 = (-4, -2) = -2\,\mathbf{q}_1$ est un vecteur propre, donc $\mathbf{e}_2 = 0{,}36\,\mathbf{e}_0 = (-1{,}44 ;\ -0{,}72)$. Pour d), $\mathbf{e}_k = 0{,}6^k\,\mathbf{q}_1 - 2 \times 0{,}1^k\,\mathbf{q}_2$. f) Le pire départ est le long de $\mathbf{q}_1$, où l'écart est multiplié par $0{,}6$ ; tout autre écart a une composante sur $\mathbf{q}_1$ qui diminue au plus aussi vite. Les départs dont l'écart est le long de $\mathbf{q}_2$ convergent plus vite (facteur $0{,}1$).

**Erreurs fréquentes.** Prendre $\mathbf{x}_0$ au lieu de l'écart $\mathbf{x}_0 - \mathbf{x}^\star$ dans d). Compter 13 pas en f) ($0{,}6^{13} > 10^{-3}$). Écrire $\mathbf{x}_3 = \mathbf{M}^3\mathbf{x}_0$ en oubliant $\mathbf{c}$.

**Variante.** Depuis $\mathbf{x}_0 = (6, 3)$, l'écart $(2, 1) = \mathbf{q}_1$ donne $\mathbf{x}_3 = (4{,}432 ;\ 2{,}216)$.

### Ex M19.4 — Résoudre un système 2 × 2 par l'itération de Richardson : trois pas à la main, et le pas critique

**Réponses.** a) `[-0.5, 1.5]` · b) `[[0.16, 0.48], [0.1408, 0.7296], [0.069376, 0.883968]]` · c) `[-0.998784, 1.372032]` · d) `[8, 2]` · e) `[0.36, 0.84]` · f) `0.25` · g) `-1.4` · h) `True`.

**Démarche.** a) $\det\mathbf{A} = 16$, $\mathbf{x}^\star = \frac{1}{16}\begin{pmatrix} 5 & -3 \\ -3 & 5 \end{pmatrix}(2, 6) = (-0{,}5 ;\ 1{,}5)$. b) $\mathbf{x}_1 = 0{,}08\,\mathbf{b} = (0{,}16 ;\ 0{,}48)$ ; $\mathbf{A}\mathbf{x}_1 = (2{,}24 ;\ 2{,}88)$, résidu $(-0{,}24 ;\ 3{,}12)$, $\mathbf{x}_2 = (0{,}1408 ;\ 0{,}7296)$ ; $\mathbf{A}\mathbf{x}_2 = (2{,}8928 ;\ 4{,}0704)$, résidu $(-0{,}8928 ;\ 1{,}9296)$, $\mathbf{x}_3 = (0{,}069376 ;\ 0{,}883968)$. c) $\mathbf{A}\mathbf{x}_3 = (2{,}998784 ;\ 4{,}627968)$. d) $5 \pm 3$, vecteurs $(1, 1)$ et $(1, -1)$. e) $1 - 0{,}64$ et $1 - 0{,}16$. f) $2/8$. g) $1 - 0{,}3 \times 8 = -1{,}4$ (l'autre vaut $0{,}4$). h) L'écart $(1, -1)$ est un vecteur propre de valeur propre $0{,}4$.

Dans ta copie : $\mathbf{e}_0 = -\mathbf{x}^\star = -0{,}5\,(1, 1) + 1 \times (1, -1)$. La composante le long de $(1, -1)$ (valeur propre 2 de $\mathbf{A}$) n'est multipliée que par $0{,}84$ à chaque pas : c'est elle qui traîne ; celle le long de $(1, 1)$ est multipliée par $0{,}36$. Avec $\omega = 0{,}3$ depuis $\mathbf{0}$, la composante le long de $(1, 1)$ est multipliée par $-1{,}4$ : les itérés sautent de part et d'autre, de plus en plus loin. h) Ce départ n'a aucune composante sur la direction qui diverge ; le théorème parle de tout départ, et presque tout départ en a une. Sur ordinateur, les arrondis en créent une, minuscule, qui est multipliée par $-1{,}4$ à chaque pas : en `float64`, l'itération finit par diverger, après une centaine de pas.

**Erreurs fréquentes.** Oublier de recalculer $\mathbf{A}\mathbf{x}_k$ à chaque pas. Donner $\frac{2}{\lambda_{\min}} = 1$ pour le pas critique. Répondre $0{,}4$ à g) (la valeur propre de plus petit module), ou $1{,}4$ (son module, sans le signe).

**Variante.** Avec $\omega = 0{,}05$ : $\mathbf{x}_1 = (0{,}1 ;\ 0{,}3)$, $\mathbf{x}_2 = (0{,}13 ;\ 0{,}51)$, et $\mathbf{I} - 0{,}05\,\mathbf{A}$ a les valeurs propres $0{,}6$ et $0{,}9$.

### Ex M19.5 — Le meilleur pas de Richardson (énoncé), et le nombre d'itérations pour gagner six décimales

**Réponses.** a) `[1, 7, 13]` · b) `"2/13"` · c) `"1/7"` · d) `"6/7"` · e) `90` · f) `"12/13"` · g) `173` · h) `760`.

**Démarche.** a) Le bloc $\begin{pmatrix} 7 & 6 \\ 6 & 7 \end{pmatrix}$ a pour valeurs propres $13$ et $1$, et le troisième axe donne 7 ; $\kappa = 13$. b) $\frac{2}{13}$. c) $\frac{2}{1 + 13} = \frac17$. d) $\frac{13 - 1}{13 + 1} = \frac{12}{14}$. e) $\frac{6\ln 10}{\ln(7/6)} = \frac{13{,}8155}{0{,}154151} \approx 89{,}6$, donc 90 ($(6/7)^{89} \approx 1{,}10 \times 10^{-6}$ ne suffit pas). f) $1 - \frac{1}{13}$. g) $\frac{13{,}8155}{\ln(13/12)} = \frac{13{,}8155}{0{,}080043} \approx 172{,}6$, donc 173. h) $\rho^\star = \frac{109}{111}$, $\frac{13{,}8155}{0{,}018182} \approx 759{,}8$, donc 760.

Dans ta copie : $\rho(\frac17) = \max\left(\lvert 1 - \frac17\rvert, \lvert 1 - \frac{13}{7}\rvert\right) = \frac67$ ; la valeur propre du milieu donne $\lvert 1 - 1\rvert = 0$ : seules les deux extrêmes comptent (∂ M19.11.4). L'approximation $1{,}15\,\kappa\,d$ donne $1{,}15 \times 13 \times 6 \approx 90$ et $1{,}15 \times 110 \times 6 \approx 759$ : multiplier $\kappa$ par environ 8,5 multiplie le travail d'autant. Le pas prudent coûte $173/90 \approx 1{,}9$ fois plus, environ deux fois, comme le dit la fiche.

**Erreurs fréquentes.** Prendre $\frac{\kappa - 1}{\kappa + 1}$ avec $\kappa = \lambda_{\max} - \lambda_{\min}$. Arrondir e) vers le bas (89 pas laissent $1{,}10 \times 10^{-6}$). Utiliser la valeur propre 7 dans le facteur.

**Variante.** $\mathbf{A} = \begin{pmatrix} 4 & 3 & 0 \\ 3 & 4 & 0 \\ 0 & 0 & 2 \end{pmatrix}$ : valeurs propres $1$, $2$, $7$, $\omega^\star = \frac14$, $\rho^\star = \frac34$, et 49 itérations pour 6 décimales.

### Ex M19.6 — Une récurrence d'ordre 2 à racines réelles : terme général et convergence

**Réponses.** a) `[0.5, 0.2]` · b) `[2, 1]` · c) `[0.54, 0.258]` · d) `0.001953` · e) `[2, -0.5]` · f) `-1` · g) `True`.

**Démarche.** a) $r^2 - 0{,}7r + 0{,}1 = (r - 0{,}5)(r - 0{,}2)$. b) $\alpha + \beta = 3$ et $0{,}5\alpha + 0{,}2\beta = 1{,}2$ : $0{,}3\alpha = 0{,}6$, $\alpha = 2$, $\beta = 1$. c) $u_2 = 0{,}84 - 0{,}3 = 0{,}54$, $u_3 = 0{,}378 - 0{,}12 = 0{,}258$. d) $2 \times 0{,}5^{10} + 0{,}2^{10} = 0{,}001953125 + 0{,}0000001024 \approx 0{,}0019532$. e) $r^2 - 1{,}5r - 1 = (r - 2)(r + 0{,}5)$. f) $v_k = \alpha\,2^k + \beta(-0{,}5)^k$ tend vers 0 si et seulement si $\alpha = 0$ ; alors $\beta = v_0 = 2$ et $v_1 = 2 \times (-0{,}5) = -1$. g) $q = 0{,}1$ et $\lvert p\rvert = 0{,}7 < 1{,}1$.

Dans ta copie : par b), $u_2 = 2 \times 0{,}25 + 0{,}04$ et $u_3 = 2 \times 0{,}125 + 0{,}008$. Le terme $2 \times 0{,}5^k$ l'emporte, et $u_{k+1}/u_k \to 0{,}5$, la plus grande racine. Pour $(v_k)$, le coefficient de $2^k$ doit être nul. Sur ordinateur, si $v_1$ est arrondi à $-1 + \delta$, $\alpha = \delta/2{,}5 \ne 0$ et $\alpha\,2^k$ finit par l'emporter : la suite tend d'abord vers 0, puis explose (ici, $-1$ et les termes $2(-0{,}5)^k$ sont exacts en binaire, et le calcul tient).

**Erreurs fréquentes.** Associer $\alpha$ à la petite racine. Écrire le polynôme de $(v_k)$ avec $+1$ au lieu de $-1$ ($r^2 - 1{,}5r + 1$, de racines complexes). Oublier le coefficient $\alpha = 2$ en d) (on trouverait environ $0{,}000977$).

**Variante.** $u_{k+2} = 0{,}9\,u_{k+1} - 0{,}2\,u_k$ avec $u_0 = 2$, $u_1 = 0{,}9$ : racines $0{,}5$ et $0{,}4$, et $u_k = 0{,}5^k + 0{,}4^k$.

### Ex M19.7 — Une récurrence d'ordre 2 à racines complexes : module et oscillation amortie

**Réponses.** a) `-1.44` · b) `[0.25, 0.6]` · c) `0.65` · d) `1.176` · e) `[-0.2975, -0.254375, -0.001494, 0.106727]` · f) `[1, 0]` · g) `17` · h) `5.34`.

**Démarche.** a) $0{,}25 - 1{,}69 = -1{,}44$. b) $\frac{0{,}5}{2} \pm i\,\frac{\sqrt{1{,}44}}{2} = 0{,}25 \pm 0{,}6i$. c) $\sqrt{0{,}0625 + 0{,}36} = 0{,}65 = \sqrt{0{,}4225}$. d) $\cos\theta = \frac{0{,}5}{2 \times 0{,}65} = \frac{5}{13}$ (et $\sin\theta = \frac{12}{13}$), $\theta = \arccos\frac{5}{13} \approx 1{,}1760$. e) $u_2 = 0{,}125 - 0{,}4225$, $u_3 = -0{,}14875 - 0{,}105625$, $u_4 = -0{,}1271875 + 0{,}12569375$, $u_5 = -0{,}000746875 + 0{,}10747344$. f) $A = u_0 = 1$, puis $0{,}65\left(\frac{5}{13} + \frac{12}{13}B\right) = 0{,}25$ donne $B = 0$. g) $0{,}65^{16} \approx 0{,}00102$ et $0{,}65^{17} \approx 0{,}00066$. h) $\frac{2\pi}{1{,}1760} \approx 5{,}34$.

Dans ta copie : $u_4 = 0{,}65^4\cos(4\theta) = 0{,}17850625 \times (-0{,}008368) \approx -0{,}001494$. Ici $u_k = 0{,}65^k\cos k\theta$ et $\lvert\cos\rvert \le 1$. Les racines sont aux points $(0{,}25 ;\ \pm0{,}6)$ du plan, sur le cercle de rayon $0{,}65$, à l'angle $\pm\theta$.

**Erreurs fréquentes.** Prendre $0{,}25$ (la partie réelle) pour le module. Calculer $\theta$ en degrés ($67{,}38°$). Oublier le signe moins de la récurrence ($u_2 = 0{,}125 + 0{,}4225$). Compter 16 en g) ($0{,}65^{16}$ dépasse encore $10^{-3}$).

**Variante.** $u_{k+2} = 0{,}96\,u_{k+1} - 0{,}36\,u_k$ : racines $0{,}48 \pm 0{,}36i$, module $0{,}6$, $\cos\theta = 0{,}8$, période $\frac{2\pi}{0{,}6435} \approx 9{,}76$ pas.

### Ex M19.8 — Une pente estimée sur B points tirés au hasard : espérance et variance de l'estimation

**Réponses.** a) `-1.5` · b) `[0, 4, -4, -6]` · c) `14.75` · d) `7.375` · e) `2.7157` · f) `59` · g) `4.9167` · h) `"3/16"` · i) `"13/6"`.

**Démarche.** En $a = 2$, les résidus $2I_k - U_k$ valent $0$, $1$, $-1$, $-1$ ; $g_k = 2I_k \times$ résidu : $0$, $4$, $-4$, $-6$, de moyenne $F'(2) = -1{,}5$. c) $\frac{0 + 16 + 16 + 36}{4} - 2{,}25 = 14{,}75$. d) $14{,}75/2$. e) $\sqrt{7{,}375} \approx 2{,}7157$. f) $B \ge 14{,}75/0{,}25 = 59$. g) $7{,}375 \times \frac{4 - 2}{4 - 1}$. h) Sur les 16 couples équiprobables, la moyenne est strictement positive pour $(g_2, g_2) = 4$, $(g_1, g_2)$ et $(g_2, g_1)$, qui valent 2 ; $(g_2, g_3)$ et $(g_3, g_2)$ donnent 0. i) $a^\star = \frac{2 + 6 + 10 + 21}{1 + 4 + 4 + 9} = \frac{39}{18}$.

Dans ta copie : $F'(2) < 0$ : $F$ décroît quand $a$ augmente, et le minimum est à droite ($a^\star \approx 2{,}17$). Une estimation positive pousserait $a$ vers la gauche, à l'opposé du minimum : un pas fait dans le mauvais sens. En $a^\star$, $F' = 0$, mais les $g_k(a^\star)$ ne sont pas tous nuls : l'estimation reste aléatoire, de moyenne nulle et de même ordre de dispersion.

**Erreurs fréquentes.** Diviser par $N - 1 = 3$ en c) (ce serait $19{,}67$). Diviser l'erreur type par $B$ au lieu de $\sqrt B$. En g), multiplier par $\frac{N - 1}{N - B}$ au lieu de $\frac{N - B}{N - 1}$. En h), compter les couples non ordonnés.

**Variante.** En $a = 2{,}5$ : $g = (1, 8, 0, 3)$, $F'(2{,}5) = 3 > 0$ (le minimum est à gauche), $\sigma^2 = 18{,}5 - 9 = 9{,}5$, et la variance sur $B = 2$ tirages avec remise vaut $4{,}75$.

### Ex M19.9 — Projeter un même vecteur sur une boule et sur un pavé : deux points, deux directions

**Réponses.** a) `7` · b) `[2.4, -1.2, 0.8]` · c) `[2, -2, 2]` · d) `[4.2, 4.1231]` · e) `0.9073` · f) `True`.

**Démarche.** a) $\sqrt{36 + 9 + 4}$. b) $\frac{2{,}8}{7}\,\mathbf{x} = 0{,}4\,\mathbf{x}$. c) $6 \to 2$, $-3 \to -2$, $2 \to 2$. d) $7 - 2{,}8 = 4{,}2$ et $\lVert(4, -1, 0)\rVert = \sqrt{17} \approx 4{,}1231$. e) $\frac{12 + 6 + 4}{7 \times 2\sqrt3} = \frac{22}{24{,}249} \approx 0{,}9073$, un angle d'environ 25°. f) $(2, -2, 2) = 0{,}5\,(4, -4, 4)$.

Dans ta copie : la projection sur la boule est un multiple positif de $\mathbf{x}$ (cosinus 1). Le pavé ne contient pas b) ($2{,}4 > 2$), et la boule ne contient pas c) ($\lVert(2, -2, 2)\rVert = 2\sqrt3 \approx 3{,}46 > 2{,}8$). La plus petite boule centrée en $\mathbf{0}$ qui contient le pavé a pour rayon la distance à un coin, $2\sqrt3$.

**Erreurs fréquentes.** Couper chaque coordonnée à $\pm2{,}8$ pour la boule (donne $(2{,}8 ;\ -2{,}8 ;\ 2)$, de norme $4{,}4$). Projeter sur le pavé en multipliant tout le vecteur par $2/6$. Donner la distance de b) comme $\lVert\mathbf{x}\rVert$.

**Variante.** $\mathbf{x} = (-4, 4, 2)$, de norme 6 : sur la boule de rayon 3, $(-2, 2, 1)$ ; sur $[-2, 2]^3$, $(-2, 2, 2)$, de cosinus $\frac{20}{6\sqrt{12}} \approx 0{,}9623$ avec $\mathbf{x}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M19.10 — Une itération linéaire de matrice symétrique converge pour tout départ si et seulement si ses valeurs propres sont de module < 1

**Démonstration.**
1. Si $\rho < 1$, aucune valeur propre ne vaut 1. Les valeurs propres de $\mathbf{I} - \mathbf{M}$ sont les $1 - \lambda_i$ (mêmes vecteurs propres), toutes non nulles : $\mathbf{I} - \mathbf{M}$ est inversible (son déterminant est leur produit, M12c), et $(\mathbf{I} - \mathbf{M})\mathbf{x} = \mathbf{c}$ a une unique solution $\mathbf{x}^\star$, l'unique point fixe.
2. $\mathbf{x}_{k+1} - \mathbf{x}^\star = (\mathbf{M}\mathbf{x}_k + \mathbf{c}) - (\mathbf{M}\mathbf{x}^\star + \mathbf{c}) = \mathbf{M}(\mathbf{x}_k - \mathbf{x}^\star)$, donc $\mathbf{e}_{k+1} = \mathbf{M}\mathbf{e}_k$ et, par récurrence, $\mathbf{e}_k = \mathbf{M}^k\mathbf{e}_0$. Les $\mathbf{q}_i$ forment une base orthonormée (théorème spectral, M12c) : $\mathbf{e}_0 = \sum_iy_i\mathbf{q}_i$ avec $y_i = \mathbf{q}_i^\top\mathbf{e}_0$, et $\mathbf{M}^k\mathbf{q}_i = \lambda_i^k\mathbf{q}_i$, d'où $\mathbf{e}_k = \sum_i\lambda_i^ky_i\mathbf{q}_i$ par linéarité.
3. La base étant orthonormée, $\lVert\mathbf{e}_k\rVert^2 = \sum_i\lambda_i^{2k}y_i^2 \le \rho^{2k}\sum_iy_i^2 = \rho^{2k}\lVert\mathbf{e}_0\rVert^2$. Comme $0 \le \rho < 1$, $\rho^k \to 0$ (R5), donc $\mathbf{e}_k \to \mathbf{0}$ et $\mathbf{x}_k \to \mathbf{x}^\star$, quel que soit $\mathbf{x}_0$. Égalité pour tout $k$ quand $\mathbf{e}_0$ n'a de composantes que sur des vecteurs propres de valeur propre $\pm\rho$.
4. Si $\mathbf{x}_k \to \boldsymbol{\ell}$, alors $\mathbf{M}\mathbf{x}_k + \mathbf{c} \to \mathbf{M}\boldsymbol{\ell} + \mathbf{c}$ (un produit par une matrice est continu), et $\mathbf{x}_{k+1} \to \boldsymbol{\ell}$ : $\boldsymbol{\ell} = \mathbf{M}\boldsymbol{\ell} + \mathbf{c}$ est un point fixe. Depuis $\boldsymbol{\ell} + \mathbf{q}_j$, l'écart à $\boldsymbol{\ell}$ vérifie la même récurrence (le calcul du 2. n'utilise que le fait que $\boldsymbol{\ell}$ est un point fixe) et vaut $\mathbf{M}^k\mathbf{q}_j = \lambda_j^k\mathbf{q}_j$, de norme $\lvert\lambda_j\rvert^k$. Par hypothèse, les itérés tendent vers $\boldsymbol{\ell}$, donc cet écart tend vers $\mathbf{0}$ : $\lvert\lambda_j\rvert^k \to 0$, ce qui impose $\lvert\lambda_j\rvert < 1$ (R5), pour chaque $j$. L'hypothèse « un même point » est nécessaire : pour $\mathbf{M} = \mathbf{I}$ et $\mathbf{c} = \mathbf{0}$, chaque départ est un point fixe, la suite est constante et converge, alors que la valeur propre vaut 1.
5. La symétrie a donné une base **orthonormée** de vecteurs propres, qui sert deux fois : pour écrire tout écart sur des vecteurs propres, et pour calculer sa norme par Pythagore au 3. Pour $\mathbf{M} = \begin{pmatrix} 0{,}5 & 10 \\ 0 & 0{,}5 \end{pmatrix}$ (valeurs propres $0{,}5$ et $0{,}5$, $\rho = 0{,}5$), $\mathbf{M}\mathbf{e}_0 = (10 ;\ 0{,}5)$ et $\mathbf{M}^2\mathbf{e}_0 = (10 ;\ 0{,}25)$, de norme environ 10, alors que $\rho^2\lVert\mathbf{e}_0\rVert = 0{,}25$ : la majoration est fausse, l'écart grandit avant de décroître (il tend bien vers 0 : $\mathbf{M}^k = 0{,}5^k\begin{pmatrix} 1 & 20k \\ 0 & 1 \end{pmatrix}$).

**Grille de relecture.** L'unicité du point fixe vient de $1 - \lambda_i \ne 0$. L'écart $\mathbf{e}_k = \mathbf{M}^k\mathbf{e}_0$ est établi, et la décomposition utilise une base orthonormée de vecteurs propres. La norme est calculée par Pythagore, et la majoration par $\rho^k$ conclut. La réciproque passe par un départ décalé d'un vecteur propre, et utilise que la limite est la même pour tous les départs ; le contre-exemple $\mathbf{M} = \mathbf{I}$ est dit. Le rôle de la symétrie est dit, et le contre-exemple montre qu'elle sert pour la majoration.

**Variante.** Pour $\mathbf{M}$ symétrique de valeurs propres $0{,}9$ et $-0{,}3$, la norme de l'écart est au plus $0{,}9^k\lVert\mathbf{e}_0\rVert$, et égale à $0{,}9^k\lVert\mathbf{e}_0\rVert$ depuis un écart le long du vecteur propre de $0{,}9$.

### Ex M19.11 — L'itération de Richardson converge si et seulement si 0 < ω < 2/λmax

**Démonstration.**
1. $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega\mathbf{b} - \omega\mathbf{A}\mathbf{x}_k = (\mathbf{I} - \omega\mathbf{A})\mathbf{x}_k + \omega\mathbf{b}$ : $\mathbf{M} = \mathbf{I} - \omega\mathbf{A}$ et $\mathbf{c} = \omega\mathbf{b}$. Un point fixe vérifie $\mathbf{x} = \mathbf{x} + \omega(\mathbf{b} - \mathbf{A}\mathbf{x})$, soit $\omega(\mathbf{b} - \mathbf{A}\mathbf{x}) = \mathbf{0}$, donc $\mathbf{A}\mathbf{x} = \mathbf{b}$ pour $\omega \ne 0$ ; $\mathbf{A}$ est inversible (ses valeurs propres sont positives), et la solution est unique.
2. $\mathbf{M}^\top = \mathbf{I} - \omega\mathbf{A}^\top = \mathbf{M}$. Si $\mathbf{A}\mathbf{q}_i = \lambda_i\mathbf{q}_i$, $\mathbf{M}\mathbf{q}_i = (1 - \omega\lambda_i)\mathbf{q}_i$ ; les $\mathbf{q}_i$ formant une base, ce sont toutes les valeurs propres de $\mathbf{M}$.
3. $\lvert 1 - \omega\lambda\rvert < 1 \iff -1 < 1 - \omega\lambda < 1 \iff 0 < \omega\lambda < 2$. Par ∂ M19.10, l'itération converge vers un même point, la solution, depuis tout départ si et seulement si $0 < \omega\lambda_i < 2$ pour tout $i$ (pour $\omega = 0$, $\mathbf{M} = \mathbf{I}$ : chaque départ reste en place). Comme les $\lambda_i$ sont positives, $\omega\lambda_i > 0$ équivaut à $\omega > 0$, et $\omega\lambda_i < 2$ pour tout $i$ équivaut à $\omega\lambda_{\max} < 2$. D'où $0 < \omega < 2/\lambda_{\max}$.
4. $\lambda \mapsto 1 - \omega\lambda$ est affine, donc monotone sur $[\lambda_{\min}, \lambda_{\max}]$ : ses valeurs sur cet intervalle sont entre $1 - \omega\lambda_{\min}$ et $1 - \omega\lambda_{\max}$, et son module y est au plus le plus grand des deux modules extrêmes, atteint aux bouts.
5. Pour $\omega = 2/\lambda_{\max}$, $1 - \omega\lambda_{\max} = -1$ : la composante de l'écart le long de ce vecteur propre change de signe à chaque pas sans diminuer ; les itérés oscillent entre deux points, sans converger (les autres composantes, elles, tendent vers 0 si $\lambda_{\min} < \lambda_{\max}$).

**Grille de relecture.** La forme $\mathbf{M}\mathbf{x} + \mathbf{c}$ et le point fixe sont établis. Les valeurs propres de $\mathbf{M}$ sont obtenues avec les mêmes vecteurs propres, et $\mathbf{M}$ est symétrique (pour appliquer ∂ M19.10). La double inégalité est résolue en utilisant $\lambda_i > 0$. Le rôle des deux valeurs propres extrêmes est justifié par la monotonie. Le cas limite est traité.

**Variante.** Pour $\mathbf{A}$ de valeurs propres 2, 5 et 10, le pas critique vaut $0{,}2$, et avec $\omega = 0{,}15$ le facteur est $\max(0{,}7 ;\ 0{,}25 ;\ 0{,}5) = 0{,}7$.

### Ex M19.12 — Une récurrence d'ordre 2 converge si et seulement si ses racines sont de module < 1 : le critère |q| < 1 et |p| < 1 + q

**Démonstration.**
1. Le système $\alpha + \beta = u_0$, $\alpha r_1 + \beta r_2 = u_1$ a pour déterminant $r_2 - r_1 \ne 0$ : il a une unique solution (complexe si les racines le sont ; alors $\beta = \bar\alpha$ quand $u_0$, $u_1$ sont réels). La suite $w_k = \alpha r_1^k + \beta r_2^k$ vérifie la récurrence, car $r_i^{k+2} = r_i^k(p\,r_i - q) = p\,r_i^{k+1} - q\,r_i^k$. Elle a les mêmes deux premiers termes que $(u_k)$ ; par récurrence (chaque terme est fixé par les deux précédents), $u_k = w_k$ pour tout $k$.
2. Si $\lvert r_1\rvert, \lvert r_2\rvert < 1$ : $\lvert u_k\rvert \le \lvert\alpha\rvert\,\lvert r_1\rvert^k + \lvert\beta\rvert\,\lvert r_2\rvert^k \to 0$ (le module est multiplicatif). Réciproquement, le départ $u_0 = 1$, $u_1 = r_1$ donne $(\alpha, \beta) = (1, 0)$ et $u_k = r_1^k$ (pour des racines complexes, prendre la partie réelle de cette suite, $\lvert r\rvert^k\cos k\theta$, qui est une solution réelle et ne tend vers 0 que si $\lvert r\rvert < 1$) ; si toutes les solutions tendent vers 0, $\lvert r_1\rvert < 1$, et de même pour $r_2$. Racine double $r$ : on vérifie que $k\,r^k$ est aussi solution ($r = p/2$ et $q = r^2$ : $p(k + 1)r^{k+1} - q\,k\,r^k = r^{k+2}(2k + 2 - k) = (k + 2)r^{k+2}$), puis $u_k = (\alpha + \beta k)r^k \to 0$ si $\lvert r\rvert < 1$ (car $k\,\lvert r\rvert^k \to 0$), et $u_k = r^k$ (départ $(1, r)$) montre que $\lvert r\rvert < 1$ est nécessaire.
3. Si $p^2 < 4q$, les racines sont conjuguées : $q = r_1r_2 = r\bar r = \lvert r\rvert^2$, donc $\lvert r_1\rvert = \lvert r_2\rvert = \sqrt q$, et la condition s'écrit $q < 1$ (ici $q > p^2/4 \ge 0$). Alors $\lvert p\rvert < 2\sqrt q \le 1 + q$, car $1 + q - 2\sqrt q = (1 - \sqrt q)^2 \ge 0$ : les deux conditions du critère sont vraies.
4. Si $p^2 \ge 4q$, les racines $r_2 \le r_1$ sont réelles. La parabole $P$ est tournée vers le haut et négative ou nulle exactement sur $[r_2, r_1]$. $P(1) > 0$ et $P(-1) > 0$ disent que $1$ et $-1$ sont hors de $[r_2, r_1]$ : l'intervalle des racines est soit entre $-1$ et $1$, soit tout entier d'un côté. Le sommet $\frac p2$, milieu des racines, dans $]-1, 1[$ exclut le second cas. Les deux racines sont donc dans $]-1, 1[$ si et seulement si $P(1) > 0$, $P(-1) > 0$ et $-1 < \frac p2 < 1$. $P(1) = 1 - p + q > 0$ et $P(-1) = 1 + p + q > 0$ s'écrivent ensemble $\lvert p\rvert < 1 + q$. Et si les deux racines sont dans $]-1, 1[$, $\lvert q\rvert = \lvert r_1r_2\rvert < 1$. Réciproquement, $\lvert q\rvert < 1$ et $\lvert p\rvert < 1 + q$ donnent $P(\pm1) > 0$ et $\lvert p\rvert < 2$, soit le sommet dans $]-1, 1[$.
5. Dans les deux cas, les racines sont de module $< 1$ si et seulement si $\lvert q\rvert < 1$ et $\lvert p\rvert < 1 + q$ (au 3., $\lvert q\rvert < 1$ équivaut à $q < 1$ puisque $q > 0$, et la seconde condition est automatique). Dans le plan $(p, q)$ : le triangle ouvert de sommets $(-2, 1)$, $(2, 1)$, $(0, -1)$, coupé par la parabole $q = p^2/4$.

**Grille de relecture.** L'existence et l'unicité de $(\alpha, \beta)$ ; la vérification que les suites géométriques sont solutions ; le sens réciproque par un départ bien choisi ; la racine double traitée. Pour le critère : $q = \lvert r\rvert^2$ dans le cas complexe, et l'inégalité $2\sqrt q \le 1 + q$ ; dans le cas réel, les signes de $P(\pm1)$ et la position du sommet, dans les deux sens. Le dessin.

**Variante.** $(p, q) = (-1{,}2 ;\ 0{,}35)$ : $\lvert q\rvert < 1$ et $1{,}2 < 1{,}35$, les racines $-0{,}7$ et $-0{,}5$ sont dans $]-1, 1[$ ; la suite tend vers 0 en changeant de signe à chaque pas.

### Ex M19.13 — La projection sur une boule est son point le plus proche, et elle garde la direction

**Démonstration.**
1. $\mathbf{x} = (\mathbf{x} - \mathbf{y}) + \mathbf{y}$, donc $\lVert\mathbf{x}\rVert \le \lVert\mathbf{x} - \mathbf{y}\rVert + \lVert\mathbf{y}\rVert \le \lVert\mathbf{x} - \mathbf{y}\rVert + r$, d'où $\lVert\mathbf{x} - \mathbf{y}\rVert \ge \lVert\mathbf{x}\rVert - r > 0$.
2. $\lVert\mathbf{y}^\star\rVert = r$, donc $\mathbf{y}^\star \in B_r$ ; et $\mathbf{x} - \mathbf{y}^\star = \left(1 - \frac{r}{\lVert\mathbf{x}\rVert}\right)\mathbf{x}$, de norme $\lVert\mathbf{x}\rVert - r$ (le facteur est positif) : la borne est atteinte.
3. Si $\lVert\mathbf{x} - \mathbf{y}\rVert = \lVert\mathbf{x}\rVert - r$, les deux inégalités du 1. sont des égalités : $\lVert\mathbf{y}\rVert = r$, et $\lVert(\mathbf{x} - \mathbf{y}) + \mathbf{y}\rVert = \lVert\mathbf{x} - \mathbf{y}\rVert + \lVert\mathbf{y}\rVert$ ; par le cas d'égalité, $\mathbf{x} - \mathbf{y}$ et $\mathbf{y}$ sont des multiples positifs l'un de l'autre ($\mathbf{x} - \mathbf{y} \ne \mathbf{0}$, $\mathbf{y} \ne \mathbf{0}$), donc $\mathbf{y} = t\,\mathbf{x}$ avec $t > 0$, et $\lVert\mathbf{y}\rVert = r$ donne $t = r/\lVert\mathbf{x}\rVert$ : $\mathbf{y} = \mathbf{y}^\star$.
4. Pour $\mathbf{y}$ dans le pavé, chaque terme $(x_i - y_i)^2$ ne dépend que de $y_i \in [-c, c]$ ; la somme est minimale quand chaque terme l'est. La fonction $y_i \mapsto (x_i - y_i)^2$ est minimale sur $[-c, c]$ en $x_i$ si $x_i$ y est, sinon au bord le plus proche (elle décroît puis croît, avec son minimum en $x_i$) : c'est $\min(\max(x_i, -c), c)$.
5. $\mathbf{x}$ est hors du pavé : au moins une coordonnée vérifie $\lvert x_i\rvert > c$. Si $P(\mathbf{x}) = t\,\mathbf{x}$ : une coordonnée coupée donne $c\,\operatorname{signe}(x_i) = t\,x_i$, soit $t = c/\lvert x_i\rvert < 1$ ; toutes les coordonnées coupées ont donc la même valeur absolue $c/t$ ; une coordonnée non coupée donne $x_i = t\,x_i$ avec $t \ne 1$, donc $x_i = 0$. Les coordonnées non nulles sont toutes coupées et ont la même valeur absolue. Réciproquement, si les coordonnées non nulles valent toutes $\pm m$ avec $m > c$, $P(\mathbf{x}) = \frac{c}{m}\,\mathbf{x}$.

**Grille de relecture.** L'inégalité triangulaire appliquée à $\mathbf{x} = (\mathbf{x} - \mathbf{y}) + \mathbf{y}$ ; l'appartenance de $\mathbf{y}^\star$ à la boule et le calcul de sa distance ; l'unicité par le cas d'égalité ; la séparation des coordonnées pour le pavé ; les deux sens de la question 5, avec le cas des coordonnées nulles.

**Variante.** Pour une boule de centre $\mathbf{a}$, la projection est $\mathbf{a} + r\,\frac{\mathbf{x} - \mathbf{a}}{\lVert\mathbf{x} - \mathbf{a}\rVert}$ quand $\lVert\mathbf{x} - \mathbf{a}\rVert > r$ (on se ramène au centre $\mathbf{0}$ en translatant) : pour $\mathbf{a} = (1, 1)$, $r = 4{,}5$ et $\mathbf{x} = (25, 8)$, $\mathbf{x} - \mathbf{a} = (24, 7)$ est de norme 25, et la projection est $\mathbf{a} + 0{,}18\,(24, 7) = (5{,}32 ;\ 2{,}26)$.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M19.14 — Pont : un pas de Richardson est un pas de descente sur ½ xᵀA x − bᵀx

**Réponses.** a) `"B"` · b) `"C"` · c) `"A"` · d) `"A"` · e) `"B"` · f) `"B"` · g) `True`.

**Démarche.** Pour $\mathbf{A}$ symétrique, $\nabla\left(\frac12\mathbf{x}^\top\mathbf{A}\mathbf{x}\right) = \mathbf{A}\mathbf{x}$ et $\nabla(\mathbf{b}^\top\mathbf{x}) = \mathbf{b}$, d'où $\nabla f = \mathbf{A}\mathbf{x} - \mathbf{b}$ et $\nabla^2 f = \mathbf{A}$. Le résidu est $-\nabla f$, et le pas de Richardson est $\mathbf{x} - \omega\nabla f(\mathbf{x})$ : une descente de gradient de pas $\omega$, le learning rate de workbookIA. Le pas critique est celui de Richardson, $2/\lambda_{\max}$. g) $f$ est strictement convexe (sa hessienne $\mathbf{A}$ est définie positive), et son unique point critique, $\nabla f = \mathbf{0}$, est la solution (M12c §7).

Dans ta copie : pour les ressorts, $f$ est l'énergie élastique moins le travail des forces ; son minimum est l'équilibre. Le gradient est perpendiculaire aux lignes de niveau (M05b), et le résidu est son opposé : il l'est aussi. « Symétrique définie positive » garantit que $f$ est strictement convexe, donc un unique minimum.

**Erreurs fréquentes.** Oublier le $\frac12$ et prendre $2\mathbf{A}$ pour hessienne. Confondre le résidu et le gradient (même direction, signes contraires).

**Variante.** $f(\mathbf{x}) = \frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x} + 7$ a le même gradient, la même hessienne et le même minimum (une constante ne change que la valeur de $f$).

### Ex M19.15 — Pont : le préconditionnement diagonal

**Réponses.** a) `[16.063, 0.187]` · b) `86.0` · c) `[[1, 0.5], [0.5, 1]]` · d) `3` · e) `[595, 20]` · f) `[2, 1]`.

**Démarche.** a) $\lambda^2 - 16{,}25\lambda + 3 = 0$ : $\lambda_{\max} = \frac{16{,}25 + \sqrt{252{,}0625}}{2} \approx 16{,}06324$, puis $\lambda_{\min} = \frac{3}{\lambda_{\max}} \approx 0{,}186762$ (par la différence des deux termes, on perdrait des chiffres). b) $16{,}06324/0{,}186762 \approx 86{,}01$. c) $\frac{1}{\sqrt{16 \times 0{,}25}} = 0{,}5$. d) $\tilde{\mathbf{A}}$ a pour valeurs propres $1{,}5$ et $0{,}5$. e) $\rho^\star = \frac{85{,}009}{87{,}009} \approx 0{,}977014$ et $\frac{13{,}8155}{0{,}023254} \approx 594{,}1$, donc 595 ; puis $\rho^\star = \frac12$ et $\frac{13{,}8155}{0{,}6931} \approx 19{,}9$, donc 20. f) $(4 \times 0{,}5 ;\ 0{,}5 \times 2)$.

Dans ta copie : sur $\tilde{\mathbf{A}}$, $\mathbf{y} \leftarrow \mathbf{y} + \omega\,\mathbf{D}^{-1/2}(\mathbf{b} - \mathbf{A}\mathbf{x})$, et, avec $\mathbf{x} = \mathbf{D}^{-1/2}\mathbf{y}$, $\mathbf{x} \leftarrow \mathbf{x} + \omega\,\mathbf{D}^{-1}(\mathbf{b} - \mathbf{A}\mathbf{x})$ : la coordonnée $i$ du résidu est divisée par $a_{ii}$. Pour $\begin{pmatrix} 1 & 0{,}9 \\ 0{,}9 & 1 \end{pmatrix}$, la diagonale vaut déjà 1 : $\mathbf{D} = \mathbf{I}$, la mise à l'échelle ne change rien, et $\kappa = \frac{1{,}9}{0{,}1} = 19$ reste. Le mauvais conditionnement vient ici du couplage : les vecteurs propres $(1, 1)$ et $(1, -1)$ sont à 45° des axes, et une mise à l'échelle des inconnues, qui étire les axes sans les tourner, ne peut pas les redresser. En une phrase : une mise à l'échelle diagonale corrige les différences d'échelle entre les inconnues, pas les couplages entre elles.

**Erreurs fréquentes.** Diviser par $a_{ii}$ au lieu de $\sqrt{a_{ii}a_{jj}}$ pour $\tilde a_{ij}$ (on obtiendrait une matrice non symétrique). Calculer $\lambda_{\min}$ par la différence $\frac{16{,}25 - 15{,}8765}{2}$ avec trop peu de chiffres. Arrondir $\rho^\star$ à $0{,}9770$ (on trouverait 594) : garde 6 chiffres significatifs.

**Variante.** $\mathbf{A} = \begin{pmatrix} 9 & 0{,}6 \\ 0{,}6 & 1 \end{pmatrix}$ : $\kappa \approx 9{,}47$ ; $\tilde{\mathbf{A}} = \begin{pmatrix} 1 & 0{,}2 \\ 0{,}2 & 1 \end{pmatrix}$, $\kappa = 1{,}5$.

### Ex M19.16 — MML §5.7 et §5.8

**Ce qu'il faut avoir relevé.**
1. MML écrit $\frac{\partial^2 f}{\partial x^2}$ pour la dérivée seconde par rapport à $x$, et $\frac{\partial^2 f}{\partial y\,\partial x}$ pour la dérivée par rapport à $x$, puis par rapport à $y$ (lis bien l'ordre). La hessienne est notée $\nabla^2_{x,y}f(x, y)$ ou $\mathbf{H}$ ; elle est symétrique quand $f$ est deux fois continûment dérivable (Schwarz).
2. Pour $f : \mathbb{R}^n \to \mathbb{R}^m$, la hessienne est un tableau à trois indices, de forme $(m, n, n)$ : une hessienne par sortie. La fiche se limite à une sortie réelle, le cas de l'optimisation et des points critiques.
3. Le terme d'ordre $k$ est $\frac{1}{k!}D^k_{\mathbf{x}}f(\mathbf{x}_0)\,\boldsymbol{\delta}^k$, où $D^k_{\mathbf{x}}f$ est le tableau à $k$ indices des dérivées $k$-ièmes, $\boldsymbol{\delta} = \mathbf{x} - \mathbf{x}_0$, et le produit somme sur tous les indices. Pour $k = 1$ : $\nabla f(\mathbf{x}_0)^\top\boldsymbol{\delta}$ ; pour $k = 2$ : $\frac12\boldsymbol{\delta}^\top\mathbf{H}\boldsymbol{\delta}$, les termes de la fiche avec $\mathbf{h} = \boldsymbol{\delta}$.
4. L'exemple de la fin du §5.8 développe un polynôme de degré 3 en deux variables : jusqu'à l'ordre 3, la série redonne exactement le polynôme. Refait à l'ordre 2 en ton point, ton gradient et ta hessienne doivent coïncider avec `numerical_hessian` à $10^{-6}$ près.
5. Par exemple : *Hessian* (hessienne), *Taylor polynomial* (polynôme de Taylor), *Taylor series* (série de Taylor), *partial derivative* (dérivée partielle), *tensor* (tableau à plusieurs indices).

**Grille.** Les notations et l'ordre des dérivations ; la forme $(m, n, n)$ ; les termes d'ordre 1 et 2 traduits ; l'exemple refait et vérifié ; trois mots traduits.

### Ex M19.17 — MML §7.1

**Ce qu'il faut avoir relevé.**
1. MML note le pas $\gamma$ (*step-size*). Trop petit, la descente est lente ; trop grand, elle dépasse le minimum, oscille ou diverge.
2. Pour la matrice de l'exemple (diagonale 2 et 20, coefficient hors diagonale 1), $\lambda^2 - 22\lambda + 39 = 0$ donne $11 \pm \sqrt{82}$, soit environ $1{,}94$ et $20{,}06$ : $\kappa \approx 10{,}3$ et le pas critique vaut $2/20{,}06 \approx 0{,}0997$. Le pas choisi par MML est en dessous, mais assez près pour que la composante raide soit multipliée par un nombre négatif proche de $-0{,}7$ : les itérés zigzaguent, comme sur sa figure.
3. La remarque relie la lenteur au conditionnement (le rapport des valeurs singulières extrêmes) : sur des lignes de niveau très allongées, le gradient pointe presque en travers, vers l'axe court. Le remède proposé est un **préconditionneur** : résoudre un système équivalent dont la matrice est mieux conditionnée, et facile à calculer. La mise à l'échelle diagonale du §5 en est le cas le plus simple.
4. La mise à jour avec momentum garde en mémoire le déplacement précédent, $\mathbf{x}_i - \mathbf{x}_{i-1}$, et en ajoute un multiple au pas ; workbookIA 19 étudie cette méthode.
5. La fonction est une somme (ou une moyenne) de termes, un par donnée ; le gradient calculé sur une partie tirée au hasard a pour espérance le vrai gradient (linéarité de l'espérance), comme au §7 de la fiche.
6. Par exemple : *step-size* (pas), *condition number* (conditionnement), *preconditioner* (préconditionneur), *momentum*, *stochastic gradient descent* (descente de gradient stochastique), *mini-batch*.

**Grille.** Le pas et ses deux défauts ; les valeurs propres, le conditionnement et le pas critique de l'exemple ; le préconditionneur relié au §5 ; ce que garde le momentum, sans l'étudier ; l'estimation sans biais reliée au §7 ; trois mots traduits.

### Ex M19.18 — Expliquer, sur un dessin de lignes de niveau, pourquoi un système mal conditionné converge lentement

**Réponse modèle (6 à 10 phrases).** L'équilibre de ta structure est le point où son énergie est la plus basse, et chaque itération corrige la position des poutres dans la direction du résidu, ce qui reste de déséquilibre. Les courbes d'énergie constante sont des ellipses. Si toutes les poutres ont des raideurs voisines, ce sont presque des cercles : le résidu pointe vers l'équilibre, et quelques itérations suffisent. Si certaines sont bien plus raides que d'autres, les ellipses deviennent très allongées, cinquante fois plus raides dans une direction que dans l'autre pour un conditionnement de 50. Le résidu est perpendiculaire aux courbes : il pointe surtout en travers des ellipses, et presque pas vers le centre. La correction ne peut pas dépasser une taille fixée par la direction la plus raide, sinon chaque itération repart plus loin de l'autre côté. Avec cette petite correction, la direction la plus souple n'avance presque pas à chaque itération. Le nombre d'itérations grandit donc comme l'allongement, mesuré par le conditionnement : cent fois plus allongé, cent fois plus d'itérations. Si le déséquilibre vient seulement des unités ou des échelles des inconnues, les remettre à l'échelle rend les ellipses presque circulaires, et la convergence redevient rapide.

**En 3 phrases.** Un système mal conditionné a des courbes d'énergie très allongées, et le résidu y pointe surtout en travers. La correction est limitée par la direction la plus raide, si bien que la direction la plus souple avance très lentement. Remettre les inconnues à l'échelle peut rendre les courbes presque circulaires et accélérer beaucoup la méthode.

**Grille.** Les deux dessins ; le résidu perpendiculaire aux lignes ; la correction limitée par la direction raide ; la lenteur le long de l'axe long ; la croissance avec le conditionnement ; la mise à l'échelle.

<a id="entretien"></a>

## 💼 Entretien

### M19.E1 — « Que nous apprend la hessienne en un minimum ? »

**Réponse modèle (60 secondes).** « La hessienne est la matrice des dérivées secondes d'une fonction de plusieurs variables ; elle est symétrique. Elle décrit la courbure : le développement de Taylor d'ordre 2 ajoute à l'approximation linéaire un terme un demi de h transposé H h, et la courbure dans une direction unitaire u vaut u transposé H u. En un point où le gradient s'annule, ses valeurs propres disent la nature du point : toutes positives, c'est un minimum local ; toutes négatives, un maximum ; de signes mélangés, un point selle ; une valeur propre nulle, et il faut regarder plus loin. En un minimum, elle dit aussi la forme du creux : les lignes de niveau y ressemblent à des ellipses, d'axes les vecteurs propres et de demi-axes proportionnels à un sur racine de lambda ; le rapport de la plus grande à la plus petite valeur propre mesure leur allongement. Enfin, elle a n au carré coefficients : en très grande dimension, on ne la forme jamais, on en calcule des produits avec des vecteurs, ou on l'approche. »

**Grille.** Définition et symétrie ; courbure et Taylor ; le test par les valeurs propres ; la forme des lignes de niveau autour du minimum ; le coût en $n^2$.

### M19.E2 — « Pourquoi un mauvais conditionnement ralentit-il une méthode itérative ? »

**Réponse modèle (60 secondes).** « Pour une matrice symétrique définie positive, le conditionnement est le rapport de la plus grande à la plus petite valeur propre. Une méthode comme Richardson, ou une descente de gradient sur une forme quadratique, multiplie l'erreur dans chaque direction propre par un facteur un moins le pas fois la valeur propre. Pour ne pas diverger, le pas doit rester sous deux sur lambda max ; avec ce pas, la direction de la plus petite valeur propre ne gagne qu'un facteur proche de un moins un sur kappa par itération. Le nombre d'itérations pour une précision donnée grandit donc comme le conditionnement, et seulement comme sa racine avec le gradient conjugué. Multiplier la matrice par un nombre ou tourner les inconnues ne change rien ; changer l'échelle des inconnues, préconditionner, peut tout changer. Par exemple, une simulation de chaleur sur un maillage de plus en plus fin a un conditionnement qui grandit avec la finesse du maillage, et c'est le préconditionneur qui la rend praticable. »

**Grille.** La définition ; le pas limité par $\lambda_{\max}$ ; la lenteur dans la direction de $\lambda_{\min}$ ; $\kappa$ contre $\sqrt\kappa$ ; les invariances ; le préconditionnement ; un exemple hors apprentissage automatique.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **M19.19 🔨** `numerical_hessian` : la dérivée seconde centrée sur la diagonale, la formule à quatre points ailleurs, chaque case calculée une fois puis recopiée, d'où une symétrie exacte. a) La hessienne numérique de $g(x, y) = \frac{x^2}{1 + y^2} + \cos(xy)$ en $(1{,}2 ;\ -0{,}5)$ vaut $\begin{pmatrix} 1{,}3937 & 2{,}5958 \\ 2{,}5958 & -1{,}5571 \end{pmatrix}$, à $3 \cdot 10^{-8}$ près de la hessienne exacte de SymPy. b) La hessienne de $s(x, y, z) = \cosh x + \cos y + xz + z^2$ en $\mathbf{0}$ a pour valeurs propres $-1$, $\frac{3 - \sqrt5}{2} \approx 0{,}3820$ et $\frac{3 + \sqrt5}{2} \approx 2{,}6180$ : c) indice 1, d) un point selle (C), où $s$ descend le long de l'axe des $y$. e) L'écart à la hessienne exacte vaut $2{,}1 \cdot 10^{-4}$, $2{,}1 \cdot 10^{-6}$, $3{,}4 \cdot 10^{-8}$, $3{,}1 \cdot 10^{-6}$, $1{,}1 \cdot 10^{-4}$, $1{,}9 \cdot 10^{-2}$ et $2{,}9$ pour $h = 10^{-2}, \ldots, 10^{-8}$ : le meilleur pas est $10^{-4}$ ($k = 4$), plus grand que le $10^{-5}$ d'une dérivée première, car les arrondis sont divisés par $h^2$.
- **M19.20 🔨** `critical_step_size` et `richardson_iterates`. a) Le pas critique du ressort raide et du ressort souple vaut $\frac{2}{\lambda_{\max}} \approx 0{,}019967$ ($\lambda_{\max} \approx 100{,}166$) ; b) après la mise à l'échelle diagonale, $\frac{2}{1{,}2} = \frac53$, environ 83 fois plus grand. c) Pour les deux ressorts avec le pas de la fiche $\omega = 0{,}32$, depuis $\mathbf{0}$, $\frac{\lVert\mathbf{e}_{61}\rVert}{\lVert\mathbf{e}_{60}\rVert} = 0{,}9200 = \rho(0{,}32)$, le module du facteur $-0{,}92$ de la valeur propre 6. Au début, le rapport est proche de l'autre facteur, $0{,}68$ : $\frac{\lVert\mathbf{e}_3\rVert}{\lVert\mathbf{e}_2\rVert} \approx 0{,}694$, car l'écart de départ est huit fois plus grand sur le vecteur propre $(1, 2)$ ; la composante raide l'emporte dès le 7ᵉ pas. d) Au meilleur pas $\frac27$, 42 itérations, comme dans la fiche : le rapport de deux écarts successifs vaut exactement $\frac57$ à chaque pas, depuis tout départ.
- **M19.21 🔨** `linear_recurrence` : $c_1$ multiplie le terme le plus récent, et $u_{k+2} = p\,u_{k+1} - q\,u_k$ s'écrit `[p, -q]`. a) Pour l'exemple de la fiche, $u_9 = -0{,}8^9 \approx -0{,}134218$ ; b) vrai : les termes suivent $0{,}8^k\cos\frac{k\pi}{3}$ à $2 \cdot 10^{-16}$ près. c) Pour $u_{k+3} = 0{,}5\,u_{k+2} + 0{,}3\,u_{k+1} + 0{,}2\,u_k$ depuis $(0, 10, 4)$, $u_{11} \approx 5{,}292669$. La racine 1 et deux racines complexes de module $\sqrt{0{,}2}$ ; la quantité $u_{k+2} + 0{,}5\,u_{k+1} + 0{,}2\,u_k = 9$ ne change pas, d'où la limite $\frac{9}{1{,}7} = \frac{90}{17} \approx 5{,}294118$ : $u_{11}$ en est encore à $1{,}4 \cdot 10^{-3}$, et l'écart est multiplié par $0{,}45$ environ par rang ($10^{-13}$ au rang 40).
- **M19.22 📦** Pour la barre de 50 points intérieurs, bouts à 10 °C et 70 °C, a) `scipy.sparse.linalg.cg` atteint le résidu relatif $10^{-8}$ en 50 itérations, $n$, et trouve le profil linéaire à $6 \cdot 10^{-14}$ près ; b) Richardson au meilleur pas $\omega^\star = \frac12$ (la méthode de Jacobi, la diagonale valant 2) en demande 7 565, contre $1{,}15\,\kappa\,d \approx 9\,700$ pour le pire départ ; c) $\kappa \approx 1\,053{,}5$, et $\sqrt\kappa \approx 32{,}5$. La matrice creuse ne stocke que 148 coefficients sur 2 500.
- **M19.23 🔮** Pour la matrice de valeurs propres 2, 5, 11 et 24, le pas critique vaut $\frac{1}{12} \approx 0{,}0833$ : a) le pas (C), $\omega = 0{,}0875$, est au-dessus et ne converge pas ($1 - 24\omega = -1{,}1$ ; l'écart est multiplié par $6 \cdot 10^{61}$ en 1 500 pas). La formule $\left\lceil\frac{6\ln 10}{-\ln\rho}\right\rceil$ donne b) 201 itérations pour (A), $\omega = \frac{1}{30}$, $\rho = \frac{14}{15}$ (c'est $\lambda_{\min}$ qui décide) ; c) 83 pour (B), le meilleur pas $\frac{1}{13}$, $\rho = \frac{11}{13}$ ; d) 684 pour (D), $\omega = 0{,}0825$, $\rho = 0{,}98$ (c'est $\lambda_{\max}$ qui décide). L'expérience compte 191, 81 et 650 itérations : un peu moins que la formule, car l'écart de départ n'a que la moitié de sa norme sur la direction la plus lente. (D) demande $\frac{684}{83} \approx 8{,}2$ fois plus d'itérations que (B), bien que son pas soit plus grand.
- **M19.24 🔬** Pour huit barres de 2 à 50 points intérieurs, $\kappa$ va de 3 à $1\,053{,}5$. Richardson au meilleur pas ($\frac12$ pour toutes) fait 20, 40, 91, 199, 466, 987, 2 294 puis a) 5 139 itérations jusqu'au résidu relatif $10^{-6}$ ; le gradient conjugué en fait exactement $n$ : 2, 3, 5… 50. b) La pente de Richardson, en échelles logarithmiques, vaut $0{,}94$, soit 1 au demi près : un compte proportionnel à $\kappa$ ; c) celle du gradient conjugué, $0{,}55$, soit $\frac12$ : un compte proportionnel à $\sqrt\kappa$, puisque $\kappa \approx \frac{4(n + 1)^2}{\pi^2}$.
- **M19.25 🎨** Pour $\mathbf{A} = \begin{pmatrix} 10 & 6 \\ 6 & 5 \end{pmatrix}$ ($\kappa = 14$), les facteurs $(1 - 14\omega ;\ 1 - \omega)$ des directions $(3, 2)$ et $(2, -3)$ valent $(0{,}2 ;\ 0{,}943)$ pour $0{,}4\,\omega_c$ (la composante raide diminue vite, sans changer de signe), $(-\frac{13}{15} ;\ \frac{13}{15})$ au meilleur pas, et $(-0{,}9 ;\ 0{,}864)$ pour $0{,}95\,\omega_c$ : la composante raide change de signe à chaque pas et diminue à peine, et les itérés passent de part et d'autre de l'axe long à chaque pas. Pour $0 < \omega < \omega_c$, le facteur de l'axe long, $1 - \omega\lambda_{\min}$, reste au-dessus de $1 - \frac{2}{\kappa} = \frac67 \approx 0{,}857$ : c'est le conditionnement qui borne la vitesse.
- **M19.26 🐛** (1) `eigvalsh` rend les valeurs propres en ordre croissant : `[0]` est $\lambda_{\min}$. Sur $4\mathbf{I}$, toutes sont égales, et l'erreur ne se voit pas ; pour les trois masses, de valeurs propres $1{,}3687$ ; $4{,}9038$ ; $10{,}7275$, le pas du collègue vaut $\frac{1}{\lambda_{\min}} \approx 0{,}7306$, près de quatre fois le pas critique $0{,}1864$ : a) $\rho = \frac{\lambda_{\max}}{\lambda_{\min}} - 1 \approx 6{,}8379$, et $\lVert\mathbf{x}_{30}\rVert \approx 2 \cdot 10^{24}$. (2) `eigvalsh` lit le triangle inférieur, vide chez le collègue : elle voit $\operatorname{diag}(2, 2, 2)$, et `inertia_26` rend $(0, 0, 3)$, celle d'un minimum ; avec la hessienne recopiée en dessous, l'inertie devient $(1, 0, 2)$ (valeurs propres $2 - \sqrt{10}$, 2 et $2 + \sqrt{10}$) : b) un point selle (C). Sur $\cos x + y^2 + z^2$, la hessienne est diagonale : aucun triangle ne manque. (3) Le module de deux racines conjuguées est $\sqrt q$ : c) pour $(p, q) = (1 ;\ 1{,}2)$, $\sqrt{1{,}2} \approx 1{,}0954 > 1$, et la suite diverge en oscillant ($\lvert u_{60}\rvert \approx 254$ depuis $(1, 0)$), là où le collègue lit $\frac{\lvert p\rvert}{2} = 0{,}5$. Les trois récurrences de la fiche ne pouvaient pas le démasquer : il faut $q > 1$ et $\lvert p\rvert < 2$.
- **M19.27 🛠️** `solve_richardson` suit le résidu par sa propre récurrence, $\mathbf{r}_{k+1} = (\mathbf{I} - \omega\mathbf{A})\,\mathbf{r}_k$, $\mathbf{r}_0 = \mathbf{b}$ : un seul produit par $\mathbf{A}$ par itération. Pour les quatre masses ($\kappa \approx 8{,}06$), la solution $(\frac{7}{19} ;\ \frac{9}{19} ;\ \frac{10}{19} ;\ \frac{12}{19})$ est atteinte en 130 itérations avec $\omega = \frac{1}{\lambda_{\max}}$ (la borne $\lVert\mathbf{r}_k\rVert \le \rho^k\lVert\mathbf{b}\rVert$, avec $\rho = 1 - \frac1\kappa$, en promet au plus 140 ; 43 pour `tol=1e-3`), en 70 au meilleur pas ; avec $1{,}2\,\omega_c$, le résidu relatif dépasse $10^{10}$ après 74 itérations, et la fonction s'arrête sans overflow ; avec `omega=np.nan`, elle s'arrête après 1 pas, le résidu n'étant plus fini. L'erreur relative sur $\mathbf{x}$ est au plus $\kappa$ fois le résidu relatif : $8 \cdot 10^{-8}$ garantis pour `tol=1e-8`, $3 \cdot 10^{-8}$ mesurés.
- **M19.28 🏆** Le schéma saute-mouton a $q = 1$ : ses racines sont complexes de module 1 tant que $0 < h\Omega < 2$, d'où a) $h_c = \frac{2}{\Omega} = 0{,}4$ s. b) Sur 300 pas, l'amplitude reste entre $0{,}30$ m et $0{,}69$ m jusqu'à $h = 0{,}36$ s, le plus grand pas borné de la grille ; en $h_c$, la racine double $-1$ donne $x_k = -h\,v_0\,k\,(-1)^k$, une croissance linéaire (180 m au 300ᵉ pas), et au-delà une racine réelle de module $> 1$ ($10^{115}$ dès $h = 0{,}44$ s). c) Pour $h = 0{,}03$ s, la période du schéma vaut $\frac{2\pi}{\theta} \approx 41{,}85$ pas, un peu moins que $\frac{2\pi}{h\Omega} \approx 41{,}89$ ; la simulation mesure $41{,}85$. d) En $h_c$, $\lvert x_{1000}\rvert = 1\,000\,h_c\,v_0 = 600$ m. Les racines étant de module exactement 1, le schéma n'amortit pas l'oscillation ; pour simuler fidèlement, on garde un pas bien plus petit que $h_c$.
