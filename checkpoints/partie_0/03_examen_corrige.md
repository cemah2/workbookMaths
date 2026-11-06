# CP0 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Barème par sous-question**, entre crochets ; sauf mention contraire, une sous-question vaut 0,25 point.
- **Crédit partiel** sur une sous-question de 0,25 point : 0,1 pour une réponse juste sans la démarche demandée, pour une méthode juste avec une erreur de calcul, ou pour une valeur approchée là où une valeur exacte est demandée (une fraction, `ln`, une racine) ; 0,2 pour une fraction juste mais non simplifiée. **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois.
- **Arrondis** : une décimale de trop ou de moins coûte au plus 0,05 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi.
- **Questions rédigées** (CP0.Q1, CP0.9, CP0.10 b) : les critères sont listés ; une idée juste formulée autrement compte autant.
- **Écriture de `ln`** : le logarithme népérien s'écrit `ln` (ou `log`, comme en Python) dans le notebook ; au lycée, $\log$ seul désigne souvent $\log_{10}$, d'où $\ln$ partout ici.

---

## CP0.Q1 — Dix affirmations sur toute la remise à niveau 🧠 · 2,5 points

Chaque affirmation : **[0,1]** pour le verdict, **[0,15]** pour une justification juste (0,05 si elle est incomplète).

**a) Faux** (R1). Un quotient de puissances d'un même nombre **soustrait** les exposants : $\frac{2^{10}}{2^5} = 2^{10 - 5} = 2^5 = 32$, et non $2^{10 \div 5} = 2^2$.

**b) Vrai** (R2). En retranchant $2x$ des deux membres, on obtient $3 = 5$, qui est faux quel que soit $x$ : aucune valeur ne convient (les droites $y = 2x + 3$ et $y = 2x + 5$ sont parallèles).

**c) Vrai** (R3). Si $a < b$, alors $f(a) < f(b)$, donc $f(a) \ne f(b)$ : deux nombres différents n'ont jamais la même image. C'est pour cela qu'une telle fonction a une réciproque.

**d) Vrai** (R4). La négation de « pour tout $n$, $P(n)$ » est « il existe $n$ tel que non $P(n)$ » : un seul $n$ pour lequel $P(n)$ est faux la démontre. (Pour montrer qu'une telle affirmation est **vraie**, en revanche, des exemples ne suffisent jamais.)

**e) Vrai** (R5). $u_n = u_0 + nr$ avec $r < 0$ : $nr$ tend vers $-\infty$, donc $u_n$ aussi.

**f) Vrai** (R6). $\ln(e^a) = a$ pour tout réel $a$ : $3 + (-3) = 0$. Ou : $\ln(e^3) + \ln(e^{-3}) = \ln(e^3 \times e^{-3}) = \ln 1 = 0$.

**g) Vrai** (R7). Une dérivée strictement positive sur un intervalle rend $f$ strictement croissante sur cet intervalle ; comme $0 < 1$, $f(0) < f(1)$.

**h) Faux** (R8). Sans remise, le contenu de l'urne change après le premier tirage : la probabilité du second dépend du résultat du premier. Exemple : avec une boule rouge et une bleue, $P(\text{rouge au 2ᵉ}) = \frac{1}{2}$, mais $P(\text{rouge au 2ᵉ} \mid \text{rouge au 1ᵉʳ}) = 0$.

**i) Faux** (R9). Le cosinus est l'abscisse du point du cercle trigonométrique : il est négatif entre $\frac{\pi}{2}$ et $\pi$. Contre-exemple : $\cos\pi = -1$.

