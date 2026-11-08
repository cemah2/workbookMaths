# M11 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m11_logique_concentration/06_mes_reponses.md` (créée par `python tools/start_chapter.py M11`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Écris chaque table de vérité en entier ; pour chaque borne, écris l'inégalité utilisée et vérifie ses hypothèses (variable positive, variables bornées et indépendantes) ; arrondis une taille d'échantillon au-dessus. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M11.Q1 — Réciproque, contraposée, négation

1. 
2. 
3. 
4. 
5. 
6. 

### M11.Q2 — Un argument valide peut-il avoir une conclusion fausse ?

1. 
2. 
3. 
4. 
5. 
6. 

### M11.Q3 — Diagrammes de Venn et quantificateurs

1. 
2. 
3. 
4. 
5. 
6. 

### M11.Q4 — Les pièges de l'induction

1. 
2. 
3. 
4. 
5. 
6. 

### M11.Q5 — Markov ou Tchebychev : quelle borne s'applique ?

1. 
2. 
3. 
4. 
5. 
6. 

### M11.Q6 — Ce que garantit l'inégalité de Hoeffding, et ce qu'elle suppose

1. 
2. 
3. 
4. 
5. 
6. 

### M11.Q7 — Explorer ou exploiter : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M11.R1 — Implication et contraposée (R4)

1. 
2. 
3. 
4. 
5. 

### M11.R2 — Espérance et variance (M02b)

1. 
2. 
3. 
4. 
5. 

### M11.R3 — La loi Beta a posteriori (M04)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M11.1 — Tables de vérité : modus ponens, modus tollens et l'affirmation du conséquent

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- Les tables complètes ; un exemple de la vie courante qui affirme le conséquent ; la forme reconnue en d) :

### Ex M11.2 — Nier des phrases quantifiées sur des modèles et des datasets

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les négations de S₁, S₃ et S₆ ; pourquoi d) et e) diffèrent :

### Ex M11.3 — Des phrases traduites en inclusions d'ensembles, et un contre-exemple

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Chaque phrase en ensembles ; la contraposée de b) ; le diagramme de Venn de A, B et P :

### Ex M11.4 — Une induction trompeuse par oubli du taux de base, recalculée avec Bayes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- L'explication au technicien, avec les effectifs ; les deux probabilités conditionnelles confondues :

### Ex M11.5 — Markov : la queue d'une durée positive

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La moyenne des huit durées et la borne de Markov au seuil 2 ; pourquoi un échantillon positif ne peut pas violer Markov :

### Ex M11.6 — Tchebychev : combien d'observations pour une moyenne à ± 0,1 ?

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La démonstration de a) ; pourquoi connaître σ divise n par plus de 10 :

### Ex M11.7 — Hoeffding : rayon de confiance et taille d'échantillon d'une proportion

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La phrase que garantit l'intervalle de b) ; c) contre d) ; e) contre f) :

### Ex M11.8 — Trois bornes pour une même question : Markov, Tchebychev, Hoeffding, et l'approximation normale

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Pourquoi Markov est si mauvaise ; l'approximation normale est-elle une borne ? ce que représente e) :

### Ex M11.9 — D'où vient le bonus d'UCB : Hoeffding avec un risque qui décroît avec t

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le rayon unilatéral pour le risque t⁻⁴ ; ce que dit g) ; pourquoi f) croît comme ln t :

### Ex M11.10 — ε-greedy : la loi du bras joué et le regret attendu par pas

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- e) contre f) ; le risque d'un ε qui décroît trop vite :

## ∂ Démonstrations

### Ex M11.11 — L'inégalité de Markov

1. 
2. 
3. 
4. 
5. 

### Ex M11.12 — Tchebychev à partir de Markov, puis la loi faible des grands nombres

1. 
2. 
3. 
4. 
5. 

### Ex M11.13 — Avec ε fixé, le regret attendu d'ε-greedy croît au moins linéairement

