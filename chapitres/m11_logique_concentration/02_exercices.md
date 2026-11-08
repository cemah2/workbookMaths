# M11 · Logique, induction et inégalités de concentration — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m11_logique_concentration/06_mes_reponses.md` (créée par `python tools/start_chapter.py M11`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, ⚖️, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 ⚖️ 🗣️ Pont, esprit critique et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : une table de vérité range ses lignes dans l'ordre VV, VF, FV, FF (pour trois propositions : VVV, VVF, VFV, VFF, FVV, FVF, FFV, FFF), et les lignes sont numérotées à partir de 1 ; $\bar{X}$ est la moyenne de $n$ variables, $\mu$ son espérance ; une **borne sur une probabilité** est au plus 1 (la borne supérieure de confiance d'UCB, en M11.9, borne une moyenne : elle peut dépasser 1). Les rayons de Hoeffding sont **bilatéraux** sauf mention contraire.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M11.Q1 — Réciproque, contraposée, négation 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

On part de l'énoncé $S$ : « si un entier se termine par 5, alors il est divisible par 5 ».
1. Écris la réciproque de $S$. Est-elle vraie ? Si non, donne un contre-exemple.
2. Écris la contraposée de $S$.
3. Écris la négation de $S$, en une phrase qui commence par « il existe ».
4. Vrai ou faux : « être divisible par 5 est une condition nécessaire pour qu'un entier se termine par 5 ».
5. Vrai ou faux : si une implication est fausse, sa contraposée est fausse aussi.
6. Écris la négation de « pour tout $\varepsilon > 0$, il existe un entier $N$ tel que, pour tout $n \ge N$, $\lvert u_n \rvert < \varepsilon$ ».

### M11.Q2 — Un argument valide peut-il avoir une conclusion fausse ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Vrai ou faux ?
1. Un argument valide peut avoir une conclusion fausse.
2. Un argument valide dont toutes les prémisses sont vraies a une conclusion vraie.
3. Un argument dont la conclusion est vraie est valide.
4. Pour prouver qu'un argument n'est pas valide, une seule ligne de sa table de vérité suffit.
5. « $P \Rightarrow Q$ ; $Q \Rightarrow R$ ; donc $P \Rightarrow R$ » est valide.
6. Si un argument est valide, au moins une ligne de sa table de vérité rend toutes ses prémisses vraies.

### M11.Q3 — Diagrammes de Venn et quantificateurs 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C*

$E = \{1, \ldots, 40\}$ ; $A$ est l'ensemble des multiples de 10 de $E$, $B$ celui des multiples de 5, $C$ celui des multiples de 7.
1. A-t-on $A \subset B$ ?
2. A-t-on $B \subset A$ ? Si non, un contre-exemple.
3. Écris $A \cap C$ en extension (il peut être vide).
4. « Tout multiple de 7 de $E$ est impair » : vrai ou faux ? Justifie par un élément.
5. Vrai ou faux : $\bar{B} \subset \bar{A}$ (les complémentaires dans $E$).
6. Combien d'éléments compte $A \cup C$ ?

### M11.Q4 — Les pièges de l'induction 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Le polynôme $n^2 + n + 41$ donne un nombre premier pour $n = 0, 1, \ldots, 39$. Peut-on en conclure qu'il en donne un pour tout entier $n \ge 0$ ?
2. Vrai ou faux : si un détecteur repère 95 % des cas et ne se trompe que sur 5 % des non-cas, alors 95 % de ses alertes sont de vrais cas.
3. « Dans les entreprises qui ont adopté l'outil X, le chiffre d'affaires a augmenté. » Donne deux explications qui ne font pas de l'outil la cause.
4. Vrai ou faux : un sondage en ligne auquel répondent 10 000 volontaires donne une estimation fiable de l'opinion de toute la population.
5. Vrai ou faux : un raisonnement par récurrence (R4) est une induction au sens du §3.
6. Aucune panne en 300 essais indépendants. Que permet de dire la règle de trois, à 95 %, sur la probabilité de panne ?

### M11.Q5 — Markov ou Tchebychev : quelle borne s'applique ? 🧠 ★ ⏱️ 4 min
*Fiche §4 et §5 · parcours C, E*

1. $X \ge 0$ et $\mathbb{E}[X] = 5$ : une borne sur $P(X \ge 20)$ ?
2. $X$ peut être négative, $\mathbb{E}[X] = 5$ : peut-on appliquer Markov à $X$ pour borner $P(X \ge 20)$ ?
3. $\mathbb{E}[X] = 5$ et $\mathbb{V}(X) = 4$ : une borne sur $P(\lvert X - 5 \rvert \ge 6)$ ?
4. La même $X$ : une borne sur $P(X \ge 11)$ ?
5. Vrai ou faux : à un écart-type ($t = \sigma$), la borne de Tchebychev n'apprend rien.
6. $X \ge 0$, $\mathbb{E}[X] = 5$ et $\mathbb{V}(X) = 4$ : quelle inégalité donne la meilleure borne sur $P(X \ge 20)$, et laquelle ?

