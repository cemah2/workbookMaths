# M14 · Les maths des ensembles — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m14_ensembles/06_mes_reponses.md` (créée par `python tools/start_chapter.py M14`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : $X$ de loi $\mathcal{B}(n, p)$ compte des succès ; la divergence $\mathrm{KL}(a \Vert p) = a\ln\frac{a}{p} + (1 - a)\ln\frac{1 - a}{1 - p}$ est en **nats** ; $\boldsymbol{\Sigma}$ est une matrice de covariance et $\mathbf{w}$ un vecteur de poids positifs de somme 1 ; Hedge donne à l'expert $k$, avant le tour $t$, un poids proportionnel à $e^{-\eta L_t[k]}$, où $L_t[k]$ est sa loss cumulée sur les tours **précédents** ; le regret sur $T$ tours est ta loss totale moins celle du meilleur expert.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M14.Q1 — La queue d'une loi binomiale et ses bornes : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Vrai ou faux : pour $X$ de loi $\mathcal{B}(n, p)$, $P(X \ge k) = 1 - P(X \le k)$.
2. Vrai ou faux : la borne de Markov $P(X \ge na) \le \frac{p}{a}$ diminue quand $n$ augmente.
3. Vrai ou faux : pour $a > p$, la borne de Chernoff est toujours au plus égale à celle de Hoeffding.
4. Que dit la borne de Chernoff quand $a \le p$, et pourquoi ?
5. $a$ et $p$ sont fixés. Que devient la borne de Chernoff de $P(X \ge na)$ quand on double $n$ ?
6. Vrai ou faux : $\mathrm{KL}(a \Vert p) = \mathrm{KL}(p \Vert a)$.

### M14.Q2 — Corrélation et variance d'une moyenne 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. $\mathbb{V}(X) = 5$, $\mathbb{V}(Y) = 3$, $\operatorname{Cov}(X, Y) = -2$ : que vaut $\mathbb{V}(X + Y)$ ?
2. Vrai ou faux : la variance d'une moyenne pondérée est la moyenne pondérée des variances.
3. $M$ variables indépendantes de même variance $\sigma^2$ : variance de leur moyenne ?
4. Vrai ou faux : une covariance négative entre deux capteurs fait baisser la variance de leur moyenne.
5. $X_1$ et $X_2$ sont indépendantes, de variance $\sigma^2$, et $X_3 = X_1$ (une copie exacte). Que vaut la variance de la moyenne simple de $X_1$, $X_2$, $X_3$ ? Compare à $\frac{\sigma^2}{3}$.
6. Vrai ou faux : une moyenne pondérée, à poids positifs de somme 1, de variables de variance au plus $\sigma^2$ peut avoir une variance plus grande que $\sigma^2$.

### M14.Q3 — Des limites remarquables 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. $\lim_{n \to +\infty}\left(1 + \frac{3}{n}\right)^n$ ?
2. $\lim_{n \to +\infty}\left(1 - \frac{1}{2n}\right)^n$ ?
3. $\lim_{n \to +\infty}\left(1 + \frac{1}{n}\right)^{2n}$ ?
4. $\lim_{n \to +\infty}\left(1 + \frac{5}{n^2}\right)^n$ ?
5. $\lim_{n \to +\infty} n\ln\left(1 + \frac{7}{n}\right)$ ?
6. Vrai ou faux : pour $n = 100$, $\left(1 + \frac{4}{n}\right)^n$ est à moins de 1 % de $e^4$.

### M14.Q4 — Des poids exponentiels 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C*

1. Deux experts, de losses cumulées $(1, 0)$, et $\eta = \ln 5$ : leurs poids ?
2. Vrai ou faux : si tous les experts ont 5 de loss en plus au même tour, les poids changent.
3. Que deviennent les poids de Hedge quand $\eta \to 0$ ? Et quand $\eta \to +\infty$ ?
4. Avec le meilleur $\eta$ pour un horizon $T$, comment le regret de Hedge grandit-il avec $T$ ? Et le regret moyen par tour ?
5. Pourquoi retranche-t-on la plus petite loss cumulée avant de prendre l'exponentielle ?
6. Vrai ou faux : Hedge fait au moins aussi bien que le meilleur expert à chaque tour.

