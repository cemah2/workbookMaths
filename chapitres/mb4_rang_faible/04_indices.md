# MB4 · Rang faible et recherche d'information — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB4.Q1 — Rang, factorisation et stockage : vrai ou faux, et le rang d'une somme de produits extérieurs

<details><summary>Indice 1</summary>

Fiche §1 : « La factorisation CR », « Une factorisation par matrice inversible », « Une somme de produits extérieurs » et « Ce qu'elle coûte, et ses nombres libres » ; §2 : « Le rang effectif et le rang stable ».

</details>
<details><summary>Indice 2</summary>

Toute matrice de rang $r$ est un produit $(m, r) \times (r, n)$, et deux tels produits diffèrent d'une $\mathbf{G}$ inversible. $\mathbf{u}_1\mathbf{e}_1^\top + \mathbf{u}_2\mathbf{e}_2^\top + \mathbf{u}_3\mathbf{e}_3^\top$ est la matrice dont les colonnes sont les $\mathbf{u}_i$. $r(m + n)$ nombres stockés, $r(m + n - r)$ libres (cas général : pivots dans les $r$ premières colonnes). Le rang stable est $\frac{\sum_is_i^2}{s_1^2}$.

</details>
<details><summary>Indice 3</summary>

2. Essaie $\mathbf{C}' = 2\mathbf{C}$ et $\mathbf{F}' = \frac12\mathbf{F}$. 3. Combien de ces trois colonnes sont libres ? 4. $2 \times (40 + 150)$, puis retire $r^2$. 5. Le rang compte les $s_i$ non nuls, et chacun vaut au plus $s_1$.

</details>

### MB4.Q2 — Le poids d'un ingrédient rare, la saturation et la normalisation : signe, sens de variation, limites

<details><summary>Indice 1</summary>

Fiche §3 : « La correction ½ » et « Sans information de pertinence » ; §4 : « La saturation » et « La normalisation par la longueur ».

</details>
<details><summary>Indice 2</summary>

Le poids $\ln\frac{N - n + 1/2}{n + 1/2}$ est négatif quand son argument est plus petit que 1. Pour les limites de $s$, divise numérateur et dénominateur par $x$, ou regarde ce que deviennent $k_1 + 1$ et $x + k_1$.

</details>
<details><summary>Indice 3</summary>

2. Pour $n = N$, l'argument vaut $\frac{1/2}{N + 1/2}$ ; la variante, $\frac{N + 1}{N + 1/2}$. 3. $\ln 0$ et une division par 0. 4. $s(1) = \frac{k_1 + 1}{1 + k_1}$ ; dérive deux fois $\frac{x(k_1 + 1)}{x + k_1} = (k_1 + 1)\big(1 - \frac{k_1}{x + k_1}\big)$. 5. $\frac{x(0 + 1)}{x + 0}$, et, pour $k_1$ grand, $\frac{k_1 + 1}{x + k_1} \to 1$ ; pour $b = 0$, remplace $b$ dans $1 - b + b\ell$.

</details>

### MB4.Q3 — Fusionner des classements : ce que change une nouvelle échelle de notes, ce que change la constante c

<details><summary>Indice 1</summary>

Fiche §5 : « Additionner des notes : une question d'échelle », « Fusionner par les rangs » et « La somme des 1/(c + rang) ».

</details>
<details><summary>Indice 2</summary>

Une transformation strictement croissante des notes d'un juge garde son classement, donc ses rangs ; une fusion par les rangs ne voit que les rangs. La contribution du rang $j$ est $\frac{1}{c + j}$.

</details>
<details><summary>Indice 3</summary>

1. et 2. Diviser par 2 et prendre la racine carrée gardent l'ordre de nombres positifs. 3. Calcule $\frac{1/(c + 5)}{1/(c + 1)} = \frac{c + 1}{c + 5}$ pour $c = 2$, puis pour $c = 10$. 4. Fiche, propriété 2 de « La somme des 1/(c + rang) ». 5. Deux notes 15 et 14, ou 15 et 5 : quels rangs ?

</details>

