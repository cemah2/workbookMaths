# M12d · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m12d_svd_acp/06_mes_reponses.md` (créée par `python tools/start_chapter.py M12d`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque SVD en refaisant le produit $\mathbf{U}\mathbf{S}\mathbf{V}^\top$, contrôle que la somme des $s_i^2$ est la somme des carrés des éléments, et que la somme des variances le long des axes est la trace de la covariance. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} a & b \\ c & d \end{pmatrix}`, une norme avec `\lVert \mathbf{A} \rVert_F` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M12d.Q1 — La SVD : formes et propriétés

1. 
2. 
3. 
4. 
5. 
6. 

### M12d.Q2 — Valeurs singulières et valeurs propres

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

### M12d.Q3 — Rang faible : ce qu'on garde, ce qu'on perd

1. 
2. 
3. 
4. 
5. 
6. 

### M12d.Q4 — Pseudo-inverse et conditionnement

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M12d.Q5 — Ce que maximise un axe principal

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M12d.Q6 — Centrer et standardiser avant une ACP ?

1. 
2. 
3. 
4. 
5. 
6. 

### M12d.Q7 — Variance expliquée et nombre de composantes

1. 
2. 
3. 
4. 
5. 
6. 

### M12d.Q8 — ACP, t-SNE ou UMAP : qui garde quoi ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M12d.R1 — Valeurs propres et théorème spectral (M12c)

1. 
2. 
3. 
4. 
5. 

### M12d.R2 — La projection orthogonale (M12b)

1. 
2. 
3. 
4. 
5. 

### M12d.R3 — Moyenne, covariance et standardisation (M02c)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M12d.1 — La SVD d'une matrice 2 × 2 à la main, par AᵀA

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- u₂, et s₁u₁v₁ᵀ + s₂u₂v₂ᵀ = A ; le lien entre g) et c) ; pourquoi h) n'a rien à voir avec c) :

### Ex M12d.2 — La SVD compacte d'une matrice 3 × 2 de rang 1

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- A = a bᵀ et s₁ = ‖a‖ ‖b‖ ; la SVD compacte, et le nombre de nombres contre la SVD complète ; le signe de u₁ :

### Ex M12d.3 — Le cercle unité devient une ellipse : axes et demi-axes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le dessin ; pourquoi e) et f) sont entre les deux demi-axes ; le point du cercle envoyé au bout du petit axe :

### Ex M12d.4 — L'approximation de rang 1 d'une matrice 3 × 3 et son erreur

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Pourquoi la troisième colonne donne une valeur singulière à elle seule ; A − A₁ élément par élément ; l'erreur en norme spectrale ; ce que raconte A₁ :

### Ex M12d.5 — Compter les nombres stockés : une image en rang k

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- f) contre g) : la même information ? le meilleur à nombre égal ; pourquoi un format d'image compte des bits :

### Ex M12d.6 — La pseudo-inverse d'une matrice non inversible et la solution de norme minimale

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- A⁺ = Aᵀ / ‖A‖²_F pour une matrice de rang 1 ; l'ensemble des solutions, et pourquoi x⁺ est le plus proche de l'origine ; ce que représente h), et la distance minimale :

### Ex M12d.7 — Le conditionnement de trois matrices, et l'erreur relative sur une solution

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- κ par s₁² + s₂² et s₁s₂ ; pourquoi κ + 1/κ = 102 ; f) comparé à c) ; la perturbation qui atteint la borne ; ce que disent les déterminants :

### Ex M12d.8 — Les axes principaux d'un nuage de ℝ³ : covariance, polynôme caractéristique, variances et axes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- det(C − λI) développé et factorisé ; somme et produit des variances ; le deuxième axe sans calcul ; pourquoi h) est sous λ₁ :

### Ex M12d.9 — Scores, reconstruction et erreur de reconstruction moyenne avec deux composantes sur trois

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- f) par les sept scores sur u₃ ; d'où vient (n − 1)/n ; la mesure de x̂₇ qui n'a pas bougé, et pourquoi :

### Ex M12d.10 — La variance expliquée cumulée : combien de composantes pour 95 % ?

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Les deux courbes ; le coude ; les seuils contre le coude ; comment trancher pour un modèle :

### Ex M12d.11 — L'ACP par la SVD de la matrice centrée : σ² / (n − 1) donne les variances

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- h) = s₁u₁, de moyenne nulle et de variance λ₁ ; pourquoi au plus trois valeurs singulières non nulles ; l'erreur s²/n :

### Ex M12d.12 — L'ACP quand n < p : passer par la petite matrice XXᵀ

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Les trois vecteurs propres de G, et pourquoi (1, 1, 1) a une valeur propre nulle ; le deuxième axe ; le coût contre la matrice 5 × 5, et pour 500 images de 10⁴ pixels :

### Ex M12d.13 — Les probabilités de voisinage de t-SNE sur quatre points, et leur perplexité 2^H

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- c) sous forme exacte ; la perplexité quand σ → 0, et entre quelles valeurs elle varie ; pourquoi une dichotomie ; pourquoi p_{2|1} ≠ p_{1|2} :

## ∂ Démonstrations

