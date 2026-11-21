# M28 · Matrice de Gram, montée sur l'entrée et lois tronquées — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M28.Q1 — Matrice de Gram : XXᵀ ou XᵀX, laquelle former, sa diagonale, et les distances qu'on y lit

<details><summary>Indice 1</summary>

Fiche §1 : « Deux lectures », « Diviser par le nombre d'échantillons », « Ce que coûte une matrice de Gram » ; §2 : « Des longueurs, des angles, des distances » et l'invariance.

</details>
<details><summary>Indice 2</summary>

$\mathbf{X}\mathbf{X}^\top$ est $n \times n$ et coûte de l'ordre de $n^2d$ multiplications ; $\mathbf{X}^\top\mathbf{X}$ est $d \times d$ et en coûte $d^2n$. $\lVert\mathbf{x}  _i - \mathbf{x}  _j\rVert^2 = G  _{ii} + G  _{jj} - 2G _{ij}$ et $\cos\theta _{ij} = G _{ij}/\sqrt{G  _{ii}G _{jj}}$. Une matrice de Gram est semi-définie positive.

</details>
<details><summary>Indice 3</summary>

1. Ici $n = 30$ et $d = 10^5$ : compare $n^2d$ et $d^2n$. 2. $9 + 16 - 12$, et $\frac{6}{3 \times 4}$. 3. Essaie deux points et une translation, et compare les normes. 4. Cherche une matrice $2 \times 2$ à coefficients positifs dont le déterminant est négatif. 5. Ce sont les colonnes qui sont les échantillons.

</details>

### M28.Q2 — Monter sur l'entrée : pas normalisé, projection sur un pavé, coordonnées gelées, point d'arrivée

<details><summary>Indice 1</summary>

Fiche §3 : « Le pas normalisé », « Rester dans un pavé », « Geler des coordonnées », puis « Une fonction convexe sur un pavé » et le ⚠️.

</details>
<details><summary>Indice 2</summary>

$\operatorname{rms}(\mathbf{g}) = \sqrt{\frac1n\sum_ig_i^2}$ ; $\operatorname{sign}$ se prend coordonnée par coordonnée, et $\operatorname{sign}(0) = 0$. La montée projetée coupe le **point** après le pas. $\mathbf{P}_F$ met à 0 les coordonnées gelées.

</details>
<details><summary>Indice 3</summary>

1. $\lVert\mathbf{g}\rVert = 17$ et $\operatorname{rms}(\mathbf{g}) = 8{,}5$ ; deux de ces vecteurs sont des multiples positifs de $\mathbf{g}$. 2. Calcule $\mathbf{x} + 0{,}5\thinspace\mathbf{g}$, puis ramène chaque coordonnée dans $[0, 1]$. 3. Garde la première et la troisième coordonnée de $\mathbf{g}$. 4. Relis l'exemple du drone. 5. Que devient la longueur du pas quand $\mathbf{g}$ tend vers $\mathbf{0}$ ?

</details>

### M28.Q3 — Variation totale et fréquences spatiales : quel motif coûte le plus, lequel traverse un flou ?

<details><summary>Indice 1</summary>

Fiche §4 : la définition de la variation totale, « Un motif périodique est un vecteur propre du laplacien », « Le gain d'un flou », le repliement, et le ⚠️ du §5.

</details>
<details><summary>Indice 2</summary>

Le rapport $\mathrm{VT}/\lVert\mathbf{x}\rVert^2$ d'un motif de fréquence $f$ vaut $4\sin^2(\pi f)$ sur un anneau ; le gain de la moyenne mobile de trois cases vaut $\frac{1 + 2\cos(2\pi f)}{3}$. Les fréquences $f$ et $1 - f$ donnent les mêmes échantillons.

</details>
<details><summary>Indice 3</summary>

1. Les différences valent $3, -1, 0, -3$. 2. et 3. Pour la période 2, $f = \frac12$ : le rapport vaut 4 et le gain $-\frac13$ ; fais de même pour les périodes 4 et 10, puis compare. 4. $1 - \frac58$, puis l'inverse. 5. Relis le ⚠️ du §5.

</details>

### M28.Q4 — Température, top-k et top-p : ce qui change l'ensemble gardé, ce qui ne change que les probabilités

<details><summary>Indice 1</summary>

Fiche §5 : les propriétés de la température, « Tronquer, c'est conditionner », « Température et troncatures ».

</details>
<details><summary>Indice 2</summary>

La température élève les rapports $p_i/p_j$ à la puissance $\frac1T$ : l'ordre ne change pas, et les zéros restent nuls ; à $T = \infty$, la loi est uniforme sur le support, et les égalités se départagent par la plus petite issue. La loi conditionnelle divise tout par $P(S)$.

