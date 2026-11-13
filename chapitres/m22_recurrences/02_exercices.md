# M22 · Récurrences vectorielles, rayon spectral et normes de matrices — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m22_recurrences/06_mes_reponses.md` (créée par `python tools/start_chapter.py M22`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les états sont des **colonnes**, $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t$, et les pas de temps sont numérotés à partir de 0 ($\mathbf{x}_0$ est l'état de départ, $\mathbf{u}_t$ l'entrée reçue au pas $t$, qui sert à calculer $\mathbf{x}_{t+1}$). La réponse impulsionnelle est $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$, et, pour $\mathbf{x}_0 = \mathbf{0}$, la sortie vérifie $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$. $\rho(\mathbf{A})$ est le rayon spectral ; $\lVert\mathbf{A}\rVert_1$, $\lVert\mathbf{A}\rVert_2 = s_{\max}(\mathbf{A})$ et $\lVert\mathbf{A}\rVert_\infty$ sont les normes induites par les normes L1, L2 et L∞ des vecteurs, et $\lVert\mathbf{A}\rVert_F$ la norme de Frobenius. Un produit de matrices s'écrit $\mathbf{P}_t = \mathbf{A}_t\cdots\mathbf{A}_1$, la matrice du dernier pas à gauche. Une jacobienne a une ligne par coordonnée de sortie (M17). $\ln$ est le logarithme népérien, $i$ le nombre complexe de carré $-1$, et l'argument d'un complexe est pris dans $]-\pi, \pi]$ sauf mention. Une matrice s'écrit dans le notebook comme une liste de ses **lignes**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M22.Q1 — La solution d'une récurrence avec entrée : quelles puissances, quels termes ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Une récurrence $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t$, avec $\mathbf{A}$ de forme $(4, 4)$ et $\mathbf{B}$ de forme $(4, 2)$.

1. Dans la formule de $\mathbf{x}_5$, quelle puissance de $\mathbf{A}$ multiplie $\mathbf{B}\mathbf{u}_2$ ?
2. Combien de termes a la réponse forcée de $\mathbf{x}_6$, et quelles entrées y figurent ?
3. Vrai ou faux : l'entrée $\mathbf{u}_5$ intervient dans $\mathbf{x}_5$.
4. $\mathbf{x}_0 = \mathbf{0}$, et toutes les entrées sont nulles sauf $\mathbf{u}_3$. Écris $\mathbf{x}_7$.
5. Quelle forme a $\mathbf{u}_t$ ? Et $\mathbf{A}\mathbf{B}$ ? Le produit $\mathbf{B}\mathbf{A}$ est-il défini ?
6. Avec une seule entrée ($m = 1$), une sortie $y_t = \mathbf{C}\mathbf{x}_t$ et $\mathbf{x}_0 = \mathbf{0}$ : écris $y_4$ avec la réponse impulsionnelle $h_k$ et les entrées $u_k$.

### M22.Q2 — Valeurs propres complexes, module, forme exponentielle et rotation : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. Vrai ou faux : $e^{i\pi/2}\,e^{i\pi/3} = e^{i5\pi/6}$.
2. Le module et l'argument de $-3 + 3i$ ?
3. $(-3 + 3i)^2$, par son module et son argument, puis sous la forme $a + ib$ ?
4. Vrai ou faux : une matrice réelle $2 \times 2$ de trace 1 et de déterminant 4 a deux valeurs propres complexes conjuguées de module 2.
5. Les valeurs propres de $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ ? Que vaut sa puissance 4 ?
6. Vrai ou faux : une matrice réelle $2 \times 2$ de trace $0{,}8$ et de déterminant $1{,}21$ a des trajectoires qui s'éteignent, parce que la partie réelle de ses valeurs propres vaut $0{,}4$.

### M22.Q3 — Le rayon spectral décide-t-il de tout ? Le long terme et les premiers pas 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Le rayon spectral de $\begin{pmatrix} 0{,}3 & 2 \\ 0 & -0{,}6 \end{pmatrix}$ ?
2. Vrai ou faux : si $\rho(\mathbf{A}) < 1$, alors $\lVert\mathbf{A}\mathbf{x}\rVert_2 \le \lVert\mathbf{x}\rVert_2$ pour tout $\mathbf{x}$.
3. Vrai ou faux : si $\rho(\mathbf{A}) < 1$, alors $\mathbf{A}^t\mathbf{x} \to \mathbf{0}$ pour tout $\mathbf{x}$.
4. Vrai ou faux : si $\rho(\mathbf{A}) = 1{,}02$, alors $\lVert\mathbf{A}^t\rVert_2 \to +\infty$.
5. $\rho(\mathbf{A}) = 1$ : les puissances de $\mathbf{A}$ restent-elles bornées ? Donne un exemple de chaque cas.
6. Vrai ou faux : pour une matrice **normale** de rayon spectral $0{,}6$, $\lVert\mathbf{A}^t\rVert_2 = 0{,}6^t$ pour tout $t$.

### M22.Q4 — Normes induites : laquelle se calcule à la main, laquelle borne quoi ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 2 & -5 & 1 \\ -3 & 0 & 4 \end{pmatrix}$.

1. $\lVert\mathbf{A}\rVert_1$ et $\lVert\mathbf{A}\rVert_\infty$ ?
2. Laquelle des trois normes induites demande une valeur propre, et de quelle matrice ?
3. Vrai ou faux : $\lVert\mathbf{M}\mathbf{x}\rVert_2 \le \lVert\mathbf{M}\rVert_\infty\,\lVert\mathbf{x}\rVert_2$ pour toute matrice $\mathbf{M}$ et tout $\mathbf{x}$.
4. $\lVert\mathbf{I}_5\rVert_1$, $\lVert\mathbf{I}_5\rVert_2$ et $\lVert\mathbf{I}_5\rVert_F$ ?
5. Vrai ou faux : $\lVert\mathbf{M}^7\rVert_1 \le \lVert\mathbf{M}\rVert_1^7$ pour toute matrice carrée $\mathbf{M}$.
6. $\lVert\operatorname{diag}(0{,}4 ;\ -1{,}5 ;\ 1{,}2)\rVert_2$ ?
7. Vrai ou faux : $\lVert\mathbf{M}^\top\rVert_1 = \lVert\mathbf{M}\rVert_1$ pour toute matrice $\mathbf{M}$.

### M22.Q5 — Un produit de facteurs dans [0, 1] : ce qui reste après n étapes 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Un silo perd chaque mois 4 % du grain qu'il contient ($\varepsilon = 0{,}04$) ; ici, $n$ compte les mois.

1. La fraction du grain qui reste après $n = 12$ mois ? Et son approximation $e^{-n\varepsilon}$ ?
2. Vrai ou faux : $e^{-n\varepsilon}$ surestime toujours ce qui reste.
3. La demi-vie approchée $\frac{\ln 2}{\varepsilon}$, puis la demi-vie exacte, en mois ?
4. Si la fraction perdue chaque mois change d'un mois à l'autre, en restant entre 0 % et 100 % exclus : ce qui reste peut-il augmenter d'un mois à l'autre ? Son logarithme est une somme de quels termes ?
5. Une autre quantité est multipliée chaque année, à pile ou face, par $1{,}8$ ou par $0{,}4$. $\mathbb{E}[a]$ ? $\mathbb{E}[\ln a]$ ? Grandit-elle pour une trajectoire typique ?
6. $\operatorname{diag}(0{,}6 ;\ 0{,}97)^3$ ?

### M22.Q6 — Contraction et point fixe : lire une jacobienne 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. En un point fixe $\mathbf{x}^\star$ d'une application $f$ du plan, $\mathbf{J}_f(\mathbf{x}^\star) = \begin{pmatrix} 0{,}3 & 1{,}2 \\ 0 & 0{,}6 \end{pmatrix}$. Le point fixe est-il attractif ? La jacobienne raccourcit-elle tous les vecteurs, en norme 2 ?
2. En un autre point fixe, la jacobienne a pour valeurs propres $0{,}3$ et $-1{,}4$. Ce point fixe est-il attractif, instable, répulsif ?
3. $f$ est contractante de facteur $q = 0{,}6$ sur une partie qu'elle envoie dans elle-même. Deux trajectoires y partent à distance 5 l'une de l'autre : leur distance après 4 pas, au plus ?
4. Vrai ou faux : une application contractante a au plus un point fixe.
5. $\frac{\partial\mathbf{x}_4}{\partial\mathbf{x}_1}$ pour $\mathbf{x}_{t+1} = f(\mathbf{x}_t)$ : quelles jacobiennes, dans quel ordre ?
6. Vrai ou faux : si $\lVert\mathbf{J}_f(\mathbf{x})\rVert_\infty \le 0{,}6$ en tout point d'une partie convexe que $f$ envoie dans elle-même, $f$ y est contractante de facteur $0{,}6$ pour $\lVert\cdot\rVert_\infty$.

### M22.Q7 — Une somme sur le temps, sur un modèle de pêche chiffré : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

Un lac est pêché et repeuplé chaque année : le stock $x_t$ (en milliers de poissons) grandit de 40 % par la reproduction, la pêche en prélève la fraction $\beta$, et l'on relâche 20 000 alevins, d'où $x_{t+1} = 1{,}4\,(1 - \beta)\,x_t + 20$. Avec $\beta = 0{,}4$ et $x_0 = 50$ : $x_1 = 62$, $x_2 = 72{,}08$, $J_t = \frac{\partial f}{\partial x} = 0{,}84$ à chaque pas, $b_t = \frac{\partial f}{\partial\beta} = -1{,}4\,x_t$, et la sensibilité $s_3 = \frac{\partial x_3}{\partial\beta} = -223{,}216$. Vrai ou faux :

1. $s_3$ est une somme de trois termes, un par année où le taux de pêche a servi.
2. Le terme de l'année 0 vaut $J_0J_1J_2\,b_0$.
3. $J_t$ est le même chaque année parce que $f$ est affine en $x$.
4. Ne garder que le dernier terme, $b_2$, donne $s_3$.
5. Passer de $\beta = 0{,}40$ à $\beta = 0{,}41$ change $x_3$ d'environ $-2{,}23$ milliers de poissons.
6. On obtient aussi $s_3$ pas à pas : $s_1 = b_0$, $s_2 = J_1s_1 + b_1$, $s_3 = J_2s_2 + b_2$.

### M22.Q8 — Ramener un vecteur sous un seuil : le tout ou chaque bloc ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

Un vecteur $\mathbf{w}$ est fait de trois blocs, de normes (L2) 1, 4 et 8.

