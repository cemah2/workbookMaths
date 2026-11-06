# R2 · Calcul littéral et équations — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r2_calcul_litteral/06_mes_reponses.md` (créée par `python tools/start_chapter.py R2`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂ et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Sans calculatrice.** Tout ce fichier se fait à la main. Vérifie chaque résultat **avant** de le reporter dans le notebook : substitue la solution dans l'équation de départ, ou essaie une valeur test sur un développement.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R2.Q1 — Variables et substitution 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Vrai ou faux ?
1. Pour $x = -3$, $x^2$ vaut $-9$.
2. $2x$ et $x^2$ sont égaux pour tout réel $x$.
3. Pour $a = 2$ et $b = 5$, $ab$ vaut 25.
4. Pour $x = -1$, $-x^2 + x$ vaut $-2$.
5. $3x + 2x^2 = 5x^3$.
6. $3(x + 2)$ et $3x + 6$ prennent la même valeur pour tout réel $x$.

### R2.Q2 — Développer ou factoriser ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Pour chaque transformation, dis si c'est un **développement** ou une **factorisation**, puis si elle est **juste** ou **fausse**.
1. $4x^2 - 6x \;\longrightarrow\; 2x(2x - 3)$
2. $(x - 1)(x + 5) \;\longrightarrow\; x^2 + 4x - 5$
3. $3x(x + 2) \;\longrightarrow\; 3x^2 + 2$
4. $x^2 - 25 \;\longrightarrow\; (x - 5)^2$
5. $6x + 9 \;\longrightarrow\; 3(2x + 3)$
6. $-2(x - 3) \;\longrightarrow\; -2x - 6$

### R2.Q3 — Identités remarquables : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. $(x + 3)^2 = x^2 + 9$
2. $(x - 1)^2 = x^2 - 2x + 1$
3. $(2x + 1)^2 = 4x^2 + 4x + 1$
4. $x^2 - 16 = (x - 4)(x + 4)$
5. $(3 - x)^2 = (x - 3)^2$
6. $x^2 + 4 = (x + 2)(x - 2)$
7. $(x + 1)^2 - x^2 = 2x + 1$

### R2.Q4 — Équations : quelles opérations sont permises ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Chaque opération est appliquée aux **deux membres** d'une équation d'inconnue $x$. Garde-t-elle **exactement** les mêmes solutions ? Oui ou non.
1. Ajouter 5.
2. Multiplier par 0.
3. Diviser par $x$.
4. Multiplier par $-2$.
5. Élever au carré.
6. Retirer $3x$.

### R2.Q5 — Inéquations : quand le sens change 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Vrai ou faux ?
1. $2 < 5$, donc $-2 < -5$.
2. $-3x \le 12 \iff x \ge -4$.
3. $\dfrac{x}{-2} > 1 \iff x < -2$.
4. $x + 4 < 1 \iff x < -3$.
5. $5 - x > 0 \iff x > 5$.
6. $[2 \;;\; +\infty]$ est une écriture correcte de l'ensemble des réels supérieurs ou égaux à 2.
7. « $x > 1$ et $x < 4$ » s'écrit $]1 \;;\; +\infty[ \;\cup\; ]-\infty \;;\; 4[$.

### R2.Q6 — Valeur absolue et distance 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

Vrai ou faux ?
1. $|-7| = -7$.
2. $|3 - 10| = 7$.
3. L'équation $|x| = 4$ a deux solutions.
4. $|x - 2|$ est la distance entre $x$ et $-2$.
5. $|x| \ge 0$ pour tout réel $x$.
6. $|a + b| = |a| + |b|$ pour tous réels $a$ et $b$.
7. $\operatorname{sign}(-0{,}5) = -0{,}5$.