### M11.Q6 — Ce que garantit l'inégalité de Hoeffding, et ce qu'elle suppose 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Vrai ou faux : l'inégalité de Hoeffding suppose que les variables suivent une loi normale.
2. Vrai ou faux : elle suppose des variables indépendantes, à valeurs dans un intervalle connu à l'avance.
3. Quand $n$ est multiplié par 4, que devient le rayon de confiance à risque fixé ?
4. Pour garder le même rayon, par combien multiplie-t-on $n$ quand le risque $\delta$ passe de 0,05 à 0,0005 ?
5. Vrai ou faux : parmi 25 modèles, on garde celui qui a la meilleure accuracy sur le jeu de test ; le rayon de Hoeffding de cette accuracy, calculé avec $\delta = 0{,}05$ comme pour un seul modèle, reste valable.
6. Vrai ou faux : on peut appliquer Hoeffding au revenu moyen par client, sans plafond connu des revenus.

### M11.Q7 — Explorer ou exploiter : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

1. Le regret $R_T$ ne peut jamais diminuer quand $T$ augmente.
2. Avec ε fixé et strictement positif, la fréquence à laquelle ε-greedy choisit une option sous-optimale ne tend pas vers 0.
3. Le bonus d'UCB d'une option diminue quand on la choisit plus souvent.
4. L'échantillonnage de Thompson choisit toujours l'option de plus grande moyenne a posteriori.
5. Un regret qui croît comme $\ln T$ veut dire que la proportion de pas mal employés tend vers 0.
6. Sur une partie où l'on a eu de la chance, le regret $R_T$ peut être négatif.

<a id="rappels"></a>

## 🔁 Rappels

### M11.R1 — Implication et contraposée (R4) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. Écris la table de vérité de $P \Rightarrow Q$.
2. Vérifie, avec une table, que $P \Rightarrow Q$ et « (non $P$) ou $Q$ » ont la même colonne.
3. Écris la contraposée de « pour tout réel $x$, si $x > 5$, alors $2x + 1 > 11$ ».
4. Démontre par contraposée : « si $n^2$ est divisible par 3, alors $n$ est divisible par 3 » (un entier non divisible par 3 s'écrit $3k + 1$ ou $3k + 2$).
5. Écris la négation de « pour tout réel $x$, $x^2 + 1 > 2x$ ». Laquelle des deux phrases est vraie ?

### M11.R2 — Espérance et variance (M02b) 🔁 ★ ⏱️ 5 min
*Fiche §4 et §5 · parcours C, E*

1. $T$ suit une loi exponentielle de paramètre $\lambda = 0{,}5$ : son espérance et sa variance ?
2. $X$ suit une loi de Bernoulli de paramètre $p$ : son espérance, sa variance, et la valeur de $p$ qui rend cette variance la plus grande ?
3. Que vaut $\mathbb{V}(aX + b)$ en fonction de $\mathbb{V}(X)$ ?
4. $X_1, \ldots, X_n$ indépendantes, d'espérance $\mu$ et de variance $\sigma^2$ : l'espérance et la variance de leur moyenne $\bar{X}$ ?
5. $S$ suit une loi binomiale de paramètres $n = 40$ et $p = 0{,}3$ : son espérance et sa variance ?

### M11.R3 — La loi Beta a posteriori (M04) 🔁 ★ ⏱️ 5 min
*Fiche §7 · parcours C*

Un nouveau test de détection de fissures est essayé sur des pièces dont on connaît l'état. Sa probabilité de succès $\theta$ reçoit l'a priori uniforme $\mathrm{Beta}(1, 1)$. Sur 11 essais, il réussit 2 fois et échoue 9 fois.
1. La loi a posteriori de $\theta$ ?
2. Sa moyenne ?
3. Sa variance (pour $\mathrm{Beta}(a, b)$, $\frac{ab}{(a + b)^2(a + b + 1)}$) ?
4. Sur 65 nouveaux essais, il réussit 25 fois et échoue 40 fois : en partant de la loi a posteriori de la question 1, la nouvelle loi a posteriori, et sa moyenne ? Pourquoi est-elle plus resserrée ?
5. Comment tirer une valeur au hasard dans la loi a posteriori de la question 1 avec NumPy ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Garde les valeurs exactes pendant les calculs et n'arrondis qu'à la fin. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `0.62`, arrondi comme le demande la question ;
- `True` ou `False` ; une liste entre crochets, comme `[False, True, True, False]` pour une colonne de table de vérité, `[2, 4]` pour des numéros de lignes, `[0.09, 0.18]` pour un intervalle ;
- une ou plusieurs lettres entre guillemets, comme `"AC"`.

### Ex M11.1 — Tables de vérité : modus ponens, modus tollens et l'affirmation du conséquent ✏️ ★ ⏱️ 20 min
**Objectif :** décider de la validité d'un argument par sa table de vérité, et trouver la ligne qui sert de contre-exemple.
**Prérequis :** fiche §1 ; R4 (tables de vérité) · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la colonne de $P \Rightarrow Q$, dans l'ordre des lignes VV, VF, FV, FF | une liste de 4 booléens |
| b | pour « $P \Rightarrow Q$ ; $Q$ ; donc $P$ », les numéros des lignes où les deux prémisses sont vraies | une liste d'entiers, dans l'ordre croissant |
| c | cet argument est-il valide ? | `True` ou `False` |
| d | pour « non $P \Rightarrow Q$ ; non $Q$ ; donc $P$ », les numéros des lignes où les deux prémisses sont vraies | une liste d'entiers, dans l'ordre croissant |
| e | cet argument est-il valide ? | `True` ou `False` |
| f | pour « $P \Rightarrow Q$ ; $Q \Rightarrow R$ ; donc $P \Rightarrow R$ », le nombre de lignes, sur 8, où les deux prémisses sont vraies | un entier |
| g | cet argument est-il valide ? | `True` ou `False` |
| h | pour « $Q \Rightarrow P$ ; non $Q$ ; donc non $P$ », le numéro de la ligne qui est un contre-exemple (lignes toujours rangées $P$ d'abord : VV, VF, FV, FF) | un entier |
| i | « ($P$ et $Q$) $\Rightarrow R$ ; $P$ ; non $R$ ; donc non $Q$ » est-il valide ? | `True` ou `False` |

Dans ta copie : écris les tables complètes. Pour b), invente un exemple de la vie courante qui a cette forme, avec des prémisses vraies et une conclusion fausse. Quelle forme de la fiche reconnais-tu en d) ?

