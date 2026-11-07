# M07 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m07_vecteurs_rn/06_mes_reponses.md` (créée par `python tools/start_chapter.py M07`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris les différences de vecteurs avant leurs normes, le produit scalaire et les deux normes avant un cosinus, le coefficient $t$ avant une projection ; garde les valeurs exactes ($\sqrt{7}$, $\frac{8}{15}$) jusqu'au bout, et n'arrondis qu'à la fin. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M07.Q1 — Vecteurs, coordonnées et one-hot

1. 
2. 
3. 
4. 
5. 
6. 

### M07.Q2 — Ce que mesure un produit scalaire

1. 
2. 
3. 
4. 
5. 
6. 

### M07.Q3 — Trois normes, trois boules unités

1. 
2. 
3. 
4. 
5. 
6. 

### M07.Q4 — Similarité cosinus : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M07.Q5 — Hyperplans : vecteur normal et côtés

1. 
2. 
3. 
4. 
5. 
6. 

### M07.Q6 — Moyenne, barycentre et inertie

1. 
2. 
3. 
4. 
5. 
6. 

### M07.Q7 — Intuitions de la grande dimension

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M07.R1 — Produit scalaire et angle dans le plan (R9)

1. 
2. 
3. 
4. 
5. 

### M07.R2 — Moyenne et variance empiriques (M02c)

1. 
2. 
3. 
4. 
5. 

### M07.R3 — Gradient et point critique (M05b)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M07.1 — Combinaisons linéaires et vecteurs one-hot dans ℝ⁴

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le système de d) ; combien d'équations suffisaient, et à quoi servent les autres ; pourquoi ne pas coder les modes par 1, 2, 3, 4 :

### Ex M07.2 — Produits scalaires, ‖u + v‖² et l'identité du parallélogramme

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- d) calculé de deux façons ; un contre-exemple ou une démonstration pour g) :

### Ex M07.3 — Normes L1, L2, L∞ et distances entre trois profils

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- d₁(P, Q), d₂(P, Q) et d∞(P, Q), et pourquoi elles sont égales ; le genre d'écart que pénalisent le plus L1 et L∞ :

### Ex M07.4 — Similarité cosinus entre des profils d'écoute musicale

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- L'auditeur aux goûts les plus proches de A ; la mesure qui répond à la question, et pourquoi l'autre se trompe ; la mesure pour recommander des morceaux :

### Ex M07.5 — Projeter sur une droite : composante parallèle et composante orthogonale

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- ‖x‖², et pourquoi f) était prévisible ; le point de la droite le plus proche de x, et sa distance :

### Ex M07.6 — Un plan de ℝ³ : vecteur normal, côté, distance signée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- O et C sont-ils du même côté ? Le point de g) vérifié sur H ; la distance entre les deux plans parallèles :

### Ex M07.7 — Un score linéaire w · x + b : calculer, décider, lire le vecteur normal

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La position de M₃ ; le sens du poids négatif ; les décisions et la distance de g) si w et b sont multipliés par 10 :

### Ex M07.8 — Centroïde, inertie et formule de König-Huygens

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- c) vérifié avec König-Huygens ; g) avec König-Huygens pour les cinq anciens points ; pourquoi un seul point lointain fait autant grandir l'inertie :

### Ex M07.9 — Où placer un dépôt : le barycentre pondéré des livraisons

- a :
- b :
- c :
- d :
- e :
- König-Huygens avec des poids, et d) par cette formule ; le coût choisi est-il raisonnable, et quel autre coût, minimisé par quel point :

### Ex M07.10 — La silhouette d'un point, à la main, en dimension 2

- a :
- b :
- c :
- d :
- e :
- f :
- Les distances utiles ; le signe de e) était-il prévisible ? a(D) comparé à a(A), b(D) comparé à b(A), et celui qui explique s(D) < s(A) :

### Ex M07.11 — k-means++ : des probabilités de tirage proportionnelles à D²

- a :
- b :
- c :
- d :
- e :
- f :
- Pourquoi P₂ est un mauvais deuxième centre ; ce que gagne k-means++ (c) et f)) ; le cas d'un point éloigné qui serait une erreur de mesure :

### Ex M07.12 — La diagonale du cube unité et son angle avec les axes, quand d grandit

- a :
- b :
- c :
- d :
- e :
- f :
- Le cosinus de f) en fonction de d, et sa limite ; l'angle de deux sommets voisins vus depuis le centre, en grande dimension :

### Ex M07.13 — La distance au carré moyenne de deux points tirés dans le cube [0, 1]ᵈ

