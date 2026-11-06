# M02a · Intégrales et densités — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m02a_integrales_densites/06_mes_reponses.md` (créée par `python tools/start_chapter.py M02a`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Dessine la courbe et l'aire cherchée avant chaque calcul, garde les valeurs exactes ($\frac{8}{3}$, $\ln 2$, $e - 1$) jusqu'au bout, et vérifie chaque primitive en la dérivant.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M02a.Q1 — Aire, signe et intégrale 🧠 ★ ⏱️ 4 min
*Fiche §1 et §2 · parcours C, E*

1. Vrai ou faux : si $f \ge 0$ sur $[a ; b]$ (avec $a < b$), alors $\int_a^b f(x)\,dx$ est l'aire de la région entre la courbe et l'axe des abscisses.
2. Sans calcul, que vaut $\int_{-1}^1 x^3\,dx$ ? Pourquoi ?
3. Si $f(x) < 0$ pour tout $x$ de $[a ; b]$ (avec $a < b$), quel est le signe de $\int_a^b f(x)\,dx$ ?
4. Que vaut $\int_2^2 f(x)\,dx$, pour n'importe quelle fonction $f$ continue ?
5. Vrai ou faux : $\int_3^1 f(x)\,dx = -\int_1^3 f(x)\,dx$.
6. Pour une fonction croissante, la somme de Riemann avec les rectangles à gauche est-elle trop petite ou trop grande ?

