# M13a · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m13a_vraisemblance_logistique/06_mes_reponses.md` (créée par `python tools/start_chapter.py M13a`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie le signe de chaque résultat : une log-vraisemblance de loi discrète est négative ou nulle, une log-loss positive ou nulle, une impureté entre 0 et son maximum. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une fraction avec `\frac{a}{b}`, un logarithme avec `\ln` ou `\log_2` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M13a.Q1 — Vraisemblance, log-vraisemblance, maximum : le vocabulaire

1. 
2. 
3. 
4. 
5. 
6. 

### M13a.Q2 — Log-loss et cross-entropy : la même chose ?

1. 
2. 
3. 
4. 
5. 
6. 

### M13a.Q3 — Les propriétés de la sigmoïde et de la softplus

1. 
2. 
3. 
4. 
5. 
6. 

### M13a.Q4 — Ce que modélise un score w · x + b

1. 
2. 
3. 
4. 
5. 
6. 

### M13a.Q5 — Génératif ou discriminant ?

1. 
2. 
3. 
4. 
5. 
6. 

### M13a.Q6 — Entropie et Gini : leurs propriétés

1. 
2. 
3. 
4. 
5. 
6. 

### M13a.Q7 — Variance intra et variance inter : les feuilles d'un arbre de régression

1. 
2. 
3. 
4. 
5. 

### M13a.Q8 — Convexe ou pas ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M13a.R1 — Bayes et le lissage de Laplace (M04)

1. 
2. 
3. 
4. 
5. 

### M13a.R2 — Entropie, cross-entropy et information mutuelle (M06)

1. 
2. 
3. 
4. 
5. 

### M13a.R3 — Fonctions convexes de plusieurs variables (M10)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M13a.1 — Le maximum de vraisemblance d'une loi de Bernoulli et d'une loi catégorielle

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- la dérivée de ℓ(p) ; un 21ᵉ client au troisième forfait ; pourquoi le lissage change aussi les autres estimations :

### Ex M13a.2 — Le maximum de vraisemblance d'une loi normale : μ̂ et σ̂²

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- ∂ℓ/∂μ et ∂ℓ/∂v ; ℓ(μ̂, σ̂²) = −(n/2)(ln(2πσ̂²) + 1) ; pourquoi g) < f) :

### Ex M13a.3 — La log-loss de quatre prédictions, puis la même en cross-entropy

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- chaque terme comme une cross-entropy ; ce que la log-loss mesure et l'accuracy non :

### Ex M13a.4 — Ce que coûte une prédiction sûre et fausse : la log-loss quand p tend vers 0

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- le taux d'erreur dans a) à c) ; une probabilité 0 et l'écrêtage ; faut-il annoncer 0 ou 1 :

### Ex M13a.5 — La sigmoïde : valeurs, logit, cote et symétrie σ(−z) = 1 − σ(z)

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- σ/(1 − σ) = eᶻ et σ(−z) = 1 − σ(z) ; h) par la cote :

### Ex M13a.6 — La softplus : valeurs, asymptotes et comportement pour |z| grand

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- s(z) − s(−z) = z et s(z) − z = ln(1 + e⁻ᶻ) ; les asymptotes ; où h) est atteint ; pourquoi e^(−|z|) :

### Ex M13a.7 — Un modèle logistique à deux features : probabilités, cote et frontière de décision

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- pourquoi la droite P = 0,85 est parallèle à la frontière ; la direction où la probabilité monte le plus vite :

### Ex M13a.8 — L'hypothèse naïve à la main : une loi jointe factorisée, comparée à la vraie

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- x₁ et x₂ sont-elles indépendantes dans la classe 1 ; pourquoi Naïve Bayes se trompe en (0, 1) ; quand il classe bien :

### Ex M13a.9 — Deux classes gaussiennes de même variance : l'a posteriori est une sigmoïde d'un score affine

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- la log-cote a posteriori, les x² qui s'annulent ; pourquoi d) vaut 0,35 ; la frontière dans le cas h) :

### Ex M13a.10 — L'entropie et l'indice de Gini de quelques distributions

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- les rangements par entropie et par Gini ; la prudence entre 2 et 4 classes :

### Ex M13a.11 — L'information mutuelle d'un tableau de contingence, et la baisse d'entropie qu'elle mesure

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- e) par la formule de la somme ; la ligne qui contribue le plus ; ce que voudrait dire I(X ; Y) = H(Y) :

### Ex M13a.12 — La variance d'un groupe coupé en deux : variance intra plus variance inter

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- la démonstration générale ; pourquoi le terme croisé est nul ; pourquoi h) ne se décompose pas aussi simplement :

## ∂ Démonstrations

### Ex M13a.13 — Le maximum de vraisemblance d'une loi catégorielle, par l'inégalité de Gibbs

1. 
2. 
3. 
4. 
5. 

### Ex M13a.14 — La log-loss moyenne est moins la log-vraisemblance divisée par n

1. 
2. 
3. 
4. 
5. 

### Ex M13a.15 — Log-somme-exp est convexe : sur une droite, sa dérivée seconde est une variance ; la softplus aussi

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M13a.16 — L'indice de Gini est maximal pour la loi uniforme

1. 
2. 
3. 
4. 
5. 

### Ex M13a.17 — L'entropie est maximale pour la loi uniforme, par l'inégalité de Gibbs

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13a.18 — Pont : une sonde linéaire, un modèle logistique en NumPy sur un batch de représentations figées, jusqu'à la log-loss

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- a) en une ligne de NumPy ; pourquoi comparer à e) ; ce que dirait une log-loss de test bien plus basse :

### Ex M13a.19 — MML §8.3, relu après M04 : estimer des paramètres, et ce que la régression logistique y ajoute

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M13a.20 — Fermi : la loi jointe complète contre l'hypothèse naïve, combien de nombres pour 30 features à 4 valeurs ?

1. 
2. 
3. 
4. 
5. 

### Ex M13a.21 — Expliquer pourquoi on minimise la log-loss plutôt que le taux d'erreur

*Ta réponse à ta collègue, en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M13a.E1 — « Pourquoi la cross-entropy est-elle une log-vraisemblance ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M13a.E2 — « Qu'est-ce que le maximum de vraisemblance, et quel lien avec les losses que vous minimisez ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*
