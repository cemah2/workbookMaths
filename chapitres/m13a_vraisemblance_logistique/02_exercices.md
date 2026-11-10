# M13a · Vraisemblance et régression logistique — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m13a_vraisemblance_logistique/06_mes_reponses.md` (créée par `python tools/start_chapter.py M13a`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, les logarithmes sont **népériens** (une log-loss, une log-vraisemblance s'expriment en nats), sauf les entropies et les gains d'information du §6, **en bits** ($\log_2$) ; le maximum de vraisemblance d'une variance divise par $n$ ; une log-loss est une **moyenne** sur les exemples, une log-vraisemblance une **somme** ; les labels valent 0 ou 1, et $\sigma(z) = \frac{1}{1 + e^{-z}}$, $s(z) = \ln(1 + e^z)$.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M13a.Q1 — Vraisemblance, log-vraisemblance, maximum : le vocabulaire 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Vrai ou faux : la vraisemblance $L(\theta)$ est une densité de probabilité en $\theta$.
2. Donne deux raisons de maximiser $\ell = \ln L$ plutôt que $L$.
3. Trente observations i.i.d. : la vraisemblance est-elle un produit ou une somme ? Et la log-vraisemblance ?
4. Sur 40 lancers d'une punaise, 14 retombent pointe en l'air. L'estimation du maximum de vraisemblance de la probabilité « pointe en l'air » ?
5. Vrai ou faux : pour une loi **discrète**, la log-vraisemblance est toujours négative ou nulle. Et pour une loi continue ?
6. Vrai ou faux : l'estimation du maximum de vraisemblance de la variance d'une loi normale est sans biais.

### M13a.Q2 — Log-loss et cross-entropy : la même chose ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. Un modèle donne la probabilité 0,9 au label observé d'un exemple : le terme de cet exemple dans la log-loss, en nats ?
2. Quelle relation exacte relie la log-loss d'un classifieur sur $n$ exemples à la log-vraisemblance de ses labels ?
3. Vrai ou faux : la log-loss binaire est un cas particulier de la cross-entropy.
4. Un modèle répond toujours 0,5. Sa log-loss dépend-elle des labels ? Que vaut-elle ?
5. Un exemple a, en vérité, la probabilité 0,2 d'avoir le label 1. Quelle probabilité un modèle doit-il annoncer pour rendre sa log-loss moyenne la plus petite ? Le taux d'erreur fait-il la même différence ?
6. Pourquoi deux modèles de même accuracy peuvent-ils avoir des log-loss très différentes ?

### M13a.Q3 — Les propriétés de la sigmoïde et de la softplus 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Que valent $\sigma(0)$ et $s(0)$ ?
2. Que vaut $\sigma(z) + \sigma(-z)$ ? Et $s(z) - s(-z)$ ?
3. Vrai ou faux : $s(z) > \max(z, 0)$ pour tout $z$.
4. Écris $-\ln\sigma(z)$ et $-\ln(1 - \sigma(z))$ à l'aide de $s$.
5. Pourquoi `np.log(1 + np.exp(z))` pose-t-il problème pour $z = 900$ ? Que calculer à la place ?
6. Les deux asymptotes de la softplus ?

### M13a.Q4 — Ce que modélise un score w · x + b 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Dans une régression logistique, que vaut exactement le score $z = \mathbf{w} \cdot \mathbf{x} + b$ : la probabilité, la cote ou la log-cote de la classe 1 ?
2. L'équation de la frontière de décision au seuil 0,5 ?
3. Quelle est la forme de l'ensemble des points de probabilité 0,9 ? Et sa position par rapport à la frontière ?
4. $w_2 = -0{,}4$ : $x_2$ augmente de 1, les autres features restent fixes. Par combien la cote est-elle multipliée ? La probabilité change-t-elle de la même quantité partout ?
5. Deux points sont à la même distance de la frontière, de part et d'autre. Si le premier a la probabilité 0,83, quelle est celle du second ?
6. Combien de paramètres pour un modèle logistique à 20 features ?

### M13a.Q5 — Génératif ou discriminant ? 🧠 ★ ⏱️ 4 min
*Fiche §4 et §5 · parcours C, E*

1. La régression logistique modélise-t-elle $P(Y \mid \mathbf{x})$ ou $p(\mathbf{x} \mid Y)$ ? Et Naïve Bayes ?
2. Lequel des deux peut simuler de nouveaux exemples d'une classe ?
3. Vrai ou faux : Naïve Bayes suppose les features indépendantes entre elles.
4. Deux classes gaussiennes de même variance, à une feature : quelle forme a $P(Y = 1 \mid x)$ ?
5. Un modèle génératif dont l'hypothèse est fausse peut-il quand même bien classer ? Que deviennent ses probabilités ?
6. Pour calculer un a posteriori de Naïve Bayes avec 300 features, pourquoi additionner des logarithmes ?

### M13a.Q6 — Entropie et Gini : leurs propriétés 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. L'entropie et l'indice de Gini d'un groupe où toutes les classes sont les mêmes ?
2. Leurs maxima pour $K$ classes, et pour quelle loi ?
3. L'indice de Gini de $(0{,}9 ;\ 0{,}05 ;\ 0{,}05)$ ?
4. Vrai ou faux : $G(\mathbf{p}) = \sum_k p_k(1 - p_k)$, et chaque terme est la variance d'une variable de Bernoulli.
5. Pourquoi couper un groupe en deux ne fait-il jamais monter l'impureté moyenne pondérée ?
6. Le gain d'information d'une feature indépendante de la classe ?

### M13a.Q7 — Variance intra et variance inter : les feuilles d'un arbre de régression 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

