# Test de positionnement — sujet

> Ce test mesure ce qui te reste du lycée, chapitre par chapitre de la remise à niveau (R1 à R9), pour savoir quoi sauter, survoler ou faire en entier. **Ce n'est pas un examen** : une réponse devinée fausse ton diagnostic et te fera sauter un chapitre dont tu avais besoin.

**Règles.**
- Environ **2 heures**, d'une traite si possible. Pas de fiche, pas de cours, pas de calculatrice, pas d'assistant IA : un papier et un crayon.
- Écris tes réponses **et ta démarche** dans ta copie, `mon_travail/positionnement/04_mes_reponses.md` (créée par `python tools/start_chapter.py POS`), ou sur papier.
- Tu ne sais pas faire ? **Laisse vide** et passe à la suite. C'est une information utile, pas un échec.
- À la fin seulement, reporte tes réponses dans ta copie du notebook (`mon_travail/positionnement/02_notebook.ipynb`) : il les vérifie et calcule ta grille. Le mode d'emploi complet est dans `README.md`.

**Comment écrire une réponse** (comme en R0, fiche §3) : un décimal avec un **point** (`0.75`, ou `"0,75"` entre guillemets), une fraction exacte entre guillemets (`"5/8"`), une expression entre guillemets (`"3*x**2 - 1"`), un intervalle entre guillemets (`"]-7 ; 0]"`, l'infini s'écrit `oo` : `"[3 ; +oo["`), plusieurs nombres dans une liste (`[4, -1]`), vrai ou faux par `True` ou `False`.

Deux exercices par chapitre ; chaque exercice a plusieurs questions (a, b, c…).

---

## R1 · Nombres et calcul

### POS.1 — Calculer avec des priorités et des fractions ✏️ ⏱️ 6 min

Donne les fractions sous forme **irréductible**.

| | Calcul |
|---|---|
| a | $7 - 3 \times (2 - 5)$ |
| b | $\dfrac{2}{3} + \dfrac{5}{4}$ |
| c | $\dfrac{3}{5} \div \dfrac{9}{10}$ |
| d | $\dfrac{1 - \frac{1}{4}}{2}$ |

### POS.2 — Puissances, racines et notation scientifique ✏️ ⏱️ 6 min

| | Calcul |
|---|---|
| a | $\dfrac{3^6 \times 3^{-2}}{3^3}$ |
| b | l'entier $a$ tel que $\sqrt{72} = a\sqrt{2}$ |
| c | $\dfrac{6 \times 10^{5}}{3 \times 10^{-2}}$, en écriture décimale (sans puissance de 10) |
| d | $2{,}5 \times 10^{-3}$, écrit comme un nombre décimal |

## R2 · Calcul littéral et équations

### POS.3 — Développer, factoriser, résoudre une équation et une inéquation ✏️ ⏱️ 7 min

| | Question | Réponse attendue |
|---|---|---|
| a | développe et réduis $(2x - 3)(x + 4)$ | une expression |
| b | $x^2 - 10x + 25 = (x - a)^2$ : donne $a$ | un nombre |
| c | résous $5x - 7 = 2x + 8$ | un nombre |
| d | résous $-3x + 6 \geq 0$ | un intervalle |

### POS.4 — Un système de deux équations à deux inconnues ✏️ ⏱️ 8 min

a) Résous le système $\begin{cases} 2x + 3y = 12 \\ x - y = 1 \end{cases}$ et donne la liste `[x, y]`.

b) Combien de solutions le système $\begin{cases} x + 3y = 2 \\ 2x + 6y = 5 \end{cases}$ a-t-il ? Réponds par le numéro : 1. aucune ; 2. une seule ; 3. une infinité.

## R3 · Fonctions

### POS.5 — Lire un graphique de fonction 📈 ⏱️ 5 min

Voici la courbe d'une fonction $g$ définie sur $[-3 ; 4]$.

![La courbe de g sur [−3 ; 4] : une ligne brisée de trois segments, sur un quadrillage d'unité 1](figures/pos_5_graphique.png)

| | Question | Réponse attendue |
|---|---|---|
| a | $g(0)$ | un nombre |
| b | le nombre de solutions de l'équation $g(x) = 1$ | un nombre |
| c | le plus grand intervalle sur lequel $g$ est décroissante | un intervalle |
| d | le maximum de $g$ sur $[-3 ; 4]$ | un nombre |

### POS.6 — Racines et sommet d'un polynôme du second degré ✏️ ⏱️ 8 min

On pose $p(x) = 2x^2 + 2x - 12$.

| | Question | Réponse attendue |
|---|---|---|
| a | le discriminant de $p$ | un nombre |
| b | les racines de $p$ | une liste, dans l'ordre que tu veux |
| c | l'abscisse du sommet de la parabole | une fraction ou un décimal |
| d | la valeur minimale de $p$ | une fraction ou un décimal |

## R4 · Logique, ensembles, Σ et Π

### POS.7 — Sommes avec Σ, somme double et produit avec Π ✏️ ⏱️ 7 min

| | Calcul |
|---|---|
| a | $\displaystyle\sum_{k=1}^{5} (2k + 1)$ |
| b | $\displaystyle\sum_{i=0}^{3} 10^i$ |
| c | $\displaystyle\sum_{i=1}^{2} \sum_{j=1}^{3} i\,j$ |
| d | $\displaystyle\prod_{k=1}^{3} (2k)$ |

### POS.8 — La négation d'une phrase avec « pour tout » ✏️ ⏱️ 5 min

a) Quelle phrase est la **négation** de « Pour tout entier $n$, $n^2 + n$ est pair » ? Réponds par son numéro.
1. Pour tout entier $n$, $n^2 + n$ est impair.
2. Il existe un entier $n$ tel que $n^2 + n$ est impair.
3. Il existe un entier $n$ tel que $n^2 + n$ est pair.
4. Aucun entier $n$ ne rend $n^2 + n$ pair.