**j) Vrai** (R8). $\mathbb{E}[X] = \frac{0 + 10}{2} = 5$ ; $\mathbb{E}[X^2] = \frac{0 + 100}{2} = 50$, donc $\mathbb{V}(X) = 50 - 25 = 25$ (les deux valeurs sont à 5 de la moyenne : l'écart-type vaut 5).

**Erreurs fréquentes** : en a), diviser les exposants ; en b), répondre « une infinité » parce que les deux membres se ressemblent ; en d), croire qu'il faut une démonstration générale pour réfuter ; en h), croire que des tirages « successifs » sont toujours indépendants ; en i), confondre $[0 ; \pi]$ et $\left[0 ; \frac{\pi}{2}\right]$.
**Remédiation** : a) R1.7 ; b) R2.5, R2.15 ; c) R3.10 ; d) R4.3, R4.8 ; e) R5.2 ; f) R6.2 ; g) R7.8 ; h) R8.7 ; i) R9.7, R9.8 ; j) R8.9.

## CP0.1 — Fractions, puissances et notation scientifique ✏️ · 1,25 point

**Réponses** : a) `"-1/8"` · b) `"1/5"` · c) `[2.8, 4]` · d) `[6, 3]` · e) `-10`.

a) La division d'abord : $\frac{5}{6} \div \frac{4}{9} = \frac{5}{6} \times \frac{9}{4} = \frac{45}{24} = \frac{15}{8}$, puis $\frac{7}{4} - \frac{15}{8} = \frac{14}{8} - \frac{15}{8} = -\frac{1}{8}$. **[0,25]**
b) Tout en puissances de 5 : $25^{-3} = (5^2)^{-3} = 5^{-6}$, donc $\frac{5^4 \times 5^{-6}}{5^{-1}} = 5^{4 - 6 - (-1)} = 5^{-1} = \frac{1}{5}$. **[0,25]**
c) $4 \times 7 = 28$ et $10^{-5} \times 10^{8} = 10^{3}$ : $28 \times 10^3 = 2{,}8 \times 10^4$. **[0,25]** (0,15 pour $28 \times 10^3$, juste mais pas en notation scientifique)
d) $\frac{9}{1{,}5} = 6$ et $\frac{10^{-4}}{10^{-7}} = 10^{-4 - (-7)} = 10^{3}$ : $6 \times 10^{3}$. **[0,25]**
e) Les coefficients se multiplient : $1{,}2 \times 0{,}75 = 0{,}9$, soit une baisse de 10 %. **[0,25]**

**Erreurs fréquentes** : en a), soustraire avant de diviser ($\frac{33}{16}$) ; en b), lire $25^{-3}$ comme $5^{-3}$ ; en c), laisser $28 \times 10^3$ ; en d), $10^{-11}$ (le signe de $-(-7)$ perdu) ou $10^{-3}$ (la soustraction à l'envers) ; en e), additionner les pourcentages ($-5$ %), ou donner le coefficient 0,9.
**Remédiation** : R1.2, R1.5, R1.7, R1.8, R1.10, R1.12.

## CP0.2 — Développer, factoriser, résoudre ✏️ · 1,25 point

**Réponses** : a) `"8*x**2 + 2*x - 5"` · b) `[0, 7]` · c) `"-3/8"` · d) `"]-oo ; -3["` · e) `"[-1 ; 7]"`.

a) $(3x - 2)(3x + 2) = 9x^2 - 4$ (identité $(a - b)(a + b) = a^2 - b^2$) et $(x - 1)^2 = x^2 - 2x + 1$ ; le signe moins s'applique à toute la parenthèse : $9x^2 - 4 - x^2 + 2x - 1 = 8x^2 + 2x - 5$. **[0,25]**
b) $x^2 - 7x = 0$, soit $x(x - 7) = 0$ : un produit est nul quand l'un de ses facteurs l'est, donc $x = 0$ ou $x = 7$. **[0,25]** (0,1 pour la seule solution 7)
c) $4 - 6x + 3 = 2x + 10$, soit $7 - 6x = 2x + 10$, donc $-3 = 8x$ et $x = -\frac{3}{8}$. **[0,25]**
d) $-2x > 6$ ; on divise par $-2$, négatif, ce qui change le sens : $x < -3$. **[0,25]**
e) $\lvert x - 3 \rvert$ est la distance de $x$ à 3 : $-4 \le x - 3 \le 4$, soit $-1 \le x \le 7$. **[0,25]**

