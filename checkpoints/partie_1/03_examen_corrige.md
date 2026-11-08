# CP1 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Barème par sous-question**, entre crochets ; sauf mention contraire, une sous-question vaut 0,25 point. Une justification demandée « sur ta copie » compte dans la sous-question à laquelle elle se rattache.
- **Crédit partiel** sur une sous-question de 0,25 point : 0,1 pour une réponse juste sans la démarche demandée, ou pour une méthode juste avec une erreur de calcul ; 0,2 pour une fraction juste mais non simplifiée. **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois (par exemple une mauvaise constante $c$ en CP1.1 b, réutilisée en c) à f)).
- **Arrondis** : une décimale de trop ou de moins coûte au plus 0,05 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi.
- **Questions rédigées** (CP1.Q1, CP1.10, CP1.11 b, les phrases demandées « sur ta copie ») : les critères sont listés ; une idée juste formulée autrement compte autant.
- **Unités** : les entropies sont en bits ($\log_2$) ; le logarithme népérien s'écrit `ln`, ou `log` comme en Python, dans le notebook.

---

## CP1.Q1 — Dix affirmations sur la partie I 🧠 · 1,5 point

Chaque affirmation : **[0,05]** pour le verdict, **[0,1]** pour une justification juste (0,05 si elle est incomplète).

**a) Faux** (M02a). La médiane $m$ vérifie $F(m) = \frac{1}{2}$ : elle partage l'aire sous la densité en deux moitiés. Le point où $f$ est maximale est le **mode**. Pour une densité dissymétrique, ils diffèrent : la densité $2x$ sur $[0 ; 1]$ a son maximum en 1, et sa médiane en $\frac{1}{\sqrt{2}} \approx 0{,}71$.

**b) Vrai** (M02b). Une loi de Poisson de paramètre $\lambda$ a pour espérance **et** pour variance $\lambda$ : $\mathbb{V}(X) = 9$, donc l'écart-type vaut $\sqrt{9} = 3$.

**c) Faux** (M02b). La loi exponentielle de paramètre $\lambda$ a pour espérance $\frac{1}{\lambda}$ : ici $\mathbb{E}[X] = \frac{1}{2}$. Le paramètre est un **taux** (2 événements par unité de temps), la durée moyenne est son inverse.

**d) Faux** (M02c). La loi des grands nombres dit que la moyenne se **rapproche** de l'espérance quand $n$ grandit (la probabilité d'un écart donné tend vers 0) ; pour $n$ fixé, elle reste une variable aléatoire, d'écart-type $\frac{\sigma}{\sqrt{n}}$, ici $\frac{\sigma}{100}$ : petit, mais pas nul. Pour une variable continue, la moyenne n'est même presque jamais exactement égale à l'espérance.

**e) Vrai** (M03). $P(A \cap B) = P(A \mid B)\,P(B) = P(A)\,P(B)$ : $A$ et $B$ sont indépendants, donc $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = P(B)$. L'indépendance est symétrique.

**f) Vrai** (M04). L'a posteriori est $\mathrm{Beta}(a + k, b + n - k)$, de moyenne $\frac{a + k}{a + b + n} = \frac{a + b}{a + b + n} \times \frac{a}{a + b} + \frac{n}{a + b + n} \times \frac{k}{n}$ : une moyenne pondérée des deux, avec des poids positifs de somme 1. Elle est donc entre les deux, et d'autant plus près de $\frac{k}{n}$ que $n$ est grand devant $a + b$.

**g) Vrai** (M05a). $f'' > 0$ rend $f'$ strictement croissante : elle ne peut pas prendre deux fois la valeur 0. (Elle peut ne jamais s'annuler, comme pour $e^x$.)

**h) Faux** (M05b). Un gradient nul donne un point critique, qui peut être un **point selle** : $f(x, y) = x^2 + 4xy + y^2$ a un gradient nul en $(0, 0)$, mais $f(t, t) = 6t^2 > 0$ et $f(t, -t) = -2t^2 < 0$ : elle monte dans une direction et descend dans une autre.

**i) Vrai** (M06). $I(X ; Y) = H(Y) - H(Y \mid X)$ : si elle est nulle, $H(Y \mid X) = H(Y)$. Connaître $X$ ne change pas, en moyenne, l'incertitude sur $Y$ (les variables sont indépendantes).

**j) Faux** (M03). C'est le paradoxe de Simpson : si les deux traitements n'ont pas été donnés aux mêmes proportions de patients de chaque groupe, le taux global pondère les groupes différemment pour chacun, et la comparaison peut s'inverser. Exemple : A réussit 9 fois sur 10 chez les cas légers et 30 fois sur 90 chez les cas graves (39 sur 100) ; B réussit 72 fois sur 90 et 2 fois sur 10 (74 sur 100) ; A fait mieux dans chaque groupe (0,9 contre 0,8 ; 0,33 contre 0,2), et moins bien au total.

**Erreurs fréquentes** : en a), confondre médiane, moyenne et mode ; en b), répondre « faux » en confondant variance et écart-type ; en c), prendre le taux pour la durée moyenne ; en d), lire « converge » comme « égale » ; en f), croire que l'a posteriori peut dépasser les données ; en h), oublier les points selles ; en j), croire qu'un total hérite de l'ordre des groupes.
**Remédiation** : a) M02a.10, M02a.Q7 ; b) c) M02b.3, M02b.4, M02b.Q3 ; d) M02c.6, M02c.Q4 ; e) M03.2, M03.Q3 ; f) M04.6, M04.8, M04.Q5 ; g) M05a.1, M05a.Q1 ; h) M05b.8, M05b.Q6 ; i) M06.5, M06.Q4 ; j) M03.17.

