# M08 · Tests statistiques — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M08.Q1 — Ce qu'une p-valeur est, et ce qu'elle n'est pas
1. **(B)** : la probabilité, calculée en supposant $H_0$ vraie, d'observer des données au moins aussi extrêmes que celles qu'on a.
2. **Faux** : la p-valeur se calcule **en supposant** $H_0$ vraie ; elle ne peut pas dire la probabilité que $H_0$ le soit.
3. **Faux** : une grande p-valeur dit seulement que les données sont compatibles avec $H_0$. Un test peu puissant (peu de données) donne souvent une grande p-valeur alors que l'effet existe.
4. **Vrai** : sous $H_0$, une p-valeur continue suit la loi uniforme sur $[0, 1]$ (M08.10).
5. L'étude sur 5 000 personnes : l'erreur type est 10 fois plus petite, la statistique 10 fois plus grande pour le même effet.
6. **Faux** : avec des millions de données, un effet minuscule donne une p-valeur minuscule. La taille de l'effet se lit sur un intervalle, pas sur la p-valeur.

### M08.Q2 — Unilatéral ou bilatéral ?
1. **Unilatéral**, si ce sens est fixé **avant** de voir les données (le protocole dit « plus rapide »).
2. **Bilatéral** : un écart dans un sens ou dans l'autre compte.
3. Environ **0,0414** : pour $p_0 = \frac{1}{2}$, la loi est symétrique, et la p-valeur bilatérale est le double de l'unilatérale.
4. **Faux** : ce n'est vrai que si la loi est symétrique. Sinon, on additionne les issues au plus aussi probables que l'observation (fiche §2 : 0,0432 et non 0,0863 dans l'exemple de $p_0 = 0{,}1$).
5. Choisir le côté après avoir vu les données revient à faire les deux tests unilatéraux et à garder le meilleur : le risque de type I réel est le **double** du seuil annoncé.
6. **Vrai** : les issues plus extrêmes que l'observation, dans son sens, sont toutes au plus aussi probables qu'elle ; la p-valeur bilatérale les contient toutes, et d'autres encore.

### M08.Q3 — Permuter quoi, et sous quelle hypothèse ?
1. Sous $H_0$ : « les deux groupes viennent de la même loi ». Les valeurs sont alors **échangeables** : le groupe d'une valeur ne dit rien d'elle.
2. $\binom{7}{3} = 35$.
3. $\frac{12 + 1}{999 + 1} = 0{,}013$.
4. **Faux** : il ne suppose aucune loi ; seulement l'échangeabilité sous $H_0$.
5. Dans chaque paire, on échange les deux mesures « avant » et « après », ce qui revient à changer le signe de chaque différence au hasard. On ne mélange pas les serveurs entre eux.
6. La répartition observée est l'une des répartitions possibles : elle est au moins aussi extrême qu'elle-même. On la compte, d'où $\frac{C + 1}{B + 1} > 0$ ; une p-valeur nulle prétendrait une certitude qu'un tirage au hasard ne peut pas donner.

### M08.Q4 — Erreurs de type I et II, puissance : associer
1. **Type I** (fausse alarme) : on rejette $H_0$, « pas de feu », alors qu'elle est vraie.
2. **Type II** : on ne rejette pas $H_0$ alors que l'effet existe.
3. L'erreur de **type I** : $\alpha = P(\text{rejeter } H_0 \mid H_0 \text{ vraie})$.
4. Puissance $= 1 - \beta$.
5. Elle **augmente**, vers 1.
6. **Vrai** : une règle plus sévère rejette moins souvent, aussi quand $H_1$ est vraie.

### M08.Q5 — Comparaisons multiples : vrai ou faux
1. $100 \times 0{,}05 = 5$.
2. **Faux** : elle repose sur l'inégalité de Boole, vraie pour des événements quelconques (M08.11).
3. $\frac{0{,}05}{25} = 0{,}002$.
4. $\min(1, 5 \times 0{,}012) = 0{,}06$.
5. **Faux** : chaque test devient plus sévère, donc **moins** puissant. C'est le prix de la garantie sur la famille.
6. **Vrai** : 25 tests ont été faits, même si un seul est publié. Avec 25 tests au seuil de 5 %, on attend plus d'un faux positif si aucun indicateur n'a d'effet : le plus significatif a de bonnes chances d'en être un. Il faut compter les 25 tests (Bonferroni) ou confirmer sur de nouvelles données.

### M08.Q6 — AIC, BIC, facteur de Bayes : qui pénalise quoi ?
1. $\mathrm{AIC} = 2k - 2\ln L$ et $\mathrm{BIC} = k\ln n - 2\ln L$.
2. Le **BIC** : chaque paramètre coûte $\ln 1000 \approx 6{,}9$, contre 2 pour l'AIC.
3. **Faux** : on préfère le plus **petit** AIC.
4. $\frac{5}{5 + 1} = \frac{5}{6} \approx 0{,}83$ : la cote a posteriori vaut $5 \times 1 = 5$.
5. **Vrai** : le grand modèle peut reproduire le petit (en fixant ses paramètres en trop), donc son maximum est au moins aussi haut.
6. L'évidence est la **moyenne** de la vraisemblance sous la loi a priori : un modèle souple répartit sa probabilité sur beaucoup de données possibles, et en donne peu à celles qu'on a observées (le rasoir d'Occam, fiche §7).

<a id="rappels"></a>

## 🔁 Rappels

### M08.R1 — La loi binomiale (M02b)
1. $\binom{5}{2}\,0{,}4^2 \times 0{,}6^3 = 10 \times 0{,}16 \times 0{,}216 = 0{,}3456$.
2. $np = 2$.
3. $np(1 - p) = 1{,}2$.
4. $1 - 0{,}6^5 = 1 - 0{,}07776 = 0{,}92224$.
5. Un nombre fixé $n$ d'essais **indépendants**, chacun à deux issues, avec la **même** probabilité de succès $p$.

### M08.R2 — L'intervalle de confiance d'une moyenne (M02c)
1. $\frac{4{,}2}{\sqrt{36}} = 0{,}7$.
2. $1{,}96 \times 0{,}7 = 1{,}372$.
3. $[17{,}128 ;\ 19{,}872]$.
4. $1{,}645 \times 0{,}7 \approx 1{,}15$.
5. Il faut $1{,}96 \times \frac{4{,}2}{\sqrt{n}} \le 0{,}5$, soit $n \ge \big(\frac{1{,}96 \times 4{,}2}{0{,}5}\big)^2 \approx 271{,}1$ : **272** mesures.

### M08.R3 — Vraisemblance et log-vraisemblance (M04)
1. $L(p) = p^3(1 - p)^5$.
2. $\ln L(p) = 3\ln p + 5\ln(1 - p)$.
3. La dérivée $\frac{3}{p} - \frac{5}{1 - p}$ s'annule en $p = \frac{3}{8}$ (la proportion observée).
4. $3\ln\frac{3}{8} + 5\ln\frac{5}{8} \approx -5{,}2925$.
5. $\ln L(\frac{1}{2}) = 8\ln\frac{1}{2} \approx -5{,}5452$ : plus bas d'environ **0,2527** (en partant de valeurs arrondies à 3 décimales, on trouverait 0,252).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M08.1 — Un test binomial à la main : un algorithme de compression est-il plus rapide sur douze fichiers ?

**Réponses** : a) `"33/2048"` · b) `"79/4096"` · c) `"79/2048"` · d) `True` · e) `False` · f) `10` · g) `0.010`.

