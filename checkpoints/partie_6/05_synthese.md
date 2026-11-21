# CP6 · Synthèse de la partie VI (M25a, M25b, M26, M27 et M28)

> La synthèse se fait **avant** l'examen blanc, un autre jour si possible. Commence par l'exercice CP6.11 : construire **ta** carte mentale et **ta** fiche d'une page. Ensuite seulement, compare-les avec les sections 1 à 4 de ce fichier, puis lis les sections 5 et 6 : ce que tu as oublié, c'est ce qu'il faut revoir. Compte 60 minutes pour CP6.11, et un quart d'heure pour comparer et lire.

**Cinq chapitres, cinq questions**

1. **M25a · Gaussienne multivariée, conditionnement et divergence KL** : *comment décrire, tirer, lire et comparer un nuage gaussien ?* La densité et la distance de Mahalanobis, la loi de $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ et le tirage par Cholesky, les ellipses et leur masse, les lois marginales et conditionnelles par le complément de Schur, Bayes avec des gaussiennes, le maximum de vraisemblance, la KL continue et l'interpolation sphérique.
2. **M25b · Variables latentes et ELBO** : *comment raisonner sur ce qu'on n'observe pas ?* Les graphes orientés et le tirage ancestral, marginaliser et inverser, les mélanges et leurs responsabilités, l'EM, l'ELBO et son écart, l'ACP probabiliste, le sens de la KL, l'inférence amortie, la dérivée d'une espérance, et la KL pondérée par $\beta$.
3. **M26 · Chaînes de Markov et équation de Bellman** : *où sera un système qui oublie son passé, et combien rapporte-t-il ?* La loi à $n$ pas, la loi stationnaire et la vitesse de convergence, l'analyse au premier pas, le retour et la valeur, le système de Bellman d'une politique fixée, la contraction, un maximum dans l'opérateur, et les estimations par échantillons.
4. **M27 · Jeux et distances entre lois** : *que jouer contre un adversaire, et à quelle distance sont deux lois ?* Maximin, minimax et point selle, les stratégies mixtes, Nash et les arbres, la descente-montée, la log-loss et Jensen-Shannon, le transport et les distances de Wasserstein, la distance de Fréchet et son biais, et la mesure d'une dérive.
5. **M28 · Matrice de Gram, montée sur l'entrée et lois tronquées** : *que dit une table de produits scalaires, comment pousser une entrée, et comment modifier une loi avant de tirer ?* La matrice de Gram et ses deux lectures, des distances aux positions, la montée sur l'entrée, la variation totale et les fréquences spatiales, la température, le top-k et le top-p avec leur coût, et les itérations qui bouclent.

## CP6.11 — Ta carte mentale et ta fiche d'une page 🗣️ ★ ⏱️ 60 min

**Objectif :** organiser toute la partie VI dans ta tête, avant l'examen, et repérer ce qui manque.

1. **De mémoire, sans rien ouvrir (20 min).** Écris au centre d'une grande feuille les cinq questions ci-dessus. Autour de chacune, place les objets (un vecteur gaussien, un mélange, une chaîne, une matrice de gains, un nuage de points, une loi catégorielle), puis leurs formules et leurs théorèmes. Ensuite, entoure d'une même couleur chaque notion qui sert dans **deux chapitres au moins** (la KL, la loi stationnaire, la valeur propre dominante, la moyenne et la covariance, la loi conditionnelle…) et relie ses apparitions. Écris sur chaque flèche **pourquoi** elle existe.
2. **Avec les fiches (25 min).** Ouvre les fiches de M25a à M28 (sections « L'essentiel » et « Les pièges classiques »), la partie VI de `annexes/formulaire.md` et les sections M25a à M28 de `annexes/erreurs_frequentes.md`. Complète ta carte d'une autre couleur : tout ce que tu ajoutes maintenant est à revoir.
3. **Ta fiche d'une page (15 min).** Sur une seule page :
   - les 20 à 25 formules ou règles que tu veux avoir en tête le jour de l'examen, chacune avec sa **condition** (ce qu'elle suppose) ;
   - le tableau des mesures entre deux lois de la section 3 : recopie sa seule ligne d'en-tête (mesure, définition, valeurs, unité, symétrie, saturation, chapitre), puis remplis de mémoire une ligne par mesure (KL, PSI, Jensen-Shannon, variation totale, Kolmogorov-Smirnov, $W_1$, $W_2$) ;
   - les cinq pièges qui te concernent le plus, tirés de tes copies de M25a à M28.
