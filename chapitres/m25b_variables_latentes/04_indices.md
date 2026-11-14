# M25b · Variables latentes et ELBO — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [📖 🗣️ 🔗 Lecture, explication et pont](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M25b.Q1 — Lire un graphe orienté : factoriser la loi jointe, l'ordre d'un tirage ancestral, et les variables qui deviennent dépendantes quand on observe leur effet commun

<details><summary>Indice 1</summary>

Fiche §1 : « Les graphes orientés et la factorisation », puis « Chaîne, fourche et collision ».

</details>
<details><summary>Indice 2</summary>

Un facteur par nœud, sachant ses parents. $V \to B \leftarrow C$ est une collision : bloquée tant qu'on n'observe ni $B$ ni un de ses descendants. $V \to B \to A$ est une chaîne : bloquée quand on observe $B$.

</details>
<details><summary>Indice 3</summary>

1. $p(V)\,p(C)\,p(B \mid V, C)\,p(A \mid B)$. Pour 4 et 5, demande-toi si l'on observe l'effet commun ou un de ses descendants ; pour 6, si le nœud du milieu de la chaîne est observé.

</details>

### M25b.Q2 — Marginaliser ou conditionner : vraisemblance marginale, posterior d'un latent, moyenne et variance d'un mélange

<details><summary>Indice 1</summary>

Fiche §2 : la vraisemblance marginale, le posterior, puis les lois de l'espérance et de la variance totales.

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(X)$ = la variance moyenne dans les groupes + la variance des moyennes. $p(x) = \sum_z p(z)\,p(x \mid z)$ et $P(Z = 1 \mid x) = \frac{p(Z = 1)\,p(x \mid Z = 1)}{p(x)}$.

</details>
<details><summary>Indice 3</summary>

1. $\frac12 \times 3 + \frac12 \times 11 = 7$. Pour 2 : dans les groupes, 2 ; entre les groupes, chaque moyenne est à 4 de 7. Pour 6, pense à l'erreur classique du §2 : une somme pondérée de variables n'est pas un mélange.

</details>

### M25b.Q3 — Un mélange de gaussiennes : responsabilités, logarithme d'une somme, vraisemblance infinie et composantes renumérotées

<details><summary>Indice 1</summary>

Fiche §3 : « Les responsabilités, calculées en log », « Une vraisemblance qui n'est pas bornée » et « Des composantes à numérotation arbitraire ».

</details>
<details><summary>Indice 2</summary>

$\ln r_{ik} = a_{ik} - \operatorname{LSE}_j\,a_{ij}$ ; avec deux termes, $r_{i1} = \frac{1}{1 + e^{a_{i2} - a_{i1}}}$. Une seule gaussienne doit expliquer **toutes** les données à la fois.

</details>
<details><summary>Indice 3</summary>

1. $e^{a_{i2} - a_{i1}} = e^{-\ln 3} = \frac13$, donc $r_{i1} = \frac{1}{1 + 1/3}$. Pour 2, factorise $e^{-3}$ dans la somme. Pour 4, compte les façons de renuméroter 3 objets.

</details>

### M25b.Q4 — L'EM : ce que font le pas E et le pas M, ce qui ne baisse jamais, ce qui n'est pas garanti, et k-means comme limite

<details><summary>Indice 1</summary>

Fiche §4 : l'algorithme, « Ce qui est garanti, et ce qui ne l'est pas », « Avec une régularisation, plus de garantie », « k-means comme limite ».

</details>
<details><summary>Indice 2</summary>

$\pi_k = \frac{N_k}{n}$. Avec des covariances $\gamma\mathbf{I}$ et des poids égaux, $r_{ik}$ dépend des différences de carrés des distances, divisées par $2\gamma$.

</details>
<details><summary>Indice 3</summary>

2. $\frac{3{,}2}{10}$ et $\frac{6{,}8}{10}$. 6. $r = \frac{1}{1 + e^{-(\lVert x - 10\rVert^2 - \lVert x - 0\rVert^2)/(2\gamma)}}$ avec $x = 4$ : regarde le signe de $36 - 16$, puis fais tendre $\gamma$ vers 0.

</details>

### M25b.Q5 — L'ELBO : une borne de quoi, une égalité quand, un écart égal à quelle KL ?

<details><summary>Indice 1</summary>

Fiche §5, le théorème et « Deux autres lectures » ; le §7 pour la question 6.

</details>
<details><summary>Indice 2</summary>

$\ln p(\mathbf{x}) = \operatorname{ELBO}(q) + \mathrm{KL}(q \,\|\, p(\mathbf{z} \mid \mathbf{x}))$, pour toute loi $q$.

</details>
<details><summary>Indice 3</summary>

4. La KL est la différence $\ln p(\mathbf{x}) - \operatorname{ELBO}(q)$. 6. Dans l'identité, quel terme ne dépend pas de $q$ ?

</details>

### M25b.Q6 — L'ACP probabiliste : covariance marginale, rotation de W, angles principaux et directions éteintes

<details><summary>Indice 1</summary>

Fiche §6 : le modèle, « La rotation : seul le sous-espace est déterminé », les angles principaux et « Les directions éteintes ».

</details>
<details><summary>Indice 2</summary>

$\mathbf{C} = \mathbf{w}\mathbf{w}^\top + \sigma^2\mathbf{I}$ : $\mathbf{w}$ est vecteur propre de $\mathbf{C}$, et tout vecteur orthogonal à $\mathbf{w}$ aussi. Bruit connu : la colonne $j$ a pour carré de norme $\max(\lambda_j - \sigma^2, 0)$.

</details>
<details><summary>Indice 3</summary>

1. $C_{11} = w_1^2 + \sigma^2$ et $C_{23} = w_2w_3$. 2. $\mathbf{C}\mathbf{w} = (\lVert\mathbf{w}\rVert^2 + \sigma^2)\mathbf{w}$. 4. Combien d'angles principaux entre une droite et un plan, et que dit la propriété « tous nuls » ?

</details>

### M25b.Q7 — KL directe ou inverse, inférence amortie et écart d'amortissement, et dériver sous l'espérance : quand le peut-on ?

<details><summary>Indice 1</summary>

Fiche §7 : « Le sens de la KL », « L'inférence amortie », « Dériver une espérance… » et « Quand l'échange échoue ».

</details>
<details><summary>Indice 2</summary>

$\mathrm{KL}(q \,\|\, p)$ est énorme là où $q$ met de la masse et $p$ presque pas ; $\mathrm{KL}(p \,\|\, q)$ apparie les moments pour une $q$ gaussienne. Les hypothèses du théorème : continuité, coins de probabilité nulle, domination.

</details>
<details><summary>Indice 3</summary>

