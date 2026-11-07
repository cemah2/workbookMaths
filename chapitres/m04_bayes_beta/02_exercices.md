# M04 · Bayes, vraisemblance et loi Beta — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m04_bayes_beta/06_mes_reponses.md` (créée par `python tools/start_chapter.py M04`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Pour chaque mise à jour, écris le tableau **hypothèse, a priori, vraisemblance, produit, a posteriori** ; pour une loi Beta, dis toujours ce que comptent $a$ et $b$ (les succès et les échecs de **quoi**). Garde les fractions exactes jusqu'au bout.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M04.Q1 — Les quatre termes de la formule de Bayes 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Un éditeur d'antivirus publie quatre chiffres sur une collection de fichiers : « 3 % des fichiers sont malveillants » ; « l'antivirus lève une alerte sur 98 % des fichiers malveillants » ; « 5 % des fichiers déclenchent une alerte » ; « 59 % des alertes concernent un fichier malveillant ». On note $H$ = « le fichier est malveillant » et $O$ = « alerte ».
1. Écris le premier chiffre avec la notation $P(\ldots)$, et donne son nom dans la formule de Bayes.
2. Même question pour le deuxième.
3. Même question pour le troisième.
4. Même question pour le quatrième.
5. Vérifie que les quatre chiffres sont cohérents entre eux.
6. Vrai ou faux : pour calculer $P(\text{non } H \mid O)$, il faut une autre évidence que pour $P(H \mid O)$.

### M04.Q2 — Mettre à jour deux fois 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Deux hypothèses $H_1$ et $H_2$, d'a priori 0,5 chacune. Une observation $O$ a la vraisemblance 0,6 sous $H_1$ et 0,2 sous $H_2$. Les observations sont indépendantes sachant l'hypothèse.
1. $P(H_1 \mid O)$ ?
2. Après deux observations $O$, $P(H_1 \mid O, O)$ ?
3. Vrai ou faux : pour la deuxième mise à jour, l'a priori de $H_1$ vaut encore 0,5.
4. Après une observation $O$ puis une observation « non $O$ », $P(H_1 \mid O, \text{non } O)$ ?
5. Après $n$ observations $O$, que vaut le rapport $\frac{P(H_1 \mid \ldots)}{P(H_2 \mid \ldots)}$ ?
6. Combien d'observations $O$ faut-il, au minimum, pour que $P(H_1 \mid \ldots)$ dépasse 0,99 ?

### M04.Q3 — La vraisemblance, une fonction du paramètre 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. On observe 4 succès en 10 essais indépendants (dans un ordre donné), de probabilité de succès $\theta$. Écris la vraisemblance $L(\theta)$.
2. Où est son maximum ?
3. Vrai ou faux : $\int_0^1 L(\theta)\,d\theta = 1$.
4. Vrai ou faux : multiplier $L$ par une constante qui ne dépend pas de $\theta$ ne change pas son maximum.
5. Pourquoi dérive-t-on $\ln L$ plutôt que $L$ ?
6. On observe 0 succès en 6 essais. Où est le maximum de vraisemblance ? Est-ce une estimation raisonnable ?

### M04.Q4 — La loi Beta : forme et paramètres 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Quelle loi est $\mathrm{Beta}(1, 1)$ ?
2. Que vaut la moyenne de $\mathrm{Beta}(3, 7)$ ?
3. Laquelle est la plus concentrée autour de sa moyenne : $\mathrm{Beta}(3, 7)$ ou $\mathrm{Beta}(30, 70)$ ?
4. Quelle forme a la densité de $\mathrm{Beta}(0{,}5 ;\ 0{,}5)$ ?
5. Que vaut $\Gamma(5)$ ?
6. Vrai ou faux : la densité d'une loi Beta ne dépasse jamais 1.

### M04.Q5 — Conjuguée, Laplace, MAP 🧠 ★ ⏱️ 4 min
*Fiche §5 et §6 · parcours C, E*

1. A priori $\mathrm{Beta}(2, 3)$ sur une probabilité de succès ; on observe 4 succès et 1 échec. Quel est l'a posteriori ?
2. Que vaut son MAP ?
3. Que vaut sa moyenne ?
4. Avec le lissage de Laplace, 0 succès en 8 essais : quelle probabilité donne-t-on au succès suivant ?
5. Vrai ou faux : avec l'a priori uniforme $\mathrm{Beta}(1, 1)$, le MAP est la fréquence observée.
6. Combien de pseudo-observations « vaut » l'a priori $\mathrm{Beta}(6, 14)$ ?

### M04.Q6 — Logarithmes et underflow 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

1. Que vaut $\ln\big(0{,}1^{400}\big)$ ?
2. Que vaut `0.1 ** 400` en Python ? Pourquoi ?
3. Pourquoi soustrait-on le maximum des $\ell_j$ avant de prendre les exponentielles, dans log-sum-exp ?
4. Que vaut $\ln\big(e^0 + e^0\big)$ ?
5. Que vaut $\ln\big(e^{-500} + e^{-500}\big)$ ?
6. Vrai ou faux : $\ln(ab) = \ln a + \ln b$ permet de remplacer un produit de vraisemblances par une somme.