### Ex M11.2 — Nier des phrases quantifiées sur des modèles et des datasets ✏️ ★ ⏱️ 15 min
**Objectif :** évaluer des phrases à deux quantificateurs sur un tableau, écrire leur négation, et voir que l'ordre des quantificateurs compte.
**Prérequis :** fiche §1 ; R4 (quantificateurs) · **Parcours :** C, E

Cinq modèles, A à E, ont été évalués sur trois datasets ; le tableau donne leur accuracy de test.

| modèle | dataset 1 | dataset 2 | dataset 3 |
|---|---|---|---|
| A | 0,91 | 0,84 | 0,88 |
| B | 0,86 | 0,90 | 0,79 |
| C | 0,93 | 0,81 | 0,85 |
| D | 0,78 | 0,92 | 0,90 |
| E | 0,88 | 0,87 | 0,86 |

- $S_1$ : « tout modèle a une accuracy d'au moins 0,80 sur chaque dataset » ;
- $S_2$ : « il existe un modèle qui est le meilleur sur chacun des trois datasets » ;
- $S_3$ : « pour chaque dataset, il existe un modèle d'accuracy au moins 0,90 » ;
- $S_4$ : « il existe un modèle d'accuracy au moins 0,90 sur chacun des trois datasets » ;
- $S_5$ : « il existe un modèle d'accuracy au moins 0,85 sur chacun des trois datasets » ;
- $S_6$ : « il existe un dataset sur lequel tous les modèles ont une accuracy d'au moins 0,84 ».

| | Question | Réponse attendue |
|---|---|---|
| a | $S_1$ est-elle vraie ? | `True` ou `False` |
| b | les modèles qui mettent $S_1$ en défaut | des lettres (dans n'importe quel ordre) |
| c | $S_2$ est-elle vraie ? | `True` ou `False` |
| d | $S_3$ est-elle vraie ? | `True` ou `False` |
| e | $S_4$ est-elle vraie ? | `True` ou `False` |
| f | $S_5$ est-elle vraie ? | `True` ou `False` |
| g | le modèle qui en est le témoin | une lettre |
| h | $S_6$ est-elle vraie ? | `True` ou `False` |

Dans ta copie : écris la négation de $S_1$, de $S_3$ et de $S_6$, avec « pour tout » et « il existe ». Pourquoi d) et e) n'ont-ils pas la même réponse ?

### Ex M11.3 — Des phrases traduites en inclusions d'ensembles, et un contre-exemple ✏️ ★★ ⏱️ 15 min
**Objectif :** traduire des phrases en relations entre ensembles, les décider par le calcul, et compter les contre-exemples.
**Prérequis :** fiche §2 ; R4 (ensembles, cardinal d'une réunion) · **Parcours :** C

$E = \{1, 2, \ldots, 30\}$. Dans $E$ : $A$ est l'ensemble des multiples de 6, $B$ celui des multiples de 3, $P$ celui des nombres premiers et $Q$ celui des multiples de 4.

| | Question | Réponse attendue |
|---|---|---|
| a | les cardinaux $\lvert A \rvert$ et $\lvert B \rvert$ | une liste de 2 entiers |
| b | « tout multiple de 6 de $E$ est multiple de 3 » : $A \subset B$ ? | `True` ou `False` |
| c | le plus petit contre-exemple de la réciproque, « tout multiple de 3 de $E$ est multiple de 6 » | un entier |
| d | le nombre de contre-exemples de cette réciproque | un entier |
| e | l'ensemble $P \cap B$, en extension | une liste d'entiers, dans l'ordre croissant |
| f | « aucun nombre premier de $E$ n'est multiple de 6 » est-elle vraie ? | `True` ou `False` |
| g | le nombre de contre-exemples de « tout multiple de 4 de $E$ est multiple de 6 » | un entier |
| h | le cardinal de $A \cup Q$ | un entier |

Dans ta copie : traduis chaque phrase en ensembles ($\subset$, $\cap$, $\varnothing$). Écris la contraposée de b) en ensembles et en français. Dessine le diagramme de Venn de $A$, $B$ et $P$ et place les éléments de $A$, de $B \setminus A$ et de $P \cap B$.

### Ex M11.4 — Une induction trompeuse par oubli du taux de base, recalculée avec Bayes ✏️ ★★ ⏱️ 15 min
**Objectif :** chiffrer l'erreur d'une induction qui oublie le taux de base, avec Bayes et des effectifs attendus.
**Prérequis :** fiche §3 ; M03 (probabilités totales, Bayes) · **Parcours :** C, E

