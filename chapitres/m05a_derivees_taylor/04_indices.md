# M05a · Dérivées, Taylor et calcul numérique — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, estimation et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M05a.Q1 — Le signe de la dérivée seconde

<details><summary>Indice 1</summary>

Relis « La dérivée de la dérivée » et « Convexe, concave » (fiche §1).

</details>
<details><summary>Indice 2</summary>

$f''$ est la dérivée de $f'$ : son signe dit si la **pente** augmente ou diminue, pas si $f$ augmente.

</details>
<details><summary>Indice 3</summary>

4 : cherche une fonction dont la dérivée seconde s'annule en 2 sans changer de signe. 6 : $(x^3)'' = 6x$.

</details>

### M05a.Q2 — Local ou global ?

<details><summary>Indice 1</summary>

Relis « Sur un intervalle fermé : ne pas oublier les bords » et « La convexité rend le local global » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Sur $[a, b]$, les candidats sont les points critiques **intérieurs** et les deux bords.

</details>
<details><summary>Indice 3</summary>

5 : $e^x$ s'approche de 0 ; l'atteint-elle ? 6 : compare $x^3$, $x^4$ et $-x^4$ en 0.

</details>

### M05a.Q3 — Taylor : quel ordre, quelle précision ?

<details><summary>Indice 1</summary>

Relis la formule de $P_n$ et le reste de Lagrange (fiche §3).

</details>
<details><summary>Indice 2</summary>

$P_1$ a la même valeur et la même pente que $f$ en $a$ : c'est une droite connue.

</details>
<details><summary>Indice 3</summary>

5 : le reste d'ordre 2 est $\frac{M}{3!}|x - a|^3$. 6 : relis le domaine de convergence de la série de $\ln(1 + x)$.

</details>

### M05a.Q4 — Newton converge-t-il ?

<details><summary>Indice 1</summary>

Relis « Suivre la tangente » et « Quand elle échoue » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}$. Près d'une racine simple, l'erreur est à peu près élevée au carré.

</details>
<details><summary>Indice 3</summary>

5 : calcule deux pas depuis 0. 6 : que vaut $f'$ à la racine ?

</details>

### M05a.Q5 — Différence avant ou centrée ?

<details><summary>Indice 1</summary>

