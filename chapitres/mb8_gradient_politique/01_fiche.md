# MB8 · Gradient de politique — fiche de cours

> Les outils statistiques du gradient de politique, hors de tout agent. La **fonction score** d'une loi, d'espérance nulle, et l'**information de Fisher** ; l'**estimateur score** de la dérivée d'une espérance, qui dérive une probabilité là où la dérivée par le chemin de M25b échoue ; la réduction de sa variance par une **variable de contrôle**, la **baseline optimale** et les **baselines de groupe**. Puis le **gradient de la valeur** d'une politique softmax tabulaire, obtenu en dérivant le système de Bellman de M26, avec la **loi d'occupation actualisée** et l'**avantage** ; les **retours à k pas** et le **λ-retour**. Enfin l'**échantillonnage d'importance** (poids, taille effective, poids tronqués) et deux **estimateurs de la KL** ; le modèle de **Bradley-Terry** et la cote **Elo** ; le **principe variationnel de Gibbs**. Le chapitre bonus B8 de workbookIA les applique.

| | |
|---|---|
| **Sections** | §1 à §8 |
| **Temps total estimé** | ≈ 13,3 h : lecture et calculs de la fiche ≈ 2 h 40, exercices ≈ 10 h 06, 16 flashcards ≈ 32 min (parcours essentiel ≈ 11,6 h) |
| **Prérequis** | R3 (trinôme du second degré) ; R5 (série géométrique) ; R7 (dérivée d'un logarithme et d'une composée) ; M02a (intégration par parties) ; M02b (lois de Bernoulli, binomiale, de Poisson, exponentielle et normale ; variance d'une somme indépendante ; simulation par inversion) ; M02c (estimateur sans biais, erreur type, covariance et corrélation, loi des grands nombres) ; M04 (maximum de vraisemblance, log-probabilités) ; M05a (Taylor d'ordre 2, tangente d'une fonction convexe, différences finies centrées et choix du pas, log-sum-exp) ; M06 (divergence KL, KL ≥ 0) ; M07 (Cauchy-Schwarz) ; M13a (sigmoïde, régression logistique) ; M14 (Hedge) ; M16 (puissances d'une matrice d'adjacence) ; M17 (Boltzmann, diag(p) − pᵀp) ; M18 (règle du produit pour des matrices) ; M19 (variance d'une moyenne de tirages) ; M20 (Horvitz-Thompson) ; M25b (dérivée par le chemin, domination, ELBO) ; M26 (MDP, P_π, r_π, Q^π, système de Bellman, loi d'occupation actualisée, erreur TD, télescopage) ; M27 (règle de score propre) ; M28 (température) |
| **Fichiers du chapitre** | `02_exercices.md` (quiz, papier) · `03_notebook.ipynb` · `04_indices.md` · `05_solutions.md` et `05_solutions.ipynb` · `06_mes_reponses.md` · `flashcards.csv` |
| **mymath** | `policy_gradient.py` : `score_function_gradient`, `policy_gradient_exact`, `importance_weights`, `bradley_terry_fit` |
| **Références** | pas de MML (le livre n'a ni fonction score, ni échantillonnage d'importance, ni apprentissage par renforcement) ; Mohamed et coll. (§2, §3) ; Owen (§3, §6) ; Sutton et Barto (§3 à §5) ; Kish, Schulman (§6) ; Bradley et Terry, Zermelo, Hunter, Elo (§7) |

## Comment utiliser ce chapitre

**Ordre conseillé.**
1. `python tools/start_chapter.py MB8` (sur Colab : `00_setup/COLAB.md` §2) : il copie le notebook, ta feuille de réponses et le squelette `mymath/policy_gradient.py`.
2. Section par section : lis **crayon en main** et refais chaque calcul, puis fais les exercices de la section, quiz 🧠 d'abord. Pas de lecture de MML ici : le livre n'a ni fonction score, ni échantillonnage d'importance, ni apprentissage par renforcement ; la fiche est le cours, et les références de « Pour aller plus loin » sont facultatives.
3. Les ✏️ et le 🔗 se font sur papier, dans ta copie de `06_mes_reponses.md`, et se vérifient dans la **partie 0** du notebook ; les ∂ se jugent avec la grille de relecture de `05_solutions.md`.

Quatre blocs : dériver une espérance par rapport au paramètre d'une loi (§1 à §3, dans l'ordre) ; la valeur d'une politique (§4 puis §5, après une relecture de M26 §4, §5 et §8) ; changer de loi (§6) ; comparer, puis choisir (§7, et le §8, qui se lit presque seul).

| Section | Quiz 🧠 et rappels 🔁 | Papier et réflexion | Notebook |
|---|---|---|---|
| §1 La fonction score | Q1 | MB8.8 ∂ | MB8.19 🐛 |
| §2 Score ou chemin | Q1, R3 | MB8.1 ✏️, MB8.11 🔗, MB8.E1 💼 | MB8.13 🔨, MB8.21 🏆 |
| §3 Réduire la variance | Q2 | MB8.2 ✏️, MB8.9 ∂, MB8.11 🔗, MB8.E1 💼 | MB8.13 🔨, MB8.17 🔮, MB8.19 🐛, MB8.21 🏆 |
| §4 Le gradient de la valeur | Q3, R1, R2 | MB8.3 ✏️, MB8.10 ∂ | MB8.14 🔨, MB8.20 🛠️ |
| §5 Retours à k pas et λ-retour | Q3, R2 | MB8.4 ✏️ | |
| §6 Échantillonnage d'importance | Q4 | MB8.5 ✏️ | MB8.15 🔨, MB8.18 🔬, MB8.19 🐛 |
| §7 Bradley-Terry et Elo | Q5 | MB8.6 ✏️, MB8.12 🗣️ | MB8.16 🔨, MB8.19 🐛 |
| §8 Le principe de Gibbs | Q6 | MB8.7 ✏️ | |

