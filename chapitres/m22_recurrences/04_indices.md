# M22 · Récurrences vectorielles, rayon spectral et normes de matrices — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M22.Q1 — La solution d'une récurrence avec entrée : quelles puissances, quels termes ?

<details><summary>Indice 1</summary>

Relis le théorème du §1 et la façon de le lire (réponse libre, réponse forcée).

</details>
<details><summary>Indice 2</summary>

Dans $\mathbf{x}_t$, l'entrée $\mathbf{u}_k$ est multipliée par $\mathbf{A}^{t-1-k}$, et $k$ va de 0 à $t - 1$. Les formes : $\mathbf{B}\mathbf{u}_t$ doit avoir la forme d'un état.

</details>
<details><summary>Indice 3</summary>

1. $t = 5$, $k = 2$. 3. Quel état $\mathbf{u}_5$ sert-il à calculer ? 6. $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$ avec $t = 3$ : $\sum_{k=0}^{3}h_{3-k}u_k$.

</details>

### M22.Q2 — Valeurs propres complexes, module, forme exponentielle et rotation : vrai ou faux

<details><summary>Indice 1</summary>

Relis « La forme exponentielle d'un nombre complexe » et « Une matrice réelle 2 × 2 à valeurs propres complexes » (§2).

</details>
<details><summary>Indice 2</summary>

Un produit multiplie les modules et additionne les arguments. Pour une matrice réelle $2 \times 2$ de discriminant négatif, le module des valeurs propres est $\sqrt{\det\mathbf{A}}$, et la partie réelle vaut $\frac{\operatorname{tr}\mathbf{A}}{2}$.

</details>
<details><summary>Indice 3</summary>

2. $-3 + 3i$ est dans le deuxième quadrant. 3. Le carré double l'argument : $\frac{3\pi}{2}$. 6. Compare $\sqrt{1{,}96}$ à 1.

</details>

### M22.Q3 — Le rayon spectral décide-t-il de tout ? Le long terme et les premiers pas

<details><summary>Indice 1</summary>

Relis le théorème du §3, « Les cas limites » et « La croissance transitoire ».

</details>
<details><summary>Indice 2</summary>

Une matrice triangulaire a ses valeurs propres sur sa diagonale. $\rho < 1$ dit la limite, pas chaque pas ; $\rho(\mathbf{A})^t \le \lVert\mathbf{A}^t\rVert$ (§4).

</details>
<details><summary>Indice 3</summary>

2. Applique la matrice de la question 1 à $(0, 1)$. 5. Pense à une rotation et à un cisaillement. 6. C'est l'encadré « matrice normale » du §3 : en quelle norme ?

</details>

### M22.Q4 — Normes induites : laquelle se calcule à la main, laquelle borne quoi ?

<details><summary>Indice 1</summary>

Relis « Trois normes induites qui se calculent » et l'encadré des propriétés (§4).

</details>
<details><summary>Indice 2</summary>

$\lVert\cdot\rVert_1$ : les colonnes ; $\lVert\cdot\rVert_\infty$ : les lignes ; $\lVert\cdot\rVert_2$ : une valeur propre de $\mathbf{A}^\top\mathbf{A}$. Toute norme induite donne $\lVert\mathbf{I}\rVert = 1$.

</details>
<details><summary>Indice 3</summary>

3. Cherche une matrice dont une colonne est lourde et les lignes légères. 7. Les colonnes de $\mathbf{M}^\top$ sont les lignes de $\mathbf{M}$.

</details>

### M22.Q5 — Un produit de facteurs dans [0, 1] : ce qui reste après n étapes

<details><summary>Indice 1</summary>

Relis « Des facteurs dans [0, 1] : ce qui reste » et « Des facteurs au hasard » (§5).

</details>
<details><summary>Indice 2</summary>

Ce qui reste : $(1 - \varepsilon)^n$ ; l'approximation $e^{-n\varepsilon}$ ; la demi-vie $\frac{\ln 2}{-\ln(1 - \varepsilon)}$. Pour des facteurs au hasard, c'est le signe de $\mathbb{E}[\ln a]$ qui décide.

</details>
<details><summary>Indice 3</summary>

2. Compare $1 - \varepsilon$ et $e^{-\varepsilon}$, pour $\varepsilon \ne 0$. 4. Chaque facteur mensuel est compris entre 0,94 et 0,965. 5. $\frac12(\ln 2{,}2 + \ln 0{,}4) = \frac12\ln 0{,}88$. 6. Le produit de matrices diagonales est diagonal.

</details>

### M22.Q6 — Contraction et point fixe : lire une jacobienne

<details><summary>Indice 1</summary>

Relis « Applications contractantes et points fixes » et « Lire une jacobienne » (§6).

</details>
<details><summary>Indice 2</summary>

Attractif : $\rho(\mathbf{J}_f(\mathbf{x}^\star)) < 1$. Instable : $\rho > 1$. Répulsif : **toutes** les valeurs propres de module $> 1$. Une contraction de facteur $q$ multiplie les écarts par au plus $q$ à chaque pas.

</details>
<details><summary>Indice 3</summary>

1. Applique la jacobienne à $(0, 1)$. 2. Une valeur propre de module $< 1$ donne une direction qui converge. 5. Trois pas, de $\mathbf{x}_1$ à $\mathbf{x}_4$, le dernier à gauche.

