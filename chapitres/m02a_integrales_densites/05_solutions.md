# M02a · Intégrales et densités — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M02a.Q1 — Aire, signe et intégrale
1. **Vrai** : les rectangles des sommes de Riemann ont tous une hauteur positive, et leur limite est l'aire.
2. **0** : $x^3$ est négative sur $[-1 ; 0]$ et positive sur $[0 ; 1]$, et les deux régions sont symétriques par rapport à l'origine : leurs aires se compensent. Par le calcul, $\left[\frac{x^4}{4}\right]_{-1}^1 = \frac{1}{4} - \frac{1}{4} = 0$.
3. **Négatif** (strictement) : chaque rectangle a une « hauteur » négative. Si $f$ est seulement négative ou nulle, l'intégrale est négative ou nulle.
4. **0** : l'intervalle est de largeur nulle.
5. **Vrai** : inverser les bornes change le signe (le pas $h = \frac{b - a}{n}$ change de signe).
6. **Trop petite** : sur chaque intervalle, la valeur à gauche est la plus petite ; chaque rectangle est sous la courbe.

### M02a.Q2 — Primitives : vrai ou faux
1. **Vrai** : la dérivée de $\frac{x^3}{3} + 7$ vaut $x^2$ (la constante disparaît).
2. **Faux** : la dérivée de $e^{2x}$ vaut $2e^{2x}$ ; une primitive est $\frac{e^{2x}}{2}$.
3. **Vrai**.
4. **Faux** : $\frac{x^0}{0}$ n'a pas de sens ; la formule de $x^n$ exclut $n = -1$, et une primitive de $\frac{1}{x}$ est $\ln \lvert x \rvert$.
5. **Vrai** : sur un intervalle, une fonction de dérivée nulle est constante.
6. **Vrai** : par la règle de la chaîne, la dérivée de $\sin(x^2)$ vaut $\cos(x^2) \times 2x$.

### M02a.Q3 — Quelle méthode de calcul pour quelle intégrale ?
1. (T) : $x^3 - 4\ln \lvert x \rvert$.
2. (P) : $u = \ln x$ (qui se simplifie en dérivant), $v' = x$.
3. (C) : $u = x^2 + 1$, $du = 2x\,dx$ ; on obtient $\ln(x^2 + 1)$.
4. (P) : $u = x$, $v' = e^{3x}$.
5. (C) : $u = 1 + e^x$, $du = e^x\,dx$ ; on obtient $\ln(1 + e^x)$.
6. (T) en développant $(x + 1)^2 = x^2 + 2x + 1$, de primitive $\frac{x^3}{3} + x^2 + x$, ou (C) avec $u = x + 1$ : $\frac{(x + 1)^3}{3}$. Les deux résultats diffèrent d'une constante ($\frac{1}{3}$).

### M02a.Q4 — Converge ou diverge ?
1. **Converge** : $p = 3 > 1$ (elle vaut $\frac{1}{2}$).
2. **Diverge** : $\frac{1}{\sqrt{x}} = x^{-1/2}$, et $p = \frac{1}{2} \le 1$ vers $+\infty$.
3. **Diverge** : près de 0, il faut $p < 1$, et ici $p = 2$.
4. **Converge** : elle vaut $\frac{1}{3}$.
5. **Converge** : $p = \frac{1}{3} < 1$ près de 0 (elle vaut $\frac{3}{2}$).
6. **Converge** : c'est l'intégrale de Gauss, $\sqrt{\pi}$.

### M02a.Q5 — Rectangles, trapèzes, Simpson
1. Les trapèzes, le point milieu et Simpson (avec un nombre pair d'intervalles) ; les rectangles à gauche ou à droite ne sont exacts que pour les constantes.
2. $n$ doit être **pair** : les intervalles vont par deux, sous une parabole.
3. Par **4** (erreur en $h^2$).
4. **11** : les points $x_0, \ldots, x_{10}$.
5. **Faux** : c'est vrai pour une fonction croissante ; pour une fonction décroissante, ils la sous-estiment.
6. Jusqu'au **degré 3**.

### M02a.Q6 — Densité et probabilité : vrai ou faux
1. **Faux** : une densité est positive ou nulle.
2. **Faux** : $P(X = 1) = 0$ ; $f(1)$ est une probabilité par unité de longueur.
3. **Vrai** : $P(X = 2) = 0$.
4. **Vrai** : elle est positive et son aire vaut $5 \times 0{,}2 = 1$. Une densité peut dépasser 1.
5. **Faux** : l'aire de $2f$ vaut 2.
6. **Vrai** : l'aire d'un rectangle étroit de largeur $h$ et de hauteur presque $f(x)$.

### M02a.Q7 — Lire une fonction de répartition
1. $F(1) = \frac{1}{4}$.
2. $1 - F(1) = \frac{3}{4}$.
3. $F(2) - F(1) = 1 - \frac{1}{4} = \frac{3}{4}$.
4. $\frac{m^2}{4} = \frac{1}{2}$, donc $m = \sqrt{2} \approx 1{,}414$.
5. $F'(x) = \frac{x}{2}$ (et l'on vérifie que $\int_0^2 \frac{x}{2}\,dx = 1$).
6. **Faux** : $F(x) = P(X \le x)$ ne peut que croître quand $x$ augmente.

<a id="rappels"></a>

## 🔁 Rappels

### M02a.R1 — Dériver une composée (R7)
1. $4(3 - x^2)^3 \times (-2x) = -8x(3 - x^2)^3$.
2. $\frac{-2}{5 - 2x}$, soit $\frac{2}{2x - 5}$.
3. $5e^{5x - 1}$.
4. $\frac{2x}{2\sqrt{1 + x^2}} = \frac{x}{\sqrt{1 + x^2}}$.

### M02a.R2 — Sommes Σ (R4)
1. $1 + 4 + 9 + 16 = 30$.
2. $1 + 4 + 7 + 10 = 22$.
3. $0{,}5\sum_{i=0}^{3} f(0{,}5\,i)$ : une somme de Riemann à gauche, avec $h = 0{,}5$.
4. $\frac{20 \times 21}{2} = 210$.

