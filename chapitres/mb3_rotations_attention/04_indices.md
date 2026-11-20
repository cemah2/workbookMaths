# MB3 · Rotations, moyennes pondérées et softmax en ligne — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB3.Q1 — Formules d'addition et rotations du plan : le bon signe, composer, inverser, rotation ou symétrie ?

<details><summary>Indice 1</summary>

Fiche §1 : « Les trois autres, et ce qu'on en tire » ; §2 : « Composer, inverser » et « Rotation ou symétrie ».

</details>
<details><summary>Indice 2</summary>

Un moins dans $\cos(a + b)$, un plus dans $\cos(a - b)$ ; le sinus garde le signe de l'opération. $\mathbf{R}_\alpha\mathbf{R}_\beta = \mathbf{R}_{\alpha + \beta}$ et $\mathbf{R}_\theta^{-1} = \mathbf{R}_\theta^\top = \mathbf{R}_{-\theta}$. Une matrice orthogonale $2 \times 2$ est une rotation si son déterminant vaut 1, une symétrie s'il vaut $-1$.

</details>
<details><summary>Indice 3</summary>

2. Mets $\frac{2\pi}{9}$ et $\frac{5\pi}{18}$ au même dénominateur. 3. Deux angles qui diffèrent de $2\pi$ donnent la même matrice. 4. Calcule $\frac{9 \times 9 \pm 40 \times 40}{1\,681}$ ; l'axe de la symétrie est la droite d'angle $\frac\theta2$, où $\cos\theta = \frac{9}{41}$ : essaie le vecteur $(1 + \cos\theta, \sin\theta)$, proportionnel à $(50, 40)$.

</details>

### MB3.Q2 — Rotations de l'espace, de Givens et par blocs : commutent-elles, que fixent-elles, que change une permutation des coordonnées ?

<details><summary>Indice 1</summary>

Fiche §3 : « Quand deux rotations commutent », « Les matrices diagonales par blocs » et « Renuméroter les coordonnées ».

</details>
<details><summary>Indice 2</summary>

Même plan ou plans disjoints : elles commutent ; plans qui partagent une coordonnée : pas en général. $\mathbf{R}_{ij}(\theta)$ ne change que les coordonnées $i$ et $j$. Le déterminant et l'inverse d'une matrice diagonale par blocs se calculent bloc par bloc. $\mathbf{P}^\top\mathbf{R}_{ij}(\theta)\mathbf{P}$ tourne le plan $(\sigma(i), \sigma(j))$.

</details>
<details><summary>Indice 3</summary>

1. Les rotations autour de $\mathbf{e}_1$ et de $\mathbf{e}_3$ sont $\mathbf{R}_{23}$ et $\mathbf{R}_{12}$ : quelle coordonnée partagent-elles ? 3. Quelles coordonnées $\mathbf{R}_{24}(\theta)$ ne touche-t-elle pas ? 5. Ici $\sigma(1) = 1$ et $\sigma(2) = 3$.

</details>

### MB3.Q3 — Encoder une direction ou un jour de l'année : une ou deux coordonnées, quelle période, quelle distance entre deux encodages ?

<details><summary>Indice 1</summary>

Fiche §4 : « Décembre et janvier » et « Un décalage est une rotation ».

</details>
<details><summary>Indice 2</summary>

$\lVert\mathbf{e}(t) - \mathbf{e}(t')\rVert^2 = 2 - 2\cos\omega(t - t')$, avec $\omega = \frac{2\pi}{\tau}$. Le cosinus est pair : $\cos(\omega t) = \cos(\omega(\tau - t))$.

</details>
<details><summary>Indice 3</summary>

1. Compare $\cos\frac{2\pi \times 100}{365}$ et $\cos\frac{2\pi \times 265}{365}$. 2. L'écart vaut 4 h dans les deux cas : $\omega \times 4 = \frac\pi3$. 4. Le cosinus vaut au plus $-1$ quand l'angle vaut $\pi$.

</details>

### MB3.Q4 — Moyennes pondérées par une softmax : dans l'enveloppe convexe ou non, largeur de bande, masque avant ou après la softmax, et un sous-ensemble vide

<details><summary>Indice 1</summary>

Fiche §5 : « Des poids par une softmax » et « La largeur de bande, une température » ; §6 : « Un score −∞ : une loi conditionnelle ».

</details>
<details><summary>Indice 2</summary>

Des poids positifs de somme 1 donnent une combinaison convexe. Le masque avant la softmax renormalise les poids restants, sur le sous-ensemble ; un poids mis à 0 après ne renormalise rien.

</details>
<details><summary>Indice 3</summary>

