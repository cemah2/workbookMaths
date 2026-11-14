# M26 · Chaînes de Markov et équation de Bellman — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m26_markov_bellman/06_mes_reponses.md` (créée par `python tools/start_chapter.py M26`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🗣️ 🔗 Explication et pont](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les états sont numérotés $0, \ldots, m - 1$ dans l'ordre où l'énoncé les nomme ; $p_{ij}$ est la probabilité d'aller de $i$ à $j$ en un pas ; une **loi** est une **ligne** ($\boldsymbol{\mu}_{n+1} = \boldsymbol{\mu}_n\mathbf{P}$), une fonction des états (un coût, une récompense, une valeur) est une **colonne** ($(\mathbf{P}\mathbf{f})_i = \mathbb{E}[f(S_1) \mid S_0 = i]$) ; chaque ligne de $\mathbf{P}$ a pour somme 1, ou au plus 1 quand le processus peut finir (la masse manquante est la probabilité de finir) ; $\gamma$ est le facteur d'actualisation ; aux §1 à §3, $\boldsymbol{\pi}$ est une loi stationnaire, et à partir du §4, $\pi(a \mid s)$ est une politique ; $\lVert\mathbf{x}\rVert_\infty = \max_i\lvert x_i\rvert$ et $\lVert\mathbf{A}\rVert_\infty$ est la plus grande somme des $\lvert a_{ij}\rvert$ d'une ligne ; $\ln$ est le logarithme népérien. Dans le notebook, une matrice s'écrit comme la liste de ses lignes, une loi ou un vecteur de valeurs comme une liste, et un tableau de forme (actions, états, états) range $\mathbf{P}_a(s, s')$ en `P[a, s, s2]`.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M26.Q1 — Matrice stochastique, convention ligne, loi à n pas et chemins du graphe : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Vrai ou faux : une matrice à coefficients positifs dont chaque **colonne** a pour somme 1 est une matrice de transition au sens de la fiche.
2. Vrai ou faux : si $\boldsymbol{\mu}$ est une loi (une ligne) et $\mathbf{P}$ une matrice stochastique, $\boldsymbol{\mu}\mathbf{P}$ est encore une loi.
3. $\mathbf{P} = \begin{pmatrix} 0{,}1 & 0{,}9 \\ 0{,}7 & 0{,}3 \end{pmatrix}$ : que vaut $(\mathbf{P}^2)_{00}$, lu sur les chemins de longueur 2 de 0 à 0 ?
4. Vrai ou faux : $(\mathbf{P}^n)_{ij} = (p_{ij})^n$.
5. Vrai ou faux : la propriété de Markov dit que le passé de la chaîne n'a aucune influence sur son avenir.
6. Pour une fonction $f$ des états écrite en colonne $\mathbf{f}$, que vaut $\mathbb{E}[f(S_{t+1}) \mid S_t = i]$ ?

### M26.Q2 — Une loi stationnaire existe-t-elle, est-elle unique, la loi de la chaîne y converge-t-elle ? Chaînes périodiques et à deux classes 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. Vrai ou faux : toute matrice stochastique a au moins une loi stationnaire.
2. Une chaîne a deux classes fermées qui ne communiquent pas. Combien a-t-elle de lois stationnaires ?
3. Quatre états visités en tournant, $0 \to 1 \to 2 \to 3 \to 0$, chaque flèche de probabilité 1, départ en 0. Vrai ou faux : $\boldsymbol{\mu}_n$ converge.
4. Vrai ou faux : une chaîne irréductible a une seule loi stationnaire, qui charge tous les états.
5. Deux chaînes irréductibles et apériodiques ont $\lvert\lambda_2\rvert = 0{,}3$ et $\lvert\lambda_2\rvert = 0{,}9$. Laquelle oublie le plus vite son départ ?
6. Vrai ou faux : $\boldsymbol{\pi}^\top$ est un vecteur propre de $\mathbf{P}$ (à droite) pour la valeur propre 1.

### M26.Q3 — Espérance conditionnelle, propriété de la tour et analyse au premier pas : quelle équation pour quel nombre ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Vrai ou faux : pour deux variables discrètes, $\mathbb{E}[X \mid Y]$ est un nombre.
2. Simplifie $\mathbb{E}\big[\mathbb{E}[X \mid Y, Z] \mid Y\big]$.
3. Associe chaque nombre à son équation. Nombres : (a) la probabilité d'être absorbé par un état donné ; (b) la durée moyenne avant la fin ; (c) le nombre moyen de visites à $j$ depuis $i$. Équations : (1) $\mathbf{t} = \mathbf{1} + \mathbf{Q}\mathbf{t}$ ; (2) $(\mathbf{I} - \mathbf{Q})^{-1}$ ; (3) $\mathbf{h} = \mathbf{Q}\mathbf{h} + \mathbf{b}$.
4. Vrai ou faux : dans $\mathbf{t} = \mathbf{1} + \mathbf{Q}\mathbf{t}$, $\mathbf{Q}$ contient aussi les lignes des états absorbants.
5. Un état transitoire reste sur place avec la probabilité 0,8 et part sinon vers un état absorbant. Combien de pas y passe-t-on en moyenne, le pas de départ compris ?
6. Vrai ou faux : si, de chaque état transitoire, un état absorbant est accessible, $\mathbf{I} - \mathbf{Q}$ est inversible.

### M26.Q4 — Le facteur γ : une actualisation, ou une probabilité de continuer ? Valeur d'un état et politique 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. On arrête à chaque pas avec la probabilité $1 - \gamma = 0{,}4$. Quelle est la durée moyenne, le premier pas compris ?
2. Vrai ou faux : si l'on simule cet arrêt, il faut encore multiplier la récompense du pas $t$ par $\gamma^t$ pour estimer la valeur.
3. Vrai ou faux : le gain total sans actualisation jusqu'à cet arrêt a la même loi que le retour actualisé.
4. Vrai ou faux : la valeur d'un état est définie sans préciser de politique.
5. Dans un état $s$, une politique choisit l'action $a$ avec la probabilité 0,3 et l'action $b$ avec 0,7 ; $r(s, a) = 4$ et $r(s, b) = 10$. Que vaut $r_\pi(s)$ ?
6. Vrai ou faux : la règle ε-greedy de M11 est une politique stochastique.

### M26.Q5 — Le système de Bellman d'une politique fixée : quelles matrices, pourquoi il est inversible, quand γ = 1 est permis 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Vrai ou faux : $\mathbf{V} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$ s'écrit aussi $(\mathbf{I} - \mathbf{P})\mathbf{V} = \gamma\mathbf{r}$.
2. En une phrase : pourquoi $\mathbf{I} - \gamma\mathbf{P}$ est-elle inversible quand $\mathbf{P}$ est stochastique et $\gamma < 1$ ?
3. Vrai ou faux : si $\mathbf{P}$ est stochastique, $\mathbf{I} - \mathbf{P}$ est singulière.
4. Vrai ou faux : $\gamma = 1$ est permis quand, depuis chaque état, le processus finit avec certitude.
5. Un état absorbant rapporte 1,2 à chaque pas, et $\gamma = 0{,}6$. Que vaut sa valeur ?
6. Vrai ou faux : pour $\gamma < 1$, coder une fin par un état absorbant de récompense nulle ou par une ligne sous-stochastique donne les mêmes valeurs.

### M26.Q6 — Contraction, bornes a priori et a posteriori, itérations synchrones ou en place : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Vrai ou faux : $\mathcal{T}(\mathbf{V}) = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$ est une γ-contraction pour $\lVert\cdot\rVert_\infty$ ($\gamma < 1$).
2. $\gamma = 0{,}7$ et $\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty = 10$ : quelle borne la fiche donne-t-elle sur $\lVert\mathbf{V}_5 - \mathbf{V}\rVert_\infty$ ?
3. $\gamma = 0{,}7$ et $\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty = 0{,}03$ : quelle borne sur $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty$ ?
4. Vrai ou faux : s'arrêter dès que $\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty < \varepsilon$ garantit une erreur inférieure à $\varepsilon$.
5. Vrai ou faux : les itérations synchrones et en place donnent les mêmes $\mathbf{V}_k$.
6. Vrai ou faux : l'itération synchrone est l'itération de Richardson de pas 1 pour $(\mathbf{I} - \gamma\mathbf{P})\mathbf{V} = \mathbf{r}$.

### M26.Q7 — Un maximum dans l'opérateur : ce qui reste (contraction, point fixe unique), ce qui se perd (le système linéaire) 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. $\mathbf{x} = (3, 8, 1)$ et $\mathbf{y} = (5, 6, 4)$ : que valent $\lvert\max\mathbf{x} - \max\mathbf{y}\rvert$ et $\lVert\mathbf{x} - \mathbf{y}\rVert_\infty$ ?
2. Vrai ou faux : pour tous vecteurs, $\max\mathbf{x} - \max\mathbf{y} = \max(\mathbf{x} - \mathbf{y})$.
3. La fiche admet que, pour $\gamma < 1$, l'opérateur d'arrêt $\mathbf{V} \mapsto \max(\mathbf{g}, \mathbf{c} + \gamma\mathbf{P}\mathbf{V})$ est une γ-contraction pour $\lVert\cdot\rVert_\infty$. Vrai ou faux : il a donc un unique point fixe, et ses itérés y convergent depuis tout départ.
4. Vrai ou faux : l'équation d'arrêt optimal $\mathbf{V} = \max(\mathbf{g}, \mathbf{c} + \gamma\mathbf{P}\mathbf{V})$ se résout comme un seul système linéaire.
5. Offres indépendantes : la valeur de continuation est $C^\star = 640$ € et l'offre de la semaine vaut 600 €. Que dit la règle à seuil ?
6. Vrai ou faux : dans $C = c + \gamma\,\mathbb{E}[\max(X, C)]$, la valeur de continuation $C$ ne dépend pas de l'offre du moment.