**Démarche.** $H_0$ : sur chaque fichier, chaque algorithme gagne avec la probabilité $\frac{1}{2}$, indépendamment ; $H_1$ : le nouveau gagne plus souvent ($p > \frac{1}{2}$). Sous $H_0$, $K$ suit $\mathcal{B}(12, \frac{1}{2})$.
- a) $P(K = 10) = \binom{12}{10}\frac{1}{2^{12}} = \frac{66}{4096} = \frac{33}{2048}$.
- b) $P(K \ge 10) = \frac{66 + 12 + 1}{4096} = \frac{79}{4096} \approx 0{,}0193$.
- c) La loi est symétrique : les issues aussi extrêmes de l'autre côté sont $K \le 2$, de même probabilité. $\frac{79}{2048} \approx 0{,}0386$.
- d) et e) $0{,}0386 \le 0{,}05$ : on rejette à 5 % ; $0{,}0386 > 0{,}01$ : pas à 1 %.
- f) $P(K \ge 9) = \frac{220 + 79}{4096} = \frac{299}{4096} \approx 0{,}073 > 0{,}05$, et $P(K \ge 10) \approx 0{,}019 \le 0{,}05$ : il faut gagner au moins **10** fichiers.
- g) $z = \frac{10 - 6}{\sqrt{3}} \approx 2{,}31$ ($\mathbb{E}[K] = 6$, $\sigma = \sqrt{12 \times \frac{1}{4}} = \sqrt{3}$), et $1 - \Phi(2{,}31) \approx 0{,}010$.

Pour la copie : l'approximation normale (0,010) est deux fois trop petite à côté de la valeur exacte (0,019) : avec 12 essais, la loi binomiale est trop discrète. Avec la **correction de continuité**, $z = \frac{9{,}5 - 6}{\sqrt{3}} \approx 2{,}02$ et $1 - \Phi(2{,}02) \approx 0{,}022$, bien plus proche. Une égalité ne dit rien sur le sens de l'écart : on l'écarte, et le test porte sur les 12 autres fichiers (c'est le **test du signe**).

**Erreurs fréquentes.** Oublier le coefficient binomial (a : $\frac{1}{4096}$) ; ne garder que $K = 10$ (b) ou que $K > 10$ ; oublier l'autre côté en bilatéral (c) ; utiliser la p-valeur unilatérale pour décider en d) alors que le test est bilatéral ; donner $\Phi(z)$ au lieu de $1 - \Phi(z)$ (g).

**Variante.** Le nouvel algorithme gagne sur 11 fichiers sur 12 : p-valeur unilatérale ? *Réponse* : $\frac{12 + 1}{4096} = \frac{13}{4096} \approx 0{,}0032$.

### Ex M08.2 — Un test par permutation exhaustif : deux groupes de trois mesures, vingt répartitions

**Réponses** : a) `20` · b) `-5` · c) `"1/20"` · d) `"1/10"` · e) `False` · f) `70` · g) `0.001`.

**Démarche.** La somme des six temps vaut $12 + 15 + 14 + 18 + 21 + 17 = 97$. Si $S_A$ est la somme du groupe A, $\bar{x}_A = \frac{S_A}{3}$ et $\bar{x}_B = \frac{97 - S_A}{3}$, donc $t = \frac{2S_A - 97}{3}$ : $t$ ne dépend que de $S_A$.
- a) Choisir les 3 temps du groupe A parmi 6 : $\binom{6}{3} = 20$.
- b) $\bar{x}_A = \frac{41}{3}$, $\bar{x}_B = \frac{56}{3}$, $t = -5$.
- Les 20 valeurs de $S_A$ : 41, 43, 44, 44, 45, 46, 47, 47, 47, 48, 49, 50, 50, 50, 51, 52, 53, 53, 54, 56. L'observation, $S_A = 41$, est la **plus petite** : les trois temps les plus courts sont tous dans le groupe A.
- c) Une seule répartition sur 20 a $t \le -5$ : $p = \frac{1}{20}$.
- d) $|t| \ge 5$ pour $S_A = 41$ et $S_A = 56$ ($t = 5$) : $\frac{2}{20} = \frac{1}{10}$.
- e) **Faux** : en bilatéral, l'observation la plus extrême et sa symétrique donnent toujours au moins $\frac{2}{20} = 0{,}1 > 0{,}05$. Avec deux groupes de trois, aucun résultat ne peut être significatif à 5 % en bilatéral.
- f) $\binom{8}{4} = 70$.
- g) $\frac{0 + 1}{999 + 1} = 0{,}001$.

Pour la copie : quelles que soient les mesures (toutes différentes), la répartition la plus extrême et son image miroir (les groupes échangés) sont au moins aussi extrêmes en valeur absolue : la p-valeur bilatérale vaut au moins $\frac{2}{20}$. Il faut plus de mesures : avec deux groupes de quatre, le minimum devient $\frac{2}{70} \approx 0{,}029$.

**Erreurs fréquentes.** Compter des arrangements ordonnés (a : 120) ou diviser par 2 (a : 10) ; inverser le sens de $t$ (b : 5) ; oublier de compter l'observation elle-même (c : 0) ; oublier l'autre côté (d) ; annoncer $p = 0$ en g).

**Variante.** Avec 12, 15, 14 contre 18, 21, 13 (le 17 remplacé par 13), la p-valeur unilatérale ? *Réponse* : $t = \frac{41 - 52}{3} = -\frac{11}{3}$ ; la somme vaut 93, et $S_A = 39$ (12, 13, 14) et $S_A = 40$ (12, 13, 15) donnent aussi $t \le -\frac{11}{3}$ : $p = \frac{3}{20}$.

### Ex M08.3 — Erreur de type I, erreur de type II et puissance d'un test binomial

**Réponses** : a) `"235/8192"` · b) `0.698` · c) `0.302` · d) `"1471/16384"` · e) `0.870` · f) `11`.

**Démarche.** Sous $H_0$, $K \sim \mathcal{B}(14, \frac{1}{2})$ ; sous l'alternative, $K \sim \mathcal{B}(14 ;\ 0{,}8)$.
- a) $P_{H_0}(K \ge 11) = \frac{\binom{14}{11} + \binom{14}{12} + \binom{14}{13} + \binom{14}{14}}{2^{14}} = \frac{364 + 91 + 14 + 1}{16\,384} = \frac{470}{16\,384} = \frac{235}{8192} \approx 0{,}0287$.
- b) $P_{0{,}8}(K \ge 11) = \sum_{j=11}^{14}\binom{14}{j}0{,}8^j\,0{,}2^{14-j} \approx 0{,}2501 + 0{,}2501 + 0{,}1539 + 0{,}0440 \approx 0{,}698$.
- c) $\beta = 1 - 0{,}698 = 0{,}302$.
- d) On ajoute $K = 10$ : $\frac{470 + 1001}{16\,384} = \frac{1471}{16\,384} \approx 0{,}0898$.
- e) On ajoute $P_{0{,}8}(K = 10) \approx 0{,}1720$ : $\approx 0{,}870$.
- f) La règle $K \ge 10$ a un risque de 0,090 > 0,05, la règle $K \ge 11$ de 0,029 : $c = 11$.

Pour la copie : passer de $K \ge 11$ à $K \ge 10$ gagne de la puissance (0,698 → 0,870) mais triple le risque de type I (0,029 → 0,090), au-dessus de 5 %. La loi est discrète : les risques possibles sautent de 0,0065 ($K \ge 12$) à 0,029 puis 0,090, sans passer par 0,05. Pour gagner en puissance sans augmenter $\alpha$, il faut **plus de paires de tasses**.

**Erreurs fréquentes.** Oublier l'issue $K = 11$ (a : $\frac{53}{8192}$) ; calculer la puissance sous $H_0$ ; confondre $\beta$ et la puissance ; ne prendre que $K = 10$ en d).

**Variante.** La puissance de la règle $K \ge 12$ contre $p = 0{,}8$ ? *Réponse* : $\approx 0{,}448$, avec un risque de type I de $\frac{53}{8192} \approx 0{,}0065$.

### Ex M08.4 — Combien d'observations pour une puissance de 80 % ? (approximation normale)