Une usine fabrique des capteurs, dont 3 % sont défectueux. Un test automatique signale 92 % des capteurs défectueux, et signale à tort 6 % des capteurs bons. Un technicien a lu que le test « détecte 92 % des défauts » et en conclut qu'un capteur signalé est défectueux avec la probabilité 0,92.

| | Question | Réponse attendue |
|---|---|---|
| a | la probabilité qu'un capteur tiré au hasard soit signalé | un nombre (4 décimales) |
| b | la probabilité qu'un capteur signalé soit défectueux | un nombre (4 décimales) |
| c | sur 10 000 capteurs, le nombre attendu de capteurs bons mais signalés | un nombre |
| d | la probabilité qu'un capteur **non** signalé soit défectueux | un nombre (4 décimales) |
| e | on refait le test sur un capteur signalé (le second résultat est indépendant du premier, sachant si le capteur est défectueux ou bon), et il est de nouveau signalé : la probabilité qu'il soit défectueux | un nombre (4 décimales) |
| f | la proportion de capteurs défectueux (au lieu de 0,03) pour laquelle un capteur signalé une fois serait défectueux avec la probabilité $\frac{1}{2}$ | un nombre entre 0 et 1 (4 décimales) |
| g | le technicien ouvre 50 capteurs signalés : le nombre de défectueux qu'il doit s'attendre à y trouver | un nombre (1 décimale) |

Dans ta copie : explique au technicien, en deux phrases et avec les effectifs de c), pourquoi sa conclusion est fausse. Quelle probabilité conditionnelle a-t-il confondue avec laquelle ?

### Ex M11.5 — Markov : la queue d'une durée positive ✏️ ★ ⏱️ 15 min
**Objectif :** appliquer l'inégalité de Markov, mesurer à quel point elle est large, et reconnaître la loi qui l'atteint.
**Prérequis :** fiche §4 ; M02b (loi exponentielle) · **Parcours :** C, E

La durée $T$ (en heures) d'une intervention de maintenance est positive, de moyenne $\mathbb{E}[T] = 1{,}5$.

| | Question | Réponse attendue |
|---|---|---|
| a | la borne de Markov sur $P(T \ge 6)$ | un nombre |
| b | la borne de Markov sur $P(T \ge 1)$ | un nombre |
| c | le plus petit seuil $a$ pour lequel Markov garantit $P(T \ge a) \le 0{,}05$ | un nombre |
| d | si $T$ suit une loi exponentielle de moyenne 1,5 : la vraie valeur de $P(T \ge 6)$ | un nombre (4 décimales) |
| e | combien de fois la borne de a) dépasse la vraie valeur de d) (calculée avec la valeur exacte de d), pas son arrondi) | un nombre (1 décimale) |
| f | une loi de moyenne 1,5, à deux valeurs 0 et 6, atteint exactement la borne de a) : la probabilité qu'elle donne à la valeur 0 | un nombre |
| g | huit interventions ont duré 0,2 ; 0,5 ; 0,9 ; 1,1 ; 1,4 ; 2,0 ; 2,6 et 3,3 heures : la proportion de ces durées au moins égales à 2 | un nombre |
| h | si l'on sait aussi que $\mathbb{E}[T^2] = 4{,}5$, la borne obtenue en appliquant Markov à $T^2$ pour $P(T \ge 6)$ | un nombre |

Dans ta copie : calcule la moyenne des huit durées de g), et compare la proportion de g) à la borne de Markov calculée avec cette moyenne. Pourquoi l'inégalité ne peut-elle jamais être violée par un échantillon de valeurs positives ?

### Ex M11.6 — Tchebychev : combien d'observations pour une moyenne à ± 0,1 ? ✏️ ★★ ⏱️ 20 min
**Objectif :** dimensionner un échantillon avec Tchebychev, en bornant une variance inconnue par l'intervalle des valeurs.
**Prérequis :** fiche §5 · **Parcours :** C, E

Le temps de chargement d'une page, en secondes, est toujours compris entre 0 et 2 (au-delà, la requête est coupée). On veut estimer son espérance $\mu$ par la moyenne $\bar{X}$ de $n$ mesures indépendantes, **à $\pm 0{,}1$ s près**, avec un risque d'au plus 5 % : $P(\lvert \bar{X} - \mu \rvert \ge 0{,}1) \le 0{,}05$.

| | Question | Réponse attendue |
|---|---|---|
| a | la plus grande variance possible d'une variable à valeurs dans $[0, 2]$ | un nombre |
| b | le plus petit $n$ que garantit Tchebychev avec cette variance | un entier |
| c | une étude pilote indique un écart-type $\sigma = 0{,}3$ s (on le suppose exact) : le plus petit $n$ que garantit alors Tchebychev | un entier |
| d | avec $n = 180$ et $\sigma = 0{,}3$, la borne de Tchebychev sur $P(\lvert \bar{X} - \mu \rvert \ge 0{,}05)$ | un nombre |
| e | quel que soit $n$, la borne de Tchebychev sur $P\big(\lvert \bar{X} - \mu \rvert \ge \frac{3\sigma}{\sqrt{n}}\big)$ | un nombre (4 décimales) |
| f | pour une proportion inconnue (des réponses 0 ou 1), la plus grande variance possible d'une réponse | un nombre |
| g | le plus petit $n$ qui garantit, par Tchebychev, une proportion à $\pm 0{,}1$ avec un risque d'au plus 10 % | un entier |
| h | à $t$ fixé, par combien la borne de Tchebychev est-elle divisée quand $n$ est multiplié par 9 ? | un entier |