### R2.Q7 — Une, aucune ou une infinité de solutions ? 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Combien de solutions chaque système a-t-il ? Réponds par **aucune**, **une seule** ou **une infinité**, sans résoudre en entier.
1. $\begin{cases} x + y = 1 \\ x + y = 2 \end{cases}$
2. $\begin{cases} x + y = 1 \\ x - y = 1 \end{cases}$
3. $\begin{cases} x - 2y = 3 \\ 2x - 4y = 6 \end{cases}$
4. $\begin{cases} y = 3x + 1 \\ y = 3x - 4 \end{cases}$
5. $\begin{cases} 2x = 4 \\ 3y = 9 \end{cases}$
6. Un système de deux équations du premier degré à deux inconnues peut-il avoir **exactement deux** solutions ?

### R2.Q8 — Quelle équation pour ce problème ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

Pour chaque problème, choisis la bonne mise en équation (a, b ou c).

1. « Un nombre augmenté de 7 vaut le triple de ce nombre. » — a) $x + 7 = 3$ ; b) $x + 7 = 3x$ ; c) $7x = x + 3$.
2. « Après une baisse de 25 %, un article coûte 30 €. » Avec $p$ le prix de départ : a) $p - 25 = 30$ ; b) $0{,}75\,p = 30$ ; c) $p = 30 \times 1{,}25$.
3. « Deux nombres ont pour somme 50 et pour différence 12. » — a) $x + y = 50$ et $x - y = 12$ ; b) $x + y = 12$ et $x - y = 50$ ; c) $x + 12 = 50$.
4. « Le périmètre d'un carré de côté $c$ dépasse son côté de 18 cm. » — a) $c^2 = c + 18$ ; b) $4c = c + 18$ ; c) $4c + 18 = c$.
5. « Pierre a 5 ans de plus que Lou ; à eux deux, ils ont 41 ans. » Avec $x$ l'âge de Lou : a) $x + 5 = 41$ ; b) $2x + 5 = 41$ ; c) $x + (x - 5) = 41$.

<a id="rappels"></a>

## 🔁 Rappels

### R2.R1 — Fractions et puissances (R1) 🔁 ★ ⏱️ 5 min
*Fiche R1 §3 et §4 · parcours C, E*

Sans regarder R1 :
1. $\dfrac{3}{4} - \dfrac{5}{6}$, sous forme irréductible ;
2. $\dfrac{2}{3} \div \dfrac{4}{9}$ ;
3. $2^3 \times 2^{-5}$, sous forme de fraction ;
4. $x^3 \times x^4$ et $(2x)^3$ : les règles des puissances valent aussi avec une lettre ;
5. $10^{-2} \times 10^{5}$.

### R2.R2 — Pourcentages et coefficients multiplicateurs (R1) 🔁 ★ ⏱️ 5 min
*Fiche R1 §7 · parcours C*

1. Le coefficient multiplicateur d'une baisse de 15 %.
2. Un prix de 80 € augmente de 5 % : le nouveau prix.
3. Une hausse de 20 % suivie d'une baisse de 20 % : le taux d'évolution global.
4. Un article passe de 50 € à 40 € : son taux d'évolution.
5. Après une hausse de 25 %, un article coûte 100 € : son prix de départ.

### R2.R3 — Saisir un intervalle et une expression (R0) 🔁 ★ ⏱️ 5 min
*Fiche R0 §3 · parcours C*

Sans regarder R0, écris ce que tu taperais dans le notebook pour que `wbm.check` lise :
1. l'intervalle $]-\infty \;;\; 5]$ ;
2. les réels $x$ tels que $-1 < x \le 0$ ;
3. l'expression $3x^2 - x$ ;
4. les réels strictement négatifs **ou** strictement supérieurs à 2 ;

Et une question à part :

5. Pourquoi `wbm.check` refuse-t-il l'écriture $[1 \;;\; +\infty]$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main**, en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre : `-1.5` (point décimal) ; une fraction exacte entre guillemets : `"5/7"` ;
- une **liste de coefficients**, du plus haut degré au terme constant, sans oublier les zéros : pour $2x^2 - 5$, on écrirait `[2, 0, -5]` ;
- une **liste de solutions**, dans l'ordre que tu veux ; une fraction s'y écrit comme un calcul, sans guillemets : `[-2/7, 6]` ;
- un **intervalle** entre guillemets : `"]-1 ; 4]"`, `"[0 ; +oo["`, une réunion `"]-oo ; 0] U ]1 ; +oo["` ; l'ensemble vide s'écrit avec le mot vide entre guillemets ;
- le **nombre de solutions** d'un système par son numéro : 1 pour aucune, 2 pour une seule, 3 pour une infinité.

