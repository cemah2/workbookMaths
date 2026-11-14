# M26 · Chaînes de Markov et équation de Bellman — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture, qui accepte toute démonstration correcte. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🗣️ 🔗 Explication et pont](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M26.Q1 — Matrice stochastique, convention ligne, loi à n pas et chemins du graphe : vrai ou faux
1. Faux : dans la fiche, ce sont les **lignes** qui ont pour somme 1 (ligne = état de départ) ; une matrice aux colonnes de somme 1 est la transposée d'une matrice de transition.
2. Vrai : $\boldsymbol{\mu}\mathbf{P}$ a des coordonnées positives ou nulles, et $(\boldsymbol{\mu}\mathbf{P})\mathbf{1} = \boldsymbol{\mu}(\mathbf{P}\mathbf{1}) = \boldsymbol{\mu}\mathbf{1} = 1$.
3. $0{,}1 \times 0{,}1 + 0{,}9 \times 0{,}7 = 0{,}64$ : les chemins $0 \to 0 \to 0$ et $0 \to 1 \to 0$.
4. Faux : $(\mathbf{P}^n)_{ij}$ somme les produits sur **tous** les chemins de longueur $n$ de $i$ à $j$ (en 3, $0{,}1^2 = 0{,}01 \ne 0{,}64$).
5. Faux : le passé compte, mais tout ce qu'il apporte sur l'avenir est déjà dans l'état présent.
6. $(\mathbf{P}\mathbf{f})_i = \sum_jp_{ij}\,f(j)$.

### M26.Q2 — Une loi stationnaire existe-t-elle, est-elle unique, la loi de la chaîne y converge-t-elle ? Chaînes périodiques et à deux classes
1. Vrai : $\rho(\mathbf{P}) = 1$, et Perron-Frobenius donne un vecteur propre positif de $\mathbf{P}^\top$ (fiche §2).
2. Une infinité : la loi stationnaire de chaque classe (complétée par des 0) et tous leurs mélanges $\theta\,\boldsymbol{\pi}_A + (1 - \theta)\,\boldsymbol{\pi}_B$, $\theta \in [0, 1]$.
3. Faux : $\boldsymbol{\mu}_n$ tourne, $(1, 0, 0, 0)$, $(0, 1, 0, 0)$… ; la chaîne est de période 4.
4. Vrai (fiche §2, théorème admis).
5. Celle de $\lvert\lambda_2\rvert = 0{,}3$ : l'écart à $\boldsymbol{\pi}$ décroît comme $\lvert\lambda_2\rvert^n$.
6. Faux : à droite, pour la valeur propre 1, $\mathbf{P}$ a le vecteur $\mathbf{1}$ ; $\boldsymbol{\pi}^\top$ est un vecteur propre de $\mathbf{P}^\top$.

### M26.Q3 — Espérance conditionnelle, propriété de la tour et analyse au premier pas : quelle équation pour quel nombre ?
1. Faux : c'est une variable aléatoire, $m(Y)$, où $m(y) = \mathbb{E}[X \mid Y = y]$.
2. $\mathbb{E}[X \mid Y]$ (la tour).
3. (a) avec (3), (b) avec (1), (c) avec (2).
4. Faux : $\mathbf{Q}$ ne garde que les états transitoires (un état absorbant y rendrait $\mathbf{I} - \mathbf{Q}$ singulière).
5. $t = 1 + 0{,}8\,t$, donc $t = 5$.
6. Vrai (fiche §3, ∂ M26.10).

### M26.Q4 — Le facteur γ : une actualisation, ou une probabilité de continuer ? Valeur d'un état et politique
1. $\frac{1}{1 - \gamma} = \frac{1}{0{,}4} = 2{,}5$ pas.
2. Faux : l'arrêt aléatoire fait déjà le travail de l'actualisation ; actualiser en plus la compterait deux fois.
3. Faux : les deux ont la même **espérance**, $V(s)$, mais pas la même loi.
4. Faux : une valeur se rapporte toujours à une politique (ou à une chaîne fixée).
5. $0{,}3 \times 4 + 0{,}7 \times 10 = 8{,}2$.
6. Vrai : elle tire l'action au hasard (fiche §4).

### M26.Q5 — Le système de Bellman d'une politique fixée : quelles matrices, pourquoi il est inversible, quand γ = 1 est permis
1. Faux : $\mathbf{V} - \gamma\mathbf{P}\mathbf{V} = \mathbf{r}$, c'est-à-dire $(\mathbf{I} - \gamma\mathbf{P})\mathbf{V} = \mathbf{r}$.
2. $\lVert\gamma\mathbf{P}\rVert_\infty = \gamma < 1$, donc $\rho(\gamma\mathbf{P}) < 1$ : 1 n'est pas valeur propre de $\gamma\mathbf{P}$, et $\mathbf{I} - \gamma\mathbf{P}$ n'a pas de noyau (ou : la série de Neumann converge et donne l'inverse).
3. Vrai : $(\mathbf{I} - \mathbf{P})\mathbf{1} = \mathbf{0}$.
4. Vrai : les lignes qui finissent rendent $\mathbf{I} - \mathbf{P}$ inversible (fiche §3 et §5).
5. $V = 1{,}2 + 0{,}6\,V$, donc $V = 3$.
6. Vrai (fiche §5).

### M26.Q6 — Contraction, bornes a priori et a posteriori, itérations synchrones ou en place : vrai ou faux
1. Vrai (fiche §6).
2. $0{,}7^5 \times 10 \approx 1{,}68$.
3. $\frac{0{,}7}{0{,}3} \times 0{,}03 = 0{,}07$.
4. Faux : l'erreur peut atteindre $\frac{\gamma}{1 - \gamma}$ fois le dernier changement (2,33 fois pour $\gamma = 0{,}7$).
5. Faux : en place, chaque nouvelle valeur sert aussitôt ; les itérés diffèrent, même s'ils ont la même limite.
6. Vrai : $\mathbf{V} + \big(\mathbf{r} - (\mathbf{I} - \gamma\mathbf{P})\mathbf{V}\big) = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$.

### M26.Q7 — Un maximum dans l'opérateur : ce qui reste (contraction, point fixe unique), ce qui se perd (le système linéaire)
1. $\lvert 8 - 6\rvert = 2$ et $\lVert\mathbf{x} - \mathbf{y}\rVert_\infty = \max(2, 2, 3) = 3$ : le lemme est vérifié.
2. Faux : avec $\mathbf{x} = (4, 0)$ et $\mathbf{y} = (1, 2)$, $\max\mathbf{x} - \max\mathbf{y} = 2$ mais $\max(\mathbf{x} - \mathbf{y}) = 3$. (Sur l'exemple de 1, les deux valent 2 par hasard.)
3. Vrai : c'est le théorème de Banach (fiche §6).
4. Faux : selon $\mathbf{V}$, le maximum choisit l'une ou l'autre branche ; on itère, ou l'on raisonne comme sur les offres.
5. Refuser l'offre et attendre : $600 < 640$.
6. Vrai : l'offre suivante est indépendante de l'offre du moment, donc ce que vaut l'attente aussi.

### M26.Q8 — Des échantillons au lieu de P : moyenne de retours, pas 1/n ou constant, erreur TD, biais du maximum
1. Vrai (la moyenne incrémentale, ∂ 11.2 de workbookIA).
2. Faux : elle suit la moyenne, mais garde un bruit de variance $\frac{\alpha\sigma^2}{2 - \alpha}$.
3. Seulement $\frac1n$. Le pas $0{,}1$ viole $\sum\alpha_n^2 < \infty$, $\frac{1}{n^2}$ viole $\sum\alpha_n = \infty$, et $\frac{1}{\sqrt n}$ viole la seconde : $\sum\frac1n = \infty$.
4. Faux : c'est son **espérance conditionnelle** qui est nulle ; une transition isolée donne une erreur TD non nulle (fiche §8, la boutique).
5. Vrai : $\mathbb{E}[\max_i\hat X_i] \ge \max_i\mathbb{E}[\hat X_i]$, avec une inégalité stricte ici.
6. $0{,}7^{20} \times 50 \approx 0{,}04$.

<a id="rappels"></a>

## 🔁 Rappels

### M26.R1 — Puissances d'une matrice diagonalisable et méthode de la puissance (M12c)
1. $\det(\mathbf{A} - \lambda\mathbf{I}) = \lambda^2 - 7\lambda + 6 = (\lambda - 6)(\lambda - 1)$ : la valeur propre 6, de vecteur propre $(2, 1)$, et la valeur propre 1, de vecteur propre $(1, -2)$.
2. $\mathbf{A}$ est symétrique : $\mathbf{A}^3 = 6^3\,\frac{\mathbf{u}_1\mathbf{u}_1^\top}{5} + 1^3\,\frac{\mathbf{u}_2\mathbf{u}_2^\top}{5}$, donc $(\mathbf{A}^3)_{01} = \frac{216 \times 2 + 1 \times (-2)}{5} = 86$. Directement : $\mathbf{A}^2 = \begin{pmatrix} 29 & 14 \\ 14 & 8 \end{pmatrix}$ et $\mathbf{A}^3 = \begin{pmatrix} 173 & 86 \\ 86 & 44 \end{pmatrix}$.
3. Vers la direction de $(2, 1)$ ; $(1, 0) = \frac25(2, 1) + \frac15(1, -2)$, et la composante sur $(1, -2)$ est multipliée par $\frac16$ relativement à l'autre à chaque pas.
4. Vrai, quand elle est seule de ce module et que le départ a une composante sur son vecteur propre.

### M26.R2 — La norme ‖·‖∞ d'une matrice, ρ(A) ≤ ‖A‖ et Aᵗ → 0 quand ρ(A) < 1 (M22), et la somme d'une série géométrique (R5)
1. $\max(0{,}2 + 0{,}4 ;\ 0{,}5 + 0{,}1) = 0{,}6$.
2. $\lambda^2 - 0{,}3\,\lambda + 0{,}22 = 0$ : $\lambda = 0{,}15 \pm i\sqrt{0{,}1975}$, de module $\sqrt{0{,}22} \approx 0{,}469 \le 0{,}6$.
3. Vrai : $\rho(\mathbf{A}) < 1$ (et même $\lVert\mathbf{A}^t\rVert_\infty \le 0{,}6^t$).
4. Faux : $\mathbf{B} = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$ a $\rho = 0$ et $\lVert\mathbf{B}\rVert_\infty = 2$.
5. 1.
6. $\frac{1}{1 - 0{,}4} = \frac53$, et $\frac53 - 1 - 0{,}4 = \frac{0{,}16}{0{,}6} = \frac{4}{15}$.

### M26.R3 — Probabilités totales et espérance d'une loi géométrique (M03, M02b)
1. $0{,}6 \times 0{,}2 + 0{,}4 \times 0{,}35 = 0{,}26$.
2. $\frac{1}{0{,}2} = 5$.
3. $0{,}8^3 = 0{,}512$ (les trois premiers essais échouent).
4. Vrai : la loi géométrique est sans mémoire.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M26.1 — Des vélos en libre-service entre trois stations : matrice de transition, graphe, loi après deux et trois jours, et coût moyen du lendemain (Pf)

**Réponses.** a) `0.27` · b) `[0.456, 0.308, 0.236]` · c) `[0.4604, 0.3072, 0.2324]` · d) `46.48` · e) `[0.68, 1.04, 1.12]` · f) `182.4`.

