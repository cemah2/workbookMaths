# R7 · Limites et dérivation — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R7.Q1 — Limites : vrai ou faux
1. **Vrai** : $x^2$ devient très grand, son inverse très petit.
2. **Faux** : $\infty - \infty$ est une forme indéterminée. Avec $f(x) = x^2$ et $g(x) = x$, $f - g = x^2 - x \to +\infty$ ; avec $f = x + 1$ et $g = x$, $f - g = 1$.
3. **Faux** : le dénominateur a le plus grand degré, la limite est 0 ($\frac{3x^2 + 1}{x^3} = \frac{3}{x} + \frac{1}{x^3}$).
4. **Vrai** : l'exponentielle l'emporte sur toute puissance (R6 §5).
5. **Vrai** : en 4, le dénominateur s'annule et le numérateur vaut 1 ; la fonction tend vers $\pm\infty$.
6. **Vrai** : $\frac{x^2 - 9}{x - 3}$ n'est pas définie en 3, mais tend vers 6 (fiche §1).
7. **Faux** : pour $x < 0$ proche de 0, $\frac{1}{x}$ est très négatif : la limite à gauche est $-\infty$.

### R7.Q2 — Continue ou pas ?
1. **Oui** : $\frac{1}{x}$ est continue sur $]-\infty \;;\; 0[$ et sur $]0 \;;\; +\infty[$. En 0, elle n'est pas définie : la question ne s'y pose pas (et la courbe y est coupée en deux morceaux).
2. **Non** en 0, où elle saute de 0 à 1 ; **oui** en 0,5, où elle vaut 1 tout autour.
3. **Oui** : 3 est entre $-2$ et 5, et $f$ est continue (théorème des valeurs intermédiaires).
4. **Faux** : sans continuité, rien n'oblige à passer par 0. La fonction qui vaut −1 sur $[0 \;;\; 0{,}5[$ et 1 sur $[0{,}5 \;;\; 1]$ ne s'annule jamais.
5. $\frac{1}{2^{10}} = \frac{1}{1\,024} \approx 0{,}001$.
6. **Faux** : $x^2$ vaut 1 en −1 et 4 en 2, sans changement de signe ; la dichotomie n'a rien à couper (et `bisection` lève une `ValueError`), bien que 0 soit un zéro. Un zéro où la courbe touche l'axe sans le traverser lui échappe.

### R7.Q3 — Le nombre dérivé est une pente
1. **Vrai** : c'est la pente de la **sécante** qui passe par $(a \;;\; f(a))$ et $(a + h \;;\; f(a + h))$.
2. Elle **monte** : la pente de sa tangente en −1 est positive.
3. $f(5{,}1) \approx f(5) + f'(5) \times 0{,}1 = 2 + 0{,}4 = $ **2,4**.
4. **Faux** : $y = f(a) + f'(a)(x - a)$ ; sans $f(a)$, la droite passe par $(a \;;\; 0)$ au lieu du point de la courbe.
5. **Faux** : $\lvert x \rvert$ est continue en 0, mais n'y est pas dérivable (R7.12).
6. Des **km/h** : une distance divisée par une durée.

### R7.Q4 — Dérivées usuelles
1. $8x^7$. 2. $-\frac{1}{x^2}$. 3. $\frac{1}{2\sqrt{x}}$. 4. $e^x$. 5. $\frac{1}{x}$. 6. $0$. 7. $-3x^{-4} = -\frac{3}{x^4}$.

### R7.Q5 — Produit, quotient : quelle formule ?
1. **Faux** : $(uv)' = u'v + uv'$.
2. **Vrai**.
3. **Faux** : c'est $\frac{u'v - uv'}{v^2}$ ; l'écriture proposée en est l'opposé.
4. **Vrai**.
5. **Faux** : $\frac{x + 1}{x} = 1 + \frac{1}{x}$, de dérivée $-\frac{1}{x^2}$.
6. **Vrai** : une constante ajoutée a une dérivée nulle.

### R7.Q6 — Règle de la chaîne : qu'y a-t-il « dedans » ?
1. $u = 2x - 7$, puis $u^6$. 2. $u = x^3$, puis $e^u$. 3. $u = 4 - x$, puis $\ln u$. 4. $u = e^x + 1$, puis $\sqrt{u}$. 5. $u = e^x + x$, puis $u^3$.
6. **Faux** : $\ln(2x) = \ln 2 + \ln x$ a pour dérivée $\frac{1}{x}$ ; par la règle de la chaîne aussi, $\frac{2}{2x} = \frac{1}{x}$. Oublier la dérivée de l'intérieur donne $\frac{1}{2x}$.

### R7.Q7 — Dérivée nulle, extremum ?
1. **Non** : $(x^3 + x)' = 3x^2 + 1 > 0$ partout ; la fonction ne fait que monter, et sa dérivée ne s'annule même pas.
2. Un **maximum** local : $f$ monte, puis descend.
3. **En 4** : $f$ est strictement croissante sur $[0 \;;\; 4]$, son maximum est au bord droit.
4. **Vrai** : $\lvert x \rvert \ge 0 = \lvert 0 \rvert$ ; un extremum peut se trouver en un coin.
5. $f(0{,}5) > f(1{,}5)$ : $f$ décroît sur $]0 \;;\; 2[$.
6. **Faux** : il est le plus grand **au voisinage** du point ; ailleurs, $f$ peut prendre des valeurs plus grandes (fiche §8 : le maximum local 5, alors que $f(5) = 21$).

### R7.Q8 — Qui domine qui ?
1. **Vrai** : $3n^2 + 100n \le 4n^2$ dès $n \ge 100$.
2. **Faux** : $\frac{n^3}{n^2} = n$ n'est pas borné.
3. $2^n$ (une exponentielle finit par dépasser toute puissance).
4. $O(n^2)$ : $n \times n$ tours.
5. **Vrai** : $\log_2 n = \frac{\ln n}{\ln 2}$, égal à $\ln n$ à une constante près.
6. Environ **200 secondes** : $n$ multiplié par 10, $n^2$ par 100.

<a id="rappels"></a>

## 🔁 Rappels

### R7.R1 — Croissances comparées (R6)
1. **0** (l'exponentielle l'emporte). 2. **0** (toute puissance, même $x^{0{,}1}$, finit par dépasser ln). 3. $\ln x$, puis $x^2$, puis $e^{0{,}1x}$.

### R7.R2 — Limite d'une suite (R5)
1. $\frac{2n + 1}{n} = 2 + \frac{1}{n} \to$ **2**. 2. **0** ($0 < 0{,}9 < 1$). 3. $e \approx 2{,}718$.

### R7.R3 — Sommet d'une parabole (R3)
1. $x = -\frac{b}{2a} = 3$, $y = 9 - 18 + 5 = -4$ : le sommet est $(3 \;;\; -4)$.
2. $x = -\frac{8}{2 \times (-2)} = 2$ : le maximum vaut $-8 + 16 = 8$, atteint en 2.
3. Un **minimum** ($a = 3 > 0$), qui vaut 2, en $x = 1$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R7.1 — Limites en l'infini des fonctions de référence

**Réponses** : a) `5` · b) `"+oo"` · c) `2` · d) `0` · e) `1` · f) `0` · g) `"+oo"` · h) `"-oo"`.

