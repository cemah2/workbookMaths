# M26 · Chaînes de Markov et équation de Bellman — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🗣️ 🔗 Explication et pont](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M26.Q1 — Matrice stochastique, convention ligne, loi à n pas et chemins du graphe : vrai ou faux

<details><summary>Indice 1</summary>

Fiche §1 : la définition, « La loi après n pas », Chapman-Kolmogorov, et « Une loi à gauche, une fonction à droite ».

</details>
<details><summary>Indice 2</summary>

Ligne = état de départ, colonne = état d'arrivée. $(\boldsymbol{\mu}\mathbf{P})\mathbf{1} = \boldsymbol{\mu}(\mathbf{P}\mathbf{1})$. $(\mathbf{P}^2)_{ij} = \sum_kp_{ik}p_{kj}$.

</details>
<details><summary>Indice 3</summary>

3. Deux chemins de 0 à 0 en deux pas : par 0 et par 1. 5. Le passé a-t-il une influence, ou une influence résumée par le présent ? 6. Une moyenne de $f$ sur la ligne $i$.

</details>

### M26.Q2 — Une loi stationnaire existe-t-elle, est-elle unique, la loi de la chaîne y converge-t-elle ? Chaînes périodiques et à deux classes

<details><summary>Indice 1</summary>

Fiche §2 : le théorème d'existence, « Unicité et convergence » et ses deux contre-exemples, puis « La vitesse ».

</details>
<details><summary>Indice 2</summary>

Existence : toujours. Unicité : chaîne irréductible. Convergence de $\boldsymbol{\mu}_n$ : irréductible et apériodique. Vitesse : $\lvert\lambda_2\rvert^n$.

</details>
<details><summary>Indice 3</summary>

2. Que vaut un mélange de deux lois stationnaires ? 3. Où est la chaîne aux pas 4, 8, 12… et aux pas 1, 5, 9… ? 6. $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$ transposée.

</details>

### M26.Q3 — Espérance conditionnelle, propriété de la tour et analyse au premier pas : quelle équation pour quel nombre ?

<details><summary>Indice 1</summary>

Fiche §3 : l'espérance conditionnelle, la tour, « L'analyse au premier pas » et « La matrice fondamentale ».

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[X \mid Y] = m(Y)$. Conditionner sur plus, puis moyenner le surplus, revient à conditionner sur moins. $\mathbf{h}$ a un second membre $\mathbf{b}$, $\mathbf{t}$ un second membre $\mathbf{1}$.

</details>
<details><summary>Indice 3</summary>

5. $t = 1 + 0{,}8\,t$.

</details>

### M26.Q4 — Le facteur γ : une actualisation, ou une probabilité de continuer ? Valeur d'un état et politique

<details><summary>Indice 1</summary>

Fiche §4 : « γ, une probabilité de continuer », puis la définition d'un MDP et la chaîne induite.

</details>
<details><summary>Indice 2</summary>

$P(N \ge t) = \gamma^t$ et $\mathbb{E}[N + 1] = \frac{1}{1 - \gamma}$. Les deux lectures ont la même espérance. $r_\pi(s) = \sum_a\pi(a \mid s)\,r(s, a)$.

</details>
<details><summary>Indice 3</summary>

1. $\frac{1}{0{,}4}$. 2. Combien de fois l'arrêt serait-il compté ?

</details>

### M26.Q5 — Le système de Bellman d'une politique fixée : quelles matrices, pourquoi il est inversible, quand γ = 1 est permis

<details><summary>Indice 1</summary>

Fiche §5 : l'équation de Bellman, le théorème, « Une fin possible » et « Sans fin, γ = 1 ne marche pas ».

</details>
<details><summary>Indice 2</summary>

$\lVert\gamma\mathbf{P}\rVert_\infty = \gamma$ et $\rho \le \lVert\cdot\rVert$ (M22). Que vaut $(\mathbf{I} - \mathbf{P})\mathbf{1}$ ?

</details>
<details><summary>Indice 3</summary>

5. $V = 1{,}2 + 0{,}6\,V$.

</details>

### M26.Q6 — Contraction, bornes a priori et a posteriori, itérations synchrones ou en place : vrai ou faux

<details><summary>Indice 1</summary>

Fiche §6 : le théorème, les bornes d'erreur, et les deux sortes d'itérations.

</details>
<details><summary>Indice 2</summary>

A priori : $\gamma^k\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty$. A posteriori : $\frac{\gamma}{1 - \gamma}\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty$.

</details>
<details><summary>Indice 3</summary>

