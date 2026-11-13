# M25a · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m25a_gaussienne/06_mes_reponses.md` (créée par `python tools/start_chapter.py M25a`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : un facteur de Cholesky par $\mathbf{L}\mathbf{L}^\top = \boldsymbol{\Sigma}$, une distance de Mahalanobis deux fois (par $\boldsymbol{\Sigma}^{-1}$ et par le système triangulaire $\mathbf{L}\mathbf{y} = \mathbf{x} - \boldsymbol{\mu}$), une variance toujours positive, une covariance $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$ symétrique, une variance conditionnelle plus petite que la variance marginale et indépendante de la valeur lue, un déterminant par $\det\boldsymbol{\Sigma}_{bb} \times \det(\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{bb})$, une fusion de mesures par des précisions qui s'additionnent, une KL positive ou nulle (et le sens des deux lois), un point du slerp de norme $R$ et d'angle $t\Omega$ avec $\mathbf{u}$. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, une loi comme `$\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$` et une divergence comme `$\mathrm{KL}(p \,\|\, q)$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M25a.Q1 — Lire une densité gaussienne multivariée : det Σ, distance de Mahalanobis et point le plus probable

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M25a.Q2 — Ce qui reste gaussien : images affines, sommes, produits et normes ; deux marginales gaussiennes ne suffisent pas

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M25a.Q3 — Ellipses de niveau et masse : quel axe, quel demi-axe, quelle proportion, en dimension 2 et au-delà

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M25a.Q4 — Complément de Schur, loi marginale ou loi conditionnelle : quel bloc, quelle moyenne, quelle variance ?

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M25a.Q5 — Fusionner des mesures et mettre à jour un a priori gaussien : précisions, moyennes pondérées et prédictive

1. 
2. 
3. 
4. 
5. 
6. 

### M25a.Q6 — Le maximum de vraisemblance de μ et Σ : diviser par n, et une covariance singulière quand n ≤ d

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M25a.Q7 — La divergence KL continue en situations : deux supports qui ne se couvrent pas, deux lois exponentielles, une loi produit, et les deux sens

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M25a.Q8 — Ligne droite ou arc de grand cercle : extrémités, norme et angle parcouru

1. 
2. 
3. 
4. 
5. 
6. 
7. 

## 🔁 Rappels

### M25a.R1 — Le changement de variable en dimension 1 et les coordonnées polaires (M02b)

1. 
2. 
3. 
4. 
5. 
6. 

### M25a.R2 — Le théorème spectral, Cholesky et la covariance AΣAᵀ (M12c)

1. 
2. 
3. 
4. 
5. 
6. 

### M25a.R3 — Les gradients de ln det X et de tr(AX) par rapport à une matrice (M18)

1. 
2. 
3. 
4. 
5. 
6. 

## ✏️ Papier-crayon

### Ex M25a.1 — La densité d'un couple gaussien (température et humidité d'une serre) en deux points : distance de Mahalanobis contre distance euclidienne

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

### Ex M25a.2 — Trois mesures corrélées : la loi d'une somme pondérée et d'une différence, puis un tirage μ + Lε par Cholesky et sa covariance

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M25a.3 — Les ellipses à 90 % et à 95 % des composantes du vent sur un site : axes, demi-axes, aire, et la part des relevés dans l'ellipse de niveau c

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

### Ex M25a.4 — Un capteur en panne estimé par ses deux voisins : complément de Schur, loi conditionnelle en dimension 3, et l'écart-type gagné

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

### Ex M25a.5 — Fusionner trois mesures d'une même distance : le produit de densités gaussiennes, des précisions qui s'additionnent, un ordre sans importance

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M25a.6 — Étalonner un thermomètre par la régression linéaire bayésienne : loi jointe, évidence, posterior de (a, b), et prédictive près et loin des points d'étalonnage

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

### Ex M25a.7 — La divergence KL continue entre deux lois exponentielles et entre deux lois uniformes : les deux sens, une KL infinie, et deux durées de vie indépendantes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M25a.8 — Deux réglages d'une machine de découpe, deux gaussiennes en dimension 2 des erreurs de position : la KL dans les deux sens, et le cas de même covariance

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

### Ex M25a.9 — La route orthodromique entre deux villes : angle au centre, point au tiers du trajet par le slerp, et profondeur du milieu de la corde

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

## ∂ Démonstrations

### Ex M25a.10 — Le changement de variable multivarié : la densité de μ + Lε est celle de N(μ, LLᵀ), et AX + b reste gaussien pour A inversible

1. 
2. 
3. 
4. 
5. 

