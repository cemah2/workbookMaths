# M02b · Variables aléatoires et lois usuelles — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M02b.Q1 — Discrète ou continue ?
1. **Discrète** : un comptage (0, 1, 2…), souvent modélisé par une loi de Poisson.
2. **À densité** : une durée peut prendre n'importe quelle valeur d'un intervalle.
3. **Discrète** : une classe parmi un nombre fini (une loi catégorielle).
4. **À densité**.
5. **Discrète** : les valeurs 1, 2, 3… s'énumèrent une à une, même s'il y en a une infinité (une loi géométrique).
6. **Faux** : une variable discrète peut prendre une **suite** infinie de valeurs (5, ou une loi de Poisson).

### M02b.Q2 — Quelle loi pour quelle situation ?
1. **Binomiale** $\mathcal{B}\big(10, \frac{1}{6}\big)$ : 10 essais indépendants, succès « faire 6 » de probabilité $\frac{1}{6}$.
2. **Poisson** $\mathcal{P}(12)$ : des événements un par un, indépendants, au rythme moyen de 12 par heure.
3. **Géométrique** de paramètre 0,3 : le rang du premier succès.
4. **Exponentielle** de paramètre $\lambda = \frac{1}{5}$ par an (espérance 5 ans) : une durée jusqu'au prochain événement, sans mémoire (« ne s'use pas »).
5. **Catégorielle** de probabilités $(0{,}7 ;\ 0{,}2 ;\ 0{,}1)$.
6. **Normale** (approximativement) : une somme de nombreux petits effets indépendants (le théorème central limite, M02c).

### M02b.Q3 — Espérance et variance : vrai ou faux
1. **Faux** : une Bernoulli de paramètre 0,3 a pour espérance 0,3, qu'elle ne prend jamais ; un dé a pour espérance 3,5.
2. **Vrai** : une moyenne de carrés est positive ou nulle, et elle n'est nulle que si $X$ vaut toujours son espérance.
3. **Faux** : $\mathbb{E}[X^2] - \mathbb{E}[X]^2 = \mathbb{V}(X) \ge 0$, donc $\mathbb{E}[X^2] \ge \mathbb{E}[X]^2$, avec égalité seulement pour une variable constante.
4. **Vrai** : le facteur 3 compte au carré, le décalage 5 ne disperse pas.
5. **Faux** : la densité $\frac{1}{x^2}$ sur $[1 ; +\infty[$ n'a pas d'espérance (fiche §4).
6. **Vrai** : l'espérance vaut $\frac{1}{\lambda}$ et l'écart-type $\sqrt{\frac{1}{\lambda^2}} = \frac{1}{\lambda}$.

### M02b.Q4 — La loi normale : ce que disent μ et σ
1. **2** : la notation $\mathcal{N}(10, 4)$ donne la variance, $\sigma = \sqrt{4}$.
2. **Vrai** : la densité vaut en 0 $\frac{1}{0{,}2\sqrt{2\pi}} \approx 1{,}99$. Une densité peut dépasser 1.
3. **0,5** : par symétrie de la cloche autour de 0.
4. $\Phi(-1{,}5) = 1 - \Phi(1{,}5)$ ($\approx 0{,}0668$).
5. Elle est **divisée par 2** : le sommet vaut $\frac{1}{\sigma\sqrt{2\pi}}$ (la cloche s'élargit, l'aire reste 1).
6. $\Phi(1) \approx 0{,}8413$ : $\mu + \sigma$ a un z-score de 1.

### M02b.Q5 — Jointe, marginale, indépendance
1. $P(X = 1) = 0{,}2 + 0{,}4 = 0{,}6$.
2. $P(Y = 1) = 0{,}3 + 0{,}4 = 0{,}7$.
3. **Non** : $P(X = 1)\,P(Y = 1) = 0{,}6 \times 0{,}7 = 0{,}42 \ne 0{,}4 = P(X = 1, Y = 1)$. Une case suffit.
4. **Vrai** (fiche §5, « Une conséquence »).
5. **Faux** : beaucoup de lois jointes ont les mêmes marginales ; elles ne la déterminent que si l'on sait les variables indépendantes.
6. En **intégrant** l'autre variable : $f_X(x) = \int_{-\infty}^{+\infty} f(x, y)\,dy$ (fiche §7).

### M02b.Q6 — La variance d'une somme
1. $36 + 64 = 100$.
2. $\sqrt{100} = 10$ (et non $6 + 8 = 14$).
3. **100** aussi : les variances s'additionnent pour une différence.
4. $2^2 \times 36 = 144$.
5. $\frac{6}{\sqrt{9}} = 2$.
6. **Faux** : la linéarité de l'espérance vaut toujours, sans hypothèse d'indépendance.

### M02b.Q7 — Simuler une loi
1. La loi **uniforme sur $[2 ; 7]$**.
2. $-\frac{\ln(1 - U)}{\lambda}$ (ou $-\frac{\ln U}{\lambda}$, puisque $1 - U$ est aussi uniforme).
3. $\mathcal{N}(3, 2^2)$, soit $\mathcal{N}(3, 4)$.
4. La classe **2** : les sommes cumulées valent 0,5 ; 0,8 ; 1, et $0{,}5 \le 0{,}65 < 0{,}8$.
5. **Vrai** : $P(1 - U \le t) = P(U \ge 1 - t) = t$ pour $t$ dans $[0 ; 1]$.
6. $\Phi^{-1}$ ne s'écrit pas avec les fonctions usuelles : il faut l'approcher numériquement à chaque tirage (une dichotomie), ce qui est lent, ou utiliser une autre méthode (M02b.27).

<a id="rappels"></a>

## 🔁 Rappels

### M02b.R1 — Espérance d'une variable discrète (R8)
1. $\mathbb{E}[X] = -2 \times 0{,}3 + 0 \times 0{,}5 + 3 \times 0{,}2 = -0{,}6 + 0{,}6 = 0$.
2. $\mathbb{E}[X^2] = 4 \times 0{,}3 + 9 \times 0{,}2 = 1{,}2 + 1{,}8 = 3$.
3. $\mathbb{V}(X) = 3 - 0^2 = 3$.
4. $\mathbb{E}[2X - 1] = 2 \times 0 - 1 = -1$ et $\mathbb{V}(2X - 1) = 4 \times 3 = 12$.

### M02b.R2 — Intégrales et densités (M02a)
1. $\left[\frac{x^3}{3}\right]_0^3 = 9$.
2. $\left[-\frac{e^{-4x}}{4}\right]_0^{+\infty} = \frac{1}{4}$.
3. **Oui** : $f \ge 0$, et $\int_1^{+\infty} 3x^{-4}\,dx = \big[-x^{-3}\big]_1^{+\infty} = 0 - (-1) = 1$.
4. $\int_1^2 3x^{-4}\,dx = \big[-x^{-3}\big]_1^2 = -\frac{1}{8} + 1 = \frac{7}{8}$.

### M02b.R3 — Coefficients binomiaux (R8)
1. $\binom{6}{2} = \frac{6 \times 5}{2} = 15$.
2. $\binom{8}{3} = \frac{8 \times 7 \times 6}{6} = 56$.
3. 1 et 1 : une seule façon de ne rien choisir, une seule de tout choisir.
4. $\binom{7}{2} = 21$ : un tel mot est fixé par les positions de ses deux A.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M02b.1 — Loi de Bernoulli et loi binomiale

**Réponses** : a) `0.3277` · b) `0.2048` · c) `0.7373` · d) `4` · e) `4.0` · f) `0.8` · g) `0.6723` · h) `11`.

