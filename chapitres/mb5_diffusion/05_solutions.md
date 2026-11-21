# MB5 · Les maths de la diffusion — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture, qui accepte toute démonstration correcte. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB5.Q1 — Une récurrence linéaire gaussienne : quelle moyenne, quelle variance, quand une loi stationnaire, et combien de pas pour oublier le départ ?
1. $x_1$ : moyenne $-0{,}5 \times 6 = -3$, variance $0 + 2^2 = 4$ ; $x_2$ : moyenne $1{,}5$, variance $0{,}25 \times 4 + 4 = 5$.
2. $\mathcal{N}\big(0, \frac{4}{1 - 0{,}25}\big) = \mathcal{N}\big(0, \frac{16}{3}\big)$, une variance d'environ $5{,}33$ ; $\lvert a\rvert < 1$.
3. $0{,}99$ et $-0{,}3$, de valeur absolue plus petite que 1. Pour $a = -1$ ou $1{,}01$, $v_t \ge v_{t-1} + b^2$ croît sans fin.
4. Vrai : $v_t = v_{t-1} + b^2$, donc $v_t = tb^2$ depuis un départ connu ; c'est la marche aléatoire.
5. L'écart de moyenne est multiplié par $\lvert a\rvert = 0{,}5$ à chaque pas : $0{,}5^{10} = \frac{1}{1\thinspace024} \le 10^{-3}$, après 10 pas ($0{,}5^9 = \frac{1}{512}$ ne suffit pas). L'écart de variance est multiplié par $a^2 = 0{,}25$ : $0{,}25^5 = \frac{1}{1\thinspace024}$, après 5 pas, deux fois moins.

### MB5.Q2 — Le pont et les couplages : où l'incertitude est la plus grande, ce que fixent les lois marginales et ce qu'elles laissent libre
1. Les pas ont la même variance, donc $V_s = 0{,}4\thinspace s$ ; la variance $\frac{V_s(V_{10} - V_s)}{V_{10}}$ est maximale quand $V_s = \frac{V_{10}}{2}$, au milieu, $s = 5$ : elle vaut $\frac{2 \times 2}{4} = 1$.
2. $V_4 = 1{,}6$ et $V_{10} = 4$ : moyenne $0 + \frac{1{,}6}{4} \times 5 = 2$, variance $\frac{1{,}6 \times 2{,}4}{4} = 0{,}96$ ; $x_4 \sim \mathcal{N}(2 ;\ 0{,}96)$.
3. $\mathcal{N}(0, 9)$ : une somme de gaussiennes indépendantes, de variance $4 + 5$. Le lemme de la fiche, avec $\omega = 3$, donne la même loi pour tout $\sigma \in [0, 3]$, et aussi pour $\sigma \in [-3, 0[$ ($\sigma Z$ et $-\sigma Z$ ont la même loi) : en tout, $\lvert\sigma\rvert \le 3$.
4. Faux : la marche, un seul tirage et un tirage frais à chaque instant ont les mêmes lois marginales et des corrélations différentes (fiche §2).
5. Oui : $X_t$ et $W_t$ suivent tous deux $\mathcal{N}(0, t)$. $X_4 = 2X_1$ : la corrélation vaut 1. $\operatorname{Cov}(W_1, W_4) = \mathbb{V}(W_1) = 1$, d'où une corrélation $\frac{1}{\sqrt{1 \times 4}} = \frac12$.

### MB5.Q3 — Signal et bruit : SNR, cotes, logit et décibels, et ce qu'un changement d'échelle ne change pas
1. $\operatorname{SNR} = \frac{3{,}24}{0{,}25} = 12{,}96$ ; $\gamma = \frac{12{,}96}{13{,}96} \approx 0{,}9284$ (soit $10\log_{10}12{,}96 \approx 11{,}13$ dB).
2. $\operatorname{SNR} = \frac{0{,}96}{0{,}04} = 24$, la cote de $\gamma$ ; $\operatorname{logit}\gamma = \ln 24 \approx 3{,}178$.
3. Ils ne changent pas : $a$ et $b$ sont tous deux multipliés par 10, et $\frac{a^2}{b^2}$ ne bouge pas.
4. $r = 10^{1{,}5} \approx 31{,}62$, et $\gamma = \frac{r}{1 + r} \approx 0{,}969$ : 97 % de la variance doit venir de la voix.
5. Faux : $\gamma = \frac{\operatorname{SNR}}{1 + \operatorname{SNR}}$ ; par exemple, un SNR de 1 donne $\gamma = 0{,}5$, un SNR de 2 donne $\gamma \approx 0{,}667$. $\gamma$ reste sous 1 ; c'est sa cote qui double.

### MB5.Q4 — Ce que la MSE apprend : une moyenne conditionnelle, pas la valeur la plus probable ; et ce qu'apprennent la MAE et la log-loss
1. $\mathbb{E}[Y \mid X = x] = 0{,}7 \times 10 + 0{,}3 \times 40 = 19$ ; non, $Y$ ne vaut jamais 19 : la prédiction tombe entre les deux modes.
2. $\mathbb{V}(Y \mid X = x) = 0{,}7 \times 9^2 + 0{,}3 \times 21^2 = 56{,}7 + 132{,}3 = 189$.
3. La médiane conditionnelle, 10 : $P(Y \le 10) = 0{,}7 \ge \frac12$ et $P(Y \ge 10) = 1 \ge \frac12$ ; ici aussi la valeur la plus probable.
4. La probabilité a posteriori $P(Y = 1 \mid X)$ (rappel de M27).
5. Vrai : c'est le théorème du §4 appliqué à la loi empirique (∂ MB5.11, q. 3).

### MB5.Q5 — Le score en x : où il pointe, la constante qu'il ignore, et ce que dit la formule de Tweedie
1. $s(x) = -\frac{x - 3}{4}$ : $s(7) = -1$ et $s(1) = 0{,}5$ ; il pointe vers 3, le mode.
2. $\ln p(x) = \ln C - \frac{x^4}{4}$, de dérivée $-x^3$ : $C$ disparaît, et $s(2) = -8$.
3. Vrai : en un mode, $p' = 0$, donc $s = \frac{p'}{p} = 0$ (il s'annule aussi au creux entre deux bosses).
4. $\mathbb{E}[n \mid y] = -b\thinspace s_Y(y) = -0{,}5 \times (-1{,}2) = 0{,}6$ ; $\mathbb{E}[x \mid y] = \frac{3 + 0{,}25 \times (-1{,}2)}{2} = 1{,}35$. Contrôle : $2 \times 1{,}35 + 0{,}5 \times 0{,}6 = 3$.
5. Faux : le signal peut suivre n'importe quelle loi ; c'est le **bruit** qui doit être gaussien.

### MB5.Q6 — L'ELBO d'une chaîne : quels termes dépendent du modèle, quelle KL compare quoi, et ce que devient une KL entre gaussiennes de même variance
1. La KL finale $\mathrm{KL}\big(q(z_T \mid x) \thinspace\Vert\thinspace p(z_T)\big)$ : $q$ et $p(z_T)$ sont fixés, elle est constante.
2. Au pas retour qui connaît $x$, $q(z_{t-1} \mid z_t, x)$, la loi a posteriori du processus aller.
3. $\frac{(2{,}2 - 1{,}7)^2}{2 \times 0{,}5} = 0{,}25$.
4. Vrai : $\operatorname{ELBO} = \ln p(x) - \mathrm{KL}\big(q(z_{1:T} \mid x) \thinspace\Vert\thinspace p(z_{1:T} \mid x)\big)$, et une KL est positive ou nulle.
5. Elle double : $\frac{(\mu_q - \mu_p)^2}{2\sigma^2}$ est inversement proportionnelle à $\sigma^2$.

### MB5.Q7 — Guider : interpoler ou extrapoler, la différence de deux scores, et quand un produit de puissances n'est plus une densité
1. Oui : $0{,}7\thinspace y_c + 0{,}3\thinspace y_u$, deux coefficients positifs de somme 1 ; on interpole.
2. Au-delà de $y_c$, du côté opposé à $y_u$, à la distance $1{,}25\thinspace\lVert y_c - y_u\rVert$ de $y_c$ ; on extrapole.
3. $\nabla_x\ln p(c \mid x)$ : la formule de Bayes en logarithmes, $p(c)$ ne dépendant pas de $x$.
4. $\lambda(w) = \frac{1 + w}{4} - w > 0$ si et seulement si $w < \frac13$ ($w^\star = \frac{\sigma_u^2}{\sigma_c^2 - \sigma_u^2} = \frac13$).
5. Vrai : $\lambda(w) = \frac{1}{\sigma_c^2} + w\big(\frac{1}{\sigma_c^2} - \frac{1}{\sigma_u^2}\big) \ge \frac{1}{\sigma_c^2} > 0$.

### MB5.Q8 — Euler, point milieu et chemin droit : ce que coûte un pas, l'ordre de l'erreur, et le sens du temps
1. 12 pas d'Euler (une évaluation par pas), 6 pas du point milieu (deux par pas).
2. Environ 2 pour Euler (ordre 1), environ 4 pour le point milieu (ordre 2).
3. $-1$ pour Euler, $-2$ pour le point milieu (contre le pas $h$ : $+1$ et $+2$).
4. $h = \frac{2 - 5}{6} = -0{,}5$.
5. (B) : en $s = 1$, $v(x, 1) = x - m$, et $z - (z - m) = m$ ; tous les points arrivent au même endroit.

<a id="rappels"></a>

## 🔁 Rappels

### MB5.R1 — Sommes et images affines de gaussiennes, produit de densités et modèle linéaire gaussien (M25a)
1. $X + Y \sim \mathcal{N}(4, 7)$ ; $2X - Y \sim \mathcal{N}(10 + 1, 4 \times 2 + 5) = \mathcal{N}(11, 13)$.
2. Les précisions s'ajoutent : $\frac12 + \frac16 = \frac23$, donc $v = 1{,}5$ ; $m = 1{,}5 \times \big(\frac12 + \frac46\big) = 1{,}75$.
3. Le gain vaut $\frac{3}{3 + 1} = 0{,}75$ : $x \mid y = 15 \sim \mathcal{N}(10 + 0{,}75 \times 5,\ 3 \times 0{,}25) = \mathcal{N}(13{,}75 ;\ 0{,}75)$.
4. Faux : il faut que $(X, Y)$ soit un vecteur gaussien (c'est le cas si elles sont indépendantes). Contre-exemple : $X \sim \mathcal{N}(0, 1)$ et $Y = SX$, avec un signe $S = \pm1$ indépendant ; $Y$ suit $\mathcal{N}(0, 1)$, mais $X + Y = 0$ avec la probabilité $\frac12$.
5. $\mathcal{N}(\mathbf{A}\boldsymbol{\mu} + \mathbf{b},\ \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top)$ (MML (6.88)).

### MB5.R2 — Espérance et variance conditionnelles, lois totales, et l'ELBO d'un latent (M25b)
1. $\mathbb{E}[X] = 0{,}7 \times 2 + 0{,}3 \times 7 = 3{,}5$ ; $\mathbb{V}(X) = \mathbb{E}[\mathbb{V}(X \mid Z)] + \mathbb{V}(\mathbb{E}[X \mid Z]) = (0{,}7 + 1{,}2) + 0{,}7 \times 0{,}3 \times 5^2 = 1{,}9 + 5{,}25 = 7{,}15$.
2. $\mathbb{E}[Y]$ : la propriété de la tour (M26 §3).
3. $\operatorname{ELBO} = \ln p(x) - \mathrm{KL} = -2{,}5$.
4. Le posterior $p(z \mid x)$, et lui seul (la KL est alors nulle).
5. $r_2 = \frac{e^{-1{,}7}}{e^{-3{,}2} + e^{-1{,}7}} = \frac{1}{1 + e^{-1{,}5}} \approx 0{,}8176$.

### MB5.R3 — Un pas d'Euler (M20), la loi stationnaire d'une chaîne finie (M26) et la cote d'une probabilité (R6)
1. $3 + 0{,}1 \times (-2 \times 3 + 1) = 2{,}5$.
2. Non : $3 + 1{,}5 \times (-5) = -4{,}5$, à 5 du point fixe au lieu de $2{,}5$ ; chaque pas multiplie l'écart par $1 - 2h = -2$ (M20 §6).
3. $\pi_1 \times 0{,}21 = \pi_2 \times 0{,}42$ et $\pi_1 + \pi_2 = 1$ : $\boldsymbol{\pi} = \big(\frac23 ;\ \frac13\big)$.
4. La cote $\frac{0{,}12}{0{,}88} = \frac{3}{22} \approx 0{,}14$ ; le logit $\ln\frac{3}{22} \approx -1{,}99$.
5. $\frac{7}{1 + 7} = \frac78$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB5.1 — L'anomalie de température d'un lac, un processus autorégressif d'ordre 1 : sa loi dans k jours sachant aujourd'hui, sa loi stationnaire, le nombre de jours pour oublier le départ, et sa loi sachant un jour passé

**Réponses.** a) `[2.2, 0.1225]` · b) `[1.7037, 0.2908]` · c) `0.543` · d) `28` · e) `[-0.7388, 0.3918]`.