**Démarche.** $\mathbf{P} = \begin{pmatrix} 0{,}6 & 0{,}3 & 0{,}1 \\ 0{,}3 & 0{,}4 & 0{,}3 \\ 0{,}4 & 0{,}2 & 0{,}4 \end{pmatrix}$ et $\boldsymbol{\mu}_0 = (0{,}4 ;\ 0{,}4 ;\ 0{,}2)$. a) Les chemins $B \to A \to C$ ($0{,}3 \times 0{,}1 = 0{,}03$), $B \to B \to C$ ($0{,}4 \times 0{,}3 = 0{,}12$) et $B \to C \to C$ ($0{,}3 \times 0{,}4 = 0{,}12$) : 0,27. b) $\boldsymbol{\mu}_1 = \boldsymbol{\mu}_0\mathbf{P} = (0{,}24 + 0{,}12 + 0{,}08 ;\ 0{,}12 + 0{,}16 + 0{,}04 ;\ 0{,}04 + 0{,}12 + 0{,}08) = (0{,}44 ;\ 0{,}32 ;\ 0{,}24)$, puis $\boldsymbol{\mu}_2 = (0{,}264 + 0{,}096 + 0{,}096 ;\ 0{,}132 + 0{,}128 + 0{,}048 ;\ 0{,}044 + 0{,}096 + 0{,}096) = (0{,}456 ;\ 0{,}308 ;\ 0{,}236)$. c) $\boldsymbol{\mu}_3 = (0{,}2736 + 0{,}0924 + 0{,}0944 ;\ 0{,}1368 + 0{,}1232 + 0{,}0472 ;\ 0{,}0456 + 0{,}0924 + 0{,}0944) = (0{,}4604 ;\ 0{,}3072 ;\ 0{,}2324)$. d) $200 \times 0{,}2324 = 46{,}48$. e) $(\mathbf{P}\mathbf{f})_A = 0{,}6 \times 0{,}4 + 0{,}3 \times 0{,}8 + 0{,}1 \times 2 = 0{,}68$ ; de même $0{,}12 + 0{,}32 + 0{,}6 = 1{,}04$ et $0{,}16 + 0{,}16 + 0{,}8 = 1{,}12$. f) Chaque vélo coûte en moyenne $(\mathbf{P}\mathbf{f})_i$ s'il est en $i$ ce matin : $200\,\boldsymbol{\mu}_0\mathbf{P}\mathbf{f} = 200\,(0{,}4 \times 0{,}68 + 0{,}4 \times 1{,}04 + 0{,}2 \times 1{,}12) = 200 \times 0{,}912 = 182{,}4$ €.

Dans ta copie : le graphe a trois nœuds, une boucle sur chacun (0,6, 0,4 et 0,4) et six flèches entre eux, les poids sortant de chaque nœud ayant pour somme 1. Chaque $\boldsymbol{\mu}_n$ a pour somme 1. f) $= 200\,(\boldsymbol{\mu}_0\mathbf{P})\mathbf{f} = 200\,\boldsymbol{\mu}_1\mathbf{f} = 200\,(0{,}176 + 0{,}256 + 0{,}48)$ : on peut moyenner le coût sur le pas suivant puis sur ce matin, ou faire avancer la loi puis la moyenner (fiche §1, « dans l'ordre qu'on veut »).

**Erreurs fréquentes.** Faire avancer la loi par $\mathbf{P}\boldsymbol{\mu}$ (la somme ne vaut plus 1 : $(0{,}3558 ;\ 0{,}3514 ;\ 0{,}3532)$ après trois jours). Calculer $(p_{BC})^2 = 0{,}09$. Lire $(\mathbf{P}^2)_{CB} = 0{,}28$. Calculer $\mathbf{P}^\top\mathbf{f} = (1{,}28 ;\ 0{,}84 ;\ 1{,}08)$. Prendre le coût des stations de ce matin, $200\,\boldsymbol{\mu}_0\mathbf{f} = 176$ €.

**Variante.** Si les 200 vélos sont à C ce matin, leur loi dans deux jours est la ligne C de $\mathbf{P}^2$, $(0{,}46 ;\ 0{,}28 ;\ 0{,}26)$.

### Ex M26.2 — Trois opérateurs et leurs parts de marché : la loi stationnaire par un système linéaire, puis vérifier πP = π

**Réponses.** a) `[0.5, 0.3333, 0.1667]` · b) `"1/6"` · c) `[0.455, 0.385, 0.16]` · d) `"1/15"` · e) `False`.

**Démarche.** $\mathbf{P}^\top - \mathbf{I} = \begin{pmatrix} -0{,}1 & 0{,}05 & 0{,}2 \\ 0{,}05 & -0{,}15 & 0{,}15 \\ 0{,}05 & 0{,}1 & -0{,}35 \end{pmatrix}$ ; on remplace la dernière ligne par $(1, 1, 1)$, second membre $(0, 0, 1)$. Multipliées par 20, les deux premières équations deviennent $-2\pi_0 + \pi_1 + 4\pi_2 = 0$ et $\pi_0 - 3\pi_1 + 3\pi_2 = 0$. Pivot (en prenant la seconde comme pivot sur $\pi_0$) : $L_1 + 2L_2$ donne $-5\pi_1 + 10\pi_2 = 0$, soit $\pi_1 = 2\pi_2$ ; $L_3 - L_2$ donne $4\pi_1 - 2\pi_2 = 1$, soit $6\pi_2 = 1$. D'où $\pi_2 = \frac16$, $\pi_1 = \frac13$, $\pi_0 = 3\pi_1 - 3\pi_2 = \frac12$. c) $\boldsymbol{\mu}_0\mathbf{P} = (0{,}405 + 0{,}02 + 0{,}03 ;\ 0{,}0225 + 0{,}34 + 0{,}0225 ;\ 0{,}0225 + 0{,}04 + 0{,}0975) = (0{,}455 ;\ 0{,}385 ;\ 0{,}16)$. d) En régime stationnaire, $P(S_t = C,\ S_{t+1} = A) = \pi_C\,p_{CA}$ et $P(S_{t+1} = A) = \pi_A$ ; par Bayes, $\frac{\frac16 \times 0{,}2}{\frac12} = \frac{1}{15}$. e) $\pi_A p_{AB} = 0{,}5 \times 0{,}05 = 0{,}025$ et $\pi_B p_{BA} = \frac13 \times 0{,}05 \approx 0{,}0167$ : faux.

Dans ta copie : $\boldsymbol{\pi}\mathbf{P} = \big(0{,}45 + \frac{0{,}05}{3} + \frac{0{,}2}{6} ;\ 0{,}025 + \frac{0{,}85}{3} + \frac{0{,}15}{6} ;\ 0{,}025 + \frac{0{,}1}{3} + \frac{0{,}65}{6}\big) = \big(\frac12 ;\ \frac13 ;\ \frac16\big)$ ; la troisième coordonnée vérifie l'équation retirée. $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$ équilibre, pour chaque opérateur, tout ce qui entre et tout ce qui sort, pas chaque paire : Azur perd vers Boréal plus qu'il n'en reçoit, et le rattrape sur Cobalt.

**Erreurs fréquentes.** Chercher un vecteur propre de $\mathbf{P}$ à droite (on trouve $\mathbf{1}$, puis la loi uniforme). Oublier de remplacer une équation (le système $3 \times 3$ est singulier) ou de normaliser. Calculer $\mathbf{P}\boldsymbol{\mu}_0^\top$ (une « loi » dont la somme vaut 1,0575). En d), donner $p_{CA} = \frac15$ ou le flux $\frac{1}{30}$ sans diviser par $\pi_A$.

**Variante.** Si Cobalt ne garde que 55 % de ses clients et en perd 30 % vers Azur (ligne $(0{,}3 ;\ 0{,}15 ;\ 0{,}55)$), $\boldsymbol{\pi} = \big(\frac{21}{38}, \frac{6}{19}, \frac{5}{38}\big) \approx (0{,}553 ;\ 0{,}316 ;\ 0{,}132)$.

### Ex M26.3 — Trois chaînes qui posent problème, périodique, à deux classes et avec un état transitoire : lois stationnaires et comportement de Pⁿ

**Réponses.** a) `[0.3228, 0.1772, 0.288, 0.212]` · b) `[0.6456, 0.3544, 0, 0]` · c) `False` · d) `[0.3818, 0.2182, 0.16, 0.24]` · e) `True` · f) `[0, 0.8, 0.2]`.