**Démarche.** $X \sim \mathcal{B}(5 ; 0{,}8)$ : 5 lancers indépendants, chacun réussi avec la probabilité 0,8.
- a) $0{,}8^5 = 0{,}32768$.
- b) $\binom{5}{3}\,0{,}8^3\,0{,}2^2 = 10 \times 0{,}512 \times 0{,}04 = 0{,}2048$.
- c) $P(X = 4) + P(X = 5) = 5 \times 0{,}4096 \times 0{,}2 + 0{,}32768 = 0{,}4096 + 0{,}32768 = 0{,}73728$.
- d) La loi complète : $P(X = 0, \ldots, 5) = 0{,}00032$ ; $0{,}0064$ ; $0{,}0512$ ; $0{,}2048$ ; $0{,}4096$ ; $0{,}32768$, de somme 1. La plus grande est $P(X = 4)$.
- e) $np = 5 \times 0{,}8 = 4$. f) $np(1 - p) = 5 \times 0{,}8 \times 0{,}2 = 0{,}8$.
- g) Le contraire de « cinq réussites » : $1 - 0{,}8^5 = 0{,}67232$.
- h) $1 - 0{,}8^n \ge 0{,}9 \iff 0{,}8^n \le 0{,}1 \iff n \ge \frac{\ln 0{,}1}{\ln 0{,}8} \approx 10{,}32$ (diviser par $\ln 0{,}8 < 0$ change le sens) ; vérification : $0{,}8^{10} \approx 0{,}107$ et $0{,}8^{11} \approx 0{,}086$. Donc $n = 11$.

Pour la copie : le nombre d'échecs $5 - X$ suit $\mathcal{B}(5 ; 0{,}2)$, la même situation vue du côté des échecs.

**Erreurs fréquentes.** Oublier $\binom{5}{3}$ en b (0,0205) ; échanger les exposants de 0,8 et 0,2 (0,0512) ; en c, ne garder que $P(X = 4)$ ; en f, donner la variance d'un seul lancer (0,16) ou l'écart-type (0,894).

**Variante.** $P(X \le 1)$ ? *Réponse* : $0{,}00032 + 0{,}0064 = 0{,}00672$.

### Ex M02b.2 — Loi géométrique : probabilités, et l'espérance par une série

**Réponses** : a) `0.144` · b) `0.216` · c) `0.64` · d) `6.25` · e) `2.5` · f) `1.5` · g) `2` · h) `"1/p"`.

**Démarche.**
- a) Deux échecs puis une réussite : $0{,}6^2 \times 0{,}4 = 0{,}144$.
- b) Les trois premières tentatives échouent : $0{,}6^3 = 0{,}216$.
- c) $1 - P(X > 2) = 1 - 0{,}6^2 = 0{,}64$ (ou $0{,}4 + 0{,}24$).
- d) $S = 1 + 2q + 3q^2 + 4q^3 + \cdots$ et $qS = q + 2q^2 + 3q^3 + \cdots$ ; en soustrayant terme à terme (rang par rang) : $S - qS = 1 + q + q^2 + \cdots = \frac{1}{1 - q}$ (R5). Donc $S = \frac{1}{(1 - q)^2} = \frac{1}{0{,}16} = 6{,}25$.
- e) $\mathbb{E}[X] = \sum_k k\,q^{k-1}p = p\,S = 0{,}4 \times 6{,}25 = 2{,}5$.
- f) Les tentatives échouées sont $X - 1$ : $\mathbb{E}[X - 1] = \mathbb{E}[X] - 1 = 1{,}5$, par linéarité, sans nouveau calcul.
- g) $P(X \le 1) = 0{,}4 < 0{,}5$ et $P(X \le 2) = 0{,}64 \ge 0{,}5$ : la médiane vaut 2.
- h) Le même calcul avec $q = 1 - p$ : $\mathbb{E}[X] = \frac{p}{(1 - q)^2} = \frac{p}{p^2} = \frac{1}{p}$.

**Erreurs fréquentes.** En b, $0{,}6^4$ (on n'impose rien à la quatrième tentative) ; en d, s'arrêter à $\frac{1}{1 - q} = 2{,}5$ ; en e, oublier le facteur $p$ (6,25) ; confondre $\mathbb{E}[X]$ et le nombre moyen d'échecs, $\frac{q}{p}$.

**Variante.** La variance de $X$, avec le tableau de la fiche ? *Réponse* : $\frac{1 - p}{p^2} = \frac{0{,}6}{0{,}16} = 3{,}75$.

### Ex M02b.3 — Loi de Poisson : probabilités, espérance, et la somme de deux variables de Poisson indépendantes

**Réponses** : a) `0.2231` · b) `0.2510` · c) `0.4422` · d) `7.5` · e) `0.0183` · f) `0.0733` · g) `0.1465` · h) `4.0`.

**Démarche.**
- a) $e^{-1{,}5} \approx 0{,}2231$. b) $e^{-1{,}5}\frac{1{,}5^2}{2} = 1{,}125\,e^{-1{,}5} \approx 0{,}2510$.
- c) $1 - P(X = 0) - P(X = 1) = 1 - e^{-1{,}5}(1 + 1{,}5) = 1 - 2{,}5\,e^{-1{,}5} \approx 0{,}4422$.
- d) La linéarité : 5 fois l'espérance d'un jour, $5 \times 1{,}5 = 7{,}5$.
- e) $P(X = 0)\,P(Y = 0) = e^{-1{,}5}e^{-2{,}5} = e^{-4} \approx 0{,}0183$.
- f) $(X, Y) = (0, 1)$ ou $(1, 0)$ : $e^{-4}(2{,}5 + 1{,}5) = 4e^{-4} \approx 0{,}0733$.
- g) $(0, 2)$, $(1, 1)$ ou $(2, 0)$ : $e^{-4}\left(\frac{2{,}5^2}{2} + 1{,}5 \times 2{,}5 + \frac{1{,}5^2}{2}\right) = e^{-4}(3{,}125 + 3{,}75 + 1{,}125) = 8e^{-4} \approx 0{,}1465$.
- h) $e^{-4}$, $4e^{-4}$, $8e^{-4} = e^{-4}\frac{4^2}{2}$ : les probabilités de $\mathcal{P}(4)$. Le paramètre est la somme $1{,}5 + 2{,}5$.

Pour la copie : $P(S = k) = \sum_{i=0}^{k} e^{-1{,}5}\frac{1{,}5^i}{i!}\,e^{-2{,}5}\frac{2{,}5^{k-i}}{(k-i)!} = \frac{e^{-4}}{k!}\sum_{i=0}^{k}\binom{k}{i}1{,}5^i\,2{,}5^{k-i} = e^{-4}\frac{4^k}{k!}$, par la formule du binôme (on a multiplié et divisé par $k!$, et $\frac{k!}{i!\,(k-i)!} = \binom{k}{i}$).

**Erreurs fréquentes.** Oublier le $2!$ en b (0,5020) ; en c, ne retirer que $P(X = 0)$ ; en e, additionner les probabilités au lieu de les multiplier ; en g, oublier le couple $(1, 1)$.

**Variante.** $P(S \ge 1)$ ? *Réponse* : $1 - e^{-4} \approx 0{,}9817$.

### Ex M02b.4 — Lois uniforme et exponentielle : probabilités et espérance

**Réponses** : a) `"1/15"` · b) `"1/3"` · c) `"8/15"` · d) `17.5` · e) `4.330` · f) `0.1353` · g) `2.5` · h) `0.3679`.

**Démarche.**
- a) $\frac{1}{25 - 10} = \frac{1}{15}$. b) $\frac{15 - 10}{15} = \frac{1}{3}$. c) $\frac{20 - 12}{15} = \frac{8}{15}$.
- d) Le milieu, $\frac{10 + 25}{2} = 17{,}5$ (8 h 17 min 30 s).
- e) $\mathbb{V}(D) = \frac{15^2}{12} = 18{,}75$, donc $\sigma(D) = \frac{15}{\sqrt{12}} = \frac{5\sqrt{3}}{2} \approx 4{,}330$.
- f) $P(T > 5) = e^{-0{,}4 \times 5} = e^{-2} \approx 0{,}1353$. g) $\frac{1}{0{,}4} = 2{,}5$ ans.
- h) $P(T > 2{,}5) = e^{-0{,}4 \times 2{,}5} = e^{-1} \approx 0{,}3679$.

