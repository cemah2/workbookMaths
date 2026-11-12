# M21 · Convolution, matrices de Toeplitz et équivariance — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m21_convolution/06_mes_reponses.md` (créée par `python tools/start_chapter.py M21`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les indices commencent à **0** ; un signal $\mathbf{x}$ a $n$ valeurs, un noyau $\mathbf{w}$ en a $k$. La **convolution** $\mathbf{x} * \mathbf{w}$ retourne le noyau, $(\mathbf{x} * \mathbf{w})_m = \sum_i x_i\,w_{m-i}$ (c'est `np.convolve`), en mode plein sauf mention contraire. La **corrélation croisée**, la somme glissante des bibliothèques, ne le retourne pas, $(\mathbf{w} \star \mathbf{x})_i = \sum_u w_u\,x_{i+u}$, en mode valide sauf mention contraire ; sa fenêtre numéro $i$ est repérée par sa **première case**. Le mode « même taille » est celui de NumPy : les valeurs de la convolution pleine à partir de l'indice $\big\lfloor\frac{\min(n, k) - 1}{2}\big\rfloor$. $\tilde{\mathbf{w}}$ est le noyau retourné, $\check{\mathbf{h}}$ le noyau retourné circulaire. Un padding $p$ ajoute $p$ zéros **de chaque côté** ; le pas est $s$, la dilatation $d$. Une grille à plusieurs canaux a la forme $(C, H, W)$, et ses poids la forme $(C_{\text{out}}, C_{\text{in}}, k_h, k_w)$ ; le coût se compte en multiplications-additions, une par poids et par position de sortie. Les lignes et les colonnes d'une grille sont numérotées à partir de 0, comme dans NumPy. Une matrice s'écrit dans le notebook comme une liste de ses **lignes**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M21.Q1 — Convolution ou corrélation : retourner, glisser, sommer 🧠 ★ ⏱️ 4 min
*Fiche §1 et §2 · parcours C, E*

1. Le noyau retourné de $\mathbf{w} = (2, 0, -1, 5)$ ?
2. Vrai ou faux : avec le noyau $(2, 5, -5, -2)$, la convolution valide d'un signal est l'opposée de sa corrélation croisée.
3. $\mathbf{a}$ a 3 termes et $\mathbf{b}$ en a 5. Quels produits $a_ib_j$ additionne-t-on pour obtenir $(\mathbf{a} * \mathbf{b})_4$ ?
4. La longueur de la convolution pleine de deux suites de 7 et de 4 termes ?
5. On veut la somme glissante $y_i = 3x_i + x_{i+1} - x_{i+2}$. Quels poids donner à `np.correlate` ? Et à `np.convolve` ?
6. Vrai ou faux : la corrélation croisée de $\mathbf{x}$ par $\mathbf{w}$, en mode valide, est la convolution valide de $\mathbf{x}$ par $\tilde{\mathbf{w}}$.

### M21.Q2 — Les propriétés de la convolution : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Vrai ou faux : $\mathbf{a} * \mathbf{b} = \mathbf{b} * \mathbf{a}$ pour toutes suites finies.
2. La somme des termes de $(2, -1, 3) * (1, 4)$, sans calculer la convolution ?
3. Vrai ou faux : $\mathbf{a} * (\mathbf{b} + \mathbf{c}) = \mathbf{a} * \mathbf{b} + \mathbf{a} * \mathbf{c}$ (pour $\mathbf{b}$ et $\mathbf{c}$ de même longueur).
4. Vrai ou faux : la convolution de deux lois de probabilité (des suites positives ou nulles de somme 1) est encore une loi de probabilité.
5. Vrai ou faux : convoluer un signal par $(0, 0, 1)$ l'avance de 2 cases.
6. Sur une portion où un signal vaut constamment 5, que vaut sa convolution par le noyau $(0{,}5 ;\ 2 ;\ -1)$ ?

### M21.Q3 — Lire une matrice de Toeplitz : diagonales, coefficients non nuls, nombre de lignes 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

$$\mathbf{M} = \begin{pmatrix} 5 & 0 & 0 \\ -2 & 5 & 0 \\ 1 & -2 & 5 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}.$$

1. $\mathbf{M}$ est la matrice d'une convolution pleine $\mathbf{x} \mapsto \mathbf{x} * \mathbf{w}$ : quel noyau $\mathbf{w}$, et quelle longueur $n$ des signaux ?
2. Un noyau de 4 coefficients, tous non nuls, et des signaux de 50 valeurs : combien de coefficients non nuls a la matrice de la convolution pleine, et sur combien de coefficients en tout ?
3. Même noyau, mêmes signaux : combien de lignes a la matrice en mode valide ? En mode même taille ?
4. Vrai ou faux : $\begin{pmatrix} 4 & 1 & 0 \\ 1 & 4 & 1 \\ 0 & 2 & 4 \end{pmatrix}$ est une matrice de Toeplitz.
5. Vrai ou faux : $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 2 \\ 2 & 0 & 1 \end{pmatrix}$ est une matrice circulante. Si oui, de quelle première colonne ?
6. Le noyau $(w_0, w_1, w_2, w_3, w_4)$, en convolution pleine : quel coefficient se trouve en ligne 7 et en colonne 4 de la matrice ?

### M21.Q4 — Équivariant, invariant, ou ni l'un ni l'autre ? Décalages, bords, pas et pooling 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Les signaux sont indexés par tous les entiers et nuls hors d'un ensemble fini : il n'y a pas de bords (sauf au 6). Pour chaque application, réponds : équivariante par translation, invariante, ou ni l'un ni l'autre.

1. $F(\mathbf{x}) = \mathbf{x} * (1, 4, -2)$.
2. $F(\mathbf{x}) = \max_i x_i$, le maximum de tout le signal.
3. $F(\mathbf{x})_i = i\,x_i$ : chaque valeur multipliée par sa position.
4. $F(\mathbf{x}) = \sum_i x_i^2$, l'énergie du signal.
5. $F(\mathbf{x})_i = x_{3i}$ : on garde une valeur sur 3. De combien de cases la sortie bouge-t-elle quand on décale l'entrée de 6 cases ? Et, quand on la décale de 2 cases, la sortie est-elle un décalage de l'ancienne ?
6. Vrai ou faux : sur des signaux périodiques de période $n$, toute convolution circulaire commute avec le décalage circulaire, sans aucun effet de bord.

### M21.Q5 — Combien de positions ? Pas, dilatation, padding et insertion de zéros 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. $n = 40$, $k = 5$, sans padding, pas de 1 : le nombre de positions ?
2. $n = 41$, $k = 5$, pas $s = 2$, sans padding ?
3. $n = 41$, $k = 5$, dilatation $d = 3$, pas de 1, sans padding : l'étendue de la fenêtre, puis le nombre de positions ?
4. « Même taille » avec un pas de 1 et un noyau de longueur 11 : combien de zéros de chaque côté ?
5. On insère $s - 1 = 3$ zéros entre deux valeurs consécutives d'une suite de 6 valeurs : combien de valeurs obtient-on ?
6. Vrai ou faux : avec $n = 30$, $k = 5$, $s = 4$ et $p = 0$, la case 29 est lue par une fenêtre.

### M21.Q6 — Canaux, groupes, convolution 1 × 1 et noyaux séparables : compter 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

Une grille de mesures a $C_{\text{in}} = 10$ canaux ; on la filtre vers $C_{\text{out}} = 6$ canaux, avec des noyaux de $2 \times 4$ cases et un biais par sortie.

1. La forme des poids, et le nombre de paramètres ?
2. Le même filtrage en convolution groupée à $g = 2$ groupes : le nombre de paramètres ?
3. Une convolution par canal sur les 10 canaux, avec des noyaux $3 \times 3$ : le nombre de paramètres (biais compris) ?
4. Une convolution $1 \times 1$ de 10 vers 6 canaux : le nombre de paramètres, et le nombre de multiplications-additions par case de la grille ?
5. Un noyau séparable de $9 \times 9$ cases : combien de multiplications par valeur de sortie en direct, puis, environ, en deux passes ?
6. Vrai ou faux : $\begin{pmatrix} 2 & -4 & 6 \\ -1 & 2 & -3 \end{pmatrix}$ est un noyau séparable (au sens de la fiche : de rang 1).

### M21.Q7 — Composer des convolutions : noyau, pas et champ récepteur 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Les étages sont des sommes glissantes (sans retournement), sans padding.

1. Deux étages de pas 1, de noyaux de longueurs 5 et 8 : la longueur du noyau équivalent ?
2. Le noyau équivalent de $(3, 1)$ puis $(1, -2)$, tous deux de pas 1 ?
3. Trois étages de pas 2, 2 et 5 : le pas total ?
4. Trois étages identiques, $(k, s) = (2, 2)$ : le champ récepteur d'une sortie ?
5. Deux étages, $(k, s, d) = (4, 1, 1)$ puis $(3, 1, 5)$ : le champ récepteur ?
6. Vrai ou faux : échanger deux étages $(k, s) = (6, 2)$ et $(3, 1)$ ne change pas le champ récepteur.