4. **Compare** avec les sections 1 à 4 ci-dessous, puis garde ta carte et ta fiche dans `mon_travail/checkpoints/partie_6/` (une photo suffit).

**Grille de relecture.** Une bonne synthèse :
1. contient les cinq chapitres et chacune de leurs sections ;
2. a au moins huit flèches justifiées, entre les chapitres de la partie VI et vers les parties précédentes ;
3. donne chaque formule avec ses conventions et ses conditions :
   - le second paramètre de $\mathcal{N}$ est une covariance, $\mathbf{L}$ est triangulaire inférieur ;
   - le sens et l'unité d'une KL ;
   - la convention ligne des chaînes, et $\gamma = 1$ seulement quand la fin est sûre ;
   - qui maximise dans une matrice de gains ;
   - les points en lignes et les **carrés** des distances ;
   - la puissance $\frac1T$, et la masse **gardée** $P(S)$ ;
4. a son tableau des mesures entre lois rempli sans erreur de sens ni d'unité ;
5. a des pièges tirés de tes propres erreurs ;
6. tient sur une page pour la fiche.

## 1. La carte de référence, question par question

```text
DÉCRIRE ET TIRER UN NUAGE                                                       M25a
  N(μ, Σ) : densité, Mahalanobis Δ² = (x − μ)ᵀΣ⁻¹(x − μ), ln det Σ = 2 Σ ln Lᵢᵢ
  ├─ Ax + b gaussien, de covariance AΣAᵀ ; deux marginales gaussiennes ne suffisent pas
  ├─ tirer : μ + Lε, L de Cholesky ; blanchir : L⁻¹(x − μ) ; en lignes : 1μᵀ + E Lᵀ
  ├─ ellipses Δ = c : axes propres, demi-axes c√λᵢ ; masse 1 − e^{−c²/2} en dimension 2 (khi-deux sinon)
  └─ la norme d'un tirage en grande dimension : une couronne, pas le centre

LIRE UNE COORDONNÉE, SAVOIR LES AUTRES                                          M25a
  ├─ marginale : le sous-bloc ; conditionnelle : moyenne affine, complément de Schur
  ├─ précision Λ = Σ⁻¹ : zéros = indépendances conditionnelles
  ├─ Bayes gaussien : les précisions s'additionnent ; régression bayésienne, évidence
  └─ maximum de vraisemblance : x̄ et S/n (gradients de ln det et de la trace, M18)

RAISONNER SUR CE QU'ON NE VOIT PAS                                              M25b
  graphe orienté → loi jointe → tirage ancestral ; collision : l'effet commun lie les causes
  ├─ évidence p(x) = Σ p(z) p(x | z) ; posterior par Bayes ; variance totale d'un mélange
  ├─ responsabilités en log (log-sum-exp) → EM : pas E, pas M pondéré par Nₖ
  ├─ ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) ; l'EM monte l'ELBO en q puis en θ
  ├─ ACP probabiliste : WWᵀ + σ²I, W défini à une rotation près ; angles principaux
  └─ approcher : sens de la KL, inférence amortie, dérivée par le chemin, β et I(X ; Z)

SUIVRE UNE SUITE D'ÉTATS                                                        M26, M28 §6
  P stochastique, convention ligne μₜ₊₁ = μₜP ; chemins de longueur n dans Pⁿ
  ├─ loi stationnaire πP = π : existe ; unique si irréductible ; limite si apériodique, en |λ₂|ⁿ (pour P diagonalisable)
  ├─ premier pas : absorption, durée moyenne, N = (I − Q)⁻¹
  ├─ valeur V = r + γPV, système linéaire ; fin possible = ligne sous-stochastique
  ├─ opérateur de Bellman : γ-contraction ; un maximum : arrêt optimal, optimalité
  ├─ échantillons : moyenne de retours, erreur TD, biais du maximum
  └─ une suite déterministe sur un ensemble fini boucle : prépériode μ, période λ, μ + λ ≤ N

JOUER CONTRE QUELQU'UN                                                          M27
  matrice de gains G : maximin ≤ minimax, point selle ; dominance
  ├─ mixtes : indifférence, valeur v, von Neumann, programme linéaire
  ├─ Nash (somme non nulle), induction arrière
  └─ descente-montée sur xᵀAy : simultanée ou alternée

COMPARER DEUX LOIS                                                              M25a, M27, M28
  KL (sens, infinie, additive) ; KL entre gaussiennes ; JS ∈ [0, ln 2]
  ├─ transport : couplages, Wₚ ; dimension 1 : trier et apparier, quantiles
  ├─ Fréchet = W₂ entre gaussiennes ; biais d'une distance estimée en tr Σ / n
  ├─ dérive : PSI, KS, W₁ ; log-loss et probabilité a posteriori
  └─ distance en variation totale ½‖p − q‖₁

UNE TABLE DE PRODUITS SCALAIRES                                                 M28
  G = XXᵀ (lignes) et XᵀX (colonnes) : mêmes valeurs propres non nulles
  ├─ distances ↔ Gram : double centrage −½ J D⁽²⁾ J ; euclidiennes ⇔ semi-définie positive
  └─ positions √λₖ qₖ, à une isométrie près

MODIFIER CE QU'ON TIRE OU CE QU'ON MONTRE                                       M28, M25a §8
  ├─ une loi : température p^{1/T}, top-k, top-p, coût −ln P(S) ; tirer dans une loi conditionnelle
  ├─ une entrée : montée, pas normalisé, projection sur un pavé, coordonnées gelées
  ├─ une grille : variation totale xᵀLx, diffusion, fréquences, flou
  └─ entre deux tirages gaussiens : slerp, sur la sphère
```