Pour la copie : la loi exponentielle est asymétrique ; de rares très longues durées tirent l'espérance vers le haut, au-dessus de la médiane $\frac{\ln 2}{\lambda} \approx 1{,}73$ an. Et pour tout $\lambda$ : $P\big(T > \frac{1}{\lambda}\big) = e^{-\lambda \cdot \frac{1}{\lambda}} = e^{-1}$, toujours 37 % environ.

**Erreurs fréquentes.** Prendre la densité $\frac{1}{25}$ (oublier que $D$ commence à 10) ; en e, donner la variance, ou diviser par 12 sans racine ; en h, répondre 0,5 comme pour une loi symétrique.

**Variante.** La médiane de $T$ ? *Réponse* : $\frac{\ln 2}{0{,}4} \approx 1{,}733$ an.

### Ex M02b.5 — Loi normale : standardiser et lire la fonction Φ

**Réponses** : a) `1.5` · b) `0.9332` · c) `0.1587` · d) `0.7745` · e) `0.0228` · f) `39.32` · g) `0.789` · h) `0.0668`.

**Démarche.** $X \sim \mathcal{N}(30, 4^2)$, donc $\sigma = 4$ et $z = \frac{x - 30}{4}$.
- a) $z = \frac{36 - 30}{4} = 1{,}5$. b) $\Phi(1{,}5) = 0{,}9332$.
- c) $z = -1$ : $\Phi(-1) = 1 - \Phi(1) = 1 - 0{,}8413 = 0{,}1587$.
- d) $\Phi(1{,}5) - \Phi(-1) = 0{,}9332 - 0{,}1587 = 0{,}7745$.
- e) $z = 2$ : $1 - \Phi(2) = 1 - 0{,}9772 = 0{,}0228$.
- f) La table : $\Phi(2{,}33) = 0{,}9901$, donc $t = 30 + 2{,}33 \times 4 = 39{,}32$ minutes.
- g) De 25 à 35, $z$ de $-1{,}25$ à $1{,}25$ : $2\Phi(1{,}25) - 1 = 2 \times 0{,}8944 - 1 = 0{,}7888$, soit 0,789.
- h) $Y \sim \mathcal{N}(31, 2^2)$ : $z = \frac{34 - 31}{2} = 1{,}5$, et $1 - \Phi(1{,}5) = 0{,}0668$.

Pour la copie : partir 34 minutes avant, c'est arriver à l'heure si la durée est au plus 34 : $P(X \le 34) = \Phi(1) = 0{,}8413$ contre $P(Y \le 34) = 0{,}9332$ : on prend $Y$, plus lent en moyenne mais plus régulier. Avec 28 minutes : $P(X \le 28) = \Phi(-0{,}5) = 0{,}3085$ contre $P(Y \le 28) = \Phi(-1{,}5) = 0{,}0668$ : on prend $X$. Quand le temps disponible est sous la moyenne, seule une grande dispersion laisse une chance d'arriver à l'heure ; quand il est au-dessus, la régularité protège du retard.

**Erreurs fréquentes.** Diviser par la variance 16 au lieu de l'écart-type 4 ; écrire $\Phi(-1) = -0{,}8413$ ; en e, oublier « $1 -$ » ; en f, donner $z$ au lieu de la durée ; en h, prendre $\sigma = 4$.

**Variante.** $P(X > 30)$ ? *Réponse* : $1 - \Phi(0) = 0{,}5$.

### Ex M02b.6 — Espérance et variance d'une variable continue (théorème de transfert)

**Réponses** : a) `"3/4"` · b) `"1/3"` · c) `"1/6"` · d) `"1/18"` · e) `"11/3"` · f) `"25/18"` · g) `1.4366` · h) `True`.

**Démarche.** D'abord, $f \ge 0$ sur $[0 ; 1]$ et $\int_0^1 2(1 - x)\,dx = \big[2x - x^2\big]_0^1 = 1$ : c'est une densité.
- a) $\big[2x - x^2\big]_0^{1/2} = 1 - \frac{1}{4} = \frac{3}{4}$.
- b) $\int_0^1 (2x - 2x^2)\,dx = 1 - \frac{2}{3} = \frac{1}{3}$.
- c) $\int_0^1 (2x^2 - 2x^3)\,dx = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}$.
- d) $\frac{1}{6} - \frac{1}{9} = \frac{1}{18}$.
- e) $5 \times \frac{1}{3} + 2 = \frac{11}{3}$. f) $25 \times \frac{1}{18} = \frac{25}{18}$.
- g) Par parties, $u = 1 - x$, $v' = e^x$ : $\int (1 - x)e^x\,dx = (1 - x)e^x + \int e^x\,dx = (2 - x)e^x$. Donc $\mathbb{E}[e^X] = 2\big[(2 - x)e^x\big]_0^1 = 2(e - 2) = 2e - 4 \approx 1{,}4366$.
- h) $e^{1/3} \approx 1{,}3956 < 1{,}4366$ : **vrai**.

Pour la copie : la médiane vérifie $2m - m^2 = \frac{1}{2}$, soit $m = 1 - \frac{1}{\sqrt{2}} \approx 0{,}293$, sous l'espérance $\frac{1}{3}$ (la queue de droite tire l'espérance). $\mathbb{E}[X^2] = \frac{1}{6} > \mathbb{E}[X]^2 = \frac{1}{9}$ : pour la fonction carré comme pour l'exponentielle, $g(\mathbb{E}[X]) \le \mathbb{E}[g(X)]$. C'est l'**inégalité de Jensen**, vraie pour toute fonction convexe (M05).

**Erreurs fréquentes.** Répondre $\frac{1}{2}$ en b, comme si $X$ était uniforme ; prendre $\mathbb{E}[X]^2$ pour $\mathbb{E}[X^2]$ ; en f, garder le + 2 ou ne pas élever 5 au carré ; en g, oublier le facteur 2 de la densité ($e - 2$).

**Variante.** $\mathbb{E}[1 - X]$ ? *Réponse* : $1 - \frac{1}{3} = \frac{2}{3}$.

### Ex M02b.7 — Un couple de variables discrètes : loi jointe, marginales, indépendance

**Réponses** : a) `0.8` · b) `[0.2, 0.4, 0.4]` · c) `1.2` · d) `1.95` · e) `1.8` · f) `False` · g) `0.21` · h) `True`.

**Démarche.**
- b) Les colonnes : $0{,}15 + 0{,}05 = 0{,}2$ ; $0{,}25 + 0{,}15 = 0{,}4$ ; $0{,}10 + 0{,}30 = 0{,}4$. a) $1 - 0{,}2 = 0{,}8$.
- c) $0 \times 0{,}2 + 1 \times 0{,}4 + 2 \times 0{,}4 = 1{,}2$.
- d) $1 \times (1 \times 0{,}25 + 2 \times 0{,}10) + 2 \times (1 \times 0{,}15 + 2 \times 0{,}30) = 0{,}45 + 1{,}5 = 1{,}95$ (les cases $y = 0$ comptent pour 0).
- e) Les lignes donnent $P(X = 1) = P(X = 2) = 0{,}5$, donc $\mathbb{E}[X] = 1{,}5$, et $1{,}5 \times 1{,}2 = 1{,}8$.
- f) $P(X = 1, Y = 0) = 0{,}15 \ne 0{,}5 \times 0{,}2 = 0{,}1$ : dépendantes (et d ≠ e le confirme).
- g) $0{,}7 \times 0{,}3 = 0{,}21$.
- h) La dernière case vaut $1 - 0{,}12 - 0{,}28 - 0{,}18 = 0{,}42$. Marginales : $P(U = 0) = 0{,}4$, $P(U = 1) = 0{,}6$, $P(V = 0) = 0{,}3$, $P(V = 1) = 0{,}7$ ; les quatre produits redonnent 0,12 ; 0,28 ; 0,18 ; 0,42 : indépendantes.

