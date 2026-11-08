# M09b · Moindres carrés et régularisation — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M09b.Q1 — MSE, RMSE, MAE, R² : ce que mesure chacune

<details><summary>Indice 1</summary>

Relis « MSE, RMSE, MAE et loss de Huber » et « Le coefficient de détermination » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une moyenne de carrés est dans l'unité au carré ; un rapport de deux sommes de carrés n'a pas d'unité.

</details>
<details><summary>Indice 3</summary>

4 : compare la moyenne des $r_i^2$ et le carré de la moyenne des $|r_i|$ (la variance des $|r_i|$ est positive). 5 : la constante $\bar{y}$ est-elle un modèle possible ?

</details>

### M09b.Q2 — Gradients matriciels : associer chaque fonction à son gradient

<details><summary>Indice 1</summary>

Relis « Trois identités » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Une fonction linéaire a un gradient constant ; une forme quadratique, un gradient qui est une matrice fois $\mathbf{w}$.

</details>
<details><summary>Indice 3</summary>

Distingue 3 et 4 par la symétrie de la matrice. 7 : le gradient a la forme de $\mathbf{w}$.

</details>

### M09b.Q3 — Équations normales : quand la solution est-elle unique ?

<details><summary>Indice 1</summary>

Relis « Le minimum annule le gradient » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Unique si et seulement si les colonnes de $\mathbf{X}$ sont indépendantes (rang $p$).

</details>
<details><summary>Indice 3</summary>

2 : le rang ne dépasse pas le nombre de lignes. 4 : additionne les trois colonnes du one-hot. 6 : le minimum de la distance à un plan existe-t-il toujours ?

</details>

### M09b.Q4 — Linéaire en x ou linéaire en w ?

<details><summary>Indice 1</summary>

Relis « Un modèle linéaire en $\mathbf{w}$ » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Un modèle est linéaire en $\mathbf{w}$ s'il s'écrit $\sum_j w_j\,\phi_j(x)$, avec des fonctions $\phi_j$ qui ne contiennent aucun poids.

</details>
<details><summary>Indice 3</summary>

6 : développe le carré. 5 : où est $w_2$ ?

</details>

### M09b.Q5 — Ridge : vrai ou faux sur la pénalité L2

<details><summary>Indice 1</summary>

Relis le §5 de la fiche, et la fin du §6.

</details>
<details><summary>Indice 2</summary>

Pour 4 : que minimisent exactement les moindres carrés ? Pour 5 : relis l'erreur classique du §5.

</details>
<details><summary>Indice 3</summary>

3 : relis « Pourquoi des zéros exacts ? » (fiche §6). 6 : relis « Weight decay ».

</details>

### M09b.Q6 — Lasso ou ridge : qui annule des poids ?

<details><summary>Indice 1</summary>

Relis le §6 de la fiche, et sa figure.

</details>
<details><summary>Indice 2</summary>

Compare le coût de pousser un poids nul à $\varepsilon$ : $\lambda\varepsilon^2$ ou $\lambda\varepsilon$.

</details>
<details><summary>Indice 3</summary>

3 : compare le gain $g\varepsilon$ au coût $\lambda\varepsilon$. 4 : $S(z, \gamma) = \operatorname{signe}(z)\max(|z| - \gamma, 0)$. 6 : dessine $|w_1| + |w_2| = 1$.

</details>

### M09b.Q7 — Bruit gaussien et moindres carrés

<details><summary>Indice 1</summary>

Relis le §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

Le log de la densité gaussienne contient $-\frac{(y - \hat{y})^2}{2\sigma^2}$ ; celui de la densité de Laplace, $-\frac{|y - \hat{y}|}{b}$.

</details>
<details><summary>Indice 3</summary>

5 : les résidus sont calculés avec des poids choisis sur ces mêmes données. 6 : pense à la division par $n - 1$ de M02c.

</details>

### M09b.Q8 — Biais, variance, bruit : ce qui change quand le modèle se complique

<details><summary>Indice 1</summary>

Relis « La décomposition d'une erreur de prédiction » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Un modèle plus souple suit mieux $f$ en moyenne, mais suit aussi le bruit de chaque dataset.

