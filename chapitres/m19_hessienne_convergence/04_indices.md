# M19 · Hessienne, conditionnement et convergence — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Ponts, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M19.Q1 — La hessienne : de quelle taille, symétrique, de quoi ?

<details><summary>Indice 1</summary>

Relis « La matrice des dérivées secondes » et « La courbure dans une direction » (fiche §1).

</details>
<details><summary>Indice 2</summary>

1. Une ligne et une colonne par variable ; grâce à Schwarz, la diagonale et un triangle suffisent. 3. Dérive $xyz$ deux fois : une dérivée seconde qui fait intervenir deux fois la même variable est nulle ici.

</details>
<details><summary>Indice 3</summary>

1. $5 + 4 + 3 + 2 + 1$. 6. $\mathbf{u}^\top\mathbf{H}\mathbf{u} = 2u_1^2 - 4u_2^2$ pour une hessienne diagonale.

</details>

### M19.Q2 — Minimum, maximum, selle ou direction plate ?

<details><summary>Indice 1</summary>

Relis l'encadré « Test du second ordre en dimension $n$ » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Regarde seulement les signes : tous positifs, tous négatifs, les deux, ou un zéro avec des autres de même signe. 5. En dimension 2, le déterminant est le produit des deux valeurs propres.

</details>
<details><summary>Indice 3</summary>

6. Cherche trois valeurs propres de produit positif qui n'ont pas toutes le même signe.

</details>

### M19.Q3 — Converge ou pas : lire les valeurs propres de M

<details><summary>Indice 1</summary>

Relis l'encadré « Théorème » du §3 : ce sont les **modules** des valeurs propres qui comptent.

</details>
<details><summary>Indice 2</summary>

Le facteur au pire est le plus grand module. 3. Une composante multipliée par $-1$ à chaque pas ne diminue pas. 5. Chaque composante de l'écart évolue seule.

</details>
<details><summary>Indice 3</summary>

4. Cherche le plus petit $k$ avec $0{,}5^k \le 10^{-3}$, c'est-à-dire $2^k \ge 1\,000$.

</details>

### M19.Q4 — Le pas de Richardson : lire la convergence sur les valeurs propres de I − ωA

<details><summary>Indice 1</summary>

Relis le §4 : si $\mathbf{A}\mathbf{q} = \lambda\mathbf{q}$, alors $(\mathbf{I} - \omega\mathbf{A})\mathbf{q} = (1 - \omega\lambda)\mathbf{q}$.

</details>
<details><summary>Indice 2</summary>

Calcule $1 - 2\omega$ et $1 - 4\omega$ pour chaque pas, puis regarde si les deux modules sont $< 1$. Le pas critique est $2/\lambda_{\max}$.

</details>
<details><summary>Indice 3</summary>

5. Applique l'énoncé du §5 : $\omega^\star = \frac{2}{\lambda_{\min} + \lambda_{\max}}$ et $\rho^\star = \frac{\kappa - 1}{\kappa + 1}$.

</details>

### M19.Q5 — Le conditionnement : ce qui ralentit, ce qui ne change rien

<details><summary>Indice 1</summary>

Relis le §5 : « Le meilleur pas, et le prix du conditionnement » et « Ce qui ne change rien ».

</details>
<details><summary>Indice 2</summary>

2. Multiplier $\mathbf{A}$ par 10 multiplie toutes ses valeurs propres par 10. 4. Le nombre d'itérations est $\frac{6\ln 10}{-\ln\rho^\star}$, ou à peu près $1{,}15\,\kappa\,d$.

</details>
<details><summary>Indice 3</summary>

5. $\tilde a_{12} = \frac{0{,}9}{\sqrt{9 \times 1}}$, puis les valeurs propres d'une matrice $\begin{pmatrix} 1 & c \\ c & 1 \end{pmatrix}$ sont $1 \pm c$. 6. Une matrice orthogonale ne change pas les valeurs propres de $\mathbf{Q}^\top\mathbf{A}\mathbf{Q}$.

</details>

### M19.Q6 — Module d'un nombre complexe et racines d'un trinôme