**Démarche.** $a = 0{,}88$ et $b^2 = 0{,}1225$. a) $m_1 = 0{,}88 \times 2{,}5 = 2{,}2$, $v_1 = 0{,}88^2 \times 0 + 0{,}1225 = 0{,}1225$. b) $m_3 = 0{,}88^3 \times 2{,}5 = 0{,}681472 \times 2{,}5 \approx 1{,}7037$ ; $v_2 = 0{,}7744 \times 0{,}1225 + 0{,}1225 = 0{,}217364$, $v_3 = 0{,}7744 \times 0{,}217364 + 0{,}1225 \approx 0{,}2908$. c) $v_\infty = \frac{0{,}1225}{1 - 0{,}7744} = \frac{0{,}1225}{0{,}2256} \approx 0{,}5430$. d) L'écart-type stationnaire vaut $\sqrt{0{,}5430} \approx 0{,}7369$ : on cherche le premier $k$ tel que $2{,}5 \times 0{,}88^k < 0{,}07369$. Comme $0{,}88^{27} \times 2{,}5 \approx 0{,}0792$ et $0{,}88^{28} \times 2{,}5 \approx 0{,}0697$, $k = 28$ (ou $k > \frac{\ln(2{,}5/0{,}07369)}{\ln(1/0{,}88)} \approx 27{,}6$). e) Sachant $x_{20}$, c'est la même récurrence, partie de $x_{20}$ et suivie 5 jours : moyenne $0{,}88^5 \times (-1{,}4) = 0{,}527732 \times (-1{,}4) \approx -0{,}7388$, variance $v_\infty\thinspace(1 - 0{,}88^{10}) = 0{,}5430 \times 0{,}721499 \approx 0{,}3918$.

Dans ta copie : $x_3 = 0{,}88^3x_0 + 0{,}35 \times 0{,}88^2\thinspace\varepsilon_1 + 0{,}35 \times 0{,}88\thinspace\varepsilon_2 + 0{,}35\thinspace\varepsilon_3$ : les trois bruits sont indépendants, d'où $v_3 = 0{,}1225\thinspace(0{,}88^4 + 0{,}88^2 + 1)$. La loi de $x_{25}$ sachant $x_{20}$ ne dépend pas de $x_0$ : $x_{25}$ s'écrit avec $x_{20}$ et les bruits des jours 21 à 25, indépendants du passé ; c'est la propriété de Markov (M26 §1).

**Erreurs fréquentes.** Partir de la variance stationnaire au lieu de 0 alors que $x_0$ est mesuré ; oublier le bruit du premier jour (une variance nulle) ; laisser la moyenne à $2{,}5$. Pour b), ajouter trois fois $b^2$ sans atténuer les bruits anciens. Pour c), un signe faux dans le point fixe ($\frac{b^2}{1 + a^2}$), ou multiplier par $1 - a^2$ au lieu de diviser. Pour d), répondre le dernier jour au-dessus du seuil (27), ou comparer la moyenne au dixième du départ (19). Pour e), garder la variance stationnaire, oublier d'atténuer les bruits des jours 21 à 25, ou repartir de $x_0$ pour 25 jours.

**Variante.** Avec $a = -0{,}88$ (un lac qui « rebondit » d'un jour à l'autre, peu réaliste), les variances ne changent pas ($a^2$ est le même), et les moyennes changent de signe chaque jour : $x_3 \sim \mathcal{N}(-1{,}7037 ;\ 0{,}2908)$.

### Ex MB5.2 — La survie d'une ruche à six mois de risques différents : le produit exact, son logarithme, le risque mensuel constant équivalent, et l'encadrement par deux exponentielles

**Réponses.** a) `0.6286` · b) `-0.4643` · c) `0.0745` · d) `0.644` · e) `0.6158`.

**Démarche.** a) $P = 0{,}99 \times 0{,}97 \times 0{,}93 \times 0{,}88 \times 0{,}86 \times 0{,}93 \approx 0{,}6286$. b) $\ln P = \sum_k\ln(1 - h_k) \approx -0{,}01005 - 0{,}03046 - 0{,}07257 - 0{,}12783 - 0{,}15082 - 0{,}07257 \approx -0{,}4643$. c) $(1 - \bar h)^6 = P$, donc $1 - \bar h = P^{1/6} = e^{\ln P/6} \approx 0{,}92553$, et $\bar h \approx 0{,}0745$. d) $H = 0{,}44$ et $e^{-0{,}44} \approx 0{,}6440$. e) $\sum_kh_k^2 = 0{,}0001 + 0{,}0009 + 0{,}0049 + 0{,}0144 + 0{,}0196 + 0{,}0049 = 0{,}0448$, et $e^{-0{,}4848} \approx 0{,}6158$. On a bien $0{,}6158 \le 0{,}6286 \le 0{,}6440$.

Dans ta copie : $\ln P = \sum_{k=1}^6\ln(1 - h_k)$ ; chaque $h_k \le 0{,}14 \le \frac12$, la condition de $\ln(1 - h) \ge -h - h^2$. (Février, $\ln 0{,}86 \approx -0{,}151$, pèse le plus.)

**Erreurs fréquentes.** Écrire $1 - H = 0{,}56$ au lieu du produit, ou $(1 - \text{moyenne des } h)^6$ ; un logarithme positif, ou $\log_{10}$ ; confondre $\ln P$ et $-H$. Pour c), donner la moyenne des risques, $0{,}0733$, ou $\frac{1 - P}{6}$. Pour e), prendre $-h - \frac{h^2}{2}$ (le terme suivant de Taylor, qui n'est pas une borne), ou $H^2$ au lieu de $\sum h_k^2$.

**Variante.** Un septième mois, avril, à $h_7 = 0{,}09$ : $P \approx 0{,}572$, entre $0{,}5583$ et $0{,}5886$.

### Ex MB5.3 — Un phoque balisé entre deux relevés : sa loi à une heure intermédiaire (le pont d'une marche aléatoire) ; puis des scénarios de position aux mêmes lois à chaque heure, tirés avec un seul nombre au hasard ou avec un bruit frais, et leur corrélation

**Réponses.** a) `[7.2353, 1.7647]` · b) `[10, 2.118]` · c) `0.7559` · d) `0.7008`.