Parcours essentiel : tout sauf MB8.9, MB8.18, MB8.20 et MB8.21 (l'énoncé de la baseline optimale et des baselines de groupe en fait partie ; sa démonstration, ∂ MB8.9, non).

📐 **Notations.**
- **Conventions.** Une loi $p_\theta$ (des probabilités ou une densité) dépend d'un paramètre réel $\theta$, et $\partial_\theta$ dérive par rapport à lui, $x$ restant fixé. La **fonction score** est $s_\theta(x) = \partial_\theta\ln p_\theta(x)$ : le score **en $\theta$**, de la forme de $\theta$ (un vecteur si $\theta$ en est un). C'est un autre objet que le **score en $x$** de MB5, $\nabla_x\ln p(x)$, une dérivée par rapport au point, de la forme de $x$. La loi exponentielle est donnée par son **taux** $\theta$ : densité $\theta e^{-\theta x}$ sur $[0, +\infty[$, moyenne $\frac1\theta$ (M25b §7 la donnait par sa moyenne). La loi de Poisson est donnée par sa moyenne, notée $\theta$ elle aussi ($\lambda$ est réservé au λ-retour). Le MDP s'écrit comme en M26.14 : $\mathbf{P}[a, s, s']$ (le tableau `P[a, s, t]` de M26.14 et de `policy_gradient`) est la probabilité d'aller de l'état $s$ à l'état $s'$ sous l'action $a$, $r[a, s] = r(s, a)$ la récompense moyenne, et les logits $z[s, a]$ sont rangés comme $\pi[s, a]$ ; les lois sont des lignes, les valeurs des colonnes (M26). En échantillonnage d'importance, les tirages viennent de $q$ (la proposition), et $w = \frac pq$ ; la KL estimée est $\mathrm{KL}(q \,\|\, p)$, avec des tirages de $q$. Elo est en base 10, à l'échelle 400 : $\beta = \frac{R\ln 10}{400}$. Les logarithmes sont népériens, sauf $\log_{10}$ ; KL en nats.
- **Lettres à double sens.** $s$ : le score $s_\theta$ (§1 à §3), un état (§4, §5). $\theta$ : le paramètre d'une loi (§1 à §3), le taux d'une proposition (§6), le paramètre d'une politique (forme score, §4) ; $\hat\theta$ : un maximum de vraisemblance (§1). $p$ : une loi $p_\theta$ (§1 à §3), la loi cible (§6), $p_i = e^{\beta_i}$ (§7), une loi, dans $r = \ln p$ (§8) ; $\mathbf{p}$ : les probabilités d'une softmax (§4). $q$ : la proposition (§6) ; $Q$ : la valeur d'une action (§4, §5). $\beta$ : la force d'un joueur (§7), le poids de la KL (§8). $\lambda$ : le paramètre du λ-retour (§5). $\gamma$ : le facteur d'actualisation (§4, §5). $w$ : un poids d'importance (§6). $r$ : une récompense moyenne $r(s, a)$ (§4, §5), le bénéfice moyen par botte, à maximiser (§8). $k$ : un nombre de pas (§5), l'indice des estimateurs $k_1$ et $k_3$ (§6), le coefficient d'Elo (§7). $c$ : le coefficient d'une variable de contrôle (§3), un seuil de troncature (§6). $h$ : une variable de contrôle (§3), le pas d'une différence finie (§4). $\nu_{s_0}$ : la loi d'occupation actualisée depuis $s_0$ (§4). $V$, $Q$, $A$ : la valeur d'un état, celle d'une action, l'avantage (§4, §5) ; $\mathbf{M} = (\mathbf{I} - \gamma\mathbf{P}_\pi)^{-1}$ (§4). $e$ : le nombre d'Euler ; $\mathbf{e}$ (en gras) : les erreurs d'une estimation $\mathbf{W}$ des valeurs (§5), et $\mathbf{e}_i$ : le vecteur de base d'une joueuse (§7) ; $W_i$ : les victoires de la joueuse $i$ (§7). $R$ : une récompense $R_t$ (§5), une cote Elo $R_i$ (§7) ; T et R (en romain) : les actions turbiner et retenir, H et B : les niveaux haut et bas du barrage (§4, §5). $E$ : le résultat espéré d'un match (§7), une énergie $E_i$ (§8), à ne pas confondre avec l'espérance $\mathbb{E}$. $I(\theta)$ : l'information de Fisher (§1) ; $\mathbf{I}$ (en gras) : l'identité (§4). $\sigma$ : un écart-type (§1, §2), la sigmoïde (§7). $n$ : un nombre de tirages (§2, §3, §6), de flèches (§1), de matchs $n_{ij}$ (§7). $S$ : le résultat d'un match (§7) ; $S_t$ : l'état au pas $t$ (§4, §5). $Z$ : une constante de normalisation (§8). $F$ : la fonction de répartition $F_\theta$ (§2), l'objectif $F(\pi)$ (§8). $H$ : l'entropie (§8) ; H (en romain) : le niveau haut (§4, §5). $T$ : une température (§8) ; T (en romain) : turbiner (§4). $z$ : un logit (§4), le score $z_m$ d'une régression logistique (§7) ; $\mathbf{z}$ : le latent de M25b (§8). $u$ : une variable réelle (§6), la loi uniforme (§8) ; $U$ : une variable uniforme (§2, §3). $\rho$ : une corrélation (§3). $\delta$ : une erreur TD (§5). $G$ : un retour (§5). $t$ : un pas de temps (§4, §5) ; $s'$ : un état d'arrivée (§4, §5). $\pi$ : une politique (§4, §5), une répartition entre des issues (§8). $\mathbf{w}_t$ : les poids de Hedge (§8). $\mu$ : la moyenne d'une normale (§2), l'espérance à estimer (§3). $\varepsilon$ : un petit accroissement de $\theta$ (§1), le bruit d'un chemin (§2). $b$ : une baseline (§3), le biais d'une régression logistique (§7). $m$ : le nombre d'états (§4), l'indice d'un match (§7) ; $K$ : le nombre d'actions (§4), le nombre d'issues (§8). Le contexte tranche.

Vocabulaire anglais de ce chapitre : *score function*, *support*, *log-likelihood*, *likelihood equation*, *Fisher information*, *score function estimator*, *likelihood ratio method*, *pathwise derivative*, *reparameterization*, *Monte Carlo estimator*, *control variate*, *variance reduction*, *baseline*, *optimal baseline*, *leave-one-out baseline*, *tabular softmax policy*, *logit*, *value function*, *action value*, *advantage*, *discounted state-visitation distribution*, *policy gradient theorem*, *finite differences*, *k-step return*, *bootstrapping*, *λ-return*, *temporal-difference (TD) error*, *importance sampling*, *target distribution*, *proposal distribution*, *importance weight*, *heavy tail*, *self-normalized importance sampling*, *consistent estimator*, *effective sample size*, *truncated importance weights*, *KL estimator*, *paired comparisons*, *Bradley-Terry model*, *strength*, *round-robin tournament*, *identifiability*, *strongly connected graph*, *MM algorithm (minorization-maximization)*, *Elo rating*, *expected score*, *K-factor*, *stochastic gradient*, *Gibbs variational principle*, *reference distribution*, *partition function*.

## Objectifs d'apprentissage

À la fin du chapitre, tu sais :
- **calculer** la fonction score d'une loi usuelle, **vérifier** qu'elle est d'espérance nulle, **calculer** l'information de Fisher de deux façons, et **démontrer** les deux identités du score pour une densité (∂ MB8.8) ;
- **dériver** l'espérance d'une fonction, même discontinue, par rapport au paramètre d'une loi par la méthode du score, et **dire** quand la dérivée par le chemin est préférable ;
- **réduire** la variance d'une estimation de Monte-Carlo par une variable de contrôle, et **calculer** la baseline optimale d'un estimateur score (∂ MB8.9) ;
- **distinguer** une baseline sans biais (la moyenne des autres tirages) d'une baseline qui biaise (la moyenne du groupe, tirage compris) ;
- **calculer** le gradient de la valeur d'une politique softmax tabulaire par le système de Bellman, et l'**écrire** avec la loi d'occupation actualisée et l'avantage (∂ MB8.10) ;
- **écrire** un retour à k pas et un λ-retour, les **relier** aux erreurs TD, et **calculer** leur biais quand les valeurs estimées sont fausses ;
- **estimer** une espérance sous une loi à partir de tirages d'une autre, **calculer** la taille effective, **tronquer** des poids, et **estimer** une KL par $k_1$ ou $k_3$ ;
- **ajuster** un modèle de Bradley-Terry à un tournoi, **dire** quand ses forces existent et ce qu'elles identifient, et **lire** une mise à jour Elo comme un pas de gradient ;
- **trouver** la loi qui maximise une moyenne moins β fois la KL à une loi de référence, et sa valeur.

## L'essentiel en 8 lignes

1. **Score** $s_\theta(x) = \partial_\theta\ln p_\theta(x)$ ; si le support ne dépend pas de $\theta$ : $\mathbb{E}_\theta[s_\theta] = 0$ et $I(\theta) = \mathbb{V}(s_\theta) = -\mathbb{E}_\theta[\partial_\theta^2\ln p_\theta]$ (∂ MB8.8) ; $nI(\theta)$ pour $n$ tirages indépendants ; $\mathrm{KL}(p_\theta \,\|\, p_{\theta'}) \approx \frac12I(\theta)(\theta' - \theta)^2$.
2. **Méthode du score** : $\frac{\mathrm{d}}{\mathrm{d}\theta}\mathbb{E}_\theta[f(X)] = \mathbb{E}_\theta[f(X)\,s_\theta(X)]$, pour $f$ quelconque (une indicatrice aussi) ; même espérance que le chemin (M25b), une autre variance ; le chemin donne 0 pour une indicatrice ou une loi discrète.
3. **Contrôle** : $f - c\,(h - \mathbb{E}[h])$, $c^\star = \frac{\operatorname{Cov}(f, h)}{\mathbb{V}(h)}$, variance $(1 - \rho^2)\,\mathbb{V}(f)$. **Baseline** : $(f - b)\,s$ sans biais, optimale en $b^\star = \frac{\mathbb{E}[fs^2]}{\mathbb{E}[s^2]} \ne \mathbb{E}[f]$ en général ; la moyenne des autres tirages est sans biais, celle du groupe multiplie l'estimateur par $\frac{n - 1}{n}$ (∂ MB8.9).
4. **Gradient de la valeur** : $\partial\mathbf{V} = \mathbf{M}\big(\partial\mathbf{r}_\pi + \gamma\,(\partial\mathbf{P}_\pi)\,\mathbf{V}\big)$, $\frac{\partial V(s_0)}{\partial z(s, a)} = \frac{\nu_{s_0}(s)}{1 - \gamma}\,\pi(a \mid s)\,A(s, a)$ (∂ MB8.10), $\sum_a\pi(a \mid s)\,A(s, a) = 0$ ; un état visité au pas $t$ pèse $(1 - \gamma)\gamma^t$ dans $\nu_{s_0}$.
5. **Retours** : $G^{(k)}_t - V(S_t) = \sum_{l<k}\gamma^l\delta_{t+l}$ ; $G^\lambda_t = \sum_{k \ge 1}(1 - \lambda)\lambda^{k-1}G^{(k)}_t$ et $G^\lambda_t - V(S_t) = \sum_{l \ge 0}(\gamma\lambda)^l\delta_{t+l}$ ; avec des valeurs fausses de $\mathbf{e}$, le retour à $k$ pas a le biais $\gamma^k(\mathbf{P}_\pi^k\mathbf{e})(s)$.
6. **Importance** : $\mathbb{E}_p[f] = \mathbb{E}_q[wf]$, $w = \frac pq$, si $q > 0$ là où $pf \ne 0$ ; $\mathbb{E}_q[w] = 1$ si $q > 0$ là où $p > 0$ ; taille effective $\frac{(\sum w_i)^2}{\sum w_i^2}$ ; poids auto-normalisés, poids tronqués $\min(w, c)$. $\mathrm{KL}(q \,\|\, p)$ : $k_1 = -\ln w$ et $k_3 = (w - 1) - \ln w \ge 0$, sans biais.
7. **Bradley-Terry** : $P(i \text{ bat } j) = \sigma(\beta_i - \beta_j)$ ; forces à une constante près ; victoires observées = victoires attendues ; maximum fini si et seulement si le graphe des victoires est fortement connexe. **Elo** : $R_i \leftarrow R_i + k\,(S - E)$, $E = \frac{1}{1 + 10^{(R_j - R_i)/400}}$, un pas de gradient stochastique.
8. **Gibbs** : $\mathbb{E}_\pi[r] - \beta\,\mathrm{KL}(\pi \,\|\, \pi_{\mathrm{ref}}) = \beta\ln Z - \beta\,\mathrm{KL}(\pi \,\|\, \pi^\star)$, $\pi^\star \propto \pi_{\mathrm{ref}}\,e^{r/\beta}$, maximum $\beta\ln Z$ ; $\beta \to 0$ : le meilleur choix ; $\beta \to \infty$ : $\pi_{\mathrm{ref}}$.

## §1 · La fonction score d'une loi : espérance nulle et information de Fisher

### Dériver par rapport au paramètre

Une archère tire 4 flèches ; chacune atteint le cœur de la cible avec la probabilité $\theta$, indépendamment des autres. Le nombre $X$ de flèches au cœur suit la loi binomiale $\mathcal{B}(4, \theta)$ (M02b) : $p_\theta(x) = \binom4x\theta^x(1 - \theta)^{4 - x}$. Si $\theta$ augmente un peu, comment change la probabilité de chaque issue, **en valeur relative** ?

> **Définition.** Pour une famille de lois $p_\theta$ dérivable en $\theta$, la **fonction score** (*score function*) est
> $$s_\theta(x) = \partial_\theta\ln p_\theta(x) = \frac{\partial_\theta p_\theta(x)}{p_\theta(x)},$$
> pour les issues $x$ du **support** (*support*), l'ensemble des $x$ où $p_\theta(x) > 0$.

Au premier ordre, $p_{\theta + \varepsilon}(x) \approx p_\theta(x)\,\big(1 + \varepsilon\,s_\theta(x)\big)$ : le score est la variation relative de la probabilité de $x$ quand le paramètre bouge. Pour la binomiale, $\ln p_\theta(x) = \ln\binom4x + x\ln\theta + (4 - x)\ln(1 - \theta)$, donc
$$s_\theta(x) = \frac x\theta - \frac{4 - x}{1 - \theta} = \frac{x - 4\theta}{\theta(1 - \theta)}, \qquad \text{et pour } \theta = 0{,}8 : \ s(x) = \frac{x - 3{,}2}{0{,}16} = 6{,}25\,x - 20.$$

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $p_{0,8}(x)$ | 0,0016 | 0,0256 | 0,1536 | 0,4096 | 0,4096 |
| $s_{0,8}(x)$ | −20 | −13,75 | −7,5 | −1,25 | 5 |

Quatre flèches au cœur devient plus probable quand $\theta$ augmente ; trois, l'issue la plus proche de la moyenne 3,2, bouge à peine ; moins de trois devient moins probable, d'autant plus vite que l'issue est rare.

Les lois usuelles (M02b), en dérivant $\ln p_\theta(x)$ :

| loi | $\ln p_\theta(x)$, à une constante près en $\theta$ | $s_\theta(x)$ | $I(\theta)$ (plus bas) |
|---|---|---|---|
| Bernoulli de paramètre $\theta$, $x \in \{0, 1\}$ | $x\ln\theta + (1 - x)\ln(1 - \theta)$ | $\frac{x - \theta}{\theta(1 - \theta)}$ | $\frac{1}{\theta(1 - \theta)}$ |
| binomiale $\mathcal{B}(n, \theta)$ | $x\ln\theta + (n - x)\ln(1 - \theta)$ | $\frac{x - n\theta}{\theta(1 - \theta)}$ | $\frac{n}{\theta(1 - \theta)}$ |
| Poisson de moyenne $\theta$ | $x\ln\theta - \theta$ | $\frac x\theta - 1$ | ∂ MB8.8 |
| exponentielle de taux $\theta$ | $\ln\theta - \theta x$ | $\frac1\theta - x$ | ∂ MB8.8 |
| normale $\mathcal{N}(\theta, \sigma^2)$, $\sigma$ connu | $-\frac{(x - \theta)^2}{2\sigma^2}$ | $\frac{x - \theta}{\sigma^2}$ | $\frac{1}{\sigma^2}$ |

### Une espérance nulle

Pour l'archère, $\sum_xp(x)\,s(x) = 6{,}25\,\big(\mathbb{E}[X] - 3{,}2\big) = 6{,}25\,(4 \times 0{,}8 - 3{,}2) = 0$. Ce n'est pas un hasard.

> **Théorème** (∂ MB8.8). Si le support de $p_\theta$ ne dépend pas de $\theta$, et si l'on peut dériver sous la somme ou sous l'intégrale (sans condition pour une somme finie ; admis pour une somme infinie ou une densité), alors $\mathbb{E}_\theta[s_\theta(X)] = 0$.

L'outil : dériver par rapport à $\theta$ l'identité $\sum_xp_\theta(x) = 1$, ou $\int p_\theta = 1$, vraie pour tout $\theta$ ; ∂ MB8.8 rédige le cas d'une densité (l'échange de la dérivée et de l'intégrale se justifie par la domination de M25b §7).

**Quand le support bouge.** La loi uniforme sur $[0, \theta]$ a la densité $\frac1\theta$ sur $[0, \theta]$ : son score vaut $-\frac1\theta$ en tout point du support, et son espérance aussi, pas 0 : le support bouge avec $\theta$ ; ∂ MB8.8 montre ce qui manque.

**Le score total et le maximum de vraisemblance.** Pour des observations indépendantes $x_1, \ldots, x_n$, la log-vraisemblance $\ell(\theta) = \sum_i\ln p_\theta(x_i)$ a pour dérivée le **score total** $\sum_is_\theta(x_i)$ : un maximum de vraisemblance intérieur l'annule (M04 §3, M13a §1). L'archère a mis 4, 3, 4, 2 et 3 flèches au cœur en cinq séances : $\sum_is_\theta(x_i) = \frac{16 - 20\theta}{\theta(1 - \theta)}$ s'annule en $\hat\theta = 0{,}8$, la proportion de flèches au cœur. Le théorème dit autre chose : au **vrai** paramètre, la pente de la log-vraisemblance d'une observation est nulle **en moyenne**.

### L'information de Fisher

> **Définition.** L'**information de Fisher** (*Fisher information*) est $I(\theta) = \mathbb{V}_\theta\big(s_\theta(X)\big) = \mathbb{E}_\theta\big[s_\theta(X)^2\big]$ (l'espérance du score étant nulle).
>
> **Théorème** (∂ MB8.8). Sous les mêmes hypothèses, avec une seconde dérivation sous l'intégrale (admise), $I(\theta) = -\mathbb{E}_\theta\big[\partial_\theta^2\ln p_\theta(X)\big]$.

L'outil : dériver une seconde fois l'identité de l'espérance nulle, $\int p_\theta\,s_\theta = 0$.

Deux lectures : la **variance** de la pente de la log-vraisemblance, et sa **courbure** moyenne, changée de signe (figure). Pour l'archère : $\mathbb{V}(s) = 6{,}25^2\,\mathbb{V}(X) = 39{,}0625 \times 0{,}64 = 25$, avec $\mathbb{V}(X) = 4 \times 0{,}8 \times 0{,}2$ ; et $\partial_\theta^2\ln p_\theta(x) = -\frac{x}{\theta^2} - \frac{4 - x}{(1 - \theta)^2}$, d'espérance $-\frac{3{,}2}{0{,}64} - \frac{0{,}8}{0{,}04} = -25$. Les deux valent $\frac{4}{\theta(1 - \theta)}$.

> **Propriété.** Pour $n$ tirages indépendants de $p_\theta$, le score total a pour variance $nI(\theta)$ : l'information d'un échantillon i.i.d. est $n$ fois celle d'un tirage (les variances de variables indépendantes s'ajoutent, M02b §6).

La binomiale compte les succès de 4 tirages de Bernoulli : $4 \times \frac{1}{0{,}8 \times 0{,}2} = 4 \times 6{,}25 = 25$. Une grande information veut dire une loi qui change vite avec $\theta$ : les observations en disent long sur lui.

![À gauche, la loi B(4 ; 0,8) de l'archère, avec le score de chaque issue (de −20 à 5) : pondérés par les probabilités, ils ont une somme nulle, et leurs carrés pondérés valent I(0,8) = 25. À droite, les log-vraisemblances θ ↦ ln p_θ(x) pour x = 2, 3 et 4, avec leurs tangentes en θ₀ = 0,8, de pentes −7,5, −1,25 et 5 ; leur moyenne sous θ₀ a une tangente horizontale en θ₀ et y épouse la parabole de courbure −25](figures/score_fisher.png)

### La KL de deux lois voisines

> **Propriété** (au second ordre). $\mathrm{KL}(p_\theta \,\|\, p_{\theta'}) \approx \frac12I(\theta)\,(\theta' - \theta)^2$ quand $\theta' \to \theta$.

L'idée : en fonction de $\theta'$, $\mathrm{KL}(p_\theta \,\|\, p_{\theta'}) = \mathbb{E}_\theta[\ln p_\theta(X) - \ln p_{\theta'}(X)]$ est positive et nulle en $\theta' = \theta$ (M06 §6) ; ses dérivées en $\theta' = \theta$ sont $-\mathbb{E}_\theta[s_\theta(X)] = 0$, puis $-\mathbb{E}_\theta[\partial_\theta^2\ln p_\theta(X)] = I(\theta)$ ; Taylor d'ordre 2 (M05a §3) conclut. Pour l'archère, de $\theta = 0{,}8$ à $\theta' = 0{,}78$ : $4\big[0{,}8\ln\frac{0{,}8}{0{,}78} + 0{,}2\ln\frac{0{,}2}{0{,}22}\big] \approx 0{,}00477$ nat, et $\frac12 \times 25 \times 0{,}02^2 = 0{,}005$. L'information de Fisher mesure, localement, la distance entre les lois de la famille.

💻 **Aujourd'hui en pratique** — les logiciels de statistique qui ajustent une loi par maximum de vraisemblance donnent son erreur type par la courbure de la log-vraisemblance au maximum (l'**information observée**, *observed information*), environ $\frac{1}{\sqrt{nI(\hat\theta)}}$ pour un paramètre réel : un résultat asymptotique, admis ici.

⚠️ **Erreur classique.** Confondre les sens du mot **score** : ici le score en $\theta$ d'une loi, $\partial_\theta\ln p_\theta(x)$, une dérivée par rapport au paramètre, de la forme de $\theta$ ; en MB5, le score en $x$ d'une densité, $\nabla_x\ln p(x)$, de la forme de $x$ ; ailleurs, le score d'un exemple que calcule un classifieur (le score $z$ de M13a, le score $S$ de M03 et de MB6), une note qui classe (MB2 à MB4), ou la règle de score propre de M27. Autre erreur : écrire le score de la loi exponentielle pour sa moyenne (le paramétrage de M25b §7), $\frac{x - \theta}{\theta^2}$, quand $\theta$ est son taux, comme dans ce chapitre : $\frac1\theta - x$.

🔗 **Dans workbookIA** — le chapitre B8 nomme la fonction score au moment de dériver l'espérance d'un retour par rapport aux paramètres d'une politique, et se sert de son espérance nulle.

## §2 · Dériver une espérance par le score, et comparer à la dérivée par le chemin (M25b)

### La méthode du score

M25b §7 dérivait $J(\theta) = \mathbb{E}_\theta[f(X)]$ en écrivant $X = g_\theta(\xi)$ ; cette **dérivée par le chemin** donnait 0 pour une indicatrice, et M25b nommait pour ce cas la **méthode du score** (*score function method*). La voici.

> **Théorème.** Si le support de $p_\theta$ ne dépend pas de $\theta$, et si l'on peut dériver sous la somme ou sous l'intégrale (sans condition pour une somme finie ; admis pour une somme infinie ou une densité), alors
> $$\frac{\mathrm{d}}{\mathrm{d}\theta}\,\mathbb{E}_\theta[f(X)] = \mathbb{E}_\theta\big[f(X)\,s_\theta(X)\big].$$

L'outil : la dérivée d'un logarithme (R7), $\partial_\theta p_\theta(x) = p_\theta(x)\,s_\theta(x)$, à l'intérieur de $\sum_xf(x)\,p_\theta(x)$ ou de $\int f\,p_\theta$. La fonction $f$ n'est jamais dérivée : elle peut sauter, comme une indicatrice ; seule la loi l'est. Avec $f = 1$, on retrouve $\mathbb{E}[s_\theta] = 0$.

> **L'estimateur score** (*score function estimator*). Pour $x_1, \ldots, x_n$ tirés indépendamment de $p_\theta$, $\hat g = \frac1n\sum_if(x_i)\,s_\theta(x_i)$ est un estimateur **sans biais** de $J'(\theta)$, de variance $\frac1n\mathbb{V}\big(f(X)\,s_\theta(X)\big)$ (M02c, M19 §7).

**Des étoiles filantes.** Une nuit d'août, le nombre $X$ d'étoiles filantes qu'on voit en un quart d'heure suit une loi de Poisson de moyenne $\theta$ ; la soirée d'observation d'un club est réussie si $X \ge 3$. Avec $f(x) = \mathbb{1}\{x \ge 3\}$ :
$$J(\theta) = P(X \ge 3) = 1 - e^{-\theta}\Big(1 + \theta + \frac{\theta^2}{2}\Big), \qquad J'(\theta) = e^{-\theta}\Big(1 + \theta + \frac{\theta^2}{2}\Big) - e^{-\theta}(1 + \theta) = \frac{\theta^2e^{-\theta}}{2}.$$
En $\theta = 2$ : $J(2) \approx 0{,}3233$ et $J'(2) = 2e^{-2} \approx 0{,}2707$. Par le score, $s_2(x) = \frac x2 - 1$, et $f(x)\,s_2(x)$ vaut 0 pour $x \le 2$, puis 0,5, 1, 1,5… pour $x = 3, 4, 5\ldots$ ; son espérance, $\sum_{x \ge 3}p_2(x)\big(\frac x2 - 1\big)$, redonne $0{,}2707$. Sa variance vaut environ $0{,}2237$ : un écart-type de $0{,}473$ pour un tirage, et de $0{,}024$ pour la moyenne de 400.

**Le chemin ne voit rien.** Pour une loi discrète comme celle-ci, tout chemin $X = g_\theta(\xi)$ ne prend que des valeurs entières : par la simulation par inversion (M02b), $X = F_\theta^{-1}(U)$, et, à $U$ fixé, $\theta \mapsto X$ est une fonction en escalier. Sa dérivée est nulle partout où elle existe : la dérivée par le chemin vaut 0, quelle que soit $f$. Toute la variation de $J$ vient des tirages qui changent de marche, invisibles tirage par tirage : c'est l'échec de l'indicatrice de M25b §7, en pire.

### Le score contre le chemin

Quand les deux existent, ils ont la même espérance, $J'(\theta)$, mais pas la même variance. Pour $X \sim \mathcal{N}(\mu, 1)$ et $f(x) = x^2$, $J(\mu) = \mu^2 + 1$ et $J'(\mu) = 2\mu$.
- **Par le chemin** $X = \mu + \varepsilon$ : $\partial_\mu f(\mu + \varepsilon) = 2X$, de variance 4.
- **Par le score** $s_\mu(x) = x - \mu$ : $X^2(X - \mu)$, de variance $15 + 14\mu^2 + \mu^4$ (un calcul de moments de $\mathcal{N}(0, 1)$), soit 30 en $\mu = 1$, 7,5 fois plus.

Le chemin se sert de la dérivée de $f$, une information que le score n'a pas ; le score n'a besoin que de $\ln p_\theta$.

| | dérivée par le chemin (M25b §7) | méthode du score |
|---|---|---|
| ce qu'elle demande | un chemin $X = g_\theta(\xi)$ et $f$ dérivables (domination) | $\ln p_\theta$ dérivable, un support fixe |
| $f$ discontinue (une indicatrice) | 0 : faux | juste |
| loi discrète | 0 : faux | juste |
| variance | souvent faible, quand elle s'applique | souvent grande |

![À gauche, la probabilité de voir au moins 3 étoiles filantes, P(X ≥ 3), en fonction de la moyenne θ, avec sa tangente en θ = 2, de pente 2e⁻² ≈ 0,2707. À droite, pour X de loi N(1, 1) et f(x) = x², les histogrammes de 20 000 estimations à un tirage de la dérivée 2 : par le chemin, 2X, d'écart-type 2 ; par le score, X²(X − 1), d'écart-type proche de √30 ≈ 5,48, avec un pic près de 0 et une longue queue](figures/score_chemin.png)

💻 **Aujourd'hui en pratique** — les lois de `torch.distributions` offrent les deux : `rsample` tire par un chemin dérivable quand la loi le permet (une normale, une exponentielle), et `log_prob` donne $\ln p_\theta$, dont on dérive le score par différentiation automatique : la voie usuelle pour une loi discrète.

⚠️ **Erreur classique.** Dériver par le chemin une loi discrète ou une indicatrice : on trouve 0 (M25b §7 l'avait vu pour l'indicatrice). Évaluer le score en un autre point que le $\theta$ où l'on dérive.

🔗 **Dans workbookIA** — REINFORCE, au chapitre B8, est cet estimateur appliqué à la loi des actions d'une politique : il dérive l'espérance d'un retour sans dériver le retour lui-même.

## §3 · Réduire la variance : variables de contrôle, baseline optimale et baselines de groupe

### Une variable de contrôle

Pour estimer $\mu = \mathbb{E}[f(X)]$ par Monte-Carlo, on dispose parfois d'une autre fonction $h(X)$, **corrélée** à $f(X)$, dont l'espérance est **connue**. Pour tout nombre $c$, $f(X) - c\,\big(h(X) - \mathbb{E}[h]\big)$ a la même espérance que $f(X)$ : c'est une **variable de contrôle** (*control variate*).

> **Propriété.** $\mathbb{V}\big(f - c\,(h - \mathbb{E}[h])\big) = \mathbb{V}(f) - 2c\operatorname{Cov}(f, h) + c^2\,\mathbb{V}(h)$ est minimale en $c^\star = \frac{\operatorname{Cov}(f, h)}{\mathbb{V}(h)}$, où elle vaut $(1 - \rho^2)\,\mathbb{V}(f)$, avec $\rho$ la corrélation de $f(X)$ et $h(X)$ (M02c).

*Démonstration.* La variance d'une combinaison se développe comme en M02c ; c'est un trinôme en $c$ (R3) de coefficient dominant $\mathbb{V}(h) > 0$, minimal en $c^\star$, où il vaut $\mathbb{V}(f) - \frac{\operatorname{Cov}(f, h)^2}{\mathbb{V}(h)} = (1 - \rho^2)\,\mathbb{V}(f)$. $\square$

**Exemple.** Pour estimer $\mathbb{E}[e^U] = e - 1 \approx 1{,}7183$, avec $U$ uniforme sur $[0, 1]$ (la valeur moyenne que M02a §8 estimait par Monte-Carlo), on prend $h = U$, d'espérance $\frac12$. Ici $\mathbb{V}(e^U) = \frac{e^2 - 1}{2} - (e - 1)^2 \approx 0{,}2420$, $\operatorname{Cov}(e^U, U) = \mathbb{E}[Ue^U] - \frac{e - 1}{2} = 1 - \frac{e - 1}{2} \approx 0{,}1409$ (une intégration par parties, M02a) et $\mathbb{V}(U) = \frac1{12}$ : $c^\star \approx 1{,}690$ et $\rho^2 \approx 0{,}984$. La variance est divisée par environ 61 : un tirage contrôlé vaut 61 tirages bruts (figure, à droite).

### Une baseline pour l'estimateur score

Comme $\mathbb{E}[s_\theta(X)] = 0$ (§1), pour tout nombre $b$, $\big(f(X) - b\big)\,s_\theta(X)$ a la même espérance que $f(X)\,s_\theta(X)$, la dérivée $J'(\theta)$. Le nombre $b$ est une **baseline** (*baseline*, une valeur de référence) : il ne change que la variance.

> **Théorème** (∂ MB8.9). Pour un paramètre réel $\theta$ tel que $I(\theta) = \mathbb{E}[s_\theta^2] > 0$, $\mathbb{V}\big((f(X) - b)\,s_\theta(X)\big)$ est minimale pour la **baseline optimale** (*optimal baseline*)
> $$b^\star = \frac{\mathbb{E}\big[f(X)\,s_\theta(X)^2\big]}{\mathbb{E}\big[s_\theta(X)^2\big]},$$
> une moyenne de $f$ pondérée par $s_\theta^2$, différente de $\mathbb{E}[f(X)]$ en général.

L'outil : comme pour la variable de contrôle, la variance est un trinôme du second degré en $b$ ; ∂ MB8.9 la rédige.

**Les étoiles filantes** ($f = \mathbb{1}\{X \ge 3\}$, $\theta = 2$). Ici $s^2 = \big(\frac X2 - 1\big)^2$, $\mathbb{E}[s^2] = \frac{\mathbb{V}(X)}{4} = 0{,}5$ (M02b) et $\mathbb{E}[f\,s^2] = \sum_{x \ge 3}p_2(x)\big(\frac x2 - 1\big)^2 \approx 0{,}2970$ : $b^\star \approx 0{,}594$, loin de $\mathbb{E}[f] = P(X \ge 3) \approx 0{,}323$. Les tirages qui pèsent dans $b^\star$ sont ceux où $\lvert s\rvert$ est grand, loin de $x = 2$ : $x = 0$, où $f$ vaut 0, et $x \ge 4$, où elle vaut 1. La variance à un tirage passe de $0{,}2237$ sans baseline à $0{,}0473$ avec $b^\star$, environ 4,7 fois moins (figure, à gauche, qui place aussi $b = \mathbb{E}[f]$).

![À gauche, pour les étoiles filantes, la variance à un tirage de (f − b)s en fonction de la baseline b : un trinôme, qui vaut 0,2237 en b = 0, 0,0840 en b = E[f] ≈ 0,323 et 0,0473 en b* ≈ 0,594, son minimum. À droite, 300 tirages (U, e^U) et la droite de pente c* ≈ 1,690 passant par (½, e − 1) : U, de moyenne connue, suit presque toute la variation de e^U](figures/baseline_variance.png)

### Des baselines tirées de l'échantillon

En pratique, ni $\mathbb{E}[f]$ ni $b^\star$ ne sont connus : on les estime sur les tirages. Pour $n \ge 2$ tirages indépendants $x_1, \ldots, x_n$, notons $f_i = f(x_i)$, $s_i = s_\theta(x_i)$, $\bar f = \frac1n\sum_jf_j$ la **moyenne du groupe**, et $\bar f_{-i} = \frac{1}{n - 1}\sum_{j \ne i}f_j$ la **moyenne des autres** (*leave-one-out*).

> **Théorème** (∂ MB8.9). L'estimateur $\frac1n\sum_i(f_i - \bar f_{-i})\,s_i$ est sans biais. L'estimateur $\frac1n\sum_i(f_i - \bar f)\,s_i$, dont la baseline contient le tirage $i$, vaut **exactement** $\frac{n - 1}{n}$ fois le précédent, sur chaque échantillon : un biais multiplicatif.

L'outil : l'indépendance des tirages et $\mathbb{E}[s] = 0$ pour le premier point ; une écriture de $\bar f$ à l'aide de $\bar f_{-i}$ pour le second.

**Cinq soirées.** Les comptes $x = (4, 0, 2, 6, 0)$ donnent $f = (1, 0, 0, 1, 0)$ et $s = (1 ;\ -1 ;\ 0 ;\ 2 ;\ -1)$. Sans baseline, l'estimation vaut $\frac{1 + 2}{5} = 0{,}6$. Avec la moyenne des autres, $\bar f_{-i} = \frac{2 - f_i}{4}$, soit $(0{,}25 ;\ 0{,}5 ;\ 0{,}5 ;\ 0{,}25 ;\ 0{,}5)$, et l'estimation vaut $\frac{0{,}75 + 0{,}5 + 0 + 1{,}5 + 0{,}5}{5} = 0{,}65$. Avec la moyenne du groupe, $\bar f = 0{,}4$, elle vaut $0{,}52 = \frac45 \times 0{,}65$. Cinq tirages disent peu de chose de $J'(2) \approx 0{,}2707$ ; mais le facteur $\frac{n - 1}{n}$ est exact.

Diviser chaque terme $(f_i - \bar f)\,s_i$ par l'écart-type des $f_j$ du groupe garde son signe ; mais l'espérance de l'estimateur n'est plus exactement proportionnelle à la dérivée.

💻 **Aujourd'hui en pratique** — `score_function_gradient` (🔨 MB8.13) rend la moyenne des $(f_i - b_i)\,s_i$ et son erreur type, avec une baseline constante ou la moyenne des autres tirages. En simulation, notamment en finance, on estime $c^\star$ sur les tirages eux-mêmes ; cela ajoute un biais de l'ordre de $\frac1n$, en général négligeable (Owen, §8.9).

⚠️ **Erreur classique.** Prendre $\mathbb{E}[f]$ pour la baseline optimale : $b^\star$ pondère les tirages par $s^2$ ($0{,}594$ contre $0{,}323$ pour les étoiles filantes) ; employer une variable de contrôle dont l'espérance n'est pas connue exactement : l'estimateur n'est plus sans biais.

🔗 **Dans workbookIA** — le chapitre B8 retranche une baseline aux retours de REINFORCE ; GRPO prend pour baseline la moyenne d'un groupe de tirages, puis divise par leur écart-type.

## §4 · Le gradient de la valeur d'une politique, sous forme matricielle (après M26)

### Rappel de M26 : une politique et ses valeurs

Un MDP (M26 §4) a des états $s$, des actions $a$, des matrices de transition $\mathbf{P}[a]$ et des récompenses moyennes $r(s, a)$. Une politique $\pi(a \mid s)$ induit la chaîne et les récompenses
$$\mathbf{P}_\pi[s, s'] = \sum_a\pi(a \mid s)\,\mathbf{P}[a, s, s'], \qquad r_\pi(s) = \sum_a\pi(a \mid s)\,r(s, a),$$
et ses valeurs résolvent le système de Bellman $(\mathbf{I} - \gamma\mathbf{P}_\pi)\,\mathbf{V} = \mathbf{r}_\pi$ (M26 §5). La valeur d'une action est $Q(s, a) = r(s, a) + \gamma\sum_{s'}\mathbf{P}[a, s, s']\,V(s')$, et $V(s) = \sum_a\pi(a \mid s)\,Q(s, a)$ (M26 §4). On note $\mathbf{M} = (\mathbf{I} - \gamma\mathbf{P}_\pi)^{-1}$. Pour $\gamma < 1$, la ligne $s_0$ de $(1 - \gamma)\,\mathbf{M}$ est la **loi d'occupation actualisée** $\boldsymbol{\nu}_{s_0}$ de M26 §5 :
$$\nu_{s_0}(s) = \sum_{t \ge 0}(1 - \gamma)\gamma^t\,P(S_t = s \mid S_0 = s_0), \qquad V(s_0) = \frac{\boldsymbol{\nu}_{s_0}\mathbf{r}_\pi}{1 - \gamma} :$$
un état visité au pas $t$ y pèse $(1 - \gamma)\gamma^t$. Avec des lignes sous-stochastiques (une fin possible, M26 §5), $\mathbf{M}$ reste défini, et même pour $\gamma = 1$ quand la fin est sûre ; seule la lecture de $(1 - \gamma)\,\mathbf{M}$ comme une loi demande des lignes stochastiques.

### Une politique softmax tabulaire

> **Définition.** Une **politique softmax tabulaire** (*tabular softmax policy*) a un **logit** $z(s, a)$ par état et par action, et $\pi(a \mid s) = \frac{e^{z(s, a)}}{\sum_be^{z(s, b)}}$ : la loi de Boltzmann (M17 §7) de la ligne $z(s, \cdot)$, à la température 1.

Ajouter un même nombre aux logits d'un état ne change pas la politique (l'origine des énergies est arbitraire, M17 §7). Toute politique dont les probabilités sont positives s'écrit ainsi ; une politique **déterministe** n'en est qu'une limite, quand des logits partent à l'infini.

