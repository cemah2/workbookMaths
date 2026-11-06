# R7 · Limites et dérivation — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R7.Q1 — Limites : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Les règles de calcul, et les formes indéterminées » et « Quand x s'approche d'un point » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Pour une fraction en l'infini, compare les degrés ; pour une forme ∞ − ∞, cherche deux exemples qui donnent des résultats différents ; pour une limite en un point, regarde le signe du dénominateur de chaque côté.

</details>
<details><summary>Indice 3</summary>

1 : **vrai**. Pour 2, essaie $f(x) = x^2$ et $g(x) = x$. Pour 7, que vaut $\frac{1}{x}$ pour $x = -0{,}001$ ?

</details>

### R7.Q2 — Continue ou pas ?

<details><summary>Indice 1</summary>

Relis « Une fonction sans saut » et le théorème des valeurs intermédiaires (fiche §2).

</details>
<details><summary>Indice 2</summary>

Les valeurs intermédiaires demandent la **continuité** ; la dichotomie demande en plus un **changement de signe** aux deux bouts.

</details>
<details><summary>Indice 3</summary>

1 : la valeur absolue n'a pas de saut, donc **oui**. Pour 4, imagine une fonction qui saute de −1 à 1. Pour 5, la longueur est divisée par 2 à chaque étape.

</details>

### R7.Q3 — Le nombre dérivé est une pente

<details><summary>Indice 1</summary>

Relis « Le nombre dérivé » (fiche §3) et « L'approximation affine » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$f'(a)$ est la pente de la tangente ; $f(a + h) \approx f(a) + f'(a)\,h$ ; l'unité d'une dérivée est celle de $f$ divisée par celle de $x$.

</details>
<details><summary>Indice 3</summary>

1 : la pente de la tangente au point d'abscisse $a$. Pour 3, $h = 0{,}1$. Pour 5, pense à $\lvert x \rvert$ en 0.

</details>

### R7.Q4 — Dérivées usuelles

<details><summary>Indice 1</summary>

Relis le tableau du §5.

</details>
<details><summary>Indice 2</summary>

$(x^n)' = nx^{n-1}$ vaut aussi pour les exposants négatifs ; $\frac{1}{x} = x^{-1}$ et $\sqrt{x} = x^{1/2}$.

</details>
<details><summary>Indice 3</summary>

1 : $8x^7$. Pour 7, l'exposant −3 descend devant, et devient −4.

</details>

### R7.Q5 — Produit, quotient : quelle formule ?

<details><summary>Indice 1</summary>

Relis le §6 et son encadré ⚠️.

</details>
<details><summary>Indice 2</summary>

$(uv)' = u'v + uv'$ ; $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$, avec $u'v$ en premier.

</details>
<details><summary>Indice 3</summary>

