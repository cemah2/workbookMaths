# MB5 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/mb5_diffusion/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB5`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une variance est positive ou nulle, et un écart-type en est la racine ; avec $\lvert a\rvert < 1$ et un départ connu, $v_t$ croît vers $v_\infty$ sans la dépasser, et la moyenne est multipliée par $a$ à chaque pas ; la variance d'un pont est nulle aux deux relevés et au plus $\frac{V_T}{4}$ ; une corrélation est entre $-1$ et 1 ; $\gamma$ est entre 0 et 1, $\gamma = \frac{\operatorname{SNR}}{1 + \operatorname{SNR}}$ et $\operatorname{logit}\gamma = \ln\operatorname{SNR}$ ; une survie est entre ses deux bornes exponentielles ; un débruiteur se recompose, $a\,\mathbb{E}[x \mid y] + b\,\mathbb{E}[n \mid y] = y$ ; des probabilités ou des responsabilités sont entre 0 et 1, de somme 1 ; une KL est positive ou nulle, et l'ELBO reste sous $\ln p(x)$ ; une loi guidée de deux gaussiennes demande $\lambda(w) > 0$ ; quand le pas est divisé par 2, l'erreur d'Euler l'est par environ 2, celle du point milieu par environ 4 ; deux pas d'Euler sur le chemin droit donnent un écart-type plus petit que $\tau$. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une loi comme `$\mathcal{N}(\mu, v)$`, une espérance conditionnelle comme `$\mathbb{E}[x \mid y]$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### MB5.Q1 — Une récurrence linéaire gaussienne : quelle moyenne, quelle variance, quand une loi stationnaire, et combien de pas pour oublier le départ ?

1. 
2. 
3. 
4. 
5. 

### MB5.Q2 — Le pont et les couplages : où l'incertitude est la plus grande, ce que fixent les lois marginales et ce qu'elles laissent libre

1. 
2. 
3. 
4. 
5. 

### MB5.Q3 — Signal et bruit : SNR, cotes, logit et décibels, et ce qu'un changement d'échelle ne change pas

1. 
2. 
3. 
4. 
5. 

### MB5.Q4 — Ce que la MSE apprend : une moyenne conditionnelle, pas la valeur la plus probable ; et ce qu'apprennent la MAE et la log-loss

1. 
2. 
3. 
4. 
5. 

### MB5.Q5 — Le score en x : où il pointe, la constante qu'il ignore, et ce que dit la formule de Tweedie

1. 
2. 
3. 
4. 
5. 

### MB5.Q6 — L'ELBO d'une chaîne : quels termes dépendent du modèle, quelle KL compare quoi, et ce que devient une KL entre gaussiennes de même variance

1. 
2. 
3. 
4. 
5. 

### MB5.Q7 — Guider : interpoler ou extrapoler, la différence de deux scores, et quand un produit de puissances n'est plus une densité

1. 
2. 
3. 
4. 
5. 

### MB5.Q8 — Euler, point milieu et chemin droit : ce que coûte un pas, l'ordre de l'erreur, et le sens du temps

1. 
2. 
3. 
4. 
5. 

## 🔁 Rappels

### MB5.R1 — Sommes et images affines de gaussiennes, produit de densités et modèle linéaire gaussien (M25a)

1. 
2. 
3. 
4. 
5. 

### MB5.R2 — Espérance et variance conditionnelles, lois totales, et l'ELBO d'un latent (M25b)

1. 
2. 
3. 
4. 
5. 

