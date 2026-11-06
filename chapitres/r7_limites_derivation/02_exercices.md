# R7 · Limites et dérivation — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r7_limites_derivation/06_mes_reponses.md` (créée par `python tools/start_chapter.py R7`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂ et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées ; les limites et les dérivées se calculent à la main, avec les règles de la fiche. Écris toujours la dérivée avant d'en calculer une valeur.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R7.Q1 — Limites : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Vrai ou faux ?
1. $\lim_{x \to +\infty} \frac{1}{x^2} = 0$.
2. Si $f(x) \to +\infty$ et $g(x) \to +\infty$ quand $x \to +\infty$, alors $f(x) - g(x) \to 0$.
3. $\lim_{x \to +\infty} \frac{3x^2 + 1}{x^3} = 3$.
4. $\lim_{x \to +\infty} \frac{e^x}{x^{20}} = +\infty$.
5. La droite $x = 4$ est une asymptote de la courbe de $x \mapsto \frac{1}{x - 4}$.
6. Une fonction peut avoir une limite finie en un point $a$ où elle n'est pas définie.
7. $\lim_{x \to 0^-} \frac{1}{x} = +\infty$.

### R7.Q2 — Continue ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. La fonction $x \mapsto \frac{1}{x}$ est-elle continue en chaque point où elle est définie ?
2. La fonction marche (0 pour $x < 0$, 1 pour $x \ge 0$) est-elle continue en 0 ? En 0,5 ?
3. $f$ est continue sur $[0 \;;\; 1]$, $f(0) = -2$ et $f(1) = 5$ : $f$ prend-elle la valeur 3 ?
4. Vrai ou faux : une fonction telle que $f(0) = -1$ et $f(1) = 1$ s'annule forcément entre 0 et 1.
5. Après 10 étapes de dichotomie partant de $[0 \;;\; 1]$, quelle est la longueur de l'intervalle ?
6. Vrai ou faux : la dichotomie trouve un zéro de $x \mapsto x^2$ sur $[-1 \;;\; 2]$.

### R7.Q3 — Le nombre dérivé est une pente 🧠 ★ ⏱️ 4 min
*Fiche §3 et §4 · parcours C, E*

1. Vrai ou faux : le taux d'accroissement de $f$ entre $a$ et $a + h$ est la pente d'une droite qui passe par deux points de la courbe.
2. Si $f'(-1) = 4$, la fonction monte-t-elle ou descend-elle en passant par −1 ?
3. $f(5) = 2$ et $f'(5) = 4$ : une valeur approchée de $f(5{,}1)$ ?
4. Vrai ou faux : la tangente en $a$ a pour équation $y = f'(a)(x - a)$.
5. Vrai ou faux : une fonction continue en $a$ est dérivable en $a$.
6. $d(t)$ est une distance en kilomètres et $t$ un temps en heures : quelle est l'unité de $d'(t)$ ?

### R7.Q4 — Dérivées usuelles 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Donne la dérivée de :
1. $x^8$
2. $\frac{1}{x}$
3. $\sqrt{x}$
4. $e^x$
5. $\ln x$
6. $7$
7. $x^{-3}$

### R7.Q5 — Produit, quotient : quelle formule ? 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

Vrai ou faux ?
1. $(uv)' = u'\,v'$.
2. $(5u)' = 5u'$.
3. $\left(\frac{u}{v}\right)' = \frac{u\,v' - u'\,v}{v^2}$.
4. $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$.
5. Pour dériver $\frac{x + 1}{x}$, la règle du quotient est indispensable.
6. $f$ et $f + 10$ ont la même dérivée.

### R7.Q6 — Règle de la chaîne : qu'y a-t-il « dedans » ? 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Pour chaque fonction, nomme l'étage intérieur $u$ et l'étage extérieur (la fonction de $u$) :
1. $(2x - 7)^6$
2. $e^{x^3}$
3. $\ln(4 - x)$
4. $\sqrt{e^x + 1}$
5. $(e^x + x)^3$
6. Vrai ou faux : $\big(\ln(2x)\big)' = \frac{1}{2x}$.

