# La grille remplie de l'exemple · Projet de synthèse (sur 20)

> La grille de `projets/projet_synthese/GRILLE.md`, mêmes critères et mêmes points, remplie pour l'exemple : chaque case cochée a sa **preuve**, une section de l'article ([`exemple.ipynb`](exemple.ipynb)), une cellule, un test ou une commande, que tu peux refaire. C'est ce qu'on attend de ta propre copie (`grille.md` de ton dossier) : une preuve qu'un relecteur vérifie en une minute, pas une affirmation. Deux critères sont **sans objet** pour l'exemple, et le disent.

**Les noms de l'exemple.** L'article est `exemple.ipynb` (au lieu de `synthese.ipynb`), le module `poisson_newton.py` (au lieu de `algo.py`), ses tests `test_poisson_newton.py` (au lieu de `test_algo.py`). L'exemple tourne sur la référence de `mymath` : les commandes passent `--impl=ref`.

**Les vérifications communes**, refaites pour l'exemple depuis le dossier de workbookMaths, sur une copie :

```bash
export PYTHONDONTWRITEBYTECODE=1 WBM_ROOT="$PWD"
rm -rf /tmp/ps_copie && cp -r projets/projet_synthese/exemple /tmp/ps_copie
(cd /tmp/ps_copie && python -m pytest -q -rfs -p no:cacheprovider test_poisson_newton.py --impl=ref)                          # 102 passed, aucun SKIPPED
(cd /tmp/ps_copie && python -m pytest -q -p no:cacheprovider test_poisson_newton.py --impl=ref --mutant=newton_direction)     # 54 failed, 48 passed
(cd /tmp/ps_copie && python -m pytest -q -p no:cacheprovider test_poisson_newton.py --impl=ref --mutant=hessian)              # 15 failed, 87 passed
python tools/run_all_notebooks.py projets/projet_synthese/exemple/exemple.ipynb   # ✅ environ 11 s, cellule la plus lente 4 s
python -m pytest -q -p no:cacheprovider --impl=ref tests/test_m12b_orthogonal.py tests/test_m12d_svd_pca.py tests/test_m12c_eigen.py tests/test_m05a_approx.py tests/test_m19_iterative.py
```

(`run_all_notebooks.py` refuse les chemins sous `mon_travail/`, pas ceux de `projets/` : l'exemple s'exécute en place, sans copie.)

## PS.1 — Cadrer (1 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | `cadrage.md` tient en une page et dit l'algorithme choisi (sa ligne de la liste du README, ou, hors liste, pourquoi il convient : une dérivation d'au moins une page et un oracle indépendant), ce qu'il calcule, ses entrées et ses sorties avec leurs formes | 0,25 | lecture ; `wc -w cadrage.md` (une page : 600 mots au plus) | `cadrage.md`, « L'algorithme » (hors liste, et pourquoi il convient ; entrées $(n, p)$ et $(n,)$, sorties $(p,)$) ; `wc -w cadrage.md` : 589 mots |
| [x] | les notions de maths dont la dérivation a besoin, chacune avec le chapitre et la section de ce dépôt qui l'enseigne (« M18 §7 ») et, s'il y en a une, la section de MML | 0,25 | lecture ; ouvrir trois renvois au hasard : la section citée enseigne bien la notion | `cadrage.md`, le tableau des maths : onze notions, chacune avec sa section (M02b §2, M19 §1, M12c §7…) et, quand elle existe, sa section de MML (§8.3.1, §5.7…) |
| [x] | l'oracle de la vérification : la bibliothèque, la fonction et les réglages qui la rendent comparable à ton algorithme, et ce que cet oracle ne vérifie pas | 0,25 | lecture ; la fonction existe dans la documentation de la bibliothèque | `cadrage.md`, « L'oracle » : `PoissonRegressor` avec `alpha=0`, `fit_intercept=False`, `solver="newton-cholesky"`, `tol=1e-9`, la normalisation de son objectif ; ce qu'il ne vérifie pas (le chemin, la vitesse, les dérivées) |
| [x] | le plan de l'article, avec les deux propriétés visées pour PS.4, le cas limite pressenti et l'expérience visée pour PS.8 | 0,25 | lecture | `cadrage.md`, « Le plan de l'article » : propriétés 1 et 2, le cas limite (H4), l'expérience Newton contre montée de gradient |