Dans ta copie : démontre a) (la fiche donne l'idée). Pourquoi la connaissance de $\sigma$ divise-t-elle le $n$ de b) par plus de 10 ?

### Ex M11.7 — Hoeffding : rayon de confiance et taille d'échantillon d'une proportion ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un rayon et un intervalle de confiance de Hoeffding, et la taille d'échantillon qui garantit un rayon.
**Prérequis :** fiche §6 · **Parcours :** C, E

On veut connaître la proportion $p$ des requêtes d'un serveur qui durent plus d'une seconde, à partir de $n$ requêtes tirées au hasard, indépendamment. Chaque requête donne 1 si elle dure plus d'une seconde, 0 sinon.

| | Question | Réponse attendue |
|---|---|---|
| a | pour $n = 1\,000$ et $\delta = 0{,}05$, le rayon de Hoeffding | un nombre (4 décimales) |
| b | sur ces 1 000 requêtes, la proportion observée vaut 0,137 : les deux bornes de l'intervalle de confiance de Hoeffding | une liste de 2 nombres (4 décimales) |
| c | le plus petit $n$ qui garantit un rayon d'au plus 0,03 avec $\delta = 0{,}05$ | un entier |
| d | même question avec $\delta = 0{,}01$ | un entier |
| e | pour $n = 1\,000$, la borne de Hoeffding sur $P(\lvert \bar{X} - p \rvert \ge 0{,}05)$ | un nombre (4 décimales) |
| f | la borne de Tchebychev pour la même probabilité, avec la variance la plus grande possible | un nombre |
| g | pour $n = 4\,000$ et $\delta = 0{,}05$, le rayon de Hoeffding | un nombre (4 décimales) |
| h | pour $n = 1\,000$ et $\delta = 0{,}05$, le rayon **unilatéral** (seulement pour $\bar{X} - p$) | un nombre (4 décimales) |

Dans ta copie : écris la phrase exacte que garantit l'intervalle de b). Compare c) et d) : pourquoi diviser le risque par 5 coûte-t-il si peu ? Compare e) et f).

### Ex M11.8 — Trois bornes pour une même question : Markov, Tchebychev, Hoeffding, et l'approximation normale ✏️ ★★ ⏱️ 20 min
**Objectif :** comparer, sur une même probabilité, les trois bornes du chapitre, l'approximation normale et la valeur exacte.
**Prérequis :** fiche §4 à §6 ; M02b (loi binomiale), M02c (théorème central limite) · **Parcours :** C

On lance 100 fois, indépendamment, une épreuve qui réussit avec la probabilité 0,2 ; $S$ est le nombre de succès (de loi binomiale $\mathcal{B}(100 ;\ 0{,}2)$) et $\bar{X} = \frac{S}{100}$. On s'intéresse à $P(S \ge 30)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la borne de Markov sur $P(S \ge 30)$ | un nombre (4 décimales) |
| b | la borne de Tchebychev (en passant par $P(\lvert S - 20 \rvert \ge 10)$) | un nombre |
| c | la borne de Hoeffding **unilatérale** sur $P(\bar{X} - 0{,}2 \ge 0{,}1)$ | un nombre (4 décimales) |
| d | l'approximation normale de $P(S \ge 30)$, sans correction de continuité | un nombre (4 décimales) |
| e | la valeur exacte de $P(S \ge 30)$ | un nombre (4 décimales) |
| f | parmi a), b) et c), la borne la plus proche de e) | une lettre (a, b ou c) |
| g | la borne de Hoeffding unilatérale sur $P(S \ge 25)$ | un nombre (4 décimales) |
| h | le plus petit nombre d'épreuves $n$ pour lequel la borne de c), avec le même écart 0,1, est au plus 0,01 | un entier |

Dans ta copie : pourquoi Markov est-elle si mauvaise ici ? L'approximation normale de d) est-elle une borne ? Pour e), calcule la valeur exacte avec `scipy.stats.binom` ou admets-la, et explique ce qu'elle représente.

### Ex M11.9 — D'où vient le bonus d'UCB : Hoeffding avec un risque qui décroît avec t ✏️ ★★★ ⏱️ 20 min
**Objectif :** retrouver le bonus d'UCB1 comme le rayon unilatéral de Hoeffding pour un risque $t^{-4}$, et en tirer le nombre de choix d'une mauvaise option.
**Prérequis :** fiche §6 et §7 · **Parcours :** C

Les récompenses sont dans $[0, 1]$. Une option a été choisie $N$ fois, de moyenne observée $\hat{\mu}$.

