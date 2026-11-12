# M16 · Applications affines, graphes et variance d'un produit — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M16.Q1 — Les formes de W, de b et de x W + b, dans chaque convention

<details><summary>Indice 1</summary>

Relis « Deux conventions pour une même application » et « Compter les paramètres » (fiche §1).

</details>
<details><summary>Indice 2</summary>

En lignes, $\mathbf{W}$ a une ligne par entrée et une colonne par sortie ; en colonnes, c'est la transposée.

</details>
<details><summary>Indice 3</summary>

5 : quand $n = m$, $\mathbf{W}$ et $\mathbf{W}^\top$ ont la même forme. 6 : un produit $(N, n) \times (n, m)$ coûte $Nnm$ multiplications.

</details>

### M16.Q2 — Coordonnées homogènes et composition : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §2 de la fiche.

</details>
<details><summary>Indice 2</summary>

$\mathbf{H}$ a la forme $(n + 1, m + 1)$ ; sa dernière colonne est $(0, \ldots, 0, 1)$ ; la première application appliquée est à gauche.

</details>
<details><summary>Indice 3</summary>

5 : faire une translation puis une autre, c'est ajouter les deux vecteurs, dans n'importe quel ordre. 6 : que vaut $\det\mathbf{H}$ ? Pense à une projection.

</details>

### M16.Q3 — Lire une matrice d'adjacence : degrés, arêtes, chemins, cycles

<details><summary>Indice 1</summary>

Relis « Nœuds, arêtes, degrés » et « Les puissances de A comptent les chemins » (§3), puis le §4.

</details>
<details><summary>Indice 2</summary>

Une ligne : les successeurs ; une colonne : les prédécesseurs. $(\mathbf{A}^2)_{ij} = \sum_l A_{il}A_{lj}$.

</details>
<details><summary>Indice 3</summary>

4 : regarde où sont les 1 par rapport à la diagonale. 5 : $\mathbf{A}^2$ ne compte que les chemins de **deux** arêtes.

</details>

### M16.Q4 — Indépendantes, décorrélées, ou ni l'un ni l'autre ?

<details><summary>Indice 1</summary>

Relis la formule du §5 et le lemme du §6.

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(XY) = \mathbb{V}(X)\,\mathbb{V}(Y) + \mathbb{V}(X)\,\mathbb{E}[Y]^2 + \mathbb{V}(Y)\,\mathbb{E}[X]^2$ ; la variance d'une somme ne fait intervenir que des covariances.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbb{E}[\varepsilon x] = 0$ et $\varepsilon^2 = 1$. 6 : les hypothèses du lemme portent sur les $\varepsilon_i$, pas sur les $x_i$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M16.R1 — Le produit matriciel, ses formes et son coût (M09a)

<details><summary>Indice 1</summary>

M09a §3 et §4.

</details>
<details><summary>Indice 2</summary>

$(a, b) \times (b, c) \to (a, c)$, pour $abc$ multiplications ; le produit de Hadamard multiplie case par case.

</details>
<details><summary>Indice 3</summary>

La transposée d'un produit inverse l'ordre des facteurs.

</details>

### M16.R2 — La variance d'une somme de variables indépendantes (M02b)

<details><summary>Indice 1</summary>

M02b §4 et §6.

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(aX + bY) = a^2\,\mathbb{V}(X) + b^2\,\mathbb{V}(Y)$ pour des variables indépendantes ; $\mathbb{E}[X^2] = \mathbb{V}(X) + \mathbb{E}[X]^2$.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbb{V}(10X) = 100\,\mathbb{V}(X)$, alors que dix copies indépendantes donnent $10\,\mathbb{V}(X)$. 5 : la loi uniforme sur $[a ; b]$ a la variance $\frac{(b - a)^2}{12}$.

</details>

### M16.R3 — Les valeurs propres d'une matrice triangulaire (M12c)

<details><summary>Indice 1</summary>

M12c §1 et §3.

</details>
<details><summary>Indice 2</summary>

Le déterminant d'une matrice triangulaire est le produit de sa diagonale ; ses valeurs propres sont ses coefficients diagonaux.

</details>
<details><summary>Indice 3</summary>

4 : cherche une matrice $2 \times 2$ triangulaire, de diagonale nulle, qui n'est pas nulle.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M16.1 — Une application affine de ℝ³ dans ℝ² dans les deux conventions

<details><summary>Indice 1</summary>

Relis l'exemple du §1 : chaque sortie lit ses coefficients dans une **colonne** de $\mathbf{W}$.