Pour la copie : n'importe quelle case suffit, par exemple $P(X = 2, Y = 2) = 0{,}30$ contre $0{,}5 \times 0{,}4 = 0{,}20$ : les utilisateurs à deux appareils se connectent plus souvent deux fois par jour qu'on ne l'attendrait si les deux grandeurs étaient sans lien. La loi jointe de $(X', Y')$ : ligne $X' = 1$ : 0,15 ; 0,09 ; 0,06 ; ligne $X' = 2$ : 0,35 ; 0,21 ; 0,14.

**Erreurs fréquentes.** En b, recopier une ligne au lieu de sommer les colonnes ; en c, la moyenne simple des valeurs (1) ; en f, conclure à l'indépendance après avoir vérifié une seule case qui marche ; en h, oublier de compléter la case manquante.

**Variante.** $\mathbb{E}[X'Y']$ ? *Réponse* : par indépendance, $\mathbb{E}[X']\,\mathbb{E}[Y'] = 1{,}7 \times 0{,}7 = 1{,}19$.

### Ex M02b.8 — Linéarité et variance d'une somme : sommes et moyennes de variables

**Réponses** : a) `20` · b) `9` · c) `3` · d) `4` · e) `2.828` · f) `7.071` · g) `0.1414` · h) `4`.

**Démarche.**
- a) $4 + 6 + 10 = 20$. b) $1^2 + 2^2 + 2^2 = 9$ (indépendance). c) $\sqrt{9} = 3$.
- d) $10 - 6 = 4$. e) $\mathbb{V}(T_3 - T_2) = 4 + 4 = 8$, $\sigma = \sqrt{8} = 2\sqrt{2} \approx 2{,}828$.
- f) $\mathbb{V} = 50 \times 1^2 = 50$, $\sigma = \sqrt{50} \approx 7{,}071$.
- g) La moyenne est la somme divisée par 50 : $\sigma = \frac{\sqrt{50}}{50} = \frac{1}{\sqrt{50}} \approx 0{,}1414$.
- h) $T_1 + T_1 = 2T_1$, de variance $4 \times 1 = 4$.

Pour la copie : deux exécutions **indépendantes** de la tâche 1 ont une durée totale de variance $1 + 1 = 2$ ; compter deux fois **la même** exécution donne 4 : les écarts ne se compensent jamais, ils s'additionnent toujours dans le même sens.

**Erreurs fréquentes.** Additionner les écarts-types (5) ; écrire $\mathbb{V}(T_3 - T_2) = 0$ ; en g, diviser l'écart-type par 50 au lieu de $\sqrt{50}$ (0,02) ; en h, répondre 2.

**Variante.** $\sigma(T_1 + T_2 - T_3)$ ? *Réponse* : $\sqrt{1 + 4 + 4} = 3$.

### Ex M02b.9 — Une intégrale double sur un rectangle, et une densité jointe

**Réponses** : a) `"9/2"` · b) `2.9525` · c) `"7/12"` · d) `"2/9"` · e) `"2*x"` · f) `"y**2/9"` · g) `True` · h) `"1/108"`.

**Démarche.**
- a) Un produit : $\int_0^1 x\,dx \times \int_0^3 y^2\,dy = \frac{1}{2} \times 9 = \frac{9}{2}$.
- b) $e^{x + y} = e^x e^y$ : $(e - 1)^2 \approx 2{,}9525$.
- c) En $x$ d'abord : $\int_0^1 (x^2 + xy)\,dx = \frac{1}{3} + \frac{y}{2}$, puis $\int_0^1 \big(\frac{1}{3} + \frac{y}{2}\big)dy = \frac{1}{3} + \frac{1}{4} = \frac{7}{12}$. En $y$ d'abord : $\int_0^1 (x^2 + xy)\,dy = x^2 + \frac{x}{2}$, puis $\frac{1}{3} + \frac{1}{4}$ : le même résultat.
- d) $c \times \frac{9}{2} = 1$, donc $c = \frac{2}{9}$.
- e) $f_X(x) = \frac{2}{9}x\int_0^3 y^2\,dy = \frac{2}{9} \times 9x = 2x$. f) $f_Y(y) = \frac{2}{9}y^2\int_0^1 x\,dx = \frac{y^2}{9}$.
- g) $2x \times \frac{y^2}{9} = \frac{2}{9}xy^2 = f(x, y)$ : indépendantes.
- h) $\int_0^{1/2} 2x\,dx \times \int_0^1 \frac{y^2}{9}\,dy = \frac{1}{4} \times \frac{1}{27} = \frac{1}{108}$.

**Erreurs fréquentes.** En a, oublier le facteur $\frac{1}{2}$ ; en c, s'arrêter après la première intégrale ($\frac{1}{3} + \frac{y}{2}$ n'est pas un nombre) ; en e, oublier la constante $c$ ; en h, ne garder qu'un des deux facteurs.

**Variante.** $P\big(X \le \frac{1}{2}\big)$ ? *Réponse* : $\int_0^{1/2} 2x\,dx = \frac{1}{4}$.

### Ex M02b.10 — Changement de variable : la loi de aX + b, et celle de X²

**Réponses** : a) `"[-1 ; 5]"` · b) `"1/6"` · c) `"1/2"` · d) `0.0665` · e) `"2/3"` · f) `"sqrt(y)/3"` · g) `"1/(6*sqrt(y))"` · h) `3`.

**Démarche.**
- a) $X$ va de 0 à 2, donc $3X - 1$ de $-1$ à 5.
- b) $f_Y(y) = \frac{1}{3}f_X\big(\frac{y + 1}{3}\big) = \frac{1}{3} \times \frac{1}{2} = \frac{1}{6}$ : $Y$ est uniforme sur $[-1 ; 5]$ (largeur 6).
- c) $3X - 1 \le 2 \iff X \le 1$, et $P(X \le 1) = \frac{1}{2}$.
- d) $Y = 2X + 5$ suit $\mathcal{N}(2 \times 10 + 5, (2 \times 3)^2) = \mathcal{N}(25, 6^2)$ ; en son centre, sa densité vaut $\frac{1}{6\sqrt{2\pi}} \approx 0{,}0665$.
- e) $X \ge 0$, donc $X^2 \le 4 \iff X \le 2$ : $\frac{2}{3}$.
- f) $F_Y(y) = P(X \le \sqrt{y}) = \frac{\sqrt{y}}{3}$ pour $0 \le y \le 9$.
- g) $f_Y(y) = \frac{1}{3} \times \frac{1}{2\sqrt{y}} = \frac{1}{6\sqrt{y}}$.
- h) Avec g : $\int_0^9 y \times \frac{1}{6\sqrt{y}}\,dy = \frac{1}{6}\int_0^9 \sqrt{y}\,dy = \frac{1}{6} \times \frac{2}{3} \times 27 = 3$. Par transfert : $\int_0^3 x^2 \times \frac{1}{3}\,dx = \frac{27}{9} = 3$. Le transfert évite de chercher la loi de $Y$.

**Erreurs fréquentes.** En b, garder la densité $\frac{1}{2}$ de $X$ ou la multiplier par 3 ; en d, prendre l'écart-type 3 de $X$ ; en f, écrire $\frac{y}{9}$ (comme si $Y$ était uniforme sur $[0 ; 9]$) ; en g, une erreur de dérivée de $\sqrt{y}$.

**Variante.** $F_Y(y)$ pour $Y = 3X - 1$ et $-1 \le y \le 5$ ? *Réponse* : $\frac{y + 1}{6}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M02b.11 — La variance d'une somme de variables indépendantes