### M21.Q8 — Le pire cas d'une perturbation bornée : quelle norme, quel vecteur ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

Un indicateur vaut $f(\mathbf{x}) = \mathbf{g} \cdot \mathbf{x}$, avec $\mathbf{g} = (1, -4, 2, 0, -2)$ ; chaque mesure $x_i$ peut être fausse de $\delta_i$.

1. Le plus grand écart $\mathbf{g} \cdot \boldsymbol{\delta}$ quand $\lVert\boldsymbol{\delta}\rVert_\infty \le 0{,}3$ ?
2. Un vecteur $\boldsymbol{\delta}$ qui l'atteint ? Est-il unique ?
3. Le plus grand écart si l'on sait seulement que $\lVert\boldsymbol{\delta}\rVert_2 \le 0{,}3$ ?
4. Et si $\lVert\boldsymbol{\delta}\rVert_1 \le 0{,}3$ (au plus 0,3 d'erreur en tout, réparties comme on veut) ?
5. Vrai ou faux : $\boldsymbol{\delta} = 0{,}3\,\mathbf{g}$ est le pire cas sur la boule L∞ de rayon 0,3.
6. Pour un $\mathbf{g}$ de $\mathbb{R}^{400}$ dont toutes les coordonnées valent $\pm 1$ : le rapport du pire écart sur la boule L∞ de rayon 0,3 au pire écart sur la boule L2 de même rayon ?

<a id="rappels"></a>

## 🔁 Rappels

### M21.R1 — La moyenne mobile d'une suite (R5) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

Les hauteurs de pluie de six jours consécutifs, en millimètres : $(12, 3, 9, 6, 0, 15)$.

1. Les moyennes mobiles sur 3 jours, $m_t = \frac{x_{t-2} + x_{t-1} + x_t}{3}$, pour $t = 2$ à $5$ ?
2. Combien de moyennes complètes pour une série de $n$ valeurs et une fenêtre de $k$ valeurs ?
3. Montre que $m_{t+1} - m_t = \frac{x_{t+1} - x_{t-2}}{3}$, et vérifie-le sur $m_3 - m_2$.
4. Avec quel noyau $\mathbf{h}$ la moyenne mobile s'écrit-elle $m_t = (\mathbf{x} * \mathbf{h})_t$ ?
5. Vrai ou faux : une moyenne mobile laisse une série constante inchangée (pour les moyennes complètes).

### M21.R2 — La matrice d'une application linéaire, son noyau et son rang (M12a) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

$f(x, y, z) = (x + 2y - z,\ 3y + z)$, de $\mathbb{R}^3$ dans $\mathbb{R}^2$.

1. La matrice de $f$ ?
2. Son rang ?
3. La dimension de son noyau, par le théorème du rang ?
4. Un vecteur non nul de son noyau ?
5. La colonne $j$ de la matrice est l'image de quel vecteur ?
6. Vrai ou faux : toute application linéaire de $\mathbb{R}^4$ dans $\mathbb{R}^2$ a un noyau non nul.

### M21.R3 — Le rang d'un produit extérieur u vᵀ et la décomposition en valeurs singulières (M12d) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C*

$\mathbf{u} = (6, 2, -3)$ et $\mathbf{v} = (4, 0, -3)$.

1. La matrice $\mathbf{u}\mathbf{v}^\top$ ?
2. Son rang ?
3. Sa seule valeur singulière non nulle ?
4. Ses vecteurs singuliers unitaires, au signe près ?
5. Vrai ou faux : une matrice dont toutes les lignes sont des multiples d'une même ligne non nulle est de rang 1.
6. Une matrice a pour valeurs singulières $7$ ; $0{,}002$ ; $0$. L'erreur de son meilleur approximant de rang 1, en norme de Frobenius ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une forme comme NumPy l'affiche, comme `(7, 2)` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- `True` ou `False` pour un vrai ou faux.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M21.1 — Deux dés truqués et un produit de polynômes : la même convolution ✏️ ★ ⏱️ 20 min
**Objectif :** calculer une convolution comme un produit de polynômes, puis la lire comme la loi de la somme de deux variables indépendantes.
**Prérequis :** fiche §1 ; R3, R8, M02b · **Parcours :** C, E

Le dé $A$ est un dé à six faces qui portent les numéros $1, 1, 1, 2, 2, 3$ : il donne 1, 2 et 3 avec les probabilités $\frac36$, $\frac26$ et $\frac16$. Le dé $B$ a huit faces, qui portent $1, 2, 3, 3, 4, 4, 4, 4$ : il donne 1, 2, 3 et 4 avec les probabilités $\frac18$, $\frac18$, $\frac28$ et $\frac48$. On les lance indépendamment, et $S = A + B$.

| | Question | Réponse attendue |
|---|---|---|
| a | les coefficients du produit $(3 + 2X + X^2)(1 + X + 2X^2 + 4X^3)$, du terme constant au terme de plus haut degré | une liste de 6 entiers |
| b | $P(S = 5)$ | une fraction irréductible, entre guillemets |
| c | $P(S \ge 6)$ | une fraction irréductible, entre guillemets |
| d | $\mathbb{E}[S]$ | une fraction irréductible, entre guillemets |
| e | l'indice $m$ du coefficient de a) qui, divisé par 48, donne $P(S = 5)$ | un entier |
| f | la valeur la plus probable de $S$ | un entier |
| g | on lance aussi un dé $A'$, pareil que $A$ et indépendant des deux autres : $P(A + B + A' \ge 9)$ | une fraction irréductible, entre guillemets |

Dans ta copie : écris le tableau à double entrée des produits $a_ib_j$, et entoure ses anti-diagonales. Pourquoi la somme des coefficients de a) vaut-elle $6 \times 8$ ? Pourquoi l'indice $m$ et la valeur de $S$ sont-ils décalés de 2 ? Vérifie d) par $\mathbb{E}[A] + \mathbb{E}[B]$. Pour g), quelle propriété de la convolution permet de partir de a) ?

### Ex M21.2 — Convoluer et corréler un signal à la main, dans les trois modes ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une corrélation croisée et une convolution dans les trois modes, et passer de l'une à l'autre par le noyau retourné.
**Prérequis :** fiche §2 · **Parcours :** C, E

$\mathbf{x} = (3, -2, 0, 5, 1, -4, 2)$ et $\mathbf{w} = (4, -1, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la corrélation croisée $\mathbf{w} \star \mathbf{x}$, en mode valide | une liste de 5 entiers |
| b | la convolution $\mathbf{x} * \mathbf{w}$, en mode plein | une liste de 9 entiers |
| c | la convolution $\mathbf{x} * \mathbf{w}$, en mode valide | une liste de 5 entiers |
| d | la convolution $\mathbf{x} * \mathbf{w}$, en mode même taille | une liste de 7 entiers |
| e | le noyau qu'il faut donner à une corrélation croisée pour obtenir c) | une liste de 3 entiers |
| f | vrai ou faux : a) et c) sont égales | `True` ou `False` |
| g | la somme des termes de b) | un entier |

Dans ta copie : pour une valeur de c), dessine le noyau retourné posé sous sa fenêtre du signal. Pourquoi d) commence-t-il à l'indice 1 de b) ? Retrouve g) sans additionner les termes de b). Quels noyaux de longueur 3 donneraient a) = c) pour tout signal ?

### Ex M21.3 — Des pochoirs de différences finies : dérivée et dérivée seconde d'un signal échantillonné ✏️ ★★ ⏱️ 15 min
**Objectif :** appliquer les pochoirs de la dérivée et de la dérivée seconde à un signal échantillonné, et mesurer leurs erreurs.
**Prérequis :** fiche §2 ; M05a · **Parcours :** C, E

Une cuve se remplit à débit croissant ; son volume, en litres, est relevé toutes les $h = 2$ minutes, aux instants $t = 0, 2, 4, 6, 8, 10$ : $\mathbf{f} = (0, 2, 16, 54, 128, 250)$. Ce sont les valeurs de $f(t) = t^3/4$.

