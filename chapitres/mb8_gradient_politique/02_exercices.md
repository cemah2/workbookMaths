# MB8 · Gradient de politique — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/mb8_gradient_politique/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB8`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et du 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : $s_\theta(x) = \partial_\theta\ln p_\theta(x)$ est le score **en $\theta$** ; la loi exponentielle est donnée par son **taux** $\theta$ (densité $\theta e^{-\theta x}$ sur $[0, +\infty[$, moyenne $\frac1\theta$), la loi de Poisson par sa moyenne $\theta$. Aux §1 à §3, $f$ est la fonction dont on dérive l'espérance, $b$ une baseline et $b^\star = \frac{\mathbb{E}[fs^2]}{\mathbb{E}[s^2]}$ la baseline optimale ; au §2 (MB8.1, MB8.21), $c$ est un seuil (une durée en MB8.1), au §3 le coefficient d'une variable de contrôle $h$, au §6 le seuil de troncature des poids. Aux §4 et §5, $s$ est un état, $a$ une action ; $\mathbf{P}_\pi$, $\mathbf{r}_\pi$, $V$, $Q$, $A$ et $\mathbf{M} = (\mathbf{I} - \gamma\mathbf{P}_\pi)^{-1}$ sont ceux de la fiche §4, $z(s, a)$ un logit, $\boldsymbol\nu_{s_0} = (1 - \gamma)\,\mathbf{M}[s_0, \cdot]$ la loi d'occupation actualisée ; au §5, $\mathbf{W} = \mathbf{V}^\pi + \mathbf{e}$ sont des valeurs estimées, $\mathbf{e}$ leurs erreurs, $G^{(k)}_t$ le retour à $k$ pas et $\lambda$ le paramètre du λ-retour. Au §6, les tirages viennent de la proposition $q$, la cible est $p$, $w = \frac pq$, et la KL estimée est $\mathrm{KL}(q \,\|\, p)$. Au §7, $\beta_i$ est la force du club $i$ et $p_i = e^{\beta_i}$, $R_i$ sa cote Elo, $k$ le coefficient d'Elo, $E$ un résultat espéré. Au §8, $\pi_{\mathrm{ref}}$ est la loi actuelle, $r$ la satisfaction, $\beta$ le poids de la KL et $Z = \mathbb{E}_{\mathrm{ref}}[e^{r/\beta}]$. Les logarithmes sont népériens, sauf $\log_{10}$ (Elo).

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 à 5 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### MB8.Q1 — La fonction score : espérance nulle, information de Fisher, support qui dépend du paramètre, et dériver une espérance par le score ou par le chemin 🧠 ★ ⏱️ 5 min
*Fiche §1 et §2 · parcours C, E*

