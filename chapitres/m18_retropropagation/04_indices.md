# M18 · Différentiation automatique et calcul matriciel — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Ponts, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M18.Q1 — Lire un graphe de calcul : nœuds, arêtes, ordre d'évaluation

<details><summary>Indice 1</summary>

Relis « Le graphe » (fiche §1) : un nœud par entrée et par opération, une arête par argument.

</details>
<details><summary>Indice 2</summary>

Dessine le graphe : $r_1$ et $r_2$ à gauche, $u_1$ et $u_2$ au milieu, $R$ à droite. Un ordre de calcul est valide si chaque arête va vers un nœud calculé plus tard.

</details>
<details><summary>Indice 3</summary>

6 : un programme qui réaffecte `x` crée une nouvelle valeur, donc un nouveau nœud ; l'ancienne valeur reste un nœud du graphe.

</details>

### M18.Q2 — Combien de chemins, et quelle somme ?

<details><summary>Indice 1</summary>

Relis « La somme sur les chemins » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Liste les chemins de $x$ à $y$ en partant de $x$ : par $a$ (puis directement vers $y$, ou par $c$), ou par $b$ (puis par $c$). Multiplie les dérivées locales le long de chacun, puis additionne.

</details>
<details><summary>Indice 3</summary>

1. et 2. : trois chemins, de produits 12, $-6$ et 2. 3. : les chemins de $a$ à $y$ sont $a \to y$ et $a \to c \to y$. 4. : un chemin fait 4 pas dans chaque direction ; choisis lesquels des 8 pas vont dans la première (R8).

</details>

### M18.Q3 — Calculer avec ε² = 0

<details><summary>Indice 1</summary>

Relis « Les nombres duaux » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Développe comme un polynôme en $\varepsilon$, puis efface tout terme en $\varepsilon^2$. Pour une fonction $g$, $g(a + b\varepsilon) = g(a) + g'(a)\,b\,\varepsilon$.

</details>
<details><summary>Indice 3</summary>

1. : $3 - 3\varepsilon + 2\varepsilon$. 3. : multiplie le haut et le bas par $2 - \varepsilon$. 7. : un carré nul n'oblige pas un nombre dual à être nul ; pense à une matrice nilpotente (M16).

</details>

### M18.Q4 — Le mode inverse : dans quel ordre visiter les nœuds ?

<details><summary>Indice 1</summary>

Relis « L'adjoint d'un nœud » et « Deux passes » (fiche §4).

</details>
<details><summary>Indice 2</summary>

L'adjoint d'un nœud demande ceux de **tous** ses successeurs. Écris les dérivées locales de $R = u_1/u_2$ et de $u_1 = r_1r_2$ : de quelles valeurs dépendent-elles ?

</details>
<details><summary>Indice 3</summary>

Ordre : $R$ d'abord, les entrées en dernier. $\frac{\partial R}{\partial u_1} = \frac{1}{u_2}$, $\frac{\partial R}{\partial u_2} = -\frac{u_1}{u_2^2}$, $\frac{\partial u_1}{\partial r_1} = r_2$ : il faut avoir gardé $u_1$, $u_2$, $r_1$ et $r_2$.

</details>

### M18.Q5 — Direct ou inverse, pour n entrées et m sorties ?

<details><summary>Indice 1</summary>

Relis « Une colonne ou une ligne de la jacobienne par passage » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Mode direct : une passe par **entrée** ; mode inverse : une passe par **sortie**, et la mémoire de la passe avant.

</details>
<details><summary>Indice 3</summary>

5. : relis « Le gradient bon marché » : le coût d'une passe arrière ne dépend pas du nombre d'entrées.

</details>

### M18.Q6 — La forme d'un gradient par rapport à une matrice

<details><summary>Indice 1</summary>

Relis « Le tableau des dérivées partielles » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le gradient a la forme de la variable : une dérivée partielle par coefficient, rangée à la place du coefficient.

</details>
<details><summary>Indice 3</summary>

2. : la dérivée de $X_{23}$ vaut 1 par rapport à $X_{23}$, 0 par rapport aux autres. 4. : l'approximation linéaire du §6.

</details>

### M18.Q7 — Identités de trace : vrai ou faux

<details><summary>Indice 1</summary>

Relis « La trace, et le produit scalaire des matrices » (fiche §7).

</details>
<details><summary>Indice 2</summary>

La trace est cyclique : on peut faire passer le dernier facteur en tête, pas échanger deux facteurs. Pour un « faux », cherche un contre-exemple avec des matrices $\mathbf{E}_{ij}$ ou $\mathbf{I}$.