### M02a.R3 — Exponentielle et logarithme (R6)
1. 0.
2. 0 : l'exponentielle l'emporte sur toute puissance (croissances comparées).
3. 5 et $-2$.
4. $-2x = \ln\frac{1}{4} = -2\ln 2$, donc $x = \ln 2 \approx 0{,}693$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M02a.1 — Sommes de Riemann à la main : rectangles à gauche, à droite, au milieu

**Réponses** : a) `0.5` · b) `6.25` · c) `4.25` · d) `5.375` · e) `2` · f) `5.8125` · g) `80` · h) `True`.

**Démarche.**
- a) $h = \frac{2 - 0}{4} = 0{,}5$ ; les points sont $0$ ; $0{,}5$ ; $1$ ; $1{,}5$ ; $2$, où $f$ vaut $4$ ; $3{,}75$ ; $3$ ; $1{,}75$ ; $0$.
- b) $L_4 = 0{,}5 \times (4 + 3{,}75 + 3 + 1{,}75) = 0{,}5 \times 12{,}5 = 6{,}25$.
- c) $R_4 = 0{,}5 \times (3{,}75 + 3 + 1{,}75 + 0) = 0{,}5 \times 8{,}5 = 4{,}25$.
- d) Aux milieux $0{,}25$ ; $0{,}75$ ; $1{,}25$ ; $1{,}75$ : $f = 3{,}9375$ ; $3{,}4375$ ; $2{,}4375$ ; $0{,}9375$, de somme $10{,}75$, d'où $M_4 = 5{,}375$.
- e) $6{,}25 - 4{,}25 = 2$.
- f) $h = 0{,}25$ ; les huit hauteurs à gauche ($x = 0$ à $1{,}75$) somment à $23{,}25$, d'où $L_8 = 5{,}8125$.
- g) Les deux sommes ont les mêmes termes, sauf le premier de $L_n$ ($h\,f(0)$) et le dernier de $R_n$ ($h\,f(2)$) : $L_n - R_n = h\big(f(0) - f(2)\big) = \frac{2}{n} \times 4 = \frac{8}{n}$. Puis $\frac{8}{n} \le 0{,}1 \iff n \ge 80$.
- h) $f$ décroît : les rectangles à gauche dépassent la courbe, ceux de droite sont dessous. L'aire exacte, $\frac{16}{3} \approx 5{,}333$, est bien entre 4,25 et 6,25.

**Erreurs fréquentes.** Oublier de multiplier par $h$ (12,5 et 8,5) ; inverser gauche et droite ; en g, prendre $h = \frac{1}{n}$ (on trouve alors 40).

**Variante.** $M_2$ pour la même fonction ? *Réponse* : $h = 1$, milieux $0{,}5$ et $1{,}5$, $M_2 = 3{,}75 + 1{,}75 = 5{,}5$.

### Ex M02a.2 — Primitives usuelles

**Réponses** (à une constante près) : a) `"2*x**3 - 2*x**2 + 5*x"` · b) `"-1/(2*x**2)"` · c) `"2*x**(3/2)/3"` · d) `"exp(3*x)/3"` · e) `"ln(2*x + 1)/2"` · f) `"sin(2*x)/2"` · g) `"x**3 + x - 2"` · h) `"4*ln(x) - exp(-x)"`.

**Démarche.**
- a) Terme à terme : $6 \times \frac{x^3}{3} - 4 \times \frac{x^2}{2} + 5x$.
- b) $x^{-3} \to \frac{x^{-2}}{-2} = -\frac{1}{2x^2}$.
- c) $x^{1/2} \to \frac{x^{3/2}}{3/2} = \frac{2}{3}x^{3/2}$ (soit $\frac{2}{3}x\sqrt{x}$).
- d) et f) La règle $f(ax + b) \to \frac{1}{a}F(ax + b)$ : on divise par 3, puis par 2.
- e) $\frac{1}{2x + 1}$ est $\frac{1}{u}$ avec $u = 2x + 1$ : $\frac{1}{2}\ln(2x + 1)$ (positif sur l'intervalle donné, d'où l'absence de valeur absolue).
- g) Les primitives sont $x^3 + x + C$ ; $F(1) = 2 + C = 0$ donne $C = -2$.
- h) $4\ln x$ et $-e^{-x}$ (la dérivée de $-e^{-x}$ vaut $e^{-x}$).

Vérifie chacune en la dérivant : c'est rapide, et c'est le seul contrôle sûr.

**Erreurs fréquentes.** Donner la dérivée au lieu d'une primitive ; diviser par l'ancien exposant ; oublier le facteur $\frac{1}{a}$ en d, e, f ; un signe en b, f ou h.

**Variante.** Une primitive de $\frac{1}{(x + 2)^2}$ sur $]-2 ; +\infty[$ ? *Réponse* : $-\frac{1}{x + 2}$.

### Ex M02a.3 — Intégrales et aires : le signe, l'aire entre deux courbes

**Réponses** : a) `12` · b) `2` · c) `6` · d) `0` · e) `"8/3"` · f) `[0, 2]` · g) `"4/3"` · h) `2`.

**Démarche.**
- a) $\big[x^2 - x\big]_1^4 = 12 - 0 = 12$.
- b) $\big[e^x\big]_0^{\ln 3} = 3 - 1 = 2$.
- c) $\big[2\ln x\big]_1^{e^3} = 2 \times 3 - 0 = 6$.
- d) $\left[\frac{x^3}{3} - x^2\right]_{-1}^{2} = \left(\frac{8}{3} - 4\right) - \left(-\frac{1}{3} - 1\right) = -\frac{4}{3} + \frac{4}{3} = 0$.
- e) $x^2 - 2x = x(x - 2)$ est positive sur $[-1 ; 0]$ et négative sur $[0 ; 2]$ : $\int_{-1}^0 = \frac{4}{3}$ et $\int_0^2 = -\frac{4}{3}$, d'où l'aire $\frac{4}{3} + \frac{4}{3} = \frac{8}{3}$. L'intégrale de d) est nulle parce que les deux morceaux se compensent.
- f) $2x = x^2 \iff x(x - 2) = 0$ : $x = 0$ ou $x = 2$.
- g) Sur $[0 ; 2]$, $2x \ge x^2$ (essaie $x = 1$) : $\int_0^2 (2x - x^2)\,dx = 4 - \frac{8}{3} = \frac{4}{3}$.
- h) $\big[-\cos x\big]_0^{\pi} = -(-1) - (-1) = 2$.