### MB4.Q4 — recall@k, precision@k, taux de succès et MRR : définitions, et leurs valeurs pour un ordre tiré au hasard

<details><summary>Indice 1</summary>

Fiche §6 : « Quatre mesures », « La ligne de base d'un ordre tiré au hasard » et « Un seul pertinent : H_n/n ».

</details>
<details><summary>Indice 2</summary>

recall@k divise le nombre de pertinents vus par $q$, precision@k par $k$ ; le succès@k vaut 1 dès qu'un pertinent est parmi les $k$ premiers, 0 sinon. Au hasard, $\mathbb{E}[\text{recall@k}] = \frac kn$, $\mathbb{E}[\text{precision@k}] = \frac qn$, $P(R = j) = \binom{n - j}{q - 1}\big/\binom nq$, et $\mathbb{E}[\frac1R] = \frac{H_n}{n}$ pour un seul pertinent.

</details>
<details><summary>Indice 3</summary>

1. Parmi les 4 premiers, un seul bon diagnostic (celui du rang 3), qui est aussi parmi les 3 premiers. 3. $R$ prend les valeurs 1, 2, 3 avec la même probabilité. 4. $\binom62 = 15$, et $\binom{6 - j}{1} = 6 - j$. 5. Le MRR vaut $\frac{H_{40}}{40}$ : divise par 40 chaque borne de $H_{40}$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### MB4.R1 — Le rang d'un produit, d'un produit extérieur et d'une somme (M12a)

<details><summary>Indice 1</summary>

M12a §4, « Le rang d'un produit » ; fiche §1, « Une somme de produits extérieurs ».

</details>
<details><summary>Indice 2</summary>

Toutes les colonnes de $\mathbf{u}\mathbf{v}^\top$ sont des multiples de $\mathbf{u}$. $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{B})$, et ce n'est qu'une borne.

</details>
<details><summary>Indice 3</summary>

3. Mets $\mathbf{u}_1$ en facteur : $\mathbf{u}_1\mathbf{v}_1^\top + 3\mathbf{u}_1\mathbf{v}_2^\top = \mathbf{u}_1(\ldots)^\top$. 4. Cherche deux matrices non nulles de produit nul. 5. Montre les deux inclusions des espaces des colonnes, la seconde avec $\mathbf{S}^{-1}$.

</details>

### MB4.R2 — L'approximation de rang k par la SVD et son erreur de Frobenius (M12d, MML §4.6)

<details><summary>Indice 1</summary>

M12d §3, « L'approximation de rang faible » ; fiche §2, le rappel de « Mesurée, une matrice a le rang plein » ; MML §4.6 (l'approximation de rang $k$ et le théorème d'Eckart-Young).

</details>
<details><summary>Indice 2</summary>

$\lVert\mathbf{M}\rVert_F^2 = \sum_is_i^2$ ; l'erreur de $\mathbf{M} _k$ vaut $\sqrt{\sum  _{i > k}s_i^2}$ en norme de Frobenius, et $s _{k+1}$ en norme spectrale.

</details>
<details><summary>Indice 3</summary>

1. $49 + 16 + 1$. 2. $\sqrt{16 + 1}$. 4. $\frac{49 + 16}{66}$. 5. Une somme de $k$ termes $s_i\mathbf{u}_i\mathbf{v}_i^\top$.

</details>

### MB4.R3 — L'information −ln p d'un événement, la cote et le logit (M06, R6)

<details><summary>Indice 1</summary>

M06 §1 (l'information d'un événement) ; R6 §7, « La cote, le logit : remonter de la probabilité au score ».

</details>
<details><summary>Indice 2</summary>

$-\ln p$ en nats, $-\log_2p = \frac{-\ln p}{\ln 2}$ en bits ; la cote $\frac{p}{1 - p}$ ; le logit est le logarithme de la cote, et sa réciproque est la sigmoïde.

</details>
<details><summary>Indice 3</summary>

1. $-\ln 0{,}04 = \ln 25$. 2. $\frac{0{,}2}{0{,}8}$. 4. Une cote de 3 : $\frac{p}{1 - p} = 3$. 5. La cote de $1 - p$ est l'inverse de celle de $p$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB4.1 — Les ventes de quatre boulangeries sur cinq produits : le rang, la factorisation par les colonnes pivots, une seconde factorisation (CG)(G⁻¹F), et les nombres stockés ou libres