**Réponses** : a) `1.645` · b) `0.842` · c) `99` · d) `126` · e) `396` · f) `0.44`.

**Démarche.** La formule de la fiche (§4) : $n \ge \Big(\frac{(z_{1-\alpha} + z_{1-\beta})\,\sigma}{\delta}\Big)^2$.
- a) $z_{0{,}95} \approx 1{,}645$ ; b) $z_{0{,}80} \approx 0{,}842$.
- c) $\big((1{,}645 + 0{,}842) \times \frac{8}{2}\big)^2 = (9{,}948)^2 \approx 98{,}96$ : on arrondit **au-dessus**, 99.
- d) En bilatéral, $z_{0{,}975} = 1{,}960$ : $\big(2{,}802 \times 4\big)^2 \approx 125{,}6$, soit 126.
- e) $\delta = 1$ : $\big(2{,}487 \times 8\big)^2 \approx 395{,}9$, soit 396.
- f) Puissance $= \Phi\big(\frac{\delta\sqrt{n}}{\sigma} - z_{0{,}95}\big) = \Phi(1{,}5 - 1{,}645) = \Phi(-0{,}145) \approx 0{,}44$.

Pour la copie : $n$ dépend de $\frac{\sigma^2}{\delta^2}$ ; diviser l'effet par 2 multiplie $n$ par 4. Avec 36 mesures, la puissance n'est que de 44 % : un test non significatif ne dit presque rien (on manquerait l'effet plus d'une fois sur deux). Il faut le dire : « pas d'effet détecté », pas « pas d'effet ».

**Erreurs fréquentes.** Prendre $z_{0{,}975}$ pour un test unilatéral ; arrondir au-dessous (98) ; oublier le carré (10) ; doubler $n$ au lieu de le quadrupler (e : 198) ; oublier $\sqrt{n}$ dans la puissance.

**Variante.** Avec $\sigma = 6$ ms (tout le reste comme en c)) ? *Réponse* : $(2{,}487 \times 3)^2 \approx 55{,}7$, soit 56 mesures.

### Ex M08.5 — L'intervalle d'une proportion : Wald contre Wilson, avec peu de succès

**Réponses** : a) `0.06` · b) `-0.0058` · c) `[0, 0.1258]` · d) `[0.0206, 0.1622]` · e) `0.0914` · f) `0.0602`.

**Démarche.**
- a) $\hat{p} = \frac{3}{50} = 0{,}06$.
- b) Demi-largeur de Wald : $1{,}96\sqrt{\frac{0{,}06 \times 0{,}94}{50}} = 1{,}96 \times 0{,}03359 \approx 0{,}0658$ ; borne basse $0{,}06 - 0{,}0658 \approx -0{,}0058$, **négative**.
- c) Ramené dans $[0, 1]$ : $[0 ;\ 0{,}1258]$.
- d) Wilson : $\frac{z^2}{n} = 0{,}07683$, dénominateur $1{,}07683$ ; centre $\frac{0{,}06 + 0{,}03842}{1{,}07683} \approx 0{,}0914$ ; demi-largeur $\frac{1{,}96\sqrt{0{,}001128 + 0{,}0003842}}{1{,}07683} \approx 0{,}0708$ ; d'où $[0{,}0206 ;\ 0{,}1622]$.
- e) $\approx 0{,}0914$ : le centre est tiré vers $\frac{1}{2}$.
- f) $k = 0$, $n = 60$ : la borne haute vaut $\frac{z^2}{n + z^2} = \frac{3{,}8416}{63{,}8416} \approx 0{,}0602$ (M08.12, question 5).

Pour la copie : Wald donne $[0, 0]$ pour 0 erreur sur 60, comme si l'on était sûr que le détecteur ne se trompe jamais : absurde après 60 cas. La règle empirique « de trois » donne $\frac{3}{60} = 0{,}05$, du même ordre que Wilson (0,060).

**Erreurs fréquentes.** Oublier la racine dans la demi-largeur ; laisser une borne négative ; centrer Wilson sur $\hat{p}$ ; répondre $[0, 0]$ en f).

**Variante.** L'intervalle de Wilson pour 3 erreurs sur 200 ? *Réponse* : environ $[0{,}0051 ;\ 0{,}0432]$, alors que Wald donnerait $[0 ;\ 0{,}0318]$.

### Ex M08.6 — L'intervalle de Student d'une différence appariée : un serveur avant et après une mise à jour

**Réponses** : a) `3.5` · b) `2.0736` · c) `0.847` · d) `2.571` · e) `[1.32, 5.68]` · f) `2.82` · g) `False` · h) `"1/64"`.

**Démarche.** Les différences valent $d = (4, 1, 6, 1, 4, 5)$.
- a) $\bar{d} = \frac{21}{6} = 3{,}5$.
- b) Les écarts à la moyenne, $0{,}5 ;\ -2{,}5 ;\ 2{,}5 ;\ -2{,}5 ;\ 0{,}5 ;\ 1{,}5$, ont des carrés de somme 21,5 : $s_d^2 = \frac{21{,}5}{5} = 4{,}3$ et $s_d \approx 2{,}0736$.
- c) $\frac{2{,}0736}{\sqrt{6}} \approx 0{,}847$.
- d) Loi de Student à $6 - 1 = 5$ degrés de liberté, quantile d'ordre 0,975 : $2{,}571$.
- e) $3{,}5 \pm 2{,}571 \times 0{,}8466 = 3{,}5 \pm 2{,}18$ : $[1{,}32 ;\ 5{,}68]$.
- f) $s^2_{\text{avant}} \approx 28{,}67$, $s^2_{\text{après}} \approx 18{,}97$ : $\sqrt{\frac{28{,}67 + 18{,}97}{6}} \approx 2{,}82$.
- g) **Faux** : les deux bornes sont positives.
- h) Sous $H_0$, chacune des six différences peut prendre un signe ou l'autre : $2^6 = 64$ combinaisons, aussi probables. Les six différences observées sont toutes positives : changer un seul signe fait baisser la moyenne. Seule la combinaison observée atteint 3,5 : $p = \frac{1}{64} \approx 0{,}016$.

Pour la copie : les routes diffèrent beaucoup entre elles (de 45 à 61 ms) ; sans appariement, cette variabilité entre routes entre dans l'erreur type, alors qu'elle n'a rien à voir avec la mise à jour. En travaillant sur les différences, chaque route sert de témoin à elle-même. Sans appariement, l'intervalle serait $3{,}5 \pm t \times 2{,}82$, environ $[-2{,}8 ;\ 9{,}8]$ avec $t \approx 2{,}24$ (la méthode de Welch, hors programme) : il contient 0 quel que soit le quantile choisi, et l'on conclurait à tort qu'on ne voit pas d'effet. En h), il y a 64 combinaisons de signes, et l'observation est la plus extrême possible : $\frac{1}{64}$ est la plus petite p-valeur unilatérale que ce test peut donner avec six paires.

**Erreurs fréquentes.** $\mathrm{ddof} = 0$ (b : 1,893) ; diviser par $n$ au lieu de $\sqrt{n}$ ; prendre 1,96 ou 6 degrés de liberté (d) ; prendre le quantile d'ordre 0,95 ; compter les deux côtés en h) ($\frac{2}{64}$), ou oublier la combinaison observée (0).

**Variante.** L'intervalle à 90 % ? *Réponse* : $t_{5 ;\ 0{,}95} \approx 2{,}015$, d'où $3{,}5 \pm 1{,}71$, soit $[1{,}79 ;\ 5{,}21]$.

### Ex M08.7 — Vingt tests au seuil de 5 % : les faux positifs attendus, puis Bonferroni

**Réponses** : a) `1` · b) `0.6415` · c) `0.0025` · d) `0.0488` · e) `[0.02, 0.08, 0.6]` · f) `1`.