2. $10 \times 0{,}7^5$. 3. $\frac{0{,}7}{0{,}3} \times 0{,}03$. 6. Écris un pas de Richardson de pas 1 pour $(\mathbf{I} - \gamma\mathbf{P})\mathbf{V} = \mathbf{r}$.

</details>

### M26.Q7 — Un maximum dans l'opérateur : ce qui reste (contraction, point fixe unique), ce qui se perd (le système linéaire)

<details><summary>Indice 1</summary>

Fiche §7 : le lemme, l'arrêt optimal et son énoncé, les offres indépendantes.

</details>
<details><summary>Indice 2</summary>

$\lvert\max\mathbf{x} - \max\mathbf{y}\rvert \le \lVert\mathbf{x} - \mathbf{y}\rVert_\infty$. Une contraction a un unique point fixe (Banach). Selon $\mathbf{V}$, le maximum choisit l'une ou l'autre branche.

</details>
<details><summary>Indice 3</summary>

2. Cherche deux vecteurs de deux coordonnées dont les maxima ne sont pas atteints au même indice. 5. Compare l'offre au seuil $C^\star$.

</details>

### M26.Q8 — Des échantillons au lieu de P : moyenne de retours, pas 1/n ou constant, erreur TD, biais du maximum

<details><summary>Indice 1</summary>

Fiche §8 : les quatre paragraphes.

</details>
<details><summary>Indice 2</summary>

Pas constant : un bruit de variance $\frac{\alpha\sigma^2}{2 - \alpha}$. Robbins-Monro : $\sum\alpha_n = \infty$ **et** $\sum\alpha_n^2 < \infty$. $\mathbb{E}[\delta \mid S = s]$ = le résidu. Troncature : $\gamma^T\lVert\mathbf{V}\rVert_\infty$.

</details>
<details><summary>Indice 3</summary>

3. Pour chaque pas, teste les deux séries ; $\big(\frac{1}{\sqrt n}\big)^2 = \frac1n$. 6. $0{,}7^{20} \times 50$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M26.R1 — Puissances d'une matrice diagonalisable et méthode de la puissance (M12c)

<details><summary>Indice 1</summary>

M12c : valeurs propres, diagonalisation, méthode de la puissance.

</details>
<details><summary>Indice 2</summary>

Le polynôme caractéristique d'une matrice $2 \times 2$ est $\lambda^2 - \operatorname{tr}(\mathbf{A})\,\lambda + \det\mathbf{A}$. La méthode de la puissance tend vers le vecteur propre de la plus grande valeur propre, au rythme $\lvert\lambda_2/\lambda_1\rvert$.

</details>
<details><summary>Indice 3</summary>

$\operatorname{tr} = 7$, $\det = 6$. Pour 2, calcule $\mathbf{A}^2$ puis $\mathbf{A}^2\mathbf{A}$.

</details>

### M26.R2 — La norme ‖·‖∞ d'une matrice, ρ(A) ≤ ‖A‖ et Aᵗ → 0 quand ρ(A) < 1 (M22), et la somme d'une série géométrique (R5)

<details><summary>Indice 1</summary>

M22 §4 (normes induites, rayon spectral) ; R5 (séries géométriques).

</details>
<details><summary>Indice 2</summary>

$\lVert\mathbf{A}\rVert_\infty$ = la plus grande somme des $\lvert a_{ij}\rvert$ d'une ligne. Valeurs propres par la trace et le déterminant. $\sum_{t \ge 0}q^t = \frac{1}{1 - q}$ pour $\lvert q\rvert < 1$.

</details>
<details><summary>Indice 3</summary>

Trace 0,3, déterminant 0,22. Pour 4, une matrice nilpotente $2 \times 2$ avec un grand coefficient. Pour 6, retire les deux premiers termes.

</details>

### M26.R3 — Probabilités totales et espérance d'une loi géométrique (M03, M02b)

<details><summary>Indice 1</summary>

M03 (probabilités totales) ; M02b (loi géométrique).

</details>
<details><summary>Indice 2</summary>

$P(A) = \sum_iP(B_i)\,P(A \mid B_i)$ ; $\mathbb{E}[X] = \frac1p$ et $P(X > k) = (1 - p)^k$.

</details>
<details><summary>Indice 3</summary>

3. Les trois premiers essais échouent. 4. L'absence de mémoire.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M26.1 — Des vélos en libre-service entre trois stations : matrice de transition, graphe, loi après deux et trois jours, et coût moyen du lendemain (Pf)

<details><summary>Indice 1</summary>

Fiche §1 : la boutique (sa matrice, $\boldsymbol{\mu}_1$, $\boldsymbol{\mu}_2$, $(\mathbf{P}^2)_{20}$ par les chemins, $\mathbf{P}\mathbf{f}$), avec ici une loi de départ qui n'est pas concentrée.