<details><summary>Indice 1</summary>

Relis « Le strict minimum sur les nombres complexes » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$\lvert a + ib\rvert = \sqrt{a^2 + b^2}$ ; $z\bar z = a^2 + b^2$. Pour un trinôme $r^2 - pr + q$ de discriminant négatif, les racines sont $\frac p2 \pm i\frac{\sqrt{-\Delta}}{2}$, de module $\sqrt q$.

</details>
<details><summary>Indice 3</summary>

3. $\Delta = 16 - 52 = -36$. 4. Le module est multiplicatif : $\lvert z^{10}\rvert = \lvert z\rvert^{10}$. 6. Vérifie d'abord que le discriminant est négatif.

</details>

### M19.Q7 — Un gradient estimé sur un échantillon : vrai ou faux

<details><summary>Indice 1</summary>

Relis « L'estimateur » (fiche §7).

</details>
<details><summary>Indice 2</summary>

La variance d'une moyenne de $B$ tirages indépendants est divisée par $B$ ; l'erreur type, sa racine, par $\sqrt B$.

</details>
<details><summary>Indice 3</summary>

5. Sans remise, $B = N$ tire tous les termes une fois chacun. 6. « Sans biais » parle de la moyenne sur tous les tirages, pas d'un tirage.

</details>

### M19.Q8 — Boule ou pavé : la direction est-elle gardée ?

<details><summary>Indice 1</summary>

Relis les formules de la boule et du pavé (fiche §8).

</details>
<details><summary>Indice 2</summary>

Boule : si la norme dépasse $r$, multiplie par $r/\lVert\mathbf{x}\rVert$, sinon ne change rien. Pavé : coupe chaque coordonnée à $[-2, 2]$.

</details>
<details><summary>Indice 3</summary>

2. et 3. La direction est gardée si le résultat est un multiple positif du vecteur de départ. 6. Calcule la norme de $(r, r)$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M19.R1 — Le théorème spectral et les valeurs propres d'une matrice symétrique (M12c)

<details><summary>Indice 1</summary>

M12c §3 et §6 : le polynôme caractéristique d'une matrice $2 \times 2$ est $\lambda^2 - (\operatorname{tr})\lambda + \det$.

</details>
<details><summary>Indice 2</summary>

Trace 9, déterminant $18 - 4 = 14$. Pour un vecteur propre de $\lambda$, résous $(\mathbf{S} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$, puis divise par la norme.

</details>
<details><summary>Indice 3</summary>

4. $\mathbf{S}^3 = \mathbf{Q}\boldsymbol{\Lambda}^3\mathbf{Q}^\top$. 6. Dans la base des vecteurs propres, la forme quadratique n'a plus de terme croisé.

</details>

### M19.R2 — Suites géométriques et récurrences d'ordre 1 (R5)

<details><summary>Indice 1</summary>

R5 §3 et §5 : $u_k = u_0\,m^k$ ; une suite $v_{k+1} = m\,v_k + c$ se ramène à une suite géométrique par l'écart à son point fixe.

</details>
<details><summary>Indice 2</summary>

3. Le point fixe vérifie $\ell = 0{,}5\,\ell + 3$ ; l'écart $v_k - \ell$ est multiplié par $0{,}5$ à chaque pas.

</details>
<details><summary>Indice 3</summary>

4. $k > \frac{\ln 0{,}01}{\ln 0{,}7}$. 5. Regarde le module de $-1{,}2$.

</details>

### M19.R3 — Le conditionnement par la SVD (M12d)

<details><summary>Indice 1</summary>

M12d §4 : $\kappa = \sigma_{\max}/\sigma_{\min}$.

</details>
<details><summary>Indice 2</summary>

2. Les valeurs singulières sont les racines des valeurs propres de $\mathbf{A}^\top\mathbf{A}$ ; pour $\mathbf{A}$ symétrique, $\mathbf{A}^\top\mathbf{A} = \mathbf{A}^2$.

</details>
<details><summary>Indice 3</summary>

5. Les valeurs singulières sont les valeurs absolues des coefficients diagonaux. Pour Richardson, regarde $1 - \omega\lambda$ pour $\lambda = -0{,}5$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M19.1 — La hessienne d'une fonction de trois variables, et son développement de Taylor d'ordre 2

<details><summary>Indice 1</summary>

Relis le §1 de la fiche et son exemple : gradient, hessienne, puis Taylor avec $\mathbf{h} = (0{,}1 ;\ -0{,}2 ;\ 0{,}1)$.

</details>
<details><summary>Indice 2</summary>

En $\mathbf{p}$, $e^{x - y} = 1$. Les dérivées premières : $2xz - 3y + e^{x-y}$, $z^2 - 3x - e^{x-y}$, $x^2 + 2yz$. Calcule $\nabla f^\top\mathbf{h}$, puis $\mathbf{H}\mathbf{h}$ et $\mathbf{h}^\top\mathbf{H}\mathbf{h}$, sans oublier le $\frac12$.

</details>
<details><summary>Indice 3</summary>

b) $f_{xx} = 2z + e^{x-y}$, $f_{xy} = -3 - e^{x-y}$, $f_{yy} = e^{x-y}$ ; les trois autres sont des polynômes. c) $f(\mathbf{p}) = 4$. f) Calcule $\mathbf{H}(2, -1, 2)$, fais le produit scalaire avec $(2, -1, 2)$, puis divise par 9. g) $5 \times 1 - (-4)^2$.

