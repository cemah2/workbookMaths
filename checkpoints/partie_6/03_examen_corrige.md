# CP6 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Le barème.** Chaque question vaut autant de points que de minutes prévues par le sujet, 111 points en tout, et ses points sont partagés également entre ses sous-questions. **Ta note sur 20 est ton total multiplié par $\frac{20}{111}$, c'est-à-dire divisé par 5,55** : chaque question pèse dans la note exactement en proportion de sa durée.
- **Le poids de chaque sous-question.**
  - 1 point par affirmation du quiz (0,4 pour le verdict, 0,6 pour la justification).
  - $\frac{10}{6} \approx 1{,}67$ point par sous-question de CP6.1 (6 sous-questions).
  - 1,5 point par sous-question de CP6.2 et CP6.5 (6 sous-questions chacune), et 1,8 point par sous-question de CP6.7 (5 sous-questions).
  - 2,5 points par sous-question de CP6.3, et 2,25 par sous-question de CP6.4 (4 sous-questions chacune).
  - 2 points par sous-question de CP6.6 (4 sous-questions).
  - $\frac{16}{7} \approx 2{,}29$ points par sous-question de CP6.10 (7 sous-questions).
  - 3 points par étape de CP6.8.
  - 4,5 points pour chacune des deux parties de CP6.9 (0,9 par lettre en a, 0,9 par ligne corrigée en b).
- **Sur ta copie.** Une justification demandée « sur ta copie » compte dans la sous-question à laquelle elle se rattache.
- **Crédit partiel** sur une sous-question de calcul : 40 % de ses points ($\frac23 \approx 0{,}67$ sur $\frac{10}{6}$ ; 0,6 sur 1,5 ; 0,72 sur 1,8 ; 0,8 sur 2 ; 0,9 sur 2,25 ; $\frac{32}{35} \approx 0{,}91$ sur $\frac{16}{7}$ ; 1 sur 2,5) pour une réponse juste sans la démarche demandée, ou pour une méthode juste avec une erreur de calcul.
- **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois (par exemple des responsabilités fausses en CP6.3 a, réutilisées en b), c) et d), une loi $\boldsymbol{\mu}_2$ fausse en CP6.4 a, réutilisée en b) et d), ou une matrice $\mathbf{P}'$ fausse en CP6.10 f, réutilisée en g)).
- **Arrondis** : une valeur arrondie là où l'énoncé demande la valeur exacte, ou une décimale de moins que le nombre demandé, coûte au plus 0,25 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi. Des décimales en plus ne coûtent rien (le notebook les accepte).
- **Questions rédigées** (CP6.Q1, CP6.8, CP6.9 b, les phrases demandées « sur ta copie ») : les critères sont listés ; une idée juste formulée autrement compte autant.
- **Conventions** : celles du sujet.
  - $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ a pour second paramètre une covariance ; $\mathbf{L}$ est triangulaire inférieur ; les KL sont en nats, l'espérance sous la première loi.
  - Les chaînes sont en convention ligne, $\boldsymbol{\mu}_{t+1} = \boldsymbol{\mu}_t\mathbf{P}$, et $\mathbf{V} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$ ; la masse qui manque à une ligne est la probabilité de finir.
  - Le joueur des lignes de $\mathbf{G}$ maximise ; les points sont les lignes de $\mathbf{X}$ ; le top-p prend les issues par probabilité décroissante, la plus petite d'abord en cas d'égalité.

---

## CP6.Q1 — Dix affirmations sur la partie VI, deux par chapitre 🧠 · 10 points

1 point par affirmation : 0,4 pour le verdict, 0,6 pour la justification. Une règle juste suffit pour la justification (en h, les supports emboîtés ; en j, la décomposition $I(X ; Z) + \mathrm{KL}$), sans le calcul.

**a) Faux** (M26 §1 et §2). $P(S_0 = i, S_1 = j) = \pi_i\,p_{ij}$, et $P(S_1 = j) = \pi_j$ puisque $\boldsymbol{\pi}$ est stationnaire. L'indépendance demande $p_{ij} = \pi_j$ pour tous $i$ et $j$ : toutes les lignes de $\mathbf{P}$ égales à $\boldsymbol{\pi}$. Contre-exemple : $\mathbf{P} = \begin{pmatrix} 0{,}7 & 0{,}3 \\ 0{,}3 & 0{,}7 \end{pmatrix}$, de loi stationnaire $(\frac12, \frac12)$ : $P(S_1 = 0 \mid S_0 = 0) = 0{,}7 \ne \frac12 = P(S_1 = 0)$. La stationnarité dit que $S_1$ a la **même loi** que $S_0$, pas qu'il en est indépendant.

**b) Faux** (M25a §7). À moyennes égales, $\mathrm{KL} = \frac12\big(\operatorname{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0) - d + \ln\frac{\det\boldsymbol{\Sigma}_1}{\det\boldsymbol{\Sigma}_0}\big)$ : le logarithme s'annule, pas le terme de la trace. Ici $\boldsymbol{\Sigma}_0 = \operatorname{diag}(6, 1)$ et $\boldsymbol{\Sigma}_1 = \operatorname{diag}(1, 6)$, de même déterminant 6 : $\mathrm{KL} = \frac12\big(6 + \frac16 - 2\big) = \frac{25}{12} \approx 2{,}083$ (la même dans l'autre sens). La KL n'est nulle que pour deux lois égales ; deux ellipses de même aire mais d'orientations différentes ne le sont pas.

**c) Vrai** (M28 §5). $\big(p_i^{1/3}/Z_3\big)^{1/4} = p_i^{1/12}/Z_3^{1/4}$, et la constante $Z_3^{1/4}$, la même pour toutes les issues, disparaît quand on renormalise : on obtient $\mathbf{p}^{(12)}$. Les températures successives se multiplient, $T\,T' = 12$.

**d) Faux** (M27 §4). Un pas simultané fait $x \leftarrow x - 0{,}4\,y$ et $y \leftarrow y + 0{,}4\,x$ (le gradient de $10xy$ en $x$ est $10y$, et $0{,}04 \times 10 = 0{,}4$), de matrice $\begin{pmatrix} 1 & -0{,}4 \\ 0{,}4 & 1 \end{pmatrix}$, de valeurs propres $1 \pm 0{,}4\,i$, de module $\sqrt{1{,}16} \approx 1{,}077 > 1$. En fait $(x - 0{,}4y)^2 + (y + 0{,}4x)^2 = 1{,}16\,(x^2 + y^2)$ : c'est le **carré** de la distance à l'équilibre qui est multiplié par 1,16 ; la distance, elle, est multipliée par $\sqrt{1{,}16} \approx 1{,}077$ à chaque pas, depuis tout point autre que $(0, 0)$. (La descente-montée simultanée s'éloigne pour tout pas $\eta > 0$.)

**e) Vrai** (M25b §7, M25a §7). $\mathrm{KL}(q \,\|\, p) = 2 \times \frac12\ln\frac{1/2}{1/6} = \ln 3$, finie parce que le support de $q$ est dans celui de $p$. $\mathrm{KL}(p \,\|\, q) = +\infty$ : $p$ met la masse $\frac46$ sur $\{3, 4, 5, 6\}$, où $q$ est nulle. Minimiser $\mathrm{KL}(q \,\|\, p)$ ne pénalise $q$ que là où $q > 0$ : $q$ peut se concentrer sur une partie de $p$ (sur un mode), alors que $\mathrm{KL}(p \,\|\, q)$ l'oblige à couvrir tout le support de $p$.

**f) Vrai** (M26 §5, ∂ M26.11). $\mathbf{V} = \sum_{t \ge 0}\gamma^t\mathbf{P}^t\mathbf{r}$ ; si $\mathbf{r}$ augmente de $\delta \ge 0$ en $s_0$ seulement, $\mathbf{V}$ augmente de $\sum_t\gamma^t\mathbf{P}^t\delta\,\mathbf{e}_{s_0}$, dont toutes les coordonnées sont positives ou nulles (les $\mathbf{P}^t$ ont des coefficients positifs ou nuls), et dont la coordonnée $s_0$ vaut au moins $\delta$ (le terme $t = 0$).

