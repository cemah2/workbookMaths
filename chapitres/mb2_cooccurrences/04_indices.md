# MB2 · Cooccurrences, PMI et embeddings — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB2.Q1 — Bases 2 et 16 : le nombre de chiffres d'un entier, la valeur d'un octet, les bits qu'il faut pour N valeurs

<details><summary>Indice 1</summary>

Fiche §1 : « Les chiffres d'un entier » (le nombre de chiffres), « Base 16 : un chiffre pour quatre bits » et « Combien de bits pour N valeurs ? ».

</details>
<details><summary>Indice 2</summary>

Un entier $N \ge 1$ a $k$ chiffres en base $b$ quand $b^{k-1} \le N < b^k$. Un chiffre hexadécimal vaut 4 bits, et sa valeur se lit $c_1 \times 16 + c_0$. Pour numéroter $N$ valeurs, il faut $2^k \ge N$.

</details>
<details><summary>Indice 3</summary>

1. Encadre $100\,000$ entre deux puissances de 2, puis de 16 ($2^{16} = 16^4 = 65\,536$). 2. A vaut 10, D vaut 13 et E vaut 14. 3. Encadre 26 et 1 000 entre deux puissances de 2 consécutives. 4. 12 bits font combien de groupes de 4 ?

</details>

### MB2.Q2 — La PMI d'une case : son signe, −∞, la PPMI, la borne des événements rares, et l'information mutuelle qui en est la moyenne

<details><summary>Indice 1</summary>

Fiche §2 : la définition de la PMI et de la PPMI, le lift dans « Plus souvent que par hasard ? », « L'information mutuelle, moyenne des PMI » et « La borne des événements rares ».

</details>
<details><summary>Indice 2</summary>

Lift $= \frac{p(x, y)}{p(x)\,p(y)}$ et $\operatorname{PMI} = \ln(\text{lift})$. $\operatorname{PMI}(x, y) \le \min(-\ln p(x), -\ln p(y))$. L'information mutuelle est une divergence KL (M06).

</details>
<details><summary>Indice 3</summary>

1. Multiplie le lift par $p(x)\,p(y)$ ; la PMI est le logarithme népérien du lift. 2. $\ln 0$ et $\max(0, -\infty)$. 3. $-\ln 0{,}05$ ; quand $p(x, y) = p(y)$. 4. Que fait $\max(0, \cdot)$ aux termes négatifs d'une moyenne ? 5. Une KL peut-elle être négative ?

</details>

### MB2.Q3 — Lisser une marge : quelles colonnes gagnent, de combien bouge la PMI d'une colonne, et quels classements le lissage garde

<details><summary>Indice 1</summary>

Fiche §3 : « Remonter les colonnes rares » (le lien avec la loi tempérée de M28) et « Une constante par colonne ».

</details>
<details><summary>Indice 2</summary>

$\frac{p_\alpha(y)}{p(y)}$ est proportionnel à $p(y)^{\alpha - 1}$. $\operatorname{PMI}_\alpha(x, y) = \operatorname{PMI}(x, y) - \ln\frac{p_\alpha(y)}{p(y)}$ : un décalage qui ne dépend que de la colonne.

</details>
<details><summary>Indice 3</summary>

1. Avec $\alpha - 1 < 0$, le rapport décroît quand $p(y)$ croît, et sa moyenne pondérée par $p(y)$ vaut 1 ; si la marge n'est pas uniforme, les rapports ne sont pas tous égaux. 2. $-\ln\frac{0{,}05}{0{,}01}$. 3. et 4. Une constante ajoutée à toute une colonne, ou des constantes différentes d'une colonne à l'autre. 5. La limite $T \to \infty$ d'une loi tempérée (M28).

</details>

### MB2.Q4 — Répartir les valeurs singulières entre deux facteurs : ce qui dépend de β, ce qui n'en dépend pas, et pourquoi ne pas centrer une table creuse

<details><summary>Indice 1</summary>

Fiche §4 : « Deux facteurs, un exposant » et « Ne pas centrer une grande table creuse » ; M12d pour Eckart-Young.

</details>
<details><summary>Indice 2</summary>

$\mathbf{S}_k^\beta\mathbf{S}_k^{1-\beta} = \mathbf{S}_k$. Les colonnes de $\mathbf{U}_k$ sont unitaires : la colonne $i$ de $\mathbf{U}_k\mathbf{S}_k^\beta$ a pour longueur $s_i^\beta$. Centrer une colonne soustrait sa moyenne à toutes ses cases, zéros compris.

</details>
<details><summary>Indice 3</summary>

1. Développe le produit. 2. $\big(\frac62\big)^\beta$ pour les trois valeurs de $\beta$. 3. $(\mathbf{U}_k\mathbf{S}_k)(\mathbf{U}_k\mathbf{S}_k)^\top$ et $\mathbf{M}_k\mathbf{M}_k^\top$, avec $\mathbf{V}_k^\top\mathbf{V}_k = \mathbf{I}$. 4. Le nombre de cases, $10^{10}$, multiplié par 0,0005, puis toutes les cases. 5. Eckart-Young s'applique-t-il à une matrice non centrée ?

