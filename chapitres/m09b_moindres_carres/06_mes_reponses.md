# M09b · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m09b_moindres_carres/06_mes_reponses.md` (créée par `python tools/start_chapter.py M09b`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris la forme de chaque matrice avant un produit ($\mathbf{X}^\top$ est $(p, n)$), chaque somme de carrés terme à terme, et vérifie une solution des équations normales par $\mathbf{X}^\top\mathbf{r} = \mathbf{0}$ ; garde les fractions exactes ($\frac{7}{9}$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M09b.Q1 — MSE, RMSE, MAE, R² : ce que mesure chacune

1. 
2. 
3. 
4. 
5. 
6. 

### M09b.Q2 — Gradients matriciels : associer chaque fonction à son gradient

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

### M09b.Q3 — Équations normales : quand la solution est-elle unique ?

1. 
2. 
3. 
4. 
5. 
6. 

### M09b.Q4 — Linéaire en x ou linéaire en w ?

1. 
2. 
3. 
4. 
5. 
6. 

### M09b.Q5 — Ridge : vrai ou faux sur la pénalité L2

1. 
2. 
3. 
4. 
5. 
6. 

### M09b.Q6 — Lasso ou ridge : qui annule des poids ?

1. 
2. 
3. 
4. 
5. 
6. 

### M09b.Q7 — Bruit gaussien et moindres carrés

1. 
2. 
3. 
4. 
5. 
6. 

### M09b.Q8 — Biais, variance, bruit : ce qui change quand le modèle se complique

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M09b.R1 — Le pivot de Gauss et l'inverse (M09a)

1. 
2. 
3. 
4. 
5. 

### M09b.R2 — Maximum de vraisemblance et MAP (M04)

1. 
2. 
3. 
4. 
5. 

### M09b.R3 — Gradient et point critique (M05b)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M09b.1 — MSE, RMSE, MAE et loss de Huber de quatre résidus

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- L'unité de chaque résultat ; pourquoi f) vaut la moitié de b) ; le R² déduit de b) et de g) :

### Ex M09b.2 — La décomposition SCT = SCE + SCR et le R² d'un ajustement donné

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- SCT = SCE + SCR vérifié pour la première droite, pas pour la seconde ; Σ rᵢ et Σ xᵢrᵢ pour chaque droite, et la condition qui manque ; les deux R² de la seconde droite :

### Ex M09b.3 — Les gradients de aᵀw, wᵀAw et ‖y − Xw‖², composante par composante en dimension 2

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- wᵀAw développé et d) par les dérivées partielles, comparé à (A + Aᵀ)w et à 2Aw ; ‖y − Xw‖² en trois carrés, dérivé par rapport à w₁ :

### Ex M09b.4 — Les équations normales d'un modèle à deux features, sans ordonnée à l'origine

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Ce que veut dire f) géométriquement ; la somme des résidus, et pourquoi elle n'est pas forcément nulle :

### Ex M09b.5 — La colonne de 1 : l'ordonnée à l'origine et des résidus de moyenne nulle

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La droite de c) passe par le point de f) ; XᵀX après centrage, et pourquoi elle est diagonale ; l'équation qui donne w₀ :

### Ex M09b.6 — La matrice chapeau d'un petit tableau : H² = H et sa trace

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Une ligne de HH ; pourquoi le point de e) ; H appliquée à la colonne de 1 et à (0, 1, 3), et pourquoi :

### Ex M09b.7 — Compter les monômes des features polynomiales

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La liste des monômes de a) ; carrés et interactions de e) ; le nombre de colonnes degré par degré pour g) :

### Ex M09b.8 — Ridge en dimension 2 : résoudre (XᵀX + λI)w = Xᵀy pour trois valeurs de λ

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La limite de λw quand λ → +∞ ; pourquoi f) augmente avec λ :

### Ex M09b.9 — Ridge comme MAP : un prior gaussien et λ = σ²/τ²

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le log du posterior de c), et pourquoi il est maximal au point de c) ; ce que devient le prior quand τ → +∞ :

### Ex M09b.10 — Les pénalités L1 et L2 de trois vecteurs de poids, et leurs boules

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Les deux boules dessinées, avec les points de d) et de e) ; ce que disent a) et b) sur un poids concentré ou réparti :

### Ex M09b.11 — La log-vraisemblance gaussienne d'un modèle linéaire et l'estimation de σ²

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- c) écrit −(n/2)(ln(2πσ̂²) + 1) ; ce que dit g) avec un bruit de Laplace :

### Ex M09b.12 — L'estimateur rétréci c·x̄ : biais, variance et erreur quadratique

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- E(c), sa dérivée et la formule du c optimal ; pourquoi on ne peut pas l'utiliser tel quel ; ce qu'il devient quand n grandit :

## ∂ Démonstrations

### Ex M09b.13 — Le gradient de wᵀAw vaut (A + Aᵀ)w

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09b.14 — Les équations normales en dimension n, par le gradient

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09b.15 — Le résidu est orthogonal aux colonnes de X ; H est symétrique et idempotente

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09b.16 — XᵀX + λI est inversible pour tout λ > 0

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09b.17 — Un bruit gaussien mène aux moindres carrés : le maximum de vraisemblance

