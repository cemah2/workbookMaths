# MB3 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/mb3_rotations_attention/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB3`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : $\cos^2 + \sin^2 = 1$, et un cosinus ou un sinus est entre $-1$ et 1 ; une rotation conserve les longueurs et a pour déterminant 1, une symétrie $-1$ ; $\mathbf{R} _\theta^{-1} = \mathbf{R} _\theta^\top = \mathbf{R} _{-\theta}$ ; dans un produit, la matrice de droite agit la première ; une rotation de Givens $\mathbf{R} _{ij}(\theta)$ ne change que les coordonnées $i$ et $j$ ; un encodage $(\cos, \sin)$ a pour norme 1, et le carré de la distance de deux encodages est entre 0 et 4 ; une direction moyenne se lit sur le vecteur moyen, jamais sur la moyenne des angles, et sa longueur $\rho$ est entre 0 et 1 ; des poids de softmax sont positifs, de somme 1, et une moyenne pondérée est entre la plus petite et la plus grande valeur ; un score $-\infty$ a un poids nul, et les autres se renormalisent entre eux ; ajouter une constante aux scores ne change pas les poids ; dans un état $(m, l, a)$, $l \ge 1$ dès que $m$ est fini, le facteur $e^{m - m'}$ est au plus 1, et $a/l$ ne dépend pas du découpage en blocs. Les formules s'écrivent en LaTeX entre `$` (R0 §5), un vecteur comme `$\mathbf{x}$`, une norme comme `$\lVert\mathbf{x}\rVert$` et une rotation comme `$\mathbf{R}_{23}(\theta)$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### MB3.Q1 — Formules d'addition et rotations du plan : le bon signe, composer, inverser, rotation ou symétrie ?

1. 
2. 
3. 
4. 
5. 

### MB3.Q2 — Rotations de l'espace, de Givens et par blocs : commutent-elles, que fixent-elles, que change une permutation des coordonnées ?

1. 
2. 
3. 
4. 
5. 

### MB3.Q3 — Encoder une direction ou un jour de l'année : une ou deux coordonnées, quelle période, quelle distance entre deux encodages ?

1. 
2. 
3. 
4. 
5. 

### MB3.Q4 — Moyennes pondérées par une softmax : dans l'enveloppe convexe ou non, largeur de bande, masque avant ou après la softmax, et un sous-ensemble vide

1. 
2. 
3. 
4. 
5. 

### MB3.Q5 — Multiplier tous les scores par c, ou leur ajouter une constante : ce qui change dans les poids, le poids maximal et l'entropie, et ce qui ne change pas

1. 
2. 
3. 
4. 
5. 

### MB3.Q6 — La softmax en ligne : ce que garde l'état, quand le remettre à l'échelle, et l'état vide

1. 
2. 
3. 
4. 
5. 

## 🔁 Rappels

### MB3.R1 — La forme exponentielle d'un complexe, et le produit comme rotation et homothétie (M22)

1. 
2. 
3. 
4. 
5. 

### MB3.R2 — Le log-sum-exp et la softmax stable (M05a)

1. 
2. 
3. 
4. 
5. 

### MB3.R3 — Tempérer et tronquer une loi : p^{1/T} renormalisée, top-k et top-p comme lois conditionnelles (M28)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex MB3.1 — Un bras articulé à deux segments : la position de la pince en valeurs exactes par les formules d'addition, les deux rotations enchaînées en une seule, et le retour par la rotation inverse

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB3.2 — Rotations de Givens : deux rotations de l'espace qui ne commutent pas, deux rotations de ℝ⁴ dans des plans disjoints qui commutent, leur matrice diagonale par blocs, et la même rotation après une permutation des coordonnées

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB3.3 — La direction du vent : l'encoder par (cos, sin), la distance entre deux encodages, un vent qui tourne comme une rotation de l'encodage, et la direction moyenne de trois relevés

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB3.4 — L'estimateur de Nadaraya-Watson : la température d'un refuge à partir de quatre stations de montagne pondérées par un noyau gaussien de l'écart d'altitude, pour deux largeurs de bande, et ses deux limites

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB3.5 — Masques : une moyenne exponentielle normalisée vue comme une softmax sur les jours passés, puis la même quand un capteur tombe en panne un jour (un score −∞)

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB3.6 — La saturation d'une softmax : trois scores multipliés par un facteur c croissant, le poids maximal, la sensibilité 1 − Σ pᵢ² et la borne (K − 1) e^{−cΔ}

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB3.7 — La softmax en ligne à la main : neuf scores (des multiples de ln 2) et leurs valeurs lus par blocs de trois, l'état (m, l, a) après chaque bloc, la moyenne pondérée finale, puis la fusion de deux états calculés séparément

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