| | Question | Réponse attendue |
|---|---|---|
| a | les différences avant $\frac{f_{i+1} - f_i}{h}$ | une liste de 5 nombres |
| b | les différences centrées $\frac{f_{i+1} - f_{i-1}}{2h}$, aux instants 2 à 8 | une liste de 4 nombres |
| c | les dérivées secondes $\frac{f_{i+1} - 2f_i + f_{i-1}}{h^2}$, aux instants 2 à 8 | une liste de 4 nombres |
| d | l'erreur de la différence centrée en $t = 4$ : la valeur de b) moins $f'(4)$ | un nombre |
| e | l'erreur (valeur approchée moins vraie valeur, comme en d)) de la différence avant $\frac{f(4) - f(2)}{2}$ comme approximation de $f'(2)$, puis comme approximation de $f'(3)$ | une liste de 2 nombres |
| f | vrai ou faux : `np.convolve(f, [-1, 0, 1], "valid") / 4` donne b) | `True` ou `False` |
| g | l'erreur de la différence centrée en $t = 4$ si l'on relevait le volume toutes les minutes ($h = 1$) | un nombre |

Dans ta copie : compare c) à $f''(t)$. Pourquoi la dérivée seconde est-elle exacte ici, et pas la différence centrée ? Exprime l'erreur de d) avec $h$ et $f'''$ (M05a), et retrouve g). Écris chacun des trois pochoirs comme une corrélation, puis comme le noyau à donner à `np.convolve`.

### Ex M21.4 — La matrice de Toeplitz d'une convolution pleine et d'une convolution valide : coefficients non nuls, rang et noyau ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire la matrice d'une convolution, compter ses coefficients non nuls, et lire son rang et son noyau.
**Prérequis :** fiche §3 ; M12a · **Parcours :** C, E

$\mathbf{w} = (1, -3, 2)$ et des signaux de longueur $n = 5$. On note $\mathbf{T}$ la matrice de $\mathbf{x} \mapsto \mathbf{x} * \mathbf{w}$ en mode plein, et $\mathbf{V}$ celle du mode valide.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice $\mathbf{T}$ | une matrice |
| b | le nombre de coefficients non nuls de $\mathbf{T}$ | un entier |
| c | $\mathbf{T}\mathbf{x}$ pour $\mathbf{x} = (2, 0, -1, 3, 1)$ | une liste de 7 entiers |
| d | la matrice $\mathbf{V}$ | une matrice |
| e | le rang de $\mathbf{V}$ | un entier |
| f | la dimension de $\ker\mathbf{V}$ | un entier |
| g | vrai ou faux : le signal $(1, 2, 4, 8, 16)$ est dans $\ker\mathbf{V}$ | `True` ou `False` |
| h | le rang de $\mathbf{T}$ | un entier |
| i | $\mathbf{V}^\top$ est la matrice d'une convolution pleine, sur des signaux de longueur 3 : par quel noyau ? | une liste de 3 entiers |

Dans ta copie : vérifie c) par un produit de polynômes. Écris l'équation $(\mathbf{V}\mathbf{x})_r = 0$ comme une récurrence d'ordre 2 et résous-la (M19 §6) : quels signaux ce filtre ne voit-il pas ? Donne une base de $\ker\mathbf{V}$. Que constates-tu avec h) : deux signaux différents peuvent-ils avoir la même convolution pleine par $\mathbf{w}$ ? (L'examen blanc CP5 propose de le démontrer.)

### Ex M21.5 — Décaler puis filtrer, ou filtrer puis décaler : l'équivariance, ses bords et son pas ✏️ ★★ ⏱️ 15 min
**Objectif :** vérifier l'équivariance sur un signal fini, voir ce que les bords en font, et ce que devient un décalage avec un pas.
**Prérequis :** fiche §4 · **Parcours :** C, E

Un capteur de vibrations enregistre un bref événement, $\mathbf{x} = (0, 0, 2, -1, 3, 0, 0, 0, 0, 0)$ ($n = 10$), qu'on filtre par la somme glissante de poids $\mathbf{w} = (1, -1, 2)$. On note $\tau_t\mathbf{x}$ le signal retardé de $t$ cases : $t$ zéros entrent à gauche, et les $t$ dernières valeurs sortent à droite.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{w} \star \mathbf{x}$, en mode valide | une liste de 8 entiers |
| b | $\mathbf{w} \star \tau_3\mathbf{x}$ | une liste de 8 entiers |
| c | le nombre de valeurs non nulles de a) perdues dans $\mathbf{w} \star \tau_5\mathbf{x}$ : celles qui, décalées de 5 cases, tomberaient au-delà de la dernière position | un entier |
| d | la sortie avec un pas de 2, $y_i = \sum_u w_u\,x_{2i+u}$ | une liste de 4 entiers |
| e | la même sortie avec un pas de 2, pour $\tau_1\mathbf{x}$ | une liste de 4 entiers |
| f | la même sortie avec un pas de 2, pour $\tau_4\mathbf{x}$ : de combien de positions de sortie est-elle décalée par rapport à d) ? | un entier |
| g | vrai ou faux : e) est un décalage de d) | `True` ou `False` |

Dans ta copie : montre sur a) et b) que décaler puis filtrer revient à filtrer puis décaler. Quelles valeurs de la réponse disparaissent avec $\tau_5$, et pourquoi ? Pourquoi d) est-il fait d'une valeur sur deux de a) ? Quelles valeurs de a) retrouves-tu dans e) ? Quels décalages de l'entrée décalent la sortie d) ?

### Ex M21.6 — Compter les positions d'une fenêtre : pas, dilatation, padding, « même taille » avec un pas, et le problème inverse ✏️ ★★ ⏱️ 25 min
**Objectif :** compter les positions d'une fenêtre dans tous les réglages, répartir le padding « même taille » avec un pas, et remonter d'un nombre de positions aux réglages.
**Prérequis :** fiche §5 ; R1 · **Parcours :** C, E

Un sismographe enregistre $n = 1\,000$ échantillons, que l'on parcourt par une fenêtre de $k = 7$ poids. Une position existe quand toute la fenêtre tient dans le signal complété.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de positions, sans padding, avec un pas de 1 | un entier |
| b | le nombre de positions avec un pas $s = 3$ et un padding $p = 2$ | un entier |
| c | le nombre de positions avec une dilatation $d = 4$, un pas de 1 et sans padding | un entier |
| d | le nombre de positions avec $d = 4$, $s = 5$ et $p = 3$ | un entier |

Une série de 365 températures moyennes journalières est lissée par une fenêtre d'une semaine ($k = 7$, $d = 1$) avec un pas $s = 3$, selon la règle « même taille » avec un pas de la fiche (§5 : $\lceil n/s\rceil$ positions, zéros répartis au début et à la fin).

| | Question | Réponse attendue |
|---|---|---|
| e | le nombre de positions | un entier |
| f | le nombre de zéros ajoutés au début, puis à la fin | une liste de 2 entiers |

Le problème inverse, sans padding et avec $d = 1$.

| | Question | Réponse attendue |
|---|---|---|
| g | toutes les longueurs $n$ de signal qui donnent exactement 50 positions avec $k = 5$ et $s = 5$, en ordre croissant | une liste d'entiers |
| h | le pas $s$ qui donne exactement 125 positions avec $n = 1\,000$ et $k = 7$ | un entier |

Dans ta copie : pour b), quelles cases du signal complété lit la dernière fenêtre, et l'une d'elles est-elle un zéro du padding ? Pour c), l'étendue de la fenêtre. Vérifie e) par la formule des positions, avec le nombre total de zéros à la place de $2p$. Pour g), pourquoi y a-t-il exactement $s$ longueurs ? Pour h), écris l'encadrement de $\frac{993}{s}$ qui donne la réponse, et explique pourquoi aucun autre pas ne convient.

### Ex M21.7 — Sous-échantillonner et insérer des zéros : la convolution transposée d'un signal et ses recouvrements ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer un sous-échantillonnage et sa transposée, puis une convolution transposée par sa matrice et par la recette « zéros insérés, puis convolution pleine », sa taille et ses recouvrements.
**Prérequis :** fiche §5 ; M09a · **Parcours :** C, E

Le sous-échantillonnage $\mathbf{D}_3$ garde une valeur sur 3 d'un signal de 7 valeurs : $(\mathbf{D}_3\mathbf{x})_i = x_{3i}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{D}_3\mathbf{x}$ pour $\mathbf{x} = (5, 1, 8, -2, 0, 4, 7)$ | une liste de 3 entiers |
| b | $\mathbf{D}_3^\top\mathbf{D}_3\mathbf{x}$ | une liste de 7 entiers |

La convolution transposée de $\mathbf{y} = (3, 2, -2)$ associée au noyau $\mathbf{w} = (2, 1, 3, -1, 1)$, avec un pas $s = 3$ et sans padding.

| | Question | Réponse attendue |
|---|---|---|
| c | sa taille | un entier |
| d | son résultat | une liste d'entiers |
| e | le nombre de tampons qui couvrent chaque case de d) | une liste d'entiers |
| f | les longueurs $n$ des signaux que la somme glissante de mêmes réglages ($k = 5$, $s = 3$, $p = 0$) envoie sur 3 positions, en ordre croissant | une liste d'entiers |
| g | la taille de la convolution transposée de c) avec un padding de sortie $p_{\text{out}} = 2$ | un entier |
| h | pour un noyau de longueur $k = 12$ et un pas $s = 4$ : le nombre de tampons qui couvrent chaque case intérieure | un entier |