### M26.Q8 — Des échantillons au lieu de P : moyenne de retours, pas 1/n ou constant, erreur TD, biais du maximum 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. Vrai ou faux : avec le pas $\alpha_n = \frac1n$, $m_n$ est la moyenne de $x_1, \ldots, x_n$.
2. Vrai ou faux : avec un pas constant, $m_n$ converge vers l'espérance des mesures.
3. Parmi les pas $\frac1n$, $0{,}1$, $\frac{1}{n^2}$ et $\frac{1}{\sqrt n}$, lesquels vérifient les deux conditions de Robbins-Monro ?
4. Vrai ou faux : quand $\mathbf{W} = \mathbf{V}$, chaque erreur TD est nulle.
5. Trois fournisseurs ont la même qualité réelle ; on annonce le meilleur score mesuré. Vrai ou faux : cette annonce est trop belle en moyenne.
6. On tronque les retours après $T = 20$ pas, avec $\gamma = 0{,}7$ et $\lVert\mathbf{V}\rVert_\infty = 50$. Quelle borne la fiche donne-t-elle sur le biais ?

<a id="rappels"></a>

## 🔁 Rappels

### M26.R1 — Puissances d'une matrice diagonalisable et méthode de la puissance (M12c) 🔁 ★ ⏱️ 5 min
*Fiche §1 et §2 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$.
1. Les valeurs propres de $\mathbf{A}$, et un vecteur propre pour chacune ?
2. $(\mathbf{A}^3)_{01}$, par la diagonalisation ou par le calcul direct ?
3. La méthode de la puissance part de $(1, 0)$ : vers quelle direction tend $\mathbf{A}^k\mathbf{x}_0 / \lVert\mathbf{A}^k\mathbf{x}_0\rVert$, et par combien la composante parasite est-elle multipliée à chaque pas, relativement ?
4. Vrai ou faux : la méthode de la puissance trouve la valeur propre de plus grand module.

### M26.R2 — La norme ‖·‖∞ d'une matrice, ρ(A) ≤ ‖A‖ et Aᵗ → 0 quand ρ(A) < 1 (M22), et la somme d'une série géométrique (R5) 🔁 ★ ⏱️ 8 min
*Fiche §5 et §6 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 0{,}2 & -0{,}4 \\ 0{,}5 & 0{,}1 \end{pmatrix}$.
1. $\lVert\mathbf{A}\rVert_\infty$ ?
2. Les valeurs propres de $\mathbf{A}$ et $\rho(\mathbf{A})$ ; vérifie $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert_\infty$.
3. Vrai ou faux : $\mathbf{A}^t \to \mathbf{0}$ quand $t \to \infty$.
4. Vrai ou faux : si $\rho(\mathbf{B}) < 1$, alors $\lVert\mathbf{B}\rVert_\infty < 1$.
5. $\lVert\mathbf{P}\rVert_\infty$ pour une matrice stochastique $\mathbf{P}$ ?
6. $\sum_{t \ge 0}0{,}4^t$ et $\sum_{t \ge 2}0{,}4^t$ ?

### M26.R3 — Probabilités totales et espérance d'une loi géométrique (M03, M02b) 🔁 ★ ⏱️ 5 min
*Fiche §3 et §4 · parcours C, E*

1. Un client arrive par une publicité (60 %) ou par un moteur de recherche (40 %) ; il achète avec la probabilité 0,2 dans le premier cas, 0,35 dans le second. La probabilité qu'il achète ?
2. On répète un essai qui réussit avec la probabilité 0,2, jusqu'au premier succès ; $X$ est le nombre d'essais. $\mathbb{E}[X]$ ?
3. $P(X > 3)$ ?
4. Vrai ou faux : $P(X > 5 \mid X > 2) = P(X > 3)$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- une forme comme NumPy l'affiche, comme `(7, 2)` ;
- `True` ou `False` pour un vrai ou faux.

« Valeurs exactes » veut dire : tous les chiffres, sans arrondir (ces calculs tombent juste). Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M26.1 — Des vélos en libre-service entre trois stations : matrice de transition, graphe, loi après deux et trois jours, et coût moyen du lendemain (Pf) ✏️ ★ ⏱️ 25 min
**Objectif :** écrire une matrice de transition et son graphe, faire avancer une loi en convention ligne, lire un coefficient de $\mathbf{P}^2$ sur les chemins, et moyenner un coût sur le pas suivant.
**Prérequis :** fiche §1 et §3 ; M03, M16 · **Parcours :** C, E

Une ville a trois stations de vélos : A (la gare), B (le centre) et C (en haut d'une colline), numérotées 0, 1 et 2. On suit un vélo d'un matin au suivant. Un vélo qui est à A le matin finit la journée à A avec la probabilité 0,6, à B avec 0,3, à C avec 0,1 ; un vélo de B finit à A, B ou C avec 0,3, 0,4 et 0,3 ; un vélo de C, avec 0,4, 0,2 et 0,4. Ce matin, les 200 vélos sont répartis ainsi : 80 à A, 80 à B, 40 à C ; chacun se déplace indépendamment des autres. Chaque soir, l'opérateur paie pour chaque vélo une recharge qui dépend de la station où il se trouve : 0,40 € à A, 0,80 € à B et 2 € à C (il faut monter la colline) ; on note $\mathbf{f} = (0{,}4 ;\ 0{,}8 ;\ 2)^\top$.

| | Question | Réponse attendue |
|---|---|---|
| a | $(\mathbf{P}^2)_{BC}$ : la probabilité qu'un vélo qui est à B ce matin soit à C dans deux jours | un nombre |
| b | la loi $\boldsymbol{\mu}_2$, dans deux jours, d'un vélo pris au hasard ce matin (A, B, C) | une liste de 3 nombres (valeurs exactes) |
| c | sa loi $\boldsymbol{\mu}_3$, dans trois jours | une liste de 3 nombres (valeurs exactes) |
| d | le nombre moyen de vélos à C dans trois jours | un nombre |
| e | le vecteur $\mathbf{P}\mathbf{f}$ : le coût moyen de ce soir pour un vélo qui est ce matin à A, à B ou à C (€) | une liste de 3 nombres |
| f | le coût moyen total de ce soir pour les 200 vélos (€) | un nombre |

Dans ta copie : écris $\mathbf{P}$ et dessine son graphe ; pour a), écris les trois chemins et leurs probabilités ; vérifie que chaque $\boldsymbol{\mu}_n$ a pour somme 1. Pourquoi f) vaut-il aussi $200\,\boldsymbol{\mu}_1\mathbf{f}$ ?

### Ex M26.2 — Trois opérateurs et leurs parts de marché : la loi stationnaire par un système linéaire, puis vérifier πP = π ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer une loi stationnaire par le système carré de la fiche (une équation remplacée par $\sum_j\pi_j = 1$), la vérifier et l'interpréter.
**Prérequis :** fiche §2 ; M03, M09a · **Parcours :** C, E

Chaque mois, les clients de trois opérateurs de téléphonie, Azur, Boréal et Cobalt (états 0, 1, 2), peuvent changer d'opérateur. Un client d'Azur y reste avec la probabilité 0,9 et passe chez Boréal ou chez Cobalt avec 0,05 chacun ; un client de Boréal passe chez Azur avec 0,05, reste avec 0,85 et passe chez Cobalt avec 0,1 ; un client de Cobalt passe chez Azur avec 0,2, chez Boréal avec 0,15, et reste avec 0,65. Aujourd'hui, les parts de marché sont $(0{,}45 ;\ 0{,}4 ;\ 0{,}15)$.

Écris le système $(\mathbf{P}^\top - \mathbf{I})\boldsymbol{\pi}^\top = \mathbf{0}$, remplace sa dernière équation par $\pi_0 + \pi_1 + \pi_2 = 1$, et résous-le par le pivot de Gauss (M09a), et non par la substitution de la fiche.

| | Question | Réponse attendue |
|---|---|---|
| a | la loi stationnaire $\boldsymbol{\pi}$ (Azur, Boréal, Cobalt) | une liste de 3 nombres (4 décimales) |
| b | la part de marché de Cobalt à long terme | une fraction irréductible, entre guillemets |
| c | les parts de marché dans un mois | une liste de 3 nombres (valeurs exactes) |
| d | à long terme, parmi les clients d'Azur d'un mois donné, la part de ceux qui étaient chez Cobalt le mois précédent | une fraction irréductible, entre guillemets |
| e | vrai ou faux : à long terme, le nombre de clients qui passent chaque mois d'Azur à Boréal égale le nombre de ceux qui passent de Boréal à Azur | `True` ou `False` |

Dans ta copie : écris le système et les étapes du pivot ; vérifie $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$ coordonnée par coordonnée, y compris pour l'équation que tu as retirée.

### Ex M26.3 — Trois chaînes qui posent problème, périodique, à deux classes et avec un état transitoire : lois stationnaires et comportement de Pⁿ ✏️ ★★ ⏱️ 25 min
**Objectif :** reconnaître, sur trois chaînes, ce qui empêche la convergence ou l'unicité, et calculer ce qui existe quand même.
**Prérequis :** fiche §2 ; ✏️ M26.2 · **Parcours :** C

1. **Un bac sur un lac.** À chaque pas, il traverse : de la rive nord (ports A et B) vers la rive sud (ports C et D), puis retour. Depuis A, il va en C avec la probabilité 0,7 et en D avec 0,3 ; depuis B, en C avec 0,35 et en D avec 0,65 ; depuis C, en A avec 0,9 et en B avec 0,1 ; depuis D, en A avec 0,3 et en B avec 0,7 (états A, B, C, D = 0, 1, 2, 3). Il part de A.
2. **Un site bilingue sans lien entre ses deux versions.** Un visiteur passe d'une page à l'autre sans changer de langue : pages françaises 0 et 1, pages anglaises 2 et 3. Depuis 0, il reste sur 0 avec la probabilité 0,8 et va en 1 avec 0,2 ; depuis 1, en 0 avec 0,35 et reste avec 0,65 ; depuis 2, il reste avec 0,55 et va en 3 avec 0,45 ; depuis 3, en 2 avec 0,3 et reste avec 0,7. 60 % des visiteurs arrivent sur la page 0, 40 % sur la page 2.
3. **Une période d'essai.** Un nouvel utilisateur d'une application est « à l'essai » (état 0), puis devient « régulier » (1) ou « occasionnel » (2), et ne revient jamais à l'essai. Depuis 0, il reste à l'essai avec la probabilité 0,4, devient régulier avec 0,45 et occasionnel avec 0,15 ; depuis 1, il reste régulier avec 0,9 et devient occasionnel avec 0,1 ; depuis 2, il devient régulier avec 0,4 et reste occasionnel avec 0,6.