1. Une moyenne de nombres pondérée par des poids positifs de somme 1 est entre le plus petit et le plus grand. 4. Divise 0,2 et 0,1 par leur somme. 5. Le dénominateur de la softmax est une somme de $e^{-\infty} = 0$.

</details>

### MB3.Q5 — Multiplier tous les scores par c, ou leur ajouter une constante : ce qui change dans les poids, le poids maximal et l'entropie, et ce qui ne change pas

<details><summary>Indice 1</summary>

Fiche §5 : « Des poids par une softmax » ; §7 : « Multiplier les scores par c ».

</details>
<details><summary>Indice 2</summary>

$\operatorname{softmax}(\mathbf{s} + b) = \operatorname{softmax}(\mathbf{s})$, et $\operatorname{softmax}(c\,\mathbf{s})_i = \frac{p_i^c}{\sum_jp_j^c}$ : la loi tempérée de M28 à la température $T = \frac1c$.

</details>
<details><summary>Indice 3</summary>

2. Avec $c = 2$, élève chaque poids au carré, puis divise par la somme des carrés, $0{,}42$. 5. Avec $c = -1$, le score le plus petit devient le plus grand.

</details>

### MB3.Q6 — La softmax en ligne : ce que garde l'état, quand le remettre à l'échelle, et l'état vide

<details><summary>Indice 1</summary>

Fiche §8 : « Le problème » (l'état et la mise à jour par un bloc) et « La fusion de deux états ».

</details>
<details><summary>Indice 2</summary>

$m' = \max(m, \max_{j \in \mathcal{B}}s_j)$ ; $l' = l\,e^{m - m'} + \sum_{j \in \mathcal{B}}e^{s_j - m'}$, et de même pour $a$. Le log-sum-exp vaut $m + \ln l$.

</details>
<details><summary>Indice 3</summary>

3. $m' = 3 + \ln 2$, donc $e^{m - m'} = e^{-\ln 2} = \frac12$, et le nouveau score apporte $e^0 = 1$ à $l$ et $1 \times 7$ à $a$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### MB3.R1 — La forme exponentielle d'un complexe, et le produit comme rotation et homothétie (M22)

<details><summary>Indice 1</summary>

M22 §2 (la forme exponentielle, Moivre) ; fiche §2, « La multiplication par e^{iθ} ».

</details>
<details><summary>Indice 2</summary>

$\lvert x + iy\rvert = \sqrt{x^2 + y^2}$, et l'argument $\theta$ vérifie $\cos\theta = \frac{x}{r}$, $\sin\theta = \frac yr$. Un produit multiplie les modules et additionne les arguments.

</details>
<details><summary>Indice 3</summary>

1. $\cos\theta = \frac{\sqrt3}{2}$ et $\sin\theta = -\frac12$. 2. $-\frac\pi6 + \frac\pi6 = 0$. 4. $6 \times (-\frac\pi6) = -\pi$.

</details>

### MB3.R2 — Le log-sum-exp et la softmax stable (M05a)

<details><summary>Indice 1</summary>

M05a §8 (log-sum-exp et softmax stables) ; fiche §8, « Le problème ».

</details>
<details><summary>Indice 2</summary>

$\operatorname{LSE}(\mathbf{s}) = m + \ln\sum_je^{s_j - m}$, avec $m = \max_js_j$ ; la softmax vaut $\frac{e^{s_j - m}}{\sum_ke^{s_k - m}}$. En `float64`, $e^s$ déborde au-delà de $s \approx 709{,}78$ et vaut 0 en dessous de $s \approx -745$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbf{s} - 750 = (0, -2, -3)$ : calcule $\ln(1 + e^{-2} + e^{-3})$. 5. Le plus grand score est $-750$.

</details>

### MB3.R3 — Tempérer et tronquer une loi : p^{1/T} renormalisée, top-k et top-p comme lois conditionnelles (M28)

<details><summary>Indice 1</summary>

M28 §5 (la loi tempérée, top-k et top-p) ; fiche §6, « Un score −∞ : une loi conditionnelle ».

</details>
<details><summary>Indice 2</summary>

Tempérer à $T$ : $p_i^{1/T}$, puis renormaliser. Tronquer : garder des issues, mettre les autres à 0, puis renormaliser par la masse gardée.

</details>
<details><summary>Indice 3</summary>

1. $T = \frac12$ : élève au carré. 3. Ajoute les probabilités dans l'ordre décroissant jusqu'à atteindre 0,8 ; la masse gardée est le dénominateur.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB3.1 — Un bras articulé à deux segments : la position de la pince en valeurs exactes par les formules d'addition, les deux rotations enchaînées en une seule, et le retour par la rotation inverse