1. Quelle constante une feuille d'un arbre de régression prédit-elle, et pourquoi celle-là ?
2. Complète : variance totale = … + ….
3. Vrai ou faux : la variance inter-groupes est nulle si les deux groupes ont la même moyenne.
4. Deux groupes de 2 et de 8 exemples : avec quels poids leurs variances entrent-elles dans la variance intra ?
5. Quel lien entre l'indice de Gini d'un groupe et une variance ?

### M13a.Q8 — Convexe ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §3 et §4 · parcours C*

Pour chaque fonction, dis si elle est convexe, et pourquoi en une ligne.
1. La softplus $s$.
2. La sigmoïde $\sigma$.
3. $\mathrm{LSE}(u_1, u_2, u_3) = \ln(e^{u_1} + e^{u_2} + e^{u_3})$.
4. $z \mapsto -\ln\sigma(z)$.
5. La log-loss d'un modèle logistique, comme fonction de $(\mathbf{w}, b)$.
6. Le taux d'erreur d'un modèle logistique, comme fonction de $\mathbf{w}$.

<a id="rappels"></a>

## 🔁 Rappels

### M13a.R1 — Bayes et le lissage de Laplace (M04) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

1. Un détecteur signale un défaut. $P(\text{défaut}) = 0{,}02$, $P(\text{signal} \mid \text{défaut}) = 0{,}8$, $P(\text{signal} \mid \text{pas de défaut}) = 0{,}1$. Que vaut $P(\text{défaut} \mid \text{signal})$ ?
2. Une machine a réussi ses 9 premiers essais. L'estimation de Laplace de sa probabilité d'échec ?
3. Trois catégories, de comptages $(4, 0, 2)$ : les estimations avec le lissage de Laplace ($\alpha = 1$) ?
4. Pourquoi calcule-t-on en log-probabilités quand on multiplie beaucoup de probabilités ?
5. Que vaut $\mathrm{LSE}(\ln 2, \ln 6) = \ln(e^{\ln 2} + e^{\ln 6})$ ?

### M13a.R2 — Entropie, cross-entropy et information mutuelle (M06) 🔁 ★ ⏱️ 5 min
*Fiche §2 et §6 · parcours C, E*

1. L'entropie, en bits, de la loi $(0{,}25 ;\ 0{,}25 ;\ 0{,}25 ;\ 0{,}125 ;\ 0{,}125)$ ?
2. $\mathbf{p} = (0{,}85 ;\ 0{,}15)$ et $\mathbf{q} = (0{,}6 ;\ 0{,}4)$ : la cross-entropy $H(\mathbf{p}, \mathbf{q})$ et la divergence $\mathrm{KL}(\mathbf{p} \,\Vert\, \mathbf{q})$, en bits ?
3. Énonce l'inégalité de Gibbs.
4. $I(X ; Y) = 0$ : que peux-tu dire de $X$ et $Y$ ?
5. Comment passer d'une entropie en nats à la même en bits ?

### M13a.R3 — Fonctions convexes de plusieurs variables (M10) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Écris la définition d'une fonction convexe $f : \mathbb{R}^n \to \mathbb{R}$.
2. Une fonction affine est-elle convexe ? Strictement convexe ?
3. Pourquoi une somme de fonctions convexes est-elle convexe ?
4. Pourquoi la norme euclidienne est-elle convexe ?
5. Pour une fonction convexe, l'ensemble $\{\mathbf{x} : f(\mathbf{x}) \le c\}$ a quelle propriété ?

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M13a.1 — Le maximum de vraisemblance d'une loi de Bernoulli et d'une loi catégorielle ✏️ ★ ⏱️ 15 min
**Objectif :** écrire une log-vraisemblance de Bernoulli et une log-vraisemblance catégorielle, trouver leurs maxima, et voir ce que change le lissage.
**Prérequis :** fiche §1 ; M04 §3 et §5 · **Parcours :** C, E

On contrôle 20 pièces : 7 sont défectueuses (label 1), 13 sont bonnes (label 0). Par ailleurs, 20 clients choisissent l'un de quatre forfaits, avec les comptages $(5, 9, 0, 6)$.

| | Question | Réponse attendue |
|---|---|---|
| a | l'estimation $\hat{p}$ du maximum de vraisemblance de la probabilité qu'une pièce soit défectueuse | une fraction |
| b | la log-vraisemblance $\ell(\hat{p})$ | un nombre (4 décimales) |
| c | la log-vraisemblance $\ell(0{,}5)$ | un nombre (4 décimales) |
| d | la log-vraisemblance moyenne par pièce, $\ell(\hat{p})/20$ | un nombre (4 décimales) |
| e | les estimations $\hat{p}_k$ du maximum de vraisemblance des quatre forfaits | une liste de 4 fractions |
| f | les estimations lissées avec $\alpha = 1$ | une liste de 4 nombres (4 décimales) |
| g | les estimations lissées avec $\alpha = \frac{1}{4}$ | une liste de 4 nombres (4 décimales) |
| h | la log-vraisemblance catégorielle $\sum_k n_k\ln\hat{p}_k$ (avec $0 \ln 0 = 0$) | un nombre (4 décimales) |

Dans ta copie : dérive $\ell(p)$ pour retrouver a). Qu'arrive-t-il à la log-vraisemblance catégorielle si un 21ᵉ client choisit le troisième forfait ? Pourquoi le lissage change-t-il aussi les estimations des forfaits déjà choisis ?

### Ex M13a.2 — Le maximum de vraisemblance d'une loi normale : μ̂ et σ̂² ✏️ ★★ ⏱️ 20 min
**Objectif :** dériver la log-vraisemblance d'une loi normale en $\mu$ et en $\sigma^2$, et comparer le maximum de vraisemblance à l'estimation sans biais.
**Prérequis :** fiche §1 ; M02b ; M02c · **Parcours :** C, E

