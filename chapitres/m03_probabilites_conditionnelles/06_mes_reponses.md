# M03 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m03_probabilites_conditionnelles/06_mes_reponses.md` (créée par `python tools/start_chapter.py M03`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris chaque probabilité conditionnelle avec le mot « sachant » et dis par quel total tu divises ; garde les fractions exactes ($\frac{70}{120}$, $\frac{34}{45}$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M03.Q1 — Jointe, marginale ou conditionnelle ?

1. 
2. 
3. 
4. 
5. 
6. 

### M03.Q2 — P(A sachant B) et P(B sachant A)

1. 
2. 
3. 
4. 
5. 
6. 

### M03.Q3 — Indépendants ou incompatibles ?

1. 
2. 
3. 
4. 
5. 
6. 

### M03.Q4 — Quelle métrique pour quelle probabilité ?

1. 
2. 
3. 
4. 
5. 
6. 

### M03.Q5 — Moyennes de métriques

1. 
2. 
3. 
4. 
5. 
6. 

### M03.Q6 — ROC et AUC : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M03.Q7 — Calibré ou pas ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M03.R1 — Arbres pondérés (R8)

1. 
2. 
3. 
4. 
5. 

### M03.R2 — Moyenne harmonique et moyenne pondérée (R1)

1. 
2. 
3. 
4. 
5. 

### M03.R3 — Aire par la méthode des trapèzes (M02a)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M03.1 — Un tableau de contingence : jointes, marginales, conditionnelles

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le tableau avec ses totaux ; f) comparé à a) : indépendance ? ; la somme de g) :

### Ex M03.2 — L'indépendance, vérifiée dans un tableau

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le tableau 1 vérifié de deux façons ; le tableau des effectifs attendus du tableau 2 ; la version B est-elle meilleure ? :

### Ex M03.3 — Probabilités totales avec trois cas

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- L'arbre ; pourquoi a) est près de 1 % ; pourquoi e) dépasse 20 % ; la meilleure amélioration :

### Ex M03.4 — Une matrice de confusion lue comme des probabilités

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La matrice complète ; chaque mesure en notation P(… | …), et où elle se lit ; faut-il croire une alerte ? :

### Ex M03.5 — F-beta : quel β pour quel coût d'erreur ?

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- a) et b) avec les comptages ; pourquoi g) = c) ; les deux F1 :

### Ex M03.6 — Balanced accuracy et MCC sur un problème déséquilibré

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les deux matrices ; le MCC du modèle A ; le modèle préféré par chaque mesure ; B est-il utile ? :

### Ex M03.7 — Changer de population : recalculer la precision quand la prévalence change

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- b) par la formule et par le tableau ; pourquoi f) est si haute ; ma proposition à l'équipe :

### Ex M03.8 — Une courbe ROC à la main, et son aire par les trapèzes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le tracé sur le quadrillage 5 × 5 et le nombre de cases sous la courbe ; g) et h) en cases :

### Ex M03.9 — L'AUC comme proportion de paires bien classées

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le tableau des 12 paires ; la relation entre d), c), b) et g) ; le segment en diagonale :

### Ex M03.10 — Courbe precision-recall et average precision à la main

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le tableau des 7 seuils ; pourquoi la precision remonte parfois :

### Ex M03.11 — Score de Brier et calibration de huit prévisions

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le diagramme de fiabilité ; calibrées ? ; le colis qui coûte le plus ; huit colis suffisent-ils ? :

## ∂ Démonstrations

### Ex M03.12 — L'aire sous la courbe ROC compte les paires bien classées

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M03.13 — En multiclasse, micro-precision, micro-recall et accuracy sont égaux

1. 
2. 
3. 
4. 
5. 
6. 
7. 

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M03.14 — Un seuil sur un score : trois seuils, trois matrices de confusion

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les trois matrices ; l'évolution de la precision et du recall ; le seuil pour un coût de 1 par erreur ; pourquoi pas sur le test :

### Ex M03.15 — Équité : les taux de faux positifs de deux groupes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- L'identité vérifiée pour chaque groupe ; les risques d'être signalé à tort ; la valeur d'une alerte ; le critère choisi et son coût :

### Ex M03.16 — MML §6.3 : règle de la somme, règle du produit et vocabulaire, en anglais

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M03.17 — Un taux de réussite trompeur : le paradoxe de Simpson

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M03.18 — Expliquer pourquoi P(A sachant B) n'est pas P(B sachant A)

*Huit lignes au plus, sans formule compliquée.*

> 

## 💼 Entretien

### M03.E1 — Une variable indépendante de la cible peut-elle aider un modèle ?

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M03.19 — Jointe, marginales et conditionnelles à partir d'un tableau de comptages

- a), d) et e) refaits à la main ; laquelle de b) et c) est la loi de la formule :

### Ex M03.20 — Tester l'indépendance avec une tolérance

- La loi de e), case par case ; l'écart de TABLE_20 ; pourquoi jamais d'indépendance exacte sur des données :

### Ex M03.21 — L'AUC en comptant les paires

- a) et b) à la main ; le temps de g) ; la valeur théorique Φ(1/√2) :

### Ex M03.22 — `sklearn.metrics.roc_auc_score` contre le comptage des paires, ex æquo compris

- a) par les paires ; pourquoi c) = d) ; le premier seuil de e) :

### Ex M03.23 — Prédire : l'AUC après une transformation croissante des scores

- Mes prédictions avant l'expérience (et pourquoi) ; l'explication de chaque résultat ; ce que l'AUC ne mesure pas :

### Ex M03.24 — Simuler pour estimer une probabilité conditionnelle

- Les valeurs exactes de a) à e) ; pourquoi a) et b) diffèrent ; ce que montrent d) et e) ; les écarts comparés aux erreurs types :

### Ex M03.25 — La courbe ROC en escalier : une case par paire

- Le nombre de cases sous la courbe ; le segment en diagonale et ses paires :

### Ex M03.26 — Chasse à l'erreur : conditionnelle inversée, marginale oubliée

- La confusion de chaque ligne fausse ; la valeur impossible :

### Ex M03.27 — Une fonction qui refuse un tableau invalide (`ValueError`)

- L'ordre de mes vérifications et pourquoi ; ma fonction de mymath résiste-t-elle aux NaN ? :

### Ex M03.28 — Défi : retrouver un tableau de contingence à partir de quelques probabilités

- La méthode (à la main ou par le code) ; l'unicité ; ce qui remplacerait l'information 6 ; indépendance ? :