**Erreurs fréquentes.** Répondre 0 à e (l'intégrale au lieu de l'aire) ; inverser les courbes en g ($-\frac{4}{3}$) ; prendre $\cos$ pour primitive de $\sin$ en h ($-2$).

**Variante.** L'aire entre $y = x^2$ et $y = 4$ ? *Réponse* : intersections en $\pm 2$, $\int_{-2}^2 (4 - x^2)\,dx = \frac{32}{3}$.

### Ex M02a.4 — Intégration par parties

**Réponses** : a) `1` · b) `2.0973` · c) `"x*sin(x) + cos(x)"` · d) `1` · e) `"x**2*ln(x)/2 - x**2/4"` · f) `0.7183`.

**Démarche.**
- a) On dérive $x$ (il devient 1) et on intègre $e^{2x}$.
- b) $u = x$, $v = \frac{e^{2x}}{2}$ : $\left[\frac{x\,e^{2x}}{2}\right]_0^1 - \int_0^1 \frac{e^{2x}}{2}\,dx = \frac{e^2}{2} - \frac{e^2 - 1}{4} = \frac{e^2 + 1}{4} \approx 2{,}0973$.
- c) $u = x$, $v = \sin x$ : $x\sin x - \int \sin x\,dx = x\sin x + \cos x$.
- d) $u = \ln x$, $v' = 1$, $v = x$ : $\big[x\ln x\big]_1^e - \int_1^e 1\,dx = e - (e - 1) = 1$. Au passage : une primitive de $\ln x$ est $x\ln x - x$.
- e) $u = \ln x$, $v = \frac{x^2}{2}$ : $\frac{x^2\ln x}{2} - \int \frac{1}{x} \times \frac{x^2}{2}\,dx = \frac{x^2\ln x}{2} - \frac{x^2}{4}$.
- f) $u = x^2$, $v = e^x$ : $\big[x^2 e^x\big]_0^1 - 2\int_0^1 x\,e^x\,dx$ ; puis $\int_0^1 x\,e^x\,dx = \big[(x - 1)e^x\big]_0^1 = 0 - (-1) = 1$. Total : $e - 2 \approx 0{,}7183$.

**Erreurs fréquentes.** Choisir $u = e^{2x}$ (l'intégrale devient plus compliquée) ; oublier le facteur $\frac{1}{2}$ de la primitive de $e^{2x}$ ; un signe dans la seconde intégrale ; en f, oublier le facteur 2 (on trouve $e - 1$).

**Variante.** $\int_0^{\pi} x\sin x\,dx$ ? *Réponse* : $\big[-x\cos x\big]_0^{\pi} + \int_0^{\pi} \cos x\,dx = \pi + 0 = \pi$.

### Ex M02a.5 — Changement de variable

**Réponses** : a) `[3, 5]` · b) `"31/5"` · c) `"ln(x**2 + 4)/2"` · d) `8.6836` · e) `0.4908` · f) `"1/3"`.

**Démarche.**
- a) $u(0) = 3$ et $u(1) = 5$.
- b) $u = x^3 + 1$, $du = 3x^2\,dx$, $u$ de 1 à 2 : $\int_1^2 u^4\,du = \frac{32 - 1}{5} = \frac{31}{5}$.
- c) $u = x^2 + 4$, $du = 2x\,dx$ : $\frac{1}{2}\int \frac{du}{u} = \frac{1}{2}\ln(x^2 + 4)$ (positif, pas de valeur absolue).
- d) $u = 2x + 1$, $du = 2\,dx$, $u$ de 1 à 3 : $\frac{1}{2}\int_1^3 e^u\,du = \frac{e^3 - e}{2} \approx 8{,}6836$.
- e) $u = x^2$, $du = 2x\,dx$, $u$ de 0 à 4 : $\frac{1}{2}\int_0^4 e^{-u}\,du = \frac{1 - e^{-4}}{2} \approx 0{,}4908$.
- f) $u = \ln x$, $du = \frac{dx}{x}$, $u$ de 0 à 1 : $\int_0^1 u^2\,du = \frac{1}{3}$.

**Erreurs fréquentes.** Garder les anciennes bornes ($\frac{1}{5}$ en b) ; oublier le facteur $\frac{1}{2}$ venu de $du = 2x\,dx$ ; poser un $u$ dont la dérivée n'apparaît pas.

**Variante.** $\int_0^{\pi/2} \sin x\,\cos^2 x\,dx$ ? *Réponse* : $u = \cos x$, $du = -\sin x\,dx$, $u$ de 1 à 0 : $\int_0^1 u^2\,du = \frac{1}{3}$.

### Ex M02a.6 — Intégrales impropres : converge, diverge, valeur

**Réponses** : a) `"1/3"` · b) `3` · c) `4` · d) `False` · e) `"1/2"` · f) `"]1 ; +oo["` · g) `"1/4"` · h) `"sqrt(pi)/2"`.