**Erreurs fréquentes** : en a), $-(x - 1)^2 = -x^2 - 2x + 1$ (un seul signe changé) ; en b), diviser par $x$ et perdre 0 ; en c), $-3 \times (-1) = -3$ ; en d), garder le sens de l'inégalité ; en e), des crochets ouverts.
**Remédiation** : R2.2, R2.4, R2.5, R2.6, R2.7, R2.9.

## CP0.3 — Un système 2 × 2 et sa lecture graphique ✏️ · 1,5 point

**Réponses** : a) `[2, 3]` · b) `-7` · c) `"1/2"` · d) `[2, -2]` · e) `[2.2, 2.4]` · f) `3`.

a) Par substitution : $y = 9 - 3x$ dans la seconde équation, $x - 18 + 6x = -4$, donc $7x = 14$, $x = 2$, puis $y = 3$. Vérification : $3 \times 2 + 3 = 9$ et $2 - 6 = -4$. Sur la figure, $D_1$ et $D_2$ se coupent bien en $(2 ; 3)$. **[0,25]**
b) $3 \times (-2) - 1 \times 1 = -7$, non nul : le système a une seule solution. **[0,25]**
c) $x - 2y = -4$ donne $2y = x + 4$, soit $y = \frac{1}{2}x + 2$ : la pente vaut $\frac{1}{2}$. **[0,25]**
d) $D_3$ passe par $(0 ; -2)$ et $(2 ; 2)$ : $m = \frac{2 - (-2)}{2 - 0} = 2$, et $p = -2$, l'ordonnée à l'origine. **[0,25]**
e) $3x + (2x - 2) = 9$, donc $5x = 11$, $x = 2{,}2$, puis $y = 2 \times 2{,}2 - 2 = 2{,}4$. Sur la figure, le croisement de $D_1$ et $D_3$ est un peu à droite et en dessous de $(2 ; 3)$. **[0,25]**
f) **3** : la seconde équation est la première multipliée par 2 ; elles décrivent la même droite, et tous ses points sont solutions (le déterminant $3 \times 2 - 6 \times 1$ est nul). **[0,25]**

**Erreurs fréquentes** : en a), inverser $x$ et $y$ ; en b), $ad + bc$ ; en c), oublier de diviser par 2 ; en d), $\frac{\Delta x}{\Delta y}$ ; en e), donner l'intersection de $D_1$ et $D_2$ ; en f), répondre « aucune » parce que les coefficients diffèrent.
**Remédiation** : R2.10, R2.11, R2.15, R3.3.

## CP0.4 — Second degré : racines et sommet ✏️ · 1,5 point

**Réponses** : a) `64` · b) `[-7, 1]` · c) `[-3, 16]` · d) `"]-7 ; 1["` · e) `0` · f) `7`.

a) $\Delta = (-6)^2 - 4 \times (-1) \times 7 = 36 + 28 = 64$. **[0,25]**
b) $x = \frac{6 \pm 8}{2 \times (-1)}$ : $\frac{14}{-2} = -7$ et $\frac{-2}{-2} = 1$. Ou : $f(x) = -(x^2 + 6x - 7) = -(x + 7)(x - 1)$. **[0,25]**
c) $\alpha = -\frac{b}{2a} = -\frac{-6}{-2} = -3$ (au milieu des racines), et $f(-3) = -9 + 18 + 7 = 16$. **[0,25]**
d) $a = -1 < 0$ : la parabole est tournée vers le bas, $f$ est positive entre ses racines, strictement entre elles. **[0,25]**
e) **0** : le maximum de $f$ est 16 (le sommet), donc $f(x) = 20$ n'a pas de solution. **[0,25]**
f) Le sommet est en $x = -3$, hors de $[0 ; 2]$ ; sur cet intervalle, à droite du sommet, $f$ est décroissante : sa plus grande valeur est $f(0) = 7$ (et $f(2) = -9$). **[0,25]**

