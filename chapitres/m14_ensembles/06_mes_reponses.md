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
- la somme de a) terme à terme ; la loi de F ; la borne de Chernoff, les trois bornes rangées, et pourquoi elles restent loin de d) ; 12 machines dont 10 nécessaires ; la vérification avec binomial_test :

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
- x et les trois N ; l'ordre de a) à d) ; e) comparé à f) ; g) comparé à −x²/(2n), et pourquoi l'approximation y est moins bonne :

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
- la moyenne écrite en deux parts ; ce que dit c) ; pourquoi b) < d) ; h) comparé à 110 modèles du groupe A ; la corrélation de deux modèles du groupe A :

### Ex M14.10 — Expliquer pourquoi une moyenne réduit la variance, et quand elle ne la réduit plus

*Ta réponse à ta collègue, en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M14.E1 — « Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est le meilleur ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M14.11 — La borne de Chernoff et la variance d'une moyenne pondérée · `chernoff_bound, variance_of_average`

- KL(0,45 ‖ 0,24) et a) à la main, comparés à Hoeffding et à la queue exacte ; c) sans les covariances ; 25 × 0.6000000000000001 et la queue qu'on calculerait sans le − 1e-9 ; pourquoi f) est refusé :

### Ex M14.12 — Les poids de l'algorithme Hedge · `hedge_weights`

- les losses cumulées après six tours et a) à la calculatrice ; l'expert le plus lourd et ses tours gagnés ; e^(−ηL) sans retrancher le minimum ; e) comparé à la borne :

### Ex M14.13 — Simuler la moyenne de deux groupes de modèles corrélés, et retrouver aᵀΣa et son plancher

- la moyenne en deux parts, a) et b) à la main ; l'écart entre simulation et théorie, et √(2/n) ; la corrélation de deux modèles du groupe B ; une covariance Cov(Z_A, Z_B) négative :

### Ex M14.14 — Les poids exponentiels au fil des tours : quel expert domine, selon le learning rate

- pour chaque η, l'expert qui domine et le tour où il passe 0,5 ; les à-coups de η = 3 et leur coût ; η = 0,15 ; ton choix pour 80 tours et √(8 ln K/T) :

### Ex M14.15 — Chasse à l'erreur : P(X ≥ k) calculée comme P(X > k), des covariances oubliées, des poids non renormalisés

- après la vérification : ce que calcule chaque ligne fausse, et sa correction ; les lignes justes qui leur ressemblent ; la borne corrigée comparée à la probabilité exacte :

### Ex M14.16 — Un test qui vérifie que la borne de Chernoff majore la queue exacte de `scipy.stats`, sur une grille de n, p et a

- la propriété et le cas de ta grille qui attrapent chaque fausse borne ; les deux vraies bornes refusées, et pourquoi ; pourquoi bound_fixed_lambda dépasse 1 :

### Ex M14.17 — Défi : suivre le meilleur de dix experts avec Hedge sans connaître l'horizon, un regret sous la borne théorique sur 1 000 tours

- où échouent η = 0,01, le meilleur η constant pour T = 1 000 et « suivre le meneur », et pourquoi ; ton choix, et pourquoi il ne dépend pas de T ; tes regrets au tour 1 000 :