**Démarche.**
- a) $\int_3^b \frac{dx}{x^2} = \frac{1}{3} - \frac{1}{b} \to \frac{1}{3}$.
- b) $\int_0^b e^{-x/3}\,dx = 3\big(1 - e^{-b/3}\big) \to 3$.
- c) $\int_\varepsilon^4 x^{-1/2}\,dx = 4 - 2\sqrt{\varepsilon} \to 4$.
- d) $p = 0{,}9 \le 1$ : $\int_1^b x^{-0{,}9}\,dx = 10\big(b^{0{,}1} - 1\big) \to +\infty$. Elle diverge, très lentement.
- e) $\int_a^0 e^{2x}\,dx = \frac{1 - e^{2a}}{2} \to \frac{1}{2}$ quand $a \to -\infty$.
- f) $p > 1$ : pour $p = 1$, $\ln b \to +\infty$ ; pour $p < 1$, $b^{1-p} \to +\infty$.
- g) $\frac{1}{p - 1} = \frac{1}{4}$.
- h) $e^{-x^2}$ est paire : les deux moitiés de l'intégrale de Gauss sont égales, donc $\frac{\sqrt{\pi}}{2}$.

**Erreurs fréquentes.** Croire qu'il suffit que la fonction tende vers 0 (d) ; inclure $p = 1$ en f ; un signe en a ou e.

**Variante.** $\int_0^{+\infty} \frac{dx}{(1 + x)^2}$ ? *Réponse* : $\left[-\frac{1}{1 + x}\right]_0^b \to 1$.

### Ex M02a.7 — Trapèzes et Simpson à la main, et leurs erreurs

**Réponses** : a) `3.1` · b) `"47/15"` · c) `3.1312` · d) `0.0416` · e) `4.0` · f) `3.14157` · g) `5` · h) `True`.

**Démarche.** $f(0) = 4$, $f(0{,}25) = \frac{4}{1{,}0625} \approx 3{,}764706$, $f(0{,}5) = 3{,}2$, $f(0{,}75) = \frac{4}{1{,}5625} = 2{,}56$, $f(1) = 2$.
- a) $T_2 = 0{,}5 \times (2 + 3{,}2 + 1) = 3{,}1$.
- b) $S_2 = \frac{0{,}5}{3}(4 + 4 \times 3{,}2 + 2) = \frac{18{,}8}{6} = \frac{47}{15} \approx 3{,}1333$.
- c) $T_4 = 0{,}25 \times (2 + 3{,}764706 + 3{,}2 + 2{,}56 + 1) \approx 3{,}131176$.
- d) $\lvert 3{,}1 - 3{,}141593 \rvert \approx 0{,}041593$.
- e) $\frac{0{,}041593}{0{,}010417} \approx 3{,}99$ : environ 4, comme le dit la fiche.
- f) $S_4 = \frac{0{,}25}{3}(4 + 4 \times 3{,}764706 + 2 \times 3{,}2 + 4 \times 2{,}56 + 2) \approx 3{,}141569$ : déjà 5 décimales justes.
- g) 5 points : $x_0$ à $x_4$.
- h) La courbe de $5 - 2x$ est une droite : chaque trapèze a exactement l'aire de la région sous elle.

**Erreurs fréquentes.** Compter les extrémités entièrement ; les poids de Simpson inversés (2 aux indices impairs) ; oublier le $\frac{h}{3}$.

**Variante.** $T_1$ et $S_2$ pour $\int_0^2 x^3\,dx = 4$ ? *Réponse* : $T_1 = 2 \times \frac{0 + 8}{2} = 8$, $S_2 = \frac{1}{3}(0 + 4 + 8) = 4$ (exact : degré 3).

### Ex M02a.8 — Vérifier qu'une fonction est une densité, trouver sa constante

**Réponses** : a) `"1/8"` · b) `2` · c) `1` · d) `"2/9"` · e) `False` · f) `True` · g) `"1/2"` · h) `2`.

**Démarche.**
- a) $\int_0^4 x\,dx = 8$, donc $8c = 1$.
- b) $\int_0^{+\infty} e^{-2x}\,dx = \frac{1}{2}$, donc $c = 2$.
- c) $\int_1^{+\infty} \frac{dx}{x^2} = 1$, donc $c = 1$.
- d) $\int_0^3 (3 - x)\,dx = 9 - \frac{9}{2} = \frac{9}{2}$, donc $c = \frac{2}{9}$.
- e) $g$ est négative sur $[0 ; 1[$ ($g(0) = -1$) : ce n'est pas une densité, même si $\int_0^2 g = 0$… et l'aire totale devrait de toute façon valoir 1.
- f) Positive, d'aire $3 \times \frac{1}{3} = 1$ : c'est une densité (qui vaut 3).
- g) $\int_1^3 \frac{x}{8}\,dx = \left[\frac{x^2}{16}\right]_1^3 = \frac{9 - 1}{16} = \frac{1}{2}$.
- h) $2e^{-2x}$ décroît : son maximum est en 0, et vaut 2.

**Erreurs fréquentes.** Prendre l'intégrale au lieu de son inverse (8 en a) ; oublier la condition de positivité (e) ; croire qu'une densité ne dépasse jamais 1 (f, h).

**Variante.** La constante $c$ qui fait de $c\sqrt{x}$ sur $[0 ; 1]$ une densité ? *Réponse* : $\int_0^1 \sqrt{x}\,dx = \frac{2}{3}$, donc $c = \frac{3}{2}$.

### Ex M02a.9 — La probabilité d'un intervalle, et la valeur moyenne d'une fonction

**Réponses** : a) `"1/8"` · b) `"7/8"` · c) `0` · d) `"13/32"` · e) `0.1353` · f) `0.2325` · g) `3` · h) `0.5820`.

**Démarche.** Pour $X$, $F(x) = \frac{x^3}{8}$ sur $[0 ; 2]$.
- a) $F(1) = \frac{1}{8}$.
- b) $F(2) - F(1) = 1 - \frac{1}{8} = \frac{7}{8}$.
- c) Une valeur exacte : probabilité nulle.
- d) $F(1{,}5) - F(0{,}5) = \frac{3{,}375 - 0{,}125}{8} = \frac{3{,}25}{8} = \frac{13}{32}$.
- e) $\int_{10}^{+\infty} 0{,}2\,e^{-0{,}2t}\,dt = e^{-2} \approx 0{,}1353$.
- f) $e^{-1} - e^{-2} \approx 0{,}367879 - 0{,}135335 = 0{,}232544 \approx 0{,}2325$ (en arrondissant d'abord à 4 décimales, on trouverait 0,2326 : on n'arrondit qu'à la fin).
- g) $\frac{1}{3}\int_0^3 x^2\,dx = \frac{9}{3} = 3$.
- h) $\frac{1}{e - 1}\int_1^e \frac{dx}{x} = \frac{1}{e - 1} \approx 0{,}5820$.