| | Question | Réponse attendue |
|---|---|---|
| a | pour $N = 50$ et un risque $\delta = 0{,}01$, le rayon unilatéral $r$ tel que $P(\mu \ge \hat{\mu} + r) \le \delta$ | un nombre (4 décimales) |
| b | avec le risque $\delta_t = t^{-4}$, le bonus au pas $t = 1\,000$ pour $N = 50$ | un nombre (4 décimales) |
| c | au pas $t = 1\,000$, la borne supérieure UCB1 d'une option 1 de moyenne observée 0,62 après 50 choix | un nombre (4 décimales) |
| d | au même pas, celle d'une option 2 de moyenne observée 0,45 après 8 choix | un nombre (4 décimales) |
| e | l'option que choisit UCB1 entre ces deux-là | un entier |
| f | au pas $t = 10\,000$, le plus petit $N$ pour lequel le bonus d'une option est inférieur à $\frac{\Delta}{2}$, avec $\Delta = 0{,}2$ | un entier |
| g | la somme des risques $\sum_{t=2}^{+\infty} t^{-4}$ | un nombre (4 décimales) |
| h | avec le risque $\delta_t = t^{-2}$ à la place de $t^{-4}$, le bonus au pas $t = 1\,000$ pour $N = 50$ | un nombre (4 décimales) |

Dans ta copie : montre que le rayon unilatéral pour le risque $t^{-4}$ est $\sqrt{\frac{2\ln t}{N}}$. Que dit g) sur la probabilité que la borne supérieure d'une option donnée, après un nombre de choix $N$ donné, soit fausse au moins une fois entre le pas 2 et l'infini ? (La preuve complète d'UCB1 doit aussi faire la borne de l'union sur les valeurs de $N$ et sur les options.) Pourquoi f) donne-t-il un nombre de choix qui croît comme $\ln t$ ?

### Ex M11.10 — ε-greedy : la loi du bras joué et le regret attendu par pas ✏️ ★★ ⏱️ 15 min
**Objectif :** écrire la loi de l'option choisie par ε-greedy, en tirer le regret d'un pas, puis comparer une exploration fixe et une exploration qui décroît.
**Prérequis :** fiche §7 ; R5 (somme harmonique) · **Parcours :** C

Cinq options, numérotées de 1 à 5, ont pour moyennes $\mu = (0{,}55 ;\ 0{,}30 ;\ 0{,}62 ;\ 0{,}48 ;\ 0{,}50)$. Une stratégie ε-greedy, avec $\varepsilon = 0{,}15$, se trompe pour l'instant sur la meilleure : son choix glouton est l'option 1.

| | Question | Réponse attendue |
|---|---|---|
| a | la probabilité qu'elle choisisse l'option 1 au prochain pas | un nombre |
| b | la probabilité qu'elle choisisse l'option 3 | un nombre |
| c | le regret attendu de ce pas, $\mathbb{E}[\mu^\star - \mu_{A_t}]$ | un nombre |
| d | si le choix glouton devient la vraie meilleure option, la valeur de $\varepsilon$ pour laquelle le regret attendu d'un pas vaut 0,01 | un nombre (4 décimales) |
| e | avec $\varepsilon = 0{,}15$ et un choix glouton juste dès le premier pas, le regret attendu après $T = 20\,000$ pas | un nombre |
| f | avec un choix glouton toujours juste et $\varepsilon_t = \frac{1}{t}$ au pas $t$, le regret attendu après 20 000 pas (la somme $\sum_{t=1}^{20\,000} \frac{1}{t}$ vaut environ 10,4807) | un nombre (4 décimales) |
| g | dans la situation de e), le nombre attendu de choix de l'option 2 en 20 000 pas | un nombre |

Dans ta copie : compare e) et f). Pourquoi faire décroître ε trop vite est-il risqué quand le choix glouton peut être faux, comme en a) ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M11.11 — L'inégalité de Markov ∂ ★ ⏱️ 15 min
**Objectif :** démontrer l'inégalité de Markov par une indicatrice, voir qu'elle ne peut pas s'améliorer, et la généraliser.
**Prérequis :** fiche §4 · **Parcours :** C, E

