# M16 · Applications affines, graphes et variance d'un produit — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m16_couches_affines/06_mes_reponses.md` (créée par `python tools/start_chapter.py M16`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les points sont des **lignes**, une application affine de $\mathbb{R}^n$ dans $\mathbb{R}^m$ s'écrit $\mathbf{x} \mapsto \mathbf{x}\mathbf{W} + \mathbf{b}$ avec $\mathbf{W}$ de forme $(n, m)$ et $\mathbf{b}$ de forme $(m,)$ ; sa matrice homogène est $\mathbf{H} = \begin{pmatrix} \mathbf{W} & \mathbf{0} \\ \mathbf{b} & 1 \end{pmatrix}$, et $[\mathbf{x}, 1]\,\mathbf{H} = [\mathbf{x}\mathbf{W} + \mathbf{b}, 1]$. La matrice d'adjacence d'un graphe orienté a $A_{ij} = 1$ quand il y a une arête $i \to j$ ; un chemin de longueur $k$ est une suite de $k$ arêtes consécutives (un nœud peut revenir). Une matrice s'écrit dans le notebook comme une liste de ses **lignes**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M16.Q1 — Les formes de W, de b et de x W + b, dans chaque convention 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Une application affine de $\mathbb{R}^5$ dans $\mathbb{R}^2$, écrite en lignes, $\mathbf{x}\mathbf{W} + \mathbf{b}$ : formes de $\mathbf{W}$ et de $\mathbf{b}$ ?
2. La même application écrite en colonnes (MML), $\mathbf{A}\mathbf{x} + \mathbf{b}$ : forme de $\mathbf{A}$, et lien avec $\mathbf{W}$ ?
3. Vrai ou faux : dans $\mathbf{x}\mathbf{W} + \mathbf{b}$, la colonne $k$ de $\mathbf{W}$ suffit, avec $b_k$, à calculer la sortie $k$.
4. $\mathbf{X}$ a la forme $(100, 5)$ : forme de $\mathbf{X}\mathbf{W} + \mathbf{b}$, et nombre de paramètres de l'application ?
5. Vrai ou faux : si l'application va de $\mathbb{R}^3$ dans $\mathbb{R}^3$ et que $\mathbf{W}$ est rangée dans la mauvaise convention, `x @ W + b` lève une erreur.
6. Combien de multiplications coûte le produit $\mathbf{X}\mathbf{W}$ de la question 4 ?

### M16.Q2 — Coordonnées homogènes et composition : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. Quelle est la forme de la matrice homogène d'une application affine de $\mathbb{R}^3$ dans $\mathbb{R}^2$ ?
2. Vrai ou faux : la dernière coordonnée de $[\mathbf{x}, 1]\,\mathbf{H}$ vaut toujours 1.
3. Vrai ou faux : avec des lignes, appliquer $f_1$ puis $f_2$ s'écrit $[\mathbf{x}, 1]\,\mathbf{H}_2\mathbf{H}_1$.
4. Écris la matrice homogène de la translation du plan de vecteur $(a, b)$.
5. Vrai ou faux : pour deux translations du plan, $\mathbf{H}_1\mathbf{H}_2 = \mathbf{H}_2\mathbf{H}_1$.
6. Vrai ou faux : la matrice homogène d'une application affine de $\mathbb{R}^2$ dans $\mathbb{R}^2$ est toujours inversible.

### M16.Q3 — Lire une matrice d'adjacence : degrés, arêtes, chemins, cycles 🧠 ★ ⏱️ 4 min
*Fiche §3 et §4 · parcours C, E*

Un graphe à 4 nœuds a pour matrice d'adjacence $\mathbf{A} = \begin{pmatrix} 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$.
1. Combien d'arêtes a-t-il ?
2. Quel est le degré entrant du nœud 4 ? Son degré sortant ?
3. Combien de chemins de longueur 2 vont du nœud 1 au nœud 4 ? Et de longueur 3 ?
4. Le graphe a-t-il un cycle ? Comment le voir d'un coup d'œil sur $\mathbf{A}$ ?
5. Vrai ou faux : si $(\mathbf{A}^2)_{ij} = 0$, il n'y a aucun chemin de $i$ à $j$.
6. Vrai ou faux : dans un graphe à 10 nœuds avec un cycle, $\mathbf{A}^{10} \ne \mathbf{0}$.