</details>

### MB2.Q5 — Le logit d'un taux et le sous-échantillonnage : ce qui bouge (l'ordonnée à l'origine), de combien, dans quel sens

<details><summary>Indice 1</summary>

Fiche §5 : « Le logit d'un taux » et « Sous-échantillonner une classe : l'étude cas-témoins ».

</details>
<details><summary>Indice 2</summary>

Le logit de vraisemblance maximale de $a$ succès et $b$ échecs vaut $\ln\frac{a}{b}$. Garder les positifs avec la probabilité $s_1$ et les négatifs avec $s_0$ multiplie la cote par $K = \frac{s_1}{s_0}$.

</details>
<details><summary>Indice 3</summary>

1. $\ln\frac{120}{360}$. 2. $K = \frac{1}{1/40}$ : le logit gagne $\ln K$. 3. Seule l'ordonnée à l'origine $\theta_0$. 4. $K = \frac{0{,}5}{0{,}5}$. 5. Retire $\ln K$.

</details>

### MB2.Q6 — Analogies, direction retirée et moyenne masquée : vrai ou faux, avec une raison

<details><summary>Indice 1</summary>

Fiche §6 : « Pourquoi on exclut a, b et c » (le lemme) ; §7 : la propriété de Pythagore et « Ce que le retrait ne fait pas » ; §8 : la définition de la moyenne masquée.

</details>
<details><summary>Indice 2</summary>

Avec $\varepsilon = \lVert\mathbf{b} - \mathbf{a}\rVert/\lVert\mathbf{c}\rVert$, $\cos(\mathbf{q}, \mathbf{c}) \ge \sqrt{1 - \varepsilon^2}$. $\lVert\mathbf{x}\rVert^2 = \lVert\mathbf{r}\rVert^2 + \frac{(\mathbf{x}\cdot\mathbf{u})^2}{\mathbf{u}\cdot\mathbf{u}}$. Un relevé de masque 0 est multiplié par 0.

</details>
<details><summary>Indice 3</summary>

1. Que vaut $\sqrt{1 - \varepsilon^2}$ pour $\varepsilon$ petit ? 2. Si $\mathbf{d} - \mathbf{c} = \mathbf{b} - \mathbf{a}$, que vaut $\mathbf{q}$ ? 3. Prends un vecteur orthogonal à $\mathbf{u}$. 4. Pense à une autre coordonnée corrélée à celle qu'on retire. 5. Regarde le numérateur et le dénominateur de la moyenne masquée.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### MB2.R1 — L'information mutuelle d'un tableau 2 × 2 (M06)

<details><summary>Indice 1</summary>

M06 : l'entropie, l'entropie conjointe, et $I(X ; Y) = H(X) + H(Y) - H(X, Y)$ ; fiche §2, « L'information mutuelle, moyenne des PMI ».

</details>
<details><summary>Indice 2</summary>

Les marges sont les sommes des lignes et des colonnes. $H = -\sum p\log_2 p$ en bits ; pour passer en nats, multiplie par $\ln 2$.

</details>
<details><summary>Indice 3</summary>

1. $0{,}20 + 0{,}04$ et $0{,}14 + 0{,}62$ ; puis les colonnes. 2. $H(X)$ et $H(Y)$ ont deux termes chacun ; $H(X, Y)$ a quatre termes distincts. 3. $H(X) + H(Y) - H(X, Y)$, puis $\times \ln 2$. 4. Compare $0{,}20$ à $0{,}24 \times 0{,}34$.

</details>

### MB2.R2 — La meilleure approximation de rang 1 d'une matrice et son erreur (Eckart-Young, M12d)

<details><summary>Indice 1</summary>

M12d : la SVD par les valeurs propres de $\mathbf{M}^\top\mathbf{M}$, et le théorème d'Eckart-Young ; fiche §4, « Rappel : SVD compacte et Eckart-Young ».

</details>
<details><summary>Indice 2</summary>

$s_i = \sqrt{\lambda_i(\mathbf{M}^\top\mathbf{M})}$, $\mathbf{v}_i$ un vecteur propre unitaire, $\mathbf{u}_i = \mathbf{M}\mathbf{v}_i/s_i$. L'erreur de la meilleure approximation de rang 1 vaut $\sqrt{s_2^2 + \cdots}$ en norme de Frobenius.

</details>
<details><summary>Indice 3</summary>

1. $\begin{pmatrix} a & c \\ c & a \end{pmatrix}$ a pour valeurs propres $a + c$ (vecteur $(1, 1)$) et $a - c$ (vecteur $(1, -1)$). 2. $\mathbf{M}\frac{(1, 1)}{\sqrt2} = \frac{(4, 8, 0)}{\sqrt2}$. 3. $s_1\mathbf{u}_1\mathbf{v}_1^\top$ répète une même ligne, à des facteurs près. 4. Calcule $\mathbf{M} - \mathbf{M}_1$ : une seule ligne non nulle.

</details>

### MB2.R3 — Cosinus, projection sur une droite et prototype d'une classe (M07, workbookIA B1)