Six temps de réaction, en millisecondes : $245, 262, 251, 270, 248, 260$. Modèle : une loi $\mathcal{N}(\mu, \sigma^2)$, observations i.i.d.

| | Question | Réponse attendue |
|---|---|---|
| a | $\hat{\mu}$ | un nombre |
| b | la somme des carrés des écarts $S = \sum_i (x_i - \hat{\mu})^2$ | un nombre |
| c | $\hat{\sigma}^2$ (maximum de vraisemblance) | un nombre (4 décimales) |
| d | l'estimation sans biais de la variance | un nombre (4 décimales) |
| e | $\hat{\sigma}$ | un nombre (4 décimales) |
| f | la log-vraisemblance au maximum, $\ell(\hat{\mu}, \hat{\sigma}^2)$ | un nombre (4 décimales) |
| g | la log-vraisemblance en $(\hat{\mu}, d)$ | un nombre (4 décimales) |
| h | le rapport $\mathbb{E}[\hat{\sigma}^2]/\sigma^2$ pour $n = 6$ | une fraction |

Dans ta copie : écris $\ell(\mu, v)$ avec $v = \sigma^2$, calcule $\frac{\partial \ell}{\partial \mu}$ et $\frac{\partial \ell}{\partial v}$, et retrouve a) et c). Montre que $\ell(\hat{\mu}, \hat{\sigma}^2) = -\frac{n}{2}\big(\ln(2\pi\hat{\sigma}^2) + 1\big)$. Pourquoi g) est-il plus petit que f) ?

### Ex M13a.3 — La log-loss de quatre prédictions, puis la même en cross-entropy ✏️ ★ ⏱️ 15 min
**Objectif :** calculer une log-loss terme à terme, la relier à la log-vraisemblance des labels et à la cross-entropy, et la comparer à l'accuracy.
**Prérequis :** fiche §2 ; M06 §5 · **Parcours :** C, E

Quatre exemples, de labels $(1, 1, 0, 0)$, reçoivent les probabilités $\hat{p} = (0{,}8 ;\ 0{,}45 ;\ 0{,}35 ;\ 0{,}05)$ d'avoir le label 1.

| | Question | Réponse attendue |
|---|---|---|
| a | les quatre termes de la log-loss | une liste de 4 nombres (4 décimales) |
| b | la log-loss, en nats | un nombre (4 décimales) |
| c | la même, en bits | un nombre (3 décimales) |
| d | la log-vraisemblance des quatre labels | un nombre (4 décimales) |
| e | l'accuracy au seuil 0,5 | une fraction |
| f | la log-loss d'un modèle qui répond toujours 0,5 | un nombre (4 décimales) |
| g | un exemple à trois classes, de classe observée 3, reçoit la loi prédite $(0{,}2 ;\ 0{,}5 ;\ 0{,}3)$ : son terme de cross-entropy | un nombre (4 décimales) |
| h | la log-loss des quatre exemples si la deuxième probabilité passe de 0,45 à 0,9 | un nombre (4 décimales) |

Dans ta copie : écris chaque terme de a) comme une cross-entropy entre deux lois sur $\{0, 1\}$. Compare b) et h), puis l'accuracy dans les deux cas : que mesure la log-loss que l'accuracy ne mesure pas ?

### Ex M13a.4 — Ce que coûte une prédiction sûre et fausse : la log-loss quand p tend vers 0 ✏️ ★ ⏱️ 15 min
**Objectif :** mesurer le poids d'un seul exemple dont le label observé a reçu une probabilité presque nulle, et comprendre pourquoi les bibliothèques écrêtent.
**Prérequis :** fiche §2 · **Parcours :** C

Un modèle est évalué sur 1 000 exemples. Il a donné la probabilité 0,98 au label observé de 999 d'entre eux, et la probabilité $q$ au label observé du dernier.

| | Question | Réponse attendue |
|---|---|---|
| a | la log-loss si $q = 0{,}98$ aussi | un nombre (4 décimales) |
| b | la log-loss si $q = 10^{-4}$ | un nombre (4 décimales) |
| c | la log-loss si $q = 10^{-12}$ | un nombre (4 décimales) |
| d | la valeur de $-\ln q$ pour laquelle le dernier exemple pèse autant, à lui seul, que les 999 autres réunis | un nombre (2 décimales) |
| e | la log-loss si $q = 0$, une bibliothèque écrêtant les probabilités à $10^{-15}$ | un nombre (4 décimales) |
| f | le terme du dernier exemple, en bits, pour $q = 10^{-4}$ | un nombre (4 décimales) |
| g | vrai ou faux : la log-loss reste bornée quand $q$ tend vers 0 | `True` ou `False` |

Dans ta copie : que vaut le taux d'erreur dans les cas a) à c) ? Pourquoi une probabilité 0 exactement est-elle un problème, et que fait l'écrêtage ? Un modèle doit-il donc éviter d'annoncer 0 ou 1 ?

### Ex M13a.5 — La sigmoïde : valeurs, logit, cote et symétrie σ(−z) = 1 − σ(z) ✏️ ★ ⏱️ 15 min
**Objectif :** passer d'un score à une probabilité, d'une probabilité à sa cote et à son logit, et s'en servir.
**Prérequis :** fiche §3 ; R6 §7 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\sigma(0{,}8)$ | un nombre (4 décimales) |
| b | $\sigma(-2{,}5)$ | un nombre (4 décimales) |
| c | $\sigma(2{,}5) + \sigma(-2{,}5)$ | un nombre |
| d | le logit de 0,15 | un nombre (4 décimales) |
| e | la cote de 0,15 | une fraction |
| f | le score $z$ tel que $\sigma(z) = 0{,}95$ | un nombre (4 décimales) |
| g | la probabilité dont la cote vaut 2,5 | une fraction |
| h | $\sigma(z + \ln 2)$, sachant que $\sigma(z) = 0{,}15$ | une fraction |

