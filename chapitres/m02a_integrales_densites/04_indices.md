# M02a · Intégrales et densités — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M02a.Q1 — Aire, signe et intégrale

<details><summary>Indice 1</summary>

Relis « Une aire algébrique » (fiche §1) et « Les règles de calcul » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Dessine chaque situation : ce qui est sous l'axe compte négativement ; un intervalle de largeur nulle n'a pas d'aire.

</details>
<details><summary>Indice 3</summary>

2 : dessine $x^3$ sur $[-1 ; 1]$ ; les deux régions sont symétriques par rapport à l'origine. 6 : pour une fonction croissante, la valeur au début de l'intervalle est la plus petite.

</details>

### M02a.Q2 — Primitives : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Primitive » et la table du §2.

</details>
<details><summary>Indice 2</summary>

Pour chaque affirmation, dérive la primitive proposée : redonne-t-elle la fonction ?

</details>
<details><summary>Indice 3</summary>

2 : la dérivée de $e^{2x}$ vaut $2e^{2x}$. 4 : que vaut $n + 1$ quand $n = -1$ ? 6 : la règle de la chaîne, avec $\sin' = \cos$.

</details>

### M02a.Q3 — Quelle méthode de calcul pour quelle intégrale ?

<details><summary>Indice 1</summary>

Relis le §3 : la table et la linéarité d'abord, puis les deux méthodes.

</details>
<details><summary>Indice 2</summary>

Un produit d'un polynôme (ou d'un logarithme) par une exponentielle ou un sinus : par parties. Une fonction composée multipliée par la dérivée de ce qu'elle compose : changement de variable.

</details>
<details><summary>Indice 3</summary>

3 : la dérivée de $x^2 + 1$ est $2x$. 5 : la dérivée de $1 + e^x$ est $e^x$. 2 : dérive $\ln x$, intègre $x$.

</details>

### M02a.Q4 — Converge ou diverge ?

<details><summary>Indice 1</summary>

Relis le §4 : les deux règles des $\frac{1}{x^p}$, et l'exponentielle.

</details>
<details><summary>Indice 2</summary>

Vers $+\infty$ : converge si $p > 1$. Près de 0 : converge si $p < 1$. Écris chaque fonction comme $x^{-p}$.

</details>
<details><summary>Indice 3</summary>

2 : $\frac{1}{\sqrt{x}} = x^{-1/2}$. 5 : $x^{-1/3}$, et l'on regarde près de 0. 6 : l'intégrale de Gauss.

</details>

### M02a.Q5 — Rectangles, trapèzes, Simpson

<details><summary>Indice 1</summary>

Relis le §5, en particulier le tableau « L'ordre d'une méthode ».

</details>
<details><summary>Indice 2</summary>

Trapèzes : $n + 1$ points. Simpson : les intervalles vont par deux. Ordre 2 : l'erreur suit $h^2$.

</details>
<details><summary>Indice 3</summary>

3 : $(h/2)^2 = h^2/4$. 5 : pense à une fonction décroissante. 6 : relis la ligne de Simpson dans le tableau.

</details>

### M02a.Q6 — Densité et probabilité : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §6, « Définition » et « Trois conséquences qui surprennent ».

</details>
<details><summary>Indice 2</summary>

Une densité : positive, d'aire totale 1. Une probabilité : une aire sous la densité.

</details>
<details><summary>Indice 3</summary>

4 : calcule l'aire du rectangle de hauteur 5 et de largeur 0,2. 5 : l'aire de $2f$ ? 6 : l'aire d'un rectangle très étroit.

</details>

### M02a.Q7 — Lire une fonction de répartition

<details><summary>Indice 1</summary>

Relis « La fonction de répartition » et « Quantiles, médiane, percentiles » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$P(X \le a) = F(a)$, $P(X > a) = 1 - F(a)$, $P(a < X \le b) = F(b) - F(a)$ ; la densité est $F'$.

</details>
<details><summary>Indice 3</summary>

4 : résous $\frac{m^2}{4} = \frac{1}{2}$. 5 : dérive $\frac{x^2}{4}$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M02a.R1 — Dériver une composée (R7)

