# M21 · Convolution, matrices de Toeplitz et équivariance — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M21.Q1 — Convolution ou corrélation : retourner, glisser, sommer

<details><summary>Indice 1</summary>

Relis « Le lien : retourner le noyau » et l'encadré 📐 du §2.

</details>
<details><summary>Indice 2</summary>

Le noyau retourné lit le noyau à l'envers. Un noyau antisymétrique vérifie $\tilde{\mathbf{w}} = -\mathbf{w}$. Dans $(\mathbf{a} * \mathbf{b})_m$, les deux indices ont pour somme $m$.

</details>
<details><summary>Indice 3</summary>

3. Les couples $(i, 4 - i)$ avec $0 \le i \le 2$ et $0 \le 4 - i \le 4$. 5. `np.correlate` pose les poids tels quels sur la fenêtre ; `np.convolve` les retourne d'abord : donne-lui les poids dans l'ordre inverse.

</details>

### M21.Q2 — Les propriétés de la convolution : vrai ou faux

<details><summary>Indice 1</summary>

Relis l'encadré « Propriétés » du §1 et le point de vue des polynômes.

</details>
<details><summary>Indice 2</summary>

2. Évalue les deux polynômes en $X = 1$. 5. Écris $(\mathbf{a} * (0, 0, 1))_m$ avec la définition. 6. Sur une portion constante, chaque valeur complète vaut la constante fois une somme.

</details>
<details><summary>Indice 3</summary>

5. $(\mathbf{a} * (0, 0, 1))_m = a_{m-2}$ : la valeur d'indice $m$ est celle qui était à l'indice $m - 2$. 6. La somme du noyau vaut $0{,}5 + 2 - 1$.

</details>

### M21.Q3 — Lire une matrice de Toeplitz : diagonales, coefficients non nuls, nombre de lignes

<details><summary>Indice 1</summary>

Relis « La matrice d'une convolution » et « Une matrice creuse » (§3), puis la définition de la matrice circulante (§4).

</details>
<details><summary>Indice 2</summary>

La colonne $j$ est le noyau descendu de $j$ lignes ; $T_{ij} = w_{i-j}$. Le mode plein a $n + k - 1$ lignes, le mode valide $n - k + 1$, le mode même taille $n$.

</details>
<details><summary>Indice 3</summary>

1. Lis la première colonne et compte les colonnes. 2. $k$ coefficients non nuls par colonne, et $n$ colonnes. 4. Regarde la diagonale juste sous la diagonale principale. 5. Chaque colonne est-elle la précédente descendue d'une case, la dernière case remontant en haut ?

</details>

### M21.Q4 — Équivariant, invariant, ou ni l'un ni l'autre ? Décalages, bords, pas et pooling

<details><summary>Indice 1</summary>

Relis les définitions du §4 : équivariante si $F(\tau_t\mathbf{x}) = \tau_tF(\mathbf{x})$, invariante si $F(\tau_t\mathbf{x}) = F(\mathbf{x})$.

</details>
<details><summary>Indice 2</summary>

Pour chaque application, remplace $\mathbf{x}$ par $\tau_t\mathbf{x}$, c'est-à-dire $x_i$ par $x_{i-t}$, et regarde si la sortie se déplace, ne bouge pas, ou change de nombres.

</details>
<details><summary>Indice 3</summary>

3. $(F(\tau_t\mathbf{x}))_i = i\,x_{i-t}$, alors que $(\tau_tF(\mathbf{x}))_i = (i - t)\,x_{i-t}$. 5. $(\tau_6\mathbf{x})_{3i} = x_{3i-6} = x_{3(i-2)}$ ; avec un décalage de 2, on lit $x_{3i-2}$.

</details>

### M21.Q5 — Combien de positions ? Pas, dilatation, padding et insertion de zéros

<details><summary>Indice 1</summary>

Relis le théorème « Compter les positions » et le paragraphe « Même taille » du §5.

</details>
<details><summary>Indice 2</summary>

$\big\lfloor\frac{n + 2p - d(k - 1) - 1}{s}\big\rfloor + 1$ ; l'étendue d'une fenêtre dilatée vaut $d(k - 1) + 1$. Entre $m$ valeurs, il y a $m - 1$ intervalles.

</details>
<details><summary>Indice 3</summary>

3. L'étendue vaut $4 \times 2 + 1$. 5. Chacun des 5 intervalles devient 4 cases. 6. Les fenêtres commencent en $0, 4, 8, \ldots$ ; quelle est la dernière case de la dernière fenêtre ?

</details>

### M21.Q6 — Canaux, groupes, convolution 1 × 1 et noyaux séparables : compter

<details><summary>Indice 1</summary>

Relis l'encadré « Comptes » et les trois cas particuliers du §6, puis « Noyaux séparables ».

</details>
<details><summary>Indice 2</summary>

Paramètres : $C_{\text{out}}\big(\frac{C_{\text{in}}}{g}k_hk_w + 1\big)$. La forme des poids est $(C_{\text{out}}, C_{\text{in}}, k_h, k_w)$. Un noyau est séparable quand il est de rang 1.

</details>
<details><summary>Indice 3</summary>

