# M08 · Tests statistiques — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m08_tests/06_mes_reponses.md` (créée par `python tools/start_chapter.py M08`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Garde les valeurs exactes (les fractions, $\sqrt{3}$) jusqu'au bout, et n'arrondis qu'à la fin. Pour les quantiles de la loi normale, prends $z_{0{,}95} \approx 1{,}645$, $z_{0{,}975} \approx 1{,}960$ et $z_{0{,}80} \approx 0{,}842$, ou la table de M02b ; pour la loi de Student, la table de la fiche (§5).

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M08.Q1 — Ce qu'une p-valeur est, et ce qu'elle n'est pas 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. La p-valeur d'un test est : (A) la probabilité que $H_0$ soit vraie, sachant les données ; (B) la probabilité, si $H_0$ est vraie, d'observer des données au moins aussi extrêmes ; (C) la probabilité que $H_1$ soit vraie ; (D) la taille de l'effet.
2. Vrai ou faux : $p = 0{,}03$ veut dire qu'il y a 3 % de chances que $H_0$ soit vraie.
3. Vrai ou faux : $p = 0{,}4$ prouve que $H_0$ est vraie.
4. Vrai ou faux : si $H_0$ est vraie et que la statistique est continue, la probabilité d'obtenir $p \le 0{,}05$ vaut 0,05.
5. Deux études mesurent le même effet, l'une sur 50 personnes, l'autre sur 5 000. Laquelle donnera en général la plus petite p-valeur ?
6. Vrai ou faux : une p-valeur de $10^{-6}$ prouve que l'effet est important en pratique.

### M08.Q2 — Unilatéral ou bilatéral ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C*

1. On veut montrer qu'un nouveau réglage est **plus rapide** que l'ancien : test unilatéral ou bilatéral ?
2. On veut savoir si une pièce est **truquée**, dans un sens ou dans l'autre : test unilatéral ou bilatéral ?
3. Sous $H_0 : p = \frac{1}{2}$, avec 20 essais, la p-valeur unilatérale $P(K \ge 15)$ vaut environ 0,0207. Que vaut la p-valeur bilatérale ?
4. Vrai ou faux : la p-valeur bilatérale d'un test binomial est toujours le double de la p-valeur unilatérale.
5. Une équipe choisit le test unilatéral dans le sens que les données viennent de montrer. Qu'est-ce qui ne va pas ?
6. Vrai ou faux : pour les mêmes données, la p-valeur unilatérale dans le sens observé est au plus égale à la p-valeur bilatérale.

### M08.Q3 — Permuter quoi, et sous quelle hypothèse ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Sous quelle hypothèse nulle a-t-on le droit de rebattre la répartition des mesures entre deux groupes ?
2. Combien y a-t-il de façons de répartir 7 valeurs en un groupe de 3 et un groupe de 4 ?
3. Avec $B = 999$ permutations tirées au hasard, dont $C = 12$ sont au moins aussi extrêmes que l'observation, quelle p-valeur annonce-t-on ?
4. Vrai ou faux : le test par permutation suppose que les mesures suivent une loi normale.
5. Chaque serveur est mesuré avant et après une mise à jour. Que permute-t-on ?
6. Pourquoi n'annonce-t-on jamais une p-valeur nulle après un test par permutation tiré au hasard ?

### M08.Q4 — Erreurs de type I et II, puissance : associer 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Une alarme incendie sonne alors qu'il n'y a pas de feu. Erreur de type I ou de type II ?
2. Une étude ne détecte pas un effet qui existe pourtant. Erreur de type I ou de type II ?
3. Quelle erreur le seuil $\alpha$ contrôle-t-il ?
4. Exprime la puissance d'un test en fonction de $\beta$.
5. À seuil $\alpha$ fixé, que devient la puissance quand le nombre d'observations augmente ?
6. Vrai ou faux : à nombre d'observations fixé, abaisser $\alpha$ augmente $\beta$.

