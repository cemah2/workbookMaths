# M13a · Vraisemblance et régression logistique — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M13a.Q1 — Vraisemblance, log-vraisemblance, maximum : le vocabulaire
1. **Faux** : c'est une probabilité (ou une densité) **des données**, lue comme une fonction du paramètre ; son intégrale en $\theta$ ne vaut pas 1 en général.
2. Le logarithme est croissant (même maximum), il transforme le produit en somme (qui se dérive terme à terme), et il évite qu'un produit de nombreuses probabilités tombe à 0 en flottants.
3. Un produit de 30 facteurs ; la log-vraisemblance est une somme de 30 termes.
4. $\hat{p} = \frac{14}{40} = 0{,}35$.
5. **Vrai** pour une loi discrète (des probabilités au plus 1, des logarithmes au plus 0). Pour une loi continue, non : une densité peut dépasser 1 (une loi normale de petite variance), et sa log-vraisemblance être positive.
6. **Faux** : $\mathbb{E}[\hat{\sigma}^2] = \frac{n - 1}{n}\sigma^2$ ; l'estimation sans biais divise par $n - 1$.

### M13a.Q2 — Log-loss et cross-entropy : la même chose ?
1. $-\ln 0{,}9 \approx 0{,}105$ nat.
2. Log-loss $= -\frac{1}{n}\,\ell$ : moins la log-vraisemblance des labels, divisée par $n$.
3. **Vrai** : chaque terme est la cross-entropy entre la loi du label observé (toute la masse sur lui) et la loi prédite sur $\{0, 1\}$.
4. Non : chaque terme vaut $-\ln 0{,}5$, quel que soit le label ; la log-loss vaut $\ln 2 \approx 0{,}693$.
5. 0,2 : la log-loss moyenne $H(0{,}2) + \mathrm{KL}(0{,}2 \,\Vert\, q)$ est la plus petite en $q = 0{,}2$. Le taux d'erreur, non : toutes les probabilités sous 0,5 donnent la même décision (label 0) et la même erreur moyenne, 0,2.
6. L'accuracy ne regarde que le côté de 0,5 ; la log-loss regarde la probabilité elle-même : un modèle qui répond 0,51 et un autre qui répond 0,99 sur les mêmes bons exemples ont la même accuracy, pas la même log-loss.

### M13a.Q3 — Les propriétés de la sigmoïde et de la softplus
1. $\sigma(0) = \frac{1}{2}$, $s(0) = \ln 2 \approx 0{,}693$.
2. $\sigma(z) + \sigma(-z) = 1$ ; $s(z) - s(-z) = z$.
3. **Vrai** : $s(z) > 0$ (car $1 + e^z > 1$) et $s(z) > z$ (car $1 + e^z > e^z$).
4. $-\ln\sigma(z) = s(-z)$ et $-\ln(1 - \sigma(z)) = s(z)$.
5. $e^{900}$ déborde (au-delà d'environ $1{,}8 \times 10^{308}$) : le résultat est `inf`, avec un avertissement. On calcule $\max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$, avec `np.log1p`.
6. $y = 0$ (quand $z \to -\infty$) et $y = z$ (quand $z \to +\infty$).

### M13a.Q4 — Ce que modélise un score w · x + b
1. La **log-cote** : $z = \ln\frac{P(Y = 1 \mid \mathbf{x})}{P(Y = 0 \mid \mathbf{x})}$.
2. $\mathbf{w} \cdot \mathbf{x} + b = 0$, un hyperplan.
3. Un hyperplan $\mathbf{w} \cdot \mathbf{x} + b = \operatorname{logit}(0{,}9)$, parallèle à la frontière, du côté où $\mathbf{w}$ pointe.
4. Par $e^{-0{,}4} \approx 0{,}670$, quel que soit le point de départ. La probabilité, non : elle change beaucoup près de 0,5, peu près de 0 ou de 1.
5. 0,17 : leurs scores sont opposés, et $\sigma(-z) = 1 - \sigma(z)$.
6. 21 : 20 poids et un biais.

### M13a.Q5 — Génératif ou discriminant ?
1. La régression logistique modélise $P(Y \mid \mathbf{x})$ (discriminant) ; Naïve Bayes modélise $p(\mathbf{x} \mid Y)$ et $P(Y)$ (génératif).
2. Naïve Bayes : il a une loi des features dans chaque classe, qu'on peut tirer au hasard.
3. **Faux** : indépendantes **sachant la classe**. Sans connaître la classe, elles peuvent être très corrélées.
4. Une sigmoïde d'une fonction affine de $x$ : $\sigma(wx + b)$.
5. Oui, souvent : la décision ne demande que de savoir quelle classe l'emporte. Ses probabilités, en revanche, sont souvent trop proches de 0 ou de 1 (une information comptée plusieurs fois).
6. Le produit de 300 probabilités ou densités tombe à 0 (ou déborde) en flottants ; la somme de leurs logarithmes reste un nombre ordinaire, et log-somme-exp normalise ensuite.

### M13a.Q6 — Entropie et Gini : leurs propriétés
1. 0 et 0.
2. $\log_2 K$ et $1 - \frac{1}{K}$, pour la loi uniforme.
3. $1 - 0{,}81 - 0{,}0025 - 0{,}0025 = 0{,}185$.
4. **Vrai** : $\sum_k p_k(1 - p_k) = \sum_k p_k - \sum_k p_k^2 = 1 - \sum_k p_k^2$, et $p_k(1 - p_k)$ est la variance de l'indicatrice « la classe est $k$ ».
5. Les impuretés sont concaves : l'impureté du groupe entier, un mélange des deux sous-groupes, est au moins la moyenne pondérée des impuretés des sous-groupes.
6. 0 : $H(Y \mid X) = H(Y)$ quand $X$ et $Y$ sont indépendantes.

### M13a.Q7 — Variance intra et variance inter : les feuilles d'un arbre de régression
1. La moyenne de ses cibles : la constante qui minimise la somme des carrés des écarts (M07).
2. Variance totale = variance intra-groupes + variance inter-groupes.
3. **Vrai** : chaque terme $(m_A - m)^2$ est nul, puisque $m_A = m_B = m$.
4. $\frac{2}{10} = 0{,}2$ et $\frac{8}{10} = 0{,}8$.
5. L'indice de Gini est la somme des variances des indicatrices de classe : la variance du vecteur one-hot des labels.

### M13a.Q8 — Convexe ou pas ?
1. Oui : $s(z) = \mathrm{LSE}(0, z)$, LSE composée avec une application affine (fiche §3).
2. Non : elle est convexe pour $z < 0$ et concave pour $z > 0$ (sa courbe en S change de concavité en 0).
3. Oui : sur toute droite, sa dérivée seconde est une variance, positive (∂ M13a.15).
4. Oui : $-\ln\sigma(z) = s(-z)$, la softplus composée avec $z \mapsto -z$.
5. Oui : une somme de softplus de fonctions affines de $(\mathbf{w}, b)$, plus une fonction affine (fiche §4).
6. Non : il est constant par morceaux (il ne change que quand un exemple change de côté), avec des sauts ; une fonction qui saute n'est pas convexe, et sa « pente » est nulle presque partout.

<a id="rappels"></a>

## 🔁 Rappels

### M13a.R1 — Bayes et le lissage de Laplace (M04)
1. $\frac{0{,}02 \times 0{,}8}{0{,}02 \times 0{,}8 + 0{,}98 \times 0{,}1} = \frac{0{,}016}{0{,}114} \approx 0{,}140$.
2. $\frac{0 + 1}{9 + 2} = \frac{1}{11} \approx 0{,}091$.
3. $\big(\frac{5}{9}, \frac{1}{9}, \frac{3}{9}\big)$ : on ajoute 1 à chaque comptage et 3 au total.
4. Pour ne pas tomber à 0 en flottants (un produit de nombreuses probabilités est minuscule), et parce qu'une somme se manipule mieux qu'un produit.
5. $\ln(2 + 6) = \ln 8 \approx 2{,}079$.

### M13a.R2 — Entropie, cross-entropy et information mutuelle (M06)
1. $3 \times 0{,}25 \times 2 + 2 \times 0{,}125 \times 3 = 1{,}5 + 0{,}75 = 2{,}25$ bits.
2. $H(\mathbf{p}, \mathbf{q}) = 0{,}85\log_2\frac{1}{0{,}6} + 0{,}15\log_2\frac{1}{0{,}4} \approx 0{,}825$ bit ; $H(\mathbf{p}) \approx 0{,}610$ ; $\mathrm{KL}(\mathbf{p} \,\Vert\, \mathbf{q}) = H(\mathbf{p}, \mathbf{q}) - H(\mathbf{p}) \approx 0{,}215$ bit.
3. Pour deux lois $\mathbf{p}$ et $\mathbf{q}$ : $H(\mathbf{p}, \mathbf{q}) \ge H(\mathbf{p})$, autrement dit $\mathrm{KL}(\mathbf{p} \,\Vert\, \mathbf{q}) \ge 0$, avec égalité si et seulement si $\mathbf{p} = \mathbf{q}$.
4. $X$ et $Y$ sont indépendantes (et réciproquement).
5. Diviser par $\ln 2 \approx 0{,}693$ (multiplier par environ 1,443).

### M13a.R3 — Fonctions convexes de plusieurs variables (M10)
1. Pour tous $\mathbf{a}, \mathbf{b}$ et tout $t \in [0, 1]$ : $f\big((1 - t)\,\mathbf{a} + t\,\mathbf{b}\big) \le (1 - t)\,f(\mathbf{a}) + t\,f(\mathbf{b})$.
2. Convexe (avec égalité partout), pas strictement convexe.
3. On additionne les deux inégalités de convexité, terme à terme.
4. Par l'inégalité triangulaire et $\lVert \lambda\mathbf{x} \rVert = \lvert\lambda\rvert\,\lVert \mathbf{x} \rVert$ : $\lVert (1 - t)\,\mathbf{a} + t\,\mathbf{b} \rVert \le (1 - t)\lVert \mathbf{a} \rVert + t\lVert \mathbf{b} \rVert$.
5. Il est convexe.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M13a.1 — Le maximum de vraisemblance d'une loi de Bernoulli et d'une loi catégorielle

**Réponses** : a) `7/20` · b) `-12.9489` · c) `-13.8629` · d) `-0.6474` · e) `[1/4, 9/20, 0, 3/10]` · f) `[0.25, 0.4167, 0.0417, 0.2917]` · g) `[0.25, 0.4405, 0.0119, 0.2976]` · h) `-21.3419`.

