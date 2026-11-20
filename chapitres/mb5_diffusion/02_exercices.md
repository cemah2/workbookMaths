# MB5 · Les maths de la diffusion — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/mb5_diffusion/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB5`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et du 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : $\mathcal{N}(\mu, v)$ a pour second paramètre une **variance** ; un bruit $\varepsilon$ ou $n$ suit $\mathcal{N}(0, 1)$ et est indépendant de tout le reste ; les logarithmes sont népériens et les KL en nats. Une récurrence s'écrit $x_t = a_tx_{t-1} + b_t\varepsilon_t$, de moments $m_t$ et $v_t$, de variance stationnaire $v_\infty = \frac{b^2}{1 - a^2}$ quand $a_t = a$ et $b_t = b$ ; une marche aléatoire a les variances cumulées $V_s$ ($s$ est un instant passé au §1, intermédiaire au §2). Une mesure s'écrit $y = ax + bn$, avec $\operatorname{SNR} = \frac{a^2}{b^2}$ et la part $\gamma = \frac{a^2}{a^2 + b^2}$ quand $x$ a la variance 1 ; $s_Y = (\ln p_Y)'$ est le score de la loi de $y$. Au §7, la loi guidée de $p_c$ et $p_u$ est proportionnelle à $p_c^{1+w}p_u^{-w}$, de précision $\lambda(w)$. Aux §8 et §9, un champ s'écrit $f(t, x)$, le temps d'abord ; $h$ est le pas (au §1, $h_k$ est un risque), $N$ le nombre de pas, $t_k = t_0 + kh$ les instants et $t_N$ l'instant final. Au §9, $x_s = (1 - s)x_0 + s\varepsilon$ ($s = 0$ la donnée, $s = 1$ le bruit), $v(x, s) = \mathbb{E}[\varepsilon - x_0 \mid x_s = x]$ est le champ moyen, et $z = x(1)$ le point de départ. Dans le notebook, un vecteur s'écrit comme une liste ou un tableau **1-D**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 à 6 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### MB5.Q1 — Une récurrence linéaire gaussienne : quelle moyenne, quelle variance, quand une loi stationnaire, et combien de pas pour oublier le départ ? 🧠 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. $x_t = -0{,}5\,x_{t-1} + 2\varepsilon_t$, avec $x_0 = 6$ connu. Que valent la moyenne et la variance de $x_1$, puis de $x_2$ ?
2. Quelle est la loi stationnaire de cette récurrence ?
3. Avec $b \ne 0$, pour lesquelles de ces valeurs de $a$ la récurrence $x_t = ax_{t-1} + b\varepsilon_t$ a-t-elle une loi stationnaire : $0{,}99$ ; $-1$ ; $1{,}01$ ; $-0{,}3$ ?
4. Vrai ou faux : pour $a = 1$ et $b \ne 0$, la variance de $x_t$ sachant $x_0$ vaut $tb^2$, et ne se stabilise jamais.
5. Pour $a = -0{,}5$, après combien de pas l'écart entre la moyenne de $x_t$ et la moyenne stationnaire est-il divisé par 1 000 ? Et l'écart entre la variance de $x_t$ et la variance stationnaire ?

### MB5.Q2 — Le pont et les couplages : où l'incertitude est la plus grande, ce que fixent les lois marginales et ce qu'elles laissent libre 🧠 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

Une marche aléatoire a des pas de même variance $0{,}4$ ; elle vaut 0 à l'instant 0 et 5 à l'instant 10.
1. À quel instant la variance de $x_s$, sachant ces deux valeurs, est-elle la plus grande, et que vaut-elle ?
2. Quelle est la loi de $x_4$ sachant ces deux valeurs ?
3. $U$ et $Z$ sont indépendants, de loi $\mathcal{N}(0, 1)$. Quelle loi suit $2U + \sqrt5\,Z$ ? Pour quelles valeurs de $\sigma$ la variable $\sqrt{9 - \sigma^2}\,U + \sigma Z$ suit-elle la même loi ?
4. Vrai ou faux : deux processus qui ont la même loi à chaque instant ont la même corrélation entre deux instants.
5. $X_t = \sqrt t\,U$ (un seul tirage) et la marche $W_t$ de pas $\mathcal{N}(0, 1)$ ont-ils la même loi à chaque instant $t \ge 1$ ? Que valent la corrélation de $X_1$ et $X_4$, puis celle de $W_1$ et $W_4$ ?

### MB5.Q3 — Signal et bruit : SNR, cotes, logit et décibels, et ce qu'un changement d'échelle ne change pas 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. $y = 1{,}8\,x + 0{,}5\,n$, avec $x$ de variance 1. Le SNR, puis la part $\gamma$ (4 décimales).
2. Une mesure a $\gamma = 0{,}96$ : son SNR, puis $\operatorname{logit}\gamma$ (3 décimales).
3. On multiplie $y$ par 10 (un amplificateur). Que deviennent le SNR et $\gamma$ ?
4. Il faut 15 dB pour comprendre une voix. À quelle part $\gamma$ cela correspond-il (3 décimales) ?
5. Vrai ou faux : quand le SNR double, $\gamma$ double.

### MB5.Q4 — Ce que la MSE apprend : une moyenne conditionnelle, pas la valeur la plus probable ; et ce qu'apprennent la MAE et la log-loss 🧠 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

1. Pour un même profil $X = x$, la cible $Y$ vaut 10 avec la probabilité $0{,}7$ et 40 avec la probabilité $0{,}3$. Quelle prédiction minimise la MSE ? $Y$ peut-elle prendre cette valeur ?
2. Que vaut alors la MSE ?
3. Quelle prédiction minimise la MAE ?
4. Pour une cible binaire (0 ou 1), que prédit, à $X$ fixé, un modèle assez souple entraîné à la log-loss ?
5. Vrai ou faux : sur un échantillon, la fonction de $X$ qui minimise la MSE empirique donne, pour chaque valeur observée de $X$, la moyenne des $Y$ de ce groupe.

### MB5.Q5 — Le score en x : où il pointe, la constante qu'il ignore, et ce que dit la formule de Tweedie 🧠 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

1. Le score de $\mathcal{N}(3, 4)$ en $x = 7$, puis en $x = 1$. Vers quel point pointe-t-il ?
2. $p(x) = C\,e^{-x^4/4}$, où la constante $C$ est inconnue. Que vaut le score en $x = 2$ ?
3. Vrai ou faux : le score d'une densité dérivable et strictement positive s'annule en chacun de ses modes.
4. $y = 2x + 0{,}5\,n$, et la loi de $y$ a le score $s_Y(3) = -1{,}2$. Que valent $\mathbb{E}[n \mid y = 3]$ et $\mathbb{E}[x \mid y = 3]$ ?
5. Vrai ou faux : la formule de Tweedie suppose que le signal $x$ suit une loi gaussienne.

### MB5.Q6 — L'ELBO d'une chaîne : quels termes dépendent du modèle, quelle KL compare quoi, et ce que devient une KL entre gaussiennes de même variance 🧠 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

Un processus aller $q$ fixé et un modèle retour $p$ dont la loi de départ $p(z_T)$ est fixée.
1. Lequel des trois termes de l'ELBO (reconstruction, KL finale, KL des pas retour) ne dépend pas du modèle retour ?
2. La KL du pas $t$ compare $p(z_{t-1} \mid z_t)$ à quelle loi ?
3. Que vaut $\mathrm{KL}\big(\mathcal{N}(2{,}2 ;\ 0{,}5) \,\|\, \mathcal{N}(1{,}7 ;\ 0{,}5)\big)$ ?
4. Vrai ou faux : quel que soit le processus aller, l'ELBO ne dépasse jamais $\ln p(x)$.
5. Deux pas retour gaussiens ont la même variance $\sigma^2$. Si l'on divise $\sigma^2$ par 2 sans changer les moyennes, que devient leur KL ?