Relis « Trois formules et leurs erreurs » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Erreur de la différence avant $\approx \frac{h}{2}f''(x)$, de la centrée $\approx \frac{h^2}{6}f'''(x)$.

</details>
<details><summary>Indice 3</summary>

4 : calcule $\frac{(x + h)^2 - (x - h)^2}{2h}$. 6 : que vaut $f''$ pour une fonction affine ?

</details>

### M05a.Q6 — Les flottants : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Une notation scientifique en base 2 » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$\varepsilon = 2^{-52}$ est l'écart après **1** ; entre $2^e$ et $2^{e+1}$, l'écart vaut $2^e\,\varepsilon$.

</details>
<details><summary>Indice 3</summary>

2 : l'écart entre $2^{53}$ et le flottant suivant. 4 : pense à l'absorption, `1e16 + 1`.

</details>

### M05a.Q7 — Overflow, underflow, log-sum-exp

<details><summary>Indice 1</summary>

Relis « Quand l'exponentielle déborde » et « L'astuce : mettre le maximum en facteur » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$e^x$ déborde au-delà de $x \approx 709{,}78$ en `float64`. $\text{LSE}(\mathbf{v}) = m + \ln\sum_i e^{v_i - m}$.

</details>
<details><summary>Indice 3</summary>

4 : quel est le signe des exposants $v_i - m$ ? Quel est le plus grand terme de la somme ? 5 : factorise $e^c$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M05a.R1 — Dérivées et variations (R7)

<details><summary>Indice 1</summary>

La dérivée d'un produit : $(uv)' = u'v + uv'$.

</details>
<details><summary>Indice 2</summary>

$(x\ln x)' = \ln x + 1$. Le signe de $\ln x$ change en 1.

</details>
<details><summary>Indice 3</summary>

4 : la tangente en $a$ est $y = f(a) + f'(a)(x - a)$. 5 : $(u^4)' = 4u^3u'$.

</details>

### M05a.R2 — Suites définies par récurrence (R5)

<details><summary>Indice 1</summary>

Calcule $u_1$ et $u_2$ avec la formule, puis résous l'équation du point fixe.

</details>
<details><summary>Indice 2</summary>

Soustrais $\ell = 0{,}4\,\ell + 1{,}2$ de $u_{n+1} = 0{,}4\,u_n + 1{,}2$.

</details>
<details><summary>Indice 3</summary>

4 : $|u_n - 2| = 3 \times 0{,}4^n$ ; essaie $n = 6$ et $n = 7$.

</details>

### M05a.R3 — Log-probabilités et log-sum-exp (M04)

<details><summary>Indice 1</summary>

$\ln(ab) = \ln a + \ln b$ et $\ln 10^k = k\ln 10$.

</details>
<details><summary>Indice 2</summary>

Le plus petit `float64` positif vaut environ $5 \times 10^{-324}$.

</details>
<details><summary>Indice 3</summary>

3 : $\frac{e^{-5}}{e^{-5} + e^{-6}} = \frac{1}{1 + e^{-1}}$. 4 : mets $e^{-5}$ en facteur.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M05a.1 — Dérivées secondes et convexité

<details><summary>Indice 1</summary>

Relis « La dérivée de la dérivée » et « Points d'inflexion » (fiche §1).

</details>
<details><summary>Indice 2</summary>

a) Dérive $x e^{2x}$ comme un produit, deux fois. b) Factorise $g''(x) = 12x^2 - 12$ et dresse son tableau de signes. d) $w'(x) = 2x\,e^{x^2}$ est un produit. e) Dérive $(1 + x^2)^{-1}$ deux fois et regarde le signe en 0.

</details>
<details><summary>Indice 3</summary>

g) Un point d'inflexion annule la dérivée **seconde** (en changeant de signe) : écris $(x^3 + kx^2 + 1)''$ et annule-la en 2. h) $\frac{1 + e^2}{2} - e = \frac{(e - 1)^2}{2}$.

</details>

### Ex M05a.2 — Extrema locaux et globaux sur un intervalle fermé

<details><summary>Indice 1</summary>

Relis l'exemple $x^2 e^{-x}$ sur $[-1, 4]$ (fiche §2).

</details>
<details><summary>Indice 2</summary>

$f'(x) = 12x(x^2 - x - 2)$ : factorise le trinôme. Puis calcule $f$ aux points critiques **et** aux bords.

</details>
<details><summary>Indice 3</summary>

g) Sur $[-1{,}5 ;\ 1{,}5]$, le point critique 2 est hors de l'intervalle : les candidats sont $-1{,}5$, $-1$, 0 et 1,5. h) Que fait $3x^4$ quand $|x|$ devient grand ?

</details>

### Ex M05a.3 — Points d'inflexion et test de la dérivée seconde

<details><summary>Indice 1</summary>

Relis le test de la dérivée seconde (fiche §2) : quand ne conclut-il pas ?

</details>
<details><summary>Indice 2</summary>

$p'(x) = 5x^3(x - 4)$ et $p''(x) = 20x^2(x - 3)$ : fais les deux tableaux de signes.

</details>
<details><summary>Indice 3</summary>

d) Le signe de $p'$ juste avant 0 (par exemple en $-1$) et juste après (en 1). e) Un facteur $x^2$ ne change pas de signe.

</details>

### Ex M05a.4 — Polynômes de Taylor de trois fonctions usuelles

<details><summary>Indice 1</summary>

Relis les développements en 0 à connaître (fiche §3), puis calcule les dérivées toi-même.

</details>
<details><summary>Indice 2</summary>

Pour chaque fonction, calcule $f(a), f'(a), f''(a), f'''(a)$, puis divise par $0!, 1!, 2!, 3!$.

</details>
<details><summary>Indice 3</summary>

d) En $a = 1$, toutes les dérivées de $e^x$ valent $e$, et les puissances sont celles de $x - 1 = 0{,}1$. g) $\sin\frac{\pi}{2} = 1$, $\cos\frac{\pi}{2} = 0$. h) $q''(1)$, divisé par $2!$.

</details>

### Ex M05a.5 — Le reste de Taylor : borner l'erreur d'une approximation

<details><summary>Indice 1</summary>

Relis « Le reste : combien se trompe-t-on ? » et l'exemple de $\sqrt{1{,}2}$ (fiche §3).

</details>
<details><summary>Indice 2</summary>

Borne de Lagrange : $\frac{M}{(n+1)!}|x - a|^{n+1}$ si $|f^{(n+1)}| \le M$ entre $a$ et $x$.

