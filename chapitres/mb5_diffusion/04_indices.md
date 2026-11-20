# MB5 · Les maths de la diffusion — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB5.Q1 — Une récurrence linéaire gaussienne : quelle moyenne, quelle variance, quand une loi stationnaire, et combien de pas pour oublier le départ ?

<details><summary>Indice 1</summary>

Fiche §1 : « Deux moments qui suivent le pas » et « La loi stationnaire d'un processus autorégressif » (le théorème et ses cas limites).

</details>
<details><summary>Indice 2</summary>

Depuis un départ connu, $m_0 = x_0$ et $v_0 = 0$ ; puis $m_t = am_{t-1}$ et $v_t = a^2v_{t-1} + b^2$. La loi stationnaire existe si $\lvert a\rvert < 1$, et sa variance est le point fixe $v_\infty = \frac{b^2}{1 - a^2}$. Chaque pas multiplie l'écart de moyenne à la loi stationnaire par $a$, et l'écart de variance par $a^2$.

</details>
<details><summary>Indice 3</summary>

1. $m_1 = -0{,}5 \times 6$ et $v_1 = 2^2$ ; recommence une fois. 2. $b^2 = 4$ et $a^2 = 0{,}25$. 3. Pour chaque valeur, $a^2$ est-il plus petit que 1 ? Sinon, que fait $v_t$ ? 4. Avec $a = 1$, $v_t = v_{t-1} + b^2$. 5. Le premier $t$ tel que $0{,}5^t \le 10^{-3}$, puis tel que $0{,}25^t \le 10^{-3}$ ; $2^{10} = 1\,024$.

</details>

### MB5.Q2 — Le pont et les couplages : où l'incertitude est la plus grande, ce que fixent les lois marginales et ce qu'elles laissent libre

<details><summary>Indice 1</summary>

Fiche §2 : « Le pont d'une marche aléatoire » (la propriété, et où la variance est maximale) et « Mêmes lois à chaque instant, d'autres trajectoires » (les trois façons de simuler, le lemme).

</details>
<details><summary>Indice 2</summary>

Des pas de même variance $0{,}4$ donnent $V_s = 0{,}4\,s$. Sachant $x_0$ et $x_T$, $x_s$ a la moyenne $x_0 + \frac{V_s}{V_T}(x_T - x_0)$ et la variance $\frac{V_s(V_T - V_s)}{V_T}$, maximale quand $V_s = \frac{V_T}{2}$. Le lemme : $\sqrt{\omega^2 - \sigma^2}\,U + \sigma Z$ suit $\mathcal{N}(0, \omega^2)$ pour $0 \le \sigma \le \omega$. Pour la marche, $\operatorname{Cov}(W_s, W_t) = \mathbb{V}(W_s)$ quand $s < t$.

</details>
<details><summary>Indice 3</summary>

1. $V_{10} = 4$ : pour quel $s$ a-t-on $V_s = 2$ ? 2. $V_4 = 1{,}6$ : la moyenne $\frac{1{,}6}{4} \times 5$, la variance $\frac{1{,}6 \times 2{,}4}{4}$. 3. La variance $4 + 5$, donc $\omega = 3$. 4. Pense aux trois façons de simuler de la fiche. 5. $X_4 = 2X_1$ ; pour la marche, $\frac{\operatorname{Cov}(W_1, W_4)}{\sqrt{\mathbb{V}(W_1)\,\mathbb{V}(W_4)}}$.

</details>

### MB5.Q3 — Signal et bruit : SNR, cotes, logit et décibels, et ce qu'un changement d'échelle ne change pas

<details><summary>Indice 1</summary>

Fiche §3 : « Le rapport signal sur bruit » (les définitions, la cote, le logit, les décibels) et le paragraphe « Ce qu'une échelle ne change pas ».

</details>
<details><summary>Indice 2</summary>

$\operatorname{SNR} = \frac{a^2}{b^2}$, $\gamma = \frac{\operatorname{SNR}}{1 + \operatorname{SNR}}$ et $\operatorname{SNR} = \frac{\gamma}{1 - \gamma}$, la cote de $\gamma$ ; $\operatorname{logit}\gamma = \ln\operatorname{SNR}$. Un seuil de $d$ dB est un SNR de $10^{d/10}$.

</details>
<details><summary>Indice 3</summary>

1. $\frac{1{,}8^2}{0{,}5^2} = \frac{3{,}24}{0{,}25}$, puis $\frac{r}{1 + r}$. 2. $\frac{0{,}96}{0{,}04}$, puis son logarithme népérien. 3. Que deviennent $a$ et $b$ ? 4. $10^{1{,}5}$, puis $\frac{r}{1 + r}$. 5. Essaie un SNR de 1, puis de 2.

</details>

### MB5.Q4 — Ce que la MSE apprend : une moyenne conditionnelle, pas la valeur la plus probable ; et ce qu'apprennent la MAE et la log-loss

<details><summary>Indice 1</summary>

Fiche §4 : « La meilleure prédiction quadratique » et « Une moyenne n'est pas la valeur la plus probable » (la MAE, la log-loss).

</details>
<details><summary>Indice 2</summary>

La MSE est minimale pour $\mathbb{E}[Y \mid X]$, et son minimum est $\mathbb{V}(Y \mid X)$ pour un profil fixé. La MAE apprend une médiane conditionnelle, la log-loss une probabilité a posteriori. Sur un échantillon, on prend la loi empirique.

</details>
<details><summary>Indice 3</summary>

1. $0{,}7 \times 10 + 0{,}3 \times 40$. 2. $0{,}7 \times (10 - \text{la moyenne})^2 + 0{,}3 \times (40 - \text{la moyenne})^2$. 3. $P(Y \le 10) = 0{,}7$ : la moitié de la masse est-elle atteinte en 10 ? 4. Rappel de M27 §5. 5. Le théorème du §4, sous la loi empirique (∂ MB5.11, question 3).

</details>

### MB5.Q5 — Le score en x : où il pointe, la constante qu'il ignore, et ce que dit la formule de Tweedie

<details><summary>Indice 1</summary>

Fiche §5 : « Le score en x » (ses quatre propriétés) et « La formule de Tweedie ».

</details>
<details><summary>Indice 2</summary>

Pour $\mathcal{N}(\mu, \sigma^2)$, $s(x) = -\frac{x - \mu}{\sigma^2}$. $\ln(Cf) = \ln C + \ln f$, et une constante a une dérivée nulle. Tweedie : $\mathbb{E}[n \mid y] = -b\,s_Y(y)$ et $\mathbb{E}[x \mid y] = \frac{y + b^2s_Y(y)}{a}$.

</details>
<details><summary>Indice 3</summary>

