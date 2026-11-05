# BIBLE — workbookMaths : les maths du machine learning, au rythme de workbookIA

*Spécification du dépôt (source de vérité). Version 1 du 2026-11-06, **validée** par l'apprenant. Toute décision ou dérogation est consignée au §24.*

Ce dépôt accompagne [workbookIA](https://github.com/cemah2/workbookIA) : **les deux workbooks se suivent en même temps**. Après une remise à niveau faite en parallèle du chapitre 0A de workbookIA, chaque chapitre de maths se fait **juste avant** le chapitre de workbookIA qui en a besoin, et porte son numéro (M12a, M12b… avant le ch. 12). Il part d'un niveau lycée lointain, reprend le format de workbookIA (fiches, exercices papier, notebooks vérifiés automatiquement, indices, solutions, flashcards, librairie construite de ses mains) et suit le livre *Mathematics for Machine Learning* (MML), dans l'ordre où workbookIA en a besoin.

## 0. Statut et points ouverts

- **Statut** : v1 validée le 2026-11-06. La v0 rangeait les chapitres par grands thèmes mathématiques ; la v1 les cale sur le chemin de workbookIA, à la demande de l'apprenant.
- **Validé** : nom du dépôt (`workbookMaths`), temps disponible sans limite, ordre calqué sur workbookIA, plan du §8, lecture de MML intégrée au travail (§3).
- **Fixé en session 1** : versions (§22), outillage copié depuis workbookIA (§23), ressources secondaires vérifiées (§3).
- **Fixé en session 2** : le syllabus détaillé (exercices, ID, signatures `mymath`, temps), comme pour workbookIA.

## 1. Profil de l'apprenant

| Élément | Valeur | Conséquence pour la génération |
|---|---|---|
| Objectif | Avoir les bases mathématiques pour étudier **workbookIA en même temps**, dans le cadre d'une **reconversion professionnelle** vers l'IA et la data | Chaque chapitre de maths prépare un chapitre précis de workbookIA, juste avant lui (§8, §9) |
| Niveau maths | **Lycée, lointain** : bases vues autrefois, en grande partie oubliées | Partie 0 de remise à niveau (du collège à la terminale), test de positionnement pour sauter ce qui est su ; aucune notion utilisée avant d'être enseignée |
| Niveau Python | Débutant | Le ch. 0A de workbookIA (Python) se fait pendant la partie 0 ; R0 ne donne que ce qui sert aux maths (SymPy, `wbm.check`, LaTeX) |
| Lecture en anglais | MML n'existe qu'en anglais, comme le livre de Glassner de workbookIA | Vocabulaire anglais en glose, glossaire FR ↔ EN, guide de lecture de chaque section |
| Temps disponible | **Sans limite** ; l'objectif est l'exhaustivité | Le parcours complet est le parcours par défaut ; un parcours essentiel existe pour qui veut aller plus vite (§12) |
| Matériel | Google Colab + ordinateur personnel sans GPU | Aucun GPU nécessaire ; tout tourne sur CPU en quelques minutes |
| Langue | Explications en français, code en anglais | §5 |

## 2. Objectifs

1. **Comprendre** chaque notion : intuition, définition, exemple chiffré, figure, puis démonstration quand elle éclaire.
2. **Calculer à la main** avec aisance : c'est le cœur d'un dépôt de maths (exercices ✏️ et ∂ majoritaires).
3. **Vérifier et explorer en code** : NumPy et SymPy retrouvent les calculs papier ; `mymath` (§11) implémente les algorithmes numériques.
4. **Arriver prêt** à chaque chapitre de workbookIA : il ne doit plus y rester de notion mathématique nouvelle, seulement son application.
5. **Lire MML** : savoir lire une section du livre et refaire ses exemples.

## 3. Livres et ressources sources

**Livre principal** : M. P. Deisenroth, A. A. Faisal et C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020 (site du livre : mml-book.github.io). La version PDF est gratuite **pour un usage personnel uniquement** ; sa notice interdit la redistribution, la revente et les **œuvres dérivées**. Conséquences :
- le PDF n'est jamais versionné (`.gitignore` : `*.pdf`) ;
- aucun passage n'est recopié, même paraphrasé de près ; les fiches sont des cours originaux et renvoient aux sections sous la forme « (MML §4.5) » ;
- les exercices sont originaux ; ceux de fin de chapitre de MML (ch. 2 à 7) sont seulement **conseillés** (« MML ex. 4.3 ») et jamais corrigés mot pour mot ;
- les renvois se font par **numéro de section**, jamais par page (les pages diffèrent entre le PDF et l'édition imprimée).

Sommaire de MML (vérifié le 2026-11-05) : partie I, ch. 2 *Linear Algebra* (§2.1 à 2.8), ch. 3 *Analytic Geometry* (§3.1 à 3.9), ch. 4 *Matrix Decompositions* (§4.1 à 4.7), ch. 5 *Vector Calculus* (§5.1 à 5.8), ch. 6 *Probability and Distributions* (§6.1 à 6.7), ch. 7 *Continuous Optimization* (§7.1 à 7.3) ; partie II, ch. 8 *When Models Meet Data* (§8.1 à 8.6), ch. 9 *Linear Regression*, ch. 10 *PCA*, ch. 11 *Gaussian Mixture Models*, ch. 12 *Support Vector Machines*.

**MML se lit dans l'ordre de workbookIA, donc dans le désordre** : la colonne « MML » du §8 dit quelle section lire avant quel chapitre, et `annexes/correspondances.md` dit, pour chaque section du livre, le chapitre qui la couvre. Le livre suppose le niveau d'un début d'études supérieures : la partie 0 ne s'y réfère pas.

**La lecture de MML fait partie du travail** (validé le 2026-11-06), comme celle de Glassner dans workbookIA : un bloc du livre, puis la partie de la fiche correspondante, puis les exercices de ce bloc. Chaque fiche reste un cours complet en français, sur lequel s'appuyer quand un passage du livre résiste.

**Ce que MML ne couvre pas** : la remise à niveau, l'analyse d'une variable (limites, intégrales), les théorèmes limites, les tests, les inégalités de concentration, les chaînes de Markov, la théorie de l'information, la convolution. Pour ces chapitres, la fiche est le cours, et elle renvoie à des ressources libres, **vérifiées en session 1** avant d'être citées :
- probabilités : J. K. Blitzstein et J. Hwang, *Introduction to Probability* (2ᵉ éd.), dont une version en ligne gratuite est annoncée par le cours Stat 110 de Harvard (vérifié le 2026-11-05) ;
- information : D. J. C. MacKay, *Information Theory, Inference, and Learning Algorithms* (PDF gratuit, à vérifier) ;
- statistique : *OpenIntro Statistics* (licence libre, à vérifier) ;
- démonstrations : R. Hammack, *Book of Proof* (gratuit, à vérifier) ;
- remise à niveau et lycée, en français : manuels Sésamath, vidéos d'Yvan Monka (Maths et tiques), Khan Academy en français ; niveau licence : cours Exo7 (tous à vérifier).

## 4. Stack technique

- **Python** : la version de Colab (3.13 pour workbookIA, revérifiée en session 1).
- **Bibliothèques** : numpy, scipy, **sympy** (calcul symbolique : vérifier une dérivée, une intégrale, une factorisation), matplotlib, pandas (léger), pytest ; scikit-learn pour quelques oracles (moindres carrés, ACP, SVM). **Pas de PyTorch** : les oracles de la différentiation automatique viennent de SymPy et des différences finies.
- **Versions** : figées sur celles préinstallées sur Colab (même politique que workbookIA), §22.
- **Budget d'exécution** : notebook de solutions < 5 min sur CPU, aucune cellule > 1 min. Pas de mode GPU.
- **Indépendance** : ce dépôt n'importe jamais rien de workbookIA. Son package d'outils s'appelle `wbm` (et non `wb`) et sa librairie `mymath` (et non `mylearn`), pour que les deux dépôts s'installent dans le même environnement sans conflit.

## 5. Langue et terminologie

- Markdown en français, tutoiement, phrases courtes ; code, docstrings et commentaires en anglais.
- **Termes mathématiques en français** (valeur propre, application linéaire, noyau, rang, espérance, vraisemblance…), avec le terme anglais en glose à la première occurrence du chapitre qui le définit : « valeur propre (*eigenvalue*) ».
- **Termes du ML** : exactement ceux de workbookIA (loss, learning rate, batch, feature, dataset… restent en anglais ; « divergence KL », « underflow »…), pour que l'apprenant retrouve les mêmes mots dans les deux workbooks. Le test de terminologie de workbookIA est copié avec la même liste.
- Tout terme va dans `annexes/glossaire.md` (FR ↔ EN, définition courte, chapitre).
- Virgule décimale dans le texte (0,5), point dans le code (0.5) ; `wbm.check` accepte les deux (§14).

## 6. Notations

- LaTeX dans le Markdown, compatible GitHub, Colab et Jupyter.
- **Mêmes conventions que workbookIA** : scalaires en italique ($x$), vecteurs en gras minuscule ($\mathbf{x}$), matrices en gras majuscule ($\mathbf{A}$) ; $n$ exemples, $p$ features, $\mathbf{X}$ de forme $(n, p)$ ; prédiction $\hat{y}$, loss $L$, learning rate $\eta$, somme pondérée $z$.
- **Écarts avec MML, signalés une fois par un encadré 📐** : MML note $N$ exemples et $D$ dimensions ; MML écrit le gradient d'une fonction $\mathbb{R}^n \to \mathbb{R}$ comme un **vecteur ligne** (convention jacobienne), alors que NumPy et workbookIA lui donnent la forme de $\mathbf{x}$. Le dépôt utilise la convention jacobienne pour le calcul matriciel (M17, M18) et $\nabla f$ de la forme de $\mathbf{x}$ pour l'optimisation, en disant chaque fois laquelle.
- Vecteurs colonnes par défaut ; $\mathbb{E}$, $\mathbb{V}$, $\operatorname{Cov}$ pour l'espérance, la variance et la covariance ; $\mathcal{N}(\mu, \sigma^2)$ ; $\log$ = logarithme népérien sauf mention ($\log_2$, $\log_{10}$).
- `annexes/symboles.md` explique comment **lire** chaque symbole à voix haute (∀, ∃, ∈, ⊂, Σ, Π, ∫, ∂, ∇, ‖·‖, ⟨·,·⟩, argmax, ∝, :=…).

## 7. Architecture du dépôt

Dépôt **`cemah2/workbookMaths`** (validé).

```
workbookMaths/
├── README.md                 présentation, démarrage Colab et local, ordre de travail commun avec workbookIA
├── CLAUDE.md                 consignes pour les sessions de génération
├── requirements.txt / pyproject.toml
├── 00_setup/                 installation (Colab, local), check_env.py, demo.ipynb
├── positionnement/           test de positionnement (sujet, notebook vérifié, grille « ce que tu peux sauter »)
├── chapitres/
│   └── <id>_<nom>/           ex. r7_derivation, m12c_valeurs_propres, mb3_rotations_attention
│       ├── 01_fiche.md        le cours
│       ├── 02_exercices.md
│       ├── 03_notebook.ipynb
│       ├── 04_indices.md
│       ├── 05_solutions.md
│       ├── 05_solutions.ipynb (exécuté, sorties conservées)
│       ├── 06_mes_reponses.md
│       ├── flashcards.csv
│       └── figures/
├── checkpoints/partie_0 … partie_6/   examen blanc, synthèse
├── projets/projet_synthese/  le projet de fin
├── annexes/                  glossaire FR↔EN, symboles, formulaire, index des notions, erreurs de calcul fréquentes,
│                             correspondances (workbookIA ↔ ce dépôt ↔ MML), cheatsheets (NumPy linalg, SymPy, matplotlib), Anki, ressources
├── src/wbm/                  outils : setup, check, datasets, figures, nbtools
├── templates/mymath_stubs/   squelettes de la librairie (figés)
├── solutions/mymath_ref/     implémentation de référence
├── tests/                    tests de mymath (test_<id>_<module>.py) et de l'outillage (tests/infra/)
├── data/                     données légères versionnées + cards/
├── docs/                     BIBLE.md, METHODE.md, SYLLABUS.md et PARCOURS.md (générés), syllabus/data/
├── suivi/                    PROGRESS.md (génération) et modèles de suivi de l'apprenant
├── tools/                    start_chapter.py, build_answers.py, run_all_notebooks.py, export_flashcards.py, syllabus.py, chapters/
└── mon_travail/              ESPACE DE L'APPRENANT : Claude n'y écrit jamais
```

Règles anti-conflit identiques à workbookIA : Claude n'écrit jamais dans `mon_travail/` ; `start_chapter.py` copie sans jamais écraser ; un stub publié ne change plus.

## 8. Plan : chapitre par chapitre de workbookIA

**Identifiants.** La remise à niveau est numérotée R0 à R9. Ensuite, chaque chapitre porte le numéro du chapitre de workbookIA qu'il prépare, avec une lettre s'il y en a plusieurs : M02a, M02b et M02c se font avant le ch. 2 de workbookIA ; MB3 avant le bonus B3. Les ID d'exercices suivent (`R7.4`, `M12c.4`, `MB3.Q2`) et ne se confondent jamais avec ceux de workbookIA (`12.4`).

**Règle de partage.** Le chapitre de maths enseigne la notion (définition, calcul à la main, démonstration, petite implémentation) ; le chapitre de workbookIA l'applique (données réelles, bibliothèques, modèles). Un chapitre de maths ne reprend ni les exemples, ni les données, ni les nombres des exercices du chapitre de workbookIA qu'il prépare, et ne donne aucune réponse qu'il vérifie.

**Chapitres de workbookIA sans chapitre de maths** (la partie 0 et les chapitres précédents suffisent) : 1, 15, 23, 24, 29, B1, B7.

Les durées sont des estimations (lecture, exercices, flashcards) ; le syllabus (session 2) les recalcule exercice par exercice.

### Partie 0 · Remise à niveau — en parallèle de workbookIA 0A, avant workbookIA 0B

| ID | Titre | Contenu | `mymath` | ≈ h |
|---|---|---|---|---|
| POS | Test de positionnement | un ou deux exercices par chapitre de la partie 0, et une grille qui dit ce que tu peux sauter | — | 3 |
| R0 | Prise en main | le notebook du dépôt, `wbm.check`, Python comme calculatrice, SymPy, écrire une formule en LaTeX | `_example` | 3 |
| R1 | Nombres et calcul | priorités, fractions, puissances, racines, notation scientifique, ordres de grandeur, arrondis, partie entière, pourcentages, proportionnalité, moyenne et moyenne pondérée, estimations de Fermi | `arith` | 12 |
| R2 | Calcul littéral et équations | développer, factoriser, identités remarquables, équations et inéquations du 1ᵉʳ degré, valeur absolue et fonction signe, systèmes 2 × 2, mettre un problème en équation | `algebra` | 14 |
| R3 | Fonctions | notion de fonction, graphe, lecture graphique, fonctions affines, carré, inverse, racine, polynômes du second degré (forme canonique, discriminant), variations, composition, réciproque | `functions` | 14 |
| R4 | Logique, ensembles, Σ et Π | propositions, quantificateurs, implication et équivalence, ensembles et intervalles, notations Σ et Π, raisonnements (direct, contraposée, absurde, contre-exemple, récurrence), rédiger une démonstration courte | `logic` | 12 |
| R5 | Suites | suites arithmétiques et géométriques, sommes finies et infinies, limite d'une suite, moyennes mobiles et exponentielles | `sequences` | 10 |
| R6 | Exponentielle et logarithmes | propriétés, croissances comparées, ln, log₂, log₁₀, échelles logarithmiques, sigmoïde et tanh | `explog` | 12 |
| R7 | Limites et dérivation | limites de fonctions, continuité, taux d'accroissement, dérivée, règles (somme, produit, quotient, composée), variations, extrema, tangente (MML §5.1, premières pages) | `deriv` | 16 |
| R8 | Probabilités de base | expérience aléatoire, événements, arbres, dénombrement (factorielle, combinaisons), indépendance, variable aléatoire discrète, espérance, variance, simulation | `proba_basics` | 12 |
| R9 | Géométrie du plan, vecteurs et trigonométrie | repère, coordonnées, distance, vecteurs du plan et de l'espace, norme, produit scalaire, droites, cercle trigonométrique, radians, cosinus et sinus | `plane` | 12 |
| CP0 | Bilan de remise à niveau | examen blanc et synthèse, avant d'ouvrir workbookIA 0B | | 4 |

Après la partie 0, le chapitre 0B de workbookIA devient une consolidation : il reprend tout cela, l'étend aux vecteurs et matrices de ℝⁿ et au gradient, et le relie au ML.

### Partie I · Fondations (workbookIA ch. 1 à 6)

| Avant | ID | Titre | Contenu | MML | `mymath` | ≈ h |
|---|---|---|---|---|---|---|
| 1 | — | rien de nouveau | | | | |
| 2 | M02a | Intégrales et densités | aire sous une courbe, primitives, intégrale, intégration par parties, changement de variable, intégrales impropres, intégrale de Gauss, méthodes numériques ; densité, fonction de répartition, quantiles | (prérequis de §6.2) | `integrate` | 14 |
| 2 | M02b | Variables aléatoires et lois usuelles | lois discrètes et continues (Bernoulli, binomiale, catégorielle, géométrique, Poisson, uniforme, exponentielle, normale), espérance, variance, linéarité, variance d'une somme de variables indépendantes, changement de variable | §6.1–6.2, §6.4, §6.7 | `distributions` | 14 |
| 2 | M02c | Échantillons et estimation | i.i.d., tirages avec et sans remise, loi des grands nombres, théorème central limite, estimateurs, biais et ddof, erreur type, intervalle de confiance, bootstrap ; covariance et corrélation empiriques, première matrice de covariance | §6.4 | `estimation` | 14 |
| 3 | M03 | Probabilités conditionnelles | probabilités jointes et marginales, tableaux de contingence, conditionnement, indépendance, probabilités totales ; l'AUC vue comme une aire et comme une probabilité | §6.3 | `conditional` | 10 |
| 4 | M04 | Bayes, vraisemblance et loi Beta | formule de Bayes, a priori, vraisemblance, a posteriori, mises à jour successives, loi Beta et conjugaison, MAP, log-probabilités, intervalle de crédibilité | §6.3, §6.6, §8.3 | `bayes` | 12 |
| 5 | M05a | Dérivées, Taylor et calcul numérique | dérivée seconde, convexité en 1D, polynômes de Taylor, méthode de Newton, différences finies, nombres flottants, erreurs d'arrondi | §5.1 | `approx` | 14 |
| 5 | M05b | Fonctions de plusieurs variables et gradient | surfaces, lignes de niveau, dérivées partielles, gradient, dérivée directionnelle, points critiques et points selles, descente de gradient | §5.2 | `multivar` | 12 |
| 6 | M06 | Théorie de l'information | information, entropie, entropies conjointe et conditionnelle, entropie croisée, divergence KL et sa positivité (inégalité de Jensen), Jensen-Shannon, codes et inégalité de Kraft, perplexité | — (MacKay) | `info` | 12 |
| CP1 | CP1 | Examen blanc et synthèse | juste avant le checkpoint I de workbookIA | | | 4 |

### Partie II · Concepts (workbookIA ch. 7 à 11)

| Avant | ID | Titre | Contenu | MML | `mymath` | ≈ h |
|---|---|---|---|---|---|---|
| 7 | M07 | Vecteurs et géométrie de ℝⁿ | normes L1, L2, L∞, distances, produit scalaire, angle, similarité cosinus, Cauchy-Schwarz, hyperplans et demi-espaces, barycentre (la moyenne minimise la somme des carrés des distances), grande dimension et concentration des distances | §3.1, §3.3–3.4 | `vectors` | 12 |
| 8 | M08 | Tests statistiques | hypothèses, statistique de test, p-valeur, test par permutation, erreurs de type I et II, intervalle d'une accuracy, comparaisons multiples, sélection de modèle | §8.6 | `testing` | 10 |
| 9 | M09a | Matrices et systèmes linéaires | matrices, produit et formes, produit élément par élément (Hadamard), transposée, systèmes linéaires, pivot de Gauss, inverse, premier contact avec le rang | §2.1–2.3 | `matrices` | 16 |
| 9 | M09b | Moindres carrés et régularisation | régression linéaire, équations normales, ridge (et ridge vue comme MAP), lasso et seuillage doux, MSE, MAE et R², décomposition biais-variance, régression vue comme maximum de vraisemblance, aperçu de la régression bayésienne | §8.1–8.2, ch. 9 | `linreg` | 14 |
| 10 | M10 | Séparabilité linéaire et convexité | ensembles convexes, enveloppe convexe, séparation par un hyperplan, XOR, théorème de convergence du perceptron (démonstration) | §12.1 | `convex` | 8 |
| 11 | M11 | Logique, induction et inégalités de concentration | déduction, validité, syllogismes, induction ; moyenne incrémentale, inégalités de Markov, Tchebychev et Hoeffding, bornes de confiance (UCB), regret | — | `concentration` | 10 |
| CP2 | CP2 | Examen blanc et synthèse | juste avant le checkpoint II de workbookIA | | | 4 |

### Partie III · ML classique (workbookIA ch. 12 à 15)

| Avant | ID | Titre | Contenu | MML | `mymath` | ≈ h |
|---|---|---|---|---|---|---|
| 12 | M12a | Espaces vectoriels et applications linéaires | sous-espaces, indépendance, base, dimension, rang, applications linéaires, noyau, image, théorème du rang, changement de base, applications affines | §2.4–2.8 | `linmaps` | 16 |
| 12 | M12b | Orthogonalité et projections | produits scalaires, bases orthonormées, Gram-Schmidt, complément orthogonal, projection orthogonale, les moindres carrés vus comme une projection, QR | §3.2, §3.5–3.8 | `orthogonal` | 14 |
| 12 | M12c | Valeurs propres et matrices symétriques | déterminant, trace, valeurs et vecteurs propres, diagonalisation, théorème spectral, matrices définies positives, Cholesky, formes quadratiques, matrice de covariance, blanchiment (*whitening*) | §4.1–4.4 | `eigen` | 16 |
| 12 | M12d | SVD et analyse en composantes principales | SVD, approximation de rang faible, pseudo-inverse, conditionnement, ACP (variance maximale et projection), variance expliquée | §4.5–4.7, ch. 10 | `svd_pca` | 14 |
| 13 | M13a | Vraisemblance et régression logistique | maximum de vraisemblance, la log-loss comme moins la log-vraisemblance, sigmoïde et sa dérivée, convexité de la log-loss, Naïve Bayes comme modèle génératif, entropie et indice de Gini | §8.3 | `likelihood` | 12 |
| 13 | M13b | Optimisation sous contraintes et SVM | multiplicateurs de Lagrange, dualité, optimisation convexe, marge, SVM primal et dual, noyaux | §7.2–7.3, ch. 12 | `svm` | 14 |
| 14 | M14 | Les maths des ensembles | vote majoritaire et loi binomiale, variance d'une moyenne de modèles corrélés, bootstrap et la limite $(1 - 1/n)^n \to 1/e$, pondérations exponentielles d'AdaBoost, gradient boosting comme descente de gradient | — | `ensembles` | 8 |
| 15 | — | rien de nouveau | | | | |
| CP3 | CP3 | Examen blanc et synthèse | juste avant le checkpoint III de workbookIA | | | 4 |

### Partie IV · Réseaux (workbookIA ch. 16 à 20)

| Avant | ID | Titre | Contenu | MML | `mymath` | ≈ h |
|---|---|---|---|---|---|---|
| 16 | M16 | Couches affines et variance à l'initialisation | composition d'applications affines (sans non-linéarité, un réseau profond reste affine), formes et comptage des paramètres, variance d'une somme de produits indépendants, initialisations de Glorot et de He (dérivation) | §6.4 | `init` | 8 |
| 17 | M17 | Jacobienne et fonctions d'activation | jacobienne, dérivées des activations, jacobienne de la softmax, propriétés de la softmax (translation, température), log-sum-exp et sa convexité | §5.3 | `jacobian` | 10 |
| 18 | M18 | Règle de la chaîne, calcul matriciel et différentiation automatique | règle de la chaîne multivariée, gradients par rapport à une matrice, identités utiles, graphe de calcul, modes direct et inverse, vérification de gradient | §5.4–5.6 | `autodiff` | 14 |
| 19 | M19 | Hessienne, convexité et convergence | hessienne, Taylor multivariée, conditionnement, convergence de la descente de gradient sur une quadratique (pas critique), momentum comme suite récurrente, moyennes exponentielles et correction du biais, fonctions convexes | §5.7–5.8, §7.1, §7.3 | `optim` | 14 |
| 20 | M20 | Tenseurs, dropout et normalisation | tableaux à n dimensions et `einsum`, espérance et dropout inversé, normalisation par batch (moyenne, variance, transformation affine), connexions résiduelles et gradient | — | `tensors` | 8 |
| CP4 | CP4 | Examen blanc et synthèse | juste avant le checkpoint IV de workbookIA | | | 4 |

### Partie V · Architectures (workbookIA ch. 21 à 24)

| Avant | ID | Titre | Contenu | MML | `mymath` | ≈ h |
|---|---|---|---|---|---|---|
| 21 | M21 | Convolution | convolution et corrélation croisée en 1D et 2D, la convolution comme application linéaire (matrice de Toeplitz), équivariance par translation, tailles de sortie, transposée d'une convolution, champ récepteur | — | `conv` | 10 |
| 22 | M22 | Récurrences et gradient évanescent | suites récurrentes vectorielles, puissances d'une matrice, rayon spectral, normes de matrices, produits de jacobiennes, gradient évanescent ou explosif, clipping | (§4.2) | `recurrence` | 10 |
| 23, 24 | — | rien de nouveau | | | | |
| CP5 | CP5 | Examen blanc et synthèse | juste avant le checkpoint V de workbookIA | | | 4 |

### Partie VI · Génératif et RL (workbookIA ch. 25 à 29)

| Avant | ID | Titre | Contenu | MML | `mymath` | ≈ h |
|---|---|---|---|---|---|---|
| 25 | M25a | Gaussienne multivariée | densité et géométrie, marginales et conditionnelles, transformations affines, échantillonnage par Cholesky, divergence KL entre gaussiennes, interpolation sphérique | §6.5 | `gaussian` | 14 |
| 25 | M25b | Variables latentes et ELBO | inégalité de Jensen, variables latentes et modèles graphiques orientés, mélanges de gaussiennes et algorithme EM, borne inférieure de l'évidence (ELBO), astuce de reparamétrisation | §6.7, §8.4–8.5, ch. 11 | `latent` | 12 |
| 26 | M26 | Chaînes de Markov et équation de Bellman | matrice de transition, loi stationnaire, processus de décision markovien, espérance conditionnelle, retour actualisé, équation de Bellman (système linéaire et point fixe) | — (Blitzstein et Hwang) | `markov` | 12 |
| 27 | M27 | Jeux et distances entre lois | jeux à somme nulle, minimax, discriminateur optimal (dérivation), Jensen-Shannon, distance de Wasserstein en 1D, distance de Fréchet entre gaussiennes, racine carrée d'une matrice | — | `distances` | 10 |
| 28 | M28 | Matrice de Gram et échantillonnage | matrice de Gram, montée de gradient, échantillonner une loi catégorielle, température, top-k et top-p | — | `sampling` | 6 |
| 29 | — | rien de nouveau | | | | |
| CP6 | CP6 | Examen blanc et synthèse | juste avant le checkpoint VI de workbookIA | | | 4 |

### Partie VII · Bonus (workbookIA B1 à B8)

| Avant | ID | Titre | Contenu | MML | `mymath` | ≈ h |
|---|---|---|---|---|---|---|
| B1 | — | rien de nouveau | | | | |
| B2 | MB2 | Cooccurrences, PMI et embeddings | information mutuelle ponctuelle (PMI, PPMI), SVD tronquée, géométrie des analogies, modèle logistique de word2vec | — | `cooccurrence` | 8 |
| B3 | MB3 | Rotations et attention | formules trigonométriques, encodages sinusoïdaux, rotations et nombres complexes (RoPE), variance d'un produit scalaire et facteur $1/\sqrt{d}$, l'attention comme moyenne pondérée | §3.9 | `positional` | 10 |
| B4 | MB4 | Rang faible et recherche d'information | adaptation de rang faible (LoRA) et nombre de paramètres, BM25, métriques de recherche (recall@k, MRR) | (§4.6) | `retrieval` | 6 |
| B5 | MB5 | Les maths de la diffusion | sommes de gaussiennes, forme fermée du processus direct, posterior gaussien, ELBO de la diffusion, équations différentielles et méthode d'Euler (flow matching) | (§6.5) | `diffusion` | 12 |
| B6 | MB6 | Shapley, intégrales de chemin et équité | valeurs de Shapley (combinatoire et axiomes), gradients intégrés (intégrale le long d'un chemin), théorème d'impossibilité de l'équité | — | `attribution` | 8 |
| B7 | — | rien de nouveau | | | | |
| B8 | MB8 | Gradient de politique | astuce de la dérivée du logarithme, échantillonnage d'importance et ratio de PPO, baseline et réduction de variance, GAE, modèle de Bradley-Terry, pénalité KL | — | `policy_gradient` | 10 |

### Fin

| ID | Titre | Contenu | ≈ h |
|---|---|---|---|
| PS | Projet de synthèse | « Les maths d'un algorithme, de A à Z » : tu choisis un algorithme de workbookIA (régression logistique, rétropropagation d'un MLP, VAE, attention…) et tu écris un notebook-article qui dérive tout, l'implémente avec `mymath` et le vérifie contre une bibliothèque ; grille sur 20, pas de solution de référence, un exemple rédigé sur un autre algorithme. Il se fait en même temps que le projet final de workbookIA | 25 |

**Totaux estimés** : 49 chapitres (≈ 565 h, dont ≈ 117 h pour la remise à niveau), 7 examens blancs (≈ 28 h), test de positionnement et projet de synthèse (≈ 28 h) : **≈ 620 h** pour le parcours complet, à ajouter aux ≈ 920 h de workbookIA ; ≈ 340 h pour le parcours essentiel. Le test de positionnement peut retirer une partie de la remise à niveau.

**MML est couvert en entier** : ch. 2 (M09a, M12a), ch. 3 (M07, M12b, MB3), ch. 4 (M12c, M12d), ch. 5 (R7, M05a, M05b, M17, M18, M19), ch. 6 (M02b, M02c, M03, M04, M25a), ch. 7 (M13b, M19), ch. 8 (M04, M08, M09b, M13a, M25b), ch. 9 (M09b), ch. 10 (M12d), ch. 11 (M25b), ch. 12 (M10, M13b).

## 9. Ordre de travail commun

La règle : **la partie 0 pendant workbookIA 0A, puis, avant chaque chapitre k de workbookIA, les chapitres de maths qui portent son numéro.** L'examen blanc de maths d'une partie se fait juste avant le checkpoint de workbookIA de la même partie. Le début de l'ordre :

1. Maths : test de positionnement, puis R0 à R9 ; en parallèle, workbookIA 0A.
2. Maths : CP0. Puis workbookIA 0B, puis workbookIA 1.
3. Maths : M02a, M02b, M02c. Puis workbookIA 2.
4. Maths : M03. Puis workbookIA 3. Et ainsi de suite jusqu'à B8.

Le README affiche l'ordre complet sous forme de liste à cocher (générée par `tools/syllabus.py build`), et `start_chapter.py` de ce dépôt, lancé avec un numéro de workbookIA (`python tools/start_chapter.py 12`), prépare d'un coup les chapitres M12a à M12d. `annexes/correspondances.md` donne, pour chaque chapitre de workbookIA, les notions de maths utilisées et l'endroit où elles sont enseignées.

## 10. Données

- **Synthétiques** (`wbm.synth`, avec graine) : la plupart des exercices.
- **Palmer Penguins** (CC0) : statistique, estimation, tests, ACP.
- **Holmes** et **Verne** (Project Gutenberg, domaine public) : comptages, probabilités, Markov, information.
- **Images** du domaine public : SVD et rang faible.
- Chaque jeu a sa fiche `data/cards/<nom>.md` (provenance, licence, limites). Les fichiers sont recopiés depuis leurs sources officielles (pas depuis workbookIA), avec `tools/build_datasets.py`. Règle du §8 : jamais les données d'un exercice du chapitre de workbookIA préparé.

## 11. mymath : la librairie que l'apprenant construit

- Même mécanisme que `mylearn` dans workbookIA : un module par chapitre dans `templates/mymath_stubs/` (signature, docstring en anglais, `raise NotImplementedError`), copié dans `mon_travail/mymath/` par `start_chapter.py` ; référence dans `solutions/mymath_ref/`.
- **Tests fondés sur un oracle qui ne révèle pas la solution** : NumPy (`numpy.linalg`), SciPy (`scipy.integrate`, `scipy.optimize`, `scipy.stats`), **SymPy** (dérivées, intégrales, limites exactes), `fractions.Fraction` (calcul exact), scikit-learn ; plus des tests de propriétés (une projection est idempotente, une matrice de covariance est symétrique semi-définie positive, une loi stationnaire est invariante…).
- Modules indicatifs dans les tableaux du §8 ; les signatures sont figées au syllabus (session 2) et ne changent plus.
- `mymath` recoupe volontairement `mylearn` (statistiques, gradient numérique, information, ACP) : l'apprenant écrit d'abord la version mathématique ici, puis la version ML dans workbookIA, ce qui fait un rappel espacé. Les deux librairies restent indépendantes.

## 12. Parcours

- **Complet** (par défaut) : tout le dépôt, démonstrations comprises.
- **Essentiel** : ce dont workbookIA a besoin, avec les démonstrations qui éclairent et les exercices de calcul centraux ; les démonstrations longues, les variantes et les sections « pour aller plus loin » sont hors parcours. Les corrigés des exercices hors parcours restent lisibles.
- Chaque exercice porte ses parcours ; examens blancs et projet de synthèse appartiennent aux deux.

## 13. Types d'exercices

Les types de workbookIA, avec deux ajouts pour un dépôt de maths (🔗 et 📖) et une composition revue : ici le papier domine.

| Icône | Type | Où |
|---|---|---|
| 🧠 | Quiz de lecture (QCM, vrai/faux justifié, contre-exemple) | 02_exercices |
| 🔁 | Rappel espacé | 02_exercices |
| ✏️ | Calcul à la main | 02_exercices (vérifié dans la partie 0 du notebook) |
| ∂ | Démonstration ou dérivation | 02_exercices |
| 🔗 | **Pont vers workbookIA** : appliquer la notion à un calcul du type de ceux du chapitre suivant de workbookIA (une loss, une couche, une métrique), sans en reprendre les exercices | 02_exercices ou notebook |
| 📖 | **Lecture guidée de MML** : questions sur une section du livre, vocabulaire anglais, refaire un exemple du livre avec ses propres nombres | 02_exercices |
| 🔨 | Implémentation from scratch (dans `mymath`) | notebook |
| 📦 | Vérifier ou explorer avec une bibliothèque (NumPy, SymPy, SciPy) | notebook |
| 🔬 | Expérience numérique (faire varier, tracer, conclure) | notebook |
| 🔮 | Prédire avant d'exécuter | notebook |
| 🐛 | Chasse à l'erreur : calcul ou code piégé à corriger | 02 ou notebook |
| 📈 | Lire un graphique | 02 ou notebook |
| 🎨 | Visualiser une notion (une application linéaire sur le cercle unité, une densité, des lignes de niveau) | notebook |
| 🧮 | Estimation de Fermi, ordre de grandeur | 02_exercices |
| 🗣️ | Explication façon Feynman | 02_exercices |
| ⚖️ | Esprit critique (statistiques trompeuses, paradoxe de Simpson…), là où c'est pertinent | 02_exercices |
| 🏆 | Défi à objectif chiffré | notebook |
| 💼 | Question d'entretien sur les maths du ML (à partir de la partie I) | 02_exercices |
| 🛠️ | Compétence pro (LaTeX propre, vérifier un calcul avec SymPy, test unitaire, docstring) | notebook ou 02 |

**Composition d'un chapitre de 10 à 16 h** (écarts justifiés dans le syllabus) : 🧠 6–10 · 🔁 3 · ✏️/∂ 10–20 · 🔗 1–3 · 📖 1–2 quand le chapitre a des sections de MML · 🔨/📦 4–8 · 🔬/🔮 ≥ 2 · 🐛 ≥ 1 · 🎨 ≥ 1 · 🗣️ 1 · 💼 1–3 à partir de la partie I · 🛠️ 1 · 🏆 1 à partir de la partie I · flashcards 15–30. Un chapitre court (6 à 8 h) en garde environ la moitié, papier d'abord.

Difficulté (★ à ★★★★), en-tête des exercices, ID stables, rappels espacés (dont un rappel tiré du chapitre de workbookIA précédent quand il a utilisé la notion) : comme workbookIA, règles recopiées en session 1.

## 14. Modèles de fichiers et vérification

**Fichiers d'un chapitre** : ceux de workbookIA (`01_fiche` → `flashcards.csv`), mêmes rubriques, avec ces adaptations :
- **La fiche est le cours.** Pour chaque notion : intuition, définition, **exemple chiffré refait à la main**, figure, propriété, démonstration (repliée dans un bloc `<details>` quand elle est longue), lien avec le ML. Quand le chapitre a des sections de MML, un **guide de lecture** dit quelles sections lire, dans quel ordre, avec quel vocabulaire, et ce qu'on peut survoler.
- La fiche se termine par **« Et maintenant, dans workbookIA »** : ce que le chapitre suivant de workbookIA fera de ces notions, sans en dévoiler les exercices.
- **Exercices papier vérifiables** : la partie 0 de chaque notebook vérifie les réponses des ✏️ (valeurs, fractions, vecteurs, matrices, expressions).
- **Indices** (3 niveaux) et **solutions** (réponse, démarche, erreurs fréquentes, variante avec sa réponse) : mêmes règles que workbookIA. Une solution de ∂ donne en plus une **grille de relecture** (ce qu'une démonstration correcte doit contenir), pour que l'apprenant juge la sienne.
- Flashcards : format Anki de workbookIA, tags `mwb::<id>::concept`, deck distinct de celui de workbookIA.

**`wbm.check`** : le mécanisme de workbookIA (empreinte SHA-256 salée par l'ID, messages pédagogiques sans révéler la réponse, `answers.json` construit depuis les solutions exécutées), avec trois extensions pour les maths :
1. **fractions exactes** : `"3/4"`, `Fraction(3, 4)` et `0.75` sont acceptés quand l'énoncé le dit ; une fraction non simplifiée reçoit un message dédié ;
2. **expressions** : `wbm.check_expr("R7.5", "2*x*exp(x**2)")` lit l'expression avec SymPy et compare ses valeurs en des points fixés aux empreintes des valeurs attendues ; deux expressions équivalentes passent, la bonne expression n'est jamais stockée en clair ;
3. **ensembles et intervalles** : une liste de solutions dans le désordre, un intervalle écrit `[2, 5[` ou `(2, 5]` selon la convention annoncée.

Les démonstrations ∂ ne se vérifient pas automatiquement : grille de relecture dans les solutions, puis correction par Claude sur demande (en lecture seule de `mon_travail/`).

## 15. Encadrés standard

Ceux de workbookIA (📐, 🧮 rappel, ⚠️ piège, 🔗 lien, 💼 en entreprise), avec ces adaptations :
- 🔗 **Dans workbookIA** — où la notion sert, avec le chapitre et l'usage (« au ch. 18, la rétropropagation applique exactement cette règle de la chaîne »).
- 📖 **Dans MML** — section, vocabulaire anglais, ce qui diffère des notations de la fiche.
- ⚠️ **Erreur de calcul classique** — par exemple $(a+b)^2 \ne a^2 + b^2$, $\ln(a+b) \ne \ln a + \ln b$, $\mathbf{AB} \ne \mathbf{BA}$ ; elles sont recensées dans `annexes/erreurs_frequentes.md`.
- Pas d'encadré 🕰️ « mise à jour » : les mathématiques ne se périment pas ; un encadré 💻 **Aujourd'hui en pratique** dit comment le calcul se fait en vrai (NumPy appelle LAPACK, personne n'inverse une matrice pour résoudre un système…).

## 16. Règles pédagogiques

Celles de workbookIA (un objectif par exercice, aucune notion avant d'être vue, difficulté croissante, intuition + maths + code, pas de remplissage), plus :
1. **Prêt pour le chapitre suivant** : chaque notion mathématique d'un chapitre de workbookIA est enseignée dans un chapitre de maths qui le précède (vérifié par `syllabus.py check` grâce aux notions requises de workbookIA, lues en lecture seule).
2. **Pas de doublon, pas de fuite** : la règle de partage du §8.
3. **Le concret d'abord** : un exemple en dimension 2 ou avec de petits nombres avant le cas général.
4. **Une figure par notion géométrique**, calculée par un script (`tools/chapters/figures_<id>.py`), jamais copiée d'un livre.
5. **Calcul à la main avant l'ordinateur** : le notebook vérifie, il ne remplace pas.
6. **Démonstrations dosées** : on démontre ce qui fait comprendre ; une démonstration hors parcours essentiel est signalée.
7. **Rédaction** : apprendre à rédiger une démonstration courte (hypothèses, étapes justifiées, conclusion) dès R4.
8. **Erreurs de calcul** : chaque chapitre de la partie 0 a ses 🐛 sur les erreurs classiques, pour les reconnaître dans son propre travail.

## 17. Volet reconversion

- 💼 : questions d'entretien qui portent sur les maths du ML (« pourquoi la cross-entropy est-elle une log-vraisemblance ? », « que dit le conditionnement d'une matrice ? »), avec réponse modèle en 60 secondes.
- Pas de mini-projet par partie : ceux de workbookIA, faits juste après, sont l'endroit où ces maths s'appliquent, et doubler les projets alourdirait le rythme commun.
- Projet de synthèse : un notebook-article qui montre qu'on sait dériver, implémenter et vérifier.

## 18. Examens blancs, positionnement et projet de synthèse

- **Examens blancs** (dans `checkpoints/partie_X/`) : comme ceux de workbookIA (60 à 120 min, sur 20, corrigé détaillé, barème), avec une synthèse d'une page et une carte mentale ; types et étoiles selon les règles de workbookIA.
- **Test de positionnement** (`positionnement/`) : une heure trente à trois heures, vérifié par `wbm.check` ; la grille dit, pour chaque chapitre de la partie 0, « à faire », « à survoler » ou « tu peux sauter » (et quels exercices faire quand même).
- **Projet de synthèse** (`projets/projet_synthese/`) : cahier des charges, grille sur 20, exemple rédigé sur un algorithme hors liste, kit de départ.

## 19. Suivi

Comme workbookIA : `suivi/PROGRESS.md` (tenu par Claude), modèles du tableau de bord (dans l'ordre de travail commun du §9), du journal et de l'auto-évaluation copiés dans `mon_travail/suivi/` par `start_chapter.py --init`.

## 20. Définition du « terminé » pour un chapitre

- [ ] Les 8 fichiers du chapitre sont présents et conformes au §14 ; figures générées par script.
- [ ] Composition du §13 respectée (ou écart justifié) ; les sections de MML visées sont couvertes par au moins un exercice.
- [ ] Toutes les notions mathématiques du chapitre de workbookIA préparé sont enseignées ici ou avant ; aucun exemple, donnée ni réponse de ses exercices n'est repris.
- [ ] `05_solutions.ipynb` s'exécute en entier sur CPU en moins de 5 minutes, sorties conservées ; `03_notebook.ipynb` passe « Run all » sans planter.
- [ ] `pytest --impl=ref` vert ; les tests échouent sur les stubs.
- [ ] `answers.json` régénéré ; chaque vérification passe avec la bonne valeur et échoue avec une mauvaise.
- [ ] ✏️, ∂ et 🧮 re-résolus à l'aveugle par un vérificateur indépendant (sous-agent) ; un second joue l'apprenant sur le notebook.
- [ ] Aucun passage recopié de MML ni d'un autre livre.
- [ ] Glossaire, symboles, formulaire, correspondances, tableau de bord et `PROGRESS.md` à jour ; commit « <id>: … ».

## 21. Sources externes

Documentation officielle (NumPy, SciPy, SymPy), livres libres du §3, cours reconnus. Chaque lien est vérifié avant d'être cité.

## 22. Versions figées

*À remplir en session 1* : même politique que workbookIA (versions préinstallées sur Colab, revérifiées à chaque examen blanc). Paquets : Python, numpy, scipy, sympy, matplotlib, pandas, scikit-learn, pytest, nbformat, nbclient, jupyterlab (local), genanki (facultatif). Les versions communes avec workbookIA restent identiques aux siennes, pour que les deux dépôts partagent un environnement.

## 23. Relation avec workbookIA et déroulé de la génération

- workbookIA n'est **jamais modifié** par les sessions de ce dépôt : il est seulement lu, pour connaître les notions requises par chacun de ses chapitres et pour éviter les doublons et les fuites.
- En session 1, l'outillage de workbookIA (`wb`, `start_chapter.py`, `build_answers.py`, `run_all_notebooks.py`, `export_flashcards.py`, `syllabus.py`, `nbbuild.py`, kit des constructeurs de chapitres, tests d'infrastructure) est **copié puis adapté** : renommage `wb` → `wbm` et `mylearn` → `mymath`, ID du §8, deux parcours, ordre de travail commun, extensions de `wbm.check` (§14). Les décisions d'outillage de la BIBLE de workbookIA (son §22) qui s'appliquent ici sont recopiées dans le §24, pour que ce dépôt se suffise à lui-même.
- **Déroulé** (≈ 70 sessions) : session 1, mise en place (outillage, versions, ressources vérifiées, `CLAUDE.md`) ; session 2, syllabus détaillé à relire ; puis les chapitres **dans l'ordre de travail commun** (la partie 0 d'abord, pour que l'apprentissage commence vite), une ou deux sessions chacun, l'examen blanc à la fin de chaque partie, le test de positionnement juste après la partie 0, des audits après les parties 0, II et IV, et une session de finalisation. La génération garde une avance sur l'étude.

## 24. Journal des décisions et dérogations

| Date | Décision | Raison |
|---|---|---|
| 2026-11-05 | Départ « lycée lointain », profondeur « maths du ML », format de workbookIA, MML comme fil conducteur. | Choix de l'apprenant. |
| 2026-11-05 | Package `wbm` et librairie `mymath`. | Installer les deux dépôts dans le même environnement. |
| 2026-11-05 | Pas de PyTorch ; SymPy ajouté. | Les oracles du calcul symbolique et de la différentiation automatique viennent de SymPy ; installation plus légère. |
| 2026-11-05 | Deux parcours (complet, essentiel). | La distinction utile est « ce dont workbookIA a besoin » ou « tout ». |
| 2026-11-06 | Dépôt `cemah2/workbookMaths` ; temps sans limite, parcours complet par défaut. | Réponses de l'apprenant. |
| 2026-11-06 | **Plan calé sur workbookIA** : partie 0 pendant 0A, puis un ou plusieurs chapitres de maths juste avant chaque chapitre de workbookIA, numérotés comme lui (R0–R9, M02a…, MB8). Remplace le plan par grands thèmes de la v0. | Demande de l'apprenant : suivre les deux workbooks en même temps. |
| 2026-11-06 | MML suivi dans l'ordre de workbookIA, donc dans le désordre ; il est couvert en entier. | Conséquence de l'ordre commun. |
| 2026-11-06 | Pas de mini-projet par partie ; examen blanc et synthèse seulement, juste avant le checkpoint de workbookIA. Projet de synthèse en fin de parcours. | Les mini-projets de workbookIA appliquent déjà ces maths ; garder un rythme commun tenable. |
| 2026-11-06 | Lecture de MML intégrée au travail (un bloc du livre, puis la fiche, puis les exercices), comme Glassner dans workbookIA ; spécification v1 validée. | Choix de l'apprenant. |
