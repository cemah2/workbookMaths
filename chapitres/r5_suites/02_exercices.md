# R5 · Suites — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r5_suites/06_mes_reponses.md` (créée par `python tools/start_chapter.py R5`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂ et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**La calculatrice (ou Python) est permise** pour les puissances décimales, comme $1{,}025^{10}$, et pour les divisions qui ne tombent pas juste ; tout le reste se fait à la main. Écris d'abord la formule que tu utilises, avec ses nombres, puis le résultat : c'est la formule qui compte.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R5.Q1 — Explicite ou par récurrence ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. La suite $u_n = 5 - 2n$ est-elle définie explicitement ou par récurrence ?
2. La suite définie par $u_0 = 1$ et $u_{n+1} = u_n + n$ est-elle définie explicitement ou par récurrence ?
3. Pour $u_n = n^2 + 1$, calcule $u_{20}$.
4. Pour $u_0 = 2$ et $u_{n+1} = 3u_n - 1$, peut-on calculer $u_{20}$ avec la seule règle de récurrence, sans calculer les termes précédents ?
5. Vrai ou faux : la règle $u_{n+1} = u_n^2$, sans rien d'autre, définit une suite.
6. Pour $u_n = (-1)^n$, écris $u_0$, $u_1$, $u_2$ et $u_3$. Cette suite est-elle croissante, décroissante, ou ni l'une ni l'autre ?

### R5.Q2 — Arithmétique, géométrique, ou ni l'une ni l'autre ? 🧠 ★ ⏱️ 4 min
*Fiche §2 et §3 · parcours C, E*

Pour chaque suite (on suppose que la règle des premiers termes continue), dis si elle est arithmétique, géométrique, les deux ou aucune, et donne sa raison quand elle en a une.
1. 4, 9, 14, 19, …
2. 5, 10, 20, 40, …
3. 1, 4, 9, 16, …
4. 10, 7, 4, 1, …
5. 2, −6, 18, −54, …
6. 5, 5, 5, 5, …
7. $u_n = 7 \times 0{,}9^n$

### R5.Q3 — Formules de somme : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Vrai ou faux ?
1. $1 + 2 + \dots + 100 = 5\,050$.
2. La somme $u_0 + u_1 + \dots + u_n$ compte $n$ termes.
3. Pour tout réel $q$ et tout entier $n \ge 1$, $1 + q + \dots + q^{n-1} = \frac{1 - q^n}{1 - q}$.
4. Si $q = 1$, $1 + q + \dots + q^{n-1} = n$.
5. La somme de termes consécutifs d'une suite arithmétique vaut le nombre de termes multiplié par la moyenne du premier et du dernier.
6. $\sum_{k=0}^{3} 5^k = \frac{5^4 - 1}{4}$.
7. $\sum_{k=1}^{5} 3^k = \frac{1 - 3^5}{1 - 3}$.

### R5.Q4 — Converge ou diverge ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Pour chaque suite : converge-t-elle (vers quelle limite ?), tend-elle vers $+\infty$, ou n'a-t-elle pas de limite ?
1. $0{,}8^n$
2. $1{,}02^n$
3. $(-1)^n$
4. $3 + \frac{1}{n}$ (pour $n \ge 1$)
5. $(-0{,}5)^n$
6. $n^2 - 10n$
7. Vrai ou faux : une suite qui ne tend pas vers $+\infty$ converge.

### R5.Q5 — Moyenne mobile ou moyenne exponentielle ? 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Laquelle des deux n'a besoin de garder en mémoire que sa dernière valeur pour calculer la suivante ?
2. Laquelle donne le même poids à chaque valeur qu'elle utilise ?
3. Laquelle ne donne aucune valeur pour les premiers instants ?
4. Combien de moyennes donne une moyenne mobile sur une fenêtre de 4 valeurs, appliquée à une série de 10 valeurs ?
5. Pour une série de valeurs toutes proches de 50, la moyenne exponentielle (partie de $v_0 = 0$) commence-t-elle trop haut ou trop bas ?
6. Pour qu'une moyenne exponentielle lisse davantage, faut-il augmenter ou diminuer $\beta$ ?

### R5.Q6 — Les poids d'une moyenne exponentielle 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