</details>
<details><summary>Indice 2</summary>

La sortie 1 vaut $1 \cdot x_1 + 0 \cdot x_2 + (-2) \cdot x_3 + 3$ : sa colonne est $(1, 0, -2)$. La matrice en colonnes est la transposée.

</details>
<details><summary>Indice 3</summary>

f) L'image de $(1, 0, 0)$ est la ligne 1 de $\mathbf{W}$, plus $\mathbf{b}$. h) $Nnm$.

</details>

### Ex M16.2 — Rotation, homothétie puis translation du plan

<details><summary>Indice 1</summary>

Relis « Composer, c'est multiplier » (§2) : avec des lignes, la première application est à gauche.

</details>
<details><summary>Indice 2</summary>

Pour $\mathbf{H}_1$, les lignes de $\mathbf{W}_1$ sont les images de $(1, 0)$ et de $(0, 1)$ ; la translation de $f_3$ va sur la dernière ligne de $\mathbf{H}_3$.

</details>
<details><summary>Indice 3</summary>

d) $\mathbf{H}_1\mathbf{H}_2\mathbf{H}_3$. f) Défais les étapes dans l'ordre inverse : retire la translation, divise par 2, puis tourne d'un quart de tour dans l'autre sens, $(x, y) \mapsto (y, -x)$.

</details>

### Ex M16.3 — Des rues à sens unique

<details><summary>Indice 1</summary>

Relis le §3 : la matrice, les degrés, puis le théorème sur $\mathbf{A}^k$.

</details>
<details><summary>Indice 2</summary>

$A_{ij} = 1$ pour une rue $i \to j$ : la ligne 3 a trois 1 (vers 1, 4 et 5). $(\mathbf{A}^2)_{ij} = \sum_l A_{il}A_{lj}$.

</details>
<details><summary>Indice 3</summary>

f) Calcule la ligne 1 de $\mathbf{A}^3$ : c'est la ligne 1 de $\mathbf{A}^2$ fois $\mathbf{A}$. g) La trace de $\mathbf{A}^3$ : un même cycle compte une fois par point de départ.

</details>

### Ex M16.4 — Un planning de tâches

<details><summary>Indice 1</summary>

Relis le §4 : la numérotation triangulaire, puis la somme sur les chemins.

</details>
<details><summary>Indice 2</summary>

e) Cherche un chemin qui passe par les six tâches : chacune de ses arêtes doit aller vers un numéro plus grand. d) Toutes les routes de Commande à Expédition passent par Montage.

</details>
<details><summary>Indice 3</summary>

d) Compte les chemins de Commande à Montage (3), puis ceux de Montage à Expédition (2), et multiplie. g) Additionne, ligne par ligne, les chemins qui partent de chaque tâche.

</details>

### Ex M16.5 — Un prix aléatoire fois une quantité indépendante

<details><summary>Indice 1</summary>

Relis la formule du §5 et l'exemple du chiffre d'affaires.

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[P^2] = \mathbb{V}(P) + \mathbb{E}[P]^2$, puis $\mathbb{V}(R) = \mathbb{E}[P^2]\,\mathbb{E}[Q^2] - \mathbb{E}[R]^2$.

</details>
<details><summary>Indice 3</summary>

d) $9{,}16 \times 14\,800 - 360^2$. h) Avec un prix fixe, $R = 3Q$.

</details>

### Ex M16.6 — Des signes aléatoires d'amplitudes différentes sur des mesures corrélées

<details><summary>Indice 1</summary>

Relis le §6 : le lemme et sa conséquence.

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(\pm a) = a^2$ ; $\mathbb{V}\big(\sum\varepsilon_ix_i\big) = \sum\mathbb{V}(\varepsilon_i)\,\mathbb{E}[x_i^2]$ ; a) est la somme de toutes les cases de la matrice de covariance.

</details>
<details><summary>Indice 3</summary>

e) $\mathbb{E}[x_1^2] = \mathbb{V}(x_1) + \mathbb{E}[x_1]^2$. d) $\varepsilon_1^2 = 1$. f) Un seul signe : $\mathbb{V}(\varepsilon T) = \mathbb{E}[\varepsilon^2]\,\mathbb{E}[T^2]$. g) La somme vaut $T + S$, deux morceaux décorrélés : leurs variances s'ajoutent.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M16.7 — (Aᵏ)ᵢⱼ compte les chemins de longueur k

<details><summary>Indice 1</summary>

Une récurrence sur $k$ (R4 §7).

