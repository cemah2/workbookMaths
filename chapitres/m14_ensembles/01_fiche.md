# M14 · Les maths des ensembles — fiche de cours

> Un **ensemble de modèles** combine plusieurs prédicteurs : il les fait voter, il moyenne leurs prédictions, il pondère leurs avis, ou il les ajoute l'un après l'autre en corrigeant les erreurs des précédents. Le chapitre 14 de workbookIA construit ces méthodes ; celui-ci rassemble les cinq outils mathématiques qu'elles utilisent. La **queue d'une loi binomiale** dit avec quelle probabilité beaucoup d'essais indépendants échouent à la fois, et la **borne de Chernoff** dit à quelle vitesse cette probabilité tend vers 0. La **variance d'une moyenne pondérée** $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ dit ce que moyenner gagne, et ce que la corrélation lui reprend. La limite $(1 + x/n)^n \to e^x$ relie les produits répétés aux exponentielles. Les **poids exponentiels** de l'algorithme Hedge suivent le meilleur de plusieurs experts sans savoir lequel c'est. Enfin, le **gradient d'une loss par rapport aux prédictions** dit dans quelle direction corriger un ensemble de prédictions.

| | |
|---|---|
| **Sections** | §1 à §5 |
| **Temps total estimé** | ≈ 7,2 h : lecture et calculs de la fiche ≈ 1 h 30, exercices ≈ 5 h 20, 12 flashcards ≈ 20 min (parcours essentiel ≈ 4,7 h) |
| **Prérequis** | M02b (loi binomiale) ; M02c (covariance, variance d'une somme, matrice de covariance) ; M05a (Taylor, $\ln(1 + u)$) ; M06 (divergence KL) ; M08 (test binomial exact) ; M11 (Markov, Hoeffding, méthode de Chernoff, regret) ; M05b (gradient) ; M09b (loss de Huber) ; M13a (log-loss) ; M13b (Lagrange, pour une remarque du §2) |
| **Fichiers du chapitre** | `02_exercices.md` (quiz, papier) · `03_notebook.ipynb` · `04_indices.md` · `05_solutions.md` et `05_solutions.ipynb` · `06_mes_reponses.md` · `flashcards.csv` |
| **mymath** | `ensembles.py` : `chernoff_bound`, `variance_of_average`, `hedge_weights` |
| **MML** | — (MML ne traite pas ces outils : la fiche est le cours) |

## Comment utiliser ce chapitre

**Ordre conseillé.**
1. `python tools/start_chapter.py M14` (sur Colab : `00_setup/COLAB.md` §2) : il copie le notebook, ta feuille de réponses et le squelette `mymath/ensembles.py`.
2. Section par section : lis **crayon en main**, refais chaque calcul ; puis fais les exercices de la section, quiz 🧠 d'abord.
3. Les exercices ✏️ et 🔗 se font sur papier, dans ta copie de `06_mes_reponses.md`, puis se vérifient dans la **partie 0** du notebook. Les démonstrations ∂ se rédigent dans ta copie et se jugent avec la grille de relecture de `05_solutions.md`.

Les cinq sections sont indépendantes : chacune prépare une méthode de workbookIA 14 sans la faire. Le vote, le bagging, AdaBoost et le gradient boosting restent à workbookIA.

| Section | Quiz 🧠 et rappels 🔁 | Papier et réflexion | Notebook |
|---|---|---|---|
| §1 La queue d'une loi binomiale | Q1, R1 | M14.1 ✏️, M14.8 ∂ | M14.11 🔨, M14.15 🐛, M14.16 🛠️ |
| §2 La variance d'une moyenne de variables corrélées | Q2, R2 | M14.2 ✏️, M14.7 ∂, M14.9 🔗, M14.10 🗣️ | M14.11 🔨, M14.13 🔬, M14.15 🐛 |
| §3 La limite $(1 + x/n)^n \to e^x$ | Q3, R3 | M14.3 ✏️, M14.6 ∂ | |
| §4 Des poids exponentiels : l'algorithme Hedge | Q4 | M14.4, M14.5 ✏️, M14.E1 💼 | M14.12 🔨, M14.14 🎨, M14.15 🐛, M14.17 🏆 |
| §5 Le gradient d'une loss par rapport aux prédictions | R1 | M14.5 ✏️ | |

Parcours essentiel : tout sauf M14.Q4, M14.5, M14.7, M14.8, M14.E1, M14.12 et M14.14 à M14.17. Le §5 se lit en survol.

## Lecture conseillée (facultatif)

MML ne traite pas ces outils : cette fiche est le cours. Pour aller plus loin, en anglais (références et conditions d'accès dans `annexes/ressources.md`) :
- J. K. Blitzstein et J. Hwang, *Introduction to Probability*, après le §2 : le chapitre sur les lois jointes, pour la covariance et la variance d'une somme ;
- T. Lattimore et C. Szepesvári, *Bandit Algorithms*, chapitre 5 (*Concentration of Measure*), après le §1, pour la méthode de Chernoff (déjà conseillé en M11) ;
- S. Arora, E. Hazan et S. Kale, « The Multiplicative Weights Update Method: a Meta-Algorithm and Applications », *Theory of Computing* 8 (2012), après le §4 : les poids multiplicatifs, et leurs nombreux usages.

Ces lectures ne sont nécessaires à aucun exercice.

Vocabulaire anglais de ce chapitre : *ensemble (of models)*, *binomial tail*, *k-out-of-n system*, *reliability*, *Chernoff bound*, *moment generating function*, *Kullback-Leibler divergence*, *Pinsker's inequality*, *majority vote*, *weighted average*, *covariance matrix*, *quadratic form*, *inverse-variance weighting*, *variance floor*, *decorrelation*, *compound interest*, *continuous compounding*, *experts (prediction with expert advice)*, *Hedge*, *exponential weights*, *multiplicative weights*, *learning rate*, *regret*, *anytime*, *full information*, *exponential loss*, *Huber loss*, *functional gradient*, *gradient boosting*.

## Objectifs d'apprentissage

À la fin du chapitre, tu sais :
- **calculer** la queue $P(X \ge k)$ d'une loi binomiale, et la **majorer** par les bornes de Hoeffding et de Chernoff, en sachant laquelle est la meilleure ;
- **calculer** la variance d'une moyenne pondérée de variables corrélées, $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$, et **expliquer** pourquoi moyenner des prédictions corrélées laisse un plancher de variance ;
- **démontrer** et **utiliser** la limite $(1 + x/n)^n \to e^x$, avec la vitesse de convergence ;
- **calculer** les poids exponentiels de l'algorithme Hedge et son regret, et **choisir** son learning rate ;
- **calculer** le gradient d'une loss par rapport au vecteur des prédictions, et **lire** les poids qu'il donne aux exemples.

## L'essentiel en 10 lignes

1. Si $X$ suit la loi $\mathcal{B}(n, p)$, sa **queue** est $P(X \ge k) = \sum_{j \ge k}\binom{n}{j}p^j(1 - p)^{n-j}$ ; attention à $P(X \ge k) = P(X > k - 1)$.
2. **Borne de Chernoff** : pour $a > p$, $P(X \ge na) \le e^{-n\,\mathrm{KL}(a \Vert p)}$, avec $\mathrm{KL}(a \Vert p) = a\ln\frac{a}{p} + (1 - a)\ln\frac{1 - a}{1 - p}$. Elle vient de Markov appliqué à $e^{\lambda X}$, avec le meilleur $\lambda$.
3. Comme $\mathrm{KL}(a \Vert p) \ge 2(a - p)^2$ (Pinsker), Chernoff fait toujours au moins aussi bien que Hoeffding, et beaucoup mieux pour les événements rares.
4. $\mathbb{V}\big(\sum_i w_iX_i\big) = \sum_{i,j}w_iw_j\operatorname{Cov}(X_i, X_j) = \mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ : les covariances comptent autant que les variances.
5. Des prédictions indépendantes de même variance $\sigma^2$ : leur moyenne a la variance $\frac{\sigma^2}{M}$. Avec une **part commune**, la variance de la moyenne ne descend pas sous la variance de cette part : seule la **décorrélation** fait baisser ce plancher.
6. $\left(1 + \frac{x}{n}\right)^n \to e^x$ pour tout réel $x$, car $n\ln\left(1 + \frac{x}{n}\right) \to x$ ; l'erreur relative vaut environ $-\frac{x^2}{2n}$.
7. **Hedge** : $K$ experts, des losses dans $[0, 1]$ ; avant le tour $t$, le poids de l'expert $k$ est proportionnel à $e^{-\eta L_t[k]}$, où $L_t[k]$ est sa loss cumulée. On retranche la plus petite loss cumulée avant l'exponentielle.
8. **Regret** de Hedge : $R_T \le \frac{\ln K}{\eta} + \frac{\eta T}{8}$ ; avec $\eta = \sqrt{8\ln K/T}$, $R_T \le \sqrt{\frac{T\ln K}{2}}$, et le regret moyen tend vers 0.
9. Le gradient d'une loss $\sum_i \ell(y_i, F_i)$ par rapport au **vecteur des prédictions** $\mathbf{F}$ a pour coordonnée $i$ la dérivée $\frac{\partial\ell}{\partial F}(y_i, F_i)$.
10. Loss exponentielle $e^{-yF}$ : gradient $-y_ie^{-y_iF_i}$, des **poids exponentiels** sur les exemples mal classés ; loss de Huber : gradient borné par $\delta$, un point aberrant tire au plus avec la force $\delta$.

## §1 · La queue d'une loi binomiale

### Au moins $k$ sur $n$

$n$ essais indépendants réussissent chacun avec la probabilité $p$ ; le nombre $X$ de succès suit la loi binomiale $\mathcal{B}(n, p)$ (M02b). La **queue** (*tail*) de la loi est la probabilité qu'il y ait **au moins** $k$ succès :
$$P(X \ge k) = \sum_{j=k}^{n}\binom{n}{j}p^j(1 - p)^{n-j}.$$

**Exemple : un système « $k$ parmi $n$ »** (*k-out-of-n system*). Une grappe de stockage a 6 disques, et elle fonctionne tant qu'au moins 4 disques fonctionnent. Chaque disque fonctionne toute l'année avec la probabilité $0{,}85$, indépendamment des autres. Avec $X$ le nombre de disques qui fonctionnent :
$$P(X = 4) = 15 \times 0{,}85^4 \times 0{,}15^2 \approx 0{,}1762, \quad P(X = 5) = 6 \times 0{,}85^5 \times 0{,}15 \approx 0{,}3993, \quad P(X = 6) = 0{,}85^6 \approx 0{,}3771,$$
et la grappe fonctionne avec la probabilité $P(X \ge 4) \approx 0{,}9527$. Elle tombe en panne si au moins 3 disques sur 6 lâchent : le nombre de pannes suit la loi $\mathcal{B}(6 ;\ 0{,}15)$, et $P(\text{panne}) = 1 - 0{,}9527 \approx 0{,}0473$. Une redondance de 2 disques fait passer d'une fiabilité de $0{,}85$ par disque à $0{,}95$ pour le système (✏️ M14.1).

⚠️ **Erreur classique.** $P(X \ge k)$ n'est pas $P(X > k)$ : la fonction de survie de SciPy, `binom.sf(m, n, p)`, rend $P(X > m)$, donc $P(X \ge k)$ = `binom.sf(k - 1, n, p)`. Avec M08, `testing.binomial_test(k, n, p, alternative="greater")` rend aussi $P(X \ge k)$ (🐛 M14.15).

### Majorer la queue : trois bornes

La somme se calcule exactement, mais elle ne dit pas **à quelle vitesse** la queue diminue quand $n$ grandit. Pour cela, on la majore. On regarde la probabilité d'avoir au moins une proportion $a$ de succès, $P(X \ge na)$, avec $a > p$ :
- **Markov** (M11) : $P(X \ge na) \le \frac{\mathbb{E}[X]}{na} = \frac{p}{a}$ ; cette borne ne dépend pas de $n$, elle ne voit pas que la queue diminue ;
- **Hoeffding** (M11), pour la moyenne $\frac{X}{n}$ de $n$ variables à valeurs dans $[0, 1]$ : $P(X \ge na) \le e^{-2n(a - p)^2}$ ;
- **Chernoff** :
$$\boxed{P(X \ge na) \le e^{-n\,\mathrm{KL}(a \Vert p)}, \qquad \mathrm{KL}(a \Vert p) = a\ln\frac{a}{p} + (1 - a)\ln\frac{1 - a}{1 - p},}$$
la divergence de Kullback-Leibler (M06), en nats, entre les lois de Bernoulli de paramètres $a$ et $p$ ($0\ln 0$ compte pour 0).

**D'où vient la borne de Chernoff.** C'est la méthode de M11 : Markov appliqué à $e^{\lambda X}$, pour un $\lambda > 0$ à choisir. Comme $x \mapsto e^{\lambda x}$ est croissante,
$$P(X \ge na) = P\big(e^{\lambda X} \ge e^{\lambda na}\big) \le e^{-\lambda na}\,\mathbb{E}\big[e^{\lambda X}\big] = e^{-\lambda na}\,\big(1 - p + pe^\lambda\big)^n :$$
$X$ est la somme de $n$ variables de Bernoulli indépendantes, et $\mathbb{E}[e^{\lambda X_i}] = (1 - p) \times e^0 + p \times e^\lambda$ ; l'indépendance transforme l'espérance du produit en produit des espérances. Chaque $\lambda > 0$ donne une borne. La meilleure annule la dérivée du logarithme, $-na + \frac{npe^\lambda}{1 - p + pe^\lambda}$, en
$$e^{\lambda^*} = \frac{a(1 - p)}{p(1 - a)},$$
et, reportée dans la borne, elle donne exactement $e^{-n\,\mathrm{KL}(a \Vert p)}$ (∂ M14.8 fait le calcul). CP2.9 B l'avait faite dans un cas particulier.

**Exemple.** $p = 0{,}3$ et $a = 0{,}5$ : $e^{\lambda^*} = \frac{0{,}5 \times 0{,}7}{0{,}3 \times 0{,}5} = \frac{7}{3}$, soit $\lambda^* = \ln\frac{7}{3} \approx 0{,}847$, et
$$\mathrm{KL}(0{,}5 \Vert 0{,}3) = 0{,}5\ln\frac{0{,}5}{0{,}3} + 0{,}5\ln\frac{0{,}5}{0{,}7} \approx 0{,}0872, \qquad 2(a - p)^2 = 0{,}08.$$

| $n$ | queue exacte $P(X \ge n/2)$ | Chernoff $e^{-0{,}0872\,n}$ | Hoeffding $e^{-0{,}08\,n}$ |
|---|---|---|---|
| 20 | 0,0480 | 0,175 | 0,202 |
| 40 | 0,00625 | 0,0306 | 0,0408 |
| 100 | $2{,}2 \times 10^{-5}$ | $1{,}6 \times 10^{-4}$ | $3{,}4 \times 10^{-4}$ |

![La queue exacte de B(n ; 0,3) au-delà de n/2 et ses bornes de Hoeffding et de Chernoff, en échelle logarithmique : trois droites presque parallèles, Chernoff entre les deux autres](figures/queue_binomiale.png)

Les trois courbes sont presque des droites en échelle logarithmique : la queue décroît **exponentiellement** en $n$. La borne de Chernoff a presque la bonne pente : la queue exacte vaut $e^{-n\,\mathrm{KL}(a \Vert p)}$ à un facteur près qui ne décroît que comme une puissance de $n$. Ni Markov ni Tchebychev ne voient cette décroissance exponentielle.

**Chernoff contre Hoeffding.** L'**inégalité de Pinsker** (*Pinsker's inequality*), que l'on admet, dit que $\mathrm{KL}(a \Vert p) \ge 2(a - p)^2$ : la borne de Chernoff est toujours au moins aussi bonne. L'écart est grand pour les **événements rares**, quand $p$ est près de 0 ou de 1 : pour $p = 0{,}01$ et $a = 0{,}05$, $\mathrm{KL} \approx 0{,}0413$, treize fois $2(a - p)^2 = 0{,}0032$. Hoeffding n'utilise que l'intervalle $[0, 1]$ des valeurs ; Chernoff utilise la loi exacte.

**De l'autre côté.** Pour $a < p$, la même méthode appliquée à $n - X$ (le nombre d'échecs, de loi $\mathcal{B}(n, 1 - p)$) donne $P(X \le na) \le e^{-n\,\mathrm{KL}(a \Vert p)}$.