b) Vrai ou faux : « pour tout réel $x$, si $x^2 = 4$, alors $x = 2$ » ?

## R5 · Suites

### POS.9 — Terme et somme d'une suite géométrique ✏️ ⏱️ 6 min

La suite $(u_n)$ est géométrique, de premier terme $u_0 = 3$ et de raison $q = 2$.

a) Calcule $u_5$.

b) Calcule $u_0 + u_1 + \dots + u_5$.

c) Sans rapport avec $(u_n)$ : la somme infinie $1 + \dfrac{1}{3} + \dfrac{1}{9} + \dfrac{1}{27} + \dots$ (une fraction).

### POS.10 — Une suite définie par récurrence : premiers termes et limite ✏️ ⏱️ 6 min

La suite $(v_n)$ est définie par $v_0 = 2$ et $v_{n+1} = \dfrac{1}{2} v_n + 3$.

a) Calcule $v_1$, $v_2$ et $v_3$, et donne la liste `[v1, v2, v3]`.

b) La suite converge. Vers quel nombre ?

## R6 · Exponentielle et logarithmes

### POS.11 — Propriétés de l'exponentielle et du logarithme ✏️ ⏱️ 5 min

| | Calcul |
|---|---|
| a | $\dfrac{e^{3} \times e^{-1}}{e^{2}}$ |
| b | l'entier $k$ tel que $\ln 21 - \ln 3 = \ln k$ |
| c | $\ln\left(\sqrt{e}\right)$ (une fraction ou un décimal) |
| d | $\log_2 64$ |

### POS.12 — Résoudre des équations avec exp et ln ✏️ ⏱️ 6 min

| | Équation | Réponse attendue |
|---|---|---|
| a | $e^{x} = 7$ | la valeur **exacte**, écrite avec `ln` (une expression entre guillemets) |
| b | $\ln x = -1$ | la valeur **exacte**, écrite avec `exp` (une expression entre guillemets) |
| c | $e^{3x - 6} = 1$ | un nombre |

## R7 · Limites et dérivation

### POS.13 — Dériver trois fonctions, dont une composée ✏️ ⏱️ 7 min

Donne chaque dérivée sous forme d'expression en $x$ (entre guillemets ; `exp(x)` pour $e^x$).

| | Fonction |
|---|---|
| a | $f(x) = 2x^5 - 3x^2 + 1$ |
| b | $g(x) = (x - 1)\,e^{x}$ |
| c | $h(x) = (5 - 2x)^3$ |

### POS.14 — Tangente, variations et une limite ✏️ ⏱️ 10 min

On pose $f(x) = x^3 - 3x$, définie sur $\mathbb{R}$.

| | Question | Réponse attendue |
|---|---|---|
| a | l'équation de la tangente à la courbe au point d'abscisse 2, sous la forme $y = mx + p$ | la liste `[m, p]` |
| b | le plus grand intervalle sur lequel $f$ est décroissante | un intervalle |
| c | la valeur du maximum local de $f$ | un nombre |
| d | la limite de $\dfrac{3x^2 - x}{x^2 + 5}$ quand $x$ tend vers $+\infty$ | un nombre |

## R8 · Probabilités de base

### POS.15 — Une probabilité avec un arbre ✏️ ⏱️ 6 min

Une urne contient 3 boules rouges et 2 boules bleues. On tire deux boules au hasard, l'une après l'autre, **sans remise**. Donne les probabilités sous forme de fractions irréductibles.

a) La probabilité de tirer deux boules rouges.

b) La probabilité de tirer une boule de chaque couleur.

### POS.16 — L'espérance et la variance d'une variable aléatoire ✏️ ⏱️ 6 min

Une variable aléatoire $X$ prend les valeurs $-2$, $0$ et $1$ avec les probabilités $0{,}1$, $0{,}4$ et $0{,}5$.

a) Son espérance $\mathbb{E}[X]$, notée $E(X)$ au lycée (un décimal).

b) Sa variance $\mathbb{V}(X)$, notée $V(X)$ au lycée (un décimal).

## R9 · Géométrie du plan, vecteurs et trigonométrie

### POS.17 — Distance et produit scalaire dans le plan ✏️ ⏱️ 6 min

| | Question | Réponse attendue |
|---|---|---|
| a | la distance entre les points $A(2 ; -1)$ et $B(7 ; 11)$ | un nombre |
| b | le produit scalaire des vecteurs $\vec{u}(3 ; -2)$ et $\vec{v}(4 ; 1)$ | un nombre |
| c | les vecteurs $\vec{u}(3 ; -2)$ et $\vec{w}(2 ; 3)$ sont-ils orthogonaux ? | `True` ou `False` |

### POS.18 — Cosinus d'un angle et radians ✏️ ⏱️ 5 min

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre $k$ tel que $150° = k\pi$ radians | une fraction |
| b | $\sin\left(\dfrac{\pi}{6}\right)$ | une fraction |
| c | l'angle entre les vecteurs $\vec{u}(2 ; 0)$ et $\vec{v}(1 ; \sqrt{3})$, en degrés | un nombre |

---

Fini ? Reporte tes réponses dans le notebook (`README.md`, étape 3), puis lis ta grille.
