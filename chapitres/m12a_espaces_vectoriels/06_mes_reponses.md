# M12a · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m12a_espaces_vectoriels/06_mes_reponses.md` (créée par `python tools/start_chapter.py M12a`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Dis où vit chaque objet (dans quel $\mathbb{R}^n$) avant de calculer, écris chaque opération sur les lignes ($L_2 \leftarrow L_2 - 2L_1$) avant son résultat, et vérifie chaque combinaison, chaque vecteur du noyau et chaque coordonnée en recalculant. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M12a.Q1 — Sous-espace ou pas ?

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.Q2 — Combinaison linéaire et famille génératrice

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.Q3 — Libre ou liée ?

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.Q4 — Base et dimension : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.Q5 — Le rang d'une matrice, d'une transposée, d'un produit

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.Q6 — Linéaire, affine, ou ni l'un ni l'autre ?

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.Q7 — Noyau et image : qui vit où ?

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.Q8 — Changer de base : ce qui change et ce qui reste

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M12a.R1 — Le pivot de Gauss et la forme échelonnée réduite (M09a)

1. 
2. 
3. 
4. 
5. 
6. 

### M12a.R2 — Produit matriciel et formes (M09a)

1. 
2. 
3. 
4. 
5. 

### M12a.R3 — Combinaisons linéaires et produit scalaire dans ℝⁿ (M07)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M12a.1 — Reconnaître des sous-espaces de ℝ³ et de l'espace des polynômes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les trois conditions pour chaque `True`, un contre-exemple précis pour chaque `False` ; pour d), la stabilité par multiplication, puis par addition :

### Ex M12a.2 — Écrire un vecteur comme combinaison linéaire : un système à résoudre

- a :
- b :
- c :
- d :
- e :
- f :
- Le plan Vect(u₁, u₂) par une équation, et b) et c) retrouvés avec elle ; pourquoi trois équations pour deux inconnues en a) :

### Ex M12a.3 — L'indépendance de trois vecteurs de ℝ³ par le pivot de Gauss

- a :
- b :
- c :
- d :
- e :
- f :
- « Deux à deux non colinéaires » suffisait-il pour b) ? Ce que voudrait dire, géométriquement, que trois vecteurs de ℝ³ soient liés :

### Ex M12a.4 — Extraire une base d'une famille génératrice, compléter une famille libre

- a :
- b :
- c :
- d :
- e :
- f :
- Ce que forment les colonnes à pivot de b), et s'il faut vérifier qu'elles engendrent ; ce que dit e) sur le choix à faire en f) :

### Ex M12a.5 — Les coordonnées d'un vecteur dans une base qui n'est pas la base canonique

- a :
- b :
- c :
- d :
- e :
- f :
- (b₁, b₂, b₃) est une base ; a) vérifié par la combinaison ; la matrice des coordonnées de e₁, e₂, e₃ :

### Ex M12a.6 — Le rang par les colonnes et par les lignes, celui d'un produit, et celui d'un tableau centré

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La relation entre les lignes de A ; A fois les deux premières colonnes de C, et la conclusion pour e) ; la combinaison nulle des lignes d'un tableau centré, et ce qu'elle dit de son rang :

### Ex M12a.7 — La matrice d'une application linéaire : les images des vecteurs de base

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- e₁ et e₂ écrits avec (1, 1) et (1, −1) ; les images de (1, 1) et de (1, −1) par la projection de f) :

### Ex M12a.8 — Composer deux applications du plan, c'est multiplier leurs matrices

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- c) vérifié en appliquant a puis b ; pourquoi « a puis b » a pour matrice BA ; b⁻¹ décrite en mots :

### Ex M12a.9 — Noyau et image d'une matrice 3 × 4, et le théorème du rang

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- A x = 0 vérifié pour d) et e), lus comme des relations entre colonnes ; le théorème du rang ; A injective ? surjective ? :

### Ex M12a.10 — Toutes les solutions de A x = b : une solution particulière plus le noyau

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- L'ensemble des solutions sous la forme x_p + s k₁ + t k₂ ; f), si c'est une solution, sous cette forme ; la relation entre les lignes qui explique g) :

### Ex M12a.11 — Une base adaptée qui rend diagonale la matrice d'une application : S⁻¹AS

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Ce que montrent a) et b), et comment cela se voit dans d) ; g) vérifié directement ; A appliquée dix fois à x :

### Ex M12a.12 — Une application affine du plan : partie linéaire, translation, inverse

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- f) vérifié par φ ; φ(0, 0), φ(2, 2), leur milieu comparé à g), et la propriété du cours :

### Ex M12a.13 — La dérivation sur les polynômes de degré au plus 3 : matrice, noyau, image

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- ker D et Im D en mots ; le théorème du rang ; D est-elle inversible ? « Dériver » se défait-il par une primitive ? :

## ∂ Démonstrations