<details><summary>Indice 1</summary>

Relis la règle de la chaîne (R7) : $(g(u(x)))' = g'(u(x))\,u'(x)$.

</details>
<details><summary>Indice 2</summary>

Repère la fonction extérieure (puissance, ln, exp, racine) et la fonction intérieure.

</details>
<details><summary>Indice 3</summary>

1 : $4u^3 \times u'$ avec $u = 3 - x^2$. 2 : la dérivée de $\ln u$ est $\frac{u'}{u}$, attention au signe de $u'$. 4 : $\sqrt{u}$ a pour dérivée $\frac{u'}{2\sqrt{u}}$.

</details>

### M02a.R2 — Sommes Σ (R4)

<details><summary>Indice 1</summary>

Relis la notation $\Sigma$ (R4) : l'indice, ses bornes, le terme général.

</details>
<details><summary>Indice 2</summary>

Écris les termes un par un avant d'additionner.

</details>
<details><summary>Indice 3</summary>

3 : les points sont $0{,}5 \times i$ pour $i = 0, 1, 2, 3$. 4 : la formule $\frac{n(n + 1)}{2}$.

</details>

### M02a.R3 — Exponentielle et logarithme (R6)

<details><summary>Indice 1</summary>

Relis les limites de $e^x$ et les croissances comparées (R6).

</details>
<details><summary>Indice 2</summary>

$e^{\ln a} = a$ et $\ln(e^b) = b$ ; l'exponentielle l'emporte sur toute puissance.

</details>
<details><summary>Indice 3</summary>

4 : prends le logarithme des deux membres : $-2x = \ln\frac{1}{4}$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M02a.1 — Sommes de Riemann à la main : rectangles à gauche, à droite, au milieu

<details><summary>Indice 1</summary>

Relis « Les sommes de Riemann » (fiche §1) et son exemple.

</details>
<details><summary>Indice 2</summary>

Commence par le tableau des valeurs de $f(x) = (2 - x)^3$ aux points $0$ ; $0{,}5$ ; $1$ ; $1{,}5$ ; $2$ (et aux milieux pour d) : $(2 - 0{,}5)^3 = 1{,}5^3$, etc. Chaque somme : $h$ fois la somme des hauteurs.

</details>
<details><summary>Indice 3</summary>

g : écris $L_n$ et $R_n$ l'une sous l'autre : tous les termes sont communs sauf $h\,f(0)$ et $h\,f(2)$, et $h = \frac{2}{n}$. h : $f$ est décroissante.

</details>

### Ex M02a.2 — Primitives usuelles

<details><summary>Indice 1</summary>

Relis la table des primitives (fiche §2), surtout la dernière ligne, $f(ax + b)$.

</details>
<details><summary>Indice 2</summary>

Écris chaque puissance sous la forme $x^n$, puis applique $\frac{x^{n+1}}{n+1}$. Vérifie chaque réponse en la dérivant.

</details>
<details><summary>Indice 3</summary>

b : $x^{-3}$, donc $n + 1 = -2$. c : $x^{1/2}$, donc $n + 1 = \frac{3}{2}$. g : écris les primitives $x^3 + x + C$, puis choisis $C$ avec $F(1) = 0$.

</details>

### Ex M02a.3 — Intégrales et aires : le signe, l'aire entre deux courbes

<details><summary>Indice 1</summary>

Relis « Le théorème fondamental », « Les règles de calcul » et « L'aire entre deux courbes » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Une primitive, puis $F(b) - F(a)$. Pour une aire géométrique : coupe là où la fonction change de signe, et additionne les valeurs absolues.

</details>
<details><summary>Indice 3</summary>

e : $x^2 - 2x = x(x - 2)$ change de signe en 0. g : sur $[0 ; 2]$, laquelle des deux courbes est au-dessus ? Essaie $x = 1$. h : une primitive de $\sin$ est $-\cos$.

</details>

### Ex M02a.4 — Intégration par parties

<details><summary>Indice 1</summary>

Relis « Intégration par parties » (fiche §3) et son exemple $\int_0^1 x\,e^{-x}\,dx$.