**Démarche.**
- a) $\frac{3}{x} \to 0$, donc $5 - \frac{3}{x} \to 5$.
- b) $x^3 - 100x^2 = x^3\left(1 - \frac{100}{x}\right)$ : $+\infty \times 1$.
- c) $\frac{x(4 + \frac{1}{x})}{x(2 - \frac{3}{x})} \to \frac{4}{2} = 2$.
- d) Degré 2 en haut, 3 en bas : $\frac{x^2 + 1}{x^3 - 2} = \frac{1}{x} \times \frac{1 + \frac{1}{x^2}}{1 - \frac{2}{x^3}} \to 0 \times 1$.
- e) $e^{-2x} \to 0$, donc la somme tend vers 1.
- f) $\frac{x^2 + 1}{e^x}$ : l'exponentielle l'emporte sur le polynôme.
- g) $\sqrt{x} = x^{1/2}$ est une puissance, qui l'emporte sur ln : le quotient tend vers $+\infty$.
- h) $x^3 + 2x = x^3\left(1 + \frac{2}{x^2}\right)$, et $x^3 \to -\infty$ quand $x \to -\infty$.

**Erreurs fréquentes.** Écrire $\infty - \infty = 0$ en b ; en c, garder les constantes au lieu des termes de plus haut degré (et répondre $\frac{1}{-3}$) ; répondre $+\infty$ en f (le polynôme grandit, mais l'exponentielle bien plus vite) ; oublier le signe en h.

**Variante.** $\lim_{x \to +\infty} \frac{6x^3 - x}{2x^3 + 5}$ et $\lim_{x \to +\infty} \left(\sqrt{x} - x\right)$ ? *Réponse* : 3 ; $\sqrt{x} - x = x\left(\frac{1}{\sqrt{x}} - 1\right) \to -\infty$.

### Ex R7.2 — Limites et asymptotes de fonctions rationnelles

**Réponses** : a) `3` · b) `"-oo"` · c) `"+oo"` · d) `[-1, 3]` · e) `5` · f) `False` · g) `[-3, 3]` · h) `"+oo"`.

**Démarche.**
- a) Même degré : $\frac{3}{1} = 3$.
- b) et c) En −1, le numérateur vaut $3 \times (-1) - 2 = -5$ et le dénominateur tend vers 0 : positif à droite ($x > -1$), négatif à gauche. $\frac{-5}{0^+} \to -\infty$ et $\frac{-5}{0^-} \to +\infty$.
- d) Asymptote verticale $x = -1$, horizontale $y = 3$.
- e) $x^2 + x - 6 = (x - 2)(x + 3)$, donc $g(x) = x + 3$ pour $x \ne 2$, et la limite vaut 5.
- f) **Faux** : $g$ tend vers 5 en 2, une limite finie ; la courbe est la droite $y = x + 3$ privée d'un point.
- g) $x^2 - 9 = 0$ pour $x = -3$ et $x = 3$, où le numérateur vaut $2 \times 9 + 3 = 21 \ne 0$.
- h) En 3 par la droite : numérateur 21, dénominateur $(x - 3)(x + 3) \to 0^+$ (car $x - 3 > 0$ et $x + 3 > 0$) : $+\infty$.

**Erreurs fréquentes.** Chercher l'asymptote là où le numérateur s'annule ($x = \frac{2}{3}$) ; donner $-5$ ou 0 pour b et c ; conclure « asymptote » en f sans factoriser ; oublier l'asymptote $x = -3$ en g.

**Variante.** Les asymptotes de $\frac{x^2}{x^2 - 4x}$ ? *Réponse* : $\frac{x^2}{x(x - 4)} = \frac{x}{x - 4}$ pour $x \ne 0$ : asymptote verticale $x = 4$ seulement (en 0, un trou : la limite vaut 0), et horizontale $y = 1$.

### Ex R7.3 — Taux d'accroissement et nombre dérivé

**Réponses** : a) `22.5` · b) `20.5` · c) `"20 + 5*h"` · d) `20` · e) `14` · f) `13` · g) `3` · h) `2.5`.

**Démarche.**
- a) $s(2) = 20$ et $s(2{,}5) = 31{,}25$ : $\frac{31{,}25 - 20}{0{,}5} = 22{,}5$ m/s.
- b) $s(2{,}1) = 22{,}05$ : $\frac{2{,}05}{0{,}1} = 20{,}5$ m/s.
- c) $s(2 + h) = 5(4 + 4h + h^2) = 20 + 20h + 5h^2$, donc $\frac{s(2 + h) - s(2)}{h} = \frac{20h + 5h^2}{h} = 20 + 5h$ ; on retrouve a ($h = 0{,}5$) et b ($h = 0{,}1$).
- d) $20 + 5h \to 20$ quand $h \to 0$ : la vitesse instantanée vaut 20 m/s.
- e) $C(10) = 50 + 30 + 100 = 180$ et $C(12) = 72 + 36 + 100 = 208$ : $\frac{28}{2} = 14$ € par pièce ajoutée.
- f) $C(10 + h) = 180 + 13h + 0{,}5h^2$, donc le taux vaut $13 + 0{,}5h \to 13$ € : le coût marginal.
- g) $\frac{\big(3(x + h) + 7\big) - (3x + 7)}{h} = \frac{3h}{h} = 3$ : le taux d'une fonction affine est sa pente, partout.
- h) $f(4) = -4$ et $f(3{,}5) = 12{,}25 - 17{,}5 = -5{,}25$ : $\frac{-5{,}25 + 4}{-0{,}5} = 2{,}5$.

**Erreurs fréquentes.** Oublier de diviser par la durée (a, b) ; laisser $\frac{20h + 5h^2}{h}$ sans le simplifier (c) ; prendre une vitesse moyenne pour la vitesse instantanée (d) ; confondre le coût moyen des pièces ajoutées (e) et le coût marginal (f) ; diviser par $+0{,}5$ en h.