</details>
<details><summary>Indice 3</summary>

3 : le bruit dépend-il du modèle ? 6 : les trois termes peuvent-ils être négatifs ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M09b.R1 — Le pivot de Gauss et l'inverse (M09a)

<details><summary>Indice 1</summary>

Relis M09a §6 et §7.

</details>
<details><summary>Indice 2</summary>

Pour 2 : $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

</details>
<details><summary>Indice 3</summary>

5 : une colonne est-elle un multiple de l'autre ?

</details>

### M09b.R2 — Maximum de vraisemblance et MAP (M04)

<details><summary>Indice 1</summary>

Relis M04 (vraisemblance d'une pièce, prior Beta, MAP).

</details>
<details><summary>Indice 2</summary>

Le posterior d'un prior $\mathrm{Beta}(a, b)$ après $k$ piles sur $n$ est $\mathrm{Beta}(a + k, b + n - k)$.

</details>
<details><summary>Indice 3</summary>

Le mode de $\mathrm{Beta}(\alpha, \beta)$ est $\frac{\alpha - 1}{\alpha + \beta - 2}$.

</details>

### M09b.R3 — Gradient et point critique (M05b)

<details><summary>Indice 1</summary>

Relis M05b (dérivées partielles, point critique).

</details>
<details><summary>Indice 2</summary>

Un point critique annule les deux dérivées partielles.

</details>
<details><summary>Indice 3</summary>

De $6y - 2x = 0$, tire $x$ en fonction de $y$ et remplace dans l'autre équation.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M09b.1 — MSE, RMSE, MAE et loss de Huber de quatre résidus

<details><summary>Indice 1</summary>

Relis le §1 de la fiche, et son exemple.

</details>
<details><summary>Indice 2</summary>

Commence par les résidus $y_i - \hat{y}_i$ ; puis, pour Huber, compare chaque $|r_i|$ à $\delta$.

</details>
<details><summary>Indice 3</summary>

d) Seul le résidu de valeur absolue 1 est pile au seuil : $\frac{1}{2}$. f) Avec $\delta = 0{,}25$, tous les résidus sont au-dessus du seuil. g) Pour quels $\delta$ chaque résidu est-il sous le seuil ?

</details>

### Ex M09b.2 — La décomposition SCT = SCE + SCR et le R² d'un ajustement donné

<details><summary>Indice 1</summary>

Relis « Le coefficient de détermination » (fiche §1) et « Le résidu est orthogonal aux colonnes » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Calcule pour chaque droite les cinq prédictions, puis les écarts à $\bar{y}$ et les résidus.

</details>
<details><summary>Indice 3</summary>

d) $\hat{y} - \bar{y} = 0{,}6(x - 5)$. g) $1 - \frac{\mathrm{SCR}}{16}$, à simplifier.

</details>

### Ex M09b.3 — Les gradients de aᵀw, wᵀAw et ‖y − Xw‖², composante par composante en dimension 2

<details><summary>Indice 1</summary>

Relis « Trois identités » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Développe chaque fonction en un polynôme de $w_1$ et $w_2$, puis dérive.

</details>
<details><summary>Indice 3</summary>

c) $\mathbf{w}^\top\mathbf{A}\mathbf{w} = a_{11}w_1^2 + (a_{12} + a_{21})w_1w_2 + a_{22}w_2^2$. g) Calcule d'abord $\mathbf{X}^\top\mathbf{r}$.

</details>

### Ex M09b.4 — Les équations normales d'un modèle à deux features, sans ordonnée à l'origine

<details><summary>Indice 1</summary>

Relis « Le minimum annule le gradient » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\mathbf{X}^\top\mathbf{X}$ contient les produits scalaires des colonnes deux à deux ; $\mathbf{X}^\top\mathbf{y}$, les produits scalaires des colonnes avec $\mathbf{y}$.

</details>
<details><summary>Indice 3</summary>

d) Le déterminant de $\mathbf{X}^\top\mathbf{X}$ vaut 20.

</details>

### Ex M09b.5 — La colonne de 1 : l'ordonnée à l'origine et des résidus de moyenne nulle