### Des décisions indépendantes qui se trompent ensemble

La borne dit à quelle vitesse il devient improbable que **beaucoup d'essais indépendants échouent à la fois**. Si $n$ décisions indépendantes sont chacune justes avec une probabilité $q > \frac{1}{2}$, la probabilité que la majorité se trompe est au plus $e^{-n\,\mathrm{KL}(1/2 \Vert 1 - q)}$ : elle tend vers 0 exponentiellement en $n$. C'est la forme générale du **théorème du jury** de Condorcet. Tout repose sur l'**indépendance** : avec des décisions corrélées, la majorité se trompe ensemble, et le §2 dit ce que la corrélation coûte.

🔗 **Dans workbookIA** — le chapitre 14 fait voter des classifieurs, et compte la probabilité qu'une majorité se trompe.

## §2 · La variance d'une moyenne de variables corrélées

### La formule

$X_1, \ldots, X_M$ sont des variables (les prédictions de $M$ modèles pour un même exemple, ou $M$ mesures d'une même grandeur), de matrice de covariance $\boldsymbol{\Sigma}$ : $\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$, et $\Sigma_{ii} = \mathbb{V}(X_i)$ (M02c). Pour des poids $w_1, \ldots, w_M$, la covariance est bilinéaire, donc
$$\boxed{\mathbb{V}\Big(\sum_{i=1}^M w_iX_i\Big) = \sum_{i=1}^M\sum_{j=1}^M w_iw_j\operatorname{Cov}(X_i, X_j) = \mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}.}$$
Les $M$ termes diagonaux sont les variances, pondérées par $w_i^2$ ; les $M(M - 1)$ autres sont les covariances, chacune comptée deux fois ($\Sigma_{ij} = \Sigma_{ji}$). Une covariance positive **augmente** la variance de la moyenne, une covariance négative la **diminue**.