## CP1.1 — Intégrales et densité ✏️ · 1,5 point

**Réponses** : a) `4` · b) `"1/4"` · c) `"(x**2 + 2*x)/8"` · d) `"5/8"` · e) `1.236` · f) `"7/6"`.

a) Par parties, avec $u = x$ et $v' = e^{x/2}$, donc $u' = 1$ et $v = 2e^{x/2}$ : $\int_0^2 x\,e^{x/2}\,dx = \left[2x\,e^{x/2}\right]_0^2 - \int_0^2 2e^{x/2}\,dx = 4e - \left[4e^{x/2}\right]_0^2 = 4e - (4e - 4) = 4$. **[0,25]**
b) $f \ge 0$ sur $[0 ; 2]$, et $\int_0^2 (x + 1)\,dx = \left[\frac{x^2}{2} + x\right]_0^2 = 4$ : l'aire totale vaut 1 pour $c = \frac{1}{4}$. **[0,25]**
c) $F(x) = \int_0^x \frac{t + 1}{4}\,dt = \frac{1}{4}\left(\frac{x^2}{2} + x\right) = \frac{x^2 + 2x}{8}$ ; vérification : $F(0) = 0$ et $F(2) = 1$. **[0,25]**
d) $F(2) - F(1) = 1 - \frac{3}{8} = \frac{5}{8}$. **[0,25]**
e) $F(m) = \frac{1}{2}$ équivaut à $m^2 + 2m - 4 = 0$, de racines $-1 \pm \sqrt{5}$ ; seule $\sqrt{5} - 1 \approx 1{,}236$ est dans $[0 ; 2]$. **[0,25]**
f) $\mathbb{E}[X] = \int_0^2 x\,\frac{x + 1}{4}\,dx = \frac{1}{4}\left[\frac{x^3}{3} + \frac{x^2}{2}\right]_0^2 = \frac{1}{4}\left(\frac{8}{3} + 2\right) = \frac{7}{6}$. **[0,25]**

La médiane (1,236) est plus grande que la moyenne (1,167) : la densité croît, la masse est à droite, et la moitié des valeurs dépasse 1,236. Comparer les deux est une bonne vérification de vraisemblance.

**Erreurs fréquentes** : en a), le signe moins de l'intégration par parties, $e^{x/2}$ pris pour sa propre primitive ($e + 1$), ou le crochet oublié en 0 ; en b), donner l'aire (4) au lieu de son inverse ; en c), oublier $c$ ou donner la densité ; en d), une différence de densités ; en e), garder la racine négative, ou résoudre $F(m) = \frac{1}{2}$ sans la constante.
**Remédiation** : M02a.4, M02a.8, M02a.9, M02a.10.

## CP1.2 — Lois usuelles : binomiale, Poisson, normale ✏️ · 1,5 point

**Réponses** : a) `0.4186` · b) `0.2033` · c) `0.2678` · d) `0.4512` · e) `0.82` · f) `12.08`.

Le nombre d'erreurs $X$ suit la loi binomiale $\mathcal{B}(12 ; 0{,}07)$.
a) $P(X = 0) = 0{,}93^{12} \approx 0{,}4186$. **[0,25]**
b) $P(X \ge 2) = 1 - P(X = 0) - P(X = 1) = 1 - 0{,}93^{12} - 12 \times 0{,}07 \times 0{,}93^{11} \approx 1 - 0{,}4186 - 0{,}3781 = 0{,}2033$. **[0,25]**
c) Le nombre d'alertes en une heure suit la loi de Poisson de paramètre 1,8 : $P(N = 2) = e^{-1{,}8}\,\frac{1{,}8^2}{2!} \approx 0{,}1653 \times 1{,}62 \approx 0{,}2678$. **[0,25]**
d) En 20 minutes, un tiers d'heure, le paramètre vaut $\frac{1{,}8}{3} = 0{,}6$ : $P(N \ge 1) = 1 - e^{-0{,}6} \approx 0{,}4512$. **[0,25]**
e) $z = \frac{12{,}5 - 14}{1{,}5} = -1$ et $z = \frac{17 - 14}{1{,}5} = 2$ : $P(12{,}5 < T < 17) = \Phi(2) - \Phi(-1) = 0{,}9772 - (1 - 0{,}8413) = 0{,}8185 \approx 0{,}82$. **[0,25]**
f) On cherche $t$ tel que $P(T > t) = 0{,}9$, soit $P(T \le t) = 0{,}1$ : $\frac{t - 14}{1{,}5} = -1{,}2816$, donc $t = 14 - 1{,}9224 \approx 12{,}08$ minutes (le 10ᵉ percentile). **[0,25]**

**Erreurs fréquentes** : en b), oublier le coefficient binomial 12 devant $P(X = 1)$, ou ne retrancher que $P(X = 0)$ (0,5814) ; en c), oublier $2!$, ou calculer $P(N \le 2)$ ; en d), garder le paramètre 1,8 pour 20 minutes ; en e), prendre $z = +1$ pour la borne 12,5 ($0{,}9772 - 0{,}8413$) ; en f), donner le 90ᵉ percentile (15,92), au-dessus de la moyenne, ou oublier de multiplier $z$ par $\sigma$ (12,72).
**Remédiation** : M02b.1, M02b.3, M02b.5, M02b.Q4.

## CP1.3 — Un couple de variables ✏️ · 1,25 point