<details><summary>Indice 1</summary>

Relis le §3 de la fiche, conséquence 1.

</details>
<details><summary>Indice 2</summary>

$\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} n & \sum x \\ \sum x & \sum x^2 \end{pmatrix}$ et $\mathbf{X}^\top\mathbf{y} = (\sum y, \sum xy)$.

</details>
<details><summary>Indice 3</summary>

c) Le déterminant vaut 56. g) Avec $x - \bar{x}$, $\sum(x - \bar{x}) = 0$.

</details>

### Ex M09b.6 — La matrice chapeau d'un petit tableau : H² = H et sa trace

<details><summary>Indice 1</summary>

Relis « La matrice chapeau » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Calcule d'abord $(\mathbf{X}^\top\mathbf{X})^{-1}$, puis $h_{ij} = (1, x_i)(\mathbf{X}^\top\mathbf{X})^{-1}(1, x_j)^\top$.

</details>
<details><summary>Indice 3</summary>

b) Le déterminant vaut 14. c) $14\,h_{ij} = 10 - 4x_i - 4x_j + 3x_ix_j$.

</details>

### Ex M09b.7 — Compter les monômes des features polynomiales

<details><summary>Indice 1</summary>

Relis « Combien de colonnes ? » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Degré exactement $k$ en $p$ variables : $\binom{k + p - 1}{k}$. Degré au plus $d$ : $\binom{p + d}{d}$, constante comprise.

</details>
<details><summary>Indice 3</summary>

d) $\binom{8}{4} - 1$. f) $\binom{4 + 3 - 1}{4}$. g) Calcule $\binom{7 + d}{d} - 1$ pour $d = 1, 2, 3, \ldots$

</details>

### Ex M09b.8 — Ridge en dimension 2 : résoudre (XᵀX + λI)w = Xᵀy pour trois valeurs de λ

<details><summary>Indice 1</summary>

Relis « Pénaliser les grands poids » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Ajoute $\lambda$ sur les deux nombres de la diagonale de $\mathbf{X}^\top\mathbf{X}$, puis résous un système $2 \times 2$.

</details>
<details><summary>Indice 3</summary>

c) Le déterminant vaut 8. d) Il vaut 15. g) Divise l'équation par $\lambda$.

</details>

### Ex M09b.9 — Ridge comme MAP : un prior gaussien et λ = σ²/τ²

<details><summary>Indice 1</summary>

Relis « Ridge est un MAP » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$\lambda = \frac{\sigma^2}{\tau^2}$ : des variances, pas des écarts-types.

</details>
<details><summary>Indice 3</summary>

c) $\lambda = 2$ : le déterminant de $\mathbf{X}^\top\mathbf{X} + 2\mathbf{I}$ vaut 27. d) Celui de $\mathbf{X}^\top\mathbf{X}$ vaut 9.

</details>

### Ex M09b.10 — Les pénalités L1 et L2 de trois vecteurs de poids, et leurs boules

<details><summary>Indice 1</summary>

Relis le §6 de la fiche, et M07 (normes).

</details>
<details><summary>Indice 2</summary>

$\lVert \mathbf{w} \rVert_1 = \sum |w_j|$ ; la pénalité ridge est $\lVert \mathbf{w} \rVert^2 = \sum w_j^2$, sans racine.

</details>
<details><summary>Indice 3</summary>

e) Paramètre un côté du losange : $(t, 1 - t)$ pour $t \in [0, 1]$, et étudie $t^2 + (1 - t)^2$.

</details>

### Ex M09b.11 — La log-vraisemblance gaussienne d'un modèle linéaire et l'estimation de σ²

<details><summary>Indice 1</summary>

Relis le §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

$\ln L = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{\mathrm{SCR}}{2\sigma^2}$, avec le logarithme népérien.

</details>
<details><summary>Indice 3</summary>

e) À $\sigma^2$ fixé, seul le second terme change d'une droite à l'autre. f) $e^{\text{différence}}$.

</details>

### Ex M09b.12 — L'estimateur rétréci c·x̄ : biais, variance et erreur quadratique

<details><summary>Indice 1</summary>