**Exemple : trois capteurs.** Trois capteurs mesurent la même température, avec des erreurs de matrice de covariance
$$\boldsymbol{\Sigma} = \begin{pmatrix} 4 & 2 & 0 \\ 2 & 9 & -1 \\ 0 & -1 & 1 \end{pmatrix}.$$
- La **moyenne simple** ($w_i = \frac{1}{3}$) : $\frac{1}{9}$ fois la somme de toutes les cases, $\frac{16}{9} \approx 1{,}78$. Sans les covariances, on aurait trouvé $\frac{4 + 9 + 1}{9} = \frac{14}{9} \approx 1{,}56$ : la covariance $+2$ coûte plus que ce que la covariance $-1$ rapporte.
- Avec les poids $\mathbf{w} = (0{,}2 ;\ 0{,}1 ;\ 0{,}7)$ : $0{,}04 \times 4 + 0{,}01 \times 9 + 0{,}49 \times 1 + 2\,(0{,}2 \times 0{,}1 \times 2 - 0{,}1 \times 0{,}7 \times 1) = 0{,}74 - 0{,}06 = 0{,}68$, mieux que le meilleur capteur seul (variance 1).

**Les meilleurs poids.** Minimiser $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ sous $\sum_i w_i = 1$ est un problème de Lagrange (M13b) : $2\boldsymbol{\Sigma}\mathbf{w} = \lambda\mathbf{1}$, donc $\mathbf{w}^* \propto \boldsymbol{\Sigma}^{-1}\mathbf{1}$, et la variance minimale vaut $\frac{1}{\mathbf{1}^\top\boldsymbol{\Sigma}^{-1}\mathbf{1}}$. Ici, $\mathbf{w}^* = \left(\frac{1}{11}, \frac{3}{22}, \frac{17}{22}\right)$ et la variance vaut $\frac{7}{11} \approx 0{,}64$. Pour des variables **indépendantes**, $\boldsymbol{\Sigma}$ est diagonale et $w_i^* \propto \frac{1}{\sigma_i^2}$ : la **pondération par l'inverse de la variance** (*inverse-variance weighting*) ; la variance minimale vaut alors $\frac{1}{\sum_i 1/\sigma_i^2}$.