<details><summary>Indice 1</summary>

Fiche §1 : « La factorisation CR » (l'exemple des alliages), « Une factorisation par matrice inversible » et « Ce qu'elle coûte, et ses nombres libres ».

</details>
<details><summary>Indice 2</summary>

Les deux premières colonnes ne sont pas proportionnelles. Écris chaque autre colonne comme $\alpha\thinspace(\text{baguettes}) + \beta\thinspace(\text{croissants})$ : deux lignes du tableau donnent un système $2 \times 2$, les deux autres servent de vérification. La colonne $j$ de $\mathbf{F}$ est $(\alpha, \beta)$ pour la colonne $j$ de $\mathbf{M}$.

</details>
<details><summary>Indice 3</summary>

Pour les pains de campagne, les lignes Halles et Moulin donnent $12\alpha + 4\beta = 10$ et $16\alpha + 2\beta = 10$, d'où $(\alpha, \beta) = (\frac12, 1)$ ; fais de même pour les deux dernières colonnes. c) La colonne $j$ de $\mathbf{C}\mathbf{G}$ est $\mathbf{C}$ fois la colonne $j$ de $\mathbf{G}$. d) $`\mathbf{G}^{-1} = \frac{1}{2}\begin{pmatrix} 2 & -1 \cr 0 & 1 \end{pmatrix}`$. f) Retire $r^2$ à e).

</details>

### Ex MB4.2 — Un tableau de relevés de stations météo donné par ses valeurs singulières : énergie captée, rang effectif à 99 %, rang stable, puis le coût de C(Fx) et de (CF)x pour un et pour mille vecteurs

<details><summary>Indice 1</summary>

Fiche §2 : « Le rang effectif et le rang stable » (l'exemple du laboratoire) et « L'ordre des produits » ; M20 §3 pour l'ordre des contractions et `np.linalg.multi_dot`.

</details>
<details><summary>Indice 2</summary>

Additionne les carrés des 60 valeurs singulières ; les parts cumulées $\frac{s_1^2 + \cdots + s_r^2}{\lVert\mathbf{M}\rVert_F^2}$ croissent avec $r$ ; l'erreur de $\mathbf{M}_r$ est la racine de la somme des carrés oubliés. Un produit $(m, n) \times (n, p)$ coûte $mnp$ multiplications.

</details>
<details><summary>Indice 3</summary>

a) $320^2 + 150^2 + 60^2 + 15^2 + 56 \times 9$. c) Compare les parts pour $r = 2$ et $r = 3$ à 0,99. d) $15^2 + 56 \times 9 = 729$. f) $\mathbf{F}\mathbf{x}$ coûte $3 \times 450$, puis $\mathbf{C}(\mathbf{F}\mathbf{x})$ coûte $60 \times 3$. g) $60 \times 3 \times 450$ pour $\mathbf{C}\mathbf{F}$, puis $60 \times 450$. h) Multiplie par mille ce qui se refait pour chaque vecteur, et seulement cela.

</details>

### Ex MB4.3 — Les ingrédients d'un carnet de recettes : surprise, cote, poids corrigé par ½ et son signe, la variante toujours positive, puis la saturation et la normalisation d'une mention répétée

<details><summary>Indice 1</summary>

Fiche §3 : « La surprise et la cote » et « Sans information de pertinence » (l'exemple de la boiterie et de la fatigue) ; §4 : « La saturation » et « La normalisation par la longueur ».

</details>
<details><summary>Indice 2</summary>

Surprise $-\ln\frac nN$, cote $\frac{n}{N - n}$, poids corrigé $\ln\frac{N - n + 1/2}{n + 1/2}$, variante $\ln\frac{N + 1}{n + 1/2}$. Avec $k_1 = 2$, $s(x) = \frac{3x}{x + 2}$ ; la saturation normalisée remplace $k_1$ par $k_1\nu$ au dénominateur, avec $\nu = 1 - b + 2b$.

</details>
<details><summary>Indice 3</summary>

a) $\ln\frac{80}{4}$. c) $\frac{80 - 4 + 0{,}5}{4 + 0{,}5} = \frac{76{,}5}{4{,}5}$, un entier. e) L'argument est plus petit que 1 quand $80 - n + \frac12 < n + \frac12$ ; un poids nul n'est pas négatif. h) Calcule $s(9)$ et $s(10)$ en fractions. i) $\nu = \frac54$, puis $\frac32$ ; la valeur est $\frac{3 \times 3}{3 + 2\nu}$.