3. La loi rendue par la règle amortie appartient à la famille : compare à un sup sur la famille. 5. L'indicatrice est-elle continue en $\mu$ ?

</details>

### M25b.Q8 — Pondérer la KL : multiplicateur, information mutuelle, posterior agrégé et code effondré

<details><summary>Indice 1</summary>

Fiche §8 : « β est une pente », « Le bruit joue le rôle de β », le posterior agrégé et la décomposition de la KL moyenne au prior.

</details>
<details><summary>Indice 2</summary>

$\mathcal{R}^{\star\prime}(B) = \beta$ ; seul $2\sigma^2\beta$ compte ; $\mathbb{E}_{\mathbf{x}}\mathrm{KL} = I(X ; Z) + \mathrm{KL}(q(\mathbf{z}) \,\|\, p(\mathbf{z}))$.

</details>
<details><summary>Indice 3</summary>

1. Une pente : $\frac{0{,}03}{0{,}1}$. 4. Écris $2 \times 2 \times 0{,}6 = 2 \times 0{,}4 \times \beta$. 5. Relis les deux conditions de la propriété du posterior agrégé.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M25b.R1 — Bayes sur une variable cachée et log-sum-exp : probabilités totales, posterior, et une somme d'exponentielles sans dépassement (M04, M05a)

<details><summary>Indice 1</summary>

M04 (probabilités totales, règle de Bayes) et M05a (le log-sum-exp stable).

</details>
<details><summary>Indice 2</summary>

$P(D) = \sum_\ell P(\ell)\,P(D \mid \ell)$ et $P(\ell \mid D) = \frac{P(\ell)\,P(D \mid \ell)}{P(D)}$. $\ln(e^a + e^b) = m + \ln(e^{a - m} + e^{b - m})$ avec $m = \max(a, b)$.

</details>
<details><summary>Indice 3</summary>

1. $0{,}55 \times 0{,}02 + 0{,}30 \times 0{,}03 + 0{,}15 \times 0{,}06$. 3. Avec $m = -800$ : $-800 + \ln(1 + e^{-2})$. 6. La somme contient le plus grand terme, et au plus $K$ termes qui ne le dépassent pas.

</details>

### M25b.R2 — L'inégalité de Jensen, la KL continue et l'information mutuelle (M06, M25a)

<details><summary>Indice 1</summary>

M06 (Jensen discret, KL, information mutuelle) et M25a §7 (KL continue, KL entre gaussiennes).

</details>
<details><summary>Indice 2</summary>

Pour une fonction concave $f$, $f(\mathbb{E}[X]) \ge \mathbb{E}[f(X)]$. Entre deux gaussiennes de même variance, $\mathrm{KL} = \frac{(\mu_0 - \mu_1)^2}{2\sigma^2}$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbb{E}[X] = 17$ et $\mathbb{E}[\ln X] = \frac12\ln 64$. 2. $\frac{3^2}{2 \times 3}$. 3. Écris $-\mathrm{KL}(p \,\|\, q)$ comme $\mathbb{E}_p\big[\ln\frac qp\big]$. 4. Calcule $h$ d'une gaussienne de très petite variance. 5. Pour des variables indépendantes, $p(x, y) = p(x)\,p(y)$.

</details>

### M25b.R3 — La SVD, l'ACP et la projection orthogonale sur un sous-espace (M12b, M12d)

<details><summary>Indice 1</summary>

M12b (projection, Gram-Schmidt) et M12d (SVD et ACP).

</details>
<details><summary>Indice 2</summary>

La projection sur la droite de $\mathbf{u}$ : $\frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\mathbf{u}$. Gram-Schmidt : retirer la projection sur les vecteurs déjà trouvés, puis normaliser.

</details>
<details><summary>Indice 3</summary>

1. $\frac{3}{2}(1, 1, 0)$. 2. $\mathbf{q}_1 = \frac{1}{\sqrt2}(1, 1, 0)$, puis $(1, 0, 1) - \frac12(1, 1, 0)$ à normaliser. 6. Cherche une matrice non symétrique dont les valeurs propres sont nulles.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M25b.1 — Trois machines produisent des pièces de longueurs gaussiennes : le graphe, la loi jointe, un tirage ancestral à la main, la vraisemblance marginale d'une longueur et le posterior de la machine

<details><summary>Indice 1</summary>

Fiche §1 (le tirage ancestral) et §2 (la vraisemblance marginale et le posterior, l'exemple de la station).

</details>
<details><summary>Indice 2</summary>

Calcule les trois densités $\mathcal{N}(98{,}2 \mid \mu_z, \sigma_z^2) = \frac{1}{\sigma_z\sqrt{2\pi}}e^{-(98{,}2 - \mu_z)^2/(2\sigma_z^2)}$, avec l'écart-type $\sigma_z$, puis pondère-les par $\pi_z$ : leur somme est $p(98{,}2)$.

</details>
<details><summary>Indice 3</summary>

a) $u = 0{,}62$ tombe dans $[0{,}5 ;\ 0{,}8[$ : machine 2, puis $102 + 1 \times (-1{,}3)$. Pour la machine 1 : $\frac{e^{-1{,}8^2/2}}{\sqrt{2\pi}} \approx 0{,}0790$, pondérée par 0,5. Fais de même pour les machines 2 et 3 (attention : $\sigma_3^2 = 4$), puis divise chaque terme pondéré par leur somme. Pour f), les proportions égales se simplifient.

</details>

### Ex M25b.2 — Deux variétés de grains de café (longueur, largeur) : moyenne et covariance du mélange par la variance totale, part de la variance entre variétés, et une corrélation qu'aucune variété n'a

<details><summary>Indice 1</summary>

Fiche §2 : « Les lois de l'espérance et de la variance totales », et la formule des moments d'un mélange en dimension $d$.

</details>
<details><summary>Indice 2</summary>

$\boldsymbol{\Sigma} = \sum_k\pi_k\boldsymbol{\Sigma}_k + \sum_k\pi_k(\boldsymbol{\mu}_k - \boldsymbol{\mu})(\boldsymbol{\mu}_k - \boldsymbol{\mu})^\top$ ; la corrélation est $\frac{\Sigma_{12}}{\sqrt{\Sigma_{11}\Sigma_{22}}}$.

</details>
<details><summary>Indice 3</summary>

a) $0{,}6(11, 7) + 0{,}4(13, 8)$. c) Les écarts à la moyenne du mélange sont $(-0{,}8 ;\ -0{,}4)$ et $(1{,}2 ;\ 0{,}6)$ : pondère leurs produits $\boldsymbol{\delta}\boldsymbol{\delta}^\top$ par 0,6 et 0,4. e) Le coefficient $(1, 1)$ de c) divisé par celui de d).

</details>