## 2. Les ponts, chacun avec sa raison

- **Le fil de la KL, de M25a à M28.** Définie et minorée par Jensen en M25a §7, elle mesure l'écart à l'ELBO en M25b §5, choisit un mode ou couvre la masse selon son sens en M25b §7, compose Jensen-Shannon et le PSI en M27 §6 et §10, et donne le coût d'une troncature en M28 §5. Chaque fois, la même question : sous quelle loi prend-on l'espérance ?
- **M25a → M25b.** Les composantes d'un mélange sont des gaussiennes, le posterior de l'ACP probabiliste est une loi conditionnelle de vecteur gaussien (le modèle linéaire gaussien de M25a §5), et l'ELBO d'un modèle gaussien contient une KL entre gaussiennes.
- **M25a → M27 §9.** La distance de Fréchet est la distance $W_2$ entre deux gaussiennes : elle ne lit que deux moyennes et deux covariances, comme la KL de M25a §7, mais elle reste finie et symétrique.
- **M26 → M28 §6.** Suivre une chaîne en prenant toujours l'état suivant le plus probable, c'est itérer une fonction sur un ensemble fini, et M28 §6 dit ce que devient une telle suite.
- **M28 §5 → M26.** Une ligne de matrice stochastique est une loi catégorielle : tout ce qu'on fait à une loi (la tempérer, la tronquer), on peut le faire ligne par ligne à une chaîne.
- **M22 → M26 §5 et M27 §4.** $\rho(\gamma\mathbf{P}) \le \gamma\lVert\mathbf{P}\rVert_\infty < 1$ rend $\mathbf{I} - \gamma\mathbf{P}$ inversible et fait converger la série de Neumann ; le module des valeurs propres complexes d'un pas de descente-montée décide si les itérés s'éloignent ou tournent.
- **M12c → M25a, M27 §9, M28 §2.** Le théorème spectral donne les axes des ellipses, la racine d'une matrice symétrique positive (dans la distance de Fréchet) et les positions $\sqrt{\lambda_k}\thinspace\mathbf{q}_k$ d'un nuage ; la factorisation de Cholesky donne le tirage $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$.
- **M12d → M28 §1 et M25b §6.** $\mathbf{X}\mathbf{X}^\top$ et $\mathbf{X}^\top\mathbf{X}$ ont les mêmes valeurs propres non nulles, les carrés des valeurs singulières de $\mathbf{X}$ ; l'ACP probabiliste prend sa matrice $\mathbf{W}$ dans la SVD.
- **M17 → M28 §5.** La loi tempérée est une loi de Boltzmann, d'énergies $-\ln p_i$ : ses limites en température sont celles de M17.
- **M04, M05a → M25b §3.** Les responsabilités sont la formule de Bayes, calculée en log avec un log-sum-exp pour ne pas dépasser les capacités des flottants.
- **M06 → M25b §8 et M27 §6.** L'entropie et l'information mutuelle mesurent ce qu'un code garde de la donnée ; Jensen-Shannon est l'information mutuelle entre le résultat d'un pile ou face qui choisit une des deux lois et le tirage fait dans la loi choisie (un fait juste que la partie n'a pas démontré ; tu peux le vérifier sur la définition).
- **M21 → M28 §4.** La variation totale est la forme quadratique d'un laplacien discret, et une moyenne mobile est une convolution : ses gains sur les cosinus sont ceux d'une matrice circulante.
- **M13b, M19 (MML §7.1 et §7.2) → M27 §1 et §4.** Maximin ≤ minimax est la dualité faible lue comme un jeu ; la descente-montée est une descente de gradient où l'un des deux joueurs monte.