</details>
<details><summary>Indice 2</summary>

Choisis $u$ qui se simplifie en dérivant (le polynôme, ou $\ln x$) et $v'$ facile à intégrer. Écris $u$, $u'$, $v'$, $v$ avant la formule.

</details>
<details><summary>Indice 3</summary>

d : $u = \ln x$, $v' = 1$, donc $v = x$. f : une première intégration par parties avec $u = x^2$, puis une seconde avec $u = x$ ; garde le facteur 2.

</details>

### Ex M02a.5 — Changement de variable

<details><summary>Indice 1</summary>

Relis « Changement de variable » (fiche §3) et son exemple.

</details>
<details><summary>Indice 2</summary>

Repère une expression $g(x)$ dont la dérivée apparaît en facteur ; pose $u = g(x)$, remplace $g'(x)\,dx$ par $du$, et change les bornes.

</details>
<details><summary>Indice 3</summary>

b : $u = x^3 + 1$. c : $u = x^2 + 4$, il reste un facteur $\frac{1}{2}$. e : $u = x^2$. f : $u = \ln x$, $du = \frac{dx}{x}$.

</details>

### Ex M02a.6 — Intégrales impropres : converge, diverge, valeur

<details><summary>Indice 1</summary>

Relis le §4 : une intégrale impropre est une limite.

</details>
<details><summary>Indice 2</summary>

Calcule l'intégrale jusqu'à une borne $b$ (ou depuis $\varepsilon$), puis fais tendre $b$ vers $+\infty$ (ou $\varepsilon$ vers 0).

</details>
<details><summary>Indice 3</summary>

d : la règle $p > 1$. f : écris l'ensemble des $p$ qui conviennent sous forme d'intervalle. h : $e^{-x^2}$ est paire.

</details>

### Ex M02a.7 — Trapèzes et Simpson à la main, et leurs erreurs

<details><summary>Indice 1</summary>

Relis « Trois méthodes » (fiche §5) et l'exemple de $\ln 2$.

</details>
<details><summary>Indice 2</summary>

Calcule d'abord $f$ en $0$ ; $0{,}25$ ; $0{,}5$ ; $0{,}75$ ; $1$, avec 6 décimales. Trapèzes : les extrémités comptent pour moitié. Simpson : poids $1, 4, 2, 4, 1$, le tout fois $\frac{h}{3}$.

</details>
<details><summary>Indice 3</summary>

b : $\frac{0{,}5}{3}(4 + 4 \times 3{,}2 + 2)$, à écrire en fraction. e : divise l'erreur de $T_2$ par celle de $T_4$.

</details>

### Ex M02a.8 — Vérifier qu'une fonction est une densité, trouver sa constante

<details><summary>Indice 1</summary>

Relis « Définition » (fiche §6) et l'exemple de $c\,(1 - x^2)$.

</details>
<details><summary>Indice 2</summary>

Calcule l'intégrale sans la constante, puis choisis $c$ pour que $c \times$ (cette intégrale) vaille 1. Pour e et f, vérifie les deux conditions.

</details>
<details><summary>Indice 3</summary>

b : $\int_0^{+\infty} e^{-2x}\,dx = \frac{1}{2}$ (fiche §4). e : regarde le signe de $g$ en $x = 0{,}5$. g : avec $c = \frac{1}{8}$, une primitive de $\frac{x}{8}$ est $\frac{x^2}{16}$.

</details>

### Ex M02a.9 — La probabilité d'un intervalle, et la valeur moyenne d'une fonction

<details><summary>Indice 1</summary>