2. Chaque sortie lit $\frac{10}{2} = 5$ canaux. 3. Une convolution par canal a autant de sorties que de canaux, et chacune lit un seul canal. 6. Compare les deux lignes de la matrice.

</details>

### M21.Q7 — Composer des convolutions : noyau, pas et champ récepteur

<details><summary>Indice 1</summary>

Relis le §7 : « Deux filtres d'affilée », « Avec un pas » et le théorème du champ récepteur.

</details>
<details><summary>Indice 2</summary>

Le noyau équivalent de deux étages de pas 1 est la convolution des deux noyaux, de longueur $k_1 + k_2 - 1$. Le pas total est le produit des pas. $r_\ell = r_{\ell-1} + d_\ell(k_\ell - 1)J_{\ell-1}$, $J_\ell = J_{\ell-1}s_\ell$.

</details>
<details><summary>Indice 3</summary>

2. $(3, 1) * (1, -2)$ : trois termes. 4. $r$ passe de 1 à 2, puis la contribution de l'étage 2 est multipliée par 2, celle de l'étage 3 par 4. 6. Calcule $r$ dans les deux ordres.

</details>

### M21.Q8 — Le pire cas d'une perturbation bornée : quelle norme, quel vecteur ?

<details><summary>Indice 1</summary>

Relis le théorème du §8 et l'erreur classique qui le suit.

</details>
<details><summary>Indice 2</summary>

Boule L∞ → norme L1 de $\mathbf{g}$, en $\varepsilon\operatorname{signe}(\mathbf{g})$ ; boule L2 → norme L2 ; boule L1 → norme L∞.

</details>
<details><summary>Indice 3</summary>

1. $\lVert\mathbf{g}\rVert_1 = 1 + 4 + 2 + 0 + 2$. 2. Que vaut $g_4\delta_4$, quel que soit $\delta_4$ ? 3. $\lVert\mathbf{g}\rVert_2 = \sqrt{1 + 16 + 4 + 0 + 4}$. 6. Chaque coordonnée vaut $\pm0{,}3$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M21.R1 — La moyenne mobile d'une suite (R5)

<details><summary>Indice 1</summary>

Relis le paragraphe « Une moyenne mobile » du §1.

</details>
<details><summary>Indice 2</summary>

Une moyenne mobile sur $k$ valeurs a une valeur complète par fenêtre de $k$ valeurs consécutives. Deux moyennes voisines ont $k - 1$ valeurs en commun.

</details>
<details><summary>Indice 3</summary>

1. $\frac{12 + 3 + 9}{3}$, puis on glisse d'une valeur. 4. $\sum_i x_i\,h_{t-i}$ ne doit garder que $i = t - 2, t - 1, t$, chacun avec le poids $\frac13$.

</details>

### M21.R2 — La matrice d'une application linéaire, son noyau et son rang (M12a)

<details><summary>Indice 1</summary>

Relis M12a : la matrice d'une application linéaire et le théorème du rang.

</details>
<details><summary>Indice 2</summary>

Les lignes de la matrice sont les coefficients de chaque coordonnée de $f$. Le rang d'une matrice $2 \times 3$ vaut au plus 2.

</details>
<details><summary>Indice 3</summary>

4. Résous $3y + z = 0$ et $x + 2y - z = 0$ en fonction de $y$. 6. $\dim\ker = 4 - \operatorname{rg} \ge 4 - 2$.

</details>

### M21.R3 — Le rang d'un produit extérieur u vᵀ et la décomposition en valeurs singulières (M12d)

<details><summary>Indice 1</summary>

Relis M12d : la décomposition en valeurs singulières, et Eckart-Young.

</details>
<details><summary>Indice 2</summary>

$(\mathbf{u}\mathbf{v}^\top)_{ij} = u_iv_j$ ; toutes ses lignes sont des multiples de $\mathbf{v}^\top$. $\mathbf{u}\mathbf{v}^\top = \lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\,\frac{\mathbf{u}}{\lVert\mathbf{u}\rVert}\frac{\mathbf{v}^\top}{\lVert\mathbf{v}\rVert}$.

</details>
<details><summary>Indice 3</summary>

3. $\lVert\mathbf{u}\rVert = 3$ et $\lVert\mathbf{v}\rVert = 5$. 6. L'erreur de Frobenius du meilleur approximant de rang 1 est la racine de la somme des carrés des valeurs singulières oubliées.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M21.1 — Deux dés truqués et un produit de polynômes : la même convolution

<details><summary>Indice 1</summary>

Relis « Trois calculs, une seule opération » (§1) : le tableau des produits et ses anti-diagonales, puis la loi de la somme de deux dés.

</details>
<details><summary>Indice 2</summary>

Le coefficient de $X^m$ est la somme des $a_ib_j$ avec $i + j = m$. $P(A = i) = \frac{a_{i-1}}{6}$ et $P(B = j) = \frac{b_{j-1}}{8}$ : les faces commencent à 1, les indices à 0.

</details>
<details><summary>Indice 3</summary>