### MB5.Q7 — Guider : interpoler ou extrapoler, la différence de deux scores, et quand un produit de puissances n'est plus une densité 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Pour $w = -0{,}3$, le point $(1 + w)\,y_c - w\,y_u$ est-il sur le segment $[y_u, y_c]$ ? Écris-le comme un barycentre de $y_c$ et $y_u$.
2. Pour $w = 1{,}25$, où est-il ?
3. Que vaut $\nabla_x\ln p(x \mid c) - \nabla_x\ln p(x)$ ?
4. $p_c = \mathcal{N}(0, 4)$ et $p_u = \mathcal{N}(1, 1)$. Pour quels $w \ge 0$ la loi guidée existe-t-elle ?
5. Vrai ou faux : si $\sigma_c \le \sigma_u$, la loi guidée de deux gaussiennes existe pour tout $w \ge 0$.

### MB5.Q8 — Euler, point milieu et chemin droit : ce que coûte un pas, l'ordre de l'erreur, et le sens du temps 🧠 ★ ⏱️ 5 min
*Fiche §8 et §9 · parcours C, E*

1. Tu as droit à 12 évaluations du champ. Combien de pas d'Euler peux-tu faire ? Combien de pas du point milieu ?
2. On divise le pas par 2. L'erreur au temps final d'Euler est divisée par environ combien ? Celle du point milieu ?
3. En échelles logarithmiques, l'erreur au temps final contre le nombre de pas suit des droites : de quelles pentes, pour Euler et pour le point milieu ?
4. Pour remonter de $t = 5$ à $t = 2$ en 6 pas, que vaut $h$ ?
5. Données $\mathcal{N}(m, \tau^2)$, chemin droit, champ moyen exact. Un seul pas d'Euler de $s = 1$ à $s = 0$ rend : (A) le départ $z$ ; (B) $m$, quel que soit $z$ ; (C) un tirage de $\mathcal{N}(m, \tau^2)$.

<a id="rappels"></a>

## 🔁 Rappels

### MB5.R1 — Sommes et images affines de gaussiennes, produit de densités et modèle linéaire gaussien (M25a) 🔁 ★ ⏱️ 6 min
*Fiche §1 et §2 · parcours C, E*

1. $X \sim \mathcal{N}(5, 2)$ et $Y \sim \mathcal{N}(-1, 5)$ sont indépendantes. La loi de $X + Y$, puis celle de $2X - Y$.
2. $\mathcal{N}(x \mid 1, 2)\,\mathcal{N}(x \mid 4, 6)$ est proportionnel à $\mathcal{N}(x \mid m, v)$ : que valent $m$ et $v$ ?
3. $x \sim \mathcal{N}(10, 3)$, et l'on mesure $y = x + w$, avec $w \sim \mathcal{N}(0, 1)$ indépendant de $x$. La loi de $x$ sachant $y = 15$.
4. Vrai ou faux : la somme de deux variables gaussiennes est toujours gaussienne.
5. D'après MML §6.5.3, quelle loi suit $\mathbf{A}\mathbf{x} + \mathbf{b}$ quand $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ ?

### MB5.R2 — Espérance et variance conditionnelles, lois totales, et l'ELBO d'un latent (M25b) 🔁 ★ ⏱️ 6 min
*Fiche §4 et §6 · parcours C, E*

1. $Z \in \{0, 1\}$, $P(Z = 1) = 0{,}3$ ; $X$ sachant $Z = 0$ suit $\mathcal{N}(2, 1)$, et $X$ sachant $Z = 1$ suit $\mathcal{N}(7, 4)$. $\mathbb{E}[X]$, puis $\mathbb{V}(X)$ par les lois totales.
2. Que vaut $\mathbb{E}\big[\mathbb{E}[Y \mid X]\big]$ ?
3. Pour une observation $x$ et une loi $q$ du latent, $\ln p(x) = -2{,}1$ et $\mathrm{KL}\big(q \,\|\, p(z \mid x)\big) = 0{,}4$. Que vaut l'ELBO de $q$ ?
4. Pour quelle loi $q$ l'ELBO vaut-elle $\ln p(x)$ ?
5. Pour une observation, les deux composantes d'un mélange ont $\ln\big(\pi_k\,\mathcal{N}(x \mid \mu_k, v_k)\big) = -3{,}2$ et $-1{,}7$. La responsabilité de la seconde (4 décimales).

### MB5.R3 — Un pas d'Euler (M20), la loi stationnaire d'une chaîne finie (M26) et la cote d'une probabilité (R6) 🔁 ★ ⏱️ 6 min
*Fiche §1, §3 et §8 · parcours C, E*