**Variante.** Le taux de $x^2 + 2x$ entre 1 et $1 + h$, et la dérivée en 1 ? *Réponse* : $4 + h$, et 4.

### Ex R7.4 — Équation de la tangente

**Réponses** : a) `[3, -16]` · b) `[2.718, 0]` · c) `[0.5, -0.307]` · d) `[0.25, 1]` · e) `2.05` · f) `0.00061` · g) `2.5` · h) `"2/3"`.

**Démarche.**
- a) $f(4) = -4$, $f'(4) = 8 - 5 = 3$ : $y = -4 + 3(x - 4) = 3x - 16$.
- b) $y = e + e(x - 1) = ex$ : la tangente de exp en 1 passe par l'origine.
- c) $y = \ln 2 + \frac{1}{2}(x - 2) = \frac{x}{2} + \ln 2 - 1 \approx 0{,}5x - 0{,}307$.
- d) $\sqrt{4} = 2$ et $\frac{1}{2\sqrt{4}} = \frac{1}{4}$ : $y = 2 + \frac{x - 4}{4} = \frac{x}{4} + 1$.
- e) $\frac{4{,}2}{4} + 1 = 2{,}05$.
- f) $\sqrt{4{,}2} \approx 2{,}049\,39$, donc l'écart vaut environ $0{,}000\,61$ : la tangente est un peu au-dessus de la courbe.
- g) $2x - 5 = 0$ pour $x = 2{,}5$.
- h) En 1 : $y = 1 + 3(x - 1) = 3x - 2$, qui s'annule en $x = \frac{2}{3}$.

**Erreurs fréquentes.** $y = f'(a)(x - a)$, sans $f(a)$ ; un signe faux en développant $-f'(a) \times a$ ; résoudre $f(x) = 0$ au lieu de $f'(x) = 0$ en g.

**Variante.** La tangente de $\sqrt{x}$ en $x = 9$, et l'approximation de $\sqrt{9{,}3}$ qu'elle donne ? *Réponse* : $f'(9) = \frac{1}{6}$, $y = 3 + \frac{x - 9}{6} = \frac{x}{6} + 1{,}5$ ; $\sqrt{9{,}3} \approx 3{,}05$ (vraie valeur 3,0496).

### Ex R7.5 — Dériver les fonctions usuelles

**Réponses** : a) `"7*x**6"` · b) `"12*x**5 - 21*x**2 + 1"` · c) `"-3/x**4"` · d) `"3*sqrt(x)/2"` · e) `"2/(3*x**(1/3))"` · f) `"3*exp(x) - 4/x"` · g) `"1/x"` · h) `"exp(x + 2)"`.

**Démarche.**
- c) $\frac{1}{x^3} = x^{-3}$, de dérivée $-3x^{-4}$.
- d) $x\sqrt{x} = x^{3/2}$, de dérivée $\frac{3}{2}x^{1/2} = \frac{3\sqrt{x}}{2}$.
- e) $\frac{2}{3}x^{2/3 - 1} = \frac{2}{3}x^{-1/3}$.
- g) $\ln(5x) = \ln 5 + \ln x$ ; la constante $\ln 5$ a une dérivée nulle.
- h) $e^{x + 2} = e^2 e^x$, de dérivée $e^2 e^x = e^{x + 2}$.

**Erreurs fréquentes.** Garder l'exposant ($7x^7$) ; $(\frac{1}{x^3})' = \frac{1}{3x^2}$ ; $(x\sqrt{x})' = \frac{1}{2\sqrt{x}}$ (dériver seulement $\sqrt{x}$) ; $\frac{1}{5x}$ en g ; $e^x$ en h.

**Variante.** Les dérivées de $\frac{2}{\sqrt{x}}$ et de $\ln(x^4)$ ? *Réponse* : $2x^{-1/2}$ donne $-x^{-3/2} = -\frac{1}{x\sqrt{x}}$ ; $\ln(x^4) = 4\ln x$ donne $\frac{4}{x}$.

### Ex R7.6 — Dériver des produits et des quotients

**Réponses** : a) `"exp(x)*log(x) + exp(x)/x"` · b) `"9*x**2 - 4*x + 3"` · c) `"log(x)/(2*sqrt(x)) + 1/sqrt(x)"` · d) `"9/(2*x + 1)**2"` · e) `"(1 - x**2)/(x**2 + 1)**2"` · f) `"x*exp(x)/(x + 1)**2"` · g) `2.718` · h) `"-(exp(x) + 1)/(exp(x) + x)**2"`.

**Démarche.**
- a) $e^x \ln x + e^x \times \frac{1}{x} = e^x \ln x + \frac{e^x}{x}$.
- b) $2x(3x - 2) + 3(x^2 + 1) = 9x^2 - 4x + 3$ (ou développer d'abord : $3x^3 - 2x^2 + 3x - 2$).
- c) $\frac{1}{2\sqrt{x}} \ln x + \sqrt{x} \times \frac{1}{x} = \frac{\ln x}{2\sqrt{x}} + \frac{1}{\sqrt{x}}$.
- d) $\frac{1 \times (2x + 1) - (x - 4) \times 2}{(2x + 1)^2} = \frac{9}{(2x + 1)^2}$.
- e) $\frac{(x^2 + 1) - x \times 2x}{(x^2 + 1)^2} = \frac{1 - x^2}{(x^2 + 1)^2}$.
- f) $\frac{e^x (x + 1) - e^x \times 1}{(x + 1)^2} = \frac{x\,e^x}{(x + 1)^2}$.
- g) En 1 : $e \ln 1 + \frac{e}{1} = 0 + e \approx 2{,}718$.
- h) $-\frac{e^x + 1}{(e^x + x)^2}$, avec $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$ et $v = e^x + x$.

**Erreurs fréquentes.** Le produit des dérivées ($e^x \times \frac{1}{x}$ en a) ; inverser $u'v$ et $uv'$ (le signe change) ; oublier le carré du dénominateur ; en g, croire que tout s'annule parce que $\ln 1 = 0$ ; en h, oublier $v'$ au numérateur.

**Variante.** Les dérivées de $(x^2 - 1)\sqrt{x}$ et de $\frac{x^2}{x - 1}$ ? *Réponse* : $2x\sqrt{x} + \frac{x^2 - 1}{2\sqrt{x}} = \frac{5x^2 - 1}{2\sqrt{x}}$ ; $\frac{2x(x - 1) - x^2}{(x - 1)^2} = \frac{x^2 - 2x}{(x - 1)^2}$.

