# M25b · Variables latentes et ELBO — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m25b_variables_latentes/06_mes_reponses.md` (créée par `python tools/start_chapter.py M25b`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [📖 🗣️ 🔗 Lecture, explication et pont](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les vecteurs sont des **colonnes** ; un mélange de $K$ gaussiennes a pour poids $\pi_k$, moyennes $\boldsymbol{\mu}_k$ et covariances $\boldsymbol{\Sigma}_k$ ; $r_{ik}$ est la responsabilité de la composante $k$ pour la donnée $i$, et $N_k = \sum_i r_{ik}$ ; $\ell(\boldsymbol{\theta})$ est la log-vraisemblance ; $\operatorname{ELBO}(q) = \mathbb{E}_q[\ln p(\mathbf{x}, \mathbf{z}) - \ln q(\mathbf{z})]$ ; $\mathrm{KL}(p \,\|\, q) = \mathbb{E}_p[\ln p - \ln q]$, en nats ; $\ln$ est le logarithme népérien ; $\mathcal{N}(c \mid \mu, \sigma^2)$ est la densité de $\mathcal{N}(\mu, \sigma^2)$ en $c$, et $\mathcal{N}(\mu, \sigma^2)$ a pour second paramètre une **variance** ; les angles principaux s'écrivent $\phi_i$. ACP probabiliste : $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_k)$, $\mathbf{x} = \mathbf{W}\mathbf{z} + \boldsymbol{\mu} + \boldsymbol{\varepsilon}$, $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \sigma^2\mathbf{I}_d)$, $\mathbf{C} = \mathbf{W}\mathbf{W}^\top + \sigma^2\mathbf{I}_d$ et $\mathbf{M} = \mathbf{W}^\top\mathbf{W} + \sigma^2\mathbf{I}_k$. Dans le notebook, les données sont les **lignes** d'un tableau de forme $(n, d)$ (des mesures en dimension 1 forment une colonne $(n, 1)$), une matrice s'écrit comme la liste de ses lignes, et les covariances d'un mélange forment un tableau $(K, d, d)$.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, dans la durée indiquée pour chacun (4 ou 5 minutes). Réponds vite, puis vérifie dans `05_solutions.md`.

### M25b.Q1 — Lire un graphe orienté : factoriser la loi jointe, l'ordre d'un tirage ancestral, et les variables qui deviennent dépendantes quand on observe leur effet commun 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Un drone de livraison : la force du vent $V$ et la charge transportée $C$ fixent la consommation de la batterie $B$ pendant le vol, et $B$ fixe l'autonomie restante $A$ affichée à l'arrivée. Le graphe est $V \to B \leftarrow C$ et $B \to A$.

1. Écris la loi jointe $p(V, C, B, A)$ selon le graphe.
2. Donne un ordre de tirage ancestral.
3. Vrai ou faux : $V$ et $C$ sont indépendantes quand on n'observe rien.
4. Vrai ou faux : $V$ et $C$ restent indépendantes quand on observe $B$.
5. Vrai ou faux : $V$ et $C$ restent indépendantes quand on observe seulement $A$.
6. Vrai ou faux : $V$ et $A$ sont indépendantes sachant $B$.

### M25b.Q2 — Marginaliser ou conditionner : vraisemblance marginale, posterior d'un latent, moyenne et variance d'un mélange 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

$X$ suit le mélange $\frac12\,\mathcal{N}(3, 2) + \frac12\,\mathcal{N}(11, 2)$, de latent $Z \in \{1, 2\}$.

1. $\mathbb{E}[X]$ ?
2. $\mathbb{V}(X)$ ?
3. Vrai ou faux : $\mathbb{V}(X)$ est la moyenne des variances des deux composantes.
4. En un point $x$, les deux densités valent $p(x \mid Z = 1) = 0{,}05$ et $p(x \mid Z = 2) = 0{,}15$. Que valent $p(x)$ et $P(Z = 1 \mid x)$ ?
5. Vrai ou faux : $\mathbb{E}[X \mid Z]$ est une variable aléatoire, qui vaut 3 ou 11.
6. Vrai ou faux : $X$ a la loi de $\frac12X_1 + \frac12X_2$, avec $X_1 \sim \mathcal{N}(3, 2)$ et $X_2 \sim \mathcal{N}(11, 2)$ indépendantes.

### M25b.Q3 — Un mélange de gaussiennes : responsabilités, logarithme d'une somme, vraisemblance infinie et composantes renumérotées 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Pour une donnée, $a_{i1} = -3$ et $a_{i2} = -3 - \ln 3$. Que vaut $r_{i1}$ ?
2. Que vaut $\ln p(\mathbf{x}_i)$ ?
3. Vrai ou faux : $\ln\sum_k\pi_k\,\mathcal{N}(\mathbf{x}_i \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k) = \sum_k\ln\big(\pi_k\,\mathcal{N}(\mathbf{x}_i \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)\big)$.
4. Un maximum à 3 composantes distinctes : combien de numérotations donnent la même loi ?
5. Vrai ou faux : avec $K \ge 2$, une composante centrée sur une donnée, dont la variance tend vers 0, fait tendre $\ell$ vers $+\infty$.
6. Vrai ou faux : pour une seule gaussienne ($K = 1$) et au moins deux données distinctes en dimension 1, la log-vraisemblance est bornée.

### M25b.Q4 — L'EM : ce que font le pas E et le pas M, ce qui ne baisse jamais, ce qui n'est pas garanti, et k-means comme limite 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Que calcule le pas E, en une phrase ?
2. $n = 10$ données, et le pas E donne $N_1 = 3{,}2$ et $N_2 = 6{,}8$. Les poids après le pas M ?
3. Vrai ou faux : sans régularisation, $\ell(\boldsymbol{\theta}_{t+1}) \ge \ell(\boldsymbol{\theta}_t)$ à chaque itération.
4. Vrai ou faux : l'EM converge vers le maximum global de $\ell$.
5. Vrai ou faux : avec `reg > 0`, $\ell$ ne baisse jamais.
6. Poids égaux, centres 0 et 10, covariances $\gamma\mathbf{I}$ : vers quoi tend la responsabilité du centre 0 pour la donnée $x = 4$ quand $\gamma \to 0$ ?

### M25b.Q5 — L'ELBO : une borne de quoi, une égalité quand, un écart égal à quelle KL ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. $\operatorname{ELBO}(q)$ est toujours au plus égale à quoi ?
2. Pour quelle loi $q$ y a-t-il égalité ?
3. L'écart $\ln p(\mathbf{x}) - \operatorname{ELBO}(q)$ est une KL : laquelle (attention à l'ordre) ?
4. $\ln p(\mathbf{x}) = -2{,}3$ et $\operatorname{ELBO}(q) = -2{,}9$ : que vaut cette KL ?
5. Vrai ou faux : $\operatorname{ELBO}(q) = \mathbb{E}_q[\ln p(\mathbf{x} \mid \mathbf{z})] - \mathrm{KL}(q \,\|\, p(\mathbf{z}))$.
6. Vrai ou faux : maximiser l'ELBO sur une famille de lois $q$ revient à y minimiser $\mathrm{KL}(q \,\|\, p(\mathbf{z} \mid \mathbf{x}))$.

### M25b.Q6 — L'ACP probabiliste : covariance marginale, rotation de W, angles principaux et directions éteintes 🧠 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

1. $k = 1$, $\mathbf{w} = (1, 2, 2)$ et $\sigma^2 = 0{,}5$ : que valent $C_{11}$ et $C_{23}$ ?
2. Les valeurs propres de ce $\mathbf{C}$ ?
3. Vrai ou faux : $\mathbf{W}$ et $-\mathbf{W}$ donnent la même loi de $\mathbf{x}$.
4. Une droite $D$ et un plan $P$ de $\mathbb{R}^4$ passent par l'origine, et leur angle principal est nul. Que peut-on en dire ?
5. Bruit connu $\sigma^2 = 4$, $k = 2$, valeurs propres des données 10 et 3 : les carrés des normes des deux colonnes de $\hat{\mathbf{W}}$ (avant la rotation) ?
6. Vrai ou faux : les valeurs singulières de $\mathbf{Q}_A^\top\mathbf{Q}_B$ sont les angles principaux.

### M25b.Q7 — KL directe ou inverse, inférence amortie et écart d'amortissement, et dériver sous l'espérance : quand le peut-on ? 🧠 ★ ⏱️ 5 min
*Fiche §7 · parcours C, E*

1. $p$ a deux bosses bien séparées ; la gaussienne $q$ qui minimise $\mathrm{KL}(q \,\|\, p)$ se place (A) entre les bosses, (B) sur une bosse, (C) de façon à couvrir les deux ?
2. $p$ a pour moyenne 3 et pour variance 5 : quelle gaussienne minimise $\mathrm{KL}(p \,\|\, q)$ ?
3. Vrai ou faux : l'ELBO d'une règle amortie est au plus égale à la meilleure ELBO obtenue observation par observation.
4. Vrai ou faux : si la famille contient le posterior et que la règle amortie sait le représenter, les deux écarts sont nuls.
5. $X = \mu + \sigma\varepsilon$ et $f(x) = \mathbb{1}\{x > 2\}$ : la dérivée par le chemin donne 0, alors que $\frac{\mathrm{d}}{\mathrm{d}\mu}P(X > 2) > 0$. Quelle hypothèse du théorème de la fiche manque ?
6. Vrai ou faux : pour $f(x) = \max(x - 2, 0)$, qui a un coin en 2, l'échange de la dérivée et de l'espérance reste permis (avec une domination).
7. Vrai ou faux : un estimateur sans biais à un tirage est précis.

### M25b.Q8 — Pondérer la KL : multiplicateur, information mutuelle, posterior agrégé et code effondré 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. Un budget d'information augmenté de 0,1 nat fait monter la meilleure reconstruction de 0,03. Que vaut, à peu près, le multiplicateur $\beta$ ?
2. Vrai ou faux : si $\mathbb{E}_{\mathbf{x}}\mathrm{KL}(q(\mathbf{z} \mid \mathbf{x}) \,\|\, p(\mathbf{z})) = 0$, alors $I(X ; Z) = 0$.
3. La KL moyenne au prior vaut 0,40 nat et $I(X ; Z) = 0{,}25$ nat : que vaut $\mathrm{KL}(q(\mathbf{z}) \,\|\, p(\mathbf{z}))$ ?
4. Avec une reconstruction gaussienne, le couple ($\sigma^2 = 2$, $\beta = 0{,}6$) équivaut au couple ($\sigma^2 = 0{,}4$, $\beta = ?$).
5. Vrai ou faux : le posterior agrégé est toujours égal au prior.
6. Vrai ou faux : un $\beta$ plus grand pousse vers un code effondré.

<a id="rappels"></a>

## 🔁 Rappels

### M25b.R1 — Bayes sur une variable cachée et log-sum-exp : probabilités totales, posterior, et une somme d'exponentielles sans dépassement (M04, M05a) 🔁 ★ ⏱️ 6 min
*Fiche §2 et §3 · parcours C, E*

