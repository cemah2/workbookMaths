# M02b · Variables aléatoires et lois usuelles — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m02b_variables_aleatoires/06_mes_reponses.md` (créée par `python tools/start_chapter.py M02b`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Avant chaque calcul, écris **la loi et ses paramètres** ($X \sim \mathcal{B}(5 ; 0{,}8)$, $T \sim \mathcal{E}(0{,}4)$…), garde les valeurs exactes ($e^{-1{,}5}$, $\frac{1}{3}$) jusqu'au bout, et utilise la table de $\Phi$ de la fiche (§3) pour la loi normale.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M02b.Q1 — Discrète ou continue ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Pour chaque variable aléatoire, dis si elle est **discrète** ou **à densité** (continue).
1. Le nombre de clients qui entrent dans une boutique entre 9 h et 10 h.
2. La durée d'un appel téléphonique.
3. La classe qu'un classifieur d'images attribue à une photo.
4. La température à midi, demain, à Lyon.
5. Le nombre de lancers d'une pièce nécessaires pour obtenir le premier pile.
6. Vrai ou faux : une variable discrète ne prend qu'un nombre fini de valeurs.

### M02b.Q2 — Quelle loi pour quelle situation ? 🧠 ★ ⏱️ 4 min
*Fiche §2 et §3 · parcours C, E*