1. $X$ suit la loi normale $\mathcal{N}(\theta, 4)$ (variance 4, connue). Son score $s_\theta(x)$ ? Son information de Fisher $I(\theta)$ ?
2. Pour la loi binomiale $\mathcal{B}(10, \theta)$, $I(\theta) = \frac{10}{\theta(1 - \theta)}$. Une valeur approchée de $\mathrm{KL}(p_{0{,}5} \,\|\, p_{0{,}52})$ ?
3. La densité $p_\theta(x) = e^{-(x - \theta)}$ pour $x \ge \theta$ (0 sinon). Son score sur $[\theta, +\infty[$ ? Son espérance est-elle nulle ? Pourquoi ?
4. Un estimateur à un tirage a la variance $1{,}44$. Combien de tirages indépendants faut-il pour que leur moyenne ait une erreur type de $0{,}05$ ?
5. Vrai ou faux : $X$ suit la loi de Poisson de moyenne $\theta$, tirée par inversion, $X = F_\theta^{-1}(U)$ avec $U$ uniforme ; la dérivée par le chemin de $\mathbb{E}_\theta[X^2]$ donne $\frac{\mathrm{d}}{\mathrm{d}\theta}\mathbb{E}_\theta[X^2] = 1 + 2\theta$.

### MB8.Q2 — Variables de contrôle et baselines : ce qui garde l'espérance, ce qui réduit la variance, ce qui biaise 🧠 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. $\mathbb{V}(f) = 10$, $\mathbb{V}(h) = 4$, $\operatorname{Cov}(f, h) = 5$, et $\mathbb{E}[h]$ est connue. Le coefficient $c^\star$ de la variable de contrôle, puis la variance de $f - c^\star(h - \mathbb{E}[h])$ ?
2. Une variable de contrôle a la corrélation $-0{,}9$ avec $f$. Par quel facteur la variance est-elle multipliée ?
3. Pour une baseline constante $b$, que vaut l'espérance de $(f(X) - b)\,s_\theta(X)$ ? Pour quelle valeur de $b$ sa variance est-elle la plus petite ?
4. Sur un batch de $n = 8$ tirages, la baseline de chaque tirage est la moyenne des huit valeurs $f$, la sienne comprise. Par quel facteur l'espérance de l'estimateur est-elle multipliée ? Et avec la moyenne des sept autres valeurs ?
5. Vrai ou faux : on peut prendre pour variable de contrôle une variable dont on ne connaît pas l'espérance.

### MB8.Q3 — Le gradient de la valeur d'une politique et le λ-retour : la loi d'occupation actualisée, l'avantage d'espérance nulle, le poids de chaque retour à k pas 🧠 ★ ⏱️ 5 min
*Fiche §4 et §5 · parcours C, E*

1. En un état, $\pi = (0{,}1 ;\ 0{,}6 ;\ 0{,}3)$ et $Q = (5 ;\ 1 ;\ 2)$. $V(s)$ ? Les trois avantages ? Leur moyenne sous $\pi$ ?
2. Avec $\gamma = 0{,}6$, pour une chaîne sans fin : à combien somment les lignes de $\mathbf{M}$ ? Quel poids porte, dans $\boldsymbol\nu_{s_0}$, la position au pas 3 ?
3. Pour $\lambda = 0{,}6$ : à partir de quel $k$ les retours de plus de $k$ pas pèsent-ils ensemble moins de 10 % du λ-retour ? Et pour $\lambda = 0{,}7$ ?
4. Vrai ou faux : le logit d'un état qu'on ne visite jamais depuis $s_0$ ne change pas $V(s_0)$.
5. Vrai ou faux : si l'on amorce avec les vraies valeurs $\mathbf{V}^\pi$, le retour à $k$ pas a pour espérance $V^\pi(S_t)$ sachant $S_t$, quel que soit $k$.

### MB8.Q4 — Échantillonnage d'importance et KL estimée : support, taille effective, poids tronqués, k₁ ou k₃ 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. La cible $p$ charge l'intervalle $[0, 1]$, où la proposition $q$ est nulle. Peut-on estimer $\mathbb{E}_p[f]$ par la moyenne des $w_if(x_i)$ ? À quelle condition sur $f$ ?
2. Les poids de quatre tirages sont $(3 ;\ 1 ;\ 1 ;\ 1)$. Leur taille effective ? Et si on les multiplie tous par 10 ?
3. Vrai ou faux : tronquer les poids à $c$ ne change pas l'espérance de l'estimateur.
4. Un tirage a le poids $w = 1{,}55$. Ses $k_1$ et $k_3$ ? Lequel des deux estimateurs peut prendre des valeurs négatives ?

### MB8.Q5 — Bradley-Terry et Elo : ce que les forces identifient, quand elles existent, ce que fait une mise à jour 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. On ajoute un même nombre à toutes les forces d'un modèle de Bradley-Terry. Que deviennent les probabilités de victoire ? Que dit-on alors des forces ?
2. Trois joueurs jouent trois matchs : A bat B, B bat C et C bat A. Les forces existent-elles ? Si oui, lesquelles (centrées) ?
3. Une joueuse avait une probabilité de victoire de $0{,}64$ contre son adversaire, et elle perd. Avec $k = 20$, combien de points perd-elle ?
4. Deux joueurs ont 400 points d'écart. Quelle est la probabilité que le mieux coté gagne ?

### MB8.Q6 — Le principe de Gibbs : la loi optimale, ses limites en β, et ce que mesure β ln Z 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. $\pi_{\mathrm{ref}} = (\frac12 ;\ \frac12)$, $r = (1 ;\ 0)$ et $\beta = \frac{1}{\ln 2}$. Que vaut $\pi^\star$ ?
2. Vers quelle loi tend $\pi^\star$ quand $\beta \to 0$ ? Quand $\beta \to +\infty$ ?
3. Vrai ou faux : $\pi^\star$ peut donner une probabilité positive à une issue que $\pi_{\mathrm{ref}}$ exclut.
4. Que vaut $\beta\ln Z$ par rapport à l'objectif $F(\pi) = \mathbb{E}_\pi[r] - \beta\,\mathrm{KL}(\pi \,\|\, \pi_{\mathrm{ref}})$ ? Entre quelles valeurs se trouve-t-il ?

<a id="rappels"></a>

## 🔁 Rappels

### MB8.R1 — La jacobienne de la softmax, diag(p) − ppᵀ, lue comme la covariance d'un vecteur one-hot, et la loi de Boltzmann (M17) 🔁 ★ ⏱️ 6 min
*Fiche §4 · parcours C, E*

En un point $\mathbf{z}$, la softmax vaut $\mathbf{p} = (0{,}6 ;\ 0{,}1 ;\ 0{,}3)$.
1. La jacobienne $\big(\frac{\partial p_i}{\partial z_j}\big)$ en ce point, comme une matrice $3 \times 3$.
2. Pourquoi chaque ligne somme-t-elle à 0 ?
3. Un vecteur aléatoire $\mathbf{Y}$ vaut $(1, 0, 0)$, $(0, 1, 0)$ ou $(0, 0, 1)$ avec les probabilités $p_1$, $p_2$, $p_3$. Calcule $\mathbb{E}[\mathbf{Y}]$ et $\mathbb{E}[\mathbf{Y}\mathbf{Y}^\top]$ en fonction de $p_1$, $p_2$, $p_3$, puis la matrice de covariance de $\mathbf{Y}$. Que reconnais-tu ?
4. La loi de Boltzmann des énergies $(0 ;\ 1{,}5 ;\ 3)$ à la température 1 (4 décimales).

### MB8.R2 — Le système de Bellman d'une politique fixée, la loi d'occupation actualisée et le télescopage des erreurs TD (M26) 🔁 ★ ⏱️ 7 min
*Fiche §4 et §5 · parcours C, E*

Une chaîne à deux états : $\mathbf{P}_\pi = \begin{pmatrix} 0{,}7 & 0{,}3 \\ 0{,}2 & 0{,}8 \end{pmatrix}$, $\mathbf{r}_\pi = (8 ;\ 1)$, $\gamma = 0{,}6$.
1. Les valeurs $\mathbf{V}$ (le système de Bellman).
2. La loi d'occupation actualisée $\boldsymbol\nu_0$ depuis l'état 0 ; vérifie $V(0) = \frac{\boldsymbol\nu_0\mathbf{r}_\pi}{1 - \gamma}$.
3. Avec des valeurs estimées $\mathbf{W} = (16 ;\ 5)$, l'espérance de l'erreur TD $\delta_t = R_t + \gamma W(S_{t+1}) - W(S_t)$ sachant $S_t = 0$.
4. Écris $\sum_{k=0}^{n-1}\gamma^k\delta_{t+k}$ avec les récompenses et $W$ seulement.

### MB8.R3 — La dérivée par le chemin, son hypothèse de domination, et l'indicatrice où elle échoue (M25b) 🔁 ★ ⏱️ 6 min
*Fiche §2 · parcours C, E*

$X = \theta + U$, avec $U$ uniforme sur $[0, 1]$, et $\theta = 1{,}5$.
1. La dérivée par le chemin de $\mathbb{E}_\theta[X^2]$ ; vérifie-la en calculant $\mathbb{E}_\theta[X^2]$.
2. Quelle hypothèse justifie d'échanger la dérivée et l'espérance (M25b §7) ?
3. $P_\theta(X > 2)$ et sa dérivée en $\theta = 1{,}5$. Que donne la dérivée par le chemin de $\mathbf{1}\{X > 2\}$ ? Pourquoi ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les logarithmes, les exponentielles, les racines et les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ; une matrice, comme une liste de ses lignes : `[[1, 0], [0.5, 0.5]]`.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex MB8.1 — Une attente au téléphone de loi exponentielle de taux θ, et une pénalité au-delà de c minutes : d/dθ P(X > c) par la formule fermée, par l'estimateur score (son espérance calculée) et par le chemin X = ξ/θ ; la variance de l'estimateur score à un tirage ✏️ ★★ ⏱️ 35 min
**Objectif :** dériver une probabilité par rapport au paramètre d'une loi de trois façons, voir le chemin échouer sur une indicatrice, et chiffrer le bruit de l'estimateur score.
**Prérequis :** fiche §2 ; M02b (loi exponentielle), M25b §7 (dérivée par le chemin) · **Parcours :** C, E

Le service client d'un fournisseur d'énergie mesure l'attente $X$ (en minutes) avant qu'un conseiller décroche. On la modélise par une loi exponentielle de taux $\theta = 0{,}1$ par minute (moyenne $\frac1\theta = 10$ minutes). Au-delà de $c = 18$ minutes, le fournisseur offre un bon d'achat : on s'intéresse à $P_\theta(X > c) = \mathbb{E}_\theta[f(X)]$, avec $f(x) = \mathbf{1}\{x > c\}$, et à sa dérivée par rapport au taux $\theta$. L'estimateur score à un tirage est $g(X) = f(X)\,s_\theta(X)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X > c)$ | un nombre (4 décimales) |
| b | $\frac{\mathrm{d}}{\mathrm{d}\theta}P(X > c)$, par la formule fermée | un nombre (4 décimales) |
| c | les deux termes de $\mathbb{E}[g(X)]$ : $\frac1\theta\,\mathbb{E}[\mathbf{1}\{X > c\}]$, puis $\mathbb{E}[X\,\mathbf{1}\{X > c\}]$ | une liste de 2 nombres (4 décimales) |
| d | les dérivées par le chemin $X = \xi/\theta$ ($\xi$ exponentielle de taux 1) de $\mathbb{E}[X]$, puis de $P(X > c)$ | une liste de 2 nombres (2 décimales) |
| e | la variance de $g(X)$, à un tirage | un nombre (2 décimales) |

Dans ta copie : écris $s_\theta(x)$ ; montre que $\mathbb{E}[X\,\mathbf{1}\{X > c\}] = (c + \frac1\theta)\,e^{-\theta c}$ ; dis pourquoi d) ne donne pas b) pour la probabilité.

### Ex MB8.2 — Deux graines par godet (une loi binomiale B(2, θ)) et un prix selon le nombre de pousses : la dérivée de la recette moyenne, puis l'estimateur score sans baseline, avec b = E[f] et avec la baseline optimale, et leurs variances ✏️ ★★ ⏱️ 35 min
**Objectif :** calculer l'estimateur score d'une loi discrète et sa variance pour trois baselines, et voir que la baseline optimale n'est pas la moyenne.
**Prérequis :** fiche §3 ; M02b (loi binomiale), M02c (variance) · **Parcours :** C, E