### Ex M12d.14 — Les valeurs singulières sont les racines des valeurs propres de AᵀA

1. 
2. 
3. 
4. 
5. 

### Ex M12d.15 — La plus grande valeur singulière est le plus grand étirement : ‖A x‖ ≤ σ₁ ‖x‖

1. 
2. 
3. 
4. 
5. 

### Ex M12d.16 — L'erreur de l'approximation de rang k vaut la somme des σ² oubliés (Frobenius)

1. 
2. 
3. 
4. 
5. 

### Ex M12d.17 — La pseudo-inverse donne la solution des moindres carrés de plus petite norme

1. 
2. 
3. 
4. 
5. 

### Ex M12d.18 — L'erreur de reconstruction moyenne est la somme des variances oubliées

1. 
2. 
3. 
4. 
5. 

### Ex M12d.19 — Les scores de deux composantes principales sont décorrélés

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12d.20 — Pont : détecter une anomalie par son erreur de reconstruction

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Ce qu'a d'inhabituel r₂ ; pourquoi r₃ n'est pas signalé, et un second score qui le signale ; pourquoi fixer le seuil sur d'autres données :

### Ex M12d.21 — Pont : un changement d'unités diagonal D change Σ en DΣD, et les axes principaux avec ; la standardisation non

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- (DΣD)ᵢⱼ = dᵢdⱼΣᵢⱼ et la corrélation inchangée ; qui a « décidé » de la direction ; un dⱼ négatif :

### Ex M12d.22 — MML §4.5 à §4.7 : SVD, approximation de rang faible, phylogénie des matrices

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

### Ex M12d.23 — MML §10.1 à §10.6 : l'ACP du livre (la dérivation par Lagrange de §10.2 se survole : M13b la relit)

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

### Ex M12d.24 — Fermi : la mémoire et le temps d'une ACP sur un million de clients et 250 features

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M12d.25 — Expliquer la SVD comme « rotation, étirement, rotation »

*Ton explication, en huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M12d.E1 — « Comment choisissez-vous le nombre de composantes d'une ACP ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M12d.E2 — « Que dit le conditionnement d'une matrice ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M12d.26 — La SVD par les valeurs propres de AᵀA · `svd`

- a) à la main par AAᵀ, et pourquoi ses valeurs propres non nulles sont celles de AᵀA ; pourquoi d) n'a qu'une valeur singulière :

### Ex M12d.27 — Approximation de rang faible et conditionnement · `low_rank_approximation, condition_number`

- c) à la main ; pourquoi d) a un conditionnement infini ; ce que rend le rang plein :

### Ex M12d.28 — La pseudo-inverse · `pinv`

- a) à la main ; ce que vaut AA⁺ ; pourquoi e) donne deux valeurs si différentes, et laquelle préférer :

### Ex M12d.29 — Les axes principaux d'une matrice de covariance, et la variance expliquée · `principal_axes, explained_variance_ratio`

- a) et b) à la main par les blocs ; le signe de la première colonne ; la part cumulée des deux premiers axes :

### Ex M12d.30 — `np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA` contre tes fonctions : les signes

- Pourquoi deux SVD justes diffèrent par des signes, et lesquels ; le piège de np.cov ; pourquoi explained_variance_ ne dépend pas de la moyenne :

### Ex M12d.31 — Prédire l'allure des valeurs singulières d'une image, et le rang qui suffit

- Mes prédictions avant l'expérience (et pourquoi) ; pourquoi aucune valeur singulière nulle ; le bruit et le débruitage ; le piège de l'image non centrée :

### Ex M12d.32 — Compresser une image du domaine public : l'erreur en fonction du rang

- e) = √(1 − part au rang 50), et pourquoi ; le rang où la tasse se reconnaît, et le grain du bois ; 99 % et la compression ; pourquoi un JPEG fait mieux :

### Ex M12d.33 — La SVD par AᵀA contre `np.linalg.svd` : ce qu'on perd quand κ est grand

- La croissance de l'erreur avec κ, et pourquoi ; pourquoi c) reste vrai ; ce que disent e) et f) du rang :

### Ex M12d.34 — La SVD en images : Vᵀ, Σ puis U appliqués au cercle unité, étape par étape

- Rotation ou symétrie à la deuxième étape ; le sens des couleurs et le signe de det A ; l'aire de l'ellipse :

### Ex M12d.35 — Chasse à l'erreur : une ACP sans centrer, n et n − 1 mélangés, des axes lus en lignes au lieu de colonnes

- Pour chaque ligne fausse, l'erreur et sa correction ; la plus trompeuse ; celle qui passerait inaperçue ; le contrôle qui détecte chacune :

### Ex M12d.36 — Un test : la reconstruction de rang plein redonne X, et l'erreur décroît avec k

- La propriété qui attrape chaque ACP fausse ; pourquoi l'ACP sans centrer passe 1 et 2 ; une propriété pour des scores :

### Ex M12d.37 — Défi : compresser une image centrée en gardant 93 % de son énergie avec au plus 5 % des nombres

- La matrice décomposée, et pourquoi ses valeurs singulières décroissent plus vite ; mes réglages ; les défauts visibles :
