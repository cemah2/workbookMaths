# M06 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m06_information/06_mes_reponses.md` (créée par `python tools/start_chapter.py M06`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris la loi utilisée avant de calculer son entropie, les lois conditionnelles (chaque ligne divisée par sa probabilité) avant $H(Y \mid X)$, et l'unité (bits ou nats) de chaque résultat ; garde les valeurs exactes ($\log_2 3$, $\frac{7}{16}$, $\ln 2$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M06.Q1 — La surprise et la probabilité

1. 
2. 
3. 
4. 
5. 
6. 

### M06.Q2 — L'entropie : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M06.Q3 — Conjointe et conditionnelle

1. 
2. 
3. 
4. 
5. 
6. 

### M06.Q4 — L'information mutuelle

1. 
2. 
3. 
4. 
5. 
6. 

### M06.Q5 — La KL n'est pas une distance

1. 
2. 
3. 
4. 
5. 
6. 

### M06.Q6 — L'inégalité de Jensen

1. 
2. 
3. 
4. 
5. 
6. 

### M06.Q7 — Codes préfixes

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M06.R1 — Logarithmes en base 2 (R6)

1. 
2. 
3. 
4. 
5. 

### M06.R2 — Probabilités jointes et conditionnelles (M03)

1. 
2. 
3. 
4. 
5. 

### M06.R3 — Convexité (M05a)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M06.1 — L'information d'événements et l'entropie d'une loi à quatre issues

- a :
- b :
- c :
- d :
- e :
- f :
- b) comme moyenne pondérée des informations de a) ; ce qu'on perd en regroupant les deux erreurs ; b) − e) écrit comme 0,1 fois l'entropie d'une loi à deux issues ; f) justifiée par la règle de la chaîne :

### Ex M06.2 — L'entropie maximale : comparer des lois à quatre issues

- a :
- b :
- c :
- d :
- e :
- f :
- L'effet du transfert de b) et du regroupement de c) ; la loi qui atteint le maximum de e), et pourquoi :

### Ex M06.3 — Entropies conjointe et conditionnelle d'un tableau 2 × 3

- a :
- b :
- c :
- d :
- e :
- f :
- La règle de la chaîne vérifiée de deux façons ; pourquoi H(Y | X = gratuit) = 0 ; le signe de f), comparé à celui de H(Y | X) − H(Y) :

### Ex M06.4 — La règle de la chaîne de l'entropie, vérifiée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- H(X) + H(Y | X) et H(Y) + H(X | Y) comparés à e) ; le canal qui rend l'ouverture la plus prévisible :

### Ex M06.5 — L'information mutuelle de deux variables

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- I(X ; Y) par H(X) + H(Y) − H(X, Y) ; la case qui contribue le plus, et celles qui contribuent négativement :

### Ex M06.6 — Cross-entropy et KL en bits perdus : un code fait pour la mauvaise loi

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- L'inégalité de Kraft pour les longueurs du compresseur ; les types plus chers et moins chers qu'avec le meilleur code ; le signe de chaque terme de la somme de d), et pourquoi le total ne peut pas être négatif :

### Ex M06.7 — L'inégalité de Jensen sur trois exemples

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Pour chaque exemple : f convexe ou concave, et le signe de l'écart :

### Ex M06.8 — Kraft : ces longueurs de code sont-elles possibles ?

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Pour a) à e) : un code préfixe existe-t-il ? (en écrire un) ; ce que dit l'inégalité de Kraft, et ce qu'elle ne dit pas (g) et h)) :

### Ex M06.9 — La longueur moyenne d'un code, comparée à l'entropie

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Un code préfixe de longueurs h) ; les quatre codes rangés par longueur moyenne, situés par rapport à H(p) et H(p) + 1 ; l'échange de deux mots qui améliore le code donné :

## ∂ Démonstrations

### Ex M06.10 — I(X ; Y) = H(X) − H(X | Y), et l'information mutuelle est positive

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M06.11 — La KL est positive : la preuve par l'inégalité de Jensen

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 🧮 🗣️ Pont, estimation et explication