**Erreurs fréquentes.** Lire la densité en un point pour une probabilité (a : $\frac{3}{8}$) ; en e, donner $P(T \le 10)$ ; oublier de diviser par la longueur de l'intervalle (g : 9).

**Variante.** $P(T \le 1)$ ? *Réponse* : $1 - e^{-0{,}2} \approx 0{,}1813$.

### Ex M02a.10 — Fonction de répartition, médiane et percentiles d'une loi donnée

**Réponses** : a) `"3/4"` · b) `"1 - 1/x**2"` · c) `"sqrt(2)"` · d) `10` · e) `"1/25"` · f) `2.7726` · g) `1.1507` · h) `9.2103`.

**Démarche.**
- b) $F(x) = \int_1^x \frac{2}{t^3}\,dt = \left[-\frac{1}{t^2}\right]_1^x = 1 - \frac{1}{x^2}$.
- a) $F(2) = 1 - \frac{1}{4} = \frac{3}{4}$.
- c) $1 - \frac{1}{m^2} = \frac{1}{2} \iff m^2 = 2 \iff m = \sqrt{2}$ (positif).
- d) $\frac{1}{x^2} = 0{,}01 \iff x = 10$.
- e) $1 - F(5) = \frac{1}{25}$.
- f) Pour $D$, $F(t) = 1 - e^{-0{,}25t}$ et $q_p = -4\ln(1 - p)$ : médiane $4\ln 2 \approx 2{,}7726$ ans.
- g) $q_{0{,}25} = -4\ln 0{,}75 = 4\ln\frac{4}{3} \approx 1{,}1507$.
- h) $q_{0{,}9} = -4\ln 0{,}1 = 4\ln 10 \approx 9{,}2103$.

**Erreurs fréquentes.** Une primitive sans la bonne constante en b ($-\frac{1}{x^2}$, qui ne vaut pas 0 en 1) ; oublier la racine en c et d ; prendre $\ln(0{,}25)$ au lieu de $\ln(0{,}75)$ en g.

**Variante.** Le percentile 75 de $X$ ? *Réponse* : $\frac{1}{x^2} = 0{,}25$, $x = 2$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M02a.11 — Le théorème fondamental : la dérivée d'une aire

**Réponse modèle.**
1. Par la relation de Chasles, $\int_a^{x+h} f = \int_a^x f + \int_x^{x+h} f$, donc $A(x + h) - A(x) = \int_x^{x+h} f(t)\,dt$.
2. $f$ est croissante : pour $t$ dans $[x ; x + h]$, $f(x) \le f(t) \le f(x + h)$. Par positivité de l'intégrale (appliquée aux différences), $\int_x^{x+h} f(x)\,dt \le \int_x^{x+h} f(t)\,dt \le \int_x^{x+h} f(x + h)\,dt$, et l'intégrale d'une constante $k$ sur un intervalle de longueur $h$ vaut $kh$. Sur le dessin : la bande est entre le rectangle de hauteur $f(x)$ et celui de hauteur $f(x + h)$.
3. En divisant par $h > 0$ : $f(x) \le \frac{A(x + h) - A(x)}{h} \le f(x + h)$. Quand $h \to 0^+$, $f(x + h) \to f(x)$ par continuité, donc, par encadrement, le taux d'accroissement tend vers $f(x)$.
4. Avec le cas $h < 0$ (admis), $A$ est dérivable et $A' = f$ : $A$ est une primitive de $f$. Si $F$ est une autre primitive, $F - A$ a une dérivée nulle sur l'intervalle, donc $F = A + C$. Alors $F(b) - F(a) = A(b) - A(a) = \int_a^b f - 0$.
5. $f(t) = e^{-t^2}$ est continue (mais pas croissante) : par la version générale du théorème, valable aussi pour $x < 0$, $G'(x) = e^{-x^2}$ et $G'(1) = e^{-1} \approx 0{,}368$. $G' > 0$ partout : $G$ est strictement croissante (logique : on ajoute de l'aire positive).

**Grille.** Une bonne démonstration : (1) cite Chasles ; (2) encadre $f$ sur $[x ; x + h]$ grâce à la croissance, puis intègre l'encadrement ; (3) divise par $h$ en gardant le sens des inégalités ($h > 0$), et invoque la continuité pour passer à la limite ; (4) explique pourquoi n'importe quelle primitive convient (constante) ; (5) applique le résultat sans chercher à calculer $G$, en remarquant que c'est la version générale (fonction continue) qui s'applique.

### Ex M02a.12 — Encadrer une aire par des rectangles : pourquoi les sommes de Riemann convergent (fonction croissante)

**Réponse modèle.**
1. Sur $[x_i ; x_{i+1}]$, $f(x_i) \le f(t) \le f(x_{i+1})$ (croissance), donc $h\,f(x_i) \le \int_{x_i}^{x_{i+1}} f \le h\,f(x_{i+1})$. En additionnant pour $i = 0$ à $n - 1$ (Chasles réunit les intégrales) : $L_n \le \int_a^b f \le R_n$.
2. $R_n - L_n = h\big(f(x_1) + \cdots + f(x_n)\big) - h\big(f(x_0) + \cdots + f(x_{n-1})\big)$ : les termes $f(x_1)$ à $f(x_{n-1})$ se simplifient, il reste $h\big(f(x_n) - f(x_0)\big) = \frac{b - a}{n}\big(f(b) - f(a)\big)$.
3. $L_n$ et $R_n$ encadrent l'intégrale, et leur écart tend vers 0 ; chacune est donc à au plus $R_n - L_n$ de l'intégrale, et tend vers elle.
4. $\frac{(1 - 0)(e - 1)}{n} \le 10^{-3} \iff n \ge 1\,000(e - 1) \approx 1\,718{,}3$ : $n = 1\,719$ suffit. (C'est une borne : l'erreur réelle de $L_n$ est environ la moitié.)
5. Pour une fonction décroissante, les inégalités s'inversent ($R_n \le \int \le L_n$) et l'écart vaut $\frac{(b - a)(f(a) - f(b))}{n}$ : même conclusion. Pour $\sin$ sur $[0 ; \pi]$, on coupe en $[0 ; \frac{\pi}{2}]$ (croissante) et $[\frac{\pi}{2} ; \pi]$ (décroissante), avec $n$ pair pour que $\frac{\pi}{2}$ soit un point de la subdivision, et on applique le résultat à chaque morceau. Pour une fonction continue quelconque, la preuve demande un outil de plus (la continuité uniforme), admis.