**Réponses** : a) `[0.3, 0.3, 0.4]` · b) `False` · c) `0.04` · d) `0.69` · e) `1.01`.

a) On additionne chaque ligne : $P(X = 0) = 0{,}3$, $P(X = 1) = 0{,}3$, $P(X = 2) = 0{,}4$. De même, en additionnant les colonnes, $P(Y = 0) = 0{,}4$ et $P(Y = 1) = 0{,}6$. **[0,25]**
b) **Non** : $P(X = 0, Y = 0) = 0{,}1$, alors que $P(X = 0)\,P(Y = 0) = 0{,}3 \times 0{,}4 = 0{,}12$. Une seule case suffit pour conclure. **[0,25]**
c) $\mathbb{E}[X] = 0{,}3 + 2 \times 0{,}4 = 1{,}1$, $\mathbb{E}[Y] = 0{,}6$ et $\mathbb{E}[XY] = 1 \times 1 \times 0{,}1 + 2 \times 1 \times 0{,}3 = 0{,}7$ (seules les cases où $x$ et $y$ sont non nuls comptent) : $\operatorname{Cov}(X, Y) = 0{,}7 - 1{,}1 \times 0{,}6 = 0{,}04$. **[0,25]**
d) $\mathbb{E}[X^2] = 0{,}3 + 4 \times 0{,}4 = 1{,}9$, donc $\mathbb{V}(X) = 1{,}9 - 1{,}1^2 = 0{,}69$. **[0,25]**
e) $\mathbb{V}(Y) = 0{,}6 \times 0{,}4 = 0{,}24$ (Bernoulli), et $\mathbb{V}(X + Y) = \mathbb{V}(X) + \mathbb{V}(Y) + 2\,\operatorname{Cov}(X, Y) = 0{,}69 + 0{,}24 + 0{,}08 = 1{,}01$. **[0,25]**

**Erreurs fréquentes** : en a), additionner les colonnes ; en b), conclure à l'indépendance sur une seule case qui « marche » (il faut que **toutes** les cases soient des produits) ; en c), donner $\mathbb{E}[XY]$ ; en d), retrancher $\mathbb{E}[X]$ au lieu de son carré ; en e), additionner les variances comme si $X$ et $Y$ étaient indépendantes (0,93), ou prendre $\mathbb{E}[Y^2]$ pour $\mathbb{V}(Y)$.
**Remédiation** : M02b.7, M02b.8, M02c.9, M02b.Q5, M02b.Q6.

## CP1.4 — Estimer une moyenne : erreur type et intervalle de confiance ✏️ · 1,5 point

**Réponses** : a) `24.6` · b) `6.245` · c) `0.883` · d) `[22.87, 26.33]` · e) `1.45` · f) `[0.227, 0.493]`.

a) $\bar{x} = \frac{1\,230}{50} = 24{,}6$ tokens. **[0,25]**
b) $s^2 = \frac{1\,911}{49} = 39$, donc $s = \sqrt{39} \approx 6{,}245$. **[0,25]**
c) $\frac{s}{\sqrt{n}} = \sqrt{\frac{39}{50}} = \sqrt{0{,}78} \approx 0{,}8832$. **[0,25]**
d) $24{,}6 \pm 1{,}96 \times 0{,}8832 = 24{,}6 \pm 1{,}731$ : $[22{,}87 ;\ 26{,}33]$. **[0,25]**
e) $1{,}645 \times 0{,}8832 \approx 1{,}45$ token : l'intervalle à 90 % est plus étroit que celui à 95 %, puisqu'il accepte de se tromper plus souvent. **[0,25]**
f) $\hat{p} = \frac{18}{50} = 0{,}36$ et $\sqrt{\frac{0{,}36 \times 0{,}64}{50}} \approx 0{,}0679$ : $0{,}36 \pm 0{,}133$, soit $[0{,}227 ;\ 0{,}493]$. **[0,25]**

**Erreurs fréquentes** : en b), diviser par $n$ (6,182) ; en c), diviser par $n$ au lieu de $\sqrt{n}$, ou par $\sqrt{49}$ ; en d), utiliser $s$ au lieu de l'erreur type, ou oublier 1,96 ; en e), garder 1,96, ou donner la largeur entière ; en f), oublier la racine carrée.
**Remédiation** : M02c.5, M02c.8, M02c.12, M02c.Q6.

## CP1.5 — Un tableau de contingence et des métriques comme probabilités ✏️ · 1,5 point

**Réponses** : a) `"3/20"` · b) `"3/5"` · c) `"3/4"` · d) `"2/3"` · e) `0.9318` · f) `False`.

La matrice de confusion (positif = chute) :

| | alerte | pas d'alerte | total |
|---|---|---|---|
| chute | TP = 45 | FN = 15 | 60 |
| pas de chute | FP = 30 | TN = 410 | 440 |
| total | 75 | 425 | 500 |

a) $P(\text{alerte}) = \frac{75}{500} = \frac{3}{20}$. **[0,25]**
b) $P(\text{chute} \mid \text{alerte}) = \frac{45}{75} = \frac{3}{5}$ : on conditionne par la colonne. **[0,25]**
c) $P(\text{alerte} \mid \text{chute}) = \frac{45}{60} = \frac{3}{4}$ : on conditionne par la ligne. **[0,25]**
d) $F_1 = \frac{2PR}{P + R} = \frac{2 \times \frac{3}{5} \times \frac{3}{4}}{\frac{3}{5} + \frac{3}{4}} = \frac{9/10}{27/20} = \frac{2}{3}$. **[0,25]**
e) $\frac{410}{440} = \frac{41}{44} \approx 0{,}9318$. **[0,25]**
f) **Non** : $P(\text{alerte} \cap \text{chute}) = \frac{45}{500} = 0{,}09$, alors que $P(\text{alerte})\,P(\text{chute}) = 0{,}15 \times 0{,}12 = 0{,}018$. Heureusement : une montre dont l'alerte serait indépendante des chutes ne servirait à rien. **[0,25]**