On pose $v_0 = 0$ et $v_t = 0{,}7\,v_{t-1} + 0{,}3\,x_t$.
1. Quel est le poids de $x_t$ dans $v_t$ ?
2. Vrai ou faux : le poids de $x_{t-1}$ dans $v_t$ vaut 0,7 fois celui de $x_t$.
3. Les poids de $x_t, x_{t-1}, x_{t-2}, \dots$ dans $v_t$ forment-ils une suite arithmétique ou géométrique ? De quelle raison ?
4. Quelle valeur a le plus grand poids dans $v_t$ : la plus récente ou la plus ancienne ?
5. Vrai ou faux : dans une moyenne mobile sur 5 valeurs, chaque valeur de la fenêtre a le poids 0,2.
6. Que vaut $v_t$ si l'on remplace 0,7 par 0 et 0,3 par 1 ?

<a id="rappels"></a>

## 🔁 Rappels

### R5.R1 — Σ et changement d'indice (R4) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

1. Écris $\sum_{k=0}^{3} (2k + 1)$ en extension, puis calcule-la.
2. Combien de termes comptent $\sum_{k=0}^{n-1} a_k$ et $\sum_{k=1}^{n} a_k$ ?
3. On pose $j = k - 1$ dans $\sum_{k=1}^{6} 5^{k-1}$ : écris la somme avec l'indice $j$ et ses nouvelles bornes.
4. Calcule $\sum_{k=1}^{30} k$.

### R5.R2 — Raisonnement par récurrence (R4) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C*

On pose $u_0 = 2$ et $u_{n+1} = 3u_n - 2$ pour tout $n \ge 0$.
1. Calcule $u_1$, $u_2$ et $u_3$.
2. Compare-les à $3^1$, $3^2$, $3^3$ : conjecture une formule explicite pour $u_n$.
3. Démontre ta conjecture par récurrence (initialisation, hérédité, conclusion).

### R5.R3 — Évolutions successives (R1) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Un prix de 80 € augmente de 5 % : quel est le nouveau prix ?
2. Par quel nombre multiplie-t-on une quantité qui baisse de 12 % ?
3. Un prix augmente de 10 %, puis baisse de 10 %. Revient-il à sa valeur de départ ? Sinon, de quel pourcentage a-t-il évolué en tout ?
4. Trois hausses successives de 20 % : par quel nombre le prix est-il multiplié en tout ? Est-ce une hausse de 60 % ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les puissances décimales), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre avec un point décimal, comme `-1.5`, arrondi comme le demande la question ;
- une fraction exacte entre guillemets, comme `"5/7"` ;
- une expression en $n$ entre guillemets, comme `"3*n**2 + 1"` (avec `*` pour multiplier et `**` pour la puissance) ;
- une liste de nombres entre crochets, dans l'ordre demandé ;
- vrai ou faux par `True` ou `False` ; un numéro de réponse proposée par un nombre entier.

### Ex R5.1 — Calculer des termes : explicite et récurrence ✏️ ★ ⏱️ 10 min
**Objectif :** calculer des termes d'une suite définie explicitement ou par récurrence, conjecturer une formule explicite et étudier un sens de variation.
**Prérequis :** fiche §1 · **Parcours :** C, E

On pose $u_n = n^2 - 3n + 1$ pour $n \ge 0$ ; $v_0 = 3$ et $v_{n+1} = 2v_n - 4$ ; $w_1 = 1$ et $w_{n+1} = w_n + 2n + 1$ pour $n \ge 1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $u_5$ | un nombre entier |
| b | $u_{10}$ | un nombre entier |
| c | la liste `[v1, v2, v3]` | une liste de 3 nombres |
| d | $w_4$ | un nombre entier |
| e | une formule explicite de $w_n$, conjecturée à partir de $w_1$ à $w_4$ | une expression en `n` |
| f | la différence $u_{n+1} - u_n$, en fonction de $n$ | une expression en `n` |
| g | le plus petit entier $N$ tel que $u_{n+1} \ge u_n$ pour tout $n \ge N$ | un nombre entier |

### Ex R5.2 — Terme général d'une suite arithmétique ✏️ ★ ⏱️ 10 min
**Objectif :** écrire et utiliser le terme général d'une suite arithmétique, y compris quand elle commence au rang 1.
**Prérequis :** fiche §2 · **Parcours :** C, E

