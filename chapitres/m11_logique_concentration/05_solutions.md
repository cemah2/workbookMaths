# M11 · Logique, induction et inégalités de concentration — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 ⚖️ 🗣️ Pont, esprit critique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M11.Q1 — Réciproque, contraposée, négation
1. « Si un entier est divisible par 5, alors il se termine par 5. » **Fausse** : 10 est divisible par 5 et se termine par 0.
2. « Si un entier n'est pas divisible par 5, alors il ne se termine pas par 5. »
3. « Il existe un entier qui se termine par 5 et qui n'est pas divisible par 5. » (Elle est fausse, puisque $S$ est vraie.)
4. **Vrai** : $S$ dit « se termine par 5 $\Rightarrow$ divisible par 5 » ; la conclusion d'une implication est une condition nécessaire de son hypothèse.
5. **Vrai** : une implication et sa contraposée ont toujours la même valeur de vérité.
6. « Il existe $\varepsilon > 0$ tel que, pour tout entier $N$, il existe $n \ge N$ avec $\lvert u_n \rvert \ge \varepsilon$. »

### M11.Q2 — Un argument valide peut-il avoir une conclusion fausse ?
1. **Vrai**, si une prémisse est fausse (« si $f$ est continue en 0, elle est dérivable en 0 ; $x \mapsto \lvert x \rvert$ est continue en 0 ; donc elle est dérivable en 0 »).
2. **Vrai** : c'est la définition d'un argument solide.
3. **Faux** : une conclusion vraie peut sortir d'une forme non valide, par chance.
4. **Vrai** : une ligne où toutes les prémisses sont vraies et la conclusion fausse.
5. **Vrai** : les huit lignes le confirment (M11.1 f et g).
6. **Faux** : si les prémisses sont contradictoires (« $P$ ; non $P$ »), aucune ligne ne les rend vraies, et l'argument est valide sans qu'aucune ligne ne compte.

### M11.Q3 — Diagrammes de Venn et quantificateurs
1. **Oui** : $A = \{10, 20, 30, 40\}$, tous multiples de 5.
2. **Non** : 5 est multiple de 5 et n'est pas multiple de 10 (15, 25 et 35 aussi).
3. $A \cap C = \varnothing$ : un élément commun serait multiple de 70, et $E$ s'arrête à 40.
4. **Faux** : 14 est multiple de 7 et pair (28 aussi).
5. **Vrai** : c'est la contraposée de $A \subset B$ (un nombre qui n'est pas multiple de 5 n'est pas multiple de 10).
6. $\lvert A \cup C \rvert = 4 + 5 - 0 = 9$.

### M11.Q4 — Les pièges de l'induction
1. **Non** : $40^2 + 40 + 41 = 1\,681 = 41^2$. Quarante exemples ne démontrent pas un « pour tout ».
2. **Faux** : 95 % est $P(\text{alerte} \mid \text{cas})$ ; la part des alertes vraies, $P(\text{cas} \mid \text{alerte})$, dépend du taux de base, et peut être faible si les cas sont rares.
3. Par exemple : les entreprises déjà en croissance ont les moyens d'adopter de nouveaux outils (un facteur de confusion, ou la causalité dans l'autre sens) ; on ne regarde que les entreprises encore ouvertes (un biais du survivant) ; tout le marché a progressé cette année-là (une évolution qui aurait eu lieu de toute façon).
4. **Faux** : des volontaires ne sont pas tirés au hasard ; le biais de sélection ne diminue pas avec la taille.
5. **Faux** : une récurrence est une déduction (l'hérédité est démontrée pour tout $n$).
6. À 95 %, $p$ est inférieur à environ $\frac{3}{300} = 1\,\%$ ; on ne peut pas dire qu'il est nul.

### M11.Q5 — Markov ou Tchebychev : quelle borne s'applique ?
1. $\frac{5}{20} = 0{,}25$.
2. **Non** : Markov demande une variable positive. (Si l'on savait $X \ge m$, on l'appliquerait à $X - m$.)
3. $\frac{4}{6^2} = \frac{1}{9} \approx 0{,}11$.
4. Au plus $\frac{1}{9}$ : $X \ge 11$ entraîne $\lvert X - 5 \rvert \ge 6$, donc $P(X \ge 11) \le P(\lvert X - 5 \rvert \ge 6)$.
5. **Vrai** : $\frac{\sigma^2}{\sigma^2} = 1$, ce que toute probabilité vérifie déjà.
6. **Tchebychev** : $P(X \ge 20) \le P(\lvert X - 5 \rvert \ge 15) \le \frac{4}{225} \approx 0{,}018$, contre $0{,}25$ pour Markov. Connaître la variance aide.

### M11.Q6 — Ce que garantit l'inégalité de Hoeffding, et ce qu'elle suppose
1. **Faux** : aucune loi n'est supposée, seulement des variables bornées et indépendantes.
2. **Vrai**.
3. Il est **divisé par 2** (le rayon est en $\frac{1}{\sqrt{n}}$).
4. Par $\frac{\ln(2/0{,}0005)}{\ln(2/0{,}05)} = \frac{\ln 4\,000}{\ln 40} \approx 2{,}25$ : diviser le risque par 100 ne coûte qu'un peu plus du double.
5. **Faux** : l'accuracy du meilleur des 25 n'est pas celle d'un modèle fixé d'avance ; il faut la borne de l'union, avec $\frac{0{,}05}{25} = 0{,}002$ pour chacun.
6. **Faux** : Hoeffding demande un intervalle $[a, b]$ connu à l'avance.

### M11.Q7 — Explorer ou exploiter : vrai ou faux
1. **Vrai** : chaque terme $\mathbb{E}[\mu^\star - \mu_{A_t}]$ est positif ou nul.
2. **Vrai** : chaque option est choisie avec une probabilité au moins $\frac{\varepsilon}{K}$ à chaque pas.
3. **Vrai** : le bonus $\sqrt{2\ln t / N}$ diminue quand $N$ augmente (à $t$ donné).
4. **Faux** : Thompson **tire** une valeur dans chaque loi a posteriori ; une option de moyenne plus basse mais incertaine gagne parfois le tirage.
5. **Vrai** : $\frac{\ln T}{T} \to 0$.
6. **Faux** : $R_T = \sum_k \Delta_k\,\mathbb{E}[N_k(T)]$, avec chaque $\Delta_k \ge 0$ : le regret est une espérance qui compare des **moyennes**, pas les récompenses tirées ; la chance change les récompenses, pas le regret.

<a id="rappels"></a>

## 🔁 Rappels

### M11.R1 — Implication et contraposée (R4)
1. $P \Rightarrow Q$ vaut V, F, V, V sur les lignes VV, VF, FV, FF.
2. « (non $P$) ou $Q$ » : F ou V = V ; F ou F = F ; V ou V = V ; V ou F = V. La même colonne.
3. « Pour tout réel $x$, si $2x + 1 \le 11$, alors $x \le 5$. »
4. Contraposée : si $n$ n'est pas divisible par 3, alors $n^2$ ne l'est pas. Si $n = 3k + 1$, $n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$ ; si $n = 3k + 2$, $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$. Dans les deux cas, le reste est 1 : $n^2$ n'est pas divisible par 3.
5. « Il existe un réel $x$ tel que $x^2 + 1 \le 2x$. » Elle est **vraie** ($x = 1$ : $x^2 + 1 - 2x = (x - 1)^2 = 0$), donc la phrase de départ est fausse.

### M11.R2 — Espérance et variance (M02b)
1. $\mathbb{E}[T] = \frac{1}{0{,}5} = 2$ et $\mathbb{V}(T) = \frac{1}{0{,}5^2} = 4$.
2. $p$ et $p(1 - p)$ ; la variance est la plus grande pour $p = \frac{1}{2}$, où elle vaut $\frac{1}{4}$.
3. $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$.
4. $\mathbb{E}[\bar{X}] = \mu$ et $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}$.
5. $\mathbb{E}[S] = 40 \times 0{,}3 = 12$ et $\mathbb{V}(S) = 40 \times 0{,}3 \times 0{,}7 = 8{,}4$.