1. Trois lignes de montage produisent 55 %, 30 % et 15 % des pièces, avec des taux de défaut de 2 %, 3 % et 6 %. La probabilité qu'une pièce soit défectueuse ?
2. Une pièce est défectueuse : la probabilité qu'elle vienne de la ligne 3 (fraction irréductible) ?
3. $\ln(e^{-800} + e^{-802})$, par le log-sum-exp (3 décimales) ?
4. Pourquoi le calcul direct de 3 en flottants donne-t-il $-\infty$ ?
5. Vrai ou faux : $\operatorname{LSE}(a_1 + c, \ldots, a_K + c) = \operatorname{LSE}(a_1, \ldots, a_K) + c$.
6. Vrai ou faux : $\max_k a_k \le \operatorname{LSE}(a_1, \ldots, a_K) \le \max_k a_k + \ln K$.

### M25b.R2 — L'inégalité de Jensen, la KL continue et l'information mutuelle (M06, M25a) 🔁 ★ ⏱️ 6 min
*Fiche §5 et §8 · parcours C, E*

1. $X$ vaut 2 ou 32 avec la probabilité $\frac12$. Compare $\ln\mathbb{E}[X]$ et $\mathbb{E}[\ln X]$ ; quelle inégalité illustre-t-on ?
2. $\mathrm{KL}\big(\mathcal{N}(2, 3) \,\|\, \mathcal{N}(5, 3)\big)$ ?
3. En une ligne : pourquoi l'inégalité de Jensen, appliquée au logarithme, donne-t-elle $\mathrm{KL}(p \,\|\, q) \ge 0$ pour deux densités $p$ et $q$ ?
4. Vrai ou faux : comme l'entropie de M06, l'entropie différentielle $h(X)$ d'une variable à densité est toujours positive ou nulle.
5. Que vaut $I(X ; Y)$ si $X$ et $Y$ sont indépendantes ?
6. Vrai ou faux : $I(X ; Y) = \mathrm{KL}\big(p(x, y) \,\|\, p(x)\,p(y)\big) = H(X) - H(X \mid Y)$ pour deux variables discrètes.

### M25b.R3 — La SVD, l'ACP et la projection orthogonale sur un sous-espace (M12b, M12d) 🔁 ★ ⏱️ 8 min
*Fiche §6 · parcours C, E*

1. La projection orthogonale de $(2, 1, 3)$ sur la droite dirigée par $(1, 1, 0)$ ?
2. Gram-Schmidt sur $(1, 1, 0)$ puis $(1, 0, 1)$ : la base orthonormée ?
3. $\mathbf{Q}$ a des colonnes orthonormées : la matrice de la projection orthogonale sur leur sous-espace ? Vrai ou faux : elle vérifie $\mathbf{P}^2 = \mathbf{P}$.
4. Une covariance a pour valeurs propres 8, 3 et 1 : la part de la variance gardée par les deux premiers axes de l'ACP ?
5. $\mathbf{X}$ centrée, de forme $(n, d)$, a pour SVD $\mathbf{U}\mathbf{S}\mathbf{V}^\top$ : où lit-on les axes principaux, et les variances qu'ils portent ?
6. Vrai ou faux : les valeurs singulières d'une matrice carrée sont les valeurs absolues de ses valeurs propres.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- une valeur exacte entre guillemets, écrite avec des entiers, des fractions, `sqrt`, `pi`, `ln` et `exp`, comme `"ln(5/2)"` ;
- une forme comme NumPy l'affiche, comme `(7, 2)` ;
- `True` ou `False` pour un vrai ou faux.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M25b.1 — Trois machines produisent des pièces de longueurs gaussiennes : le graphe, la loi jointe, un tirage ancestral à la main, la vraisemblance marginale d'une longueur et le posterior de la machine ✏️ ★★ ⏱️ 25 min
**Objectif :** écrire un modèle à variable latente discrète, en tirer un échantillon ancestral, puis l'inverser par la règle de Bayes.
**Prérequis :** fiche §1 et §2 ; M04 · **Parcours :** C, E

Un atelier coupe des tiges sur trois machines. Une tige vient de la machine $z \in \{1, 2, 3\}$ avec les probabilités $\boldsymbol{\pi} = (0{,}5 ;\ 0{,}3 ;\ 0{,}2)$ ; sachant $z$, sa longueur $x$ (en mm) suit $\mathcal{N}(\mu_z, \sigma_z^2)$, avec les moyennes $\boldsymbol{\mu} = (100 ;\ 102 ;\ 97)$ et les **écarts-types** $(\sigma_1, \sigma_2, \sigma_3) = (1 ;\ 1 ;\ 2)$. Pour tirer une machine avec un nombre $u$ uniforme sur $[0, 1[$ : machine 1 si $u < 0{,}5$, machine 2 si $0{,}5 \le u < 0{,}8$, machine 3 sinon. Une tige mesurée vaut $x = 98{,}2$ mm.

| | Question | Réponse attendue |
|---|---|---|
| a | le tirage ancestral fait avec $u = 0{,}62$, puis le tirage $\varepsilon = -1{,}3$ de $\mathcal{N}(0, 1)$ : le numéro de la machine, puis la longueur (mm) | une liste de 2 nombres |
| b | la densité de la longueur en 98,2 mm, $p(98{,}2)$ (par mm) | un nombre (4 décimales) |
| c | les probabilités a posteriori $P(z = k \mid x = 98{,}2)$, dans l'ordre des machines | une liste de 3 nombres (3 décimales) |
| d | le numéro de la machine la plus probable pour cette tige | un entier |
| e | vrai ou faux : la machine dont la moyenne est la plus proche de 98,2 mm est la plus probable | `True` ou `False` |
| f | si les trois machines produisaient chacune un tiers des tiges : $P(z = 3 \mid x = 98{,}2)$ | un nombre (4 décimales) |

Dans ta copie : dessine le graphe du modèle pour $n$ tiges (un cadre), écris la loi jointe $p(x, z)$ et donne la valeur de $p(x = 98{,}2,\ z = 1)$. Explique en deux phrases pourquoi c) et f) ne donnent pas la même machine.

### Ex M25b.2 — Deux variétés de grains de café (longueur, largeur) : moyenne et covariance du mélange par la variance totale, part de la variance entre variétés, et une corrélation qu'aucune variété n'a ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer la moyenne et la covariance d'un mélange en dimension 2 par les lois de l'espérance et de la variance totales, et voir une corrélation naître du mélange.
**Prérequis :** fiche §2 ; M12c · **Parcours :** C, E

Un sac contient deux variétés de grains de café : 60 % de la variété 1, 40 % de la variété 2. Pour un grain, $\mathbf{x} = (\text{longueur}, \text{largeur})$, en mm. Dans chaque variété, $\mathbf{x}$ suit une loi de moyenne et de covariance
$$\boldsymbol{\mu}_1 = \begin{pmatrix} 11 \\ 7 \end{pmatrix},\ \ \boldsymbol{\Sigma}_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0{,}4 \end{pmatrix} ; \qquad \boldsymbol{\mu}_2 = \begin{pmatrix} 13 \\ 8 \end{pmatrix},\ \ \boldsymbol{\Sigma}_2 = \begin{pmatrix} 1{,}5 & 0 \\ 0 & 0{,}3 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne $\boldsymbol{\mu}$ du mélange | une liste de 2 nombres |
| b | la covariance moyenne dans les variétés, $\sum_k\pi_k\boldsymbol{\Sigma}_k$ | une matrice $2 \times 2$ |
| c | la covariance entre les variétés, $\sum_k\pi_k(\boldsymbol{\mu}_k - \boldsymbol{\mu})(\boldsymbol{\mu}_k - \boldsymbol{\mu})^\top$ | une matrice $2 \times 2$ |
| d | la covariance $\boldsymbol{\Sigma}$ du mélange | une matrice $2 \times 2$ |
| e | la part de la variance de la longueur qui vient de l'écart entre les variétés | une fraction irréductible, entre guillemets |
| f | la corrélation de la longueur et de la largeur dans le sac | un nombre (4 décimales) |
| g | vrai ou faux : dans chaque variété, longueur et largeur sont décorrélées, et pourtant elles sont corrélées dans le sac | `True` ou `False` |

Dans ta copie : retrouve d) par la seconde forme, $\sum_k\pi_k(\boldsymbol{\Sigma}_k + \boldsymbol{\mu}_k\boldsymbol{\mu}_k^\top) - \boldsymbol{\mu}\boldsymbol{\mu}^\top$, et vérifie que c) vaut $\pi_1\pi_2(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2)(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2)^\top$. Pourquoi la corrélation est-elle positive ?

### Ex M25b.3 — Deux séries de résistances mélangées : les responsabilités de quatre mesures en log, un pas M (proportion, moyennes, variances), et la log-vraisemblance qui monte (suite de M13a, composantes inconnues) ✏️ ★★ ⏱️ 55 min
**Objectif :** faire une itération complète de l'EM à la main, en log, et vérifier que la log-vraisemblance monte.
**Prérequis :** fiche §3 et §4 ; M05a, M13a · **Parcours :** C, E

Un bac mélange des résistances de deux séries, de valeurs nominales 47 Ω et 51 Ω, dans des proportions inconnues. On modélise la valeur mesurée par un mélange de deux gaussiennes et l'on part de $\boldsymbol{\pi} = (0{,}45 ;\ 0{,}55)$, $\boldsymbol{\mu} = (47 ;\ 51)$ Ω et des variances $(\sigma_1^2, \sigma_2^2) = (1 ;\ 2{,}5)$ Ω². Quatre mesures : $x = 46{,}0$ ; $48{,}0$ ; $49{,}4$ ; $52{,}1$ Ω. Calcule les $a_{ik} = \ln\pi_k + \ln\mathcal{N}(x_i \mid \mu_k, \sigma_k^2)$, puis tout le reste en log (fiche §3).

| | Question | Réponse attendue |
|---|---|---|
| a | les responsabilités $r_{i1}$ de la série 1 pour les quatre mesures, dans l'ordre des mesures | une liste de 4 nombres (4 décimales) |
| b | les poids $(\pi_1, \pi_2)$ après le pas M | une liste de 2 nombres (4 décimales) |
| c | les moyennes $(\mu_1, \mu_2)$ après le pas M (Ω) | une liste de 2 nombres (3 décimales) |
| d | les variances $(\sigma_1^2, \sigma_2^2)$ après le pas M (Ω²) | une liste de 2 nombres (3 décimales) |
| e | la log-vraisemblance $\ell$ des quatre mesures avec les paramètres de départ | un nombre (4 décimales) |
| f | la log-vraisemblance avec les paramètres après le pas M | un nombre (4 décimales) |
| g | vrai ou faux : f) est plus grand que e) | `True` ou `False` |