### M16.Q4 — Indépendantes, décorrélées, ou ni l'un ni l'autre ? 🧠 ★ ⏱️ 4 min
*Fiche §5 et §6 · parcours C, E*

1. $X$ et $Y$ sont indépendantes, $\mathbb{E}[X] = 2$ et $\mathbb{E}[Y] = -1$ : que vaut $\mathbb{E}[XY]$ ?
2. $X$ et $Y$ sont indépendantes et centrées, $\mathbb{V}(X) = 4$ et $\mathbb{V}(Y) = 9$ : que vaut $\mathbb{V}(XY)$ ?
3. Vrai ou faux : pour $X$ et $Y$ indépendantes, $\mathbb{V}(XY) \ge \mathbb{V}(X)\,\mathbb{V}(Y)$.
4. $\varepsilon$ vaut $\pm 1$ avec la probabilité $\frac{1}{2}$ chacun, indépendamment de $x$, et $\mathbb{E}[x^2] = 5$ : que vaut $\mathbb{V}(\varepsilon x)$ ?
5. Vrai ou faux : pour que $\mathbb{V}(Z_1 + Z_2 + Z_3) = \mathbb{V}(Z_1) + \mathbb{V}(Z_2) + \mathbb{V}(Z_3)$, il faut que les $Z_i$ soient indépendantes.
6. Vrai ou faux : si $x_2 = x_1$, les produits $\varepsilon_1x_1$ et $\varepsilon_2x_2$, avec des signes $\varepsilon_1$, $\varepsilon_2$ indépendants, centrés et indépendants de $x_1$, sont décorrélés.

<a id="rappels"></a>

## 🔁 Rappels

### M16.R1 — Le produit matriciel, ses formes et son coût (M09a) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. $\mathbf{A}$ a la forme $(3, 4)$ et $\mathbf{B}$ la forme $(4, 6)$ : forme de $\mathbf{A}\mathbf{B}$ ? Le produit $\mathbf{B}\mathbf{A}$ existe-t-il ?
2. Combien de multiplications coûte $\mathbf{A}\mathbf{B}$ ?
3. Écris $(\mathbf{A}\mathbf{B})^\top$ en fonction de $\mathbf{A}^\top$ et $\mathbf{B}^\top$.
4. Calcule le produit de Hadamard $(1, -2, 3) \odot (4, 0, -1)$.
5. $\mathbf{x}$ est une ligne de forme $(4,)$ : forme de $\mathbf{x}\mathbf{B}$ ?

### M16.R2 — La variance d'une somme de variables indépendantes (M02b) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

Dans tout le rappel, $X$ et $Y$ sont indépendantes, $\mathbb{E}[X] = 1$, $\mathbb{V}(X) = 2$, $\mathbb{E}[Y] = -3$, $\mathbb{V}(Y) = 5$.
1. $\mathbb{E}[2X - Y]$ et $\mathbb{V}(2X - Y)$ ?
2. $\mathbb{E}[X^2]$ ?
3. $\operatorname{Cov}(X, Y)$, et pourquoi ?
4. La variance de la somme de 10 copies indépendantes de $X$ ? Et celle de $10X$ ?
5. La variance de la loi uniforme sur $[0 ; 6]$ ?

### M16.R3 — Les valeurs propres d'une matrice triangulaire (M12c) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C*

1. Les valeurs propres de $\begin{pmatrix} 2 & 5 & -1 \\ 0 & -3 & 4 \\ 0 & 0 & 7 \end{pmatrix}$ ?
2. Son déterminant ?
3. Les valeurs propres d'une matrice strictement triangulaire supérieure ?
4. Vrai ou faux : une matrice dont toutes les valeurs propres sont nulles est la matrice nulle.
5. Calcule $\mathbf{N}^2$ et $\mathbf{N}^3$ pour $\mathbf{N} = \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit.

### Ex M16.1 — Une application affine de ℝ³ dans ℝ² dans les deux conventions : formes, transposée, nombre de paramètres ✏️ ★ ⏱️ 15 min
**Objectif :** écrire une application affine en lignes et en colonnes, avec les formes, l'appliquer à un point et à plusieurs points d'un coup, et compter ses paramètres.
**Prérequis :** fiche §1 ; M09a · **Parcours :** C, E