<details><summary>Indice 1</summary>

Fiche §1 : « Les trois autres, et ce qu'on en tire » ; §2 : « Composer, inverser » et « Ce qu'une rotation conserve ».

</details>
<details><summary>Indice 2</summary>

$105° = 60° + 45°$ : $\cos(a + b) = \cos a\cos b - \sin a\sin b$ et $\sin(a + b) = \sin a\cos b + \cos a\sin b$. $\mathbf{R}_\theta(r, 0) = (r\cos\theta, r\sin\theta)$. $\mathbf{R}_\alpha\mathbf{R}_\beta = \mathbf{R}_{\alpha + \beta}$, $\mathbf{R}_{60°}^\top = \mathbf{R}_{-60°}$, et une rotation conserve les normes.

</details>
<details><summary>Indice 3</summary>

c) $\mathbf{p} = (4\cos 60° + 2\cos 105°,\ 4\sin 60° + 2\sin 105°)$. f) $\mathbf{R}_{-60°}\mathbf{p} = \mathbf{R}_{-60°}\mathbf{R}_{60°}(4, 0) + \mathbf{R}_{-60°}\mathbf{R}_{105°}(2, 0)$ : simplifie chaque produit de rotations. g) La norme de f) est celle de $\mathbf{p}$.

</details>

### Ex MB3.2 — Rotations de Givens : deux rotations de l'espace qui ne commutent pas, deux rotations de ℝ⁴ dans des plans disjoints qui commutent, leur matrice diagonale par blocs, et la même rotation après une permutation des coordonnées

<details><summary>Indice 1</summary>

Fiche §3 : « Les rotations de Givens », « Quand deux rotations commutent » (l'exemple des deux quarts de tour), « Les matrices diagonales par blocs » et « Renuméroter les coordonnées ».

</details>
<details><summary>Indice 2</summary>

La matrice de droite agit la première. $\mathbf{R}_{ij}(\theta)$ envoie $\mathbf{e}_i$ sur $\cos\theta\,\mathbf{e}_i + \sin\theta\,\mathbf{e}_j$ et $\mathbf{e}_j$ sur $-\sin\theta\,\mathbf{e}_i + \cos\theta\,\mathbf{e}_j$. $\mathbf{P}^\top\mathbf{R}_{ij}(\theta)\mathbf{P}$ tourne $\mathbf{e}_{\sigma(i)}$ vers $\mathbf{e}_{\sigma(j)}$.

</details>
<details><summary>Indice 3</summary>

a) $\mathbf{R}_{12}(\frac\pi3)\mathbf{e}_2 = (-\frac{\sqrt3}{2}, \frac12, 0)$, puis $\mathbf{R}_{23}(\frac\pi2)$ envoie $(x_1, x_2, x_3)$ sur $(x_1, -x_3, x_2)$. b) Que fait $\mathbf{R}_{23}(\frac\pi2)$ de $\mathbf{e}_2$, et $\mathbf{R}_{12}$ de $\mathbf{e}_3$ ? f) $\sigma(1) = 1$ et $\sigma(2) = 4$ : $\mathbf{R}_{12}(\frac\pi3)$ devient $\mathbf{R}_{14}(\frac\pi3)$ ; fais de même pour $\mathbf{R}_{34}(\frac\pi2)$, sans changer l'ordre des deux indices. g) $\mathbf{R}_{ji}(\theta)$ est la transposée de $\mathbf{R}_{ij}(\theta)$ : c'est $\mathbf{R}_{ij}(-\theta)$.

</details>

### Ex MB3.3 — La direction du vent : l'encoder par (cos, sin), la distance entre deux encodages, un vent qui tourne comme une rotation de l'encodage, et la direction moyenne de trois relevés

<details><summary>Indice 1</summary>

Fiche §4 : « Décembre et janvier », « Un décalage est une rotation » et « La direction moyenne ».

</details>
<details><summary>Indice 2</summary>

$\lVert\mathbf{e}(\theta) - \mathbf{e}(\theta')\rVert^2 = 2 - 2\cos(\theta - \theta')$ et $\mathbf{R}_{45°}\mathbf{e}(\theta) = \mathbf{e}(\theta + 45°)$. La direction moyenne est l'angle du vecteur moyen des encodages, et $\rho$ sa longueur.

</details>
<details><summary>Indice 3</summary>

b) $340° - 20° = 320°$, et $\cos 320° = \cos 40°$. c) $150° + 45° = 195°$. e) $330° = 20° - 50°$ et $70° = 20° + 50°$ : $\mathbf{e}(20° - 50°) + \mathbf{e}(20° + 50°)$ se simplifie par les formules d'addition.

</details>