**Un barrage.** Chaque semaine, le lac d'un barrage hydroélectrique est à un niveau haut (H) ou bas (B). L'exploitant peut **turbiner** (T : vendre de l'électricité, ce qui vide le lac) ou **retenir** (R) ; les pluies rendent les transitions aléatoires. En milliers d'euros (retenir quand le lac est haut le fait parfois déborder, ce qui coûte) :

| depuis | $\mathbf{P}[\mathrm{T}]$ : vers H ; vers B | $\mathbf{P}[\mathrm{R}]$ : vers H ; vers B | $r(s, \mathrm{T})$ | $r(s, \mathrm{R})$ |
|---|---|---|---|---|
| H | 0,35 ; 0,65 | 0,85 ; 0,15 | 7 | −1 |
| B | 0,1 ; 0,9 | 0,45 ; 0,55 | 2 | 0 |

Les logits $z(\mathrm{H}, \mathrm{T}) = \ln 2$, $z(\mathrm{H}, \mathrm{R}) = -\ln 2$, $z(\mathrm{B}, \mathrm{T}) = 0$, $z(\mathrm{B}, \mathrm{R}) = \ln 1{,}5$ donnent une politique qui turbine avec la probabilité 0,8 en H et 0,4 en B. Avec $\gamma = 0{,}6$ : la ligne H de $\mathbf{P}_\pi$ vaut $0{,}8\,(0{,}35 ;\ 0{,}65) + 0{,}2\,(0{,}85 ;\ 0{,}15) = (0{,}45 ;\ 0{,}55)$, la ligne B $(0{,}31 ;\ 0{,}69)$, et $\mathbf{r}_\pi = (0{,}8 \times 7 - 0{,}2 ;\ 0{,}4 \times 2) = (5{,}4 ;\ 0{,}8)$. Puis
$$\mathbf{I} - 0{,}6\,\mathbf{P}_\pi = \begin{pmatrix} 0{,}73 & -0{,}33 \\ -0{,}186 & 0{,}586 \end{pmatrix}, \quad \det = 0{,}3664, \quad \mathbf{M} \approx \begin{pmatrix} 1{,}5993 & 0{,}9007 \\ 0{,}5076 & 1{,}9924 \end{pmatrix}, \quad \mathbf{V} = \mathbf{M}\,\mathbf{r}_\pi \approx (9{,}3570 ;\ 4{,}3352),$$
et les lois d'occupation sont $\boldsymbol{\nu}_{\mathrm{H}} \approx (0{,}6397 ;\ 0{,}3603)$ et $\boldsymbol{\nu}_{\mathrm{B}} \approx (0{,}2031 ;\ 0{,}7969)$.

### Dériver le système de Bellman

> **Théorème** (∂ MB8.10). Si la politique dépend d'un paramètre réel de façon dérivable (un logit, par exemple), avec $\gamma < 1$ ou une fin sûre,
> $$\partial\mathbf{V} = \mathbf{M}\,\big(\partial\mathbf{r}_\pi + \gamma\,(\partial\mathbf{P}_\pi)\,\mathbf{V}\big).$$
> Pour une politique softmax tabulaire, avec l'**avantage** (*advantage*) $A(s, a) = Q(s, a) - V(s)$ de l'action $a$ en $s$ :
> $$\frac{\partial V(s_0)}{\partial z(s, a)} = \mathbf{M}[s_0, s]\;\pi(a \mid s)\;A(s, a) = \frac{\nu_{s_0}(s)}{1 - \gamma}\;\pi(a \mid s)\;A(s, a) \quad (\text{la seconde écriture pour } \gamma < 1).$$

L'outil : dériver l'égalité $(\mathbf{I} - \gamma\mathbf{P}_\pi)\,\mathbf{V} = \mathbf{r}_\pi$ par la règle du produit (M18 §7) et résoudre en $\partial\mathbf{V}$, puis la jacobienne de la softmax, $\operatorname{diag}(\mathbf{p}) - \mathbf{p}^\top\mathbf{p}$ (M17 §7) ; ∂ MB8.10 le rédige.

Trois facteurs, trois lectures.
- $\frac{\nu_{s_0}(s)}{1 - \gamma}$ : combien de fois, actualisées, on passe en $s$ depuis $s_0$ ; un logit d'un état qu'on ne visite jamais depuis $s_0$ ne change pas $V(s_0)$.
- $\pi(a \mid s)$ : une action rarement tirée pèse peu. Près d'une politique déterministe, toutes les dérivées en $s$ sont presque nulles (l'action presque sûre a un avantage presque nul, les autres une probabilité presque nulle) : la softmax sature, comme en MB3 §7.
- $A(s, a)$ : l'avantage, d'espérance nulle sous la politique.