### Ex M25b.3 — Deux séries de résistances mélangées : les responsabilités de quatre mesures en log, un pas M (proportion, moyennes, variances), et la log-vraisemblance qui monte (suite de M13a, composantes inconnues)

<details><summary>Indice 1</summary>

Fiche §3 (les responsabilités en log, l'exemple en $x = 8$) et §4 (l'algorithme et l'exemple d'une itération).

</details>
<details><summary>Indice 2</summary>

Calcule une fois les deux constantes $\ln\pi_k - \frac12\ln(2\pi\sigma_k^2)$, puis $a_{ik}$ = constante $- \frac{(x_i - \mu_k)^2}{2\sigma_k^2}$. Pour chaque mesure, $\operatorname{LSE} = m + \ln(1 + e^{a_{\text{petit}} - m})$, $r_{ik} = e^{a_{ik} - \operatorname{LSE}}$, et $\ell$ = la somme des LSE.

</details>
<details><summary>Indice 3</summary>

Pour 46,0 Ω : $a_{11} = -1{,}717446 - \frac{1}{2} = -2{,}217446$ et $a_{12} = -1{,}974921 - \frac{25}{5} = -6{,}974921$, d'où $\operatorname{LSE} = -2{,}217446 + \ln(1 + e^{-4{,}757475})$ et $r_{11} \approx 0{,}9915$. Fais de même pour les trois autres, puis $N_k$, $\pi_k = \frac{N_k}{4}$, $\mu_k = \frac{\sum_ir_{ik}x_i}{N_k}$ et $\sigma_k^2 = \frac{\sum_ir_{ik}(x_i - \mu_k)^2}{N_k}$ avec les **nouvelles** moyennes. Pour f), refais le tableau des $a_{ik}$ avec les nouveaux paramètres.

</details>

### Ex M25b.6 — Une sonde de qualité de l'eau, un état caché à deux valeurs et une mesure gaussienne : ln p(x), l'ELBO pour trois lois q, et l'écart égal à la KL au posterior

<details><summary>Indice 1</summary>

Fiche §5 : la définition de l'ELBO, le théorème et l'exemple de la chaudière.

</details>
<details><summary>Indice 2</summary>

Avec $a_z = \ln p(z) + \ln\mathcal{N}(x \mid \mu_z, \sigma_z^2)$ : $\ln p(x) = \operatorname{LSE}(a_1, a_2)$ et $\operatorname{ELBO}(q) = \sum_zq(z)\big(a_z - \ln q(z)\big)$.

</details>
<details><summary>Indice 3</summary>

$\ln\mathcal{N}(2 \mid 1 ;\ 0{,}25) = -\frac12\ln(0{,}5\pi) - 2$ et $\ln\mathcal{N}(2 \mid 3, 1) = -\frac12\ln(2\pi) - \frac12$ ; ajoute $\ln 0{,}9$ et $\ln 0{,}1$. c) $\frac12(a_1 - \ln\frac12) + \frac12(a_2 - \ln\frac12)$. f) $\sum_zq(z)\ln\frac{q(z)}{p(z \mid x)}$, avec le posterior de b).

</details>

### Ex M25b.9 — Trois épreuves d'un concours expliquées par une aptitude cachée : covariance marginale, posterior d'un candidat (une règle affine des notes), et maximum de vraisemblance à partir de valeurs propres données, dont une direction éteinte

<details><summary>Indice 1</summary>

Fiche §6 : la loi marginale et le posterior exact, « Le maximum de vraisemblance » et « Les directions éteintes » ; le §7 pour l'inférence amortie.

</details>
<details><summary>Indice 2</summary>

$k = 1$ : $\mathbf{C} = \mathbf{w}\mathbf{w}^\top + \sigma^2\mathbf{I}$, $M = \lVert\mathbf{w}\rVert^2 + \sigma^2$ (un nombre), $z \mid \mathbf{x} \sim \mathcal{N}\big(\frac{\mathbf{w}^\top(\mathbf{x} - \boldsymbol{\mu})}{M}, \frac{\sigma^2}{M}\big)$. Tipping et Bishop : $\hat\sigma^2$ = la moyenne des valeurs propres écartées, $\lVert\hat{\mathbf{w}}\rVert^2 = \lambda_1 - \hat\sigma^2$.

</details>
<details><summary>Indice 3</summary>

a) $\mathbf{w}\mathbf{w}^\top$ a pour première ligne $(4, 2, 4)$ ; ajoute 3 sur la diagonale. d) $\mathbf{x} - \boldsymbol{\mu} = (3, 1, 2)$. f) À $k = 1$, on écarte $\lambda_2$ et $\lambda_3$. h) Compare chaque valeur propre gardée au bruit connu 5.

</details>

### Ex M25b.10 — Les angles principaux entre deux plans de ℝ⁴ et entre deux droites de ℝ³ : bases orthonormées, SVD de Q_Aᵀ Q_B, et pourquoi le résultat ne dépend pas des bases choisies

<details><summary>Indice 1</summary>

Fiche §6 : « Les angles principaux entre deux sous-espaces » ; M12b pour Gram-Schmidt, M12d pour la SVD.

</details>
<details><summary>Indice 2</summary>

Les valeurs singulières de $\mathbf{M} = \mathbf{Q}_A^\top\mathbf{Q}_B$ sont les racines des valeurs propres de $\mathbf{M}^\top\mathbf{M}$ ; les angles sont leurs arccosinus. Pour deux droites, $\cos\phi = \frac{\lvert\mathbf{u}^\top\mathbf{v}\rvert}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}$.

</details>
<details><summary>Indice 3</summary>

a) $\mathbf{q}_1 = \frac{1}{\sqrt5}(1, 2, 0, 0)$ ; $\mathbf{a}_2 - \frac45(1, 2, 0, 0) = \frac35(2, -1, 0, 0)$. b) $\lVert\mathbf{b}_1\rVert = 13$ et $\mathbf{b}_2 \cdot \frac{\mathbf{b}_1}{13} = 13$. d) Calcule $\mathbf{M}^\top\mathbf{M}$ : ses coefficients hors diagonale s'annulent. Dans ta copie, écris $\mathbf{Q}_A'^\top\mathbf{Q}_B' = \mathbf{R}_A^\top\mathbf{M}\mathbf{R}_B$.

</details>

### Ex M25b.12 — Le coût d'un stock c face à une demande gaussienne : E[(D − c)⁺], ses dérivées en μ et en σ par le chemin, puis par la formule fermée

<details><summary>Indice 1</summary>

Fiche §7 : « Dériver une espérance par rapport à un paramètre de la loi », les deux formules du chemin gaussien, et l'exemple de l'ampoule (même méthode).

</details>
<details><summary>Indice 2</summary>