### R7.Q7 — Dérivée nulle, extremum ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. La fonction $x \mapsto x^3 + x$ a-t-elle un extremum local ?
2. $f'$ passe du signe $+$ au signe $-$ en $c$ : maximum ou minimum local ?
3. Sur $[0 \;;\; 4]$, $f'(x) > 0$ partout : où $f$ atteint-elle son maximum sur cet intervalle ?
4. Vrai ou faux : $\lvert x \rvert$ a un minimum en 0, bien qu'elle n'y soit pas dérivable.
5. $f' < 0$ sur $]0 \;;\; 2[$ : compare $f(0{,}5)$ et $f(1{,}5)$.
6. Vrai ou faux : un maximum local est toujours la plus grande valeur de la fonction.

### R7.Q8 — Qui domine qui ? 🧠 ★ ⏱️ 4 min
*Fiche §9 · parcours C*

1. Vrai ou faux : $3n^2 + 100n = O(n^2)$.
2. Vrai ou faux : $n^3 = O(n^2)$.
3. Pour $n$ très grand, lequel est le plus grand : $2^n$ ou $n^{10}$ ?
4. Deux boucles imbriquées de $n$ tours chacune : quel coût, en grand O ?
5. Vrai ou faux : $\log_2 n = O(\ln n)$.
6. Un algorithme en $O(n^2)$ met 2 secondes pour $n = 1\,000$ : combien, environ, pour $n = 10\,000$ ?

<a id="rappels"></a>

## 🔁 Rappels

### R7.R1 — Croissances comparées (R6) 🔁 ★ ⏱️ 5 min
*Fiche §1 et §9 · parcours C, E*

1. $\lim_{x \to +\infty} \frac{x^3}{e^x}$ ?
2. $\lim_{x \to +\infty} \frac{\ln x}{x^{0{,}1}}$ ?
3. Range du plus lent au plus rapide, pour $x$ très grand : $x^2$, $e^{0{,}1x}$, $\ln x$.

### R7.R2 — Limite d'une suite (R5) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. $\lim_{n \to +\infty} \frac{2n + 1}{n}$ ?
2. $\lim_{n \to +\infty} 0{,}9^n$ ?
3. Vers quel nombre tend $\left(1 + \frac{1}{n}\right)^n$ ?

### R7.R3 — Sommet d'une parabole (R3) 🔁 ★ ⏱️ 5 min
*Fiche §8 · parcours C*