> **Propriété.** $\sum_a\pi(a \mid s)\,A(s, a) = V(s) - V(s) = 0$ pour tout $s$ (M26 §4) ; donc $\sum_a\frac{\partial V(s_0)}{\partial z(s, a)} = 0$, ce qu'annonçait l'invariance des logits par l'ajout d'une constante.

**La forme score.** Pour une politique qui dépend d'un paramètre $\theta$ de façon quelconque, le même calcul donne (énoncé)
$$\partial_\theta V(s_0) = \frac{1}{1 - \gamma}\sum_s\nu_{s_0}(s)\sum_a\pi(a \mid s)\;\partial_\theta\ln\pi(a \mid s)\;Q(s, a),$$
où $Q$ peut être remplacé par $A$ (∂ MB8.10 ; l'outil : l'espérance nulle du score du §1, pour la loi $\pi(\cdot \mid s)$). C'est le **théorème du gradient de politique** (*policy gradient theorem*), ici sous sa forme actualisée (Sutton et Barto, §13.2, l'énoncent pour des épisodes, sans actualisation) : une moyenne, sur les états pondérés par $\boldsymbol{\nu}_{s_0}$ et sur les actions tirées de $\pi$, du score de l'action fois sa valeur.

**Le barrage.** $Q(\mathrm{H}, \mathrm{T}) = 7 + 0{,}6\,(0{,}35 \times 9{,}3570 + 0{,}65 \times 4{,}3352) \approx 10{,}6557$, et de même :