<details><summary>Indice 1</summary>

M07 : le cosinus, la projection sur une droite et le barycentre ; fiche §6, « Cosinus, normalisation, produit scalaire ».

</details>
<details><summary>Indice 2</summary>

Le prototype est la moyenne des points de la classe. $\cos(\mathbf{q}, \mathbf{m}) = \frac{\mathbf{q}\cdot\mathbf{m}}{\lVert\mathbf{q}\rVert\lVert\mathbf{m}\rVert}$, et la projection sur la droite de $\mathbf{m}$ vaut $\frac{\mathbf{q}\cdot\mathbf{m}}{\mathbf{m}\cdot\mathbf{m}}\mathbf{m}$.

</details>
<details><summary>Indice 3</summary>

1. $\frac12\big((2, 7) + (4, 5)\big)$, et de même pour B. 2. $\mathbf{q}\cdot\mathbf{m}_A = 18 + 30$, $\lVert\mathbf{q}\rVert = \sqrt{61}$, $\lVert\mathbf{m}_A\rVert = \sqrt{45}$. 3. $\frac{48}{45}\mathbf{m}_A$. 4. $\lVert(3, -1)\rVert$ et $\lVert(-2, 3)\rVert$. 5. Le cosinus dépend-il de la longueur ?

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB2.1 — Des entiers en base 2 et en base 16 : conversions, une couleur #RRGGBB, les bits pour 5 000 codes, et un mot de 16 bits découpé en deux champs

<details><summary>Indice 1</summary>

Fiche §1, en entier : les divisions successives, le passage par groupes de 4 bits, les couleurs, le rappel sur les bits pour $N$ valeurs (R6 §4, M06 §7), et la propriété du champ de $\ell$ bits.

</details>
<details><summary>Indice 2</summary>

Divise par 2 jusqu'à un quotient nul, et lis les restes **du dernier au premier**. Chaque chiffre hexadécimal donne 4 bits : regroupe a) par 4 à partir de la droite. Une paire hexadécimale $c_1c_0$ vaut $16c_1 + c_0$. Le champ haut d'un mot de 16 bits découpé en 4 + 12 est $\lfloor w/2^{12}\rfloor$, le champ bas $w \bmod 2^{12}$.

</details>
<details><summary>Indice 3</summary>

a) $214 = 2 \times 107 + 0$, $107 = 2 \times 53 + 1$, … (huit divisions). b) $214 = 16 \times 13 + 6$. c) $128 + 64 + 8 + 2 + 1$. d) 4A, 7C, 59 : A vaut 10 et C vaut 12. e) $2^{12} = 4\,096$. f) Le premier chiffre hexadécimal est le champ haut ; les trois autres, B4D, le champ bas. g) Écris 200 en base 16 sur **trois** chiffres, et place le 9 devant.

</details>

### Ex MB2.2 — Cent oiseaux, trois milieux, quatre espèces : la PMI des cases, le lift d'une règle, la PPMI, l'espèce vue une seule fois, et l'information mutuelle comme moyenne

<details><summary>Indice 1</summary>

Fiche §2 : « Plus souvent que par hasard ? » (la PMI, le lift, la forme avec les comptes), « L'information mutuelle, moyenne des PMI », « La borne des événements rares ».

</details>
<details><summary>Indice 2</summary>

Avec les comptes : $\operatorname{PMI}(x, y) = \ln\frac{n(x, y)\,N}{n(x)\,n(y)}$, avec $N = 100$. Une case vide a une PMI de $-\infty$ ; la PPMI garde les PMI strictement positives. $I(X ; Y) = \sum p(x, y)\operatorname{PMI}(x, y)$ sur les cases non vides.

</details>
<details><summary>Indice 3</summary>

a) $\frac{6/40}{8/100}$. b) $\ln$ de a). c) $\ln\frac{3 \times 100}{25 \times 27}$. d) Les cases à 0 dans la table. e) $\ln\frac{1 \times 100}{35 \times 1}$. f) Calcule les neuf PMI finies et compte les positives (il y en a dans chaque ligne). g) Neuf termes $p(x, y)\operatorname{PMI}(x, y)$, dont quatre négatifs.

</details>

### Ex MB2.3 — Lisser la marge des espèces de la même table (α = 1/3) : la loi lissée, le décalage de la PMI de chaque colonne, et le classement des espèces d'un milieu avant et après

<details><summary>Indice 1</summary>

Fiche §3 : « Remonter les colonnes rares » et « Une constante par colonne ».

</details>
<details><summary>Indice 2</summary>

$p_\alpha(y) = \frac{n(y)^{1/3}}{\sum_{y'}n(y')^{1/3}}$, et $\operatorname{PMI}_\alpha(x, y) = \operatorname{PMI}(x, y) - \ln\frac{p_\alpha(y)}{p(y)}$. Les comptes 1, 8, 27 et 64 sont des cubes.

</details>
<details><summary>Indice 3</summary>