### Ex R2.1 — Substituer et réduire ✏️ ★ ⏱️ 10 min
**Objectif :** calculer la valeur d'une expression pour des valeurs données, et réduire une expression.
**Prérequis :** fiche §1 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la valeur de $2x^2 - 3x + 1$ pour $x = -3$ | un nombre |
| b | la valeur de $(a - b)^2 - ab$ pour $a = 2$ et $b = -1$ | un nombre |
| c | $5x - 3 + 2x^2 - 7x + 4 - x^2$ réduite, sous la forme $\alpha x^2 + \beta x + \gamma$ | la liste $[\alpha, \beta, \gamma]$ |
| d | $4xy - 2x + 3xy + 5x$ réduite, sous la forme $\alpha\, xy + \beta x$ | la liste $[\alpha, \beta]$ |
| e | la valeur de $\dfrac{x + 1}{x - 1}$ pour $x = \frac{1}{2}$ | un nombre |

### Ex R2.2 — Développer ✏️ ★ ⏱️ 15 min
**Objectif :** développer et réduire, avec la double distributivité et les signes.
**Prérequis :** fiche §2 · **Parcours :** C, E

Développe et réduis ; donne la liste des coefficients.

| | Expression | Réponse attendue |
|---|---|---|
| a | $3(2x - 5) - 4(x - 1)$ | la liste $[\alpha, \beta]$ de $\alpha x + \beta$ |
| b | $(x - 2)(3x + 5)$ | la liste de $\alpha x^2 + \beta x + \gamma$ |
| c | $(2x + 1)(x^2 - x + 3)$ | la liste de $\alpha x^3 + \beta x^2 + \gamma x + \delta$ |
| d | $-(x - 4)(x + 1)$ | la liste de $\alpha x^2 + \beta x + \gamma$ |
| e | $(a + 2b)(a - b)$, sous la forme $\alpha a^2 + \beta ab + \gamma b^2$ | la liste $[\alpha, \beta, \gamma]$ |

### Ex R2.3 — Factoriser par un facteur commun ✏️ ★★ ⏱️ 15 min
**Objectif :** repérer le plus grand facteur commun, nombre, lettre ou parenthèse, et factoriser.
**Prérequis :** fiche §2 · **Parcours :** C, E

| | Factoriser | Sous la forme | Réponse attendue |
|---|---|---|---|
| a | $6x^2 + 15x$ | $kx(\alpha x + \beta)$, avec $k$ le plus grand entier positif possible | la liste $[k, \alpha, \beta]$ |
| b | $4x^3 - 8x^2 + 12x$ | $4x(x^2 + \alpha x + \beta)$ | la liste $[\alpha, \beta]$ |
| c | $(x - 1)(2x + 3) + (x - 1)(x - 5)$ | $(x - 1)(\alpha x + \beta)$ | la liste $[\alpha, \beta]$ |
| d | $(2x + 1)^2 - (2x + 1)(x - 4)$ | $(2x + 1)(\alpha x + \beta)$ | la liste $[\alpha, \beta]$ |
| e | $5x(x + 2) - 3(x + 2)$ | $(x + 2)(\alpha x + \beta)$ | la liste $[\alpha, \beta]$ |
| f | $x(x - 7) + x - 7$ | $(x - 7)(\alpha x + \beta)$ | la liste $[\alpha, \beta]$ |