</details>
<details><summary>Indice 3</summary>

2. : $\mathbf{A} = \mathbf{E}_{12}$, $\mathbf{B} = \mathbf{E}_{21}$, $\mathbf{C} = \mathbf{E}_{11}$. 6. : relis « La différentielle » : on lit $\mathbf{G} = \mathbf{M}^\top$.

</details>

### M18.Q8 — Gradient d'une moyenne, moyenne des gradients

<details><summary>Indice 1</summary>

Relis le §8 de la fiche.

</details>
<details><summary>Indice 2</summary>

La dérivation est linéaire. Pour la moyenne des carrés des distances, le gradient est $2(\mathbf{p} - \bar{\mathbf{x}})$.

</details>
<details><summary>Indice 3</summary>

3. : $\bar{\mathbf{x}} = (2, 1)$. 5. : $\mathbf{I}$ est symétrique ; relis « Pourquoi des directions au hasard ».

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M18.R1 — La jacobienne d'une composée (M17)

<details><summary>Indice 1</summary>

Relis M17 §3 et §4.

</details>
<details><summary>Indice 2</summary>

$\mathbf{J}_g$ s'évalue au point intermédiaire $\mathbf{f}(3, 1)$ ; en ligne, le gradient de $h$ est $\mathbf{J}_g\,\mathbf{J}_{\mathbf{f}}$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{J}_g(u, v) = \begin{pmatrix} v & u + 2v \end{pmatrix}$ ; $\mathbf{J}_{\mathbf{f}}(x, y) = \begin{pmatrix} 1 & -1 \\ y & x \end{pmatrix}$.

</details>

### M18.R2 — Le gradient de wᵀAw (M09b)

<details><summary>Indice 1</summary>

Relis M09b §2.

</details>
<details><summary>Indice 2</summary>

$\nabla_{\mathbf{w}}(\mathbf{w}^\top\mathbf{A}\mathbf{w}) = (\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$, et $2\mathbf{A}\mathbf{w}$ seulement si $\mathbf{A}$ est symétrique.

</details>
<details><summary>Indice 3</summary>

$\mathbf{A}\mathbf{w} = (5, 0)$ et $\mathbf{A} + \mathbf{A}^\top = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix}$.

</details>

### M18.R3 — Différences centrées et choix du pas (M05a)

<details><summary>Indice 1</summary>

Relis M05a §6 et §7.

</details>
<details><summary>Indice 2</summary>

L'erreur de troncature de la différence centrée est d'ordre $h^2$ ; celle des arrondis grandit comme $\frac{1}{h}$.

</details>
<details><summary>Indice 3</summary>

2. : $\frac{1{,}331 - 0{,}729}{0{,}2}$. 3. : le meilleur pas équilibre $h^2$ et $\frac{\varepsilon}{h}$ : $h \approx \varepsilon^{1/3}$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M18.1 — Le graphe de calcul d'une formule de physique

<details><summary>Indice 1</summary>

Relis le §1 de la fiche : une arête par argument de chaque opération.

</details>
<details><summary>Indice 2</summary>

Calcule les onze opérations dans l'ordre de l'énoncé ($\cos\frac{\pi}{3} = 0{,}5$). Pour c), compte les arguments de chaque opération. Pour e), regroupe en une étape toutes les opérations dont les arguments sont déjà connus.

</details>
<details><summary>Indice 3</summary>

c) Six opérations ont un argument, cinq en ont deux. d) Regarde quels nœuds apparaissent dans deux opérations. e) Étape 1 : $u_1$, $u_2$, $u_6$, $u_8$ ; étape 2 : $u_3$, $u_7$, $u_9$ ; continue.

</details>

### Ex M18.2 — Dériver par la somme sur les chemins

<details><summary>Indice 1</summary>

Relis « La somme sur les chemins » (fiche §2), et son exemple.

</details>
<details><summary>Indice 2</summary>

Calcule d'abord les valeurs ($u_1 = 144$, $u_2 = 6$, $u_3 = 36$, $u_4 = 576$), puis la dérivée locale de chaque arête, par exemple $\frac{\partial P}{\partial u_3} = -\frac{u_4}{u_3^2}$.

</details>
<details><summary>Indice 3</summary>

b) $\frac{\partial u_4}{\partial R} \times \frac{\partial P}{\partial u_4} = 144 \times \frac{1}{36}$. c) $\frac{\partial u_2}{\partial R} \times \frac{\partial u_3}{\partial u_2} \times \frac{\partial P}{\partial u_3} = 1 \times 12 \times (-\frac49)$. g) Écris $\frac{\partial P}{\partial R}$ pour un $R$ quelconque : son signe change en un seul point.