**Erreurs fréquentes** : en a), ne compter que les vraies alertes (45) ; en b) et c), échanger precision et recall (le conditionnement se lit à droite de la barre) ; en d), la moyenne arithmétique (0,675), ou $2PR$ sans le dénominateur ; en e), diviser par les « pas d'alerte » (410/425) au lieu des « pas de chute », ou par le total ; en f), comparer $P(\text{chute} \mid \text{alerte})$ à… rien.
**Remédiation** : M03.1, M03.2, M03.4, M03.Q4, M03.R2.

## CP1.6 — Bayes et la loi Beta : une mise à jour conjuguée ✏️ · 1,5 point

**Réponses** : a) `"1/3"` · b) `[11, 31]` · c) `"11/42"` · d) `"1/4"` · e) `"7/26"` · f) `0.0762`.

a) La moyenne de $\mathrm{Beta}(a, b)$ est $\frac{a}{a + b} = \frac{4}{12} = \frac{1}{3}$. **[0,25]**
b) Conjugaison : $\mathrm{Beta}(a + k, b + n - k) = \mathrm{Beta}(4 + 7, 8 + 23) = \mathrm{Beta}(11, 31)$. **[0,25]**
c) $\frac{11}{42} \approx 0{,}262$, entre la moyenne a priori ($\frac{1}{3}$) et la fréquence observée ($\frac{7}{30} \approx 0{,}233$). **[0,25]**
d) Le mode $\frac{a - 1}{a + b - 2} = \frac{10}{40} = \frac{1}{4}$. **[0,25]**
e) L'a posteriori de b) devient l'a priori : $\mathrm{Beta}(11 + 3, 31 + 7) = \mathrm{Beta}(14, 38)$, de moyenne $\frac{14}{52} = \frac{7}{26}$ ; c'est aussi ce que donnerait une seule mise à jour avec les 10 acceptations sur 40. **[0,25]**
f) La probabilité que la prochaine proposition soit acceptée est la moyenne a posteriori, $\frac{14}{52}$ ; si elle l'est, la loi devient $\mathrm{Beta}(15, 38)$, et la suivante l'est avec la probabilité $\frac{15}{53}$. Les deux : $\frac{14}{52} \times \frac{15}{53} = \frac{105}{1\,378} \approx 0{,}0762$. **[0,25]**

**Erreurs fréquentes** : en b), ajouter le nombre d'essais à $b$ (au lieu des échecs) ; en c), donner la fréquence $\frac{7}{30}$ ; en d), confondre mode et moyenne ; en e), repartir de l'a priori ; en f), élever $\frac{7}{26}$ au carré (0,0725), comme si la première acceptation n'apprenait rien.
**Remédiation** : M04.5, M04.6, M04.7, M04.8, M04.Q5.

## CP1.7 — Taylor, Newton et un calcul stable ✏️ · 1,5 point

**Réponses** : a) `"2 + x/4 - x**2/64"` · b) `2.0975` · c) `1.25` · d) `1.2143` · e) `-784.867` · f) `0.876`.

a) $f(0) = 2$ ; $f'(x) = \frac{1}{2\sqrt{4 + x}}$, $f'(0) = \frac{1}{4}$ ; $f''(x) = -\frac{1}{4(4 + x)^{3/2}}$, $f''(0) = -\frac{1}{32}$. Donc $T_2(x) = 2 + \frac{x}{4} - \frac{1}{32} \times \frac{x^2}{2} = 2 + \frac{x}{4} - \frac{x^2}{64}$. **[0,25]**
b) Avec $x = 0{,}4$ : $2 + 0{,}1 - 0{,}0025 = 2{,}0975$, pour $\sqrt{4{,}4} \approx 2{,}09762$ : l'erreur, environ $1{,}2 \times 10^{-4}$, est de l'ordre du terme suivant. **[0,25]**
c) $g(x) = x^3 + x - 3$, $g'(x) = 3x^2 + 1$ : $g(1) = -1$ et $g'(1) = 4$, donc $x_1 = 1 - \frac{-1}{4} = 1{,}25$. **[0,25]**
d) $g(1{,}25) = 0{,}203125$ et $g'(1{,}25) = 5{,}6875$ : $x_2 = 1{,}25 - 0{,}035714 \approx 1{,}2143$ (la racine vaut environ 1,2134). **[0,25]**
e) On met le plus grand score en facteur : $\ln\left(e^{-785}\left(e^{-5} + e^{-2} + 1\right)\right) = -785 + \ln(1{,}142073) \approx -785 + 0{,}132845 = -784{,}867$. **[0,25]** Sur la copie : chaque `math.exp` vaut 0 en `float64` (au-dessous d'environ $e^{-745}$, c'est l'underflow), la somme vaut 0, et `math.log(0)` lève une erreur (`ValueError`) ; on ne calcule que des exponentielles d'écarts au maximum, toutes entre 0 et 1, dont une vaut exactement 1.
f) $\frac{e^{-785}}{e^{-790} + e^{-787} + e^{-785}} = \frac{1}{e^{-5} + e^{-2} + 1} \approx 0{,}876$. **[0,25]**