</details>
<details><summary>Indice 3</summary>

c) $P_3 = P_4$ pour $\sin$ : utilise le reste d'ordre 4, avec $x^5/5!$. d) Écris $2!, 3!, \ldots$ jusqu'à dépasser $3 \times 10^6$. f) Même astuce qu'en c) pour $\cos$.

</details>

### Ex M05a.6 — Newton à la main : une racine carrée en trois pas

<details><summary>Indice 1</summary>

Relis l'exemple de $e^x = 3$ et la méthode de Héron (fiche §4).

</details>
<details><summary>Indice 2</summary>

Pour $x^2 - 10$ : $x_{k+1} = \frac{1}{2}\big(x_k + \frac{10}{x_k}\big)$. Garde les fractions exactes pour a) et b).

</details>
<details><summary>Indice 3</summary>

e) Le numérateur est l'erreur de $x_2$, le dénominateur le **carré** de l'erreur de $x_1$. h) $g'(x) = \frac{1}{x}$, donc $\frac{g(2)}{g'(2)} = 2(\ln 2 - 1)$.

</details>

### Ex M05a.7 — L'erreur d'une différence avant et d'une différence centrée, par Taylor

<details><summary>Indice 1</summary>

Relis l'exemple de $\ln$ en 2 (fiche §5).

</details>
<details><summary>Indice 2</summary>

$f'(x) = \frac{1}{2}x^{-1/2}$, $f''(x) = -\frac{1}{4}x^{-3/2}$, $f'''(x) = \frac{3}{8}x^{-5/2}$ ; en 4, $x^{1/2} = 2$.

</details>
<details><summary>Indice 3</summary>

c) L'erreur est la différence avant **moins** $\frac{1}{4}$. e) La différence centrée divise par $2h = 0{,}4$. h) La différence seconde approche $f''(4)$.

</details>

### Ex M05a.8 — Les flottants : 0,1 en binaire, epsilon machine, nombres représentables

<details><summary>Indice 1</summary>

Relis « Une notation scientifique en base 2 » et le tableau des formats (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour la partie après la virgule : multiplie par 2, note la partie entière (0 ou 1), recommence avec la partie après la virgule.

</details>
<details><summary>Indice 3</summary>

b) Écris chaque nombre en fraction irréductible : le dénominateur doit être une puissance de 2. d), e) et g) L'écart vaut $\varepsilon$ fois la puissance de 2 juste **en dessous** du nombre ($0{,}25 \le 0{,}3 < 0{,}5$). f) Avec 23 bits après la virgule, combien de bits significatifs ? h) L'erreur relative d'arrondi est $\frac{\varepsilon}{2}$.

</details>

### Ex M05a.9 — Le meilleur pas par le calcul : minimiser une borne d'erreur

<details><summary>Indice 1</summary>

Relis « Deux erreurs qui varient en sens contraire » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Dérive chaque borne par rapport à $h$ et résous $E'(h) = 0$ : $\big(\frac{1}{h}\big)' = -\frac{1}{h^2}$.

</details>
<details><summary>Indice 3</summary>

a) $h^2 = \frac{4\delta}{M_2}$. c) $h^3 = \frac{3\delta}{M_3}$. e) et f) Écris $h^*$ et $E(h^*)$ comme des puissances de $\delta$. g) $h^4 = 4\delta$.

</details>

### Ex M05a.10 — log-sum-exp à la main : la softmax stable de trois scores

<details><summary>Indice 1</summary>

Relis l'exemple $(710, 708, 700)$ (fiche §8).

</details>
<details><summary>Indice 2</summary>

Soustrais le maximum : $(0, -2, -7)$. Il ne reste que des exponentielles d'exposants négatifs.

</details>
<details><summary>Indice 3</summary>

c) $802 + \ln(1 + e^{-2} + e^{-7})$. e) Le log-softmax est $v_2 - \text{LSE}(\mathbf{v})$. g) Trois termes égaux à $e^{802}$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M05a.11 — La différence centrée est d'ordre 2 : le calcul par Taylor (cas général)

<details><summary>Indice 1</summary>

Relis « Trois formules et leurs erreurs » (fiche §5) : c'est le calcul, sans le reste exact.

</details>
<details><summary>Indice 2</summary>

Écris les deux développements avec un reste de Lagrange chacun, puis soustrais-les (pour $D_0$) ou additionne-les (pour la différence seconde).

</details>
<details><summary>Indice 3</summary>

