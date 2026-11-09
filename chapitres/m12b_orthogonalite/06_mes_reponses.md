# M12b · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m12b_orthogonalite/06_mes_reponses.md` (créée par `python tools/start_chapter.py M12b`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Dis pour quel produit scalaire tu calcules, vérifie chaque orthogonalité et chaque norme en recalculant, et garde les fractions jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5), un produit scalaire avec `\langle \mathbf{x}, \mathbf{y} \rangle`, une matrice avec `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M12b.Q1 — Produit scalaire ou pas ? Symétrie et positivité

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.Q2 — Orthogonale, orthonormée, matrice orthogonale

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.Q3 — Gram-Schmidt : ce que chaque étape retire

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.Q4 — Le complément orthogonal : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.Q5 — Une matrice de projection : sur quoi, et quelles propriétés ?

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.Q6 — Moindres carrés et projection

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.Q7 — QR : formes et propriétés

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.Q8 — Des fonctions orthogonales

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M12b.R1 — La projection sur une droite (M07)

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.R2 — Les équations normales et la matrice chapeau (M09b)

1. 
2. 
3. 
4. 
5. 
6. 

### M12b.R3 — Base, rang et noyau (M12a)

1. 
2. 
3. 
4. 
5. 
6. 

## ✏️ Papier-crayon

### Ex M12b.1 — Un produit scalaire défini par une matrice 2 × 2 : normes, angles, orthogonalité

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- xᵀMx en somme de deux carrés ; f) avec le produit usuel ; une base orthonormée pour ⟨·,·⟩_M qui contient e₂ ; pour h), un vecteur précis :

### Ex M12b.2 — Les coordonnées dans une base orthonormée : des produits scalaires au lieu d'un système

- a :
- b :
- c :
- d :
- e :
- f :
- Deux autres paires orthogonales et une norme ; c) vérifié en recombinant ; pourquoi la dernière coordonnée de f) diffère, et dans quel rapport ; le coût d'un système 4 × 4 :

### Ex M12b.3 — Une matrice orthogonale 3 × 3 conserve normes et angles

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- c) comparé à ‖x‖, d) à x · y ; les deux angles ; pourquoi e) ne demande aucun pivot ; Q est-elle symétrique ? :

### Ex M12b.4 — Gram-Schmidt sur trois vecteurs de ℝ³

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les trois orthogonalités et les trois normes ; a₂ et a₃ en combinaisons de q₁, q₂, q₃ ; l'étape 3 refaite avec le procédé modifié :

### Ex M12b.5 — Gram-Schmidt pour un produit scalaire qui n'est pas l'usuel

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- ⟨q₁, q₂⟩_D, ‖q₂‖_D, puis q₁ · q₂ pour le produit usuel ; x − h) orthogonal à a₁ et a₂ pour ⟨·,·⟩_D, et pour le produit usuel ? :

### Ex M12b.6 — Une base du complément orthogonal d'un plan de ℝ⁴

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- U⊥ comme noyau d'une matrice ; b) et c) vérifiés ; g) de deux façons ; comment obtenir une base orthonormée de U⊥ :

### Ex M12b.7 — Projeter sur un plan de ℝ³ : avec une base quelconque, puis orthonormée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- d) retrouvé avec e) ; q₁ et q₂ dans U (combinaisons de a₁, a₂) et orthonormés ; la méthode pour projeter dix vecteurs :

### Ex M12b.8 — La matrice de projection : P² = P, Pᵀ = P, trace et rang

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- P² ; une équation du plan U à partir de b), et pourquoi c) était prévisible ; la droite de I − P ; M², Mᵀ et un dessin de ce que fait M :

### Ex M12b.9 — La distance d'un point à un sous-espace, et le résidu orthogonal

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- e) orthogonal à u₁ et u₂ ; Pythagore avec ‖v‖² ; pourquoi g) ≥ f) :

### Ex M12b.10 — Des moindres carrés comme une projection : y, son projeté et le résidu

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La somme des résidus, et pourquoi ; Pythagore avec ‖y‖² ; la projection sur la base orthogonale (1, x − x̄1) :

### Ex M12b.11 — La décomposition QR d'une matrice 3 × 2, puis les moindres carrés par R w = Qᵀy

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- A = QR colonne par colonne ; les équations normales, comparées ; h) orthogonal aux colonnes ; la ligne résolue en premier, et pourquoi :

### Ex M12b.12 — Le produit scalaire de fonctions sur [−1 ; 1] : orthogonaliser 1, x et x²

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Pourquoi p₁ = x ; le calcul de f) et g) ; |x| et son projeté dessinés ; le projeté sur Vect(1, x) seul :