</details>
<details><summary>Indice 2</summary>

La ligne $i$ de $\mathbf{P}$ est la station du matin. $\boldsymbol{\mu}_{n+1} = \boldsymbol{\mu}_n\mathbf{P}$ : la coordonnée $j$ est $\sum_i\mu_n(i)\,p_{ij}$. $(\mathbf{P}^2)_{BC} = \sum_kp_{Bk}\,p_{kC}$. $(\mathbf{P}\mathbf{f})_i = \sum_jp_{ij}\,f(j)$.

</details>
<details><summary>Indice 3</summary>

$\boldsymbol{\mu}_1 = (0{,}44 ;\ 0{,}32 ;\ 0{,}24)$. Pour f), chaque vélo coûte en moyenne $(\mathbf{P}\mathbf{f})_i$ s'il est en $i$ ce matin : $200\,\boldsymbol{\mu}_0(\mathbf{P}\mathbf{f})$.

</details>

### Ex M26.2 — Trois opérateurs et leurs parts de marché : la loi stationnaire par un système linéaire, puis vérifier πP = π

<details><summary>Indice 1</summary>

Fiche §2 : « Le calcul par un système linéaire ». Ici, on résout par le pivot, pas par substitution.

</details>
<details><summary>Indice 2</summary>

L'équation $j$ de $(\mathbf{P}^\top - \mathbf{I})\boldsymbol{\pi}^\top = \mathbf{0}$ est $\pi_j = \sum_i\pi_i\,p_{ij}$ (la colonne $j$ de $\mathbf{P}$). Multiplie les deux premières par 20 pour n'avoir que des entiers. Pour d), la règle de Bayes en régime stationnaire.

</details>
<details><summary>Indice 3</summary>

$-2\pi_0 + \pi_1 + 4\pi_2 = 0$, $\pi_0 - 3\pi_1 + 3\pi_2 = 0$, $\pi_0 + \pi_1 + \pi_2 = 1$ ; élimine $\pi_0$, tu trouves $\pi_1 = 2\pi_2$. d) $P(S_t = C \mid S_{t+1} = A) = \frac{\pi_C\,p_{CA}}{\pi_A}$.

</details>

### Ex M26.3 — Trois chaînes qui posent problème, périodique, à deux classes et avec un état transitoire : lois stationnaires et comportement de Pⁿ

<details><summary>Indice 1</summary>

Fiche §2 : « Unicité et convergence », ses deux contre-exemples et les définitions. Une chaîne à deux états $\begin{pmatrix} 1 - a & a \\ b & 1 - b \end{pmatrix}$ a pour loi stationnaire $\big(\frac{b}{a+b}, \frac{a}{a+b}\big)$.

</details>
<details><summary>Indice 2</summary>

Le bac : regarde les ports du nord deux traversées à la fois (le produit du bloc nord → sud par le bloc sud → nord). Le site : deux chaînes à deux états, indépendantes. L'essai : la première colonne de $\mathbf{P}$.

</details>
<details><summary>Indice 3</summary>

La chaîne du nord a pour matrice $\begin{pmatrix} 0{,}72 & 0{,}28 \\ 0{,}51 & 0{,}49 \end{pmatrix}$. La loi stationnaire du bac met la masse $\frac12$ au nord (proportionnelle à la loi de cette chaîne) et $\frac12$ au sud (son image après une traversée).

</details>

### Ex M26.4 — Un cursus en trois années, avec redoublement et abandon : la probabilité d'être diplômé et la durée moyenne des études, par l'analyse au premier pas

<details><summary>Indice 1</summary>

Fiche §3 : le site marchand ($\mathbf{Q}$, $\mathbf{b}$, $\mathbf{h}$, $\mathbf{t}$, $\mathbf{N}$).

</details>
<details><summary>Indice 2</summary>

$\mathbf{Q}$ ne contient que L1, L2, L3, réorientation comprise ; $\mathbf{b}$ est la colonne « diplômé ». L3 ne mène qu'à lui-même parmi les transitoires : commence par lui.

</details>
<details><summary>Indice 3</summary>

$h_3 = \frac{0{,}75}{0{,}85}$ et $h_1 = \frac{0{,}7}{0{,}85}h_2$ ; reporte dans l'équation de $h_2$ (multiplie par 17). Pour d), $\mathbf{n}(\mathbf{I} - \mathbf{Q}) = (1, 0, 0)$ donne $n_2 = \frac{14}{17}n_1$.

</details>

### Ex M26.5 — Un abonné qui peut résilier chaque mois : durée géométrique, revenu total moyen, et le même nombre comme revenu actualisé

<details><summary>Indice 1</summary>