a) Les racines cubiques valent 1, 2, 3 et 4. b) $-\ln\frac{0{,}1}{0{,}01}$, $-\ln\frac{0{,}2}{0{,}08}$, $-\ln\frac{0{,}3}{0{,}27}$, $-\ln\frac{0{,}4}{0{,}64}$. c) Ajoute le décalage de la huppe à e) de MB2.2. d) $\ln\frac{0{,}06}{0{,}4 \times 0{,}2}$, et de même pour la grive et le moineau. e) Range les trois valeurs de d). f) Toute une colonne reçoit le même décalage.

</details>

### Ex MB2.4 — Quatre magasins, trois produits, une table de rang 2 de SVD donnée : les facteurs U S^β et V S^{1−β} pour β = 0, ½ et 1, leur produit, et le cosinus de deux magasins

<details><summary>Indice 1</summary>

Fiche §4 : « Rappel : SVD compacte et Eckart-Young » (la vérification d'une case) et « Deux facteurs, un exposant » (l'exemple des mangeoires et sa formule du cosinus).

</details>
<details><summary>Indice 2</summary>

La case $(i, j)$ du terme $k$ vaut $s_k\,(\mathbf{u}_k)_i\,(\mathbf{v}_k)_j$. $\mathbf{U}_2\mathbf{S}_2^\beta$ multiplie la première colonne de $\mathbf{U}_2$ par $399^\beta$ et la seconde par $133^\beta$ ; $\mathbf{V}_2\mathbf{S}_2^{1-\beta}$ fait de même avec $1 - \beta$. Un cosinus ne change pas si l'on multiplie ses deux vecteurs par un même nombre positif.

</details>
<details><summary>Indice 3</summary>

a) $399 \times \frac47 \times \frac{10}{19}$ et $133 \times \big(-\frac17\big) \times \frac{6}{19}$. b) Les lignes de $\mathbf{U}_2$, avec leurs deux coordonnées multipliées par 399 et par 133. c) Les lignes de $\mathbf{V}_2$, multipliées de même. d) Les lignes 1 et 4 de $\mathbf{A}_\beta$ sont $\frac47(399^\beta, -133^\beta)$ et $\frac47(399^\beta, 133^\beta)$ ; divise par $133^\beta$ et pose $t = 3^\beta$. e) Les lignes 1 et 2 : $\frac17(4 \times 399^\beta, -4 \times 133^\beta)$ et $\frac17(399^\beta, 4 \times 133^\beta)$. f) $\mathbf{S}_2^\beta\mathbf{S}_2^{1-\beta}$.

</details>

### Ex MB2.5 — Une bannière affichée 3 200 fois et cliquée 50 fois : le logit de vraisemblance maximale, puis un non-clic gardé sur 9, le décalage de ln 9 et sa correction

<details><summary>Indice 1</summary>

Fiche §5 : « Le logit d'un taux » et « Sous-échantillonner une classe : l'étude cas-témoins » (l'exemple du piège photographique).

</details>
<details><summary>Indice 2</summary>

Le logit de vraisemblance maximale de $a$ succès et $b$ échecs est $\ln\frac{a}{b}$, celui de la proportion $\frac{a}{a + b}$. Garder un négatif sur 9 et tous les positifs multiplie la cote par 9. Pour corriger, on retire $\ln 9$ au logit, ou l'on divise la cote par 9.

</details>
<details><summary>Indice 3</summary>

a) $\frac{50}{3\,200}$, simplifié. b) $\ln\frac{50}{3\,150}$. c) $\frac{3\,150}{9}$ non-clics gardés, puis $\ln\frac{50}{350}$. d) c) − b). e) $\frac{50}{50 + 350}$. f) La cote lue est $\frac{0{,}2}{0{,}8}$ ; divise-la par 9, puis repasse en probabilité, $\frac{\text{cote}}{1 + \text{cote}}$.

</details>

### Ex MB2.6 — Yaourt et fromage blanc, nature et sucrés : mesurer le parallélogramme d'une analogie (défaut, rapport ε, borne du cosinus), et dire si d peut l'emporter sur c

<details><summary>Indice 1</summary>

Fiche §6 : « Le parallélogramme d'une analogie » (la requête et le défaut) et « Pourquoi on exclut a, b et c » (le lemme, qui vaut pour tout candidat $\mathbf{x}$ assez proche de $\mathbf{q}$).

</details>
<details><summary>Indice 2</summary>

$\mathbf{q} - \mathbf{c} = \mathbf{b} - \mathbf{a}$ : le lemme avec $\mathbf{x} = \mathbf{c}$ et $\varepsilon = \frac{\lVert\mathbf{b} - \mathbf{a}\rVert}{\lVert\mathbf{c}\rVert}$. $\mathbf{q} - \mathbf{d}$ a pour norme $\delta$ : le lemme avec $\mathbf{x} = \mathbf{d}$ et $\varepsilon = \frac{\delta}{\lVert\mathbf{d}\rVert}$.

</details>
<details><summary>Indice 3</summary>