**Démarche.** Les variances cumulées depuis 8 h valent, de 9 h à 16 h : $V = 2, 4, 6, 6{,}5, 7, 7{,}5, 8, 8{,}5$. a) À 11 h, $V_s = 6$ et $V_T = 8{,}5$ : moyenne $3 + \frac{6}{8{,}5} \times 6 \approx 7{,}2353$, variance $\frac{6 \times 2{,}5}{8{,}5} \approx 1{,}7647$. b) $\frac{V_s(8{,}5 - V_s)}{8{,}5}$ vaut, de 9 h à 15 h, $1{,}529$ ; $2{,}118$ ; $1{,}765$ ; $1{,}529$ ; $1{,}235$ ; $0{,}882$ ; $0{,}471$ : le maximum est à 10 h ($V_s = 4$, le plus proche de $\frac{V_T}{2} = 4{,}25$), et vaut $\frac{4 \times 4{,}5}{8{,}5} \approx 2{,}118$. c) Pour la marche, $X_{13\thinspace\mathrm{h}} = X_{10\thinspace\mathrm{h}} + (\text{trois déplacements indépendants})$ : $\operatorname{Cov} = V_{10\thinspace\mathrm{h}} = 4$, et la corrélation vaut $\frac{4}{\sqrt{4 \times 7}} = \sqrt{\frac47} \approx 0{,}7559$. d) Seul $U$ est commun : $\operatorname{Cov} = \sqrt{(4 - 1{,}5)(7 - 1{,}5)} = \sqrt{13{,}75} \approx 3{,}7081$, et la corrélation vaut $\frac{3{,}7081}{\sqrt{28}} \approx 0{,}7008$. Avec un seul tirage, la corrélation vaut 1 : les trois scénarios ont les mêmes lois à chaque heure, et des corrélations $0{,}76$, $1$ et $0{,}70$ ; l'écart $X_{13\thinspace\mathrm{h}} - X_{10\thinspace\mathrm{h}}$ a la variance 3 pour la marche, $(\sqrt7 - 2)^2 \approx 0{,}42$ pour un seul tirage, $11 - 2 \times 3{,}7081 \approx 3{,}58$ pour le bruit frais.

Dans ta copie : avec le bruit frais, $X_t$ est la somme de deux gaussiennes indépendantes, de variances $V_t - \sigma^2$ et $\sigma^2$ : c'est le lemme, avec $\omega^2 = V_t$. Il faut $\sigma^2 \le V_t$ à chaque heure, en particulier à 9 h, où $V = 2$ : $\sigma^2 \le 2$.

**Erreurs fréquentes.** Interpoler selon le temps ($\frac38$ du trajet : 5,25 km à 11 h) au lieu des variances cumulées ; mettre le poids $\frac{V_s}{V_T}$ sur le relevé de 8 h ; donner $V_s$ pour variance (on oublie le relevé de 16 h) ; placer le maximum au milieu de la durée (12 h) ; calculer la corrélation des scénarios avec les variances du pont, alors qu'ils ne connaissent pas le relevé de 16 h ; donner 1, la corrélation d'un seul tirage, pour la marche ; prendre le même $Z$ aux deux heures dans le scénario au bruit frais ; oublier de normaliser la covariance.

**Variante.** Avec une même variance horaire, $\frac{8{,}5}{8} = 1{,}0625$ km², pour le même $V_T$ : le maximum est à 12 h, au milieu, et vaut $\frac{8{,}5}{4} = 2{,}125$.

### Ex MB5.4 — Une voix mêlée à un bruit de fond : SNR, part de variance de la voix, logit et décibels, puis la voix retrouvée à partir d'une estimation du bruit, et l'erreur amplifiée

**Réponses.** a) `5.76` · b) `0.8521` · c) `1.7509` · d) `7.6` · e) `0.8882` · f) `-1.2` · g) `[0.4167, 6]`.

**Démarche.** a) $\frac{1{,}2^2}{0{,}5^2} = \frac{1{,}44}{0{,}25} = 5{,}76$. b) $\gamma = \frac{5{,}76}{6{,}76} \approx 0{,}8521$ (ou $\frac{1{,}44}{1{,}69}$). c) $\operatorname{logit}\gamma = \ln\frac{\gamma}{1 - \gamma} = \ln 5{,}76 \approx 1{,}7509$. d) $10\log_{10}5{,}76 \approx 7{,}6$ dB. e) $r = 10^{9/10} \approx 7{,}943$, et $\gamma = \frac{r}{1 + r} \approx 0{,}8882$ : l'enregistrement 1 (7,6 dB) n'y suffit pas. f) $\hat x = \frac{y - b\hat n}{a} = \frac{0{,}9 - 1{,}8 \times 0{,}7}{0{,}3} = \frac{-0{,}36}{0{,}3} = -1{,}2$. g) $\hat x - x = -\frac ba(\hat n - n)$ : le rapport des erreurs est $-\frac ba$, soit $\frac ba$ en valeur absolue (fiche §3), soit $\frac{0{,}5}{1{,}2} \approx 0{,}4167$ (l'erreur est réduite) et $\frac{1{,}8}{0{,}3} = 6$ (elle est multipliée par 6).

Dans ta copie : $x = \frac{y - bn}{a}$ et $\hat x = \frac{y - b\hat n}{a}$, d'où $\hat x - x = -\frac ba(\hat n - n)$.

**Erreurs fréquentes.** Inverser le SNR ; calculer a) ou b) sur l'enregistrement 2 ; prendre $\frac{b^2}{a^2 + b^2}$, la part du bruit, pour $\gamma$ ; $\log_{10}$ au lieu de $\ln$ pour le logit, ou $\ln\gamma$ ; $10\ln$ pour les décibels, ou oublier le facteur 10 ; lire 9 dB comme un SNR de 9, prendre $e^{0{,}9}$, ou s'arrêter au seuil $r$ sans passer à la part $\gamma$ ; $\frac{1}{1 + r}$ au lieu de $\frac{r}{1 + r}$. Pour f), oublier le gain $b$ du bruit, oublier de diviser par $a$, ou ajouter $b\hat n$. Pour g), $\frac ab$, ou oublier de diviser $b$ par $a$.

**Variante.** Pour que l'erreur de l'enregistrement 2 ne soit multipliée que par 3, il faudrait $\frac ba = 3$, soit $a = 0{,}6$ à bruit égal : un SNR de $\frac19$, un gain de la voix deux fois plus grand (quatre fois plus de variance), en enregistrant plus près.

### Ex MB5.5 — Débruiter un signal reçu, d'abord gaussien, puis émis à deux niveaux ±c : E[x | y] par M25a et par la formule de Tweedie (une tanh), et ce que rend le débruiteur quand le bruit tend vers 0

**Réponses.** a) `2.28` · b) `-0.16` · c) `0.48` · d) `1.601` · e) `0.2995` · f) `2`.

**Démarche.** Partie A : $y \sim \mathcal{N}(am, a^2\tau^2 + b^2) = \mathcal{N}(2, 25)$. a) $\mathbb{E}[x \mid y] = m + \frac{a\tau^2}{a^2\tau^2 + b^2}(y - am) = 1 + \frac{8}{25} \times 4 = 2{,}28$. b) $s_Y(y) = -\frac{y - 2}{25}$, et $s_Y(6) = -0{,}16$. c) $\mathbb{E}[n \mid y] = -b\thinspace s_Y(y) = 0{,}48$ ; contrôle : $2 \times 2{,}28 + 3 \times 0{,}48 = 6$. Partie B : $p_Y(y) = \frac12\mathcal{N}(y \mid 1, 1) + \frac12\mathcal{N}(y \mid -1, 1)$. d) Par Bayes, $\mathbb{E}[x \mid y] = 2\thinspace\frac{e^{-(y-1)^2/2} - e^{-(y+1)^2/2}}{e^{-(y-1)^2/2} + e^{-(y+1)^2/2}} = 2\tanh(y)$, soit $2\tanh(1{,}1) \approx 2 \times 0{,}80050 \approx 1{,}6010$. e) $\mathbb{E}[n \mid y] = \frac{y - a\thinspace\mathbb{E}[x \mid y]}{b} = 1{,}1 - 0{,}5 \times 1{,}6010 \approx 0{,}2995$. f) En général, $\mathbb{E}[x \mid y] = c\tanh\big(\frac{acy}{b^2}\big)$ : pour $y = 1{,}1 > 0$, l'argument tend vers $+\infty$ et la tanh vers 1 : la limite vaut $c = 2$, le niveau de même signe que $y$ (en $y = 0$, la tanh vaudrait 0 pour tout $b$ : la moyenne des deux niveaux).

Dans ta copie : par Tweedie, $\mathbb{E}[x \mid y = 6] = \frac{6 + 9 \times (-0{,}16)}{2} = \frac{4{,}56}{2} = 2{,}28$, la valeur de a). Pour la partie B, $s_Y(y) = -\frac{y}{b^2} + \frac{ac}{b^2}\tanh\big(\frac{acy}{b^2}\big)$, et $\frac{y + b^2s_Y(y)}{a} = c\tanh\big(\frac{acy}{b^2}\big)$.

**Erreurs fréquentes.** Pour a), répondre $\frac ya = 3$, qui ignore la loi de $x$ et le bruit ; la variance de $y$ écrite $\tau^2 + b^2$, l'écart $y - m$ au lieu de $y - am$, ou un gain sans le facteur $a$ au numérateur. Pour b), oublier le signe moins, ou centrer sur $m$ au lieu de $am$. Pour c), oublier le signe moins, ou partir de la moyenne a priori au lieu de $\mathbb{E}[x \mid y]$. Pour d), oublier $a$ dans l'argument de la tanh, ou oublier le facteur $c$. Pour f), répondre $\frac ya = 2{,}2$ : le débruiteur ne rend que des niveaux possibles ; ou prendre le niveau de signe opposé à $y$.

**Variante.** Avec $b = 0{,}7$ dans la partie B, $\mathbb{E}[x \mid y = 1{,}1] = 2\tanh\big(\frac{1{,}1}{0{,}49}\big) \approx 1{,}9556$ : moins de bruit, plus près de $c$.

### Ex MB5.6 — Un bit altéré par deux relais, puis reconstitué par un modèle retour : ln p(x), l'ELBO de la loi aller des relais, et sa décomposition en reconstruction, KL finale et KL d'un pas retour

**Réponses.** a) `[0.444, 0.556]` · b) `[0.7027, 0.8417]` · c) `-0.7962` · d) `-1.017` · e) `[-0.5515, 0.1409, 0.3246]`.

