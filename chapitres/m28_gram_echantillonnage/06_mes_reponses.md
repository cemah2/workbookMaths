# M28 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m28_gram_echantillonnage/06_mes_reponses.md` (créée par `python tools/start_chapter.py M28`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une matrice de Gram est symétrique, de diagonale positive (les carrés des normes), semi-définie positive, et $\mathbf{X}\mathbf{X}^\top$ a la forme $(n, n)$ ; une matrice des moments se divise par le nombre d'**échantillons** ; le double centrage porte sur les **carrés** des distances, et chaque ligne de $-\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ a une somme nulle ; une carte se vérifie par ses distances, jamais par ses coordonnées ; une montée projetée reste dans le pavé, et l'on coupe le point, pas le gradient ; $\mathrm{VT} = \mathbf{x}^\top\mathbf{L}\mathbf{x} \ge 0$, et un pas de descente garde la moyenne ; $4\sin^2\frac\omega2$ attend $\omega = 2\pi f$ en radians par case, et ce rapport ne dépasse pas 4 par direction ; une loi tempérée a la même somme, 1, et le même ordre que la loi de départ ; une loi tronquée est nulle hors de l'ensemble gardé, et $\mathrm{KL}(\mathbf{p}_S \,\|\, \mathbf{p}) = -\ln P(S)$, en nats ; une période ne compte pas la queue, et $\mu + \lambda \le N$. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice comme `$\mathbf{G}$` et une norme comme `$\lVert\mathbf{x}\rVert$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M28.Q1 — Matrice de Gram : XXᵀ ou XᵀX, laquelle former, sa diagonale, et les distances qu'on y lit

1. 
2. 
3. 
4. 
5. 

### M28.Q2 — Monter sur l'entrée : pas normalisé, projection sur un pavé, coordonnées gelées, point d'arrivée

1. 
2. 
3. 
4. 
5. 

### M28.Q3 — Variation totale et fréquences spatiales : quel motif coûte le plus, lequel traverse un flou ?

1. 
2. 
3. 
4. 
5. 

### M28.Q4 — Température, top-k et top-p : ce qui change l'ensemble gardé, ce qui ne change que les probabilités

1. 
2. 
3. 
4. 
5. 

### M28.Q5 — Une itération sur un ensemble fini : prépériode, période, et ce qui empêche de boucler

1. 
2. 
3. 
4. 
5. 

## 🔁 Rappels

### M28.R1 — Le quotient de Rayleigh et la méthode de la puissance (M12c)

1. 
2. 
3. 
4. 
5. 

### M28.R2 — Le laplacien discret et la moyenne mobile d'un signal (M21)

1. 
2. 
3. 
4. 

### M28.R3 — La loi de Boltzmann et ses limites en température (M17)

1. 
2. 
3. 
4. 

## ✏️ Papier-crayon

### Ex M28.1 — Quatre points du plan : leur matrice de Gram 4 × 4, leur matrice des moments d'ordre 2, et les distances lues dans la Gram

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M28.2 — Quatre villes aux sommets d'un losange : le double centrage des carrés des distances, puis une carte à une isométrie près

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M28.3 — Régler quatre émetteurs entre 0 et 1 : le maximum d'une réponse linéaire sur la boule et sur le pavé, d'une énergie quadratique sur la sphère, et deux pas de montée projetée

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M28.4 — Les températures le long d'une barre : la variation totale xᵀLx, son gradient 2Lx, un pas de lissage, et une marche étalée sur n pas, au carré ou en valeur absolue

- a :
- b :
- c :
- e :
- f :
- g :
- dans ta copie :

### Ex M28.5 — Des étoffes rayées : période, fréquence, fréquence de Nyquist, repliement, variation totale rapportée à l'énergie 4 sin²(ω/2), et gain d'une moyenne mobile

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M28.6 — La prévision d'un météorologue en six catégories : la refroidir, garder les trois plus probables, garder le plus petit ensemble de masse donnée, et le coût de chaque troncature

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M28.7 — Les décimales de a/n et l'itération x ↦ x² + c modulo n : prépériode et période à la main, et la borne du principe des tiroirs

- a :
- b :
- c :
- dans ta copie :

## ∂ Démonstrations

### Ex M28.8 — Deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie

1. 
2. 
3. 
4. 
5. 

### Ex M28.9 — Le maximum d'une fonction convexe sur un pavé est atteint en un sommet

1. 
2. 
3. 
4. 

### Ex M28.10 — Les issues les plus probables, prises jusqu'à atteindre la masse p, forment un plus petit ensemble de masse au moins p, et la loi tronquée est à −ln P(S) de la loi de départ en divergence KL

1. 
2. 
3. 
4. 
5. 

## 🔗 🗣️ Pont et explication

### Ex M28.11 — Pont : diviser des scores par T avant la softmax, ou élever les probabilités à la puissance 1/T, la même loi ; et le même top-k

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M28.12 — Expliquer avec une structure de barres rigides ce que la matrice de Gram d'une famille de vecteurs fixe, et ce qu'elle laisse libre

*Ta réponse en 6 à 10 phrases, sans formule, avec la structure de barres rigides, puis en 3 phrases.*

> 

## 💼 Entretien

### M28.E1 — « Que perd-on, en divergence KL, à ne garder que les issues les plus probables d'une loi avant de tirer ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M28.13 — Une configuration de points de matrice de Gram donnée, par le théorème spectral · points_from_gram

> 

### Ex M28.14 — Tempérer une loi donnée par ses probabilités, et le plus petit ensemble de masse donnée · temper, smallest_mass_set

> 

### Ex M28.15 — Prédire ce que deviennent un pas η∇f et un pas normalisé quand la fonction est multipliée par 1 000, puis vérifier

> 

### Ex M28.16 — Des motifs rayés de fréquence croissante jusqu'au damier : leur variation totale, et ce qu'en laissent un flou 3 × 3 et dix pas de descente sur la variation totale

> 

### Ex M28.17 — Chasse à l'erreur : un double centrage fait sur les distances au lieu de leurs carrés, une montée qui coupe le gradient au lieu du point, une prépériode comptée dans la période

> 

### Ex M28.18 — Un test de propriété : la configuration rendue redonne la matrice de Gram et les distances, pour des points tirés au hasard

> 

### Ex M28.19 — Défi : redessiner la carte de 30 villes quand un quart des distances manquent, à moins de 1 km en moyenne après alignement

>