b) $S = 5$ correspond à $m = 5 - 2$. d) $\mathbb{E}[S] = \mathbb{E}[A] + \mathbb{E}[B]$, ou $\sum_m (m + 2)\frac{c_m}{48}$. g) Convolue a) par $(3, 2, 1)$ : seuls les deux derniers coefficients ($A + B + A' = 9$ et $10$) servent, sur $48 \times 6$.

</details>

### Ex M21.2 — Convoluer et corréler un signal à la main, dans les trois modes

<details><summary>Indice 1</summary>

Relis le §2 : la définition de la corrélation croisée, le lien par le noyau retourné, et « Trois modes ».

</details>
<details><summary>Indice 2</summary>

a) La fenêtre $i$ couvre $x_i, x_{i+1}, x_{i+2}$, multipliés par $w_0, w_1, w_2$. b) $(\mathbf{x} * \mathbf{w})_m = \sum_i x_i\,w_{m-i}$, 9 valeurs. c) Les indices $k - 1$ à $n - 1$ de b). d) $n$ valeurs à partir de l'indice $\lfloor\frac{k-1}{2}\rfloor$ de b).

</details>
<details><summary>Indice 3</summary>

b) Les deux premières valeurs : $3 \times 4 = 12$, puis $3 \times (-1) + (-2) \times 4$. c) Ou fais glisser $\tilde{\mathbf{w}} = (2, -1, 4)$ sur le signal : $6 + 2 + 0$ pour la première. g) La somme d'une convolution est le produit des sommes.

</details>

### Ex M21.3 — Des pochoirs de différences finies : dérivée et dérivée seconde d'un signal échantillonné

<details><summary>Indice 1</summary>

Relis « Les pochoirs de différences finies » (§2) et, dans M05a, l'erreur de chaque différence.

</details>
<details><summary>Indice 2</summary>

Les dénominateurs : $h$, $2h$ et $h^2$, avec $h = 2$. $f'(t) = \frac{3t^2}{4}$, $f''(t) = \frac{3t}{2}$, $f''' = \frac32$. L'erreur de la différence centrée vaut $\frac{h^2}{6}f'''$.

</details>
<details><summary>Indice 3</summary>

b) En $t = 2$ : $\frac{16 - 0}{4}$. d) $f'(4) = 12$. e) $f'(2) = 3$ et $f'(3) = \frac{27}{4}$. f) Écris le premier terme de `np.convolve(f, [-1, 0, 1], "valid")` : $-f_2 + f_0$ ou $f_2 - f_0$ ?

</details>

### Ex M21.4 — La matrice de Toeplitz d'une convolution pleine et d'une convolution valide : coefficients non nuls, rang et noyau

<details><summary>Indice 1</summary>

Relis le §3 : « La matrice d'une convolution », « Rang et noyau » et l'énoncé de « La transposée ».

</details>
<details><summary>Indice 2</summary>

$T_{ij} = w_{i-j}$, de forme $(7, 5)$ ; le mode valide garde les lignes 2 à 4. Une matrice échelonnée a pour rang son nombre de lignes non nulles. $\dim\ker = n - \operatorname{rg}$.

</details>
<details><summary>Indice 3</summary>

c) Le produit $(2 - X^2 + 3X^3 + X^4)(1 - 3X + 2X^2)$. g) Calcule $2x_r - 3x_{r+1} + x_{r+2}$ pour $r = 0, 1, 2$. i) Les colonnes de $\mathbf{V}^\top$ sont les lignes de $\mathbf{V}$, lues de haut en bas.

</details>

### Ex M21.5 — Décaler puis filtrer, ou filtrer puis décaler : l'équivariance, ses bords et son pas

<details><summary>Indice 1</summary>

Relis le §4 : « Décaler puis filtrer », « Les bords » et « Le pas ».

</details>
<details><summary>Indice 2</summary>

a) $y_i = x_i - x_{i+1} + 2x_{i+2}$, pour $i = 0$ à 7. Avec un pas de 2, $y_i$ est la valeur $2i$ de la sortie de pas 1.

</details>
<details><summary>Indice 3</summary>

c) Avec $\tau_5$, l'événement occupe les cases 7 à 9 ; la réponse complète aurait besoin des positions 8 et 9. e) La sortie de pas 1 de $\tau_1\mathbf{x}$ est a) décalée d'une case : garde ses valeurs d'indices pairs.

</details>

### Ex M21.6 — Compter les positions d'une fenêtre : pas, dilatation, padding, « même taille » avec un pas, et le problème inverse

<details><summary>Indice 1</summary>

Relis le §5 : le théorème « Compter les positions », ses exemples (dont « À l'envers »), et « Même taille » avec un pas.

</details>
<details><summary>Indice 2</summary>

$n_{\text{out}} = \big\lfloor\frac{n + 2p - d(k - 1) - 1}{s}\big\rfloor + 1$. En « même taille » avec un pas : $n_{\text{out}} = \lceil\frac ns\rceil$ et $P_{\text{tot}} = (n_{\text{out}} - 1)s + d(k - 1) + 1 - n$ zéros, $\lfloor\frac{P_{\text{tot}}}{2}\rfloor$ au début.

</details>
<details><summary>Indice 3</summary>

b) $\lfloor\frac{997}{3}\rfloor + 1$. d) $\lfloor\frac{981}{5}\rfloor + 1$. g) Encadre : $49 \le \frac{n - 5}{5} < 50$. h) $\lfloor\frac{993}{s}\rfloor = 99$ veut dire $99 \le \frac{993}{s} < 100$.