- a :
- b :
- c :
- d :
- e :
- f :
- c) retrouvé avec 𝔼[U − V] et 𝕍(U − V) ; f) dépend-il de d ? Ce que j'en conclus :

## ∂ Démonstrations

### Ex M07.14 — L'inégalité de Cauchy-Schwarz, par le discriminant

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M07.15 — L'inégalité triangulaire pour L2, L1 et L∞

1. 
2. 
3. 
4. 
5. 

### Ex M07.16 — La moyenne minimise la somme des carrés des distances, en dimension n

1. 
2. 
3. 
4. 
5. 

### Ex M07.17 — La distance d'un point à un hyperplan vaut |w · x + b| / ‖w‖

1. 
2. 
3. 
4. 
5. 

### Ex M07.18 — Les deux étapes de k-means font baisser l'inertie, ou la laissent égale

1. 
2. 
3. 
4. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M07.19 — Pont : changer l'unité d'une feature change le plus proche voisin

- a :
- b :
- c :
- d :
- e :
- f :
- Pourquoi la réponse change entre c) et d) ; pourquoi la standardisation ne dépend pas de l'unité de départ ; les méthodes de workbookIA 7 concernées :

### Ex M07.20 — MML §3.1 et §3.2.1 : normes et produit scalaire, en anglais

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M07.21 — MML §3.3 et §3.4 : longueurs, distances, angles et orthogonalité

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M07.22 — Fermi : la mémoire d'un million d'embeddings

1. 
2. 
3. 
4. 

### Ex M07.23 — Expliquer la similarité cosinus à quelqu'un qui a fait le lycée

*Huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M07.E1 — Distance euclidienne ou similarité cosinus : laquelle pour comparer des textes ?

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M07.24 — Normes Lp et similarité cosinus · `norm_p, cosine_similarity`

- a) à d) et f) à la main ; pourquoi la norme diminue quand p augmente ; pourquoi np.clip est nécessaire :

### Ex M07.25 — La projection sur une droite · `project_onto_line`

- a), c) et d) à la main ; ce que fait la projection sur un axe ; pourquoi le signe de u ne change rien en c) :

### Ex M07.26 — Barycentre et somme des carrés des distances · `centroid, sum_sq_distances_to`

- a) à d) à la main, d) vérifié avec König-Huygens ; pourquoi le dernier point ne compte pas en b) :

### Ex M07.27 — Côté d'un hyperplan et distance à un hyperplan · `side_of_hyperplane, distance_to_hyperplane`

- a) et b) à la main ; la distance de l'origine à l'hyperplan, et son côté :

### Ex M07.28 — `np.linalg.norm` (ord = 1, 2, inf) et `scipy.spatial.distance` contre tes fonctions

- La similarité cosinus qui correspond à d) ; pourquoi SciPy préfère une distance à une similarité :

### Ex M07.29 — Prédire : l'angle de deux vecteurs tirés au hasard en dimension 1 000

- Mes prédictions avant l'expérience (et pourquoi) ; ce que j'ai observé ; ce que cela dit des cosinus entre embeddings sans structure :

### Ex M07.30 — La norme d'un vecteur gaussien se concentre autour de √d

- Ce que dit d) de la dispersion relative ; c) comparé à 0,603 ; la limite apparente de l'écart-type de b) :

### Ex M07.31 — Médiane ou moyenne : le centre qui minimise les distances L1 ou leurs carrés, face à des points aberrants

- Pourquoi la médiane résiste aux points aberrants, et pas le barycentre ; lequel décrit le mieux le troupeau ; ce que confirme g) :

### Ex M07.32 — Les boules unités L1, L2, L∞ et Lp dans le plan

- Comment les courbes s'emboîtent, et l'inégalité entre normes que cela traduit ; pourquoi la courbe de p = 1/2 montre que ce n'est pas une norme :

### Ex M07.33 — Chasse à l'erreur : une distance sans racine, un cosinus mal normalisé, une projection sur un vecteur non unitaire

- Pour chaque ligne fausse, l'erreur et sa correction ; ce que calcule la ligne (E), et à quoi sert ce nombre :

### Ex M07.34 — Les normes de toutes les lignes d'un tableau : axis, keepdims et broadcasting

- Ce que donnerait np.sum(X ** 2, axis=0) ; pourquoi X / row_norms(X) échoue, ou se trompe quand X est carré ; le rapport des temps de calcul :

### Ex M07.35 — Défi : le point qui minimise la somme des distances (non au carré) à 60 villes, à 0,1 % près

- L'écart (en %) du barycentre et de la médiane coordonnée par coordonnée ; l'idée de ma méthode ; la position du point trouvé par rapport au groupe de 26 villes, et pourquoi :