**Démarche.**
- a) Chaque test donne un faux positif avec la probabilité 0,05 ; l'espérance d'une somme est la somme des espérances : $20 \times 0{,}05 = 1$.
- b) $1 - P(\text{aucun}) = 1 - 0{,}95^{20} \approx 0{,}6415$.
- c) $\frac{0{,}05}{20} = 0{,}0025$.
- d) $1 - 0{,}9975^{20} \approx 0{,}0488$, juste sous 0,05.
- e) $20 \times 0{,}001 = 0{,}02$, $20 \times 0{,}004 = 0{,}08$, $20 \times 0{,}03 = 0{,}6$.
- f) Seule la première est au plus 0,05 : **1** feature.

Pour la copie : sans correction, 3 features (les trois p-valeurs sont sous 0,05). La correction garantit que la probabilité de déclarer **au moins une** fausse feature reste sous 5 % ; elle ne garantit pas de trouver les vraies. Une feature vraiment liée de p-valeur 0,004 n'est pas déclarée (p-valeur ajustée 0,08) : c'est une erreur de type II, le prix de la garantie.

**Erreurs fréquentes.** $20 \times 0{,}05 = 1$ comme **probabilité** d'au moins un faux positif (b) ; donner $0{,}95^{20}$, la probabilité d'aucun ; multiplier le seuil au lieu de le diviser (c) ; diviser les p-valeurs au lieu de les multiplier (e) ; prendre $m = 3$, le nombre de p-valeurs citées, au lieu de 20.

**Variante.** Avec 50 tests, le seuil de Bonferroni et la probabilité d'au moins un faux positif sans correction ? *Réponse* : 0,001 et $1 - 0{,}95^{50} \approx 0{,}923$.

### Ex M08.8 — L'AIC et le BIC de deux modèles, à partir de leurs log-vraisemblances

**Réponses** : a) `831.2` · b) `824.2` · c) `841.1` · d) `847.3` · e) `2` · f) `1` · g) `10.597`.

**Démarche.**
- a) $2 \times 3 - 2 \times (-412{,}6) = 6 + 825{,}2 = 831{,}2$ ; b) $14 + 810{,}2 = 824{,}2$.
- c) $3\ln 200 + 825{,}2 \approx 15{,}89 + 825{,}2 \approx 841{,}1$ ; d) $7\ln 200 + 810{,}2 \approx 37{,}09 + 810{,}2 \approx 847{,}3$.
- e) Le plus petit AIC : le modèle 2. f) Le plus petit BIC : le modèle 1.
- g) Le BIC préfère le modèle 2 quand $7\ln 200 - 2\ln L_2 < 3\ln 200 - 2\ln L_1$, soit $\ln L_2 - \ln L_1 > 2\ln 200 \approx 10{,}597$.

Pour la copie : $\mathrm{AIC}_1 - \mathrm{AIC}_2 = 2(\ln L_2 - \ln L_1) - 2(k_2 - k_1) = 15 - 8 = 7 > 0$ : le gain d'ajustement (15) dépasse la pénalité (8). Pour le BIC, la pénalité vaut $4\ln 200 \approx 21{,}2$ : elle l'emporte. Le BIC fait payer chaque paramètre $\ln 200 \approx 5{,}3$, l'AIC seulement 2 : avec beaucoup d'observations, le BIC préfère les modèles plus simples.

**Erreurs fréquentes.** Un signe perdu ($2k + 2\ln L$) ; le logarithme décimal dans le BIC (c : 832,1) ; préférer le plus grand critère ; oublier le facteur 2 en g) (21,193).

**Variante.** Avec $n = 30$ au lieu de 200 (mêmes log-vraisemblances), quel modèle le BIC choisit-il ? *Réponse* : $4\ln 30 \approx 13{,}6 < 15$ : le modèle 2.

### Ex M08.9 — Un facteur de Bayes entre deux taux de clics

**Réponses** : a) `0.107` · b) `0.125` · c) `1.17` · d) `0.28` · e) `"1/41"` · f) `4.4`.

**Démarche.**
- a) $P(6 \mid M_A) = \binom{40}{6}\,0{,}1^6\,0{,}9^{34} \approx 3\,838\,380 \times 10^{-6} \times 0{,}02781 \approx 0{,}107$.
- b) $\binom{40}{6}\,0{,}2^6\,0{,}8^{34} \approx 0{,}125$.
- c) $\mathrm{BF}_{BA} = \frac{0{,}1246}{0{,}1068} \approx 1{,}17$ (le coefficient binomial se simplifie : $2^6 \times \big(\frac{8}{9}\big)^{34}$).
- d) Cote a posteriori $= 1{,}167 \times \frac{1}{3} \approx 0{,}389$, probabilité $\frac{0{,}389}{1{,}389} \approx 0{,}28$.
- e) En moyennant $\binom{40}{6}p^6(1 - p)^{34}$ sur $p$ uniforme, on trouve la même valeur pour chacun des 41 résultats possibles (0 à 40 clics), comme pour la pièce de la fiche : $\frac{1}{41}$.
- f) $\mathrm{BF}_{AC} = 0{,}1068 \times 41 \approx 4{,}4$.

Pour la copie : la vraisemblance est maximale en $\hat{p} = \frac{6}{40} = 0{,}15$, entre les deux taux. $M_C$ contient ce taux, mais il répartit sa probabilité sur tous les taux de 0 à 1, dont la plupart expliquent mal 6 clics sur 40 : son évidence est la moyenne de la vraisemblance, pas son maximum. c) Un facteur de Bayes de 1,17 est très faible : les données ne départagent presque pas $M_A$ et $M_B$, et la cote a priori garde l'essentiel du poids.

**Erreurs fréquentes.** Inverser le facteur de Bayes (c : 0,86) ; oublier la cote a priori (d : 0,54) ou rendre la cote au lieu de la probabilité (d : 0,39) ; compter 40 résultats possibles au lieu de 41 (e).

**Variante.** Avec 4 clics sur 40, $\mathrm{BF}_{BA}$ ? *Réponse* : $2^4 \times \big(\frac{8}{9}\big)^{36} \approx 0{,}23$ : cette fois les données favorisent $M_A$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M08.10 — Sous H0, une p-valeur continue suit la loi uniforme