a) $(4, 10, 3) - (4, 5, 3) + (8, 4, 3)$. b) $(0, 5, 0) - (-1, 5, 0)$. c) $\frac{5}{\sqrt{89}}$, puis $\sqrt{1 - \frac{25}{89}}$. d) $\mathbf{q}\cdot\mathbf{c} = 109$, $\lVert\mathbf{q}\rVert^2 = 154$. e) $\lVert\mathbf{d}\rVert^2 = 139$. f) Compare e) et d). g) $(0, 5, 0)\cdot(-1, 5, 0) = 25$. h) La nouvelle requête est $(2, 8, 30)$, et $\lVert(2, 3, 30)\rVert^2 = 913$.

</details>

### Ex MB2.7 — Des mesures d'animaux en logarithme : la direction de taille estimée sur deux différences, la retirer de trois animaux, et les distances qui restent

<details><summary>Indice 1</summary>

Fiche §7 : « Projeter sur le complément d'une droite » (Pythagore, le centrage), « Estimer la direction : le premier axe de différences » (la matrice de Gram) et « Ce qui reste ».

</details>
<details><summary>Indice 2</summary>

$G_{ij} = \mathbf{d}_i\cdot\mathbf{d}_j$. Si $\mathbf{D}\mathbf{D}^\top\mathbf{w} = \lambda\mathbf{w}$, l'axe est dirigé par $\mathbf{D}^\top\mathbf{w}$, qu'on normalise. Retirer $\mathbf{u}$ : $\mathbf{x} - (\mathbf{x}\cdot\mathbf{u})\,\mathbf{u}$ pour $\mathbf{u}$ unitaire.

</details>
<details><summary>Indice 3</summary>

a) $4 + 16 + 9$ et $8 + 8 + 9$. b) $\begin{pmatrix} a & c \\ c & a \end{pmatrix}$ a pour valeurs propres $a \pm c$. c) $\mathbf{D}^\top(1, 1) = (6, 6, 6)$. d) Pour $\mathbf{u} = \frac{1}{\sqrt3}(1, 1, 1)$, $(\mathbf{x}\cdot\mathbf{u})\,\mathbf{u}$ est la moyenne des coordonnées de $\mathbf{x}$ fois $(1, 1, 1)$. e) $\mathbf{x}_1 - \mathbf{x}_3$, puis la différence des deux animaux corrigés. f) $(\mathbf{x}_1 - \mathbf{x}_3)\cdot\mathbf{u} = -\frac{3}{\sqrt3}$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB2.8 — La PMI est majorée par −ln p(x) et par −ln p(y), avec égalité quand x n'arrive qu'avec y ; la PMI normalisée est donc au plus 1

<details><summary>Indice 1</summary>

Fiche §2, « La borne des événements rares ». Il suffit de comparer $p(x, y)$ à $p(x)$ et à $p(y)$, et d'utiliser que $\ln$ est croissante.

</details>
<details><summary>Indice 2</summary>

$p(x) = \sum_{y'}p(x, y')$, une somme de termes positifs dont $p(x, y)$. Écris $\operatorname{PMI}(x, y) = \ln P(Y = y \mid X = x) - \ln p(y)$ pour 2. Pour 4, multiplie l'inégalité par $-\ln p(x, y) > 0$.

</details>
<details><summary>Indice 3</summary>

1. $\ln p(x, y) - \ln p(x) - \ln p(y) \le \ln p(x) - \ln p(x) - \ln p(y)$. 2. Égalité si et seulement si $\ln P(Y = y \mid X = x) = 0$. 3. $c \le \operatorname{PMI} \le -\ln p(y)$. 4. $\operatorname{NPMI} \le 1$ revient à $2\ln p(x, y) \le \ln p(x) + \ln p(y)$, la somme de deux inégalités de 1. Pour aller plus loin : $-\ln p(x) \ge 0$ et $-\ln p(y) \ge 0$ donnent $\operatorname{PMI} \ge \ln p(x, y)$ ; pour l'inégalité stricte, que faudrait-il pour l'égalité ?

</details>

### Ex MB2.9 — Répartir les valeurs singulières entre deux facteurs : le produit ne dépend pas de β, les produits scalaires des lignes si

<details><summary>Indice 1</summary>

Fiche §4, « Deux facteurs, un exposant ». Les puissances d'une matrice diagonale se prennent coefficient par coefficient ; le coefficient $(i, j)$ de $\mathbf{A}\mathbf{A}^\top$ est le produit scalaire des lignes $i$ et $j$ de $\mathbf{A}$.

</details>
<details><summary>Indice 2</summary>

1. $(\mathbf{V}_k\mathbf{S}_k^{1-\beta})^\top = \mathbf{S}_k^{1-\beta}\mathbf{V}_k^\top$. 2. $\mathbf{M}_k\mathbf{M}_k^\top$ se simplifie grâce à $\mathbf{V}_k^\top\mathbf{V}_k = \mathbf{I}_k$. 3. Si toutes les $s_i$ sont égales, $\mathbf{S}_k^\beta$ est un multiple de l'identité. 4. Le théorème spectral (M12c) écrit $\mathbf{M} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$, avec des valeurs propres positives ou nulles.

</details>
<details><summary>Indice 3</summary>