Redessine les ponts de mémoire : chacun doit pouvoir s'illustrer par un exemple que tu inventes (« deux ateliers dont on résume les mesures par une gaussienne : leur KL vient de M25a §7 et leur distance de Fréchet de M27 §9 ; la première change de valeur quand on échange les deux ateliers, la seconde non »).

## 3. Comparer deux lois : sept mesures

| Mesure | Définition | Valeurs | Unité | Symétrique ? | Quand elle sature ou devient infinie | Chapitre |
|---|---|---|---|---|---|---|
| divergence KL | $\mathrm{KL}(p \thinspace\Vert\thinspace q) = \mathbb{E}_p[\ln p - \ln q]$ | $[0, +\infty]$ | nat | non | infinie dès que $q$ s'annule là où $p$ a de la masse | M25a §7 |
| PSI (Jeffreys) | $\mathrm{KL}(p \thinspace\Vert\thinspace q) + \mathrm{KL}(q \thinspace\Vert\thinspace p) = \sum_k(p_k - q_k)\ln\frac{p_k}{q_k}$ | $[0, +\infty]$ | nat | oui | infinie dès qu'une catégorie est vide d'un seul côté | M27 §10 |
| Jensen-Shannon | $\frac12\mathrm{KL}(p \thinspace\Vert\thinspace m) + \frac12\mathrm{KL}(q \thinspace\Vert\thinspace m)$, $m = \frac12(p + q)$ | $[0, \ln 2]$ | nat | oui | vaut $\ln 2$ pour des supports disjoints, quelle que soit leur distance | M27 §6 |
| distance en variation totale | $\frac12\lVert p - q\rVert_1 = \max_A\lvert p(A) - q(A)\rvert$ | $[0, 1]$ | sans (une probabilité) | oui | vaut 1 pour des supports disjoints | M28 §5 |
| Kolmogorov-Smirnov | $\sup_x\lvert F(x) - G(x)\rvert$ | $[0, 1]$ | sans | oui | vaut 1 pour deux lois séparées sur la droite | M27 §10 |
| $W_1$ | $\min$ du coût moyen $\lvert x - y\rvert$ ; en dimension 1, $\int\lvert F - G\rvert$ | $[0, +\infty[$ | celle de la variable | oui | jamais : elle grandit avec le décalage, même sans recouvrement | M27 §7, §8 |
| $W_2$ (Fréchet entre gaussiennes) | racine du $\min$ du coût moyen $\lVert x - y\rVert^2$ | $[0, +\infty[$ | celle de la variable | oui | jamais ; $W_1 \le W_2$ | M27 §7, §9 |

Deux réflexes : **dis toujours le sens** d'une KL (sous quelle loi l'espérance est prise), et **dis l'unité** d'une distance (nats, probabilité, ou unité de la variable). Une mesure estimée sur des échantillons a aussi un biais : deux échantillons d'une même loi ne sont presque jamais à distance nulle.

## 4. Les formules, avec ce qu'elles supposent

| Objet | À savoir écrire | Ce qu'elle suppose ou ce qu'il faut préciser |
|---|---|---|
| densité (M25a) | $p(\mathbf{x}) = (2\pi)^{-d/2}(\det\boldsymbol{\Sigma})^{-1/2}e^{-\frac12\Delta^2}$, $\Delta^2 = (\mathbf{x} - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ | $\boldsymbol{\Sigma}$ définie positive ; $\ln\det\boldsymbol{\Sigma} = 2\sum_i\ln L_{ii}$ |
| image affine et tirage (M25a) | $\mathbf{A}\mathbf{x} + \mathbf{b} \sim \mathcal{N}(\mathbf{A}\boldsymbol{\mu} + \mathbf{b}, \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top)$ ; $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{L}\mathbf{L}^\top)$ | $\mathbf{x}$ vecteur gaussien (pas seulement des coordonnées gaussiennes) ; $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ |
| ellipses (M25a) | demi-axes $c\sqrt{\lambda_i}$ ; aire $\pi c^2\sqrt{\det\boldsymbol{\Sigma}}$ ; masse $1 - e^{-c^2/2}$ | la masse en $1 - e^{-c^2/2}$ ne vaut qu'en dimension 2 |
| blocs (M25a) | $\mathbf{x} _a \mid \mathbf{x} _b \sim \mathcal{N}\big(\boldsymbol{\mu} _a + \boldsymbol{\Sigma} _{ab}\boldsymbol{\Sigma} _{bb}^{-1}(\mathbf{x} _b - \boldsymbol{\mu} _b),\ \boldsymbol{\Sigma} _{aa} - \boldsymbol{\Sigma} _{ab}\boldsymbol{\Sigma}  _{bb}^{-1}\boldsymbol{\Sigma} _{ba}\big)$ | on divise par la covariance du bloc **lu** ; la covariance ne dépend pas de la valeur lue |
| KL entre gaussiennes (M25a) | $\frac12\big[\operatorname{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0) + \boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta} - d + \ln\frac{\det\boldsymbol{\Sigma}_1}{\det\boldsymbol{\Sigma}_0}\big]$, $\boldsymbol{\delta} = \boldsymbol{\mu}_1 - \boldsymbol{\mu}_0$ | c'est $\mathrm{KL}(p_0 \thinspace\Vert\thinspace p_1)$ : la seconde loi est celle qu'on inverse ; entropie différentielle $\frac12\ln\big((2\pi e)^d\det\boldsymbol{\Sigma}\big)$ |
| slerp (M25a) | $\frac{\sin((1 - t)\Omega)}{\sin\Omega}\mathbf{u} + \frac{\sin(t\Omega)}{\sin\Omega}\mathbf{v}$, $\cos\Omega = \frac{\mathbf{u}^\top\mathbf{v}}{\lVert\mathbf{u}\rVert\thinspace\lVert\mathbf{v}\rVert}$ | garde la norme quand $\lVert\mathbf{u}\rVert = \lVert\mathbf{v}\rVert$ ; $\Omega \ne 0, \pi$ |
| mélange (M25b) | $a_{ik} = \ln\pi_k + \ln\mathcal{N}(\mathbf{x} _i \mid \boldsymbol{\mu} _k, \boldsymbol{\Sigma} _k)$, $\ln r _{ik} = a _{ik} - \operatorname{LSE} _j\thinspace a _{ij}$ ; $N_k = \sum_ir _{ik}$, $\pi_k = \frac{N_k}{n}$, $\boldsymbol{\mu} _k = \frac{1}{N_k}\sum_ir _{ik}\mathbf{x}_i$ | les responsabilités avec les paramètres **du moment** ; variance totale : moyenne des variances + variance des moyennes |
| ELBO (M25b) | $\ln p(\mathbf{x}) = \operatorname{ELBO}(q) + \mathrm{KL}\big(q \thinspace\Vert\thinspace p(\mathbf{z} \mid \mathbf{x})\big)$, $\operatorname{ELBO} = \mathbb{E}_q[\ln p(\mathbf{x} \mid \mathbf{z})] - \mathrm{KL}(q \thinspace\Vert\thinspace p(\mathbf{z}))$ | une borne, atteinte si et seulement si $q$ est le posterior |
| code (M25b) | $\mathbb{E}_{\mathbf{x}}\mathrm{KL}\big(q(\mathbf{z} \mid \mathbf{x}) \thinspace\Vert\thinspace p(\mathbf{z})\big) = I(X ; Z) + \mathrm{KL}\big(q(\mathbf{z}) \thinspace\Vert\thinspace p(\mathbf{z})\big)$ | $q(\mathbf{z})$ est le posterior agrégé, $\mathbb{E}_{\mathbf{x}}[q(\mathbf{z} \mid \mathbf{x})]$ |
| chaîne (M26) | $\boldsymbol{\mu}_n = \boldsymbol{\mu}_0\mathbf{P}^n$ ; $\boldsymbol{\pi}\mathbf{P} = \boldsymbol{\pi}$, $\sum_j\pi_j = 1$ ; écart en $\lvert\lambda_2\rvert^n$ (pour $\mathbf{P}$ diagonalisable) | convention ligne ; unicité si irréductible, convergence si de plus apériodique |
| Bellman (M26) | $\mathbf{V} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$, $\mathbf{V} = (\mathbf{I} - \gamma\mathbf{P})^{-1}\mathbf{r} = \sum_t\gamma^t\mathbf{P}^t\mathbf{r}$ ; $\lVert\mathbf{V} _k - \mathbf{V}\rVert _\infty \le \gamma^k\lVert\mathbf{V} _0 - \mathbf{V}\rVert _\infty$ | $\gamma < 1$, ou $\gamma = 1$ quand la fin est sûre (lignes sous-stochastiques) ; une politique **fixée**, sans maximum |
| jeu $2 \times 2$ (M27) | $\kappa = a - b - c + d$, $p^\star = \frac{d - c}{\kappa}$, $q^\star = \frac{d - b}{\kappa}$, $v = \frac{ad - bc}{\kappa}$ | seulement sans point selle ; sinon, la valeur est celle du point selle |
| descente-montée (M27) | simultanée sur $xy$ : valeurs propres $1 \pm i\eta$ ; alternée : $\lVert\mathbf{x}\rVert^2 + \lVert\mathbf{y}\rVert^2 - \eta\thinspace\mathbf{x}^\top\mathbf{A}\mathbf{y}$ constant | $x$ descend, $y$ monte ; l'alterné utilise déjà le nouveau $x$ |
| Wasserstein (M27) | dimension 1 : trier, apparier ; $W_2^2\big(\mathcal{N}(\mu_1, \sigma_1^2), \mathcal{N}(\mu_2, \sigma_2^2)\big) = (\Delta\mu)^2 + (\Delta\sigma)^2$ ; Fréchet : $\lVert\Delta\boldsymbol{\mu}\rVert^2 + \operatorname{tr}\boldsymbol{\Sigma}_1 + \operatorname{tr}\boldsymbol{\Sigma}_2 - 2\sum_i\sqrt{\lambda_i(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)}$ | des écarts-types (pas des variances) en dimension 1 ; $W_2$ est la racine |
| biais (M27) | $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \frac{\operatorname{tr}\boldsymbol{\Sigma}_1}{n_1} + \frac{\operatorname{tr}\boldsymbol{\Sigma}_2}{n_2}$ | deux échantillons indépendants |
| Gram (M28) | $\lVert\mathbf{x} _i - \mathbf{x} _j\rVert^2 = G _{ii} + G  _{jj} - 2G _{ij}$ ; $\mathbf{G} = -\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$, $\mathbf{J} = \mathbf{I} - \frac1n\mathbf{1}\mathbf{1}^\top$ ; positions $\sqrt{\lambda_k}\thinspace\mathbf{q}_k$ | les points sont les lignes ; $\mathbf{D}^{(2)}$ contient des carrés ; la carte est centrée, à une isométrie près |
| grilles (M28) | variation totale $\mathbf{x}^\top\mathbf{L}\mathbf{x}$, gradient $2\mathbf{L}\mathbf{x}$ ; période $\frac{1}{\sqrt{f_1^2 + f_2^2}}$ ; gain d'une moyenne mobile de trois cases $\frac{1 + 2\cos\omega}{3}$ | $f$ en cycles par case, $\omega = 2\pi f$ ; Nyquist $\frac12$ |
| lois (M28) | $p_i^{(T)} \propto p_i^{1/T}$ ; $\mathbf{p}_S = \frac{\mathbf{p}\thinspace\mathbb{1}_S}{P(S)}$ ; $\mathrm{KL}(\mathbf{p}_S \thinspace\Vert\thinspace \mathbf{p}) = -\ln P(S)$, $\frac12\lVert\mathbf{p}_S - \mathbf{p}\rVert_1 = 1 - P(S)$ | $P(S)$ est la masse **gardée** ; $\mathbf{p}_S$ est la première loi |
| boucles (M28) | $u_{t+1} = f(u_t)$ sur $N$ éléments : $\mu + \lambda \le N$ | une itération **déterministe** |

## 5. Les faux amis de la partie

Des paires qui se ressemblent et qu'il faut savoir séparer, chacune avec la question qui les distingue :

| D'un côté | De l'autre | La question à se poser |
|---|---|---|
| la loi marginale d'un bloc (le sous-bloc de $\boldsymbol{\Sigma}$) | sa loi conditionnelle (le complément de Schur) | ai-je lu une autre coordonnée ? |
| la covariance du maximum de vraisemblance, $\frac{\mathbf{S}}{n}$ | la covariance empirique sans biais, $\frac{\mathbf{S}}{n - 1}$ | que demande-t-on : une vraisemblance maximale, ou une estimation sans biais ? |
| $\mathrm{KL}(q \thinspace\Vert\thinspace p)$, qui choisit un mode (bosses séparées) | $\mathrm{KL}(p \thinspace\Vert\thinspace q)$, qui couvre la masse (et apparie les moments pour une gaussienne $q$) | sous quelle loi l'espérance est-elle prise ? |
| la responsabilité $r_{ik}$, une probabilité | l'affectation dure, une décision | garde-t-on l'incertitude ou la tranche-t-on ? |
| la convention ligne, $\boldsymbol{\mu}\mathbf{P}$ | la convention colonne, $\mathbf{P}^\top\boldsymbol{\mu}^\top$ | la ligne $i$ de $\mathbf{P}$ donne-t-elle les suites de $i$ ? |
| une ligne de somme 1 | une ligne sous-stochastique, qui peut finir | où va la masse qui manque ? |
| la valeur d'une politique fixée, un système linéaire | la valeur optimale, avec un maximum | y a-t-il un choix à faire dans l'équation ? |
| le maximin, en stratégies pures | la valeur, en stratégies mixtes | y a-t-il un point selle ? |
| la descente-montée simultanée | la descente-montée alternée | le second joueur voit-il déjà le nouveau coup du premier ? |
| le top-k, que la température ne change pas | le top-p, qui rétrécit quand on refroidit | fixe-t-on un nombre d'issues, ou une masse ? |
| la matrice de Gram $\mathbf{X}\mathbf{X}^\top$ | la matrice $\mathbf{X}^\top\mathbf{X}$ | les objets comparés sont-ils les lignes ou les colonnes ? |
| les distances | leurs carrés, dans $\mathbf{D}^{(2)}$ | ai-je élevé au carré avant de centrer ? |
| la variation totale d'une grille | la distance en variation totale entre deux lois | parle-t-on de cases voisines, ou de deux lois ? |
| multiplier des probabilités par $\frac1T$ | les élever à la puissance $\frac1T$ | ai-je renormalisé une puissance ? |
| un tirage ancestral, des parents aux enfants | un posterior, des enfants observés vers les parents | va-t-on dans le sens du graphe, ou à rebours ? |

Le détail, chapitre par chapitre, est dans les sections « Les pièges classiques » des fiches et dans `annexes/erreurs_frequentes.md`.

## 6. Vers le checkpoint VI de workbookIA

Le checkpoint VI de workbookIA se fait juste après cet examen blanc. Ce qui t'y attend, dans les chapitres 25 à 29, sans en dévoiler les exercices :
- **ch. 25 (autoencodeurs et VAE)** : des tirages gaussiens et la norme d'un tirage en grande dimension (M25a §1 à §3) ; des log-densités gaussiennes diagonales, une KL entre gaussiennes et l'interpolation sphérique (M25a §7, §8) ; un espace latent, une ELBO écrite « reconstruction moins KL au prior », une inférence amortie, la dérivée d'une espérance par le chemin, une KL pondérée par $\beta$ (M25b §5, §7, §8).
- **ch. 26 (apprentissage par renforcement)** : des probabilités de transition et des politiques (M26 §1, §4), le retour actualisé et la valeur d'un état ou d'une action (M26 §4, §5), l'équation d'optimalité et son itération (M26 §6, §7), des estimations par échantillons, avec un pas et une erreur TD, et la surestimation due au maximum (M26 §8).
- **ch. 27 (réseaux antagonistes génératifs, GAN)** : un jeu à somme nulle et l'idée d'équilibre (M27 §1 à §4), des log-loss et Jensen-Shannon (M27 §5, §6), $W_1$ en dimension 1 et la distance de Fréchet, estimée sur des échantillons (M27 §8, §9).
- **ch. 28 (réseaux créatifs)** : la montée sur l'entrée (M28 §3), des matrices de Gram et une variation totale (M28 §1, §4), une température, un top-k ou un top-p pour générer, et ce qu'une génération gloutonne finit par faire (M28 §5, §6).
- **ch. 29 (datasets)** : pas de nouvel outil de la partie VI ; le décalage entre deux datasets s'y lit avec les probabilités de M02c et M03, et les mesures de dérive de M27 §10 serviront au bonus B7.

Le mini-projet VI de workbookIA assemble ces outils dans un modèle génératif. Ensuite, la partie VII de ce dépôt prépare les bonus de workbookIA, en commençant par MB2 (cooccurrences, PMI et embeddings), avant workbookIA B2.

## 7. À dire à voix haute

Dis chaque mot en français puis en anglais, puis la phrase de la dernière colonne, et invente ton propre exemple.

| Français | Anglais | À dire à voix haute |
|---|---|---|
| distance de Mahalanobis | Mahalanobis distance | « L'écart à la moyenne, mesuré à l'échelle de la covariance : une même distance de Mahalanobis, une même densité. » |
| complément de Schur | Schur complement | « Ce qui reste de la covariance d'un bloc quand on a lu l'autre. » |
| matrice de précision | precision matrix | « L'inverse de la covariance : ses zéros disent quelles coordonnées sont indépendantes sachant les autres. » |
| interpolation sphérique | spherical linear interpolation (slerp) | « Aller d'un vecteur à l'autre sur la sphère, en tournant à vitesse constante. » |
| variable latente, posterior | latent variable, posterior | « Ce qu'on ne voit pas, et ce qu'on en sait une fois la donnée lue. » |
| responsabilité | responsibility | « La probabilité qu'une mesure vienne de chaque composante, avec les paramètres du moment. » |
| borne inférieure de l'évidence | evidence lower bound (ELBO) | « Une borne de ln p(x), dont l'écart est une KL au posterior. » |
| posterior agrégé, effondrement | aggregated posterior, posterior collapse | « La moyenne des codes sur les données ; un code effondré ne dit plus rien de la donnée. » |
| loi stationnaire | stationary distribution | « La loi que la chaîne garde quand elle la possède ; vers laquelle elle converge si elle mélange bien. » |
| équation de Bellman | Bellman equation | « La valeur d'un état est sa récompense plus la valeur, actualisée, de ce qui suit. » |
| point selle, stratégie mixte | saddle point, mixed strategy | « Sans point selle, jouer au hasard, avec les bonnes probabilités, rend l'adversaire indifférent. » |
| couplage, plan de transport | coupling, transport plan | « Une loi jointe dont les marges sont les deux lois à comparer ; son coût minimal est une distance de Wasserstein. » |
| distance de Fréchet | Fréchet distance | « La distance de Wasserstein d'ordre 2 entre deux gaussiennes : deux moyennes, deux covariances. » |
| dérive | drift | « Une variable qui change de loi entre deux périodes ; je dis avec quelle mesure, et dans quelle unité. » |
| positionnement multidimensionnel | multidimensional scaling | « Des distances aux positions : double centrage, puis théorème spectral, à une isométrie près. » |
| montée projetée | projected gradient ascent | « Un pas de gradient, puis on ramène le point dans le domaine permis. » |
| fréquence spatiale, repliement | spatial frequency, aliasing | « Un motif plus rapide que deux cases par période se replie sur un motif plus lent. » |
| température, top-p | temperature, nucleus sampling | « Chauffer aplatit la loi ; le top-p garde les plus probables jusqu'à la masse demandée, et paie −ln P(S). » |
| prépériode, période | preperiod, cycle length | « Une suite déterministe sur un ensemble fini finit par revenir sur ses pas : une queue, puis un cycle. » |