</details>

### Ex M21.7 — Sous-échantillonner et insérer des zéros : la convolution transposée d'un signal et ses recouvrements

<details><summary>Indice 1</summary>

Relis le §5 : « Sous-échantillonner, insérer des zéros » et « La convolution transposée » (la recette, les tampons, la taille, les recouvrements).

</details>
<details><summary>Indice 2</summary>

Taille : $(m - 1)s + k + p_{\text{out}}$ pour $p = 0$ et $d = 1$. Recette : insérer $s - 1$ zéros entre les valeurs, puis convoluer en mode plein par $\mathbf{w}$ ; ou poser $y_i\,\mathbf{w}$ à partir de la case $si$.

</details>
<details><summary>Indice 3</summary>

d) Les tampons $3\mathbf{w}$ sur les cases 0 à 4, $\mathbf{w}$ sur 3 à 7, $-2\mathbf{w}$ sur 6 à 10 ; additionne case par case. e) Compte, pour chaque case $j$, les $i \in \{0, 1, 2\}$ tels que $0 \le j - 3i \le 4$. f) $\lfloor\frac{n - 5}{3}\rfloor + 1 = 3$.

</details>

### Ex M21.8 — Une carte de températures filtrée par un laplacien discret et par un lissage séparable

<details><summary>Indice 1</summary>

Relis le §6 : « La corrélation en deux dimensions », son exemple du laplacien, et « Noyaux séparables ».

</details>
<details><summary>Indice 2</summary>

La sortie $(i, j)$ est centrée sur la case $(i + 1, j + 1)$ de $\mathbf{T}$ : les quatre voisines moins 4 fois la case. Le lissage en deux passes : d'abord chaque colonne par $\mathbf{a}$ (2 valeurs par colonne), puis chaque ligne du résultat par $\mathbf{a}$.

</details>
<details><summary>Indice 3</summary>

a) En $(1, 4)$ : $15 + 14 + 19 + 17 - 4 \times 12$. d) Colonne 0 : $\frac{14 + 3 \times 15 + 16}{5}$. e) $\frac{15 + 3 \times 17{,}8 + 20{,}8}{5}$ pour la première. f) Compte les valeurs calculées par chaque passe, et 3 produits pour chacune.

</details>

### Ex M21.9 — Paramètres et coût d'un filtrage à plusieurs canaux : standard, groupé, par canal, 1 × 1

<details><summary>Indice 1</summary>

Relis l'encadré « Comptes » du §6 et son exemple de la grille météo.

</details>
<details><summary>Indice 2</summary>

Paramètres : $C_{\text{out}}\big(\frac{C_{\text{in}}}{g}k_hk_w + 1\big)$. Coût : $H_{\text{out}}W_{\text{out}}\,C_{\text{out}}\frac{C_{\text{in}}}{g}k_hk_w$. Avec $p = 2$ et $k = 5$, la sortie de pas 1 garde la taille.

</details>
<details><summary>Indice 3</summary>

b) $20 \times (12 \times 25 + 1)$. d) Chaque sortie lit $\frac{12}{4} = 3$ bandes. h) $\lfloor\frac{200 + 4 - 4 - 1}{2}\rfloor + 1$ et de même pour 300. i) $20 \times 200 \times 300$ valeurs, 4 octets chacune.

</details>

### Ex M21.10 — Le noyau équivalent de deux lissages successifs, et le champ récepteur d'une pile avec pas et dilatation

<details><summary>Indice 1</summary>

Relis le §7 : « Deux filtres d'affilée », « Avec un pas » et le théorème du champ récepteur.

</details>
<details><summary>Indice 2</summary>

Le noyau équivalent est $\mathbf{a} * \mathbf{b}$ (pas 1) ; avec un pas $s_1$, c'est $\mathbf{a} * (\mathbf{b}$ dilaté de $s_1)$. Pour la pile : $r_\ell = r_{\ell-1} + d_\ell(k_\ell - 1)J_{\ell-1}$, $J_\ell = J_{\ell-1}s_\ell$ ; la sortie $z_j$ va de la case $Sj$ à $Sj + r - 1$.

</details>
<details><summary>Indice 3</summary>

a) $(1, 1) * (1, 1, 1)$, divisé par 6. c) $\mathbf{b}$ dilaté de 2 : $\frac13(1, 0, 1, 0, 1)$. e) Le tableau : $r = 1, 2, 10, \ldots$ avec $J = 1, 2, 8, 8$.

</details>

### Ex M21.11 — Le pire cas d'une erreur de capteurs bornée : une forme linéaire sur les boules L∞ et L2

<details><summary>Indice 1</summary>

Relis le §8 : le théorème, l'exemple des thermomètres et « En grande dimension ».

</details>
<details><summary>Indice 2</summary>

