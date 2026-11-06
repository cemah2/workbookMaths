# CP0 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Barème par sous-question**, entre crochets ; sauf mention contraire, une sous-question vaut 0,25 point. Une réponse juste sans démarche, quand la question en demande une, rapporte la moitié des points.
- **Méthode juste, erreur de calcul** : la moitié des points de la sous-question. **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois.
- **Valeurs exactes** : une valeur approchée là où une valeur exacte est demandée (une fraction, `ln`, une racine) rapporte la moitié des points ; une fraction juste mais non simplifiée, les trois quarts.
- **Arrondis** : une décimale de trop ou de moins coûte au plus 0,05 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi.
- **Questions rédigées** (CP0.Q1, CP0.9, CP0.10 b) : les critères sont listés ; une idée juste formulée autrement compte autant.

---

## CP0.Q1 — Dix affirmations sur toute la remise à niveau 🧠 · 2,5 points

Chaque affirmation : **[0,1]** pour le verdict, **[0,15]** pour une justification juste (0,05 si elle est incomplète).

**a) Faux** (R1). Une puissance de puissance **multiplie** les exposants : $(2^3)^2 = 2^{3 \times 2} = 2^6 = 64$, alors que $2^5 = 32$.

**b) Faux** (R2, R3). $\sqrt{x^2} = \lvert x \rvert$ : une racine carrée n'est jamais négative. Contre-exemple : $x = -3$ donne $\sqrt{9} = 3 \ne -3$.

**c) Vrai** (R3). Si $a < b$, alors $f(a) < f(b)$, donc $f(a) \ne f(b)$ : deux nombres différents n'ont jamais la même image. C'est pour cela qu'une telle fonction a une réciproque.

**d) Faux** (R4). La contraposée de « $P \Rightarrow Q$ » est « non $Q \Rightarrow$ non $P$ » : « si le sol n'est pas mouillé, alors il ne pleut pas ». La phrase proposée est la **réciproque**, qui peut être fausse (un arrosage mouille le sol).

**e) Vrai** (R5). $u_n = 2 \times 0{,}9^n$, et $0{,}9^n$ tend vers 0 car $0 < 0{,}9 < 1$.

**f) Vrai** (R6). $e^{2\ln 5} = \left(e^{\ln 5}\right)^2 = 5^2 = 25$ (ou $2\ln 5 = \ln 25$, et $e^{\ln 25} = 25$).

**g) Faux** (R7). La valeur absolue est continue en 0, mais pas dérivable en 0 : son taux d'accroissement vaut $-1$ à gauche et $1$ à droite (un « coin »). L'inverse est vrai : dérivable entraîne continue.

**h) Faux** (R8). Incompatibles : $P(A \cap B) = 0$. Indépendants : $P(A \cap B) = P(A)\,P(B) > 0$. Les deux ensemble sont impossibles quand $P(A) > 0$ et $P(B) > 0$ : savoir que $A$ est arrivé dit que $B$ n'est pas arrivé.

**i) Vrai** (R9). $\vec{u} \cdot \vec{v} = \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert\cos\theta$, avec des normes positives : le produit scalaire a le signe de $\cos\theta$, négatif exactement quand $\theta$ est entre 90° et 180°.

**j) Faux** (R8). Ajouter une constante décale toutes les valeurs, sans changer leur dispersion : $\mathbb{V}(X + 3) = \mathbb{V}(X)$. Plus généralement, $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$.

**Erreurs fréquentes** : en a), additionner les exposants ; en d), confondre contraposée et réciproque ; en g), croire que « continue » suffit ; en h), confondre « incompatibles » et « indépendants » ; en j), appliquer à la variance la règle de l'espérance.
**Remédiation** : a) R1.7 ; b) R2.9, R3.5 ; c) R3.10 ; d) R4.2 ; e) R5.3, R5.5 ; f) R6.1, R6.2 ; g) R7.12 ; h) R8.7 ; i) R9.5, R9.9 ; j) R8.9.

## CP0.1 — Fractions, puissances et notation scientifique ✏️ · 1,25 point

**Réponses** : a) `"-1/8"` · b) `"1/5"` · c) `[2.8, 4]` · d) `[6, 3]` · e) `-10`.