### Ex MB3.4 — L'estimateur de Nadaraya-Watson : la température d'un refuge à partir de quatre stations de montagne pondérées par un noyau gaussien de l'écart d'altitude, pour deux largeurs de bande, et ses deux limites

<details><summary>Indice 1</summary>

Fiche §5 : « L'estimateur de Nadaraya-Watson » (l'exemple du vélo) et « La largeur de bande, une température ».

</details>
<details><summary>Indice 2</summary>

Les scores sont $s_i = -\frac{(x - x_i)^2}{2h^2}$ ; on retranche le plus grand, on prend les exponentielles, on divise par leur somme, puis $\hat y = \sum_ip_iy_i$. $h \to 0$ : la station la plus proche ; $h \to \infty$ : la moyenne.

</details>
<details><summary>Indice 3</summary>

Les écarts valent $-600$, $-200$, 400 et 800 m. Pour $h = 200$ m, $2h^2 = 80\,000$ ; pour $h = 400$ m, $2h^2 = 320\,000$. Après le décalage par le plus grand score, les scores de $h = 200$ m valent $(-4 ;\ 0 ;\ -1{,}5 ;\ -7{,}5)$.

</details>

### Ex MB3.5 — Masques : une moyenne exponentielle normalisée vue comme une softmax sur les jours passés, puis la même quand un capteur tombe en panne un jour (un score −∞)

<details><summary>Indice 1</summary>

Fiche §6 : « Ne regarder que le passé » (la moyenne exponentielle normalisée) et « Un score −∞ : une loi conditionnelle ».

</details>
<details><summary>Indice 2</summary>

Le jour $u \le t$ reçoit le poids $\lambda^{t - u}$, normalisé par la somme sur les jours permis ; un jour de score $-\infty$ reçoit 0, et les autres se renormalisent entre eux.

</details>
<details><summary>Indice 3</summary>

a) $\lambda^3, \lambda^2, \lambda, 1$ valent $\frac18, \frac14, \frac12, 1$. c) Seuls les jours 1 et 2 sont permis. d) Retire $\frac12$ de la somme $\frac{15}{8}$.

</details>

### Ex MB3.6 — La saturation d'une softmax : trois scores multipliés par un facteur c croissant, le poids maximal, la sensibilité 1 − Σ pᵢ² et la borne (K − 1) e^{−cΔ}

<details><summary>Indice 1</summary>

Fiche §7 : « Multiplier les scores par c » et « La saturation » (la sensibilité et la borne de saturation).

</details>
<details><summary>Indice 2</summary>

Pour chaque $c$, retranche le plus grand score : les exponentielles valent 1, $e^{-0{,}8c}$ et $e^{-2{,}1c}$. $\Delta$ est l'écart entre le plus grand score et le suivant.

</details>
<details><summary>Indice 3</summary>

b) Avec les trois poids de $c = 6$, calcule $1 - (p_1^2 + p_2^2 + p_3^2)$. c) $2e^{-6 \times 0{,}8}$. d) Résous $2e^{-0{,}8c} \le 0{,}01$ en prenant le logarithme népérien.

</details>

### Ex MB3.7 — La softmax en ligne à la main : neuf scores (des multiples de ln 2) et leurs valeurs lus par blocs de trois, l'état (m, l, a) après chaque bloc, la moyenne pondérée finale, puis la fusion de deux états calculés séparément

<details><summary>Indice 1</summary>

Fiche §8 : « Le problème » (la mise à jour par un bloc, et l'exemple des avis) et « La fusion de deux états ».

</details>
<details><summary>Indice 2</summary>

$e^{s_j - m} = 2^{k_j - m/\ln 2}$ : tout se calcule en puissances de 2. Quand le maximum passe de $k\ln 2$ à $k'\ln 2$, $l$ et $a$ sont multipliés par $2^{k - k'}$ ; s'il ne change pas, par 1.

</details>
<details><summary>Indice 3</summary>

a) $m = 3\ln 2$ et les poids $2^{k_j - 3}$ valent $\frac14$, 1, $\frac18$. b) Le maximum passe à $4\ln 2$ : facteur $\frac12$. c) Le bloc 3 a pour plus grand score $4\ln 2$, égal à $m$. e) La machine B part de l'état vide. f) Remets l'état de A à l'échelle du maximum commun, $4\ln 2$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB3.8 — Les formules d'addition par le produit scalaire de deux vecteurs unitaires ; puis R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}, et la règle e^{iα}e^{iβ} = e^{i(α+β)} que M22 admettait

<details><summary>Indice 1</summary>