</details>

### Ex M18.3 — Le mode direct à la main

<details><summary>Indice 1</summary>

Relis « Les nombres duaux » et « Le projectile, avec des nombres duaux » (fiche §3).

</details>
<details><summary>Indice 2</summary>

La graine porte la partie en $\varepsilon$ : $x = 2 + \varepsilon$ et $y = -1$ (sans $\varepsilon$) pour dériver par rapport à $x$. Calcule nœud par nœud : $x^2$, $x^2y$, $x + y$, $\ln(x + y)$, puis la somme.

</details>
<details><summary>Indice 3</summary>

$\ln(1 + b\varepsilon) = \ln 1 + \frac{1}{1}\,b\,\varepsilon = b\,\varepsilon$. f) $x^2y = (4 + 4\varepsilon)(-1 + 2\varepsilon)$ et $x + y = 1 + 3\varepsilon$. g) La règle du quotient avec $a = 3$, $b = 2$, $c = 1$, $d = -1$.

</details>

### Ex M18.4 — Le mode inverse à la main

<details><summary>Indice 1</summary>

Relis « Deux passes » et « Accumuler » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Passe avant, puis passe arrière dans l'ordre $f$, $u_3$, $u_2$, $u_1$, puis les entrées. Les dérivées locales : $\frac{\partial f}{\partial u_1} = u_3$, $\frac{\partial f}{\partial u_3} = u_1$, $\frac{\partial u_3}{\partial u_2} = \frac{1}{2\sqrt{u_2}}$, $\frac{\partial u_2}{\partial u_1} = \frac{\partial u_2}{\partial q} = 1$, $\frac{\partial u_1}{\partial p} = q$, $\frac{\partial u_1}{\partial q} = p$.

</details>
<details><summary>Indice 3</summary>

$\bar{u}_3 = 3$, $\bar{u}_2 = 0{,}75$, puis $\bar{u}_1 = \bar{f} \times u_3 + \bar{u}_2 \times 1$ : $u_1$ a deux successeurs. De même, $\bar{q}$ reçoit une contribution de $u_1$ et une de $u_2$. e) $\nabla f \cdot \mathbf{v}$. f) $u_1 = (3 + 2\varepsilon)(1 - \varepsilon)$, puis $u_2 = u_1 + (1 - \varepsilon)$, et $\sqrt{c + d\varepsilon} = \sqrt c + \frac{d}{2\sqrt c}\varepsilon$.

</details>

### Ex M18.5 — Le même gradient par les deux modes

<details><summary>Indice 1</summary>

Relis les §3, §4 et §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

Écris d'abord les dix dérivées locales : 1 sur les arêtes des sommes, $u_2$, $u_1$, $u_3$ et $u_4$ sur celles des deux produits. Puis trois passes directes (graines $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$) et une passe arrière.

</details>
<details><summary>Indice 3</summary>

Graine $\mathbf{e}_1$ : $\dot{u}_1 = 1$, $\dot{u}_2 = 0$, $\dot{u}_3 = 1$, $\dot{u}_4 = 5$, $\dot{f} = 4 \times 5 + 15 \times 1$. Passe arrière : $\bar{u}_4 = u_3 = 4$, $\bar{u}_3 = u_4 = 15$, et $\bar{x}_1 = \bar{u}_1 + \bar{u}_3$. g) Chaque passe utilise chaque arête une fois.

</details>

### Ex M18.6 — Le gradient de aᵀXb, de la forme de X

<details><summary>Indice 1</summary>

Relis le §6 de la fiche, et l'identité 1 du §7.

</details>
<details><summary>Indice 2</summary>

Dans $\sum_{ij}a_iX_{ij}b_j$, chaque $X_{ij}$ apparaît une seule fois, multiplié par $a_ib_j$.

</details>
<details><summary>Indice 3</summary>

$\frac{\partial f}{\partial X_{ij}} = a_ib_j$ : le tableau $\mathbf{a}\mathbf{b}^\top$, de forme $(3, 2)$. e) $\sum_{ij}G_{ij}H_{ij}$ n'a que deux termes non nuls.

</details>

### Ex M18.7 — Les gradients de tr(AX) et de tr(XᵀAX)

<details><summary>Indice 1</summary>

Relis les identités 2 et 3 du §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

$\operatorname{tr}(\mathbf{A}\mathbf{X}) = \sum_i(\mathbf{A}\mathbf{X})_{ii} = \sum_{i,j}A_{ij}X_{ji}$ : repère le coefficient de $X_{pq}$.