**Réponse modèle.**
1. Pour une observation $t$, la p-valeur est $P_{H_0}(T \ge t) = 1 - P_{H_0}(T < t) = 1 - F(t)$, car $P(T = t) = 0$ pour une loi continue. Vue comme une variable aléatoire (on remplace $t$ par $T$) : $P = 1 - F(T)$.
2. $F$ est continue et strictement croissante : c'est une bijection de l'ensemble des valeurs de $T$ sur $]0, 1[$. Pour $v \in\, ]0, 1[$, $F(T) \le v \iff T \le F^{-1}(v)$, donc $P\big(F(T) \le v\big) = F\big(F^{-1}(v)\big) = v$ ; pour $v = 0$ et $v = 1$, les deux membres valent 0 et 1. Alors $P(P \le u) = P\big(F(T) \ge 1 - u\big) = 1 - P\big(F(T) < 1 - u\big) = 1 - (1 - u) = u$, car $F(T)$ a une loi continue (uniforme), et $P\big(F(T) = 1 - u\big) = 0$. La p-valeur suit la loi uniforme sur $[0, 1]$.
3. Le risque de type I est $P_{H_0}(\text{rejeter}) = P_{H_0}(P \le \alpha) = \alpha$, exactement.
4. Pour $K \sim \mathcal{B}(3, \frac{1}{2})$ : $k = 0$ donne $p = 1$ (probabilité $\frac{1}{8}$), $k = 1$ donne $\frac{7}{8}$ (probabilité $\frac{3}{8}$), $k = 2$ donne $\frac{1}{2}$ ($\frac{3}{8}$), $k = 3$ donne $\frac{1}{8}$ ($\frac{1}{8}$). $P(P \le 0{,}2) = P(K = 3) = \frac{1}{8} = 0{,}125 < 0{,}2$. Pour une loi discrète, on a seulement $P(P \le u) \le u$ : le test est **conservateur**, son risque réel est au plus le seuil annoncé.
5. Sous $H_0$, un histogramme **plat** (aux fluctuations près, environ 500 p-valeurs par barre de largeur 0,05). Sous une alternative, les p-valeurs s'entassent près de 0, d'autant plus que la puissance est grande (M08.21).

**Grille.** (1) $P = 1 - F(T)$, avec l'argument $P(T = t) = 0$ ; (2) l'inversion de $F$ pour $F(T)$, puis le passage à $P$ par le complément ; (3) la conclusion sur le risque de type I ; (4) les quatre p-valeurs, leurs probabilités, $\frac{1}{8} \le 0{,}2$, et le mot « conservateur » ; (5) plat sous $H_0$, entassé près de 0 sous $H_1$.

### Ex M08.11 — L'inégalité de Boole et la garantie de Bonferroni, sans hypothèse d'indépendance

**Réponse modèle.**
1. $A \cup B$ est la réunion **disjointe** de $A$ et de $B \setminus A$ : $P(A \cup B) = P(A) + P(B \setminus A) \le P(A) + P(B)$, car $B \setminus A \subset B$.
2. Pour $m = 1$, c'est une égalité. Si l'inégalité est vraie pour $m$ événements, alors $P(A_1 \cup \cdots \cup A_{m+1}) = P\big((A_1 \cup \cdots \cup A_m) \cup A_{m+1}\big) \le P(A_1 \cup \cdots \cup A_m) + P(A_{m+1}) \le P(A_1) + \cdots + P(A_{m+1})$, par 1 puis par l'hypothèse de récurrence.
3. Pour chacune des $m_0$ hypothèses nulles vraies, soit $A_i$ l'événement « on rejette $H_{0,i}$ » : comme le test est au seuil $\frac{\alpha}{m}$ et que $H_{0,i}$ est vraie, $P(A_i) \le \frac{\alpha}{m}$. Par 2, $P(\text{au moins un faux rejet}) \le m_0\,\frac{\alpha}{m} \le \alpha$. L'indépendance n'a servi **nulle part** : l'inégalité de Boole est vraie pour des événements quelconques.
4. Quand les événements sont deux à deux incompatibles (plus précisément, quand $P(A_i \cap A_j) = 0$ pour $i \ne j$) : rien n'est compté deux fois.
5. Pour $m = 1$, égalité. Si $(1 - x)^m \ge 1 - mx$, alors, comme $1 - x \ge 0$, $(1 - x)^{m+1} \ge (1 - mx)(1 - x) = 1 - (m + 1)x + mx^2 \ge 1 - (m + 1)x$. Avec $x = \frac{\alpha}{m}$ : $1 - \big(1 - \frac{\alpha}{m}\big)^m \le 1 - (1 - \alpha) = \alpha$, la même garantie.
6. Si $m\,p_i \ge 1$, la p-valeur ajustée vaut 1, plus grand que $\alpha$, et $p_i \ge \frac{1}{m} > \frac{\alpha}{m}$ : les deux règles ne rejettent pas. Sinon, $\min(1, m\,p_i) = m\,p_i \le \alpha \iff p_i \le \frac{\alpha}{m}$. Les deux règles prennent les mêmes décisions.

**Grille.** (1) la réunion disjointe ; (2) une récurrence complète (initialisation, hérédité, utilisation de 1) ; (3) les événements bien définis, $m_0 \le m$, et la remarque sur l'indépendance ; (4) le cas d'égalité ; (5) la récurrence, avec l'argument $1 - x \ge 0$ pour multiplier une inégalité ; (6) les deux cas.

### Ex M08.12 — L'intervalle de Wilson, en inversant le test d'une proportion

**Réponse modèle.**
1. Les deux membres de $|\hat{p} - p_0| \le z\sqrt{\frac{p_0(1 - p_0)}{n}}$ sont positifs ou nuls : on peut les élever au carré sans changer le sens, $(\hat{p} - p_0)^2 \le \frac{z^2}{n}\,p_0(1 - p_0)$.
2. $\hat{p}^2 - 2\hat{p}p_0 + p_0^2 \le \frac{z^2}{n}p_0 - \frac{z^2}{n}p_0^2$, soit $a\,p_0^2 + b\,p_0 + c \le 0$ avec $a = 1 + \frac{z^2}{n}$, $b = -\big(2\hat{p} + \frac{z^2}{n}\big)$, $c = \hat{p}^2$.
3. $\Delta = \big(2\hat{p} + \frac{z^2}{n}\big)^2 - 4\big(1 + \frac{z^2}{n}\big)\hat{p}^2 = \frac{4z^2}{n}\hat{p}(1 - \hat{p}) + \frac{z^4}{n^2} = 4z^2\Big(\frac{\hat{p}(1 - \hat{p})}{n} + \frac{z^2}{4n^2}\Big) \ge 0$. Comme $a > 0$, le trinôme est négatif ou nul entre ses racines : $p_0 = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{\hat{p} + \frac{z^2}{2n} \pm z\sqrt{\frac{\hat{p}(1 - \hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}$, la formule de la fiche.
4. Le trinôme vaut $c = \hat{p}^2 \ge 0$ en 0 et $a + b + c = (1 - \hat{p})^2 \ge 0$ en 1. Son sommet, $-\frac{b}{2a} = \frac{2\hat{p} + z^2/n}{2(1 + z^2/n)}$, est entre 0 et 1 (car $2\hat{p} \le 2 + \frac{z^2}{n}$). Le trinôme est négatif entre les racines et positif ou nul en 0 et en 1, de part et d'autre du sommet : 0 est à gauche de la petite racine, et 1 à droite de la grande. Les deux bornes sont dans $[0, 1]$.
5. Pour $k = 0$, $c = 0$ : les racines sont 0 et $\frac{z^2/n}{1 + z^2/n} = \frac{z^2}{n + z^2}$. L'intervalle est $\big[0 ;\ \frac{z^2}{n + z^2}\big]$, de largeur non nulle (Wald donnait $[0, 0]$).
6. $\hat{p} = 0{,}08$, $\frac{z^2}{n} = 0{,}1537$ : centre $\frac{0{,}08 + 0{,}0768}{1{,}1537} \approx 0{,}1359$, demi-largeur $\frac{1{,}96\sqrt{0{,}002944 + 0{,}001537}}{1{,}1537} \approx 0{,}1137$, d'où $[0{,}022 ;\ 0{,}250]$, comme dans la fiche.

**Grille.** (1) la justification du passage au carré ; (2) $a$, $b$, $c$ justes ; (3) le discriminant simplifié, son signe, l'argument « $a > 0$, négatif entre les racines », la formule retrouvée ; (4) le signe en 0 et en 1 et la position du sommet (ou un argument équivalent : la somme et le produit des racines) ; (5) l'intervalle pour $k = 0$ ; (6) la vérification numérique.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M08.13 — Pont : l'importance d'une feature par permutation, sur un petit tableau

**Réponses** : a) `1` · b) `"1/3"` · c) `"2/3"` · d) `"2/3"` · e) `"1/3"` · f) `0`.

**Démarche.**
- a) $x_1 + x_2 = 9, 6, 9, 6, 6, 9$ : les prédictions $1, 0, 1, 0, 0, 1$ sont toutes justes.
- b) $x_1$ décalé devient $2, 7, 3, 5, 4, 6$ ; les sommes $5, 11, 5, 8, 5, 11$ donnent $0, 1, 0, 1, 0, 1$ : justes aux lignes 5 et 6, soit $\frac{2}{6} = \frac{1}{3}$.
- c) $1 - \frac{1}{3} = \frac{2}{3}$.
- d) $x_2$ décalé devient $4, 2, 3, 1, 5, 3$ ; les sommes $10, 4, 10, 4, 10, 7$ donnent $1, 0, 1, 0, 1, 0$ : justes aux lignes 1 à 4, soit $\frac{2}{3}$.
- e) $1 - \frac{2}{3} = \frac{1}{3}$.
- f) Le modèle n'utilise pas $x_3$ : ses prédictions ne changent pas, l'importance est nulle.