### M08.Q5 — Comparaisons multiples : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. On fait 100 tests au seuil de 5 %, et toutes les hypothèses nulles sont vraies. Combien de faux positifs attend-on en moyenne ?
2. Vrai ou faux : la correction de Bonferroni suppose que les tests sont indépendants.
3. Quel seuil Bonferroni donne-t-il à chacun de 25 tests, pour $\alpha = 0{,}05$ ?
4. Quelle est la p-valeur ajustée de Bonferroni d'un test de p-valeur 0,012, parmi 5 tests ?
5. Vrai ou faux : la correction de Bonferroni augmente la puissance de chaque test.
6. Vrai ou faux : tester 25 indicateurs de santé et ne publier que le plus significatif est une comparaison multiple.

### M08.Q6 — AIC, BIC, facteur de Bayes : qui pénalise quoi ? 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

1. Écris l'AIC et le BIC d'un modèle à $k$ paramètres, de log-vraisemblance maximale $\ln L$, sur $n$ observations.
2. Pour $n = 1\,000$, lequel des deux pénalise le plus chaque paramètre ?
3. Vrai ou faux : on préfère le modèle de plus grand AIC.
4. Le facteur de Bayes $\mathrm{BF}_{12}$ vaut 5, et les deux modèles avaient la même probabilité a priori. Quelle est la probabilité a posteriori de $M_1$ (si ce sont les deux seuls modèles en lice) ?
5. Vrai ou faux : ajouter un paramètre à un modèle (qui contient l'ancien) ne peut pas faire baisser sa vraisemblance maximale.
6. Pourquoi l'évidence d'un modèle très souple peut-elle être plus petite que celle d'un modèle simple, même s'il colle mieux aux données ?

<a id="rappels"></a>

## 🔁 Rappels

### M08.R1 — La loi binomiale (M02b) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

$K$ suit la loi binomiale $\mathcal{B}(5 ;\ 0{,}4)$.
1. $P(K = 2)$ ?
2. $\mathbb{E}[K]$ ?
3. $\mathbb{V}(K)$ ?
4. $P(K \ge 1)$ ?
5. Quelles conditions font qu'un nombre de succès suit une loi binomiale ?

### M08.R2 — L'intervalle de confiance d'une moyenne (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

36 mesures ont une moyenne $\bar{x} = 18{,}5$ et un écart-type $s = 4{,}2$. Utilise l'approximation normale ($z = 1{,}96$ à 95 %, $z = 1{,}645$ à 90 %).
1. L'erreur type de la moyenne ?
2. La demi-largeur de l'intervalle à 95 % ?
3. L'intervalle à 95 % ?
4. La demi-largeur de l'intervalle à 90 % (2 décimales) ?
5. Combien de mesures faudrait-il pour une demi-largeur de 0,5 à 95 %, si $s$ reste voisin de 4,2 ?

### M08.R3 — Vraisemblance et log-vraisemblance (M04) 🔁 ★ ⏱️ 5 min
*Fiche §7 · parcours C*

Huit essais indépendants de même probabilité de succès $p$ donnent 3 succès.
1. Écris la vraisemblance $L(p)$ (sans le coefficient binomial, qui ne dépend pas de $p$).
2. Écris la log-vraisemblance $\ln L(p)$.
3. La valeur de $p$ qui la maximise ?
4. La log-vraisemblance maximale (4 décimales) ?
5. De combien la log-vraisemblance est-elle plus basse en $p = \frac{1}{2}$ (calcule à partir des valeurs non arrondies) ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"7/9"` ;
- une liste entre crochets, comme `[-1.5, 2.5, 0]` (deux bornes, une liste de valeurs) ; vrai ou faux par `True` ou `False`.

### Ex M08.1 — Un test binomial à la main : un algorithme de compression est-il plus rapide sur douze fichiers ? ✏️ ★ ⏱️ 20 min
**Objectif :** poser un test, calculer à la main une p-valeur binomiale exacte, unilatérale et bilatérale, et décider.
**Prérequis :** fiche §1 et §2 ; R8 (coefficients binomiaux) · **Parcours :** C, E

On compare un nouvel algorithme de compression à l'ancien sur 12 fichiers. Le nouveau est le plus rapide sur 10 fichiers, l'ancien sur 2 (aucune égalité). On pose $H_0$ : sur chaque fichier, chacun des deux algorithmes a une chance sur deux d'être le plus rapide, indépendamment des autres fichiers. On note $K$ le nombre de fichiers où le nouveau gagne.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(K = 10)$ sous $H_0$ | une fraction irréductible |
| b | la p-valeur unilatérale, pour $H_1$ : « le nouveau gagne plus souvent » | une fraction irréductible |
| c | la p-valeur bilatérale | une fraction irréductible |
| d | rejette-t-on $H_0$ au seuil de 5 %, en bilatéral ? | `True` ou `False` |
| e | rejette-t-on $H_0$ au seuil de 1 %, en bilatéral ? | `True` ou `False` |
| f | le plus petit nombre $k$ de fichiers gagnés pour lequel la p-valeur unilatérale est au plus 0,05 | un entier |
| g | la p-valeur unilatérale donnée par l'approximation normale, $1 - \Phi(z)$ avec $z = \frac{10 - 6}{\sqrt{3}}$ | un nombre (3 décimales) |

Dans ta copie : écris $H_0$ et $H_1$ en une phrase chacune. Pourquoi la p-valeur bilatérale est-elle ici exactement le double de l'unilatérale ? Que vaut l'approximation normale à côté de la valeur exacte ? Si un treizième fichier avait donné une égalité, qu'en aurais-tu fait ?

### Ex M08.2 — Un test par permutation exhaustif : deux groupes de trois mesures, vingt répartitions ✏️ ★★ ⏱️ 25 min
**Objectif :** construire à la main la loi nulle exacte d'un test par permutation, en déduire une p-valeur, et voir les limites des petits groupes.
**Prérequis :** fiche §3 ; R8 (combinaisons) · **Parcours :** C, E

Un service répond en 12, 15 et 14 ms avec une nouvelle configuration du cache (groupe A), et en 18, 21 et 17 ms avec l'ancienne (groupe B). La statistique est $t = \bar{x}_A - \bar{x}_B$. On pose $H_0$ : les six temps viennent de la même loi ; $H_1$ (unilatérale) : la nouvelle configuration est plus rapide ($t$ petit).

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de façons de répartir les six temps en deux groupes de trois | un entier |
| b | la statistique observée $t$ | un nombre |
| c | la p-valeur exacte unilatérale | une fraction irréductible |
| d | la p-valeur exacte bilatérale (on compte les $|t_{\text{perm}}| \ge |t|$) | une fraction irréductible |
| e | vrai ou faux : avec deux groupes de trois mesures toutes différentes, un test bilatéral par permutation peut rejeter $H_0$ au seuil de 5 % | `True` ou `False` |
| f | le nombre de façons de répartir huit valeurs en deux groupes de quatre | un entier |
| g | avec $B = 999$ permutations tirées au hasard et $C = 0$ tirage au moins aussi extrême, la p-valeur annoncée | un nombre |

Dans ta copie : montre que $t = \frac{2S_A - 97}{3}$, où $S_A$ est la somme des trois temps du groupe A, puis liste les 20 valeurs possibles de $S_A$. Pourquoi l'observation est-elle la plus extrême possible ? Pourquoi la p-valeur bilatérale ne peut-elle pas descendre sous celle de d), quelles que soient les mesures ?

### Ex M08.3 — Erreur de type I, erreur de type II et puissance d'un test binomial ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer le risque de type I et la puissance d'une règle de décision, et voir le compromis entre les deux.
**Prérequis :** fiche §2 et §4 · **Parcours :** C, E

Une dégustatrice affirme reconnaître un thé de son producteur parmi deux tasses. On lui présente 14 paires de tasses ; $K$ est le nombre de bonnes réponses. $H_0$ : elle répond au hasard ($p = \frac{1}{2}$) ; on envisage l'alternative $p = 0{,}8$. La règle de décision est : « rejeter $H_0$ si $K \ge c$ ».

| | Question | Réponse attendue |
|---|---|---|
| a | le risque de type I de la règle $K \ge 11$ | une fraction irréductible |
| b | la puissance de la règle $K \ge 11$ contre $p = 0{,}8$ | un nombre (3 décimales) |
| c | le risque de type II $\beta$ de cette règle, contre $p = 0{,}8$ | un nombre (3 décimales) |
| d | le risque de type I de la règle $K \ge 10$ | une fraction irréductible |
| e | la puissance de la règle $K \ge 10$ contre $p = 0{,}8$ | un nombre (3 décimales) |
| f | la plus petite valeur critique $c$ dont le risque de type I est au plus 0,05 | un entier |

Dans ta copie : que gagne-t-on et que perd-on en passant de $K \ge 11$ à $K \ge 10$ ? Pourquoi ne peut-on pas obtenir un risque de type I d'exactement 0,05 ? Comment augmenter la puissance sans augmenter le risque de type I ?

### Ex M08.4 — Combien d'observations pour une puissance de 80 % ? (approximation normale) ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la puissance d'un test sur une moyenne et la taille d'échantillon qui atteint une puissance voulue.
**Prérequis :** fiche §4 ; M02b (quantiles de la loi normale) · **Parcours :** C

Le temps de démarrage d'un service a un écart-type connu $\sigma = 8$ ms. Après une optimisation, on veut détecter une **baisse** de la moyenne de $\delta = 2$ ms, avec un test unilatéral au seuil $\alpha = 0{,}05$ et une puissance de 80 %. On utilise la formule de la fiche (§4).

| | Question | Réponse attendue |
|---|---|---|
| a | le quantile $z_{1-\alpha}$ | un nombre (3 décimales) |
| b | le quantile $z_{1-\beta}$ pour une puissance de 80 % | un nombre (3 décimales) |
| c | le nombre minimal de mesures | un entier |
| d | le nombre minimal de mesures pour un test **bilatéral** au même seuil, avec la même puissance | un entier |
| e | le nombre minimal de mesures pour détecter une baisse de 1 ms (test unilatéral, puissance 80 %) | un entier |
| f | la puissance du test unilatéral avec seulement 36 mesures, pour $\delta = 2$ ms | un nombre (2 décimales) |

Dans ta copie : pourquoi le nombre de mesures est-il multiplié par 4 quand l'effet à détecter est divisé par 2 ? Que conclurais-tu d'un test non significatif fait avec 36 mesures ?

### Ex M08.5 — L'intervalle d'une proportion : Wald contre Wilson, avec peu de succès ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer les intervalles de Wald et de Wilson d'une proportion petite, et voir où Wald échoue.
**Prérequis :** fiche §5 · **Parcours :** C, E

Un détecteur de pannes s'est trompé 3 fois sur 50 cas. On cherche un intervalle à 95 % ($z \approx 1{,}96$) pour sa proportion d'erreurs.

| | Question | Réponse attendue |
|---|---|---|
| a | la proportion observée $\hat{p}$ | un nombre |
| b | la borne basse de l'intervalle de Wald, avant de la ramener dans $[0, 1]$ | un nombre (4 décimales) |
| c | l'intervalle de Wald, ramené dans $[0, 1]$ | une liste de 2 nombres (4 décimales) |
| d | l'intervalle de Wilson | une liste de 2 nombres (4 décimales) |
| e | le centre de l'intervalle de Wilson | un nombre (4 décimales) |
| f | sur une autre série de cas, le détecteur ne s'est jamais trompé en 60 cas : la borne haute de l'intervalle de Wilson | un nombre (4 décimales) |

Dans ta copie : que donnerait l'intervalle de Wald pour f) ? Pourquoi est-ce absurde ? Compare la borne haute de f) à $\frac{3}{n}$, une règle empirique pour zéro erreur.

### Ex M08.6 — L'intervalle de Student d'une différence appariée : un serveur avant et après une mise à jour ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer l'intervalle de Student d'une différence moyenne sur des mesures appariées, et mesurer ce qu'apporte l'appariement.
**Prérequis :** fiche §5 ; M02c (écart-type, $\mathrm{ddof}$) · **Parcours :** C, E

Le temps de réponse médian (en ms) de six routes d'une application est mesuré avant et après une mise à jour du serveur :

| route | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| avant | 52 | 47 | 61 | 55 | 49 | 58 |
| après | 48 | 46 | 55 | 54 | 45 | 53 |

On note $d_i$ = avant − après.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne $\bar{d}$ des différences | un nombre |
| b | l'écart-type $s_d$ des différences, avec $\mathrm{ddof} = 1$ | un nombre (4 décimales) |
| c | l'erreur type $\frac{s_d}{\sqrt{6}}$ | un nombre (3 décimales) |
| d | le quantile de Student utilisé pour un intervalle à 95 % | un nombre (3 décimales) |
| e | l'intervalle à 95 % de la différence moyenne | une liste de 2 nombres (2 décimales) |
| f | l'erreur type si l'on oubliait l'appariement, $\sqrt{\frac{s_{\text{avant}}^2}{6} + \frac{s_{\text{après}}^2}{6}}$ | un nombre (2 décimales) |
| g | vrai ou faux : 0 est dans l'intervalle de e) | `True` ou `False` |
| h | la p-valeur exacte unilatérale du test par permutation apparié : sous $H_0$, chaque différence garde sa valeur absolue mais prend un signe au hasard (fiche §3) ; on compare la moyenne des différences à celle observée | une fraction irréductible |

Dans ta copie : pourquoi l'erreur type de f) est-elle plus de trois fois plus grande que celle de c) ? Que dirait-on de la mise à jour si l'on avait oublié l'appariement ? Combien de combinaisons de signes y a-t-il en h), et pourquoi aucune p-valeur plus petite n'est-elle possible avec six paires ?

### Ex M08.7 — Vingt tests au seuil de 5 % : les faux positifs attendus, puis Bonferroni ✏️ ★ ⏱️ 15 min
**Objectif :** chiffrer le risque des comparaisons multiples, puis appliquer la correction de Bonferroni.
**Prérequis :** fiche §6 · **Parcours :** C, E

On teste 20 features, une par une, pour savoir si chacune est liée à une cible ; chaque test est au seuil de 5 %. On suppose d'abord qu'aucune feature n'est liée à la cible, et que les tests sont indépendants.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre moyen de faux positifs | un nombre |
| b | la probabilité d'au moins un faux positif | un nombre (4 décimales) |
| c | le seuil de Bonferroni de chaque test, pour un risque de la famille de 5 % | un nombre |
| d | la probabilité d'au moins un faux positif quand chaque test est fait au seuil de c) | un nombre (4 décimales) |

On fait maintenant les 20 tests sur de vraies données. Les trois plus petites p-valeurs sont 0,001, 0,004 et 0,03 ; toutes les autres dépassent 0,1.

| | Question | Réponse attendue |
|---|---|---|
| e | les p-valeurs ajustées de Bonferroni de ces trois tests | une liste de 3 nombres |
| f | le nombre de features déclarées liées à la cible, au risque de la famille de 5 % | un entier |

Dans ta copie : combien de features auraient été déclarées liées sans correction ? Quelle garantie la correction donne-t-elle, et laquelle ne donne-t-elle pas (que dire d'une feature vraiment liée dont la p-valeur vaut 0,004) ?

### Ex M08.8 — L'AIC et le BIC de deux modèles, à partir de leurs log-vraisemblances ✏️ ★ ⏱️ 15 min
**Objectif :** calculer l'AIC et le BIC de deux modèles, et voir qu'ils peuvent ne pas choisir le même.
**Prérequis :** fiche §7 ; R6 (logarithmes) · **Parcours :** C, E

Deux modèles sont ajustés par maximum de vraisemblance sur les mêmes $n = 200$ observations. Le modèle 1 a 3 paramètres et une log-vraisemblance maximale $\ln L_1 = -412{,}6$ ; le modèle 2 a 7 paramètres et $\ln L_2 = -405{,}1$.

| | Question | Réponse attendue |
|---|---|---|
| a | l'AIC du modèle 1 | un nombre |
| b | l'AIC du modèle 2 | un nombre |
| c | le BIC du modèle 1 | un nombre (1 décimale) |
| d | le BIC du modèle 2 | un nombre (1 décimale) |
| e | le modèle choisi par l'AIC | 1 ou 2 |
| f | le modèle choisi par le BIC | 1 ou 2 |
| g | le gain de log-vraisemblance, $\ln L_2 - \ln L_1$, au-delà duquel le BIC préfère le modèle 2 (garde $\ln 200$ avec 4 décimales au moins) | un nombre (3 décimales) |

Dans ta copie : écris la différence des AIC comme un gain d'ajustement moins une pénalité. Pourquoi les deux critères ne sont-ils pas d'accord ici ?

### Ex M08.9 — Un facteur de Bayes entre deux taux de clics ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer un facteur de Bayes entre deux hypothèses simples, puis contre un modèle à paramètre libre, et passer des cotes a priori aux probabilités a posteriori.
**Prérequis :** fiche §7 ; M04 (formule de Bayes, loi Beta) · **Parcours :** C

Une bannière a été affichée 40 fois et a reçu 6 clics. Trois modèles sont en concurrence : $M_A$ : le taux de clics vaut 0,1 ; $M_B$ : il vaut 0,2 ; $M_C$ : il est inconnu, uniforme sur $[0, 1]$. Sous chaque modèle, les affichages sont indépendants.

| | Question | Réponse attendue |
|---|---|---|
| a | l'évidence de $M_A$, $P(6 \text{ clics} \mid M_A)$ | un nombre (3 décimales) |
| b | l'évidence de $M_B$ | un nombre (3 décimales) |
| c | le facteur de Bayes $\mathrm{BF}_{BA}$ | un nombre (2 décimales) |
| d | la probabilité a posteriori de $M_B$, si l'on ne compare que $M_A$ et $M_B$ et que la cote a priori de $M_B$ contre $M_A$ vaut $\frac{1}{3}$ | un nombre (2 décimales) |
| e | l'évidence de $M_C$ (raisonne comme pour la pièce de la fiche, §7) | une fraction irréductible |
| f | le facteur de Bayes $\mathrm{BF}_{AC}$ | un nombre (1 décimale) |

Dans ta copie : où se situe le taux de clics qui maximise la vraisemblance ? Pourquoi $M_C$, qui contient ce taux, a-t-il pourtant une évidence plus petite que $M_A$ et $M_B$ ? Que conclure de c) ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M08.10 — Sous H0, une p-valeur continue suit la loi uniforme ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que, sous $H_0$, la p-valeur d'un test à statistique continue est uniforme sur $[0, 1]$, et voir ce qui change pour une loi discrète.
**Prérequis :** fiche §1 et §4 ; M02b (fonction de répartition, loi uniforme) · **Parcours :** C

Un test rejette $H_0$ pour les grandes valeurs d'une statistique $T$. Sous $H_0$, $T$ a une fonction de répartition $F$ continue et strictement croissante. La p-valeur d'une observation $t$ est $P_{H_0}(T \ge t)$.
1. Montre que la p-valeur, vue comme une variable aléatoire, s'écrit $P = 1 - F(T)$.
2. Montre que $P\big(F(T) \le v\big) = v$ pour tout $v \in [0, 1]$, puis que $P(P \le u) = u$ pour tout $u \in [0, 1]$.
3. Déduis-en que la règle « rejeter $H_0$ quand $P \le \alpha$ » a un risque de type I exactement égal à $\alpha$.
4. Cas discret : $K \sim \mathcal{B}(3, \frac{1}{2})$ et le test unilatéral à droite. Liste les quatre p-valeurs possibles et leurs probabilités sous $H_0$. Que vaut $P(P \le 0{,}2)$ ? Qu'en conclus-tu ?
5. À quoi ressemble l'histogramme de 10 000 p-valeurs calculées sous $H_0$ (statistique continue) ? Et sous une alternative où l'effet existe ?

### Ex M08.11 — L'inégalité de Boole et la garantie de Bonferroni, sans hypothèse d'indépendance ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'inégalité de Boole, en déduire la garantie de Bonferroni, et la comparer au cas indépendant.
**Prérequis :** fiche §6 ; R8 (probabilité d'une réunion) ; R4 (récurrence) · **Parcours :** C, E

1. Montre que $P(A \cup B) \le P(A) + P(B)$ pour deux événements quelconques.
2. Démontre par récurrence que $P(A_1 \cup \cdots \cup A_m) \le P(A_1) + \cdots + P(A_m)$.
3. On fait $m$ tests, chacun au seuil $\frac{\alpha}{m}$ ; $m_0$ des hypothèses nulles sont vraies. Montre que la probabilité de rejeter à tort au moins l'une d'elles est au plus $\alpha$. Où as-tu utilisé l'indépendance des tests ?
4. Quand l'inégalité de Boole est-elle une égalité ?
5. Si les $m$ hypothèses nulles sont vraies, que les tests sont indépendants et que chacun rejette à tort avec la probabilité $\frac{\alpha}{m}$, la probabilité d'au moins un faux positif vaut $1 - \big(1 - \frac{\alpha}{m}\big)^m$. Montre par récurrence que $(1 - x)^m \ge 1 - mx$ pour $x \in [0, 1]$, et retrouve la garantie de 3.
6. Montre que, pour $\alpha < 1$, « $\min(1, m\,p_i) \le \alpha$ » équivaut à « $p_i \le \frac{\alpha}{m}$ » : les p-valeurs ajustées et les seuils divisés prennent les mêmes décisions.

### Ex M08.12 — L'intervalle de Wilson, en inversant le test d'une proportion ∂ ★★★ ⏱️ 25 min
**Objectif :** retrouver la formule de l'intervalle de Wilson en résolvant une inéquation du second degré.
**Prérequis :** fiche §5 ; R3 (second degré, discriminant) · **Parcours :** C

Après $k$ succès en $n$ essais, $\hat{p} = \frac{k}{n}$. L'intervalle de Wilson est l'ensemble des valeurs $p_0 \in [0, 1]$ que le test « $|\hat{p} - p_0| \le z\sqrt{\frac{p_0(1 - p_0)}{n}}$ » accepte.
1. Montre que cette condition équivaut à $(\hat{p} - p_0)^2 \le \frac{z^2}{n}\,p_0(1 - p_0)$.
2. Écris-la sous la forme $a\,p_0^2 + b\,p_0 + c \le 0$, avec $a$, $b$ et $c$ en fonction de $\hat{p}$, $z$ et $n$.
3. Calcule le discriminant, vérifie qu'il est positif ou nul, et déduis-en les deux bornes : retrouve la formule de la fiche.
4. Montre que les deux bornes sont dans $[0, 1]$ (indication : le signe du trinôme en 0 et en 1, et la position de son sommet).
5. Que deviennent les bornes quand $k = 0$ ?
6. Vérifie la formule sur l'exemple de la fiche (2 erreurs sur 25).

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M08.13 — Pont : l'importance d'une feature par permutation, sur un petit tableau 🔗 ★ ⏱️ 15 min
**Objectif :** calculer à la main l'importance par permutation de trois features d'un modèle déjà entraîné.
**Prérequis :** fiche §3 · **Parcours :** C

Un modèle déjà entraîné prédit la classe 1 quand $x_1 + x_2 \ge 8$, et 0 sinon ; il ignore la feature $x_3$, un numéro de ligne. Sur un petit jeu de validation :

| ligne | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $x_1$ | 6 | 2 | 7 | 3 | 5 | 4 |
| $x_2$ | 3 | 4 | 2 | 3 | 1 | 5 |
| $x_3$ | 1 | 2 | 3 | 4 | 5 | 6 |
| $y$ | 1 | 0 | 1 | 0 | 0 | 1 |

Pour « mélanger » une feature, on décale sa colonne d'un cran : chaque ligne reçoit la valeur de la ligne suivante, et la ligne 6 celle de la ligne 1 ; les autres colonnes ne bougent pas. L'importance d'une feature est l'accuracy de départ moins l'accuracy après le mélange de cette feature.

| | Question | Réponse attendue |
|---|---|---|
| a | l'accuracy du modèle sur ce tableau | un nombre |
| b | l'accuracy après le mélange de $x_1$ | une fraction irréductible |
| c | l'importance de $x_1$ | une fraction irréductible |
| d | l'accuracy après le mélange de $x_2$ | une fraction irréductible |
| e | l'importance de $x_2$ | une fraction irréductible |
| f | l'importance de $x_3$ | un nombre |

Dans ta copie : pourquoi mélanger une colonne casse-t-il son lien avec la cible sans changer ses valeurs ? En pratique, on mélange au hasard, plusieurs fois : pourquoi ? Pourquoi calcule-t-on cette importance sur un jeu de validation plutôt que sur les données d'entraînement ?

### Ex M08.14 — MML §8.6 : validation croisée imbriquée, sélection bayésienne de modèle et facteur de Bayes 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la section du livre sur le choix d'un modèle, et relier ses notions à la fiche.
**Prérequis :** fiche §7 ; M04 (évidence) · **Parcours :** C

Lis MML §8.6 en entier. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Au §8.6.1, à quoi sert chacune des deux boucles de la validation croisée imbriquée ? Pourquoi ne peut-on pas annoncer le score qui a servi à choisir le modèle ?
2. Au §8.6.2, sur quoi le livre met-il une loi a priori, en plus des paramètres ? Quelle quantité utilise-t-il pour comparer les modèles, et quels sont ses deux noms anglais ?
3. Le livre relie ce choix au rasoir d'Occam. Explique pourquoi l'évidence pénalise d'elle-même les modèles trop souples, avec l'exemple de la pièce de la fiche (§7).
4. Au §8.6.3, écris la relation entre la cote a priori, le facteur de Bayes et la cote a posteriori. Calcule la cote a posteriori pour un facteur de Bayes de 4 et une cote a priori de $\frac{1}{2}$, puis la probabilité a posteriori correspondante.
5. Le livre signale que l'évidence est souvent difficile à calculer. Quelle opération pose problème ? Pourquoi n'y en avait-il pas pour $M_A$ et $M_B$ de M08.9 ?
6. Note trois mots ou tournures en anglais de cette section, avec leur traduction.

### Ex M08.15 — Expliquer une p-valeur sans dire « la probabilité que H0 soit vraie » 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer ce que mesure une p-valeur, et ce qu'elle ne mesure pas, sans formule.
**Prérequis :** fiche §1 · **Parcours :** C, E

Un responsable produit te demande : « Le test de la nouvelle page donne $p = 0{,}02$. Ça veut dire qu'il y a 98 % de chances qu'elle soit meilleure ? »

Réponds-lui **en huit lignes au plus**, sans formule. Ta réponse doit dire ce que calcule la p-valeur (et sous quelle supposition), pourquoi elle n'est pas la probabilité que la page soit meilleure, et ce qu'elle ne dit pas sur la taille du gain.

<a id="entretien"></a>

## 💼 Entretien

### M08.E1 — « Votre test donne p = 0,03 : que concluez-vous, et que dites-vous à l'équipe produit ? » 💼 ★ ⏱️ 10 min
*Fiche §1 et §4 · parcours C*

« Votre test donne $p = 0{,}03$. Que concluez-vous, et que dites-vous à l'équipe produit ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire ce que signifie $p = 0{,}03$ (et ce qu'il ne signifie pas), la décision au seuil prévu, les questions à poser avant d'y croire (la métrique et la taille d'échantillon fixées à l'avance, sans s'arrêter dès que la p-valeur passe sous 0,05 ; la taille de l'effet et son intervalle), et ce qu'on dit à l'équipe produit. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m08_tests/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M08.16 | Le test binomial exact · `binomial_test` | 🔨 | ★ | 15 | C, E |
| M08.17 | Le test par permutation à deux échantillons · `permutation_test` | 🔨 | ★★ | 25 | C, E |
| M08.18 | Les intervalles de Wilson et de Student · `proportion_ci, paired_difference_ci` | 🔨 | ★ | 20 | C, E |
| M08.19 | Bonferroni, l'AIC et le BIC · `bonferroni, aic_bic` | 🔨 | ★ | 10 | C |
| M08.20 | `scipy.stats.binomtest`, `permutation_test` et `ttest_rel` contre tes fonctions | 📦 | ★ | 15 | C |
| M08.21 | Prédire : sous H0, quelle part de 1 000 p-valeurs tombe sous 0,05 ? | 🔮 | ★ | 10 | C, E |
| M08.22 | La puissance d'un test par permutation, selon l'effet et la taille des groupes | 🔬 | ★★ | 25 | C |
| M08.23 | La loi de la statistique sous H0, et la p-valeur comme une aire | 🎨 | ★ | 15 | C |
| M08.24 | Chasse à l'erreur : une p-valeur nulle, un test unilatéral choisi après coup, Bonferroni à l'envers | 🐛 | ★ | 15 | C |
| M08.25 | Tester un test : un pytest qui vérifie l'uniformité des p-valeurs sous H0 | 🛠️ | ★ | 15 | C |
| M08.26 | Défi : retrouver les trois vraies features parmi cinquante, avec au plus un faux positif | 🏆 | ★★★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