**Démarche.** Le bac. Deux traversées de suite ramènent au nord, par la matrice $\mathbf{M} = \begin{pmatrix} 0{,}7 \times 0{,}9 + 0{,}3 \times 0{,}3 & 0{,}7 \times 0{,}1 + 0{,}3 \times 0{,}7 \\ 0{,}35 \times 0{,}9 + 0{,}65 \times 0{,}3 & 0{,}35 \times 0{,}1 + 0{,}65 \times 0{,}7 \end{pmatrix} = \begin{pmatrix} 0{,}72 & 0{,}28 \\ 0{,}51 & 0{,}49 \end{pmatrix}$, irréductible et apériodique, de loi stationnaire $\big(\frac{51}{79}, \frac{28}{79}\big)$ ($0{,}28\,x_A = 0{,}51\,x_B$). b) Aux pas pairs, le bac suit $\mathbf{M}$ depuis A : $\boldsymbol{\mu}_{2k} \to \big(\frac{51}{79}, \frac{28}{79}, 0, 0\big) \approx (0{,}6456 ;\ 0{,}3544 ;\ 0 ;\ 0)$. a) Toute la masse du sud vient du nord en un pas et y retourne : $\pi(\text{nord}) = \pi(\text{sud}) = \frac12$. Au nord, $\boldsymbol{\pi}$ est proportionnelle à la loi stationnaire de $\mathbf{M}$ ; au sud, c'est son image après une traversée, $\big(\frac{51}{79} \times 0{,}7 + \frac{28}{79} \times 0{,}35 ;\ \frac{51}{79} \times 0{,}3 + \frac{28}{79} \times 0{,}65\big) = \big(\frac{91}{158}, \frac{67}{158}\big)$. D'où $\boldsymbol{\pi} = \big(\frac{51}{158}, \frac{28}{158}, \frac{91}{316}, \frac{67}{316}\big) \approx (0{,}3228 ;\ 0{,}1772 ;\ 0{,}2880 ;\ 0{,}2120)$ ; contrôle : $0{,}9 \times 0{,}2880 + 0{,}3 \times 0{,}2120 = 0{,}3228$. c) Faux : aux pas impairs, $\boldsymbol{\mu}_n \to \big(0, 0, \frac{91}{158}, \frac{67}{158}\big)$. Le site. Dans chaque version, $0{,}2\,\pi_0 = 0{,}35\,\pi_1$ donne $\big(\frac{7}{11}, \frac{4}{11}\big)$ et $0{,}45\,\pi_2 = 0{,}3\,\pi_3$ donne $(0{,}4 ;\ 0{,}6)$. d) Chaque version garde la masse qui y arrive : $0{,}6\,\big(\frac{7}{11}, \frac{4}{11}, 0, 0\big) + 0{,}4\,(0, 0, 0{,}4, 0{,}6) = \big(\frac{21}{55}, \frac{12}{55}, 0{,}16, 0{,}24\big)$. e) Vrai : $\boldsymbol{\pi} \mapsto \boldsymbol{\pi}\mathbf{P}$ est linéaire, et le mélange garde des coordonnées positives de somme 1. L'essai. f) La première colonne de $\mathbf{P}$ est $(0{,}4 ;\ 0 ;\ 0)^\top$, donc $\pi_0 = 0{,}4\,\pi_0$ et $\pi_0 = 0$ ; sur $\{1, 2\}$, $0{,}1\,\pi_1 = 0{,}4\,\pi_2$ donne $(0{,}8 ;\ 0{,}2)$.

Dans ta copie : le bac est irréductible mais de période 2 (valeur propre $-1$) ; le site est apériodique mais pas irréductible (deux classes fermées) ; l'essai n'est pas irréductible (on ne revient jamais en 0), mais il n'a qu'une classe fermée, apériodique : sa loi stationnaire est unique, et $\boldsymbol{\mu}_n$ y converge.

**Erreurs fréquentes.** Donner la loi uniforme pour le bac. Prendre $\boldsymbol{\pi}$ pour la limite de $\boldsymbol{\mu}_{2k}$, ou mettre la masse au sud. Pondérer les deux versions du site par $\frac12$, ou échanger 0,6 et 0,4. Échanger 0,8 et 0,2 dans l'essai, ou laisser une masse en 0.

**Variante.** Parti de C, le bac a pour limite de $\boldsymbol{\mu}_{2k}$ la loi $\big(0, 0, \frac{91}{158}, \frac{67}{158}\big) \approx (0 ;\ 0 ;\ 0{,}5759 ;\ 0{,}4241)$.

### Ex M26.4 — Un cursus en trois années, avec redoublement et abandon : la probabilité d'être diplômé et la durée moyenne des études, par l'analyse au premier pas

**Réponses.** a) `[0.674, 0.818, 0.882]` · b) `"126/187"` · c) `[3.15, 2.4, 1.18]` · d) `1.24` · e) `598.89`.

**Démarche.** $\mathbf{Q} = \begin{pmatrix} 0{,}15 & 0{,}7 & 0 \\ 0{,}05 & 0{,}15 & 0{,}75 \\ 0 & 0 & 0{,}15 \end{pmatrix}$ et $\mathbf{b} = (0 ;\ 0 ;\ 0{,}75)$. a) $h_3 = 0{,}75 + 0{,}15\,h_3$, donc $h_3 = \frac{15}{17} \approx 0{,}8824$ ; $h_1 = 0{,}15\,h_1 + 0{,}7\,h_2$, donc $h_1 = \frac{14}{17}h_2$ ; puis $0{,}85\,h_2 = 0{,}05 \times \frac{14}{17}h_2 + 0{,}75 \times \frac{15}{17}$, soit $13{,}75\,h_2 = 11{,}25$ (en multipliant par 17) : $h_2 = \frac{9}{11} \approx 0{,}8182$ et $h_1 = \frac{126}{187} \approx 0{,}6738$. c) $t_3 = \frac{1}{0{,}85} = \frac{20}{17}$ ; $t_1 = \frac{1 + 0{,}7\,t_2}{0{,}85}$ ; $0{,}85\,t_2 = 1 + 0{,}05\,t_1 + 0{,}75\,t_3$, soit, multiplié par 17, $14{,}45\,t_2 = 17 + (1 + 0{,}7\,t_2) + 15$ : $t_2 = \frac{33}{13{,}75} = 2{,}4$, puis $t_1 = \frac{2{,}68}{0{,}85} = \frac{268}{85} \approx 3{,}1529$. d) $\mathbf{n}(\mathbf{I} - \mathbf{Q}) = (1, 0, 0)$ : $0{,}85\,n_1 - 0{,}05\,n_2 = 1$, $-0{,}7\,n_1 + 0{,}85\,n_2 = 0$, $-0{,}75\,n_2 + 0{,}85\,n_3 = 0$ ; donc $n_2 = \frac{14}{17}n_1$, $13{,}75\,n_1 = 17$, $n_1 = \frac{68}{55} \approx 1{,}2364$, $n_2 = \frac{56}{55}$, $n_3 = \frac{168}{187}$. e) $170\,(n_1 + n_2) + 240\,n_3 = \frac{21\,080}{55} + \frac{40\,320}{187} = \frac{111\,992}{187} \approx 598{,}89$ €.

Dans ta copie : $n_1 + n_2 + n_3 = \frac{124}{55} + \frac{168}{187} = \frac{268}{85} = t_1$. e) est un système de Bellman avec $\gamma = 1$ et les frais comme récompenses : la fin est sûre, donc $\mathbf{I} - \mathbf{Q}$ est inversible (fiche §5, le site).

**Erreurs fréquentes.** Oublier la réorientation (on trouve $\mathbf{h} \approx (0{,}641 ;\ 0{,}779 ;\ 0{,}882)$). Prendre la colonne de l'abandon pour $\mathbf{b}$. Oublier le 1 de $\mathbf{t} = \mathbf{1} + \mathbf{Q}\mathbf{t}$, ou compter une année de plus pour la sortie. Prendre $N_{11} = \frac{1}{0{,}85} \approx 1{,}18$ en oubliant les retours depuis L2. Calculer les frais comme $170\,t_1 \approx 535{,}99$ € ou comme 580 € (une année par niveau).

**Variante.** Sans réorientation (un étudiant de L2 redouble alors avec 0,2) : $\mathbf{h} = \big(\frac{1575}{2312}, \frac{225}{272}, \frac{15}{17}\big) \approx (0{,}681 ;\ 0{,}827 ;\ 0{,}882)$ et $\mathbf{t} = \big(\frac{900}{289}, \frac{40}{17}, \frac{20}{17}\big) \approx (3{,}11 ;\ 2{,}35 ;\ 1{,}18)$.

### Ex M26.5 — Un abonné qui peut résilier chaque mois : durée géométrique, revenu total moyen, et le même nombre comme revenu actualisé

**Réponses.** a) `0.1681` · b) `"10/3"` · c) `30` · d) `30` · e) `0.657` · f) `21`.

**Démarche.** Il paie le mois $t$ si et seulement s'il a renouvelé $t$ fois : $P(N \ge t) = 0{,}7^t$. a) $0{,}7^5 = 0{,}16807$. b) $\mathbb{E}[N + 1] = \sum_{t \ge 0}P(N \ge t) = \frac{1}{0{,}3} = \frac{10}{3}$ : $N + 1$ suit la loi géométrique de paramètre 0,3 (M02b). c) $9 \times \frac{10}{3} = 30$ €. d) $\sum_{t \ge 0}9 \times 0{,}7^t = \frac{9}{0{,}3} = 30$ €. e) Un revenu inférieur à 30 € veut dire au plus 3 mois payés : $P(N \le 2) = 1 - 0{,}7^3 = 0{,}657$. f) $\sum_{t \ge 1}9 \times 0{,}7^t = 9 \times \frac{0{,}7}{0{,}3} = 21$ €.

Dans ta copie : $\mathbb{E}\big[\sum_{t=0}^{N}9\big] = \sum_{t \ge 0}9\,P(N \ge t)$ (on écrit la somme avec $\mathbb{1}\{N \ge t\}$, fiche §4) et $P(N \ge t) = \gamma^t$ : les deux sommes sont égales terme à terme. La loi géométrique a une longue queue : quelques abonnés fidèles rapportent beaucoup, et tirent la moyenne au-dessus de ce que rapporte la majorité.

**Erreurs fréquentes.** $0{,}7^6$ (un renouvellement de trop). $\frac73$ ou $\frac{10}{7}$ pour la durée. Commencer la somme actualisée à $t = 1$ (21 € au lieu de 30). $P(N + 1 \le 4)$ en e). Retirer $9 \times 0{,}7$ au lieu de 9 en f).