**Réponse modèle.**
1. Notons $\mu = \mathbb{E}[X]$, un nombre. $(X - \mu)^2 = X^2 - 2\mu X + \mu^2$, donc par linéarité $\mathbb{V}(X) = \mathbb{E}[X^2] - 2\mu\,\mathbb{E}[X] + \mu^2 = \mathbb{E}[X^2] - 2\mu^2 + \mu^2 = \mathbb{E}[X^2] - \mu^2$.
2. Par le théorème de transfert pour un couple, $\mathbb{E}[XY] = \sum_x\sum_y xy\,P(X = x, Y = y)$. L'indépendance donne $P(X = x, Y = y) = P(X = x)\,P(Y = y)$, donc $\mathbb{E}[XY] = \sum_x x\,P(X = x)\left(\sum_y y\,P(Y = y)\right) = \sum_x x\,P(X = x)\,\mathbb{E}[Y] = \mathbb{E}[X]\,\mathbb{E}[Y]$.
3. Posons $A = X - \mathbb{E}[X]$ et $B = Y - \mathbb{E}[Y]$ ; alors $X + Y - \mathbb{E}[X + Y] = A + B$, et $\mathbb{V}(X + Y) = \mathbb{E}[(A + B)^2] = \mathbb{E}[A^2] + \mathbb{E}[B^2] + 2\,\mathbb{E}[AB]$. Or $\mathbb{E}[A^2] = \mathbb{V}(X)$, $\mathbb{E}[B^2] = \mathbb{V}(Y)$, et $AB = XY - \mathbb{E}[Y]X - \mathbb{E}[X]Y + \mathbb{E}[X]\mathbb{E}[Y]$, d'espérance $\mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.
4. Si $X$ et $Y$ sont indépendantes, le dernier terme est nul par 2, d'où $\mathbb{V}(X + Y) = \mathbb{V}(X) + \mathbb{V}(Y)$. $-Y$ est indépendante de $X$ : $P(X = x, -Y = y) = P(X = x, Y = -y) = P(X = x)\,P(Y = -y) = P(X = x)\,P(-Y = y)$. Donc $\mathbb{V}(X - Y) = \mathbb{V}(X) + \mathbb{V}(-Y) = \mathbb{V}(X) + \mathbb{V}(Y)$, car $\mathbb{V}(-Y) = (-1)^2\,\mathbb{V}(Y)$.
5. Pour $n = 2$, c'est 4. Si la formule vaut au rang $n - 1$, on applique 4 à $S_{n-1} = X_1 + \cdots + X_{n-1}$ et $X_n$ (indépendantes, admis) : $\mathbb{V}(S_{n-1} + X_n) = \mathbb{V}(S_{n-1}) + \mathbb{V}(X_n) = \mathbb{V}(X_1) + \cdots + \mathbb{V}(X_n)$.
6. Une binomiale est la somme de $n$ indicatrices indépendantes de variance $p(1 - p)$ : $\mathbb{V}(X) = np(1 - p)$. Pour la moyenne : $\mathbb{V}(\bar{X}) = \frac{1}{n^2}\,\mathbb{V}(X_1 + \cdots + X_n) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$.
7. $X + Y = 2X$, de variance $4 \times \frac{1}{4} = 1$, alors que $\mathbb{V}(X) + \mathbb{V}(Y) = \frac{1}{2}$. Ici $\mathbb{E}[XY] = \mathbb{E}[X^2] = \frac{1}{2} \ne \frac{1}{4} = \mathbb{E}[X]\mathbb{E}[Y]$ : l'hypothèse d'indépendance manque (la variable est liée à elle-même).

**Grille.** Une bonne démonstration : (1) traite $\mathbb{E}[X]$ comme une constante dans la linéarité ; (2) factorise la double somme grâce à l'indépendance ; (3) développe le carré et identifie le terme croisé, sans supposer l'indépendance ; (4) conclut, et justifie que $-Y$ reste indépendante de $X$ ; (5) rédige la récurrence (initialisation, hérédité), en notant que $X_1, \ldots, X_{n-1}$ restent mutuellement indépendantes ; (6) applique aux indicatrices et à la moyenne ; (7) explique le contre-exemple par le terme croisé.

### Ex M02b.12 — L'intégrale de Gauss par une intégrale double (changement en coordonnées polaires admis)

**Réponse modèle.**
1. $g(x, y) = e^{-x^2}e^{-y^2}$, un produit : sur le carré $C_R$, $\iint_{C_R} g = \int_{-R}^R e^{-x^2}\,dx \times \int_{-R}^R e^{-y^2}\,dy = I(R)^2$ (fiche §7, le cas d'un produit).
2. En polaires, $x^2 + y^2 = r^2$ et $dx\,dy = r\,dr\,d\theta$ : $J(r) = \int_0^{2\pi}\left(\int_0^{r} e^{-s^2}s\,ds\right)d\theta = 2\pi\left[-\frac{1}{2}e^{-s^2}\right]_0^{r} = \pi\big(1 - e^{-r^2}\big)$.
3. Un point de $D_R$ est à une distance au plus $R$ de l'origine, donc ses deux coordonnées sont entre $-R$ et $R$ : il est dans $C_R$. Un point de $C_R$ a $x^2 + y^2 \le R^2 + R^2 = 2R^2$ : il est dans $D_{R\sqrt{2}}$ (le coin du carré est sur le cercle). Comme $g > 0$, $J(R) \le I(R)^2 \le J(R\sqrt{2})$, soit $\pi\big(1 - e^{-R^2}\big) \le I(R)^2 \le \pi\big(1 - e^{-2R^2}\big)$.
4. Les deux bornes tendent vers $\pi$ quand $R \to +\infty$ ; par encadrement (théorème des gendarmes, R5), $I(R)^2 \to \pi$. Or $I(R) \to I = \int_{-\infty}^{+\infty} e^{-x^2}\,dx$ (M02a §4), donc $I^2 = \pi$. Comme $I > 0$ (l'intégrale d'une fonction strictement positive), $I = \sqrt{\pi}$.
5. Avec $x = \frac{t}{\sqrt{2}}$, $dx = \frac{dt}{\sqrt{2}}$ et les bornes infinies restent infinies : $\int e^{-t^2/2}\,dt = \sqrt{2}\int e^{-x^2}\,dx = \sqrt{2\pi}$. Puis, avec $t = \frac{x - \mu}{\sigma}$ ($dx = \sigma\,dt$) : $\int \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x - \mu)^2}{2\sigma^2}}\,dx = \frac{1}{\sqrt{2\pi}}\int e^{-t^2/2}\,dt = 1$.
6. $h \ge 0$ et $\iint h = \frac{1}{2\pi}\left(\int e^{-x^2/2}\,dx\right)^2 = \frac{2\pi}{2\pi} = 1$. Et $h(x, y) = \varphi(x)\,\varphi(y)$ : les deux coordonnées sont **indépendantes** (fiche §7), chacune de loi $\mathcal{N}(0, 1)$. Cette densité ne dépend que de $r^2 = x^2 + y^2$ : la loi est invariante par rotation, l'angle est uniforme. C'est l'idée de la méthode de Box-Muller (M02b.27).