</details>
<details><summary>Indice 3</summary>

b) $\mathbf{A}^\top$. e) $(\mathbf{A} + \mathbf{A}^\top)\mathbf{X}$ avec $\mathbf{A} + \mathbf{A}^\top = \begin{pmatrix} 4 & 0 \\ 0 & 6 \end{pmatrix}$. f) $\sum_{ij}G_{ij}H_{ij}$ ne garde que $G_{11}$ et $G_{12}$.

</details>

### Ex M18.8 — Le gradient de log det X sur une matrice 2 × 2

<details><summary>Indice 1</summary>

Relis l'exemple du déterminant au §6 de la fiche, et l'identité 5 du §7.

</details>
<details><summary>Indice 2</summary>

$\det\mathbf{X} = x_{11}x_{22} - x_{12}x_{21}$ : dérive par rapport à chaque coefficient. Puis $\frac{\partial\ln\det\mathbf{X}}{\partial x_{ij}} = \frac{1}{\det\mathbf{X}}\frac{\partial\det\mathbf{X}}{\partial x_{ij}}$.

</details>
<details><summary>Indice 3</summary>

b) $\begin{pmatrix} x_{22} & -x_{21} \\ -x_{12} & x_{11} \end{pmatrix}$. d) $\mathbf{X}^{-1} = \frac{1}{\det\mathbf{X}}\begin{pmatrix} x_{22} & -x_{12} \\ -x_{21} & x_{11} \end{pmatrix}$ : compare avec c). f) $\det(\mathbf{X} + 0{,}01\,\mathbf{H}) = 4{,}01 \times 2{,}99 - 1{,}02 \times 2$ ; divise par $\det\mathbf{X}$ avant de prendre le logarithme.

</details>

### Ex M18.9 — Le gradient d'une moyenne de distances

<details><summary>Indice 1</summary>

Relis « La moyenne des gradients » et « Les distances elles-mêmes » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\nabla F(\mathbf{p}) = \frac14\sum_k\frac{\mathbf{p} - \mathbf{x}_k}{\lVert\mathbf{p} - \mathbf{x}_k\rVert}$ : la moyenne de quatre vecteurs **unitaires**, qui partent des villes vers $\mathbf{p}$.

</details>
<details><summary>Indice 3</summary>

c) Les quatre vecteurs en $(3, 1)$ : $\frac{(3, 1)}{\sqrt{10}}$, $\frac{(-5, 1)}{\sqrt{26}}$, $\frac{(-3, -5)}{\sqrt{34}}$, $\frac{(3, -3)}{\sqrt{18}}$. d) Les diagonales $y = x$ et $y = 4 - \frac{x}{2}$ ; sur $[AC]$, les directions vers $A$ et vers $C$ sont opposées. e) $\frac{AC + BD}{4}$.

</details>

### Ex M18.10 — La différentielle d'une fonction de matrice

<details><summary>Indice 1</summary>

Relis « La différentielle » (fiche §7) : la règle du produit, sans changer l'ordre, puis la cyclicité de la trace.

</details>
<details><summary>Indice 2</summary>

$\mathrm{d}(\mathbf{X}^2) = \mathrm{d}\mathbf{X}\,\mathbf{X} + \mathbf{X}\,\mathrm{d}\mathbf{X}$. Pour $f$, $\operatorname{tr}(\mathrm{d}\mathbf{X}\,\mathbf{X}) = \operatorname{tr}(\mathbf{X}\,\mathrm{d}\mathbf{X})$. Pour $g$, écris chaque terme $\mathbf{a}^\top\cdots\mathbf{b}$ comme une trace, et fais passer $\mathrm{d}\mathbf{X}$ à la fin.

</details>
<details><summary>Indice 3</summary>

$\mathrm{d}f = \operatorname{tr}(2\mathbf{X}\,\mathrm{d}\mathbf{X})$ donne $\mathbf{G} = (2\mathbf{X})^\top$. $\mathrm{d}g = \operatorname{tr}(\mathbf{X}\mathbf{b}\mathbf{a}^\top\mathrm{d}\mathbf{X}) + \operatorname{tr}(\mathbf{b}\mathbf{a}^\top\mathbf{X}\,\mathrm{d}\mathbf{X})$ : transpose chacune des deux matrices devant $\mathrm{d}\mathbf{X}$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M18.11 — La règle de la chaîne sur un graphe sans cycle

<details><summary>Indice 1</summary>

Relis le §2 de la fiche, et la somme sur les chemins de M16 §4.

</details>
<details><summary>Indice 2</summary>