Dans ta copie : écris la matrice $\mathbf{D}_3$. Pourquoi $\mathbf{D}_3^\top\mathbf{D}_3$ n'est-elle pas l'identité ? Écris la matrice $\mathbf{C}^\top$ ($11 \times 3$) de la convolution transposée : que sont ses colonnes ? Vérifie d) $= \mathbf{C}^\top\mathbf{y}$, puis retrouve-le par $\mathbf{D}_3^\top$ (a) et b) l'ont préparé) suivi de la convolution pleine par $\mathbf{w}$. Pourquoi e) est-il irrégulier, et h) régulier ? Relie f) à g).

### Ex M21.8 — Une carte de températures filtrée par un laplacien discret et par un lissage séparable ✏️ ★★ ⏱️ 30 min
**Objectif :** filtrer une grille de mesures par le laplacien discret, puis par un noyau séparable en deux passes, et compter les multiplications.
**Prérequis :** fiche §2 et §6 ; M12d · **Parcours :** C, E

Une carte de températures (°C) relevées sur une grille régulière de 4 lignes et 6 colonnes :
$$\mathbf{T} = \begin{pmatrix} 14 & 15 & 17 & 16 & 15 & 13 \\ 15 & 18 & 21 & 19 & 12 & 14 \\ 16 & 20 & 24 & 22 & 17 & 15 \\ 15 & 17 & 19 & 18 & 16 & 14 \end{pmatrix}.$$
On la filtre par le laplacien discret à 5 points de la fiche ($h = 1$), puis par le lissage $\mathbf{K} = \mathbf{a}\mathbf{a}^\top$, avec $\mathbf{a} = \frac15(1, 3, 1)$, tous deux en mode valide.

| | Question | Réponse attendue |
|---|---|---|
| a | la sortie du laplacien | une matrice $2 \times 4$ d'entiers |
| b | la position $[i, j]$ dans $\mathbf{T}$ de la case la plus « en creux » (le plus grand laplacien) | une liste de 2 entiers |
| c | la position $[i, j]$ dans $\mathbf{T}$ du sommet le plus marqué (le plus petit laplacien) | une liste de 2 entiers |
| d | la passe verticale : chaque colonne de $\mathbf{T}$ filtrée par $\mathbf{a}$, en mode valide | une matrice $2 \times 6$ (1 décimale) |
| e | la sortie du lissage $\mathbf{K}$ | une matrice $2 \times 4$ (2 décimales) |
| f | le nombre total de multiplications pour toute la sortie du lissage, en direct, puis en deux passes (la passe verticale d), puis la passe horizontale) | une liste de 2 entiers |
| g | vrai ou faux : le laplacien discret est un noyau séparable | `True` ou `False` |

Dans ta copie : écris $\mathbf{K}$ et calcule sa valeur $(0, 0)$ en direct, avec ses 9 produits. Pourquoi la corrélation et la convolution donnent-elles ici le même résultat ? Que vaut le laplacien d'une grille où toutes les températures sont égales ? Pour une grande carte, combien de multiplications par valeur de sortie coûtent environ les deux passes ?

### Ex M21.9 — Paramètres et coût d'un filtrage à plusieurs canaux : standard, groupé, par canal, 1 × 1 ✏️ ★★ ⏱️ 20 min
**Objectif :** compter les paramètres, le coût et la mémoire d'un filtrage à plusieurs canaux, dans ses quatre variantes.
**Prérequis :** fiche §6 ; M20 · **Parcours :** C, E

Un satellite fournit une grille de $200 \times 300$ pixels en $C_{\text{in}} = 12$ bandes spectrales. On la filtre vers $C_{\text{out}} = 20$ canaux, avec des noyaux $5 \times 5$, un padding de 2 (même taille), un pas de 1 et un biais par sortie ; les nombres sont stockés en `float32`, sur 4 octets.

| | Question | Réponse attendue |
|---|---|---|
| a | la forme des poids | une forme |
| b | le nombre de paramètres | un entier |
| c | le nombre de multiplications-additions | un entier |
| d | le nombre de paramètres du même filtrage en convolution groupée à $g = 4$ groupes | un entier |
| e | son nombre de multiplications-additions | un entier |
| f | le nombre de paramètres d'une convolution par canal, avec des noyaux $5 \times 5$ (12 sorties) | un entier |
| g | le nombre de paramètres d'une convolution $1 \times 1$ de 12 vers 5 canaux (cinq indices calculés en chaque pixel) | un entier |
| h | la forme de la sortie du filtrage standard avec un pas de 2 (même padding) | une forme |
| i | la mémoire occupée par la sortie du filtrage standard (pas de 1), en octets | un entier |

Dans ta copie : le coût de f) et de g). Pourquoi le nombre de paramètres ne dépend-il pas de la taille de la grille ? Que deviennent b) et c) pour une grille de $400 \times 600$ pixels ? Combien de multiplications-additions coûte une position de sortie ?

### Ex M21.10 — Le noyau équivalent de deux lissages successifs, et le champ récepteur d'une pile avec pas et dilatation ✏️ ★★ ⏱️ 20 min
**Objectif :** composer deux sommes glissantes en une seule, avec et sans pas, et calculer le champ récepteur d'une pile.
**Prérequis :** fiche §7 ; R4 · **Parcours :** C, E

On lisse une série par la moyenne de 2 valeurs, $\mathbf{a} = \frac12(1, 1)$, puis par la moyenne de 3 valeurs, $\mathbf{b} = \frac13(1, 1, 1)$ : deux sommes glissantes d'affilée, $\mathbf{y} = \mathbf{a} \star \mathbf{x}$ puis $\mathbf{z} = \mathbf{b} \star \mathbf{y}$, toutes deux de pas 1 sauf au c).

| | Question | Réponse attendue |
|---|---|---|
| a | $6\,\mathbf{K}$, où $\mathbf{K}$ est le noyau équivalent | une liste de 4 entiers |
| b | $\mathbf{z}$ pour $\mathbf{x} = (5, 9, 2, 8, 4, 10, 1)$ | une liste de 4 nombres (4 décimales) |
| c | $6\,\mathbf{K}$ quand le premier étage a un pas $s_1 = 3$ (le second, un pas de 1) | une liste d'entiers |
| d | le pas total de c) | un entier |

Une pile de trois étages, $(k, s, d) = (2, 2, 1)$, puis $(5, 4, 1)$, puis $(3, 1, 4)$.

| | Question | Réponse attendue |
|---|---|---|
| e | le champ récepteur d'une sortie de la pile | un entier |
| f | le pas total | un entier |
| g | les bornes du champ récepteur de la sortie $z_2$ : la première et la dernière case du signal d'origine que lisent ses calculs | une liste de 2 entiers |
| h | vrai ou faux : on obtient le champ récepteur en additionnant les étendues des trois fenêtres, $2 + 5 + 9$ | `True` ou `False` |

Dans ta copie : vérifie b) en appliquant $\mathbf{K}$ directement. Que calcule la pile de c), en mots ? Pour e), écris le tableau de la récurrence ($r_\ell$ et $J_\ell$ étage par étage). Pour g), pourquoi la sortie $z_j$ commence-t-elle à la case $Sj$ ?

### Ex M21.11 — Le pire cas d'une erreur de capteurs bornée : une forme linéaire sur les boules L∞ et L2 ✏️ ★ ⏱️ 15 min
**Objectif :** trouver le pire cas d'une forme linéaire sur les boules L∞, L2 et L1, et comparer ces pires cas.
**Prérequis :** fiche §8 ; M07, R2 · **Parcours :** C, E

Un débit est calculé à partir de cinq capteurs de pression : $f(\mathbf{x}) = -2x_0 + 5x_1 + x_2 - 3x_3 + x_4$. Chaque capteur est juste à $\varepsilon = 0{,}25$ kPa près : l'erreur $\boldsymbol{\delta}$ vérifie $\lvert\delta_i\rvert \le 0{,}25$ pour tout $i$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert\mathbf{g}\rVert_1$, avec $\mathbf{g}$ le vecteur des poids | un entier |
| b | le plus grand écart $f(\mathbf{x} + \boldsymbol{\delta}) - f(\mathbf{x})$ possible | un nombre |
| c | le vecteur $\boldsymbol{\delta}$ qui l'atteint | une liste de 5 nombres |
| d | le plus grand écart si l'on sait seulement que $\lVert\boldsymbol{\delta}\rVert_2 \le 0{,}25$ | un nombre (3 décimales) |
| e | la norme L2 du vecteur c) | un nombre (4 décimales) |
| f | le plus grand écart si l'on sait seulement que $\lVert\boldsymbol{\delta}\rVert_1 \le 0{,}25$ | un nombre |
| g | le plus grand écart possible sur une valeur du laplacien discret de M21.8 ($h = 1$), si chaque température est juste à 0,3 °C près | un nombre |
| h | $n = 2\,500$ mesures, une grandeur de poids tous égaux à $\pm 0{,}02$ : le pire écart quand chaque erreur vaut au plus 0,01 en valeur absolue, puis quand la norme L2 de l'erreur vaut au plus 0,01 | une liste de 2 nombres |