| $s$ | $Q(s, \mathrm{T})$ | $Q(s, \mathrm{R})$ | $A(s, \mathrm{T})$ | $A(s, \mathrm{R})$ | $\sum_a\pi(a \mid s)\,A(s, a)$ |
|---|---|---|---|---|---|
| H | 10,6557 | 4,1622 | 1,2987 | −5,1948 | $0{,}8 \times 1{,}2987 - 0{,}2 \times 5{,}1948 \approx 0$ |
| B | 4,9024 | 3,9570 | 0,5672 | −0,3782 | $0{,}4 \times 0{,}5672 - 0{,}6 \times 0{,}3782 \approx 0$ |

Depuis H : $\frac{\partial V(\mathrm{H})}{\partial z(\mathrm{H}, \mathrm{T})} \approx 1{,}5993 \times 0{,}8 \times 1{,}2987 \approx 1{,}6616$ et $\frac{\partial V(\mathrm{H})}{\partial z(\mathrm{B}, \mathrm{T})} \approx 0{,}9007 \times 0{,}4 \times 0{,}5672 \approx 0{,}2044$ ; les dérivées en $z(\cdot, \mathrm{R})$ sont leurs opposées. Depuis B, ces deux dérivées valent $0{,}5274$ et $0{,}4521$ : le logit de l'état B compte plus pour la valeur de B ($0{,}4521$) que pour celle de H ($0{,}2044$), car on passe plus de temps en B depuis B ($\nu_{\mathrm{B}}(\mathrm{B}) \approx 0{,}797$) que depuis H ($0{,}360$).

**Vérifier par différences finies** (M05a §5). On change $z(\mathrm{H}, \mathrm{T})$ de $\pm h$, on résout les deux systèmes, et $\frac{V^+(\mathrm{H}) - V^-(\mathrm{H})}{2h}$ redonne $1{,}6616$ pour $h = 10^{-3}$ ; l'erreur est la plus petite vers $h \approx 10^{-5}$, entre la troncature et l'arrondi (M05a §7, figure).