Dans ta copie : montre que $\frac{\sigma(z)}{1 - \sigma(z)} = e^z$, puis que $\sigma(-z) = 1 - \sigma(z)$. Explique h) avec la cote, sans calculer $z$.

### Ex M13a.6 — La softplus : valeurs, asymptotes et comportement pour |z| grand ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des valeurs de la softplus, vérifier ses propriétés et voir l'écart à ses asymptotes.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $s(2{,}5)$ | un nombre (4 décimales) |
| b | $s(-2{,}5)$ | un nombre (4 décimales) |
| c | $s(2{,}5) - s(-2{,}5)$ | un nombre |
| d | $s(6) - 6$ | un nombre (6 décimales) |
| e | $s(-3{,}4)$, avec l'écriture $\max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$ | un nombre (4 décimales) |
| f | $-\ln(1 - \sigma(0{,}7))$ | un nombre (4 décimales) |
| g | vrai ou faux : $s(z) \ge \max(z, 0)$ pour tout $z$ | `True` ou `False` |
| h | la plus grande valeur de l'écart $s(z) - \max(z, 0)$ | un nombre (4 décimales) |

Dans ta copie : montre que $s(z) - s(-z) = z$ et que $s(z) - z = \ln(1 + e^{-z})$ ; déduis-en les deux asymptotes. Où l'écart h) est-il atteint ? Pourquoi écrit-on la softplus avec $e^{-\lvert z \rvert}$ dans un programme ?

### Ex M13a.7 — Un modèle logistique à deux features : probabilités, cote et frontière de décision ✏️ ★ ⏱️ 15 min
**Objectif :** lire un modèle logistique : probabilités, cote, effet d'une feature, frontière et lignes de niveau.
**Prérequis :** fiche §4 ; M07 · **Parcours :** C, E

Un modèle logistique a pour poids $\mathbf{w} = (0{,}7 ;\ 1{,}1)$ et pour biais $b = -3{,}2$. On note $A = (1, 1)$ et $B = (2, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le score de $A$ | un nombre (4 décimales) |
| b | $P(Y = 1 \mid A)$ | un nombre (4 décimales) |
| c | la cote de la classe 1 en $B$ | un nombre (4 décimales) |
| d | le facteur qui multiplie la cote quand $x_2$ augmente de 1 | un nombre (4 décimales) |
| e | le point de la frontière de décision d'abscisse $x_1 = 2$ : son ordonnée $x_2$ | un nombre (4 décimales) |
| f | l'ordonnée $x_2$ du point d'abscisse $x_1 = 2$ où la probabilité vaut 0,85 | un nombre (4 décimales) |
| g | la distance de $B$ à la frontière | un nombre (4 décimales) |
| h | $P(Y = 1 \mid (0, 0))$ | un nombre (4 décimales) |

Dans ta copie : pourquoi les points de probabilité 0,85 forment-ils une droite parallèle à la frontière ? Dans quelle direction faut-il aller pour que la probabilité augmente le plus vite ?

### Ex M13a.8 — L'hypothèse naïve à la main : une loi jointe factorisée, comparée à la vraie ✏️ ★★ ⏱️ 20 min
**Objectif :** remplacer une loi jointe par le produit de ses marginales dans chaque classe, et mesurer ce que l'hypothèse naïve change aux a posteriori et aux décisions.
**Prérequis :** fiche §5 ; M04 §1 · **Parcours :** C, E

Deux features binaires $x_1$ et $x_2$, deux classes, $P(Y = 1) = 0{,}4$. Les vraies lois jointes de $(x_1, x_2)$ dans chaque classe :

| $(x_1, x_2)$ | $(0, 0)$ | $(0, 1)$ | $(1, 0)$ | $(1, 1)$ |
|---|---|---|---|---|
| $P(\cdot \mid Y = 1)$ | 0,05 | 0,25 | 0,25 | 0,45 |
| $P(\cdot \mid Y = 0)$ | 0,52 | 0,10 | 0,10 | 0,28 |

Naïve Bayes remplace chaque loi jointe par le produit de ses deux marginales.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(x_1 = 1 \mid Y = 1)$ | une fraction |
| b | la probabilité factorisée de $(0, 1)$ dans la classe 1 | une fraction |
| c | la vraie probabilité $P(Y = 1 \mid (0, 1))$ | une fraction |
| d | la même, calculée par Naïve Bayes | un nombre (4 décimales) |
| e | la vraie probabilité $P(Y = 1 \mid (1, 1))$ | un nombre (4 décimales) |
| f | la même, calculée par Naïve Bayes | un nombre (4 décimales) |
| g | le nombre des quatre cases où la classe la plus probable n'est pas la même selon la vraie loi et selon Naïve Bayes | un entier |
| h | pour 10 features binaires et 2 classes : le nombre de probabilités à estimer avec les lois jointes complètes, puis avec Naïve Bayes (dans les deux cas, la proportion des classes comprise) | une liste de 2 entiers |

Dans ta copie : dans la classe 1, les deux features sont-elles indépendantes ? Explique avec les cases $(0, 1)$ et $(1, 1)$ pourquoi Naïve Bayes s'y trompe. Pourquoi peut-il tout de même bien classer quand l'hypothèse est presque vraie ?

### Ex M13a.9 — Deux classes gaussiennes de même variance : l'a posteriori est une sigmoïde d'un score affine ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer l'a posteriori d'un modèle génératif gaussien à une feature, l'écrire comme une régression logistique, et voir le rôle des proportions des classes.
**Prérequis :** fiche §4 et §5 ; M02b · **Parcours :** C

Une feature $x$. Classe 0 : $x \sim \mathcal{N}(-1, 4)$ ; classe 1 : $x \sim \mathcal{N}(3, 4)$ (même variance, $\sigma^2 = 4$) ; $P(Y = 1) = 0{,}35$.

| | Question | Réponse attendue |
|---|---|---|
| a | le poids $w$ de l'écriture $P(Y = 1 \mid x) = \sigma(wx + b)$ | un nombre |
| b | le biais $b$ | un nombre (4 décimales) |
| c | la frontière $x^*$ où $P(Y = 1 \mid x) = 0{,}5$ | un nombre (4 décimales) |
| d | $P(Y = 1 \mid x = 1)$ | un nombre (4 décimales) |
| e | $P(Y = 1 \mid x = 3)$ | un nombre (3 décimales) |
| f | la frontière si les classes étaient équiprobables | un nombre |
| g | le facteur qui multiplie la cote a posteriori quand $x$ augmente de 1 | un nombre (4 décimales) |
| h | si la variance de la classe 1 passait à 9 (celle de la classe 0 restant 4) : le coefficient de $x^2$ dans la log-cote a posteriori | un nombre (4 décimales) |

Dans ta copie : écris la log-cote a posteriori, et montre que les termes en $x^2$ s'annulent. Pourquoi d) vaut-il exactement la proportion de la classe 1 ? Que devient la frontière dans le cas h) ?

### Ex M13a.10 — L'entropie et l'indice de Gini de quelques distributions ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des entropies (en bits) et des indices de Gini, et comparer leurs maxima.
**Prérequis :** fiche §6 ; M06 §2 · **Parcours :** C, E

Trois lois : $\mathbf{p}_1 = (0{,}95 ;\ 0{,}05)$, $\mathbf{p}_2 = (0{,}4 ;\ 0{,}4 ;\ 0{,}2)$ et $\mathbf{p}_3 = (\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8})$.