### M11.R3 — La loi Beta a posteriori (M04)
1. $\mathrm{Beta}(3, 10)$.
2. $\frac{3}{13} \approx 0{,}231$.
3. $\frac{3 \times 10}{13^2 \times 14} = \frac{30}{2\,366} \approx 0{,}0127$.
4. $\mathrm{Beta}(28, 50)$, de moyenne $\frac{28}{78} \approx 0{,}359$ ; sa variance, $\frac{28 \times 50}{78^2 \times 79} \approx 0{,}0029$, est plus de quatre fois plus petite : $a + b$ a grandi, et l'incertitude sur $\theta$ diminue avec les données.
5. `rng = np.random.default_rng(0)`, puis `rng.beta(3, 10)`.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M11.1 — Tables de vérité : modus ponens, modus tollens et l'affirmation du conséquent

**Réponses** : a) `[True, False, True, True]` · b) `[1, 3]` · c) `False` · d) `[2]` · e) `True` · f) `4` · g) `True` · h) `2` · i) `True`.

**Démarche.**
- a) $P \Rightarrow Q$ n'est fausse qu'à la ligne VF.
- b) et c) Les prémisses $P \Rightarrow Q$ et $Q$ sont vraies aux lignes 1 (VV) et 3 (FV). À la ligne 3, la conclusion $P$ est fausse : contre-exemple, l'argument n'est pas valide.
- d) et e) « non $P \Rightarrow Q$ » est fausse seulement à la ligne FF (non $P$ vraie, $Q$ fausse) ; « non $Q$ » demande $Q$ fausse (lignes 2 et 4). Seule la ligne 2 (VF) rend les deux prémisses vraies, et $P$ y est vraie : valide. C'est un *modus tollens* dont l'hypothèse est « non $P$ » : sa conclusion « non (non $P$) » est $P$.
- f) et g) Les deux prémisses sont vraies aux lignes VVV, FVV, FFV et FFF ; dans les quatre, $P \Rightarrow R$ est vraie (V ⇒ V, ou $P$ faux). Valide.
- h) La ligne 2 (VF) : $Q \Rightarrow P$ est vraie ($Q$ fausse), non $Q$ est vraie, et la conclusion non $P$ est fausse ($P$ vraie). C'est la forme « nier l'antécédent » de la fiche, avec les rôles de $P$ et $Q$ échangés : son contre-exemple, la ligne « $P$ faux, $Q$ vrai » de la fiche, devient ici « $Q$ faux, $P$ vrai », la ligne 2.
- i) Les prémisses $P$ et non $R$ forcent $P$ vraie et $R$ fausse ; « ($P$ et $Q$) $\Rightarrow R$ » n'est alors vraie que si « $P$ et $Q$ » est faux, donc si $Q$ est fausse : la conclusion non $Q$ est vraie dans la seule ligne qui reste (VFF). Valide.

Pour la copie : un exemple d'affirmation du conséquent avec des prémisses vraies et une conclusion fausse : « s'il y a un accident sur l'autoroute, j'arrive en retard ; je suis arrivé en retard ; donc il y a eu un accident » (le réveil n'a pas sonné : les deux prémisses sont vraies, la conclusion est fausse).

**Erreurs fréquentes.** Croire que $P \Rightarrow Q$ est fausse quand $P$ est fausse ; oublier une ligne (huit pour trois propositions) ; juger la validité sur une seule ligne où tout est vrai (la ligne 1 de b) ne prouve rien) ; confondre « non $P \Rightarrow Q$ » avec « non ($P \Rightarrow Q$) ».

**Variante.** « $P \Rightarrow Q$ ; $P \Rightarrow$ non $Q$ ; donc non $P$ » est-il valide ? *Réponse* : oui ; les deux prémisses ne sont vraies qu'aux lignes 3 et 4 ($P$ faux), où non $P$ est vraie.

### Ex M11.2 — Nier des phrases quantifiées sur des modèles et des datasets

**Réponses** : a) `False` · b) `"BD"` · c) `False` · d) `True` · e) `False` · f) `True` · g) `"E"` · h) `False`.

**Démarche.**
- a) et b) Deux cases sont sous 0,80 : B sur le dataset 3 (0,79) et D sur le dataset 1 (0,78).
- c) Le meilleur sur le dataset 1 est C (0,93), sur le dataset 2 D (0,92), sur le dataset 3 D (0,90) : aucun modèle n'est le meilleur partout.
- d) Dataset 1 : A (0,91) ou C ; dataset 2 : B (0,90) ou D ; dataset 3 : D (0,90). Chaque colonne a sa case ≥ 0,90.
- e) Il faudrait une **ligne** entière ≥ 0,90 : A a 0,84 ; B 0,79 ; C 0,81 ; D 0,78 ; E 0,88. Aucune.
- f) et g) E a 0,88, 0,87 et 0,86. Les autres ont tous une case sous 0,85 (A : 0,84).
- h) Chaque colonne a une case sous 0,84 : 0,78, 0,81 et 0,79.

Pour la copie : non $S_1$ : « il existe un modèle et un dataset sur lequel ce modèle a moins de 0,80 ». Non $S_3$ : « il existe un dataset sur lequel tous les modèles ont moins de 0,90 ». Non $S_6$ : « pour tout dataset, il existe un modèle d'accuracy inférieure à 0,84 ». d) et e) diffèrent par l'ordre des quantificateurs : dans $S_3$, le modèle peut dépendre du dataset ; dans $S_4$, le même modèle doit marcher pour tous.

**Erreurs fréquentes.** Lire $S_3$ comme $S_4$ ; nier « pour tout … au moins 0,80 » en « pour tout … moins de 0,80 » ; oublier une case en b).

**Variante.** « Pour chaque modèle, il existe un dataset où il atteint au moins 0,90 » ? *Réponse* : fausse ; E ne dépasse jamais 0,88.

### Ex M11.3 — Des phrases traduites en inclusions d'ensembles, et un contre-exemple

**Réponses** : a) `[5, 10]` · b) `True` · c) `3` · d) `5` · e) `[3]` · f) `True` · g) `5` · h) `10`.

**Démarche.**
- a) $A = \{6, 12, 18, 24, 30\}$ ; $B = \{3, 6, \ldots, 30\}$, dix éléments.
- b) $6k = 3 \times 2k$ : $A \subset B$.
- c) et d) $B \setminus A = \{3, 9, 15, 21, 27\}$, les multiples de 3 impairs ; le plus petit est 3.
- e) Le seul premier multiple de 3 est 3.
- f) Un multiple de 6 est divisible par 2 et par 3 : jamais premier. $P \cap A = \varnothing$.
- g) $Q = \{4, 8, 12, 16, 20, 24, 28\}$ ; $Q \cap A = \{12, 24\}$ ; $Q \setminus A$ a 5 éléments.
- h) $\lvert A \cup Q \rvert = 5 + 7 - 2 = 10$.

Pour la copie : b) $A \subset B$ ; réciproque $B \subset A$ ; f) $P \cap A = \varnothing$ ; g) « tout multiple de 4 est multiple de 6 » s'écrit $Q \subset A$. La contraposée de b) : $\bar{B} \subset \bar{A}$, « un nombre de $E$ qui n'est pas multiple de 3 n'est pas multiple de 6 ».

**Erreurs fréquentes.** Oublier 30 dans $A$ ou dans $B$ ; compter les exemples au lieu des contre-exemples en g) ; additionner $\lvert A \rvert + \lvert Q \rvert$ sans retirer $A \cap Q$.

**Variante.** Combien de contre-exemples a « tout multiple de 5 de $E$ est multiple de 10 » ? *Réponse* : 3 (5, 15 et 25).

### Ex M11.4 — Une induction trompeuse par oubli du taux de base, recalculée avec Bayes

**Réponses** : a) `0.0858` · b) `0.3217` · c) `582` · d) `0.0026` · e) `0.8791` · f) `0.0612` · g) `16.1`.