Dans ta copie : justifie b) coordonnée par coordonnée, et d) par Cauchy-Schwarz. Pourquoi la norme e) dépasse-t-elle 0,25 ? Pour f), quel vecteur atteint le pire cas ? Pour h), calcule $\lVert\mathbf{g}\rVert_1$ et $\lVert\mathbf{g}\rVert_2$, et compare leur rapport à $\sqrt n$.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M21.12 — La convolution est commutative et associative ; la corrélation croisée ne l'est pas ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer la commutativité et l'associativité de la convolution sur sa formule, puis montrer que la corrélation croisée n'a aucune des deux.
**Prérequis :** fiche §1 et §2 ; R4 · **Parcours :** C

Les suites sont finies, indexées à partir de 0 et nulles hors de leurs indices ; $\mathbf{a}$ a $n$ termes et $\mathbf{b}$ en a $k$. Pour comparer la corrélation croisée dans les deux sens, on la prend ici en **mode plein** : $\mathbf{a} \star \mathbf{b}$ fait glisser $\mathbf{a}$ sur $\mathbf{b}$ dans toutes les positions où ils se touchent, $(\mathbf{a} \star \mathbf{b})_m = \sum_t a_t\,b_{t + m - (n-1)}$, pour $m = 0, \ldots, n + k - 2$.

1. Montre que $\mathbf{a} * \mathbf{b} = \mathbf{b} * \mathbf{a}$, par le changement d'indice $j = m - i$. Explique pourquoi les deux sommes portent sur les mêmes couples d'indices.
2. Montre que $\big((\mathbf{a} * \mathbf{b}) * \mathbf{c}\big)_m = \sum_{i + j + l = m} a_i\,b_j\,c_l$, et déduis-en l'associativité.
3. Montre que le retourné d'une convolution est la convolution des retournés : $\widetilde{\mathbf{u} * \mathbf{v}} = \tilde{\mathbf{u}} * \tilde{\mathbf{v}}$.
4. Montre que $\mathbf{a} \star \mathbf{b} = \tilde{\mathbf{a}} * \mathbf{b}$, puis que $\mathbf{b} \star \mathbf{a} = \widetilde{\mathbf{a} \star \mathbf{b}}$. Trouve deux suites de longueur 2 telles que $\mathbf{a} \star \mathbf{b} \ne \mathbf{b} \star \mathbf{a}$.
5. Écris $(\mathbf{a} \star \mathbf{b}) \star \mathbf{c}$ et $\mathbf{a} \star (\mathbf{b} \star \mathbf{c})$ comme des convolutions de $\mathbf{a}$ ou $\tilde{\mathbf{a}}$, $\tilde{\mathbf{b}}$ et $\mathbf{c}$. Déduis-en un contre-exemple à l'associativité, avec des suites de longueur au plus 2.
6. Quand la corrélation croisée de deux suites est-elle égale à celle prise dans l'autre sens ? Qu'en retiens-tu pour la composition de deux sommes glissantes (fiche §7) ?

### Ex M21.13 — Les applications linéaires qui commutent avec le décalage circulaire sont les convolutions circulaires ; la transposée d'une matrice circulante ∂ ★★★ ⏱️ 30 min
**Objectif :** démontrer que l'équivariance caractérise les convolutions circulaires, et que la transposée d'une matrice circulante est la matrice circulante du noyau retourné circulaire.
**Prérequis :** fiche §4 ; M09a, M12a · **Parcours :** C

Les indices sont lus modulo $n$. $\mathbf{P}$ est le décalage circulaire, $(\mathbf{P}\mathbf{x})_i = x_{(i-1) \bmod n}$, $\mathbf{e}_0, \ldots, \mathbf{e}_{n-1}$ la base canonique de $\mathbb{R}^n$, et $\operatorname{circ}(\mathbf{h})$ la matrice de coefficients $h_{(i-j) \bmod n}$.

1. Montre que $\mathbf{P}\mathbf{e}_j = \mathbf{e}_{(j+1) \bmod n}$, puis que $\mathbf{e}_j = \mathbf{P}^j\mathbf{e}_0$ pour $j = 0, \ldots, n - 1$.
2. Montre que $(\mathbf{P}^j\mathbf{v})_i = v_{(i-j) \bmod n}$ pour tout vecteur $\mathbf{v}$ (par récurrence sur $j$).
3. Soit $\mathbf{A}$ une matrice $n \times n$ telle que $\mathbf{A}\mathbf{P} = \mathbf{P}\mathbf{A}$, et $\mathbf{h} = \mathbf{A}\mathbf{e}_0$ sa première colonne. Montre que $\mathbf{A}\mathbf{P}^j = \mathbf{P}^j\mathbf{A}$, puis que la colonne $j$ de $\mathbf{A}$ est $\mathbf{P}^j\mathbf{h}$. Conclus : $\mathbf{A} = \operatorname{circ}(\mathbf{h})$.
4. Réciproquement, montre que $\operatorname{circ}(\mathbf{h}) = \sum_{m=0}^{n-1} h_m\,\mathbf{P}^m$, puis que $\operatorname{circ}(\mathbf{h})$ commute avec $\mathbf{P}$.
5. Montre que $\operatorname{circ}(\mathbf{h})\,\mathbf{x} = \mathbf{x} \circledast \mathbf{h}$ pour tout $\mathbf{x}$ : les applications linéaires qui commutent avec le décalage circulaire sont exactement les convolutions circulaires.
6. Montre que $\operatorname{circ}(\mathbf{h})^\top = \operatorname{circ}(\check{\mathbf{h}})$, avec $\check h_m = h_{(-m) \bmod n}$. Pour $\mathbf{h} = (2, 7, 0, 1, 3)$, écris $\check{\mathbf{h}}$ et le simple renversement de $\mathbf{h}$ ; montre que le renversement est un décalage circulaire de $\check{\mathbf{h}}$, et dis lequel.

### Ex M21.14 — Le nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 quand la fenêtre tient, par un dénombrement ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule du nombre de positions en comptant les positions de départ possibles, et en tirer la règle « même taille » avec un pas.
**Prérequis :** fiche §5 ; R1 · **Parcours :** C, E

Un signal de longueur $n$ est complété par $p$ zéros de chaque côté ; une fenêtre de $k$ poids, de dilatation $d$, avance avec un pas $s$. La fenêtre numéro $i$ ($i \ge 0$) lit les cases $si, si + d, \ldots, si + d(k - 1)$ du signal complété. On pose $A = n + 2p - d(k - 1) - 1$, et l'on suppose $A \ge 0$.

1. Montre que la fenêtre $i$ existe si et seulement si $si + d(k - 1) \le n + 2p - 1$, c'est-à-dire $0 \le i \le \frac As$.
2. Montre que le nombre d'entiers $i$ de l'intervalle $[0, \frac As]$ est $\lfloor\frac As\rfloor + 1$ (R1), et conclus.
3. Que donne la formule quand $A < 0$ ? Distingue $-s \le A \le -1$ et $A < -s$. Pourquoi l'hypothèse est-elle nécessaire ?
4. Les réglages $k$, $s$, $p$, $d$ étant fixés, montre que deux longueurs $n$ et $n'$ donnent le même nombre de positions si et seulement si $\lfloor\frac As\rfloor = \lfloor\frac{A'}{s}\rfloor$, et que chaque nombre de positions est donné par exactement $s$ longueurs consécutives (tant que $A \ge 0$).
5. « Même taille » avec un pas : on pose $n_{\text{out}} = \lceil\frac ns\rceil$ et $P_{\text{tot}} = (n_{\text{out}} - 1)s + d(k - 1) + 1 - n$, supposé $\ge 0$. Montre qu'avec $P_{\text{tot}}$ zéros en tout (à la place de $2p$), la formule donne exactement $n_{\text{out}}$ positions, et que, si $P_{\text{tot}} \ge 1$, avec $P_{\text{tot}} - 1$ zéros elle en donne une de moins (utilise la question 3 si $n_{\text{out}} = 1$).

### Ex M21.15 — Le champ récepteur d'une pile de convolutions : récurrence et forme close ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer par récurrence la formule du champ récepteur d'une pile de sommes glissantes, et en tirer sa forme close.
**Prérequis :** fiche §7 ; R4 · **Parcours :** C