Relis « Biais et variance d'un estimateur » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[c\,\bar{x}] = c\mu$ et $\mathbb{V}(c\,\bar{x}) = c^2\frac{\sigma^2}{n}$.

</details>
<details><summary>Indice 3</summary>

e) Dérive $E(c) = 4(c - 1)^2 + c^2$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M09b.13 — Le gradient de wᵀAw vaut (A + Aᵀ)w

<details><summary>Indice 1</summary>

Relis « Trois identités » (fiche §2), et R4 pour les doubles sommes.

</details>
<details><summary>Indice 2</summary>

Dérive terme à terme la double somme $\sum_i\sum_j a_{ij}w_iw_j$ par rapport à $w_k$ : seuls comptent les termes où $i = k$ ou $j = k$.

</details>
<details><summary>Indice 3</summary>

Le terme $i = j = k$, $a_{kk}w_k^2$, donne $2a_{kk}w_k$ : un $a_{kk}w_k$ va dans chacune des deux sommes.

</details>

### Ex M09b.14 — Les équations normales en dimension p, par le gradient

<details><summary>Indice 1</summary>

Relis le §2 (identité 3) et le §3 de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour 3, développe $\lVert \mathbf{r}^* - \mathbf{X}\mathbf{v} \rVert^2$ comme un carré $\lVert \mathbf{a} - \mathbf{b} \rVert^2 = \lVert \mathbf{a} \rVert^2 - 2\mathbf{a} \cdot \mathbf{b} + \lVert \mathbf{b} \rVert^2$.

</details>
<details><summary>Indice 3</summary>

Le double produit est $\mathbf{v}^\top\mathbf{X}^\top\mathbf{r}^*$, et les équations normales disent $\mathbf{X}^\top\mathbf{r}^* = \mathbf{0}$.

</details>

### Ex M09b.15 — Le résidu est orthogonal aux colonnes de X ; H est symétrique et idempotente

<details><summary>Indice 1</summary>

Relis « La matrice chapeau » (fiche §3), et M09a §4 et §7.

</details>
<details><summary>Indice 2</summary>

Partout, $(\mathbf{X}^\top\mathbf{X})^{-1}(\mathbf{X}^\top\mathbf{X}) = \mathbf{I}$ se simplifie.

</details>
<details><summary>Indice 3</summary>

5 : avec $\mathbf{A} = \mathbf{X}$ et $\mathbf{B} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$ et $\mathbf{B}\mathbf{A} = \mathbf{I}_p$. 6 : la première ligne de $\mathbf{X}^\top$ est faite de 1.

</details>

### Ex M09b.16 — XᵀX + λI est inversible pour tout λ > 0

<details><summary>Indice 1</summary>

Relis « Pénaliser les grands poids » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Multiplie $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ à gauche par $\mathbf{v}^\top$, et utilise 1.

</details>
<details><summary>Indice 3</summary>

6 : le déterminant de $\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}$ est un polynôme en $\lambda$ ; cherche ses racines.

</details>

### Ex M09b.17 — Un bruit gaussien mène aux moindres carrés : le maximum de vraisemblance

<details><summary>Indice 1</summary>

Relis le §7 de la fiche, et M04.

</details>
<details><summary>Indice 2</summary>

Le log d'un produit est la somme des logs ; le log d'une exponentielle est son exposant.

</details>
<details><summary>Indice 3</summary>

4 : dérive par rapport à $s = \sigma^2$, en voyant $\mathrm{SCR}$ comme un nombre fixé.

</details>

### Ex M09b.18 — La décomposition biais² + variance + bruit, démontrée

<details><summary>Indice 1</summary>

Relis « Biais et variance d'un estimateur » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Ajoute et retire $\mathbb{E}[\hat{\theta}]$, puis développe le carré.

</details>
<details><summary>Indice 3</summary>

3 : un double produit est nul parce que $\mathbb{E}[\varepsilon] = 0$, un autre par l'indépendance, le troisième par la définition de $\bar{f}$.

</details>

### Ex M09b.19 — Le nombre de monômes de degré au plus d en p variables : C(p + d, d)