$(u_n)$ est la suite arithmétique de premier terme $u_0 = 7$ et de raison 4 ; $(a_n)$, la suite arithmétique de premier terme $a_1 = 12$ (elle commence au rang 1) et de raison −2,5.

| | Question | Réponse attendue |
|---|---|---|
| a | $u_n$ en fonction de $n$ | une expression en `n` |
| b | $u_{25}$ | un nombre entier |
| c | $a_{11}$ | un nombre |
| d | le rang du premier terme strictement négatif de $(a_n)$ | un nombre entier |
| e | le rang $n$ tel que $u_n = 2\,023$ | un nombre entier |
| f | 2 026 est un terme de $(u_n)$ | vrai ou faux |
| g | une bougie de 24 cm raccourcit de 1,5 cm par heure : au bout de combien d'heures est-elle entièrement consumée ? | un nombre entier |

### Ex R5.3 — Terme général d'une suite géométrique ✏️ ★ ⏱️ 10 min
**Objectif :** écrire et utiliser le terme général d'une suite géométrique, avec une raison fractionnaire, décimale ou négative.
**Prérequis :** fiche §3 · **Parcours :** C, E

$(v_n)$ est la suite géométrique de premier terme $v_0 = 5$ et de raison 3 ; $(w_n)$, la suite géométrique de premier terme $w_1 = 64$ et de raison $\frac{3}{4}$ ; $(t_n)$, la suite géométrique de premier terme $t_0 = 2$ et de raison −3. Une population de 500 bactéries augmente de 20 % par heure ; $p_n$ est sa taille au bout de $n$ heures.

| | Question | Réponse attendue |
|---|---|---|
| a | $v_n$ en fonction de $n$ | une expression en `n` |
| b | $v_4$ | un nombre entier |
| c | $w_4$ | un nombre entier |
| d | $w_7$ | une fraction |
| e | $p_3$ | un nombre entier |
| f | $t_5$ | un nombre entier |
| g | le plus petit entier $n$ tel que $p_n > 2\,000$ (essaie des valeurs de $n$) | un nombre entier |

### Ex R5.4 — Sommes arithmétiques et géométriques ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des sommes de termes consécutifs d'une suite arithmétique ou géométrique avec les formules, en comptant d'abord les termes.
**Prérequis :** fiche §4 ; R5.2, R5.3 · **Parcours :** C, E

Pour chaque somme, écris dans ta copie le premier terme, le nombre de termes et la raison (et le dernier terme pour une suite arithmétique), puis applique la formule.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de termes de $5 + 8 + 11 + \dots + 50$ | un nombre entier |
| b | la somme $5 + 8 + 11 + \dots + 50$ | un nombre entier |
| c | $\sum_{k=0}^{19} (2 + 0{,}5\,k)$ | un nombre |
| d | $1 + 4 + 16 + \dots + 4^5$ | un nombre entier |
| e | $81 + 54 + 36 + 24 + 16$, avec la formule (vérifie ensuite en additionnant) | un nombre entier |
| f | $\sum_{k=3}^{8} 2^k$ | un nombre entier |
| g | $\sum_{k=0}^{9} (-2)^k$ | un nombre entier |
| h | $\sum_{k=0}^{n-1} (3 + 2k)$, en fonction de $n$ | une expression en `n` |

### Ex R5.5 — Sommes infinies d'une suite géométrique ✏️ ★★ ⏱️ 15 min
**Objectif :** reconnaître une somme infinie géométrique, dire si elle a une valeur finie, et la calculer.
**Prérequis :** fiche §5 ; R5.4 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\sum_{k=0}^{+\infty} \left(\frac{3}{4}\right)^k$ | un nombre entier |
| b | $2 + \frac{2}{5} + \frac{2}{25} + \frac{2}{125} + \dots$ | une fraction |
| c | $9 - 6 + 4 - \frac{8}{3} + \dots$ | une fraction |
| d | $\sum_{k=1}^{+\infty} 0{,}3^k$ (attention au premier terme) | une fraction |
| e | la somme infinie $1 + 1{,}1 + 1{,}1^2 + \dots$ a une valeur finie | vrai ou faux |
| f | à partir de combien de termes la somme partielle de a) est-elle à moins de 0,1 de sa limite ? (essaie des valeurs) | un nombre entier |