Fiche §4 : « γ, une probabilité de continuer », la propriété et sa démonstration.

</details>
<details><summary>Indice 2</summary>

Il paie le mois $t$ s'il a renouvelé $t$ fois : $P(N \ge t) = 0{,}7^t$. $\mathbb{E}[N + 1] = \sum_{t \ge 0}P(N \ge t)$.

</details>
<details><summary>Indice 3</summary>

e) Un revenu sous 30 € : 9, 18 ou 27 €. f) La somme commence à $t = 1$.

</details>

### Ex M26.6 — Une machine qui s'use, deux politiques d'entretien : P_π et r_π, deux systèmes de Bellman 3 × 3, et la valeur d'une action

<details><summary>Indice 1</summary>

Fiche §4 (la boutique comme MDP, la chaîne induite, la valeur d'une action) et §5 (le système).

</details>
<details><summary>Indice 2</summary>

$r(s, a) = \sum_{s'}\mathbf{P}_a(s, s')\,r(s, a, s')$. Chaque ligne de $\mathbf{P}_\pi$ vient de l'action que $\pi$ choisit. Écris $(\mathbf{I} - 0{,}6\,\mathbf{P}_\pi)\mathbf{V} = \mathbf{r}_\pi$.

</details>
<details><summary>Indice 3</summary>

Pour $\pi_A$ : $0{,}58\,V_0 - 0{,}18\,V_1 = 10$, $0{,}61\,V_1 - 0{,}21\,V_2 = 4{,}95$, $-0{,}48\,V_0 + 0{,}88\,V_2 = -8$. e) $4{,}95 + 0{,}6\,\big(0{,}65\,V^{\pi_B}(1) + 0{,}35\,V^{\pi_B}(2)\big)$.

</details>

### Ex M26.7 — Les itérés de Bellman de la machine de M26.6 : trois pas synchrones puis en place, comparés à la solution, et le nombre d'itérations qui garantit 10⁻³

<details><summary>Indice 1</summary>

Fiche §6 : l'exemple de la boutique (synchrones, puis en place), les bornes et « Combien d'itérations pour un centime ? ».

</details>
<details><summary>Indice 2</summary>

Synchrone : $\mathbf{V}_{k+1} = \mathbf{r} + 0{,}6\,\mathbf{P}\mathbf{V}_k$, les trois coordonnées à partir des anciennes. En place : $V(0)$, puis $V(1)$ avec le nouveau $V(0)$, puis $V(2)$ avec les deux nouvelles valeurs. A priori : $0{,}6^k\lVert\mathbf{V}^{\pi_A}\rVert_\infty \le 10^{-3}$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{V}_2 = (15{,}091 ;\ 5{,}2005 ;\ -4{,}16)$ et $\mathbf{W}_1 = (10 ;\ 4{,}95 ;\ -3{,}2)$. e) $k \ge \frac{\ln(10^{-3}/19{,}95116)}{\ln 0{,}6}$, puis l'entier supérieur.

</details>

### Ex M26.8 — Vendre une voiture d'occasion : offres au hasard, coût d'attente, valeur de continuation et règle à seuil

<details><summary>Indice 1</summary>

Fiche §7 : « Des offres indépendantes : une seule équation ».

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[\max(X, C)]$ dépend de la place de $C$ parmi les offres : les offres sous $C$ comptent pour $C$, les autres pour leur valeur. Suppose $C$ dans un intervalle, résous l'équation (linéaire), puis vérifie l'intervalle.

</details>
<details><summary>Indice 3</summary>

Pour $4\,000 \le C \le 5\,000$, $\mathbb{E}[\max(X, C)] = 0{,}6\,C + 2\,400$. e) La règle fixe ses décisions : $C_r = c + \gamma\,(0{,}3\,C_r + 0{,}3 \times 4\,000 + 0{,}2 \times 5\,000 + 0{,}2 \times 7\,000)$.

</details>

### Ex M26.9 — Le meilleur de deux fournisseurs sur des mesures bruitées : le maximum surestime, l'estimateur double non

<details><summary>Indice 1</summary>

Fiche §8 : « Le biais du maximum », les démonstrations de $\mathbb{E}[\max(Z_1, Z_2)] = \frac{1}{\sqrt\pi}$ et de l'estimateur double.

</details>
<details><summary>Indice 2</summary>

$\max(u, v) = \frac{u + v}{2} + \frac{\lvert u - v\rvert}{2}$, et $D = \hat A - \hat B$ suit $\mathcal{N}(\delta, \sigma_A^2 + \sigma_B^2)$ : les variances s'ajoutent.

</details>
<details><summary>Indice 3</summary>