Une pépinière sème deux graines par godet ; chacune lève avec la probabilité $\theta = 0{,}75$, indépendamment : le nombre de pousses $X$ suit la loi binomiale $\mathcal{B}(2, \theta)$. Un godet se vend $f(0) = 0$ € (on le jette), $f(1) = 3{,}50$ € et $f(2) = 5$ € (la seconde pousse est repiquée à part). On cherche la dérivée de la recette moyenne $\mathbb{E}_\theta[f(X)]$ par rapport à $\theta$, et l'on étudie l'estimateur score à un tirage $(f(X) - b)\,s_\theta(X)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les scores $s_\theta(0)$, $s_\theta(1)$, $s_\theta(2)$ | une liste de 3 nombres (2 décimales) |
| b | $\frac{\mathrm{d}}{\mathrm{d}\theta}\mathbb{E}_\theta[f(X)]$ | un nombre (2 décimales) |
| c | la variance de l'estimateur sans baseline ($b = 0$), à un tirage | un nombre (2 décimales) |
| d | la variance avec la baseline $b = \mathbb{E}[f(X)]$, à un tirage | un nombre (2 décimales) |
| e | la baseline optimale $b^\star$, puis la variance avec $b^\star$, à un tirage | une liste de 2 nombres (3 décimales) |

Dans ta copie : vérifie que $\mathbb{E}[s_\theta(X)] = 0$ et que $\mathbb{E}[f(X)\,s_\theta(X)]$ redonne b) ; compare $b^\star$ à $\mathbb{E}[f(X)]$.

### Ex MB8.3 — Un camion de crêpes entre deux emplacements, une politique softmax dans l'un d'eux : la chaîne induite, les valeurs, la loi d'occupation actualisée, les valeurs et les avantages des deux actions, puis le gradient de la valeur par rapport aux deux logits ✏️ ★★ ⏱️ 40 min
**Objectif :** dérouler sur un petit MDP la formule du gradient de la valeur : la chaîne, les valeurs, $\mathbf{M}$, les avantages, puis les dérivées par rapport aux logits.
**Prérequis :** fiche §4 ; M26 §4 et §5 (chaîne induite, système de Bellman), M17 §7 (softmax) ; MB8.R2 · **Parcours :** C, E

Un camion de crêpes passe chaque journée sur un marché (l'état 0) ou dans un parc (l'état 1). Au marché, la gérante choisit chaque jour de **rester** ou de **partir** :
- si elle reste, elle vend pour 3 (centaines d'euros) en moyenne dans la journée, et le lendemain elle est encore au marché avec la probabilité 0,86, au parc avec la probabilité 0,14 (le placier donne parfois sa place à un autre camion) ;
- si elle part, elle ne vend rien ce jour-là (0), et elle est au parc le lendemain.

Au parc, elle n'a pas le choix (la mairie fixe la rotation) : elle vend pour 4 en moyenne, et le lendemain elle retourne au marché avec la probabilité 0,3. Au marché, elle suit une politique softmax de logits $z(\text{marché}, \text{rester}) = \ln 3$ et $z(\text{marché}, \text{partir}) = 0$. Les journées sont actualisées par $\gamma = 0{,}7$.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice $\mathbf{P}_\pi$ (lignes et colonnes : marché, parc) | une matrice $2 \times 2$ (3 décimales) |
| b | les valeurs $V(\text{marché})$, $V(\text{parc})$ | une liste de 2 nombres (2 décimales) |
| c | la colonne du marché de $\mathbf{M}$ : $\mathbf{M}[\text{marché}, \text{marché}]$, puis $\mathbf{M}[\text{parc}, \text{marché}]$ | une liste de 2 nombres (3 décimales) |
| d | $Q(\text{marché}, \text{rester})$, $Q(\text{marché}, \text{partir})$, puis les avantages $A(\text{marché}, \text{rester})$, $A(\text{marché}, \text{partir})$ | une liste de 4 nombres (4 décimales) |
| e | $\frac{\partial V(\text{marché})}{\partial z(\text{marché}, \text{rester})}$, $\frac{\partial V(\text{marché})}{\partial z(\text{marché}, \text{partir})}$, $\frac{\partial V(\text{parc})}{\partial z(\text{marché}, \text{rester})}$, $\frac{\partial V(\text{parc})}{\partial z(\text{marché}, \text{partir})}$ | une liste de 4 nombres (4 décimales) |

Pour d) et e), repars des valeurs non arrondies de b) et c). Dans ta copie : calcule la loi d'occupation actualisée $\boldsymbol\nu_{\text{marché}}$ ; vérifie que $\sum_a\pi(a \mid \text{marché})\,A(\text{marché}, a) = 0$ ; dis pourquoi un logit du marché change $V(\text{parc})$.

### Ex MB8.4 — L'état d'une route (bonne, usée, en travaux) et des valeurs estimées fausses : le biais des retours à 1 et 2 pas, les poids (1 − λ)λ^{k−1} d'un λ-retour, et son biais quand l'erreur est la même partout ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer le biais qu'un retour à $k$ pas hérite de valeurs estimées fausses, puis celui d'un λ-retour.
**Prérequis :** fiche §5 ; M26 §1 (loi à $k$ pas d'une chaîne), R5 (série géométrique) · **Parcours :** C, E

Chaque mois, un tronçon de route à péage est **bon**, **usé** ou **en travaux**. Sous la politique d'entretien de la société concessionnaire, fixée, son état suit la chaîne
$$\mathbf{P}_\pi = \begin{pmatrix} 0{,}85 & 0{,}15 & 0 \\ 0 & 0{,}7 & 0{,}3 \\ 0{,}85 & 0 & 0{,}15 \end{pmatrix} \quad (\text{lignes et colonnes : bon, usé, en travaux}),$$
et les mois sont actualisés par $\gamma = 0{,}6$. Un bureau d'études a estimé la valeur de chaque état (la recette de péage actualisée à venir, en centaines de milliers d'euros) ; ses estimations $\mathbf{W} = \mathbf{V}^\pi + \mathbf{e}$ sont fausses de $\mathbf{e} = (3 ;\ 0 ;\ 2)$ : trop hautes de 3 pour un tronçon bon, justes pour un tronçon usé, trop hautes de 2 pour un tronçon en travaux. On amorce avec $\mathbf{W}$ des retours à $k$ pas, et un λ-retour avec $\lambda = 0{,}7$. Le biais d'un retour à $k$ pas $G_t^{(k)}$ (fiche §5) depuis l'état $s$ est $\mathbb{E}\big[G_t^{(k)} \mid S_t = s\big] - V^\pi(s)$, et de même pour le λ-retour $G_t^\lambda$ ; les recettes du mois n'y interviennent pas.

| | Question | Réponse attendue |
|---|---|---|
| a | le biais du retour à 1 pas, partant de chaque état (bon, usé, en travaux) | une liste de 3 nombres (3 décimales) |
| b | le biais du retour à 2 pas, partant de chaque état | une liste de 3 nombres (4 décimales) |
| c | le poids du retour à 5 pas dans le λ-retour, puis le plus petit $k$ tel que les retours de plus de $k$ pas pèsent ensemble moins de 5 % | une liste de 2 nombres : le poids (4 décimales), puis un entier |
| d | le biais du λ-retour si l'erreur valait 2 dans les trois états, $\mathbf{e} = (2 ;\ 2 ;\ 2)$ | un nombre (4 décimales) |

Dans ta copie : dis pourquoi le biais depuis un tronçon usé n'est pas nul, alors que son estimation est juste ; écris le biais de d) comme une série en $k$, puis somme-la.