$X$ est une variable aléatoire qui a une espérance, et $a > 0$. On note $\mathbf{1}_{X \ge a}$ la variable qui vaut 1 si $X \ge a$ et 0 sinon.
1. On suppose $X \ge 0$. Montre que $a\,\mathbf{1}_{X \ge a} \le X$, en distinguant les cas $X \ge a$ et $X < a$. Déduis-en $P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$ ; dis quelles propriétés de l'espérance tu utilises.
2. Pour $p \in [0, 1]$, la variable $Y$ vaut $a$ avec la probabilité $p$ et 0 sinon. Montre que $Y$ atteint la borne. Pourquoi, connaissant seulement $\mathbb{E}[X]$, ne peut-on pas faire mieux ?
3. Montre par un exemple que l'hypothèse $X \ge 0$ est nécessaire.
4. Soit $\varphi$ une fonction croissante et positive sur $\mathbb{R}$, avec $\varphi(a) > 0$. Montre que $P(X \ge a) \le \frac{\mathbb{E}[\varphi(X)]}{\varphi(a)}$, pour une $X$ quelconque (si $\mathbb{E}[\varphi(X)]$ est infinie, l'inégalité est vraie mais ne dit rien). Écris ce que cela donne pour $\varphi(x) = e^{\lambda x}$, avec $\lambda > 0$.
5. Pour $X \ge 0$ d'espérance $\mu > 0$ et $k > 0$, montre que $P(X \ge k\mu) \le \frac{1}{k}$.

### Ex M11.12 — Tchebychev à partir de Markov, puis la loi faible des grands nombres ∂ ★★ ⏱️ 20 min
**Objectif :** déduire Tchebychev de Markov, en tirer la loi faible des grands nombres et une taille d'échantillon, et borner la variance d'une variable bornée.
**Prérequis :** fiche §5 ; Ex M11.11 · **Parcours :** C, E

$X$ a une espérance $\mu$ et une variance $\sigma^2$ ; $t > 0$.
1. Démontre $P(\lvert X - \mu \rvert \ge t) \le \frac{\sigma^2}{t^2}$ en appliquant Markov à une variable bien choisie.
2. Montre que la variable qui vaut $\mu - t$ et $\mu + t$ avec la probabilité $\frac{p}{2}$ chacune, et $\mu$ sinon, atteint la borne.
3. $X_1, \ldots, X_n$ sont indépendantes, d'espérance $\mu$ et de variance $\sigma^2$. Montre que $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}$ ; dis où sert l'indépendance (il suffirait que les covariances soient nulles).
4. Déduis-en la loi faible des grands nombres : pour tout $t > 0$, $P(\lvert \bar{X} - \mu \rvert \ge t) \to 0$ quand $n \to +\infty$. Donne un $n$ qui garantit $P(\lvert \bar{X} - \mu \rvert \ge t) \le \delta$.
5. On suppose maintenant $X$ à valeurs dans $[a, b]$. Montre que $\mathbb{E}[(X - c)^2] = \sigma^2 + (\mu - c)^2$ pour tout réel $c$, puis que $\sigma^2 \le \frac{(b - a)^2}{4}$. Quand y a-t-il égalité ?

### Ex M11.13 — Avec ε fixé, le regret attendu d'ε-greedy croît au moins linéairement ∂ ★★ ⏱️ 20 min
**Objectif :** décomposer le regret par option, et démontrer qu'une exploration fixe coûte un regret linéaire alors qu'une exploration en $\frac{1}{t}$ ne coûte qu'un logarithme.
**Prérequis :** fiche §7 ; R5 (somme harmonique) · **Parcours :** C

$K$ options de moyennes $\mu_1, \ldots, \mu_K$ ; $\mu^\star = \max_k \mu_k$, $\Delta_k = \mu^\star - \mu_k$ ; $N_k(T)$ est le nombre de fois que l'option $k$ est choisie en $T$ pas, $A_t$ l'option choisie au pas $t$. À chaque pas, ε-greedy tire, avec la probabilité $\varepsilon$, une option uniformément parmi les $K$ ; sinon, elle prend son choix glouton (quel qu'il soit).
1. Montre que $\mathbb{E}[\mu^\star - \mu_{A_t}] = \sum_{k=1}^{K} \Delta_k\,P(A_t = k)$, puis que $R_T = \sum_{t=1}^{T}\mathbb{E}[\mu^\star - \mu_{A_t}] = \sum_{k=1}^{K} \Delta_k\,\mathbb{E}[N_k(T)]$ (écris $N_k(T)$ comme une somme d'indicatrices).
2. Montre que $P(A_t = k) \ge \frac{\varepsilon}{K}$ pour toute option $k$ et tout pas $t$.
3. Déduis-en $R_T \ge \frac{\varepsilon\,T}{K}\sum_k \Delta_k$. Que veut dire ce résultat, si au moins une option n'est pas la meilleure ?
4. On remplace ε par $\varepsilon_t = \min(1, \frac{c}{t})$, avec $c > 0$. Au pas $t$, le tirage au hasard a lieu avec la probabilité $\varepsilon_t$ et coûte en moyenne $\frac{1}{K}\sum_k \Delta_k$ ; on appelle **part du regret due aux tirages au hasard** la somme $\sum_{t=1}^{T} \varepsilon_t \cdot \frac{1}{K}\sum_k \Delta_k$. Montre qu'elle est au plus $\frac{1}{K}\sum_k \Delta_k \sum_{t=1}^{T} \frac{c}{t}$, puis que $\sum_{t=1}^{T} \frac{1}{t} \le 1 + \ln T$ (compare $\frac{1}{t}$ à $\int_{t-1}^{t} \frac{dx}{x}$ pour $t \ge 2$).
5. Pourquoi ce résultat ne suffit-il pas à garantir un regret logarithmique ? Quelle autre part du regret faudrait-il borner ?

<a id="reflexion"></a>

## 🔗 ⚖️ 🗣️ Pont, esprit critique et explication

### Ex M11.14 — Pont : combien d'exemples de test pour connaître une accuracy à ± 2 points, garanti par Hoeffding ? 🔗 ★ ⏱️ 15 min
**Objectif :** dimensionner un jeu de test et donner le rayon de confiance d'une accuracy, y compris quand on choisit le meilleur de plusieurs modèles.
**Prérequis :** fiche §6 · **Parcours :** C, E

L'accuracy d'un modèle sur un jeu de test est la moyenne des variables « bien classé » (1) ou « mal classé » (0) sur ses exemples ; on suppose les exemples tirés indépendamment des données de service, et le modèle fixé avant de regarder le test.

| | Question | Réponse attendue |
|---|---|---|
| a | le plus petit nombre d'exemples de test qui garantit, par Hoeffding, une accuracy à $\pm 0{,}02$ avec $\delta = 0{,}05$ | un entier |
| b | sur 3 000 exemples, le modèle A obtient 0,874 : le rayon de Hoeffding (bilatéral) de son accuracy, avec $\delta = 0{,}05$ | un nombre (4 décimales) |
| c | une garantie d'un seul côté : le nombre $\ell$ tel que, avec une probabilité au moins 0,95, l'accuracy de A est au moins $\ell$ (rayon **unilatéral** de Hoeffding) | un nombre (4 décimales) |
| d | on a choisi A parmi 20 modèles, comme le meilleur sur ce jeu de test : le rayon bilatéral à utiliser pour garder un risque global de 0,05 | un nombre (4 décimales) |
| e | le rayon à 95 % de l'approximation normale pour l'accuracy de A, avec l'écart-type estimé $\sqrt{\hat{p}(1 - \hat{p})}$ | un nombre (4 décimales) |
| f | le plus petit nombre d'exemples qui garantit un rayon de Hoeffding de 0,015 avec $\delta = 0{,}05$ | un entier |

Dans ta copie : pourquoi le rayon de Hoeffding est-il plus large que celui de e) ? Que protège la correction de d) ? Écris en une phrase la garantie de c), et dis pourquoi elle utilise $\ln(1/\delta)$ et non $\ln(2/\delta)$.