$\sigma_D = 12{,}5$ h. b) $\mathbb{E}\lvert D\rvert = \sigma_D\sqrt{2/\pi}$ pour $\delta = 0$. c) $P(D < 0) = \Phi(-\delta/\sigma_D)$. d) L'espérance totale, sur le fournisseur choisi.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M26.10 — L'analyse au premier pas démontrée : t = 1 + Qt et h = Qh + b, et I − Q inversible dès que la fin est possible depuis chaque état

<details><summary>Indice 1</summary>

Fiche §3 : l'idée de l'inversibilité ; M22 : la sous-multiplicativité de $\lVert\cdot\rVert_\infty$.

</details>
<details><summary>Indice 2</summary>

La somme de la ligne $i$ de $\mathbf{Q}^n$ est la probabilité de ne pas être absorbé au pas $n$. Un plus court chemin vers un état absorbant passe par des états transitoires distincts : sa longueur est au plus $m$. Prends $\varepsilon$ = le plus petit, sur les états, de la probabilité d'un tel chemin.

</details>
<details><summary>Indice 3</summary>

Inversibilité : si $\mathbf{x} = \mathbf{Q}\mathbf{x}$, alors $\mathbf{x} = \mathbf{Q}^t\mathbf{x} \to \mathbf{0}$. Durée : $T = 1 + T'$ et $\mathbb{E}[T' \mid S_0 = i, S_1 = j] = t_j$ par la propriété de Markov ; $t_i = \sum_uP(T > u)$.

</details>

### Ex M26.11 — V = Σ γᵗPᵗr est l'unique solution du système de Bellman : I − γP inversible, série de Neumann démontrée pour γP, et (1 − γ)(I − γP)⁻¹ stochastique

<details><summary>Indice 1</summary>

Fiche §5 : le théorème et la propriété de la loi d'occupation actualisée.

</details>
<details><summary>Indice 2</summary>

$\mathbf{P}^t\mathbf{1} \le \mathbf{1}$ par récurrence. Dans $\mathbf{S}_n(\mathbf{I} - \gamma\mathbf{P})$, les termes se compensent deux à deux.

</details>
<details><summary>Indice 3</summary>

$\mathbf{S}_n(\mathbf{I} - \gamma\mathbf{P}) = \mathbf{I} - \gamma^{n+1}\mathbf{P}^{n+1}$ ; chaque coefficient de la série est majoré par $\gamma^t$ (comparaison). Pour 4, $(\mathbf{I} - \gamma\mathbf{P})\mathbf{1} = (1 - \gamma)\mathbf{1}$, puis multiplie par $(\mathbf{I} - \gamma\mathbf{P})^{-1}$.

</details>

### Ex M26.12 — L'opérateur de Bellman d'une politique fixée est une γ-contraction pour ‖·‖∞ ; bornes a priori et a posteriori ; le maximum est 1-lipschitzien

<details><summary>Indice 1</summary>

Fiche §6 (la contraction démontrée) et §7 (le lemme du maximum et sa démonstration).

</details>
<details><summary>Indice 2</summary>

2 : l'inégalité triangulaire entre $\mathbf{V}_{k-1}$ et $\mathbf{V}$, en passant par $\mathbf{V}_k$. 3 : une récurrence sur $i$, qui sépare les valeurs déjà mises à jour et les anciennes. 4 : les $k$ indices des $k$ plus grandes coordonnées de $\mathbf{x}$.

</details>
<details><summary>Indice 3</summary>

3 : $\lvert U'_i - W'_i\rvert \le \gamma\big(\sum_{j < i}p_{ij}\,\gamma\delta + \sum_{j \ge i}p_{ij}\,\delta\big)$. 5 : $f(e) \le g(e) + \delta \le \sup_Eg + \delta$ pour tout $e$.

</details>

### Ex M26.13 — L'erreur TD se télescope : Σ γᵏ δ_{t+k} = G_t − V(S_t) ; une récompense ajoutée γΦ(s′) − Φ(s) décale chaque valeur de −Φ(s)

<details><summary>Indice 1</summary>

Fiche §8 : « Le télescopage » et l'idée commune.

</details>
<details><summary>Indice 2</summary>

Écris $\gamma^k\delta_{t+k} = \gamma^kR_{t+k} + \gamma^{k+1}V(S_{t+k+1}) - \gamma^kV(S_{t+k})$, et décale l'indice d'une des deux sommes en $V$.

</details>
<details><summary>Indice 3</summary>

La somme en $V$ vaut $\gamma^{T-t}V(S_T) - V(S_t)$. Pour 3, $\Phi(S_0) = \Phi(s)$ sachant $S_0 = s$, et la linéarité de l'espérance.

