# M09a · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m09a_matrices/06_mes_reponses.md` (créée par `python tools/start_chapter.py M09a`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris la forme de chaque matrice avant de calculer un produit, chaque opération sur les lignes ($L_2 \leftarrow L_2 - 2L_1$) avant son résultat, et vérifie une solution dans les équations de départ ; garde les fractions exactes ($\frac{5}{3}$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M09a.Q1 — Formes : ce qui se multiplie et ce qui ne se multiplie pas

1. 
2. 
3. 
4. 
5. 
6. 

### M09a.Q2 — Le produit matrice-vecteur, deux lectures

1. 
2. 
3. 
4. 
5. 

### M09a.Q3 — Produit matriciel : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M09a.Q4 — Hadamard ou produit matriciel ?

1. 
2. 
3. 
4. 
5. 
6. 

### M09a.Q5 — Les règles de la transposée

1. 
2. 
3. 
4. 
5. 
6. 

### M09a.Q6 — Combien de solutions ?

1. 
2. 
3. 
4. 
5. 
6. 

### M09a.Q7 — Les opérations permises sur les lignes

1. 
2. 
3. 
4. 
5. 
6. 

### M09a.Q8 — Inverse et rang

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M09a.R1 — Les systèmes 2 × 2 (R2)

1. 
2. 
3. 
4. 
5. 

### M09a.R2 — Produit scalaire et normes (M07)

1. 
2. 
3. 
4. 
5. 

### M09a.R3 — Moyenne et écart-type empiriques (M02c)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M09a.1 — Un tableau de données vu comme une matrice : forme, lignes, colonnes, moyennes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Ce que représentent une ligne et une colonne ; pourquoi centrer retire le même vecteur à chaque ligne ; la moyenne de chaque colonne du tableau centré :

### Ex M09a.2 — Le produit matrice-vecteur, par les lignes puis par les colonnes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- b) refait par la lecture en colonnes ; pourquoi d) donne une colonne de A ; le coût de g) pour un million d'exemples à 20 features :

### Ex M09a.3 — Produits matriciels à la main : formes compatibles et calculs

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- d) comme un produit scalaire d'une ligne et d'une colonne ; A(BC) comparé à g) ; pourquoi AB = BA n'a ici aucun sens :

### Ex M09a.4 — Le coût d'un produit, et l'ordre des parenthèses dans ABC

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La règle simple pour choisir les parenthèses ; l'ordre de f), et le coût de ((AB)C)D ; pourquoi le résultat est le même dans tous les ordres :

### Ex M09a.5 — Une couche dense Z = XW + b à la main : deux exemples, trois entrées, deux sorties

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La colonne de W qui contient les poids du neurone 2 ; pourquoi b est ajouté à chaque ligne ; la forme de Z pour un batch de 128 exemples :

### Ex M09a.6 — Un embedding : une ligne one-hot fois une matrice

- a :
- b :
- c :
- d :
- e :
- f :
- Pourquoi on ne calcule jamais ce produit en pratique ; ce que représente la ligne de comptage de f) :

### Ex M09a.7 — Transposées de produits, et la matrice symétrique XᵀX

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- b) vérifié par BᵀAᵀ ; ce que représentent la diagonale de XᵀX et un zéro hors de la diagonale ; ce que dit g) des exemples 1 et 2 :

### Ex M09a.8 — Le pivot de Gauss sur un système 3 × 3 à solution unique

- a :
- b :
- c :
- d :
- e :
- f :
- La forme échelonnée complète, puis la forme échelonnée réduite ; la vérification dans les trois équations ; pourquoi l'échange du début ne change pas les solutions :

### Ex M09a.9 — Un système sans solution, un système à une infinité de solutions

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La solution générale de (S₂) avec un paramètre t ; la différence des solutions de e) et f) dans le système homogène ; pourquoi g) était prévisible :

### Ex M09a.10 — La forme échelonnée réduite d'une matrice 3 × 4 et la solution générale

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La solution générale, « une solution particulière plus t fois une solution du système homogène » ; la variable libre, et pourquoi :

### Ex M09a.11 — L'inverse d'une matrice 2 × 2, par la formule, puis vérifiée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- AA⁻¹ et A⁻¹A ; pourquoi X = A⁻¹C et pas CA⁻¹ en d) ; e) et f) justifiés par les règles de la fiche ; (A²)⁻¹ = (A⁻¹)², et l'origine du 16 :

### Ex M09a.12 — L'inverse d'une matrice 3 × 3 par Gauss-Jordan

- a :
- b :
- c :
- d :
- e :
- Chaque étape de la réduction de [A | I₃] ; pourquoi c) est une colonne de A⁻¹ ; ce qui se passe en réduisant [B | I₃] :

### Ex M09a.13 — Le rang de quatre matrices, et les colonnes redondantes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Les colonnes 3 et 4 de M₃ comme combinaisons des colonnes 1 et 2 ; pourquoi le rang de M₄ se lit sans calcul :