</details>

### M22.Q7 — Une somme sur le temps, sur un modèle de pêche chiffré : vrai ou faux

<details><summary>Indice 1</summary>

Relis « La somme sur le temps » (§7) et l'exemple de la pêcherie.

</details>
<details><summary>Indice 2</summary>

$s_T = \sum_{k=0}^{T-1}J_{T-1}\cdots J_{k+1}\,b_k$ : le terme $k$ est porté par les jacobiennes des pas **suivants** $k$.

</details>
<details><summary>Indice 3</summary>

3. Dérive $1{,}4\,(1 - \beta)\,x + 20$ par rapport à $x$. 5. Au premier ordre, $\Delta x_3 \approx s_3\,\Delta\beta$, avec $\Delta\beta = 0{,}02$. 6. C'est la récurrence $s_{t+1} = J_ts_t + b_t$.

</details>

### M22.Q8 — Ramener un vecteur sous un seuil : le tout ou chaque bloc ?

<details><summary>Indice 1</summary>

Relis le §8 et sa propriété.

</details>
<details><summary>Indice 2</summary>

La norme globale : $\sqrt{\sum_k\lVert\mathbf{w}_k\rVert^2}$. Le tout : un seul facteur $\min(1, \frac{c}{\lVert\mathbf{w}\rVert})$. Chaque bloc : son propre facteur $\min(1, \frac{c}{\lVert\mathbf{w}_k\rVert})$.

</details>
<details><summary>Indice 3</summary>

3. Le bloc de norme 4 est déjà sous le seuil. 5. $p$ blocs de norme au plus $c'$ donnent une norme globale au plus $c'\sqrt p$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M22.R1 — La diagonalisation et les puissances d'une matrice (M12c)

<details><summary>Indice 1</summary>

M12c §4, et le premier paragraphe du §2 de la fiche.

</details>
<details><summary>Indice 2</summary>

Les valeurs propres d'une matrice $2 \times 2$ par la trace et le déterminant ; puis $\mathbf{A}^t = \mathbf{V}\mathbf{D}^t\mathbf{V}^{-1}$.

</details>
<details><summary>Indice 3</summary>

$\lambda^2 - 9\lambda + 18 = 0$. Pour 6, la première ligne de $\mathbf{A} - 6\mathbf{I}$ est $(-1, 2)$.

</details>

### M22.R2 — Valeurs singulières et norme spectrale (M12d)

<details><summary>Indice 1</summary>

M12d : les valeurs singulières sont les racines des valeurs propres de $\mathbf{A}^\top\mathbf{A}$.

</details>
<details><summary>Indice 2</summary>

$\mathbf{A}^\top\mathbf{A}$ est symétrique $2 \times 2$ : trace et déterminant. Le vecteur qui maximise $\lVert\mathbf{A}\mathbf{x}\rVert_2$ est un vecteur propre de $\mathbf{A}^\top\mathbf{A}$.

</details>
<details><summary>Indice 3</summary>

$\lambda^2 - 20\lambda + 36 = 0$. 5. $\lVert\mathbf{A}\rVert_F^2$ est la somme des carrés des coefficients, et aussi celle des carrés des valeurs singulières.

</details>

### M22.R3 — La règle de la chaîne comme produit de jacobiennes (M17)

<details><summary>Indice 1</summary>

M17 §3 : la jacobienne d'une composée.

</details>
<details><summary>Indice 2</summary>

$\mathbf{J}_{f \circ g}(\mathbf{p}) = \mathbf{J}_f\big(g(\mathbf{p})\big)\,\mathbf{J}_g(\mathbf{p})$ : la fonction appliquée en dernier à gauche, évaluée au point où elle est appliquée.

</details>
<details><summary>Indice 3</summary>

$\mathbf{J}_g = \begin{pmatrix} y & x \\ 1 & 1 \end{pmatrix}$ et $\mathbf{J}_f = \begin{pmatrix} 2u & 0 \\ 1 & -1 \end{pmatrix}$, en $(u, v) = g(-1, 4)$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M22.1 — Une population à trois classes d'âge, avec des arrivées : trois pas à la main, et la solution écrite avec les puissances

<details><summary>Indice 1</summary>

Relis le §1 : la définition, le théorème et la lecture « réponse libre, réponse forcée ».

</details>
<details><summary>Indice 2</summary>

Un pas : $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t$, où $\mathbf{B}\mathbf{u}_t = (j_t, 0, a_t)$. Puis $\mathbf{x}_3 = \mathbf{A}^3\mathbf{x}_0 + \mathbf{A}^2\mathbf{B}\mathbf{u}_0 + \mathbf{A}\mathbf{B}\mathbf{u}_1 + \mathbf{B}\mathbf{u}_2$.

</details>
<details><summary>Indice 3</summary>

a) $\mathbf{A}\mathbf{x}_0 = (1{,}2 \times 20 + 0{,}8 \times 30 ;\ 0{,}4 \times 40 ;\ 0{,}6 \times 20)$. d) $\mathbf{A}^2\mathbf{B}$ est formée de la première et de la troisième colonne de $\mathbf{A}^2$. e) Calcule $\mathbf{A}^2$, puis $\mathbf{A}^3 = \mathbf{A}\mathbf{A}^2$, ou applique $\mathbf{A}$ trois fois à $\mathbf{x}_0$. h) Dans $\mathbf{x}_3 = $ e) $+$ f), quelle partie double avec $\mathbf{x}_0$ ?