Relis le §6 (probabilité d'un intervalle) et « La valeur moyenne d'une fonction » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Pour $X$, une primitive de $\frac{3}{8}x^2$ est $\frac{x^3}{8}$. Pour $T$, une primitive de $0{,}2\,e^{-0{,}2t}$ est $-e^{-0{,}2t}$. Valeur moyenne : l'intégrale divisée par la longueur de l'intervalle.

</details>
<details><summary>Indice 3</summary>

d : les inégalités strictes ne changent rien. e : une intégrale jusqu'à $+\infty$, la limite de $-e^{-0{,}2b}$ vaut 0. h : $\frac{1}{e - 1}\big[\ln x\big]_1^e$.

</details>

### Ex M02a.10 — Fonction de répartition, médiane et percentiles d'une loi donnée

<details><summary>Indice 1</summary>

Relis « La fonction de répartition » et « Quantiles, médiane, percentiles » (fiche §7), avec l'exemple exponentiel.

</details>
<details><summary>Indice 2</summary>

$F(x) = \int_1^x \frac{2}{t^3}\,dt$ ; un quantile se trouve en résolvant $F(x) = p$. Pour $D$, $F(t) = 1 - e^{-0{,}25t}$.

</details>
<details><summary>Indice 3</summary>

c : $1 - \frac{1}{m^2} = \frac{1}{2}$. d : $\frac{1}{x^2} = 0{,}01$. f à h : $q_p = -4\ln(1 - p)$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M02a.11 — Le théorème fondamental : la dérivée d'une aire

<details><summary>Indice 1</summary>

Relis « Pourquoi ? » sous le théorème fondamental (fiche §2) et la figure de la fonction aire.

</details>
<details><summary>Indice 2</summary>

La bande entre $x$ et $x + h$ est coincée entre deux rectangles de largeur $h$ : l'un de hauteur $f(x)$, l'autre de hauteur $f(x + h)$.

</details>
<details><summary>Indice 3</summary>

Divise l'encadrement par $h > 0$ : $f(x) \le \frac{A(x + h) - A(x)}{h} \le f(x + h)$, puis fais tendre $h$ vers 0 (continuité de $f$, théorème des gendarmes). Pour la question 5, ne calcule pas $G$ : applique le résultat.

</details>

### Ex M02a.12 — Encadrer une aire par des rectangles : pourquoi les sommes de Riemann convergent (fonction croissante)

<details><summary>Indice 1</summary>

Relis le §1 (l'encadrement de l'aire de $x^2$ entre $L_4$ et $R_4$) et la question g de M02a.1.

</details>
<details><summary>Indice 2</summary>

Sur chaque petit intervalle, $f(x_i) \le f(t) \le f(x_{i+1})$ ; intègre, puis additionne.

</details>
<details><summary>Indice 3</summary>

Pour 2, écris $R_n = h(f(x_1) + \cdots + f(x_n))$ et $L_n = h(f(x_0) + \cdots + f(x_{n-1}))$ : les termes du milieu se simplifient. Pour 4, la borne vaut $\frac{e - 1}{n}$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M02a.13 — L'aire sous une courbe ROC donnée par une formule

<details><summary>Indice 1</summary>

Relis « L'AUC est une aire » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Chaque AUC est l'intégrale de la courbe entre 0 et 1. Pour A, intègre $1$ et $(1 - x)^3$ séparément.

</details>
<details><summary>Indice 3</summary>

a : une primitive de $(1 - x)^3$ est $-\frac{(1 - x)^4}{4}$. f : compare d) et e). g : trois points, deux trapèzes, extrémités pour moitié.

</details>

### Ex M02a.14 — MML §6.2 (la partie continue) : densité et fonction de répartition, en anglais

<details><summary>Indice 1</summary>

Lis le passage avec la fiche (§6 et §7) ouverte à côté.

</details>
<details><summary>Indice 2</summary>

Cherche les mots *probability density function* et *cumulative distribution function* : les définitions suivent.

</details>
<details><summary>Indice 3</summary>

Pour 4, pense à une loi uniforme sur un intervalle court. Pour 5, une loi discrète de R8, dont la fonction de répartition monte par marches.

</details>

### Ex M02a.15 — Expliquer pourquoi P(X = a) = 0 pour une variable continue

<details><summary>Indice 1</summary>

Relis « Trois conséquences qui surprennent » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Où se lit une probabilité ? Quelle est l'aire au-dessus d'un seul point ?

</details>
<details><summary>Indice 3</summary>

Une image possible : la largeur de la bande. Pense aussi à distinguer « impossible » et « de probabilité nulle ».