| | Question | Réponse attendue |
|---|---|---|
| a | $G(\mathbf{p}_1)$ | un nombre (4 décimales) |
| b | $H(\mathbf{p}_1)$ | un nombre (4 décimales) |
| c | $G(\mathbf{p}_2)$ | un nombre (4 décimales) |
| d | $H(\mathbf{p}_2)$ | un nombre (4 décimales) |
| e | $H(\mathbf{p}_3)$ | une fraction |
| f | $G(\mathbf{p}_3)$ | une fraction |
| g | l'entropie maximale d'une loi à 6 issues | un nombre (4 décimales) |
| h | l'indice de Gini maximal d'une loi à 6 issues | une fraction |

Dans ta copie : range $\mathbf{p}_1$, $\mathbf{p}_2$ et $\mathbf{p}_3$ par entropie, puis par Gini : le rangement est-il le même ? Pourquoi comparer l'impureté de $\mathbf{p}_1$ (2 classes) à celle de $\mathbf{p}_3$ (4 classes) demande-t-il de la prudence ?

### Ex M13a.11 — L'information mutuelle d'un tableau de contingence, et la baisse d'entropie qu'elle mesure ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une information mutuelle comme une baisse d'entropie moyenne, et la comparer à la baisse de Gini.
**Prérequis :** fiche §6 ; M06 §3 et §4 · **Parcours :** C, E

Cent trajets domicile-travail, selon le mode de transport $X$ et l'arrivée à l'heure $Y$ :

| | à l'heure | en retard | total |
|---|---|---|---|
| bus | 22 | 18 | 40 |
| vélo | 26 | 4 | 30 |
| voiture | 17 | 13 | 30 |
| total | 65 | 35 | 100 |

| | Question | Réponse attendue |
|---|---|---|
| a | $P(Y = \text{à l'heure})$ | une fraction |
| b | $H(Y)$, en bits | un nombre (4 décimales) |
| c | $H(Y \mid X = \text{vélo})$ | un nombre (4 décimales) |
| d | $H(Y \mid X)$ | un nombre (4 décimales) |
| e | l'information mutuelle $I(X ; Y)$ | un nombre (4 décimales) |
| f | $H(X)$ | un nombre (4 décimales) |
| g | la baisse de l'indice de Gini de $Y$ quand on connaît $X$ (Gini de $Y$ moins la moyenne pondérée des Gini des lignes) | un nombre (4 décimales) |
| h | l'information mutuelle si chaque ligne avait les proportions 65 % et 35 % | un nombre |

Dans ta copie : retrouve e) avec la formule $\sum_{x, y} p(x, y)\log_2\frac{p(x, y)}{p(x)\,p(y)}$. Quelle ligne contribue le plus à la baisse d'entropie ? Que signifierait $I(X ; Y) = H(Y)$ ?

### Ex M13a.12 — La variance d'un groupe coupé en deux : variance intra plus variance inter ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer et démontrer la décomposition de la variance d'un groupe coupé en deux.
**Prérequis :** fiche §7 ; M02c · **Parcours :** C

Sept cibles : le groupe $A = (6, 10, 8)$ et le groupe $B = (15, 19, 17, 21)$. Les variances se calculent avec $\frac{1}{n}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne des sept cibles | un nombre (4 décimales) |
| b | leur variance | un nombre (4 décimales) |
| c | les moyennes $m_A$ et $m_B$ | une liste de 2 nombres |
| d | les variances $V_A$ et $V_B$ | une liste de 2 nombres (4 décimales) |
| e | la variance intra-groupes | un nombre (4 décimales) |
| f | la variance inter-groupes | un nombre (4 décimales) |
| g | vrai ou faux : e) + f) = b) | `True` ou `False` |
| h | la variance des sept cibles calculée avec $\frac{1}{n - 1}$ | un nombre (4 décimales) |