Récurrence **forte** sur $k$ : suppose $\dot{u}_j = S_j$ pour tous les $j < k$. Un chemin de $x$ à $u_k$ finit par une arête $u_j \to u_k$.

</details>
<details><summary>Indice 3</summary>

$S_k = \sum_{j < k}D_{jk}\,S_j$ (on classe les chemins par leur dernière arête), et la question 1 donne la même formule pour $\dot{u}_k$. Pour 5., écris la coordonnée $k$ de $\mathbf{D}^\top\dot{\mathbf{u}}$ : c'est $\sum_jD_{jk}\,\dot{u}_j$.

</details>

### Ex M18.12 — Les nombres duaux calculent la dérivée

<details><summary>Indice 1</summary>

Relis « Les nombres duaux » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pour 2., remplace $f(a + b\varepsilon)$ et $g(a + b\varepsilon)$ par leurs formes compatibles, et calcule la somme, le produit, le quotient ; compare la partie en $\varepsilon$ aux règles de dérivation de R7.

</details>
<details><summary>Indice 3</summary>

Produit : $\big(f(a) + bf'(a)\varepsilon\big)\big(g(a) + bg'(a)\varepsilon\big) = f(a)g(a) + b\,(f'g + fg')(a)\,\varepsilon$. Composée : applique la compatibilité de $g$ au point $f(a)$, avec la partie en $\varepsilon$ égale à $bf'(a)$.

</details>

### Ex M18.13 — Le mode inverse calcule tout le gradient en un passage

<details><summary>Indice 1</summary>

Relis le §4 de la fiche, et ta démonstration de M18.11.

</details>
<details><summary>Indice 2</summary>

C'est M18.11 « à l'envers » : classe les chemins de $u_j$ à $y$ par leur **première** arête.

</details>
<details><summary>Indice 3</summary>

$T_j = \sum_{k > j}D_{jk}T_k$. Pour une entrée, $T_i$ est la même somme que $S_N$ de M18.11. En 5., la coordonnée $j$ de $\mathbf{D}\mathbf{t}$ est $\sum_kD_{jk}T_k$, d'où $(\mathbf{I} - \mathbf{D})\mathbf{t} = \mathbf{e}_N$.

</details>

### Ex M18.14 — ∇ log det X = X⁻ᵀ

<details><summary>Indice 1</summary>

Relis « La comatrice » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Le développement selon la ligne $i$ est **affine** en les coefficients de cette ligne : sa dérivée par rapport à $X_{ij}$ se lit directement.

</details>
<details><summary>Indice 3</summary>

$\frac{\partial\det\mathbf{X}}{\partial X_{ij}} = C_{ij}$. Puis $\mathbf{X}\operatorname{com}(\mathbf{X})^\top = \det\mathbf{X}\;\mathbf{I}$ donne $\mathbf{X}^{-1} = \frac{\operatorname{com}(\mathbf{X})^\top}{\det\mathbf{X}}$ : transpose.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M18.15 — Pont : combien de passages dans chaque mode ?

<details><summary>Indice 1</summary>

Relis le §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

La jacobienne a une ligne par sortie et une colonne par entrée ; le mode direct en donne une colonne par passage, le mode inverse une ligne.

</details>
<details><summary>Indice 3</summary>

a) $(3, 2\,000)$. d) Toutes les émissions qui augmentent ensemble, c'est une seule direction : un produit jacobienne-vecteur. e) La somme des sorties, c'est une seule combinaison des lignes : un produit vecteur-jacobienne. f) $10^6 \times 8$ octets.

</details>

### Ex M18.16 — Pont : de la convention de MML à celle de NumPy

<details><summary>Indice 1</summary>

Relis M17 §4 et « Le cas d'un vecteur, et la convention de MML » (fiche §6).

</details>
<details><summary>Indice 2</summary>

En ligne, $\nabla(\mathbf{x}^\top\mathbf{A}\mathbf{x}) = \mathbf{x}^\top(\mathbf{A} + \mathbf{A}^\top)$ et $\nabla(\mathbf{b}^\top\mathbf{x}) = \mathbf{b}^\top$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{A} + \mathbf{A}^\top = \begin{pmatrix} 2 & 2 \\ 2 & 6 \end{pmatrix}$. c) Une matrice $(3, 4)$ aplatie a 12 coordonnées : sa jacobienne est une ligne de 12.

</details>

### Ex M18.17 — MML §5.4 et §5.5

<details><summary>Indice 1</summary>

Lis d'abord les §6 et §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

Cherche, au début du §5.4, la forme de la dérivée d'une matrice par rapport à une matrice, et la figure qui montre deux façons de la calculer. Dans le §5.5, cherche les identités de la trace, du déterminant et de l'inverse.