### M02a.Q2 — Primitives : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Vrai ou faux ?
1. $\frac{x^3}{3} + 7$ est une primitive de $x^2$.
2. $e^{2x}$ est une primitive de $e^{2x}$.
3. $\ln x$ est une primitive de $\frac{1}{x}$ sur $]0 ; +\infty[$.
4. $\frac{x^0}{0}$ est une primitive de $x^{-1}$.
5. Deux primitives d'une même fonction sur un intervalle diffèrent d'une constante.
6. $\sin(x^2)$ est une primitive de $2x\cos(x^2)$.

### M02a.Q3 — Quelle méthode de calcul pour quelle intégrale ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C*

Pour chaque intégrale, quelle méthode choisirais-tu : (T) la table et la linéarité, (P) une intégration par parties, (C) un changement de variable ? Pour (C), donne aussi le $u$ que tu poserais.
1. $\int \left(3x^2 - \frac{4}{x}\right)dx$
2. $\int x \ln x\,dx$
3. $\int \frac{2x}{x^2 + 1}\,dx$
4. $\int x\,e^{3x}\,dx$
5. $\int \frac{e^x}{1 + e^x}\,dx$
6. $\int (x + 1)^2\,dx$ (deux méthodes conviennent : lesquelles ?)

### M02a.Q4 — Converge ou diverge ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Converge ou diverge ?
1. $\int_1^{+\infty} \frac{dx}{x^3}$
2. $\int_1^{+\infty} \frac{dx}{\sqrt{x}}$
3. $\int_0^1 \frac{dx}{x^2}$
4. $\int_0^{+\infty} e^{-3x}\,dx$
5. $\int_0^1 \frac{dx}{x^{1/3}}$
6. $\int_{-\infty}^{+\infty} e^{-x^2}\,dx$

### M02a.Q5 — Rectangles, trapèzes, Simpson 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Quelles méthodes donnent la valeur exacte de l'intégrale d'une fonction affine, avec n'importe quel nombre d'intervalles qu'elles acceptent ?
2. Quelle condition la méthode de Simpson impose-t-elle au nombre $n$ d'intervalles ?
3. Pour une fonction régulière, quand on divise le pas par 2, l'erreur des trapèzes est divisée par environ combien ?
4. Combien d'évaluations de $f$ demande la méthode des trapèzes avec $n = 10$ ?
5. Vrai ou faux : les rectangles à droite surestiment toujours l'intégrale.
6. Jusqu'à quel degré la méthode de Simpson est-elle exacte pour les polynômes ?

### M02a.Q6 — Densité et probabilité : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

$X$ est une variable aléatoire de densité $f$. Vrai ou faux ?
1. Une densité peut prendre des valeurs négatives.
2. $f(1)$ est la probabilité que $X$ vaille 1.
3. $P(X \le 2) = P(X < 2)$.
4. La fonction qui vaut 5 sur $[1 ; 1{,}2]$ et 0 ailleurs est une densité.
5. Si $f$ est une densité, $2f$ en est une aussi.
6. Pour un petit nombre $h > 0$, $P(x \le X \le x + h) \approx f(x)\,h$ (là où $f$ est continue).

### M02a.Q7 — Lire une fonction de répartition 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

La variable $X$ a pour fonction de répartition $F(x) = 0$ pour $x < 0$, $F(x) = \frac{x^2}{4}$ pour $0 \le x \le 2$, et $F(x) = 1$ pour $x > 2$.
1. $P(X \le 1)$ ?
2. $P(X > 1)$ ?
3. $P(1 < X \le 2)$ ?
4. La médiane de $X$ ?
5. La densité de $X$ sur $]0 ; 2[$ ?
6. Vrai ou faux : une fonction de répartition peut décroître sur un intervalle.

<a id="rappels"></a>

## 🔁 Rappels

### M02a.R1 — Dériver une composée (R7) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

1. La dérivée de $x \mapsto (3 - x^2)^4$ ?
2. La dérivée de $x \mapsto \ln(5 - 2x)$, pour $x < \frac{5}{2}$ ?
3. La dérivée de $x \mapsto e^{5x - 1}$ ?
4. La dérivée de $x \mapsto \sqrt{1 + x^2}$ ?

### M02a.R2 — Sommes Σ (R4) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. $\sum_{k=1}^{4} k^2$ ?
2. $\sum_{k=1}^{4} (3k - 2)$ ?
3. Écris $0{,}5 \times \big(f(0) + f(0{,}5) + f(1) + f(1{,}5)\big)$ avec le symbole $\Sigma$.
4. $\sum_{k=1}^{20} k$ ?

### M02a.R3 — Exponentielle et logarithme (R6) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C*

1. $\lim_{x \to +\infty} e^{-x}$ ?
2. $\lim_{x \to +\infty} x\,e^{-x}$ ?
3. $e^{\ln 5}$ et $\ln(e^{-2})$ ?
4. La solution de $e^{-2x} = \frac{1}{4}$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/9"` ;
- une valeur exacte entre guillemets, avec `sqrt`, `pi`, `exp` ou `ln`, comme `"sqrt(5)/3"` ;
- une expression en $x$ entre guillemets, avec `**` pour les puissances, `exp`, `ln`, `sqrt`, `sin` et `cos`, comme `"x**4/4 - 3*x"` (pour une primitive, sans la constante) ;
- une liste entre crochets, comme `[-1.25, 1]` ; un intervalle entre guillemets, comme `"]-oo ; -7]"` ; vrai ou faux par `True` ou `False`.

### Ex M02a.1 — Sommes de Riemann à la main : rectangles à gauche, à droite, au milieu ✏️ ★ ⏱️ 20 min
**Objectif :** calculer les trois sommes de Riemann d'une fonction, et s'en servir pour encadrer une aire.
**Prérequis :** fiche §1 ; R4 (Σ) · **Parcours :** C, E

On étudie $f(x) = 4 - x^2$ sur $[0 ; 2]$, une fonction décroissante sur cet intervalle. On note $L_n$, $R_n$ et $M_n$ ses sommes de Riemann à gauche, à droite et au milieu avec $n$ rectangles de même largeur.

| | Question | Réponse attendue |
|---|---|---|
| a | le pas $h$ pour $n = 4$ | un nombre (1 décimale) |
| b | $L_4$ | un nombre (2 décimales) |
| c | $R_4$ | un nombre (2 décimales) |
| d | $M_4$ | un nombre (3 décimales) |
| e | $L_4 - R_4$ | un nombre |
| f | $L_8$ | un nombre (4 décimales) |
| g | le plus petit $n$ pour lequel $L_n - R_n \le 0{,}1$ | un entier |
| h | pour tout $n$, l'aire sous la courbe est comprise entre $R_n$ et $L_n$ | vrai ou faux |

Dans ta copie : écris $L_n - R_n$ en fonction de $n$ ; pourquoi presque tous les termes des deux sommes disparaissent-ils dans la différence ?

### Ex M02a.2 — Primitives usuelles ✏️ ★ ⏱️ 15 min
**Objectif :** trouver des primitives avec la table et la linéarité, et vérifier chacune en la dérivant.
**Prérequis :** fiche §2 ; R7 (dérivées) · **Parcours :** C, E

Donne **une** primitive de chaque fonction (sans la constante), sur l'intervalle indiqué.

| | Fonction | Réponse attendue |
|---|---|---|
| a | $6x^2 - 4x + 5$ sur $\mathbb{R}$ | une expression en $x$ |
| b | $\frac{1}{x^3}$ sur $]0 ; +\infty[$ | une expression en $x$ |
| c | $\sqrt{x}$ sur $]0 ; +\infty[$ | une expression en $x$ |
| d | $e^{3x}$ sur $\mathbb{R}$ | une expression en $x$ |
| e | $\frac{1}{2x + 1}$ sur $\left]-\frac{1}{2} ; +\infty\right[$ | une expression en $x$ |
| f | $\cos(2x)$ sur $\mathbb{R}$ | une expression en $x$ |
| g | la primitive $F$ de $3x^2 + 1$ qui vérifie $F(1) = 0$ | une expression en $x$ (avec sa constante) |
| h | $\frac{4}{x} + e^{-x}$ sur $]0 ; +\infty[$ | une expression en $x$ |

### Ex M02a.3 — Intégrales et aires : le signe, l'aire entre deux courbes ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des intégrales par le théorème fondamental, et distinguer l'intégrale d'une aire géométrique.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\int_1^4 (2x - 1)\,dx$ | un entier |
| b | $\int_0^{\ln 3} e^x\,dx$ | un entier |
| c | $\int_1^{e^3} \frac{2}{x}\,dx$ | un entier |
| d | $\int_{-1}^{2} (x^2 - 2x)\,dx$ | un entier |
| e | l'aire géométrique de la région comprise entre la courbe de $x^2 - 2x$ et l'axe des abscisses, pour $x$ de $-1$ à $2$ | une fraction irréductible |
| f | les abscisses des points d'intersection des courbes $y = 2x$ et $y = x^2$ | une liste, dans l'ordre croissant |
| g | l'aire de la région comprise entre ces deux courbes | une fraction irréductible |
| h | $\int_0^{\pi} \sin x\,dx$ | un entier |

Dans ta copie : dessine la courbe de $x^2 - 2x$ sur $[-1 ; 2]$, et explique pourquoi d) et e) diffèrent.