</details>
<details><summary>Indice 2</summary>

Range les chemins de longueur $k + 1$ selon leur avant-dernier nœud $l$.

</details>
<details><summary>Indice 3</summary>

Pour un $l$ fixé, il y a $c_k(i, l)$ façons d'aller de $i$ à $l$, puis $A_{lj}$ façons (0 ou 1) d'aller de $l$ à $j$ ; reconnais $(\mathbf{A}^k\mathbf{A})_{ij}$.

</details>

### Ex M16.8 — Sans cycle si et seulement si nilpotente

<details><summary>Indice 1</summary>

Le principe des tiroirs (fiche §4) pour le sens direct ; un cycle répété pour la réciproque.

</details>
<details><summary>Indice 2</summary>

Un chemin de $n$ arêtes visite $n + 1$ nœuds. Un cycle de longueur $m$ parcouru $q$ fois est un chemin de longueur $qm$.

</details>
<details><summary>Indice 3</summary>

5 : développe le produit, les termes se télescopent ; pour $i \ne j$, le coefficient de $\mathbf{I}$ est nul.

</details>

### Ex M16.9 — La variance d'un produit de deux variables indépendantes

<details><summary>Indice 1</summary>

M02b §5 donne $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$ pour des variables indépendantes : applique-le deux fois.

</details>
<details><summary>Indice 2</summary>

$\{X^2 = u\}$ est la réunion de $\{X = \sqrt{u}\}$ et $\{X = -\sqrt{u}\}$.

</details>
<details><summary>Indice 3</summary>

3 : développe $(\mathbb{V}(X) + \mathbb{E}[X]^2)(\mathbb{V}(Y) + \mathbb{E}[Y]^2)$. 5 : divise par $\mathbb{E}[X]^2\,\mathbb{E}[Y]^2$.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M16.10 — Pont : n points rangés en lignes, X W + 1bᵀ

<details><summary>Indice 1</summary>

Relis « Beaucoup de points d'un coup » (§1), puis le §2.

</details>
<details><summary>Indice 2</summary>

$\mathbf{1}\mathbf{b}^\top$ : une colonne de 4 uns fois la ligne $\mathbf{b}^\top$.

</details>
<details><summary>Indice 3</summary>

e) C'est c) avec une colonne de uns en plus : $[\mathbf{x}, 1]\,\mathbf{H} = [\mathbf{x}\mathbf{W} + \mathbf{b}, 1]$ pour chaque ligne.

</details>

### Ex M16.11 — Expliquer pourquoi la variance d'un produit n'est pas le produit des variances

<details><summary>Indice 1</summary>

Relis l'exemple du chiffre d'affaires (§5).

</details>
<details><summary>Indice 2</summary>

Que devient une petite erreur de longueur quand on la multiplie par la largeur ?

</details>
<details><summary>Indice 3</summary>

Trois termes : deux amplifiés par les moyennes, un petit produit de variances ; et le cas d'une mesure exacte.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M16.E1 — « Pourquoi l'écart-type d'une somme de n termes indépendants grandit-il comme √n ? »

<details><summary>Indice 1</summary>

Qu'est-ce qui s'additionne : les variances ou les écarts-types ?

</details>
<details><summary>Indice 2</summary>

Covariances nulles ⇒ variance $n\sigma^2$ ; termes égaux ⇒ variance $n^2\sigma^2$.

</details>
<details><summary>Indice 3</summary>

Ajoute le rôle des signes aléatoires (§6) et la conséquence pour une moyenne.

</details>

<a id="notebook"></a>

## Notebook

### M16.12 — La matrice homogène d'une application affine

<details><summary>Indice 1</summary>

Fiche §2 : $\mathbf{H} = \begin{pmatrix} \mathbf{W} & \mathbf{0} \\ \mathbf{b} & 1 \end{pmatrix}$.

</details>
<details><summary>Indice 2</summary>

`np.hstack([W, np.zeros((n, 1))])` pour le haut, `np.hstack([b, [1.0]])` pour le bas, puis `np.vstack`.

</details>
<details><summary>Indice 3</summary>

Vérifie les formes avant de construire : `W.ndim == 2`, `b.ndim == 1`, `len(b) == W.shape[1]`.

</details>

### M16.13 — Sommer sur les chemins d'un graphe sans cycle

<details><summary>Indice 1</summary>

Fiche §4 : sans cycle, $\mathbf{S} = \mathbf{A} + \cdots + \mathbf{A}^{n-1}$.

</details>
<details><summary>Indice 2</summary>