### M04.Q7 — Fréquentiste ou bayésien ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

Pour les phrases 1 à 4, dis si elle se place du point de vue fréquentiste, bayésien, ou si les deux peuvent l'écrire ; puis réponds aux questions 5 et 6.
1. « Sachant ces données, le taux de clic a 95 % de chances d'être entre 4 % et 7 %. »
2. « Si l'on répétait l'étude, 95 % des intervalles calculés ainsi contiendraient le vrai taux de clic. »
3. « Avant de voir les données, je pense que le taux de clic est proche de 5 %, à 2 points près. »
4. « La probabilité qu'un dé équilibré donne 6 vaut $\frac{1}{6}$. »
5. Vrai ou faux : avec beaucoup de données et un a priori peu informatif, les deux points de vue donnent des estimations très proches.
6. Pourquoi l'échantillonnage de Thompson affiche-t-il encore, de temps en temps, le titre qui semble le moins bon ?

<a id="rappels"></a>

## 🔁 Rappels

### M04.R1 — Probabilités conditionnelles (M03) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

Sur 200 utilisateurs d'une application, 120 sont sur Android et 80 sur iOS ; 30 utilisateurs Android et 24 utilisateurs iOS ont fait un achat.
1. $P(\text{achat})$ ?
2. $P(\text{achat} \mid \text{iOS})$ ?
3. $P(\text{iOS} \mid \text{achat})$ ?
4. $P(\text{iOS} \cap \text{achat})$ ?
5. L'achat est-il indépendant du système ?

### M04.R2 — Intégrales et densités (M02a) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

1. $\int_0^1 x^2\,dx$ ?
2. $\int_0^1 x(1 - x)\,dx$ ?
3. Pour quelle constante $c$ la fonction $c\,x(1 - x)$ est-elle une densité sur $[0, 1]$ ?
4. Que vaut l'espérance de cette densité ?
5. $\int_0^1 (1 - x)^4\,dx$ ?

### M04.R3 — Loi binomiale (M02b) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C*

$X$ suit la loi binomiale $\mathcal{B}(10 ;\ 0{,}3)$.
1. $P(X = 0)$ ?
2. $\mathbb{E}[X]$ ?
3. $\mathbb{V}(X)$ ?
4. $P(X = 2)$ ?
5. On observe $X = 2$ et l'on cherche le $p$ qui rend cette observation la plus probable. Pourquoi le coefficient $\binom{10}{2}$ ne compte-t-il pas ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"7/9"` ;
- une liste entre crochets, comme `[-1.5, 2.5]` ; vrai ou faux par `True` ou `False` ; une lettre entre guillemets, comme `"B"`.

### Ex M04.1 — Bayes avec deux hypothèses : un capteur de fuite d'eau ✏️ ★ ⏱️ 20 min
**Objectif :** calculer une évidence et un a posteriori à deux hypothèses, en probabilités et en effectifs, et voir l'effet de l'a priori.
**Prérequis :** fiche §1 ; M03 §2 et §3 · **Parcours :** C, E

Un capteur surveille une cave. Une nuit donnée, une fuite d'eau se produit avec la probabilité 0,01. S'il y a une fuite, le capteur sonne avec la probabilité 0,95 ; sans fuite, il sonne quand même avec la probabilité 0,03 (de la condensation).

| | Question | Réponse attendue |
|---|---|---|
| a | l'évidence $P(\text{sonne})$ | un nombre (4 décimales) |
| b | $P(\text{fuite} \mid \text{sonne})$ | un nombre (3 décimales) |
| c | $P(\text{fuite} \mid \text{ne sonne pas})$, multipliée par 10 000 | un nombre (1 décimale) |
| d | sur 1 000 nuits, le nombre moyen de nuits où le capteur sonne | un nombre (1 décimale) |
| e | sur ces 1 000 nuits, le nombre moyen de fausses alertes (il sonne, sans fuite) | un nombre (1 décimale) |
| f | un second capteur identique, indépendant du premier sachant qu'il y a une fuite ou non, sonne aussi : $P(\text{fuite} \mid \text{les deux sonnent})$ | un nombre (3 décimales) |
| g | avec un seul capteur, la plus grande valeur de $P(\text{sonne} \mid \text{pas de fuite})$ (au lieu de 0,03) pour laquelle $P(\text{fuite} \mid \text{sonne}) \ge 0{,}5$ | une fraction irréductible |
| h | dans une vieille maison où la probabilité d'une fuite par nuit est 0,05 : $P(\text{fuite} \mid \text{sonne})$, avec un seul capteur | un nombre (3 décimales) |

Dans ta copie : refais b) avec les effectifs de d) et e). Pourquoi b) est-il si petit alors que le capteur détecte 95 % des fuites ? Que vaut-il mieux améliorer : la détection (0,95) ou les fausses alertes (0,03) ?

### Ex M04.2 — Trois hypothèses et un tableau de mise à jour ✏️ ★★ ⏱️ 20 min
**Objectif :** mettre à jour trois hypothèses observation après observation, calculer l'évidence d'une suite et la probabilité de l'observation suivante.
**Prérequis :** fiche §2 · **Parcours :** C, E