a) La division d'abord : $\frac{5}{6} \div \frac{4}{9} = \frac{5}{6} \times \frac{9}{4} = \frac{45}{24} = \frac{15}{8}$, puis $\frac{7}{4} - \frac{15}{8} = \frac{14}{8} - \frac{15}{8} = -\frac{1}{8}$. **[0,25]**
b) Tout en puissances de 5 : $25^{-3} = (5^2)^{-3} = 5^{-6}$, donc $\frac{5^4 \times 5^{-6}}{5^{-1}} = 5^{4 - 6 - (-1)} = 5^{-1} = \frac{1}{5}$. **[0,25]**
c) $4 \times 7 = 28$ et $10^{-5} \times 10^{8} = 10^{3}$ : $28 \times 10^3 = 2{,}8 \times 10^4$. **[0,25]** (0,15 pour $28 \times 10^3$, juste mais pas en notation scientifique)
d) $\frac{9}{1{,}5} = 6$ et $\frac{10^{-4}}{10^{-7}} = 10^{-4 - (-7)} = 10^{3}$ : $6 \times 10^{3}$. **[0,25]**
e) Les coefficients se multiplient : $1{,}2 \times 0{,}75 = 0{,}9$, soit une baisse de 10 %. **[0,25]**

**Erreurs fréquentes** : en a), soustraire avant de diviser ($\frac{33}{16}$) ; en b), lire $25^{-3}$ comme $5^{-3}$ ; en c), laisser $28 \times 10^3$ ; en d), oublier le signe dans $-4 - (-7)$ ; en e), additionner les pourcentages ($-5$ %).
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

**Réponses** : a) `16` · b) `[1, 3]` · c) `[2, 2]` · d) `"]1 ; 3["` · e) `0` · f) `-6`.

a) $\Delta = 8^2 - 4 \times (-2) \times (-6) = 64 - 48 = 16$. **[0,25]**
b) $x = \frac{-8 \pm 4}{2 \times (-2)}$ : $\frac{-4}{-4} = 1$ et $\frac{-12}{-4} = 3$. Ou : $f(x) = -2(x^2 - 4x + 3) = -2(x - 1)(x - 3)$. **[0,25]**
c) $\alpha = -\frac{b}{2a} = -\frac{8}{-4} = 2$ (au milieu des racines), et $f(2) = -8 + 16 - 6 = 2$. **[0,25]**
d) $a = -2 < 0$ : la parabole est tournée vers le bas, $f$ est positive entre ses racines, strictement entre elles. **[0,25]**
e) **0** : le maximum de $f$ est 2 (le sommet), donc $f(x) = 3$ n'a pas de solution. **[0,25]**
f) Le sommet est en $x = 2$, hors de $[-1 ; 0]$ ; sur cet intervalle, à gauche du sommet, $f$ est croissante : sa plus grande valeur est $f(0) = -6$ (et $f(-1) = -16$). **[0,25]**

**Erreurs fréquentes** : en a), $64 + 48$ ; en b), oublier le signe de $a$ au dénominateur ; en d), donner l'extérieur des racines (le cas $a > 0$) ; en f), répondre 2, le maximum sur $\mathbb{R}$.
**Remédiation** : R3.5, R3.6, R3.7, R3.8.

## CP0.5 — Exponentielle et logarithme ✏️ · 1,25 point

**Réponses** : a) `7` · b) `"(log(4) + 2)/3"` · c) `10.54` · d) `0` · e) `"4/5"`.

a) $\ln(e^4) = 4$, $e^{\ln 3} = 3$, $\ln 1 = 0$ : $4 + 3 - 0 = 7$. **[0,25]**
b) $3x - 2 = \ln 4$, donc $x = \frac{\ln 4 + 2}{3}$ (ou $\frac{2\ln 2 + 2}{3}$), environ 1,129. **[0,25]** (0,1 pour la seule valeur approchée)
c) $2x - 1 = e^3$, donc $x = \frac{e^3 + 1}{2} \approx \frac{20{,}086 + 1}{2} \approx 10{,}54$ ; on vérifie que $2x - 1 > 0$. **[0,25]**
d) $\log_{10}(1\,000) = 3$ et $\log_2\left(\frac{1}{8}\right) = \log_2(2^{-3}) = -3$ : la somme vaut 0. **[0,25]**
e) $e^{-\ln 4} = \frac{1}{e^{\ln 4}} = \frac{1}{4}$, donc $\sigma(\ln 4) = \frac{1}{1 + \frac{1}{4}} = \frac{4}{5}$. **[0,25]**

**Erreurs fréquentes** : en a), $\ln 1 = 1$ ; en b), diviser avant d'ajouter 2 ; en c), prendre $\ln$ au lieu de $\exp$ pour défaire $\ln$ ; en d), $\log_2\frac{1}{8} = 3$ ; en e), oublier le signe moins de $e^{-z}$ ($\frac{1}{5}$).
**Remédiation** : R6.1, R6.2, R6.3, R6.4, R6.7.

## CP0.6 — Dériver et étudier les variations ✏️ · 2 points

**Réponses** : a) `"3*x**2 - 12"` · b) `[-2, 2]` · c) `[21, -11]` · d) `"[-2 ; 2]"` · e) `[-9, 3]` · f) `"(6*x + 1)*exp(2*x)"` · g) `"1/sqrt(2*x + 5)"` · h) `0`.