<a id="rappels"></a>

## 🔁 Rappels

### M14.R1 — La log-loss et la divergence KL (M13a, M06) 🔁 ★ ⏱️ 5 min
*Fiche §1 et §5 · parcours C, E*

1. Calcule $\mathrm{KL}(0{,}25 \Vert 0{,}1)$ en nats (4 décimales).
2. Calcule $\mathrm{KL}(0{,}1 \Vert 0{,}25)$. Que montre la comparaison avec 1 ?
3. Un modèle annonce toujours la probabilité $0{,}25$ pour le label 1, sur des données où 10 % des labels valent 1. Que vaut sa log-loss moyenne (en nats, 4 décimales) ?
4. Écris cette log-loss comme l'entropie $H(0{,}1)$ plus une divergence : laquelle ?
5. Quand $\mathrm{KL}(a \Vert p)$ est-elle nulle ? Quelle propriété de M06 le dit ?

### M14.R2 — La variance d'une somme et la matrice de covariance (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

Dans tout le rappel, $\mathbb{V}(X) = 2$, $\mathbb{V}(Y) = 3$ et $\operatorname{Cov}(X, Y) = 0{,}5$.
1. Écris $\mathbb{V}(aX + bY)$ en fonction de $\mathbb{V}(X)$, $\mathbb{V}(Y)$ et $\operatorname{Cov}(X, Y)$, puis calcule $\mathbb{V}(3X - 2Y)$.
2. La variance de la moyenne $\frac{X + Y}{2}$ ? Compare-la à la moyenne des deux variances.
3. $\operatorname{Cov}(X + Y,\ X - Y)$ ?
4. La matrice de covariance du couple $(X, Y)$ ; pourquoi une matrice de covariance est-elle symétrique et semi-définie positive ?
5. La corrélation de $X$ et $Y$ (4 décimales) ?

### M14.R3 — Taylor et ln(1 + u) (M05a) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Le développement de Taylor de $\ln(1 + u)$ en 0, à l'ordre 2 ?
2. En déduire une valeur approchée de $\ln 0{,}97$ ; compare à la valeur exacte (6 décimales). L'approximation est-elle au-dessus ou au-dessous ?
3. Pour quels $u$ la série $u - \frac{u^2}{2} + \frac{u^3}{3} - \cdots$ converge-t-elle vers $\ln(1 + u)$ ?
4. Que vaut $\lim_{u \to 0}\frac{\ln(1 + u)}{u}$, et que dit-elle de $\ln(1 + u)$ pour $u$ petit ?
5. Le développement en série de $e^x$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction entre guillemets, comme `"3/7"`, ou une liste de fractions, comme `["1/4", "3/4"]` ;
- une liste entre crochets, comme `[0.2, -1]`.

### Ex M14.1 — La fiabilité d'un système « k parmi n » : au moins k composants qui marchent ✏️ ★ ⏱️ 15 min
**Objectif :** calculer la queue d'une loi binomiale, puis la comparer aux bornes de Markov, de Hoeffding et de Chernoff.
**Prérequis :** fiche §1 ; M02b ; M11 · **Parcours :** C, E

Un service de calcul tourne sur 9 machines et tient la charge tant qu'**au moins 7** fonctionnent. Chaque machine fonctionne toute la journée avec la probabilité $0{,}9$, indépendamment des autres. $X$ est le nombre de machines qui fonctionnent, $F = 9 - X$ le nombre de pannes.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X \ge 7)$, la probabilité que le service tienne | un nombre (4 décimales) |
| b | $P(X = 7)$ | un nombre (4 décimales) |
| c | $\mathbb{E}[F]$ | un nombre |
| d | $P(F \ge 3)$, la probabilité que le service tombe | un nombre (4 décimales) |
| e | la borne de Chernoff de $P(F \ge 3)$ : $e^{-9\,\mathrm{KL}(1/3 \Vert 0{,}1)}$ | un nombre (4 décimales) |
| f | la borne de Hoeffding de $P(F \ge 3)$ : $e^{-2 \times 9 \times (1/3 - 0{,}1)^2}$ | un nombre (4 décimales) |
| g | la borne de Markov de $P(F \ge 3)$ | un nombre (4 décimales) |
| h | la probabilité que le service tienne avec 12 machines, s'il en faut au moins 10 | un nombre (4 décimales) |

