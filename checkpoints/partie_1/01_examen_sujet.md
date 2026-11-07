# CP1 · Examen blanc de la partie I (M02a à M06)

| | |
|---|---|
| **Durée** | 124 minutes (environ 2 heures), d'une traite |
| **Note** | sur 20 points |
| **Chapitres** | M02a à M06 : intégrales et densités, lois usuelles, échantillons et estimation, probabilités conditionnelles, Bayes et loi Beta, dérivées, Taylor et calcul numérique, gradient, théorie de l'information |
| **Ta copie** | `04_mes_reponses.md` (ta copie, dans `mon_travail/checkpoints/partie_1/`), ou une feuille de papier |
| **Après** | le notebook `02_examen_notebook.ipynb` vérifie tes réponses chiffrées ; `03_examen_corrige.md` donne le corrigé détaillé, le barème et la remédiation |

## Règles

- **Fiches, notes, flashcards, annexes et corrigés fermés.** Pas d'assistant IA, pas de recherche sur le web.
- **Calculatrice autorisée**, ou Python comme simple calculatrice (`+`, `*`, `**`, `math.sqrt`, `math.exp`, `math.log`, `math.log2`) ; ni NumPy, ni SciPy, ni SymPy, ni `mymath`, ni les notebooks des chapitres. Les valeurs de la loi normale et des logarithmes dont tu as besoin sont données dans l'énoncé.
- Donne les valeurs **exactes** quand la question le demande (une fraction irréductible, une expression), et sinon le nombre de décimales demandé. **N'arrondis qu'à la fin** du calcul : garde au moins 4 décimales dans les calculs intermédiaires.
- Écris ta démarche : la moitié des points d'une question de calcul vont à la méthode. Quand une question dit « justifie », une réponse sans justification ne rapporte qu'une partie des points.
- Les durées sont indicatives : commence par ce que tu sais faire ; si tu bloques, passe à la question suivante et reviens-y à la fin.

| Question | Type | Sujet | Points | ⏱️ |
|---|---|---|---|---|
| CP1.Q1 | 🧠 | Dix affirmations sur la partie I : vrai ou faux | 1,5 | 10 min |
| CP1.1 | ✏️ | Intégrales et densité : une aire, une fonction de répartition, un quantile | 1,5 | 10 min |
| CP1.2 | ✏️ | Lois usuelles : binomiale, Poisson, normale | 1,5 | 9 min |
| CP1.3 | ✏️ | Un couple de variables : marginales, indépendance, variance d'une somme | 1,25 | 8 min |
| CP1.4 | ✏️ | Estimer une moyenne : erreur type et intervalle de confiance | 1,5 | 8 min |
| CP1.5 | ✏️ | Un tableau de contingence et des métriques comme probabilités | 1,5 | 8 min |
| CP1.6 | ✏️ | Bayes et la loi Beta : une mise à jour conjuguée | 1,5 | 8 min |
| CP1.7 | ✏️ | Taylor, Newton et un calcul stable | 1,5 | 9 min |
| CP1.8 | ✏️ | Gradient, dérivée directionnelle et point critique | 1,5 | 10 min |
| CP1.9 | ✏️ | Entropie, information mutuelle et KL | 1,5 | 10 min |
| CP1.10 | ∂ | Une démonstration courte, au choix parmi deux | 2 | 12 min |
| CP1.11 | 🐛 | Corriger une copie : cinq erreurs | 1,25 | 8 min |
| CP1.12 | 🔗 | Problème de synthèse : estimer un paramètre de bout en bout | 2 | 14 min |
| | | **Total** | **20** | **124 min** |

Le barème de chaque sous-question est entre crochets. Sauf mention contraire, une sous-question vaut 0,25 point ; une justification demandée « sur ta copie » compte dans les points de la sous-question à laquelle elle se rattache.

---

### CP1.Q1 — Dix affirmations sur la partie I : vrai ou faux 🧠 ★ ⏱️ 10 min · 1,5 point

Pour chaque affirmation, réponds **Vrai** ou **Faux**, puis justifie en une phrase : une règle, un calcul ou un contre-exemple. Chaque affirmation vaut 0,15 point : 0,05 pour le verdict, 0,1 pour la justification.