Le test de cycle : multiplie $n - 1$ fois le motif booléen `(A != 0)` par lui-même, en gardant `(B @ P) > 0` ; s'il reste un `True`, il y a un cycle.

</details>
<details><summary>Indice 3</summary>

Une boucle qui garde la puissance courante et ajoute son coefficient `[source, target]` ; pour `source == target`, la boucle donne 0 toute seule sur un graphe sans cycle.

</details>

### M16.14 — Espérance et variance d'un produit

<details><summary>Indice 1</summary>

Fiche §5, la formule encadrée.

</details>
<details><summary>Indice 2</summary>

Trois termes pour la variance ; vérifie d'abord que les variances sont positives ou nulles.

</details>
<details><summary>Indice 3</summary>

Rends un tuple de deux `float` Python.

</details>

### M16.15 — Prédire l'écart-type d'une somme de produits aléatoires

<details><summary>Indice 1</summary>

Fiche §6 et 💼 M16.E1.

</details>
<details><summary>Indice 2</summary>

Des mesures égales : la somme vaut 25 fois une mesure. Des mesures indépendantes : les variances s'ajoutent.

</details>
<details><summary>Indice 3</summary>

Avec des signes indépendants, seuls les $\mathbb{E}[x_i^2]$ comptent, que les mesures soient corrélées ou non.

</details>

### M16.16 — Une variance multipliée d'étage en étage

<details><summary>Indice 1</summary>

Fiche §7, « Avec un bruit à chaque étage ».

</details>
<details><summary>Indice 2</summary>

$v_{k+1} = g^2v_k + s^2$, de point fixe $\frac{s^2}{1 - g^2}$ ; l'écart au point fixe est multiplié par $g^2$ à chaque étage.

</details>
<details><summary>Indice 3</summary>

Pour $g = 0{,}6$, $v_k = \frac{1 - 0{,}36^k}{0{,}64}$ : cherche le premier $k$ tel que $0{,}36^k < 0{,}01$.

</details>

### M16.17 — L'image d'une figure par une suite d'applications affines

<details><summary>Indice 1</summary>

Fiche §2 et la figure de la maison.

</details>
<details><summary>Indice 2</summary>

Ajoute une colonne de uns aux sommets, multiplie par le produit cumulé des matrices, et garde les deux premières colonnes.

</details>
<details><summary>Indice 3</summary>

`ax.fill` ou `Polygon` pour chaque étape, avec une couleur et un nom (`label=`), puis `ax.legend()` et `ax.set_aspect("equal")`.

</details>

### M16.18 — Chasse à l'erreur

<details><summary>Indice 1</summary>

Fiche, les ⚠️ des §2, §4 et §5.

</details>
<details><summary>Indice 2</summary>

(A) Où est la translation dans la matrice construite ? (B) Combien de termes a la variance d'un produit ? (C) Que se passe-t-il sur un graphe avec un cycle ?

</details>
<details><summary>Indice 3</summary>

(A) Pour des lignes, $\mathbf{W}$ en haut à gauche et $\mathbf{b}$ sur la dernière ligne. (C) Teste d'abord le cycle, comme `sum_over_paths`.

</details>

### M16.19 — Un test de propriété

<details><summary>Indice 1</summary>

Fiche §2 : $[\mathbf{x}, 1]\,\mathbf{H}_1\mathbf{H}_2 = [f_2(f_1(\mathbf{x})), 1]$.

</details>
<details><summary>Indice 2</summary>

Tire $\mathbf{W}_1$, $\mathbf{b}_1$, $\mathbf{W}_2$, $\mathbf{b}_2$ de formes compatibles et quelques points ; calcule les deux côtés.

</details>
<details><summary>Indice 3</summary>

Compare avec `np.allclose`, et mets dans le message ce qui était attendu.

</details>

### M16.20 — Défi : la loi du produit de deux uniformes

<details><summary>Indice 1</summary>

$\mathbb{E}[UV]$ et $\mathbb{V}(UV)$ : le §5. Pour la loi : calcule $P(UV \le z)$ en conditionnant sur $U = u$.

</details>
<details><summary>Indice 2</summary>

Pour $u \le z$, $P(V \le \frac{z}{u}) = 1$ ; pour $u > z$, elle vaut $\frac{z}{u}$.

</details>
<details><summary>Indice 3</summary>

$P(UV \le z) = z + \int_z^1\frac{z}{u}\,du$ ; dérive pour la densité ; la médiane résout une équation qu'on résout par dichotomie (R7).

</details>