**Variante.** Si l'abonné résilie avec la probabilité 0,4 ($\gamma = 0{,}6$) : 2,5 mois en moyenne, 22,50 € de revenu moyen, 13,50 € avec le premier mois offert.

### Ex M26.6 — Une machine qui s'use, deux politiques d'entretien : P_π et r_π, deux systèmes de Bellman 3 × 3, et la valeur d'une action

**Réponses.** a) `4.95` · b) `[[0.7, 0.3, 0], [0.95, 0, 0.05], [0.8, 0, 0.2]]` · c) `[19.95, 8.73, 1.79]` · d) `[21.73, 14.47, 2.76]` · e) `11.17` · f) `True`.

**Démarche.** a) $0{,}65 \times 6 + 0{,}35 \times 3 = 4{,}95$. On a $\mathbf{P}_{\pi_A} = \begin{pmatrix} 0{,}7 & 0{,}3 & 0 \\ 0 & 0{,}65 & 0{,}35 \\ 0{,}8 & 0 & 0{,}2 \end{pmatrix}$, $\mathbf{r}_{\pi_A} = (10 ;\ 4{,}95 ;\ -8)$, et b) la ligne de la machine usée de $\mathbf{P}_{\pi_B}$ vient de « entretenir », avec $\mathbf{r}_{\pi_B} = (10 ;\ 2 ;\ -8)$. c) $(\mathbf{I} - 0{,}6\,\mathbf{P}_{\pi_A})\mathbf{V} = \mathbf{r}$ s'écrit $0{,}58\,V_0 - 0{,}18\,V_1 = 10$, $0{,}61\,V_1 - 0{,}21\,V_2 = 4{,}95$, $-0{,}48\,V_0 + 0{,}88\,V_2 = -8$. La troisième donne $V_2 = \frac{6}{11}V_0 - \frac{100}{11}$, la deuxième $V_1 = \frac{33{,}45 + 1{,}26\,V_0}{6{,}71}$, et la première, multipliée par 6,71, $3{,}665\,V_0 = 73{,}121$ : $V_0 \approx 19{,}9512$, $V_1 \approx 8{,}7315$, $V_2 \approx 1{,}7915$. d) De même, $V_2 = \frac{6}{11}V_0 - \frac{100}{11}$, $V_1 = 2 + 0{,}57\,V_0 + 0{,}03\,V_2 = \frac{19 + 6{,}45\,V_0}{11}$, et $0{,}58\,V_0 - 0{,}18\,V_1 = 10$ donne $5{,}219\,V_0 = 113{,}42$ : $V_0 \approx 21{,}7321$, $V_1 \approx 14{,}4702$, $V_2 \approx 2{,}7630$. e) $Q^{\pi_B}(1, \text{cont}) = 4{,}95 + 0{,}6\,(0{,}65 \times 14{,}4702 + 0{,}35 \times 2{,}7630) = 4{,}95 + 0{,}6 \times 10{,}3727 \approx 11{,}1736$. f) Vrai : $2 + 0{,}6\,(0{,}95 \times 21{,}7321 + 0{,}05 \times 2{,}7630) = 14{,}4702 = V^{\pi_B}(1)$, la deuxième équation du système de $\pi_B$.

Dans ta copie : e) est ce que rapporte en moyenne une machine usée qu'on laisse tourner un mois sans entretien, puis qu'on gère selon $\pi_B$.

**Erreurs fréquentes.** Moyenner 6 et 3 à parts égales (4,5). Garder la ligne « continuer » dans $\mathbf{P}_{\pi_B}$. Écrire $\gamma$ devant $\mathbf{r}$ (on trouve $0{,}6\,\mathbf{V}$). Prendre 6 au lieu de 4,95 pour la machine usée sous $\pi_A$, ou 6 au lieu de 2 sous $\pi_B$. Calculer $Q^{\pi_B}$ avec les valeurs de $\pi_A$, ou avec la ligne de l'entretien.

**Variante.** Avec $\gamma = 0{,}7$ : $\mathbf{V}^{\pi_A} \approx (24{,}59 ;\ 12{,}10 ;\ 6{,}71)$ et $\mathbf{V}^{\pi_B} \approx (28{,}32 ;\ 21{,}15 ;\ 9{,}14)$.

### Ex M26.7 — Les itérés de Bellman de la machine de M26.6 : trois pas synchrones puis en place, comparés à la solution, et le nombre d'itérations qui garantit 10⁻³

**Réponses.** a) `[17.27431, 6.104595, -1.25552]` · b) `3.0471` · c) `[17.45575, 7.1318478, 0.2419216]` · d) `2.4954` · e) `20` · f) `"1/1500"` · g) `4.36`.

**Démarche.** $\mathbf{V}_1 = \mathbf{r} = (10 ;\ 4{,}95 ;\ -8)$. $\mathbf{P}\mathbf{V}_1 = (8{,}485 ;\ 0{,}4175 ;\ 6{,}4)$, donc $\mathbf{V}_2 = (15{,}091 ;\ 5{,}2005 ;\ -4{,}16)$. $\mathbf{P}\mathbf{V}_2 = (12{,}12385 ;\ 1{,}924325 ;\ 11{,}2408)$, donc a) $\mathbf{V}_3 = (17{,}27431 ;\ 6{,}104595 ;\ -1{,}25552)$. b) $\mathbf{V} - \mathbf{V}_3 \approx (2{,}6769 ;\ 2{,}6269 ;\ 3{,}0471)$. c) En place : $W(0) = 10$, $W(1) = 4{,}95$ (elle ne dépend pas de $W(0)$), $W(2) = -8 + 0{,}6 \times 0{,}8 \times 10 = -3{,}2$ ; puis $\mathbf{W}_2 = (15{,}091 ;\ 6{,}2085 ;\ -1{,}14032)$ et $\mathbf{W}_3 = (17{,}45575 ;\ 7{,}1318478 ;\ 0{,}2419216)$, par exemple $W(1) = 4{,}95 + 0{,}6\,(0{,}65 \times 6{,}2085 + 0{,}35 \times (-1{,}14032))$. d) $\mathbf{V} - \mathbf{W}_3 \approx (2{,}4954 ;\ 1{,}5997 ;\ 1{,}5496)$. e) $0{,}6^k \times 19{,}95116 \le 10^{-3}$ si et seulement si $k \ge \frac{\ln(10^{-3}/19{,}95116)}{\ln 0{,}6} \approx 19{,}38$ : 20 itérations. f) $10^{-3} \times \frac{0{,}4}{0{,}6} = \frac{1}{1500}$. g) $\lVert\mathbf{V}_3 - \mathbf{V}_2\rVert_\infty = \max(2{,}18331 ;\ 0{,}904095 ;\ 2{,}90448) = 2{,}90448$, et $\frac{0{,}6}{0{,}4} \times 2{,}90448 \approx 4{,}36 \ge 3{,}05$.

Dans ta copie : g) majore bien b), sans être serrée. $\mathbf{P}$ est stochastique, donc $\gamma\mathbf{P}\mathbf{1} = \gamma\mathbf{1}$ : la composante de l'écart le long de $\mathbf{1}$ est multipliée exactement par $\gamma$ à chaque pas, et la borne a priori est presque atteinte ; il faut à peine moins de 20 itérations (le notebook en trouve 19).

**Erreurs fréquentes.** Mélanger les deux balayages (servir en synchrone d'une valeur déjà mise à jour). Oublier $\gamma$. Prendre la somme des écarts au lieu du plus grand. Arrondir 19,38 à 19, ou oublier $\lVert\mathbf{V}\rVert_\infty$ (14 itérations). Écrire $\varepsilon\frac{\gamma}{1 - \gamma}$ ($\frac{3}{2000}$) ou $\varepsilon$ seul pour le seuil. Diviser par $1 - \gamma$ au lieu de multiplier par $\frac{\gamma}{1 - \gamma}$ en g).

**Variante.** Avec $\gamma = 0{,}7$, $\lVert\mathbf{V}^{\pi_A}\rVert_\infty \approx 24{,}59$ : la borne a priori demande 29 itérations, et le seuil a posteriori vaut $\frac{3}{7000}$.

### Ex M26.8 — Vendre une voiture d'occasion : offres au hasard, coût d'attente, valeur de continuation et règle à seuil

**Réponses.** a) `4500` · b) `4061` · c) `[5000, 7000]` · d) `4837` · e) `4040` · f) `21`.

**Démarche.** a) $900 + 1\,200 + 1\,000 + 1\,400 = 4\,500$ €. b) Si $3\,000 \le C \le 4\,000$, $\mathbb{E}[\max(X, C)] = 0{,}3\,C + 3\,600$, et $C = -50 + 0{,}85\,(0{,}3\,C + 3\,600)$ donne $0{,}745\,C = 3\,010$, $C \approx 4\,040{,}27$ : hors de l'intervalle, rejeté. Si $4\,000 \le C \le 5\,000$, $\mathbb{E}[\max(X, C)] = 0{,}6\,C + 2\,400$, et $0{,}49\,C = 1\,990$ : $C^\star \approx 4\,061{,}22$, dans l'intervalle. (Sous 3 000 €, on trouverait $-50 + 0{,}85 \times 4\,500 = 3\,775$, et entre 5 000 et 7 000 €, 3 562,50 : rejetés tous deux.) Le point fixe est unique (contraction), c'est donc lui. c) Elle accepte $x \ge C^\star$ : 5 000 et 7 000 €. d) $\mathbb{E}[\max(X, C^\star)] = 0{,}6 \times 4\,061{,}22 + 2\,400 \approx 4\,836{,}73$ €, aussi $\frac{C^\star - c}{\gamma}$. e) La règle refuse seulement 3 000 € : $C_r = -50 + 0{,}85\,(0{,}3\,C_r + 3\,600)$, l'équation linéaire de son évaluation, donne $C_r \approx 4\,040{,}27$ €. f) $4\,061{,}22 - 4\,040{,}27 \approx 20{,}96$ €.

Dans ta copie : la solution rejetée de l'intervalle $[3\,000, 4\,000]$ est exactement e) : sur chaque intervalle, $\max(X, C)$ prend les décisions d'une règle à seuil, et l'équation linéaire est celle de cette règle. $C^\star$ est la seule valeur cohérente avec sa propre règle, et la plus grande.