</details>
<details><summary>Indice 3</summary>

1. L'ordre des issues change-t-il ? 2. Le support a quatre issues ; pour $0 < T < \infty$, range-les par probabilité ; à $T = \infty$, quatre égalités. 3. Relis la propriété « Température et troncatures ». 4. Écris $p_{S,i}/p_{S,j}$. 5. Quel est le plus petit ensemble de masse 1 ?

</details>

### M28.Q5 — Une itération sur un ensemble fini : prépériode, période, et ce qui empêche de boucler

<details><summary>Indice 1</summary>

Fiche §6 : la définition, le théorème et sa démonstration, le cas d'une bijection, « Un générateur glouton boucle » et ses deux limites.

</details>
<details><summary>Indice 2</summary>

Écris les termes jusqu'à la première valeur déjà vue, $u_j = u_i$ : $\mu = i$ et $\lambda = j - i$. Le théorème donne $\mu + \lambda \le N$ ; il suppose une règle déterministe et un ensemble fini.

</details>
<details><summary>Indice 3</summary>

1. $1, 0, 3, 5, 4, \ldots$ : continue jusqu'à revoir une valeur. 2. Relis « Si $f$ est une bijection de $E$, $\mu = 0$ ». 3. Compare $\lambda$ à $N$. 4. Un tirage au hasard est-il une fonction de l'état ? 5. Combien d'états de 4 symboles pris parmi 3 ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M28.R1 — Le quotient de Rayleigh et la méthode de la puissance (M12c)

<details><summary>Indice 1</summary>

M12c : valeurs propres d'une matrice $2 \times 2$ par la trace et le déterminant, quotient de Rayleigh, méthode de la puissance ; et la fiche M28 §3.

</details>
<details><summary>Indice 2</summary>

$\lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A} = 0$. Le maximum de $R$ est $\lambda_{\max}$, atteint sur la droite de son vecteur propre. Décompose $(1, 0)$ sur les deux vecteurs propres : chaque composante est multipliée par sa valeur propre à chaque pas.

</details>
<details><summary>Indice 3</summary>

1. Trace 15 et déterminant 50. 2. $R(1, 1) = \frac{9 + 2 + 2 + 6}{2}$. 4. $(1, 0) = a(2, 1) + b(1, -2)$ avec $a = \frac25$ ; le rapport $b/a$ est multiplié par le rapport des deux valeurs propres. 5. Essaie un départ orthogonal au vecteur propre dominant.

</details>

### M28.R2 — Le laplacien discret et la moyenne mobile d'un signal (M21)

<details><summary>Indice 1</summary>

M21 : le pochoir du laplacien discret et la moyenne mobile ; la fiche M28 §4, « Descendre sur la variation totale : lisser ».

</details>
<details><summary>Indice 2</summary>

Calcule case par case, aux cases 1, 2 et 3 seulement. Pour 3, développe $\frac13(x_{j-1} + x_j + x_{j+1}) - x_j$.

</details>
<details><summary>Indice 3</summary>

1. En $j = 1$ : $1 - 2 \times 4 + 2 = -5$. 2. En $j = 1$ : $\frac{1 + 4 + 2}{3} = \frac73$. 3. À un pic, la différence seconde est-elle positive ou négative ? 4. Écris $y_j$ comme $\sum_lk_lx_{j-l}$.

</details>

### M28.R3 — La loi de Boltzmann et ses limites en température (M17)

<details><summary>Indice 1</summary>

M17 : la loi de Boltzmann et ses limites ; la fiche M28 §5, les propriétés de la température.

</details>
<details><summary>Indice 2</summary>

$p_i = e^{-E_i/T}/\sum_je^{-E_j/T}$, et $e^{-\ln a} = \frac1a$. Quand $T \to 0$, seuls les niveaux d'énergie minimale gardent un poids ; quand $T \to \infty$, tous les poids finis tendent vers 1.

</details>
<details><summary>Indice 3</summary>

1. Les poids valent $1, \frac12, \frac12, \frac14$ : divise par leur somme. 2. Quel niveau a la plus petite énergie ? 3. Compare les deux poids. 4. Que vaut $e^{-E/T}$ pour $E = +\infty$ ?

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M28.1 — Quatre points du plan : leur matrice de Gram 4 × 4, leur matrice des moments d'ordre 2, et les distances lues dans la Gram

<details><summary>Indice 1</summary>

Fiche §1 (les deux lectures, la matrice des moments, le ⚠️) et §2 (les longueurs, les angles, les distances).

</details>
<details><summary>Indice 2</summary>