1. Un pas d'Euler de $h = 0{,}1$ pour $x' = -2x + 1$, depuis $x = 3$.
2. Même champ, depuis $x = 3$, avec $h = 1{,}5$ : le pas rapproche-t-il $x$ du point fixe $0{,}5$ ?
3. La loi stationnaire de la chaîne de matrice de transition $\begin{pmatrix} 0{,}79 & 0{,}21 \\ 0{,}42 & 0{,}58 \end{pmatrix}$.
4. La cote puis le logit de $p = 0{,}12$ (2 décimales).
5. Quelle probabilité a pour cote 7 ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les logarithmes, les exponentielles et les racines), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex MB5.1 — L'anomalie de température d'un lac, un processus autorégressif d'ordre 1 : sa loi dans k jours sachant aujourd'hui, sa loi stationnaire, le nombre de jours pour oublier le départ, et sa loi sachant un jour passé ✏️ ★★ ⏱️ 30 min
**Objectif :** propager la loi d'un AR(1) jour après jour, trouver sa loi stationnaire, mesurer combien de temps il garde la mémoire de son départ, et écrire sa loi sachant un jour passé.
**Prérequis :** fiche §1 ; R5 (suite géométrique, somme), M25a (image affine d'une gaussienne) · **Parcours :** C, E

L'anomalie de température de surface d'un lac (l'écart à la normale du jour, en °C) suit, d'un jour au suivant, $x_t = 0{,}88\,x_{t-1} + 0{,}35\,\varepsilon_t$. Aujourd'hui (jour 0), on mesure $x_0 = 2{,}5$.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne et la variance de $x_1$ | une liste de 2 nombres (4 décimales) |
| b | la moyenne et la variance de $x_3$ | une liste de 2 nombres (4 décimales) |
| c | la variance $v_\infty$ de la loi stationnaire | un nombre (4 décimales) |
| d | le plus petit nombre de jours $k$ pour lequel la moyenne de $x_k$ passe sous le dixième de l'écart-type stationnaire | un entier |
| e | le jour 20, on mesure $x_{20} = -1{,}4$ : la moyenne et la variance de $x_{25}$ sachant $x_{20}$ | une liste de 2 nombres (4 décimales) |

Dans ta copie : écris $x_3$ en fonction de $x_0$, $\varepsilon_1$, $\varepsilon_2$, $\varepsilon_3$ ; dis pourquoi la loi de $x_{25}$ sachant $x_{20}$ ne dépend pas de $x_0$.

### Ex MB5.2 — La survie d'une ruche à six mois de risques différents : le produit exact, son logarithme, le risque mensuel constant équivalent, et l'encadrement par deux exponentielles ✏️ ★ ⏱️ 20 min
**Objectif :** calculer une survie comme un produit cumulé, passer par son logarithme, et l'encadrer par deux exponentielles du risque cumulé.
**Prérequis :** fiche §1 ; R6 (logarithme d'un produit), M20 §6 ($1 + u \le e^u$) · **Parcours :** C, E

Une apicultrice suit une colonie d'abeilles pendant l'hivernage, d'octobre à mars. Le risque de perdre la colonie au cours d'un mois, si elle a survécu jusque-là, vaut, mois après mois : $h = (0{,}01 ;\ 0{,}03 ;\ 0{,}07 ;\ 0{,}12 ;\ 0{,}14 ;\ 0{,}07)$. On note $H = \sum_kh_k$ le risque cumulé.

| | Question | Réponse attendue |
|---|---|---|
| a | la probabilité $P$ que la colonie survive aux six mois | un nombre (4 décimales) |
| b | $\ln P$ | un nombre (4 décimales) |
| c | le risque mensuel constant $\bar h$ qui donnerait la même survie en six mois | un nombre (4 décimales) |
| d | la borne supérieure $e^{-H}$ | un nombre (4 décimales) |
| e | la borne inférieure $e^{-H - \sum_kh_k^2}$ | un nombre (4 décimales) |

Dans ta copie : écris $\ln P$ comme une somme, et vérifie que chaque $h_k$ remplit la condition de la borne inférieure.

### Ex MB5.3 — Un phoque balisé entre deux relevés : sa loi à une heure intermédiaire (le pont d'une marche aléatoire) ; puis des scénarios de position aux mêmes lois à chaque heure, tirés avec un seul nombre au hasard ou avec un bruit frais, et leur corrélation ✏️ ★★ ⏱️ 30 min
**Objectif :** conditionner une marche aléatoire sur deux instants, puis construire des scénarios qui ont les mêmes lois à chaque heure mais pas les mêmes trajectoires.
**Prérequis :** fiche §2 ; M25a §5 (modèle linéaire gaussien), M02b (variance d'une différence) · **Parcours :** C

Un phoque porte une balise qui donne sa position le long d'une côte (en km) quand il fait surface. Entre deux relevés, sa position suit une marche aléatoire heure par heure : de 8 h à 11 h, il chasse, et chaque heure ajoute un déplacement de variance 2 km² ; de 11 h à 16 h, il se repose, et chaque heure ajoute une variance de $0{,}5$ km². La balise donne 3 km à 8 h et 9 km à 16 h.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne et la variance de la position à 11 h, sachant les deux relevés | une liste de 2 nombres (4 décimales) |
| b | l'heure entière, de 9 h à 15 h, où cette variance est la plus grande, puis cette variance | une liste de 2 nombres (3 décimales) |

Pour préparer des scénarios à partir de 8 h, sans connaître le relevé de 16 h, on prend la position de 8 h pour origine. La position à l'heure $t$ suit alors $\mathcal{N}(0, V_t)$, où $V_t$ est la variance cumulée depuis 8 h. Trois façons de tirer des scénarios qui ont **cette loi à chaque heure**, de 9 h à 16 h (à 8 h, la position est l'origine) :
- **la marche** : un déplacement frais à chaque heure ;
- **un seul tirage** : $X_t = \sqrt{V_t}\,U$, avec un seul $U \sim \mathcal{N}(0, 1)$ pour toute la journée ;
- **un bruit frais** : $X_t = \sqrt{V_t - \sigma^2}\,U + \sigma Z_t$, avec $\sigma^2 = 1{,}5$ et un $Z_t \sim \mathcal{N}(0, 1)$ frais à chaque heure, indépendant de $U$.

| | Question | Réponse attendue |
|---|---|---|
| c | la corrélation des positions de 10 h et de 13 h, pour la marche | un nombre (4 décimales) |
| d | la même corrélation, pour le bruit frais | un nombre (4 décimales) |

Dans ta copie : vérifie par le lemme de la fiche que, avec le bruit frais, $X_t$ suit bien $\mathcal{N}(0, V_t)$ à chaque heure, et dis pourquoi $\sigma^2$ ne peut pas dépasser 2 ici.

### Ex MB5.4 — Une voix mêlée à un bruit de fond : SNR, part de variance de la voix, logit et décibels, puis la voix retrouvée à partir d'une estimation du bruit, et l'erreur amplifiée ✏️ ★★ ⏱️ 20 min
**Objectif :** passer du SNR à la part de variance, au logit et aux décibels, puis retrouver un signal à partir d'une estimation du bruit et chiffrer l'erreur qui l'accompagne.
**Prérequis :** fiche §3 ; R6 (cote, logit, $\log_{10}$) · **Parcours :** C, E

Deux enregistrements mêlent une voix $x$ et un bruit de fond $n$, indépendants, de moyenne nulle et de variance 1 : l'enregistrement 1 mesure $y = 1{,}2\,x + 0{,}5\,n$, l'enregistrement 2, fait de loin, $y = 0{,}3\,x + 1{,}8\,n$.

| | Question | Réponse attendue |
|---|---|---|
| a | le SNR de l'enregistrement 1 | un nombre (2 décimales) |
| b | sa part de variance de la voix $\gamma$ | un nombre (4 décimales) |
| c | $\operatorname{logit}\gamma$ | un nombre (4 décimales) |
| d | son SNR en décibels | un nombre (1 décimale) |
| e | un logiciel de transcription demande au moins 9 dB : la part $\gamma$ qui correspond à ce seuil | un nombre (4 décimales) |
| f | enregistrement 2 : on mesure $y = 0{,}9$, et un filtre estime le bruit à $\hat n = 0{,}7$ : l'estimation $\hat x$ de la voix | un nombre (4 décimales) |
| g | le rapport $\lvert\hat x - x\rvert / \lvert\hat n - n\rvert$ des deux erreurs, pour l'enregistrement 1 puis pour l'enregistrement 2 | une liste de 2 nombres (4 décimales) |

Dans ta copie : écris $\hat x - x$ en fonction de $\hat n - n$.

### Ex MB5.5 — Débruiter un signal reçu, d'abord gaussien, puis émis à deux niveaux ±c : E[x | y] par M25a et par la formule de Tweedie (une tanh), et ce que rend le débruiteur quand le bruit tend vers 0 ✏️ ★★ ⏱️ 35 min
**Objectif :** calculer le débruiteur optimal de deux façons pour un signal gaussien, puis pour un signal à deux niveaux, et voir sa limite quand le bruit s'efface.
**Prérequis :** fiche §5 ; M25a §5 (modèle linéaire gaussien), R6 (tanh) · **Parcours :** C, E

Un récepteur capte $y = ax + bn$.
- **Partie A.** Le signal émis suit $x \sim \mathcal{N}(1, 4)$, et $y = 2x + 3n$. On reçoit $y = 6$.
- **Partie B.** La source envoie $x = +2$ ou $x = -2$, avec la probabilité $\frac12$ chacun, et $y = 0{,}5\,x + n$. On reçoit $y = 1{,}1$.

| | Question | Réponse attendue |
|---|---|---|
| a | partie A : $\mathbb{E}[x \mid y = 6]$ par le modèle linéaire gaussien | un nombre (4 décimales) |
| b | partie A : le score $s_Y(6)$ de la loi de $y$ | un nombre (4 décimales) |
| c | partie A : $\mathbb{E}[n \mid y = 6]$ par la formule de Tweedie | un nombre (4 décimales) |
| d | partie B : $\mathbb{E}[x \mid y = 1{,}1]$ | un nombre (4 décimales) |
| e | partie B : $\mathbb{E}[n \mid y = 1{,}1]$ | un nombre (4 décimales) |
| f | partie B, avec toujours $a = 0{,}5$ et $y = 1{,}1$ : la limite de $\mathbb{E}[x \mid y]$ quand $b \to 0$ | un nombre (4 décimales) |

Dans ta copie : retrouve a) par la formule de Tweedie ; pour la partie B, écris $p_Y(y)$, puis $\mathbb{E}[x \mid y]$ sous la forme $c\tanh(\cdot)$.

### Ex MB5.6 — Un bit altéré par deux relais, puis reconstitué par un modèle retour : ln p(x), l'ELBO de la loi aller des relais, et sa décomposition en reconstruction, KL finale et KL d'un pas retour ✏️ ★★★ ⏱️ 40 min
**Objectif :** calculer sur une chaîne binaire de deux pas la vraisemblance, l'ELBO de la loi aller et ses trois termes, et vérifier que l'ELBO reste sous $\ln p(x)$.
**Prérequis :** fiche §6 ; M25b §5 (ELBO d'un latent), M26 (produit de matrices de transition), M04 (Bayes), M06 (KL discrète) · **Parcours :** C, E

Un bit $x \in \{0, 1\}$ traverse deux relais radio. Le premier l'inverse avec la probabilité $0{,}22$ et rend $z_1$ ; le second inverse $z_1$ avec la probabilité $0{,}4$ et rend $z_2$ : c'est le processus aller $q(z_1 \mid x)\,q(z_2 \mid z_1)$. Un modèle retour reconstitue le message dans l'autre sens : $p(z_2 = 1) = 0{,}3$ ; $p(z_1 \mid z_2)$ inverse $z_2$ avec la probabilité $0{,}16$ ; $p(x \mid z_1)$ inverse $z_1$ avec la probabilité $0{,}32$. On observe $x = 1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $q(z_2 \mid x = 1)$, sous la forme $[q(z_2 = 0 \mid x = 1),\ q(z_2 = 1 \mid x = 1)]$ | une liste de 2 nombres (4 décimales) |
| b | le pas retour qui connaît $x$ : $[q(z_1 = 1 \mid z_2 = 0, x = 1),\ q(z_1 = 1 \mid z_2 = 1, x = 1)]$ | une liste de 2 nombres (4 décimales) |
| c | $\ln p(x = 1)$ | un nombre (4 décimales) |
| d | l'ELBO de la loi aller $q(z_1, z_2 \mid x = 1)$, par sa décomposition : la reconstruction moins les deux KL de e) | un nombre (4 décimales) |
| e | la reconstruction, la KL finale et la KL du pas retour moyennée sous $q$ | une liste de 3 nombres (4 décimales) |

Dans ta copie : écris $q(z_2 \mid x)$ comme le produit de deux matrices $2 \times 2$ ; vérifie que d) reste sous c), et dis ce que mesure l'écart.

### Ex MB5.7 — La date de floraison d'une variété et celle de tout le verger, deux lois gaussiennes : la loi p_v^{1+w} p_g^{−w} pour deux valeurs de w, son score, sa condition d'existence et le w limite ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer une loi guidée de deux gaussiennes, son score comme une combinaison de deux scores, et la condition qui la fait exister.
**Prérequis :** fiche §7 ; M25a §5 (produit de deux densités gaussiennes) · **Parcours :** C, E

Dans un verger de pommiers, la date de pleine floraison (en jours depuis le 1er janvier) d'une variété suit $p_v = \mathcal{N}(102, 25)$ ; celle de tout le verger, toutes variétés mêlées, suit $p_g = \mathcal{N}(108, 81)$. On guide la variété contre le verger : la loi guidée est proportionnelle à $p_v^{1+w}p_g^{-w}$ ($p_v$ joue le rôle de $p_c$ et $p_g$ celui de $p_u$).

| | Question | Réponse attendue |
|---|---|---|
| a | la variance de la loi guidée pour $w = 0{,}4$ | un nombre (4 décimales) |
| b | sa moyenne pour $w = 0{,}4$ | un nombre (4 décimales) |
| c | la moyenne et la variance de la loi guidée pour $w = 1{,}25$ | une liste de 2 nombres (4 décimales) |
| d | le score de la loi guidée pour $w = 1{,}25$, en $x = 96$ | un nombre (4 décimales) |
| e | une variété tardive suit $\mathcal{N}(115, 144)$ : le $w$ limite à partir duquel sa loi guidée contre le verger n'existe plus | un nombre (4 décimales) |

Dans ta copie : écris la précision $\lambda(w)$ ; dis de quel côté de 102 la moyenne est poussée, et pourquoi la première variété n'a pas de $w$ limite.

### Ex MB5.8 — Une tasse de thé qui refroidit : Euler et point milieu contre la solution exacte, l'erreur quand le pas est divisé par deux, un courant de vitesse constante, et un calcul à rebours ✏️ ★★ ⏱️ 30 min
**Objectif :** suivre une équation différentielle par les deux méthodes, mesurer leurs erreurs quand le pas diminue, et remonter le temps ; dire quand Euler est exact.
**Prérequis :** fiche §8 ; M20 §6 (Euler), R6 (exponentielle) · **Parcours :** C, E

Une tasse de thé à 85 °C refroidit dans une pièce à 20 °C selon $T' = -0{,}06\,(T - 20)$, $t$ en minutes ($T$ est ici la température, pas une durée comme au §8).

| | Question | Réponse attendue |
|---|---|---|
| a | la température exacte à 10 min | un nombre (2 décimales) |
| b | la température à 10 min par Euler, avec $h = 5$ min, puis avec $h = 2{,}5$ min | une liste de 2 nombres (2 décimales) |
| c | la même par le point milieu, avec $h = 5$ min, puis $h = 2{,}5$ min | une liste de 2 nombres (2 décimales) |
| d | le rapport de l'erreur avec $h = 5$ à l'erreur avec $h = 2{,}5$, pour Euler, puis pour le point milieu, calculé avec les valeurs non arrondies de a), b) et c) | une liste de 2 nombres (1 décimale) |
| e | à 10 min, une autre tasse est à 47 °C : sa température à 5 min par un pas d'Euler à rebours, puis la valeur exacte | une liste de 2 nombres (2 décimales) |