**Erreurs fréquentes.** Oublier $\gamma$ (on trouve 6 750 €) ou le coût $c$ (4 163 €). Garder la solution de $[3\,000, 4\,000]$ sans vérifier l'intervalle. Accepter 4 000 €. Donner $\mathbb{E}[X]$ ou $C^\star$ en d). Évaluer en e) la règle « seulement 7 000 € » (3 562,50 €).

**Variante.** Si la meilleure offre vaut 8 000 € au lieu de 7 000 €, $C^\star \approx 4\,408$ € : elle accepte toujours 5 000 et 8 000 €.

### Ex M26.9 — Le meilleur de deux fournisseurs sur des mesures bruitées : le maximum surestime, l'estimateur double non

**Réponses.** a) `[7.5, 10]` · b) `4.99` · c) `0.212` · d) `1007.88` · e) `True` · f) `1011.5`.

**Démarche.** a) $\frac{30}{\sqrt{16}} = 7{,}5$ h et $\frac{30}{\sqrt9} = 10$ h. b) $\max(u, v) = \frac{u + v}{2} + \frac{\lvert u - v\rvert}{2}$ ; $\mathbb{E}\big[\frac{\hat A + \hat B}{2}\big] = \mu$ et $D = \hat A - \hat B \sim \mathcal{N}(0, 7{,}5^2 + 10^2)$, d'écart-type $\sigma_D = 12{,}5$, donc $\mathbb{E}\lvert D\rvert = \sigma_D\sqrt{2/\pi}$ et le biais vaut $\frac{\sigma_D}{\sqrt{2\pi}} \approx 4{,}9868$ h. c) $D \sim \mathcal{N}(10 ;\ 156{,}25)$ : $P(D < 0) = \Phi(-0{,}8) = 1 - 0{,}788145 \approx 0{,}2119$. d) Par l'espérance totale, $1\,010 \times 0{,}788145 + 1\,000 \times 0{,}211855 \approx 1\,007{,}88$ h. e) Vrai : sachant le choix, la remesure a pour espérance la vraie moyenne du fournisseur choisi ; sa moyenne est d), sous 1 010 h. f) $\mathbb{E}\lvert D\rvert = 12{,}5\sqrt{2/\pi}\,e^{-0{,}32} + 10\,(1 - 2 \times 0{,}211855) \approx 7{,}2423 + 5{,}7629 = 13{,}0052$, donc $\mathbb{E}[\max(\hat A, \hat B)] = 1\,005 + 6{,}5026 \approx 1\,011{,}50$ h.

Dans ta copie : la démonstration de la fiche vaut avec deux écarts-types différents, à condition d'additionner les **variances** ; d) $< 1\,010 <$ f) : le maximum surestime la meilleure option, l'estimateur double la sous-estime un peu, parce qu'il choisit parfois B.

**Erreurs fréquentes.** $\frac{\sigma_0}{n}$ au lieu de $\frac{\sigma_0}{\sqrt n}$. La formule $\frac{\sigma}{\sqrt\pi}$ de la fiche avec $\sigma = \sigma_D$ (7,05 h). Additionner les écarts-types. Donner la probabilité de choisir A (0,788). Annoncer 1 010 h en d). Oublier le facteur $\frac12$ devant $\mathbb{E}\lvert D\rvert$ en f).

**Variante.** Si l'entreprise teste aussi 16 batteries de B ($\sigma_A = \sigma_B = 7{,}5$ h) : le biais à moyennes égales vaut $\frac{7{,}5}{\sqrt\pi} \approx 4{,}23$ h (la formule de la fiche), et la probabilité de choisir B tombe à $\Phi(-10/10{,}607) \approx 0{,}173$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M26.10 — L'analyse au premier pas démontrée : t = 1 + Qt et h = Qh + b, et I − Q inversible dès que la fin est possible depuis chaque état

**Démonstration.**
1. Un chemin qui reste parmi les transitoires n'utilise que des coefficients de $\mathbf{Q}$, et un état absorbant ne se quitte plus : $(\mathbf{Q}^t)_{ij} = P(S_t = j \mid S_0 = i)$ pour $j$ transitoire, et la somme de la ligne $i$ de $\mathbf{Q}^t$ est $P(S_t \text{ transitoire} \mid S_0 = i) = P(\text{pas encore absorbé au pas } t)$. Depuis chaque transitoire $i$, un chemin du graphe mène à un état absorbant ; en retirant ses boucles, on en obtient un de longueur $\ell_i \le m$, de probabilité $c_i > 0$. Avec $n = m$ et $\varepsilon = \min_ic_i > 0$ (un minimum sur un nombre fini d'états), la probabilité d'être absorbé en au plus $n$ pas est au moins $c_i \ge \varepsilon$ (une fois absorbé, on le reste). Donc chaque ligne de $\mathbf{Q}^n$, à coefficients positifs, a une somme au plus $1 - \varepsilon$ : $\lVert\mathbf{Q}^n\rVert_\infty \le 1 - \varepsilon$, puis $\lVert\mathbf{Q}^{kn}\rVert_\infty \le \lVert\mathbf{Q}^n\rVert_\infty^k \le (1 - \varepsilon)^k$ (sous-multiplicativité, M22).
2. Pour $t = kn + s$ avec $0 \le s < n$, $\lVert\mathbf{Q}^t\rVert_\infty \le \lVert\mathbf{Q}^{kn}\rVert_\infty\,\lVert\mathbf{Q}^s\rVert_\infty \le (1 - \varepsilon)^k$, car $\lVert\mathbf{Q}^s\rVert_\infty \le 1$ : $\mathbf{Q}^t \to \mathbf{0}$. Si $(\mathbf{I} - \mathbf{Q})\mathbf{x} = \mathbf{0}$, alors $\mathbf{x} = \mathbf{Q}\mathbf{x} = \mathbf{Q}^t\mathbf{x} \to \mathbf{0}$, donc $\mathbf{x} = \mathbf{0}$ : $\mathbf{I} - \mathbf{Q}$ est inversible. Ensuite $P(T > t \mid S_0 = i) = (\mathbf{Q}^t\mathbf{1})_i \le \lVert\mathbf{Q}^t\rVert_\infty$, donc $P(T > kn) \le (1 - \varepsilon)^k \to 0$ et $T < \infty$ avec la probabilité 1. Enfin $t_i = \sum_{u \ge 0}P(T > u \mid S_0 = i) \le n\sum_{k \ge 0}(1 - \varepsilon)^k < \infty$ (les $n$ termes de chaque bloc sont au plus $(1 - \varepsilon)^k$).
3. $T = 1 + T'$, où $T'$ compte les pas parmi les transitoires à partir du pas 1. Si $S_1 = j$ est absorbant, $T' = 0$. Si $j$ est transitoire, sachant $S_0 = i$ et $S_1 = j$, la suite $(S_1, S_2, \ldots)$ est une chaîne partie de $j$ qui ne dépend plus de $S_0$ (propriété de Markov), donc $\mathbb{E}[T' \mid S_0 = i, S_1 = j] = t_j$. Par l'espérance totale, $t_i = 1 + \sum_{j\ \text{transitoire}}q_{ij}\,t_j$, des quantités finies par 2.
4. De même, $h_i = \sum_jp_{ij}\,P(\text{absorption en } a \mid S_0 = i, S_1 = j)$ : ce terme vaut 1 si $j = a$, 0 si $j$ est un autre état absorbant, et $h_j$ si $j$ est transitoire (Markov). Donc $h_i = b_i + \sum_jq_{ij}\,h_j$. Comme $\mathbf{I} - \mathbf{Q}$ est inversible, $\mathbf{t} = (\mathbf{I} - \mathbf{Q})^{-1}\mathbf{1}$ et $\mathbf{h} = (\mathbf{I} - \mathbf{Q})^{-1}\mathbf{b}$ sont les seules solutions.

**Grille de relecture.** Un $n$ et un $\varepsilon > 0$ sont construits (un chemin vers la fin depuis chaque état, un minimum sur un ensemble fini), avec le lien « somme d'une ligne de $\mathbf{Q}^n$ = probabilité de ne pas être encore absorbé ». La sous-multiplicativité donne $(1 - \varepsilon)^k$, et le cas de $t$ quelconque (pas seulement multiple de $n$) est traité. L'inversibilité est justifiée (noyau nul, ou série $\sum_t\mathbf{Q}^t$ qui converge et donne l'inverse). $P(T > t) = (\mathbf{Q}^t\mathbf{1})_i$ et la finitude de $t_i$ sont établies avant d'écrire l'équation. Le conditionnement sur $S_1$ cite la propriété de Markov et traite les états absorbants (0 pour $T'$, 1 ou 0 pour $h$). L'unicité vient de l'inversibilité.

**Variante.** Le même argument montre $(\mathbf{I} - \mathbf{Q})^{-1} = \sum_{t \ge 0}\mathbf{Q}^t$ (la matrice fondamentale), en reprenant les sommes partielles de ∂ M26.11 avec $\mathbf{Q}$ au lieu de $\gamma\mathbf{P}$.

### Ex M26.11 — V = Σ γᵗPᵗr est l'unique solution du système de Bellman : I − γP inversible, série de Neumann démontrée pour γP, et (1 − γ)(I − γP)⁻¹ stochastique

