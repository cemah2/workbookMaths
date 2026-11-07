# M04 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m04_bayes_beta/06_mes_reponses.md` (créée par `python tools/start_chapter.py M04`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Pour chaque mise à jour, écris le tableau hypothèse, a priori, vraisemblance, produit, a posteriori ; pour une loi Beta, dis ce que comptent $a$ et $b$ ; garde les fractions exactes ($\frac{18}{67}$, $\frac{1}{30}$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M04.Q1 — Les quatre termes de la formule de Bayes

1. 
2. 
3. 
4. 
5. 
6. 

### M04.Q2 — Mettre à jour deux fois

1. 
2. 
3. 
4. 
5. 
6. 

### M04.Q3 — La vraisemblance, une fonction du paramètre

1. 
2. 
3. 
4. 
5. 
6. 

### M04.Q4 — La loi Beta : forme et paramètres

1. 
2. 
3. 
4. 
5. 
6. 

### M04.Q5 — Conjuguée, Laplace, MAP

1. 
2. 
3. 
4. 
5. 
6. 

### M04.Q6 — Logarithmes et underflow

1. 
2. 
3. 
4. 
5. 
6. 

### M04.Q7 — Fréquentiste ou bayésien ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M04.R1 — Probabilités conditionnelles (M03)

1. 
2. 
3. 
4. 
5. 

### M04.R2 — Intégrales et densités (M02a)

1. 
2. 
3. 
4. 
5. 

### M04.R3 — Loi binomiale (M02b)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M04.1 — Bayes avec deux hypothèses : un capteur de fuite d'eau

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- b) refait avec les effectifs de d) et e) ; pourquoi b) est si petit ; détection ou fausses alertes : que faut-il améliorer ? :

### Ex M04.2 — Trois hypothèses et un tableau de mise à jour

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le tableau de chaque mise à jour ; e) vérifié de deux façons ; pourquoi la semaine N fait baisser le type R :

### Ex M04.3 — La vraisemblance d'un taux de clic

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- L'allure de L sur [0 ; 0,5] ; b) en une phrase ; pourquoi d) dépasse L(0,15) sans changer le maximum :

### Ex M04.4 — Maximiser une vraisemblance : dériver son logarithme

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- ℓ(λ), ℓ'(λ) et λ̂ pour des durées quelconques ; de même pour μ̂ (Poisson) ; pourquoi le signe de e) prouve un maximum :

### Ex M04.5 — La loi Beta : normalisation, moyenne, mode, variance

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- a) par l'intégrale (parties ou changement de variable) ; f) par le calcul de l'intégrale :

### Ex M04.6 — Conjugaison : de Beta(a, b) à Beta(a + k, b + n − k)

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- b) comme moyenne pondérée de la moyenne a priori et de la fréquence ; ce que change l'a priori moins sûr de g) :

### Ex M04.7 — Lissage de Laplace : la prédictive avec Beta(1, 1)

- a :
- b :
- c :
- d :
- e :
- f :
- Le maximum de vraisemblance en a) et b), et pourquoi il est dangereux ; pourquoi e) n'est pas le carré de a) :

### Ex M04.8 — MAP, maximum de vraisemblance et moyenne a posteriori

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les trois estimations rangées, et l'ordre expliqué ; ce qu'elles deviennent avec 900 adoptions sur 1 000 :

### Ex M04.9 — Un intervalle de crédibilité d'une loi Beta

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La fonction de répartition de Beta(1, b) vérifiée ; pourquoi l'intervalle est asymétrique ; ce que dirait le maximum de vraisemblance :

### Ex M04.10 — Log-probabilités : additionner au lieu de multiplier, normaliser par log-sum-exp

- a :
- b :
- c :
- d :
- e :
- f :
- Les étapes de e) et f) ; le calcul direct de e^(−1000) en float64 :

## ∂ Démonstrations

### Ex M04.11 — La conjugaison Beta-binomiale, démontrée

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M04.12 — Le maximum de vraisemblance d'une loi de Bernoulli est la fréquence

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M04.13 — Le mode de la loi Beta

1. 
2. 
3. 
4. 
5. 
6. 
7. 

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M04.14 — Un test A/B : deux taux de conversion et P(θB > θA) par simulation

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La différence de deux lois normales indépendantes ; ma phrase pour l'équipe produit ; tout passer sur B ? ; ce que ferait Thompson :

### Ex M04.15 — MML §6.3 (relire le théorème de Bayes) et §6.6 : conjugaison et famille exponentielle (lecture guidée)

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M04.16 — MML §8.3 : maximum de vraisemblance et MAP (lecture guidée)

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M04.17 — Expliquer la conjugaison avec des pseudo-observations

*Huit lignes au plus, sans formule compliquée.*

> 

## 💼 Entretien

### M04.E1 — Qu'est-ce que le lissage de Laplace, et pourquoi l'utiliser ?

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M04.18 — Densité et moments de la loi Beta (avec `math.lgamma`)

- a), c) et f) refaits à la main ; pourquoi e) dépasse 20 :

### Ex M04.19 — Mise à jour conjuguée et loi prédictive des prochains essais

- c) et d) à la main ; la binomiale de probabilité 7/20, et pourquoi elle diffère de d) :

### Ex M04.20 — Le MAP d'une loi Beta, cas limites compris

- Les croquis de b), c), d) et e) ; ce que je retrouve en h) :

### Ex M04.21 — La fonction Beta avec `scipy.special` : `beta`, `betaln` et l'underflow

- e) par la formule et par posterior_predictive ; le quotient direct ; l'exponentielle de f) :

### Ex M04.22 — Prédire : le MAP avec Beta(1, 1) après trois échecs

- Mes prédictions avant l'expérience (et pourquoi) ; l'explication de chaque résultat ; pourquoi d) n'est pas le carré de b) :

### Ex M04.23 — Le posterior se resserre : la largeur de l'intervalle en 1/√n

- La largeur quand n est multiplié par 4 ; d) et e) expliqués ; pourquoi la pente n'est pas −0,5 ; g) comparé à a) :

### Ex M04.24 — Prior, vraisemblance et posterior sur une même figure

- La place du sommet de l'a posteriori ; qui tire le plus fort ; la figure avec 90 sur 150 :

### Ex M04.25 — Chasse à l'erreur : évidence oubliée, mise à jour à l'envers, mode et moyenne

- La confusion de chaque ligne fausse ; la ligne juste qui corrige (B) :

### Ex M04.26 — Un calcul stable : comparer des vraisemblances en logarithmes (`math.lgamma`)

- Les trois log-vraisemblances et les a posteriori à la main ; pourquoi des a posteriori si tranchés :

### Ex M04.27 — Défi : traduire l'avis d'un expert en une loi Beta (moyenne, écart type, intervalle)

- Les experts sont-ils d'accord ? lequel est le plus sûr ? ce que pèse chaque avis après 50 pièces :