</details>

### Ex M19.2 — Classer les points critiques d'une fonction de trois variables

<details><summary>Indice 1</summary>

Relis l'exemple du §2 : annuler le gradient, puis lire les signes des valeurs propres en chaque point.

</details>
<details><summary>Indice 2</summary>

$\frac{\partial f}{\partial x} = 3x^2 + 3y^2 - 15$, $\frac{\partial f}{\partial y} = 6xy - 12$, $\frac{\partial f}{\partial z} = 2z - 2$. La hessienne est diagonale par blocs : un bloc $2 \times 2$ en $(x, y)$, et 2 pour $z$.

</details>
<details><summary>Indice 3</summary>

$x^2 + y^2 = 5$ et $xy = 2$ donnent $(x + y)^2 = 9$ et $(x - y)^2 = 1$. Le bloc $\begin{pmatrix} 6x & 6y \\ 6y & 6x \end{pmatrix}$ a pour valeurs propres $6x + 6y$ (vecteur $(1, 1)$) et $6x - 6y$ (vecteur $(1, -1)$).

</details>

### Ex M19.3 — Une itération linéaire 2 × 2 : point fixe, erreur, et convergence par les valeurs propres

<details><summary>Indice 1</summary>

Relis le §3 : point fixe, écart, et décomposition de l'écart sur les vecteurs propres.

</details>
<details><summary>Indice 2</summary>

a) Résous $(\mathbf{I} - \mathbf{M})\mathbf{x}^\star = \mathbf{c}$. c) Calcule $\mathbf{M}\mathbf{q}_1$ et $\mathbf{M}\mathbf{q}_2$. d) $\mathbf{e}_0 = \mathbf{x}_0 - \mathbf{x}^\star$, puis résous $a\,\mathbf{q}_1 + b\,\mathbf{q}_2 = \mathbf{e}_0$.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{x}_3 = \mathbf{x}^\star + a\,\lambda_1^3\,\mathbf{q}_1 + b\,\lambda_2^3\,\mathbf{q}_2$. f) Le plus petit $k$ tel que $0{,}6^k \le 10^{-3}$. g) Calcule l'écart de départ $(5, 0) - \mathbf{x}^\star$.

</details>

### Ex M19.4 — Résoudre un système 2 × 2 par l'itération de Richardson : trois pas à la main, et le pas critique

<details><summary>Indice 1</summary>

Relis le §4 et l'exemple des deux ressorts : $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega(\mathbf{b} - \mathbf{A}\mathbf{x}_k)$.

</details>
<details><summary>Indice 2</summary>