1. 
2. 
3. 
4. 
5. 

## 🔗 ⚖️ 🗣️ Pont, esprit critique et explication

### Ex M11.14 — Pont : combien d'exemples de test pour connaître une accuracy à ± 2 points, garanti par Hoeffding ?

- a :
- b :
- c :
- d :
- e :
- f :
- Pourquoi Hoeffding est plus large que e) ; ce que protège d) ; la garantie de c) en une phrase, et pourquoi ln(1/δ) :

### Ex M11.15 — Corrélation, causalité et induction : trois titres de presse à démonter

- Titre 1 : (a) l'induction ; (b) deux autres explications ; (c) la donnée qui trancherait :
- Titre 2 : (a) l'induction ; (b) deux autres explications ; (c) la donnée qui trancherait :
- Titre 3 : (a) l'induction ; (b) deux autres explications ; (c) la donnée qui trancherait :
- La règle générale :

### Ex M11.16 — Expliquer « l'optimisme face à l'incertitude » à partir d'un intervalle de confiance

*Six lignes au plus, sans formule, avec « intervalle », « borne supérieure » et « explorer ».*

> 

## 💼 Entretien

### M11.E1 — « À quoi sert l'inégalité de Hoeffding en apprentissage, et que suppose-t-elle ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M11.17 — Les bornes de Markov et de Tchebychev · `markov_bound, chebyshev_bound`

- Pourquoi b) vaut 1, et ce que rendrait la formule sans le min ; ce que dit d) d'une variance nulle :

### Ex M11.18 — La borne et le rayon de Hoeffding · `hoeffding_bound, hoeffding_radius`

- Pourquoi e) redonne le risque de c) ; pourquoi b) dépasse a) et d) vaut le double de c) :

### Ex M11.19 — La queue empirique d'un échantillon · `empirical_tail`

- c) contre e⁻³ ; pourquoi e) est vrai pour tout échantillon positif :

### Ex M11.20 — Les vraies queues d'une loi exponentielle et d'une binomiale (`scipy.stats`) contre les bornes

- La meilleure des deux bornes de e) et f), et pourquoi Hoeffding perd avec n = 60 :

### Ex M11.21 — Prédire : laquelle des trois bornes est la plus serrée pour n = 100 ?

- Mes prédictions avant le calcul (et pourquoi) ; ce que chaque borne utilise ; laquelle choisir sans rien savoir de p :

### Ex M11.22 — La fréquence des écarts |x̄ − p| ≥ t comparée à la borne de Hoeffding, quand n grandit

- La suite qui décroît comme une droite en échelle log ; l'écart entre a) et d) ; pourquoi la borne devient de plus en plus lâche :

### Ex M11.23 — La probabilité qu'un tirage d'une loi Beta dépasse celui d'une autre, par simulation

- Pourquoi Thompson choisit l'option 2 presque une fois sur deux en c) ; ce qui change entre d) et e) :

### Ex M11.24 — Les bornes de Markov, de Tchebychev et de Hoeffding contre la vraie queue, en échelle log

- La meilleure borne selon t ; la borne qui a la même forme que la vraie queue :

### Ex M11.25 — Chasse à l'erreur : Markov pour une variable négative, Hoeffding sans bornes, un rayon sans racine

- Les trois lignes corrigées ; ce que vaudrait markov pour une moyenne négative ; le rayon faux, trop grand ou trop petit :

### Ex M11.26 — Un test paramétré qui vérifie l'inégalité de Markov sur dix lois

- La loi qui attrape markov_bound_half ; pourquoi des lois ordinaires laissent passer une borne trop petite :

### Ex M11.27 — Défi : la plus petite taille d'échantillon qui garantit une moyenne à ± 0,05 avec 99 %, vérifiée sur une loi défavorable

- Mon n₀ et ma méthode ; la comparaison avec Hoeffding et le TCL ; pourquoi Bernoulli(1/2) est défavorable :