### Ex MB8.5 — Un panel en ligne dont les classes d'âge ne suivent pas le recensement : les poids p/q, la dépense moyenne repondérée, la taille effective de Kish d'un petit échantillon, des poids tronqués (le biais), puis KL(q ‖ p) exacte et ses estimateurs k₁ et k₃ classe par classe ✏️ ★★ ⏱️ 40 min
**Objectif :** repondérer des tirages d'une loi pour estimer une moyenne sous une autre, mesurer ce que la repondération coûte en tirages, chiffrer le biais d'une troncature, et estimer une KL par tirages.
**Prérequis :** fiche §6 ; M06 (divergence KL), M20 §5 (Horvitz-Thompson) · **Parcours :** C, E

Un institut interroge un panel en ligne sur la dépense mensuelle en livres. Ses panélistes ne suivent pas la population (le recensement) :

| classe d'âge | 18–34 ans | 35–59 ans | 60 ans et plus |
|---|---|---|---|
| part dans le panel, $q$ | 0,50 | 0,25 | 0,25 |
| part dans la population, $p$ | 0,26 | 0,41 | 0,33 |
| dépense de la classe, $f$ (€ par mois) | 36 | 50 | 44 |

On suppose que la dépense ne dépend que de la classe d'âge. Un panéliste tiré au hasard dans le panel est un tirage de $q$ (sa classe) ; on veut des moyennes sous $p$. Un petit échantillon compte six panélistes : trois de 18–34 ans, un de 35–59 ans et deux de 60 ans et plus.

| | Question | Réponse attendue |
|---|---|---|
| a | les poids $w = \frac pq$ des trois classes | une liste de 3 nombres (2 décimales) |
| b | la dépense moyenne du panel brut, $\mathbb{E}_q[f]$ (sous $q$, pas sur les six panélistes), puis la dépense moyenne repondérée $\mathbb{E}_q[wf]$ | une liste de 2 nombres (2 décimales) |
| c | la taille effective de Kish des six panélistes | un nombre (2 décimales) |
| d | l'espérance repondérée avec les poids tronqués à $c = 1{,}6$, $\mathbb{E}_q[\min(w, c)\,f]$, puis son biais | une liste de 2 nombres (2 décimales) |
| e | $\mathrm{KL}(q \,\Vert\, p)$ | un nombre (5 décimales) |
| f | $k_1$ pour un panéliste de chaque classe | une liste de 3 nombres (4 décimales) |
| g | $k_3$ pour un panéliste de chaque classe | une liste de 3 nombres (4 décimales) |

Dans ta copie : vérifie que $\mathbb{E}_q[w] = 1$ ; dis pourquoi $k_1$ est négatif pour deux classes ; vérifie que les moyennes de $k_1$ et de $k_3$ sous $q$ redonnent e).

### Ex MB8.6 — Un tournoi de babyfoot entre trois clubs : deux clubs seuls (la différence de forces en forme fermée), puis vérifier les équations du maximum de vraisemblance pour des forces proposées, la probabilité qu'un club batte un autre, une mise à jour Elo, et un club invaincu ✏️ ★★ ⏱️ 35 min
**Objectif :** ajuster un modèle de Bradley-Terry à la main, lire ses équations comme « victoires observées = victoires attendues », passer à la cote Elo, et voir quand les forces n'existent pas.
**Prérequis :** fiche §7 ; M04 (maximum de vraisemblance), M13a (sigmoïde) · **Parcours :** C, E

Trois clubs de babyfoot, A, B et C, se rencontrent pendant une saison. Le tableau donne le nombre de victoires du club de la ligne contre celui de la colonne :

| | A | B | C |
|---|---|---|---|
| A | — | 2 | 10 |
| B | 5 | — | 1 |
| C | 0 | 3 | — |

Dans le modèle de Bradley-Terry, le club $i$ bat le club $j$ avec la probabilité $\sigma(\beta_i - \beta_j) = \frac{p_i}{p_i + p_j}$, où $p_i = e^{\beta_i}$. D'abord, A et B seuls : on oublie C et les matchs contre lui. Puis tout le tournoi : on propose $p_A = 4$, $p_B = 3$, $p_C = 1$ (à un facteur commun près). Enfin, la cote Elo (base 10, échelle 400) : $R_A - R_C = \frac{400}{\ln 10}(\beta_A - \beta_C)$, et après un match, le club $i$ gagne $k\,(S - E)$ points, avec $k = 32$, $S = 1$ s'il gagne, 0 s'il perd, et $E$ sa probabilité de victoire.

| | Question | Réponse attendue |
|---|---|---|
| a | A et B seuls : la différence $\beta_A - \beta_B$ qui maximise la vraisemblance | un nombre (4 décimales) |
| b | avec les forces proposées : les victoires attendues de A contre B, de A contre C, puis de B contre C | une liste de 3 nombres (2 décimales) |
| c | les forces centrées $\beta_A$, $\beta_B$, $\beta_C$ ($\beta_A + \beta_B + \beta_C = 0$) | une liste de 3 nombres (4 décimales) |
| d | la probabilité que C batte A lors d'un prochain match | un nombre (4 décimales) |
| e | l'écart des cotes Elo $R_A - R_C$, puis les points que gagne C s'il bat A | une liste de 2 nombres (1 décimale) |

Dans ta copie : avec b), vérifie que chaque club a autant de victoires attendues que de victoires observées ; un quatrième club, D, joue deux matchs contre A et deux contre C, et les gagne tous : montre, avec l'équation du maximum de vraisemblance de D, que les forces n'existent plus.

### Ex MB8.7 — Trois plats à la cantine : la loi de service qui maximise la satisfaction moyenne moins β fois la KL à la loi actuelle, pour deux valeurs de β, sa valeur β ln Z, comparée à la loi actuelle et au meilleur plat seul ✏️ ★★ ⏱️ 30 min
**Objectif :** appliquer le principe de Gibbs : la loi optimale, sa valeur, et ce qu'elle gagne sur deux lois simples.
**Prérequis :** fiche §8 ; M06 (divergence KL), M05a §8 (log-sum-exp) · **Parcours :** C, E

Une cantine scolaire sert chaque midi un plat parmi trois : gratin, couscous ou lasagnes, aujourd'hui dans les proportions $\pi_{\mathrm{ref}} = (0{,}45 ;\ 0{,}40 ;\ 0{,}15)$. Une enquête donne leur satisfaction moyenne $r = (2 ;\ 4 ;\ 5)$ (sur 5). Changer brutalement les menus a un coût (les fournisseurs, les habitudes) : le gestionnaire cherche la loi de service $\pi$ qui maximise $F(\pi) = \mathbb{E}_\pi[r] - \beta\,\mathrm{KL}(\pi \,\|\, \pi_{\mathrm{ref}})$, pour $\beta = 1$, puis pour $\beta = 3$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\beta = 1$ : la loi $\pi^\star$ (gratin, couscous, lasagnes) | une liste de 3 nombres (4 décimales) |
| b | $\beta = 1$ : la valeur $\beta\ln Z$ | un nombre (4 décimales) |
| c | $\beta = 1$ : $F(\pi_{\mathrm{ref}})$, puis $F$ pour la loi qui ne sert que le plat le mieux noté | une liste de 2 nombres (4 décimales) |
| d | $\beta = 3$ : la loi $\pi^\star$, puis la valeur $\beta\ln Z$ | une liste de 4 nombres (4 décimales) |