### Ex R2.4 — Identités remarquables dans les deux sens ✏️ ★★ ⏱️ 20 min
**Objectif :** développer avec une identité, reconnaître une forme développée pour la factoriser, et calculer de tête.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $(x + 5)^2$ développé | la liste de $\alpha x^2 + \beta x + \gamma$ |
| b | $(3x - 4)^2$ développé | la liste de $\alpha x^2 + \beta x + \gamma$ |
| c | $(2x + 7)(2x - 7)$ développé | la liste de $\alpha x^2 + \beta x + \gamma$ |
| d | le nombre $a$ tel que $x^2 - 14x + 49 = (x - a)^2$ | un nombre |
| e | $25x^2 - 9 = (\alpha x - \beta)(\alpha x + \beta)$, avec $\alpha > 0$ et $\beta > 0$ | la liste $[\alpha, \beta]$ |
| f | $4x^2 + 20x + 25 = (\alpha x + \beta)^2$, avec $\alpha > 0$ et $\beta > 0$ | la liste $[\alpha, \beta]$ |
| g | $101^2$, de tête, avec une identité | un entier |
| h | $59 \times 61$, de tête, avec une identité | un entier |

### Ex R2.5 — Équations du premier degré ✏️ ★ ⏱️ 15 min
**Objectif :** résoudre une équation du premier degré par équations équivalentes, et reconnaître les cas sans solution ou avec une infinité de solutions.
**Prérequis :** fiche §4 · **Parcours :** C, E

| | Équation | Réponse attendue |
|---|---|---|
| a | $4x + 9 = 1$ | la solution |
| b | $5 - 2x = 3x + 20$ | la solution |
| c | $3(x - 2) = 2(x + 4) - 1$ | la solution |
| d | $\dfrac{2x}{3} - 1 = \dfrac{x + 4}{2}$ | la solution |
| e | $3(x - 1) + 5 = 3x + 4$ | le nombre de solutions : 1, 2 ou 3 |
| f | $4(x - 1) + 6 = 2(2x + 1)$ | le nombre de solutions : 1, 2 ou 3 |

Pour e et f, la légende est celle de l'introduction : 1 pour aucune, 2 pour une seule, 3 pour une infinité.

### Ex R2.6 — Équations produit nul et équations avec des fractions ✏️ ★★ ⏱️ 20 min
**Objectif :** résoudre en factorisant, sans jamais diviser par l'inconnue, et traiter une inconnue au dénominateur.
**Prérequis :** fiche §4 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | les solutions de $(x - 4)(2x + 3) = 0$ | une liste de solutions |
| b | les solutions de $4x^2 = 9x$ | une liste de solutions |
| c | les solutions de $(3x - 1)^2 = 0$ | une liste de solutions |
| d | les solutions de $9x^2 - 16 = 0$ | une liste de solutions |
| e | la valeur interdite de l'équation $\dfrac{x + 2}{x - 1} = 3$ | un nombre |
| f | les solutions de $\dfrac{x + 2}{x - 1} = 3$ | une liste de solutions |
| g | les solutions de $\dfrac{x}{4} - \dfrac{x - 2}{6} = 1$ | une liste de solutions |

### Ex R2.7 — Inéquations et intervalles ✏️ ★ ⏱️ 15 min
**Objectif :** résoudre une inéquation du premier degré, en retournant le sens quand il le faut, et écrire ses solutions en intervalle.
**Prérequis :** fiche §5 · **Parcours :** C, E

Donne l'ensemble des solutions, en intervalle.

| | Inéquation |
|---|---|
| a | $2x - 7 < 5$ |
| b | $3 - 5x \ge 18$ |
| c | $2(x + 1) \le 5x - 7$ |
| d | $-4 < 2x + 2 \le 8$ |
| e | $\dfrac{x}{2} + 1 > \dfrac{x - 3}{3}$ |

### Ex R2.8 — Réunion et intersection d'intervalles ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer une intersection et une réunion, et traduire « et » et « ou ».
**Prérequis :** fiche §5 · **Parcours :** C

Donne chaque ensemble sous la forme la plus simple : un seul intervalle quand c'est possible, sinon une réunion, ou l'ensemble vide.