### Ex M25a.11 — La masse d'une ellipse de Mahalanobis en dimension 2 vaut 1 − e^{−c²/2} ; la densité de la norme en dimension d, et son mode √(d − 1)

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M25a.12 — Le maximum de vraisemblance d'une gaussienne multivariée : μ̂ = x̄ et Σ̂ = S/n, par les gradients de ln det et de la trace

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M25a.13 — L'inégalité de Jensen pour une variable continue, la positivité de la KL continue, et l'additivité de la KL sur des lois produits

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M25a.14 — La KL entre N(μ₀, Σ₀) et N(μ₁, Σ₁) en dimension d, par le lemme de la trace ; l'entropie différentielle de N(μ, Σ)

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M25a.15 — Le slerp entre deux vecteurs de même norme reste sur la sphère et avance d'un angle constant ; sa limite quand l'angle tend vers 0

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M25a.16 — Pont : des vecteurs rangés en lignes (n, d) comme dans les bibliothèques : tirer n points d'un coup par E Lᵀ + μ, la log-densité de chaque ligne, et la moyenne en nats par coordonnée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M25a.17 — MML §6.5 et la fin de §6.7.2 : densité, marginales et conditionnelles, produit, sommes et transformations, échantillonnage et changement de variable multivarié, en anglais

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

### Ex M25a.18 — MML §9.3 : régression linéaire bayésienne, prédictions a priori et a posteriori, vraisemblance marginale, en anglais

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 

### Ex M25a.19 — Expliquer avec deux thermomètres voisins pourquoi lire l'un resserre l'estimation de l'autre, et pourquoi la valeur lue ne change pas cette incertitude

*Ta réponse en 6 à 10 phrases, sans formule, avec une image de la vie courante, puis en 3 phrases.*

> 

## 💼 Entretien

### M25a.E1 — « Comment tirer un vecteur gaussien de covariance donnée à partir de tirages indépendants, et pourquoi Cholesky ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M25a.20 — La log-densité d'une loi normale multivariée, par Cholesky · mvn_logpdf

- tes contrôles de formes et tes refus ; les tests qui ont échoué d'abord, et pourquoi ; ce que montre la dimension 600 :

### Ex M25a.21 — Tirer des vecteurs de loi N(μ, Σ) par Cholesky · sample_mvn

- ton tirage en lignes et la graine ; l'écart entre les moments empiriques et la loi, et le blanchiment :

### Ex M25a.22 — Le complément de Schur d'un bloc, et la loi conditionnelle d'un vecteur gaussien · schur_complement, condition_gaussian

- tes blocs et l'ordre des indices ; ce que montrent le déterminant, la précision et le changement des valeurs lues :

### Ex M25a.23 — Le posterior d'une régression linéaire bayésienne · linreg_posterior

- la forme « précisions » ; la mise à jour bain par bain, le lien avec ridge, et la bande de la prédictive :

### Ex M25a.24 — scipy.stats.multivariate_normal, np.cov et scipy.integrate : tes log-densités, le maximum de vraisemblance, et la KL de M25a.8 par une intégrale double

- les comparaisons avec SciPy et np.cov ; la KL par trois méthodes et l'erreur type de l'estimation par tirages :

### Ex M25a.25 — Prédire la part des tirages dans l'ellipsoïde de Mahalanobis de même niveau quand la dimension passe de 2 à 10, puis mesurer

- tes prédictions avant l'expérience ; celles qui étaient fausses, et pourquoi :

### Ex M25a.26 — Conditionner par simulation : garder les tirages dont une mesure tombe près d'une valeur, et comparer à la loi conditionnelle exacte

- le biais et le nombre de relevés gardés selon la fenêtre, et ta conclusion :

### Ex M25a.27 — Les ellipses de niveau d'une gaussienne en dimension 2, une tranche (la loi conditionnelle) et une projection (la loi marginale), selon la corrélation

- ce que montre chaque colonne, et le rôle de la corrélation :

### Ex M25a.28 — Chasse à l'erreur : un tirage par E L au lieu de E Lᵀ, ln det Σ sans le facteur 2, et une covariance conditionnelle qui dépend de la valeur observée

- pour chaque erreur : ce qu'elle faisait, pourquoi la vérification fournie ne la voyait pas, et ta correction :

### Ex M25a.29 — Un test de propriété : la moyenne et la covariance empiriques de tes tirages, à une tolérance fixée par l'erreur type

- ton choix de k, le taux d'échec mesuré, les versions fausses attrapées, et le nombre de tirages nécessaire pour une erreur fine :

### Ex M25a.30 — Défi : reconstruire les températures manquantes le long d'une route par la loi conditionnelle d'une gaussienne, sous une erreur quadratique moyenne fixée

- ta covariance jointe, ton erreur quadratique moyenne, et où ta reconstruction bat l'interpolation linéaire :