**Démarche.** $\ell(p) = 7\ln p + 13\ln(1 - p)$, $\ell'(p) = \frac{7}{p} - \frac{13}{1 - p} = 0$ donne $7(1 - p) = 13p$, $\hat{p} = \frac{7}{20}$ ; $\ell'' < 0$. b) $7\ln 0{,}35 + 13\ln 0{,}65 \approx -7{,}349 - 5{,}600$. c) $20\ln 0{,}5$. d) b) divisé par 20. e) $\frac{n_k}{20}$. f) $\frac{n_k + 1}{24}$ : $\big(\frac{6}{24}, \frac{10}{24}, \frac{1}{24}, \frac{7}{24}\big)$. g) $\frac{n_k + 0{,}25}{21}$. h) $5\ln\frac{1}{4} + 9\ln\frac{9}{20} + 6\ln\frac{3}{10}$ (le forfait jamais choisi ne compte pas).

Pour la copie : un 21ᵉ client qui choisit le troisième forfait ajoute $\ln\hat{p}_3 = \ln 0 = -\infty$ : la log-vraisemblance devient $-\infty$, le modèle déclarait l'événement impossible. Le lissage ajoute $K\alpha$ au dénominateur : toutes les probabilités baissent un peu pour faire de la place au forfait jamais vu (ici, la première ne bouge pas par hasard : $\frac{5}{20} = \frac{6}{24}$).

**Erreurs fréquentes.** La proportion de bonnes pièces ($\frac{13}{20}$) ; un logarithme décimal ; ajouter $\alpha$ au numérateur sans ajouter $K\alpha$ au dénominateur (les probabilités ne somment plus à 1).

**Variante.** On contrôle 10 pièces de plus, dont 3 défectueuses : le nouveau $\hat{p}$ ? *Réponse* : $\frac{10}{30} = \frac{1}{3}$ (les comptages s'additionnent).

### Ex M13a.2 — Le maximum de vraisemblance d'une loi normale : μ̂ et σ̂²

**Réponses** : a) `256` · b) `458` · c) `76.3333` · d) `91.6` · e) `8.7369` · f) `-21.519` · g) `-21.5659` · h) `5/6`.

**Démarche.** $\sum x_i = 1\,536$, $\hat{\mu} = 256$ ; écarts $-11, 6, -5, 14, -8, 4$, carrés $121, 36, 25, 196, 64, 16$, $S = 458$. c) $\frac{458}{6}$. d) $\frac{458}{5}$. e) $\sqrt{76{,}333}$. f) $-\frac{6}{2}\big(\ln(2\pi \times 76{,}333) + 1\big) \approx -3 \times 7{,}173$. g) $-3\ln(2\pi \times 91{,}6) - \frac{458}{2 \times 91{,}6}$. h) $\frac{n - 1}{n} = \frac{5}{6}$ (M02c).

Pour la copie : $\frac{\partial \ell}{\partial \mu} = \frac{1}{v}\sum_i (x_i - \mu) = 0$ donne $\hat{\mu} = \bar{x}$ ; $\frac{\partial \ell}{\partial v} = -\frac{n}{2v} + \frac{S}{2v^2} = 0$ donne $v = \frac{S}{n}$, positif avant, négatif après. En $(\hat{\mu}, \hat{\sigma}^2)$, $\frac{S}{2\hat{\sigma}^2} = \frac{n}{2}$, d'où la formule. g) est plus petit parce que f) est **le** maximum de $\ell$ : toute autre variance, même l'estimation sans biais, rend les données moins probables.