Une salle de sport classe ses abonnés en trois types : **réguliers** (R, a priori 0,3), **occasionnels** (O, 0,5) et **inactifs** (I, 0,2). Une semaine donnée, un régulier vient à la salle avec la probabilité 0,9, un occasionnel 0,4, un inactif 0,05. Pour un abonné dont on ignore le type, on observe trois semaines : il vient (V) la première, ne vient pas (N) la deuxième, vient (V) la troisième. Les semaines sont indépendantes sachant le type. Donne les listes dans l'ordre R, O, I.

| | Question | Réponse attendue |
|---|---|---|
| a | l'évidence de la première observation, $P(V)$ | un nombre (2 décimales) |
| b | l'a posteriori après V | une liste de 3 nombres (4 décimales) |
| c | l'a posteriori après V puis N | une liste de 3 nombres (4 décimales) |
| d | l'a posteriori après V, N, V | une liste de 3 nombres (4 décimales) |
| e | l'évidence de la suite entière, $P(V, N, V)$ | un nombre (4 décimales) |
| f | le type le plus probable après les trois semaines | une lettre entre guillemets (R, O ou I) |
| g | la probabilité que l'abonné vienne la quatrième semaine, sachant V, N, V | un nombre (3 décimales) |
| h | après V, N, V, le nombre minimal de semaines **consécutives** sans venir pour que le type I devienne le plus probable | un entier |

Dans ta copie : écris le tableau de chaque mise à jour. Vérifie e) de deux façons : en multipliant les évidences des trois étapes, et par la formule « d'un coup » de la fiche. Pourquoi la semaine N fait-elle tant baisser le type R ?

### Ex M04.3 — La vraisemblance d'un taux de clic ✏️ ★ ⏱️ 20 min
**Objectif :** écrire une vraisemblance, comparer des valeurs du paramètre par un rapport, et calculer une log-vraisemblance.
**Prérequis :** fiche §3 ; M02b (loi binomiale) · **Parcours :** C, E

Une publicité a été affichée 20 fois et cliquée 3 fois. On note $\theta$ son taux de clic, et l'on suppose les affichages indépendants. Pour la suite observée (3 clics, 17 non-clics, dans un ordre donné), $L(\theta) = \theta^3(1 - \theta)^{17}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le maximum de vraisemblance $\hat{\theta}$ | un nombre (2 décimales) |
| b | le rapport $\frac{L(0{,}15)}{L(0{,}10)}$ | un nombre (3 décimales) |
| c | la log-vraisemblance $\ell(0{,}15) = \ln L(0{,}15)$ | un nombre (3 décimales) |
| d | la probabilité d'obtenir 3 clics sur 20 (dans n'importe quel ordre) si $\theta = 0{,}15$ | un nombre (4 décimales) |
| e | le rapport $\frac{L(0{,}30)}{L(0{,}15)}$ | un nombre (3 décimales) |
| f | le maximum de vraisemblance après un 21ᵉ affichage sans clic | un nombre (4 décimales) |
| g | le lendemain, 2 clics sur 30 affichages ; le maximum de vraisemblance sur les deux jours, en supposant le même $\theta$ | un nombre (2 décimales) |
| h | deux suites de 20 affichages ont chacune 3 clics, à des places différentes : ont-elles la même vraisemblance ? | `True` ou `False` |

Dans ta copie : trace l'allure de $L$ sur $[0 ; 0{,}5]$. Que veut dire b) en une phrase ? Pourquoi la probabilité de d) est-elle plus grande que $L(0{,}15)$, et pourquoi cela ne change-t-il pas le maximum ?

### Ex M04.4 — Maximiser une vraisemblance : dériver son logarithme ✏️ ★★ ⏱️ 20 min
**Objectif :** trouver un maximum de vraisemblance en dérivant une log-vraisemblance, pour une loi exponentielle, puis pour une loi de Poisson et une loi de Bernoulli.
**Prérequis :** fiche §3 ; R7 ; M02b (lois exponentielle et de Poisson) · **Parcours :** C, E

Un serveur reçoit des requêtes ; on a mesuré 5 durées (en secondes) entre deux requêtes consécutives : $2{,}0$ ; $0{,}5$ ; $1{,}5$ ; $3{,}0$ ; $1{,}0$. On les suppose indépendantes, de loi exponentielle de paramètre $\lambda > 0$ (densité $\lambda e^{-\lambda x}$), si bien que $L(\lambda) = \lambda^5 e^{-8\lambda}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la log-vraisemblance $\ell(1)$ | un nombre (2 décimales) |
| b | la dérivée $\ell'(1)$ | un nombre (2 décimales) |
| c | le maximum de vraisemblance $\hat{\lambda}$ | un nombre (3 décimales) |
| d | $\ell(\hat{\lambda})$ | un nombre (3 décimales) |
| e | la dérivée seconde $\ell''(\hat{\lambda})$ | un nombre (2 décimales) |
| f | la durée moyenne entre deux requêtes estimée par $\frac{1}{\hat{\lambda}}$ | un nombre (2 décimales) |

Un autre serveur compte ses erreurs par jour pendant 5 jours : $2, 0, 3, 1, 4$, supposées indépendantes, de loi de Poisson de paramètre $\mu$ ($P(X = x) = e^{-\mu}\frac{\mu^x}{x!}$).