### Ex R7.7 — Dériver des composées

**Réponses** : a) `"12*x*(2*x**2 - 1)**2"` · b) `"-2*exp(-x/5)"` · c) `"3/(3*x + 2)"` · d) `"3*x**2/(2*sqrt(x**3 + 1))"` · e) `"exp(sqrt(x))/(2*sqrt(x))"` · f) `"1/(x*log(x))"` · g) `"-(2*x + 1)/(x**2 + x)**2"` · h) `"4/3"`.

**Démarche.**
- a) $u = 2x^2 - 1$, $u' = 4x$ : $3u^2 \times 4x = 12x(2x^2 - 1)^2$.
- b) $u = -\frac{x}{5}$, $u' = -\frac{1}{5}$ : $10 \times \left(-\frac{1}{5}\right) e^{-x/5} = -2e^{-x/5}$.
- c) $\frac{u'}{u} = \frac{3}{3x + 2}$.
- d) $u = x^3 + 1$, $u' = 3x^2$ : $\frac{3x^2}{2\sqrt{x^3 + 1}}$.
- e) $u = \sqrt{x}$ : $e^{\sqrt{x}} \times \frac{1}{2\sqrt{x}}$.
- f) $u = \ln x$, $u' = \frac{1}{x}$ : $\frac{1/x}{\ln x} = \frac{1}{x \ln x}$.
- g) $-u^{-2} \times u'$ avec $u = x^2 + x$ et $u' = 2x + 1$.
- h) $\frac{2x + 2}{x^2 + 2x}$ en 1 : $\frac{4}{3}$.

**Erreurs fréquentes.** Oublier la dérivée de l'intérieur (la plus fréquente de toutes) ; perdre le signe de $u' = -\frac{1}{5}$ en b ; $\frac{1}{\ln x}$ en f ; en h, remplacer $x$ par 1 avant de dériver.

**Variante.** Les dérivées de $(1 - 3x)^4$ et de $e^{1/x}$ ? *Réponse* : $-12(1 - 3x)^3$ ; $-\frac{1}{x^2}e^{1/x}$.

### Ex R7.8 — Variations et tableau de variations

**Réponses** : a) `"4*x**3 - 12*x**2"` · b) `[0, 3]` · c) `"]-oo ; 3]"` · d) `1` · e) `-17` · f) `15` · g) `2` · h) `0.614`.

**Démarche.**
- a) et b) $f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$, nulle en 0 et en 3.
- c) $4x^2 \ge 0$ : $f'$ a le signe de $x - 3$. Elle est négative avant 3 (sauf en 0, où elle s'annule sans changer de signe), positive après. $f$ décroît sur $]-\infty \;;\; 3]$.

| $x$ | $-\infty$ | | $0$ | | $3$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $-$ | $0$ | $+$ | |
| $f$ | | ↘ | 10 | ↘ | −17 | ↗ | |

- d) Un seul extremum local, le minimum en 3. En 0, la tangente est horizontale, mais $f$ continue de descendre : pas d'extremum (comme $x^5$ en 0, fiche §8).
- e) $f(3) = 81 - 108 + 10 = -17$ : $f$ décroît jusqu'à 3 puis croît, c'est sa plus petite valeur sur $\mathbb{R}$.
- f) Sur $[-1 \;;\; 4]$ : $f(-1) = 1 + 4 + 10 = 15$, $f(0) = 10$, $f(3) = -17$, $f(4) = 256 - 256 + 10 = 10$. Le maximum, 15, est atteint au bord gauche.
- g) $g'(x) = 1 - \frac{2}{x} = \frac{x - 2}{x}$ : négatif sur $]0 \;;\; 2[$, positif ensuite ; minimum en 2.
- h) $g(2) = 2 - 2\ln 2 \approx 0{,}614$.

**Erreurs fréquentes.** Oublier la racine 0 du facteur $x^2$ (b) ; compter 0 comme un extremum (d) ; oublier les bords en f (répondre 10) ; donner l'abscisse au lieu de la valeur (e, h).

**Variante.** Le minimum de $x^2 - 8\ln x$ sur $]0 \;;\; +\infty[$ ? *Réponse* : $2x - \frac{8}{x} = \frac{2(x^2 - 4)}{x}$, négative avant 2 et positive après : minimum $4 - 8\ln 2 \approx -1{,}545$ en 2.

### Ex R7.9 — Optimiser : la boîte de volume maximal

**Réponses** : a) `"]0 ; 5["` · b) `"4*x**3 - 52*x**2 + 160*x"` · c) `"12*x**2 - 104*x + 160"` · d) `2` · e) `144` · f) `[12, 6, 2]`.

**Démarche.**
- a) Il faut $x > 0$ et $10 - 2x > 0$ (le côté le plus court) : $0 < x < 5$.
- b) $(16 - 2x)(10 - 2x) = 160 - 52x + 4x^2$, puis on multiplie par $x$.
- c) et d) $V'(x) = 12x^2 - 104x + 160 = 4(3x^2 - 26x + 40) = 4(3x - 20)(x - 2)$ : nulle en 2 et en $\frac{20}{3} \approx 6{,}67$, hors du domaine. $V'$ est positive sur $]0 \;;\; 2[$, négative sur $]2 \;;\; 5[$ : maximum en 2.
- e) $V(2) = 2 \times 12 \times 6 = 144$ cm³.
- f) Longueur $16 - 4 = 12$, largeur $10 - 4 = 6$, hauteur 2.

**Erreurs fréquentes.** Garder la racine $\frac{20}{3}$ ; un domaine $]0 \;;\; 8[$ (oublier que le côté de 10 cm limite) ; retirer $x$ au lieu de $2x$ à chaque côté.

**Variante.** La même boîte dans un carré de 12 cm de côté ? *Réponse* : $V(x) = x(12 - 2x)^2$, $V'(x) = (12 - 2x)(12 - 6x)$, maximum en $x = 2$ : $V = 2 \times 8^2 = 128$ cm³.

### Ex R7.10 — La règle de la chaîne en série : trois étages, et l'ordre qui compte

**Réponses** : a) `"6*x*(x**2 + 1)**2*exp((x**2 + 1)**3)"` · b) `"1/(2*x*sqrt(log(x)))"` · c) `"3*exp(x)*(2 + exp(x))**2"` · d) `"4/(2*x + 1)"` · e) `20` · f) `1.269` · g) `0.5` · h) `[109.196, 218.393]`.