Dans ta copie : démontre la décomposition dans le cas général (écris $y - m = (y - m_A) + (m_A - m)$ dans le groupe $A$). Pourquoi le terme croisé est-il nul ? Pourquoi h) ne se décompose-t-il pas aussi simplement ?

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M13a.13 — Le maximum de vraisemblance d'une loi catégorielle, par l'inégalité de Gibbs ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que les fréquences observées maximisent la vraisemblance d'une loi catégorielle, sans dériver.
**Prérequis :** fiche §1 ; M06 §5 et §6 · **Parcours :** C, E

$N$ observations d'une variable à $K$ valeurs, de comptages $n_1, \ldots, n_K$, et $\hat{p}_k = \frac{n_k}{N}$. Pour une loi $\mathbf{p}$ à valeurs strictement positives, $\ell(\mathbf{p}) = \sum_k n_k\ln p_k$.
1. Montre que $\frac{1}{N}\ell(\mathbf{p}) = -H(\hat{\mathbf{p}}, \mathbf{p})$, avec la cross-entropy en nats.
2. Rappelle l'inégalité de Gibbs, et déduis-en $\ell(\mathbf{p}) \le \ell(\hat{\mathbf{p}})$, avec égalité si et seulement si $\mathbf{p} = \hat{\mathbf{p}}$.
3. Que devient le raisonnement quand un comptage $n_k$ est nul ? (Pense à la convention $0 \ln 0 = 0$.)
4. Écris $\ell(\mathbf{p}) - \ell(\hat{\mathbf{p}})$ avec une divergence KL.
5. Montre que l'estimation lissée $\frac{n_k + \alpha}{N + K\alpha}$ maximise $\sum_k (n_k + \alpha)\ln p_k$ : que signifie ce résultat ?

### Ex M13a.14 — La log-loss moyenne est moins la log-vraisemblance divisée par n ∂ ★ ⏱️ 15 min
**Objectif :** démontrer l'équivalence entre minimiser la log-loss et maximiser la vraisemblance des labels, et la relire en cross-entropy.
**Prérequis :** fiche §2 ; M06 §5 · **Parcours :** C, E

Un classifieur donne à chaque exemple $i$ la probabilité $\hat{p}_i$ du label 1 ; les labels $y_i \in \{0, 1\}$ sont supposés indépendants sachant les features.
1. Écris la probabilité du label $y_i$ selon le modèle, en une seule formule valable pour $y_i = 0$ et $y_i = 1$.
2. Déduis-en la vraisemblance $L$ des $n$ labels, puis montre que la log-loss vaut $-\frac{1}{n}\ln L$.
3. Montre que le terme d'un exemple est la cross-entropy $H(\mathbf{e}_{y_i}, \hat{\mathbf{q}}_i)$, où $\mathbf{e}_{y_i}$ met toute la masse sur le label observé et $\hat{\mathbf{q}}_i = (1 - \hat{p}_i, \hat{p}_i)$.
4. Généralise à $K$ classes : quelle est la log-loss, et quelle loi des labels suppose-t-elle ?
5. Pourquoi minimiser la log-loss, la somme $-\ln L$ ou la log-loss en bits donne-t-il les mêmes paramètres ?

### Ex M13a.15 — Log-somme-exp est convexe : sur une droite, sa dérivée seconde est une variance ; la softplus aussi ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer la convexité de log-somme-exp par sa restriction à une droite, et en déduire celle de la softplus et de la log-loss logistique.
**Prérequis :** fiche §3 et §4 ; M05a ; M10 ; M02b · **Parcours :** C, E

$\mathrm{LSE}(\mathbf{u}) = \ln\sum_{k=1}^K e^{u_k}$. On fixe $\mathbf{a}, \mathbf{d} \in \mathbb{R}^K$ et l'on pose $g(t) = \mathrm{LSE}(\mathbf{a} + t\,\mathbf{d})$ et $\pi_k(t) = \frac{e^{a_k + t d_k}}{\sum_j e^{a_j + t d_j}}$.
1. Montre que les $\pi_k(t)$ forment une loi de probabilité sur $\{1, \ldots, K\}$.
2. Montre que $g'(t) = \sum_k \pi_k(t)\,d_k$ : la moyenne des $d_k$ sous cette loi.
3. Calcule $\pi_k'(t)$, puis montre que $g''(t) = \sum_k \pi_k d_k^2 - \big(\sum_k \pi_k d_k\big)^2$. Reconnais une variance, et conclus que $g'' \ge 0$.
4. Explique pourquoi la convexité de $g$ pour tous $\mathbf{a}$ et $\mathbf{d}$ entraîne celle de $\mathrm{LSE}$ (définition de M10).
5. Déduis-en que la softplus est convexe, puis que $(\mathbf{w}, b) \mapsto s(\mathbf{w} \cdot \mathbf{x} + b) - y(\mathbf{w} \cdot \mathbf{x} + b)$ l'est, pour $\mathbf{x}$ et $y$ fixés.
6. Quand $g''(t)$ est-il nul ? Montre que $\mathrm{LSE}$ n'est pas **strictement** convexe (cherche une direction $\mathbf{d}$ où $g$ est affine).

### Ex M13a.16 — L'indice de Gini est maximal pour la loi uniforme ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer le maximum de l'indice de Gini et le cas d'égalité, de deux façons.
**Prérequis :** fiche §6 ; M07 · **Parcours :** C