**g) Vrai** (M25a §4). La covariance de $x_1$ sachant $(x_2, x_3)$ est le complément de Schur $\Sigma_{11} - \boldsymbol{\Sigma}_{1b}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{b1}$, et la formule de l'inverse par blocs dit que c'est l'inverse du bloc correspondant de $\boldsymbol{\Lambda}$ : $\frac{1}{\Lambda_{11}}$. Un coefficient de la précision lit une variance **conditionnelle**, un coefficient de la covariance une variance **marginale**.

**h) Faux** (M27 §6). $\mathrm{JS} = \ln 2$ seulement pour deux lois de supports disjoints, et le support de $p$ est dans celui de $m$. Le calcul : le mélange de $p$ et $m$ est $\frac34p + \frac14q$ ; $\mathrm{KL}\big(p \,\|\, \frac34p + \frac14q\big) = \ln\frac43$ et $\mathrm{KL}\big(m \,\|\, \frac34p + \frac14q\big) = \frac12\ln\frac{1/2}{3/4} + \frac12\ln\frac{1/2}{1/4} = \frac12\ln\frac43$, donc $\mathrm{JS}(p, m) = \frac12\ln\frac43 + \frac14\ln\frac43 = \frac34\ln\frac43 \approx 0{,}216 < \ln 2$.

**i) Vrai** (M28 §4). La moyenne mobile de trois cases multiplie un cosinus de pulsation $\omega$ par $\frac{1 + 2\cos\omega}{3}$. Ce gain est nul si et seulement si $\cos\omega = -\frac12$, soit $\omega = \frac{2\pi}{3}$ sur $[0, \pi]$ : trois valeurs consécutives d'un cosinus de période 3 ont une somme nulle, quelle que soit la phase. Une période plus longue a $\omega < \frac{2\pi}{3}$, donc $\cos\omega > -\frac12$ et un gain positif.

**j) Faux** (M25b §8). Le posterior agrégé vaut bien $\frac12(0{,}84 + 0{,}34 ;\ 0{,}16 + 0{,}66) = (0{,}59 ;\ 0{,}41)$, le prior. Mais $\mathbb{E}_x\,\mathrm{KL}\big(q(z \mid x) \,\|\, p(z)\big) = I(X ; Z) + \mathrm{KL}\big(q(z) \,\|\, p(z)\big)$ : le second terme est nul, pas le premier. $\mathrm{KL}\big((0{,}84 ;\ 0{,}16) \,\|\, (0{,}59 ;\ 0{,}41)\big) \approx 0{,}1462$ et $\mathrm{KL}\big((0{,}34 ;\ 0{,}66) \,\|\, (0{,}59 ;\ 0{,}41)\big) \approx 0{,}1268$ : la KL moyenne vaut environ 0,1365 nat, l'information que le code garde sur $x$. Elle ne serait nulle que si $q(z \mid x) = p(z)$ pour chaque $x$ : un code effondré, qui ignore la donnée.

**Erreurs fréquentes** :
- en a), confondre « même loi » et « indépendants » ;
- en b), oublier le terme de la trace ;
- en c), additionner les températures ($3 + 4 = 7$) ;
- en d), confondre la distance et son carré : 1,16 multiplie le carré de la distance ;
- en e), croire qu'une KL finie dans un sens l'est dans l'autre ;
- en f), croire qu'un état peut perdre de la valeur quand un autre en gagne ;
- en g), lire la variance conditionnelle sur $\boldsymbol{\Sigma}$, ou prendre $\frac{1}{\Sigma_{11}}$ ;
- en h), appliquer la règle des supports disjoints à des supports emboîtés ;
- en i), croire qu'une moyenne mobile ne fait qu'atténuer, sans jamais effacer ;
- en j), croire que le posterior agrégé égal au prior annule chaque KL.

**Remédiation** :
- a) M26.Q1, M26.Q2, M26.2 ;
- b) M25a.8, M25a.14, M25a.Q7 ;
- c) M28.11, M28.Q4, M28.R3, M28.6 ;
- d) M27.4, M27.24, M27.Q3, M27.21 ;
- e) M25b.13, M25b.27, M25b.Q7, M25a.Q7 ;
- f) M26.11, M26.Q5, M26.R2 ;
- g) M25a.4, M25a.Q4, M25a.22 ;
- h) M27.13, M27.6, M27.Q4 ;
- i) M28.5, M28.Q3, M28.R2 ;
- j) M25b.14, M25b.Q8.

## CP6.1 — Un vecteur gaussien de dimension 2 : loi marginale, loi conditionnelle, et la loi de μ + Lε ✏️ · 10 points ($\frac{10}{6} \approx 1{,}67$ par sous-question)

**Réponses** : a) `[[4, 0], [3, 2]]` · b) `[55, 13]` · c) `[61, 4]` · d) `[34, 4.9231]` · e) `[44, 53]` · f) `[[16, 12], [12, 13]]`.

a) $l_{11} = \sqrt{16} = 4$, $l_{21} = \frac{12}{4} = 3$, $l_{22} = \sqrt{13 - 3^2} = 2$.
b) La loi marginale d'une coordonnée garde sa moyenne et son coefficient diagonal : $x_2 \sim \mathcal{N}(55, 13)$.
c) Moyenne $55 + \frac{12}{16}(48 - 40) = 61$ ; variance, le complément de Schur, $13 - \frac{12^2}{16} = 4$.
d) Moyenne $40 + \frac{12}{13}(48{,}5 - 55) = 40 - 6 = 34$ ; variance $16 - \frac{144}{13} = \frac{64}{13} \approx 4{,}9231$.
e) $\mathbf{L}\boldsymbol{\varepsilon} = (4 \times 1 ;\ 3 \times 1 + 2 \times (-2{,}5)) = (4 ;\ -2)$, et le tirage vaut $(44 ;\ 53)$.
f) La covariance de $\boldsymbol{\mu} + \mathbf{M}\boldsymbol{\varepsilon}$ est $\mathbf{M}\mathbf{M}^\top = \begin{pmatrix} 0 + 16 & 0 + 12 \\ 0 + 12 & 4 + 9 \end{pmatrix} = \boldsymbol{\Sigma}$.

Sur ta copie :
- $\mathbf{L}\mathbf{L}^\top = \begin{pmatrix} 16 & 12 \\ 12 & 9 + 4 \end{pmatrix} = \boldsymbol{\Sigma}$.
- $x_1 = 40 + 4\varepsilon_1$ et $x_2 = 55 + 3\varepsilon_1 + 2\varepsilon_2$. Lire $x_1 = 48$ fixe $\varepsilon_1 = 2$, et il reste $x_2 = 61 + 2\varepsilon_2$, où $\varepsilon_2 \sim \mathcal{N}(0, 1)$ est indépendant de $\varepsilon_1$ : la variance vaut $l_{22}^2 = 4$ quelle que soit la valeur lue, qui ne fait que déplacer la moyenne.
- $\mathbf{M} = \mathbf{L}\mathbf{R}$ avec $\mathbf{R} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, orthogonale : $\mathbf{R}\boldsymbol{\varepsilon}$ suit encore $\mathcal{N}(\mathbf{0}, \mathbf{I})$, et les tirages $\boldsymbol{\mu} + \mathbf{M}\boldsymbol{\varepsilon}$ ont bien la loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. Mais, pour $\boldsymbol{\varepsilon} = (1 ;\ -2{,}5)$, on obtient $(40 + 4 \times (-2{,}5) ;\ 55 + 2 \times 1 + 3 \times (-2{,}5)) = (30 ;\ 49{,}5)$, pas le point de e) : même loi, pas les mêmes tirages. Deux tireurs se comparent par leurs lois (moyenne et covariance), jamais tirage par tirage.