### Ex R5.6 — Intérêts composés et actualisation ✏️ ★★ ⏱️ 20 min
**Objectif :** modéliser un placement par une suite géométrique, comparer intérêts simples et composés, actualiser une somme future.
**Prérequis :** fiche §3 et §5 ; R5.R3 · **Parcours :** C

On place 3 000 € à 2,5 % par an, à intérêts composés. Arrondis les montants au centime.

| | Question | Réponse attendue |
|---|---|---|
| a | le capital au bout d'un an | un nombre |
| b | le capital au bout de 10 ans | un nombre (2 décimales) |
| c | le capital au bout de 10 ans à intérêts **simples** (2,5 % de 3 000 € chaque année) | un nombre |
| d | le nombre d'années pleines au bout duquel le capital à intérêts composés dépasse 4 000 € | un nombre entier |
| e | la somme à placer aujourd'hui, au même taux, pour disposer de 5 000 € dans 6 ans | un nombre (2 décimales) |
| f | un autre placement rapporte 1 % **par mois**, à intérêts composés : de quel pourcentage le capital augmente-t-il en un an ? | un nombre (2 décimales) |
| g | au taux de 2,5 %, la valeur actuelle de 1 € reçu dans $n$ années tend vers 0 quand $n$ tend vers $+\infty$ | vrai ou faux |

### Ex R5.7 — Une moyenne exponentielle à la main sur cinq valeurs ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer pas à pas une moyenne exponentielle et une moyenne mobile, et constater le démarrage trop bas de la première.
**Prérequis :** fiche §6 · **Parcours :** C, E

On mesure les valeurs $x_1, \dots, x_5 = 10, 20, 15, 5, 25$. On calcule la moyenne exponentielle $v_0 = 0$, $v_t = 0{,}8\,v_{t-1} + 0{,}2\,x_t$.

| | Question | Réponse attendue |
|---|---|---|
| a | la liste `[v1, v2, v3, v4, v5]` | une liste de 5 nombres (4 décimales) |
| b | la liste des moyennes mobiles sur une fenêtre de 3 valeurs | une liste (2 décimales) |
| c | la moyenne des cinq valeurs | un nombre |
| d | $v_5$ est plus petit que la moyenne des cinq valeurs | vrai ou faux |
| e | le poids de $x_1$ dans $v_3$, en écrivant $v_3$ en fonction de $x_1$, $x_2$ et $x_3$ | un nombre |
| f | $v_5$ si l'on remplace 0,8 par 0 et 0,2 par 1 | un nombre |

Dans ta copie : pourquoi les premières valeurs de $v$ sont-elles si petites ?

### Ex R5.8 — Retrouver le premier terme et la raison à partir de deux termes ✏️ ★ ⏱️ 10 min
**Objectif :** retrouver une suite arithmétique ou géométrique à partir de deux de ses termes.
**Prérequis :** fiche §2 et §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $(u_n)$ est arithmétique, $u_4 = 17$ et $u_{10} = 41$ : sa raison | un nombre entier |
| b | son premier terme $u_0$ | un nombre entier |
| c | $(v_n)$ est géométrique, $v_1 = 12$ et $v_4 = -96$ : sa raison | un nombre entier |
| d | son premier terme $v_0$ | un nombre entier |
| e | $(w_n)$ est géométrique à termes positifs, $w_1 = 50$ et $w_3 = 32$ : sa raison | un nombre |
| f | son premier terme $w_0$ | un nombre |
| g | $(s_n)$ est géométrique, $s_2 = 18$ et $s_4 = 8$ : la liste des valeurs possibles de sa raison | une liste, dans l'ordre que tu veux : des fractions entre guillemets, ou des nombres arrondis à 6 décimales |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex R5.9 — La somme d'une suite géométrique, démontrée par récurrence ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer par récurrence la formule de la somme de termes consécutifs d'une suite géométrique, et l'étendre à un premier terme et un premier rang quelconques.
**Prérequis :** fiche §4 ; R4 §7 (récurrence) · **Parcours :** C, E