| | Ensemble |
|---|---|
| a | $[-2 \;;\; 5] \cap [1 \;;\; 8]$ |
| b | $]-\infty \;;\; 3[ \;\cap\; [0 \;;\; +\infty[$ |
| c | $[-4 \;;\; 1] \cup [0 \;;\; 6[$ |
| d | $]-\infty \;;\; -1] \;\cap\; [2 \;;\; +\infty[$ |
| e | les réels $x$ tels que $x < -2$ **ou** $x \ge 3$ |
| f | les réels $x$ tels que $2x - 1 > 3$ **et** $3x < 15$ |

### Ex R2.9 — Équations et inéquations avec une valeur absolue, et la fonction signe ✏️ ★★ ⏱️ 20 min
**Objectif :** résoudre avec une valeur absolue en la lisant comme une distance, et calculer un signe.
**Prérequis :** fiche §6 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | les solutions de $\lvert x - 3 \rvert = 4$ | une liste de solutions |
| b | les solutions de $\lvert 2x + 1 \rvert = 9$ | une liste de solutions |
| c | le nombre de solutions de $\lvert x - 6 \rvert = -2$ | un entier |
| d | les solutions de $\lvert x + 1 \rvert \le 3$ | un intervalle |
| e | les solutions de $\lvert x - 2 \rvert > 5$ | un intervalle ou une réunion |
| f | la distance entre $-4{,}5$ et $2$ | un nombre |
| g | $\operatorname{sign}(x^2 - 9)$ pour $x = -2$ | un nombre |

### Ex R2.10 — Système 2 × 2 par substitution et par combinaison ✏️ ★★ ⏱️ 20 min
**Objectif :** résoudre un système par substitution ou par combinaison, en choisissant la méthode la plus courte.
**Prérequis :** fiche §7 · **Parcours :** C, E

Résous chaque système (au moins un par substitution, au moins un par combinaison), vérifie le couple trouvé dans **les deux** équations, puis donne la liste $[x, y]$.

| | Système |
|---|---|
| a | $\begin{cases} x + 2y = 8 \\ 3x - y = 3 \end{cases}$ |
| b | $\begin{cases} 5x + 2y = 1 \\ 3x + 4y = -5 \end{cases}$ |
| c | $\begin{cases} 4x - 3y = 17 \\ 2x + y = 1 \end{cases}$ |
| d | $\begin{cases} \dfrac{x}{2} + \dfrac{y}{3} = 4 \\ x - y = 3 \end{cases}$ |

### Ex R2.11 — Système 2 × 2 par la formule de Cramer ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer un déterminant 2 × 2, appliquer la formule de Cramer, et conclure quand le déterminant est nul.
**Prérequis :** fiche §7 · **Parcours :** C, E

On note $(S)$ le système $\begin{cases} 2x + 5y = 1 \\ 3x - y = 10 \end{cases}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le déterminant $D$ de $(S)$ | un nombre |
| b | la solution de $(S)$, par la formule de Cramer | la liste $[x, y]$ |
| c | le nombre de solutions de $\begin{cases} 2x - 3y = 4 \\ -4x + 6y = -8 \end{cases}$ | 1, 2 ou 3 |
| d | le nombre de solutions de $\begin{cases} 2x - 3y = 4 \\ -4x + 6y = 1 \end{cases}$ | 1, 2 ou 3 |

### Ex R2.12 — Mettre en équation : trois problèmes ✏️ ★★ ⏱️ 25 min
**Objectif :** choisir l'inconnue, traduire l'énoncé, résoudre, vérifier dans l'énoncé.
**Prérequis :** fiche §8 · **Parcours :** C, E

Pour chaque problème, écris dans ta copie l'inconnue choisie, l'équation (ou le système), la résolution, la vérification et une phrase de réponse.

| | Problème | Réponse attendue |
|---|---|---|
| a | Un rectangle a un périmètre de 46 cm, et sa longueur dépasse sa largeur de 7 cm. Quelle est son aire ? | un nombre (en cm²) |
| b | Après une baisse de 20 %, un casque coûte 56 €. Quel était son prix avant la baisse ? | un nombre (en €) |
| c | Une salle compte 22 tables, de 4 places ou de 6 places, soit 108 places en tout. Combien y a-t-il de tables de 6 places ? | un entier |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut. La solution donne une **grille de relecture** pour juger la tienne.

### Ex R2.13 — Démontrer les identités remarquables ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer les trois identités à partir de la distributivité, puis s'en servir pour démontrer une propriété des entiers.
**Prérequis :** fiche §2 et §3 · **Parcours :** C, E

Soient $a$ et $b$ deux réels.
1. Développe $(a + b)(a + b)$ avec la double distributivité. Quelle propriété de la multiplication te permet de regrouper $ab$ et $ba$ ? Conclus que $(a + b)^2 = a^2 + 2ab + b^2$.
2. Déduis-en $(a - b)^2 = a^2 - 2ab + b^2$ **sans refaire le développement** : applique la question 1 à $a$ et à $-b$.
3. Démontre que $(a + b)(a - b) = a^2 - b^2$.
4. Montre que, pour tout entier $n$, $(n + 1)^2 - n^2$ est un entier impair. Puis explique avec la question 3 pourquoi $99 \times 101$ se calcule de tête.
5. ★ La figure de la fiche (§3) découpe un carré de côté $a + b$. Pour $a > b > 0$, décris une figure qui illustre $(a - b)^2 = a^2 - 2ab + b^2$ : pars d'un carré de côté $a$, retire deux bandes $a \times b$… que faut-il rajouter, et pourquoi ?

### Ex R2.14 — Pourquoi multiplier par un nombre négatif retourne l'inégalité ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer les règles de calcul sur les inégalités à partir d'une définition, et voir ce qui ne marche pas.
**Prérequis :** fiche §5 · **Parcours :** C

On prend comme **définition** : $a < b$ veut dire $b - a > 0$. On admet seulement les règles des signes : le produit de deux nombres strictement positifs est strictement positif, le produit d'un nombre strictement positif et d'un nombre strictement négatif est strictement négatif.

Soient $a$ et $b$ deux réels tels que $a < b$.
1. Montre que $a + c < b + c$ pour tout réel $c$.
2. Montre que $ka < kb$ pour tout réel $k > 0$.
3. Montre que $ka > kb$ pour tout réel $k < 0$.
4. On suppose de plus $0 < a$. Montre que $\dfrac{1}{a} > \dfrac{1}{b}$ : multiplie l'inégalité $a < b$ par un nombre positif bien choisi.
5. L'affirmation « si $a < b$, alors $a^2 < b^2$ » est fausse en général : donne un contre-exemple. Montre qu'elle devient vraie quand $0 \le a$ (factorise $b^2 - a^2$).

### Ex R2.15 — Quand un système 2 × 2 a-t-il une seule solution ? ∂ ★★★ ⏱️ 40 min
**Objectif :** démontrer qu'un système 2 × 2 a une seule solution exactement quand son déterminant n'est pas nul, et décrire les deux autres cas.
**Prérequis :** fiche §7 · **Parcours :** C

On étudie le système $(S)$ : $\begin{cases} ax + by = e \\ cx + dy = f \end{cases}$, de déterminant $D = ad - bc$.
1. Soit $(x, y)$ une solution de $(S)$. En multipliant la première équation par $d$, la seconde par $b$, puis en soustrayant, montre que $D\,x = ed - bf$. Montre de même que $D\,y = af - ec$.
2. On suppose $D \ne 0$. Déduis de 1 que $(S)$ a **au plus** une solution, puis vérifie, en le substituant dans la **première** équation, que le couple de Cramer est bien solution (la seconde se vérifie de la même façon ; tu peux l'admettre). Conclus.
3. On suppose $D = 0$, avec $a \ne 0$. Pose $k = \dfrac{c}{a}$. Montre que $c = ka$ et $d = kb$ (utilise $ad = bc$) : la seconde équation s'écrit $k(ax + by) = f$.
4. Toujours avec $D = 0$ et $a \ne 0$ : montre que si $f = ke$, tout couple qui vérifie la première équation vérifie aussi la seconde (une infinité de solutions), et que si $f \ne ke$, aucun couple ne vérifie les deux (aucune solution).
5. Conclus : « $(S)$ a une seule solution si et seulement si $D \ne 0$ ». Applique le critère au système $\begin{cases} 6x - 4y = 2 \\ -9x + 6y = m \end{cases}$ : pour quelle valeur de $m$ a-t-il une infinité de solutions ?

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R2.16 — Deux mesures, deux inconnues : retrouver a et b dans y = ax + b par un système 🔗 ★★ ⏱️ 20 min
**Objectif :** retrouver les deux paramètres d'un modèle affine à partir de deux mesures, et voir ce qui change avec une troisième.
**Prérequis :** fiche §7 et §8 · **Parcours :** C, E

Un capteur de température renvoie une tension $u$, en volts. Son fabricant indique que la température vaut $T = a\,u + b$ (en °C), mais ne donne ni $a$ ni $b$. Pour **étalonner** le capteur, on fait deux mesures : quand $u = 0{,}8$ V, un thermomètre de référence indique $T = 12$ °C ; quand $u = 2$ V, il indique $T = 42$ °C.

| | Question | Réponse attendue |
|---|---|---|
| a | les paramètres du modèle, trouvés par un système de deux équations d'inconnues $a$ et $b$ | la liste $[a, b]$ |
| b | la température prédite par le modèle quand le capteur renvoie $1{,}4$ V | un nombre (en °C) |
| c | une troisième mesure donne $u = 2{,}4$ V et $T = 51{,}5$ °C : l'écart « température mesurée − température prédite » | un nombre (en °C) |
| d | avec les trois mesures, le nombre de couples $(a, b)$ qui vérifient les **trois** équations | 1, 2 ou 3 |

Dans ta copie, explique en deux phrases ce que les questions c et d disent d'un modèle qu'on ajuste à beaucoup de données.

### Ex R2.17 — Expliquer ce que veut dire « résoudre une équation » 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, avec des mots simples, ce qu'est l'ensemble des solutions et pourquoi on vérifie.
**Prérequis :** fiche §4 · **Parcours :** C, E

Un élève de seconde t'envoie deux résolutions :
- « $x^2 = 6x$, je divise par $x$, donc $x = 6$. » ;
- « $5x - 3 = 2x + 9$, j'essaie $x = 4$ : $17 = 17$, ça marche, donc c'est résolu. »

Réponds-lui **en huit lignes au plus**, sans jargon. Ta réponse doit dire : ce que veut dire « résoudre » (trouver quoi, exactement ?), ce qui manque dans chacune de ses deux résolutions, et à quoi sert une vérification (et ce qu'elle ne prouve pas).

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r2_calcul_litteral/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R2.22 | Vérifier développements et factorisations avec SymPy | 📦 | ★ | 15 | C, E |
| R2.27 | Chasse à l'erreur : six erreurs de calcul littéral | 🐛 | ★★ | 20 | C, E |
| R2.18 | Résoudre ax + b = 0 dans tous les cas · `solve_linear` | 🔨 | ★ | 25 | C, E |
| R2.19 | Résoudre ax + b ≤ 0 et rendre l'intervalle des solutions · `solve_linear_inequality` | 🔨 | ★★ | 40 | C |
| R2.20 | Résoudre \|x − a\| = c · `solve_abs_equation` | 🔨 | ★★ | 30 | C |
| R2.23 | Résoudre avec `sympy.solve` et lire son résultat | 📦 | ★ | 15 | C |
| R2.28 | Écrire un test pytest pour une fonction qui résout une équation | 🛠️ | ★ | 15 | C |
| R2.21 | Système 2 × 2 par la formule de Cramer · `solve_2x2` | 🔨 | ★★ | 40 | C, E |
| R2.26 | Un système, deux droites : voir la solution | 🎨 | ★★ | 20 | C, E |
| R2.24 | Prédire le nombre de solutions de trois systèmes, puis tracer leurs droites | 🔮 | ★ | 15 | C, E |
| R2.25 | Expérience : un système presque dégénéré, un coefficient bouge de 0,001 et la solution s'envole | 🔬 | ★★ | 20 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