### Ex M02a.4 — Intégration par parties ✏️ ★★ ⏱️ 20 min
**Objectif :** choisir les deux facteurs d'une intégration par parties, et l'appliquer une ou deux fois.
**Prérequis :** fiche §3 · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | dans $\int x\,e^{2x}\,dx$, le facteur à dériver (le $u$ de la formule) : 1 pour $x$, 2 pour $e^{2x}$ | 1 ou 2 |
| b | $\int_0^1 x\,e^{2x}\,dx$ | un nombre (4 décimales) |
| c | une primitive de $x\cos x$ sur $\mathbb{R}$ | une expression en $x$ |
| d | $\int_1^e \ln x\,dx$ (écris $\ln x = \ln x \times 1$) | un entier |
| e | une primitive de $x \ln x$ sur $]0 ; +\infty[$ | une expression en $x$ |
| f | $\int_0^1 x^2 e^x\,dx$ (deux intégrations par parties) | un nombre (4 décimales) |

### Ex M02a.5 — Changement de variable ✏️ ★★ ⏱️ 20 min
**Objectif :** repérer le changement de variable qui simplifie une intégrale, et changer les bornes avec lui.
**Prérequis :** fiche §3 ; R7 (règle de la chaîne) · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | dans $\int_0^1 (2x + 3)^5\,dx$, on pose $u = 2x + 3$ : les nouvelles bornes, dans l'ordre | une liste |
| b | $\int_0^1 3x^2 (x^3 + 1)^4\,dx$ | une fraction irréductible |
| c | une primitive de $\frac{x}{x^2 + 4}$ sur $\mathbb{R}$ | une expression en $x$ |
| d | $\int_0^1 e^{2x + 1}\,dx$ | un nombre (4 décimales) |
| e | $\int_0^2 x\,e^{-x^2}\,dx$ | un nombre (4 décimales) |
| f | $\int_1^e \frac{(\ln x)^2}{x}\,dx$ | une fraction irréductible |

### Ex M02a.6 — Intégrales impropres : converge, diverge, valeur ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une intégrale impropre comme une limite, et reconnaître les intégrales qui convergent.
**Prérequis :** fiche §4 ; R6 (limites de exp) · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\int_3^{+\infty} \frac{dx}{x^2}$ | une fraction irréductible |
| b | $\int_0^{+\infty} e^{-x/3}\,dx$ | un entier |
| c | $\int_0^4 \frac{dx}{\sqrt{x}}$ | un entier |
| d | $\int_1^{+\infty} \frac{dx}{x^{0{,}9}}$ converge | vrai ou faux |
| e | $\int_{-\infty}^0 e^{2x}\,dx$ | une fraction irréductible |
| f | l'ensemble des nombres $p$ pour lesquels $\int_1^{+\infty} \frac{dx}{x^p}$ converge | un intervalle |
| g | $\int_1^{+\infty} \frac{dx}{x^5}$ | une fraction irréductible |
| h | $\int_0^{+\infty} e^{-x^2}\,dx$, avec l'intégrale de Gauss | une valeur exacte |

### Ex M02a.7 — Trapèzes et Simpson à la main, et leurs erreurs ✏️ ★★ ⏱️ 20 min
**Objectif :** appliquer les méthodes des trapèzes et de Simpson à la main, et mesurer leurs erreurs.
**Prérequis :** fiche §5 · **Parcours :** C

On admet que $\int_0^1 \frac{4}{1 + x^2}\,dx = \pi$. On note $T_n$ et $S_n$ les approximations par les trapèzes et par Simpson avec $n$ intervalles. Garde 6 chiffres après la virgule dans les calculs intermédiaires.

| | Question | Réponse attendue |
|---|---|---|
| a | $T_2$ | un nombre (1 décimale) |
| b | $S_2$ | une fraction irréductible |
| c | $T_4$ | un nombre (4 décimales) |
| d | l'erreur $\lvert T_2 - \pi \rvert$ | un nombre (4 décimales) |
| e | le rapport des erreurs $\frac{\lvert T_2 - \pi \rvert}{\lvert T_4 - \pi \rvert}$ | un nombre (1 décimale) |
| f | $S_4$ | un nombre (5 décimales) |
| g | le nombre d'évaluations de la fonction pour calculer $S_4$ | un entier |
| h | la méthode des trapèzes donne la valeur exacte de $\int_0^3 (5 - 2x)\,dx$, quel que soit $n$ | vrai ou faux |

### Ex M02a.8 — Vérifier qu'une fonction est une densité, trouver sa constante ✏️ ★ ⏱️ 20 min
**Objectif :** trouver la constante qui fait d'une fonction une densité, et reconnaître une densité.
**Prérequis :** fiche §4 et §6 · **Parcours :** C, E

Chaque fonction est nulle en dehors de l'intervalle indiqué. La constante $c$ est positive.

| | Question | Réponse attendue |
|---|---|---|
| a | la constante $c$ qui fait de $c\,x$ sur $[0 ; 4]$ une densité | une fraction irréductible |
| b | la constante $c$ qui fait de $c\,e^{-2x}$ sur $[0 ; +\infty[$ une densité | un entier |
| c | la constante $c$ qui fait de $\frac{c}{x^2}$ sur $[1 ; +\infty[$ une densité | un entier |
| d | la constante $c$ qui fait de $c\,(3 - x)$ sur $[0 ; 3]$ une densité | une fraction irréductible |
| e | $g(x) = x - 1$ sur $[0 ; 2]$ est une densité | vrai ou faux |
| f | $h(x) = 3$ sur $\left[0 ; \frac{1}{3}\right]$ est une densité | vrai ou faux |
| g | pour la densité de a), $P(1 \le X \le 3)$ | une fraction irréductible |
| h | la plus grande valeur prise par la densité de b) | un entier |

### Ex M02a.9 — La probabilité d'un intervalle, et la valeur moyenne d'une fonction ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des probabilités d'intervalles avec une densité, et la valeur moyenne d'une fonction.
**Prérequis :** fiche §4, §6 et §8 · **Parcours :** C, E

La variable $X$ a pour densité $f(x) = \frac{3}{8}x^2$ sur $[0 ; 2]$ (et 0 ailleurs). Le temps $T$ (en minutes) entre deux appels reçus par un standard téléphonique a pour densité $0{,}2\,e^{-0{,}2t}$ pour $t \ge 0$ (et 0 pour $t < 0$). Garde les valeurs exactes ($e^{-2}$, $e^{-1}$) jusqu'au calcul final, puis arrondis.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X \le 1)$ | une fraction irréductible |
| b | $P(1 \le X \le 2)$ | une fraction irréductible |
| c | $P(X = 1)$ | un nombre |
| d | $P(0{,}5 < X < 1{,}5)$ | une fraction irréductible |
| e | $P(T > 10)$ | un nombre (4 décimales) |
| f | $P(5 \le T \le 10)$ | un nombre (4 décimales) |
| g | la valeur moyenne de $x \mapsto x^2$ sur $[0 ; 3]$ | un entier |
| h | la valeur moyenne de $x \mapsto \frac{1}{x}$ sur $[1 ; e]$ | un nombre (4 décimales) |

### Ex M02a.10 — Fonction de répartition, médiane et percentiles d'une loi donnée ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une fonction de répartition, puis des quantiles en résolvant $F(x) = p$.
**Prérequis :** fiche §4 et §7 ; R6 (équations avec exp et ln) · **Parcours :** C, E

La variable $X$ a pour densité $\frac{2}{x^3}$ sur $[1 ; +\infty[$ (et 0 ailleurs). La durée de vie $D$ (en années) d'un composant a pour densité $0{,}25\,e^{-0{,}25t}$ pour $t \ge 0$ (et 0 pour $t < 0$).

| | Question | Réponse attendue |
|---|---|---|
| a | $F(2) = P(X \le 2)$ | une fraction irréductible |
| b | l'expression de $F(x)$ pour $x \ge 1$ | une expression en $x$ |
| c | la médiane de $X$ | une valeur exacte |
| d | le percentile 99 de $X$ | un entier |
| e | $P(X > 5)$ | une fraction irréductible |
| f | la médiane de $D$ | un nombre (4 décimales) |
| g | le premier quartile de $D$ | un nombre (4 décimales) |
| h | le percentile 90 de $D$ | un nombre (4 décimales) |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex M02a.11 — Le théorème fondamental : la dérivée d'une aire ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer que la fonction aire est une primitive, et en déduire le calcul d'une intégrale par une primitive.
**Prérequis :** fiche §1 et §2 ; R7 (taux d'accroissement, dérivée) · **Parcours :** C

Soit $f$ une fonction continue et **croissante** sur un intervalle $[a ; b]$, et $A(x) = \int_a^x f(t)\,dt$ pour $x$ dans $[a ; b]$ (l'aire de $a$ à $x$ quand $f \ge 0$).
1. Soit $x$ dans $[a ; b[$ et $h > 0$ tel que $x + h \le b$. Justifie que $A(x + h) - A(x) = \int_x^{x+h} f(t)\,dt$.
2. Pourquoi a-t-on $h\,f(x) \le \int_x^{x+h} f(t)\,dt \le h\,f(x + h)$ ? Fais un dessin.
3. Déduis-en un encadrement du taux d'accroissement $\frac{A(x + h) - A(x)}{h}$, puis sa limite quand $h \to 0^+$ (utilise la continuité de $f$). Le cas $h < 0$ se traite de la même façon : on l'admet.
4. Conclus : $A$ est une primitive de $f$. Puis montre que $\int_a^b f(t)\,dt = F(b) - F(a)$ pour **toute** primitive $F$ de $f$ (deux primitives sur un intervalle diffèrent d'une constante).
On a supposé $f$ croissante pour simplifier ; le théorème reste vrai pour toute fonction continue (on encadre alors par le minimum et le maximum de $f$ sur $[x ; x + h]$), et pour $x < a$ (avec la convention $\int_a^x = -\int_x^a$). La question 5 s'en sert.

5. Application : soit $G(x) = \int_0^x e^{-t^2}\,dt$, pour tout réel $x$ ($e^{-t^2}$ n'est pas croissante : c'est la version générale du théorème qui s'applique). Calcule $G'(x)$, puis $G'(1)$, alors que tu ne sais pas calculer $G(x)$. Que dit le signe de $G'$ sur le sens de variation de $G$ ?

### Ex M02a.12 — Encadrer une aire par des rectangles : pourquoi les sommes de Riemann convergent (fonction croissante) ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer que les sommes de Riemann d'une fonction croissante tendent vers l'intégrale, avec une borne de l'erreur.
**Prérequis :** fiche §1, §2 et §5 · **Parcours :** C

Soit $f$ continue et croissante sur $[a ; b]$, $h = \frac{b - a}{n}$, $x_i = a + ih$, et $L_n$, $R_n$ les sommes à gauche et à droite.
1. Sur un intervalle $[x_i ; x_{i+1}]$, compare $h\,f(x_i)$, $\int_{x_i}^{x_{i+1}} f$ et $h\,f(x_{i+1})$. En additionnant ces encadrements (Chasles), démontre que $L_n \le \int_a^b f \le R_n$.
2. Démontre que $R_n - L_n = \frac{(b - a)\big(f(b) - f(a)\big)}{n}$. (Écris les deux sommes l'une sous l'autre : presque tous les termes se simplifient.)
3. Déduis-en que $L_n$ et $R_n$ tendent vers $\int_a^b f$ quand $n \to +\infty$, et que l'erreur de chacune est au plus $\frac{(b - a)\big(f(b) - f(a)\big)}{n}$.
4. Combien de rectangles faut-il, d'après cette borne, pour que la somme à gauche de $e^x$ sur $[0 ; 1]$ approche $e - 1$ à $10^{-3}$ près ?
5. Que devient le résultat pour une fonction **décroissante** ? Et pour une fonction ni croissante ni décroissante, comme $\sin$ sur $[0 ; \pi]$, comment adapterais-tu l'argument ?

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M02a.13 — L'aire sous une courbe ROC donnée par une formule 🔗 ★★ ⏱️ 20 min
**Objectif :** calculer l'AUC de courbes ROC données par des formules, et voir ce qu'une AUC résume et ce qu'elle cache.
**Prérequis :** fiche §2, §5 et §8 · **Parcours :** C, E

Deux modèles de détection ont des courbes ROC idéalisées, données en fonction du taux de faux positifs $x$ (de 0 à 1) : $\text{TPR}_A(x) = 1 - (1 - x)^3$ pour le modèle A, et $\text{TPR}_B(x) = x^{1/4}$ pour le modèle B.

| | Question | Réponse attendue |
|---|---|---|
| a | l'AUC du modèle A | une fraction irréductible |
| b | l'AUC du modèle B | une fraction irréductible |
| c | le modèle qui a la plus grande AUC | une lettre entre guillemets : A ou B |
| d | le TPR du modèle A au FPR 0,5 | un nombre (3 décimales) |
| e | le TPR du modèle B au FPR 0,5 | un nombre (4 décimales) |
| f | le modèle de plus grande AUC a le plus grand TPR à tous les FPR | vrai ou faux |
| g | l'approximation de l'AUC du modèle A par la méthode des trapèzes avec les trois points de FPR 0 ; 0,5 et 1 | un nombre (4 décimales) |
| h | l'AUC d'un modèle C de courbe ROC $\text{TPR}_C(x) = x^2$ | une fraction irréductible |

Dans ta copie : dessine les trois courbes et la diagonale. Si l'on n'accepte pas plus de 10 % de faux positifs, quel modèle choisir ? Que dire du modèle C, comparé au hasard ?

### Ex M02a.14 — MML §6.2 (la partie continue) : densité et fonction de répartition, en anglais 📖 ★★ ⏱️ 25 min
**Objectif :** lire en anglais la définition d'une densité et d'une fonction de répartition, et relier les notations du livre à celles de la fiche.
**Prérequis :** fiche §6 et §7 · **Parcours :** C

Lis la partie de MML §6.2 sur les probabilités continues, puis la comparaison d'une loi discrète et d'une loi continue (quelques pages). Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Quelle lettre le livre utilise-t-il pour une densité ? Quels mots anglais emploie-t-il pour « densité » et « fonction de répartition », et quelles abréviations ?
2. Quelles sont les deux conditions qu'une fonction doit remplir pour être une densité ? Compare avec la définition du §6 de la fiche.
3. Écris la relation entre la fonction de répartition et la densité, avec les notations de la fiche.
4. Que dit le livre sur les valeurs que peut prendre une densité, quand il compare une loi discrète et une loi continue ? Refais son raisonnement avec tes propres nombres : une loi uniforme sur un intervalle de longueur 0,4. Quelle est sa densité ?
5. Le livre remarque qu'une fonction de répartition n'a pas toujours de densité. Donne un exemple que tu connais déjà (R8 et §7 de la fiche).
6. Note trois mots ou tournures en anglais de ce passage qui étaient nouveaux pour toi, avec leur traduction.

### Ex M02a.15 — Expliquer pourquoi P(X = a) = 0 pour une variable continue 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement pourquoi une valeur exacte a une probabilité nulle, sans que cela empêche quoi que ce soit d'arriver.
**Prérequis :** fiche §6 · **Parcours :** C, E

Un ami s'étonne : « Si la probabilité que le bus arrive à exactement 8 h 03 min 00 s est nulle, et pareil pour chaque instant, alors le bus n'arrive jamais ? »

Réponds-lui **en huit lignes au plus, avec une seule formule**. Ta réponse doit dire : où se lit une probabilité pour une variable continue, pourquoi l'aire au-dessus d'un seul point est nulle, pourquoi un intervalle, lui, a une probabilité positive, et ce que cela change entre $P(X \le a)$ et $P(X < a)$.

<a id="entretien"></a>

## 💼 Entretien

### M02a.E1 — Chaque valeur a une probabilité nulle : comment dire qu'une valeur est plus probable qu'une autre ? 💼 ★ ⏱️ 10 min
*Fiche §6 · parcours C, E*

« Pour une variable continue, chaque valeur exacte a une probabilité nulle. Alors, quand un modèle dit qu'une mesure de 1,8 est plus vraisemblable qu'une mesure de 2,5, qu'est-ce qu'il compare ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit parler de la densité, de la probabilité d'un petit intervalle autour de chaque valeur, et dire pourquoi une densité supérieure à 1 n'est pas une erreur. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m02a_integrales_densites/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M02a.16 | Rectangles et trapèzes · `riemann_sum`, `trapezoid` | 🔨 | ★ | 20 | C, E |
| M02a.17 | La méthode de Simpson · `simpson` | 🔨 | ★★ | 15 | C |
| M02a.18 | De la densité à la fonction de répartition, puis au quantile par dichotomie · `cdf_from_pdf`, `quantile` | 🔨 | ★★ | 25 | C, E |
| M02a.19 | Vérifier avec `scipy.integrate.quad` et SymPy | 📦 | ★ | 15 | C, E |
| M02a.20 | Prédire : le pas divisé par 2, l'erreur divisée par combien ? | 🔮 | ★ | 10 | C, E |
| M02a.21 | L'intégrale de Gauss par le calcul : la borne qui s'éloigne | 🔬 | ★★ | 20 | C |
| M02a.22 | L'aire qui se remplit : la courbe, les rectangles et la primitive | 🎨 | ★ | 20 | C, E |
| M02a.23 | Chasse à l'erreur : bornes inversées, primitive fausse, aire négative | 🐛 | ★ | 15 | C |
| M02a.24 | Vérifier une primitive avec SymPy : dériver le résultat | 🛠️ | ★ | 10 | C |
| M02a.25 | Défi : la meilleure précision avec dix évaluations de la fonction | 🏆 | ★★★ | 30 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