</details>

<a id="entretien"></a>

## 💼 Entretien

### M02a.E1 — Chaque valeur a une probabilité nulle : comment dire qu'une valeur est plus probable qu'une autre ?

<details><summary>Indice 1</summary>

Relis « Trois conséquences qui surprennent » (fiche §6), la deuxième.

</details>
<details><summary>Indice 2</summary>

La densité est une probabilité par unité de longueur : $P(x \le X \le x + h) \approx f(x)\,h$.

</details>
<details><summary>Indice 3</summary>

Compare deux petits intervalles de même largeur, l'un autour de 1,8, l'autre autour de 2,5 : le rapport de leurs probabilités est celui des densités.

</details>

<a id="notebook"></a>

## Notebook

### Ex M02a.16 — Rectangles et trapèzes · `riemann_sum`, `trapezoid`

<details><summary>Indice 1</summary>

Relis les formules de $L_n$, $R_n$, $M_n$ (fiche §1) et de $T_n$ (fiche §5).

</details>
<details><summary>Indice 2</summary>

Les trois règles ne diffèrent que par le point où l'on lit la hauteur : $a + (i + \text{décalage})\,h$, avec un décalage de 0, 1 ou 0,5. Teste `n` et `rule` avant de calculer.

</details>
<details><summary>Indice 3</summary>

`float(h * sum(f(a + (i + shift) * h) for i in range(n)))`. Pour les trapèzes : `h * ((f(a) + f(b)) / 2 + sum(f(a + i * h) for i in range(1, n)))`.

</details>

### Ex M02a.17 — La méthode de Simpson · `simpson`

<details><summary>Indice 1</summary>

Relis la formule de Simpson (fiche §5).

</details>
<details><summary>Indice 2</summary>

Les poids : 1 aux extrémités, 4 aux indices impairs, 2 aux indices pairs intérieurs ; le tout multiplié par $\frac{h}{3}$.

</details>
<details><summary>Indice 3</summary>

Une boucle `for i in range(1, n)` qui ajoute `(4 if i % 2 == 1 else 2) * f(a + i * h)` à `f(a) + f(b)`.

</details>

### Ex M02a.18 — De la densité à la fonction de répartition, puis au quantile par dichotomie · `cdf_from_pdf`, `quantile`

<details><summary>Indice 1</summary>