**Erreurs fréquentes.** Diviser par $n - 1$ pour le maximum de vraisemblance ; dériver en $\sigma$ au lieu de $\sigma^2$ (on trouve le même point, mais les calculs sont plus lourds) ; oublier le terme $-\frac{n}{2}\ln(2\pi v)$ dans $\ell$.

**Variante.** Un septième temps de 256 ms : $\hat{\mu}$ et $\hat{\sigma}^2$ ? *Réponse* : 256 et $\frac{458}{7} \approx 65{,}43$.

### Ex M13a.3 — La log-loss de quatre prédictions, puis la même en cross-entropy

**Réponses** : a) `[0.2231, 0.7985, 0.4308, 0.0513]` · b) `0.3759` · c) `0.542` · d) `-1.5037` · e) `3/4` · f) `0.6931` · g) `1.204` · h) `0.2026`.

**Démarche.** a) $-\ln 0{,}8$, $-\ln 0{,}45$ (labels 1), puis $-\ln 0{,}65$, $-\ln 0{,}95$ (labels 0 : $1 - \hat{p}$). b) leur moyenne. c) b) divisé par $\ln 2$. d) moins la somme des termes. e) décisions $1, 0, 0, 0$ contre labels $1, 1, 0, 0$ : trois justes. f) $\ln 2$. g) $-\ln 0{,}3$. h) le deuxième terme devient $-\ln 0{,}9 \approx 0{,}105$, moyenne $\approx 0{,}203$.

Pour la copie : le terme du premier exemple est $H\big((0, 1), (0{,}2 ;\ 0{,}8)\big) = -\ln 0{,}8$, et ainsi de suite. De b) à h), la log-loss baisse de 0,376 à 0,203, et l'accuracy passe de $\frac{3}{4}$ à 1. Mais même sans changer de décision (0,45 remplacé par 0,1, toujours du mauvais côté), la log-loss aurait bougé : elle mesure la **confiance** que le modèle accorde au bon label, l'accuracy seulement le côté de 0,5.

**Erreurs fréquentes.** $-\ln\hat{p}$ pour les labels 0 ; la somme au lieu de la moyenne ; multiplier par $\ln 2$ au lieu de diviser.

**Variante.** Si le dernier exemple avait le label 1 (même $\hat{p} = 0{,}05$) : son terme ? *Réponse* : $-\ln 0{,}05 \approx 3{,}00$.

### Ex M13a.4 — Ce que coûte une prédiction sûre et fausse : la log-loss quand p tend vers 0

**Réponses** : a) `0.0202` · b) `0.0294` · c) `0.0478` · d) `20.18` · e) `0.0547` · f) `13.2877` · g) `False`.

**Démarche.** Les 999 exemples pèsent $999 \times (-\ln 0{,}98) \approx 20{,}18$. b) $\frac{20{,}18 + 9{,}21}{1\,000}$. c) $\frac{20{,}18 + 27{,}63}{1\,000}$. d) $-\ln q = 999 \times 0{,}020\,203 \approx 20{,}18$ (soit $q \approx 1{,}7 \times 10^{-9}$) : garde assez de chiffres de a), le facteur 999 grossit l'arrondi. e) $\frac{20{,}18 + 34{,}54}{1\,000}$. f) $\log_2 10^4 \approx 13{,}29$ bits. g) $-\ln q \to +\infty$.

Pour la copie : le taux d'erreur vaut $\frac{1}{1\,000}$ dans b) et c) (un exemple du mauvais côté) et 0 dans a) ; il ne distingue pas b) de c). Une probabilité exactement 0 donne $-\ln 0 = +\infty$ : la log-loss devient infinie et inutilisable ; l'écrêtage remplace 0 par un tout petit nombre, ce qui garde un nombre fini mais énorme. Un modèle a donc intérêt à ne jamais annoncer 0 ou 1 exactement.

**Erreurs fréquentes.** Oublier de diviser par 1 000 ; confondre $q$ et $-\ln q$ ; des nats au lieu de bits pour f).

**Variante.** Sur 100 exemples au lieu de 1 000 (99 à 0,98, un à $10^{-4}$) ? *Réponse* : $\frac{99 \times 0{,}0202 + 9{,}21}{100} \approx 0{,}112$.

### Ex M13a.5 — La sigmoïde : valeurs, logit, cote et symétrie σ(−z) = 1 − σ(z)

**Réponses** : a) `0.69` · b) `0.0759` · c) `1` · d) `-1.7346` · e) `3/17` · f) `2.9444` · g) `5/7` · h) `6/23`.

**Démarche.** a) $\frac{1}{1 + e^{-0{,}8}} = \frac{1}{1 + 0{,}4493} \approx 0{,}6900$. b) $\frac{1}{1 + e^{2{,}5}} \approx 0{,}0759$. c) la symétrie. d) $\ln\frac{0{,}15}{0{,}85}$. e) $\frac{0{,}15}{0{,}85} = \frac{3}{17}$. f) $\ln\frac{0{,}95}{0{,}05} = \ln 19$. g) $\frac{2{,}5}{1 + 2{,}5} = \frac{5}{7}$. h) la cote passe de $\frac{3}{17}$ à $\frac{6}{17}$, d'où $p = \frac{6/17}{1 + 6/17} = \frac{6}{23}$.

Pour la copie : $1 - \sigma(z) = \frac{e^{-z}}{1 + e^{-z}}$, donc $\frac{\sigma(z)}{1 - \sigma(z)} = \frac{1}{e^{-z}} = e^z$ ; et $1 - \sigma(z) = \frac{1}{e^{z} + 1} = \sigma(-z)$ (multiplie haut et bas par $e^z$). Ajouter $\ln 2$ au score multiplie la cote par $e^{\ln 2} = 2$.

**Erreurs fréquentes.** $\frac{1}{1 + e^{z}}$ (le signe) ; la cote inversée $\frac{1 - p}{p}$ ; doubler la probabilité au lieu de la cote (h : 0,3 est faux).

**Variante.** Le logit de 0,85 ? *Réponse* : $\ln\frac{17}{3} \approx 1{,}735$, l'opposé de d).

### Ex M13a.6 — La softplus : valeurs, asymptotes et comportement pour |z| grand

**Réponses** : a) `2.5789` · b) `0.0789` · c) `5/2` · d) `0.002476` · e) `0.0328` · f) `1.1032` · g) `True` · h) `0.6931`.

**Démarche.** a) $\ln(1 + e^{2{,}5}) = \ln 13{,}18$. b) $\ln(1 + e^{-2{,}5}) = \ln 1{,}0821$. c) $s(z) - s(-z) = z$. d) $\ln(1 + e^{-6}) \approx e^{-6}$. e) $0 + \ln(1 + e^{-3{,}4}) \approx 0{,}0328$. f) $-\ln(1 - \sigma(0{,}7)) = s(0{,}7) = \ln(1 + e^{0{,}7})$. g) $s(z) > 0$ et $s(z) > z$. h) $\ln(1 + e^{-\lvert z \rvert})$ est le plus grand en $z = 0$ : $\ln 2$.