a) La médiane d'une variable aléatoire de densité $f$ est le point où $f$ atteint son maximum.
b) Si $X$ suit une loi de Poisson de paramètre 9, l'écart-type de $X$ vaut 3.
c) Si $X$ suit la loi exponentielle de paramètre 2, alors $\mathbb{E}[X] = 2$.
d) D'après la loi des grands nombres, la moyenne d'un échantillon i.i.d. de 10 000 valeurs est égale à l'espérance de la loi.
e) Si $P(A \mid B) = P(A)$, avec $P(A) > 0$ et $P(B) > 0$, alors $P(B \mid A) = P(B)$.
f) Après une mise à jour d'un a priori $\mathrm{Beta}(a, b)$ par $k$ succès en $n$ essais, la moyenne a posteriori est toujours comprise entre la moyenne a priori $\frac{a}{a + b}$ et la fréquence observée $\frac{k}{n}$.
g) Si $f''(x) > 0$ pour tout réel $x$, alors $f'$ s'annule au plus une fois.
h) Un point où le gradient d'une fonction de deux variables est nul est un minimum local ou un maximum local.
i) Si l'information mutuelle de deux variables discrètes $X$ et $Y$ est nulle, alors $H(Y \mid X) = H(Y)$.
j) Si un traitement a un meilleur taux de réussite qu'un autre dans chacun de deux groupes de patients, il a aussi un meilleur taux de réussite sur les deux groupes réunis.

### CP1.1 — Intégrales et densité : une aire, une fonction de répartition, un quantile ✏️ ★★ ⏱️ 10 min · 1,5 point

La question a) est indépendante de la suite. Pour b) à f), on pose $f(x) = c\,(x + 1)$ pour $0 \le x \le 2$, et $f(x) = 0$ ailleurs ; $X$ est une variable aléatoire de densité $f$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\displaystyle\int_0^2 x\,e^{x/2}\,dx$ (par parties) | un nombre (valeur exacte, ou 3 décimales) |
| b | la constante $c$ qui fait de $f$ une densité | une fraction irréductible |
| c | la fonction de répartition $F(x) = P(X \le x)$, pour $0 \le x \le 2$ | une expression en $x$ |
| d | $P(1 < X \le 2)$ | une fraction irréductible |
| e | la médiane de $X$ | un nombre (3 décimales) |
| f | $\mathbb{E}[X]$ | une fraction irréductible |

### CP1.2 — Lois usuelles : binomiale, Poisson, normale ✏️ ★★ ⏱️ 9 min · 1,5 point

Un modèle de lecture d'écriture manuscrite lit un formulaire de 12 cases ; il se trompe sur chaque case avec la probabilité 0,07, indépendamment des autres cases. Un serveur reçoit en moyenne 1,8 alerte par heure ; le nombre d'alertes sur une durée donnée suit une loi de Poisson. L'autonomie d'une batterie de drone suit la loi normale de moyenne 14 minutes et d'écart-type 1,5 minute.

Valeurs utiles de la fonction de répartition $\Phi$ de la loi normale centrée réduite : $\Phi(1) \approx 0{,}8413$ ; $\Phi(1{,}2816) \approx 0{,}90$ ; $\Phi(1{,}645) \approx 0{,}95$ ; $\Phi(1{,}96) \approx 0{,}975$ ; $\Phi(2) \approx 0{,}9772$ ; et $\Phi(-z) = 1 - \Phi(z)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la probabilité que le modèle ne fasse aucune erreur sur un formulaire | un nombre (4 décimales) |
| b | la probabilité qu'il fasse au moins deux erreurs sur un formulaire | un nombre (4 décimales) |
| c | la probabilité de recevoir exactement 2 alertes en une heure | un nombre (4 décimales) |
| d | la probabilité de recevoir au moins une alerte en 20 minutes | un nombre (4 décimales) |
| e | la probabilité qu'une batterie tienne entre 12,5 et 17 minutes | un nombre (2 décimales) |
| f | l'autonomie que dépassent 90 % des batteries | un nombre (2 décimales) |