| | Question | Réponse attendue |
|---|---|---|
| g | le maximum de vraisemblance $\hat{\mu}$ | un nombre (2 décimales) |
| h | sans rapport avec les serveurs : pour une loi de Bernoulli, le maximum de vraisemblance après 7 succès sur 25 essais | un nombre (2 décimales) |

Dans ta copie : écris $\ell(\lambda)$ et $\ell'(\lambda)$ pour des durées $x_1, \ldots, x_n$ quelconques, et la formule générale de $\hat{\lambda}$. Fais de même pour $\hat{\mu}$ (la loi de Poisson). Pourquoi le signe de $\ell''(\lambda)$, pour **tout** $\lambda > 0$ (pas seulement en $\hat{\lambda}$), prouve-t-il que c) est le maximum ?

### Ex M04.5 — La loi Beta : normalisation, moyenne, mode, variance ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la constante, la densité, la moyenne, le mode, la variance et une probabilité d'une loi Beta à paramètres entiers.
**Prérequis :** fiche §4 ; M02a (intégrale, intégration par parties) · **Parcours :** C, E

On étudie la loi $\mathrm{Beta}(2, 5)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la constante $B(2, 5)$ | une fraction irréductible |
| b | la densité en $\theta = 0{,}2$ | un nombre (4 décimales) |
| c | la moyenne | une fraction irréductible |
| d | le mode | un nombre (2 décimales) |
| e | la variance | une fraction irréductible |
| f | $P(\Theta \le 0{,}5)$ | un nombre (4 décimales) |
| g | la constante $c$ pour laquelle $c\,\theta^2(1 - \theta)$ est une densité sur $[0, 1]$ | un entier |
| h | les paramètres `[a, b]` de la loi Beta de moyenne 0,25 telle que $a + b = 8$ | une liste de 2 entiers |

Dans ta copie : retrouve a) en calculant l'intégrale $\int_0^1 \theta(1 - \theta)^4\,d\theta$ par parties (ou par le changement de variable $u = 1 - \theta$). Pour f), calcule $\int_0^{0{,}5}$ de la densité de la même façon.

### Ex M04.6 — Conjugaison : de Beta(a, b) à Beta(a + k, b + n − k) ✏️ ★ ⏱️ 20 min
**Objectif :** mettre à jour une loi Beta par conjugaison, lire la moyenne a posteriori comme une moyenne pondérée, et mesurer le poids de l'a priori.
**Prérequis :** fiche §4 et §5 · **Parcours :** C, E

Une boutique en ligne veut estimer le taux de retour $\theta$ d'un nouveau produit (la proportion des ventes renvoyées). D'après ses produits voisins, elle choisit l'a priori $\mathrm{Beta}(3, 27)$. Sur les 50 premières ventes, 8 sont renvoyées.

| | Question | Réponse attendue |
|---|---|---|
| a | les paramètres de l'a posteriori, `[a, b]` | une liste de 2 entiers |
| b | la moyenne a posteriori | un nombre (4 décimales) |
| c | le poids des données dans cette moyenne, $\frac{n}{a + b + n}$, où $a$ et $b$ sont les paramètres de l'a priori de départ | un nombre (3 décimales) |
| d | 50 ventes plus tard, 6 nouveaux retours : les paramètres de l'a posteriori, `[a, b]` | une liste de 2 entiers |
| e | la moyenne de cet a posteriori | un nombre (4 décimales) |
| f | l'écart-type de l'a posteriori de a) | un nombre (4 décimales) |
| g | avec l'a priori $\mathrm{Beta}(1{,}5 ;\ 13{,}5)$, de même moyenne mais deux fois moins sûr, la moyenne a posteriori après les 50 premières ventes | un nombre (4 décimales) |
| h | avec l'a priori de départ, le nombre total de ventes $n$ pour lequel le poids des données $\frac{n}{a + b + n}$ atteint 0,9 | un entier |

Dans ta copie : écris la moyenne a posteriori de b) comme une moyenne pondérée de la moyenne a priori et de la fréquence observée. Compare b) et g) : que change un a priori moins sûr ?

### Ex M04.7 — Lissage de Laplace : la prédictive avec Beta(1, 1) ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des probabilités prédictives avec l'a priori uniforme, pour un essai puis pour plusieurs.
**Prérequis :** fiche §5 · **Parcours :** C

Un site de vente vient d'ajouter un article. On note $\theta$ la probabilité qu'une visite de sa page se termine par un achat, avec l'a priori uniforme $\mathrm{Beta}(1, 1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | après 4 visites sans achat, la probabilité que la visite suivante donne un achat | une fraction irréductible |
| b | après 5 visites et 5 achats, la probabilité que la visite suivante donne un achat | une fraction irréductible |
| c | avec $\alpha = 0{,}5$ ajouté à chaque comptage au lieu de 1, la probabilité de a) | un nombre (2 décimales) |
| d | les visiteurs choisissent une couleur parmi 3 ; comptages 6, 3 et 0 : la probabilité lissée (Laplace) de la troisième couleur | une fraction irréductible |
| e | après 4 visites sans achat, la probabilité que les **2** visites suivantes donnent chacune un achat | une fraction irréductible |
| f | après 4 visites sans achat, la probabilité qu'au moins une des 2 visites suivantes donne un achat | une fraction irréductible |