| | Question | Réponse attendue |
|---|---|---|
| a | le bac : sa loi stationnaire (A, B, C, D) | une liste de 4 nombres (4 décimales) |
| b | le bac : la limite de $\boldsymbol{\mu}_{2k}$ quand $k \to \infty$, depuis A | une liste de 4 nombres (4 décimales) |
| c | vrai ou faux : depuis A, $\boldsymbol{\mu}_n$ converge | `True` ou `False` |
| d | le site : la limite de $\boldsymbol{\mu}_n$ pour un visiteur | une liste de 4 nombres (4 décimales) |
| e | vrai ou faux : $\frac12(\boldsymbol{\pi}_{\text{FR}} + \boldsymbol{\pi}_{\text{EN}})$, la moyenne des lois stationnaires des deux versions (chacune complétée par des 0), est une loi stationnaire du site | `True` ou `False` |
| f | l'essai : sa loi stationnaire (0, 1, 2) | une liste de 3 nombres (valeurs exactes) |

Dans ta copie : pour chaque chaîne, dis ce qui manque (l'irréductibilité ou l'apériodicité) ; montre que la loi stationnaire du bac met la moitié de sa masse au nord ; explique pourquoi $\pi_0 = 0$ pour l'essai, à partir de la première colonne de $\mathbf{P}$.

### Ex M26.4 — Un cursus en trois années, avec redoublement et abandon : la probabilité d'être diplômé et la durée moyenne des études, par l'analyse au premier pas ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer des probabilités d'absorption, des durées moyennes et des nombres de visites par l'analyse au premier pas et la matrice fondamentale.
**Prérequis :** fiche §3 ; M09a · **Parcours :** C, E

Une licence se fait en trois années, L1, L2 et L3 (états 0, 1, 2). Chaque année, un étudiant de L1 redouble avec la probabilité 0,15, passe en L2 avec 0,7 et abandonne avec 0,15 ; un étudiant de L2 est réorienté en L1 avec 0,05, redouble avec 0,15, passe en L3 avec 0,75 et abandonne avec 0,05 ; un étudiant de L3 redouble avec 0,15, obtient son diplôme avec 0,75 et abandonne avec 0,1. « Diplômé » et « abandon » sont absorbants. Les frais d'inscription sont de 170 € par an en L1 et en L2, et de 240 € par an en L3.

| | Question | Réponse attendue |
|---|---|---|
| a | les probabilités $\mathbf{h}$ d'être diplômé, depuis L1, L2 et L3 | une liste de 3 nombres (3 décimales) |
| b | $h_{\text{L1}}$, la probabilité qu'un nouvel étudiant soit diplômé | une fraction irréductible, entre guillemets |
| c | les durées moyennes $\mathbf{t}$ des études, en années, jusqu'au diplôme ou à l'abandon, depuis L1, L2 et L3 | une liste de 3 nombres (2 décimales) |
| d | le nombre moyen d'années qu'un nouvel étudiant passe en L1 | un nombre (2 décimales) |
| e | les frais d'inscription totaux moyens d'un nouvel étudiant (€) | un nombre (2 décimales) |

Dans ta copie : écris $\mathbf{Q}$ et $\mathbf{b}$, puis les systèmes $\mathbf{h} = \mathbf{Q}\mathbf{h} + \mathbf{b}$ et $\mathbf{t} = \mathbf{1} + \mathbf{Q}\mathbf{t}$, et résous-les en commençant par L3. Pour d) et e), calcule la première ligne $\mathbf{n}$ de $\mathbf{N} = (\mathbf{I} - \mathbf{Q})^{-1}$ en résolvant $\mathbf{n}(\mathbf{I} - \mathbf{Q}) = (1, 0, 0)$, et vérifie que sa somme redonne $t_{\text{L1}}$.

### Ex M26.5 — Un abonné qui peut résilier chaque mois : durée géométrique, revenu total moyen, et le même nombre comme revenu actualisé ✏️ ★ ⏱️ 20 min
**Objectif :** relier une durée géométrique, un gain total sans actualisation et un gain actualisé, sur un exemple où les deux chemins donnent le même nombre.
**Prérequis :** fiche §4 ; M02b, R5 · **Parcours :** C, E

Un service de streaming facture 9 € chaque mois commencé, le premier mois compris, payé aujourd'hui. À la fin de chaque mois, l'abonné résilie avec la probabilité 0,3, indépendamment des mois précédents : il continue avec la probabilité $\gamma = 0{,}7$. On numérote les mois à partir de 0 (le mois en cours) et l'on note $N$ son dernier mois : il paie $N + 1$ mois.

| | Question | Réponse attendue |
|---|---|---|
| a | la probabilité qu'il paie le 6ᵉ mois (le mois 5) | un nombre (4 décimales) |
| b | le nombre moyen de mois payés, $\mathbb{E}[N + 1]$ | une fraction irréductible, entre guillemets |
| c | le revenu total moyen d'un abonné, sans actualisation (€) | un nombre |
| d | la valeur actualisée, avec $\gamma = 0{,}7$ par mois, de 9 € payés chaque mois sans fin, le premier aujourd'hui (€) | un nombre |
| e | la probabilité que le revenu total d'un abonné soit inférieur à la moyenne c) | un nombre (3 décimales) |
| f | le revenu total moyen si le premier mois est offert (€) | un nombre |

Dans ta copie : écris c) comme $\sum_{t \ge 0}9\,P(N \ge t)$ et d) comme $\sum_{t \ge 0}9\,\gamma^t$ : pourquoi est-ce la même somme ? Pourquoi la majorité des abonnés rapporte-t-elle moins que la moyenne ?

### Ex M26.6 — Une machine qui s'use, deux politiques d'entretien : P_π et r_π, deux systèmes de Bellman 3 × 3, et la valeur d'une action ✏️ ★★ ⏱️ 35 min
**Objectif :** construire la chaîne et les récompenses induites par une politique, résoudre deux systèmes de Bellman $3 \times 3$, et calculer la valeur d'une action.
**Prérequis :** fiche §4 et §5 ; M09a · **Parcours :** C, E

Un atelier suit chaque mois l'état d'une machine : neuve (0), usée (1), en panne (2). Les gains sont en milliers d'euros, actualisés avec $\gamma = 0{,}6$ par mois.
- **Neuve** (une seule action, « continuer ») : elle rapporte 10 dans le mois ; le mois suivant, elle est encore neuve avec la probabilité 0,7, usée avec 0,3.
- **Usée**, deux actions. « Continuer » : le mois suivant, elle est encore usée avec la probabilité 0,65 et en panne avec 0,35 ; elle rapporte 6 si elle reste usée, et 3 si elle tombe en panne pendant le mois : $r(1, \text{continuer}, 1) = 6$ et $r(1, \text{continuer}, 2) = 3$. « Entretenir » : elle produit 6, mais l'entretien coûte 4, soit un gain de 2 ; le mois suivant, elle est neuve avec la probabilité 0,95, et en panne avec 0,05 (l'entretien a raté).
- **En panne** (une seule action, « réparer ») : la réparation coûte 8, un gain de $-8$ ; le mois suivant, la machine est neuve avec la probabilité 0,8, et encore en panne avec 0,2.

La politique $\pi_A$ n'entretient jamais la machine ; la politique $\pi_B$ entretient toute machine usée.

| | Question | Réponse attendue |
|---|---|---|
| a | $r(1, \text{continuer})$, la récompense moyenne de « continuer » pour une machine usée | un nombre |
| b | la matrice $\mathbf{P}_{\pi_B}$ | une matrice $3 \times 3$ |
| c | $\mathbf{V}^{\pi_A}$ (neuve, usée, en panne) | une liste de 3 nombres (2 décimales) |
| d | $\mathbf{V}^{\pi_B}$ (neuve, usée, en panne) | une liste de 3 nombres (2 décimales) |
| e | $Q^{\pi_B}(1, \text{continuer})$ | un nombre (2 décimales) |
| f | vrai ou faux : $Q^{\pi_B}(1, \text{entretenir}) = V^{\pi_B}(1)$ | `True` ou `False` |

Dans ta copie : écris $\mathbf{P}_{\pi_A}$, $\mathbf{r}_{\pi_A}$ et $\mathbf{r}_{\pi_B}$, puis les deux systèmes $(\mathbf{I} - \gamma\mathbf{P})\mathbf{V} = \mathbf{r}$, et résous-les (exprime $V(2)$ en fonction de $V(0)$, puis $V(1)$, puis trouve $V(0)$). Dis en une phrase ce que mesure le nombre de e).

### Ex M26.7 — Les itérés de Bellman de la machine de M26.6 : trois pas synchrones puis en place, comparés à la solution, et le nombre d'itérations qui garantit 10⁻³ ✏️ ★★ ⏱️ 30 min
**Objectif :** itérer l'opérateur de Bellman à la main, synchrone puis en place, mesurer l'erreur, et choisir un nombre d'itérations par les bornes a priori et a posteriori.
**Prérequis :** fiche §6 ; ✏️ M26.6, R6 · **Parcours :** C, E