Dans ta copie : compare b) aux deux valeurs de c) ; dis comment $\pi^\star$ change quand $\beta$ passe de 1 à 3, et vers quelle loi il tend quand $\beta$ grandit encore.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex MB8.8 — Les deux identités du score, E[s_θ(X)] = 0 et Var(s_θ) = −E[∂²_θ ln p_θ(X)], pour une famille à densité dont le support ne dépend pas de θ ; leur application aux lois de Poisson et exponentielle ; puis la loi uniforme sur [0, θ], où elles tombent ∂ ★★ ⏱️ 35 min
**Objectif :** démontrer les deux identités du score, les appliquer, et voir pourquoi un support qui bouge avec $\theta$ les fait tomber.
**Prérequis :** fiche §1 ; M02b (lois de Poisson, exponentielle et uniforme), M25b §7 (dériver sous l'intégrale) · **Parcours :** C, E

Une famille de densités $p_\theta$ sur $\mathbb{R}$, de paramètre réel $\theta$ dans un intervalle ouvert, est strictement positive sur un ensemble $S$ qui ne dépend pas de $\theta$, et nulle ailleurs ; $\theta \mapsto p_\theta(x)$ est deux fois dérivable pour tout $x \in S$, et l'on admet qu'on peut dériver deux fois $\int_Sp_\theta(x)\,\mathrm{d}x$ sous le signe intégrale (une hypothèse de domination).
1. En dérivant $\int_Sp_\theta(x)\,\mathrm{d}x = 1$, montre que $\mathbb{E}_\theta[s_\theta(X)] = 0$.
2. Écris $\partial^2_\theta\ln p_\theta$ avec $p_\theta$, $\partial_\theta p_\theta$ et $\partial^2_\theta p_\theta$. En dérivant une seconde fois, montre que $\mathbb{V}(s_\theta(X)) = -\mathbb{E}_\theta[\partial^2_\theta\ln p_\theta(X)]$.
3. Applique les deux identités à la loi de Poisson de moyenne $\theta$ (une somme remplace l'intégrale) : son score, et son information de Fisher par les deux formules ; puis donne le score de la loi exponentielle de taux $\theta$, et son information de Fisher par la formule de ton choix.
4. La loi uniforme sur $[0, \theta]$, $\theta > 0$ : son score sur $[0, \theta[$, puis $\mathbb{E}_\theta[s_\theta(X)]$, $\mathbb{V}(s_\theta(X))$ et $-\mathbb{E}_\theta[\partial^2_\theta\ln p_\theta(X)]$. Quelle étape de 1 tombe, et pourquoi ?

### Ex MB8.9 — La baseline optimale b* = E[f s²]/E[s²] d'un estimateur score ; sur n tirages, la moyenne des autres est une baseline sans biais, et la moyenne du groupe multiplie l'estimateur par (n − 1)/n ∂ ★★ ⏱️ 30 min
**Objectif :** démontrer la baseline optimale, puis séparer exactement une baseline sans biais d'une baseline qui biaise.
**Prérequis :** fiche §3 ; M02c (variance, covariance, estimateur sans biais) · **Parcours :** C

On estime $D = \frac{\mathrm{d}}{\mathrm{d}\theta}\mathbb{E}_\theta[f(X)] = \mathbb{E}[f(X)\,s(X)]$, où $s = s_\theta$ ; on suppose $\mathbb{E}[s(X)] = 0$, $0 < \mathbb{E}[s(X)^2] < +\infty$, $\mathbb{E}[f(X)^2s(X)^2] < +\infty$ et $\mathbb{E}[\lvert f(X)\rvert] < +\infty$.
1. Pour une constante $b$, montre que $(f(X) - b)\,s(X)$ est sans biais, et que sa variance est un trinôme du second degré en $b$. Déduis-en $b^\star$ et la variance minimale.
2. Donne une condition sous laquelle $b^\star = \mathbb{E}[f(X)]$, puis dis pourquoi ✏️ MB8.2 ne la vérifie pas.
3. On tire $x_1, \ldots, x_n$ indépendants ($n \ge 2$), et $b_i = \frac{1}{n - 1}\sum_{j \ne i}f(x_j)$. Montre que $\frac1n\sum_i\big(f(x_i) - b_i\big)\,s(x_i)$ est sans biais.
4. Avec la moyenne du groupe $\bar f = \frac1n\sum_jf(x_j)$, montre que $f(x_i) - \bar f = \frac{n - 1}{n}\big(f(x_i) - b_i\big)$ pour tout $i$. Déduis-en l'espérance de $\frac1n\sum_i\big(f(x_i) - \bar f\big)\,s(x_i)$. D'où vient le biais ?

### Ex MB8.10 — Le gradient de la valeur d'une politique sous forme matricielle : dériver V = r_π + γP_πV, faire apparaître la loi d'occupation actualisée et la valeur des actions, puis remplacer Q^π par l'avantage ∂ ★★★ ⏱️ 40 min
**Objectif :** démontrer le théorème de la fiche §4 en dérivant le système de Bellman, puis sa forme score avec l'avantage.
**Prérequis :** fiche §4 ; M18 §7 (règle du produit), M26 §5 (système de Bellman) ; MB8.R1 · **Parcours :** C, E

Un MDP a $m$ états et $K$ actions, $\gamma < 1$, et une politique softmax tabulaire a les logits $z(s, a)$ ; $\mathbf{P}_\pi$, $\mathbf{r}_\pi$, $V$, $Q$, $A$ et $\mathbf{M}$ sont ceux de la fiche §4. On admet que $\mathbf{V}$ est une fonction dérivable des logits.
1. La matrice $\mathbf{I} - \gamma\mathbf{P}_\pi$ est inversible (M26 §5). Dérive $(\mathbf{I} - \gamma\mathbf{P}_\pi)\,\mathbf{V} = \mathbf{r}_\pi$ par rapport à un paramètre réel de la politique, et montre que $\partial\mathbf{V} = \mathbf{M}\big(\partial\mathbf{r}_\pi + \gamma\,(\partial\mathbf{P}_\pi)\,\mathbf{V}\big)$.
2. Calcule $\frac{\partial\pi(b \mid s')}{\partial z(s, a)}$ pour tous les états $s'$ et toutes les actions $b$.
3. Déduis-en que le vecteur $\partial\mathbf{r}_\pi + \gamma\,(\partial\mathbf{P}_\pi)\,\mathbf{V}$ (la dérivée étant prise par rapport à $z(s, a)$) n'a qu'une coordonnée non nulle, celle de $s$, et qu'elle vaut $\pi(a \mid s)\,A(s, a)$.
4. Conclus : $\frac{\partial V(s_0)}{\partial z(s, a)} = \mathbf{M}[s_0, s]\,\pi(a \mid s)\,A(s, a) = \frac{\nu_{s_0}(s)}{1 - \gamma}\,\pi(a \mid s)\,A(s, a)$, et vérifie que la somme de ces dérivées sur les actions $a$ est nulle.
5. Pour une politique qui dépend d'un paramètre réel $\theta$ de façon quelconque (dérivable, de probabilités positives), écris le résultat de 1 sous la forme $\partial_\theta V(s_0) = \sum_s\mathbf{M}[s_0, s]\sum_a\pi(a \mid s)\,\partial_\theta\ln\pi(a \mid s)\,Q(s, a)$, puis montre qu'on peut y remplacer $Q(s, a)$ par $A(s, a)$.

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB8.11 — Pont : la « loss de substitution » −(1/n)Σ(f(x_i) − b) ln p_θ(x_i), dont la dérivée, les f(x_i) et b tenus fixes, est moins l'estimateur score : sur le taux d'une loi de Poisson, puis ce que changent des f standardisés dans le batch 🔗 ★ ⏱️ 20 min
**Objectif :** voir qu'en dérivant une loss bien choisie, on obtient l'estimateur score, et lire ce que changent la baseline et la standardisation.
**Prérequis :** fiche §2 et §3 ; M02b (loi de Poisson), M04 (log-vraisemblance) · **Parcours :** C, E

Une laverie automatique a deux séchoirs. Il y arrive $X$ clients par quart d'heure, de loi de Poisson de moyenne $\theta = 2{,}5$, et $f(x) = \max(0, x - 2)$ d'entre eux attendent un séchoir. Sur un batch de huit quarts d'heure, $\mathbf{x} = (3, 1, 4, 2, 5, 1, 3, 4)$. Un logiciel qui ne sait dériver que des fonctions de $\theta$ minimise la **loss de substitution** $L(\theta) = -\frac1n\sum_i\big(f(x_i) - b\big)\ln p_\theta(x_i)$, où les $f(x_i)$ et $b$ sont tenus pour des constantes.

| | Question | Réponse attendue |
|---|---|---|
| a | les huit scores $s_\theta(x_i)$ en $\theta = 2{,}5$ | une liste de 8 nombres (2 décimales) |
| b | $\frac{\mathrm{d}L}{\mathrm{d}\theta}$ en $\theta = 2{,}5$, avec $b = 1$ | un nombre (4 décimales) |
| c | la même dérivée, avec $b = 0$ | un nombre (4 décimales) |

Dans ta copie : montre que $-\frac{\mathrm{d}L}{\mathrm{d}\theta}$ est l'estimateur score de $\frac{\mathrm{d}}{\mathrm{d}\theta}\mathbb{E}_\theta[f(X)]$ ; dis pourquoi b) et c) diffèrent sur ce batch, alors que les deux estimateurs ont la même espérance ; si l'on remplaçait les $f(x_i)$ par leurs valeurs standardisées dans le batch (centrées sur leur moyenne, puis divisées par leur écart-type), dis, sans calcul, ce que fait le centrage, puis ce que fait la division à l'espérance de l'estimateur.

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB8.12 — Expliquer avec un club d'échecs pourquoi une cote Elo ne dit que des écarts de niveau, et pourquoi battre plus fort que soi rapporte plus de points 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule ce que mesure une cote Elo et comment elle se met à jour.
**Prérequis :** fiche §7 · **Parcours :** C, E

Une nouvelle adhérente de ton club d'échecs vient de recevoir sa première cote. Elle demande ce que veut dire ce nombre, si un club où « tout le monde aurait 300 points de plus » serait plus fort, et pourquoi elle a gagné beaucoup de points en battant la meilleure joueuse du club, mais très peu en battant un débutant.

Réponds-lui en 5 à 8 phrases, sans formule ni calcul : ce que prédit l'écart entre deux cotes ; pourquoi ajouter le même nombre à toutes les cotes ne changerait aucune prédiction ; ce qu'on compare après une partie ; pourquoi battre une joueuse plus forte rapporte plus ; et ce que perd la perdante.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### MB8.E1 — « Comment dériver la probabilité d'un événement par rapport au paramètre d'une loi quand on ne peut pas dériver à travers les tirages, et comment rendre l'estimation moins bruitée ? » 💼 ★ ⏱️ 10 min
*Fiche §2 et §3 · parcours C, E*

« Comment dériver la probabilité d'un événement par rapport au paramètre d'une loi quand on ne peut pas dériver à travers les tirages, et comment rendre l'estimation moins bruitée ? »

Ta réponse doit dire pourquoi la dérivée à travers les tirages échoue ici ; donner l'identité du score et ce qu'elle suppose ; dire comment on l'estime, et pourquoi c'est bruité ; puis donner deux façons de réduire la variance sans biais, et un piège.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/mb8_gradient_politique/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir.**

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| MB8.13 | L'estimateur score d'une dérivée sur un échantillon, avec une baseline constante ou la moyenne des autres tirages, et son erreur type · `score_function_gradient` | 🔨 | ★ | 25 | C, E |
| MB8.14 | Le gradient exact de la valeur d'une politique softmax tabulaire, par le système de Bellman · `policy_gradient_exact` | 🔨 | ★★ | 35 | C, E |
| MB8.15 | Des poids d'importance calculés en log, auto-normalisés ou tronqués, et la taille effective de l'échantillon · `importance_weights` | 🔨 | ★★ | 25 | C, E |
| MB8.16 | Les forces d'un modèle de Bradley-Terry par maximum de vraisemblance (l'algorithme de Zermelo), centrées, et le refus d'un tournoi où elles n'existent pas · `bradley_terry_fit` | 🔨 | ★★ | 35 | C, E |
| MB8.17 | Prédire l'ordre des écarts-types de l'estimateur score d'une même dérivée, sans baseline, avec la moyenne des autres tirages et avec la baseline optimale, puis les mesurer | 🔮 | ★ | 20 | C, E |
| MB8.18 | Un événement rare, P(Z > 4) pour Z normale centrée réduite : Monte-Carlo naïf contre l'échantillonnage d'importance sous N(4, 1), la taille effective, puis des poids tronqués à c : le biais et la variance selon c | 🔬 | ★★ | 30 | C |
| MB8.19 | Chasse à l'erreur : le score d'une loi exponentielle écrit pour la moyenne au lieu du taux, des poids d'importance inversés (q/p), une baseline qui contient le tirage lui-même, des forces de deux tournois sans joueur commun comparées sur une même échelle | 🐛 | ★ | 25 | C, E |
| MB8.20 | Un test de propriété pour le gradient exact : sur des MDP tirés au hasard, comparé à des différences finies centrées, et de somme nulle sur les actions de chaque état | 🛠️ | ★ | 25 | C |
| MB8.21 | Défi : estimer, avec un budget de tirages, la dérivée d'une probabilité de dépassement par rapport au paramètre d'une loi, assez précisément neuf fois sur dix (score, baseline, variable de contrôle) | 🏆 | ★★★ | 40 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les quatre 🔨 complètent ta copie `mon_travail/mymath/policy_gradient.py` (**mymath :** `policy_gradient.py`), dont la docstring du module dit ce qui est permis : NumPy et le module `math` ; de `np.linalg`, seulement `solve` et `matrix_rank` (dans `policy_gradient_exact`) ; ni SciPy (`scipy.optimize`, `scipy.special`…), ni scikit-learn : les tests comparent tes résultats à des sommes exactes, à des différences finies de valeurs calculées par `np.linalg.solve`, à `scipy.optimize.minimize` et à scikit-learn ; l'import relatif de ta fonction de M26 est permis (`from .markov import bellman_linear_solve`) ; rien n'y tire au hasard ; ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de sa fonction dans `tests/test_mb8_policy_gradient.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.policy_gradient.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier sont recopiées dans une cellule du notebook.

**MB8.13 · 🔨 `score_function_gradient(f_values, scores, baseline=0.0)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments (au moins deux valeurs finies ; des scores à 1 ou 2 dimensions, avec une ligne par valeur ; une baseline qui est un nombre fini ou `"leave-one-out"`, pas un booléen) ; puis les termes $g_i = (f_i - b_i)\,s_i$, leur moyenne, et leur écart-type (`ddof=1`) divisé par $\sqrt n$. Lance le groupe de tests. Ensuite, le notebook tire 2 000 attentes au téléphone de ✏️ MB8.1 (taux $0{,}1$ par minute, seuil 18 minutes ; graine fixée) et calcule les $f(x_i)$ et les scores : a) l'estimation sans baseline et son erreur type (une liste de 2 nombres) ; b) l'estimation avec la moyenne des autres tirages et son erreur type (une liste de 2 nombres) ; c) le rapport de l'estimation avec la moyenne du groupe, `baseline=float(np.mean(f))`, à celle de b) (un nombre). Ce qu'il faut regarder : la dérivée exacte (ta réponse à MB8.1 b) est-elle à moins de deux erreurs types de a) ? de b) ? Pourquoi l'erreur type de b) est-elle plus petite ? Pourquoi le rapport c) ne dépend-il pas du tirage ?

**MB8.14 · 🔨 `policy_gradient_exact(P, r, logits, gamma)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments ; $\pi$, la softmax de chaque ligne des logits (retranche d'abord le maximum de la ligne) ; $\mathbf{P}_\pi$ et $\mathbf{r}_\pi$ ; $\mathbf{M}$ par `np.linalg.solve` ; $\mathbf{V}$, $Q$, puis la formule de la fiche §4 pour tous les $(s_0, s, a)$ d'un coup ; refuse $\gamma = 1$ quand $\mathbf{I} - \mathbf{P}_\pi$ est singulière. Lance le groupe de tests. Ensuite : a) le camion de crêpes de MB8.3, écrit comme un MDP à deux actions (au parc, les deux actions font la même chose) : $V(\text{marché})$, $V(\text{parc})$, puis les dérivées de $V(\text{marché})$ et de $V(\text{parc})$ par rapport aux deux logits du marché (une liste de 6 nombres, à comparer à ta copie) ; b) le notebook fournit `P_14`, `R_14` et `LOGITS_14`, un MDP à trois états et deux actions, avec $\gamma = 0{,}6$ : les dérivées de $V(0)$ par rapport aux six logits, état par état (une liste de 6 nombres) ; c) celles de $V(2)$ (une liste de 6 nombres). Ce qu'il faut regarder : pourquoi, en b), les dérivées par rapport aux logits de l'état 2 sont-elles nulles, et pas en c) ? Pourquoi les deux dérivées d'un même état ont-elles une somme nulle ? Pourquoi, en a), les logits du parc ne comptent-ils pas ?

**MB8.15 · 🔨 `importance_weights(log_target, log_proposal, self_normalize=False, max_weight=None)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments ; les différences $d_i = \ln p(x_i) - \ln q(x_i)$, ramenées à $\ln c$ au plus avec `max_weight` $= c$ ; la taille effective à partir de $e^{d_i - \max d}$ ; puis les poids $e^{d_i}$, ou divisés par leur somme. Lance le groupe de tests. Ensuite : a) les six panélistes de MB8.5 ($\ln p$ et $\ln q$ de leurs classes) : le plus grand poids auto-normalisé, puis la taille effective (une liste de 2 nombres, à comparer à ta copie) ; b) le notebook fournit `LOG_P_15` et `LOG_Q_15`, les log-densités de cinq tirages d'une proposition en dimension 900, de l'ordre de $-1\,300$ : calcule d'abord `np.exp(LOG_P_15) / np.exp(LOG_Q_15)` et regarde ce que rend NumPy ; puis, avec `self_normalize=True`, le plus grand poids normalisé et la taille effective (une liste de 2 nombres). Ce qu'il faut regarder : pourquoi le quotient direct ne donne-t-il rien d'utilisable ? Pourquoi les poids de b) sont-ils pourtant bien définis ? Que dit la taille effective trouvée, pour cinq tirages ?

