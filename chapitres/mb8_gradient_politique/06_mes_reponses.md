# MB8 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/mb8_gradient_politique/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB8`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : un score a une espérance nulle sous sa loi (quand le support ne dépend pas du paramètre), et une information de Fisher est positive ; une probabilité et ses estimations sont entre 0 et 1 ; une variance est positive, et la baseline optimale donne la plus petite des variances que tu calcules ; un estimateur sans biais redonne, en espérance, la dérivée de la formule fermée ; les lignes de $\mathbf{P}_\pi$ somment à 1, celles de $\mathbf{M}$ à $\frac{1}{1 - \gamma}$, et une loi d'occupation actualisée à 1 ; $\sum_a\pi(a \mid s)\,A(s, a) = 0$, et les dérivées par rapport aux logits d'un même état somment à 0 ; les poids d'un λ-retour somment à 1 ; $\mathbb{E}_q[w] = 1$, une taille effective est entre 1 et $n$, une KL est positive et $k_3 \ge 0$ ; les forces centrées somment à 0, et chaque club a autant de victoires attendues qu'observées ; une loi $\pi^\star$ somme à 1, et $\beta\ln Z$ dépasse $F$ de toute autre loi. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une KL comme `$\mathrm{KL}(q \,\|\, p)$`, un score comme `$s_\theta(x) = \partial_\theta\ln p_\theta(x)$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### MB8.Q1 — La fonction score : espérance nulle, information de Fisher, support qui dépend du paramètre, et dériver une espérance par le score ou par le chemin

1. 
2. 
3. 
4. 
5. 

### MB8.Q2 — Variables de contrôle et baselines : ce qui garde l'espérance, ce qui réduit la variance, ce qui biaise

1. 
2. 
3. 
4. 
5. 

### MB8.Q3 — Le gradient de la valeur d'une politique et le λ-retour : la loi d'occupation actualisée, l'avantage d'espérance nulle, le poids de chaque retour à k pas

1. 
2. 
3. 
4. 
5. 

### MB8.Q4 — Échantillonnage d'importance et KL estimée : support, taille effective, poids tronqués, k₁ ou k₃

1. 
2. 
3. 
4. 

### MB8.Q5 — Bradley-Terry et Elo : ce que les forces identifient, quand elles existent, ce que fait une mise à jour

1. 
2. 
3. 
4. 

### MB8.Q6 — Le principe de Gibbs : la loi optimale, ses limites en β, et ce que mesure β ln Z

1. 
2. 
3. 
4. 

## 🔁 Rappels

### MB8.R1 — La jacobienne de la softmax, diag(p) − ppᵀ, lue comme la covariance d'un vecteur one-hot, et la loi de Boltzmann (M17)

1. 
2. 
3. 
4. 

### MB8.R2 — Le système de Bellman d'une politique fixée, la loi d'occupation actualisée et le télescopage des erreurs TD (M26)

1. 
2. 
3. 
4. 

### MB8.R3 — La dérivée par le chemin, son hypothèse de domination, et l'indicatrice où elle échoue (M25b)

1. 
2. 
3. 

## ✏️ Papier-crayon

### Ex MB8.1 — Une attente au téléphone de loi exponentielle de taux θ, et une pénalité au-delà de c minutes : d/dθ P(X > c) par la formule fermée, par l'estimateur score (son espérance calculée) et par le chemin X = ξ/θ ; la variance de l'estimateur score à un tirage

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB8.2 — Deux graines par godet (une loi binomiale B(2, θ)) et un prix selon le nombre de pousses : la dérivée de la recette moyenne, puis l'estimateur score sans baseline, avec b = E[f] et avec la baseline optimale, et leurs variances

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB8.3 — Un camion de crêpes entre deux emplacements, une politique softmax dans l'un d'eux : la chaîne induite, les valeurs, la loi d'occupation actualisée, les valeurs et les avantages des deux actions, puis le gradient de la valeur par rapport aux deux logits

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB8.4 — L'état d'une route (bonne, usée, en travaux) et des valeurs estimées fausses : le biais des retours à 1 et 2 pas, les poids (1 − λ)λ^{k−1} d'un λ-retour, et son biais quand l'erreur est la même partout

- a :
- b :
- c :
- d :
- dans ta copie :