**Démarche.** Pour $x = 1$ : $q(z_1 \mid x) = (0{,}22 ;\ 0{,}78)$ (pour $z_1 = 0$ puis 1). a) La ligne $(0{,}22 ;\ 0{,}78)$ fois la matrice du second relais $\begin{pmatrix} 0{,}6 & 0{,}4 \cr 0{,}4 & 0{,}6 \end{pmatrix}$ : $q(z_2 = 0 \mid x) = 0{,}132 + 0{,}312 = 0{,}444$ et $q(z_2 = 1 \mid x) = 0{,}088 + 0{,}468 = 0{,}556$. b) Bayes : $q(z_1 = 1 \mid z_2 = 0, x) = \frac{0{,}312}{0{,}444} \approx 0{,}7027$ et $q(z_1 = 1 \mid z_2 = 1, x) = \frac{0{,}468}{0{,}556} \approx 0{,}8417$. c) $p(x = 1) = 0{,}7 \times (0{,}84 \times 0{,}32 + 0{,}16 \times 0{,}68) + 0{,}3 \times (0{,}16 \times 0{,}32 + 0{,}84 \times 0{,}68) = 0{,}26432 + 0{,}18672 = 0{,}45104$, et $\ln 0{,}45104 \approx -0{,}7962$. e) La reconstruction $0{,}22\ln 0{,}32 + 0{,}78\ln 0{,}68 \approx -0{,}2507 - 0{,}3008 = -0{,}5515$ ; la KL finale $0{,}444\ln\frac{0{,}444}{0{,}7} + 0{,}556\ln\frac{0{,}556}{0{,}3} \approx -0{,}2021 + 0{,}3430 = 0{,}1409$ ; le pas retour : sachant $z_2 = 0$, $\mathrm{KL}\big((0{,}2973 ;\ 0{,}7027) \thinspace\Vert\thinspace (0{,}84 ;\ 0{,}16)\big) \approx 0{,}7310$, sachant $z_2 = 1$, $\mathrm{KL}\big((0{,}1583 ;\ 0{,}8417) \thinspace\Vert\thinspace (0{,}16 ;\ 0{,}84)\big) \approx 0{,}00001$, en moyenne sous $q(z_2 \mid x)$ : $0{,}444 \times 0{,}7310 + 0{,}556 \times 0{,}00001 \approx 0{,}3246$. d) Par la décomposition, $\operatorname{ELBO} = -0{,}5515 - 0{,}1409 - 0{,}3246 \approx -1{,}0170$ (la somme directe sur les quatre couples $(z_1, z_2)$ donne la même valeur).

Dans ta copie : $\big(q(z_2 \mid x)\big)_{x, z_2} = \begin{pmatrix} 0{,}78 & 0{,}22 \cr 0{,}22 & 0{,}78 \end{pmatrix}\begin{pmatrix} 0{,}6 & 0{,}4 \cr 0{,}4 & 0{,}6 \end{pmatrix} = \begin{pmatrix} 0{,}556 & 0{,}444 \cr 0{,}444 & 0{,}556 \end{pmatrix}$ (lignes $x = 0$ et $x = 1$) ; et $-1{,}0170 < -0{,}7962$ : l'ELBO reste sous $\ln p(x = 1)$, d'un écart de $0{,}2208$, la KL de $q(z_1, z_2 \mid x)$ à la loi a posteriori du modèle.

**Erreurs fréquentes.** Pour a), ne garder que le second relais ($0{,}4$ et $0{,}6$), ou donner d'abord $q(z_2 = 1 \mid x)$. Pour b), normaliser $q(z_2 \mid z_1)$ seule, sans l'a priori $q(z_1 \mid x)$, oublier de diviser par $q(z_2 \mid x)$, ou garder $q(z_1 = 1 \mid x) = 0{,}78$ sans conditionner sur $z_2$. Pour c), partir de $q(z_2 \mid x)$ au lieu de $p(z_2)$, ou oublier le signe. Pour d), ajouter les deux KL au lieu de les retirer ($-0{,}0860$), ou ajouter l'écart au lieu de le retirer. Pour e), écrire $\mathrm{KL}(p \thinspace\Vert\thinspace q)$, ou moyenner les deux KL du pas retour avec des poids égaux au lieu de $q(z_2 \mid x)$.

**Variante.** Si le modèle prenait $p(z_2) = q(z_2 \mid x = 1) = (0{,}444 ;\ 0{,}556)$, la KL finale serait nulle, l'ELBO vaudrait $-0{,}5515 - 0{,}3246 = -0{,}8761$, et $\ln p(x = 1) = \ln(0{,}444 \times 0{,}3776 + 0{,}556 \times 0{,}6224) \approx -0{,}6661$.

### Ex MB5.7 — La date de floraison d'une variété et celle de tout le verger, deux lois gaussiennes : la loi p_v^{1+w} p_g^{−w} pour deux valeurs de w, son score, sa condition d'existence et le w limite

**Réponses.** a) `19.5841` · b) `101.4197` · c) `[100.7583, 13.4106]` · d) `0.3548` · e) `1.2857`.

**Démarche.** $\lambda(w) = \frac{1 + w}{25} - \frac{w}{81}$, et $\lambda(w)\thinspace\mu(w) = \frac{(1 + w) \times 102}{25} - \frac{w \times 108}{81}$. a) $\lambda(0{,}4) = 0{,}056 - 0{,}004938 = 0{,}0510617$, variance $\frac{1}{\lambda} \approx 19{,}5841$. b) $\lambda\mu = 5{,}712 - 0{,}53333 = 5{,}17867$, d'où $\mu \approx 101{,}4197$. c) $\lambda(1{,}25) = 0{,}09 - 0{,}015432 = 0{,}0745679$ (variance $\approx 13{,}4106$) ; $\lambda\mu = 9{,}18 - 1{,}66667 = 7{,}51333$, $\mu \approx 100{,}7583$. d) Les deux scores en 96 : $s_v = -\frac{96 - 102}{25} = 0{,}24$ et $s_g = -\frac{96 - 108}{81} \approx 0{,}148148$ ; $(1 + w)\thinspace s_v - w\thinspace s_g = 2{,}25 \times 0{,}24 - 1{,}25 \times 0{,}148148 \approx 0{,}3548$, ce que donne aussi $-\lambda\thinspace(96 - \mu) = -0{,}0745679 \times (96 - 100{,}7583)$. e) $\frac{1 + w}{144} - \frac{w}{81} > 0 \iff w\big(\frac{1}{81} - \frac{1}{144}\big) < \frac{1}{144} \iff w < \frac{81}{144 - 81} = \frac97 \approx 1{,}2857$.

Dans ta copie : $\lambda(w) = \frac{1 + w}{25} - \frac{w}{81} = \frac{1}{25} + w\big(\frac{1}{25} - \frac{1}{81}\big)$ ; la moyenne est poussée sous 102, du côté opposé à 108 (101,42 puis 100,76) : la floraison guidée est plus précoce que celle de la variété, et plus étroite ; comme $25 < 81$, $\lambda(w) \ge \frac{1}{25} > 0$ pour tout $w \ge 0$ : pas de $w$ limite.

**Erreurs fréquentes.** Ajouter $\frac{w}{81}$ au lieu de le retirer ; combiner les variances au lieu des précisions ; oublier le facteur $1 + w$ devant la précision de $p_v$ ; pour a), donner la précision $\lambda(w)$ au lieu de la variance. Pour b), pousser la moyenne vers 108 au lieu de l'en éloigner. Pour b) et c), prendre la combinaison affine des moyennes, $(1 + w) \times 102 - w \times 108$, qui ignore les précisions. Pour d), oublier le signe du score, ou ajouter $w\thinspace s_g$. Pour e), écrire $w^\star = \frac{144}{144 - 81}$, ou $\frac{81}{144}$.

**Variante.** Pour $w = -0{,}5$, on interpole : $\lambda = \frac{0{,}5}{25} + \frac{0{,}5}{81}$, une variance d'environ $38{,}2$ et une moyenne d'environ $103{,}4$, entre 102 et 108.

### Ex MB5.8 — Une tasse de thé qui refroidit : Euler et point milieu contre la solution exacte, l'erreur quand le pas est divisé par deux, un courant de vitesse constante, et un calcul à rebours

**Réponses.** a) `55.67` · b) `[51.85, 53.93]` · c) `[56.08, 55.76]` · d) `[2.2, 4.5]` · e) `[55.1, 56.45]`.

**Démarche.** $T(t) = 20 + 65\thinspace e^{-0{,}06t}$. a) $20 + 65\thinspace e^{-0{,}6} \approx 20 + 65 \times 0{,}548812 \approx 55{,}67$. b) Chaque pas d'Euler multiplie l'écart à 20 °C par $1 - 0{,}06h$ : $0{,}7$ pour $h = 5$, d'où $20 + 65 \times 0{,}7^2 = 51{,}85$ ; $0{,}85$ pour $h = 2{,}5$, d'où $20 + 65 \times 0{,}85^4 \approx 53{,}93$. c) Chaque pas du point milieu multiplie l'écart par $1 - rh + \frac{(rh)^2}{2}$ (avec le taux $r = 0{,}06$) : $0{,}745$ pour $h = 5$, d'où $20 + 65 \times 0{,}745^2 \approx 56{,}08$ ; $0{,}86125$ pour $h = 2{,}5$, d'où $\approx 55{,}76$. d) Les erreurs : Euler $-3{,}8228$ puis $-1{,}7424$, rapport $\approx 2{,}2$ ; point milieu $0{,}4039$ puis $0{,}0899$, rapport $\approx 4{,}5$. e) $h = -5$ : $47 + (-5) \times \big(-0{,}06 \times 27\big) = 55{,}1$ ; exactement, $20 + 27\thinspace e^{0{,}3} \approx 56{,}45$.

Dans ta copie : la vitesse de la feuille ne change pas, sa trajectoire est une droite, et la tangente la suit exactement : un pas, de n'importe quelle durée, tombe sur elle. La courbe du thé est convexe ($T'' = 0{,}06^2(T - 20) > 0$) : en remontant le temps, la pente devient plus raide que celle lue à 10 min ; le pas à rebours garde la pente de 10 min, trop faible, et sous-estime la remontée.

**Erreurs fréquentes.** Faire décroître la température entière au lieu de l'écart à 20 °C ; prendre un seul pas pour la solution exacte ; donner les deux valeurs dans l'autre ordre ; pour le point milieu, faire un pas entier d'Euler avant de lire la vitesse ; pour d), diviser l'erreur du petit pas par celle du grand, les valeurs au lieu des erreurs, des températures arrondies à 2 décimales (le point milieu donnerait 4,6), ou les rapports de la théorie, 2 et 4 ; pour e), faire remonter la température entière au lieu de l'écart à 20 °C, ou donner deux fois la valeur du pas d'Euler.