1. $\sigma^2 = 4$ : $-\frac{7 - 3}{4}$ et $-\frac{1 - 3}{4}$. 2. La dérivée de $-\frac{x^4}{4}$, en 2. 3. $s = \frac{p'}{p}$, et que vaut $p'$ en un mode ? 4. $a = 2$, $b = 0{,}5$, $b^2 = 0{,}25$ ; contrôle : $a\,\mathbb{E}[x \mid y] + b\,\mathbb{E}[n \mid y] = 3$. 5. Dans la preuve (∂ MB5.12), qu'est-ce qui doit être gaussien : le signal ou le bruit ?

</details>

### MB5.Q6 — L'ELBO d'une chaîne : quels termes dépendent du modèle, quelle KL compare quoi, et ce que devient une KL entre gaussiennes de même variance

<details><summary>Indice 1</summary>

Fiche §6 : « Une chaîne de latents » (le théorème et la lecture des termes) et « Quand les pas sont gaussiens de même variance ».

</details>
<details><summary>Indice 2</summary>

La KL finale compare $q(z_T \mid x)$ à $p(z_T)$ ; chaque terme du milieu compare le pas retour du modèle au pas retour qui connaît $x$. Deux gaussiennes de même variance $\sigma^2$ ont la KL $\frac{(\mu_q - \mu_p)^2}{2\sigma^2}$. Et $\operatorname{ELBO} = \ln p(x) - \mathrm{KL}\big(q(z_{1:T} \mid x) \,\|\, p(z_{1:T} \mid x)\big)$.

</details>
<details><summary>Indice 3</summary>

1. Lequel des trois termes ne contient aucune loi que le modèle retour choisit ? 2. La loi a posteriori du processus aller, sachant $z_t$ et $x$. 3. $\frac{(2{,}2 - 1{,}7)^2}{2 \times 0{,}5}$. 4. Quel est le signe d'une KL ? 5. $\sigma^2$ est au dénominateur.

</details>

### MB5.Q7 — Guider : interpoler ou extrapoler, la différence de deux scores, et quand un produit de puissances n'est plus une densité

<details><summary>Indice 1</summary>

Fiche §7 : « Interpoler ou extrapoler », « Bayes en logarithmes : une combinaison de scores » et « Deux densités gaussiennes » (la précision $\lambda(w)$ et la propriété).

</details>
<details><summary>Indice 2</summary>

$(1 + w)\,y_c - w\,y_u = y_c + w\,(y_c - y_u)$ : deux coefficients de somme 1, tous deux positifs ou nuls exactement quand $w \in [-1, 0]$. La loi guidée de deux gaussiennes existe tant que $\lambda(w) = \frac{1 + w}{\sigma_c^2} - \frac{w}{\sigma_u^2} > 0$.

</details>
<details><summary>Indice 3</summary>

1. $1 + w = 0{,}7$ et $-w = 0{,}3$. 2. $y_c + 1{,}25\,(y_c - y_u)$ : de quel côté de $y_c$ ? 3. Bayes en logarithmes, $\ln p(x \mid c) = \ln p(c \mid x) + \ln p(x) - \ln p(c)$, puis dérive en $x$. 4. $\lambda(w) = \frac{1 + w}{4} - w$ : résous $\lambda(w) > 0$. 5. Écris $\lambda(w) = \frac{1}{\sigma_c^2} + w\big(\frac{1}{\sigma_c^2} - \frac{1}{\sigma_u^2}\big)$ : quel est le signe de la parenthèse ?

</details>

### MB5.Q8 — Euler, point milieu et chemin droit : ce que coûte un pas, l'ordre de l'erreur, et le sens du temps

<details><summary>Indice 1</summary>

Fiche §8 : « La méthode d'Euler, dans les deux sens du temps » et « Le point milieu » (le paragraphe « À nombre d'évaluations égal ») ; §9 : « Des données gaussiennes » (un seul pas d'Euler depuis $s = 1$).

</details>
<details><summary>Indice 2</summary>

Euler lit le champ une fois par pas, le point milieu deux fois. Une erreur d'ordre $p$ est de l'ordre de $h^p$, donc de $N^{-p}$. Le pas vaut $h = \frac{t_N - t_0}{N}$, négatif pour remonter le temps. En $s = 1$, $x_s$ ne dit rien de $x_0$.

</details>
<details><summary>Indice 3</summary>

1. $\frac{12}{1}$ et $\frac{12}{2}$. 2. Compare $\frac h2$ à $h$, puis $\big(\frac h2\big)^2$ à $h^2$. 3. Si l'erreur vaut $CN^{-p}$, son logarithme vaut $\ln C - p\ln N$. 4. $\frac{2 - 5}{6}$. 5. $v(z, 1) = z - m$ et $h = -1$ : calcule $z + h\,v(z, 1)$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### MB5.R1 — Sommes et images affines de gaussiennes, produit de densités et modèle linéaire gaussien (M25a)

<details><summary>Indice 1</summary>

M25a : sommes et images affines de gaussiennes, produit de deux densités, modèle linéaire gaussien ; MML §6.5.3 (relecture, d'après le guide de lecture de la fiche).

</details>
<details><summary>Indice 2</summary>

Pour des gaussiennes indépendantes, $cX + dY$ a la moyenne $c\mu_X + d\mu_Y$ et la variance $c^2v_X + d^2v_Y$. Dans un produit de deux densités gaussiennes, les précisions s'ajoutent, et la moyenne est pondérée par les précisions. Pour $y = x + w$, le gain vaut $\frac{\mathbb{V}(x)}{\mathbb{V}(x) + \mathbb{V}(w)}$.

</details>
<details><summary>Indice 3</summary>

1. Pour $2X - Y$ : la moyenne $2 \times 5 - (-1)$, la variance $4 \times 2 + 5$. 2. $\frac1v = \frac12 + \frac16$, puis $m = v\big(\frac12 + \frac46\big)$. 3. Le gain $\frac34$ : la moyenne $10 + \frac34 \times (15 - 10)$, la variance $3 \times \big(1 - \frac34\big)$. 4. Essaie $Y = SX$, avec un signe $S = \pm1$ indépendant de $X$. 5. La moyenne et la covariance d'une image affine.

</details>

### MB5.R2 — Espérance et variance conditionnelles, lois totales, et l'ELBO d'un latent (M25b)

<details><summary>Indice 1</summary>

M25b §2 (lois totales), §3 (responsabilités) et §5 (ELBO d'un latent) ; M26 §3 (propriété de la tour).

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[X] = \sum_kP(Z = k)\,\mathbb{E}[X \mid Z = k]$ et $\mathbb{V}(X) = \mathbb{E}[\mathbb{V}(X \mid Z)] + \mathbb{V}(\mathbb{E}[X \mid Z])$. $\operatorname{ELBO} = \ln p(x) - \mathrm{KL}\big(q \,\|\, p(z \mid x)\big)$. Les responsabilités sont la softmax des logarithmes.

</details>
<details><summary>Indice 3</summary>

1. $\mathbb{E}[\mathbb{V}(X \mid Z)] = 0{,}7 \times 1 + 0{,}3 \times 4$ ; $\mathbb{V}(\mathbb{E}[X \mid Z]) = 0{,}7 \times 0{,}3 \times (7 - 2)^2$. 2. La tour. 3. $-2{,}1 - 0{,}4$. 4. Quand une KL est-elle nulle ? 5. $r_2 = \frac{1}{1 + e^{-3{,}2 - (-1{,}7)}}$.

</details>

### MB5.R3 — Un pas d'Euler (M20), la loi stationnaire d'une chaîne finie (M26) et la cote d'une probabilité (R6)

<details><summary>Indice 1</summary>

M20 §6 (la méthode d'Euler et sa stabilité), M26 §2 (loi stationnaire) et R6 §7 (cote, logit).

</details>
<details><summary>Indice 2</summary>

Un pas d'Euler : $x + h\,f(x)$. Pour $x' = -2x + 1$, chaque pas multiplie l'écart au point fixe $0{,}5$ par $1 - 2h$. Pour une chaîne à deux états, la loi stationnaire équilibre les flux : $\pi_1P_{12} = \pi_2P_{21}$. La cote est $\frac{p}{1 - p}$, le logit son logarithme, et $p = \frac{\text{cote}}{1 + \text{cote}}$.

</details>
<details><summary>Indice 3</summary>

1. $f(3) = -5$. 2. $1 - 2 \times 1{,}5 = -2$ : l'écart $2{,}5$ devient… 3. $\pi_1 \times 0{,}21 = \pi_2 \times 0{,}42$ et $\pi_1 + \pi_2 = 1$. 4. $\frac{0{,}12}{0{,}88} = \frac{3}{22}$, puis $\ln$. 5. $\frac{7}{1 + 7}$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB5.1 — L'anomalie de température d'un lac, un processus autorégressif d'ordre 1 : sa loi dans k jours sachant aujourd'hui, sa loi stationnaire, le nombre de jours pour oublier le départ, et sa loi sachant un jour passé

<details><summary>Indice 1</summary>

Fiche §1 : « Deux moments qui suivent le pas » et « La loi stationnaire d'un processus autorégressif » (le théorème, point 1 : sachant un instant passé).

</details>
<details><summary>Indice 2</summary>

$x_0$ est mesuré : $m_0 = 2{,}5$ et $v_0 = 0$. Puis $m_t = 0{,}88\,m_{t-1}$ et $v_t = 0{,}88^2v_{t-1} + 0{,}35^2$. La variance stationnaire est $\frac{b^2}{1 - a^2}$. Pour d), compare $m_k = 2{,}5 \times 0{,}88^k$ au dixième de $\sqrt{v_\infty}$. Pour e), repars de $x_{20}$, connu, pour cinq jours.

</details>
<details><summary>Indice 3</summary>

$a^2 = 0{,}7744$ et $b^2 = 0{,}1225$. a) $m_1 = 0{,}88 \times 2{,}5$ et $v_1 = b^2$. b) $v_2 = 0{,}7744 \times 0{,}1225 + 0{,}1225 = 0{,}217364$, puis $v_3$ de la même façon ; $m_3 = 0{,}88^3 \times 2{,}5$. c) $\frac{0{,}1225}{0{,}2256}$. d) Résous $2{,}5 \times 0{,}88^k < 0{,}1\sqrt{v_\infty}$ par les logarithmes, prends l'entier juste au-dessus, et vérifie-le, ainsi que l'entier d'avant. e) La moyenne $0{,}88^5 \times (-1{,}4)$, la variance $v_\infty\,(1 - 0{,}88^{10})$.