**Une borne générale.** Si chaque $X_i$ a une variance au plus $\sigma^2$, toute moyenne pondérée (poids positifs de somme 1) a une variance au plus $\sigma^2$ : moyenner ne fait jamais pire que le pire des $X_i$ (∂ M14.7, avec $\lvert\operatorname{Cov}(X_i, X_j)\rvert \le \sigma_i\sigma_j$).

### Moyenner des prédictions corrélées : un plancher

Pour $M$ variables **indépendantes** de même variance $\sigma^2$, la moyenne simple a la variance $\frac{\sigma^2}{M}$ : elle tend vers 0 quand $M$ grandit. Des modèles entraînés sur les mêmes données font pourtant des erreurs **corrélées**. Un modèle simple de cette situation : chaque prédiction a une **part commune** $Z$ et une **part propre** $E_i$,
$$X_i = a_iZ + E_i,$$
avec $\mathbb{V}(Z) = 1$, $\mathbb{V}(E_i) = s_i$, et toutes ces variables indépendantes. Alors $\operatorname{Cov}(X_i, X_j) = a_ia_j$ pour $i \ne j$, et la moyenne simple vaut $\bar{a}Z + \frac{1}{M}\sum_i E_i$, de variance
$$\mathbb{V}(\bar{X}) = \bar{a}^2 + \frac{1}{M^2}\sum_{i=1}^M s_i, \qquad \bar{a} = \frac{1}{M}\sum_{i=1}^M a_i.$$
Le second terme tend vers 0 (au plus $\frac{\max s_i}{M}$) ; le premier reste : **moyenner réduit la part propre, pas la part commune**. Le plancher $\bar{a}^2$ ne baisse que si les modèles dépendent **moins** de la même part, c'est-à-dire s'ils sont **décorrélés**.

