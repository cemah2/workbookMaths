# M13b · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m13b_lagrange_svm/06_mes_reponses.md` (créée par `python tools/start_chapter.py M13b`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie le signe de chaque résultat : un multiplicateur de contrainte d'inégalité est positif ou nul, une valeur de la fonction duale ne dépasse jamais le minimum du primal, une hinge est positive ou nulle, un noyau RBF est entre 0 et 1. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une fraction avec `\frac{a}{b}`, une norme avec `\lVert \mathbf{w} \rVert` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M13b.Q1 — Lagrange : ce que dit ∇f = λ ∇g

1. 
2. 
3. 
4. 
5. 
6. 

### M13b.Q2 — Contrainte active ou inactive ?

1. 
2. 
3. 
4. 
5. 
6. 

### M13b.Q3 — Primal, dual, dualité faible

1. 
2. 
3. 
4. 
5. 
6. 

### M13b.Q4 — Problème convexe ou pas ?

1. 
2. 
3. 
4. 
5. 
6. 

### M13b.Q5 — Ce que maximise une SVM, ce que minimise son problème

1. 
2. 
3. 
4. 
5. 
6. 

### M13b.Q6 — La hinge loss : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M13b.Q7 — Noyau valide ou pas ?

1. 
2. 
3. 
4. 
5. 
6. 

### M13b.Q8 — Primal ou dual : lequel résoudre, et quand ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M13b.R1 — La marge géométrique et l'astuce du biais (M10)

1. 
2. 
3. 
4. 
5. 

### M13b.R2 — Gradient et lignes de niveau (M05b)

1. 
2. 
3. 
4. 
5. 

### M13b.R3 — Matrices définies positives (M12c)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M13b.1 — Lagrange à la main : un produit maximal sous une contrainte linéaire

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- les quatre équations et x = 2y = 4z ; la formule de P*(c) ; pourquoi Lagrange seul ne prouve pas le maximum, et ce qu'apporte g) :

### Ex M13b.2 — La distance d'un point à un plan, retrouvée par Lagrange

- a :
- b :
- c :
- d :
- e :
- f :
- la stationnarité ; x − x₀ colinéaire à n ; la formule générale de la distance ; la méthode qui se généralise à une surface :

### Ex M13b.3 — Un problème quadratique sous deux contraintes linéaires : le système de Lagrange

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- le système par blocs en entier ; pourquoi h) < g) < d) ; Q définie positive et ce que cela garantit :

### Ex M13b.4 — Relire l'ACP par Lagrange : maximiser uᵀCu sous ‖u‖ = 1

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- le lagrangien et sa stationnarité ; la valeur de l'objectif en un point critique ; ν = 0 ; la plus petite valeur propre :

### Ex M13b.5 — Une contrainte d'inégalité : active ou non, les conditions KKT à la main

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- les quatre conditions KKT pour c = 3 ; μ pour c = 8 ; le signe de g) et la vraie solution sous la contrainte inverse :

### Ex M13b.6 — La fonction duale d'un petit problème quadratique, et la dualité faible

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- le lagrangien minimisé à μ fixé ; pourquoi b) et g) sont sous f) ; les conditions KKT ; le saut de dualité :

### Ex M13b.7 — Reconnaître un problème convexe : fonctions, contraintes, ensembles

- a :
- pour chaque problème non convexe, la partie qui viole la définition ; (E) résolu par Lagrange :

### Ex M13b.8 — Une SVM à marge dure sur trois points, résolue par les conditions KKT

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- pourquoi w est orthogonal à x₂ − x₁ ; le système et sa résolution ; les quatre conditions KKT ; le quatrième exemple :

### Ex M13b.9 — La hinge loss et l'objectif régularisé de quelques points

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- les trois groupes d'exemples ; ce que vérifie J = nC × (la forme de f)) :

### Ex M13b.10 — Un pas de sous-gradient sur l'objectif d'une SVM linéaire

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- pourquoi g) est aussi un sous-gradient ; J a-t-il baissé, et est-ce garanti pour un pas plus grand :

### Ex M13b.11 — Le dual d'une SVM : lire les vecteurs de support et retrouver w

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- vecteurs libres et bornés ; b sur les deux vecteurs libres ; la cohérence avec les trois groupes ; ce que dit l'égalité de f) et g) :

### Ex M13b.12 — Le noyau (1 + x · z)² en dimension 2 : sa fonction φ à six coordonnées

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- le développement et φ ; l'origine des √2 ; f) et g) par count_monomials ; le nombre d'opérations :

### Ex M13b.13 — La matrice de Gram d'un noyau RBF sur trois points, et l'effet de γ

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- ce que dit d) de K ; pourquoi les distances sont sous √2 ; ce qu'une SVM apprend avec les matrices de g) et de h) :

## ∂ Démonstrations

### Ex M13b.14 — Au point optimal sous une contrainte d'égalité, ∇f est colinéaire à ∇g

1. 
2. 
3. 
4. 
5. 

### Ex M13b.15 — La dualité faible : la fonction duale minore le minimum du primal

1. 
2. 
3. 
4. 
5. 

### Ex M13b.16 — Pour un problème convexe, un minimum local est global

1. 
2. 
3. 
4. 
5. 

### Ex M13b.17 — Maximiser la marge revient à minimiser ½ ‖w‖²

1. 
2. 
3. 
4. 
5. 

### Ex M13b.18 — Marge souple : la formulation avec des variables d'écart et celle avec la hinge loss sont équivalentes

1. 
2. 
3. 
4. 
5. 

### Ex M13b.19 — La somme et le produit de deux noyaux sont des noyaux ; une matrice de Gram est semi-définie positive

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13b.20 — Pont : la décision d'une SVM à noyau, une somme pondérée sur les vecteurs de support

- a :
- b :
- c :
- d :
- e :
- f :
- pourquoi a) est nécessaire ; la prédiction loin des vecteurs de support ; ce qui décide du coût d'une prédiction :

### Ex M13b.21 — MML §7.2 et §7.3 : Lagrange, dualité et optimisation convexe, en anglais

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M13b.22 — MML §12.2 à §12.5 : marge, primal, dual et noyaux (§12.1 a été lu en M10)

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M13b.23 — Fermi : la taille de la matrice de Gram d'une SVM à noyau sur 100 000 exemples

1. 
2. 
3. 
4. 
5. 

### Ex M13b.24 — Expliquer un multiplicateur de Lagrange comme un prix

*Ta réponse à ton ami, en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M13b.E1 — « Qu'est-ce qu'un problème d'optimisation convexe, et pourquoi est-ce une bonne nouvelle ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M13b.E2 — « Hinge loss ou log-loss : quelles différences ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*