### Ex M06.12 — La log loss d'un classifieur, une cross-entropy moyenne

- a :
- b :
- c :
- d :
- e :
- f :
- L'image qui coûte le plus cher, et pourquoi ; f) lu comme une perplexité ; la cross-entropy de l'image 3 si la classe C avait reçu la probabilité 0 :

### Ex M06.13 — Choisir une feature par l'information mutuelle

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- g) justifié par un calcul ; l'information mutuelle d'un numéro de client sur ces données, et son utilité pour un nouveau client ; comparer des features qui n'ont pas le même nombre de valeurs :

### Ex M06.14 — Fermi : combien de bits pour un génome humain ?

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M06.15 — Expliquer l'information mutuelle avec deux capteurs

*Huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M06.E1 — Information mutuelle ou corrélation : laquelle détecte quoi ?

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M06.16 — Entropies conjointe et conditionnelle d'un tableau · `joint_entropy, conditional_entropy`

- L'entropie conditionnelle que calcule c), et pourquoi la transposition suffit ; b) vérifiée ligne par ligne ; pourquoi le tableau de e) est refusé ; la loi à deux issues de g) :

### Ex M06.17 — L'information mutuelle · `mutual_information`

- La loi construite par np.outer en c), et pourquoi le résultat était prévisible ; H(Y | X) pour le tableau de d) ; pourquoi np.any(table < 0) ne suffit pas en f) :

### Ex M06.18 — Codes préfixes et somme de Kraft · `kraft_sum, is_prefix_code`

- Pour a) et b), un code préfixe existe-t-il ? L'arbre du code de d) ; pourquoi le mot vide ne peut pas faire partie d'un code :

### Ex M06.19 — L'écart de Jensen d'une loi discrète · `jensen_gap`

- Convexe ou concave, et le signe, pour a) à d) ; a) à la main et la grandeur de M02b retrouvée ; pourquoi abs donne un écart non nul en d), et quand il serait nul :

### Ex M06.20 — `sklearn.metrics.mutual_info_score` contre ta fonction, en nats

- L'entropie que donne c) ; pourquoi e) n'est pas nulle, et ce qu'elle deviendrait avec 4 000 observations ; le piège pour classer des features sur peu de données :

### Ex M06.21 — Prédire : l'information mutuelle de X et X³, de X et X²

- Mes prédictions avant l'expérience (et pourquoi) ; pourquoi I(X ; X³) = H(X) alors que la corrélation n'est pas 1 ; pourquoi I(X ; X²) = H(X²) ; ce qui reste inconnu sur X quand on connaît X², en bits ; ce que mesurent la corrélation et l'information mutuelle :

### Ex M06.22 — Estimer une entropie à partir d'un échantillon : le biais des petits échantillons

- Le sens de l'erreur du plug-in, et pourquoi ; a) et b) comparés à −(k − 1)/(2n ln 2) ; pourquoi Miller-Madow laisse un biais pour n = 10 ; la conséquence pour l'information mutuelle estimée :

### Ex M06.23 — Un diagramme de l'information : H(X), H(Y), H(X | Y), I(X ; Y)

- Les règles de la chaîne et les trois écritures de I lues sur la figure ; la figure pour deux variables indépendantes, et pour Y = X :

### Ex M06.24 — Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers

- Ce que renvoie chaque ligne fausse (un nombre faux, nan ou inf), et sa correction ; pourquoi une ligne fausse peut passer inaperçue :

### Ex M06.25 — Calculer 0 log 0 proprement (`scipy.special.xlogy`)

- La limite de x ln x en 0 ; H(Y | X) pour T25, à partir de ma liste ; pourquoi la troisième ligne a une entropie nulle :

### Ex M06.26 — Défi : localiser une panne parmi 100 serveurs en un minimum de questions

- Pourquoi 6,72 est le mieux possible pour la loi uniforme ; pourquoi couper la liste en deux moitiés ne suffit pas pour la seconde loi ; mon score comparé à bound_26 :