### CP1.3 — Un couple de variables : marginales, indépendance, variance d'une somme ✏️ ★★ ⏱️ 8 min · 1,25 point

Pour un abonné d'un service de vidéo pris au hasard, $X$ est le nombre de films regardés le week-end (0, 1 ou 2), et $Y$ vaut 1 s'il a aussi regardé un épisode de série, 0 sinon. La loi jointe :

| | $Y = 0$ | $Y = 1$ |
|---|---|---|
| $X = 0$ | 0,1 | 0,2 |
| $X = 1$ | 0,2 | 0,1 |
| $X = 2$ | 0,1 | 0,3 |

| | Question | Réponse attendue |
|---|---|---|
| a | la loi marginale de $X$ : $[P(X = 0), P(X = 1), P(X = 2)]$ | une liste |
| b | $X$ et $Y$ sont-elles indépendantes ? (justifie sur ta copie) | `True` ou `False` |
| c | $\mathrm{Cov}(X, Y)$ | un nombre (2 décimales) |
| d | $\mathbb{V}(X)$ | un nombre (2 décimales) |
| e | $\mathbb{V}(X + Y)$ | un nombre (2 décimales) |

### CP1.4 — Estimer une moyenne : erreur type et intervalle de confiance ✏️ ★★ ⏱️ 8 min · 1,5 point

On a mesuré la longueur, en tokens, de 50 questions posées à un assistant. La somme des 50 longueurs vaut 1 230, et la somme des carrés des écarts à la moyenne, $\sum_i (x_i - \bar{x})^2$, vaut 1 911. Parmi ces 50 questions, 18 dépassent 30 tokens.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne $\bar{x}$ | un nombre (1 décimale) |
| b | l'écart-type $s$ de l'échantillon, avec ddof = 1 | un nombre (3 décimales) |
| c | l'erreur type de la moyenne | un nombre (3 décimales) |
| d | l'intervalle de confiance à 95 % de la longueur moyenne (quantile 1,96) | la liste [bas, haut] (2 décimales) |
| e | la demi-largeur de l'intervalle de confiance à 90 % de la longueur moyenne (quantile 1,645) | un nombre (2 décimales) |
| f | l'intervalle de confiance à 95 % de la proportion de questions de plus de 30 tokens | la liste [bas, haut] (3 décimales) |

### CP1.5 — Un tableau de contingence et des métriques comme probabilités ✏️ ★★ ⏱️ 8 min · 1,5 point

Une montre connectée détecte les chutes. Sur 500 événements enregistrés (des mouvements brusques), 60 sont de vraies chutes. La montre a donné l'alerte pour 45 des 60 vraies chutes, et pour 30 des 440 autres événements. Écris d'abord la matrice de confusion sur ta copie.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(\text{alerte})$, pour un événement pris au hasard | une fraction irréductible |
| b | la precision, $P(\text{chute} \mid \text{alerte})$ | une fraction irréductible |
| c | le recall, $P(\text{alerte} \mid \text{chute})$ | une fraction irréductible |
| d | le F1 | une fraction irréductible |
| e | la spécificité, $P(\text{pas d'alerte} \mid \text{pas de chute})$ | un nombre (4 décimales) |
| f | les événements « alerte » et « chute » sont-ils indépendants ? (justifie sur ta copie par un calcul) | `True` ou `False` |

### CP1.6 — Bayes et la loi Beta : une mise à jour conjuguée ✏️ ★★ ⏱️ 8 min · 1,5 point

Un outil propose des correctifs de code ; $\theta$ est la probabilité qu'un développeur accepte une proposition. A priori, $\theta$ suit la loi $\mathrm{Beta}(4, 8)$. Sur les 30 premières propositions, 7 sont acceptées (les décisions sont indépendantes sachant $\theta$).

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne a priori de $\theta$ | une fraction irréductible |
| b | les paramètres de la loi a posteriori $\mathrm{Beta}(a, b)$ | la liste $[a, b]$ |
| c | la moyenne a posteriori de $\theta$ | une fraction irréductible |
| d | le MAP de $\theta$ (le mode de la loi a posteriori) | une fraction irréductible |
| e | 10 propositions de plus, dont 3 acceptées : la nouvelle moyenne a posteriori | une fraction irréductible |
| f | après e), la probabilité que les **deux** propositions suivantes soient acceptées toutes les deux | un nombre (4 décimales) |

### CP1.7 — Taylor, Newton et un calcul stable ✏️ ★★ ⏱️ 9 min · 1,5 point

| | Question | Réponse attendue |
|---|---|---|
| a | le polynôme de Taylor d'ordre 2 de $f(x) = \sqrt{4 + x}$ en 0 | une expression en $x$ |
| b | la valeur approchée de $\sqrt{4{,}4}$ que donne a) | un nombre (4 décimales) |
| c | pour résoudre $x^3 + x - 3 = 0$, le premier pas de la méthode de Newton depuis $x_0 = 1$ : $x_1$ | un nombre (2 décimales) |
| d | le deuxième pas, $x_2$ | un nombre (4 décimales) |
| e | $\ln\left(e^{-790} + e^{-787} + e^{-785}\right)$ | un nombre (3 décimales) |
| f | la probabilité que la softmax des scores $(-790, -787, -785)$ donne au score $-785$ | un nombre (3 décimales) |