Pour la copie : $s(z) - s(-z) = \ln\frac{1 + e^z}{1 + e^{-z}} = \ln e^z = z$, et $s(z) - z = \ln\frac{1 + e^z}{e^z} = \ln(1 + e^{-z}) \to 0$ quand $z \to +\infty$ : asymptote $y = z$ ; quand $z \to -\infty$, $s(z) \to \ln 1 = 0$ : asymptote $y = 0$. Dans un programme, $e^{-\lvert z \rvert} \le 1$ ne déborde jamais, alors que $e^z$ déborde au-delà de 709 environ.

**Erreurs fréquentes.** Un logarithme décimal ; croire $s(6) - 6 = 0$ ; calculer $s(3{,}4)$ au lieu de $s(-3{,}4)$.

**Variante.** $s(-6)$ ? *Réponse* : la même valeur que d), $\approx 0{,}002476$ ($s(-6) = s(6) - 6$).

### Ex M13a.7 — Un modèle logistique à deux features : probabilités, cote et frontière de décision

**Réponses** : a) `-1.4` · b) `0.1978` · c) `1.4918` · d) `3.0042` · e) `1.6364` · f) `3.2133` · g) `0.3068` · h) `0.0392`.

**Démarche.** a) $0{,}7 + 1{,}1 - 3{,}2$. b) $\sigma(-1{,}4)$. c) $z_B = 1{,}4 + 2{,}2 - 3{,}2 = 0{,}4$, cote $e^{0{,}4}$. d) $e^{1{,}1}$. e) $0{,}7 \times 2 + 1{,}1\,x_2 - 3{,}2 = 0$ : $x_2 = \frac{1{,}8}{1{,}1}$. f) $1{,}4 + 1{,}1\,x_2 - 3{,}2 = \ln\frac{0{,}85}{0{,}15}$ : $x_2 = \frac{1{,}8 + 1{,}7346}{1{,}1}$. g) $\frac{z_B}{\lVert \mathbf{w} \rVert} = \frac{0{,}4}{\sqrt{0{,}49 + 1{,}21}}$. h) $\sigma(-3{,}2)$.

Pour la copie : $P = 0{,}85$ équivaut à $\mathbf{w} \cdot \mathbf{x} + b = \operatorname{logit}(0{,}85)$, une droite de même vecteur normal $\mathbf{w}$ que la frontière : elles sont parallèles. La probabilité augmente le plus vite dans la direction de $\mathbf{w}$, orthogonale aux lignes de niveau.

**Erreurs fréquentes.** Le signe du biais ; donner la probabilité au lieu de la cote ; $w_2$ au lieu de $e^{w_2}$ ; oublier de diviser par $\lVert \mathbf{w} \rVert$ pour la distance.

**Variante.** $P(Y = 1 \mid (3, 2))$ ? *Réponse* : $z = 2{,}1 + 2{,}2 - 3{,}2 = 1{,}1$, $\sigma(1{,}1) \approx 0{,}750$.

### Ex M13a.8 — L'hypothèse naïve à la main : une loi jointe factorisée, comparée à la vraie

**Réponses** : a) `7/10` · b) `21/100` · c) `5/8` · d) `0.3727` · e) `0.5172` · f) `0.6935` · g) `2` · h) `[2047, 21]`.

**Démarche.** Classe 1 : $P(x_1 = 1) = 0{,}25 + 0{,}45 = 0{,}7$ et $P(x_2 = 1) = 0{,}7$ ; classe 0 : $0{,}38$ et $0{,}38$. b) $0{,}3 \times 0{,}7$. c) $\frac{0{,}4 \times 0{,}25}{0{,}4 \times 0{,}25 + 0{,}6 \times 0{,}10} = \frac{0{,}1}{0{,}16}$. d) $\frac{0{,}4 \times 0{,}21}{0{,}4 \times 0{,}21 + 0{,}6 \times 0{,}62 \times 0{,}38}$. e) $\frac{0{,}18}{0{,}18 + 0{,}168}$. f) $\frac{0{,}4 \times 0{,}49}{0{,}196 + 0{,}6 \times 0{,}1444}$. g) a posteriori vrais $(0{,}060 ;\ 0{,}625 ;\ 0{,}625 ;\ 0{,}517)$, naïfs $(0{,}135 ;\ 0{,}373 ;\ 0{,}373 ;\ 0{,}693)$ : les cases $(0, 1)$ et $(1, 0)$ changent de décision. h) $2 \times (2^{10} - 1) + 1$ et $2 \times 10 + 1$.

Pour la copie : non, $P(1, 1 \mid Y = 1) = 0{,}45 \ne 0{,}7 \times 0{,}7 = 0{,}49$ ; dans la classe 1, avoir exactement une des deux features est plus fréquent que ne le dit le produit ($0{,}25$ contre $0{,}21$) ; surtout, dans la classe 0, la case $(0, 1)$ vaut $0{,}10$ pour de vrai et $0{,}62 \times 0{,}38 \approx 0{,}236$ une fois factorisée, plus du double : la classe 0 y devient beaucoup plus vraisemblable qu'elle ne l'est. Elle a aussi l'excès inverse en $(1, 1)$ ($0{,}28$ contre $0{,}144$). Naïve Bayes ignore ces dépendances et inverse deux décisions. Quand l'hypothèse est presque vraie, les produits sont proches des vraies probabilités, et la classe qui l'emporte reste la même.

**Erreurs fréquentes.** Prendre la vraie probabilité jointe au lieu du produit des marginales ; oublier les proportions des classes ; compter $2^{10}$ au lieu de $2^{10} - 1$ probabilités libres.

**Variante.** Avec des classes équiprobables, l'a posteriori naïf en $(0, 1)$ ? *Réponse* : $\frac{0{,}21}{0{,}21 + 0{,}2356} \approx 0{,}471$.

### Ex M13a.9 — Deux classes gaussiennes de même variance : l'a posteriori est une sigmoïde d'un score affine

**Réponses** : a) `1` · b) `-1.619` · c) `1.619` · d) `0.35` · e) `0.799` · f) `1` · g) `2.7183` · h) `0.0694`.

**Démarche.** a) $\frac{3 - (-1)}{4}$. b) $\frac{1 - 9}{8} + \ln\frac{0{,}35}{0{,}65} = -1 - 0{,}619$. c) $-\frac{b}{w}$. d) $\sigma(1 - 1{,}619) = \sigma(\ln\frac{0{,}35}{0{,}65}) = 0{,}35$. e) $\sigma\big(2 + \ln\frac{7}{13}\big) = \frac{7e^2}{7e^2 + 13} \approx 0{,}799$ (avec b) arrondi, on trouve 0,7992 à 4 décimales : d'où les 3 décimales demandées). f) le milieu $\frac{-1 + 3}{2}$. g) $e^w = e$. h) $-\frac{1}{2 \times 9} + \frac{1}{2 \times 4} = \frac{-4 + 9}{72} = \frac{5}{72}$.

Pour la copie : $\ln\frac{P(1 \mid x)}{P(0 \mid x)} = \ln\frac{\pi_1}{\pi_0} - \frac{(x - 3)^2}{8} + \frac{(x + 1)^2}{8}$ : les $x^2$ s'annulent, il reste $x - 1 + \ln\frac{0{,}35}{0{,}65}$. En $x = 1$, le milieu des moyennes, les deux densités sont égales : l'a posteriori vaut l'a priori. Dans le cas h), la log-cote est un polynôme du second degré en $x$ : la frontière est formée de deux points (au plus), la classe 1, plus étalée, l'emportant aux deux extrémités.