**Grille.** Une bonne démonstration : (1) encadre sur chaque petit intervalle, puis additionne avec Chasles ; (2) montre la simplification télescopique ; (3) conclut par encadrement, avec la borne de l'erreur ; (4) résout l'inégalité et arrondit $n$ vers le haut ; (5) adapte l'argument (décroissante, puis découpage en morceaux monotones).

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M02a.13 — L'aire sous une courbe ROC donnée par une formule

**Réponses** : a) `"3/4"` · b) `"4/5"` · c) `"B"` · d) `0.875` · e) `0.8409` · f) `False` · g) `0.6875` · h) `"1/3"`.

**Démarche.**
- a) $\int_0^1 \big(1 - (1 - x)^3\big)\,dx = 1 - \int_0^1 (1 - x)^3\,dx = 1 - \left[-\frac{(1 - x)^4}{4}\right]_0^1 = 1 - \frac{1}{4} = \frac{3}{4}$.
- b) $\left[\frac{x^{5/4}}{5/4}\right]_0^1 = \frac{4}{5}$.
- d) $1 - 0{,}5^3 = 0{,}875$. e) $0{,}5^{1/4} \approx 0{,}8409$.
- f) Au FPR 0,5, A fait mieux que B, alors que l'AUC de B est plus grande : les courbes se croisent.
- g) $0{,}5 \times \left(\frac{0}{2} + 0{,}875 + \frac{1}{2}\right) = 0{,}6875$ : trois points ne suffisent pas (0,75 en vrai).
- h) $\int_0^1 x^2\,dx = \frac{1}{3}$.

Pour la copie : à 10 % de faux positifs, $\text{TPR}_A = 1 - 0{,}9^3 \approx 0{,}271$ et $\text{TPR}_B = 0{,}1^{1/4} \approx 0{,}562$ : on choisit B. Le modèle C est **sous** la diagonale : il classe moins bien que le hasard (son AUC est inférieure à $\frac{1}{2}$) ; tu verras en M03 qu'inverser ses scores le rendrait meilleur que le hasard.

**Erreurs fréquentes.** Oublier le « 1 − » de la courbe A ($\frac{1}{4}$) ; croire qu'une AUC plus grande garantit un meilleur TPR partout ; en g, compter les extrémités entièrement.

**Variante.** L'AUC de $\text{TPR} = 2x - x^2$ ? *Réponse* : $1 - \frac{1}{3} = \frac{2}{3}$.

### Ex M02a.14 — MML §6.2 (la partie continue) : densité et fonction de répartition, en anglais

**Éléments de réponse** (ta formulation compte, pas la nôtre).
1. La définition est donnée pour une fonction $f$ ; le livre écrit ensuite souvent $p(x)$, pour une loi discrète comme pour une densité. Mots : *probability density function* (*pdf*), *cumulative distribution function* (*cdf*) ; pour une loi discrète, *probability mass function* (*pmf*).
2. La fonction est positive ou nulle partout, et son intégrale sur tout l'ensemble des valeurs vaut 1 : les deux conditions du §6 de la fiche. Le livre les écrit pour des variables à plusieurs dimensions, $\mathbf{x} \in \mathbb{R}^D$ : l'intégrale est alors une intégrale multiple (M02b en donne un premier contact).
3. $F(x) = \int_{-\infty}^x f(t)\,dt$.
4. Une densité peut prendre des valeurs supérieures à 1, contrairement aux probabilités d'une loi discrète. Avec une loi uniforme sur un intervalle de longueur 0,4, par exemple $[3 ; 3{,}4]$ : la densité vaut $\frac{1}{0{,}4} = 2{,}5$, et l'aire $2{,}5 \times 0{,}4 = 1$.
5. Une loi discrète : sa fonction de répartition monte par marches et n'a pas de densité (aucune fonction ne donne une probabilité positive à un seul point par une intégrale).
6. Personnel. Mots fréquents : *support*, *univariate* (à une variable), *non-negative*, *integrable*, *state space* (l'ensemble des valeurs).

### Ex M02a.15 — Expliquer pourquoi P(X = a) = 0 pour une variable continue

**Exemple de réponse.**

> Pour une durée, qui peut prendre toutes les valeurs, on ne lit pas la probabilité en un point mais sur un intervalle : c'est l'aire sous la courbe de la densité, $P(a \le X \le b) = \int_a^b f(x)\,dx$. Au-dessus d'un seul instant, la « bande » a une largeur nulle, donc une aire nulle : la probabilité que le bus arrive à 8 h 03 min 00 s exactement, à l'infini de décimales près, vaut 0. Mais une minute entière, de 8 h 03 à 8 h 04, a une aire positive : le bus arrive bien dans un intervalle, il n'arrive simplement jamais « pile » à un instant fixé à l'avance. Une infinité d'instants de probabilité nulle peuvent former un intervalle de probabilité positive : on ne peut pas additionner une infinité continue de zéros. Conséquence pratique : $P(X \le a) = P(X < a)$, le point $a$ ne compte pas.

**Grille.** Une bonne réponse : (1) la probabilité est une aire sous la densité ; (2) au-dessus d'un point, la largeur est nulle ; (3) un intervalle a une probabilité positive : rien d'impossible ; (4) l'infinité de points ne s'additionne pas ; (5) $\le$ et $<$ donnent la même probabilité ; (6) huit lignes au plus, une seule formule.

<a id="entretien"></a>

## 💼 Entretien

### M02a.E1 — Chaque valeur a une probabilité nulle : comment dire qu'une valeur est plus probable qu'une autre ?

**Réponse modèle (60 secondes).**

> On compare les **densités**, pas des probabilités de points. La densité $f(x)$ est une probabilité par unité de longueur : pour un petit intervalle de largeur $h$ autour de $x$, la probabilité vaut environ $f(x)\,h$. Dire que 1,8 est plus vraisemblable que 2,5, c'est dire que $f(1{,}8) > f(2{,}5)$ : un petit intervalle autour de 1,8 a plus de chances qu'un intervalle de même largeur autour de 2,5. Le rapport $\frac{f(1{,}8)}{f(2{,}5)}$ ne dépend même pas de $h$. C'est ce que font les modèles qui maximisent une vraisemblance continue, ou un modèle génératif qui donne une « log-densité ». Et une densité peut dépasser 1 sans problème : seule son aire totale doit valoir 1 ; une loi très concentrée a une densité très haute.

**Grille.** (1) densité, et non probabilité d'un point ; (2) $P(x \le X \le x + h) \approx f(x)\,h$ ; (3) comparer deux densités, c'est comparer deux petits intervalles de même largeur ; (4) densité supérieure à 1 : normale, seule l'aire compte ; (5) un exemple ML (vraisemblance, modèle génératif).

<a id="notebook"></a>

## Notebook

### Ex M02a.16 — Rectangles et trapèzes · `riemann_sum`, `trapezoid`

**Réponses** : a) `14.0` · b) `27.0` · c) `19.75` · d) `1.7197` · e) `"ValueError"` · f) `"ValueError"` · g) `"float"` · h) `20.5`.