</details>

### Ex M22.2 — La réponse impulsionnelle de deux réservoirs en cascade, et la sortie comme convolution de l'entrée

<details><summary>Indice 1</summary>

Relis « La réponse impulsionnelle, et la sortie comme convolution » (§1) et l'exemple du §2 (puissances d'une matrice triangulaire).

</details>
<details><summary>Indice 2</summary>

$h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$ : calcule $\mathbf{A}^k\mathbf{B}$ de proche en proche, en multipliant par $\mathbf{A}$, puis prends 0,6 fois la seconde coordonnée. La sortie : $y_{t+1} = \sum_{k \le t}h_{t-k}u_k$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{A}\mathbf{B} = (0{,}4 ;\ 0{,}4)$. e) Les valeurs propres sont 0,4 et 0,3 ; $\mathbf{A}^k\mathbf{B} = \big(0{,}4^k ;\ c\,(0{,}4^k - 0{,}3^k)\big)$ : trouve $c$, puis somme deux séries géométriques. f) Seule la réponse libre $\mathbf{C}\mathbf{A}^4\mathbf{x}_0$ change.

</details>

### Ex M22.3 — Une matrice de rotation et d'homothétie : valeurs propres complexes, forme exponentielle, puissances

<details><summary>Indice 1</summary>

Relis « Multiplier par un complexe : une rotation et une homothétie » (§2).

</details>
<details><summary>Indice 2</summary>

$\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ est la multiplication par $a + ib$, de valeurs propres $a \pm ib$. Écris $a + ib = r\,e^{i\theta}$, puis $\mathbf{M}^t = r^t\,\mathbf{R}_{t\theta}$.

</details>
<details><summary>Indice 3</summary>

$r = \sqrt{0{,}09 + 0{,}27}$ ; $\cos\theta = \frac{-0{,}3}{r}$, $\sin\theta = \frac{0{,}3\sqrt3}{r}$. d) $3\theta = 2\pi$. g) $5\theta = \frac{10\pi}{3}$, à ramener dans $[0, 2\pi[$.

</details>

### Ex M22.4 — Le rayon spectral de trois matrices 2 × 2 non symétriques, et le comportement de leurs puissances

<details><summary>Indice 1</summary>

Relis le §3 (définition, théorème, cas limites) et la méthode de la trace et du déterminant (§2).

</details>
<details><summary>Indice 2</summary>

Pour chaque matrice, $\lambda^2 - (\operatorname{tr})\lambda + \det = 0$ ; si le discriminant est négatif, le module vaut $\sqrt{\det}$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{B}$ : $\lambda^2 - \lambda + 1 = 0$. Calcule $\mathbf{B}^2$, puis $\mathbf{B}^3$. $\mathbf{C}^2$ est un multiple de $\mathbf{I}$.

</details>

### Ex M22.5 — Une matrice triangulaire de rayon spectral < 1 dont les puissances grandissent d'abord : Aᵗ en formule

<details><summary>Indice 1</summary>

Relis « Les cas limites » (le bloc de Jordan) et « La croissance transitoire » (§3).

</details>
<details><summary>Indice 2</summary>

Pour la récurrence, calcule $\mathbf{T}^{t+1} = \mathbf{T}^t\mathbf{T}$ : le coefficient en haut à droite vaut $\lambda_1^t\gamma + \gamma\sigma_t\lambda_2$. Pour $\mathbf{A}$, $c_t = 3t\left(\frac23\right)^{t-1}$.

</details>
<details><summary>Indice 3</summary>

c) $\frac{c_{t+1}}{c_t} = \frac{t+1}{t}\cdot\frac23$ : compare-le à 1 pour $t = 1, 2, 3$. e) Calcule $c_9$ et $c_{10}$. f) $\mathbf{A}^6\mathbf{e}_2$ est la seconde colonne de $\mathbf{A}^6$. g) Les valeurs propres de $\mathbf{B}$ sont distinctes : $\sigma_t = \frac{(2/3)^t - (1/3)^t}{1/3}$.

</details>

### Ex M22.6 — Les normes ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice 2 × 2, et trois majorations de ‖A⁵x‖

<details><summary>Indice 1</summary>

Relis « Trois normes induites qui se calculent » et « Deux usages » (§4).

</details>
<details><summary>Indice 2</summary>

Colonnes pour $\lVert\cdot\rVert_1$, lignes pour $\lVert\cdot\rVert_\infty$, la plus grande valeur propre de $\mathbf{A}^\top\mathbf{A}$ pour $\lVert\cdot\rVert_2$. $\lVert\mathbf{A}^5\mathbf{x}\rVert_p \le \lVert\mathbf{A}\rVert_p^5\,\lVert\mathbf{x}\rVert_p$, la même norme des deux côtés.

</details>
<details><summary>Indice 3</summary>

c) Les colonnes de $\mathbf{A}$ sont orthogonales. e) Trace 3, déterminant 4. f) $\mathbf{A}\mathbf{x} = (-4, -8)$, puis continue. g) $\lVert\mathbf{x}\rVert_1 = 5$, $\lVert\mathbf{x}\rVert_2 = \sqrt{13}$, $\lVert\mathbf{x}\rVert_\infty = 3$.