**Démarche.**
- a) $0{,}03 \times 0{,}92 + 0{,}97 \times 0{,}06 = 0{,}0276 + 0{,}0582 = 0{,}0858$ (probabilités totales).
- b) $\frac{0{,}0276}{0{,}0858} \approx 0{,}3217$ (Bayes).
- c) $10\,000 \times 0{,}97 \times 0{,}06 = 582$, contre $276$ capteurs défectueux signalés.
- d) $\frac{0{,}03 \times 0{,}08}{1 - 0{,}0858} = \frac{0{,}0024}{0{,}9142} \approx 0{,}0026$.
- e) Avec le taux de base $q = 0{,}3217$ : $\frac{0{,}92\,q}{0{,}92\,q + 0{,}06\,(1 - q)} \approx 0{,}8791$.
- f) $0{,}92\,\pi = 0{,}06\,(1 - \pi)$ donne $\pi = \frac{0{,}06}{0{,}98} \approx 0{,}0612$.
- g) $50 \times 0{,}3217 \approx 16{,}1$.

Pour la copie : sur 10 000 capteurs, 276 défectueux sont signalés, mais aussi 582 bons, parce que les bons sont 32 fois plus nombreux ; un capteur signalé n'est donc défectueux qu'environ une fois sur trois. Le technicien a confondu $P(\text{signalé} \mid \text{défectueux}) = 0{,}92$ et $P(\text{défectueux} \mid \text{signalé})$.

**Erreurs fréquentes.** Répondre 0,92 en b) ; oublier les bons signalés dans a) ; en e), multiplier 0,92 par 0,92.

**Variante.** Avec 30 % de capteurs défectueux, $P(\text{défectueux} \mid \text{signalé})$ ? *Réponse* : $\frac{0{,}276}{0{,}276 + 0{,}042} \approx 0{,}868$.

### Ex M11.5 — Markov : la queue d'une durée positive

**Réponses** : a) `0.25` · b) `1.0` · c) `30` · d) `0.0183` · e) `13.6` · f) `0.75` · g) `0.375` · h) `0.125`.

**Démarche.**
- a) $\frac{1{,}5}{6} = 0{,}25$.
- b) $\frac{1{,}5}{1} = 1{,}5 > 1$ : la borne vaut 1, elle n'apprend rien.
- c) $\frac{1{,}5}{a} \le 0{,}05$ donne $a \ge 30$.
- d) $P(T \ge 6) = e^{-6/1{,}5} = e^{-4} \approx 0{,}0183$.
- e) $\frac{0{,}25}{e^{-4}} = 0{,}25\,e^{4} \approx 13{,}6$ (avec la valeur arrondie 0,0183, on trouve 13,7, accepté aussi ; la valeur exacte reste la référence).
- f) La loi qui vaut 6 avec la probabilité $p$ et 0 sinon a pour moyenne $6p = 1{,}5$ : $p = 0{,}25$, et $P(T = 0) = 0{,}75$.
- g) Trois durées sur huit (2,0 ; 2,6 ; 3,3) : $0{,}375$.
- h) $P(T \ge 6) = P(T^2 \ge 36) \le \frac{4{,}5}{36} = 0{,}125$.

Pour la copie : la moyenne des huit durées vaut $\frac{12}{8} = 1{,}5$, et la borne de Markov au seuil 2 vaut $0{,}75 \ge 0{,}375$. L'échantillon est une loi (chaque valeur avec le poids $\frac{1}{8}$), positive, d'espérance $1{,}5$ : Markov s'y applique exactement, il ne peut pas la violer.

**Erreurs fréquentes.** $\frac{a}{\mathbb{E}[T]}$ au lieu de $\frac{\mathbb{E}[T]}{a}$ ; rendre 1,5 en b) ; en d), prendre $e^{-1{,}5 \times 6}$ (le paramètre d'une exponentielle de moyenne 1,5 est $\frac{1}{1{,}5}$) ; exclure la durée 2,0 en g).

**Variante.** La borne de Markov sur $P(T \ge 4)$, et la vraie valeur pour l'exponentielle ? *Réponse* : $0{,}375$ et $e^{-8/3} \approx 0{,}069$.

### Ex M11.6 — Tchebychev : combien d'observations pour une moyenne à ± 0,1 ?

**Réponses** : a) `1.0` · b) `2000` · c) `180` · d) `0.2` · e) `0.1111` · f) `0.25` · g) `250` · h) `9`.

**Démarche.**
- a) $\frac{(2 - 0)^2}{4} = 1$, atteinte par la loi qui vaut 0 ou 2 avec la probabilité $\frac{1}{2}$.
- b) $n \ge \frac{1}{0{,}05 \times 0{,}1^2} = 2\,000$.
- c) $n \ge \frac{0{,}09}{0{,}05 \times 0{,}01} = 180$.
- d) $\frac{0{,}09}{180 \times 0{,}05^2} = \frac{0{,}09}{0{,}45} = 0{,}2$.
- e) $\frac{\sigma^2}{n \times 9\sigma^2 / n} = \frac{1}{9}$.
- f) $p(1 - p) \le \frac{1}{4}$.
- g) $n \ge \frac{0{,}25}{0{,}1 \times 0{,}01} = 250$.
- h) La borne $\frac{\sigma^2}{n t^2}$ est divisée par 9.

Pour la copie : a) se démontre par $\mathbb{V}(X) \le \mathbb{E}[(X - 1)^2] \le 1$, car $\lvert X - 1 \rvert \le 1$ (M11.12, question 5). Connaître $\sigma = 0{,}3$ remplace la variance 1 du pire cas par $0{,}09$, plus de 11 fois plus petite : $n$ est divisé d'autant.

**Erreurs fréquentes.** Prendre $(b - a)^2$ ou $\frac{b - a}{2}$ pour la variance maximale ; mettre $\sigma$ au lieu de $\sigma^2$ en c) ; garder $t = 0{,}1$ en d) ; répondre 3 en h) (c'est le rayon, à risque fixé, qui est divisé par 3).

**Variante.** Valeurs dans $[0, 5]$, même précision et même risque, sans rien savoir de la variance ? *Réponse* : variance au plus $6{,}25$, et $n \ge 12\,500$.

### Ex M11.7 — Hoeffding : rayon de confiance et taille d'échantillon d'une proportion

**Réponses** : a) `0.0429` · b) `[0.0941, 0.1799]` · c) `2050` · d) `2944` · e) `0.0135` · f) `0.1` · g) `0.0215` · h) `0.0387`.

**Démarche.**
- a) $\sqrt{\frac{\ln 40}{2\,000}} = \sqrt{0{,}001844} \approx 0{,}0429$.
- b) $0{,}137 \pm 0{,}0429$ : $[0{,}0941 ;\ 0{,}1799]$.
- c) $n \ge \frac{\ln 40}{2 \times 0{,}03^2} = \frac{3{,}6889}{0{,}0018} \approx 2\,049{,}4$, donc 2 050.
- d) $\frac{\ln 200}{0{,}0018} = \frac{5{,}2983}{0{,}0018} \approx 2\,943{,}5$, donc 2 944.
- e) $2e^{-2 \times 1\,000 \times 0{,}0025} = 2e^{-5} \approx 0{,}0135$.
- f) $\frac{0{,}25}{1\,000 \times 0{,}0025} = 0{,}1$.
- g) $\frac{0{,}0429}{2} \approx 0{,}0215$ : quatre fois plus de requêtes, un rayon deux fois plus petit.
- h) $\sqrt{\frac{\ln 20}{2\,000}} \approx 0{,}0387$.

Pour la copie : « avec une probabilité au moins 0,95 sur le tirage des 1 000 requêtes, l'intervalle ainsi construit contient la vraie proportion $p$ » ; ce n'est pas « $p$ a 95 % de chances d'être dans $[0{,}0941 ;\ 0{,}1799]$ » ($p$ n'est pas aléatoire). Diviser le risque par 5 ne fait passer $\ln(2/\delta)$ que de 3,69 à 5,30 : $n$ n'est multiplié que par 1,44. Hoeffding (0,0135) bat Tchebychev (0,1) d'un facteur 7.