Dans ta copie : écris la somme de a) terme à terme. Pourquoi $F$ suit-il la loi $\mathcal{B}(9 ;\ 0{,}1)$ ? Range les trois bornes de la meilleure à la moins bonne, et dis pourquoi aucune n'est proche de d) pour $n = 9$. Avec 12 machines et toujours 2 machines de réserve, le service est-il plus ou moins fiable ? Pourquoi ? Vérifie a) avec `testing.binomial_test` de M08.

### Ex M14.2 — La variance de la moyenne de trois mesures corrélées, par la matrice de covariance ✏️ ★ ⏱️ 15 min
**Objectif :** calculer la variance d'une moyenne pondérée de variables corrélées par $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$, et trouver les meilleurs poids.
**Prérequis :** fiche §2 ; M02c ; M13b · **Parcours :** C, E

Trois instruments mesurent la même masse. Leurs erreurs ont la matrice de covariance
$$\boldsymbol{\Sigma} = \begin{pmatrix} 3 & 1 & -1 \\ 1 & 5 & -1 \\ -1 & -1 & 2 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la variance de la moyenne simple des trois mesures | une fraction |
| b | ce qu'on trouverait en oubliant les covariances | une fraction |
| c | la variance de la moyenne pondérée de poids $\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{2}\right)$ | une fraction |
| d | les poids $\mathbf{w}^* \propto \boldsymbol{\Sigma}^{-1}\mathbf{1}$, de somme 1, qui minimisent la variance | une liste de 3 fractions |
| e | la variance minimale | une fraction |
| f | la corrélation des erreurs des instruments 1 et 2 | un nombre (4 décimales) |

Dans ta copie : écris $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ comme une somme de 9 termes pour c). Pourquoi a) est-il plus petit que b) ? Retrouve $\mathbf{w}^* \propto \boldsymbol{\Sigma}^{-1}\mathbf{1}$ par le lagrangien de $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ sous $\sum_i w_i = 1$ (M13b), et vérifie que e) $= \frac{1}{\mathbf{1}^\top\boldsymbol{\Sigma}^{-1}\mathbf{1}}$. Pourquoi e) est-il plus petit que la variance du meilleur instrument seul ?

### Ex M14.3 — (1 + x/n)ⁿ pour quelques n, et des intérêts composés en continu ✏️ ★ ⏱️ 10 min
**Objectif :** calculer $(1 + x/n)^n$, le comparer à $e^x$, et estimer l'erreur par $-\frac{x^2}{2n}$.
**Prérequis :** fiche §3 · **Parcours :** C, E

Un placement rapporte 6,5 % par an, pendant 6 ans. Si les intérêts sont versés $m$ fois par an (chaque fois $\frac{6{,}5}{m}$ %), le capital est multiplié en 6 ans par $\left(1 + \frac{0{,}065}{m}\right)^{6m}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le facteur sur 6 ans avec un versement par an | un nombre (6 décimales) |
| b | le même avec un versement par trimestre | un nombre (6 décimales) |
| c | le même avec un versement par semaine (52 par an) | un nombre (6 décimales) |
| d | la limite du facteur quand le nombre de versements tend vers l'infini | un nombre (6 décimales) |
| e | l'erreur relative de b) par rapport à d) | un nombre (6 décimales) |
| f | l'erreur relative prévue par l'approximation $-\frac{x^2}{2N}$ pour b), avec le bon $x$ et le bon $N$ | un nombre (6 décimales) |
| g | l'erreur relative de $\left(1 + \frac{3}{30}\right)^{30}$ par rapport à $e^3$ | un nombre (4 décimales) |
| h | le plus petit $n$ pour lequel l'approximation $-\frac{x^2}{2n}$ annonce une erreur de moins de 1 % en valeur absolue, pour $x = 3$ | un entier |