1. $\mathbf{S}_k^\beta\mathbf{S}_k^{1-\beta}$ a pour coefficients $s_i^\beta s_i^{1-\beta}$. 2. $\mathbf{U}_k\mathbf{S}_k\mathbf{V}_k^\top\mathbf{V}_k\mathbf{S}_k\mathbf{U}_k^\top$. 3. $\mathbf{A}_\beta = s^\beta\mathbf{U}_k$ ; pour l'exemple, reprends d) de MB2.4. 4. Garde les $r$ valeurs propres non nulles : $\mathbf{Q}_r\boldsymbol{\Lambda}_r\mathbf{Q}_r^\top$ a la forme d'une SVD compacte ; alors $\mathbf{A}_{1/2}$ et $\mathbf{B}_{1/2}$ valent tous deux $\mathbf{Q}_k\boldsymbol{\Lambda}_k^{1/2}$.

</details>

### Ex MB2.10 — Sous-échantillonner une classe : par la formule de Bayes, la cote observée est celle de la population multipliée par le rapport des taux de sélection s₁/s₀ ; dans un modèle logistique, seule l'ordonnée à l'origine bouge, de ln(s₁/s₀)

<details><summary>Indice 1</summary>

Fiche §5, « Sous-échantillonner une classe : l'étude cas-témoins » ; M04 pour la formule de Bayes, conditionnellement à $\mathbf{x}$.

</details>
<details><summary>Indice 2</summary>

$P(G \mid y = 1, \mathbf{x}) = s_1$ et $P(G \mid y = 0, \mathbf{x}) = s_0$. Écris $P(y = 1 \mid \mathbf{x}, G)$ et $P(y = 0 \mid \mathbf{x}, G)$ : ils ont le même dénominateur, $P(G \mid \mathbf{x})$, qui disparaît dans leur rapport.

</details>
<details><summary>Indice 3</summary>

1. $\frac{s_1\pi(\mathbf{x})}{s_1\pi(\mathbf{x}) + s_0(1 - \pi(\mathbf{x}))}$. 2. Le rapport vaut $\frac{s_1\pi}{s_0(1 - \pi)}$ ; prends le logarithme. 3. Remplace $\operatorname{logit}\pi(\mathbf{x})$ par $\theta_0 + \boldsymbol{\theta}^\top\mathbf{x}$, et regroupe les constantes. 4. $\ln\frac{a}{b}$ estime le logit de l'échantillon : retire $\ln\frac{s_1}{s_0}$. 5. Le décalage devient $\ln s_1 - \gamma_0 - \boldsymbol{\gamma}^\top\mathbf{x}$ : regroupe les termes en $\mathbf{x}$ avec $\boldsymbol{\theta}^\top\mathbf{x}$, et les constantes avec $\theta_0$. Si $\ln s_0(\mathbf{x})$ n'est pas affine, le logit de l'échantillon peut-il être affine en $\mathbf{x}$ ?

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex MB2.11 — Pont : résumer des séries de relevés de longueurs différentes par une moyenne masquée, montrer que le remplissage ne change rien, et compter les comparaisons par paires

<details><summary>Indice 1</summary>

Fiche §8 : « La moyenne masquée » et « Le coût des comparaisons par paires » ; R8 pour $\binom{n}{2}$.

</details>
<details><summary>Indice 2</summary>

$\frac{\sum_tm_t\mathbf{h}_t}{\sum_tm_t}$ : la somme des vrais relevés, divisée par leur nombre. Un modèle par paires fait $\binom{n}{2}$ passages, un modèle de résumé $n$.

</details>
<details><summary>Indice 3</summary>

a) $\frac13\big((12, 80) + (15, 71) + (18, 62)\big)$. b) $\frac12\big((9, 88) + (11, 84)\big)$. c) Les relevés ajoutés ont un masque 0. d) $\frac{300 \times 299}{2}$. e) $\binom{300}{2}/300$.

</details>

### Ex MB2.12 — Expliquer à un ornithologue ce que mesure la PMI d'un milieu et d'une espèce, et pourquoi une espèce vue une seule fois a la plus grande

<details><summary>Indice 1</summary>