**Erreurs fréquentes** :
- en a), donner $\mathbf{L}^\top$, triangulaire supérieure, ou prendre $l_{22} = \sqrt{13}$ ;
- en b), donner la variance conditionnelle (4), ou un écart-type ($\sqrt{13}$) ;
- en c), garder la variance 13, ou diviser par $\Sigma_{22}$ au lieu de $\Sigma_{11}$ ;
- en d), garder la variance 16, diviser par $\Sigma_{11}$ ($35{,}125$ et $7$, ou seulement dans la variance : $[34, 7]$), ou se tromper de signe sur $x_2 - \mu_2$ (46) ;
- en e), multiplier par $\mathbf{L}^\top$ ($(36{,}5 ;\ 50)$), par $\boldsymbol{\Sigma}$ ($(26 ;\ 34{,}5)$), ou oublier $\boldsymbol{\mu}$ ;
- en f), calculer $\mathbf{M}^\top\mathbf{M} = \begin{pmatrix} 4 & 6 \\ 6 & 25 \end{pmatrix}$, ou conclure de « $\mathbf{M}$ n'est pas triangulaire » que la loi est fausse.

**Remédiation** : M25a.2, M25a.4, M25a.10, M25a.21, M25a.22, M25a.Q2, M25a.Q4, M25a.R2.

## CP6.2 — La divergence KL entre deux gaussiennes de dimension 2, et une interpolation sphérique ✏️ · 9 points (1,5 par sous-question)

**Réponses** : a) `3.5` · b) `1` · c) `0.7442` · d) `48.19` · e) `[1.5826, 2.4227, 0.7913]` · f) `2.806`.

a) $\det\boldsymbol{\Sigma}_1 = 8 - 4 = 4$ et $\boldsymbol{\Sigma}_1^{-1} = \frac14\begin{pmatrix} 2 & -2 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} 0{,}5 & -0{,}5 \\ -0{,}5 & 1 \end{pmatrix}$ ; $\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0 = \begin{pmatrix} 1 & -0{,}5 \\ 0{,}5 & 2{,}5 \end{pmatrix}$, de trace 3,5.
b) $\boldsymbol{\delta} = (2, 1)$, $\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta} = (0{,}5 ;\ 0)$, et $\boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta} = 1$.
c) $\det\boldsymbol{\Sigma}_0 = 20 - 9 = 11$ : $\mathrm{KL} = \frac12\big(3{,}5 + 1 - 2 + \ln\frac{4}{11}\big) = \frac12(2{,}5 - 1{,}011601) \approx 0{,}7442$.
d) $\lVert\mathbf{u}\rVert = \lVert\mathbf{v}\rVert = 3$ et $\mathbf{u} \cdot \mathbf{v} = 6$ : $\cos\Omega = \frac23$, $\Omega \approx 48{,}19°$ (0,8411 rad).
e) $\sin\Omega = \frac{\sqrt5}{3} \approx 0{,}745356$. Les coefficients valent $\frac{\sin(\frac34\Omega)}{\sin\Omega} = \frac{\sin 36{,}142°}{\sin\Omega} \approx 0{,}791289$ pour $\mathbf{u}$ et $\frac{\sin(\frac14\Omega)}{\sin\Omega} = \frac{\sin 12{,}047°}{\sin\Omega} \approx 0{,}280029$ pour $\mathbf{v}$ : $0{,}791289\,(2, 2, 1) + 0{,}280029\,(0, 3, 0) \approx (1{,}5826 ;\ 2{,}4227 ;\ 0{,}7913)$.
f) $\frac34\mathbf{u} + \frac14\mathbf{v} = (1{,}5 ;\ 2{,}25 ;\ 0{,}75)$, de norme $\sqrt{7{,}875} \approx 2{,}806$.

Sur ta copie :
- Les trois termes : $\operatorname{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0)$ compare la forme et l'étalement de $p_0$ à ceux de $p_1$ ; $\boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta}$ mesure l'écart des moyennes à l'échelle de $p_1$ (une distance de Mahalanobis au carré) ; $\ln\frac{\det\boldsymbol{\Sigma}_1}{\det\boldsymbol{\Sigma}_0}$ compare les volumes. Ici il est négatif ($p_1$ est plus concentrée), mais la somme reste positive.
- L'angle de $\mathbf{u}$ avec le point de e) : $\frac\Omega4 \approx 12{,}05°$, sans calcul, parce que le slerp tourne de $t\Omega$ ; sa norme est 3, celle de $\mathbf{u}$ et de $\mathbf{v}$ (contre 2,806 pour le point de f). Un calcul de contrôle ($\cos = \frac{8{,}8018}{9} \approx 0{,}97798$) est accepté, mais pas demandé.
- Pour aller plus loin (non noté) : $1{,}5826^2 + 2{,}4227^2 + 0{,}7913^2 \approx 2{,}5046 + 5{,}8695 + 0{,}6262 = 9{,}0003$, soit 9 aux arrondis près (avec les coordonnées non arrondies, la somme vaut 9) : la norme est 3. Le point de f), lui, fait avec $\mathbf{u}$ l'angle $11{,}49°$ ($\cos = \frac{8{,}25}{3 \times 2{,}806243} \approx 0{,}97996$), pas $\frac\Omega4$ : la ligne droite passe à l'intérieur de la sphère et n'avance pas régulièrement en angle.

**Erreurs fréquentes** :
- en a), calculer $\operatorname{tr}(\boldsymbol{\Sigma}_0^{-1}\boldsymbol{\Sigma}_1) = \frac{14}{11}$, oublier de diviser par $\det\boldsymbol{\Sigma}_1$ (14), ou multiplier les traces ;
- en b), utiliser $\boldsymbol{\Sigma}_1$ au lieu de son inverse (26), $\boldsymbol{\Sigma}_0^{-1}$ ($\frac{9}{11}$), oublier la matrice ($\boldsymbol{\delta}^\top\boldsymbol{\delta} = 5$), ou ses termes hors diagonale (1,5) ;
- en c), écrire $\ln\frac{11}{4}$ (1,7558), oublier $-d$ (1,7442) ou le facteur $\frac12$ (1,4884), ou calculer $\mathrm{KL}(p_1 \,\|\, p_0) \approx 0{,}5513$ ;
- en d), répondre en radians, ou prendre l'arc sinus ($41{,}81°$) ;
- en e), échanger les deux coefficients, prendre le point de la ligne droite, ou le ramener sur la sphère ($(1{,}6036 ;\ 2{,}4054 ;\ 0{,}8018)$, à l'angle $11{,}49°$) ;
- en f), oublier la racine (7,875), répondre 3, ou prendre le milieu ($3\cos\frac\Omega2 \approx 2{,}739$).

**Remédiation** : M25a.8, M25a.9, M25a.14, M25a.15, M25a.Q7, M25a.Q8.

## CP6.3 — Un mélange de deux gaussiennes de variances connues et trois mesures : responsabilités, un pas d'EM sur le poids et les moyennes, et l'écart à l'ELBO d'une affectation dure ✏️ · 10 points (2,5 par sous-question)

**Réponses** : a) `[0.9704, 0.7290, 0.0290]` · b) `0.5761` · c) `[24.344, 33.756]` · d) `0.3756`.