**Grille.** Une bonne démonstration : (1) passe d'un produit d'intégrales à une intégrale double sur le carré ; (2) calcule $J$ en polaires avec le facteur $r$, et trouve la primitive de $r\,e^{-r^2}$ ; (3) justifie les deux inclusions (le coin du carré), puis la comparaison des intégrales par la positivité ; (4) conclut par encadrement, en justifiant que $I(R)$ tend vers $I$ (l'intégrale impropre converge, par comparaison, M02a §4) et le signe de $I$ ; (5) enchaîne les deux changements de variable ; (6) reconnaît le produit de deux densités, donc l'indépendance.

### Ex M02b.13 — La loi de Poisson, limite de lois binomiales

**Réponse modèle.**
1. $P(X_n = k) = \binom{n}{k}\left(\frac{\lambda}{n}\right)^k\left(1 - \frac{\lambda}{n}\right)^{n-k}$, avec $\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}$ et $\left(1 - \frac{\lambda}{n}\right)^{n-k} = \left(1 - \frac{\lambda}{n}\right)^n\left(1 - \frac{\lambda}{n}\right)^{-k}$. En regroupant $\frac{n(n-1)\cdots(n-k+1)}{n^k}$, on obtient la formule.
2. $\frac{n(n-1)\cdots(n-k+1)}{n^k} = 1 \times \left(1 - \frac{1}{n}\right) \times \cdots \times \left(1 - \frac{k-1}{n}\right)$ : un produit de $k$ facteurs (un nombre fixe), qui tendent chacun vers 1. Le produit tend vers 1.
3. $\left(1 - \frac{\lambda}{n}\right)^n = \exp\big(n\ln(1 + h)\big)$ avec $h = -\frac{\lambda}{n} \to 0$, et $n\ln(1 + h) = -\lambda\,\frac{\ln(1 + h)}{h} \to -\lambda \times 1$. Par continuité de l'exponentielle, la puissance tend vers $e^{-\lambda}$.
4. $\left(1 - \frac{\lambda}{n}\right)^{-k} \to 1^{-k} = 1$ ($k$ est fixe). Donc $P(X_n = k) \to 1 \times \frac{\lambda^k}{k!} \times e^{-\lambda} \times 1 = e^{-\lambda}\frac{\lambda^k}{k!}$.
5. $P(X_n = 0) = \left(1 - \frac{2}{n}\right)^n$ : 0,10737 pour $n = 10$, 0,13262 pour $n = 100$, 0,13506 pour $n = 1\,000$, contre $e^{-2} \approx 0{,}13534$. Écarts : 0,0280 ; 0,0027 ; 0,00027 : divisés par 10 quand $n$ est multiplié par 10, comme $\frac{1}{n}$.
6. Sur une longue période découpée en beaucoup de petits intervalles, chacun contient rarement un événement, indépendamment des autres : c'est une binomiale de grand $n$ et de petit $p$, donc presque une loi de Poisson de paramètre $np$. Pour 10 lancers d'une pièce, $n = 10$ est petit et $p = \frac{1}{2}$ n'est pas petit : la loi est $\mathcal{B}(10 ; 0{,}5)$, que $\mathcal{P}(5)$ approche mal (elle donne une probabilité positive à 11 faces ou plus, et une variance de 5 au lieu de 2,5).

**Grille.** Une bonne démonstration : (1) écrit le coefficient binomial avec le produit descendant et sépare la puissance (avec $n > \lambda$, $1 - \frac{\lambda}{n} > 0$) ; (2) remarque que le nombre de facteurs est fixe ; (3) passe par le logarithme et la limite $\frac{\ln(1 + h)}{h} \to 1$ ; (4) assemble les quatre limites ; (5) fait le calcul numérique et lit la vitesse en $\frac{1}{n}$ ; (6) relie l'hypothèse « $n$ grand, $p$ petit » à la situation.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M02b.14 — Combien d'erreurs d'annotation dans un dataset ? Binomiale et Poisson

**Réponses** : a) `4` · b) `1.998` · c) `0.0182` · d) `0.0183` · e) `0.2381` · f) `0.6321` · g) `1152`.

**Démarche.** $X \sim \mathcal{B}(2\,000 ;\ 0{,}002)$, approchée par $\mathcal{P}(4)$.
- a) $np = 4$. b) $\sqrt{2\,000 \times 0{,}002 \times 0{,}998} = \sqrt{3{,}992} \approx 1{,}998$ (la loi de Poisson donnerait $\sqrt{4} = 2$ : presque pareil).
- c) $0{,}998^{2\,000} \approx 0{,}01824$. d) $e^{-4} \approx 0{,}01832$ : un écart de $7 \times 10^{-5}$.
- e) $e^{-4}\left(1 + 4 + \frac{4^2}{2}\right) = 13e^{-4} \approx 0{,}2381$ (la binomiale donne 0,2378).
- f) $Y \approx \mathcal{P}(500 \times 0{,}002) = \mathcal{P}(1)$ : $1 - e^{-1} \approx 0{,}6321$.
- g) $1 - e^{-0{,}002\,n} \ge 0{,}9 \iff n \ge \frac{\ln 10}{0{,}002} \approx 1\,151{,}3$, donc $n = 1\,152$ (la binomiale exacte, $0{,}998^n \le 0{,}1$, donne 1 151 : l'approximation coûte une image).

Pour la copie : $n$ est grand, $p$ petit et $np = 4$ modéré : la situation type de la loi des événements rares. Avec $p = 0{,}2$, $np = 400$ et la variance binomiale $np(1 - p) = 320$ n'est plus proche de 400 : l'approximation de Poisson ne vaut plus (on approchera alors par une loi normale, M02c). Des erreurs groupées violent l'**indépendance** (et la même probabilité pour chaque image) : la variance réelle du nombre d'erreurs devient plus grande que celle du modèle.

**Erreurs fréquentes.** En b, donner la variance ; échanger c et d ; en e, oublier $k = 0$ ou le $2!$ ; en f, prendre le paramètre 4 de $X$.

**Variante.** $P(X \ge 1)$ avec l'approximation de Poisson ? *Réponse* : $1 - e^{-4} \approx 0{,}9817$.

### Ex M02b.15 — MML §6.1 et §6.2 : espace probabilisé, pmf et pdf, en anglais

**Éléments de réponse** (ta formulation compte, pas la nôtre).
1. Deux lectures : la probabilité comme **degré de croyance** d'un agent face à l'incertitude (lecture dite bayésienne), et comme **fréquence relative** d'un événement sur un très grand nombre de répétitions (lecture fréquentiste). Exemples : « je crois à 70 % qu'il pleuvra demain » ; « une pièce tombe sur pile une fois sur deux sur des milliers de lancers ».
2. L'univers (*sample space*), l'ensemble des événements (*event space*) et la probabilité (*probability*). Le livre ajoute l'ensemble d'arrivée d'une variable aléatoire, le *target space* $\mathcal{T}$.
3. Une *random variable* n'est ni aléatoire ni une variable : c'est une **fonction** (déterministe) des issues vers $\mathcal{T}$. Le hasard est dans le choix de l'issue, pas dans la fonction (fiche §1).
4. $\Omega = \{PP, PF, FP, FF\}$, quatre issues équiprobables ; $X(PP) = 0$, $X(PF) = X(FP) = 1$, $X(FF) = 2$. La loi : $P(X = 0) = \frac{1}{4}$, $P(X = 1) = \frac{1}{2}$, $P(X = 2) = \frac{1}{4}$ (c'est $\mathcal{B}(2 ; 0{,}5)$).
5. On divise chaque comptage $n_{ij}$ par le total $N$ pour obtenir la loi jointe ; les marginales sont les sommes des lignes et des colonnes divisées par $N$ (la règle de la somme). Le tableau du stand de glaces est déjà divisé par $N$.
6. *pmf* (fonction de masse), *pdf* (densité), *cdf* (fonction de répartition). Le livre écrit $p(x)$ dans les deux cas, pour alléger, en laissant le contexte dire s'il s'agit d'une probabilité ou d'une densité (fiche §1 et M02a).
7. Personnel. Mots fréquents : *outcome* (issue), *event* (événement), *state* (valeur possible), *joint probability*, *marginal probability*, *quantity of interest*.

### Ex M02b.16 — MML §6.4 et §6.7 : espérance, variance, sommes de variables, changement de variable

**Éléments de réponse.**
1. Le livre définit l'espérance d'une **fonction** $g$ de la variable : une somme pondérée (discret) ou une intégrale contre la densité (continu). Prendre $g(x) = x$ donne la moyenne ; prendre une autre $g$, c'est exactement le théorème de transfert, sans passer par la loi de $g(X)$.
2. La **médiane** et le **mode** (la valeur de plus grande probabilité, ou le maximum de la densité). Pour $\mathcal{E}(3)$ : moyenne $\frac{1}{3}$, médiane $\frac{\ln 2}{3} \approx 0{,}231$, mode 0 (la densité est maximale en 0).
3. La définition $\mathbb{E}[(X - \mu)^2]$ et la formule $\mathbb{E}[X^2] - \mathbb{E}[X]^2$ (la troisième, avec les écarts deux à deux, n'est pas dans la fiche). La seconde soustrait deux grands nombres presque égaux quand la moyenne est grande devant l'écart-type : un ordinateur, qui ne garde qu'environ 16 chiffres, perd alors presque tous les chiffres significatifs du résultat (une erreur d'annulation). On préfère calculer la moyenne d'abord, puis la moyenne des écarts au carré.
4. $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ ; $\mathbb{V}[X + Y] = \mathbb{V}[X] + \mathbb{V}[Y]$ plus deux termes de covariance (fiche §6). Pour des variables indépendantes, les covariances sont nulles et les variances s'additionnent.
5. $F_Y(y) = P(\sqrt{X} \le y) = P(X \le y^2) = y^2$ pour $y$ dans $[0 ; 1]$, donc $f_Y(y) = 2y$.
6. Si $F$ est continue et strictement croissante, $F(X)$ suit la loi uniforme sur $[0 ; 1]$. En sens inverse : partir d'une uniforme $U$ et appliquer $F^{-1}$ donne une variable de loi $F$, la simulation par inversion.
7. $f_Y(y) = f_X\big(g^{-1}(y)\big)\,\big\lvert (g^{-1})'(y) \big\rvert$. Ici $g(x) = \sqrt{x}$, $g^{-1}(y) = y^2$, $(g^{-1})'(y) = 2y$, et $f_X = 1$ sur $[0 ; 1]$ : $f_Y(y) = 1 \times 2y = 2y$, comme en 5.

### Ex M02b.17 — Expliquer la différence entre une variable aléatoire et sa loi

**Exemple de réponse.**

> Une variable aléatoire, c'est une règle qui associe un nombre à chaque résultat possible d'une expérience : une fonction des résultats vers les nombres. Par exemple, « la taille de la personne qu'on va tirer au hasard ». Sa loi, c'est seulement la répartition des chances : quelle proportion de tirages tombe entre 1,60 m et 1,70 m, entre 1,70 m et 1,80 m… Un tirage, c'est une valeur obtenue une fois, comme 1,74 m. « $X$ et $Y$ suivent la même loi normale » veut dire qu'elles ont les mêmes chances pour chaque intervalle, pas qu'elles sont égales : si $X$ est la taille de la première personne tirée et $Y$ celle de la seconde, elles ont la même loi, mais presque jamais la même valeur. Même avec une pièce : « pile » et « face » (codés 1 et 0) ont la même loi, et ne sont jamais égaux en même temps.

**Grille.** Une bonne réponse : (1) une variable aléatoire est une fonction des issues vers les nombres ; (2) la loi décrit les chances de chaque valeur ou intervalle ; (3) un tirage est une valeur réalisée ; (4) même loi ne veut pas dire égales, avec un exemple ; (5) huit lignes au plus, sans formule compliquée.

<a id="entretien"></a>

## 💼 Entretien

### M02b.E1 — Quand modéliser un comptage par une loi de Poisson ?

**Réponse modèle (60 secondes).**

> Une loi de Poisson est un bon premier modèle si les requêtes arrivent une par une, indépendamment les unes des autres, à un rythme moyen constant sur la période regardée : c'est la loi des événements rares, la limite d'une binomiale avec beaucoup d'utilisateurs qui ont chacun une petite probabilité d'envoyer une requête dans la minute. Son paramètre unique, $\lambda$, est le nombre moyen par minute, et sa variance vaut aussi $\lambda$. D'où un test simple : sur des données, je compare la moyenne et la variance des comptages par minute. Si la variance est nettement plus grande, on parle de surdispersion, et la loi de Poisson ne convient pas. Deux cas typiques : des rafales (un robot, une campagne publicitaire, des relances automatiques après une panne), qui cassent l'indépendance, et un rythme qui change dans la journée, qui casse la constance ; on découpe alors par heure, ou l'on prend une loi plus souple comme la binomiale négative. Je regarderais aussi l'histogramme des comptages contre les probabilités de Poisson, et les durées entre requêtes, qui devraient suivre une loi exponentielle.

**Grille.** (1) les trois hypothèses (un par un, indépendants, rythme constant) ; (2) $\lambda$ = le nombre moyen, espérance = variance ; (3) le test moyenne/variance sur des données (surdispersion) ; (4) deux contre-exemples (rafales, rythme variable) ; (5) un prolongement : durées exponentielles, ou une autre loi.

<a id="notebook"></a>

## Notebook

### Ex M02b.18 — Lois binomiale et de Poisson · `binomial_pmf`, `poisson_pmf`

**Réponses** : a) `0.266828` · b) `1.0` · c) `0.0` · d) `"ValueError"` · e) `0.133602` · f) `1.0` · g) `"float"` · h) `6.5`.

