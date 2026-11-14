# M26 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m26_markov_bellman/06_mes_reponses.md` (créée par `python tools/start_chapter.py M26`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une loi a des coordonnées positives de somme 1 et avance par $\boldsymbol{\mu}\mathbf{P}$ (une ligne à gauche), une fonction des états est moyennée par $\mathbf{P}\mathbf{f}$ (une colonne à droite) ; une loi stationnaire vérifie $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$, y compris l'équation que tu as retirée ; une probabilité d'absorption est entre 0 et 1 et une durée moyenne au moins 1 ; une valeur vérifie $\mathbf{V} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$ ligne par ligne ; $Q^\pi(s, \pi(s)) = V^\pi(s)$ ; une erreur d'itération respecte les bornes $\gamma^k\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty$ et $\frac{\gamma}{1 - \gamma}\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty$ ; une valeur de continuation tombe dans l'intervalle supposé ; le meilleur de plusieurs scores mesurés est trop beau en moyenne. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice comme `$\mathbf{P}$` et une norme comme `$\lVert\mathbf{x}\rVert_\infty$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M26.Q1 — Matrice stochastique, convention ligne, loi à n pas et chemins du graphe : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M26.Q2 — Une loi stationnaire existe-t-elle, est-elle unique, la loi de la chaîne y converge-t-elle ? Chaînes périodiques et à deux classes

1. 
2. 
3. 
4. 
5. 
6. 

### M26.Q3 — Espérance conditionnelle, propriété de la tour et analyse au premier pas : quelle équation pour quel nombre ?

1. 
2. 
3. 
4. 
5. 
6. 

### M26.Q4 — Le facteur γ : une actualisation, ou une probabilité de continuer ? Valeur d'un état et politique

1. 
2. 
3. 
4. 
5. 
6. 

### M26.Q5 — Le système de Bellman d'une politique fixée : quelles matrices, pourquoi il est inversible, quand γ = 1 est permis

1. 
2. 
3. 
4. 
5. 
6. 

### M26.Q6 — Contraction, bornes a priori et a posteriori, itérations synchrones ou en place : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M26.Q7 — Un maximum dans l'opérateur : ce qui reste (contraction, point fixe unique), ce qui se perd (le système linéaire)

1. 
2. 
3. 
4. 
5. 
6. 

### M26.Q8 — Des échantillons au lieu de P : moyenne de retours, pas 1/n ou constant, erreur TD, biais du maximum

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M26.R1 — Puissances d'une matrice diagonalisable et méthode de la puissance (M12c)

1. 
2. 
3. 
4. 

### M26.R2 — La norme ‖·‖∞ d'une matrice, ρ(A) ≤ ‖A‖ et Aᵗ → 0 quand ρ(A) < 1 (M22), et la somme d'une série géométrique (R5)

1. 
2. 
3. 
4. 
5. 
6. 

### M26.R3 — Probabilités totales et espérance d'une loi géométrique (M03, M02b)

1. 
2. 
3. 
4. 

## ✏️ Papier-crayon

### Ex M26.1 — Des vélos en libre-service entre trois stations : matrice de transition, graphe, loi après deux et trois jours, et coût moyen du lendemain (Pf)

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M26.2 — Trois opérateurs et leurs parts de marché : la loi stationnaire par un système linéaire, puis vérifier πP = π

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M26.3 — Trois chaînes qui posent problème, périodique, à deux classes et avec un état transitoire : lois stationnaires et comportement de Pⁿ

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M26.4 — Un cursus en trois années, avec redoublement et abandon : la probabilité d'être diplômé et la durée moyenne des études, par l'analyse au premier pas

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M26.5 — Un abonné qui peut résilier chaque mois : durée géométrique, revenu total moyen, et le même nombre comme revenu actualisé

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M26.6 — Une machine qui s'use, deux politiques d'entretien : P_π et r_π, deux systèmes de Bellman 3 × 3, et la valeur d'une action

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M26.7 — Les itérés de Bellman de la machine de M26.6 : trois pas synchrones puis en place, comparés à la solution, et le nombre d'itérations qui garantit 10⁻³

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M26.8 — Vendre une voiture d'occasion : offres au hasard, coût d'attente, valeur de continuation et règle à seuil

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M26.9 — Le meilleur de deux fournisseurs sur des mesures bruitées : le maximum surestime, l'estimateur double non

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