a) Les deux composantes ont la même variance : le facteur $\frac{1}{\sqrt{2\pi\sigma^2}}$ se simplifie, et
$$r_{i1} = \frac{1}{1 + e^{-z_i}}, \qquad z_i = \ln\frac{\pi_1}{\pi_2} + \frac{(x_i - \mu_2)^2 - (x_i - \mu_1)^2}{2\sigma^2}.$$
Les trois fractions valent $\frac{100 - 4}{32} = 3$, $\frac{25 - 9}{32} = 0{,}5$ et $\frac{16 - 144}{32} = -4$ ; avec $\ln\frac{0{,}62}{0{,}38} \approx 0{,}489548$ : $z = 3{,}489548$ ; $0{,}989548$ ; $-3{,}510452$, et $r_{\cdot 1} \approx 0{,}970389$ ; $0{,}728999$ ; $0{,}029016$.
b) $N_1 = \sum_i r_{i1} \approx 1{,}728404$, et $\pi_1 = \frac{N_1}{3} \approx 0{,}5761$.
c) $\sum_i r_{i1}x_i \approx 42{,}076107$, donc $\mu_1 \approx \frac{42{,}076107}{1{,}728404} \approx 24{,}344$ ; $N_2 \approx 1{,}271596$ et $\sum_i r_{i2}x_i \approx 42{,}923893$, donc $\mu_2 \approx 33{,}756$.
d) Les mesures sont indépendantes : $\ln p(x_1, x_2, x_3) - \operatorname{ELBO}(q) = \sum_i\mathrm{KL}\big(q_i \,\|\, p(z_i \mid x_i)\big)$ (M25b §5). Pour une loi $q_i$ certaine sur $k$, cette KL vaut $1 \times \ln\frac{1}{r_{ik}} = -\ln r_{ik}$. L'affectation dure met les graines 1 et 2 dans la composante 1 et la graine 3 dans la composante 2 : $-\ln 0{,}970389 - \ln 0{,}728999 - \ln 0{,}970984 \approx 0{,}030058 + 0{,}316083 + 0{,}029446 \approx 0{,}3756$.

Sur ta copie : les trois nombres 3 ; 0,5 ; −4 ; l'écart de d) est la somme des KL de $q_i$ aux posteriors ; chacune vaut $-\ln r$ parce que $q_i$ met toute sa masse sur une seule valeur ; il serait nul pour $q_i = p(z_i \mid x_i)$, la loi des responsabilités, que choisit justement le pas E. (La graine 2, dont la responsabilité 0,73 est la moins tranchée, coûte le plus.)

**Erreurs fréquentes** :
- en a), oublier les poids ($0{,}9526$ ; $0{,}6225$ ; $0{,}0180$), donner $r_{i2}$, ou diviser le carré par $\sigma^2$ au lieu de $2\sigma^2$ ;
- en b), donner $N_1$ sans diviser par 3, garder 0,62, ou prendre la part des graines affectées à la composante 1 ($\frac23$) ;
- en c), diviser par $n = 3$ au lieu de $N_k$ ($14{,}025$ et $14{,}308$), affecter chaque graine tout entière à une seule composante, ou échanger les moyennes ;
- en d), mettre les trois graines dans la composante 1 (3,886), changer le signe, ou donner l'entropie des posteriors (0,8489).

**Remédiation** : M25b.3, M25b.5, M25b.6, M25b.20, M25b.21, M25b.Q3, M25b.Q4, M25b.Q5.

## CP6.4 — Une chaîne de Markov à trois états : loi à deux pas, et la valeur d'une politique fixée par le système de Bellman, quand une ligne finit ✏️ · 9 points (2,25 par sous-question)

**Réponses** : a) `[0.36, 0.429, 0.066]` · b) `0.145` · c) `[66, 80, 10]` · d) `9.834`.

$$\mathbf{P} = \begin{pmatrix} 0{,}6 & 0{,}33 & 0 \\ 0 & 0{,}7 & 0{,}2 \\ 0 & 0 & 0{,}4 \end{pmatrix}, \qquad \text{probabilités de finir : } 0{,}07 ;\ 0{,}1 ;\ 0{,}6 \ \text{(ce qui manque à chaque ligne)}.$$

a) $\boldsymbol{\mu}_0 = (1, 0, 0)$, $\boldsymbol{\mu}_1 = (0{,}6 ;\ 0{,}33 ;\ 0)$, $\boldsymbol{\mu}_2 = \boldsymbol{\mu}_1\mathbf{P} = (0{,}36 ;\ 0{,}198 + 0{,}231 ;\ 0{,}066) = (0{,}36 ;\ 0{,}429 ;\ 0{,}066)$.
b) $1 - (0{,}36 + 0{,}429 + 0{,}066) = 0{,}145$ : $0{,}07$ la première année, puis $0{,}6 \times 0{,}07 + 0{,}33 \times 0{,}1 = 0{,}075$ la deuxième.
c) Le système $\mathbf{V} = \mathbf{r} + \mathbf{P}\mathbf{V}$, en commençant par le bas : $V(2) = 6 + 0{,}4\,V(2)$, donc $V(2) = 10$ ; $V(1) = 22 + 0{,}7\,V(1) + 0{,}2 \times 10$, donc $0{,}3\,V(1) = 24$ et $V(1) = 80$ ; $V(0) = 0 + 0{,}6\,V(0) + 0{,}33 \times 80$, donc $0{,}4\,V(0) = 26{,}4$ et $V(0) = 66$.
d) $\boldsymbol{\mu}_2\mathbf{r} = 0{,}429 \times 22 + 0{,}066 \times 6 = 9{,}438 + 0{,}396 = 9{,}834$ hl.

Sur ta copie : $\mathbf{P}$ ci-dessus, de sommes de lignes $0{,}93$, $0{,}9$ et $0{,}4$ ; $\mathbf{P}$ est triangulaire supérieure (une parcelle ne rajeunit jamais), donc la dernière équation ne fait intervenir que $V(2)$, l'avant-dernière $V(1)$ et $V(2)$, etc. $\gamma = 1$ est permis parce que la fin est sûre : chaque ligne perd de la masse, $\rho(\mathbf{P}) = 0{,}7 < 1$ (les valeurs propres d'une matrice triangulaire sont sur sa diagonale), $\mathbf{I} - \mathbf{P}$ est inversible et $\mathbf{V} = \sum_t\mathbf{P}^t\mathbf{r}$ converge.

**Erreurs fréquentes** :
- en a), multiplier dans la convention colonne ($(0{,}36 ;\ 0 ;\ 0)$), élever les coefficients au carré, ou s'arrêter à $\boldsymbol{\mu}_1$ ;
- en b), ne compter qu'une année (0,07 ou 0,075), doubler la probabilité de la première année (0,14), ou donner 0,855 ;
- en c), oublier les coefficients diagonaux ($(7{,}656 ;\ 23{,}2 ;\ 6)$), résoudre avec $\mathbf{P}^\top$, ou oublier la récolte de l'année en cours ($(66 ;\ 58 ;\ 4)$) ;
- en d), prendre $\boldsymbol{\mu}_1\mathbf{r} = 7{,}26$ ou $\boldsymbol{\mu}_3\mathbf{r} \approx 9{,}893$, ou renormaliser $\boldsymbol{\mu}_2$ (11,50).

**Remédiation** : M26.1, M26.4, M26.6, M26.11, M26.18, M26.Q1, M26.Q5.

## CP6.5 — Un jeu à somme nulle 2 × 2 en stratégies mixtes, et W₁ entre deux petits échantillons de même taille ✏️ · 9 points (1,5 par sous-question)

**Réponses** : a) `[-2, 3]` · b) `1/3` · c) `8/15` · d) `2/3` · e) `3.6` · f) `3.6878`.

a) Minima des lignes : $-4$ et $-2$, donc le maximin vaut $-2$ (le sud). Maxima des colonnes : $3$ et $6$, donc le minimax vaut $3$ (le garde au nord).
b) Le garde est indifférent : $-4p + 3(1 - p) = 6p - 2(1 - p)$, soit $3 - 7p = 8p - 2$ et $p^\star = \frac13$.
c) Le braconnier est indifférent : $-4q + 6(1 - q) = 3q - 2(1 - q)$, soit $6 - 10q = 5q - 2$ et $q^\star = \frac{8}{15}$.
d) $v = 3 - 7 \times \frac13 = \frac23$ (environ 67 €). Par la formule : $\kappa = a - b - c + d = -15$ et $v = \frac{ad - bc}{\kappa} = \frac{8 - 18}{-15} = \frac23$, entre le maximin et le minimax.
e) Triés, A donne $19, 21, 26, 32, 34$ et B donne $14, 18, 22, 29, 37$ ; les écarts appariés valent $5, 3, 4, 3, 3$ en valeur absolue : $W_1 = \frac{18}{5} = 3{,}6$ cm.
f) $W_2 = \sqrt{\frac{25 + 9 + 16 + 9 + 9}{5}} = \sqrt{13{,}6} \approx 3{,}6878$ cm.