Dans ta copie : montre que les quatre facteurs s'écrivent $\left(1 + \frac{x}{N}\right)^N$ avec le même $x$ ; que valent $x$ et les quatre $N$ ? Pourquoi a), b) et c) sont-ils rangés dans cet ordre, et tous plus petits que d) ? Compare e) et f). Pour g), compare à $-\frac{x^2}{2n}$ : pourquoi l'approximation est-elle bien moins bonne qu'en e) et f) ?

### Ex M14.4 — Les poids exponentiels de cinq experts après trois tours ✏️ ★ ⏱️ 15 min
**Objectif :** calculer les poids de Hedge à la main, la loss de l'algorithme, son regret et la borne de regret.
**Prérequis :** fiche §4 · **Parcours :** C, E

Cinq experts, $\eta = \ln 3$ (le poids est donc proportionnel à $3^{-L}$), et leurs losses sur trois tours :

| tour | expert 1 | expert 2 | expert 3 | expert 4 | expert 5 |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 1 | 0 | 1 |
| 2 | 1 | 0 | 1 | 0 | 0 |
| 3 | 0 | 1 | 0 | 1 | 0 |

| | Question | Réponse attendue |
|---|---|---|
| a | les poids avant le tour 2 | une liste de 5 fractions |
| b | les poids avant le tour 3 | une liste de 5 fractions |
| c | les poids après le tour 3 | une liste de 5 fractions |
| d | la loss totale de l'algorithme, $\sum_t \mathbf{w}_t \cdot \boldsymbol{\ell}_t$ | une fraction |
| e | la loss totale du meilleur expert | un entier |
| f | le regret | un nombre (4 décimales) |
| g | la borne $\frac{\ln K}{\eta} + \frac{\eta T}{8}$ | un nombre (3 décimales) |
| h | le $\eta$ qui rend cette borne la plus petite pour $K = 5$ et $T = 3$ | un nombre (4 décimales) |

Dans ta copie : écris, pour chaque tour, les losses cumulées et les puissances de 3 avant de normaliser. Quels experts sont les meilleurs à la fin ? Pourquoi le regret est-il loin de la borne ici ? Que changerait le $\eta$ de h) sur les poids après trois tours ?

### Ex M14.5 — Le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport aux prédictions, et les poids exponentiels qu'il fait apparaître ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer le gradient d'une loss par rapport au vecteur des prédictions, et lire les poids qu'il donne aux exemples.
**Prérequis :** fiche §4 et §5 ; M09b · **Parcours :** C

Cinq exemples de classification, de labels $\mathbf{y} = (+1, +1, -1, -1, +1)$ et de scores $\mathbf{F} = (2 ;\ -0{,}5 ;\ -1{,}5 ;\ 0{,}3 ;\ 0)$, et la loss exponentielle $\mathcal{L}(\mathbf{F}) = \sum_i e^{-y_iF_i}$. Puis quatre exemples de régression, de cibles $(2{,}4 ;\ -0{,}5 ;\ 1 ;\ 5{,}8)$ et de prédictions $(1{,}9 ;\ 0{,}6 ;\ 1{,}3 ;\ 3{,}1)$, et la loss de Huber de seuil $\delta = 0{,}8$ sur les résidus $y_i - F_i$.

| | Question | Réponse attendue |
|---|---|---|
| a | les cinq marges $y_iF_i$ | une liste de 5 nombres |
| b | $\mathcal{L}(\mathbf{F})$ | un nombre (4 décimales) |
| c | le gradient $\nabla_{\mathbf{F}}\mathcal{L}$ | une liste de 5 nombres (4 décimales) |
| d | les poids $\frac{e^{-y_iF_i}}{\sum_j e^{-y_jF_j}}$ | une liste de 5 nombres (4 décimales) |
| e | le numéro de l'exemple de plus grand poids | un entier |
| f | le gradient de la loss de Huber par rapport aux quatre prédictions | une liste de 4 nombres |
| g | la loss de Huber totale | un nombre (4 décimales) |