Calcule à chaque pas $\mathbf{A}\mathbf{x}_k$, puis le résidu, puis le pas. Les valeurs propres de $\mathbf{A}$ ont pour vecteurs $(1, 1)$ et $(1, -1)$.

</details>
<details><summary>Indice 3</summary>

b) $\mathbf{x}_1 = 0{,}08\,\mathbf{b}$ ; $\mathbf{A}\mathbf{x}_1 = (2{,}24 ;\ 2{,}88)$. d) $5 \pm 3$. g) $1 - 0{,}3 \times 8$. h) L'écart de départ $(1, -1)$ est un vecteur propre : de quelle valeur propre de $\mathbf{I} - 0{,}3\,\mathbf{A}$ ?

</details>

### Ex M19.5 — Le meilleur pas de Richardson (énoncé), et le nombre d'itérations pour gagner six décimales

<details><summary>Indice 1</summary>

Relis l'encadré « Énoncé » du §5 et la formule $k \ge \frac{d\ln 10}{-\ln\rho}$ du §3.

</details>
<details><summary>Indice 2</summary>

a) Le bloc $\begin{pmatrix} 7 & 6 \\ 6 & 7 \end{pmatrix}$ a pour valeurs propres $7 \pm 6$ ; la troisième se lit. Ensuite $\omega^\star = \frac{2}{\lambda_{\min} + \lambda_{\max}}$ et $\rho^\star = \frac{\kappa - 1}{\kappa + 1}$.

</details>
<details><summary>Indice 3</summary>

e) $\frac{6\ln 10}{\ln(7/6)} \approx 89{,}6$. f) $1 - \frac{1}{13}$. h) $\kappa = 110$ : $\rho^\star = \frac{109}{111}$.

</details>

### Ex M19.6 — Une récurrence d'ordre 2 à racines réelles : terme général et convergence

<details><summary>Indice 1</summary>

Relis « Le polynôme caractéristique » (fiche §6) et son exemple.

</details>
<details><summary>Indice 2</summary>

$r^2 - 0{,}7r + 0{,}1 = 0$ : somme $0{,}7$, produit $0{,}1$. Puis $\alpha + \beta = u_0$ et $\alpha r_1 + \beta r_2 = u_1$. Pour $(v_k)$, attention aux signes : $v_{k+2} = 1{,}5\,v_{k+1} + v_k$ donne $r^2 - 1{,}5r - 1$.

</details>
<details><summary>Indice 3</summary>

d) $u_{10} = 2 \times 0{,}5^{10} + 0{,}2^{10}$. f) Pour que $v_k \to 0$, le coefficient de $2^k$ doit être nul : $v_k = \beta(-0{,}5)^k$, avec $\beta = v_0$.

</details>

### Ex M19.7 — Une récurrence d'ordre 2 à racines complexes : module et oscillation amortie

<details><summary>Indice 1</summary>

Relis « Le strict minimum sur les nombres complexes » et l'exemple qui le suit (fiche §6).

</details>
<details><summary>Indice 2</summary>

$p = 0{,}5$, $q = 0{,}4225$ : $\Delta = p^2 - 4q$ ; les racines sont $\frac p2 \pm i\frac{\sqrt{-\Delta}}{2}$, de module $\sqrt q$ ; $\cos\theta = \frac{p}{2\sqrt q}$.

</details>
<details><summary>Indice 3</summary>

e) $u_2 = 0{,}5 \times 0{,}25 - 0{,}4225 \times 1$, puis continue. f) $k = 0$ donne $A = u_0$ ; $k = 1$ donne $0{,}65(A\cos\theta + B\sin\theta) = u_1$, avec $\cos\theta = \frac{5}{13}$ et $\sin\theta = \frac{12}{13}$. h) Une période fait tourner l'angle de $2\pi$.

</details>

### Ex M19.8 — Une pente estimée sur B points tirés au hasard : espérance et variance de l'estimation

<details><summary>Indice 1</summary>

Relis le §7 et son exemple du capteur : la dérivée exacte est la moyenne des dérivées des termes.