### Ex MB8.5 — Un panel en ligne dont les classes d'âge ne suivent pas le recensement : les poids p/q, la dépense moyenne repondérée, la taille effective de Kish d'un petit échantillon, des poids tronqués (le biais), puis KL(q ‖ p) exacte et ses estimateurs k₁ et k₃ classe par classe

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex MB8.6 — Un tournoi de babyfoot entre trois clubs : deux clubs seuls (la différence de forces en forme fermée), puis vérifier les équations du maximum de vraisemblance pour des forces proposées, la probabilité qu'un club batte un autre, une mise à jour Elo, et un club invaincu

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB8.7 — Trois plats à la cantine : la loi de service qui maximise la satisfaction moyenne moins β fois la KL à la loi actuelle, pour deux valeurs de β, sa valeur β ln Z, comparée à la loi actuelle et au meilleur plat seul

- a :
- b :
- c :
- d :
- dans ta copie :

## ∂ Démonstrations

### Ex MB8.8 — Les deux identités du score, E[s_θ(X)] = 0 et Var(s_θ) = −E[∂²_θ ln p_θ(X)], pour une famille à densité dont le support ne dépend pas de θ ; leur application aux lois de Poisson et exponentielle ; puis la loi uniforme sur [0, θ], où elles tombent

1. 
2. 
3. 
4. 
5. 

### Ex MB8.9 — La baseline optimale b* = E[f s²]/E[s²] d'un estimateur score ; sur n tirages, la moyenne des autres est une baseline sans biais, et la moyenne du groupe multiplie l'estimateur par (n − 1)/n

1. 
2. 
3. 
4. 

### Ex MB8.10 — Le gradient de la valeur d'une politique sous forme matricielle : dériver V = r_π + γP_πV, faire apparaître la loi d'occupation actualisée et la valeur des actions, puis remplacer Q^π par l'avantage

1. 
2. 
3. 
4. 
5. 

## 🔗 🗣️ Pont et explication

### Ex MB8.11 — Pont : la « loss de substitution » −(1/n)Σ(f(x_i) − b) ln p_θ(x_i), dont la dérivée, les f(x_i) et b tenus fixes, est moins l'estimateur score : sur le taux d'une loi de Poisson, puis ce que changent des f standardisés dans le batch

- a :
- b :
- c :
- dans ta copie :

### Ex MB8.12 — Expliquer avec un club d'échecs pourquoi une cote Elo ne dit que des écarts de niveau, et pourquoi battre plus fort que soi rapporte plus de points

*Ta réponse en 5 à 8 phrases, sans formule.*

> 

## 💼 Entretien

### MB8.E1 — « Comment dériver la probabilité d'un événement par rapport au paramètre d'une loi quand on ne peut pas dériver à travers les tirages, et comment rendre l'estimation moins bruitée ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex MB8.13 — L'estimateur score d'une dérivée sur un échantillon, avec une baseline constante ou la moyenne des autres tirages, et son erreur type · score_function_gradient

> 

### Ex MB8.14 — Le gradient exact de la valeur d'une politique softmax tabulaire, par le système de Bellman · policy_gradient_exact

> 

### Ex MB8.15 — Des poids d'importance calculés en log, auto-normalisés ou tronqués, et la taille effective de l'échantillon · importance_weights

> 

### Ex MB8.16 — Les forces d'un modèle de Bradley-Terry par maximum de vraisemblance (l'algorithme de Zermelo), centrées, et le refus d'un tournoi où elles n'existent pas · bradley_terry_fit

> 

### Ex MB8.17 — Prédire l'ordre des écarts-types de l'estimateur score d'une même dérivée, sans baseline, avec la moyenne des autres tirages et avec la baseline optimale, puis les mesurer

> 

### Ex MB8.18 — Un événement rare, P(Z > 4) pour Z normale centrée réduite : Monte-Carlo naïf contre l'échantillonnage d'importance sous N(4, 1), la taille effective, puis des poids tronqués à c : le biais et la variance selon c

> 

### Ex MB8.19 — Chasse à l'erreur : le score d'une loi exponentielle écrit pour la moyenne au lieu du taux, des poids d'importance inversés (q/p), une baseline qui contient le tirage lui-même, des forces de deux tournois sans joueur commun comparées sur une même échelle

> 

### Ex MB8.20 — Un test de propriété pour le gradient exact : sur des MDP tirés au hasard, comparé à des différences finies centrées, et de somme nulle sur les actions de chaque état

> 

### Ex MB8.21 — Défi : estimer, avec un budget de tirages, la dérivée d'une probabilité de dépassement par rapport au paramètre d'une loi, assez précisément neuf fois sur dix (score, baseline, variable de contrôle)

>