**MB8.16 · 🔨 `bradley_terry_fit(wins, tol=1e-10, max_iter=10_000)`.** Écris la fonction, en suivant sa docstring : contrôle les arguments ; la forte connexité (la matrice booléenne « $i$ atteint $j$ » et ses produits par elle-même, M16) ; puis les balayages de Zermelo sur $p = e^\beta$, centrés à chaque balayage, jusqu'à ce que le plus grand changement de $\beta$ passe sous `tol`. Lance le groupe de tests. Ensuite : a) le tournoi de MB8.6 (une liste de 3 nombres, à comparer à ta copie) ; b) le notebook fournit `WINS_16`, une saison de six clubs, qui n'ont pas tous joué le même nombre de matchs : les six forces, puis la probabilité que le club 0 batte le club 5 (une liste de 7 nombres) ; c) dans une copie de `WINS_16`, mets à 0 toutes les défaites du club 1 (sa colonne) : que fait ta fonction ? (la vérification attend une `ValueError`). Ce qu'il faut regarder : la probabilité que le club 0 batte le club 5 vaut-elle la part de ses victoires contre lui, 6 sur 7 ? Pourquoi le modèle ne recopie-t-il pas cette part ?

**MB8.17 · 🔮 Trois écarts-types.** $X$ suit une loi de Poisson de moyenne $\theta = 3{,}5$ ; on estime $\frac{\mathrm{d}}{\mathrm{d}\theta}P_\theta(X \ge 5)$ par l'estimateur score sur $n = 40$ tirages, de trois façons : sans baseline, avec la moyenne des autres tirages, et avec la baseline optimale $b^\star$, que le notebook calcule par des sommes exactes sur la loi. On répète l'estimation 2 000 fois. **Avant d'exécuter**, prédis (une lettre chacune) : a) l'ordre des trois écarts-types : (A) ils sont égaux, puisque les trois estimations ont la même espérance ; (B) sans baseline < moyenne des autres < baseline optimale ; (C) sans baseline > moyenne des autres > baseline optimale ; b) le rapport de l'écart-type sans baseline à celui avec $b^\star$ : (A) entre 1 et $1{,}5$ ; (B) entre $1{,}5$ et $2{,}5$ ; (C) plus de $2{,}5$. Puis mesure avec `score_function_gradient` : c) les trois écarts-types des 2 000 estimations, dans l'ordre de a) (une liste de 3 nombres). Ce qu'il faut regarder (après l'expérience) : les trois moyennes des estimations sont-elles proches de la même valeur ? $b^\star$ est-il proche de $P_\theta(X \ge 5)$ ? Pourquoi la moyenne des autres tirages, proche de $\mathbb{E}[f]$, ne fait-elle pas aussi bien que $b^\star$ ?