1. 
2. 
3. 
4. 
5. 

### Ex M09b.18 — La décomposition biais² + variance + bruit, démontrée

1. 
2. 
3. 
4. 
5. 

### Ex M09b.19 — Le nombre de monômes de degré au plus d en p variables : C(p + d, d)

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09b.20 — Pont : la loss d'un modèle linéaire et son gradient pour un batch, prêts pour la descente de gradient

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Les formes de chaque étape ; le coût du gradient pour un batch de B exemples à p colonnes ; pourquoi diviser par n, et l'effet sur η :

### Ex M09b.21 — Pont : pourquoi standardiser les colonnes avant ridge

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le facteur de rétrécissement ‖xⱼ‖²/(‖xⱼ‖² + λ) pour des colonnes orthogonales ; pourquoi une petite unité épargne une feature :

### Ex M09b.22 — MML §5.5, §8.1 et §8.2 : identités de gradients et minimisation du risque empirique

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09b.23 — MML §9.1 et §9.2 : régression linéaire, maximum de vraisemblance et MAP

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M09b.24 — Fermi : la taille de XᵀX pour des features polynomiales de degré 3 sur 100 variables

1. 
2. 
3. 
4. 
5. 

### Ex M09b.25 — Expliquer la matrice chapeau : ce que veut dire « projeter y »

*Huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M09b.E1 — « Pourquoi ne pas inverser XᵀX, et que faire si des features sont colinéaires ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M09b.E2 — « Quel lien entre la régularisation L2 et un prior gaussien ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M09b.26 — Équations normales et résolution, avec ou sans ridge · `normal_equations, solve_least_squares`

- a), b) et c) à la main ; pourquoi e) est singulière et f) ne l'est plus ; pourquoi la solution de f) est proportionnelle à (1, 2) :

### Ex M09b.27 — La matrice chapeau et les trois sommes de carrés · `hat_matrix, residual_decomposition`

- Pourquoi les leviers des deux points extrêmes sont les plus grands ; SCT = SCE + SCR en d), et pourquoi c'est garanti :

### Ex M09b.28 — Compter les monômes, et la loss de Huber · `count_monomials, huber_loss`

- e) à la main, résidu par résidu ; c), et pourquoi ; les colonnes de degré 4 sur 30 variables, et la taille de XᵀX :

### Ex M09b.29 — `np.linalg.lstsq` et scikit-learn contre tes équations normales

- Pourquoi a) et b) sont égaux ; pourquoi d) et e) diffèrent, surtout sur l'ordonnée à l'origine ; pourquoi lstsq est préférable quand des colonnes sont presque dépendantes :

### Ex M09b.30 — Prédire : le R² d'entraînement quand on ajoute une feature de pur bruit

- Mes prédictions avant l'expérience (et pourquoi) ; pourquoi le R² d'entraînement ne baisse jamais ; ce qui se passe pour k = 18 ; pourquoi le R² de test baisse, et le terme de la fiche §8 qui grandit :

### Ex M09b.31 — Simuler l'estimateur rétréci c·x̄ : le c qui minimise l'erreur quadratique

- Le gain de c*x̄ sur x̄ ; pourquoi rétrécir aide quand σ²/n est grand devant μ² ; le lien avec ridge :

### Ex M09b.32 — Le conditionnement de XᵀX avec des puissances non standardisées

- Pourquoi x⁴ et x⁵ sont presque proportionnelles sur [0, 20] ; pourquoi les poids bougent beaucoup et les prédictions presque pas ; quand cela devient grave :

### Ex M09b.33 — Les lignes de niveau de la loss des moindres carrés en dimension 2, et son gradient

- Pourquoi des ellipses ; pourquoi allongées et penchées avec x brut, alignées avec x centré (XᵀX dans les deux cas) ; les flèches pointent-elles vers le minimum, et ce qu'on en déduit pour une descente de gradient :

### Ex M09b.34 — Chasse à l'erreur : XXᵀ au lieu de XᵀX, un gradient de mauvais signe, un R² sans centrer

- Pour chaque ligne fausse, l'erreur et sa correction ; la forme du résultat de (A), et pourquoi Python ne signale rien ; pourquoi (D) est juste :

### Ex M09b.35 — Vérifier un gradient matriciel avec SymPy et par différences finies

- Pourquoi des différences centrées ; pourquoi pas h = 10⁻¹² ; pourquoi diviser par la taille du gradient ; le coût d'un gradient numérique, et pourquoi on n'entraîne pas un réseau ainsi :

### Ex M09b.36 — Défi : approcher une fonction par un polynôme de degré au plus 5, avec une erreur maximale sous 1e−3

- L'erreur de ma première version, et où elle était la plus grande ; ce que j'ai changé ; pourquoi les moindres carrés ne minimisent pas l'erreur maximale ; un degré 4 suffit-il :