**Démarche.** `binomial_pmf` : d'abord les paramètres impossibles (`n < 0`, `p` hors de $[0 ; 1]$ : `raise ValueError(...)`), puis les valeurs de `k` impossibles (`return 0.0`), puis `float(math.comb(n, k) * p ** k * (1 - p) ** (n - k))`. `poisson_pmf` : `lam < 0` lève l'erreur, `k < 0` rend 0.0, sinon `float(math.exp(-lam) * lam ** k / math.factorial(k))` ; en Python `0 ** 0 == 1`, ce qui donne f sans cas particulier. Pour la copie : b) vérifie que les probabilités ont une somme de 1, et h) que l'espérance vaut $\lambda$ ; au-delà de $k = 100$, les termes de $\mathcal{P}(6{,}5)$ sont inférieurs à $10^{-70}$.

**Erreurs fréquentes.** Lever une erreur pour `k > n` au lieu de rendre 0.0 ; `math.comb(n, k)` avec `k < 0` lève une `ValueError` qu'on n'a pas voulue ; oublier `/ math.factorial(k)` ; renvoyer un `np.float64` (avec `np.exp`).

### Ex M02b.19 — Densité et fonction de répartition de la loi normale (avec `math.erf`) · `normal_pdf`, `normal_cdf`

**Réponses** : a) `0.241971` · b) `1.9947` · c) `0.9332` · d) `0.0668` · e) `0.3023` · f) `"ValueError"` · g) `"float"` · h) `0.31225`.

**Démarche.** Tester `sigma <= 0` d'abord, puis standardiser, `z = (x - mu) / sigma` : `math.exp(-z * z / 2) / (sigma * math.sqrt(2 * math.pi))` et `(1 + math.erf(z / math.sqrt(2))) / 2`. Pour la copie : b) dépasse 1, et ce n'est pas une erreur (une cloche étroite est haute). h) approche $\varphi(0{,}7) \approx 0{,}312254$ : la dérivée de la fonction de répartition est la densité (M02a §7).

**Erreurs fréquentes.** Mettre $\sigma^2$ au dénominateur du facteur ; oublier $\sqrt{2}$ dans `erf` (c donne alors 0,9831) ; standardiser par la variance ; laisser `sigma = 0` provoquer une `ZeroDivisionError`.

### Ex M02b.20 — Simuler par inversion de la fonction de répartition · `inverse_transform_sample`

**Réponses** : a) `6.369617` · b) `0.3328` · c) `4995` · d) `"ValueError"` · e) `5.0` · f) `0.2` · g) `"float64"` · h) `0.856492`.

**Démarche.** `if n < 1: raise ValueError(...)`, puis `uniforms = np.random.default_rng(seed).random(n)` et `np.array([float(inverse_cdf(float(u))) for u in uniforms], dtype=float)`. Pour la copie : b) 0,3328 pour $\frac{1}{3}$, c) 4 995 pour $100\,000\,e^{-3} \approx 4\,979$, f) 0,200 : l'aléa de quelques millièmes attendu avec 100 000 ou 50 000 tirages. Pour la loi géométrique : $\ln(1 - p) < 0$, donc $\left\lceil \frac{\ln(1 - U)}{\ln(1 - p)} \right\rceil > k \iff \frac{\ln(1 - U)}{\ln(1 - p)} > k \iff \ln(1 - U) < k\ln(1 - p) \iff 1 - U < (1 - p)^k$, de probabilité $(1 - p)^k$ puisque $1 - U$ est uniforme : c'est $P(X > k)$.

**Erreurs fréquentes.** Appeler `inverse_cdf(uniforms)` sur tout l'array (cela marche pour `10 * u`, mais `math.log` refuse un array) ; créer un générateur sans la graine reçue ; renvoyer une liste ; un array d'entiers pour la loi géométrique.