</details>

<a id="reflexion"></a>

## 🗣️ 🔗 Explication et pont

### Ex M26.14 — Pont : d'une politique stochastique à la chaîne qu'elle induit, P_π = Σ_a π(a | s) P_a et r_π avec des tableaux à trois axes (actions, états, états), puis Q^π(s, a) et r(s, a, s′)

<details><summary>Indice 1</summary>

Fiche §4 (MDP, chaîne induite, valeur d'une action) ; M20 (axes, réductions, `einsum`).

</details>
<details><summary>Indice 2</summary>

`(P * R).sum(axis=2)[a, s]` $= \sum_{s'}\mathbf{P}_a(s, s')\,r(s, a, s')$. $\mathbf{P}_\pi(s, \cdot) = \sum_a\pi(a \mid s)$ `P[a, s, :]`. L'état « parti » a une valeur nulle.

</details>
<details><summary>Indice 3</summary>

`r_sa` $= \begin{pmatrix} 30 & 21 & 0 \\ 21 & ? & 0 \end{pmatrix}$. e) $0{,}235\,V_0 - 0{,}085\,V_1 = 30$ et $-0{,}34\,V_0 + 0{,}677\,V_1 = r_\pi(1)$.

</details>

### Ex M26.15 — Expliquer avec une image hors informatique pourquoi une chaîne qui mélange oublie son état de départ

<details><summary>Indice 1</summary>

Fiche §2 : la chaîne à deux états (« L'oubli du départ ») et les deux contre-exemples.

</details>
<details><summary>Indice 2</summary>

Plan : l'image ; ce qui correspond au départ, à la loi, à un pas ; la loi qui ne bouge plus ; les deux obstacles ; la vitesse.

</details>
<details><summary>Indice 3</summary>

« Imagine une goutte d'encre dans un verre d'eau qu'on remue : l'endroit où elle tombe, c'est le départ ; la façon dont l'encre est répartie, c'est la loi… »

</details>

<a id="entretien"></a>

## 💼 Entretien

### M26.E1 — « Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que se passe-t-il pour γ = 1 ? »

<details><summary>Indice 1</summary>

Fiche §5 : le théorème, « Une fin possible », « Sans fin, γ = 1 ne marche pas » ; ∂ M26.11.

</details>
<details><summary>Indice 2</summary>

Deux arguments au choix : la norme ($\lVert\gamma\mathbf{P}\rVert_\infty = \gamma$) ou la série de Neumann. Pour $\gamma = 1$ : $\mathbf{P}\mathbf{1} = \mathbf{1}$.

</details>
<details><summary>Indice 3</summary>

D'où vient le système, l'argument, la pratique (résoudre, itérer), $\gamma = 1$ sans fin, $\gamma = 1$ avec une fin sûre, le conditionnement.

</details>

<a id="notebook"></a>

## Notebook

### M26.16 — La loi d'une chaîne après n pas, en convention ligne : `n_step_distribution`

<details><summary>Indice 1</summary>

La docstring de `n_step_distribution` et son TODO ; la fiche §1, « La loi après n pas » et le 💻.

</details>
<details><summary>Indice 2</summary>

`P = np.array(P, dtype=float)` (une copie) ; contrôle `P.ndim == 2`, `P.shape[0] == P.shape[1] >= 1`, `np.isfinite(P).all()`, `(P >= 0).all()` et `np.all(np.abs(P.sum(axis=1) - 1) <= 1e-9)` ; de même pour `mu0` ; pour `n`, `isinstance(n, numbers.Integral) and not isinstance(n, (bool, np.bool_)) and n >= 0`.

</details>
<details><summary>Indice 3</summary>

`mu = np.array(mu0, dtype=float)`, puis `for _ in range(n): mu = mu @ P`. Pour b), `mymath.markov.n_step_distribution(P_ferry, [1, 0, 0, 0], 100)` et `np.allclose(mu100, ta_reponse, atol=1e-12, rtol=0)`.

</details>

### M26.17 — La loi stationnaire par un système linéaire, et le refus d'une chaîne qui en a plusieurs : `stationary_distribution`

<details><summary>Indice 1</summary>

La docstring et le TODO de `stationary_distribution` ; la fiche §2, « Le calcul par un système linéaire ».

</details>
<details><summary>Indice 2</summary>

`A = P.T - np.eye(m)`, puis `A[-1, :] = 1` ; `b = np.zeros(m)` et `b[-1] = 1`.

</details>
<details><summary>Indice 3</summary>

`if np.linalg.matrix_rank(A) < m: raise ValueError("the stationary law is not unique")` ; `pi = np.linalg.solve(A, b)`, `pi = np.where(pi < 0, 0.0, pi)`, `return pi / pi.sum()`. Pour c), un `try: … except ValueError:` autour de `mymath.markov.stationary_distribution(P_site)`.