Dans ta copie : écris les huit $a_{ik}$ et les quatre $\operatorname{LSE}_k\,a_{ik}$ (4 décimales). Pourquoi la responsabilité de la série 1 pour 52,1 Ω est-elle presque nulle (de l'ordre de $10^{-6}$), et pas seulement petite ? Compare les écarts de 52,1 à 47 et à 51, en écarts-types de chaque série.

### Ex M25b.6 — Une sonde de qualité de l'eau, un état caché à deux valeurs et une mesure gaussienne : ln p(x), l'ELBO pour trois lois q, et l'écart égal à la KL au posterior ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer l'ELBO pour plusieurs lois $q$ d'un latent discret et vérifier l'identité $\ln p(x) = \operatorname{ELBO}(q) + \mathrm{KL}(q \,\|\, p(z \mid x))$.
**Prérequis :** fiche §5 ; M06 · **Parcours :** C, E

Une sonde mesure la turbidité $x$ d'une rivière, en NTU. L'eau est dans l'un de deux états cachés : conforme ($z = 1$, probabilité a priori 0,9) ou polluée ($z = 2$, probabilité 0,1). Sachant $z = 1$, $x \sim \mathcal{N}(1 ;\ 0{,}25)$ ; sachant $z = 2$, $x \sim \mathcal{N}(3 ;\ 1)$. La sonde lit $x = 2$ NTU.

| | Question | Réponse attendue |
|---|---|---|
| a | $\ln p(x = 2)$ | un nombre (4 décimales) |
| b | la probabilité a posteriori que l'eau soit polluée, $P(z = 2 \mid x = 2)$ | un nombre (3 décimales) |
| c | $\operatorname{ELBO}(q)$ pour $q = (0{,}5 ;\ 0{,}5)$ | un nombre (4 décimales) |
| d | $\operatorname{ELBO}(q)$ pour $q = (0{,}6 ;\ 0{,}4)$, avec $q(z = 1) = 0{,}6$ | un nombre (4 décimales) |
| e | $\operatorname{ELBO}(q)$ quand $q$ est le posterior | un nombre (4 décimales) |
| f | $\mathrm{KL}\big(q \,\|\, p(z \mid x = 2)\big)$ pour $q = (0{,}5 ;\ 0{,}5)$, calculée par sa définition | un nombre (4 décimales) |
| g | vrai ou faux : c) + f) = a) | `True` ou `False` |

Dans ta copie : pourquoi l'ELBO de d) dépasse-t-elle celle de c) ? Laquelle des trois lois $q$ est la plus proche du prior, et cela l'aide-t-il ?

### Ex M25b.9 — Trois épreuves d'un concours expliquées par une aptitude cachée : covariance marginale, posterior d'un candidat (une règle affine des notes), et maximum de vraisemblance à partir de valeurs propres données, dont une direction éteinte ✏️ ★★ ⏱️ 35 min
**Objectif :** appliquer l'ACP probabiliste à un facteur : loi marginale, posterior exact, et maximum de vraisemblance de Tipping et Bishop, avec un bruit estimé puis connu.
**Prérequis :** fiche §6 et §7 ; M12c, M25a · **Parcours :** C, E

Un concours a trois épreuves, notées sur 20. On modélise les notes $\mathbf{x} \in \mathbb{R}^3$ d'un candidat par l'ACP probabiliste à un facteur ($k = 1$), son aptitude cachée $z \sim \mathcal{N}(0, 1)$ :
$$\mathbf{x} = \mathbf{w}\,z + \boldsymbol{\mu} + \boldsymbol{\varepsilon}, \qquad \mathbf{w} = \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix}, \quad \boldsymbol{\mu} = \begin{pmatrix} 12 \\ 11 \\ 13 \end{pmatrix}, \quad \boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, 3\,\mathbf{I}_3).$$
Pour les questions f) à i), une autre session du concours a donné une covariance des notes (au sens du maximum de vraisemblance) de valeurs propres $\lambda_1 = 14$, $\lambda_2 = 4{,}5$ et $\lambda_3 = 2{,}5$.

| | Question | Réponse attendue |
|---|---|---|
| a | la covariance marginale $\mathbf{C}$ des notes | une matrice $3 \times 3$ |
| b | $M = \mathbf{w}^\top\mathbf{w} + \sigma^2$ | un nombre |
| c | les trois coefficients $\mathbf{c}$ de la règle affine $\mathbb{E}[z \mid \mathbf{x}] = \mathbf{c}^\top(\mathbf{x} - \boldsymbol{\mu})$ | une liste de 3 nombres (4 décimales) |
| d | pour le candidat noté $(15, 12, 15)$ : la moyenne et la variance a posteriori de son aptitude | une liste de 2 nombres (4 décimales) |
| e | vrai ou faux : le candidat noté $(11, 11, 17)$ a la même variance a posteriori | `True` ou `False` |
| f | le maximum de vraisemblance à $k = 1$ : $\hat\sigma^2$ | un nombre |
| g | à $k = 1$ : $\lVert\hat{\mathbf{w}}\rVert^2$ | un nombre |
| h | si le bruit est **connu**, $\sigma^2 = 5$, avec $k = 2$ : les carrés des normes des deux colonnes de $\hat{\mathbf{W}}$ avant la rotation $\mathbf{R}$, dans l'ordre des valeurs propres | une liste de 2 nombres |
| i | vrai ou faux : dans h), la deuxième direction est éteinte | `True` ou `False` |

Dans ta copie : donne les valeurs propres de $\mathbf{C}$ et un vecteur propre de la plus grande. Pourquoi la règle de c) est-elle « amortie » : que coûte le posterior d'un nouveau candidat ? Dans h), quelles valeurs propres a la covariance du modèle ajusté ?

### Ex M25b.10 — Les angles principaux entre deux plans de ℝ⁴ et entre deux droites de ℝ³ : bases orthonormées, SVD de Q_Aᵀ Q_B, et pourquoi le résultat ne dépend pas des bases choisies ✏️ ★★ ⏱️ 40 min
**Objectif :** calculer des angles principaux par Gram-Schmidt et une SVD, et démontrer qu'ils ne dépendent pas des bases.
**Prérequis :** fiche §6 ; M12b, M12d · **Parcours :** C, E

Dans $\mathbb{R}^4$, le plan $A$ est engendré par $\mathbf{a}_1 = (1, 2, 0, 0)$ et $\mathbf{a}_2 = (2, 1, 0, 0)$, le plan $B$ par $\mathbf{b}_1 = (12, 0, 5, 0)$ et $\mathbf{b}_2 = (12, 7, 5, 24)$. On obtient $\mathbf{Q}_A$ par Gram-Schmidt sur $(\mathbf{a}_1, \mathbf{a}_2)$, dans cet ordre, et $\mathbf{Q}_B$ de même sur $(\mathbf{b}_1, \mathbf{b}_2)$. Dans $\mathbb{R}^3$, la droite $D_1$ est dirigée par $\mathbf{u} = (1, 4, 8)$ et la droite $D_2$ par $\mathbf{v} = (-4, -8, 1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{Q}_A$ | une matrice $4 \times 2$ (4 décimales) |
| b | $\mathbf{Q}_B$ | une matrice $4 \times 2$ (4 décimales) |
| c | $\mathbf{Q}_A^\top\mathbf{Q}_B$ | une matrice $2 \times 2$ (4 décimales) |
| d | ses valeurs singulières, de la plus grande à la plus petite | une liste de 2 nombres (4 décimales) |
| e | les angles principaux $\phi_1 \le \phi_2$ entre $A$ et $B$, en degrés | une liste de 2 nombres (2 décimales) |
| f | l'angle principal entre $D_1$ et $D_2$, en degrés | un nombre (2 décimales) |
| g | vrai ou faux : en divisant seulement $\mathbf{b}_1$ et $\mathbf{b}_2$ par leurs normes (sans Gram-Schmidt), on trouverait les mêmes valeurs singulières | `True` ou `False` |

Dans ta copie : montre que si $\mathbf{Q}_A' = \mathbf{Q}_A\mathbf{R}_A$ et $\mathbf{Q}_B' = \mathbf{Q}_B\mathbf{R}_B$ sont deux autres bases orthonormées ($\mathbf{R}_A$, $\mathbf{R}_B$ orthogonales), $\mathbf{Q}_A'^\top\mathbf{Q}_B'$ a les mêmes valeurs singulières que $\mathbf{Q}_A^\top\mathbf{Q}_B$. Pourquoi peut-on lire d) sans calculer de SVD complète (calcule $\mathbf{M}^\top\mathbf{M}$ pour $\mathbf{M} = \mathbf{Q}_A^\top\mathbf{Q}_B$) ?

### Ex M25b.12 — Le coût d'un stock c face à une demande gaussienne : E[(D − c)⁺], ses dérivées en μ et en σ par le chemin, puis par la formule fermée ✏️ ★★★ ⏱️ 45 min
**Objectif :** dériver une espérance par rapport aux paramètres de la loi par le chemin $D = \mu + \sigma\varepsilon$, sur une fonction seulement continue, et le vérifier par la formule fermée.
**Prérequis :** fiche §7 ; M02b, M19 · **Parcours :** C

Une boulangerie cuit chaque matin $c = 252$ baguettes. La demande du jour suit $D \sim \mathcal{N}(\mu, \sigma^2)$ avec $\mu = 240$ et $\sigma = 40$ baguettes ; on l'écrit $D = \mu + \sigma\varepsilon$, $\varepsilon \sim \mathcal{N}(0, 1)$. La demande non servie est $(D - c)^+ = \max(D - c, 0)$. On note $z = \frac{c - \mu}{\sigma} = 0{,}3$ et l'on donne $\varphi(0{,}3) \approx 0{,}381388$ (la densité de $\mathcal{N}(0, 1)$) et $\Phi(0{,}3) \approx 0{,}617911$.

| | Question | Réponse attendue |
|---|---|---|
| a | la demande non servie moyenne $\mathbb{E}[(D - c)^+]$ (baguettes) | un nombre (2 décimales) |
| b | $\frac{\partial}{\partial\mu}\mathbb{E}[(D - c)^+]$, par le chemin | un nombre (4 décimales) |
| c | $\frac{\partial}{\partial\sigma}\mathbb{E}[(D - c)^+]$, par le chemin | un nombre (4 décimales) |
| d | les estimations à un tirage des dérivées en $\mu$ puis en $\sigma$, pour le tirage $\varepsilon = 1{,}2$ | une liste de 2 nombres |
| e | les mêmes pour le tirage $\varepsilon = 0{,}1$ | une liste de 2 nombres |
| f | la variance de l'estimateur à un tirage de la dérivée en $\mu$ | un nombre (4 décimales) |
| g | $\frac{\partial}{\partial c}\mathbb{E}[(D - c)^+]$ | un nombre (4 décimales) |