Dans ta copie : que donnerait le maximum de vraisemblance en a) et en b) ? Pourquoi est-il dangereux d'annoncer ces valeurs ? Pour e), pourquoi le résultat n'est-il pas le carré de a) ?

### Ex M04.8 — MAP, maximum de vraisemblance et moyenne a posteriori ✏️ ★★ ⏱️ 20 min
**Objectif :** comparer trois estimations d'une proportion et voir l'effet de l'a priori quand les données s'accumulent.
**Prérequis :** fiche §5 et §6 · **Parcours :** C, E

Une équipe teste une nouvelle fonctionnalité auprès de 10 utilisateurs ; 9 l'adoptent. On note $\theta$ le taux d'adoption ; l'a priori de l'équipe est $\mathrm{Beta}(5, 5)$ (« autour de 50 %, sans plus »).

| | Question | Réponse attendue |
|---|---|---|
| a | le maximum de vraisemblance | un nombre (2 décimales) |
| b | le MAP avec l'a priori $\mathrm{Beta}(5, 5)$ | un nombre (4 décimales) |
| c | la moyenne a posteriori avec l'a priori $\mathrm{Beta}(5, 5)$ | un nombre (2 décimales) |
| d | le MAP avec l'a priori uniforme $\mathrm{Beta}(1, 1)$ | un nombre (2 décimales) |
| e | la moyenne a posteriori avec l'a priori uniforme | un nombre (4 décimales) |
| f | avec l'a priori $\mathrm{Beta}(5, 5)$, la plus petite des trois estimations (maximum de vraisemblance, MAP, moyenne a posteriori) | un nombre (2 décimales) |
| g | avec l'a priori $\mathrm{Beta}(2, 2)$, le MAP après 0 adoption sur 3 utilisateurs | un nombre (2 décimales) |
| h | pour un **autre** groupe d'utilisateurs, à partir du seul a priori $\mathrm{Beta}(5, 5)$ (sans les 10 premiers), le nombre minimal d'utilisateurs qui adoptent **tous** pour que le MAP dépasse strictement 0,8 | un entier |

Dans ta copie : range les trois estimations de b), c) et a), et explique l'ordre. Que deviennent-elles si 900 utilisateurs sur 1 000 adoptent ?

### Ex M04.9 — Un intervalle de crédibilité d'une loi Beta ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer à la main les quantiles et un intervalle de crédibilité de lois Beta dont la fonction de répartition est simple.
**Prérequis :** fiche §4 et §6 ; M02a §7 (quantiles) · **Parcours :** C

Un nouveau procédé de fabrication a tourné 8 fois sans défaut. On note $\theta$ sa probabilité de défaut, avec l'a priori uniforme. La fonction de répartition de $\mathrm{Beta}(1, b)$ vaut $F(x) = 1 - (1 - x)^b$, et celle de $\mathrm{Beta}(a, 1)$, $F(x) = x^a$.

| | Question | Réponse attendue |
|---|---|---|
| a | les paramètres de l'a posteriori, `[a, b]` | une liste de 2 entiers |
| b | $P(\theta \le 0{,}1)$ selon l'a posteriori | un nombre (4 décimales) |
| c | la borne basse de l'intervalle de crédibilité à 95 % à queues égales | un nombre (5 décimales) |
| d | sa borne haute | un nombre (4 décimales) |
| e | la borne $u$ telle que $P(\theta \le u) = 0{,}95$ (une borne supérieure à 95 %) | un nombre (4 décimales) |
| f | la médiane de l'a posteriori | un nombre (4 décimales) |
| g | l'intervalle de crédibilité à 95 % à queues égales de $\mathrm{Beta}(3, 1)$, `[basse, haute]` | une liste de 2 nombres (4 décimales) |

Dans ta copie : vérifie la formule de $F$ pour $\mathrm{Beta}(1, b)$ en intégrant sa densité. Pourquoi l'intervalle de c) et d) est-il si asymétrique autour de la moyenne $\frac{1}{10}$ ? Que dirait le maximum de vraisemblance ?

### Ex M04.10 — Log-probabilités : additionner au lieu de multiplier, normaliser par log-sum-exp ✏️ ★ ⏱️ 20 min
**Objectif :** reconnaître un underflow, calculer en logarithmes et normaliser des log-probabilités par log-sum-exp.
**Prérequis :** fiche §7 ; R6 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\ln\big(0{,}2^{500}\big)$ | un nombre (2 décimales) |
| b | $\log_{10}\big(0{,}2^{500}\big)$ | un nombre (3 décimales) |
| c | `0.2 ** 500` vaut-il exactement 0 en `float64` (le plus petit nombre positif représentable vaut environ $5 \times 10^{-324}$) ? | `True` ou `False` |
| d | $\ln\big(e^{-1000} + e^{-1001} + e^{-1003}\big)$ | un nombre (3 décimales) |
| e | les probabilités obtenues en normalisant $(e^{-1000}, e^{-1001}, e^{-1003})$ | une liste de 3 nombres (4 décimales) |
| f | trois hypothèses d'a priori $(0{,}2 ;\ 0{,}5 ;\ 0{,}3)$ ont pour log-vraisemblances $(-1000 ;\ -1001 ;\ -1003)$ : leurs a posteriori | une liste de 3 nombres (4 décimales) |