</details>

### Ex MB4.4 — Trois jurys classent cinq pâtissiers : les points de Borda, la somme des 1/(c + rang) pour c = 2 et c = 10, et la somme des notes qui change de gagnant quand un jury passe de 20 à 100 points

<details><summary>Indice 1</summary>

Fiche §5 : « Additionner des notes : une question d'échelle », « Fusionner par les rangs » et « La somme des 1/(c + rang) » (l'exemple du concours photo).

</details>
<details><summary>Indice 2</summary>

Écris d'abord, pour chaque jury, le classement, puis les rangs de chaque pâtissier. Le rang $j$ rapporte $5 - j$ points de Borda et $\frac{1}{c + j}$ à la somme ; additionne sur les trois jurys.

</details>
<details><summary>Indice 3</summary>

Les rangs de A sont $(1, 1, 5)$ et ceux de B $(2, 2, 2)$ : A a $4 + 4 + 0 = 8$ points de Borda, et, pour $c = 2$, $\frac13 + \frac13 + \frac17$. Fais de même pour C, D et E. e) Multiplie par 5 la seule ligne de la presse. f) Résous $\frac{2}{c + 1} + \frac{1}{c + 5} = \frac{3}{c + 2}$ en multipliant par les trois dénominateurs.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB4.5 — Une matrice de rang r est un produit C F de r colonnes par r lignes ; deux telles factorisations diffèrent d'une matrice inversible ; le rang est le plus petit nombre de produits extérieurs dont elle est la somme

<details><summary>Indice 1</summary>

Fiche §1 : le théorème de « Une somme de produits extérieurs », et les outils qu'il nomme ; M12a §3 (coordonnées dans une base) et §4 (le rang d'un produit).

</details>
<details><summary>Indice 2</summary>

1. Les coordonnées de chaque colonne dans la base $\mathbf{c}_1, \ldots, \mathbf{c}_r$ forment une colonne de $\mathbf{F}$. 2. L'espace des colonnes de $\mathbf{C}'\mathbf{F}'$ est inclus dans celui de $\mathbf{C}'$ ; compare les dimensions. 3. Écris une somme de $p$ produits extérieurs comme un produit de deux matrices à $p$ colonnes.

</details>
<details><summary>Indice 3</summary>

1. Pour le rang de $\mathbf{F}$ : $r = \operatorname{rg}(\mathbf{C}\mathbf{F}) \le \operatorname{rg}\mathbf{F}$, et $\mathbf{F}$ a $r$ lignes. 2. Chaque colonne de $\mathbf{C}'$ est dans l'espace des colonnes de $\mathbf{M}$, donc s'écrit $\mathbf{C}\mathbf{g}_k$ comme à la question 1 ; pour $\mathbf{G}$ inversible, utilise $\operatorname{rg}\mathbf{C}' \le \operatorname{rg}\mathbf{G}$ ; pour $\mathbf{F}'$, écris $\mathbf{C}(\mathbf{F} - \mathbf{G}\mathbf{F}') = \mathbf{0}$, et sers-toi des colonnes libres de $\mathbf{C}$. 3. $\sum_i\mathbf{u}_i\mathbf{v}_i^\top = \mathbf{U}\mathbf{V}^\top$.

</details>

### Ex MB4.6 — Une fusion par les rangs ne change pas quand un jury change d'échelle ; j-ième pour deux jurys bat premier pour un seul si et seulement si j < c + 2 ; quand c grandit, la somme des 1/(c + rang) range selon le nombre de listes, puis la somme des rangs