On reprend la machine de M26.6 sous la politique $\pi_A$ (jamais d'entretien), avec $\gamma = 0{,}6$, et sa valeur $\mathbf{V}^{\pi_A}$ (ta réponse c, avec toutes ses décimales). On part de $\mathbf{V}_0 = \mathbf{0}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{V}_3$, après trois pas synchrones | une liste de 3 nombres (valeurs exactes) |
| b | l'erreur $\lVert\mathbf{V}_3 - \mathbf{V}^{\pi_A}\rVert_\infty$ | un nombre (4 décimales) |
| c | $\mathbf{W}_3$, après trois balayages en place depuis $\mathbf{W}_0 = \mathbf{0}$, dans l'ordre neuve, usée, en panne | une liste de 3 nombres (valeurs exactes) |
| d | l'erreur $\lVert\mathbf{W}_3 - \mathbf{V}^{\pi_A}\rVert_\infty$ | un nombre (4 décimales) |
| e | le plus petit nombre $k$ d'itérations synchrones pour lequel la borne a priori garantit une erreur au plus $10^{-3}$, depuis $\mathbf{V}_0 = \mathbf{0}$ | un entier |
| f | le seuil $s$ du critère a posteriori : s'arrêter dès que $\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty \le s$ garantit une erreur au plus $10^{-3}$ | une fraction irréductible, entre guillemets |
| g | la borne a posteriori de l'erreur de $\mathbf{V}_3$ | un nombre (2 décimales) |

Dans ta copie : écris $\mathbf{V}_1$, $\mathbf{V}_2$, $\mathbf{W}_1$ et $\mathbf{W}_2$, et compare g) à b). Le notebook (🔨 M26.19) dira combien d'itérations il faut vraiment : prédis si ce sera nettement moins que e), en regardant ce que $\gamma\mathbf{P}$ fait au vecteur $\mathbf{1}$.

### Ex M26.8 — Vendre une voiture d'occasion : offres au hasard, coût d'attente, valeur de continuation et règle à seuil ✏️ ★★ ⏱️ 30 min
**Objectif :** résoudre par intervalles une équation d'arrêt optimal à offres discrètes, en déduire la règle à seuil, et la comparer à une règle fixée, évaluée par une équation linéaire.
**Prérequis :** fiche §7 · **Parcours :** C, E

Une personne vend sa voiture. Chaque semaine, elle reçoit une offre $X$, indépendante des précédentes : 3 000 € avec la probabilité 0,3, 4 000 € avec 0,3, 5 000 € avec 0,2, 7 000 € avec 0,2. Accepter : elle encaisse l'offre, et c'est fini. Refuser : l'offre est perdue, la semaine d'annonce et d'assurance coûte 50 € ($c = -50$), et elle attend l'offre suivante. Pressée d'acheter une autre voiture, elle actualise avec $\gamma = 0{,}85$ par semaine. Comme dans la fiche, la valeur de continuation $C$ vérifie $C = c + \gamma\,\mathbb{E}[\max(X, C)]$.

| | Question | Réponse attendue |
|---|---|---|
| a | l'offre moyenne $\mathbb{E}[X]$ (€) | un nombre |
| b | la valeur de continuation $C^\star$ (€) | un nombre (arrondi à l'euro) |
| c | les offres qu'elle accepte, dans l'ordre croissant | une liste d'entiers |
| d | la valeur de la voiture avant la première offre (€) | un nombre (arrondi à l'euro) |
| e | la valeur de continuation de la règle fixée « accepter toute offre d'au moins 4 000 € » (€) | un nombre (arrondi à l'euro) |
| f | ce que coûte cette règle en moyenne : $C^\star$ moins la valeur de e) (€) | un nombre (arrondi à l'euro) |

Dans ta copie : écris $\mathbb{E}[\max(X, C)]$ quand $C$ est entre 3 000 et 4 000 €, puis entre 4 000 et 5 000 € ; résous l'équation dans chaque cas, et dis pourquoi une seule solution convient. Compare la solution rejetée à e).

### Ex M26.9 — Le meilleur de deux fournisseurs sur des mesures bruitées : le maximum surestime, l'estimateur double non ✏️ ★★ ⏱️ 25 min
**Objectif :** mesurer le biais du maximum avec des écarts-types différents puis des moyennes inégales, et voir l'estimateur double devenir pessimiste.
**Prérequis :** fiche §8 ; M02b, M02c · **Parcours :** C

Une entreprise compare la durée de vie des batteries de deux fournisseurs, A et B. Elle teste 16 batteries de A et 9 de B ; la durée de vie d'une batterie a un écart-type $\sigma_0 = 30$ h autour de la moyenne de son fournisseur, et les tests sont indépendants. Elle note $\hat A$ et $\hat B$ les durées moyennes mesurées (supposées gaussiennes), choisit le fournisseur dont la moyenne mesurée est la plus grande, et annonce $\max(\hat A, \hat B)$. On donne $\Phi(0{,}8) \approx 0{,}788145$, et l'on admet, pour $D \sim \mathcal{N}(\delta, s^2)$ : $\mathbb{E}\lvert D\rvert = s\sqrt{2/\pi}\;e^{-\delta^2/(2s^2)} + \delta\big(1 - 2\Phi(-\delta/s)\big)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les écarts-types $\sigma_A$ et $\sigma_B$ de $\hat A$ et de $\hat B$ (h) | une liste de 2 nombres |
| b | si les deux fournisseurs ont la même durée de vie moyenne $\mu$ : le biais $\mathbb{E}[\max(\hat A, \hat B)] - \mu$ (h) | un nombre (2 décimales) |
| c | si A dure en moyenne 1 010 h et B 1 000 h : la probabilité de choisir B | un nombre (3 décimales) |
| d | dans le cas de c) : la durée de vie moyenne vraie du fournisseur choisi, en moyenne sur les expériences (h) | un nombre (2 décimales) |
| e | vrai ou faux : dans le cas de c), si l'entreprise remesure le fournisseur choisi sur de nouvelles batteries (l'estimateur double), elle annonce en moyenne moins que 1 010 h | `True` ou `False` |
| f | dans le cas de c) : $\mathbb{E}[\max(\hat A, \hat B)]$ (h) | un nombre (2 décimales) |

Dans ta copie : adapte la démonstration de $\mathbb{E}[\max(Z_1, Z_2)] = \frac{1}{\sqrt\pi}$ de la fiche pour obtenir b) ; justifie d) par la loi de l'espérance totale ; range f), 1 010 h et d).

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M26.10 — L'analyse au premier pas démontrée : t = 1 + Qt et h = Qh + b, et I − Q inversible dès que la fin est possible depuis chaque état ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer le théorème du §3, de l'estimation des puissances de $\mathbf{Q}$ jusqu'aux deux systèmes.
**Prérequis :** fiche §3 ; M22 · **Parcours :** C

Une chaîne a des états transitoires $1, \ldots, m$ et des états absorbants ; $\mathbf{Q}$ est le bloc des transitoires et $\mathbf{b}$ la colonne des probabilités de passer en un pas dans un état absorbant fixé $a$. On suppose que, depuis chaque état transitoire, un état absorbant est accessible. $T$ est le nombre de pas passés parmi les transitoires avant l'absorption (le départ compris), $t_i = \mathbb{E}[T \mid S_0 = i]$ et $h_i = P(\text{absorption en } a \mid S_0 = i)$.
1. Montre qu'il existe un entier $n \ge 1$ et un $\varepsilon > 0$ tels que, depuis chaque état transitoire, la probabilité d'être absorbé en au plus $n$ pas soit au moins $\varepsilon$. Déduis-en que chaque ligne de $\mathbf{Q}^n$ a une somme au plus $1 - \varepsilon$, puis que $\lVert\mathbf{Q}^{kn}\rVert_\infty \le (1 - \varepsilon)^k$.
2. Déduis-en que $\mathbf{Q}^t \to \mathbf{0}$, que $\mathbf{I} - \mathbf{Q}$ est inversible, et que $P(T > kn \mid S_0 = i) \le (1 - \varepsilon)^k$ : $T$ est fini avec la probabilité 1, et $t_i < \infty$.
3. En conditionnant sur $S_1$, démontre $t_i = 1 + \sum_j q_{ij}\,t_j$ ; dis où sert la propriété de Markov.
4. Démontre de même $h_i = b_i + \sum_j q_{ij}\,h_j$, et conclus : $\mathbf{t}$ et $\mathbf{h}$ sont les uniques solutions de leurs systèmes.

### Ex M26.11 — V = Σ γᵗPᵗr est l'unique solution du système de Bellman : I − γP inversible, série de Neumann démontrée pour γP, et (1 − γ)(I − γP)⁻¹ stochastique ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer en entier le théorème et la propriété du §5 : l'inversibilité, la série de Neumann et la loi d'occupation actualisée.
**Prérequis :** fiche §4 et §5 ; M22 · **Parcours :** C, E