**Démarche.**
- a) Trois étages : $v = x^2 + 1$, $u = v^3$, $z = e^u$. $\frac{dz}{dx} = e^u \times 3v^2 \times 2x$.
- b) $u = \ln x$ : $\frac{1}{2\sqrt{\ln x}} \times \frac{1}{x}$.
- c) $3(2 + e^x)^2 \times e^x$.
- d) $\ln\big((2x + 1)^2\big) = 2\ln(2x + 1)$ (pour $2x + 1 > 0$), de dérivée $2 \times \frac{2}{2x + 1}$.
- e) $5(x^2 - 3)^4 \times 2x$ en 2 : $5 \times 1 \times 4 = 20$.
- f) $(\ln u)' = \frac{u'}{u}$ avec $u = x^2 + e^x$ et $u' = 2x + e^x$ : en 1, $\frac{2 + e}{1 + e} \approx 1{,}269$.
- g) $\frac{2e^{2x}}{2\sqrt{e^{2x} + 3}} = \frac{e^{2x}}{\sqrt{e^{2x} + 3}}$ en 0 : $\frac{1}{\sqrt{4}} = 0{,}5$.
- h) $(e^x)^2 = e^{2x}$ a pour dérivée $2e^{2x}$, soit $2e^4 \approx 109{,}196$ en 2 ; $e^{x^2}$ a pour dérivée $2x\,e^{x^2}$, soit $4e^4 \approx 218{,}393$.

**Erreurs fréquentes.** S'arrêter à deux étages en a ; oublier le 2 de l'exposant en d ou en g ; oublier $u'$ en f ; confondre $(e^x)^2$ et $e^{x^2}$ en h.

**Variante.** Les dérivées de $\sqrt{1 + e^{-x}}$ et de $\ln(\ln(\ln x))$ ? *Réponse* : $\frac{-e^{-x}}{2\sqrt{1 + e^{-x}}}$ ; $\frac{1}{x \ln x \ln(\ln x)}$.

### Ex R7.11 — Dériver par rapport à une lettre, les autres fixées : A e^(kt), π r² h, ½ m v²

**Réponses** : a) `"A*k*exp(k*t)"` · b) `"A*t*exp(k*t)"` · c) `"exp(k*t)"` · d) `"2*pi*r*h"` · e) `"pi*r**2"` · f) `188.50` · g) `"m*v"` · h) `"v**2/2"`.

**Démarche.**
- a) Par rapport à $t$ : $A$ est un facteur constant, et $(e^{kt})' = k\,e^{kt}$ (l'intérieur $kt$ a pour dérivée $k$).
- b) Par rapport à $k$ : l'intérieur $kt$ a pour dérivée $t$.
- c) Par rapport à $A$ : $N = A \times e^{kt}$, une constante fois $A$.
- d) $\pi h$ est une constante : $(\pi h)\,(r^2)' = 2\pi r h$. e) $\pi r^2$ est une constante, $(h)' = 1$.
- f) $2\pi \times 3 \times 10 = 60\pi \approx 188{,}50$.
- g) $\frac{1}{2} m \times 2v = mv$. h) $\frac{1}{2}v^2 \times 1$.

**Erreurs fréquentes.** Oublier la dérivée de l'intérieur en a ; en b, donner $k$ comme dérivée de $kt$ par rapport à $k$ (c'est $t$) ; « perdre » une lettre constante (répondre $2\pi r$ en d) ; dériver aussi les lettres fixées.

**Variante.** Pour $P = \frac{nRT}{V}$ (loi des gaz parfaits), $\frac{dP}{dT}$ et $\frac{dP}{dV}$ ? *Réponse* : $\frac{nR}{V}$ ; $-\frac{nRT}{V^2}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R7.12 — La dérivée de x² à partir de la définition, et |x| qui n'est pas dérivable en 0

**Démonstration.**
1. Pour $h \ne 0$ : $\frac{(a + h)^2 - a^2}{h} = \frac{a^2 + 2ah + h^2 - a^2}{h} = \frac{h(2a + h)}{h} = 2a + h$.
2. Quand $h \to 0$, $2a + h \to 2a$, une limite finie : $f$ est dérivable en $a$, et $f'(a) = 2a$. Comme $a$ est quelconque, $(x^2)' = 2x$. ∎
3. Le taux de $g$ entre 0 et $h$ est $\frac{\lvert h \rvert - \lvert 0 \rvert}{h} = \frac{\lvert h \rvert}{h}$ : il vaut $\frac{h}{h} = 1$ pour $h > 0$, et $\frac{-h}{h} = -1$ pour $h < 0$.
4. Quand $h \to 0$, le taux vaut 1 à droite et −1 à gauche : il n'a pas de limite, donc $g$ n'est pas dérivable en 0. Elle y est pourtant continue : $\lvert x \rvert \to 0 = \lvert 0 \rvert$ quand $x \to 0$ (la courbe n'a pas de saut, seulement un coin). ∎
5. Pour $a > 0$ et $h$ assez petit ($\lvert h \rvert < a$), $a + h > 0$, donc $g(a + h) = a + h$ et le taux vaut $\frac{h}{h} = 1$ : $g'(a) = 1$. Pour $a < 0$, de même, $g(x) = -x$ près de $a$, et $g'(a) = -1$.

**Grille de relecture.**
- Le calcul de 1 est fait pour $h \ne 0$, et la simplification par $h$ est justifiée par $h \ne 0$.
- En 2, on dit que la limite est **finie** et qu'elle vaut $2a$ pour **tout** $a$.
- En 3 et 4, les deux cas $h > 0$ et $h < 0$ sont traités séparément, avec $\lvert h \rvert = h$ ou $-h$.
- La conclusion de 4 dit pourquoi l'absence de limite empêche la dérivabilité, et distingue continuité et dérivabilité.
- En 5, on explique pourquoi $a + h$ garde le signe de $a$ quand $h$ est petit.

**Erreurs fréquentes.** Simplifier par $h$ sans dire $h \ne 0$ ; poser $h = 0$ directement dans le taux ($\frac{0}{0}$) ; conclure en 4 sur un seul côté ; croire que « continue » entraîne « dérivable ».

**Variante.** Montre de même que $x \mapsto x\lvert x \rvert$ **est** dérivable en 0. *Réponse* : le taux entre 0 et $h$ vaut $\frac{h\lvert h \rvert}{h} = \lvert h \rvert \to 0$ des deux côtés : la dérivée en 0 vaut 0.

### Ex R7.13 — Démontrer la règle du produit

**Démonstration.**
1. Pour $h \ne 0$, $v(a + h) - v(a) = h \times \frac{v(a + h) - v(a)}{h}$. Quand $h \to 0$, le premier facteur tend vers 0 et le second vers $v'(a)$ (un nombre fini) : le produit tend vers $0 \times v'(a) = 0$. Donc $v(a + h) \to v(a)$ : $v$ est continue en $a$.
2. En développant le membre de droite : $u(a + h)v(a + h) - u(a)v(a + h) + u(a)v(a + h) - u(a)v(a)$ ; les deux termes du milieu s'annulent, il reste le membre de gauche.
3. En divisant par $h$ :
$$\frac{(uv)(a + h) - (uv)(a)}{h} = \frac{u(a + h) - u(a)}{h} \times v(a + h) + u(a) \times \frac{v(a + h) - v(a)}{h}.$$
Quand $h \to 0$, le premier quotient tend vers $u'(a)$, $v(a + h)$ tend vers $v(a)$ (c'est là que sert la question 1), et le dernier quotient tend vers $v'(a)$. Donc $(uv)'(a) = u'(a)v(a) + u(a)v'(a)$. ∎
4. *Initialisation* : pour $n = 1$, $(x)' = 1 = 1 \times x^0$. *Hérédité* : si $(x^n)' = nx^{n-1}$, alors, par la règle du produit, $(x^{n+1})' = (x^n \times x)' = nx^{n-1} \times x + x^n \times 1 = (n + 1)x^n$. *Conclusion* : vrai pour tout $n \ge 1$. ∎
5. $(u^2)' = (u \times u)' = u'u + uu' = 2uu'$, puis $(u^3)' = (u^2 \times u)' = 2uu' \times u + u^2 u' = 3u^2 u'$.

