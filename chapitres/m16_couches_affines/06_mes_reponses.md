# M16 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m16_couches_affines/06_mes_reponses.md` (créée par `python tools/start_chapter.py M16`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : les formes d'un produit matriciel s'enchaînent, la dernière colonne d'une matrice homogène est $(0, \ldots, 0, 1)$, un nombre de chemins est un entier positif ou nul, une variance est positive et celle d'un produit dépasse le produit des variances. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, une puissance de matrice avec `\mathbf{A}^k` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M16.Q1 — Les formes de W, de b et de x W + b, dans chaque convention

1. 
2. 
3. 
4. 
5. 
6. 

### M16.Q2 — Coordonnées homogènes et composition : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M16.Q3 — Lire une matrice d'adjacence : degrés, arêtes, chemins, cycles

1. 
2. 
3. 
4. 
5. 
6. 

### M16.Q4 — Indépendantes, décorrélées, ou ni l'un ni l'autre ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M16.R1 — Le produit matriciel, ses formes et son coût (M09a)

1. 
2. 
3. 
4. 
5. 

### M16.R2 — La variance d'une somme de variables indépendantes (M02b)

1. 
2. 
3. 
4. 
5. 

### M16.R3 — Les valeurs propres d'une matrice triangulaire (M12c)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M16.1 — Une application affine de ℝ³ dans ℝ² dans les deux conventions : formes, transposée, nombre de paramètres

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- la ligne de W qui répartit x₃ et la colonne de la deuxième sortie ; d) comparé à a) ; pourquoi la ligne 1 de f) ne dépend que de (1, 0, 0) ; les lignes de W dans f), et la troisième ligne :

### Ex M16.2 — Rotation, homothétie puis translation du plan : la matrice homogène de la composée, et celle de la réciproque

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- a) vérifié sur (1, 0) ; f(x, y) en formule ; f) de deux façons et le retour en (2, 1) ; pourquoi e) et g) diffèrent :

### Ex M16.3 — Des rues à sens unique : degrés, matrice d'adjacence, et chemins de longueur 2 et 3 par ses puissances

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- les chemins de f) et de g) ; pourquoi aucune puissance de A n'est nulle ; les rues qu'on peut supprimer, et g) sans l'une d'elles :

### Ex M16.4 — Un planning de tâches : l'absence de cycle par les puissances de A, une numérotation qui la rend triangulaire, et le nombre de chemins entre deux tâches

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- pourquoi A n'est pas triangulaire au départ ; pourquoi e) est la seule numérotation possible ; la matrice renumérotée et A⁶ = 0 ; d) comme coefficient de (I − A)⁻¹ :

### Ex M16.5 — Un prix aléatoire fois une quantité indépendante : espérance et variance du produit

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- d) en trois termes, et celui qui domine ; la vérification de 1 + c_R² ; un prix et une quantité dépendants :

### Ex M16.6 — Des signes aléatoires d'amplitudes différentes sur des mesures corrélées : la variance d'une somme de produits

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- pourquoi d) n'est pas nul ; les covariances absentes de c) ; E[x₁²] et non V(x₁) dans e) ; l'hypothèse qui manque à f) et à g) ; g) écrit comme (x₁ + x₂ + x₃) + S :

## ∂ Démonstrations

### Ex M16.7 — (Aᵏ)ᵢⱼ compte les chemins de longueur k de i à j, par récurrence

1. 
2. 
3. 
4. 
5. 

### Ex M16.8 — Un graphe est sans cycle si et seulement si sa matrice d'adjacence est nilpotente

1. 
2. 
3. 
4. 
5. 

### Ex M16.9 — La variance d'un produit de deux variables indépendantes

1. 
2. 
3. 
4. 
5. 

## 🔗 🗣️ Pont et explication

### Ex M16.10 — Pont : n points rangés en lignes, X W + 1bᵀ, et la diffusion de b

- a :
- b :
- c :
- d :
- e :
- f :
- pourquoi 1bᵀ est 4 × 3, et ce que fait NumPy à sa place ; un cinquième point ; ce que montre e) :

### Ex M16.11 — Expliquer, sur un exemple, pourquoi la variance d'un produit n'est pas le produit des variances

*Ta réponse à ton ami, en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M16.E1 — « Pourquoi l'écart-type d'une somme de n termes indépendants grandit-il comme √n ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M16.12 — La matrice homogène d'une application affine · `homogeneous_matrix`

- l'image de (2, −1) à la main ; la forme de H et sa dernière colonne ; les entrées que ta fonction refuse :

### Ex M16.13 — Sommer sur les chemins d'un graphe sans cycle par les puissances de sa matrice · `sum_over_paths`

- ton test de cycle ; pourquoi s'arrêter à Aⁿ⁻¹ ; les 70 chemins de la grille par un raisonnement de dénombrement :

### Ex M16.14 — Espérance et variance d'un produit de variables indépendantes · `variance_of_product`

- les trois termes de la variance de la surface, et celui qu'on peut négliger :

### Ex M16.15 — Prédire l'écart-type d'une somme de produits aléatoires, mesures corrélées ou non, puis simuler

- tes quatre prédictions avant la simulation, et celles qui t'ont surpris ; ce que prédit le lemme du §6 pour c) et d) :

### Ex M16.16 — Une variance multipliée d'étage en étage : simuler une chaîne d'amplificateurs bruités

- la limite pour g < 1 ; v₄₀ pour g = 1 et g = 1,1 ; le premier étage à moins de 1 % de la limite ; l'écart entre simulation et récurrence :

### Ex M16.17 — L'image d'une figure par une suite d'applications affines du plan, en coordonnées homogènes

- l'ordre des produits de matrices ; ce que fait chaque étape à la flèche :

### Ex M16.18 — Chasse à l'erreur : une matrice homogène écrite pour des colonnes et appliquée à des lignes, Var(XY) = Var X · Var Y, et (I − A)⁻¹ sur un graphe qui a un cycle

- après la vérification : ce que calcule chaque fonction de la collègue, et sa correction ; les b pour lesquels apply_affine a raison, les moyennes pour lesquelles product_variance a raison, le nombre trouvé en c) :

### Ex M16.19 — Un test de propriété : la matrice homogène d'une composée est le produit des matrices homogènes

- la propriété testée ; ce qui attrape chaque fausse implémentation ; pourquoi comparer des images de points :

### Ex M16.20 — Défi : la loi du produit de deux uniformes indépendantes, sa densité et ses deux premiers moments

- E[UV] et V(UV) par le §5 ; la fonction de répartition z − z ln z et la densité −ln z ; ta médiane et ta méthode :