**Erreurs fréquentes.** Diviser par $\sigma$ au lieu de $\sigma^2$ ; oublier $\ln\frac{\pi_1}{\pi_0}$ ; placer la frontière au milieu des moyennes malgré des classes inégales.

**Variante.** Avec $\sigma^2 = 1$ (même proportions) : $w$ et $x^*$ ? *Réponse* : $w = 4$, $b = -4 - 0{,}619$, $x^* \approx 1{,}155$ : la frontière se rapproche du milieu quand les classes se séparent mieux.

### Ex M13a.10 — L'entropie et l'indice de Gini de quelques distributions

**Réponses** : a) `0.095` · b) `0.2864` · c) `0.64` · d) `1.5219` · e) `7/4` · f) `21/32` · g) `2.585` · h) `5/6`.

**Démarche.** a) $1 - 0{,}9025 - 0{,}0025$. b) $0{,}95\log_2\frac{1}{0{,}95} + 0{,}05\log_2 20$. c) $1 - 0{,}16 - 0{,}16 - 0{,}04$. d) $2 \times 0{,}4\log_2 2{,}5 + 0{,}2\log_2 5$. e) $\frac{1}{2} \times 1 + \frac{1}{4} \times 2 + 2 \times \frac{1}{8} \times 3$. f) $1 - \frac{1}{4} - \frac{1}{16} - \frac{2}{64}$. g) $\log_2 6$. h) $1 - \frac{1}{6}$.

Pour la copie : par entropie, $\mathbf{p}_1 < \mathbf{p}_2 < \mathbf{p}_3$ (0,29 ; 1,52 ; 1,75) ; par Gini, $\mathbf{p}_1 < \mathbf{p}_2 < \mathbf{p}_3$ aussi (0,095 ; 0,64 ; 0,656). Le rangement est le même ici, mais ce n'est pas garanti. Les maxima dépendent du nombre de classes ($\log_2 K$, $1 - \frac{1}{K}$) : une impureté de 1,5 bit est très mélangée pour 3 classes, assez peu pour 8.

**Erreurs fréquentes.** Des nats au lieu de bits ; confondre Gini et taux d'erreur ($1 - \max_k p_k$) ; $\frac{1}{K}$ pour le maximum de Gini.

**Variante.** $(0{,}6 ;\ 0{,}2 ;\ 0{,}2)$ ? *Réponse* : $G = 0{,}56$, $H \approx 1{,}371$ bit.

### Ex M13a.11 — L'information mutuelle d'un tableau de contingence, et la baisse d'entropie qu'elle mesure

**Réponses** : a) `13/20` · b) `0.9341` · c) `0.5665` · d) `0.8632` · e) `0.0709` · f) `1.571` · g) `0.0403` · h) `0`.

**Démarche.** b) $H(0{,}65 ;\ 0{,}35)$. Lignes : bus $(0{,}55 ;\ 0{,}45)$, $H \approx 0{,}9928$ ; vélo $(\frac{26}{30}, \frac{4}{30})$, $H \approx 0{,}5665$ ; voiture $(\frac{17}{30}, \frac{13}{30})$, $H \approx 0{,}9871$. d) $0{,}4 \times 0{,}9928 + 0{,}3 \times 0{,}5665 + 0{,}3 \times 0{,}9871$ (garde 4 décimales dans les intermédiaires). e) b) − d). f) $H(0{,}4 ;\ 0{,}3 ;\ 0{,}3)$. g) $G(Y) = 1 - 0{,}65^2 - 0{,}35^2 = 0{,}455$, moyenne pondérée des Gini des lignes $0{,}4 \times 0{,}495 + 0{,}3 \times 0{,}231 + 0{,}3 \times 0{,}491 \approx 0{,}4147$. h) indépendance : $I = 0$.

Pour la copie : la formule somme six termes $p(x, y)\log_2\frac{p(x, y)}{p(x)\,p(y)}$ et redonne $0{,}0709$. C'est la ligne « vélo » qui fait baisser l'entropie : la seule qui s'écarte nettement de $(0{,}65 ;\ 0{,}35)$. $I(X ; Y) = H(Y)$ voudrait dire $H(Y \mid X) = 0$ : connaître le mode de transport suffirait à savoir si l'on arrive à l'heure.

**Erreurs fréquentes.** Des nats ; la moyenne non pondérée des entropies des lignes ; donner $H(Y \mid X)$ au lieu de la baisse.

**Variante.** $H(Y \mid X = \text{bus})$ ? *Réponse* : $\approx 0{,}993$, plus que $H(Y)$ : sachant qu'on prend le bus, l'incertitude **augmente** ; c'est seulement en moyenne que connaître $X$ la fait baisser.

### Ex M13a.12 — La variance d'un groupe coupé en deux : variance intra plus variance inter

**Réponses** : a) `13.7143` · b) `28.4898` · c) `[8, 18]` · d) `[2.6667, 5.0]` · e) `4.0` · f) `24.4898` · g) `True` · h) `33.2381`.

**Démarche.** a) $\frac{96}{7}$. b) $\frac{1}{7}\sum (y - 13{,}714)^2$. c) $\frac{24}{3}$, $\frac{72}{4}$. d) $\frac{4 + 4 + 0}{3}$, $\frac{9 + 1 + 1 + 9}{4}$. e) $\frac{3}{7} \times \frac{8}{3} + \frac{4}{7} \times 5 = \frac{8 + 20}{7} = 4$. f) $\frac{3}{7}(8 - 13{,}714)^2 + \frac{4}{7}(18 - 13{,}714)^2$. h) b) $\times \frac{7}{6}$.

