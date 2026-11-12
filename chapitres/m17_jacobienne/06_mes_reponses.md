# M17 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m17_jacobienne/06_mes_reponses.md` (créée par `python tools/start_chapter.py M17`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une jacobienne d'une application de $\mathbb{R}^n$ dans $\mathbb{R}^m$ a la forme $(m, n)$, les formes d'un produit de jacobiennes s'enchaînent, une jacobienne s'évalue au point où l'on applique sa fonction, des probabilités sont positives et de somme 1, une matrice de covariance est symétrique et ses lignes, pour un vecteur one-hot, ont une somme nulle. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, une dérivée partielle avec `\frac{\partial f_i}{\partial x_j}` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M17.Q1 — La forme d'une jacobienne

1. 
2. 
3. 
4. 
5. 
6. 

### M17.Q2 — Diagonale ou pleine ?

1. 
2. 
3. 
4. 
5. 
6. 

### M17.Q3 — Dans quel ordre multiplier les jacobiennes ?

1. 
2. 
3. 
4. 
5. 
6. 

### M17.Q4 — Gradient en ligne ou de la forme de la variable

1. 
2. 
3. 
4. 
5. 
6. 

### M17.Q5 — Jacobienne-vecteur ou vecteur-jacobienne : combien d'opérations ?

1. 
2. 
3. 
4. 
5. 
6. 

### M17.Q6 — La loi de Boltzmann : populations relatives et énergie moyenne

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M17.R1 — Dérivées partielles et gradient (M05b)

1. 
2. 
3. 
4. 
5. 

### M17.R2 — La règle de la chaîne en une variable (R7)

1. 
2. 
3. 
4. 
5. 

### M17.R3 — La matrice de covariance (M02c)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M17.1 — La jacobienne des coordonnées polaires, son déterminant, et l'approximation linéaire près d'un point

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M17.2 — Une fonction appliquée coordonnée par coordonnée : la jacobienne diagonale, et son produit par un vecteur

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M17.3 — Dériver une composée de trois applications par le produit de leurs jacobiennes

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M17.4 — La normalisation x/‖x‖ : sa jacobienne (I − uuᵀ)/‖x‖, et la direction qu'elle écrase

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M17.5 — Le gradient d'une fonction scalaire d'une composée, dans les deux conventions : J_fᵀ ∇L

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M17.6 — Dérivées à gauche et à droite d'une fonction définie par morceaux, et la dérivée d'une composée de sept copies d'une fonction lisse

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M17.7 — Une loi de Boltzmann à quatre niveaux d'énergie : rapports de populations, énergie moyenne, et la température où le niveau fondamental garde la moitié

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M17.11 — Le recuit simulé : une loi de Boltzmann sur cinq configurations, dont on baisse la température

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

## ∂ Démonstrations

### Ex M17.8 — La règle de la chaîne pour des applications de ℝⁿ dans ℝᵐ, à partir de l'approximation linéaire

1. 
2. 
3. 
4. 
5. 

### Ex M17.9 — Une fonction appliquée coordonnée par coordonnée a une jacobienne diagonale, et J v = f′(x) ⊙ v

1. 
2. 
3. 
4. 
5. 

### Ex M17.10 — diag(p) − pᵀp est la covariance d'un vecteur one-hot : symétrique, semi-définie positive, de noyau contenant 1

1. 
2. 
3. 
4. 
5. 

## 📖 🗣️ Lecture et explication

### Ex M17.12 — MML §5.3 : gradients de fonctions à valeurs vectorielles, en anglais

1. 
2. 
3. 
4. 
5. 

### Ex M17.13 — Expliquer la règle de la chaîne multivariée avec des taux de change entre monnaies

*Ta réponse à ton ami, en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M17.E1 — « Qu'est-ce qu'une jacobienne ? Donne un exemple hors du machine learning. »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M17.14 — La jacobienne par différences centrées, colonne par colonne · `numerical_jacobian`

- pourquoi un degré de longitude vaut R cos φ π/180 ; le coût en évaluations ; les entrées que ta fonction refuse :

### Ex M17.15 — Une jacobienne diagonale avec une seule paire d'évaluations · `diagonal_jacobian`

- les deux nombres d'appels ; la trace approchée par une intégrale ; ce que rendrait ta fonction sur une application qui n'est pas coordonnée par coordonnée :

### Ex M17.16 — Un produit jacobienne-vecteur sans former la jacobienne · `jacobian_vector_product`

- (J v)ᵢ écrit à la main et son coût ; les deux nombres d'appels :

### Ex M17.17 — `sympy.Matrix.jacobian` et `scipy.differentiate.jacobian` contre ta jacobienne numérique

- le déterminant r² sin θ et son sens ; ce que fait chaque outil ; les écarts mesurés :

### Ex M17.18 — Prédire la forme et les zéros de la jacobienne d'une composée, puis vérifier

- tes trois prédictions avant l'expérience ; le motif des zéros de J_f, de J_g et de leur produit :

### Ex M17.19 — Une longue composition : une dérivée qui s'éteint ou explose selon la pente au point fixe

- la pente au point fixe pour c = 2,6 ; les taux mesurés ; pourquoi la dérivée explose pour c = 4 alors que les valeurs restent dans [0 ; 1] :

### Ex M17.20 — Une grille du plan déformée par une application non linéaire, et par son approximation linéaire

- ce que montrent les deux figures ; pourquoi les grilles s'écartent loin de a :

### Ex M17.21 — Chasse à l'erreur : une jacobienne transposée, un produit dans le mauvais ordre, une jacobienne évaluée au mauvais point

- après la vérification : ce que calcule chaque fonction de la collègue, la règle de la fiche qu'elle viole, et sa correction :

### Ex M17.22 — Un test de propriété : J_{g∘f} = J_g J_f sur des applications tirées au hasard

- la propriété testée ; ce qui attrape chaque fausse implémentation :

### Ex M17.23 — Défi : la jacobienne de l'inversion X ↦ X⁻¹, vue comme une application de ℝ^{n²} dans ℝ^{n²}

- la dérivée de X X⁻¹ = I ; la jacobienne 4 × 4 et son déterminant ; ta vérification sur des matrices 3 × 3 :