Boule L∞ : $\varepsilon\lVert\mathbf{g}\rVert_1$, en $\varepsilon\operatorname{signe}(\mathbf{g})$. Boule L2 : $\varepsilon\lVert\mathbf{g}\rVert_2$. Boule L1 : $\varepsilon\lVert\mathbf{g}\rVert_\infty$. Le laplacien est une forme linéaire des 5 températures de sa fenêtre.

</details>
<details><summary>Indice 3</summary>

d) $\lVert\mathbf{g}\rVert_2 = \sqrt{4 + 25 + 1 + 9 + 1}$. e) Cinq coordonnées de 0,25. g) Les coefficients du pochoir sont $1, 1, 1, 1$ et $-4$. h) $\lVert\mathbf{g}\rVert_1 = 2\,500 \times 0{,}02$ et $\lVert\mathbf{g}\rVert_2 = \sqrt{2\,500 \times 0{,}02^2}$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M21.12 — La convolution est commutative et associative ; la corrélation croisée ne l'est pas

<details><summary>Indice 1</summary>

Relis le §1 (les propriétés et le point de vue des polynômes) et le lien du §2 entre corrélation et convolution.

</details>
<details><summary>Indice 2</summary>

1. Avec la convention « nul hors des indices », tu peux sommer sur tous les entiers. 3. Écris $(\widetilde{\mathbf{u} * \mathbf{v}})_m = (\mathbf{u} * \mathbf{v})_{n+k-2-m}$, puis change d'indice. 4. Pose $v = n - 1 - u$ dans la définition de la corrélation pleine.

</details>
<details><summary>Indice 3</summary>

4. Pour la seconde égalité, applique 3 à $\tilde{\mathbf{a}} * \mathbf{b}$. 5. $(\mathbf{a} \star \mathbf{b}) \star \mathbf{c}$ s'écrit avec $\mathbf{a}$, et $\mathbf{a} \star (\mathbf{b} \star \mathbf{c})$ avec $\tilde{\mathbf{a}}$ : prends une suite $\mathbf{a}$ qui n'est pas symétrique, comme $(1, 0)$, et $\mathbf{b} = \mathbf{c} = (1)$.

</details>

### Ex M21.13 — Les applications linéaires qui commutent avec le décalage circulaire sont les convolutions circulaires ; la transposée d'une matrice circulante

<details><summary>Indice 1</summary>

Relis « Les convolutions circulaires » (§4) : la définition de $\mathbf{P}$, de $\operatorname{circ}(\mathbf{h})$ et l'idée de la démonstration ($\mathbf{e}_j = \mathbf{P}^j\mathbf{e}_0$).

</details>
<details><summary>Indice 2</summary>

3. Si $\mathbf{A}$ commute avec $\mathbf{P}$, elle commute avec ses puissances ; alors $\mathbf{A}\mathbf{e}_j = \mathbf{A}\mathbf{P}^j\mathbf{e}_0$. 4. Calcule le coefficient $(i, j)$ de $\mathbf{P}^m$ : il vaut 1 exactement quand $(i - j) \bmod n = m$.

</details>
<details><summary>Indice 3</summary>

6. Le coefficient $(i, j)$ de la transposée est $h_{(j-i) \bmod n}$ ; écris-le $\check h_{(i-j) \bmod n}$. Pour l'exemple, $\check{\mathbf{h}} = (h_0, h_4, h_3, h_2, h_1)$ ; compare-le au renversement, case par case, et cherche le décalage.

</details>

### Ex M21.14 — Le nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 quand la fenêtre tient, par un dénombrement

<details><summary>Indice 1</summary>

Relis le théorème « Compter les positions » (§5) et son idée : une position existe quand la dernière case de sa fenêtre reste dans le signal complété.

</details>
<details><summary>Indice 2</summary>

1. La dernière case lue par la fenêtre $i$ est $si + d(k - 1)$ ; le signal complété a $n + 2p$ cases. 2. Les entiers de $[0, x]$, pour $x \ge 0$, sont $0, 1, \ldots, \lfloor x\rfloor$.

</details>
<details><summary>Indice 3</summary>

4. $\lfloor\frac As\rfloor = q$ équivaut à $qs \le A \le qs + s - 1$. 5. Calcule $A$ avec $P_{\text{tot}}$ à la place de $2p$ : il vaut exactement $(n_{\text{out}} - 1)s$.

</details>

### Ex M21.15 — Le champ récepteur d'une pile de convolutions : récurrence et forme close

<details><summary>Indice 1</summary>

Relis le théorème du champ récepteur (§7), la définition du champ récepteur (une plage, trous compris) et le rôle de $J_\ell$.

</details>
<details><summary>Indice 2</summary>

1. La sortie $j$ de l'étage $\ell$ lit les sorties $t_u = s_\ell j + d_\ell u$ de l'étage précédent ; applique l'hypothèse de récurrence à $t_0$ et à $t_{k_\ell-1}$. 3. Une somme télescopique : $r_L = r_0 + \sum_\ell (r_\ell - r_{\ell-1})$.

</details>
<details><summary>Indice 3</summary>