$G_{ij} = \mathbf{x}_i^\top\mathbf{x}_j$. Les échantillons sont les lignes : la matrice des moments des coordonnées est $\frac1N\mathbf{X}^\top\mathbf{X}$ avec $N = 4$. $\mathbf{X}\mathbf{X}^\top$ et $\mathbf{X}^\top\mathbf{X}$ ont les mêmes valeurs propres non nulles.

</details>
<details><summary>Indice 3</summary>

a) $G_{11} = 3^2 + 1^2 = 10$ et $G_{12} = 3 \times 1 + 1 \times 3 = 6$ ; continue de même. b) Calcule d'abord $\mathbf{X}^\top\mathbf{X}$, de forme $(2, 2)$. c) Une matrice $\begin{pmatrix} a & b \cr b & a \end{pmatrix}$ a pour valeurs propres $a \pm b$. d) $G_{11} + G_{jj} - 2G_{1j}$. e) $\cos\theta = G_{12}/\sqrt{G_{11}G_{22}}$.

</details>

### Ex M28.2 — Quatre villes aux sommets d'un losange : le double centrage des carrés des distances, puis une carte à une isométrie près

<details><summary>Indice 1</summary>

Fiche §2 : « Des distances à la matrice de Gram : le double centrage » (la formule en $r_i$ et $s$), « De la matrice de Gram aux positions », et « Une matrice de distances est-elle euclidienne ? ».

</details>
<details><summary>Indice 2</summary>

Élève d'abord chaque distance au carré : $29^2 = 841$, $40^2 = 1\thinspace600$, $42^2 = 1\thinspace764$. $G_{ij} = -\frac12\big(D^{(2)}_{ij} - r_i - r_j + s\big)$. Dans l'ordre A, C, B, D, $\mathbf{G}$ a deux blocs de la forme $\begin{pmatrix} a & -a \cr -a & a \end{pmatrix}$. Pour e), un point à égale distance de B et de D est sur l'hyperplan médiateur de [BD].

</details>
<details><summary>Indice 3</summary>

a) La ligne de A vaut $(0, 841, 1\thinspace600, 841)$, de moyenne 820,5 ; fais de même pour B, puis moyenne les quatre moyennes. b) $G_{AA} = -\frac12(0 - 2 \times 820{,}5 + s)$. c) $\begin{pmatrix} a & -a \cr -a & a \end{pmatrix}$ a pour valeurs propres $2a$ (vecteur $(1, -1)$) et 0. d) Écris chaque vecteur propre dans l'ordre A, B, C, D, normalise-le, multiplie-le par la racine de sa valeur propre, puis applique la convention de signe. e) Avec M le milieu de [BD], calcule MA par Pythagore.

</details>

### Ex M28.3 — Régler quatre émetteurs entre 0 et 1 : le maximum d'une réponse linéaire sur la boule et sur le pavé, d'une énergie quadratique sur la sphère, et deux pas de montée projetée

<details><summary>Indice 1</summary>

Fiche §3 : « Rester dans un pavé : la montée projetée » et « Ce que trouve la montée » (forme linéaire, forme quadratique sur la sphère, fonction convexe sur un pavé).

</details>
<details><summary>Indice 2</summary>

Sur la boule, Cauchy-Schwarz ; sur le pavé, les termes $w_ix_i$ se règlent un par un. $\nabla f = \mathbf{w}$ est constant : chaque pas ajoute $\eta\thinspace\mathbf{w}$, puis coupe. Sur la sphère, le maximum de $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ est la plus grande valeur propre ; les valeurs propres d'une matrice à blocs sont celles de ses blocs.

</details>
<details><summary>Indice 3</summary>

a) $\lVert\mathbf{w}\rVert$. b) Le signe de chaque $w_i$ décide. c) $\mathbf{x}_0 + 0{,}2\thinspace\mathbf{w} = (0{,}7 ;\ 0{,}1 ;\ 1 ;\ 1{,}72)$ : coupe, puis recommence. d) Pour la première coordonnée, il faut $0{,}3 + 2\eta \ge 1$ ; écris la condition de chaque coordonnée (pour la deuxième, $0{,}3 - \eta \le 0$). e) Le second bloc a pour trace 16 et pour déterminant 39. f) $E$ est une somme d'une fonction de $(x_1, x_2)$ et d'une fonction de $(x_3, x_4)$ : maximise chacune sur les quatre sommets de son carré.

</details>

### Ex M28.4 — Les températures le long d'une barre : la variation totale xᵀLx, son gradient 2Lx, un pas de lissage, et une marche étalée sur n pas, au carré ou en valeur absolue