a) $f'(x) = 3x^2 - 12$. **[0,25]**
b) $3x^2 - 12 = 0$ équivaut à $x^2 = 4$ : $x = -2$ ou $x = 2$. **[0,25]**
c) $f'$ est positive avant $-2$, négative entre $-2$ et 2, positive après : maximum local $f(-2) = -8 + 24 + 5 = 21$, minimum local $f(2) = 8 - 24 + 5 = -11$. **[0,25]**
d) $f' \le 0$ sur $[-2 ; 2]$ (nulle seulement aux bornes) : $f$ y est décroissante. **[0,25]**
e) $f(1) = -6$ et $f'(1) = -9$ : $y = -9(x - 1) - 6 = -9x + 3$. **[0,25]**
f) Règle du produit avec $u = 3x - 1$, $v = e^{2x}$, $v' = 2e^{2x}$ (règle de la chaîne) : $g'(x) = 3e^{2x} + (3x - 1) \times 2e^{2x} = (6x + 1)e^{2x}$. **[0,25]**
g) $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$ avec $u = 2x + 5$, $u' = 2$ : $h'(x) = \frac{2}{2\sqrt{2x + 5}} = \frac{1}{\sqrt{2x + 5}}$. **[0,25]**
h) Croissances comparées : $x^2 e^{-x} = \frac{x^2}{e^x}$ tend vers 0, car l'exponentielle l'emporte sur toute puissance de $x$. **[0,25]**

**Erreurs fréquentes** : en a), garder le 5 ; en b), oublier $-2$ ; en c), donner les abscisses au lieu des valeurs ; en e), répondre $[-9, -6]$ (le point au lieu de l'ordonnée à l'origine) ; en f), $u'v'$, ou oublier le facteur 2 de $e^{2x}$ ; en g), oublier la dérivée de $2x + 5$ ; en h), « $+\infty$ » parce que $x^2$ grandit.
**Remédiation** : R7.1, R7.4, R7.5, R7.6, R7.7, R7.8 ; R6 (croissances comparées).

## CP0.7 — Un arbre de probabilités et une espérance ✏️ · 1,5 point

**Réponses** : a) `0.07` · b) `0.04` · c) `0.1351` · d) `2.44` · e) `4.17` · f) `3.88`.

L'arbre : une première branche $A$ (0,6) ou $B$ (0,4), puis $D$ ou $\bar{D}$ : 0,05 et 0,95 après $A$, 0,1 et 0,9 après $B$.

a) $P(D) = 0{,}6 \times 0{,}05 + 0{,}4 \times 0{,}1 = 0{,}03 + 0{,}04 = 0{,}07$ (probabilités totales). **[0,25]**
b) $P(B \cap D) = P(B) \times P_B(D) = 0{,}4 \times 0{,}1 = 0{,}04$. **[0,25]**
c) Par l'événement contraire : aucune des deux n'est défectueuse avec probabilité $0{,}93^2 = 0{,}8649$ (indépendance), donc au moins une l'est avec probabilité $1 - 0{,}8649 = 0{,}1351$. **[0,25]**
d) $\mathbb{E}[X] = 0{,}93 \times 3 + 0{,}07 \times (-5) = 2{,}79 - 0{,}35 = 2{,}44$. **[0,25]**
e) $\mathbb{E}[X^2] = 0{,}93 \times 9 + 0{,}07 \times 25 = 8{,}37 + 1{,}75 = 10{,}12$, puis $\mathbb{V}(X) = 10{,}12 - 2{,}44^2 = 10{,}12 - 5{,}9536 = 4{,}1664 \approx 4{,}17$. **[0,25]**
f) Linéarité de l'espérance : $\mathbb{E}[2X - 1] = 2\,\mathbb{E}[X] - 1 = 3{,}88$. **[0,25]**

**Erreurs fréquentes** : en a), additionner les taux de défaut (0,15) ; en b), répondre 0,1, la seule probabilité conditionnelle ; en c), $2 \times 0{,}07$ ; en d), la moyenne non pondérée $-1$ ; en e), oublier de retrancher $\mathbb{E}[X]^2$ ; en f), oublier le $-1$.
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

**Réponse** : a) `"ADEFH"`.

a) **[0,5]** : 0,1 par lettre juste, et 0,1 de moins par ligne juste citée (au moins 0).
b) **[0,75]** : 0,15 par ligne fausse corrigée avec sa règle.
- **(A)** $\sqrt{36 + 64} = \sqrt{100} = 10$ : la racine d'une somme n'est pas la somme des racines.
- **(D)** $\frac{2}{5} + \frac{1}{3} = \frac{6}{15} + \frac{5}{15} = \frac{11}{15}$ : on additionne des fractions sur un dénominateur commun, jamais numérateurs et dénominateurs entre eux.
- **(E)** $3^4 \times 3^5 = 3^{4 + 5} = 3^9$ : un produit de puissances d'un même nombre additionne les exposants.
- **(F)** la dérivée de $e^{-4x}$ est $-4e^{-4x}$ : règle de la chaîne, on multiplie par la dérivée de $-4x$.
- **(H)** $\mathbb{V}(-2X) = (-2)^2\,\mathbb{V}(X) = 16$ : une variance n'est jamais négative, $\mathbb{V}(aX) = a^2\,\mathbb{V}(X)$.