</details>
<details><summary>Indice 3</summary>

Pour l'inverse, différentie $\mathbf{X}\mathbf{X}^{-1} = \mathbf{I}$ avec la règle du produit, sans changer l'ordre des facteurs.

</details>

### Ex M18.18 — MML §5.6

<details><summary>Indice 1</summary>

Lis d'abord les §1 à §4 de la fiche.

</details>
<details><summary>Indice 2</summary>

Dans le §5.6.2, repère la liste des variables intermédiaires de l'exemple et son graphe ; écris la dérivée locale de chaque arête.

</details>
<details><summary>Indice 3</summary>

Une variable intermédiaire de l'exemple sert deux fois : son adjoint reçoit deux contributions. Choisis $x = 1$ pour des calculs simples.

</details>

### Ex M18.19 — Expliquer le mode inverse

<details><summary>Indice 1</summary>

Relis le §4 de la fiche et choisis ton image (une rivière et ses affluents, une recette).

</details>
<details><summary>Indice 2</summary>

Dans ton image, qu'est-ce que l'adjoint d'une étape ? Qu'est-ce qui se multiplie, et qu'est-ce qui s'additionne ?

</details>
<details><summary>Indice 3</summary>

Le plan : la question (la sensibilité du résultat à chaque étape) ; le départ à la fin, à 1 ; la remontée, en multipliant ; les étapes qui en alimentent plusieurs, en additionnant ; la mémoire de l'aller ; une seule remontée pour toutes les entrées.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M18.E1 — « Différentiation automatique, symbolique ou numérique : quelles différences ? »

<details><summary>Indice 1</summary>

Relis les §3 à §5 de la fiche, et M05a pour les différences finies.

</details>
<details><summary>Indice 2</summary>

Pour chaque méthode : ce qu'elle manipule (des formules, des nombres et un pas $h$, des nombres et les règles de dérivation), ce qu'elle rend, ce qu'elle coûte.

</details>
<details><summary>Indice 3</summary>

Le plan : symbolique (expressions exactes, qui gonflent) ; numérique (approchée, une erreur qui dépend du pas) ; automatique (exacte aux arrondis près, même avec des boucles) ; ses deux modes ; pourquoi le mode inverse pour un seul nombre et des milliers d'entrées (la forme d'une aile, par exemple).

</details>

### M18.E2 — « Quand le mode direct est-il préférable au mode inverse ? »

<details><summary>Indice 1</summary>

Relis le §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

Une passe directe donne une colonne de la jacobienne, une passe arrière une ligne.

</details>
<details><summary>Indice 3</summary>

Le plan : colonne contre ligne ; peu d'entrées et beaucoup de sorties ; un exemple (une trajectoire en fonction d'une condition initiale) ; la mémoire ; une seule direction.

</details>

<a id="notebook"></a>

## Notebook

### M18.20 — Les nombres duaux : la classe `Dual`, et `dual_derivative`

<details><summary>Indice 1</summary>

Fiche §3, « Les nombres duaux » ; la docstring de la classe donne la règle de chaque opération.

</details>
<details><summary>Indice 2</summary>

Une petite fonction d'aide qui change un nombre ordinaire `c` en `Dual(c, 0.0)` évite de répéter ce test dans chaque opération. `__radd__` et `__rmul__` peuvent appeler `__add__` et `__mul__` (la somme et le produit commutent), mais pas `__rsub__` ni `__rtruediv__` : là, l'ordre compte. Chaque opération construit un **nouveau** `Dual`, sans toucher à `self`.

</details>
<details><summary>Indice 3</summary>

Avec `a, b = self.value, self.derivative` et `c, d` ceux de l'autre opérande, le produit est `Dual(a * c, a * d + b * c)`, et `sin` rend `Dual(math.sin(a), math.cos(a) * b)` ; les autres suivent le même modèle. Pour la puissance, traite `p == 0` d'abord, puis les deux cas de `ValueError`. `dual_derivative` : `y = f(Dual(x, 1.0))`, puis trois cas, un `Dual`, un nombre, autre chose. Pour l'usage : `dual_derivative(lambda t: ..., x)[1]`.

</details>

### M18.21 — Le gradient en mode direct : `forward_gradient`

<details><summary>Indice 1</summary>

Fiche §3 (une graine par passe) et §5.

</details>
<details><summary>Indice 2</summary>

Convertis `x` en un tableau de flottants (`np.array(x, dtype=float)`, une copie), vérifie `ndim == 1` et `size > 0`, puis fais une passe par coordonnée.