Fiche §1 : « Le cosinus d'une différence » (et son paragraphe « Pas de cercle vicieux »), « Les trois autres, et ce qu'on en tire », « La règle des exponentielles, enfin démontrée » ; §2 : « Composer, inverser ».

</details>
<details><summary>Indice 2</summary>

1. Ramène $a - b$ dans $]-\pi, \pi]$ par la périodicité ; l'angle de deux points du cercle unité est la longueur de l'arc qui les sépare. 2. $\cos(a + b) = \cos(a - (-b))$ ; $\cos(\frac\pi2 - x) = \sin x$ ; $\sin(a + b) = \cos((\frac\pi2 - a) - b)$. 3. Chaque coefficient du produit est une formule d'addition.

</details>
<details><summary>Indice 3</summary>

1. $\mathbf{u}_a\cdot\mathbf{u}_b$ vaut $\cos a\cos b + \sin a\sin b$ en coordonnées, et $\cos\varphi$ par l'angle, avec $\cos\varphi = \cos\lvert a - b\rvert = \cos(a - b)$. 4. $\cos(-\theta) = \cos\theta$ et $\sin(-\theta) = -\sin\theta$, puis $\mathbf{R}_{-\theta}\mathbf{R}_\theta = \mathbf{R}_0$. 5. Développe le produit avec $i^2 = -1$ et reconnais 2.

</details>

### Ex MB3.9 — Une moyenne pondérée par une softmax sur un ensemble de points commute avec toute renumérotation des points ; un masque triangulaire casse cette équivariance

<details><summary>Indice 1</summary>

Fiche §6 : « L'équivariance par permutation » ; §3 : « Renuméroter les coordonnées » (la matrice $\mathbf{P}$).

</details>
<details><summary>Indice 2</summary>

$(\mathbf{P}\mathbf{s})_k = s_{\sigma(k)}$ et $(\mathbf{P}\mathbf{S}\mathbf{P}^\top)_{kw} = S_{\sigma(k)\sigma(w)}$. Une somme sur tous les indices ne change pas quand on les renumérote. $\mathbf{P}^\top\mathbf{P} = \mathbf{I}$.

</details>
<details><summary>Indice 3</summary>

3. La ligne $k$ de $\mathbf{P}\mathbf{S}\mathbf{P}^\top$ est la ligne $\sigma(k)$ de $\mathbf{S}$, permutée : applique 1 ligne par ligne, puis calcule $(\mathbf{P}\mathbf{C}\mathbf{P}^\top)(\mathbf{P}\mathbf{Y})$. 4. Deux capteurs, un score nul partout, des mesures 0 et 1 : calcule les deux sorties avant et après l'échange.

</details>

### Ex MB3.10 — La softmax en ligne est exacte : l'invariant de l'état après chaque bloc, par récurrence ; puis la fusion de deux états est associative et commutative, d'élément neutre (−∞, 0, 0)

<details><summary>Indice 1</summary>

Fiche §8 : « Le problème » (la mise à jour et l'invariant) et « La fusion de deux états ».

</details>
<details><summary>Indice 2</summary>

Le nouveau maximum $m'$ est le plus grand score de $J \cup \mathcal{B}$. La clé : $e^{s_j - m_J}\,e^{m_J - m'} = e^{s_j - m'}$. L'état vide se traite avec la convention $e^{-\infty} = 0$.

</details>
<details><summary>Indice 3</summary>

1. Écris $l_J\,e^{m_J - m'}$ comme une somme sur $J$, puis ajoute la somme sur $\mathcal{B}$. 2. Initialisation : le bloc 1 depuis l'état vide ; à la fin, multiplie $a$ et $l$ par $e^m$. 4. Le calcul de 1 marche pour deux états quelconques de réunions disjointes : la commutativité et l'associativité viennent de celles de la réunion. 5. Que vaudrait $e^{-\infty - (-\infty)}$ ?

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex MB3.11 — Pont : à normes égales, les poids d'un noyau gaussien sont une softmax des produits scalaires divisés par h² ; le vérifier sur quatre stations d'un même cercle, et lire 1/h² comme l'échelle des scores

<details><summary>Indice 1</summary>

Fiche §5 : « À normes égales, des produits scalaires » ; §7 : « Multiplier les scores par c ».

</details>
<details><summary>Indice 2</summary>

$\lVert\mathbf{x} - \mathbf{x}_i\rVert^2 = \lVert\mathbf{x}\rVert^2 - 2\,\mathbf{x}\cdot\mathbf{x}_i + \lVert\mathbf{x}_i\rVert^2$, et ici les deux normes valent 5. Une constante commune à tous les scores disparaît dans la softmax.

</details>
<details><summary>Indice 3</summary>

b) $\lVert\mathbf{x} - \mathbf{x}_i\rVert^2 = 50 - 2\,\mathbf{x}\cdot\mathbf{x}_i$. c) Les scores $-\frac{\lVert\mathbf{x} - \mathbf{x}_i\rVert^2}{50}$ valent $\frac{\mathbf{x}\cdot\mathbf{x}_i}{25} - 1$. f) Avec $h = 2{,}5$ km, $\frac{1}{h^2}$ est 4 fois plus grand.