Dans ta copie : établis la formule fermée $\mathbb{E}[(D - c)^+] = \sigma\varphi(z) - (c - \mu)(1 - \Phi(z))$ en intégrant sur $\{\varepsilon > z\}$. Dérive-la en $\mu$, puis en $\sigma$ (avec $\varphi'(z) = -z\varphi(z)$), et retrouve b) et c). Pourquoi l'échange de la dérivée et de l'espérance est-il permis ici, bien que $x \mapsto (x - c)^+$ ait un coin ?

### Ex M25b.13 — Une seule gaussienne pour la loi bimodale des temps de trajet par deux itinéraires : KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un itinéraire ✏️ ★★ ⏱️ 35 min
**Objectif :** voir sur un calcul ce que choisit chaque sens de la KL quand on approche une loi bimodale par une seule gaussienne.
**Prérequis :** fiche §2 et §7 ; M25a · **Parcours :** C, E

Une conductrice va au travail par la rocade (70 % des jours) ou par le centre-ville (30 %). Son temps de trajet, en minutes, suit le mélange
$$p = 0{,}7\,\mathcal{N}(22, 4) + 0{,}3\,\mathcal{N}(40 ;\ 6{,}25).$$
On l'approche par une seule gaussienne $q$. On note $q_1 = \mathcal{N}(22, 4)$, $q_2 = \mathcal{N}(40 ;\ 6{,}25)$, et $q_\star$ la gaussienne qui minimise $\mathrm{KL}(p \,\|\, q)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne et la variance de $p$ (qui sont celles de $q_\star$) | une liste de 2 nombres (valeurs exactes) |
| b | le rapport $\frac{q_\star(27{,}4)}{p(27{,}4)}$ des deux densités en 27,4 min | un nombre (2 décimales) |
| c | $\mathrm{KL}(q_1 \,\|\, p)$, en remplaçant sous $q_1$ la densité $p$ par $0{,}7\,q_1$ (l'autre bosse y est négligeable) | une valeur exacte, entre guillemets |
| d | $\mathrm{KL}(q_2 \,\|\, p)$, de même avec $0{,}3\,q_2$ | une valeur exacte, entre guillemets |
| e | le numéro de l'itinéraire (1 pour la rocade, 2 pour le centre-ville) où se pose le minimum global de $\mathrm{KL}(q \,\|\, p)$ | un entier |
| f | $\mathbb{E}_p[\ln q_1(X)]$ | un nombre (4 décimales) |
| g | $\mathbb{E}_p[\ln q_\star(X)]$ | un nombre (4 décimales) |
| h | vrai ou faux : $\mathrm{KL}(p \,\|\, q_1) - \mathrm{KL}(p \,\|\, q_\star) > 10$ | `True` ou `False` |

Dans ta copie : pourquoi $q_\star$ est-elle une mauvaise description des trajets (que dit b) ?), et pourquoi $q_1$ est-elle une très mauvaise approximation au sens de $\mathrm{KL}(p \,\|\, q)$ ? Pour f), sers-toi de $\mathbb{E}_p[(X - m)^2] = \mathbb{V}_p(X) + (\mathbb{E}_p[X] - m)^2$.

### Ex M25b.14 — Un code stochastique d'une source à trois symboles : posterior agrégé, information mutuelle, KL moyenne au prior décomposée en I(X ; Z) + KL(q(z) ‖ p(z)), puis le code qui s'effondre ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer, sur des tableaux, le posterior agrégé, l'information mutuelle d'un code, et la décomposition de la KL moyenne au prior.
**Prérequis :** fiche §8 ; M06 · **Parcours :** C, E

Une source émet les symboles $a$, $b$, $c$ avec les probabilités $p(x) = (0{,}5 ;\ 0{,}3 ;\ 0{,}2)$. Un code stochastique les transmet par $z \in \{1, 2\}$ selon
$$q(z \mid a) = (0{,}85 ;\ 0{,}15), \qquad q(z \mid b) = (0{,}35 ;\ 0{,}65), \qquad q(z \mid c) = (0{,}15 ;\ 0{,}85),$$
et le prior du code est $p(z) = (0{,}8 ;\ 0{,}2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le posterior agrégé $q(z) = \sum_xp(x)\,q(z \mid x)$ | une liste de 2 nombres (4 décimales) |
| b | les trois KL au prior $\mathrm{KL}(q(\cdot \mid x) \,\|\, p(z))$, pour $x = a$, $b$, $c$ dans cet ordre | une liste de 3 nombres (4 décimales) |
| c | la KL moyenne au prior, $\mathbb{E}_x\mathrm{KL}(q(\cdot \mid x) \,\|\, p(z))$ | un nombre (4 décimales) |
| d | l'information mutuelle $I(X ; Z)$ de la loi jointe $p(x)\,q(z \mid x)$, par sa définition | un nombre (4 décimales) |
| e | $\mathrm{KL}(q(z) \,\|\, p(z))$ | un nombre (4 décimales) |
| f | vrai ou faux : c) = d) + e) | `True` ou `False` |
| g | un code effondré rend $q(z \mid x) = p(z)$ pour les trois symboles : la KL moyenne au prior et $I(X ; Z)$, dans cet ordre | une liste de 2 nombres |
| h | vrai ou faux : si $q(z \mid x)$ était le posterior exact d'un modèle de prior $p(z)$, et si la source suivait la loi marginale de ce modèle, e) vaudrait 0 | `True` ou `False` |

Dans ta copie : lesquels des trois symboles le code envoie-t-il le plus sûrement sur un même $z$, et lequel coûte le plus cher en information ? Pourquoi la KL moyenne au prior surestime-t-elle ce que le code transmet ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M25b.4 — Le pas M d'un mélange de gaussiennes : les poids N_k/n par un multiplicateur de Lagrange, les moyennes et les covariances comme maximum de vraisemblance pondéré ∂ ★★ ⏱️ 40 min
**Objectif :** démontrer que le pas M maximise $Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}_t)$.
**Prérequis :** fiche §4 ; M13b, M18, M25a (∂ M25a.12, parcours C, facultatif) · **Parcours :** C, E

$\mathbf{x}_1, \ldots, \mathbf{x}_n$ sont dans $\mathbb{R}^d$ ; les responsabilités $r_{ik} \ge 0$ sont **fixées** (calculées au pas E), chaque ligne a pour somme 1, et $N_k = \sum_ir_{ik} > 0$. On maximise en $\boldsymbol{\theta} = (\pi_k, \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)_{k \le K}$
$$Q(\boldsymbol{\theta}) = \sum_{i=1}^n\sum_{k=1}^Kr_{ik}\big[\ln\pi_k + \ln\mathcal{N}(\mathbf{x}_i \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)\big].$$

1. Montre que $Q(\boldsymbol{\theta}) = \sum_kN_k\ln\pi_k + \sum_kQ_k(\boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)$, avec $Q_k = \sum_ir_{ik}\ln\mathcal{N}(\mathbf{x}_i \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)$, et explique pourquoi on peut maximiser séparément les poids et chaque couple $(\boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)$.
2. Maximise $\sum_kN_k\ln\pi_k$ sous la contrainte $\sum_k\pi_k = 1$ par un multiplicateur de Lagrange (M13b). Montre que le point trouvé, $\pi_k = \frac{N_k}{n}$, est bien le maximum (par exemple avec la positivité d'une KL discrète, M06).
3. À $\boldsymbol{\Sigma}_k$ fixée, annule le gradient de $Q_k$ en $\boldsymbol{\mu}_k$, puis montre que $Q_k(\boldsymbol{\mu}, \boldsymbol{\Sigma}_k) = Q_k(\hat{\boldsymbol{\mu}}_k, \boldsymbol{\Sigma}_k) - \frac{N_k}{2}(\hat{\boldsymbol{\mu}}_k - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}_k^{-1}(\hat{\boldsymbol{\mu}}_k - \boldsymbol{\mu})$, avec $\hat{\boldsymbol{\mu}}_k = \frac{1}{N_k}\sum_ir_{ik}\mathbf{x}_i$.
4. En $\boldsymbol{\mu}_k = \hat{\boldsymbol{\mu}}_k$, écris $Q_k$ en fonction de la précision $\boldsymbol{\Lambda}_k = \boldsymbol{\Sigma}_k^{-1}$ et de $\mathbf{S}_k = \sum_ir_{ik}(\mathbf{x}_i - \hat{\boldsymbol{\mu}}_k)(\mathbf{x}_i - \hat{\boldsymbol{\mu}}_k)^\top$, supposée définie positive ; annule son gradient (M18) et trouve $\boldsymbol{\Sigma}_k = \frac{\mathbf{S}_k}{N_k}$. Montre que c'est un maximum : si tu as fait ∂ M25a.12, dis quelle question le donne, en remplaçant $n$ par $N_k$ et $\mathbf{S}$ par $\mathbf{S}_k$ ; sinon, redémontre-le (avec $\frac{\mathbf{S}_k}{N_k} = \mathbf{C}\mathbf{C}^\top$, $\mathbf{B} = \mathbf{C}^\top\boldsymbol{\Lambda}_k\mathbf{C}$ et $\ln b \le b - 1$).
5. Pourquoi la covariance du pas M utilise-t-elle la **nouvelle** moyenne ? (Que donne 3 si l'on garde l'ancienne ?) Vérifie que, pour des $r_{ik}$ égales à 0 ou 1, on retrouve la proportion, la moyenne et la covariance de chaque groupe.

### Ex M25b.5 — L'ELBO en général : ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour un latent discret ou continu, la borne retrouvée par Jensen, et la forme E_q[ln p(x | z)] − KL(q ‖ p(z)) ∂ ★★★ ⏱️ 35 min
**Objectif :** démontrer l'identité de l'ELBO, la borne et son cas d'égalité, par deux chemins.
**Prérequis :** fiche §5 ; M06, M25a §7 · **Parcours :** C, E

On fixe un modèle $p(\mathbf{x}, \mathbf{z})$ et une observation $\mathbf{x}$, avec $p(\mathbf{x}) > 0$.

1. **Latent discret.** $q$ est une loi sur les valeurs de $\mathbf{z}$ telle que $q(\mathbf{z}) > 0 \Rightarrow p(\mathbf{x}, \mathbf{z}) > 0$. Démontre $\ln p(\mathbf{x}) = \operatorname{ELBO}(q) + \mathrm{KL}(q \,\|\, p(\mathbf{z} \mid \mathbf{x}))$.
2. Déduis-en $\operatorname{ELBO}(q) \le \ln p(\mathbf{x})$, avec égalité si et seulement si $q = p(\cdot \mid \mathbf{x})$.
3. **Latent continu.** Refais 1 avec des densités. Sur quel ensemble intègre-t-on ? Que vaut l'ELBO si $q$ met une masse positive là où $p(\mathbf{x}, \mathbf{z}) = 0$ ?
4. **Par Jensen.** Sans passer par la KL, montre $\operatorname{ELBO}(q) \le \ln p(\mathbf{x})$ en appliquant l'inégalité de Jensen (M25a §7) au logarithme et à la variable $\frac{p(\mathbf{x}, \mathbf{Z})}{q(\mathbf{Z})}$, $\mathbf{Z} \sim q$. Retrouve le cas d'égalité par le cas d'égalité de Jensen (le logarithme est strictement concave).
5. Montre $\operatorname{ELBO}(q) = \mathbb{E}_q[\ln p(\mathbf{x} \mid \mathbf{z})] - \mathrm{KL}(q \,\|\, p(\mathbf{z}))$ et $\operatorname{ELBO}(q) = \mathbb{E}_q[\ln p(\mathbf{x}, \mathbf{z})] + H(q)$.

### Ex M25b.7 — L'EM comme montée par coordonnées de l'ELBO : le pas E maximise en q, le pas M en θ, d'où la monotonie ; et ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] pour la moyenne d'une composante ∂ ★★★ ⏱️ 40 min
**Objectif :** démontrer la monotonie de l'EM par l'ELBO, son extension à un pas M partiel, et l'identité du gradient de la log-vraisemblance.
**Prérequis :** fiche §4 et §5 ; ∂ M25b.5 ; M09b · **Parcours :** C, E

Un modèle à latent discret, de paramètres $\boldsymbol{\theta}$, et $n$ données indépendantes : $\ell(\boldsymbol{\theta}) = \sum_i\ln p(\mathbf{x}_i \mid \boldsymbol{\theta})$ et $\operatorname{ELBO}(q, \boldsymbol{\theta}) = \sum_i\mathbb{E}_{q_i}\big[\ln p(\mathbf{x}_i, z \mid \boldsymbol{\theta}) - \ln q_i(z)\big]$, avec $q = (q_1, \ldots, q_n)$.

1. À $\boldsymbol{\theta}_t$ fixé, montre que $q \mapsto \operatorname{ELBO}(q, \boldsymbol{\theta}_t)$ atteint son maximum en $q_i = p(\cdot \mid \mathbf{x}_i, \boldsymbol{\theta}_t)$ et **seulement** là, et que ce maximum vaut $\ell(\boldsymbol{\theta}_t)$.
2. Avec $q_t$ ce maximum, montre que $\operatorname{ELBO}(q_t, \boldsymbol{\theta}) = Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}_t) + \sum_iH(q_{t,i})$, puis justifie chaque maillon de $\ell(\boldsymbol{\theta}_{t+1}) \ge \operatorname{ELBO}(q_t, \boldsymbol{\theta}_{t+1}) \ge \operatorname{ELBO}(q_t, \boldsymbol{\theta}_t) = \ell(\boldsymbol{\theta}_t)$.
3. **Un pas M partiel.** On ne met à jour que les moyennes (les poids et les covariances restent ceux de $\boldsymbol{\theta}_t$), de sorte que seulement $Q(\boldsymbol{\theta}_{t+1} \mid \boldsymbol{\theta}_t) \ge Q(\boldsymbol{\theta}_t \mid \boldsymbol{\theta}_t)$. Montre que $\ell$ ne baisse toujours pas (c'est l'**EM généralisé**). Quel maillon un pas M régularisé casse-t-il ?
4. Démontre $\nabla_{\boldsymbol{\theta}}\ln p(\mathbf{x} \mid \boldsymbol{\theta}) = \mathbb{E}_{p(z \mid \mathbf{x}, \boldsymbol{\theta})}\big[\nabla_{\boldsymbol{\theta}}\ln p(\mathbf{x}, z \mid \boldsymbol{\theta})\big]$ pour un latent à $K$ valeurs (une somme finie).
5. Pour un mélange de gaussiennes, déduis-en $\nabla_{\boldsymbol{\mu}_k}\ell = \sum_ir_{ik}\boldsymbol{\Sigma}_k^{-1}(\mathbf{x}_i - \boldsymbol{\mu}_k)$, où les $r_{ik}$ sont les responsabilités en $\boldsymbol{\theta}$. Montre qu'en un point fixe de l'EM ($\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t$), ce gradient est nul.