Sur ta copie, pour e) : que se passe-t-il si l'on calcule en Python `math.log(math.exp(-790) + math.exp(-787) + math.exp(-785))`, et comment l'éviter ?

### CP1.8 — Gradient, dérivée directionnelle et point critique ✏️ ★★ ⏱️ 10 min · 1,5 point

On pose $f(x, y) = x^3 - 6xy + 3y^2$.

| | Question | Réponse attendue |
|---|---|---|
| a | le gradient $\nabla f(1, -1)$ | la liste $[\partial_x f, \partial_y f]$ |
| b | la dérivée directionnelle de $f$ en $(1, -1)$ dans la direction du vecteur $(20, 21)$ | une fraction irréductible |
| c | la plus grande pente de $f$ en $(1, -1)$, toutes directions confondues | un nombre |
| d | les deux points critiques de $f$, dans l'ordre des $x$ croissants | la liste $[x_1, y_1, x_2, y_2]$ |
| e | la nature du premier point critique de d), celui qui a le plus petit $x$ : 1. un minimum local ; 2. un maximum local ; 3. un point selle | le numéro 1, 2 ou 3 |
| f | la valeur de $f$ au second point critique de d) (dont tu justifieras la nature sur ta copie) | un nombre |

### CP1.9 — Entropie, information mutuelle et KL ✏️ ★★ ⏱️ 10 min · 1,5 point

Un forum d'entraide classe ses messages en trois catégories, question, réponse et annonce, de fréquences $p = (0{,}45 ;\ 0{,}4 ;\ 0{,}15)$. Un ancien modèle supposait $q = (0{,}6 ;\ 0{,}35 ;\ 0{,}05)$. Une feature binaire $F$ (le message contient un point d'interrogation, $F = 1$, ou non) et la variable $Y$ (le message est une question, ou non) ont la loi jointe :

| | question | pas une question |
|---|---|---|
| $F = 1$ | 0,35 | 0,05 |
| $F = 0$ | 0,10 | 0,50 |

Les entropies se calculent en bits. Valeurs utiles : $\log_2 3 \approx 1{,}5850$ ; $\log_2 5 \approx 2{,}3219$ ; $\log_2 7 \approx 2{,}8074$ ; $-\log_2 0{,}45 \approx 1{,}1520$ ; $-\log_2 0{,}4 \approx 1{,}3219$ ; $-\log_2 0{,}15 \approx 2{,}7370$ ; $-\log_2 0{,}6 \approx 0{,}7370$ ; $-\log_2 0{,}35 \approx 1{,}5146$ ; $-\log_2 0{,}05 \approx 4{,}3219$ ; $-\log_2 0{,}55 \approx 0{,}8625$.