Une pile de $L$ sommes glissantes : l'étage $\ell$ a un noyau de $k_\ell$ poids non nuls, un pas $s_\ell$ et une dilatation $d_\ell$ ; sa sortie $j$ lit les sorties $s_\ell j + d_\ell u$ ($u = 0, \ldots, k_\ell - 1$) de l'étage précédent, l'étage 0 étant le signal d'origine. Une sortie **lit** une case du signal d'origine quand cette case intervient dans son calcul, par au moins une suite de lectures d'étage en étage ; son **champ récepteur** (fiche §7) est la plage des cases lues, de la première à la dernière, trous compris. On pose $r_0 = 1$, $J_0 = 1$, $r_\ell = r_{\ell-1} + d_\ell(k_\ell - 1)J_{\ell-1}$ et $J_\ell = J_{\ell-1}s_\ell$.

1. Montre par récurrence sur $\ell$ que la sortie $j$ de l'étage $\ell$ ne lit que des cases du signal d'origine comprises entre $J_\ell\,j$ et $J_\ell\,j + r_\ell - 1$, et qu'elle lit les deux cases extrêmes. (Pour l'étape de récurrence, regarde les sorties lues avec $u = 0$ et avec $u = k_\ell - 1$.) Pourquoi la sortie dépend-elle vraiment de ces deux cases extrêmes, c'est-à-dire avec un coefficient non nul ?
2. Montre que $J_\ell = s_1s_2\cdots s_\ell$.
3. Déduis-en la forme close $r_L = 1 + \sum_{\ell=1}^{L} d_\ell(k_\ell - 1)\,s_1\cdots s_{\ell-1}$ (une somme télescopique).
4. Pour $L$ étages identiques de noyaux de longueur 4, de pas 2 et sans dilatation, calcule $r_L$ en fonction de $L$, et calcule aussi $J_L$. Pour $L = 6$, combien de cases ont en commun les champs récepteurs de deux sorties voisines ? Vers quoi tend $r_L/J_L$, et que veut dire ce nombre pour les lectures ?
5. Avec $d_1 = 3$ et $k_1 = 2$ (un seul étage), le champ récepteur couvre 4 cases : combien de cases la sortie lit-elle vraiment ? Montre que, si $d_\ell J_{\ell-1} \le r_{\ell-1}$ à chaque étage, la sortie lit **toutes** les cases de son champ récepteur.

### Ex M21.16 — Le maximum d'une forme linéaire sur une boule L∞ vaut ε‖g‖₁, atteint en ε signe(g) ∂ ★ ⏱️ 10 min
**Objectif :** démontrer le résultat du §8 sur la boule L∞, et le comparer à celui de la boule L2.
**Prérequis :** fiche §8 ; M07, R2 · **Parcours :** C

Soit $\mathbf{g} \in \mathbb{R}^n$ et $\varepsilon > 0$.

1. Montre que, pour tout $\boldsymbol{\delta}$ tel que $\lVert\boldsymbol{\delta}\rVert_\infty \le \varepsilon$, $\mathbf{g} \cdot \boldsymbol{\delta} \le \varepsilon\lVert\mathbf{g}\rVert_1$.
2. Montre que $\boldsymbol{\delta}^\star = \varepsilon\operatorname{signe}(\mathbf{g})$ est dans la boule et atteint cette borne. Que se passe-t-il pour une coordonnée $g_i = 0$ ?
3. Déduis-en le minimum de $\mathbf{g} \cdot \boldsymbol{\delta}$ sur la boule, et la majoration $\lvert\mathbf{g} \cdot \boldsymbol{\delta}\rvert \le \varepsilon\lVert\mathbf{g}\rVert_1$.
4. Montre que, si aucune coordonnée de $\mathbf{g}$ n'est nulle, $\boldsymbol{\delta}^\star$ est le seul vecteur de la boule qui atteint le maximum.
5. Sur la boule L2 de même rayon, le maximum vaut $\varepsilon\lVert\mathbf{g}\rVert_2$ (fiche §8, Cauchy-Schwarz). Montre que $\varepsilon\lVert\mathbf{g}\rVert_2 \le \varepsilon\lVert\mathbf{g}\rVert_1 \le \varepsilon\sqrt n\,\lVert\mathbf{g}\rVert_2$, et dis quand la seconde inégalité est une égalité.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M21.17 — Pont : filtrer une grille à trois canaux comme les bibliothèques, formes (C, H, W), poids (C_out, C_in, k, k), et sans retournement 🔗 ★ ⏱️ 25 min
**Objectif :** calculer à la main une sortie d'un filtrage à plusieurs canaux, avec les formes et la convention (sans retournement) des bibliothèques, et voir le décalage du « même taille » pour un noyau de longueur paire.
**Prérequis :** fiche §2 et §6 ; M20 · **Parcours :** C, E

Des capteurs agricoles couvrent une parcelle découpée en une grille de 4 lignes et 5 colonnes ; en chaque case, trois mesures (température, humidité du sol, ensoleillement, ramenées à des entiers). Comme les bibliothèques, on range les canaux en premier : $\mathbf{X}$ a pour canaux
$$\mathbf{X}_0 = \begin{pmatrix} 2 & 1 & 0 & 3 & 1 \\ 0 & 4 & 2 & 1 & 3 \\ 1 & 2 & 5 & 0 & 2 \\ 3 & 0 & 1 & 2 & 4 \end{pmatrix}, \quad \mathbf{X}_1 = \begin{pmatrix} 1 & 0 & 2 & 2 & 0 \\ 3 & 1 & 0 & 4 & 1 \\ 2 & 2 & 1 & 0 & 3 \\ 0 & 1 & 3 & 1 & 2 \end{pmatrix}, \quad \mathbf{X}_2 = \begin{pmatrix} 0 & 2 & 1 & 1 & 4 \\ 1 & 0 & 3 & 2 & 0 \\ 4 & 1 & 0 & 2 & 1 \\ 2 & 3 & 1 & 0 & 1 \end{pmatrix}.$$
Le filtrage a deux sorties. La sortie 0 applique aux canaux 0, 1 et 2 les noyaux $2 \times 2$
$$\begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix}, \quad \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \quad \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}, \quad \text{biais } b_0 = 1 ;$$
la sortie 1, les noyaux
$$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}, \quad \begin{pmatrix} -1 & 0 \\ 0 & 2 \end{pmatrix}, \quad \text{biais } b_1 = -2.$$
Le filtrage est la somme glissante des bibliothèques (fiche §6), en mode valide, avec un pas de 1.

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{X}$ | une forme |
| b | la forme du tableau des poids $\mathbf{W}$ | une forme |
| c | la forme de la sortie $\mathbf{Y}$ | une forme |
| d | le nombre de paramètres, biais compris | un entier |
| e | $Y_{0,0,0}$ | un entier |
| f | $Y_{1,2,3}$ | un entier |
| g | le noyau à donner à `scipy.signal.convolve2d`, qui retourne son noyau selon les deux axes (une convolution 2D), pour retrouver la contribution du canal 0 à la sortie 0 | une matrice $2 \times 2$ |
| h | le nombre de multiplications-additions pour toute la sortie | un entier |

En une dimension, un noyau de longueur paire : $\mathbf{x} = (4, 1, 3, 2, 5)$ et la somme glissante $y_i = x_i + 4x_{i+1}$.

| | Question | Réponse attendue |
|---|---|---|
| i | la sortie « même taille » de PyTorch (`padding="same"`, qui met le zéro en trop à droite) | une liste de 5 entiers |
| j | ce que rend `np.convolve(x, [4, 1], "same")` | une liste de 5 entiers |

Dans ta copie : écris $Y_{0,0,0}$ comme une triple somme. Pourquoi faut-il donner à `np.convolve` les poids dans l'ordre $(4, 1)$, et non $(1, 4)$ ? De combien de cases i) et j) sont-elles décalées, et de quel côté est le zéro en trop dans chacune ?

### Ex M21.18 — Expliquer avec une règle graduée et un pochoir pourquoi une convolution est équivariante, mais pas invariante 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule ce qu'est l'équivariance par translation, et la distinguer de l'invariance.
**Prérequis :** fiche §4 · **Parcours :** C, E

Une amie relève chaque jour la hauteur d'une rivière le long d'une règle graduée posée sur la berge, et cherche les crues brèves avec un pochoir : une bande de carton percée de trois trous, qu'elle fait glisser le long de ses relevés, en notant à chaque position un score calculé avec les trois valeurs qu'elle voit. Elle te demande : « Si la même crue arrive trois jours plus tard, mon score change-t-il ? »