Pour la copie : mélanger une colonne garde ses valeurs (sa moyenne, sa dispersion) mais casse son lien avec la cible et avec les autres colonnes, comme le test par permutation casse le lien entre une valeur et son groupe. Un seul mélange est une mesure bruitée (ici, le décalage d'un cran est un mélange particulier) : on mélange plusieurs fois au hasard et l'on fait la moyenne. Sur les données d'entraînement, un modèle qui a appris du bruit par cœur donnerait de l'importance à des features inutiles ; sur un jeu de validation, l'importance mesure ce qui sert vraiment à prédire.

**Erreurs fréquentes.** Décaler dans l'autre sens (ici, le résultat est le même, mais vérifie-le) ; calculer l'accuracy après le mélange moins celle de départ (une importance négative) ; mélanger toutes les colonnes à la fois.

**Variante.** Si le modèle prédisait 1 quand $x_1 \ge 5$ (sans $x_2$), l'importance de $x_2$ ? *Réponse* : 0 ; et l'accuracy de départ vaudrait $\frac{2}{3}$ (les lignes 5 et 6 seraient fausses).

### Ex M08.14 — MML §8.6 : validation croisée imbriquée, sélection bayésienne de modèle et facteur de Bayes

**Réponse modèle.**
1. La boucle **intérieure** choisit le modèle (ou ses hyperparamètres) par validation croisée sur la partie d'entraînement ; la boucle **extérieure** estime, sur des parties qui n'ont servi ni à entraîner ni à choisir, la performance de toute la procédure, choix compris : sur des parties des données que la boucle intérieure n'a jamais vues.
2. Le livre met une loi a priori sur les **modèles** eux-mêmes, en plus de celle des paramètres de chaque modèle. Il compare les modèles par leur probabilité a posteriori, proportionnelle à la loi a priori du modèle fois $p(\mathcal{D} \mid M_k)$, la vraisemblance moyennée sur les paramètres : l'*evidence* (*model evidence*) ou *marginal likelihood*.
3. Un modèle très souple peut expliquer beaucoup de datasets différents : sa probabilité, qui fait 1 au total, est répartie sur eux tous, et chacun en reçoit peu. Pour la pièce de la fiche (7 faces sur 10), le modèle « probabilité inconnue » donne $\frac{1}{11}$ à chacun des 11 résultats, alors que le modèle « pièce équilibrée » concentre sa probabilité près de 5 faces et donne 0,117 à 7 faces : le modèle simple l'emporte, sans pénalité ajoutée à la main.
4. Cote a posteriori $=$ facteur de Bayes $\times$ cote a priori : $4 \times \frac{1}{2} = 2$, et la probabilité a posteriori du premier modèle vaut $\frac{2}{1 + 2} = \frac{2}{3}$.
5. L'**intégrale** sur les paramètres, $\int p(\mathcal{D} \mid \boldsymbol{\theta})\,p(\boldsymbol{\theta} \mid M)\,d\boldsymbol{\theta}$, souvent impossible à calculer exactement en grande dimension. $M_A$ et $M_B$ n'ont aucun paramètre libre (le taux est fixé) : leur évidence est simplement la vraisemblance.
6. Par exemple *nested cross-validation* (validation croisée imbriquée), *marginal likelihood* (vraisemblance marginale), *prior odds* et *posterior odds* (cotes a priori et a posteriori), *Occam's razor* (rasoir d'Occam).

**Grille.** (1) le rôle des deux boucles, et les données sur lesquelles la boucle extérieure mesure la performance ; (2) la loi a priori sur les modèles et les deux noms de $p(\mathcal{D} \mid M)$ ; (3) l'argument « la probabilité totale vaut 1 » et l'exemple de la pièce ; (4) la relation et les deux calculs ; (5) l'intégrale, et l'absence de paramètre libre pour $M_A$ et $M_B$ ; (6) trois mots traduits. Les réponses sont écrites avec tes mots, pas recopiées.

### Ex M08.15 — Expliquer une p-valeur sans dire « la probabilité que H0 soit vraie »

**Réponse modèle.**

> Pas tout à fait. Le test part de l'hypothèse que la nouvelle page ne change rien, puis se demande : si c'était le cas, un écart aussi grand que celui qu'on a vu arriverait-il souvent, juste par hasard ? Réponse : dans 2 % des cas seulement. C'est rare, donc on a de bonnes raisons de croire que la page change quelque chose. Mais 2 % n'est pas la probabilité que la page soit moins bonne : c'est la probabilité de voir un tel écart **si** elle ne changeait rien. Et un résultat net ne veut pas dire un gain important : il peut être réel mais minuscule. Pour savoir combien elle rapporte, il faut regarder l'intervalle du gain.

**Grille.** (1) la supposition « la page ne change rien » ; (2) la p-valeur comme fréquence d'un écart au moins aussi grand, sous cette supposition ; (3) pourquoi ce n'est pas la probabilité que la page soit meilleure ; (4) significatif ne veut pas dire important, et l'intervalle du gain ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M08.E1 — « Votre test donne p = 0,03 : que concluez-vous, et que dites-vous à l'équipe produit ? »

**Réponse modèle (60 secondes).**

> Si l'hypothèse nulle était vraie, si le changement n'avait aucun effet, un écart au moins aussi grand que le nôtre n'arriverait que 3 fois sur 100. Ce n'est pas la probabilité que le changement soit inutile. Au seuil de 5 % fixé avant le test, je rejette l'hypothèse nulle. Mais avant d'y croire, je vérifie deux choses. D'abord le protocole : la métrique et la taille d'échantillon étaient-elles fixées à l'avance, ou s'est-on arrêté dès que la p-valeur est passée sous 0,05 en regardant les résultats chaque jour ? Cet arrêt-là gonfle beaucoup le risque de faux positif. Ensuite la taille de l'effet, avec son intervalle de confiance : un effet réel peut être trop petit pour compter. À l'équipe produit, je ne dis pas « c'est prouvé » : je dis que l'effet est probablement réel, qu'il vaut entre telle et telle valeur, et je recommande de le confirmer si la décision coûte cher.

**Grille.** (1) le sens exact de $p = 0{,}03$ et le contresens à éviter ; (2) la décision au seuil prévu à l'avance ; (3) les questions sur le protocole (fixé à l'avance, sans arrêt au premier résultat favorable) et sur la taille de l'effet ; (4) un message pour l'équipe produit en termes d'effet et d'intervalle, pas de « significatif ».

<a id="notebook"></a>

## Notebook

### Ex M08.16 — Le test binomial exact · `binomial_test`

**Réponses** : a) `0.0106` · b) `0.0213` · c) `0.0142` · d) `0.02` · e) `"ValueError"` · f) `"float"`.

**Démarche.** Les vérifications d'abord (`n` entier au moins 1, `k` entier entre 0 et `n`, `0 < p < 1`, `alternative` connue) ; puis les probabilités $P(K = j)$ avec `math.comb(n, j) * p ** j * (1 - p) ** (n - j)`. `"greater"` : la somme pour $j \ge k$ ; `"less"` : pour $j \le k$ ; `"two-sided"` : la somme des $P(K = j)$ qui vérifient `P(K = j) <= P(K = k) * (1 + 1e-7)`, puis `min(1.0, ...)`. Pour la copie : a) $\frac{560 + 120 + 16 + 1}{65\,536} = \frac{697}{65\,536}$ ; b) le double, car la loi $\mathcal{B}(16, \frac{1}{2})$ est symétrique ; d) la loi $\mathcal{B}(15 ;\ 0{,}3)$ ne l'est pas : seules $j = 0$ et $j = 9$ à 15 sont au plus aussi probables que $j = 9$, d'où 0,0200 et non $2 \times 0{,}0152 = 0{,}0305$.