1. Les bornes : $J_{\ell-1}t_0 = J_\ell\,j$ et $J_{\ell-1}t_{k_\ell-1} + r_{\ell-1} - 1$. 4. $r_L = 1 + \sum_{\ell=1}^{L}3 \times 2^{\ell-1}$. 5. Les intervalles lus par $t_u$ et $t_{u+1}$ commencent à $J_{\ell-1}d_\ell$ cases l'un de l'autre : quand se touchent-ils ?

</details>

### Ex M21.16 — Le maximum d'une forme linéaire sur une boule L∞ vaut ε‖g‖₁, atteint en ε signe(g)

<details><summary>Indice 1</summary>

Relis le théorème du §8 et son idée : sur la boule L∞, les coordonnées sont indépendantes.

</details>
<details><summary>Indice 2</summary>

1. Majore chaque terme : $g_i\delta_i \le \lvert g_i\rvert\,\lvert\delta_i\rvert$. 2. $g_i\operatorname{signe}(g_i) = \lvert g_i\rvert$. 3. La boule est symétrique par $\boldsymbol{\delta} \mapsto -\boldsymbol{\delta}$.

</details>
<details><summary>Indice 3</summary>

4. L'égalité dans 1 impose $g_i\delta_i = \varepsilon\lvert g_i\rvert$ pour chaque $i$. 5. Cauchy-Schwarz entre $(\lvert g_1\rvert, \ldots, \lvert g_n\rvert)$ et le vecteur de uns ; son cas d'égalité.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M21.17 — Pont : filtrer une grille à trois canaux comme les bibliothèques

<details><summary>Indice 1</summary>

Relis le §6 : « Plusieurs canaux » (la formule à canaux, les formes) et l'encadré « Comptes » ; et, au §2, le « même taille » d'un noyau de longueur paire.

</details>
<details><summary>Indice 2</summary>

$Y_{o,i,j} = b_o + \sum_c\sum_u\sum_v W_{o,c,u,v}\,X_{c,i+u,j+v}$, sans retournement. Pour e), prends dans chaque canal la fenêtre $2 \times 2$ en haut à gauche. Pour g), retourne chaque noyau d'un demi-tour.

</details>
<details><summary>Indice 3</summary>

e) Trois produits case par case, de 4 termes chacun, puis le biais 1. h) $3 \times 4$ positions $\times$ 2 sorties $\times$ 12 poids. j) Calcule la convolution pleine $\mathbf{x} * (4, 1)$ (6 valeurs), puis garde-en 5 à partir de l'indice $\lfloor\frac{2 - 1}{2}\rfloor$.

</details>

### Ex M21.18 — Expliquer avec une règle graduée et un pochoir pourquoi une convolution est équivariante, mais pas invariante

<details><summary>Indice 1</summary>

Relis le §4 : « Décaler puis filtrer, ou filtrer puis décaler », son exemple et « Les bords ».

</details>
<details><summary>Indice 2</summary>

Fais le calcul sur un petit exemple avant d'écrire : une crue de deux jours, le pochoir, la liste des scores, puis la même crue trois jours plus tard.

</details>
<details><summary>Indice 3</summary>

Les mots à faire passer sans formule : « la même recette partout », « la liste se décale d'autant », « invariant voudrait dire : ne bouge pas », « la liste garde la date », « au bout des relevés, des scores manquent ».

</details>

<a id="entretien"></a>

## 💼 Entretien

### M21.E1 — « Pourquoi une convolution est-elle une matrice de Toeplitz, et pourquoi ne la forme-t-on jamais ? »

<details><summary>Indice 1</summary>

Relis le §3 en entier, et son encadré 💻.

</details>
<details><summary>Indice 2</summary>

La colonne $j$ de la matrice est la convolution du $j$-ième vecteur de base : une impulsion. Compte les coefficients non nuls, puis compare le coût d'un produit dense à celui de la convolution directe.

</details>
<details><summary>Indice 3</summary>

Le plan de la réponse : linéarité → colonnes = noyau décalé → diagonales constantes → $nk$ non nuls sur environ $n^2$ → ce qu'on fait à la place → à quoi sert la matrice (rang, noyau, transposée).

</details>

<a id="notebook"></a>

## Notebook

### M21.19 — La convolution de deux suites, dans les trois modes : `convolve`

<details><summary>Indice 1</summary>

Fiche §1 (la définition, le point de vue des polynômes) et §2 (« Trois modes ») ; la docstring de `convolve` dit quelles valeurs garde chaque mode.

</details>
<details><summary>Indice 2</summary>

Avec $n$ = `len(a)` et $m$ = `len(b)` : un tableau de $n + m - 1$ zéros ; pour chaque $j$, ajoute $b_j$ fois tout $\mathbf{a}$ à partir de la case $j$ (une tranche). Puis coupe : « valid » de l'indice $\min(n, m) - 1$ à $\max(n, m) - 1$, « same » $\max(n, m)$ valeurs à partir de $\lfloor\frac{\min(n, m) - 1}{2}\rfloor$. Convertis d'abord les entrées en tableaux de flottants (des copies).

</details>
<details><summary>Indice 3</summary>