## ∂ Démonstrations

### Ex M26.10 — L'analyse au premier pas démontrée : t = 1 + Qt et h = Qh + b, et I − Q inversible dès que la fin est possible depuis chaque état

1. 
2. 
3. 
4. 

### Ex M26.11 — V = Σ γᵗPᵗr est l'unique solution du système de Bellman : I − γP inversible, série de Neumann démontrée pour γP, et (1 − γ)(I − γP)⁻¹ stochastique

1. 
2. 
3. 
4. 

### Ex M26.12 — L'opérateur de Bellman d'une politique fixée est une γ-contraction pour ‖·‖∞ ; bornes a priori et a posteriori ; le maximum est 1-lipschitzien

1. 
2. 
3. 
4. 
5. 

### Ex M26.13 — L'erreur TD se télescope : Σ γᵏ δ_{t+k} = G_t − V(S_t) ; une récompense ajoutée γΦ(s′) − Φ(s) décale chaque valeur de −Φ(s)

1. 
2. 
3. 

## 🗣️ 🔗 Explication et pont

### Ex M26.14 — Pont : d'une politique stochastique à la chaîne qu'elle induit, P_π = Σ_a π(a | s) P_a et r_π avec des tableaux à trois axes (actions, états, états), puis Q^π(s, a) et r(s, a, s′)

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M26.15 — Expliquer avec une image hors informatique pourquoi une chaîne qui mélange oublie son état de départ

*Ta réponse en 6 à 10 phrases, sans formule, avec une image hors informatique, puis en 3 phrases.*

> 

## 💼 Entretien

### M26.E1 — « Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que se passe-t-il pour γ = 1 ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M26.16 — La loi d'une chaîne après n pas, en convention ligne · n_step_distribution

> 

### Ex M26.17 — La loi stationnaire par un système linéaire, et le refus d'une chaîne qui en a plusieurs · stationary_distribution

> 

### Ex M26.18 — Le système de Bellman d'une politique fixée, avec une fin possible (matrice sous-stochastique) et γ = 1 quand la fin est sûre · bellman_linear_solve

> 

### Ex M26.19 — Les itérés de l'opérateur de Bellman d'une politique fixée (Richardson de pas 1) · bellman_fixed_point_iterates

> 

### Ex M26.20 — La loi stationnaire de trois façons, np.linalg.eig sur Pᵀ, scipy.linalg.null_space et la méthode de la puissance, sur le surfeur aléatoire d'un web de six pages

> 

### Ex M26.21 — Prédire la somme des lignes de (1 − γ)(I − γP)⁻¹, puis leur limite quand γ tend vers 1, et vérifier

> 

### Ex M26.22 — Le biais du maximum par simulation : k fournisseurs de même qualité, n mesures chacun, le meilleur mesuré contre l'estimateur double

> 

### Ex M26.23 — La loi d'une chaîne au fil des pas depuis trois départs, et ‖μ_n − π‖₁ en échelle logarithmique contre |λ₂|ⁿ

> 

### Ex M26.24 — Chasse à l'erreur : une matrice lue dans la mauvaise convention, une loi stationnaire non normalisée, un état final qui rapporte encore, γ = 1 sans fin

> 

### Ex M26.25 — Un test de propriété : πP = π, et pour bellman_fixed_point_iterates, V_k − V tenu par γᵏ‖V₀ − V‖∞ et V = r + γPV pour la limite, sur des chaînes tirées au hasard

> 

### Ex M26.26 — Défi : estimer la valeur d'un état à 0,01 près en simulant l'arrêt géométrique (continuer avec la probabilité γ) et en sommant les récompenses sans actualisation, sous un budget de pas simulés

>