<details><summary>Indice 1</summary>

Fiche §4 : « Une forme quadratique : le laplacien de la grille », « Descendre sur la variation totale : lisser » (le pas critique), « Le carré ou la valeur absolue ».

</details>
<details><summary>Indice 2</summary>

$(\mathbf{L}\mathbf{x})  _j = \deg(j)\thinspace x_j - \sum  _{\text{voisines}}x_l$, avec $\deg = 1$ aux bouts et 2 ailleurs. Un pas : $\mathbf{x} - \eta \cdot 2\mathbf{L}\mathbf{x}$. $\eta^\star = 1/\lambda _{\max}(\mathbf{L})$, avec $\lambda _{\max}$ donné par la formule admise pour $k = n - 1$. Une marche étalée sur $n$ pas coûte $\frac{h^2}{n}$ au carré et $h$ en valeur absolue.

</details>
<details><summary>Indice 3</summary>

a) Les différences valent $-2, 1, -4, -2$. b) $(\mathbf{L}\mathbf{x})_0 = 8 - 6 = 2$ et $(\mathbf{L}\mathbf{x}) _1 = 2 \times 6 - 8 - 7 = -3$ ; continue, puis double. c) Retire $0{,}15 \times 2\mathbf{L}\mathbf{x}$. e) $\lambda _{\max} = 4\sin^2\frac{4\pi}{10}$. f) Quatre différences de $\frac64$. g) Résous $\frac{36}{n} < 1$ dans les entiers.

</details>

### Ex M28.5 — Des étoffes rayées : période, fréquence, fréquence de Nyquist, repliement, variation totale rapportée à l'énergie 4 sin²(ω/2), et gain d'une moyenne mobile

<details><summary>Indice 1</summary>

Fiche §4 : « Motifs périodiques et fréquences » (dimension 1 et 2, repliement), « Un motif périodique est un vecteur propre du laplacien », « Le gain d'un flou ».

</details>
<details><summary>Indice 2</summary>

Une période $P$ donne $f = \frac1P$ et $\omega = \frac{2\pi}{P}$. Rapport : $4\sin^2\frac\omega2$ par direction où le motif varie, à additionner ; gain le long d'une direction : $\frac{1 + 2\cos\omega}{3}$, et 1 si le motif ne varie pas dans cette direction ; le flou $3 \times 3$ multiplie les deux gains. Période d'un motif $(f_1, f_2)$ : $1/\sqrt{f_1^2 + f_2^2}$.

</details>
<details><summary>Indice 3</summary>

a) Pour A, $\omega = \frac\pi3$ et $4\sin^2\frac\pi6 = 1$ ; fais de même pour B, avec $\sin^2\frac{\pi}{12} = \frac{1 - \cos(\pi/6)}{2}$. b) $\cos\frac\pi3 = \frac12$ et $\cos\frac\pi6 = \frac{\sqrt3}{2}$. c) $(f_1, f_2) = (\frac{1}{12}, \frac16)$. d) Additionne les rapports des deux directions. e) Le gain des lignes ($f_2$) fois celui des colonnes ($f_1$). f) Replie $\frac{16}{17}$ dans $[0, \frac12]$, puis prends l'inverse.

</details>

### Ex M28.6 — La prévision d'un météorologue en six catégories : la refroidir, garder les trois plus probables, garder le plus petit ensemble de masse donnée, et le coût de chaque troncature

<details><summary>Indice 1</summary>

Fiche §5 : « La température », « Tronquer, c'est conditionner », « Le coût d'une troncature ».

</details>
<details><summary>Indice 2</summary>

À $T = \frac13$, on élève au cube puis on renormalise. Range les catégories par probabilité décroissante et cumule. $\mathbf{p}_S = \mathbf{p}/P(S)$ sur $S$, 0 ailleurs ; $\mathrm{KL}(\mathbf{p}_S \thinspace\Vert\thinspace \mathbf{p}) = -\ln P(S)$ et $\frac12\lVert\mathbf{p}_S - \mathbf{p}\rVert_1 = 1 - P(S)$. Le top-p garde $k$ catégories quand la masse des $k - 1$ premières est sous $m$ et celle des $k$ premières atteint $m$.

</details>
<details><summary>Indice 3</summary>

a) La somme des six cubes vaut 0,061 948 ; divise chaque cube par elle. b) Le top-3 garde les catégories 2, 3 et 1, de masse 0,78. c) $-\ln 0{,}78$ et $1 - 0{,}78$. d) Les masses cumulées valent 0,33 ; 0,59 ; 0,78 ; 0,88 ; … e) Même calcul avec la masse de d). f) Exactement trois catégories : la masse des deux premières est sous $m$, celle des trois premières l'atteint ; attention aux crochets aux deux bouts.