$\psi(\mu, \varepsilon) = (\mu + \sigma\varepsilon - c)^+$ : sa dérivée en $\mu$ est l'indicatrice $\mathbb{1}\{\varepsilon > z\}$, sa dérivée en $\sigma$ est $\varepsilon\,\mathbb{1}\{\varepsilon > z\}$. Pour la formule fermée, $(D - c)^+ = \sigma(\varepsilon - z)$ sur $\{\varepsilon > z\}$.

</details>
<details><summary>Indice 3</summary>

a) $\sigma\int_z^{+\infty}(u - z)\varphi(u)\,\mathrm{d}u$, avec $\int_z^{+\infty}u\,\varphi(u)\,\mathrm{d}u = \varphi(z)$ (une primitive de $u\varphi(u)$ est $-\varphi(u)$). b) $P(\varepsilon > 0{,}3)$. c) $\mathbb{E}[\varepsilon\,\mathbb{1}\{\varepsilon > z\}]$, par la même primitive. f) $\hat g_\mu$ ne prend que les valeurs 0 et 1.

</details>

### Ex M25b.13 — Une seule gaussienne pour la loi bimodale des temps de trajet par deux itinéraires : KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un itinéraire

<details><summary>Indice 1</summary>

Fiche §2 (les moments d'un mélange) et §7 (« Le sens de la KL », la propriété d'appariement des moments et sa démonstration).

</details>
<details><summary>Indice 2</summary>

Sous $q_1$, $\ln p(x) \approx \ln 0{,}7 + \ln q_1(x)$, donc $\ln q_1 - \ln p \approx -\ln 0{,}7$, une constante. $\mathbb{E}_p[\ln q(X)] = -\frac12\ln(2\pi s^2) - \frac{\mathbb{E}_p[(X - m)^2]}{2s^2}$ pour $q = \mathcal{N}(m, s^2)$.

</details>
<details><summary>Indice 3</summary>

a) Variance dans les groupes $0{,}7 \times 4 + 0{,}3 \times 6{,}25$, entre les groupes $0{,}7 \times 5{,}4^2 + 0{,}3 \times 12{,}6^2$. c) L'espérance d'une constante est la constante : écris $-\ln 0{,}7$ comme un logarithme positif. f) $\mathbb{E}_p[(X - 22)^2] = 72{,}715 + 5{,}4^2$. h) $\mathrm{KL}(p \,\|\, q) = -h(p) - \mathbb{E}_p[\ln q]$ : compare f) et g).

</details>

### Ex M25b.14 — Un code stochastique d'une source à trois symboles : posterior agrégé, information mutuelle, KL moyenne au prior décomposée en I(X ; Z) + KL(q(z) ‖ p(z)), puis le code qui s'effondre

<details><summary>Indice 1</summary>

Fiche §8 : le posterior agrégé, le théorème « KL moyenne au prior » et son exemple à deux symboles, l'effondrement du code.

</details>
<details><summary>Indice 2</summary>

$q(z) = \sum_xp(x)\,q(z \mid x)$ ; $I(X ; Z) = \sum_{x,z}p(x)\,q(z \mid x)\ln\frac{q(z \mid x)}{q(z)}$ ; $\mathrm{KL}(q(\cdot \mid x) \,\|\, p) = \sum_zq(z \mid x)\ln\frac{q(z \mid x)}{p(z)}$.

</details>
<details><summary>Indice 3</summary>

a) $q(z = 1) = 0{,}5 \times 0{,}85 + 0{,}3 \times 0{,}35 + 0{,}2 \times 0{,}15$. b) Pour $a$ : $0{,}85\ln\frac{0{,}85}{0{,}8} + 0{,}15\ln\frac{0{,}15}{0{,}2}$ ; fais de même pour $b$ et $c$. d) Six termes, chacun pondéré par $p(x)\,q(z \mid x)$, avec $q(z)$ de a) au dénominateur.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M25b.4 — Le pas M d'un mélange de gaussiennes : les poids N_k/n par un multiplicateur de Lagrange, les moyennes et les covariances comme maximum de vraisemblance pondéré

<details><summary>Indice 1</summary>