| | Question | Réponse attendue |
|---|---|---|
| a | $H(p)$ | un nombre (3 décimales) |
| b | la cross-entropy $H(p, q)$ | un nombre (3 décimales) |
| c | $\mathrm{KL}(p \,\|\, q)$ | un nombre (3 décimales) |
| d | $P(\text{question} \mid F = 1)$ | une fraction irréductible |
| e | $H(Y \mid F)$ | un nombre (2 décimales) |
| f | l'information mutuelle $I(F ; Y)$ | un nombre (2 décimales) |

### CP1.10 — Une démonstration courte, au choix parmi deux ∂ ★★★ ⏱️ 12 min · 2 points

Traite **un seul** des deux sujets. Rédige en phrases : ce que tu supposes, chaque étape et la règle qui la justifie, ce que tu conclus.

**Sujet A — Combiner deux mesures.** Deux balances pèsent le même colis, de masse $\mu$. Leurs mesures $X_1$ et $X_2$ sont indépendantes, avec $\mathbb{E}[X_1] = \mathbb{E}[X_2] = \mu$, $\mathbb{V}(X_1) = \sigma_1^2$ et $\mathbb{V}(X_2) = \sigma_2^2$ (deux réels strictement positifs). Pour un réel $w$, on pose $T_w = w\,X_1 + (1 - w)\,X_2$.
1. Montre que $T_w$ est un estimateur sans biais de $\mu$, quel que soit $w$. **[0,25]**
2. Montre que $\mathbb{V}(T_w) = w^2 \sigma_1^2 + (1 - w)^2 \sigma_2^2$, en nommant les règles utilisées. **[0,5]**
3. Trouve le $w^*$ qui rend $\mathbb{V}(T_w)$ la plus petite possible, et justifie que c'est bien un minimum. **[0,5]**
4. Montre que $\mathbb{V}(T_{w^*}) = \dfrac{\sigma_1^2\,\sigma_2^2}{\sigma_1^2 + \sigma_2^2}$, et que cette variance est plus petite que $\sigma_1^2$ et que $\sigma_2^2$. **[0,5]**
5. Que deviennent $w^*$ et $\mathbb{V}(T_{w^*})$ quand $\sigma_1 = \sigma_2$ ? Quel résultat du cours retrouves-tu ? **[0,25]**

**Sujet B — Une courbe convexe est au-dessus de ses tangentes.** Soit $f$ une fonction deux fois dérivable sur $\mathbb{R}$, avec $f''(x) \ge 0$ pour tout $x$, et $a$ un réel. On pose $g(x) = f(x) - \big[f(a) + f'(a)\,(x - a)\big]$.
1. Calcule $g(a)$, $g'(x)$, $g'(a)$ et $g''(x)$. **[0,5]**
2. Déduis-en le sens de variation de $g'$, puis le signe de $g'(x)$ selon que $x < a$ ou $x > a$, puis que $g(x) \ge 0$ pour tout réel $x$. Traduis ce résultat en une phrase sur la courbe de $f$. **[0,75]**
3. Déduis-en que $e^x \ge 1 + x$ pour tout réel $x$. **[0,25]**
4. Déduis-en que $(1 - p)^n \le e^{-np}$ pour tout $p \in [0 ; 1]$ et tout entier $n \ge 1$. Application : un test échoue indépendamment avec la probabilité 0,01 à chaque exécution ; majore la probabilité qu'il n'échoue jamais en 300 exécutions. **[0,5]**

### CP1.11 — Corriger une copie : cinq erreurs 🐛 ★★ ⏱️ 8 min · 1,25 point

Voici huit lignes extraites de la copie d'un élève. **Cinq** sont fausses.

- **(A)** Si $X$ suit la loi normale de moyenne 12 et de variance 0,25, alors $P(X > 12{,}6) = P(Z > 2{,}4)$, où $Z$ suit la loi normale centrée réduite.
- **(B)** $\displaystyle\int_0^1 2x\,e^{x^2}\,dx = e - 1$.
- **(C)** 25 mesures indépendantes ont un écart-type de 10 : l'erreur type de leur moyenne vaut $\frac{10}{25} = 0{,}4$.
- **(D)** $P(A) = 0{,}2$, $P(B) = 0{,}5$ et $P(B \mid A) = 0{,}6$, donc $P(A \mid B) = 0{,}6$.
- **(E)** Avec l'a priori $\mathrm{Beta}(2, 2)$, après 3 succès en 5 essais, l'a posteriori est $\mathrm{Beta}(5, 4)$.
- **(F)** Pour résoudre $x^3 - 2 = 0$ par la méthode de Newton depuis $x_0 = 1$ : $x_1 = 1 - \frac{3}{-1} = 4$.
- **(G)** Pour $p = (0{,}6 ;\ 0{,}4)$ et $q = (0{,}3 ;\ 0{,}7)$ : $\mathrm{KL}(p \,\|\, q) = 0{,}6 \log_2 \frac{0{,}3}{0{,}6} + 0{,}4 \log_2 \frac{0{,}7}{0{,}4} \approx -0{,}277$ bit.
- **(H)** Pour $y > 0$, la dérivée partielle de $x \ln y$ par rapport à $y$ vaut $\frac{x}{y}$.

a) Les lettres des cinq lignes fausses, dans l'ordre alphabétique (un texte, comme `"ABCDE"`). **[0,5]**
b) Pour chaque ligne fausse, écris le résultat juste et la règle oubliée, en une ligne. **[0,75]** (0,15 par ligne)