1. Le sommet de la parabole $y = x^2 - 6x + 5$ ?
2. Le maximum de $x \mapsto -2x^2 + 8x$, et où il est atteint ?
3. $y = 3(x - 1)^2 + 2$ : le sommet est-il un minimum ou un maximum, et que vaut-il ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre avec un point décimal, comme `-1.5`, arrondi comme le demande la question ; une limite infinie par `"+oo"` ou `"-oo"` ;
- une fraction exacte entre guillemets, comme `"5/7"` ;
- une expression entre guillemets, comme `"3*x**2 - 1"` (`*` pour multiplier, `**` pour la puissance ; `exp(x)`, `log(x)` pour $\ln x$, `sqrt(x)`) ;
- un intervalle entre guillemets, comme `"[-2 ; 4["` (`-oo` et `+oo` pour l'infini) ;
- une liste de nombres entre crochets (une droite $y = mx + p$ par la liste `[m, p]`) ; vrai ou faux par `True` ou `False`.

### Ex R7.1 — Limites en l'infini des fonctions de référence ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des limites en l'infini, en levant les formes indéterminées par le terme dominant et par les croissances comparées.
**Prérequis :** fiche §1 ; R6 §5 · **Parcours :** C, E

Limites quand $x \to +\infty$, sauf à la ligne h.

| | Limite | Réponse attendue |
|---|---|---|
| a | $5 - \dfrac{3}{x}$ | un nombre |
| b | $x^3 - 100x^2$ | un nombre ou `"+oo"`, `"-oo"` |
| c | $\dfrac{4x + 1}{2x - 3}$ | un nombre |
| d | $\dfrac{x^2 + 1}{x^3 - 2}$ | un nombre |
| e | $e^{-2x} + 1$ | un nombre |
| f | $(x^2 + 1)\,e^{-x}$ | un nombre |
| g | $\dfrac{\sqrt{x}}{\ln x}$ | un nombre ou `"+oo"`, `"-oo"` |
| h | $x^3 + 2x$, quand $x \to -\infty$ | un nombre ou `"+oo"`, `"-oo"` |

### Ex R7.2 — Limites et asymptotes de fonctions rationnelles ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des limites en l'infini et en un point, distinguer une asymptote verticale d'un trou, et donner les asymptotes d'une courbe.
**Prérequis :** fiche §1 ; R2 (factoriser) · **Parcours :** C

On pose $f(x) = \dfrac{3x - 2}{x + 1}$, $g(x) = \dfrac{x^2 + x - 6}{x - 2}$ et $k(x) = \dfrac{2x^2 + 3}{x^2 - 9}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lim_{x \to +\infty} f(x)$ | un nombre |
| b | $\lim_{x \to -1^+} f(x)$ (par la droite) | un nombre ou `"+oo"`, `"-oo"` |
| c | $\lim_{x \to -1^-} f(x)$ (par la gauche) | un nombre ou `"+oo"`, `"-oo"` |
| d | les asymptotes de $f$, $x = a$ et $y = L$ : la liste `[a, L]` | une liste |
| e | $\lim_{x \to 2} g(x)$ | un nombre |
| f | la courbe de $g$ a-t-elle une asymptote verticale d'équation $x = 2$ ? | vrai ou faux |
| g | les abscisses des asymptotes verticales de $k$, dans l'ordre croissant | une liste |
| h | $\lim_{x \to 3^+} k(x)$ | un nombre ou `"+oo"`, `"-oo"` |

### Ex R7.3 — Taux d'accroissement et nombre dérivé ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des taux d'accroissement, les simplifier, et en déduire une vitesse instantanée et un coût marginal.
**Prérequis :** fiche §3 · **Parcours :** C, E

Un objet lâché sans vitesse a parcouru $s(t) = 5t^2$ mètres au bout de $t$ secondes (on néglige l'air).

| | Question | Réponse attendue |
|---|---|---|
| a | sa vitesse moyenne entre $t = 2$ et $t = 2{,}5$, en m/s | un nombre |
| b | sa vitesse moyenne entre $t = 2$ et $t = 2{,}1$, en m/s | un nombre |
| c | le taux d'accroissement de $s$ entre 2 et $2 + h$, simplifié et développé, en fonction de $h$ | une expression en `h` |
| d | sa vitesse instantanée à $t = 2$, en m/s | un nombre |

Fabriquer $q$ pièces coûte $C(q) = 0{,}5q^2 + 3q + 100$ euros. Et $g(x) = 3x + 7$, $f(x) = x^2 - 5x$.

| | Question | Réponse attendue |
|---|---|---|
| e | le coût moyen de chacune des pièces supplémentaires quand on passe de 10 à 12 pièces : le taux d'accroissement de $C$ entre 10 et 12 | un nombre |
| f | le coût marginal en 10 pièces, $C'(10)$, à partir de la limite du taux | un nombre |
| g | le taux d'accroissement de $g$ entre deux nombres distincts quelconques | un nombre |
| h | le taux d'accroissement de $f$ entre 4 et $4 + h$ pour $h = -0{,}5$ | un nombre |

### Ex R7.4 — Équation de la tangente ✏️ ★ ⏱️ 15 min
**Objectif :** écrire l'équation d'une tangente, s'en servir pour une approximation affine, et trouver une tangente horizontale.
**Prérequis :** fiche §4 · **Parcours :** C, E

On admet les dérivées (fiche §5) : $(x^2 - 5x)' = 2x - 5$, $(e^x)' = e^x$, $(\ln x)' = \frac{1}{x}$, $(\sqrt{x})' = \frac{1}{2\sqrt{x}}$, $(x^3)' = 3x^2$. Une tangente $y = mx + p$ se répond par la liste `[m, p]`.

| | Question | Réponse attendue |
|---|---|---|
| a | la tangente à la courbe de $x \mapsto x^2 - 5x$ au point d'abscisse 4 | une liste |
| b | la tangente à la courbe de exp au point d'abscisse 1 | une liste (3 décimales) |
| c | la tangente à la courbe de ln au point d'abscisse 2 | une liste (3 décimales) |
| d | la tangente à la courbe de $x \mapsto \sqrt{x}$ au point d'abscisse 4 | une liste |
| e | l'approximation de $\sqrt{4{,}2}$ que donne la tangente de d | un nombre (2 décimales) |
| f | l'écart entre cette approximation et la vraie valeur de $\sqrt{4{,}2}$ (approximation moins vraie valeur) | un nombre (5 décimales) |
| g | l'abscisse du point où la tangente à la courbe de $x \mapsto x^2 - 5x$ est horizontale | un nombre |
| h | l'abscisse du point où la tangente à la courbe de $x \mapsto x^3$ en 1 coupe l'axe des abscisses | une fraction |

### Ex R7.5 — Dériver les fonctions usuelles ✏️ ★ ⏱️ 15 min
**Objectif :** dériver avec le tableau des dérivées usuelles, la somme et la constante multiplicative, après avoir réécrit la fonction si besoin.
**Prérequis :** fiche §5 et §6 (somme, constante) ; R6 §1 et §3 · **Parcours :** C, E

Donne $f'(x)$ pour chaque fonction (là où elle est définie).

| | $f(x)$ | Réponse attendue |
|---|---|---|
| a | $x^7$ | une expression en `x` |
| b | $2x^6 - 7x^3 + x$ | une expression en `x` |
| c | $\dfrac{1}{x^3}$ | une expression en `x` |
| d | $x\sqrt{x}$ | une expression en `x` |
| e | $x^{2/3}$ | une expression en `x` |
| f | $3e^x - 4\ln x$ | une expression en `x` |
| g | $\ln(5x)$, pour $x > 0$ (récris-la d'abord avec R6) | une expression en `x` |
| h | $e^{x + 2}$ (récris-la d'abord avec R6) | une expression en `x` |

### Ex R7.6 — Dériver des produits et des quotients ✏️ ★★ ⏱️ 20 min
**Objectif :** appliquer les règles du produit et du quotient, et simplifier le résultat.
**Prérequis :** fiche §6 · **Parcours :** C, E

| | $f(x)$ | Réponse attendue |
|---|---|---|
| a | $e^x \ln x$ | une expression en `x` |
| b | $(x^2 + 1)(3x - 2)$ | une expression en `x` |
| c | $\sqrt{x}\,\ln x$ | une expression en `x` |
| d | $\dfrac{x - 4}{2x + 1}$ | une expression en `x` |
| e | $\dfrac{x}{x^2 + 1}$ | une expression en `x` |
| f | $\dfrac{e^x}{x + 1}$ | une expression en `x` |
| g | la valeur en $x = 1$ de la dérivée de a | un nombre (3 décimales) |
| h | $\dfrac{1}{e^x + x}$ | une expression en `x` |

### Ex R7.7 — Dériver des composées ✏️ ★★ ⏱️ 25 min
**Objectif :** dériver une composée en nommant l'étage intérieur, avec la règle de la chaîne.
**Prérequis :** fiche §7 · **Parcours :** C, E

Pour chaque fonction, nomme $u$ dans ta copie, dérive chaque étage, puis multiplie.

| | $f(x)$ | Réponse attendue |
|---|---|---|
| a | $(2x^2 - 1)^3$ | une expression en `x` |
| b | $10\,e^{-x/5}$ | une expression en `x` |
| c | $\ln(3x + 2)$ | une expression en `x` |
| d | $\sqrt{x^3 + 1}$, pour $x > -1$ | une expression en `x` |
| e | $e^{\sqrt{x}}$ | une expression en `x` |
| f | $\ln(\ln x)$, pour $x > 1$ | une expression en `x` |
| g | $\dfrac{1}{x^2 + x}$, écrite $(x^2 + x)^{-1}$ | une expression en `x` |
| h | la valeur en $x = 1$ de la dérivée de $\ln(x^2 + 2x)$ | une fraction |

### Ex R7.8 — Variations et tableau de variations ✏️ ★★ ⏱️ 25 min
**Objectif :** étudier le signe d'une dérivée, en déduire les variations et les extremums, y compris aux bords d'un intervalle.
**Prérequis :** fiche §8 ; R3 (second degré) · **Parcours :** C, E

On pose $f(x) = x^4 - 4x^3 + 10$, définie sur $\mathbb{R}$. Dresse son tableau de variations dans ta copie.

| | Question | Réponse attendue |
|---|---|---|
| a | $f'(x)$ | une expression en `x` |
| b | les points où $f'$ s'annule, dans l'ordre croissant | une liste |
| c | l'intervalle sur lequel $f$ est décroissante (le plus grand possible) | un intervalle |
| d | le nombre d'extremums locaux de $f$ | un nombre entier |
| e | la plus petite valeur de $f$ sur $\mathbb{R}$ | un nombre |
| f | la plus grande valeur de $f$ sur l'intervalle $[-1 \;;\; 4]$ | un nombre |

Puis $g(x) = x - 2\ln x$, sur $]0 \;;\; +\infty[$.

| | Question | Réponse attendue |
|---|---|---|
| g | l'abscisse où $g$ atteint son minimum | un nombre |
| h | la valeur de ce minimum | un nombre (3 décimales) |

### Ex R7.9 — Optimiser : la boîte de volume maximal ✏️ ★★ ⏱️ 25 min
**Objectif :** mettre un problème d'optimisation en équation, préciser le domaine, et trouver un maximum avec la dérivée.
**Prérequis :** fiche §8 · **Parcours :** C, E

Dans une feuille de carton de 16 cm sur 10 cm, on découpe un carré de côté $x$ cm à chaque coin, puis on relève les bords pour former une boîte sans couvercle. Son volume est $V(x) = x(16 - 2x)(10 - 2x)$ cm³.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs de $x$ possibles (une boîte qui existe vraiment) | un intervalle |
| b | $V(x)$ développé | une expression en `x` |
| c | $V'(x)$ | une expression en `x` |
| d | le point du domaine où $V'$ s'annule | un nombre |
| e | le volume maximal, en cm³ | un nombre |
| f | les dimensions de cette boîte : longueur, largeur, hauteur, en cm | une liste |

### Ex R7.10 — La règle de la chaîne en série : trois étages, et l'ordre qui compte ✏️ ★★ ⏱️ 25 min
**Objectif :** dériver des composées de trois étages, calculer des dérivées en un point, et voir que l'ordre de la composition change la dérivée.
**Prérequis :** fiche §7 ; R6 §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la dérivée de $e^{(x^2 + 1)^3}$ | une expression en `x` |
| b | la dérivée de $\sqrt{\ln x}$, pour $x > 1$ | une expression en `x` |
| c | la dérivée de $(2 + e^x)^3$ | une expression en `x` |
| d | la dérivée de $\ln\big((2x + 1)^2\big)$, pour $x > -\frac{1}{2}$ | une expression en `x` |
| e | la valeur en $x = 2$ de la dérivée de $(x^2 - 3)^5$ | un nombre |
| f | la valeur en $x = 1$ de la dérivée de $\ln(x^2 + e^x)$ | un nombre (3 décimales) |
| g | la valeur en $x = 0$ de la dérivée de $\sqrt{e^{2x} + 3}$ | un nombre |
| h | les valeurs en $x = 2$ des dérivées de $\left(e^x\right)^2$ et de $e^{x^2}$, dans cet ordre | une liste (3 décimales) |

### Ex R7.11 — Dériver par rapport à une lettre, les autres fixées : A e^(kt), π r² h, ½ m v² ✏️ ★★ ⏱️ 20 min
**Objectif :** dériver une formule à plusieurs lettres par rapport à l'une d'elles, en traitant les autres comme des constantes.
**Prérequis :** fiche §5 et §7 · **Parcours :** C, E

Une population vaut $N = A\,e^{kt}$ (au temps $t$, avec l'effectif initial $A$ et le taux $k$) ; un cylindre de rayon $r$ et de hauteur $h$ a pour volume $V = \pi r^2 h$ ; un objet de masse $m$ et de vitesse $v$ a l'énergie cinétique $E = \frac{1}{2} m v^2$. Réponds avec les mêmes lettres (`A`, `k`, `t`, `r`, `h`, `m`, `v`, et `pi` pour $\pi$).

| | Question | Réponse attendue |
|---|---|---|
| a | $\frac{dN}{dt}$ ($A$ et $k$ fixés) | une expression |
| b | $\frac{dN}{dk}$ ($A$ et $t$ fixés) | une expression |
| c | $\frac{dN}{dA}$ ($k$ et $t$ fixés) | une expression |
| d | $\frac{dV}{dr}$ ($h$ fixé) | une expression |
| e | $\frac{dV}{dh}$ ($r$ fixé) | une expression |
| f | la valeur de $\frac{dV}{dr}$ pour $r = 3$ et $h = 10$ | un nombre (2 décimales) |
| g | $\frac{dE}{dv}$ ($m$ fixée) | une expression |
| h | $\frac{dE}{dm}$ ($v$ fixée) | une expression |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex R7.12 — La dérivée de x² à partir de la définition, et |x| qui n'est pas dérivable en 0 ∂ ★★ ⏱️ 20 min
**Objectif :** calculer une dérivée à partir de la définition, et démontrer qu'une fonction continue n'est pas dérivable en un point.
**Prérequis :** fiche §3 · **Parcours :** C, E

1. Soit $f(x) = x^2$ et $a$ un réel. Calcule le taux d'accroissement $\frac{f(a + h) - f(a)}{h}$ pour $h \ne 0$, et simplifie-le.
2. Déduis-en que $f$ est dérivable en tout réel $a$, et que $f'(a) = 2a$.
3. Soit $g(x) = \lvert x \rvert$. Calcule le taux d'accroissement de $g$ entre 0 et $h$, d'abord pour $h > 0$, puis pour $h < 0$.
4. Conclus : $g$ n'est pas dérivable en 0. Explique pourquoi elle est pourtant continue en 0.
5. Montre que $g$ est dérivable en tout $a \ne 0$, et donne $g'(a)$ selon le signe de $a$.

### Ex R7.13 — Démontrer la règle du produit ∂ ★★ ⏱️ 35 min
**Objectif :** démontrer la règle du produit à partir de la définition de la dérivée, puis en déduire la dérivée des puissances entières.
**Prérequis :** fiche §3 et §6 ; R4 §7 (récurrence) · **Parcours :** C

Soient $u$ et $v$ deux fonctions dérivables en $a$.
1. Montre que $v$ est continue en $a$ : écris $v(a + h) - v(a) = h \times \frac{v(a + h) - v(a)}{h}$ et fais tendre $h$ vers 0.
2. Vérifie l'égalité $u(a + h)\,v(a + h) - u(a)\,v(a) = \big(u(a + h) - u(a)\big)\,v(a + h) + u(a)\,\big(v(a + h) - v(a)\big)$.
3. Divise par $h$ et fais tendre $h$ vers 0 : déduis-en que $(uv)'(a) = u'(a)\,v(a) + u(a)\,v'(a)$. Où sers-tu la question 1 ?
4. Démontre par récurrence que $(x^n)' = n\,x^{n-1}$ pour tout entier $n \ge 1$ (avec $x^{n+1} = x^n \times x$).
5. Déduis de 3 la dérivée de $u^2$, puis celle de $u^3$, en fonction de $u$ et $u'$.

### Ex R7.14 — La règle du quotient à partir de la règle du produit : (1/v)′ = −v′/v² ∂ ★★ ⏱️ 25 min
**Objectif :** déduire la règle du quotient de la règle du produit, et l'appliquer aux puissances négatives.
**Prérequis :** fiche §6 · **Parcours :** C, E

Soit $v$ une fonction dérivable qui ne s'annule pas. On admet que $\frac{1}{v}$ est dérivable.
1. Dérive les deux membres de l'égalité $v(x) \times \frac{1}{v(x)} = 1$ avec la règle du produit.
2. Déduis-en que $\left(\frac{1}{v}\right)' = -\frac{v'}{v^2}$.
3. Écris $\frac{u}{v} = u \times \frac{1}{v}$ et déduis-en la règle du quotient $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$.
4. Applique 2 à $v(x) = x^n$ ($n \ge 1$ entier, $x \ne 0$) : montre que $(x^{-n})' = -n\,x^{-n-1}$. Que dit ce résultat de la règle $(x^m)' = m\,x^{m-1}$ ?
5. Applique 2 à $v(x) = x^3 + 2$ : donne la dérivée de $\frac{1}{x^3 + 2}$, et vérifie-la avec la règle de la chaîne (fiche §7).

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R7.15 — Minimiser une fonction de coût donnée par une formule : dériver, annuler, vérifier 🔗 ★★ ⏱️ 20 min
**Objectif :** trouver le minimum d'une fonction de coût en annulant sa dérivée, puis vérifier que c'est bien un minimum.
**Prérequis :** fiche §5 à §8 · **Parcours :** C, E

Un réglage $a > 0$ d'un modèle donne une erreur modélisée par $E(a) = 2a + \frac{8}{a} + 1$ : le terme $2a$ grandit avec le réglage, le terme $\frac{8}{a}$ diminue. Puis un seuil $t$ (un réel quelconque) donne un coût $L(t) = e^{t} + 4e^{-t}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $E'(a)$ | une expression en `a` |
| b | le réglage $a^*$ qui minimise $E$ | un nombre |
| c | l'erreur minimale $E(a^*)$ | un nombre |
| d | $E'(1)$ : son signe dit de quel côté de $a^*$ se trouve 1 | un nombre |
| e | le seuil $t^*$ qui minimise $L$ | un nombre (3 décimales) |
| f | le coût minimal $L(t^*)$ | un nombre |
| g | les valeurs $L(t^* - 0{,}1)$ et $L(t^* + 0{,}1)$, dans cet ordre | une liste (3 décimales) |

Dans ta copie : pourquoi annuler la dérivée ne suffit-il pas ? Comment as-tu vérifié que $a^*$ et $t^*$ sont des minimums, et pourquoi ces minimums sont-ils les plus petites valeurs sur tout le domaine, pas seulement au voisinage ?

### Ex R7.16 — Expliquer ce qu'est une dérivée sans écrire de formule 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement la dérivée, avec deux images concrètes.
**Prérequis :** fiche §3 et §4 · **Parcours :** C, E

Une amie te demande : « On me parle tout le temps de dérivées en machine learning. C'est quoi, une dérivée ? »

Réponds-lui **en huit lignes au plus, sans aucune formule**. Ta réponse doit contenir : une image de vitesse (un compteur de voiture, par exemple), l'idée d'un rapport entre deux petites variations, ce que dit le signe de la dérivée, ce que dit sa taille, et pourquoi c'est utile pour trouver le bas d'une courbe.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r7_limites_derivation/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R7.17 | Le taux d'accroissement · `difference_quotient` | 🔨 | ★ | 15 | C, E |
| R7.18 | La tangente à partir de f et de sa dérivée · `tangent_line` | 🔨 | ★★ | 20 | C |
| R7.19 | Trouver un zéro par dichotomie · `bisection` | 🔨 | ★★ | 25 | C, E |
| R7.20 | Vérifier ses dérivées avec `sympy.diff` | 📦 | ★ | 15 | C, E |
| R7.21 | Prédire : le taux d'accroissement a-t-il toujours une limite quand h tend vers 0 ? | 🔮 | ★★ | 15 | C |
| R7.22 | Zoomer sur une courbe jusqu'à voir une droite | 🔬 | ★★ | 20 | C, E |
| R7.23 | Tracer f, f′ et des tangentes | 🎨 | ★★ | 20 | C |
| R7.24 | Chasse à l'erreur : quatre dérivées fausses | 🐛 | ★★ | 20 | C, E |
| R7.25 | Tester une dérivée avec pytest et SymPy | 🛠️ | ★ | 15 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