</details>

### Ex M22.7 — Trois équipements qui s'usent à des rythmes différents : une récurrence diagonale, ce qui reste, et la demi-vie

<details><summary>Indice 1</summary>

Relis « Des matrices diagonales » et « Des facteurs dans [0, 1] : ce qui reste » (§5).

</details>
<details><summary>Indice 2</summary>

Chaque capacité évolue seule : $a_i^n$ ce qui reste, $e^{-n\varepsilon_i}$ son approximation, $\frac{\ln 2}{-\ln a_i}$ la demi-vie. Avec entretien, l'équilibre vérifie $x_i^\star = a_ix_i^\star + b_i$.

</details>
<details><summary>Indice 3</summary>

a) $0{,}985^{12}$, $0{,}93^{12}$, $0{,}65^{12}$. e) $\mathbf{x}_1 = (0{,}997 ;\ 0{,}986 ;\ 0{,}93)$, puis encore un pas. f) $x_i^\star = \frac{b_i}{\varepsilon_i}$.

</details>

### Ex M22.8 — Les jacobiennes d'une application du plan en trois points d'une trajectoire, et leur produit

<details><summary>Indice 1</summary>

Relis « La jacobienne d'un état par rapport à un état antérieur » (§6).

</details>
<details><summary>Indice 2</summary>

$\mathbf{J}_f(x, y) = \begin{pmatrix} -2{,}8\,x & 1 \\ 0{,}3 & 0 \end{pmatrix}$ ; $\frac{\partial\mathbf{x}_3}{\partial\mathbf{x}_0} = \mathbf{J}_f(\mathbf{x}_2)\,\mathbf{J}_f(\mathbf{x}_1)\,\mathbf{J}_f(\mathbf{x}_0)$, chaque jacobienne au point où $f$ est appliquée.

</details>
<details><summary>Indice 3</summary>

$\mathbf{x}_1 = (1, 0)$, $\mathbf{x}_2 = (-0{,}4 ;\ 0{,}3)$. Calcule d'abord $\mathbf{J}_f(\mathbf{x}_1)\mathbf{J}_f(\mathbf{x}_0)$. e) $\det\mathbf{J}_f = -0{,}3$ partout. g) d) fois $(0{,}01 ;\ 0)$.

</details>

### Ex M22.9 — Un capital placé à taux fixe avec des versements : la dérivée du capital final par rapport au taux, une somme sur les années

<details><summary>Indice 1</summary>

Relis « Une récurrence pour la dérivée » et « La somme sur le temps » (§7).

</details>
<details><summary>Indice 2</summary>

$J_t = \frac{\partial f}{\partial x} = 1 + \beta$ et $b_t = \frac{\partial f}{\partial\beta} = x_t$ ; $s_4 = \sum_{k=0}^{3}J^{3-k}\,b_k$.

</details>
<details><summary>Indice 3</summary>

d) Le terme de l'année 0 est $1{,}035^3 \times 2\,500$. f) $\Delta\beta = 0{,}002$. g) Recalcule $x_4$ avec $\beta = 0{,}037$.

</details>

### Ex M22.10 — La norme globale de trois blocs, et deux façons de les ramener sous un seuil

<details><summary>Indice 1</summary>

Relis le §8 : la norme globale, puis les deux façons de ramener sous un seuil.

</details>
<details><summary>Indice 2</summary>

Le tout : un seul facteur $\min(1, \frac{c}{\lVert\mathbf{w}\rVert})$ pour tous les blocs. Chaque bloc : $\min(1, \frac{c}{\lVert\mathbf{w}_k\rVert})$, un facteur par bloc.

</details>
<details><summary>Indice 3</summary>

b) $\sqrt{16 + 49 + 16}$. e) Seul $\mathbf{w}_2$ dépasse 5. g) $\mathbf{w} \cdot \mathbf{w}' = 16 + \frac57 \times 49 + 16$, puis divise par les deux normes.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M22.11 — Sous-multiplicativité, ‖Aᵀ‖₂ = ‖A‖₂, ‖diag(d)‖₂ = max |dᵢ| et ρ(A) ≤ ‖A‖

<details><summary>Indice 1</summary>

Relis la définition d'une norme induite et l'encadré des propriétés (§4) : tout repose sur $\lVert\mathbf{M}\mathbf{y}\rVert \le \lVert\mathbf{M}\rVert\,\lVert\mathbf{y}\rVert$.

</details>
<details><summary>Indice 2</summary>

1. $\lVert\mathbf{A}(\mathbf{B}\mathbf{x})\rVert$. 2. Multiplie $\mathbf{A}^\top\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ à gauche par $\mathbf{A}$. 3. Une majoration, puis un vecteur de base. 4. $\mathbf{A}\mathbf{z} = \mathbf{A}\mathbf{u} + i\,\mathbf{A}\mathbf{v}$, avec $\mathbf{A}\mathbf{u}$ et $\mathbf{A}\mathbf{v}$ réels.

</details>
<details><summary>Indice 3</summary>