**Erreurs fréquentes** : en a), $36 - 28$ ; en b), oublier le signe de $a$ au dénominateur ($[-1, 7]$) ; en d), donner l'extérieur des racines (le cas $a > 0$) ; en f), répondre 16, le maximum sur $\mathbb{R}$.
**Remédiation** : R3.5, R3.6, R3.7, R3.8.

## CP0.5 — Exponentielle et logarithme ✏️ · 1,25 point

**Réponses** : a) `0` · b) `"(ln(3) + 5)/2"` · c) `1.43` · d) `3` · e) `"3/5"`.

a) $\ln 12 - \ln 3 + \ln\frac{1}{4} = \ln\left(\frac{12}{3} \times \frac{1}{4}\right) = \ln 1 = 0$. **[0,25]**
b) $2x - 5 = \ln 3$, donc $x = \frac{\ln 3 + 5}{2} \approx 3{,}049$. **[0,25]** (0,1 pour la seule valeur approchée)
c) $4x - 3 = e^1$, donc $x = \frac{e + 3}{4} \approx \frac{5{,}718}{4} \approx 1{,}43$ ; on vérifie que $4x - 3 = e > 0$. **[0,25]**
d) $\log_2 40 - \log_2 5 = \log_2 \frac{40}{5} = \log_2 8 = 3$. **[0,25]**
e) $e^{\ln 2} = 2$ et $e^{-\ln 2} = \frac{1}{2}$, donc $\tanh(\ln 2) = \frac{2 - \frac{1}{2}}{2 + \frac{1}{2}} = \frac{3/2}{5/2} = \frac{3}{5}$. **[0,25]**

**Erreurs fréquentes** : en a) et d), $\ln(a - b)$ ou $\log_2(a - b)$ au lieu de $\ln\frac{a}{b}$ ; en b), diviser avant d'ajouter 5 ; en c), prendre $\ln$ au lieu de $\exp$ pour défaire $\ln$ ; en e), $e^{-\ln 2} = 2$, ou la fraction à l'envers ($\frac{5}{3}$).
**Remédiation** : R6.1, R6.2, R6.3, R6.4, R6.10.

## CP0.6 — Dériver et étudier les variations ✏️ · 2 points

**Réponses** : a) `"3*x**2 - 12"` · b) `[-2, 2]` · c) `[21, -11]` · d) `"[-2 ; 2]"` · e) `[-9, 3]` · f) `"(2*x - x**2)*exp(-x)"` · g) `"7/(x + 3)**2"` · h) `3`.

a) $f'(x) = 3x^2 - 12$. **[0,25]**
b) $3x^2 - 12 = 0$ équivaut à $x^2 = 4$ : $x = -2$ ou $x = 2$. **[0,25]**
c) $f'$ est positive avant $-2$, négative entre $-2$ et 2, positive après : maximum local $f(-2) = -8 + 24 + 5 = 21$, minimum local $f(2) = 8 - 24 + 5 = -11$. **[0,25]**
d) $f' \le 0$ sur $[-2 ; 2]$ (nulle seulement aux bornes) : $f$ y est décroissante. **[0,25]**
e) $f(1) = -6$ et $f'(1) = -9$ : $y = -9(x - 1) - 6 = -9x + 3$. **[0,25]**
f) Règle du produit avec $u = x^2$, $v = e^{-x}$, $v' = -e^{-x}$ (règle de la chaîne) : $g'(x) = 2x\,e^{-x} - x^2 e^{-x} = (2x - x^2)\,e^{-x}$. **[0,25]**
g) Règle du quotient avec $u = 2x - 1$, $v = x + 3$ : $h'(x) = \frac{2(x + 3) - (2x - 1) \times 1}{(x + 3)^2} = \frac{7}{(x + 3)^2}$. **[0,25]**
h) **3** : $f$ part de $-\infty$ (en $-\infty$), monte jusqu'à $f(-2) = 21 > 0$, descend jusqu'à $f(2) = -11 < 0$, puis remonte vers $+\infty$. Sur chacun des trois intervalles où elle est monotone, elle passe par 0 exactement une fois. **[0,25]** (0,1 sans le tableau de variations)