<details><summary>Indice 1</summary>

Relis « Combien de colonnes ? » (fiche §4), et R8 (combinaisons).

</details>
<details><summary>Indice 2</summary>

Une suite de $k$ étoiles et $p - 1$ barres est déterminée par la position de ses étoiles.

</details>
<details><summary>Indice 3</summary>

3 : ajoute une variable d'écart $k_0 = d - (k_1 + \cdots + k_p)$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09b.20 — Pont : la loss d'un modèle linéaire et son gradient pour un batch, prêts pour la descente de gradient

<details><summary>Indice 1</summary>

Relis le §2 de la fiche (identité 3, et la MSE).

</details>
<details><summary>Indice 2</summary>

$\nabla\mathrm{MSE} = -\frac{2}{n}\mathbf{X}^\top\mathbf{r}$, puis $\mathbf{w} \leftarrow \mathbf{w} - \eta\nabla\mathrm{MSE}$.

</details>
<details><summary>Indice 3</summary>

e) $-\frac{2}{4} = -0{,}5$ fois $\mathbf{X}^\top\mathbf{r}$.

</details>

### Ex M09b.21 — Pont : pourquoi standardiser les colonnes avant ridge

<details><summary>Indice 1</summary>

Relis l'erreur classique du §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

Chaque question est un système $2 \times 2$ : forme $\mathbf{X}^\top\mathbf{X}$ (plus $\lambda\mathbf{I}$ pour ridge) et $\mathbf{X}^\top\mathbf{y}$, puis inverse la matrice $2 \times 2$.

</details>
<details><summary>Indice 3</summary>

c) et d) En euros, la colonne du prix vaut $10\,x_1$ : $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 400 & 20 \\ 20 & 2 \end{pmatrix}$ et $\mathbf{X}^\top\mathbf{y} = (40, 3)$. e) Le premier exemple a $x_1 = -10$ en euros.

</details>

### Ex M09b.22 — MML §5.5, §8.1 et §8.2 : identités de gradients et minimisation du risque empirique

<details><summary>Indice 1</summary>

Lis d'abord MML §8.1 et §8.2 en entier, puis cherche dans §5.5 les identités avec $\mathbf{a}^\top\mathbf{x}$ et $\mathbf{x}^\top\mathbf{B}\mathbf{x}$.

</details>
<details><summary>Indice 2</summary>

Les sous-titres du §8.2 répondent presque aux questions 2 à 4.

</details>
<details><summary>Indice 3</summary>

5 : le livre écrit les gradients en lignes (voir la note 📐 du guide de lecture de la fiche).

</details>

### Ex M09b.23 — MML §9.1 et §9.2 : régression linéaire, maximum de vraisemblance et MAP

<details><summary>Indice 1</summary>

Lis MML §9.1 et §9.2 en entier, avec la fiche §3, §5 et §7 à côté.

</details>
<details><summary>Indice 2</summary>

Le livre note la variance du prior autrement que la fiche : repère son symbole.

</details>
<details><summary>Indice 3</summary>

6 : le $\lambda$ s'écrit comme un rapport de deux variances.

</details>

### Ex M09b.24 — Fermi : la taille de XᵀX pour des features polynomiales de degré 3 sur 100 variables

<details><summary>Indice 1</summary>

Relis « Combien de colonnes ? » (fiche §4) et le coût d'un produit (M09a §3).

</details>
<details><summary>Indice 2</summary>

$\binom{103}{3} - 1$ colonnes ; $\mathbf{X}^\top\mathbf{X}$ en a le carré.

</details>
<details><summary>Indice 3</summary>

3 : un produit $(p, n) \times (n, p)$ coûte $n\,p^2$ multiplications.

</details>

### Ex M09b.25 — Expliquer la matrice chapeau : ce que veut dire « projeter y »

<details><summary>Indice 1</summary>

Relis « La projection de $\mathbf{y}$ » et « La matrice chapeau » (fiche §3), et regarde la figure.

</details>
<details><summary>Indice 2</summary>

Trouve une image du quotidien pour « le point d'un plan le plus proche d'un point ».

</details>
<details><summary>Indice 3</summary>