**Erreurs fréquentes.** Oublier la racine (0,0018) ou le 2 de $2n$ (0,0607) ; utiliser $\ln(1/\delta)$ pour un rayon bilatéral ; arrondir $n$ au-dessous ; diviser le rayon par 4 en g).

**Variante.** Le rayon pour $n = 250$ et $\delta = 0{,}1$ ? *Réponse* : $\sqrt{\frac{\ln 20}{500}} \approx 0{,}0774$.

### Ex M11.8 — Trois bornes pour une même question : Markov, Tchebychev, Hoeffding, et l'approximation normale

**Réponses** : a) `0.6667` · b) `0.16` · c) `0.1353` · d) `0.0062` · e) `0.0112` · f) `"c"` · g) `0.6065` · h) `231`.

**Démarche.**
- a) $\mathbb{E}[S] = 20$ : $\frac{20}{30} \approx 0{,}6667$.
- b) $\mathbb{V}(S) = 100 \times 0{,}2 \times 0{,}8 = 16$ ; $P(S \ge 30) \le P(\lvert S - 20 \rvert \ge 10) \le \frac{16}{100} = 0{,}16$.
- c) $S \ge 30$ équivaut à $\bar{X} - 0{,}2 \ge 0{,}1$ : $e^{-2 \times 100 \times 0{,}01} = e^{-2} \approx 0{,}1353$.
- d) $z = \frac{30 - 20}{4} = 2{,}5$ ; $P(Z \ge 2{,}5) \approx 0{,}0062$.
- e) $P(S \ge 30) = \sum_{k=30}^{100} \binom{100}{k} 0{,}2^k\,0{,}8^{100-k} \approx 0{,}0112$.
- f) Hoeffding (0,135) est la plus proche de 0,0112 ; Tchebychev (0,16) suit, Markov (0,67) est loin.
- g) $S \ge 25$ : écart $t = 0{,}05$, $e^{-2 \times 100 \times 0{,}0025} = e^{-0{,}5} \approx 0{,}6065$ (la valeur exacte est 0,13).
- h) $e^{-0{,}02 n} \le 0{,}01$ donne $n \ge \frac{\ln 100}{0{,}02} \approx 230{,}3$, donc 231.

Pour la copie : Markov n'utilise que la moyenne, et la loi qui l'atteint (0 ou 30) est très loin d'une binomiale. L'approximation normale n'est pas une borne : elle peut être au-dessous de la vraie valeur, comme ici (0,0062 contre 0,0112). La valeur exacte est la probabilité de 30 succès ou plus, la somme des probabilités binomiales correspondantes (`scipy.stats.binom(100, 0.2).sf(29)`).

**Erreurs fréquentes.** Mettre le facteur 2 du bilatéral en c) ; diviser la variance par 10 au lieu de $10^2$ ; en e), oublier $S = 30$ ; prendre l'approximation normale pour une borne.

**Variante.** Les bornes de Tchebychev et de Hoeffding sur $P(S \le 10)$ ? *Réponse* : 0,16 et $e^{-2} \approx 0{,}135$ (par symétrie de l'écart) ; la valeur exacte vaut environ 0,0057.

### Ex M11.9 — D'où vient le bonus d'UCB : Hoeffding avec un risque qui décroît avec t

**Réponses** : a) `0.2146` · b) `0.5257` · c) `1.1457` · d) `1.7641` · e) `2` · f) `1843` · g) `0.0823` · h) `0.3717`.

**Démarche.**
- a) $e^{-2Nr^2} = \delta$ donne $r = \sqrt{\frac{\ln(1/\delta)}{2N}} = \sqrt{\frac{\ln 100}{100}} \approx 0{,}2146$.
- b) $\ln(1/\delta_t) = 4\ln t$, donc $r = \sqrt{\frac{4\ln t}{2N}} = \sqrt{\frac{2\ln t}{N}} = \sqrt{\frac{2 \times 6{,}9078}{50}} \approx 0{,}5257$.
- c) $0{,}62 + 0{,}5257 = 1{,}1457$.
- d) $0{,}45 + \sqrt{\frac{13{,}8155}{8}} \approx 0{,}45 + 1{,}3141 = 1{,}7641$.
- e) L'option 2, de borne supérieure la plus haute, malgré une moyenne observée plus basse.
- f) $\sqrt{\frac{2\ln t}{N}} < 0{,}1$ équivaut à $N > 200\ln(10\,000) \approx 1\,842{,}07$ : $N = 1\,843$.
- g) $\sum_{t \ge 1} t^{-4} = \frac{\pi^4}{90} \approx 1{,}0823$ ; sans le terme $t = 1$ : $0{,}0823$.
- h) $\ln(1/\delta_t) = 2\ln t$ : $\sqrt{\frac{\ln 1\,000}{50}} \approx 0{,}3717$.

Pour la copie : b) est le calcul général. g) : par la borne de l'union, la probabilité qu'une borne supérieure soit fausse au moins une fois entre le pas 2 et l'infini (pour une option et un nombre de choix donnés) est au plus 0,08 (la preuve complète d'UCB1 fait aussi la borne de l'union sur les valeurs de $N$, au plus $t$, et sur les $K$ options, d'où le choix d'un risque qui décroît vite) ; le risque décroît assez vite pour que la somme reste petite. f) : le seuil $\frac{8\ln t}{\Delta^2}$ ne croît que comme $\ln t$ ; au-delà, la borne de l'option d'écart $\Delta$ passe sous $\mu^\star$ (si les bornes sont justes), et UCB ne la choisit plus.

**Erreurs fréquentes.** Utiliser $\ln(2/\delta)$ (bilatéral) au lieu de $\ln(1/\delta)$ ; oublier le 2 de $2N$ ; prendre $\log_{10}$ pour $\ln$ ; choisir l'option de plus grande moyenne en e).

**Variante.** Le bonus d'UCB1 au pas 10 000 pour une option choisie 200 fois ? *Réponse* : $\sqrt{\frac{2 \times 9{,}2103}{200}} \approx 0{,}3035$.

### Ex M11.10 — ε-greedy : la loi du bras joué et le regret attendu par pas

**Réponses** : a) `0.88` · b) `0.03` · c) `0.079` · d) `0.0769` · e) `390` · f) `1.3625` · g) `600`.

**Démarche.** $\mu^\star = 0{,}62$ (option 3) ; les écarts valent $\Delta = (0{,}07 ;\ 0{,}32 ;\ 0 ;\ 0{,}14 ;\ 0{,}12)$, de somme $0{,}65$.
- a) $0{,}85 + \frac{0{,}15}{5} = 0{,}88$.
- b) $\frac{0{,}15}{5} = 0{,}03$.
- c) $0{,}88 \times 0{,}07 + 0{,}03 \times (0{,}32 + 0 + 0{,}14 + 0{,}12) = 0{,}0616 + 0{,}0174 = 0{,}079$.
- d) $\frac{\varepsilon}{5} \times 0{,}65 = 0{,}01$ donne $\varepsilon = \frac{0{,}05}{0{,}65} \approx 0{,}0769$.
- e) $0{,}03 \times 0{,}65 = 0{,}0195$ par pas, soit 390 sur 20 000 pas.
- f) $\sum_{t=1}^{20\,000} \frac{1}{t} \times \frac{0{,}65}{5} = 0{,}13 \times 10{,}4807 \approx 1{,}3625$.
- g) $20\,000 \times 0{,}03 = 600$.

Pour la copie : e) croît linéairement (390 sur 20 000 pas, 1 950 sur 100 000), f) comme $\ln T$ (à peine 1,57 sur 100 000 pas). Mais f) suppose un choix glouton juste dès le départ ; si le glouton est faux, comme en a), il faut explorer assez pour le corriger, et un ε qui décroît trop vite peut laisser l'option 1 choisie pour toujours.