Soit $q$ un réel différent de 1. Pour tout entier $n \ge 1$, on note $P(n)$ : « $\displaystyle\sum_{k=0}^{n-1} q^k = \frac{1 - q^n}{1 - q}$ ».
1. Écris $P(1)$ et $P(2)$, et vérifie-les (pour $P(2)$, développe ou factorise $1 - q^2$).
2. Rédige l'initialisation.
3. Rédige l'hérédité : suppose $P(n)$ vraie pour un entier $n \ge 1$ fixé, isole le dernier terme de $\sum_{k=0}^{n} q^k$, utilise $P(n)$ et réduis au même dénominateur pour obtenir $P(n + 1)$.
4. Rédige la conclusion.
5. Déduis-en, sans nouvelle récurrence, la somme $\sum_{k=0}^{n-1} u_0\,q^k$ (linéarité), puis la somme $\sum_{k=m}^{m+n-1} q^k$ de $n$ termes à partir du rang $m$ (mets $q^m$ en facteur).
6. Pourquoi la démonstration ne marche-t-elle pas pour $q = 1$ ? Que vaut alors la somme, et pourquoi ?

### Ex R5.10 — La somme d'une suite arithmétique : l'astuce de Gauss ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer la formule « nombre de termes × (premier + dernier) / 2 » en appariant les termes, et l'appliquer.
**Prérequis :** fiche §2 et §4 · **Parcours :** C

On raconte que le jeune Gauss, à qui l'on avait demandé d'additionner les entiers de 1 à 100, a écrit la somme deux fois, une fois à l'endroit et une fois à l'envers :
$$\begin{array}{rcccccccc} S & = & 1 & + & 2 & + & \dots & + & 100 \\ S & = & 100 & + & 99 & + & \dots & + & 1 \end{array}$$
1. Additionne les deux lignes **colonne par colonne** : que vaut chaque colonne, et combien y a-t-il de colonnes ? Déduis-en $2S$, puis $S$.
2. Soit $(u_n)$ une suite arithmétique de raison $r$, et $S = u_0 + u_1 + \dots + u_{n-1}$. Montre que, pour tout $k$ de 0 à $n - 1$, $u_k + u_{n-1-k} = u_0 + u_{n-1}$ (écris les deux termes avec $u_0$ et $r$).
3. En écrivant $S$ à l'endroit et à l'envers, déduis-en $S = n \times \frac{u_0 + u_{n-1}}{2}$.
4. Applique la formule à la somme des $n$ premiers nombres impairs, $1 + 3 + 5 + \dots + (2n - 1)$. Vérifie ton résultat pour $n = 1, 2, 3, 4$.
5. La fiche démontre la même formule autrement (§4). Laquelle des deux démonstrations préfères-tu, et pourquoi ? Une phrase suffit.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R5.11 — Actualiser : ce que vaut aujourd'hui une somme versée chaque année (une somme géométrique) 🔗 ★★ ⏱️ 20 min
**Objectif :** calculer la valeur actuelle d'une suite de versements avec une somme géométrique, et faire le lien avec le facteur d'actualisation du RL.
**Prérequis :** fiche §3 à §5 ; R5.4 · **Parcours :** C, E

Tu gagnes un prix : 1 000 € versés à la fin de chaque année pendant 8 ans (le premier versement dans un an). L'argent placé rapporte 4 % par an, à intérêts composés. La **valeur actuelle** d'une somme reçue dans $k$ années est la somme qu'il faudrait placer aujourd'hui pour l'obtenir dans $k$ années (fiche §3). Arrondis les montants au centime.

| | Question | Réponse attendue |
|---|---|---|
| a | la valeur actuelle du premier versement | un nombre (2 décimales) |
| b | les valeurs actuelles des versements successifs forment une suite géométrique : sa raison | un nombre (4 décimales) |
| c | la valeur actuelle des 8 versements | un nombre (2 décimales) |
| d | on te propose plutôt 7 000 € tout de suite : que choisis-tu, si tu ne regardes que la valeur actuelle ? 1 pour les 7 000 € tout de suite, 2 pour les 8 versements | 1 ou 2 |
| e | la valeur actuelle des 8 versements si l'argent rapporte 6 % par an | un nombre (2 décimales) |