Relis la fin du §7 (« Quand l'équation $F(x) = p$ ne se résout pas à la main ») et la dichotomie de R7.

</details>
<details><summary>Indice 2</summary>

`cdf_from_pdf` : un appel à ta fonction `trapezoid`. `quantile` : garde un intervalle `[lo, hi]` avec `cdf(lo) < p <= cdf(hi)`, et coupe-le en deux.

</details>
<details><summary>Indice 3</summary>

Dans la boucle (200 tours au plus) : `mid = (lo + hi) / 2`, puis `lo = mid` si `cdf(mid) < p`, sinon `hi = mid` ; arrête quand `hi - lo < tol`.

</details>

### Ex M02a.19 — Vérifier avec `scipy.integrate.quad` et SymPy

<details><summary>Indice 1</summary>

Relis les exemples de code des §2 et §4.

</details>
<details><summary>Indice 2</summary>

`quad` rend un couple : `value, error = quad(...)`. SymPy : `sp.integrate(expr, (x, a, b))`, avec `sp.oo` pour l'infini.

</details>
<details><summary>Indice 3</summary>

d : `str(sp.integrate(4 / (1 + x ** 2), (x, 0, 1)))`. f : affiche `sp.integrate(sp.exp(-x ** 2), x)` et lis le nom de la fonction.

</details>

### Ex M02a.20 — Prédire : le pas divisé par 2, l'erreur divisée par combien ?

<details><summary>Indice 1</summary>

Relis « L'ordre d'une méthode » (fiche §5), et surtout l'hypothèse qui l'accompagne.

</details>
<details><summary>Indice 2</summary>

Les règles « ÷ 4 » et « ÷ 16 » supposent une fonction régulière. Qu'arrive-t-il à la dérivée de $\sqrt{x}$ en 0 ?

</details>
<details><summary>Indice 3</summary>

Pour d, dessine une fonction périodique et ses trapèzes sur une période : les surplus et les manques se compensent-ils ?

</details>

### Ex M02a.21 — L'intégrale de Gauss par le calcul : la borne qui s'éloigne

<details><summary>Indice 1</summary>

Relis « L'intégrale de Gauss » (fiche §4) et M02a.19 pour `quad`.

</details>
<details><summary>Indice 2</summary>

Écris une petite fonction `I(B)` qui renvoie `quad(lambda x: math.exp(-x ** 2), -B, B)[0]`.

</details>
<details><summary>Indice 3</summary>

b : `next(B for B in bounds if abs(I(B) - gauss) < 1e-6)`. Pour la borne de la copie : $\int_B^{+\infty} e^{-Bx}\,dx = \frac{e^{-B^2}}{B}$.

</details>

### Ex M02a.22 — L'aire qui se remplit : la courbe, les rectangles et la primitive

<details><summary>Indice 1</summary>

Relis « Les sommes de Riemann » (fiche §1) et « Le théorème fondamental » (fiche §2).

</details>
<details><summary>Indice 2</summary>

`ax.bar(lefts, heights, width=h, align="edge")` dessine des rectangles dont le bord gauche est en `lefts`. Pour la fonction aire : additionne les aires des petits trapèzes de la grille, une à une.

</details>
<details><summary>Indice 3</summary>

`pieces = (xs[1:] - xs[:-1]) * (ys[1:] + ys[:-1]) / 2`, puis `np.concatenate([[0.0], np.cumsum(pieces)])` : une valeur par point de la grille, en partant de 0.

</details>

### Ex M02a.23 — Chasse à l'erreur : bornes inversées, primitive fausse, aire négative

<details><summary>Indice 1</summary>

Relis les ⚠️ des §1 et §2.

</details>
<details><summary>Indice 2</summary>

Pour chaque calcul : l'ordre des bornes, la primitive (dérive-la), et la différence entre une intégrale et une aire.

</details>
<details><summary>Indice 3</summary>

(C) : la dérivée de $e^{-3x}$ vaut $-3e^{-3x}$. (D) : $x^2 - 1$ est-elle positive sur tout $[0 ; 2]$ ?

</details>

### Ex M02a.24 — Vérifier une primitive avec SymPy : dériver le résultat

<details><summary>Indice 1</summary>

Relis l'exemple SymPy du §2.

</details>
<details><summary>Indice 2</summary>

Dérive `F` avec `sp.diff(F, x)`, soustrais `f`, simplifie : une primitive donne 0.

</details>
<details><summary>Indice 3</summary>

`return bool(sp.simplify(sp.diff(F, x) - f) == 0)`.

</details>

### Ex M02a.25 — Défi : la meilleure précision avec dix évaluations de la fonction

<details><summary>Indice 1</summary>

Simpson avec 8 intervalles utilise 9 évaluations : c'est le point de départ. L'erreur de Simpson suit $h^4$ : que donne $\frac{16 S_8 - S_4}{15}$ (les points de $S_4$ sont parmi ceux de $S_8$) ?

</details>
<details><summary>Indice 2</summary>

Pour aller plus loin, abandonne les points réguliers : la quadrature de Gauss-Legendre place $n$ points et choisit $n$ poids pour être exacte sur les polynômes de degré au plus $2n - 1$. `np.polynomial.legendre.leggauss(10)` donne les points $t_i$ et les poids $w_i$ sur $[-1 ; 1]$.

</details>
<details><summary>Indice 3</summary>

Changement de variable affine (§3) : $x = \frac{a + b}{2} + \frac{b - a}{2}t$, donc $\int_a^b f(x)\,dx = \frac{b - a}{2}\int_{-1}^1 f\big(\tfrac{a + b}{2} + \tfrac{b - a}{2}t\big)\,dt \approx \frac{b - a}{2}\sum_i w_i\,f\big(\tfrac{a + b}{2} + \tfrac{b - a}{2}t_i\big)$.

</details>