</details>

### Ex M28.7 — Les décimales de a/n et l'itération x ↦ x² + c modulo n : prépériode et période à la main, et la borne du principe des tiroirs

<details><summary>Indice 1</summary>

Fiche §6 : la définition de $\mu$ et $\lambda$, le théorème et sa démonstration (les indices $i < j$ de la première répétition).

</details>
<details><summary>Indice 2</summary>

Écris les termes un par un jusqu'à la première valeur déjà vue : si $u_j = u_i$ avec $i < j$, alors $\mu = i$ et $\lambda = j - i$. En a), ce sont les **restes** qu'il faut suivre, pas les chiffres.

</details>
<details><summary>Indice 3</summary>

a) $r_0 = 5$, $r_1 = 50 \bmod 26 = 24$, $r_2 = 240 \bmod 26 = 6$ ; continue jusqu'à revoir un reste. b) $u_1 = 2$, $u_2 = 6$, $u_3 = 38 \bmod 17 = 4$ ; continue. c) Que se passe-t-il après un reste nul ? Combien de valeurs restent possibles sinon ?

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M28.8 — Deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie

<details><summary>Indice 1</summary>

Fiche §2 : l'invariance, la réciproque et le double centrage ; M12a (applications linéaires, théorème du rang) ; M12b (bases orthonormées, Gram-Schmidt, matrices orthogonales).

</details>
<details><summary>Indice 2</summary>

1 : développe $\big(\sum_ia_i\mathbf{x}_i\big)^\top\big(\sum_ja_j\mathbf{x}_j\big)$. 2 : deux écritures d'un même vecteur diffèrent d'une combinaison nulle ; pour le produit scalaire, l'identité de polarisation $\mathbf{u}^\top\mathbf{v} = \frac14(\lVert\mathbf{u} + \mathbf{v}\rVert^2 - \lVert\mathbf{u} - \mathbf{v}\rVert^2)$. 4 : une matrice qui envoie une base orthonormée sur une base orthonormée est orthogonale. 5 : centre les deux nuages.

</details>
<details><summary>Indice 3</summary>

2 : si $\sum_ia_i\mathbf{x}_i = \sum_ib_i\mathbf{x}_i$, applique 1 aux coefficients $a_i - b_i$. 3 : $T\mathbf{u} = \mathbf{0}$ entraîne $\lVert\mathbf{u}\rVert = 0$. 4 : avec $\mathbf{E}$ et $\mathbf{F}$ les matrices de colonnes $\mathbf{e}_k$ et $\mathbf{f}_k$, pose $\mathbf{R} = \mathbf{F}\mathbf{E}^\top$, puis écris $\mathbf{x}_i$ dans la base $(\mathbf{e}_1, \ldots, \mathbf{e}_r)$ de $U$. 5 : les points centrés ont la même matrice $\mathbf{D}^{(2)}$, donc la même matrice de Gram $-\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ ; la translation se lit sur les centres de gravité.

</details>

### Ex M28.9 — Le maximum d'une fonction convexe sur un pavé est atteint en un sommet

<details><summary>Indice 1</summary>