**Grille de relecture.**
- La question 1 utilise la limite d'un produit (un facteur tend vers 0, l'autre vers un nombre fini).
- L'égalité de 2 est vérifiée par un calcul, pas affirmée.
- En 3, chaque limite est nommée, et l'usage de la continuité de $v$ est signalé.
- La récurrence de 4 a ses trois étapes, et l'hérédité cite la règle du produit.
- En 5, on reconnaît la règle de la chaîne pour $u^2$ et $u^3$ (fiche §7).

**Erreurs fréquentes.** Écrire $\frac{u(a + h)v(a + h) - u(a)v(a)}{h} = u'(a)v'(a)$ « par passage à la limite » ; oublier que $v(a + h)$ dépend de $h$ ; une récurrence sans initialisation.

**Variante.** Déduis de la règle du produit la dérivée de $uvw$. *Réponse* : $(uvw)' = (uv)'w + (uv)w' = u'vw + uv'w + uvw'$ : un terme par facteur dérivé.

### Ex R7.14 — La règle du quotient à partir de la règle du produit : (1/v)′ = −v′/v²

**Démonstration.**
1. La dérivée d'une constante est nulle : $\left(v \times \frac{1}{v}\right)' = 0$, et la règle du produit donne $v' \times \frac{1}{v} + v \times \left(\frac{1}{v}\right)' = 0$.
2. Donc $v \times \left(\frac{1}{v}\right)' = -\frac{v'}{v}$, et, en divisant par $v \ne 0$, $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$. ∎
3. $\left(\frac{u}{v}\right)' = \left(u \times \frac{1}{v}\right)' = u' \times \frac{1}{v} + u \times \left(-\frac{v'}{v^2}\right) = \frac{u'v}{v^2} - \frac{uv'}{v^2} = \frac{u'v - uv'}{v^2}$. ∎
4. Avec $v = x^n$, $v' = nx^{n-1}$ : $(x^{-n})' = \left(\frac{1}{x^n}\right)' = -\frac{nx^{n-1}}{x^{2n}} = -nx^{-n-1}$. C'est la règle $(x^m)' = mx^{m-1}$ avec $m = -n$ : elle vaut aussi pour les exposants entiers négatifs.
5. $\left(\frac{1}{x^3 + 2}\right)' = -\frac{3x^2}{(x^3 + 2)^2}$. Avec la règle de la chaîne, $(u^{-1})' = -u^{-2} \times u'$ avec $u = x^3 + 2$ : le même résultat.

**Grille de relecture.**
- La dérivée de la constante 1 est écrite (0), et la règle du produit est citée.
- La division par $v$ en 2 est justifiée ($v$ ne s'annule pas).
- En 3, la réduction au même dénominateur $v^2$ est faite.
- En 4, le calcul $\frac{x^{n-1}}{x^{2n}} = x^{-n-1}$ est détaillé.
- En 5, les deux méthodes donnent la même expression.

**Erreurs fréquentes.** Écrire $\left(\frac{1}{v}\right)' = \frac{1}{v'}$ ; perdre le signe moins ; diviser par $v$ sans dire qu'il ne s'annule pas.

**Variante.** Dérive $\frac{x^2 + 1}{x^2}$ de deux façons : avec la règle du quotient, puis après l'avoir écrite $1 + \frac{1}{x^2}$. *Réponse* : $\frac{2x \cdot x^2 - (x^2 + 1) \cdot 2x}{x^4} = \frac{-2x}{x^4} = -\frac{2}{x^3}$, et $(1 + x^{-2})' = -2x^{-3}$ : le même résultat, la seconde façon bien plus vite.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R7.15 — Minimiser une fonction de coût donnée par une formule : dériver, annuler, vérifier

**Réponses** : a) `"2 - 8/a**2"` · b) `2` · c) `9` · d) `-6` · e) `0.693` · f) `4` · g) `[4.020, 4.020]`.

**Démarche.**
- a) $(2a)' = 2$, $\left(\frac{8}{a}\right)' = -\frac{8}{a^2}$, la constante 1 disparaît.
- b) $2 - \frac{8}{a^2} = 0 \iff a^2 = 4 \iff a = 2$ (car $a > 0$).
- c) $E(2) = 4 + 4 + 1 = 9$.
- d) $E'(1) = 2 - 8 = -6 < 0$ : $E$ descend encore en 1, qui est à gauche du minimum.
- e) $L'(t) = e^t - 4e^{-t} = 0 \iff e^{2t} = 4 \iff t = \frac{\ln 4}{2} = \ln 2 \approx 0{,}693$.
- f) $L(\ln 2) = 2 + 4 \times \frac{1}{2} = 4$.
- g) Les deux valeurs voisines valent environ 4,020, plus que 4 : un minimum, et les deux côtés sont symétriques ($L(\ln 2 \pm d) = 2e^{d} + 2e^{-d}$).