2. Pourquoi $\mathbf{A}\mathbf{v} \ne \mathbf{0}$ : sinon $\lambda\mathbf{v} = \mathbf{0}$. Contre-exemple : $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$. 5. Applique 4 à un vecteur propre $\mathbf{v} \in \mathbb{C}^n$ de $\lambda$, avec $\lvert\lambda\rvert = \rho(\mathbf{A})$. 6. Une matrice nilpotente, puis une matrice diagonale.

</details>

### Ex M22.12 — La norme induite ‖·‖∞ est le maximum des sommes de lignes

<details><summary>Indice 1</summary>

Imite la preuve de la fiche pour $\lVert\cdot\rVert_1$, ligne par ligne au lieu de colonne par colonne.

</details>
<details><summary>Indice 2</summary>

1. $\lvert\sum_j a_{ij}x_j\rvert \le \sum_j\lvert a_{ij}\rvert\,\lvert x_j\rvert$, et $\lvert x_j\rvert \le \lVert\mathbf{x}\rVert_\infty$. 2. $a\operatorname{signe}(a) = \lvert a\rvert$.

</details>
<details><summary>Indice 3</summary>

4. $(\mathbf{A}\mathbf{x})_0 = 2x_0 - 5x_2$, avec $\lvert x_j\rvert \le 1$ : quand vaut-il 7 ? 5. Calcule $\mathbf{S}(1, 1, 1)$ ; une ligne de coefficients positifs a pour somme de valeurs absolues sa somme tout court.

</details>

### Ex M22.13 — Aᵗ → 0 si et seulement si ρ(A) < 1, pour une matrice diagonalisable sur ℂ

<details><summary>Indice 1</summary>

Relis l'idée de la preuve après le théorème du §3.

</details>
<details><summary>Indice 2</summary>

2. $(\mathbf{V}\mathbf{D}^t\mathbf{V}^{-1})_{jk} = \sum_iV_{ji}\lambda_i^t(\mathbf{V}^{-1})_{ik}$, puis l'inégalité triangulaire. 3. $\mathbf{A}^t\mathbf{v} = \lambda^t\mathbf{v}$, et regarde une coordonnée non nulle de $\mathbf{v}$.

</details>
<details><summary>Indice 3</summary>

4. Vecteurs propres $(1, 1)$ et $(2, -3)$ ; $\mathbf{A}^t = 0{,}6^t\,\mathbf{v}_1\mathbf{r}_1 + (-0{,}4)^t\,\mathbf{v}_2\mathbf{r}_2$, avec $\mathbf{r}_1, \mathbf{r}_2$ les lignes de $\mathbf{V}^{-1}$. 6. $\mathbf{A}^t = \lambda^t\mathbf{I} + t\lambda^{t-1}\mathbf{U}$ : le facteur $t$.

</details>

### Ex M22.14 — Une application contractante oublie son point de départ : l'écart entre deux trajectoires décroît géométriquement

<details><summary>Indice 1</summary>

Relis la définition et la propriété des applications contractantes (§6).

</details>
<details><summary>Indice 2</summary>

1. Une récurrence sur $t$, qui porte aussi sur « $\mathbf{x}_t, \tilde{\mathbf{x}}_t \in \mathcal{D}$ ». 2. Applique la définition à deux points fixes. 4. $f(\mathbf{x}) - f(\tilde{\mathbf{x}}) = \mathbf{A}(\mathbf{x} - \tilde{\mathbf{x}})$.

</details>
<details><summary>Indice 3</summary>

4. $\lVert\mathbf{A}\rVert_1$ : les sommes des colonnes. Le point fixe : $(\mathbf{I} - \mathbf{A})\mathbf{x}^\star = \mathbf{c}$. L'écart initial en norme 1 : $\lvert 5 - (-1)\rvert + \lvert -3 - 4\rvert$. 5. Applique $\mathbf{J}$, $\mathbf{J}^2$ et $\mathbf{J}^3$ à $\mathbf{e}_2$.

</details>

### Ex M22.15 — La sensibilité de l'état final à un paramètre utilisé à chaque pas suit une récurrence avec entrée : sa solution est une somme sur le temps

<details><summary>Indice 1</summary>

Relis « Une récurrence pour la dérivée » (§7), puis le théorème du §1 et sa preuve par récurrence.

</details>
<details><summary>Indice 2</summary>

1. $\beta \mapsto (\mathbf{x}_t(\beta), \beta)$ a pour jacobienne la colonne $(\mathbf{s}_t ; 1)$ ; $f$ a pour jacobienne $\begin{pmatrix} \mathbf{J}_t & \mathbf{b}_t \end{pmatrix}$. 2. Comme la preuve du §1, avec des matrices qui changent.

</details>
<details><summary>Indice 3</summary>

4. Pars de $\mathbf{s}_0 \ne \mathbf{0}$ et suis la récurrence : quel terme contient $\mathbf{s}_0$ ? 6. $J_t = 0{,}84$, $b_t = -1{,}4\,x_t$, avec $x_0 = 40$, $x_1 = 53{,}6$, $x_2 = 65{,}024$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M22.16 — Pont : la convention ligne x_{t+1} = x_t A + u_t B, ses formes, et la jacobienne Aᵀ

<details><summary>Indice 1</summary>

Relis le 📐 du §1, et la convention des jacobiennes de M17 (une ligne par coordonnée de sortie).

</details>
<details><summary>Indice 2</summary>