Pour la copie : dans $A$, $\sum_{y \in A}(y - m)^2 = \sum_{y \in A}(y - m_A)^2 + 2(m_A - m)\sum_{y \in A}(y - m_A) + n_A(m_A - m)^2$, et la somme du milieu est nulle (les écarts à la moyenne d'un groupe ont une somme nulle). On fait de même dans $B$, on additionne et on divise par $n$. Avec $\frac{1}{n - 1}$, les variances des groupes seraient en $\frac{1}{n_A - 1}$ et $\frac{1}{n_B - 1}$ : les poids ne s'accordent plus, et la décomposition perd sa forme simple.

**Erreurs fréquentes.** La moyenne non pondérée des variances ; mélanger $\frac{1}{n}$ et $\frac{1}{n - 1}$.

**Variante.** Autre coupe : $(6, 10)$ et $(8, 15, 19, 17, 21)$ : variances intra et inter ? *Réponse* : $\approx 15{,}43$ et $\approx 13{,}06$ ; la somme est toujours 28,49, mais cette coupe sépare moins bien les cibles.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M13a.13 — Le maximum de vraisemblance d'une loi catégorielle, par l'inégalité de Gibbs

**Réponse modèle.**
1. $\frac{1}{N}\ell(\mathbf{p}) = \sum_k \frac{n_k}{N}\ln p_k = \sum_k \hat{p}_k\ln p_k = -H(\hat{\mathbf{p}}, \mathbf{p})$.
2. Gibbs : $H(\hat{\mathbf{p}}, \mathbf{p}) \ge H(\hat{\mathbf{p}}, \hat{\mathbf{p}}) = H(\hat{\mathbf{p}})$, avec égalité si et seulement si $\mathbf{p} = \hat{\mathbf{p}}$. En multipliant par $-N$ : $\ell(\mathbf{p}) \le -N\,H(\hat{\mathbf{p}}) = \ell(\hat{\mathbf{p}})$.
3. Si $n_k = 0$, $\hat{p}_k = 0$ : $\hat{\mathbf{p}}$ sort du domaine des lois à valeurs strictement positives, et l'on étend $\ell$ par la convention $0\ln 0 = 0$ (le terme $n_k\ln p_k$ vaut alors 0 pour tout $p_k$) ; avec $0\ln 0 = 0$, l'inégalité de Gibbs reste vraie (elle somme sur les $k$ où $\hat{p}_k > 0$), et le maximum met $p_k = 0$ : toute masse donnée à une valeur jamais vue est perdue pour les autres.
4. $\ell(\mathbf{p}) - \ell(\hat{\mathbf{p}}) = -N\big(H(\hat{\mathbf{p}}, \mathbf{p}) - H(\hat{\mathbf{p}})\big) = -N\,\mathrm{KL}(\hat{\mathbf{p}} \,\Vert\, \mathbf{p})$.
5. Le même raisonnement avec les comptages $n_k + \alpha$ (de total $N + K\alpha$) : $\sum_k (n_k + \alpha)\ln p_k$ est maximale en $p_k = \frac{n_k + \alpha}{N + K\alpha}$. Le lissage est un maximum de vraisemblance sur des données augmentées de $\alpha$ observations fictives de chaque valeur.

**Grille.** (1) la réécriture en cross-entropy avec $\hat{p}_k = n_k/N$ ; (2) Gibbs et le cas d'égalité, le signe en multipliant par $-N$ ; (3) le cas $n_k = 0$ traité ; (4) la KL ; (5) les pseudo-comptages.

### Ex M13a.14 — La log-loss moyenne est moins la log-vraisemblance divisée par n

**Réponse modèle.**
1. $P(y_i) = \hat{p}_i^{\,y_i}(1 - \hat{p}_i)^{1 - y_i}$ : cela vaut $\hat{p}_i$ si $y_i = 1$ et $1 - \hat{p}_i$ si $y_i = 0$.
2. Par indépendance sachant les features, $L = \prod_i \hat{p}_i^{\,y_i}(1 - \hat{p}_i)^{1 - y_i}$, $\ln L = \sum_i \big[y_i\ln\hat{p}_i + (1 - y_i)\ln(1 - \hat{p}_i)\big]$, et la log-loss est $-\frac{1}{n}\ln L$.
3. $H(\mathbf{e}_{y_i}, \hat{\mathbf{q}}_i) = -\sum_{c \in \{0, 1\}} e_{y_i}(c)\ln\hat{q}_i(c) = -\ln\hat{q}_i(y_i)$, la même chose.
4. $-\frac{1}{n}\sum_i \ln\hat{q}_i(y_i)$, avec $\hat{\mathbf{q}}_i$ la loi prédite sur les $K$ classes : elle suppose chaque label tiré d'une loi catégorielle de paramètres $\hat{\mathbf{q}}_i$, indépendamment.
5. Multiplier une fonction par une constante positive ($\frac{1}{n}$, ou $\frac{1}{\ln 2}$ pour passer en bits) ne change pas l'endroit où elle est minimale.

**Grille.** (1) la formule unique ; (2) l'indépendance, le logarithme, le signe et le $\frac{1}{n}$ ; (3) la cross-entropy avec une loi one-hot ; (4) le cas de $K$ classes et son modèle ; (5) l'argument de la constante positive.

### Ex M13a.15 — Log-somme-exp est convexe : sur une droite, sa dérivée seconde est une variance ; la softplus aussi

**Réponse modèle.**
1. Les $\pi_k(t)$ sont strictement positifs et leur somme vaut $\frac{\sum_k e^{a_k + t d_k}}{\sum_j e^{a_j + t d_j}} = 1$.
2. $g(t) = \ln S(t)$ avec $S(t) = \sum_j e^{a_j + t d_j}$, $S'(t) = \sum_j d_j e^{a_j + t d_j}$, donc $g'(t) = \frac{S'(t)}{S(t)} = \sum_k \pi_k(t)\,d_k$.
3. $\pi_k = \frac{e^{a_k + t d_k}}{S}$ donne $\pi_k' = \frac{d_k e^{a_k + t d_k}S - e^{a_k + t d_k}S'}{S^2} = \pi_k\,(d_k - g'(t))$. Alors $g''(t) = \sum_k \pi_k'\,d_k = \sum_k \pi_k d_k^2 - g'(t)\sum_k \pi_k d_k = \sum_k \pi_k d_k^2 - \big(\sum_k \pi_k d_k\big)^2$ : la variance des $d_k$ sous la loi $\boldsymbol{\pi}(t)$ (l'espérance du carré moins le carré de l'espérance, M02b), positive ou nulle. $g$ est convexe (M05a).
4. La définition de M10 ne compare $f$ qu'en des points d'un même segment $[\mathbf{a}, \mathbf{b}]$, et ce segment est l'image de $[0, 1]$ par $t \mapsto \mathbf{a} + t(\mathbf{b} - \mathbf{a})$ : l'inégalité pour LSE est l'inégalité de convexité de $g$ avec $\mathbf{d} = \mathbf{b} - \mathbf{a}$.
5. $s(z) = \mathrm{LSE}(0, z)$, composée de LSE et de l'application affine $z \mapsto (0, z)$ : convexe. Puis $(\mathbf{w}, b) \mapsto z = \mathbf{w} \cdot \mathbf{x} + b$ est affine, donc $s(z)$ est convexe en $(\mathbf{w}, b)$, et $-yz$ est affine : la somme est convexe.
6. $g'' = 0$ quand les $d_k$ sont tous égaux (une variance nulle, puisque tous les $\pi_k > 0$). Avec $\mathbf{d} = (1, \ldots, 1)$, $g(t) = \mathrm{LSE}(\mathbf{a}) + t$ : $g$ est affine, et LSE n'est pas strictement convexe (ajouter la même constante à tous les $u_k$ l'augmente de cette constante).

**Grille.** (1) une loi de probabilité ; (2) $g'$ comme une moyenne ; (3) $\pi_k'$, puis $g''$ comme une variance, et la convexité de $g$ ; (4) le passage des droites à LSE ; (5) la composition affine, deux fois, et la somme ; (6) le cas d'égalité et la direction $(1, \ldots, 1)$.

### Ex M13a.16 — L'indice de Gini est maximal pour la loi uniforme

**Réponse modèle.**
1. $\sum_k \big(p_k - \frac{1}{K}\big)^2 = \sum_k p_k^2 - \frac{2}{K}\sum_k p_k + \frac{K}{K^2} = \sum_k p_k^2 - \frac{1}{K} \ge 0$.
2. $G = 1 - \sum_k p_k^2 \le 1 - \frac{1}{K}$, avec égalité si et seulement si la somme de carrés du point 1 est nulle, c'est-à-dire $p_k = \frac{1}{K}$ pour tout $k$.
3. Cauchy-Schwarz : $\big(\sum_k p_k \times 1\big)^2 \le \big(\sum_k p_k^2\big)\big(\sum_k 1^2\big)$, soit $1 \le K\sum_k p_k^2$.
4. $p_k^2 \le p_k$ (car $0 \le p_k \le 1$), donc $\sum_k p_k^2 \le 1$ et $G \ge 0$ ; égalité si et seulement si chaque $p_k$ vaut 0 ou 1, c'est-à-dire une classe de probabilité 1.
5. $\mathbf{p} \mapsto \sum_k p_k^2$ est convexe (une somme de fonctions convexes, M10), donc $G$, une constante moins elle, est concave : $G\big(t\,\mathbf{p} + (1 - t)\,\mathbf{q}\big) \ge t\,G(\mathbf{p}) + (1 - t)\,G(\mathbf{q})$.

**Grille.** (1) le développement ; (2) la borne et le cas d'égalité ; (3) Cauchy-Schwarz avec le bon vecteur ; (4) le minimum et son cas d'égalité ; (5) la concavité et l'inégalité du mélange.

### Ex M13a.17 — L'entropie est maximale pour la loi uniforme, par l'inégalité de Gibbs

**Réponse modèle.**
1. $\mathrm{KL}(\mathbf{p} \,\Vert\, \mathbf{u}) = \sum_k p_k\log_2\frac{p_k}{1/K} = \sum_k p_k\log_2 p_k + \log_2 K\sum_k p_k = \log_2 K - H(\mathbf{p})$.
2. $\mathrm{KL} \ge 0$ (Gibbs), donc $H(\mathbf{p}) \le \log_2 K$, avec égalité si et seulement si $\mathbf{p} = \mathbf{u}$.
3. Chaque terme $-p_k\log_2 p_k$ est positif ou nul (pour $0 \le p_k \le 1$), nul si et seulement si $p_k \in \{0, 1\}$ : $H = 0$ si et seulement si une valeur a la probabilité 1.
4. $\log_2 8 = 3$ : c'est le maximum, donc la loi est uniforme, $p_k = \frac{1}{8}$.
5. Une loi uniforme sur $K = 2^m$ valeurs demande $m$ questions oui/non (couper en deux à chaque fois) ; aucune loi sur $K$ valeurs n'en demande plus, en moyenne, avec un bon code (M06 §7), et l'entropie mesure ce nombre moyen.

**Grille.** (1) le calcul de la KL ; (2) Gibbs et le cas d'égalité ; (3) le minimum ; (4) l'application ; (5) le lien avec les codes.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13a.18 — Pont : une sonde linéaire, un modèle logistique en NumPy sur un batch de représentations figées, jusqu'à la log-loss

**Réponses** : a) `[1.4, -1.1, 0.1, -0.4, 1.8, -0.3]` · b) `[0.8022, 0.2497, 0.525, 0.4013, 0.8581, 0.4256]` · c) `0.4121` · d) `5/6` · e) `0.6365` · f) `0.2244` · g) `0` · h) `769`.