</details>

### Ex MB3.12 — MML §3.9 lu : la rotation du plan (3.76), les rotations de l'espace (3.77)–(3.79), la rotation de Givens (3.80)–(3.81) et les propriétés du §3.9.4 ; R₂(θ) écrite comme une rotation de Givens, et deux rotations de l'espace qui ne commutent pas, sur un vecteur choisi

<details><summary>Indice 1</summary>

Le guide de lecture de MML de la fiche, puis fiche §2 (« La matrice d'une rotation », « Composer, inverser ») et §3 (« Les rotations autour des axes de l'espace », « Les rotations de Givens », « Quand deux rotations commutent »).

</details>
<details><summary>Indice 2</summary>

La rotation de Givens $\mathbf{R}_{ij}(\theta)$ a $-\sin\theta$ à la ligne $i$, colonne $j$, et $\sin\theta$ à la ligne $j$, colonne $i$. Compare (3.78) à $\mathbf{R}_{13}(\theta)$ : où sont les signes ?

</details>
<details><summary>Indice 3</summary>

2. Calcule $\mathbf{R}_2(\theta)\mathbf{e}_3$ : la colonne 3 de (3.78). 3. Pour $(i, j) = (2, 4)$ dans $\mathbb{R}^5$, les trois blocs identité ont pour tailles $i - 1$, $j - i - 1$ et $n - j$. 4. Prends un vecteur qui n'est sur aucun des deux axes, comme $(1, 1, 0)$ ou $(0, 1, 1)$, et applique les deux rotations dans les deux ordres.

</details>

### Ex MB3.13 — Expliquer, avec une caisse tenue dans une monnaie qui change, pourquoi la softmax en ligne donne exactement le résultat du calcul en une fois

<details><summary>Indice 1</summary>

Fiche §8 : « Le problème » (l'invariant) et « La fusion de deux états » ; ✏️ MB3.7.

</details>
<details><summary>Indice 2</summary>

La monnaie de référence est le plus grand score lu ; les deux registres sont $l$ et $a$ ; le taux de conversion est $e^{m - m'}$, plus petit que 1.

</details>
<details><summary>Indice 3</summary>

Ce que l'on veut à la fin est $a/l$ : un rapport de deux montants écrits dans la même monnaie. Que devient ce rapport quand on convertit les deux montants au même taux ?

</details>

<a id="entretien"></a>

## 💼 Entretien

### MB3.E1 — « Comment encoder une variable cyclique comme une heure ou une direction, et pourquoi pas par sa valeur ? »

<details><summary>Indice 1</summary>

Fiche §4 : « Décembre et janvier », « Plusieurs horloges », et le 💻 « Aujourd'hui en pratique » de la fin du §4.

</details>
<details><summary>Indice 2</summary>

Pense à 23 h et minuit, à 6 h et 18 h, et à la formule de la distance entre deux encodages.

</details>
<details><summary>Indice 3</summary>

Plan : le problème de la valeur brute ; le cercle $(\cos, \sin)$ et sa période ; pourquoi deux coordonnées ; la distance $2 - 2\cos$ de l'écart ; plusieurs périodes ; une alternative (le one-hot) ; un piège (la période, la standardisation).

</details>

<a id="notebook"></a>

## Notebook

### MB3.14 — La matrice d'une rotation de Givens de ℝⁿ : `givens_rotation`

<details><summary>Indice 1</summary>

Fiche §3, « Les rotations de Givens », et la docstring de `givens_rotation` dans ta copie de `positional.py`.

</details>
<details><summary>Indice 2</summary>

Refuse `bool` avant de tester l'entier (`isinstance(True, int)` vaut `True`) ; accepte `np.integer` ; pour $\theta$, `math.isfinite`. Puis quatre affectations dans `np.eye(n)`.

</details>
<details><summary>Indice 3</summary>

`G[i, i] = G[j, j] = math.cos(theta)`, `G[j, i] = math.sin(theta)`, `G[i, j] = -math.sin(theta)`. b) Essaie les six couples $(i, j)$ avec `np.allclose`. c) `np.linalg.norm(G @ H - H @ G)` donne la norme de Frobenius.

</details>