### Ex M25b.8 — L'ACP probabiliste : la loi marginale N(μ, WWᵀ + σ²I), le posterior de z par le modèle linéaire gaussien, et W ou WR donnent la même loi ∂ ★★ ⏱️ 35 min
**Objectif :** démontrer la loi jointe, la loi marginale et les deux formes du posterior de l'ACP probabiliste, et ce que la rotation change.
**Prérequis :** fiche §6 ; M25a §4 et §5 · **Parcours :** C, E

$\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_k)$ et $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \sigma^2\mathbf{I}_d)$ sont indépendants, $\sigma^2 > 0$, $\mathbf{W}$ est de forme $(d, k)$ et $\mathbf{x} = \mathbf{W}\mathbf{z} + \boldsymbol{\mu} + \boldsymbol{\varepsilon}$.

1. Justifie que $(\mathbf{z}, \mathbf{x})$ est un vecteur gaussien, et écris **en entier** sa loi : la moyenne et les quatre blocs de la covariance. Calcule $\operatorname{Cov}(\mathbf{x}, \mathbf{z})$ et $\operatorname{Cov}(\mathbf{z}, \mathbf{x})$.
2. Déduis-en la loi marginale de $\mathbf{x}$, puis, par le conditionnement de M25a, la loi de $\mathbf{z}$ sachant $\mathbf{x}$ sous la forme : moyenne $\mathbf{W}^\top\mathbf{C}^{-1}(\mathbf{x} - \boldsymbol{\mu})$, covariance $\mathbf{I}_k - \mathbf{W}^\top\mathbf{C}^{-1}\mathbf{W}$. Pourquoi $\mathbf{C}$ est-elle inversible ?
3. Montre $\mathbf{W}^\top(\mathbf{W}\mathbf{W}^\top + \sigma^2\mathbf{I}_d) = (\mathbf{W}^\top\mathbf{W} + \sigma^2\mathbf{I}_k)\mathbf{W}^\top$, puis $\mathbf{W}^\top\mathbf{C}^{-1} = \mathbf{M}^{-1}\mathbf{W}^\top$ (justifie que $\mathbf{M}$ est inversible).
4. Déduis-en $\mathbf{I}_k - \mathbf{W}^\top\mathbf{C}^{-1}\mathbf{W} = \sigma^2\mathbf{M}^{-1}$, et écris le posterior sous la forme de la fiche.
5. $\mathbf{R}$ est orthogonale $(k, k)$ et $\mathbf{W}' = \mathbf{W}\mathbf{R}$. Montre que $\mathbf{x}$ a la même loi avec $\mathbf{W}$ et avec $\mathbf{W}'$, mais que la loi jointe de $(\mathbf{z}, \mathbf{x})$ change si $\mathbf{W}' \ne \mathbf{W}$. Exprime la moyenne a posteriori obtenue avec $\mathbf{W}'$ en fonction de celle obtenue avec $\mathbf{W}$, et interprète.

### Ex M25b.11 — Dériver une espérance par rapport à un paramètre de la loi : l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré), la variance de l'estimateur à un tirage de ∂_σ E[e^X], et une indicatrice 1{X > c} pour laquelle l'échange échoue ∂ ★★★ ⏱️ 40 min
**Objectif :** démontrer le théorème de la dérivée par le chemin, l'appliquer à $\mathbb{E}[e^X]$ avec la variance de son estimateur, et voir sur une indicatrice ce qui casse.
**Prérequis :** fiche §7 ; M02a, M02b, M19 · **Parcours :** C, E

On reprend les notations et les hypothèses du théorème de la fiche §7 : $\psi(\theta, \xi) = f(g_\theta(\xi))$, continue en $\theta$ sur $I$ et dérivable sauf en un nombre fini de points pour presque tout $\xi$, dérivable en chaque $\theta$ pour presque tout $\xi$, et $\lvert\partial_\theta\psi(\theta, \xi)\rvert \le G(\xi)$ avec $\mathbb{E}[G(\xi)] < \infty$. On admet le théorème de convergence dominée.