**Erreurs fréquentes** : en a), oublier le $\frac{1}{2}$ du terme d'ordre 2 ($-\frac{x^2}{32}$), ou prendre les coefficients de $\sqrt{1 + x}$ ; en c), le pas $\frac{g'}{g}$ au lieu de $\frac{g}{g'}$ ; en e), répondre $-785$ (le maximum seul), ou oublier le terme $e^0 = 1$ du maximum ; en f), donner la probabilité d'un autre score.
**Remédiation** : M05a.4, M05a.6, M05a.10, M05a.Q7, M05a.14.

## CP1.8 — Gradient, dérivée directionnelle et point critique ✏️ · 1,5 point

**Réponses** : a) `[9, -12]` · b) `"-72/29"` · c) `15` · d) `[0, 0, 2, 2]` · e) `3` · f) `-4`.

$\frac{\partial f}{\partial x} = 3x^2 - 6y$ et $\frac{\partial f}{\partial y} = -6x + 6y$.
a) En $(1, -1)$ : $3 + 6 = 9$ et $-6 - 6 = -12$. **[0,25]**
b) $\lVert(20, 21)\rVert = \sqrt{400 + 441} = 29$, donc $\mathbf{u} = \left(\frac{20}{29}, \frac{21}{29}\right)$ et $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \frac{180 - 252}{29} = -\frac{72}{29} \approx -2{,}48$ : $f$ descend dans cette direction. **[0,25]**
c) La plus grande pente est $\lVert \nabla f(1, -1) \rVert = \sqrt{81 + 144} = 15$, dans la direction du gradient. **[0,25]**
d) $\frac{\partial f}{\partial y} = 0$ donne $y = x$ ; alors $3x^2 - 6x = 0$, soit $x = 0$ ou $x = 2$ : les points $(0, 0)$ et $(2, 2)$. **[0,25]**
e) **3**. Les dérivées secondes : $f_{xx} = 6x$, $f_{yy} = 6$, $f_{xy} = -6$. En $(0, 0)$, $f_{xx} f_{yy} - f_{xy}^2 = 0 - 36 < 0$ : point selle. (Autre argument : $f(x, 0) = x^3$ change de signe autour de 0, alors que $f(0, 0) = 0$.) **[0,25]**
f) $f(2, 2) = 8 - 24 + 12 = -4$. En $(2, 2)$, $f_{xx} f_{yy} - f_{xy}^2 = 72 - 36 > 0$ et $f_{xx} = 12 > 0$ : un minimum **local** (pas global : $f(x, 0) = x^3$ tend vers $-\infty$). **[0,25]**

**Erreurs fréquentes** : en a), oublier le terme $-6y$ en dérivant par rapport à $x$, ou une erreur de signe avec $y = -1$ ; en b), ne pas rendre la direction unitaire ($-72$) ; en c), oublier la racine (225) ; en e), croire qu'un point critique est toujours un extremum ; en f), dire « minimum global » sans regarder les limites.
**Remédiation** : M05b.2, M05b.3, M05b.4, M05b.5, M05b.8, M05b.Q6.

## CP1.9 — Entropie, information mutuelle et KL ✏️ · 1,5 point

**Réponses** : a) `1.458` · b) `1.586` · c) `0.128` · d) `"7/8"` · e) `0.61` · f) `0.39`.

a) $H(p) = 0{,}45 \times 1{,}1520 + 0{,}4 \times 1{,}3219 + 0{,}15 \times 2{,}7370 \approx 0{,}5184 + 0{,}5288 + 0{,}4106 = 1{,}4578$, soit 1,458 bit. **[0,25]**
b) $H(p, q) = -\sum p_i \log_2 q_i \approx 0{,}45 \times 0{,}7370 + 0{,}4 \times 1{,}5146 + 0{,}15 \times 4{,}3219 \approx 0{,}3317 + 0{,}6058 + 0{,}6483 = 1{,}5858$, soit 1,586 bit. **[0,25]**
c) $\mathrm{KL}(p \,\|\, q) = H(p, q) - H(p) \approx 1{,}5858 - 1{,}4578 = 0{,}128$ bit (ou directement $\sum p_i \log_2 \frac{p_i}{q_i}$). Le gros terme vient des annonces : l'ancien modèle leur donnait 0,05, alors que leur fréquence est 0,15. **[0,25]**
d) $P(\text{question} \mid F = 1) = \frac{0{,}35}{0{,}35 + 0{,}05} = \frac{7}{8}$. **[0,25]**
e) Les lois conditionnelles de $Y$ : $\left(\frac{7}{8}, \frac{1}{8}\right)$ si $F = 1$, d'entropie $\frac{7}{8}(3 - \log_2 7) + \frac{1}{8} \times 3 \approx 0{,}5435$ ; $\left(\frac{1}{6}, \frac{5}{6}\right)$ si $F = 0$, d'entropie $\frac{1}{6}\log_2 6 + \frac{5}{6}\log_2 \frac{6}{5} \approx 0{,}6501$ (avec $\log_2 6 = 1 + \log_2 3$). Pondérées par $P(F = 1) = 0{,}4$ et $P(F = 0) = 0{,}6$ : $H(Y \mid F) \approx 0{,}2174 + 0{,}3901 = 0{,}6075$ avec les valeurs de la table (0,6074 en valeurs exactes), soit 0,61 bit. **[0,25]**
f) $Y$ a la loi $(0{,}45 ;\ 0{,}55)$, d'entropie $\approx 0{,}5184 + 0{,}4744 = 0{,}9928$ ; $I(F ; Y) = H(Y) - H(Y \mid F) \approx 0{,}9928 - 0{,}6075 = 0{,}385$, soit 0,39 bit : le point d'interrogation enlève presque 40 % de l'incertitude sur « question ou non ». **[0,25]**