Dans ta copie : une feuille de thé tombée dans un ruisseau suit un courant de vitesse constante ; dis, sans calcul, pourquoi un seul pas d'Euler donne sa position exacte à tout instant ; puis dis pourquoi le pas à rebours de e) donne une température trop basse.

### Ex MB5.9 — Le chemin droit d'un bruit N(0, 1) vers une loi N(m, τ²) : le champ moyen (affine en x), un pas d'Euler depuis s = 1 qui rend m pour tout départ, puis deux pas, et l'écart-type obtenu contre τ ✏️ ★★★ ⏱️ 35 min
**Objectif :** calculer le champ moyen d'un chemin droit vers des données gaussiennes, puis voir ce qu'en font un et deux pas d'Euler.
**Prérequis :** fiche §9 ; M25a §5 (modèle linéaire gaussien), MB5.5 · **Parcours :** C, E

Des données $x_0 \sim \mathcal{N}(4 ;\ 0{,}25)$ ($m = 4$, $\tau = 0{,}5$), un bruit $\varepsilon \sim \mathcal{N}(0, 1)$ indépendant, le chemin droit $x_s = (1 - s)\,x_0 + s\,\varepsilon$, et son champ moyen $v(x, s) = \frac{x - \mathbb{E}[x_0 \mid x_s = x]}{s}$. On suit $x' = v(x, s)$ de $s = 1$ à $s = 0$ par la méthode d'Euler, depuis $z = x(1) = -0{,}7$.

| | Question | Réponse attendue |
|---|---|---|
| a | la variance $\sigma(s)^2$ de $x_s$ en $s = 0{,}5$ | un nombre (4 décimales) |
| b | le champ moyen $v(1{,}5 ;\ 0{,}5)$ | un nombre (4 décimales) |
| c | le point atteint par un seul pas d'Euler, de $s = 1$ à $s = 0$ | un nombre (4 décimales) |
| d | le point atteint par deux pas d'Euler ($h = -0{,}5$) | un nombre (4 décimales) |
| e | l'écart-type de la loi qu'on obtient en deux pas depuis $z \sim \mathcal{N}(0, 1)$, puis le point d'arrivée exact de la trajectoire partie de $z = -0{,}7$ | une liste de 2 nombres (4 décimales) |

Dans ta copie : montre que $v(x, 1) = x - m$, et écris le point atteint en deux pas sous la forme $m + \kappa z$.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex MB5.10 — La récurrence linéaire gaussienne à coefficients quelconques : la loi de x_t sachant x_0 ; à coefficient constant |a| < 1, la loi sachant un instant passé, la loi stationnaire et la convergence depuis toute loi initiale ; aucune loi stationnaire si |a| ≥ 1 ∂ ★★ ⏱️ 30 min
**Objectif :** démontrer la loi d'une récurrence linéaire gaussienne à coefficients quelconques, puis le comportement d'un AR(1) selon $\lvert a\rvert$.
**Prérequis :** fiche §1 ; R4 (récurrence), R5 (somme géométrique, récurrence affine), M25a §2 (combinaison de gaussiennes indépendantes), M26 §1 (propriété de Markov) · **Parcours :** C, E