Dans ta copie : pourquoi le gradient de la loss exponentielle a-t-il le signe de $-y_i$ ? Quel exemple pèse le plus, et pourquoi ? Que deviendraient les poids de d) si l'on ajoutait 1 à toutes les marges ? Si l'on ajoute aux scores un modèle $h$ multiplié par $\alpha > 0$, par quoi le poids de l'exemple $i$ est-il multiplié avant la renormalisation (réponds en lettres) ? Pour Huber, quels exemples ont un gradient « coupé », et qu'est-ce que cela change pour un point aberrant ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M14.6 — (1 + x/n)ⁿ → eˣ, par le logarithme et ln(1 + u) ≈ u ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la limite $(1 + x/n)^n \to e^x$ pour tout réel $x$, en encadrant $\ln(1 + u)$.
**Prérequis :** fiche §3 ; M05a · **Parcours :** C, E

∂ M02b.13 a montré $\left(1 - \frac{\lambda}{n}\right)^n \to e^{-\lambda}$ par le logarithme et $\frac{\ln(1 + h)}{h} \to 1$. Ici, un **encadrement** de $\ln(1 + u)$ donne la limite pour tout $x$, et en plus la vitesse et le sens de variation. On utilise $\ln(1 + u) \le u$ pour tout $u > -1$ : c'est $e^v \ge 1 + v$ (CP1.9 B), avec $v = \ln(1 + u)$.
1. Montre que, pour tout $u \ge 0$, $\ln(1 + u) \ge u - \frac{u^2}{2}$ (étudie la différence et sa dérivée).
2. Montre que, pour $-\frac{1}{2} \le u \le 0$, $\ln(1 + u) \ge u - u^2$.
3. Soit $x$ un réel et $n > 2\lvert x \rvert$. Avec $u = \frac{x}{n}$, encadre $n\ln\left(1 + \frac{x}{n}\right)$ entre $x - \frac{x^2}{n}$ et $x$, puis conclus : $\left(1 + \frac{x}{n}\right)^n \to e^x$. Quelle propriété de l'exponentielle utilises-tu ?
4. **La vitesse.** Pour $x \ge 0$ et $n \ge 1$, déduis de 1 que $-\frac{x^2}{2n} \le \frac{(1 + x/n)^n}{e^x} - 1 \le 0$ (utilise $e^{-v} \ge 1 - v$). Que dit cet encadrement de l'erreur relative, et du $n$ qu'il faut pour une précision donnée ?
5. **Le sens de variation.** Pour $x > 0$, on pose $\varphi(t) = t\ln\left(1 + \frac{x}{t}\right)$ pour $t > 0$. Montre que $\varphi'(t) = \ln(1 + v) - \frac{v}{1 + v}$ avec $v = \frac{x}{t}$, puis que $\varphi'(t) \ge 0$ (applique $\ln(1 + u) \le u$ à $u = -\frac{v}{1 + v}$). Conclus : $n \mapsto \left(1 + \frac{x}{n}\right)^n$ est croissante.

### Ex M14.7 — Une moyenne pondérée de variables de variance σ² a une variance au plus σ² ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer qu'une moyenne pondérée ne fait jamais pire que la pire de ses variables, avec l'inégalité $\lvert\operatorname{Cov}(X, Y)\rvert \le \sigma_X\sigma_Y$.
**Prérequis :** fiche §2 ; M02c ; M07 · **Parcours :** C

$X_1, \ldots, X_M$ ont chacune une variance au plus $\sigma^2$ ; $w_1, \ldots, w_M \ge 0$ et $\sum_i w_i = 1$.
1. Montre que $\lvert\operatorname{Cov}(X, Y)\rvert \le \sqrt{\mathbb{V}(X)\,\mathbb{V}(Y)}$ (regarde $\mathbb{V}(X - tY)$ comme un polynôme du second degré en $t$, toujours positif ou nul).
2. Déduis-en $\operatorname{Cov}(X_i, X_j) \le \sigma^2$ pour tous $i, j$.
3. Avec $\sigma_i^2 = \mathbb{V}(X_i)$, montre que $\mathbb{V}\big(\sum_i w_iX_i\big) \le \big(\sum_i w_i\sigma_i\big)^2$, puis que cette quantité est au plus $\sigma^2$.
4. Quand y a-t-il égalité ? Donne un exemple où elle est atteinte avec $M = 2$ et des poids non nuls.
5. Montre par un exemple que la conclusion devient fausse si l'on autorise des poids négatifs (de somme 1).