### Ex M02b.21 — `scipy.stats` : pmf, pdf, cdf, ppf et rvs

**Réponses** : a) `0.2428` · b) `0.1736` · c) `0.9772` · d) `119.22` · e) `0.5` · f) `1.96` · g) `4.4493` · h) `3.0`.

**Démarche.** a) `stats.binom(20, 0.15).pmf(3)` ; b) `stats.poisson(4.5).cdf(2)` ; c) `stats.norm(100, 15).cdf(130)` ($\Phi(2)$) ; d) `stats.norm(100, 15).ppf(0.9)` ; e) `stats.expon(scale=1/2).mean()` ; f) `stats.norm().ppf(0.975)` ; g) `stats.poisson(4.5).rvs(size=10_000, random_state=0).mean()` ; h) `stats.uniform(loc=2, scale=6).var()`. Pour la copie : e) $\frac{1}{\lambda}$ et h) $\frac{(b - a)^2}{12}$ (fiche §4) ; d) avec la table : $100 + 1{,}2816 \times 15 \approx 119{,}22$.

**Erreurs fréquentes.** `stats.expon(2)` : le premier argument est `loc`, un décalage (espérance 3) ; `stats.uniform(2, 8)` couvre $[2 ; 10]$, car le second argument est la largeur `scale` ; `stats.norm(100, 225)` (la variance au lieu de l'écart-type) ; `cdf` à la place de `ppf` pour un percentile.

### Ex M02b.22 — Prédire : la variance de la moyenne de quatre dés

**Réponses** : a) `3` · b) `2` · c) `3` · d) `4`.

**Démarche.** Un dé à 8 faces : $\mathbb{V} = \frac{8^2 - 1}{12} = 5{,}25$. a) $\mathbb{V}(\bar{X}) = \frac{5{,}25}{4}$ : divisée par 4. b) Écart-type divisé par $\sqrt{4} = 2$. c) $\mathbb{V}(S) = 4 \times 5{,}25$ : multipliée par 4. d) $\mathbb{V}(4X) = 16 \times 5{,}25$ : multipliée par 16. Pour la copie : la somme de quatre dés et 4 fois un dé ont la même espérance, 18, mais les quatre dés indépendants compensent en partie leurs écarts, alors qu'un seul dé multiplié par 4 amplifie chacun de ses écarts.

**Erreurs fréquentes.** Croire que la moyenne garde la variance d'un dé ; confondre c et d (somme de copies indépendantes et multiple d'une seule variable).

### Ex M02b.23 — Binomiale et Poisson côte à côte quand n grandit

**Réponses** : a) `0.0428` · b) `0.00034` · c) `10.2` · d) `100`.

**Démarche.** `gap(n)` : `ks = np.arange(n + 1)`, puis `np.max(np.abs(stats.binom(n, LAM / n).pmf(ks) - stats.poisson(LAM).pmf(ks)))`. Les écarts valent environ 0,12 ; 0,043 ; 0,012 ; 0,0034 ; 0,00034. Pour la copie : une pente de $-1$ en échelles logarithmiques, l'écart diminue comme $\frac{1}{n}$ (c'est-à-dire comme $p$) ; avec $n = 100$, l'écart est déjà sous $\frac{1}{200}$, assez pour 2 décimales.

**Erreurs fréquentes.** Prendre $p = 3$ au lieu de $\frac{3}{n}$ ; comparer les lois sur des $k$ différents ; une échelle linéaire, qui écrase les petits écarts.

### Ex M02b.24 — Une loi jointe en carte de chaleur, ses marginales sur les bords

**Réponse** : `0.0378`.

**Démarche.** `marginals` : `joint.sum(axis=1), joint.sum(axis=0)`. `draw_joint` : `ax.imshow(joint.T, origin="lower", cmap="Blues")`, `ax_top.bar(...)` des marginales des lignes, `ax_right.barh(...)` de celles des colonnes. `max_gap_24 = np.max(np.abs(JOINT_24 - np.outer(p_min, p_max)))`. Pour la copie : la moitié sous la diagonale est vide (le plus petit numéro ne dépasse jamais le plus grand) ; la diagonale vaut $\frac{1}{36}$ (un seul couple, les deux dés égaux), les cases au-dessus $\frac{2}{36}$ (deux couples). Les variables sont dépendantes : une case vide, comme $P(X = 6, Y = 1) = 0$, le montre sans calcul, puisque le produit de ses marginales est positif.

**Erreurs fréquentes.** Échanger `axis=0` et `axis=1` ; dessiner `joint` au lieu de `joint.T` (les axes sont alors inversés) ; ouvrir une nouvelle figure dans `draw_joint`.

### Ex M02b.25 — Chasse à l'erreur : une densité prise pour une probabilité, σ et σ²

**Réponses** : a) `"ABD"` · b) `[3.9894, 0.8413, 1.1547, 0.0, 5.0]`.

**Démarche.** (A) La valeur $\frac{1}{0{,}1\sqrt{2\pi}} \approx 3{,}9894$ est juste ; la conclusion est fausse : une densité n'est pas une probabilité. (B) $\mathcal{N}(5, 4)$ a pour écart-type 2 : $\Phi(1) \approx 0{,}8413$. (D) $P(T = 1) = 0$ pour une variable à densité. (C) $\sqrt{\frac{16}{12}} \approx 1{,}1547$ et (E) $\sqrt{9 + 16} = 5$ sont justes.

**Erreurs fréquentes.** Accuser (E), où les variances s'additionnent bien ; donner pour (A) la valeur 0 (la valeur était juste) ; garder $f(1)$ pour (D).

### Ex M02b.26 — Documenter une loi : docstring et exemples testés (`doctest`)

**Démarche.** La fonction : `if not 0 < p <= 1: raise ValueError("p must be in ]0, 1]")`, `if k < 1: return 0.0`, puis `float((1 - p) ** (k - 1) * p)`. La docstring : un résumé, puis `Parameters`, `Returns`, `Raises`, `Examples`, avec des exemples à résultat exact (`geometric_pmf(3, 0.5)` affiche `0.125`), le cas `k = 0`, et l'exemple de l'erreur avec `Traceback (most recent call last):`, `...` et la ligne `ValueError: p must be in ]0, 1]`. Pour la copie : un exemple non testé dérive quand la fonction change ; `doctest` compare des **textes**, et un flottant comme `0.09000000000000001` ferait échouer l'exemple, d'où `round(..., 4)`.

**Erreurs fréquentes.** Un message d'erreur différent dans l'exemple et dans le `raise` ; un exemple qui affiche 17 chiffres ; oublier une section de la docstring.

### Ex M02b.27 — Défi : tirer des valeurs normales avec seulement des tirages uniformes

**Démarche.** La méthode de **Box-Muller** : avec $m = \lceil n/2 \rceil$ paires d'uniformes, `radius = np.sqrt(-2 * np.log(1 - rng.random(m)))` et `angle = 2 * np.pi * rng.random(m)`, puis `np.concatenate([radius * np.cos(angle), radius * np.sin(angle)])[:n]`. Pourquoi : la densité jointe de deux normales indépendantes, $\frac{1}{2\pi}e^{-r^2/2}$, ne dépend que de $r$ (M02b.12) ; l'angle est uniforme, et $P(R^2 > t) = e^{-t/2}$ : $R^2$ suit la loi exponentielle d'espérance 2, qu'on tire par inversion (fiche §8). Pour la copie : la somme de 12 uniformes moins 6 a l'espérance 0 et la variance 1, et passe souvent le test de Kolmogorov-Smirnov, mais elle ne dépasse jamais 6 et ses queues sont trop minces (environ $1{,}4 \times 10^{-5}$ au-delà de 4 au lieu de $6{,}3 \times 10^{-5}$).

**Erreurs fréquentes.** Utiliser le même uniforme pour le rayon et l'angle (les deux normales ne sont plus indépendantes) ; `np.log(rng.random(m))` peut valoir $-\infty$ si un uniforme vaut exactement 0 (`1 - u` l'évite) ; une boucle Python sur un million de valeurs (trop lente).