**Démonstration.**
1. La ligne $i$ de $\gamma\mathbf{P}$ a pour somme des valeurs absolues $\gamma\sum_jp_{ij} \le \gamma$ : $\lVert\gamma\mathbf{P}\rVert_\infty \le \gamma$. Les coefficients de $\mathbf{P}^t$ sont positifs ou nuls, et $\mathbf{P}^t\mathbf{1} \le \mathbf{1}$ coordonnée par coordonnée, par récurrence : $\mathbf{P}^{t}\mathbf{1} = \mathbf{P}(\mathbf{P}^{t-1}\mathbf{1}) \le \mathbf{P}\mathbf{1} \le \mathbf{1}$, car $\mathbf{P} \ge 0$. Chaque coefficient de $\mathbf{P}^t$ est donc entre 0 et 1, et chaque coefficient de $\gamma^t\mathbf{P}^t$ entre 0 et $\gamma^t$.
2. $\mathbf{S}_n(\mathbf{I} - \gamma\mathbf{P}) = \sum_{t=0}^{n}\gamma^t\mathbf{P}^t - \sum_{t=1}^{n+1}\gamma^t\mathbf{P}^t = \mathbf{I} - \gamma^{n+1}\mathbf{P}^{n+1}$ : les termes de 1 à $n$ s'annulent. Le même calcul vaut à gauche, puisque $\mathbf{P}$ commute avec ses puissances.
3. Pour chaque $(i, j)$, $\sum_t(\gamma^t\mathbf{P}^t)_{ij}$ est une série à termes positifs majorés par $\gamma^t$ : elle converge par comparaison avec la série géométrique de raison $\gamma < 1$ (R5). Donc $\mathbf{S}_n \to \mathbf{S}$ coefficient par coefficient, et $\gamma^{n+1}\mathbf{P}^{n+1} \to \mathbf{0}$ (coefficients au plus $\gamma^{n+1}$). Le produit par la matrice fixe $\mathbf{I} - \gamma\mathbf{P}$ passe à la limite (chaque coefficient est une somme finie) : $\mathbf{S}(\mathbf{I} - \gamma\mathbf{P}) = (\mathbf{I} - \gamma\mathbf{P})\mathbf{S} = \mathbf{I}$. Si $\mathbf{V} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$, alors $(\mathbf{I} - \gamma\mathbf{P})\mathbf{V} = \mathbf{r}$ et $\mathbf{V} = \mathbf{S}\mathbf{r}$ ; réciproquement, $\mathbf{S}\mathbf{r}$ est solution. Et $\mathbf{S}\mathbf{r} = \lim_n\mathbf{S}_n\mathbf{r} = \sum_{t \ge 0}\gamma^t\mathbf{P}^t\mathbf{r}$.
4. $\mathbf{M} = (1 - \gamma)\mathbf{S}$ a des coefficients positifs ou nuls, limites de sommes de termes positifs. Pour $\mathbf{P}$ stochastique, $(\mathbf{I} - \gamma\mathbf{P})\mathbf{1} = \mathbf{1} - \gamma\mathbf{1} = (1 - \gamma)\mathbf{1}$ ; en multipliant à gauche par $\mathbf{S}$, $\mathbf{1} = (1 - \gamma)\mathbf{S}\mathbf{1} = \mathbf{M}\mathbf{1}$ : $\mathbf{M}$ est stochastique. Pour $\mathbf{P}$ sous-stochastique, $(\mathbf{I} - \gamma\mathbf{P})\mathbf{1} \ge (1 - \gamma)\mathbf{1}$, et $\mathbf{S} \ge 0$ conserve l'inégalité : $\mathbf{1} \ge \mathbf{M}\mathbf{1}$, des lignes de somme au plus 1 (la masse manquante est la probabilité que le processus finisse avant l'arrêt géométrique).

**Grille de relecture.** La majoration de $\lVert\gamma\mathbf{P}\rVert_\infty$ et celle des coefficients de $\gamma^t\mathbf{P}^t$ utilisent la positivité. Le télescopage des sommes partielles est écrit, des deux côtés. La convergence est démontrée (comparaison, ou norme : $\lVert\gamma^t\mathbf{P}^t\rVert_\infty \le \gamma^t$), sans supposer l'inversibilité, et sans renvoyer à M22 ni à CP5.8. Le passage à la limite donne l'inverse, des deux côtés (ou d'un seul côté, en invoquant qu'un inverse à gauche d'une matrice carrée est un inverse). L'unicité est établie : toute solution vaut $\mathbf{S}\mathbf{r}$. Pour $\mathbf{M}$ : la positivité par la série, $\mathbf{M}\mathbf{1} = \mathbf{1}$ par le calcul de $(\mathbf{I} - \gamma\mathbf{P})\mathbf{1}$, et le cas sous-stochastique ($\mathbf{M}\mathbf{1} \le \mathbf{1}$).

**Variante.** Avec $\gamma = 1$ et $\mathbf{P} = \mathbf{Q}$ sous-stochastique dont la fin est sûre, la même preuve vaut dès que $\mathbf{Q}^t \to \mathbf{0}$ assez vite (∂ M26.10) : c'est le cas $\gamma = 1$ permis de la fiche.

### Ex M26.12 — L'opérateur de Bellman d'une politique fixée est une γ-contraction pour ‖·‖∞ ; bornes a priori et a posteriori ; le maximum est 1-lipschitzien

**Démonstration.**
1. Pour $k = 0$, c'est une égalité. Si $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty \le \gamma^k\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty$, alors, comme $\mathcal{T}(\mathbf{V}) = \mathbf{V}$, $\lVert\mathbf{V}_{k+1} - \mathbf{V}\rVert_\infty = \lVert\mathcal{T}(\mathbf{V}_k) - \mathcal{T}(\mathbf{V})\rVert_\infty \le \gamma\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty \le \gamma^{k+1}\lVert\mathbf{V}_0 - \mathbf{V}\rVert_\infty$.
2. $\lVert\mathbf{V}_{k-1} - \mathbf{V}\rVert_\infty \le \lVert\mathbf{V}_{k-1} - \mathbf{V}_k\rVert_\infty + \lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty \le \lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty + \gamma\lVert\mathbf{V}_{k-1} - \mathbf{V}\rVert_\infty$ ; comme $1 - \gamma > 0$, $\lVert\mathbf{V}_{k-1} - \mathbf{V}\rVert_\infty \le \frac{1}{1 - \gamma}\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty$. Puis $\lVert\mathbf{V}_k - \mathbf{V}\rVert_\infty \le \gamma\lVert\mathbf{V}_{k-1} - \mathbf{V}\rVert_\infty \le \frac{\gamma}{1 - \gamma}\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty$. Donc, si $\lVert\mathbf{V}_k - \mathbf{V}_{k-1}\rVert_\infty \le \varepsilon\frac{1 - \gamma}{\gamma}$, l'erreur est au plus $\varepsilon$.
3. Soit $\delta = \lVert\mathbf{U} - \mathbf{W}\rVert_\infty$. Supposons $\lvert U'_j - W'_j\rvert \le \gamma\delta$ pour tout $j < i$ (rien à supposer pour $i = 1$). Alors $\lvert U'_i - W'_i\rvert = \gamma\,\big\lvert\sum_{j < i}p_{ij}(U'_j - W'_j) + \sum_{j \ge i}p_{ij}(U_j - W_j)\big\rvert \le \gamma\big(\sum_{j < i}p_{ij}\,\gamma\delta + \sum_{j \ge i}p_{ij}\,\delta\big) \le \gamma\delta\sum_jp_{ij} \le \gamma\delta$, puisque $\gamma\delta \le \delta$, que les $p_{ij}$ sont positifs et que leur somme est au plus 1. Donc $\lVert\mathbf{U}' - \mathbf{W}'\rVert_\infty \le \gamma\delta$. Si $\mathbf{U} = \mathbf{V}$, la première mise à jour donne $r_1 + \gamma\sum_jp_{1j}V_j = V_1$, et par récurrence chaque coordonnée mise à jour reste égale à $V_i$ (les valeurs déjà mises à jour sont celles de $\mathbf{V}$) : $\mathbf{V}$ est un point fixe du balayage, et $\lVert\mathbf{W}_k - \mathbf{V}\rVert_\infty \le \gamma^k\lVert\mathbf{W}_0 - \mathbf{V}\rVert_\infty \to 0$.
4. Soit $\delta = \lVert\mathbf{x} - \mathbf{y}\rVert_\infty$, et $I$ un ensemble de $k$ indices où $x_i \ge x_{(k)}$ (les $k$ plus grandes coordonnées). Pour $i \in I$, $y_i \ge x_i - \delta \ge x_{(k)} - \delta$ : au moins $k$ coordonnées de $\mathbf{y}$ valent au moins $x_{(k)} - \delta$, donc $y_{(k)} \ge x_{(k)} - \delta$. En échangeant les rôles, $x_{(k)} \ge y_{(k)} - \delta$.
5. Soit $\delta = \sup_E\lvert f - g\rvert$, fini. Pour tout $e \in E$, $f(e) \le g(e) + \delta \le \sup_Eg + \delta$ ; $\sup_Eg + \delta$ majore $f$, donc $\sup_Ef \le \sup_Eg + \delta$. En échangeant les rôles, $\sup_Eg \le \sup_Ef + \delta$.

**Grille de relecture.** 1 : une récurrence qui utilise $\mathcal{T}(\mathbf{V}) = \mathbf{V}$ et la contraction. 2 : l'inégalité triangulaire par $\mathbf{V}_k$, la division par $1 - \gamma > 0$, puis une contraction de plus ; le critère d'arrêt en découle. 3 : une récurrence sur l'indice mis à jour, qui sépare les valeurs déjà mises à jour (écart au plus $\gamma\delta$, donc au plus $\delta$) et les anciennes (écart au plus $\delta$), et utilise des poids positifs de somme au plus 1 ; la vérification que $\mathbf{V}$ est un point fixe du balayage ; la convergence. 4 : un argument sur $k$ coordonnées (ou sur le tri), puis la symétrie. 5 : une majoration point par point, puis le passage au supremum, puis la symétrie. Toute démonstration correcte est acceptée ; on ne demande aucune application à un autre opérateur.

**Variante.** Le minimum, $\min\mathbf{x} = -\max(-\mathbf{x})$, est le cas $k = n$ de la question 4.

### Ex M26.13 — L'erreur TD se télescope : Σ γᵏ δ_{t+k} = G_t − V(S_t) ; une récompense ajoutée γΦ(s′) − Φ(s) décale chaque valeur de −Φ(s)

**Démonstration.**
1. Avec $K = T - t - 1$ : $\sum_{k=0}^{K}\gamma^k\delta_{t+k} = \sum_{k=0}^{K}\gamma^kR_{t+k} + \sum_{k=0}^{K}\big(\gamma^{k+1}V(S_{t+k+1}) - \gamma^kV(S_{t+k})\big)$. La première somme est $G_t$. Dans la seconde, en décalant l'indice du premier terme ($k + 1 = j$), $\sum_{j=1}^{K+1}\gamma^jV(S_{t+j}) - \sum_{k=0}^{K}\gamma^kV(S_{t+k}) = \gamma^{K+1}V(S_{t+K+1}) - V(S_t) = \gamma^{T-t}V(S_T) - V(S_t)$. Comme $V(S_T) = 0$, elle vaut $-V(S_t)$. Sans cette hypothèse, il resterait le terme $\gamma^{T-t}V(S_T)$.
2. Le même calcul, avec $\Phi$ à la place de $V$ : $G'_t = \sum_{k=0}^{K}\gamma^k\big(R_{t+k} + \gamma\Phi(S_{t+k+1}) - \Phi(S_{t+k})\big) = G_t + \gamma^{T-t}\Phi(S_T) - \Phi(S_t) = G_t - \Phi(S_t)$.
3. L'épisode finit avec la probabilité 1, donc l'égalité de 2 vaut avec la probabilité 1, pour $t = 0$. Sachant $S_0 = s$, $\Phi(S_0) = \Phi(s)$ est une constante ; par linéarité de l'espérance (les retours sont intégrables), $\mathbb{E}[G'_0 \mid S_0 = s] = \mathbb{E}[G_0 \mid S_0 = s] - \Phi(s)$, c'est-à-dire $V'(s) = V(s) - \Phi(s)$.