Dans ta copie : pour e) et f), écris les étapes : soustraire le maximum, prendre les exponentielles, normaliser. Que donnerait le calcul direct de $e^{-1000}$ en `float64` ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex M04.11 — La conjugaison Beta-binomiale, démontrée ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer que l'a posteriori d'une loi Beta après des essais binomiaux est une loi Beta, et en tirer la loi prédictive.
**Prérequis :** fiche §4 et §5 ; M02b (loi binomiale) · **Parcours :** C

Une proportion $\Theta$ a pour a priori $\mathrm{Beta}(a, b)$. Sachant $\Theta = \theta$, on fait $n \ge 1$ essais indépendants de probabilité de succès $\theta$ : le nombre $K$ de succès suit la loi binomiale $\mathcal{B}(n, \theta)$. La formule de Bayes pour une densité s'écrit $f(\theta \mid k) = \frac{P(K = k \mid \theta)\,f(\theta)}{P(K = k)}$, avec $P(K = k) = \int_0^1 P(K = k \mid \theta)\,f(\theta)\,d\theta$.
1. Écris $P(K = k \mid \theta)$ et $f(\theta)$, puis le produit $P(K = k \mid \theta)\,f(\theta)$.
2. Montre que $f(\theta \mid k)$ est proportionnelle à $\theta^{a + k - 1}(1 - \theta)^{b + n - k - 1}$, avec un coefficient qui ne dépend pas de $\theta$.
3. Déduis-en, sans calculer d'intégrale, que l'a posteriori est $\mathrm{Beta}(a + k,\ b + n - k)$. Quel argument fixe la constante ?
4. Calcule $P(K = k)$ et reconnais la loi bêta-binomiale de la fiche (§5) : la loi prédictive, calculée ici avec l'a priori.
5. Montre que la moyenne a posteriori est une moyenne pondérée de la moyenne a priori et de la fréquence $\frac{k}{n}$, et donne les poids.
6. On fait tendre $n$ vers $+\infty$ avec $\frac{k}{n} \to p$, pour $p$ dans $]0, 1[$. Que deviennent la moyenne et la variance a posteriori ? Interprète.
7. Pour aller plus loin : un taux $\Lambda$ a pour a priori la **loi Gamma** de paramètres $\alpha > 0$ et $\beta > 0$, dont la densité sur $]0, +\infty[$ est proportionnelle à $\lambda^{\alpha - 1}e^{-\beta\lambda}$ (ici, $\beta$ n'a rien à voir avec la loi Beta) ; sachant $\Lambda = \lambda$, on observe $x_1, \ldots, x_n$, indépendants de loi de Poisson de paramètre $\lambda$. Montre que l'a posteriori est encore une loi Gamma, et donne ses paramètres.

### Ex M04.12 — Le maximum de vraisemblance d'une loi de Bernoulli est la fréquence ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que la fréquence observée maximise la vraisemblance, cas limites compris, et étudier cet estimateur.
**Prérequis :** fiche §3 ; R7 ; M02c §6 et §7 (biais, variance, erreur type) · **Parcours :** C

$X_1, \ldots, X_n$ sont indépendantes, de loi de Bernoulli de paramètre $\theta \in [0, 1]$ ; on observe $x_1, \ldots, x_n$ dans $\{0, 1\}$, et l'on note $k = \sum_i x_i$.
1. Montre que $L(\theta) = \prod_i \theta^{x_i}(1 - \theta)^{1 - x_i} = \theta^k(1 - \theta)^{n - k}$ (avec la convention $0^0 = 1$, pour $\theta = 0$ ou 1). Que faut-il retenir des données pour connaître $L$ ?
2. On suppose $0 < k < n$. Calcule $\ell'(\theta)$ sur $]0, 1[$, résous $\ell'(\theta) = 0$, et démontre que la solution est le maximum de $L$ sur $[0, 1]$ (pense aussi aux bords, où $L$ vaut 0).
3. Traite les cas $k = 0$ et $k = n$ sans dériver $\ell$ : où $L$ est-elle maximale ? Conclus que, dans tous les cas, $\hat{\theta} = \frac{k}{n}$.
4. On voit maintenant $\hat{\theta} = \frac{1}{n}\sum_i X_i$ comme une variable aléatoire. Démontre qu'il est sans biais, et calcule sa variance.
5. Relie le résultat de 4 à l'erreur type d'une proportion de M02c.
6. Avec l'a priori $\mathrm{Beta}(a, b)$, $a > 1$ et $b > 1$, montre que le MAP vaut $\frac{k + a - 1}{n + a + b - 2}$ et qu'il se rapproche de $\hat{\theta}$ quand $n$ grandit, à fréquence $\frac{k}{n}$ fixée.
7. Pour aller plus loin : démontre que le maximum de vraisemblance du paramètre $\mu$ d'une loi de Poisson, pour des observations $x_1, \ldots, x_n$ non toutes nulles, est leur moyenne.

### Ex M04.13 — Le mode de la loi Beta ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule du mode d'une loi Beta, la comparer à la moyenne, et traiter les cas limites.
**Prérequis :** fiche §4 et §6 ; R7 · **Parcours :** C

On note $g(\theta) = (a - 1)\ln\theta + (b - 1)\ln(1 - \theta)$ sur $]0, 1[$, le logarithme de la densité de $\mathrm{Beta}(a, b)$ à une constante près. Convention (celle de la docstring de `map_estimate_beta`) : quand la densité est monotone sur $]0, 1[$, son mode est le bord vers lequel elle croît, même si elle y tend vers l'infini.
1. On suppose $a > 1$ et $b > 1$. Calcule $g'(\theta)$, trouve son unique zéro, et démontre que c'est le maximum de la densité. Que vaut la densité aux bords 0 et 1 ?
2. Toujours pour $a > 1$ et $b > 1$, démontre que le mode est plus petit que la moyenne si et seulement si $a < b$. Que se passe-t-il pour $a = b$ ?
3. Cas $a = 1 < b$ : écris la densité et montre qu'elle est décroissante. Quel est son mode ?
4. Cas $a < 1 < b$ : que vaut la limite de la densité en $0^+$ ? Montre qu'elle est décroissante, et conclus.
5. Cas $a < 1$ et $b < 1$ : montre que $g'$ s'annule en un unique point, et que ce point est un **minimum**. Où sont les modes ?
6. Cas $a = b = 1$ : pourquoi n'y a-t-il pas un mode unique ?
7. Applique 1 et 3 à l'a posteriori $\mathrm{Beta}(k + 1,\ n - k + 1)$ (a priori uniforme, $k$ succès sur $n \ge 1$ essais) : retrouve le maximum de vraisemblance, cas $k = 0$ et $k = n$ compris (pour $k = n$, utilise la symétrie $\theta \mapsto 1 - \theta$).

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M04.14 — Un test A/B : deux taux de conversion et P(θB > θA) par simulation 🔗 ★★ ⏱️ 20 min
**Objectif :** comparer deux proportions par leurs lois a posteriori, avec une approximation normale puis une simulation, comme le fera le notebook de workbookIA.
**Prérequis :** fiche §5, §6 et §8 ; M02b (loi normale, table de $\Phi$) ; M02c §5 · **Parcours :** C, E

Une boutique compare deux pages de commande. La page A a reçu 300 visites et 30 commandes ; la page B, 300 visites et 45 commandes. Les taux de conversion $\theta_A$ et $\theta_B$ ont chacun l'a priori uniforme.

| | Question | Réponse attendue |
|---|---|---|
| a | les paramètres de l'a posteriori de $\theta_A$, `[a, b]` | une liste de 2 entiers |
| b | la moyenne a posteriori de $\theta_B$ | un nombre (4 décimales) |
| c | l'écart-type a posteriori de $\theta_B$ | un nombre (4 décimales) |
| d | l'écart-type a posteriori de $\theta_A$ | un nombre (4 décimales) |
| e | $P(\theta_B > \theta_A)$, en approchant chaque a posteriori par une loi normale de même moyenne et de même écart-type, les deux étant indépendants (table de $\Phi$ de M02b) | un nombre (2 décimales) |
| f | la même probabilité estimée par la simulation ci-dessous | un nombre (3 décimales) |
| g | dans cette simulation, la moyenne de $\theta_B - \theta_A$ | un nombre (4 décimales) |

La simulation (sa cellule est dans la partie 0 du notebook ; remplace d'abord les `...` par les paramètres des deux a posteriori) :

```python
import numpy as np
a_A, b_A = ..., ...                      # the parameters of the posterior of θA (your answer to a)
a_B, b_B = ..., ...                      # the parameters of the posterior of θB
rng = np.random.default_rng(14)
theta_A = rng.beta(a_A, b_A, 100_000)    # 100 000 draws from the posterior of A, first
theta_B = rng.beta(a_B, b_B, 100_000)    # then 100 000 draws from the posterior of B
print(np.mean(theta_B > theta_A), np.mean(theta_B - theta_A))
```

Dans ta copie : pourquoi la différence de deux lois normales indépendantes est-elle normale, et de quelle variance (M02b, M02c) ? e) et f) diffèrent un peu : de combien une proportion estimée sur 100 000 tirages peut-elle s'écarter de sa vraie valeur (l'erreur type d'une proportion, M02c §7) ? Rédige en une phrase, pour l'équipe produit, ce que dit e) ou f). L'équipe doit-elle passer toutes les visites sur la page B ? Que ferait l'échantillonnage de Thompson ?