**Variante.** Avec $h = 1{,}25$ (8 pas) : Euler donne $54{,}84$ (une erreur de $0{,}84$, encore divisée par $2{,}1$), le point milieu $55{,}69$ (une erreur de $0{,}021$, divisée par $4{,}2$).

### Ex MB5.9 — Le chemin droit d'un bruit N(0, 1) vers une loi N(m, τ²) : le champ moyen (affine en x), un pas d'Euler depuis s = 1 qui rend m pour tout départ, puis deux pas, et l'écart-type obtenu contre τ

**Réponses.** a) `0.3125` · b) `-4.6` · c) `4` · d) `3.86` · e) `[0.2, 3.65]`.

**Démarche.** $x_s$ est une mesure de $x_0$ de gains $1 - s$ et $s$ : $x_s \sim \mathcal{N}\big((1 - s)m, \sigma(s)^2\big)$, $\sigma(s)^2 = (1 - s)^2\tau^2 + s^2$, et le modèle linéaire gaussien donne $\mathbb{E}[x_0 \mid x_s = x] = m + \frac{(1 - s)\tau^2}{\sigma(s)^2}\big(x - (1 - s)m\big)$. a) $\sigma(0{,}5)^2 = 0{,}25 \times 0{,}25 + 0{,}25 = 0{,}3125$. b) $\mathbb{E}[x_0 \mid x_{0{,}5} = 1{,}5] = 4 + \frac{0{,}125}{0{,}3125}(1{,}5 - 2) = 3{,}8$, et $v = \frac{1{,}5 - 3{,}8}{0{,}5} = -4{,}6$. c) $v(z, 1) = z - 4 = -4{,}7$, et $z + (-1) \times (-4{,}7) = 4$. d) Premier pas : $x = -0{,}7 - 0{,}5 \times (-4{,}7) = 1{,}65$ ; en $s = 0{,}5$, $\mathbb{E}[x_0 \mid x_{0{,}5} = 1{,}65] = 4 + 0{,}4 \times (-0{,}35) = 3{,}86$, $v = \frac{1{,}65 - 3{,}86}{0{,}5} = -4{,}42$, et $x = 1{,}65 + 0{,}5 \times 4{,}42 = 3{,}86$. e) Les deux pas envoient $z$ sur $m + \frac{\tau^2}{1 + \tau^2}z = 4 + 0{,}2z$ : l'écart-type obtenu vaut $0{,}2$, contre $\tau = 0{,}5$ ; la trajectoire exacte arrive en $m + \tau z = 4 - 0{,}35 = 3{,}65$.

Dans ta copie : en $s = 1$, $x_1 = \varepsilon$ est indépendant de $x_0$, donc $\mathbb{E}[x_0 \mid x_1 = x] = m$ et $v(x, 1) = x - m$. En deux pas : $x_{1/2} = \frac{z + m}{2}$, puis $v\big(x_{1/2}, \frac12\big) = -m + \frac{1 - \tau^2}{1 + \tau^2}z$, et $x = m + \frac{\tau^2}{1 + \tau^2}z$ : $\kappa = 0{,}2$. Le dernier pas, de $s$ à 0 avec $h = -s$, rend $x - s\thinspace v(x, s) = \mathbb{E}[x_0 \mid x_s = x]$ : un débruitage complet, qui écrase la dispersion.

**Erreurs fréquentes.** Pour a), oublier la part du bruit, $s^2$, ou celle de la donnée. Pour b), oublier de diviser par $s$, ou écrire l'écart $x - m$ au lieu de $x - (1 - s)m$. Pour c), un pas de durée $\frac12$, $v(x, 1) = -m$, ou le point d'arrivée exact $m + \tau z$. Pour d), lire le champ du second pas au départ $z$, ou en $s = 1$, ou donner le point d'arrivée exact. Pour e), répondre l'écart-type 0 d'un seul pas, $\tau$ lui-même, ou un signe faux dans $m + \tau z$.

**Variante.** Pour $\tau = 1{,}2$, deux pas donnent un écart-type $\frac{1{,}44}{2{,}44} \approx 0{,}590$, contre $1{,}2$ : deux pas d'Euler resserrent toujours la loi.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB5.10 — La récurrence linéaire gaussienne à coefficients quelconques : la loi de x_t sachant x_0 ; à coefficient constant |a| < 1, la loi sachant un instant passé, la loi stationnaire et la convergence depuis toute loi initiale ; aucune loi stationnaire si |a| ≥ 1