$\mathbf{P}$ est une matrice $m \times m$ stochastique ou sous-stochastique (coefficients $\ge 0$, lignes de somme au plus 1), et $0 \le \gamma < 1$.
1. Montre que $\lVert\gamma\mathbf{P}\rVert_\infty \le \gamma$, puis que chaque coefficient de $\gamma^t\mathbf{P}^t$ est compris entre 0 et $\gamma^t$.
2. On pose $\mathbf{S}_n = \sum_{t=0}^{n}\gamma^t\mathbf{P}^t$. Montre que $\mathbf{S}_n(\mathbf{I} - \gamma\mathbf{P}) = (\mathbf{I} - \gamma\mathbf{P})\mathbf{S}_n = \mathbf{I} - \gamma^{n+1}\mathbf{P}^{n+1}$.
3. Montre que $\mathbf{S}_n$ converge coefficient par coefficient vers une matrice $\mathbf{S}$, et que $\mathbf{S}(\mathbf{I} - \gamma\mathbf{P}) = (\mathbf{I} - \gamma\mathbf{P})\mathbf{S} = \mathbf{I}$ : $\mathbf{I} - \gamma\mathbf{P}$ est inversible, d'inverse $\sum_{t \ge 0}\gamma^t\mathbf{P}^t$. Déduis-en que $\mathbf{V} = \sum_{t \ge 0}\gamma^t\mathbf{P}^t\mathbf{r}$ est l'unique solution de $\mathbf{V} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$.
4. Pour $\mathbf{P}$ stochastique, montre que $\mathbf{M} = (1 - \gamma)(\mathbf{I} - \gamma\mathbf{P})^{-1}$ est stochastique : ses coefficients sont positifs ou nuls (par la série), et $\mathbf{M}\mathbf{1} = \mathbf{1}$ (calcule d'abord $(\mathbf{I} - \gamma\mathbf{P})\mathbf{1}$). Que peut-on dire de $\mathbf{M}\mathbf{1}$ si $\mathbf{P}$ est seulement sous-stochastique ?

### Ex M26.12 — L'opérateur de Bellman d'une politique fixée est une γ-contraction pour ‖·‖∞ ; bornes a priori et a posteriori ; le maximum est 1-lipschitzien ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer les bornes d'erreur de l'itération de Bellman, la contraction d'un balayage en place, et deux extensions du lemme du maximum de la fiche.
**Prérequis :** fiche §6 et §7 ; M22 · **Parcours :** C, E

$\mathbf{P}$ est stochastique ou sous-stochastique, $0 \le \gamma < 1$, $\mathcal{T}(\mathbf{V}) = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$, $\mathbf{V}$ est son point fixe, et $\mathbf{V}_{k+1} = \mathcal{T}(\mathbf{V}_k)$. Tu peux utiliser la contraction démontrée dans la fiche (§6) et le lemme du maximum (§7).
1. **A priori.** Montre $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty \le \gamma^k\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty$ par récurrence sur $k$.
2. **A posteriori.** Montre $\lVert\mathbf{V}_{k-1} - \mathbf{V}\rVert_\infty \le \frac{1}{1 - \gamma}\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty$ (passe par $\mathbf{V}_k$), puis $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty \le \frac{\gamma}{1 - \gamma}\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty$. Déduis-en le critère d'arrêt de la fiche.
3. **En place.** Un balayage en place transforme $\mathbf{U}$ en $\mathbf{U}'$ : pour $i = 1, \ldots, m$ dans l'ordre, $U'_i = r_i + \gamma\big(\sum_{j < i}p_{ij}U'_j + \sum_{j \ge i}p_{ij}U_j\big)$. Pour deux vecteurs $\mathbf{U}$ et $\mathbf{W}$ et leurs images $\mathbf{U}'$ et $\mathbf{W}'$, montre par récurrence sur $i$ que $\lvert U'_i - W'_i\rvert \le \gamma\lVert\mathbf{U} - \mathbf{W}\rVert_\infty$. Conclus : un balayage est une γ-contraction pour $\lVert\cdot\rVert_\infty$, et ses itérés convergent vers $\mathbf{V}$ (vérifie que $\mathbf{V}$ est un point fixe du balayage).
4. **La k-ième plus grande coordonnée.** Pour $\mathbf{x} \in \mathbb{R}^n$, on note $x_{(k)}$ sa $k$-ième plus grande coordonnée ($x_{(1)} = \max\mathbf{x}$ ; la médiane de 5 nombres est $x_{(3)}$). Montre $\lvert x_{(k)} - y_{(k)}\rvert \le \lVert\mathbf{x} - \mathbf{y}\rVert_\infty$.
5. **Le supremum d'une famille.** $f$ et $g$ sont deux fonctions bornées sur un ensemble $E$ quelconque. Montre $\big\lvert\sup_E f - \sup_E g\big\rvert \le \sup_E\lvert f - g\rvert$.

### Ex M26.13 — L'erreur TD se télescope : Σ γᵏ δ_{t+k} = G_t − V(S_t) ; une récompense ajoutée γΦ(s′) − Φ(s) décale chaque valeur de −Φ(s) ∂ ★★ ⏱️ 20 min
**Objectif :** rédiger les deux télescopages du §8 avec leurs indices, puis passer du retour à la valeur.
**Prérequis :** fiche §8 ; R4 (la notation Σ) · **Parcours :** C

Un épisode d'une chaîne finit au pas $T$ : on observe $S_0, R_0, S_1, R_1, \ldots, R_{T-1}, S_T$, où $S_T$ est l'état final. $V$ est une fonction quelconque des états, nulle en tout état final, et $\delta_t = R_t + \gamma V(S_{t+1}) - V(S_t)$ pour $t < T$ ; $G_t = \sum_{k=0}^{T-t-1}\gamma^kR_{t+k}$.
1. Pour $t < T$, sépare $\sum_{k=0}^{T-t-1}\gamma^k\delta_{t+k}$ en une somme en $R$ et une somme en $V$, et montre que la seconde vaut $-V(S_t)$ : $\sum_{k=0}^{T-t-1}\gamma^k\delta_{t+k} = G_t - V(S_t)$. Dis où sert $V(S_T) = 0$.
2. **Une récompense ajoutée.** $\Phi$ est une fonction des états, nulle en tout état final, et l'on remplace chaque récompense par $R'_t = R_t + \gamma\Phi(S_{t+1}) - \Phi(S_t)$. Montre que le nouveau retour vaut $G'_t = G_t - \Phi(S_t)$.
3. On suppose que, depuis chaque état, l'épisode finit avec la probabilité 1, et que les retours sont intégrables. En passant à l'espérance sachant $S_0 = s$, montre que la valeur de chaque état non final, pour les nouvelles récompenses, est $V(s) - \Phi(s)$, où $V$ est la valeur pour les récompenses d'origine.

<a id="reflexion"></a>

## 🗣️ 🔗 Explication et pont

### Ex M26.14 — Pont : d'une politique stochastique à la chaîne qu'elle induit, P_π = Σ_a π(a | s) P_a et r_π avec des tableaux à trois axes (actions, états, états), puis Q^π(s, a) et r(s, a, s′) 🔗 ★★ ⏱️ 25 min
**Objectif :** passer des sommes $\sum_{s'}P(s' \mid s, a)\,[\ldots]$ des livres d'apprentissage par renforcement à des opérations sur des tableaux à trois axes, et calculer la chaîne induite, sa valeur et la valeur d'une action.
**Prérequis :** fiche §4 et §5 ; M20 · **Parcours :** C, E

Une salle de sport suit chaque mois ses adhérents : fidèle (0), hésitant (1), parti (2, absorbant). Elle a deux actions : ne rien faire (0) ou offrir une remise de 30 % sur le mois suivant (1). On range le modèle comme le ferait un notebook : `P` de forme (2, 3, 3), avec `P[a, s, s2]` $= \mathbf{P}_a(s, s')$ ; `R` de même forme, avec `R[a, s, s2]` $= r(s, a, s')$ ; `pi` de forme (3, 2), avec `pi[s, a]` $= \pi(a \mid s)$.
$$\mathbf{P}_0 = \begin{pmatrix} 0{,}9 & 0{,}1 & 0 \\ 0{,}3 & 0{,}4 & 0{,}3 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \mathbf{P}_1 = \begin{pmatrix} 0{,}95 & 0{,}05 & 0 \\ 0{,}55 & 0{,}35 & 0{,}1 \\ 0 & 0 & 1 \end{pmatrix}.$$
La cotisation du mois suivant n'est perçue que si l'adhérent ne part pas : depuis un fidèle ou un hésitant, $r(s, 0, s') = 30$ € et $r(s, 1, s') = 21$ € quand $s'$ est « fidèle » ou « hésitant », et 0 quand $s'$ est « parti » ; depuis « parti », tout vaut 0. La politique : rien pour un fidèle ; pour un hésitant, la remise avec la probabilité 0,4 et rien avec 0,6 ; rien pour un parti. On prend $\gamma = 0{,}85$.

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de `r_sa = (P * R).sum(axis=2)` | une forme |
| b | le tableau `r_sa`, de lignes « rien » et « remise », de colonnes fidèle, hésitant, parti | une matrice $2 \times 3$ |
| c | $\mathbf{r}_\pi$ (fidèle, hésitant, parti) | une liste de 3 nombres |
| d | la ligne « hésitant » de $\mathbf{P}_\pi$ | une liste de 3 nombres |
| e | $\mathbf{V}^\pi$ (fidèle, hésitant, parti) | une liste de 3 nombres (2 décimales) |
| f | $Q^\pi(0, \text{remise})$ | un nombre (2 décimales) |
| g | vrai ou faux : sans l'état « parti », la matrice $\mathbf{P}_\pi$ restreinte à fidèle et hésitant est sous-stochastique, et donne les mêmes valeurs pour ces deux états | `True` ou `False` |