**Démarche.** `riemann_sum` : tester `n` et `rule` (une `ValueError` sinon), puis `h = (b - a) / n` et un décalage (0, 1 ou 0,5) selon la règle : `float(h * sum(f(a + (i + shift) * h) for i in range(n)))`. `trapezoid` : `h * ((f(a) + f(b)) / 2 + sum(f(a + i * h) for i in range(1, n)))`. Pour la copie : h) $= \frac{a) + b)}{2}$, les trapèzes sont la moyenne des sommes à gauche et à droite ; le point milieu (19,75) est le plus proche de 20.

**Erreurs fréquentes.** Un décalage faux pour `"right"` (commencer à `i = 1` et oublier le dernier point) ; diviser par `n` avant de le tester (une `ZeroDivisionError` au lieu d'une `ValueError`) ; renvoyer un entier ou un nombre de NumPy.

### Ex M02a.17 — La méthode de Simpson · `simpson`

**Réponses** : a) `1.718319` · b) `"ValueError"` · c) `0.75` · d) `16.9` · e) `"float"`.

**Démarche.** Tester `n` (pair, au moins 2), puis `total = f(a) + f(b)` et, pour `i` de 1 à `n - 1`, ajouter `4 * f(a + i * h)` si `i` est impair, `2 * f(...)` sinon ; rendre `float(h / 3 * total)`. Pour la copie : c) $\left[\frac{x^4}{4} - x^2\right]_{-1}^2 = 0{,}75$, Simpson est exacte pour un polynôme de degré 3 ; d) environ 16,9, proche de 16.

**Erreurs fréquentes.** Les poids 2 et 4 inversés ; oublier `h / 3` ; accepter `n` impair.

### Ex M02a.18 — De la densité à la fonction de répartition, puis au quantile par dichotomie · `cdf_from_pdf`, `quantile`

**Réponses** : a) `0.216` · b) `0.0` · c) `0.189` · d) `0.5` · e) `1.151293` · f) `"ValueError"` · g) `0.865`.

**Démarche.** `cdf_from_pdf` : tester `n`, rendre 0,0 si `x <= lower`, sinon `trapezoid(pdf, lower, x, n)`. `quantile` : tester `p`, `low < high` et `cdf(low) <= p <= cdf(high)`, puis une dichotomie qui garde `cdf(lo) < p <= cdf(hi)` : si `cdf(mid) < p`, le quantile est à droite (`lo = mid`), sinon à gauche (`hi = mid`) ; s'arrêter quand `hi - lo < tol` ou après 200 tours. Pour la copie : e) $\frac{\ln 10}{2}$, la formule de la fiche ; c) un seul trapèze remplace l'arc par une corde.

**Erreurs fréquentes.** Une boucle `while` sans limite de tours (elle ne s'arrête pas avec `tol = 0`) ; garder la moitié où `cdf(mid) <= p` (on obtient le plus **grand** $x$ d'un palier, pas le plus petit) ; oublier le cas `x <= lower`.

### Ex M02a.19 — Vérifier avec `scipy.integrate.quad` et SymPy

**Réponses** : a) `1.772454` · b) `True` · c) `1` · d) `"pi"` · e) `2.0` · f) `"erf"`.

**Démarche.** `value, error = quad(lambda t: math.exp(-t ** 2), -math.inf, math.inf)` ; `sp.integrate(x * sp.exp(-x), (x, 0, sp.oo))` ; `str(sp.integrate(4 / (1 + x ** 2), (x, 0, 1)))` ; `quad(lambda t: 1 / math.sqrt(t), 0, 1)[0]` ; `sp.integrate(sp.exp(-x ** 2), x)` rend `sqrt(pi)*erf(x)/2`. Pour la copie : `erf` est un **nom** donné à l'intégrale $\frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$, pas une formule avec les fonctions usuelles : pas de contradiction.

**Erreurs fréquentes.** Rendre le couple de `quad` entier ; oublier `sp.oo` (SymPy attend son infini) ; une primitive au lieu d'une intégrale en d.

### Ex M02a.20 — Prédire : le pas divisé par 2, l'erreur divisée par combien ?