**Erreurs fréquentes** : en a), $\ln$ au lieu de $\log_2$ (1,010) ; en b), pondérer par $q$ (1,291) ; en c), calculer $\mathrm{KL}(q \,\|\, p)$ (0,102) ; en d), diviser par la colonne ($\frac{7}{9}$) ; en e), additionner les entropies des lignes sans les pondérer, ou calculer $H(F \mid Y)$ (0,59) ; en f), soustraire des valeurs arrondies trop tôt.
**Remédiation** : M06.1, M06.3, M06.5, M06.6, M06.Q5.

## CP1.10 — Une démonstration courte, au choix ∂ · 2 points

Un seul sujet est noté. Barème entre crochets ; une rédaction qui affirme sans justifier rapporte la moitié des points de l'étape.

### Sujet A — Combiner deux mesures

1. Par linéarité de l'espérance, $\mathbb{E}[T_w] = w\,\mathbb{E}[X_1] + (1 - w)\,\mathbb{E}[X_2] = w\mu + (1 - w)\mu = \mu$. **[0,25]**
2. $X_1$ et $X_2$ sont indépendantes, donc $wX_1$ et $(1 - w)X_2$ aussi : la variance de leur somme est la somme des variances. Et $\mathbb{V}(aX) = a^2\,\mathbb{V}(X)$. D'où $\mathbb{V}(T_w) = w^2 \sigma_1^2 + (1 - w)^2 \sigma_2^2$. **[0,5]** (0,25 pour l'indépendance citée, 0,25 pour $a^2$)
3. $\varphi(w) = w^2 \sigma_1^2 + (1 - w)^2 \sigma_2^2$ a pour dérivée $\varphi'(w) = 2w\sigma_1^2 - 2(1 - w)\sigma_2^2$, nulle pour $w^* = \frac{\sigma_2^2}{\sigma_1^2 + \sigma_2^2}$. Comme $\varphi''(w) = 2(\sigma_1^2 + \sigma_2^2) > 0$, $\varphi$ est convexe (une parabole tournée vers le haut) : $w^*$ est son minimum global. **[0,5]** (0,25 pour $w^*$, 0,25 pour la justification du minimum)
4. Avec $1 - w^* = \frac{\sigma_1^2}{\sigma_1^2 + \sigma_2^2}$ : $\mathbb{V}(T_{w^*}) = \frac{\sigma_2^4 \sigma_1^2 + \sigma_1^4 \sigma_2^2}{(\sigma_1^2 + \sigma_2^2)^2} = \frac{\sigma_1^2 \sigma_2^2\,(\sigma_1^2 + \sigma_2^2)}{(\sigma_1^2 + \sigma_2^2)^2} = \frac{\sigma_1^2 \sigma_2^2}{\sigma_1^2 + \sigma_2^2}$. C'est $\sigma_1^2 \times \frac{\sigma_2^2}{\sigma_1^2 + \sigma_2^2}$, et la fraction est strictement inférieure à 1 : la variance est plus petite que $\sigma_1^2$ ; de même pour $\sigma_2^2$. **[0,5]**
5. Si $\sigma_1 = \sigma_2 = \sigma$ : $w^* = \frac{1}{2}$ (la moyenne des deux mesures) et $\mathbb{V} = \frac{\sigma^2}{2}$, la variance de la moyenne de $n = 2$ mesures, $\frac{\sigma^2}{n}$ (M02c). **[0,25]**