$\mathbf{p} = (p_1, \ldots, p_K)$ est une loi de probabilité, et $G(\mathbf{p}) = 1 - \sum_k p_k^2$.
1. Développe $\sum_k \big(p_k - \frac{1}{K}\big)^2$, et déduis-en $\sum_k p_k^2 \ge \frac{1}{K}$.
2. Conclus : $G(\mathbf{p}) \le 1 - \frac{1}{K}$, avec égalité si et seulement si $\mathbf{p}$ est uniforme.
3. Retrouve $\sum_k p_k^2 \ge \frac{1}{K}$ par l'inégalité de Cauchy-Schwarz (M07) appliquée à $\mathbf{p}$ et au vecteur $(1, \ldots, 1)$.
4. Montre que $G(\mathbf{p}) \ge 0$, avec égalité si et seulement si une classe a la probabilité 1.
5. Montre que $G$ est concave, et déduis-en qu'un mélange de deux lois a un indice de Gini au moins égal à la moyenne pondérée des leurs.

### Ex M13a.17 — L'entropie est maximale pour la loi uniforme, par l'inégalité de Gibbs ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer le maximum de l'entropie et le cas d'égalité, en une ligne d'inégalité de Gibbs.
**Prérequis :** fiche §6 ; M06 §6 · **Parcours :** C

$\mathbf{p}$ est une loi sur $K$ valeurs, $\mathbf{u}$ la loi uniforme, et les logarithmes sont en base 2.
1. Montre que $\mathrm{KL}(\mathbf{p} \,\Vert\, \mathbf{u}) = \log_2 K - H(\mathbf{p})$.
2. Conclus : $H(\mathbf{p}) \le \log_2 K$, avec égalité si et seulement si $\mathbf{p} = \mathbf{u}$.
3. Montre que $H(\mathbf{p}) \ge 0$, avec égalité si et seulement si une valeur a la probabilité 1.
4. Une loi sur $K = 8$ valeurs a une entropie de 3 bits : que peux-tu en dire ?
5. Pourquoi ce résultat dit-il que l'entropie mesure un nombre moyen de questions oui/non (M06 §7) ?

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13a.18 — Pont : une sonde linéaire, un modèle logistique en NumPy sur un batch de représentations figées, jusqu'à la log-loss 🔗 ★ ⏱️ 15 min
**Objectif :** évaluer à la main une sonde linéaire sur un petit batch de représentations, en écriture matricielle, jusqu'à la log-loss et l'accuracy.
**Prérequis :** fiche §2 à §4 ; M09a · **Parcours :** C, E

Un réseau déjà entraîné, laissé tel quel, a produit les représentations de dimension 3 de quatre exemples, rangées en lignes d'une matrice, avec leurs labels :

$$\mathbf{H} = \begin{pmatrix} 2 & 0 & 0{,}5 \\ 0 & 1 & 0 \\ 1 & 1 & 0{,}5 \\ 0 & 2 & 1 \end{pmatrix}, \qquad \mathbf{y} = (1, 0, 0, 0).$$

Une sonde linéaire de poids $\mathbf{w} = (0{,}4 ;\ -0{,}9 ;\ 1{,}6)$ et de biais $b = -0{,}2$ calcule les scores $\mathbf{z} = \mathbf{H}\mathbf{w} + b$, puis les probabilités $\sigma(\mathbf{z})$.

| | Question | Réponse attendue |
|---|---|---|
| a | les quatre scores | une liste de 4 nombres (4 décimales) |
| b | les quatre probabilités | une liste de 4 nombres (4 décimales) |
| c | la log-loss de la sonde, avec $s(z) - yz$ | un nombre (4 décimales) |
| d | l'accuracy au seuil 0,5 | une fraction |
| e | la log-loss du meilleur modèle constant, qui répond toujours la proportion de labels 1 | un nombre (4 décimales) |
| f | ce que la sonde gagne sur ce modèle constant : e) − c) | un nombre (4 décimales) |
| g | le label prédit pour une représentation nouvelle $(1, 1, 0)$ | un entier |
| h | le nombre de paramètres d'une sonde sur des représentations de dimension 768 | un entier |

Dans ta copie : écris le calcul de a) en une ligne de NumPy. Pourquoi comparer à e) plutôt qu'à $\ln 2$ ? Si la sonde atteignait une log-loss bien plus basse sur des données de test, que conclurais-tu sur la représentation ?

### Ex M13a.19 — MML §8.3, relu après M04 : estimer des paramètres, et ce que la régression logistique y ajoute 📖 ★★ ⏱️ 30 min
**Objectif :** relire en anglais la section du livre sur l'estimation de paramètres, relier ses notations à la fiche, et y situer la régression logistique.
**Prérequis :** fiche §1, §2 et §4 · **Parcours :** C

Relis MML §8.3. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Quelle quantité le livre note-t-il $L(\boldsymbol{\theta})$ ou $\mathcal{L}(\boldsymbol{\theta})$ ? Pourquoi la minimise-t-il au lieu de maximiser ? Relie-la à la $\ell$ de la fiche.
2. Où l'hypothèse i.i.d. intervient-elle dans le §8.3.1, et que transforme-t-elle ?
3. Dans l'exemple du livre où le bruit est gaussien, quelle loss obtient-on ? Refais le calcul avec la loi normale de la fiche §1.
4. Que dit le §8.3.2 du MAP, et comment le relies-tu au lissage de la fiche §1 ?
5. Le §8.3.4 évoque des prédicteurs $\varphi(\boldsymbol{\theta}^\top\mathbf{x})$ : quelle fonction $\varphi$ et quelle loi des labels donnent la régression logistique ? Et la régression linéaire ?
6. Le livre ne donne pas de formule pour les paramètres de la régression logistique : pourquoi n'en existe-t-il pas, et comment les obtient-on ?
7. Trois mots anglais de la section, avec leur traduction.