</details>

### Ex MB5.2 — La survie d'une ruche à six mois de risques différents : le produit exact, son logarithme, le risque mensuel constant équivalent, et l'encadrement par deux exponentielles

<details><summary>Indice 1</summary>

Fiche §1 : « Les produits cumulés » (la survie, le risque, la propriété d'encadrement et le risque constant équivalent).

</details>
<details><summary>Indice 2</summary>

La colonie survit à chaque mois avec la probabilité $1 - h_k$ : $P = \prod_k(1 - h_k)$. Le logarithme d'un produit est la somme des logarithmes. Le risque constant équivalent vérifie $(1 - \bar h)^6 = P$. L'encadrement $e^{-H - \sum_kh_k^2} \le P \le e^{-H}$ demande $h_k \le \frac12$ pour chaque mois.

</details>
<details><summary>Indice 3</summary>

a) $0{,}99 \times 0{,}97 \times 0{,}93 \times 0{,}88 \times 0{,}86 \times 0{,}93$. b) La somme des six $\ln(1 - h_k)$, tous négatifs. c) $1 - \bar h = P^{1/6} = e^{\ln P/6}$. d) $H = 0{,}44$. e) $\sum_kh_k^2 = 0{,}0001 + 0{,}0009 + \cdots$ ; vérifie à la fin que $P$ est bien entre tes deux bornes.

</details>

### Ex MB5.3 — Un phoque balisé entre deux relevés : sa loi à une heure intermédiaire (le pont d'une marche aléatoire) ; puis des scénarios de position aux mêmes lois à chaque heure, tirés avec un seul nombre au hasard ou avec un bruit frais, et leur corrélation

<details><summary>Indice 1</summary>

Fiche §2 : « Le pont d'une marche aléatoire » (avec des pas de variances différentes, comme la montre) et « Mêmes lois à chaque instant, d'autres trajectoires » (les corrélations, le lemme).

</details>
<details><summary>Indice 2</summary>

Calcule d'abord les variances cumulées $V$ depuis 8 h, heure par heure. Le pont : la moyenne $x_0 + \frac{V_s}{V_T}(x_T - x_0)$, la variance $\frac{V_s(V_T - V_s)}{V_T}$, maximale là où $V_s$ est le plus proche de $\frac{V_T}{2}$. Une corrélation est $\frac{\operatorname{Cov}}{\sqrt{V_sV_t}}$ ; pour la marche, $\operatorname{Cov} = V_s$ ($s < t$) ; pour le bruit frais, seul $U$ est commun aux deux heures.

</details>
<details><summary>Indice 3</summary>

De 9 h à 16 h : $V = 2, 4, 6, 6{,}5, 7, 7{,}5, 8, 8{,}5$. a) $V_s = 6$ et $V_T = 8{,}5$. b) Quelle heure entière a le $V_s$ le plus proche de $4{,}25$ ? Puis $\frac{V_s(8{,}5 - V_s)}{8{,}5}$. c) $V = 4$ à 10 h et $V = 7$ à 13 h : $\frac{4}{\sqrt{4 \times 7}}$. d) $\operatorname{Cov} = \sqrt{(4 - 1{,}5)(7 - 1{,}5)}$, à diviser par $\sqrt{4 \times 7}$.

</details>

### Ex MB5.4 — Une voix mêlée à un bruit de fond : SNR, part de variance de la voix, logit et décibels, puis la voix retrouvée à partir d'une estimation du bruit, et l'erreur amplifiée

<details><summary>Indice 1</summary>

Fiche §3 : « Le rapport signal sur bruit » (les définitions, un seuil en décibels) et « Trois cibles qui portent la même information » (la propriété).

</details>
<details><summary>Indice 2</summary>

$\operatorname{SNR} = \frac{a^2}{b^2}$, $\gamma = \frac{\operatorname{SNR}}{1 + \operatorname{SNR}}$, $\operatorname{logit}\gamma = \ln\operatorname{SNR}$, $10\log_{10}\operatorname{SNR}$ dB ; un seuil de $d$ dB est un SNR $r = 10^{d/10}$, de part $\frac{r}{1 + r}$. Connaissant $y$, $x = \frac{y - bn}{a}$ : remplace $n$ par $\hat n$.

</details>
<details><summary>Indice 3</summary>

a) $\frac{1{,}44}{0{,}25}$. b) $\frac{1{,}44}{1{,}44 + 0{,}25}$. c) Le logarithme népérien du SNR. d) $10\log_{10}$ du SNR. e) $10^{0{,}9}$, puis $\frac{r}{1 + r}$. f) $\frac{0{,}9 - 1{,}8 \times 0{,}7}{0{,}3}$. g) Retire $x = \frac{y - bn}{a}$ de $\hat x$ : le rapport des deux erreurs est un rapport des deux gains, pour chaque enregistrement.

</details>

### Ex MB5.5 — Débruiter un signal reçu, d'abord gaussien, puis émis à deux niveaux ±c : E[x | y] par M25a et par la formule de Tweedie (une tanh), et ce que rend le débruiteur quand le bruit tend vers 0

<details><summary>Indice 1</summary>