**Erreurs fréquentes** : en a), garder le 5 ; en b), oublier $-2$ ; en c), donner les abscisses au lieu des valeurs ; en e), répondre $[-9, -6]$ (le point au lieu de l'ordonnée à l'origine) ; en f), $u'v'$, ou oublier le signe moins de la dérivée de $e^{-x}$ ; en g), $uv' - u'v$, dans le mauvais ordre ($-\frac{7}{(x + 3)^2}$) ; en h), ne pas comparer les extrema à 0.
**Remédiation** : R7.1, R7.4, R7.5, R7.6, R7.7, R7.8.

## CP0.7 — Un arbre de probabilités et une espérance ✏️ · 1,5 point

**Réponses** : a) `0.052` · b) `0.024` · c) `0.1013` · d) `1.38` · e) `7.10` · f) `1.75`.

L'arbre : une première branche $C$ (0,7) ou $V$ (0,3), puis $R$ ou $\bar{R}$ : 0,04 et 0,96 après $C$, 0,08 et 0,92 après $V$.

a) $P(R) = 0{,}7 \times 0{,}04 + 0{,}3 \times 0{,}08 = 0{,}028 + 0{,}024 = 0{,}052$ (probabilités totales). **[0,25]**
b) $P(V \cap R) = P(V) \times P_V(R) = 0{,}3 \times 0{,}08 = 0{,}024$. **[0,25]**
c) Par l'événement contraire : aucun des deux n'est en retard avec probabilité $0{,}948^2 = 0{,}898704$ (indépendance), donc au moins un l'est avec probabilité $1 - 0{,}898704 \approx 0{,}1013$. **[0,25]**
d) $\mathbb{E}[X] = 0{,}948 \times 2 + 0{,}052 \times (-10) = 1{,}896 - 0{,}52 = 1{,}376 \approx 1{,}38$. **[0,25]**
e) $\mathbb{E}[X^2] = 0{,}948 \times 4 + 0{,}052 \times 100 = 3{,}792 + 5{,}2 = 8{,}992$, puis $\mathbb{V}(X) = 8{,}992 - 1{,}376^2 = 8{,}992 - 1{,}893376 \approx 7{,}10$. **[0,25]**
f) Linéarité de l'espérance : $\mathbb{E}[2X - 1] = 2\,\mathbb{E}[X] - 1 = 1{,}752 \approx 1{,}75$. **[0,25]**

**Erreurs fréquentes** : en a), additionner les taux de retard (0,12) ou en faire la moyenne (0,06) ; en b), répondre 0,08, la seule probabilité conditionnelle ; en c), $2 \times 0{,}052$ ; en d), la moyenne non pondérée $-4$ ; en e), oublier de retrancher $\mathbb{E}[X]^2$ ; en f), oublier le $-1$.
**Remédiation** : R8.3, R8.6, R8.7, R8.8, R8.9.

## CP0.8 — Vecteurs, produit scalaire, angle ✏️ · 1,25 point

**Réponses** : a) `[6, -4]` · b) `7.21` · c) `10` · d) `"5/13"` · e) `67.4`.