Sur ta copie : pas de point selle, parce que le maximin ($-2$) est strictement plus petit que le minimax ($3$) ; $W_1 = 3{,}6 \le W_2 \approx 3{,}688$ : la moyenne des écarts appariés est au plus la racine de la moyenne de leurs carrés (Jensen, ou Cauchy-Schwarz), avec égalité seulement si tous les écarts appariés sont égaux en valeur absolue.

**Erreurs fréquentes** :
- en a), prendre les minima des colonnes pour le garde ($-2$ au lieu de 3), ou donner le minimax en premier ;
- en b), écrire l'indifférence du mauvais joueur (on trouve $\frac{8}{15}$), ou donner $1 - p^\star = \frac23$ ;
- en c), symétriquement, $\frac13$ ou $\frac{7}{15}$ ;
- en d), répondre le maximin ou le minimax, ou se tromper de signe sur $\kappa$ ($-\frac23$) ;
- en e), apparier dans l'ordre des relevés (11,2), donner l'écart des moyennes (2,4), ou la somme des écarts (18) ;
- en f), oublier la racine (13,6), ou ne pas trier ($\sqrt{186} \approx 13{,}64$).

**Remédiation** : M27.1, M27.2, M27.8, M27.14, M27.20, M27.Q1, M27.Q2, M27.Q5.

## CP6.6 — Des distances aux positions : double centrage, matrice de Gram, et une configuration à une isométrie près ✏️ · 8 points (2 par sous-question)

**Réponses** : a) `124/3` · b) `[[25, 5, -30], [5, 1, -6], [-30, -6, 36]]` · c) `[62, 0, 0]` · d) `[[5], [1], [-6]]`.

a) Les neuf coefficients de $\mathbf{D}^{(2)}$ ont pour somme $2(16 + 121 + 49) = 372$, et $s = \frac{372}{9} = \frac{124}{3}$.
b) Les moyennes des lignes : $r_A = \frac{137}{3}$, $r_B = \frac{65}{3}$, $r_C = \frac{170}{3}$. Puis $G_{ij} = -\frac12\big(D^{(2)}_{ij} - r_i - r_j + s\big)$ : $G_{AA} = -\frac12\big(0 - \frac{274}{3} + \frac{124}{3}\big) = 25$, $G_{AB} = -\frac12(16 - 26) = 5$, $G_{AC} = -\frac12(121 - 61) = -30$, $G_{BB} = 1$, $G_{BC} = -\frac12(49 - 37) = -6$, $G_{CC} = 36$.
c) Les lignes de $\mathbf{G}$ sont proportionnelles : $(25, 5, -30) = 5\,(5, 1, -6)$ et $(-30, -6, 36) = -6\,(5, 1, -6)$. Donc $\mathbf{G} = \mathbf{v}\mathbf{v}^\top$ avec $\mathbf{v} = (5, 1, -6)$, de rang 1 : $\mathbf{G}\mathbf{v} = \lVert\mathbf{v}\rVert^2\,\mathbf{v} = 62\,\mathbf{v}$, et tout vecteur orthogonal à $\mathbf{v}$ a pour image $\mathbf{0}$. Les valeurs propres sont 62, 0 et 0 (la trace vaut bien $25 + 1 + 36 = 62$).
d) $\mathbf{q}_1 = \frac{\mathbf{v}}{\sqrt{62}}$ et $\sqrt{62}\,\mathbf{q}_1 = \mathbf{v} = (5, 1, -6)$ : une seule colonne, et la coordonnée de A, 5, est positive. A $= 5$, B $= 1$, C $= -6$, en hm.

Sur ta copie : les lignes de $\mathbf{G}$ ont pour somme $25 + 5 - 30 = 0$, $5 + 1 - 6 = 0$ et $-30 - 6 + 36 = 0$, donc $\mathbf{G}\mathbf{1} = \mathbf{0}$ (les points sont centrés) ; une seule valeur propre non nulle : les bouées sont **alignées** (la configuration tient sur une droite), avec $\mathrm{AB} = 4$, $\mathrm{BC} = 7$ et $\mathrm{AC} = 11 = 4 + 7$, B entre A et C ; la carte est centrée au barycentre des bouées, et peut différer de la vraie position par une translation, une rotation et une symétrie : les distances ne voient ni l'origine, ni l'orientation de la droite.

**Erreurs fréquentes** :
- en a), oublier les zéros de la diagonale (62, la moyenne des six autres coefficients), ou compter chaque distance une seule fois ($\frac{62}{3}$) ;
- en b), oublier le facteur $-\frac12$, se tromper de signe devant $s$, ou centrer les distances au lieu de leurs carrés ;
- en c), ranger les valeurs propres dans l'ordre croissant, oublier les valeurs propres nulles, ou prendre la diagonale de $\mathbf{G}$ (25, 1, 36) pour ses valeurs propres ;
- en d), changer le signe de la colonne, ou multiplier $\mathbf{q}_1$ par $\lambda_1$ ($\approx (39{,}37 ;\ 7{,}87 ;\ -47{,}24)$), ou ne pas le multiplier ($\approx (0{,}635 ;\ 0{,}127 ;\ -0{,}762)$), au lieu de $\sqrt{\lambda_1}$.

**Remédiation** : M28.1, M28.2, M28.8, M28.13, M28.18, M28.Q1.

## CP6.7 — La distance de Fréchet de deux gaussiennes du plan de covariances proportionnelles, et le biais de la distance entre deux moyennes estimées ✏️ · 9 points (1,8 par sous-question)

**Réponses** : a) `[676, 256]` · b) `21` · c) `5.5678` · d) `13.15` · e) `14.2`.

a) $\boldsymbol{\Sigma}_A$ a pour trace 21 et pour déterminant 104 : ses valeurs propres sont 13 et 8. $\boldsymbol{\Sigma}_A\boldsymbol{\Sigma}_B = 4\boldsymbol{\Sigma}_A^2$ a les mêmes vecteurs propres, de valeurs propres $4 \times 169 = 676$ et $4 \times 64 = 256$. (Directement : $\boldsymbol{\Sigma}_A\boldsymbol{\Sigma}_B = \begin{pmatrix} 592 & 168 \\ 168 & 340 \end{pmatrix}$, de trace 932 et de déterminant 173 056.)
b) $21 + 84 - 2(26 + 16) = 21$.
c) $\lVert\boldsymbol{\mu}_A - \boldsymbol{\mu}_B\rVert^2 = 3^2 + 1^2 = 10$, et $W_2 = \sqrt{10 + 21} = \sqrt{31} \approx 5{,}5678$ MWh.
d) $10 + \frac{21}{20} + \frac{84}{40} = 10 + 1{,}05 + 2{,}1 = 13{,}15$ MWh².
e) $10 + \frac{21}{25} + \frac{84}{25} = 10 + 0{,}84 + 3{,}36 = 14{,}2$ MWh².

Sur ta copie : les valeurs propres de $\boldsymbol{\Sigma}_A$ (13 et 8) ; $\boldsymbol{\Sigma}_B = c\,\boldsymbol{\Sigma}_A$ avec $c = 4$, donc $\boldsymbol{\Sigma}_A\boldsymbol{\Sigma}_B = c\,\boldsymbol{\Sigma}_A^2$, de valeurs propres $c\lambda_i^2$ et de racines $\sqrt c\,\lambda_i$ ; la part des covariances vaut $(1 + c - 2\sqrt c)\operatorname{tr}\boldsymbol{\Sigma}_A = (\sqrt c - 1)^2\operatorname{tr}\boldsymbol{\Sigma}_A = \operatorname{tr}\boldsymbol{\Sigma}_A = 21$. d) et e) portent sur les mêmes lois, et le vrai $\lVert\boldsymbol{\mu}_A - \boldsymbol{\mu}_B\rVert^2$ vaut 10 ; pourtant l'espérance estimée vaut 13,15 ou 14,2 selon les tailles des échantillons : une distance estimée est biaisée vers le haut, de $\frac{\operatorname{tr}\boldsymbol{\Sigma}_A}{n_A} + \frac{\operatorname{tr}\boldsymbol{\Sigma}_B}{n_B}$. On ne compare deux distances estimées qu'à tailles d'échantillons égales, ou après avoir retranché ce biais.