**Grille de relecture.** La séparation des sommes, avec les bonnes bornes ; le décalage d'indice qui montre l'annulation deux à deux ; le rôle de $V(S_T) = 0$ (et de $\Phi(S_T) = 0$). Pour la récompense ajoutée, le passage du retour à l'espérance conditionnelle : la fin sûre, $\Phi(S_0)$ connu sachant $S_0 = s$, la linéarité. Rien n'est demandé sur la façon dont la somme dépend de $V$.

**Variante.** Sur un épisode de deux pas ($T = 2$, $t = 0$) : $\delta_0 + \gamma\delta_1 = R_0 + \gamma V(S_1) - V(S_0) + \gamma R_1 + \gamma^2V(S_2) - \gamma V(S_1) = R_0 + \gamma R_1 - V(S_0)$, puisque $V(S_2) = 0$.

<a id="reflexion"></a>

## 🗣️ 🔗 Explication et pont

### Ex M26.14 — Pont : d'une politique stochastique à la chaîne qu'elle induit, P_π = Σ_a π(a | s) P_a et r_π avec des tableaux à trois axes (actions, états, états), puis Q^π(s, a) et r(s, a, s′)

**Réponses.** a) `(2, 3)` · b) `[[30, 21, 0], [21, 18.9, 0]]` · c) `[30, 20.16, 0]` · d) `[0.4, 0.38, 0.22]` · e) `[169.16, 114.73, 0]` · f) `162.47` · g) `True`.

**Démarche.** a) `(P * R)` garde la forme (2, 3, 3), et la somme sur l'axe 2 ($s'$) laisse (actions, états). b) $r(0, \text{rien}) = 0{,}9 \times 30 + 0{,}1 \times 30 = 30$ ; $r(1, \text{rien}) = 0{,}3 \times 30 + 0{,}4 \times 30 + 0{,}3 \times 0 = 21$ ; $r(0, \text{remise}) = 21$ ; $r(1, \text{remise}) = (0{,}55 + 0{,}35) \times 21 = 18{,}9$ ; depuis « parti », 0. c) $r_\pi(1) = 0{,}6 \times 21 + 0{,}4 \times 18{,}9 = 12{,}6 + 7{,}56 = 20{,}16$. d) $0{,}6\,(0{,}3 ;\ 0{,}4 ;\ 0{,}3) + 0{,}4\,(0{,}55 ;\ 0{,}35 ;\ 0{,}1) = (0{,}4 ;\ 0{,}38 ;\ 0{,}22)$. e) $V(2) = 0$ (état absorbant de récompense nulle) ; il reste $0{,}235\,V_0 - 0{,}085\,V_1 = 30$ et $-0{,}34\,V_0 + 0{,}677\,V_1 = 20{,}16$, de déterminant $0{,}130195$ : $V_0 = \frac{30 \times 0{,}677 + 0{,}085 \times 20{,}16}{0{,}130195} \approx 169{,}1586$ et $V_1 = \frac{0{,}235 \times 20{,}16 + 0{,}34 \times 30}{0{,}130195} \approx 114{,}7325$. f) $21 + 0{,}85\,(0{,}95 \times 169{,}1586 + 0{,}05 \times 114{,}7325) \approx 21 + 0{,}85 \times 166{,}4373 \approx 162{,}4717$. g) Vrai : les lignes restreintes, $(0{,}9 ;\ 0{,}1)$ et $(0{,}4 ;\ 0{,}38)$, ont pour sommes 1 et 0,78, et les équations sont les mêmes puisque $V(\text{parti}) = 0$.