</details>
<details><summary>Indice 2</summary>

En $a = 2$, les résidus $a\,I_k - U_k$ valent $0$, $1$, $-1$, $-1$. La variance avec remise est $\sigma^2/B$ ; sans remise, multiplie par $\frac{N - B}{N - 1}$.

</details>
<details><summary>Indice 3</summary>

c) Moyenne des carrés moins carré de la moyenne : $\frac{0 + 16 + 16 + 36}{4} - 1{,}5^2$. f) $\frac{\sigma}{\sqrt B} \le 0{,}5$ revient à $B \ge 4\sigma^2$. h) Seuls les couples qui contiennent le 4 et pas de $-4$ ni de $-6$ donnent une moyenne positive. i) $a^\star = \frac{\sum I_kU_k}{\sum I_k^2}$.

</details>

### Ex M19.9 — Projeter un même vecteur sur une boule et sur un pavé : deux points, deux directions

<details><summary>Indice 1</summary>

Relis les formules du §8 et son exemple.

</details>
<details><summary>Indice 2</summary>

b) $\lVert\mathbf{x}\rVert > 2{,}8$ : multiplie $\mathbf{x}$ par $2{,}8/7$. c) Coupe chaque coordonnée à $[-2, 2]$. d) La distance à la projection sur la boule est $\lVert\mathbf{x}\rVert - r$.

</details>
<details><summary>Indice 3</summary>

d) $\mathbf{x} - (2, -2, 2) = (4, -1, 0)$. e) $\cos = \frac{\mathbf{x}\cdot\mathbf{y}}{\lVert\mathbf{x}\rVert\,\lVert\mathbf{y}\rVert}$ avec $\lVert(2, -2, 2)\rVert = 2\sqrt3$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M19.10 — Une itération linéaire de matrice symétrique converge pour tout départ si et seulement si ses valeurs propres sont de module < 1

<details><summary>Indice 1</summary>

Relis le §3 : l'écart vérifie $\mathbf{e}_{k+1} = \mathbf{M}\mathbf{e}_k$, et, dans une base de vecteurs propres, chaque composante est une suite géométrique.

</details>
<details><summary>Indice 2</summary>

1. $\mathbf{I} - \mathbf{M}$ a pour valeurs propres les $1 - \lambda_i$. 3. Les $\mathbf{q}_i$ sont orthonormés : $\lVert\sum_ic_i\mathbf{q}_i\rVert^2 = \sum_ic_i^2$ (Pythagore, M12b). 4. Passe à la limite dans $\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$.

</details>
<details><summary>Indice 3</summary>

4. Depuis $\boldsymbol{\ell}$ (un point fixe), la suite est constante ; depuis $\boldsymbol{\ell} + \mathbf{q}_j$, l'écart à $\boldsymbol{\ell}$ vaut $\mathbf{M}^k\mathbf{q}_j = \lambda_j^k\mathbf{q}_j$, dont la norme est $\lvert\lambda_j\rvert^k$. 5. La symétrie a donné une base **orthonormée** de vecteurs propres.

</details>

### Ex M19.11 — L'itération de Richardson converge si et seulement si 0 < ω < 2/λmax

<details><summary>Indice 1</summary>

Relis le §4 : $\mathbf{M} = \mathbf{I} - \omega\mathbf{A}$ et $\mathbf{c} = \omega\mathbf{b}$, puis applique ∂ M19.10.

</details>
<details><summary>Indice 2</summary>

2. $(\mathbf{I} - \omega\mathbf{A})^\top = \mathbf{I} - \omega\mathbf{A}^\top$ ; et $(\mathbf{I} - \omega\mathbf{A})\mathbf{q} = \mathbf{q} - \omega\lambda\mathbf{q}$. 3. $-1 < 1 - \omega\lambda < 1$, puis utilise $\lambda > 0$ pour toutes les valeurs propres.

</details>
<details><summary>Indice 3</summary>

4. $\lambda \mapsto 1 - \omega\lambda$ est affine, donc monotone : sur $[\lambda_{\min}, \lambda_{\max}]$, son module est le plus grand à un bout. 5. La composante est multipliée par $-1$ à chaque pas.