**Erreurs fréquentes** :
- en a), donner les valeurs propres de $\boldsymbol{\Sigma}_A$ (13 et 8), ou leurs racines (26 et 16) ;
- en b), oublier le facteur 2 (63), les racines (−1 759), ou tout le terme croisé (105) ;
- en c), oublier la racine (31), les moyennes ($\sqrt{21} \approx 4{,}583$), ou leur carré ($\approx 4{,}916$) ;
- en d), oublier de diviser par les tailles (115), les échanger (14,725), diviser la somme des traces par le nombre total de jours (11,75), ou oublier l'écart des vraies moyennes (3,15) ;
- en e), prendre deux échantillons de la même ferme (1,68), ne compter qu'un terme (10,84 ou 13,36), diviser la somme des traces par le nombre total de jours (12,1), ou oublier l'écart des vraies moyennes (4,2).

**Remédiation** : M27.9, M27.15, M27.16, M27.25, M27.Q6, M27.R3, M27.E2.

## CP6.8 — Une démonstration au choix ∂ · 12 points (3 par étape)

Toute démonstration juste et complète d'une étape a tous les points de cette étape, même si elle prend un autre chemin que celui du corrigé.

### Sujet A — L'entropie d'une loi tempérée croît avec la température

1. **[3]** $p_i^{1/T} = e^{\frac1T\ln p_i} = e^{-\beta E_i}$, donc $p_i^{(T)} = \frac{e^{-\beta E_i}}{Z}$ : la loi tempérée est la loi de Boltzmann des énergies $E_i$. Alors $\ln p_i^{(T)} = -\beta E_i - \ln Z$, et $H(T) = -\sum_i p_i^{(T)}(-\beta E_i - \ln Z) = \beta\langle E\rangle + \ln Z$, puisque $\sum_i p_i^{(T)} = 1$.
2. **[3]** $\frac{\mathrm{d}Z}{\mathrm{d}\beta} = -\sum_j E_je^{-\beta E_j} = -Z\langle E\rangle$, donc $\frac{\mathrm{d}\ln Z}{\mathrm{d}\beta} = -\langle E\rangle$. Par la dérivée d'un quotient, $\frac{\mathrm{d}p_i^{(T)}}{\mathrm{d}\beta} = \frac{-E_ie^{-\beta E_i}}{Z} - \frac{e^{-\beta E_i}}{Z}\,\frac{\mathrm{d}\ln Z}{\mathrm{d}\beta} = p_i^{(T)}\big(\langle E\rangle - E_i\big)$. Puis $\frac{\mathrm{d}\langle E\rangle}{\mathrm{d}\beta} = \sum_i E_i\,p_i^{(T)}\big(\langle E\rangle - E_i\big) = \langle E\rangle^2 - \langle E^2\rangle = -\mathbb{V}(E)$ (les $E_i$ ne dépendent pas de $\beta$).
3. **[3]** $\frac{\mathrm{d}H}{\mathrm{d}\beta} = \langle E\rangle + \beta\,\frac{\mathrm{d}\langle E\rangle}{\mathrm{d}\beta} + \frac{\mathrm{d}\ln Z}{\mathrm{d}\beta} = \langle E\rangle - \beta\,\mathbb{V}(E) - \langle E\rangle = -\beta\,\mathbb{V}(E)$. Comme $\beta = \frac1T$, $\frac{\mathrm{d}\beta}{\mathrm{d}T} = -\frac{1}{T^2}$ et $\frac{\mathrm{d}H}{\mathrm{d}T} = -\beta\,\mathbb{V}(E) \times \big(-\frac{1}{T^2}\big) = \frac{\mathbb{V}(E)}{T^3} \ge 0$ (une variance est positive ou nulle, et $T > 0$). Elle n'est nulle que si $E$ est constante sur le support de $\mathbf{p}^{(T)}$, c'est-à-dire sur toutes les issues (toutes les $p_i$ sont positives) : si $\mathbf{p}$ est uniforme. Alors $\mathbf{p}^{(T)} = \mathbf{p}$ pour tout $T$, et $H = \ln n$ est constante ; sinon $\mathbb{V}(E) > 0$ à toute température, et $H$ est **strictement croissante** en $T$.
4. **[3]** En $T = 1$, $\mathbf{p}^{(1)} = \mathbf{p}$. $H(1) = -0{,}6\ln 0{,}6 - 0{,}4\ln 0{,}1 \approx 0{,}3065 + 0{,}9210 = 1{,}2275$. En $T = 1$, l'énergie ne prend que deux valeurs, $-\ln 0{,}6$ (probabilité 0,6) et $\ln 10$ (probabilité 0,4), d'écart $\ln 6$ : $\mathbb{V}(E) = 0{,}6 \times 0{,}4 \times (\ln 6)^2 \approx 0{,}24 \times 3{,}2104 \approx 0{,}7705$, et $\frac{\mathrm{d}H}{\mathrm{d}T}(1) \approx 0{,}7705$. (Pour aller plus loin, non noté : en divisant numérateur et dénominateur par $0{,}1^{1/T}$, $\mathbf{p}^{(T)} = \frac{(a, 1, 1, 1, 1)}{a + 4}$ avec $a = 6^{1/T}$ ; quand $T \to 0$, $a \to +\infty$ et $H \to 0$ ; quand $T \to +\infty$, $a \to 1$, la loi devient uniforme et $H \to \ln 5$.)

**Grille de relecture.**
- (1) L'écriture en exponentielle, et le calcul de $H$ avec $\sum_i p_i^{(T)} = 1$.
- (2) Les trois dérivées, avec la règle utilisée (quotient, ou dérivée de $\ln Z$) et la variance reconnue.
- (3) La dérivée en $\beta$, le changement de variable $\beta = \frac1T$ avec son signe, le signe de la variance, et le cas d'égalité (la loi uniforme).
- (4) $H(1)$ et $\frac{\mathrm{d}H}{\mathrm{d}T}(1)$, par la variance (une dérivée calculée directement compte autant).

### Sujet B — La loi de Boltzmann minimise l'énergie libre