## PS.2 — Poser le problème (1,5 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | §2 dit ce qu'est un exemple, ce que sont les paramètres et ce que l'algorithme calcule ou minimise, en une phrase, puis en une formule | 0,25 | lecture de §2 | §2, « En une phrase », puis « En une formule », éq. (2.1) et (2.2) |
| [x] | un tableau des notations : chaque symbole, son sens, sa forme (`(n, p)`, `(p,)`, scalaire) et son domaine | 0,5 | lecture ; trois symboles pris au hasard dans §3 sont dans le tableau, avec la même forme | §2, « Les notations » : 19 lignes, colonnes Sens, Forme, Domaine ; par exemple $\mathbf{W}$ $(n, n)$, $\tilde{\mathbf{r}}$ $(n,)$, $\boldsymbol{\delta}$ $(p,)$, que §3.3 à §3.5 utilisent avec ces formes |
| [x] | les hypothèses (sur les données, sur les paramètres : rang, positivité, indépendance, domaine de définition) écrites et numérotées, pour être citées en §3 et en §4 | 0,25 | lecture ; §3 ou §4 cite au moins une hypothèse par son numéro | §2, (H1) à (H4) ; citées en §3.1 (H1), §3.4 (H1, H2), §3.5 (H2), le lemme et les propriétés de §4 |
| [x] | les conventions annoncées : vecteurs lignes ou colonnes, gradient en ligne (convention jacobienne) ou de la forme de la variable, somme ou moyenne sur les exemples | 0,25 | lecture de §2 | §2, « Les conventions » : colonnes ; gradient de la forme de $\mathbf{w}$ (et l'écart avec MML) ; somme, et l'écart avec scikit-learn |
| [x] | les notations du dépôt ($n$ exemples, $p$ features, $\mathbf{X}$ de forme $(n, p)$, vecteurs et matrices en gras, $\ln$), ou chaque écart signalé | 0,25 | lecture | §2, dernier paragraphe : notations du dépôt gardées ; deux écarts signalés ($\mathbf{z}$ au lieu de $\boldsymbol{\eta}$, le sens de $\mathbf{W}$) |

## PS.3 — La dérivation complète (4 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | la dérivation part de l'objectif de §2 et arrive aux formules exactes que le code calcule : chaque formule finale porte un numéro, et la docstring de la fonction qui la calcule cite ce numéro | 1 | lecture croisée de §3 et des docstrings du module (la sortie « API » de §6) : aucune formule finale sans fonction, aucune fonction de calcul sans formule | §3, de (2.1) à (3.12), et la table « Les formules finales et le code » ; sortie « API » de la cellule « Contrôle du module » de §6 : chaque fonction de calcul cite « Eq. (…) » ((3.4) et (3.5) dans le corps des docstrings de `newton_direction` et `fit`) ; `check_data` vérifie (H1) et (H2) |
| [x] | chaque étape cite le résultat qui la justifie : chapitre et section de ce dépôt (« M17 §3 », « M12c §7 ») ou section de MML (« MML §5.5 »), et le résultat cité dit bien ce qui est utilisé | 1 | lecture ; ouvrir trois renvois au hasard | §3.2 : M17 §1 (jacobienne d'une application linéaire), R7 §5, M17 §3 et §4, M18 §6 et §7 ; §3.4 : M19 §1, M12c §7 (« Le minimum d'une quadratique »), R7 §3 ; §3.5 : M09a §4, M09b §3, M12b §1 et §7, M12d §4 |
| [x] | la forme de chaque objet est écrite, et chaque produit est vérifié (`(n, p)` fois `(p,)` donne `(n,)`) | 0,5 | lecture ; trois équations prises au hasard | les lignes *Formes* après (3.1), (3.2), (3.3), (3.4), (3.6) et (3.9) ; dans §3.3, $(n, n) \times (n, p) \to (n, p)$ puis $(p, n) \times (n, n) \times (n, p) \to (p, p)$ |
| [x] | la convention annoncée en §2 est tenue partout : pas de gradient tantôt ligne, tantôt colonne, pas de transposée qui apparaît sans être justifiée | 0,5 | lecture | §3.2, étape 3 : $\mathbf{J}_{\mathbf{f}}^\top$ justifiée par M17 §4, et le contrôle par la différentielle ($\nabla\ell = \mathbf{M}^\top$, M18 §7) ; la forme ligne de MML nommée comme un écart, jamais utilisée |
| [x] | aucune étape sautée : chaque ligne applique une règle, et aucune phrase ne remplace un calcul (« on voit que », « il est facile de voir », « après calcul », « évident ») | 0,5 | lecture ; `grep -c -i -E "on voit|facile de voir|après calcul|évident|clairement" /tmp/ps_copie/synthese.ipynb` donne 0 | `grep -c -i -E "on voit|facile de voir|après calcul|évident|clairement" projets/projet_synthese/exemple/exemple.ipynb` donne 0 (et `tests/infra/test_projet_synthese_exemple.py` le vérifie) |
| [x] | les points délicats du domaine sont dits et réglés : division par zéro, logarithme de 0, fonction non dérivable en un point, matrice non inversible (une hypothèse, une convention, un sous-gradient, une régularisation) | 0,5 | lecture | §3.1, « Points délicats » (comptage nul et $\ln 0$, overflow de $e^{z_i}$) ; §3.4 (la hessienne inversible : (H2)) ; §3.5 (pas de division par $\mu_i = 0$) ; §3.7 (le cas $S = 0$) |

## PS.4 — Deux propriétés et un cas limite (2,5 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | propriété 1 : un énoncé complet (hypothèses citées par leur numéro de §2, conclusion) et une démonstration rédigée (hypothèses, étapes justifiées, conclusion) où chaque hypothèse sert | 0,75 | lecture de §4 : retirer une hypothèse casse une étape précise | §4, le lemme et la propriété 1 (sous (H1) et (H2)) ; « Où servent les hypothèses » : (H1) donne $\mu_i > 0$ dans (4.1), (H2) donne $\ker\mathbf{X} = \lbrace \mathbf{0} \rbrace$ |
| [x] | propriété 2 : mêmes exigences | 0,75 | lecture de §4 | §4, propriété 2 (sous (H1), (H3) et (H4)), éq. (4.2) ; « Où servent les hypothèses » : sans (H3), $\sum_i\hat{\mu}_i \approx 12{,}35 \ne 12$ (cellule « cas limite ») |
| [x] | les deux propriétés portent sur l'algorithme (convexité, unicité, invariance, espérance, borne, coût…), pas sur un outil seul, et l'article dit ce que chacune garantit en pratique | 0,25 | lecture | §4, les deux paragraphes « Ce qu'elle garantit en pratique » (le pas défini et montant, un seul maximum ; le modèle calibré en moyenne) |
| [x] | le cas où une hypothèse tombe : l'hypothèse nommée, et un contre-exemple chiffré ou une expérience qui montre ce qui casse (une conclusion fausse, une itération qui diverge, plusieurs solutions), calculé par la cellule « cas limite » de §4 | 0,5 | lecture ; la sortie de la cellule | §4, théorème 3 et « Le cas où une hypothèse tombe » ; sortie de la cellule « cas limite » : (H4) $\ell$ croît le long de $\mathbf{d}$ et `NoMaximumError` après 28 pas ; (H2) $\ell$ constante le long du noyau ; (H3) la somme 12,35 |
| [x] | chaque propriété est aussi vérifiée numériquement (un test de propriété de PS.7 ou l'expérience de PS.8), et §4 renvoie à cette vérification | 0,25 | le renvoi dans §4 ; le test ou la figure existe | §4, « Vérifiée numériquement par » : `test_hessian_is_negative_definite`, `test_fit_finds_the_same_maximum_from_random_starts`, `test_fitted_means_sum_to_the_counts` ; le théorème 3 par §8.2 et `figures/sans_maximum.png` |

## PS.5 — Un exemple à la main (1,5 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | un exemple en petite dimension (2 ou 3, quelques exemples), dont toutes les données sont écrites dans §5 | 0,25 | lecture de §5 | §5, « Les données » : cinq soirées, $p = 2$, le tableau des $x_i$ et des $y_i$ |
| [x] | le calcul complet, étape par étape, avec les formules de §3 (citées par leur numéro), en fractions exactes quand c'est possible, sinon avec le nombre de chiffres gardés | 0,5 | lecture : les résultats intermédiaires sont écrits, pas seulement le résultat final | §5 : $\ell(\mathbf{0})$ par (3.1), $\nabla\ell(\mathbf{0}) = (7, 20)$ par (3.2), $-\mathbf{X}^\top\mathbf{X}$ par (3.3), $\boldsymbol{\delta}_0 = (\frac{1}{10}, \frac{13}{10})$ par (3.8), le pas plein refusé et $\mathbf{w}_1 = (\frac{1}{20}, \frac{13}{20})$ par (3.5), « 4 décimales gardées » pour les moyennes |
| [x] | la cellule de vérification de §5 retrouve le résultat à la main par le module, à une tolérance écrite et justifiée (en fractions : égalité exacte ; en flottants : pourquoi cet ordre de grandeur) | 0,5 | la sortie de la cellule : ✅ et l'écart le plus grand | sortie de la cellule « vérification de l'exemple » : « ✅ écart le plus grand … 2.2e-16 (tolérance 1e-12) », la tolérance justifiée dans le commentaire de `TOLERANCE` ; $\boldsymbol{\delta}_0$ refait en `Fraction` |
| [x] | un contrôle de vraisemblance annoncé avant le calcul : un ordre de grandeur, un signe, un cas dont le résultat est connu d'avance (un paramètre nul, une symétrie) | 0,25 | lecture | §5, « Le contrôle de vraisemblance, annoncé avant le calcul » : (a) le signe de la pente, (b) l'ordre de grandeur $\frac14\ln 10$ et le modèle sans feature, (c) la somme 12, (d) le dénominateur ; repris dans « Le résultat, et les contrôles annoncés » |

## PS.6 — L'implémentation avec `mymath` (3 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | chaque fonction publique du module a une docstring en anglais : ce qu'elle calcule (et son équation de §3), ses paramètres avec leurs formes, ce qu'elle rend et sa forme, les erreurs qu'elle lève | 0,75 | la sortie « API » de la cellule « Contrôle du module » de §6 ; lecture du module | sortie « API » : 13 ✅ ; `poisson_newton.py`, sections Parameters, Returns, Raises de chaque fonction |
| [x] | le module appelle au moins trois fonctions de `mymath`, chacune utile au calcul (pas un appel dont le résultat ne sert à rien) | 0,5 | la sortie « mymath » de la cellule « Contrôle du module » ; lecture | sortie « mymath » : cinq fonctions ; §6, premier point : le rôle de chacune dans le calcul |
| sans objet | ces trois fonctions sont les tiennes : leurs modules sont dans `mon_travail/mymath/` (la cellule les marque « à toi », jamais « référence »), et leurs tests passent avec ton code | 0,75 | la sortie « mymath » ; `python -m pytest -q tests/test_<id>_<module>.py` pour chaque module (vérifications communes) | **sans objet pour l'exemple**, qui tourne par construction sur la référence (setup de solution) : la sortie « mymath » marque les cinq fonctions « référence ». Leurs tests passent sur la référence (cellule suivante de §6, et la dernière commande des vérifications communes). Dans ton projet, ce critère est indispensable |
| [x] | les imports du module : NumPy, la bibliothèque standard et `mymath` ; ni scikit-learn, ni PyTorch, ni SciPy, ni SymPy (ce sont les oracles de PS.7) | 0,25 | la sortie « imports » de la cellule ; `grep -n -E "^\s*(import|from) " algo.py` | sortie « imports » : `math`, `numpy`, `mymath` ; `grep -n -E "^\s*(import|from) " projets/projet_synthese/exemple/poisson_newton.py` |
| [x] | une entrée invalide (formes incompatibles, valeur hors du domaine des hypothèses de §2) lève l'erreur que la docstring annonce, avec un message qui dit ce qui était attendu | 0,25 | lecture ; un test de `test_algo.py` le vérifie | sortie de la deuxième cellule de §6 (trois `ValueError`) ; `test_check_data_rejects_invalid_counts`, `test_check_data_rejects_dependent_columns`, `test_fit_raises_no_maximum_for_a_group_of_zeros` |
| [x] | le code se lit à côté des équations (mêmes noms, une équation par bloc) et ne boucle pas en Python sur les exemples ou les coordonnées quand une opération de NumPy le fait (une boucle sur les itérations ou sur le temps est normale) | 0,5 | lecture | `poisson_newton.py` : `mean`, `gradient`, `hessian` en une ligne de NumPy chacune, $\ln(y_i!)$ par une somme cumulée ; §6, « Sans boucle sur les exemples » : seules les itérations et les divisions du pas bouclent |

## PS.7 — La vérification contre une bibliothèque (3 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | `test_algo.py` compare l'algorithme à un oracle (NumPy, SciPy, SymPy, scikit-learn ou PyTorch) sur des cas tirés au hasard : au moins trois tailles et trois graines, en tests paramétrés aux noms lisibles | 0,75 | `python -m pytest test_algo.py -v` dans la copie : les cas sont listés | `python -m pytest projets/projet_synthese/exemple/test_poisson_newton.py --impl=ref -v` : `test_fit_matches_sklearn[n=20,p=2-seed=9010]` … `[n=500,p=5-seed=9012]`, et de même contre SciPy |
| [x] | l'oracle est indépendant : jamais une autre fonction du module ni de `mymath`, ni une formule de §3 recopiée dans le test ; ses réglages (tolérance d'un optimiseur, régularisation retirée, même initialisation) sont écrits et justifiés | 0,5 | lecture des tests | `test_poisson_newton.py` : `sklearn_weights` (réglages et leur raison), `oracle_log_likelihood` (`scipy.stats.poisson.logpmf`, pas la formule (3.1)) ; §7, le tableau ; `tests/infra/test_projet_synthese_exemple.py` vérifie qu'aucun test n'importe `mymath` |
| [x] | les dérivées que le code calcule sont comparées à des différences finies centrées écrites dans le test, avec le pas et la tolérance justifiés ; un algorithme dont le code ne calcule aucune dérivée vérifie à la place une condition d'optimalité de sa dérivation (par différences finies) ou un second oracle exact (fractions, énumération) | 0,5 | lecture des tests | `centred_gradient` et `centred_hessian` ; `test_gradient_matches_centred_differences` ($h = 10^{-5}$), `test_hessian_matches_centred_differences` ($h = 10^{-4}$), leurs docstrings justifient le pas et la tolérance (M05a §5 et §7, M19 §1) ; en plus, `test_fit_is_a_critical_point_by_finite_differences` |
| [x] | un test de propriété (une propriété de §4, une invariance, une identité, une borne) sur des cas tirés au hasard | 0,25 | lecture des tests | `test_fitted_means_sum_to_the_counts` (propriété 2, 3 × 3 cas), `test_fit_finds_the_same_maximum_from_random_starts` (propriété 1), `test_shifting_a_feature_changes_only_the_intercept` (une invariance) |
| [x] | la mutation : une copie d'une fonction avec une erreur plausible (dans `mutants.py`), que les tests attrapent ; la sortie de pytest qui échoue est dans §7, avec le nom du test qui l'attrape | 0,5 | la sortie de la cellule « mutation » de §7 ; `python -m pytest -q test_algo.py --mutant=<nom>` échoue dans la copie | `mutants.py` (`newton_direction`, `hessian`) ; sortie de la cellule « mutation » : 54 et 15 tests en échec, nommés (`test_newton_direction_matches_finite_differences`, `test_hessian_matches_centred_differences`…) ; §7, « Qui attrape quoi » ; vérifications communes, deuxième et troisième commandes |
| [x] | chaque message d'échec dit sur sa première ligne ce qui était attendu ; tous les tests passent, aucun n'est sauté | 0,5 | vérifications communes (`-rfs` : aucune ligne `SKIPPED`) ; lecture de trois `assert` | vérifications communes : « 102 passed », aucun `SKIPPED` ; `assert_close` (« … expected … at index … ») et les `assert … , f"expected …"` du fichier ; la sortie de la cellule « mutation » le montre |

## PS.8 — Une expérience numérique (1,5 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | la question et la prédiction sont écrites avant l'exécution (`PREDICTION` dans §8 : une phrase, et un nombre, une pente ou un sens de variation quand c'est possible), et reliées à une propriété de §4 ou à la dérivation | 0,5 | lecture de §8 | §8.1, « La question », « La prédiction » et `PREDICTION` (une pente $\log_{10}(1 - 1/\kappa)$, « au plus 7 pas »), reliée à (3.12) et au lemme ; §8.2, `PREDICTION_NO_MAXIMUM` et (8.1) ($s_k = -k$, le pas 28), reliée au théorème 3 |
| [x] | une figure lisible : les deux axes nommés avec leurs unités, une légende, un titre, une échelle adaptée (logarithmique pour une erreur qui décroît vite), enregistrée dans `figures/` | 0,5 | la sortie de la cellule de §8 (elle signale un axe sans nom ou une légende absente) ; le fichier dans `figures/` | sorties des deux cellules de figure de §8 (aucun ⚠️, « 🖼️ enregistrée ») ; `figures/convergence.png` et `figures/sans_maximum.png`, échelles logarithmiques pour les erreurs |
| [x] | la conclusion dit si la prédiction tient, avec la valeur lue sur la figure, et ce qui expliquerait un écart ; plusieurs graines quand le résultat dépend du hasard | 0,5 | lecture de §8 | §8.1, « Ce que montre la figure » et « Conclusion » (trois graines, pentes $-0{,}01167$, $-0{,}00897$, $-0{,}01070$, l'écart du début expliqué) ; §8.2, la conclusion (rapport 1, pas 28) |

## PS.9 — Rédiger l'article (1 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | l'article se lit seul : un résumé, une introduction qui dit ce qu'on dérive et pourquoi, un plan, une conclusion, des limites (ce que l'article ne montre pas) | 0,25 | lecture du résumé, de §1 et de §9 | « Résumé » ; §1 (pourquoi dériver, et le plan) ; §9, « Ce que l'article établit » et « Les limites » (ce qui est admis, ce que le code et les oracles ne font pas) |
| [x] | des références par sections (« MML §5.5 », « M18 §7 », le chapitre de workbookIA), rassemblées en fin d'article ; toute source qui a inspiré un passage est citée | 0,25 | lecture des références | « Références » : les sections de ce dépôt et de MML, Nelder et Wedderburn (1972), Wedderburn (1976), les documentations des oracles ; workbookIA : aucun chapitre, et pourquoi |
| [x] | un LaTeX propre : il s'affiche sans erreur sur GitHub ou Colab, les équations utiles sont numérotées, les notations de §2 sont tenues | 0,25 | ouvrir le notebook sur GitHub ou Colab | équations numérotées par `\tag` de (2.1) à (8.1) ; rendu vérifié dans Jupyter (le notebook exécuté) ; à rouvrir sur GitHub après publication |
| [x] | « Run all » finit en moins de 5 minutes sur CPU, aucune cellule ne dépasse une minute, et le notebook livré garde ses sorties | 0,25 | vérifications communes (`run_all_notebooks.py` donne les durées) ; les sorties présentes dans `mon_travail/projet_synthese/synthese.ipynb` | `run_all_notebooks.py` : environ 11 s, cellule la plus lente 4 s ; sortie de la dernière cellule (« ⏱️ « Run all » », moins de 15 s) ; sorties conservées dans `exemple.ipynb` |

## PS.E1 — Présenter (1 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [x] | le plan de l'exposé de cinq minutes dans l'annexe de l'article : les parties et la durée de chacune | 0,25 | lecture de l'annexe | « Annexe · La présentation », le tableau : cinq parties, 45 s, 1 min 30 s, 1 min, 45 s, 1 min |
| sans objet | la durée mesurée d'une répétition, entre 4 et 6 minutes | 0,25 | lecture de l'annexe | **sans objet pour l'exemple** : son auteur n'a pas de voix. L'annexe donne une estimation, pas une mesure : 650 mots, environ 5,0 minutes à 130 mots par minute (sortie de la cellule du texte de l'exposé). Dans ton projet, chronomètre une vraie répétition |
| [x] | cinq questions d'entretien (de la banque du README ou les tiennes) et tes réponses écrites, de quelques lignes chacune, qui renvoient à une équation, une propriété ou une figure de l'article, et qui disent « je ne sais pas » avec la façon de le vérifier quand c'est le cas | 0,5 | lecture de l'annexe | « Annexe », les cinq questions (de la banque du README) : renvois à (2.1), (3.7), la propriété 1, (3.12), §8.1, le théorème 3, (8.1) ; « je ne l'ai pas démontré ici ; je le vérifierais ainsi » (questions 3 et 5), et ce que les tests laisseraient passer (question 4) |

## Les pénalités

| Fait | Pénalité | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | un passage recopié ou paraphrasé de près sans être cité : un corrigé de workbookIA ou de ce dépôt, MML, un livre, un article, une page web (une citation entre guillemets avec sa source ne compte pas) | −3 | lecture à côté de la source soupçonnée ; une dérivation identique, ligne à ligne, à un corrigé | non appliquée : les dérivations sont rédigées pour l'exemple ; les sources qui l'ont guidé (Nelder et Wedderburn, Wedderburn) sont citées là où elles servent |
| [ ] | un notebook livré qui ne s'exécute pas de bout en bout : une sortie d'erreur dans le notebook livré, ou « Run all » qui s'arrête sur une erreur dans la copie | −2 | lecture des sorties ; vérifications communes | non appliquée : aucune sortie d'erreur (`tests/infra/test_projet_synthese_exemple.py::test_example_notebook_is_executed_without_errors`), « Run all » ✅ |

## Le total et les seuils

| | |
|---|---|
| Total des étapes | 19 / 19 points applicables (deux critères sans objet : 0,75 en PS.6 et 0,25 en PS.E1) |
| Pénalités | 0 |
| **Note** | **19 / 19**, soit 20 / 20 sur les critères applicables |

Ton projet, lui, est noté sur les 20 points : les deux critères sans objet ici (tes fonctions de `mymath`, ta répétition chronométrée) valent 1 point.