Fiche §5 : « La formule de Tweedie » (l'exemple des notes) et « Le débruiteur optimal d'un mélange » (le nuage de points, et sa propriété quand $b \to 0$) ; M25a §5.

</details>
<details><summary>Indice 2</summary>

Partie A : $y \sim \mathcal{N}(am, a^2\tau^2 + b^2)$, $\mathbb{E}[x \mid y] = m + \frac{a\tau^2}{a^2\tau^2 + b^2}(y - am)$, et le score d'une gaussienne ; puis $\mathbb{E}[n \mid y] = -b\,s_Y(y)$. Partie B : $p_Y(y) = \frac12\mathcal{N}(y \mid ac, b^2) + \frac12\mathcal{N}(y \mid -ac, b^2)$, et $\mathbb{E}[x \mid y] = c\,\frac{\mathcal{N}(y \mid ac, b^2) - \mathcal{N}(y \mid -ac, b^2)}{\mathcal{N}(y \mid ac, b^2) + \mathcal{N}(y \mid -ac, b^2)}$ : simplifie le facteur commun, et reconnais une tanh. Puis $n = \frac{y - ax}{b}$.

</details>
<details><summary>Indice 3</summary>

A : $y \sim \mathcal{N}(2, 25)$. a) $1 + \frac{2 \times 4}{25}(6 - 2)$. b) $-\frac{6 - 2}{25}$. c) $-3 \times s_Y(6)$ ; contrôle : $2\,\mathbb{E}[x \mid y] + 3\,\mathbb{E}[n \mid y] = 6$. B : le rapport vaut $\tanh\big(\frac{acy}{b^2}\big)$ ; ici $ac = 1$ et $b^2 = 1$. d) $2\tanh(1{,}1)$. e) $\frac{1{,}1 - 0{,}5 \times \mathbb{E}[x \mid y]}{1}$. f) Quand $b \to 0$, que devient $\frac{acy}{b^2}$ pour $y = 1{,}1$, et vers quoi tend alors la tanh ?

</details>

### Ex MB5.6 — Un bit altéré par deux relais, puis reconstitué par un modèle retour : ln p(x), l'ELBO de la loi aller des relais, et sa décomposition en reconstruction, KL finale et KL d'un pas retour

<details><summary>Indice 1</summary>

Fiche §6 : « Une chaîne de latents » (le théorème) et l'exemple « Une case qui s'efface », qui fait le même calcul pas à pas ; M26 (produit de matrices de transition), M04 (Bayes), M06 (KL discrète).

</details>
<details><summary>Indice 2</summary>

a) $q(z_2 \mid x) = \sum_{z_1}q(z_1 \mid x)\,q(z_2 \mid z_1)$. b) Bayes : $q(z_1 \mid z_2, x) = \frac{q(z_1 \mid x)\,q(z_2 \mid z_1)}{q(z_2 \mid x)}$. c) $p(x) = \sum_{z_2}p(z_2)\sum_{z_1}p(z_1 \mid z_2)\,p(x \mid z_1)$. e) La reconstruction $\sum_{z_1}q(z_1 \mid x)\ln p(x \mid z_1)$, la KL finale $\mathrm{KL}\big(q(z_2 \mid x) \,\|\, p(z_2)\big)$, et la KL du pas retour $\sum_{z_2}q(z_2 \mid x)\,\mathrm{KL}\big(q(z_1 \mid z_2, x) \,\|\, p(z_1 \mid z_2)\big)$. d) La reconstruction moins les deux KL de e).

</details>
<details><summary>Indice 3</summary>

$q(z_1 \mid x = 1) = (0{,}22 ;\ 0{,}78)$ pour $z_1 = 0$ puis 1. a) $q(z_2 = 0 \mid x) = 0{,}22 \times 0{,}6 + 0{,}78 \times 0{,}4$. b) $q(z_1 = 1, z_2 = 0 \mid x) = 0{,}78 \times 0{,}4$, à diviser par $q(z_2 = 0 \mid x)$ ; de même pour $z_2 = 1$. c) $p(x = 1 \mid z_1)$ vaut $0{,}32$ pour $z_1 = 0$ et $0{,}68$ pour $z_1 = 1$ ; $p(z_1 = 1 \mid z_2)$ vaut $0{,}16$ pour $z_2 = 0$ et $0{,}84$ pour $z_2 = 1$. e) Sachant $z_2 = 0$, la KL compare $q(z_1 \mid z_2 = 0, x)$ à $(0{,}84 ;\ 0{,}16)$ ; sachant $z_2 = 1$, à $(0{,}16 ;\ 0{,}84)$, presque la même loi.

</details>

### Ex MB5.7 — La date de floraison d'une variété et celle de tout le verger, deux lois gaussiennes : la loi p_v^{1+w} p_g^{−w} pour deux valeurs de w, son score, sa condition d'existence et le w limite

<details><summary>Indice 1</summary>

Fiche §7 : « Deux densités gaussiennes » (la précision $\lambda(w)$, la moyenne $\mu(w)$, la propriété et l'exemple de l'eau de mer), et « Bayes en logarithmes » pour le score.

</details>
<details><summary>Indice 2</summary>

$\lambda(w) = \frac{1 + w}{25} - \frac{w}{81}$, la variance $\frac{1}{\lambda(w)}$, et $\lambda(w)\,\mu(w) = \frac{(1 + w) \times 102}{25} - \frac{w \times 108}{81}$. Le score guidé est $(1 + w)\,s_v - w\,s_g$, ou $-\lambda(w)\,(x - \mu(w))$. Pour e), la loi existe tant que $\lambda(w) > 0$.

</details>
<details><summary>Indice 3</summary>

a) $\frac{1{,}4}{25} - \frac{0{,}4}{81}$, puis l'inverse. b) $\frac{1{,}4 \times 102}{25} - \frac{0{,}4 \times 108}{81}$, divisé par $\lambda(0{,}4)$. c) La même chose avec $w = 1{,}25$. d) $s_v(96) = -\frac{96 - 102}{25}$ et $s_g(96) = -\frac{96 - 108}{81}$ ; puis $2{,}25\,s_v - 1{,}25\,s_g$. e) $\frac{1 + w}{144} - \frac{w}{81} > 0$ : isole $w$ (ou $w^\star = \frac{\sigma_u^2}{\sigma_c^2 - \sigma_u^2}$, avec $\sigma_c^2 = 144$ et $\sigma_u^2 = 81$).

</details>

### Ex MB5.8 — Une tasse de thé qui refroidit : Euler et point milieu contre la solution exacte, l'erreur quand le pas est divisé par deux, un courant de vitesse constante, et un calcul à rebours

<details><summary>Indice 1</summary>

Fiche §8 : « Une équation, une condition initiale » (le refroidissement), « La méthode d'Euler, dans les deux sens du temps » (le pain, et « Exacte pour une vitesse constante ») et « Le point milieu ».

</details>
<details><summary>Indice 2</summary>

La solution exacte est $T(t) = 20 + 65\,e^{-0{,}06t}$. Un pas d'Euler multiplie l'écart $T - 20$ par $1 - 0{,}06h$ ; un pas du point milieu, par $1 - rh + \frac{(rh)^2}{2}$ avec $r = 0{,}06$ (vérifie-le sur un pas). L'erreur est la valeur approchée moins la valeur exacte. Pour e), le pas vaut $h = -5$, et la pente se lit à 10 min. Pour la feuille de ta copie : sa vitesse change-t-elle le long de sa trajectoire ?

</details>
<details><summary>Indice 3</summary>

a) $20 + 65\,e^{-0{,}6}$. b) $20 + 65 \times 0{,}7^2$ et $20 + 65 \times 0{,}85^4$. c) $rh = 0{,}3$ donne le facteur $0{,}745$, $rh = 0{,}15$ le facteur $0{,}86125$ ; deux pas, puis quatre. d) L'erreur avec $h = 5$ divisée par l'erreur avec $h = 2{,}5$, pour chaque méthode, avec les températures non arrondies (les erreurs du point milieu sont petites). e) La pente à 10 min vaut $-0{,}06 \times 27$ ; un pas : $47 + (-5) \times \text{pente}$ ; exactement, l'écart $27$ est multiplié par $e^{+0{,}3}$.

