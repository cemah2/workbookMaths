# M02c · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m02c_echantillons_estimation/06_mes_reponses.md` (créée par `python tools/start_chapter.py M02c`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Dis toujours si tu divises par $n$ ou par $n - 1$, écris les séries triées avant d'en lire un quantile, et garde les valeurs exactes ($\sqrt{8}$, $\frac{27}{16}$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M02c.Q1 — Résumer une série : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M02c.Q2 — z-scores et valeurs aberrantes

1. 
2. 
3. 
4. 
5. 
6. 

### M02c.Q3 — i.i.d. ou pas ?

1. 
2. 
3. 
4. 
5. 
6. 

### M02c.Q4 — Grands nombres et TCL : ce qu'ils disent, ce qu'ils ne disent pas

1. 
2. 
3. 
4. 
5. 
6. 

### M02c.Q5 — Biais, variance et ddof

1. 
2. 
3. 
4. 
5. 
6. 

### M02c.Q6 — Lire un intervalle de confiance

1. 
2. 
3. 
4. 
5. 
6. 

### M02c.Q7 — Covariance et corrélation : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M02c.R1 — Espérance et variance d'une somme (M02b)

1. 
2. 
3. 
4. 

### M02c.R2 — Loi normale et fonction Φ (M02b)

1. 
2. 
3. 
4. 
5. 

### M02c.R3 — Racines et puissances (R1)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M02c.1 — Les statistiques d'une petite série : moyenne, médiane, quartiles, variance

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La série triée ; la somme des écarts ; d) par la formule de calcul, et la méthode la plus sûre :

### Ex M02c.2 — z-scores, écart interquartile et valeurs aberrantes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Pourquoi c) et h) sont si différents ; le plus grand z-score possible avec 10 valeurs :

### Ex M02c.3 — Imputer par la moyenne ou la médiane : ce qui change

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- e) et f) par la formule de la fiche ; l'imputation choisie et pourquoi ; les non-répondants ressemblent-ils aux autres ? :

### Ex M02c.4 — Avec ou sans remise : la variance de la moyenne

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les 10 paires, leurs moyennes, et la variance de ces moyennes ; ce que dit h) d'un sondage :

### Ex M02c.5 — Combien d'observations pour une moyenne précise à 1 % ?

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Ce que garantissent c) et e) ; pourquoi Bienaymé-Tchebychev demande plus de mesures :

### Ex M02c.6 — Le théorème central limite à la main : une somme de 100 variables

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Pourquoi la loi normale convient pour S, et pas pour un seul jour :

### Ex M02c.7 — Biais, variance et erreur quadratique de trois estimateurs

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le biais et l'EQM de T₃ en fonction de μ ; pourquoi on ne peut pas choisir T₃ en pratique :

### Ex M02c.8 — Erreur type et intervalle de confiance d'une moyenne

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La phrase correcte qui interprète b) ; ce qu'il faudrait pour départager les deux modèles :

### Ex M02c.9 — La variance d'une somme et la covariance : V(X + Y), V(X − Y)

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- h) par la formule de la variance d'une somme ; le dessin des quatre points :

### Ex M02c.10 — La matrice de covariance de trois variables : la lire et la vérifier

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La matrice de corrélation ; la propriété violée par chaque tableau refusé en g) :

## ∂ Démonstrations

### Ex M02c.11 — Pourquoi diviser par n − 1 : E[S²] = σ²

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M02c.12 — La variance de la moyenne : V(X̄) = σ²/n, et l'erreur type

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M02c.13 — Le 99e percentile d'une latence : l'estimer et dire son incertitude

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Les valeurs sur lesquelles repose le p99,9 ; pourquoi il varie d'une heure à l'autre ; ce que je propose :

### Ex M02c.14 — Standardiser des features avec les statistiques du seul train

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Pourquoi f) est plus petit que c) ; les statistiques à utiliser en production ; pourquoi standardiser avec le test fausse l'évaluation :

### Ex M02c.15 — MML §6.4 : moyennes et covariances empiriques, en anglais

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M02c.16 — Le biais du survivant : des données qui ne montrent que ceux qui restent

1. 
2. 
3. 
4. 
5. 

### Ex M02c.17 — Expliquer le théorème central limite avec un histogramme

*Huit lignes au plus, sans formule compliquée.*

> 

## 💼 Entretien

### M02c.E1 — L'erreur type décroît en 1/√n : qu'est-ce que cela change pour un jeu de test ?

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M02c.18 — La distribution des moyennes d'échantillons

- c), d), e) et h) comparés à ce que prévoient les §3 et §5 :

### Ex M02c.19 — Biais et erreur quadratique d'un estimateur, par simulation

- a) à d) comparés à la fiche ; ce que mesure e) ; l'estimateur préféré et le critère ; h) et le calcul de la fiche :

### Ex M02c.20 — Erreur type et intervalle de confiance

- a) et c) refaits à la main ; pourquoi h) n'est pas exactement 1,96 :

### Ex M02c.21 — NumPy et SciPy : ddof, np.percentile, scipy.stats.sem

- c) avec la convention de la fiche ; h) par une formule en n ; pourquoi c) et d) diffèrent :

### Ex M02c.22 — Prédire : l'histogramme des moyennes d'une loi exponentielle quand n grandit

- Mes prédictions avant l'expérience (et pourquoi) ; l'explication de chaque résultat ; la symétrie pour n = 64 :

### Ex M02c.23 — Couverture : 95 % des intervalles contiennent-ils la vraie moyenne ?

- Les couvertures nettement sous leur niveau ; pourquoi b) est la plus basse et c) remonte ; ce que corrige e) :

### Ex M02c.24 — Grande dimension : le cube dont le centre est vide

- a), b), d) comparés aux valeurs exactes ; l'écart entre c) et e) ; le nombre de points pour en voir un en dimension 20 :

### Ex M02c.25 — Voir le théorème central limite : histogrammes et densité normale

- Le n à partir duquel la cloche décrit l'histogramme ; où se voit l'écart pour n = 10 ; pourquoi n = 1 est si loin :

### Ex M02c.26 — Chasse à l'erreur : un intervalle de confiance mal calculé

- La confusion de chaque ligne fausse ; le sens de l'intervalle de (E) :

### Ex M02c.27 — Tester une fonction aléatoire : une tolérance en erreurs types

- Ce qui se passe avec k = 1 et k = 50 ; pourquoi la fonction décalée de 0,002 passe ; combien de points pour l'attraper :

### Ex M02c.28 — Défi : un intervalle à 95 % avec dix valeurs d'une loi asymétrique

- La méthode retenue ; pourquoi l'intervalle n'est pas symétrique autour de x̄ ; pourquoi le bootstrap couvre mal :