### Ex M09a.14 — Mettre un problème en système : trois engrais pour trois nutriments

- a :
- b :
- c :
- d :
- e :
- Pourquoi la solution de e) n'a pas de sens pour le jardinier ; ce qu'aurait signifié une matrice A singulière :

## ∂ Démonstrations

### Ex M09a.15 — (AB)ᵀ = BᵀAᵀ, coefficient par coefficient

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09a.16 — L'inverse est unique, et (AB)⁻¹ = B⁻¹A⁻¹

1. 
2. 
3. 
4. 
5. 

### Ex M09a.17 — Deux solutions distinctes entraînent une infinité de solutions

1. 
2. 
3. 
4. 
5. 

### Ex M09a.18 — Une matrice dont une colonne combine les autres n'est pas inversible

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09a.19 — Pont : une passe avant à deux couches, deux produits matriciels et leurs formes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- b₁W₂ + b₂ ; la sortie de x sans ReLU, comparée à x(W₁W₂) + (b₁W₂ + b₂), et pourquoi en développant :

### Ex M09a.20 — Pont : centrer et réduire un tableau en écriture matricielle

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Pourquoi multiplier à droite par D⁻¹ divise chaque colonne par son écart-type ; la diagonale de (1/3) XₛᵀXₛ, et pourquoi ; le nom de l'élément de g) :

### Ex M09a.21 — MML §2.1 et §2.2 : systèmes et matrices, en anglais

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09a.22 — MML §2.3 : résoudre un système, la forme échelonnée et le « Minus-1 trick »

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09a.23 — Fermi : combien de multiplications pour une passe avant sur un million d'images ?

1. 
2. 
3. 
4. 
5. 

### Ex M09a.24 — Expliquer pourquoi on ne calcule pas l'inverse pour résoudre un système

*Huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M09a.E1 — « Combien coûte un produit matriciel, et pourquoi les GPU l'accélèrent-ils ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M09a.25 — Le produit matriciel et la transposée · `matmul, transpose`

- a) et b) calculés à la main ; le nombre de multiplications de a) ; pourquoi transpose doit renvoyer un nouveau tableau :

### Ex M09a.26 — La forme échelonnée réduite et le rang · `rref, rank`

- Pourquoi la deuxième colonne n'a pas de pivot en a) ; les lignes de d) qui combinent les autres :

### Ex M09a.27 — Résoudre un système par le pivot de Gauss · `solve`

- a) vérifié dans les trois équations ; c) sans pivot partiel ; pourquoi d) est singulière :

### Ex M09a.28 — L'inverse par Gauss-Jordan · `inverse`

- b) comparé à la transposée de la matrice ; pourquoi c) est singulière :

### Ex M09a.29 — `@`, `*`, `.T`, `np.linalg.solve`, `matrix_rank` et `sympy.Matrix.rref` contre tes fonctions

- L'élément (1, 2) de a) à la main ; ce que donnerait A * B, et pourquoi :

### Ex M09a.30 — Prédire la forme du résultat : `@`, `*` et broadcasting

- Mes prédictions avant l'expérience (et pourquoi) ; pourquoi a) rend un tableau à deux dimensions et b) à une seule ; pourquoi d) marche et pas e) ; un tableau (2, 1) pour e) :

### Ex M09a.31 — Le temps d'un produit matriciel en fonction de n : une pente de 3 en échelle log-log

- La pente mesurée, et pourquoi elle n'est pas exactement 3 ; pourquoi garder le plus petit de trois temps ; combien de fois @ est plus rapide :

### Ex M09a.32 — Pourquoi le pivot partiel : un petit pivot et les arrondis

- Le multiplicateur 1/ε et ce qu'il fait à la seconde équation ; pourquoi échanger les lignes règle le problème ; pourquoi l'erreur croît comme 10⁻¹⁶/ε :

### Ex M09a.33 — Une matrice 2 × 2 comme transformation du plan : la grille et le carré unité

- Où vont e₁ et e₂ pour chaque matrice ; ce que devient le carré unité pour la matrice singulière, et pourquoi ; la matrice qui défait la rotation :

### Ex M09a.34 — Chasse à l'erreur : `*` au lieu de `@`, une transposée oubliée, un pivot nul

- Pour chaque ligne fausse, l'erreur et sa correction ; la forme du résultat de (D), et pourquoi Python ne signale rien :

### Ex M09a.35 — Tester une propriété : un pytest pour (AB)ᵀ = BᵀAᵀ sur des matrices aléatoires

- Les formes pour lesquelles la transposée par reshape est juste, et pourquoi un test limité à ces formes la laisserait passer ; pourquoi le produit de Hadamard passe le test ; ce qu'il faut ajouter pour l'attraper :

### Ex M09a.36 — Défi : un système 400 × 400 résolu par ton `solve`, à 1e−9 près de NumPy, en moins d'une seconde

- Le temps de ma première version et de la version finale ; l'opération vectorisée ; pourquoi le troisième système échoue sans pivot partiel :