### Ex M12a.14 — L'intersection de deux sous-espaces en est un ; la réunion, presque jamais

1. 
2. 
3. 
4. 
5. 

### Ex M12a.15 — Les coordonnées dans une base sont uniques

1. 
2. 
3. 
4. 

### Ex M12a.16 — Le noyau est un sous-espace, et une application linéaire est injective si et seulement si son noyau est {0}

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M12a.17 — Le théorème du rang : dim ker + rang = nombre de colonnes

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M12a.18 — rg(AB) ≤ min(rg A, rg B)

1. 
2. 
3. 
4. 
5. 

### Ex M12a.19 — L'inverse d'une application affine bijective est affine

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12a.20 — Pont : une feature somme de deux autres rend XᵀX singulière, et le noyau dit laquelle

- a :
- b :
- c :
- d :
- e :
- f :
- e) comparé à X w ; ce que dit d sur les features ; XᵀX inversible ? une méthode peut-elle choisir entre w et w′, et pourquoi ; une colonne « total » chronométrée :

### Ex M12a.21 — Pont : projeter sur un plan puis revenir, ce que la transformation inverse ne peut pas rendre

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- E(1, 2, 0) comparé à c) ; E D, et ce qu'il dit de l'erreur de g) ; les vecteurs reconstruits exactement ; d) par le rang d'un produit :

### Ex M12a.22 — MML §2.4 et §2.5 : espaces vectoriels, sous-espaces et indépendance, en anglais

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M12a.23 — MML §2.6 à §2.8 : base, rang, applications linéaires, changement de base, espaces affines

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M12a.24 — Fermi : les paramètres d'une application linéaire, puis affine, d'images 32 × 32 en couleurs vers 100 classes

1. 
2. 
3. 
4. 
5. 

### Ex M12a.25 — Expliquer la dimension et le rang sans une seule formule

*Ton explication, en huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M12a.E1 — « Que veut dire qu'une matrice est de rang plein, et pourquoi s'en soucier ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M12a.E2 — « Qu'est-ce que le noyau d'une matrice, et où le croise-t-on en ML ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M12a.26 — Tester l'indépendance et extraire une base de l'espace des colonnes · `is_independent, column_space_basis`

- La colonne de b) qui combine les autres, et ses coefficients ; pourquoi c) est liée sans calcul ; pourquoi la première colonne manque en e) :

### Ex M12a.27 — Une base du noyau, colonne libre par colonne libre · `null_space_basis`

- a) lu comme deux relations entre colonnes ; pourquoi c) a zéro colonne et d) trois ; le théorème du rang pour e) :

### Ex M12a.28 — Coordonnées dans une base et changement de base · `coordinates, change_of_basis`

- a) vérifié par la combinaison des colonnes ; pourquoi c) lève une erreur ; les colonnes de S en d) :

### Ex M12a.29 — `sympy.Matrix.nullspace`, `columnspace` et `rank` contre tes fonctions

- Les relations entre les colonnes de P que disent les vecteurs du noyau ; pourquoi f) donne le même nombre que a) :

### Ex M12a.30 — Prédire le rang : matrices aléatoires, produits, colonnes répétées

- Mes prédictions avant l'expérience (et pourquoi) ; pourquoi une matrice tirée au hasard est de rang plein ; la règle qui explique b) ; les lignes de e) comme combinaisons de deux vecteurs :

### Ex M12a.31 — Le rang numérique : une colonne presque redondante et le choix de la tolérance

- Le « bon » rang pour k = 12 ; pourquoi l'échelle 10⁶ change le rang de mes pivots et pas celui de matrix_rank ; la tolérance pour des mesures à 4 chiffres significatifs :

### Ex M12a.32 — Une application linéaire du plan : l'image du carré unité, et ce qu'elle écrase quand son noyau n'est pas nul

- Ce que devient le carré par la matrice de rang 1 ; pourquoi chaque segment va sur un point, et où ; pourquoi aucune matrice ne défait la transformation :

### Ex M12a.33 — Chasse à l'erreur : une « base » liée, un noyau faux, S⁻¹AS écrit à l'envers

- Pour chaque ligne fausse, l'erreur et sa correction ; la plus dangereuse, et pourquoi :

### Ex M12a.34 — Un test de propriété : A fois une base du noyau donne 0, et le théorème du rang sur des matrices aléatoires

- La propriété qui attrape le noyau fait de zéros, et pourquoi les autres le laissent passer ; celle qui attrape l'image faite de toutes les colonnes ; un noyau multiplié par 2 :

### Ex M12a.35 — Défi : retrouver les relations linéaires exactes cachées entre les colonnes d'un tableau, sans en inventer

- La tolérance choisie, et pourquoi ; ce qui se passe avec 10⁻⁵, et sans changer d'échelle ; le choix de la tolérance sur de vraies mesures :
