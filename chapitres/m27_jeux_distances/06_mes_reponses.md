# M27 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m27_jeux_distances/06_mes_reponses.md` (créée par `python tools/start_chapter.py M27`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : le maximin ne dépasse jamais le minimax, et un point selle est le plus petit de sa ligne et le plus grand de sa colonne ; la valeur d'un jeu est entre le maximin et le minimax, et $p^\star$ rend l'**adversaire** indifférent ; une probabilité a posteriori est entre 0 et 1 et tient compte des priors ; JS est en nats, entre 0 et $\ln 2$ ; un plan de transport respecte ses deux marges ; $W_1 \le W_2$, et $\lvert\mathbb{E}X - \mathbb{E}Y\rvert \le W_1$ ; $W_2$ de deux gaussiennes prend des écarts-types, et la distance de Fréchet est $W_2$, pas son carré ; une distance estimée est biaisée vers le haut ; KS est sans unité, $W_1$ dans l'unité de la variable. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice comme `$\mathbf{G}$` et une norme comme `$\lVert\mathbf{x}\rVert$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M27.Q1 — Maximin, minimax et point selle : qui annonce son coup en premier, et qui y gagne ?

1. 
2. 
3. 
4. 
5. 

### M27.Q2 — Stratégies mixtes, gain espéré et valeur d'un jeu : vrai ou faux

1. 
2. 
3. 
4. 
5. 

### M27.Q3 — Équilibres de Nash, arbres de jeu et descente-montée : unique ou non, le meilleur pour tous ou non, converger ou tourner ?

1. 
2. 
3. 
4. 
5. 

### M27.Q4 — La probabilité a posteriori et la log-loss ; Jensen-Shannon et KL quand les supports se séparent

1. 
2. 
3. 
4. 
5. 

### M27.Q5 — Couplages et distances de Wasserstein : marges, translation, dilatation, et W₁ ≤ W₂

1. 
2. 
3. 
4. 
5. 

### M27.Q6 — La distance de Fréchet et son estimation : rotation commune, covariances, taille des échantillons

1. 
2. 
3. 
4. 
5. 

### M27.Q7 — Mesurer une dérive : PSI, KS ou W₁, leurs unités, et ce que chacun ne voit pas

1. 
2. 
3. 
4. 
5. 

## 🔁 Rappels

### M27.R1 — Le maximum de vraisemblance d'une loi de Bernoulli (des comptes entiers), et la log-loss quand la probabilité prédite tend vers 0 (M04, M13a)

1. 
2. 
3. 
4. 

### M27.R2 — Les valeurs propres complexes d'une matrice réelle 2 × 2, leur module et les puissances (M22)

1. 
2. 
3. 
4. 

### M27.R3 — La racine carrée d'une matrice symétrique positive, et la trace comme somme des valeurs propres (M12c)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M27.1 — Deux enseignes se partagent un marché : réduire une matrice 3 × 4 par dominance, trouver ses deux points selles et vérifier qu'ils ont la même valeur, et ce que la réduction ne change pas (maximin, minimax)

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex M27.2 — Tirs au but : la probabilité de tirer à gauche par indifférence, la réponse du gardien et la valeur du jeu

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M27.3 — Les équilibres de Nash d'un dilemme du prisonnier et d'un jeu de coordination (purs et mixte), puis la valeur d'un jeu d'allumettes par induction arrière

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M27.4 — Descente-montée sur f(x, y) = xy : la matrice d'un pas simultané puis alterné, leurs valeurs propres et leurs modules, et deux pas différents pour x et y

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M27.5 — Deux fournisseurs et un défaut noté sur quatre niveaux : la probabilité a posteriori, et la log-loss moyenne de trois prédicteurs (a priori, a posteriori, trop sûr de lui)

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M27.6 — Deux lois uniformes de même largeur, translatées : JS en fonction du décalage, la KL, et ce que le décalage lui-même mesure

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M27.7 — Trois dépôts et trois magasins le long d'une route : vérifier des couplages, leur coût, le couplage indépendant et le plan monotone (coin nord-ouest)

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M27.8 — W₁ et W₂ par l'aire entre les fonctions de répartition et par les quantiles : deux lois uniformes, puis W₂ de deux gaussiennes (et W₁ quand elles ont le même écart-type)

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex M27.9 — La distance de Fréchet de deux gaussiennes du plan à covariances diagonales, puis tournées ensemble : la part des moyennes et celle des covariances

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M27.10 — Une dérive en deux mois d'une variable à trois catégories : la divergence de Jeffreys (le PSI) et JS, puis l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage ; enfin KS et W₁ entre deux petits échantillons de températures de même taille

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