Pense à l'ombre d'un objet sous une lampe placée juste au-dessus : la projeter une seconde fois ne la déplace pas.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M09b.E1 — « Pourquoi ne pas inverser XᵀX, et que faire si des features sont colinéaires ? »

<details><summary>Indice 1</summary>

Relis le §3 (« Aujourd'hui en pratique ») et le §5 de la fiche, et M09a §7.

</details>
<details><summary>Indice 2</summary>

Trois idées : résoudre plutôt qu'inverser ; `lstsq` évite même de former $\mathbf{X}^\top\mathbf{X}$ ; la colinéarité rend la solution non unique ou instable.

</details>
<details><summary>Indice 3</summary>

Remèdes : ridge, retirer une feature redondante, la plus petite norme, une ACP.

</details>

### M09b.E2 — « Quel lien entre la régularisation L2 et un prior gaussien ? »

<details><summary>Indice 1</summary>

Relis « Ridge est un MAP » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Écris le log du posterior : un terme vient de la vraisemblance, l'autre du prior.

</details>
<details><summary>Indice 3</summary>

Multiplie par $-2\sigma^2$ pour retrouver la loss de ridge, et lis le coefficient de $\lVert \mathbf{w} \rVert^2$.

</details>

<a id="notebook"></a>

## Notebook

### Ex M09b.26 — Équations normales et résolution, avec ou sans ridge · `normal_equations, solve_least_squares`

<details><summary>Indice 1</summary>

Lis les deux docstrings ; `np.linalg.solve` est permis.

</details>
<details><summary>Indice 2</summary>

`normal_equations` : vérifie les formes (`X.ndim == 2`, `y.ndim == 1` et une valeur de `y` par ligne de `X`), puis `X.T @ X` et `X.T @ y`. `solve_least_squares` : ajoute `ridge * np.eye(p)`.

</details>
<details><summary>Indice 3</summary>

`try: return np.linalg.solve(A, Xty)` puis `except np.linalg.LinAlgError: raise ValueError(...)` ; teste `if not ridge >= 0` (ce test refuse aussi `nan`).

</details>

### Ex M09b.27 — La matrice chapeau et les trois sommes de carrés · `hat_matrix, residual_decomposition`

<details><summary>Indice 1</summary>

Lis les deux docstrings, et la fiche §1 et §3.

</details>
<details><summary>Indice 2</summary>

`np.linalg.solve(X.T @ X, X.T)` résout pour toutes les colonnes de $\mathbf{X}^\top$ d'un coup.

</details>
<details><summary>Indice 3</summary>

`H = X @ np.linalg.solve(X.T @ X, X.T)` ; les trois sommes autour de `y.mean()`, chacune convertie par `float(...)`.

</details>

### Ex M09b.28 — Compter les monômes, et la loss de Huber · `count_monomials, huber_loss`

<details><summary>Indice 1</summary>

Lis les deux docstrings, et la fiche §1 et §4.

</details>
<details><summary>Indice 2</summary>

`math.comb(p + degree, degree)`, moins 1 sans la constante. Pour Huber, `np.where(condition, valeur_si_vrai, valeur_si_faux)`.

</details>
<details><summary>Indice 3</summary>

`a = np.abs(r)` puis `np.where(a <= delta, r ** 2 / 2, delta * (a - delta / 2))`, et la moyenne.

</details>

### Ex M09b.29 — `np.linalg.lstsq` et scikit-learn contre tes équations normales

<details><summary>Indice 1</summary>

Relis l'énoncé : ce que rend chaque fonction.

</details>
<details><summary>Indice 2</summary>

`np.linalg.lstsq(...)` rend quatre objets : la solution est le premier, le rang le troisième.

</details>
<details><summary>Indice 3</summary>

d) `[ridge.intercept_, *ridge.coef_]`. f) Compare les valeurs absolues des premiers nombres de d) et de e).

</details>

### Ex M09b.30 — Prédire : le R² d'entraînement quand on ajoute une feature de pur bruit

<details><summary>Indice 1</summary>

Relis le §1 (le $R^2$) et le §8 (la variance) de la fiche.

