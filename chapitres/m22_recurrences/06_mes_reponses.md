# M22 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m22_recurrences/06_mes_reponses.md` (créée par `python tools/start_chapter.py M22`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : un état se recalcule pas à pas et par la formule $\mathbf{A}^t\mathbf{x}_0 + \sum_k\mathbf{A}^{t-1-k}\mathbf{B}\mathbf{u}_k$, une sortie par la convolution $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$, des valeurs propres par la trace et le déterminant, un module par $\sqrt{\det}$ pour une matrice $2 \times 2$, une norme induite par un vecteur qui l'atteint, $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert$ toujours, un produit de jacobiennes par son ordre (le dernier pas à gauche) et par son déterminant, une norme globale par Pythagore. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, une norme comme `$\lVert\mathbf{A}\rVert_2$` et un rayon spectral comme `$\rho(\mathbf{A})$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M22.Q1 — La solution d'une récurrence avec entrée : quelles puissances, quels termes ?

1. 
2. 
3. 
4. 
5. 
6. 

### M22.Q2 — Valeurs propres complexes, module, forme exponentielle et rotation : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M22.Q3 — Le rayon spectral décide-t-il de tout ? Le long terme et les premiers pas

1. 
2. 
3. 
4. 
5. 
6. 

### M22.Q4 — Normes induites : laquelle se calcule à la main, laquelle borne quoi ?

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M22.Q5 — Un produit de facteurs dans [0, 1] : ce qui reste après n étapes

1. 
2. 
3. 
4. 
5. 
6. 

### M22.Q6 — Contraction et point fixe : lire une jacobienne

1. 
2. 
3. 
4. 
5. 
6. 

### M22.Q7 — Une somme sur le temps, sur un modèle de pêche chiffré : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M22.Q8 — Ramener un vecteur sous un seuil : le tout ou chaque bloc ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M22.R1 — La diagonalisation et les puissances d'une matrice (M12c)

1. 
2. 
3. 
4. 
5. 

### M22.R2 — Valeurs singulières et norme spectrale (M12d)

1. 
2. 
3. 
4. 
5. 
6. 

### M22.R3 — La règle de la chaîne comme produit de jacobiennes (M17)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M22.1 — Une population à trois classes d'âge, avec des arrivées : trois pas à la main, et la solution écrite avec les puissances

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M22.2 — La réponse impulsionnelle de deux réservoirs en cascade, et la sortie comme convolution de l'entrée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M22.3 — Une matrice de rotation et d'homothétie : valeurs propres complexes, forme exponentielle, puissances

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- dans ta copie :

### Ex M22.4 — Le rayon spectral de trois matrices 2 × 2 non symétriques, et le comportement de leurs puissances

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M22.5 — Une matrice triangulaire de rayon spectral < 1 dont les puissances grandissent d'abord : Aᵗ en formule

- la formule de $\mathbf{T}^t$, par récurrence, et ses deux cas :
- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M22.6 — Les normes ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice 2 × 2, et trois majorations de ‖A⁵x‖

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- dans ta copie :

### Ex M22.7 — Trois équipements qui s'usent à des rythmes différents : une récurrence diagonale, ce qui reste, et la demi-vie

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M22.8 — Les jacobiennes d'une application du plan en trois points d'une trajectoire, et leur produit

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M22.9 — Un capital placé à taux fixe avec des versements : la dérivée du capital final par rapport au taux, une somme sur les années

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M22.10 — La norme globale de trois blocs, et deux façons de les ramener sous un seuil

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

## ∂ Démonstrations

### Ex M22.11 — Sous-multiplicativité, ‖Aᵀ‖₂ = ‖A‖₂, ‖diag(d)‖₂ = max |dᵢ| et ρ(A) ≤ ‖A‖

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M22.12 — La norme induite ‖·‖∞ est le maximum des sommes de lignes

1. 
2. 
3. 
4. 
5. 

### Ex M22.13 — Aᵗ → 0 si et seulement si ρ(A) < 1, pour une matrice diagonalisable sur ℂ

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M22.14 — Une application contractante oublie son point de départ : l'écart entre deux trajectoires décroît géométriquement

1. 
2. 
3. 
4. 
5. 

### Ex M22.15 — La sensibilité de l'état final à un paramètre utilisé à chaque pas suit une récurrence avec entrée : sa solution est une somme sur le temps

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M22.16 — Pont : la convention ligne x_{t+1} = x_t A + u_t B, ses formes, et la jacobienne Aᵀ

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M22.17 — MML §4.2 relu : les cinq applications du plan de la figure 4.4, leurs valeurs propres, et le comportement de leurs puissances

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

### Ex M22.18 — Expliquer avec une image non mathématique pourquoi un système linéaire oublie son passé au rythme de ρ(A)

*Ta réponse en 6 à 10 phrases, sans formule, avec une image de la vie courante, puis en 3 phrases.*

> 

## 💼 Entretien

### M22.E1 — « Quelle différence entre le rayon spectral et la norme d'une matrice ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M22.E2 — « Pourquoi Aⁿ peut-il grandir longtemps alors que toutes les valeurs propres de A sont de module < 1 ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M22.19 — Les états d'une récurrence linéaire avec entrée · linear_system_states

- ta boucle et tes contrôles de formes ; les tests qui ont échoué d'abord, et pourquoi ; l'équilibre de la population et le rythme auquel elle l'atteint :

### Ex M22.20 — Les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂ · operator_norm

- tes trois calculs et tes refus ; ce que montrent la formule de Gelfand et la norme de Frobenius de l'identité :

### Ex M22.21 — Les normes des produits cumulés, et leur majoration · product_norms

- l'ordre du produit ; l'écart entre la norme et sa majoration sur la trajectoire de Hénon, et le cas des matrices diagonales :

### Ex M22.22 — np.linalg.eigvals et np.linalg.norm : rayon spectral et normes de matrices tirées au hasard, et ρ ≤ ‖A‖

- les proportions et les moyennes obtenues ; le piège de np.linalg.norm sans ord :

### Ex M22.23 — Prédire l'allure de ‖Aᵗ‖₂ pour une matrice non normale de rayon spectral 0,8, puis tracer

- tes prédictions avant l'expérience ; celles qui étaient fausses, et pourquoi :

### Ex M22.24 — Des produits de matrices aléatoires : le taux de croissance (1/n) ln ‖Aₙ ⋯ A₁‖

- les taux mesurés, leur comparaison avec ln ρ(E[A]) et avec la majoration par les normes, et ta conclusion :

### Ex M22.25 — Les spirales d'une récurrence 2 × 2 à valeurs propres complexes, selon leur module

- ce que montre chaque panneau, et le nombre de pas par tour :

### Ex M22.26 — Chasse à l'erreur : ρ(A) pris pour ‖A‖, un produit de jacobiennes dans le mauvais ordre, un seuil appliqué bloc par bloc

- pour chaque erreur : ce qu'elle faisait, pourquoi la vérification fournie ne la voyait pas, et ta correction :

### Ex M22.27 — Un test de propriété : ‖AB‖ ≤ ‖A‖ ‖B‖ et ρ(A) ≤ ‖A‖ sur des matrices tirées au hasard

- ton test, pourquoi les versions fausses le passaient d'abord, et les propriétés qui les ont attrapées :

### Ex M22.28 — Défi : une matrice 3 × 3 à coefficients dans [−3, 3], de rayon spectral 0,85, dont une puissance a une norme ‖·‖₂ supérieure à 100

- ta matrice, comment tu l'as trouvée, le premier pas au-delà de 100 et le maximum :