**Démonstration.**
1. Pour $t = 1$ : $x_1 = a_1x_0 + b_1\varepsilon_1$, la formule (les produits vides valent 1). Si la formule vaut au rang $t - 1$, alors $x_t = a_tx_{t-1} + b_t\varepsilon_t = (a_1\cdots a_t)x_0 + \sum_{k=1}^{t-1}b_k(a_{k+1}\cdots a_{t-1})\thinspace a_t\thinspace\varepsilon_k + b_t\varepsilon_t$, qui est la formule au rang $t$. Sachant $x_0$, $x_t$ est une constante plus une combinaison linéaire des bruits $\varepsilon_1, \ldots, \varepsilon_t$, indépendants entre eux et de $x_0$ (donc de même loi sachant $x_0$) : elle est gaussienne, de moyenne $(a_1\cdots a_t)x_0$ (les bruits sont centrés) et de variance $\sum_kb_k^2(a_{k+1}\cdots a_t)^2$ (la variance d'une somme de variables indépendantes, M02b).
2. Pour $u > s$, $x_u = ax_{u-1} + b\varepsilon_u$ : le processus $(x_s, x_{s+1}, \ldots)$ suit la même récurrence, partie de $x_s$, avec les bruits $\varepsilon_{s+1}, \ldots, \varepsilon_t$, indépendants de $x_s$ (qui ne dépend que de $x_0$ et des bruits d'avant). La question 1, appliquée à ce processus avec $t - s$ pas de coefficients $a$ et $b$, donne la moyenne $a^{t-s}x_s$ et la variance $b^2\sum_{j=0}^{t-s-1}a^{2j} = b^2\frac{1 - a^{2(t-s)}}{1 - a^2}$ (somme géométrique, R5, valable car $a^2 \ne 1$).
3. Si $x_0 \sim \mathcal{N}(0, v_\infty)$, indépendant de $\varepsilon_1$, alors $x_1 = ax_0 + b\varepsilon_1$ est gaussienne, de moyenne 0 et de variance $a^2v_\infty + b^2 = \frac{a^2b^2 + b^2(1 - a^2)}{1 - a^2} = v_\infty$ : $x_1$ a la même loi, et par récurrence chaque $x_t$. Depuis $x_0 \sim \mathcal{N}(m_0, v_0)$ : $m_t = am_{t-1}$, donc $m_t = a^tm_0$ ; $v_t = a^2v_{t-1} + b^2$ et $v_\infty = a^2v_\infty + b^2$, d'où $v_t - v_\infty = a^2(v_{t-1} - v_\infty)$, et $v_t - v_\infty = a^{2t}(v_0 - v_\infty)$. Comme $\lvert a\rvert < 1$, $m_t \to 0$ et $v_t \to v_\infty$ : la loi $\mathcal{N}(m_t, v_t)$ de $x_t$ tend vers la loi stationnaire, quel que soit le départ ; l'écart de moyenne décroît comme $\lvert a\rvert^t$, celui de variance comme $a^{2t}$.
4. Si une loi de variance finie $v$ était stationnaire, $x_1 = ax_0 + b\varepsilon_1$, somme de deux termes indépendants, aurait la variance $a^2v + b^2$ ; la stationnarité imposerait $v = a^2v + b^2$, soit $(1 - a^2)\thinspace v = b^2 > 0$, impossible quand $a^2 \ge 1$ et $v \ge 0$. Pour $a = 1$ : $v_t = v_{t-1} + b^2$, donc $v_t = v_0 + tb^2$, qui croît sans borne.

**Grille de relecture.** 1 : l'initialisation et l'hérédité écrites, avec le produit vide ; la gaussianité par une combinaison de bruits indépendants entre eux et de $x_0$ (M25a), la moyenne et la variance justifiées. 2 : la récurrence repartie de $x_s$, l'indépendance de $x_s$ et des bruits suivants (la propriété de Markov), la somme géométrique et la condition $a^2 \ne 1$. 3 : l'invariance vérifiée (la loi de $x_1$, pas seulement sa variance) ; les deux écarts et leurs facteurs ; la conclusion pour tout départ. 4 : l'argument par la variance, avec $b \ne 0$ ; le cas $a = 1$. Une démonstration de 3 qui part de la question 2, en faisant tendre $s$ vers $-\infty$, n'est pas demandée.

**Variante.** Pour $a = -1$, $v_t = v_0 + tb^2$ aussi, et la moyenne change de signe à chaque pas : pas plus de loi stationnaire que pour la marche aléatoire.

### Ex MB5.11 — La meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + E[(E[Y | X] − g(X))²], donc g = E[Y | X] ; sur un échantillon, la moyenne de chaque groupe

**Démonstration.**
1. Notons $\mu_k = \mathbb{E}[Y \mid X = \xi_k]$. Sachant $X = \xi_k$, $(Y - c)^2 = (Y - \mu_k)^2 + 2(Y - \mu_k)(\mu_k - c) + (\mu_k - c)^2$. En prenant l'espérance sachant $X = \xi_k$, le terme du milieu donne $2(\mu_k - c)\thinspace\mathbb{E}[Y - \mu_k \mid X = \xi_k] = 0$, d'où $\mathbb{E}[(Y - c)^2 \mid X = \xi_k] = \mathbb{V}(Y \mid X = \xi_k) + (\mu_k - c)^2$ (l'identité de M02c §1, sous la loi conditionnelle).
2. Par la formule des probabilités totales (M25b §2), $\mathbb{E}[(Y - g(X))^2] = \sum_kp_k\thinspace\mathbb{E}[(Y - g(\xi_k))^2 \mid X = \xi_k]$ ; avec $c = g(\xi_k)$ dans la question 1, c'est $\sum_kp_k\thinspace\mathbb{V}(Y \mid X = \xi_k) + \sum_kp_k(\mu_k - g(\xi_k))^2 = \mathbb{E}[\mathbb{V}(Y \mid X)] + \mathbb{E}\big[(\mathbb{E}[Y \mid X] - g(X))^2\big]$. Le premier terme ne dépend pas de $g$, le second est positif ou nul, et nul exactement quand $g(\xi_k) = \mu_k$ pour tout $k$ (les $p_k$ étant positifs) : la MSE est minimale pour $g(X) = \mathbb{E}[Y \mid X]$, et son minimum vaut $\mathbb{E}[\mathbb{V}(Y \mid X)]$.
3. La loi empirique de l'échantillon donne à chaque couple le poids $\frac1n$ ; sous cette loi, $X$ est discrète, de valeurs les $\xi$ observés, de probabilités $\frac{n_\xi}{n}$, et la MSE empirique est $\mathbb{E}[(Y - g(X))^2]$. Par 2, la meilleure $g$ vaut, en $\xi$, l'espérance de $Y$ sachant $X = \xi$ sous cette loi : la moyenne $\bar y_\xi$ des $y_i$ du groupe. Le minimum vaut $\sum_\xi\frac{n_\xi}{n}\thinspace\hat\sigma_\xi^2$, où $\hat\sigma_\xi^2 = \frac{1}{n_\xi}\sum_{x_i = \xi}(y_i - \bar y_\xi)^2$ est la variance empirique du groupe.

**Grille de relecture.** 1 : le développement du carré, le terme croisé nul par la définition de l'espérance conditionnelle (ou la propriété de la tour), le résultat. 2 : la formule des probabilités totales, la substitution $c = g(\xi_k)$, la positivité du second terme, le cas d'égalité (pour tout $k$, grâce à $p_k > 0$), et le minimum. 3 : la loi empirique comme une loi discrète, l'application de 2, la moyenne et la variance de chaque groupe (en divisant par $n_\xi$, pas $n_\xi - 1$). Une preuve qui développe directement $\mathbb{E}[(Y - \mathbb{E}[Y \mid X] + \mathbb{E}[Y \mid X] - g(X))^2]$ et annule le terme croisé par la tour est correcte aussi.

**Variante.** Pour les douze appartements de la fiche (§4), le minimum vaut $\frac{650 + 800 + 1\thinspace000}{12} \approx 204{,}2$ : $\frac{4}{12} \times 162{,}5 + \frac{3}{12} \times 266{,}7 + \frac{5}{12} \times 200$.

### Ex MB5.12 — La formule de Tweedie : dériver la densité de y = a x + b n sous l'espérance, d'où E[x | y] et E[n | y] ; la vérification quand x est gaussien

**Démonstration.**
1. Sachant $x = \xi_k$, $y = a\xi_k + bn$ a la densité $\varphi_b(y - a\xi_k)$ ; par la formule des probabilités totales, $p_Y(y) = \sum_k\pi_k\thinspace\varphi_b(y - a\xi_k)$. Comme $\varphi_b(u) = \frac{1}{\sqrt{2\pi}b}e^{-u^2/(2b^2)}$ a pour dérivée $\varphi_b'(u) = -\frac{u}{b^2}\varphi_b(u)$, une somme finie se dérive terme à terme : $p_Y'(y) = -\frac{1}{b^2}\sum_k\pi_k(y - a\xi_k)\thinspace\varphi_b(y - a\xi_k)$.
2. Par Bayes, $P(x = \xi_k \mid y) = \frac{\pi_k\thinspace\varphi_b(y - a\xi_k)}{p_Y(y)}$. En divisant 1 par $p_Y(y)$ : $s_Y(y) = \frac{p_Y'(y)}{p_Y(y)} = -\frac{1}{b^2}\sum_kP(x = \xi_k \mid y)\thinspace(y - a\xi_k) = -\frac{y - a\thinspace\mathbb{E}[x \mid y]}{b^2}$. D'où, pour $a \ne 0$, $\mathbb{E}[x \mid y] = \frac{y + b^2s_Y(y)}{a}$. Et $n = \frac{y - ax}{b}$, donc $\mathbb{E}[n \mid y] = \frac{y - a\thinspace\mathbb{E}[x \mid y]}{b} = -b\thinspace s_Y(y)$ (cette dernière vaut aussi pour $a = 0$).
3. Avec une densité, $p_Y(y) = \int p_X(u)\thinspace\varphi_b(y - au)\thinspace\mathrm{d}u$ ; en dérivant sous l'intégrale (admis), $p_Y'(y) = -\frac{1}{b^2}\int(y - au)\thinspace p_X(u)\thinspace\varphi_b(y - au)\thinspace\mathrm{d}u$, et la loi a posteriori a la densité $\frac{p_X(u)\thinspace\varphi_b(y - au)}{p_Y(y)}$ : le même calcul, avec une intégrale, donne les mêmes formules.
4. Pour $x \sim \mathcal{N}(m, \tau^2)$, $y \sim \mathcal{N}(am, a^2\tau^2 + b^2)$ et $s_Y(y) = -\frac{y - am}{a^2\tau^2 + b^2}$. Tweedie donne $\mathbb{E}[x \mid y] = \frac1a\Big(y - \frac{b^2(y - am)}{a^2\tau^2 + b^2}\Big) = \frac1a\Big(am + (y - am)\frac{a^2\tau^2}{a^2\tau^2 + b^2}\Big) = m + \frac{a\tau^2}{a^2\tau^2 + b^2}(y - am)$, la moyenne a posteriori du modèle linéaire gaussien (M25a §5).

**Grille de relecture.** 1 : $p_Y$ par les probabilités totales, la dérivée de $\varphi_b$, la dérivation d'une somme finie. 2 : les probabilités a posteriori par Bayes, la division par $p_Y(y)$ (strictement positive), la reconnaissance de $\mathbb{E}[x \mid y]$, les deux formules, et $a \ne 0$ pour la première. 3 : l'intégrale, l'hypothèse de dérivation sous l'intégrale nommée. 4 : la loi de $y$, son score, et le calcul jusqu'à la forme de M25a.

**Variante.** En dimension $d$ (énoncé) : $\mathbb{E}[\mathbf{x} \mid \mathbf{y}] = \frac{\mathbf{y} + b^2\nabla\ln p_Y(\mathbf{y})}{a}$ ; le même calcul, coordonnée par coordonnée, avec $\nabla\varphi_b(\mathbf{u}) = -\frac{\mathbf{u}}{b^2}\varphi_b(\mathbf{u})$.

### Ex MB5.13 — L'ELBO d'une chaîne de latents : Markov et Bayes réécrivent chaque pas aller, la somme télescope ; puis chaque KL entre gaussiennes de même variance devient une MSE pondérée des moyennes

**Démonstration.**
1. Le processus aller est markovien : sachant $z_{t-1}$, la loi de $z_t$ ne dépend plus de $x$, donc $q(z_t \mid z_{t-1}) = q(z_t \mid z_{t-1}, x)$. La formule de Bayes, sous la loi $q(\cdot \mid x)$, donne $q(z_t \mid z_{t-1}, x) = \frac{q(z_{t-1} \mid z_t, x)\thinspace q(z_t \mid x)}{q(z_{t-1} \mid x)}$.
2. $\ln q(z_{1:T} \mid x) = \ln q(z_1 \mid x) + \sum_{t=2}^T\big[\ln q(z_{t-1} \mid z_t, x) + \ln q(z_t \mid x) - \ln q(z_{t-1} \mid x)\big]$ ; la somme des $\ln q(z_t \mid x) - \ln q(z_{t-1} \mid x)$ télescope (R4) en $\ln q(z_T \mid x) - \ln q(z_1 \mid x)$, d'où $\ln q(z_{1:T} \mid x) = \ln q(z_T \mid x) + \sum_{t=2}^T\ln q(z_{t-1} \mid z_t, x)$.
3. Avec $\ln p(x, z_{1:T}) = \ln p(z_T) + \sum_{t=2}^T\ln p(z_{t-1} \mid z_t) + \ln p(x \mid z_1)$ :
$\operatorname{ELBO} = \mathbb{E} _q[\ln p(x \mid z_1)] - \mathbb{E} _q\Big[\ln\frac{q(z_T \mid x)}{p(z_T)}\Big] - \sum  _{t=2}^T\mathbb{E}  _q\Big[\ln\frac{q(z  _{t-1} \mid z_t, x)}{p(z  _{t-1} \mid z_t)}\Big]$. Le deuxième terme ne fait intervenir que $z_T$, de loi $q(z_T \mid x)$ : c'est $\mathrm{KL}\big(q(z_T \mid x) \thinspace\Vert\thinspace p(z_T)\big)$. Dans le terme $t$, on prend d'abord l'espérance sachant $z_t$ (propriété de la tour), où $z _{t-1}$ suit $q(z _{t-1} \mid z_t, x)$ : c'est $\mathrm{KL}\big(q(z _{t-1} \mid z_t, x) \thinspace\Vert\thinspace p(z _{t-1} \mid z_t)\big)$, puis l'espérance en $z_t$.
4. La KL de deux gaussiennes de même variance $\sigma^2$ vaut $\frac{(\mu_q - \mu_p)^2}{2\sigma^2}$ (M25a §7) : le terme du pas $t$ est $-\mathbb{E}_q\big[\frac{(\mu_q - \mu_p)^2}{2\sigma^2}\big]$, où $\mu_q$ dépend de $(z_t, x)$ et $\mu_p$ de $z_t$. Maximiser l'ELBO, c'est minimiser la moyenne de $(\mu_q - \mu_p)^2$, une erreur quadratique moyenne entre deux moyennes, pesée par $\frac{1}{2\sigma^2}$ : une MSE pondérée.

**Grille de relecture.** 1 : Markov invoqué pour retirer $x$, Bayes sous $q(\cdot \mid x)$. 2 : le remplacement terme à terme et le télescopage, sans oublier $q(z_1 \mid x)$, qui s'annule. 3 : la factorisation du modèle, le regroupement en trois sortes de termes, la KL finale (une espérance sur $z_T$ seul), la tour pour chaque terme du milieu, et les signes (on retire les KL). 4 : la formule admise, le poids $\frac{1}{2\sigma^2}$, et ce qui dépend de quoi. Les latents peuvent être continus : les sommes deviennent des intégrales, rien d'autre ne change.

**Variante.** Pour $T = 1$, la somme est vide et l'on retrouve l'ELBO d'un latent de M25b §5 : $\mathbb{E}_q[\ln p(x \mid z_1)] - \mathrm{KL}\big(q(z_1 \mid x) \thinspace\Vert\thinspace p(z_1)\big)$.

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB5.14 — Pont : une loss de débruitage à plusieurs niveaux de bruit, son minimiseur à chaque niveau, et pour des données gaussiennes les MSE minimales sur le signal et sur le bruit, dont le rapport est le SNR

**Réponses.** a) `0.4146` · b) `[0.8288, 0.2951, 0.0385]` · c) `[0.1712, 0.7049, 0.9615]` · d) `0.5106`.