Fiche §4 : le théorème du pas M et son idée ; M13b (Lagrange), M18 ($\nabla\ln\det$, $\nabla\operatorname{tr}$) ; M25a §6 (le maximum de vraisemblance non pondéré, démontré en ∂ M25a.12 si tu l'as fait).

</details>
<details><summary>Indice 2</summary>

Développe $Q$ : la somme sur $i$ de $r_{ik}\ln\pi_k$ donne $N_k\ln\pi_k$. Dans $Q_k$, chaque donnée compte pour $r_{ik}$ : c'est le maximum de vraisemblance d'une gaussienne avec des poids, et $n$ devient $N_k$.

</details>
<details><summary>Indice 3</summary>

2. Les dérivées du lagrangien sont $\frac{N_k}{\pi_k} - \lambda$ ; somme les égalités $N_k = \lambda\pi_k$ sur $k$. Pour le maximum, compare $\sum N_k\ln\pi_k$ à sa valeur en $\hat\pi_k = \frac{N_k}{n}$ : la différence est $-n$ fois une KL. 3. Écris $\mathbf{x}_i - \boldsymbol{\mu} = (\mathbf{x}_i - \hat{\boldsymbol{\mu}}_k) + (\hat{\boldsymbol{\mu}}_k - \boldsymbol{\mu})$ et montre que les termes croisés sont nuls. 4. Pour le maximum, avec $\frac{\mathbf{S}_k}{N_k} = \mathbf{C}\mathbf{C}^\top$ et $\mathbf{B} = \mathbf{C}^\top\boldsymbol{\Lambda}_k\mathbf{C}$ de valeurs propres $b_j$ : $Q_k$ vaut une constante plus $\frac{N_k}{2}\sum_j(\ln b_j - b_j)$.

</details>

### Ex M25b.5 — L'ELBO en général : ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour un latent discret ou continu, la borne retrouvée par Jensen, et la forme E_q[ln p(x | z)] − KL(q ‖ p(z))

<details><summary>Indice 1</summary>

Fiche §5 : le théorème et son idée ; M06 et M25a §7 pour la positivité de la KL et l'inégalité de Jensen.

</details>
<details><summary>Indice 2</summary>

Pour tout $\mathbf{z}$ où $q(\mathbf{z}) > 0$ : $\ln p(\mathbf{x}) = \ln p(\mathbf{x}, \mathbf{z}) - \ln p(\mathbf{z} \mid \mathbf{x})$. Prends l'espérance sous $q$, puis ajoute et retire $\mathbb{E}_q[\ln q]$.

</details>
<details><summary>Indice 3</summary>

4. $\operatorname{ELBO}(q) = \mathbb{E}_q\big[\ln\frac{p(\mathbf{x}, \mathbf{Z})}{q(\mathbf{Z})}\big] \le \ln\mathbb{E}_q\big[\frac{p(\mathbf{x}, \mathbf{Z})}{q(\mathbf{Z})}\big]$, et cette espérance vaut au plus $p(\mathbf{x})$ (elle intègre $p(\mathbf{x}, \cdot)$ sur le support de $q$). Pour l'égalité, il faut que les **deux** inégalités en soient : quand une variable a une image par une fonction strictement concave d'espérance égale à l'image de l'espérance, elle est constante ; et la seconde demande que $q$ couvre tout le support de $p(\mathbf{x}, \cdot)$.

</details>

### Ex M25b.7 — L'EM comme montée par coordonnées de l'ELBO : le pas E maximise en q, le pas M en θ, d'où la monotonie ; et ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] pour la moyenne d'une composante

<details><summary>Indice 1</summary>

Fiche §5 : « L'EM, une montée par coordonnées » et « Le gradient de ln p(x) » ; ∂ M25b.5 et ∂ M25b.4.

</details>
<details><summary>Indice 2</summary>

Par ∂ M25b.5, $\operatorname{ELBO}(q, \boldsymbol{\theta}_t) = \ell(\boldsymbol{\theta}_t) - \sum_i\mathrm{KL}(q_i \,\|\, p(\cdot \mid \mathbf{x}_i, \boldsymbol{\theta}_t))$. Pour le gradient : $\nabla p = p\,\nabla\ln p$, puis la règle de Bayes.

</details>
<details><summary>Indice 3</summary>

1. Une somme de termes positifs ou nuls est nulle si et seulement si chacun l'est. 3. Le deuxième maillon de la chaîne n'utilise que $Q(\boldsymbol{\theta}_{t+1} \mid \boldsymbol{\theta}_t) \ge Q(\boldsymbol{\theta}_t \mid \boldsymbol{\theta}_t)$. 5. Seul le terme $j = k$ de $\ln p(\mathbf{x}_i, z = j)$ dépend de $\boldsymbol{\mu}_k$, de gradient $\boldsymbol{\Sigma}_k^{-1}(\mathbf{x}_i - \boldsymbol{\mu}_k)$ ; en un point fixe, $\boldsymbol{\mu}_k$ est sa propre moyenne pondérée.

</details>

### Ex M25b.8 — L'ACP probabiliste : la loi marginale N(μ, WWᵀ + σ²I), le posterior de z par le modèle linéaire gaussien, et W ou WR donnent la même loi

<details><summary>Indice 1</summary>

Fiche §6 : le modèle et l'idée du théorème ; M25a §4 (le conditionnement) et §5 (le modèle linéaire gaussien).

</details>
<details><summary>Indice 2</summary>

$(\mathbf{z}, \mathbf{x})$ est une image affine de $(\mathbf{z}, \boldsymbol{\varepsilon})$. $\operatorname{Cov}(\mathbf{x}, \mathbf{z}) = \mathbb{E}[(\mathbf{W}\mathbf{z} + \boldsymbol{\varepsilon})\mathbf{z}^\top]$. Pour l'identité, développe $\mathbf{W}^\top(\mathbf{W}\mathbf{W}^\top + \sigma^2\mathbf{I}_d)$.

</details>
<details><summary>Indice 3</summary>

3. $\mathbf{W}^\top\mathbf{W}\mathbf{W}^\top + \sigma^2\mathbf{W}^\top = (\mathbf{W}^\top\mathbf{W} + \sigma^2\mathbf{I}_k)\mathbf{W}^\top$, puis multiplie par $\mathbf{M}^{-1}$ à gauche et $\mathbf{C}^{-1}$ à droite. 4. $\mathbf{W}^\top\mathbf{W} = \mathbf{M} - \sigma^2\mathbf{I}_k$. 5. Le bloc croisé de la loi jointe est $\mathbf{W}\mathbf{R}$, pas $\mathbf{W}$.

</details>

### Ex M25b.11 — Dériver une espérance par rapport à un paramètre de la loi : l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré), la variance de l'estimateur à un tirage de ∂_σ E[e^X], et une indicatrice 1{X > c} pour laquelle l'échange échoue

<details><summary>Indice 1</summary>

Fiche §7 : le théorème, son idée et le contre-exemple discret ; M19 §7 pour la variance d'un estimateur sans biais à un tirage.

</details>
<details><summary>Indice 2</summary>

Le taux d'accroissement est $\frac1t\int_\theta^{\theta + t}\partial_\theta\psi(u, \xi)\,\mathrm{d}u$, donc majoré par $G(\xi)$. Pour $\mathbb{E}[\varepsilon\,e^{t\varepsilon}]$ : $-\frac{u^2}{2} + tu = -\frac{(u - t)^2}{2} + \frac{t^2}{2}$.

</details>
<details><summary>Indice 3</summary>

2. $G(\varepsilon) = \lvert\varepsilon\rvert\,e^{\lvert\mu\rvert + s_0\lvert\varepsilon\rvert}$ convient. Après la complétion du carré, $\mathbb{E}[\varepsilon\,e^{t\varepsilon}] = e^{t^2/2}$ fois la moyenne de $\mathcal{N}(t, 1)$. 3. Même calcul avec le moment d'ordre 2 de $\mathcal{N}(t, 1)$, et $t = 2\sigma$ pour $\hat g^2$. 4. Où se trouve le saut de $\mu \mapsto \mathbb{1}\{\mu + \sigma\varepsilon > c\}$ ? Pour la vraie dérivée, dérive $1 - \Phi\big(\frac{c - \mu}{\sigma}\big)$ en $\mu$ ; puis cherche l'étape de 1 qui suppose que $\psi(\cdot, \xi)$ ne saute pas.

</details>

### Ex M25b.15 — β comme multiplicateur de Lagrange : une mesure gaussienne codée avec du bruit, distorsion s² e^{−2I}, le lagrangien D + βI, et le code qui s'éteint quand β dépasse 2s²

<details><summary>Indice 1</summary>

Fiche §8 : « L'information mutuelle de deux variables continues », « Une mesure gaussienne bruitée » et « β est une pente » ; M25a §4 et §7.

</details>
<details><summary>Indice 2</summary>

$h(\mathcal{N}(m, \sigma^2)) = \frac12\ln(2\pi e\sigma^2)$, et $Z \sim \mathcal{N}(m, s^2 + v)$. La variance de $X$ sachant $Z$ vient du complément de Schur de la covariance de $(X, Z)$.

</details>
<details><summary>Indice 3</summary>

2. La covariance de $(X, Z)$ est $\begin{pmatrix} s^2 & s^2 \\ s^2 & s^2 + v \end{pmatrix}$ ; puis $e^{2I} = 1 + \frac{s^2}{v}$ pour éliminer $v$. 3. $\mathcal{L}'(I) = \beta - 2s^2e^{-2I}$ : regarde son signe en $I = 0$ et son sens de variation.

</details>

<a id="reflexion"></a>

## 📖 🗣️ 🔗 Lecture, explication et pont

### Ex M25b.16 — MML §8.4 et §8.5 : modèles probabilistes, inférence bayésienne, modèles à variables latentes, graphes orientés et d-séparation (survol), en anglais

<details><summary>Indice 1</summary>

Le guide de lecture de la fiche (avant le §1) ; garde la fiche §1 et §2 ouverte à côté du livre.

</details>
<details><summary>Indice 2</summary>

8.4.1 dit en une phrase en marge ce qui spécifie un modèle ; 8.4.2 oppose deux problèmes de calcul ; 8.4.3 sépare deux sortes de quantités cachées.

</details>
<details><summary>Indice 3</summary>

3. Pour les machines, l'intégrale de (8.25) devient une somme sur les trois machines. 5. Pour que $a$ et $c$ soient indépendants sachant $b$, mais pas sachant $b$ et $e$, il faut une collision dont $e$ est un descendant.

</details>

### Ex M25b.17 — MML ch. 11 : mélange de gaussiennes, responsabilités, mises à jour, EM et point de vue latent, en anglais ; refaire l'Exemple 11.1 avec ses propres données

<details><summary>Indice 1</summary>

Le guide de lecture de la fiche (avant le §3) ; la fiche §3 à §5 ouverte à côté.

</details>
<details><summary>Indice 2</summary>

Pour 3, regarde de quoi dépendent les $r_{nk}$ dans (11.17). Pour 4, relis « Ce qui est garanti » et « Avec une régularisation » (fiche §4). Pour 5, choisis des mesures assez proches pour que les responsabilités ne soient pas toutes 0 ou 1.

</details>
<details><summary>Indice 3</summary>

5. Avec une variance commune et des poids égaux, la constante $\ln\frac12 - \frac12\ln(2\pi\sigma^2)$ se simplifie dans les responsabilités : seuls comptent les carrés des écarts aux moyennes. Garde les variances et les poids, remplace seulement les moyennes par les moyennes pondérées, et recalcule les quatre log-sum-exp.

</details>

### Ex M25b.18 — MML §10.7 : l'ACP probabiliste, processus génératif, vraisemblance, loi jointe et posterior, en anglais

<details><summary>Indice 1</summary>

Le guide de lecture de la fiche (avant le §6) et l'encadré 📐 (notations de l'ACP probabiliste).