![La variance de la moyenne de M prédictions à part commune, en fonction de M en échelle logarithmique : elle descend vite, puis se stabilise sur le carré de la moyenne des aᵢ ; sans part commune, elle tendrait vers 0](figures/variance_moyenne.png)

C'est l'idée d'une **forêt aléatoire** (*random forest*) : des arbres entraînés sur des tirages différents des mêmes données restent très corrélés ; en ne laissant à chaque nœud qu'une partie des features au hasard, on rend leurs erreurs moins semblables, et l'on abaisse le plancher, au prix d'arbres un peu moins bons chacun. 🔬 M14.13 et 🔗 M14.9 chiffrent un plancher sur deux groupes de modèles.

🔗 **Dans workbookIA** — le chapitre 14 moyenne des arbres (bagging, forêts aléatoires) et mesure ce que la corrélation entre eux coûte.

## §3 · La limite $(1 + x/n)^n \to e^x$

### L'énoncé et l'idée

> **Pour tout réel $x$,** $\displaystyle\lim_{n \to +\infty}\left(1 + \frac{x}{n}\right)^n = e^x$.

**Idée.** Pour $n > \lvert x \rvert$, $1 + \frac{x}{n} > 0$, et $\left(1 + \frac{x}{n}\right)^n = \exp\left(n\ln\left(1 + \frac{x}{n}\right)\right)$. Le développement de Taylor de M05a, $\ln(1 + u) = u - \frac{u^2}{2} + \cdots$ pour $u$ petit, donne, avec $u = \frac{x}{n}$,
$$n\ln\left(1 + \frac{x}{n}\right) = x - \frac{x^2}{2n} + \cdots \xrightarrow[n \to +\infty]{} x,$$
et l'exponentielle est continue. ∂ M14.6 rend ce « $\cdots$ » rigoureux, en encadrant $\ln(1 + u)$.

**La vitesse.** Le même calcul donne $\left(1 + \frac{x}{n}\right)^n \approx e^x\,e^{-x^2/(2n)} \approx e^x\left(1 - \frac{x^2}{2n}\right)$ : l'erreur relative vaut environ $-\frac{x^2}{2n}$. Il faut que $n$ soit grand **devant $x^2$**, pas seulement grand. Pour $x = 2$ ($e^2 \approx 7{,}3891$) :

| $n$ | 1 | 2 | 10 | 100 | 1 000 |
|---|---|---|---|---|---|
| $(1 + 2/n)^n$ | 3 | 4 | 6,1917 | 7,2446 | 7,3743 |
| erreur relative | $-59\,\%$ | $-46\,\%$ | $-16\,\%$ | $-1{,}95\,\%$ | $-0{,}20\,\%$ |
| $-x^2/(2n)$ | | | $-20\,\%$ | $-2\,\%$ | $-0{,}2\,\%$ |

La suite **croît** vers $e^2$ ; l'approximation de l'erreur devient bonne dès que $\frac{x^2}{n}$ est petit.

![(1 + 2/n)ⁿ et (1 − 3/n)ⁿ en fonction de n, en échelle logarithmique : les deux suites montent vers e² et e⁻³](figures/limite_exponentielle.png)

### Deux usages

**Des intérêts composés en continu** (*continuous compounding*). Un placement à 5 % par an, dont les intérêts sont versés $n$ fois par an (chaque fois $\frac{5}{n}$ %), est multiplié en un an par $\left(1 + \frac{0{,}05}{n}\right)^n$ : 1,05 pour $n = 1$, $\approx 1{,}051162$ pour un versement mensuel, et au plus $e^{0{,}05} \approx 1{,}051271$, quel que soit $n$.

