# MB6 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/mb6_shapley_equite/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB6`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : des indices de Shapley-Shubik sont entre 0 et 1, de somme 1, et des parts de Shapley somment à $v(N) - v(\varnothing)$ ; deux joueurs symétriques reçoivent la même part, un joueur nul 0 ; les dividendes redonnent chaque valeur, $v(S) = \sum_{T \subseteq S}d_T$ ; l'intégrale d'un gradient vaut $f(\text{fin}) - f(\text{début})$ sur tout chemin, et un chemin parcouru à l'envers change le signe ; les parts des coordonnées le long du segment somment à $f(\mathbf{x}) - f(\mathbf{r})$ ; une interpolation bilinéaire reste entre la plus petite et la plus grande des quatre valeurs ; une corrélation de rangs est entre $-1$ et 1, et un rang moyen d'ex aequo est un entier ou un demi-entier ; des taux et une probabilité $q$ sont entre 0 et 1 ; des comptes repondérés gardent les totaux de chaque groupe et de chaque label ; l'erreur type d'un écart est plus grande que chacune des deux, et plus petite que leur somme. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une espérance conditionnelle comme `$\mathbb{E}[Y \mid X = x]$`, une indépendance conditionnelle comme `$\hat Y \perp G \mid Y$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### MB6.Q1 — Jeux coopératifs : ordres ou coalitions, poids d'une coalition, et ce que garantit chaque axiome

1. 
2. 
3. 
4. 
5. 

### MB6.Q2 — Fixer une variable : moyenne marginale ou conditionnelle, courbes ICE parallèles ou non

1. 
2. 
3. 
4. 
5. 

### MB6.Q3 — Intégrales de chemin : boucle fermée, chemin parcouru à l'envers, champ qui n'est pas un gradient, fonction homogène

1. 
2. 
3. 
4. 
5. 

### MB6.Q4 — Grilles et rangs : interpolation bilinéaire, centres ou coins alignés, ex aequo et transformation strictement croissante

1. 
2. 
3. 
4. 

### MB6.Q5 — Indépendance, séparation, suffisance : quel critère pour quelle phrase, et lesquels se contredisent

1. 
2. 
3. 
4. 
5. 

### MB6.Q6 — Tirer au sort entre deux seuils, repondérer, lire l'écart de deux taux : vrai ou faux

1. 
2. 
3. 
4. 
5. 

## 🔁 Rappels

### MB6.R1 — Parties d'un ensemble, factorielles et combinaisons (R4, R8)

1. 
2. 
3. 
4. 
5. 

### MB6.R2 — La dérivée d'une fonction le long d'une courbe : gradient, vitesse et règle de la chaîne (M05b, M17)

1. 
2. 
3. 
4. 
5. 

### MB6.R3 — La loi conditionnelle d'un couple gaussien : une moyenne affine en la valeur observée (M25a)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex MB6.1 — Un conseil de quatre membres à vote pondéré : l'indice de Shapley-Shubik par les 24 ordres, un membre nul, deux membres de poids différents et de même pouvoir, et le nombre d'ordres tirés au hasard qui suffit (Hoeffding)

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex MB6.2 — Trois hameaux partagent une conduite d'eau : la valeur de Shapley par les ordres, les dividendes de Harsanyi, le partage tronçon par tronçon, et les quatre axiomes vérifiés

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex MB6.3 — Le rendement d'une parcelle selon la pluie et l'engrais : courbes ICE et dérivée croisée de deux modèles, puis la moyenne marginale et la moyenne conditionnelle quand pluie et engrais sont corrélés

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB6.4 — Le travail de deux forces entre deux points : un champ de gradient le long de trois chemins, puis un champ qui n'en est pas un (Schwarz) le long de deux chemins

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB6.5 — La variation d'un coût à trois facteurs (prix, quantité, taux de change) partagée entre les facteurs : le long du segment, puis par la moyenne des six chemins en escalier, et pourquoi les deux partages coïncident

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex MB6.6 — Des relevés de capteurs sur une grille 3 × 4 : la dérivée d'un indice régional par un réchauffement uniforme, puis la grille agrandie deux fois par interpolation bilinéaire, centres ou coins alignés

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB6.7 — Un contrôle de pièces sur deux lignes de production aux taux de défauts différents : les taux de rejet sous la séparation, un tirage au sort entre deux seuils pour atteindre un taux de détection, et les poids qui rendent ligne et défaut indépendants

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

## ∂ Démonstrations

### Ex MB6.8 — Unicité de la valeur de Shapley : les jeux d'unanimité forment une base, et les quatre axiomes imposent φ_i = Σ_{T ∋ i} d_T / |T|

1. 
2. 
3. 
4. 
5. 

### Ex MB6.9 — Un score calibré dans un groupe vérifie p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; si deux groupes ont les mêmes moyennes de scores chez leurs positifs et chez leurs négatifs, leurs taux de base sont égaux ou le score est parfait

1. 
2. 
3. 
4. 

### Ex MB6.10 — Indépendance et séparation ne tiennent ensemble, quand les taux de base diffèrent, que pour une décision qui ignore le label ; la repondération P(g)P(y)/P(g, y) rend groupe et label indépendants sans changer leurs marges

1. 
2. 

## 🔗 🗣️ Pont et explication

### Ex MB6.11 — Pont : l'écart des taux de détection de deux laboratoires et son intervalle, par l'erreur type d'une différence de deux proportions, qui se lit avec le nombre d'échantillons positifs de chacun

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex MB6.12 — Expliquer avec trois amis qui partagent un taxi pourquoi on moyenne l'apport de chacun sur tous les ordres d'arrivée

*Ta réponse en 5 à 8 phrases, sans formule.*

> 

## 💼 Entretien

### MB6.E1 — « La valeur de Shapley est la seule répartition qui respecte quatre règles simples : lesquelles, et pourquoi suffisent-elles ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex MB6.13 — Les poids des coalitions dans la valeur de Shapley, exacts ou en flottants · coalition_weights

> 

### Ex MB6.14 — Les dividendes de Harsanyi d'un jeu donné par sa fonction caractéristique · harsanyi_dividends

> 

### Ex MB6.15 — L'intégrale d'un champ de vecteurs le long d'une ligne brisée, par la méthode de Simpson sur chaque segment · line_integral

> 

### Ex MB6.16 — La corrélation de rangs de Spearman, ex aequo compris · spearman_rho

> 

### Ex MB6.17 — Prédire l'intégrale d'un champ de gradient et d'un champ tournant le long d'une boucle triangulaire, dans un sens, dans l'autre et deux fois, puis vérifier

> 

### Ex MB6.18 — Deux mesures corrélées : la moyenne marginale (dépendance partielle) et la moyenne conditionnelle d'une même fonction, simulées pour plusieurs corrélations et comparées aux formules gaussiennes

> 

### Ex MB6.19 — Les lignes de niveau d'une fonction de deux variables, deux chemins entre les mêmes points, et l'intégrale du gradient cumulée le long de chacun

> 

### Ex MB6.20 — Chasse à l'erreur : des poids de coalition sans le facteur 1/n, des ex aequo classés dans l'ordre d'apparition, une interpolation linéaire aux poids échangés

> 

### Ex MB6.21 — Un test de propriété sur des lignes brisées tirées au hasard : le chemin inversé change le signe, un segment coupé en deux ne change rien, un champ de gradient donne f(fin) − f(début)

> 

### Ex MB6.22 — Défi : les indices de Shapley-Shubik exacts d'un conseil de 25 membres, sans parcourir ses coalitions une à une, en comptant par taille et par poids celles où chaque membre est pivot

>