```python
full = np.zeros(n + m - 1)
for j in range(m):
    full[j:j + n] += b[j] * a
...      # then the slice of the mode, and a copy
```
Pour a), la loi d'un dé à 8 faces est huit fois $\frac18$ ; convolue-la deux fois avec elle-même ; l'indice $m$ correspond au total $m + 3$. Pour b), pars de $(1)$ et convolue sept fois par $(2, -1)$.

</details>

### M21.20 — La matrice de Toeplitz d'une convolution : `toeplitz_matrix`

<details><summary>Indice 1</summary>

Fiche §3 (« La matrice d'une convolution ») ; la docstring de `toeplitz_matrix` (les lignes de chaque mode, les refus).

</details>
<details><summary>Indice 2</summary>

La matrice pleine de forme $(n + k - 1, n)$ : la colonne $j$ reçoit le noyau dans les lignes $j$ à $j + k - 1$. Puis garde les mêmes lignes que `convolve`. Refuse un `n` booléen ou non entier, et $n < k$ hors du mode plein.

</details>
<details><summary>Indice 3</summary>

La ligne clé : `full[j:j + k, j] = w` pour chaque `j`. Pour c), compare avec `np.array_equal` la transposée de `toeplitz_matrix(w, 7, "valid")` et `toeplitz_matrix(w[::-1], 4)`, puis la même chose en mode "same" (avec $n = 7$ des deux côtés).

</details>

### M21.21 — La convolution circulaire : `circular_convolve`

<details><summary>Indice 1</summary>

Fiche §4 (« Les convolutions circulaires », l'exemple et le lien avec la convolution pleine repliée).

</details>
<details><summary>Indice 2</summary>

Pour chaque $i$, ajoute $a_i$ fois $\mathbf{b}$ décalé circulairement de $i$ cases : les indices `(np.arange(n) - i) % n`. Pour a), le noyau de la moyenne centrée a ses trois valeurs non nulles aux indices 0, 1 et 23.

</details>
<details><summary>Indice 3</summary>

La boucle : `result += a[i] * b[(np.arange(n) - i) % n]`. Pour d), la colonne $j$ de $\operatorname{circ}(\mathbf{h})$ est `circular_convolve(np.eye(n)[j], h)` ; $\check{\mathbf{h}}$ est `h[(-np.arange(n)) % n]`, le renversement `h[::-1]`.

</details>

### M21.22 — Reconnaître un noyau séparable et le factoriser : `separable_factors`

<details><summary>Indice 1</summary>

Fiche §6 (« Reconnaître un noyau séparable ») ; M12d (la décomposition en valeurs singulières) ; la docstring (tolérance relative, convention de signe).

</details>
<details><summary>Indice 2</summary>

`np.linalg.svd(K, full_matrices=False)` rend les valeurs singulières en ordre décroissant ; le noyau est rejeté si $s_2 > \text{tol} \cdot s_1$. Sinon, $\mathbf{v}$ est la première ligne de $\mathbf{V}^\top$, son signe est fixé par sa première coordonnée de valeur absolue $> 10^{-8}$, et $\mathbf{u} = \mathbf{K}\mathbf{v}$.

</details>
<details><summary>Indice 3</summary>

Les lignes clés : `_, s, Vt = np.linalg.svd(M, full_matrices=False)`, `if s.size > 1 and s[1] > tol * s[0]: return None`, puis `first = np.flatnonzero(np.abs(v) > 1e-8)[0]`. Pour c), `np.linalg.norm(K - np.outer(u, v))` (norme de Frobenius pour une matrice).

</details>

### M21.23 — Le noyau équivalent et le pas d'une pile de sommes glissantes : `equivalent_kernel`

<details><summary>Indice 1</summary>

Fiche §7 (« Avec un pas » : l'étage suivant lit le signal avec des trous) ; la docstring (longueur exacte de $\mathbf{K}$, zéros gardés).

</details>
<details><summary>Indice 2</summary>

Pars de $\mathbf{K} = (1)$ et $S = 1$. Pour chaque étage : le noyau $\mathbf{w}_\ell$ écarté de $S - 1$ zéros entre ses coefficients, convolué avec $\mathbf{K}$ (ta `convolve`), puis $S \leftarrow S\,s_\ell$.

</details>
<details><summary>Indice 3</summary>

```python
spread = np.zeros((len(w) - 1) * S + 1)
spread[::S] = w
K = convolve(K, spread)
S *= s
```
Pour d), applique les étages un par un (une somme glissante de pas $s$ : `convolve(x, w[::-1], "valid")[::s]`), puis le noyau équivalent de la même façon avec le pas $S$, et compare les positions communes.

</details>

### M21.24 — Prédire l'effet d'un décalage de l'entrée sur un filtrage avec pas

<details><summary>Indice 1</summary>

Fiche §4 (« Le pas ») et M21.5 d) à g).

</details>
<details><summary>Indice 2</summary>

La sortie de pas 3 garde une valeur sur 3 de la sortie de pas 1. Un décalage de l'entrée de $t$ cases décale la sortie de pas 1 de $t$ cases : lesquelles de ses valeurs tombent alors aux indices multiples de 3 ?

</details>
<details><summary>Indice 3</summary>