1. La norme globale de $\mathbf{w}$ ?
2. On ramène le tout sous $c = 2{,}7$ : par quel nombre multiplie-t-on chaque bloc ?
3. On ramène plutôt chaque bloc sous $c = 2{,}7$ : les normes des trois blocs après coup, puis la norme globale ?
4. Vrai ou faux : ramener chaque bloc sous $c$ garde toujours la direction de $\mathbf{w}$.
5. Pour $p = 25$ blocs, quel seuil par bloc garantit une norme globale au plus égale à $c$ ?
6. Vrai ou faux : si la norme globale vaut 2, ramener le tout sous $c = 2{,}7$ ne change rien.

<a id="rappels"></a>

## 🔁 Rappels

### M22.R1 — La diagonalisation et les puissances d'une matrice (M12c) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 5 & 2 \\ 1 & 4 \end{pmatrix}$.

1. Ses valeurs propres ?
2. Un vecteur propre pour chacune ?
3. $\mathbf{A}^t$ en formule, par $\mathbf{A} = \mathbf{V}\mathbf{D}\mathbf{V}^{-1}$ ?
4. $\mathbf{A}^3$ ?
5. Vrai ou faux : $\mathbf{A}^t/6^t$ tend vers une matrice de rang 1.

### M22.R2 — Valeurs singulières et norme spectrale (M12d) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 3 & 3 \\ -1 & 1 \end{pmatrix}$.

1. $\mathbf{A}^\top\mathbf{A}$ ?
2. Ses valeurs propres ?
3. Les valeurs singulières $s_{\max}$ et $s_{\min}$ de $\mathbf{A}$ ?
4. Un vecteur unitaire $\mathbf{x}$ qui rend $\lVert\mathbf{A}\mathbf{x}\rVert_2$ le plus grand possible, et $\mathbf{A}\mathbf{x}$ ?
5. $\lVert\mathbf{A}\rVert_F$, et son lien avec les valeurs singulières ?
6. Le conditionnement $\kappa(\mathbf{A}) = s_{\max}/s_{\min}$ ?

### M22.R3 — La règle de la chaîne comme produit de jacobiennes (M17) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

$g(x, y) = (xy,\ x + y)$ et $f(u, v) = (u^2,\ u - v)$, toutes deux de $\mathbb{R}^2$ dans $\mathbb{R}^2$.

