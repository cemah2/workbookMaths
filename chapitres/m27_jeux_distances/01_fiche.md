# M27 · Jeux et distances entre lois — fiche de cours

> Une équipe prépare un match en devinant le plan de l'adversaire, qui devine le sien ; deux pêcheurs partagent un lac ; on déplace de la terre pour combler des trous. Ce chapitre traite d'abord les **jeux à deux joueurs** : le **maximin**, le **minimax** et les **points selles** ; les **stratégies mixtes** et le **théorème minimax** de von Neumann ; l'**équilibre de Nash** et l'**induction arrière** ; deux joueurs qui avancent chacun par un pas de gradient. Il passe ensuite aux **distances entre lois** : la probabilité a posteriori, meilleur prédicteur pour la log-loss ; **Jensen-Shannon**, qui plafonne à $\ln 2$ quand deux lois ne se recouvrent plus ; les **distances de Wasserstein**, le coût minimal pour transporter une loi sur une autre, calculées en dimension 1 par les quantiles ; la **distance de Fréchet** entre gaussiennes et le **biais** d'une distance estimée ; trois mesures d'une **dérive**. Le chapitre 27 de workbookIA s'en servira pour les réseaux génératifs adverses (GAN), et son bonus B7 pour surveiller un modèle en production.

| | |
|---|---|
| **Sections** | §1 à §10 |
| **Temps total estimé** | ≈ 14,7 h : lecture et calculs de la fiche ≈ 2 h 45, exercices ≈ 11 h 15, 20 flashcards ≈ 40 min (parcours essentiel ≈ 10,8 h) |
| **Prérequis** | M02a (intégrales, changement de variable, fonction de répartition et quantile $F^{-1}(u) = \inf\{x : F(x) \ge u\}$) ; M02b (espérance d'une variable discrète, indépendance, loi normale et $\Phi$, simulation par inversion $F^{-1}(U)$) ; M02c (biais d'un estimateur, variance d'une moyenne, matrice de covariance) ; M04 (formule de Bayes ; le maximum de vraisemblance d'une loi de Bernoulli est la fréquence) ; M05a (approximation $\ln(1 + x) \approx x$) ; M05b (point selle d'une fonction de deux variables, descente et montée de gradient) ; M06 (divergence KL, inégalités de Jensen et de Gibbs, Jensen-Shannon) ; M08 (p-valeur d'un test) ; M10 (programmes linéaires) ; M12c (trace, matrices semblables, théorème spectral, racine carrée d'une matrice symétrique positive) ; M13a (log-loss, et ce qu'elle devient quand la probabilité prédite tend vers 0) ; M13b (lagrangien et dualité faible, MML §7.2 lu une première fois) ; M22 (valeurs propres complexes d'une matrice $2 \times 2$, module, rotations et homothéties) ; M25a (KL entre lois continues, infinie quand le support de $q$ ne couvre pas celui de $p$) |
| **Fichiers du chapitre** | `02_exercices.md` (quiz, papier) · `03_notebook.ipynb` · `04_indices.md` · `05_solutions.md` et `05_solutions.ipynb` · `06_mes_reponses.md` · `flashcards.csv` |
| **mymath** | `distances.py` : `pure_strategy_values`, `mixed_strategy_value_2x2`, `descent_ascent_iterates`, `w2_gaussians_1d` |
| **MML** | §7.2 (*Constrained Optimization and Lagrange Multipliers*), relu ; §7.3.1 (*Linear Programming*) en option |

## Comment utiliser ce chapitre

**Ordre conseillé.**
1. `python tools/start_chapter.py M27` (sur Colab : `00_setup/COLAB.md` §2) : il copie le notebook, ta feuille de réponses et le squelette `mymath/distances.py`.
2. Section par section : lis **crayon en main** et refais chaque calcul, puis fais les exercices de la section, quiz 🧠 d'abord. Le passage de MML se lit après le §1, comme le dit le guide ci-dessous.
3. Les exercices ✏️ et 🔗 se font sur papier, dans ta copie de `06_mes_reponses.md`, puis se vérifient dans la **partie 0** du notebook. Les démonstrations ∂ se rédigent dans ta copie et se jugent avec la grille de relecture de `05_solutions.md`.

Le chapitre a deux moitiés. Les §1 à §4 traitent les jeux : le §2 s'appuie sur le §1, le §3 sur le §2, et le §4 sur l'exemple du §2. Les §5 à §10 traitent les lois : le §5 ne demande que M04, M06 (Gibbs) et M13a, le §6 que M06 ; les §7 et §8 forment un bloc, sur lequel s'appuient les §9 et §10.

| Section | Quiz 🧠 et rappels 🔁 | Papier et réflexion | Notebook |
|---|---|---|---|
| §1 Somme nulle, maximin et minimax | Q1 | M27.1 ✏️, M27.11 ∂, M27.17 📖 | M27.19 🔨 |
| §2 Stratégies mixtes, von Neumann | Q2 | M27.2 ✏️, M27.18 🗣️ | M27.20 🔨, M27.27 🐛, M27.28 🛠️ |
| §3 Nash, arbres de jeu | Q3 | M27.3 ✏️ | |
| §4 Descente-montée | Q3, R2 | M27.4 ✏️ | M27.21 🔨, M27.24 🔮 |
| §5 La probabilité a posteriori | Q4, R1 | M27.5 ✏️, M27.12 ∂ | |
| §6 Jensen-Shannon revisitée | Q4 | M27.6 ✏️, M27.13 ∂, M27.E1 💼 | |
| §7 Couplages, Wasserstein | Q5 | M27.7 ✏️ | M27.23 📦 |
| §8 Wasserstein en dimension 1 | Q5 | M27.8 ✏️, M27.14 ∂, M27.16 🔗, M27.E1 💼 | M27.22 🔨, M27.23 📦, M27.26 🎨, M27.27 🐛, M27.29 🏆 |
| §9 Fréchet, biais d'une distance estimée | Q6, R3 | M27.9 ✏️, M27.15 ∂, M27.16 🔗, M27.E2 💼 | M27.25 🔬 |
| §10 Mesurer une dérive | Q7 | M27.10 ✏️, M27.E2 💼 | M27.26 🎨 |

Parcours essentiel : tout sauf M27.13, M27.14, M27.17, M27.E2, M27.21, M27.23, M27.24, M27.25, M27.27, M27.28 et M27.29.

## Guide de lecture de MML

MML ne touche qu'un point de ce chapitre : l'inégalité minimax, qu'il emploie pour la dualité de Lagrange. Tu as lu son **§7.2** en M13b, en pensant aux contraintes ; relis-le **après le §1** de la fiche, en pensant aux jeux. Le §1 donne l'inégalité sur une matrice, avec des nombres ; le livre l'énonce pour une fonction quelconque de deux variables, en deux lignes de preuve qu'on suit mieux avec une matrice en tête, et en tire la dualité faible, que la fin du §1 relit comme un jeu.

- Dans la remarque qui suit la Définition 7.1 : l'**inégalité minimax** (*minimax inequality*) (7.23) et sa preuve par (7.24). Attention aux rôles : dans (7.23), $\mathbf{x}$ minimise et $\mathbf{y}$ maximise, alors qu'au §1 le joueur des lignes maximise.
- (7.25) à (7.27) : le maximum du lagrangien sur $\boldsymbol{\lambda} \ge \mathbf{0}$ redonne la fonction (7.18) qui vaut $+\infty$ hors des contraintes, puis la **dualité faible** (*weak duality*) vient en échangeant le min et le max.
- Survole le reste du §7.2 (la concavité de la fonction duale, les contraintes d'égalité), vu en M13b.

Le 📖 M27.17 te guide. En option, après le §2 : le **§7.3.1** (*Linear Programming*), (7.39) à (7.43), le dual d'un programme linéaire, la forme sous laquelle le §2 énonce qu'un jeu fini se résout ; exercice du livre conseillé avec lui : 7.6. MML n'a ni stratégie mixte, ni équilibre de Nash, ni distance de Wasserstein : pour la suite, la fiche est le cours.

📐 **Notations.**
- **Jeux.** $\mathbf{G} = (g_{ij})$ (en gras), de forme $(m, n)$, est la matrice des gains : $g_{ij}$ est ce que gagne le joueur des lignes (qui maximise) et ce que paie le joueur des colonnes (qui minimise), comme dans `distances.py`. Les stratégies du texte sont numérotées à partir de 1, celles de `distances.py` à partir de 0. Une stratégie mixte est un vecteur de probabilités, $\mathbf{p}$ pour les lignes et $\mathbf{q}$ pour les colonnes ; dans un jeu $2 \times 2$, $p$ et $q$ (en italique) sont les probabilités de la première ligne et de la première colonne. MML (7.23) et `descent_ascent_iterates` (§4) appellent $\mathbf{x}$ le joueur qui **minimise**. $\eta > 0$ est un pas.
- **Lois.** Au §5, $p_0$ et $p_1$ sont des densités (ou des lois discrètes), $\pi_0$ et $\pi_1$ des probabilités a priori, $t(x)$ une probabilité prédite. Aux §6 et §10, $p$ et $q$ sont des lois discrètes, et $m = \frac{p + q}{2}$. Logarithme népérien : JS, KL et PSI sont en **nats** (M06 calculait JS en bits : 1 bit $= \ln 2$ nat).
- **Transport.** $\mu$ et $\nu$ sont deux lois, $a_i$ et $b_j$ leurs masses, $\boldsymbol{\Gamma} = (\gamma_{ij})$ un plan de transport. Dans $W_p$, $p \ge 1$ est un exposant ; $W_p$ est la distance et $W_p^p$ le coût minimal. $F$ et $G$ (en italique) sont des fonctions de répartition, $F(x) = P(X \le x)$ et $F^{-1}(u) = \inf\{x : F(x) \ge u\}$ (M02a) ; $\Phi$ est celle de $\mathcal{N}(0, 1)$. La fonction $G$ n'a rien à voir avec la matrice $\mathbf{G}$. La lettre $m$ sert à trois choses (le nombre de lignes de $\mathbf{G}$, le mélange du §6, le nombre de points d'une loi au §7), comme $\mu$ (une loi ou une moyenne au §8) et $\lambda$ (un multiplicateur au §1, comme dans MML, quand M13b écrivait $\mu$ ; une valeur propre au §9) : le contexte tranche.
- **Deux lettres à double sens.** $\theta$ est un angle au §4 et un décalage aux §6 et §8 ; $\sigma$ est la sigmoïde au §5 et un écart-type ailleurs : le contexte les distingue.

Vocabulaire anglais de ce chapitre : *zero-sum game*, *payoff matrix*, *pure strategy*, *maximin*, *minimax*, *saddle point*, *value of the game*, *strictly dominated strategy*, *minimax inequality*, *weak duality*, *mixed strategy*, *expected payoff*, *best response*, *principle of indifference*, *minimax theorem*, *general-sum game*, *bimatrix game*, *Nash equilibrium*, *prisoner's dilemma*, *coordination game*, *perfect information*, *game tree*, *backward induction*, *gradient descent-ascent*, *simultaneous / alternating updates*, *bilinear game*, *posterior probability*, *proper scoring rule*, *support*, *coupling*, *transport plan*, *independent coupling*, *optimal transport*, *Wasserstein distance*, *earth mover's distance*, *Kantorovich-Rubinstein duality*, *Lipschitz function*, *quantile function*, *exchange argument*, *north-west corner rule*, *Fréchet distance*, *commuting matrices*, *data drift*, *population stability index (PSI)*, *Jeffreys divergence*, *Kolmogorov-Smirnov statistic*.

## Objectifs d'apprentissage

À la fin du chapitre, tu sais :
- **trouver** le maximin, le minimax et les points selles d'une matrice de gains, et **réduire** un jeu par dominance ;
- **calculer** les stratégies optimales et la valeur d'un jeu $2 \times 2$ par indifférence, et **énoncer** le théorème minimax de von Neumann ;
- **trouver** les équilibres de Nash d'un jeu à deux joueurs, et la valeur d'un arbre de jeu par induction arrière ;
- **prévoir**, par les valeurs propres d'un pas, si la descente-montée tourne autour d'un équilibre ou s'en éloigne ;
- **calculer** la probabilité a posteriori qui minimise la log-loss espérée, et **démontrer** qu'elle la minimise ;
- **calculer** la divergence de Jensen-Shannon de deux lois, et **expliquer** pourquoi elle plafonne à $\ln 2$ ;
- **écrire** un couplage de deux lois discrètes, **calculer** son coût, et **trouver** le plan optimal sur la droite ;
- **calculer** $W_1$ et $W_2$ en dimension 1 par les fonctions de répartition ou par les quantiles, dont $W_2$ de deux gaussiennes ;
- **calculer** la distance de Fréchet de deux gaussiennes dans un cas commutatif, et le biais d'une distance estimée sur des échantillons ;
- **mesurer** une dérive par le PSI, la statistique de Kolmogorov-Smirnov et $W_1$, et **dire** ce que chacune mesure.

## L'essentiel en 10 lignes

1. **Somme nulle** : la ligne maximise $g_{ij}$, la colonne le minimise. $\max_i\min_j g_{ij}$ (maximin) $\le \min_j\max_i g_{ij}$ (minimax), égalité si et seulement s'il y a un **point selle** (le plus petit de sa ligne, le plus grand de sa colonne) ; jouer en second ne nuit jamais ; la dualité faible est cette inégalité pour le lagrangien. Une stratégie strictement dominée se raye.
2. **Mixtes** : gain espéré $\mathbf{p}^\top\mathbf{G}\mathbf{q}$. Sans point selle, $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ a pour solution $p^\star = \frac{d - c}{\kappa}$, $q^\star = \frac{d - b}{\kappa}$, $v = \frac{ad - bc}{\kappa}$, $\kappa = a - b - c + d$, et $E(p, q) = v + \kappa(p - p^\star)(q - q^\star)$. **Von Neumann** : $\max_{\mathbf{p}}\min_{\mathbf{q}}\mathbf{p}^\top\mathbf{G}\mathbf{q} = \min_{\mathbf{q}}\max_{\mathbf{p}}\mathbf{p}^\top\mathbf{G}\mathbf{q}$ ; un jeu fini est un programme linéaire.
3. **Nash** : chaque stratégie est une meilleure réponse à l'autre. Dilemme du prisonnier : un équilibre, moins bon pour tous qu'une autre issue ; coordination : deux équilibres purs et un mixte. **Arbre** : induction arrière, max aux nœuds du premier joueur, min à ceux du second.
4. **Descente-montée** sur $\mathbf{x}^\top\mathbf{A}\mathbf{y}$ : simultanée, $\lVert\mathbf{x}\rVert^2 + \lVert\mathbf{y}\rVert^2$ ne baisse jamais (sur $xy$, valeurs propres $1 \pm i\eta$ : une spirale qui s'éloigne) ; alternée, $\lVert\mathbf{x}\rVert^2 + \lVert\mathbf{y}\rVert^2 - \eta\,\mathbf{x}^\top\mathbf{A}\mathbf{y}$ est constant (sur $xy$, déterminant 1 : une ellipse si $\eta < 2$).
5. **Log-loss** : $t^\star(x) = P(Y = 1 \mid X = x) = \frac{\pi_1p_1(x)}{\pi_1p_1(x) + \pi_0p_0(x)}$ minimise la log-loss espérée (∂ M27.12, par Gibbs) ; sans observation, la meilleure constante est la fréquence.
6. **JS** $= \frac12\mathrm{KL}(p \,\|\, m) + \frac12\mathrm{KL}(q \,\|\, m) \in [0, \ln 2]$ (∂ M27.13), égale à $\ln 2$ pour des supports disjoints, quelle que soit leur distance : aucune pente. La KL y est infinie.
7. **Transport** : un plan $\boldsymbol{\Gamma} \ge 0$ de marges $\mathbf{a}$ et $\mathbf{b}$ ; $W_p^p = \min\sum\gamma_{ij}\lvert x_i - y_j\rvert^p$, un programme linéaire ; $W_1 \le W_2$ ; $W_1 = \max\big(\mathbb{E}_\mu f - \mathbb{E}_\nu f\big)$ sur les $f$ 1-lipschitziennes.
8. **Dimension 1** : $W_1 = \int\lvert F - G\rvert$, $W_p^p = \int_0^1\lvert F^{-1}(u) - G^{-1}(u)\rvert^p\,\mathrm{d}u$ ; trier puis apparier (∂ M27.14) ; $W_2^2\big(\mathcal{N}(\mu_1, \sigma_1^2), \mathcal{N}(\mu_2, \sigma_2^2)\big) = (\mu_1 - \mu_2)^2 + (\sigma_1 - \sigma_2)^2$ ; une translation de $\theta$ : $W_p = \lvert\theta\rvert$.
9. **Fréchet** : $W_2^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \operatorname{tr}\boldsymbol{\Sigma}_1 + \operatorname{tr}\boldsymbol{\Sigma}_2 - 2\sum_i\sqrt{\lambda_i(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)}$ ; commutatif : $\lVert\Delta\boldsymbol{\mu}\rVert^2 + \sum_i(\sigma_{1,i} - \sigma_{2,i})^2$ ; invariante par une rotation commune. **Biais** : $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \frac{\operatorname{tr}\boldsymbol{\Sigma}_1}{n_1} + \frac{\operatorname{tr}\boldsymbol{\Sigma}_2}{n_2}$ (∂ M27.15).
10. **Dérive** : $\mathrm{PSI} = \sum_k(p_k - q_k)\ln\frac{p_k}{q_k} = \mathrm{KL}(p \,\|\, q) + \mathrm{KL}(q \,\|\, p) \approx \sum_k\frac{(p_k - q_k)^2}{q_k}$ ; $\mathrm{KS} = \sup\lvert F - G\rvert$, sans unité ; $W_1 = \int\lvert F - G\rvert$, dans l'unité de la variable ; $W_1 \le (b - a)\,\mathrm{KS}$ sur $[a, b]$.

## §1 · Jeux à somme nulle : matrice des gains, maximin et minimax, point selle, stratégies dominées

### Deux joueurs, des intérêts opposés

Une équipe de handball prépare un match. Elle a trois schémas d'attaque, l'adversaire trois systèmes de défense, et chacun choisit le sien sans connaître celui de l'autre. L'analyse des matchs passés donne, pour chaque paire, le nombre moyen de buts marqués sur dix attaques :

| | défense 1 | défense 2 | défense 3 |
|---|---|---|---|
| **attaque 1** | 5 | 3 | 7 |
| **attaque 2** | 4 | 2 | 1 |
| **attaque 3** | 6 | 4 | 5 |

Un but marqué par l'une est un but encaissé par l'autre : ce que l'attaque gagne, la défense le perd.

> **Définition.** Un **jeu à somme nulle** (*zero-sum game*) à deux joueurs est donné par une **matrice des gains** (*payoff matrix*) $\mathbf{G} = (g_{ij})$ de forme $(m, n)$ : quand le joueur des lignes joue $i$ et celui des colonnes $j$, le premier gagne $g_{ij}$ et le second perd $g_{ij}$. Le joueur des lignes veut $g_{ij}$ grand, celui des colonnes le veut petit. Choisir une ligne ou une colonne avec certitude, c'est jouer une **stratégie pure** (*pure strategy*).

### Le maximin et le minimax

Pour chaque ligne, le joueur des lignes calcule son plus petit gain, $\min_j g_{ij}$ : ce que cette ligne lui rapporte au moins, quoi que fasse l'autre. En jouant une ligne où ce plancher est le plus haut, il s'assure le **maximin** (*maximin*) $\max_i\min_j g_{ij}$. Pour chaque colonne, le joueur des colonnes calcule ce qu'elle peut lui coûter au plus, $\max_i g_{ij}$ ; en jouant une colonne où ce plafond est le plus bas, il ne paie jamais plus que le **minimax** (*minimax*) $\min_j\max_i g_{ij}$.

Au handball : les minimums des lignes sont 3, 1 et 4, donc le maximin vaut 4 (attaque 3) ; les maximums des colonnes sont 6, 4 et 7, donc le minimax vaut 4 (défense 2). L'attaque est sûre de 4 buts, la défense n'en concède pas plus de 4.

> **Propriétés** (∂ M27.11). Pour toute matrice, maximin $\le$ minimax. Ils sont égaux si et seulement si le jeu a un **point selle** (*saddle point*) : une case qui est la plus petite de sa ligne et la plus grande de sa colonne. Leur valeur commune est la **valeur** du jeu (*value of the game*), et deux points selles ont toujours la même valeur.

L'idée de l'inégalité : la case où se croisent une ligne qui donne le maximin et une colonne qui donne le minimax est au moins égale au minimum de sa ligne et au plus égale au maximum de sa colonne ; le ∂ M27.11 rédige le tout. Ici, la case (attaque 3, défense 2) vaut 4, le plus petit de sa ligne (6, 4, 5) et le plus grand de sa colonne (3, 2, 4) : un point selle. Aucun des deux ne voudrait changer après coup : contre la défense 2, aucune attaque ne fait mieux que la 3, et inversement. Comme la selle de M05b, la case est un minimum dans une direction et un maximum dans l'autre.

![Deux matrices de gains en couleurs. À gauche, le handball, 3 × 3 : les minimums des lignes (3, 1, 4) et les maximums des colonnes (6, 4, 7) en marge, le point selle (attaque 3, défense 2) entouré, de valeur 4 ; l'attaque 2, dominée, est barrée. À droite, le volley, 2 × 2 : minimums des lignes 40 et 45, maximums des colonnes 60 et 75, maximin 45 < minimax 60, aucun point selle](figures/matrices_gains.png)

C'est le moment de relire MML §7.2 (le guide de lecture le détaille), puis de faire le 📖 M27.17.

### L'ordre des coups compte

Au volley, le passeur envoie le ballon à l'attaquant de gauche ou à celui de droite ; le contre adverse se place d'avance d'un côté ou de l'autre. Les probabilités (en %) que l'attaque gagne le point :

| | contre à gauche | contre à droite |
|---|---|---|
| **attaque à gauche** | 40 | 75 |
| **attaque à droite** | 60 | 45 |

Minimums des lignes : 40 et 45, maximin 45 (attaquer à droite). Maximums des colonnes : 60 et 75, minimax 60 (contrer à gauche). Pas de point selle. Si l'attaque devait **annoncer** son côté, le contre s'y placerait : elle gagnerait 45 % des points, le maximin. Si le contre se montrait d'abord, il se montrerait à gauche, et l'attaque, partie à droite, gagnerait 60 % : le minimax. Sans point selle, celui qui joue **en second** gagne l'écart minimax − maximin ; chacun a donc intérêt à cacher son choix (§2).

### Les stratégies dominées

> **Définition.** La ligne $i$ est **strictement dominée** (*strictly dominated*) par la ligne $k$ si $g_{ij} < g_{kj}$ pour toute colonne $j$ : quoi que fasse l'adversaire, $k$ rapporte plus. Pour le joueur des colonnes, qui paie, la colonne $j$ est strictement dominée par la colonne $l$ si $g_{ij} > g_{il}$ pour toute ligne $i$.

Un joueur raisonnable ne joue jamais une stratégie strictement dominée : on peut la rayer, et le jeu réduit a la même valeur et les mêmes stratégies optimales (en stratégies mixtes aussi, §2). Au handball, l'attaque 2, (4, 2, 1), est dominée par l'attaque 3, (6, 4, 5). Une fois la ligne rayée, la défense 1, (5, 6), et la défense 3, (7, 5), sont dominées par la défense 2, (3, 4). Il ne reste qu'une colonne, où l'attaque choisit 4 plutôt que 3 : le point selle. Les dominances s'enchaînent : la défense 3 n'était pas dominée avant qu'on raye l'attaque 2.

⚠️ **Erreur classique.** Chercher le minimax sur les minimums des colonnes : le joueur des colonnes paie, son pire est le **maximum** de chaque colonne. Et retourner la dominance pour lui : une colonne est dominée quand elle coûte **plus** qu'une autre, partout.

### La dualité faible, un jeu

Pour minimiser $f(\mathbf{x})$ sous $g(\mathbf{x}) \le 0$ (M13b), un joueur choisit $\mathbf{x}$, l'autre un multiplicateur $\lambda \ge 0$, et le premier paie au second $\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda\,g(\mathbf{x})$.
- Si $\mathbf{x}$ annonce d'abord, $\lambda$ répond : $\max_{\lambda \ge 0}\mathcal{L}(\mathbf{x}, \lambda)$ vaut $f(\mathbf{x})$ si $g(\mathbf{x}) \le 0$, et $+\infty$ sinon. Donc $\min_{\mathbf{x}}\max_\lambda\mathcal{L}$ est le minimum cherché, le problème **primal** (MML (7.25) et (7.26)).
- Si $\lambda$ annonce d'abord, $\mathbf{x}$ répond par le minimum du lagrangien, la fonction duale $D(\lambda)$ : le joueur des multiplicateurs obtient $\max_\lambda D(\lambda)$, le problème **dual**.

L'inégalité minimax donne $\max_\lambda\min_{\mathbf{x}}\mathcal{L} \le \min_{\mathbf{x}}\max_\lambda\mathcal{L}$, la **dualité faible** (MML (7.27)) : le saut de dualité est l'avantage du joueur des multiplicateurs, qui annonce en second dans le primal. La dualité forte (un problème convexe, avec la condition de Slater) dit que cet avantage est nul ; quand le minimum est atteint, le lagrangien a un point selle.

🔗 **Dans workbookIA** — le chapitre 27 écrit l'entraînement de deux réseaux comme un jeu à somme nulle, avec un min et un max ; ce paragraphe donne le sens de ces mots sur un jeu fini.

## §2 · Stratégies mixtes : gain espéré, indifférence et théorème minimax de von Neumann

### Jouer au hasard

Au volley, une attaque qui va toujours du même côté est vite lue. Elle tire donc son côté au hasard, avec des probabilités choisies, et le contre aussi.

> **Définition.** Une **stratégie mixte** (*mixed strategy*) du joueur des lignes est un vecteur de probabilités $\mathbf{p} = (p_1, \ldots, p_m)$ ($p_i \ge 0$, $\sum_i p_i = 1$) : il joue la ligne $i$ avec la probabilité $p_i$. De même $\mathbf{q}$ pour les colonnes. Les deux tirages sont indépendants, et le **gain espéré** (*expected payoff*) du joueur des lignes vaut
> $$E(\mathbf{p}, \mathbf{q}) = \sum_i\sum_j p_i\,q_j\,g_{ij} = \mathbf{p}^\top\mathbf{G}\,\mathbf{q}.$$

Contre une stratégie $\mathbf{q}$ fixée, $(\mathbf{G}\mathbf{q})_i$ est le gain espéré de la ligne pure $i$, et $\mathbf{p}^\top(\mathbf{G}\mathbf{q})$ en est une moyenne : une **meilleure réponse** (*best response*) peut toujours être pure. De même, avec $\mathbf{p}$, le joueur des lignes s'assure $\min_j(\mathbf{p}^\top\mathbf{G})_j$, son plus petit gain espéré contre une colonne pure, et il cherche le $\mathbf{p}$ qui maximise ce minimum.

### L'indifférence, dans un jeu 2 × 2

Écrivons $\mathbf{G} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $p$ la probabilité de la première ligne et $q$ celle de la première colonne :
$$E(p, q) = pq\,a + p(1 - q)\,b + (1 - p)q\,c + (1 - p)(1 - q)\,d .$$

**Le principe d'indifférence** (*principle of indifference*). Le joueur des lignes choisit $p$ pour que l'adversaire n'ait **plus de préférence** : ses deux colonnes lui coûtent alors autant,
$$pa + (1 - p)c = pb + (1 - p)d \quad\Longleftrightarrow\quad p^\star = \frac{d - c}{a - b - c + d} ;$$
de même, $q^\star$ rend les deux lignes équivalentes, $qa + (1 - q)b = qc + (1 - q)d$, soit $q^\star = \frac{d - b}{a - b - c + d}$. On calcule $p^\star$ avec les colonnes de $\mathbf{G}$, c'est-à-dire avec ce que l'adversaire peut choisir.

**Exemple : le volley.** $a = 40$, $b = 75$, $c = 60$, $d = 45$, donc $\kappa = a - b - c + d = -50$. L'attaque va à gauche avec la probabilité $p^\star = \frac{45 - 60}{-50} = 0{,}3$ ; alors chaque placement du contre lui laisse $0{,}3 \times 40 + 0{,}7 \times 60 = 0{,}3 \times 75 + 0{,}7 \times 45 = 54$ %. Le contre se place à gauche avec la probabilité $q^\star = \frac{45 - 75}{-50} = 0{,}6$ ; alors chaque côté d'attaque gagne $0{,}6 \times 40 + 0{,}4 \times 75 = 0{,}6 \times 60 + 0{,}4 \times 45 = 54$ %. Les deux garanties se rejoignent à 54 %, entre le maximin (45) et le minimax (60). L'attaquant de gauche, le meilleur quand il n'est pas contré (75 contre 60), reçoit pourtant le moins de ballons : le contre le surveille plus souvent.

> **Théorème** (jeu $2 \times 2$ sans point selle). Si $\mathbf{G} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ n'a pas de point selle, alors $\kappa = a - b - c + d \ne 0$, $p^\star$ et $q^\star$ sont strictement entre 0 et 1, et
> $$E(p, q) = v + \kappa\,(p - p^\star)(q - q^\star), \qquad v = \frac{ad - bc}{\kappa}.$$
> Donc $p^\star$ garantit au joueur des lignes le gain espéré $v$ contre toute stratégie de l'autre, et $q^\star$ garantit au joueur des colonnes de ne pas payer plus de $v$ : ces stratégies sont **optimales**, et $v$ est la **valeur** du jeu.

*Démonstration.* (i) **Les inégalités tournent.** Si $a \ge c$, alors $a$ est le plus grand de sa colonne ; ce n'est pas un point selle, donc $a$ n'est pas le plus petit de sa ligne : $a > b$. Alors $b$ est le plus petit de sa ligne, donc pas le plus grand de sa colonne : $b < d$. Alors $d$ est le plus grand de sa colonne, donc pas le plus petit de sa ligne : $d > c$. Enfin $c$, le plus petit de sa ligne, n'est pas le plus grand de sa colonne : $c < a$. La diagonale $(a, d)$ est donc au-dessus de l'autre : $a - b$, $d - c$, $a - c$ et $d - b$ sont positifs, $\kappa = (a - b) + (d - c) > 0$, et $p^\star = \frac{d - c}{(a - b) + (d - c)}$, $q^\star = \frac{d - b}{(a - c) + (d - b)}$ sont dans $]0, 1[$. Si $a < c$, le même tour, parti de $c$, donne $b, c > a, d$ (le volley) : tous ces écarts changent de signe, $\kappa < 0$, et les deux fractions restent dans $]0, 1[$.
(ii) **L'identité.** En développant, $E(p, q) = d + (b - d)p + (c - d)q + \kappa pq$, et $v + \kappa(p - p^\star)(q - q^\star) = v + \kappa pq - (d - b)p - (d - c)q + \frac{(d - c)(d - b)}{\kappa}$. Les termes en $p$, en $q$ et en $pq$ coïncident, et $v + \frac{(d - c)(d - b)}{\kappa} = \frac{ad - bc + d^2 - bd - cd + bc}{\kappa} = \frac{d\kappa}{\kappa} = d$.
(iii) **La conclusion.** $E(p^\star, q) = v$ pour tout $q$ et $E(p, q^\star) = v$ pour tout $p$. Donc $\max_p\min_q E \ge \min_q E(p^\star, q) = v$ et $\min_q\max_p E \le \max_p E(p, q^\star) = v$. L'inégalité minimax du §1 vaut aussi pour les stratégies mixtes (même preuve) : $\max_p\min_q E \le \min_q\max_p E$. Tout est égal à $v$. $\square$

Pour le volley, $E(p, q) = 54 - 50\,(p - 0{,}3)(q - 0{,}6)$ (en %) : une selle de M05b, centrée en $(0{,}3 ;\ 0{,}6)$. La figure montre ce que chaque joueur peut garantir.

![À gauche, le gain espéré de l'attaque du volley en fonction de p, la probabilité d'attaquer à gauche : deux droites, contre le contre à gauche (60 − 20p) et contre le contre à droite (45 + 30p) ; leur minimum, en trait épais, est maximal en p* = 0,3, où il vaut 54. À droite, ce que paie le contre en fonction de q : deux droites (75 − 35q et 45 + 15q) ; leur maximum est minimal en q* = 0,6, où il vaut 54. Les niveaux 45 (maximin) et 60 (minimax) sont tracés en pointillés](figures/gain_mixte.png)

> **Théorème minimax de von Neumann** (1928 ; *minimax theorem*, admis). Pour toute matrice $\mathbf{G}$,
> $$\max_{\mathbf{p}}\,\min_{\mathbf{q}}\,\mathbf{p}^\top\mathbf{G}\,\mathbf{q} = \min_{\mathbf{q}}\,\max_{\mathbf{p}}\,\mathbf{p}^\top\mathbf{G}\,\mathbf{q} = v .$$
> Il existe des stratégies mixtes optimales $\mathbf{p}^\star$ et $\mathbf{q}^\star$ : $\mathbf{p}^\star$ garantit au moins $v$, $\mathbf{q}^\star$ au plus $v$, et maximin $\le v \le$ minimax (en stratégies pures).

Les min et max intérieurs se prennent sur les stratégies pures : $\max_{\mathbf{p}}\min_j(\mathbf{p}^\top\mathbf{G})_j = \min_{\mathbf{q}}\max_i(\mathbf{G}\mathbf{q})_i$. Une stratégie strictement dominée a une probabilité nulle dans toute stratégie optimale : on peut la rayer avant de calculer.

> **Un jeu fini est un programme linéaire** (énoncé). Le joueur des lignes résout
> $$\text{maximiser } v \quad\text{sous}\quad (\mathbf{p}^\top\mathbf{G})_j \ge v \text{ pour toute colonne } j, \qquad p_i \ge 0, \qquad \textstyle\sum_i p_i = 1,$$
> un programme linéaire en $(\mathbf{p}, v)$ (M10). Le problème du joueur des colonnes est son dual (MML §7.3.1), et l'égalité des deux optimums, la dualité forte des programmes linéaires, redonne le théorème de von Neumann.

💻 **Aujourd'hui en pratique** — un jeu de quelques milliers de stratégies se résout par ce programme linéaire (`scipy.optimize.linprog`, l'oracle des tests de `distances.py`) ; pour des jeux bien plus grands, on approche les stratégies optimales par des algorithmes itératifs.

⚠️ **Erreur classique.** Calculer $p^\star$ pour que le joueur des lignes soit indifférent : $p^\star$ rend **l'adversaire** indifférent (🐛 M27.27). Appliquer les formules d'indifférence à un jeu qui a un point selle : elles peuvent sortir de $[0, 1]$, ou diviser par zéro ; la réponse est alors le point selle, en stratégies pures (🔨 M27.20).

🔗 **Dans workbookIA** — le chapitre 27 parle d'équilibre sans en calculer ; ce paragraphe montre ce que le mot veut dire dans un jeu fini, et comment on le trouve.

## §3 · Équilibre de Nash, jeux à somme non nulle, et arbres de jeu (induction arrière)

### Quand les intérêts ne s'opposent pas tout à fait

Dans un jeu à **somme non nulle** (*general-sum game*), chaque joueur a sa matrice : $\mathbf{A}$ pour celui des lignes, $\mathbf{B}$ pour celui des colonnes (un **jeu bimatriciel**, *bimatrix game*), et chaque case porte les deux gains $(a_{ij}, b_{ij})$. Chacun maximise le sien ; la somme nulle est le cas $\mathbf{B} = -\mathbf{A}$.

> **Définition.** Un couple de stratégies, pures ou mixtes, $(\mathbf{p}^\star, \mathbf{q}^\star)$ est un **équilibre de Nash** (*Nash equilibrium*) si chacune est une meilleure réponse à l'autre : contre $\mathbf{q}^\star$, le joueur des lignes ne trouve rien de mieux que $\mathbf{p}^\star$, et contre $\mathbf{p}^\star$, le joueur des colonnes rien de mieux que $\mathbf{q}^\star$ :
> $$\mathbf{p}^\top\mathbf{A}\,\mathbf{q}^\star \le \mathbf{p}^{\star\top}\mathbf{A}\,\mathbf{q}^\star \text{ pour tout } \mathbf{p}, \qquad \mathbf{p}^{\star\top}\mathbf{B}\,\mathbf{q} \le \mathbf{p}^{\star\top}\mathbf{B}\,\mathbf{q}^\star \text{ pour tout } \mathbf{q}.$$

Comme au §2, il suffit de comparer aux stratégies pures. Nash a démontré en 1950 que tout jeu fini a au moins un équilibre, éventuellement mixte (admis). Dans un jeu à somme nulle, les équilibres de Nash sont exactement les couples de stratégies optimales du §2 ; en stratégies pures, ce sont les points selles.

**Le dilemme du prisonnier** (*prisoner's dilemma*). Deux pêcheurs exploitent le même lac ; chaque saison, chacun pêche avec modération (M) ou intensément (I). Leurs gains, en tonnes, le premier nombre pour le pêcheur des lignes :

| | M | I |
|---|---|---|
| **M** | (6, 6) | (2, 8) |
| **I** | (8, 2) | (3, 3) |

Quoi que fasse l'autre, I rapporte plus que M ($8 > 6$ et $3 > 2$) : M est strictement dominée, pour chacun. L'unique équilibre de Nash est (I, I), à 3 tonnes chacun, alors que (M, M) en donnerait 6 à chacun : un équilibre n'est pas « le meilleur pour tous », et (M, M), meilleur pour les deux, n'est pas stable : contre M, chacun a intérêt à passer à I.

**Un jeu de coordination** (*coordination game*). Deux services d'une entreprise choisissent un format de fichier, X ou Y ; ils ne gagnent rien s'ils ne choisissent pas le même, et X est le meilleur :

| | X | Y |
|---|---|---|
| **X** | (4, 4) | (0, 0) |
| **Y** | (0, 0) | (2, 2) |

(X, X) et (Y, Y) sont deux équilibres purs : contre X, le meilleur choix est X, et contre Y, c'est Y. Il y en a un troisième, mixte : chaque service choisit X avec la probabilité $x$ qui rend l'**autre** indifférent, $4x = 2(1 - x)$, soit $x = \frac13$. Chacun gagne alors en moyenne $4 \times \frac19 + 2 \times \frac49 = \frac43$, moins que dans les deux équilibres purs : ils ne tombent d'accord que 5 fois sur 9. Plusieurs équilibres, de valeurs différentes : la définition ne dit pas lequel sera joué.

### Les arbres de jeu

Aux échecs, on joue chacun son tour en voyant tout : un jeu à **information parfaite** (*perfect information*), qui se dessine comme un **arbre** (*game tree*) : un nœud par position, une branche par coup, et à chaque feuille, si la somme est nulle, un seul nombre, le gain du premier joueur.

> **L'induction arrière** (*backward induction*). On remonte des feuilles vers la racine : à un nœud où joue le premier joueur, la valeur est le **maximum** des valeurs de ses enfants ; à un nœud où joue le second, le **minimum**. La valeur de la racine est la valeur du jeu, le **minimax de l'arbre**, et les branches choisies forment des stratégies optimales pures.

**Exemple : un jeu d'allumettes.** Sept allumettes sont sur la table ; chacun à son tour en retire 1, 2 ou 3, et celui qui prend la dernière gagne. Plutôt que l'arbre entier, on remonte par le nombre d'allumettes restantes, du point de vue du joueur qui doit jouer : une position est **gagnante** si un coup mène à une position perdante pour l'adversaire, **perdante** si tous mènent à des positions gagnantes pour lui (le max et le min de l'induction, avec des gains $\pm 1$). 0 est perdante (l'adversaire vient de prendre la dernière) ; 1, 2 et 3 sont gagnantes (on prend tout) ; 4 est perdante (chaque coup laisse 3, 2 ou 1) ; 5, 6 et 7 sont gagnantes (on laisse 4) ; 8 est perdante, et ainsi de suite : les positions perdantes sont les multiples de 4. Avec 7 allumettes, le premier joueur gagne en retirant 3, puis en complétant à 4 chaque coup de l'adversaire.

⚠️ **Erreur classique.** Croire qu'un équilibre de Nash est le meilleur pour tous (le dilemme du prisonnier), ou qu'il est unique (la coordination). Calculer la probabilité d'un équilibre mixte avec ses propres gains : elle rend l'**autre** indifférent.

🔗 **Dans workbookIA** — les chapitres 26 et 27 parlent d'arbre, de somme nulle et d'équilibre : ce paragraphe donne le sens précis des trois.

## §4 · Jouer par gradients : descente-montée simultanée ou alternée sur un jeu bilinéaire

### Deux descentes qui se répondent

Quand les stratégies sont des vecteurs de nombres réels, chaque joueur avance par un pas de gradient. Soit $f(\mathbf{x}, \mathbf{y})$, que le joueur $\mathbf{x}$ veut petite et le joueur $\mathbf{y}$ grande. Un équilibre est un couple $(\mathbf{x}^\star, \mathbf{y}^\star)$ tel que $f(\mathbf{x}^\star, \mathbf{y}) \le f(\mathbf{x}^\star, \mathbf{y}^\star) \le f(\mathbf{x}, \mathbf{y}^\star)$ pour tous $\mathbf{x}$ et $\mathbf{y}$ : un minimum en $\mathbf{x}$ quand $\mathbf{y} = \mathbf{y}^\star$, un maximum en $\mathbf{y}$ quand $\mathbf{x} = \mathbf{x}^\star$, comme la case selle du §1. C'est un point selle au sens des jeux ; un point selle de M05b n'en est pas toujours un : $(0, 0)$ est un point selle de $-x^2 + y^2$, mais un maximum en $x$. La **descente-montée de gradient** (*gradient descent-ascent*), de pas $\eta > 0$, se joue de deux façons :
- **simultanée** (*simultaneous updates*) : $\mathbf{x}_{k+1} = \mathbf{x}_k - \eta\,\nabla_{\mathbf{x}}f(\mathbf{x}_k, \mathbf{y}_k)$ et $\mathbf{y}_{k+1} = \mathbf{y}_k + \eta\,\nabla_{\mathbf{y}}f(\mathbf{x}_k, \mathbf{y}_k)$, tous deux calculés depuis l'ancien couple ;
- **alternée** (*alternating updates*) : $\mathbf{x}_{k+1}$ comme ci-dessus, puis $\mathbf{y}_{k+1} = \mathbf{y}_k + \eta\,\nabla_{\mathbf{y}}f(\mathbf{x}_{k+1}, \mathbf{y}_k)$, qui voit déjà le nouveau $\mathbf{x}$.

Le cas le plus simple est le **jeu bilinéaire** (*bilinear game*) $f(\mathbf{x}, \mathbf{y}) = \mathbf{x}^\top\mathbf{A}\,\mathbf{y}$ : $\nabla_{\mathbf{x}}f = \mathbf{A}\mathbf{y}$, $\nabla_{\mathbf{y}}f = \mathbf{A}^\top\mathbf{x}$, et $(\mathbf{0}, \mathbf{0})$ est un équilibre. Il n'est pas artificiel : autour de ses stratégies optimales, un jeu $2 \times 2$ en est un, puisque $E(p, q) - v = \kappa\,(p - p^\star)(q - q^\star)$ (§2).

### Le pas simultané s'éloigne

> **Propriété.** Pour le pas simultané sur $\mathbf{x}^\top\mathbf{A}\,\mathbf{y}$,
> $$\lVert\mathbf{x}_{k+1}\rVert^2 + \lVert\mathbf{y}_{k+1}\rVert^2 = \lVert\mathbf{x}_k\rVert^2 + \lVert\mathbf{y}_k\rVert^2 + \eta^2\big(\lVert\mathbf{A}\mathbf{y}_k\rVert^2 + \lVert\mathbf{A}^\top\mathbf{x}_k\rVert^2\big) :$$
> la distance à l'équilibre ne diminue jamais.

*Démonstration.* $\lVert\mathbf{x} - \eta\mathbf{A}\mathbf{y}\rVert^2 = \lVert\mathbf{x}\rVert^2 - 2\eta\,\mathbf{x}^\top\mathbf{A}\mathbf{y} + \eta^2\lVert\mathbf{A}\mathbf{y}\rVert^2$ et $\lVert\mathbf{y} + \eta\mathbf{A}^\top\mathbf{x}\rVert^2 = \lVert\mathbf{y}\rVert^2 + 2\eta\,\mathbf{y}^\top\mathbf{A}^\top\mathbf{x} + \eta^2\lVert\mathbf{A}^\top\mathbf{x}\rVert^2$ ; les termes croisés s'annulent, car $\mathbf{y}^\top\mathbf{A}^\top\mathbf{x} = \mathbf{x}^\top\mathbf{A}\mathbf{y}$. $\square$

Sur $f(x, y) = xy$, un pas multiplie le vecteur $(x, y)$ par
$$\mathbf{M}_s = \begin{pmatrix} 1 & -\eta \\ \eta & 1 \end{pmatrix} = \sqrt{1 + \eta^2}\;\mathbf{R}_\theta, \qquad \theta = \arctan\eta ,$$
la multiplication par le complexe $1 + i\eta$ de M22 : une rotation et un agrandissement de rapport $\sqrt{1 + \eta^2}$. Ses valeurs propres $1 \pm i\eta$ ont pour module $\sqrt{1 + \eta^2} > 1$ : les itérés tournent autour de l'équilibre en s'en éloignant, une **spirale**. Pour $\eta = 0{,}2$, la distance à l'équilibre gagne un facteur $\sqrt{1{,}04} \approx 1{,}02$ par pas, et double en 35 pas environ ($1{,}04^{17{,}5} \approx 1{,}99$).

### Le pas alterné tourne en rond

Avec le pas alterné sur $xy$ : $x_{k+1} = x_k - \eta y_k$, puis $y_{k+1} = y_k + \eta x_{k+1} = \eta x_k + (1 - \eta^2)\,y_k$, soit
$$\mathbf{M}_a = \begin{pmatrix} 1 & -\eta \\ \eta & 1 - \eta^2 \end{pmatrix}, \qquad \det\mathbf{M}_a = 1, \qquad \operatorname{tr}\mathbf{M}_a = 2 - \eta^2 .$$
Pour $0 < \eta < 2$, le discriminant $(2 - \eta^2)^2 - 4 = \eta^2(\eta^2 - 4)$ est négatif : deux valeurs propres complexes conjuguées de produit 1, donc de module 1 (M22). Les itérés ne s'éloignent pas et ne se rapprochent pas : voici la courbe fermée qu'ils parcourent.

> **Propriété.** Pour le pas alterné sur $\mathbf{x}^\top\mathbf{A}\,\mathbf{y}$, la quantité
> $$Q(\mathbf{x}, \mathbf{y}) = \lVert\mathbf{x}\rVert^2 + \lVert\mathbf{y}\rVert^2 - \eta\,\mathbf{x}^\top\mathbf{A}\,\mathbf{y}$$
> garde la même valeur à chaque itération. Sur $xy$, les itérés restent sur l'ellipse $x^2 + y^2 - \eta xy = $ constante (une ellipse dès que $\eta < 2$).

*Démonstration.* Notons $\mathbf{x}' = \mathbf{x} - \eta\mathbf{A}\mathbf{y}$ et $\mathbf{y}' = \mathbf{y} + \eta\mathbf{A}^\top\mathbf{x}'$. On développe $\lVert\mathbf{y}'\rVert^2 = \lVert\mathbf{y}\rVert^2 + 2\eta\,\mathbf{x}'^\top\mathbf{A}\mathbf{y} + \eta^2\lVert\mathbf{A}^\top\mathbf{x}'\rVert^2$ et $\mathbf{x}'^\top\mathbf{A}\mathbf{y}' = \mathbf{x}'^\top\mathbf{A}\mathbf{y} + \eta\lVert\mathbf{A}^\top\mathbf{x}'\rVert^2$ : il reste $Q(\mathbf{x}', \mathbf{y}') = \lVert\mathbf{x}'\rVert^2 + \lVert\mathbf{y}\rVert^2 + \eta\,\mathbf{x}'^\top\mathbf{A}\mathbf{y}$. On remplace $\mathbf{x}'$ : $\lVert\mathbf{x}'\rVert^2 = \lVert\mathbf{x}\rVert^2 - 2\eta\,\mathbf{x}^\top\mathbf{A}\mathbf{y} + \eta^2\lVert\mathbf{A}\mathbf{y}\rVert^2$ et $\eta\,\mathbf{x}'^\top\mathbf{A}\mathbf{y} = \eta\,\mathbf{x}^\top\mathbf{A}\mathbf{y} - \eta^2\lVert\mathbf{A}\mathbf{y}\rVert^2$ ; la somme donne $Q(\mathbf{x}, \mathbf{y})$. $\square$

Comme $\lvert\mathbf{x}^\top\mathbf{A}\mathbf{y}\rvert \le \lVert\mathbf{A}\rVert_2\lVert\mathbf{x}\rVert\lVert\mathbf{y}\rVert \le \frac{\lVert\mathbf{A}\rVert_2}{2}\big(\lVert\mathbf{x}\rVert^2 + \lVert\mathbf{y}\rVert^2\big)$ (M22), $Q$ est définie positive dès que $\eta\lVert\mathbf{A}\rVert_2 < 2$, et les itérés restent bornés. Mais ils ne convergent pas : ils tournent autour de l'équilibre.

La figure fait jouer l'attaque et le contre du volley sur leurs probabilités, avec $\eta = 0{,}4$. Comme $\kappa = -0{,}5$ quand les gains sont des probabilités, c'est le jeu $xy$ avec un pas de $0{,}2$, à un changement de signe près.

![Une partie du carré des stratégies du volley, p (attaque à gauche) en abscisse, q (contre à gauche) en ordonnée, avec l'équilibre (0,3 ; 0,6) au centre. Partis du même point, à 0,08 de l'équilibre, les 60 pas simultanés font presque deux tours en s'éloignant (la distance est multipliée par 1,04³⁰ ≈ 3,2), tandis que les 60 pas alternés parcourent presque deux fois une même ellipse, presque un cercle, un peu allongée le long d'une diagonale, autour de l'équilibre](figures/descente_montee.png)

💻 **Aujourd'hui en pratique** — pour converger vers un point selle, on change la dynamique : moyenne des itérés alternés (elle converge, eux non), pas « extragradient » qui calcule le gradient en un point d'essai, un pas en avant, termes d'amortissement.

⚠️ **Erreur classique.** Croire qu'un pas plus petit fait converger le pas simultané : le module $\sqrt{1 + \eta^2}$ dépasse 1 pour tout $\eta > 0$. Croire que le pas alterné converge parce qu'il reste borné.

🔗 **Dans workbookIA** — le chapitre 27 entraîne deux réseaux à tour de rôle ; ce paragraphe étudie, sur le jeu le plus simple, ce que font deux joueurs qui avancent par gradients.

## §5 · Le meilleur prédicteur pour la log-loss : la probabilité a posteriori

### Rappel : la meilleure constante

La log-loss d'une probabilité prédite $t \in\ ]0, 1[$ pour un label $y \in \{0, 1\}$ vaut $\ell(t, y) = -\big[y\ln t + (1 - y)\ln(1 - t)\big]$ (M06, M13a) ; elle tend vers $+\infty$ quand la probabilité prédite pour la classe observée tend vers 0. Sur $n$ observations dont $k$ valent 1, la constante qui minimise la log-loss moyenne est la fréquence $t = \frac{k}{n}$ : c'est le maximum de vraisemblance $k\ln t + (n - k)\ln(1 - t)$ d'une loi de Bernoulli (∂ M04.12, ✏️ M13a.1). Le 🔁 M27.R1 te le fait refaire.

### Avec une observation : la probabilité a posteriori

Le label $Y$ vaut 1 avec la probabilité a priori $\pi_1$, et 0 avec $\pi_0 = 1 - \pi_1$ ; sachant $Y = k$, l'observation $X$ suit la loi $p_k$ (une densité ou une loi discrète). Un prédicteur est une fonction $t(x) \in\ ]0, 1[$, et sa **log-loss espérée** est $R(t) = \mathbb{E}\big[\ell(t(X), Y)\big]$, la moyenne sur le couple $(X, Y)$.

> **Théorème** (∂ M27.12). La log-loss espérée est minimale pour la **probabilité a posteriori** (*posterior probability*)
> $$t^\star(x) = P(Y = 1 \mid X = x) = \frac{\pi_1\,p_1(x)}{\pi_1\,p_1(x) + \pi_0\,p_0(x)}$$
> (la formule de Bayes, M04) : $R(t) \ge R(t^\star)$ pour tout prédicteur $t$.

L'idée : l'écart $R(t) - R(t^\star)$ s'écrit comme une moyenne, sur $X$, de divergences KL entre deux lois de Bernoulli, de paramètres $t^\star(X)$ et $t(X)$ ; l'inégalité de Gibbs (M06) les rend positives. Le ∂ M27.12 rédige la preuve, sans aucune dérivée. On dit que la log-loss est une **règle de score propre** (*proper scoring rule*) : pour la minimiser, il faut annoncer la vraie probabilité, ni plus sûre ni moins sûre.

**Exemple : deux variétés de pommes.** Un verger récolte deux variétés : A, 90 % des pommes, et B, 10 %. La masse d'une pomme A suit $\mathcal{N}(150, 10^2)$, celle d'une pomme B $\mathcal{N}(170, 10^2)$, en grammes ; $Y = 1$ pour B. Le rapport des densités vaut
$$\frac{p_A(x)}{p_B(x)} = \exp\Big(\frac{(x - 170)^2 - (x - 150)^2}{2 \times 100}\Big) = \exp\Big(-\frac{x - 160}{5}\Big), \qquad\text{d'où}\qquad t^\star(x) = \frac{1}{1 + 9\,e^{-(x - 160)/5}} ,$$
le 9 venant de $\pi_A/\pi_B = 0{,}9/0{,}1$. Une pomme de 155 g est une B avec la probabilité $t^\star(155) = \frac{1}{1 + 9e} \approx 0{,}039$ ; une de 180 g avec $\frac{1}{1 + 9e^{-4}} \approx 0{,}858$. Une pomme de 170 g, la masse moyenne des B, n'est pourtant une B qu'avec la probabilité $\frac{1}{1 + 9e^{-2}} \approx 0{,}451$ : les B sont neuf fois moins nombreuses.

Ici, $t^\star(x) = \sigma\big(0{,}2\,x - 32 - \ln 9\big)$, la sigmoïde d'une fonction affine de $x$ : avec deux gaussiennes de même écart-type, les carrés se simplifient, et la probabilité a posteriori est un modèle de régression logistique (M13a).

💻 **Aujourd'hui en pratique** — on ne connaît ni les $\pi_k$ ni les $p_k$ : un classifieur entraîné à minimiser la log-loss moyenne sur des données approche $t^\star(x)$, et c'est pourquoi ses sorties peuvent se lire comme des probabilités, à condition de vérifier qu'il est bien **calibré** (*calibrated*).

⚠️ **Erreur classique.** Oublier les priors : $t^\star(x)$ dépend de $\pi_0$ et de $\pi_1$, pas seulement des densités ; une pomme de 170 g, la masse typique des B, reste plus probablement une A. Croire qu'une prédiction plus tranchée que $t^\star$ fait mieux : elle fait toujours moins bien en moyenne.

🔗 **Dans workbookIA** — le chapitre 27 emploie la log-loss (la cross-entropy binaire) à chaque pas de son entraînement ; ce paragraphe dit ce qu'elle mesure.

## §6 · Jensen-Shannon revisitée : bornée par ln 2, aveugle quand les supports se séparent

### Une divergence bornée

Rappel de M06 : pour deux lois $p$ et $q$ et leur mélange $m = \frac{p + q}{2}$,
$$\mathrm{JS}(p, q) = \tfrac12\,\mathrm{KL}(p \,\|\, m) + \tfrac12\,\mathrm{KL}(q \,\|\, m),$$
symétrique, toujours finie, nulle seulement si $p = q$. M06 la calculait en bits ; ici, en nats, avec $\ln$. Le **support** (*support*) d'une loi est l'ensemble des issues de probabilité (ou de densité) positive.

> **Propriétés** (∂ M27.13). $0 \le \mathrm{JS}(p, q) \le \ln 2$, et $\mathrm{JS}(p, q) = \ln 2$ si et seulement si $p$ et $q$ ont des supports disjoints.

L'idée : M06 a montré que $m \ge \frac{p}{2}$ ; le ∂ M27.13 en tire la borne et étudie le cas d'égalité. En bits, la borne vaut 1 bit.

**Exemple : deux sites.** Un capteur rend un niveau 0, 1 ou 2. Sur un premier site, $p = (0{,}6 ;\ 0{,}4 ;\ 0)$ ; sur un second, $q = (0 ;\ 0{,}2 ;\ 0{,}8)$. Alors $m = (0{,}3 ;\ 0{,}3 ;\ 0{,}4)$,
$$\mathrm{KL}(p \,\|\, m) = 0{,}6\ln 2 + 0{,}4\ln\tfrac43 \approx 0{,}5310, \qquad \mathrm{KL}(q \,\|\, m) = 0{,}2\ln\tfrac23 + 0{,}8\ln 2 \approx 0{,}4734,$$
et $\mathrm{JS}(p, q) \approx 0{,}5022$ nat ($\approx 0{,}7245$ bit), sous $\ln 2 \approx 0{,}6931$. Les deux KL directes, elles, sont infinies : $p$ met de la masse en 0, où $q$ n'en met pas, et $q$ en 2, où $p$ n'en met pas (M06, M25a).

### Aveugle quand les supports se séparent

Prenons deux lois ponctuelles : $\delta_0$ (toute la masse en 0) et $\delta_\theta$ (toute la masse en $\theta$). Pour $\theta \ne 0$, leurs supports sont disjoints : $m$ met $\frac12$ en 0 et $\frac12$ en $\theta$, donc $\mathrm{KL}(\delta_0 \,\|\, m) = \ln\frac{1}{1/2} = \ln 2$, de même pour $\delta_\theta$, et $\mathrm{JS}(\delta_0, \delta_\theta) = \ln 2$, que $\theta$ vaille 0,001 ou 1 000. Vue comme une fonction de $\theta$, JS est constante sur $]0, +\infty[$ : sa **pente est nulle**, et qui ajuste $\theta$ en suivant cette pente ne reçoit aucune information sur la direction à prendre. Les KL valent $+\infty$, sans plus d'information. Pourtant, transporter $\delta_0$ sur $\delta_\theta$ coûte $\lvert\theta\rvert$ : c'est la distance de Wasserstein $W_1$ du §7, qui croît avec l'écart et garde une pente de 1.

Le même phénomène apparaît sans supports disjoints : pour $\mathcal{N}(0, 1)$ et $\mathcal{N}(\theta, 1)$, les supports se recouvrent toujours, mais JS s'approche de $\ln 2$ et s'aplatit dès que $\theta$ dépasse quelques écarts-types.

![JS en fonction du décalage θ (de 0 à 6), en nats : pour deux lois ponctuelles δ₀ et δ_θ, elle saute de 0 à ln 2 ≈ 0,693 dès que θ ≠ 0 et reste plate ; pour N(0, 1) contre N(θ, 1), elle monte en S vers ln 2 et s'aplatit au-delà de θ ≈ 4. En pointillés, sur le même graphique (échelle de droite), W₁ = θ pour les deux familles : une droite de pente 1](figures/js_plafond.png)

⚠️ **Erreur classique.** Mélanger bits et nats : la borne vaut $\ln 2 \approx 0{,}693$ nat, ou 1 bit. Croire qu'une JS proche de $\ln 2$ dit à quelle distance sont les lois : elle dit seulement qu'elles se recouvrent peu.

🔗 **Dans workbookIA** — Jensen-Shannon revient au chapitre 27, en nats ; ce paragraphe dit ce qu'elle ne voit pas, et pourquoi on lui préfère parfois une distance de Wasserstein.

## §7 · Transporter une loi sur une autre : couplages, plans de transport et distances de Wasserstein

### Le problème de Monge

En 1781, Gaspard Monge cherche comment déplacer des **déblais** pour combler des **remblais** avec le moins de travail. Sur une route droite, des tas de terre (les déblais) sont aux kilomètres 0, 2 et 3, avec 50 %, 30 % et 20 % de la terre ; deux trous à combler sont aux kilomètres 1 et 4, et en prennent 60 % et 40 %. Déplacer une masse $w$ sur une distance $d$ coûte $w\,d$.

> **Définition.** Soit $\mu$ une loi sur les points $x_1, \ldots, x_m$, de masses $a_i$, et $\nu$ une loi sur $y_1, \ldots, y_n$, de masses $b_j$. Un **couplage** (*coupling*), ou **plan de transport** (*transport plan*), est une matrice $\boldsymbol{\Gamma} = (\gamma_{ij}) \ge 0$ de forme $(m, n)$ dont les marges sont $\mathbf{a}$ et $\mathbf{b}$ :
> $$\sum_j\gamma_{ij} = a_i \ \text{(chaque départ est vidé)}, \qquad \sum_i\gamma_{ij} = b_j \ \text{(chaque arrivée est remplie)} .$$
> $\gamma_{ij}$ est la masse envoyée de $x_i$ à $y_j$, et $\Pi(\mathbf{a}, \mathbf{b})$ l'ensemble des plans. Pour un coût $c(x, y)$, le coût du plan est $\sum_{i,j}\gamma_{ij}\,c(x_i, y_j)$.

Un couplage est aussi une loi jointe : $\gamma_{ij} = P(X = x_i, Y = y_j)$, avec $X$ de loi $\mu$ et $Y$ de loi $\nu$, et son coût vaut $\mathbb{E}[c(X, Y)]$. Le **couplage indépendant** (*independent coupling*), $\gamma_{ij} = a_i b_j$, soit $\boldsymbol{\Gamma} = \mathbf{a}\mathbf{b}^\top$, est toujours admissible.

**Exemple.** Le couplage indépendant envoie chaque tas vers chaque trou en proportion :
$$\boldsymbol{\Gamma}_{\text{ind}} = \begin{pmatrix} 0{,}3 & 0{,}2 \\ 0{,}18 & 0{,}12 \\ 0{,}12 & 0{,}08 \end{pmatrix}, \quad\text{de coût}\quad 0{,}3 \times 1 + 0{,}2 \times 4 + 0{,}18 \times 1 + 0{,}12 \times 2 + 0{,}12 \times 2 + 0{,}08 \times 1 = 1{,}84$$
avec $c(x, y) = \lvert x - y\rvert$. Mieux : combler le trou du km 1 avec le tas du km 0 et un peu de celui du km 2, et le trou du km 4 avec le reste,
$$\boldsymbol{\Gamma}^\star = \begin{pmatrix} 0{,}5 & 0 \\ 0{,}1 & 0{,}2 \\ 0 & 0{,}2 \end{pmatrix}, \quad\text{de coût}\quad 0{,}5 \times 1 + 0{,}1 \times 1 + 0{,}2 \times 2 + 0{,}2 \times 1 = 1{,}2 .$$
Le §8 montrera qu'on ne fait pas mieux.

![À gauche, la route de 0 à 4 km : trois tas de terre (0,5 au km 0, 0,3 au km 2, 0,2 au km 3) au-dessus de l'axe, deux trous (0,6 au km 1, 0,4 au km 4) en dessous, et les flèches du plan optimal Γ*, d'épaisseur proportionnelle à la masse : 0,5 de 0 vers 1, 0,1 de 2 vers 1, 0,2 de 2 vers 4, 0,2 de 3 vers 4 ; aucune flèche ne croise une autre. À droite, les deux plans en matrices colorées, l'indépendant (coût 1,84) et Γ* (coût 1,2)](figures/plan_transport.png)

### Les distances de Wasserstein

> **Définition.** Pour $p \ge 1$, la **distance de Wasserstein** (*Wasserstein distance*) d'ordre $p$ est
> $$W_p(\mu, \nu) = \Big(\min_{\boldsymbol{\Gamma} \in \Pi(\mathbf{a}, \mathbf{b})}\ \sum_{i,j}\gamma_{ij}\,\lvert x_i - y_j\rvert^p\Big)^{1/p} = \Big(\min\ \mathbb{E}\lvert X - Y\rvert^p\Big)^{1/p},$$
> le second minimum portant sur les couplages de $\mu$ et $\nu$ ; $W_p^p$ est le **coût minimal**.

Elle se définit de même dans $\mathbb{R}^d$, avec $\lVert x - y\rVert$, et pour des lois continues, dont les couplages sont les lois jointes de marges $\mu$ et $\nu$. C'est une distance sur les lois de moment d'ordre $p$ fini (admis) : positive, symétrique, nulle seulement si $\mu = \nu$, avec l'inégalité triangulaire. $W_1$ s'appelle aussi *earth mover's distance*, la distance du terrassier. Pour la terre, $W_1 = 1{,}2$ km (les masses ont pour somme 1) ; avec le coût $(x - y)^2$, $\boldsymbol{\Gamma}^\star$ coûte $0{,}5 + 0{,}1 + 0{,}2 \times 4 + 0{,}2 = 1{,}6$, et le §8 montrera qu'il est encore optimal : $W_2 = \sqrt{1{,}6} \approx 1{,}26$ km.

> **Un programme linéaire** (énoncé). Les inconnues $\gamma_{ij}$, le coût $\sum\gamma_{ij}c_{ij}$ et les contraintes (les marges, $\gamma_{ij} \ge 0$) sont linéaires : le **transport optimal** (*optimal transport*) est un programme linéaire (M10), à $mn$ inconnues et $m + n$ contraintes d'égalité ; le 📦 M27.23 le résout avec `linprog`.

### Deux propriétés

> **$W_1 \le W_2$.** Soit $(X, Y)$ un couplage optimal pour $W_2$. Par Jensen (M06), $\big(\mathbb{E}\lvert X - Y\rvert\big)^2 \le \mathbb{E}\lvert X - Y\rvert^2 = W_2^2$ ; et $W_1 \le \mathbb{E}\lvert X - Y\rvert$, puisque $W_1$ est un minimum sur les couplages. Donc $W_1 \le W_2$. (Plus généralement, $W_p$ croît avec $p$.)

Pour la terre : $1{,}2 \le \sqrt{1{,}6}$.

> **Dualité de Kantorovich-Rubinstein** (*Kantorovich-Rubinstein duality*, énoncée). $W_1(\mu, \nu) = \max_f\big(\mathbb{E}_\mu[f(X)] - \mathbb{E}_\nu[f(Y)]\big)$, le maximum portant sur les fonctions **1-lipschitziennes** (*1-Lipschitz*) : $\lvert f(x) - f(y)\rvert \le \lvert x - y\rvert$ pour tous $x, y$.

Une inégalité est immédiate : pour tout couplage, $\mathbb{E}f(X) - \mathbb{E}f(Y) = \mathbb{E}[f(X) - f(Y)] \le \mathbb{E}\lvert X - Y\rvert$, et l'on prend le couplage optimal. Chaque $f$ donne donc une minoration de $W_1$ ; l'égalité, admise, dit que la meilleure l'atteint. Pour la terre, $f(x) = -x$ donne $\mathbb{E}_\nu[Y] - \mathbb{E}_\mu[X] = 2{,}2 - 1{,}2 = 1 \le W_1 = 1{,}2$ : le déplacement moyen n'est qu'une minoration.

⚠️ **Erreur classique.** Oublier une marge : un plan doit vider chaque départ **et** remplir chaque arrivée. Confondre $W_2$ et $W_2^2$. Prendre $\lvert\mathbb{E}X - \mathbb{E}Y\rvert$ pour $W_1$ : ce n'est qu'une minoration.

🔗 **Dans workbookIA** — le chapitre 27 mesure par $W_1$ l'écart entre deux échantillons de la droite ; ce paragraphe en donne la définition par les couplages.

## §8 · Wasserstein en dimension 1 : fonctions de répartition, quantiles, appariement trié, deux gaussiennes

### Le couplage des quantiles

Sur la droite, pas besoin de programme linéaire : il suffit de ranger les deux lois dans l'ordre.

> **Théorème** (admis en général). Soit $\mu$ et $\nu$ deux lois sur $\mathbb{R}$, de fonctions de répartition $F$ et $G$, et $U$ de loi $\mathcal{U}([0 ; 1])$. Le couple $\big(F^{-1}(U), G^{-1}(U)\big)$ est un couplage de $\mu$ et $\nu$ (M02b : $F^{-1}(U)$ suit $\mu$), et il est optimal pour tout $p \ge 1$ :
> $$W_p^p(\mu, \nu) = \int_0^1\big\lvert F^{-1}(u) - G^{-1}(u)\big\rvert^p\,\mathrm{d}u .$$
> Pour $p = 1$, c'est aussi l'aire entre les deux fonctions de répartition : $W_1(\mu, \nu) = \displaystyle\int_{-\infty}^{+\infty}\lvert F(x) - G(x)\rvert\,\mathrm{d}x$.

Le couplage des quantiles envoie le premier centile de $\mu$ sur le premier de $\nu$, le deuxième sur le deuxième, etc. : deux trajets ne se croisent jamais. Les deux formules de $W_1$ mesurent la même aire, vue entre $F^{-1}$ et $G^{-1}$ ou entre $F$ et $G$ (la symétrie par rapport à la diagonale échange les axes).

> **L'appariement trié** (∂ M27.14). Pour deux échantillons de même taille $n$, $x_1, \ldots, x_n$ et $y_1, \ldots, y_n$, apparier le plus petit $x$ avec le plus petit $y$, le deuxième avec le deuxième, etc., minimise $\sum_i\lvert x_i - y_{\sigma(i)}\rvert$ et $\sum_i(x_i - y_{\sigma(i)})^2$ parmi les appariements $\sigma$.

C'est le théorème pour deux lois uniformes sur $n$ points, dont les quantiles sont les valeurs triées. L'idée est un **argument d'échange** (*exchange argument*) : si deux paires se croisent, décroiser ne coûte jamais plus. Par exemple, pour $x = (2, 5)$ et $y = (3, 9)$, l'appariement trié coûte $1 + 4 = 5$ et l'appariement croisé $7 + 2 = 9$ ; en carrés, $1 + 16 = 17$ contre $49 + 4 = 53$. Le ∂ M27.14 le démontre pour deux paires, puis pour $n$.

**Exemple : la terre de Monge.** $F$ (les tas) vaut 0,5 sur $[0 ; 2[$, 0,8 sur $[2 ; 3[$ et 1 ensuite ; $G$ (les trous) vaut 0 avant 1, 0,6 sur $[1 ; 4[$ et 1 ensuite. Donc $\lvert F - G\rvert$ vaut 0,5 sur $[0 ; 1[$, 0,1 sur $[1 ; 2[$, 0,2 sur $[2 ; 3[$ et 0,4 sur $[3 ; 4[$, et
$$W_1 = 0{,}5 + 0{,}1 + 0{,}2 + 0{,}4 = 1{,}2 ,$$
le coût de $\boldsymbol{\Gamma}^\star$. Ce plan est le couplage des quantiles : pour $u \in\ ]0 ; 0{,}5]$, $F^{-1}(u) = 0$ et $G^{-1}(u) = 1$ ; pour $u \in\ ]0{,}5 ; 0{,}6]$, 2 et 1 ; pour $u \in\ ]0{,}6 ; 0{,}8]$, 2 et 4 ; pour $u \in\ ]0{,}8 ; 1]$, 3 et 4 : les masses 0,5, 0,1, 0,2 et 0,2 de $\boldsymbol{\Gamma}^\star$. Il est donc optimal pour tout $p$, et $W_2^2 = 1{,}6$. Ce plan se construit aussi par la **règle du coin nord-ouest** (*north-west corner rule*) : les points rangés dans l'ordre croissant, on remplit la matrice depuis la case en haut à gauche, en mettant chaque fois la plus grande masse possible, puis en descendant si la ligne est vide ou en allant à droite si la colonne est pleine.

![À gauche, les fonctions de répartition en escalier des tas (F) et des trous (G) sur [−0,5 ; 4,5], et l'aire entre elles, hachurée par tranches : 0,5 + 0,1 + 0,2 + 0,4 = 1,2 = W₁. À droite, les fonctions quantiles F⁻¹ et G⁻¹ sur ]0 ; 1], en escalier, et la même aire entre elles, par tranches de u de largeurs 0,5, 0,1, 0,2 et 0,2](figures/repartition_quantiles.png)

### Deux gaussiennes, une translation

Pour $\mathcal{N}(\mu, \sigma^2)$, la **fonction quantile** (*quantile function*) est $F^{-1}(u) = \mu + \sigma\,\Phi^{-1}(u)$ (M02b). Avec $Z = \Phi^{-1}(U)$, de loi $\mathcal{N}(0, 1)$ :
$$W_2^2 = \int_0^1\big(\mu_1 - \mu_2 + (\sigma_1 - \sigma_2)\Phi^{-1}(u)\big)^2\mathrm{d}u = (\mu_1 - \mu_2)^2 + 2(\mu_1 - \mu_2)(\sigma_1 - \sigma_2)\,\mathbb{E}[Z] + (\sigma_1 - \sigma_2)^2\,\mathbb{E}[Z^2],$$
et $\mathbb{E}[Z] = 0$, $\mathbb{E}[Z^2] = 1$. D'où :

> $$W_2\big(\mathcal{N}(\mu_1, \sigma_1^2), \mathcal{N}(\mu_2, \sigma_2^2)\big) = \sqrt{(\mu_1 - \mu_2)^2 + (\sigma_1 - \sigma_2)^2}\,,$$
> la distance euclidienne entre les points $(\mu_1, \sigma_1)$ et $(\mu_2, \sigma_2)$ du plan (moyenne, écart-type).

**Exemple.** Le temps de trajet suit $\mathcal{N}(31, 4^2)$ par un itinéraire et $\mathcal{N}(36 ;\ 2{,}5^2)$ par l'autre, en minutes : $W_2 = \sqrt{5^2 + 1{,}5^2} = \sqrt{27{,}25} \approx 5{,}22$ minutes.

> **Une translation.** Si $Y = X + \theta$, alors $G^{-1}(u) = F^{-1}(u) + \theta$, et $W_p = \lvert\theta\rvert$ pour tout $p \ge 1$, quelle que soit la loi de $X$.

💻 **Aujourd'hui en pratique** — en dimension 1, $W_p$ entre deux échantillons se calcule par un tri, donc très vite. En dimension $d \ge 2$, plus de tri : on résout le programme linéaire, ou une version régularisée, bien plus rapide (Peyré et Cuturi, ch. 4).

⚠️ **Erreur classique.** Apparier deux échantillons dans l'ordre où ils arrivent, sans les trier. Mettre des variances dans la formule des gaussiennes : $(\sigma_1^2 - \sigma_2^2)^2$ n'est pas $(\sigma_1 - \sigma_2)^2$ (🐛 M27.27 pour les deux). Lire $F$ quand il faut $F^{-1}$ : l'aire entre $F$ et $G$ donne $W_1$, pas $W_2$.

🔗 **Dans workbookIA** — le chapitre 27 calcule $W_1$ en dimension 1 ; tu sais maintenant pourquoi trier suffit.

## §9 · La distance de Fréchet entre gaussiennes, et le biais d'une distance estimée

### La formule

> **Théorème** (admis en général). Pour deux gaussiennes $\mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)$ et $\mathcal{N}(\boldsymbol{\mu}_2, \boldsymbol{\Sigma}_2)$ de $\mathbb{R}^d$,
> $$W_2^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \operatorname{tr}\Big(\boldsymbol{\Sigma}_1 + \boldsymbol{\Sigma}_2 - 2\,\big(\boldsymbol{\Sigma}_1^{1/2}\boldsymbol{\Sigma}_2\boldsymbol{\Sigma}_1^{1/2}\big)^{1/2}\Big).$$

La distance $W_2$ entre deux gaussiennes s'appelle aussi leur **distance de Fréchet** (*Fréchet distance*) ; la formule en donne le carré, et en dimension 1, c'est le carré de la formule du §8. On l'écrit souvent avec $\operatorname{tr}\big((\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)^{1/2}\big)$ : les deux traces sont égales, et voici pourquoi.

> **Propriété.** Si $\boldsymbol{\Sigma}_1$ est définie positive, $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2$ est semblable à la matrice symétrique semi-définie positive $\mathbf{S} = \boldsymbol{\Sigma}_1^{1/2}\boldsymbol{\Sigma}_2\boldsymbol{\Sigma}_1^{1/2}$. Ses valeurs propres $\lambda_i$ sont donc réelles et positives, et $\operatorname{tr}(\mathbf{S}^{1/2}) = \sum_i\sqrt{\lambda_i(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)}$.

*Démonstration.* $\boldsymbol{\Sigma}_1^{1/2}$ est inversible (M12c) et $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2 = \boldsymbol{\Sigma}_1^{1/2}\big(\boldsymbol{\Sigma}_1^{1/2}\boldsymbol{\Sigma}_2\boldsymbol{\Sigma}_1^{1/2}\big)\boldsymbol{\Sigma}_1^{-1/2} = \boldsymbol{\Sigma}_1^{1/2}\,\mathbf{S}\,\boldsymbol{\Sigma}_1^{-1/2}$ : les deux matrices sont semblables, donc ont les mêmes valeurs propres (M12c). $\mathbf{S}$ est symétrique et $\mathbf{x}^\top\mathbf{S}\mathbf{x} = (\boldsymbol{\Sigma}_1^{1/2}\mathbf{x})^\top\boldsymbol{\Sigma}_2(\boldsymbol{\Sigma}_1^{1/2}\mathbf{x}) \ge 0$ : ses valeurs propres sont positives, et $\mathbf{S}^{1/2}$ a pour valeurs propres leurs racines (M12c), dont la somme est sa trace. $\square$

**Exemple.** $\boldsymbol{\Sigma}_1 = \operatorname{diag}(3, 2)$ et $\boldsymbol{\Sigma}_2 = \begin{pmatrix} 5 & 1 \\ 1 & 5 \end{pmatrix}$ ne commutent pas. $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2 = \begin{pmatrix} 15 & 3 \\ 2 & 10 \end{pmatrix}$, non symétrique, a pour trace 25 et pour déterminant 144 ; ses valeurs propres, $\frac{25 \pm 7}{2}$, soit 16 et 9, sont bien réelles et positives, et $\sum_i\sqrt{\lambda_i} = 4 + 3 = 7$. Avec des moyennes égales, $W_2^2 = 5 + 10 - 2 \times 7 = 1$.

### Le cas commutatif

Supposons $\boldsymbol{\Sigma}_1$ et $\boldsymbol{\Sigma}_2$ diagonales dans une même base orthonormée $\mathbf{u}_1, \ldots, \mathbf{u}_d$ (elles commutent alors : des **matrices qui commutent**, *commuting matrices*) : $\boldsymbol{\Sigma}_k\mathbf{u}_i = \sigma_{k,i}^2\,\mathbf{u}_i$.

> **Propriété** (cas commutatif). $W_2^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \sum_i(\sigma_{1,i} - \sigma_{2,i})^2$ : la somme des $W_2^2$ en dimension 1 le long des axes communs.

*Démonstration.* Écrivons les coordonnées dans la base $(\mathbf{u}_i)$ : $X'_i = \mathbf{u}_i^\top X$ pour $X$ de loi $\mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)$, et de même $Y'_i$. Les $X'_i$ sont des gaussiennes indépendantes $\mathcal{N}(\mathbf{u}_i^\top\boldsymbol{\mu}_1, \sigma_{1,i}^2)$ (M25a), et $\lVert X - Y\rVert^2 = \sum_i(X'_i - Y'_i)^2$. **Minoration** : pour tout couplage, $\mathbb{E}(X'_i - Y'_i)^2$ est au moins le $W_2^2$ en dimension 1 de ces deux gaussiennes, $\big(\mathbf{u}_i^\top(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2)\big)^2 + (\sigma_{1,i} - \sigma_{2,i})^2$ (§8) ; on somme, et Pythagore dans la base $(\mathbf{u}_i)$ donne $\sum_i\big(\mathbf{u}_i^\top(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2)\big)^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2$. **Égalité** : avec un même $\mathbf{z}$ de loi $\mathcal{N}(\mathbf{0}, \mathbf{I})$, $X'_i = \mathbf{u}_i^\top\boldsymbol{\mu}_1 + \sigma_{1,i}z_i$ et $Y'_i = \mathbf{u}_i^\top\boldsymbol{\mu}_2 + \sigma_{2,i}z_i$ forment un couplage qui atteint la somme. $\square$

> **Invariance par une rotation commune.** Pour une matrice orthogonale $\mathbf{R}$ et un vecteur $\mathbf{c}$, les lois de $\mathbf{R}X + \mathbf{c}$ et de $\mathbf{R}Y + \mathbf{c}$ sont à la même distance $W_2$ que celles de $X$ et de $Y$ : $\lVert(\mathbf{R}\mathbf{x} + \mathbf{c}) - (\mathbf{R}\mathbf{y} + \mathbf{c})\rVert = \lVert\mathbf{x} - \mathbf{y}\rVert$, et chaque couplage de l'un donne un couplage de l'autre, de même coût. Pour des gaussiennes, $\mathcal{N}(\boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)$ devient $\mathcal{N}(\mathbf{R}\boldsymbol{\mu}_k + \mathbf{c}, \mathbf{R}\boldsymbol{\Sigma}_k\mathbf{R}^\top)$.

**Exemple.** $\boldsymbol{\Sigma}_1 = \begin{pmatrix} 13 & 12 \\ 12 & 13 \end{pmatrix}$ et $\boldsymbol{\Sigma}_2 = \begin{pmatrix} 12{,}5 & -3{,}5 \\ -3{,}5 & 12{,}5 \end{pmatrix}$ ont les mêmes vecteurs propres $\mathbf{u}_1 = \frac{1}{\sqrt2}(1, 1)$ et $\mathbf{u}_2 = \frac{1}{\sqrt2}(1, -1)$ : $\boldsymbol{\Sigma}_1\mathbf{u}_1 = 25\,\mathbf{u}_1$, $\boldsymbol{\Sigma}_1\mathbf{u}_2 = \mathbf{u}_2$, $\boldsymbol{\Sigma}_2\mathbf{u}_1 = 9\,\mathbf{u}_1$, $\boldsymbol{\Sigma}_2\mathbf{u}_2 = 16\,\mathbf{u}_2$. Les écarts-types sont 5 et 1 d'un côté, 3 et 4 de l'autre : les covariances apportent $(5 - 3)^2 + (1 - 4)^2 = 13$. Avec les moyennes $(0, 0)$ et $(3, 3)$, décalées le long de $\mathbf{u}_1$, $W_2^2 = 18 + 13 = 31$ et $W_2 \approx 5{,}57$. Ce sont deux gaussiennes à covariances diagonales, $\operatorname{diag}(25, 1)$ et $\operatorname{diag}(9, 16)$, tournées ensemble de 45°.

![Deux paires d'ellipses à 2 écarts-types. À gauche, l'exemple non commutatif : diag(3, 2), alignée sur les axes, et la matrice [[5, 1], [1, 5]], aux axes inclinés à 45° ; W₂² = 1 à moyennes égales. À droite, l'exemple commutatif : les deux ellipses ont les mêmes axes, inclinés à 45° (écarts-types 5 et 1, puis 3 et 4), et des centres (0, 0) et (3, 3) ; W₂² = 18 + 13 = 31](figures/frechet_ellipses.png)

### Le biais d'une distance estimée

On ne connaît pas $\boldsymbol{\mu}_1$ et $\boldsymbol{\mu}_2$ : on les estime par les moyennes $\bar{\mathbf{x}}_1$ et $\bar{\mathbf{x}}_2$ de deux échantillons indépendants, de tailles $n_1$ et $n_2$ et de covariances $\boldsymbol{\Sigma}_1$ et $\boldsymbol{\Sigma}_2$, et l'on calcule $\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2$.

> **Propriété** (∂ M27.15). $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \dfrac{\operatorname{tr}\boldsymbol{\Sigma}_1}{n_1} + \dfrac{\operatorname{tr}\boldsymbol{\Sigma}_2}{n_2}$.

L'idée : $\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2$ a pour moyenne $\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2$ et pour covariance $\frac{\boldsymbol{\Sigma}_1}{n_1} + \frac{\boldsymbol{\Sigma}_2}{n_2}$ (M02c) ; il reste à relier $\mathbb{E}\lVert\mathbf{v}\rVert^2$ à la moyenne et à la covariance d'un vecteur aléatoire $\mathbf{v}$, ce que fait le ∂ M27.15.

La distance estimée est donc **biaisée vers le haut** : entre deux échantillons d'une **même** loi, elle vaut en moyenne $\operatorname{tr}\boldsymbol{\Sigma}\,\big(\frac{1}{n_1} + \frac{1}{n_2}\big) > 0$. **Exemple.** Un anémomètre mesure le vent $(u, v)$ en m/s, avec des écarts-types 2 et 1,5 : $\operatorname{tr}\boldsymbol{\Sigma} = 6{,}25$ (m/s)². Pour deux échantillons de 25 relevés d'un même vent, $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 = 6{,}25 \times \big(\frac{1}{25} + \frac{1}{25}\big) = 0{,}5$ (m/s)² ; pour 25 relevés contre 125, $0{,}25 + 0{,}05 = 0{,}3$. Le biais dépend des tailles : deux distances estimées ne se comparent qu'**à tailles égales**, ou après en avoir retiré une estimation du biais.

⚠️ **Erreur classique.** Prendre la racine de $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2$ coefficient par coefficient (M12c). Ajouter $\operatorname{tr}\boldsymbol{\Sigma}_1 + \operatorname{tr}\boldsymbol{\Sigma}_2$ sans retrancher le terme croisé. Comparer deux distances estimées sur des échantillons de tailles différentes.

🔗 **Dans workbookIA** — le chapitre 27 utilise la distance de Fréchet entre deux gaussiennes ; il en admet la formule, que ce paragraphe démontre dans le cas commutatif.

## §10 · Mesurer une dérive : PSI, Kolmogorov-Smirnov et W₁

### Une variable qui glisse

Les données d'un modèle en production peuvent changer de loi sans prévenir : c'est une **dérive** (*data drift*). On compare la loi d'une variable sur une période de **référence** à sa loi d'aujourd'hui. Exemple : le nombre d'articles par commande d'un site marchand, de 1 à 4 (4 voulant dire « 4 ou plus »). En janvier, la référence, les proportions sont $q = (0{,}42 ;\ 0{,}33 ;\ 0{,}16 ;\ 0{,}09)$ ; en juin, $p = (0{,}37 ;\ 0{,}32 ;\ 0{,}19 ;\ 0{,}12)$. Trois mesures, trois regards.

### Le PSI, une divergence de Jeffreys

> **Définition.** Pour une variable répartie en classes $k$, de proportions $q_k$ (référence) et $p_k$ (aujourd'hui), toutes positives, l'**indice de stabilité de population** (*population stability index*, PSI) vaut
> $$\mathrm{PSI} = \sum_k(p_k - q_k)\ln\frac{p_k}{q_k} .$$

> **Propriété.** $\mathrm{PSI} = \mathrm{KL}(p \,\|\, q) + \mathrm{KL}(q \,\|\, p)$, la **divergence de Jeffreys** (*Jeffreys divergence*) : une KL symétrisée, positive, nulle seulement si $p = q$.

*Démonstration.* $\sum_k(p_k - q_k)\ln\frac{p_k}{q_k} = \sum_k p_k\ln\frac{p_k}{q_k} - \sum_k q_k\ln\frac{p_k}{q_k} = \mathrm{KL}(p \,\|\, q) + \sum_k q_k\ln\frac{q_k}{p_k}$. $\square$

> **Un petit décalage.** Si $p_k = q_k + \varepsilon_k$ avec $\lvert\varepsilon_k\rvert$ petit devant $q_k$, alors $\ln\frac{p_k}{q_k} = \ln\big(1 + \frac{\varepsilon_k}{q_k}\big) \approx \frac{\varepsilon_k}{q_k}$ (M05a), donc $\mathrm{PSI} \approx \sum_k\frac{(p_k - q_k)^2}{q_k}$.

**Exemple.** $\mathrm{PSI} = -0{,}05\ln\frac{0{,}37}{0{,}42} - 0{,}01\ln\frac{0{,}32}{0{,}33} + 0{,}03\ln\frac{0{,}19}{0{,}16} + 0{,}03\ln\frac{0{,}12}{0{,}09} \approx 0{,}0204$ nat, et l'approximation donne $\frac{0{,}0025}{0{,}42} + \frac{0{,}0001}{0{,}33} + \frac{0{,}0009}{0{,}16} + \frac{0{,}0009}{0{,}09} \approx 0{,}0219$.

![Le PSI et son approximation Σ(pₖ − qₖ)²/qₖ le long d'une dérive de plus en plus forte, p(t) = q + t·(p − q) pour t de 0 à 8, à partir des commandes de janvier (juin est en t = 1) : les deux courbes partent de 0 et restent proches tant que le décalage est petit (juin, t = 1 : 0,0204 contre 0,0219) ; l'approximation reste au-dessus jusqu'à t ≈ 7, où les courbes se croisent, et au bout du chemin, où la première classe ne garde que 0,02, le PSI vaut ≈ 1,77 et l'approximation ≈ 1,40](figures/psi_approximation.png)

### Kolmogorov-Smirnov et W₁

> **Définition.** La **statistique de Kolmogorov-Smirnov** (*Kolmogorov-Smirnov statistic*) entre deux lois de fonctions de répartition $F$ et $G$ (le plus souvent empiriques) est
> $$\mathrm{KS} = \sup_x\,\lvert F(x) - G(x)\rvert ,$$
> le plus grand écart vertical entre les deux courbes ; $W_1 = \int\lvert F(x) - G(x)\rvert\,\mathrm{d}x$ en est l'aire (§8).

Ce sont deux tailles de la même fonction $F - G$ : son maximum en valeur absolue et son intégrale en valeur absolue. Pour les commandes, $F_{\text{janv}} = (0{,}42 ;\ 0{,}75 ;\ 0{,}91 ;\ 1)$ et $F_{\text{juin}} = (0{,}37 ;\ 0{,}69 ;\ 0{,}88 ;\ 1)$ en 1, 2, 3 et 4, d'où des écarts 0,05, 0,06, 0,03 et 0 : $\mathrm{KS} = 0{,}06$. Les fonctions sont en escalier, à marches d'un article : $W_1 = (0{,}05 + 0{,}06 + 0{,}03) \times 1 = 0{,}14$ article (pour la variable codée de 1 à 4). Ici $F_{\text{juin}} \le F_{\text{janv}}$ partout : toute la masse a glissé vers le haut, et $W_1$ est exactement l'écart des moyennes, $2{,}06 - 1{,}92 = 0{,}14$.

Pour deux échantillons, $F$ et $G$ sont les fonctions de répartition empiriques. Sous l'hypothèse « même loi » (continue), la loi de KS ne dépend pas de cette loi : on en tire un test et sa **p-valeur** (M08), que les bibliothèques calculent (`scipy.stats.ks_2samp`).

> **Une borne.** Si les deux lois vivent dans $[a, b]$, $W_1 = \int_a^b\lvert F - G\rvert \le (b - a)\,\mathrm{KS}$.

Pour les commandes, sur $[1 ; 4]$ : $W_1 = 0{,}14 \le 3 \times 0{,}06 = 0{,}18$.

### Ce que chacun mesure

- **Les unités.** KS est une différence de probabilités, sans unité ; le PSI est en nats ; $W_1$ est dans l'unité de la variable (des articles, des degrés) : multiplier la variable par $a$ multiplie $W_1$ par $\lvert a\rvert$, et ne change pas KS.
- **Les invariances.** KS ne change pas si l'on applique aux deux lois une même fonction strictement croissante (un changement d'unité, un logarithme) : il ne voit que l'ordre des valeurs. Le PSI ignore l'ordre des classes : il convient à une variable sans ordre (un mode de paiement), pour laquelle KS et $W_1$ n'ont pas de sens.
- **Ce qu'ils ne voient pas.** KS ne dit pas **de combien** la masse s'est déplacée : deux lois dont l'une est tout entière à gauche de l'autre ont $\mathrm{KS} = 1$, qu'elles soient voisines ou lointaines ; $W_1$ le dit. Le PSI ne voit pas un déplacement à l'intérieur d'une classe, et dépend du découpage choisi.

💻 **Aujourd'hui en pratique** — un outil de surveillance affiche souvent plusieurs de ces mesures côte à côte : elles ne se contredisent pas, elles ne regardent pas la même chose (un découpage en classes, l'ordre des valeurs, leur unité).

⚠️ **Erreur classique.** Comparer un $W_1$ en degrés Celsius à un $W_1$ en degrés Fahrenheit, ou à un KS : $W_1$ a l'unité de la variable, KS n'en a pas. Calculer KS ou $W_1$ sur une variable sans ordre. Oublier que le PSI dépend des classes.

🔗 **Dans workbookIA** — le bonus B7 surveille un modèle en production et mesure la dérive de ses données ; tu y retrouveras le PSI et Kolmogorov-Smirnov.

## Les pièges classiques ⚠️ (récapitulatif)

- **Les rôles** : la ligne maximise, la colonne paie ; le pire d'une colonne est son maximum. Dans MML (7.23) et `descent_ascent_iterates`, c'est $\mathbf{x}$ qui minimise.
- **L'indifférence** : $p^\star$ se calcule pour rendre l'**adversaire** indifférent ; avec un point selle, on joue pur.
- **L'équilibre** n'est ni forcément le meilleur pour tous, ni forcément unique.
- **La descente-montée** : simultanée, elle s'éloigne pour tout pas ; alternée, elle tourne sans converger.
- **La log-loss** : le meilleur prédicteur est $t^\star(x)$, avec les priors ; plus tranché, il fait moins bien.
- **Jensen-Shannon** : en nats, au plus $\ln 2$ ; constante dès que les supports sont disjoints, quelle que soit la distance.
- **Le transport** : deux marges à respecter ; $W_2$ n'est pas $W_2^2$ ; $\lvert\mathbb{E}X - \mathbb{E}Y\rvert$ ne fait que minorer $W_1$.
- **La dimension 1** : trier avant d'apparier ; des écarts-types, pas des variances, dans $W_2$ de deux gaussiennes.
- **Fréchet** : la racine d'une matrice n'est pas la matrice des racines ; une distance estimée est biaisée vers le haut, et ne se compare qu'à tailles égales.
- **La dérive** : KS sans unité, $W_1$ dans l'unité de la variable, un PSI qui dépend des classes.

## Et maintenant

**Dans ce dépôt** : M28 passe à la matrice de Gram, à la montée sur l'entrée d'une fonction et aux lois tronquées ; l'examen blanc CP6 reprend toute la partie VI ; MB8 retrouvera une log-loss sur des comparaisons par paires (le modèle de Bradley-Terry) et une pénalité KL.

**Dans workbookIA** : le chapitre 27 traite les réseaux génératifs adverses. Tu y reconnaîtras un jeu à somme nulle entre deux réseaux, l'idée d'équilibre, des log-loss, Jensen-Shannon, $W_1$ en dimension 1 calculé par un tri, la distance de Fréchet entre gaussiennes, et des distances estimées sur des échantillons. Le bonus B7, plus loin, surveille un modèle en production avec le PSI et la statistique de Kolmogorov-Smirnov.

## Pour aller plus loin

- G. Peyré et M. Cuturi, *Computational Optimal Transport*, Foundations and Trends in Machine Learning, vol. 11, n° 5-6, 2019 (version gratuite sur arXiv, 1803.00567) : ch. 2 (couplages, problème de Kantorovich, propriétés métriques, dualité, et au §2.6 les cas particuliers, dont la dimension 1 et les gaussiennes) et ch. 3 (le programme linéaire de Kantorovich, la règle du coin nord-ouest au §3.4.2).
- T. S. Ferguson, *Game Theory*, notes de cours (département de mathématiques de l'UCLA, en ligne) : partie I, §1 (*Take-Away Games*, les jeux d'allumettes) ; partie II, §2 à §5 (la domination, le principe d'indifférence, la résolution d'un jeu fini par la programmation linéaire, la forme extensive) ; partie III, §1 et §2 (jeux bimatriciels, niveaux de sécurité, équilibres de Nash).
- MML §7.2 (relu) et §7.3.1, avec l'exercice 7.6.
- `annexes/symboles.md`, `annexes/formulaire.md` et `annexes/erreurs_frequentes.md`.
