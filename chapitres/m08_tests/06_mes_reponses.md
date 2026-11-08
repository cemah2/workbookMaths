# M08 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m08_tests/06_mes_reponses.md` (créée par `python tools/start_chapter.py M08`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris $H_0$ et $H_1$ avant de calculer une p-valeur, la loi de la statistique sous $H_0$ avant d'additionner des probabilités, les issues que tu comptes avant leur somme ; garde les valeurs exactes ($\frac{79}{4096}$, $\sqrt{3}$) jusqu'au bout, et n'arrondis qu'à la fin. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M08.Q1 — Ce qu'une p-valeur est, et ce qu'elle n'est pas

1. 
2. 
3. 
4. 
5. 
6. 

### M08.Q2 — Unilatéral ou bilatéral ?

1. 
2. 
3. 
4. 
5. 
6. 

### M08.Q3 — Permuter quoi, et sous quelle hypothèse ?

1. 
2. 
3. 
4. 
5. 
6. 

### M08.Q4 — Erreurs de type I et II, puissance : associer

1. 
2. 
3. 
4. 
5. 
6. 

### M08.Q5 — Comparaisons multiples : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M08.Q6 — AIC, BIC, facteur de Bayes : qui pénalise quoi ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M08.R1 — La loi binomiale (M02b)

1. 
2. 
3. 
4. 
5. 

### M08.R2 — L'intervalle de confiance d'une moyenne (M02c)

1. 
2. 
3. 
4. 
5. 

### M08.R3 — Vraisemblance et log-vraisemblance (M04)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M08.1 — Un test binomial à la main : un algorithme de compression est-il plus rapide sur douze fichiers ?

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- H₀ et H₁ en une phrase chacune ; pourquoi la p-valeur bilatérale est le double de l'unilatérale ; l'approximation normale à côté de la valeur exacte ; que faire d'une égalité :

### Ex M08.2 — Un test par permutation exhaustif : deux groupes de trois mesures, vingt répartitions

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- t = (2S_A − 97)/3 démontré, et les 20 valeurs de S_A ; pourquoi l'observation est la plus extrême ; pourquoi la p-valeur bilatérale ne descend jamais sous celle de d) :

### Ex M08.3 — Erreur de type I, erreur de type II et puissance d'un test binomial

- a :
- b :
- c :
- d :
- e :
- f :
- Ce qu'on gagne et ce qu'on perd en passant de K ≥ 11 à K ≥ 10 ; pourquoi un risque d'exactement 0,05 est impossible ; comment augmenter la puissance sans augmenter le risque :

### Ex M08.4 — Combien d'observations pour une puissance de 80 % ? (approximation normale)

- a :
- b :
- c :
- d :
- e :
- f :
- Pourquoi n est multiplié par 4 quand l'effet est divisé par 2 ; ce que je conclurais d'un test non significatif avec 36 mesures :

### Ex M08.5 — L'intervalle d'une proportion : Wald contre Wilson, avec peu de succès

- a :
- b :
- c :
- d :
- e :
- f :
- L'intervalle de Wald pour f), et pourquoi il est absurde ; la borne haute de f) comparée à 3/n :

### Ex M08.6 — L'intervalle de Student d'une différence appariée : un serveur avant et après une mise à jour

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Pourquoi l'erreur type de f) est plus de trois fois celle de c) ; ce qu'on aurait dit de la mise à jour sans l'appariement ; le nombre de combinaisons de signes en h), et pourquoi aucune p-valeur plus petite n'est possible :

### Ex M08.7 — Vingt tests au seuil de 5 % : les faux positifs attendus, puis Bonferroni

- a :
- b :
- c :
- d :
- e :
- f :
- Le nombre de features déclarées sans correction ; la garantie que donne la correction, et celle qu'elle ne donne pas :

### Ex M08.8 — L'AIC et le BIC de deux modèles, à partir de leurs log-vraisemblances

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La différence des AIC comme un gain d'ajustement moins une pénalité ; pourquoi les deux critères ne sont pas d'accord :

### Ex M08.9 — Un facteur de Bayes entre deux taux de clics