1. $g(-1, 4)$ et $\mathbf{J}_g(-1, 4)$ ?
2. $\mathbf{J}_f$ au point $g(-1, 4)$ ?
3. $\mathbf{J}_{f \circ g}(-1, 4)$ : quel produit, et sa valeur ?
4. Vrai ou faux : $\mathbf{J}_g(-1, 4)\,\mathbf{J}_f\big(g(-1, 4)\big)$ donne la même matrice.
5. Au premier ordre, de combien change $f \circ g$ quand $x$ passe de $-1$ à $-0{,}99$ ($y = 4$ fixé) ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- un nombre complexe $a + ib$ comme la liste `[a, b]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- un angle exact en radians entre guillemets, comme `"pi/4"` ;
- une forme comme NumPy l'affiche, comme `(7, 2)` ;
- `True` ou `False` pour un vrai ou faux.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M22.1 — Une population à trois classes d'âge, avec des arrivées : trois pas à la main, et la solution écrite avec les puissances ✏️ ★★ ⏱️ 20 min
**Objectif :** dérouler une récurrence linéaire avec entrée, puis retrouver le résultat par la formule de la solution, réponse libre et réponse forcée.
**Prérequis :** fiche §1 ; M09a · **Parcours :** C, E

Une espèce d'oiseau vit au plus trois ans. Chaque printemps, on compte sa population dans une réserve en trois classes : $\mathbf{x}_t = (\text{jeunes de l'année},\ \text{oiseaux d'un an},\ \text{oiseaux de deux ans})$. D'un printemps au suivant, un oiseau d'un an donne en moyenne 1,2 jeune et un oiseau de deux ans 0,8 jeune ; 40 % des jeunes atteignent un an, 60 % des oiseaux d'un an atteignent deux ans, et les oiseaux de deux ans meurent. Un centre d'élevage relâche aussi, pendant l'année $t$, $j_t$ jeunes et $a_t$ oiseaux de deux ans, comptés au printemps suivant : l'entrée est $\mathbf{u}_t = (j_t, a_t)$. Donc
$$\mathbf{x}_{t+1} = \underbrace{\begin{pmatrix} 0 & 1{,}2 & 0{,}8 \\ 0{,}4 & 0 & 0 \\ 0 & 0{,}6 & 0 \end{pmatrix}}_{\mathbf{A}}\mathbf{x}_t + \underbrace{\begin{pmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{pmatrix}}_{\mathbf{B}}\mathbf{u}_t,$$
avec $\mathbf{x}_0 = (40, 20, 30)$, $\mathbf{u}_0 = (20, 10)$, $\mathbf{u}_1 = (0, 10)$ et $\mathbf{u}_2 = (30, 0)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{x}_1$ | une liste de 3 nombres |
| b | $\mathbf{x}_2$ | une liste de 3 nombres |
| c | $\mathbf{x}_3$ | une liste de 3 nombres |
| d | la matrice $\mathbf{A}^2\mathbf{B}$, qui multiplie $\mathbf{u}_0$ dans $\mathbf{x}_3$ | une matrice $3 \times 2$ |
| e | la réponse libre $\mathbf{A}^3\mathbf{x}_0$ | une liste de 3 nombres |
| f | la réponse forcée de $\mathbf{x}_3$ (la part due aux lâchers) | une liste de 3 nombres |
| g | le nombre de termes de la réponse forcée de $\mathbf{x}_{10}$ | un entier |
| h | vrai ou faux : le produit $\mathbf{B}\mathbf{A}$ est défini | `True` ou `False` |

Dans ta copie : écris la formule $\mathbf{x}_3 = \mathbf{A}^3\mathbf{x}_0 + \mathbf{A}^2\mathbf{B}\mathbf{u}_0 + \mathbf{A}\mathbf{B}\mathbf{u}_1 + \mathbf{B}\mathbf{u}_2$ et vérifie que e) + f) redonne c). Pourquoi $\mathbf{u}_2$ n'est-il multiplié par aucune puissance de $\mathbf{A}$ ? Que dit la première colonne de d) sur le devenir, deux ans plus tard, de 1 jeune relâché ? Calcule la population totale au printemps 3.

### Ex M22.2 — La réponse impulsionnelle de deux réservoirs en cascade, et la sortie comme convolution de l'entrée ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une réponse impulsionnelle, la sortie par une convolution, et ce que devient toute la pluie reçue.
**Prérequis :** fiche §1 et §2 ; M21, R5 · **Parcours :** C, E

Deux bassins de rétention en cascade recueillent la pluie d'un parking. Chaque jour, le bassin 1 garde 40 % de son eau, en verse 40 % dans le bassin 2 et perd le reste par infiltration ; le bassin 2 garde 30 % de son eau, en rejette 60 % à la rivière et perd le reste. La pluie $u_t$ du jour $t$ tombe dans le bassin 1. L'état est $\mathbf{x}_t = (\text{niveau du bassin 1},\ \text{niveau du bassin 2})$, en millimètres, et la sortie $y_t = 0{,}6 \times (\text{niveau du bassin 2})$ est le rejet à la rivière du jour $t$ :
$$\mathbf{A} = \begin{pmatrix} 0{,}4 & 0 \\ 0{,}4 & 0{,}3 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \mathbf{C} = \begin{pmatrix} 0 & 0{,}6 \end{pmatrix}, \qquad \mathbf{x}_0 = \mathbf{0}$$
(sauf au f). Les pluies sont $\mathbf{u} = (10, 0, 20, 5)$ mm les jours 0 à 3, puis nulles.

| | Question | Réponse attendue |
|---|---|---|
| a | la réponse impulsionnelle $h_0, h_1, h_2, h_3, h_4$ | une liste de 5 nombres (4 décimales) |
| b | les rejets $y_1, \ldots, y_5$, par la convolution $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$ | une liste de 5 nombres (4 décimales) |
| c | $\mathbf{x}_3$, en déroulant la récurrence | une liste de 2 nombres |
| d | le premier jour $t$ où la pluie du jour 3 apparaît dans le rejet $y_t$ | un entier |
| e | la fraction de la pluie qui finit à la rivière, $\sum_{k \ge 0} h_k$ | une fraction irréductible, entre guillemets |
| f | le bassin 2 contenait 10 mm au départ, $\mathbf{x}_0 = (0, 10)$, et les pluies sont les mêmes : de combien ce départ change-t-il $y_4$ ? | un nombre (4 décimales) |
| g | vrai ou faux : avec $\mathbf{x}_0 = \mathbf{0}$, une pluie deux fois plus forte chaque jour double chaque rejet | `True` ou `False` |

Dans ta copie : trouve les valeurs propres de $\mathbf{A}$, puis une formule de $h_k$ (les puissances d'une matrice triangulaire, fiche §2), et déduis-en e) par deux séries géométriques. Vérifie e) par $\mathbf{C}(\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}$. Pourquoi $h_0 = 0$ ? Vérifie $y_3$ à partir de c). Que dit f) sur la mémoire du système ?

### Ex M22.3 — Une matrice de rotation et d'homothétie : valeurs propres complexes, forme exponentielle, puissances ✏️ ★★ ⏱️ 20 min
**Objectif :** lire une matrice $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ comme la multiplication par un complexe, et en déduire ses puissances.
**Prérequis :** fiche §2 ; M12c §3, M19 §6 · **Parcours :** C, E

Un point du plan est déplacé à chaque pas par
$$\mathbf{M} = \begin{pmatrix} -0{,}3 & -0{,}3\sqrt3 \\ 0{,}3\sqrt3 & -0{,}3 \end{pmatrix}, \qquad \mathbf{x}_{t+1} = \mathbf{M}\mathbf{x}_t, \qquad \mathbf{x}_0 = (2, 0).$$
On note $\mu$ la valeur propre de $\mathbf{M}$ de partie imaginaire positive.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mu$, comme `[a, b]` pour $a + ib$ | une liste de 2 nombres (4 décimales) |
| b | son module $r$ | un nombre |
| c | son argument $\theta$ | un angle exact, entre guillemets |
| d | $\mathbf{M}^3$ | une matrice (4 décimales) |
| e | $\mu^4$, comme `[a, b]` | une liste de 2 nombres (4 décimales) |
| f | la distance de $\mathbf{x}_5$ à l'origine | un nombre (5 décimales) |
| g | l'angle que fait $\mathbf{x}_5$ avec l'axe des abscisses, pris dans $[0, 2\pi[$ | un angle exact, entre guillemets |
| h | vrai ou faux : $\mathbf{M}$ est orthogonale | `True` ou `False` |
| i | vrai ou faux : $\mathbf{M}$ est normale | `True` ou `False` |

Dans ta copie : écris le polynôme caractéristique de $\mathbf{M}$, puis $\mathbf{M} = r\,\mathbf{R}_\theta$. Pourquoi $\mathbf{M}^3$ est-il un multiple de $\mathbf{I}$ ? Combien de pas faut-il pour faire un tour ? Exprime $\mathbf{x}_5$ à l'aide de $\mathbf{x}_2$. Décris la trajectoire en une phrase.

### Ex M22.4 — Le rayon spectral de trois matrices 2 × 2 non symétriques, et le comportement de leurs puissances ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer le rayon spectral de matrices non symétriques, valeurs propres complexes comprises, et en déduire le comportement de leurs puissances.
**Prérequis :** fiche §2 et §3 · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 0{,}2 & 0{,}4 \\ 0{,}6 & 0 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 2 & -3 \\ 1 & -1 \end{pmatrix}, \qquad \mathbf{C} = \begin{pmatrix} 0 & -1 \\ 1{,}69 & 0 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\rho(\mathbf{A})$ | un nombre |
| b | $\rho(\mathbf{B})$ | un nombre |
| c | $\rho(\mathbf{C})$ | un nombre |
| d | $\mathbf{B}^3$ | une matrice |
| e | le plus petit nombre de pas $t \ge 1$ tel que $\mathbf{B}^t = \mathbf{I}$ | un entier |
| f | $\mathbf{C}^4$ | une matrice (4 décimales) |
| g | le comportement des puissances de $\mathbf{A}$, de $\mathbf{B}$ et de $\mathbf{C}$, dans cet ordre, codé 1 (elles tendent vers $\mathbf{0}$), 2 (elles restent bornées sans tendre vers $\mathbf{0}$) ou 3 (elles ne sont pas bornées) | une liste de 3 entiers |
| h | vrai ou faux : comme $\lVert\mathbf{B}\rVert_\infty = 5 > 1$, les puissances de $\mathbf{B}$ ne sont pas bornées | `True` ou `False` |

Dans ta copie : les valeurs propres de chaque matrice, par la trace et le déterminant ; pour $\mathbf{B}$, leur forme exponentielle. Calcule $\mathbf{B}^2$ puis $\mathbf{B}^3$. Pour $\mathbf{C}$, calcule $\mathbf{C}^2$ et décris ce que fait $\mathbf{C}$ à chaque pas. Pour $\mathbf{A}$, que devient $\mathbf{A}^t\mathbf{x}$ quand $t$ grandit : quelle composante s'éteint le plus vite, et laquelle change de signe à chaque pas ?

### Ex M22.5 — Une matrice triangulaire de rayon spectral < 1 dont les puissances grandissent d'abord : Aᵗ en formule ✏️ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule des puissances d'une matrice triangulaire $2 \times 2$, et suivre la croissance transitoire qu'elle produit.
**Prérequis :** fiche §3 ; R4, R5 · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} \frac23 & 3 \\ 0 & \frac23 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} \frac23 & 3 \\ 0 & \frac13 \end{pmatrix}.$$
On note $c_t = (\mathbf{A}^t)_{12}$, le coefficient en haut à droite de $\mathbf{A}^t$.

**Dans ta copie, d'abord.** Pour $\mathbf{T} = \begin{pmatrix} \lambda_1 & \gamma \\ 0 & \lambda_2 \end{pmatrix}$, montre par récurrence sur $t \ge 1$ que $\mathbf{T}^t = \begin{pmatrix} \lambda_1^t & \gamma\,\sigma_t \\ 0 & \lambda_2^t \end{pmatrix}$ avec $\sigma_t = \sum_{j=0}^{t-1}\lambda_1^{t-1-j}\lambda_2^{\,j}$. Déduis-en $\sigma_t = \frac{\lambda_1^t - \lambda_2^t}{\lambda_1 - \lambda_2}$ si $\lambda_1 \ne \lambda_2$, et $\sigma_t = t\,\lambda^{t-1}$ si $\lambda_1 = \lambda_2 = \lambda$. Écris $c_t$ pour la matrice $\mathbf{A}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\rho(\mathbf{A})$ | une fraction irréductible, entre guillemets |
| b | $c_1, c_2, c_3, c_4, c_5$ | une liste de 5 nombres (4 décimales) |
| c | les pas $t$ où $c_t$ est le plus grand, en ordre croissant | une liste d'entiers |
| d | $c_{15}$ | un nombre (4 décimales) |
| e | le plus petit pas $t$ tel que $c_t < 1$ | un entier |
| f | $\mathbf{A}^3\mathbf{e}_2$, avec $\mathbf{e}_2 = (0, 1)$ | une liste de 2 nombres (4 décimales) |
| g | $(\mathbf{B}^t)_{12}$ pour $t = 1, 2, 3$ | une liste de 3 nombres (4 décimales) |
| h | vrai ou faux : $\mathbf{A}$ est normale | `True` ou `False` |

Dans ta copie : pour c), étudie le rapport $\frac{c_{t+1}}{c_t}$ et dis pour quels $t$ il dépasse 1. Compare $\mathbf{A}$ à $\operatorname{diag}(\frac23, \frac23)$, de mêmes valeurs propres, et $\mathbf{A}$ à $\mathbf{B}$ : laquelle grandit le plus longtemps, et pourquoi ? Vérifie $\mathbf{A}^2$ par un produit.

### Ex M22.6 — Les normes ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice 2 × 2, et trois majorations de ‖A⁵x‖ ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer les trois normes induites, et majorer une puissance appliquée à un vecteur sans calculer la puissance.
**Prérequis :** fiche §4 ; M07, M12d · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 1 & 2 \\ -1 & 2 \end{pmatrix}, \qquad \mathbf{x} = (2, -3).$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert\mathbf{A}\rVert_1$ | un nombre |
| b | $\lVert\mathbf{A}\rVert_\infty$ | un nombre |
| c | $\mathbf{A}^\top\mathbf{A}$ | une matrice |
| d | $\lVert\mathbf{A}\rVert_2$ | un nombre (4 décimales) |
| e | $\rho(\mathbf{A})$ | un nombre |
| f | $\mathbf{A}^5\mathbf{x}$, par cinq produits successifs | une liste de 2 entiers |
| g | les trois majorations $\lVert\mathbf{A}\rVert_p^5\,\lVert\mathbf{x}\rVert_p$, pour $p = 1$, $2$ et $\infty$, dans cet ordre | une liste de 3 nombres (2 décimales) |
| h | les trois normes $\lVert\mathbf{A}^5\mathbf{x}\rVert_p$, pour $p = 1$, $2$ et $\infty$, dans cet ordre | une liste de 3 nombres (2 décimales) |
| i | vrai ou faux : $\rho(\mathbf{A})^5\,\lVert\mathbf{x}\rVert_2 \ge \lVert\mathbf{A}^5\mathbf{x}\rVert_2$ | `True` ou `False` |

Dans ta copie : un vecteur où $\lVert\mathbf{A}\rVert_1$, puis $\lVert\mathbf{A}\rVert_2$, sont atteintes. Pour chaque $p$, le rapport de la majoration g) à la vraie norme h). Ramène les trois majorations à une majoration de $\lVert\mathbf{A}^5\mathbf{x}\rVert_2$, avec $\lVert\mathbf{y}\rVert_2 \le \lVert\mathbf{y}\rVert_1$ et $\lVert\mathbf{y}\rVert_2 \le \sqrt2\,\lVert\mathbf{y}\rVert_\infty$ pour $\mathbf{y} \in \mathbb{R}^2$ : laquelle est la meilleure ici ? Que montre i) ?

### Ex M22.7 — Trois équipements qui s'usent à des rythmes différents : une récurrence diagonale, ce qui reste, et la demi-vie ✏️ ★ ⏱️ 15 min
**Objectif :** suivre une récurrence diagonale à facteurs dans [0, 1], comparer ce qui reste à son approximation exponentielle, et calculer des demi-vies.
**Prérequis :** fiche §5 ; R5, R6 · **Parcours :** C, E

Un atelier suit chaque mois la capacité de trois équipements, en fraction de leur capacité neuve : une meule perd 1,5 % de sa capacité par mois, une lame de scie 7 %, un filtre à huile 35 %. Sans entretien, $\mathbf{x}_t = \mathbf{a} \odot \mathbf{x}_{t-1}$, avec $\mathbf{a} = (0{,}985 ;\ 0{,}93 ;\ 0{,}65)$ ; ici, $n$ compte les mois.

| | Question | Réponse attendue |
|---|---|---|
| a | ce qui reste de chaque capacité après $n = 12$ mois sans entretien | une liste de 3 nombres (4 décimales) |
| b | les approximations $e^{-n\varepsilon}$ de ces trois nombres | une liste de 3 nombres (4 décimales) |
| c | les demi-vies exactes, en mois | une liste de 3 nombres (2 décimales) |
| d | les demi-vies approchées $\frac{\ln 2}{\varepsilon}$, en mois | une liste de 3 nombres (2 décimales) |

L'atelier entretient maintenant ses équipements : chaque mois, l'entretien rend $\mathbf{b} = (0{,}012 ;\ 0{,}056 ;\ 0{,}28)$, et $\mathbf{x}_t = \mathbf{a} \odot \mathbf{x}_{t-1} + \mathbf{b}$, à partir d'équipements neufs, $\mathbf{x}_0 = (1, 1, 1)$.

| | Question | Réponse attendue |
|---|---|---|
| e | $\mathbf{x}_2$ | une liste de 3 nombres (4 décimales) |
| f | l'état d'équilibre $\mathbf{x}^\star$ | une liste de 3 nombres |
| g | vrai ou faux : pour chacun des trois équipements, $e^{-n\varepsilon}$ est juste à 1 % près (en valeur relative) après 12 mois | `True` ou `False` |

Dans ta copie : écris la récurrence avec $\operatorname{diag}(\mathbf{a})$, et dis pourquoi chaque capacité évolue seule. Calcule le rapport de b) à a) pour chaque équipement : pourquoi l'approximation se dégrade-t-elle avec $\varepsilon$ ? Montre que $\mathbf{x}_t - \mathbf{x}^\star = \mathbf{a}^t \odot (\mathbf{x}_0 - \mathbf{x}^\star)$ (les puissances coordonnée par coordonnée) : lequel des trois équipements oublie le plus lentement qu'il était neuf ?

### Ex M22.8 — Les jacobiennes d'une application du plan en trois points d'une trajectoire, et leur produit ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer le produit des jacobiennes le long d'une trajectoire, dans le bon ordre, et le comparer au produit de leurs normes.
**Prérequis :** fiche §6 ; M17 · **Parcours :** C, E

L'application de Hénon, un modèle classique de dynamique dans le plan :
$$f(x, y) = (1 - 1{,}4\,x^2 + y,\ \ 0{,}3\,x), \qquad \mathbf{x}_{t+1} = f(\mathbf{x}_t), \qquad \mathbf{x}_0 = (0, 0).$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{x}_3$ | une liste de 2 nombres |
| b | $\mathbf{J}_f(\mathbf{x}_1)$ | une matrice |
| c | $\mathbf{J}_f(\mathbf{x}_2)$ | une matrice |
| d | $\frac{\partial\mathbf{x}_3}{\partial\mathbf{x}_0}$ | une matrice |
| e | le déterminant de d) | un nombre |
| f | $\lVert\mathbf{J}_f(\mathbf{x}_0)\rVert_\infty$, $\lVert\mathbf{J}_f(\mathbf{x}_1)\rVert_\infty$, $\lVert\mathbf{J}_f(\mathbf{x}_2)\rVert_\infty$, puis $\big\lVert\frac{\partial\mathbf{x}_3}{\partial\mathbf{x}_0}\big\rVert_\infty$ | une liste de 4 nombres |
| g | au premier ordre, le déplacement de $\mathbf{x}_3$ quand $\mathbf{x}_0$ passe de $(0, 0)$ à $(0{,}01 ;\ 0)$ | une liste de 2 nombres (5 décimales) |
| h | vrai ou faux : $\mathbf{J}_f(\mathbf{x}_0)\,\mathbf{J}_f(\mathbf{x}_1)\,\mathbf{J}_f(\mathbf{x}_2)$ donne la même matrice que d) | `True` ou `False` |

Dans ta copie : écris $\mathbf{J}_f(x, y)$. Pourquoi son déterminant vaut-il $-0{,}3$ en tout point, et que vaut alors e), sans calcul ? Compare le produit des trois normes de f) à la norme de d). Calcule le vrai $\mathbf{x}_3$ partant de $(0{,}01 ;\ 0)$ et compare son déplacement à g).

### Ex M22.9 — Un capital placé à taux fixe avec des versements : la dérivée du capital final par rapport au taux, une somme sur les années ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire la sensibilité d'un état final à un paramètre utilisé à chaque pas comme une somme sur le temps, et la vérifier.
**Prérequis :** fiche §7 ; R5, M17 · **Parcours :** C, E

Tu places $x_0 = 2\,000$ € au taux annuel fixe $\beta = 3\,\%$, et tu verses 600 € à la fin de chaque année :
$$x_{t+1} = f(x_t, \beta) = (1 + \beta)\,x_t + 600 .$$
On note $s_t = \frac{\partial x_t}{\partial\beta}$, $J_t = \frac{\partial f}{\partial x}(x_t, \beta)$ et $b_t = \frac{\partial f}{\partial\beta}(x_t, \beta)$ (fiche §7).

| | Question | Réponse attendue |
|---|---|---|
| a | $x_1, x_2, x_3, x_4$ | une liste de 4 nombres (2 décimales) |
| b | $J_t$ (le même chaque année) | un nombre |
| c | $b_0, b_1, b_2, b_3$ | une liste de 4 nombres (2 décimales) |
| d | les quatre termes de la somme sur le temps de $s_4$, de celui de l'année 0 à celui de l'année 3 | une liste de 4 nombres (2 décimales) |
| e | $s_4$ | un nombre (2 décimales) |
| f | au premier ordre, le changement de $x_4$ quand le taux passe de 3 % à 3,2 % | un nombre (2 décimales) |
| g | le changement exact de $x_4$ | un nombre (2 décimales) |

Dans ta copie : calcule aussi $s_4$ pas à pas, par $s_{t+1} = J_ts_t + b_t$. Écris $x_4$ comme une formule en $\beta$ (la solution du §1), dérive-la, et retrouve e). Que représente le terme de l'année $k$ ? Pourquoi f) et g) diffèrent-ils un peu ?

### Ex M22.10 — La norme globale de trois blocs, et deux façons de les ramener sous un seuil ✏️ ★ ⏱️ 15 min
**Objectif :** calculer la norme d'un vecteur fait de blocs, et comparer les deux façons de le ramener sous un seuil.
**Prérequis :** fiche §8 ; M07, M19 §8 · **Parcours :** C, E

Un robot a trois bras ; sa commande regroupe les vitesses de leurs articulations, en rad/s : $\mathbf{w}_1 = (2, -2, 2, 2)$ pour le bras à quatre articulations, $\mathbf{w}_2 = (2, 3, -6)$ pour celui à trois, $\mathbf{w}_3 = (-4)$ pour celui à une. Par sécurité, la norme globale de $\mathbf{w} = (\mathbf{w}_1, \mathbf{w}_2, \mathbf{w}_3)$ doit rester au plus $c = 5$.

| | Question | Réponse attendue |
|---|---|---|
| a | les normes des trois blocs | une liste de 3 nombres |
| b | la norme globale de $\mathbf{w}$ | un nombre |
| c | le bloc $\mathbf{w}_2$ après qu'on a ramené le tout sous $c$ | une liste de 3 nombres (4 décimales) |
| d | les normes des trois blocs après qu'on a ramené le tout sous $c$ | une liste de 3 nombres (4 décimales) |
| e | les normes des trois blocs quand on ramène plutôt chaque bloc sous $c$ | une liste de 3 nombres |
| f | la norme globale dans le cas e) | un nombre (4 décimales) |
| g | le cosinus de l'angle entre $\mathbf{w}$ et le vecteur du cas e) | un nombre (4 décimales) |
| h | la norme globale quand on ramène chaque bloc sous le seuil $\frac{c}{\sqrt3}$ | un nombre |

Dans ta copie : pourquoi la norme globale n'est-elle pas la somme des normes des blocs ? Vérifie que c) garde les proportions entre les blocs. Convertis g) en degrés. Pourquoi h) tombe-t-il exactement sur $c$ ici, et que se passerait-il si un bloc était déjà sous $\frac{c}{\sqrt3}$ ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M22.11 — Sous-multiplicativité, ‖Aᵀ‖₂ = ‖A‖₂, ‖diag(d)‖₂ = max |dᵢ| et ρ(A) ≤ ‖A‖ ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer les propriétés des normes induites que le chapitre utilise, y compris pour un vecteur propre complexe.
**Prérequis :** fiche §4 ; M12c §3, M12d · **Parcours :** C, E

Sauf mention, $\lVert\cdot\rVert$ désigne l'une des trois normes induites $\lVert\cdot\rVert_1$, $\lVert\cdot\rVert_2$, $\lVert\cdot\rVert_\infty$, associée à la norme de vecteurs de même indice, et les matrices sont réelles.

1. Soit $\mathbf{A}$ de forme $(m, k)$ et $\mathbf{B}$ de forme $(k, n)$. Montre que $\lVert\mathbf{A}\mathbf{B}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{B}\rVert$. Déduis-en, par récurrence, $\lVert\mathbf{A}^t\rVert \le \lVert\mathbf{A}\rVert^t$ pour $\mathbf{A}$ carrée, et $\lVert\mathbf{A}_t\cdots\mathbf{A}_1\rVert \le \lVert\mathbf{A}_t\rVert\cdots\lVert\mathbf{A}_1\rVert$.
2. Soit $\lambda \ne 0$ une valeur propre de $\mathbf{A}^\top\mathbf{A}$, de vecteur propre $\mathbf{v}$. Montre que $\mathbf{A}\mathbf{v} \ne \mathbf{0}$, et que $\mathbf{A}\mathbf{v}$ est un vecteur propre de $\mathbf{A}\mathbf{A}^\top$ pour la même valeur propre. Déduis-en $\lVert\mathbf{A}^\top\rVert_2 = \lVert\mathbf{A}\rVert_2$ (traite à part le cas $\mathbf{A} = \mathbf{0}$). Trouve une matrice $2 \times 2$ telle que $\lVert\mathbf{A}^\top\rVert_1 \ne \lVert\mathbf{A}\rVert_1$.
3. Montre que $\lVert\operatorname{diag}(\mathbf{d})\rVert_2 = \max_i\lvert d_i\rvert$ : majore $\lVert\operatorname{diag}(\mathbf{d})\,\mathbf{x}\rVert_2^2$, puis trouve un vecteur qui atteint la borne. Dis en une phrase pourquoi c'est encore vrai pour $\lVert\cdot\rVert_1$ et $\lVert\cdot\rVert_\infty$.
4. Les normes des vecteurs complexes : pour $\mathbf{z} \in \mathbb{C}^n$, $\lVert\mathbf{z}\rVert_1 = \sum_j\lvert z_j\rvert$, $\lVert\mathbf{z}\rVert_\infty = \max_j\lvert z_j\rvert$ et $\lVert\mathbf{z}\rVert_2^2 = \sum_j\lvert z_j\rvert^2$. Écris $\mathbf{z} = \mathbf{u} + i\mathbf{v}$ avec $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, montre que $\lVert\mathbf{z}\rVert_2^2 = \lVert\mathbf{u}\rVert_2^2 + \lVert\mathbf{v}\rVert_2^2$, puis que $\lVert\mathbf{A}\mathbf{z}\rVert_2 \le \lVert\mathbf{A}\rVert_2\,\lVert\mathbf{z}\rVert_2$ pour $\mathbf{A}$ réelle. Montre aussi $\lVert\mathbf{A}\mathbf{z}\rVert_1 \le \lVert\mathbf{A}\rVert_1\,\lVert\mathbf{z}\rVert_1$, en refaisant avec des modules le calcul de la fiche (§4), et dis comment se traite $\lVert\cdot\rVert_\infty$.
5. Déduis-en $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert$ pour $\mathbf{A}$ carrée et pour chacune des trois normes, puis $\rho(\mathbf{A})^t \le \lVert\mathbf{A}^t\rVert$.
6. Donne une matrice $2 \times 2$ non nulle telle que $\rho(\mathbf{A}) < \lVert\mathbf{A}\rVert$ pour les trois normes, et une matrice non nulle pour laquelle il y a égalité dans les trois.

### Ex M22.12 — La norme induite ‖·‖∞ est le maximum des sommes de lignes ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule de $\lVert\cdot\rVert_\infty$, la relier à celle de $\lVert\cdot\rVert_1$, et s'en servir pour une matrice à coefficients positifs.
**Prérequis :** fiche §4 ; M07 · **Parcours :** C

$\mathbf{A}$ est une matrice réelle de forme $(m, n)$, non nulle, et $L = \max_i\sum_j\lvert a_{ij}\rvert$ la plus grande somme des valeurs absolues d'une ligne.

1. Montre que $\lVert\mathbf{A}\mathbf{x}\rVert_\infty \le L\,\lVert\mathbf{x}\rVert_\infty$ pour tout $\mathbf{x} \in \mathbb{R}^n$.
2. Soit $i^\star$ une ligne où la somme vaut $L$, et $\mathbf{x}^\star$ le vecteur de coordonnées $x^\star_j = \operatorname{signe}(a_{i^\star j})$ (et $x^\star_j = 1$ si $a_{i^\star j} = 0$). Montre que $\lVert\mathbf{x}^\star\rVert_\infty = 1$ et que $(\mathbf{A}\mathbf{x}^\star)_{i^\star} = L$. Conclus : $\lVert\mathbf{A}\rVert_\infty = L$.
3. Déduis-en $\lVert\mathbf{A}^\top\rVert_1 = \lVert\mathbf{A}\rVert_\infty$, avec la formule de $\lVert\cdot\rVert_1$ de la fiche.
4. Pour $\mathbf{A} = \begin{pmatrix} 2 & 0 & -5 \\ 1 & -3 & 1 \end{pmatrix}$ : calcule $\lVert\mathbf{A}\rVert_\infty$, et trouve **tous** les vecteurs $\mathbf{x}$ tels que $\lVert\mathbf{x}\rVert_\infty = 1$ et $(\mathbf{A}\mathbf{x})_0 = \lVert\mathbf{A}\rVert_\infty$ (la première ligne est la ligne 0). Pourquoi y en a-t-il une infinité ?
5. $\mathbf{S} = \begin{pmatrix} 0{,}2 & 0{,}3 & 0{,}1 \\ 0{,}1 & 0{,}2 & 0{,}3 \\ 0{,}4 & 0 & 0{,}2 \end{pmatrix}$ a des coefficients positifs ou nuls. Montre que $\lVert\mathbf{S}^t\rVert_\infty = 0{,}6^t$ exactement (pense au vecteur $(1, 1, 1)$), que chaque coefficient de $\mathbf{S}^t$ est au plus $0{,}6^t$, et que $\rho(\mathbf{S}) = 0{,}6$.

### Ex M22.13 — Aᵗ → 0 si et seulement si ρ(A) < 1, pour une matrice diagonalisable sur ℂ ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer le théorème du §3 dans le cas diagonalisable, avec une constante explicite, et voir où l'hypothèse sert.
**Prérequis :** fiche §2 et §3 ; M12c §4 · **Parcours :** C, E

$\mathbf{A}$ est une matrice carrée réelle, diagonalisable sur $\mathbb{C}$ : $\mathbf{A} = \mathbf{V}\mathbf{D}\mathbf{V}^{-1}$, avec $\mathbf{D} = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$ et $\mathbf{V}$ inversible, éventuellement complexes. « $\mathbf{A}^t \to \mathbf{0}$ » veut dire que chaque coefficient tend vers 0.

1. Montre par récurrence que $\mathbf{A}^t = \mathbf{V}\mathbf{D}^t\mathbf{V}^{-1}$ pour tout $t \ge 0$.
2. Écris le coefficient $(j, k)$ de $\mathbf{A}^t$ comme une somme sur $i$ faisant intervenir $\lambda_i^t$. Déduis-en $\lvert(\mathbf{A}^t)_{jk}\rvert \le C_{jk}\,\rho(\mathbf{A})^t$, avec une constante $C_{jk}$ que tu donnes, puis que $\rho(\mathbf{A}) < 1$ entraîne $\mathbf{A}^t \to \mathbf{0}$.
3. Réciproquement, soit $\lambda$ une valeur propre de module $\lvert\lambda\rvert \ge 1$, et $\mathbf{v} \ne \mathbf{0}$ un vecteur propre (complexe peut-être). Montre que $\mathbf{A}^t\mathbf{v}$ ne tend pas vers $\mathbf{0}$, et conclus que $\mathbf{A}^t$ ne tend pas vers $\mathbf{0}$.
4. Applique à la matrice $\mathbf{A} = \begin{pmatrix} 0{,}2 & 0{,}4 \\ 0{,}6 & 0 \end{pmatrix}$ de M22.4 : trouve $\mathbf{V}$ et $\mathbf{V}^{-1}$, écris $\mathbf{A}^t$ en formule, et montre que chaque coefficient de $\mathbf{A}^t$ est au plus $1{,}2 \times 0{,}6^t$ en valeur absolue.
5. Pour la matrice $\mathbf{B} = \begin{pmatrix} 2 & -3 \\ 1 & -1 \end{pmatrix}$ de M22.4 : explique avec la question 3 pourquoi $\mathbf{B}^t$ ne tend pas vers $\mathbf{0}$, et avec la question 1 pourquoi ses puissances restent bornées.
6. Où la démonstration de la question 2 utilise-t-elle l'hypothèse « diagonalisable » ? Pour le bloc de Jordan $\begin{pmatrix} \lambda & \gamma \\ 0 & \lambda \end{pmatrix}$ de la fiche, avec $\lvert\lambda\rvert < 1$ et $\gamma \ne 0$, qu'est-ce qui change, et pourquoi la conclusion tient-elle encore ?

### Ex M22.14 — Une application contractante oublie son point de départ : l'écart entre deux trajectoires décroît géométriquement ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer la propriété des contractions du §6, puis la tester sur une application affine et sur un contre-exemple.
**Prérequis :** fiche §4 et §6 ; R4, R5 · **Parcours :** C

$f$ envoie une partie $\mathcal{D}$ de $\mathbb{R}^n$ dans elle-même, et il existe $q \in [0, 1[$ tel que $\lVert f(\mathbf{x}) - f(\tilde{\mathbf{x}})\rVert \le q\,\lVert\mathbf{x} - \tilde{\mathbf{x}}\rVert$ pour tous $\mathbf{x}, \tilde{\mathbf{x}} \in \mathcal{D}$, pour une norme $\lVert\cdot\rVert$. Deux trajectoires $\mathbf{x}_{t+1} = f(\mathbf{x}_t)$ et $\tilde{\mathbf{x}}_{t+1} = f(\tilde{\mathbf{x}}_t)$ partent de $\mathbf{x}_0, \tilde{\mathbf{x}}_0 \in \mathcal{D}$.

1. Montre par récurrence que $\mathbf{x}_t$ et $\tilde{\mathbf{x}}_t$ restent dans $\mathcal{D}$, et que $\lVert\mathbf{x}_t - \tilde{\mathbf{x}}_t\rVert \le q^t\,\lVert\mathbf{x}_0 - \tilde{\mathbf{x}}_0\rVert$.
2. Montre que $f$ a au plus un point fixe dans $\mathcal{D}$.
3. Si $\mathbf{x}^\star \in \mathcal{D}$ est un point fixe, montre que $\lVert\mathbf{x}_t - \mathbf{x}^\star\rVert \le q^t\,\lVert\mathbf{x}_0 - \mathbf{x}^\star\rVert$.
4. $f(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{c}$ sur $\mathcal{D} = \mathbb{R}^2$, avec $\mathbf{A} = \begin{pmatrix} 0{,}3 & -0{,}3 \\ 0{,}1 & 0{,}3 \end{pmatrix}$ et $\mathbf{c} = (1, 2)$. Montre que $f$ est contractante de facteur $0{,}6$ pour $\lVert\cdot\rVert_1$. Trouve son point fixe, en résolvant un système linéaire. Deux trajectoires partent de $(5, -3)$ et de $(-1, 4)$ : majore leur écart en norme 1 après 10 pas.
5. $g(\mathbf{x}) = \mathbf{J}\mathbf{x}$ avec $\mathbf{J} = \begin{pmatrix} 0{,}2 & 3 \\ 0 & 0{,}2 \end{pmatrix}$ : $\rho(\mathbf{J}) = 0{,}2$, et toutes les trajectoires tendent vers $\mathbf{0}$. Montre que $g$ n'est pas contractante pour $\lVert\cdot\rVert_2$, en exhibant deux points. Montre ensuite que $g \circ g$ ne l'est pas non plus, mais que $g \circ g \circ g$ l'est.

### Ex M22.15 — La sensibilité de l'état final à un paramètre utilisé à chaque pas suit une récurrence avec entrée : sa solution est une somme sur le temps ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la récurrence de la sensibilité et sa solution, la propriété du §7.
**Prérequis :** fiche §5 et §7 ; M17, M18 · **Parcours :** C

$f : \mathbb{R}^n \times \mathbb{R} \to \mathbb{R}^n$ est dérivable, $\mathbf{x}_{t+1} = f(\mathbf{x}_t, \beta)$, et $\mathbf{x}_0$ ne dépend pas de $\beta$. On note $\mathbf{s}_t = \frac{\partial\mathbf{x}_t}{\partial\beta}$, $\mathbf{J}_t = \frac{\partial f}{\partial\mathbf{x}}(\mathbf{x}_t, \beta)$ et $\mathbf{b}_t = \frac{\partial f}{\partial\beta}(\mathbf{x}_t, \beta)$.

1. En appliquant la règle de la chaîne (M17) à $\beta \mapsto f\big(\mathbf{x}_t(\beta), \beta\big)$, montre que $\mathbf{s}_{t+1} = \mathbf{J}_t\mathbf{s}_t + \mathbf{b}_t$, avec $\mathbf{s}_0 = \mathbf{0}$. Dessine le graphe de calcul de $\mathbf{x}_2$ et repère ses chemins de $\beta$ à $\mathbf{x}_2$ (M18).
2. Montre par récurrence sur $T \ge 1$ que $\mathbf{s}_T = \sum_{k=0}^{T-1}\mathbf{J}_{T-1}\mathbf{J}_{T-2}\cdots\mathbf{J}_{k+1}\,\mathbf{b}_k$, le produit valant $\mathbf{I}$ pour $k = T - 1$.
3. Si $f(\mathbf{x}, \beta) = \mathbf{A}\mathbf{x} + \mathbf{g}(\beta)$ avec $\mathbf{A}$ fixe, montre que la formule devient celle du théorème du §1, l'entrée $\mathbf{B}\mathbf{u}_k$ étant remplacée par $\mathbf{b}_k$.
4. Si $\mathbf{x}_0$ dépend aussi de $\beta$, avec $\mathbf{s}_0 = \frac{\partial\mathbf{x}_0}{\partial\beta} \ne \mathbf{0}$, quel terme s'ajoute à la somme ? À quoi correspond-il dans le vocabulaire du §1 ?
5. Pour $n = 1$, vérifie la formule pour $T = 2$ en dérivant directement $x_2 = f\big(f(x_0, \beta), \beta\big)$.
6. Applique à la pêche avec repeuplement de M22.Q7, $x_{t+1} = 1{,}4\,(1 - \beta)\,x_t + 20$ : donne $J_t$ et $b_t$, écris $s_3$ comme une somme de trois termes, et retrouve la valeur $s_3 = -223{,}216$ de l'énoncé du quiz pour $\beta = 0{,}4$ et $x_0 = 50$.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M22.16 — Pont : la convention ligne x_{t+1} = x_t A + u_t B, ses formes, et la jacobienne Aᵀ 🔗 ★ ⏱️ 15 min
**Objectif :** passer de la convention colonne de ce chapitre à la convention ligne des bibliothèques, avec les formes, la solution et la jacobienne.
**Prérequis :** fiche §1 et §6 ; M17 · **Parcours :** C, E

Les bibliothèques (NumPy, PyTorch) rangent les états en **lignes** : un état est un vecteur ligne $\mathbf{x}_t$ de forme $(1, n)$, une entrée un vecteur ligne $\mathbf{u}_t$ de forme $(1, m)$, et
$$\mathbf{x}_{t+1} = \mathbf{x}_t\mathbf{A} + \mathbf{u}_t\mathbf{B}.$$
Pour les questions c) à f) : $n = 2$, $m = 1$,
$$\mathbf{A} = \begin{pmatrix} 0{,}2 & 0{,}6 \\ -0{,}4 & 0{,}3 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 1 & -2 \end{pmatrix}, \qquad \mathbf{x}_0 = (4, -1), \qquad (u_0, u_1, u_2) = (1, 0, -1).$$

| | Question | Réponse attendue |
|---|---|---|
| a | pour $n = 3$ coordonnées d'état et $m = 2$ entrées, la forme de $\mathbf{B}$ en convention ligne | une forme |
| b | $N = 8$ états rangés en lignes dans un tableau $\mathbf{X}_t$ de forme $(8, 3)$ : la forme de $\mathbf{X}_t\mathbf{A}$ | une forme |
| c | $\mathbf{x}_1$, $\mathbf{x}_2$ et $\mathbf{x}_3$, rangés en lignes | une matrice $3 \times 2$ |
| d | la matrice $\mathbf{A}_{\text{col}}$ telle que $\mathbf{x}_{t+1}^\top = \mathbf{A}_{\text{col}}\,\mathbf{x}_t^\top + \mathbf{B}^\top u_t$ (la même récurrence en convention colonne) | une matrice |
| e | la jacobienne de $\mathbf{x} \mapsto \mathbf{x}\mathbf{A}$ (une ligne par coordonnée de sortie, M17) | une matrice |
| f | $\frac{\partial\mathbf{x}_3}{\partial\mathbf{x}_0}$, avec la même convention pour la jacobienne | une matrice (4 décimales) |
| g | vrai ou faux : en convention ligne, $\mathbf{x}_t = \mathbf{x}_0\mathbf{A}^t + \sum_{k=0}^{t-1}\mathbf{u}_k\mathbf{B}\mathbf{A}^{t-1-k}$ | `True` ou `False` |

Dans ta copie : transpose la récurrence ligne pour retrouver une récurrence de ce chapitre. Pourquoi la jacobienne de $\mathbf{x} \mapsto \mathbf{x}\mathbf{A}$ est-elle $\mathbf{A}^\top$ (écris $(\mathbf{x}\mathbf{A})_j$) ? Le long d'une trajectoire, les bibliothèques multiplient donc des transposées : que valent $\big\lVert(\mathbf{A}^\top)^t\big\rVert_2$ et $\rho(\mathbf{A}^\top)$, comparés à ceux de $\mathbf{A}^t$ et de $\mathbf{A}$ (∂ M22.11) ?

### Ex M22.17 — MML §4.2 relu : les cinq applications du plan de la figure 4.4, leurs valeurs propres, et le comportement de leurs puissances 📖 ★★ ⏱️ 30 min
**Objectif :** relire une section de MML avec les outils du chapitre : valeurs propres complexes, rayon spectral, matrices normales et puissances.
**Prérequis :** fiche §2 et §3 ; M12c · **Parcours :** C

Relis MML §4.2 (*Eigenvalues and Eigenvectors*), de la définition 4.6 à la fin du passage *Graphical Intuition in Two Dimensions*, en t'arrêtant sur la figure 4.4 (guide de lecture de la fiche). Réponds dans ta copie, en français. Les cinq matrices de la figure sont notées $\mathbf{A}_1$ à $\mathbf{A}_5$, comme dans le livre.
1. Relève les valeurs propres et le déterminant de chacune des cinq matrices, et vérifie-les par la trace et le déterminant (fiche §2).
2. La figure écrit les valeurs propres de $\mathbf{A}_3$ à la manière de Python. Écris-les sous forme exponentielle. Pourquoi la définition 4.6 du livre ne donne-t-elle aucune valeur propre à $\mathbf{A}_3$, alors que la fiche lui en donne deux ? Que valent $\mathbf{A}_3^6$ et $\mathbf{A}_3^{12}$ ?
3. Calcule le rayon spectral de chacune, et écris $\mathbf{A}_i^t$ en formule (pour $\mathbf{A}_4$, calcule d'abord $\mathbf{A}_4^2$ ; pour $\mathbf{A}_5$, passe par ses vecteurs propres). Classe les cinq selon le comportement de leurs puissances : elles tendent vers $\mathbf{0}$, restent bornées sans tendre vers $\mathbf{0}$, ou ne sont pas bornées. Attention à $\mathbf{A}_2$.
4. Lesquelles sont normales ? Pour celles-là, $\lVert\mathbf{A}_i^t\rVert_2 = \rho(\mathbf{A}_i)^t$. Compare $\lVert\mathbf{A}_2^t\rVert_2$, pour $t$ grand, à $\rho(\mathbf{A}_2)^t$.
5. La figure montre l'image d'une grille de points par une application de chaque matrice. Décris en une phrase, sans la tracer, l'image de la même grille par $\mathbf{A}_i^6$, pour chacune des cinq.
6. $\mathbf{A}_2$ n'a qu'une direction propre : quels mots du livre le disent (deux multiplicités), et à quel objet du §3 de la fiche $\mathbf{A}_2$ ressemble-t-elle ?
7. Refais l'analyse de $\mathbf{A}_5$ avec tes propres nombres : pour $\begin{pmatrix} a & c \\ c & a \end{pmatrix}$, donne les valeurs propres, et la condition sur $a$ et $c$ pour que les puissances tendent vers $\mathbf{0}$. Choisis un couple $(a, c)$ qui la vérifie et un qui ne la vérifie pas.
8. Relève cinq expressions anglaises de la section et leur traduction dans la fiche.

### Ex M22.18 — Expliquer avec une image non mathématique pourquoi un système linéaire oublie son passé au rythme de ρ(A) 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule pourquoi une récurrence linéaire oublie son état de départ, et ce qui fixe la vitesse de cet oubli.
**Prérequis :** fiche §2 et §3 · **Parcours :** C, E

Un ami gère trois bassins de rétention reliés entre eux. Après un orage, il remarque que trois semaines plus tard les niveaux n'en gardent presque aucune trace, mais que, selon les réglages des vannes, la trace s'efface plus ou moins vite. Il te demande : « Pourquoi l'orage est-il oublié, et qu'est-ce qui décide de la vitesse de cet oubli ? »

Réponds-lui en 6 à 10 phrases, sans formule, avec une image de la vie courante (une maison qu'on aère, un écho, ou une autre de ton choix) : ce que la règle fait chaque jour à l'excès d'eau laissé par l'orage, pourquoi cet excès se décompose en plusieurs « façons de s'effacer » qui ont chacune leur rythme, pourquoi la plus lente finit par décider seule, ce que vaut ce rythme dans le vocabulaire du chapitre, et la mise en garde qu'on doit ajouter pour les premiers jours. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M22.E1 — « Quelle différence entre le rayon spectral et la norme d'une matrice ? » 💼 ★ ⏱️ 10 min
*Fiche §3 et §4 · parcours C*

« Quelle différence entre le rayon spectral et la norme d'une matrice ? »

Ta réponse doit dire ce que mesure chacun (le long terme, chaque pas), l'inégalité qui les relie et pourquoi, le cas où ils sont égaux (et dans quelle norme), un exemple où ils diffèrent beaucoup, ce que chacun permet de garantir sur $\mathbf{A}^t$, comment on calcule l'un et l'autre, et le lien que donne la formule de Gelfand.

### M22.E2 — « Pourquoi Aⁿ peut-il grandir longtemps alors que toutes les valeurs propres de A sont de module < 1 ? » 💼 ★ ⏱️ 10 min
*Fiche §3 · parcours C*

« Pourquoi Aⁿ peut-il grandir longtemps alors que toutes les valeurs propres de A sont de module < 1 ? »

Ta réponse doit dire ce que garantit le rayon spectral et ce qu'il ne garantit pas, donner un exemple $2 \times 2$, expliquer le mécanisme (des vecteurs propres presque parallèles, ou une valeur propre double), dire pour quelles matrices le phénomène est impossible, et pourquoi il compte en pratique.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m22_recurrences/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M22.19 | Les états d'une récurrence linéaire avec entrée · `linear_system_states` | 🔨 | ★ | 20 | C, E |
| M22.20 | Les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂ · `operator_norm` | 🔨 | ★★ | 30 | C, E |
| M22.21 | Les normes des produits cumulés, et leur majoration · `product_norms` | 🔨 | ★ | 20 | C, E |
| M22.22 | `np.linalg.eigvals` et `np.linalg.norm` : rayon spectral et normes de matrices tirées au hasard, et ρ ≤ ‖A‖ | 📦 | ★ | 15 | C |
| M22.23 | Prédire l'allure de ‖Aᵗ‖₂ pour une matrice non normale de rayon spectral 0,8, puis tracer | 🔮 | ★ | 15 | C, E |
| M22.24 | Des produits de matrices aléatoires : le taux de croissance (1/n) ln ‖Aₙ ⋯ A₁‖ | 🔬 | ★★ | 20 | C |
| M22.25 | Les spirales d'une récurrence 2 × 2 à valeurs propres complexes, selon leur module | 🎨 | ★ | 15 | C, E |
| M22.26 | Chasse à l'erreur : ρ(A) pris pour ‖A‖, un produit de jacobiennes dans le mauvais ordre, un seuil appliqué bloc par bloc | 🐛 | ★ | 20 | C, E |
| M22.27 | Un test de propriété : ‖AB‖ ≤ ‖A‖ ‖B‖ et ρ(A) ≤ ‖A‖ sur des matrices tirées au hasard | 🛠️ | ★ | 15 | C |
| M22.28 | Défi : une matrice 3 × 3 à coefficients dans [−3, 3], de rayon spectral 0,85, dont une puissance a une norme ‖·‖₂ supérieure à 100 | 🏆 | ★★★ | 25 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les trois 🔨 complètent ta copie `mon_travail/mymath/recurrence.py` (**mymath :** `recurrence.py`), dont la docstring du module dit ce qui est permis : NumPy, mais, de `np.linalg`, seulement `eigvalsh` (dans `operator_norm`) et `norm` (dans `product_norms`), et aucune fonction de SciPy. Chaque 🔨 lance ensuite le groupe de tests de sa fonction dans `tests/test_m22_recurrence.py`, puis s'en sert. Dans les exercices suivants, le rayon spectral se calcule par `np.abs(np.linalg.eigvals(A)).max()`, et une puissance $\mathbf{A}^t$ par $t$ produits successifs (ou `np.linalg.matrix_power`), hors de `mymath`.

**M22.19 · 🔨 `linear_system_states(A, B, x0, inputs)`.** Écris les états $\mathbf{x}_0, \ldots, \mathbf{x}_T$ de $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t$, rangés en lignes dans un tableau $(T + 1, n)$ (la docstring fixe les formes et les refus), une multiplication par $\mathbf{A}$ par pas, sans jamais calculer $\mathbf{A}^t$ ; puis lance le groupe de tests `linear_system_states`. Ensuite, avec ta fonction : a) $\mathbf{x}_3$ pour la population de M22.1 (ses trois entrées), à comparer à ta réponse c) ; b) la même population, partie de $\mathbf{x}_0 = (40, 20, 30)$, avec les mêmes lâchers $\mathbf{u}_t = (20, 10)$ chaque année pendant $T = 60$ ans : la population totale (la somme des trois classes) au printemps 60 (2 décimales) ; c) l'équilibre $\mathbf{x}^\star$, solution de $(\mathbf{I} - \mathbf{A})\mathbf{x}^\star = \mathbf{B}\mathbf{u}$ (`np.linalg.solve`), et sa population totale ; d) vrai ou faux : les trois coordonnées de $\mathbf{x}_{60}$ sont à moins de 0,01 de celles de $\mathbf{x}^\star$ ; e) pour les bassins de M22.2 : la réponse impulsionnelle $h_0, \ldots, h_6$, obtenue en simulant une impulsion ($u_0 = 1$, puis des pluies nulles) avec ta fonction et en lisant $y_{t+1} = h_t$ ; puis les rejets $y_1, \ldots, y_7$ pour les pluies $(10, 0, 20, 5, 0, 0, 0)$, calculés à partir des états ($y_t = \mathbf{C}\mathbf{x}_t$) : vrai ou faux, ils sont égaux, à $10^{-12}$ près, aux sept premières valeurs de `np.convolve(h, u)` ; f) $y_6$ et $y_7$ (4 décimales). Ce qu'il faut observer : partie d'un autre état, la population oublie son départ et rejoint l'équilibre, au rythme de $\rho(\mathbf{A}) \approx 0{,}84$ par an ; et la sortie d'un système linéaire parti de $\mathbf{0}$ est la convolution de son entrée par sa réponse impulsionnelle.

**M22.20 · 🔨 `operator_norm(A, ord=2)`.** Écris les trois normes induites : la plus grande somme des valeurs absolues d'une colonne (`ord=1`), d'une ligne (`ord=np.inf`), et $s_{\max}$, la racine de la plus grande valeur propre de $\mathbf{A}^\top\mathbf{A}$ (`np.linalg.eigvalsh`, valeur ramenée à 0 si l'arrondi la rend négative) ; la docstring fixe les refus (dont `"fro"`). Lance le groupe de tests `operator_norm`. Ensuite : a) les trois normes de la matrice de M22.6, dans l'ordre 1, 2, $\infty$ ; b) pour cette matrice, $\lVert\mathbf{A}^t\rVert_2^{1/t}$ pour $t = 1$, 10 et 50 (4 décimales), à comparer à $\rho(\mathbf{A}) = 2$ ; c) `operator_norm(np.eye(5), ord)` pour `ord` = 1, 2 et `np.inf`, puis `np.linalg.norm(np.eye(5))` (4 décimales) ; d) pour la matrice $\mathbf{A}$ de M22.5, le pas $t$ (de 1 à 10) où $\lVert\mathbf{A}^t\rVert_2$ est le plus grand ; e) vrai ou faux : pour cette matrice, $\lVert\mathbf{A}^t\rVert_2 \ge (\mathbf{A}^t)_{12}$ pour $t = 1, \ldots, 30$. Ce qu'il faut observer : $\lVert\mathbf{A}^t\rVert^{1/t}$ descend lentement vers $\rho(\mathbf{A})$ (la formule de Gelfand) ; la norme de Frobenius de $\mathbf{I}_5$ n'est pas 1, elle n'est pas induite ; et le maximum de la norme n'est pas toujours au même pas que celui d'un coefficient (d) contre M22.5 c)).

**M22.21 · 🔨 `product_norms(matrices, ord=2)`.** Écris les normes des produits cumulés $\mathbf{P}_t = \mathbf{A}_t\cdots\mathbf{A}_1$ (le nouveau facteur à gauche) et leurs majorations $\lVert\mathbf{A}_t\rVert\cdots\lVert\mathbf{A}_1\rVert$, avec `np.linalg.norm` ; lance le groupe de tests `product_norms`. Ensuite : a) la trajectoire de l'application de Hénon de M22.8, partie de $(0, 0)$, sur 30 pas ; avec les jacobiennes $\mathbf{J}_f(\mathbf{x}_0), \ldots, \mathbf{J}_f(\mathbf{x}_{29})$ données dans cet ordre, la troisième norme rendue, $\lVert\mathbf{P}_3\rVert_2$, qui est la norme de ta réponse d) de M22.8 (3 décimales) ; b) le rapport de la majoration à la norme pour $t = 30$, arrondi à l'entier ; c) le taux $\frac{1}{30}\ln\lVert\mathbf{P}_{30}\rVert_2$ (2 décimales) ; d) les douze matrices $\operatorname{diag}(0{,}985 ;\ 0{,}93 ;\ 0{,}65)$ des équipements de M22.7 : vrai ou faux, les normes et les majorations sont égales à $10^{-12}$ près (en valeur relative) ; e) trace, en échelle logarithmique, les normes et les majorations de a) contre $t$. Ce qu'il faut observer : la majoration par les normes grossit beaucoup plus vite que le produit quand les jacobiennes tournent les vecteurs dans des directions différentes (un facteur de l'ordre de mille après 30 pas) ; elle est exacte pour des matrices diagonales égales.

**M22.22 · 📦 `np.linalg.eigvals` et `np.linalg.norm`.** Tire 1 000 matrices $4 \times 4$ de coefficients gaussiens, `rng = np.random.default_rng(5722)` puis `A = rng.normal(size=(1000, 4, 4))`, et calcule, pour chaque `A[k]`, son rayon spectral (`np.abs(np.linalg.eigvals(A[k])).max()`) et ses normes `np.linalg.norm(A[k], 1)`, `np.linalg.norm(A[k], 2)`, `np.linalg.norm(A[k], np.inf)` et `np.linalg.norm(A[k], "fro")`. a) La proportion des matrices pour lesquelles $\rho$ est au plus égal à la plus petite des trois normes induites ; b) la moyenne de $\rho/\lVert\cdot\rVert_2$ (2 décimales) ; c) la proportion des matrices pour lesquelles $\lVert\cdot\rVert_1 < \lVert\cdot\rVert_2$ (3 décimales) ; d) pour les parties symétriques $\mathbf{S}_k = \frac12(\mathbf{A}_k + \mathbf{A}_k^\top)$ : vrai ou faux, $\lvert\rho(\mathbf{S}_k) - \lVert\mathbf{S}_k\rVert_2\rvert < 10^{-12}$ pour les 1 000 ; e) pour `A[0]`, deux vrai ou faux : `np.linalg.norm(A[0])` (sans `ord`) est égal à la norme de Frobenius, puis à $\lVert\cdot\rVert_2$ ; f) pour `A[0]`, $\lVert\mathbf{A}^t\rVert_2^{1/t}$ pour $t = 1$, 5, 25 et 100, puis $\rho$ (une liste de 5 nombres, 3 décimales). Ce qu'il faut observer : $\rho \le \lVert\cdot\rVert$ sans exception, avec un écart important pour une matrice quelconque (en moyenne, $\rho$ n'est que les deux tiers de $\lVert\cdot\rVert_2$) ; l'égalité pour les matrices symétriques (en norme 2) ; et le piège de `np.linalg.norm` sans `ord`.

**M22.23 · 🔮 Prédire l'allure de ‖Aᵗ‖₂ pour une matrice non normale de rayon spectral 0,8, puis tracer.** $\mathbf{A} = \begin{pmatrix} -1{,}2 & 2 \\ -2 & 2{,}8 \end{pmatrix}$. **Avant d'exécuter**, calcule à la main ses valeurs propres et $\mathbf{A}^\top\mathbf{A}$ et $\mathbf{A}\mathbf{A}^\top$, puis prédis : a) l'allure de $\lVert\mathbf{A}^t\rVert_2$ pour $t = 0$ à 40 : (A) elle décroît dès le premier pas, comme $0{,}8^t$ ; (B) elle monte pendant quelques pas, puis décroît vers 0 ; (C) elle monte sans fin ; (D) elle oscille sans décroître ; b) le pas $t$ de son maximum : (A) $t = 1$ ; (B) entre 3 et 6 ; (C) entre 15 et 25 ; c) vrai ou faux : $\lVert\mathbf{A}^{10}\rVert_2 > 1$ ; d) vrai ou faux : $\lVert\mathbf{A}^t\rVert_2 \ge 0{,}8^t$ pour tout $t$. Puis calcule $\lVert\mathbf{A}^t\rVert_2$ pour $t = 0, \ldots, 40$ avec ta `operator_norm`, trace-la en échelle logarithmique avec $0{,}8^t$, et relève : e) le pas $t$ du maximum ; f) la valeur du maximum (2 décimales) ; g) le premier pas $t$ où $\lVert\mathbf{A}^t\rVert_2 < 1$. Ce qu'il faut observer : la valeur propre double 0,8 dit le long terme, pas les premiers pas ; la norme est multipliée par plus de 8 avant de décroître, et passe 20 pas au-dessus de 1.

**M22.24 · 🔬 Des produits de matrices aléatoires : le taux de croissance.** Une plante vivace a deux stades, les graines dans le sol et les plantes en fleur : $\mathbf{x}_t = (\text{graines},\ \text{plantes})$. Une bonne année applique $\mathbf{G} = \begin{pmatrix} 0{,}2 & 3 \\ 0{,}6 & 0{,}4 \end{pmatrix}$, une mauvaise $\mathbf{M} = \begin{pmatrix} 0{,}2 & 0{,}4 \\ 0{,}2 & 0{,}2 \end{pmatrix}$, à pile ou face, indépendamment ; $n$ compte les années, c'est-à-dire les facteurs du produit $\mathbf{P}_n = \mathbf{A}_n\cdots\mathbf{A}_1$. Les années sont tirées par `rng = np.random.default_rng(5724)` puis `years = rng.integers(0, 2, size=20000)` (0 = bonne, 1 = mauvaise ; `years[k - 1]` donne $\mathbf{A}_k$). Mesure : a) $\ln\rho(\mathbb{E}[\mathbf{A}])$, avec $\mathbb{E}[\mathbf{A}] = \frac12(\mathbf{G} + \mathbf{M})$ (3 décimales) : $\mathbb{E}[\mathbf{P}_n] = \mathbb{E}[\mathbf{A}]^n$, la population **moyenne**, grandit à ce taux ; b) avec ta `product_norms`, sur les 200 premières années, $\frac{1}{200}\ln\lVert\mathbf{P}_{200}\rVert_2$ (3 décimales) ; c) sur les 20 000 années, en renormalisant à chaque pas (partir de $\mathbf{x} = \frac{1}{\sqrt2}(1, 1)$, puis, chaque année, $\mathbf{x} \leftarrow \mathbf{A}_k\mathbf{x}$, ajouter $\ln\lVert\mathbf{x}\rVert_2$ à un cumul, et diviser $\mathbf{x}$ par sa norme), le taux $\frac{1}{n}\sum\ln\lVert\mathbf{x}\rVert$ pour $n = 20\,000$ (3 décimales) ; d) la majoration par les normes, $\mathbb{E}[\ln\lVert\mathbf{A}\rVert_2] = \frac12(\ln\lVert\mathbf{G}\rVert_2 + \ln\lVert\mathbf{M}\rVert_2)$ (3 décimales) ; e) le taux c) pour cinq autres suites d'années, tirées de la même façon avec les graines 5731 à 5735 (une liste de 5 nombres, 2 décimales) ; f) vrai ou faux : une trajectoire typique s'éteint, alors que la population moyenne grandit. Trace $\frac1n\ln\lVert\mathbf{P}_n\mathbf{x}_0\rVert$ contre $n$ (abscisse logarithmique) pour les six suites, avec les droites horizontales a) et d). Pourquoi ne pas utiliser `product_norms` sur les 20 000 années ? (Regarde l'ordre de grandeur de $\lVert\mathbf{P}_n\rVert$.) Ce qu'il faut conclure : le taux converge vers le même nombre négatif pour toutes les suites (Furstenberg et Kesten, fiche §5) ; la population typique s'éteint, alors que la moyenne grandit, tirée par de rares suites très chanceuses ; et ni $\ln\rho(\mathbb{E}[\mathbf{A}])$, ni la majoration par les normes ne donnent ce taux : c'est la version matricielle de la plante du §5.

**M22.25 · 🎨 Les spirales d'une récurrence 2 × 2 à valeurs propres complexes, selon leur module.** $\mathbf{A} = \begin{pmatrix} 0 & -1 \\ 1 & 0{,}6 \end{pmatrix}$ a pour déterminant 1 et pour valeurs propres $e^{\pm i\theta}$, avec $\cos\theta = 0{,}3$. Pour $r = 0{,}6$, $0{,}93$, $1$ et $1{,}04$, calcule la trajectoire $\mathbf{x}_t = (r\mathbf{A})^t\mathbf{x}_0$ depuis $\mathbf{x}_0 = (1, 0)$, pour $t = 0$ à 60, avec ta `linear_system_states` (une entrée nulle), et dessine les quatre trajectoires dans quatre panneaux côte à côte, avec des axes à la même échelle dans chaque panneau, les points reliés, et un titre qui donne $r$ et le module des valeurs propres. Dans un cinquième panneau, trace $\lVert\mathbf{x}_t\rVert_2$ contre $t$ en échelle logarithmique pour les quatre valeurs de $r$, avec les droites $r^t$. Ce qu'il faut observer : la matrice tourne d'environ $\theta \approx 1{,}27$ rad (environ 73°) à chaque pas, un tour en un peu moins de 5 pas, dans un repère oblique ; le module des valeurs propres, $r$, décide seul : spirale qui rentre ($r < 1$), ellipse ($r = 1$), spirale qui sort ($r > 1$) ; et $\lVert\mathbf{x}_t\rVert$ suit $r^t$ en oscillant autour, parce que la trajectoire est une ellipse et non un cercle.

**M22.26 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `max_stretch(A)` doit rendre le plus grand facteur par lequel $\mathbf{A}$ peut allonger un vecteur, en norme 2 ; elle renvoie `np.abs(np.linalg.eigvals(A)).max()`, et il l'a vérifiée sur $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, pour laquelle elle rend 3. Il l'applique à $\begin{pmatrix} 2 & 3 \\ -1 & -2 \end{pmatrix}$.
- (2) `trajectory_jacobian(jac, states)` doit rendre $\frac{\partial\mathbf{x}_T}{\partial\mathbf{x}_0} = \mathbf{J}_f(\mathbf{x}_{T-1})\cdots\mathbf{J}_f(\mathbf{x}_0)$ à partir de la fonction jacobienne `jac` et des états `states` $= [\mathbf{x}_0, \ldots, \mathbf{x}_{T-1}]$ ; elle part de $\mathbf{P} = \mathbf{I}$ et fait `P = P @ jac(x)` pour chaque état, dans l'ordre. Il l'a vérifiée sur l'application linéaire $\mathbf{x} \mapsto \begin{pmatrix} 0{,}6 & 0{,}2 \\ 0{,}1 & 0{,}3 \end{pmatrix}\mathbf{x}$. Il l'applique au modèle proie-prédateur $f(x, y) = (1{,}3\,x - 0{,}1\,xy,\ 0{,}8\,y + 0{,}1\,xy)$ ($x$ les proies, $y$ les prédateurs, en milliers), sur trois pas depuis $(4, 2)$.
- (3) `cap_speeds(V, c)` reçoit les vitesses d'une flotte de drones, une ligne par drone (un tableau de forme $(p, 3)$), et doit rendre un **nouveau** tableau dont la norme globale est au plus $c$, sans changer la direction de l'ensemble ; elle multiplie chaque ligne de norme supérieure à $c$ par $\frac{c}{\lVert\text{ligne}\rVert}$. Il l'a vérifiée sur un seul drone, $\mathbf{V} = \begin{pmatrix} 4 & -4 & 2 \end{pmatrix}$ et $c = 5$. Il l'applique à la flotte $\mathbf{V} = \begin{pmatrix} -2 & 1 & 2 \\ 4 & -4 & 2 \\ 6 & 2 & -3 \\ 0 & 0 & 2 \end{pmatrix}$, avec $c = 5$.

Trouve et corrige chaque erreur (la fonction (3) corrigée doit rendre un tableau nul inchangé, sans division par 0), puis réponds : a) `max_stretch` corrigée, pour $\begin{pmatrix} 2 & 3 \\ -1 & -2 \end{pmatrix}$ (4 décimales) ; b) `trajectory_jacobian` corrigée, pour le modèle proie-prédateur (une matrice, 4 décimales) ; c) la norme globale de la flotte rendue par la version fausse de `cap_speeds` (4 décimales) ; d) la norme globale rendue par la version corrigée ; e) la première ligne rendue par la version corrigée (4 décimales). Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas.

**M22.27 · 🛠️ Un test de propriété.** Écris une fonction `property_test_27(norm)` qui reçoit une fonction de même signature que `operator_norm` et tire au hasard (graine 5727), 300 fois, trois tailles $m$, $k$, $n$ entre 1 et 5, une matrice $\mathbf{A}$ de forme $(m, k)$ et une matrice $\mathbf{B}$ de forme $(k, n)$ gaussiennes, puis une matrice carrée $\mathbf{S}$ de taille $k$, et qui vérifie, pour `ord` = 1, 2 et `np.inf` : $\lVert\mathbf{A}\mathbf{B}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{B}\rVert$ et $\rho(\mathbf{S}) \le \lVert\mathbf{S}\rVert$, avec une marge relative de $10^{-12}$ pour l'arrondi, et un message d'échec qui dit d'abord ce qui était attendu, puis le cas fautif ($m$, $k$, $n$, `ord`). Ajoute un cas d'égalité : $\mathbf{B} = c\,\mathbf{I}$, qui doit donner $\lVert\mathbf{A}\mathbf{B}\rVert = \lvert c\rvert\,\lVert\mathbf{A}\rVert$. Lance ton test sur ta `operator_norm`, puis sur deux versions fausses fournies : `norm_frobenius`, qui rend la norme de Frobenius pour `ord=2`, et `norm_swapped`, qui échange les lignes et les colonnes (`ord=1` rend la plus grande somme d'une ligne, `ord=np.inf` celle d'une colonne). Constate que les deux versions fausses **passent** ton test, et explique pourquoi dans une cellule de texte. Ajoute alors deux propriétés qui les attrapent : $\lVert\mathbf{I}_n\rVert = 1$ pour $n \ge 2$, et $\lVert\mathbf{A}\mathbf{x}\rVert_p \le \lVert\mathbf{A}\rVert_p\,\lVert\mathbf{x}\rVert_p$ pour les vecteurs de la base canonique et pour des vecteurs de signes $\pm1$. Ton test complété doit passer sur ta `operator_norm` et échouer sur chacune des deux versions fausses, avec un message qui permet de dire laquelle des propriétés a échoué. Ce qu'il faut retenir : ces deux propriétés valent pour toute norme sous-multiplicative, pas seulement pour les normes induites ; un test de propriété ne remplace pas un oracle, il faut choisir des propriétés qui **distinguent** la bonne fonction des fausses plausibles.

**M22.28 · 🏆 Défi : une matrice 3 × 3 à coefficients dans [−3, 3], de rayon spectral 0,85, dont une puissance a une norme ‖·‖₂ supérieure à 100.** Construis une matrice $\mathbf{A}$ de forme $(3, 3)$, de coefficients tous dans $[-3, 3]$, de rayon spectral $\rho(\mathbf{A}) = 0{,}85$ (à $10^{-9}$ près), telle que $\lVert\mathbf{A}^t\rVert_2 > 100$ pour un pas $t \le 200$. Montre d'abord, dans une cellule de texte, qu'il faut $t \ge 3$ : majore $\lVert\mathbf{A}\rVert_2$ par $\lVert\mathbf{A}\rVert_F$, puis $\lVert\mathbf{A}^2\rVert_2$. **Critère de réussite :** la cellule de vérification contrôle la forme et les coefficients de ta matrice, calcule $\rho(\mathbf{A})$ par `np.linalg.eigvals`, puis $\lVert\mathbf{A}^t\rVert_2$ pour $t = 1, \ldots, 200$ (par produits successifs et ta `operator_norm`), et réussit si $\lvert\rho(\mathbf{A}) - 0{,}85\rvert \le 10^{-9}$ et si l'une de ces normes dépasse 100. Puis relève : a) le premier pas $t$ où $\lVert\mathbf{A}^t\rVert_2 > 100$ ; b) le plus grand $\lVert\mathbf{A}^t\rVert_2$ pour $t \le 200$, et le pas où il est atteint. Pour aller plus loin : peut-on réussir avec une matrice $2 \times 2$ de coefficients dans $[-3, 3]$ ?