a) $\mathbf{u}_t$ a la forme $(1, m)$, $\mathbf{u}_t\mathbf{B}$ celle d'un état $(1, n)$. d) Transpose : $(\mathbf{x}\mathbf{A})^\top = \mathbf{A}^\top\mathbf{x}^\top$. e) $(\mathbf{x}\mathbf{A})_j = \sum_ix_ia_{ij}$.

</details>
<details><summary>Indice 3</summary>

c) $\mathbf{x}_1 = (4 \times 0{,}2 + 0{,}4 ;\ 4 \times 0{,}6 - 0{,}3) + (1, -2)$. f) La jacobienne de $\mathbf{x} \mapsto \mathbf{x}\mathbf{A}^3$ est $(\mathbf{A}^3)^\top = (\mathbf{A}^\top)^3$.

</details>

### Ex M22.17 — MML §4.2

<details><summary>Indice 1</summary>

Le guide de lecture de MML de la fiche : lis le passage *Graphical Intuition in Two Dimensions* en entier, figure 4.4 sous les yeux.

</details>
<details><summary>Indice 2</summary>

1. Pour chaque matrice, la somme des valeurs propres est la trace, leur produit le déterminant. 3. $\mathbf{A}_4^2 = 2\mathbf{A}_4$ ; $\mathbf{A}_5$ a pour vecteurs propres $(1, 1)$ et $(1, -1)$. 4. Une matrice est normale si $\mathbf{A}^\top\mathbf{A} = \mathbf{A}\mathbf{A}^\top$.

</details>
<details><summary>Indice 3</summary>

2. La définition 4.6 cherche $\lambda$ dans $\mathbb{R}$. 3. $\mathbf{A}_2^t = \begin{pmatrix} 1 & t/2 \\ 0 & 1 \end{pmatrix}$. 6. Cherche les deux mots qui accompagnent *multiplicity* autour de l'exemple 4.6. 7. Les valeurs propres de $\begin{pmatrix} a & c \\ c & a \end{pmatrix}$ sont $a \pm c$.

</details>

### Ex M22.18 — Expliquer avec une image non mathématique pourquoi un système linéaire oublie son passé au rythme de ρ(A)

<details><summary>Indice 1</summary>

Le §2 (chaque coordonnée dans la base des vecteurs propres est multipliée par sa valeur propre) et le §3 (le rayon spectral, puis la croissance transitoire).

</details>
<details><summary>Indice 2</summary>

Trouve une image où quelque chose s'efface « par fractions » d'un jour à l'autre, avec plusieurs vitesses : une maison qu'on aère pièce par pièce, un écho dans une salle.

</details>
<details><summary>Indice 3</summary>

Plan : la même règle chaque jour ; l'excès se décompose en plusieurs façons de s'effacer ; les rapides disparaissent, la plus lente reste ; son facteur est le rayon spectral ; mais au début, un niveau peut monter avant de descendre.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M22.E1 — « Quelle différence entre le rayon spectral et la norme d'une matrice ? »

<details><summary>Indice 1</summary>

Le §3 (rayon spectral, croissance transitoire), le §4 (normes induites, $\rho \le \lVert\mathbf{A}\rVert$, Gelfand) et la récapitulation des pièges.

</details>
<details><summary>Indice 2</summary>

Un mot clé pour chacun : « le long terme » pour le rayon spectral, « chaque pas » pour la norme.

</details>
<details><summary>Indice 3</summary>

L'exemple où ils diffèrent le plus : une matrice nilpotente non nulle. Le cas d'égalité : en norme 2, pour une matrice normale.

</details>

### M22.E2 — « Pourquoi Aⁿ peut-il grandir longtemps alors que toutes les valeurs propres de A sont de module < 1 ? »

<details><summary>Indice 1</summary>

« La croissance transitoire » (§3) et ✏️ M22.5.

</details>
<details><summary>Indice 2</summary>

Deux mécanismes : des vecteurs propres presque parallèles (des composantes qui se compensent), ou une valeur propre double (le facteur $n$ de $n\lambda^{n-1}$).

</details>
<details><summary>Indice 3</summary>

Pour quelles matrices est-ce impossible, et dans quelle norme ? Pense aux matrices normales.

</details>

<a id="notebook"></a>

## Notebook

### M22.19 — Les états d'une récurrence linéaire avec entrée : `linear_system_states`

<details><summary>Indice 1</summary>

Fiche §1 et le 💻 qui suit : un pas à la fois, une multiplication par $\mathbf{A}$ par pas. La docstring dit les formes à contrôler et ce qui est refusé (un `inputs` à une dimension, une matrice non carrée…).

</details>
<details><summary>Indice 2</summary>

Convertis avec `np.asarray(…, dtype=float)`, contrôle `A.ndim == 2` et `A.shape[0] == A.shape[1]`, puis `B.shape == (n, m)`, `x0.shape == (n,)`, `inputs.ndim == 2` et `inputs.shape[1] == m`. Crée `states = np.empty((T + 1, n))`, `states[0] = x0`, puis, pour chaque ligne `u` de `inputs`, `x = A @ x + B @ u`.

</details>
<details><summary>Indice 3</summary>