Dans ta copie : une dérivée nulle peut aussi signaler un maximum ou un replat ($x^5$ en 0). Ici, $E'(a) = \frac{2(a^2 - 4)}{a^2}$ est négative sur $]0 \;;\; 2[$ et positive ensuite : $E$ décroît puis croît sur tout son domaine, donc $E(2)$ est la plus petite valeur **partout**, pas seulement au voisinage. De même, $L'(t) = e^{-t}(e^{2t} - 4)$ a le signe de $e^{2t} - 4$ : négative avant $\ln 2$, positive après.

**Erreurs fréquentes.** Garder $a = -2$ ; oublier le signe de $\left(\frac{8}{a}\right)'$ ; en e, s'arrêter à $\ln 4$ ; affirmer « minimum » sans étudier le signe.

**Variante.** Minimise $E(a) = a + \frac{9}{a}$ sur $]0 \;;\; +\infty[$. *Réponse* : $1 - \frac{9}{a^2} = 0$ en $a = 3$, minimum $E(3) = 6$.

### Ex R7.16 — Expliquer ce qu'est une dérivée sans écrire de formule

**Exemple de réponse.**

> Imagine le compteur d'une voiture : il ne dit pas la distance parcourue, mais à quelle vitesse elle change, à cet instant. Une dérivée, c'est ce compteur pour n'importe quelle quantité : elle dit de combien la quantité bouge quand on bouge un tout petit peu ce dont elle dépend, rapporté à ce petit pas. Si elle est positive, la quantité monte ; négative, elle descend ; nulle, elle est à plat, pour un instant. Sa taille dit la sensibilité : une grande dérivée veut dire qu'un petit changement a un gros effet. Sur une courbe, c'est la pente à l'endroit où tu es. Et au moment où une quantité cesse de descendre pour remonter, comme le niveau d'un lac au plus sec de l'été, sa dérivée vaut zéro : c'est ainsi qu'on repère le plus petit niveau, ou la plus petite erreur d'un modèle.

**Grille.** Une bonne réponse : (1) l'image de la vitesse (compteur) ; (2) le rapport entre deux petites variations ; (3) le signe : monte ou descend ; (4) la taille : la sensibilité ; (5) l'usage pour trouver un minimum (la dérivée nulle au moment où la quantité cesse de descendre) ; (6) aucune formule, huit lignes au plus.

<a id="notebook"></a>

## Notebook

### Ex R7.17 — Le taux d'accroissement · `difference_quotient`

**Réponses** : a) `[0.2361, 0.2485, 0.2498]` · b) `0.2502` · c) `"ValueError"` · d) `1.000`.

**Démarche.** Le test `if h == 0: raise ValueError(...)`, puis `return float((f(a + h) - f(a)) / h)`. Pour la copie : les taux se rapprochent de $\frac{1}{2\sqrt{4}} = 0{,}25$, par en dessous pour $h > 0$ et par au-dessus pour $h < 0$ ; et $x^x = e^{x\ln x}$ a pour dérivée $(\ln x + 1)\,e^{x\ln x}$, qui vaut 1 en 1.

**Erreurs fréquentes.** Oublier la division par $h$ ; diviser par `abs(h)` ; laisser Python lever `ZeroDivisionError` au lieu de la `ValueError` demandée.

### Ex R7.18 — La tangente à partir de f et de sa dérivée · `tangent_line`

**Réponses** : a) `[0.3679, 0]` · b) `[11, -16]` · c) `"int int"` · d) `[0.3679, 0.7358]`.

**Démarche.** `m = df(a)`, puis `return m, f(a) - m * a`. En a), la tangente de ln en $e$ est $y = \frac{x}{e}$ : elle passe par l'origine. Pour la copie : la tangente de exp en $a$ est $y = e^a x + e^a(1 - a)$ ; elle coupe l'axe des abscisses en $x = a - 1$ (ici −2), toujours une unité à gauche du point de contact.

**Erreurs fréquentes.** `c = f(a)` (oublier $-f'(a) \times a$) ; un signe faux ; `float(...)` qui transforme les entiers de b en flottants.

### Ex R7.19 — Trouver un zéro par dichotomie · `bisection`

**Réponses** : a) `0.619061` · b) `1.557146` · c) `"ValueError"` · d) `"ValueError"` · e) `1.0` · f) `True` · g) `34`.

**Démarche.** Vérifier `a < b` ; calculer `f(a)` et `f(b)` ; renvoyer une borne où `f` vaut 0 ; lever une `ValueError` si les deux signes sont stricts et identiques ; puis, au plus `max_iter` fois et tant que `b - a >= tol`, couper en deux et garder la moitié où le signe change ; renvoyer le milieu. g) $2^{-n} < 10^{-10} \iff n > 10\log_2 10 \approx 33{,}2$ : 34 coupes.

**Erreurs fréquentes.** Tester `f(a) * f(b) > 0` sans traiter les zéros aux bornes (ni un milieu où `f` vaut exactement 0) ; renvoyer `a` au lieu du milieu (on perd jusqu'à la moitié de `tol`) ; une boucle `while b - a > tol` sans limite, qui ne s'arrête jamais pour `tol = 0`.

### Ex R7.20 — Vérifier ses dérivées avec `sympy.diff`

**Réponses** : a) $(x^2 + 2x - 3)\,e^x$ · b) `[-3, 1]` · c) `[True, True, False]` · d) `1/4`.

**Démarche.** a) `sp.diff((x**2 - 3) * sp.exp(x), x)`, qui affiche $2x e^x + (x^2 - 3)e^x$ ; b) `sorted(int(v) for v in sp.solve(..., x))` : $(x^2 + 2x - 3)e^x = (x + 3)(x - 1)e^x$ s'annule en −3 et en 1 ; c) `sp.simplify(sp.diff(f, x) - proposed) == 0` pour chaque couple ; d) `sp.limit((sp.sqrt(x + 4) - 2) / x, x, 0)`, le nombre dérivé de $\sqrt{x}$ en 4. La troisième dérivée proposée est fausse : $\left(\sqrt{x}\,e^{2x}\right)' = \frac{e^{2x}}{2\sqrt{x}} + 2\sqrt{x}\,e^{2x}$ (le facteur 2 de la règle de la chaîne manque). Avec `==`, la première, juste pourtant, serait déclarée fausse : `==` compare des écritures.

**Erreurs fréquentes.** Comparer avec `==` deux écritures de la même dérivée ; oublier les parenthèses autour de $x^2 - 3$ ; chercher les zéros de la fonction au lieu de ceux de la dérivée ; `math.exp` au lieu de `sp.exp` (une erreur, car $x$ est un symbole).