**Grille de relecture.** (1) la linéarité de l'espérance, nommée ; (2) l'indépendance, utilisée pour additionner les variances, et le facteur $a^2$ ; (3) la dérivée, $w^*$, et un argument de minimum (dérivée seconde, ou signe de $\varphi'$) ; (4) le calcul de la variance minimale et la comparaison avec chaque $\sigma_i^2$ ; (5) le cas égal. À retenir : chaque mesure reçoit un poids proportionnel à l'**inverse de sa variance** ; la balance la plus précise compte le plus, et la combinaison est meilleure que la meilleure des deux.

### Sujet B — Une courbe convexe est au-dessus de ses tangentes

1. $g(a) = f(a) - f(a) = 0$ ; $g'(x) = f'(x) - f'(a)$, donc $g'(a) = 0$ ; $g''(x) = f''(x) \ge 0$. **[0,5]**
2. $g'' \ge 0$ : $g'$ est croissante. Comme $g'(a) = 0$, $g'(x) \le 0$ pour $x < a$ et $g'(x) \ge 0$ pour $x > a$. Donc $g$ décroît sur $]-\infty ; a]$ et croît sur $[a ; +\infty[$ : elle atteint son minimum en $a$, et $g(x) \ge g(a) = 0$ pour tout $x$. Autrement dit, la courbe de $f$ est au-dessus de sa tangente au point d'abscisse $a$, quel que soit $a$. **[0,75]** (0,25 pour $g'$ croissante, 0,25 pour son signe, 0,25 pour la conclusion et sa traduction)
3. $f = \exp$ vérifie $f'' = \exp > 0$ ; sa tangente en $a = 0$ est $y = e^0 + e^0\,(x - 0) = 1 + x$. Donc $e^x \ge 1 + x$ pour tout réel $x$. **[0,25]**
4. Avec $x = -p$ : $1 - p \le e^{-p}$. Pour $p \in [0 ; 1]$, les deux membres sont positifs ou nuls, et $t \mapsto t^n$ est croissante sur $[0 ; +\infty[$ : $(1 - p)^n \le \left(e^{-p}\right)^n = e^{-np}$. Application : $0{,}99^{300} \le e^{-3} \approx 0{,}0498$ (la valeur exacte, environ 0,0490, est très proche). **[0,5]** (0,25 pour l'inégalité, avec l'argument de positivité ; 0,25 pour l'application)

**Grille de relecture.** (1) les quatre calculs ; (2) la chaîne « $g''$ positive, donc $g'$ croissante, nulle en $a$, donc de signe connu, donc $g$ minimale en $a$ » ; (3) la bonne tangente ; (4) la positivité des deux membres avant d'élever à la puissance $n$. Cette inégalité sert à majorer la probabilité qu'un événement rare ne se produise jamais en $n$ essais indépendants.

**Erreurs fréquentes** (deux sujets) : en A, additionner les variances sans citer l'indépendance, ou oublier le carré des coefficients ; trouver $w^*$ sans montrer que c'est un minimum. En B, conclure « $g'' \ge 0$ donc $g \ge 0$ » sans passer par $g'$ ; élever une inégalité à la puissance $n$ sans vérifier les signes.
**Remédiation** : A : M02b.8, M02b.11, M02c.12, et R7 pour l'étude d'un extremum ; B : M05a.1, M05a.2, M05a.Q1.

## CP1.11 — Corriger une copie : cinq erreurs 🐛 · 1,25 point

**Réponse de a)** : `"ACDFG"`. **[0,5]** (0,1 par lettre juste, −0,1 par lettre en trop, sans descendre sous 0)

b) Une ligne par erreur **[0,15 chacune]** :
- **(A)** La variance vaut 0,25, donc l'écart-type 0,5 : $P(X > 12{,}6) = P\left(Z > \frac{12{,}6 - 12}{0{,}5}\right) = P(Z > 1{,}2) \approx 0{,}115$. On standardise avec l'écart-type, pas avec la variance (diviser par une variance plus petite que 1 gonfle $z$).
- **(C)** L'erreur type vaut $\frac{10}{\sqrt{25}} = 2$ : on divise par $\sqrt{n}$, pas par $n$.
- **(D)** $P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)} = \frac{0{,}6 \times 0{,}2}{0{,}5} = 0{,}24$ : la formule de Bayes ; une probabilité conditionnelle ne se retourne pas sans elle.
- **(F)** Avec $f(x) = x^3 - 2$ et $f'(x) = 3x^2$ : $x_1 = 1 - \frac{f(1)}{f'(1)} = 1 - \frac{-1}{3} = \frac{4}{3} \approx 1{,}333$ : le pas de Newton est $\frac{f}{f'}$, pas $\frac{f'}{f}$.
- **(G)** $\mathrm{KL}(p \,\|\, q) = 0{,}6 \log_2 \frac{0{,}6}{0{,}3} + 0{,}4 \log_2 \frac{0{,}4}{0{,}7} \approx 0{,}6 - 0{,}323 = 0{,}277$ bit : le rapport est $\frac{p}{q}$ ; une KL n'est jamais négative, et un résultat négatif devait alerter.

Les lignes justes : (B) par le changement de variable $u = x^2$, $\int_0^1 e^u\,du = e - 1$ ; (E) $\mathrm{Beta}(2 + 3, 2 + 2) = \mathrm{Beta}(5, 4)$ ; (H) $x$ est une constante quand on dérive par rapport à $y$, et $(\ln y)' = \frac{1}{y}$.

**Erreurs fréquentes** : croire (E) fausse (les 3 succès vont à $a$, les **2** échecs à $b$) ; croire (B) fausse faute de voir le changement de variable ; laisser passer (G) parce que la formule « ressemble » à celle de la KL.
**Remédiation** : M02a.5, M02b.5, M02c.8, M03.Q2, M04.25, M05a.6, M06.24.

## CP1.12 — Problème de synthèse : estimer un paramètre de bout en bout 🔗 · 2 points

**Réponses** : a) `0.313` · b) `"32/lam - 20/(1 - exp(-lam))"` · c) `1.123` · d) `1.032` · e) `1.027` · f) `True` · g) `0.358` · h) `[0.48, 1.58]`.