Ne fais jamais `x[:] = …` sur `x0` : `x = A @ x + B @ u` crée un nouveau tableau. Pour $T = 0$, `inputs` a la forme `(0, m)` et la boucle ne tourne pas. Ensuite, b) `linear_system_states(A, B, x0, np.tile([20.0, 10.0], (60, 1)))[-1].sum()` ; e) une impulsion `np.array([[1.0]] + [[0.0]] * 6)` (7 entrées), et `y = states @ C`.

</details>

### M22.20 — Les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂ : `operator_norm`

<details><summary>Indice 1</summary>

Fiche §4 : les trois formules. La docstring dit les refus : un tableau qui n'est pas à deux axes, une matrice vide, un `ord` qui n'est ni 1, ni 2, ni `np.inf` (un booléen, `"fro"`).

</details>
<details><summary>Indice 2</summary>

`np.abs(A).sum(axis=0).max()` (colonnes) pour `ord=1`, `axis=1` (lignes) pour `np.inf`. Pour 2 : `np.linalg.eigvalsh(A.T @ A)` rend les valeurs propres en ordre croissant ; prends la dernière.

</details>
<details><summary>Indice 3</summary>

Teste `ord` avant tout calcul, et refuse `True` (`isinstance(ord, bool)`), car `True == 1`. L'arrondi peut rendre la plus grande valeur propre très légèrement négative pour une matrice nulle : `max(…, 0.0)` avant la racine. Rends `float(…)`. Ensuite, b) `operator_norm(np.linalg.matrix_power(A, t), 2) ** (1 / t)`.

</details>

### M22.21 — Les normes des produits cumulés, et leur majoration : `product_norms`

<details><summary>Indice 1</summary>

Fiche §5 : $\mathbf{P}_t = \mathbf{A}_t\cdots\mathbf{A}_1$, la majoration $\lVert\mathbf{A}_t\rVert\cdots\lVert\mathbf{A}_1\rVert$, et la docstring.

</details>
<details><summary>Indice 2</summary>

`P = np.eye(n)`, `bound = 1.0` ; pour chaque matrice `M`, dans l'ordre : `P = M @ P` (la nouvelle à gauche), `bound *= np.linalg.norm(M, ord)`, puis range `np.linalg.norm(P, ord)` et `bound`.

</details>
<details><summary>Indice 3</summary>

Contrôle qu'il y a au moins une matrice, toutes carrées et de même forme, et le même `ord` que `operator_norm`. Ensuite, a) une liste `[jac(x) for x in xs[:30]]` avec `jac(x) = np.array([[-2.8 * x[0], 1.0], [0.3, 0.0]])`, et `norms[2]` ; b) `bounds[29] / norms[29]`.

</details>

### M22.22 — `np.linalg.eigvals` et `np.linalg.norm` : rayon spectral et normes de matrices tirées au hasard

<details><summary>Indice 1</summary>

Fiche §4, le 💻 : les arguments `ord` de `np.linalg.norm`, et ce qu'elle rend sans `ord`.

</details>
<details><summary>Indice 2</summary>

Une boucle sur `A[k]`, et des listes `rho`, `n1`, `n2`, `ninf`, `fro` ; puis `np.mean(rho <= np.minimum(np.minimum(n1, n2), ninf))`, `np.mean(rho / n2)`, `np.mean(n1 < n2)`.

</details>
<details><summary>Indice 3</summary>

d) `S = (A[k] + A[k].T) / 2`, puis `abs(rho(S) - np.linalg.norm(S, 2)) < 1e-12` pour tous. f) `np.linalg.norm(np.linalg.matrix_power(A[0], t), 2) ** (1 / t)`.

</details>

### M22.23 — Prédire l'allure de ‖Aᵗ‖₂ pour une matrice non normale de rayon spectral 0,8

<details><summary>Indice 1</summary>

Fiche §3 (« La croissance transitoire ») et ✏️ M22.5 : une valeur propre double et une partie nilpotente.

</details>
<details><summary>Indice 2</summary>

Trace et déterminant de $\mathbf{A}$ donnent ses valeurs propres. Une matrice de valeur propre double $\lambda$ qui n'est pas $\lambda\mathbf{I}$ se comporte comme $\lambda^t\mathbf{I} + t\lambda^{t-1}\mathbf{U}$.

</details>
<details><summary>Indice 3</summary>

Le maximum de $t \times 0{,}8^{t-1}$ est vers $t = -\frac{1}{\ln 0{,}8} \approx 4{,}5$. Pour le tracé : `plt.semilogy(range(41), norms)` et `plt.semilogy(range(41), 0.8 ** np.arange(41))`.

</details>

### M22.24 — Des produits de matrices aléatoires : le taux de croissance

<details><summary>Indice 1</summary>

Fiche §5 : « Des facteurs au hasard : la moyenne géométrique », le théorème de Furstenberg et Kesten et le 💻 sur la renormalisation.

</details>
<details><summary>Indice 2</summary>

`mats = [G if c == 0 else M for c in years]`. b) `norms, _ = product_norms(mats[:200])`, puis `np.log(norms[-1]) / 200`. c) `x = np.ones(2) / np.sqrt(2)` ; pour chaque matrice : `x = A @ x`, `r = np.linalg.norm(x)`, `total += np.log(r)`, `x = x / r`.

</details>
<details><summary>Indice 3</summary>