1. Démontre le théorème : écris le taux d'accroissement $\frac{\psi(\theta + t, \xi) - \psi(\theta, \xi)}{t}$ comme une moyenne de $\partial_\theta\psi$ sur $[\theta, \theta + t]$, majore-le, puis passe à la limite sous l'espérance. Dis à quel endroit sert chaque hypothèse.
2. $X = \mu + \sigma\varepsilon$, $\varepsilon \sim \mathcal{N}(0, 1)$, et $J(\sigma) = \mathbb{E}[e^X]$ pour $\sigma \in\, ]0, s_0[$. Propose une fonction $G$ qui domine, et déduis-en $J'(\sigma) = \mathbb{E}[\varepsilon\,e^{\mu + \sigma\varepsilon}]$. Calcule cette espérance : montre $\mathbb{E}[\varepsilon\,e^{t\varepsilon}] = t\,e^{t^2/2}$ en complétant le carré.
3. L'estimateur à un tirage est $\hat g = \varepsilon\,e^{\mu + \sigma\varepsilon}$. Montre $\mathbb{E}[\varepsilon^2e^{t\varepsilon}] = (1 + t^2)\,e^{t^2/2}$, puis calcule $\mathbb{V}(\hat g)$. Pour $\mu = 1$ et $\sigma = 0{,}4$ : compare l'écart-type de $\hat g$ à $J'(\sigma)$.
4. $f(x) = \mathbb{1}\{x > c\}$ et $\theta = \mu$ : la fiche (§7) dit que l'hypothèse de continuité en $\theta$ manque. Montre que $\partial_\mu\psi(\mu, \varepsilon) = 0$ pour tout $\varepsilon$ sauf un, de sorte que la dérivée par le chemin vaut 0. Calcule la vraie dérivée $\frac{\mathrm{d}}{\mathrm{d}\mu}P(X > c)$, et écris-la comme la densité d'une loi normale en $c$. À quel endroit de ta démonstration de 1 l'absence de continuité se voit-elle ?

### Ex M25b.15 — β comme multiplicateur de Lagrange : une mesure gaussienne codée avec du bruit, distorsion s² e^{−2I}, le lagrangien D + βI, et le code qui s'éteint quand β dépasse 2s² ∂ ★★★ ⏱️ 35 min
**Objectif :** traiter jusqu'au bout un compromis distorsion-information gaussien : l'information par les entropies, la distorsion en fonction de l'information, et le seuil où le code s'éteint.
**Prérequis :** fiche §8 ; M13b, M25a §4 et §7 · **Parcours :** C, E

Une grandeur $X \sim \mathcal{N}(m, s^2)$ est transmise par le code $Z = X + U$, avec un bruit $U \sim \mathcal{N}(0, v)$ indépendant de $X$, de variance $v > 0$ choisie : plus $v$ est grand, moins le code coûte, et moins il renseigne. On reconstruit $X$ par $\hat X = \mathbb{E}[X \mid Z]$, avec la distorsion $D = \mathbb{E}[(X - \hat X)^2]$. Ici $s^2 = 3$ (la variance de la source n'est pas 1).

1. Montre $I(X ; Z) = h(Z) - h(Z \mid X) = \frac12\ln\big(1 + \frac{s^2}{v}\big)$, avec l'entropie différentielle d'une loi normale (M25a §7) ; justifie $h(Z \mid X) = h(U)$.
2. Par le conditionnement gaussien (M25a), montre $D = \frac{s^2v}{s^2 + v}$, puis exprime $D$ en fonction de $I = I(X ; Z)$ : $D(I) = s^2e^{-2I}$.
3. Pour $\beta > 0$, on minimise le lagrangien $\mathcal{L}(I) = D(I) + \beta I$ sur $I \in [0, +\infty[$. Montre que si $\beta \ge 2s^2$, le minimum est en $I = 0$ (le code s'éteint : vers quoi doit tendre $v$ ?), et que sinon il est en $I^\star = \frac12\ln\frac{2s^2}{\beta}$, avec $D^\star = \frac\beta2$.
4. Montre qu'à l'optimum $\beta = -D'(I^\star)$ : ce que coûte, en distorsion, un nat d'information en moins. Pourquoi est-ce cohérent avec la fiche (§8, « β est une pente ») ?
5. Pour $s^2 = 3$ : le seuil d'extinction ; puis, pour $\beta = 2$, les valeurs de $I^\star$, $D^\star$ et du bruit $v^\star$ du code optimal.

<a id="reflexion"></a>

## 📖 🗣️ 🔗 Lecture, explication et pont

### Ex M25b.16 — MML §8.4 et §8.5 : modèles probabilistes, inférence bayésienne, modèles à variables latentes, graphes orientés et d-séparation (survol), en anglais 📖 ★★ ⏱️ 40 min
**Objectif :** relire MML §8.4 et §8.5 avec la fiche : ce qui définit un modèle, ce que coûte l'inférence bayésienne, la place des latents, et la lecture d'un graphe.
**Prérequis :** fiche §1 et §2 · **Parcours :** C

Lis MML §8.4 (8.4.1 à 8.4.3) et §8.5 (8.5.1 ; survole 8.5.2), en suivant le guide de lecture de la fiche. Réponds dans ta copie, en français.
1. D'après 8.4.1, qu'est-ce qui spécifie un modèle probabiliste, et quelles trois quantités en découlent ? Relie-les à $p(\mathbf{x}, \mathbf{z}) = p(\mathbf{z})\,p(\mathbf{x} \mid \mathbf{z})$ de la fiche.
2. Dans (8.22) et (8.23), nomme le prior, la vraisemblance et l'évidence. D'après 8.4.2, quel est le problème de calcul central de l'inférence bayésienne, et celui de l'estimation par maximum de vraisemblance ou MAP ?
3. Comment 8.4.3 distingue-t-il les variables latentes $\mathbf{z}$ des paramètres $\boldsymbol{\theta}$ ? Écris (8.25) et (8.28) pour les machines de ✏️ M25b.1 ($z$ la machine, $\boldsymbol{\theta}$ les proportions, moyennes et écarts-types).
4. Avec (8.31) et la notation en cadre (Figure 8.10), dessine le graphe de ✏️ M25b.1 pour $n$ tiges : quels nœuds sont grisés, lesquels sont hors du cadre ?
5. En 8.5.2 (survol), fais correspondre *head to tail*, *tail to tail* et *head to head* à la chaîne, la fourche et la collision de la fiche. Sur la Figure 8.11, explique (8.36) et (8.38) : quel nœud est une collision, et pourquoi observer $e$ change-t-il la conclusion ? Relève au passage quatre expressions anglaises et leur traduction dans la fiche.

### Ex M25b.17 — MML ch. 11 : mélange de gaussiennes, responsabilités, mises à jour, EM et point de vue latent, en anglais ; refaire l'Exemple 11.1 avec ses propres données 📖 ★★ ⏱️ 50 min
**Objectif :** relire le chapitre 11 de MML avec la fiche, corriger une affirmation trop rapide, et refaire le début de son exemple avec tes nombres.
**Prérequis :** fiche §3 à §5 · **Parcours :** C

Lis MML §11.1 à §11.4, en suivant le guide de lecture de la fiche ; les figures des exemples se regardent sans être refaites. Réponds dans ta copie, en français.
1. (11.4) permet $\pi_k = 0$ : que devient alors la composante $k$, et pourquoi la fiche et `latent.py` demandent-ils $\pi_k > 0$ ?
2. Les responsabilités (11.17) sont appelées une affectation « douce » (*soft assignment*) ; à quoi §11.4 (11.72) les identifie-t-il ? Fais le lien avec la fiche (§3).
3. Les Théorèmes 11.1 à 11.3 annulent le gradient de la log-vraisemblance : quelles quantités traitent-ils comme fixées, et pourquoi le début de §11.3 dit-il que ce n'est pas une solution en forme fermée ? Quelle fonction la fiche maximise-t-elle à la place (∂ M25b.4) ?
4. §11.3 affirme que chaque pas de l'EM augmente la log-vraisemblance. Corrige la phrase de deux façons (fiche §4).
5. **Refais l'Exemple 11.1 avec tes données** : quatre mesures en dimension 1, deux composantes, une initialisation de ton choix (poids $\frac12$, deux moyennes, une même variance). Calcule les responsabilités (comme l'Exemple 11.2), mets à jour **seulement les moyennes** (comme l'Exemple 11.3), et calcule la log-vraisemblance avant et après cette mise à jour. Pourquoi est-on sûr qu'elle ne baisse pas (∂ M25b.7, question 3) ?

### Ex M25b.18 — MML §10.7 : l'ACP probabiliste, processus génératif, vraisemblance, loi jointe et posterior, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** relire MML §10.7 avec la fiche : notations, la loi jointe, une écriture à corriger et les deux formes du posterior.
**Prérequis :** fiche §6 · **Parcours :** C

Lis MML §10.7 (10.7.1 à 10.7.3) et, au §10.8, le passage (10.77) à (10.79), en suivant le guide de lecture de la fiche. Réponds dans ta copie, en français.
1. Fais la correspondance entre $\mathbf{B}$, $M$, $D$ de (10.63) et les notations de la fiche. Que désigne $\mathbf{M}$ dans la fiche ?
2. La remarque qui suit la Figure 10.14 parle du sens de la flèche entre $\mathbf{z}$ et $\mathbf{x}$ : que veut dire « inverser » la flèche, et avec quel outil ?
3. Dans (10.71), le livre écrit $\operatorname{Cov}[\mathbf{x}, \mathbf{z}] = \operatorname{Cov}_{\mathbf{z}}[\mathbf{B}\mathbf{z} + \boldsymbol{\mu}]$. Qu'aurait-il fallu écrire, et pourquoi le résultat $\mathbf{B}$ est-il quand même juste ?
4. Compare (10.74) et (10.75) à la forme du posterior de la fiche : quelle matrice inverse-t-on dans chaque forme, et de quelle taille ? Que dit le livre de la covariance a posteriori ?
5. Dans (10.78) et (10.79), à quoi correspondent $\mathbf{T}$ et $\boldsymbol{\Lambda}$ dans la fiche ? La note en marge dit que $\boldsymbol{\Lambda} - \sigma^2\mathbf{I}$ est semi-définie positive : justifie-le avec (10.79).

### Ex M25b.19 — Expliquer l'EM avec un bac de pièces venues de deux machines inconnues : deviner, réestimer, recommencer, sans jamais reculer 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule l'idée de l'EM et pourquoi il ne recule jamais.
**Prérequis :** fiche §4 · **Parcours :** C, E

Un ami trie un bac de pièces mélangées venues de deux machines, dont il ne connaît ni les réglages ni les proportions ; seule la taille des pièces les distingue un peu. Il te demande comment un ordinateur peut retrouver les deux machines « sans savoir qui a fait quoi ».

Réponds-lui en 6 à 10 phrases, sans formule, avec l'image du bac : le point de départ (une supposition sur les deux machines) ; ce que fait l'étape « deviner » (pour chaque pièce, une part de responsabilité de chaque machine, et pas un choix tout ou rien) ; ce que fait l'étape « réestimer » (des moyennes pondérées par ces parts) ; pourquoi on recommence ; pourquoi la qualité de l'explication ne recule jamais ; et pourquoi le résultat peut dépendre de la supposition de départ. Puis réécris ta réponse en 3 phrases.

### Ex M25b.23 — Pont : l'ELBO de n mesures rangées en lignes, écrite « reconstruction moins KL au prior » E_q[ln p(x | z)] − KL(q ‖ π), en nats par mesure, et ce que gagne chaque terme quand q devient le posterior 🔗 ★ ⏱️ 30 min
**Objectif :** calculer, sur un tableau de mesures en lignes, l'ELBO sous la forme « reconstruction moins KL au prior » utilisée par les bibliothèques, en nats par mesure.
**Prérequis :** fiche §5 ; 🔨 M25b.22 (facultatif : tu peux retrouver tes nombres avec ta `gmm_elbo`) · **Parcours :** C, E

Deux machines produisent des pièces de masses $\mathcal{N}(10, 1)$ et $\mathcal{N}(14 ;\ 2{,}25)$ (en g), dans les proportions $\boldsymbol{\pi} = (0{,}75 ;\ 0{,}25)$. Trois pièces pesées forment le tableau $\mathbf{X}$ de forme $(3, 1)$, de lignes 9,2 ; 11,6 ; 13,4. Pour chaque pièce, une loi $q_i$ sur les deux machines est donnée par la ligne $i$ du tableau
$$\mathbf{R} = \begin{pmatrix} 0{,}85 & 0{,}15 \\ 0{,}5 & 0{,}5 \\ 0{,}3 & 0{,}7 \end{pmatrix}.$$
La reconstruction est $\sum_i\sum_kr_{ik}\ln\mathcal{N}(x_i \mid \mu_k, \sigma_k^2)$, la KL au prior $\sum_i\mathrm{KL}(q_i \,\|\, \boldsymbol{\pi})$ ; on donne tout **en nats par mesure** (divisé par $n = 3$).

| | Question | Réponse attendue |
|---|---|---|
| a | la forme du tableau des log-densités $\ln\mathcal{N}(x_i \mid \mu_k, \sigma_k^2)$ | une forme |
| b | la reconstruction, par mesure | un nombre (4 décimales) |
| c | la KL au prior, par mesure | un nombre (4 décimales) |
| d | l'ELBO, par mesure | un nombre (4 décimales) |
| e | les responsabilités $r_{i1}$ du posterior, pour les trois pièces | une liste de 3 nombres (3 décimales) |
| f | avec $q_i$ = le posterior : la reconstruction puis la KL au prior, par mesure | une liste de 2 nombres (4 décimales) |
| g | l'ELBO par mesure quand $q_i$ est le posterior | un nombre (4 décimales) |
| h | vrai ou faux : en passant de $\mathbf{R}$ au posterior, la reconstruction **et** la KL au prior augmentent toutes les deux | `True` ou `False` |

Dans ta copie : pourquoi g) est-il aussi $\frac{\ell}{n}$ ? Le posterior paie plus de KL au prior que $\mathbf{R}$ : pourquoi l'ELBO monte-t-elle quand même ? Pourquoi diviser par $n$ pour comparer des tableaux de tailles différentes ?

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M25b.E1 — « Pourquoi l'algorithme EM ne fait-il jamais baisser la vraisemblance, et vers quoi converge-t-il ? » 💼 ★ ⏱️ 10 min
*Fiche §4 et §5 · parcours C, E*

« Pourquoi l'algorithme EM ne fait-il jamais baisser la vraisemblance, et vers quoi converge-t-il ? »

Ta réponse doit dire ce qu'est l'ELBO et pourquoi c'est une borne, ce que fait chaque pas (et pourquoi le pas E rend la borne exacte), la chaîne d'inégalités qui donne la monotonie, la condition « sans régularisation », vers quoi l'EM converge (un point stationnaire, souvent un maximum local, jamais garanti global ; et le maximum global d'un mélange n'existe pas), ce qu'on fait en pratique (plusieurs initialisations), et la vitesse.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m25b_variables_latentes/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus (M25b.23 se fait sur papier, après le 🔨 M25b.22). **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M25b.20 | Les responsabilités d'un mélange de gaussiennes, calculées en log (le pas E) · `gmm_e_step` | 🔨 | ★★ | 35 | C, E |
| M25b.21 | Le pas M d'un mélange de gaussiennes : poids, moyennes et covariances pondérées, avec une régularisation · `gmm_m_step` | 🔨 | ★★ | 30 | C, E |
| M25b.22 | La log-vraisemblance d'un mélange de gaussiennes, et son ELBO pour des responsabilités quelconques · `gmm_log_likelihood`, `gmm_elbo` | 🔨 | ★★ | 30 | C, E |
| M25b.24 | `scipy.linalg.subspace_angles` et `np.linalg.eigh` : les angles principaux de M25b.10, et l'ACP probabiliste de mesures par leurs valeurs propres, contre la vraisemblance de `mvn_logpdf` | 📦 | ★ | 30 | C, E |
| M25b.25 | Prédire ce que devient la log-vraisemblance quand une composante centrée sur un point se resserre (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis avec une régularisation, et mesurer | 🔮 | ★ | 15 | C |
| M25b.26 | L'EM sur des longueurs de poissons de trois cohortes : la log-vraisemblance et l'ELBO après chaque demi-pas, sans régularisation, plusieurs initialisations et des maxima locaux | 🔬 | ★★ | 30 | C, E |
| M25b.27 | Une gaussienne ajustée à un mélange bimodal par KL(p ‖ q) puis par KL(q ‖ p) : les deux courbes, et les deux minima de la KL inverse | 🎨 | ★ | 30 | C |
| M25b.28 | Chasse à l'erreur : des responsabilités sans log qui donnent 0/0, un pas M qui divise par n au lieu de N_k, et une ELBO sans l'entropie de q | 🐛 | ★ | 25 | C, E |
| M25b.29 | Un test de propriété : sur des mélanges tirés au hasard, ELBO ≤ log-vraisemblance, égalité après le pas E, et un EM sans régularisation (reg = 0) qui ne descend jamais (à une tolérance près) | 🛠️ | ★ | 30 | C |
| M25b.30 | Défi : retrouver trois populations de mesures en dimension 2 par l'EM, sous un seuil de log-vraisemblance moyenne sur des mesures de test | 🏆 | ★★★ | 35 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les trois 🔨 complètent ta copie `mon_travail/mymath/latent.py` (**mymath :** `latent.py`), dont la docstring du module dit ce qui est permis : NumPy, mais ni `np.cov` ni `np.average`, de `np.linalg` seulement `cholesky` et `solve`, aucune fonction de SciPy ni de scikit-learn. Ton `latent.py` importe la log-densité de M25a par un import relatif, `from .gaussian import mvn_logpdf` ; il peut importer de même `logsumexp` d'`approx` (M05a), mais celui-ci ne prend qu'une séquence : le log-sum-exp de chaque ligne d'un tableau $(n, K)$ s'écrit en NumPy, en retirant le maximum de la ligne. **Si ton `gaussian.py` contient encore le stub de `mvn_logpdf`, les tests de `latent` échouent** (« ⏳ `mvn_logpdf()` n'est pas encore écrite ») : termine d'abord le 🔨 M25a.20. Chaque 🔨 lance le groupe de tests de ses fonctions dans `tests/test_m25b_latent.py`, puis s'en sert ; dans le notebook, tu les appelles par `mymath.latent.<nom>(…)`, et celles de M25a par `mymath.gaussian.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy.

**M25b.20 · 🔨 `gmm_e_step(X, weights, means, covs)`.** Écris les responsabilités d'un mélange de gaussiennes : le tableau $a_{ik} = \ln\pi_k + \ln\mathcal{N}(\mathbf{x}_i \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)$ de forme $(n, K)$ (une colonne de `mvn_logpdf(X, means[k], covs[k])` par composante), auquel on retire le log-sum-exp de chaque ligne, puis l'exponentielle (la docstring fixe les formes et les refus) ; lance le groupe de tests de `gmm_e_step`. Ensuite, avec ta fonction : a) les responsabilités des quatre résistances de M25b.3 (un `X` de forme $(4, 1)$, les paramètres de départ, `covs` de forme $(2, 1, 1)$), à comparer à ta réponse a) ; b) on ajoute en cinquième ligne une résistance de 120 Ω égarée dans le bac : sa ligne de responsabilités, et vrai ou faux, le tableau ne contient aucun `nan` ; c) la tige de 98,2 mm de M25b.1 avec les trois machines (`covs` = les variances 1, 1 et 4, de forme $(3, 1, 1)$) : sa ligne, à comparer à ta réponse c). Ce qu'il faut observer : loin de toutes les composantes, c'est la plus large qui prend toute la responsabilité, et le calcul en log ne donne jamais $0/0$.

**M25b.21 · 🔨 `gmm_m_step(X, resp, reg=0.0)`.** Écris le pas M : $N_k$, les poids $N_k/n$, les moyennes pondérées, puis les covariances pondérées autour des **nouvelles** moyennes, plus `reg` sur la diagonale ; lance le groupe de tests de `gmm_m_step`. Ensuite : a) le pas M à partir des responsabilités de M25b.20 a), à comparer à tes réponses b), c) et d) de M25b.3 ; b) des responsabilités dures, chaque résistance allant à la valeur nominale la plus proche, `resp = [[1, 0], [1, 0], [0, 1], [0, 1]]` : les poids, les moyennes et les variances, et vrai ou faux, ce sont la proportion, `np.mean` et `np.var` de chaque groupe ; c) vrai ou faux : avec `reg=0.01`, les covariances dépassent celles de a) d'exactement 0,01 (à $10^{-12}$ près) ; d) avec `resp = [[1, 0], [0, 1], [0, 1], [0, 1]]`, la composante 1 n'a qu'une résistance : sa variance rendue, et vrai ou faux, `gmm_e_step` refuse ces paramètres par une `ValueError`. Ce qu'il faut observer : on divise par $N_k$ ; une composante portée par une seule donnée a une variance nulle, la singularité de la fiche §3.

**M25b.22 · 🔨 `gmm_log_likelihood(X, weights, means, covs)` et `gmm_elbo(X, resp, weights, means, covs)`.** Écris la log-vraisemblance (le même tableau $a$, le log-sum-exp de chaque ligne, puis la somme) et l'ELBO pour des lois $q_i$ quelconques, $\sum_i\sum_kr_{ik}(a_{ik} - \ln r_{ik})$ avec $0\ln 0 = 0$ ; lance les groupes de tests de ces deux fonctions. Ensuite : a) la log-vraisemblance des quatre résistances avant et après le pas M de M25b.21 a), à comparer à tes réponses e) et f) de M25b.3 ; b) pour les trois pièces du 🔗 M25b.23 : l'ELBO par mesure avec $\mathbf{R}$, puis avec les responsabilités de `gmm_e_step`, à comparer à tes réponses d) et g), et vrai ou faux, la seconde égale `gmm_log_likelihood(X, …) / 3` à $10^{-12}$ près ; c) la log-vraisemblance des cinq résistances (avec celle de 120 Ω), et vrai ou faux, elle est finie ; d) l'écart entre la log-vraisemblance des quatre résistances (paramètres de départ de M25b.3) et l'ELBO des responsabilités dures de M25b.21 b). Ce qu'il faut observer : l'ELBO reste sous la log-vraisemblance et la touche au posterior ; l'écart est une somme de KL.

**M25b.24 · 📦 `scipy.linalg.subspace_angles` et `np.linalg.eigh`.** a) Lis la section *Returns* de la documentation de `scipy.linalg.subspace_angles` (`help(...)` ou la page en ligne) : combien d'angles rend-elle pour un plan et une droite de $\mathbb{R}^4$ ? b) Applique-la aux deux plans de M25b.10, donnés par leurs bases **non orthonormées** (les colonnes $\mathbf{a}_1$, $\mathbf{a}_2$ et $\mathbf{b}_1$, $\mathbf{b}_2$), puis aux deux droites : vrai ou faux : les cosinus des angles rendus, rangés par ordre décroissant (`np.sort(np.cos(angles))[::-1]`), sont égaux à tes valeurs singulières de M25b.10 d), recalculées exactement (ou par `np.linalg.svd` de ta $\mathbf{Q}_A^\top\mathbf{Q}_B$), à $10^{-12}$ près. c) On tire 500 candidats du modèle de M25b.9 : `X = sample_mvn(mu, C, 500, seed=6054)`, avec $\boldsymbol{\mu} = (12, 11, 13)$ et $\mathbf{C} = \mathbf{w}\mathbf{w}^\top + 3\,\mathbf{I}$. Avec la covariance du maximum de vraisemblance $\hat{\boldsymbol{\Sigma}}$ (`np.cov(X, rowvar=False, bias=True)`) et ses valeurs et vecteurs propres par `np.linalg.eigh` (rangés par ordre croissant : retourne-les), ajuste l'ACP probabiliste à $k = 1$ par Tipping et Bishop : $\hat\sigma^2$ et $\lVert\hat{\mathbf{w}}\rVert^2$ (2 décimales chacun), puis la log-vraisemblance moyenne par candidat sous $\mathcal{N}(\bar{\mathbf{x}}, \hat{\mathbf{w}}\hat{\mathbf{w}}^\top + \hat\sigma^2\mathbf{I})$, par ta `mvn_logpdf` (4 décimales) ; et trois vrai ou faux : elle est plus petite que sous $\mathcal{N}(\bar{\mathbf{x}}, \hat{\boldsymbol{\Sigma}})$ ; elle baisse si l'on remplace $\hat\sigma^2$ par $1{,}1\,\hat\sigma^2$ (même $\hat{\mathbf{w}}$) ; elle est plus grande que sous les vrais paramètres $\mathcal{N}(\boldsymbol{\mu}, \mathbf{C})$. d) Le posterior du candidat noté $(15, 12, 15)$, dans le vrai modèle, comme loi conditionnelle de la loi jointe de $(z, \mathbf{x})$ en dimension 4, par ta `condition_gaussian` (moyenne $(0, \boldsymbol{\mu})$, covariance par blocs $\begin{pmatrix} 1 & \mathbf{w}^\top \\ \mathbf{w} & \mathbf{C} \end{pmatrix}$, indices `[1, 2, 3]`) : la moyenne et la variance (4 décimales), à comparer à ta réponse d) de M25b.9. Ce qu'il faut observer : la formule de Tipping et Bishop donne le maximum de vraisemblance parmi les modèles à un facteur ; le modèle complet a plus de paramètres et fait mieux sur ses propres données, comme l'estimation fait mieux que la vérité.

**M25b.25 · 🔮 Prédire ce que devient la log-vraisemblance quand une composante se resserre sur un point, puis avec une régularisation, et mesurer.** On reprend les quatre résistances de M25b.3 et le mélange de poids $(0{,}48 ;\ 0{,}52)$ dont la composante 2 a pour moyenne 50,57 Ω et pour variance 2,36 Ω², et dont la composante 1 est **centrée sur la première mesure**, 46,0 Ω, avec l'écart-type $\sigma_1$. **Avant d'exécuter**, prédis : a) quand $\sigma_1$ passe de $10^{-1}$ à $10^{-3}$, la log-vraisemblance (A) augmente d'environ 46 ; (B) ne change presque pas ; (C) augmente d'environ 4,6 ; (D) baisse ; b) quand $\sigma_1$ passe de $10^{-3}$ à $10^{-6}$, elle (A) augmente d'environ 6,9 ; (B) augmente d'environ 4,6 ; (C) devient `inf` ; c) si l'on ajoute `reg = 0.01` à la variance de la composante 1, elle (A) augmente des mêmes quantités ; (B) baisse à chaque fois ; (C) ne bouge presque plus dès $\sigma_1 = 10^{-3}$. Puis mesure avec ta `gmm_log_likelihood`, pour $\sigma_1 = 10^{-1}$, $10^{-3}$ et $10^{-6}$, sans puis avec `reg`, et relève : d) la log-vraisemblance pour $\sigma_1 = 10^{-6}$ sans régularisation (2 décimales) ; e) les trois valeurs avec régularisation (3 décimales). Ce qu'il faut observer : chaque facteur 100 sur $\sigma_1$ ajoute environ $\ln 100$ nats, sans limite (une seule donnée expliquée par une aiguille) ; `reg` met un plancher sous la variance et borne la log-vraisemblance.

**M25b.26 · 🔬 L'EM sur des longueurs de poissons de trois cohortes.** Les longueurs (en cm) de poissons d'un étang viennent de trois cohortes, d'un, deux et trois ans : proportions $(0{,}5 ;\ 0{,}3 ;\ 0{,}2)$, moyennes 12, 20 et 28 cm, écarts-types 1,5 ; 2 et 2,5 cm. La cellule de données les tire par un tirage ancestral : `rng = np.random.default_rng(6056)`, `z = rng.choice(3, size=300, p=(0.5, 0.3, 0.2))`, puis, pour chaque cohorte $k = 0, 1, 2$, les longueurs des lignes où `z == k` par `sample_mvn([mu_k], [[var_k]], n_k, seed=6057 + k)` ; `X` est de forme $(300, 1)$. Écris `em_trace_26(X, weights, means, covs, n_iter)`, qui fait `n_iter` itérations de l'EM sans régularisation et rend deux tableaux `ll` et `elbo` de longueur `2 * n_iter + 1` : la log-vraisemblance et l'ELBO après le premier pas E (le posterior des paramètres de départ), puis après chaque pas M et chaque pas E. Lance-la depuis dix initialisations : `rng = np.random.default_rng(6060)` puis, pour chacune, `idx = rng.choice(300, 3, replace=False)`, les moyennes `X[idx]`, trois variances égales à `X.var()`, des poids égaux, et `n_iter = 100`. Relève : a) vrai ou faux : dans les dix essais, aucun demi-pas ne fait baisser l'ELBO de plus de $10^{-9}(1 + \lvert\operatorname{ELBO}\rvert)$ ; b) vrai ou faux : après chaque pas E, l'ELBO et la log-vraisemblance diffèrent de moins de $10^{-9}(1 + \lvert\ell\rvert)$ ; c) la meilleure log-vraisemblance finale par poisson (4 décimales) ; d) le nombre d'essais dont la valeur finale par poisson est à moins de $10^{-3}$ de c) ; e) la valeur finale par poisson des autres essais (2 décimales) ; f) les trois moyennes du meilleur essai, dans l'ordre croissant (1 décimale). Trace, en fonction du demi-pas, sur les 30 premiers demi-pas, la log-vraisemblance et l'ELBO du meilleur essai et d'un des autres. Ce qu'il faut conclure : la log-vraisemblance monte en escalier et l'ELBO la touche après chaque pas E ; certaines initialisations restent longtemps près d'un moins bon point, où deux composantes se partagent les cohortes du haut : on relance depuis plusieurs initialisations.

**M25b.27 · 🎨 Une gaussienne ajustée à un mélange bimodal par KL(p ‖ q) puis par KL(q ‖ p).** Écris `draw_kl_fits_27(ax_density, ax_kl, weights, means, variances)`, qui dessine sur les **axes reçus** (sans ouvrir de figure) : dans `ax_density`, la densité $p$ du mélange (les temps de trajet de M25b.13 sur $[0, 60]$ min), la gaussienne $q_\star$ des moments, et les gaussiennes $q_1$ et $q_2$ de M25b.13, avec une légende ; dans `ax_kl`, pour $m$ de 10 à 55 par pas de 0,25, la KL inverse $m \mapsto \mathrm{KL}(\mathcal{N}(m, 4) \,\|\, p)$ et la KL directe $m \mapsto \mathrm{KL}(p \,\|\, \mathcal{N}(m, \mathbb{V}_p(X)))$, calculées sur une grille de $x$ de $-30$ à 100 (260 001 points) par `np.trapezoid`, avec $\ln p$ par un log-sum-exp (sur cette grille, $p$ reste représentable, mais une bosse plus étroite ou une grille plus large la feraient sortir des flottants). La vérification l'appelle sur une figure de deux panneaux et l'affiche ; tes propres calculs servent à relever a) à e). Relève : a) les abscisses des minima locaux de la KL inverse sur la grille (1 décimale) ; b) leurs valeurs (3 décimales) ; c) $\mathrm{KL}(p \,\|\, q_\star)$ (4 décimales) ; d) $\mathrm{KL}(q_\star \,\|\, p)$ (2 décimales) ; e) vrai ou faux : $\mathrm{KL}(q_\star \,\|\, p)$ dépasse les deux minima de a). Puis minimise $\mathrm{KL}(\mathcal{N}(m, s^2) \,\|\, p)$ en $(m, s)$ par `scipy.optimize.minimize` avec la borne $s \ge 0{,}1$ (`method="L-BFGS-B"`), depuis $(22, 2)$ et depuis $(40 ;\ 2{,}5)$, et compare les deux minima à tes réponses c) et d) de M25b.13. Ce qu'il faut observer : la KL inverse a un minimum par itinéraire, le plus bas sur la bosse la plus lourde ; la KL directe n'en a qu'un, entre les bosses, là où $p$ est presque nulle.

**M25b.28 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions pour des mesures en dimension 1 (`x` est un tableau 1-D, `sds` les écarts-types), chacune accompagnée d'une vérification qui passe.
- (1) `machine_shares(x, weights, means, sds)` doit rendre les responsabilités, de forme $(n, K)$ ; elle calcule chaque $\pi_k\,\mathcal{N}(x_i \mid \mu_k, \sigma_k^2)$ par `np.exp`, puis divise chaque ligne par sa somme. Il l'a vérifiée sur les quatre résistances de M25b.3 (paramètres de départ, `sds` = les racines de 1 et 2,5) : chaque ligne a pour somme 1 et toutes les valeurs sont dans $[0, 1]$. Il l'applique au bac qui contient aussi la résistance de 120 Ω.
- (2) `refit_machines(x, resp)` doit rendre le pas M, `(weights, means, variances)` ; elle calcule les poids $N_k/n$, les moyennes $\frac{1}{N_k}\sum_ir_{ik}x_i$, puis les variances $\frac1n\sum_ir_{ik}(x_i - \mu_k)^2$. Il l'a vérifiée avec une seule composante (une colonne de 1) : elle rend bien `np.mean(x)` et `np.var(x)`.
- (3) `bound_of_evidence(x, resp, weights, means, sds)` doit rendre l'ELBO ; elle rend $\sum_i\sum_kr_{ik}\big(\ln\pi_k + \ln\mathcal{N}(x_i \mid \mu_k, \sigma_k^2)\big)$. Il l'a vérifiée sur 200 tableaux de responsabilités tirés au hasard (`np.random.default_rng(6066).dirichlet`) : elle reste toujours sous la log-vraisemblance des quatre résistances.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `machine_shares_fixed`, `refit_machines_fixed` et `bound_of_evidence_fixed`, avec les mêmes arguments), puis réponds : a) vrai ou faux : la dernière ligne que rend `machine_shares` pour les cinq résistances contient des `nan` ; b) cette ligne, par `machine_shares_fixed` (4 décimales) ; c) les variances que rend `refit_machines` pour les quatre résistances, avec les responsabilités de `machine_shares_fixed` (3 décimales) ; d) `bound_of_evidence` au posterior moins la log-vraisemblance, pour les quatre résistances (4 décimales). Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas.

**M25b.29 · 🛠️ Un test de propriété.** Écris `em_property_test_29(X, weights, means, covs, m_step, n_iter, tol, rng)`, qui fait `n_iter` itérations de l'EM (le pas E de `gmm_e_step`, puis le pas M `m_step(X, resp)` reçu) depuis les paramètres donnés, et rend un dictionnaire de trois compteurs : `"bound"`, le nombre d'itérations où l'ELBO d'un tableau de responsabilités tiré au hasard (`rng.dirichlet(np.ones(K), size=n)`) dépasse la log-vraisemblance de plus de `tol * (1 + |ℓ|)` ; `"gap"`, le nombre d'itérations où l'ELBO au posterior s'écarte de la log-vraisemblance de plus de `tol * (1 + |ℓ|)` ; `"descent"`, le nombre de demi-pas où l'ELBO baisse de plus de `tol * (1 + |ELBO|)`. Le notebook fournit `random_mixture_29(rng)`, qui tire un mélange (dimension de 1 à 5, de 2 à 4 composantes), 200 données de ce mélange et des paramètres de départ, et `m_step_means_over_n(X, resp)`, un pas M faux qui divise les moyennes par $n$. a) Justifie `tol = 1e-9` : de quel ordre sont les erreurs d'arrondi sur une somme de quelques centaines de termes ? b) Sur 40 mélanges (`rng = np.random.default_rng(6061)`, puis `random_mixture_29(rng)` pour chacun, et ce même `rng` pour ton test), avec `gmm_m_step` sans régularisation et `n_iter = 30` : vrai ou faux, les trois compteurs restent nuls (un mélange où `gmm_e_step` lève une `ValueError`, une composante effondrée, se compte à part et se saute). c) Vrai ou faux : avec `m_step_means_over_n`, ton test compte au moins une descente. d) Vrai ou faux : avec `lambda X, r: gmm_m_step(X, r, reg=0.2)`, ton test compte au moins une descente. La vérification remplace aussi un instant ton `gmm_e_step` par un pas E faux (sans $\ln\pi_k$), puis ton `gmm_elbo` par une ELBO qui compte deux fois l'entropie : tes compteurs `"gap"`, puis `"bound"`, doivent alors compter ; elle exige aussi le nombre exact de descentes de la référence pour `m_step_means_over_n` sur deux mélanges cachés. Ce qu'il faut retenir : un test de propriété compte ses échecs sur beaucoup de cas tirés au hasard, avec une tolérance justifiée, et doit échouer sur un pas faux ; avec `reg > 0`, la monotonie n'est plus garantie.

**M25b.30 · 🏆 Défi : retrouver trois populations de mesures en dimension 2 par l'EM.** Une sonde mesure dans une rivière la turbidité (en NTU) et la conductivité (en centaines de µS/cm) ; l'eau est dans l'un de trois régimes, étiage, normal ou crue, que la sonde ne voit pas. La cellule de données tire 600 mesures d'entraînement et 400 mesures de test par un tirage ancestral (`draw_regimes_30(n, seed)`, graines 6062 et 6070, avec `sample_mvn`), d'un mélange de trois gaussiennes dont elle garde les paramètres cachés jusqu'à la vérification. Écris `fit_gmm_30(X, K, n_init, n_iter, reg, seed)`, qui rend `(weights, means, covs)` à partir de tes fonctions `mymath.latent` : plusieurs initialisations (les moyennes sur des mesures distinctes tirées avec la graine, chaque covariance égale à la covariance globale plus `reg` fois l'identité, des poids égaux), l'EM avec la régularisation `reg`, un arrêt quand la log-vraisemblance bouge de moins de $10^{-8}\lvert\ell\rvert$, et l'essai de meilleure log-vraisemblance d'entraînement. **Critère de réussite :** la log-vraisemblance moyenne des mesures de test (`gmm_log_likelihood(X_test, …) / 400`) est au moins $-3{,}38$. La vérification compare ensuite ton ajustement au modèle exact : $K = 3$, puis, après la meilleure permutation des composantes, des poids à 0,05 près, des moyennes à 0,3 près et des covariances à 0,4 près, coordonnée par coordonnée, et une log-vraisemblance de test à 0,02 près de celle du modèle exact ; enfin, pour un ajustement à $K = 4$ sur les mesures d'entraînement, où les cinq départs aboutissent à des points différents, la log-vraisemblance d'entraînement de ton ajustement doit égaler, à $10^{-6}$ près, celle du meilleur des essais de la référence. Relève : a) ta log-vraisemblance moyenne de test (affichée par la vérification) ; b) celle du modèle exact (affichée aussi) ; c) celles de tes ajustements à $K = 2$ et $K = 6$ (affichées aussi). Trace les mesures d'entraînement, colorées par la composante de plus grande responsabilité, avec l'ellipse à 90 % de chacune de tes trois composantes (M25a §3).