a) $P(X = 1) = \frac{e^{-2} \times 2}{1! \times (1 - e^{-2})} \approx \frac{0{,}2707}{0{,}8647} \approx 0{,}313$. **[0,25]**
b) La vraisemblance est le produit des 20 probabilités ; son logarithme : $\ell(\lambda) = \sum_i \left[x_i \ln\lambda - \lambda - \ln(x_i!) - \ln\left(1 - e^{-\lambda}\right)\right] = 32\ln\lambda - 20\lambda - 20\ln\left(1 - e^{-\lambda}\right) + C$, où $C$ ne dépend pas de $\lambda$. Puis $\ell'(\lambda) = \frac{32}{\lambda} - 20 - \frac{20\,e^{-\lambda}}{1 - e^{-\lambda}} = \frac{32}{\lambda} - \frac{20}{1 - e^{-\lambda}}$. **[0,25]**
c) Pour $\lambda > 0$, $\ell'(\lambda) = 0$ équivaut à $32\left(1 - e^{-\lambda}\right) = 20\lambda$, soit $\lambda = 1{,}6\left(1 - e^{-\lambda}\right)$ : c'est $g(\lambda) = 0$ ($g$ s'annule aussi en 0, mais $\lambda > 0$). Avec $g'(\lambda) = 1 - 1{,}6\,e^{-\lambda}$ : $g(1{,}6) = 1{,}6\,e^{-1{,}6} \approx 0{,}32303$, $g'(1{,}6) \approx 0{,}67697$, donc $\lambda_1 = 1{,}6 - \frac{0{,}32303}{0{,}67697} \approx 1{,}12282$, soit 1,123. **[0,25]**
d) $e^{-\lambda_1} \approx 0{,}32536$, $g(\lambda_1) \approx 0{,}04340$ et $g'(\lambda_1) \approx 0{,}47942$ : $\lambda_2 \approx 1{,}12282 - 0{,}09052 = 1{,}03230$, soit 1,032. **[0,25]**
e) Le pas suivant donne $\lambda_3 \approx 1{,}02719$, puis les décimales ne bougent plus (Newton double les décimales justes) : $\hat{\lambda} \approx 1{,}027$. **[0,25]**
f) **Vrai** : $\ell'(1) = 32 - \frac{20}{1 - e^{-1}} \approx 32 - 31{,}64 = 0{,}36 > 0$. Et $\ell'(1{,}6) = 20 - \frac{20}{1 - e^{-1{,}6}} \approx -5{,}06 < 0$ : $\ell'$ passe du positif au négatif en $\hat{\lambda}$, qui est donc bien un maximum. **[0,25]**
g) La proportion des jours sans signalement est $P(\text{Poisson} = 0) = e^{-\hat{\lambda}} \approx 0{,}358$ : un peu plus d'un jour sur trois n'a aucun signalement, et n'apparaît jamais dans le journal. **[0,25]**
h) $1{,}027 \pm 1{,}96 \times 0{,}28 = 1{,}027 \pm 0{,}549$ : $[0{,}48 ;\ 1{,}58]$. **[0,25]** Il est large parce que l'estimation ne repose que sur 20 jours.

Sur la copie, avec e) : la moyenne des jours du journal est celle des jours qui ont **au moins un** signalement ; les jours sans signalement, absents du journal, auraient fait baisser la moyenne. En formule, l'espérance de la loi du journal vaut $\frac{\lambda}{1 - e^{-\lambda}} > \lambda$, et c'est justement l'équation $g(\lambda) = 0$ : le maximum de vraisemblance égale l'espérance du modèle à la moyenne observée.

Le lien avec workbookIA : écrire une vraisemblance, la maximiser par un calcul numérique quand l'équation n'a pas de solution exacte, puis dire l'incertitude de l'estimation, c'est ce que font les bibliothèques de ML quand elles « entraînent » un modèle ; ici, avec un seul paramètre, chaque étape se fait à la main.

**Erreurs fréquentes** : en a), oublier de diviser par $1 - e^{-\lambda}$ (0,271) ; en b), oublier de dériver le terme $-20\ln(1 - e^{-\lambda})$, ou de sommer sur les 20 jours ; en c), le pas de Newton à l'envers, ou une erreur de signe dans $g'$ ; en e), répondre 1,6, ou s'arrêter à $\lambda_2$ ; en g), utiliser 1,6 au lieu de $\hat{\lambda}$ ; en h), centrer l'intervalle sur 1,6, oublier 1,96, ou diviser 0,28 par $\sqrt{20}$.
**Remédiation** : M02b.3, M04.3, M04.4, M05a.6, M02c.8, M02c.13.

## Barème récapitulatif et remédiation

| Question | Points | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP1.Q1 | 1,5 | M02a à M06 | les exercices cités au CP1.Q1, puis les quiz et les flashcards des chapitres concernés |
| CP1.1 | 1,5 | M02a | M02a.4, M02a.8, M02a.9, M02a.10 |
| CP1.2 | 1,5 | M02b | M02b.1, M02b.3, M02b.5, M02b.Q4 |
| CP1.3 | 1,25 | M02b, M02c | M02b.7, M02b.8, M02c.9 |
| CP1.4 | 1,5 | M02c | M02c.5, M02c.8, M02c.12, M02c.Q6 |
| CP1.5 | 1,5 | M03 | M03.1, M03.2, M03.4, M03.Q4 |
| CP1.6 | 1,5 | M04 | M04.5, M04.6, M04.7, M04.8 |
| CP1.7 | 1,5 | M05a | M05a.4, M05a.6, M05a.10, M05a.14 |
| CP1.8 | 1,5 | M05b | M05b.2, M05b.3, M05b.4, M05b.5, M05b.8 |
| CP1.9 | 1,5 | M06 | M06.1, M06.3, M06.5, M06.6 |
| CP1.10 | 2 | M02b, M02c ou M05a | A : M02b.8, M02b.11, M02c.12 ; B : M05a.1, M05a.2 |
| CP1.11 | 1,25 | M02a à M06 | M02a.5, M02b.5, M02c.8, M03.Q2, M04.25, M05a.6, M06.24 |
| CP1.12 | 2 | M02b, M04, M05a, M02c | M02b.3, M04.3, M04.4, M05a.6, M02c.8, M02c.13 |
| **Total** | **20** | | |

**Lire ta note**
- **16 à 20** : la partie I est solide. Passe au checkpoint I de workbookIA ; garde les flashcards de la partie I dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe au checkpoint I de workbookIA.
- **8 à moins de 12** : avant le checkpoint I de workbookIA, fais la remédiation, relis ta synthèse et les fiches des chapitres concernés.
- **Moins de 8** : reprends les exercices ★★ des chapitres où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