a) `np.log(np.abs(np.linalg.eigvals((G + M) / 2)).max())`. e) Une fonction `rate(seed)` qui retire les années avec `np.random.default_rng(seed).integers(0, 2, size=20000)` et renvoie le taux de c). Pour le graphique, range `total / n` à chaque pas $n$.

</details>

### M22.25 — Les spirales d'une récurrence 2 × 2 à valeurs propres complexes, selon leur module

<details><summary>Indice 1</summary>

Fiche §2 : « Une matrice réelle 2 × 2 à valeurs propres complexes », et sa figure des spirales.

</details>
<details><summary>Indice 2</summary>

`linear_system_states(r * A, np.zeros((2, 1)), [1.0, 0.0], np.zeros((60, 1)))` rend les 61 points. `fig, axes = plt.subplots(1, 5, figsize=…)`, et `ax.set_aspect("equal")` dans les quatre premiers.

</details>
<details><summary>Indice 3</summary>

Les points : `ax.plot(X[:, 0], X[:, 1], "o-", ms=3)`. Le cinquième panneau : `np.linalg.norm(X, axis=1)` contre $t$, en `semilogy`, avec `r ** np.arange(61)` en pointillés.

</details>

### M22.26 — Chasse à l'erreur : ρ(A) pris pour ‖A‖, un produit de jacobiennes dans le mauvais ordre, un seuil appliqué bloc par bloc

<details><summary>Indice 1</summary>

La fiche : le ⚠️ du §4 (la plus grande valeur propre n'est pas le plus grand allongement), le ⚠️ du §6 (l'ordre des jacobiennes), le §8 (le tout ou chaque bloc).

</details>
<details><summary>Indice 2</summary>

(1) Pour quelles matrices $\rho = \lVert\cdot\rVert_2$ ? La matrice de la vérification en est une. (2) Pour une application linéaire, toutes les jacobiennes sont égales : l'ordre peut-il se voir ? (3) Avec un seul drone, y a-t-il une différence entre « le tout » et « chaque ligne » ?

</details>
<details><summary>Indice 3</summary>

(1) `np.sqrt(np.linalg.eigvalsh(A.T @ A)[-1])`. (2) `P = jac(x) @ P`. (3) Calcule d'abord l'énergie de toute la flotte, puis un seul facteur $\sqrt{\min(1, E/E_{\text{flotte}})}$ pour tout le tableau ; rends une copie quand l'énergie est nulle. b) Les états : $(4, 2)$, puis $f(4, 2)$, puis $f(f(4, 2))$.

</details>

### M22.27 — Un test de propriété : ‖AB‖ ≤ ‖A‖ ‖B‖ et ρ(A) ≤ ‖A‖

<details><summary>Indice 1</summary>

Fiche §4 (les propriétés), M21.28 (le test de propriété de M21), et la convention des tests : la première ligne d'un message d'échec dit ce qui était attendu.

</details>
<details><summary>Indice 2</summary>

`rng = np.random.default_rng(5727)` ; à chaque tirage, `m, k, n = rng.integers(1, 6, size=3)`, puis `A`, `B`, `S` ; pour chaque `ord`, un `assert norm(A @ B, ord) <= norm(A, ord) * norm(B, ord) * (1 + 1e-12), f"expected …"`.

</details>
<details><summary>Indice 3</summary>

La fonction reçoit la fonction à tester en argument, `property_test_27(norm)` : la cellule suivante l'appelle sur `operator_norm`, puis sur `norm_frobenius` et `norm_swapped`. Pour les propriétés ajoutées : `norm(np.eye(n), ord) == 1` (à $10^{-12}$ près) pour $n \ge 2$, et `np.linalg.norm(A @ x, ord) <= norm(A, ord) * np.linalg.norm(x, ord)` pour `x` dans `np.eye(k)` et pour des vecteurs `rng.choice([-1.0, 1.0], size=k)`. Laisse l'`AssertionError` sortir de ta fonction.

</details>

### M22.28 — Défi : une matrice 3 × 3 de rayon spectral 0,85 dont une puissance dépasse 100

<details><summary>Indice 1</summary>

✏️ M22.5 et 🔮 M22.23 : une valeur propre répétée et des coefficients au-dessus de la diagonale font grandir les puissances. En dimension 3, il y a de la place pour deux étages.

</details>
<details><summary>Indice 2</summary>

Une matrice triangulaire supérieure a ses valeurs propres sur sa diagonale : mets-y 0,85 trois fois, et tu contrôles $\rho$ exactement. Pour $t \ge 3$ : $\lVert\mathbf{A}\rVert_F \le \sqrt{9 \times 3^2}$, et $\lVert\mathbf{A}^2\rVert_2 \le \lVert\mathbf{A}\rVert_2^2$.

</details>
<details><summary>Indice 3</summary>

Avec $\mathbf{A} = 0{,}85\,\mathbf{I} + \mathbf{U}$ et $\mathbf{U}$ triangulaire strictement supérieure, $\mathbf{U}^3 = \mathbf{0}$ et $\mathbf{A}^t = 0{,}85^t\mathbf{I} + t\,0{,}85^{t-1}\mathbf{U} + \binom t2 0{,}85^{t-2}\mathbf{U}^2$ : rends les coefficients de $\mathbf{U}$ aussi grands que possible, avec des signes qui ne se compensent pas dans $\mathbf{U}^2$.

</details>