Fiche §3, « Une fonction convexe sur un pavé » ; M05a et M10 (la définition d'une fonction convexe).

</details>
<details><summary>Indice 2</summary>

La restriction d'une fonction convexe à un segment est convexe. Sur un segment $[a, b]$, une fonction convexe est sous sa corde, donc sous le plus grand de ses deux bouts. Traite ensuite les coordonnées une à une.

</details>
<details><summary>Indice 3</summary>

1 : écris $t = (1 - \theta)l_k + \theta u_k$ avec $\theta = \frac{t - l_k}{u_k - l_k}$, et applique la convexité au point $\mathbf{x}(t) = (1 - \theta)\thinspace\mathbf{x}(l_k) + \theta\thinspace\mathbf{x}(u_k)$. 2 : à chaque coordonnée, choisis la borne où $\varphi$ est la plus grande ; $f$ ne baisse jamais. 3 : par 2, toute valeur de $f$ sur $P$ est majorée par le maximum de $f$ sur les sommets. 4 : une fonction constante ; une fonction concave maximale au centre.

</details>

### Ex M28.10 — Les issues les plus probables, prises jusqu'à atteindre la masse p, forment un plus petit ensemble de masse au moins p, et la loi tronquée est à −ln P(S) de la loi de départ en divergence KL

<details><summary>Indice 1</summary>

Fiche §5 : la définition du top-p, la propriété (∂ M28.10), « Le coût d'une troncature » ; M06 (divergence KL).

</details>
<details><summary>Indice 2</summary>

1 : la $i$-ième plus grande probabilité de $A$ ne dépasse pas la $i$-ième plus grande de toutes les issues. 3 : un échange remplace une issue de $A$ hors de $S^\star$ par une issue de $S^\star$ hors de $A$, au moins aussi probable. 4 : sur $S$, le rapport $p_{S,i}/p_i$ ne dépend pas de $i$.

</details>
<details><summary>Indice 3</summary>

1 : si $a_1 \ge \cdots \ge a_j$ sont les probabilités de $A$, au moins $i$ issues ont une probabilité $\ge a_i$ ; que peux-tu en dire de $p_{(i)}$ ? 2 : utilise la définition de $k^\star$ comme plus petit indice. 3 : chaque échange fait grandir $\lvert A \cap S^\star\rvert$ d'une unité. 4 : $\sum_{i \in S}\frac{p_i}{P(S)}\ln\frac{1}{P(S)}$. 5 : $-\ln$ est décroissante.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M28.11 — Pont : diviser des scores par T avant la softmax, ou élever les probabilités à la puissance 1/T, la même loi ; et le même top-k

<details><summary>Indice 1</summary>

Fiche §5 : la température (la loi de Boltzmann des énergies $-\ln p_i$), « Tronquer, c'est conditionner », « Température et troncatures » ; M17 (softmax).

</details>
<details><summary>Indice 2</summary>

$\operatorname{softmax}(\mathbf{z})_i = e^{z_i}/\sum_je^{z_j}$. Élever $p_i$ à la puissance $\frac1T$ élève aussi le dénominateur commun, qui disparaît à la renormalisation. Pour un top-k, l'ensemble gardé dépend seulement de l'ordre des issues.

</details>
<details><summary>Indice 3</summary>

a) $e^{\mathbf{z}} \approx (3{,}004 ;\ 11{,}023 ;\ 1{,}105 ;\ 8{,}166 ;\ 0{,}607)$ : divise par leur somme. b) Même calcul avec $\mathbf{z}/3$. c) Élève $\mathbf{p}$, avec au moins 6 chiffres significatifs (pas les 4 décimales de a)), à la puissance $\frac13$, garde les trois plus grandes et renormalise. d) et e) Écris, pour une espèce gardée, les deux lois, et compare-les.

</details>

### Ex M28.12 — Expliquer avec une structure de barres rigides ce que la matrice de Gram d'une famille de vecteurs fixe, et ce qu'elle laisse libre

<details><summary>Indice 1</summary>

Fiche §2 : « Des longueurs, des angles, des distances », l'invariance et la réciproque, puis le double centrage.

</details>
<details><summary>Indice 2</summary>

Fais correspondre chaque coefficient de la matrice de Gram à quelque chose de la structure : un coefficient diagonal à une barre, un coefficient hors diagonale à une paire de barres.

</details>
<details><summary>Indice 3</summary>

Ce qui est fixé : les longueurs, les angles, donc tous les écarts entre les bouts. Ce qui est libre : tourner la structure autour du nœud, la retourner en miroir. Sans le nœud : elle peut aussi glisser d'un bloc. Dis tout cela avec des mots de charpentier.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M28.E1 — « Que perd-on, en divergence KL, à ne garder que les issues les plus probables d'une loi avant de tirer ? »

<details><summary>Indice 1</summary>

Fiche §5 : « Tronquer, c'est conditionner » et « Le coût d'une troncature », avec son ⚠️.

</details>
<details><summary>Indice 2</summary>

La loi tronquée est la loi conditionnelle sachant $S$ ; sa divergence KL à la loi de départ ne dépend que de $P(S)$. Le top-p garde au moins la masse $m$. Dans l'autre sens, la divergence est infinie.

</details>
<details><summary>Indice 3</summary>

Ta réponse tient en cinq temps : la loi conditionnelle ; $-\ln P(S)$, et pourquoi ; la borne $-\ln m$ ; le sens inverse, infini ; la distance en variation totale $1 - P(S)$, avec un exemple chiffré (choisis une masse gardée et calcule les deux nombres).

</details>

<a id="notebook"></a>

## Notebook

### M28.13 — Une configuration de points de matrice de Gram donnée, par le théorème spectral : `points_from_gram`

<details><summary>Indice 1</summary>

Fiche §2, « De la matrice de Gram aux positions », et la docstring de `points_from_gram` : elle dit l'ordre des étapes, le seuil $s$ et la convention de signe.

</details>
<details><summary>Indice 2</summary>