**Démarche.** À chaque niveau, $(x, n, y)$ est un vecteur gaussien centré, avec $\mathbb{V}(y) = a^2 + b^2$, $\operatorname{Cov}(n, y) = b$ et $\operatorname{Cov}(x, y) = a$ ; d'où $\mathbb{E}[n \mid y] = \frac{b}{a^2 + b^2}\thinspace y$ et $\mathbb{E}[x \mid y] = \frac{a}{a^2 + b^2}\thinspace y$ (M25a). a) $\frac{1{,}7}{1{,}21 + 2{,}89} = \frac{1{,}7}{4{,}1} \approx 0{,}4146$. b) $1 - \frac{b^2}{a^2 + b^2} = \frac{a^2}{a^2 + b^2} = \gamma_k$ : $\frac{4{,}84}{5{,}84} \approx 0{,}8288$, $\frac{1{,}21}{4{,}1} \approx 0{,}2951$, $\frac{0{,}25}{6{,}5} \approx 0{,}0385$. c) $1 - \frac{a^2}{a^2 + b^2} = 1 - \gamma_k$ : $0{,}1712$ ; $0{,}7049$ ; $0{,}9615$. d) $0{,}5 \times 0{,}8288 + 0{,}3 \times 0{,}2951 + 0{,}2 \times 0{,}0385 \approx 0{,}5106$.

Dans ta copie : $L$ est une somme pondérée, sur $k$, de termes dont chacun ne dépend que de $g(\cdot, k)$ ; on minimise chacun séparément, et le §4 dit que le minimiseur est $\mathbb{E}[n \mid y]$ à chaque niveau. Le rapport de b) à c) vaut $\frac{\gamma_k}{1 - \gamma_k} = \operatorname{SNR}_k = \frac{a_k^2}{b_k^2}$ : au niveau 2, $\frac{0{,}2951}{0{,}7049} \approx 0{,}4187 = \frac{1{,}21}{2{,}89}$.

**Erreurs fréquentes.** Prendre $\operatorname{Cov}(x, y)$ au lieu de $\operatorname{Cov}(n, y)$ ; se tromper de niveau ; confondre la MSE sur le bruit et celle sur le signal ; prendre la MSE de la prédiction 0 (qui vaut 1), ou ajouter $\frac{\operatorname{Cov}^2}{\mathbb{V}(y)}$ au lieu de le retirer ; une moyenne simple, ou une somme, des trois niveaux en d).

**Variante.** Une loss qui ferait prédire le signal, $\sum_k\omega_k\thinspace\mathbb{E}[(x - g(y, k))^2]$, aurait pour minimum $\sum_k\omega_k(1 - \gamma_k) \approx 0{,}4894$ ; les niveaux s'y pèsent autrement, puisque chaque MSE sur $x$ vaut la MSE sur $n$ divisée par $\operatorname{SNR}_k$ (§3).

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB5.15 — Expliquer avec le jeu du téléphone pourquoi, après assez de relais qui atténuent et bruitent, le message reçu ne dit plus rien du message émis

**Réponse modèle (5 à 8 phrases).** Chaque joueur fait deux choses : il répète le message un peu plus faiblement, et il y glisse une petite erreur à lui, qui ne dépend pas de ce qu'il a entendu. Ce qui reste du message de départ est donc affaibli à chaque relais, et affaibli encore au relais suivant : au bout de vingt ou trente joueurs, il n'en reste presque rien. Les erreurs, elles, s'ajoutent, mais chacune est affaiblie à son tour par les joueurs qui suivent : les vieilles erreurs s'effacent comme le message, et les récentes pèsent le plus. Il s'installe un équilibre, où l'erreur ajoutée à chaque relais compense ce que l'affaiblissement retire : le message reçu a toujours à peu près la même dispersion, quel qu'ait été le message de départ. Au bout de la file, le message reçu ressemble donc à un tirage au hasard dans cette dispersion habituelle, et il ne dit plus rien de ce qu'a dit le premier joueur. Plus chaque joueur affaiblit le message, plus vite cet oubli arrive ; si personne ne l'affaiblissait, les erreurs s'accumuleraient sans fin, sans jamais se stabiliser.

**Grille.** Les deux effets d'un relais (affaiblir, ajouter une erreur nouvelle) ; le message de départ qui s'efface par affaiblissements répétés ; les erreurs anciennes affaiblies aussi ; l'équilibre (une dispersion qui ne change plus) ; le message reçu comme un tirage dans cette dispersion ; la vitesse de l'oubli liée à l'affaiblissement ; aucune formule. En plus, non exigé : le cas sans affaiblissement, où les erreurs s'accumulent sans équilibre.

<a id="entretien"></a>

## 💼 Entretien

### MB5.E1 — « Un modèle de régression entraîné à la MSE prédit-il le prix le plus probable ? Que prédit-il quand les prix d'un même profil se partagent en deux groupes, et quelle loss prendre pour une médiane ? »

**Réponse modèle (60 secondes).** « Non. Entraîné à la MSE, un modèle assez souple et nourri d'assez de données approche l'espérance conditionnelle, le prix moyen sachant le profil : la MSE de toute prédiction se décompose en la variance que le profil n'explique pas, plus l'écart quadratique entre la prédiction et cette moyenne, et seul ce second terme dépend du modèle. La moyenne n'est pas la valeur la plus probable : pour une loi asymétrique, comme des prix avec quelques biens très chers, elle est tirée vers la queue. Si les prix d'un même profil se partagent en deux groupes, par exemple avec ou sans vue sur la mer, le modèle prédit un prix entre les deux, que presque aucun bien n'a : c'est la bonne réponse à la question qu'on lui a posée, mais peut-être pas à celle qu'on se pose. Pour une médiane, on prend la MAE, l'erreur absolue moyenne, qui apprend la médiane conditionnelle : elle est moins sensible aux prix extrêmes. Pour en savoir plus, on peut apprendre plusieurs quantiles avec une pinball loss, ou modéliser la loi entière, par exemple un mélange, et alors repérer les deux groupes ; ou ajouter la variable cachée, la vue, si on peut la mesurer. »