**Réponses** : a) `2` · b) `3` · c) `1` · d) `4`.

**Démarche.** a) et b) : $e^x$ est régulière ; l'expérience donne 4,0 et 15,9. c) La dérivée de $\sqrt{x}$ est infinie en 0 : le premier intervalle concentre l'erreur, qui n'est divisée que par environ 2,8 ($2^{1{,}5}$). d) Pour une fonction régulière et périodique, intégrée sur une période entière, les erreurs des trapèzes se compensent : l'erreur passe de $3 \times 10^{-2}$ à $10^{-6}$ (rapport de plusieurs dizaines de milliers). Pour la copie : l'hypothèse « fonction régulière » (dérivées bornées) manque en c.

**Erreurs fréquentes.** Appliquer « ÷ 16 » à Simpson quelle que soit la fonction ; croire que les trapèzes sont toujours d'ordre 2.

### Ex M02a.21 — L'intégrale de Gauss par le calcul : la borne qui s'éloigne

**Réponses** : a) `1.4936` · b) `4` · c) `0.999978` · d) `2.5066`.

**Démarche.** `I(B) = quad(lambda x: math.exp(-x ** 2), -B, B)[0]` ; b) les écarts valent 0,28 ; 0,0083 ; 3,9e-5 ; 2,7e-8 ; 2,7e-12 pour $B = 1$ à 5 ; d) $\sqrt{2\pi} \approx 2{,}5066$. Pour la copie : $\sqrt{\pi} - I(B) = 2\int_B^{+\infty} e^{-x^2}\,dx \le 2\int_B^{+\infty} e^{-Bx}\,dx = \frac{2e^{-B^2}}{B}$, soit $5{,}6 \times 10^{-8}$ pour $B = 4$ : la borne est proche de l'écart réel. Au-delà de 6 écarts types, la densité normale n'a plus qu'environ $2 \times 10^{-9}$ de sa masse : couper à 6 ne change rien.

**Erreurs fréquentes.** Intégrer de 0 à $B$ (on trouve la moitié) ; prendre $e^{-x^2}$ au lieu de $e^{-x^2/2}$ en d.

### Ex M02a.22 — L'aire qui se remplit : la courbe, les rectangles et la primitive

**Démarche.** `draw_riemann` : `h = (b - a) / n`, `lefts = [a + i * h ...]`, `heights = [f(left + h / 2) ...]`, `ax.bar(lefts, heights, width=h, align="edge", alpha=0.4)`, la courbe avec `ax.plot`, et le titre `f"... somme = {h * sum(heights):.4f}"`. `draw_area_function` : une grille `xs = np.linspace(a, b, 200)`, les aires des petits trapèzes `(xs[1:] - xs[:-1]) * (ys[1:] + ys[:-1]) / 2`, leurs sommes cumulées `np.cumsum`, précédées d'un 0, puis les deux courbes et une légende. Pour la copie : les deux courbes se superposent (théorème fondamental) ; la fonction aire monte le plus vite là où $f$ est la plus haute, vers $x = 1$.

**Erreurs fréquentes.** `align="center"` (les rectangles débordent) ; oublier le 0 au début de la somme cumulée (199 valeurs pour 200 points) ; ouvrir une figure dans la fonction.

### Ex M02a.23 — Chasse à l'erreur : bornes inversées, primitive fausse, aire négative

**Réponses** : a) `"ACD"` · b) `[8, 0.5, 0.3167, 2, 2]`.

**Démarche.** (A) bornes inversées dans le crochet : $\big[x^3\big]_0^2 = 8$. (C) primitive fausse ($-\frac{1}{3}e^{-3x}$), d'où $\frac{1 - e^{-3}}{3} \approx 0{,}3167$ ; un résultat négatif pour une fonction positive devait alerter. (D) $x^2 - 1 < 0$ sur $[0 ; 1[$ : l'aire vaut $\frac{2}{3} + \frac{4}{3} = 2$, l'intégrale $\frac{2}{3}$. (B) et (E) sont justes.

**Erreurs fréquentes.** Accuser (B), où les deux signes moins se compensent bien ; donner pour (D) la valeur de l'intégrale.

### Ex M02a.24 — Vérifier une primitive avec SymPy : dériver le résultat

**Démarche.** `return bool(sp.simplify(sp.diff(F, x) - f) == 0)`. Pour la copie : $\frac{\sin^2 x}{2} + \frac{\cos 2x}{4} = \frac{1}{4}$ (car $\cos 2x = 1 - 2\sin^2 x$) : deux primitives d'une même fonction diffèrent d'une constante.

**Erreurs fréquentes.** Comparer `sp.diff(F, x) == f` sans simplifier (SymPy compare l'écriture, pas la valeur) ; renvoyer un booléen de SymPy au lieu de `True` ou `False`.

### Ex M02a.25 — Défi : la meilleure précision avec dix évaluations de la fonction

**Démarche.** La quadrature de Gauss-Legendre à 10 points : `nodes, weights = np.polynomial.legendre.leggauss(10)`, puis le changement de variable affine $x = \frac{a + b}{2} + \frac{b - a}{2}t$, qui envoie $[-1 ; 1]$ sur $[a ; b]$ et multiplie les poids par $\frac{b - a}{2}$. Erreurs : $3 \times 10^{-13}$, $7 \times 10^{-16}$ et $2 \times 10^{-9}$. La piste 1 (Boole, $\frac{16S_8 - S_4}{15}$, 9 évaluations) atteint $10^{-6}$ sur les deux premières, mais pas la troisième ($4 \times 10^{-5}$). Pour la copie : les points de Gauss sont placés pour être exacts sur les polynômes de degré au plus 19 ; $\sqrt{1 + x^3}$ a des dérivées d'ordre élevé qui grandissent vite, ce qui pénalise les méthodes à points réguliers.

**Erreurs fréquentes.** Appeler `f` plus de 10 fois sans s'en rendre compte (Simpson avec $n = 10$ en demande 11) ; oublier le facteur $\frac{b - a}{2}$ du changement de variable.