$x_t = a_tx_{t-1} + b_t\varepsilon_t$ pour $t \ge 1$, avec des réels $a_t$ et $b_t$ quelconques, et des bruits $\varepsilon_1, \varepsilon_2, \ldots$ indépendants de loi $\mathcal{N}(0, 1)$, indépendants de $x_0$. Tu peux utiliser sans le redémontrer qu'une combinaison linéaire de variables gaussiennes indépendantes, plus une constante, est gaussienne (M25a).
1. Montre par récurrence sur $t$ que $x_t = (a_1\cdots a_t)\,x_0 + \sum_{k=1}^tb_k\,(a_{k+1}\cdots a_t)\,\varepsilon_k$ (un produit vide vaut 1). Déduis-en que, sachant $x_0$, $x_t$ suit $\mathcal{N}\big((a_1\cdots a_t)\,x_0,\ \sum_kb_k^2(a_{k+1}\cdots a_t)^2\big)$.
2. Désormais $a_t = a$ et $b_t = b \ne 0$. Si $a^2 \ne 1$, montre que, pour $t > s$, $x_t$ sachant $x_s$ suit $\mathcal{N}\Big(a^{t-s}x_s,\ b^2\dfrac{1 - a^{2(t-s)}}{1 - a^2}\Big)$.
3. On suppose $\lvert a\rvert < 1$. Montre que $\mathcal{N}(0, v_\infty)$, $v_\infty = \frac{b^2}{1 - a^2}$, est stationnaire. Puis, si $x_0 \sim \mathcal{N}(m_0, v_0)$, montre que $m_t = a^tm_0$ et $v_t - v_\infty = a^{2t}(v_0 - v_\infty)$, et conclus sur la loi de $x_t$ quand $t \to \infty$.
4. On suppose $\lvert a\rvert \ge 1$. Montre qu'aucune loi de variance finie n'est stationnaire. Que vaut $v_t$ pour $a = 1$ ?

### Ex MB5.11 — La meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + E[(E[Y | X] − g(X))²], donc g = E[Y | X] ; sur un échantillon, la moyenne de chaque groupe ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que la MSE est minimale pour l'espérance conditionnelle, et ce que cela donne sur un échantillon.
**Prérequis :** fiche §4 ; M02c §1 (la moyenne minimise la somme des carrés), M25b §2 (lois totales) · **Parcours :** C, E

$X$ est une variable discrète, de valeurs $\xi_1, \ldots, \xi_K$ de probabilités $p_k > 0$ ; $Y$ a une variance finie ; $g$ est une fonction quelconque.
1. Pour un $k$ fixé et une constante $c$, montre que $\mathbb{E}\big[(Y - c)^2 \mid X = \xi_k\big] = \mathbb{V}(Y \mid X = \xi_k) + \big(\mathbb{E}[Y \mid X = \xi_k] - c\big)^2$.
2. Déduis-en, par la formule des probabilités totales, que $\mathbb{E}[(Y - g(X))^2] = \mathbb{E}[\mathbb{V}(Y \mid X)] + \mathbb{E}\big[(\mathbb{E}[Y \mid X] - g(X))^2\big]$. Conclus : quelle $g$ minimise la MSE, et quel est ce minimum ?
3. Sur un échantillon $(x_1, y_1), \ldots, (x_n, y_n)$, on minimise la MSE empirique $\frac1n\sum_i(y_i - g(x_i))^2$. Montre que la meilleure $g$ prend, en chaque valeur $\xi$ observée de $X$, la moyenne des $y_i$ tels que $x_i = \xi$, et que le minimum est la moyenne des variances empiriques des groupes, pondérées par leurs effectifs.