`np.linalg.eigh` rend les valeurs propres par ordre croissant et les vecteurs propres unitaires **en colonnes** : retourne les deux. Les valeurs propres de $[-s, s]$ deviennent 0, une valeur propre sous $-s$ lève une `ValueError`. Pour b), $\mathbf{Y} = \mathbf{X}\mathbf{R}^\top$, que tu résous avec $\mathbf{X}^\top\mathbf{X}$ inversible.

</details>
<details><summary>Indice 3</summary>

Squelette : `w, V = np.linalg.eigh(G)` puis `w, V = w[::-1], V[:, ::-1]` ; `w = np.where(w > s, w, 0.0)` ; `X = V[:, :k] * np.sqrt(w[:k])` ; puis, pour chaque colonne `k`, l'indice `i` de la première coordonnée de valeur absolue $> 10^{-8}$ (`np.flatnonzero`), et `X[:, k] *= -1` si elle est négative. N'oublie ni les contrôles de la docstring, ni que `G` ne doit pas être modifiée.

</details>

### M28.14 — Tempérer une loi donnée par ses probabilités, et le plus petit ensemble de masse donnée : `temper`, `smallest_mass_set`

<details><summary>Indice 1</summary>

Fiche §5 et les docstrings de `temper` et de `smallest_mass_set` : les deux limites de la température, le calcul par les logarithmes, la tolérance $10^{-9}$, l'ordre des issues gardées.

</details>
<details><summary>Indice 2</summary>

Une seule fonction de contrôle de la loi, partagée par les deux. Pour `temper`, ne prends le logarithme que des $p_i > 0$, et retranche leur maximum avant de diviser par $T$ (comme un log-sum-exp, M05a). Pour `smallest_mass_set`, un tri **stable** par probabilité décroissante, puis une somme cumulée.

</details>
<details><summary>Indice 3</summary>

`temper` : `q = np.zeros_like(p)`, puis les deux limites ($T = 0$ : où $\mathbf{p}$ est-elle maximale ? $T = \infty$ : où est-elle positive ?), et sinon la ligne clé `w = np.exp((logs - logs.max()) / T)`, avec `logs` les logarithmes des seuls $p_i > 0$. `smallest_mass_set` : `order = np.argsort(-p, kind="stable")` et `c = np.cumsum(p[order])`, puis le premier indice où le cumul atteint `mass - 1e-9`. Lis dans la docstring ce qu'il faut rendre si ce seuil n'est jamais atteint.

</details>

### M28.15 — Prédire ce que deviennent un pas η∇f et un pas normalisé quand la fonction est multipliée par 1 000, puis vérifier

<details><summary>Indice 1</summary>

Fiche §3 : « Le pas normalisé » (l'invariance d'échelle, le revers près d'un maximum) et « Rester dans un pavé ».

</details>
<details><summary>Indice 2</summary>

$\nabla(1\thinspace000f) = 1\thinspace000\thinspace\nabla f$, avec $\nabla f(\mathbf{x}) = -2(\mathbf{x} - \mathbf{c})$. Pour b), calcule $\mathbf{x}_0 + \eta \times 1\thinspace000 \times (-2)(\mathbf{x}_0 - \mathbf{c})$, puis projette. Pour d), le pas normalisé avance de $\eta$ en ligne droite vers $\mathbf{c}$.

</details>
<details><summary>Indice 3</summary>

`ascent_15` lit `C_15`, `X0_15` et `ETA_15` au moment de l'appel, pas dans des arguments par défaut : `x = np.array(X0_15, dtype=float)`, puis, dans une boucle de `n_steps` pas qui range les itérés dans une liste, les deux lignes clés `g = scale * (-2.0 * (x - C_15))` et `x = np.clip(x + ETA_15 * step, 0.0, 1.0)`, où `step` est `g` ou `g` divisé par sa norme. Pour d), $\lVert\mathbf{x}_0 - \mathbf{c}\rVert$ se calcule à la main.

</details>

### M28.16 — Des motifs rayés de fréquence croissante jusqu'au damier : leur variation totale, et ce qu'en laissent un flou 3 × 3 et dix pas de descente sur la variation totale

<details><summary>Indice 1</summary>

Fiche §4 : le laplacien de la grille, « Descendre sur la variation totale : lisser », « Un motif périodique est un vecteur propre du laplacien » (les bords libres), « Le gain d'un flou ».

</details>
<details><summary>Indice 2</summary>

$\mathbf{L}\mathbf{x}$ à bords libres : pour chaque paire de voisines, la différence s'ajoute à l'une et se retranche de l'autre ; quatre opérations sur des tranches suffisent (`x[1:, :] - x[:-1, :]`, et de même le long des colonnes). La courbe : `np.linspace(0, 0.5, 200)` et `ax.set_yscale("log")`.