</details>
<details><summary>Indice 3</summary>

La passe `i` évalue `f` sur `[Dual(point[j], 1.0 if j == i else 0.0) for j in range(n)]` ; range la partie `derivative` du résultat à la case `i` d'un tableau `np.zeros(n)` (une fonction qui rend un nombre laisse 0). Pour c), passe `Counted(height_21)` à ta fonction, puis lis son attribut `calls`.

</details>

### M18.22 — Lire le gradient dans la différentielle : `gradient_from_differential`

<details><summary>Indice 1</summary>

Fiche §6, « Lire le gradient dans l'approximation linéaire ».

</details>
<details><summary>Indice 2</summary>

Ramène `shape` à un tuple (`(shape,)` pour un entier) et vérifie chaque longueur ; `np.ndindex(shape)` parcourt toutes les cases, quel que soit le nombre d'indices.

</details>
<details><summary>Indice 3</summary>

Pour chaque `index` : un déplacement `np.zeros(shape)` avec un 1 en `index`, puis `float(differential(...))` à la case `index` du gradient. Pour l'usage : `Counted(lambda H: det_X * np.trace(np.linalg.solve(X_22, H)))`, avec `det_X = np.linalg.det(X_22)`.

</details>

### M18.23 — SymPy : dériver une fonction de matrice symbolique

<details><summary>Indice 1</summary>

Fiche §7 ; l'énoncé donne les trois dérivées de `MatrixSymbol` à calculer.

</details>
<details><summary>Indice 2</summary>

Un seul dictionnaire `{A: sympy.Matrix(A_23), X: sympy.Matrix(X_23), a: sympy.Matrix(a_23), b: sympy.Matrix(b_23)}` sert aux trois évaluations : `.subs(...).doit()`, puis `np.array(..., dtype=float)`. Compare avec `np.allclose` à `A_23.T`, `(A_23 + A_23.T) @ X_23` et `np.outer(a_23, b_23)`.

</details>
<details><summary>Indice 3</summary>

Pour c) : `S = sympy.Matrix(2, 2, sympy.symbols("x11 x12 x21 x22"))` et `L = sympy.log(S.det())` ; la matrice des dérivées est `sympy.Matrix(2, 2, lambda i, j: sympy.diff(L, S[i, j]))`, à évaluer par `.subs(dict(zip(S, X_23.ravel())))`.

</details>

### M18.24 — Prédire le nombre d'opérations de chaque mode

<details><summary>Indice 1</summary>

Fiche §5 : ce que donne une passe directe, ce que donne une passe arrière.

</details>
<details><summary>Indice 2</summary>

Compte d'abord les multiplications d'une seule évaluation de $f$, un produit de $n$ nombres ; puis le nombre d'évaluations que fait le mode direct pour tout le gradient.

</details>
<details><summary>Indice 3</summary>

Dans `product_by_hand_24`, seule la boucle de la passe arrière est comptée : combien de produits « adjoint × dérivée locale » fait-elle à chaque tour (une arête par produit), et combien de tours ? Pour d), écris chacun des deux comptes comme une fonction de $n$, puis remplace $n$ par 16.

</details>

### M18.25 — Différences finies contre nombres duaux

<details><summary>Indice 1</summary>

M05a (l'erreur d'une différence centrée et le choix du pas) et fiche §8.

</details>
<details><summary>Indice 2</summary>

`float(sympy.diff(sympy.exp(sympy.sin(x_25)), x_25).subs(x_25, 1))` pour la dérivée exacte ; une liste en compréhension sur `STEPS_25` pour les treize erreurs.

</details>
<details><summary>Indice 3</summary>

a) `np.argmin` rend un indice, qui part de 0, alors que la liste des pas commence à $h = 10^{-1}$. b) `math.floor(math.log10(...))`. c) et d) Sur des axes logarithmiques, une erreur proportionnelle à $h^p$ est une droite de pente $p$ : compte de combien de puissances de 10 l'erreur change quand $h$ change d'une puissance de 10. e) `mymath.autodiff.dual_derivative(f_dual_25, 1.0)[1]`, comparée en valeur absolue.

</details>

### M18.26 — Dessiner un graphe de calcul

<details><summary>Indice 1</summary>

Fiche §1, §2 et §4 : le projectile, son tableau de dérivées locales, sa passe arrière et sa figure.

</details>
<details><summary>Indice 2</summary>

Les dérivées locales : celles d'un produit, d'une somme et d'un quotient, par rapport à chacun de leurs arguments, aux valeurs de la passe avant. Les adjoints : $\bar{R} = 1$, puis $\bar{u}_1$ et $\bar{u}_2$, puis $r_1$ et $r_2$, qui ont chacun deux successeurs.