### MB3.15 — La softmax en ligne : l'état (m, l, a) de scores et de valeurs lus par blocs, et l'état après chaque bloc : `online_softmax`

<details><summary>Indice 1</summary>

Fiche §8, « Le problème » (la mise à jour par un bloc), et la docstring de `online_softmax`.

</details>
<details><summary>Indice 2</summary>

Pars de `m = -math.inf`, `l = 0.0` et d'un accumulateur nul (0.0 ou `np.zeros(k)`, ou `None`). Pour chaque tranche `s[b:b + block_size]` : si son maximum vaut `-inf`, l'état ne change pas (mais il compte dans l'historique) ; sinon `m_new = max(m, mb)` et `f = math.exp(m - m_new)` (qui vaut 0 quand `m = -inf`).

</details>
<details><summary>Indice 3</summary>

`w = np.exp(s_b - m_new)`, `l = l * f + float(w.sum())`, `acc = acc * f + w @ v_b`. Avec `history`, ajoute l'état à une liste après chaque bloc, avec une copie de `acc` quand c'est un tableau. Rends `float(acc)` pour des valeurs 1-D. d) `np.column_stack([np.cos(np.radians(theta)), np.sin(np.radians(theta))])`, puis `np.degrees(np.arctan2(y, x)) % 360`.

</details>

### MB3.16 — La fusion de deux états de la softmax en ligne : `merge_softmax_states`

<details><summary>Indice 1</summary>

Fiche §8, « La fusion de deux états », et la docstring de `merge_softmax_states`.

</details>
<details><summary>Indice 2</summary>

Contrôle les deux états, puis traite à part deux états vides. Sinon `m = max(m1, m2)` et chaque état est multiplié par $e^{m_k - m}$ (0 pour un état vide).

</details>
<details><summary>Indice 3</summary>

`f1 = 0.0 if m1 == -math.inf else math.exp(m1 - m)`, de même `f2` ; rends `(m, l1 * f1 + l2 * f2, acc1 * f1 + acc2 * f2)` (un nouveau tableau, `None` si les deux `acc` le sont). b) Les morceaux : `S_16[:2]`, `S_16[2:7]`, `S_16[7:8]`, `S_16[8:]`.

</details>

### MB3.17 — Prédire ce que deviennent les poids et la prévision de Nadaraya-Watson quand la largeur de bande est divisée ou multipliée par 10, puis tracer

<details><summary>Indice 1</summary>

Fiche §5, « La largeur de bande, une température » : ses deux limites, et la figure de l'exemple du vélo.

</details>
<details><summary>Indice 2</summary>

La largeur de bande est une température, $T = 2h^2$. Compare $h/10 = 0{,}025$ km à l'écart entre deux stations voisines (environ 0,07 km), et $10h = 2{,}5$ km à l'étendue des altitudes (1,6 km) : laquelle des deux limites de la fiche est presque atteinte, dans chaque cas ?

</details>
<details><summary>Indice 3</summary>

a) Le rapport des poids de deux stations vaut $e^{(d_2^2 - d_1^2)/(2h^2)}$, où $d_1 < d_2$ sont leurs distances à 1,85 km : que devient-il quand $h$ est très petit devant l'écart entre stations ? b) Quand $h$ est très grand devant l'étendue des altitudes, tous les scores sont proches de 0 : que valent alors les poids, en tout point ? c) À l'altitude d'une station, quelle station est la plus proche, et quel poids reçoit-elle quand $h$ est très petit ? Pour le code : les scores `-(x[:, None] - X[None, :]) ** 2 / (2 * h ** 2)`, `scipy.special.softmax(..., axis=1)`, puis `@ Y`.

</details>

### MB3.18 — La softmax en ligne selon l'ordre et la taille des blocs : le nombre de remises à l'échelle (les états après chaque bloc) pour des scores croissants, décroissants ou mélangés, comparé à H_N − 1, et la mémoire gardée

<details><summary>Indice 1</summary>

Fiche §8, « Combien de remises à l'échelle ? ».

</details>
<details><summary>Indice 2</summary>

Une remise à l'échelle a lieu au bloc $b \ge 2$ quand le plus grand des scores lus change, c'est-à-dire quand le bloc $b$ contient un nouveau record. `np.argsort(S_18)` donne l'ordre croissant ; permute les valeurs avec les scores.

</details>
<details><summary>Indice 3</summary>

`count_rescalings_18` : compte les indices `b ≥ 1` tels que `states[b][0] != states[b - 1][0]`. $H_N - 1$ : `sum(1 / k for k in range(2, N + 1))`. e) $5 + B(1 + 3)$.

</details>