</details>
<details><summary>Indice 2</summary>

Une covariance croisée se définit par $\mathbb{E}[(\mathbf{x} - \mathbb{E}\mathbf{x})(\mathbf{z} - \mathbb{E}\mathbf{z})^\top]$. La forme de la fiche passe par l'identité de ∂ M25b.8.

</details>
<details><summary>Indice 3</summary>

3. Remplace $\mathbf{x} - \boldsymbol{\mu}$ par $\mathbf{B}\mathbf{z} + \boldsymbol{\epsilon}$ et sers-toi de l'indépendance du bruit. 5. (10.79) est une moyenne de valeurs propres rangées par ordre décroissant : compare-la à $\lambda_M$.

</details>

### Ex M25b.19 — Expliquer l'EM avec un bac de pièces venues de deux machines inconnues : deviner, réestimer, recommencer, sans jamais reculer

<details><summary>Indice 1</summary>

Fiche §4 : « L'idée : deviner les latents, puis réestimer » ; et la chaîne du §5 pour « sans jamais reculer ».

</details>
<details><summary>Indice 2</summary>

Le partage d'une pièce entre les deux machines, ce sont les responsabilités ; la réestimation, ce sont des moyennes où chaque pièce compte pour sa part.

</details>
<details><summary>Indice 3</summary>

Pour « jamais reculer » : chaque étape fait le meilleur choix possible pour ce que l'autre a fixé, donc aucune n'abîme l'explication. Termine par la dépendance au départ et les relances.

</details>

### Ex M25b.23 — Pont : l'ELBO de n mesures rangées en lignes, écrite « reconstruction moins KL au prior » E_q[ln p(x | z)] − KL(q ‖ π), en nats par mesure, et ce que gagne chaque terme quand q devient le posterior

<details><summary>Indice 1</summary>

Fiche §5 : « Deux autres lectures » (la forme reconstruction moins KL au prior) et le paragraphe sur $n$ observations.

</details>
<details><summary>Indice 2</summary>

Forme le tableau $(3, 2)$ des $\ln\mathcal{N}(x_i \mid \mu_k, \sigma_k^2)$ une fois pour toutes : la reconstruction est la somme de ses coefficients pondérés par ceux de $\mathbf{R}$, et la KL de la ligne $i$ est $\sum_kr_{ik}\ln\frac{r_{ik}}{\pi_k}$.

</details>
<details><summary>Indice 3</summary>

Première ligne du tableau : $-\frac12\ln(2\pi) - \frac{0{,}8^2}{2}$ et $-\frac12\ln(2\pi \times 2{,}25) - \frac{4{,}8^2}{4{,}5}$. e) Ajoute $\ln\pi_k$ à chaque coefficient, puis normalise chaque ligne en log. Divise toutes les sommes par 3.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M25b.E1 — « Pourquoi l'algorithme EM ne fait-il jamais baisser la vraisemblance, et vers quoi converge-t-il ? »

<details><summary>Indice 1</summary>

Fiche §5 (« L'EM, une montée par coordonnées ») et §4 (« Ce qui est garanti, et ce qui ne l'est pas », « Avec une régularisation »).

</details>
<details><summary>Indice 2</summary>

Construis la réponse autour de la chaîne $\ell(\boldsymbol{\theta}_{t+1}) \ge \operatorname{ELBO}(q_t, \boldsymbol{\theta}_{t+1}) \ge \operatorname{ELBO}(q_t, \boldsymbol{\theta}_t) = \ell(\boldsymbol{\theta}_t)$, dite avec des mots.

</details>
<details><summary>Indice 3</summary>

Pour la convergence : point stationnaire, maximum local, singularités d'un mélange (pas de maximum global), plusieurs initialisations, vitesse quand les composantes se recouvrent.

</details>

<a id="notebook"></a>

## Notebook

### M25b.20 — Les responsabilités d'un mélange de gaussiennes, calculées en log (le pas E) : `gmm_e_step`

<details><summary>Indice 1</summary>

Fiche §3, « Les responsabilités, calculées en log », et la docstring de `gmm_e_step` : les formes, les poids valides (positifs, de somme 1 à $10^{-9}$ près) et les refus.