Quelle loi usuelle (avec ses paramètres, quand l'énoncé les donne) modélise le mieux chaque variable ?
1. Le nombre de 6 obtenus en 10 lancers d'un dé équilibré.
2. Le nombre d'e-mails reçus en une heure, quand on en reçoit 12 par heure en moyenne, un par un et indépendamment.
3. Le numéro de la première tentative de connexion qui réussit, chaque tentative réussissant avec la probabilité 0,3.
4. La durée jusqu'à la prochaine panne d'un composant électronique qui ne s'use pas, quand il tombe en panne une fois tous les 5 ans en moyenne.
5. La classe tirée au hasard selon les probabilités $(0{,}7 ;\ 0{,}2 ;\ 0{,}1)$ que donne un réseau pour trois classes.
6. L'erreur d'une mesure, somme de nombreuses petites perturbations indépendantes.

### M02b.Q3 — Espérance et variance : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Vrai ou faux ?
1. L'espérance d'une variable aléatoire est toujours une valeur qu'elle peut prendre.
2. $\mathbb{V}(X) \ge 0$, et $\mathbb{V}(X) = 0$ seulement si $X$ est constante.
3. $\mathbb{E}[X^2] = \mathbb{E}[X]^2$.
4. $\mathbb{V}(3X + 5) = 9\,\mathbb{V}(X)$.
5. Toute variable à densité a une espérance.
6. Pour une loi exponentielle, l'espérance et l'écart-type sont égaux.

### M02b.Q4 — La loi normale : ce que disent μ et σ 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. $X \sim \mathcal{N}(10, 4)$ : que vaut l'écart-type de $X$ ?
2. Vrai ou faux : la densité de $\mathcal{N}(0, 0{,}2^2)$ dépasse 1 en 0.
3. Pour $Z \sim \mathcal{N}(0, 1)$, que vaut $P(Z \le 0)$ ?
4. Écris $\Phi(-1{,}5)$ à l'aide de $\Phi(1{,}5)$.
5. On double $\sigma$ sans changer $\mu$ : que devient la hauteur du sommet de la cloche ?
6. $X \sim \mathcal{N}(\mu, \sigma^2)$ : que vaut $P(X \le \mu + \sigma)$, avec la table de la fiche ?

### M02b.Q5 — Jointe, marginale, indépendance 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Deux variables $X$ et $Y$, à valeurs dans $\{0, 1\}$, ont la loi jointe : $P(X = 0, Y = 0) = 0{,}1$ ; $P(X = 0, Y = 1) = 0{,}3$ ; $P(X = 1, Y = 0) = 0{,}2$ ; $P(X = 1, Y = 1) = 0{,}4$.
1. $P(X = 1)$ ?
2. $P(Y = 1)$ ?
3. $X$ et $Y$ sont-elles indépendantes ? Justifie par un calcul.
4. Vrai ou faux : si $X$ et $Y$ sont indépendantes, $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$.
5. Vrai ou faux : les deux lois marginales suffisent à retrouver la loi jointe.
6. Comment obtient-on la densité marginale de $X$ à partir d'une densité jointe $f(x, y)$ ?

### M02b.Q6 — La variance d'une somme 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

$X$ et $Y$ sont indépendantes, avec $\sigma(X) = 6$ et $\sigma(Y) = 8$.
1. $\mathbb{V}(X + Y)$ ?
2. $\sigma(X + Y)$ ?
3. $\mathbb{V}(X - Y)$ ?
4. $\mathbb{V}(2X)$ ?
5. $X_1, \ldots, X_9$ sont i.i.d., de même loi que $X$ : l'écart-type de leur moyenne ?
6. Vrai ou faux : $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ demande que $X$ et $Y$ soient indépendantes.

### M02b.Q7 — Simuler une loi 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

$U$ suit la loi uniforme sur $[0 ; 1]$, et $Z$ la loi $\mathcal{N}(0, 1)$.
1. Quelle loi suit $5U + 2$ ?
2. Quelle fonction de $U$ suit la loi exponentielle de paramètre $\lambda$ ?
3. Quelle loi suit $3 + 2Z$ ?
4. Pour la loi catégorielle de probabilités $(0{,}5 ;\ 0{,}3 ;\ 0{,}2)$ sur les classes 1, 2 et 3, quelle classe donne le nombre uniforme $u = 0{,}65$ ?
5. Vrai ou faux : $1 - U$ suit aussi la loi uniforme sur $[0 ; 1]$.
6. Pourquoi la simulation par inversion est-elle malcommode pour la loi normale ?

<a id="rappels"></a>

## 🔁 Rappels

### M02b.R1 — Espérance d'une variable discrète (R8) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

$X$ prend les valeurs $-2$, $0$ et $3$ avec les probabilités 0,3 ; 0,5 et 0,2.
1. $\mathbb{E}[X]$ ?
2. $\mathbb{E}[X^2]$ ?
3. $\mathbb{V}(X)$ ?
4. $\mathbb{E}[2X - 1]$ et $\mathbb{V}(2X - 1)$ ?

### M02b.R2 — Intégrales et densités (M02a) 🔁 ★ ⏱️ 5 min
*Fiche §3 et §4 · parcours C, E*

1. $\int_0^3 x^2\,dx$ ?
2. $\int_0^{+\infty} e^{-4x}\,dx$ ?
3. La fonction $f(x) = \frac{3}{x^4}$ sur $[1 ; +\infty[$ (et 0 ailleurs) est-elle une densité ?
4. Pour cette fonction, que vaut $P(X \le 2)$ ?

### M02b.R3 — Coefficients binomiaux (R8) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C*

1. $\binom{6}{2}$ ?
2. $\binom{8}{3}$ ?
3. $\binom{10}{0}$ et $\binom{10}{10}$ ?
4. Combien de mots de 7 lettres, formés seulement de A et de B, contiennent exactement deux A ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/9"` ;
- une expression entre guillemets, dans la variable indiquée, avec `**` pour les puissances, `exp`, `ln` et `sqrt`, et des parenthèses autour d'un dénominateur, comme `"3/(2*p)"` ou `"sqrt(y)/5"` ;
- une liste entre crochets, comme `[0.25, 0.75]` ; un intervalle entre guillemets, comme `"[-2 ; 7]"` ; vrai ou faux par `True` ou `False`.

### Ex M02b.1 — Loi de Bernoulli et loi binomiale ✏️ ★ ⏱️ 20 min
**Objectif :** reconnaître une loi binomiale, calculer ses probabilités, son espérance et sa variance.
**Prérequis :** fiche §2 et §4 ; R8 (coefficients binomiaux) · **Parcours :** C, E

Une joueuse de basket réussit chaque lancer franc avec la probabilité 0,8, indépendamment des autres lancers. Elle tire 5 lancers francs, et $X$ est son nombre de réussites.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X = 5)$ | un nombre (4 décimales) |
| b | $P(X = 3)$ | un nombre (4 décimales) |
| c | $P(X \ge 4)$ | un nombre (4 décimales) |
| d | la valeur de $X$ la plus probable | un entier |
| e | $\mathbb{E}[X]$ | un nombre (1 décimale) |
| f | $\mathbb{V}(X)$ | un nombre (2 décimales) |
| g | la probabilité de rater au moins un des 5 lancers | un nombre (4 décimales) |
| h | le plus petit nombre $n$ de lancers pour lequel la probabilité de rater au moins un lancer atteint 0,9 | un entier |

Dans ta copie : écris la loi complète de $X$ (six probabilités) et vérifie que leur somme vaut 1. Quelle est la loi du nombre d'échecs $5 - X$ ?

### Ex M02b.2 — Loi géométrique : probabilités, et l'espérance par une série ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des probabilités d'une loi géométrique, et démontrer son espérance avec une série géométrique.
**Prérequis :** fiche §2 et §4 ; R5 (somme d'une suite géométrique) · **Parcours :** C, E

Un programme tente de se connecter à un serveur surchargé. Chaque tentative réussit avec la probabilité 0,4, indépendamment des autres, et le programme recommence jusqu'à la première réussite. $X$ est le numéro de la tentative qui réussit ; on note $q = 1 - 0{,}4 = 0{,}6$.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X = 3)$ | un nombre (3 décimales) |
| b | $P(X > 3)$ | un nombre (3 décimales) |
| c | $P(X \le 2)$ | un nombre (2 décimales) |
| d | la somme $S = \sum_{k=1}^{+\infty} k\,q^{k-1}$ pour $q = 0{,}6$ : calcule $S - qS$, reconnais une série géométrique, puis déduis $S$ | un nombre (2 décimales) |
| e | $\mathbb{E}[X] = \sum_{k \ge 1} k\,P(X = k)$, avec d | un nombre (1 décimale) |
| f | le nombre moyen de tentatives **échouées** avant la réussite | un nombre (1 décimale) |
| g | la médiane de $X$ : le plus petit entier $k$ tel que $P(X \le k) \ge 0{,}5$ | un entier |
| h | $\mathbb{E}[X]$ pour une probabilité de réussite $p$ quelconque ($0 < p \le 1$), avec la même méthode | une expression en $p$ |

Dans ta copie : écris le calcul de $S - qS$ terme à terme (on admet qu'on peut manipuler ces séries convergentes comme des sommes finies). Pourquoi la réponse de f se déduit-elle de e sans nouveau calcul ?

### Ex M02b.3 — Loi de Poisson : probabilités, espérance, et la somme de deux variables de Poisson indépendantes ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des probabilités de Poisson, et découvrir que la somme de deux variables de Poisson indépendantes est encore une variable de Poisson.
**Prérequis :** fiche §2 et §6 · **Parcours :** C

Chaque jour, le dépôt d'une bibliothèque de code reçoit $X$ signalements de bugs et $Y$ demandes de fonctionnalités. On modélise $X$ par la loi de Poisson de paramètre 1,5 et $Y$ par la loi de Poisson de paramètre 2,5, les deux étant indépendantes. On note $S = X + Y$.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X = 0)$ | un nombre (4 décimales) |
| b | $P(X = 2)$ | un nombre (4 décimales) |
| c | $P(X \ge 2)$ | un nombre (4 décimales) |
| d | le nombre moyen de signalements de bugs sur 5 jours | un nombre (1 décimale) |
| e | $P(S = 0)$ | un nombre (4 décimales) |
| f | $P(S = 1)$ (deux cas : lesquels ?) | un nombre (4 décimales) |
| g | $P(S = 2)$ (trois cas) | un nombre (4 décimales) |
| h | e, f et g sont les probabilités $e^{-\lambda}\frac{\lambda^k}{k!}$ d'une même loi de Poisson : laquelle ? Donne $\lambda$ | un nombre (1 décimale) |

Dans ta copie : démontre que $P(S = k) = e^{-4}\frac{4^k}{k!}$ pour tout entier $k \ge 0$, en écrivant $P(S = k) = \sum_{i=0}^{k} P(X = i)\,P(Y = k - i)$ et en utilisant la formule du binôme (fiche §2).

### Ex M02b.4 — Lois uniforme et exponentielle : probabilités et espérance ✏️ ★ ⏱️ 20 min
**Objectif :** calculer probabilités, espérance et écart-type pour une loi uniforme et une loi exponentielle.
**Prérequis :** fiche §3 et §4 · **Parcours :** C, E

Un train part à un instant aléatoire, uniformément réparti entre 8 h 10 et 8 h 25. On note $D$ le nombre de minutes écoulées après 8 h au moment du départ : $D \sim \mathcal{U}([10 ; 25])$. Ensuite, la durée de vie $T$ (en années) d'un disque dur suit la loi exponentielle de paramètre $\lambda = 0{,}4$.

| | Question | Réponse attendue |
|---|---|---|
| a | la densité de $D$ sur $[10 ; 25]$ | une fraction irréductible |
| b | $P(D \le 15)$ | une fraction irréductible |
| c | $P(12 \le D \le 20)$ | une fraction irréductible |
| d | $\mathbb{E}[D]$ | un nombre (1 décimale) |
| e | $\sigma(D)$ | un nombre (3 décimales) |
| f | $P(T > 5)$ | un nombre (4 décimales) |
| g | $\mathbb{E}[T]$ | un nombre (1 décimale) |
| h | $P\big(T > \mathbb{E}[T]\big)$ | un nombre (4 décimales) |

Dans ta copie : pourquoi h est-il inférieur à $\frac{1}{2}$ ? Montre que $P\big(T > \mathbb{E}[T]\big)$ a la même valeur pour tout $\lambda$.

### Ex M02b.5 — Loi normale : standardiser et lire la fonction Φ ✏️ ★★ ⏱️ 20 min
**Objectif :** ramener une loi normale à la loi normale centrée réduite, et lire la table de $\Phi$ dans les deux sens.
**Prérequis :** fiche §3 (la table de $\Phi$) · **Parcours :** C, E

La durée $X$ (en minutes) d'un trajet domicile-travail suit la loi normale $\mathcal{N}(30, 4^2)$. Utilise la table de $\Phi$ de la fiche, et $\Phi(-z) = 1 - \Phi(z)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le z-score d'une durée de 36 minutes | un nombre (1 décimale) |
| b | $P(X \le 36)$ | un nombre (4 décimales) |
| c | $P(X \le 27)$ | un nombre (4 décimales) |
| d | $P(27 \le X \le 36)$ | un nombre (4 décimales) |
| e | $P(X > 38)$ | un nombre (4 décimales) |
| f | la durée $t$ telle que $P(X \le t) = 0{,}9901$ | un nombre (2 décimales) |
| g | $P(\lvert X - 30 \rvert \le 5)$ | un nombre (3 décimales) |
| h | un autre itinéraire a une durée $Y \sim \mathcal{N}(31, 2^2)$ : $P(Y > 34)$ | un nombre (4 décimales) |

Dans ta copie : tu pars 34 minutes avant un rendez-vous ; quel itinéraire choisis-tu pour avoir le plus de chances d'arriver à l'heure ? Et si tu ne pars que 28 minutes avant ? Explique pourquoi la réponse change.

### Ex M02b.6 — Espérance et variance d'une variable continue (théorème de transfert) ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer l'espérance et la variance d'une variable à densité, et l'espérance d'une fonction de cette variable sans chercher sa loi.
**Prérequis :** fiche §4 ; M02a (intégration par parties) · **Parcours :** C, E

$X$ a pour densité $f(x) = 2(1 - x)$ sur $[0 ; 1]$, et 0 ailleurs.

| | Question | Réponse attendue |
|---|---|---|
| a | $P\big(X \le \frac{1}{2}\big)$ | une fraction irréductible |
| b | $\mathbb{E}[X]$ | une fraction irréductible |
| c | $\mathbb{E}[X^2]$ | une fraction irréductible |
| d | $\mathbb{V}(X)$ | une fraction irréductible |
| e | $\mathbb{E}[5X + 2]$ | une fraction irréductible |
| f | $\mathbb{V}(5X + 2)$ | une fraction irréductible |
| g | $\mathbb{E}[e^X]$ (par parties) | un nombre (4 décimales) |
| h | $e^{\mathbb{E}[X]} < \mathbb{E}[e^X]$ | vrai ou faux |

Dans ta copie : vérifie d'abord que $f$ est une densité, et dessine-la avec $\mathbb{E}[X]$ et la médiane. Compare aussi $\mathbb{E}[X^2]$ et $\mathbb{E}[X]^2$ : quelle inégalité, du même type que h, retrouves-tu ?

### Ex M02b.7 — Un couple de variables discrètes : loi jointe, marginales, indépendance ✏️ ★★ ⏱️ 20 min
**Objectif :** lire une loi jointe, calculer ses marginales et une espérance de produit, et décider de l'indépendance.
**Prérequis :** fiche §5 · **Parcours :** C, E

On choisit au hasard un utilisateur d'une application. $X$ est son nombre d'appareils connectés (1 ou 2), et $Y$ son nombre de connexions dans la journée (0, 1 ou 2). Leur loi jointe :

| | $Y = 0$ | $Y = 1$ | $Y = 2$ |
|---|---|---|---|
| $X = 1$ | 0,15 | 0,25 | 0,10 |
| $X = 2$ | 0,05 | 0,15 | 0,30 |

Ensuite, deux variables $X'$ et $Y'$ sont **indépendantes**, avec $P(X' = 1) = 0{,}3$, $P(X' = 2) = 0{,}7$, et $P(Y' = 0) = 0{,}5$, $P(Y' = 1) = 0{,}3$, $P(Y' = 2) = 0{,}2$. Enfin, deux variables $U$ et $V$ à valeurs dans $\{0, 1\}$ ont pour loi jointe $P(U = 0, V = 0) = 0{,}12$, $P(U = 0, V = 1) = 0{,}28$, $P(U = 1, V = 0) = 0{,}18$, la dernière case étant à compléter.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(Y \ge 1)$ | un nombre (2 décimales) |
| b | la loi marginale de $Y$ : $[P(Y = 0), P(Y = 1), P(Y = 2)]$ | une liste (2 décimales) |
| c | $\mathbb{E}[Y]$ | un nombre (2 décimales) |
| d | $\mathbb{E}[XY]$ | un nombre (2 décimales) |
| e | $\mathbb{E}[X]\,\mathbb{E}[Y]$ | un nombre (2 décimales) |
| f | $X$ et $Y$ sont indépendantes | vrai ou faux |
| g | $P(X' = 2, Y' = 1)$ | un nombre (2 décimales) |
| h | $U$ et $V$ sont indépendantes | vrai ou faux |

Dans ta copie : quelle case du premier tableau suffit à prouver la dépendance ? Que dit-elle concrètement de ces utilisateurs ? Écris la loi jointe complète de $(X', Y')$.

### Ex M02b.8 — Linéarité et variance d'une somme : sommes et moyennes de variables ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer l'espérance et l'écart-type d'une somme, d'une différence et d'une moyenne de variables indépendantes.
**Prérequis :** fiche §6 · **Parcours :** C, E

Un pipeline de données enchaîne trois tâches, de durées $T_1$, $T_2$ et $T_3$ (en minutes), indépendantes, d'espérances 4, 6 et 10, et d'écarts-types 1, 2 et 2. On note $S = T_1 + T_2 + T_3$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{E}[S]$ | un entier |
| b | $\mathbb{V}(S)$ | un entier |
| c | $\sigma(S)$ | un entier |
| d | $\mathbb{E}[T_3 - T_2]$ | un entier |
| e | $\sigma(T_3 - T_2)$ | un nombre (3 décimales) |
| f | on exécute 50 fois la tâche 1, de façon indépendante (50 durées i.i.d., de même loi que $T_1$) : l'écart-type de la durée **totale** | un nombre (3 décimales) |
| g | l'écart-type de la durée **moyenne** de ces 50 exécutions | un nombre (4 décimales) |
| h | $\mathbb{V}(T_1 + T_1)$ | un entier |

Dans ta copie : explique la différence entre h et la variance de la durée totale de **deux** exécutions indépendantes de la tâche 1.

### Ex M02b.9 — Une intégrale double sur un rectangle, et une densité jointe ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des intégrales doubles sur un rectangle, et s'en servir pour une densité jointe, ses marginales et une probabilité.
**Prérequis :** fiche §7 · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | $\iint_{[0 ; 1] \times [0 ; 3]} x\,y^2\,dx\,dy$ | une fraction irréductible |
| b | $\iint_{[0 ; 1] \times [0 ; 1]} e^{x + y}\,dx\,dy$ | un nombre (4 décimales) |
| c | $\iint_{[0 ; 1] \times [0 ; 1]} (x^2 + xy)\,dx\,dy$ | une fraction irréductible |

On pose $f(x, y) = c\,x\,y^2$ pour $(x, y)$ dans $[0 ; 1] \times [0 ; 3]$, et 0 ailleurs.

| | Question | Réponse attendue |
|---|---|---|
| d | la constante $c$ pour que $f$ soit une densité jointe | une fraction irréductible |
| e | la densité marginale $f_X(x)$, pour $x$ dans $[0 ; 1]$ | une expression en $x$ |
| f | la densité marginale $f_Y(y)$, pour $y$ dans $[0 ; 3]$ | une expression en $y$ |
| g | $X$ et $Y$ sont indépendantes | vrai ou faux |
| h | $P\big(X \le \frac{1}{2},\ Y \le 1\big)$ | une fraction irréductible |

Dans ta copie : calcule c dans les deux ordres d'intégration. Pour b, quelle propriété de $e^{x + y}$ permet d'écrire l'intégrale double comme un produit ?

### Ex M02b.10 — Changement de variable : la loi de aX + b, et celle de X² ✏️ ★★ ⏱️ 20 min
**Objectif :** trouver la loi d'une variable transformée en passant par la fonction de répartition.
**Prérequis :** fiche §3 et §8 · **Parcours :** C

D'abord, $X$ suit la loi uniforme sur $[0 ; 2]$ et $Y = 3X - 1$. Ensuite, $X$ suit $\mathcal{N}(10, 3^2)$ et $Y = 2X + 5$. Enfin, $X$ suit la loi uniforme sur $[0 ; 3]$ et $Y = X^2$.

| | Question | Réponse attendue |
|---|---|---|
| a | pour $Y = 3X - 1$ : l'intervalle des valeurs de $Y$ | un intervalle |
| b | la densité de $Y = 3X - 1$ sur cet intervalle | une fraction irréductible |
| c | $P(3X - 1 \le 2)$ | une fraction irréductible |
| d | pour $Y = 2X + 5$, avec $X \sim \mathcal{N}(10, 3^2)$ : la densité de $Y$ en 25 | un nombre (4 décimales) |
| e | pour $Y = X^2$, avec $X \sim \mathcal{U}([0 ; 3])$ : $F_Y(4) = P(Y \le 4)$ | une fraction irréductible |
| f | $F_Y(y)$ pour $0 \le y \le 9$ | une expression en $y$ |
| g | la densité $f_Y(y)$ pour $0 < y < 9$ | une expression en $y$ |
| h | $\mathbb{E}[Y] = \mathbb{E}[X^2]$ | un entier |

Dans ta copie : calcule h de deux façons, avec la densité de g puis par le théorème de transfert. Pour d, quelle loi suit $Y = 2X + 5$ ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex M02b.11 — La variance d'une somme de variables indépendantes ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer que les variances de variables indépendantes s'additionnent, et en tirer la variance d'une binomiale et celle d'une moyenne.
**Prérequis :** fiche §4, §5 et §6 ; R4 (Σ, récurrence) · **Parcours :** C, E

$X$ et $Y$ sont deux variables aléatoires discrètes qui prennent un nombre fini de valeurs, définies sur le même univers. On utilise la linéarité de l'espérance (fiche §6).
1. Démontre que $\mathbb{V}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2$, à partir de la définition $\mathbb{V}(X) = \mathbb{E}\big[(X - \mathbb{E}[X])^2\big]$.
2. On suppose $X$ et $Y$ indépendantes. Démontre que $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$, en écrivant $\mathbb{E}[XY]$ comme une double somme sur les valeurs $x$ et $y$ (théorème de transfert pour un couple, fiche §5).
3. Sans supposer l'indépendance, développe $\big(X + Y - \mathbb{E}[X] - \mathbb{E}[Y]\big)^2$ et démontre que $\mathbb{V}(X + Y) = \mathbb{V}(X) + \mathbb{V}(Y) + 2\big(\mathbb{E}[XY] - \mathbb{E}[X]\,\mathbb{E}[Y]\big)$.
4. Conclus : si $X$ et $Y$ sont indépendantes, $\mathbb{V}(X + Y) = \mathbb{V}(X) + \mathbb{V}(Y)$. Que vaut alors $\mathbb{V}(X - Y)$ ? (Commence par justifier que $X$ et $-Y$ sont indépendantes.)
5. Démontre par récurrence sur $n \ge 2$ que $\mathbb{V}(X_1 + \cdots + X_n) = \mathbb{V}(X_1) + \cdots + \mathbb{V}(X_n)$ pour des variables mutuellement indépendantes (on admet que $X_1 + \cdots + X_{n-1}$ est alors indépendante de $X_n$).
6. Applications : déduis-en la variance de la loi binomiale $\mathcal{B}(n, p)$ (fiche §6, les indicatrices), puis la variance de la moyenne $\bar{X}$ de $n$ variables i.i.d. de variance $\sigma^2$.
7. Un contre-exemple : $X$ suit la loi de Bernoulli de paramètre $\frac{1}{2}$, et $Y = X$. Compare $\mathbb{V}(X + Y)$ et $\mathbb{V}(X) + \mathbb{V}(Y)$. Quelle hypothèse manque ?

### Ex M02b.12 — L'intégrale de Gauss par une intégrale double (changement en coordonnées polaires admis) ∂ ★★★ ⏱️ 30 min
**Objectif :** démontrer que $\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt{\pi}$, la valeur admise en M02a, et en déduire que la densité normale a une aire de 1.
**Prérequis :** fiche §7 ; M02a §4 (intégrales impropres, règle de comparaison) · **Parcours :** C

Pour $R > 0$, on pose $I(R) = \int_{-R}^{R} e^{-x^2}\,dx$, $C_R$ le carré $[-R ; R] \times [-R ; R]$, et $D_r$ le disque de centre $O$ et de rayon $r$. On note $g(x, y) = e^{-(x^2 + y^2)}$.
1. Démontre que $I(R)^2 = \iint_{C_R} g(x, y)\,dx\,dy$ (le cas d'un produit, fiche §7).
2. On pose $J(r) = \iint_{D_r} g(x, y)\,dx\,dy$. En passant en coordonnées polaires (fiche §7, admis), démontre que $J(r) = \pi\big(1 - e^{-r^2}\big)$.
3. Fais un dessin, puis justifie que $D_R \subset C_R \subset D_{R\sqrt{2}}$. Comme $g$ est positive, l'intégrale sur une région plus grande est plus grande (admis) : déduis-en un encadrement de $I(R)^2$ entre deux valeurs de $J$.
4. Fais tendre $R$ vers $+\infty$ et conclus que $\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt{\pi}$. Pourquoi peut-on prendre la racine carrée, sans signe $\pm$ ?
5. Par le changement de variable $x = \frac{t}{\sqrt{2}}$ (M02a §3), déduis-en $\int_{-\infty}^{+\infty} e^{-t^2/2}\,dt = \sqrt{2\pi}$, puis que la densité de $\mathcal{N}(\mu, \sigma^2)$ a une aire totale de 1 (un second changement de variable, $t = \frac{x - \mu}{\sigma}$).
6. Pour aller plus loin : montre que $h(x, y) = \frac{1}{2\pi}e^{-(x^2 + y^2)/2}$ est une densité jointe sur $\mathbb{R}^2$, et qu'elle est le produit de deux densités $\varphi$. Que peut-on en dire des deux coordonnées d'un point de densité $h$ ?

### Ex M02b.13 — La loi de Poisson, limite de lois binomiales ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer que la loi binomiale $\mathcal{B}\big(n, \frac{\lambda}{n}\big)$ tend vers la loi de Poisson de paramètre $\lambda$, et comprendre quand l'approximation est bonne.
**Prérequis :** fiche §2 ; R6 (ln, exp) ; R7 (limites, nombre dérivé) · **Parcours :** C

On fixe $\lambda > 0$ et un entier $k \ge 0$. Pour $n > \lambda$ et $n \ge k$, $X_n$ suit la loi binomiale $\mathcal{B}\big(n, \frac{\lambda}{n}\big)$.
1. Démontre que
$$P(X_n = k) = \frac{n(n-1)\cdots(n-k+1)}{n^k} \times \frac{\lambda^k}{k!} \times \left(1 - \frac{\lambda}{n}\right)^n \times \left(1 - \frac{\lambda}{n}\right)^{-k}.$$
2. Démontre que le premier facteur tend vers 1 quand $n \to +\infty$ ($k$ est fixé : combien de facteurs y a-t-il ?).
3. Démontre que $\left(1 - \frac{\lambda}{n}\right)^n$ tend vers $e^{-\lambda}$. Indication : écris-le $\exp\big(n \ln(1 - \frac{\lambda}{n})\big)$, pose $h = -\frac{\lambda}{n}$, et utilise $\lim_{h \to 0}\frac{\ln(1 + h)}{h} = 1$ (le nombre dérivé de $\ln$ en 1, R7).
4. Que devient le dernier facteur ? Conclus : $P(X_n = k) \to e^{-\lambda}\frac{\lambda^k}{k!}$.
5. Application numérique : pour $\lambda = 2$, calcule $P(X_n = 0)$ pour $n = 10$, $n = 100$ et $n = 1\,000$, et compare avec $e^{-2}$. L'écart diminue-t-il à peu près comme $\frac{1}{n}$ ?
6. Explique en deux phrases pourquoi la loi de Poisson modélise bien un nombre d'événements rares sur une longue période (des pannes, des clics), et pourquoi elle modélise mal le nombre de faces en 10 lancers d'une pièce.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M02b.14 — Combien d'erreurs d'annotation dans un dataset ? Binomiale et Poisson 🔗 ★ ⏱️ 15 min
**Objectif :** modéliser des erreurs rares dans un dataset par une loi binomiale, l'approcher par une loi de Poisson, et décider combien d'exemples vérifier.
**Prérequis :** fiche §2 et §4 · **Parcours :** C, E

Un dataset compte 2 000 images annotées à la main. Chaque annotation est fausse avec la probabilité 0,002, indépendamment des autres. $X$ est le nombre d'annotations fausses du dataset.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{E}[X]$ | un entier |
| b | $\sigma(X)$, avec la loi binomiale | un nombre (3 décimales) |
| c | $P(X = 0)$, avec la loi binomiale | un nombre (4 décimales) |
| d | $P(X = 0)$, avec l'approximation de Poisson | un nombre (4 décimales) |
| e | $P(X \le 2)$, avec l'approximation de Poisson | un nombre (4 décimales) |
| f | on vérifie 500 images tirées au hasard, et $Y$ est le nombre d'annotations fausses trouvées : $P(Y \ge 1)$, avec l'approximation de Poisson | un nombre (4 décimales) |
| g | le plus petit nombre $n$ d'images à vérifier pour trouver au moins une erreur avec une probabilité d'au moins 0,9, avec l'approximation de Poisson | un entier |

Dans ta copie : pourquoi la loi de Poisson convient-elle ici ? Que devient l'approximation si chaque annotation est fausse avec la probabilité 0,2 ? Un dataset réel a souvent des erreurs **groupées** (un annotateur fatigué, une classe ambiguë) : quelle hypothèse du modèle tombe alors ?

### Ex M02b.15 — MML §6.1 et §6.2 : espace probabilisé, pmf et pdf, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la construction d'un espace probabilisé et la description des lois discrètes et continues, et relier les notations du livre à celles de la fiche.
**Prérequis :** fiche §1 à §3 · **Parcours :** C

Lis MML §6.1 en entier, puis §6.2 (la partie discrète en détail ; la partie continue est une relecture de M02a). Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Le livre distingue deux façons de comprendre une probabilité (§6.1.1). Lesquelles ? En une phrase chacune, avec un exemple à toi.
2. Quels sont les trois éléments d'un espace probabilisé, et leurs noms anglais (§6.1.2) ? Quel quatrième ensemble le livre ajoute-t-il pour définir une variable aléatoire ?
3. Le livre dit que le nom *random variable* est trompeur. Pourquoi ? Relie sa remarque au §1 de la fiche.
4. Le livre illustre une variable aléatoire par un tirage d'objets dans un sac. Refais le même type de raisonnement avec **ta propre expérience** : deux lancers d'une pièce équilibrée, et $X$ = le nombre de faces. Écris $\Omega$, la fonction $X$ issue par issue, et la loi de $X$.
5. En §6.2.1, comment le livre obtient-il une loi jointe à partir d'un tableau de comptages, puis les marginales ? Fais le lien avec le tableau du stand de glaces (fiche §5).
6. Quelles abréviations le livre emploie-t-il pour une fonction de masse, une densité et une fonction de répartition ? Pourquoi écrit-il souvent $p(x)$ dans les deux cas ?
7. Note trois mots ou tournures en anglais de ces deux sections qui étaient nouveaux pour toi, avec leur traduction.

### Ex M02b.16 — MML §6.4 et §6.7 : espérance, variance, sommes de variables, changement de variable 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais les définitions de l'espérance et de la variance, les règles pour les sommes de variables, et le calcul de la loi d'une variable transformée.
**Prérequis :** fiche §4, §6 et §8 · **Parcours :** C

Lis MML §6.4 (sauf §6.4.2 et §6.4.6), puis §6.7.1 et le début de §6.7.2 (le cas d'une seule variable). Réponds dans ta copie, avec tes mots.
1. Comment le livre définit-il l'espérance (§6.4.1) ? En quoi sa définition contient-elle déjà le théorème de transfert de la fiche ?
2. Le livre cite d'autres façons de résumer une loi que l'espérance. Lesquelles ? Pour la loi exponentielle de paramètre 3 (fiche §4), donne-les.
3. En §6.4.3, le livre présente trois écritures de la variance. Lesquelles reconnais-tu dans la fiche ? Le livre signale un inconvénient **numérique** de l'une d'elles : lequel, et pourquoi un ordinateur y est-il sensible ?
4. En §6.4.4, quelles formules le livre donne-t-il pour l'espérance et la variance d'une somme ? Que devient la variance quand les variables sont indépendantes (§6.4.5) ?
5. En §6.7.1, le livre calcule la loi d'une transformation par la fonction de répartition. Refais le même raisonnement avec **ta propre loi** : $X$ uniforme sur $[0 ; 1]$ et $Y = \sqrt{X}$. Trouve $F_Y$ puis $f_Y$.
6. Quel résultat le livre énonce-t-il sur la variable $F(X)$, quand $F$ est la fonction de répartition de $X$ ? Pourquoi est-ce, en sens inverse, la simulation par inversion de la fiche (§8) ?
7. Écris la formule du changement de variable pour une seule variable telle que la donne §6.7.2, avec les notations de la fiche, et vérifie-la sur ton exemple de la question 5.

### Ex M02b.17 — Expliquer la différence entre une variable aléatoire et sa loi 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement ce qu'est une variable aléatoire, ce qu'est sa loi, et pourquoi deux variables de même loi ne sont pas forcément égales.
**Prérequis :** fiche §1 · **Parcours :** C

Une amie qui commence le machine learning te demande : « Dans le cours, on dit que $X$ et $Y$ "suivent la même loi normale". Ça veut dire qu'elles sont égales ? Et c'est quoi, au juste, une variable aléatoire ? »

Réponds-lui **en huit lignes au plus**, avec un exemple simple et sans formule compliquée. Ta réponse doit dire ce qu'est une variable aléatoire (une fonction de quoi dans quoi), ce que décrit sa loi, ce qu'est un tirage, et donner un exemple de deux variables de même loi qui ne sont presque jamais égales.

<a id="entretien"></a>

## 💼 Entretien

### M02b.E1 — Quand modéliser un comptage par une loi de Poisson ? 💼 ★ ⏱️ 10 min
*Fiche §2 · parcours C, E*

« Vous devez modéliser le nombre de requêtes que reçoit un service web chaque minute. Proposeriez-vous une loi de Poisson ? Sous quelles hypothèses, et comment vérifieriez-vous qu'elle convient ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit citer les hypothèses de la loi de Poisson, un test simple sur des données (que comparer à quoi ?), et deux situations où elle ne convient pas. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m02b_variables_aleatoires/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M02b.18 | Lois binomiale et de Poisson · `binomial_pmf`, `poisson_pmf` | 🔨 | ★ | 20 | C, E |
| M02b.19 | Densité et fonction de répartition de la loi normale (avec `math.erf`) · `normal_pdf`, `normal_cdf` | 🔨 | ★ | 20 | C, E |
| M02b.20 | Simuler par inversion de la fonction de répartition · `inverse_transform_sample` | 🔨 | ★★ | 20 | C |
| M02b.21 | `scipy.stats` : pmf, pdf, cdf, ppf et rvs | 📦 | ★ | 15 | C, E |
| M02b.22 | Prédire : la variance de la moyenne de quatre dés | 🔮 | ★ | 10 | C, E |
| M02b.23 | Binomiale et Poisson côte à côte quand n grandit | 🔬 | ★★ | 20 | C |
| M02b.24 | Une loi jointe en carte de chaleur, ses marginales sur les bords | 🎨 | ★ | 20 | C |
| M02b.25 | Chasse à l'erreur : une densité prise pour une probabilité, σ et σ² | 🐛 | ★ | 15 | C |
| M02b.26 | Documenter une loi : docstring et exemples testés (`doctest`) | 🛠️ | ★ | 15 | C |
| M02b.27 | Défi : tirer des valeurs normales avec seulement des tirages uniformes | 🏆 | ★★★ | 30 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