### MB3.19 — Trois horloges (la journée, la semaine, l'année) : l'encodage d'une date sur trois cercles, un décalage comme trois rotations, et le produit scalaire de deux encodages en fonction de l'écart

<details><summary>Indice 1</summary>

Fiche §4, « Plusieurs horloges » (et sa figure à deux aiguilles) et « Un décalage est une rotation ».

</details>
<details><summary>Indice 2</summary>

$\mathbf{E}(0)\cdot\mathbf{E}(\delta) = \cos\omega_1\delta + \cos\omega_2\delta + \cos\omega_3\delta$. Le décalage de $\delta$ tourne chaque horloge de $\omega_k\delta$ : une matrice diagonale par blocs, produit de trois rotations de Givens de plans disjoints.

</details>
<details><summary>Indice 3</summary>

`w = 2 * np.pi / np.array([24, 168, 8760])` ; `encode_19` empile `np.cos(w * t)` et `np.sin(w * t)` dans l'ordre (cos, sin) de chaque horloge. c) Calcule le produit pour tous les $\delta$ de 1 à 8 760 et prends `np.argmax` (+ 1). Pense à 365 = 52 × 7 + 1.

</details>

### MB3.20 — Chasse à l'erreur : deux rotations de l'espace composées dans le mauvais ordre, une direction moyenne prise comme la moyenne des angles, une softmax en ligne qui remet l à l'échelle mais pas l'accumulateur

<details><summary>Indice 1</summary>

Fiche §3 (⚠️ : la matrice de droite agit la première), §4 (« La direction moyenne ») et §8 (⚠️ : remettre $l$ **et** $a$ à l'échelle).

</details>
<details><summary>Indice 2</summary>

(1) Dans `A @ B @ x`, $\mathbf{B}$ agit d'abord. (2) Que donne la moyenne de 340 et 10, et quelle est la direction entre les deux ? (3) Quand l'accumulateur a-t-il besoin d'être remis à l'échelle ? Que se passe-t-il pour des scores décroissants ?

</details>
<details><summary>Indice 3</summary>

(1) `R23(beta) @ R12(alpha) @ x` ; deux demi-tours sont diagonaux. (2) L'argument du vecteur moyen des $(\cos, \sin)$. (3) `acc = acc * f + w @ v_b`, comme `l`.

</details>

### MB3.21 — Un test de propriété : la softmax en ligne ne dépend ni de la taille des blocs, ni d'une même permutation des scores et des valeurs, ni d'une constante ajoutée aux scores, et la fusion de trois états est associative

<details><summary>Indice 1</summary>

Fiche §8 (l'invariant, la fusion) et §5 (une constante ajoutée aux scores) ; le 🛠️ MB2.18, qui avait la même structure.

</details>
<details><summary>Indice 2</summary>

Chaque contrôle compare deux états par la fonction fournie `differ_21(state1, state2, rtol)` ; calcule d'abord `ref = func(scores, values, block_size=1)`, puis les quatre contrôles, avec un seul `try` autour de tout.

</details>
<details><summary>Indice 3</summary>

Pour `"shift"`, l'état attendu est `(ref[0] + shift, ref[1], ref[2])`. Pour `"associative"`, les morceaux `scores[:i]`, `scores[i:j]`, `scores[j:]` et leurs valeurs. c) Une version fausse peut respecter une propriété : relis ce que chacune fait aux poids, au maximum, et à l'ordre des fusions.

</details>

### MB3.22 — Défi : prévoir la production d'une éolienne par Nadaraya-Watson sur l'encodage cyclique de la direction du vent et du jour de l'année, la largeur de bande choisie par validation croisée « un de côté », sous une erreur quadratique moyenne donnée

<details><summary>Indice 1</summary>

Fiche §4 (encoder une variable cyclique) et §5 (Nadaraya-Watson, la validation croisée « un de côté »).

</details>
<details><summary>Indice 2</summary>

Encode les relevés par `encode_22(theta, day)`, puis calcule une fois la matrice $(400, 400)$ des distances au carré entre relevés. Pour chaque $h$ de la grille, prévois chaque relevé par les 399 autres : mets la diagonale des scores à $-\infty$.

</details>
<details><summary>Indice 3</summary>

`Z = encode_22(train[:, 0], train[:, 1])` et `y = train[:, 2]` ; `D2 = ((Z[:, None, :] - Z[None, :, :]) ** 2).sum(-1)` ; pour chaque `h`, `S = -D2 / (2 * h ** 2)`, `np.fill_diagonal(S, -np.inf)`, `pred = scipy.special.softmax(S, axis=1) @ y`, et l'erreur `np.mean((pred - y) ** 2)` ; garde le meilleur `h`, puis prévois `TEST_22` avec tous les relevés.

</details>