$g(x_1, x_2, x_3) = (x_1 - 2x_3 + 3,\ 4x_1 + x_2 - x_3 - 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice $\mathbf{W}$ telle que $g(\mathbf{x}) = \mathbf{x}\mathbf{W} + \mathbf{b}$, $\mathbf{x}$ en ligne | une matrice (liste de lignes) |
| b | le vecteur $\mathbf{b}$ | une liste de 2 nombres |
| c | $g(2, -1, 1)$ | une liste de 2 nombres |
| d | la matrice $\mathbf{A}$ telle que $g(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}$, $\mathbf{x}$ en colonne | une matrice (liste de lignes) |
| e | le nombre de paramètres de $g$ | un entier |
| f | les images des trois points $(1, 0, 0)$, $(0, 1, 0)$ et $(1, 1, 1)$, rangées en lignes : $\mathbf{X}\mathbf{W} + \mathbf{1}\mathbf{b}^\top$ | une matrice (liste de lignes) |
| g | le nombre de paramètres d'une application affine de $\mathbb{R}^{60}$ dans $\mathbb{R}^7$ | un entier |
| h | le nombre de multiplications du produit $\mathbf{X}\mathbf{W}$ pour 500 points de $\mathbb{R}^{60}$ et cette application | un entier |

Dans ta copie : quelle ligne de $\mathbf{W}$ dit comment $x_3$ se répartit entre les deux sorties, et quelle colonne sert à calculer la deuxième sortie ? Vérifie que d) est la transposée de a). Pourquoi la ligne 1 de f) ne dépend-elle que du point $(1, 0, 0)$ ? Pourquoi f) contient-il, en plus de $\mathbf{b}$, les lignes de $\mathbf{W}$ ?

### Ex M16.2 — Rotation, homothétie puis translation du plan : la matrice homogène de la composée, et celle de la réciproque ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire des matrices homogènes en lignes, les multiplier dans le bon ordre, appliquer et inverser la composée.
**Prérequis :** fiche §2 ; M12a §8 · **Parcours :** C, E

$f_1$ est la rotation du plan d'un quart de tour dans le sens direct autour de l'origine, $(x, y) \mapsto (-y, x)$ ; $f_2$ est l'homothétie de centre l'origine et de rapport 2 ; $f_3$ est la translation de vecteur $(1, -3)$. On applique $f_1$, puis $f_2$, puis $f_3$ : $f = f_3 \circ f_2 \circ f_1$. Toutes les matrices sont homogènes, $3 \times 3$, pour des points en **lignes**.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice homogène $\mathbf{H}_1$ de $f_1$ | une matrice (liste de lignes) |
| b | la matrice homogène $\mathbf{H}_2$ de $f_2$ | une matrice (liste de lignes) |
| c | la matrice homogène $\mathbf{H}_3$ de $f_3$ | une matrice (liste de lignes) |
| d | la matrice homogène $\mathbf{H}$ de $f$ | une matrice (liste de lignes) |
| e | l'image du point $(2, 1)$ par $f$ | une liste de 2 nombres |
| f | la matrice homogène de $f^{-1}$ | une matrice (liste de lignes, nombres décimaux) |
| g | l'image du point $(2, 1)$ si l'on applique les trois dans l'ordre inverse : $f_3$, puis $f_2$, puis $f_1$ | une liste de 2 nombres |

Dans ta copie : vérifie a) sur le point $(1, 0)$, qui doit aller en $(0, 1)$. Écris $f(x, y)$ en formule à partir de d). Calcule f) de deux façons : en inversant $\mathbf{H}$, et en défaisant les trois étapes dans l'ordre inverse ; vérifie que l'image de e) revient en $(2, 1)$. Pourquoi e) et g) diffèrent-ils ?

### Ex M16.3 — Des rues à sens unique : degrés, matrice d'adjacence, et chemins de longueur 2 et 3 par ses puissances ✏️ ★ ⏱️ 15 min
**Objectif :** écrire une matrice d'adjacence, y lire les degrés, et compter des chemins par ses puissances.
**Prérequis :** fiche §3 · **Parcours :** C, E