</details>

### Ex MB5.9 — Le chemin droit d'un bruit N(0, 1) vers une loi N(m, τ²) : le champ moyen (affine en x), un pas d'Euler depuis s = 1 qui rend m pour tout départ, puis deux pas, et l'écart-type obtenu contre τ

<details><summary>Indice 1</summary>

Fiche §9 : « Un chemin droit », « Le champ moyen » et « Des données gaussiennes » ; M25a §5, avec les gains $a = 1 - s$ et $b = s$.

</details>
<details><summary>Indice 2</summary>

$x_s \sim \mathcal{N}\big((1 - s)m, \sigma(s)^2\big)$, $\sigma(s)^2 = (1 - s)^2\tau^2 + s^2$, et $\mathbb{E}[x_0 \mid x_s = x] = m + \frac{(1 - s)\tau^2}{\sigma(s)^2}\big(x - (1 - s)m\big)$. Puis $v(x, s) = \frac{x - \mathbb{E}[x_0 \mid x_s = x]}{s}$. Un pas d'Euler de $s$ à $s + h$, avec $h < 0$ : $x + h\,v(x, s)$, le champ lu au début du pas.

</details>
<details><summary>Indice 3</summary>

a) $0{,}5^2 \times 0{,}25 + 0{,}5^2$. b) $\mathbb{E}[x_0 \mid x_{0{,}5} = 1{,}5] = 4 + \frac{0{,}5 \times 0{,}25}{0{,}3125}(1{,}5 - 2)$, puis divise $1{,}5$ moins ce nombre par $0{,}5$. c) $v(z, 1) = z - 4$ et $h = -1$. d) Le premier pas, $h = -0{,}5$, mène en $s = 0{,}5$ ; le second lit le champ en ce point et en $s = 0{,}5$. e) Refais d) avec un $z$ quelconque : tu obtiens $4 + \kappa z$, et $\kappa$ est l'écart-type cherché. La trajectoire exacte arrive en $m + \tau z$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB5.10 — La récurrence linéaire gaussienne à coefficients quelconques : la loi de x_t sachant x_0 ; à coefficient constant |a| < 1, la loi sachant un instant passé, la loi stationnaire et la convergence depuis toute loi initiale ; aucune loi stationnaire si |a| ≥ 1

<details><summary>Indice 1</summary>

Fiche §1 : « Deux moments qui suivent le pas » (la formule de $x_t$) et « La loi stationnaire d'un processus autorégressif » (le théorème) ; R4 (récurrence), R5 §4 et §5 (somme géométrique, point fixe), M25a §2, M26 §1.

</details>
<details><summary>Indice 2</summary>

1. Hérédité : remplace $x_{t-1}$ par la formule au rang $t - 1$ dans $x_t = a_tx_{t-1} + b_t\varepsilon_t$ ; le coefficient de chaque $\varepsilon_k$ gagne un facteur $a_t$. Puis : une constante plus une combinaison de bruits indépendants, et la variance d'une somme de variables indépendantes. 2. Repars de $x_s$ : la même récurrence, avec les bruits d'après $s$, indépendants de $x_s$. 3. Si $x_0 \sim \mathcal{N}(0, v_\infty)$, quelle est la loi de $x_1$ ? Puis écris la récurrence de $v_t - v_\infty$. 4. Suppose qu'une loi de variance $v$ est stationnaire, et calcule la variance de $x_1$.

</details>
<details><summary>Indice 3</summary>

1. $x_t = a_t\Big[(a_1\cdots a_{t-1})x_0 + \sum_{k<t}b_k(a_{k+1}\cdots a_{t-1})\varepsilon_k\Big] + b_t\varepsilon_t$. 2. $b^2\sum_{j=0}^{t-s-1}a^{2j}$, une somme géométrique de raison $a^2 \ne 1$. 3. $a^2v_\infty + b^2 = v_\infty$ ; retire-la de $v_t = a^2v_{t-1} + b^2$. 4. $v = a^2v + b^2$ donne $(1 - a^2)\,v = b^2 > 0$ : est-ce possible si $a^2 \ge 1$ et $v \ge 0$ ? Pour $a = 1$, $v_t = v_{t-1} + b^2$.

</details>

### Ex MB5.11 — La meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + E[(E[Y | X] − g(X))²], donc g = E[Y | X] ; sur un échantillon, la moyenne de chaque groupe

<details><summary>Indice 1</summary>

Fiche §4 : « La meilleure prédiction quadratique » et ses outils ; M02c §1 (la moyenne minimise la somme des carrés), M25b §2 (probabilités totales).

</details>
<details><summary>Indice 2</summary>

1. Écris $Y - c = (Y - \mu_k) + (\mu_k - c)$, avec $\mu_k = \mathbb{E}[Y \mid X = \xi_k]$, développe le carré et prends l'espérance sachant $X = \xi_k$. 2. $\mathbb{E}[(Y - g(X))^2] = \sum_kp_k\,\mathbb{E}\big[(Y - g(\xi_k))^2 \mid X = \xi_k\big]$, et la question 1 avec $c = g(\xi_k)$. 3. La loi empirique : $X$ prend les valeurs observées, avec les probabilités $\frac{n_\xi}{n}$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbb{E}[Y - \mu_k \mid X = \xi_k] = 0$ annule le terme croisé. 2. Le second terme est une somme de carrés pondérés par des $p_k > 0$ : quand est-il nul ? 3. Sous la loi empirique, $\mathbb{E}[Y \mid X = \xi]$ est la moyenne du groupe, et $\mathbb{V}(Y \mid X = \xi)$ sa variance empirique, en divisant par $n_\xi$.

</details>

### Ex MB5.12 — La formule de Tweedie : dériver la densité de y = a x + b n sous l'espérance, d'où E[x | y] et E[n | y] ; la vérification quand x est gaussien

<details><summary>Indice 1</summary>