<details><summary>Indice 1</summary>

Fiche §5 : « Fusionner par les rangs » et les propriétés de « La somme des 1/(c + rang) », avec les outils qu'elles nomment ; M05a (le développement de $\frac{1}{1 + u}$).

</details>
<details><summary>Indice 2</summary>

1. Le rang d'un candidat est 1 plus le nombre de candidats mieux notés. 2. Compare $\frac{2}{c + j}$ et $\frac{1}{c + 1}$. 3. Réduis $\frac1c - \frac{j}{c^2} + \frac{j^2}{c^2(c + j)}$ au même dénominateur, puis compare deux candidats selon l'ordre de grandeur des termes en $\frac1c$ et en $\frac{1}{c^2}$.

</details>
<details><summary>Indice 3</summary>

1. Pour l'exemple, X noté $(a, b)$ et Y noté $(a', b')$, avec $a > a'$ et $b < b'$ ; multiplie les notes du jury 2 par $\lambda$. 2. Les dénominateurs sont positifs : $2(c + 1) > c + j$. Pour $c = 0$, quel $j \ge 2$ vérifie $j < 2$ ? 3. Le reste est positif et au plus $\frac{j^2}{c^3}$ par liste ; si $L > L'$, la différence est au moins $\frac1c$ moins des termes en $\frac{1}{c^2}$ ; si $L = L'$ et $S < S'$, elle est au moins $\frac{1}{c^2}$ moins un terme en $\frac{1}{c^3}$.

</details>

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB4.7 — Expliquer à un pâtissier pourquoi un ingrédient présent dans toutes les recettes n'aide pas à retrouver la sienne, et pourquoi la dixième mention compte moins que la première

<details><summary>Indice 1</summary>

Fiche §3 (la surprise, et le poids qui s'annule à la moitié des fiches) et §4 (la saturation : des rendements décroissants, la longueur).

</details>
<details><summary>Indice 2</summary>

Un indice utile **sépare** les fiches ; une mention de plus n'apprend que ce que les précédentes n'ont pas dit. Pour le logarithme, pense à deux indices indépendants : leurs probabilités se multiplient.

</details>
<details><summary>Indice 3</summary>

Plan : ce que dit un ingrédient partout ; ce que dit un ingrédient rare, et la surprise ; pourquoi un logarithme (des surprises qui s'ajoutent) ; la première mention contre la dixième, une prime qui plafonne ; la longueur de la fiche.

</details>

<a id="entretien"></a>

## 💼 Entretien

### MB4.E1 — « Comment combiner les classements de deux systèmes dont les scores ne sont pas sur la même échelle ? »

<details><summary>Indice 1</summary>

Fiche §5 : « Additionner des notes : une question d'échelle », « Fusionner par les rangs », « La somme des 1/(c + rang) » et le paragraphe « Deux systèmes, deux échelles ».

</details>
<details><summary>Indice 2</summary>

Trois familles : additionner (des scores bruts ou normalisés), fusionner les rangs, apprendre la combinaison. Pour chacune, dis ce qu'elle suppose et ce qu'elle perd.

</details>
<details><summary>Indice 3</summary>

Plan : le problème des échelles ; la normalisation et sa fragilité ; Borda et la somme des $\frac{1}{c + \text{rang}}$, invariantes par une transformation croissante ; le rôle de $c$ ; ce qu'on perd (les écarts) ; une méthode apprise, validée sur des données à part.

</details>

<a id="notebook"></a>

## Notebook

### MB4.8 — La factorisation de rang C F : les colonnes pivots de M et les lignes non nulles de sa forme échelonnée réduite : `rank_factorization`

<details><summary>Indice 1</summary>

Fiche §1, « La factorisation CR », et la docstring de `rank_factorization` dans ta copie de `ranks.py` ; ton `rref` de M09a, avec une petite tolérance `tol` sur les pivots (le 💻 du §1).

</details>
<details><summary>Indice 2</summary>

Contrôle `M` (2-D, non vide, finie) et `tol` (refuse `bool` avant de tester le type). Réduis une copie en flottants : `R, pivots = rref(M, tol)` si tu importes `rref` de `.matrices` ; sinon recopie-le. Puis $\mathbf{C}$ = les colonnes `pivots` de $\mathbf{M}$, $\mathbf{F}$ = les `len(pivots)` premières lignes de `R`.

</details>
<details><summary>Indice 3</summary>

`A = np.array(M, dtype=float)` (une copie) ; `C = A[:, list(pivots)]` et `F = R[:len(pivots)]` ; pour une matrice nulle, `pivots` est vide, et les formes $(m, 0)$ et $(0, n)$ viennent seules. b) Appelle `rank_factorization(M_8, tol=...)` et lis `C.shape[1]`. c) `np.max(np.abs(C @ F - M_8))`.