**Une survie.** Une journée est coupée en $n$ créneaux ; dans chacun, une panne survient avec la probabilité $\frac{3}{n}$, indépendamment. La probabilité d'une journée sans panne vaut $\left(1 - \frac{3}{n}\right)^n$ : $\approx 0{,}0282$ pour $n = 10$, $\approx 0{,}0476$ pour $n = 100$, et tend vers $e^{-3} \approx 0{,}0498$, la probabilité de 0 pour la loi de Poisson de paramètre 3 (M02b). Le nombre de pannes, de loi $\mathcal{B}\left(n, \frac{3}{n}\right)$, tend vers cette loi de Poisson.

**Multiplicatif et exponentiel.** Pour $\eta$ petit, $1 - \eta \approx e^{-\eta}$, donc multiplier $L$ fois un poids par $1 - \eta$ revient presque à le multiplier par $e^{-\eta L}$ : les poids **multiplicatifs** et les poids **exponentiels** du §4 sont presque les mêmes.

## §4 · Des poids exponentiels : l'algorithme Hedge

### Prédire avec des experts

$K$ **experts** (des modèles, des règles, des prévisionnistes) font chacun une prédiction à chaque tour. Au tour $t$, avant de voir le résultat, tu choisis une loi $\mathbf{w}_t$ sur les experts (tu suis l'expert $k$ avec la probabilité $w_t[k]$, ou tu mélanges leurs avis avec ces poids). Puis chaque expert reçoit une loss $\ell_t[k] \in [0, 1]$, et tu subis la loss moyenne $\mathbf{w}_t \cdot \boldsymbol{\ell}_t$. On ne suppose rien sur la façon dont les losses sont produites : elles peuvent même être choisies contre toi.

Ton **regret** après $T$ tours compare ta loss totale à celle du meilleur expert, choisi après coup :
$$R_T = \sum_{t=1}^T \mathbf{w}_t \cdot \boldsymbol{\ell}_t - \min_k L_{T+1}[k], \qquad L_t[k] = \sum_{s < t}\ell_s[k].$$
C'est le regret de M11, dans un cadre plus riche : en M11, on ne voyait que la récompense de l'option choisie (un bandit) ; ici, on voit les losses de **tous** les experts (information complète, *full information*).

### Les poids exponentiels

**Hedge** donne à chaque expert un poids qui décroît exponentiellement avec sa loss cumulée :
$$w_t[k] = \frac{e^{-\eta L_t[k]}}{\sum_{j=1}^K e^{-\eta L_t[j]}},$$
avec un **learning rate** $\eta > 0$. Avant le premier tour, toutes les losses cumulées sont nulles : les poids sont uniformes. D'un tour à l'autre, chaque poids est multiplié par $e^{-\eta\ell_t[k]}$, puis tous sont renormalisés (une mise à jour **multiplicative**).

**Le calcul en pratique.** Pour de grandes losses, tous les $e^{-\eta L_t[k]}$ deviennent 0 en flottants (*underflow*), et la normalisation divise 0 par 0. On retranche donc la plus petite loss cumulée, $L_t[k] - \min_j L_t[j]$, avant l'exponentielle : la normalisation annule ce facteur commun, et le meilleur expert garde l'exposant 0 (l'astuce de log-somme-exp, M04 et M05a).

**Exemple.** Trois experts, $\eta = 0{,}5$, quatre tours :

| tour $t$ | losses $\boldsymbol{\ell}_t$ | losses cumulées avant $t$ | poids $\mathbf{w}_t$ | ta loss $\mathbf{w}_t \cdot \boldsymbol{\ell}_t$ |
|---|---|---|---|---|
| 1 | $(0 ;\ 1 ;\ 0{,}5)$ | $(0 ;\ 0 ;\ 0)$ | $(0{,}333 ;\ 0{,}333 ;\ 0{,}333)$ | 0,5 |
| 2 | $(1 ;\ 0 ;\ 0{,}5)$ | $(0 ;\ 1 ;\ 0{,}5)$ | $(0{,}419 ;\ 0{,}254 ;\ 0{,}327)$ | 0,583 |
| 3 | $(0 ;\ 1 ;\ 0{,}5)$ | $(1 ;\ 1 ;\ 1)$ | $(0{,}333 ;\ 0{,}333 ;\ 0{,}333)$ | 0,5 |
| 4 | $(0 ;\ 0 ;\ 1)$ | $(1 ;\ 2 ;\ 1{,}5)$ | $(0{,}419 ;\ 0{,}254 ;\ 0{,}327)$ | 0,327 |

Au tour 2, $e^{-0{,}5 \times (0 ;\ 1 ;\ 0{,}5)} = (1 ;\ 0{,}607 ;\ 0{,}779)$, de somme $2{,}385$, d'où les poids. Ta loss totale vaut $\approx 1{,}909$ ; le meilleur expert, le premier, a perdu 1 en tout : le regret vaut $\approx 0{,}909$.

### Le regret de Hedge

> **Théorème.** Pour des losses dans $[0, 1]$, Hedge de learning rate $\eta$ a, sur $T$ tours et pour toute suite de losses, un regret
> $$R_T \le \frac{\ln K}{\eta} + \frac{\eta T}{8}.$$

<details><summary>L'idée de la démonstration (facultatif)</summary>

On suit le « potentiel » $\Phi_t = \ln\sum_k e^{-\eta L_t[k]}$. Au départ, $\Phi_1 = \ln K$. À chaque tour, $\Phi_{t+1} - \Phi_t = \ln\sum_k w_t[k]\,e^{-\eta\ell_t[k]}$ : c'est le logarithme de l'espérance de $e^{-\eta\ell}$ quand on tire un expert selon $\mathbf{w}_t$. Le lemme de Hoeffding (M11) le majore par $-\eta\,\mathbf{w}_t \cdot \boldsymbol{\ell}_t + \frac{\eta^2}{8}$. En sommant sur les $T$ tours, $\Phi_{T+1} - \ln K \le -\eta\sum_t \mathbf{w}_t \cdot \boldsymbol{\ell}_t + \frac{T\eta^2}{8}$. Enfin, la somme qui définit $\Phi_{T+1}$ est au moins son plus grand terme : $\Phi_{T+1} \ge -\eta\min_k L_{T+1}[k]$. On réunit les deux inégalités et on divise par $\eta$.
</details>

Sur l'exemple : $\frac{\ln 3}{0{,}5} + \frac{0{,}5 \times 4}{8} \approx 2{,}45$, au-dessus du regret $0{,}909$.

**Choisir $\eta$.** Les deux termes tirent en sens contraires : un petit $\eta$ change lentement les poids (le premier terme grandit), un grand $\eta$ suit le dernier en tête, et ses à-coups (le second terme grandit). Le minimum de $\frac{\ln K}{\eta} + \frac{\eta T}{8}$ est atteint en $\eta = \sqrt{\frac{8\ln K}{T}}$, où la borne vaut
$$R_T \le \sqrt{\frac{T\ln K}{2}}.$$
Le regret grandit comme $\sqrt{T}$, donc le **regret moyen** $\frac{R_T}{T}$ tend vers 0 : à long terme, tu fais en moyenne aussi bien que le meilleur expert, sans jamais savoir lequel c'est. Et la borne ne dépend de $K$ que par $\ln K$ : mille experts coûtent à peine plus que dix.

![Les poids de quatre experts au fil de 100 tours, pour η = 0,1 et η = 0,8 : avec le petit η, les poids restent répartis ; avec le grand, ils se concentrent sur l'expert en tête](figures/hedge_poids.png)

**Sans connaître $T$.** Le bon $\eta$ dépend de l'horizon $T$. Quand on ne le connaît pas, on prend un learning rate qui **décroît** avec le tour, $\eta_t = \sqrt{\frac{8\ln K}{t}}$ ; on admet que le regret reste alors au plus $\sqrt{2T\ln K} + \sqrt{\frac{\ln K}{8}}$, à peine deux fois la borne avec le meilleur $\eta$ fixe (🏆 M14.17).

🔗 **Dans workbookIA** — le chapitre 14 combine des classifieurs avec des poids, et AdaBoost repondère les **exemples** de façon exponentielle (§5).

## §5 · Le gradient d'une loss par rapport aux prédictions

### Le vecteur des prédictions

Sur $n$ exemples d'entraînement, un modèle produit un **vecteur de prédictions** $\mathbf{F} = (F_1, \ldots, F_n)$, une prédiction par exemple. La loss totale ne dépend que de lui :
$$\mathcal{L}(\mathbf{F}) = \sum_{i=1}^n \ell(y_i, F_i).$$
Chaque terme ne dépend que d'une coordonnée de $\mathbf{F}$ : la coordonnée $i$ du gradient (M05b) est la dérivée d'une fonction d'une variable,
$$\big(\nabla_{\mathbf{F}}\mathcal{L}\big)_i = \frac{\partial\ell}{\partial F}(y_i, F_i).$$
Ce gradient dit, exemple par exemple, dans quel sens bouger chaque prédiction pour faire baisser la loss, et de combien elle baisserait au premier ordre.

### La loss exponentielle : des poids exponentiels sur les exemples

Pour des labels $y_i \in \{-1, +1\}$ et un score $F_i$, la **loss exponentielle** (*exponential loss*) vaut $\ell(y, F) = e^{-yF}$ : elle est petite quand la marge $yF$ est grande, et énorme quand l'exemple est nettement mal classé. Sa dérivée en $F$ vaut
$$\frac{\partial}{\partial F}e^{-yF} = -y\,e^{-yF} :$$
le gradient pousse chaque prédiction vers son label ($-y$), avec une force égale à la **loss actuelle** de l'exemple.

**Exemple.** Quatre exemples, de labels $\mathbf{y} = (+1, -1, +1, -1)$ et de scores $\mathbf{F} = (0{,}5 ;\ 0{,}2 ;\ -1 ;\ -0{,}8)$. Les marges valent $0{,}5$, $-0{,}2$, $-1$ et $0{,}8$ ; les losses $e^{-yF}$, $0{,}607$, $1{,}221$, $2{,}718$ et $0{,}449$ ; le gradient, $(-0{,}607 ;\ 1{,}221 ;\ -2{,}718 ;\ 0{,}449)$. Normalisées, les losses donnent les poids $(0{,}121 ;\ 0{,}244 ;\ 0{,}544 ;\ 0{,}090)$ : l'exemple le plus mal classé (le troisième) pèse plus de la moitié. Ce sont des **poids exponentiels**, comme au §4, mais sur les **exemples**, avec la marge à la place de la loss cumulée.

### La loss de Huber : une force bornée

Pour une régression, la loss de Huber de M09b porte sur le résidu $r = y - F$ : $\frac{1}{2}r^2$ si $\lvert r \rvert \le \delta$, $\delta\left(\lvert r \rvert - \frac{\delta}{2}\right)$ sinon. Sa dérivée en $F$ vaut
$$\frac{\partial}{\partial F}\ell_\delta(y - F) = -\operatorname{clip}(y - F,\ -\delta,\ \delta),$$
où $\operatorname{clip}(r, -\delta, \delta)$ ramène $r$ dans $[-\delta, \delta]$. Avec $\delta = 1$ et les résidus $(0{,}4 ;\ -2{,}5 ;\ 1{,}2 ;\ -0{,}3)$, le gradient vaut $(-0{,}4 ;\ 1 ;\ -1 ;\ 0{,}3)$ : le point aberrant (résidu $-2{,}5$) tire sa prédiction avec la force 1, pas $2{,}5$.

![À gauche, la loss exponentielle et sa dérivée en fonction de la marge ; à droite, la loss de Huber et sa dérivée, bornée par δ, en fonction du résidu](figures/losses_gradients.png)

### Descendre le gradient dans l'espace des prédictions (idée)

Un pas de descente de gradient sur $\mathbf{F}$ serait $\mathbf{F} \leftarrow \mathbf{F} - \eta\,\nabla_{\mathbf{F}}\mathcal{L}$. Mais un modèle ne peut pas fixer chaque $F_i$ à sa guise : il doit prédire aussi sur de nouveaux exemples. L'idée est alors d'**approcher** la direction $-\nabla_{\mathbf{F}}\mathcal{L}$ par un modèle simple, entraîné sur les exemples, et d'ajouter ce modèle, multiplié par un petit pas, à l'ensemble : une descente de gradient dans un espace de fonctions. Le choix de la loss fixe la direction : la loss exponentielle insiste sur les exemples mal classés, la loss de Huber ne laisse pas un point aberrant tout décider.

⚠️ **Erreur classique.** Ne confonds pas ce gradient, par rapport aux **prédictions**, avec le gradient par rapport aux **paramètres** $\mathbf{w}$ d'un modèle : les deux sont reliés par la règle de la chaîne, que M18 généralisera.

🔗 **Dans workbookIA** — le chapitre 14 construit AdaBoost et le gradient boosting, qui ajoutent des modèles l'un après l'autre en suivant ce gradient.

## Les pièges classiques ⚠️ (récapitulatif)

- **$P(X \ge k)$ ou $P(X > k)$.** `binom.sf(k - 1, n, p)` pour « au moins $k$ ».
- **Le sens de la divergence.** La borne de Chernoff utilise $\mathrm{KL}(a \Vert p)$ : d'abord la proportion de l'événement, puis le paramètre de la loi. $\mathrm{KL}$ n'est pas symétrique.
- **Une borne pour $a \le p$.** Elle ne dit rien : la probabilité n'est pas petite.
- **Oublier les covariances.** $\mathbb{V}(\sum w_iX_i) \ne \sum w_i^2\,\mathbb{V}(X_i)$ dès que les variables sont corrélées.
- **$\frac{\sigma^2}{M}$ pour des modèles corrélés.** Moyenner ne réduit que la part propre des erreurs.
- **$(1 + x/n)^n$ pour $n$ « grand ».** Il faut $n$ grand devant $x^2$.
- **Des poids non renormalisés, ou qui débordent.** Divise par la somme ; retranche la plus petite loss cumulée avant l'exponentielle.
- **Le signe dans l'exponentielle.** Le poids d'un expert est $e^{-\eta L}$ : une grande loss, un **petit** poids.
- **Le gradient par rapport à quoi ?** Aux prédictions $\mathbf{F}$ ici, pas aux paramètres.

## Et maintenant

**Dans ce dépôt** : CP3, l'examen blanc de la partie III, juste avant le checkpoint III de workbookIA ; puis M16, qui ouvre la partie IV (réseaux de neurones).

**Dans workbookIA** : le chapitre 14 fait voter des classifieurs, moyenne des arbres (bagging, forêts aléatoires) et construit AdaBoost et le gradient boosting. Tu sais maintenant pourquoi un vote de modèles indépendants se trompe rarement, ce que leur corrélation coûte, d'où viennent des poids exponentiels, et ce que veut dire « suivre le gradient » d'une loss quand on ajoute des modèles.

## Pour aller plus loin

- Les lectures conseillées en tête de fiche.
- `annexes/symboles.md` (lire $\mathrm{KL}(a \Vert p)$, $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ et $\nabla_{\mathbf{F}}$ à voix haute), `annexes/formulaire.md` et `annexes/erreurs_frequentes.md`.