Fiche §5 : « La formule de Tweedie » et son outil ; M04 (Bayes), M25a §5, M25b §7 (dériver sous l'espérance).

</details>
<details><summary>Indice 2</summary>

1. Sachant $x = \xi_k$, $y$ a la densité $\varphi_b(y - a\xi_k)$ ; probabilités totales ; et $\varphi_b'(u) = -\frac{u}{b^2}\varphi_b(u)$. 2. $P(x = \xi_k \mid y) = \frac{\pi_k\,\varphi_b(y - a\xi_k)}{p_Y(y)}$. 3. Remplace la somme par $\int p_X(u)\,\varphi_b(y - au)\,\mathrm{d}u$. 4. $y \sim \mathcal{N}(am, a^2\tau^2 + b^2)$, et le score d'une gaussienne.

</details>
<details><summary>Indice 3</summary>

2. $s_Y = \frac{p_Y'}{p_Y} = -\frac{1}{b^2}\sum_kP(x = \xi_k \mid y)\,(y - a\xi_k)$ : la somme vaut $y - a\,\mathbb{E}[x \mid y]$ ; isole $\mathbb{E}[x \mid y]$, puis écris $n = \frac{y - ax}{b}$ et prends l'espérance sachant $y$. 4. $\frac1a\Big(y - \frac{b^2(y - am)}{a^2\tau^2 + b^2}\Big)$ : écris $y = am + (y - am)$ et regroupe les termes en $y - am$.

</details>

### Ex MB5.13 — L'ELBO d'une chaîne de latents : Markov et Bayes réécrivent chaque pas aller, la somme télescope ; puis chaque KL entre gaussiennes de même variance devient une MSE pondérée des moyennes

<details><summary>Indice 1</summary>

Fiche §6 : « Une chaîne de latents » (le théorème et ses outils) et « Quand les pas sont gaussiens de même variance » ; M25b §5, R4 §5 (somme télescopique), M25a §7.

</details>
<details><summary>Indice 2</summary>

1. Markov : sachant $z_{t-1}$, $z_t$ ne dépend plus de $x$ ; puis Bayes sous la loi $q(\cdot \mid x)$, pour le couple $(z_{t-1}, z_t)$. 2. $\ln q(z_{1:T} \mid x) = \ln q(z_1 \mid x) + \sum_{t \ge 2}\ln q(z_t \mid z_{t-1})$ ; remplace chaque terme. 3. Écris $\ln p(x, z_{1:T})$ comme une somme ; regroupe $\ln p(z_T)$ avec $\ln q(z_T \mid x)$, et chaque $\ln p(z_{t-1} \mid z_t)$ avec $\ln q(z_{t-1} \mid z_t, x)$. 4. La KL de deux gaussiennes de même variance.

</details>
<details><summary>Indice 3</summary>

2. Il reste $\ln q(z_{1:T} \mid x) = \ln q(z_T \mid x) + \sum_{t=2}^T\ln q(z_{t-1} \mid z_t, x)$. 3. Le terme de $z_T$ ne dépend que de $z_T$, de loi $q(z_T \mid x)$ ; pour chaque terme du milieu, prends d'abord l'espérance sachant $z_t$ (la tour), sous $q(z_{t-1} \mid z_t, x)$. 4. Chaque terme vaut $-\frac{1}{2\sigma^2}\mathbb{E}_q\big[(\mu_q - \mu_p)^2\big]$ : de quoi dépendent $\mu_q$ et $\mu_p$ ?

</details>

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB5.14 — Pont : une loss de débruitage à plusieurs niveaux de bruit, son minimiseur à chaque niveau, et pour des données gaussiennes les MSE minimales sur le signal et sur le bruit, dont le rapport est le SNR

<details><summary>Indice 1</summary>

Fiche §3 (« Trois cibles qui portent la même information »), §4 (« La meilleure prédiction quadratique ») et §5 ; M25a §5 (conditionner un vecteur gaussien).

</details>
<details><summary>Indice 2</summary>

À chaque niveau, $(x, n, y)$ est un vecteur gaussien centré : $\mathbb{V}(y) = a^2 + b^2$, $\operatorname{Cov}(n, y) = b$ et $\operatorname{Cov}(x, y) = a$. Alors $\mathbb{E}[n \mid y] = \frac{\operatorname{Cov}(n, y)}{\mathbb{V}(y)}\,y$, et la MSE minimale vaut $\mathbb{V}(n) - \frac{\operatorname{Cov}(n, y)^2}{\mathbb{V}(y)}$ ; de même pour $x$. $L$ est une somme sur les niveaux de termes qui ne dépendent chacun que de $g(\cdot, k)$.

</details>
<details><summary>Indice 3</summary>

a) $\frac{1{,}7}{1{,}1^2 + 1{,}7^2}$. b) $1 - \frac{b_k^2}{a_k^2 + b_k^2}$, à chaque niveau. c) $1 - \frac{a_k^2}{a_k^2 + b_k^2}$. d) $\sum_k\omega_k \times$ (la MSE de b) au niveau $k$). Pour ta copie, simplifie le rapport de b) à c), et compare au §3.

</details>

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB5.15 — Expliquer avec le jeu du téléphone pourquoi, après assez de relais qui atténuent et bruitent, le message reçu ne dit plus rien du message émis

<details><summary>Indice 1</summary>

Fiche §1 : « Une règle qui atténue et qui bruite » et « La loi stationnaire d'un processus autorégressif » (le processus oublie son départ) ; MB5.1 d).

</details>
<details><summary>Indice 2</summary>

Un relais fait deux choses : il affaiblit ce qu'il reçoit, et il y ajoute une erreur nouvelle. Le message de départ subit tous les affaiblissements ; chaque erreur, seulement ceux des relais qui la suivent.

</details>
<details><summary>Indice 3</summary>

Plan : les deux effets d'un relais ; le message de départ, affaibli encore et encore ; les erreurs anciennes, affaiblies elles aussi, et un équilibre entre ce qui s'ajoute et ce qui s'efface ; le message reçu comme un tirage dans une dispersion habituelle ; un oubli d'autant plus rapide que chaque relais affaiblit . Aucune formule. (Pour aller plus loin : que se passerait-il si personne n'affaiblissait le message ?)

</details>

<a id="entretien"></a>

## 💼 Entretien

### MB5.E1 — « Un modèle de régression entraîné à la MSE prédit-il le prix le plus probable ? Que prédit-il quand les prix d'un même profil se partagent en deux groupes, et quelle loss prendre pour une médiane ? »

<details><summary>Indice 1</summary>

Fiche §4 : « La meilleure prédiction quadratique », « Une moyenne n'est pas la valeur la plus probable » (la MAE, la médiane) et son 💻.

</details>
<details><summary>Indice 2</summary>

La MSE apprend $\mathbb{E}[Y \mid X]$ : l'argument est la décomposition du ∂ MB5.11. Une moyenne n'est ni un mode ni une médiane : pense à une loi asymétrique, puis à une loi à deux modes. Chaque loss apprend un résumé de la loi de $Y$ sachant $X$.

</details>
<details><summary>Indice 3</summary>

Plan : non, la moyenne conditionnelle, et l'argument en une phrase ; une loi asymétrique tire la moyenne vers sa queue ; deux groupes donnent une prédiction entre les deux, que presque aucun bien n'a ; la MAE apprend la médiane, moins sensible aux prix extrêmes ; pour aller plus loin, des quantiles, la loi entière, ou la variable qui sépare les deux groupes.

</details>

<a id="notebook"></a>

## Notebook

### MB5.16 — Propager la moyenne et la variance d'une récurrence linéaire gaussienne à coefficients quelconques : `linear_gaussian_recursion`

<details><summary>Indice 1</summary>

Fiche §1 : « Deux moments qui suivent le pas » et son 💻 ; la docstring de `linear_gaussian_recursion`, qui dit chaque contrôle.

</details>
<details><summary>Indice 2</summary>

Les contrôles d'abord : `np.asarray(…, dtype=float)`, une dimension, la même longueur, des nombres finis ; `mean0` et `var0` réels finis, pas des booléens (`isinstance(…, bool)` avant le reste), `var0` positif ou nul. Puis une boucle sur les couples $(a_t, b_t)$, sans modifier les tableaux reçus. Pour la suite : a) trois pas de mêmes coefficients ; b) `A_16`, `B_16` et le départ $\mathcal{N}(1{,}5 ;\ 0{,}3)$ ; c) `np.full(6, -0.68)`.

</details>
<details><summary>Indice 3</summary>

```python
means, variances = [float(mean0)], [float(var0)]
for at, bt in zip(a, b):
    means.append(at * means[-1])
    variances.append(at ** 2 * variances[-1] + bt ** 2)
return np.array(means), np.array(variances)
```
c) $v_\infty = \frac{1{,}1^2}{1 - 0{,}68^2}$ ; compare $v_6$ à $v_\infty$.

</details>

### MB5.17 — Le débruiteur optimal d'une mesure bruitée quand le signal suit un mélange de gaussiennes, des points compris : `posterior_mean_mixture`

<details><summary>Indice 1</summary>

Fiche §5 : « Le débruiteur optimal d'un mélange » (les trois temps, et « Un nuage de points ») et son 💻 ; la docstring de `posterior_mean_mixture` ; M05a §8 (log-sum-exp).

</details>
<details><summary>Indice 2</summary>