**Erreurs fréquentes.** Oublier la part $\frac{\varepsilon}{K}$ du choix glouton en a) ; prendre l'option 1 pour la meilleure en c) ; oublier le $K$ en d) et f).

**Variante.** Avec $\varepsilon = 0{,}3$ et le même choix glouton faux, la probabilité de choisir l'option 1 ? *Réponse* : $0{,}7 + 0{,}06 = 0{,}76$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M11.11 — L'inégalité de Markov

**Réponse modèle.**
1. Si $X \ge a$, $a\,\mathbf{1}_{X \ge a} = a \le X$. Si $X < a$, $a\,\mathbf{1}_{X \ge a} = 0 \le X$ car $X \ge 0$. L'espérance est **croissante** (si $U \le V$, $\mathbb{E}[U] \le \mathbb{E}[V]$) et **linéaire**, et $\mathbb{E}[\mathbf{1}_{X \ge a}] = P(X \ge a)$ : $a\,P(X \ge a) \le \mathbb{E}[X]$, puis on divise par $a > 0$.
2. $\mathbb{E}[Y] = a \times p + 0 \times (1 - p) = pa$ et $P(Y \ge a) = p = \frac{\mathbb{E}[Y]}{a}$. Pour toute valeur $m \in [0, a]$ de l'espérance, la loi $Y$ avec $p = \frac{m}{a}$ a cette espérance et atteint la borne : aucune borne qui n'utilise que $\mathbb{E}[X]$ ne peut être plus petite.
3. $X = 10$ ou $-10$ avec la probabilité $\frac{1}{2}$ : $\mathbb{E}[X] = 0$, mais $P(X \ge 5) = \frac{1}{2} > \frac{0}{5}$.
4. $\varphi$ croissante : $X \ge a$ entraîne $\varphi(X) \ge \varphi(a)$, donc $P(X \ge a) \le P(\varphi(X) \ge \varphi(a))$. La variable $\varphi(X)$ est positive, et la question 1 au seuil $\varphi(a) > 0$ donne $P(\varphi(X) \ge \varphi(a)) \le \frac{\mathbb{E}[\varphi(X)]}{\varphi(a)}$. Avec $\varphi(x) = e^{\lambda x}$ : $P(X \ge a) \le e^{-\lambda a}\,\mathbb{E}[e^{\lambda X}]$ (la méthode de Chernoff, fiche §6).
5. La question 1 au seuil $a = k\mu > 0$ : $P(X \ge k\mu) \le \frac{\mu}{k\mu} = \frac{1}{k}$.

**Grille.** (1) les deux cas, l'usage de $X \ge 0$ dans le second, la croissance et la linéarité de l'espérance, $\mathbb{E}[\mathbf{1}_A] = P(A)$ ; (2) le calcul pour la loi à deux valeurs et l'argument « on ne peut pas faire mieux » ; (3) un contre-exemple vérifié ; (4) l'inclusion des événements grâce à la croissance de $\varphi$, puis la question 1 appliquée à $\varphi(X)$ ; (5) le bon seuil.

### Ex M11.12 — Tchebychev à partir de Markov, puis la loi faible des grands nombres

**Réponse modèle.**
1. $Y = (X - \mu)^2 \ge 0$ a pour espérance $\sigma^2$. L'événement $\lvert X - \mu \rvert \ge t$ est l'événement $Y \ge t^2$ ($t > 0$). Markov : $P(\lvert X - \mu \rvert \ge t) = P(Y \ge t^2) \le \frac{\sigma^2}{t^2}$.
2. La loi a pour espérance $\mu$ (par symétrie) et pour variance $\frac{p}{2}t^2 + \frac{p}{2}t^2 + 0 = pt^2$ ; et $P(\lvert X - \mu \rvert \ge t) = p = \frac{pt^2}{t^2}$.
3. $\mathbb{V}(\sum X_i) = \sum \mathbb{V}(X_i) + \sum_{i \ne j} \operatorname{Cov}(X_i, X_j) = n\sigma^2$, les covariances étant nulles pour des variables indépendantes (il suffit qu'elles le soient). Puis $\mathbb{V}(\bar{X}) = \frac{1}{n^2} n\sigma^2 = \frac{\sigma^2}{n}$.
4. $\mathbb{E}[\bar{X}] = \mu$, et Tchebychev donne $P(\lvert \bar{X} - \mu \rvert \ge t) \le \frac{\sigma^2}{nt^2}$, qui tend vers 0 quand $n \to +\infty$ ; une probabilité positive majorée par une quantité qui tend vers 0 tend vers 0. Pour $n \ge \frac{\sigma^2}{\delta t^2}$, la borne est au plus $\delta$.
5. $\mathbb{E}[(X - c)^2] = \mathbb{E}[(X - \mu)^2] + 2(\mu - c)\mathbb{E}[X - \mu] + (\mu - c)^2 = \sigma^2 + (\mu - c)^2$, car $\mathbb{E}[X - \mu] = 0$. Donc $\sigma^2 \le \mathbb{E}[(X - c)^2]$ pour tout $c$. Avec $c = \frac{a + b}{2}$, $\lvert X - c \rvert \le \frac{b - a}{2}$, d'où $\sigma^2 \le \frac{(b - a)^2}{4}$. Égalité quand $\mu = c$ et $\lvert X - c \rvert = \frac{b - a}{2}$ partout : $X$ vaut $a$ ou $b$ avec la probabilité $\frac{1}{2}$ chacune.

**Grille.** (1) la variable positive $(X - \mu)^2$ et l'égalité des événements ; (2) la variance de la loi à trois points ; (3) la variance d'une somme, où sert l'indépendance (covariances nulles), le facteur $\frac{1}{n^2}$ ; (4) le passage à la limite et un $n$ explicite ; (5) l'identité avec $c$ quelconque, le choix du milieu, le cas d'égalité.

### Ex M11.13 — Avec ε fixé, le regret attendu d'ε-greedy croît au moins linéairement

**Réponse modèle.**
1. $\mu^\star - \mu_{A_t} = \sum_k \Delta_k\,\mathbf{1}_{A_t = k}$ (une seule indicatrice vaut 1) ; l'espérance donne $\sum_k \Delta_k\,P(A_t = k)$. En sommant sur $t$ et en échangeant les sommes : $R_T = \sum_k \Delta_k \sum_t P(A_t = k) = \sum_k \Delta_k\,\mathbb{E}\big[\sum_t \mathbf{1}_{A_t = k}\big] = \sum_k \Delta_k\,\mathbb{E}[N_k(T)]$.
2. Par la formule des probabilités totales sur le résultat de la pièce : $P(A_t = k) = \varepsilon \times \frac{1}{K} + (1 - \varepsilon)\,P(\text{glouton} = k) \ge \frac{\varepsilon}{K}$.
3. $\mathbb{E}[\mu^\star - \mu_{A_t}] \ge \frac{\varepsilon}{K}\sum_k \Delta_k$ à chaque pas, donc $R_T \ge \frac{\varepsilon T}{K}\sum_k \Delta_k$. Si une option au moins n'est pas la meilleure, $\sum_k \Delta_k > 0$ et le regret croît au moins linéairement : la proportion de pas mal employés ne tend pas vers 0.
4. Les tirages au hasard du pas $t$ coûtent en espérance $\varepsilon_t \times \frac{1}{K}\sum_k \Delta_k \le \frac{c}{t} \times \frac{1}{K}\sum_k \Delta_k$ ; on somme sur $t$. Pour $t \ge 2$, $\frac{1}{t} \le \frac{1}{x}$ sur $[t - 1, t]$, donc $\frac{1}{t} \le \int_{t-1}^{t} \frac{dx}{x}$ ; en sommant de 2 à $T$, $\sum_{t=2}^{T} \frac{1}{t} \le \int_1^T \frac{dx}{x} = \ln T$, et $\sum_{t=1}^{T} \frac{1}{t} \le 1 + \ln T$.
5. Il reste la part des pas où la pièce dit « glouton » et où le choix glouton n'est pas la meilleure option. Elle dépend de la qualité des estimations ; avec trop peu d'exploration, une option mal estimée au début peut rester le choix glouton longtemps, et cette part peut croître linéairement. Il faudrait montrer que les estimations deviennent justes assez vite (c'est possible si $c$ est assez grand, ce qu'on ne fait pas ici).

**Grille.** (1) la décomposition par indicatrices et l'échange des sommes ; (2) les probabilités totales sur la pièce ; (3) la somme sur $T$ pas et l'interprétation ; (4) la comparaison série-intégrale, avec le terme $t = 1$ à part ; (5) l'identification de la part « exploitation d'un mauvais choix glouton ».

<a id="reflexion"></a>

## 🔗 ⚖️ 🗣️ Pont, esprit critique et explication

### Ex M11.14 — Pont : combien d'exemples de test pour connaître une accuracy à ± 2 points, garanti par Hoeffding ?

**Réponses** : a) `4612` · b) `0.0248` · c) `0.8517` · d) `0.0334` · e) `0.0119` · f) `8198`.