### Ex MB5.12 — La formule de Tweedie : dériver la densité de y = a x + b n sous l'espérance, d'où E[x | y] et E[n | y] ; la vérification quand x est gaussien ∂ ★★★ ⏱️ 30 min
**Objectif :** démontrer la formule de Tweedie en dimension 1, puis la retrouver dans le cas gaussien.
**Prérequis :** fiche §5 ; M04 (Bayes), M25a §5, M25b §7 (dériver sous l'espérance) · **Parcours :** C

$y = ax + bn$, avec $b > 0$ et $n \sim \mathcal{N}(0, 1)$ indépendant de $x$. On note $\varphi_b$ la densité de $\mathcal{N}(0, b^2)$.
1. $x$ est discrète, de valeurs $\xi_1, \ldots, \xi_K$ de probabilités $\pi_k$. Écris $p_Y(y)$ comme une somme, puis montre que $p_Y'(y) = -\frac{1}{b^2}\sum_k\pi_k\,(y - a\xi_k)\,\varphi_b(y - a\xi_k)$.
2. Divise par $p_Y(y)$ et reconnais, par la formule de Bayes, les probabilités $P(x = \xi_k \mid y)$. Déduis-en $s_Y(y) = -\frac{y - a\,\mathbb{E}[x \mid y]}{b^2}$, puis $\mathbb{E}[x \mid y] = \frac{y + b^2s_Y(y)}{a}$ (pour $a \ne 0$) et $\mathbb{E}[n \mid y] = -b\,s_Y(y)$.
3. $x$ a une densité $p_X$ : dis en une ou deux phrases ce qui change dans le calcul (une intégrale au lieu de la somme ; la dérivation sous l'intégrale, admise, M25b §7).
4. Vérifie la formule quand $x \sim \mathcal{N}(m, \tau^2)$ : calcule $s_Y$, puis $\mathbb{E}[x \mid y]$ par Tweedie, et compare au modèle linéaire gaussien de M25a §5.

### Ex MB5.13 — L'ELBO d'une chaîne de latents : Markov et Bayes réécrivent chaque pas aller, la somme télescope ; puis chaque KL entre gaussiennes de même variance devient une MSE pondérée des moyennes ∂ ★★★ ⏱️ 40 min
**Objectif :** démontrer la décomposition de l'ELBO d'une chaîne de latents, puis lire ses termes quand les pas sont gaussiens.
**Prérequis :** fiche §6 ; M25b §5 (ELBO d'un latent), M04 (Bayes), R4 (somme télescopique), M25a §7 (KL entre gaussiennes) · **Parcours :** C

Le processus aller est $q(z_{1:T} \mid x) = q(z_1 \mid x)\prod_{t=2}^Tq(z_t \mid z_{t-1})$, le modèle retour $p(x, z_{1:T}) = p(z_T)\prod_{t=2}^Tp(z_{t-1} \mid z_t)\;p(x \mid z_1)$, pour des latents discrets ou continus, et $\operatorname{ELBO} = \mathbb{E}_q\big[\ln p(x, z_{1:T}) - \ln q(z_{1:T} \mid x)\big]$, l'espérance étant prise sous $q(z_{1:T} \mid x)$.
1. Pour $t \ge 2$, explique pourquoi $q(z_t \mid z_{t-1}) = q(z_t \mid z_{t-1}, x)$, puis montre que $q(z_t \mid z_{t-1}, x) = \frac{q(z_{t-1} \mid z_t, x)\,q(z_t \mid x)}{q(z_{t-1} \mid x)}$.
2. Remplace chaque $q(z_t \mid z_{t-1})$ dans $\ln q(z_{1:T} \mid x)$, et montre que les rapports $\frac{q(z_t \mid x)}{q(z_{t-1} \mid x)}$ se télescopent.
3. Regroupe les termes de l'ELBO en $\mathbb{E}_q[\ln p(x \mid z_1)]$, en un terme qui ne fait intervenir que $z_T$, et en un terme pour chaque $t \ge 2$. Montre que ces deux derniers sont $-\mathrm{KL}\big(q(z_T \mid x) \,\|\, p(z_T)\big)$ et $-\mathbb{E}_q\big[\mathrm{KL}\big(q(z_{t-1} \mid z_t, x) \,\|\, p(z_{t-1} \mid z_t)\big)\big]$.
4. Pour deux pas gaussiens de même variance $\sigma^2$ et de moyennes $\mu_q$ et $\mu_p$, écris le terme du pas $t$ avec $\mu_q - \mu_p$ (KL de M25a §7 admise) : pourquoi une MSE pondérée ?

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB5.14 — Pont : une loss de débruitage à plusieurs niveaux de bruit, son minimiseur à chaque niveau, et pour des données gaussiennes les MSE minimales sur le signal et sur le bruit, dont le rapport est le SNR 🔗 ★ ⏱️ 25 min
**Objectif :** minimiser une loss de débruitage qui mêle plusieurs niveaux de bruit, et relier ses MSE minimales au SNR de chaque niveau.
**Prérequis :** fiche §3, §4 et §5 ; M25a §5 · **Parcours :** C, E

Un signal standardisé $x \sim \mathcal{N}(0, 1)$ est mesuré à trois niveaux de bruit $k = 1, 2, 3$ : $y = a_kx + b_kn$, avec $(a_1, b_1) = (2{,}2 ;\ 1)$, $(a_2, b_2) = (1{,}1 ;\ 1{,}7)$ et $(a_3, b_3) = (0{,}5 ;\ 2{,}5)$. Chaque exemple tire son niveau avec les probabilités $0{,}5$, $0{,}3$ et $0{,}2$, et l'on cherche une fonction $g(y, k)$ qui prédit le bruit $n$, en minimisant la loss $L(g) = \sum_k\omega_k\,\mathbb{E}\big[(n - g(y, k))^2\big]$, où $(\omega_1, \omega_2, \omega_3) = (0{,}5 ;\ 0{,}3 ;\ 0{,}2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | au niveau 2, le coefficient $c$ du meilleur prédicteur $\mathbb{E}[n \mid y] = c\,y$ | un nombre (4 décimales) |
| b | la MSE minimale sur le bruit, $\mathbb{E}\big[(n - \mathbb{E}[n \mid y])^2\big]$, aux trois niveaux | une liste de 3 nombres (4 décimales) |
| c | la MSE minimale sur le signal, $\mathbb{E}\big[(x - \mathbb{E}[x \mid y])^2\big]$, aux trois niveaux | une liste de 3 nombres (4 décimales) |
| d | la valeur minimale de $L$ | un nombre (4 décimales) |

Dans ta copie : dis en une phrase pourquoi le minimiseur de $L$ est, à chaque niveau, $\mathbb{E}[n \mid y]$ ; vérifie, au niveau 2, que le rapport de la MSE de b) à celle de c) est le SNR.

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB5.15 — Expliquer avec le jeu du téléphone pourquoi, après assez de relais qui atténuent et bruitent, le message reçu ne dit plus rien du message émis 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule l'oubli du départ d'une récurrence qui atténue et bruite.
**Prérequis :** fiche §1 ; MB5.1 · **Parcours :** C, E

Au jeu du téléphone, chaque joueur murmure à son voisin ce qu'il a cru entendre. Imagine un message réduit à un nombre (une hauteur de voix, par exemple), que chaque joueur transmet un peu affaibli et brouillé d'une erreur nouvelle. Un enfant te demande : « pourquoi, au bout de la file, on ne peut plus deviner ce qu'a dit le premier ? ».

Réponds-lui en 5 à 8 phrases, sans formule : ce que fait chaque relais au message et à l'erreur ; ce qui reste du message de départ après beaucoup de relais ; pourquoi l'erreur ne grandit pas sans fin ; ce que l'on peut encore dire du message reçu (sa dispersion habituelle) ; et pourquoi la file oublie d'autant plus vite que chaque relais affaiblit davantage.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### MB5.E1 — « Un modèle de régression entraîné à la MSE prédit-il le prix le plus probable ? Que prédit-il quand les prix d'un même profil se partagent en deux groupes, et quelle loss prendre pour une médiane ? » 💼 ★ ⏱️ 10 min
*Fiche §4 · parcours C*

« Un modèle de régression entraîné à la MSE prédit-il le prix le plus probable ? Que prédit-il quand les prix d'un même profil se partagent en deux groupes, et quelle loss prendre pour une médiane ? »

Ta réponse doit dire ce que la MSE apprend, avec l'argument en une phrase ; pourquoi ce n'est pas la valeur la plus probable ; ce qui se passe quand les prix d'un même profil forment deux groupes ; ce qu'apprend la MAE, et quand la préférer ; et comment obtenir plus que la moyenne (des quantiles, ou la loi entière).

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/mb5_diffusion/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| MB5.16 | Propager la moyenne et la variance d'une récurrence linéaire gaussienne à coefficients quelconques · `linear_gaussian_recursion` | 🔨 | ★ | 25 | C, E |
| MB5.17 | Le débruiteur optimal d'une mesure bruitée quand le signal suit un mélange de gaussiennes, des points compris · `posterior_mean_mixture` | 🔨 | ★★ | 35 | C, E |
| MB5.18 | Suivre un champ de vitesses qui dépend du temps : la méthode d'Euler et celle du point milieu, dans les deux sens du temps · `euler_ode`, `midpoint_ode` | 🔨 | ★★ | 35 | C, E |
| MB5.19 | `scipy.integrate.solve_ivp` : une croissance logistique suivie par tes deux méthodes, l'erreur au temps final selon le nombre de pas en échelle log-log, et les pentes 1 et 2 | 📦 | ★ | 20 | C |
| MB5.20 | Prédire ce que rend le débruiteur optimal de cinq relevés quand le bruit tend vers 0, pour une mesure proche d'un relevé puis à égale distance de deux, et mesurer | 🔮 | ★ | 15 | C, E |
| MB5.21 | Le chemin droit vers une loi gaussienne : Euler et point milieu sur le champ moyen exact, de 1 à 32 pas, la moyenne et l'écart-type obtenus contre ceux de la cible | 🔬 | ★★ | 25 | C, E |
| MB5.22 | Des lois guidées p_c^{1+w} p_u^{−w} sur une grille : une loi générale à deux bosses, une loi de classe gaussienne, et ce que w resserre et déplace | 🎨 | ★ | 20 | C |
| MB5.23 | Chasse à l'erreur : un pont aux poids inversés, un débruiteur qui oublie le bruit dans ses responsabilités, et un Euler dont le temps n'avance pas | 🐛 | ★ | 20 | C, E |
| MB5.24 | Un test de propriété : Euler exact pour une vitesse constante, le point milieu exact pour une vitesse affine en t, et l'erreur d'Euler divisée par deux avec le pas | 🛠️ | ★ | 25 | C |
| MB5.25 | Défi : transporter un bruit N(0, 1) vers une loi à deux bosses par son champ moyen exact, en au plus huit évaluations du champ, sous une distance de Wasserstein fixée | 🏆 | ★★★ | 30 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les trois 🔨 complètent ta copie `mon_travail/mymath/gaussian_paths.py` (**mymath :** `gaussian_paths.py`), dont la docstring du module dit ce qui est permis : NumPy et `math`, et aucune SciPy (`solve_ivp`, `odeint`, `quad`, `norm`, `logsumexp`, `softmax`) : les tests comparent tes résultats avec SciPy et avec des simulations ; les imports relatifs de tes propres modules sont permis (`from .approx import logsumexp`, M05a) ; ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de sa fonction dans `tests/test_mb5_gaussian_paths.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.gaussian_paths.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier sont recopiées dans une cellule du notebook.

**MB5.16 · 🔨 `linear_gaussian_recursion(a, b, mean0=0.0, var0=0.0)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments (deux tableaux 1-D de même longueur, de nombres finis ; `mean0` et `var0` réels finis, ni booléens, `var0` $\ge 0$), puis propage $m_t = a_tm_{t-1}$ et $v_t = a_t^2v_{t-1} + b_t^2$, et rends les deux tableaux de longueur $T + 1$. Lance le groupe de tests. Ensuite : a) le lac de MB5.1 sur trois jours : la moyenne et la variance de $x_3$ (une liste de 2 nombres, à comparer à ta copie) ; b) au printemps, la persistance et le bruit changent chaque semaine : le notebook fournit `A_16` et `B_16`, les coefficients de douze semaines, et le départ $x_0 \sim \mathcal{N}(1{,}5 ;\ 0{,}3)$ : la moyenne et la variance de $x_{12}$ (une liste de 2 nombres) ; c) $a = -0{,}68$, $b = 1{,}1$ pendant six pas, depuis $x_0 = 5$ connu : la moyenne et la variance de $x_6$, puis $v_\infty$ (une liste de 3 nombres). Ce qu'il faut regarder : pourquoi les moyennes de c) changent-elles de signe à chaque pas, et de combien leur valeur absolue diminue-t-elle ? Par quel côté la variance approche-t-elle $v_\infty$ ?