</details>
<details><summary>Indice 3</summary>

`L = np.zeros_like(x)` ; `L[1:, :] += x[1:, :] - x[:-1, :]` ; `L[:-1, :] += x[:-1, :] - x[1:, :]` ; et les deux mêmes lignes sur les colonnes. Dans `draw_stripes_16`, une boucle sur `motifs.items()`, trois `axes[i, k].imshow(..., vmin=-1, vmax=1)` par ligne d'axes, et trois listes à remplir. Le bloc central est `y[12:36, 12:36]`. Les deux fonctions dessinent dans les axes reçus, sans `plt.figure` ni `plt.subplots` ; la courbe se trace d'un seul `ax.plot`, les points mesurés d'un autre, sans trait.

</details>

### M28.17 — Chasse à l'erreur : un double centrage fait sur les distances au lieu de leurs carrés, une montée qui coupe le gradient au lieu du point, une prépériode comptée dans la période

<details><summary>Indice 1</summary>

Les trois ⚠️ de la fiche, aux §2, §3 et §6.

</details>
<details><summary>Indice 2</summary>

Pour chaque vérification du collègue, demande-toi quelle propriété particulière de ses données cache l'erreur : des distances qui valent toutes 1 ; un départ sous un maximum intérieur, avec des gradients positifs ; une suite sans queue.

</details>
<details><summary>Indice 3</summary>

(1) Que vaut $d^2$ quand $d = 1$ ? (2) Que devient une coordonnée dont le gradient est négatif, si l'on coupe le gradient dans $[0, 1]$ ? Et un point qui dépasse 1 ? (3) Pour une bijection, $\mu = 0$ : que vaut alors $j$ ? Corrige chaque fonction en une ligne.

</details>

### M28.18 — Un test de propriété : la configuration rendue redonne la matrice de Gram et les distances, pour des points tirés au hasard

<details><summary>Indice 1</summary>

Fiche §2 (la formule des distances, le double centrage) et la docstring de `points_from_gram` (le rang, la convention de signe, « compare des matrices de Gram ou des distances, jamais des coordonnées »).

</details>
<details><summary>Indice 2</summary>

La boucle des tirages est fournie : tes contrôles reçoivent les points `P`, la translation `t`, la fonction à tester `func` et `rtol`, et rendent un ensemble de noms (`set()` quand tout passe). Appelle toujours `func`, jamais `mymath` directement. Les carrés des distances d'un nuage `Z` : `((Z[:, None, :] - Z[None, :, :]) ** 2).sum(-1)`. Pour a), un contrôle de quelques lignes, qui ne regarde que $\mathbf{X}\mathbf{X}^\top - \mathbf{G}$, passé à la boucle par `checks=`.

</details>
<details><summary>Indice 3</summary>

Squelette de `failed_checks_18` : `failed = set()`, `n = len(P)`, `G = P @ P.T`, `s = max(1.0, np.abs(G).max())`, `X = np.asarray(func(G), dtype=float)`, `finite = np.all(np.isfinite(X))`, puis les quatre conditions de l'énoncé, chacune avec `or not finite`, et `failed.add("gram")` (ou un autre nom) quand l'une est vraie ; pour la translation, `J = np.eye(n) - np.ones((n, n)) / n` et `Gc = -0.5 * J @ D2 @ J`, où `D2` sont les carrés des distances de `P + t`. Pour d), demande-toi ce qu'une isométrie qui fixe l'origine change à $\mathbf{X}\mathbf{X}^\top$.

</details>

### M28.19 — Défi : redessiner la carte de 30 villes quand un quart des distances manquent, à moins de 1 km en moyenne après alignement

<details><summary>Indice 1</summary>

Fiche §2 : le double centrage, les positions par le théorème spectral, et la remarque sur les petites valeurs propres négatives (on garde les plus grandes).

</details>
<details><summary>Indice 2</summary>

Une carte, même grossière, donne une distance pour chaque paire, y compris les paires manquantes. Remplis les trous avec une première estimation, fais une carte, remplace les seules distances manquantes par celles de la carte, et recommence.

</details>
<details><summary>Indice 3</summary>

Départ : les trous remplis par la moyenne des distances connues. Puis une centaine de fois : `G = -0.5 * J @ (Df ** 2) @ J`, les valeurs propres négatives de `G` mises à 0 (sinon `points_from_gram` refuse la matrice), `X = points_from_gram(G, dim=2)`, et `Df = np.where(missing, distances_of(X), D)`. Mesure l'erreur avec `procrustes_error_19` après chaque variante que tu essaies.

</details>