Cinq carrefours, numérotés de 1 à 5, sont reliés par des rues à sens unique : $1 \to 2$, $2 \to 3$, $3 \to 1$, $2 \to 4$, $3 \to 4$, $4 \to 5$ et $3 \to 5$.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice d'adjacence $\mathbf{A}$ | une matrice (liste de lignes) |
| b | les degrés sortants des carrefours 1 à 5 | une liste de 5 entiers |
| c | les degrés entrants des carrefours 1 à 5 | une liste de 5 entiers |
| d | $\mathbf{A}^2$ | une matrice (liste de lignes) |
| e | le nombre de chemins de longueur 2 du carrefour 1 au carrefour 4 | un entier |
| f | le nombre de chemins de longueur 3 du carrefour 1 au carrefour 5 | un entier |
| g | le nombre de chemins de longueur 3 qui reviennent à leur carrefour de départ, tous départs confondus | un entier |
| h | le nombre total de chemins de longueur 2 | un entier |

Dans ta copie : liste les chemins de f) et ceux de g). Pourquoi $\mathbf{A}^k$ n'est-elle nulle pour aucun $k$ ? Quelle rue faudrait-il supprimer pour que le réseau n'ait plus de cycle, et que deviendrait alors g) ?

### Ex M16.4 — Un planning de tâches : l'absence de cycle par les puissances de A, une numérotation qui la rend triangulaire, et le nombre de chemins entre deux tâches ✏️ ★★ ⏱️ 25 min
**Objectif :** vérifier qu'un graphe est sans cycle, le renuméroter pour rendre sa matrice triangulaire, et sommer sur ses chemins.
**Prérequis :** fiche §4 ; M16.3 · **Parcours :** C, E

Un atelier fabrique un meuble en six tâches, numérotées dans l'ordre où on les a notées : 1 Montage, 2 Commande, 3 Expédition, 4 Peinture, 5 Découpe, 6 Contrôle. Une arête $i \to j$ veut dire « la tâche $i$ doit être finie avant la tâche $j$ » : Commande → Découpe, Commande → Peinture, Découpe → Peinture, Découpe → Montage, Peinture → Montage, Montage → Contrôle, Montage → Expédition, Contrôle → Expédition.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice d'adjacence $\mathbf{A}$, dans la numérotation donnée | une matrice (liste de lignes) |
| b | les degrés entrants des tâches 1 à 6 | une liste de 6 entiers |
| c | le nombre de chemins de longueur 2 de Commande à Montage | un entier |
| d | le nombre de chemins, de toutes longueurs, de Commande à Expédition | un entier |
| e | une numérotation qui rend la matrice strictement triangulaire supérieure : la liste des **anciens** numéros, dans le nouvel ordre | une liste de 6 entiers |
| f | le nombre de chemins, de toutes longueurs, de Découpe à Expédition | un entier |
| g | le nombre total de chemins du graphe : la somme de toutes les cases de $\mathbf{A} + \mathbf{A}^2 + \cdots + \mathbf{A}^5$ | un entier |

Dans ta copie : pourquoi $\mathbf{A}$ n'est-elle pas triangulaire dans la numérotation donnée ? Pourquoi e) est-elle la seule numérotation possible ici ? Écris la matrice renumérotée et déduis-en, sans calcul de puissance, que $\mathbf{A}^6 = \mathbf{0}$. Pourquoi d) est-il le coefficient (Commande, Expédition) de $(\mathbf{I} - \mathbf{A})^{-1}$ ?

### Ex M16.5 — Un prix aléatoire fois une quantité indépendante : espérance et variance du produit ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer l'espérance, le second moment et la variance d'un produit de variables indépendantes, et mesurer ce qu'oublie la formule fausse.
**Prérequis :** fiche §5 ; M02b · **Parcours :** C, E

Une coopérative vend chaque semaine une quantité $Q$ de pommes (en kilos), au prix $P$ du marché (en € par kilo) ; $P$ et $Q$ sont indépendants, $\mathbb{E}[P] = 3$, $\mathbb{V}(P) = 0{,}16$, $\mathbb{E}[Q] = 120$, $\mathbb{V}(Q) = 400$. La recette est $R = PQ$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{E}[R]$ | un nombre |
| b | $\mathbb{E}[P^2]$ | un nombre |
| c | $\mathbb{E}[Q^2]$ | un nombre |
| d | $\mathbb{V}(R)$ | un nombre |
| e | l'écart-type de $R$ | un nombre (2 décimales) |
| f | ce que donnerait la formule fausse $\mathbb{V}(P)\,\mathbb{V}(Q)$ | un nombre |
| g | le coefficient de variation de $R$, $\frac{\sigma_R}{\mathbb{E}[R]}$ | un nombre (4 décimales) |
| h | la variance de $R$ si le prix était fixé à 3 € | un nombre |