![À gauche, depuis H, le poids (1 − γ)γᵗ de chaque pas t (γ = 0,6), partagé entre H et B selon la loi de S_t : leur somme sur t est la loi d'occupation ν_H. Au milieu, les lois d'occupation du barrage : depuis H, 0,640 en H et 0,360 en B ; depuis B, 0,203 et 0,797. À droite, l'écart entre la différence finie centrée et la formule (1,6616) en fonction du pas h, en échelles logarithmiques : un V, minimal vers h ≈ 10⁻⁵](figures/occupation.png)

💻 **Aujourd'hui en pratique** — `policy_gradient_exact` (🔨 MB8.14) calcule $\mathbf{V}$ et les $m \times m \times K$ dérivées d'un coup, avec `np.linalg.solve` ; au-delà de quelques milliers d'états, ni $\mathbf{M}$ ni $\boldsymbol{\nu}$ ne s'écrivent, et l'on estime ce gradient par simulation.

⚠️ **Erreur classique.** Oublier le facteur $1 - \gamma$ entre $\mathbf{M}$ et $\boldsymbol{\nu}$ : les lignes de $\mathbf{M}$ somment à $\frac{1}{1 - \gamma}$, pas à 1 (pour une chaîne sans fin).

🔗 **Dans workbookIA** — le chapitre B8 énonce le théorème du gradient de politique avec l'avantage, et l'estime par simulation ; ses estimateurs usuels omettent le poids $\gamma^t$ du pas $t$, que porte $\boldsymbol{\nu}$.

## §5 · Retours à k pas et λ-retour

### Des retours qui s'arrêtent

On suit la chaîne d'une politique fixée (M26 §4) : des états $S_t$ et des récompenses $R_t$. Pour une fonction $V$ des états, les vraies valeurs ou une estimation, le **retour à $k$ pas** (*k-step return*) depuis $t$ est
$$G_t^{(k)} = \sum_{j=0}^{k-1}\gamma^jR_{t+j} + \gamma^kV(S_{t+k}) :$$
les $k$ premières récompenses, puis la valeur de l'état atteint, à la place de la suite. On dit qu'on **amorce** (*bootstrapping*) avec $V$. Quand $k \to \infty$, on retrouve le retour actualisé $G_t$ de M26 §4. Avec les erreurs TD $\delta_{t+l} = R_{t+l} + \gamma V(S_{t+l+1}) - V(S_{t+l})$ de M26 §8 :

> **Propriété.** $G_t^{(k)} - V(S_t) = \sum_{l=0}^{k-1}\gamma^l\,\delta_{t+l}$.

C'est le télescopage de M26 §8 (∂ M26.13), arrêté au pas $k$ : dans la somme, les termes en $V$ se compensent deux à deux, sauf $-V(S_t)$ et $\gamma^kV(S_{t+k})$.

### Le λ-retour

> **Définition.** Pour $0 \le \lambda < 1$, le **λ-retour** (*λ-return*) est la moyenne des retours à $k$ pas de poids $(1 - \lambda)\lambda^{k-1}$ :
> $$G_t^\lambda = (1 - \lambda)\sum_{k \ge 1}\lambda^{k-1}\,G_t^{(k)}.$$

Les poids sont positifs et de somme $(1 - \lambda)(1 + \lambda + \lambda^2 + \cdots) = 1$ (R5). Pour $\lambda = 0{,}7$ : $0{,}3$ ; $0{,}21$ ; $0{,}147$ ; $0{,}1029$… ; les retours de plus de 4 pas pèsent ensemble $\lambda^4 = 0{,}2401$, et le nombre moyen de pas vaut $\frac{1}{1 - \lambda} \approx 3{,}33$ (figure).

> **Théorème.** Si les récompenses et $V$ sont bornées et $\gamma < 1$,
> $$G_t^\lambda - V(S_t) = \sum_{l \ge 0}(\gamma\lambda)^l\,\delta_{t+l}.$$

*Démonstration.* Les poids somment à 1, donc $G_t^\lambda - V(S_t) = (1 - \lambda)\sum_{k \ge 1}\lambda^{k-1}\big(G_t^{(k)} - V(S_t)\big) = (1 - \lambda)\sum_{k \ge 1}\lambda^{k-1}\sum_{l=0}^{k-1}\gamma^l\delta_{t+l}$ par la propriété. Les $\delta$ sont bornés, et la série double converge absolument (une comparaison à une série géométrique) : on peut échanger les sommes. Le terme $\delta_{t+l}$ apparaît dans tous les $G^{(k)}$ tels que $k > l$, avec le poids total $(1 - \lambda)\sum_{k > l}\lambda^{k-1} = \lambda^l$. D'où $\sum_l\gamma^l\lambda^l\,\delta_{t+l}$. $\square$

Pour $\lambda = 0$ (avec $\lambda^0 = 1$), seul le retour à un pas compte : $G_t^0 - V(S_t) = \delta_t$. Quand $\lambda \to 1$, les poids s'étalent sur des retours de plus en plus longs, et l'on retrouve le retour complet, $\sum_l\gamma^l\delta_{t+l} = G_t - V(S_t)$, le télescopage entier de M26 §8 ; on pose $G_t^1 = G_t$.

### Ce que vaut un retour, en moyenne

**L'erreur TD et l'avantage.** Si $V = V^\pi$, en conditionnant aussi par l'action $a_t$ choisie au pas $t$ :
$$\mathbb{E}[\delta_t \mid S_t = s,\ a_t = a] = r(s, a) + \gamma\sum_{s'}\mathbf{P}[a, s, s']\,V^\pi(s') - V^\pi(s) = Q(s, a) - V(s) = A(s, a).$$
Sachant l'action, une erreur TD est en moyenne l'avantage de cette action ; sachant l'état seul, sa moyenne est le résidu de Bellman de M26 §8, nul pour $V = V^\pi$.

> **Propriété.** Si l'on amorce avec des valeurs estimées $\mathbf{W} = \mathbf{V}^\pi + \mathbf{e}$, le retour à $k$ pas a pour biais $\mathbb{E}\big[G_t^{(k)} \mid S_t = s\big] - V^\pi(s) = \gamma^k(\mathbf{P}_\pi^k\mathbf{e})(s)$, au plus $\gamma^k\lVert\mathbf{e}\rVert_\infty$ en valeur absolue.

L'outil : avec les vraies valeurs, le retour à $k$ pas a pour moyenne $V^\pi(s)$ (la troncature de M26 §8 : la suite oubliée a pour moyenne $\gamma^k(\mathbf{P}_\pi^k\mathbf{V}^\pi)(s)$) ; l'erreur ajoutée, $\gamma^ke(S_{t+k})$, a pour moyenne $\gamma^k(\mathbf{P}_\pi^k\mathbf{e})(s)$, par la loi à $k$ pas (M26 §1). Le biais du λ-retour est la moyenne de ces biais, avec les poids $(1 - \lambda)\lambda^{k-1}$ (✏️ MB8.4 le calcule pour une erreur constante).

**Le barrage.** Sous sa politique (§4), avec des valeurs estimées trop hautes de 1 en H et justes en B, $\mathbf{e} = (1 ;\ 0)$ : le retour à un pas a le biais $\gamma\,\mathbf{P}_\pi\mathbf{e} = 0{,}6\,(0{,}45 ;\ 0{,}31) = (0{,}27 ;\ 0{,}186)$. Le biais décroît ensuite comme $\gamma^k$ (figure) ; la variance, elle, croît en général avec $k$, puisque plus de récompenses aléatoires s'additionnent.

![À gauche, les poids (1 − λ)λ^(k−1) des retours à k pas dans un λ-retour, pour λ = 0,6 (0,4 ; 0,24 ; 0,144…) et λ = 0,7 (0,3 ; 0,21 ; 0,147…). À droite, sur la chaîne du barrage, avec des valeurs estimées trop hautes de 1 en H, le biais γᵏ(Pᵏe)(s) du retour à k pas depuis H (1, puis 0,27, …) et depuis B (0, puis 0,186, …), sous la borne γᵏ](figures/retours_k_pas.png)

💻 **Aujourd'hui en pratique** — on ne forme pas les retours à $k$ pas un par un, qui demanderaient chacun $k$ récompenses : les bibliothèques calculent la somme pondérée des erreurs TD du théorème.

⚠️ **Erreur classique.** Oublier le facteur $1 - \lambda$ : les poids $\lambda^{k-1}$ seuls somment à $\frac{1}{1 - \lambda}$. Croire qu'un retour à un pas est sans biais parce qu'il utilise une récompense observée : il hérite de l'erreur des valeurs, $\gamma\,(\mathbf{P}_\pi\mathbf{e})(s)$.

🔗 **Dans workbookIA** — le chapitre B8 estime des avantages par GAE : la somme $\sum_l(\gamma\lambda)^l\delta_{t+l}$ du théorème, avec des valeurs apprises.

## §6 · L'échantillonnage d'importance : poids, taille effective, poids tronqués ; estimer une KL par échantillons

### Changer de loi

On veut $\mathbb{E}_p[f(X)]$ sous une loi **cible** $p$ (*target distribution*), mais on a, ou l'on préfère, des tirages d'une autre loi $q$, la **proposition** (*proposal distribution*).

> **Théorème.** Si $q(x) > 0$ partout où $p(x)\,f(x) \ne 0$, alors $\mathbb{E}_p[f(X)] = \mathbb{E}_q[w(X)\,f(X)]$, avec le **poids d'importance** (*importance weight*) $w = \frac pq$. Pour $x_1, \ldots, x_n$ tirés indépendamment de $q$, $\frac1n\sum_iw(x_i)\,f(x_i)$ est un estimateur sans biais de $\mathbb{E}_p[f]$.

*Démonstration.* $\sum_xq(x)\,\frac{p(x)}{q(x)}\,f(x) = \sum_xp(x)\,f(x)$, les sommes portant sur les $x$ où $q > 0$, qui contiennent tous ceux où $pf \ne 0$ ; de même avec des intégrales. $\square$

- **$\mathbb{E}_q[w] = 1$** (le cas $f = 1$) si $q > 0$ partout où $p > 0$. Un tirage où $p = 0$ reçoit le poids 0, sans dommage. Si $q$ s'annule là où $p$ ne s'annule pas, ces $x$ ne sont jamais tirés : $\mathbb{E}_q[w] = P_p(q > 0) < 1$, et l'estimateur oublie la part de $\mathbb{E}_p[f]$ qui vient de là.
- **La variance** à un tirage vaut $\mathbb{E}_q[w^2f^2] - \big(\mathbb{E}_p[f]\big)^2 = \mathbb{E}_p[wf^2] - \big(\mathbb{E}_p[f]\big)^2$. Pour $f \ge 0$, la proposition $q = \frac{pf}{\mathbb{E}_p[f]}$ rend $wf$ constant, égal à $\mathbb{E}_p[f]$ : une variance nulle, mais il faudrait connaître $\mathbb{E}_p[f]$. Comme pour Horvitz-Thompson (M20 §5), tirer plus souvent ce qui compte le plus réduit la variance. À l'inverse, une proposition à queue trop **légère** peut la rendre infinie (ci-dessous, dès un taux $\theta \ge 2$).

**Deux propositions.** La cible est la loi exponentielle de taux 1, $p(x) = e^{-x}$, et la proposition celle de taux $\theta$ : $w(x) = \frac{e^{(\theta - 1)x}}{\theta}$ et
$$\mathbb{E}_q[w^2] = \int_0^\infty\frac{p(x)^2}{q(x)}\,\mathrm{d}x = \frac1\theta\int_0^\infty e^{-(2 - \theta)x}\,\mathrm{d}x = \frac{1}{\theta(2 - \theta)} \ \text{ pour } \theta < 2, \quad +\infty \text{ pour } \theta \ge 2.$$
Pour $\theta = \frac12$, une proposition à queue plus lourde que la cible, $w = 2e^{-x/2} \le 2$ et $\mathbb{V}_q(w) = \frac43 - 1 = \frac13$. Pour $\theta = 3$, $w = \frac{e^{2x}}{3}$ n'est pas borné, et sa variance est infinie : la moyenne des poids tend encore vers 1 (la loi des grands nombres demande seulement $\mathbb{E}_q[w]$ fini), mais par à-coups, au gré des rares grands $x$.

**Des poids calculés en logarithmes.** Les densités elles-mêmes peuvent s'effacer en flottants (*underflow*, M05a §8) ; on calcule $\ln w = \ln p - \ln q$, puis l'exponentielle. Quatre tirages de la proposition de taux $\frac12$, $x = 0{,}3$ ; $1{,}5$ ; $2{,}6$ ; $4{,}8$, donnent $\ln w = \ln 2 - \frac x2 \approx 0{,}5431$ ; $-0{,}0569$ ; $-0{,}6069$ ; $-1{,}7069$, et $w \approx 1{,}7214$ ; $0{,}9447$ ; $0{,}5451$ ; $0{,}1814$, de somme $3{,}3926$. Pour $f(x) = x$, dont l'espérance sous la cible vaut 1 : $\frac14\sum_iw_ix_i \approx \frac{4{,}2216}{4} \approx 1{,}0554$.

### Normaliser, mesurer, tronquer

> **Définition.** Les poids **auto-normalisés** (*self-normalized*) sont $\tilde w_i = \frac{w_i}{\sum_jw_j}$, et l'estimateur correspondant est $\sum_i\tilde w_i\,f(x_i)$.

C'est un quotient de deux moyennes : il est **biaisé** pour $n$ fini, mais **convergent** (*consistent*, M02c §6) : il tend vers $\mathbb{E}_p[f]$ quand $n \to \infty$ (la loi des grands nombres au numérateur et au dénominateur, admis). Et c'est le seul possible quand $p$ ou $q$ n'est connue qu'à une constante près, comme une loi a posteriori (M04) ou une loi de Boltzmann dont on ignore $Z$ (M17) : la constante se simplifie. Sur les quatre tirages : $\frac{4{,}2216}{3{,}3926} \approx 1{,}244$.

> **Définition** (Kish, 1965). La **taille effective** (*effective sample size*) des poids $w_1, \ldots, w_n$ est $n_{\mathrm{eff}} = \frac{(\sum_iw_i)^2}{\sum_iw_i^2}$.

Une moyenne pondérée $\sum_i\tilde w_iY_i$ de variables indépendantes de même variance $\sigma^2$, à poids fixés, a pour variance $\sigma^2\sum_i\tilde w_i^2 = \frac{\sigma^2}{n_{\mathrm{eff}}}$ : autant qu'une moyenne ordinaire de $n_{\mathrm{eff}}$ variables. Dès qu'un poids est positif, $1 \le n_{\mathrm{eff}} \le n$, avec $n_{\mathrm{eff}} = n$ si et seulement si les poids sont égaux (Cauchy-Schwarz, M07), et $n_{\mathrm{eff}}$ proche de 1 quand un poids écrase les autres. Multiplier tous les poids par un même nombre ne la change pas : les poids normalisés ont la même. Sur les quatre tirages, $n_{\mathrm{eff}} \approx \frac{3{,}3926^2}{4{,}1858} \approx 2{,}75$. Pour les propositions de taux $\theta$, $\frac{n_{\mathrm{eff}}}{n}$ tend vers $\frac{(\mathbb{E}_q[w])^2}{\mathbb{E}_q[w^2]} = \theta(2 - \theta)$ pour $\theta < 2$, au mieux 1 pour $q = p$ (figure).

> **Définition.** Les **poids tronqués** (*truncated importance weights*) au seuil $c > 0$ sont les $\min(w_i, c)$.

Bornés par $c$, ils donnent un estimateur de variance au plus $c^2\,\mathbb{E}_q[f^2]$, finie même quand celle de $wf$ ne l'est pas. En échange, un biais : $\mathbb{E}_q[\min(w, c)\,f] - \mathbb{E}_p[f] = -\mathbb{E}_q\big[(w - c)_+\,f\big]$, avec $(u)_+ = \max(u, 0)$, négatif pour $f \ge 0$ ; il disparaît quand $c \to \infty$. Pour la proposition de taux $\frac12$ et $c = 1{,}25$ : $w > 1{,}25$ quand $x < 2\ln 1{,}6 \approx 0{,}94$, et $\mathbb{E}_q[\min(w, 1{,}25)] = \frac{55}{64} \approx 0{,}859$ au lieu de 1 ; sur les quatre tirages, le premier poids devient 1,25, et l'estimation de $\mathbb{E}_p[X]$ passe de $1{,}0554$ à $1{,}0200$. Tronquer sert quand de grands poids rendent la variance énorme ou infinie ; quand $wf$ est déjà borné, comme ici ($2xe^{-x/2} \le \frac4e$), la troncature n'apporte qu'un biais : la variance de l'estimateur de $\mathbb{E}_p[X]$ passe même de $0{,}185$ à $0{,}2143$ par tirage.

![À gauche, la cible p (taux 1), deux propositions q de taux ½ et 3, et leurs poids p/q : bornés par 2 pour la proposition à queue plus lourde, explosifs pour l'autre. À droite, la taille effective par tirage en fonction du taux θ de la proposition : la courbe θ(2 − θ), maximale (1) en θ = 1 et nulle à partir de θ = 2, et sa valeur mesurée sur 2 000 tirages, proche de la courbe jusqu'à θ ≈ 1,3, au-dessus d'elle ensuite (la variance des w² est infinie dès θ ≥ 4/3), et erratique au-delà de 2](figures/importance.png)

### Estimer une KL par échantillons

On veut $\mathrm{KL}(q \,\|\, p) = \mathbb{E}_q\big[\ln\frac qp\big]$ à partir de tirages de $q$, avec $w = \frac pq$.

> **Propriété.** Si $p$ et $q$ ont le même support, $k_1 = -\ln w$ et $k_3 = (w - 1) - \ln w$ ont tous deux pour espérance $\mathrm{KL}(q \,\|\, p)$ sous $q$ : leurs moyennes sur $n$ tirages sont sans biais. $k_1$ peut être négatif ; $k_3 \ge 0$ à chaque tirage, nul seulement quand $w = 1$.

*Démonstration.* $\mathbb{E}_q[-\ln w] = \mathbb{E}_q\big[\ln\frac qp\big]$ ; et $\mathbb{E}_q[w - 1] = 0$, puisque $\mathbb{E}_q[w] = 1$ sur un même support. Enfin $-\ln$ est convexe, donc au-dessus de sa tangente en 1 (M05a §1) : $-\ln u \ge 1 - u$, soit $(u - 1) - \ln u \ge 0$, avec égalité seulement en $u = 1$. $\square$

$k_3$ est $k_1$ plus la variable de contrôle $w - 1$, d'espérance nulle (§3). Pour la proposition de taux $\frac12$ et la cible de taux 1 : $\mathrm{KL}(q \,\|\, p) = \mathbb{E}_q\big[\frac X2 - \ln 2\big] = 1 - \ln 2 \approx 0{,}3069$. Sur les quatre tirages, $k_1 = \frac x2 - \ln 2 \approx -0{,}5431$ ; $0{,}0569$ ; $0{,}6069$ ; $1{,}7069$ (moyenne $0{,}4569$), et $k_3 \approx 0{,}1783$ ; $0{,}0016$ ; $0{,}1519$ ; $0{,}8883$ (moyenne $0{,}3050$). À un tirage, $\mathbb{V}_q(k_1) = \mathbb{V}_q\big(\frac X2\big) = 1$, et un calcul d'intégrales donne $\mathbb{V}_q(k_3) = \frac13$.

💻 **Aujourd'hui en pratique** — `importance_weights` (🔨 MB8.15) prend $\ln p$ et $\ln q$ aux tirages, rend les poids, auto-normalisés ou tronqués au besoin, et la taille effective, calculée en logarithmes. Les filtres particulaires surveillent la taille effective de leurs tirages pondérés, et les rééchantillonnent quand elle tombe sous un seuil, par exemple $\frac n2$.

⚠️ **Erreur classique.** Choisir une proposition qui s'annule là où la cible ne s'annule pas, ou dont la queue est beaucoup plus légère que la sienne. Lire une grande taille effective comme une garantie : elle ne voit pas les régions que $q$ ne tire jamais.

🔗 **Dans workbookIA** — PPO, au chapitre B8, réutilise les tirages d'une ancienne politique en les pondérant par un poids d'importance calculé en logarithmes, et suit pendant l'apprentissage une KL estimée par $k_3$.

## §7 · Comparaisons par paires : le modèle de Bradley-Terry et la cote Elo

### Le modèle

Une ligue de tennis de table réunit quatre joueuses, A, B, C et D ; chaque paire s'est rencontrée 4 fois. Le tableau donne le nombre de victoires de la joueuse de la ligne contre celle de la colonne :

| | A | B | C | D | victoires $W_i$ |
|---|---|---|---|---|---|
| A | — | 3 | 2 | 4 | 9 |
| B | 1 | — | 3 | 2 | 6 |
| C | 2 | 1 | — | 3 | 6 |
| D | 0 | 2 | 1 | — | 3 |

> **Définition** (Zermelo, 1929 ; Bradley et Terry, 1952). Le **modèle de Bradley-Terry** (*Bradley-Terry model*) donne à chaque joueur $i$ une **force** (*strength*) $\beta_i$, et suppose les matchs indépendants, avec
> $$P(i \text{ bat } j) = \sigma(\beta_i - \beta_j) = \frac{e^{\beta_i}}{e^{\beta_i} + e^{\beta_j}},$$
> où $\sigma$ est la sigmoïde (R6, M13a §3). La log-vraisemblance d'un tournoi est $\ell(\boldsymbol\beta) = \sum_{i \ne j}\mathrm{wins}[i, j]\,\ln\sigma(\beta_i - \beta_j)$.

**Seules les différences comptent.** Ajouter un même nombre à toutes les forces ne change aucune probabilité : les forces ne sont **identifiées** (*identifiable*) qu'à une constante près, et l'on impose $\sum_i\beta_i = 0$.

**Une régression logistique.** Chaque match entre $i$ et $j$ est une observation de label 1 si $i$ gagne, de features $\mathbf{x} = \mathbf{e}_i - \mathbf{e}_j$ (des indicatrices) : $P(\text{label} = 1) = \sigma(\boldsymbol\beta \cdot \mathbf{x})$, sans constante. Bradley-Terry est une régression logistique sans terme constant (sans le biais $b$ de M13a §4) sur des différences d'indicatrices, et $\ell$ est sa log-vraisemblance, concave.

> **Propriété.** $\frac{\partial\ell}{\partial\beta_i} = W_i - \sum_{j \ne i}n_{ij}\,\sigma(\beta_i - \beta_j)$, avec $W_i = \sum_j\mathrm{wins}[i, j]$ et $n_{ij} = \mathrm{wins}[i, j] + \mathrm{wins}[j, i]$. Les **équations du maximum de vraisemblance** (*likelihood equations*) disent donc, pour chaque joueur : **victoires observées = victoires attendues**.

L'outil : le gradient de la log-vraisemblance d'une régression logistique, $\sum_m\big(y_m - \sigma(z_m)\big)\,\mathbf{x}_m$, que le chapitre 13 de workbookIA calcule pour la descente de gradient, avec $\mathbf{x}_m = \mathbf{e}_i - \mathbf{e}_j$.

Les forces ne dépendent donc du tableau que par les totaux $W_i$ et les nombres de matchs $n_{ij}$. Quand chaque paire a joué le même nombre de fois, le classement par les forces est le classement par les victoires (le membre de droite croît avec $\beta_i$), et deux joueuses à égalité de victoires ont la même force, même si l'une a battu l'autre 3 fois sur 4 : c'est le cas de B et C.

### Quand les forces existent

Le **graphe des victoires** a une flèche $i \to j$ quand $i$ a battu $j$ au moins une fois.

> **Théorème** (Zermelo, 1929 ; Ford, 1957 ; énoncé). Le maximum de vraisemblance existe, et il est unique sous la contrainte $\sum_i\beta_i = 0$, si et seulement si le graphe des victoires est **fortement connexe** (*strongly connected*) : depuis chaque joueur, des flèches mènent à chaque autre, comme dans une chaîne irréductible (M26 §2) ; autrement dit, quelle que soit la façon de partager les joueurs en deux groupes, quelqu'un de chaque groupe a battu quelqu'un de l'autre.

- **Un joueur invaincu** : aucune flèche n'arrive à lui. La vraisemblance augmente toujours quand sa force grandit, sans maximum : sa force n'est pas finie.
- **Deux groupes qui ne se sont jamais rencontrés** : chacun a ses forces, définies à la constante de son groupe près ; rien ne les met sur une échelle commune.

Dans la ligue, D a battu B et C, B et C ont battu A, A a battu tout le monde : le graphe est fortement connexe.

### L'algorithme de Zermelo

Avec $p_i = e^{\beta_i}$, chaque balayage remplace, pour tout $i$,
$$p_i \leftarrow \frac{W_i}{\sum_{j \ne i}\frac{n_{ij}}{p_i + p_j}},$$
puis divise les $p_i$ par leur moyenne géométrique, pour garder $\sum_i\ln p_i = 0$. Un point fixe vérifie $\sum_{j \ne i}n_{ij}\frac{p_i}{p_i + p_j} = W_i$ : les équations de vraisemblance, puisque $\frac{p_i}{p_i + p_j} = \sigma(\beta_i - \beta_j)$. Chaque balayage augmente $\ell$ (un algorithme **MM**, de minorisation-maximisation ; Hunter, 2004 ; admis).

Dans la ligue, depuis $p = (1, 1, 1, 1)$, chaque dénominateur vaut $\frac{3 \times 4}{2} = 6$ : $p = (1{,}5 ;\ 1 ;\ 1 ;\ 0{,}5)$, divisé par $0{,}75^{1/4} \approx 0{,}9306$, soit $\boldsymbol\beta \approx (0{,}477 ;\ 0{,}072 ;\ 0{,}072 ;\ -0{,}621)$. Les balayages suivants (figure) mènent à $\boldsymbol\beta \approx (0{,}8549 ;\ 0 ;\ 0 ;\ -0{,}8549)$. Vérification pour A : $4\sigma(0{,}8549) + 4\sigma(0{,}8549) + 4\sigma(1{,}7098) \approx 8 \times 0{,}7016 + 4 \times 0{,}8468 \approx 9$, ses 9 victoires. Le modèle donne à A la probabilité $0{,}8468$ de battre D.

### La cote Elo

Aux échecs, et dans beaucoup de jeux, chaque joueur a une **cote Elo** (*Elo rating*) $R_i$. Avant un match contre $j$, le **résultat espéré** (*expected score*) de $i$ est $E = \frac{1}{1 + 10^{(R_j - R_i)/400}}$ ; après, avec le résultat $S = 1$, $\frac12$ ou 0 (victoire, nul, défaite),
$$R_i \leftarrow R_i + k\,(S - E),$$
et $j$ reçoit l'opposé ; le coefficient $k$ (*K-factor*) est fixé par la fédération.

> **Propriété.** Avec $\beta = \frac{R\ln 10}{400}$, $E = \sigma(\beta_i - \beta_j)$ : Elo est un modèle de Bradley-Terry, à une autre échelle. La dérivée par rapport à $\beta_i$ de la log-vraisemblance d'un match, $S\ln\sigma(\beta_i - \beta_j) + (1 - S)\ln\sigma(\beta_j - \beta_i)$ (un nul compte pour une demi-victoire), vaut $S - \sigma(\beta_i - \beta_j)$ : l'équation de vraisemblance d'un seul match. La mise à jour d'Elo est donc un pas de **gradient stochastique** (*stochastic gradient*) sur cette log-vraisemblance, de learning rate $\frac{k\ln 10}{400}$ sur l'échelle des $\beta$.

En effet, $10^{(R_j - R_i)/400} = e^{(R_j - R_i)\ln 10/400} = e^{-(\beta_i - \beta_j)}$. **Exemple** : deux joueurs cotés 1 720 et 1 580, avec $k = 24$. Pour le premier, $E = \frac{1}{1 + 10^{-0{,}35}} \approx 0{,}6912$ (c'est $\sigma(0{,}8059)$, avec $\Delta\beta = \frac{140\ln 10}{400}$) ; il gagne $24 \times 0{,}3088 \approx 7{,}41$ points s'il l'emporte, en perd $16{,}59$ s'il perd, et en perd $4{,}59$ en cas de nul.

![À gauche, la probabilité de victoire σ(β_i − β_j) en fonction de l'écart de forces, avec en haut l'écart de cotes Elo correspondant (400/ln 10 ≈ 173,7 points par unité de β) ; un écart de 140 points donne 0,6912. À droite, les forces de la ligue de tennis de table après chaque balayage de l'algorithme de Zermelo : A monte vers 0,8549, D descend vers −0,8549, B et C, confondues, reviennent à 0](figures/bradley_terry_elo.png)

💻 **Aujourd'hui en pratique** — `bradley_terry_fit` (🔨 MB8.16) contrôle la forte connexité par des produits de matrices booléennes (M16), puis fait les balayages de Zermelo ; `sklearn.linear_model.LogisticRegression(fit_intercept=False, C=np.inf)`, sur les différences d'indicatrices, donne les mêmes forces au centrage près. Les systèmes de classement des jeux en ligne, comme Glicko, ajoutent à chaque cote une incertitude.

⚠️ **Erreur classique.** Chercher les forces d'un tournoi où une joueuse n'a jamais perdu : le maximum n'existe pas.

🔗 **Dans workbookIA** — le chapitre B8 apprend un modèle de récompense par Bradley-Terry, à partir de comparaisons par paires, et DPO reprend la même probabilité $\sigma(\cdot)$ d'une différence.

## §8 · Le principe variationnel de Gibbs : maximiser une moyenne moins β fois une KL

### Un compromis

Une fleuriste répartit ses achats au marché entre quatre fleurs : roses, tulipes, pivoines et lys, l'an dernier dans les proportions $\pi_{\mathrm{ref}} = (0{,}55 ;\ 0{,}2 ;\ 0{,}15 ;\ 0{,}1)$. Leurs bénéfices moyens par botte sont $r = (2 ;\ 1 ;\ 4 ;\ 3)$ euros. Tout miser sur les pivoines bouleverserait ses habitudes et celles de ses clients : elle cherche la répartition $\pi$ qui maximise
$$F(\pi) = \mathbb{E}_\pi[r] - \beta\,\mathrm{KL}(\pi \,\|\, \pi_{\mathrm{ref}}),$$
le bénéfice moyen moins $\beta > 0$ fois l'écart à l'an dernier.

> **Théorème** (principe variationnel de Gibbs, *Gibbs variational principle*). Pour $\beta > 0$ et toute loi $\pi$ sur les issues de $\pi_{\mathrm{ref}}$,
> $$\mathbb{E}_\pi[r] - \beta\,\mathrm{KL}(\pi \,\|\, \pi_{\mathrm{ref}}) = \beta\ln Z - \beta\,\mathrm{KL}(\pi \,\|\, \pi^\star), \qquad \pi^\star(x) = \frac{\pi_{\mathrm{ref}}(x)\,e^{r(x)/\beta}}{Z}, \qquad Z = \mathbb{E}_{\mathrm{ref}}\big[e^{r/\beta}\big].$$
> Le maximum de $F$ est atteint en $\pi^\star$ seulement, et il vaut $\beta\ln Z$.

*Démonstration.* Par définition, $\pi_{\mathrm{ref}}(x)\,e^{r(x)/\beta} = Z\,\pi^\star(x)$. Pour une loi $\pi$ nulle là où $\pi_{\mathrm{ref}}$ l'est (sinon $F(\pi) = -\infty$),
$$F(\pi) = \sum_x\pi(x)\Big[r(x) - \beta\ln\frac{\pi(x)}{\pi_{\mathrm{ref}}(x)}\Big] = -\beta\sum_x\pi(x)\ln\frac{\pi(x)}{\pi_{\mathrm{ref}}(x)\,e^{r(x)/\beta}} = -\beta\sum_x\pi(x)\ln\frac{\pi(x)}{Z\,\pi^\star(x)} = \beta\ln Z - \beta\,\mathrm{KL}(\pi \,\|\, \pi^\star).$$
Comme $\mathrm{KL}(\pi \,\|\, \pi^\star) \ge 0$, avec égalité seulement pour $\pi = \pi^\star$ (M06 §6), $F(\pi) \le \beta\ln Z$, avec égalité seulement en $\pi^\star$. $\square$

L'identité $\ln Z = \frac{F(\pi)}{\beta} + \mathrm{KL}(\pi \,\|\, \pi^\star)$ a la forme de $\ln p(\mathbf{x}) = \operatorname{ELBO}(q) + \mathrm{KL}(q \,\|\, p(\mathbf{z} \mid \mathbf{x}))$ (M25b §5) : un terme qu'on sait calculer, plus un écart positif à la meilleure loi (le corrigé du sujet B de CP6.8 l'avait noté pour la loi de Boltzmann).

**La fleuriste.** Pour $\beta = 1$, les poids $\pi_{\mathrm{ref}}\,e^{r}$ valent $0{,}55e^2 \approx 4{,}0640$ ; $0{,}2e \approx 0{,}5437$ ; $0{,}15e^4 \approx 8{,}1897$ ; $0{,}1e^3 \approx 2{,}0086$, de somme $Z \approx 14{,}8059$ : $\pi^\star \approx (0{,}2745 ;\ 0{,}0367 ;\ 0{,}5531 ;\ 0{,}1357)$, de valeur $\beta\ln Z \approx 2{,}695$ € ; la figure suit $\pi^\star$ pour tous les $\beta$. Contrôle de l'identité pour $\beta = 1$ et la loi uniforme $u$ : $\mathbb{E}_u[r] = 2{,}5$ et $\mathrm{KL}(u \,\|\, \pi_{\mathrm{ref}}) \approx 0{,}2155$, donc $F(u) \approx 2{,}2845$ ; et $\mathrm{KL}(u \,\|\, \pi^\star) \approx 0{,}4105$, avec $2{,}6950 - 0{,}4105 = 2{,}2845$ : la même valeur.

### Les deux limites

- **$\beta \to 0$** : s'écarter de $\pi_{\mathrm{ref}}$ ne coûte plus rien, et $\pi^\star$ se concentre sur les issues de plus grand bénéfice **parmi celles où $\pi_{\mathrm{ref}} > 0$** (les pivoines) ; $\beta\ln Z$ tend vers ce bénéfice maximal, 4 €, puisque $\max r + \beta\ln\pi_{\mathrm{ref}}(x^\star) \le \beta\ln Z \le \max r$, pour $x^\star$ une issue de bénéfice maximal.
- **$\beta \to \infty$** : $e^{r/\beta} \to 1$, $\pi^\star \to \pi_{\mathrm{ref}}$, et $\beta\ln Z \to \mathbb{E}_{\mathrm{ref}}[r] = 2{,}2$ € (Taylor d'ordre 1, M05a §3 : $\ln\mathbb{E}_{\mathrm{ref}}[e^{r/\beta}] \approx \frac{\mathbb{E}_{\mathrm{ref}}[r]}{\beta}$).

Entre les deux, la valeur décroît du meilleur bénéfice au bénéfice moyen de l'an dernier (figure). Réciproquement, $\pi^\star$, $\pi_{\mathrm{ref}}$ et $\beta$ déterminent $r$ sur le support de $\pi_{\mathrm{ref}}$, à une constante additive près : une constante ajoutée à $r$ se simplifie dans $Z$.

![À gauche, les quatre probabilités de la loi de Gibbs π* ∝ π_ref·e^(r/β) en fonction de β, en échelle logarithmique : les pivoines (r = 4) prennent tout quand β est petit, et chaque fleur revient vers sa part de l'an dernier (0,55 ; 0,2 ; 0,15 ; 0,1) quand β grandit. À droite, la valeur β ln Z, qui décroît de max r = 4 vers E_ref[r] = 2,2, et le bénéfice moyen E_π*[r], au-dessus d'elle](figures/gibbs.png)

### Des cas déjà vus

- **La loi de Boltzmann** (M17 §7) : $\pi_{\mathrm{ref}}$ uniforme sur $K$ issues, $r = -E$ (les énergies), $\beta = T$. Comme $\mathrm{KL}(\pi \,\|\, \text{uniforme}) = \ln K - H(\pi)$, maximiser $F$ revient à minimiser l'énergie libre $\mathbb{E}_\pi[E] - T\,H(\pi)$ : le sujet B de CP6.8, au choix, en était ce cas particulier.
- **Hedge** (M14 §4) : $\pi_{\mathrm{ref}}$ uniforme sur les experts, $r = -L_t$ (leurs losses cumulées), $\beta = \frac1\eta$ ; les poids $\mathbf{w}_t$ sont $\pi^\star$.
- **La température d'une loi** (M28 §5) : $\pi_{\mathrm{ref}}$ uniforme, $r = \ln p$, $\beta = T$ ; $\pi^\star \propto p^{1/T}$.

💻 **Aujourd'hui en pratique** — $\beta\ln Z = \beta\ln\sum_x\pi_{\mathrm{ref}}(x)\,e^{r(x)/\beta}$ se calcule par un log-sum-exp (M05a §8), sans débordement même pour un petit $\beta$ ; la même loi sert au recuit simulé (M17) et à l'apprentissage par renforcement régularisé par une KL.

⚠️ **Erreur classique.** Multiplier par $e^{\beta r}$ au lieu de $e^{r/\beta}$ : les rôles des limites s'inversent. Prendre le bénéfice moyen $\mathbb{E}_{\pi^\star}[r]$ pour la valeur : la valeur retranche $\beta\,\mathrm{KL}(\pi^\star \,\|\, \pi_{\mathrm{ref}})$. Croire que $\pi^\star$ peut donner une probabilité positive à une issue que $\pi_{\mathrm{ref}}$ exclut.

🔗 **Dans workbookIA** — le chapitre B8 pénalise par $\beta\,\mathrm{KL}(\pi \,\|\, \pi_{\mathrm{ref}})$ l'apprentissage par renforcement à partir de préférences (RLHF), admet que la meilleure loi est $\pi^\star \propto \pi_{\mathrm{ref}}\,e^{r/\beta}$, et DPO en tire sa loss.

## Les pièges classiques ⚠️ (récapitulatif)

- **Le score** : plusieurs sens du mot dans ce dépôt ; le score de la loi exponentielle dépend de son paramétrage (taux ou moyenne) ; l'espérance nulle demande un support qui ne bouge pas.
- **Dériver une espérance** : le chemin ne voit ni une indicatrice ni une loi discrète ; le score se calcule au $\theta$ où l'on dérive.
- **Réduire la variance** : $b^\star$ n'est pas $\mathbb{E}[f]$ ; une variable de contrôle demande une espérance connue ; la moyenne du groupe, tirage compris, multiplie l'estimateur par $\frac{n - 1}{n}$.
- **Les valeurs d'une politique** : $\mathbf{M}$ et $\boldsymbol\nu$ diffèrent d'un facteur $1 - \gamma$ ; les poids d'un λ-retour ont le facteur $1 - \lambda$ ; un retour amorcé hérite de l'erreur des valeurs.
- **Changer de loi** : une proposition qui ne couvre pas la cible, ou à queue trop légère ; la taille effective ne voit pas ce qui n'est jamais tiré.
- **Comparer et choisir** : pas de forces pour un invaincu ; $e^{r/\beta}$, pas $e^{\beta r}$ ; la valeur de Gibbs n'est pas le bénéfice moyen.

## Et maintenant

**Dans ce dépôt** : MB8 est le dernier chapitre de maths. Reste le projet de synthèse, « Les maths d'un algorithme, de A à Z » : un algorithme de workbookIA dérivé, implémenté et vérifié de bout en bout ; les outils de ce chapitre peuvent en être la matière.

**Dans workbookIA** : le chapitre B8 aborde l'apprentissage par renforcement moderne. Tu y reconnaîtras REINFORCE, qui estime un gradient par la méthode du score (§1, §2), et ses baselines (§3) ; le théorème du gradient de politique, l'avantage et les méthodes acteur-critique (§4) ; GAE, une moyenne d'erreurs TD comme le λ-retour (§5) ; PPO, ses poids d'importance et sa KL estimée (§6) ; le modèle de récompense appris par Bradley-Terry (§7) ; RLHF et DPO, qui partent de la loi de Gibbs (§8) ; et GRPO, avec sa baseline de groupe (§3).

## Pour aller plus loin

- S. Mohamed, M. Rosca, M. Figurnov et A. Mnih, « Monte Carlo Gradient Estimation in Machine Learning », *Journal of Machine Learning Research*, vol. 21, n° 132, 2020 : les estimateurs par le chemin et par le score, leurs hypothèses, leurs variances, et la réduction de variance (§2, §3).
- A. B. Owen, *Monte Carlo theory, methods and examples*, 2013, en ligne sur le site de l'auteur : §8.9 (*Control variates*, §3) ; §9.1 à §9.3 (échantillonnage d'importance, poids auto-normalisés, taille effective, §6).
- R. S. Sutton et A. G. Barto, *Reinforcement Learning: An Introduction*, 2ᵉ éd., MIT Press, 2018, en ligne sous licence Creative Commons : §12.1 (*The λ-return*, §5), §13.2 (*The Policy Gradient Theorem*, §4), §13.4 (*REINFORCE with Baseline*, §3).
- L. Kish, *Survey Sampling*, Wiley, 1965 : la taille effective d'un échantillon pondéré (§6).
- J. Schulman, « Approximating KL Divergence », billet de blog, 2020 (joschu.net) : les estimateurs $k_1$ et $k_3$ (§6).
- E. Zermelo, « Die Berechnung der Turnier-Ergebnisse als ein Maximumproblem der Wahrscheinlichkeitsrechnung », *Mathematische Zeitschrift*, vol. 29, 1929, p. 436-460 ; R. A. Bradley et M. E. Terry, « Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons », *Biometrika*, vol. 39, 1952, p. 324-345 (§7).
- L. R. Ford Jr., « Solution of a Ranking Problem from Binary Comparisons », *The American Mathematical Monthly*, vol. 64, n° 8, 1957, p. 28-33 : la condition d'existence des forces (§7).
- D. R. Hunter, « MM algorithms for generalized Bradley-Terry models », *The Annals of Statistics*, vol. 32, n° 1, 2004, p. 384-406 : l'algorithme de Zermelo comme algorithme MM, et sa convergence (§7).
- A. E. Elo, *The Rating of Chessplayers, Past and Present*, Arco, 1978 (§7).
- `annexes/symboles.md`, `annexes/formulaire.md` et `annexes/erreurs_frequentes.md`.