- a :
- b :
- c :
- d :
- e :
- f :
- Le taux qui maximise la vraisemblance ; pourquoi M_C a une évidence plus petite ; ce que je conclus de c) :

## ∂ Démonstrations

### Ex M08.10 — Sous H0, une p-valeur continue suit la loi uniforme

1. 
2. 
3. 
4. 
5. 

### Ex M08.11 — L'inégalité de Boole et la garantie de Bonferroni, sans hypothèse d'indépendance

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M08.12 — L'intervalle de Wilson, en inversant le test d'une proportion

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M08.13 — Pont : l'importance d'une feature par permutation, sur un petit tableau

- a :
- b :
- c :
- d :
- e :
- f :
- Pourquoi mélanger une colonne casse son lien avec la cible sans changer ses valeurs ; pourquoi mélanger plusieurs fois au hasard ; pourquoi un jeu de validation :

### Ex M08.14 — MML §8.6 : validation croisée imbriquée, sélection bayésienne de modèle et facteur de Bayes

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M08.15 — Expliquer une p-valeur sans dire « la probabilité que H0 soit vraie »

*Huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M08.E1 — « Votre test donne p = 0,03 : que concluez-vous, et que dites-vous à l'équipe produit ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M08.16 — Le test binomial exact · `binomial_test`

- a) à la main, en fraction ; pourquoi b) est le double de a), et d) pas le double de P(K ≥ 9) ; les issues additionnées en d) :

### Ex M08.17 — Le test par permutation à deux échantillons · `permutation_test`

- L'écart de a) à la p-valeur exacte de M08.20 c), comparé à l'erreur type ; pourquoi c) ne descend pas sous 1/500 :

### Ex M08.18 — Les intervalles de Wilson et de Student · `proportion_ci, paired_difference_ci`

- Pourquoi c) ne contient pas seulement 1 ; pourquoi d) est plus étroit que a) ; l'effet de la mise à jour du compilateur d'après e) :

### Ex M08.19 — Bonferroni, l'AIC et le BIC · `bonferroni, aic_bic`

- Les tests de a) qui rejettent ; pourquoi plafonner à 1 ; le critère qui pénalise le plus en c), et à partir de quel n :

### Ex M08.20 — `scipy.stats.binomtest`, `permutation_test` et `ttest_rel` contre tes fonctions

- c) comparé à M08.17 a) ; ce que dit d), et sa cohérence avec l'intervalle de M08.18 e) :

### Ex M08.21 — Prédire : sous H0, quelle part de 1 000 p-valeurs tombe sous 0,05 ?

- Mes prédictions avant l'expérience (et pourquoi) ; ce que j'ai observé ; les issues qui font rejeter le test binomial sur 10 essais ; ce que mesure c) :

### Ex M08.22 — La puissance d'un test par permutation, selon l'effet et la taille des groupes

- Ce que mesure a), et pourquoi il ne vaut pas exactement 0,05 ; l'effet de δ et de n ; la comparaison avec le test z :

### Ex M08.23 — La loi de la statistique sous H0, et la p-valeur comme une aire

- Le nombre de répartitions ; la p-valeur et la partie de la figure qui lui correspond ; pourquoi la loi est symétrique :

### Ex M08.24 — Chasse à l'erreur : une p-valeur nulle, un test unilatéral choisi après coup, Bonferroni à l'envers

- Pour chaque ligne fausse, l'erreur et sa correction ; le vrai risque de type I de la règle (E) :

### Ex M08.25 — Tester un test : un pytest qui vérifie l'uniformité des p-valeurs sous H0

- Mon K_SE et pourquoi ; l'erreur de chaque copie fausse et son sens ; pourquoi la copie 1 − p passerait, et comment l'attraper :

### Ex M08.26 — Défi : retrouver les trois vraies features parmi cinquante, avec au plus un faux positif

- Le nombre de features de la règle p ≤ 0,05 sur X_26, et le nombre de faux positifs attendu ; pourquoi les trois plus fortes corrélations ne suffisent pas ; ma règle, sa garantie et son risque :