</details>

### MB4.9 — Les points de Borda de classements complets, et le MRR exact d'un ordre tiré au hasard, en fractions : `borda_scores`, `random_ranking_mrr`

<details><summary>Indice 1</summary>

Fiche §5, « Fusionner par les rangs » (la définition de Borda), §6, « La ligne de base d'un ordre tiré au hasard » (la loi de $R$), et les docstrings des deux fonctions.

</details>
<details><summary>Indice 2</summary>

Une ligne est un ordre : le candidat `row[p]` est à la position $p$ (à partir de 0), donc au rang $p + 1$, et reçoit $n - 1 - p$ points. Pour une permutation, chaque valeur de $0, \ldots, n - 1$ apparaît une fois : compare la ligne triée à `range(n)`, ou compte. Pour le MRR, $P(R = j) = \binom{n - j}{q - 1}\big/\binom nq$.

</details>
<details><summary>Indice 3</summary>

`points = np.zeros(n, dtype=int)`, puis `for row in R: for p, cand in enumerate(row): points[cand] += n - 1 - p`. Pour le MRR : `last = n - q + 1`, ou `min(last, depth)`, puis `sum(Fraction(math.comb(n - j, q - 1), math.comb(n, q)) / j for j in range(1, last + 1))`. d) `Fraction(sum(Fraction(1, k) for k in range(1, n + 1)), n)`.

</details>

### MB4.10 — Prédire le MRR d'un ordre tiré au hasard parmi 10, 100 puis 1 000 candidats, puis le simuler et le comparer à H_n/n

<details><summary>Indice 1</summary>

Fiche §6, « Un seul pertinent : H_n/n », et l'encadrement de $H_n$ par des rectangles.

</details>
<details><summary>Indice 2</summary>

Le MRR d'un ordre au hasard vaut $\frac{H_n}{n}$, et $H_n$ est entre $\ln(n + 1)$ et $1 + \ln n$. Pour a), calcule ces deux bornes pour $n = 10$, puis divise par 10. Pour b) et c), compare $\ln 100$ et $\ln 1\thinspace000$ : de combien $H_n$ grandit-il quand $n$ est multiplié par 10 ?

</details>
<details><summary>Indice 3</summary>

a) $\frac{\ln 11}{10} \approx 0{,}24$ et $\frac{1 + \ln 10}{10} \approx 0{,}33$ : laquelle des trois valeurs proposées tombe entre les deux ? b) $\frac{H_{100}/100}{H_{1\thinspace000}/1\thinspace000} = 10 \times \frac{H_{100}}{H_{1\thinspace000}}$, et l'encadrement de la fiche donne $\frac{\ln 101}{1 + \ln 1\thinspace000} \le \frac{H_{100}}{H_{1\thinspace000}} \le \frac{1 + \ln 100}{\ln 1\thinspace001}$. c) $n \times \text{MRR} = H_n$ : de combien $H_n$ augmente-t-il chaque fois que $n$ est multiplié par 10, et combien de fois $n$ l'est-il de 10 à 1 000 ? Pour la simulation : une liste des 20 000 valeurs de $\frac1R$ par $n$, sa moyenne, et l'erreur type `np.std(v, ddof=1) / np.sqrt(len(v))`.

</details>

### MB4.11 — Les courbes de saturation x ↦ x(k₁ + 1)/(x + k₁) de k₁ = 0 à l'infini, et ce que la normalisation par la longueur leur fait

