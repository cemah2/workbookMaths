# M05b · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m05b_gradient/06_mes_reponses.md` (créée par `python tools/start_chapter.py M05b`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris les dérivées partielles avant de les évaluer, un gradient comme un vecteur $(\ldots, \ldots)$, une direction par un vecteur unitaire, et pour un point critique le tableau $f_{xx}$, $f_{yy}$, $f_{xy}$, $D$ ; garde les valeurs exactes ($\sqrt{34}$, $e^{0{,}5}$, $\frac{1}{130}$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M05b.Q1 — Lire des lignes de niveau

1. 
2. 
3. 
4. 
5. 
6. 

### M05b.Q2 — Dérivées partielles : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M05b.Q3 — Où pointe le gradient ?

1. 
2. 
3. 
4. 
5. 
6. 

### M05b.Q4 — La dérivée directionnelle

1. 
2. 
3. 
4. 
5. 
6. 

### M05b.Q5 — Le plan tangent

1. 
2. 
3. 
4. 
5. 
6. 

### M05b.Q6 — Minimum, maximum ou selle ?

1. 
2. 
3. 
4. 
5. 
6. 

### M05b.Q7 — Descendre ou monter

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M05b.R1 — Dériver une composée (R7)

1. 
2. 
3. 
4. 
5. 

### M05b.R2 — Produit scalaire et norme (R9)

1. 
2. 
3. 
4. 
5. 

### M05b.R3 — Dérivée seconde et convexité (M05a)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M05b.1 — Les lignes de niveau de trois fonctions

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les trois lignes de niveau de chaque fonction, avec leur valeur ; la direction où les lignes de f₂ sont les plus serrées, et pourquoi :

### Ex M05b.2 — Dérivées partielles

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La tranche x ↦ f(x, −2) et sa dérivée en 1 ; pourquoi les deux dérivées de g ont le même facteur exponentiel :

### Ex M05b.3 — Le gradient en un point et sa norme

- a :
- b :
- c :
- d :
- e :
- f :
- Le système ∇f = 0 et ses solutions ; la valeur de f aux points de d) :

### Ex M05b.4 — La dérivée directionnelle dans trois directions

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- d) vérifiée par ‖∇f‖ cos θ ; la direction unitaire de pente nulle, de première composante positive :

### Ex M05b.5 — Monter le plus vite : la direction et la valeur de la plus grande pente

- a :
- b :
- c :
- d :
- e :
- f :
- Le croquis (P, la flèche de b), la direction de e)) ; ce que représente la direction de e) sur la carte de T :

### Ex M05b.6 — Le plan tangent et l'approximation d'une valeur

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le plan sous la forme z = f(3, 4) + …, puis développé ; le facteur sur l'erreur pour un déplacement double, et pourquoi :

### Ex M05b.7 — Dérivées secondes croisées : le théorème de Schwarz vérifié

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- f_yx calculée en dérivant f_y par rapport à x, comparée à a) ; pourquoi les courbures f) et g) diffèrent :

### Ex M05b.8 — Les points critiques et leur nature (test du second ordre)

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le système ∇g = 0 et ses quatre solutions ; le tableau point, g_xx, g_yy, g_xy, D, nature ; la vraie nature de (0, 0) en h), et comment je la vois :

### Ex M05b.9 — Pourquoi un petit pas contre le gradient fait baisser f : le calcul au premier ordre

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La baisse réelle comparée à la prévision, la hausse de f) comparée à η‖∇f(P)‖² ; le développement au premier ordre écrit pour h = −η∇f(P) :

### Ex M05b.10 — argmin et argmax sur un segment

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- g(t) développé et son tableau de variations sur [0, 1] ; le sens géométrique de h) ; les lignes de niveau de f (leur centre) et le segment :

## ∂ Démonstrations

### Ex M05b.11 — La dérivée directionnelle vaut ∇f · u, et la plus grande pente

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M05b.12 — Le gradient est orthogonal aux lignes de niveau

1. 
2. 
3. 
4. 
5. 

### Ex M05b.13 — Le test du second ordre pour ax² + bxy + cy²

1. 
2. 
3. 
4. 
5. 
6. 
7. 

## 🔗 📖 📈 🗣️ Pont, lecture, graphique et explication

### Ex M05b.14 — La loss d'un neurone à deux poids sur deux exemples : son gradient

- a :
- b :
- c :
- d :
- e :
- f :
- ∂L/∂w₁ en général et ce que pèse chaque exemple ; la valeur de L aux poids de f), et pourquoi ; ce qui changerait avec trois exemples incompatibles :

### Ex M05b.15 — MML §5.2 : dérivées partielles et gradient, la convention en ligne (lecture guidée)

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M05b.16 — Lire une carte de lignes de niveau : estimer une dérivée partielle

- a :
- b :
- c :
- d :
- e :
- f :
- La justification de f) par l'écart entre les lignes ; ∂f/∂y et ∂f/∂x sur la carte ; ma formule pour f, vérifiée sur deux points :

### Ex M05b.17 — Expliquer ce que disent des lignes de niveau serrées

*Huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M05b.E1 — Pourquoi le gradient est-il la direction de plus grande pente ?

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M05b.18 — Une dérivée partielle par différence centrée · `partial_derivative`

- a), b) et c) calculés à la main ; pourquoi f) demande une copie en flottants :

### Ex M05b.19 — Dérivée directionnelle et direction de plus grande pente · `directional_derivative, steepest_ascent_direction`

- ∇f(1, 2) à la main, puis a), b) et c) ; ce que représente la direction de c) ; pourquoi f) n'a pas de réponse :

### Ex M05b.20 — Le plan tangent · `tangent_plane`

- Les deux plans, sous la forme z = f(x₀, y₀) + …, puis développés ; le signe de l'écart de d), et ce qu'il dit de la surface :

### Ex M05b.21 — SymPy : dérivées partielles, gradient, points critiques

- Le tableau des trois points critiques (k_xx, k_yy, k_xy, D, nature) ; a) et c) vérifiés à la main :

### Ex M05b.22 — Prédire : la dérivée directionnelle le long d'une ligne de niveau

- Mes prédictions avant l'expérience (et pourquoi) ; f(P + t u) en fonction de t ; le dessin de l'ellipse, de sa tangente et du gradient ; le cas d'une fonction affine :

### Ex M05b.23 — L'erreur du plan tangent quand on s'éloigne du point

- Ce que dit c) de l'ordre de l'erreur ; pourquoi d) est nul ; e) et a) comparés au terme s²/2 :

### Ex M05b.24 — Lignes de niveau et flèches du gradient sur la même figure

- Les maxima, minima et selles repérés, et ce que font les flèches autour ; où les flèches sont les plus longues :

### Ex M05b.25 — Chasse à l'erreur : la mauvaise variable dérivée, une direction non unitaire

- L'erreur de chaque ligne fausse et sa correction ; la ligne juste qui utilise l'approximation linéaire :

### Ex M05b.26 — Vectoriser : une fonction de deux variables sur une grille (`np.meshgrid`)

- Pourquoi des grilles de tailles différentes ; ce qui se passe avec math.sin ; le gain de temps mesuré :

### Ex M05b.27 — Défi : retrouver une fonction du second degré à partir de son gradient

- La fonction de GRAD_27, son point critique et sa nature ; pourquoi deux appels ne suffisent pas :