**Erreurs fréquentes.** Commencer la somme à $k + 1$ (a : 0,0021) ; doubler la p-valeur unilatérale pour $p \ne \frac{1}{2}$ (d : 0,0305) ; oublier le plafond à 1 ; comparer les probabilités avec `<` strict ou sans tolérance (les arrondis font perdre l'issue observée elle-même, ou une issue de même probabilité de l'autre côté) ; ne pas lever d'erreur pour $k > n$ (`math.comb(3, 4)` vaut 0, et la fonction renverrait un nombre).

### Ex M08.17 — Le test par permutation à deux échantillons · `permutation_test`

**Réponses** : a) `0.019` · b) `0.026` · c) `0.002` · d) `"ValueError"` · e) `"float"`.

**Démarche.** Les deux échantillons en tableaux de flottants (une `ValueError` s'ils sont vides), les vérifications de `n_permutations` et de `alternative`, puis : `observed = x.mean() - y.mean()`, `pooled = np.concatenate([x, y])`, `rng = np.random.default_rng(seed)` **une seule fois** ; dans la boucle, `perm = rng.permutation(pooled)` et `t_perm = perm[:len(x)].mean() - perm[len(x):].mean()` ; le compte selon `alternative` avec la tolérance $10^{-9}$ ; enfin `float((count + 1) / (n_permutations + 1))`. Pour la copie : $C = 37$ en a), d'où $\frac{38}{2000}$, contre $\frac{2}{126} \approx 0{,}0159$ exactement : l'écart (0,003) vaut un peu plus d'une erreur type, $\sqrt{0{,}0159 \times 0{,}984/1999} \approx 0{,}0028$. En c), aucun tirage n'atteint l'écart observé : $\frac{0 + 1}{500}$, la plus petite p-valeur possible avec 499 permutations. Pour descendre plus bas, il faut plus de permutations (ou parcourir les $\binom{16}{8} = 12\,870$ répartitions).

**Erreurs fréquentes.** Recréer le générateur à chaque tour de boucle (toutes les permutations sont alors identiques) ; mélanger les indices au lieu des valeurs, ou mélanger `x` et `y` séparément (la suite des tirages change, et les tests de la procédure échouent) ; oublier le $+1$ (c : 0) ; comparer sans tolérance (une permutation égale à l'observation peut être perdue par un arrondi) ; prendre la valeur absolue en unilatéral.

### Ex M08.18 — Les intervalles de Wilson et de Student · `proportion_ci, paired_difference_ci`

**Réponses** : a) `[0.0531, 0.2968]` · b) `[0.0117, 0.255]` · c) `[0.8865, 1.0]` · d) `[0.0613, 0.266]` · e) `[0.0823, 0.7977]` · f) `"ValueError"` · g) `"tuple"`.

**Démarche.** `proportion_ci` : `z = statistics.NormalDist().inv_cdf((1 + level) / 2)` ; Wald, `p_hat ± z * math.sqrt(p_hat * (1 - p_hat) / n)` ; Wilson, la formule de la fiche ; puis chaque borne ramenée dans $[0, 1]$ et `(float(low), float(high))`. `paired_difference_ci` : `d = a - b`, `t = scipy.stats.t.ppf((1 + level) / 2, n - 1)`, `half = t * d.std(ddof=1) / math.sqrt(n)`. Pour la copie : c) 30 succès sur 30 n'excluent pas une probabilité de 0,9 ; Wilson le dit, Wald ($[1, 1]$) non. d) À 90 %, $z \approx 1{,}645$ : l'intervalle est plus étroit, au prix d'un risque plus grand de manquer la vraie valeur. e) Les différences valent 0,5 ; 0,2 ; 0,9 ; 0,4 ; 0,2 (moyenne 0,44 s) ; l'intervalle ne contient pas 0 : la mise à jour accélère la compilation, de quelques dixièmes de seconde.

**Erreurs fréquentes.** Prendre le quantile d'ordre `level` au lieu de $\frac{1 + \text{level}}{2}$ (a, d) ; Wald par défaut (a) ; le quantile de la loi normale, ou $n$ degrés de liberté au lieu de $n - 1$ (e) ; $\mathrm{ddof} = 0$ ; renvoyer une liste ou un tableau (g).

### Ex M08.19 — Bonferroni, l'AIC et le BIC · `bonferroni, aic_bic`

**Réponses** : a) `[0.008, 0.12, 0.8, 0.044]` · b) `[1.0, 1.0]` · c) `[122.6, 133.75]` · d) `"ValueError"` · e) `"ndarray"`.

**Démarche.** `bonferroni` : `p = np.array(p_values, dtype=float)`, les vérifications (une dimension, non vide, chaque valeur dans $[0, 1]$), puis `np.minimum(1.0, p * p.size)`. `aic_bic` : `(float(2 * k - 2 * ll), float(k * math.log(n) - 2 * ll))`. Pour la copie : au risque de la famille de 5 %, le premier et le quatrième test rejettent (0,008 et 0,044). $m\,p_i$ peut dépasser 1, qui n'est pas une probabilité. En c), le BIC fait payer chaque paramètre $\ln 120 \approx 4{,}79$, l'AIC 2 : $\ln n > 2$ dès que $n \ge 8$.

**Erreurs fréquentes.** Diviser au lieu de multiplier (a) ; oublier le plafond (b : 1,4) ; `math.log10` au lieu de `math.log` (c) ; un signe perdu devant $2\ln L$ ; l'ordre (BIC, AIC).

### Ex M08.20 — `scipy.stats.binomtest`, `permutation_test` et `ttest_rel` contre tes fonctions

**Réponses** : a) `0.0258` · b) `[0.1179, 0.4093]` · c) `0.0159` · d) `0.0269` · e) `True` · f) `True`.

**Démarche.** `stats.binomtest(7, 30, p=0.1)` donne `.pvalue` et `.proportion_ci(confidence_level=0.95, method="wilson")`. Pour c), `stats.permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), permutation_type="independent", alternative="greater", n_resamples=np.inf).pvalue` parcourt les 126 répartitions : $\frac{2}{126}$. Pour d), `stats.ttest_rel(a, b).pvalue`. Pour e), une boucle sur $k$ de 0 à 30 avec `abs(... - ...) <= 1e-9`, et `all(...)`. Pour la copie : la p-valeur estimée de M08.17 a), 0,019, est à environ une erreur type de la valeur exacte. d) $\approx 0{,}027 < 0{,}05$, cohérent avec l'intervalle de M08.18 e), qui ne contient pas 0 : un intervalle de Student à 95 % exclut 0 exactement quand la p-valeur bilatérale du test de Student est sous 0,05.

**Erreurs fréquentes.** Une fonction `statistic` sans argument `axis` (SciPy l'appelle sur des tableaux de permutations) ; oublier `n_resamples=np.inf` (la p-valeur devient une estimation, qui change d'un appel à l'autre) ; `ttest_ind` au lieu de `ttest_rel` (des mesures appariées) ; comparer des flottants avec `==`.

### Ex M08.21 — Prédire : sous H0, quelle part de 1 000 p-valeurs tombe sous 0,05 ?

**Réponses** : a) `2` · b) `2` · c) `3` · d) `1`.

Sous $H_0$, la p-valeur d'un test à statistique continue est uniforme (M08.10) : environ 5 % des 1 000 p-valeurs sont sous 0,05 (0,058 ici, à une erreur type et demie de 0,05, car $\sqrt{0{,}05 \times 0{,}95/1000} \approx 0{,}007$), et l'histogramme est plat. Le test binomial sur 10 essais ne rejette que pour 0, 1, 9 ou 10 succès : $\frac{2 \times 11}{1024} \approx 0{,}021$, un test **conservateur**. Sous $H_1$, la part des p-valeurs sous 0,05 est la **puissance** : environ 0,61 ici, $\Phi(0{,}5\sqrt{20} - 1{,}96)$ ; elle grandit avec l'effet et avec le nombre de mesures.