**MB8.18 · 🔬 Un événement rare.** $Z$ suit la loi normale centrée réduite, et l'on estime $P(Z > 4)$, connue par ailleurs (`scipy.stats.norm.sf(4)`). a) Monte-Carlo naïf sur 100 000 tirages (le notebook fixe la graine) : l'estimation, puis le nombre de tirages au-delà de 4 (une liste de 2 nombres) ; b) échantillonnage d'importance sous la proposition $q = \mathcal{N}(4, 1)$, avec 10 000 tirages et `importance_weights` (les log-densités par `scipy.stats.norm.logpdf`) : l'estimation divisée par la vraie valeur, l'erreur type relative (l'erreur type divisée par la vraie valeur), puis la taille effective des 10 000 poids (une liste de 3 nombres) ; c) des poids tronqués à $c$, pour $c = 10^{-4}$, $2 \cdot 10^{-4}$, $3{,}35 \cdot 10^{-4}$ et 1 : sur 400 répétitions de 10 000 tirages, le biais relatif et l'écart-type relatif de l'estimation pour chaque $c$, en deux courbes en fonction de $c$ ; relève les biais relatifs pour $c = 10^{-4}$ et $2 \cdot 10^{-4}$ (une liste de 2 nombres). Ce qu'il faut regarder : pourquoi le Monte-Carlo naïf ne donne-t-il presque rien ? Que vaut le poids $\frac pq$ d'un tirage $z$, et quel est le plus grand poids d'un tirage au-delà de 4 ? Pourquoi la taille effective de b) est-elle si petite, alors que l'estimation est précise ? À partir de quel $c$ la troncature ne biaise-t-elle plus ?