</details>
<details><summary>Indice 2</summary>

a) Quel poids donner à la nouvelle colonne pour retrouver l'ancien ajustement ?

</details>
<details><summary>Indice 3</summary>

b) Combien de colonnes faut-il pour que $\mathbf{X}$ soit carrée ?

</details>

### Ex M09b.31 — Simuler l'estimateur rétréci c·x̄ : le c qui minimise l'erreur quadratique

<details><summary>Indice 1</summary>

Relis la fiche §8 et M09b.12.

</details>
<details><summary>Indice 2</summary>

Tire **une fois** les échantillons, de forme `(reps, n)`, et calcule les moyennes par ligne (`axis=1`).

</details>
<details><summary>Indice 3</summary>

`np.array([np.mean((c * means - mu) ** 2) for c in cs])` ; c) $c^* = \frac{\mu^2}{\mu^2 + \sigma^2/n}$.

</details>

### Ex M09b.32 — Le conditionnement de XᵀX avec des puissances non standardisées

<details><summary>Indice 1</summary>

Relis « Des colonnes presque dépendantes » (fiche §4).

</details>
<details><summary>Indice 2</summary>

`np.column_stack([x ** k for k in range(degree + 1)])`, puis `np.linalg.cond(X.T @ X)`.

</details>
<details><summary>Indice 3</summary>

c) Une boucle sur les degrés de 1 à 8, et le premier conditionnement au-dessus de $10^{15}$.

</details>

### Ex M09b.33 — Les lignes de niveau de la loss des moindres carrés en dimension 2, et son gradient

<details><summary>Indice 1</summary>

Relis le §2 et le §3 de la fiche, et le 🎨 de M05b (lignes de niveau et flèches).

</details>
<details><summary>Indice 2</summary>

Une grille fine de poids pour `ax.contour`, une grille grossière pour `ax.quiver`, la solution des équations normales pour le point.

</details>
<details><summary>Indice 3</summary>

Calcule $L$ en chaque point de la grille (une double boucle suffit ; NumPy et le broadcasting vont plus vite) ; des niveaux `L_min + np.geomspace(0.05, 50, 10)` montrent la vallée ; pour les flèches, $-\nabla L(\mathbf{w}) = 2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$.

</details>

### Ex M09b.34 — Chasse à l'erreur : XXᵀ au lieu de XᵀX, un gradient de mauvais signe, un R² sans centrer

<details><summary>Indice 1</summary>

Relis le récapitulatif des pièges de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, écris la forme du résultat et refais le calcul à la main sur ce petit exemple.

</details>
<details><summary>Indice 3</summary>

Trois lignes sont fausses ; une ligne qui ajoute au lieu de retrancher peut être juste, selon le signe de ce qu'elle ajoute.

</details>

### Ex M09b.35 — Vérifier un gradient matriciel avec SymPy et par différences finies

<details><summary>Indice 1</summary>

Relis M05a (différences finies) et la fiche §2.

</details>
<details><summary>Indice 2</summary>

Pour chaque coordonnée $k$, un vecteur nul sauf en $k$, où il vaut $h$ ; la différence centrée divise par $2h$.

</details>
<details><summary>Indice 3</summary>

SymPy : `sympy.Matrix(sympy.symbols('w1:4'))`, `sympy.Matrix(3, 3, sympy.symbols('a1:10'))`, `(w.T * A * w)[0, 0]`, puis `sympy.diff`.

</details>

### Ex M09b.36 — Défi : approcher une fonction par un polynôme de degré au plus 5, avec une erreur maximale sous 1e−3

<details><summary>Indice 1</summary>

Commence par les moindres carrés sur la grille, et regarde **où** l'erreur maximale est atteinte.

</details>
<details><summary>Indice 2</summary>

Les moindres carrés minimisent une somme : pour faire baisser l'erreur aux bords, il faut que les bords pèsent plus dans cette somme.

</details>
<details><summary>Indice 3</summary>

Des points plus serrés près de $t = \pm 1$ : les points de Tchebychev $t_k = \cos\frac{(2k + 1)\pi}{2m}$, avec $m = 30$ par exemple.

</details>