## ∂ Démonstrations

### Ex MB3.8 — Les formules d'addition par le produit scalaire de deux vecteurs unitaires ; puis R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}, et la règle e^{iα}e^{iβ} = e^{i(α+β)} que M22 admettait

1. 
2. 
3. 
4. 
5. 
6. 

### Ex MB3.9 — Une moyenne pondérée par une softmax sur un ensemble de points commute avec toute renumérotation des points ; un masque triangulaire casse cette équivariance

1. 
2. 
3. 
4. 

### Ex MB3.10 — La softmax en ligne est exacte : l'invariant de l'état après chaque bloc, par récurrence ; puis la fusion de deux états est associative et commutative, d'élément neutre (−∞, 0, 0)

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex MB3.11 — Pont : à normes égales, les poids d'un noyau gaussien sont une softmax des produits scalaires divisés par h² ; le vérifier sur quatre stations d'un même cercle, et lire 1/h² comme l'échelle des scores

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB3.12 — MML §3.9 lu : la rotation du plan (3.76), les rotations de l'espace (3.77)–(3.79), la rotation de Givens (3.80)–(3.81) et les propriétés du §3.9.4 ; R₂(θ) écrite comme une rotation de Givens, et deux rotations de l'espace qui ne commutent pas, sur un vecteur choisi

1. 
2. 
3. 
4. 
5. 

### Ex MB3.13 — Expliquer, avec une caisse tenue dans une monnaie qui change, pourquoi la softmax en ligne donne exactement le résultat du calcul en une fois

*Ta réponse en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### MB3.E1 — « Comment encoder une variable cyclique comme une heure ou une direction, et pourquoi pas par sa valeur ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex MB3.14 — La matrice d'une rotation de Givens de ℝⁿ · givens_rotation

> 

### Ex MB3.15 — La softmax en ligne : l'état (m, l, a) de scores et de valeurs lus par blocs, et l'état après chaque bloc · online_softmax

> 

### Ex MB3.16 — La fusion de deux états de la softmax en ligne · merge_softmax_states

> 

### Ex MB3.17 — Prédire ce que deviennent les poids et la prévision de Nadaraya-Watson quand la largeur de bande est divisée ou multipliée par 10, puis tracer

> 

### Ex MB3.18 — La softmax en ligne selon l'ordre et la taille des blocs : le nombre de remises à l'échelle (les états après chaque bloc) pour des scores croissants, décroissants ou mélangés, comparé à H_N − 1, et la mémoire gardée

> 

### Ex MB3.19 — Trois horloges (la journée, la semaine, l'année) : l'encodage d'une date sur trois cercles, un décalage comme trois rotations, et le produit scalaire de deux encodages en fonction de l'écart

> 

### Ex MB3.20 — Chasse à l'erreur : deux rotations de l'espace composées dans le mauvais ordre, une direction moyenne prise comme la moyenne des angles, une softmax en ligne qui remet l à l'échelle mais pas l'accumulateur

> 

### Ex MB3.21 — Un test de propriété : la softmax en ligne ne dépend ni de la taille des blocs, ni d'une même permutation des scores et des valeurs, ni d'une constante ajoutée aux scores, et la fusion de trois états est associative

> 

### Ex MB3.22 — Défi : prévoir la production d'une éolienne par Nadaraya-Watson sur l'encodage cyclique de la direction du vent et du jour de l'année, la largeur de bande choisie par validation croisée « un de côté », sous une erreur quadratique moyenne donnée

>