Les lignes (B) (une identité remarquable), (C) ($\ln a + \ln b = \ln(ab)$) et (G) (une valeur remarquable) sont justes.

**Erreurs fréquentes** : citer (C), en confondant avec l'erreur $\ln(a + b) = \ln a + \ln b$ ; laisser passer (H) parce que la règle des espérances est linéaire.
**Remédiation** : R1.28, R2.27, R6.21, R7.24, R8.23, et `annexes/erreurs_frequentes.md`.

## CP0.11 — Une somme écrite avec Σ et une somme géométrique ✏️ · 1,25 point

**Réponses** : a) `26` · b) `155` · c) `27` · d) `"5/3"` · e) `"1/6"`.

a) $0 + 3 + 8 + 15 = 26$ (ou $1 + 4 + 9 + 16 - 4$). **[0,25]**
b) Somme géométrique de premier terme 5, de raison 2, à 5 termes : $5 \times \frac{2^5 - 1}{2 - 1} = 5 \times 31 = 155$ (vérification : $5 + 10 + 20 + 40 + 80$). **[0,25]**
c) De $k = 4$ à $k = 12$, il y a $12 - 4 + 1 = 9$ termes, tous égaux à 3 : 27. **[0,25]**
d) Raison $q = \frac{2}{5}$, avec $\lvert q \rvert < 1$, premier terme 1 : $\frac{1}{1 - \frac{2}{5}} = \frac{5}{3}$. **[0,25]**
e) $\frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} \times \frac{4}{5} \times \frac{5}{6} = \frac{1}{6}$ : chaque numérateur se simplifie avec le dénominateur précédent. **[0,25]**

**Erreurs fréquentes** : en a), compter le $-1$ une seule fois (29) ; en b) et c), un terme de moins (75, 24) ; en d), $\frac{q}{1 - q}$ en oubliant le terme $k = 0$ ; en e), s'arrêter à $k = 5$.
**Remédiation** : R4.6, R4.7, R5.4, R5.5.

## CP0.12 — Problème de synthèse : étudier une fonction de coût 🔗 · 2 points

**Réponses** : a) `1` · b) `"exp(w) - 2"` · c) `"log(2)"` · d) `0.614` · e) `"]-oo ; log(2)]"` · f) `"+oo"` · g) `[-1, 1]` · h) `True`.

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
**Remédiation** : R6.3, R7.4, R7.8, R7.15, R3.15.

## Barème récapitulatif et remédiation

| Question | Points | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP0.Q1 | 2,5 | R1 à R9 | les exercices cités au CP0.Q1, puis les quiz et les flashcards des chapitres concernés |
| CP0.1 | 1,25 | R1 | R1.5, R1.7, R1.8, R1.10, R1.12 |
| CP0.2 | 1,25 | R2 | R2.2, R2.4, R2.6, R2.7, R2.9 |
| CP0.3 | 1,5 | R2, R3 | R2.10, R2.11, R2.15, R3.3 |
| CP0.4 | 1,5 | R3 | R3.6, R3.7, R3.8 |
| CP0.5 | 1,25 | R6 | R6.1, R6.2, R6.3, R6.4, R6.7 |
| CP0.6 | 2 | R7 | R7.4, R7.5, R7.6, R7.7, R7.8 |
| CP0.7 | 1,5 | R8 | R8.3, R8.6, R8.8, R8.9 |
| CP0.8 | 1,25 | R9 | R9.1, R9.5, R9.9 |
| CP0.9 | 1,5 | R4, R5 | R4.12, R4.13, R4.24, R5.3 |
| CP0.10 | 1,25 | R1 à R9 | R1.28, R2.27, R6.21, R7.24, R8.23 |
| CP0.11 | 1,25 | R4, R5 | R4.6, R4.7, R5.4, R5.5 |
| CP0.12 | 2 | R6, R7 | R7.8, R7.15, R6.3 |
| **Total** | **20** | | |

**Lire ta note**
- **16 à 20** : la remise à niveau est solide. Passe à workbookIA 0B ; garde les flashcards de la partie 0 dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe à workbookIA 0B.
- **8 à moins de 12** : avant workbookIA 0B, fais la remédiation, relis ta synthèse et les fiches des chapitres concernés.
- **Moins de 8** : reprends les exercices ★★ des chapitres où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