a) Arrivée moins départ : $\overrightarrow{AB} = (3 - (-3) ; -3 - 1) = (6 ; -4)$. **[0,25]**
b) $AB = \sqrt{6^2 + (-4)^2} = \sqrt{52} = 2\sqrt{13} \approx 7{,}21$. **[0,25]**
c) $\overrightarrow{AC} = (3 ; 2)$, donc $\overrightarrow{AB} \cdot \overrightarrow{AC} = 6 \times 3 + (-4) \times 2 = 18 - 8 = 10$. **[0,25]**
d) $AC = \sqrt{13}$, et $\cos\widehat{BAC} = \frac{10}{\sqrt{52}\,\sqrt{13}} = \frac{10}{\sqrt{676}} = \frac{10}{26} = \frac{5}{13}$. **[0,25]**
e) $\arccos\frac{5}{13} \approx 1{,}176$ radian, soit environ 67,4°. **[0,25]**

**Erreurs fréquentes** : en a), départ moins arrivée ; en b), oublier la racine (52) ; en c), un signe perdu (26) ; en d), diviser par une seule norme, ou ne pas simplifier $\frac{10}{26}$ ; en e), donner l'angle en radians.
**Remédiation** : R9.1, R9.2, R9.5, R9.9.

## CP0.9 — Une démonstration courte par récurrence ∂ · 1,5 point

**Réponse modèle.**
1. $u_1 = 2 \times 1 + 5 = 7$, $u_2 = 2 \times 7 + 5 = 19$, $u_3 = 2 \times 19 + 5 = 43$.
2. Pour tout entier $n \ge 0$, notons $P(n)$ la propriété « $u_n = 6 \times 2^n - 5$ ».
   - *Initialisation* : $6 \times 2^0 - 5 = 6 - 5 = 1 = u_0$ : $P(0)$ est vraie.
   - *Hérédité* : soit $n \ge 0$ tel que $P(n)$ est vraie, c'est-à-dire $u_n = 6 \times 2^n - 5$. Alors $u_{n+1} = 2u_n + 5 = 2(6 \times 2^n - 5) + 5 = 6 \times 2^{n+1} - 10 + 5 = 6 \times 2^{n+1} - 5$ : $P(n + 1)$ est vraie.
   - *Conclusion* : $P(0)$ est vraie et $P(n)$ entraîne $P(n + 1)$ ; par récurrence, $u_n = 6 \times 2^n - 5$ pour tout entier $n \ge 0$. ∎
3. $2^n$ tend vers $+\infty$ (suite géométrique de raison $2 > 1$), donc $6 \times 2^n - 5$ aussi : $(u_n)$ tend vers $+\infty$.
4. $u_n > 1\,000$ équivaut à $6 \times 2^n > 1\,005$, soit $2^n > 167{,}5$. Or $2^7 = 128$ et $2^8 = 256$ : le plus petit entier est $n = 8$ ($u_7 = 763$, $u_8 = 1\,531$). Comme $(u_n)$ est croissante (elle l'est, puisque $2^n$ l'est), tous les rangs suivants conviennent aussi.

**Barème.** 1. **[0,25]** (0,1 si un seul terme est faux) ; 2. initialisation **[0,2]**, hérédité **[0,4]** (l'hypothèse de récurrence écrite et utilisée, le calcul jusqu'à la formule au rang $n + 1$), conclusion **[0,15]** ; 3. **[0,25]** (la limite avec sa justification) ; 4. **[0,25]** (0,1 pour la valeur sans justification).

**Grille.** Une bonne démonstration : (1) nomme la propriété $P(n)$ et dit pour quels $n$ ; (2) vérifie le premier rang **avec la définition** de la suite ; (3) écrit l'hypothèse de récurrence, puis part de $u_{n+1} = 2u_n + 5$ et **utilise** l'hypothèse ; (4) conclut par une phrase qui cite l'initialisation et l'hérédité.

**Erreurs fréquentes** : vérifier quelques rangs et conclure « donc c'est vrai pour tout $n$ » ; partir de la formule au rang $n + 1$ pour arriver à une égalité vraie (le raisonnement est à l'envers) ; oublier l'initialisation.
**Remédiation** : R4.12, R4.13, R4.24, R5.1, R5.3.