### Ex M14.8 — La borne de Chernoff d'une queue binomiale : le meilleur λ donne exp(−n KL(a ‖ p)) ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer la borne de Chernoff d'une loi binomiale, de Markov au meilleur $\lambda$, et la comparer à Hoeffding.
**Prérequis :** fiche §1 ; M06 ; M11 · **Parcours :** C

$X$ suit la loi $\mathcal{B}(n, p)$ avec $0 < p < 1$, et $p < a < 1$.
1. Pour $\lambda > 0$, montre que $P(X \ge na) \le e^{-\lambda na}\,\mathbb{E}\big[e^{\lambda X}\big]$, en nommant l'inégalité utilisée et en justifiant qu'elle s'applique.
2. Montre que $\mathbb{E}\big[e^{\lambda X}\big] = (1 - p + pe^\lambda)^n$ ; dis où sert l'indépendance.
3. Soit $g(\lambda) = -\lambda a + \ln(1 - p + pe^\lambda)$. Montre que $g$ atteint son minimum sur $]0, +\infty[$ en $\lambda^*$ tel que $e^{\lambda^*} = \frac{a(1 - p)}{p(1 - a)}$, et vérifie que $\lambda^* > 0$.
4. Montre que $g(\lambda^*) = -\mathrm{KL}(a \Vert p)$, et conclus : $P(X \ge na) \le e^{-n\,\mathrm{KL}(a \Vert p)}$.
5. Pour $a = 1$, la formule de 3 ne s'applique plus. Montre directement que $P(X \ge n) = p^n = e^{-n\,\mathrm{KL}(1 \Vert p)}$ (avec $0\ln 0 = 0$) : la borne est alors exacte.
6. **Chernoff contre Hoeffding.** $p$ est fixé. Pour $a \in\ ]0, 1[$, on pose $f(a) = \mathrm{KL}(a \Vert p) - 2(a - p)^2$. Calcule $f(p)$, $f'(p)$ et $f''(a)$, montre que $f'' \ge 0$, et conclus : $\mathrm{KL}(a \Vert p) \ge 2(a - p)^2$ (l'inégalité de Pinsker, pour deux lois de Bernoulli). Qu'en déduis-tu sur les bornes de Chernoff et de Hoeffding de $P(X \ge na)$ ?

CP2.9 B a fait les questions 1 à 4 dans un cas particulier : tu les fais ici pour tous $p$ et $a$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M14.9 — Pont : ajouter des modèles très corrélés ne sert presque à rien, un plancher de variance sur deux groupes de modèles 🔗 ★ ⏱️ 15 min
**Objectif :** calculer la variance de la moyenne de modèles qui forment deux groupes corrélés, son plancher, et ce que le mélange des deux groupes rapporte.
**Prérequis :** fiche §2 · **Parcours :** C, E

On moyenne des modèles de régression de deux familles. Pour un exemple donné, l'erreur d'un modèle du groupe A vaut $Z_A + E_i$, celle d'un modèle du groupe B, $Z_B + E_i$ : $Z_A$ et $Z_B$ sont les parts communes à chaque groupe, avec $\mathbb{V}(Z_A) = 0{,}8$, $\mathbb{V}(Z_B) = 1{,}2$ et $\operatorname{Cov}(Z_A, Z_B) = 0{,}4$ ; les $E_i$ sont les parts propres, indépendantes de tout le reste, de variance 3 chacune.