La sortie d'origine : la fenêtre 2 lit $x_6$ à $x_9$, la fenêtre 3 lit $x_9$ à $x_{12}$. Pour $t = 1$, refais ces deux fenêtres avec l'événement aux cases 8 à 10.

</details>

### M21.25 — Le coût d'un filtrage direct ou séparable, selon la taille du noyau

<details><summary>Indice 1</summary>

Fiche §6 (« Noyaux séparables », le compte $k_h + k_w$ contre $k_hk_w$).

</details>
<details><summary>Indice 2</summary>

Direct : une boucle sur $(u, v)$, chaque tour ajoute $K_{u,v}$ fois une tranche décalée de la grille. Séparable : une boucle sur $u$ (tranches de lignes, poids $a_u$), puis une boucle sur $v$ (tranches de colonnes, poids $b_v$). Mesure avec `time.perf_counter()` avant et après, garde le meilleur de 3 essais.

</details>
<details><summary>Indice 3</summary>

```python
out = np.zeros((H - k + 1, W - k + 1))
for u in range(k):
    for v in range(k):
        out += K[u, v] * X[u:u + H - k + 1, v:v + W - k + 1]
```
Le rapport des temps se compare à $\frac{k^2}{2k} = \frac k2$.

</details>

### M21.26 — La carte des recouvrements d'une convolution transposée

<details><summary>Indice 1</summary>

Fiche §5 (« Les recouvrements ») et M21.7 e).

</details>
<details><summary>Indice 2</summary>

En 1D : un tableau de $(m - 1)s + k$ zéros, et, pour chaque $i$, ajoute 1 aux cases $si$ à $si + k - 1$. En 2D, la carte est le produit extérieur des comptes des deux axes.

</details>
<details><summary>Indice 3</summary>

`counts[s * i:s * i + k] += 1` pour `i` de 0 à $m - 1$, puis `np.outer(counts, counts)` ; quatre `ax.imshow` dans une grille $2 \times 2$, chacun avec `fig.colorbar` et un titre qui donne $(k, s)$.

</details>

### M21.27 — Chasse à l'erreur : un noyau non retourné, une taille arrondie vers le haut, un noyau de rang 2 « séparé »

<details><summary>Indice 1</summary>

Les ⚠️ de la fiche : §2 (les poids d'une corrélation passés à `np.convolve`, le « même taille » d'un noyau pair), §5 (arrondir vers le haut) et §6 (séparer un noyau de rang 2).

</details>
<details><summary>Indice 2</summary>

(1) Que fait `np.convolve` à ses poids ? Essaie-la avec un noyau antisymétrique. (2) Sur quels cas `math.ceil` et une partie entière vers le bas donnent-ils le même résultat ? (3) Le produit extérieur de la première colonne et de la première ligne redonne-t-il un noyau de rang 2 ?

</details>
<details><summary>Indice 3</summary>

(1) `np.convolve(x, w[::-1], "valid")`. (2) `(n + 2 * p - d * (k - 1) - 1) // s + 1`. (3) Teste d'abord le rang (par exemple avec `separable_factors`), et rends `None` s'il dépasse 1. e) `np.convolve(x, [-3, 2], "same")`.

</details>

### M21.28 — Un test de propriété : la matrice de Toeplitz fois x égale la convolution

<details><summary>Indice 1</summary>

Fiche §3 et M20 (le test de propriété de M20.17) ; la convention des tests : la première ligne d'un message d'échec dit ce qui était attendu.

</details>
<details><summary>Indice 2</summary>

Un générateur `np.random.default_rng(5538)` ; à chaque tirage, $k$, puis $n \ge k$, un noyau et un signal d'entiers ; pour chaque mode, `np.allclose`, et un `assert` dont le message donne l'attendu, puis $k$, $n$ et le mode.

</details>
<details><summary>Indice 3</summary>

Passe la fonction à tester en argument (`toeplitz=toeplitz_matrix`), pour pouvoir la lancer sur la version fausse fournie ; entoure cet appel d'un `try` / `except AssertionError` qui affiche le message du premier échec.

</details>

### M21.29 — Défi : retrouver un noyau inconnu

<details><summary>Indice 1</summary>

Fiche §3 (« La matrice des fenêtres » : la sortie est linéaire en $\mathbf{w}$) ; M09b (les moindres carrés).

</details>
<details><summary>Indice 2</summary>

La convolution est commutative : $\mathbf{w} \star \mathbf{x} = \mathbf{x} * \tilde{\mathbf{w}} = \tilde{\mathbf{w}} * \mathbf{x}$, et la matrice pleine de $\mathbf{x}$ (pris comme noyau), pour des signaux de longueur 7, envoie $\tilde{\mathbf{w}}$ sur la convolution pleine ; garde ses lignes du mode valide.

</details>
<details><summary>Indice 3</summary>

`A = toeplitz_matrix(x, 7)[6:2000]`, `w_flip, *_ = np.linalg.lstsq(A, y, rcond=None)`, puis `w_hat = w_flip[::-1]`. Pour b), le résidu `y - A @ w_flip`. Pour c), les $m$ premières lignes de `A` et de `y`.

</details>