Pour chaque composante : `spread = a**2 * s2 + b**2`, le logarithme $\ln\pi_k - \frac12\ln(2\pi\,\text{spread}) - \frac{(y - a\mu_k)^2}{2\,\text{spread}}$ ($-\infty$ si $\pi_k = 0$), et $\mathbb{E}[x \mid y, k] = \mu_k + \frac{as_k^2}{\text{spread}}(y - a\mu_k)$. Ajoute un axe à `y` (`y[..., None]`) pour calculer toutes les composantes d'un coup ; retire le maximum sur cet axe avant l'exponentielle. Pour $a = 0$, rends la moyenne du mélange, de la forme de `y`. Puis : a) un mélange à une composante ; b) deux points de poids $\frac12$ et de variance 0.

</details>
<details><summary>Indice 3</summary>

```python
spread = a ** 2 * s2 + b ** 2                      # s2: the K variances
post = mu + a * s2 / spread * (y[..., None] - a * mu)
with np.errstate(divide="ignore"):
    logw = np.log(w)
lw = logw - 0.5 * np.log(2 * np.pi * spread) - (y[..., None] - a * mu) ** 2 / (2 * spread)
lw = lw - lw.max(axis=-1, keepdims=True)
r = np.exp(lw)
r = r / r.sum(axis=-1, keepdims=True)
return (r * post).sum(axis=-1)
```
c) `weights=[0.25, 0.75]`, `means=[-1.4, 2.3]`, `variances=[0.2, 0.5]`, $a = 0{,}7$, $b = 0{,}5$, et les trois mesures dans un seul tableau.

</details>

### MB5.18 — Suivre un champ de vitesses qui dépend du temps : la méthode d'Euler et celle du point milieu, dans les deux sens du temps : `euler_ode`, `midpoint_ode`

<details><summary>Indice 1</summary>

Fiche §8 : « La méthode d'Euler, dans les deux sens du temps » et « Le point milieu » ; les docstrings de `euler_ode` et `midpoint_ode`.

</details>
<details><summary>Indice 2</summary>

Contrôle `n_steps` (refuse un booléen avant de tester l'entier) et les deux instants, puis $h = \frac{t_N - t_0}{N}$, négatif si $t_N < t_0$ (l'argument `t1` est l'instant final $t_N$). Recalcule $t_k = t_0 + kh$ à chaque pas, plutôt que d'ajouter $h$ à chaque fois. Vérifie que chaque vitesse a la forme de $x$. Garde tous les points, départ compris, et empile-les. Pour la suite : a) le thé, `lambda t, T: -0.06 * (T - 20)` ; b) $t_0 = 10$ et $t_N = 5$ ; c) `lambda t, x: 3 * t**2` ; d) la solution exacte en $t = 3$.

</details>
<details><summary>Indice 3</summary>

```python
h = (t1 - t0) / n_steps
x = np.array(x0, dtype=float)                      # a copy: x0 is never modified
xs = [x]
for k in range(n_steps):
    t = t0 + k * h
    v = f(t, x)                                    # Euler
    # midpoint: v = f(t + h / 2, x + h / 2 * f(t, x))
    x = x + h * v
    xs.append(x)
return np.array(xs)
```
c) Euler et le point milieu font ici deux sommes de M02a §1 : lesquelles ?

</details>

### MB5.19 — `scipy.integrate.solve_ivp` : une croissance logistique suivie par tes deux méthodes, l'erreur au temps final selon le nombre de pas en échelle log-log, et les pentes 1 et 2

<details><summary>Indice 1</summary>

Fiche §8 : « Une équation, une condition initiale » (la croissance logistique et sa solution exacte), le paragraphe « À nombre d'évaluations égal » et le 💻 sur `solve_ivp`.

</details>
<details><summary>Indice 2</summary>

Un seul champ `f(t, P)`, le temps d'abord, sert à SciPy et à tes deux fonctions. `solve_ivp(f, (0, 8), [1.5], rtol=1e-10, atol=1e-10)` rend un objet dont `.y[0, -1]` est la valeur en $t = 8$. L'erreur est l'écart absolu à la solution exacte $\frac{K}{1 + (K/P_0 - 1)\,e^{-rt}}$. Les pentes : `np.polyfit` sur les logarithmes de $N$ et des erreurs, pour les quatre plus grands $N$.

</details>
<details><summary>Indice 3</summary>

`f = lambda t, P: 0.9 * P * (1 - P / 40)` ; la solution exacte en 8 : $\frac{40}{1 + (40/1{,}5 - 1)\,e^{-7{,}2}}$. b) `Ns = [8, 16, 32, 64, 128, 256]`, une liste d'erreurs par méthode, puis `ax.loglog(Ns, errors)`. c) `np.polyfit(np.log(Ns[2:]), np.log(err[2:]), 1)[0]` ; puis, dans tes listes de b), l'erreur d'Euler à $N = 64$ et celle du point milieu à $N = 32$.

</details>

### MB5.20 — Prédire ce que rend le débruiteur optimal de cinq relevés quand le bruit tend vers 0, pour une mesure proche d'un relevé puis à égale distance de deux, et mesurer

<details><summary>Indice 1</summary>

Fiche §5 : le paragraphe « Un nuage de points » et sa propriété. Écris ta prédiction avant d'ouvrir l'indice 2.

</details>
<details><summary>Indice 2</summary>

Cinq relevés de même poids et de variance nulle : $\mathbb{E}[x \mid y] = \sum_kr_k\,\mu_k$, avec $r_k \propto \exp\big(-\frac{a^2(y/a - \mu_k)^2}{2b^2}\big)$, une softmax de scores $-\frac{a^2}{2b^2}\big(\frac ya - \mu_k\big)^2$ : plus un relevé est proche de $\frac ya$, plus il pèse. Quand $b$ diminue, quels poids survivent ? Quand $b$ est énorme devant toutes les distances, que valent-ils ?

</details>
<details><summary>Indice 3</summary>

Ta prédiction, raisonnée : a) les distances de 2 aux cinq relevés sont $0{,}8$ ; $0{,}1$ ; $0{,}3$ ; $1{,}6$ ; 2 : vers où se concentre la softmax ? b) $2{,}95$ est à la même distance de $2{,}3$ et de $3{,}6$ : ces deux poids restent égaux pour tout $b$, les trois autres s'éteignent ; quelle est la limite ? c) Pour $b = 50$, $\frac{b^2}{a^2}$ est énorme devant le carré de chaque distance (au plus 4) : les distances ne comptent presque plus. Pour mesurer : `posterior_mean_mixture(y, 0.5, b, [0.2] * 5, releves, [0.0] * 5)`.

</details>

### MB5.21 — Le chemin droit vers une loi gaussienne : Euler et point milieu sur le champ moyen exact, de 1 à 32 pas, la moyenne et l'écart-type obtenus contre ceux de la cible

<details><summary>Indice 1</summary>

Fiche §9 : « Le champ moyen » et « Des données gaussiennes » (le champ affine en $x$, les trajectoires $x(s) = (1 - s)m + \sigma(s)z$) ; §8 : l'ordre des deux méthodes ; MB5.9.

</details>
<details><summary>Indice 2</summary>

`field_21(s, x)` : $\mathbb{E}[x_0 \mid x_s = x] = m + \frac{(1 - s)\tau^2}{\sigma(s)^2}\big(x - (1 - s)m\big)$, puis $\frac{x - \mathbb{E}[x_0 \mid x_s = x]}{s}$. `euler_ode` l'appelle `f(t, x)` avec $t = s$ : l'ordre des arguments convient. Transporte de $t_0 = 1$ à $t_N = 0$ : aucune des deux méthodes ne lit le champ en $s = 0$, où il n'est pas défini.