Dans ta copie : `r_sa[a, s]` $= \sum_{s'}$ `P[a, s, s2] * R[a, s, s2]`, soit `(P * R).sum(axis=2)` ; $\mathbf{P}_\pi$ = `np.einsum("sa,ast->st", pi, P)` et $\mathbf{r}_\pi$ = `np.einsum("sa,as->s", pi, r_sa)`. f) est ce que rapporte en moyenne un adhérent fidèle à qui l'on offre une remise ce mois-ci, la politique s'appliquant ensuite.

**Erreurs fréquentes.** Sommer sur l'axe des actions (forme (3, 3)). Prendre la cotisation sans la moyenner sur $s'$ (30 pour un hésitant). Moyenner les deux actions à parts égales, ou échanger 0,6 et 0,4. Écrire $\gamma$ devant $\mathbf{r}$. Mettre la cotisation pleine dans $Q^\pi(0, \text{remise})$, ou la transition de « rien ».

**Variante.** Pour la politique qui offre toujours la remise aux hésitants, $\mathbf{V} \approx (180{,}95 ;\ 147{,}32 ;\ 0)$.

### Ex M26.15 — Expliquer avec une image hors informatique pourquoi une chaîne qui mélange oublie son état de départ

**Réponse modèle (6 à 10 phrases).** Imagine une goutte d'encre déposée à un endroit précis d'un verre d'eau qu'on remue régulièrement. L'endroit où tombe la goutte, c'est l'état de départ ; la façon dont l'encre est répartie dans le verre à chaque instant, c'est la loi de la chaîne. Chaque coup de cuillère déplace chaque particule d'encre un peu au hasard, selon des règles qui ne dépendent que de l'endroit où elle est : la tache s'étale. Au bout de quelques coups, l'encre est répartie de la même façon, quel que soit l'endroit où la goutte est tombée : la répartition ne bouge plus, c'est la loi stationnaire, et elle ne garde aucune trace du départ. Deux choses peuvent l'empêcher : un verre coupé en deux par une paroi, où l'encre reste du côté où elle est tombée (deux classes qui ne communiquent pas), ou un mouvement si régulier qu'il ramène l'encre au même endroit tous les deux coups (une chaîne périodique). La vitesse de l'oubli dépend de l'efficacité du mélange : à chaque coup de cuillère, l'écart à la répartition finale est multiplié par un même facteur, d'autant plus petit que le mélange est énergique.

**En 3 phrases.** La loi de la chaîne est comme une tache d'encre qu'on remue : chaque pas l'étale, et au bout d'un moment sa répartition ne dépend plus de l'endroit de départ. Cela suppose que tout le verre communique et que le mouvement ne soit pas trop régulier. L'écart à la répartition finale est multiplié à chaque pas par un même facteur, qui fixe la vitesse de l'oubli.

**Grille.** L'image, avec une correspondance claire (départ, loi, pas) ; un mélange un peu au hasard à chaque pas, selon l'état présent ; une loi qui ne bouge plus et ne dépend plus du départ ; les deux obstacles (deux parties séparées, un mouvement périodique) ; une vitesse géométrique, liée à l'efficacité du mélange.

<a id="entretien"></a>

## 💼 Entretien

### M26.E1 — « Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que se passe-t-il pour γ = 1 ? »

**Réponse modèle (60 secondes).** « Ce système vient de la valeur d'une politique fixée : en conditionnant sur le premier pas, V égale r plus gamma P V. P est stochastique, donc chaque ligne a des coefficients positifs de somme 1 : sa norme infinie vaut 1, et celle de gamma P vaut gamma, plus petit que 1. Le rayon spectral de gamma P est donc au plus gamma : 1 n'est pas une valeur propre, et I moins gamma P est inversible. On peut aussi le voir par la série de Neumann : la somme des gamma puissance t P puissance t converge, et c'est l'inverse ; elle redonne V comme la somme des récompenses moyennes actualisées. En pratique, on résout avec un solveur, sans former l'inverse, ou l'on itère, et l'erreur est divisée par au moins un sur gamma à chaque pas. Pour gamma égal à 1 et P stochastique, P fois le vecteur des 1 donne le vecteur des 1 : I moins P est singulière, et la somme des récompenses diverge en général, elle grandit comme le nombre de pas fois la récompense moyenne. Mais si le processus finit avec certitude, avec des lignes sous-stochastiques dont la masse manquante est la probabilité de finir, I moins P redevient inversible : c'est le calcul d'une durée moyenne ou d'une probabilité d'absorption. Enfin, quand gamma approche 1, le système devient mal conditionné et l'itération ralentit. »

**Grille.** L'origine du système ; $\lVert\gamma\mathbf{P}\rVert_\infty = \gamma$ et $\rho(\gamma\mathbf{P}) < 1$, ou la série de Neumann ; ce qu'on fait en pratique (résoudre, itérer en $\gamma^k$) ; $\gamma = 1$ sans fin : $\mathbf{P}\mathbf{1} = \mathbf{1}$, une matrice singulière, une somme divergente ; $\gamma = 1$ avec une fin sûre : un système inversible ; le conditionnement quand $\gamma \to 1$.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **M26.16 🔨** `n_step_distribution` : contrôler `P` (carrée, finie, $\ge 0$, lignes de somme 1 à $10^{-9}$), `mu0` et `n` ; `mu = np.array(mu0, dtype=float)`, puis `n` fois `mu = mu @ P` (ou l'élévation au carré). a) Comme M26.1 b) et c). b) $\boldsymbol{\mu}_{100} \approx (0{,}6456 ;\ 0{,}3544 ;\ 0 ;\ 0)$ et $\boldsymbol{\mu}_{101} \approx (0 ;\ 0 ;\ 0{,}5759 ;\ 0{,}4241)$ ; vrai. c) Vrai.
- **M26.17 🔨** `stationary_distribution` : `A = P.T - np.eye(m)`, `A[-1] = 1`, `b = np.zeros(m); b[-1] = 1` ; `ValueError` si `np.linalg.matrix_rank(A) < m` ; `pi = np.linalg.solve(A, b)`, `pi = np.where(pi < 0, 0, pi)`, `pi / pi.sum()`. a) $(0{,}5 ;\ 0{,}3333 ;\ 0{,}1667)$. b) $(0{,}3228 ;\ 0{,}1772 ;\ 0{,}2880 ;\ 0{,}2120)$. c) Vrai (« the stationary law is not unique »). d) $(0 ;\ 0{,}8 ;\ 0{,}2)$ ; vrai (la coordonnée 0 vaut exactement 0 ici).
- **M26.18 🔨** `bellman_linear_solve` : `M = np.eye(m) - gamma * P` ; si `gamma == 1` et `np.linalg.matrix_rank(M) < m`, `ValueError` ; `np.linalg.solve(M, r)`. a) Comme M26.6 c) et d). b) $\mathbf{t} \approx (3{,}1529 ;\ 2{,}4 ;\ 1{,}1765)$ et $\mathbf{h} \approx (0{,}6738 ;\ 0{,}8182 ;\ 0{,}8824)$. c) Vrai ; avec $\gamma = 0{,}96$, $\approx 564{,}49$ € depuis L1 ; vrai. d) 30 et 30 : une ligne qui finit avec la probabilité 0,3 et une actualisation par 0,7 donnent la même valeur.
- **M26.19 🔨** `bellman_fixed_point_iterates` : `out = np.empty((n_steps + 1, m))`, `out[0] = V`, puis `V = r + gamma * (P @ V)` et `out[k] = V`. a) Comme M26.7 a). b) 19 itérations (la borne a priori en garantissait 20) ; le critère a posteriori s'arrête aussi à $k = 19$, avec une erreur $\approx 7{,}7 \times 10^{-4}$ : vrai. c) La ligne 3 de `in_place_sweeps_19` est M26.7 c) ; 17 balayages suffisent.
- **M26.20 📦** a) $\boldsymbol{\pi} \approx (0{,}2091 ;\ 0{,}1252 ;\ 0{,}2322 ;\ 0{,}2518 ;\ 0{,}1021 ;\ 0{,}0797)$. b) Vrai (`null_space` rend une seule colonne). c) 41 pas ; la borne $2\,d^k \le 10^{-12}$ en demande 175. d) $0{,}5121$ et $0{,}5121$ : les valeurs propres de $\mathbf{P}_d$ autres que 1 sont celles de $\mathbf{L}$ multipliées par $d$. e) $[4, 3, 1, 2, 5, 6]$ : la page 4, que pointent trois pages, passe devant la page 3.
- **M26.21 🔮** Prédictions attendues : a) (A) ; b) (B) ; c) (A). d) De l'ordre de $10^{-16}$. e) $0{,}5116$ ; $0{,}4451$ ; $0{,}3060$ ; $0{,}1138$ pour $\gamma = 0{,}6$, $0{,}7$, $0{,}85$, $0{,}96$ : l'écart baisse, mais lentement, car $\lambda_2 \approx 0{,}82$ : il est de l'ordre de $\frac{1 - \gamma}{1 - \gamma\lambda_2}$, qui ne devient petit que tout près de $\gamma = 1$. f) Vrai : chaque ligne tend vers $\big(\frac12, \frac13, \frac16\big)$. g) La matrice identité. La vérification n'emploie aucun $\gamma$ hors de la liste : la limite se calcule exactement.
- **M26.22 🔬** a) Biais naïfs (h), $n = 4$, 16, 64 : $k = 2$ : 8,40 ; 4,18 ; 2,07 ; $k = 3$ : 12,77 ; 6,32 ; 3,17 ; $k = 5$ : 17,47 ; 8,71 ; 4,33 ; $k = 10$ : 23,12 ; 11,55 ; 5,80. b) Vrai (4,18 contre 4,23). c) $\approx 0{,}843$, contre 0,846. d) Vrai (le plus grand écart vaut 0,18 h). e) Naïf $\approx 3{,}47$ h, double $\approx -2{,}38$ h : le naïf reste optimiste, le double devient pessimiste (il choisit parfois un fournisseur moins bon). Le rapport des biais pour $n = 4$ et $n = 64$ vaut à peu près 4.
- **M26.23 🎨** a) $\lvert\lambda_2\rvert = 0{,}7 + \sqrt{0{,}015} \approx 0{,}8225$. b) $\approx -0{,}1954$, égale à $\ln 0{,}8225$ à $10^{-8}$ près. c) $n = 73$. La vérification regarde les titres, l'échelle logarithmique et la légende, et reconnaît une figure qui trace $\boldsymbol{\mu}_n$ en convention colonne (des courbes qui ne tendent pas vers 0).
- **M26.24 🐛** (1) `bikes_after` fait avancer la loi en convention colonne (`P @ mu`, la récurrence de $\mathbf{P}^\top$). Sur $\mathbf{S}$ symétrique, $\mathbf{S}^\top = \mathbf{S}$ et les deux conventions coïncident : la vérification ne pouvait rien voir. Correction : `mu = mu @ P`. a) $(0{,}4604 ;\ 0{,}3072 ;\ 0{,}2324)$ ; la version fautive rend une somme de 1,0604. (2) `market_shares` rend le vecteur propre normalisé pour la norme euclidienne, au signe près : une loi multipliée par une constante vérifie encore $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$, et la vérification ne testait ni la somme ni le signe. Correction : diviser par la somme. b) $(0{,}5 ;\ 0{,}3333 ;\ 0{,}1667)$ ; $\lvert\text{somme}\rvert \approx 1{,}6036$ (le signe du vecteur rendu dépend de la bibliothèque d'algèbre linéaire : ici, il est négatif). (3) Les frais de résiliation sont la récompense de l'état absorbant : ils seraient perçus chaque mois, pour toujours ($\frac{15}{0{,}04} = 375$ € pour un abonné déjà parti). Le résidu ne contrôle que la résolution du système, pas le modèle. Correction : une récompense nulle pour « résilié », et les frais sur la transition, $r(s) = $ `monthly_fee` $\cdot\,\mathbb{1}\{s = 1\} + $ `closing_fee` $\cdot\,p_{s2}$, soit $\mathbf{r} = (6{,}75 ;\ 13{,}5 ;\ 0)$. c) $(59{,}16 ;\ 99{,}26 ;\ 0)$ ; la version fautive donne 375 à l'état résilié (et 352,94 au lieu de 99,26 à un abonné payant). (4) $\gamma = 1$ sans fin : la chaîne des vélos est stochastique, $\mathbf{I} - \mathbf{P}$ est singulière (son rang vaut 2), et `np.linalg.solve` rend selon les arrondis une erreur `LinAlgError` ou, ici, des nombres absurdes ($\approx 6{,}5 \times 10^{16}$). Le cursus de la vérification a une fin sûre. Correction : tester `np.linalg.matrix_rank(np.eye(m) - P) < m` et lever une `ValueError` ; d) vrai. (Avec $\gamma = 0{,}96$, `bellman_linear_solve` donnerait des valeurs finies, $\approx (28{,}80 ;\ 28{,}00 ;\ 27{,}47)$ €.)
- **M26.25 🛠️** a) Les quantités sont d'ordre 1 à 100 et passent par quelques centaines d'opérations : des erreurs relatives de l'ordre de $10^{-15}$ à $10^{-13}$ ; `1e-9 * scale` laisse une marge sans masquer une vraie faute (celles des versions fausses sont d'ordre 1). b) Vrai ; pire rapport $\approx 1{,}0000$ : pour une chaîne stochastique, la composante de $\mathbf{V}_0 - \mathbf{V}$ le long de $\mathbf{1}$ est multipliée exactement par $\gamma$ à chaque pas, et elle finit par dominer l'écart. c) `"law"` = 138 (les essais stochastiques dont la loi stationnaire est unique) ; vrai. d) `"recurrence"` = 292 ; vrai : un balayage en place est aussi une γ-contraction (∂ M26.12), il passe les deux bornes. e) Vrai (et `"recurrence"`, `"a_posteriori"`, `"fixed_point"` comptent aussi les 300 essais). Ce test ajoute à ceux de `tests/test_m26_markov.py` la borne a posteriori, des chaînes sous-stochastiques et creuses tirées au hasard, des échecs comptés et la preuve qu'il attrape des versions fausses que les propriétés prises une à une laissent passer.
- **M26.26 🏆** a) $V \approx 1{,}8787$ €. b) Un écart-type $\approx 1{,}84$ € ; une erreur type de 0,004 demanderait $\approx 212\,000$ visites ($\approx 707\,000$ pas), plus que le budget. c) La référence simule $0{,}95 \times 600\,000 \times 0{,}3 = 171\,000$ visites par graine ($\approx 570\,000$ pas, une erreur type $\approx 0{,}0045$) et réussit 9 fois sur 10 (la graine 6230 donne 1,8682, à 0,0106). Le retour actualisé tronqué à 60 pas a un écart-type $\approx 0{,}45$ €, quatre fois plus petit, pour un biais de troncature d'au plus $0{,}7^{60}\lVert\mathbf{V}\rVert_\infty \approx 2 \times 10^{-9}$ € : l'arrêt géométrique paie l'absence de tout biais par une variance bien plus grande. La vérification refuse un estimateur qui actualise en plus (sur la chaîne de récompenses 1, `estimate * n_visits` ne vaut plus `n_steps`), qui coupe les visites (la moyenne tombe sous 25), ou qui continue avec la probabilité $1 - \gamma$.