## CP0.10 — Corriger une copie : cinq erreurs 🐛 · 1,25 point

**Réponse** : a) `"BCEFH"`.

a) **[0,5]** : 0,1 par lettre juste, et 0,1 de moins par ligne juste citée (au moins 0).
b) **[0,75]** : 0,15 par ligne fausse corrigée avec sa règle.
- **(B)** $\frac{x + 6}{3} = \frac{x}{3} + 2$ : on divise **chaque** terme du numérateur, pas un seul.
- **(C)** $(-1)^7 = -1$ : un nombre négatif élevé à une puissance impaire reste négatif.
- **(E)** $e^3 \times e^4 = e^{3 + 4} = e^7$ : un produit d'exponentielles additionne les exposants.
- **(F)** la dérivée de $\sqrt{x}$ est $\frac{1}{2\sqrt{x}}$ (pour $x > 0$) : $\sqrt{x} = x^{1/2}$, de dérivée $\frac{1}{2}x^{-1/2}$.
- **(H)** $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0{,}45 + 0{,}35 - 0{,}15 = 0{,}65$ : sans retrancher l'intersection, on la compte deux fois.

Les lignes (A) ($\sqrt{ab} = \sqrt{a}\sqrt{b}$ : $5 \times 4$), (D) ($\ln a - \ln b = \ln\frac{a}{b}$) et (G) (une valeur remarquable : $\frac{2\pi}{3} = \pi - \frac{\pi}{3}$) sont justes.

**Erreurs fréquentes** : citer (A), en confondant avec l'erreur $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$, ou (D) ; laisser passer (C) ou (G) faute de vérifier le signe.
**Remédiation** : R1.28, R1.29, R2.27, R6.21, R7.24, R8.23, et `annexes/erreurs_frequentes.md`.

## CP0.11 — Une somme écrite avec Σ et une somme géométrique ✏️ · 1,25 point

**Réponses** : a) `26` · b) `155` · c) `27` · d) `"5/3"` · e) `1024`.

a) $0 + 3 + 8 + 15 = 26$ (ou $1 + 4 + 9 + 16 - 4$). **[0,25]**
b) Somme géométrique de premier terme 5, de raison 2, à 5 termes : $5 \times \frac{2^5 - 1}{2 - 1} = 5 \times 31 = 155$ (vérification : $5 + 10 + 20 + 40 + 80$). **[0,25]**
c) De $k = 4$ à $k = 12$, il y a $12 - 4 + 1 = 9$ termes, tous égaux à 3 : 27. **[0,25]**
d) Raison $q = \frac{2}{5}$, avec $\lvert q \rvert < 1$, premier terme 1 : $\frac{1}{1 - \frac{2}{5}} = \frac{5}{3}$. **[0,25]**
e) $2^1 \times 2^2 \times 2^3 \times 2^4 = 2^{1 + 2 + 3 + 4} = 2^{10} = 1\,024$ : un produit de puissances d'un même nombre additionne les exposants. **[0,25]**

**Erreurs fréquentes** : en a), compter le $-1$ une seule fois (29) ; en b) et c), un terme de moins (75, 24) ; en d), $\frac{q}{1 - q}$ en oubliant le terme $k = 0$ ; en e), additionner les termes (30), ou multiplier les exposants ($2^{24}$).
**Remédiation** : R4.6, R4.7, R5.4, R5.5.

## CP0.12 — Problème de synthèse : étudier une fonction de coût 🔗 · 2 points

**Réponses** : a) `1` · b) `"exp(w) - 2"` · c) `"ln(2)"` · d) `0.614` · e) `"]-oo ; ln(2)]"` · f) `"+oo"` · g) `[-1, 1]` · h) `True`.