Réponds-lui en 6 à 10 phrases, sans formule : ce que fait le pochoir à chaque position, pourquoi les mêmes trous servent partout, ce que devient la liste des scores quand la crue arrive plus tard, ce que voudrait dire « invariant » pour cette liste et pourquoi elle ne l'est pas, et ce qui se passe quand la crue touche le bout de ses relevés. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M21.E1 — « Pourquoi une convolution est-elle une matrice de Toeplitz, et pourquoi ne la forme-t-on jamais ? » 💼 ★ ⏱️ 10 min
*Fiche §3 · parcours C*

« Pourquoi une convolution est-elle une matrice de Toeplitz, et pourquoi ne la forme-t-on jamais ? »

Ta réponse doit dire pourquoi la convolution par un noyau fixé est linéaire, ce que contient chaque colonne de sa matrice et pourquoi ses diagonales sont constantes, combien de ses coefficients sont non nuls, ce que coûterait le produit par la matrice pleine, comment le calcul se fait en vrai (des boucles, la matrice des fenêtres, la transformée de Fourier pour les longs noyaux), et à quoi la matrice sert quand même (le rang, le noyau, la transposée).

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m21_convolution/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus. Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir ; les décimales demandées ci-dessous sont celles à écrire dans ta copie. Les docstrings de `convolve` et de `circular_convolve` notent $k$ l'indice de sortie ; ici, comme dans la fiche, $k$ est la longueur du noyau.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M21.19 | La convolution de deux suites, dans les trois modes · `convolve` | 🔨 | ★★ | 30 | C, E |
| M21.20 | La matrice de Toeplitz d'une convolution · `toeplitz_matrix` | 🔨 | ★★ | 25 | C, E |
| M21.21 | La convolution circulaire · `circular_convolve` | 🔨 | ★ | 20 | C |
| M21.22 | Reconnaître un noyau séparable et le factoriser · `separable_factors` | 🔨 | ★★ | 25 | C |
| M21.23 | Le noyau équivalent et le pas d'une pile de sommes glissantes · `equivalent_kernel` | 🔨 | ★★ | 30 | C, E |
| M21.24 | Prédire l'effet d'un décalage de l'entrée sur un filtrage avec pas, puis vérifier | 🔮 | ★ | 15 | C, E |
| M21.25 | Le coût d'un filtrage direct ou séparable, selon la taille du noyau : mesurer, puis comparer à k² et 2k | 🔬 | ★★ | 30 | C |
| M21.26 | La carte des recouvrements d'une convolution transposée : un damier ou pas, selon k et s | 🎨 | ★ | 15 | C, E |
| M21.27 | Chasse à l'erreur : un noyau non retourné, des recouvrements supposés réguliers, un noyau de rang 2 « séparé » | 🐛 | ★ | 25 | C, E |
| M21.28 | Un test de propriété : la matrice de Toeplitz fois x égale la convolution, pour des longueurs tirées au hasard | 🛠️ | ★ | 20 | C |
| M21.29 | Défi : retrouver un noyau inconnu à partir d'un signal et de sa version filtrée bruitée, par les moindres carrés | 🏆 | ★★★ | 25 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les cinq 🔨 complètent ta copie `mon_travail/mymath/convolution.py` (**mymath :** `convolution.py`), dont la docstring du module dit ce qui est permis : NumPy, sauf `np.convolve`, `np.correlate`, `np.polymul`, `np.polynomial` et `np.fft`, aucune fonction de SciPy, et, de `np.linalg`, seulement `svd`, dans `separable_factors`. Chaque 🔨 lance ensuite le groupe de tests de sa fonction dans `tests/test_m21_convolution.py`, puis s'en sert.

**M21.19 · 🔨 `convolve(a, b, mode="full")`.** Écris la convolution des mathématiciens dans les trois modes (la docstring fixe les lignes gardées par « valid » et « same »), puis lance le groupe de tests `convolve`. Ensuite, avec ta fonction : a) la probabilité que trois dés équilibrés à 8 faces (numérotées de 1 à 8, lancés indépendamment) totalisent 11, en fraction irréductible ; b) le coefficient de $X^5$ dans $(2 - X)^7$, par sept convolutions successives ; c) la première valeur du mode même taille de la moyenne mobile sur 5 jours (un noyau de cinq valeurs égales à 0,2) des températures $(8, 10, 13, 15, 14, 12, 11, 9, 7, 6, 8, 10)$ ; d) le nombre de valeurs de ce mode même taille qui sont des moyennes de 5 vraies mesures. Ce qu'il faut observer : les valeurs du bord du mode même taille sont tirées vers 0 par les zéros ajoutés.

**M21.20 · 🔨 `toeplitz_matrix(kernel, n, mode="full")`.** Écris la matrice de $\mathbf{x} \mapsto$ `convolve(x, kernel, mode)` (colonne $j$ : le noyau descendu de $j$ lignes, puis les lignes du mode), puis lance le groupe de tests `toeplitz_matrix`. Ensuite : a) les rangs des matrices pleine et valide du noyau $(1, -3, 2)$ de M21.4 pour $n = 6$ (avec `np.linalg.matrix_rank`) ; b) le pourcentage de coefficients non nuls de la matrice pleine d'un noyau de 7 coefficients non nuls, pour $n = 1\,000$ (3 décimales) ; c) trois vrai ou faux sur l'énoncé de la transposée (fiche §3) : la transposée de la matrice valide de $\mathbf{w} = (1, 4, -2, 3)$ pour $n = 7$ est la matrice pleine de $\tilde{\mathbf{w}}$ (pour $n = 4$) ; la transposée de sa matrice même taille ($n = 7$) est la matrice même taille de $\tilde{\mathbf{w}}$ ; la même chose pour $\mathbf{w} = (2, 0, -1, 5, 1)$. Ce qu'il faut observer : la transposition échange valide et plein, et ne garde le mode même taille que pour un noyau de longueur impaire.

**M21.21 · 🔨 `circular_convolve(a, b)`.** Écris la convolution circulaire de deux suites de même longueur, puis lance le groupe de tests `circular_convolve`. Ensuite, le profil moyen d'une journée, une température (°C) par heure de 0 h à 23 h : $(9, 8, 8, 7, 6, 7, 8, 10, 12, 14, 16, 17, 19, 20, 21, 20, 18, 16, 14, 13, 12, 11, 10, 9)$ ; l'heure 24 est l'heure 0. On le lisse par la moyenne circulaire centrée sur 3 heures, le noyau $\mathbf{h}$ de 24 valeurs nulles sauf $h_0 = h_1 = h_{23} = \frac13$. a) La valeur lissée à 0 h (4 décimales) ; b) l'heure du maximum lissé ; c) vrai ou faux : en complétant $(3, -1, 2, 5)$ et $(1, 2, -2)$ par des zéros jusqu'à la longueur 6, la convolution circulaire donne la convolution pleine ; d) pour $\mathbf{h} = (5, -2, 0, 3, 1, 4)$, en construisant $\operatorname{circ}(\mathbf{h})$ colonne par colonne avec ta fonction : deux vrai ou faux, $\operatorname{circ}(\mathbf{h})^\top = \operatorname{circ}(\check{\mathbf{h}})$, puis $\operatorname{circ}(\mathbf{h})^\top$ égale la matrice circulante du simple renversement de $\mathbf{h}$.

**M21.22 · 🔨 `separable_factors(kernel, tol=1e-10)`.** Écris la factorisation d'un noyau de rang 1 par la décomposition en valeurs singulières (M12d), avec la convention de signe et la tolérance relative de la docstring, puis lance le groupe de tests `separable_factors`. Ensuite : a) le facteur $\mathbf{v}$ du lissage $\mathbf{K}$ de M21.8 (4 décimales) ; b) le rapport $s_2/s_1$ des valeurs singulières de la moyenne en croix $\frac15\begin{pmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{pmatrix}$ (3 décimales), et ce que rend ta fonction pour ce noyau ; c) un noyau presque séparable, le produit extérieur de $(1, 2, 4, 2, 1)$ et de $(2, -1, 3)$, plus un bruit gaussien d'écart type 0,001 (graine 5532) : avec la tolérance par défaut, ta fonction rend `None` ; avec une tolérance de $10^{-2}$, elle rend deux facteurs ; l'erreur $\lVert\mathbf{K} - \mathbf{u}\mathbf{v}^\top\rVert_F$ de cette approximation (5 décimales). Ce qu'il faut observer : cette erreur est $\sqrt{s_2^2 + s_3^2}$, comme le dit Eckart-Young (M12d).