### Ex M08.22 — La puissance d'un test par permutation, selon l'effet et la taille des groupes

**Réponses** : a) `0.05` · b) `0.68` · c) `0.47` · d) `20`.

**Démarche.** Un générateur, une boucle de `n_sims` tours qui tire `x` puis `y` dans cet ordre, appelle `mymath.testing.permutation_test(x, y, n_permutations, alternative="greater", seed=sim)` et compte les p-valeurs au plus égales à 0,05 ; on renvoie `float(rejected / n_sims)`. Pour la copie : a) mesure le risque de type I ; sur 100 simulations, son erreur type vaut $\sqrt{0{,}05 \times 0{,}95/100} \approx 0{,}022$ : 0,05 ou 0,08 sont aussi normaux l'un que l'autre. La puissance grandit avec l'effet et avec $n$ ; il faut 20 mesures par groupe pour dépasser 0,8 avec un effet de 1. La grille suit de près le test $z$ (0,72 contre 0,68, 0,94 contre 0,95…), qui connaît pourtant $\sigma$ : le test par permutation perd peu, et ne suppose rien sur la loi.

**Erreurs fréquentes.** Tirer `y` avant `x`, ou créer le générateur dans la boucle (les valeurs ne correspondent plus) ; compter les p-valeurs au-dessus de 0,05 ; oublier `alternative="greater"` (le test bilatéral est moins puissant).

### Ex M08.23 — La loi de la statistique sous H0, et la p-valeur comme une aire

**Démarche.** `pooled = np.concatenate([x, y])` ; pour chaque `idx` de `itertools.combinations(range(len(pooled)), len(x))`, un masque booléen du premier groupe et l'écart des deux moyennes ; puis deux `ax.hist` (les répartitions au moins aussi extrêmes, `values >= observed - 1e-9`, dans une autre couleur, avec les **mêmes** classes), `ax.axvline(observed)`, et `return float(np.mean(extreme))`. Pour la copie : $\binom{10}{5} = 252$ répartitions ; l'écart observé vaut $30{,}8 - 26{,}6 = 4{,}2$ minutes, et 7 répartitions sur 252 font au moins aussi bien : $p = \frac{7}{252} = \frac{1}{36} \approx 0{,}028$, la part des barres de l'autre couleur. Avec deux groupes de même taille, échanger les groupes change $t$ en $-t$ : la loi est symétrique autour de 0.

**Erreurs fréquentes.** Ouvrir une nouvelle figure dans la fonction ; deux histogrammes avec des classes différentes ; oublier la tolérance ($t_{\text{perm}} = t$ peut être perdu par un arrondi) ; renvoyer un nombre de répartitions au lieu d'une proportion.

### Ex M08.24 — Chasse à l'erreur : une p-valeur nulle, un test unilatéral choisi après coup, Bonferroni à l'envers

**Réponses** : a) `"ACE"` · b) `[0.001, 0.015, 0.012, 1.96, 0.072, 0.127]`.

**Démarche.** (A) annonce $\frac{0}{999} = 0$ : la bonne p-valeur est $\frac{C + 1}{B + 1} = 0{,}001$. (B) est juste : $\frac{3060 + 816 + 153 + 18 + 1}{2^{18}} = \frac{4048}{262\,144} \approx 0{,}015$. (C) divise au lieu de multiplier : $\min(1, 3 \times 0{,}004) = 0{,}012$. (D) est juste : 1,960. (E) ne compte qu'un côté : $2\big(1 - \Phi(1{,}8)\big) \approx 0{,}072$, pas 0,036. (F) est juste : $1{,}96\sqrt{0{,}21/50} \approx 0{,}127$. Pour la copie : prendre toujours le côté où tombe $z$, c'est choisir le test unilatéral après coup ; la règle « rejeter si $1 - \Phi(|z|) \le 0{,}05$ » rejette dès que $|z| \ge 1{,}645$, ce qui arrive avec la probabilité 0,10 sous $H_0$ : le double du seuil annoncé.

**Erreurs fréquentes.** Citer (B) parce que la somme commence à 14 (elle doit commencer à 14 pour $P(K \ge 14)$) ; citer (D) en pensant au 1,645 d'un test unilatéral ; oublier (E), qui « a l'air » d'une p-valeur.

### Ex M08.25 — Tester un test : un pytest qui vérifie l'uniformité des p-valeurs sous H0

**Démarche.** `assert_calibrated` : `samples = np.random.default_rng(seed).normal(0, 1, size=(n_sims, n))`, `share = np.mean(p_value_function(samples) <= alpha)`, `se = math.sqrt(alpha * (1 - alpha) / n_sims)`, puis `assert abs(share - alpha) <= K_SE * se, f"expected … got {share}"`. `test_z_test_is_calibrated` appelle `assert_calibrated(z_test_p_values, seed=2025)`. Pour la copie : l'erreur type vaut $\sqrt{0{,}05 \times 0{,}95/4000} \approx 0{,}0034$ ; un $K_{SE}$ entre 4 et 8 convient (la bonne fonction échoue avec la probabilité $2(1 - \Phi(K_{SE}))$, $6 \times 10^{-5}$ pour 4). La copie 1 oublie le facteur 2 : elle rejette dans 10 % des cas, le sens dangereux (des faux positifs). La copie 2 divise par $\sqrt{n}$ au lieu de multiplier : $z$ est 20 fois trop petit, et le test ne rejette presque jamais (pas de faux positifs, mais plus de puissance). Les deux s'écartent de 0,05 d'environ 14 erreurs types, dans un sens ou dans l'autre : il faut comparer l'écart **en valeur absolue**. Une copie `1 - p` passerait : si $P$ est uniforme, $1 - P$ l'est aussi. Elle ne se trahit que sous $H_1$, où elle ne rejette presque jamais : un test complet vérifie aussi la puissance sur un cas où l'effet existe.

**Erreurs fréquentes.** Un test à sens unique (`share <= alpha + tol`), qui laisse passer la copie 2 ; une tolérance fixe (`0.01`) au lieu d'une tolérance en erreurs types ; un générateur sans graine (un test qui n'est pas reproductible) ; un `assert` sans message.

### Ex M08.26 — Défi : retrouver les trois vraies features parmi cinquante, avec au plus un faux positif

**Réponse** : `True`.

**Démarche.** Une p-valeur par feature (`stats.pearsonr(X[:, j], y).pvalue`), puis la correction de Bonferroni (`mymath.testing.bonferroni`) au risque de la famille de 5 % : on garde les features dont la p-valeur ajustée est au plus 0,05. Pour la copie : la règle « $p \le 0{,}05$ » déclare 4 features sur `X_26` (une fausse) ; sur 47 features de bruit, on attendait $47 \times 0{,}05 \approx 2{,}4$ faux positifs, et l'un des cinq datasets en donne 7. « Les trois plus fortes corrélations » suppose de connaître le nombre de vraies features : elle en manque une sur le dataset qui en a quatre, et ajoute des faux positifs sur ceux qui en ont une ou deux. Bonferroni garantit une probabilité d'au moins un faux positif sous 5 %, quelle que soit la dépendance entre les tests (M08.11) ; son risque est de manquer une vraie feature faible, ce qui n'arrive pas ici (la plus faible a une corrélation d'environ 0,35, et une p-valeur ajustée bien plus petite que 0,05).

**Erreurs fréquentes.** Le seuil 0,05 sans correction ; un nombre de features fixé d'avance ; un seuil sur la corrélation choisi en regardant les cinq datasets (il marche ici, mais rien ne dit ce qu'il garantit ailleurs).