**MB8.19 · 🐛 Chasse à l'erreur.** Un collègue a écrit quatre fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `score_exp_bad(x, theta)` doit rendre le score $s_\theta(x)$ de la loi exponentielle de taux $\theta$ en chaque point de `x`. Sur 100 000 tirages au taux $0{,}4$, la moyenne des scores est loin de 0. Il l'a vérifiée au taux 1, où la moyenne des scores est proche de 0.
- (2) `weights_bad(log_p, log_q)` doit rendre les poids d'importance de tirages de $q$. Avec la cible $\mathcal{N}(0{,}8 ;\ 1)$ et la proposition $\mathcal{N}(0 ;\ 1{,}5^2)$, la moyenne des $w_ix_i$, qui devrait estimer $\mathbb{E}_p[X] = 0{,}8$, est énorme et négative. Il l'a vérifiée avec la même loi pour $p$ et pour $q$.
- (3) `estimate_bad(f, s)` doit rendre l'estimateur score d'un batch, avec pour chaque tirage une baseline calculée sur le batch, et rester sans biais. Sur 20 000 batches de 4 tirages (loi de Poisson de moyenne $1{,}5$, $f(x) = \mathbf{1}\{x \ge 2\}$), la moyenne des estimations reste nettement sous la dérivée exacte, $1{,}5\,e^{-1{,}5}$. Il l'a vérifiée sur un seul batch de 10 000 tirages.
- (4) `strongest_bad(wins_a, wins_b)` doit dire quel est le club le plus fort de deux tournois réunis, A (clubs A0, A1, A2) et B (clubs B0, B1, B2), ou lever une `ValueError` quand les données ne permettent pas de le dire. Quand on ajoute au tournoi B un club faible, B3, sans rien changer aux matchs des autres, sa réponse change. Il l'a vérifiée en lui donnant deux fois le même tableau de matchs : elle a bien désigné le meilleur club de ce tableau.

Trouve et corrige chaque erreur dans le code du collègue lui-même : les fonctions corrigées s'appellent `score_exp_fixed`, `weights_fixed`, `estimate_fixed` et `strongest_fixed`, avec les mêmes arguments, et n'appellent ni `mymath` ni la référence `ref_pg` dont se sert le collègue (la vérification le contrôle, copies de leur code comprises). Puis réponds : a) la moyenne des scores au taux $0{,}4$, avec la fonction corrigée, puis avec la fonction fautive (une liste de 2 nombres) ; b) l'estimation de $\mathbb{E}_p[X]$, corrigée puis fautive (une liste de 2 nombres) ; c) la moyenne des 20 000 estimations, corrigée puis fautive (une liste de 2 nombres) ; d) les réponses de la fonction fautive avant puis après l'ajout de B3 (une liste de 2 noms de clubs). Pour chacune des quatre erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés.

**MB8.20 · 🛠️ Un test de propriété.** Écris deux fonctions qui testent une méthode qu'on leur passe, de la même signature que `policy_gradient_exact(P, r, logits, gamma)`, et rendent `True` si la propriété tient, `False` sinon : `matches_finite_differences_20(method)`, qui tire au hasard plusieurs MDP (de 2 à 5 états, 2 ou 3 actions, des matrices $\mathbf{P}[a]$ stochastiques, des récompenses et des logits quelconques, $\gamma$ parmi $0{,}6$ et $0{,}7$) et compare chaque dérivée rendue à la différence finie centrée des valeurs calculées par `np.linalg.solve`, à $10^{-6}$ près en valeur absolue (plus finement que la tolérance par défaut de `np.allclose`, `rtol=1e-5`, `atol=1e-8`) ; `sums_to_zero_20(method)`, qui vérifie, sur des MDP tirés au hasard, que pour tout $s_0$ et tout $s$ la somme des dérivées sur les actions de $s$ est nulle à $10^{-10}$ près. Choisis le pas de tes différences finies pour que la référence passe : l'erreur d'une différence finie centrée a deux parts, la troncature, de l'ordre de $h^2$, et l'arrondi, de l'ordre de $\frac{\varepsilon}{h}$ (M05a §7). La vérification lance tes deux tests sur `policy_gradient_exact` de la référence (`ref_pg.policy_gradient_exact`), sur deux autres méthodes justes, puis sur des méthodes fausses cachées, passées sous un nom neutre (un test juge ce que fait la méthode, pas son nom), une au moins par clause de l'énoncé, que chaque test doit refuser quand sa propriété est fausse. Un test exécute la méthode sur ses MDP et compare ses résultats à ce que dit la propriété : il ne lit ni la méthode ni la pile d'appels, et n'appelle pas `policy_gradient_exact` (ni celle de la référence, ni la tienne : la vérification le contrôle). Relève : a) les résultats de tes deux tests sur `policy_gradient_exact` de la référence (une liste de 2 booléens, dans l'ordre différences finies, somme nulle). Ce qu'il faut regarder : quel pas $h$ donne le plus petit écart, et pourquoi pas $h = 10^{-12}$ ? Quelle méthode fausse passerait le test de somme nulle seul ? Pourquoi tirer les MDP au hasard, avec des logits non nuls ? Une seule taille de MDP, un seul $\gamma$ ou un oracle analytique écrit à la main passeraient-ils la vérification ? Pourquoi l'énoncé demande-t-il des différences finies centrées ?

**MB8.21 · 🏆 Défi : une dérivée avec un budget de tirages.** Écris `derivative_21(draw, c, budget)`, qui estime $J'(\theta) = \frac{\mathrm{d}}{\mathrm{d}\theta}P_\theta(X > c)$ pour une loi $p_\theta$ que tu ne connais pas. Ta fonction peut appeler `draw(k, delta=0.0)` : $k$ tirages, un décalage $\delta$ de $\theta$ (propre à cet exercice). Elle rend deux tableaux de `k` flottants : `k` tirages indépendants $x_i$ de $p_{\theta + \delta}$, puis leurs scores $s_{\theta + \delta}(x_i)$, au paramètre du tirage ; ses appels réunis ne doivent pas dépasser `budget` tirages (au-delà, `draw` rend des `nan`, et le cas échoue). Ni la famille de la loi ni $\theta$ ne sont donnés : la loi est exponentielle, de Poisson, normale ou binomiale, et le seuil $c$ donne une probabilité $P_\theta(X > c)$ qui va de presque 0 à presque 1. Le notebook fournit un cas d'essai, les attentes au téléphone de MB8.1 (taux $0{,}1$, seuil 18 minutes) avec un budget de 10 000 tirages, et une fonction `draw` pour lui. **Critère de réussite :** ton estimation est à 10 % près (en valeur relative) de $J'(\theta)$ pour le cas d'essai, et pour au moins 90 % des 120 cas cachés (douze séries de dix), tirés à nouveau à chaque exécution par un processus à part, qui sert les tirages et compte ceux de chaque cas. Ta fonction ne doit ni exécuter le code du module caché du défi (`solutions/challenges/mb8_21.py`), ni lancer un autre processus, ni lire la vérification (sa pile d'appels, le processus à part) : la vérification le contrôle. Relève : a) ton estimation pour le cas d'essai (un nombre ; la vérification la compare à la dérivée exacte, à 10 % près). Point de départ : la dérivée par le chemin d'une indicatrice est nulle ; des différences finies entre deux échantillons indépendants, à $\theta + h$ et à $\theta - h$, noient l'écart de deux probabilités voisines dans leur bruit ; l'estimateur score sans baseline est sans biais, mais est-il assez précis dans tous les cas ?