## ∂ Démonstrations

### Ex M12b.13 — L'inégalité de Cauchy-Schwarz pour tout produit scalaire

1. 
2. 
3. 
4. 
5. 

### Ex M12b.14 — Une famille orthogonale de vecteurs non nuls est libre

1. 
2. 
3. 
4. 
5. 

### Ex M12b.15 — Gram-Schmidt donne une base orthonormée du même sous-espace

1. 
2. 
3. 
4. 
5. 

### Ex M12b.16 — L'orthogonal de l'image de A est le noyau de Aᵀ

1. 
2. 
3. 
4. 
5. 

### Ex M12b.17 — Le projeté orthogonal est le point le plus proche (Pythagore)

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12b.18 — Pont : retirer d'une feature ce qu'explique une autre, une projection puis un résidu

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- f) comparé à g) ; pourquoi Vect(x₁, x₂) = Vect(x₁, r) ; les prédictions avec x₁ et r ; « l'effet de x₂ à x₁ fixé » ; un r presque nul :

### Ex M12b.19 — Pont : projeter sur k directions orthonormées, reconstruire, et l'erreur par Pythagore

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- f) comparé aux carrés de g), et ‖x‖² à ‖z‖² + ‖e‖² ; la démonstration pour une base orthonormée quelconque ; ce que vaut U Uᵀ :

### Ex M12b.20 — MML §3.2, §3.5 à §3.7 : produits scalaires, orthogonalité, fonctions, en anglais

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M12b.21 — MML §3.8 et §9.4 : projections, Gram-Schmidt et moindres carrés

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

### Ex M12b.22 — Fermi : le coût de Gram-Schmidt sur une matrice 100 000 × 50

1. 
2. 
3. 
4. 
5. 

### Ex M12b.23 — Expliquer pourquoi le projeté est le point le plus proche

*Ton explication, en huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M12b.E1 — « Pourquoi résoudre des moindres carrés par QR plutôt que par les équations normales ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M12b.E2 — « Qu'est-ce qu'une matrice orthogonale, et pourquoi est-elle agréable en calcul numérique ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M12b.24 — Gram-Schmidt, classique et modifié · `gram_schmidt`

- a) retrouvé à la main ; pourquoi d) a des −1 ; pourquoi e) lève une erreur, et ce que vaut v₂ :

### Ex M12b.25 — La projection orthogonale sur un sous-espace · `project`

- La droite de régression de a) ; b) par la formule de M07 ; pourquoi e) était prévisible :

### Ex M12b.26 — La décomposition QR et les moindres carrés par QR · `qr, least_squares_qr`

- a) à la main ; R et Qᵀy pour d), et la résolution ; pourquoi np.triu en c) :

### Ex M12b.27 — `np.linalg.qr` et `lstsq` contre ta projection et ta QR : les signes de Q et de R

- Pourquoi les valeurs absolues de R sont les mêmes ; ce que vérifie d) ; ce que lstsq rend pour A₄ :

### Ex M12b.28 — Prédire : Gram-Schmidt classique sur des vecteurs presque colinéaires, QᵀQ vaut-il encore I ?

- Mes prédictions avant l'expérience (et pourquoi) ; l'élément de QᵀQ loin de 0 ; pourquoi les normes restent à 1 ; ce que perd le procédé classique :

### Ex M12b.29 — Gram-Schmidt classique contre modifié : l'orthogonalité perdue quand les colonnes sont presque dépendantes

- Le facteur de croissance des deux écarts d'un degré au suivant ; pourquoi orthogonaliser deux fois répare ; mon choix pour une régression de degré 10 :

### Ex M12b.30 — Projeter un nuage de ℝ³ sur un plan : les résidus orthogonaux en image

- Les segments perpendiculaires au plan ? la perspective ; le point le plus loin du plan ; une autre base du même plan :

### Ex M12b.31 — Chasse à l'erreur : une normalisation oubliée, QQᵀ sur une base non orthonormée, R w = Qᵀy résolu dans le mauvais sens

- Pour chaque ligne fausse, l'erreur et sa correction ; la plus dangereuse, et pourquoi :

### Ex M12b.32 — Un test de propriétés pour la projection : idempotente, symétrique, résidu orthogonal

- Les propriétés qui attrapent chaque copie fausse, et celle qui la laisse passer ; pourquoi k < m ; une fonction fausse qui passerait tout :

### Ex M12b.33 — Défi : des colonnes presque dépendantes, des moindres carrés à 1e−8 près de `lstsq` par l'orthogonalisation de [X | y]

- Pourquoi R = QᵀX recalculé est moins précis ; ce que représente le dernier élément diagonal de R ; une autre voie :