</details>

### Ex M19.12 — Une récurrence d'ordre 2 converge si et seulement si ses racines sont de module < 1 : le critère |q| < 1 et |p| < 1 + q

<details><summary>Indice 1</summary>

Relis « Quand tend-elle vers 0 ? » (fiche §6) et le triangle de la figure.

</details>
<details><summary>Indice 2</summary>

1. Le système $\alpha + \beta = u_0$, $\alpha r_1 + \beta r_2 = u_1$ a pour déterminant $r_2 - r_1 \ne 0$ ; pour l'hérédité, $r_i^2 = p\,r_i - q$. 3. $q = r_1r_2 = r\bar r = \lvert r\rvert^2$, et $(1 - \sqrt q)^2 \ge 0$. 4. Une parabole tournée vers le haut a ses deux racines dans $]-1, 1[$ exactement quand elle est positive en $-1$ et en $1$ et que son sommet est entre les deux.

</details>
<details><summary>Indice 3</summary>

4. $P(1) = 1 - p + q$ et $P(-1) = 1 + p + q$. Pour $\lvert q\rvert < 1$ : $q = r_1r_2$ avec $\lvert r_1\rvert, \lvert r_2\rvert < 1$. Pour la réciproque au 5., avec des racines réelles : $\lvert p\rvert < 1 + q < 2$ place le sommet $\frac p2$ dans $]-1, 1[$.

</details>

### Ex M19.13 — La projection sur une boule est son point le plus proche, et elle garde la direction

<details><summary>Indice 1</summary>

Relis le §8 ; pour 1., écris $\mathbf{x} = (\mathbf{x} - \mathbf{y}) + \mathbf{y}$.

</details>
<details><summary>Indice 2</summary>

1. $\lVert\mathbf{x}\rVert \le \lVert\mathbf{x} - \mathbf{y}\rVert + \lVert\mathbf{y}\rVert$. 2. $\mathbf{x} - \mathbf{y}^\star = \left(1 - \frac{r}{\lVert\mathbf{x}\rVert}\right)\mathbf{x}$. 4. Une somme de termes qui dépendent chacun d'une seule coordonnée se minimise terme à terme.

</details>
<details><summary>Indice 3</summary>

5. Si $P(\mathbf{x}) = t\,\mathbf{x}$ avec $t < 1$ (puisque $\mathbf{x}$ est hors du pavé) : une coordonnée coupée vérifie $c = t\lvert x_i\rvert$ ; une coordonnée non coupée vérifie $x_i = t\,x_i$, donc $x_i = 0$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M19.14 — Pont : un pas de Richardson est un pas de descente sur ½ xᵀA x − bᵀx

<details><summary>Indice 1</summary>

Relis « Richardson est une descente de gradient » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Le gradient de $\frac12\mathbf{x}^\top\mathbf{A}\mathbf{x}$ est $\mathbf{A}\mathbf{x}$ pour $\mathbf{A}$ symétrique (M09b), celui de $\mathbf{b}^\top\mathbf{x}$ est $\mathbf{b}$.

</details>
<details><summary>Indice 3</summary>

c) Compare $\mathbf{b} - \mathbf{A}\mathbf{x}$ et $-\nabla f(\mathbf{x})$. e) C'est le pas critique de Richardson.

</details>

### Ex M19.15 — Pont : le préconditionnement diagonal

<details><summary>Indice 1</summary>

Relis « Préconditionner » (fiche §5) et son exemple des deux ressorts.

</details>
<details><summary>Indice 2</summary>

a) Trace $16{,}25$, déterminant $4 - 1 = 3$ ; pour ne pas perdre de chiffres, calcule la petite valeur propre comme le déterminant divisé par la grande. c) $\tilde a_{ij} = \frac{a_{ij}}{\sqrt{a_{ii}a_{jj}}}$. e) Le nombre d'itérations au meilleur pas est $\frac{6\ln 10}{-\ln\frac{\kappa - 1}{\kappa + 1}}$.

