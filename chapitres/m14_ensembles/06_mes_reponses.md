# M14 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m14_ensembles/06_mes_reponses.md` (créée par `python tools/start_chapter.py M14`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une probabilité et une borne sont entre 0 et 1, une variance est positive, des poids sont positifs et de somme 1, une divergence KL est positive ou nulle, un regret de Hedge reste sous sa borne. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une fraction avec `\frac{a}{b}`, une divergence avec `\mathrm{KL}(a \Vert p)` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M14.Q1 — La queue d'une loi binomiale et ses bornes : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M14.Q2 — Corrélation et variance d'une moyenne

1. 
2. 
3. 
4. 
5. 
6. 

### M14.Q3 — Des limites remarquables

1. 
2. 
3. 
4. 
5. 
6. 

### M14.Q4 — Des poids exponentiels

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M14.R1 — La log-loss et la divergence KL (M13a, M06)

1. 
2. 
3. 
4. 
5. 

### M14.R2 — La variance d'une somme et la matrice de covariance (M02c)

1. 
2. 
3. 
4. 
5. 

### M14.R3 — Taylor et ln(1 + u) (M05a)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M14.1 — La fiabilité d'un système « k parmi n » : au moins k composants qui marchent

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- la somme de a) terme à terme ; la loi de F ; les trois bornes rangées, et pourquoi elles restent loin de d) ; 12 machines dont 10 nécessaires ; la vérification avec binomial_test :

### Ex M14.2 — La variance de la moyenne de trois mesures corrélées, par la matrice de covariance

- a :
- b :
- c :
- d :
- e :
- f :
- c) en 9 termes ; pourquoi a) < b) ; le lagrangien et w* ∝ Σ⁻¹1 ; e) = 1/(1ᵀΣ⁻¹1) ; pourquoi e) bat le meilleur instrument seul :

### Ex M14.3 — (1 + x/n)ⁿ pour quelques n, et des intérêts composés en continu

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- x et les quatre N ; l'ordre de a) à d) ; e) comparé à f) ; g) comparé à −x²/(2n), et pourquoi l'approximation y est moins bonne :

### Ex M14.4 — Les poids exponentiels de cinq experts après trois tours

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- les losses cumulées et les puissances de 3 de chaque tour ; les meilleurs experts ; pourquoi le regret est loin de la borne ; l'effet du η de h) :

### Ex M14.5 — Le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport aux prédictions, et les poids exponentiels qu'il fait apparaître

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- le signe −yᵢ ; l'exemple le plus lourd ; les marges toutes augmentées de 1 ; le facteur multiplicatif quand on ajoute αh ; les gradients coupés de Huber et le point aberrant :

## ∂ Démonstrations

### Ex M14.6 — (1 + x/n)ⁿ → eˣ, par le logarithme et ln(1 + u) ≈ u

1. 
2. 
3. 
4. 
5. 

### Ex M14.7 — Une moyenne pondérée de variables de variance σ² a une variance au plus σ²

1. 
2. 
3. 
4. 
5. 

### Ex M14.8 — La borne de Chernoff d'une queue binomiale : le meilleur λ donne exp(−n KL(a ‖ p))

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 🗣️ Pont et explication

### Ex M14.9 — Pont : ajouter des modèles très corrélés ne sert presque à rien, un plancher de variance sur deux groupes de modèles

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- la moyenne écrite en deux parts ; pourquoi g) > a) ; pourquoi mélanger baisse le plancher ; h) comparé à 110 modèles du groupe A ; la corrélation de deux modèles du groupe A :

### Ex M14.10 — Expliquer pourquoi une moyenne réduit la variance, et quand elle ne la réduit plus

*Ta réponse à ta collègue, en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M14.E1 — « Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est le meilleur ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*
