# M18 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m18_retropropagation/06_mes_reponses.md` (créée par `python tools/start_chapter.py M18`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une dérivée par la somme sur les chemins se retrouve en dérivant la formule directement, le mode direct et le mode inverse donnent les mêmes nombres, un adjoint qui reçoit plusieurs contributions les additionne, un gradient par rapport à une matrice a la forme de cette matrice. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, un nombre dual comme `$a + b\varepsilon$`, un adjoint comme `$\bar{u}$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M18.Q1 — Lire un graphe de calcul : nœuds, arêtes, ordre d'évaluation

1. 
2. 
3. 
4. 
5. 
6. 

### M18.Q2 — Combien de chemins, et quelle somme ?

1. 
2. 
3. 
4. 
5. 
6. 

### M18.Q3 — Calculer avec ε² = 0

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M18.Q4 — Le mode inverse : dans quel ordre visiter les nœuds ?

1. 
2. 
3. 
4. 
5. 
6. 

### M18.Q5 — Direct ou inverse, pour n entrées et m sorties ?

1. 
2. 
3. 
4. 
5. 
6. 

### M18.Q6 — La forme d'un gradient par rapport à une matrice

1. 
2. 
3. 
4. 
5. 
6. 

### M18.Q7 — Identités de trace : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M18.Q8 — Gradient d'une moyenne, moyenne des gradients

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M18.R1 — La jacobienne d'une composée (M17)

1. 
2. 
3. 
4. 
5. 

### M18.R2 — Le gradient de wᵀAw (M09b)

1. 
2. 
3. 
4. 
5. 

### M18.R3 — Différences centrées et choix du pas (M05a)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M18.1 — Le graphe de calcul d'une formule de physique, et l'ordre de ses calculs

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M18.2 — Dériver par la somme sur les chemins : une variable qui sert deux fois

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M18.3 — Le mode direct à la main : des nombres duaux sur une fonction de deux variables

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M18.4 — Le mode inverse à la main : les adjoints d'un graphe de six nœuds

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M18.5 — Le même gradient par les deux modes, et le compte des opérations

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M18.6 — Le gradient de aᵀXb, de la forme de X

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M18.7 — Les gradients de tr(AX) et de tr(XᵀAX), coordonnée par coordonnée

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M18.8 — Le gradient de log det X sur une matrice 2 × 2, à la main puis par la formule

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M18.9 — Le gradient d'une moyenne de distances : le point qui minimise la somme des distances à des villes

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M18.10 — La différentielle d'une fonction de matrice, df = tr(Gᵀ dX), et le gradient G qu'on y lit

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

## ∂ Démonstrations

### Ex M18.11 — La règle de la chaîne sur un graphe sans cycle : la somme sur les chemins, nœud par nœud dans l'ordre de la numérotation

1. 
2. 
3. 
4. 
5. 

### Ex M18.12 — Les nombres duaux calculent la dérivée : f(a + bε) = f(a) + b f′(a) ε, pour les sommes, les produits et les composées

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M18.13 — Le mode inverse calcule tout le gradient en un passage : l'adjoint d'un nœud est la somme, sur ses successeurs, des adjoints fois les dérivées locales

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M18.14 — ∇ log det X = X⁻ᵀ, par le développement du déterminant selon une ligne

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M18.15 — Pont : workbookIA 18 programme le mode inverse ; pour une simulation de ℝ²⁰⁰⁰ dans ℝ³, combien de passages dans chaque mode ?

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M18.16 — Pont : de la convention de MML (gradient en ligne) à celle de NumPy et des bibliothèques de deep learning

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex M18.17 — MML §5.4 et §5.5 : gradients par rapport à des matrices et identités utiles, en anglais

1. 
2. 
3. 
4. 
5. 

### Ex M18.18 — MML §5.6 : rétropropagation et différentiation automatique, en anglais

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M18.19 — Expliquer le mode inverse à quelqu'un qui connaît la règle de la chaîne en une variable

*Ta réponse, en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M18.E1 — « Différentiation automatique, symbolique ou numérique : quelles différences ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M18.E2 — « Quand le mode direct est-il préférable au mode inverse ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M18.20 — Les nombres duaux : la classe `Dual`, et la dérivée d'une fonction d'une variable · `Dual, dual_derivative`

- les règles de dérivation que suit chaque opération de ta classe ; les tests qui ont échoué d'abord, et pourquoi :

### Ex M18.21 — Le gradient en mode direct : n passages avec des nombres duaux · `forward_gradient`

- le nombre d'appels de f pour n entrées ; les gradients obtenus, comparés à la fiche :

### Ex M18.22 — Lire le gradient dans la différentielle : G[i, j] = df(E_ij), de la forme de la variable · `gradient_from_differential`

- pourquoi G[i, j] = df(E_ij) ; ce que tu as comparé à la comatrice :

### Ex M18.23 — SymPy : dériver une fonction de matrice symbolique, et comparer aux identités

- ce que SymPy rend pour chaque fonction, comparé aux identités de la fiche ; le cas de log det :

### Ex M18.24 — Prédire le nombre d'opérations de chaque mode, puis le compter

- tes prédictions avant l'expérience ; les comptes mesurés, et comment ils croissent avec n :

### Ex M18.25 — Différences finies contre nombres duaux : l'erreur selon le pas h

- le meilleur pas et la meilleure erreur des différences centrées ; les deux pentes de la courbe ; l'erreur des nombres duaux :

### Ex M18.26 — Dessiner un graphe de calcul, avec les dérivées locales sur les arêtes et les adjoints sur les nœuds

- les valeurs, les dérivées locales et les adjoints de ton dessin ; ce que montre la figure :

### Ex M18.27 — Chasse à l'erreur : un gradient transposé, un adjoint compté sur un seul chemin, un pas h trop petit

- pour chaque erreur : ce qu'elle faisait, pourquoi la vérification fournie ne la voyait pas (ou criait à tort), et ta correction :

### Ex M18.28 — Tester une classe par ses propriétés : distributivité et dérivées connues des nombres duaux

- les propriétés testées ; le test qui attrape la classe fausse :

### Ex M18.29 — Défi : dériver une boucle, la méthode de Newton pour √a, en mode direct

- ton point de départ et ton nombre d'itérations ; pourquoi la dérivée converge aussi vite que la valeur :