1 : **faux** ($(x \times x)' = 2x$, pas 1). Pour 5, simplifie d'abord $\frac{x + 1}{x}$.

</details>

### R7.Q6 — Règle de la chaîne : qu'y a-t-il « dedans » ?

<details><summary>Indice 1</summary>

Relis « La méthode en trois temps » (fiche §7).

</details>
<details><summary>Indice 2</summary>

L'étage extérieur est l'opération faite **en dernier** quand on calcule la valeur ; l'intérieur est ce qu'on lui donne.

</details>
<details><summary>Indice 3</summary>

1 : pour calculer $(2x - 7)^6$, on calcule d'abord $u = 2x - 7$, puis $u^6$. Fais de même pour les autres.

</details>

### R7.Q7 — Dérivée nulle, extremum ?

<details><summary>Indice 1</summary>

Relis « Extremums : dérivée nulle, mais pas seulement » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Un extremum demande que $f'$ **change de signe** ; il peut aussi se trouver au bord d'un intervalle ou en un coin.

</details>
<details><summary>Indice 3</summary>

1 : $(x^7)' = 7x^6$ : change-t-elle de signe en 0 ? Pour 3, une fonction croissante atteint son maximum… où ?

</details>

### R7.Q8 — Qui domine qui ?

<details><summary>Indice 1</summary>

Relis « La notation grand O » (fiche §9).

</details>
<details><summary>Indice 2</summary>

On garde le terme qui domine et on oublie son coefficient ; $f = O(g)$ demande que $\frac{f}{g}$ reste borné.

</details>
<details><summary>Indice 3</summary>

1 : $3n^2 + 100n \le 4n^2$ dès que $n$ est assez grand : **vrai**. Pour 6, que devient $n^2$ quand $n$ est multiplié par 10 ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### R7.R1 — Croissances comparées (R6)

<details><summary>Indice 1</summary>

Relis l'encadré « Croissances comparées » de la fiche de R6 (§5).

</details>
<details><summary>Indice 2</summary>

L'exponentielle l'emporte sur toute puissance ; toute puissance (même petite) l'emporte sur ln.

</details>
<details><summary>Indice 3</summary>

1 : $\frac{x^3}{e^x} \to 0$. Pour 3, place $\ln x$ en premier.

</details>

### R7.R2 — Limite d'une suite (R5)

<details><summary>Indice 1</summary>

Relis le §5 de la fiche de R5 (limite d'une suite).

</details>
<details><summary>Indice 2</summary>

Divise par $n$ ; une suite géométrique de raison entre 0 et 1 tend vers 0 ; la troisième définit $e$ (R6 §2).

</details>
<details><summary>Indice 3</summary>

1 : $\frac{2n + 1}{n} = 2 + \frac{1}{n}$.

</details>

### R7.R3 — Sommet d'une parabole (R3)

<details><summary>Indice 1</summary>

Relis la forme canonique et le sommet (fiche de R3).

</details>
<details><summary>Indice 2</summary>

Le sommet de $ax^2 + bx + c$ est en $x = -\frac{b}{2a}$ ; c'est un minimum si $a > 0$, un maximum si $a < 0$.

</details>
<details><summary>Indice 3</summary>

1 : $x = 3$, puis calcule $y$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R7.1 — Limites en l'infini des fonctions de référence

<details><summary>Indice 1</summary>

Relis « Les règles de calcul, et les formes indéterminées » (fiche §1) et les croissances comparées de R6.

</details>
<details><summary>Indice 2</summary>

Repère d'abord les formes indéterminées ; pour une fraction de polynômes, mets en facteur le terme de plus haut degré en haut et en bas ; pour un mélange d'exponentielle, de puissance et de ln, ce sont les croissances comparées qui décident.

</details>
<details><summary>Indice 3</summary>

a : $\frac{3}{x} \to 0$, donc la limite est 5. Pour b, $x^3 - 100x^2 = x^3(1 - \frac{100}{x})$. Pour h, quel est le signe de $x^3$ quand $x$ est très négatif ?

</details>

### Ex R7.2 — Limites et asymptotes de fonctions rationnelles

<details><summary>Indice 1</summary>

Relis « Quand x s'approche d'un point » et « Les asymptotes » (fiche §1).

</details>
<details><summary>Indice 2</summary>

En un point où le dénominateur s'annule : calcule la limite du numérateur, puis le signe du dénominateur de chaque côté. Si le numérateur s'annule aussi, factorise.

</details>
<details><summary>Indice 3</summary>

a : même degré, $\frac{3}{1}$. Pour b, le numérateur tend vers −5 et le dénominateur $x + 1$ est positif quand $x > -1$. Pour e, cherche les racines de $x^2 + x - 6$.

</details>

### Ex R7.3 — Taux d'accroissement et nombre dérivé

<details><summary>Indice 1</summary>

Relis « Une vitesse moyenne » et « Le nombre dérivé » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Taux $= \frac{f(a + h) - f(a)}{h}$ ; pour l'avoir en fonction de $h$, développe $f(4 + h)$ et simplifie par $h$ ; sa limite quand $h \to 0$ est le nombre dérivé.

</details>
<details><summary>Indice 3</summary>

a : $f(5) = 0$ et $f(4) = -4$, donc $\frac{0 - (-4)}{1} = 4$. Pour c, divise par $-0{,}5$. Pour g, calcule le taux de $s$ entre 2 et $2 + h$, puis fais tendre $h$ vers 0.

</details>

### Ex R7.4 — Équation de la tangente

<details><summary>Indice 1</summary>

Relis « L'équation de la tangente » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$y = f(a) + f'(a)(x - a)$, puis développe pour l'écrire $y = mx + p$ ; une tangente horizontale a une pente nulle.

</details>
<details><summary>Indice 3</summary>

a : $f(4) = -4$, $f'(4) = 3$, donc $y = -4 + 3(x - 4) = 3x - 16$. Pour e, remplace $x$ par 4,2 dans la tangente de d. Pour h, écris la tangente, puis résous $y = 0$.

</details>

### Ex R7.5 — Dériver les fonctions usuelles

<details><summary>Indice 1</summary>

Relis le tableau du §5 et « Somme et constante » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Écris chaque terme comme une puissance de $x$ quand c'est possible ($\frac{1}{x^3} = x^{-3}$, $x\sqrt{x} = x^{3/2}$) ; pour g et h, utilise d'abord les propriétés de ln et de exp de R6.

</details>
<details><summary>Indice 3</summary>

a : $7x^6$. Pour d, $x \times x^{1/2} = x^{3/2}$. Pour g, $\ln(5x) = \ln 5 + \ln x$.

</details>

### Ex R7.6 — Dériver des produits et des quotients

<details><summary>Indice 1</summary>

Relis « Produit » et « Quotient » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Nomme $u$ et $v$, calcule $u'$ et $v'$, puis applique la formule ; pour un quotient, $u'v$ vient en premier au numérateur, et le dénominateur est $v^2$.

</details>
<details><summary>Indice 3</summary>

a : $u = x^3$, $v = \ln x$, donc $3x^2 \ln x + x^3 \times \frac{1}{x}$. Pour d, $u' = 1$ et $v' = 2$. Pour h, $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$.

</details>

### Ex R7.7 — Dériver des composées

<details><summary>Indice 1</summary>

Relis « La méthode en trois temps » et le tableau des formes à reconnaître (fiche §7).

</details>
<details><summary>Indice 2</summary>

Nomme l'étage intérieur $u$, dérive l'extérieur par rapport à $u$, multiplie par $u'$, puis remplace $u$.

</details>
<details><summary>Indice 3</summary>

a : $u = 2x^2 - 1$, $u' = 4x$, et $(u^3)' = 3u^2 u'$. Pour f, $u = \ln x$. Pour h, dérive d'abord, remplace $x$ par 1 ensuite.

</details>

### Ex R7.8 — Variations et tableau de variations

<details><summary>Indice 1</summary>

Relis « Le tableau de variations » et « Extremums : dérivée nulle, mais pas seulement » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Factorise $f'(x)$, étudie son signe, puis calcule $f$ aux points où il change ; sur un intervalle fermé, compare aussi les valeurs aux bords.

</details>
<details><summary>Indice 3</summary>

a : $f'(x) = 6x^2 + 6x - 12 = 6(x^2 + x - 2)$. Pour f, calcule $f(-3)$, $f(-2)$, $f(1)$ et $f(3)$. Pour g, $g'(x) = 1 - \frac{2}{x}$.

</details>

### Ex R7.9 — Optimiser : la boîte de volume maximal

<details><summary>Indice 1</summary>

Relis « Un problème d'optimisation » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Les trois dimensions doivent être positives ; développe $V$, dérive, factorise $V'$, et ne garde que la racine du domaine.

</details>
<details><summary>Indice 3</summary>

a : il faut $x > 0$ et $10 - 2x > 0$. Pour c, $V'(x) = 4(3x^2 - 26x + 40)$ : cherche ses racines. Pour f, la longueur est $16 - 2x$.

</details>

### Ex R7.10 — La règle de la chaîne en série : trois étages, et l'ordre qui compte

<details><summary>Indice 1</summary>

Relis « Plus de deux étages » et l'encadré ⚠️ sur l'ordre de la composition (fiche §7).

</details>
<details><summary>Indice 2</summary>

Nomme chaque étage, de l'intérieur vers l'extérieur, et multiplie toutes les dérivées. Pour d, simplifie d'abord avec $\ln(a^2) = 2\ln a$.

</details>
<details><summary>Indice 3</summary>

a : $v = x^2 + 1$, $u = v^3$, $z = e^u$, donc $\frac{dz}{dx} = e^u \times 3v^2 \times 2x$. Pour h, $(e^x)^2 = e^{2x}$, alors que dans $e^{x^2}$ c'est $x$ qui est au carré.

</details>

### Ex R7.11 — Dériver par rapport à une lettre, les autres fixées : A e^(kt), π r² h, ½ m v²

<details><summary>Indice 1</summary>

Relis « Dériver par rapport à une lettre, les autres fixées » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Toutes les lettres autres que celle par rapport à laquelle on dérive sont des constantes : elles restent en facteur, ou disparaissent si elles sont ajoutées.

</details>
<details><summary>Indice 3</summary>

a : par rapport à $t$, $A$ reste devant et $(e^{kt})' = k\,e^{kt}$. Pour b, l'exposant $kt$ a pour dérivée $t$ par rapport à $k$. Pour d, $\pi h$ est une constante.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R7.12 — La dérivée de x² à partir de la définition, et |x| qui n'est pas dérivable en 0

<details><summary>Indice 1</summary>

Relis la définition du nombre dérivé (fiche §3) et « Dérivable ou non ».

</details>
<details><summary>Indice 2</summary>

Développe $(a + h)^2$ et simplifie par $h \ne 0$. Pour $\lvert h \rvert$, distingue $h > 0$ et $h < 0$.

</details>
<details><summary>Indice 3</summary>

1 : $\frac{(a + h)^2 - a^2}{h} = \frac{2ah + h^2}{h}$. Pour 3, $\lvert h \rvert = h$ si $h > 0$, $-h$ si $h < 0$. Pour 5, si $a > 0$ et $h$ petit, $a + h$ est encore positif.

</details>

### Ex R7.13 — Démontrer la règle du produit

<details><summary>Indice 1</summary>

Relis la définition du nombre dérivé (fiche §3), et la récurrence (R4 §7).

</details>
<details><summary>Indice 2</summary>

L'égalité de 2 ajoute et retire $u(a)v(a + h)$ ; il reste à diviser par $h$ et à prendre la limite de chaque morceau.

</details>
<details><summary>Indice 3</summary>

1 : $h \to 0$ et $\frac{v(a + h) - v(a)}{h} \to v'(a)$, donc le produit tend vers 0. Pour 4, $(x^{n+1})' = (x^n \times x)'$.

</details>

### Ex R7.14 — La règle du quotient à partir de la règle du produit : (1/v)′ = −v′/v²

<details><summary>Indice 1</summary>

Relis « Quotient » (fiche §6).

</details>
<details><summary>Indice 2</summary>

La dérivée de la constante 1 est 0 ; la règle du produit appliquée à $v \times \frac{1}{v}$ donne une équation dont l'inconnue est $\left(\frac{1}{v}\right)'$.

</details>
<details><summary>Indice 3</summary>

1 : $v' \times \frac{1}{v} + v \times \left(\frac{1}{v}\right)' = 0$. Pour 3, écris $\frac{u}{v} = u \times \frac{1}{v}$ et réduis au dénominateur $v^2$.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R7.15 — Minimiser une fonction de coût donnée par une formule : dériver, annuler, vérifier

<details><summary>Indice 1</summary>

Relis « Le signe de la dérivée » et « Un problème d'optimisation » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Dérive, résous $E'(a) = 0$ dans le domaine $a > 0$, puis vérifie le signe de $E'$ de part et d'autre ; pour $L$, multiplie l'équation $L'(t) = 0$ par $e^{t}$.

</details>
<details><summary>Indice 3</summary>

a : $(2a)' = 2$ et $\left(\frac{8}{a}\right)' = -\frac{8}{a^2}$. Pour e, $e^t - 4e^{-t} = 0$ donne $e^{2t} = 4$. Pour g, calcule $L$ en $t^* - 0{,}1$ et en $t^* + 0{,}1$ à la calculatrice.

</details>

### Ex R7.16 — Expliquer ce qu'est une dérivée sans écrire de formule

<details><summary>Indice 1</summary>

Relis les débuts du §3 et du §4.

</details>
<details><summary>Indice 2</summary>

Pars d'une vitesse lue sur un compteur ; dis ce que mesure une dérivée (une variation rapportée à une petite variation), puis ce que disent son signe et sa taille.

</details>
<details><summary>Indice 3</summary>

Par exemple : « une vitesse, c'est de combien la distance change pour une seconde de plus, mesuré sur un temps très court » ; puis la pente d'un chemin, et le fond d'une vallée, où la pente est nulle.

</details>

<a id="notebook"></a>

## Notebook

### Ex R7.17 — Le taux d'accroissement · `difference_quotient`

<details><summary>Indice 1</summary>

Relis « Une vitesse moyenne » (fiche §3) et la docstring de `difference_quotient`.

</details>
<details><summary>Indice 2</summary>

D'abord le cas interdit (`h == 0`) avec `raise ValueError(...)` ; puis une ligne : la formule du taux, convertie en `float`.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
if h == 0:
    raise ValueError("...")
return float(...)
```
Pour d, essaie de deviner la dérivée à partir du taux, puis écris $x^x = e^{x \ln x}$.

</details>

### Ex R7.18 — La tangente à partir de f et de sa dérivée · `tangent_line`

<details><summary>Indice 1</summary>

Relis « L'équation de la tangente » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Développe $y = f(a) + f'(a)(x - a)$ : la pente est $f'(a)$, l'ordonnée à l'origine $f(a) - f'(a) \times a$. Pas de conversion en flottant.

</details>
<details><summary>Indice 3</summary>

Calcule d'abord `m = df(a)` ; l'ordonnée à l'origine s'écrit avec `f(a)`, `m` et `a`. Renvoie le couple `(m, c)`.

</details>

### Ex R7.19 — Trouver un zéro par dichotomie · `bisection`

<details><summary>Indice 1</summary>

Relis « La dichotomie : couper en deux » (fiche §2) et toute la docstring de `bisection`.

</details>
<details><summary>Indice 2</summary>

Dans l'ordre : les vérifications (`a >= b`, une borne où `f` vaut 0, deux signes stricts identiques) ; puis une boucle d'au plus `max_iter` tours, qui s'arrête dès que `b - a < tol`, coupe en deux et garde la moitié où le signe change ; enfin le milieu.

</details>
<details><summary>Indice 3</summary>

Dans la boucle :
```python
m = (a + b) / 2
if f(m) == 0:
    return m
# garde [a, m] ou [m, b] selon le signe de f(m) comparé à celui de f(a)
```
Pour g, cherche le plus petit $n$ tel que $2^{-n} < 10^{-10}$.

</details>

### Ex R7.20 — Vérifier ses dérivées avec `sympy.diff`

<details><summary>Indice 1</summary>

Relis l'énoncé : chaque fonction de SymPy y est nommée ; et le bloc Python du §6 de la fiche.

</details>
<details><summary>Indice 2</summary>

a et b : `sp.diff`, puis `sp.solve(…, x)` ; c : pour chaque couple de `proposals`, compare la dérivée de SymPy à la proposée avec `sp.simplify(…) == 0` ; d : `sp.limit`.

</details>
<details><summary>Indice 3</summary>

a : `sp.diff(x**2 * sp.exp(-x), x)`. Pour c, une compréhension de liste sur `for f, proposed in proposals`. Pour d, `sp.sqrt` et le troisième argument 0.

</details>

### Ex R7.21 — Prédire : le taux d'accroissement s'approche-t-il toujours de la dérivée quand h devient minuscule ?

<details><summary>Indice 1</summary>

Relis l'arrondi des flottants (fiche de R1) : un flottant garde environ 16 chiffres significatifs.

</details>
<details><summary>Indice 2</summary>

Le numérateur $e^{1 + h} - e$ est la différence de deux nombres presque égaux : combien de ses chiffres restent justes quand $h$ est minuscule ? Et que vaut `1 + 1e-16` ?

</details>
<details><summary>Indice 3</summary>

Écris tes prédictions, même incertaines : l'expérience tranchera. Puis, pour la copie, tape `1 + 1e-16 == 1` dans une cellule.

</details>

### Ex R7.22 — Zoomer sur une courbe jusqu'à voir une droite

<details><summary>Indice 1</summary>

Relis « L'approximation affine » et le zoom (fiche §4), puis le calcul vectorisé (workbookIA 0A §100.8.3).

</details>
<details><summary>Indice 2</summary>

Une grille `np.linspace(a - w, a + w, 1001)`, les valeurs de `f` et de `line` sur toute la grille d'un coup, l'écart en valeur absolue, puis son maximum.

</details>
<details><summary>Indice 3</summary>

`xs = np.linspace(a - w, a + w, 1001)`, puis `np.abs(...)` et `np.max(...)`. Pour d, regarde les quatre rapports de b.

</details>

### Ex R7.23 — Tracer f, f′ et des tangentes

<details><summary>Indice 1</summary>

Relis « L'équation de la tangente » (fiche §4) et le tableau de variations (fiche §8) ; pour les axes, le tracé de R3.

</details>
<details><summary>Indice 2</summary>

Dans `axes[0]` : une grille pour la courbe, puis, pour chaque `p`, un petit segment de la tangente et le point de contact ; dans `axes[1]` : `df` et `axes[1].axhline(0)` ; un titre pour chacun.

</details>
<details><summary>Indice 3</summary>

Pour chaque `p` :
```python
segment = np.linspace(p - 0.6, p + 0.6, 2)
axes[0].plot(segment, f(p) + df(p) * (segment - p), "--")
```
Pour a, factorise $f'(x) = 4x^3 - 8x$.

</details>

### Ex R7.24 — Chasse à l'erreur : quatre dérivées fausses

<details><summary>Indice 1</summary>

Relis les §6 et §7 et leurs encadrés ⚠️.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, demande-toi si la fonction est un produit, un quotient ou une composée, et si la règle correspondante est appliquée en entier. Puis compare chaque dérivée à `slope(f, 2)`.

</details>
<details><summary>Indice 3</summary>

(A) : $x^4 \ln x$ est un produit ; la ligne n'écrit qu'un produit de dérivées. Pour chacune des autres, nomme l'étage intérieur et sa dérivée.

</details>

### Ex R7.25 — Tester une dérivée avec pytest et SymPy

<details><summary>Indice 1</summary>

Relis la règle du quotient (fiche §6) et les tests de R0 (`assert`, `math.isclose`).

</details>
<details><summary>Indice 2</summary>

`dg` : la dérivée simplifiée, en une ligne. Le test : un symbole `X = sp.symbols("x")`, la dérivée exacte `sp.diff(...)`, puis une boucle sur quelques points avec un `assert`.

</details>
<details><summary>Indice 3</summary>

Dans le test :
```python
exact = sp.diff((X ** 2 + 1) / (X + 3), X)
for point in (...):
    assert math.isclose(dg(point), float(exact.subs(X, point)), rel_tol=1e-12)
```
Choisis des points variés, dont un négatif, et pas −3.

</details>