### Ex M04.15 — MML §6.3 (relire le théorème de Bayes) et §6.6 : conjugaison et famille exponentielle (lecture guidée) 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais le théorème de Bayes, la définition d'un a priori conjugué et la famille exponentielle, et les relier à la fiche.
**Prérequis :** fiche §1, §5 et §7 · **Parcours :** C

Lis la fin de MML §6.3 (le théorème de Bayes), puis §6.6. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. En §6.3, quels noms le livre donne-t-il aux quatre termes du théorème de Bayes ? Lequel dit-il difficile à calculer, et pourquoi ?
2. Pourquoi, d'après le livre, peut-on souvent travailler avec « a posteriori ∝ vraisemblance × a priori », sans calculer le dénominateur ?
3. En §6.6, comment le livre définit-il un a priori conjugué ? Dans son exemple Beta-binomial, identifie les paramètres de l'a priori, les données et les paramètres de l'a posteriori, et vérifie qu'ils suivent la règle de la fiche (§5).
4. Le livre donne un tableau de lois conjuguées. Cite deux couples (vraisemblance, a priori conjugué) autres que Beta-binomial.
5. Qu'est-ce qu'une statistique suffisante, d'après le livre ? Laquelle pour $n$ essais de Bernoulli ?
6. Écris la forme de la famille exponentielle du livre. Pour la loi de Bernoulli, identifie le paramètre naturel, la statistique et la fonction de normalisation, et compare avec la fiche (§7).
7. Note trois mots ou tournures en anglais de ces sections qui étaient nouveaux pour toi, avec leur traduction.