Fiche §2 (la PMI comme logarithme du lift, la borne des événements rares, la PMI estimée sur peu d'observations) et §3 (le lissage) ; ta réponse à MB2.2 e) et la variante de MB2.2 dans `05_solutions.md`.

</details>
<details><summary>Indice 2</summary>

Parle de fréquences : la part des huppes parmi les oiseaux de la prairie, comparée à leur part parmi tous les oiseaux. Une espèce vue une seule fois a toutes ses observations dans un seul milieu.

</details>
<details><summary>Indice 3</summary>

Plan possible : ce que compare la PMI ; ce que disent son signe et une case vide ; pourquoi la huppe atteint la plus grande valeur possible pour la prairie ; ce que ferait une deuxième huppe vue ailleurs ; deux protections (le lissage, un nombre minimal d'observations) ; une conclusion prudente sur la huppe.

</details>

<a id="entretien"></a>

## 💼 Entretien

### MB2.E1 — « Pourquoi ne centre-t-on pas une grande table de comptages creuse avant de la factoriser par une SVD tronquée ? »

<details><summary>Indice 1</summary>

Fiche §4, « Ne pas centrer une grande table creuse », et l'encadré 💻 qui le suit.

</details>
<details><summary>Indice 2</summary>

Deux raisons : la mémoire (une table creuse devient pleine) et ce qu'on approche (la table, ou ses écarts aux moyennes). Puis : ce que porte le premier axe d'une SVD non centrée, et comment centrer sans écrire la table.

</details>
<details><summary>Indice 3</summary>

Chiffre un exemple : un nombre de lignes, de colonnes et une proportion de cases non nulles ; compare les nombres stockés avant et après. La table centrée s'écrit $\mathbf{M} - \mathbf{1}\bar{\mathbf{m}}^\top$, une table creuse moins une matrice de rang 1 ; une SVD itérative n'a besoin que de produits par des vecteurs.

</details>

<a id="notebook"></a>

## Notebook

### MB2.13 — La table des PMI d'une loi jointe, −∞ sur les cases vides : `pmi`

<details><summary>Indice 1</summary>

Fiche §2 ; la docstring de `pmi` et le commentaire `TODO` du squelette ; M20 pour la diffusion d'une colonne et d'une ligne.

</details>
<details><summary>Indice 2</summary>

`px = P.sum(axis=1, keepdims=True)` a la forme $(m, 1)$ et `py = P.sum(axis=0, keepdims=True)` la forme $(1, n)$ : `px * py` est la table des produits. Pour éviter l'avertissement de `np.log(0)`, ne calcule le logarithme que sur `mask = P > 0`.

</details>
<details><summary>Indice 3</summary>

`out = np.full(P.shape, -np.inf)`, puis `out[mask] = np.log(P[mask] / (px * py)[mask])`. Contrôle d'abord les booléens (`np.asarray(joint).dtype.kind == "b"`), la dimension, la taille, `np.isfinite`, le signe et la somme. Pour c), compare avec `np.allclose`, qui tient deux $-\infty$ pour égaux.

</details>

### MB2.14 — Deux briques : le logit d'une population estimé sur un échantillon cas-témoins, et retirer une direction des lignes d'une matrice : `case_control_logit`, `remove_direction`

<details><summary>Indice 1</summary>

Fiche §5 (« Sous-échantillonner une classe ») et §7 (« Projeter sur le complément d'une droite ») ; les docstrings et les commentaires `TODO` des deux fonctions.

</details>
<details><summary>Indice 2</summary>

`np.broadcast_arrays(n1, n0)` donne deux tableaux de même forme ; trois masques : les deux positifs, seul $n_1 > 0$, seul $n_0 > 0$, et une erreur si les deux sont nuls quelque part. Pour `remove_direction`, `X @ u / (u @ u)` donne les coefficients de toutes les lignes.

</details>
<details><summary>Indice 3</summary>

`out = np.where(n1 > 0, np.inf, -np.inf)`, puis, sur `both = (n1 > 0) & (n0 > 0)`, `np.log(n1[both] / n0[both]) - math.log(s1 / s0)` ; `float(out)` si `out.shape == ()`. Pour `remove_direction` : `X - np.multiply.outer(X @ u / (u @ u), u)`, qui marche pour un `X` 1-D comme 2-D. En c), la cote de la population est $e^{\text{logit}}$, et la probabilité $\frac{\text{cote}}{1 + \text{cote}}$.

</details>

### MB2.15 — Prédire puis mesurer la dispersion de la PMI estimée sur 400 observations, pour une case rare et une case fréquente, avec et sans lissage

<details><summary>Indice 1</summary>

Fiche §2, « Une PMI estimée sur peu d'observations », et §3, « Une constante par colonne » (ce que le lissage fait et ne fait pas).

</details>
<details><summary>Indice 2</summary>

a) Chaque oiseau est une huppe avec la probabilité 0,01 : la probabilité qu'aucun des 400 ne le soit est $0{,}99^{400}$, et $\ln 0{,}99 \approx -0{,}01$. b) Combien d'oiseaux de chaque case attend-on dans 400 ? Une proportion estimée sur $k$ oiseaux a une erreur relative de l'ordre de $1/\sqrt{k}$. Mais où sont vues toutes les huppes ? Écris l'estimation de $\operatorname{PMI}(\text{prairie}, \text{huppe})$ avec les comptes : qu'est-ce qui se simplifie ? c) Avec le lissage, $\hat p(\text{huppe})$ est remplacée par une marge où $n(\text{huppe})$ n'apparaît plus qu'à la puissance 1/3 : la simplification tient-elle encore ?

</details>
<details><summary>Indice 3</summary>

Pour (prairie, huppe) sans lissage, $\ln\frac{n(x, y)\,N}{n(x)\,n(y)}$ se simplifie : il ne reste que $\ln\frac{N}{n(\text{prairie})}$. Avec le lissage, $\hat p_\alpha(\text{huppe})$ ne contient plus que $n(\text{huppe})^{1/3}$ : la simplification disparaît. Dans `pmi_samples_15`, `counts = rng.multinomial(n_obs, P.ravel()).reshape(3, 4)`, puis `pmi(counts / n_obs)` et, pour le lissage, `temper(Ph.sum(axis=0), 3)` ; garde les cases dans l'ordre de l'énoncé.

</details>

### MB2.16 — Des magasins dans le plan des deux facteurs U₂S₂^β, pour β = 0, ½ et 1 : ce qui s'étire, et les angles qui changent

<details><summary>Indice 1</summary>

Fiche §4, « Deux facteurs, un exposant » et sa figure ; M12d pour `svd` et `low_rank_approximation`.

</details>
<details><summary>Indice 2</summary>

`U, s, Vt = mymath.svd_pca.svd(M)` ; les deux premières colonnes de `U`, multipliées par `s[:2] ** beta`. Pour le dessin : `ax.scatter`, `ax.annotate(nom, (x, y))`, `ax.set_aspect("equal")` et `ax.set_xlabel`.

</details>
<details><summary>Indice 3</summary>

`factor_rows_16` : `U[:, :k] * s[:k] ** beta`. d) Le rapport des longueurs des colonnes vaut $(s_1/s_2)^\beta$ : vérifie-le. e) et f) Compare les cosinus des lignes de `factor_rows_16(M, 1)` à ceux des lignes de `low_rank_approximation(M, 2)`, puis de `M`, pour toutes les paires, avec une tolérance de $10^{-9}$.