## ∂ Démonstrations

### Ex M27.11 — Le maximin est au plus le minimax ; ils sont égaux si et seulement si le jeu a un point selle, et deux points selles ont la même valeur

1. 
2. 
3. 
4. 

### Ex M27.12 — La log-loss espérée est minimale pour la probabilité a posteriori : une preuve par l'inégalité de Gibbs

1. 
2. 
3. 
4. 

### Ex M27.13 — 0 ≤ JS ≤ ln 2, et JS = ln 2 si et seulement si les deux lois ont des supports disjoints

1. 
2. 
3. 
4. 

### Ex M27.14 — L'appariement trié est optimal : un argument d'échange sur deux paires, puis sur n paires, pour les coûts |x − y| et (x − y)²

1. 
2. 
3. 
4. 

### Ex M27.15 — E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ : une distance estimée sur deux échantillons est biaisée vers le haut

1. 
2. 
3. 
4. 

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M27.16 — Pont : la distance de Fréchet en dimension 1, W₂² = (Δμ)² + (Δσ)², entre deux lois résumées par leur moyenne et leur écart-type (deux séries d'une machine, avant et après réglage) : la part de la moyenne et celle de l'écart-type, et pourquoi workbookIA 27 l'écrit avec des covariances et en rend le carré

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M27.17 — MML §7.2 relu : l'inégalité minimax (7.23) et sa preuve, la dualité faible (7.27) lue comme un jeu, et l'inégalité vérifiée sur une matrice de gains choisie

1. 
2. 
3. 
4. 
5. 

### Ex M27.18 — Expliquer avec une partie de cache-cache pourquoi jouer au hasard peut être la meilleure stratégie, et ce que le hasard garantit

*Ta réponse en 6 à 10 phrases, sans formule, avec la partie de cache-cache, puis en 3 phrases.*

> 

## 💼 Entretien

### M27.E1 — « Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se recouvrent pas, et pas Jensen-Shannon ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M27.E2 — « Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et comment comparer deux mesures ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M27.19 — Les valeurs d'un jeu en stratégies pures : maximin, minimax et coups prudents, points selles compris · pure_strategy_values

> 

### Ex M27.20 — Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle · mixed_strategy_value_2x2

> 

### Ex M27.21 — Les itérés de la descente-montée simultanée ou alternée sur un jeu bilinéaire xᵀAy · descent_ascent_iterates

> 

### Ex M27.22 — W₂ de deux gaussiennes en dimension 1, à partir des moyennes et des écarts-types · w2_gaussians_1d

> 

### Ex M27.23 — scipy.optimize.linprog : le transport optimal entre deux lois discrètes de la droite comme programme linéaire, comparé au plan monotone et à l'aire entre les fonctions de répartition

> 

### Ex M27.24 — Prédire la trajectoire de la descente-montée simultanée puis alternée sur xy, puis la tracer : spirale qui s'éloigne ou courbe fermée ?

> 

### Ex M27.25 — Le biais d'une distance estimée : ‖x̄₁ − x̄₂‖² entre deux échantillons d'une même loi de ℝ³, selon leurs tailles, contre tr Σ₁/n₁ + tr Σ₂/n₂

> 

### Ex M27.26 — Deux fonctions de répartition sur une même figure : l'aire entre elles (W₁) et leur plus grand écart vertical (KS), pour une translation puis une dilatation

> 

### Ex M27.27 — Chasse à l'erreur : une stratégie d'indifférence calculée sur ses propres gains, W₂ de deux gaussiennes avec des variances, des échantillons appariés sans être triés

> 

### Ex M27.28 — Un test de propriété : la valeur d'un jeu 2 × 2 tiré au hasard est entre maximin et minimax, et devient v + c pour G + c et k v pour k G (k > 0)

> 

### Ex M27.29 — Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂, et cette distance, à 10⁻³ près

>