<details><summary>Indice 1</summary>

Fiche §4, « La saturation » (ses quatre propriétés et sa figure) et « La normalisation par la longueur ».

</details>
<details><summary>Indice 2</summary>

Traite à part $k_1 = 0$ (`(x > 0).astype(float)`) et $k_1$ infini (`math.isinf(k1)` : rends `x`). Pour un tracé, `x = np.linspace(0, xmax, 241)`, une courbe par valeur, `ax.legend()`, `ax.set_xlabel(...)`, `ax.set_ylabel(...)`. b) Résous $s(x) = 0{,}9(k_1 + 1)$.

</details>
<details><summary>Indice 3</summary>

`np.asarray(x, dtype=float) * (k1 + 1) / (x + k1)` ; pour la longueur, `nu = 1 - b + b * ell`, puis `x * (k1 + 1) / (x + k1 * nu)`. b) $x(k_1 + 1) = 0{,}9(k_1 + 1)(x + k_1)$ donne $0{,}1x = 0{,}9k_1$. c) Pour $k_1 = 1$ et $b = \frac12$, $\nu$ vaut $\frac34$, 1 et $\frac32$. d) La limite en $+\infty$ de $\frac{x(k_1 + 1)}{x + k_1\nu}$ dépend-elle de $\nu$ ?

</details>

### MB4.12 — Chasse à l'erreur : C pris dans la forme réduite au lieu de M, un classement lu comme la liste des rangs des candidats, un poids de rareté écrit ln(n/N)

<details><summary>Indice 1</summary>

Les ⚠️ de la fiche : §1 (« Prendre $\mathbf{C}$ dans la forme réduite »), §3 (« Écrire la surprise $\ln\frac nN$ au lieu de $-\ln\frac nN$ ») et §5 (« Lire un classement comme la liste des rangs »).

</details>
<details><summary>Indice 2</summary>

Pour chaque fonction, cherche une entrée où l'erreur ne change rien : une matrice égale à sa forme réduite, un classement égal à son inverse, un ingrédient présent partout. C'est là qu'était la vérification du collègue.

</details>
<details><summary>Indice 3</summary>

(1) `C = np.asarray(M, dtype=float)[:, list(pivots)]`. (2) `for p, cand in enumerate(row): points[cand] += n - 1 - p`. (3) `-math.log(n / N)`. Pour la vérification du collègue, la ligne `[1, 0, 3, 2]` : que dit-elle lue comme un ordre, puis comme une liste de rangs ?

</details>

### MB4.13 — Défi : retrouver le rang caché de cinq tableaux bruités, cinq fois sur cinq, par leurs valeurs singulières

<details><summary>Indice 1</summary>

Fiche §2 : « Mesurée, une matrice a le rang plein », « Où couper : chercher un écart » et son encadré 💻 (le niveau $\sigma(\sqrt m + \sqrt n)$ d'un bruit de moyenne nulle et d'écart-type $\sigma$).

</details>
<details><summary>Indice 2</summary>

Ni un seuil fixe sur les valeurs singulières ni une part d'énergie ne suivent un bruit dont l'échelle change d'un tableau à l'autre : il faut un seuil proportionnel à $\sigma$. Une fois un rang $r$ choisi, les valeurs singulières qu'il laisse de côté viennent presque toutes du bruit, et leur énergie vaut environ $\sigma^2$ par case qui reste.

</details>
<details><summary>Indice 3</summary>

Pars de $r = 0$. Estime $\hat\sigma^2 = \frac{\sum_{i > r}s_i^2}{(m - r)(n - r)}$, compte les $s_i$ au-dessus de $\tau\thinspace\hat\sigma(\sqrt m + \sqrt n)$, et recommence avec ce nouveau $r$ jusqu'à ce qu'il ne change plus. Prends une marge $\tau$ un peu au-dessus de 1 : le bruit seul dépasse parfois légèrement $\sigma(\sqrt m + \sqrt n)$, mais un signal faible reste nettement au-dessus. Essaie ta fonction sur des tableaux que tu fabriques toi-même (un rang connu, un bruit d'écart-type choisi), dont un sans signal.

</details>