Dans ta copie : écris $r(s, a) = \sum_{s'}\mathbf{P}_a(s, s')\,r(s, a, s')$ comme une somme, puis comme une opération sur `P` et `R` ; écris $\mathbf{P}_\pi$ et $\mathbf{r}_\pi$ avec `np.einsum` (indices `s`, `a`, `t`) ; résous le système de e). Dis en une phrase ce que mesure f).

### Ex M26.15 — Expliquer avec une image hors informatique pourquoi une chaîne qui mélange oublie son état de départ 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule l'oubli du départ, la loi stationnaire et ce qui peut les empêcher.
**Prérequis :** fiche §2 · **Parcours :** C, E

Une amie te demande pourquoi, au bout de quelques semaines, on ne peut plus deviner d'où est partie une chaîne de Markov « qui mélange bien ».

Réponds-lui en 6 à 10 phrases, sans formule, avec une image hors informatique de ton choix (une goutte d'encre dans un verre d'eau qu'on remue, un paquet de cartes qu'on bat, les visiteurs d'un musée…) : ce que sont l'état de départ et la loi de la chaîne ; pourquoi chaque pas mélange un peu les possibilités ; pourquoi la loi finit par ne plus bouger ; ce qui peut empêcher l'oubli (deux parties qui ne communiquent pas, un mouvement trop régulier) ; et ce qui fixe la vitesse de l'oubli. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M26.E1 — « Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que se passe-t-il pour γ = 1 ? » 💼 ★ ⏱️ 10 min
*Fiche §5 · parcours C*

« Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que se passe-t-il pour γ = 1 ? »

Ta réponse doit dire d'où vient ce système (la valeur d'une politique fixée), l'argument de norme ($\lVert\gamma\mathbf{P}\rVert_\infty = \gamma$, donc pas de valeur propre 1 pour $\gamma\mathbf{P}$, ou la série de Neumann), ce que cela donne en pratique (une solution unique, `np.linalg.solve`, l'itération qui converge en $\gamma^k$), le cas $\gamma = 1$ sans fin ($\mathbf{P}\mathbf{1} = \mathbf{1}$, une matrice singulière, une somme qui diverge), le cas $\gamma = 1$ avec une fin sûre (des lignes sous-stochastiques, un système inversible), et pourquoi le conditionnement se dégrade quand $\gamma$ approche 1.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m26_markov_bellman/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M26.16 | La loi d'une chaîne après n pas, en convention ligne · `n_step_distribution` | 🔨 | ★ | 20 | C, E |
| M26.17 | La loi stationnaire par un système linéaire, et le refus d'une chaîne qui en a plusieurs · `stationary_distribution` | 🔨 | ★★ | 25 | C, E |
| M26.18 | Le système de Bellman d'une politique fixée, avec une fin possible (matrice sous-stochastique) et γ = 1 quand la fin est sûre · `bellman_linear_solve` | 🔨 | ★★ | 25 | C, E |
| M26.19 | Les itérés de l'opérateur de Bellman d'une politique fixée (Richardson de pas 1) · `bellman_fixed_point_iterates` | 🔨 | ★ | 20 | C, E |
| M26.20 | La loi stationnaire de trois façons, `np.linalg.eig` sur Pᵀ, `scipy.linalg.null_space` et la méthode de la puissance, sur le surfeur aléatoire d'un web de six pages | 📦 | ★ | 20 | C |
| M26.21 | Prédire la somme des lignes de (1 − γ)(I − γP)⁻¹, puis leur limite quand γ tend vers 1, et vérifier | 🔮 | ★ | 15 | C, E |
| M26.22 | Le biais du maximum par simulation : k fournisseurs de même qualité, n mesures chacun, le meilleur mesuré contre l'estimateur double | 🔬 | ★★ | 20 | C |
| M26.23 | La loi d'une chaîne au fil des pas depuis trois départs, et ‖μ_n − π‖₁ en échelle logarithmique contre \|λ₂\|ⁿ | 🎨 | ★ | 15 | C |
| M26.24 | Chasse à l'erreur : une matrice lue dans la mauvaise convention, une loi stationnaire non normalisée, un état final qui rapporte encore, γ = 1 sans fin | 🐛 | ★ | 25 | C, E |
| M26.25 | Un test de propriété : πP = π, et pour `bellman_fixed_point_iterates`, V_k − V tenu par γᵏ‖V₀ − V‖∞ et V = r + γPV pour la limite, sur des chaînes tirées au hasard | 🛠️ | ★ | 20 | C |
| M26.26 | Défi : estimer la valeur d'un état à 0,01 près en simulant l'arrêt géométrique (continuer avec la probabilité γ) et en sommant les récompenses sans actualisation, sous un budget de pas simulés | 🏆 | ★★★ | 30 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les quatre 🔨 complètent ta copie `mon_travail/mymath/markov.py` (**mymath :** `markov.py`), dont la docstring du module dit ce qui est permis : NumPy, mais de `np.linalg` seulement `solve` et `matrix_rank`, et seulement dans `stationary_distribution` et `bellman_linear_solve` ; ni `np.linalg.matrix_power`, `eig`, `eigvals`, `inv`, ni SciPy ; et ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de sa fonction dans `tests/test_m26_markov.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.markov.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier (les vélos, les opérateurs, le bac, le site, l'essai, le cursus, la machine) sont recopiées dans une cellule du notebook.

**M26.16 · 🔨 `n_step_distribution(P, mu0, n)`.** Écris la loi $\boldsymbol{\mu}_n = \boldsymbol{\mu}_0\mathbf{P}^n$ : contrôle `P` (carrée, finie, coefficients $\ge 0$, lignes de somme 1 à $10^{-9}$ près), `mu0` (une loi à $m$ coordonnées, de somme 1 à $10^{-9}$ près) et `n` (un entier $\ge 0$, ni un booléen ni un flottant comme `2.0`), puis fais $n$ produits `mu @ P` (ou l'élévation au carré que suggère le TODO) ; pour $n = 0$, rends une copie flottante de `mu0` ; lance le groupe de tests de `n_step_distribution`. Ensuite, avec ta fonction : a) les lois des vélos de M26.1 dans deux et trois jours, à comparer à tes réponses b) et c) ; b) pour le bac de M26.3, depuis A : $\boldsymbol{\mu}_{100}$ et $\boldsymbol{\mu}_{101}$, et vrai ou faux, $\boldsymbol{\mu}_{100}$ est à $10^{-12}$ près ta réponse b) de M26.3 ; c) vrai ou faux : pour les vélos, `n_step_distribution(P, n_step_distribution(P, mu0, 4), 6)` et `n_step_distribution(P, mu0, 10)` coïncident à $10^{-12}$ près (Chapman-Kolmogorov). Ce qu'il faut observer : la loi des vélos se fixe en quelques jours ; celle du bac alterne sans fin entre les deux rives.

**M26.17 · 🔨 `stationary_distribution(P)`.** Écris la loi stationnaire par le système carré de la fiche : `A = P.T - I`, dont la dernière ligne est remplacée par des 1, et `b = (0, …, 0, 1)` ; lève une `ValueError` si `np.linalg.matrix_rank(A) < m` ; sinon `np.linalg.solve(A, b)`, les coordonnées négatives dues aux arrondis mises à 0, puis la division par la somme ; lance le groupe de tests. Ensuite : a) la loi stationnaire des trois opérateurs de M26.2, à comparer à ta réponse a) ; b) celle du bac de M26.3, à comparer à ta réponse a) (la chaîne est périodique, mais sa loi stationnaire est unique : ta fonction l'accepte) ; c) vrai ou faux : ta fonction refuse le site bilingue de M26.3 par une `ValueError` ; d) la loi de la période d'essai de M26.3, et vrai ou faux, sa coordonnée 0 est inférieure à $10^{-12}$. Ce qu'il faut observer : le système voit l'unicité, pas la période ; un état transitoire reçoit 0.

**M26.18 · 🔨 `bellman_linear_solve(P, r, gamma)`.** Écris la solution de $(\mathbf{I} - \gamma\mathbf{P})\mathbf{V} = \mathbf{r}$ : contrôle `P` (carrée, finie, coefficients $\ge 0$, lignes de somme au plus $1 + 10^{-9}$), `r` (1-D, $m$ coordonnées) et `gamma` (un nombre de $[0, 1]$, pas un booléen) ; pour `gamma == 1`, lève une `ValueError` si `np.linalg.matrix_rank(I - P) < m` ; puis `np.linalg.solve` ; lance le groupe de tests. Ensuite : a) les valeurs des deux politiques de la machine de M26.6, à comparer à tes réponses c) et d) ; b) le cursus de M26.4 avec $\gamma = 1$ et $\mathbf{P} = \mathbf{Q}$ (les trois années, aux lignes sous-stochastiques) : les durées moyennes ($\mathbf{r} = \mathbf{1}$) et les probabilités d'être diplômé ($\mathbf{r} = \mathbf{b}$), à comparer à tes réponses c) et a) ; c) le cursus avec ses deux états absorbants gardés comme états (une matrice $5 \times 5$, dans l'ordre L1, L2, L3, diplômé, abandon, et les frais $(170, 170, 240, 0, 0)$) : vrai ou faux, ta fonction le refuse pour $\gamma = 1$ ; avec $\gamma = 0{,}96$, les frais actualisés depuis L1, et vrai ou faux, la matrice $3 \times 3$ $\mathbf{Q}$ avec les frais $(170, 170, 240)$ donne les mêmes trois premières valeurs à $10^{-12}$ près ; d) l'abonné de M26.5 de deux façons, une ligne qui finit avec $\gamma = 1$ (`P = [[0.7]]`) et un état qui ne finit jamais avec $\gamma = 0{,}7$ (`P = [[1.0]]`), avec `r = [9]` : les deux valeurs, à comparer à tes réponses c) et d). Ce qu'il faut observer : $\gamma\mathbf{P}$ et une ligne qui finit jouent le même rôle ; avec $\gamma = 1$, un état absorbant gardé comme état rend le système singulier.

**M26.19 · 🔨 `bellman_fixed_point_iterates(P, r, gamma, V0=None, n_steps=10)`.** Écris les itérés synchrones $\mathbf{V}_{k+1} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}_k$, un par ligne d'un tableau de forme $(N + 1, m)$ dont la ligne 0 est `V0` (le vecteur nul s'il manque) ; mêmes contrôles que `bellman_linear_solve`, sans le cas singulier, plus `V0` (1-D, $m$ coordonnées) et `n_steps` (un entier $\ge 0$) ; aucune vérification de convergence ; lance le groupe de tests. Ensuite, sur la machine de M26.6 sous $\pi_A$ ($\gamma = 0{,}6$) : a) les lignes 1 à 3 depuis $\mathbf{V}_0 = \mathbf{0}$, à comparer à ta réponse a) de M26.7 ; b) le nombre d'itérations synchrones qu'il faut vraiment pour que $\lVert\mathbf{V}_k - \mathbf{V}^{\pi_A}\rVert_\infty \le 10^{-3}$, à comparer à ta réponse e) de M26.7 ; puis le premier $k$ où le critère a posteriori de M26.7 f) arrête l'itération, et vrai ou faux, l'erreur y est bien au plus $10^{-3}$ ; c) écris `in_place_sweeps_19(P, r, gamma, V0, n_sweeps)`, qui rend le tableau de forme $(n_{\text{sweeps}} + 1, m)$ des balayages en place (les états dans l'ordre, chaque nouvelle valeur servant aussitôt ; la ligne 0 est `V0`) : sa ligne 3 depuis 0, à comparer à ta réponse c) de M26.7, et le nombre de balayages qu'il faut pour $10^{-3}$. Ce qu'il faut observer : la borne a priori est presque atteinte (l'écart garde une composante le long de $\mathbf{1}$, que $\gamma\mathbf{P}$ multiplie exactement par $\gamma$), et l'itération en place gagne quelques balayages.

**M26.20 · 📦 La loi stationnaire de trois façons.** Un petit web a six pages, numérotées 1 à 6 (états 0 à 5). Les liens : $1 \to 2$, $1 \to 3$ ; $2 \to 4$ ; $3 \to 1$, $3 \to 4$, $3 \to 5$ ; $4 \to 1$, $4 \to 3$ ; $5 \to 4$, $5 \to 6$ ; la page 6 n'a aucun lien. Construis $\mathbf{L}$ (le surfeur choisit au hasard un lien de sa page ; sur la page 6, il va sur une page quelconque, uniformément) puis $\mathbf{P}_d = d\,\mathbf{L} + \frac{1 - d}{6}\mathbf{1}\mathbf{1}^\top$ avec $d = 0{,}85$. Calcule sa loi stationnaire de trois façons : (1) par `np.linalg.eig(P_d.T)`, en prenant le vecteur propre de la valeur propre la plus proche de 1, sa partie réelle, divisée par sa somme ; (2) par `scipy.linalg.null_space(P_d.T - np.eye(6))`, qui doit rendre une seule colonne, divisée par sa somme ; (3) par la méthode de la puissance, dans `power_stationary_20(P, tol)`, qui part de la loi uniforme, fait $\mathbf{x} \leftarrow \mathbf{x}\mathbf{P}$ jusqu'à ce que $\lVert\mathbf{x}_{k+1} - \mathbf{x}_k\rVert_1 < $ `tol`, et rend la loi et le nombre de pas. Relève : a) le PageRank des six pages (4 décimales) ; b) vrai ou faux : les trois calculs et ta `stationary_distribution` coïncident à $10^{-10}$ près ; c) le nombre de pas de `power_stationary_20(P_d, 1e-12)`, et le nombre de pas que garantit la borne $\lVert\mathbf{x}_k - \boldsymbol{\pi}\rVert_1 \le 2\,d^k$ de la fiche pour $10^{-12}$ ; d) $\lvert\lambda_2(\mathbf{P}_d)\rvert$ et $d\,\lvert\lambda_2(\mathbf{L})\rvert$ (4 décimales) ; e) les numéros des pages, du plus grand PageRank au plus petit. Ce qu'il faut observer : trois méthodes, une seule loi ; la méthode de la puissance converge au rythme de $\lvert\lambda_2(\mathbf{P}_d)\rvert$, plus vite que ne le garantit $d$.

**M26.21 · 🔮 Prédire la somme des lignes de (1 − γ)(I − γP)⁻¹, puis leur limite quand γ tend vers 1, et vérifier.** On reprend les trois opérateurs de M26.2 et $\mathbf{M}_\gamma = (1 - \gamma)(\mathbf{I} - \gamma\mathbf{P})^{-1}$. **Avant d'exécuter**, prédis : a) la somme de chaque ligne de $\mathbf{M}_\gamma$ : (A) 1 ; (B) $\frac{1}{1 - \gamma}$ ; (C) elle dépend de la ligne ; b) quand $\gamma$ tend vers 1, chaque ligne de $\mathbf{M}_\gamma$ tend vers : (A) la loi concentrée sur l'état de départ ; (B) la loi stationnaire $\boldsymbol{\pi}$ ; (C) la loi uniforme ; (D) le vecteur nul ; c) quand $\gamma$ tend vers 0, $\mathbf{M}_\gamma$ tend vers : (A) $\mathbf{I}$ ; (B) $\mathbf{P}$ ; (C) la matrice dont chaque ligne est $\boldsymbol{\pi}$. Puis calcule $\mathbf{M}_\gamma$ colonne par colonne avec ta `bellman_linear_solve` (la colonne $j$ est $(1 - \gamma)$ fois la solution pour $\mathbf{r} = \mathbf{e}_j$), pour $\gamma = 0{,}6$, $0{,}7$, $0{,}85$ et $0{,}96$, et $\boldsymbol{\pi}$ avec ta `stationary_distribution`. Relève : d) le plus grand écart à 1 des sommes des lignes, sur les quatre valeurs de $\gamma$ ; e) pour chaque $\gamma$, le plus grand écart $\max_{s, s'}\lvert M_\gamma(s, s') - \pi_{s'}\rvert$ (4 décimales) ; f) vrai ou faux : la limite exacte de $\mathbf{M}_\gamma$ quand $\gamma \to 1$, calculée par SymPy (la matrice en fractions, un symbole `gamma`, `sp.limit` sur chaque coefficient), a toutes ses lignes égales à $\boldsymbol{\pi}$ ; g) la limite exacte quand $\gamma \to 0$, par le même calcul. Ce qu'il faut observer : les lignes sont des lois pour tout $\gamma$ ; quand l'arrêt est rare, la loi de l'état où il tombe oublie le départ et devient $\boldsymbol{\pi}$ ; quand il est immédiat, elle reste sur le départ.

**M26.22 · 🔬 Le biais du maximum par simulation.** $k$ fournisseurs ont la même durée de vie moyenne, 1 000 h, et l'on teste $n$ batteries de chacun (écart-type 30 h par batterie). Écris `max_bias_22(k, n, delta, n_rep, rng)`, qui simule `n_rep` expériences, toutes en une fois avec des tableaux : les moyennes vraies valent 1 000 h, sauf celle du fournisseur 0, qui vaut $1\,000 + \delta$ ; dans chaque expérience, on tire les $n \times k$ durées (`rng.normal`, un tableau de forme `(n_rep, n, k)`), l'estimateur naïf est la plus grande des $k$ moyennes mesurées, et l'estimateur double remesure le fournisseur choisi sur $n$ nouvelles batteries (un tableau de forme `(n_rep, n)`, tiré après le premier) ; la fonction rend les deux biais moyens, par rapport à la meilleure moyenne vraie $1\,000 + \max(\delta, 0)$. Avec `rng = np.random.default_rng(6222)`, `n_rep = 20000`, et ce même `rng` pour tous les appels, dans l'ordre : $k$ parcourt $(2, 3, 5, 10)$ et, pour chaque $k$, $n$ parcourt $(4, 16, 64)$, avec $\delta = 0$ ; puis un dernier appel avec $k = 3$, $n = 16$ et $\delta = 5$. Relève : a) le tableau des biais naïfs, une ligne par $k$, une colonne par $n$ (2 décimales) ; b) vrai ou faux : pour $k = 2$ et $n = 16$, le biais naïf est à moins de 0,2 h de $\frac{\sigma}{\sqrt\pi}$, avec $\sigma = 30/\sqrt{16}$ ; c) pour $k = 3$ et $n = 16$, le biais naïf divisé par $\sigma$, à comparer à $\frac{3}{2\sqrt\pi} \approx 0{,}846$ (l'espérance du maximum de trois variables indépendantes de loi $\mathcal{N}(0, 1)$, admise) ; d) vrai ou faux : dans tout le tableau, le biais de l'estimateur double est inférieur à 0,3 h en valeur absolue ; e) avec $k = 3$, $n = 16$ et $\delta = 5$ : les deux biais (2 décimales). Trace le biais naïf en fonction de $k$, une courbe par $n$. Ce qu'il faut conclure : le biais grandit avec $k$ et décroît comme $1/\sqrt n$ (il est divisé par 4 quand $n$ est multiplié par 16) ; l'estimateur double est sans biais quand tout se vaut, et pessimiste quand une option est meilleure.

**M26.23 · 🎨 La loi d'une chaîne au fil des pas depuis trois départs, et ‖μ_n − π‖₁ en échelle logarithmique.** Écris `draw_convergence_23(ax_law, ax_dist, P, starts, n_max)`, qui dessine sur les **axes reçus** (sans ouvrir de figure), avec ta `n_step_distribution` et ta `stationary_distribution` : dans `ax_law`, la probabilité d'être dans l'état 0 en fonction de $n$, de 0 à `n_max`, une courbe par état de départ de `starts`, et la droite horizontale $\pi_0$ ; dans `ax_dist`, en échelle logarithmique, $\lVert\boldsymbol{\mu}_n - \boldsymbol{\pi}\rVert_1$ pour chaque départ, et en pointillés la courbe $\lvert\lambda_2\rvert^n$ (avec $\lambda_2$ calculée par `np.linalg.eigvals`) ; des titres, des noms d'axes et une légende. La vérification l'appelle sur les trois opérateurs de M26.2, avec `starts = [0, 1, 2]` et `n_max = 100`, et affiche la figure. Relève : a) $\lvert\lambda_2\rvert$ (4 décimales) ; b) la pente de $n \mapsto \ln\lVert\boldsymbol{\mu}_n - \boldsymbol{\pi}\rVert_1$ entre $n = 50$ et $n = 100$, depuis l'état 0 (4 décimales), à comparer à $\ln\lvert\lambda_2\rvert$ ; c) le premier $n$ où les trois écarts sont tous inférieurs à $10^{-6}$. Ce qu'il faut observer : après quelques pas, les trois courbes deviennent des droites parallèles de pente $\ln\lvert\lambda_2\rvert$ ; le départ ne change que leur hauteur.

**M26.24 · 🐛 Chasse à l'erreur.** Un collègue a écrit quatre fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `bikes_after(P, mu0, n)` doit rendre la loi d'un vélo après `n` jours ; elle répète `n` fois `mu = P @ mu`. Il l'a vérifiée sur la matrice $\mathbf{S} = \begin{pmatrix} 0{,}7 & 0{,}2 & 0{,}1 \\ 0{,}2 & 0{,}6 & 0{,}2 \\ 0{,}1 & 0{,}2 & 0{,}7 \end{pmatrix}$, depuis la station 0, sur 5 jours : le résultat a pour somme 1 et égale la ligne 0 de `np.linalg.matrix_power(S, 5)`. Il l'applique aux vélos de M26.1.
- (2) `market_shares(P)` doit rendre la loi stationnaire ; elle calcule `w, v = np.linalg.eig(P.T)`, prend la colonne de `v` dont la valeur propre est la plus proche de 1, et rend sa partie réelle. Il l'a vérifiée sur les trois opérateurs de M26.2 : `np.allclose(pi @ P, pi)` vaut `True`.
- (3) `subscription_value(P, monthly_fee, closing_fee, gamma)` doit rendre les valeurs d'un abonnement à trois états, essai (0), payant (1) et résilié (2, absorbant), où un abonné payant verse `monthly_fee` chaque mois et où une résiliation coûte une fois `closing_fee` à l'abonné ; elle construit $\mathbf{r} = (0,\ \text{monthly\_fee},\ \text{closing\_fee})$ et rend `np.linalg.solve(np.eye(3) - gamma * P, r)`. Il l'a vérifiée avec $\mathbf{P} = \begin{pmatrix} 0 & 0{,}55 & 0{,}45 \\ 0 & 0{,}9 & 0{,}1 \\ 0 & 0 & 1 \end{pmatrix}$, 12 € par mois, 15 € de frais et $\gamma = 0{,}96$ : le résidu $\lVert\mathbf{V} - (\mathbf{r} + \gamma\mathbf{P}\mathbf{V})\rVert_\infty$ est inférieur à $10^{-9}$.
- (4) `total_takings(P, r)` doit rendre la recette totale moyenne jusqu'à la fin, depuis chaque état ; elle rend `np.linalg.solve(np.eye(m) - P, r)`. Il l'a vérifiée sur le cursus de M26.4 (`P` = les trois années, `r` = des 1) : elle redonne les durées moyennes. Il l'applique ensuite aux vélos, avec une matrice estimée sur 100 trajets par station, de lignes $(61, 29, 10)/100$, $(33, 41, 26)/100$ et $(38, 23, 39)/100$, et les recettes journalières $(1{,}5 ;\ 1 ;\ 0{,}5)$ €.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `bikes_after_fixed`, `market_shares_fixed`, `subscription_value_fixed` et `total_takings_fixed`, avec les mêmes arguments ; `total_takings_fixed` lève une `ValueError` quand le processus ne finit pas avec certitude, testé par `np.linalg.matrix_rank`), puis réponds : a) la loi des vélos de M26.1 après trois jours par `bikes_after_fixed`, et la somme des coordonnées de ce que rend `bikes_after` (4 décimales) ; b) la loi rendue par `market_shares_fixed` pour les trois opérateurs, et la valeur absolue de la somme de ce que rend `market_shares` (4 décimales) ; c) les valeurs que rend `subscription_value_fixed` pour le modèle du collègue (2 décimales), et celle que `subscription_value` donne à l'état résilié ; d) vrai ou faux : `total_takings_fixed` lève une `ValueError` sur la matrice des vélos ; et ce que rend `total_takings` sur cette matrice (une erreur, ou des nombres : lesquels ?). Pour chacune des quatre erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas.

**M26.25 · 🛠️ Un test de propriété.** Le notebook fournit `random_chain_25(rng)`, qui tire une chaîne de 2 à 8 états, plus ou moins creuse, stochastique ou sous-stochastique (une fois sur deux), des récompenses et un $\gamma$ parmi 0,6, 0,7, 0,85 et 0,96, et rend `(P, r, gamma, stochastic)` ; et trois versions fausses : `stationary_times_two` (rend $2\boldsymbol{\pi}$), `iterates_in_place` (des balayages en place au lieu des itérés synchrones) et `iterates_without_gamma` (le pas $\mathbf{r} + \mathbf{P}\mathbf{V}$). Écris `markov_property_test_25(n_trials, rng, stationary=None, iterates=None, tol=1e-9)` ; quand `stationary` ou `iterates` vaut `None`, le test prend `mymath.markov.stationary_distribution` ou `mymath.markov.bellman_fixed_point_iterates` **au moment de l'appel**. Pour chacun des `n_trials` essais, dans cet ordre : `P, r, gamma, stochastic = random_chain_25(rng)`, puis `V0 = rng.normal(0, 10, size=m)` ; si la chaîne est stochastique, $\boldsymbol{\pi}$ = `stationary(P)` (un essai où elle lève une `ValueError`, une chaîne à plusieurs classes fermées, se saute pour cette partie) ; $\mathbf{V}$ = `mymath.markov.bellman_linear_solve(P, r, gamma)` ; les itérés = `iterates(P, r, gamma, V0, 600)` ; avec `scale = 1 + max|V|`. La fonction rend un dictionnaire de six compteurs d'essais et d'un rapport : `"law"`, si $\boldsymbol{\pi}$ a une coordonnée inférieure à $-$`tol` ou une somme qui s'écarte de 1 de plus de `tol` ; `"invariance"`, si $\lVert\boldsymbol{\pi}\mathbf{P} - \boldsymbol{\pi}\rVert_\infty >$ `tol` ; `"recurrence"`, si une ligne $k + 1$ des itérés s'écarte de $\mathbf{r} + \gamma\mathbf{P}\mathbf{V}_k$ de plus de `tol * scale` ; `"a_priori"`, s'il existe $k$ avec $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty > \gamma^k\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty + $ `tol * scale` ; `"a_posteriori"`, s'il existe $k \ge 1$ avec $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty > \frac{\gamma}{1 - \gamma}\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty + $ `tol * scale` ; `"fixed_point"`, si la dernière ligne s'écarte de $\mathbf{r} + \gamma\mathbf{P}\mathbf{V}_{600}$ de plus de `tol * scale` ; et `"worst_ratio"`, le plus grand rapport $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty / (\gamma^k\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty)$, sur les essais et les $k$ où le dénominateur dépasse $10^{-6}$ `* scale`. a) Justifie `tol = 1e-9` : de quel ordre sont les erreurs d'arrondi sur ces calculs ? b) Avec `rng = np.random.default_rng(6225)` et 300 essais, avec tes fonctions : vrai ou faux, les six compteurs sont nuls ; et le pire rapport (4 décimales) : pourquoi est-il si proche de 1 ? c) Avec le même départ (`default_rng(6225)`, 300 essais) et `stationary=stationary_times_two` : le compteur `"law"`, et vrai ou faux, `"invariance"` reste nul ; d) avec `iterates=iterates_in_place` : le compteur `"recurrence"`, et vrai ou faux, `"a_priori"` et `"a_posteriori"` restent nuls ; e) avec `iterates=iterates_without_gamma` : vrai ou faux, `"a_priori"` compte les 300 essais. La vérification compare aussi tes compteurs à ceux de la référence sur deux départs cachés, et remplace un instant `mymath.markov.stationary_distribution` par une version qui ne normalise pas : ton compteur `"law"` doit alors compter. Ce qu'il faut retenir : une propriété nécessaire ne suffit pas ($2\boldsymbol{\pi}$ vérifie encore $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$ ; un balayage en place vérifie encore les deux bornes) ; un bon test combine des propriétés qui, ensemble, caractérisent le résultat.

**M26.26 · 🏆 Défi : estimer la valeur d'un état à 0,01 près en simulant l'arrêt géométrique.** Le petit web de M26.20 ($\mathbf{P}_d$, $d = 0{,}85$) rapporte une recette publicitaire par page vue : 0,40 €, 1,20 €, 0,20 €, 0,80 €, 0 € et 1,60 € pour les pages 1 à 6. Après chaque page, le visiteur continue avec la probabilité $\gamma = 0{,}7$ et quitte le site avec 0,3. D'après la fiche (§4), la recette totale moyenne d'une visite qui commence en page 1, sans actualisation, est la valeur $V$ de la page 1 pour $\gamma = 0{,}7$. Écris `estimate_value_26(P, r, gamma, s0, budget, rng)`, qui simule des visites depuis l'état `s0` : à chaque page vue, la visite encaisse `r` de cette page, puis continue avec la probabilité `gamma` (sinon elle s'arrête) et passe à la page suivante selon la ligne de `P` ; elle somme les recettes **sans actualisation**. Chaque page vue est un pas simulé ; le nombre total de pas, toutes visites comprises, ne doit jamais dépasser `budget`, et toute visite simulée est menée à son terme et comptée (choisis donc le nombre de visites avec une marge). La fonction rend `(estimate, n_visits, n_steps)` : la moyenne des recettes totales, le nombre de visites et le nombre de pas simulés. **Critère de réussite :** avec `budget = 600_000`, pour chacune des dix graines 6230 à 6239 (`rng = np.random.default_rng(seed)`), `n_steps <= budget`, et l'estimation tombe à moins de 0,01 de la valeur exacte (par ta `bellman_linear_solve`) au moins 8 fois sur 10. La vérification contrôle aussi, sur une chaîne cachée où chaque page rapporte 1 avec $\gamma = 0{,}96$, que `estimate * n_visits` égale `n_steps` (chaque pas compté, aucune actualisation ajoutée) et que l'estimation est à moins de 4 erreurs types de $\frac{1}{1 - 0{,}96} = 25$ (l'arrêt géométrique, sans troncature) ; et, sur une autre chaîne cachée avec $\gamma = 0{,}6$, que l'estimation est à moins de 4 erreurs types de la valeur exacte. Relève : a) la valeur exacte $V$ de la page 1 (4 décimales) ; b) l'écart-type de la recette totale d'une visite, estimé sur une simulation pilote de 20 000 visites (2 décimales), et le nombre de visites qu'il faudrait pour une erreur type de 0,004 ; c) tes dix estimations et ton nombre de succès (affichés par la vérification). Puis estime de même l'écart-type du retour actualisé $\sum_{t < 60}\gamma^tR_t$ d'une visite qui ne s'arrête pas : lequel des deux écarts-types est le plus grand, et que coûte la troncature à 60 pas ? Ce qu'il faut retenir : l'arrêt géométrique donne une estimation sans biais de la valeur actualisée, au prix d'une variance plus grande.