### CP1.12 — Problème de synthèse : estimer un paramètre de bout en bout 🔗 ★★ ⏱️ 14 min · 2 points

Un service de vélos en libre-service ne garde dans son journal que les jours où au moins un vélo a été signalé en panne. On modélise le nombre de signalements d'un jour par une loi de Poisson de paramètre $\lambda > 0$ ; un jour n'apparaît dans le journal que s'il compte au moins un signalement, si bien que le nombre de signalements d'un jour **du journal** suit la loi

$$P(X = k) = \frac{e^{-\lambda}\,\lambda^k}{k!\,\left(1 - e^{-\lambda}\right)}, \qquad k = 1, 2, 3, \ldots$$

Le journal compte 20 jours, et 32 signalements en tout. On cherche le maximum de vraisemblance $\hat{\lambda}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(X = 1)$ quand $\lambda = 2$ | un nombre (3 décimales) |
| b | écris la log-vraisemblance $\ell(\lambda)$ des 20 jours (à une constante près) sur ta copie, puis donne $\ell'(\lambda)$ | une expression en $\lambda$ (écrite `lam`) |
| c | montre sur ta copie que, pour $\lambda > 0$, $\ell'(\lambda) = 0$ équivaut à $g(\lambda) = \lambda - 1{,}6\,\left(1 - e^{-\lambda}\right) = 0$, puis fais un pas de la méthode de Newton sur $g$ depuis $\lambda_0 = 1{,}6$ : $\lambda_1$ | un nombre (3 décimales) |
| d | le pas suivant, $\lambda_2$ | un nombre (3 décimales) |
| e | l'estimation $\hat{\lambda}$, en continuant les pas | un nombre (3 décimales) |
| f | vrai ou faux : $\ell'(1) > 0$ (sur ta copie : que dit le signe de $\ell'$ de part et d'autre de $\hat{\lambda}$ ?) | `True` ou `False` |
| g | la proportion estimée des jours sans aucun signalement | un nombre (3 décimales) |
| h | un bootstrap (2 000 rééchantillons des 20 jours, chacun ré-estimé de la même façon) donne des estimations d'écart-type 0,28 : l'intervalle de confiance approché à 95 % de $\lambda$, $\hat{\lambda} \pm 1{,}96 \times 0{,}28$ | la liste [bas, haut] (2 décimales) |

Sur ta copie, avec e) : pourquoi la moyenne des 32 signalements sur 20 jours, 1,6, surestime-t-elle $\lambda$ ?

---

**Fin de l'examen.** Note l'heure, relis ta copie, puis passe à la vérification : le notebook `02_examen_notebook.ipynb` (ta copie), puis le corrigé `03_examen_corrige.md`.