6 : $\xi_+$ et $\xi_-$ sont coincés entre $x - h$ et $x + h$, et $f'''$ est continue. 7 : remplace $h$ par $\frac{h}{2}$ dans le développement admis, puis forme $4D_0(\frac{h}{2}) - D_0(h)$.

</details>

### Ex M05a.12 — Newton double les décimales justes : l'erreur au carré (racine simple)

<details><summary>Indice 1</summary>

Relis « Pourquoi elle va si vite » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Dans le développement de 2, divise par $f'(x_k)$ et reconnais $x_k - x_{k+1} = \frac{f(x_k)}{f'(x_k)}$.

</details>
<details><summary>Indice 3</summary>

4 : pose $d_k = C|e_k|$ et montre $d_{k+1} \le d_k^2$. 5 : $x_{k+1} - \sqrt{c} = \frac{x_k^2 + c}{2x_k} - \sqrt{c}$ : mets au même dénominateur, une identité remarquable apparaît.

</details>

### Ex M05a.13 — Encadrer le log-sum-exp : max ≤ LSE ≤ max + ln n

<details><summary>Indice 1</summary>

Relis l'encadrement du log-sum-exp, sous « Un maximum adouci » (fiche §8).

</details>
<details><summary>Indice 2</summary>

La somme $\sum_i e^{v_i}$ contient le terme $e^m$, et chacun de ses $n$ termes est au plus $e^m$.

</details>
<details><summary>Indice 3</summary>

5 : sépare les cas $t \ge 0$ et $t < 0$. 6 : écris $\text{LSE}(\mathbf{v}) - m = \ln\big(1 + \sum_{i \ne i^*} e^{v_i - m}\big)$, puis majore chaque terme par $e^{-g}$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, estimation et explication

### Ex M05a.14 — Pourquoi les bibliothèques de ML calculent log(softmax) d'un seul coup

<details><summary>Indice 1</summary>

Relis « L'astuce : mettre le maximum en facteur » (fiche §8) et le plus petit `float64` positif (fiche §6).

</details>
<details><summary>Indice 2</summary>

a) Après soustraction du maximum, les deux autres termes valent $e^{-760}$ et $e^{-810}$ : que pèsent-ils à côté de 1 ?

</details>
<details><summary>Indice 3</summary>

c) Compare $e^{-760}$ à $5 \times 10^{-324} \approx e^{-744}$. e) Que fait `math.log(0.0)` ? f) $\text{LSE}(2, 0, -1) = 2 + \ln(1 + e^{-2} + e^{-3})$.

</details>

### Ex M05a.15 — MML §5.1 : dérivée d'une fonction d'une variable et série de Taylor (lecture guidée)

<details><summary>Indice 1</summary>

Lis MML §5.1 avec la fiche (§1 et §3) ouverte à côté.

</details>
<details><summary>Indice 2</summary>

Cherche les définitions numérotées (quotient différentiel, dérivée, polynôme et série de Taylor) et les exemples qui suivent.

</details>
<details><summary>Indice 3</summary>

3 : les dérivées de $x^3$ en 2 sont $8, 12, 12, 6, 0$. 4 : les dérivées de $\cos - \sin$ tournent sur quatre valeurs. 6 : cherche le mot *analytic*.

</details>

### Ex M05a.16 — Fermi : l'erreur d'arrondi d'une somme d'un million de nombres

<details><summary>Indice 1</summary>

Relis « Une notation scientifique en base 2 » et « Les erreurs d'arrondi » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Chaque addition fait une erreur d'au plus $u$ fois la somme partielle, qui est au plus de l'ordre de $10^6$.

</details>
<details><summary>Indice 3</summary>

2 : $n$ erreurs de même signe s'additionnent : $n\,u$ en relatif. 3 : $n$ erreurs de signes au hasard : environ $\sqrt{n}$ fois une erreur. 5 : $\log_2 10^6 \approx 20$.

</details>

### Ex M05a.17 — Expliquer la convexité et pourquoi elle rassure quand on minimise

<details><summary>Indice 1</summary>

Relis « Convexe, concave » (fiche §1) et « La convexité rend le local global » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Choisis une seule image (la corde, la cuvette ou la tangente) et tiens-t'y.

</details>
<details><summary>Indice 3</summary>

Trois idées : ce qu'est une cuvette ; pourquoi une cuvette n'a qu'un fond ; une courbe à deux creux où une descente peut se tromper.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M05a.E1 — Pourquoi soustraire le maximum avant de calculer une softmax ?

<details><summary>Indice 1</summary>

Relis « Quand l'exponentielle déborde » et « L'astuce : mettre le maximum en facteur » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Que vaut `np.exp(1000)` ? Et `inf / inf` ?

</details>
<details><summary>Indice 3</summary>

Plan : le problème (seuil d'environ 709) ; pourquoi le résultat ne change pas (le facteur $e^{-m}$) ; le dénominateur au moins 1 ; le log-softmax pour la loss.

</details>

<a id="notebook"></a>

## Notebook

### Ex M05a.18 — Évaluer un polynôme de Taylor · `taylor_polynomial`

<details><summary>Indice 1</summary>

Relis la docstring : `derivatives` contient $f(a), f'(a), f''(a), \ldots$

</details>
<details><summary>Indice 2</summary>

Une boucle `for k, derivative in enumerate(derivatives)`, un total, et le terme $\frac{(x - a)^k}{k!}$ gardé à jour.

</details>
<details><summary>Indice 3</summary>

`term = 1.0` avant la boucle ; dans la boucle, `if k > 0: term *= (x - a) / k`, puis `total += derivative * term`. N'oublie pas `list(derivatives)`, la `ValueError` et `float(total)`.

</details>

### Ex M05a.19 — La méthode de Newton, avec ses cas d'échec · `newton`

<details><summary>Indice 1</summary>

Relis l'ordre des trois tests dans l'énoncé.

</details>
<details><summary>Indice 2</summary>

Une boucle `for _ in range(max_iter):` ; la `RuntimeError` se lève **après** la boucle.

</details>
<details><summary>Indice 3</summary>

Dans la boucle : `fx = f(x)` ; `if fx == 0: return float(x)` ; `slope = fprime(x)` ; `if slope == 0: raise ValueError(...)` ; `x_new = x - fx / slope` ; `if abs(x_new - x) < tol: return float(x_new)` ; `x = x_new`.

</details>

### Ex M05a.20 — L'extrapolation de Richardson : annuler le terme d'erreur en h² · `richardson_derivative`

<details><summary>Indice 1</summary>

Relis « L'extrapolation de Richardson » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Une fonction interne `centred(step)` qui renvoie $\frac{f(x + \text{step}) - f(x - \text{step})}{2\,\text{step}}$.

</details>
<details><summary>Indice 3</summary>

`if not h > 0: raise ValueError(...)`, puis `float((4 * centred(h / 2) - centred(h)) / 3)`.

</details>

### Ex M05a.21 — L'epsilon machine, en float64, float32 et float16 · `machine_epsilon`

<details><summary>Indice 1</summary>

Relis « Une notation scientifique en base 2 » (fiche §6).

</details>
<details><summary>Indice 2</summary>

`one, two, eps = dtype(1), dtype(2), dtype(1)` ; divise `eps` par `two` tant que `one + eps / two` est différent de `one`.

</details>
<details><summary>Indice 3</summary>

`while dtype(one + dtype(eps / two)) != one: eps = dtype(eps / two)`, puis `return float(eps)`.

</details>

### Ex M05a.22 — Un log-sum-exp stable · `logsumexp`

<details><summary>Indice 1</summary>

Relis « L'astuce : mettre le maximum en facteur » (fiche §8).

</details>
<details><summary>Indice 2</summary>

`values = [float(v) for v in values]`, la `ValueError`, `m = max(values)`.

</details>
<details><summary>Indice 3</summary>

`if math.isinf(m): return m` (tout vaut $-\infty$), puis `float(m + math.log(math.fsum(math.exp(v - m) for v in values)))`.

</details>

### Ex M05a.23 — SymPy `series` et `numpy.finfo` contre tes fonctions

<details><summary>Indice 1</summary>

Commence par `x = sp.Symbol("x")` et affiche `sp.series(sp.tan(x), x, 0, 8)`.

</details>
<details><summary>Indice 2</summary>

`.removeO().coeff(x, k)` lit un coefficient ; `np.finfo(np.float16).tiny`, `np.finfo(float).tiny`, puis `math.log2` ou `math.log10`.

</details>
<details><summary>Indice 3</summary>

f) `[float(sp.diff(sp.exp(sp.sin(x)), x, k).subs(x, 0)) for k in range(5)]`, puis `mymath.approx.taylor_polynomial(..., 0, 0.3)`. c) `tiny` est le plus petit nombre **normal** (pas un sous-normal, pas l'epsilon).

</details>

### Ex M05a.24 — Prédire : Newton depuis un mauvais point de départ

<details><summary>Indice 1</summary>

Dessine la courbe et la tangente au point de départ : où coupe-t-elle l'axe ?

</details>
<details><summary>Indice 2</summary>

Pour d) et e), calcule le pas de Newton en général : $\frac{f(x)}{f'(x)}$ se simplifie.

</details>
<details><summary>Indice 3</summary>

a) et b) $\arctan$ s'aplatit loin de 0 : plus la tangente est plate, plus elle renvoie loin. c) Deux pas depuis 0. d) $\frac{x^{1/3}}{\frac{1}{3}x^{-2/3}} = 3x$. e) $\frac{x^2}{2x} = \frac{x}{2}$.

</details>

### Ex M05a.25 — Taylor de plus en plus loin : où le polynôme décroche

<details><summary>Indice 1</summary>

Relis le domaine de convergence de $\ln(1 + x)$ (fiche §3).

</details>
<details><summary>Indice 2</summary>

Une somme sur $k$ de 1 à $n$ **inclus** : `range(1, n + 1)`.

</details>
<details><summary>Indice 3</summary>

`float(sum((-1) ** (k + 1) * x ** k / k for k in range(1, n + 1)))`.

</details>

### Ex M05a.26 — Une fonction et ses polynômes de Taylor d'ordre 1, 2 et 3

<details><summary>Indice 1</summary>

Relis la figure des polynômes de Taylor de $\cos$ (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pour l'ordre $n$, n'utilise que `derivatives[:n + 1]`.

</details>
<details><summary>Indice 3</summary>

`xs = np.linspace(a - 2, a + 2, 401)` ; `ax.plot(xs, f(xs), label="la fonction")` ; pour chaque ordre, `values = [mymath.approx.taylor_polynomial(derivatives[:order + 1], a, x) for x in xs]` et `ax.plot(xs, values, label=...)` ; `ax.plot(a, f(a), "o")` ; `ax.legend()`.

</details>

### Ex M05a.27 — Chasse à l'erreur : une softmax qui renvoie `nan`

<details><summary>Indice 1</summary>

Relis le tableau des pièges classiques et le §8 de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, demande-toi : la formule est-elle juste ? Et chaque nombre intermédiaire est-il représentable en `float64` ?

</details>
<details><summary>Indice 3</summary>

(A) : quel score faut-il retirer ? (C) : $\text{LSE} = m + \ln(\ldots)$. (E) : que vaut `math.exp(-800)` ? (F) : des probabilités se divisent par le total.

</details>

### Ex M05a.28 — Erreur relative ou absolue : choisir la tolérance d'un test

<details><summary>Indice 1</summary>

Traite d'abord les cas particuliers, puis la formule.

</details>
<details><summary>Indice 2</summary>

Dans l'ordre : tolérances négatives (`ValueError`), égalité exacte (`True`), infinis et `nan` (`False`), puis l'inégalité.

</details>
<details><summary>Indice 3</summary>

`if got == expected: return True` ; `if math.isinf(got) or math.isinf(expected) or math.isnan(got) or math.isnan(expected): return False` ; puis `abs(got - expected) <= max(rel_tol * max(abs(got), abs(expected)), abs_tol)`.

</details>

### Ex M05a.29 — Défi : une racine cubique à 10⁻¹² en le moins d'itérations possible

<details><summary>Indice 1</summary>

Écris d'abord la version simple (départ $x_0 = a$, un compteur de pas), et regarde combien de pas il faut pour $a = 10^{30}$.

</details>
<details><summary>Indice 2</summary>

`m, e = math.frexp(a)` donne $a = m \times 2^e$ ; avec `q, r = divmod(e, 3)`, $\sqrt[3]{a} = \sqrt[3]{m} \times 2^{r/3} \times 2^q$.

</details>
<details><summary>Indice 3</summary>

Une droite qui approche $\sqrt[3]{m}$ sur $[0{,}5 ;\ 1[$ : elle passe par $(0{,}5 ;\ 0{,}8)$ et $(1 ;\ 1)$, soit $0{,}6 + 0{,}4\,m$. Puis `x_new = (2 * x + a / (x * x)) / 3` jusqu'à `abs(x_new - x) <= 1e-15 * x_new`.

</details>