Dans ta copie : en apprentissage par renforcement (workbookIA, ch. 26), une récompense reçue dans $k$ pas est multipliée par $\gamma^k$, avec $0 \le \gamma < 1$. À quoi correspond $\gamma$ dans cet exercice ? Que veut dire, pour un agent, un $\gamma$ proche de 0, et un $\gamma$ proche de 1 ?

### Ex R5.12 — Une moyenne mobile qui glisse : la mettre à jour sans tout recalculer 🔗 ★ ⏱️ 15 min
**Objectif :** écrire une moyenne mobile comme une suite définie par récurrence, et compter ce que cette mise à jour fait gagner.
**Prérequis :** fiche §6 et §1 · **Parcours :** C, E

On lisse les valeurs $x_1, \dots, x_8 = 12, 18, 15, 9, 21, 24, 6, 15$ par une moyenne mobile sur une fenêtre de 4 valeurs : $m_t = \frac{x_{t-3} + x_{t-2} + x_{t-1} + x_t}{4}$ pour $t \ge 4$.

**c)** Quelle formule donne $m_{t+1} - m_t$ ?
1. $\frac{x_{t+1} - x_{t-3}}{4}$
2. $\frac{x_{t+1} - x_t}{4}$
3. $\frac{x_{t+1}}{4} - m_t$
4. $\frac{x_{t+1} - x_{t-4}}{4}$

| | Question | Réponse attendue |
|---|---|---|
| a | $m_4$ | un nombre |
| b | $m_5$, calculé directement | un nombre |
| c | le numéro de la bonne formule ci-dessus | un nombre entier |
| d | $m_6$, calculé à partir de $m_5$ avec cette formule | un nombre |
| e | pour une fenêtre de 100 valeurs, la liste `[direct, mise à jour]` du nombre minimal d'additions et de soustractions qu'il faut pour obtenir une nouvelle moyenne : en additionnant les 100 valeurs, puis avec la formule de c) (sans compter la division) | une liste de 2 entiers |
| f | $m_8$ | un nombre |

Dans ta copie : quand des mesures arrivent une par une (un capteur, les pas d'un entraînement suivis en direct), pourquoi cette mise à jour est-elle utile ? Que faut-il quand même garder en mémoire ?

### Ex R5.13 — Expliquer pourquoi une somme infinie peut être finie 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement comment une infinité de termes peut avoir une somme finie, et quand ce n'est pas le cas.
**Prérequis :** fiche §5 · **Parcours :** C, E

Une amie te dit : « Si on additionne une infinité de nombres positifs, on obtient forcément l'infini, non ? »

Réponds-lui **en huit lignes au plus**. Ta réponse doit contenir : un exemple de somme infinie de nombres positifs qui a une valeur finie, l'idée de somme partielle et de ce dont elle se rapproche, ce qui distingue une somme géométrique finie d'une somme infinie qui grandit sans fin, et un piège (des termes qui tendent vers 0 ne suffisent pas).

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r5_suites/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R5.14 | Terme d'une suite arithmétique et somme géométrique · `arithmetic_term`, `geometric_sum` | 🔨 | ★ | 15 | C, E |
| R5.15 | Itérer une récurrence · `iterate` | 🔨 | ★ | 15 | C, E |
| R5.16 | Moyennes mobile et exponentielle · `moving_average`, `exponential_moving_average` | 🔨 | ★★ | 25 | C, E |
| R5.17 | Les mêmes calculs avec NumPy : `np.cumsum`, `np.cumprod`, `np.convolve` | 📦 | ★ | 15 | C |
| R5.18 | Prédire : vers quoi tend u(n + 1) = 0,75 u(n) + 2 ? | 🔮 | ★ | 10 | C, E |
| R5.19 | Lisser un signal bruité : l'effet de la fenêtre et de β | 🔬 | ★★ | 20 | C |
| R5.20 | Des suites qui convergent, divergent, oscillent | 🎨 | ★ | 15 | C |
| R5.21 | Chasse à l'erreur : un décalage d'indice dans une somme | 🐛 | ★ | 15 | C, E |
| R5.22 | Une boucle ou une formule ? Mesurer le temps de calcul | 🛠️ | ★ | 15 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