**Démarche.** a) $0{,}8 + 0{,}8 - 0{,}2$ ; $-0{,}9 - 0{,}2$ ; $0{,}4 - 0{,}9 + 0{,}8 - 0{,}2$ ; $-1{,}8 + 1{,}6 - 0{,}2$ ; $0{,}4 + 1{,}6 - 0{,}2$ ; $-0{,}9 + 0{,}8 - 0{,}2$. b) $\sigma$ de chaque score. c) les termes $s(z) - yz$ : $s(-1{,}4) \approx 0{,}220$ et $s(-1{,}8) \approx 0{,}153$ (labels 1), $s(-1{,}1) \approx 0{,}287$, $s(0{,}1) \approx 0{,}744$, $s(-0{,}4) \approx 0{,}513$ et $s(-0{,}3) \approx 0{,}554$ (labels 0) ; somme $\approx 2{,}472$, moyenne $\approx 0{,}412$. d) décisions $1, 0, 1, 0, 1, 0$ contre $1, 0, 0, 0, 1, 0$ : une seule erreur, au troisième exemple. e) proportion $\frac{1}{3}$ : $-\big(\frac{1}{3}\ln\frac{1}{3} + \frac{2}{3}\ln\frac{2}{3}\big) \approx 0{,}6365$. f) $0{,}6365 - 0{,}4121$. g) $z = 0{,}4 - 0{,}9 - 0{,}2 = -0{,}7 < 0$. h) 768 poids et un biais.

Pour la copie : `z = H @ w + b`. $\ln 2$ est la log-loss d'un modèle qui répond 0,5 ; mais un modèle qui ne regarde pas les représentations peut faire mieux, en répondant la fréquence des 1 : c'est lui qu'il faut battre. Une log-loss de test bien plus basse que e) dirait que la propriété est **linéairement** lisible dans la représentation (sans dire que le réseau s'en sert).

**Erreurs fréquentes.** Oublier le biais ; la somme au lieu de la moyenne ; comparer à $\ln 2$.

**Variante.** Avec $b = 0$ : les scores ? *Réponse* : $(1{,}6 ;\ -0{,}9 ;\ 0{,}3 ;\ -0{,}2 ;\ 2 ;\ -0{,}1)$.

### Ex M13a.19 — MML §8.3, relu après M04 : estimer des paramètres, et ce que la régression logistique y ajoute

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. Le livre note $L$ (ou $\mathcal{L}$) **moins** la log-vraisemblance, $-\log p(\text{données} \mid \boldsymbol{\theta})$ : une quantité à minimiser, comme une loss. C'est $-\ell$ dans la fiche.
2. Il suppose les exemples indépendants et de même loi : la vraisemblance des données est un produit, et moins son logarithme une somme de termes, un par exemple.
3. Avec un bruit gaussien de variance fixée autour d'une prédiction, moins la log-vraisemblance est, à une constante et à un facteur près, la somme des carrés des écarts : les moindres carrés. Avec la fiche : $-\ell(\mu, v) = \frac{n}{2}\ln(2\pi v) + \frac{1}{2v}\sum_i (x_i - \mu)^2$, et à $v$ fixé, seul le second terme dépend de $\mu$.
4. Le MAP ajoute le logarithme d'un a priori sur les paramètres : on maximise $\ell(\boldsymbol{\theta}) + \ln p(\boldsymbol{\theta})$. Le lissage de la fiche est de cette nature : la moyenne de l'a posteriori avec un a priori qui ajoute des pseudo-comptages (M04).
5. $\varphi = \sigma$ et des labels de Bernoulli donnent la régression logistique ; $\varphi$ l'identité et un bruit gaussien, la régression linéaire. Ce sont deux modèles linéaires généralisés, de fonctions de lien le logit et l'identité.
6. Les équations « dérivée nulle » contiennent des sigmoïdes des scores de tous les exemples : elles ne se résolvent pas avec une formule, contrairement aux équations normales. On minimise numériquement, par une descente de gradient ou une méthode de Newton (workbookIA 13).
7. Par exemple : *negative log-likelihood* (moins la log-vraisemblance), *maximum a posteriori* (maximum a posteriori), *link function* (fonction de lien), *overfitting* (overfitting).