### Ex R7.21 — Prédire : le taux d'accroissement a-t-il toujours une limite quand h tend vers 0 ?

**Réponses** : a) `2` · b) `3` · c) `1`.

**Démarche.** a) Pour $h > 0$, $\frac{e^{h} - 1}{h} \to 1$ ; pour $h < 0$, $\frac{e^{-h} - 1}{h} \to -1$. Deux limites différentes : $e^{\lvert x \rvert}$ fait un coin en 0, comme $\lvert x \rvert$, et n'y est pas dérivable. b) Juste à gauche de 2, la partie entière vaut 1 : le taux vaut $\frac{1 - 2}{h} = \frac{1}{\lvert h \rvert}$ (10, 100, …, $10^6$), sans limite finie ; à droite, il vaut 0. Une fonction qui saute n'est pas dérivable : elle n'est même pas continue. c) Les taux valent $\frac{h^2}{h} = h$ à droite et $\frac{0}{h} = 0$ à gauche : ils tendent vers 0 des deux côtés. $\big(\max(0, x)\big)^2$ est dérivable en 0, de dérivée 0, alors que $\max(0, x)$ y fait un coin.

**Pour la copie.** Seule la fonction c) est dérivable en son point. Un nombre dérivé existe quand les taux ont **la même limite finie** des deux côtés : un coin donne deux limites différentes, un saut une limite infinie.

**Erreurs fréquentes.** Croire qu'une fonction sans formule « bizarre » est toujours dérivable (a) ; regarder un seul côté (b : à droite, tout semble tranquille) ; confondre $\max(0, x)$, qui fait un coin, et son carré, qui se raccorde en douceur.

### Ex R7.22 — Zoomer sur une courbe jusqu'à voir une droite

**Réponses** : a) `[0.03131, 0.00568, 0.00056, 0.00006]` · b) `[0.0626, 0.0568, 0.0557, 0.0556]` · c) `[1, 1, 1, 1]` · d) `0.056`.

**Démarche.** `xs = np.linspace(a - w, a + w, 1001)`, puis `float(np.max(np.abs(f(xs) - line(xs))))`. La courbe de ln est sous sa tangente, et l'écart est le plus grand au bord gauche : $-\frac{w}{3} - \ln\left(1 - \frac{w}{3}\right)$. Les rapports de a) tendent vers 0 (la courbe se confond avec sa tangente) ; ceux de b) se stabilisent vers 0,0556 (c'est $\frac{1}{18}$) : l'écart est de l'ordre de $w^2$, comme le petit carré du coin de la fiche (§4). Pour $\lvert x \rvert$, le rapport reste 1 : aucune droite ne colle au coin.

**Erreurs fréquentes.** Oublier la valeur absolue (le maximum de différences négatives vaut 0, atteint au point de contact) ; une grille sans les bornes ; diviser par $w$ en b.

### Ex R7.23 — Tracer f, f′ et des tangentes

**Réponses** : a) `[-1, 0, 1]` · b) `1`.

**Démarche.** Dans `axes[0]` : la courbe, puis pour chaque $p$ le segment `f(p) + df(p) * (s - p)` sur $[p - 0{,}3 \;;\; p + 0{,}3]$ et le point $(p \;;\; f(p))$ ; dans `axes[1]` : `df` et `axhline(0)`. $f'(x) = 6x(x^2 - 1)^2$ s'annule en −1, 0 et 1, mais le facteur $(x^2 - 1)^2$ n'est jamais négatif : $f'$ a le signe de $x$, et ne change de signe qu'en 0. Un seul minimum local, $f(0) = -1$.

**Pour la copie.** $f$ monte là où la courbe de droite est au-dessus de l'axe, ici pour $x > 0$. La tangente en 1 est horizontale, mais $f$ n'y a pas d'extremum : la courbe traverse sa tangente (elle monte avant 1 et après 1), et la courbe de $f'$ touche l'axe en 1 sans le traverser.

**Erreurs fréquentes.** Ouvrir une figure dans la fonction ; tracer $f$ dans les deux axes ; donner les zéros de $f$ (−1 et 1) en a ; compter trois extremums en b.

### Ex R7.24 — Chasse à l'erreur : quatre dérivées fausses

**Réponses** : a) `"ACDE"` · b) `[8.0829, -5.0, 1210.2864, 1.3333, 0.5, 12.25]`.

**Démarche.** (A) $\left(x^2\sqrt{x + 1}\right)' = 2x\sqrt{x + 1} + \frac{x^2}{2\sqrt{x + 1}}$ : la règle du produit, pas le produit des dérivées. (C) $(e^{3x})' = 3e^{3x}$. (D) $\big(\ln(x^3 + 1)\big)' = \frac{3x^2}{x^3 + 1}$. (E) $(\sqrt{2x})' = \frac{2}{2\sqrt{2x}} = \frac{1}{\sqrt{2x}}$. (B) est juste malgré son signe moins : $\frac{1 \times (x - 3) - (x + 2) \times 1}{(x - 3)^2} = \frac{-5}{(x - 3)^2}$ ; (F) aussi (la dérivée de $-\frac{1}{x}$ est $+\frac{1}{x^2}$, ce qui peut surprendre). En 2, `slope` donne des valeurs proches des dérivées corrigées.

**Erreurs fréquentes.** Accuser (B) ou (F) à cause de leur signe ; corriger (A) avec un seul des deux termes de la règle du produit.

### Ex R7.25 — Tester une dérivée avec pytest et SymPy

**Réponses** : a) `True` · b) `True`.

**Démarche.** $g'(x) = \frac{2x(x + 3) - (x^2 + 1)}{(x + 3)^2} = \frac{x^2 + 6x - 1}{(x + 3)^2}$. Le test crée son symbole (`X = sp.symbols("x")`, dans la fonction : pytest l'exécute seul), calcule `exact = sp.diff((X**2 + 1) / (X + 3), X)`, puis, pour plusieurs points (dont un négatif), `assert math.isclose(dg(p), float(exact.subs(X, p)), rel_tol=1e-12)`. Il passe sur la bonne dérivée et échoue sur `dg_bug`.

**Erreurs fréquentes.** Un test qui utilise un nom défini dans une autre cellule (pytest lève `NameError`) ; un test qui ne compare qu'en un point (une dérivée fausse peut y être juste par hasard) ; comparer avec `==` des flottants ; choisir $-3$, où $g$ n'est pas définie.