### MB5.R3 — Un pas d'Euler (M20), la loi stationnaire d'une chaîne finie (M26) et la cote d'une probabilité (R6)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex MB5.1 — L'anomalie de température d'un lac, un processus autorégressif d'ordre 1 : sa loi dans k jours sachant aujourd'hui, sa loi stationnaire, le nombre de jours pour oublier le départ, et sa loi sachant un jour passé

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB5.2 — La survie d'une ruche à six mois de risques différents : le produit exact, son logarithme, le risque mensuel constant équivalent, et l'encadrement par deux exponentielles

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB5.3 — Un phoque balisé entre deux relevés : sa loi à une heure intermédiaire (le pont d'une marche aléatoire) ; puis des scénarios de position aux mêmes lois à chaque heure, tirés avec un seul nombre au hasard ou avec un bruit frais, et leur corrélation

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex MB5.4 — Une voix mêlée à un bruit de fond : SNR, part de variance de la voix, logit et décibels, puis la voix retrouvée à partir d'une estimation du bruit, et l'erreur amplifiée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB5.5 — Débruiter un signal reçu, d'abord gaussien, puis émis à deux niveaux ±c : E[x | y] par M25a et par la formule de Tweedie (une tanh), et ce que rend le débruiteur quand le bruit tend vers 0

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB5.6 — Un bit altéré par deux relais, puis reconstitué par un modèle retour : ln p(x), l'ELBO de la loi aller des relais, et sa décomposition en reconstruction, KL finale et KL d'un pas retour

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB5.7 — La date de floraison d'une variété et celle de tout le verger, deux lois gaussiennes : la loi p_v^{1+w} p_g^{−w} pour deux valeurs de w, son score, sa condition d'existence et le w limite

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB5.8 — Une tasse de thé qui refroidit : Euler et point milieu contre la solution exacte, l'erreur quand le pas est divisé par deux, un courant de vitesse constante, et un calcul à rebours

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB5.9 — Le chemin droit d'un bruit N(0, 1) vers une loi N(m, τ²) : le champ moyen (affine en x), un pas d'Euler depuis s = 1 qui rend m pour tout départ, puis deux pas, et l'écart-type obtenu contre τ

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

## ∂ Démonstrations

### Ex MB5.10 — La récurrence linéaire gaussienne à coefficients quelconques : la loi de x_t sachant x_0 ; à coefficient constant |a| < 1, la loi sachant un instant passé, la loi stationnaire et la convergence depuis toute loi initiale ; aucune loi stationnaire si |a| ≥ 1

1. 
2. 
3. 
4. 

### Ex MB5.11 — La meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + E[(E[Y | X] − g(X))²], donc g = E[Y | X] ; sur un échantillon, la moyenne de chaque groupe

1. 
2. 
3. 

### Ex MB5.12 — La formule de Tweedie : dériver la densité de y = a x + b n sous l'espérance, d'où E[x | y] et E[n | y] ; la vérification quand x est gaussien

1. 
2. 
3. 
4. 

### Ex MB5.13 — L'ELBO d'une chaîne de latents : Markov et Bayes réécrivent chaque pas aller, la somme télescope ; puis chaque KL entre gaussiennes de même variance devient une MSE pondérée des moyennes

1. 
2. 
3. 
4. 

## 🔗 🗣️ Pont et explication

### Ex MB5.14 — Pont : une loss de débruitage à plusieurs niveaux de bruit, son minimiseur à chaque niveau, et pour des données gaussiennes les MSE minimales sur le signal et sur le bruit, dont le rapport est le SNR

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB5.15 — Expliquer avec le jeu du téléphone pourquoi, après assez de relais qui atténuent et bruitent, le message reçu ne dit plus rien du message émis

*Ta réponse en 5 à 8 phrases, sans formule.*

> 

## 💼 Entretien

### MB5.E1 — « Un modèle de régression entraîné à la MSE prédit-il le prix le plus probable ? Que prédit-il quand les prix d'un même profil se partagent en deux groupes, et quelle loss prendre pour une médiane ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex MB5.16 — Propager la moyenne et la variance d'une récurrence linéaire gaussienne à coefficients quelconques · linear_gaussian_recursion

> 

### Ex MB5.17 — Le débruiteur optimal d'une mesure bruitée quand le signal suit un mélange de gaussiennes, des points compris · posterior_mean_mixture

> 

### Ex MB5.18 — Suivre un champ de vitesses qui dépend du temps : la méthode d'Euler et celle du point milieu, dans les deux sens du temps · euler_ode, midpoint_ode

> 

### Ex MB5.19 — scipy.integrate.solve_ivp : une croissance logistique suivie par tes deux méthodes, l'erreur au temps final selon le nombre de pas en échelle log-log, et les pentes 1 et 2

> 

### Ex MB5.20 — Prédire ce que rend le débruiteur optimal de cinq relevés quand le bruit tend vers 0, pour une mesure proche d'un relevé puis à égale distance de deux, et mesurer

> 

### Ex MB5.21 — Le chemin droit vers une loi gaussienne : Euler et point milieu sur le champ moyen exact, de 1 à 32 pas, la moyenne et l'écart-type obtenus contre ceux de la cible

> 

### Ex MB5.22 — Des lois guidées p_c^{1+w} p_u^{−w} sur une grille : une loi générale à deux bosses, une loi de classe gaussienne, et ce que w resserre et déplace

> 

### Ex MB5.23 — Chasse à l'erreur : un pont aux poids inversés, un débruiteur qui oublie le bruit dans ses responsabilités, et un Euler dont le temps n'avance pas

> 

### Ex MB5.24 — Un test de propriété : Euler exact pour une vitesse constante, le point milieu exact pour une vitesse affine en t, et l'erreur d'Euler divisée par deux avec le pas

> 

### Ex MB5.25 — Défi : transporter un bruit N(0, 1) vers une loi à deux bosses par son champ moyen exact, en au plus huit évaluations du champ, sous une distance de Wasserstein fixée

>