### Ex M13a.20 — Fermi : la loi jointe complète contre l'hypothèse naïve, combien de nombres pour 30 features à 4 valeurs ? 🧮 ★ ⏱️ 10 min
**Objectif :** estimer le nombre de paramètres d'une loi jointe complète et celui de Naïve Bayes, et le nombre d'exemples qu'il faudrait pour les estimer.
**Prérequis :** fiche §5 · **Parcours :** C

Un modèle génératif classe des clients en 3 segments, à partir de 30 features catégorielles à 4 valeurs chacune.
1. Combien de probabilités faut-il pour décrire la loi jointe complète des 30 features dans un segment ? Donne un ordre de grandeur en puissance de 10.
2. Combien d'octets pour stocker ces nombres en `float64`, pour les trois segments ? Compare à la mémoire d'un ordinateur.
3. Combien de probabilités avec l'hypothèse naïve, pour les trois segments, proportions des segments comprises ?
4. Pour estimer une probabilité avec une précision raisonnable, il faut quelques dizaines d'exemples par case. Combien d'exemples faudrait-il pour la loi jointe complète ? Pour Naïve Bayes ?
5. Conclus : quel est le vrai problème de la loi jointe complète, la mémoire ou les données ?

### Ex M13a.21 — Expliquer pourquoi on minimise la log-loss plutôt que le taux d'erreur 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, à quelqu'un qui connaît l'accuracy mais pas la vraisemblance, pourquoi un modèle s'entraîne sur la log-loss.
**Prérequis :** fiche §2 à §4 · **Parcours :** C, E

Une collègue analyste te demande : « Puisqu'on juge le modèle sur son taux d'erreur, pourquoi l'entraîner sur une autre quantité ? » Réponds-lui en 6 à 10 phrases, sans formule, en t'appuyant sur trois idées : ce que le taux d'erreur ne voit pas (la confiance), ce qui rend une loss facile ou difficile à minimiser (une marche plate contre une courbe lisse et convexe), et le lien avec la vraisemblance. Donne un exemple chiffré simple. Puis réécris ta réponse en 3 phrases pour un message rapide.

<a id="entretien"></a>

## 💼 Entretien

### M13a.E1 — « Pourquoi la cross-entropy est-elle une log-vraisemblance ? » 💼 ★ ⏱️ 10 min
*Fiche §2 · parcours C*

« Pourquoi la cross-entropy est-elle une log-vraisemblance ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire quel modèle des labels un classifieur probabiliste définit, écrire en mots la vraisemblance des labels et son logarithme, montrer que la moyenne de moins ce logarithme est la cross-entropy entre le label observé et la loi prédite, et dire ce que l'on gagne à voir les choses ainsi (le choix d'une loss comme choix d'un modèle de bruit, la récompense des probabilités honnêtes). Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M13a.E2 — « Qu'est-ce que le maximum de vraisemblance, et quel lien avec les losses que vous minimisez ? » 💼 ★ ⏱️ 10 min
*Fiche §1 et §2 · parcours C*

« Qu'est-ce que le maximum de vraisemblance, et quel lien avec les losses que vous minimisez ? »

Prépare une réponse orale de **60 secondes**. Elle doit définir la vraisemblance comme une fonction des paramètres à données fixées, expliquer le passage au logarithme et l'hypothèse i.i.d., donner deux exemples (la proportion pour une loi de Bernoulli, la moyenne et la variance en $\frac{1}{n}$ pour une loi normale), puis relier deux losses à deux modèles de bruit (les moindres carrés et un bruit gaussien, la log-loss et des labels de Bernoulli), et dire une limite (le biais de la variance, l'overfitting quand les paramètres sont nombreux). Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m13a_vraisemblance_logistique/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M13a.22 | La log-vraisemblance et le maximum de vraisemblance d'une loi de Bernoulli · `bernoulli_log_likelihood, bernoulli_mle` | 🔨 | ★ | 15 | C, E |
| M13a.23 | Maximum de vraisemblance catégoriel, avec lissage, et gaussien · `categorical_mle, gaussian_mle` | 🔨 | ★ | 20 | C, E |
| M13a.24 | La log-loss à partir des scores, sans débordement · `logistic_loss` | 🔨 | ★★ | 20 | C, E |
| M13a.25 | `scipy.stats`, `scipy.special` et `sklearn.metrics.log_loss` contre tes fonctions | 📦 | ★ | 15 | C, E |
| M13a.26 | Prédire la log-loss d'un modèle qui répond toujours 0,5, puis toujours la fréquence des 1 | 🔮 | ★ | 10 | C, E |
| M13a.27 | La variabilité du maximum de vraisemblance d'une loi de Bernoulli d'un échantillon à l'autre | 🔬 | ★★ | 20 | C |
| M13a.28 | L'entropie et l'indice de Gini sur les lois à trois issues : lignes de niveau et maximum au centre | 🎨 | ★ | 20 | C, E |
| M13a.29 | Chasse à l'erreur : un ln 0, une sigmoïde qui déborde, une variance de maximum de vraisemblance divisée par n − 1 | 🐛 | ★ | 15 | C |
| M13a.30 | Vérifier avec SymPy le maximum de vraisemblance d'une loi géométrique et d'une loi de Poisson | 🛠️ | ★ | 15 | C |
| M13a.31 | Défi : la proportion d'un mélange de deux lois connues par maximum de vraisemblance, à 1e−6 près du maximum (dichotomie ou Newton) | 🏆 | ★★★ | 25 | C |