</details>
<details><summary>Indice 3</summary>

a) Pour chaque $N$, `np.std(euler_ode(field_21, Z_21, 1.0, 0.0, N)[-1])`, puis la même chose avec `midpoint_ode`. b) `np.std(4 + 0.5 * Z_21)`. Pour la moyenne, `np.mean` des mêmes points. Pour la question sur l'ordre : divise chaque écart à l'écart-type exact de b) par celui du $N$ suivant.

</details>

### MB5.22 — Des lois guidées p_c^{1+w} p_u^{−w} sur une grille : une loi générale à deux bosses, une loi de classe gaussienne, et ce que w resserre et déplace

<details><summary>Indice 1</summary>

Fiche §7 : « Bayes en logarithmes : une combinaison de scores » (la propriété) et le paragraphe « Avec une loi générale à plusieurs bosses » ; MB5.7.

</details>
<details><summary>Indice 2</summary>

Calcule $p_u$ et $p_c$ sur `xs` à partir des arguments `general` (les poids, les moyennes et les variances du mélange) et `cls` (la moyenne et la variance de la classe), jamais à partir des lois de l'énoncé écrites en dur : la vérification passe un autre mélange. Le logarithme de la loi guidée est $(1 + w)\ln p_c - w\ln p_u$ ; retire son maximum, prends l'exponentielle et divise par `np.trapezoid(d, xs)`. Les moments s'intègrent de même : la moyenne $\int x\,d(x)\,\mathrm{d}x$, l'écart-type $\sqrt{\int(x - \text{moyenne})^2d(x)\,\mathrm{d}x}$. Pour la figure : une courbe par loi, chacune avec un `label`, puis `ax.legend()`, `ax.set_xlabel(…)` et `ax.set_ylabel(…)`.

</details>
<details><summary>Indice 3</summary>

```python
# from scipy.special import logsumexp; from scipy.stats import norm
weights, means, variances = general
lpu = logsumexp([np.log(p) + norm.logpdf(xs, m, np.sqrt(v))
                 for p, m, v in zip(weights, means, variances)], axis=0)      # ln p_u, without underflow
lpc = norm.logpdf(xs, cls[0], np.sqrt(cls[1]))
lg = (1 + w) * lpc - w * lpu
d = np.exp(lg - lg.max())
d = d / np.trapezoid(d, xs)
```
c) `np.trapezoid(np.where(xs < 0, d, 0), xs)`. Compare à la masse de $p_c$ sur $x < 0$ : la loi guidée vaut $p_c\big(\frac{p_c}{p_u}\big)^w$, et que vaut $\frac{p_c}{p_u}$ du côté de l'autre bosse ?

</details>

### MB5.23 — Chasse à l'erreur : un pont aux poids inversés, un débruiteur qui oublie le bruit dans ses responsabilités, et un Euler dont le temps n'avance pas

<details><summary>Indice 1</summary>

Fiche §2 : la propriété du pont (quel relevé reçoit le poids $\frac{V_s}{V_T}$ ?) ; les ⚠️ du §5 (les responsabilités) et du §8 (l'instant du champ).

</details>
<details><summary>Indice 2</summary>

Pour chaque fonction, cherche une entrée où l'erreur ne change rien : un instant où $\frac{V_s}{V_T} = \frac12$, une seule composante, un champ qui ne dépend pas du temps. C'est là qu'était la vérification du collègue. Corrige le code du collègue lui-même, sans appeler `mymath`.

</details>
<details><summary>Indice 3</summary>

(1) `mean = x0 + Vs / VT * (xT - x0)` ; la variance ne change pas. (2) Dans le logarithme de la loi de $y$ sachant la composante, la variance `a**2 * s2 + b**2`. (3) `f(t0 + k * h, x)` au pas $k$. a) $x_0 = 3$, $x_T = 9$, $V_s = 6$, $V_T = 8{,}5$. b) `weights=[0.4, 0.6]`, `means=[-1, 2.5]`, `variances=[0.3, 0.6]`, $a = 1{,}2$, $b = 0{,}9$. c) `lambda t, x: t - x`, depuis $x(0) = 1$, de 0 à 2 en six pas.

</details>

### MB5.24 — Un test de propriété : Euler exact pour une vitesse constante, le point milieu exact pour une vitesse affine en t, et l'erreur d'Euler divisée par deux avec le pas

<details><summary>Indice 1</summary>

Fiche §8 : « Exacte pour une vitesse constante », « Le point milieu » (exact pour une vitesse affine en $t$) et l'erreur au temps final (ordre 1, ordre 2).

</details>
<details><summary>Indice 2</summary>

Chaque test appelle `method(f, x0, t0, t1, N)` sur plusieurs cas et compare **chaque** point rendu à la solution exacte aux instants $t_k = t_0 + k\frac{t_N - t_0}{N}$ : plusieurs vitesses (dont une négative) et plusieurs $N$ (dont 1). Le champ doit rendre la forme de $x$ : `lambda t, x: c + 0 * x`. Pour `error_halves_24`, un champ qui dépend de $t$ et de $x$, de solution connue, et $N$ assez grand pour que l'erreur suive sa droite. Rends un booléen Python.

</details>
<details><summary>Indice 3</summary>

Les solutions exactes : $x_0 + c\,(t - t_0)$ pour une vitesse constante, $x_0 + \kappa_0(t - t_0) + \kappa_1\frac{t^2 - t_0^2}{2}$ pour $\kappa_0 + \kappa_1t$. Pour chaque cas : `ts = t0 + np.arange(N + 1) * (t1 - t0) / N`, puis `np.max(np.abs(xs - exact(ts))) <= 1e-9`. Pour `error_halves_24` : $x' = t - x$, $x(0) = 2$, sur $[0, 3]$, de solution $t - 1 + 3e^{-t}$, avec $N = 64$ puis 128, et `1.8 <= e64 / e128 <= 2.2`.

</details>

### MB5.25 — Défi : transporter un bruit N(0, 1) vers une loi à deux bosses par son champ moyen exact, en au plus huit évaluations du champ, sous une distance de Wasserstein fixée

<details><summary>Indice 1</summary>

Fiche §9 : « Le champ moyen » (le champ par le débruiteur, avec $a = 1 - s$ et $b = s$) ; §8 : « Le point milieu » et le paragraphe « À nombre d'évaluations égal » ; Q8, MB5.19 c) et MB5.21.

</details>
<details><summary>Indice 2</summary>

`field_25` : $\frac{x - \mathbb{E}[x_0 \mid x_s = x]}{s}$, avec `posterior_mean_mixture(x, 1 - s, s, …)`. Huit appels, c'est huit pas d'Euler ou quatre pas du point milieu : laquelle des deux méthodes a l'erreur la plus petite à ce coût ? Ne lis jamais le champ en $s = 0$. Pour compter tes appels, enveloppe `field` dans une fonction qui incrémente un compteur.

</details>
<details><summary>Indice 3</summary>

Quatre pas du point milieu, $h = -0{,}25$, de $s = 1$ à $s = 0$ : à chaque pas, un appel en $(x, s)$ pour le demi-pas, puis un appel en $\big(x + \frac h2\,v, s + \frac h2\big)$ pour le pas entier. Mesure `scipy.stats.wasserstein_distance(points, TARGET_25)`, divise-la par l'écart-type du mélange : la vérification fait la moyenne de ces rapports sur quinze lois cachées, chacune avec ses huit appels. Essaie ta fonction sur des mélanges que tu fabriques toi-même : deux bosses très étroites, très écartées, une bosse légère.

</details>