**Grille.** Ce que la MSE apprend et l'argument de la décomposition ; la moyenne contre la valeur la plus probable ; la prédiction entre deux groupes ; la MAE et la médiane conditionnelle, et sa robustesse ; des quantiles, la loi entière ou la variable manquante pour aller plus loin.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **MB5.16 🔨** `linear_gaussian_recursion` : les contrôles, puis deux listes qui démarrent à `mean0` et `var0`, et à chaque pas `m = a_t * m` et `v = a_t ** 2 * v + b_t ** 2`. a) $(1{,}703680 ;\ 0{,}290827)$, comme MB5.1 b). b) $(0{,}200712 ;\ 0{,}682062)$. c) $(-0{,}336149 ;\ 2{,}240571 ;\ 2{,}250744)$, après sept pas. Ce qu'il faut observer : avec $a = -0{,}68$, chaque pas multiplie la moyenne par $-0{,}68$ : son signe alterne ($5 ; -3{,}4 ; 2{,}312 ; \ldots$), si bien qu'après un nombre impair de pas elle est négative, et sa valeur absolue est multipliée par $0{,}68$ à chaque pas ; la variance part de 0 et approche $v_\infty \approx 2{,}25$ par en dessous, sans la dépasser.
- **MB5.17 🔨** `posterior_mean_mixture` : les contrôles, puis, pour chaque composante, `spread = a**2 * s2 + b**2`, les logarithmes $\ln\pi_k - \frac12\ln(2\pi\thinspace\text{spread}) - \frac{(y - a\mu_k)^2}{2\thinspace\text{spread}}$, une softmax par mesure (retirer le maximum), et la moyenne des $\mu_k + \frac{av_k}{\text{spread}}(y - a\mu_k)$ ($v_k$ est la variance `s2` de la composante, $s_k^2$ dans la docstring) ; pour $a = 0$, la moyenne du mélange. a) $2{,}28$. b) $\approx 1{,}600998$. c) $(-1{,}359572 ;\ 0{,}975972 ;\ 2{,}363601)$ ; la formule de Tweedie, avec le score $s_Y(0{,}3) \approx 1{,}532722$ calculé par différences, redonne $\frac{0{,}3 + 0{,}25 \times 1{,}532722}{0{,}7} \approx 0{,}975972$. Ce qu'il faut observer : en $y = -0{,}9$, la première composante l'emporte (sa moyenne $a\mu_1 = -0{,}98$ est tout près, malgré son poids de $0{,}25$), et $\mathbb{E}[x \mid y]$ est presque sa moyenne a posteriori, ramenée de $\frac ya \approx -1{,}29$ vers $-1{,}4$ ; le débruiteur ne divise pas par $a$, il combine ce que dit la mesure et ce que l'on savait du signal. Pour $a = 0$, il rend la moyenne du mélange, $1{,}375$, quel que soit $y$.
- **MB5.18 🔨** `euler_ode` et `midpoint_ode` : $h = \frac{t_N - t_0}{N}$ (`t1` est l'instant final $t_N$), puis `x = x + h * f(t, x)` (Euler) ou `x = x + h * f(t + h/2, x + h/2 * f(t, x))` (point milieu), avec `t = t0 + k * h` recalculé à chaque pas. a) $(51{,}85 ;\ 56{,}076625)$, comme MB5.8. b) $\approx 56{,}2857$ en dix pas, contre $56{,}4462$ exactement et $55{,}1$ en un pas (MB5.8 e) : l'erreur passe de $1{,}35$ à $0{,}16$, environ 8 fois moins pour 10 fois plus de pas. c) $(5{,}25 ;\ 7{,}875)$, contre 8 : Euler est la somme de Riemann à gauche de $3t^2$, le point milieu la règle du point milieu de M02a, exacte seulement pour une fonction affine ($3t^2$ ne l'est pas). d) $(0{,}102486 ;\ 0{,}029453)$, autour de la valeur exacte $2{,}149361$ (Euler en dessous, le point milieu au-dessus).
- **MB5.19 📦** a) $P(8) \approx 39{,}247917$ (l'écart à la solution exacte est de l'ordre de $10^{-9}$). b) Euler : $0{,}477$ ; $0{,}156$ ; $0{,}0655$ ; $0{,}0302$ ; $0{,}0145$ ; $0{,}00710$ ; point milieu : $0{,}430$ ; $0{,}0843$ ; $0{,}0194$ ; $0{,}00470$ ; $0{,}00116$ ; $0{,}000289$. c) $(-1{,}1 ;\ -2{,}0)$ ($-1{,}067$ et $-2{,}022$) ; lues dans b), à 64 évaluations du champ, les erreurs sont $0{,}0302$ (Euler, 64 pas) et $0{,}0194$ (point milieu, 32 pas). Ce qu'il faut observer : aux petits $N$, les erreurs ne suivent pas encore leur droite (avec 8 pas, les deux méthodes se trompent autant) ; l'ordre est une propriété des petits pas. À 64 évaluations, le point milieu (32 pas) se trompe 1,6 fois moins qu'Euler (64 pas), et l'écart grandit avec le budget.
- **MB5.20 🔮** Prédictions attendues : a) (B) ; b) (A) ; c) (C). Mesures : d) $(2{,}43201 ;\ 1{,}95272 ;\ 2{,}00735 ;\ 1{,}90001 ;\ 1{,}9)$ ; e) $(2{,}67385 ;\ 2{,}93404 ;\ 2{,}95 ;\ 2{,}95 ;\ 2{,}95)$ ; f) $\approx 2{,}59993$, presque la moyenne $2{,}6$ des relevés. Ce qu'il faut observer (après l'expérience) : dès $b = 0{,}03$, le débruiteur rend un relevé à $10^{-5}$ près, le plus proche de $\frac ya$ ; il ne rend jamais 2 : quand le bruit est faible, il « sait » que $x$ est l'un des cinq relevés, et choisit le plus vraisemblable ; à égale distance de deux relevés, il hésite pour toujours et rend leur moyenne, $2{,}95$, une valeur qui n'est pas un relevé, mais aussi la seule chose nouvelle qu'il fabrique ; quand le bruit est énorme, la mesure ne dit rien, et il rend la moyenne des relevés. Un débruiteur optimal d'un nuage de points le recopie.
- **MB5.21 🔬** `field_21(s, x)` $= -4 + \frac{s - 0{,}25(1 - s)}{0{,}25(1 - s)^2 + s^2}\big(x - 4(1 - s)\big)$. a) Euler : $(0 ;\ 0{,}200173 ;\ 0{,}340834 ;\ 0{,}415142 ;\ 0{,}456076 ;\ 0{,}477775)$ ; point milieu : $(0{,}400345 ;\ 0{,}494813 ;\ 0{,}498721 ;\ 0{,}500208 ;\ 0{,}500403 ;\ 0{,}500428)$. b) $0{,}500431$. Ce qu'il faut observer : le transport est affine en $z$, et la moyenne de la loi obtenue est le point atteint depuis $z = 0$ ; la trajectoire partie de $z = 0$ est la droite $x(s) = 4(1 - s)$ : Euler et le point milieu la suivent exactement, et la moyenne est juste dès un pas (4, à l'erreur d'échantillonnage de `Z_21` près) ; les autres trajectoires sont courbes, et l'écart-type obtenu en dépend. L'écart à l'écart-type exact est divisé par environ 2 quand $N$ double pour Euler (ordre 1 : 0,30 ; 0,16 ; 0,085 ; 0,044 ; 0,023), et par environ 8 pour le point milieu (de $1{,}7 \times 10^{-3}$ à $3{,}6 \times 10^{-6}$ de 4 à 32 pas) : mieux que l'ordre 2 de la fiche, qui est une garantie pour tout champ régulier ; sur ce champ particulier, le terme en $h^2$ de l'erreur s'annule.
- **MB5.22 🎨** `guided_22(xs, w, general, cls)` (par défaut, les deux lois de l'énoncé ; `pc` et `pu` sont leurs densités sur `xs`) : `lg = (1 + w) * np.log(pc) - w * np.log(pu)`, `d = np.exp(lg - lg.max())`, `d / np.trapezoid(d, xs)`. Pour $w = 0{,}25$, $1{,}75$ et $3{,}5$ : a) moyennes $(1{,}617613 ;\ 1{,}657115 ;\ 1{,}676298)$ ; b) écarts-types $(0{,}818055 ;\ 0{,}782353 ;\ 0{,}767596)$ ; c) pour $w = 3{,}5$, par `np.trapezoid(np.where(xs < 0, d, 0), xs)`, une masse sur $x < 0$ de $0{,}0027$, contre $0{,}0279$ pour $p_c$ (et $0{,}0207$ puis $0{,}0068$ pour $w = 0{,}25$ et $1{,}75$). Ce qu'il faut observer : la loi guidée vaut $p_c\big(\frac{p_c}{p_u}\big)^w$, et $\frac{p_c}{p_u}$ est petit du côté de l'autre bosse, où $p_u$ est grande : la masse quitte ce côté, la moyenne s'écarte de $1{,}6$ vers la droite, loin de $-1{,}8$, et la loi se resserre ; elle existe pour tout $w \ge 0$, car la composante la plus large de $p_u$ a la variance de $p_c$ ($0{,}7$), si bien que les queues restent celles de $p_c$.
- **MB5.23 🐛** (1) Le poids $\frac{V_s}{V_T}$ va avec $x_T$ : `mean = x0 + Vs / VT * (xT - x0)`. a) $(7{,}235294 ;\ 4{,}764706)$. Au milieu d'une marche de pas égaux, $\frac{V_s}{V_T} = \frac12$ : les deux poids sont égaux, et l'erreur ne se voit pas. (2) Les responsabilités demandent la loi de $y$ sachant la composante, de variance `a**2 * s2 + b**2`. b) $(0{,}086508 ;\ 1{,}608911 ;\ -0{,}127978 ;\ 1{,}811618)$. Avec une seule composante, la responsabilité vaut 1 quelle que soit la variance : l'erreur ne se voit pas. (3) Le temps du champ avance : `f(t0 + k * h, x)`. c) $(1{,}175583 ;\ 0{,}087791)$, pour $x(0) = 1$ sur $[0, 2]$ en six pas. Pour $x' = -\frac x3$, le champ ne dépend pas du temps : lire $t_0$ au lieu de $t_k$ ne change rien.
- **MB5.24 🛠️** Une correction possible : `constant_is_exact_24` essaie trois vitesses (dont une négative) et $N = 1$, 3 et 7, avec $t_0 < t_N$, et compare chaque point à `x0 + c * (t_k - t0)`, à $10^{-9}$ près en valeur absolue (pas `np.allclose` par défaut, trop large) ; `affine_is_exact_24` compare chaque point à `x0 + k0 * (t_k - t0) + k1 * (t_k**2 - t0**2) / 2` ; `error_halves_24` prend $x' = t - x$, $x(0) = 2$, sur $[0, 3]$, avec $N = 64$ et 128, et teste que le rapport des erreurs est entre $1{,}8$ et $2{,}2$. a) Euler : `[True, False, True]` ; point milieu : `[True, True, False]`. Ce qu'il faut observer : Euler n'est pas exact pour une vitesse affine (il fait la somme de Riemann à gauche), et l'erreur du point milieu est divisée par environ 4, pas 2 : chaque test vise une seule propriété. Tester chaque point rendu, et pas seulement le dernier, attrape une méthode dont les points intermédiaires sont faux (un pas mal compté, des instants décalés).
- **MB5.25 🏆** `field_25` : `(x - posterior_mean_mixture(x, 1 - s, s, weights, means, variances)) / s`. `transport_25` : la méthode du point milieu avec quatre pas égaux de $s = 1$ à $s = 0$ (huit appels) : `h = -0.25` ; à chaque pas, `x = x + h * field(x + h / 2 * field(x, s), s + h / 2)`. b) Un pas d'Euler : $W_1 \approx 1{,}744$ (tous les points tombent sur la moyenne du mélange, $0{,}694$) ; huit pas d'Euler : $\approx 0{,}173$ ($0{,}093$ fois l'écart-type $1{,}86$ du mélange, au-dessus du seuil $0{,}07$) ; le point milieu : $\approx 0{,}032$ ($0{,}017$ fois l'écart-type). c) 8. Le piège : huit pas d'Euler semblent le meilleur usage du budget, mais l'erreur d'Euler n'est que d'ordre 1 ; quatre pas du point milieu, d'ordre 2, font bien mieux pour le même nombre d'évaluations (la fiche §8). La vérification tire trois séries de cinq lois cachées et compare la moyenne des quinze rapports au seuil. Sur 220 exécutions, le point milieu à quatre pas égaux réussit toujours (moyenne de $0{,}014$ à $0{,}021$ fois l'écart-type ; au pire $0{,}049$ sur une seule loi), comme toute méthode d'ordre 2 qui emploie ses huit appels (pas resserrés près de $s = 0$ ou de $s = 1$, Heun, RK4 à deux pas) ; échouent toujours : un pas d'Euler (au moins $0{,}86$), aucun pas (au moins $0{,}50$), huit pas d'Euler égaux (au moins $0{,}093$), resserrés ou suivis d'un pas du point milieu (au moins $0{,}087$), deux pas du point milieu, qui n'emploient que quatre appels (au moins $0{,}074$), et les quantiles du mélange du notebook appliqués aux points (une méthode figée, qui réussit le notebook seul). Une idée qui réussit aussi, en un seul appel : demander le champ sur une grille fine en un petit $s$ (0,01), en déduire par la formule de Tweedie le score, donc la densité de $x_s$, presque celle des données, puis envoyer chaque $z$ sur le quantile de même rang ; c'est un transport rangé, comme celui du champ (M27 §8). Exécuter le code du module caché, ou le recopier, n'est pas une méthode : la vérification le refuse.