</details>

### M26.18 — Le système de Bellman d'une politique fixée, avec une fin possible (matrice sous-stochastique) et γ = 1 quand la fin est sûre : `bellman_linear_solve`

<details><summary>Indice 1</summary>

La docstring du module (matrices sous-stochastiques, $\gamma = 1$) et celle de `bellman_linear_solve` ; la fiche §5.

</details>
<details><summary>Indice 2</summary>

Lignes de somme au plus $1 + 10^{-9}$ ; `gamma` : `isinstance(gamma, numbers.Real) and not isinstance(gamma, (bool, np.bool_))`, fini, dans $[0, 1]$. `M = np.eye(m) - gamma * P`.

</details>
<details><summary>Indice 3</summary>

`if gamma == 1 and np.linalg.matrix_rank(M) < m: raise ValueError(...)`, puis `return np.linalg.solve(M, r)`. Pour c), la matrice $5 \times 5$ a pour lignes celles de L1, L2, L3 (avec les colonnes « diplômé » et « abandon ») puis $(0, 0, 0, 1, 0)$ et $(0, 0, 0, 0, 1)$.

</details>

### M26.19 — Les itérés de l'opérateur de Bellman d'une politique fixée (Richardson de pas 1) : `bellman_fixed_point_iterates`

<details><summary>Indice 1</summary>

La docstring et le TODO de `bellman_fixed_point_iterates` ; la fiche §6.

</details>
<details><summary>Indice 2</summary>

`V = np.zeros(m) if V0 is None else np.array(V0, dtype=float)` ; `out = np.empty((n_steps + 1, m))` et `out[0] = V`.

</details>
<details><summary>Indice 3</summary>

`for k in range(1, n_steps + 1): V = r + gamma * (P @ V); out[k] = V`. b) `err = np.abs(its - V_exact).max(axis=1)` puis `np.argmax(err <= 1e-3)`. c) Dans `in_place_sweeps_19`, une boucle sur les états à l'intérieur de la boucle des balayages : `W[i] = r[i] + gamma * P[i] @ W`, puis une copie de `W` par ligne.

</details>

### M26.20 — La loi stationnaire de trois façons, `np.linalg.eig` sur Pᵀ, `scipy.linalg.null_space` et la méthode de la puissance, sur le surfeur aléatoire d'un web de six pages

<details><summary>Indice 1</summary>

Fiche §2, « Le PageRank » (la matrice $\mathbf{P}_d$, la page sans lien, la borne en $d^k$).

</details>
<details><summary>Indice 2</summary>

Une ligne de $\mathbf{L}$ par page : $\frac{1}{\text{nombre de liens}}$ sur chaque page pointée, $\frac16$ partout pour la page 6. `w, v = np.linalg.eig(Pd.T)`, `i = np.argmin(np.abs(w - 1))` ; `ns = scipy.linalg.null_space(Pd.T - np.eye(6))`.

</details>
<details><summary>Indice 3</summary>

Dans `power_stationary_20` : `x = np.full(len(P), 1 / len(P))`, puis répéter `y = x @ P` jusqu'à `np.abs(y - x).sum() < tol`, en comptant les pas. La borne : $k \ge \frac{\ln(10^{-12}/2)}{\ln 0{,}85}$.

</details>

### M26.21 — Prédire la somme des lignes de (1 − γ)(I − γP)⁻¹, puis leur limite quand γ tend vers 1, et vérifier

<details><summary>Indice 1</summary>

Fiche §5, « La loi d'occupation actualisée » : la loi de l'état où l'on est quand l'arrêt géométrique tombe.

</details>
<details><summary>Indice 2</summary>

La colonne $j$ de $(\mathbf{I} - \gamma\mathbf{P})^{-1}$ résout $(\mathbf{I} - \gamma\mathbf{P})\mathbf{x} = \mathbf{e}_j$ : c'est `mymath.markov.bellman_linear_solve(P, np.eye(3)[j], gamma)`.

</details>
<details><summary>Indice 3</summary>

`g = sp.symbols("gamma")`, `M = (1 - g) * (sp.eye(3) - g * P_sym).inv()`, puis `M.applyfunc(lambda e: sp.limit(sp.simplify(e), g, 1))` ; `P_sym` s'écrit avec `sp.Rational`.

</details>

### M26.22 — Le biais du maximum par simulation : k fournisseurs de même qualité, n mesures chacun, le meilleur mesuré contre l'estimateur double

<details><summary>Indice 1</summary>

Fiche §8, « Le biais du maximum » et l'estimateur double.

