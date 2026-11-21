# Projet de synthèse · Les maths d'un algorithme, de A à Z

> La dernière brique de workbookMaths, environ **25 h** (la lecture de ce cahier des charges et de l'exemple comprise), sur **quatre semaines**, en même temps que le projet final de workbookIA. Tu choisis un algorithme de workbookIA et tu écris un **notebook-article** qui le dérive entièrement, démontre deux de ses propriétés, le calcule à la main sur un petit exemple, l'implémente avec **ta** librairie `mymath`, le vérifie contre une bibliothèque indépendante et illustre une propriété par une expérience. Puis tu le présentes en cinq minutes, comme en entretien. Il n'y a pas de solution de référence : c'est ton projet. Il y a une grille, des indices et un exemple rédigé sur un autre algorithme.

| | |
|---|---|
| **Algorithme** | un algorithme de workbookIA, choisi dans [la liste](#algorithmes) (ou hors liste, justifié dans le cadrage) |
| **Livrable** | ton dossier `mon_travail/projet_synthese/` : le cadrage, le notebook-article `synthese.ipynb` exécuté, le module `algo.py`, ses tests `test_algo.py` et ta grille remplie |
| **Méthode imposée** | une dérivation où chaque étape cite le résultat qui la justifie ; trois fonctions de `mymath` écrites par toi ; des tests contre un oracle indépendant ; une erreur introduite exprès que les tests attrapent |
| **Prérequis** | tout le parcours, en particulier les chapitres de maths de ton algorithme (colonne « Préparé par » de la liste) et le chapitre de workbookIA qui l'utilise |
| **Évaluation** | sur 20, avec [`GRILLE.md`](GRILLE.md) : auto-évaluation, puis correction par Claude sur demande ([La correction](#correction)) |
| **Durée** | 25 h, dont 60 min de lecture ; [les jalons](#jalons) sur quatre semaines |

**Par où commencer** : lis [le contexte](#contexte), [la liste](#algorithmes) et [les règles](#regles), installe le kit ([Démarrer](#demarrer)), puis fais PS.1. **Ce que tu rends** : ton dossier, avec le livrable de chaque étape (la ligne « Livrable » de chacune des [dix étapes](#etapes)). **Comment tu es noté** : [la grille](#grille), critère par critère, avec ses pénalités et ses seuils.

**Sommaire** : [Le contexte](#contexte) · [Les algorithmes](#algorithmes) · [Les règles](#regles) · [Les jalons](#jalons) · [Démarrer](#demarrer) · [Le kit](#kit) · [Les dix étapes](#etapes) · [La grille](#grille) · [La correction](#correction) · [Les questions d'entretien](#entretien) · [L'exemple](#exemple) · [Ce qu'on ne fait pas ici](#hors-champ)

<a id="contexte"></a>

## Le contexte

Tout au long des deux workbooks, tu as appris les outils (la règle de la chaîne, les gradients par rapport à une matrice, les valeurs propres, les espérances) et tu as vu les algorithmes s'en servir. Ce projet te demande de tenir le fil entier pour **un** algorithme : partir de ce qu'il cherche à faire, arriver aux formules exactes que le code calcule, démontrer ce qu'il garantit, et prouver que ton code est juste. C'est ce qu'on attend d'un data scientist ou d'un ML engineer en entretien technique : « dérive-moi le gradient », « pourquoi ça converge ? », « comment sais-tu que ton implémentation est juste ? ».

Le résultat est un **article** : un notebook qu'un relecteur lit seul, de haut en bas, et dont il peut vérifier chaque ligne. Un bon article de ce type montre à un recruteur trois choses que le projet final de workbookIA ne montre pas : tu sais **dériver** (sans « on voit que »), tu sais **implémenter** à partir de tes formules, et tu sais **vérifier** (des tests qui attrapent de vraies erreurs).

Les deux projets se font en même temps et se complètent : le projet final de workbookIA est un projet de bout en bout sur des données réelles ; celui-ci est un article de maths vérifié, sur des données synthétiques.

<a id="algorithmes"></a>

## Les algorithmes

Chaque ligne est un algorithme de workbookIA dont la dérivation tient sur plusieurs pages. « Préparé par » donne les chapitres de ce dépôt qui en enseignent les outils ; « `mymath` utile » propose des briques de ta librairie (`module.fonction`), parmi lesquelles tu en appelles au moins trois ; « Oracle conseillé » est la bibliothèque contre laquelle tu le vérifies.

| N° | Algorithme | workbookIA | Préparé par | `mymath` utile | Oracle conseillé | Difficulté |
|---|---|---|---|---|---|---|
| 1 | Régression logistique : log-loss, gradient, descente de gradient | ch. 13 | M13a, M05b, M17, M19 | `explog.sigmoid`, `likelihood.logistic_loss`, `likelihood.bernoulli_log_likelihood`, `approx.logsumexp`, `iterative.critical_step_size` | scikit-learn `LogisticRegression(penalty=None)` | ★★ |
| 2 | Ridge et lasso : forme fermée de ridge, lasso par descente de coordonnées et seuillage doux | ch. 9 | M09b, M10, M12b, M12c | `linreg.normal_equations`, `orthogonal.qr`, `orthogonal.least_squares_qr`, `eigen.cholesky`, `vectors.norm_p` | scikit-learn `Ridge`, `Lasso` (lis dans leur documentation la loss exacte qu'ils minimisent) | ★★ |
| 3 | ACP : axes principaux, projection, reconstruction, variance expliquée | ch. 12 | M12c, M12d, M02c | `eigen.power_iteration`, `eigen.rayleigh_quotient`, `svd_pca.svd`, `svd_pca.low_rank_approximation`, `svd_pca.explained_variance_ratio`, `orthogonal.project` | scikit-learn `PCA` (axes définis au signe près) | ★★ |
| 4 | k-means : l'algorithme de Lloyd et l'initialisation k-means++ | ch. 7 | M07, M02b | `vectors.centroid`, `vectors.sum_sq_distances_to`, `vectors.norm_p`, `distributions.inverse_transform_sample` | scikit-learn `KMeans` (mêmes centres de départ, `n_init=1`) | ★★ |
| 5 | Itération sur les valeurs et Q-learning tabulaire | ch. 26 | M26, M22 | `markov.bellman_linear_solve`, `markov.bellman_fixed_point_iterates`, `markov.stationary_distribution`, `recurrence.operator_norm` | `np.linalg.solve` (la valeur exacte d'une politique fixée) et l'énumération des politiques sur un petit problème | ★★ |
| 6 | Rétropropagation d'un MLP : une couche cachée, softmax et cross-entropy | ch. 16 à 18 | M16, M17, M18, M05a | `explog.sigmoid`, `explog.tanh`, `approx.logsumexp`, `affine.variance_of_product`, `tensors.moments_along_axes` | PyTorch (autograd) ou SymPy, et des différences finies | ★★★ |
| 7 | Momentum et Adam | ch. 19 | M19, R5, M12c | `sequences.exponential_moving_average`, `iterative.critical_step_size`, `iterative.linear_recurrence`, `eigen.power_iteration` | `torch.optim.SGD(momentum=…)`, `torch.optim.Adam` (mêmes conventions) | ★★★ |
| 8 | Convolution 2D et sa rétropropagation | ch. 21 | M21, M18 | `convolution.convolve`, `convolution.toeplitz_matrix`, `convolution.separable_factors`, `convolution.equivalent_kernel` | `scipy.signal.correlate2d`, `torch.nn.functional.conv2d` | ★★★ |
| 9 | VAE gaussien : ELBO, KL en forme fermée, reparamétrisation | ch. 25 | M25a, M25b | `gaussian.mvn_logpdf`, `gaussian.sample_mvn`, `approx.logsumexp`, `explog.sigmoid` | SciPy (`scipy.stats`, `scipy.integrate`), Monte-Carlo, PyTorch (autograd) | ★★★ |
| 10 | Attention par produit scalaire : masque, multi-têtes, RoPE | B3 | MB3, M17 | `positional.givens_rotation`, `positional.online_softmax`, `positional.merge_softmax_states`, `approx.logsumexp` | `torch.nn.functional.scaled_dot_product_attention` | ★★★ |
| 11 | Skip-gram à échantillonnage négatif, ou PPMI et SVD | B2 | MB2, M12d | `cooccurrence.pmi`, `svd_pca.svd`, `svd_pca.low_rank_approximation`, `vectors.cosine_similarity`, `explog.sigmoid` | scikit-learn `TruncatedSVD`, PyTorch (autograd) | ★★★ |
| 12 | DDPM : processus direct, posterior gaussien, loss de prédiction du bruit | B5 | MB5, M25a | `gaussian_paths.linear_gaussian_recursion`, `gaussian.condition_gaussian`, `gaussian.mvn_logpdf`, `gaussian.sample_mvn` | SciPy (`scipy.stats`), Monte-Carlo | ★★★ |
| 13 | REINFORCE avec baseline | B8 | MB8, M26 | `policy_gradient.score_function_gradient`, `policy_gradient.importance_weights`, `markov.bellman_linear_solve`, `approx.logsumexp` | des différences finies sur une valeur exacte (`np.linalg.solve`), Monte-Carlo | ★★★ |
| 14 | Batchnorm : passe avant et gradient, dans une petite couche | ch. 20 | M20, M18 | `tensors.moments_along_axes`, `explog.tanh`, `approx.logsumexp`, `affine.variance_of_product` | `torch.nn.BatchNorm1d` (mode entraînement) et autograd | ★★★★ |
| 15 | RNN et rétropropagation dans le temps | ch. 22 | M22, M17, M18 | `recurrence.linear_system_states`, `recurrence.product_norms`, `recurrence.operator_norm`, `explog.tanh`, `approx.logsumexp` | `torch.nn.RNN` et autograd | ★★★★ |

**Un autre algorithme de workbookIA** est accepté si sa dérivation tient sur au moins une page et s'il a un oracle indépendant : ton cadrage le justifie. **Ne sont pas acceptés** : la régression de Poisson (c'est [l'exemple](#exemple)) ; un algorithme sans dérivation (un arbre de décision seul, le vote d'un ensemble). La méthode de Newton appliquée à la régression logistique suit le schéma de l'exemple : elle n'est permise qu'en complément de la descente de gradient (dans l'expérience, par exemple), pas comme algorithme principal.

**Les fonctions de `mymath` qui comptent** (PS.6) sont des briques du calcul : une sigmoïde, un log-sum-exp, une factorisation, un pas critique, une loi stationnaire. Ne comptent pas : une fonction qui fait tout l'algorithme à ta place (`linreg.solve_least_squares` avec `ridge` n'est pas ton ridge, `svd_pca.principal_axes` n'est pas ton ACP), ni une dérivée numérique (`jacobian.numerical_jacobian`, `iterative.numerical_hessian`, `multivar.partial_derivative`) qui remplacerait une formule de ta dérivation.

<a id="regles"></a>

## Les règles

1. **La dérivation est la tienne.** Tu as fait (ou tu feras) dans workbookIA les démonstrations qui dérivent ces algorithmes (∂ 7.7, 9.2, 9.3, 9.6, 12.8, 13.8, 17.7, 18.6 à 18.8, 19.7, 19.8, 20.8, 21.7, 22.6, 22.7, 25.5, 25.7, 26.7, 26.8, B2.7, B3.6, B3.7, B5.6, B5.7, B8.7). Ici, tu les reprends entièrement, avec tes mots, plus complètes (formes, conventions, cas limites), et ce dépôt ne les donne nulle part : ni ce cahier des charges, ni la grille, ni les indices, ni l'exemple. Si tu t'appuies sur un corrigé, un livre ou une page web, cite-le à l'endroit où il sert. Un passage recopié ou paraphrasé de près sans être cité coûte 3 points.
2. **MML** se cite par sections (« MML §5.5 »), jamais par pages, et ne se recopie pas.
3. **Le module** (`algo.py`) n'importe que NumPy, la bibliothèque standard et `mymath`. Il appelle au moins trois fonctions de `mymath` **écrites par toi** : leurs modules sont dans `mon_travail/mymath/` (pas un repli sur la référence) et leurs tests passent avec ton code. Si tu as sauté un chapitre, écris d'abord ses fonctions.
4. **Les oracles** : NumPy, SciPy, SymPy, scikit-learn, et PyTorch, que tu as installé pour workbookIA et que Colab fournit (ce dépôt, lui, ne l'importe jamais). Jamais une autre fonction de ton module ni de `mymath`, ni une formule de ta dérivation recopiée dans un test : un test qui compare ton code à lui-même ne peut pas échouer. Ces bibliothèques servent dans `test_algo.py`, dans §4 et dans l'expérience, jamais dans `algo.py`.
5. **Les données** sont synthétiques, tirées avec une graine, assez petites pour que « Run all » tienne en **moins de 5 minutes** sur CPU (aucune cellule de plus d'une minute).
6. **L'aide reçue** (une relecture, un forum, un assistant comme Claude) se dit dans les références. Ce que tu rends reste ta dérivation et ton code : tu dois pouvoir en refaire chaque ligne au tableau.

<a id="jalons"></a>

## Les jalons (quatre semaines)

Ils suivent ceux du projet final de workbookIA, une demi-journée environ par semaine en plus de lui. Choisis de préférence l'algorithme du modèle ou de la baseline de ton projet final (une régression logistique, un CNN, un LSTM…) : les deux projets s'éclairent l'un l'autre, sans que ce soit une obligation.

| Semaine | Étapes | À la fin de la semaine | ⏱️ |
|---|---|---|---|
| 1 | lecture, PS.1, PS.2, début de PS.3 | `cadrage.md` (relu après l'exemple), §2 de l'article, les premières étapes de la dérivation | 6 h |
| 2 | fin de PS.3, PS.4, PS.5 | la dérivation complète, les deux propriétés et le cas limite, l'exemple à la main | 7 h |
| 3 | PS.6, PS.7 | `algo.py`, `test_algo.py` vert, la mutation attrapée | 6 h 30 |
| 4 | PS.8, PS.9, PS.E1 | l'expérience, l'article relu et exécuté, la répétition chronométrée, `grille.md` remplie | 5 h 30 |

Le jalon qui compte le plus est la dérivation de la semaine 2 : l'implémentation et les tests en partent. Si une étape de la dérivation résiste, écris le code d'abord sur un petit exemple, vérifie-le par différences finies, puis reviens à la dérivation : le chiffre juste te dit ce que la formule doit donner.

<a id="demarrer"></a>

## Démarrer

```bash
python tools/start_chapter.py PS
```

copie le kit dans `mon_travail/projet_synthese/`, sans jamais écraser un fichier existant (relance la commande après une mise à jour du dépôt : seuls les fichiers manquants arrivent). C'est dans ce dossier que tu travailles ; les fichiers de `projets/projet_synthese/` sont mis à jour par Claude.

1. **Ta librairie** : le projet appelle tes fonctions de `mymath`, dans `mon_travail/mymath/`. Vérifie les modules dont tu as besoin : `python -m pytest -q tests/test_<chapitre>_<module>.py` (par exemple `tests/test_m12c_eigen.py`).
2. **Le notebook** : ouvre `mon_travail/projet_synthese/synthese.ipynb` (sur Colab, depuis ton Drive : `workbookMaths/mon_travail/projet_synthese/`) et lance « Run all » : il va au bout, avec des ⏳ partout où ton travail manque.
3. **Les tests** : depuis le dossier du dépôt, `python -m pytest -q mon_travail/projet_synthese/test_algo.py` ; ils sont sautés avec ⏳ tant que leurs squelettes ne sont pas écrits. Avec `--impl=ref`, ton module tourne sur la `mymath` de référence : utile pour savoir si un bug vient de ton module ou de ta librairie, jamais pour le rendu.
4. **Le cadrage** : remplis `cadrage.md` (PS.1), puis lis [l'exemple](#exemple), puis reprends ton cadrage.

<a id="kit"></a>

## Le kit

| Fichier | Contenu | Étapes |
|---|---|---|
| `cadrage.md` | le modèle du cadrage (une page) | PS.1 |
| `synthese.ipynb` | le modèle du notebook-article : une section par étape, ce qu'il faut y écrire, les cellules qui vérifient ton travail (« cas limite », « vérification de l'exemple », « Contrôle du module », tests et « mutation », « expérience », la durée de « Run all ») | PS.2 à PS.9, PS.E1 |
| `algo.py` | le module de ton algorithme : un en-tête qui rappelle les règles, une fonction exemple (le modèle d'une docstring et d'un contrôle d'entrée) | PS.6 |
| `test_algo.py` | les squelettes de tes tests (oracle sur des cas tirés au hasard, différences finies, propriété, exemple à la main, entrée invalide), sautés avec ⏳ tant qu'ils ne sont pas écrits ; `assert_close`, dont le message dit d'abord ce qui était attendu | PS.7 |
| `mutants.py` | tes erreurs introduites exprès : une copie fautive d'une fonction de `algo.py`, sous le même nom | PS.7 |
| `conftest.py` | ce que pytest fournit à tes tests : les fixtures `algo` et `mymath`, `--impl {learner,ref,stubs}`, `--mutant=<nom>`, le ⏳ des fonctions pas encore écrites | PS.7 |
| `grille.md` | ta copie de la grille, pour l'auto-évaluation (cases et colonne « Preuve ») | toutes |
| `README.md` | le mode d'emploi du kit | |

<a id="etapes"></a>

## Les dix étapes

Les étapes suivent les quatre parties du projet : §1 Choisir et cadrer (PS.1), §2 Dériver (PS.2 à PS.5), §3 Implémenter et vérifier (PS.5 à PS.8), §4 Rédiger et présenter (PS.9, PS.E1). Dans les livrables, « §n de l'article » désigne une section de ton notebook `synthese.ipynb`. Les critères détaillés, case par case, sont dans [`GRILLE.md`](GRILLE.md) ; les indices dans [`04_indices.md`](04_indices.md).

### PS.1 — Cadrer : l'algorithme choisi, ce qu'il calcule, ses entrées et sorties, les notions de maths et leurs chapitres, l'oracle de la vérification et le plan de l'article 🗣️ ★★ ⏱️ 60 min
**Objectif :** dire en une page ce que tu vas dériver, avec quels outils, et comment tu sauras que ton code est juste.
**Prérequis :** la liste ci-dessus · le chapitre de workbookIA de ton algorithme · **Points :** 1

**Chapitres mobilisés** : [`annexes/correspondances.md`](../../annexes/correspondances.md) (§1 : pour chaque chapitre de workbookIA, les chapitres de maths qui le préparent ; §2 : pour chaque section de MML, le chapitre qui la couvre) ; la section « Et maintenant » de la fiche de chacun des chapitres de la colonne « Préparé par » ; [`docs/syllabus/COUVERTURE_IA.md`](../../docs/syllabus/COUVERTURE_IA.md) (chaque notion mathématique de workbookIA et le chapitre qui l'enseigne).

**Livrable** : `cadrage.md`.

**Critères de réussite**
- une page au plus : l'algorithme et sa ligne de la liste (ou, hors liste, pourquoi il convient), ce qu'il calcule, ses entrées et ses sorties avec leurs formes ;
- les notions de maths de la dérivation, chacune avec son chapitre et sa section dans ce dépôt, et sa section de MML s'il y en a une ;
- l'oracle : la bibliothèque, la fonction, les réglages qui la rendent comparable, et ce qu'elle ne vérifie pas ;
- le plan de l'article, avec les deux propriétés visées, le cas limite pressenti et l'expérience visée.

**Erreurs à éviter** : un algorithme trop gros pour 25 h (un Transformer entier : prends l'attention) ; un oracle qui ne calcule pas la même chose que toi (une régularisation par défaut, une autre normalisation de la loss, une autre initialisation) ; un plan sans propriétés ; lire l'exemple avant d'avoir écrit une première version.

### PS.2 — Poser le problème : données, paramètres et leurs formes, objectif, hypothèses, tableau des notations et conventions ✏️ ★★ ⏱️ 90 min
**Objectif :** fixer, avant tout calcul, chaque objet de l'article, sa forme et ce qu'on suppose de lui.
**Prérequis :** PS.1 · **Points :** 1,5

**Chapitres mobilisés** : M09a (formes et produits de matrices, $\mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}$) ; M16 §1 (applications affines : formes et conventions) ; M17 §4 (gradient en ligne ou de la forme de la variable) ; M20 §1 (tableaux à $k$ dimensions et axes) ; [`annexes/symboles.md`](../../annexes/symboles.md) et [`annexes/formulaire.md`](../../annexes/formulaire.md) (les notations du dépôt). MML §5.2 et §5.3 (les conventions du livre, différentes des nôtres pour le gradient).

**Livrable** : §2 de l'article (« Le problème »).

**Critères de réussite**
- ce qu'est un exemple, ce que sont les paramètres et ce que l'algorithme calcule ou minimise, en une phrase puis en une formule ;
- le tableau des notations : chaque symbole, son sens, sa forme et son domaine ;
- les hypothèses, numérotées, pour être citées plus loin ;
- les conventions annoncées (vecteurs lignes ou colonnes, forme du gradient, somme ou moyenne sur les exemples) ;
- les notations du dépôt, ou chaque écart signalé.

**Erreurs à éviter** : des symboles introduits en cours de route ; une même lettre pour deux objets ; des formes oubliées ; une somme qui devient une moyenne d'une ligne à l'autre ; des hypothèses implicites (« les données sont bonnes »).

### PS.3 — La dérivation complète, de l'objectif aux formules que le code calcule : chaque étape justifiée par un résultat cité, chaque forme vérifiée ∂ ★★★★ ⏱️ 270 min
**Objectif :** aller de l'objectif de §2 aux formules exactes de ton code, sans qu'aucune ligne demande au lecteur de te croire.
**Prérequis :** PS.2 · **Points :** 4

**Chapitres mobilisés** : R7 §5 à §7 (dérivées usuelles, règles, composée) ; M05b §3 (gradient) ; M09b §2 (les gradients de $\mathbf{a}^\top\mathbf{w}$ et $\mathbf{w}^\top\mathbf{A}\mathbf{w}$) ; M17 §1 à §4 (jacobienne, jacobienne diagonale, règle de la chaîne, convention) ; M18 §2, §4, §6 à §8 (somme sur les chemins, mode inverse, gradients par rapport à une matrice, identités, gradient d'une moyenne et vérification) ; M19 §1 (hessienne) ; et les chapitres de ton algorithme (colonne « Préparé par »). MML §5.2 à §5.6.

**Livrable** : §3 de l'article (« La dérivation »).

**Critères de réussite**
- de l'objectif de §2 jusqu'aux formules exactes que le code calcule : chaque formule finale numérotée, et la docstring de la fonction qui la calcule cite ce numéro ;
- chaque étape cite le résultat qui la justifie (chapitre et section de ce dépôt, ou section de MML), et ce résultat dit bien ce qui est utilisé ;
- la forme de chaque objet écrite, chaque produit vérifié ;
- la convention de §2 tenue partout ;
- aucune étape sautée, aucune phrase qui remplace un calcul ;
- les points délicats du domaine (division par zéro, logarithme de 0, point non dérivable, matrice non inversible) dits et réglés.

**Erreurs à éviter** : sauter de l'objectif à la formule finale ; dériver « comme dans le cas scalaire » sans vérifier l'ordre des facteurs d'un produit de matrices ; changer de convention en route ; une formule finale qui n'est pas celle que le code calcule (un facteur, une moyenne, une transposée) ; citer un chapitre entier au lieu de la section qui sert.

### PS.4 — Deux propriétés démontrées avec leurs hypothèses (convexité, unicité, invariance, espérance, borne, coût), et un cas où une hypothèse tombe ∂ ★★★ ⏱️ 180 min
**Objectif :** dire ce que l'algorithme garantit, sous quelles hypothèses, et montrer ce qui casse quand l'une d'elles manque.
**Prérequis :** PS.3 · **Points :** 2,5

**Chapitres mobilisés** : R4 §6 à §8 (raisonnements, récurrence, rédiger une démonstration courte) ; M05a §1 (convexité en une variable) ; M10 §1 (ensembles convexes) ; M12c §6 et §7 (théorème spectral, quotient de Rayleigh, matrices définies positives, hessienne et convexité) ; M19 §2 à §5 (points critiques, itérations linéaires, pas critique, conditionnement) ; M22 §3 et §4 (rayon spectral, normes de matrices) ; M02c §4 et §6 (loi des grands nombres, biais et variance d'un estimateur) ; M18 §5 (le coût de chaque mode). MML §7.1 et §7.3.

**Livrable** : §4 de l'article (« Deux propriétés et un cas limite »), avec sa cellule « cas limite » exécutée.

**Critères de réussite**
- pour chacune des deux propriétés : un énoncé complet (les hypothèses de §2 citées, la conclusion) et une démonstration rédigée où chaque hypothèse sert ;
- des propriétés de l'algorithme, pas d'un outil seul, et ce que chacune garantit en pratique ;
- le cas où une hypothèse tombe, montré par un contre-exemple chiffré ou une expérience, calculé dans la cellule « cas limite » ;
- chaque propriété aussi vérifiée numériquement (un test de propriété de PS.7 ou l'expérience de PS.8), avec le renvoi.

**Erreurs à éviter** : démontrer sur un exemple ; un énoncé sans hypothèses ; une hypothèse jamais utilisée (elle est inutile, ou une étape manque) ; un contre-exemple qui ne viole pas l'hypothèse annoncée ; confondre « converge » et « converge vers le bon point ».

### PS.5 — Un exemple à la main en dimension 2 ou 3 (en fractions quand c'est possible), retrouvé par le code ✏️ ★★★ ⏱️ 120 min
**Objectif :** dérouler tes formules une fois, à la main, sur un exemple assez petit pour que chaque nombre se vérifie, puis le retrouver par ton code.
**Prérequis :** PS.3 · **Points :** 1,5

**Chapitres mobilisés** : R1 §3 (fractions) ; M09a (calcul matriciel à la main) ; R0 §4 (vérifier un calcul avec SymPy) ; M05a §6 (nombres flottants et erreurs d'arrondi : quelle tolérance) et 🛠️ M05a.28 (erreur relative ou absolue).

**Livrable** : §5 de l'article (« Un exemple à la main »), avec sa cellule « vérification de l'exemple » exécutée (conseillé : le même exemple dans `test_algo.py::test_hand_example`, qui le garde vrai quand le code change).

**Critères de réussite**
- un exemple en petite dimension, dont toutes les données sont écrites ;
- le calcul complet, étape par étape, avec les formules de §3 citées par leur numéro, en fractions exactes quand c'est possible ;
- la cellule de vérification retrouve ton résultat par le module, à une tolérance écrite et justifiée ;
- un contrôle de vraisemblance annoncé avant le calcul.

**Erreurs à éviter** : un exemple trop grand pour être fait à la main ; ne garder que le résultat final ; arrondir en cours de route ; un exemple si symétrique qu'une transposée oubliée ne change rien (prends des nombres tous différents et une matrice qui n'est pas symétrique).

### PS.6 — L'implémentation : un module documenté (contrat, formes, erreurs) qui appelle au moins trois fonctions de ta librairie `mymath`, sans bibliothèque de ML 🛠️ ★★★★ ⏱️ 210 min
**Objectif :** traduire tes formules en un module qu'on lit à côté de l'article, construit sur ta propre librairie.
**Prérequis :** PS.3 · **Points :** 3

**Chapitres mobilisés** : R0 §7 (ta librairie `mymath` et ses tests) ; 🛠️ R1.31 (une docstring au format NumPy) et 🛠️ M02b.26 (docstring et exemples testés) ; M05a §8 (overflow, underflow et log-sum-exp) ; M20 §2 et §3 (réductions et diffusion le long d'axes, `einsum`) ; M18 §5 (le coût d'un calcul) ; les modules de `mymath` de ton algorithme (colonne « `mymath` utile »). [`annexes/cheatsheets/numpy.md`](../../annexes/cheatsheets/numpy.md).

**Livrable** : `algo.py` ; §6 de l'article (« L'implémentation »), avec la cellule « Contrôle du module » et les tests de tes modules de `mymath` exécutés.

**Critères de réussite**
- chaque fonction publique a une docstring en anglais : ce qu'elle calcule et son équation de §3, ses paramètres et leurs formes, ce qu'elle rend, les erreurs qu'elle lève ;
- au moins trois fonctions de `mymath` appelées, chacune utile au calcul ;
- ces trois fonctions sont les tiennes : modules dans `mon_travail/mymath/`, tests verts avec ton code ;
- NumPy, la bibliothèque standard et `mymath` seulement ;
- une entrée invalide lève l'erreur annoncée, avec un message qui dit ce qui était attendu ;
- un code qui se lit à côté des équations, sans boucle Python sur les exemples ou les coordonnées quand NumPy le fait.

**Erreurs à éviter** : un appel à `mymath` décoratif, dont le résultat ne sert pas ; un module de `mymath` absent, que la référence remplace sans que tu le voies (la cellule « Contrôle du module » le marque « référence ») ; des noms de variables qui ne sont pas ceux des équations ; une docstring sans formes ; un calcul instable qu'un log-sum-exp ou une factorisation éviteraient.

### PS.7 — La vérification : des tests contre une bibliothèque indépendante sur des cas tirés au hasard, les dérivées contre des différences finies, une propriété, et une erreur introduite exprès que les tests attrapent 📦 ★★★★ ⏱️ 180 min
**Objectif :** prouver que ton code calcule ce que l'article dit, par des tests qui attraperaient une vraie erreur.
**Prérequis :** PS.6 · **Points :** 3

**Chapitres mobilisés** : 🛠️ R2.28 (un test pytest) ; 🛠️ R7.25 (tester une dérivée avec pytest et SymPy) ; M05a §5 et §7 (différences finies : l'erreur par Taylor, le choix du pas) ; 🛠️ M02c.27 (tester une fonction aléatoire : une tolérance en erreurs types) ; 🛠️ M09a.35 (un test de propriété) ; M18 §8 (vérifier un gradient matriciel le long d'une direction). MML §5.1.

**Livrable** : `test_algo.py` et `mutants.py` ; §7 de l'article (« La vérification »), avec les cellules des tests et de la mutation exécutées.

**Critères de réussite**
- l'algorithme comparé à un oracle sur des cas tirés au hasard : au moins trois tailles et trois graines, en tests paramétrés aux noms lisibles ;
- un oracle indépendant de ton code, ses réglages écrits et justifiés ;
- les dérivées que le code calcule contre des différences finies centrées, le pas et la tolérance justifiés (sans dérivée dans le code : une condition d'optimalité de la dérivation, ou un second oracle exact) ;
- un test de propriété sur des cas tirés au hasard ;
- une mutation plausible dans `mutants.py`, que les tests attrapent, montrée dans §7 ;
- des messages d'échec qui disent d'abord ce qui était attendu ; tout passe, rien n'est sauté.

**Erreurs à éviter** : un test qui compare le code à lui-même ; une tolérance si large qu'elle passe toujours, ou si serrée qu'elle échoue sur des arrondis ; un pas de différences finies trop petit (l'arrondi domine) ou trop grand (la troncature domine) ; une seule graine ; un oracle mal réglé dont on a « corrigé » l'écart en élargissant la tolérance ; une mutation que rien n'attrape, gardée telle quelle (ajoute le test qui manque).

### PS.8 — Une expérience numérique qui illustre une propriété démontrée (convergence, conditionnement, stabilité, effet d'un hyperparamètre) : une figure légendée et sa conclusion 🔬 ★★★ ⏱️ 150 min
**Objectif :** voir une propriété de l'article sur une figure, après avoir prédit ce qu'elle montrerait.
**Prérequis :** PS.6 · **Points :** 1,5

**Chapitres mobilisés** : M19 §3 à §5 (convergence d'une itération, pas critique, conditionnement) ; M05a §7 (troncature contre arrondi) ; M22 §3 (rayon spectral et croissance transitoire) ; M02c §5 et §7 (variabilité d'une moyenne, intervalles) ; [`annexes/cheatsheets/matplotlib.md`](../../annexes/cheatsheets/matplotlib.md). MML §7.1.

**Livrable** : §8 de l'article (« L'expérience »), avec sa figure dans `figures/`.

**Critères de réussite**
- la question et la prédiction écrites avant l'exécution, reliées à une propriété de §4 ou à la dérivation ;
- une figure lisible (axes nommés avec leurs unités, légende, titre, échelle adaptée), enregistrée dans `figures/` ;
- une conclusion qui dit si la prédiction tient, avec la valeur lue, et ce qui expliquerait un écart ; plusieurs graines quand le hasard intervient.

**Erreurs à éviter** : une prédiction écrite après coup ; une échelle linéaire pour une erreur qui décroît exponentiellement ; conclure sur une seule graine ; une expérience trop longue pour le budget de 5 minutes (réduis les tailles, garde le phénomène).

### PS.9 — Rédiger l'article : introduction, plan, conclusion et limites, références par sections, LaTeX propre, notebook exécuté de bout en bout en moins de 5 minutes 🛠️ ★★★ ⏱️ 120 min
**Objectif :** livrer un article qu'un relecteur lit seul, et qu'il peut réexécuter.
**Prérequis :** PS.8 · **Points :** 1

**Chapitres mobilisés** : R0 §5 (écrire une formule en LaTeX) ; R4 §8 et 🛠️ R4.25 (rédiger une démonstration propre en LaTeX) ; [`annexes/symboles.md`](../../annexes/symboles.md).

**Livrable** : `synthese.ipynb` en entier (résumé, §1, §9, références), exécuté, sorties conservées.

**Critères de réussite**
- un article qui se lit seul : résumé, introduction qui dit ce qu'on dérive et pourquoi, plan, conclusion, limites ;
- des références par sections, rassemblées en fin d'article ; toute source qui a inspiré un passage citée ;
- un LaTeX propre, qui s'affiche sur GitHub et sur Colab ;
- « Run all » en moins de 5 minutes sur CPU, aucune cellule de plus d'une minute, sorties conservées.

**Erreurs à éviter** : un article qu'on ne comprend qu'en ayant lu le cadrage ; des cellules qui ne marchent que dans un certain ordre ; des sorties effacées avant le rendu ; des blocs 📝 du modèle restés en place.

### PS.E1 — Présenter l'algorithme en cinq minutes, puis répondre à cinq questions d'entretien sur ses maths 💼 ★★★ ⏱️ 60 min
**Objectif :** expliquer ton algorithme et ses maths comme en entretien technique, en cinq minutes, puis tenir les questions.
**Prérequis :** PS.9 · **Points :** 1

**Chapitres mobilisés** : les exercices 💼 et 🗣️ des chapitres de ton algorithme ; [la banque de questions](#entretien) ci-dessous.

**Livrable** : l'annexe « La présentation » de l'article.

**Critères de réussite**
- le plan des cinq minutes, avec la durée de chaque partie ;
- la durée mesurée d'une répétition (entre 4 et 6 minutes) ;
- cinq questions et tes réponses écrites, de quelques lignes, qui renvoient à l'article et disent « je ne sais pas » avec la façon de le vérifier quand c'est le cas.

**Erreurs à éviter** : dérouler tous les calculs ; lire ses notes ; dépasser le temps ; esquiver une question au lieu de dire ce que tu sais, ce que tu ne sais pas, et comment tu le vérifierais.

<a id="grille"></a>

## La grille (sur 20)

| Étape | Points |
|---|---|
| PS.1 Cadrer | 1 |
| PS.2 Poser le problème | 1,5 |
| PS.3 La dérivation complète | 4 |
| PS.4 Deux propriétés et un cas limite | 2,5 |
| PS.5 Un exemple à la main | 1,5 |
| PS.6 L'implémentation avec `mymath` | 3 |
| PS.7 La vérification contre une bibliothèque | 3 |
| PS.8 Une expérience numérique | 1,5 |
| PS.9 Rédiger l'article | 1 |
| PS.E1 Présenter | 1 |
| **Total** | **20** |

**Pénalités** : un passage recopié ou paraphrasé de près sans être cité (un corrigé de workbookIA ou de ce dépôt, MML, un livre, un article, une page web) (**−3**) ; un notebook livré qui ne s'exécute pas de bout en bout (**−2**).

**Seuils** : **14/20 ou plus**, l'article est présentable (portfolio, entretien) ; **moins de 10/20**, reprends les étapes que signale la correction.

Le détail, critère par critère, avec la façon de vérifier chacun et une colonne de preuve à remplir : [`GRILLE.md`](GRILLE.md) (ta copie est `grille.md` dans ton dossier).

<a id="correction"></a>

## La correction

1. **L'auto-évaluation** : remplis `mon_travail/projet_synthese/grille.md`, une case par critère, et la colonne « Preuve » (la section et l'équation, le test, la sortie de cellule, le fichier). Un critère sans preuve ne compte pas. Fais toi-même les « vérifications communes » du haut de la grille.
2. **La correction par Claude**, sur demande : il lit ton dossier sans jamais y écrire, refait les vérifications de la grille sur une copie et note chaque critère. Copie ce prompt dans une session de Claude ouverte sur le dépôt :

```text
Tu corriges mon projet de synthèse de workbookMaths. Lis projets/projet_synthese/README.md et
projets/projet_synthese/GRILLE.md, puis mon dossier mon_travail/projet_synthese/ (cadrage.md, synthese.ipynb et
ses sorties, algo.py, test_algo.py, mutants.py, grille.md) et ma librairie mon_travail/mymath/.
1. N'écris rien dans mon_travail/ : fais les « vérifications communes » de GRILLE.md sur une copie (/tmp/ps_copie),
   avec PYTHONDONTWRITEBYTECODE=1 et WBM_ROOT égal au dossier du dépôt.
2. Note critère par critère avec GRILLE.md, preuve par preuve : pour chaque critère, la preuve que tu as vérifiée
   (section, équation, cellule, test, commande et sa sortie) et les points (tous, la moitié ou zéro). Un critère
   sans preuve vérifiable vaut zéro, même coché dans ma grille.
3. Pour PS.3 et PS.4, relis chaque étape des démonstrations, pas seulement la formule finale. Montre-moi l'étape
   fausse ou sautée et la règle qui manque (chapitre et section du dépôt), sans écrire la dérivation à ma place.
4. N'applique une pénalité que si la vérification de sa ligne la montre.
5. Rends un tableau étape par étape (points obtenus sur points possibles), les pénalités, la note sur 20, le seuil
   atteint, et pour chaque étape sous la moitié de ses points, ce qu'il faut reprendre, dans l'ordre.
```

3. **La présentation simulée** : demande à quelqu'un (ou à Claude) de te poser cinq questions de la banque ci-dessous, sans tes notes, après tes cinq minutes.

Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`, puis coche PS dans ton tableau de bord.

<a id="entretien"></a>

## Les questions d'entretien

Une banque générique, sans réponses : choisis-en cinq pour PS.E1 (ou écris les tiennes), et réponds avec ton algorithme, en renvoyant à ton article.

- Pourquoi cette loss, ou cet objectif, et pas un autre ? Que suppose-t-il sur les données ?
- D'où vient chaque terme de ta formule finale ? Que se passe-t-il si l'on en oublie un ?
- Quelle est la forme de chaque objet de ton calcul ? Où une transposée se glisse-t-elle le plus facilement ?
- Que se passe-t-il si une hypothèse tombe : des features colinéaires, un groupe vide, une variance nulle, un pas trop grand ?
- Le problème est-il convexe ? Que garantit la réponse, et que ne garantit-elle pas ?
- Ton algorithme converge-t-il ? Vers quoi, à quelle vitesse, et qu'est-ce qui règle cette vitesse ?
- Quel est le coût en temps et en mémoire, en fonction de $n$, de $p$ et du nombre d'itérations ? Où est le goulot ?
- Que change une mise à l'échelle des features, ou des données ?
- Comment se comporte l'algorithme avec très peu d'exemples, ou en grande dimension ?
- Comment sais-tu que ton implémentation est juste ? Que vérifient tes tests, et que ne vérifient-ils pas ?
- Pourquoi des différences finies centrées ? Comment as-tu choisi le pas et la tolérance ?
- Quelle erreur as-tu introduite exprès, et quel test l'a attrapée ? Quelle erreur tes tests laisseraient-ils passer ?
- Où ton calcul risque-t-il un overflow ou un underflow, et comment l'évites-tu ?
- Que fait la bibliothèque de ton oracle de plus que ton code (stabilité, cas limites, vitesse) ?
- Qu'est-ce qui est aléatoire dans ton expérience, et combien de graines faut-il pour conclure ?
- Si tu ne devais garder qu'une équation de ton article, laquelle, et pourquoi ?
- Explique ta dérivation à quelqu'un qui connaît la règle de la chaîne mais pas cet algorithme.

<a id="exemple"></a>

## L'exemple

Le dossier [`exemple/`](exemple/) contient un projet rédigé de bout en bout sur un algorithme qui n'est ni dans la liste ni dans workbookIA : **la régression de Poisson ajustée par la méthode de Newton** (moindres carrés repondérés), sur des données synthétiques, vérifiée contre scikit-learn et SciPy. Il a son cadrage, son article exécuté, son module, ses tests et sa grille remplie, avec une preuve par critère. **Ce n'est pas une solution** et ce n'est pas un modèle à recopier : il montre le niveau de détail attendu. Lis-le **après** une première version de ton cadrage, pas avant ; [`exemple/README.md`](exemple/README.md) dit quoi y regarder. L'exemple n'est jamais copié dans ton dossier.

<a id="hors-champ"></a>

## Ce qu'on ne fait pas ici

- **Pas de dataset réel**, pas de test scellé, pas de paquet installable, pas d'intégration continue, pas d'API : c'est le projet final de workbookIA, que tu fais en même temps. Ici, des données synthétiques suffisent : elles ont l'avantage de connaître la bonne réponse.
- **Pas de modèle entraîné à grande échelle** : tout tient en 5 minutes de CPU. Un petit exemple bien vérifié vaut plus qu'un grand qu'on ne peut pas contrôler.
- **Pas de bibliothèque de ML dans le module** : scikit-learn et PyTorch sont des oracles, dans les tests.
- **Pas de solution de référence** : la grille, les indices et l'exemple remplacent le corrigé.