Dans ta copie : écris d) comme la somme des trois termes de la fiche, et dis lequel domine et pourquoi. Vérifie $1 + c_R^2 = (1 + c_P^2)(1 + c_Q^2)$. Que serait d) si $P$ et $Q$ n'étaient pas indépendants (un prix qui baisse quand la récolte est abondante) : la formule s'appliquerait-elle ?

### Ex M16.6 — Des signes aléatoires d'amplitudes différentes sur des mesures corrélées : la variance d'une somme de produits ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la variance d'une somme de produits par des multiplicateurs aléatoires centrés, et voir les covariances disparaître ou revenir selon les hypothèses.
**Prérequis :** fiche §6 ; M02c · **Parcours :** C, E

Trois mesures centrées $x_1$, $x_2$, $x_3$ ont la matrice de covariance $\begin{pmatrix} 4 & 5 & 1 \\ 5 & 9 & 2 \\ 1 & 2 & 1 \end{pmatrix}$. Trois multiplicateurs $\varepsilon_1 = \pm 1$, $\varepsilon_2 = \pm 0{,}5$, $\varepsilon_3 = \pm 2$ prennent chacun leurs deux valeurs avec la probabilité $\frac{1}{2}$, indépendamment entre eux et des mesures. $S = \varepsilon_1x_1 + \varepsilon_2x_2 + \varepsilon_3x_3$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{V}(x_1 + x_2 + x_3)$ | un nombre |
| b | $\mathbb{V}(\varepsilon_2)$ | un nombre |
| c | $\mathbb{V}(S)$ | un nombre |
| d | $\operatorname{Cov}(\varepsilon_1x_1,\ \varepsilon_2x_2)$ | un nombre |
| e | $\mathbb{V}(S)$ si $x_1$ avait pour moyenne 1 au lieu de 0, le reste inchangé | un nombre |
| f | $\mathbb{V}\big(\varepsilon(x_1 + x_2 + x_3)\big)$, avec **un seul** signe $\varepsilon = \pm 1$ pour les trois mesures | un nombre |
| g | $\mathbb{V}\big((1 + \varepsilon_1)x_1 + (1 + \varepsilon_2)x_2 + (1 + \varepsilon_3)x_3\big)$ : des multiplicateurs de moyenne 1 | un nombre |

Dans ta copie : justifie d) à partir des hypothèses (laquelle sert à chaque étape ?). Pourquoi les covariances 5, 1 et 2 n'apparaissent-elles pas dans c) ? Pourquoi e) fait-il intervenir $\mathbb{E}[x_1^2]$ et non $\mathbb{V}(x_1)$ ? Explique f) et g) : quelle hypothèse du lemme manque à chaque fois ? Pour g), écris la somme comme $(x_1 + x_2 + x_3) + S$ et calcule la covariance des deux morceaux.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M16.7 — (Aᵏ)ᵢⱼ compte les chemins de longueur k de i à j, par récurrence ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer par récurrence que les puissances de la matrice d'adjacence comptent les chemins, et l'étendre aux poids.
**Prérequis :** fiche §3 ; R4 · **Parcours :** C

$\mathbf{A}$ est la matrice d'adjacence d'un graphe orienté à $n$ nœuds ; on note $c_k(i, j)$ le nombre de chemins de longueur $k$ de $i$ à $j$.
1. Vérifie l'énoncé pour $k = 1$.
2. Un chemin de longueur $k + 1$ de $i$ à $j$ se termine par une arête $l \to j$. Montre que $c_{k+1}(i, j) = \sum_{l=1}^n c_k(i, l)\,A_{lj}$ (dis pourquoi chaque chemin est compté exactement une fois).
3. Conclus par récurrence : $(\mathbf{A}^k)_{ij} = c_k(i, j)$ pour tout $k \ge 1$.
4. Avec des poids $A_{ij}$ sur les arêtes, adapte la démonstration : $(\mathbf{A}^k)_{ij}$ est la somme, sur les chemins de longueur $k$ de $i$ à $j$, des produits des poids.
5. Que compte la somme de la ligne $i$ de $\mathbf{A}^k$ ? Et la trace de $\mathbf{A}^k$ ?