1. **[3]** $\ln p^\star_i = -\frac{E_i}{T} - \ln Z$ ; en multipliant par $-T$ : $E_i = -T\ln p^\star_i - T\ln Z$.
2. **[3]** $\mathbb{E}_q[E] = \sum_i q_iE_i = -T\sum_i q_i\ln p^\star_i - T\ln Z$, puisque $\sum_i q_i = 1$ ; et $-T\,H(q) = T\sum_i q_i\ln q_i$. En additionnant : $F(q) = T\sum_i q_i\ln\frac{q_i}{p^\star_i} - T\ln Z = T\,\mathrm{KL}(q \,\|\, p^\star) - T\ln Z$. (Les issues où $q_i = 0$ ne comptent ni dans $\mathbb{E}_q[E]$ ni dans l'entropie, avec $0\ln 0 = 0$, ni dans la KL.)
3. **[3]** $\mathrm{KL}(q \,\|\, p^\star) \ge 0$, avec égalité si et seulement si $q = p^\star$ (inégalité de Gibbs, par Jensen) ; et $T > 0$. Donc $F(q) \ge -T\ln Z$, avec égalité seulement pour $q = p^\star$ : la loi de Boltzmann est l'unique minimum de l'énergie libre, et $F(p^\star) = -T\ln Z$. En divisant par $-T$ : $\ln Z = -\frac{F(q)}{T} + \mathrm{KL}(q \,\|\, p^\star)$. C'est l'identité de M25b, $\ln p(\mathbf{x}) = \operatorname{ELBO}(q) + \mathrm{KL}\big(q \,\|\, p(\mathbf{z} \mid \mathbf{x})\big)$ : $\ln Z$ joue le rôle de $\ln p(\mathbf{x})$ (le logarithme d'une constante de normalisation), $-\frac{F(q)}{T} = \mathbb{E}_q\big[-\frac ET\big] + H(q)$ celui de l'ELBO (l'espérance d'une log-densité non normalisée, plus une entropie), et $p^\star$ celui du posterior. Maximiser l'ELBO, c'est minimiser une énergie libre ; l'écart est la KL.
4. **[3]** $e^{-E_i} = (1, \frac13, \frac19)$, $Z = \frac{13}{9}$ (valeur exacte), $p^\star = \big(\frac{9}{13}, \frac{3}{13}, \frac{1}{13}\big) \approx (0{,}6923 ;\ 0{,}2308 ;\ 0{,}0769)$, et $F(p^\star) = -\ln\frac{13}{9} \approx -0{,}3677$. Pour $q$ uniforme : $\mathbb{E}_q[E] = \frac{0 + \ln 3 + 2\ln 3}{3} = \ln 3$ et $H(q) = \ln 3$, donc $F = 0$. Pour $q = (1, 0, 0)$ : énergie 0, entropie 0, $F = 0$. (Pour aller plus loin, non noté : $\mathrm{KL}(q \,\|\, p^\star) = \frac13\sum_i\ln\frac{1/3}{p^\star_i} = -\ln 3 - \frac13\ln\frac{9 \times 3 \times 1}{13^3} = \ln\frac{13}{9} \approx 0{,}3677 = F(q) - F(p^\star)$ pour $q$ uniforme.) La loi qui met toute sa masse sur l'énergie la plus basse minimise $\mathbb{E}_q[E]$, mais son entropie est nulle : déplacer une petite masse $\varepsilon$ vers les autres issues coûte une énergie de l'ordre de $\varepsilon$, et rapporte une entropie de l'ordre de $-\varepsilon\ln\varepsilon$, bien plus grande quand $\varepsilon$ est petit. À $T > 0$, $F$ arbitre entre énergie et entropie ; ce n'est qu'en $T \to 0$ que $p^\star$ se concentre sur l'énergie la plus basse.

**Grille de relecture.**
- (1) Le logarithme de $p^\star_i$, et la multiplication par $-T$.
- (2) $\mathbb{E}_q[E]$ réécrite avec $\sum_i q_i = 1$, l'entropie, et la KL reconnue.
- (3) La positivité de la KL et son cas d'égalité, la conclusion (le minimum, sa valeur, son unicité), et la correspondance avec $\ln p(\mathbf{x}) = \operatorname{ELBO} + \mathrm{KL}$, terme à terme.
- (4) $Z$, $p^\star$, $F(p^\star)$, les deux autres valeurs de $F$, et l'arbitrage entre énergie et entropie.

**Erreurs fréquentes** (deux sujets) :
- en A, dériver $p_i^{(T)}$ sans dériver $Z$, oublier le signe de $\frac{\mathrm{d}\beta}{\mathrm{d}T}$, ou conclure « croissante » sans traiter le cas d'égalité ;
- en A, calculer $\mathbb{V}(E)$ en $T = 1$ sous une autre loi que $\mathbf{p}^{(1)} = \mathbf{p}$ ;
- en B, écrire $F(q) = T\,\mathrm{KL}(p^\star \,\|\, q) - T\ln Z$ (la KL dans le mauvais sens), ou oublier le facteur $T$ ;
- en B, croire que la loi d'énergie minimale minimise $F$, ou ne pas dire que l'égalité de la KL n'a lieu qu'en $q = p^\star$.

**Remédiation** :
- A : M28.6, M28.11, M28.Q4, M28.R3 ;
- B : M25b.5, M25b.6, M25a.13, M25b.Q5, M25b.R2.

## CP6.9 — Corriger une copie : cinq erreurs, une par chapitre 🐛 · 9 points

**Réponse de a)** : `ACEGH`. **[4,5]** (0,9 par lettre juste, −0,9 par lettre en trop, sans descendre sous 0)

b) Une ligne par erreur **[0,9 chacune]** :
- **(A)** (M26) $\lvert -0{,}6\rvert < 1$ : la chaîne (irréductible, apériodique, ses coefficients diagonaux sont positifs) converge vers $\boldsymbol{\pi} = \big(\frac{13}{32}, \frac{19}{32}\big)$. La valeur propre négative fait seulement changer de signe l'écart $\boldsymbol{\mu}_n - \boldsymbol{\pi}$, qui est multiplié par $-0{,}6$ à chaque pas : une oscillation amortie. C'est $\lvert\lambda_2\rvert$ qui compte, pas son signe ; une oscillation sans fin demande $\lvert\lambda_2\rvert = 1$ (une chaîne périodique).
- **(C)** (M25a) En dimension 2, l'ellipse de niveau $c$ contient $1 - e^{-c^2/2} = 1 - e^{-3{,}125} \approx 95{,}6$ % des tirages, moins que les 98,8 % de la dimension 1 : à niveau égal, la masse baisse quand la dimension grandit.
- **(E)** (M25b) $\mathrm{KL}(p \,\|\, q)$ sur les gaussiennes est minimale quand $q$ a la moyenne et la variance de $p$ : la variance du mélange est la moyenne des variances plus la variance des moyennes, $2 + \frac13 \times 36 + \frac23 \times 9 = 2 + 18 = 20$, donc $q = \mathcal{N}(6, 20)$.
- **(G)** (M28) La période de $\cos\big(2\pi(f_1i + f_2j)\big)$ est $\frac{1}{\sqrt{f_1^2 + f_2^2}} = \frac{1}{\sqrt{0{,}0576 + 0{,}0049}} = \frac{1}{0{,}25} = 4$ cases, mesurée dans la direction $(f_1, f_2)$ ; les périodes le long des axes ne s'additionnent pas.
- **(H)** (M27) $W_1 = 0$ : le couplage $\operatorname{diag}(\frac12, \frac12)$ ne déplace rien et coûte 0. $W_1$ est le **minimum** du coût sur tous les couplages ; le couplage indépendant n'est qu'un couplage admissible, en général plus cher (fiche §7 : 1,84 contre 1,2).

Les lignes justes :
- **(B)** Vrai : $\mathbf{X}\mathbf{X}^\top$ et $\mathbf{X}^\top\mathbf{X}$ ont les mêmes valeurs propres non nulles (M28 §1, M12d), et le rang est au plus 3.
- **(D)** Pour le pas alterné sur $xy$, $x^2 + y^2 - \eta\,xy$ est constant (M27 §4) ; avec $\eta = 0{,}4 < 2$, cette forme quadratique est définie positive : ses lignes de niveau sont des ellipses.
- **(F)** $\frac12\ln(2\pi e \times 0{,}03) = \frac12\ln 0{,}5124 \approx -0{,}334$ : une entropie différentielle est négative dès que $\sigma^2 < \frac{1}{2\pi e} \approx 0{,}0585$. Seule l'entropie d'une loi discrète est toujours positive.

**Erreurs fréquentes** :
- laisser passer (A), en confondant « valeur propre négative » et « valeur propre de module 1 » ;
- laisser passer (C), en appliquant en dimension 2 les pourcentages de la dimension 1 ;
- laisser passer (E), en prenant la variance d'une composante pour celle du mélange ;
- laisser passer (G), en additionnant les périodes des deux axes ;
- laisser passer (H), en prenant le couplage indépendant pour le plan optimal ;
- croire (B) fausse, parce qu'une matrice $50 \times 50$ aurait 50 valeurs propres non nulles ;
- croire (D) fausse, en prêtant au pas alterné la spirale du pas simultané ;
- croire (F) fausse, parce qu'une entropie « ne peut pas être négative ».

**Remédiation** : M25a.3, M25a.11, M25a.14, M25a.Q3, M25b.2, M25b.13, M25b.27, M26.3, M26.23, M26.Q2, M27.4, M27.7, M27.Q5, M28.1, M28.Q1, M28.5, M28.Q3.