</details>
<details><summary>Indice 2</summary>

`means = np.full(k, 1000.0); means[0] += delta` ; `s1 = rng.normal(means, 30, size=(n_rep, n, k)).mean(axis=1)` ; `choice = s1.argmax(axis=1)`.

</details>
<details><summary>Indice 3</summary>

`s2 = rng.normal(means[choice][:, None], 30, size=(n_rep, n)).mean(axis=1)` ; les biais sont `s1.max(axis=1).mean() - best` et `s2.mean() - best`, avec `best = 1000 + max(delta, 0)`.

</details>

### M26.23 — La loi d'une chaîne au fil des pas depuis trois départs, et ‖μ_n − π‖₁ en échelle logarithmique contre |λ₂|ⁿ

<details><summary>Indice 1</summary>

Fiche §2, « La vitesse : la deuxième valeur propre ».

</details>
<details><summary>Indice 2</summary>

Pour chaque départ $s$, `mymath.markov.n_step_distribution(P, np.eye(m)[s], n)` pour $n = 0, \ldots,$ `n_max` ; `ax_dist.set_yscale("log")` ; $\lvert\lambda_2\rvert$ est le deuxième plus grand module de `np.linalg.eigvals(P)`.

</details>
<details><summary>Indice 3</summary>

b) `(np.log(d[100]) - np.log(d[50])) / 50`. c) Le premier $n$ où le maximum des trois écarts passe sous $10^{-6}$.

</details>

### M26.24 — Chasse à l'erreur : une matrice lue dans la mauvaise convention, une loi stationnaire non normalisée, un état final qui rapporte encore, γ = 1 sans fin

<details><summary>Indice 1</summary>

Les quatre ⚠️ des §1, §2 et §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

(1) Quelle convention `P @ mu` suit-il, et que vaut $\mathbf{S}^\top$ ? (2) Quels vecteurs vérifient $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$ ? (3) Que rapporte un état absorbant à chaque pas ? (4) Que vaut $(\mathbf{I} - \mathbf{P})\mathbf{1}$ pour une chaîne qui ne finit pas ?

</details>
<details><summary>Indice 3</summary>

Corrections : `mu = mu @ P` ; diviser par la somme ; $r(s) = $ `monthly_fee` si $s = 1$, plus `closing_fee` $\times\,p_{s2}$, et 0 pour l'état résilié ; `if np.linalg.matrix_rank(np.eye(m) - P) < m: raise ValueError(...)`.

</details>

### M26.25 — Un test de propriété : πP = π, et pour `bellman_fixed_point_iterates`, V_k − V tenu par γᵏ‖V₀ − V‖∞ et V = r + γPV pour la limite, sur des chaînes tirées au hasard

<details><summary>Indice 1</summary>

Fiche §2 (une loi stationnaire est une loi) et §6 (les deux bornes) ; ∂ M26.12, question 3.

</details>
<details><summary>Indice 2</summary>

Dans la fonction : `if stationary is None: stationary = mymath.markov.stationary_distribution` (au moment de l'appel, pas à la définition) ; un dictionnaire de compteurs initialisés à 0, et un booléen par propriété et par essai.

</details>
<details><summary>Indice 3</summary>

`e = np.abs(it - V).max(axis=1)` ; `k = np.arange(len(e))` ; `a_priori` si `np.any(e > gamma**k * e[0] + tol * scale)` ; `recurrence` si `np.abs(it[1:] - (r + gamma * it[:-1] @ P.T)).max() > tol * scale`.

</details>

### M26.26 — Défi : estimer la valeur d'un état à 0,01 près en simulant l'arrêt géométrique (continuer avec la probabilité γ) et en sommant les récompenses sans actualisation, sous un budget de pas simulés

<details><summary>Indice 1</summary>

Fiche §4 (la propriété de l'arrêt géométrique) et §8 (la moyenne de retours simulés, son erreur type).

</details>
<details><summary>Indice 2</summary>

Une visite dure en moyenne $\frac{1}{1 - \gamma}$ pas : choisis $n$ visites pour que $\frac{n}{1 - \gamma}$ reste sous le budget avec une marge (5 %, par exemple). Simule toutes les visites en parallèle : un tableau de recettes, un d'états, un de visites en cours.

</details>
<details><summary>Indice 3</summary>

Un pas : `idx = np.flatnonzero(alive)` ; `total[idx] += r[state[idx]]` ; `steps += idx.size` ; `alive[idx] = rng.random(idx.size) < gamma` ; l'état suivant par les sommes cumulées des lignes de `P`. Si `steps` dépasse le budget (très rare avec la marge), recommence avec moins de visites.

</details>