</details>
<details><summary>Indice 2</summary>

Convertis avec `np.asarray(…, dtype=float)` et contrôle les formes avant tout calcul. `a = np.log(weights) + np.column_stack([mvn_logpdf(X, means[k], covs[k]) for k in range(K)])`, de forme $(n, K)$ ; ton `mvn_logpdf` refuse déjà une covariance qui n'est pas définie positive.

</details>
<details><summary>Indice 3</summary>

Le log-sum-exp de chaque ligne : `m = a.max(axis=1, keepdims=True)` puis `lse = m + np.log(np.exp(a - m).sum(axis=1, keepdims=True))` ; rends `np.exp(a - lse)`. Ensuite, dans le notebook : a) `mymath.latent.gmm_e_step(X, [0.45, 0.55], [[47.0], [51.0]], [[[1.0]], [[2.5]]])` avec `X` de forme `(4, 1)` ; b) `np.vstack([X, [[120.0]]])` et `np.isnan(R).any()` ; c) trois composantes, `covs = [[[1.0]], [[1.0]], [[4.0]]]`.

</details>

### M25b.21 — Le pas M d'un mélange de gaussiennes : poids, moyennes et covariances pondérées, avec une régularisation : `gmm_m_step`

<details><summary>Indice 1</summary>

Fiche §4, l'algorithme EM (le pas M), et la docstring de `gmm_m_step` : les refus de `resp` (une colonne de zéros) et de `reg` (un booléen, une valeur négative ou non finie).

</details>
<details><summary>Indice 2</summary>

`N = resp.sum(axis=0)`, `weights = N / n`, `means = (resp.T @ X) / N[:, None]`. Pour chaque $k$, les écarts aux **nouvelles** moyennes, pondérés par la colonne $k$ de `resp`, puis divisés par `N[k]`.

</details>
<details><summary>Indice 3</summary>

`D = X - means[k]` puis `covs[k] = (resp[:, k, None] * D).T @ D / N[k] + reg * np.eye(d)`. Pour refuser un booléen : `isinstance(reg, (bool, np.bool_))` avant `isinstance(reg, numbers.Real)`. Ensuite : b) compare à `X[:2].mean()`, `X[:2].var()` (et de même pour les deux dernières) ; d) appelle `mymath.latent.gmm_e_step` dans un `try` qui attrape `ValueError`.

</details>

### M25b.22 — La log-vraisemblance d'un mélange de gaussiennes, et son ELBO pour des responsabilités quelconques : `gmm_log_likelihood`, `gmm_elbo`

<details><summary>Indice 1</summary>

Fiche §3 (la log-vraisemblance) et §5 (la phrase sur `gmm_elbo` : la convention $0\ln 0 = 0$) ; les docstrings, qui disent que `gmm_elbo` accepte une colonne de zéros dans `resp`.

</details>
<details><summary>Indice 2</summary>

Le même tableau `a` que dans `gmm_e_step` ; `gmm_log_likelihood` rend la somme des log-sum-exp des lignes, en `float`. Pour l'ELBO, ne calcule jamais `np.log(0)` : remplace d'abord les zéros de `resp` par 1 dans le logarithme.

</details>
<details><summary>Indice 3</summary>

`safe = np.where(resp > 0, resp, 1.0)` puis `float(np.where(resp > 0, resp * (a - np.log(safe)), 0.0).sum())`. Ensuite : b) `mymath.latent.gmm_elbo(X, R, w, m, C) / 3`, puis la même chose avec `R = mymath.latent.gmm_e_step(X, w, m, C)` ; d) l'écart vaut la somme des $-\ln r_{ik}$ des composantes choisies par les responsabilités dures.

</details>

### M25b.24 — `scipy.linalg.subspace_angles` et `np.linalg.eigh` : les angles principaux de M25b.10, et l'ACP probabiliste de mesures par leurs valeurs propres, contre la vraisemblance de `mvn_logpdf`

<details><summary>Indice 1</summary>

`help(scipy.linalg.subspace_angles)` : lis la section *Returns*. Fiche §6 pour Tipping et Bishop.

</details>
<details><summary>Indice 2</summary>

Les bases se passent en **colonnes** : `A = np.column_stack([a1, a2])`, de forme `(4, 2)`. `np.linalg.eigh(S)` rend les valeurs propres par ordre croissant et les vecteurs propres en colonnes : retourne les deux avec `[::-1]` et `[:, ::-1]`.

</details>
<details><summary>Indice 3</summary>

c) `S = np.cov(X, rowvar=False, bias=True)`, `lam, U = np.linalg.eigh(S)`, puis (après retournement) `s2 = lam[1:].mean()`, `w = U[:, 0] * np.sqrt(lam[0] - s2)`, et `mymath.gaussian.mvn_logpdf(X, X.mean(axis=0), np.outer(w, w) + s2 * np.eye(3)).mean()`. d) La moyenne jointe `np.r_[0.0, mu]`, la covariance `J = np.zeros((4, 4))` remplie par blocs (`J[0, 0] = 1`, `J[0, 1:] = J[1:, 0] = w`, `J[1:, 1:] = C`), puis `mymath.gaussian.condition_gaussian(np.r_[0.0, mu], J, [1, 2, 3], [15, 12, 15])`.

</details>

### M25b.25 — Prédire ce que devient la log-vraisemblance quand une composante centrée sur un point se resserre (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis avec une régularisation, et mesurer

<details><summary>Indice 1</summary>

Fiche §3, « Une vraisemblance qui n'est pas bornée » : un seul terme de la log-vraisemblance change quand $\sigma_1$ diminue. Fais tes prédictions avant d'ouvrir l'indice 3.

</details>
<details><summary>Indice 2</summary>

Écris la densité de la composante 1 en son propre centre, $\mathcal{N}(46{,}0 \mid 46{,}0, \sigma_1^2)$, en fonction de $\sigma_1$ ; pour la régularisation, la variance utilisée devient $\sigma_1^2 + 0{,}01$.

</details>
<details><summary>Indice 3</summary>

Pour mesurer, une boucle sur `s1` dans `(1e-1, 1e-3, 1e-6)` et sur `reg` dans `(0.0, 0.01)` : `mymath.latent.gmm_log_likelihood(X, [0.48, 0.52], [[46.0], [50.57]], [[[s1 ** 2 + reg]], [[2.36]]])`, puis `np.diff` des trois valeurs de chaque série.

</details>

### M25b.26 — L'EM sur des longueurs de poissons de trois cohortes : la log-vraisemblance et l'ELBO après chaque demi-pas, sans régularisation, plusieurs initialisations et des maxima locaux

<details><summary>Indice 1</summary>