a) $L(0) = e^0 - 0 = 1$. **[0,25]**
b) $L'(w) = e^w - 2$. **[0,25]**
c) $e^w - 2 = 0$ équivaut à $e^w = 2$, soit $w^* = \ln 2 \approx 0{,}693$. **[0,25]**
d) $L(\ln 2) = e^{\ln 2} - 2\ln 2 = 2 - 2\ln 2 \approx 0{,}614$. **[0,25]**
e) $L'(w) < 0$ équivaut à $e^w < 2$, soit $w < \ln 2$ ($\exp$ est croissante) : $L$ est décroissante sur $]-\infty ; \ln 2]$, puis croissante : $w^*$ est bien un minimum. **[0,25]**
f) $L(w) = w\left(\frac{e^w}{w} - 2\right)$ et $\frac{e^w}{w}$ tend vers $+\infty$ (croissances comparées) : $L(w)$ tend vers $+\infty$. **[0,25]**
g) $L'(0) = e^0 - 2 = -1$ et $L(0) = 1$ : $y = -w + 1$. **[0,25]**
h) **Vrai** : le minimum de $L$ sur $\mathbb{R}$ est $2 - 2\ln 2 \approx 0{,}614 > 0$. **[0,25]**

Le lien avec workbookIA : « entraîner » un modèle, c'est chercher le paramètre qui minimise une fonction de coût. Ici, une seule variable et une formule simple permettent de le faire à la main : dériver, annuler la dérivée, vérifier les variations. workbookIA fera la même chose avec des milliers de paramètres, par un calcul numérique.

**Erreurs fréquentes** : en c), $w = 2$ ou $w = e^2$ ; en d), oublier que $e^{\ln 2} = 2$ ; en e), inverser décroissante et croissante ; en f), « $-\infty$ », en croyant que $-2w$ l'emporte ; en g), donner le point $(0 ; 1)$ au lieu de l'équation.
**Remédiation** : R6.3, R6 §5 et R6.19 (croissances comparées), R7.1, R7.4, R7.8, R7.15.

## Barème récapitulatif et remédiation

| Question | Points | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP0.Q1 | 2,5 | R1 à R9 | les exercices cités au CP0.Q1, puis les quiz et les flashcards des chapitres concernés |
| CP0.1 | 1,25 | R1 | R1.2, R1.5, R1.7, R1.8, R1.10, R1.12 |
| CP0.2 | 1,25 | R2 | R2.2, R2.4, R2.5, R2.6, R2.7, R2.9 |
| CP0.3 | 1,5 | R2, R3 | R2.10, R2.11, R2.15, R3.3 |
| CP0.4 | 1,5 | R3 | R3.5, R3.6, R3.7, R3.8 |
| CP0.5 | 1,25 | R6 | R6.1, R6.2, R6.3, R6.4, R6.10 |
| CP0.6 | 2 | R7 | R7.1, R7.4, R7.5, R7.6, R7.7, R7.8 |
| CP0.7 | 1,5 | R8 | R8.3, R8.6, R8.7, R8.8, R8.9 |
| CP0.8 | 1,25 | R9 | R9.1, R9.2, R9.5, R9.9 |
| CP0.9 | 1,5 | R4, R5 | R4.12, R4.13, R4.24, R5.1, R5.3 |
| CP0.10 | 1,25 | R1 à R9 | R1.28, R1.29, R2.27, R6.21, R7.24, R8.23 |
| CP0.11 | 1,25 | R4, R5 | R4.6, R4.7, R5.4, R5.5 |
| CP0.12 | 2 | R6, R7 | R6.3, R6.19, R7.1, R7.4, R7.8, R7.15 |
| **Total** | **20** | | |

**Lire ta note**
- **16 à 20** : la remise à niveau est solide. Passe à workbookIA 0B ; garde les flashcards de la partie 0 dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe à workbookIA 0B.
- **8 à moins de 12** : avant workbookIA 0B, fais la remédiation, relis ta synthèse et les fiches des chapitres concernés.
- **Moins de 8** : reprends les exercices ★★ des chapitres où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