### Ex M11.15 — Corrélation, causalité et induction : trois titres de presse à démonter ⚖️ ★★ ⏱️ 20 min
**Objectif :** reconnaître une induction causale hâtive, proposer d'autres explications, et dire quelle donnée trancherait.
**Prérequis :** fiche §3 · **Parcours :** C

Trois titres (inventés) :
1. « Les villes qui ont le plus de pistes cyclables ont le moins de maladies cardiaques : construisons des pistes, et nous serons en meilleure santé. »
2. « Les élèves qui utilisent l'application de révision X obtiennent de meilleures notes : rendons-la obligatoire. »
3. « Depuis l'installation du nouveau modèle de recommandation en novembre, les ventes ont augmenté de 8 % : le modèle rapporte 8 % de ventes. »

Pour chaque titre, dans ta copie : (a) écris l'induction qu'il fait, sous la forme « on a observé…, donc… » ; (b) donne au moins deux autres explications de l'observation (un facteur de confusion, un sens de causalité inversé, une sélection, une évolution qui aurait eu lieu de toute façon) ; (c) décris l'expérience ou la donnée qui permettrait de trancher. Termine par une règle générale, en une phrase, sur ce qu'il faut pour conclure à une cause.

### Ex M11.16 — Expliquer « l'optimisme face à l'incertitude » à partir d'un intervalle de confiance 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, sans formule, pourquoi choisir l'option dont la borne supérieure est la plus haute fait explorer au début, puis exploiter.
**Prérequis :** fiche §6 et §7 · **Parcours :** C, E

Une amie qui organise des dégustations doit choisir, chaque soir, l'un de trois vins à mettre en avant ; elle note la satisfaction des clients. Explique-lui, **en six lignes au plus** et **sans formule**, la règle « choisis le vin dont la borne supérieure de l'intervalle de confiance est la plus haute ». Ton explication doit contenir les mots « intervalle », « borne supérieure » et « explorer », et dire pourquoi un vin peu goûté est souvent choisi au début, et pourquoi un mauvais vin cesse vite de l'être.

<a id="entretien"></a>

## 💼 Entretien

### M11.E1 — « À quoi sert l'inégalité de Hoeffding en apprentissage, et que suppose-t-elle ? » 💼 ★ ⏱️ 10 min
*Fiche §6 · parcours C*

« À quoi sert l'inégalité de Hoeffding en apprentissage, et que suppose-t-elle ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit donner l'énoncé en mots, un usage concret (la taille d'un jeu de test, le rayon d'une accuracy, ou les bornes de confiance d'UCB), les trois hypothèses et ce qui se passe quand l'une manque, et la comparaison avec l'approximation normale. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m11_logique_concentration/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M11.17 | Les bornes de Markov et de Tchebychev · `markov_bound, chebyshev_bound` | 🔨 | ★ | 15 | C, E |
| M11.18 | La borne et le rayon de Hoeffding · `hoeffding_bound, hoeffding_radius` | 🔨 | ★ | 15 | C, E |
| M11.19 | La queue empirique d'un échantillon · `empirical_tail` | 🔨 | ★ | 10 | C |
| M11.20 | Les vraies queues d'une loi exponentielle et d'une binomiale (`scipy.stats`) contre les bornes | 📦 | ★ | 15 | C |
| M11.21 | Prédire : laquelle des trois bornes est la plus serrée pour n = 100 ? | 🔮 | ★ | 10 | C, E |
| M11.22 | La fréquence des écarts \|x̄ − p\| ≥ t comparée à la borne de Hoeffding, quand n grandit | 🔬 | ★★ | 20 | C |
| M11.23 | La probabilité qu'un tirage d'une loi Beta dépasse celui d'une autre, par simulation | 🔬 | ★★ | 15 | C |
| M11.24 | Les bornes de Markov, de Tchebychev et de Hoeffding contre la vraie queue, en échelle log | 🎨 | ★ | 15 | C |
| M11.25 | Chasse à l'erreur : Markov pour une variable négative, Hoeffding sans bornes, un rayon sans racine | 🐛 | ★ | 15 | C |
| M11.26 | Un test paramétré qui vérifie l'inégalité de Markov sur dix lois | 🛠️ | ★ | 15 | C |
| M11.27 | Défi : la plus petite taille d'échantillon qui garantit une moyenne à ± 0,05 avec 99 %, vérifiée sur une loi défavorable | 🏆 | ★★★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