### Ex M04.16 — MML §8.3 : maximum de vraisemblance et MAP (lecture guidée) 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais l'estimation par maximum de vraisemblance et par MAP, et la relier à la régularisation.
**Prérequis :** fiche §3 et §6 · **Parcours :** C

Lis MML §8.3. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Comment le livre définit-il l'estimation par maximum de vraisemblance ? Pourquoi minimise-t-il **moins** le logarithme de la vraisemblance ?
2. Dans l'exemple où les observations ont un bruit gaussien, à quelle loss bien connue cette minimisation se ramène-t-elle ?
3. Comment le livre définit-il l'estimation MAP ? Quel terme ajoute-t-elle à moins la log-vraisemblance ?
4. Avec un a priori gaussien sur les paramètres, à quoi ressemble ce terme ? Comment l'appelle-t-on en ML ?
5. Applique à l'imprimante de la fiche : écris moins le logarithme de l'a posteriori pour l'a priori $\mathrm{Beta}(2, 8)$ et 2 échecs sur 12, à une constante près, puis trouve son minimum en dérivant. Retrouves-tu 0,15 ?
6. Que dit le livre du risque du maximum de vraisemblance quand on a peu de données ? En quoi le MAP aide-t-il ?
7. Note trois mots ou tournures en anglais de cette section qui étaient nouveaux pour toi, avec leur traduction.

### Ex M04.17 — Expliquer la conjugaison avec des pseudo-observations 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement ce que fait une mise à jour Beta, et ce que représentent ses paramètres.
**Prérequis :** fiche §5 · **Parcours :** C, E

Un collègue voit dans ton code `rate = (clicks + 2) / (views + 10)` et s'étonne : « Pourquoi ajouter 2 clics et 10 affichages qui n'ont jamais eu lieu ? C'est truquer les données. »

Réponds-lui **en huit lignes au plus**, sans formule compliquée. Ta réponse doit dire quel a priori correspond à ce calcul et ce que représentent ces 2 et ces 10, ce qui se passe quand les vraies données s'accumulent, et dans quel cas ces nombres imaginaires sont utiles.

<a id="entretien"></a>

## 💼 Entretien

### M04.E1 — Qu'est-ce que le lissage de Laplace, et pourquoi l'utiliser ? 💼 ★ ⏱️ 10 min
*Fiche §5 · parcours C, E*

« Qu'est-ce que le lissage de Laplace ? Pourquoi l'utilise-t-on, et que se passerait-il sans lui ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit donner la formule (pour deux issues et pour $K$ catégories), dire le problème qu'il évite avec un exemple, son interprétation bayésienne, et une limite ou une variante. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m04_bayes_beta/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M04.18 | Densité et moments de la loi Beta (avec `math.lgamma`) · `beta_pdf, beta_moments` | 🔨 | ★ | 20 | C, E |
| M04.19 | Mise à jour conjuguée et loi prédictive des prochains essais · `conjugate_beta_update, posterior_predictive` | 🔨 | ★★ | 25 | C, E |
| M04.20 | Le MAP d'une loi Beta, cas limites compris · `map_estimate_beta` | 🔨 | ★★ | 15 | C |
| M04.21 | La fonction Beta avec `scipy.special` : `beta`, `betaln` et l'underflow | 📦 | ★ | 15 | C |
| M04.22 | Prédire : le MAP avec Beta(1, 1) après trois échecs | 🔮 | ★ | 10 | C |
| M04.23 | Le posterior se resserre : la largeur de l'intervalle en 1/√n | 🔬 | ★★ | 20 | C |
| M04.24 | Prior, vraisemblance et posterior sur une même figure | 🎨 | ★ | 20 | C, E |
| M04.25 | Chasse à l'erreur : évidence oubliée, mise à jour à l'envers, mode et moyenne | 🐛 | ★ | 15 | C |
| M04.26 | Un calcul stable : comparer des vraisemblances en logarithmes (`math.lgamma`) | 🛠️ | ★ | 15 | C |
| M04.27 | Défi : traduire l'avis d'un expert en une loi Beta (moyenne, écart-type, intervalle) | 🏆 | ★★★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