**Démarche.**
- a) $n \ge \frac{\ln 40}{2 \times 0{,}0004} \approx 4\,611{,}1$, donc 4 612.
- b) $\sqrt{\frac{\ln 40}{6\,000}} \approx 0{,}0248$.
- c) Le rayon unilatéral vaut $\sqrt{\frac{\ln 20}{6\,000}} \approx 0{,}0223$ : avec une probabilité au moins 0,95, l'accuracy de A est au moins $0{,}874 - 0{,}0223 \approx 0{,}8517$.
- d) $\sqrt{\frac{\ln(2 / 0{,}0025)}{6\,000}} = \sqrt{\frac{\ln 800}{6\,000}} \approx 0{,}0334$.
- e) $1{,}96\sqrt{\frac{0{,}874 \times 0{,}126}{3\,000}} \approx 1{,}96 \times 0{,}00606 \approx 0{,}0119$.
- f) $\frac{\ln 40}{2 \times 0{,}015^2} \approx 8\,197{,}5$, donc 8 198.

Pour la copie : Hoeffding suppose le pire cas, une variance $\frac{1}{4}$, quand la vraie vaut $0{,}874 \times 0{,}126 \approx 0{,}11$, et elle vaut pour tout $n$ sans approximation : elle est donc plus large que l'intervalle normal. La correction de d) protège contre le choix sur le test : parmi 20 modèles, l'un a pu avoir de la chance sur ce jeu, et son accuracy est optimiste. La garantie de c) : « avec une probabilité au moins 0,95 sur le tirage des 3 000 exemples, l'accuracy de A sur les données de service est au moins 0,8517 ». On ne borne que le côté que l'on craint (une accuracy trop basse) : tout le risque $\delta$ va de ce côté, d'où $\ln(1/\delta)$ au lieu de $\ln(2/\delta)$ et une borne un peu plus serrée.

**Erreurs fréquentes.** Arrondir $n$ au-dessous ; diviser par $n$ au lieu de $2n$ ; mettre le 20 de d) devant la racine au lieu de dans le logarithme ; en c), garder $\ln(2/\delta)$, ou rendre le rayon au lieu de la borne basse.

**Variante.** Le rayon de Hoeffding pour 10 000 exemples de test, avec $\delta = 0{,}05$ ? *Réponse* : $\sqrt{\frac{\ln 40}{20\,000}} \approx 0{,}0136$.

### Ex M11.15 — Corrélation, causalité et induction : trois titres de presse à démonter

**Réponse attendue** (avec tes mots).
1. *Induction* : on a observé que les villes riches en pistes cyclables ont moins de maladies cardiaques, donc les pistes rendent la population plus saine. *Autres explications* : les villes plus riches, plus jeunes ou au climat doux ont à la fois plus de pistes et moins de maladies (facteurs de confusion) ; une population déjà sportive réclame des pistes (causalité inverse) ; une comparaison entre villes ne dit rien des individus. *Pour trancher* : suivre, dans des villes comparables, l'évolution de la santé avant et après la construction, par rapport à des villes sans nouvelles pistes ; mieux, tirer au sort l'ordre dans lequel des quartiers sont équipés.
2. *Induction* : les utilisateurs de l'application ont de meilleures notes, donc l'application fait progresser. *Autres explications* : les élèves motivés ou mieux suivis choisissent l'application (sélection) ; les bons élèves aiment réviser (confusion par le niveau de départ). *Pour trancher* : tirer au sort les élèves qui reçoivent l'application, et comparer les progrès, pas les notes.
3. *Induction* : les ventes ont augmenté après l'installation, donc le modèle en est la cause. *Autres explications* : novembre et décembre sont des mois de fêtes (saisonnalité) ; une tendance de fond, une promotion, un concurrent en difficulté ; un mois précédent anormalement bas (retour vers la moyenne). *Pour trancher* : un test où une partie des visiteurs, tirée au hasard, garde l'ancien modèle pendant la même période.

Règle générale : pour conclure qu'une chose en cause une autre, il faut comparer des groupes qui ne diffèrent que par elle, ce que garantit un tirage au sort ; une corrélation observée seule ne suffit pas.

**Grille.** (1) chaque induction écrite « on a observé…, donc… » ; (2) au moins deux explications par titre, nommées (confusion, causalité inverse, sélection, tendance) ; (3) une expérience ou une donnée qui sépare les explications, avec un groupe de comparaison ; (4) la règle générale.

### Ex M11.16 — Expliquer « l'optimisme face à l'incertitude » à partir d'un intervalle de confiance

**Réponse modèle.**

> Pour chaque vin, tu calcules la satisfaction moyenne et un intervalle autour d'elle : large si le vin a été peu goûté, étroit s'il l'a été souvent. Chaque soir, tu mets en avant le vin dont la borne supérieure de l'intervalle est la plus haute, comme si chacun valait le mieux qu'il peut raisonnablement valoir. Un vin peu goûté a un grand intervalle : même avec une moyenne moyenne, sa borne supérieure dépasse souvent les autres, et tu l'essaies ; c'est ce qui te fait explorer. À force d'être goûté, un mauvais vin a un intervalle étroit autour d'une note basse : sa borne supérieure passe sous la moyenne du meilleur, et tu ne le choisis presque plus. Au bout du compte, tu exploites le meilleur, sans avoir abandonné trop tôt un vin malchanceux.

**Grille.** (1) l'intervalle, large avec peu de données ; (2) la règle « la plus haute borne supérieure » ; (3) pourquoi un vin peu goûté est choisi (explorer) ; (4) pourquoi un mauvais vin cesse de l'être ; (5) six lignes au plus, sans formule, avec les trois mots imposés.

<a id="entretien"></a>

## 💼 Entretien

### M11.E1 — « À quoi sert l'inégalité de Hoeffding en apprentissage, et que suppose-t-elle ? »

**Réponse modèle (60 secondes).**

> L'inégalité de Hoeffding dit que la moyenne de $n$ variables indépendantes et bornées s'écarte de son espérance de plus de $t$ avec une probabilité au plus $2e^{-2nt^2/(b - a)^2}$ : une probabilité qui décroît exponentiellement avec $n$, quelle que soit la loi. En apprentissage, elle sert d'abord à évaluer : l'accuracy sur $n$ exemples de test est une moyenne de 0 et de 1, donc on sait combien d'exemples il faut pour la connaître à $\pm t$ avec un risque $\delta$, environ $\frac{\ln(2/\delta)}{2t^2}$, soit 4 600 exemples pour $\pm 2$ points à 95 %. Elle est aussi la brique des bornes de généralisation et des bornes de confiance des bandits, comme UCB. Elle suppose trois choses : des variables bornées dans un intervalle connu d'avance (pas une loss qui peut exploser) ; des exemples indépendants (pas de séries temporelles ni de doublons entre entraînement et test) ; une quantité fixée avant de regarder les données : si l'on choisit le meilleur de $K$ modèles sur le test, il faut la borne de l'union, $\frac{\delta}{K}$. Par rapport à l'intervalle normal, elle est plus large, mais c'est une garantie, valable pour tout $n$, sans approximation.