### Ex M16.8 — Un graphe est sans cycle si et seulement si sa matrice d'adjacence est nilpotente ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer le lien entre l'absence de cycle et la nilpotence, et en déduire la somme sur les chemins.
**Prérequis :** fiche §4 ; M16.7 · **Parcours :** C, E

$\mathbf{A}$ est la matrice d'adjacence d'un graphe orienté à $n$ nœuds. On admet le résultat de M16.7.
1. Montre qu'un chemin de $n$ arêtes passe deux fois par un même nœud (compte les nœuds qu'il visite), et qu'il contient alors un cycle.
2. Déduis-en : si le graphe est sans cycle, alors $\mathbf{A}^n = \mathbf{0}$.
3. Réciproquement, le graphe a un cycle de longueur $m$ qui passe par le nœud $i$. Montre que $(\mathbf{A}^{qm})_{ii} \ge 1$ pour tout entier $q \ge 1$, et conclus qu'aucune puissance de $\mathbf{A}$ n'est nulle.
4. Énonce l'équivalence démontrée.
5. On suppose le graphe sans cycle. Montre que $(\mathbf{I} - \mathbf{A})(\mathbf{I} + \mathbf{A} + \cdots + \mathbf{A}^{n-1}) = \mathbf{I}$, et déduis-en que $\mathbf{I} - \mathbf{A}$ est inversible et que, pour $i \ne j$, $\big((\mathbf{I} - \mathbf{A})^{-1}\big)_{ij}$ est le nombre de chemins de $i$ à $j$.

### Ex M16.9 — La variance d'un produit de deux variables indépendantes ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer la formule de la variance d'un produit de variables indépendantes, et en tirer deux conséquences.
**Prérequis :** fiche §5 ; M02b · **Parcours :** C

$X$ et $Y$ sont deux variables aléatoires discrètes indépendantes, qui ont une variance.
1. Montre que $X^2$ et $Y^2$ sont indépendantes : pour toutes valeurs $u$ et $v$, exprime l'événement $\{X^2 = u\}$ avec des valeurs de $X$, et utilise l'indépendance de $X$ et $Y$.
2. Déduis-en $\mathbb{E}[X^2Y^2] = \mathbb{E}[X^2]\,\mathbb{E}[Y^2]$ (M02b §5), puis $\mathbb{V}(XY) = \mathbb{E}[X^2]\,\mathbb{E}[Y^2] - \mathbb{E}[X]^2\,\mathbb{E}[Y]^2$.
3. Développe pour obtenir $\mathbb{V}(XY) = \mathbb{V}(X)\,\mathbb{V}(Y) + \mathbb{V}(X)\,\mathbb{E}[Y]^2 + \mathbb{V}(Y)\,\mathbb{E}[X]^2$.
4. Montre que $\mathbb{V}(XY) \ge \mathbb{V}(X)\,\mathbb{V}(Y)$, et dis exactement quand il y a égalité.
5. Si $\mathbb{E}[X] \ne 0$ et $\mathbb{E}[Y] \ne 0$, montre que $1 + c_{XY}^2 = (1 + c_X^2)(1 + c_Y^2)$, où $c_Z = \frac{\sigma_Z}{\lvert\mathbb{E}[Z]\rvert}$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M16.10 — Pont : n points rangés en lignes, X W + 1bᵀ, et la diffusion de b 🔗 ★ ⏱️ 15 min
**Objectif :** appliquer une application affine à plusieurs points d'un seul produit, avec le terme $\mathbf{1}\mathbf{b}^\top$, puis en coordonnées homogènes.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