</details>
<details><summary>Indice 3</summary>

$\bar{u}_2 = \bar{R} \times \left(-\frac{u_1}{u_2^2}\right)$ et $\bar{r}_1 = \bar{u}_1 \times r_2 + \bar{u}_2 \times 1$. Pour le dessin : une boucle sur `local.items()` qui fait `ax.annotate("", xy=positions[w], xytext=positions[u], arrowprops=...)` puis `ax.text(*EDGE_LABELS_26[(u, w)], ...)` ; une autre sur `positions.items()` pour les nœuds et les adjoints ; `Fraction(x).limit_denominator(100)` écrit $\frac49$ plutôt que 0,4444.

</details>

### M18.27 — Chasse à l'erreur : un gradient transposé, un adjoint incomplet, un pas trop petit

<details><summary>Indice 1</summary>

Fiche §4 (un nœud qui a plusieurs successeurs), §7 (le gradient de $\operatorname{tr}(\mathbf{A}\mathbf{X})$) et §8 (« Pourquoi des directions au hasard », et l'erreur classique sur le pas).

</details>
<details><summary>Indice 2</summary>

(1) `np.random.default_rng(5137).normal(size=X_27.shape)`. (2) Dessine le graphe de $f(x, y) = x\sin(xy)$ : combien d'arêtes partent de $x$ ? Chacune apporte un terme à $\bar{x}$. (3) Le pas que conseillent M05a et la fiche §8, de l'ordre de $10^{-5}$.

</details>
<details><summary>Indice 3</summary>

a) Refais la passe de `adjoints_27` en $(1{,}5 ;\ -0{,}5)$ : $u_1 = xy = -0{,}75$, $u_2 = \sin u_1$, $\bar{u}_2 = x = 1{,}5$, $\bar{u}_1 = 1{,}5\cos(-0{,}75)$, puis sa ligne de `x_bar`. (2) Dans `adjoints_27_fixed`, la ligne de `x_bar` doit avoir deux termes : celui du chemin direct $x \to f$, $\bar{f}\,u_2$, et celui qui passe par $u_1$. (1) La fiche §7 donne le gradient de $\operatorname{tr}(\mathbf{A}\mathbf{X})$ ; vérifie la forme sur une matrice $\mathbf{A}$ qui n'est pas carrée.

</details>

### M18.28 — Tester une classe par ses propriétés

<details><summary>Indice 1</summary>

M17.22 (un test de propriété) et fiche §3.

</details>
<details><summary>Indice 2</summary>

Distributivité : construis $u$, $v$, $w$ une seule fois par triplet (six nombres de `rng.normal(size=6)`), calcule `u * (v + w)` d'abord, puis `u * v + u * w` avec les mêmes objets, et compare valeurs et dérivées. Dérivées connues : `x = Dual(t, 1.0)`, puis `s, c = x.sin(), x.cos()`.

</details>
<details><summary>Indice 3</summary>

`assert math.isclose(left.derivative, right.derivative, rel_tol=1e-9, abs_tol=1e-12), f"case {k}: ..."` ; de même pour la valeur. Pour $\sin^2 + \cos^2$, `s * s + c * c` ; pour $t^p$, compare `(x ** p).derivative` à `p * t ** (p - 1)` pour plusieurs `p`, dont un négatif et un fractionnaire.

</details>

### M18.29 — Défi : la méthode de Newton pour √a, en mode direct

<details><summary>Indice 1</summary>

Fiche §3 : une boucle écrite avec les opérations de `Dual` se dérive comme une formule ; la graine est sur $a$.

</details>
<details><summary>Indice 2</summary>

Tout se joue au départ. Écris $a = m \cdot 4^k$ avec $\frac12 \le m < 2$ : alors $\sqrt{a} = \sqrt{m}\,2^k$, et $2^k$ est à moins d'un facteur $\sqrt2$ de $\sqrt{a}$. `math.frexp(a)` donne $a = m \cdot 2^e$ (rends l'exposant pair), et `math.ldexp(1.0, k)` vaut $2^k$ ; une boucle qui divise par 4 marche aussi.

</details>
<details><summary>Indice 3</summary>

`a_dual = mymath.autodiff.Dual(a, 1.0)` et un départ constant `Dual(2.0 ** k, 0.0)` ; puis quelques tours de `x = newton_step_29(x, a_dual)`. Compte : l'erreur relative du départ est au plus 0,42, et chaque pas la remplace à peu près par la moitié de son carré.

</details>