**Grille.** (1) la notation et le signe ; (2) l'i.i.d. et la somme ; (3) le bruit gaussien et les moindres carrés, refaits ; (4) le MAP et le lissage ; (5) les deux modèles linéaires généralisés ; (6) l'absence de formule et la méthode numérique ; (7) trois mots.

### Ex M13a.20 — Fermi : la loi jointe complète contre l'hypothèse naïve, combien de nombres pour 30 features à 4 valeurs ?

**Réponse modèle.**
1. $4^{30} - 1 = 2^{60} - 1 \approx 1{,}15 \times 10^{18}$ probabilités par segment.
2. $3 \times 1{,}15 \times 10^{18} \times 8 \approx 2{,}8 \times 10^{19}$ octets, environ 28 exaoctets : près de deux milliards de fois la mémoire d'un ordinateur portable (16 Go $\approx 1{,}6 \times 10^{10}$ octets).
3. $3 \times 30 \times 3 = 270$ probabilités de features, plus 2 pour les proportions des segments : 272.
4. Quelques dizaines d'exemples par case : de l'ordre de $10^{19}$ à $10^{20}$ exemples pour la loi complète, des milliards de fois le nombre d'humains sur Terre ($\approx 8 \times 10^9$) ; pour Naïve Bayes, chaque probabilité s'estime sur tous les exemples d'un segment : quelques centaines à quelques milliers d'exemples suffisent.
5. Les deux, mais surtout les données : même avec une mémoire infinie, presque toutes les cases resteraient vides, et leurs estimations vaudraient 0.

### Ex M13a.21 — Expliquer pourquoi on minimise la log-loss plutôt que le taux d'erreur

**Réponse modèle** (6 à 10 phrases).
> Le taux d'erreur ne regarde que la décision : un modèle qui dit 51 % et un autre qui dit 99 % pour le même client qui finit par acheter ont tous deux raison, et il ne fait pas la différence. Or on se sert souvent de la probabilité elle-même, pour fixer un seuil ou estimer un risque. La log-loss note la probabilité donnée à ce qui s'est vraiment passé : une bonne réponse prudente coûte un peu, une erreur commise avec assurance coûte beaucoup, et la meilleure stratégie est d'annoncer la vraie probabilité. Elle a aussi une forme commode : quand on change un peu les paramètres, le taux d'erreur ne bouge pas (puis saute d'un coup quand un exemple change de côté), alors que la log-loss varie doucement, en une courbe sans creux parasites qu'on sait descendre. Enfin, ce n'est pas un choix arbitraire : minimiser la log-loss, c'est choisir les paramètres qui rendent les labels observés les plus probables. Par exemple, pour un label 1 prédit à 0,6, la log-loss vaut $-\ln 0{,}6 \approx 0{,}51$, et à 0,95, environ 0,05, alors que l'erreur est 0 dans les deux cas. On évalue bien sûr aussi le taux d'erreur à la fin.

En 3 phrases : « Le taux d'erreur ne voit que le côté de 50 % où tombe la prédiction ; la log-loss note la confiance donnée à la bonne réponse, et elle est la plus petite quand le modèle annonce les vraies probabilités. Elle varie doucement et sans faux minimum, alors que le taux d'erreur est fait de marches plates : on sait la minimiser. Et c'est exactement maximiser la vraisemblance des labels. »

**Grille.** (1) ce que l'erreur ne voit pas (la confiance) ; (2) la récompense des probabilités honnêtes ; (3) lisse et convexe contre des marches ; (4) le lien avec la vraisemblance ; (5) un exemple chiffré ; (6) une version en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M13a.E1 — « Pourquoi la cross-entropy est-elle une log-vraisemblance ? »

**Réponse modèle (60 secondes).**

> Un classifieur probabiliste donne, pour chaque exemple, une loi sur les classes. Si l'on suppose les labels indépendants sachant les features, chacun tiré de la loi prédite pour son exemple, la probabilité que le modèle donne aux labels observés est le produit, sur les exemples, de la probabilité prédite pour la bonne classe : c'est la vraisemblance des paramètres. Son logarithme est une somme ; changée de signe et divisée par le nombre d'exemples, c'est la moyenne de moins le logarithme de la probabilité de la bonne classe. Et ce terme est exactement la cross-entropy entre la loi du label observé, qui met toute la masse sur une classe, et la loi prédite. Donc minimiser la cross-entropy, c'est maximiser la vraisemblance. Cette lecture dit deux choses utiles : choisir une loss, c'est choisir un modèle de bruit (la MSE correspond à un bruit gaussien, la cross-entropy à des labels catégoriels) ; et la log-loss récompense les probabilités honnêtes : en moyenne, elle est minimale quand le modèle annonce les vraies probabilités.

**Grille.** (1) le modèle des labels (indépendants, tirés de la loi prédite) ; (2) la vraisemblance comme produit, puis la somme ; (3) moins la moyenne du log = la cross-entropy avec un label one-hot ; (4) l'équivalence des deux minimisations ; (5) une conséquence (le modèle de bruit, les probabilités honnêtes).

### M13a.E2 — « Qu'est-ce que le maximum de vraisemblance, et quel lien avec les losses que vous minimisez ? »

**Réponse modèle (60 secondes).**

> Un modèle est une famille de lois indexée par des paramètres. Une fois les données observées, la vraisemblance est la probabilité de ces données, vue comme une fonction des paramètres ; le maximum de vraisemblance choisit les paramètres qui la rendent la plus grande. Avec des observations indépendantes, c'est un produit, et l'on maximise son logarithme, une somme. Pour une loi de Bernoulli, on retrouve la proportion observée ; pour une loi normale, la moyenne et la variance divisée par n, qui est biaisée, d'où le n − 1 de l'estimation sans biais. Le lien avec les losses : minimiser moins la log-vraisemblance, c'est minimiser une loss. Un bruit gaussien donne les moindres carrés, des labels de Bernoulli donnent la log-loss de la régression logistique, des labels catégoriels la cross-entropy. Deux limites : l'estimation peut être biaisée, et avec beaucoup de paramètres et peu de données, elle colle aux données : c'est l'overfitting, qu'on combat par une régularisation, que l'on peut lire comme un a priori, donc un MAP.

**Grille.** (1) la définition (fonction des paramètres à données fixées) ; (2) i.i.d., produit, logarithme ; (3) deux exemples, dont la variance en $\frac{1}{n}$ et son biais ; (4) deux losses reliées à deux modèles de bruit ; (5) une limite (biais, overfitting, régularisation et MAP).

<a id="notebook"></a>

## Notebook

*(complété avec les exercices M13a.22 à M13a.31)*