**MB5.17 · 🔨 `posterior_mean_mixture(y, a, b, weights, means, variances)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments ; pour chaque composante, la variance $a^2s_k^2 + b^2$ de $y$, le logarithme de $\pi_k\,\mathcal{N}(y \mid a\mu_k, a^2s_k^2 + b^2)$ ($-\infty$ pour un poids nul) et $\mathbb{E}[x \mid y, k]$ ; les responsabilités par un log-sum-exp sur $k$, pour chaque mesure ; enfin la moyenne pondérée, de la forme de `y` ; pour $a = 0$, la moyenne du mélange. Lance le groupe de tests. Ensuite : a) la partie A de MB5.5, comme un mélange à une composante (un nombre, à comparer à ta copie) ; b) la partie B de MB5.5, comme deux points de poids $\frac12$ (un nombre) ; c) un signal reçu qui suit le mélange $0{,}25\,\mathcal{N}(-1{,}4 ;\ 0{,}2) + 0{,}75\,\mathcal{N}(2{,}3 ;\ 0{,}5)$, mesuré par $y = 0{,}7\,x + 0{,}5\,n$ : $\mathbb{E}[x \mid y]$ pour $y = -0{,}9$, $0{,}3$ et $1{,}7$ (une liste de 3 nombres). Ce qu'il faut regarder : pour $y = -0{,}9$, quelle composante l'emporte, malgré son petit poids, et pourquoi $\mathbb{E}[x \mid y]$ n'est-il pas $\frac ya$ ? Que rend ta fonction pour $a = 0$ ?

**MB5.18 · 🔨 `euler_ode(f, x0, t0, t1, n_steps)` et `midpoint_ode(f, x0, t0, t1, n_steps)`.** Écris les deux fonctions, en suivant leurs docstrings : contrôle `n_steps` (un entier $\ge 1$, pas un booléen ni un flottant), `t0` et `t1` (des réels finis) et la forme de chaque vitesse ; $h = \frac{t_N - t_0}{N}$, négatif si $t_N < t_0$ (l'argument `t1`, comme celui de `solve_ivp`, est l'instant final $t_N$) ; une évaluation de `f` par pas pour Euler, deux pour le point milieu ; rends les $N + 1$ points, départ compris. Lance les deux groupes de tests. Ensuite : a) le thé de MB5.8, à 10 min, par Euler puis par le point milieu, avec deux pas (une liste de 2 nombres, à comparer à ta copie) ; b) la tasse à 47 °C de MB5.8 e), remontée de 10 min à 5 min en dix pas d'Euler (un nombre) ; c) $x' = 3t^2$, $x(0) = 0$, sur $[0, 2]$ en quatre pas : Euler, puis le point milieu (une liste de 2 nombres) ; d) $x' = t - x$, $x(0) = 2$, sur $[0, 3]$ en six pas : l'erreur d'Euler, puis celle du point milieu, par rapport à la solution exacte $t - 1 + 3e^{-t}$ (une liste de 2 nombres, positifs). Ce qu'il faut regarder : à quelle somme de M02a correspondent les deux valeurs de c), et pourquoi le point milieu n'y est-il pas exact ? De combien l'erreur de b) en dix pas est-elle plus petite que celle d'un seul pas, en MB5.8 e) ?

**MB5.19 · 📦 `scipy.integrate.solve_ivp` et une croissance logistique.** Une culture de levures suit $P' = 0{,}9\,P\big(1 - \frac{P}{40}\big)$ (en millions de cellules, $t$ en heures), depuis $P(0) = 1{,}5$. Relève : a) $P(8)$ par `solve_ivp(…, rtol=1e-10, atol=1e-10)` (un nombre), à comparer à la solution exacte de la fiche ; b) pour $N = 8$, 16, 32, 64, 128 et 256 pas, l'erreur de `euler_ode` puis celle de `midpoint_ode` en $t = 8$ (deux listes de 6 nombres), et trace-les contre $N$ en échelles logarithmiques ; c) les pentes des deux droites, ajustées sur $N = 32$ à 256 par `np.polyfit` sur les logarithmes (une liste de 2 nombres, 1 décimale), puis lis dans b), à 64 évaluations du champ, l'erreur d'Euler (64 pas) et celle du point milieu (32 pas). Ce qu'il faut regarder : pourquoi ajuster les pentes sur les grands $N$ seulement ? À nombre d'évaluations égal, quelle méthode gagne, et de combien ?

**MB5.20 · 🔮 Le débruiteur de cinq relevés quand le bruit tend vers 0.** Un marégraphe a relevé cinq fois la hauteur de la mer, en m : $1{,}2$ ; $1{,}9$ ; $2{,}3$ ; $3{,}6$ ; $4{,}0$, de poids égaux ; un capteur mesure $y = 0{,}5\,x + b\,n$, où $x$ est l'un des cinq relevés. **Avant d'exécuter**, prédis, quand $b$ tend vers 0 : a) pour $y = 1$ (donc $\frac ya = 2$), $\mathbb{E}[x \mid y]$ tend vers : (A) 2 ; (B) $1{,}9$ ; (C) $2{,}6$, la moyenne des relevés (une lettre) ; b) pour $y = 1{,}475$ (donc $\frac ya = 2{,}95$, à égale distance de $2{,}3$ et de $3{,}6$) : (A) $2{,}95$ ; (B) $2{,}3$ ; (C) $3{,}6$ (une lettre) ; c) pour $y = 1$ et un bruit énorme, $b = 50$ : (A) $1{,}9$ ; (B) 2 ; (C) $2{,}6$ (une lettre). Puis mesure, avec `posterior_mean_mixture` (des variances nulles) : d) $\mathbb{E}[x \mid y = 1]$ pour $b = 1$, $0{,}3$, $0{,}1$, $0{,}03$ et $0{,}01$ (une liste de 5 nombres) ; e) la même chose pour $y = 1{,}475$ (une liste de 5 nombres) ; f) $\mathbb{E}[x \mid y = 1]$ pour $b = 50$ (un nombre). Ce qu'il faut regarder (après l'expérience) : à partir de quel $b$ le débruiteur rend-il presque exactement un relevé ? Pourquoi ne rend-il jamais 2, la valeur $\frac ya$ ? Qu'est-ce qu'un débruiteur optimal fabrique de nouveau à partir d'un nuage de points ?

**MB5.21 · 🔬 Le chemin droit vers une loi gaussienne.** Données $\mathcal{N}(4 ;\ 0{,}25)$ de MB5.9. Écris `field_21(s, x)`, le champ moyen exact $v(x, s)$, affine en $x$ (une fonction du temps puis du point, pour `euler_ode` et `midpoint_ode`, qui l'appellent `f(t, x)`) ; la vérification le compare au débruiteur de `posterior_mean_mixture` avec $a = 1 - s$ et $b = s$. Le notebook fournit `Z_21`, 100 000 tirages de $\mathcal{N}(0, 1)$. Transporte-les de $s = 1$ à $s = 0$ par Euler, puis par le point milieu, avec $N = 1$, 2, 4, 8, 16 et 32 pas. Relève : a) l'écart-type (`np.std`) des points obtenus, pour Euler puis pour le point milieu (deux listes de 6 nombres) ; b) l'écart-type obtenu en transportant exactement : celui de $4 + 0{,}5\,$`Z_21` (un nombre). Ce qu'il faut regarder : pourquoi la moyenne des points (`np.mean`) est-elle juste dès un seul pas, et l'écart-type pas ? Par combien l'écart à l'écart-type exact est-il divisé quand $N$ double, pour Euler, puis pour le point milieu ? Est-ce l'ordre que donne la fiche ?

**MB5.22 · 🎨 Des lois guidées sur une grille.** La loi générale est le mélange $p_u = 0{,}55\,\mathcal{N}(-1{,}8 ;\ 0{,}5) + 0{,}45\,\mathcal{N}(1{,}6 ;\ 0{,}7)$, à deux bosses, et la loi de la classe est $p_c = \mathcal{N}(1{,}6 ;\ 0{,}7)$. Sur la grille `np.linspace(-8, 8, 3201)`, écris `guided_22(xs, w, general, cls)` (par défaut, les deux lois ci-dessus), qui rend la densité normalisée de $p_c^{1+w}p_u^{-w}$ (calcule son logarithme, retire son maximum avant l'exponentielle, puis normalise par `np.trapezoid`) ; puis `draw_guided_22(ax, ws)`, qui trace dans les axes reçus $p_u$, $p_c$ et la loi guidée pour chaque $w$ de `ws`, avec une légende qui nomme chaque courbe et des noms d'axes, et rend la liste des densités guidées tracées. La vérification l'appelle avec $w = 0{,}25$, $1{,}75$ et $3{,}5$, et l'essaie sur des appels cachés (d'autres $w$, dans un autre ordre, et un autre mélange). Relève, pour $w = 0{,}25$, $1{,}75$ et $3{,}5$ : a) la moyenne de la loi guidée (une liste de 3 nombres) ; b) son écart-type (une liste de 3 nombres) ; c) pour $w = 3{,}5$ seulement, sa masse sur $x < 0$, le côté de l'autre bosse (avec `np.trapezoid` sur la grille ; un nombre). Ce qu'il faut regarder : que devient, pour $w = 3{,}5$, la masse du côté de l'autre bosse, comparée à celle de $p_c$ ? Pourquoi la moyenne s'écarte-t-elle de $1{,}6$, et de quel côté ? Pourquoi ces lois existent-elles pour tout $w \ge 0$ ?

**MB5.23 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `bridge_bad(x0, xT, Vs, VT)` doit rendre la moyenne et la variance du pont d'une marche aléatoire ; elle met le poids $\frac{V_s}{V_T}$ sur $x_0$ au lieu de $x_T$. Il l'a vérifiée au milieu d'une marche de pas égaux.
- (2) `denoiser_bad(y, a, b, weights, means, variances)` doit rendre $\mathbb{E}[x \mid y]$ pour un mélange ; elle calcule les responsabilités avec la variance $s_k^2$ du signal seule, au lieu de $a^2s_k^2 + b^2$. Il l'a vérifiée sur un mélange à une seule composante.
- (3) `euler_bad(f, x0, t0, t1, n_steps)` doit suivre la méthode d'Euler ; elle lit le champ en $t_0$ à chaque pas. Il l'a vérifiée sur $x' = -\frac x3$.

Trouve et corrige chaque erreur dans le code du collègue lui-même : les fonctions corrigées s'appellent `bridge_fixed`, `denoiser_fixed` et `euler_fixed`, avec les mêmes arguments, et n'appellent **pas** `mymath` (la vérification le contrôle), puis réponds : a) pour le phoque de MB5.3, la moyenne de la position à 11 h par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres) ; b) pour le mélange $0{,}4\,\mathcal{N}(-1 ;\ 0{,}3) + 0{,}6\,\mathcal{N}(2{,}5 ;\ 0{,}6)$ mesuré par $y = 1{,}2\,x + 0{,}9\,n$, $\mathbb{E}[x \mid y]$ pour $y = 0{,}4$ et $1{,}4$, par la fonction corrigée, puis par la fonction fautive (une liste de 4 nombres) ; c) $x' = t - x$, $x(0) = 1$, sur $[0, 2]$ en six pas, par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres). Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : d'autres ponts, des mélanges de deux composantes ou plus, des champs qui dépendent du temps, et des tableaux qu'elles ne doivent pas modifier.

**MB5.24 · 🛠️ Un test de propriété.** Écris trois fonctions qui testent une méthode d'intégration qu'on leur passe, et rendent `True` si la propriété tient, `False` sinon : `constant_is_exact_24(method)`, qui vérifie qu'avec un champ constant (plusieurs valeurs, plusieurs nombres de pas, avec $t_0 < t_N$) **chaque** point rendu est sur la droite exacte, à $10^{-9}$ près ; `affine_is_exact_24(method)`, qui vérifie de même qu'avec un champ $f(t, x) = \kappa_0 + \kappa_1t$ chaque point rendu est sur la parabole exacte ; et `error_halves_24(method)`, qui vérifie que, pour un champ qui dépend de $t$ et de $x$ dont tu connais la solution exacte, l'erreur au temps final est divisée par un nombre entre $1{,}8$ et $2{,}2$ quand le nombre de pas passe de $N$ à $2N$ (avec $N$ assez grand). La vérification lance tes trois tests sur `euler_ode` et `midpoint_ode` de la référence, puis sur des méthodes fausses cachées, une par clause de l'énoncé, que chaque test doit refuser quand sa propriété est fausse. Relève : a) les résultats de tes trois tests sur `euler_ode`, puis sur `midpoint_ode` de la référence (deux listes de 3 booléens). Ce qu'il faut regarder : pourquoi `affine_is_exact_24` refuse-t-il la méthode d'Euler, et `error_halves_24` le point milieu ? Pourquoi tester chaque point rendu, et pas seulement le dernier ?

**MB5.25 · 🏆 Défi : transporter un bruit vers une loi à deux bosses.** Le notebook fournit `MIX_25`, une loi à deux bosses (les poids, les moyennes et les variances d'un mélange de deux gaussiennes de dimension 1), `Z_25`, 20 000 tirages de $\mathcal{N}(0, 1)$, et `TARGET_25`, 200 000 tirages de `MIX_25`. a) Écris `field_25(x, s, weights, means, variances)`, le champ moyen exact $v(x, s)$ du chemin droit vers ce mélange, avec `posterior_mean_mixture` (pour $0 < s \le 1$). Puis écris `transport_25(field, z)` : depuis les points `z` (en $s = 1$), suis $x' = v(x, s)$ jusqu'en $s = 0$, en appelant `field(x, s)` **au plus huit fois** (un appel sur un tableau entier compte pour un), et rends les points atteints. Ta fonction ne connaît le mélange que par `field` ; tout NumPy et SciPy sont permis. **Critère de réussite :** avec au plus huit appels du champ pour chaque loi, la distance de Wasserstein $W_1$ (M27) entre tes points et la loi à deux bosses, divisée par l'écart-type de cette loi, est au plus $0{,}07$ pour `MIX_25`, et au plus $0{,}07$ en moyenne pour trois séries de cinq lois cachées, tirées à nouveau à chaque exécution (la moyenne des quinze rapports) ; chaque série a une loi de chacun de ces cinq types : facile ; deux bosses très étroites ; une bosse légère d'une autre largeur ; deux bosses plus écartées que le bruit n'est large ; deux bosses qui se chevauchent. Elle ne doit pas exécuter le code du module caché du défi (`solutions/challenges/mb5_25.py`) : la vérification le contrôle. Relève : b) avec `scipy.stats.wasserstein_distance` entre tes points et `TARGET_25`, la distance obtenue par un seul pas d'Euler, puis par huit pas d'Euler, puis par ta fonction (une liste de 3 nombres) ; c) le nombre d'appels de `field` que fait ta fonction (un entier). Point de départ : huit pas d'Euler ne suffisent pas ; la fiche §8 dit comment comparer deux méthodes qui ont droit au même nombre d'évaluations.