**Grille.** (1) l'énoncé en mots, avec la décroissance exponentielle et l'absence d'hypothèse de loi ; (2) un usage concret chiffré (taille d'un jeu de test, rayon) ; (3) les trois hypothèses, avec un exemple de ce qui les casse ; (4) la borne de l'union pour un choix fait sur les données ; (5) la comparaison avec l'approximation normale.

<a id="notebook"></a>

## Notebook

### Ex M11.17 — Les bornes de Markov et de Tchebychev · `markov_bound, chebyshev_bound`

**Réponses** : a) `0.25` · b) `1.0` · c) `0.25` · d) `0.0` · e) `"ValueError"` · f) `"ValueError"` · g) `"float"`.

**Démarche.** `mean, a = float(mean), float(a)` ; une `ValueError` si `mean < 0`, une autre si `a <= 0` ; puis `return float(min(1.0, mean / a))`. Même schéma pour `chebyshev_bound`, avec `variance / t ** 2`. Pour la copie : b) la formule donne $\frac{4}{3}$, qui n'est pas une probabilité ; sans le `min`, la fonction rendrait une « borne » plus grande que 1, vraie mais sans valeur. d) Une variance nulle donne une borne nulle : la variable est presque sûrement égale à sa moyenne.

**Erreurs fréquentes.** Oublier le `min` ; lever une `ValueError` pour une variance nulle ; diviser par $t$ au lieu de $t^2$ ; rendre un `np.float64` ou un entier.

### Ex M11.18 — La borne et le rayon de Hoeffding · `hoeffding_bound, hoeffding_radius`

**Réponses** : a) `0.0815` · b) `0.8987` · c) `0.0547` · d) `0.1095` · e) `0.1` · f) `"ValueError"` · g) `"ValueError"`.

**Démarche.** Une fonction auxiliaire vérifie `n >= 1` et `a < b` ; la borne vaut `min(1.0, 2 * math.exp(-2 * n * t ** 2 / (b - a) ** 2))` après le contrôle de `t > 0` ; le rayon `(b - a) * math.sqrt(math.log(2 / delta) / (2 * n))` après le contrôle de `0 < delta < 1`. a) $2e^{-3{,}2} \approx 0{,}0815$ ; b) $2e^{-0{,}8} \approx 0{,}8987$ ; c) $\sqrt{\frac{\ln 20}{1\,000}} \approx 0{,}0547$ ; d) le double. Pour la copie : e) le rayon est défini comme l'écart où la borne vaut $\delta$ ; b) est plus grand que a) parce qu'un écart de 0,08 sur $[0, 2]$ ne vaut qu'un écart de 0,04 sur $[0, 1]$.

**Erreurs fréquentes.** Oublier le facteur 2, le carré de $b - a$, ou la racine du rayon ; `math.log(1 / delta)` ; accepter $\delta = 1$ ou $n = 0$.

### Ex M11.19 — La queue empirique d'un échantillon · `empirical_tail`

**Réponses** : a) `0.5` · b) `0.3333` · c) `0.05145` · d) `"ValueError"` · e) `True`.

**Démarche.** `values = np.asarray(samples, dtype=float)` ; une `ValueError` si `values.size == 0` ; `return float(np.mean(values >= threshold))`. Pour la copie : c) 0,0515 contre $e^{-3} \approx 0{,}0498$ : l'écart (0,0017) est de l'ordre de l'erreur type d'une proportion sur 20 000 tirages ($\approx 0{,}0015$). e) L'échantillon est une loi positive d'espérance $\bar{x}$ : Markov s'y applique exactement.

**Erreurs fréquentes.** `>` au lieu de `>=` (a) donne $\frac{1}{3}$) ; rendre un nombre de valeurs au lieu d'une proportion ; ne pas refuser l'échantillon vide (`np.mean([])` rend `nan` avec un avertissement).

### Ex M11.20 — Les vraies queues d'une loi exponentielle et d'une binomiale (`scipy.stats`) contre les bornes

**Réponses** : a) `0.0067` · b) `29.68` · c) `13.8155` · d) `0.0993` · e) `0.3125` · f) `0.6024`.

**Démarche.** a) `stats.expon(scale=3).sf(15)` $= e^{-5} \approx 0{,}0067$ ; b) Markov donne $\frac{3}{15} = 0{,}2$, soit 29,7 fois trop ; c) `.isf(0.01)` $= 3\ln 100 \approx 13{,}8155$ ; d) `S.cdf(9) + S.sf(20)` avec `S = stats.binom(60, 0.25)` ; e) `chebyshev_bound(0.25 * 0.75 / 60, 0.1)` ; f) `hoeffding_bound(60, 0.1)` $= 2e^{-1{,}2}$. Pour la copie : Tchebychev (0,31) bat Hoeffding (0,60) parce que $2nt^2 = 1{,}2$ est petit et que la variance (0,1875) est sous le maximum $\frac{1}{4}$ que Hoeffding suppose ; la vraie valeur (0,099) est encore trois fois plus petite.

**Erreurs fréquentes.** `stats.expon(3)` (3 serait le décalage `loc`, pas la moyenne) ; `sf(21)` au lieu de `sf(20)` pour $P(S \ge 21)$ ; `ppf` au lieu de `isf` ; oublier un des deux côtés en d).

### Ex M11.21 — Prédire : laquelle des trois bornes est la plus serrée pour n = 100 ?

**Réponses** : a) `3` · b) `2` · c) `3` · d) `1`.

**Démarche.** Les trois bornes, cas par cas :

| cas | Markov $\frac{p}{p + t}$ | Tchebychev $\frac{p(1 - p)}{nt^2}$ | Hoeffding $e^{-2nt^2}$ | la plus serrée |
|---|---|---|---|---|
| a) $p = 0{,}5$, $t = 0{,}1$ | 0,83 | 0,25 | 0,135 | Hoeffding |
| b) $p = 0{,}02$, $t = 0{,}05$ | 0,29 | 0,078 | 0,61 | Tchebychev |
| c) $p = 0{,}01$, $t = 0{,}5$ | 0,020 | 0,0004 | $2 \times 10^{-22}$ | Hoeffding |
| d) $p = 0{,}001$, $t = 0{,}004$ | 0,2 | 0,62 | 0,997 | Markov |

Pour la copie : Markov utilise la moyenne seule (elle gagne quand la moyenne est minuscule devant l'écart à franchir, en valeur absolue : $\bar{X} \ge 0{,}005$ est peu probable si $\mathbb{E}[\bar{X}] = 0{,}001$) ; Tchebychev utilise la variance (elle gagne quand la variance est petite et l'écart modeste) ; Hoeffding utilise l'intervalle $[0, 1]$ (elle gagne pour les écarts grands devant $\frac{1}{\sqrt{n}}$). Sans rien savoir de $p$, Hoeffding est le choix sûr : elle ne suppose rien sur la variance.

**Erreurs fréquentes de prédiction.** b) Hoeffding, par habitude : elle ignore la variance, qui est ici minuscule ; d) Tchebychev ou Hoeffding : pour un écart minuscule, seules les valeurs absolues comptent.

### Ex M11.22 — La fréquence des écarts |x̄ − p| ≥ t comparée à la borne de Hoeffding, quand n grandit

**Réponses** : a) `0.021` · b) `True` · c) `512` · d) `0.0250` · e) `28.1`.