</details>
<details><summary>Indice 3</summary>

c) $\frac{1}{\sqrt{16 \times 0{,}25}} = 0{,}5$. f) $y_i = \sqrt{a_{ii}}\,x_i$. Dans ta copie : regarde la diagonale de $\begin{pmatrix} 1 & 0{,}9 \\ 0{,}9 & 1 \end{pmatrix}$.

</details>

### Ex M19.16 — MML §5.7 et §5.8

<details><summary>Indice 1</summary>

Lis d'abord le §5.7 en entier, puis le §5.8 jusqu'à la définition de la série de Taylor en plusieurs variables ; l'exemple final se lit crayon en main.

</details>
<details><summary>Indice 2</summary>

Le terme d'ordre $k$ de MML est un tableau à $k$ indices contracté $k$ fois avec le déplacement : pour $k = 1$, c'est $\nabla f^\top\mathbf{h}$ ; pour $k = 2$, $\mathbf{h}^\top\mathbf{H}\mathbf{h}$.

</details>
<details><summary>Indice 3</summary>

4. Pour vérifier ta hessienne, appelle `numerical_hessian` (ou la référence) dans le notebook, en ton point.

</details>

### Ex M19.17 — MML §7.1

<details><summary>Indice 1</summary>

Lis le §7.1 jusqu'à la fin de son exemple, puis la remarque sur le conditionnement ; les deux sous-sections suivantes se lisent plus vite.

</details>
<details><summary>Indice 2</summary>

2. Pour une matrice $2 \times 2$ symétrique, trace et déterminant donnent les valeurs propres. 4. Repère dans la formule le terme qui n'existe pas dans la descente simple.

</details>
<details><summary>Indice 3</summary>

3. Compare le remède du livre à la mise à l'échelle des inconnues du §5. 5. Linéarité de l'espérance, comme dans le §7 de la fiche.

</details>

### Ex M19.18 — Expliquer, sur un dessin de lignes de niveau, pourquoi un système mal conditionné converge lentement

<details><summary>Indice 1</summary>

Relis « Le dessin » (fiche §5) et la figure des deux ressorts (§4).

</details>
<details><summary>Indice 2</summary>

Des cercles pour un conditionnement 1 ; des ellipses dont les axes sont dans le rapport $\sqrt{50} \approx 7$ pour 50.

</details>
<details><summary>Indice 3</summary>

Le plan : la forme des lignes ; le résidu perpendiculaire aux lignes ; le pas limité par la direction propre de la plus grande valeur propre ; l'autre direction qui avance peu ; l'allongement et le nombre d'itérations ; la mise à l'échelle.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M19.E1 — « Que nous apprend la hessienne en un minimum ? »

<details><summary>Indice 1</summary>

Relis l'essentiel en 10 lignes, points 1 à 3, et « Les formes quadratiques » de M12c §7.

</details>
<details><summary>Indice 2</summary>

Taylor d'ordre 2 ; les valeurs propres comme courbures ; le test du second ordre ; les lignes de niveau, des ellipses de demi-axes proportionnels à $1/\sqrt{\lambda_i}$.

</details>
<details><summary>Indice 3</summary>

Le plan : définition ; courbures ; nature du point ; forme des lignes de niveau ; coût en grande dimension.

</details>

### M19.E2 — « Pourquoi un mauvais conditionnement ralentit-il une méthode itérative ? »

<details><summary>Indice 1</summary>

Relis le §5 en entier.

</details>
<details><summary>Indice 2</summary>

$\kappa = \lambda_{\max}/\lambda_{\min}$ ; le pas sous $2/\lambda_{\max}$ ; la direction plate avance d'un facteur $1 - \omega\lambda_{\min}$.

</details>
<details><summary>Indice 3</summary>

Le plan : définition ; ce qui limite le pas ; ce qui fixe la vitesse ; l'ordre de grandeur des itérations ; les invariances ; le préconditionnement ; un exemple (une structure, un circuit, une simulation de chaleur).

</details>

<a id="notebook"></a>

## Notebook