$\mathbf{W} = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 3 & 1 \end{pmatrix}$, $\mathbf{b} = (1, 0, -2)$, et quatre points rangés en lignes dans $\mathbf{X} = \begin{pmatrix} 1 & 1 \\ 0 & 2 \\ -1 & 1 \\ 2 & 0 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{X}\mathbf{W} + \mathbf{1}\mathbf{b}^\top$ | une liste de 2 entiers |
| b | la matrice $\mathbf{1}\mathbf{b}^\top$ | une matrice (liste de lignes) |
| c | $\mathbf{X}\mathbf{W} + \mathbf{1}\mathbf{b}^\top$ | une matrice (liste de lignes) |
| d | la matrice homogène $\mathbf{H}$ de $\mathbf{x} \mapsto \mathbf{x}\mathbf{W} + \mathbf{b}$ | une matrice (liste de lignes) |
| e | le produit $[\mathbf{X} \mid \mathbf{1}]\,\mathbf{H}$, où $[\mathbf{X} \mid \mathbf{1}]$ ajoute une colonne de uns à $\mathbf{X}$ | une matrice (liste de lignes) |
| f | le nombre de multiplications de $\mathbf{X}\mathbf{W}$ | un entier |

Dans ta copie : pourquoi $\mathbf{1}\mathbf{b}^\top$ est-elle une matrice $4 \times 3$, et que fait NumPy à la place quand on écrit `X @ W + b` ? Que devient c) si l'on ajoute un cinquième point : quelles lignes changent ? Que montre e) ?

### Ex M16.11 — Expliquer, sur un exemple, pourquoi la variance d'un produit n'est pas le produit des variances 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule ce que la variance d'un produit doit aux moyennes des facteurs.
**Prérequis :** fiche §5 · **Parcours :** C, E

Un ami calcule la variance de la surface d'un champ rectangulaire dont la longueur et la largeur sont mesurées avec de petites erreurs indépendantes : « la variance de la longueur fois la variance de la largeur, c'est minuscule, donc la surface est connue presque exactement ». Réponds-lui en 6 à 10 phrases, sans formule, en t'appuyant sur trois idées : ce que devient une petite erreur sur la longueur quand on la multiplie par une largeur de plusieurs dizaines de mètres ; le cas où l'une des deux mesures est exacte ; le seul cas où son calcul est juste. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M16.E1 — « Pourquoi l'écart-type d'une somme de n termes indépendants grandit-il comme √n ? » 💼 ★ ⏱️ 10 min
*Fiche §6 et §7 · parcours C*

« Pourquoi l'écart-type d'une somme de $n$ termes indépendants grandit-il comme $\sqrt{n}$ ? »

Prépare une réponse orale de **60 secondes**. Elle doit dire ce qui s'additionne (les variances, grâce aux covariances nulles) et ce qui ne s'additionne pas (les écarts-types), ce que change une corrélation entre les termes (jusqu'à une croissance en $n$), le cas de termes multipliés par des signes aléatoires indépendants, la conséquence pour la moyenne de $n$ termes (un écart-type en $\frac{1}{\sqrt{n}}$), et ce que cela implique quand on additionne beaucoup de contributions aléatoires : pour garder une échelle donnée, il faut réduire chaque contribution. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m16_couches_affines/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M16.12 | La matrice homogène d'une application affine · `homogeneous_matrix` | 🔨 | ★ | 15 | C, E |
| M16.13 | Sommer sur les chemins d'un graphe sans cycle par les puissances de sa matrice · `sum_over_paths` | 🔨 | ★★ | 20 | C, E |
| M16.14 | Espérance et variance d'un produit de variables indépendantes · `variance_of_product` | 🔨 | ★ | 15 | C |
| M16.15 | Prédire l'écart-type d'une somme de produits aléatoires, mesures corrélées ou non, puis simuler | 🔮 | ★ | 10 | C, E |
| M16.16 | Une variance multipliée d'étage en étage : simuler une chaîne d'amplificateurs bruités | 🔬 | ★★ | 20 | C |
| M16.17 | L'image d'une figure par une suite d'applications affines du plan, en coordonnées homogènes | 🎨 | ★ | 15 | C, E |
| M16.18 | Chasse à l'erreur : une matrice homogène écrite pour des colonnes et appliquée à des lignes, Var(XY) = Var X · Var Y, et (I − A)⁻¹ sur un graphe qui a un cycle | 🐛 | ★ | 15 | C, E |
| M16.19 | Un test de propriété : la matrice homogène d'une composée est le produit des matrices homogènes | 🛠️ | ★ | 15 | C |
| M16.20 | Défi : la loi du produit de deux uniformes indépendantes, sa densité et ses deux premiers moments | 🏆 | ★★★ | 25 | C |