**Démarche.** `k = rng.binomial(n, p, size=reps)` puis `float(np.mean(np.abs(k / n - p) >= t))`, avec un seul générateur créé avant la boucle sur $n$. La probabilité exacte : `stats.binom.pmf(k, n, p)` sur `k = np.arange(n + 1)`, sommée sur les $k$ loin de $np$. La borne vaut $2e^{-n/128}$ : 1, 1, 0,74, 0,27, 0,037 puis 0,0007 ; elle passe sous 0,05 à $n = 512$. Pour la copie : en échelle log, la borne est une droite en $n$ ; la probabilité exacte décroît plus vite (son exposant dépend de la variance $0{,}1875$), d'où un rapport qui grandit (11 à $n = 256$, 28 à $n = 512$). a) et d) diffèrent par le hasard des 4 000 tirages (erreur type $\approx 0{,}0025$).

**Erreurs fréquentes.** Créer un nouveau générateur pour chaque $n$ (des tirages différents) ; tirer les variables de Bernoulli une à une dans une boucle (lent, et d'autres tirages) ; compter un seul côté de l'écart.

### Ex M11.23 — La probabilité qu'un tirage d'une loi Beta dépasse celui d'une autre, par simulation

**Réponses** : a) `0.667175` · b) `0.6667` · c) `0.46982` · d) `0.4725` · e) `0.2693`.

**Démarche.** Simulation : `x1 = rng.beta(a1, b1, size)`, `x2 = rng.beta(a2, b2, size)`, `float(np.mean(x2 > x1))`. Intégrale : $P(\theta_2 > \theta_1) = \int_0^1 f_2(x)\,P(\theta_1 < x)\,dx$, par `integrate.quad`. b) Pour $\theta_1$ uniforme, $P(\theta_1 < \theta_2) = \mathbb{E}[\theta_2] = \frac{2}{3}$. Pour la copie : $\mathrm{Beta}(4, 3)$, tirée de 5 essais, est très étalée (écart-type 0,17) ; $\mathrm{Beta}(13, 9)$ l'est moins (0,10) : leurs tirages se croisent souvent, et Thompson choisit l'option 2 presque une fois sur deux, ce qui l'aide à apprendre si elle vaut mieux. En e), l'option 2 a 58 essais : sa loi se resserre autour de 0,52, sous l'option 1, et la probabilité tombe à 0,27.

**Erreurs fréquentes.** Tirer `x2` avant `x1` (d'autres tirages) ; la proportion des `x1 > x2` ; intégrer $f_1 F_2$ (on obtient $P(\theta_1 > \theta_2)$).

### Ex M11.24 — Les bornes de Markov, de Tchebychev et de Hoeffding contre la vraie queue, en échelle log

**Réponse** : la figure, et les vérifications automatiques au vert.

**Démarche.** Pour chaque $t$, la vraie queue `stats.binom.sf(k - 1, n, p)` avec `k = math.ceil(n * (p + t) - 1e-9)` ; puis `p / (p + ts)`, `np.minimum(1.0, p * (1 - p) / (n * ts ** 2))` et `np.exp(-2 * n * ts ** 2)`, quatre `ax.plot(ts, …, label=…)`, `ax.set_yscale("log")`, `ax.legend()`. Pour la copie : avec $n = 50$ et $p = 0{,}3$, Hoeffding est la meilleure presque partout (Markov seulement pour $t < 0{,}033$ environ) ; la vraie queue et Hoeffding ont la même forme en échelle log, une parabole en $t$, car leur exposant est en $t^2$.

**Erreurs fréquentes.** `sf(k)` au lieu de `sf(k - 1)` (on oublie $S = k$) ; oublier le plafond de Tchebychev ; une échelle linéaire, où les petites probabilités sont invisibles.

### Ex M11.25 — Chasse à l'erreur : Markov pour une variable négative, Hoeffding sans bornes, un rayon sans racine

**Réponses** : a) `"BEF"` · b) `0.2707` · c) `0.6791` · d) `0.0461`.

**Démarche.** (B) applique Markov à une variable qui peut être négative ; (E) oublie $(b - a)^2 = 100$ ; (F) oublie la racine carrée. (A), (C) et (D) sont justes ((D) remplace la variance par son estimation, comme le dit son commentaire). b) $2e^{-2 \times 400 \times 0{,}25 / 100} = 2e^{-2} \approx 0{,}2707$ ; c) $10\sqrt{\frac{\ln 40}{800}} \approx 0{,}6791$ ; d) $\frac{10 \ln 40}{800} \approx 0{,}0461$. Pour la copie : `markov = min(1.0, (mean + 5) / (threshold + 5))` (Markov sur $X + 5 \ge 0$), `hoeffding = min(1.0, 2 * math.exp(-2 * n * t ** 2 / 10 ** 2))`, `radius = 10 * math.sqrt(math.log(2 / delta) / (2 * n))`. Pour une moyenne de $-0{,}2$, la ligne (B) rendrait un nombre négatif, la borne d'aucune probabilité ; le rayon faux de d) est quinze fois trop petit et fait croire à une précision qu'on n'a pas.

**Erreurs fréquentes.** Citer (D) ; en b), oublier le facteur 2 ou diviser par 10 au lieu de 100 ; en c), multiplier par 100.

### Ex M11.26 — Un test paramétré qui vérifie l'inégalité de Markov sur dix lois

**Réponse** : les vérifications automatiques au vert : ton test passe sur la vraie borne et échoue sur les deux fausses.

**Démarche.** Un dictionnaire de dix lois gelées, positives, une boucle sur des seuils non entiers (pour qu'une loi à valeurs entières ait `sf(a)` $= P(X \ge a)$), un `assert bound >= tail - 1e-12, f"{name}, a = {a}: …"`. Les lois qui comptent : une loi à deux valeurs où Markov est presque atteinte (`stats.bernoulli(0.9)` au seuil 0,999 : la vraie valeur 0,9, la borne 0,901, la borne deux fois trop petite 0,45) et une loi à queue lourde (`stats.pareto(1.2)`, `stats.lognorm(1.5)`), dont la queue décroît plus lentement qu'une exponentielle. Pour la copie : les lois usuelles (exponentielle, uniforme, Poisson) ont des queues bien plus légères que $\frac{\mathbb{E}[X]}{a}$ ; même divisée par deux, une borne fausse reste au-dessus d'elles.

**Erreurs fréquentes.** Des seuils entiers avec `sf(a)` pour une loi discrète (on teste $P(X > a)$, plus petit : le test passerait à tort) ; utiliser dans le test un nom défini ailleurs dans le notebook ; seulement des lois « ordinaires ».

### Ex M11.27 — Défi : la plus petite taille d'échantillon qui garantit une moyenne à ± 0,05 avec 99 %, vérifiée sur une loi défavorable

**Réponse** : `681`.

**Démarche.** Pour chaque $n$ de 1 à 3 000, la probabilité exacte : `stats.binom.pmf(k, n, 0.5)` sur `k = np.arange(n + 1)`, sommée sur les $k$ tels que $10\,\lvert 2k - n \rvert \ge n$ (la condition $\lvert \frac{k}{n} - \frac{1}{2} \rvert \ge 0{,}05$ écrite en entiers). Puis on part de 3 000 et l'on descend tant que la probabilité reste au plus 0,01. La probabilité passe une première fois sous 1 % à $n = 651$, mais remonte au-dessus pour $n$ = 665, 667, 669, 678 et 680 (des $n$ où un $k$ tombe pile sur la frontière, et compte) ; d'où $n_0 = 681$. En flottants, $\lvert k/n - 0{,}5 \rvert$ vaut parfois 0,04999999… au lieu de 0,05, et l'on trouve 679. Hoeffding demande 1 060, plus d'une fois et demie plus : elle vaut pour **toute** loi de $[0, 1]$ et pour tout $n$, avec une marge ; l'approximation normale (664) tombe près de la vraie valeur, sans garantie. Pour $n_0 = 681$, la probabilité vaut 0,0091 pour $p = 0{,}5$, 0,0044 pour $p = 0{,}3$ et 0,00002 pour $p = 0{,}1$ : la loi la plus dispersée est la plus défavorable.

**Erreurs fréquentes.** S'arrêter au premier $n$ qui marche (651) ; comparer des flottants à la frontière (679) ; rendre la valeur de Hoeffding ou du TCL ; oublier un des deux côtés de l'écart.