Fiche §5, « L'EM, une montée par coordonnées » : quelle loi $q$ utilise-t-on après un pas M, et après un pas E ?

</details>
<details><summary>Indice 2</summary>

Après un pas M, les responsabilités ne changent pas encore : l'ELBO se calcule avec les anciennes responsabilités et les nouveaux paramètres. Après un pas E, avec les nouvelles responsabilités ; elle égale alors la log-vraisemblance.

</details>
<details><summary>Indice 3</summary>

Squelette : `R = mymath.latent.gmm_e_step(X, w, m, C)` ; on ajoute $\ell$ et l'ELBO ; puis, `n_iter` fois : `w, m, C = mymath.latent.gmm_m_step(X, R)`, on ajoute $\ell$ et `gmm_elbo(X, R, w, m, C)`, puis `R = gmm_e_step(X, w, m, C)`, on ajoute $\ell$ et `gmm_elbo(X, R, w, m, C)`. Les covariances de départ : `np.full((3, 1, 1), X.var())`. Pour a), regarde `np.diff(elbo)` contre `-1e-9 * (1 + np.abs(elbo[:-1]))`.

</details>

### M25b.27 — Une gaussienne ajustée à un mélange bimodal par KL(p ‖ q) puis par KL(q ‖ p) : les deux courbes, et les deux minima de la KL inverse

<details><summary>Indice 1</summary>

Fiche §7, « Le sens de la KL » ; ✏️ M25b.13 pour $q_\star$, $q_1$ et $q_2$.

</details>
<details><summary>Indice 2</summary>

Sur la grille `x = np.linspace(-30, 100, 260001)`, $\ln p(x)$ = `scipy.special.logsumexp(np.log(weights) + scipy.stats.norm.logpdf(x[:, None], means, np.sqrt(variances)), axis=1)`. Pour $q = \mathcal{N}(m, s^2)$ : $\mathrm{KL}(q \,\|\, p)$ = `np.trapezoid(q * (lq - lp), x)` et $\mathrm{KL}(p \,\|\, q)$ = `np.trapezoid(p * (lp - lq), x)`.

</details>
<details><summary>Indice 3</summary>

Les minima locaux d'une courbe `y` sur la grille `ms` : les indices `i` où `y[i] < y[i - 1]` et `y[i] < y[i + 1]`. Dessine sur les axes reçus (`ax_density.plot(…)`, `ax_kl.plot(…)`, `ax_density.legend()`), sans `plt.figure` ni `plt.subplots` dans la fonction : la cellule d'appel crée `fig, (ax1, ax2) = plt.subplots(1, 2)`. Pour `scipy.optimize.minimize`, optimise $(m, \ln s^2)$ pour que la variance reste positive.

</details>

### M25b.28 — Chasse à l'erreur : des responsabilités sans log qui donnent 0/0, un pas M qui divise par n au lieu de N_k, et une ELBO sans l'entropie de q

<details><summary>Indice 1</summary>

Les trois ⚠️ des §3, §4 et §5 de la fiche. Pour chaque vérification, demande-toi : dans quel cas l'erreur ne change-t-elle rien ?

</details>
<details><summary>Indice 2</summary>

(1) Calcule $e^{-(120 - 47)^2/2}$ en flottants. (2) Que vaut $N_1$ quand il n'y a qu'une composante ? (3) De quel signe est l'entropie d'une loi discrète, et que vaut l'ELBO correcte au posterior ?

</details>
<details><summary>Indice 3</summary>

(1) Passe en log : `a = np.log(weights) - np.log(sds * np.sqrt(2 * np.pi)) - (x[:, None] - means) ** 2 / (2 * sds ** 2)`, puis un log-sum-exp par ligne. (2) Divise les variances par `N` au lieu de `n`. (3) Ajoute `- resp * np.log(resp)`, avec la convention $0\ln 0 = 0$. d) est l'opposé de la somme des entropies des lignes du posterior.

</details>

### M25b.29 — Un test de propriété : sur des mélanges tirés au hasard, ELBO ≤ log-vraisemblance, égalité après le pas E, et un EM sans régularisation (reg = 0) qui ne descend jamais (à une tolérance près)

<details><summary>Indice 1</summary>

Fiche §4 et §5 (ce qui est garanti, et pourquoi la régularisation casse la garantie) ; ton 🔬 M25b.26 fait déjà un EM demi-pas par demi-pas.

</details>
<details><summary>Indice 2</summary>

Une erreur d'arrondi relative sur une somme de $n$ termes est de l'ordre de $n$ fois $10^{-16}$. Compte les échecs dans un dictionnaire au lieu de lever une exception, pour pouvoir lancer le test sur des pas faux.

</details>
<details><summary>Indice 3</summary>

Squelette : `counts = {"bound": 0, "gap": 0, "descent": 0}` ; à chaque itération, `R = mymath.latent.gmm_e_step(...)`, `ll = mymath.latent.gmm_log_likelihood(...)`, un tableau aléatoire `rng.dirichlet(np.ones(K), size=n)`, les deux comparaisons à `tol * (1 + abs(ll))`, puis `w, m, C = m_step(X, R)` et la comparaison des ELBO avant et après chaque demi-pas. Dans la boucle sur les 40 mélanges, mets l'appel dans un `try` qui compte les `ValueError` à part.

</details>

### M25b.30 — Défi : retrouver trois populations de mesures en dimension 2 par l'EM, sous un seuil de log-vraisemblance moyenne sur des mesures de test

<details><summary>Indice 1</summary>

Fiche §3 (singularités et `reg`) et §4 (plusieurs initialisations) ; le 💻 du §4 décrit ce que fait `GaussianMixture`.

</details>
<details><summary>Indice 2</summary>

Une petite régularisation (de l'ordre de $10^{-6}$ à $10^{-2}$) évite qu'une composante s'effondre ; garde, sur plusieurs départs, celui qui a la meilleure log-vraisemblance **d'entraînement**, jamais celle de test.

</details>
<details><summary>Indice 3</summary>

Squelette : `rng = np.random.default_rng(seed)` ; pour chaque départ, `m = X[rng.choice(n, K, replace=False)]`, `C = np.tile(np.cov(X, rowvar=False, bias=True) + reg * np.eye(2), (K, 1, 1))`, `w = np.full(K, 1 / K)` ; puis la boucle `gmm_e_step` / `gmm_m_step(X, R, reg=reg)` jusqu'à ce que `abs(ll - ll_old) < 1e-8 * abs(ll)`. Pour l'ellipse à 90 % d'une composante : le cercle de rayon $c = \sqrt{2\ln 10}$ envoyé par $\boldsymbol{\varepsilon} \mapsto \boldsymbol{\mu}_k + \mathbf{L}_k\boldsymbol{\varepsilon}$ (M25a §3).

</details>