**M21.23 · 🔨 `equivalent_kernel(kernels, strides=None)`** (avec ta `convolve`). Écris le noyau équivalent et le pas total d'une pile de sommes glissantes (fiche §7 : le noyau de l'étage $\ell$, dilaté du pas accumulé, convolué avec le noyau des étages précédents), puis lance le groupe de tests `equivalent_kernel`. Ensuite : a) $6\,\mathbf{K}$ pour la pile de M21.10 c) ; b) la longueur du noyau équivalent et le pas total de quatre étages identiques de noyaux de longueur 4 et de pas 2 ; c) le champ récepteur de la pile de M21.10 e), en écrivant le troisième étage, dilaté, comme le noyau à trous $(w_0, 0, 0, 0, w_1, 0, 0, 0, w_2)$ ; d) une pile tirée au hasard (graine 5533 : des noyaux de longueurs 3, 4 et 2, de pas 2, 3 et 1, et un signal de 200 valeurs), appliquée étage par étage, puis par son noyau équivalent avec le pas total : vrai ou faux, les deux sorties coïncident à $10^{-12}$ près (sur les positions communes).

**M21.24 · 🔮 Prédire l'effet d'un décalage de l'entrée sur un filtrage avec pas, puis vérifier.** Un signal de 30 valeurs, nul sauf $x_7 = 2$, $x_8 = 5$, $x_9 = -1$, est filtré par la somme glissante de poids $(1, -1, 2, 1)$ avec un pas de 3, en mode valide (9 positions). On le retarde de $t$ cases ($t$ zéros entrent à gauche). **Avant d'exécuter**, prédis : a) pour $t = 3$, de combien de positions de sortie la sortie est décalée ; b) pour $t = 6$ ; c) vrai ou faux : pour $t = 1$, la sortie est un décalage de la sortie d'origine ; d) la même question pour $t = 2$ ; e) les 9 valeurs de la sortie pour $t = 1$, calculées à la main. Puis vérifie avec ta `convolve` (une somme glissante est une convolution valide par le noyau retourné, dont on garde une valeur sur 3). Ce qu'il faut observer : seuls les décalages multiples du pas décalent la sortie ; les autres font lire au filtre d'autres paquets de valeurs, et la sortie change de nombres, pas seulement de place.

**M21.25 · 🔬 Le coût d'un filtrage direct ou séparable, selon la taille du noyau.** Une grille de $360 \times 360$ valeurs tirées au hasard (graine 5535) est filtrée, en mode valide, par des noyaux de rang 1, $\mathbf{K} = \mathbf{a}\mathbf{b}^\top$, de taille $k \times k$ pour $k = 3, 5, 9, 15, 25$. Écris deux fonctions : le filtrage direct, qui ajoute $k^2$ tranches décalées de la grille multipliées par $K_{u,v}$, et le filtrage séparable, qui fait $k$ tranches le long des colonnes avec $\mathbf{a}$, puis $k$ le long des lignes avec $\mathbf{b}$. Mesure leurs temps (`time.perf_counter`, le meilleur de 3 essais), trace-les contre $k$ en échelles logarithmiques, ainsi que leur rapport à côté de $k/2$. a) Le nombre de multiplications par valeur de sortie pour $k = 25$, selon les comptes de la fiche ($k_hk_w$ en direct, environ $k_h + k_w$ en deux passes) ; b) le rapport mesuré des temps pour $k = 25$ est le plus proche, en ordre de grandeur (sur une échelle logarithmique), de : (A) 2 ; (B) 12,5 ; (C) 625 ; c) vrai ou faux : les deux sorties coïncident à $10^{-9}$ près. Ce qu'il faut conclure : le séparable gagne un facteur de l'ordre de $k/2$, peu de chose pour $k = 3$, beaucoup pour un grand noyau. (La transformée de Fourier, qui accélère encore les très grands noyaux, n'est qu'évoquée dans la fiche, §4.)

**M21.26 · 🎨 La carte des recouvrements d'une convolution transposée.** Pour une entrée de $6 \times 6$ valeurs et des noyaux $k \times k$ de pas $s$ selon les deux axes, compte, en chaque case de la sortie, le nombre de tampons qui la couvrent (en 2D, c'est le produit des comptes des deux axes), pour $(k, s) = (5, 2)$, $(6, 2)$, $(7, 3)$ et $(9, 3)$, et dessine les quatre cartes côte à côte, avec une barre de couleurs et un titre qui donne $(k, s)$. Ce qu'il faut observer : un damier de cases fortes et faibles quand $s$ ne divise pas $k$, une carte uniforme à l'intérieur quand $s$ divise $k$.

**M21.27 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe. (1) `poly_product(p, q)` doit rendre les coefficients du produit de deux polynômes (du terme constant au plus haut degré) ; elle renvoie `np.correlate(p, q, "full")`, et il l'a vérifiée sur $(1 + 2X)(2 + 5X + 2X^2)$, dont le second facteur a des coefficients palindromes. Il l'applique à $(1 + 2X)(3 - X + 4X^2)$. (2) `n_covers(k, s)` doit rendre le nombre de tampons qui couvrent une case intérieure d'une convolution transposée de noyau de longueur $k$ et de pas $s$ ; elle renvoie `k // s`, et il l'a vérifiée sur $(k, s) = (6, 3)$, $(8, 2)$ et $(12, 4)$. (3) `separate(K)` rend la première colonne de $\mathbf{K}$ et sa première ligne divisée par $K_{0,0}$, sans regarder le rang ; il l'a vérifiée sur un produit extérieur, et l'applique au noyau $\begin{pmatrix} 2 & 1 & 3 \\ 4 & 2 & 5 \\ 2 & 1 & 3 \end{pmatrix}$. Trouve et corrige chaque erreur, puis réponds : a) les coefficients de $(1 + 2X)(3 - X + 4X^2)$, avec la fonction corrigée ; b) pour une convolution transposée de noyau de longueur $k = 8$, de pas $s = 3$ et de $m = 6$ valeurs d'entrée, les nombres de tampons qui couvrent les cases 9, 10 et 11 ; c) le plus grand écart, en valeur absolue, entre $\mathbf{K}$ et le produit extérieur des deux facteurs de `separate` ; d) vrai ou faux : `separable_factors` rend `None` pour ce noyau ; e) une question à part, sur le mode « même taille » d'un noyau de longueur paire, où NumPy et PyTorch diffèrent d'une case : pour la somme glissante de poids $(2, -3)$ et $\mathbf{x} = (6, 2, 7, 1, 8, 3)$, ce que rend `np.convolve` en mode même taille, avec les poids retournés. Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas.

**M21.28 · 🛠️ Un test de propriété.** Écris une fonction de test qui tire au hasard (graine 5538), 200 fois, une longueur de noyau $k$ de 1 à 6, une longueur de signal $n$ de $k$ à 12, un noyau et un signal d'entiers, et vérifie que `toeplitz_matrix(w, n, mode) @ x` égale `convolve(x, w, mode)` dans les trois modes, avec un message d'échec qui dit d'abord ce qui était attendu, puis le cas fautif ($k$, $n$, le mode). Ajoute les cas limites $k = 1$ et $n = k$. Lance-la sur ta librairie, puis sur une version volontairement fausse, fournie, dont le mode même taille garde les lignes à partir de $\lfloor k/2\rfloor$ au lieu de $\lfloor\frac{k-1}{2}\rfloor$ : ton test doit l'attraper, et son message doit montrer un noyau de longueur paire.

**M21.29 · 🏆 Défi : retrouver un noyau inconnu.** Un capteur a été filtré par une somme glissante de 7 poids inconnus, puis bruité : le notebook tire (graine 5539) les poids secrets, un signal $\mathbf{x}$ de 2 000 valeurs gaussiennes, et la sortie $\mathbf{y} = \mathbf{w} \star \mathbf{x} + 0{,}05\,\boldsymbol{\eta}$ (1 994 valeurs, $\boldsymbol{\eta}$ gaussien). Retrouve $\mathbf{w}$ par les moindres carrés (M09b), avec ta `toeplitz_matrix` : les lignes $k - 1$ à $n - 1$ de la matrice pleine de $\mathbf{x}$ (comme noyau, pour des signaux de longueur 7) envoient $\tilde{\mathbf{w}}$ sur $\mathbf{w} \star \mathbf{x}$ (ou la matrice des fenêtres de la fiche §3, qui envoie $\mathbf{w}$ sur $\mathbf{w} \star \mathbf{x}$), puis `np.linalg.lstsq`. **Critère de réussite :** a) ton estimation, arrondie à 2 décimales, redonne exactement les 7 poids secrets. Puis : b) l'écart type du bruit estimé par $\frac{\lVert\mathbf{y} - \mathbf{X}_{\text{f}}\hat{\mathbf{w}}\rVert}{\sqrt{1\,994 - 7}}$ (2 décimales) ; c) le plus petit nombre $m$ de valeurs de $\mathbf{y}$, parmi 10, 20, 50, 100, 200 et 500 (les $m$ premières, avec leurs fenêtres), pour lequel l'estimation a tous ses poids à moins de 0,025 des poids secrets.