| | Question | Réponse attendue |
|---|---|---|
| a | la variance de la moyenne simple de 10 modèles, 5 de chaque groupe | une fraction |
| b | le plancher : la limite de cette variance avec $m$ modèles de chaque groupe, quand $m \to \infty$ | une fraction |
| c | le plus petit $m$ (modèles par groupe) pour que la variance dépasse le plancher d'au plus $0{,}04$ | un entier |
| d | le plancher si l'on ne garde que des modèles du groupe A | une fraction |
| e | la proportion $\alpha$ de modèles du groupe A qui donne le plus petit plancher, quand les deux groupes ont beaucoup de modèles | une fraction |
| f | ce plus petit plancher | une fraction |
| g | la variance de la moyenne de 10 modèles du groupe A seulement | une fraction |
| h | tu as 100 modèles du groupe A et tu en ajoutes 10 du groupe B : la variance de la moyenne des 110 | une fraction |

Dans ta copie : écris la moyenne des $2m$ modèles comme $\frac{Z_A + Z_B}{2} + \frac{1}{2m}\sum_i E_i$, et déduis-en a) et b). Pourquoi g) est-il plus grand que a), à nombre de modèles égal ? Pourquoi mélanger deux groupes baisse-t-il le plancher, même si le groupe B est moins bon seul ? Pour h), compare à la variance de la moyenne de 110 modèles du groupe A : lequel des deux ajouts vaut mieux, et pourquoi ? Quelle est la corrélation entre deux modèles du groupe A ?

### Ex M14.10 — Expliquer pourquoi une moyenne réduit la variance, et quand elle ne la réduit plus 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, sans formule, ce que moyenner des prédictions gagne et ce que leur corrélation lui reprend.
**Prérequis :** fiche §2 · **Parcours :** C, E

Une collègue te dit : « Un thermomètre de la salle serveur a une erreur de variance 4. Avec cent thermomètres du même modèle, la moyenne aura une erreur de variance 0,04, non ? » Réponds-lui en 6 à 10 phrases, sans formule, en t'appuyant sur quatre idées : ce qui se compense quand on moyenne (le bruit propre à chaque appareil) ; ce qui ne se compense pas (une erreur que tous partagent : le même étalonnage d'usine, la même bouche de ventilation) ; ce que changent des appareils de conceptions différentes, ou des erreurs qui vont en sens opposés ; ce que des poids inégaux peuvent apporter. Termine par le lien avec des modèles d'apprentissage entraînés sur les mêmes données. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M14.E1 — « Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est le meilleur ? » 💼 ★ ⏱️ 10 min
*Fiche §4 · parcours C*

« Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est le meilleur ? »

Prépare une réponse orale de **60 secondes**. Elle doit décrire le cadre (des experts, des losses révélées tour après tour, aucune hypothèse sur leur origine), pourquoi suivre simplement l'expert en tête jusqu'ici peut mal finir, l'algorithme des poids exponentiels et sa mise à jour multiplicative, ce que mesure le regret et ce que Hedge garantit (un regret en $\sqrt{T\ln K}$, donc un regret moyen qui tend vers 0), le rôle du learning rate et comment le régler sans connaître l'horizon, la différence avec un bandit (M11), et un usage concret. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m14_ensembles/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M14.11 | La borne de Chernoff et la variance d'une moyenne pondérée · `chernoff_bound, variance_of_average` | 🔨 | ★ | 20 | C, E |
| M14.12 | Les poids de l'algorithme Hedge · `hedge_weights` | 🔨 | ★ | 15 | C |
| M14.13 | Simuler la moyenne de deux groupes de modèles corrélés, et retrouver aᵀΣa et son plancher | 🔬 | ★★ | 20 | C, E |
| M14.14 | Les poids exponentiels au fil des tours : quel expert domine, selon le learning rate | 🎨 | ★ | 15 | C |
| M14.15 | Chasse à l'erreur : P(X ≥ k) calculée comme P(X > k), des covariances oubliées, des poids non renormalisés | 🐛 | ★ | 15 | C |
| M14.16 | Un test qui vérifie que la borne de Chernoff majore la queue exacte de `scipy.stats`, sur une grille de n, p et a | 🛠️ | ★ | 15 | C |
| M14.17 | Défi : suivre le meilleur de dix experts avec Hedge sans connaître l'horizon, un regret sous la borne théorique sur 1 000 tours | 🏆 | ★★★ | 25 | C |