</details>

### MB2.17 — Chasse à l'erreur : une PMI calculée sans le total, des facteurs U S^β et V S^β, une direction retirée sans diviser par u·u

<details><summary>Indice 1</summary>

Fiche §2, §4 et §7 : chaque ⚠️ « Erreur classique » renvoie à ce 🐛.

</details>
<details><summary>Indice 2</summary>

Pour chaque fonction, demande-toi ce que la vérification du collègue avait de particulier : une table de somme 1, $\beta = \frac12$, un $\mathbf{u}$ de norme 1.

</details>
<details><summary>Indice 3</summary>

(1) $\frac{n(x, y)}{n(x)\,n(y)} = \frac{p(x, y)}{p(x)\,p(y)}\cdot\frac1N$ : il manque $\ln N$. (2) $\mathbf{S}^\beta\mathbf{S}^\beta = \mathbf{S}^{2\beta}$, égal à $\mathbf{S}$ seulement pour $\beta = \frac12$. (3) $(\mathbf{x}\cdot\mathbf{u})\,\mathbf{u}$ n'est la projection que si $\mathbf{u}\cdot\mathbf{u} = 1$.

</details>

### MB2.18 — Un test de propriété de `pmi` sur des tables tirées au hasard : la borne, la transposition, et la moyenne qui redonne l'information mutuelle de M06

<details><summary>Indice 1</summary>

Fiche §2 (la borne et l'information mutuelle) ; ∂ MB2.8 ; M06 pour `mutual_information(P, base=math.e)`.

</details>
<details><summary>Indice 2</summary>

Calcule la borne de toutes les cases d'un coup : `np.minimum(-np.log(px)[:, None], -np.log(py)[None, :])`, puis ne regarde que les cases de `P > 0`. Pour la transposition, compare d'abord les places des $-\infty$ (`np.isneginf`), puis le reste avec `np.allclose`. Entoure les appels de `func` d'un `try`.

</details>
<details><summary>Indice 3</summary>

Une colonne ou une ligne vide donne `-np.log(0) = inf` dans la borne : ce n'est pas gênant, puisque ses cases ont $P = 0$ et ne sont pas regardées (mets `np.errstate(divide="ignore")`). Pour c), demande-toi quelles cases chaque contrôle regarde, et ce qu'il ne regarde jamais : les cases vides, l'échelle de la table, sa symétrie.

</details>

### MB2.19 — Défi : retrouver, sur 3 000 observations, les cinq paires les plus associées d'une table cachée de 10 × 10, sans se laisser piéger par les cases rares

<details><summary>Indice 1</summary>

Fiche §2 (« La borne des événements rares » et « Une PMI estimée sur peu d'observations ») et §3 ; M04 pour les pseudo-comptes.

</details>
<details><summary>Indice 2</summary>

Regarde les cinq cases que choisit l'estimation directe : leurs comptes, et les sommes de leurs lignes et de leurs colonnes. Une case de 2 ou 3 ventes dans un rayon rare atteint une grande PMI estimée par hasard.

</details>
<details><summary>Indice 3</summary>

Deux pistes : n'accepter que les cases d'au moins une dizaine de ventes ; ou rapprocher chaque case de l'indépendance, $\ln\frac{n(x, y) + \kappa}{e(x, y) + \kappa}$, avec $e(x, y) = \frac{n(x)\,n(y)}{N}$ le compte qu'on aurait à l'indépendance et $\kappa$ de l'ordre de quelques unités. Essaie ta méthode sur des tables que tu tires toi-même, avec des lignes et des colonnes rares.

</details>