## CP6.10 — Problème de synthèse : une file d'attente à trois états suivie de façon gloutonne, puis échantillonnée après la troncature top-p de ses transitions 🔗 · 16 points ($\frac{16}{7} \approx 2{,}29$ par sous-question)

**Réponses** : a) `[1, 2, 1]` · b) `[1, 2]` · c) `[2, 1]` · d) `[0, 0.4177, 0.5823]` · e) `0.2357` · f) `[[0.3478, 0.6522, 0], [0, 0.4177, 0.5823], [0, 0.6316, 0.3684]]` · g) `[0, 0.5203, 0.4797]`.

a) Le plus grand coefficient de chaque ligne : 0,60 (état 1) dans la ligne 0, 0,46 (état 2) dans la ligne 1, 0,60 (état 1) dans la ligne 2.
b) La suite vaut $0, 1, 2, 1, 2, \ldots$ : l'état 0 ne revient jamais, donc la prépériode vaut $\mu = 1$, et le cycle $(1, 2)$ donne la période $\lambda = 2$.
c) La ligne 1 rangée par probabilité décroissante : 2 (0,46), 1 (0,33), 0 (0,21). $0{,}46 < 0{,}68 \le 0{,}79$ : $S_1 = [2, 1]$, de masse $P(S_1) = 0{,}79$.
d) $\mathbf{p}_{S_1} = \big(0 ;\ \frac{0{,}33}{0{,}79} ;\ \frac{0{,}46}{0{,}79}\big) \approx (0 ;\ 0{,}4177 ;\ 0{,}5823)$.
e) $\mathrm{KL}(\mathbf{p}_{S_1} \,\|\, \mathbf{p}_1) = \sum_{i \in S_1}\frac{p_i}{P(S_1)}\ln\frac{p_i/P(S_1)}{p_i} = -\ln P(S_1) = -\ln 0{,}79 \approx 0{,}2357$ nat.
f) Ligne 0 : 1 (0,60) puis 0 (0,32), masse 0,92 : $(0{,}3478 ;\ 0{,}6522 ;\ 0)$. Ligne 2 : 1 (0,60) puis 2 (0,35), masse 0,95 : $(0 ;\ 0{,}6316 ;\ 0{,}3684)$. Ligne 1 : d).
g) La colonne 0 de $\mathbf{P}'$ n'a qu'un coefficient non nul, $P'_{00}$ : $\pi'_0 = \pi'_0 \times 0{,}3478$, donc $\pi'_0 = 0$. Entre 1 et 2, à l'équilibre, le flux de 1 vers 2 égale le flux de 2 vers 1 : $\pi'_1 \times \frac{46}{79} = \pi'_2 \times \frac{12}{19}$, donc $\frac{\pi'_1}{\pi'_2} = \frac{12 \times 79}{19 \times 46} = \frac{474}{437}$ et $\boldsymbol{\pi}' = \big(0 ;\ \frac{474}{911} ;\ \frac{437}{911}\big) \approx (0 ;\ 0{,}5203 ;\ 0{,}4797)$.

Sur ta copie :
- Sur un ensemble de $N = 3$ états, $\mu + \lambda \le N$ (parmi $u_0, \ldots, u_3$, deux sont égaux, par le principe des tiroirs) : ici $1 + 2 = 3$.
- $\mathrm{KL}(\mathbf{p}_1 \,\|\, \mathbf{p}_{S_1})$ est infinie : $\mathbf{p}_1$ donne 0,21 à l'état 0, où $\mathbf{p}_{S_1}$ est nulle.
- $\pi'_0 = 0$ : la troncature a coupé, dans les lignes 1 et 2, le passage vers la file vide (0,21 et 0,05, les moins probables). Une fois la file non vide, le simulateur aléatoire ne la revoit **jamais** vide, alors que la vraie file l'est environ 17 % du temps : couper les événements rares change le comportement à long terme.
- Pour aller plus loin (non noté) : la loi stationnaire de $\mathbf{P}$ est $\big(\frac{1595}{9271} ;\ \frac{60}{127} ;\ \frac{3296}{9271}\big) \approx (0{,}1720 ;\ 0{,}4724 ;\ 0{,}3555)$.

**Erreurs fréquentes** :
- en a), lire les colonnes au lieu des lignes ($[0, 0, 1]$) ;
- en b), compter la queue dans la période ($[1, 3]$), ou oublier la queue ($[0, 2]$) ;
- en c), s'arrêter à l'état le plus probable ($[2]$), garder les trois, ou ranger les états dans l'ordre de leurs numéros ;
- en d), ne pas renormaliser ($(0 ;\ 0{,}33 ;\ 0{,}46)$), ou répartir la masse coupée à parts égales ($(0 ;\ 0{,}435 ;\ 0{,}565)$) ;
- en e), prendre $-\ln 0{,}21 \approx 1{,}5606$, un logarithme en base 2 (0,3401), ou la masse coupée (0,21) ;
- en f), ne pas renormaliser, ou ne garder que l'état le plus probable de chaque ligne ;
- en g), donner la loi stationnaire de $\mathbf{P}$, oublier de normaliser ($(0 ;\ 1 ;\ 0{,}9219)$), ou échanger $\pi'_1$ et $\pi'_2$.

**Remédiation** : M28.6, M28.7, M28.10, M28.14, M28.Q4, M28.Q5, M26.2, M26.17, M26.Q2.

## Barème récapitulatif et remédiation

| Question | Points (sur 111) | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP6.Q1 | 10 | M25a, M25b, M26, M27, M28 | les exercices cités au CP6.Q1, puis les quiz et les flashcards des cinq chapitres |
| CP6.1 | 10 | M25a | M25a.2, M25a.4, M25a.10, M25a.21, M25a.22, M25a.Q2, M25a.Q4, M25a.R2 |
| CP6.2 | 9 | M25a | M25a.8, M25a.9, M25a.14, M25a.15, M25a.Q7, M25a.Q8 |
| CP6.3 | 10 | M25b | M25b.3, M25b.5, M25b.6, M25b.20, M25b.21, M25b.Q3, M25b.Q4, M25b.Q5 |
| CP6.4 | 9 | M26 | M26.1, M26.4, M26.6, M26.11, M26.18, M26.Q1, M26.Q5 |
| CP6.5 | 9 | M27 | M27.1, M27.2, M27.8, M27.14, M27.20, M27.Q1, M27.Q2, M27.Q5 |
| CP6.6 | 8 | M28 | M28.1, M28.2, M28.8, M28.13, M28.18, M28.Q1 |
| CP6.7 | 9 | M27 | M27.9, M27.15, M27.16, M27.25, M27.Q6, M27.R3, M27.E2 |
| CP6.8 | 12 | M28 ou M25b | A : M28.6, M28.11, M28.Q4, M28.R3 ; B : M25b.5, M25b.6, M25a.13, M25b.Q5, M25b.R2 |
| CP6.9 | 9 | M25a, M25b, M26, M27, M28 | M25a.3, M25a.11, M25a.14, M25a.Q3, M25b.2, M25b.13, M25b.27, M26.3, M26.23, M26.Q2, M27.4, M27.7, M27.Q5, M28.1, M28.Q1, M28.5, M28.Q3 |
| CP6.10 | 16 | M26, M28 | M28.6, M28.7, M28.10, M28.14, M28.Q4, M28.Q5, M26.2, M26.17, M26.Q2 |
| **Total** | **111** | | **note sur 20 = total × 20/111 (total ÷ 5,55)** |

**Lire ta note** (sur 20, après la division par 5,55)
- **16 à 20** : la partie VI est solide. Passe au checkpoint VI de workbookIA ; garde les flashcards de M25a à M28 dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe au checkpoint VI de workbookIA.
- **8 à moins de 12** : avant le checkpoint VI de workbookIA, fais la remédiation, relis ta synthèse et les fiches des chapitres où tu as perdu le plus de points.
- **Moins de 8** : reprends les exercices ★★ des sections où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
