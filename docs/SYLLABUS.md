# SYLLABUS — workbookMaths

*Généré par `python tools/syllabus.py build` à partir de `docs/syllabus/data/` : ne pas modifier à la main.*

Le contrat du workbook : pour chaque chapitre, ses notions, ses prérequis, les sections de MML, le chapitre de workbookIA qu'il prépare et le module `mymath` ; pour une partie **détaillée**, chaque exercice. Les exercices d'une partie sont détaillés dans une session de syllabus juste avant sa génération (BIBLE §24, 2026-11-06), pour profiter des retours d'étude des parties précédentes.

## Conventions

- **ID** : `R1.4` (exercice), `R1.Q2` (quiz), `R1.R1` (rappel), `M12c.E1` (entretien) ; stables une fois publiés.
- **★** : ★ application directe (5–15 min) · ★★ standard (15–30 min) · ★★★ approfondi (30–90 min) · ★★★★ défi.
- **Parcours** : C = complet (tout) ; E = essentiel (ce dont workbookIA a besoin).
- **Vérification** : `wbm` (`wbm.check` dans le notebook, partie 0 pour les calculs papier), `pytest` (tests de `mymath`), `manuel` (solutions et grille de relecture).
- **Types** : 🧠 quiz · 🔁 rappel · ✏️ calcul à la main · ∂ démonstration · 🔗 pont vers workbookIA · 📖 lecture de MML · 🔨 from scratch (mymath) · 📦 avec une bibliothèque · 🔬 expérience · 🔮 prédire · 🐛 chasse à l'erreur · 📈 lire un graphique · 🎨 visualiser · 🧮 Fermi · 🗣️ Feynman · ⚖️ esprit critique · 🏆 défi · 💼 entretien · 🛠️ compétence pro.

## Vue d'ensemble

| Chapitre | Titre | Prépare (workbookIA) | MML | Durée | Détail | Sessions |
|---|---|---|---|---|---|---|
| [R0](#r0) | Prise en main | 0B | — | 3,2 h | ✅ exercices | 1 |
| [POS](#pos) | Test de positionnement | — | — | 2,1 h | ✅ exercices | 1 |
| [R1](#r1) | Nombres et calcul | 0B | — | 12,7 h | ✅ exercices | 1 |
| [R2](#r2) | Calcul littéral et équations | 0B | — | 13,6 h | ✅ exercices | 1 |
| [R3](#r3) | Fonctions | 0B | — | 12,8 h | ✅ exercices | 1 |
| [R4](#r4) | Logique, ensembles, Σ et Π | 0B | — | 13,2 h | ✅ exercices | 1 |
| [R5](#r5) | Suites | 0B | — | 10,2 h | ✅ exercices | 1 |
| [R6](#r6) | Exponentielle et logarithmes | 0B | — | 10,4 h | ✅ exercices | 1 |
| [R7](#r7) | Limites et dérivation | 0B | — | 13,2 h | ✅ exercices | 2 |
| [R8](#r8) | Probabilités de base | 0B | — | 10,9 h | ✅ exercices | 1 |
| [R9](#r9) | Géométrie du plan, vecteurs et trigonométrie | 0B | — | 11,0 h | ✅ exercices | 1 |
| [CP0](#cp0) | Bilan de remise à niveau | 0B | — | 3,3 h | ✅ exercices | 1 |
| [M02a](#m02a) | Intégrales et densités | 2 | (prérequis de §6.2) | 12,6 h | ✅ exercices | 1 |
| [M02b](#m02b) | Variables aléatoires et lois usuelles | 2 | §6.1, §6.2, §6.4, §6.7 | 13,9 h | ✅ exercices | 1 |
| [M02c](#m02c) | Échantillons et estimation | 2 | §6.4 | 13,8 h | ✅ exercices | 1 |
| [M03](#m03) | Probabilités conditionnelles | 3 | §6.3 | 12,8 h | ✅ exercices | 1 |
| [M04](#m04) | Bayes, vraisemblance et loi Beta | 4 | §6.3, §6.6, §8.3 | 12,9 h | ✅ exercices | 1 |
| [M05a](#m05a) | Dérivées, Taylor et calcul numérique | 5 | §5.1 | 13,5 h | ✅ exercices | 1 |
| [M05b](#m05b) | Fonctions de plusieurs variables et gradient | 5 | §5.2 | 13,3 h | ✅ exercices | 1 |
| [M06](#m06) | Théorie de l'information | 6 | — | 11,4 h | ✅ exercices | 1 |
| [CP1](#cp1) | Examen blanc de la partie I | — | — | 3,3 h | ✅ exercices | 1 |
| [M07](#m07) | Vecteurs et géométrie de ℝⁿ | 7 | §3.1, §3.2.1, §3.3, §3.4 | 15,3 h | ✅ exercices | 1 |
| [M08](#m08) | Tests statistiques | 8 | §8.6 | 12,1 h | ✅ exercices | 1 |
| [M09a](#m09a) | Matrices et systèmes linéaires | 9 | §2.1, §2.2, §2.3 | 16,7 h | ✅ exercices | 2 |
| [M09b](#m09b) | Moindres carrés et régularisation | 9 | §5.5, §8.1, §8.2, §9.1, §9.2 | 17,0 h | ✅ exercices | 2 |
| [M10](#m10) | Séparabilité linéaire et convexité | 10 | §12.1 | 8,1 h | ✅ exercices | 1 |
| [M11](#m11) | Logique, induction et inégalités de concentration | 11 | — | 11,5 h | ✅ exercices | 1 |
| [CP2](#cp2) | Examen blanc de la partie II | — | — | 3,2 h | ✅ exercices | 1 |
| [M12a](#m12a) | Espaces vectoriels et applications linéaires | 12 | §2.4, §2.5, §2.6, §2.7, §2.8 | 16,6 h | ✅ exercices | 2 |
| [M12b](#m12b) | Orthogonalité et projections | 12 | §3.2.2, §3.2.3, §3.5, §3.6, §3.7, §3.8, §9.4 | 15,2 h | ✅ exercices | 1 |
| [M12c](#m12c) | Valeurs propres et matrices symétriques | 12 | §4.1, §4.2, §4.3, §4.4 | 16,8 h | ✅ exercices | 2 |
| [M12d](#m12d) | SVD et analyse en composantes principales | 12 | §4.5, §4.6, §4.7, §10.1, §10.2, §10.3, §10.4, §10.5, §10.6 | 18,0 h | ✅ exercices | 2 |
| [M13a](#m13a) | Vraisemblance et régression logistique | 13 | §8.3 | 14,4 h | ✅ exercices | 2 |
| [M13b](#m13b) | Optimisation sous contraintes et SVM | 13 | §7.2, §7.3, ch. 12 | 16,1 h | ✅ exercices | 2 |
| [M14](#m14) | Les maths des ensembles | 14 | — | 7,2 h | ✅ exercices | 1 |
| [CP3](#cp3) | Examen blanc de la partie III | — | — | 3,1 h | ✅ exercices | 1 |
| [M16](#m16) | Applications affines, graphes et variance d'un produit | 16 | — | 8,0 h | ✅ exercices | 1 |
| [M17](#m17) | Jacobienne et règle de la chaîne | 17 | §5.3 | 10,2 h | ✅ exercices | 1 |
| [M18](#m18) | Différentiation automatique et calcul matriciel | 18 | §5.4, §5.5, §5.6 | 14,6 h | ✅ exercices | 1 |
| [M19](#m19) | Hessienne, conditionnement et convergence | 19 | §5.7, §5.8, §7.1 | 14,2 h | ✅ exercices | 1 |
| [M20](#m20) | Tenseurs, axes et estimateurs pondérés | 20 | — | 8,8 h | ✅ exercices | 1 |
| [CP4](#cp4) | Examen blanc de la partie IV | — | — | 3,1 h | ✅ exercices | 1 |
| [M21](#m21) | Convolution, matrices de Toeplitz et équivariance | 21 | — | 14,8 h | ✅ exercices | 1 |
| [M22](#m22) | Récurrences vectorielles, rayon spectral et normes de matrices | 22 | (§4.2) | 15,6 h | ✅ exercices | 1 |
| [CP5](#cp5) | Examen blanc de la partie V | — | — | 3,1 h | ✅ exercices | 1 |
| [M25a](#m25a) | Gaussienne multivariée, conditionnement et divergence KL | 25 | §6.5, §6.7, §9.3 | 20,3 h | ✅ exercices | 2 |
| [M25b](#m25b) | Variables latentes et ELBO | 25 | §8.4, §8.5, §10.7, ch. 11 | 21,1 h | ✅ exercices | 2 |
| [M26](#m26) | Chaînes de Markov et équation de Bellman | 26 | — | 17,9 h | ✅ exercices | 1 |
| [M27](#m27) | Jeux et distances entre lois | 27 | §7.2 | 18,7 h | ✅ exercices | 1 |
| [M28](#m28) | Matrice de Gram, montée sur l'entrée et lois tronquées | 28 | — | 13,6 h | ✅ exercices | 1 |
| [CP6](#cp6) | Examen blanc de la partie VI | — | — | 3,1 h | ✅ exercices | 1 |
| [MB2](#mb2) | Cooccurrences, PMI et embeddings | B2 | — | 13,2 h | ✅ exercices | 1 |
| [MB3](#mb3) | Rotations, moyennes pondérées et softmax en ligne | B3 | §3.9 | 14,8 h | ✅ exercices | 1 |
| [MB4](#mb4) | Rang faible et recherche d'information | B4 | (§4.6) | 9,0 h | ✅ exercices | 1 |
| [MB5](#mb5) | Les maths de la diffusion | B5 | (§6.5) | 16,6 h | ✅ exercices | 2 |
| [MB6](#mb6) | Shapley, intégrales de chemin et équité | B6 | — | 13,0 h | ✅ exercices | 1 |
| [MB8](#mb8) | Gradient de politique | B8 | — | 14,8 h | ✅ exercices | 1 |
| [PS](#ps) | Projet de synthèse | — | — | 27,3 h | ✅ exercices | 1 |

## Totaux par partie

| Partie | Chapitres | Exercices détaillés | Durée (complet) | Durée (essentiel) |
|---|---|---|---|---|
| 0 · Remise à niveau | 12 | 363 | 116,5 h | 93,3 h |
| I · Fondations | 9 | 319 | 107,6 h | 69,7 h |
| II · Concepts | 7 | 256 | 83,9 h | 54,0 h |
| III · ML classique | 8 | 321 | 107,5 h | 71,2 h |
| IV · Réseaux | 6 | 182 | 58,8 h | 41,9 h |
| V · Architectures | 3 | 94 | 33,5 h | 25,9 h |
| VI · Génératif et RL | 6 | 203 | 94,7 h | 70,8 h |
| VII · Bonus | 6 | 182 | 81,5 h | 62,7 h |
| fin · Fin | 1 | 10 | 27,3 h | 27,3 h |

<a id="r0"></a>
## R0 · Prise en main

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r0_prise_en_main/` · **MML** — · **sessions de génération** 1

Les outils du workbook, sans maths nouvelles : le notebook, Python comme calculatrice, taper une réponse (un nombre, une fraction, une expression, un intervalle) et la faire vérifier par `wbm.check`, SymPy pour vérifier un calcul à la main, LaTeX pour écrire une formule, et la première fonction de ta librairie `mymath`. Se fait en même temps que le début du chapitre 0A de workbookIA, qui enseigne Python en profondeur.

**Temps** : 3,2 h en parcours complet, 2,8 h en parcours essentiel (lecture 45 min, 10 flashcards).

**Objectifs**

- Exécuter un notebook du dépôt et y écrire tes réponses.
- Calculer avec Python en respectant ses priorités (`**`, `//`, `%`), et savoir pourquoi 0,1 + 0,2 n'y vaut pas exactement 0,3.
- Taper un nombre, une fraction, une expression et un intervalle pour `wbm.check`.
- Vérifier un développement ou une simplification avec SymPy.
- Écrire une formule en LaTeX dans une cellule Markdown.
- Écrire une fonction de `mymath` et lancer ses tests.

**Sections de la fiche**

- §1 Le notebook du dépôt
- §2 Python comme calculatrice
- §3 Taper une réponse et la faire vérifier
- §4 SymPy : vérifier un calcul à la main
- §5 Écrire une formule en LaTeX
- §6 Un premier graphique
- §7 Ta librairie mymath et ses tests

**Notions enseignées** : cellules, exécution, « Run all » · priorités en Python (`**`, `//`, `%`) · nombres flottants (0,1 + 0,2) · saisie d'une fraction, d'une expression, d'un intervalle · `wbm.check` · SymPy (expand, simplify, subs) · LaTeX dans Markdown · tracer une courbe (recette : np.linspace et plt.plot) · mymath et pytest : lancer les tests, lire un échec, écrire un assert

**Python (workbookIA 0A, à avoir fait avant)** : §100.1.1 Cellules de code et Markdown, noyau, ordre d'exécution, « Tout exécuter » · §100.2.1 Nombres, opérateurs arithmétiques, booléens et None · §100.2.2 Chaînes de caractères et f-strings · §100.3.1 Listes : indices, tranches, méthodes, mutabilité · §100.4.1 Conditions : if, elif, else, opérateurs logiques · §100.5.1 Définir une fonction : paramètres, valeurs par défaut, return, portée

**mymath** : `_example.py` (signatures figées) : `mean`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R0.Q1 | 🧠 | Le notebook : cellules, ordre d'exécution, « Run all » | ★ | 3 | §1 | C, E | manuel | — |
| R0.Q2 | 🧠 | Python calculatrice : `**` ou `^`, `//` ou `%` | ★ | 3 | §2 | C, E | manuel | — |
| R0.Q3 | 🧠 | Taper une réponse : fraction, expression, intervalle | ★ | 3 | §3 | C, E | manuel | — |
| R0.Q4 | 🧠 | SymPy et LaTeX : vrai ou faux | ★ | 3 | §4 §5 | C | manuel | — |
| R0.1 | ✏️ | Calculer avec Python : priorités, division entière et reste | ★ | 10 | §2 | C, E | wbm | — |
| R0.2 | 🗣️ | Expliquer à quoi sert `wbm.check`, et pourquoi il ne montre jamais la réponse | ★ | 10 | §3 | C | manuel | — |
| R0.3 | 📦 | Taper une fraction exacte, une expression et un intervalle | ★ | 10 | §3 | C, E | wbm | — |
| R0.4 | 🔮 | Prédire : 0,5 + 0,25 et dix fois 0,1, exacts ou arrondis ? | ★ | 10 | §2 | C, E | wbm | — |
| R0.5 | 📦 | Vérifier un développement avec SymPy (expand, simplify) | ★ | 15 | §4 | C, E | wbm | — |
| R0.6 | 🐛 | Chasse à l'erreur : `x^2` et `2x` en Python | ★ | 10 | §2 §4 | C, E | wbm | — |
| R0.7 | 🎨 | Tracer une fonction avec matplotlib | ★ | 10 | §6 | C | manuel | — |
| R0.8 | 🛠️ | Écrire trois formules en LaTeX dans ta feuille de réponses | ★ | 15 | §5 | C, E | manuel | — |
| R0.9 | 🔨 | Ta première fonction : la moyenne (`mean`) · `mean` | ★ | 25 | §7 | C, E | pytest | — |

*Notes* : COMPOSITION : chapitre d'outils de 3 h, sans calcul nouveau (un seul ✏️, pas de ∂ ni de 🔁). `mean` est la fonction d'exemple de `templates/mymath_stubs/_example.py` (fichier de base, déjà publié) : la fiche et les indices de R0.9 disent de tester une liste vide avec `len(values) == 0` (`if not values` échoue sur un tableau NumPy, que les tests lui passent). Recettes minimales, que workbookIA 0A approfondit plus tard : §6 `np.linspace` et `plt.plot` (0A §100.8, §100.10), §7 `raise ValueError(...)`, lancer pytest et écrire un `assert` (0A §100.6.2, §100.11.3). Elles suffisent aux graphiques et aux tests 🛠️ de la remise à niveau.

<a id="pos"></a>
## POS · Test de positionnement

**Partie** 0 · **prépare** — · **dossier** `positionnement/` · **MML** — · **sessions de génération** 1

Le test de positionnement : deux exercices par chapitre de R1 à R9, vérifiés par `wbm.check`, et une grille qui dit pour chaque chapitre « à faire », « à survoler » ou « tu peux sauter » (avec les exercices à faire quand même). À passer juste après R0 (qui apprend à taper une fraction, une expression ou un intervalle dans `wbm.check`), sans préparation : il mesure ce qui reste, pas ce qu'on peut réviser en une soirée.

**Temps** : 2,1 h en parcours complet, 2,1 h en parcours essentiel (lecture 10 min, 0 flashcards).

**Objectifs**

- Savoir quels chapitres de la remise à niveau tu peux sauter, survoler ou dois faire en entier.
- Repérer tes erreurs de calcul récurrentes avant de commencer.

**Sections de la fiche**

- §R1 Nombres et calcul
- §R2 Calcul littéral et équations
- §R3 Fonctions
- §R4 Logique, ensembles, Σ et Π
- §R5 Suites
- §R6 Exponentielle et logarithmes
- §R7 Limites et dérivation
- §R8 Probabilités de base
- §R9 Géométrie du plan, vecteurs et trigonométrie

**Notions enseignées** : aucune notion nouvelle : un diagnostic

**Prérequis** : taper une réponse dans wbm.check (R0)

**Python (workbookIA 0A, à avoir fait avant)** : §100.1.1 Cellules de code et Markdown, noyau, ordre d'exécution, « Tout exécuter » · §100.2.1 Nombres, opérateurs arithmétiques, booléens et None

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| POS.1 | ✏️ | Calculer avec des priorités et des fractions | ★ | 6 | §R1 | C, E | wbm | — |
| POS.2 | ✏️ | Puissances, racines et notation scientifique | ★ | 6 | §R1 | C, E | wbm | — |
| POS.3 | ✏️ | Développer, factoriser, résoudre une équation et une inéquation | ★ | 7 | §R2 | C, E | wbm | — |
| POS.4 | ✏️ | Un système de deux équations à deux inconnues | ★★ | 8 | §R2 | C, E | wbm | — |
| POS.5 | 📈 | Lire un graphique de fonction | ★ | 5 | §R3 | C, E | wbm | — |
| POS.6 | ✏️ | Racines et sommet d'un polynôme du second degré | ★★ | 8 | §R3 | C, E | wbm | — |
| POS.7 | ✏️ | Sommes avec Σ, somme double et produit avec Π | ★ | 7 | §R4 | C, E | wbm | — |
| POS.8 | ✏️ | La négation d'une phrase avec « pour tout » | ★ | 5 | §R4 | C, E | wbm | — |
| POS.9 | ✏️ | Terme et somme d'une suite géométrique | ★ | 6 | §R5 | C, E | wbm | — |
| POS.10 | ✏️ | Une suite définie par récurrence : premiers termes et limite | ★ | 6 | §R5 | C, E | wbm | — |
| POS.11 | ✏️ | Propriétés de l'exponentielle et du logarithme | ★ | 5 | §R6 | C, E | wbm | — |
| POS.12 | ✏️ | Résoudre des équations avec exp et ln | ★ | 6 | §R6 | C, E | wbm | — |
| POS.13 | ✏️ | Dériver trois fonctions, dont une composée | ★ | 7 | §R7 | C, E | wbm | — |
| POS.14 | ✏️ | Tangente, variations et une limite | ★★ | 10 | §R7 | C, E | wbm | — |
| POS.15 | ✏️ | Une probabilité avec un arbre | ★ | 6 | §R8 | C, E | wbm | — |
| POS.16 | ✏️ | L'espérance et la variance d'une variable aléatoire | ★ | 6 | §R8 | C, E | wbm | — |
| POS.17 | ✏️ | Distance et produit scalaire dans le plan | ★ | 6 | §R9 | C, E | wbm | — |
| POS.18 | ✏️ | Cosinus d'un angle et radians | ★ | 5 | §R9 | C, E | wbm | — |

*Notes* : Fichiers : README.md (mode d'emploi), 01_sujet.md, 02_notebook.ipynb (réponses vérifiées, grille calculée), 03_corrige.md (où chaque question est enseignée), 03_solutions.ipynb, 04_mes_reponses.md, 05_grille.md (deux exercices par chapitre ; seuils : 2/2 → tu peux sauter, 1/2 → survoler la fiche et faire les exercices E, 0/2 → chapitre complet). Généré juste après R0, avant R1, pour être prêt quand l'apprenant en a besoin ; il vise les notions de la partie 0 telles que ce syllabus les fixe.

<a id="r1"></a>
## R1 · Nombres et calcul

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r1_nombres_calcul/` · **MML** — · **sessions de génération** 1

Le calcul sur les nombres, du collège à la seconde : les ensembles de nombres, les priorités, les fractions, les puissances et les racines, la notation scientifique et les arrondis, les pourcentages et les évolutions successives, les moyennes pondérées. Tout ce que le chapitre 0B de workbookIA suppose sans le dire, avec ses pièges classiques.

**Temps** : 12,7 h en parcours complet, 9,7 h en parcours essentiel (lecture 135 min, 25 flashcards).

**Objectifs**

- Calculer sans erreur avec des priorités, des nombres négatifs et des fractions, à la main puis en vérifiant avec Python.
- Appliquer les règles des puissances (exposants négatifs compris) et des racines carrées, et repérer les « règles » qui n'existent pas.
- Écrire un nombre en notation scientifique, l'arrondir à un nombre de chiffres significatifs et donner son ordre de grandeur.
- Calculer une évolution en pourcentage, des évolutions successives et une évolution réciproque.
- Calculer une moyenne pondérée, et reconnaître la somme pondérée qui fait le calcul d'un neurone.
- Estimer un ordre de grandeur à la manière de Fermi.

**Sections de la fiche**

- §1 Les ensembles de nombres et la droite numérique
- §2 Priorités, nombres négatifs et distributivité
- §3 Fractions
- §4 Puissances
- §5 Racines carrées
- §6 Notation scientifique, ordres de grandeur et arrondis
- §7 Proportionnalité et pourcentages
- §8 Moyennes
- §9 Estimations de Fermi

**Notions enseignées** : ℕ, ℤ, ℚ, ℝ et la droite numérique · priorités des opérations · nombres négatifs · distributivité · fractions : simplifier, additionner, multiplier, diviser, comparer · PGCD · puissances entières et leurs règles · puissances de 10 · racines carrées · notation scientifique · chiffres significatifs, arrondis · partie entière ⌊x⌋ et ⌈x⌉ · ordres de grandeur · proportionnalité · pourcentages et coefficients multiplicateurs · évolutions successives et réciproques · moyenne, moyenne pondérée, somme pondérée · moyenne harmonique (aperçu) · estimation de Fermi

**Prérequis** : taper une fraction pour wbm.check (R0)

**Python (workbookIA 0A, à avoir fait avant)** : §100.3.1 Listes : indices, tranches, méthodes, mutabilité · §100.4.2 Boucles : for, range, enumerate, zip, while, break, continue · §100.5.5 Docstrings au format NumPy et annotations de type · §100.6.2 Exceptions : lire un traceback, raise, try/except

**mymath** : `arith.py` (signatures figées) : `gcd`, `simplify_fraction`, `add_fractions`, `scientific_notation`, `successive_changes`, `weighted_mean`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.1 ✏️ Puissances, racines et notation scientifique sans calculatrice

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R1.Q1 | 🧠 | Quel ensemble ? Entiers, décimaux, rationnels, réels | ★ | 4 | §1 | C, E | manuel | — |
| R1.Q2 | 🧠 | Priorités et signes : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| R1.Q3 | 🧠 | Fractions : quelles opérations sont justes ? | ★ | 4 | §3 | C, E | manuel | — |
| R1.Q4 | 🧠 | Règles des puissances : vrai ou faux | ★ | 4 | §4 | C, E | manuel | — |
| R1.Q5 | 🧠 | Racines carrées : vrai ou faux | ★ | 4 | §5 | C, E | manuel | — |
| R1.Q6 | 🧠 | Notation scientifique et chiffres significatifs | ★ | 4 | §6 | C, E | manuel | — |
| R1.Q7 | 🧠 | Les pièges des évolutions successives | ★ | 4 | §7 | C, E | manuel | — |
| R1.Q8 | 🧠 | Moyenne, moyenne pondérée, moyenne harmonique | ★ | 4 | §8 | C | manuel | — |
| R1.R1 | 🔁 | Taper une fraction et un intervalle pour `wbm.check` (R0) | ★ | 5 | §3 | C, E | manuel | — |
| R1.1 | ✏️ | Placer des nombres sur la droite numérique et les ranger | ★ | 10 | §1 | C, E | wbm | — |
| R1.2 | ✏️ | Calculer avec les priorités et les signes | ★ | 10 | §2 | C, E | wbm | — |
| R1.3 | ✏️ | Calcul mental avec la distributivité : 17 × 99, 23 × 101 | ★ | 10 | §2 | C | wbm | — |
| R1.4 | ✏️ | Simplifier des fractions avec le PGCD | ★ | 15 | §3 | C, E | wbm | — |
| R1.5 | ✏️ | Additionner, multiplier et diviser des fractions | ★★ | 20 | §3 | C, E | wbm | — |
| R1.6 | ✏️ | Comparer des fractions | ★ | 10 | §3 | C | wbm | — |
| R1.7 | ✏️ | Appliquer les règles des puissances | ★ | 15 | §4 | C, E | wbm | — |
| R1.8 | ✏️ | Puissances négatives et puissances de 10 | ★★ | 15 | §4 | C, E | wbm | — |
| R1.9 | ✏️ | Simplifier des racines carrées | ★ | 15 | §5 | C, E | wbm | — |
| R1.10 | ✏️ | Écrire en notation scientifique et arrondir | ★ | 10 | §6 | C, E | wbm | — |
| R1.11 | ✏️ | Partie entière, arrondi au plus proche, arrondi supérieur | ★ | 10 | §6 | C, E | wbm | — |
| R1.12 | ✏️ | Évolutions successives et évolution réciproque | ★★ | 20 | §7 | C, E | wbm | — |
| R1.13 | ✏️ | Règle de trois et proportionnalité | ★ | 10 | §7 | C | wbm | — |
| R1.14 | ✏️ | Moyenne pondérée : la note finale et la somme pondérée d'un neurone | ★★ | 15 | §8 | C, E | wbm | — |
| R1.15 | ∂ | Pourquoi a⁰ = 1 et a⁻ⁿ = 1/aⁿ : prolonger les règles des puissances | ★★ | 25 | §4 | C, E | manuel | — |
| R1.16 | ∂ | Pourquoi on n'additionne pas les dénominateurs | ★★ | 25 | §3 | C | manuel | — |
| R1.17 | 🔗 | Combien de paramètres, combien d'octets ? Un réseau en notation scientifique | ★★ | 20 | §6 | C, E | wbm | — |
| R1.18 | 🧮 | Fermi : combien de mots lis-tu dans une vie ? | ★★ | 20 | §9 | C | manuel | — |
| R1.19 | 🧮 | Fermi : la place que prend un dataset de photos | ★★ | 20 | §9 §6 | C, E | manuel | — |
| R1.20 | 🗣️ | Expliquer pourquoi +10 % puis −10 % ne ramène pas au départ | ★ | 10 | §7 | C, E | manuel | — |
| R1.21 | 🔨 | PGCD par l'algorithme d'Euclide et fraction irréductible · `gcd, simplify_fraction` | ★★ | 40 | §3 | C, E | pytest | — |
| R1.22 | 🔨 | Additionner deux fractions sans passer par les décimaux · `add_fractions` | ★★ | 30 | §3 | C, E | pytest | R1.21 |
| R1.23 | 🔨 | La notation scientifique à n chiffres significatifs · `scientific_notation` | ★★ | 40 | §6 | C | pytest | — |
| R1.24 | 🔨 | Évolutions successives et moyenne pondérée · `successive_changes, weighted_mean` | ★ | 30 | §7 §8 | C, E | pytest | — |
| R1.25 | 📦 | Calculer exactement avec `fractions.Fraction` | ★ | 10 | §3 | C, E | wbm | — |
| R1.26 | 🔮 | Prédire : arrondir deux fois, est-ce arrondir une fois ? | ★ | 10 | §6 | C | wbm | — |
| R1.27 | 🔬 | Après n hausses de 10 % : tracer et comparer à une hausse de 10n % | ★★ | 20 | §7 | C | wbm | — |
| R1.28 | 🐛 | Chasse à l'erreur : cinq calculs de fractions et de puissances | ★ | 15 | §3 §4 | C, E | wbm | — |
| R1.29 | 🐛 | Chasse à l'erreur : `-3**2` et les parenthèses | ★ | 10 | §2 | C, E | wbm | — |
| R1.30 | 🎨 | Les ordres de grandeur sur une échelle : de l'atome aux paramètres d'un LLM | ★ | 15 | §6 | C | manuel | — |
| R1.31 | 🛠️ | Écrire la docstring d'une fonction (format NumPy) | ★ | 15 | §8 | C | manuel | — |

*Notes* : Un seul 🔁 : seul R0 précède. Les nombres des exemples de la fiche ne reprennent aucun exercice de 0B (workbookIA).

<a id="r2"></a>
## R2 · Calcul littéral et équations

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r2_calcul_litteral/` · **MML** — · **sessions de génération** 1

Le calcul avec des lettres : réduire, développer, factoriser, les identités remarquables ; les équations et les inéquations du premier degré et leurs ensembles de solutions en intervalles ; la valeur absolue comme distance ; les systèmes de deux équations à deux inconnues, première rencontre avec l'algèbre linéaire ; et l'art de mettre un problème en équation.

**Temps** : 13,6 h en parcours complet, 10,1 h en parcours essentiel (lecture 150 min, 25 flashcards).

**Objectifs**

- Réduire, développer et factoriser une expression, identités remarquables comprises.
- Résoudre une équation et une inéquation du premier degré, et écrire l'ensemble des solutions avec des intervalles.
- Résoudre une équation avec une valeur absolue, en lisant |a − b| comme une distance.
- Résoudre un système 2 × 2 par substitution, par combinaison et par la formule de Cramer, et dire quand il a une seule solution.
- Mettre un problème concret en équation.

**Sections de la fiche**

- §1 Expressions littérales : substituer, réduire
- §2 Développer et factoriser
- §3 Identités remarquables
- §4 Équations du premier degré
- §5 Inéquations du premier degré et intervalles
- §6 Valeur absolue et fonction signe
- §7 Systèmes de deux équations à deux inconnues
- §8 Mettre un problème en équation

**Notions enseignées** : variables et expressions · substitution · réduire · développer · factoriser · identités remarquables · équation du premier degré · équation produit nul · inéquation du premier degré · intervalles, réunion, intersection · valeur absolue et distance · fonction signe · système linéaire 2 × 2 · substitution et combinaison · formule de Cramer, déterminant 2 × 2 (premier contact) · droite d'équation ax + by = c : la tracer avec deux points (lecture graphique d'un système) · mise en équation

**Prérequis** : fractions et priorités (R1) · puissances (R1)

**Python (workbookIA 0A, à avoir fait avant)** : §100.4.2 Boucles : for, range, enumerate, zip, while, break, continue · §100.6.2 Exceptions : lire un traceback, raise, try/except

**mymath** : `algebra.py` (signatures figées) : `solve_linear`, `solve_linear_inequality`, `solve_abs_equation`, `solve_2x2`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.21 ✏️ Identité, inverse 2 × 2 et système de deux équations

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R2.Q1 | 🧠 | Variables et substitution | ★ | 4 | §1 | C, E | manuel | — |
| R2.Q2 | 🧠 | Développer ou factoriser ? | ★ | 4 | §2 | C, E | manuel | — |
| R2.Q3 | 🧠 | Identités remarquables : vrai ou faux | ★ | 4 | §3 | C, E | manuel | — |
| R2.Q4 | 🧠 | Équations : quelles opérations sont permises ? | ★ | 4 | §4 | C, E | manuel | — |
| R2.Q5 | 🧠 | Inéquations : quand le sens change | ★ | 4 | §5 | C, E | manuel | — |
| R2.Q6 | 🧠 | Valeur absolue et distance | ★ | 4 | §6 | C | manuel | — |
| R2.Q7 | 🧠 | Une, aucune ou une infinité de solutions ? | ★ | 4 | §7 | C, E | manuel | — |
| R2.Q8 | 🧠 | Quelle équation pour ce problème ? | ★ | 4 | §8 | C | manuel | — |
| R2.R1 | 🔁 | Fractions et puissances (R1) | ★ | 5 | §1 | C, E | manuel | — |
| R2.R2 | 🔁 | Pourcentages et coefficients multiplicateurs (R1) | ★ | 5 | §8 | C | manuel | — |
| R2.R3 | 🔁 | Saisir un intervalle et une expression (R0) | ★ | 5 | §5 | C | manuel | — |
| R2.1 | ✏️ | Substituer et réduire | ★ | 10 | §1 | C, E | wbm | — |
| R2.2 | ✏️ | Développer | ★ | 15 | §2 | C, E | wbm | — |
| R2.3 | ✏️ | Factoriser par un facteur commun | ★★ | 15 | §2 | C, E | wbm | — |
| R2.4 | ✏️ | Identités remarquables dans les deux sens | ★★ | 20 | §3 | C, E | wbm | — |
| R2.5 | ✏️ | Équations du premier degré | ★ | 15 | §4 | C, E | wbm | — |
| R2.6 | ✏️ | Équations produit nul et équations avec des fractions | ★★ | 20 | §4 | C, E | wbm | — |
| R2.7 | ✏️ | Inéquations et intervalles | ★ | 15 | §5 | C, E | wbm | — |
| R2.8 | ✏️ | Réunion et intersection d'intervalles | ★★ | 15 | §5 | C | wbm | — |
| R2.9 | ✏️ | Équations et inéquations avec une valeur absolue, et la fonction signe | ★★ | 20 | §6 | C, E | wbm | — |
| R2.10 | ✏️ | Système 2 × 2 par substitution et par combinaison | ★★ | 20 | §7 | C, E | wbm | — |
| R2.11 | ✏️ | Système 2 × 2 par la formule de Cramer | ★★ | 15 | §7 | C, E | wbm | — |
| R2.12 | ✏️ | Mettre en équation : trois problèmes | ★★ | 25 | §8 | C, E | wbm | — |
| R2.13 | ∂ | Démontrer les identités remarquables | ★★ | 20 | §3 | C, E | manuel | — |
| R2.14 | ∂ | Pourquoi multiplier par un nombre négatif retourne l'inégalité | ★★ | 20 | §5 | C | manuel | — |
| R2.15 | ∂ | Quand un système 2 × 2 a-t-il une seule solution ? | ★★★ | 40 | §7 | C | manuel | — |
| R2.16 | 🔗 | Deux mesures, deux inconnues : retrouver a et b dans y = ax + b par un système | ★★ | 20 | §7 §8 | C, E | wbm | — |
| R2.17 | 🗣️ | Expliquer ce que veut dire « résoudre une équation » | ★ | 10 | §4 | C, E | manuel | — |
| R2.18 | 🔨 | Résoudre ax + b = 0 dans tous les cas · `solve_linear` | ★ | 25 | §4 | C, E | pytest | — |
| R2.19 | 🔨 | Résoudre ax + b ≤ 0 et rendre l'intervalle des solutions · `solve_linear_inequality` | ★★ | 40 | §5 | C | pytest | R2.18 |
| R2.20 | 🔨 | Résoudre |x − a| = c · `solve_abs_equation` | ★★ | 30 | §6 | C | pytest | — |
| R2.21 | 🔨 | Système 2 × 2 par la formule de Cramer · `solve_2x2` | ★★ | 40 | §7 | C, E | pytest | — |
| R2.22 | 📦 | Vérifier développements et factorisations avec SymPy | ★ | 15 | §2 §3 | C, E | wbm | — |
| R2.23 | 📦 | Résoudre avec `sympy.solve` et lire son résultat | ★ | 15 | §4 §7 | C | wbm | — |
| R2.24 | 🔮 | Prédire le nombre de solutions de trois systèmes, puis tracer leurs droites | ★ | 15 | §7 | C, E | wbm | — |
| R2.25 | 🔬 | Expérience : un système presque dégénéré, un coefficient bouge de 0,001 et la solution s'envole | ★★ | 20 | §7 | C | wbm | — |
| R2.26 | 🎨 | Un système, deux droites : voir la solution | ★★ | 20 | §7 | C, E | manuel | — |
| R2.27 | 🐛 | Chasse à l'erreur : six erreurs de calcul littéral | ★★ | 20 | §2 §3 §5 | C, E | wbm | — |
| R2.28 | 🛠️ | Écrire un test pytest pour une fonction qui résout une équation | ★ | 15 | §4 | C | manuel | — |

<a id="r3"></a>
## R3 · Fonctions

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r3_fonctions/` · **MML** — · **sessions de génération** 1

La notion de fonction et ses représentations : images, antécédents, ensemble de définition, lecture graphique ; les fonctions affines (pente, ordonnée à l'origine) et les fonctions de référence ; le second degré en entier (forme canonique, discriminant, sommet) ; les variations et les extremums ; la composition et la réciproque, qui reviennent partout en ML (une couche suivie d'une activation, l'inverse d'une normalisation).

**Temps** : 12,8 h en parcours complet, 10,4 h en parcours essentiel (lecture 165 min, 25 flashcards).

**Objectifs**

- Calculer des images et des antécédents, lire un graphique et déterminer un ensemble de définition.
- Déterminer une fonction affine à partir de deux points et interpréter sa pente et son ordonnée à l'origine.
- Mettre un polynôme du second degré sous forme canonique, trouver ses racines et son sommet.
- Étudier le sens de variation des fonctions de référence et trouver un extremum.
- Composer deux fonctions et trouver une réciproque, en sachant dans quel ordre on les applique.

**Sections de la fiche**

- §1 Image, antécédent, ensemble de définition
- §2 Représentation graphique et lecture graphique
- §3 Fonctions affines
- §4 Fonctions de référence : carré, inverse, racine carrée, valeur absolue
- §5 Polynômes du second degré
- §6 Sens de variation, maximum et minimum
- §7 Composition de fonctions
- §8 Fonction réciproque
- §9 Polynômes de degré quelconque (aperçu)

**Notions enseignées** : fonction, image, antécédent · ensemble de définition · courbe représentative · lecture graphique · fonctions affines, pente, ordonnée à l'origine · fonctions carré, inverse, racine carrée, valeur absolue · second degré : forme canonique, discriminant, racines, sommet, factorisation · sens de variation · maximum, minimum · composition · fonction réciproque · polynômes, degré, schéma de Horner · normalisation min-max (une fonction affine) · max, min, argmax et argmin d'une fonction ou d'une liste · fonctions définies par morceaux : max(0, x), la marche, |x|

**Prérequis** : développer, factoriser, identités remarquables (R2) · équations et intervalles (R2)

**Python (workbookIA 0A, à avoir fait avant)** : §100.5.3 Fonctions comme valeurs : lambda, key=, fonctions en argument, Callable · §100.5.4 Fermetures (closures)

**mymath** : `functions.py` (signatures figées) : `polyval`, `affine_from_points`, `quadratic_roots`, `quadratic_vertex`, `compose`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.6 ✏️ Droites et paraboles : pente, ordonnée à l'origine, racines, sommet · 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ)

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R3.Q1 | 🧠 | Image, antécédent, ensemble de définition | ★ | 4 | §1 | C, E | manuel | — |
| R3.Q2 | 🧠 | Lire un graphique | ★ | 4 | §2 | C, E | manuel | — |
| R3.Q3 | 🧠 | Pente et ordonnée à l'origine | ★ | 4 | §3 | C, E | manuel | — |
| R3.Q4 | 🧠 | Fonctions de référence : allure et variations | ★ | 4 | §4 | C, E | manuel | — |
| R3.Q5 | 🧠 | Discriminant : combien de racines ? | ★ | 4 | §5 | C, E | manuel | — |
| R3.Q6 | 🧠 | Croissante, décroissante, extremum | ★ | 4 | §6 | C | manuel | — |
| R3.Q7 | 🧠 | f∘g ou g∘f ? | ★ | 4 | §7 | C, E | manuel | — |
| R3.Q8 | 🧠 | Réciproque et inverse : ne pas confondre | ★ | 4 | §8 | C, E | manuel | — |
| R3.R1 | 🔁 | Identités remarquables (R2) | ★ | 5 | §5 | C, E | manuel | — |
| R3.R2 | 🔁 | Inéquations et intervalles (R2) | ★ | 5 | §1 | C, E | manuel | — |
| R3.R3 | 🔁 | Puissances et racines (R1) | ★ | 5 | §4 | C | manuel | — |
| R3.1 | ✏️ | Images, antécédents et ensemble de définition | ★ | 15 | §1 | C, E | wbm | — |
| R3.2 | 📈 | Lire des valeurs, des solutions et des variations sur un graphique | ★ | 15 | §2 | C, E | wbm | — |
| R3.3 | ✏️ | La fonction affine qui passe par deux points | ★ | 15 | §3 | C, E | wbm | — |
| R3.4 | ✏️ | Ramener des données entre 0 et 1 avec une fonction affine (min-max) | ★★ | 20 | §3 | C, E | wbm | — |
| R3.5 | ✏️ | Variations et signe des fonctions de référence | ★ | 15 | §4 §6 | C, E | wbm | — |
| R3.6 | ✏️ | Forme canonique et sommet d'une parabole | ★★ | 20 | §5 | C, E | wbm | — |
| R3.7 | ✏️ | Racines par le discriminant et factorisation | ★★ | 20 | §5 | C, E | wbm | — |
| R3.8 | ✏️ | Trouver le maximum d'une aire ou d'un bénéfice | ★★ | 20 | §5 §6 | C, E | wbm | — |
| R3.9 | ✏️ | Composer deux fonctions dans les deux ordres | ★ | 15 | §7 | C, E | wbm | — |
| R3.10 | ✏️ | Trouver une réciproque et son ensemble de définition | ★★ | 20 | §8 | C, E | wbm | — |
| R3.11 | ✏️ | Fonctions par morceaux et argmax : max(0, x), |x|, la marche, et où une fonction atteint son maximum | ★★ | 20 | §4 §6 | C, E | wbm | — |
| R3.12 | ✏️ | Évaluer un polynôme par le schéma de Horner | ★ | 10 | §9 | C | wbm | — |
| R3.13 | ∂ | Démontrer la formule des racines du second degré | ★★ | 35 | §5 | C | manuel | — |
| R3.14 | ∂ | Une fonction affine de pente positive est croissante | ★★ | 20 | §3 §6 | C | manuel | — |
| R3.15 | 🔗 | Une fonction de coût donnée par une formule : une parabole et son sommet | ★★ | 20 | §5 §6 | C, E | wbm | — |
| R3.16 | 🗣️ | Expliquer ce qu'est une fonction à quelqu'un qui n'aime pas les maths | ★ | 10 | §1 | C, E | manuel | — |
| R3.17 | 🔨 | Évaluer un polynôme par Horner · `polyval` | ★ | 25 | §9 | C | pytest | — |
| R3.18 | 🔨 | La fonction affine qui passe par deux points · `affine_from_points` | ★ | 25 | §3 | C, E | pytest | — |
| R3.19 | 🔨 | Racines et sommet d'un polynôme du second degré · `quadratic_roots, quadratic_vertex` | ★★ | 40 | §5 | C, E | pytest | — |
| R3.20 | 🔨 | Composer deux fonctions · `compose` | ★ | 25 | §7 | C, E | pytest | — |
| R3.21 | 📦 | Tracer et lire les fonctions de référence | ★ | 15 | §4 | C, E | wbm | — |
| R3.22 | 🎨 | Faire varier a, b et c : déformer une parabole | ★★ | 20 | §5 | C, E | manuel | — |
| R3.23 | 🔮 | Prédire f∘g et g∘f pour « valeur absolue » et « moins 3 » | ★ | 10 | §7 | C | wbm | — |
| R3.24 | 🔬 | Combien de racines ? Le signe du discriminant sur une grille de paramètres | ★★ | 20 | §5 | C | wbm | — |
| R3.25 | 🐛 | Chasse à l'erreur : composition, réciproque et racines | ★★ | 20 | §5 §7 §8 | C, E | wbm | — |
| R3.26 | 🛠️ | Un graphique propre : titre, axes, légende | ★ | 15 | §2 | C | manuel | — |

<a id="r4"></a>
## R4 · Logique, ensembles, Σ et Π

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r4_logique_ensembles/` · **MML** — · **sessions de génération** 1

Le langage des mathématiques : propositions et connecteurs, implication et contraposée, quantificateurs et leur négation, ensembles et opérations, notations Σ et Π. Puis les grands types de raisonnement (direct, contraposée, absurde, contre-exemple, récurrence) et la rédaction d'une démonstration courte : de quoi lire MML, et workbookIA 11 (déduction, induction).

**Temps** : 13,2 h en parcours complet, 9,9 h en parcours essentiel (lecture 195 min, 22 flashcards).

**Objectifs**

- Construire une table de vérité et nier une phrase qui contient des quantificateurs.
- Distinguer une implication, sa réciproque et sa contraposée.
- Manipuler les ensembles et leurs opérations, et lire la notation des ensembles de nombres.
- Lire, écrire et calculer des sommes Σ et des produits Π, et changer d'indice.
- Choisir un type de raisonnement et rédiger une démonstration courte, récurrence comprise.

**Sections de la fiche**

- §1 Propositions, « et », « ou », « non »
- §2 Implication, réciproque, contraposée, équivalence
- §3 Quantificateurs et négation
- §4 Ensembles
- §5 Notations Σ et Π
- §6 Raisonnements : direct, contraposée, absurde, contre-exemple, disjonction de cas
- §7 Raisonnement par récurrence
- §8 Rédiger une démonstration courte

**Notions enseignées** : proposition, connecteurs et, ou, non · table de vérité · implication, réciproque, contraposée, équivalence · quantificateurs ∀ et ∃ et leur négation · ensembles, appartenance, inclusion · union, intersection, complémentaire, cardinal · produit cartésien · notations Σ et Π, changement d'indice · sommes doubles Σᵢ Σⱼ · raisonnement direct, par contraposée, par l'absurde · contre-exemple · disjonction de cas · récurrence · rédaction d'une démonstration · déduction (premier contact)

**Prérequis** : équations et inéquations (R2) · fonctions (R3)

**Python (workbookIA 0A, à avoir fait avant)** : §100.3.4 Ensembles · §100.6.6 itertools et heapq (aperçu)

**mymath** : `logic.py` (signatures figées) : `truth_table`, `implies`, `sum_over`, `prod_over`, `find_counterexample`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.3 ✏️ Lire et calculer des Σ et des Π · 0B.5 ✏️ Ensembles : union, intersection, complémentaire et cardinal · 9.1 ✏️ MSE et R² à la main sur cinq points

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R4.Q1 | 🧠 | Vrai, faux, ou pas une proposition ? | ★ | 4 | §1 | C, E | manuel | — |
| R4.Q2 | 🧠 | Réciproque ou contraposée ? | ★ | 4 | §2 | C, E | manuel | — |
| R4.Q3 | 🧠 | Nier une phrase avec « pour tout » | ★ | 4 | §3 | C, E | manuel | — |
| R4.Q4 | 🧠 | Ensembles : vrai ou faux | ★ | 4 | §4 | C, E | manuel | — |
| R4.Q5 | 🧠 | Lire une somme Σ | ★ | 4 | §5 | C, E | manuel | — |
| R4.Q6 | 🧠 | Quel raisonnement pour quelle affirmation ? | ★ | 4 | §6 | C, E | manuel | — |
| R4.Q7 | 🧠 | Les deux étapes d'une récurrence | ★ | 4 | §7 | C | manuel | — |
| R4.Q8 | 🧠 | Ce qui manque dans une démonstration | ★ | 4 | §8 | C | manuel | — |
| R4.R1 | 🔁 | Résoudre une inéquation (R2) | ★ | 5 | §3 | C, E | manuel | — |
| R4.R2 | 🔁 | Composer deux fonctions (R3) | ★ | 5 | §6 | C | manuel | — |
| R4.R3 | 🔁 | Additionner des fractions (R1) | ★ | 5 | §5 | C, E | manuel | — |
| R4.1 | ✏️ | Tables de vérité de « et », « ou », « non » et de l'implication | ★ | 15 | §1 §2 | C, E | wbm | — |
| R4.2 | ✏️ | Réciproque, contraposée, négation : écrire les trois | ★★ | 20 | §2 §3 | C, E | wbm | — |
| R4.3 | ✏️ | Nier des phrases à deux quantificateurs | ★★ | 20 | §3 | C, E | wbm | — |
| R4.4 | ✏️ | Opérations sur des ensembles et dénombrement | ★ | 15 | §4 | C, E | wbm | — |
| R4.5 | ✏️ | Produit cartésien et couples | ★ | 10 | §4 | C | wbm | — |
| R4.6 | ✏️ | Calculer des sommes Σ et des produits Π | ★ | 15 | §5 | C, E | wbm | — |
| R4.7 | ✏️ | Développer, réindexer et découper une somme Σ ; calculer une somme double | ★★ | 20 | §5 | C, E | wbm | — |
| R4.8 | ✏️ | Trouver un contre-exemple | ★ | 10 | §6 | C, E | wbm | — |
| R4.9 | ∂ | Démonstration directe : la somme de deux nombres pairs est paire | ★★ | 20 | §6 §8 | C, E | manuel | — |
| R4.10 | ∂ | Par contraposée : si n² est pair, alors n est pair | ★★ | 25 | §6 | C, E | manuel | — |
| R4.11 | ∂ | Par l'absurde : √2 n'est pas une fraction | ★★★ | 40 | §6 | C | manuel | — |
| R4.12 | ∂ | Par récurrence : 1 + 2 + … + n = n(n + 1)/2 | ★★ | 35 | §7 §5 | C, E | manuel | — |
| R4.13 | ∂ | Par récurrence : 2ⁿ ≥ n + 1 | ★★ | 35 | §7 | C | manuel | — |
| R4.14 | 🔗 | Écrire la loss moyenne d'un modèle avec Σ | ★★ | 15 | §5 | C, E | wbm | — |
| R4.15 | ⚖️ | Repérer un raisonnement fautif dans une phrase de presse | ★ | 15 | §2 §6 | C | manuel | — |
| R4.16 | 🗣️ | Expliquer la différence entre « si » et « si et seulement si » | ★ | 10 | §2 | C, E | manuel | — |
| R4.17 | 🔨 | Tables de vérité et implication · `truth_table, implies` | ★ | 30 | §1 §2 | C | pytest | — |
| R4.18 | 🔨 | Σ et Π en Python : `sum_over` et `prod_over` · `sum_over, prod_over` | ★ | 25 | §5 | C, E | pytest | — |
| R4.19 | 🔨 | Chercher un contre-exemple de 0 à N · `find_counterexample` | ★★ | 30 | §6 | C, E | pytest | — |
| R4.20 | 📦 | Les ensembles de Python : `set`, `|`, `&`, `-` | ★ | 10 | §4 | C, E | wbm | — |
| R4.21 | 🔮 | Prédire : n² + n + 41 est-il toujours un nombre premier ? | ★ | 15 | §6 | C, E | wbm | — |
| R4.22 | 🔬 | Vérifier une formule de somme de 1 à 1 000, puis la démontrer | ★★ | 20 | §5 §7 | C | wbm | — |
| R4.23 | 🎨 | Diagrammes de Venn | ★ | 15 | §4 | C | manuel | — |
| R4.24 | 🐛 | Chasse à l'erreur : une « démonstration » par récurrence qui prouve le faux | ★★ | 20 | §7 §8 | C, E | wbm | — |
| R4.25 | 🛠️ | Rédiger une démonstration propre en LaTeX | ★ | 20 | §8 | C | manuel | — |

<a id="r5"></a>
## R5 · Suites

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r5_suites/` · **MML** — · **sessions de génération** 1

Les suites : définies explicitement ou par récurrence, arithmétiques et géométriques, leurs sommes, leur limite et la somme infinie d'une suite géométrique. Puis les moyennes mobiles et exponentielles, dont les poids forment une suite géométrique : on les retrouvera dans le momentum des optimiseurs (workbookIA 19) et le retour actualisé du RL (26), qui les étudient pour leur compte.

**Temps** : 10,2 h en parcours complet, 8,2 h en parcours essentiel (lecture 180 min, 20 flashcards).

**Objectifs**

- Calculer les termes d'une suite définie explicitement ou par récurrence.
- Reconnaître une suite arithmétique ou géométrique, et calculer un terme et une somme.
- Dire si une suite géométrique converge et calculer la somme d'une série géométrique.
- Calculer une moyenne mobile et une moyenne exponentielle, et relier leurs poids à une suite géométrique.

**Sections de la fiche**

- §1 Suites : explicites et par récurrence
- §2 Suites arithmétiques
- §3 Suites géométriques
- §4 Sommes de termes
- §5 Limite d'une suite et somme infinie
- §6 Moyennes mobiles et exponentielles

**Notions enseignées** : suite, terme, indice · définition explicite et par récurrence · suite arithmétique, raison · suite géométrique, raison · somme des termes d'une suite arithmétique · somme des termes d'une suite géométrique · limite d'une suite · somme infinie d'une suite géométrique · moyenne mobile · moyenne exponentielle (lissage) · intérêts composés, actualisation

**Prérequis** : Σ et récurrence (R4) · puissances (R1) · fonctions affines (R3)

**Python (workbookIA 0A, à avoir fait avant)** : §100.8.1 Créer des arrays : dtype, shape, ndim · §100.8.3 Calcul vectorisé et fonctions universelles · §100.8.5 Réductions par axe, tri, argmax, unique

**mymath** : `sequences.py` (signatures figées) : `arithmetic_term`, `geometric_sum`, `iterate`, `moving_average`, `exponential_moving_average`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.13 ✏️ Suites géométriques : ce qui fond, ce qui explose · 11.2 ∂ Moyenne incrémentale : Qₙ₊₁ = Qₙ + (Rₙ − Qₙ)/n · 19.8 ∂ Moyenne mobile exponentielle : mémoire effective et biais initial · 26.1 ✏️ Retours total et actualisé d'une partie de six coups · 26.7 ∂ Somme géométrique et horizon effectif de γ

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R5.Q1 | 🧠 | Explicite ou par récurrence ? | ★ | 4 | §1 | C, E | manuel | — |
| R5.Q2 | 🧠 | Arithmétique, géométrique, ou ni l'une ni l'autre ? | ★ | 4 | §2 §3 | C, E | manuel | — |
| R5.Q3 | 🧠 | Formules de somme : vrai ou faux | ★ | 4 | §4 | C, E | manuel | — |
| R5.Q4 | 🧠 | Converge ou diverge ? | ★ | 4 | §5 | C, E | manuel | — |
| R5.Q5 | 🧠 | Moyenne mobile ou moyenne exponentielle ? | ★ | 4 | §6 | C, E | manuel | — |
| R5.Q6 | 🧠 | Les poids d'une moyenne exponentielle | ★ | 4 | §6 | C | manuel | — |
| R5.R1 | 🔁 | Σ et changement d'indice (R4) | ★ | 5 | §4 | C, E | manuel | — |
| R5.R2 | 🔁 | Raisonnement par récurrence (R4) | ★ | 5 | §1 | C | manuel | — |
| R5.R3 | 🔁 | Évolutions successives (R1) | ★ | 5 | §3 | C, E | manuel | — |
| R5.1 | ✏️ | Calculer des termes : explicite et récurrence | ★ | 10 | §1 | C, E | wbm | — |
| R5.2 | ✏️ | Terme général d'une suite arithmétique | ★ | 10 | §2 | C, E | wbm | — |
| R5.3 | ✏️ | Terme général d'une suite géométrique | ★ | 10 | §3 | C, E | wbm | — |
| R5.4 | ✏️ | Sommes arithmétiques et géométriques | ★★ | 20 | §4 | C, E | wbm | — |
| R5.5 | ✏️ | Sommes infinies d'une suite géométrique | ★★ | 15 | §5 | C, E | wbm | — |
| R5.6 | ✏️ | Intérêts composés et actualisation | ★★ | 20 | §3 §5 | C | wbm | — |
| R5.7 | ✏️ | Une moyenne exponentielle à la main sur cinq valeurs | ★★ | 20 | §6 | C, E | wbm | — |
| R5.8 | ✏️ | Retrouver le premier terme et la raison à partir de deux termes | ★ | 10 | §2 §3 | C, E | wbm | — |
| R5.9 | ∂ | La somme d'une suite géométrique, démontrée par récurrence | ★★ | 25 | §4 | C, E | manuel | — |
| R5.10 | ∂ | La somme d'une suite arithmétique : l'astuce de Gauss (premier + dernier) | ★★ | 25 | §2 §4 | C | manuel | — |
| R5.11 | 🔗 | Actualiser : ce que vaut aujourd'hui une somme versée chaque année (une somme géométrique) | ★★ | 20 | §5 | C, E | wbm | — |
| R5.12 | 🔗 | Une moyenne mobile qui glisse : la mettre à jour sans tout recalculer | ★ | 15 | §6 §1 | C, E | wbm | — |
| R5.13 | 🗣️ | Expliquer pourquoi une somme infinie peut être finie | ★ | 10 | §5 | C, E | manuel | — |
| R5.14 | 🔨 | Terme d'une suite arithmétique et somme géométrique · `arithmetic_term, geometric_sum` | ★ | 15 | §2 §4 | C, E | pytest | — |
| R5.15 | 🔨 | Itérer une récurrence · `iterate` | ★ | 15 | §1 | C, E | pytest | — |
| R5.16 | 🔨 | Moyennes mobile et exponentielle · `moving_average, exponential_moving_average` | ★★ | 25 | §6 | C, E | pytest | — |
| R5.17 | 📦 | Les mêmes calculs avec NumPy : `np.cumsum`, `np.cumprod`, `np.convolve` | ★ | 15 | §4 §6 | C | wbm | — |
| R5.18 | 🔮 | Prédire : vers quoi tend u(n + 1) = 0,75 u(n) + 2 ? | ★ | 10 | §1 §5 | C, E | wbm | — |
| R5.19 | 🔬 | Lisser un signal bruité : l'effet de la fenêtre et de β | ★★ | 20 | §6 | C | wbm | — |
| R5.20 | 🎨 | Des suites qui convergent, divergent, oscillent | ★ | 15 | §5 | C | manuel | — |
| R5.21 | 🐛 | Chasse à l'erreur : un décalage d'indice dans une somme | ★ | 15 | §4 | C, E | wbm | — |
| R5.22 | 🛠️ | Une boucle ou une formule ? Mesurer le temps de calcul | ★ | 15 | §4 | C | manuel | — |

<a id="r6"></a>
## R6 · Exponentielle et logarithmes

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r6_exp_log/` · **MML** — · **sessions de génération** 1

L'exponentielle et le logarithme : leurs propriétés algébriques, le nombre e, le logarithme népérien comme réciproque de l'exponentielle, les bases 2 et 10 et le changement de base (les bits), les croissances comparées et les échelles logarithmiques. Puis la sigmoïde et la tangente hyperbolique, et pourquoi le ML calcule avec des log-probabilités.

**Temps** : 10,4 h en parcours complet, 8,0 h en parcours essentiel (lecture 170 min, 22 flashcards).

**Objectifs**

- Utiliser les propriétés de exp et de ln pour simplifier une expression et résoudre une équation.
- Passer d'une base de logarithme à une autre, et compter en bits.
- Comparer les croissances des puissances, des exponentielles et des logarithmes.
- Lire et tracer un graphique en échelle logarithmique.
- Étudier la sigmoïde et la tangente hyperbolique, et les écrire avec exp.

**Sections de la fiche**

- §1 La fonction exponentielle et ses propriétés
- §2 Le nombre e
- §3 Le logarithme népérien
- §4 Logarithmes en base 2 et 10, changement de base, bits
- §5 Croissances comparées
- §6 Échelles logarithmiques
- §7 Sigmoïde et tangente hyperbolique

**Notions enseignées** : croissance exponentielle · propriétés de exp · le nombre e · logarithme népérien · ln réciproque de exp · propriétés de ln · log₂ et log₁₀ · changement de base · bits et nats · croissances comparées · échelles logarithmiques · sigmoïde et ses symétries · tangente hyperbolique · cote, log-cote et logit : la réciproque de la sigmoïde · log-probabilités : d'un produit à une somme · TF-IDF et PSNR (des logarithmes au travail)

**Prérequis** : puissances (R1) · fonctions, réciproque (R3) · suites géométriques (R5) · limite d'une suite (R5)

**Python (workbookIA 0A, à avoir fait avant)** : §100.8.3 Calcul vectorisé et fonctions universelles

**mymath** : `explog.py` (signatures figées) : `log_base`, `sigmoid`, `tanh`, `doubling_time`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.15 ✏️ Exponentielles et logarithmes : règles de calcul en bases 2, e et 10 · 0B.17 ✏️ Sigmoïde et tanh : valeurs, limites, symétries · 0B.E3 💼 Pourquoi manipuler des log-probabilités plutôt que des probabilités ? · 17.4 ∂ Dériver la sigmoïde, tanh et softplus · 17.13 🔨 Sigmoïde, tanh et softplus sans débordement

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R6.Q1 | 🧠 | Propriétés de l'exponentielle : vrai ou faux | ★ | 4 | §1 §2 | C, E | manuel | — |
| R6.Q2 | 🧠 | ln d'un produit, d'un quotient, d'une puissance | ★ | 4 | §3 | C, E | manuel | — |
| R6.Q3 | 🧠 | Combien de bits ? | ★ | 4 | §4 | C, E | manuel | — |
| R6.Q4 | 🧠 | Qui grandit le plus vite ? | ★ | 4 | §5 | C, E | manuel | — |
| R6.Q5 | 🧠 | Lire une échelle logarithmique | ★ | 4 | §6 | C | manuel | — |
| R6.Q6 | 🧠 | Sigmoïde : valeurs remarquables et symétrie | ★ | 4 | §7 | C, E | manuel | — |
| R6.R1 | 🔁 | Suites géométriques (R5) | ★ | 5 | §1 | C, E | manuel | — |
| R6.R2 | 🔁 | Fonction réciproque (R3) | ★ | 5 | §3 | C, E | manuel | — |
| R6.R3 | 🔁 | Notation scientifique (R1) | ★ | 5 | §6 | C | manuel | — |
| R6.1 | ✏️ | Simplifier avec les propriétés de exp | ★ | 15 | §1 §2 | C, E | wbm | — |
| R6.2 | ✏️ | Simplifier avec les propriétés de ln | ★ | 15 | §3 | C, E | wbm | — |
| R6.3 | ✏️ | Équations et inéquations avec exp et ln | ★★ | 20 | §3 | C, E | wbm | — |
| R6.4 | ✏️ | Changer de base : log₂, log₁₀, ln | ★ | 15 | §4 | C, E | wbm | — |
| R6.5 | ✏️ | Compter en bits et en nats : combien de questions oui ou non ? | ★★ | 15 | §4 | C, E | wbm | — |
| R6.6 | ✏️ | Temps de doublement et demi-vie | ★★ | 20 | §1 §3 | C | wbm | — |
| R6.7 | ✏️ | La cote et le logit : d'une probabilité à un score, et retour | ★★ | 20 | §7 | C, E | wbm | — |
| R6.8 | ✏️ | Placer des valeurs sur une échelle logarithmique | ★ | 10 | §6 | C | wbm | — |
| R6.9 | ∂ | Démontrer ln(ab) = ln a + ln b à partir de exp | ★★ | 25 | §3 | C, E | manuel | — |
| R6.10 | ∂ | Les propriétés de tanh, démontrées avec exp | ★★ | 25 | §2 §7 | C | manuel | — |
| R6.11 | 🔗 | Des produits de probabilités aux sommes de logarithmes | ★★ | 20 | §3 | C, E | wbm | — |
| R6.12 | 🔗 | Des logarithmes au travail : TF-IDF et PSNR | ★ | 15 | §4 | C | wbm | — |
| R6.13 | 🗣️ | Expliquer ce que compte un logarithme : des chiffres, des doublements, des bits | ★ | 10 | §3 | C, E | manuel | — |
| R6.14 | 🔨 | Un logarithme dans n'importe quelle base · `log_base` | ★ | 15 | §4 | C, E | pytest | — |
| R6.15 | 🔨 | Sigmoïde et tanh à partir de exp · `sigmoid, tanh` | ★★ | 20 | §7 | C, E | pytest | — |
| R6.16 | 🔨 | Temps de doublement · `doubling_time` | ★ | 15 | §1 §3 | C | pytest | — |
| R6.17 | 📦 | Sur tout un tableau : `np.exp`, `np.log2` et `scipy.special.expit` | ★ | 15 | §4 §7 | C | wbm | — |
| R6.18 | 🔮 | Prédire : exp(800) et exp(−800), avec math et avec NumPy | ★★ | 15 | §5 | C, E | wbm | — |
| R6.19 | 🔬 | Croissances comparées : x¹⁰, 2ˣ et ln x de plus en plus loin | ★★ | 20 | §5 | C | wbm | — |
| R6.20 | 🎨 | Les mêmes données en échelle linéaire et en échelle logarithmique | ★ | 15 | §6 | C, E | manuel | — |
| R6.21 | 🐛 | Chasse à l'erreur : ln(a + b), e^(a + b) et log(0) | ★★ | 15 | §3 | C, E | wbm | — |
| R6.22 | 🛠️ | Lire la documentation de `numpy.log`, `log2`, `log10`, `log1p` | ★ | 15 | §4 | C | manuel | — |

*Notes* : exp est définie sans dérivée (la dérivation vient en R7) : e = lim (1 + 1/n)ⁿ (limite d'une suite, R5), eˣ prolonge les puissances, et ses propriétés algébriques en découlent ; les limites de fonctions restent intuitives (« quand x devient très grand »). R7 §5 démontre (eˣ)′ = eˣ à partir de cette définition. Le 🔨 R6.15 calcule σ et tanh pour |x| ≤ 30 (sans viser la stabilité numérique, que workbookIA 17.13 demande) ; R6.18 montre seulement le débordement de exp(800) et le sous-dépassement silencieux de exp(−800). La relation tanh x = 2σ(2x) − 1 est énoncée sans preuve (17.4 la démontre) : le ∂ R6.10 démontre les autres propriétés de tanh avec les seules règles de exp.

<a id="r7"></a>
## R7 · Limites et dérivation

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r7_limites_derivation/` · **MML** — · **sessions de génération** 2

Le cœur de l'analyse du lycée : limites et asymptotes, continuité et théorème des valeurs intermédiaires (avec la dichotomie), taux d'accroissement, nombre dérivé et tangente, dérivées usuelles et règles de calcul, la règle de la chaîne, et l'étude des variations pour trouver un extremum. C'est la base de toute l'optimisation de workbookIA, de la descente de gradient (5) à la rétropropagation (18).

**Temps** : 13,2 h en parcours complet, 11,0 h en parcours essentiel (lecture 200 min, 25 flashcards).

**Objectifs**

- Calculer des limites simples et repérer une asymptote.
- Calculer un taux d'accroissement, en déduire le nombre dérivé et l'équation de la tangente.
- Dériver les fonctions usuelles avec les règles de somme, de produit, de quotient et de composition.
- Étudier les variations d'une fonction et trouver ses extremums avec la dérivée.
- Approcher un zéro par dichotomie et une dérivée par un taux d'accroissement en Python.

**Sections de la fiche**

- §1 Limites et asymptotes
- §2 Continuité, valeurs intermédiaires, dichotomie
- §3 Taux d'accroissement et nombre dérivé
- §4 Tangente
- §5 Dérivées usuelles
- §6 Règles : somme, produit, quotient
- §7 Dérivée d'une composée : la règle de la chaîne
- §8 Dérivée, variations et extremums
- §9 Comparer des croissances (grand O)

**Notions enseignées** : limite en un point et à l'infini · asymptotes · continuité · théorème des valeurs intermédiaires, dichotomie · taux d'accroissement · nombre dérivé · tangente et approximation affine · dérivées usuelles (puissances, racine, exp, ln) · dérivée d'une somme, d'un produit, d'un quotient · règle de la chaîne · signe de la dérivée et variations · extremums, dérivée nulle · (eˣ)′ = eˣ à partir de la définition de R6 · dérivable ou non : |x| et max(0, x) en 0 · dériver par rapport à une lettre, les autres fixées · grand O (aperçu) · dérivée approchée par un taux

**Prérequis** : fonctions de référence, composition (R3) · exponentielle et logarithme (R6) · limite d'une suite (R5)

**Python (workbookIA 0A, à avoir fait avant)** : §100.5.3 Fonctions comme valeurs : lambda, key=, fonctions en argument, Callable

**mymath** : `deriv.py` (signatures figées) : `difference_quotient`, `tangent_line`, `bisection`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.10 ✏️ Taux d'accroissement : de la sécante à la tangente · 0B.22 ✏️ Dériver avec les règles : somme, produit, quotient, exp, ln · 0B.23 ✏️ Règle de la chaîne : décomposer, puis dériver · 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 17.4 ∂ Dériver la sigmoïde, tanh et softplus · 18.R1 🔁 La dérivée de la sigmoïde à partir de sa sortie · 18.3 ✏️ Descente sur une parabole : quel learning rate ? · 18.5 ✏️ Le même réseau avec une sigmoïde cachée : le facteur σ'(z) · 19.7 ∂ Sur une parabole, η doit rester sous 2/a

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R7.Q1 | 🧠 | Limites : vrai ou faux | ★ | 4 | §1 | C, E | manuel | — |
| R7.Q2 | 🧠 | Continue ou pas ? | ★ | 4 | §2 | C, E | manuel | — |
| R7.Q3 | 🧠 | Le nombre dérivé est une pente | ★ | 4 | §3 §4 | C, E | manuel | — |
| R7.Q4 | 🧠 | Dérivées usuelles | ★ | 4 | §5 | C, E | manuel | — |
| R7.Q5 | 🧠 | Produit, quotient : quelle formule ? | ★ | 4 | §6 | C, E | manuel | — |
| R7.Q6 | 🧠 | Règle de la chaîne : qu'y a-t-il « dedans » ? | ★ | 4 | §7 | C, E | manuel | — |
| R7.Q7 | 🧠 | Dérivée nulle, extremum ? | ★ | 4 | §8 | C, E | manuel | — |
| R7.Q8 | 🧠 | Qui domine qui ? | ★ | 4 | §9 | C | manuel | — |
| R7.R1 | 🔁 | Croissances comparées (R6) | ★ | 5 | §1 §9 | C, E | manuel | — |
| R7.R2 | 🔁 | Limite d'une suite (R5) | ★ | 5 | §1 | C, E | manuel | — |
| R7.R3 | 🔁 | Sommet d'une parabole (R3) | ★ | 5 | §8 | C | manuel | — |
| R7.1 | ✏️ | Limites en l'infini des fonctions de référence | ★ | 15 | §1 | C, E | wbm | — |
| R7.2 | ✏️ | Limites et asymptotes de fonctions rationnelles | ★★ | 20 | §1 | C | wbm | — |
| R7.3 | ✏️ | Taux d'accroissement et nombre dérivé | ★ | 15 | §3 | C, E | wbm | — |
| R7.4 | ✏️ | Équation de la tangente | ★ | 15 | §4 | C, E | wbm | — |
| R7.5 | ✏️ | Dériver les fonctions usuelles | ★ | 15 | §5 | C, E | wbm | — |
| R7.6 | ✏️ | Dériver des produits et des quotients | ★★ | 20 | §6 | C, E | wbm | — |
| R7.7 | ✏️ | Dériver des composées | ★★ | 25 | §7 | C, E | wbm | — |
| R7.8 | ✏️ | Variations et tableau de variations | ★★ | 25 | §8 | C, E | wbm | — |
| R7.9 | ✏️ | Optimiser : la boîte de volume maximal | ★★ | 25 | §8 | C, E | wbm | — |
| R7.10 | ✏️ | La règle de la chaîne en série : trois étages, et l'ordre qui compte | ★★ | 25 | §7 | C, E | wbm | — |
| R7.11 | ✏️ | Dériver par rapport à une lettre, les autres fixées : A e^(kt), π r² h, ½ m v² | ★★ | 20 | §5 §7 | C, E | wbm | — |
| R7.12 | ∂ | La dérivée de x² à partir de la définition, et |x| qui n'est pas dérivable en 0 | ★★ | 20 | §3 | C, E | manuel | — |
| R7.13 | ∂ | Démontrer la règle du produit | ★★ | 35 | §6 | C | manuel | — |
| R7.14 | ∂ | La règle du quotient à partir de la règle du produit : (1/v)′ = −v′/v² | ★★ | 25 | §6 | C, E | manuel | — |
| R7.15 | 🔗 | Minimiser une fonction de coût donnée par une formule : dériver, annuler, vérifier | ★★ | 20 | §8 | C, E | wbm | — |
| R7.16 | 🗣️ | Expliquer ce qu'est une dérivée sans écrire de formule | ★ | 10 | §3 | C, E | manuel | — |
| R7.17 | 🔨 | Le taux d'accroissement · `difference_quotient` | ★ | 15 | §3 | C, E | pytest | — |
| R7.18 | 🔨 | La tangente à partir de f et de sa dérivée · `tangent_line` | ★★ | 20 | §4 | C | pytest | — |
| R7.19 | 🔨 | Trouver un zéro par dichotomie · `bisection` | ★★ | 25 | §2 | C, E | pytest | — |
| R7.20 | 📦 | Vérifier ses dérivées avec `sympy.diff` | ★ | 15 | §5 §6 §7 | C, E | wbm | — |
| R7.21 | 🔮 | Prédire : le taux d'accroissement a-t-il toujours une limite quand h tend vers 0 ? | ★★ | 15 | §3 | C | wbm | — |
| R7.22 | 🔬 | Zoomer sur une courbe jusqu'à voir une droite | ★★ | 20 | §4 | C, E | wbm | — |
| R7.23 | 🎨 | Tracer f, f′ et des tangentes | ★★ | 20 | §4 §8 | C | manuel | — |
| R7.24 | 🐛 | Chasse à l'erreur : quatre dérivées fausses | ★★ | 20 | §6 §7 | C, E | wbm | — |
| R7.25 | 🛠️ | Tester une dérivée avec pytest et SymPy | ★ | 15 | §5 | C | manuel | — |

*Notes* : Deux sessions de génération (chapitre long, figures nombreuses). Le 🔮 R7.21 porte sur l'existence du nombre dérivé (un coin, un saut, un raccord lisse) ; le choix du pas h en flottants (l'erreur du taux qui remonte quand h devient minuscule, workbookIA 5.12) est laissé à workbookIA 5 et à M05a ; ni différence centrée ni dérivée seconde (workbookIA 5). Frontières : on ne dérive ni σ, ni tanh, ni softplus (workbookIA 17.4) ; les fonctions de coût de R7.15 sont données par une formule, jamais par des données (pas de moyenne qui minimise les carrés, pas de w* = Σxy / Σx²) ; pas de pas de descente ; pas de tableau de variations de x³ − 3x (workbookIA 5.4) ; les composées de R7.7 et R7.10 et la dérivation « une lettre à la fois » de R7.11 évitent celles de 0B.23, de 0B §101.5.3 (la loss (wx + b − y)²) et de workbookIA 5.R3.

<a id="r8"></a>
## R8 · Probabilités de base

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r8_probabilites/` · **MML** — · **sessions de génération** 1

Les probabilités du lycée : expérience aléatoire, événements et leurs opérations, probabilité et équiprobabilité, dénombrement (principe multiplicatif, factorielle, combinaisons), arbres pondérés, indépendance, variable aléatoire discrète, espérance et variance, et la simulation qui fait voir la loi des grands nombres.

**Temps** : 10,9 h en parcours complet, 9,1 h en parcours essentiel (lecture 150 min, 25 flashcards).

**Objectifs**

- Décrire une expérience aléatoire et calculer des probabilités par équiprobabilité ou avec un arbre.
- Dénombrer avec le principe multiplicatif, les factorielles et les coefficients binomiaux.
- Reconnaître des événements indépendants.
- Calculer la loi, l'espérance, la variance et l'écart-type d'une variable aléatoire discrète.
- Estimer une probabilité par simulation et observer la loi des grands nombres.

**Sections de la fiche**

- §1 Expérience aléatoire, univers, événements
- §2 Probabilités
- §3 Dénombrer
- §4 Arbres pondérés
- §5 Indépendance
- §6 Variable aléatoire discrète
- §7 Espérance, variance, écart-type
- §8 Simuler pour estimer

**Notions enseignées** : expérience aléatoire, univers, issue · événement, complémentaire, union, intersection · probabilité, équiprobabilité · P(A ∪ B) · fréquence et probabilité · principe multiplicatif · arrangements, factorielle · combinaisons C(n, k) · triangle de Pascal · arbre pondéré · probabilité conditionnelle (premier contact) · indépendance · variable aléatoire discrète · loi d'une variable aléatoire · espérance, espérance de aX + b · variance, écart-type · V(X) = E[X²] − E[X]² (énoncée et utilisée ; démontrée en workbookIA 0B) · V(aX + b) · simulation, générateur aléatoire et graine · loi des grands nombres (intuition)

**Prérequis** : ensembles (R4) · fractions (R1) · Σ (R4)

**Python (workbookIA 0A, à avoir fait avant)** : §100.8.7 Aléatoire reproductible (np.random.default_rng) et mini-batches

**mymath** : `proba_basics.py` (signatures figées) : `factorial`, `binomial`, `enumerate_probability`, `expectation`, `variance`, `simulate_frequency`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.11 ✏️ Probabilités : issues, complémentaire, union · 0B.12 ✏️ Dénombrer : choix successifs, factorielle et C(n, k) · 0B.26 ✏️ Indépendance : tester P(A ∩ B) = P(A) P(B) avec deux dés · 0B.27 ✏️ Espérance et variance d'une variable discrète · 0B.53 🔨 Espérance et variance : le calcul exact contre la simulation · 7.1 ✏️ Compter les classifieurs OvR et OvO

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R8.Q1 | 🧠 | Univers, issue, événement | ★ | 4 | §1 | C, E | manuel | — |
| R8.Q2 | 🧠 | Propriétés d'une probabilité | ★ | 4 | §2 | C, E | manuel | — |
| R8.Q3 | 🧠 | Arrangement ou combinaison ? | ★ | 4 | §3 | C, E | manuel | — |
| R8.Q4 | 🧠 | Lire un arbre pondéré | ★ | 4 | §4 | C, E | manuel | — |
| R8.Q5 | 🧠 | Indépendants ou incompatibles ? | ★ | 4 | §5 | C, E | manuel | — |
| R8.Q6 | 🧠 | Espérance et variance : vrai ou faux | ★ | 4 | §6 §7 | C, E | manuel | — |
| R8.Q7 | 🧠 | Ce que dit la loi des grands nombres | ★ | 4 | §8 | C | manuel | — |
| R8.R1 | 🔁 | Ensembles et complémentaire (R4) | ★ | 5 | §1 | C, E | manuel | — |
| R8.R2 | 🔁 | Σ et Π (R4) | ★ | 5 | §7 | C, E | manuel | — |
| R8.R3 | 🔁 | Fractions (R1) | ★ | 5 | §2 | C | manuel | — |
| R8.1 | ✏️ | Décrire univers et événements : cartes et pièces | ★ | 10 | §1 | C, E | wbm | — |
| R8.2 | ✏️ | Probabilités par équiprobabilité | ★ | 15 | §2 | C, E | wbm | — |
| R8.3 | ✏️ | P(A ∪ B) et le complémentaire | ★★ | 15 | §2 | C, E | wbm | — |
| R8.4 | ✏️ | Principe multiplicatif et factorielles | ★ | 15 | §3 | C, E | wbm | — |
| R8.5 | ✏️ | Combinaisons et triangle de Pascal | ★★ | 20 | §3 | C, E | wbm | — |
| R8.6 | ✏️ | Arbres pondérés : épreuves successives | ★★ | 20 | §4 | C, E | wbm | — |
| R8.7 | ✏️ | Indépendant ou pas ? Le décider par le calcul, avec des cartes et des pièces | ★★ | 15 | §5 | C, E | wbm | — |
| R8.8 | ✏️ | La loi d'une variable aléatoire | ★ | 15 | §6 | C, E | wbm | — |
| R8.9 | ✏️ | Espérance, variance (avec V = E[X²] − E[X]²) et écart-type | ★★ | 20 | §7 | C, E | wbm | — |
| R8.10 | ✏️ | Deux jeux de hasard : équité et risque | ★★ | 20 | §7 | C | wbm | — |
| R8.11 | ∂ | Démontrer C(n, k) = C(n − 1, k − 1) + C(n − 1, k) | ★★ | 25 | §3 | C | manuel | — |
| R8.12 | ∂ | L'espérance d'une somme : E[X + Y] = E[X] + E[Y], même pour des variables liées | ★★ | 25 | §7 | C, E | manuel | — |
| R8.13 | 🔗 | Comparer toutes les paires : un tournoi, C(n, 2) et une croissance en n² | ★ | 10 | §3 | C, E | wbm | — |
| R8.14 | 🧮 | Fermi : la probabilité de croiser quelqu'un que l'on connaît dans le métro | ★★ | 20 | §2 | C | manuel | — |
| R8.15 | 🗣️ | Expliquer la différence entre probabilité et fréquence | ★ | 10 | §2 §8 | C, E | manuel | — |
| R8.16 | 🔨 | Factorielle et combinaisons · `factorial, binomial` | ★ | 15 | §3 | C, E | pytest | — |
| R8.17 | 🔨 | Une probabilité exacte par énumération · `enumerate_probability` | ★★ | 25 | §2 | C | pytest | — |
| R8.18 | 🔨 | Espérance et variance d'une loi · `expectation, variance` | ★ | 15 | §7 | C, E | pytest | — |
| R8.19 | 🔨 | Estimer une probabilité par simulation · `simulate_frequency` | ★★ | 20 | §8 | C, E | pytest | — |
| R8.20 | 🔮 | Prédire : dans une classe de 30, deux élèves ont-ils le même anniversaire ? | ★★ | 15 | §2 §3 | C, E | wbm | — |
| R8.21 | 🔬 | La loi des grands nombres : fréquence et nombre d'essais | ★★ | 20 | §8 | C, E | wbm | — |
| R8.22 | 🎨 | Le diagramme en bâtons d'une loi | ★ | 10 | §6 | C | manuel | — |
| R8.23 | 🐛 | Chasse à l'erreur : trois raisonnements de probabilités faux | ★★ | 20 | §2 §5 | C, E | wbm | — |
| R8.24 | 🛠️ | Reproductibilité : générateur aléatoire et graine | ★ | 15 | §8 | C, E | manuel | — |

*Notes* : Une session de génération. Règle de partage avec workbookIA 0B : 0B.28 démontre E[aX + b], V(X) = E[X²] − E[X]² et V(aX + b), seulement énoncés et utilisés ici ; le ∂ R8.12 démontre l'énoncé plus général E[X + Y] = E[X] + E[Y] (que 0B admet), en sommant sur les issues. Les exemples et les données évitent ceux de 0B (deux dés à 6 faces, la somme 7, « au moins un 6 », la pièce et le dé, la loi 0, 1, 2, 5 de 0B.27, le dé 1, 1, 2, 3, 3, 3), de workbookIA 2 (dé à 20 faces, pièce truquée à 30 %), de 3.R1 (deux cartes rouges parmi 32) et du test de positionnement (urne de 3 rouges et 2 bleues, loi −2, 0, 1) ; le 🔗 R8.13 compte des paires sans parler d'un-contre-un (workbookIA 7.1) ; le 🔬 R8.21 mesure la proportion de séries qui s'écartent de la probabilité, pas l'écart-type des fréquences (0B.52). Session 13 (relecture à l'aveugle) : les exemples de la fiche et des exercices ✏️ R8.4, R8.6, R8.7, R8.9, R8.10 et 🔬 R8.21 ont été remplacés pour s'éloigner davantage de workbookIA (roue de 8 secteurs, playlist, lancers francs, roue de 3 secteurs) ; les 🔗 de la fiche renvoient aux chapitres 2, 3, 9, 19 et 26 sans en reprendre d'exemple. Le 🔨 R8.18 (expectation, variance) recouvre en partie 0B.53, qui fait coder les mêmes formules : recouvrement assumé, ses signatures étant fixées au syllabus depuis la session 2.

<a id="r9"></a>
## R9 · Géométrie du plan, vecteurs et trigonométrie

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `chapitres/r9_geometrie_vecteurs/` · **MML** — · **sessions de génération** 1

La géométrie du plan avec des coordonnées : distances, vecteurs, normes, équations de droites, produit scalaire et orthogonalité ; le cercle trigonométrique, les radians, le cosinus et le sinus ; l'angle entre deux vecteurs et la similarité cosinus ; puis les mêmes calculs avec trois composantes et plus, qui annoncent ℝⁿ (workbookIA 0B, puis M07).

**Temps** : 11,0 h en parcours complet, 8,8 h en parcours essentiel (lecture 150 min, 25 flashcards).

**Objectifs**

- Calculer des coordonnées, des distances et des vecteurs dans un repère du plan.
- Additionner des vecteurs, les multiplier par un nombre et calculer leur norme.
- Écrire l'équation d'une droite et reconnaître des vecteurs orthogonaux.
- Calculer un produit scalaire et en déduire un angle.
- Passer des degrés aux radians, et lire cosinus et sinus sur le cercle trigonométrique.
- Refaire ces calculs avec des vecteurs à trois composantes et plus.

**Sections de la fiche**

- §1 Repère, coordonnées, distance
- §2 Vecteurs
- §3 Norme d'un vecteur
- §4 Équations de droites
- §5 Produit scalaire et orthogonalité
- §6 Cercle trigonométrique, radians, cosinus et sinus
- §7 Angle entre deux vecteurs et similarité cosinus
- §8 Vecteurs de l'espace et au-delà

**Notions enseignées** : repère, coordonnées · distance entre deux points · vecteur, coordonnées d'un vecteur · somme de vecteurs, produit par un nombre · norme · droite : équation réduite, vecteur directeur · produit scalaire · orthogonalité · radians · cercle trigonométrique · cosinus, sinus, valeurs remarquables · cos² + sin² = 1 · périodicité, courbes de cos et de sin · arccos sur [0, π] · normes L1 et L∞ (aperçu) · dérivées de sin et cos (aperçu) · angle entre deux vecteurs · similarité cosinus · vecteurs de ℝ³ et de ℝⁿ (aperçu)

**Prérequis** : valeur absolue et distance (R2) · racines carrées (R1) · fonctions affines (R3) · dérivation, règle de la chaîne (R7) · Σ (R4)

**Python (workbookIA 0A, à avoir fait avant)** : §100.8.1 Créer des arrays : dtype, shape, ndim · §100.8.3 Calcul vectorisé et fonctions universelles

**mymath** : `plane.py` (signatures figées) : `vector`, `norm`, `dot`, `angle_between`, `line_through`, `deg_to_rad`
(même nom qu'une fonction de `mylearn` en workbookIA 0B, voulu : `norm`, `dot`)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 0B.7 ✏️ Cosinus : cercle, période et planning en cosinus · 0B.8 ✏️ Vecteurs : somme, multiple, norme et distance entre deux manchots · 0B.18 ✏️ Produit scalaire, similarité cosinus et produit de Hadamard · 0B.39 🔨 linalg_basics (2) : produit scalaire, norme, distance, cosinus · 0B.41 🔬 Distance ou similarité cosinus : l'effet de la longueur · 0B.E2 💼 Produit scalaire et similarité cosinus : à quoi servent-ils en ML ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| R9.Q1 | 🧠 | Coordonnées et distance | ★ | 4 | §1 | C, E | manuel | — |
| R9.Q2 | 🧠 | Vecteurs : vrai ou faux | ★ | 4 | §2 §3 | C, E | manuel | — |
| R9.Q3 | 🧠 | Pente et vecteur directeur | ★ | 4 | §4 | C, E | manuel | — |
| R9.Q4 | 🧠 | Le signe du produit scalaire | ★ | 4 | §5 | C, E | manuel | — |
| R9.Q5 | 🧠 | Radians et valeurs remarquables | ★ | 4 | §6 | C, E | manuel | — |
| R9.Q6 | 🧠 | Le cosinus de deux vecteurs | ★ | 4 | §7 | C, E | manuel | — |
| R9.Q7 | 🧠 | Combien de composantes ? | ★ | 4 | §8 | C | manuel | — |
| R9.R1 | 🔁 | Fonctions affines (R3) | ★ | 5 | §4 | C, E | manuel | — |
| R9.R2 | 🔁 | Racines carrées (R1) | ★ | 5 | §3 | C, E | manuel | — |
| R9.R3 | 🔁 | Dériver une composée (R7) | ★ | 5 | §6 | C | manuel | — |
| R9.1 | ✏️ | Coordonnées et distance | ★ | 15 | §1 | C, E | wbm | — |
| R9.2 | ✏️ | Vecteurs : somme, différence, produit par un nombre | ★ | 15 | §2 | C, E | wbm | — |
| R9.3 | ✏️ | Normes (euclidienne, avec un aperçu de L1 et L∞) et vecteurs unitaires | ★ | 15 | §3 | C, E | wbm | — |
| R9.4 | ✏️ | Équations de droites | ★★ | 20 | §4 | C, E | wbm | — |
| R9.5 | ✏️ | Le produit scalaire en coordonnées | ★ | 15 | §5 | C, E | wbm | — |
| R9.6 | ✏️ | Orthogonalité et projections simples | ★★ | 20 | §5 | C | wbm | — |
| R9.7 | ✏️ | Degrés et radians, cosinus et sinus remarquables | ★ | 15 | §6 | C, E | wbm | — |
| R9.8 | ✏️ | Les courbes de cos et de sin : période, symétries, et arccos sur [0, π] | ★★ | 20 | §6 §7 | C, E | wbm | — |
| R9.9 | ✏️ | L'angle entre deux vecteurs | ★★ | 20 | §7 | C, E | wbm | — |
| R9.10 | ✏️ | Distances et produits scalaires dans ℝ³ et ℝ⁴ | ★★ | 20 | §8 | C, E | wbm | — |
| R9.11 | ∂ | Démontrer cos² + sin² = 1 avec Pythagore | ★★ | 20 | §6 | C | manuel | — |
| R9.12 | ∂ | La formule d'Al-Kashi par la hauteur du triangle et Pythagore | ★★ | 35 | §5 §7 | C | manuel | — |
| R9.13 | 🔗 | Deux recettes, deux vecteurs d'ingrédients : la similarité cosinus | ★★ | 20 | §7 | C, E | wbm | — |
| R9.14 | 🔗 | Un neurone trace une droite : w₁x₁ + w₂x₂ + b = 0 | ★ | 15 | §4 §5 | C, E | wbm | — |
| R9.15 | 🗣️ | Expliquer ce que mesure un produit scalaire | ★ | 10 | §5 | C, E | manuel | — |
| R9.16 | 🔨 | Le vecteur entre deux points et sa norme · `vector, norm` | ★ | 15 | §2 §3 | C, E | pytest | — |
| R9.17 | 🔨 | Produit scalaire et angle · `dot, angle_between` | ★ | 20 | §5 §7 | C, E | pytest | R9.16 |
| R9.18 | 🔨 | La droite qui passe par deux points, et les radians · `line_through, deg_to_rad` | ★ | 15 | §4 §6 | C | pytest | — |
| R9.19 | 📦 | Les mêmes calculs avec NumPy (`np.linalg.norm`, `@`) | ★ | 15 | §3 §5 | C, E | wbm | — |
| R9.20 | 🔮 | Prédire : permuter, décaler ou retourner des coordonnées change-t-il la similarité cosinus ? | ★ | 10 | §7 | C, E | wbm | — |
| R9.21 | 🎨 | Dessiner des vecteurs, leur somme et un angle | ★★ | 20 | §2 §7 | C, E | manuel | — |
| R9.22 | 🔬 | Le cercle trigonométrique : cos et sin d'un angle qui tourne | ★★ | 20 | §6 | C | wbm | — |
| R9.23 | 🐛 | Chasse à l'erreur : radians et degrés | ★ | 15 | §6 | C, E | wbm | — |
| R9.24 | 🛠️ | Comparer deux flottants : `np.isclose` | ★ | 10 | §5 | C | manuel | — |

<a id="cp0"></a>
## CP0 · Bilan de remise à niveau

**Partie** 0 · **prépare** workbookIA 0B · **dossier** `checkpoints/partie_0/` · **MML** — · **sessions de génération** 1

Le bilan de la remise à niveau, avant d'ouvrir workbookIA 0B : un examen blanc de 2 heures sur toute la partie 0 (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.

**Temps** : 3,3 h en parcours complet, 3,3 h en parcours essentiel (lecture 15 min, 0 flashcards).

**Objectifs**

- Vérifier en temps limité que la remise à niveau est acquise.
- Construire ta propre synthèse de la partie 0.

**Sections de la fiche**

- §1 Examen blanc
- §2 Synthèse

**Notions enseignées** : révision de la partie 0

**Prérequis** : toute la remise à niveau (R9)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 0B.14 ∂ La somme géométrique démontrée pas à pas · 0B.16 ∂ Changer de base : log₂ x = ln x / ln 2, bits et nats · 0B.19 ∂ Développer ‖a − b‖² avec le produit scalaire · 0B.24 ∂ La moyenne minimise la somme des carrés des écarts · 0B.28 ∂ Variance : deux formules, et l'espérance est linéaire · 0B.29 ∂ Règle de la chaîne à deux variables : la somme sur les chemins · 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 18.3 ✏️ Descente sur une parabole : quel learning rate ? · 19.7 ∂ Sur une parabole, η doit rester sous 2/a

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| CP0.Q1 | 🧠 | Dix affirmations sur toute la remise à niveau : vrai ou faux | ★ | 10 | §1 | C, E | manuel | — |
| CP0.1 | ✏️ | Fractions, puissances et notation scientifique | ★ | 8 | §1 | C, E | wbm | — |
| CP0.2 | ✏️ | Développer, factoriser, résoudre | ★ | 8 | §1 | C, E | wbm | — |
| CP0.3 | ✏️ | Un système 2 × 2 et sa lecture graphique | ★★ | 10 | §1 | C, E | wbm | — |
| CP0.4 | ✏️ | Second degré : racines et sommet | ★★ | 10 | §1 | C, E | wbm | — |
| CP0.5 | ✏️ | Exponentielle et logarithme | ★ | 8 | §1 | C, E | wbm | — |
| CP0.6 | ✏️ | Dériver et étudier les variations | ★★ | 12 | §1 | C, E | wbm | — |
| CP0.7 | ✏️ | Un arbre de probabilités et une espérance | ★★ | 10 | §1 | C, E | wbm | — |
| CP0.8 | ✏️ | Vecteurs, produit scalaire, angle | ★ | 8 | §1 | C, E | wbm | — |
| CP0.9 | ∂ | Une démonstration courte par récurrence | ★★ | 10 | §1 | C, E | manuel | — |
| CP0.10 | 🐛 | Corriger une copie : cinq erreurs | ★★ | 8 | §1 | C, E | wbm | — |
| CP0.11 | ✏️ | Une somme écrite avec Σ et une somme géométrique | ★ | 8 | §1 | C, E | wbm | — |
| CP0.12 | 🔗 | Problème de synthèse : étudier une fonction de coût donnée par une formule | ★★ | 12 | §1 | C, E | wbm | — |
| CP0.13 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme les checkpoints de workbookIA : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md (barème sur 20), 04_mes_reponses.md, 05_synthese.md. Durées d'épreuve, plus courtes que celles des exercices d'entraînement.

<a id="m02a"></a>
## M02a · Intégrales et densités

**Partie** I · **prépare** workbookIA 2 · **dossier** `chapitres/m02a_integrales_densites/` · **MML** (prérequis de §6.2) · **sessions de génération** 1

L'intégrale comme aire sous une courbe, les primitives et les méthodes de calcul, les intégrales impropres, les méthodes numériques ; puis la densité de probabilité, la fonction de répartition et les quantiles, sans lesquels les lois continues de workbookIA 2 restent des boîtes noires.

**Temps** : 12,6 h en parcours complet, 8,7 h en parcours essentiel (lecture 180 min, 22 flashcards).

**Objectifs**

- Approcher une aire par des sommes de Riemann, et la calculer exactement par une primitive.
- Calculer une intégrale par linéarité, par parties ou par un changement de variable.
- Reconnaître une intégrale impropre convergente et la calculer.
- Programmer les méthodes des rectangles, des trapèzes et de Simpson, et comparer leurs erreurs.
- Vérifier qu'une fonction est une densité, en déduire des probabilités et sa fonction de répartition.
- Calculer un quantile, un percentile et la médiane d'une loi continue.

**Sections de la fiche**

- §1 L'aire sous une courbe : sommes de Riemann
- §2 Primitives et intégrale : le théorème fondamental
- §3 Calculer : linéarité, intégration par parties, changement de variable
- §4 Intégrales impropres et intégrale de Gauss
- §5 Méthodes numériques : rectangles, trapèzes, Simpson
- §6 Densité de probabilité
- §7 Fonction de répartition, quantiles et percentiles
- §8 Des aires en ML : l'AUC et la valeur moyenne d'une fonction

**Notions enseignées** : aire sous une courbe, sommes de Riemann · primitives · intégrale, théorème fondamental · intégration par parties · changement de variable · intégrales impropres · intégrale de Gauss (valeur admise, vérifiée numériquement ; démontrée en M02b) · méthodes des rectangles, des trapèzes et de Simpson · densité de probabilité · fonction de répartition · quantiles et percentiles · l'AUC est une aire · valeur moyenne d'une fonction sur un intervalle

**Prérequis** : dérivées usuelles et règle de la chaîne (R7) · Σ (R4) · exp et ln (R6) · limites en l'infini (R7) · probabilité d'un événement (R8) · fonctions affines (R3)

**mymath** : `integrate.py` (signatures figées) : `riemann_sum`, `trapezoid`, `simpson`, `cdf_from_pdf`, `quantile`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 2.8 ∂ Changer d'unité : la covariance bouge, pas la corrélation · 2.3 ✏️ La règle 68-95-99,7 sur les nageoires des manchots · 2.17 🎨 Galerie des lois usuelles · 2.18 🔬 68-95-99,7 : la théorie face aux tirages et aux manchots

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M02a.Q1 | 🧠 | Aire, signe et intégrale | ★ | 4 | §1 §2 | C, E | manuel | — |
| M02a.Q2 | 🧠 | Primitives : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| M02a.Q3 | 🧠 | Quelle méthode de calcul pour quelle intégrale ? | ★ | 4 | §3 | C | manuel | — |
| M02a.Q4 | 🧠 | Converge ou diverge ? | ★ | 4 | §4 | C, E | manuel | — |
| M02a.Q5 | 🧠 | Rectangles, trapèzes, Simpson | ★ | 4 | §5 | C, E | manuel | — |
| M02a.Q6 | 🧠 | Densité et probabilité : vrai ou faux | ★ | 4 | §6 | C, E | manuel | — |
| M02a.Q7 | 🧠 | Lire une fonction de répartition | ★ | 4 | §7 | C, E | manuel | — |
| M02a.R1 | 🔁 | Dériver une composée (R7) | ★ | 5 | §2 | C, E | manuel | — |
| M02a.R2 | 🔁 | Sommes Σ (R4) | ★ | 5 | §1 | C, E | manuel | — |
| M02a.R3 | 🔁 | Exponentielle et logarithme (R6) | ★ | 5 | §4 | C | manuel | — |
| M02a.1 | ✏️ | Sommes de Riemann à la main : rectangles à gauche, à droite, au milieu | ★ | 20 | §1 | C, E | wbm | — |
| M02a.2 | ✏️ | Primitives usuelles | ★ | 15 | §2 | C, E | wbm | — |
| M02a.3 | ✏️ | Intégrales et aires : le signe, l'aire entre deux courbes | ★★ | 20 | §2 | C, E | wbm | — |
| M02a.4 | ✏️ | Intégration par parties | ★★ | 20 | §3 | C | wbm | — |
| M02a.5 | ✏️ | Changement de variable | ★★ | 20 | §3 | C | wbm | — |
| M02a.6 | ✏️ | Intégrales impropres : converge, diverge, valeur | ★★ | 20 | §4 | C, E | wbm | — |
| M02a.7 | ✏️ | Trapèzes et Simpson à la main, et leurs erreurs | ★★ | 20 | §5 | C | wbm | — |
| M02a.8 | ✏️ | Vérifier qu'une fonction est une densité, trouver sa constante | ★ | 20 | §6 | C, E | wbm | — |
| M02a.9 | ✏️ | La probabilité d'un intervalle, et la valeur moyenne d'une fonction | ★★ | 20 | §6 §8 | C, E | wbm | — |
| M02a.10 | ✏️ | Fonction de répartition, médiane et percentiles d'une loi donnée | ★★ | 20 | §7 | C, E | wbm | — |
| M02a.11 | ∂ | Le théorème fondamental : la dérivée d'une aire | ★★ | 25 | §2 | C | manuel | — |
| M02a.12 | ∂ | Encadrer une aire par des rectangles : pourquoi les sommes de Riemann convergent (fonction croissante) | ★★ | 25 | §1 §5 | C | manuel | — |
| M02a.13 | 🔗 | L'aire sous une courbe ROC donnée par une formule | ★★ | 20 | §8 | C, E | wbm | — |
| M02a.14 | 📖 | MML §6.2 (la partie continue) : densité et fonction de répartition, en anglais | ★★ | 25 | §6 §7 | C | manuel | — |
| M02a.15 | 🗣️ | Expliquer pourquoi P(X = a) = 0 pour une variable continue | ★ | 10 | §6 | C, E | manuel | — |
| M02a.E1 | 💼 | Chaque valeur a une probabilité nulle : comment dire qu'une valeur est plus probable qu'une autre ? | ★ | 10 | §6 | C, E | manuel | — |
| M02a.16 | 🔨 | Rectangles et trapèzes · `riemann_sum, trapezoid` | ★ | 20 | §1 §5 | C, E | pytest | — |
| M02a.17 | 🔨 | La méthode de Simpson · `simpson` | ★★ | 15 | §5 | C | pytest | M02a.16 |
| M02a.18 | 🔨 | De la densité à la fonction de répartition, puis au quantile par dichotomie · `cdf_from_pdf, quantile` | ★★ | 25 | §7 | C, E | pytest | M02a.16 |
| M02a.19 | 📦 | Vérifier avec `scipy.integrate.quad` et SymPy | ★ | 15 | §2 §4 | C, E | wbm | — |
| M02a.20 | 🔮 | Prédire : le pas divisé par 2, l'erreur divisée par combien ? | ★ | 10 | §5 | C, E | wbm | — |
| M02a.21 | 🔬 | L'intégrale de Gauss par le calcul : la borne qui s'éloigne | ★★ | 20 | §4 | C | wbm | — |
| M02a.22 | 🎨 | L'aire qui se remplit : la courbe, les rectangles et la primitive | ★ | 20 | §1 §2 | C, E | manuel | — |
| M02a.23 | 🐛 | Chasse à l'erreur : bornes inversées, primitive fausse, aire négative | ★ | 15 | §2 §3 | C | wbm | — |
| M02a.24 | 🛠️ | Vérifier une primitive avec SymPy : dériver le résultat | ★ | 10 | §2 | C | manuel | — |
| M02a.25 | 🏆 | Défi : la meilleure précision avec dix évaluations de la fonction | ★★★ | 30 | §5 | C | wbm | — |

*Notes* : Parcours essentiel : intégration par parties, changement de variable et Simpson hors parcours (workbookIA 2 n'en a pas besoin). 📖 : MML §6.2 n'est lu qu'en partie ici (la partie continue) ; M02b le lit en entier.

<a id="m02b"></a>
## M02b · Variables aléatoires et lois usuelles

**Partie** I · **prépare** workbookIA 2 · **dossier** `chapitres/m02b_variables_aleatoires/` · **MML** §6.1, §6.2, §6.4, §6.7 · **sessions de génération** 1

Les variables aléatoires discrètes et continues et leurs lois usuelles, l'espérance et la variance, les couples de variables (loi jointe, marginales, indépendance, variance d'une somme), une première intégrale double, le changement de variable et la simulation par inversion.

**Temps** : 13,9 h en parcours complet, 8,7 h en parcours essentiel (lecture 180 min, 25 flashcards).

**Objectifs**

- Reconnaître la loi qui modélise une situation (Bernoulli, binomiale, catégorielle, géométrique, Poisson, uniforme, exponentielle, normale).
- Calculer des probabilités, une espérance et une variance, pour une loi discrète ou continue.
- Lire une loi jointe, ses marginales, et décider de l'indépendance de deux variables.
- Utiliser la linéarité de l'espérance et la variance d'une somme de variables indépendantes.
- Calculer une intégrale double simple et la loi d'une variable transformée.
- Simuler une loi par inversion de sa fonction de répartition.

**Sections de la fiche**

- §1 Variable aléatoire et loi : l'espace probabilisé (aperçu)
- §2 Lois discrètes : Bernoulli, binomiale, catégorielle, géométrique, Poisson
- §3 Lois continues : uniforme, exponentielle, normale
- §4 Espérance et variance ; théorème de transfert
- §5 Couples de variables : loi jointe, marginales, indépendance
- §6 Linéarité de l'espérance, variance d'une somme
- §7 Intégrale double (premier contact) et intégrale de Gauss
- §8 Changement de variable et simulation

**Notions enseignées** : espace probabilisé (aperçu) · lois discrètes : Bernoulli, binomiale, catégorielle, géométrique, Poisson · lois continues : uniforme, exponentielle, normale · espérance d'une variable continue · variance, propriétés · couples de variables discrètes : loi jointe, marginales · indépendance de deux variables aléatoires · linéarité de l'espérance · variance d'une somme de variables indépendantes · intégrale double sur un rectangle, densité jointe, marginale par intégration (premier contact) · l'intégrale de Gauss par une intégrale double · théorème de transfert · changement de variable · simulation par inversion · tirage catégoriel

**Prérequis** : variable aléatoire discrète, espérance, variance (R8) · dénombrement, coefficients binomiaux (R8) · intégrale, densité, fonction de répartition (M02a) · intégrales impropres (M02a) · suites géométriques et leurs sommes (R5)

**mymath** : `distributions.py` (signatures figées) : `binomial_pmf`, `poisson_pmf`, `normal_pdf`, `normal_cdf`, `inverse_transform_sample`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 2.8 ∂ Changer d'unité : la covariance bouge, pas la corrélation · 2.3 ✏️ La règle 68-95-99,7 sur les nageoires des manchots · 2.5 ✏️ Espérances : Bernoulli, multinoulli et jeu de hasard · 2.17 🎨 Galerie des lois usuelles · 2.18 🔬 68-95-99,7 : la théorie face aux tirages et aux manchots · 2.19 🔨 La roue de la fortune : tirer dans une distribution discrète · 2.20 🔮 Le pelage des animaux : une variable qui dépend d'une autre

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M02b.Q1 | 🧠 | Discrète ou continue ? | ★ | 4 | §1 | C, E | manuel | — |
| M02b.Q2 | 🧠 | Quelle loi pour quelle situation ? | ★ | 4 | §2 §3 | C, E | manuel | — |
| M02b.Q3 | 🧠 | Espérance et variance : vrai ou faux | ★ | 4 | §4 | C, E | manuel | — |
| M02b.Q4 | 🧠 | La loi normale : ce que disent μ et σ | ★ | 4 | §3 | C, E | manuel | — |
| M02b.Q5 | 🧠 | Jointe, marginale, indépendance | ★ | 4 | §5 | C, E | manuel | — |
| M02b.Q6 | 🧠 | La variance d'une somme | ★ | 4 | §6 | C, E | manuel | — |
| M02b.Q7 | 🧠 | Simuler une loi | ★ | 4 | §8 | C | manuel | — |
| M02b.R1 | 🔁 | Espérance d'une variable discrète (R8) | ★ | 5 | §4 | C, E | manuel | — |
| M02b.R2 | 🔁 | Intégrales et densités (M02a) | ★ | 5 | §3 §4 | C, E | manuel | — |
| M02b.R3 | 🔁 | Coefficients binomiaux (R8) | ★ | 5 | §2 | C | manuel | — |
| M02b.1 | ✏️ | Loi de Bernoulli et loi binomiale | ★ | 20 | §2 | C, E | wbm | — |
| M02b.2 | ✏️ | Loi géométrique : probabilités, et l'espérance par une série | ★★ | 20 | §2 §4 | C, E | wbm | — |
| M02b.3 | ✏️ | Loi de Poisson : probabilités, espérance, et la somme de deux variables de Poisson indépendantes | ★★ | 20 | §2 | C | wbm | — |
| M02b.4 | ✏️ | Lois uniforme et exponentielle : probabilités et espérance | ★ | 20 | §3 §4 | C, E | wbm | — |
| M02b.5 | ✏️ | Loi normale : standardiser et lire la fonction Φ | ★★ | 20 | §3 | C, E | wbm | — |
| M02b.6 | ✏️ | Espérance et variance d'une variable continue (théorème de transfert) | ★★ | 20 | §4 | C, E | wbm | — |
| M02b.7 | ✏️ | Un couple de variables discrètes : loi jointe, marginales, indépendance | ★★ | 20 | §5 | C, E | wbm | — |
| M02b.8 | ✏️ | Linéarité et variance d'une somme : sommes et moyennes de variables | ★★ | 20 | §6 | C, E | wbm | — |
| M02b.9 | ✏️ | Une intégrale double sur un rectangle, et une densité jointe | ★★ | 20 | §7 | C | wbm | — |
| M02b.10 | ✏️ | Changement de variable : la loi de aX + b, et celle de X² | ★★ | 20 | §8 | C | wbm | — |
| M02b.11 | ∂ | La variance d'une somme de variables indépendantes | ★★ | 25 | §6 | C, E | manuel | — |
| M02b.12 | ∂ | L'intégrale de Gauss par une intégrale double (changement en coordonnées polaires admis) | ★★★ | 30 | §7 | C | manuel | — |
| M02b.13 | ∂ | La loi de Poisson, limite de lois binomiales | ★★ | 25 | §2 | C | manuel | — |
| M02b.14 | 🔗 | Combien d'erreurs d'annotation dans un dataset ? Binomiale et Poisson | ★ | 15 | §2 | C, E | wbm | — |
| M02b.15 | 📖 | MML §6.1 et §6.2 : espace probabilisé, pmf et pdf, en anglais | ★★ | 30 | §1 §2 §3 | C | manuel | — |
| M02b.16 | 📖 | MML §6.4 et §6.7 : espérance, variance, sommes de variables, changement de variable | ★★ | 30 | §4 §6 §8 | C | manuel | — |
| M02b.17 | 🗣️ | Expliquer la différence entre une variable aléatoire et sa loi | ★ | 10 | §1 | C | manuel | — |
| M02b.E1 | 💼 | Quand modéliser un comptage par une loi de Poisson ? | ★ | 10 | §2 | C, E | manuel | — |
| M02b.18 | 🔨 | Lois binomiale et de Poisson · `binomial_pmf, poisson_pmf` | ★ | 20 | §2 | C, E | pytest | — |
| M02b.19 | 🔨 | Densité et fonction de répartition de la loi normale (avec `math.erf`) · `normal_pdf, normal_cdf` | ★ | 20 | §3 | C, E | pytest | — |
| M02b.20 | 🔨 | Simuler par inversion de la fonction de répartition · `inverse_transform_sample` | ★★ | 20 | §8 | C | pytest | — |
| M02b.21 | 📦 | `scipy.stats` : pmf, pdf, cdf, ppf et rvs | ★ | 15 | §2 §3 | C, E | wbm | — |
| M02b.22 | 🔮 | Prédire : la variance de la moyenne de quatre dés | ★ | 10 | §6 | C, E | wbm | — |
| M02b.23 | 🔬 | Binomiale et Poisson côte à côte quand n grandit | ★★ | 20 | §2 | C | wbm | — |
| M02b.24 | 🎨 | Une loi jointe en carte de chaleur, ses marginales sur les bords | ★ | 20 | §5 | C | manuel | — |
| M02b.25 | 🐛 | Chasse à l'erreur : une densité prise pour une probabilité, σ et σ² | ★ | 15 | §3 §6 | C | wbm | — |
| M02b.26 | 🛠️ | Documenter une loi : docstring et exemples testés (`doctest`) | ★ | 15 | §3 | C | manuel | — |
| M02b.27 | 🏆 | Défi : tirer des valeurs normales avec seulement des tirages uniformes | ★★★ | 30 | §8 | C | wbm | — |

*Notes* : La loi catégorielle est dans la fiche et les quiz, sans ✏️ propre (workbookIA 2.5 calcule son espérance, 2.19 programme son tirage) ; la règle 68-95-99,7 n'est pas un exercice (workbookIA 2.3 et 2.18). Parcours essentiel : l'intégrale double, l'intégrale de Gauss et la limite de Poisson hors parcours.

<a id="m02c"></a>
## M02c · Échantillons et estimation

**Partie** I · **prépare** workbookIA 2 · **dossier** `chapitres/m02c_echantillons_estimation/` · **MML** §6.4 · **sessions de génération** 1

De la loi à l'échantillon : variables i.i.d., tirages avec et sans remise, loi des grands nombres et théorème central limite, estimateurs, leur biais et leur erreur quadratique (le ddof), erreur type, intervalles de confiance et bootstrap ; puis la covariance et la corrélation, et une première matrice de covariance.

**Temps** : 13,8 h en parcours complet, 9,0 h en parcours essentiel (lecture 180 min, 25 flashcards).

**Objectifs**

- Résumer une série (moyenne, médiane, quantiles, variance) et repérer ses valeurs aberrantes.
- Énoncer la loi des grands nombres et le théorème central limite, et s'en servir pour une probabilité.
- Calculer le biais, la variance et l'erreur quadratique d'un estimateur, et justifier le n − 1.
- Calculer une erreur type et un intervalle de confiance pour une moyenne.
- Calculer une covariance, une corrélation et une matrice de covariance, et les interpréter.
- Reconnaître un biais d'échantillonnage et l'effet d'une imputation.

**Sections de la fiche**

- §1 Statistiques descriptives : moyenne, médiane, variance, quantiles
- §2 Standardiser : z-score ; valeurs aberrantes
- §3 Échantillon i.i.d., tirages avec et sans remise
- §4 Loi des grands nombres
- §5 Théorème central limite
- §6 Estimateurs : biais, variance, erreur quadratique ; le ddof
- §7 Erreur type, intervalle de confiance et bootstrap (principe)
- §8 Covariance, corrélation, matrice de covariance
- §9 Données réelles : imputation, biais d'échantillonnage, grande dimension

**Notions enseignées** : statistiques descriptives : moyenne, médiane, variance, quantiles · z-score, standardisation · échantillon i.i.d. · tirages avec et sans remise · loi des grands nombres · théorème central limite · estimateur, biais, ddof · erreur quadratique d'un estimateur · erreur type · intervalle de confiance · bootstrap (principe) · covariance et corrélation · matrice de covariance (première rencontre) · valeurs aberrantes : z-score et écart interquartile · imputer par la moyenne ou la médiane : ce que cela change · biais d'échantillonnage · grande dimension (premières surprises) · percentiles d'une mesure (latence)

**Prérequis** : espérance, variance, variance d'une somme (M02b) · loi normale, fonction Φ (M02b) · quantiles (M02a) · Σ (R4) · produit scalaire, norme (R9)

**mymath** : `estimation.py` (signatures figées) : `sample_means`, `estimator_bias`, `estimator_mse`, `standard_error`, `confidence_interval_mean`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 2.8 ∂ Changer d'unité : la covariance bouge, pas la corrélation · 2.1 ✏️ Moyenne, médiane et mode d'une liste de salaires · 2.4 ✏️ Variance : diviser par N ou par N − 1 ? · 2.7 ✏️ Covariance et corrélation de cinq points à la main · 2.9 🗣️ Le bootstrap en cinq lignes · 2.22 🔨 Bootstrap : distribution et intervalle de confiance · 2.25 📦 Distances entre chiffres dans l'espace à 784 dimensions · 2.29 🐛 Le piège de ddof : NumPy, pandas et toi · 2.E4 💼 Corrélation nulle veut-elle dire indépendance ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M02c.Q1 | 🧠 | Résumer une série : vrai ou faux | ★ | 4 | §1 | C, E | manuel | — |
| M02c.Q2 | 🧠 | z-scores et valeurs aberrantes | ★ | 4 | §2 | C, E | manuel | — |
| M02c.Q3 | 🧠 | i.i.d. ou pas ? | ★ | 4 | §3 | C, E | manuel | — |
| M02c.Q4 | 🧠 | Grands nombres et TCL : ce qu'ils disent, ce qu'ils ne disent pas | ★ | 4 | §4 §5 | C, E | manuel | — |
| M02c.Q5 | 🧠 | Biais, variance et ddof | ★ | 4 | §6 | C, E | manuel | — |
| M02c.Q6 | 🧠 | Lire un intervalle de confiance | ★ | 4 | §7 | C, E | manuel | — |
| M02c.Q7 | 🧠 | Covariance et corrélation : vrai ou faux | ★ | 4 | §8 | C, E | manuel | — |
| M02c.R1 | 🔁 | Espérance et variance d'une somme (M02b) | ★ | 5 | §4 §6 | C, E | manuel | — |
| M02c.R2 | 🔁 | Loi normale et fonction Φ (M02b) | ★ | 5 | §5 | C, E | manuel | — |
| M02c.R3 | 🔁 | Racines et puissances (R1) | ★ | 5 | §7 | C | manuel | — |
| M02c.1 | ✏️ | Les statistiques d'une petite série : moyenne, médiane, quartiles, variance | ★ | 20 | §1 | C, E | wbm | — |
| M02c.2 | ✏️ | z-scores, écart interquartile et valeurs aberrantes | ★ | 15 | §2 | C, E | wbm | — |
| M02c.3 | ✏️ | Imputer par la moyenne ou la médiane : ce qui change | ★ | 15 | §9 | C | wbm | — |
| M02c.4 | ✏️ | Avec ou sans remise : la variance de la moyenne | ★★ | 20 | §3 | C | wbm | — |
| M02c.5 | ✏️ | Combien d'observations pour une moyenne précise à 1 % ? | ★★ | 20 | §4 §5 | C, E | wbm | — |
| M02c.6 | ✏️ | Le théorème central limite à la main : une somme de 100 variables | ★★ | 20 | §5 | C, E | wbm | — |
| M02c.7 | ✏️ | Biais, variance et erreur quadratique de trois estimateurs | ★★ | 25 | §6 | C, E | wbm | — |
| M02c.8 | ✏️ | Erreur type et intervalle de confiance d'une moyenne | ★★ | 20 | §7 | C, E | wbm | — |
| M02c.9 | ✏️ | La variance d'une somme et la covariance : V(X + Y), V(X − Y) | ★★ | 20 | §8 | C, E | wbm | — |
| M02c.10 | ✏️ | La matrice de covariance de trois variables : la lire et la vérifier | ★★ | 20 | §8 | C | wbm | — |
| M02c.11 | ∂ | Pourquoi diviser par n − 1 : E[S²] = σ² | ★★★ | 30 | §6 | C | manuel | — |
| M02c.12 | ∂ | La variance de la moyenne : V(X̄) = σ²/n, et l'erreur type | ★★ | 20 | §5 §7 | C, E | manuel | — |
| M02c.13 | 🔗 | Le 99e percentile d'une latence : l'estimer et dire son incertitude | ★★ | 20 | §1 §7 | C, E | wbm | — |
| M02c.14 | 🔗 | Standardiser des features avec les statistiques du seul train | ★ | 15 | §2 | C | wbm | — |
| M02c.15 | 📖 | MML §6.4 : moyennes et covariances empiriques, en anglais | ★★ | 30 | §1 §8 | C | manuel | — |
| M02c.16 | ⚖️ | Le biais du survivant : des données qui ne montrent que ceux qui restent | ★ | 15 | §9 | C | manuel | — |
| M02c.17 | 🗣️ | Expliquer le théorème central limite avec un histogramme | ★ | 10 | §5 | C, E | manuel | — |
| M02c.E1 | 💼 | L'erreur type décroît en 1/√n : qu'est-ce que cela change pour un jeu de test ? | ★ | 10 | §7 | C, E | manuel | — |
| M02c.18 | 🔨 | La distribution des moyennes d'échantillons · `sample_means` | ★ | 20 | §5 | C, E | pytest | — |
| M02c.19 | 🔨 | Biais et erreur quadratique d'un estimateur, par simulation · `estimator_bias, estimator_mse` | ★★ | 25 | §6 | C | pytest | — |
| M02c.20 | 🔨 | Erreur type et intervalle de confiance · `standard_error, confidence_interval_mean` | ★ | 20 | §7 | C, E | pytest | — |
| M02c.21 | 📦 | NumPy et SciPy : `ddof`, `np.percentile`, `scipy.stats.sem` | ★ | 15 | §1 §7 | C | wbm | — |
| M02c.22 | 🔮 | Prédire : l'histogramme des moyennes d'une loi exponentielle quand n grandit | ★ | 10 | §5 | C, E | wbm | — |
| M02c.23 | 🔬 | Couverture : 95 % des intervalles contiennent-ils la vraie moyenne ? | ★★ | 20 | §7 | C, E | wbm | — |
| M02c.24 | 🔬 | Grande dimension : le cube dont le centre est vide | ★★ | 20 | §9 | C | wbm | — |
| M02c.25 | 🎨 | Voir le théorème central limite : histogrammes et densité normale | ★ | 20 | §5 | C | manuel | — |
| M02c.26 | 🐛 | Chasse à l'erreur : un intervalle de confiance mal calculé | ★ | 15 | §7 | C | wbm | — |
| M02c.27 | 🛠️ | Tester une fonction aléatoire : une tolérance en erreurs types | ★ | 15 | §5 §7 | C | manuel | — |
| M02c.28 | 🏆 | Défi : un intervalle à 95 % avec dix valeurs d'une loi asymétrique | ★★★ | 30 | §7 | C | wbm | — |

*Notes* : mymath étudie les estimateurs (biais, erreur quadratique, théorème central limite par simulation) ; les fonctions de statistiques descriptives et de bootstrap sont celles de `mylearn` en workbookIA 2. Le 🐛 ne repose pas sur le ddof (workbookIA 2.29), le quiz ne demande pas si une corrélation nulle implique l'indépendance (workbookIA 2.E4). Parcours essentiel : la démonstration de E[S²] = σ², les tirages sans remise et la grande dimension hors parcours.

<a id="m03"></a>
## M03 · Probabilités conditionnelles

**Partie** I · **prépare** workbookIA 3 · **dossier** `chapitres/m03_probabilites_conditionnelles/` · **MML** §6.3 · **sessions de génération** 1

Les probabilités jointes, marginales et conditionnelles, les tableaux de contingence, l'indépendance et la formule des probabilités totales ; puis les métriques de classification vues comme des probabilités conditionnelles, leurs moyennes, la prévalence, et l'AUC comme une aire et comme une probabilité.

**Temps** : 12,8 h en parcours complet, 7,2 h en parcours essentiel (lecture 150 min, 22 flashcards).

**Objectifs**

- Lire dans un tableau de contingence des probabilités jointes, marginales et conditionnelles.
- Décider de l'indépendance de deux événements ou de deux variables par le calcul.
- Utiliser la formule des probabilités totales.
- Écrire accuracy, precision, recall et spécificité comme des probabilités, et calculer leurs moyennes.
- Mesurer l'effet de la prévalence et du seuil de décision sur ces métriques.
- Calculer une AUC comme une aire et comme une proportion de paires, une average precision et un score de Brier.

**Sections de la fiche**

- §1 Probabilité jointe, marginale, tableau de contingence
- §2 Probabilité conditionnelle et indépendance
- §3 Probabilités totales
- §4 La matrice de confusion, un tableau de contingence
- §5 Moyennes de métriques : F-beta, macro, micro, pondérée ; balanced accuracy et MCC
- §6 Prévalence, classes déséquilibrées et seuil de décision
- §7 Courbe ROC et AUC, courbe precision-recall et average precision
- §8 Calibration, score de Brier, taux par groupe

**Notions enseignées** : probabilité jointe · probabilité marginale · tableau de contingence · probabilité conditionnelle · indépendance · probabilités totales (énoncée et utilisée) · precision, recall, spécificité, accuracy comme probabilités · F-beta (moyenne harmonique pondérée) · moyennes macro, micro et pondérée · prévalence et classes déséquilibrées : repondérer · courbe ROC et AUC · AUC comme probabilité de bien classer une paire · courbe precision-recall · average precision : une aire sous la courbe precision-recall · calibration et score de Brier · taux par groupe (équité, premier contact) · matrice de confusion : un tableau de contingence · balanced accuracy : la moyenne des rappels · MCC : une corrélation entre deux variables binaires · seuil de décision et compromis · paradoxe de Simpson

**Prérequis** : probabilités, arbres, indépendance d'événements (R8) · moyenne harmonique et moyenne pondérée (R1) · aire, méthode des trapèzes (M02a) · corrélation (M02c)

**mymath** : `conditional.py` (signatures figées) : `joint_from_counts`, `marginal`, `conditional`, `are_independent`, `auc_by_pairs`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 3.4 ∂ Règle du produit et formule des probabilités totales · 3.8 ∂ F1, moyenne harmonique : pourquoi elle punit le maillon faible · 3.1 ✏️ Fléchettes et aires : probabilités simples et conditionnelles · 3.2 ✏️ Les 20 points : matrice de confusion et quatre mesures · 3.3 ✏️ Le glacier : jointes, marginales et conditionnelles · 3.6 ✏️ Trois espèces : moyennes macro, micro et pondérée · 3.7 ✏️ Le test « fiable à 99 % » dans une ville à 1 % de malades · 3.13 🔮 Deux disques : P(A|B) = P(B|A) ? · 3.14 📦 Penguins : espèce × île avec pd.crosstab · 3.21 🔬 Simuler le dépistage : la prévalence fait la precision · 3.29 🏆 Recall ≥ 0,99 au meilleur prix · 3.E1 💼 99 % d'accuracy sur la détection de fraude : bonne nouvelle ? · 3.E3 💼 Expliquer la courbe ROC et l'AUC

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M03.Q1 | 🧠 | Jointe, marginale ou conditionnelle ? | ★ | 4 | §1 §2 | C, E | manuel | — |
| M03.Q2 | 🧠 | P(A sachant B) et P(B sachant A) | ★ | 4 | §2 | C, E | manuel | — |
| M03.Q3 | 🧠 | Indépendants ou incompatibles ? | ★ | 4 | §2 | C, E | manuel | — |
| M03.Q4 | 🧠 | Quelle métrique pour quelle probabilité ? | ★ | 4 | §4 | C, E | manuel | — |
| M03.Q5 | 🧠 | Moyennes de métriques | ★ | 4 | §5 | C | manuel | — |
| M03.Q6 | 🧠 | ROC et AUC : vrai ou faux | ★ | 4 | §7 | C, E | manuel | — |
| M03.Q7 | 🧠 | Calibré ou pas ? | ★ | 4 | §8 | C | manuel | — |
| M03.R1 | 🔁 | Arbres pondérés (R8) | ★ | 5 | §3 | C, E | manuel | — |
| M03.R2 | 🔁 | Moyenne harmonique et moyenne pondérée (R1) | ★ | 5 | §5 | C, E | manuel | — |
| M03.R3 | 🔁 | Aire par la méthode des trapèzes (M02a) | ★ | 5 | §7 | C | manuel | — |
| M03.1 | ✏️ | Un tableau de contingence : jointes, marginales, conditionnelles | ★ | 20 | §1 §2 | C, E | wbm | — |
| M03.2 | ✏️ | L'indépendance, vérifiée dans un tableau | ★ | 15 | §2 | C, E | wbm | — |
| M03.3 | ✏️ | Probabilités totales avec trois cas | ★ | 15 | §3 | C, E | wbm | — |
| M03.4 | ✏️ | Une matrice de confusion lue comme des probabilités | ★ | 20 | §4 | C, E | wbm | — |
| M03.5 | ✏️ | F-beta : quel β pour quel coût d'erreur ? | ★★ | 20 | §5 | C | wbm | — |
| M03.6 | ✏️ | Balanced accuracy et MCC sur un problème déséquilibré | ★★ | 20 | §5 §6 | C | wbm | — |
| M03.7 | ✏️ | Changer de population : recalculer la precision quand la prévalence change | ★★ | 20 | §6 | C, E | wbm | — |
| M03.8 | ✏️ | Une courbe ROC à la main, et son aire par les trapèzes | ★★ | 20 | §7 | C, E | wbm | — |
| M03.9 | ✏️ | L'AUC comme proportion de paires bien classées | ★★ | 20 | §7 | C, E | wbm | — |
| M03.10 | ✏️ | Courbe precision-recall et average precision à la main | ★★ | 20 | §7 | C | wbm | — |
| M03.11 | ✏️ | Score de Brier et calibration de huit prévisions | ★ | 15 | §8 | C | wbm | — |
| M03.12 | ∂ | L'aire sous la courbe ROC compte les paires bien classées | ★★★ | 30 | §7 | C | manuel | — |
| M03.13 | ∂ | En multiclasse, micro-precision, micro-recall et accuracy sont égaux | ★★ | 20 | §5 | C | manuel | — |
| M03.14 | 🔗 | Un seuil sur un score : trois seuils, trois matrices de confusion | ★ | 20 | §6 | C, E | wbm | — |
| M03.15 | 🔗 | Équité : les taux de faux positifs de deux groupes | ★★ | 15 | §8 | C | wbm | — |
| M03.16 | 📖 | MML §6.3 : règle de la somme, règle du produit et vocabulaire, en anglais | ★★ | 30 | §1 §2 §3 | C | manuel | — |
| M03.17 | ⚖️ | Un taux de réussite trompeur : le paradoxe de Simpson | ★★ | 20 | §2 §3 | C | manuel | — |
| M03.18 | 🗣️ | Expliquer pourquoi P(A sachant B) n'est pas P(B sachant A) | ★ | 10 | §2 | C, E | manuel | — |
| M03.E1 | 💼 | Une variable indépendante de la cible peut-elle aider un modèle ? | ★ | 10 | §2 | C | manuel | — |
| M03.19 | 🔨 | Jointe, marginales et conditionnelles à partir d'un tableau de comptages · `joint_from_counts, marginal, conditional` | ★ | 20 | §1 §2 | C, E | pytest | — |
| M03.20 | 🔨 | Tester l'indépendance avec une tolérance · `are_independent` | ★ | 15 | §2 | C | pytest | M03.19 |
| M03.21 | 🔨 | L'AUC en comptant les paires · `auc_by_pairs` | ★★ | 20 | §7 | C, E | pytest | — |
| M03.22 | 📦 | `sklearn.metrics.roc_auc_score` contre le comptage des paires, ex aequo compris | ★ | 15 | §7 | C | wbm | — |
| M03.23 | 🔮 | Prédire : l'AUC après une transformation croissante des scores | ★ | 10 | §7 | C, E | wbm | — |
| M03.24 | 🔬 | Simuler pour estimer une probabilité conditionnelle | ★★ | 20 | §2 | C | wbm | — |
| M03.25 | 🎨 | La courbe ROC en escalier : une case par paire | ★ | 20 | §7 | C | manuel | — |
| M03.26 | 🐛 | Chasse à l'erreur : conditionnelle inversée, marginale oubliée | ★ | 15 | §2 §3 | C | wbm | — |
| M03.27 | 🛠️ | Une fonction qui refuse un tableau invalide (`ValueError`) | ★ | 10 | §1 | C | manuel | — |
| M03.28 | 🏆 | Défi : retrouver un tableau de contingence à partir de quelques probabilités | ★★★ | 25 | §1 §3 | C | wbm | — |

*Notes* : workbookIA 3 calcule les métriques sur des données ; ce chapitre les écrit comme des probabilités conditionnelles, sur d'autres exemples, et démontre l'AUC comme probabilité. Ni fléchettes, ni glacier, ni test médical à 99 %, ni prévisions météo (workbookIA 3.1, 3.3, 3.7, 3.28). Parcours essentiel : MCC, average precision et taux par groupe hors parcours.

<a id="m04"></a>
## M04 · Bayes, vraisemblance et loi Beta

**Partie** I · **prépare** workbookIA 4 · **dossier** `chapitres/m04_bayes_beta/` · **MML** §6.3, §6.6, §8.3 · **sessions de génération** 1

La formule de Bayes en profondeur : a priori, vraisemblance, évidence, a posteriori, mises à jour successives, hypothèses multiples ; la loi Beta, la conjugaison avec la binomiale et un aperçu de la famille exponentielle, le lissage de Laplace, le MAP, les log-probabilités et les intervalles de crédibilité.

**Temps** : 12,9 h en parcours complet, 8,2 h en parcours essentiel (lecture 150 min, 22 flashcards).

**Objectifs**

- Appliquer la formule de Bayes à deux hypothèses ou plus, une fois ou en boucle.
- Écrire une vraisemblance et trouver son maximum.
- Calculer la densité, la moyenne, le mode et la variance d'une loi Beta.
- Mettre à jour une loi Beta par conjugaison, et en déduire le MAP, la moyenne a posteriori et la probabilité prédictive.
- Calculer avec des log-probabilités pour éviter l'underflow.
- Distinguer les points de vue fréquentiste et bayésien.

**Sections de la fiche**

- §1 La formule de Bayes : a priori, vraisemblance, évidence, a posteriori
- §2 Hypothèses multiples et mises à jour successives
- §3 Vraisemblance et maximum de vraisemblance
- §4 La loi Beta
- §5 Conjugaison Beta-binomiale, lissage de Laplace, prédictive
- §6 MAP et intervalle de crédibilité
- §7 Log-probabilités, underflow et log-sum-exp ; famille exponentielle (aperçu)
- §8 Fréquentiste et bayésien ; échantillonnage de Thompson (premier contact)

**Notions enseignées** : formule de Bayes · a priori, vraisemblance, évidence, a posteriori · mise à jour séquentielle · hypothèses multiples · argmax et MAP · maximum de vraisemblance (premier contact) · loi Beta · conjugaison Beta-binomiale · famille exponentielle (aperçu : Bernoulli, gaussienne, Beta) · lissage de Laplace · log-probabilités et underflow · log-sum-exp : normaliser des log-probabilités · intervalle de crédibilité · fréquentiste et bayésien · échantillonnage de Thompson (premier contact)

**Prérequis** : probabilité conditionnelle, probabilités totales (M03) · loi binomiale (M02b) · densité, intégrale (M02a) · logarithmes (R6) · dériver, maximum (R7)

**mymath** : `bayes.py` (signatures figées) : `beta_pdf`, `beta_moments`, `conjugate_beta_update`, `posterior_predictive`, `map_estimate_beta`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 4.3 ∂ Retrouver la règle de Bayes en trois lignes · 4.7 ∂ Le posterior reste une distribution, un prior nul reste nul · 4.1 ✏️ Une face : la pièce est-elle équilibrée ? · 4.2 ✏️ Une pile : le verdict s'inverse · 4.4 ✏️ Vie extraterrestre : lire la sonde avec Bayes · 4.5 ✏️ Deux faces : une mise à jour double ou deux simples ? · 4.6 ✏️ Cinq hypothèses de biais après face, pile, face · 4.8 ✏️ Combien de sondes pour descendre sous un sur un million ? · 4.12 🔮 Combien de lancers pour démasquer la pièce truquée ? · 4.21 🔮 Un prior trompeur centré sur 0,8 · 4.22 📦 Le posterior continu : vérifier avec scipy.stats.beta · 4.24 🔨 coin_bias_posterior : 500 hypothèses en log-probabilités · 4.25 🔨 Intervalle de crédibilité contre intervalle bootstrap · 4.E1 💼 Expliquer la règle de Bayes avec un test médical

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M04.Q1 | 🧠 | Les quatre termes de la formule de Bayes | ★ | 4 | §1 | C, E | manuel | — |
| M04.Q2 | 🧠 | Mettre à jour deux fois | ★ | 4 | §2 | C, E | manuel | — |
| M04.Q3 | 🧠 | La vraisemblance, une fonction du paramètre | ★ | 4 | §3 | C, E | manuel | — |
| M04.Q4 | 🧠 | La loi Beta : forme et paramètres | ★ | 4 | §4 | C, E | manuel | — |
| M04.Q5 | 🧠 | Conjuguée, Laplace, MAP | ★ | 4 | §5 §6 | C, E | manuel | — |
| M04.Q6 | 🧠 | Logarithmes et underflow | ★ | 4 | §7 | C | manuel | — |
| M04.Q7 | 🧠 | Fréquentiste ou bayésien ? | ★ | 4 | §8 | C | manuel | — |
| M04.R1 | 🔁 | Probabilités conditionnelles (M03) | ★ | 5 | §1 | C, E | manuel | — |
| M04.R2 | 🔁 | Intégrales et densités (M02a) | ★ | 5 | §4 | C, E | manuel | — |
| M04.R3 | 🔁 | Loi binomiale (M02b) | ★ | 5 | §5 | C | manuel | — |
| M04.1 | ✏️ | Bayes avec deux hypothèses : un capteur de fuite d'eau | ★ | 20 | §1 | C, E | wbm | — |
| M04.2 | ✏️ | Trois hypothèses et un tableau de mise à jour | ★★ | 20 | §2 | C, E | wbm | — |
| M04.3 | ✏️ | La vraisemblance d'un taux de clic | ★ | 20 | §3 | C, E | wbm | — |
| M04.4 | ✏️ | Maximiser une vraisemblance : dériver son logarithme | ★★ | 20 | §3 | C, E | wbm | — |
| M04.5 | ✏️ | La loi Beta : normalisation, moyenne, mode, variance | ★★ | 20 | §4 | C, E | wbm | — |
| M04.6 | ✏️ | Conjugaison : de Beta(a, b) à Beta(a + k, b + n − k) | ★ | 20 | §5 | C, E | wbm | — |
| M04.7 | ✏️ | Lissage de Laplace : la prédictive avec Beta(1, 1) | ★ | 15 | §5 | C | wbm | — |
| M04.8 | ✏️ | MAP, maximum de vraisemblance et moyenne a posteriori | ★★ | 20 | §6 | C, E | wbm | — |
| M04.9 | ✏️ | Un intervalle de crédibilité d'une loi Beta | ★★ | 15 | §6 | C | wbm | — |
| M04.10 | ✏️ | Log-probabilités : additionner au lieu de multiplier, normaliser par log-sum-exp | ★ | 20 | §7 | C, E | wbm | — |
| M04.11 | ∂ | La conjugaison Beta-binomiale, démontrée | ★★ | 25 | §5 | C | manuel | — |
| M04.12 | ∂ | Le maximum de vraisemblance d'une loi de Bernoulli est la fréquence | ★★ | 20 | §3 | C | manuel | — |
| M04.13 | ∂ | Le mode de la loi Beta | ★★ | 20 | §4 §6 | C | manuel | — |
| M04.14 | 🔗 | Un test A/B : deux taux de conversion et P(θB > θA) par simulation | ★★ | 20 | §5 §8 | C, E | wbm | — |
| M04.15 | 📖 | MML §6.3 (relire le théorème de Bayes) et §6.6 : conjugaison et famille exponentielle (lecture guidée) | ★★ | 30 | §1 §5 §7 | C | manuel | — |
| M04.16 | 📖 | MML §8.3 : maximum de vraisemblance et MAP (lecture guidée) | ★★ | 30 | §3 §6 | C | manuel | — |
| M04.17 | 🗣️ | Expliquer la conjugaison avec des pseudo-observations | ★ | 10 | §5 | C, E | manuel | — |
| M04.E1 | 💼 | Qu'est-ce que le lissage de Laplace, et pourquoi l'utiliser ? | ★ | 10 | §5 | C, E | manuel | — |
| M04.18 | 🔨 | Densité et moments de la loi Beta (avec `math.lgamma`) · `beta_pdf, beta_moments` | ★ | 20 | §4 | C, E | pytest | — |
| M04.19 | 🔨 | Mise à jour conjuguée et loi prédictive des prochains essais · `conjugate_beta_update, posterior_predictive` | ★★ | 25 | §5 | C, E | pytest | M04.18 |
| M04.20 | 🔨 | Le MAP d'une loi Beta, cas limites compris · `map_estimate_beta` | ★★ | 15 | §6 | C | pytest | — |
| M04.21 | 📦 | La fonction Beta avec `scipy.special` : `beta`, `betaln` et l'underflow | ★ | 15 | §4 §7 | C | wbm | — |
| M04.22 | 🔮 | Prédire : le MAP avec Beta(1, 1) après trois échecs | ★ | 10 | §6 | C | wbm | — |
| M04.23 | 🔬 | Le posterior se resserre : la largeur de l'intervalle en 1/√n | ★★ | 20 | §6 | C | wbm | — |
| M04.24 | 🎨 | Prior, vraisemblance et posterior sur une même figure | ★ | 20 | §5 | C, E | manuel | — |
| M04.25 | 🐛 | Chasse à l'erreur : évidence oubliée, mise à jour à l'envers, mode et moyenne | ★ | 15 | §1 §5 | C | wbm | — |
| M04.26 | 🛠️ | Un calcul stable : comparer des vraisemblances en logarithmes (`math.lgamma`) | ★ | 15 | §7 | C | manuel | — |
| M04.27 | 🏆 | Défi : traduire l'avis d'un expert en une loi Beta (moyenne, écart-type, intervalle) | ★★★ | 25 | §4 §6 | C | wbm | — |

*Notes* : mymath écrit les formules de la loi Beta et de la conjugaison ; le posterior sur une grille et l'intervalle de crédibilité sont les fonctions de `mylearn` en workbookIA 4. Aucun exemple de pièce de monnaie (workbookIA 4 les utilise tous) : taux de clic, capteurs, contrôle qualité. Le log-sum-exp est enseigné ici parce que workbookIA 4 s'en sert (posterior sur une grille en log-probabilités) ; M05a l'approfondit (flottants, encadrement, implémentation). §6.3 de MML est déjà lu en M03 : M04.15 n'en relit que le théorème de Bayes. Parcours essentiel : famille exponentielle, Thompson et les démonstrations hors parcours.

<a id="m05a"></a>
## M05a · Dérivées, Taylor et calcul numérique

**Partie** I · **prépare** workbookIA 5 · **dossier** `chapitres/m05a_derivees_taylor/` · **MML** §5.1 · **sessions de génération** 1

La dérivée seconde et la convexité en une variable, les polynômes de Taylor, la méthode de Newton, l'erreur des différences finies, l'extrapolation de Richardson et le choix du pas, les nombres flottants, les erreurs d'arrondi, l'overflow et l'underflow, et le log-sum-exp qui rend les calculs stables.

**Temps** : 13,5 h en parcours complet, 8,9 h en parcours essentiel (lecture 180 min, 24 flashcards).

**Objectifs**

- Étudier la convexité d'une fonction et classer ses extrema locaux et globaux.
- Écrire un polynôme de Taylor et borner son erreur.
- Résoudre une équation par la méthode de Newton, et dire quand elle converge vite.
- Calculer l'erreur d'une différence finie avant ou centrée, et choisir un pas.
- Expliquer comment un ordinateur représente un nombre réel, et ses limites.
- Calculer un log-sum-exp et une softmax sans overflow.

**Sections de la fiche**

- §1 Dérivée seconde et convexité en une variable
- §2 Extrema locaux et globaux
- §3 Polynômes de Taylor et reste
- §4 La méthode de Newton
- §5 Différences finies : l'erreur par Taylor
- §6 Nombres flottants : représentation, epsilon machine, arrondis
- §7 Le choix du pas h : troncature contre arrondi
- §8 Overflow, underflow et log-sum-exp

**Notions enseignées** : dérivée seconde · convexité en une variable · extrema locaux et globaux · polynômes de Taylor, reste · méthode de Newton · différences finies avant et centrée : l'erreur par Taylor (cas général) · extrapolation de Richardson · choix du pas h : troncature et arrondi · nombres flottants · erreurs d'arrondi · overflow et underflow · log-sum-exp et stabilité numérique

**Prérequis** : dérivées, variations, tangente (R7) · suites, limites, récurrence (R5) · exp et ln, croissances comparées (R6) · notation scientifique (R1)

**mymath** : `approx.py` (signatures figées) : `taylor_polynomial`, `newton`, `richardson_derivative`, `machine_epsilon`, `logsumexp`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 5.6 ∂ Pourquoi la différence centrée est plus précise (calcul exact sur x³) · 5.7 ∂ Rosenbrock : gradient et minimum à la main · 5.1 ✏️ La sécante qui se resserre sur la tangente · 5.4 ✏️ Tableau de variations : extrema locaux et globaux de x³ − 3x · 5.11 🔨 Dérivées numériques : première et seconde · 5.12 🔮 Quel pas h choisir ? Prédire la courbe d'erreur · 5.13 🔬 Erreur de troncature contre erreur d'arrondi

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M05a.Q1 | 🧠 | Le signe de la dérivée seconde | ★ | 4 | §1 | C, E | manuel | — |
| M05a.Q2 | 🧠 | Local ou global ? | ★ | 4 | §2 | C, E | manuel | — |
| M05a.Q3 | 🧠 | Taylor : quel ordre, quelle précision ? | ★ | 4 | §3 | C, E | manuel | — |
| M05a.Q4 | 🧠 | Newton converge-t-il ? | ★ | 4 | §4 | C | manuel | — |
| M05a.Q5 | 🧠 | Différence avant ou centrée ? | ★ | 4 | §5 | C, E | manuel | — |
| M05a.Q6 | 🧠 | Les flottants : vrai ou faux | ★ | 4 | §6 | C, E | manuel | — |
| M05a.Q7 | 🧠 | Overflow, underflow, log-sum-exp | ★ | 4 | §8 | C, E | manuel | — |
| M05a.R1 | 🔁 | Dérivées et variations (R7) | ★ | 5 | §1 | C, E | manuel | — |
| M05a.R2 | 🔁 | Suites définies par récurrence (R5) | ★ | 5 | §4 | C, E | manuel | — |
| M05a.R3 | 🔁 | Log-probabilités et log-sum-exp (M04) | ★ | 5 | §8 | C | manuel | — |
| M05a.1 | ✏️ | Dérivées secondes et convexité | ★ | 20 | §1 | C, E | wbm | — |
| M05a.2 | ✏️ | Extrema locaux et globaux sur un intervalle fermé | ★★ | 20 | §2 | C, E | wbm | — |
| M05a.3 | ✏️ | Points d'inflexion et test de la dérivée seconde | ★★ | 15 | §1 §2 | C | wbm | — |
| M05a.4 | ✏️ | Polynômes de Taylor de trois fonctions usuelles | ★ | 20 | §3 | C, E | wbm | — |
| M05a.5 | ✏️ | Le reste de Taylor : borner l'erreur d'une approximation | ★★ | 20 | §3 | C | wbm | — |
| M05a.6 | ✏️ | Newton à la main : une racine carrée en trois pas | ★ | 20 | §4 | C, E | wbm | — |
| M05a.7 | ✏️ | L'erreur d'une différence avant et d'une différence centrée, par Taylor | ★★ | 20 | §5 | C, E | wbm | — |
| M05a.8 | ✏️ | Les flottants : 0,1 en binaire, epsilon machine, nombres représentables | ★★ | 20 | §6 | C | wbm | — |
| M05a.9 | ✏️ | Le meilleur pas par le calcul : minimiser une borne d'erreur | ★★ | 20 | §7 | C, E | wbm | — |
| M05a.10 | ✏️ | log-sum-exp à la main : la softmax stable de trois scores | ★ | 15 | §8 | C, E | wbm | — |
| M05a.11 | ∂ | La différence centrée est d'ordre 2 : le calcul par Taylor (cas général) | ★★ | 25 | §5 | C | manuel | — |
| M05a.12 | ∂ | Newton double les décimales justes : l'erreur au carré (racine simple) | ★★★ | 25 | §4 | C | manuel | — |
| M05a.13 | ∂ | Encadrer le log-sum-exp : max ≤ LSE ≤ max + ln n | ★★ | 20 | §8 | C | manuel | — |
| M05a.14 | 🔗 | Pourquoi les bibliothèques de ML calculent log(softmax) d'un seul coup | ★ | 15 | §8 | C, E | wbm | — |
| M05a.15 | 📖 | MML §5.1 : dérivée d'une fonction d'une variable et série de Taylor (lecture guidée) | ★★ | 30 | §1 §3 | C, E | manuel | — |
| M05a.16 | 🧮 | Fermi : l'erreur d'arrondi d'une somme d'un million de nombres | ★ | 10 | §6 | C | manuel | — |
| M05a.17 | 🗣️ | Expliquer la convexité et pourquoi elle rassure quand on minimise | ★ | 10 | §1 | C, E | manuel | — |
| M05a.E1 | 💼 | Pourquoi soustraire le maximum avant de calculer une softmax ? | ★ | 10 | §8 | C, E | manuel | — |
| M05a.18 | 🔨 | Évaluer un polynôme de Taylor · `taylor_polynomial` | ★ | 20 | §3 | C, E | pytest | — |
| M05a.19 | 🔨 | La méthode de Newton, avec ses cas d'échec · `newton` | ★ | 20 | §4 | C, E | pytest | — |
| M05a.20 | 🔨 | L'extrapolation de Richardson : annuler le terme d'erreur en h² · `richardson_derivative` | ★★ | 20 | §5 | C | pytest | — |
| M05a.21 | 🔨 | L'epsilon machine, en float64, float32 et float16 · `machine_epsilon` | ★ | 15 | §6 | C | pytest | — |
| M05a.22 | 🔨 | Un log-sum-exp stable · `logsumexp` | ★ | 15 | §8 | C, E | pytest | — |
| M05a.23 | 📦 | SymPy `series` et `numpy.finfo` contre tes fonctions | ★ | 15 | §3 §6 | C | wbm | — |
| M05a.24 | 🔮 | Prédire : Newton depuis un mauvais point de départ | ★ | 10 | §4 | C | wbm | — |
| M05a.25 | 🔬 | Taylor de plus en plus loin : où le polynôme décroche | ★★ | 20 | §3 | C | wbm | — |
| M05a.26 | 🎨 | Une fonction et ses polynômes de Taylor d'ordre 1, 2 et 3 | ★ | 20 | §3 | C, E | manuel | — |
| M05a.27 | 🐛 | Chasse à l'erreur : une softmax qui renvoie `nan` | ★ | 15 | §8 | C | wbm | — |
| M05a.28 | 🛠️ | Erreur relative ou absolue : choisir la tolérance d'un test | ★ | 10 | §6 | C | manuel | — |
| M05a.29 | 🏆 | Défi : une racine cubique à 10⁻¹² en le moins d'itérations possible | ★★★ | 25 | §4 | C | wbm | — |

*Notes* : La dérivée numérique et la dérivée seconde numérique sont les fonctions de `mylearn` en workbookIA 5, et la courbe d'erreur en fonction du pas est son 🔮 5.12 et son 🔬 5.13 : M05a établit l'erreur par Taylor et le meilleur pas par le calcul d'une borne (✏️), sans tracer cette courbe ; mymath écrit Taylor, Newton, l'extrapolation de Richardson, l'epsilon machine et le log-sum-exp (vu en M04, approfondi ici). Pas de x³ − 3x (workbookIA 5.4). Parcours essentiel : le reste de Taylor, la convergence de Newton et la représentation binaire des flottants hors parcours.

<a id="m05b"></a>
## M05b · Fonctions de plusieurs variables et gradient

**Partie** I · **prépare** workbookIA 5 · **dossier** `chapitres/m05b_gradient/` · **MML** §5.2 · **sessions de génération** 1

Les fonctions de deux variables et plus : surfaces et lignes de niveau, dérivées partielles, gradient et dérivée directionnelle, plan tangent, dérivées partielles secondes et classement d'un point critique en dimension 2, et la descente de gradient vue comme « descendre la plus grande pente ».

**Temps** : 13,3 h en parcours complet, 9,2 h en parcours essentiel (lecture 180 min, 24 flashcards).

**Objectifs**

- Lire une fonction de deux variables sur une surface et sur ses lignes de niveau.
- Calculer des dérivées partielles, un gradient et une dérivée directionnelle.
- Expliquer pourquoi le gradient donne la plus grande pente et coupe les lignes de niveau à angle droit.
- Écrire le plan tangent et s'en servir pour approcher une valeur.
- Trouver les points critiques d'une fonction de deux variables et les classer.
- Expliquer le principe de la descente et de la montée de gradient.

**Sections de la fiche**

- §1 Fonctions de deux variables : surfaces et lignes de niveau
- §2 Dérivées partielles
- §3 Gradient et dérivée directionnelle
- §4 La plus grande pente ; le gradient et les lignes de niveau
- §5 Plan tangent et approximation linéaire
- §6 Dérivées partielles secondes
- §7 Points critiques : minimum, maximum, selle
- §8 Descente et montée de gradient (principe) ; argmin et argmax

**Notions enseignées** : fonctions de plusieurs variables · surfaces et lignes de niveau · dérivées partielles · gradient · dérivée directionnelle · plus grande pente · plan tangent · dérivées partielles secondes, courbure dans une direction · points critiques : minimum, maximum, selle (test en dimension 2) · descente et montée de gradient (principe) · argmin et argmax

**Prérequis** : dérivées, règle de la chaîne (R7) · produit scalaire, norme, angle (R9) · dérivée seconde, convexité (M05a) · différences finies (M05a)

**mymath** : `multivar.py` (signatures figées) : `partial_derivative`, `directional_derivative`, `steepest_ascent_direction`, `tangent_plane`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 5.6 ∂ Pourquoi la différence centrée est plus précise (calcul exact sur x³) · 5.7 ∂ Rosenbrock : gradient et minimum à la main · 5.2 ✏️ Gradient à la main et direction de plus grande pente · 5.3 ✏️ Trois pas de descente de gradient à la main · 5.5 ✏️ Point selle : x² − y² vu dans deux directions · 5.15 🔨 numerical_gradient sur la vallée de Rosenbrock · 5.17 📈 Lire des lignes de niveau : où pointe le gradient ? · 5.18 🔨 gradient_descent, et sa version qui monte · 5.19 🔬 Learning rate sur un bol : trop petit, juste, trop grand · 5.20 🔮 Démarrer pile sur un point selle · 5.24 🔨 Minimum, maximum, selle ou plat : classify_critical_point · 5.25 🏆 Atteindre le fond de la vallée de Rosenbrock · 5.E1 💼 Descente de gradient : que se passe-t-il avec un learning rate trop grand, puis trop petit ? · 5.E3 💼 Comment vérifier un gradient calculé ? · 5.E4 💼 Point selle : définition et effet sur l'optimisation

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M05b.Q1 | 🧠 | Lire des lignes de niveau | ★ | 4 | §1 | C, E | manuel | — |
| M05b.Q2 | 🧠 | Dérivées partielles : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| M05b.Q3 | 🧠 | Où pointe le gradient ? | ★ | 4 | §3 §4 | C, E | manuel | — |
| M05b.Q4 | 🧠 | La dérivée directionnelle | ★ | 4 | §3 | C | manuel | — |
| M05b.Q5 | 🧠 | Le plan tangent | ★ | 4 | §5 | C | manuel | — |
| M05b.Q6 | 🧠 | Minimum, maximum ou selle ? | ★ | 4 | §7 | C, E | manuel | — |
| M05b.Q7 | 🧠 | Descendre ou monter | ★ | 4 | §8 | C, E | manuel | — |
| M05b.R1 | 🔁 | Dériver une composée (R7) | ★ | 5 | §2 | C, E | manuel | — |
| M05b.R2 | 🔁 | Produit scalaire et norme (R9) | ★ | 5 | §3 | C, E | manuel | — |
| M05b.R3 | 🔁 | Dérivée seconde et convexité (M05a) | ★ | 5 | §6 | C | manuel | — |
| M05b.1 | ✏️ | Les lignes de niveau de trois fonctions | ★ | 20 | §1 | C, E | wbm | — |
| M05b.2 | ✏️ | Dérivées partielles | ★ | 20 | §2 | C, E | wbm | — |
| M05b.3 | ✏️ | Le gradient en un point et sa norme | ★ | 15 | §3 | C, E | wbm | — |
| M05b.4 | ✏️ | La dérivée directionnelle dans plusieurs directions | ★★ | 20 | §3 | C, E | wbm | — |
| M05b.5 | ✏️ | Monter le plus vite : la direction et la valeur de la plus grande pente | ★★ | 15 | §4 | C, E | wbm | — |
| M05b.6 | ✏️ | Le plan tangent et l'approximation d'une valeur | ★★ | 20 | §5 | C | wbm | — |
| M05b.7 | ✏️ | Dérivées secondes croisées : le théorème de Schwarz vérifié | ★★ | 15 | §6 | C | wbm | — |
| M05b.8 | ✏️ | Les points critiques et leur nature (test du second ordre) | ★★ | 25 | §7 | C, E | wbm | — |
| M05b.9 | ✏️ | Pourquoi un petit pas contre le gradient fait baisser f : le calcul au premier ordre | ★★ | 20 | §5 §8 | C, E | wbm | — |
| M05b.10 | ✏️ | argmin et argmax sur un segment | ★★ | 20 | §7 §8 | C | wbm | — |
| M05b.11 | ∂ | La dérivée directionnelle vaut ∇f · u, et la plus grande pente | ★★ | 25 | §3 §4 | C | manuel | — |
| M05b.12 | ∂ | Le gradient est orthogonal aux lignes de niveau | ★★ | 20 | §4 | C | manuel | — |
| M05b.13 | ∂ | Le test du second ordre pour ax² + bxy + cy² | ★★★ | 30 | §6 §7 | C | manuel | — |
| M05b.14 | 🔗 | La loss d'un neurone à deux poids sur deux exemples : son gradient | ★★ | 20 | §2 §8 | C, E | wbm | — |
| M05b.15 | 📖 | MML §5.2 : dérivées partielles et gradient, la convention en ligne (lecture guidée) | ★★ | 30 | §2 §3 | C, E | manuel | — |
| M05b.16 | 📈 | Lire une carte de lignes de niveau : estimer une dérivée partielle | ★ | 15 | §1 §2 | C | wbm | — |
| M05b.17 | 🗣️ | Expliquer ce que disent des lignes de niveau serrées | ★ | 10 | §1 §4 | C, E | manuel | — |
| M05b.E1 | 💼 | Pourquoi le gradient est-il la direction de plus grande pente ? | ★ | 10 | §4 | C, E | manuel | — |
| M05b.18 | 🔨 | Une dérivée partielle par différence centrée · `partial_derivative` | ★ | 20 | §2 | C, E | pytest | — |
| M05b.19 | 🔨 | Dérivée directionnelle et direction de plus grande pente · `directional_derivative, steepest_ascent_direction` | ★★ | 20 | §3 §4 | C, E | pytest | M05b.18 |
| M05b.20 | 🔨 | Le plan tangent · `tangent_plane` | ★ | 15 | §5 | C | pytest | M05b.18 |
| M05b.21 | 📦 | SymPy : dérivées partielles, gradient, points critiques | ★ | 20 | §2 §6 §7 | C, E | wbm | — |
| M05b.22 | 🔮 | Prédire : la dérivée directionnelle le long d'une ligne de niveau | ★ | 10 | §3 §4 | C, E | wbm | — |
| M05b.23 | 🔬 | L'erreur du plan tangent quand on s'éloigne du point | ★★ | 20 | §5 | C | wbm | — |
| M05b.24 | 🎨 | Lignes de niveau et flèches du gradient sur la même figure | ★ | 20 | §1 §4 | C, E | manuel | — |
| M05b.25 | 🐛 | Chasse à l'erreur : la mauvaise variable dérivée, une direction non unitaire | ★ | 15 | §2 §3 §8 | C | wbm | — |
| M05b.26 | 🛠️ | Vectoriser : une fonction de deux variables sur une grille (`np.meshgrid`) | ★ | 15 | §1 | C | manuel | — |
| M05b.27 | 🏆 | Défi : retrouver une fonction du second degré à partir de son gradient | ★★★ | 25 | §2 §3 §7 | C | wbm | — |

*Notes* : Le gradient numérique, la descente de gradient et le classement d'un point critique sont les fonctions de `mylearn` en workbookIA 5 ; mymath écrit les briques (dérivée partielle, dérivée directionnelle, plan tangent). Ni la fonction de Rosenbrock ni x² − y² (workbookIA 5) ; aucun réglage du learning rate (workbookIA 5, puis M19). Parcours essentiel : plan tangent, dérivées secondes et démonstrations hors parcours, sauf le test du second ordre appliqué.

<a id="m06"></a>
## M06 · Théorie de l'information

**Partie** I · **prépare** workbookIA 6 · **dossier** `chapitres/m06_information/` · **MML** — · **sessions de génération** 1

La théorie de l'information : quantité d'information, entropie, entropies conjointe et conditionnelle, information mutuelle, cross-entropy, divergence KL et sa positivité (inégalité de Jensen), Jensen-Shannon, codes et inégalité de Kraft, perplexité. Référence libre : MacKay.

**Temps** : 11,4 h en parcours complet, 6,5 h en parcours essentiel (lecture 150 min, 22 flashcards).

**Objectifs**

- Calculer l'information d'un événement et l'entropie d'une loi, en bits et en nats.
- Calculer des entropies conjointe et conditionnelle et une information mutuelle à partir d'un tableau.
- Calculer une cross-entropy et une divergence KL, et démontrer que la KL est positive.
- Décider si des longueurs de code sont possibles (inégalité de Kraft) et comparer un code à l'entropie.
- Relier la log loss et la perplexité à la cross-entropy.

**Sections de la fiche**

- §1 Information de Shannon : bits et nats
- §2 Entropie
- §3 Entropies conjointe et conditionnelle
- §4 Information mutuelle
- §5 Cross-entropy et divergence KL
- §6 Inégalité de Jensen, positivité de la KL, Jensen-Shannon
- §7 Codes : longueur fixe ou variable, inégalité de Kraft
- §8 Perplexité, et choisir des features par l'information mutuelle

**Notions enseignées** : information de Shannon · bits et nats · entropie · entropie conjointe et conditionnelle · information mutuelle · cross-entropy, log loss · divergence KL · inégalité de Jensen · positivité de la divergence KL · divergence de Jensen-Shannon · codes de longueur fixe et variable · inégalité de Kraft, outils du code de Huffman (codes préfixes, arbres, borne de l'entropie) · perplexité · sélectionner des features par l'information mutuelle (idée)

**Prérequis** : logarithmes, bits (R6) · probabilités jointes et conditionnelles (M03) · espérance d'une variable discrète (M02b) · convexité (M05a)

**mymath** : `info.py` (signatures figées) : `joint_entropy`, `conditional_entropy`, `mutual_information`, `kraft_sum`, `is_prefix_code`, `jensen_gap`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 6.7 ∂ H(p, q) = H(p) + KL(p‖q), et KL(p‖p) = 0 · 6.8 ∂ L'entropie d'une pièce est maximale à p = 1/2 · 6.1 ✏️ Combien de bits pour une pièce, un dé, une lettre E ? · 6.2 ✏️ Bits par mot : Seuss, Holmes et l'alphabet · 6.3 ✏️ Entropie de quelques distributions · 6.4 ✏️ Morse contre code fixe : SHERLOCK HOLMES · 6.5 ✏️ Cross-entropy et KL dans les deux sens · 6.6 ✏️ Un code de Huffman à la main · 6.16 🔨 cross_entropy, kl_divergence et js_divergence · 6.17 🐛 La cross-entropy infinie : la lettre qui manque · 6.19 📦 scipy.stats.entropy et un vrai compresseur (zlib) · 6.23 🔨 Huffman : construire, encoder, décoder · 6.27 🏆 Passer sous la barre de Huffman lettre à lettre · 6.E1 💼 Pourquoi la cross-entropy comme loss de classification ? · 6.E2 💼 Entropie, cross-entropy, KL : les différences

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M06.Q1 | 🧠 | La surprise et la probabilité | ★ | 4 | §1 | C, E | manuel | — |
| M06.Q2 | 🧠 | L'entropie : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| M06.Q3 | 🧠 | Conjointe et conditionnelle | ★ | 4 | §3 | C, E | manuel | — |
| M06.Q4 | 🧠 | L'information mutuelle | ★ | 4 | §4 | C | manuel | — |
| M06.Q5 | 🧠 | La KL n'est pas une distance | ★ | 4 | §5 | C, E | manuel | — |
| M06.Q6 | 🧠 | L'inégalité de Jensen | ★ | 4 | §6 | C | manuel | — |
| M06.Q7 | 🧠 | Codes préfixes | ★ | 4 | §7 | C, E | manuel | — |
| M06.R1 | 🔁 | Logarithmes en base 2 (R6) | ★ | 5 | §1 | C, E | manuel | — |
| M06.R2 | 🔁 | Probabilités jointes et conditionnelles (M03) | ★ | 5 | §3 | C, E | manuel | — |
| M06.R3 | 🔁 | Convexité (M05a) | ★ | 5 | §6 | C | manuel | — |
| M06.1 | ✏️ | L'information d'événements et l'entropie d'une loi à quatre issues | ★ | 20 | §1 §2 §3 | C, E | wbm | — |
| M06.2 | ✏️ | L'entropie maximale : comparer des lois à quatre issues | ★★ | 15 | §2 §3 | C | wbm | — |
| M06.3 | ✏️ | Entropies conjointe et conditionnelle d'un tableau 2 × 3 | ★★ | 20 | §3 | C, E | wbm | — |
| M06.4 | ✏️ | La règle de la chaîne de l'entropie, vérifiée | ★ | 15 | §3 | C | wbm | — |
| M06.5 | ✏️ | L'information mutuelle de deux variables | ★★ | 20 | §4 | C, E | wbm | — |
| M06.6 | ✏️ | Cross-entropy et KL en bits perdus : un code fait pour la mauvaise loi | ★★ | 20 | §5 | C, E | wbm | — |
| M06.7 | ✏️ | L'inégalité de Jensen sur trois exemples | ★ | 15 | §6 | C | wbm | — |
| M06.8 | ✏️ | Kraft : ces longueurs de code sont-elles possibles ? | ★ | 15 | §7 | C, E | wbm | — |
| M06.9 | ✏️ | La longueur moyenne d'un code, comparée à l'entropie | ★★ | 20 | §7 | C | wbm | — |
| M06.10 | ∂ | I(X ; Y) = H(X) − H(X | Y), et l'information mutuelle est positive | ★★ | 20 | §4 | C | manuel | — |
| M06.11 | ∂ | La KL est positive : la preuve par l'inégalité de Jensen | ★★★ | 25 | §6 | C | manuel | — |
| M06.12 | 🔗 | La log loss d'un classifieur, une cross-entropy moyenne | ★ | 15 | §5 §8 | C, E | wbm | — |
| M06.13 | 🔗 | Choisir une feature par l'information mutuelle | ★★ | 20 | §8 | C | wbm | — |
| M06.14 | 🧮 | Fermi : combien de bits pour un génome humain ? | ★ | 10 | §2 | C | manuel | — |
| M06.15 | 🗣️ | Expliquer l'information mutuelle avec deux capteurs | ★ | 10 | §4 | C, E | manuel | — |
| M06.E1 | 💼 | Information mutuelle ou corrélation : laquelle détecte quoi ? | ★ | 10 | §4 | C | manuel | — |
| M06.16 | 🔨 | Entropies conjointe et conditionnelle d'un tableau · `joint_entropy, conditional_entropy` | ★ | 20 | §3 | C, E | pytest | — |
| M06.17 | 🔨 | L'information mutuelle · `mutual_information` | ★ | 15 | §4 | C, E | pytest | M06.16 |
| M06.18 | 🔨 | Codes préfixes et somme de Kraft · `kraft_sum, is_prefix_code` | ★ | 15 | §7 | C | pytest | — |
| M06.19 | 🔨 | L'écart de Jensen d'une loi discrète · `jensen_gap` | ★ | 15 | §6 | C | pytest | — |
| M06.20 | 📦 | `sklearn.metrics.mutual_info_score` contre ta fonction, en nats | ★ | 15 | §4 | C | wbm | — |
| M06.21 | 🔮 | Prédire : l'information mutuelle de X et X³, de X et X² | ★ | 10 | §4 | C, E | wbm | — |
| M06.22 | 🔬 | Estimer une entropie à partir d'un échantillon : le biais des petits échantillons | ★★ | 20 | §2 | C | wbm | — |
| M06.23 | 🎨 | Un diagramme de l'information : H(X), H(Y), H(X | Y), I(X ; Y) | ★ | 20 | §3 §4 | C | manuel | — |
| M06.24 | 🐛 | Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers | ★ | 15 | §5 | C | wbm | — |
| M06.25 | 🛠️ | Calculer 0 log 0 proprement (`scipy.special.xlogy`) | ★ | 10 | §2 §3 | C | manuel | — |
| M06.26 | 🏆 | Défi : localiser une panne parmi 100 serveurs en un minimum de questions | ★★★ | 25 | §2 §7 | C | wbm | — |

*Notes* : Entropie, cross-entropy, KL, Jensen-Shannon, Huffman et perplexité sont les fonctions de `mylearn` en workbookIA 6 ; mymath écrit ce qui les entoure (entropies conjointe et conditionnelle, information mutuelle, Kraft, codes préfixes, écart de Jensen). Le code de Huffman est énoncé, pas construit à la main ni programmé (workbookIA 6.6 et 6.23) ; ni Morse, ni pièce, ni dé, ni textes littéraires (workbookIA 6.1 à 6.4) ; la KL est calculée dans un seul sens, comme des bits perdus (workbookIA 6.5 la calcule dans les deux). COMPOSITION : pas de 📖 (MML ne traite pas l'information) ; lecture conseillée : MacKay, chapitres 1, 2, 5 et 8. Parcours essentiel : Jensen, la fin du §7 (longueur moyenne), Jensen-Shannon et démonstrations hors parcours ; Kraft y est, par Q7 et M06.8.

<a id="cp1"></a>
## CP1 · Examen blanc de la partie I

**Partie** I · **prépare** — · **dossier** `checkpoints/partie_1/` · **MML** — · **sessions de génération** 1

Le bilan de la partie I (M02a à M06), juste avant le checkpoint I de workbookIA : un examen blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.

**Temps** : 3,3 h en parcours complet, 3,3 h en parcours essentiel (lecture 15 min, 0 flashcards).

**Objectifs**

- Vérifier en temps limité que les notions de la partie I sont acquises.
- Construire ta propre synthèse de la partie I.

**Sections de la fiche**

- §1 Examen blanc
- §2 Synthèse

**Notions enseignées** : révision de la partie I

**Prérequis** : toute la partie I (M06)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 2.8 ∂ Changer d'unité : la covariance bouge, pas la corrélation · 3.4 ∂ Règle du produit et formule des probabilités totales · 3.8 ∂ F1, moyenne harmonique : pourquoi elle punit le maillon faible · 4.3 ∂ Retrouver la règle de Bayes en trois lignes · 4.7 ∂ Le posterior reste une distribution, un prior nul reste nul · 5.6 ∂ Pourquoi la différence centrée est plus précise (calcul exact sur x³) · 5.7 ∂ Rosenbrock : gradient et minimum à la main · 6.7 ∂ H(p, q) = H(p) + KL(p‖q), et KL(p‖p) = 0 · 6.8 ∂ L'entropie d'une pièce est maximale à p = 1/2

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| CP1.Q1 | 🧠 | Dix affirmations sur la partie I : vrai ou faux | ★ | 10 | §1 | C, E | manuel | — |
| CP1.1 | ✏️ | Intégrales et densité : une aire, une fonction de répartition, un quantile | ★★ | 10 | §1 | C, E | wbm | — |
| CP1.2 | ✏️ | Lois usuelles : binomiale, Poisson, normale | ★★ | 9 | §1 | C, E | wbm | — |
| CP1.3 | ✏️ | Un couple de variables : marginales, indépendance, variance d'une somme | ★★ | 8 | §1 | C, E | wbm | — |
| CP1.4 | ✏️ | Estimer une moyenne : erreur type et intervalle de confiance | ★★ | 8 | §1 | C, E | wbm | — |
| CP1.5 | ✏️ | Un tableau de contingence et des métriques comme probabilités | ★★ | 8 | §1 | C, E | wbm | — |
| CP1.6 | ✏️ | Bayes et la loi Beta : une mise à jour conjuguée | ★★ | 8 | §1 | C, E | wbm | — |
| CP1.7 | ✏️ | Taylor, Newton et un calcul stable | ★★ | 9 | §1 | C, E | wbm | — |
| CP1.8 | ✏️ | Gradient, dérivée directionnelle et point critique | ★★ | 10 | §1 | C, E | wbm | — |
| CP1.9 | ✏️ | Entropie, information mutuelle et KL | ★★ | 10 | §1 | C, E | wbm | — |
| CP1.10 | ∂ | Une démonstration courte, au choix parmi deux | ★★★ | 12 | §1 | C, E | manuel | — |
| CP1.11 | 🐛 | Corriger une copie : cinq erreurs | ★★ | 8 | §1 | C, E | wbm | — |
| CP1.12 | 🔗 | Problème de synthèse : estimer un paramètre de bout en bout (vraisemblance, maximum, Newton, incertitude) | ★★ | 14 | §1 | C, E | wbm | — |
| CP1.13 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme CP0 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, 03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend le checkpoint I de workbookIA (`checkpoints/partie_1/` de workbookIA), qui se fait juste après.

<a id="m07"></a>
## M07 · Vecteurs et géométrie de ℝⁿ

**Partie** II · **prépare** workbookIA 7 · **dossier** `chapitres/m07_vecteurs_rn/` · **MML** §3.1, §3.2.1, §3.3, §3.4 · **sessions de génération** 1

Les vecteurs de ℝⁿ : produit scalaire, normes L1, L2, L∞ et distances, angle et similarité cosinus, inégalité de Cauchy-Schwarz, projection sur une droite, hyperplans et demi-espaces ; le barycentre (la moyenne minimise la somme des carrés des distances), l'inertie, la silhouette et le principe de k-means ; et les surprises de la grande dimension.

**Temps** : 15,3 h en parcours complet, 9,9 h en parcours essentiel (lecture 180 min, 24 flashcards).

**Objectifs**

- Calculer avec des vecteurs de ℝⁿ : combinaisons linéaires, produit scalaire, vecteurs one-hot.
- Calculer les normes L1, L2 et L∞ et les distances associées, et démontrer l'inégalité triangulaire.
- Calculer un angle et une similarité cosinus, démontrer l'inégalité de Cauchy-Schwarz, projeter sur une droite.
- Décrire un hyperplan par son vecteur normal, dire de quel côté est un point et calculer sa distance.
- Démontrer que le barycentre minimise la somme des carrés des distances, et calculer une inertie, une silhouette et les probabilités de k-means++.
- Mesurer, à la main et par simulation, ce qui change quand la dimension grandit.

**Sections de la fiche**

- §1 Vecteurs de ℝⁿ : un exemple est un vecteur
- §2 Produit scalaire
- §3 Normes et distances : L1, L2, L∞
- §4 Angle, similarité cosinus, Cauchy-Schwarz et projection
- §5 Hyperplans et demi-espaces
- §6 Barycentres : la moyenne, l'inertie, la silhouette et k-means
- §7 La grande dimension

**Notions enseignées** : vecteurs de ℝⁿ · normes L1, L2, L∞ · distances · produit scalaire · angle · similarité cosinus · inégalité de Cauchy-Schwarz · inégalité triangulaire · projection sur une droite · hyperplans et demi-espaces, distance à un hyperplan · frontière de décision linéaire · barycentre et centroïde · classifieur du centroïde le plus proche (définition) · k-means : affectation et mise à jour (le principe) · inertie et silhouette · grande dimension : diagonale du cube, vecteurs presque orthogonaux, norme d'un vecteur gaussien · le neurone comme produit scalaire plus biais · vecteurs one-hot et base canonique · k-means++ : tirer selon le carré des distances

**Prérequis** : vecteurs du plan, norme, produit scalaire, angle (R9) · Σ, raisonnements (R4) · polynôme du second degré, discriminant (R3) · moyenne et variance empiriques (M02c) · espérance, variance, loi uniforme, loi normale (M02b) · gradient, point critique (M05b) · intégration par parties (M02a) · inégalité de Bienaymé-Tchebychev (M02c) · approximation par la tangente (M05a)

**mymath** : `vectors.py` (signatures figées) : `norm_p`, `cosine_similarity`, `project_onto_line`, `centroid`, `sum_sq_distances_to`, `side_of_hyperplane`, `distance_to_hyperplane`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 7.5 ∂ Le rayon de l'hyper-orange : r(d) = √d − 1 · 7.6 ∂ Boule dans un cube : rapport des volumes par récurrence · 7.7 ∂ La frontière du centroïde le plus proche est une droite · 7.1 ✏️ Compter les classifieurs OvR et OvO · 7.2 ✏️ Dépouiller les votes d'un un-contre-un à quatre classes · 7.3 ✏️ Une itération de k-means à la main · 7.4 ✏️ Densité d'échantillons et nombre d'œufs nécessaires · 7.13 🔨 Distances au carré vectorisées : pairwise_sq_distances · 7.14 🔨 Le classifieur du centroïde le plus proche · 7.19 🔮 Distance au plus proche voisin quand la dimension grimpe · 7.20 🔬 Densité, plus proche voisin et concentration des distances · 7.21 🎨 Reproduire les figures 7.27 et 7.30 (boule/cube, hyper-orange) · 7.25 🔨 Initialisation k-means++ · 7.26 🔨 k-means de Lloyd : la classe KMeans · 7.28 🔨 Coefficient de silhouette · 7.R3 🔁 Développer ‖a − b‖² avec le produit scalaire

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M07.Q1 | 🧠 | Vecteurs, coordonnées et one-hot | ★ | 4 | §1 | C, E | manuel | — |
| M07.Q2 | 🧠 | Ce que mesure un produit scalaire | ★ | 4 | §2 | C, E | manuel | — |
| M07.Q3 | 🧠 | Trois normes, trois boules unités | ★ | 4 | §3 | C, E | manuel | — |
| M07.Q4 | 🧠 | Similarité cosinus : vrai ou faux | ★ | 4 | §4 | C, E | manuel | — |
| M07.Q5 | 🧠 | Hyperplans : vecteur normal et côtés | ★ | 4 | §5 | C, E | manuel | — |
| M07.Q6 | 🧠 | Moyenne, barycentre et inertie | ★ | 4 | §6 | C | manuel | — |
| M07.Q7 | 🧠 | Intuitions de la grande dimension | ★ | 4 | §7 | C, E | manuel | — |
| M07.R1 | 🔁 | Produit scalaire et angle dans le plan (R9) | ★ | 5 | §2 | C, E | manuel | — |
| M07.R2 | 🔁 | Moyenne et variance empiriques (M02c) | ★ | 5 | §6 | C, E | manuel | — |
| M07.R3 | 🔁 | Gradient et point critique (M05b) | ★ | 5 | §6 | C | manuel | — |
| M07.1 | ✏️ | Combinaisons linéaires et vecteurs one-hot dans ℝ⁴ | ★ | 15 | §1 | C, E | wbm | — |
| M07.2 | ✏️ | Produits scalaires, ‖u + v‖² et l'identité du parallélogramme | ★ | 15 | §2 | C, E | wbm | — |
| M07.3 | ✏️ | Normes L1, L2, L∞ et distances entre trois profils | ★ | 20 | §3 | C, E | wbm | — |
| M07.4 | ✏️ | Similarité cosinus entre des profils d'écoute musicale | ★★ | 20 | §4 | C, E | wbm | — |
| M07.5 | ✏️ | Projeter sur une droite : composante parallèle et composante orthogonale | ★★ | 20 | §4 | C, E | wbm | — |
| M07.6 | ✏️ | Un plan de ℝ³ : vecteur normal, côté, distance signée | ★★ | 20 | §5 | C, E | wbm | — |
| M07.7 | ✏️ | Un score linéaire w · x + b : calculer, décider, lire le vecteur normal | ★ | 15 | §2 §5 | C, E | wbm | — |
| M07.8 | ✏️ | Centroïde, inertie et formule de König-Huygens | ★★ | 20 | §6 | C, E | wbm | — |
| M07.9 | ✏️ | Où placer un dépôt : le barycentre pondéré des livraisons | ★★ | 15 | §6 | C | wbm | — |
| M07.10 | ✏️ | La silhouette d'un point, à la main, en dimension 2 | ★★ | 15 | §6 | C | wbm | — |
| M07.11 | ✏️ | k-means++ : des probabilités de tirage proportionnelles à D² | ★★ | 15 | §6 | C | wbm | — |
| M07.12 | ✏️ | La diagonale du cube unité et son angle avec les axes, quand d grandit | ★ | 15 | §7 | C, E | wbm | — |
| M07.13 | ✏️ | La norme d'un vecteur gaussien : espérance, variance et concentration | ★★ | 15 | §7 | C | wbm | — |
| M07.14 | ∂ | L'inégalité de Cauchy-Schwarz, par le discriminant | ★★ | 25 | §4 | C, E | manuel | — |
| M07.15 | ∂ | L'inégalité triangulaire pour L2, L1 et L∞ | ★★ | 20 | §3 §4 | C | manuel | — |
| M07.16 | ∂ | La moyenne minimise la somme des carrés des distances, en dimension n | ★★ | 20 | §6 | C, E | manuel | — |
| M07.17 | ∂ | La distance d'un point à un hyperplan vaut |w · x + b| / ‖w‖ | ★★ | 20 | §5 | C, E | manuel | — |
| M07.18 | ∂ | Les deux étapes de k-means font baisser l'inertie, ou la laissent égale | ★★★ | 20 | §6 | C | manuel | — |
| M07.19 | 🔗 | Pont : changer l'unité d'une feature change le plus proche voisin | ★ | 15 | §3 | C, E | wbm | — |
| M07.20 | 📖 | MML §3.1 et §3.2.1 : normes et produit scalaire, en anglais | ★★ | 30 | §2 §3 | C | manuel | — |
| M07.21 | 📖 | MML §3.3 et §3.4 : longueurs, distances, angles et orthogonalité | ★★ | 30 | §4 | C | manuel | — |
| M07.22 | 🧮 | Fermi : la mémoire d'un million d'embeddings | ★ | 10 | §1 | C | manuel | — |
| M07.23 | 🗣️ | Expliquer la similarité cosinus à quelqu'un qui a fait le lycée | ★ | 10 | §4 | C, E | manuel | — |
| M07.E1 | 💼 | Que représente géométriquement le vecteur de poids d'un modèle linéaire ? | ★ | 10 | §2 §5 | C | manuel | — |
| M07.24 | 🔨 | Normes Lp et similarité cosinus · `norm_p, cosine_similarity` | ★ | 20 | §3 §4 | C, E | pytest | — |
| M07.25 | 🔨 | La projection sur une droite · `project_onto_line` | ★ | 15 | §4 | C, E | pytest | — |
| M07.26 | 🔨 | Barycentre et somme des carrés des distances · `centroid, sum_sq_distances_to` | ★ | 20 | §6 | C, E | pytest | — |
| M07.27 | 🔨 | Côté d'un hyperplan et distance à un hyperplan · `side_of_hyperplane, distance_to_hyperplane` | ★ | 20 | §5 | C, E | pytest | M07.24 |
| M07.28 | 📦 | `np.linalg.norm` (ord = 1, 2, inf) et `scipy.spatial.distance` contre tes fonctions | ★ | 10 | §3 | C | wbm | — |
| M07.29 | 🔮 | Prédire : l'angle de deux vecteurs tirés au hasard en dimension 1 000 | ★ | 10 | §7 | C, E | wbm | — |
| M07.30 | 🔬 | La norme d'un vecteur gaussien se concentre autour de √d | ★★ | 20 | §7 | C | wbm | — |
| M07.31 | 🔬 | Médiane ou moyenne : le centre qui minimise les distances L1 ou leurs carrés, face à des points aberrants | ★★ | 20 | §3 §6 | C | wbm | — |
| M07.32 | 🎨 | Les boules unités L1, L2, L∞ et Lp dans le plan | ★ | 20 | §3 | C | manuel | — |
| M07.33 | 🐛 | Chasse à l'erreur : une distance sans racine, un cosinus mal normalisé, une projection sur un vecteur non unitaire | ★ | 15 | §3 §4 | C | wbm | — |
| M07.34 | 🛠️ | Les normes de toutes les lignes d'un tableau : axis, keepdims et broadcasting | ★ | 15 | §1 §3 | C | manuel | — |
| M07.35 | 🏆 | Défi : le point qui minimise la somme des distances (non au carré) à 60 villes, à 0,1 % près | ★★★ | 30 | §3 §6 | C | wbm | — |

*Notes* : Évités (règle de partage) : les œufs, les manchots, les deux lunes et les autres données de workbookIA 7, et les mini-exemples de sa fiche (centroïdes (1, 1) et (3, 5) avec x = (6, 0) ; a = (1, 2) et b = (3, 4) ; les points 0, 2, 3, 9, 11, 12 ; 0, 1, 5, 9 ; les clusters {0, 1, 2} et {6, 7} ; la pureté 40 Adélie et 10 Chinstrap). Frontières : la densité n / bᵈ et le nombre d'échantillons nécessaires (7.4), la boule dans le cube (7.6), l'hyper-orange (7.5), l'écorce 1 − (1 − ε)ᵈ, la distance au plus proche voisin et la concentration des distances (7.19, 7.20) : M07 étudie la diagonale du cube, l'angle de deux vecteurs aléatoires (sans calculer la variance de leur produit scalaire, ∂ B3.6) et la norme d'un vecteur gaussien (M07.13, qui démontre la variance de Z² admise en M02c), d'où la concentration des distances entre deux vecteurs gaussiens, sans plus proche voisin ni cube uniforme ; pas de changement d'échelle de (w, b) en entretien (10.3 f, 13.4 i) ; pas de choix de k (7.Q8, 7.E3), et M07.E1 ne reprend pas 0B.E2 (cosinus ou distance euclidienne) ; la médiatrice comme frontière du centroïde le plus proche (7.7) est énoncée, pas démontrée ; pas d'itération complète de k-means (7.3) : M07 démontre que l'inertie ne peut pas augmenter et place un seul dépôt au barycentre ; pas de développement de ‖a − b‖² (7.R3) ni de distances par paires vectorisées (7.13). Les distances par paires, le centroïde le plus proche, k-means, k-means++ et la silhouette sont les fonctions de `mylearn` en workbookIA 7 ; `vectors` écrit les briques (normes, cosinus, projection, barycentre, inertie, hyperplans). Coût : environ 15 h au lieu de 14 (19 notions).

<a id="m08"></a>
## M08 · Tests statistiques

**Partie** II · **prépare** workbookIA 8 · **dossier** `chapitres/m08_tests/` · **MML** §8.6 · **sessions de génération** 1

Les tests statistiques : hypothèses, statistique de test, p-valeur, test binomial exact, test par permutation, erreurs de type I et II, puissance, intervalles d'une proportion (Wald, Wilson) et d'une différence appariée (Student), comparaisons multiples (Bonferroni) ; puis la sélection de modèle (AIC, BIC, facteur de Bayes) et la validation croisée vue comme une estimation bruitée.

**Temps** : 12,1 h en parcours complet, 7,6 h en parcours essentiel (lecture 150 min, 22 flashcards).

**Objectifs**

- Poser une hypothèse nulle et une alternative, choisir une statistique et interpréter une p-valeur sans contresens.
- Calculer à la main la p-valeur exacte d'un test binomial et d'un petit test par permutation.
- Calculer les erreurs de type I et II et la puissance d'un test, et dimensionner un échantillon.
- Calculer un intervalle de Wald et de Wilson pour une proportion, et un intervalle de Student pour des mesures appariées.
- Corriger des comparaisons multiples par Bonferroni et en démontrer la garantie.
- Comparer des modèles par l'AIC, le BIC et un facteur de Bayes.

**Sections de la fiche**

- §1 Le raisonnement d'un test : hypothèses, statistique, p-valeur
- §2 Un test exact : le test binomial
- §3 Le test par permutation
- §4 Erreurs de type I et II, puissance, taille d'échantillon
- §5 Intervalles : une proportion (Wald, Wilson), une différence appariée (Student)
- §6 Comparaisons multiples : Bonferroni
- §7 Choisir un modèle : AIC, BIC, facteur de Bayes, validation croisée

**Notions enseignées** : hypothèse nulle et alternative · statistique de test · p-valeur · test binomial exact · test par permutation · erreurs de type I et II · puissance d'un test · taille d'échantillon · intervalle d'une proportion : Wald et Wilson · intervalle d'une accuracy · loi de Student (aperçu) et mesures appariées · comparaisons multiples (Bonferroni) · comparer deux modèles (principe) · sélection de modèle : AIC, BIC, facteur de Bayes (aperçu) · validation croisée : principe statistique · importance par permutation (principe) · évaluation sur plusieurs graines

**Prérequis** : dénombrement, combinaisons (R8) · loi binomiale, loi normale, Φ (M02b) · erreur type, intervalle de confiance, bootstrap (M02c) · vraisemblance, Bayes (M04) · logarithmes (R6) · polynôme du second degré (R3)

**mymath** : `testing.py` (signatures figées) : `binomial_test`, `permutation_test`, `proportion_ci`, `paired_difference_ci`, `bonferroni`, `aic_bic`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 8.6 ∂ Le biais d'optimisme du meilleur de K modèles · 8.1 ✏️ Découper 344 manchots : hold-out, validation et folds · 8.2 ✏️ Compter les entraînements d'une recherche d'hyperparamètres · 8.4 ✏️ Quelle confiance accorder à une accuracy de test ? Erreur type et taille du test · 8.5 ✏️ Moyenne et écart-type de scores de validation croisée · 8.23 🔬 Variabilité de l'évaluation : hold-out répétés contre k-fold · 8.25 🔬 Sélectionner des features avant la validation croisée : 90 % sur du bruit · 8.26 🔬 Comparer deux modèles honnêtement : test par permutation, p-valeur et bootstrap apparié · 8.E2 💼 Qu'est-ce qu'une p-valeur ? Comment savoir si le modèle B bat vraiment le modèle A ? · 8.E3 💼 Validation croisée ou simple hold-out : quand choisir quoi ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M08.Q1 | 🧠 | Ce qu'une p-valeur est, et ce qu'elle n'est pas | ★ | 4 | §1 | C, E | manuel | — |
| M08.Q2 | 🧠 | Unilatéral ou bilatéral ? | ★ | 4 | §2 | C | manuel | — |
| M08.Q3 | 🧠 | Permuter quoi, et sous quelle hypothèse ? | ★ | 4 | §3 | C, E | manuel | — |
| M08.Q4 | 🧠 | Erreurs de type I et II, puissance : associer | ★ | 4 | §4 | C, E | manuel | — |
| M08.Q5 | 🧠 | Comparaisons multiples : vrai ou faux | ★ | 4 | §6 | C, E | manuel | — |
| M08.Q6 | 🧠 | AIC, BIC, facteur de Bayes : qui pénalise quoi ? | ★ | 4 | §7 | C | manuel | — |
| M08.R1 | 🔁 | La loi binomiale (M02b) | ★ | 5 | §2 | C, E | manuel | — |
| M08.R2 | 🔁 | L'intervalle de confiance d'une moyenne (M02c) | ★ | 5 | §5 | C, E | manuel | — |
| M08.R3 | 🔁 | Vraisemblance et log-vraisemblance (M04) | ★ | 5 | §7 | C | manuel | — |
| M08.1 | ✏️ | Un test binomial à la main : un algorithme de compression est-il plus rapide sur douze fichiers ? | ★ | 20 | §1 §2 | C, E | wbm | — |
| M08.2 | ✏️ | Un test par permutation exhaustif : deux groupes de trois mesures, vingt répartitions | ★★ | 25 | §3 | C, E | wbm | — |
| M08.3 | ✏️ | Erreur de type I, erreur de type II et puissance d'un test binomial | ★★ | 20 | §4 | C, E | wbm | — |
| M08.4 | ✏️ | Combien d'observations pour une puissance de 80 % ? (approximation normale) | ★★ | 20 | §4 | C | wbm | — |
| M08.5 | ✏️ | L'intervalle d'une proportion : Wald contre Wilson, avec peu de succès | ★★ | 20 | §5 | C, E | wbm | — |
| M08.6 | ✏️ | L'intervalle de Student d'une différence appariée : un serveur avant et après une mise à jour | ★★ | 20 | §5 | C, E | wbm | — |
| M08.7 | ✏️ | Vingt tests au seuil de 5 % : les faux positifs attendus, puis Bonferroni | ★ | 15 | §6 | C, E | wbm | — |
| M08.8 | ✏️ | L'AIC et le BIC de deux modèles, à partir de leurs log-vraisemblances | ★ | 15 | §7 | C, E | wbm | — |
| M08.9 | ✏️ | Un facteur de Bayes entre deux taux de clics | ★★ | 15 | §7 | C | wbm | — |
| M08.10 | ∂ | Sous H0, une p-valeur continue suit la loi uniforme | ★★ | 20 | §1 §4 | C | manuel | — |
| M08.11 | ∂ | L'inégalité de Boole et la garantie de Bonferroni, sans hypothèse d'indépendance | ★★ | 20 | §6 | C, E | manuel | — |
| M08.12 | ∂ | L'intervalle de Wilson, en inversant le test d'une proportion | ★★★ | 25 | §5 | C | manuel | — |
| M08.13 | 🔗 | Pont : l'importance d'une feature par permutation, sur un petit tableau | ★ | 15 | §3 | C | wbm | — |
| M08.14 | 📖 | MML §8.6 : validation croisée imbriquée, sélection bayésienne de modèle et facteur de Bayes | ★★ | 30 | §7 | C | manuel | — |
| M08.15 | 🗣️ | Expliquer une p-valeur sans dire « la probabilité que H0 soit vraie » | ★ | 10 | §1 | C, E | manuel | — |
| M08.E1 | 💼 | « Votre test donne p = 0,03 : que concluez-vous, et que dites-vous à l'équipe produit ? » | ★ | 10 | §1 §4 | C | manuel | — |
| M08.16 | 🔨 | Le test binomial exact · `binomial_test` | ★ | 15 | §2 | C, E | pytest | — |
| M08.17 | 🔨 | Le test par permutation à deux échantillons · `permutation_test` | ★★ | 25 | §3 | C, E | pytest | — |
| M08.18 | 🔨 | Les intervalles de Wilson et de Student · `proportion_ci, paired_difference_ci` | ★ | 20 | §5 | C, E | pytest | — |
| M08.19 | 🔨 | Bonferroni, l'AIC et le BIC · `bonferroni, aic_bic` | ★ | 10 | §6 §7 | C | pytest | — |
| M08.20 | 📦 | `scipy.stats.binomtest`, `permutation_test` et `ttest_rel` contre tes fonctions | ★ | 15 | §2 §3 §5 | C | wbm | — |
| M08.21 | 🔮 | Prédire : sous H0, quelle part de 1 000 p-valeurs tombe sous 0,05 ? | ★ | 10 | §1 §4 | C, E | wbm | — |
| M08.22 | 🔬 | La puissance d'un test par permutation, selon l'effet et la taille des groupes | ★★ | 25 | §4 | C | wbm | — |
| M08.23 | 🎨 | La loi de la statistique sous H0, et la p-valeur comme une aire | ★ | 15 | §1 §3 | C | manuel | — |
| M08.24 | 🐛 | Chasse à l'erreur : une p-valeur nulle, un test unilatéral choisi après coup, Bonferroni à l'envers | ★ | 15 | §3 §6 | C | wbm | — |
| M08.25 | 🛠️ | Tester un test : un pytest qui vérifie l'uniformité des p-valeurs sous H0 | ★ | 15 | §1 | C | manuel | — |
| M08.26 | 🏆 | Défi : retrouver les trois vraies features parmi cinquante, avec au plus un faux positif | ★★★ | 25 | §6 | C | wbm | — |

*Notes* : Évités (règle de partage) : les manchots, l'accuracy de 0,92 sur 250 exemples et la taille de test minimale (8.4), les scores de deux modèles sur cinq folds (8.5), la loi du maximum de K scores (∂ 8.6), les cinq désaccords (4 contre 1) du mini-exemple de la fiche, la comparaison de deux modèles sur le même jeu de test par leurs désaccords et le bootstrap apparié (8.26, 8.E2 : M08 définit la p-valeur et teste d'autres situations), la sélection de features sur du bruit avant la validation croisée (8.25), le contexte « 91,2 % contre 90,5 % ». M08 enseigne le test binomial, le test par permutation à deux échantillons (on rebat la répartition des valeurs entre les deux groupes), Wald et Wilson, Student pour des mesures appariées (pas des folds), Bonferroni et l'AIC et le BIC, dans d'autres cadres (temps de calcul, mesures physiques, taux de clics). La loi de Student n'est vue qu'en aperçu (une table, ou `scipy.stats.t.ppf`). Coût : environ 12 h au lieu de 10 (17 notions).

<a id="m09a"></a>
## M09a · Matrices et systèmes linéaires

**Partie** II · **prépare** workbookIA 9 · **dossier** `chapitres/m09a_matrices/` · **MML** §2.1, §2.2, §2.3 · **sessions de génération** 2

Les matrices et les systèmes linéaires : formes, produit matrice-vecteur et produit matriciel, produit de Hadamard, transposée et matrice XᵀX, systèmes, pivot de Gauss et forme échelonnée réduite, inverse, premier contact avec le rang ; la passe avant d'un réseau écrite comme un produit matriciel.

**Temps** : 16,7 h en parcours complet, 10,6 h en parcours essentiel (lecture 210 min, 26 flashcards).

**Objectifs**

- Lire un tableau de données comme une matrice et prévoir la forme de chaque produit.
- Calculer des produits matrice-vecteur et matriciels à la main, sous leurs deux lectures, et en compter le coût.
- Écrire une couche Z = XW + b et un embedding comme des produits matriciels.
- Appliquer les règles de la transposée et démontrer (AB)ᵀ = BᵀAᵀ.
- Résoudre un système par le pivot de Gauss et décrire toutes ses solutions.
- Calculer une inverse, un rang, et relier le rang au nombre de solutions.

**Sections de la fiche**

- §1 Matrices : un tableau de données est une matrice
- §2 Le produit matrice-vecteur : deux lectures
- §3 Le produit matriciel, le produit de Hadamard et Z = XW + b
- §4 La transposée et la matrice XᵀX
- §5 Systèmes linéaires : zéro, une ou une infinité de solutions
- §6 Le pivot de Gauss et la forme échelonnée réduite
- §7 L'inverse d'une matrice
- §8 Le rang : premier contact

**Notions enseignées** : matrices, formes · produit matrice-vecteur et matriciel · coût d'un produit matriciel · produit de Hadamard · transposée et ses règles · systèmes linéaires · pivot de Gauss, forme échelonnée et forme échelonnée réduite · inverse d'une matrice · rang (premier contact) · matrice identité, matrices diagonales · un dataset est une matrice : opérer par ligne, par colonne, élément par élément · Z = XW + b : la convention des poids · un embedding est un produit one-hot × matrice

**Prérequis** : systèmes 2 × 2, calcul littéral (R2) · Σ (R4) · vecteurs de ℝⁿ, produit scalaire, one-hot (M07) · moyenne, écart-type (M02c)

**mymath** : `matrices.py` (signatures figées) : `matmul`, `transpose`, `rref`, `rank`, `solve`, `inverse`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 9.6 ∂ Lasso en dimension 1 : le seuillage doux et les zéros exacts · 9.16 🔨 LinearRegression par moindres carrés · 9.17 🔨 Ridge en forme fermée, intercept non pénalisé · 10.14 🔨 neuron_forward : un neurone appliqué à tout un batch · 10.15 🔨 Des noms de poids (AD, BE…) à la matrice W

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M09a.Q1 | 🧠 | Formes : ce qui se multiplie et ce qui ne se multiplie pas | ★ | 4 | §1 §3 | C, E | manuel | — |
| M09a.Q2 | 🧠 | Le produit matrice-vecteur, deux lectures | ★ | 4 | §2 | C, E | manuel | — |
| M09a.Q3 | 🧠 | Produit matriciel : vrai ou faux | ★ | 4 | §3 | C, E | manuel | — |
| M09a.Q4 | 🧠 | Hadamard ou produit matriciel ? | ★ | 4 | §3 | C | manuel | — |
| M09a.Q5 | 🧠 | Les règles de la transposée | ★ | 4 | §4 | C, E | manuel | — |
| M09a.Q6 | 🧠 | Combien de solutions ? | ★ | 4 | §5 | C, E | manuel | — |
| M09a.Q7 | 🧠 | Les opérations permises sur les lignes | ★ | 4 | §6 | C, E | manuel | — |
| M09a.Q8 | 🧠 | Inverse et rang | ★ | 4 | §7 §8 | C, E | manuel | — |
| M09a.R1 | 🔁 | Les systèmes 2 × 2 (R2) | ★ | 5 | §5 | C, E | manuel | — |
| M09a.R2 | 🔁 | Produit scalaire et normes (M07) | ★ | 5 | §2 | C, E | manuel | — |
| M09a.R3 | 🔁 | Moyenne et écart-type empiriques (M02c) | ★ | 5 | §1 | C | manuel | — |
| M09a.1 | ✏️ | Un tableau de données vu comme une matrice : forme, lignes, colonnes, moyennes | ★ | 15 | §1 | C, E | wbm | — |
| M09a.2 | ✏️ | Le produit matrice-vecteur, par les lignes puis par les colonnes | ★ | 15 | §2 | C, E | wbm | — |
| M09a.3 | ✏️ | Produits matriciels à la main : formes compatibles et calculs | ★ | 20 | §3 | C, E | wbm | — |
| M09a.4 | ✏️ | Le coût d'un produit, et l'ordre des parenthèses dans ABC | ★★ | 15 | §3 | C | wbm | — |
| M09a.5 | ✏️ | Une couche dense Z = XW + b à la main : deux exemples, trois entrées, deux sorties | ★ | 20 | §3 | C, E | wbm | — |
| M09a.6 | ✏️ | Un embedding : une ligne one-hot fois une matrice | ★ | 10 | §3 | C | wbm | — |
| M09a.7 | ✏️ | Transposées de produits, et la matrice symétrique XᵀX | ★ | 15 | §4 | C, E | wbm | — |
| M09a.8 | ✏️ | Le pivot de Gauss sur un système 3 × 3 à solution unique | ★★ | 25 | §5 §6 | C, E | wbm | — |
| M09a.9 | ✏️ | Un système sans solution, un système à une infinité de solutions | ★★ | 25 | §5 §6 | C, E | wbm | — |
| M09a.10 | ✏️ | La forme échelonnée réduite d'une matrice 3 × 4 et la solution générale | ★★ | 20 | §6 | C | wbm | — |
| M09a.11 | ✏️ | L'inverse d'une matrice 2 × 2, par la formule, puis vérifiée | ★ | 15 | §7 | C, E | wbm | — |
| M09a.12 | ✏️ | L'inverse d'une matrice 3 × 3 par Gauss-Jordan | ★★ | 25 | §7 | C | wbm | — |
| M09a.13 | ✏️ | Le rang de quatre matrices, et les colonnes redondantes | ★★ | 20 | §8 | C, E | wbm | — |
| M09a.14 | ✏️ | Mettre un problème en système : trois engrais pour trois nutriments | ★★ | 20 | §5 | C | wbm | — |
| M09a.15 | ∂ | (AB)ᵀ = BᵀAᵀ, coefficient par coefficient | ★ | 15 | §4 | C, E | manuel | — |
| M09a.16 | ∂ | L'inverse est unique, et (AB)⁻¹ = B⁻¹A⁻¹ | ★★ | 15 | §7 | C | manuel | — |
| M09a.17 | ∂ | Deux solutions distinctes entraînent une infinité de solutions | ★★ | 15 | §5 | C, E | manuel | — |
| M09a.18 | ∂ | Une matrice dont une colonne combine les autres n'est pas inversible | ★★ | 20 | §7 §8 | C | manuel | — |
| M09a.19 | 🔗 | Pont : une passe avant à deux couches, deux produits matriciels et leurs formes | ★ | 15 | §3 | C, E | wbm | — |
| M09a.20 | 🔗 | Pont : centrer et réduire un tableau en écriture matricielle | ★★ | 15 | §1 §3 | C | wbm | — |
| M09a.21 | 📖 | MML §2.1 et §2.2 : systèmes et matrices, en anglais | ★★ | 30 | §1 §3 §5 | C | manuel | — |
| M09a.22 | 📖 | MML §2.3 : résoudre un système, la forme échelonnée et le « Minus-1 trick » | ★★ | 30 | §6 §8 | C | manuel | — |
| M09a.23 | 🧮 | Fermi : combien de multiplications pour une passe avant sur un million d'images ? | ★ | 10 | §3 | C | manuel | — |
| M09a.24 | 🗣️ | Expliquer pourquoi on ne calcule pas l'inverse pour résoudre un système | ★ | 10 | §7 | C, E | manuel | — |
| M09a.E1 | 💼 | « Combien coûte un produit matriciel, et pourquoi les GPU l'accélèrent-ils ? » | ★ | 10 | §3 | C | manuel | — |
| M09a.25 | 🔨 | Le produit matriciel et la transposée · `matmul, transpose` | ★ | 20 | §3 §4 | C, E | pytest | — |
| M09a.26 | 🔨 | La forme échelonnée réduite et le rang · `rref, rank` | ★★ | 35 | §6 §8 | C, E | pytest | — |
| M09a.27 | 🔨 | Résoudre un système par le pivot de Gauss · `solve` | ★★ | 30 | §6 | C, E | pytest | — |
| M09a.28 | 🔨 | L'inverse par Gauss-Jordan · `inverse` | ★ | 20 | §7 | C | pytest | M09a.26 |
| M09a.29 | 📦 | `@`, `*`, `.T`, `np.linalg.solve`, `matrix_rank` et `sympy.Matrix.rref` contre tes fonctions | ★ | 15 | §3 §6 §8 | C, E | wbm | — |
| M09a.30 | 🔮 | Prédire la forme du résultat : `@`, `*` et broadcasting | ★ | 10 | §1 §3 | C, E | wbm | — |
| M09a.31 | 🔬 | Le temps d'un produit matriciel en fonction de n : une pente de 3 en échelle log-log | ★★ | 20 | §3 | C | wbm | — |
| M09a.32 | 🔬 | Pourquoi le pivot partiel : un petit pivot et les arrondis | ★★ | 20 | §6 | C | wbm | — |
| M09a.33 | 🎨 | Une matrice 2 × 2 comme transformation du plan : la grille et le carré unité | ★ | 20 | §2 §3 | C | manuel | — |
| M09a.34 | 🐛 | Chasse à l'erreur : `*` au lieu de `@`, une transposée oubliée, un pivot nul | ★ | 15 | §3 §6 | C | wbm | — |
| M09a.35 | 🛠️ | Tester une propriété : un pytest pour (AB)ᵀ = BᵀAᵀ sur des matrices aléatoires | ★ | 15 | §4 | C | manuel | — |
| M09a.36 | 🏆 | Défi : un système 400 × 400 résolu par ton `solve`, à 1e−9 près de NumPy, en moins d'une seconde | ★★★ | 30 | §6 | C | wbm | — |

*Notes* : Évités (règle de partage) : le tempo de la boutique et California (workbookIA 9), le mini-exemple (0 ; 1), (1 ; 2), (2 ; 4) de sa fiche, les poids nommés AD, BE… et la conversion vers PyTorch (workbookIA 10.14, 10.15). M09a ne forme pas les équations normales (M09b). Z = XW + b suit la convention de `mylearn` (W de forme (n_in, n_out)) et signale celle de PyTorch. `mymath` écrit `rref` (la forme réduite, unique, donc testable contre SymPy) au lieu de `row_echelon` prévu. Deux sessions de génération : §1 à §4 (matrices et produits), puis §5 à §8 (systèmes, Gauss, inverse, rang).

<a id="m09b"></a>
## M09b · Moindres carrés et régularisation

**Partie** II · **prépare** workbookIA 9 · **dossier** `chapitres/m09b_moindres_carres/` · **MML** §5.5, §8.1, §8.2, §9.1, §9.2 · **sessions de génération** 2

La régression linéaire par les moindres carrés : risque empirique, MSE, MAE, Huber et R², gradients de aᵀw et de wᵀAw, équations normales, projection et matrice chapeau, features polynomiales, régularisation ridge (et ridge vue comme MAP), principe du lasso, régression vue comme maximum de vraisemblance, décomposition biais-variance, aperçu de la double descente.

**Temps** : 17,0 h en parcours complet, 9,9 h en parcours essentiel (lecture 210 min, 26 flashcards).

**Objectifs**

- Calculer les losses d'une régression (MSE, RMSE, MAE, Huber) et un R², et décomposer la variance.
- Calculer les gradients de aᵀw, de wᵀAw et de ‖y − Xw‖², et en déduire les équations normales en dimension p.
- Interpréter les moindres carrés comme une projection, avec la matrice chapeau.
- Compter les colonnes de features polynomiales.
- Résoudre un problème ridge, démontrer qu'il a toujours une solution et le relier à un prior gaussien.
- Démontrer que le bruit gaussien mène aux moindres carrés, et décomposer une erreur en biais², variance et bruit.

**Sections de la fiche**

- §1 Le problème : modèle linéaire, risque empirique et losses (MSE, MAE, Huber, R²)
- §2 Calcul matriciel minimal : les gradients de aᵀw, wᵀAw et ‖y − Xw‖²
- §3 Les équations normales, la projection et la matrice chapeau
- §4 Features polynomiales : compter les monômes
- §5 La régression ridge, et ridge vue comme un MAP
- §6 Le lasso : le principe de la parcimonie
- §7 La régression comme maximum de vraisemblance
- §8 Biais, variance et double descente

**Notions enseignées** : risque empirique · gradients de aᵀw et de wᵀAw (calcul matriciel minimal) · moindres carrés · équations normales · projection et matrice chapeau · features polynomiales : combien de monômes (combinaisons avec répétition) · régularisation ridge · ridge comme MAP · lasso (principe) · MSE, MAE, loss de Huber, R², RMSE · décomposition biais-variance · overfitting et underfitting vus par le biais et la variance · régression comme maximum de vraisemblance · double descente (aperçu) · pénalité L2 et weight decay

**Prérequis** : matrices, transposée, inverse, pivot de Gauss, rang (M09a) · normes, produit scalaire, projection sur une droite (M07) · gradient, point critique (M05b) · vraisemblance, MAP (M04) · loi normale (M02b) · biais et variance d'un estimateur (M02c) · combinaisons (R8)

**mymath** : `linreg.py` (signatures figées) : `normal_equations`, `solve_least_squares`, `hat_matrix`, `residual_decomposition`, `count_monomials`, `huber_loss`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 9.6 ∂ Lasso en dimension 1 : le seuillage doux et les zéros exacts · 9.1 ✏️ MSE et R² à la main sur cinq points · 9.4 ✏️ Biais² et variance à partir d'un tableau de prédictions · 9.7 ✏️ Mise à jour bayésienne d'une droite sur une grille 3 × 3 · 9.14 🔨 mean_squared_error, mean_absolute_error et r2_score · 9.15 🔨 polynomial_features, interactions comprises · 9.16 🔨 LinearRegression par moindres carrés · 9.17 🔨 Ridge en forme fermée, intercept non pénalisé · 9.19 🔮 Que deviennent les coefficients quand λ grandit ? · 9.23 🔨 Lasso par descente de coordonnées et soft_threshold · 9.24 🔨 Biais et variance mesurés : 50 sous-échantillons de 30 points · 9.26 🔨 Le posterior des droites sur une grille pente-ordonnée · 9.E3 💼 Régularisation L1 ou L2 : différences et usages

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M09b.Q1 | 🧠 | MSE, RMSE, MAE, R² : ce que mesure chacune | ★ | 4 | §1 | C, E | manuel | — |
| M09b.Q2 | 🧠 | Gradients matriciels : associer chaque fonction à son gradient | ★ | 4 | §2 | C, E | manuel | — |
| M09b.Q3 | 🧠 | Équations normales : quand la solution est-elle unique ? | ★ | 4 | §3 | C, E | manuel | — |
| M09b.Q4 | 🧠 | Linéaire en x ou linéaire en w ? | ★ | 4 | §4 | C, E | manuel | — |
| M09b.Q5 | 🧠 | Ridge : vrai ou faux sur la pénalité L2 | ★ | 4 | §5 | C, E | manuel | — |
| M09b.Q6 | 🧠 | Lasso ou ridge : qui annule des poids ? | ★ | 4 | §6 | C | manuel | — |
| M09b.Q7 | 🧠 | Bruit gaussien et moindres carrés | ★ | 4 | §7 | C, E | manuel | — |
| M09b.Q8 | 🧠 | Biais, variance, bruit : ce qui change quand le modèle se complique | ★ | 4 | §8 | C, E | manuel | — |
| M09b.R1 | 🔁 | Le pivot de Gauss et l'inverse (M09a) | ★ | 5 | §3 | C, E | manuel | — |
| M09b.R2 | 🔁 | Maximum de vraisemblance et MAP (M04) | ★ | 5 | §5 §7 | C, E | manuel | — |
| M09b.R3 | 🔁 | Gradient et point critique (M05b) | ★ | 5 | §2 | C, E | manuel | — |
| M09b.1 | ✏️ | MSE, RMSE, MAE et loss de Huber de quatre résidus | ★ | 15 | §1 | C, E | wbm | — |
| M09b.2 | ✏️ | La décomposition SCT = SCE + SCR et le R² d'un ajustement donné | ★ | 20 | §1 §3 | C | wbm | — |
| M09b.3 | ✏️ | Les gradients de aᵀw, wᵀAw et ‖y − Xw‖², composante par composante en dimension 2 | ★★ | 20 | §2 | C, E | wbm | — |
| M09b.4 | ✏️ | Les équations normales d'un modèle à deux features, sans ordonnée à l'origine | ★★ | 20 | §3 | C, E | wbm | — |
| M09b.5 | ✏️ | La colonne de 1 : l'ordonnée à l'origine et des résidus de moyenne nulle | ★★ | 20 | §3 | C, E | wbm | — |
| M09b.6 | ✏️ | La matrice chapeau d'un petit tableau : H² = H et sa trace | ★★ | 20 | §3 | C | wbm | — |
| M09b.7 | ✏️ | Compter les monômes des features polynomiales | ★ | 15 | §4 | C, E | wbm | — |
| M09b.8 | ✏️ | Ridge en dimension 2 : résoudre (XᵀX + λI)w = Xᵀy pour trois valeurs de λ | ★★ | 20 | §5 | C, E | wbm | — |
| M09b.9 | ✏️ | Ridge comme MAP : un prior gaussien et λ = σ²/τ² | ★★ | 20 | §5 §7 | C | wbm | — |
| M09b.10 | ✏️ | Les pénalités L1 et L2 de trois vecteurs de poids, et leurs boules | ★ | 15 | §6 | C | wbm | — |
| M09b.11 | ✏️ | La log-vraisemblance gaussienne d'un modèle linéaire et l'estimation de σ² | ★★ | 20 | §7 | C | wbm | — |
| M09b.12 | ✏️ | L'estimateur rétréci c·x̄ : biais, variance et erreur quadratique | ★★ | 20 | §8 | C | wbm | — |
| M09b.13 | ∂ | Le gradient de wᵀAw vaut (A + Aᵀ)w | ★★ | 20 | §2 | C, E | manuel | — |
| M09b.14 | ∂ | Les équations normales en dimension p, par le gradient | ★★ | 25 | §2 §3 | C, E | manuel | — |
| M09b.15 | ∂ | Le résidu est orthogonal aux colonnes de X ; H est symétrique et idempotente | ★★ | 20 | §3 | C | manuel | — |
| M09b.16 | ∂ | XᵀX + λI est inversible pour tout λ > 0 | ★★ | 20 | §5 | C, E | manuel | — |
| M09b.17 | ∂ | Un bruit gaussien mène aux moindres carrés : le maximum de vraisemblance | ★★ | 20 | §7 | C, E | manuel | — |
| M09b.18 | ∂ | La décomposition biais² + variance + bruit, démontrée | ★★★ | 25 | §8 | C | manuel | — |
| M09b.19 | ∂ | Le nombre de monômes de degré au plus d en p variables : C(p + d, d) | ★★★ | 25 | §4 | C | manuel | — |
| M09b.20 | 🔗 | Pont : la loss d'un modèle linéaire et son gradient pour un batch, prêts pour la descente de gradient | ★ | 15 | §2 | C, E | wbm | — |
| M09b.21 | 🔗 | Pont : pourquoi standardiser les colonnes avant ridge | ★ | 15 | §5 | C | wbm | — |
| M09b.22 | 📖 | MML §5.5, §8.1 et §8.2 : identités de gradients et minimisation du risque empirique | ★★ | 30 | §1 §2 | C | manuel | — |
| M09b.23 | 📖 | MML §9.1 et §9.2 : régression linéaire, maximum de vraisemblance et MAP | ★★ | 30 | §3 §5 §7 | C | manuel | — |
| M09b.24 | 🧮 | Fermi : la taille de XᵀX pour des features polynomiales de degré 3 sur 100 variables | ★ | 10 | §4 | C | manuel | — |
| M09b.25 | 🗣️ | Expliquer la matrice chapeau : ce que veut dire « projeter y » | ★ | 10 | §3 | C, E | manuel | — |
| M09b.E1 | 💼 | « Pourquoi ne pas inverser XᵀX, et que faire si des features sont colinéaires ? » | ★ | 10 | §3 §5 | C | manuel | — |
| M09b.E2 | 💼 | « Quel lien entre la régularisation L2 et un prior gaussien ? » | ★ | 10 | §5 §7 | C | manuel | — |
| M09b.26 | 🔨 | Équations normales et résolution, avec ou sans ridge · `normal_equations, solve_least_squares` | ★ | 25 | §3 §5 | C, E | pytest | — |
| M09b.27 | 🔨 | La matrice chapeau et les trois sommes de carrés · `hat_matrix, residual_decomposition` | ★ | 20 | §1 §3 | C, E | pytest | M09b.26 |
| M09b.28 | 🔨 | Compter les monômes, et la loss de Huber · `count_monomials, huber_loss` | ★ | 15 | §1 §4 | C | pytest | — |
| M09b.29 | 📦 | `np.linalg.lstsq` et scikit-learn contre tes équations normales | ★ | 15 | §3 | C, E | wbm | — |
| M09b.30 | 🔮 | Prédire : le R² d'entraînement quand on ajoute une feature de pur bruit | ★ | 10 | §1 §4 | C, E | wbm | — |
| M09b.31 | 🔬 | Simuler l'estimateur rétréci c·x̄ : le c qui minimise l'erreur quadratique | ★★ | 20 | §8 | C | wbm | — |
| M09b.32 | 🔬 | Le conditionnement de XᵀX avec des puissances non standardisées | ★★ | 20 | §4 | C | wbm | — |
| M09b.33 | 🎨 | Les lignes de niveau de la loss des moindres carrés en dimension 2, et son gradient | ★ | 20 | §2 §3 | C | manuel | — |
| M09b.34 | 🐛 | Chasse à l'erreur : XXᵀ au lieu de XᵀX, un gradient de mauvais signe, un R² sans centrer | ★ | 15 | §1 §2 §3 | C | wbm | — |
| M09b.35 | 🛠️ | Vérifier un gradient matriciel avec SymPy et par différences finies | ★ | 15 | §2 | C | manuel | — |
| M09b.36 | 🏆 | Défi : approcher une fonction par un polynôme de degré au plus 5, avec une erreur maximale sous 1e−3 | ★★★ | 25 | §3 §4 | C | wbm | — |

*Notes* : Frontières : les moindres carrés d'une droite par dérivées partielles (9.2), ridge (9.3) et lasso (9.6) en dimension 1 ne sont pas démontrés ici : M09b travaille en dimension p, par les gradients matriciels, et énonce le seuillage doux sans le dériver. Évités : le tempo de la boutique, California, les mini-exemples de la fiche de workbookIA 9 (les points (0 ; 1), (1 ; 2), (2 ; 4) ; les cibles 1, 4, 6 et les prédictions 2, 4, 3 ; Σxy = 6 et Σx² = 4 ; S(1,8 ; 0,5) ; les prédictions 1, 2 et 4 du biais-variance ; les dénombrements 9 pour p = 3 et d = 2, 285 pour p = 10 et d = 3), la grille 3 × 3 de droites (9.7), les MSE et R² sur cinq points (9.1), le tableau de prédictions de 9.4. La régression bayésienne (MML §9.3) se lit en M25a, la projection sur un sous-espace (MML §9.4) en M12b. MSE, MAE, R², features polynomiales, LinearRegression, Ridge, Lasso, soft_threshold et la décomposition biais-variance sont les fonctions de `mylearn` en workbookIA 9 ; `linreg` écrit les briques (équations normales, ridge qui pénalise tous les coefficients, matrice chapeau, sommes de carrés, nombre de monômes, Huber). Deux sessions de génération : §1 à §4, puis §5 à §8.

<a id="m10"></a>
## M10 · Séparabilité linéaire et convexité

**Partie** II · **prépare** workbookIA 10 · **dossier** `chapitres/m10_separabilite_convexite/` · **MML** §12.1 · **sessions de génération** 1

Les ensembles convexes et l'enveloppe convexe, la séparation de deux nuages par un hyperplan, l'astuce du biais et la marge géométrique, les récurrences sur une norme, et les fonctions d'activation appliquées à un score linéaire : les outils que workbookIA 10 assemble pour le perceptron.

**Temps** : 8,1 h en parcours complet, 5,7 h en parcours essentiel (lecture 110 min, 16 flashcards).

**Objectifs**

- Reconnaître et démontrer qu'un ensemble est convexe.
- Construire l'enveloppe convexe d'un nuage du plan, à la main et en code.
- Démontrer que deux nuages séparables ont des enveloppes convexes disjointes, et tester la séparabilité.
- Calculer une marge géométrique, et passer d'un hyperplan affine à un hyperplan par l'origine (astuce du biais).
- Borner une suite de normes pas à pas.

**Sections de la fiche**

- §1 Ensembles convexes
- §2 L'enveloppe convexe
- §3 Séparer deux nuages : séparabilité linéaire, astuce du biais, marge
- §4 Récurrences sur une norme : croissance linéaire contre croissance en √k
- §5 Activations : des fonctions d'une variable appliquées à un score

**Notions enseignées** : ensembles convexes · fonctions convexes et strictement convexes de plusieurs variables (définition) · enveloppe convexe · séparabilité linéaire (enveloppes convexes disjointes) · astuce du biais (une coordonnée en plus) · marge géométrique · inégalités de récurrence sur une norme · fonctions d'activation : des fonctions d'une variable (rappel R3, R6)

**Prérequis** : hyperplans, distance à un hyperplan, Cauchy-Schwarz (M07) · produit matriciel (M09a) · raisonnement par récurrence (R4) · sigmoïde, tanh (R6) · fonctions, composition (R3) · convexité d'une fonction (M05a)

**mymath** : `convex.py` (signatures figées) : `convex_hull_2d`, `is_linearly_separable`, `margin_of_separator`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 10.4 ∂ Pourquoi un seul perceptron ne peut pas calculer XOR · 10.7 ∂ Le théorème de convergence du perceptron, guidé pas à pas · 10.1 ✏️ Sortie d'un perceptron à quatre entrées, avec et sans biais · 10.2 ✏️ L'astuce du biais : même neurone, une entrée de plus · 10.3 ✏️ Portes logiques à la main : AND, OR, NOT, NAND · 10.5 ✏️ XOR en deux couches : câbler et nommer les poids · 10.6 ✏️ Une epoch de la règle du perceptron à la main · 10.13 🔮 AND, OR, XOR : le perceptron va-t-il converger ? · 10.19 📈 Erreurs par epoch : séparable ou pas ? · 10.23 🔬 Marge et vitesse de convergence : la borne (R/γ)² à l'épreuve

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M10.Q1 | 🧠 | Convexe ou non ? | ★ | 4 | §1 | C, E | manuel | — |
| M10.Q2 | 🧠 | L'enveloppe convexe : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| M10.Q3 | 🧠 | Séparable ou non ? | ★ | 4 | §3 | C, E | manuel | — |
| M10.Q4 | 🧠 | Marge et astuce du biais | ★ | 4 | §3 | C | manuel | — |
| M10.R1 | 🔁 | Hyperplans et distance à un hyperplan (M07) | ★ | 5 | §3 | C, E | manuel | — |
| M10.R2 | 🔁 | L'inégalité de Cauchy-Schwarz (M07) | ★ | 5 | §4 | C, E | manuel | — |
| M10.R3 | 🔁 | La sigmoïde et tanh (R6) | ★ | 5 | §5 | C | manuel | — |
| M10.1 | ✏️ | Convexe ou non : segments, demi-plans, intersections | ★ | 15 | §1 | C, E | wbm | — |
| M10.2 | ✏️ | L'enveloppe convexe de huit points, à la main | ★ | 20 | §2 | C, E | wbm | — |
| M10.3 | ✏️ | Une droite qui sépare deux petits nuages, et sa marge | ★★ | 20 | §3 | C, E | wbm | — |
| M10.4 | ✏️ | L'astuce du biais : une droite du plan devient un plan de ℝ³ passant par l'origine | ★ | 15 | §3 | C | wbm | — |
| M10.5 | ✏️ | Borner une norme pas à pas : ‖v_{k+1}‖² ≤ ‖v_k‖² + c | ★★ | 15 | §4 | C | wbm | — |
| M10.6 | ∂ | Un demi-espace est convexe, et une intersection de convexes aussi | ★ | 15 | §1 | C, E | manuel | — |
| M10.7 | ∂ | Deux nuages séparés par un hyperplan ont des enveloppes convexes disjointes | ★★ | 20 | §2 §3 | C, E | manuel | — |
| M10.8 | ∂ | La marge géométrique ne change pas quand on multiplie (w, b) par un réel positif | ★ | 15 | §3 | C | manuel | — |
| M10.9 | 🔗 | Pont : seuil, sigmoïde, tanh et ReLU appliqués à un même score linéaire | ★ | 15 | §5 | C, E | wbm | — |
| M10.10 | 📖 | MML §12.1 : les hyperplans séparateurs, en anglais | ★★ | 20 | §3 | C | manuel | — |
| M10.11 | 🗣️ | Expliquer la convexité et l'enveloppe convexe avec un élastique | ★ | 10 | §1 §2 | C, E | manuel | — |
| M10.E1 | 💼 | « Que veut dire « linéairement séparable », et comment le vérifier ? » | ★ | 10 | §3 | C | manuel | — |
| M10.12 | 🔨 | L'enveloppe convexe dans le plan : la chaîne monotone d'Andrew · `convex_hull_2d` | ★★ | 25 | §2 | C, E | pytest | — |
| M10.13 | 🔨 | Séparabilité par programmation linéaire, et marge géométrique · `is_linearly_separable, margin_of_separator` | ★★ | 25 | §3 | C, E | pytest | — |
| M10.14 | 🔮 | Prédire : n points aux labels tirés au hasard en dimension d sont-ils séparables ? | ★ | 10 | §3 | C, E | wbm | — |
| M10.15 | 🎨 | Deux nuages, leurs enveloppes convexes et un hyperplan séparateur avec sa marge | ★ | 15 | §2 §3 | C | manuel | — |
| M10.16 | 🐛 | Chasse à l'erreur : un produit vectoriel de signe inversé, une marge non normalisée | ★ | 15 | §2 §3 | C | wbm | — |
| M10.17 | 🛠️ | Des tests de propriétés pour l'enveloppe convexe | ★ | 15 | §2 | C | manuel | — |
| M10.18 | 🏆 | Défi : la plus grande marge possible entre deux nuages donnés, à 1 % près | ★★★ | 20 | §3 | C | wbm | — |

*Notes* : Frontières : XOR n'est pas séparable (10.4) et la convergence du perceptron (10.7) sont démontrés en workbookIA 10 : M10 démontre l'énoncé général (deux nuages séparables ont des enveloppes convexes disjointes) sans l'appliquer aux portes logiques, et enseigne les récurrences sur une norme sur une suite quelconque, sans la règle du perceptron ni la borne (R/γ)². Évités : les portes logiques (AND, OR, NOT, NAND, XOR), le perceptron et sa règle, les manchots, les chiffres de 20 × 20 pixels ; la marge et l'astuce du biais sont vues en géométrie (10.2 et 10.23 restent à workbookIA). COMPOSITION : chapitre court (8 h, puis 8,1 h quand l'apprenant simulé a allongé M10.2 et M10.16, sans contenu nouveau) : la moitié de la composition, papier d'abord ; pas de 🔬 ni de 📦 (le 🔮 sur le théorème de Cover et les deux 🔨 suffisent).

<a id="m11"></a>
## M11 · Logique, induction et inégalités de concentration

**Partie** II · **prépare** workbookIA 11 · **dossier** `chapitres/m11_logique_concentration/` · **MML** — · **sessions de génération** 1

La logique au service du raisonnement (implication, contraposée, négation, validité, ensembles et contre-exemples, induction et ses pièges) ; puis les inégalités de Markov, Tchebychev et Hoeffding, le rayon de confiance d'une moyenne, et ce qu'elles disent des bandits : bornes supérieures de confiance, ε-greedy, regret, échantillonnage de Thompson.

**Temps** : 11,5 h en parcours complet, 7,2 h en parcours essentiel (lecture 150 min, 22 flashcards).

**Objectifs**

- Écrire la contraposée et la négation d'un énoncé, et décider par une table de vérité si un argument est valide.
- Traduire des phrases en inclusions d'ensembles et construire un contre-exemple.
- Repérer les pièges d'une induction (taux de base, échantillon biaisé, corrélation).
- Démontrer et appliquer les inégalités de Markov et de Tchebychev, et en déduire la loi faible des grands nombres.
- Appliquer l'inégalité de Hoeffding : rayon de confiance et taille d'échantillon.
- Expliquer d'où vient le bonus d'une borne supérieure de confiance, et calculer le regret attendu d'ε-greedy.

**Sections de la fiche**

- §1 Raisonner juste : implication, contraposée, négation, validité
- §2 Ensembles, diagrammes de Venn et contre-exemples
- §3 L'induction et ses pièges
- §4 L'inégalité de Markov
- §5 L'inégalité de Tchebychev et la loi des grands nombres
- §6 L'inégalité de Hoeffding et le rayon de confiance
- §7 Explorer ou exploiter : bornes supérieures de confiance, ε-greedy, regret, Thompson

**Notions enseignées** : déduction, validité, solidité · modus ponens, modus tollens et sophismes formels · ensembles et contre-exemples · induction et ses pièges · inégalité de Markov · inégalité de Tchebychev · loi faible des grands nombres (démontrée) · inégalité de Hoeffding · rayon de confiance d'une moyenne · bornes supérieures de confiance (UCB, principe) · ε-greedy · regret · échantillonnage de Thompson

**Prérequis** : propositions, quantificateurs, implication, ensembles, raisonnements (R4) · suites définies par récurrence (l'outil de la moyenne incrémentale) (R5) · exp et ln (R6) · espérance, variance, lois exponentielle et binomiale (M02b) · moyenne empirique, TCL, intervalle de confiance (M02c) · probabilités totales, taux de base (M03) · formule de Bayes, loi Beta a posteriori (M04)

**mymath** : `concentration.py` (signatures figées) : `markov_bound`, `chebyshev_bound`, `hoeffding_bound`, `hoeffding_radius`, `empirical_tail`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 11.2 ∂ Moyenne incrémentale : Qₙ₊₁ = Qₙ + (Rₙ − Qₙ)/n · 11.1 ✏️ Représentable sur n bits : compter, puis conclure · 11.3 ✏️ Syllogismes : valides ? solides ? · 11.4 ✏️ Six raisonnements fautifs à diagnostiquer et à réfuter · 11.5 ✏️ Enquête au phare : réduire le domaine du discours · 11.6 ✏️ Syllogisme statistique et prédiction : 15 % de pommes mûres · 11.7 ✏️ Renforcement ou punition, positif ou négatif : classer huit situations · 11.8 ✏️ Un bandit à la main : ε-greedy, moyennes et regret · 11.15 🔨 Valider un syllogisme par force brute : 256 mondes de Venn · 11.20 🔨 argmax_random_tie, epsilon_greedy_action et incremental_update · 11.23 🔨 ucb_action et thompson_action · 11.E2 💼 A/B test ou bandit : lequel choisir ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M11.Q1 | 🧠 | Réciproque, contraposée, négation | ★ | 4 | §1 | C, E | manuel | — |
| M11.Q2 | 🧠 | Un argument valide peut-il avoir une conclusion fausse ? | ★ | 4 | §1 | C, E | manuel | — |
| M11.Q3 | 🧠 | Diagrammes de Venn et quantificateurs | ★ | 4 | §2 | C | manuel | — |
| M11.Q4 | 🧠 | Les pièges de l'induction | ★ | 4 | §3 | C, E | manuel | — |
| M11.Q5 | 🧠 | Markov ou Tchebychev : quelle borne s'applique ? | ★ | 4 | §4 §5 | C, E | manuel | — |
| M11.Q6 | 🧠 | Ce que garantit l'inégalité de Hoeffding, et ce qu'elle suppose | ★ | 4 | §6 | C, E | manuel | — |
| M11.Q7 | 🧠 | Explorer ou exploiter : vrai ou faux | ★ | 4 | §7 | C | manuel | — |
| M11.R1 | 🔁 | Implication et contraposée (R4) | ★ | 5 | §1 | C, E | manuel | — |
| M11.R2 | 🔁 | Espérance et variance (M02b) | ★ | 5 | §4 §5 | C, E | manuel | — |
| M11.R3 | 🔁 | La loi Beta a posteriori (M04) | ★ | 5 | §7 | C | manuel | — |
| M11.1 | ✏️ | Tables de vérité : modus ponens, modus tollens et l'affirmation du conséquent | ★ | 20 | §1 | C, E | wbm | — |
| M11.2 | ✏️ | Nier des phrases quantifiées sur des modèles et des datasets | ★ | 15 | §1 | C, E | wbm | — |
| M11.3 | ✏️ | Des phrases traduites en inclusions d'ensembles, et un contre-exemple | ★★ | 15 | §2 | C | wbm | — |
| M11.4 | ✏️ | Une induction trompeuse par oubli du taux de base, recalculée avec Bayes | ★★ | 15 | §3 | C, E | wbm | — |
| M11.5 | ✏️ | Markov : la queue d'une durée positive | ★ | 15 | §4 | C, E | wbm | — |
| M11.6 | ✏️ | Tchebychev : combien d'observations pour une moyenne à ± 0,1 ? | ★★ | 20 | §5 | C, E | wbm | — |
| M11.7 | ✏️ | Hoeffding : rayon de confiance et taille d'échantillon d'une proportion | ★★ | 20 | §6 | C, E | wbm | — |
| M11.8 | ✏️ | Trois bornes pour une même question : Markov, Tchebychev, Hoeffding, et l'approximation normale | ★★ | 20 | §4 §5 §6 | C | wbm | — |
| M11.9 | ✏️ | D'où vient le bonus d'UCB : Hoeffding avec un risque qui décroît avec t | ★★★ | 20 | §6 §7 | C | wbm | — |
| M11.10 | ✏️ | ε-greedy : la loi du bras joué et le regret attendu par pas | ★★ | 15 | §7 | C | wbm | — |
| M11.11 | ∂ | L'inégalité de Markov | ★ | 15 | §4 | C, E | manuel | — |
| M11.12 | ∂ | Tchebychev à partir de Markov, puis la loi faible des grands nombres | ★★ | 20 | §5 | C, E | manuel | — |
| M11.13 | ∂ | Avec ε fixé, le regret attendu d'ε-greedy croît au moins linéairement | ★★ | 20 | §7 | C | manuel | — |
| M11.14 | 🔗 | Pont : combien d'exemples de test pour connaître une accuracy à ± 2 points, garanti par Hoeffding ? | ★ | 15 | §6 | C, E | wbm | — |
| M11.15 | ⚖️ | Corrélation, causalité et induction : trois titres de presse à démonter | ★★ | 20 | §3 | C | manuel | — |
| M11.16 | 🗣️ | Expliquer « l'optimisme face à l'incertitude » à partir d'un intervalle de confiance | ★ | 10 | §7 | C, E | manuel | — |
| M11.E1 | 💼 | « À quoi sert l'inégalité de Hoeffding en apprentissage, et que suppose-t-elle ? » | ★ | 10 | §6 | C | manuel | — |
| M11.17 | 🔨 | Les bornes de Markov et de Tchebychev · `markov_bound, chebyshev_bound` | ★ | 15 | §4 §5 | C, E | pytest | — |
| M11.18 | 🔨 | La borne et le rayon de Hoeffding · `hoeffding_bound, hoeffding_radius` | ★ | 15 | §6 | C, E | pytest | — |
| M11.19 | 🔨 | La queue empirique d'un échantillon · `empirical_tail` | ★ | 10 | §4 | C | pytest | — |
| M11.20 | 📦 | Les vraies queues d'une loi exponentielle et d'une binomiale (`scipy.stats`) contre les bornes | ★ | 15 | §4 §5 §6 | C | wbm | — |
| M11.21 | 🔮 | Prédire : laquelle des trois bornes est la plus serrée pour n = 100 ? | ★ | 10 | §6 | C, E | wbm | — |
| M11.22 | 🔬 | La fréquence des écarts |x̄ − p| ≥ t comparée à la borne de Hoeffding, quand n grandit | ★★ | 20 | §6 | C | wbm | — |
| M11.23 | 🔬 | La probabilité qu'un tirage d'une loi Beta dépasse celui d'une autre, par simulation | ★★ | 15 | §7 | C | wbm | — |
| M11.24 | 🎨 | Les bornes de Markov, de Tchebychev et de Hoeffding contre la vraie queue, en échelle log | ★ | 15 | §4 §5 §6 | C | manuel | — |
| M11.25 | 🐛 | Chasse à l'erreur : Markov pour une variable négative, Hoeffding sans bornes, un rayon sans racine | ★ | 15 | §4 §6 | C | wbm | — |
| M11.26 | 🛠️ | Un test paramétré qui vérifie l'inégalité de Markov sur dix lois | ★ | 15 | §4 | C | manuel | — |
| M11.27 | 🏆 | Défi : la plus petite taille d'échantillon qui garantit une moyenne à ± 0,05 avec 99 %, vérifiée sur une loi défavorable | ★★★ | 25 | §6 | C | wbm | — |

*Notes* : Frontière : la moyenne incrémentale (11.2) est démontrée par workbookIA ; M11 s'appuie sur les suites de R5. Évités (règle de partage) : les syllogismes catégoriques de workbookIA 11 (Barbara, les chats carnivores, Socrate, les formes A, E, I, O et leurs règles, les 256 mondes de Venn de 11.15), le phare (11.5), les pommes mûres (11.6), Holmes, le renforcement et la punition (11.7), le bandit à la main de 11.8 et les nombres de la fiche (récompenses 4, 2, 6 ; ε = 0,1 et K = 4, qui donnent 0,925 ; UCB avec c = 2 et t = 25 ; les moyennes 0,1, 0,4 et 0,7 du regret ; 48 spams sur 400). M11 enseigne la logique propositionnelle (tables de vérité, R4) et les ensembles plutôt que les syllogismes, et les bandits par leurs outils (bornes, regret attendu, loi d'un tirage Beta), sans agent ni boucle de jeu (les fonctions de `mylearn` en workbookIA 11). Pas de 📖 : MML ne traite ni la logique ni les inégalités de concentration. Coût : environ 11 h au lieu de 10.

<a id="cp2"></a>
## CP2 · Examen blanc de la partie II

**Partie** II · **prépare** — · **dossier** `checkpoints/partie_2/` · **MML** — · **sessions de génération** 1

Le bilan de la partie II (M07 à M11), juste avant le checkpoint II de workbookIA : un examen blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.

**Temps** : 3,2 h en parcours complet, 3,2 h en parcours essentiel (lecture 15 min, 0 flashcards).

**Objectifs**

- Vérifier en temps limité que les notions de la partie II sont acquises.
- Construire ta propre synthèse de la partie II.

**Sections de la fiche**

- §1 Examen blanc
- §2 Synthèse

**Notions enseignées** : révision de la partie II

**Prérequis** : toute la partie II (M11)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 7.5 ∂ Le rayon de l'hyper-orange : r(d) = √d − 1 · 7.6 ∂ Boule dans un cube : rapport des volumes par récurrence · 7.7 ∂ La frontière du centroïde le plus proche est une droite · 8.6 ∂ Le biais d'optimisme du meilleur de K modèles · 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 9.6 ∂ Lasso en dimension 1 : le seuillage doux et les zéros exacts · 10.4 ∂ Pourquoi un seul perceptron ne peut pas calculer XOR · 10.7 ∂ Le théorème de convergence du perceptron, guidé pas à pas · 11.2 ∂ Moyenne incrémentale : Qₙ₊₁ = Qₙ + (Rₙ − Qₙ)/n

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| CP2.Q1 | 🧠 | Dix affirmations sur la partie II : vrai ou faux | ★ | 10 | §1 | C, E | manuel | — |
| CP2.1 | ✏️ | Normes, cosinus, projection et distance à un hyperplan | ★★ | 10 | §1 | C, E | wbm | — |
| CP2.2 | ✏️ | Un test binomial et un intervalle de Wilson | ★★ | 10 | §1 | C, E | wbm | — |
| CP2.3 | ✏️ | Comparaisons multiples, AIC et BIC | ★★ | 8 | §1 | C, E | wbm | — |
| CP2.4 | ✏️ | Pivot de Gauss, rang et inverse | ★★ | 10 | §1 | C, E | wbm | — |
| CP2.5 | ✏️ | Les équations normales d'un petit modèle, avec et sans ridge | ★★ | 10 | §1 | C, E | wbm | — |
| CP2.6 | ✏️ | Biais, variance et erreur quadratique d'un estimateur | ★★ | 8 | §1 | C, E | wbm | — |
| CP2.7 | ✏️ | Convexité, enveloppe convexe et marge | ★★ | 8 | §1 | C, E | wbm | — |
| CP2.8 | ✏️ | Markov, Tchebychev et Hoeffding | ★★ | 9 | §1 | C, E | wbm | — |
| CP2.9 | ∂ | Une démonstration courte, au choix parmi deux | ★★★ | 12 | §1 | C, E | manuel | — |
| CP2.10 | 🐛 | Corriger une copie : cinq erreurs | ★★ | 8 | §1 | C, E | wbm | — |
| CP2.11 | 🔗 | Problème de synthèse : ajuster un modèle, mesurer son erreur, décider | ★★ | 14 | §1 | C, E | wbm | — |
| CP2.12 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme CP1 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, 03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend le checkpoint II de workbookIA (`checkpoints/partie_2/` de workbookIA : un-contre-tous et un-contre-un, une itération de k-means, densité et hyper-orange, plan d'évaluation, ridge en dimension 1, courbes d'apprentissage, perceptron sur NAND, syllogismes, fuite d'une validation croisée, ε-greedy et moyenne incrémentale), qui se fait juste après, ni son mini-projet II (California).

<a id="m12a"></a>
## M12a · Espaces vectoriels et applications linéaires

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12a_espaces_vectoriels/` · **MML** §2.4, §2.5, §2.6, §2.7, §2.8 · **sessions de génération** 2

Les espaces vectoriels et les applications linéaires : sous-espaces, combinaisons linéaires et familles génératrices, indépendance, base et dimension, coordonnées, rang, matrice d'une application linéaire, noyau, image et théorème du rang, changement de base, applications et espaces affines, transformation inverse.

**Temps** : 16,6 h en parcours complet, 10,8 h en parcours essentiel (lecture 210 min, 26 flashcards).

**Objectifs**

- Reconnaître un sous-espace vectoriel et le décrire par une famille génératrice ou par des équations.
- Décider si une famille est libre, en extraire une base, et calculer des coordonnées dans une base.
- Calculer le rang d'une matrice et majorer celui d'un produit.
- Écrire la matrice d'une application linéaire, et composer des applications en multipliant leurs matrices.
- Calculer un noyau et une image, appliquer le théorème du rang, et décrire toutes les solutions de A x = b.
- Changer de base, et inverser une application affine.

**Sections de la fiche**

- §1 Espaces vectoriels et sous-espaces
- §2 Combinaisons linéaires, familles génératrices et indépendance
- §3 Bases, dimension et coordonnées
- §4 Le rang, et le rang d'un produit
- §5 Applications linéaires et leur matrice
- §6 Noyau, image et théorème du rang
- §7 Changer de base
- §8 Applications affines et transformation inverse

**Notions enseignées** : espace vectoriel, sous-espace · combinaison linéaire, famille génératrice · indépendance linéaire · base et dimension · coordonnées dans une base · rang, rang d'un produit · application linéaire et sa matrice · composition et produit · noyau et image · théorème du rang · changement de base · applications et espaces affines · application réciproque, transformation inverse

**Prérequis** : pivot de Gauss, forme échelonnée réduite, rang (premier contact), inverse (M09a) · vecteurs de ℝⁿ, combinaisons linéaires, produit scalaire (M07) · raisonnements, ensembles (R4) · dérivée d'un polynôme (R7) · centrer et réduire (M02c)

**mymath** : `linmaps.py` (signatures figées) : `is_independent`, `column_space_basis`, `null_space_basis`, `coordinates`, `change_of_basis`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale · 15.3 ✏️ Ramener une droite ajustée dans l'espace d'origine

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M12a.Q1 | 🧠 | Sous-espace ou pas ? | ★ | 4 | §1 | C, E | manuel | — |
| M12a.Q2 | 🧠 | Combinaison linéaire et famille génératrice | ★ | 4 | §2 | C, E | manuel | — |
| M12a.Q3 | 🧠 | Libre ou liée ? | ★ | 4 | §2 | C, E | manuel | — |
| M12a.Q4 | 🧠 | Base et dimension : vrai ou faux | ★ | 4 | §3 | C, E | manuel | — |
| M12a.Q5 | 🧠 | Le rang d'une matrice, d'une transposée, d'un produit | ★ | 4 | §4 | C, E | manuel | — |
| M12a.Q6 | 🧠 | Linéaire, affine, ou ni l'un ni l'autre ? | ★ | 4 | §5 §8 | C, E | manuel | — |
| M12a.Q7 | 🧠 | Noyau et image : qui vit où ? | ★ | 4 | §6 | C, E | manuel | — |
| M12a.Q8 | 🧠 | Changer de base : ce qui change et ce qui reste | ★ | 4 | §7 | C | manuel | — |
| M12a.R1 | 🔁 | Le pivot de Gauss et la forme échelonnée réduite (M09a) | ★ | 5 | §2 | C, E | manuel | — |
| M12a.R2 | 🔁 | Produit matriciel et formes (M09a) | ★ | 5 | §5 | C, E | manuel | — |
| M12a.R3 | 🔁 | Combinaisons linéaires et produit scalaire dans ℝⁿ (M07) | ★ | 5 | §2 | C | manuel | — |
| M12a.1 | ✏️ | Reconnaître des sous-espaces de ℝ³ et de l'espace des polynômes | ★ | 15 | §1 | C, E | wbm | — |
| M12a.2 | ✏️ | Écrire un vecteur comme combinaison linéaire : un système à résoudre | ★ | 15 | §2 | C, E | wbm | — |
| M12a.3 | ✏️ | L'indépendance de trois vecteurs de ℝ³ par le pivot de Gauss | ★ | 15 | §2 | C, E | wbm | — |
| M12a.4 | ✏️ | Extraire une base d'une famille génératrice, compléter une famille libre | ★★ | 20 | §3 | C, E | wbm | — |
| M12a.5 | ✏️ | Les coordonnées d'un vecteur dans une base qui n'est pas la base canonique | ★ | 15 | §3 | C, E | wbm | — |
| M12a.6 | ✏️ | Le rang par les colonnes et par les lignes, celui d'un produit, et celui d'un tableau centré | ★★ | 20 | §4 | C, E | wbm | — |
| M12a.7 | ✏️ | La matrice d'une application linéaire : les images des vecteurs de base | ★ | 15 | §5 | C, E | wbm | — |
| M12a.8 | ✏️ | Composer deux applications du plan, c'est multiplier leurs matrices | ★ | 15 | §5 | C | wbm | — |
| M12a.9 | ✏️ | Noyau et image d'une matrice 3 × 4, et le théorème du rang | ★★ | 25 | §6 | C, E | wbm | — |
| M12a.10 | ✏️ | Toutes les solutions de A x = b : une solution particulière plus le noyau | ★★ | 20 | §6 | C, E | wbm | — |
| M12a.11 | ✏️ | Une base adaptée qui rend diagonale la matrice d'une application : S⁻¹AS | ★★ | 20 | §7 | C, E | wbm | — |
| M12a.12 | ✏️ | Une application affine du plan : partie linéaire, translation, inverse | ★★ | 20 | §8 | C, E | wbm | — |
| M12a.13 | ✏️ | La dérivation sur les polynômes de degré au plus 3 : matrice, noyau, image | ★★ | 20 | §3 §5 §6 | C | wbm | — |
| M12a.14 | ∂ | L'intersection de deux sous-espaces en est un ; la réunion, presque jamais | ★ | 15 | §1 | C, E | manuel | — |
| M12a.15 | ∂ | Les coordonnées dans une base sont uniques | ★★ | 20 | §3 | C | manuel | — |
| M12a.16 | ∂ | Le noyau est un sous-espace, et une application linéaire est injective si et seulement si son noyau est {0} | ★★ | 20 | §6 | C, E | manuel | — |
| M12a.17 | ∂ | Le théorème du rang : dim ker + rang = nombre de colonnes | ★★★ | 25 | §6 | C | manuel | — |
| M12a.18 | ∂ | rang(AB) ≤ min(rang A, rang B) | ★★ | 20 | §4 | C | manuel | — |
| M12a.19 | ∂ | L'inverse d'une application affine bijective est affine | ★★ | 20 | §8 | C | manuel | — |
| M12a.20 | 🔗 | Pont : une feature somme de deux autres rend XᵀX singulière, et le noyau dit laquelle | ★ | 15 | §4 §6 | C, E | wbm | — |
| M12a.21 | 🔗 | Pont : projeter sur un plan puis revenir, ce que la transformation inverse ne peut pas rendre | ★★ | 15 | §6 §8 | C | wbm | — |
| M12a.22 | 📖 | MML §2.4 et §2.5 : espaces vectoriels, sous-espaces et indépendance, en anglais | ★★ | 30 | §1 §2 | C | manuel | — |
| M12a.23 | 📖 | MML §2.6 à §2.8 : base, rang, applications linéaires, changement de base, espaces affines | ★★ | 45 | §3 §4 §5 §6 §7 §8 | C | manuel | — |
| M12a.24 | 🧮 | Fermi : les paramètres d'une application linéaire, puis affine, d'images 32 × 32 en couleurs vers 100 classes | ★ | 10 | §5 §8 | C | manuel | — |
| M12a.25 | 🗣️ | Expliquer la dimension et le rang sans une seule formule | ★ | 10 | §3 §4 | C, E | manuel | — |
| M12a.E1 | 💼 | « Que veut dire qu'une matrice est de rang plein, et pourquoi s'en soucier ? » | ★ | 10 | §4 §6 | C | manuel | — |
| M12a.E2 | 💼 | « Qu'est-ce que le noyau d'une matrice, et où le croise-t-on en ML ? » | ★ | 10 | §6 | C | manuel | — |
| M12a.26 | 🔨 | Tester l'indépendance et extraire une base de l'espace des colonnes · `is_independent, column_space_basis` | ★★ | 20 | §2 §3 §4 | C, E | pytest | — |
| M12a.27 | 🔨 | Une base du noyau, colonne libre par colonne libre · `null_space_basis` | ★★ | 25 | §6 | C, E | pytest | M12a.26 |
| M12a.28 | 🔨 | Coordonnées dans une base et changement de base · `coordinates, change_of_basis` | ★ | 20 | §3 §7 | C | pytest | M12a.26 |
| M12a.29 | 📦 | `sympy.Matrix.nullspace`, `columnspace` et `rank` contre tes fonctions | ★ | 15 | §4 §6 | C, E | wbm | — |
| M12a.30 | 🔮 | Prédire le rang : matrices aléatoires, produits, colonnes répétées | ★ | 10 | §4 | C, E | wbm | — |
| M12a.31 | 🔬 | Le rang numérique : une colonne presque redondante et le choix de la tolérance | ★★ | 20 | §4 | C | wbm | — |
| M12a.32 | 🎨 | Une application linéaire du plan : l'image du carré unité, et ce qu'elle écrase quand son noyau n'est pas nul | ★ | 20 | §5 §6 | C, E | manuel | — |
| M12a.33 | 🐛 | Chasse à l'erreur : une « base » liée, un noyau faux, S⁻¹AS écrit à l'envers | ★ | 15 | §2 §6 §7 | C | wbm | — |
| M12a.34 | 🛠️ | Un test de propriété : A fois une base du noyau donne 0, et le théorème du rang sur des matrices aléatoires | ★ | 15 | §6 | C | manuel | — |
| M12a.35 | 🏆 | Défi : retrouver les relations linéaires exactes cachées entre les colonnes d'un tableau, sans en inventer | ★★★ | 30 | §6 | C | wbm | — |

*Notes* : Frontières : 15.3 (ramener une droite ajustée dans l'espace d'origine par la réciproque d'un min-max), et les ∂ 12.6 (moyenne nulle et variance 1 des z-scores, invariance par x′ = ax + b) et 12.8 de workbookIA. M12a enseigne les applications affines et leur réciproque sur des transformations du plan, sans min-max, z-score ni droite ajustée. Évités (règle de partage) : les exemples et nombres de la fiche de workbookIA 12 (la météo en one-hot et `drop="first"`, l'ordinal faible, moyen, fort, la colonne 2, 4, 9, les températures et comptages de voitures de 12.4, les étendues de 12.3, le tableau de 12.5, les îles et les sexes des manchots) ; la colinéarité d'un one-hot avec la constante s'illustre ailleurs que sur ces catégories. M12a.6 montre que le rang d'un tableau centré est au plus n − 1 (1ᵀX_c = 0), ce dont la fiche de workbookIA 12 se sert pour compter les composantes d'une ACP. `linmaps` écrit les briques (indépendance, bases de l'espace des colonnes et du noyau comme SymPy, coordonnées, S⁻¹AS) ; NumPy permis, pas `matrix_rank`, `svd`, `qr`, `lstsq`, `pinv`, `inv` ni SymPy. La fiche énonce que la composée de deux applications affines est affine (le ∂ 17.3.1 de workbookIA la démontre, avec sa matrice et son vecteur) : M12a.19 ne démontre que l'inverse. Le Fermi M12a.24 évite les images 28 × 28 vers dix scores (7 850, réponse de workbookIA 13.9). M12a.11 annonce les vecteurs propres de M12c sans les nommer. Parcours essentiel : le théorème du rang et rang(AB) démontrés hors parcours. Deux sessions de génération : §1 à §4, puis §5 à §8.

<a id="m12b"></a>
## M12b · Orthogonalité et projections

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12b_orthogonalite/` · **MML** §3.2.2, §3.2.3, §3.5, §3.6, §3.7, §3.8, §9.4 · **sessions de génération** 1

Les produits scalaires généraux, l'orthogonalité, les bases orthonormées et les matrices orthogonales, le procédé de Gram-Schmidt, le complément orthogonal, la projection orthogonale sur un sous-espace, les moindres carrés revus comme une projection, la décomposition QR, et le produit scalaire de fonctions.

**Temps** : 15,2 h en parcours complet, 9,5 h en parcours essentiel (lecture 180 min, 24 flashcards).

**Objectifs**

- Reconnaître un produit scalaire défini par une matrice symétrique, et calculer normes et angles avec.
- Calculer dans une base orthonormée, et reconnaître une matrice orthogonale.
- Orthonormaliser une famille par Gram-Schmidt.
- Calculer un complément orthogonal et une projection orthogonale, et démontrer que le projeté est le point le plus proche.
- Résoudre des moindres carrés par une projection, puis par la décomposition QR.
- Calculer un produit scalaire de fonctions et orthogonaliser des polynômes.

**Sections de la fiche**

- §1 Produits scalaires généraux
- §2 Orthogonalité, bases orthonormées et matrices orthogonales
- §3 Le procédé de Gram-Schmidt
- §4 Le complément orthogonal
- §5 La projection orthogonale sur un sous-espace
- §6 Les moindres carrés vus comme une projection
- §7 La décomposition QR
- §8 Le produit scalaire de fonctions

**Notions enseignées** : produits scalaires généraux, matrices symétriques définies positives (en dimension 2) · bases orthonormées · matrices orthogonales · procédé de Gram-Schmidt · complément orthogonal · projection orthogonale · moindres carrés comme projection · décomposition QR · produit scalaire de fonctions

**Prérequis** : base, dimension, rang, noyau et image (M12a) · équations normales, matrice chapeau (M09b) · produit scalaire, normes, projection sur une droite, Cauchy-Schwarz (M07) · intégrales (M02a)

**mymath** : `orthogonal.py` (signatures figées) : `gram_schmidt`, `project`, `qr`, `least_squares_qr`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale · 12.7 ✏️ PCA à la main en 2D : covariance, axe principal, projection

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M12b.Q1 | 🧠 | Produit scalaire ou pas ? Symétrie et positivité | ★ | 4 | §1 | C, E | manuel | — |
| M12b.Q2 | 🧠 | Orthogonale, orthonormée, matrice orthogonale | ★ | 4 | §2 | C, E | manuel | — |
| M12b.Q3 | 🧠 | Gram-Schmidt : ce que chaque étape retire | ★ | 4 | §3 | C, E | manuel | — |
| M12b.Q4 | 🧠 | Le complément orthogonal : vrai ou faux | ★ | 4 | §4 | C, E | manuel | — |
| M12b.Q5 | 🧠 | Une matrice de projection : sur quoi, et quelles propriétés ? | ★ | 4 | §5 | C, E | manuel | — |
| M12b.Q6 | 🧠 | Moindres carrés et projection | ★ | 4 | §6 | C, E | manuel | — |
| M12b.Q7 | 🧠 | QR : formes et propriétés | ★ | 4 | §7 | C | manuel | — |
| M12b.Q8 | 🧠 | Des fonctions orthogonales | ★ | 4 | §8 | C | manuel | — |
| M12b.R1 | 🔁 | La projection sur une droite (M07) | ★ | 5 | §5 | C, E | manuel | — |
| M12b.R2 | 🔁 | Les équations normales et la matrice chapeau (M09b) | ★ | 5 | §6 | C, E | manuel | — |
| M12b.R3 | 🔁 | Base, rang et noyau (M12a) | ★ | 5 | §4 | C, E | manuel | — |
| M12b.1 | ✏️ | Un produit scalaire défini par une matrice 2 × 2 : normes, angles, orthogonalité | ★ | 15 | §1 | C, E | wbm | — |
| M12b.2 | ✏️ | Les coordonnées dans une base orthonormée : des produits scalaires au lieu d'un système | ★ | 15 | §2 | C, E | wbm | — |
| M12b.3 | ✏️ | Une matrice orthogonale 3 × 3 conserve normes et angles | ★ | 15 | §2 | C, E | wbm | — |
| M12b.4 | ✏️ | Gram-Schmidt sur trois vecteurs de ℝ³ | ★★ | 20 | §3 | C, E | wbm | — |
| M12b.5 | ✏️ | Gram-Schmidt pour un produit scalaire qui n'est pas l'usuel | ★★ | 20 | §1 §3 | C | wbm | — |
| M12b.6 | ✏️ | Une base du complément orthogonal d'un plan de ℝ⁴ | ★★ | 20 | §4 | C, E | wbm | — |
| M12b.7 | ✏️ | Projeter sur un plan de ℝ³ : avec une base quelconque, puis orthonormée | ★★ | 20 | §5 | C, E | wbm | — |
| M12b.8 | ✏️ | La matrice de projection : P² = P, Pᵀ = P, trace et rang | ★★ | 15 | §5 | C | wbm | — |
| M12b.9 | ✏️ | La distance d'un point à un sous-espace, et le résidu orthogonal | ★ | 15 | §5 §6 | C, E | wbm | — |
| M12b.10 | ✏️ | Des moindres carrés comme une projection : y, son projeté et le résidu | ★★ | 20 | §6 | C, E | wbm | — |
| M12b.11 | ✏️ | La décomposition QR d'une matrice 3 × 2, puis les moindres carrés par R w = Qᵀy | ★★ | 25 | §7 | C | wbm | — |
| M12b.12 | ✏️ | Le produit scalaire de fonctions sur [−1 ; 1] : orthogonaliser 1, x et x² | ★★ | 25 | §8 | C | wbm | — |
| M12b.13 | ∂ | L'inégalité de Cauchy-Schwarz pour tout produit scalaire | ★★ | 20 | §1 | C | manuel | — |
| M12b.14 | ∂ | Une famille orthogonale de vecteurs non nuls est libre | ★ | 15 | §2 | C, E | manuel | — |
| M12b.15 | ∂ | Gram-Schmidt donne une base orthonormée du même sous-espace | ★★ | 20 | §3 | C | manuel | — |
| M12b.16 | ∂ | L'orthogonal de l'image de A est le noyau de Aᵀ | ★★ | 20 | §4 | C, E | manuel | — |
| M12b.17 | ∂ | Le projeté orthogonal est le point le plus proche (Pythagore) | ★★ | 20 | §5 §6 | C, E | manuel | — |
| M12b.18 | 🔗 | Pont : retirer d'une feature ce qu'explique une autre, une projection puis un résidu | ★ | 15 | §3 §5 | C, E | wbm | — |
| M12b.19 | 🔗 | Pont : projeter sur k directions orthonormées, reconstruire, et l'erreur par Pythagore | ★★ | 15 | §5 | C, E | wbm | — |
| M12b.20 | 📖 | MML §3.2, §3.5 à §3.7 : produits scalaires, orthogonalité, fonctions, en anglais | ★★ | 30 | §1 §2 §4 §8 | C | manuel | — |
| M12b.21 | 📖 | MML §3.8 et §9.4 : projections, Gram-Schmidt et moindres carrés | ★★ | 30 | §3 §5 §6 | C | manuel | — |
| M12b.22 | 🧮 | Fermi : le coût de Gram-Schmidt sur une matrice 100 000 × 50 | ★ | 10 | §3 §7 | C | manuel | — |
| M12b.23 | 🗣️ | Expliquer pourquoi le projeté est le point le plus proche | ★ | 10 | §5 | C, E | manuel | — |
| M12b.E1 | 💼 | « Pourquoi résoudre des moindres carrés par QR plutôt que par les équations normales ? » | ★ | 10 | §6 §7 | C | manuel | — |
| M12b.E2 | 💼 | « Qu'est-ce qu'une matrice orthogonale, et pourquoi est-elle agréable en calcul numérique ? » | ★ | 10 | §2 | C | manuel | — |
| M12b.24 | 🔨 | Gram-Schmidt, classique et modifié · `gram_schmidt` | ★★ | 25 | §3 | C, E | pytest | — |
| M12b.25 | 🔨 | La projection orthogonale sur un sous-espace · `project` | ★ | 15 | §5 | C, E | pytest | — |
| M12b.26 | 🔨 | La décomposition QR et les moindres carrés par QR · `qr, least_squares_qr` | ★★ | 25 | §7 | C | pytest | M12b.24 |
| M12b.27 | 📦 | `np.linalg.qr` et `lstsq` contre ta projection et ta QR : les signes de Q et de R | ★ | 15 | §7 | C | wbm | — |
| M12b.28 | 🔮 | Prédire : Gram-Schmidt classique sur des vecteurs presque colinéaires, QᵀQ vaut-il encore I ? | ★ | 10 | §3 | C, E | wbm | — |
| M12b.29 | 🔬 | Gram-Schmidt classique contre modifié : l'orthogonalité perdue quand les colonnes sont presque dépendantes | ★★ | 20 | §3 §7 | C | wbm | — |
| M12b.30 | 🎨 | Projeter un nuage de ℝ³ sur un plan : les résidus orthogonaux en image | ★ | 20 | §5 | C, E | manuel | — |
| M12b.31 | 🐛 | Chasse à l'erreur : une normalisation oubliée, QQᵀ sur une base non orthonormée, R w = Qᵀy résolu dans le mauvais sens | ★ | 15 | §3 §5 §7 | C | wbm | — |
| M12b.32 | 🛠️ | Un test de propriétés pour la projection : idempotente, symétrique, résidu orthogonal | ★ | 15 | §5 | C | manuel | — |
| M12b.33 | 🏆 | Défi : des colonnes presque dépendantes, des moindres carrés à 1e−8 près de `lstsq` par l'orthogonalisation de [X | y] | ★★★ | 30 | §6 §7 | C | wbm | — |

*Notes* : Frontières : 12.7 (l'erreur de reconstruction d'une ACP 2D, égale à la coordonnée orthogonale), et les ∂ 12.6 et 12.8 de workbookIA. Évités : la projection de la fiche de workbookIA 12 (u = (0,6 ; 0,8), x = (2, 3), t = 3,6, distance 0,2, variance 10,72 = uᵀΣu) et ses coordonnées projetées ; la propriété « l'erreur de reconstruction est la coordonnée orthogonale » de 12.7 n'est pas posée sur un nuage 2D : M12b.19 la démontre pour k directions orthonormées quelconques, par Pythagore. Les moindres carrés vus comme une projection (MML §9.4) reprennent M09b en dimension p, sans ses exemples ni ceux de workbookIA 9. Parcours essentiel : QR et le produit scalaire de fonctions hors parcours (workbookIA 12 n'en a pas besoin). `orthogonal` écrit Gram-Schmidt (classique et modifié), la projection (par une base orthonormée, QQᵀv, pas par les équations normales de M09b), QR et les moindres carrés par QR ; NumPy permis, pas `np.linalg.qr`, `lstsq`, `pinv` ni `inv`. Le conditionnement n'est défini qu'en M12d : M12b parle de colonnes presque dépendantes, et la réponse modèle de M12b.E1 cite Householder (LAPACK) et les arrondis que XᵀX amplifie (M09b.32), sans κ. Le 🏆 M12b.33 attend l'orthogonalisation de la matrice augmentée [X | y] (Björck), sur des données bruitées et des colonnes presque dépendantes (à calibrer à la génération, entre les seuils où les équations normales échouent et où `gram_schmidt` refuse) : `least_squares_qr` (Gram-Schmidt modifié puis Qᵀy) n'y suffit pas.

<a id="m12c"></a>
## M12c · Valeurs propres et matrices symétriques

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12c_valeurs_propres/` · **MML** §4.1, §4.2, §4.3, §4.4 · **sessions de génération** 2

Le déterminant et la trace, les valeurs et vecteurs propres, la méthode de la puissance, la diagonalisation et le théorème spectral, le quotient de Rayleigh, les matrices définies positives, les formes quadratiques et la décomposition de Cholesky ; la matrice de covariance vue comme une matrice symétrique positive, le blanchiment et la racine carrée d'une matrice.

**Temps** : 16,8 h en parcours complet, 11,5 h en parcours essentiel (lecture 210 min, 26 flashcards).

**Objectifs**

- Calculer un déterminant, l'interpréter comme un volume orienté, et l'utiliser pour l'inversibilité.
- Calculer les valeurs et vecteurs propres d'une petite matrice, et diagonaliser.
- Appliquer le théorème spectral et le quotient de Rayleigh à une matrice symétrique.
- Approcher la plus grande valeur propre par la méthode de la puissance.
- Reconnaître une matrice définie positive et calculer sa décomposition de Cholesky.
- Transformer une matrice de covariance, et blanchir des données.

**Sections de la fiche**

- §1 Le déterminant : volume orienté et inversibilité
- §2 La trace
- §3 Valeurs propres et vecteurs propres
- §4 La diagonalisation
- §5 La méthode de la puissance
- §6 Matrices symétriques : le théorème spectral et le quotient de Rayleigh
- §7 Matrices définies positives, formes quadratiques et Cholesky
- §8 La matrice de covariance, le blanchiment et la racine carrée d'une matrice

**Notions enseignées** : déterminant · trace · polynôme caractéristique · valeurs et vecteurs propres · le strict minimum sur les nombres complexes (i, conjugué, module, racines conjuguées d'un trinôme réel, vecteurs de ℂⁿ et z̄ᵀz) · méthode de la puissance · diagonalisation · théorème spectral · quotient de Rayleigh · matrices définies positives · décomposition de Cholesky · formes quadratiques · hessienne d'une fonction de n variables (définition ; Taylor d'ordre 2 et son étude : M19) · convexité à plusieurs variables par la hessienne semi-définie positive (la définition par les cordes : M10) · matrice de Gram XᵀX (semi-définie positive) · matrice de covariance symétrique positive · covariance d'une transformation affine · blanchiment (whitening) · racine carrée d'une matrice symétrique positive

**Prérequis** : base, rang, noyau, changement de base (M12a) · bases orthonormées, matrices orthogonales (M12b) · matrice de covariance empirique (M02c) · fonctions convexes de plusieurs variables (M10) · hessienne d'une fonction de deux variables (M05b) · racines d'un polynôme (R3)

**mymath** : `eigen.py` (signatures figées) : `det`, `power_iteration`, `rayleigh_quotient`, `cholesky`, `is_positive_definite`, `sqrtm_psd`, `whitening_matrix`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale · 12.7 ✏️ PCA à la main en 2D : covariance, axe principal, projection · 12.22 🎨 Projeter un nuage 2D : axe horizontal contre axe de variance maximale · 12.29 🔬 Échelle des features et descente de gradient · 12.R3 🔁 Descente de gradient dans une vallée très allongée

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M12c.Q1 | 🧠 | Ce que mesure un déterminant | ★ | 4 | §1 | C, E | manuel | — |
| M12c.Q2 | 🧠 | Les propriétés du déterminant et de la trace : vrai ou faux | ★ | 4 | §1 §2 | C, E | manuel | — |
| M12c.Q3 | 🧠 | Reconnaître un vecteur propre | ★ | 4 | §3 | C, E | manuel | — |
| M12c.Q4 | 🧠 | Diagonalisable ou pas ? | ★ | 4 | §4 | C, E | manuel | — |
| M12c.Q5 | 🧠 | Ce que garantit le théorème spectral | ★ | 4 | §6 | C, E | manuel | — |
| M12c.Q6 | 🧠 | Définie positive, semi-définie positive ou indéfinie ? | ★ | 4 | §7 | C, E | manuel | — |
| M12c.Q7 | 🧠 | Cholesky, racine carrée, blanchiment : qui est quoi ? | ★ | 4 | §7 §8 | C | manuel | — |
| M12c.Q8 | 🧠 | Trace, déterminant et valeurs propres | ★ | 4 | §2 §3 | C, E | manuel | — |
| M12c.R1 | 🔁 | Le rang et le noyau (M12a) | ★ | 5 | §3 | C, E | manuel | — |
| M12c.R2 | 🔁 | Bases orthonormées et matrices orthogonales (M12b) | ★ | 5 | §6 | C, E | manuel | — |
| M12c.R3 | 🔁 | La matrice de covariance empirique (M02c) | ★ | 5 | §8 | C, E | manuel | — |
| M12c.1 | ✏️ | Déterminants 2 × 2 et 3 × 3 : aire, volume et signe | ★ | 15 | §1 | C, E | wbm | — |
| M12c.2 | ✏️ | Le déterminant d'une matrice 4 × 4 par élimination | ★★ | 20 | §1 | C | wbm | — |
| M12c.3 | ✏️ | Les valeurs et vecteurs propres d'une matrice 2 × 2 | ★ | 15 | §3 | C, E | wbm | — |
| M12c.4 | ✏️ | Une matrice 3 × 3 triangulaire, puis une avec une valeur propre double | ★★ | 20 | §3 §4 | C, E | wbm | — |
| M12c.5 | ✏️ | Diagonaliser, puis calculer une puissance dixième | ★★ | 20 | §4 | C, E | wbm | — |
| M12c.6 | ✏️ | Une matrice non diagonalisable, et une rotation sans valeur propre réelle | ★★ | 15 | §3 §4 | C | wbm | — |
| M12c.7 | ✏️ | Le théorème spectral sur une matrice symétrique 2 × 2 : Q, Λ et QΛQᵀ | ★ | 15 | §6 | C, E | wbm | — |
| M12c.8 | ✏️ | Le quotient de Rayleigh : le maximum et le minimum de xᵀAx sur le cercle unité | ★★ | 20 | §6 | C, E | wbm | — |
| M12c.9 | ✏️ | Trois itérations de la méthode de la puissance à la main | ★ | 15 | §5 | C | wbm | — |
| M12c.10 | ✏️ | Définie positive ? Par les valeurs propres, les mineurs et la forme quadratique ; une hessienne qui prouve la convexité | ★★ | 20 | §7 | C, E | wbm | — |
| M12c.11 | ✏️ | La décomposition de Cholesky d'une matrice 3 × 3 | ★★ | 20 | §7 | C, E | wbm | — |
| M12c.12 | ✏️ | Une forme quadratique réduite à une somme de carrés, et ses lignes de niveau | ★★ | 20 | §6 §7 | C | wbm | — |
| M12c.13 | ✏️ | La covariance d'un vecteur transformé, AΣAᵀ, et le blanchiment d'une covariance 2 × 2 | ★★ | 20 | §8 | C, E | wbm | — |
| M12c.14 | ∂ | det A ≠ 0 si et seulement si A est inversible (det AB = det A det B admis) | ★★ | 20 | §1 | C | manuel | — |
| M12c.15 | ∂ | Une matrice symétrique réelle : valeurs propres réelles, vecteurs propres de valeurs distinctes orthogonaux | ★★ | 20 | §6 | C, E | manuel | — |
| M12c.16 | ∂ | La somme des valeurs propres est la trace, leur produit le déterminant | ★★ | 20 | §2 §3 | C | manuel | — |
| M12c.17 | ∂ | Une matrice de covariance, et toute matrice de Gram XᵀX, est symétrique semi-définie positive | ★ | 15 | §8 | C, E | manuel | — |
| M12c.18 | ∂ | Le quotient de Rayleigh d'une matrice symétrique est entre λ_min et λ_max | ★★ | 20 | §6 | C | manuel | — |
| M12c.19 | ∂ | ½ xᵀAx − bᵀx, avec A définie positive, a un unique minimum, en A⁻¹b | ★★ | 20 | §7 | C, E | manuel | — |
| M12c.20 | 🔗 | Pont : la variance d'une somme pondérée de trois features, wᵀΣw, et pourquoi Σ doit être semi-définie positive | ★ | 15 | §8 | C, E | wbm | — |
| M12c.21 | 🔗 | Pont : après un blanchiment, la covariance est l'identité | ★★ | 15 | §8 | C | wbm | — |
| M12c.22 | 📖 | MML §4.1 et §4.2 : déterminant, trace, valeurs propres, en anglais | ★★ | 30 | §1 §2 §3 | C | manuel | — |
| M12c.23 | 📖 | MML §4.3 et §4.4 : Cholesky, diagonalisation et décomposition spectrale | ★★ | 30 | §4 §6 §7 | C | manuel | — |
| M12c.24 | 🧮 | Fermi : un déterminant 20 × 20 par cofacteurs ou par élimination, combien d'opérations ? | ★ | 10 | §1 | C | manuel | — |
| M12c.25 | 🗣️ | Expliquer un vecteur propre avec une image | ★ | 10 | §3 | C, E | manuel | — |
| M12c.E1 | 💼 | « Que représentent les valeurs propres d'une matrice de covariance ? » | ★ | 10 | §6 §8 | C | manuel | — |
| M12c.E2 | 💼 | « Comment savoir qu'une matrice est définie positive, et pourquoi est-ce important en optimisation ? » | ★ | 10 | §7 | C | manuel | — |
| M12c.26 | 🔨 | Le déterminant par élimination · `det` | ★ | 20 | §1 | C, E | pytest | — |
| M12c.27 | 🔨 | La méthode de la puissance et le quotient de Rayleigh · `power_iteration, rayleigh_quotient` | ★★ | 25 | §5 §6 | C, E | pytest | — |
| M12c.28 | 🔨 | La décomposition de Cholesky et le test « définie positive » · `cholesky, is_positive_definite` | ★★ | 25 | §7 | C, E | pytest | — |
| M12c.29 | 🔨 | La racine carrée d'une matrice symétrique positive et la matrice de blanchiment · `sqrtm_psd, whitening_matrix` | ★★ | 25 | §6 §8 | C, E | pytest | M12c.28 |
| M12c.30 | 📦 | `np.linalg.eigh`, `det`, `cholesky` et `scipy.linalg.sqrtm` contre tes fonctions | ★ | 15 | §1 §6 §7 | C, E | wbm | — |
| M12c.31 | 🔮 | Prédire : la méthode de la puissance quand les deux plus grandes valeurs propres sont proches | ★ | 10 | §5 | C, E | wbm | — |
| M12c.32 | 🔬 | La vitesse de la méthode de la puissance et le rapport |λ₂ / λ₁| | ★★ | 20 | §5 | C | wbm | — |
| M12c.33 | 🎨 | Les lignes de niveau de xᵀAx : définie positive, semi-définie positive, indéfinie | ★ | 20 | §6 §7 | C, E | manuel | — |
| M12c.34 | 🐛 | Chasse à l'erreur : det(A + B) = det A + det B, un vecteur propre nul, Cholesky d'une matrice non symétrique | ★ | 15 | §1 §3 §7 | C | wbm | — |
| M12c.35 | 🛠️ | Vérifier avec SymPy : polynôme caractéristique, valeurs propres exactes, diagonalisation | ★ | 15 | §3 §4 | C | manuel | — |
| M12c.36 | 🏆 | Défi : les trois plus grandes valeurs propres d'une matrice symétrique semi-définie positive 300 × 300, par la puissance avec déflation, à 1e−6 près | ★★★ | 30 | §5 §6 | C | wbm | — |

*Notes* : Frontières : 12.7 (ACP 2D à la main), 12.22 (« l'axe principal d'un nuage standardisé en 2D est à 45° et garde (1 + r)/2 »), 12.29 et 12.R3 (courbures de la MSE, pas critique 2/λ_max de la descente de gradient), et les ∂ 12.6 et 12.8. M12c énonce le théorème spectral en dimension n (démontré quand les valeurs propres sont distinctes), démontre le quotient de Rayleigh par QΛQᵀ (M12c.8 et M12c.18, sans u = (cos t, sin t) ni l'enchaînement diagonale 2D, 3D puis rotation de 12.8), V(aᵀX) = aᵀΣa pour un vecteur aléatoire et la positivité d'une matrice de Gram (M12c.17), et la trace par tr(QᵀAQ) = tr(A). La diagonalisation (§4) vient avant la méthode de la puissance (§5), dont l'analyse suppose une base de vecteurs propres. Évités : les matrices [[1, r], [r, 1]] et [[a, b], [b, a]] (12.22), [[3, 1], [1, 3]] et le blanchiment « 3 devient 1,5 et 2,12 » (fiche de workbookIA 12), la covariance [[4, 5], [5, 7]] des points (0, 1), (2, 2), (4, 6), la quadratique x² + 100y² (12.R3). Conventions : la fiche montre les deux normalisations de Σ (1/n pour le `StandardScaler` et le `covariance_matrix` de `mylearn`, 1/(n − 1) pour l'ACP de workbookIA 12) et le facteur (n − 1)/n ; elle décrit le blanchiment de l'ACP (Λ^(−1/2)Qᵀ, celui de scikit-learn et de la PCA de `mylearn` en 12.27) et le blanchiment ZCA (Σ^(−1/2)), et M12c.13 calcule les deux en disant la convention ; `whitening_matrix` n'écrit que ZCA et Cholesky. `eigen` : NumPy permis, `np.linalg.eigh` seulement dans `sqrtm_psd` et `whitening_matrix`. Deux sessions de génération : §1 à §5, puis §6 à §8. Audit (session 55) : la fiche enseigne le strict minimum sur les nombres complexes (§3 ; M12c.6, M12c.15.3 et M12c.16.2 s'en servent ; M19 le rappelle) et définit la hessienne d'une fonction de n variables (§7).

<a id="m12d"></a>
## M12d · SVD et analyse en composantes principales

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12d_svd_acp/` · **MML** §4.5, §4.6, §4.7, §10.1, §10.2, §10.3, §10.4, §10.5, §10.6 · **sessions de génération** 2

La décomposition en valeurs singulières et son interprétation géométrique, l'approximation de rang faible, la pseudo-inverse et le conditionnement ; puis les axes principaux par le quotient de Rayleigh, l'ACP (centrer, projeter, reconstruire), la variance expliquée, l'erreur de reconstruction, l'ACP en grande dimension, et la place de t-SNE et d'UMAP.

**Temps** : 18,0 h en parcours complet, 11,3 h en parcours essentiel (lecture 210 min, 26 flashcards).

**Objectifs**

- Calculer la SVD d'une petite matrice et l'interpréter comme rotation, étirement, rotation.
- Calculer une approximation de rang faible et son erreur (Eckart-Young).
- Calculer une pseudo-inverse et un conditionnement, et dire ce qu'ils signifient.
- Calculer les axes principaux d'un nuage, les scores, une reconstruction et la variance expliquée.
- Relier l'erreur de reconstruction aux valeurs propres oubliées.
- Situer l'ACP par rapport à t-SNE et UMAP.

**Sections de la fiche**

- §1 La décomposition en valeurs singulières
- §2 Rotation, étirement, rotation : la géométrie de la SVD
- §3 L'approximation de rang faible
- §4 La pseudo-inverse et le conditionnement
- §5 Les axes principaux : maximiser la variance sur la sphère
- §6 L'ACP : centrer, projeter, reconstruire
- §7 Variance expliquée, erreur de reconstruction, grande dimension
- §8 Au-delà du linéaire : t-SNE et UMAP (aperçu)

**Notions enseignées** : décomposition en valeurs singulières · interprétation géométrique · normes de Frobenius et spectrale d'une matrice · approximation de rang faible (Eckart-Young) · pseudo-inverse · conditionnement · axes principaux : maximiser uᵀCu sur la sphère (quotient de Rayleigh) · ACP : projection · variance expliquée · ACP en grande dimension · erreur de reconstruction d'une projection · t-SNE et UMAP : préserver des voisinages (aperçu) · erreur de reconstruction et détection d'anomalies

**Prérequis** : valeurs propres, théorème spectral, quotient de Rayleigh (M12c) · projection orthogonale, bases orthonormées (M12b) · rang, noyau, image (M12a) · moyenne, matrice de covariance, standardisation (M02c) · moindres carrés (M09b) · entropie, divergence KL (M06)

**mymath** : `svd_pca.py` (signatures figées) : `svd`, `low_rank_approximation`, `pinv`, `condition_number`, `principal_axes`, `explained_variance_ratio`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale · 12.7 ✏️ PCA à la main en 2D : covariance, axe principal, projection · 12.22 🎨 Projeter un nuage 2D : axe horizontal contre axe de variance maximale · 12.27 🔨 Coder la PCA (SVD, variance expliquée, whitening, reconstruction) · 12.29 🔬 Échelle des features et descente de gradient · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé)

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M12d.Q1 | 🧠 | La SVD : formes et propriétés | ★ | 4 | §1 | C, E | manuel | — |
| M12d.Q2 | 🧠 | Valeurs singulières et valeurs propres | ★ | 4 | §1 §2 | C, E | manuel | — |
| M12d.Q3 | 🧠 | Rang faible : ce qu'on garde, ce qu'on perd | ★ | 4 | §3 | C, E | manuel | — |
| M12d.Q4 | 🧠 | Pseudo-inverse et conditionnement | ★ | 4 | §4 | C, E | manuel | — |
| M12d.Q5 | 🧠 | Ce que maximise un axe principal | ★ | 4 | §5 | C, E | manuel | — |
| M12d.Q6 | 🧠 | Centrer et standardiser avant une ACP ? | ★ | 4 | §6 | C, E | manuel | — |
| M12d.Q7 | 🧠 | Variance expliquée et nombre de composantes | ★ | 4 | §7 | C, E | manuel | — |
| M12d.Q8 | 🧠 | ACP, t-SNE ou UMAP : qui garde quoi ? | ★ | 4 | §8 | C, E | manuel | — |
| M12d.R1 | 🔁 | Valeurs propres et théorème spectral (M12c) | ★ | 5 | §1 | C, E | manuel | — |
| M12d.R2 | 🔁 | La projection orthogonale (M12b) | ★ | 5 | §5 | C, E | manuel | — |
| M12d.R3 | 🔁 | Moyenne, covariance et standardisation (M02c) | ★ | 5 | §6 | C, E | manuel | — |
| M12d.1 | ✏️ | La SVD d'une matrice 2 × 2 à la main, par AᵀA | ★★ | 20 | §1 | C, E | wbm | — |
| M12d.2 | ✏️ | La SVD compacte d'une matrice 3 × 2 de rang 1 | ★★ | 15 | §1 | C | wbm | — |
| M12d.3 | ✏️ | Le cercle unité devient une ellipse : axes et demi-axes | ★ | 15 | §2 | C, E | wbm | — |
| M12d.4 | ✏️ | L'approximation de rang 1 d'une matrice 3 × 3 et son erreur | ★★ | 20 | §3 | C, E | wbm | — |
| M12d.5 | ✏️ | Compter les nombres stockés : une image en rang k | ★ | 10 | §3 | C | wbm | — |
| M12d.6 | ✏️ | La pseudo-inverse d'une matrice non inversible et la solution de norme minimale | ★★ | 20 | §4 | C, E | wbm | — |
| M12d.7 | ✏️ | Le conditionnement de trois matrices, et l'erreur relative sur une solution | ★★ | 15 | §4 | C, E | wbm | — |
| M12d.8 | ✏️ | Les axes principaux d'un nuage de ℝ³ : covariance, polynôme caractéristique, variances et axes | ★★ | 35 | §5 §6 | C, E | wbm | — |
| M12d.9 | ✏️ | Scores, reconstruction et erreur de reconstruction moyenne avec deux composantes sur trois | ★★ | 20 | §6 §7 | C, E | wbm | — |
| M12d.10 | ✏️ | La variance expliquée cumulée : combien de composantes pour 95 % ? | ★ | 15 | §7 | C, E | wbm | — |
| M12d.11 | ✏️ | L'ACP par la SVD de la matrice centrée : s² / (n − 1) donne les variances | ★★ | 20 | §1 §6 | C | wbm | — |
| M12d.12 | ✏️ | L'ACP quand n < p : passer par la petite matrice XXᵀ | ★★ | 20 | §7 | C | wbm | — |
| M12d.13 | ✏️ | Les probabilités de voisinage de t-SNE sur quatre points, et leur perplexité 2^H | ★ | 15 | §8 | C, E | wbm | — |
| M12d.14 | ∂ | Les valeurs singulières sont les racines des valeurs propres de AᵀA | ★★ | 20 | §1 | C, E | manuel | — |
| M12d.15 | ∂ | La plus grande valeur singulière est le plus grand étirement : ‖A x‖ ≤ s₁ ‖x‖ | ★★ | 20 | §2 | C | manuel | — |
| M12d.16 | ∂ | L'erreur de l'approximation de rang k vaut la somme des s² oubliés (Frobenius) | ★★★ | 25 | §3 | C | manuel | — |
| M12d.17 | ∂ | La pseudo-inverse donne la solution des moindres carrés de plus petite norme | ★★ | 20 | §4 | C | manuel | — |
| M12d.18 | ∂ | L'erreur de reconstruction moyenne est la somme des variances oubliées | ★★ | 20 | §7 | C, E | manuel | — |
| M12d.19 | ∂ | Les scores de deux composantes principales sont décorrélés | ★★ | 15 | §6 | C | manuel | — |
| M12d.20 | 🔗 | Pont : détecter une anomalie par son erreur de reconstruction | ★ | 15 | §7 | C, E | wbm | — |
| M12d.21 | 🔗 | Pont : un changement d'unités diagonal D change Σ en DΣD, et les axes principaux avec ; la standardisation non | ★★ | 15 | §6 | C | wbm | — |
| M12d.22 | 📖 | MML §4.5 à §4.7 : SVD, approximation de rang faible, phylogénie des matrices | ★★ | 45 | §1 §2 §3 §4 | C | manuel | — |
| M12d.23 | 📖 | MML §10.1 à §10.6 : l'ACP du livre (la dérivation par Lagrange de §10.2 se survole : M13b la relit) | ★★ | 50 | §5 §6 §7 | C | manuel | — |
| M12d.24 | 🧮 | Fermi : la mémoire et le temps d'une ACP sur un million de clients et 250 features | ★ | 10 | §6 §7 | C | manuel | — |
| M12d.25 | 🗣️ | Expliquer la SVD comme « rotation, étirement, rotation » | ★ | 10 | §2 | C, E | manuel | — |
| M12d.E1 | 💼 | « Comment choisissez-vous le nombre de composantes d'une ACP ? » | ★ | 10 | §7 | C | manuel | — |
| M12d.E2 | 💼 | « Que dit le conditionnement d'une matrice ? » | ★ | 10 | §4 | C | manuel | — |
| M12d.26 | 🔨 | La SVD par les valeurs propres de AᵀA · `svd` | ★★ | 40 | §1 | C, E | pytest | — |
| M12d.27 | 🔨 | Approximation de rang faible et conditionnement · `low_rank_approximation, condition_number` | ★ | 20 | §3 §4 | C, E | pytest | M12d.26 |
| M12d.28 | 🔨 | La pseudo-inverse · `pinv` | ★ | 15 | §4 | C | pytest | M12d.26 |
| M12d.29 | 🔨 | Les axes principaux d'une matrice de covariance, et la variance expliquée · `principal_axes, explained_variance_ratio` | ★★ | 25 | §5 §6 §7 | C, E | pytest | — |
| M12d.30 | 📦 | `np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA` contre tes fonctions : les signes | ★ | 15 | §1 §4 §6 | C, E | wbm | — |
| M12d.31 | 🔮 | Prédire l'allure des valeurs singulières d'une image, et le rang qui suffit | ★ | 10 | §3 | C, E | wbm | — |
| M12d.32 | 🔬 | Compresser une image du domaine public : l'erreur en fonction du rang | ★★ | 20 | §3 | C | wbm | — |
| M12d.33 | 🔬 | La SVD par AᵀA contre `np.linalg.svd` : ce qu'on perd quand κ est grand | ★★ | 20 | §1 §4 | C | wbm | — |
| M12d.34 | 🎨 | La SVD en images : Vᵀ, Σ puis U appliqués au cercle unité, étape par étape | ★ | 20 | §2 | C, E | manuel | — |
| M12d.35 | 🐛 | Chasse à l'erreur : une ACP sans centrer, n et n − 1 mélangés, des axes lus en lignes au lieu de colonnes | ★ | 15 | §6 | C | wbm | — |
| M12d.36 | 🛠️ | Un test : la reconstruction de rang plein redonne X, et l'erreur décroît avec k | ★ | 15 | §3 §7 | C | manuel | — |
| M12d.37 | 🏆 | Défi : compresser une image centrée en gardant 93,5 % de son énergie avec au plus 5 % des nombres | ★★★ | 30 | §3 | C | wbm | — |

*Notes* : Frontières : 12.7 et 12.22 (ACP 2D à la main, axe à 45° d'un nuage standardisé), 12.27 (la PCA de `mylearn` par SVD : centrage, signe, choix de k par un seuil, whitening, `inverse_transform`), 12.29 (conditionnement et pas de la descente de gradient), 25.8 (autoencodeur linéaire et ACP), et les ∂ 12.6 et 12.8 (variance d'une projection et axe de variance maximale). M12d passe par le quotient de Rayleigh de M12c en dimension n, et fait ses ACP à la main en dimension 3, par le polynôme caractéristique d'une covariance à structure par blocs (une valeur propre évidente), sans reprendre la suite de 12.7 : M12d.9 demande l'erreur de reconstruction moyenne (la somme des variances oubliées), pas la distance d'un point à sa reconstruction, et aucun blanchiment ; M12d.21 pose DΣD en général. `principal_axes` prend une matrice de covariance (pas les données) et `explained_variance_ratio` des valeurs propres, pour ne pas écrire la PCA de `mylearn` (ce sont des briques, avec la même convention de signe). M12d.13 calcule les probabilités de voisinage de t-SNE et leur perplexité 2^H (M06), sans MNIST ni perplexité 30. La SVD par AᵀA ne voit pas les valeurs singulières sous 1e−6 · s_max : les comparaisons à `np.linalg.cond` se font pour κ < 1e6. MML §10.2 dérive l'axe de variance maximale par Lagrange : cette dérivation se relit en M13b ; §10.7 (point de vue latent) se lit en M25b. Évités : les nombres MNIST de workbookIA 12 (86, 321, 35, 78, 59 composantes, 0,572, 0,911…), `load_digits`, les « 10 features, 3 directions et du bruit » de sa fiche, le passage des kilogrammes aux grammes, les points A(1, 1) à E(7, 3) de 12.7, et pour l'anomalie MNIST contre Fashion-MNIST, le seuil au 99ᵉ centile et la ROC-AUC (workbookIA 25). Le 🏆 M12d.37 est calibré (session 41) sur la photo CC0 de la tasse de café (`data/cards/tasse_cafe.md`), centrée : avec 5 % des nombres, la SVD globale garde 88,8 % de l'énergie, des tuiles de rang adapté 89,5 à 91,6 %, la seule moyenne de chaque rectangle de 4 × 5 pixels 93,3 %, l'ACP de ses carrés de 8 × 8 pixels 94,1 % : l'objectif est donc 93,5 % (97 % demandait 14 à 26 % des nombres). Convention de signe des axes comme scikit-learn et la PCA de `mylearn` (la coordonnée de plus grande valeur absolue est positive). `svd_pca` : NumPy et `np.linalg.eigh` permis, pas `np.linalg.svd`, `pinv`, `cond`, `lstsq` ni scikit-learn. Deux sessions de génération : §1 à §4 (SVD), puis §5 à §8 (ACP).

<a id="m13a"></a>
## M13a · Vraisemblance et régression logistique

**Partie** III · **prépare** workbookIA 13 · **dossier** `chapitres/m13a_vraisemblance_logistique/` · **MML** §8.3 · **sessions de génération** 2

Le maximum de vraisemblance (Bernoulli, catégorielle, gaussienne), la log-loss comme moins la log-vraisemblance, la sigmoïde et la fonction softplus, la régression logistique comme modèle probabiliste (et la sonde linéaire), Naïve Bayes comme modèle génératif, l'entropie, l'indice de Gini, le gain d'information et la réduction de variance des arbres.

**Temps** : 14,4 h en parcours complet, 10,6 h en parcours essentiel (lecture 180 min, 24 flashcards).

**Objectifs**

- Calculer et démontrer des estimateurs du maximum de vraisemblance (Bernoulli, catégorielle, gaussienne).
- Écrire la log-loss comme moins la log-vraisemblance, et la calculer.
- Calculer avec la sigmoïde et la softplus, et démontrer la convexité de la softplus.
- Lire un modèle logistique : probabilités, cote, frontière de décision.
- Calculer à la main un Naïve Bayes avec lissage, en log-probabilités.
- Calculer une entropie, un indice de Gini, un gain d'information et une réduction de variance.

**Sections de la fiche**

- §1 Le maximum de vraisemblance, revisité
- §2 La log-loss est moins la log-vraisemblance
- §3 La sigmoïde et la softplus
- §4 La régression logistique, un modèle probabiliste
- §5 Naïve Bayes, un modèle génératif
- §6 Impureté : entropie, indice de Gini et gain d'information
- §7 Arbres de régression : la réduction de variance

**Notions enseignées** : maximum de vraisemblance · log-vraisemblance · log-loss = moins la log-vraisemblance · régression logistique : le modèle · convexité de log-somme-exp et de log(1 + eᶻ) · Naïve Bayes : hypothèse d'indépendance · impureté d'une distribution : entropie, Gini · gain d'information (information mutuelle) · réduction de variance (arbres de régression) · linear probe

**Prérequis** : vraisemblance, MAP, lissage de Laplace, log-sum-exp (M04) · entropie, cross-entropy, information mutuelle, inégalité de Gibbs (M06) · sigmoïde, logit, cote (R6) · dérivée seconde, convexité en 1D (M05a) · fonctions convexes de plusieurs variables (M10) · gradient (M05b) · loi normale (M02b) · biais d'un estimateur (M02c) · hyperplans, produit scalaire (M07)

**mymath** : `likelihood.py` (signatures figées) : `bernoulli_log_likelihood`, `bernoulli_mle`, `categorical_mle`, `gaussian_mle`, `logistic_loss`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 13.8 ∂ Gradient de la log-loss de la régression logistique · 13.2 ✏️ Gini et entropie d'une feuille · 13.3 ✏️ Choisir le meilleur seuil sur la longueur des nageoires · 13.6 ✏️ Anglais ou français ? Naïve Bayes multinomial sur des lettres · 13.7 ✏️ Posterior d'un Naïve Bayes gaussien · 13.12 🔮 Prédire la frontière de cinq classifieurs avant de l'afficher · 13.27 🔮 Naïve Bayes sur des nuages gaussiens puis sur des lunes

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M13a.Q1 | 🧠 | Vraisemblance, log-vraisemblance, maximum : le vocabulaire | ★ | 4 | §1 | C, E | manuel | — |
| M13a.Q2 | 🧠 | Log-loss et cross-entropy : la même chose ? | ★ | 4 | §2 | C, E | manuel | — |
| M13a.Q3 | 🧠 | Les propriétés de la sigmoïde et de la softplus | ★ | 4 | §3 | C, E | manuel | — |
| M13a.Q4 | 🧠 | Ce que modélise un score w · x + b | ★ | 4 | §4 | C, E | manuel | — |
| M13a.Q5 | 🧠 | Génératif ou discriminant ? | ★ | 4 | §4 §5 | C, E | manuel | — |
| M13a.Q6 | 🧠 | Entropie et Gini : leurs propriétés | ★ | 4 | §6 | C, E | manuel | — |
| M13a.Q7 | 🧠 | Variance intra et variance inter : les feuilles d'un arbre de régression | ★ | 4 | §7 | C | manuel | — |
| M13a.Q8 | 🧠 | Convexe ou pas ? | ★ | 4 | §3 §4 | C | manuel | — |
| M13a.R1 | 🔁 | Bayes et le lissage de Laplace (M04) | ★ | 5 | §5 | C, E | manuel | — |
| M13a.R2 | 🔁 | Entropie, cross-entropy et information mutuelle (M06) | ★ | 5 | §2 §6 | C, E | manuel | — |
| M13a.R3 | 🔁 | Fonctions convexes de plusieurs variables (M10) | ★ | 5 | §3 | C, E | manuel | — |
| M13a.1 | ✏️ | Le maximum de vraisemblance d'une loi de Bernoulli et d'une loi catégorielle | ★ | 15 | §1 | C, E | wbm | — |
| M13a.2 | ✏️ | Le maximum de vraisemblance d'une loi normale : μ̂ et σ̂² | ★★ | 20 | §1 | C, E | wbm | — |
| M13a.3 | ✏️ | La log-loss de quatre prédictions, puis la même en cross-entropy | ★ | 15 | §2 | C, E | wbm | — |
| M13a.4 | ✏️ | Le poids d'un seul exemple mal prédit : la log-loss quand p tend vers 0 | ★ | 15 | §2 | C | wbm | — |
| M13a.5 | ✏️ | La sigmoïde : valeurs, logit, cote et symétrie σ(−z) = 1 − σ(z) | ★ | 15 | §3 | C, E | wbm | — |
| M13a.6 | ✏️ | La softplus : valeurs, asymptotes et comportement pour |z| grand | ★ | 15 | §3 | C, E | wbm | — |
| M13a.7 | ✏️ | Un modèle logistique à deux features : probabilités, cote et frontière de décision | ★ | 15 | §4 | C, E | wbm | — |
| M13a.8 | ✏️ | L'hypothèse naïve à la main : une loi jointe factorisée, comparée à la vraie | ★★ | 25 | §5 | C, E | wbm | — |
| M13a.9 | ✏️ | Deux classes gaussiennes de même variance : l'a posteriori est une sigmoïde d'un score affine | ★★ | 20 | §4 §5 | C | wbm | — |
| M13a.10 | ✏️ | L'entropie et l'indice de Gini de quelques distributions | ★ | 15 | §6 | C, E | wbm | — |
| M13a.11 | ✏️ | L'information mutuelle d'un tableau de contingence, et la baisse d'entropie qu'elle mesure | ★★ | 25 | §6 | C, E | wbm | — |
| M13a.12 | ✏️ | La variance d'un groupe coupé en deux : variance intra plus variance inter | ★★ | 15 | §7 | C | wbm | — |
| M13a.13 | ∂ | Le maximum de vraisemblance d'une loi catégorielle, par l'inégalité de Gibbs | ★★ | 20 | §1 | C, E | manuel | — |
| M13a.14 | ∂ | La log-loss moyenne est moins la log-vraisemblance divisée par n | ★ | 15 | §2 | C, E | manuel | — |
| M13a.15 | ∂ | Log-somme-exp est convexe : sur une droite, sa dérivée seconde est une variance ; la softplus aussi | ★★★ | 25 | §3 §4 | C, E | manuel | — |
| M13a.16 | ∂ | L'indice de Gini est maximal pour la loi uniforme | ★★ | 20 | §6 | C | manuel | — |
| M13a.17 | ∂ | L'entropie est maximale pour la loi uniforme, par l'inégalité de Gibbs | ★★ | 15 | §6 | C | manuel | — |
| M13a.18 | 🔗 | Pont : une sonde linéaire, un modèle logistique en NumPy sur un batch de représentations figées, jusqu'à la log-loss | ★ | 25 | §4 | C, E | wbm | — |
| M13a.19 | 📖 | MML §8.3, relu après M04 : estimer des paramètres, et ce que la régression logistique y ajoute | ★★ | 30 | §1 §4 | C | manuel | — |
| M13a.20 | 🧮 | Fermi : la loi jointe complète contre l'hypothèse naïve, combien de nombres pour 30 features à 4 valeurs ? | ★ | 10 | §5 | C | manuel | — |
| M13a.21 | 🗣️ | Expliquer pourquoi on minimise la log-loss plutôt que le taux d'erreur | ★ | 10 | §2 §4 | C, E | manuel | — |
| M13a.E1 | 💼 | « Pourquoi la cross-entropy est-elle une log-vraisemblance ? » | ★ | 10 | §2 | C | manuel | — |
| M13a.E2 | 💼 | « Qu'est-ce que le maximum de vraisemblance, et quel lien avec les losses que vous minimisez ? » | ★ | 10 | §1 §2 | C | manuel | — |
| M13a.22 | 🔨 | La log-vraisemblance et le maximum de vraisemblance d'une loi de Bernoulli · `bernoulli_log_likelihood, bernoulli_mle` | ★ | 15 | §1 | C, E | pytest | — |
| M13a.23 | 🔨 | Maximum de vraisemblance catégoriel, avec lissage, et gaussien · `categorical_mle, gaussian_mle` | ★ | 20 | §1 §5 | C, E | pytest | — |
| M13a.24 | 🔨 | La log-loss à partir des scores, sans débordement · `logistic_loss` | ★★ | 20 | §2 §3 | C, E | pytest | — |
| M13a.25 | 📦 | `scipy.stats`, `scipy.special` et `sklearn.metrics.log_loss` contre tes fonctions | ★ | 25 | §1 §2 §3 | C, E | wbm | — |
| M13a.26 | 🔮 | Prédire la log-loss d'un modèle qui répond toujours 0,5, puis toujours la fréquence des 1 | ★ | 10 | §2 | C, E | wbm | — |
| M13a.27 | 🔬 | La variabilité du maximum de vraisemblance d'une loi de Bernoulli d'un échantillon à l'autre | ★★ | 20 | §1 | C | wbm | — |
| M13a.28 | 🎨 | L'entropie et l'indice de Gini sur les lois à trois issues : lignes de niveau et maximum au centre | ★ | 25 | §6 | C, E | manuel | — |
| M13a.29 | 🐛 | Chasse à l'erreur : un ln 0, une sigmoïde qui déborde, une variance de maximum de vraisemblance divisée par n − 1 | ★ | 15 | §1 §2 §3 | C | wbm | — |
| M13a.30 | 🛠️ | Vérifier avec SymPy le maximum de vraisemblance d'une loi géométrique et d'une loi de Poisson | ★ | 15 | §1 | C | manuel | — |
| M13a.31 | 🏆 | Défi : la proportion d'un mélange de deux lois connues par maximum de vraisemblance, à 1e−6 près du maximum (dichotomie ou Newton) | ★★★ | 25 | §1 | C | wbm | — |

*Notes* : Frontières : 13.2 (interprétations de l'indice de Gini, maxima avec K = 3), 13.3 (recherche du meilleur seuil d'un arbre et gain d'un split), 13.6 (Naïve Bayes multinomial et lissage sur des lettres), 13.7 (posterior d'un Naïve Bayes gaussien à deux features), 13.12 et 13.27 (prédictions de Naïve Bayes), et le ∂ 13.8 (σ′ = σ(1 − σ), dℓ/dz = p̂ − y, gradient (1/n)Xᵀ(p̂ − y), convexité par d²ℓ/dz², pas de minimum sur des données séparables). M13a ne dérive aucun gradient de log-loss, et σ′ n'y est ni démontrée ni utilisée (13.8.1, 17.4.1) : la convexité de log-somme-exp se démontre par sa restriction à une droite, dont la dérivée seconde est une variance, sans écrire la hessienne diag(p) − ppᵀ (le ∂ 17.7 de workbookIA, et M17) ni la dérivée seconde de la softplus (13.8.6) ; la softplus en est la composée avec z ↦ (0, z) (M10). M13a.6 utilise l'écriture stable de la softplus sans l'établir (le ∂ 18.8.5 de workbookIA la démontre ; 17.13 code une sigmoïde stable). Il reste à l'impureté d'une distribution (maxima et concavité pour K quelconque), à l'information mutuelle d'un tableau de contingence de deux variables catégorielles quelconques (pas les deux enfants d'un split) et à la décomposition de la variance (intra plus inter), sans recherche de split ; Naïve Bayes y est l'hypothèse d'indépendance conditionnelle et un modèle génératif (deux gaussiennes de même variance donnent un a posteriori logistique), sans classer de mots ni de manchots ; la sonde linéaire est le pont M13a.18. Évités : la feuille 10/90 et les nœuds 30/70, 80/20, (3, 1) et (1, 3) de la fiche de workbookIA 13, les lois 0,5/0,3/0,2 et 25/75 (13.2), 50/50 (13.Q9) et 6/3/1 (14.R1), la figure des trois impuretés d'une loi binaire, les cibles 2, 4, 9, le modèle w = (2, −1), b = 0,5, σ(2) et σ′(2), la log-densité en x = 12, le logsumexp de (−1 000, −1 001), le lissage 1/250, le nombre de paramètres d'un Naïve Bayes gaussien (13.Q11 c) et les 20 features binaires de la fiche, les nageoires et becs des manchots, les lettres e, h, q, w, l'équivalence α = 1/(Cn) de 13.32 et (checkpoint III de workbookIA, CP3.12 d) une feature en deux copies dans Naïve Bayes. `likelihood` écrit les briques du maximum de vraisemblance et la log-loss à partir des scores ; `categorical_mle` est la formule de `MultinomialNB` et `gaussian_mle` l'ajustement d'une classe de `GaussianNB` (des briques, que workbookIA assemble) ; `mymath` a déjà `explog.sigmoid`, `approx.logsumexp` et `info.mutual_information` (pas réécrits) ; les impuretés, le meilleur split, `log_gaussian_pdf`, GaussianNB, MultinomialNB et LogisticRegression sont les fonctions de `mylearn` en workbookIA 13. Conventions : log-loss en logarithme népérien, entropies des arbres en bits.

<a id="m13b"></a>
## M13b · Optimisation sous contraintes et SVM

**Partie** III · **prépare** workbookIA 13 · **dossier** `chapitres/m13b_lagrange_svm/` · **MML** §7.2, §7.3, ch. 12 · **sessions de génération** 2

L'optimisation sous contraintes : multiplicateurs de Lagrange, conditions KKT, dualité, optimisation convexe, et l'ACP relue par Lagrange ; puis les SVM : marge, problème primal à marge dure et souple, hinge loss et sous-gradient, problème dual, vecteurs de support, noyaux et astuce du noyau (polynomial, RBF).

**Temps** : 16,1 h en parcours complet, 9,6 h en parcours essentiel (lecture 180 min, 24 flashcards).

**Objectifs**

- Résoudre un problème d'optimisation sous contraintes d'égalité par les multiplicateurs de Lagrange.
- Écrire les conditions KKT d'un problème avec inégalités, et sa fonction duale.
- Reconnaître un problème convexe et ce qu'il garantit.
- Écrire le problème d'une SVM à marge dure et à marge souple, et le relier à la hinge loss.
- Lire le problème dual d'une SVM et ses vecteurs de support.
- Calculer avec des noyaux polynomiaux et RBF, et reconnaître un noyau valide.

**Sections de la fiche**

- §1 Optimiser sous une contrainte d'égalité : les multiplicateurs de Lagrange
- §2 Plusieurs contraintes, et l'ACP relue par Lagrange
- §3 Contraintes d'inégalité : les conditions KKT
- §4 La dualité (aperçu)
- §5 L'optimisation convexe
- §6 La SVM à marge dure
- §7 Marge souple, hinge loss et sous-gradient
- §8 Le problème dual, les vecteurs de support et les noyaux

**Notions enseignées** : optimisation sous contraintes · multiplicateurs de Lagrange · conditions KKT · dualité (aperçu) · optimisation convexe · relire MML §10.2 : l'ACP par Lagrange · marge · SVM primal · hinge loss · sous-gradient · SVM dual · noyaux et astuce du noyau · noyau RBF

**Prérequis** : marge géométrique, astuce du biais, séparabilité, programmes linéaires (M10) · gradient, lignes de niveau (M05b) · matrices définies positives, quotient de Rayleigh, matrice de Gram (M12c) · axes principaux (M12d) · distance à un hyperplan (M07) · systèmes linéaires (M09a)

**mymath** : `svm.py` (signatures figées) : `lagrange_equality_qp`, `hinge_loss`, `svm_subgradient`, `rbf_kernel`, `polynomial_kernel`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 13.8 ∂ Gradient de la log-loss de la régression logistique · 13.4 ✏️ Distance à une droite et marge d'un SVM · 13.5 ✏️ L'astuce du noyau vérifiée à la main · 13.17 🎨 Relever les cercles en 3D pour les séparer par un plan

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M13b.Q1 | 🧠 | Lagrange : ce que dit ∇f = λ ∇g | ★ | 4 | §1 | C, E | manuel | — |
| M13b.Q2 | 🧠 | Contrainte active ou inactive ? | ★ | 4 | §3 | C, E | manuel | — |
| M13b.Q3 | 🧠 | Primal, dual, dualité faible | ★ | 4 | §4 | C | manuel | — |
| M13b.Q4 | 🧠 | Problème convexe ou pas ? | ★ | 4 | §5 | C, E | manuel | — |
| M13b.Q5 | 🧠 | Ce que maximise une SVM, ce que minimise son problème | ★ | 4 | §6 | C, E | manuel | — |
| M13b.Q6 | 🧠 | La hinge loss : vrai ou faux | ★ | 4 | §7 | C, E | manuel | — |
| M13b.Q7 | 🧠 | Noyau valide ou pas ? | ★ | 4 | §8 | C, E | manuel | — |
| M13b.Q8 | 🧠 | Primal ou dual : lequel résoudre, et quand ? | ★ | 4 | §8 | C | manuel | — |
| M13b.R1 | 🔁 | La marge géométrique et l'astuce du biais (M10) | ★ | 5 | §6 | C, E | manuel | — |
| M13b.R2 | 🔁 | Gradient et lignes de niveau (M05b) | ★ | 5 | §1 | C, E | manuel | — |
| M13b.R3 | 🔁 | Matrices définies positives (M12c) | ★ | 5 | §5 §8 | C, E | manuel | — |
| M13b.1 | ✏️ | Lagrange à la main : un produit maximal sous une contrainte linéaire | ★ | 15 | §1 | C, E | wbm | — |
| M13b.2 | ✏️ | La distance d'un point à un plan, retrouvée par Lagrange | ★★ | 20 | §1 | C | wbm | — |
| M13b.3 | ✏️ | Un problème quadratique sous deux contraintes linéaires : le système de Lagrange | ★★ | 20 | §2 | C, E | wbm | — |
| M13b.4 | ✏️ | Relire l'ACP par Lagrange : maximiser uᵀCu sous ‖u‖ = 1 | ★★ | 20 | §2 | C | wbm | — |
| M13b.5 | ✏️ | Une contrainte d'inégalité : active ou non, les conditions KKT à la main | ★★ | 20 | §3 | C, E | wbm | — |
| M13b.6 | ✏️ | La fonction duale d'un petit problème quadratique, et la dualité faible | ★★ | 20 | §4 | C | wbm | — |
| M13b.7 | ✏️ | Reconnaître un problème convexe : fonctions, contraintes, ensembles | ★ | 15 | §5 | C, E | wbm | — |
| M13b.8 | ✏️ | Une SVM à marge dure sur trois points, résolue par les conditions KKT | ★★ | 25 | §6 §8 | C, E | wbm | — |
| M13b.9 | ✏️ | La hinge loss et l'objectif régularisé de quelques points | ★ | 15 | §7 | C, E | wbm | — |
| M13b.10 | ✏️ | Un pas de sous-gradient sur l'objectif d'une SVM linéaire | ★★ | 15 | §7 | C | wbm | — |
| M13b.11 | ✏️ | Le dual d'une SVM : lire les vecteurs de support et retrouver w | ★★ | 20 | §8 | C | wbm | — |
| M13b.12 | ✏️ | Le noyau (1 + x · z)² en dimension 2 : sa fonction φ à six coordonnées | ★★ | 20 | §8 | C | wbm | — |
| M13b.13 | ✏️ | La matrice de Gram d'un noyau RBF sur trois points, et l'effet de γ | ★ | 15 | §8 | C, E | wbm | — |
| M13b.14 | ∂ | Au point optimal sous une contrainte d'égalité, ∇f est colinéaire à ∇g | ★★ | 20 | §1 | C | manuel | — |
| M13b.15 | ∂ | La dualité faible : la fonction duale minore le minimum du primal | ★★ | 15 | §4 | C, E | manuel | — |
| M13b.16 | ∂ | Pour un problème convexe, un minimum local est global | ★★ | 15 | §5 | C, E | manuel | — |
| M13b.17 | ∂ | Maximiser la marge revient à minimiser ½ ‖w‖² | ★★ | 20 | §6 | C, E | manuel | — |
| M13b.18 | ∂ | Marge souple : la formulation avec des variables d'écart et celle avec la hinge loss sont équivalentes | ★★ | 20 | §7 | C | manuel | — |
| M13b.19 | ∂ | La somme et le produit de deux noyaux sont des noyaux ; une matrice de Gram est semi-définie positive | ★★★ | 25 | §8 | C | manuel | — |
| M13b.20 | 🔗 | Pont : la décision d'une SVM à noyau, une somme pondérée sur les vecteurs de support | ★ | 15 | §8 | C, E | wbm | — |
| M13b.21 | 📖 | MML §7.2 et §7.3 : Lagrange, dualité et optimisation convexe, en anglais | ★★ | 40 | §1 §3 §4 §5 | C | manuel | — |
| M13b.22 | 📖 | MML §12.2 à §12.5 : marge, primal, dual et noyaux (§12.1 a été lu en M10) | ★★ | 50 | §6 §7 §8 | C | manuel | — |
| M13b.23 | 🧮 | Fermi : la taille de la matrice de Gram d'une SVM à noyau sur 100 000 exemples | ★ | 10 | §8 | C | manuel | — |
| M13b.24 | 🗣️ | Expliquer un multiplicateur de Lagrange comme un prix | ★ | 10 | §1 §4 | C, E | manuel | — |
| M13b.E1 | 💼 | « Qu'est-ce qu'un problème d'optimisation convexe, et pourquoi est-ce une bonne nouvelle ? » | ★ | 10 | §5 | C | manuel | — |
| M13b.E2 | 💼 | « Hinge loss ou log-loss : quelles différences ? » | ★ | 10 | §7 | C | manuel | — |
| M13b.25 | 🔨 | Un problème quadratique sous contraintes d'égalité, par le système de Lagrange · `lagrange_equality_qp` | ★ | 20 | §2 | C, E | pytest | — |
| M13b.26 | 🔨 | La hinge loss et un sous-gradient de l'objectif d'une SVM linéaire · `hinge_loss, svm_subgradient` | ★★ | 25 | §7 | C, E | pytest | — |
| M13b.27 | 🔨 | Les noyaux RBF et polynomial · `rbf_kernel, polynomial_kernel` | ★ | 20 | §8 | C, E | pytest | — |
| M13b.28 | 📦 | `scipy.optimize.minimize` sous contraintes et les noyaux de scikit-learn contre tes fonctions | ★ | 15 | §2 §8 | C, E | wbm | — |
| M13b.29 | 🔮 | Prédire : comment change le minimum quand on relâche la contrainte, et ce que dit λ | ★ | 10 | §1 §4 | C, E | wbm | — |
| M13b.30 | 🔬 | La descente de sous-gradient sur la hinge loss : pas constant contre pas décroissant | ★★ | 20 | §7 | C | wbm | — |
| M13b.31 | 🎨 | Lignes de niveau et contrainte : voir le point de Lagrange | ★ | 20 | §1 | C, E | manuel | — |
| M13b.32 | 🐛 | Chasse à l'erreur : le signe d'un multiplicateur, une largeur de bande 1/‖w‖ au lieu de 2/‖w‖, une matrice de Gram non symétrique | ★ | 15 | §3 §6 §8 | C | wbm | — |
| M13b.33 | 🛠️ | Vérifier une solution KKT : faisabilité, stationnarité, complémentarité | ★ | 15 | §3 | C | manuel | — |
| M13b.34 | 🏆 | Défi : une SVM linéaire entraînée par sous-gradient, un objectif à 1 % de celui de scikit-learn au même C | ★★★ | 30 | §7 | C | wbm | — |

*Notes* : Frontières : 13.4 (vérifier une solution de SVM primal sur six points), 13.5 (le noyau (x · z)² et φ = (x₁², √2 x₁x₂, x₂²)), 13.17 (des cercles relevés en 3D par x₁² + x₂²), et le ∂ 13.8. M13b résout de petites SVM par les conditions KKT et le dual (un énoncé plus général que la vérification de 13.4) et enseigne l'astuce du noyau par (1 + x · z)², la matrice de Gram semi-définie positive et le développement en série du noyau RBF. Conventions : marge = 1/‖w‖ (de la frontière au point le plus proche, comme MML §12.2 et M10), largeur de la bande = 2/‖w‖ (le syllabus de workbookIA 13 écrit « marge = 2/‖w‖ », sa fiche dit 1/‖w‖) ; RBF écrit avec γ ; contrainte de boîte 0 ≤ αᵢ ≤ C dans le dual. Évités : l'exemple x₁ + 2x₂ − 4 = 0 et le point (3, 3), les valeurs du RBF à distance 1 (γ = 0,1, 1, 10), φ(2, 0) et φ(1, 1), et, pour motiver les noyaux, le ou exclusif, les cercles, le relèvement |x| → (x, x²), les spirales et les demi-lunes ; les six coordonnées de φ en M13b.12 sont un rappel de `linreg.count_monomials` (M09b), pas un comptage par étoiles et barres (workbookIA 15.4). Le 🏆 M13b.34 mesure l'optimisation : l'objectif J, à 1 % de celui de `SVC(kernel="linear")` au même C. workbookIA n'écrit pas de SVM (pas de `mylearn`) : `svm` écrit Lagrange sous contraintes d'égalité, la hinge loss et son sous-gradient, et les noyaux ; NumPy permis, pas `scipy.optimize`, `scipy.spatial` ni scikit-learn.

<a id="m14"></a>
## M14 · Les maths des ensembles

**Partie** III · **prépare** workbookIA 14 · **dossier** `chapitres/m14_ensembles/` · **MML** — · **sessions de génération** 1

Les outils des ensembles de modèles : la queue de la loi binomiale et sa borne de Chernoff, la variance d'une moyenne pondérée de variables corrélées, la limite (1 + x/n)ⁿ → eˣ, les poids exponentiels (l'algorithme Hedge) et le gradient d'une loss par rapport aux prédictions. workbookIA 14 les applique au vote, au bagging et au boosting.

**Temps** : 7,2 h en parcours complet, 4,7 h en parcours essentiel (lecture 90 min, 12 flashcards).

**Objectifs**

- Calculer la queue d'une loi binomiale, et la majorer par la borne de Chernoff.
- Calculer la variance d'une moyenne pondérée de variables corrélées par leur matrice de covariance.
- Démontrer et utiliser la limite (1 + x/n)ⁿ → eˣ.
- Calculer des poids exponentiels renormalisés, et suivre le meilleur de plusieurs experts.
- Calculer le gradient d'une loss par rapport au vecteur des prédictions.

**Sections de la fiche**

- §1 La queue d'une loi binomiale
- §2 La variance d'une moyenne de variables corrélées
- §3 La limite (1 + x/n)ⁿ → eˣ
- §4 Des poids exponentiels : l'algorithme Hedge
- §5 Le gradient d'une loss par rapport aux prédictions

**Notions enseignées** : queue de la loi binomiale · borne de Chernoff (divergence KL) · variance d'une moyenne de variables corrélées · (1 + x/n)ⁿ → eˣ · poids exponentiels et renormalisation · descente de gradient dans un espace de fonctions (idée) · forêt aléatoire : décorréler pour réduire la variance

**Prérequis** : loi binomiale (M02b) · covariance, variance d'une somme, matrice de covariance (M02c) · développements de Taylor, ln(1 + u) (M05a) · inégalité de Hoeffding, méthode de Chernoff, regret (M11) · divergence KL (M06) · gradient (M05b) · loss de Huber (M09b) · log-loss (M13a)

**mymath** : `ensembles.py` (signatures figées) : `chernoff_bound`, `variance_of_average`, `hedge_weights`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 14.3 ∂ Probabilité d'être oublié par un bootstrap : vers 36,8 % · 14.4 ∂ Ajuster les résidus, c'est descendre le gradient de la MSE · 14.5 ✏️ Quand la majorité de votants indépendants se trompe · 14.6 ✏️ Une itération d'AdaBoost à la main · 14.7 ✏️ Deux itérations de gradient boosting sur cinq points · 14.13 🔬 Jury de votants : indépendants puis corrélés · 14.23 🐛 L'AdaBoost qui n'apprend rien

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M14.Q1 | 🧠 | La queue d'une loi binomiale et ses bornes : vrai ou faux | ★ | 4 | §1 | C, E | manuel | — |
| M14.Q2 | 🧠 | Corrélation et variance d'une moyenne | ★ | 4 | §2 | C, E | manuel | — |
| M14.Q3 | 🧠 | Des limites remarquables | ★ | 4 | §3 | C, E | manuel | — |
| M14.Q4 | 🧠 | Des poids exponentiels | ★ | 4 | §4 | C | manuel | — |
| M14.R1 | 🔁 | La log-loss et la divergence KL (M13a, M06) | ★ | 5 | §1 §5 | C, E | manuel | — |
| M14.R2 | 🔁 | La variance d'une somme et la matrice de covariance (M02c) | ★ | 5 | §2 | C, E | manuel | — |
| M14.R3 | 🔁 | Taylor et ln(1 + u) (M05a) | ★ | 5 | §3 | C, E | manuel | — |
| M14.1 | ✏️ | La fiabilité d'un système « k parmi n » : au moins k composants qui marchent | ★ | 15 | §1 | C, E | wbm | — |
| M14.2 | ✏️ | La variance de la moyenne de trois mesures corrélées, par la matrice de covariance | ★ | 15 | §2 | C, E | wbm | — |
| M14.3 | ✏️ | (1 + x/n)ⁿ pour quelques n, et des intérêts composés en continu | ★ | 10 | §3 | C, E | wbm | — |
| M14.4 | ✏️ | Les poids exponentiels de cinq experts après trois tours | ★ | 15 | §4 | C, E | wbm | — |
| M14.5 | ✏️ | Le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport aux prédictions, et les poids exponentiels qu'il fait apparaître | ★★ | 15 | §4 §5 | C | wbm | — |
| M14.6 | ∂ | (1 + x/n)ⁿ → eˣ, par le logarithme et ln(1 + u) ≈ u | ★★ | 20 | §3 | C, E | manuel | — |
| M14.7 | ∂ | Une moyenne pondérée de variables de variance σ² a une variance au plus σ² | ★★ | 15 | §2 | C | manuel | — |
| M14.8 | ∂ | La borne de Chernoff d'une queue binomiale : le meilleur λ donne exp(−n KL(a ‖ p)) | ★★★ | 25 | §1 | C | manuel | — |
| M14.9 | 🔗 | Pont : ajouter des modèles très corrélés ne sert presque à rien, un plancher de variance sur deux groupes de modèles | ★ | 15 | §2 | C, E | wbm | — |
| M14.10 | 🗣️ | Expliquer pourquoi une moyenne réduit la variance, et quand elle ne la réduit plus | ★ | 10 | §2 | C, E | manuel | — |
| M14.E1 | 💼 | « Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est le meilleur ? » | ★ | 10 | §4 | C | manuel | — |
| M14.11 | 🔨 | La borne de Chernoff et la variance d'une moyenne pondérée · `chernoff_bound, variance_of_average` | ★ | 20 | §1 §2 | C, E | pytest | — |
| M14.12 | 🔨 | Les poids de l'algorithme Hedge · `hedge_weights` | ★ | 15 | §4 | C | pytest | — |
| M14.13 | 🔬 | Simuler la moyenne de deux groupes de modèles corrélés, et retrouver aᵀΣa et son plancher | ★★ | 20 | §2 | C, E | wbm | — |
| M14.14 | 🎨 | Les poids exponentiels au fil des tours : quel expert domine, selon le learning rate | ★ | 15 | §4 | C | manuel | — |
| M14.15 | 🐛 | Chasse à l'erreur : P(X ≥ k) calculée comme P(X > k), des covariances oubliées, des poids non renormalisés | ★ | 15 | §1 §2 §4 | C | wbm | — |
| M14.16 | 🛠️ | Un test qui vérifie que la borne de Chernoff majore la queue exacte de `scipy.stats`, sur une grille de n, p et a | ★ | 15 | §1 | C | manuel | — |
| M14.17 | 🏆 | Défi : suivre le meilleur de dix experts avec Hedge sans connaître l'horizon, un regret sous la borne théorique sur 1 000 tours | ★★★ | 25 | §4 | C | wbm | — |

*Notes* : Réduit à 7 h. Frontières : 14.5 (la majorité de votants indépendants), 14.6 et 14.23 (une itération d'AdaBoost, les mal classés qui pèsent la moitié), 14.7 (deux itérations de gradient boosting), 14.13 (des votants corrélés par un choc commun), et les ∂ 14.3 ((1 − 1/n)ⁿ → e⁻¹ dans le bootstrap) et 14.4 (les résidus comme gradient de la MSE, la médiane pour la valeur absolue, y − p̂ pour la log-loss). Hors des cadres de workbookIA : la queue binomiale sur la fiabilité de systèmes « k parmi n » (calculée avec `testing.binomial_test` de M08) et la borne de Chernoff exp(−n KL(a ‖ p)), qui généralise CP2.9 B et relie M06 à M11 (le théorème du jury en général) ; la limite (1 + x/n)ⁿ → eˣ pour tout x (intérêts composés, survie) ; la variance d'une moyenne pondérée par aᵀΣa, sur des prédictions continues et deux groupes de modèles (M14.9, M14.13) ; les poids exponentiels de l'algorithme Hedge (des experts, avec un learning rate qui décroît quand l'horizon est inconnu, M14.17) ; le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport aux prédictions, d'où les poids exponentiels (M14.5). Le checkpoint III de workbookIA démontre ρσ² + (1 − ρ)σ²/M (CP3.13, que la copie figée ne permet pas de lister ici) : M14 ne démontre ni ne chiffre ce cas équicorrélé ; « la moyenne minimise les carrés » et « la médiane minimise les écarts absolus » ne sont pas redémontrés. Évités : la redondance triple d'Apollo (2 parmi 3), 15 votants à 70 % (14.Q1), 7 votants à 80 %, les q et M de 14.5 (0,7 pour 3, 5, 9 votants ; 0,6 et 11 ; 0,51 et 101 ; 0,45 et 25 ; 0,65 et 7), q = 0,58 (14.13), q = 42 %, 55 %, 65 %, ρ = 0,2 et 0,6, σ² = 1 et ρ = 0,5, les valeurs de CP3.13 (σ² = 4, ρ = 0,25, M = 10 ; ρ = 0,1, σ² = 5), x = −1 dans la limite (0,9¹⁰, 0,999¹⁰⁰⁰, 100 ln 0,99, n = 5 et 0,328), a = 3/4 et p = 1/2 (CP2.9 B), AdaBoost à 20 exemples, les cibles 3 et 4 du gradient boosting, l'hypergéométrique 32, 5, 2 (14.16). Le bootstrap qui oublie 36,8 % des points, les résidus comme gradient, la majorité qui se trompe, AdaBoost et le gradient boosting à la main sont des exercices de workbookIA 14 ; `ensembles` n'écrit ni vote ni mise à jour d'AdaBoost (`mylearn`), ni de queue binomiale exacte (`testing.binomial_test`, M08).

<a id="cp3"></a>
## CP3 · Examen blanc de la partie III

**Partie** III · **prépare** — · **dossier** `checkpoints/partie_3/` · **MML** — · **sessions de génération** 1

Le bilan de la partie III (M12a à M14), juste avant le checkpoint III de workbookIA : un examen blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.

**Temps** : 3,1 h en parcours complet, 3,1 h en parcours essentiel (lecture 15 min, 0 flashcards).

**Objectifs**

- Vérifier en temps limité que les notions de la partie III sont acquises.
- Construire ta propre synthèse de la partie III.

**Sections de la fiche**

- §1 Examen blanc
- §2 Synthèse

**Notions enseignées** : révision de la partie III

**Prérequis** : toute la partie III (M14)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.7 ✏️ PCA à la main en 2D : covariance, axe principal, projection · 12.8 ∂ Variance d'une projection et axe de variance maximale · 12.22 🎨 Projeter un nuage 2D : axe horizontal contre axe de variance maximale · 12.27 🔨 Coder la PCA (SVD, variance expliquée, whitening, reconstruction) · 12.29 🔬 Échelle des features et descente de gradient · 12.R3 🔁 Descente de gradient dans une vallée très allongée · 13.2 ✏️ Gini et entropie d'une feuille · 13.3 ✏️ Choisir le meilleur seuil sur la longueur des nageoires · 13.4 ✏️ Distance à une droite et marge d'un SVM · 13.5 ✏️ L'astuce du noyau vérifiée à la main · 13.6 ✏️ Anglais ou français ? Naïve Bayes multinomial sur des lettres · 13.7 ✏️ Posterior d'un Naïve Bayes gaussien · 13.8 ∂ Gradient de la log-loss de la régression logistique · 13.12 🔮 Prédire la frontière de cinq classifieurs avant de l'afficher · 13.17 🎨 Relever les cercles en 3D pour les séparer par un plan · 13.27 🔮 Naïve Bayes sur des nuages gaussiens puis sur des lunes · 14.3 ∂ Probabilité d'être oublié par un bootstrap : vers 36,8 % · 14.4 ∂ Ajuster les résidus, c'est descendre le gradient de la MSE · 14.5 ✏️ Quand la majorité de votants indépendants se trompe · 14.6 ✏️ Une itération d'AdaBoost à la main · 14.7 ✏️ Deux itérations de gradient boosting sur cinq points · 14.13 🔬 Jury de votants : indépendants puis corrélés · 14.23 🐛 L'AdaBoost qui n'apprend rien · 15.3 ✏️ Ramener une droite ajustée dans l'espace d'origine

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| CP3.Q1 | 🧠 | Dix affirmations sur la partie III : vrai ou faux | ★ | 10 | §1 | C, E | manuel | — |
| CP3.1 | ✏️ | Indépendance, base, rang et noyau | ★★ | 10 | §1 | C, E | wbm | — |
| CP3.2 | ✏️ | Gram-Schmidt, projection et moindres carrés | ★★ | 10 | §1 | C, E | wbm | — |
| CP3.3 | ✏️ | Valeurs propres, matrice définie positive et Cholesky | ★★ | 10 | §1 | C, E | wbm | — |
| CP3.4 | ✏️ | SVD, rang faible et variance expliquée | ★★ | 10 | §1 | C, E | wbm | — |
| CP3.5 | ✏️ | Maximum de vraisemblance, log-loss et entropie | ★★ | 9 | §1 | C, E | wbm | — |
| CP3.6 | ✏️ | Lagrange, hinge loss et noyau | ★★ | 9 | §1 | C, E | wbm | — |
| CP3.7 | ✏️ | Queue binomiale et borne de Chernoff, limite et poids exponentiels | ★★ | 8 | §1 | C, E | wbm | — |
| CP3.8 | ∂ | Une démonstration courte, au choix parmi deux | ★★★ | 12 | §1 | C, E | manuel | — |
| CP3.9 | 🐛 | Corriger une copie : cinq erreurs | ★★ | 8 | §1 | C, E | wbm | — |
| CP3.10 | 🔗 | Problème de synthèse : des données centrées, leurs axes principaux, un modèle sur les scores | ★★ | 14 | §1 | C, E | wbm | — |
| CP3.11 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme CP2 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, 03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend le checkpoint III de workbookIA (`checkpoints/partie_3/` de workbookIA : prédictions de scikit-learn, standardiser et encoder des becs de manchots, Gini et meilleur seuil sur six points, kNN avant et après standardisation, une itération d'AdaBoost et une de gradient boosting, fuites d'un script, seuil de coût minimal, courbes de validation et de boosting, l'astuce du noyau par une parabole, calibration et déploiement, precision et folds stratifiés, Naïve Bayes avec une feature en deux copies, variance d'une moyenne de modèles corrélés, coût d'une recherche en grille), qui se fait juste après, ni son mini-projet III (recensement Adult, revenus, audit d'équité). CP3.10 n'enchaîne pas la suite de 12.7 (un vecteur donné puis vérifié, la part expliquée, les coordonnées, la reconstruction, le blanchiment), et CP3.7 ne porte pas sur la variance d'une moyenne de modèles corrélés (CP3.13 de workbookIA).

<a id="m16"></a>
## M16 · Applications affines, graphes et variance d'un produit

**Partie** IV · **prépare** workbookIA 16 · **dossier** `chapitres/m16_couches_affines/` · **MML** — · **sessions de génération** 1

Les outils d'un réseau feed-forward, pris hors des réseaux : les applications affines dans les deux conventions (x W + b et W x + b) et leurs formes, leur composition par les coordonnées homogènes, les graphes orientés lus sur leur matrice d'adjacence (degrés, chemins comptés par les puissances, graphe sans cycle et matrice nilpotente, numérotation qui la rend triangulaire, somme sur les chemins), puis l'espérance et la variance d'un produit de variables indépendantes, la variance d'une somme de produits seulement décorrélés, et des variances qui se multiplient d'étage en étage. workbookIA 16 les applique aux couches, à l'ordre topologique et à l'initialisation.

**Temps** : 8,0 h en parcours complet, 6,0 h en parcours essentiel (lecture 80 min, 12 flashcards).

**Objectifs**

- Écrire une application affine de ℝⁿ dans ℝᵐ dans les deux conventions (x W + b et W x + b), avec la forme de chaque objet, et compter ses paramètres.
- Composer des applications affines en multipliant leurs matrices en coordonnées homogènes.
- Lire un graphe orienté sur sa matrice d'adjacence : degrés entrants et sortants, chemins de longueur k comptés par Aᵏ.
- Reconnaître un graphe sans cycle par la nilpotence de sa matrice d'adjacence, numéroter ses nœuds pour la rendre triangulaire, et sommer sur ses chemins.
- Calculer l'espérance et la variance d'un produit de variables indépendantes, et la variance d'une somme de variables seulement décorrélées.
- Suivre une variance multipliée par le même facteur à chaque étage, et prévoir son explosion ou son extinction.

**Sections de la fiche**

- §1 Applications affines : formes et conventions
- §2 Composer des applications affines : les coordonnées homogènes
- §3 Graphes orientés et matrice d'adjacence
- §4 Graphes sans cycle : nilpotence, numérotation triangulaire, somme sur les chemins
- §5 Espérance et variance d'un produit de variables indépendantes
- §6 Sommes de produits : décorrélées suffit
- §7 Des variances qui se multiplient d'étage en étage

**Notions enseignées** : application affine de ℝⁿ dans ℝᵐ : conventions ligne (x W + b) et colonne (W x + b), formes · nombre de paramètres d'une application affine (n m + m) · coordonnées homogènes : composer des applications affines, c'est multiplier des matrices · graphe orienté : degrés entrant et sortant, matrice d'adjacence · chemins de longueur k : les puissances de la matrice d'adjacence · graphe sans cycle ⇔ matrice d'adjacence nilpotente ⇔ numérotation qui la rend triangulaire · somme sur les chemins des produits de poids : (I − A)⁻¹ = I + A + … + Aⁿ⁻¹ · espérance et variance d'un produit de variables indépendantes · covariance nulle sans indépendance ; variance d'une somme de variables décorrélées · multiplicateurs aléatoires centrés : des produits εᵢ xᵢ décorrélés même quand les xᵢ sont corrélés · variance multipliée par un facteur g à chaque étage : gᴸ

**Prérequis** : Z = XW + b : la convention des poids, produit matriciel, formes, coût d'un produit (M09a) · produit de Hadamard (M09a) · applications affines, composition et produit de matrices, réciproque (M12a) · matrices triangulaires, valeurs propres d'une matrice triangulaire (M12c) · variance, indépendance, variance d'une somme de variables indépendantes, lois uniforme et normale (M02b) · covariance, corrélation (M02c) · suites géométriques (R5) · raisonnement par récurrence (R4) · dénombrement (R8)

**mymath** : `affine.py` (signatures figées) : `homogeneous_matrix`, `sum_over_paths`, `variance_of_product`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 16.6 ∂ Symétrie : pourquoi une initialisation constante ne se brise jamais · 16.7 ∂ Conserver la variance : retrouver les règles de LeCun, Glorot et He · 16.1 ✏️ Compter les poids et les biais d'un MLP · 16.2 ✏️ Passe avant à la main dans un réseau 2-2-1 · 16.3 ✏️ Formes et broadcasting d'un mini-batch à travers les couches · 16.4 ✏️ Ordre d'évaluation d'un graphe et détection de boucle · 16.8 🧮 Fermi : taille, mémoire et coût d'un MLP pour MNIST · 16.Q10 🧠 LeCun, Glorot, He : quel fan-in, pour quelle activation ? · 16.15 🎨 Reproduire les figures 16.5 et 16.6, puis comparer Glorot et He · 16.19 🔮 Initialisation constante : les neurones restent-ils jumeaux ? · 16.23 🔬 Activations à travers 20 couches selon l'initialisation · 17.1 ✏️ Effondrer un réseau linéaire en un seul neurone · 17.3 ∂ Une composition d'affines reste affine ; une ReLU casse tout

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M16.Q1 | 🧠 | Les formes de W, de b et de x W + b, dans chaque convention | ★ | 4 | §1 | C, E | manuel | — |
| M16.Q2 | 🧠 | Coordonnées homogènes et composition : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| M16.Q3 | 🧠 | Lire une matrice d'adjacence : degrés, arêtes, chemins, cycles | ★ | 4 | §3 §4 | C, E | manuel | — |
| M16.Q4 | 🧠 | Indépendantes, décorrélées, ou ni l'un ni l'autre ? | ★ | 4 | §5 §6 | C, E | manuel | — |
| M16.R1 | 🔁 | Le produit matriciel, ses formes et son coût (M09a) | ★ | 5 | §1 | C, E | manuel | — |
| M16.R2 | 🔁 | La variance d'une somme de variables indépendantes (M02b) | ★ | 5 | §5 | C, E | manuel | — |
| M16.R3 | 🔁 | Les valeurs propres d'une matrice triangulaire (M12c) | ★ | 5 | §4 | C | manuel | — |
| M16.1 | ✏️ | Une application affine de ℝ³ dans ℝ² dans les deux conventions : formes, transposée, nombre de paramètres | ★ | 15 | §1 | C, E | wbm | — |
| M16.2 | ✏️ | Rotation, homothétie puis translation du plan : la matrice homogène de la composée, et celle de la réciproque | ★★ | 20 | §2 | C, E | wbm | — |
| M16.3 | ✏️ | Des rues à sens unique : degrés, matrice d'adjacence, et chemins de longueur 2 et 3 par ses puissances | ★ | 15 | §3 | C, E | wbm | — |
| M16.4 | ✏️ | Un planning de tâches : l'absence de cycle par les puissances de A, une numérotation qui la rend triangulaire, et le nombre de chemins entre deux tâches | ★★ | 25 | §4 | C, E | wbm | — |
| M16.5 | ✏️ | Un prix aléatoire fois une quantité indépendante : espérance et variance du produit | ★★ | 15 | §5 | C, E | wbm | — |
| M16.6 | ✏️ | Des signes aléatoires d'amplitudes différentes sur des mesures corrélées : la variance d'une somme de produits | ★★ | 20 | §6 | C, E | wbm | — |
| M16.7 | ∂ | (Aᵏ)ᵢⱼ compte les chemins de longueur k de i à j, par récurrence | ★★ | 15 | §3 | C | manuel | — |
| M16.8 | ∂ | Un graphe est sans cycle si et seulement si sa matrice d'adjacence est nilpotente | ★★ | 20 | §4 | C, E | manuel | — |
| M16.9 | ∂ | La variance d'un produit de deux variables indépendantes | ★★ | 15 | §5 | C | manuel | — |
| M16.10 | 🔗 | Pont : n points rangés en lignes, X W + 1bᵀ, et la diffusion de b | ★ | 15 | §1 | C, E | wbm | — |
| M16.11 | 🗣️ | Expliquer, sur un exemple, pourquoi la variance d'un produit n'est pas le produit des variances | ★ | 10 | §5 | C, E | manuel | — |
| M16.E1 | 💼 | « Pourquoi l'écart-type d'une somme de n termes indépendants grandit-il comme √n ? » | ★ | 10 | §6 §7 | C | manuel | — |
| M16.12 | 🔨 | La matrice homogène d'une application affine · `homogeneous_matrix` | ★ | 15 | §2 | C, E | pytest | — |
| M16.13 | 🔨 | Sommer sur les chemins d'un graphe sans cycle par les puissances de sa matrice · `sum_over_paths` | ★★ | 20 | §3 §4 | C, E | pytest | — |
| M16.14 | 🔨 | Espérance et variance d'un produit de variables indépendantes · `variance_of_product` | ★ | 15 | §5 | C | pytest | — |
| M16.15 | 🔮 | Prédire l'écart-type d'une somme de produits aléatoires, mesures corrélées ou non, puis simuler | ★ | 10 | §6 §7 | C, E | wbm | — |
| M16.16 | 🔬 | Une variance multipliée d'étage en étage : simuler une chaîne d'amplificateurs bruités | ★★ | 20 | §7 | C | wbm | — |
| M16.17 | 🎨 | L'image d'une figure par une suite d'applications affines du plan, en coordonnées homogènes | ★ | 15 | §2 | C, E | manuel | M16.12 |
| M16.18 | 🐛 | Chasse à l'erreur : une matrice homogène écrite pour des colonnes et appliquée à des lignes, Var(XY) = Var X · Var Y, et (I − A)⁻¹ sur un graphe qui a un cycle | ★ | 15 | §1 §4 §5 | C, E | wbm | — |
| M16.19 | 🛠️ | Un test de propriété : la matrice homogène d'une composée est le produit des matrices homogènes | ★ | 15 | §2 | C | manuel | M16.12 |
| M16.20 | 🏆 | Défi : la loi du produit de deux uniformes indépendantes, sa densité et ses deux premiers moments | ★★★ | 25 | §5 | C | wbm | — |

*Notes* : Frontières : les ∂ 16.6 (la symétrie des neurones jumeaux) et 16.7 (retrouver LeCun, Glorot et He), 16.1 (compter les paramètres d'un MLP), 16.2 (une passe avant 2-2-1), 16.3 (formes et diffusion d'un mini-batch), 16.4 (Kahn à la main, compter les ordres topologiques), 16.8 (Fermi d'un MLP pour MNIST), 16.Q10 (écarts-types de LeCun, Glorot et He), 16.15 (hauteurs de densité), 16.19 (jumeaux sur un XOR), 16.23 (profils d'écart-type sur 20 couches), 17.1 (la couche équivalente d'un réseau linéaire) et le ∂ 17.3 (une composée d'affines est affine, sa matrice et son biais, la caractérisation des fonctions affines, le nombre de morceaux d'un réseau ReLU). M16 enseigne les outils hors réseau. Les applications affines sont des transformations du plan et de l'espace (rotations, homothéties, translations) ; que la composée de deux applications affines soit affine est énoncé (M12a l'énonçait aussi ; ∂ 17.3.1 le démontre) et calculé en coordonnées homogènes, sans formule générale du biais équivalent d'une suite de couches. Les graphes sont des rues à sens unique, des tâches et des prérequis, lus sur leur matrice d'adjacence (chemins comptés par Aᵏ, sans cycle ⇔ nilpotente ⇔ numérotation triangulaire, somme sur les chemins, qui prépare la règle de la chaîne de M18), sans l'algorithme de Kahn ni `graphlib` (la fiche de workbookIA 16 et `mylearn.nn.layers.topological_order`). La variance d'un produit est prise avec des moyennes non nulles (un prix fois une quantité), la décorrélation de produits εᵢ xᵢ (εᵢ centrés, indépendants de mesures xᵢ corrélées) sur des signes aléatoires, sans poids, fan-in, ni variance réglée pour se conserver d'une couche à l'autre : le §6 énonce ce lemme sans le démontrer (c'est la première étape de ∂ 16.7.1, et l'encadré de la fiche 16 l'énonce aussi), et M16.6 prend des Var(εᵢ) et des E[xᵢ²] différents, pour que le résultat ne soit pas n Var(ε) E[x²] ; la croissance gᴸ sur une chaîne d'amplificateurs bruités. « Décorrélées sans être indépendantes » n'est pas un 🗣️ (workbookIA 2.E4, frontière de M02c). M16.10 reste sur l'algèbre de X W + 1bᵀ, sans piège de forme du biais (16.3, 16.20) ; M16.18 n'est pas un `a @ W.T` (16.20) ; M16.19 vérifie sur des images de points (f₂(f₁(x)) contre [x, 1] H₁ H₂), sans former W₁W₂ ni b₁W₂ + b₂. Le moment d'ordre 2 d'une variable rectifiée n'est pas traité (∂ 16.7.3). La variance de la loi uniforme est connue (M02b, (b − a)²/12). Évités (règle de partage) : les réseaux et graphes de workbookIA 16 (3-4-4-2, 784-…, 10-8-6-3, 1000-500-100-10, A → C …, U → A …, P, Q, R, S, T, x, h1, h2, y), les matrices de sa fiche et de 16.2, 16.13 et 16.17, les neurones R, G, B, les lois 𝒰(±0,05), 𝒰(±0,1), 𝒰(±0,2) et 𝒩(0 ; 0,1²), les couches 300 × 300, 400 × 100, 600 × 400 et 200 × 200, les gains 1,25, 0,8, 1,5 et 0,5 sur 9, 10, 20 ou 30 étages, le DAG à 4 nœuds et 6 arêtes, la chaîne d'usine, le parquet et l'effet Larsen. Conventions de workbookIA suivies : vecteurs en lignes, W de forme (n_in, n_out), x W + b, avec le passage à W x + b de MML par transposition ; « degré entrant » est le fan-in de workbookIA. Le Hadamard annoncé par M09a sert aux multiplicateurs aléatoires (§6). `affine` : NumPy permis, pas `matrix_power`, `inv` ni `solve` dans `sum_over_paths`. 8 h comme prévu au §8 : pas de 📖 (MML §6.4 a été lu en M02b et M02c) ni de 🧮.

<a id="m17"></a>
## M17 · Jacobienne et règle de la chaîne

**Partie** IV · **prépare** workbookIA 17 · **dossier** `chapitres/m17_jacobienne/` · **MML** §5.3 · **sessions de génération** 1

La dérivée d'une application de ℝⁿ dans ℝᵐ : la jacobienne (une ligne par sortie, une colonne par entrée), diagonale pour une fonction appliquée coordonnée par coordonnée, la règle de la chaîne comme produit de jacobiennes, les deux conventions de gradient (en ligne pour MML, de la forme de la variable pour NumPy), les produits jacobienne-vecteur et vecteur-jacobienne qui évitent de former la matrice ; puis les fonctions définies par morceaux et les longues compositions, dont la dérivée est un produit de dérivées, et la loi de Boltzmann (translation des énergies, température), dont la matrice diag(p) − ppᵀ est la covariance d'un vecteur one-hot. workbookIA 17 applique ces outils aux activations et à la softmax.

**Temps** : 10,2 h en parcours complet, 7,2 h en parcours essentiel (lecture 130 min, 16 flashcards).

**Objectifs**

- Calculer la jacobienne d'une application de ℝⁿ dans ℝᵐ, et s'en servir comme approximation linéaire.
- Reconnaître une jacobienne diagonale, et la calculer avec une seule paire d'évaluations.
- Dériver une composée par le produit des jacobiennes, dans le bon ordre et avec les bonnes formes.
- Passer du gradient en ligne de MML au gradient de la forme de la variable de NumPy.
- Calculer un produit jacobienne-vecteur ou vecteur-jacobienne sans former la jacobienne.
- Dériver une fonction définie par morceaux, et suivre la dérivée d'une longue composition.
- Calculer une loi de Boltzmann et ses limites en température, et la covariance diag(p) − ppᵀ d'un vecteur one-hot.

**Sections de la fiche**

- §1 La jacobienne d'une application de ℝⁿ dans ℝᵐ
- §2 Fonctions appliquées coordonnée par coordonnée : une jacobienne diagonale
- §3 La règle de la chaîne : un produit de jacobiennes
- §4 Gradient en ligne ou de la forme de la variable
- §5 Produits jacobienne-vecteur et vecteur-jacobienne
- §6 Fonctions définies par morceaux et longues compositions
- §7 La loi de Boltzmann et la matrice diag(p) − ppᵀ

**Notions enseignées** : jacobienne (lignes = sorties, colonnes = entrées) · approximation linéaire d'une application de ℝⁿ dans ℝᵐ · jacobienne diagonale d'une fonction appliquée coordonnée par coordonnée, et produit de Hadamard · règle de la chaîne multivariée : J_{g∘f} = J_g J_f, somme sur les variables intermédiaires · gradient en ligne (MML) et gradient de la forme de la variable (NumPy) : ∇(L∘f) = J_fᵀ ∇L · produit jacobienne-vecteur, produit vecteur-jacobienne · dérivées à gauche et à droite, fonctions affines par morceaux · saturation : une dérivée qui tend vers 0 loin de l'origine (arctan′) · dérivée d'une longue composition : un produit de dérivées, qui s'éteint ou explose · loi de Boltzmann : invariance par translation des énergies, limites en température · matrice diag(p) − ppᵀ : covariance d'un vecteur one-hot, symétrique, semi-définie positive, noyau contenant 1

**Prérequis** : dérivées partielles, gradient (vecteur ligne), dérivée directionnelle (M05b) · règle de la chaîne en une variable, dérivées usuelles, |x| et max(0, x) (R7) · exponentielle, logarithme, tanh (R6) · produit matriciel et formes, produit de Hadamard, transposée (M09a) · matrice d'une application linéaire, composition (M12a) · matrices semi-définies positives, valeurs propres, déterminant (M12c) · matrice de covariance (M02c) · loi catégorielle (M02b) · vecteurs one-hot et base canonique (M07) · softmax de trois scores, log-sum-exp, différences finies centrées (M05a) · sous-gradient, un maximum de fonctions affines est convexe (M13b) · applications affines, coordonnées homogènes (M16)

**mymath** : `jacobian.py` (signatures figées) : `numerical_jacobian`, `diagonal_jacobian`, `jacobian_vector_product`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 17.3 ∂ Une composition d'affines reste affine ; une ReLU casse tout · 17.4 ∂ Dériver la sigmoïde, tanh et softplus · 17.7 ∂ La Jacobienne de la softmax · 17.1 ✏️ Effondrer un réseau linéaire en un seul neurone · 17.2 ✏️ Tableau de valeurs de neuf activations · 17.5 ✏️ Maxout et ReLU : construire |x|, une cuvette et une bosse · 17.6 ✏️ Softmax à la main : translation, température, rapports · 17.8 🧮 Fermi : une activation coûte-t-elle cher face au produit matriciel ? · 17.16 🔨 La Jacobienne de la softmax en NumPy · 17.19 🔮 Softmax et température : prédire la distribution · 17.21 📈 Diagnostiquer la saturation sur des histogrammes de pré-activations · 17.23 🔬 Produit des dérivées sur 10 couches : sigmoïde, tanh, ReLU, GELU · 17.Q11 🧠 Softmax : somme à 1, ordre conservé, mais pas une activation · 17.Q12 🧠 Vrai ou faux : des scores 0,6 / 0,3 / 0,1 se lisent comme des probabilités

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M17.Q1 | 🧠 | La forme d'une jacobienne | ★ | 4 | §1 | C, E | manuel | — |
| M17.Q2 | 🧠 | Diagonale ou pleine ? | ★ | 4 | §2 | C, E | manuel | — |
| M17.Q3 | 🧠 | Dans quel ordre multiplier les jacobiennes ? | ★ | 4 | §3 | C, E | manuel | — |
| M17.Q4 | 🧠 | Gradient en ligne ou de la forme de la variable | ★ | 4 | §4 | C, E | manuel | — |
| M17.Q5 | 🧠 | Jacobienne-vecteur ou vecteur-jacobienne : combien d'opérations ? | ★ | 4 | §5 | C | manuel | — |
| M17.Q6 | 🧠 | La loi de Boltzmann : populations relatives et énergie moyenne | ★ | 4 | §7 | C, E | manuel | — |
| M17.R1 | 🔁 | Dérivées partielles et gradient (M05b) | ★ | 5 | §1 | C, E | manuel | — |
| M17.R2 | 🔁 | La règle de la chaîne en une variable (R7) | ★ | 5 | §3 | C, E | manuel | — |
| M17.R3 | 🔁 | La matrice de covariance (M02c) | ★ | 5 | §7 | C | manuel | — |
| M17.1 | ✏️ | La jacobienne des coordonnées polaires, son déterminant, et l'approximation linéaire près d'un point | ★ | 15 | §1 | C, E | wbm | — |
| M17.2 | ✏️ | Une fonction appliquée coordonnée par coordonnée : la jacobienne diagonale, et son produit par un vecteur | ★ | 15 | §2 | C, E | wbm | — |
| M17.3 | ✏️ | Dériver une composée de trois applications par le produit de leurs jacobiennes | ★★ | 20 | §3 | C, E | wbm | — |
| M17.4 | ✏️ | La normalisation x/‖x‖ : sa jacobienne (I − uuᵀ)/‖x‖, et la direction qu'elle écrase | ★★ | 20 | §3 §5 | C | wbm | — |
| M17.5 | ✏️ | Le gradient d'une fonction scalaire d'une composée, dans les deux conventions : J_fᵀ ∇L | ★ | 15 | §4 | C, E | wbm | — |
| M17.6 | ✏️ | Dérivées à gauche et à droite d'une fonction définie par morceaux, et la dérivée d'une composée de sept copies d'une fonction lisse | ★★ | 15 | §6 | C, E | wbm | — |
| M17.7 | ✏️ | Une loi de Boltzmann à quatre niveaux d'énergie : rapports de populations, énergie moyenne, et la température où le niveau fondamental garde la moitié | ★★ | 15 | §7 | C, E | wbm | — |
| M17.8 | ∂ | La règle de la chaîne pour des applications de ℝⁿ dans ℝᵐ, à partir de l'approximation linéaire | ★★★ | 20 | §3 | C, E | manuel | — |
| M17.9 | ∂ | Une fonction appliquée coordonnée par coordonnée a une jacobienne diagonale, et J v = g′(x) ⊙ v | ★ | 15 | §2 | C | manuel | — |
| M17.10 | ∂ | diag(p) − ppᵀ est la covariance d'un vecteur one-hot : symétrique, semi-définie positive, de noyau contenant 1 | ★★ | 20 | §7 | C, E | manuel | — |
| M17.11 | ✏️ | Le recuit simulé : une loi de Boltzmann sur cinq configurations, dont on baisse la température | ★★ | 15 | §7 | C | wbm | — |
| M17.12 | 📖 | MML §5.3 : gradients de fonctions à valeurs vectorielles, en anglais | ★★ | 35 | §1 §3 §4 | C | manuel | — |
| M17.13 | 🗣️ | Expliquer la règle de la chaîne multivariée avec des taux de change entre monnaies | ★ | 10 | §3 | C, E | manuel | — |
| M17.E1 | 💼 | « Qu'est-ce qu'une jacobienne ? Donne un exemple hors du machine learning. » | ★ | 10 | §1 §5 | C | manuel | — |
| M17.14 | 🔨 | La jacobienne par différences centrées, colonne par colonne · `numerical_jacobian` | ★★ | 20 | §1 | C, E | pytest | — |
| M17.15 | 🔨 | Une jacobienne diagonale avec une seule paire d'évaluations · `diagonal_jacobian` | ★ | 15 | §2 | C, E | pytest | M17.14 |
| M17.16 | 🔨 | Un produit jacobienne-vecteur sans former la jacobienne · `jacobian_vector_product` | ★ | 15 | §5 | C | pytest | M17.14 |
| M17.17 | 📦 | `sympy.Matrix.jacobian` et `scipy.differentiate.jacobian` contre ta jacobienne numérique | ★ | 15 | §1 §3 | C, E | wbm | M17.14 |
| M17.18 | 🔮 | Prédire la forme et les zéros de la jacobienne d'une composée, puis vérifier | ★ | 10 | §3 | C, E | wbm | — |
| M17.19 | 🔬 | Une longue composition : une dérivée qui s'éteint ou explose selon la pente au point fixe | ★★ | 20 | §6 | C | wbm | — |
| M17.20 | 🎨 | Une grille du plan déformée par une application non linéaire, et par son approximation linéaire | ★ | 20 | §1 | C, E | manuel | — |
| M17.21 | 🐛 | Chasse à l'erreur : une jacobienne transposée, un produit dans le mauvais ordre, une jacobienne évaluée au mauvais point | ★ | 15 | §3 §4 | C, E | wbm | — |
| M17.22 | 🛠️ | Un test de propriété : J_{g∘f} = J_g J_f sur des applications tirées au hasard | ★ | 15 | §3 | C | manuel | M17.14 |
| M17.23 | 🏆 | Défi : la jacobienne de l'inversion X ↦ X⁻¹, vue comme une application de ℝ^{n²} dans ℝ^{n²} | ★★★ | 25 | §3 §5 | C | wbm | — |

*Notes* : Frontières : les ∂ 17.3 (composée d'affines), 17.4 (dérivées de la sigmoïde, de tanh, de softplus et de SiLU) et 17.7 (la jacobienne de la softmax), 17.1, 17.2 (valeurs de neuf activations), 17.5 (maxout, cuvette et bosse), 17.6 (softmax à la main), 17.8 (Fermi d'une activation), 17.16 (la jacobienne de la softmax en NumPy), 17.19 (température et entropie), 17.21 (saturation sur des histogrammes), 17.23 (produit des dérivées sur 10 couches), 17.Q11 et 17.Q12 (softmax translatée, dilatée, rapports). M17 n'écrit ni ne dérive aucune activation de `mylearn` (ReLU et ses variantes, marches, sigmoïde, tanh, softplus, ELU, SiLU, GELU, softmax) : ses exemples sont les coordonnées polaires et sphériques, la normalisation x/‖x‖, arctan, t³, sin, cos, et l'itération de cos. La règle de la chaîne multivariée (forme jacobienne) est ici et non en M18, car workbookIA 17 s'en sert (∂ 17.7.4, 🔬 17.23), comme l'annonçait M05b. La loi de Boltzmann est celle de la physique (niveaux d'énergie, température) : la fiche en énonce l'invariance par translation des énergies et les limites T → 0 et T → ∞, sans logits, scores ni classes, et sans la dériver ; ses exercices posent des questions de physique (rapports de populations e^{−ΔE/T}, énergie moyenne et ses limites, température où le niveau fondamental garde la moitié, recuit simulé), jamais la suite « tout décaler, refroidir, chauffer » de 17.6, ni un vrai ou faux de translation et de dilatation (17.Q11, 17.Q12), ni un agent qui choisit ses actions (workbookIA 26) ; la matrice diag(p) − ppᵀ y est étudiée comme la covariance d'un vecteur one-hot (symétrique, semi-définie positive, de noyau contenant 1, de rang K − 1 quand tous les pᵢ sont > 0), ce qui tient la note de M13a sans faire ∂ 17.7 : p est une ligne et la matrice s'écrit diag(p) − pᵀp (convention de workbookIA), et aucune solution ne calcule (diag(p) − pᵀp) v = p ⊙ (v − p · v) (∂ 17.7.6). M17.4 (la jacobienne de x/‖x‖) ne fait aucun lien avec la standardisation ni avec le centrage (∂ 20.8). Les produits de dérivées d'une longue composition sont pris sur des itérations de point fixe d'une variable, sans le facteur 1/4 ni (1/4)ᴸ (CP4.5 de workbookIA), sans dix copies ou dix couches (🔬 17.23, L = 10 de CP4.5), sans demander si une composée de fonctions affines par morceaux l'est encore ni compter ses morceaux (∂ 17.3.5–6), et sans la phrase « calculer en z, pas en a ». Évités : 47A + 6B + 61C, h = (2x + 1, −x + 3) et 4x − 4,5, les points ln 2, ln 3 et ln 4, les scores et températures de 17.6, 17.12 et 17.19, les vecteurs p = (0,1 ; 0,9) et (1/6, 1/3, 1/2), K = 50 000, les limites 709,78 et 88,7, les escaliers ⌊4z⌋/4 et ⌊5z⌋/5, le train articulé et l'origami ; 💼 M17.E1 ne prend pas la softmax ni K = 50 000 comme exemple (∂ 17.7.6). Conventions : jacobienne à une ligne par sortie et une colonne par entrée (MML §5.3, comme workbookIA) ; gradient en ligne chez MML (M05b) et de la forme de la variable dans NumPy, les deux écrits ; vecteurs en lignes pour x W + b. `jacobian` : NumPy permis, pas SymPy ni `scipy.differentiate`. Parcours essentiel : la jacobienne diagonale démontrée hors parcours.

<a id="m18"></a>
## M18 · Différentiation automatique et calcul matriciel

**Partie** IV · **prépare** workbookIA 18 · **dossier** `chapitres/m18_retropropagation/` · **MML** §5.4, §5.5, §5.6 · **sessions de génération** 1

Dériver un calcul entier : le graphe de calcul d'une formule et la règle de la chaîne comme somme sur les chemins, le mode direct par les nombres duaux, le mode inverse par des adjoints accumulés dans l'ordre inverse, et ce que coûte chaque mode ; puis les gradients par rapport à un vecteur et à une matrice (de la forme de la variable), la différentielle df = tr(Gᵀ dX), les identités de MML §5.5 (traces, formes bilinéaires, log det), le gradient d'une moyenne, et la vérification d'un gradient matriciel par différences centrées. workbookIA 18 en fait la rétropropagation.

**Temps** : 14,6 h en parcours complet, 8,9 h en parcours essentiel (lecture 160 min, 22 flashcards).

**Objectifs**

- Écrire le graphe de calcul d'une formule, et dériver sa sortie par la somme, sur les chemins, des produits des dérivées locales.
- Propager à la main des dérivées en mode direct (nombres duaux) et des adjoints en mode inverse.
- Choisir le mode selon le nombre d'entrées et de sorties, et en estimer le coût.
- Calculer le gradient d'une fonction d'une matrice, de la forme de cette matrice, par les coordonnées puis par la différentielle.
- Dériver une moyenne de fonctions, et vérifier un gradient matriciel par différences centrées.

**Sections de la fiche**

- §1 Le graphe de calcul d'une formule
- §2 La règle de la chaîne sur un graphe : une somme sur les chemins
- §3 Le mode direct : les nombres duaux
- §4 Le mode inverse : des adjoints, dans l'ordre inverse
- §5 Ce que coûte chaque mode
- §6 Gradients par rapport à une matrice : la forme de la variable
- §7 Les identités du calcul matriciel : traces, formes bilinéaires, log det
- §8 Le gradient d'une moyenne, et vérifier un gradient matriciel

**Notions enseignées** : graphe de calcul d'une formule, variables intermédiaires · règle de la chaîne sur un graphe : somme sur les chemins des produits des dérivées locales · mode direct : nombres duaux a + bε, ε² = 0 · mode inverse : adjoints, ordre inverse, accumulation sur les chemins · coût des modes direct et inverse selon les nombres d'entrées et de sorties ; principe du gradient bon marché · gradient par rapport à un vecteur et à une matrice : la convention de la forme de la variable · différentielle d'une fonction de matrice : df = tr(Gᵀ dX) · identités : ∇ aᵀXb, ∇ tr(AX), ∇ tr(XᵀAX), ∇ ‖X‖²_F, ∇ log det X · comatrice : X com(X)ᵀ = det X · I (énoncée) · gradient d'une moyenne = moyenne des gradients · vérifier un gradient matriciel par différences centrées

**Prérequis** : règle de la chaîne multivariée, jacobiennes, produits jacobienne-vecteur et vecteur-jacobienne (M17) · gradient en ligne et gradient de la forme de la variable (M17) · somme sur les chemins d'un graphe sans cycle, numérotation triangulaire (M16) · gradients de aᵀw et wᵀAw (M09b) · trace, déterminant, tr(A x xᵀ) (M12c) · différences finies centrées, erreur relative, choix du pas (M05a) · gradient, dérivée directionnelle (M05b) · produit de Hadamard, transposée (M09a) · centroïde : la moyenne minimise la somme des carrés des distances (M07) · classes Python et surcharge d'opérateurs (IA:0A)

**mymath** : `autodiff.py` (signatures figées) : `Dual`, `dual_derivative`, `forward_gradient`, `gradient_from_differential`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 18.6 ∂ La règle de la chaîne derrière les deltas · 18.7 ∂ Forme matricielle : XᵀΔ, ΔWᵀ et somme des lignes · 18.8 ∂ Softmax et cross-entropy : le gradient vaut p − y · 18.1 ✏️ Le delta, amplificateur de changement · 18.2 ✏️ Deltas de sortie avec l'erreur quadratique : attention au signe · 18.3 ✏️ Descente sur une parabole : quel learning rate ? · 18.4 ✏️ Rétropropagation complète du réseau minuscule, sans activation · 18.5 ✏️ Le même réseau avec une sigmoïde cachée : le facteur σ'(z) · 18.9 🧮 Fermi : rétropropagation contre force brute · 18.14 🔨 Cross-entropies calculées sur les logits (binaire et softmax) · 18.15 🔨 dense_backward : les trois gradients d'une couche · 18.16 🔨 gradient_check : vérifier un gradient par différences finies · 18.17 🐛 Chasse au bug : trois gradients faux démasqués · 18.26 🔨 Micro-autograd : la classe Value · 18.27 🔮 À la main, Value, mlp_backward, différences finies : quatre gradients identiques ? · 18.Q2 🧠 Perturber un poids au hasard : pourquoi est-ce si lent ? · 18.E2 💼 Pourquoi la rétropropagation bat-elle les différences finies ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M18.Q1 | 🧠 | Lire un graphe de calcul : nœuds, arêtes, ordre d'évaluation | ★ | 4 | §1 | C, E | manuel | — |
| M18.Q2 | 🧠 | Combien de chemins, et quelle somme ? | ★ | 4 | §2 | C, E | manuel | — |
| M18.Q3 | 🧠 | Calculer avec ε² = 0 | ★ | 4 | §3 | C, E | manuel | — |
| M18.Q4 | 🧠 | Le mode inverse : dans quel ordre visiter les nœuds ? | ★ | 4 | §4 | C, E | manuel | — |
| M18.Q5 | 🧠 | Direct ou inverse, pour n entrées et m sorties ? | ★ | 4 | §5 | C, E | manuel | — |
| M18.Q6 | 🧠 | La forme d'un gradient par rapport à une matrice | ★ | 4 | §6 | C, E | manuel | — |
| M18.Q7 | 🧠 | Identités de trace : vrai ou faux | ★ | 4 | §7 | C | manuel | — |
| M18.Q8 | 🧠 | Gradient d'une moyenne, moyenne des gradients | ★ | 4 | §8 | C, E | manuel | — |
| M18.R1 | 🔁 | La jacobienne d'une composée (M17) | ★ | 5 | §2 | C, E | manuel | — |
| M18.R2 | 🔁 | Le gradient de wᵀAw (M09b) | ★ | 5 | §7 | C, E | manuel | — |
| M18.R3 | 🔁 | Différences centrées et choix du pas (M05a) | ★ | 5 | §8 | C | manuel | — |
| M18.1 | ✏️ | Le graphe de calcul d'une formule de physique, et l'ordre de ses calculs | ★ | 15 | §1 | C, E | wbm | — |
| M18.2 | ✏️ | Dériver par la somme sur les chemins : une variable qui sert deux fois | ★★ | 20 | §2 | C, E | wbm | — |
| M18.3 | ✏️ | Le mode direct à la main : des nombres duaux sur une fonction de deux variables | ★★ | 20 | §3 | C, E | wbm | — |
| M18.4 | ✏️ | Le mode inverse à la main : les adjoints d'un graphe de six nœuds | ★★ | 20 | §4 | C, E | wbm | — |
| M18.5 | ✏️ | Le même gradient par les deux modes, et le compte des opérations | ★★ | 20 | §3 §4 §5 | C, E | wbm | — |
| M18.6 | ✏️ | Le gradient de aᵀXb, de la forme de X | ★ | 15 | §6 | C, E | wbm | — |
| M18.7 | ✏️ | Les gradients de tr(AX) et de tr(XᵀAX), coordonnée par coordonnée | ★★ | 20 | §7 | C, E | wbm | — |
| M18.8 | ✏️ | Le gradient de log det X sur une matrice 2 × 2, à la main puis par la formule | ★★ | 20 | §7 | C | wbm | — |
| M18.9 | ✏️ | Le gradient d'une moyenne de distances : le point qui minimise la somme des distances à des villes | ★★ | 15 | §8 | C, E | wbm | — |
| M18.10 | ✏️ | La différentielle d'une fonction de matrice, df = tr(Gᵀ dX), et le gradient G qu'on y lit | ★★ | 20 | §6 §7 | C | wbm | — |
| M18.11 | ∂ | La règle de la chaîne sur un graphe sans cycle : la somme sur les chemins, nœud par nœud dans l'ordre de la numérotation | ★★ | 20 | §2 | C, E | manuel | — |
| M18.12 | ∂ | Les nombres duaux calculent la dérivée : f(a + bε) = f(a) + b f′(a) ε, pour les sommes, les produits et les composées | ★★ | 20 | §3 | C, E | manuel | — |
| M18.13 | ∂ | Le mode inverse calcule tout le gradient en un passage : l'adjoint d'un nœud est la somme, sur ses successeurs, des adjoints fois les dérivées locales | ★★★ | 20 | §4 | C | manuel | — |
| M18.14 | ∂ | ∇ log det X = X⁻ᵀ, par le développement du déterminant selon une ligne | ★★★ | 20 | §7 | C | manuel | — |
| M18.15 | 🔗 | Pont : workbookIA 18 programme le mode inverse ; pour une simulation de ℝ²⁰⁰⁰ dans ℝ³, combien de passages dans chaque mode ? | ★ | 15 | §5 | C, E | wbm | — |
| M18.16 | 🔗 | Pont : de la convention de MML (gradient en ligne) à celle de NumPy et des bibliothèques de deep learning | ★ | 15 | §6 | C | wbm | — |
| M18.17 | 📖 | MML §5.4 et §5.5 : gradients par rapport à des matrices et identités utiles, en anglais | ★★ | 40 | §6 §7 | C | manuel | — |
| M18.18 | 📖 | MML §5.6 : rétropropagation et différentiation automatique, en anglais | ★★ | 35 | §1 §2 §4 §5 | C | manuel | — |
| M18.19 | 🗣️ | Expliquer le mode inverse à quelqu'un qui connaît la règle de la chaîne en une variable | ★ | 10 | §4 | C, E | manuel | — |
| M18.E1 | 💼 | « Différentiation automatique, symbolique ou numérique : quelles différences ? » | ★ | 10 | §3 §4 §5 | C | manuel | — |
| M18.E2 | 💼 | « Quand le mode direct est-il préférable au mode inverse ? » | ★ | 10 | §5 | C | manuel | — |
| M18.20 | 🔨 | Les nombres duaux : la classe `Dual`, et la dérivée d'une fonction d'une variable · `Dual, dual_derivative` | ★★ | 45 | §3 | C, E | pytest | — |
| M18.21 | 🔨 | Le gradient en mode direct : n passages avec des nombres duaux · `forward_gradient` | ★ | 20 | §3 §5 | C | pytest | M18.20 |
| M18.22 | 🔨 | Lire le gradient dans la différentielle : G[i, j] = df(E_ij), de la forme de la variable · `gradient_from_differential` | ★ | 15 | §6 §7 | C, E | pytest | — |
| M18.23 | 📦 | SymPy : dériver une fonction de matrice symbolique, et comparer aux identités | ★ | 25 | §7 | C | wbm | — |
| M18.24 | 🔮 | Prédire le nombre d'opérations de chaque mode, puis le compter | ★ | 10 | §5 | C, E | wbm | M18.20 |
| M18.25 | 🔬 | Différences finies contre nombres duaux : l'erreur selon le pas h | ★★ | 20 | §3 §8 | C | wbm | M18.20 |
| M18.26 | 🎨 | Dessiner un graphe de calcul, avec les dérivées locales sur les arêtes et les adjoints sur les nœuds | ★ | 30 | §1 §4 | C | manuel | — |
| M18.27 | 🐛 | Chasse à l'erreur : un gradient transposé, un adjoint compté sur un seul chemin, un pas h trop petit | ★ | 15 | §4 §6 §8 | C, E | wbm | — |
| M18.28 | 🛠️ | Tester une classe par ses propriétés : distributivité et dérivées connues des nombres duaux | ★ | 15 | §3 | C | manuel | M18.20 |
| M18.29 | 🏆 | Défi : dériver une boucle, la méthode de Newton pour √a, en mode direct | ★★★ | 30 | §3 | C | wbm | M18.20 |

*Notes* : Frontières : les ∂ 18.6 (les deltas), 18.7 (XᵀΔ, ΔWᵀ, la somme des lignes, la moyenne des gradients d'exemples) et 18.8 (le gradient p − y), 18.1, 18.2, 18.3 (la parabole et le learning rate), 18.4 et 18.5 (le réseau minuscule à la main), 18.9 (Fermi), 18.14 (les cross-entropies sur les logits), 18.15 (`dense_backward`), 18.16 (`gradient_check`), 18.17 (les erreurs relatives 1/3, 1 et 5/7), 18.26 (`Value`), 18.27, 18.Q2 (un million de poids, un million de passes) et 18.E2 (pourquoi pas des différences finies poids par poids) : le coût des modes se compare sur des fonctions de ℝⁿ dans ℝᵐ (simulations, formules), jamais sur un « modèle » et ses « paramètres ». M18 dérive des formules de physique, de géométrie et d'algèbre linéaire, jamais un réseau ni une loss de classification : pas de delta, ni de « ce qui entre fois le delta », ni de règle générale ∂L/∂W = Xᵀ ∂L/∂Z. La somme sur les chemins prolonge celle de M16 (des dérivées locales sur les arêtes). Le mode inverse est fait à la main sur des graphes de formules et démontré en général (les adjoints), et seul le mode direct est programmé (`Dual`, sans `backward` : `mylearn.Value` est le mode inverse de workbookIA 18) ; ses exemples ne reprennent ni ab + a en (2, −3), ni x² + 2x en 3, ni tanh(x³ − 4x) en 2, ni (ab + c)a en (3, −1, 4), ni `multiplier(2)`. Le coût des deux modes est énoncé par le principe du gradient bon marché (Baur et Strassen), sans « deux passes avant » ni 2P passes. Les identités sont celles de MML §5.5 (traces, aᵀXb, log det), sans ‖XW − Y‖² ni ‖Xw − y‖² (M09b, ∂ 18.7) ; la moyenne des gradients est faite sur des fonctions quelconques (la médiane géométrique de villes), sans le contre-exemple de la moyenne des produits (∂ 18.7.5). Le 🔨 matriciel lit le gradient dans la différentielle (G[i, j] = df(E_ij)) : le gradient numérique d'un tableau est `mylearn.calculus.numerical_gradient` de workbookIA 5, à ne pas réécrire ; la vérification d'un gradient matriciel se fait par une dérivée le long d'une direction H comparée à tr(GᵀH) (la fonction de M05b, ou deux évaluations), sans l'erreur relative de `gradient_check` (M05a.28 l'a déjà ; ni les seuils 10⁻⁷ et 10⁻³, ni |k − 1|/(k + 1)), ni la matrice [[1, −2], [0,5, 3]] (🔨 19.16). ∇ log det X = X⁻ᵀ (M18.14) s'appuie sur X com(X)ᵀ = det X · I, énoncé au §7. Le 🐛 M18.27 corrige un calcul d'adjoints écrit ligne à ligne pour une formule donnée, sans classe ni graphe générique (le `+=` de `Value`, 🔨 18.26). La descente sur une parabole (encadré et 18.3 de workbookIA) n'est pas traitée : M19 étudie la convergence des itérations. Évités aussi : la loss quadratique et ses deltas (0,6 ; −1,2), E(o) = (o − 2)², les logits (2 ; 0 ; −1), z = 3, 5, 40 et 1 000, le réseau 2-2-4-3-2, les lunes, Karpathy et les dates 1970 et 1986. Conventions : gradient de la forme de la variable (NumPy, PyTorch), écrit à côté de la convention en ligne de MML ; df = tr(Gᵀ dX). `autodiff` : `math` et NumPy permis, pas SymPy. Pour le 📦 M18.23 : `sympy.MatrixSymbol` dérive tr(AX), tr(XᵀAX) et aᵀXb (sans indexer [0, 0]), mais rend 0 pour log det X (SymPy 1.14) : passer alors par une matrice de symboles 2 × 2. Parcours essentiel : log det et la démonstration du mode inverse hors parcours.

<a id="m19"></a>
## M19 · Hessienne, conditionnement et convergence

**Partie** IV · **prépare** workbookIA 19 · **dossier** `chapitres/m19_hessienne_convergence/` · **MML** §5.7, §5.8, §7.1 · **sessions de génération** 1

La courbure d'une fonction de n variables, puis la convergence des méthodes itératives : la hessienne et Taylor d'ordre 2, la nature d'un point critique par les signes des valeurs propres ; les itérations linéaires x ← M x + c, qui convergent quand toutes les valeurs propres de M (symétrique) sont de module < 1 ; l'itération de Richardson pour un système A x = b, son pas critique 2/λmax, le conditionnement qui fixe la vitesse et le préconditionnement diagonal ; les récurrences linéaires d'ordre 2 et le module de leurs racines (le strict minimum sur les nombres complexes) ; un gradient estimé sans biais sur un échantillon ; la projection sur une boule et sur un pavé. workbookIA 19 en tire le learning rate critique, le momentum, les pas adaptatifs et le clipping.

**Temps** : 14,2 h en parcours complet, 9,8 h en parcours essentiel (lecture 160 min, 22 flashcards).

**Objectifs**

- Calculer une hessienne, écrire le développement de Taylor d'ordre 2, et classer un point critique de ℝⁿ par les signes des valeurs propres de la hessienne.
- Décider de la convergence d'une itération linéaire x ← M x + c par les valeurs propres de M symétrique.
- Choisir le pas de l'itération de Richardson pour un système à matrice symétrique définie positive, et prévoir le nombre d'itérations par le conditionnement.
- Préconditionner un système par une matrice diagonale.
- Résoudre une récurrence linéaire d'ordre 2, et décider de sa convergence par le module des racines de son polynôme caractéristique.
- Montrer qu'un gradient estimé sur un échantillon tiré au hasard est sans biais, et calculer sa variance.
- Projeter un vecteur sur une boule et sur un pavé, et comparer les directions obtenues.

**Sections de la fiche**

- §1 La hessienne et Taylor d'ordre 2 en n variables
- §2 Points critiques en dimension n : les signes des valeurs propres
- §3 Itérations linéaires : quand convergent-elles ?
- §4 L'itération de Richardson et le pas critique 2/λmax
- §5 Conditionnement, vitesse et préconditionnement diagonal
- §6 Récurrences linéaires d'ordre 2 et module des racines
- §7 Un gradient estimé sur un échantillon : sans biais, et sa variance
- §8 Projeter sur une boule ou sur un pavé

**Notions enseignées** : hessienne d'une fonction de n variables, symétrique (Schwarz, admis) · Taylor d'ordre 2 à plusieurs variables · nature d'un point critique par les valeurs propres de la hessienne (minimum, maximum, selle, direction plate) · itération linéaire x ← M x + c : point fixe, erreur eₖ₊₁ = M eₖ · convergence pour M symétrique : toutes les valeurs propres de module < 1, vitesse max |λ| · itération de Richardson pour A x = b (A symétrique définie positive) : 0 < ω < 2/λmax · conditionnement κ = λmax/λmin et nombre d'itérations ; pas optimal et facteur (κ − 1)/(κ + 1) (énoncés) · préconditionnement diagonal (Jacobi) · fonctions de courbure bornée (valeurs propres de la hessienne dans [μ, L]) : le pas sous 2/L (énoncé) · récurrence linéaire d'ordre 2 : polynôme caractéristique, matrice compagnon · nombres complexes (rappel de M12c §3) : module d'un produit, forme trigonométrique, somme et produit des racines complexes d'un trinôme réel · convergence d'une récurrence d'ordre 2 : |q| < 1 et |p| < 1 + q · gradient sur un échantillon : estimateur sans biais, variance en 1/B · projection sur une boule (direction gardée) et sur un pavé (direction changée)

**Prérequis** : dérivées partielles secondes, points critiques en dimension 2 (M05b) · Taylor en une variable, choix du pas des différences finies (M05a) · valeurs propres, théorème spectral, formes quadratiques, définie positive, hessienne et convexité, le strict minimum sur les nombres complexes (M12c) · conditionnement (M12d) · suites géométriques, récurrences d'ordre 1, moyenne exponentielle (R5) · trinôme du second degré, discriminant, racines, factorisation (R3) · espérance, variance d'une moyenne, erreur type (M02c) · projection orthogonale, point le plus proche (M12b) · normes L2 et L∞ (M07) · gradient de wᵀAw, moindres carrés (M09b) · jacobienne (M17) · gradient d'une moyenne (M18)

**mymath** : `iterative.py` (signatures figées) : `numerical_hessian`, `critical_step_size`, `richardson_iterates`, `linear_recurrence`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 19.7 ∂ Sur une parabole, η doit rester sous 2/a · 19.8 ∂ Moyenne mobile exponentielle : mémoire effective et biais initial · 18.3 ✏️ Descente sur une parabole : quel learning rate ? · 19.2 ✏️ Trois pas de momentum, deux conventions · 19.3 ✏️ Nesterov : gradient anticipé et reformulation de PyTorch · 19.4 ✏️ Adagrad et RMSprop sur une suite de gradients · 19.5 ✏️ Un pas d'Adam et la correction de biais · 19.6 ✏️ Adam + L2 ou AdamW : la même pénalité ? Convertir alpha, lambda et weight_decay d'une convention à l'autre · 19.9 🧮 Fermi : la mémoire des optimiseurs, du MLP au LLM · 19.Q3 🧠 Minima locaux ou points selles : le vrai piège en grande dimension · 19.Q5 🧠 Pas constant : pourquoi rebondit-on au fond de la vallée ? · 19.Q6 🧠 Décroissance exponentielle : que vaut η après 50 pas ? · 19.Q9 🧠 Momentum : que se passe-t-il si γ = 0 ? si γ = 1 ? · 19.R3 🔁 Standardiser les features, et l'effet sur la descente · 19.12 📄 Kingma et Ba (2014) : l'algorithme Adam ligne par ligne · 19.14 🔮 Pas constant sur une vallée : combien de pas pour le fond ? · 19.20 🔮 Trop de momentum : la bille quitte-t-elle la vallée ? · 19.21 🎨 Reproduire les figures du chapitre : pas constant, décroissant, momentum, Nesterov

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M19.Q1 | 🧠 | La hessienne : de quelle taille, symétrique, de quoi ? | ★ | 4 | §1 | C, E | manuel | — |
| M19.Q2 | 🧠 | Minimum, maximum, selle ou direction plate ? | ★ | 4 | §2 | C, E | manuel | — |
| M19.Q3 | 🧠 | Converge ou pas : lire les valeurs propres de M | ★ | 4 | §3 | C, E | manuel | — |
| M19.Q4 | 🧠 | Le pas de Richardson : lire la convergence sur les valeurs propres de I − ωA | ★ | 4 | §4 | C, E | manuel | — |
| M19.Q5 | 🧠 | Le conditionnement : ce qui ralentit, ce qui ne change rien | ★ | 4 | §5 | C, E | manuel | — |
| M19.Q6 | 🧠 | Module d'un nombre complexe et racines d'un trinôme | ★ | 4 | §6 | C, E | manuel | — |
| M19.Q7 | 🧠 | Un gradient estimé sur un échantillon : vrai ou faux | ★ | 4 | §7 | C, E | manuel | — |
| M19.Q8 | 🧠 | Boule ou pavé : la direction est-elle gardée ? | ★ | 4 | §8 | C | manuel | — |
| M19.R1 | 🔁 | Le théorème spectral et les valeurs propres d'une matrice symétrique (M12c) | ★ | 5 | §2 §3 | C, E | manuel | — |
| M19.R2 | 🔁 | Suites géométriques et récurrences d'ordre 1 (R5) | ★ | 5 | §3 §6 | C, E | manuel | — |
| M19.R3 | 🔁 | Le conditionnement par la SVD (M12d) | ★ | 5 | §5 | C | manuel | — |
| M19.1 | ✏️ | La hessienne d'une fonction de trois variables, et son développement de Taylor d'ordre 2 | ★★ | 20 | §1 | C, E | wbm | — |
| M19.2 | ✏️ | Classer les points critiques d'une fonction de trois variables | ★★ | 20 | §2 | C, E | wbm | — |
| M19.3 | ✏️ | Une itération linéaire 2 × 2 : point fixe, erreur, et convergence par les valeurs propres | ★★ | 20 | §3 | C, E | wbm | — |
| M19.4 | ✏️ | Résoudre un système 2 × 2 par l'itération de Richardson : trois pas à la main, et le pas critique | ★★ | 20 | §4 | C, E | wbm | — |
| M19.5 | ✏️ | Le meilleur pas de Richardson (énoncé), et le nombre d'itérations pour gagner six décimales | ★★ | 20 | §4 §5 | C, E | wbm | — |
| M19.6 | ✏️ | Une récurrence d'ordre 2 à racines réelles : terme général et convergence | ★★ | 20 | §6 | C, E | wbm | — |
| M19.7 | ✏️ | Une récurrence d'ordre 2 à racines complexes : module et oscillation amortie | ★★ | 20 | §6 | C, E | wbm | — |
| M19.8 | ✏️ | Une pente estimée sur B points tirés au hasard : espérance et variance de l'estimation | ★★ | 20 | §7 | C, E | wbm | — |
| M19.9 | ✏️ | Projeter un même vecteur sur une boule et sur un pavé : deux points, deux directions | ★ | 15 | §8 | C, E | wbm | — |
| M19.10 | ∂ | Une itération linéaire de matrice symétrique converge pour tout départ si et seulement si ses valeurs propres sont de module < 1 | ★★★ | 25 | §3 | C, E | manuel | — |
| M19.11 | ∂ | L'itération de Richardson converge si et seulement si 0 < ω < 2/λmax | ★★ | 15 | §4 | C, E | manuel | — |
| M19.12 | ∂ | Une récurrence d'ordre 2 converge si et seulement si ses racines sont de module < 1 : le critère |q| < 1 et |p| < 1 + q | ★★★ | 25 | §6 | C | manuel | — |
| M19.13 | ∂ | La projection sur une boule est son point le plus proche, et elle garde la direction | ★★ | 15 | §8 | C | manuel | — |
| M19.14 | 🔗 | Pont : un pas de Richardson est un pas de descente sur ½ xᵀA x − bᵀx (énoncé, sans calcul) | ★ | 10 | §4 | C | wbm | — |
| M19.15 | 🔗 | Pont : le préconditionnement diagonal, une idée commune à plusieurs méthodes de workbookIA 19 | ★ | 15 | §5 | C | wbm | — |
| M19.16 | 📖 | MML §5.7 et §5.8 : dérivées d'ordre supérieur et Taylor à plusieurs variables, en anglais | ★★ | 35 | §1 | C | manuel | — |
| M19.17 | 📖 | MML §7.1 : la descente de gradient, le pas, le momentum et la version stochastique, en anglais | ★★ | 40 | §3 §4 §7 | C | manuel | — |
| M19.18 | 🗣️ | Expliquer, sur un dessin de lignes de niveau, pourquoi un système mal conditionné converge lentement | ★ | 10 | §5 | C, E | manuel | — |
| M19.E1 | 💼 | « Que nous apprend la hessienne en un minimum ? » | ★ | 10 | §1 §2 | C | manuel | — |
| M19.E2 | 💼 | « Pourquoi un mauvais conditionnement ralentit-il une méthode itérative ? » | ★ | 10 | §5 | C | manuel | — |
| M19.19 | 🔨 | La hessienne par différences centrées · `numerical_hessian` | ★★ | 35 | §1 | C, E | pytest | — |
| M19.20 | 🔨 | Le pas critique d'une matrice symétrique définie positive, et les itérés de Richardson · `critical_step_size, richardson_iterates` | ★★ | 30 | §4 | C, E | pytest | — |
| M19.21 | 🔨 | Une récurrence linéaire d'ordre d · `linear_recurrence` | ★ | 15 | §6 | C | pytest | — |
| M19.22 | 📦 | `scipy.sparse.linalg.cg` : le gradient conjugué contre Richardson | ★ | 15 | §5 | C | wbm | M19.20 |
| M19.23 | 🔮 | Prédire le nombre d'itérations de Richardson selon ω, puis vérifier | ★ | 10 | §4 §5 | C, E | wbm | M19.20 |
| M19.24 | 🔬 | Le nombre d'itérations contre le conditionnement : une droite en échelle logarithmique | ★★ | 20 | §5 | C | wbm | M19.20 |
| M19.25 | 🎨 | Les itérés de Richardson sur les lignes de niveau d'une forme quadratique | ★ | 20 | §4 §5 | C, E | manuel | M19.20 |
| M19.26 | 🐛 | Chasse à l'erreur : un pas réglé sur λmin, une hessienne non symétrique, le module d'une racine complexe | ★ | 25 | §2 §4 §6 | C, E | wbm | — |
| M19.27 | 🛠️ | Un critère d'arrêt : le résidu relatif ‖b − A x‖/‖b‖ et un nombre maximal d'itérations | ★ | 15 | §4 | C | manuel | M19.20 |
| M19.28 | 🏆 | Défi : le schéma saute-mouton d'un oscillateur, x_{k+1} = (2 − h²Ω²) x_k − x_{k−1}, borné si et seulement si hΩ < 2 | ★★★ | 30 | §6 | C | wbm | M19.21 |

*Notes* : Frontières : les ∂ 19.7 (le pas sous 2/a, la quadratique diagonale, le pas optimal, la base propre, le momentum) et 19.8 (moyenne exponentielle : mémoire et biais initial), 18.3 (la parabole de workbookIA 18), 19.2 à 19.6 (momentum, Nesterov, Adagrad, RMSprop, Adam, AdamW à la main), 19.9 (Fermi de la mémoire des optimiseurs), 19.Q3, 19.Q5, 19.Q6, 19.Q9, 19.R3, 19.12, 19.14, 19.20 et 19.21. M19 démontre le théorème général des itérations linéaires x ← M x + c (M symétrique : convergence pour tout départ ⇔ toutes les |λ| < 1) et l'applique à l'itération de Richardson pour A x = b ; il énonce seulement qu'un pas de Richardson est un pas de descente de gradient sur ½ xᵀA x − bᵀx (∂ 19.7 fait la démonstration pour une loss), énonce le pas optimal 2/(λmin + λmax) et le facteur (κ − 1)/(κ + 1) sans les démontrer (∂ 19.7.4), et démontre le critère général de convergence d'une récurrence d'ordre 2 (|q| < 1 et |p| < 1 + q) sans le spécialiser au momentum (∂ 19.7.6) : aucun exercice, ni CP4, n'étudie la méthode de la bille lourde (Frankel, Polyak) x ← x + ω(b − A x) + β(x − x₋₁), qui est le momentum ; le défi M19.28 est une récurrence de la mécanique (le schéma saute-mouton), dont les racines sont de module 1. Le pont M19.14 énonce sans calcul (hors parcours essentiel), et M19.Q4 se lit sur des matrices 2 × 2, sans les quatre comportements en dimension 1 (∂ 19.7.1, 19.Q5). Le strict minimum sur les nombres complexes (i, module, conjugué, racines d'un trinôme réel) est en M12c §3 (audit de la session 55) ; M19 le rappelle et ajoute le module d'un produit, la forme trigonométrique et le produit des racines ; M22 fait le reste (valeurs propres complexes, rayon spectral). Le gradient estimé sur un échantillon est étudié comme un estimateur (sans biais, variance en 1/B), sur une pente de moindres carrés, sans compter epochs ni mises à jour. La projection sur une boule et sur un pavé est faite en géométrie (M07, M12b), sans norme globale de gradients ni constante 10⁻⁶ (`mylearn.clip_grad_norm`). Ni optimiseur, ni planning de learning rate, ni moyenne exponentielle corrigée du biais (workbookIA 19 et R5), ni nouvelle étude de la convexité (M10, M12c, M13b) ; MML §7.3 a été lu en M13b. Évités : les paraboles 5w², w² depuis 1, 2(w − 1)² depuis 3, 0,05(w − 1)², 5(w + 2)² et 8w², la vallée 1 − e^{−8w²}, Rosenbrock, les quadratiques de coefficients (10, 1) et de courbures 1 et 20, κ = 9 et η = 1,8/a₁, κ = 4 × 10⁶ (mètres et proportion), les selles x² − y² et 2x² − y², x² + 3y², −x² − y² et une fonction constante (19.Q2), les gradients et hyperparamètres de 19.2 à 19.6 et de CP4.3 de workbookIA, les vecteurs (6 ; 8), (3 ; 4), (6 ; 0,5), (1 ; 2) et (0,3 ; −0,4) et les seuils 5, 1 et 1,5, la comparaison d'angles des notes de 🔨 19.19 (M19.9 compare des directions sans angle chiffré de workbookIA), la bille et la vallée étroite. Le pont M19.15 ne reprend pas « un learning rate par poids » (19.Q11). Deux « Richardson » dans `mymath` (`approx.richardson_derivative` de M05a, `iterative.richardson_iterates`) : la fiche le signale. Le module s'appelle `iterative` (et non `optim`, le module d'optimiseurs de `mylearn`) ; `condition_number` existe déjà (M12d) et n'est pas réécrit ; NumPy permis, `np.linalg.eigvalsh` dans `critical_step_size` seulement, pas `np.linalg.solve`, `inv`, `scipy.optimize` ni `scipy.sparse.linalg`. Parcours essentiel : le critère d'ordre 2 et la projection démontrés hors parcours.

<a id="m20"></a>
## M20 · Tenseurs, axes et estimateurs pondérés

**Partie** IV · **prépare** workbookIA 20 · **dossier** `chapitres/m20_tenseurs_normalisation/` · **MML** — · **sessions de génération** 1

Les tableaux à k dimensions et leurs axes (forme, remodelage, réductions, diffusion), la notation d'Einstein et `einsum`, les moyennes et variances le long d'axes (ddof), le centrage vu comme une projection orthogonale et la standardisation invariante par translation et dilatation, l'estimateur de Horvitz-Thompson (une observation divisée par sa probabilité d'inclusion : sans biais, et sa variance), et les applications proches de l'identité x ↦ x + hF(x), dont la jacobienne I + hJ garde des produits proches de 1. workbookIA 20 en tire le dropout, les normalisations et les connexions résiduelles.

**Temps** : 8,8 h en parcours complet, 6,8 h en parcours essentiel (lecture 90 min, 15 flashcards).

**Objectifs**

- Décrire un tableau à k dimensions par sa forme et ses axes, le remodeler, et le réduire le long d'axes choisis.
- Écrire produits, traces et contractions en notation d'Einstein, et les calculer avec `einsum`.
- Calculer moyennes et variances le long d'axes, avec le bon ddof, et centrer par diffusion.
- Reconnaître le centrage comme une projection orthogonale, et les invariances de la standardisation.
- Construire un estimateur sans biais en divisant par une probabilité d'inclusion, et calculer sa variance.
- Calculer la jacobienne d'une application proche de l'identité, et suivre le produit de L telles jacobiennes.

**Sections de la fiche**

- §1 Tableaux à k dimensions : forme, axes, remodelage
- §2 Réductions et diffusion le long d'axes
- §3 La notation d'Einstein et `einsum`
- §4 Centrer et réduire : une projection et des invariances
- §5 Diviser par la probabilité d'inclusion : l'estimateur de Horvitz-Thompson
- §6 Des applications proches de l'identité : I + hJ

**Notions enseignées** : tableau à k dimensions (tenseur) : forme, axes, nombre d'éléments, remodelage en ordre C · réductions le long d'axes, keepdims, diffusion · notation d'Einstein, einsum, coût d'une contraction · moyenne et variance le long d'axes, ddof · matrice de centrage I − (1/m) 11ᵀ : projection orthogonale · standardisation invariante par translation et par dilatation · estimateur de Horvitz-Thompson : espérance et variance d'une observation divisée par sa probabilité d'inclusion · application proche de l'identité x ↦ x + hF(x) : jacobienne I + hJ_F, produit de L facteurs, (1 + hλ)ᴸ · méthode d'Euler pour x′ = F(x), exponentielle de matrice comme limite de (I + TJ/L)ᴸ (aperçu)

**Prérequis** : NumPy : arrays, formes, axis, broadcasting (IA:0A) · moyenne, variance, ddof, z-score, standardisation (M02c) · loi de Bernoulli, espérance, variance d'une somme de variables indépendantes (M02b) · projection orthogonale, matrice de projection (M12b) · produit matriciel, coût d'un produit (M09a) · trace (M12c) · jacobienne, règle de la chaîne (M17) · (1 + x/n)ⁿ → eˣ (M14) · 2ⁿ sous-ensembles, dénombrement (R8) · valeurs singulières (M12d)

**mymath** : `tensors.py` (signatures figées) : `einsum_pair`, `moments_along_axes`, `horvitz_thompson_total`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 20.5 ∂ Dropout : espérance, sous-réseaux et règle du test · 20.8 ∂ Le gradient de la batchnorm · 20.3 ✏️ Dropout inversé à la main · 20.4 ✏️ Batchnorm à la main sur un mini-batch de quatre exemples · 20.6 ✏️ Compter les 138 millions de paramètres de VGG16 · 20.7 ✏️ Connexion résiduelle et layer norm à la main · 20.9 🧮 Fermi : entraîner VGG16 sur ImageNet chez soi ? · 20.Q5 🧠 Vrai ou faux : le dropout tire ses neurones une fois par epoch · 20.Q6 🧠 Vrai ou faux : la batchnorm n'a aucun paramètre · 20.17 🔨 layer_norm, l2_penalty et EarlyStopping · 20.22 🔨 batchnorm_forward et batchnorm_backward · 20.30 🔬 Un réseau de 30 couches : connexions résiduelles et layer norm

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M20.Q1 | 🧠 | Forme, axes et nombre d'éléments | ★ | 4 | §1 | C, E | manuel | — |
| M20.Q2 | 🧠 | Réduire le long de quel axe ? | ★ | 4 | §2 | C, E | manuel | — |
| M20.Q3 | 🧠 | Lire une formule d'einsum | ★ | 4 | §3 | C, E | manuel | — |
| M20.Q4 | 🧠 | Diviser par une probabilité : sans biais ou biaisé ? | ★ | 4 | §5 | C, E | manuel | — |
| M20.R1 | 🔁 | Variance biaisée et non biaisée : ddof (M02c) | ★ | 5 | §2 | C, E | manuel | — |
| M20.R2 | 🔁 | La projection orthogonale sur une droite (M12b) | ★ | 5 | §4 | C, E | manuel | — |
| M20.R3 | 🔁 | La limite (1 + x/n)ⁿ → eˣ (M14) | ★ | 5 | §6 | C | manuel | — |
| M20.1 | ✏️ | Un tableau de mesures (stations × jours × heures) : les formes après réductions et remodelages | ★ | 15 | §1 §2 | C, E | wbm | — |
| M20.2 | ✏️ | Écrire en notation d'Einstein : produit matriciel, trace, forme bilinéaire, produits de matrices empilées le long d'un axe | ★ | 20 | §3 | C, E | wbm | — |
| M20.3 | ✏️ | La matrice de centrage, et une standardisation qui ne voit ni translation ni dilatation | ★★ | 20 | §4 | C, E | wbm | — |
| M20.4 | ✏️ | Un sondage à probabilités inégales : l'estimateur de Horvitz-Thompson d'un total, son espérance et sa variance | ★★ | 25 | §5 | C, E | wbm | — |
| M20.5 | ✏️ | Un schéma d'Euler en L pas : la jacobienne d'un pas, celle de L pas, et la limite (1 + λT/L)ᴸ | ★★ | 30 | §6 | C, E | wbm | — |
| M20.6 | ∂ | La matrice de centrage est la projection orthogonale sur l'orthogonal de 1 | ★★ | 15 | §4 | C | manuel | — |
| M20.7 | ∂ | L'estimateur de Horvitz-Thompson est sans biais, et sa variance quand les inclusions sont indépendantes | ★★ | 20 | §5 | C, E | manuel | — |
| M20.8 | 🔗 | Pont : où workbookIA 20 divise par une probabilité | ★ | 10 | §5 | C, E | wbm | — |
| M20.9 | 🗣️ | Expliquer ce qu'est un axe d'un tableau à quelqu'un qui ne connaît que les tableurs | ★ | 10 | §1 §2 | C, E | manuel | — |
| M20.E1 | 💼 | « Pourquoi standardiser des données décalées ou dilatées donne-t-il le même résultat ? » | ★ | 10 | §4 | C | manuel | — |
| M20.10 | 🔨 | `einsum` pour deux tableaux, avec des boucles · `einsum_pair` | ★★ | 45 | §3 | C, E | pytest | — |
| M20.11 | 🔨 | Moyennes et variances le long d'axes choisis · `moments_along_axes` | ★ | 25 | §2 | C, E | pytest | — |
| M20.12 | 🔨 | L'estimateur de Horvitz-Thompson d'un total · `horvitz_thompson_total` | ★ | 15 | §5 | C | pytest | — |
| M20.13 | 🔮 | Prédire la forme d'une réduction ou d'un einsum, puis vérifier | ★ | 10 | §1 §3 | C, E | wbm | — |
| M20.14 | 🔬 | Simuler un sondage : Horvitz-Thompson contre la moyenne naïve, biais et variance | ★★ | 20 | §5 | C | wbm | M20.12 |
| M20.15 | 🎨 | Le produit de L jacobiennes I + hJ : ses valeurs singulières extrêmes quand L grandit, à hL fixé | ★ | 20 | §6 | C, E | manuel | — |
| M20.16 | 🐛 | Chasse à l'erreur : une moyenne sur le mauvais axe, une diffusion silencieuse, un ddof oublié | ★ | 15 | §2 | C, E | wbm | — |
| M20.17 | 🛠️ | Un test de propriété : réduire sur deux axes d'un coup, ou l'un après l'autre | ★ | 25 | §2 | C | manuel | M20.11 |
| M20.18 | 🏆 | Défi : des probabilités d'inclusion proportionnelles à la taille, et un estimateur presque sans variance | ★★★ | 25 | §5 | C | wbm | — |

*Notes* : Frontières : les ∂ 20.5 (espérance et variance du dropout, sous-réseaux, règle du test, Jensen sur une ReLU) et 20.8 (le gradient de la batchnorm), 20.3 (dropout à la main), 20.4 (batchnorm à la main), 20.6 et 20.9 (VGG16), 20.7 (connexion résiduelle et layer norm à la main), 20.Q5, 20.Q6, 20.17 (layer norm, RMSNorm), 20.22 et 20.30 (30 couches). M20 enseigne l'estimateur de Horvitz-Thompson sur des sondages (communes, entreprises, arbres d'une forêt) : c'est l'outil du dropout inversé (diviser par la probabilité d'être gardé), sans neurone, masque ni probabilité de coupure, et sans les probabilités 0,5, 0,6, 0,75 et 0,8 ; le centrage est une projection orthogonale (M12b), et la standardisation est invariante par translation et dilatation, sans γ, β, statistiques glissantes, ε ni dérivée de la standardisation (∂ 20.8) ; I + hJ est la jacobienne d'un pas d'Euler, et le produit de L pas, à horizon T = hL fixé, tend vers une exponentielle (M14), sans 0,5³⁰, 1,01³⁰ ni 0,9 et 44 couches. Le pont M20.8 dit seulement où workbookIA 20 divise par une probabilité, sans correspondance π ↔ 1 − p ni formule en p (∂ 20.5.1). Ni la fiche ni un exercice ne composent la normalisation x/‖x‖ de M17.4 avec la matrice de centrage, ni ne tirent des invariances de la standardisation une propriété de sa jacobienne ou d'un gradient (∂ 20.8.3 et 20.8.5). Les tableaux sont des mesures (stations × jours × heures), des notes (élèves × matières) et des images en (hauteur, largeur, canaux), sans les formes de workbookIA 20 ((32, 3, 28, 28), (32, 1, 28, 28), (1, 512, 7, 7), (10, 3, 5), arange(150), arange(30), arange(20)), ni VGG16, ni les vecteurs (1, 2, 3, 6), (2, 4, 6, 8), (2 ; 6 ; 8 ; 12), (2, 2, 8, 8) et le tableau 4 × 2 de 20.4. `einsum` ne sert pas à workbookIA 19 et 20 (il arrive en 21, B3, B6 et 28) : M20 le prépare. `tensors` : `einsum_pair` écrit `einsum` pour deux tableaux par des boucles (pas `np.einsum`, `tensordot`, `@`, `dot`, `inner` ni `outer`), `moments_along_axes` rend moyenne et variance sans normaliser (pas `np.var` ni `np.std`), `horvitz_thompson_total` l'estimation d'un total. Pas de 📖 (MML n'a pas de section sur les tenseurs). Réduit à 8 h (§8). COMPOSITION : prévu court (7,7 h), porté à 8,8 h par les durées que l'apprenant simulé a mesurées (session 53) ; la composition d'un chapitre court est gardée (4 quiz, 7 ✏️ et ∂, 3 🔨).

<a id="cp4"></a>
## CP4 · Examen blanc de la partie IV

**Partie** IV · **prépare** — · **dossier** `checkpoints/partie_4/` · **MML** — · **sessions de génération** 1

Le bilan de la partie IV (M16 à M20), juste avant le checkpoint IV de workbookIA : un examen blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.

**Temps** : 3,1 h en parcours complet, 3,1 h en parcours essentiel (lecture 15 min, 0 flashcards).

**Objectifs**

- Vérifier en temps limité que les notions de la partie IV sont acquises.
- Construire ta propre synthèse de la partie IV.

**Sections de la fiche**

- §1 Examen blanc
- §2 Synthèse

**Notions enseignées** : révision de la partie IV

**Prérequis** : toute la partie IV (M20)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 16.1 ✏️ Compter les poids et les biais d'un MLP · 16.2 ✏️ Passe avant à la main dans un réseau 2-2-1 · 16.3 ✏️ Formes et broadcasting d'un mini-batch à travers les couches · 16.4 ✏️ Ordre d'évaluation d'un graphe et détection de boucle · 16.6 ∂ Symétrie : pourquoi une initialisation constante ne se brise jamais · 16.7 ∂ Conserver la variance : retrouver les règles de LeCun, Glorot et He · 16.8 🧮 Fermi : taille, mémoire et coût d'un MLP pour MNIST · 16.Q10 🧠 LeCun, Glorot, He : quel fan-in, pour quelle activation ? · 16.15 🎨 Reproduire les figures 16.5 et 16.6, puis comparer Glorot et He · 16.19 🔮 Initialisation constante : les neurones restent-ils jumeaux ? · 16.23 🔬 Activations à travers 20 couches selon l'initialisation · 17.1 ✏️ Effondrer un réseau linéaire en un seul neurone · 17.2 ✏️ Tableau de valeurs de neuf activations · 17.3 ∂ Une composition d'affines reste affine ; une ReLU casse tout · 17.4 ∂ Dériver la sigmoïde, tanh et softplus · 17.5 ✏️ Maxout et ReLU : construire |x|, une cuvette et une bosse · 17.6 ✏️ Softmax à la main : translation, température, rapports · 17.7 ∂ La Jacobienne de la softmax · 17.8 🧮 Fermi : une activation coûte-t-elle cher face au produit matriciel ? · 17.16 🔨 La Jacobienne de la softmax en NumPy · 17.19 🔮 Softmax et température : prédire la distribution · 17.21 📈 Diagnostiquer la saturation sur des histogrammes de pré-activations · 17.23 🔬 Produit des dérivées sur 10 couches : sigmoïde, tanh, ReLU, GELU · 18.1 ✏️ Le delta, amplificateur de changement · 18.2 ✏️ Deltas de sortie avec l'erreur quadratique : attention au signe · 18.3 ✏️ Descente sur une parabole : quel learning rate ? · 18.4 ✏️ Rétropropagation complète du réseau minuscule, sans activation · 18.5 ✏️ Le même réseau avec une sigmoïde cachée : le facteur σ'(z) · 18.6 ∂ La règle de la chaîne derrière les deltas · 18.7 ∂ Forme matricielle : XᵀΔ, ΔWᵀ et somme des lignes · 18.8 ∂ Softmax et cross-entropy : le gradient vaut p − y · 18.9 🧮 Fermi : rétropropagation contre force brute · 18.14 🔨 Cross-entropies calculées sur les logits (binaire et softmax) · 18.15 🔨 dense_backward : les trois gradients d'une couche · 18.16 🔨 gradient_check : vérifier un gradient par différences finies · 18.17 🐛 Chasse au bug : trois gradients faux démasqués · 18.26 🔨 Micro-autograd : la classe Value · 18.27 🔮 À la main, Value, mlp_backward, différences finies : quatre gradients identiques ? · 19.2 ✏️ Trois pas de momentum, deux conventions · 19.3 ✏️ Nesterov : gradient anticipé et reformulation de PyTorch · 19.4 ✏️ Adagrad et RMSprop sur une suite de gradients · 19.5 ✏️ Un pas d'Adam et la correction de biais · 19.6 ✏️ Adam + L2 ou AdamW : la même pénalité ? Convertir alpha, lambda et weight_decay d'une convention à l'autre · 19.7 ∂ Sur une parabole, η doit rester sous 2/a · 19.8 ∂ Moyenne mobile exponentielle : mémoire effective et biais initial · 19.9 🧮 Fermi : la mémoire des optimiseurs, du MLP au LLM · 19.Q3 🧠 Minima locaux ou points selles : le vrai piège en grande dimension · 19.Q5 🧠 Pas constant : pourquoi rebondit-on au fond de la vallée ? · 19.Q6 🧠 Décroissance exponentielle : que vaut η après 50 pas ? · 19.Q9 🧠 Momentum : que se passe-t-il si γ = 0 ? si γ = 1 ? · 19.R3 🔁 Standardiser les features, et l'effet sur la descente · 19.12 📄 Kingma et Ba (2014) : l'algorithme Adam ligne par ligne · 19.14 🔮 Pas constant sur une vallée : combien de pas pour le fond ? · 19.20 🔮 Trop de momentum : la bille quitte-t-elle la vallée ? · 19.21 🎨 Reproduire les figures du chapitre : pas constant, décroissant, momentum, Nesterov · 20.3 ✏️ Dropout inversé à la main · 20.4 ✏️ Batchnorm à la main sur un mini-batch de quatre exemples · 20.5 ∂ Dropout : espérance, sous-réseaux et règle du test · 20.6 ✏️ Compter les 138 millions de paramètres de VGG16 · 20.7 ✏️ Connexion résiduelle et layer norm à la main · 20.8 ∂ Le gradient de la batchnorm · 20.9 🧮 Fermi : entraîner VGG16 sur ImageNet chez soi ? · 20.Q5 🧠 Vrai ou faux : le dropout tire ses neurones une fois par epoch · 20.Q6 🧠 Vrai ou faux : la batchnorm n'a aucun paramètre · 20.17 🔨 layer_norm, l2_penalty et EarlyStopping · 20.22 🔨 batchnorm_forward et batchnorm_backward · 20.30 🔬 Un réseau de 30 couches : connexions résiduelles et layer norm

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| CP4.Q1 | 🧠 | Dix affirmations sur la partie IV : vrai ou faux | ★ | 10 | §1 | C, E | manuel | — |
| CP4.1 | ✏️ | Coordonnées homogènes, chemins d'un graphe et variance d'un produit | ★★ | 10 | §1 | C, E | wbm | — |
| CP4.2 | ✏️ | Jacobienne d'une composée et produit vecteur-jacobienne | ★★ | 10 | §1 | C, E | wbm | — |
| CP4.3 | ✏️ | Mode direct et mode inverse sur un graphe de calcul | ★★ | 10 | §1 | C, E | wbm | — |
| CP4.4 | ✏️ | Gradients par rapport à une matrice | ★★ | 9 | §1 | C, E | wbm | — |
| CP4.5 | ✏️ | Hessienne, Taylor d'ordre 2 et nature d'un point critique | ★★ | 10 | §1 | C, E | wbm | — |
| CP4.6 | ✏️ | Itération de Richardson et récurrence d'ordre 2 | ★★ | 9 | §1 | C, E | wbm | — |
| CP4.7 | ✏️ | Moments le long d'axes, einsum et estimateur de Horvitz-Thompson | ★★ | 8 | §1 | C, E | wbm | — |
| CP4.8 | ∂ | Une démonstration au choix : une matrice qui raccourcit les vecteurs, ou Var(XY) ≥ Var X · Var Y | ★★★ | 12 | §1 | C, E | manuel | — |
| CP4.9 | 🐛 | Corriger une copie : cinq erreurs | ★★ | 8 | §1 | C, E | wbm | — |
| CP4.10 | 🔗 | Problème de synthèse : ajuster une loi exponentielle, du graphe de calcul au pas critique | ★★ | 14 | §1 | C, E | wbm | — |
| CP4.11 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme CP3 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, 03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend le checkpoint IV de workbookIA (`checkpoints/partie_4/` de workbookIA : le comptage d'un MLP 20-64-32-3, un réseau 2-2-1 à ReLU à la main, momentum, Adam et AdamW sur deux gradients, dropout et batchnorm à la main, le gradient à travers des sigmoïdes empilées et L = 10, le Fermi d'un MLP 784-1 024-1 024-10 avec AdamW, les bugs d'une boucle PyTorch, des courbes d'entraînement, une epoch d'AdamW avec clipping, les manchots et la ridge des parties I à III), qui se fait juste après, ni son mini-projet IV (un mini-framework NumPy validé contre PyTorch). La synthèse ne recopie pas le tableau des 24 formules de la synthèse de workbookIA. CP4.2 n'est pas une chaîne de fonctions d'une variable à dérivée bornée (CP4.5 de workbookIA) ; CP4.6 n'étudie pas la bille lourde (le momentum, ∂ 19.7.6) ; CP4.8 donne le choix entre deux énoncés neufs : une matrice symétrique qui raccourcit tout vecteur non nul (‖M x‖ < ‖x‖) a ses valeurs propres dans ]−1, 1[, ou Var(XY) ≥ Var X · Var Y pour X et Y indépendantes, avec le cas d'égalité ; aucune ne compose la normalisation avec le centrage (∂ 20.8). CP4.10 ajuste une loi exponentielle à trois mesures prises ailleurs qu'en x = 1, 2, 3 (CP4.12 d de workbookIA), hors réseau : graphe de calcul, gradient par le mode inverse, hessienne et pas critique.

<a id="m21"></a>
## M21 · Convolution, matrices de Toeplitz et équivariance

**Partie** V · **prépare** workbookIA 21 · **dossier** `chapitres/m21_convolution/` · **MML** — · **sessions de génération** 1

La convolution, d'abord entre deux suites (le produit de deux polynômes, la loi de la somme de deux dés, une moyenne mobile), puis la corrélation croisée des bibliothèques, qui ne retourne pas le noyau, et les pochoirs de différences finies ; la convolution comme application linéaire, de matrice de Toeplitz creuse ; l'équivariance par translation, les convolutions circulaires et le pooling ; le pas, la dilatation, le padding, le nombre de positions d'une fenêtre (un dénombrement) et la convolution transposée ; les grilles de mesures à plusieurs canaux, les noyaux séparables, les paramètres et le coût ; la composition de convolutions et le champ récepteur ; enfin le pire cas d'une petite perturbation, une forme linéaire maximisée sur une boule. workbookIA 21 applique ces outils aux réseaux convolutifs.

**Temps** : 14,8 h en parcours complet, 11,0 h en parcours essentiel (lecture 160 min, 22 flashcards).

**Objectifs**

- Calculer à la main la convolution et la corrélation croisée de deux suites, dans les modes plein, valide et même taille, et passer d'une convention à l'autre.
- Écrire la matrice de Toeplitz d'une convolution, compter ses coefficients non nuls, et lire son rang.
- Démontrer et utiliser l'équivariance par translation, et reconnaître une convolution circulaire.
- Compter les positions d'une fenêtre avec pas, dilatation et padding, et calculer la taille d'une convolution transposée.
- Compter les paramètres et le coût d'un filtrage à plusieurs canaux, et séparer un noyau de rang 1.
- Composer des convolutions en une seule, et calculer un champ récepteur.
- Trouver le pire cas d'une perturbation bornée d'une forme linéaire, pour les normes L∞ et L2.

**Sections de la fiche**

- §1 La convolution de deux suites : polynômes, dés et moyennes mobiles
- §2 Corrélation croisée, retournement, modes et pochoirs
- §3 La convolution comme application linéaire : matrices de Toeplitz et matrices creuses
- §4 Équivariance par translation : décalages, convolutions circulaires et pooling
- §5 Pas, dilatation, padding : compter les positions, et la convolution transposée
- §6 Grilles de mesures et canaux : noyaux séparables, paramètres et coût
- §7 Composer des convolutions : noyau équivalent et champ récepteur
- §8 Le pire cas d'une petite perturbation : une forme linéaire sur une boule

**Notions enseignées** : convolution de deux suites : produit de polynômes, loi de la somme de deux variables discrètes indépendantes, moyenne mobile ; commutative, associative, linéaire · corrélation croisée (sans retournement, celle des bibliothèques) et convolution (noyau retourné) ; modes plein, valide et même taille ; conventions d'indices · pochoirs de différences finies : dérivée, dérivée seconde, laplacien discret · matrice de Toeplitz d'une convolution ; matrice creuse : coefficients non nuls, coût d'un produit · matrice des fenêtres (im2col, la notion) : une convolution est un produit matriciel · transposée de la matrice d'une convolution : énoncée en général, démontrée pour les matrices circulantes · équivariance par translation ; convolution circulaire, matrices circulantes ; une application linéaire qui commute avec le décalage circulaire est une convolution circulaire · pooling moyen (une convolution suivie d'un sous-échantillonnage) et pooling max (non linéaire, invariance locale) · pas, dilatation, padding : nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 démontré comme un dénombrement ; padding « même taille », avec ou sans pas (⌈n/s⌉) · sous-échantillonnage et insertion de zéros, deux matrices transposées l'une de l'autre ; convolution transposée : taille, recouvrements, damier ; une taille de sortie vient de plusieurs tailles d'entrée · convolution 2D sur des grilles de mesures à plusieurs canaux, convolution 1 × 1, convolutions groupées et par canal : paramètres C_out(C_in/g · k_h k_w + 1), coût et mémoire · noyau séparable : un noyau de rang 1 (produit extérieur) s'applique en deux convolutions 1D · composition de convolutions : noyau équivalent (associativité), pas produit, champ récepteur (récurrence et forme close) · maximum d'une forme linéaire sur une boule : ε‖g‖₁ en ε signe(g) pour la norme L∞, ε‖g‖₂ pour la norme L2

**Prérequis** : partie entière ⌊x⌋ et ⌈x⌉ (R1) · fonction signe (R2) · polynômes (R3) · sommes Σ, raisonnement par récurrence (R4) · moyenne mobile (R5) · loi d'un couple de variables discrètes, indépendance (M02b) · différences finies avant et centrée (M05a) · normes L1, L2 et L∞, Cauchy-Schwarz (M07) · produit matriciel, transposée, coût d'un produit (M09a) · moindres carrés (M09b) · matrice d'une application linéaire, noyau, rang (M12a) · rang 1, décomposition en valeurs singulières (M12d) · approximation au premier ordre f(x + δ) ≈ f(x) + ∇f(x) · δ (M05b) · tableaux à plusieurs axes, formes, einsum (M20)

**mymath** : `convolution.py` (signatures figées) : `convolve`, `toeplitz_matrix`, `circular_convolve`, `equivalent_kernel`, `separable_factors`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 21.7 ∂ Rétropropager dans une convolution 1D : la somme sur les positions · 21.R2 🔁 Le gradient d'un poids utilisé à plusieurs endroits · 21.Q3 🧠 Convolution ou corrélation croisée ? · 21.Q4 🧠 Détecteurs de motifs et hiérarchie de filtres · 21.Q5 🧠 Padding et stride : que devient la taille ? · 21.Q6 🧠 Canaux d'entrée, nombre de filtres, canaux de sortie · 21.Q7 🧠 Convolution 1D ou convolution 1×1 ? · 21.Q9 🧠 Convolution transposée : les mots piégés · 21.Q11 🧠 Exemples adversariaux : vrai ou faux ? · 21.1 ✏️ Le détecteur de jaune à la main · 21.2 ✏️ Une corrélation 5×5 par 3×3 à la main · 21.3 ✏️ Tailles de sortie : padding, stride et la hiérarchie 600 → 300 → 100 · 21.4 ✏️ Compter les paramètres : convolution contre couche dense · 21.5 ✏️ Champ récepteur effectif d'une pile convolution + pooling · 21.6 ✏️ Convolution transposée à la main : insérer des zéros puis corréler · 21.8 🧮 Fermi : paramètres, mémoire et calcul de VGG16 · 21.11 📄 Lire LeCun et coll. (1998) : LeNet-5 · 21.12 🔨 conv_output_size et pad2d · 21.16 🛠️ Tests pytest paramétrés pour conv2d · 21.17 🎨 Reproduire la chasse aux rayures verticales (Fig. 21.14) · 21.20 🔮 Conv1d, noyau pleine largeur et 1×1 : prédire formes et paramètres · 21.26 🔬 Stride ou pooling : accuracy et temps sur CIFAR-10 · 21.29 📦 Attaque FGSM contre ton CNN Fashion-MNIST · 21.E2 💼 Taille de sortie et paramètres d'une Conv2d(3, 64, 3, stride=2, padding=1) sur une image 224×224 · 21.E3 💼 À quoi sert une convolution 1×1 ? · 22.R1 🔁 Une convolution 1D peut-elle lire une séquence ? · 24.R2 🔁 Taille de sortie d'une convolution à padding 'same' et stride 2 · 24.2 ✏️ Formes et paramètres du CNN à pooling du livre · 24.3 ✏️ Stride ou pooling : compter les multiplications · 24.Q9 🧠 Motifs conv-conv-pool, stride contre pooling, batchnorm contre dropout

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M21.Q1 | 🧠 | Convolution ou corrélation : retourner, glisser, sommer | ★ | 4 | §1 §2 | C, E | manuel | — |
| M21.Q2 | 🧠 | Les propriétés de la convolution : vrai ou faux | ★ | 4 | §1 | C, E | manuel | — |
| M21.Q3 | 🧠 | Lire une matrice de Toeplitz : diagonales, coefficients non nuls, nombre de lignes | ★ | 4 | §3 | C, E | manuel | — |
| M21.Q4 | 🧠 | Équivariant, invariant, ou ni l'un ni l'autre ? Décalages, bords, pas et pooling | ★ | 4 | §4 | C, E | manuel | — |
| M21.Q5 | 🧠 | Combien de positions ? Pas, dilatation, padding et insertion de zéros | ★ | 4 | §5 | C, E | manuel | — |
| M21.Q6 | 🧠 | Canaux, groupes, convolution 1 × 1 et noyaux séparables : compter | ★ | 4 | §6 | C, E | manuel | — |
| M21.Q7 | 🧠 | Composer des convolutions : noyau, pas et champ récepteur | ★ | 4 | §7 | C, E | manuel | — |
| M21.Q8 | 🧠 | Le pire cas d'une perturbation bornée : quelle norme, quel vecteur ? | ★ | 4 | §8 | C | manuel | — |
| M21.R1 | 🔁 | La moyenne mobile d'une suite (R5) | ★ | 5 | §1 | C, E | manuel | — |
| M21.R2 | 🔁 | La matrice d'une application linéaire, son noyau et son rang (M12a) | ★ | 5 | §3 | C, E | manuel | — |
| M21.R3 | 🔁 | Le rang d'un produit extérieur u vᵀ et la décomposition en valeurs singulières (M12d) | ★ | 5 | §6 | C | manuel | — |
| M21.1 | ✏️ | Deux dés truqués et un produit de polynômes : la même convolution | ★ | 20 | §1 | C, E | wbm | — |
| M21.2 | ✏️ | Convoluer et corréler un signal à la main, dans les trois modes | ★★ | 20 | §2 | C, E | wbm | — |
| M21.3 | ✏️ | Des pochoirs de différences finies : dérivée et dérivée seconde d'un signal échantillonné | ★★ | 15 | §2 | C, E | wbm | — |
| M21.4 | ✏️ | La matrice de Toeplitz d'une convolution pleine et d'une convolution valide : coefficients non nuls, rang et noyau | ★★ | 20 | §3 | C, E | wbm | — |
| M21.5 | ✏️ | Décaler puis filtrer, ou filtrer puis décaler : l'équivariance, ses bords et son pas | ★★ | 15 | §4 | C, E | wbm | — |
| M21.6 | ✏️ | Compter les positions d'une fenêtre : pas, dilatation, padding, « même taille » avec un pas, et le problème inverse | ★★ | 25 | §5 | C, E | wbm | — |
| M21.7 | ✏️ | Sous-échantillonner et insérer des zéros : la convolution transposée d'un signal et ses recouvrements | ★★ | 25 | §5 | C, E | wbm | — |
| M21.8 | ✏️ | Une carte de températures filtrée par un laplacien discret et par un lissage séparable | ★★ | 30 | §6 | C, E | wbm | — |
| M21.9 | ✏️ | Paramètres et coût d'un filtrage à plusieurs canaux : standard, groupé, par canal, 1 × 1 | ★★ | 20 | §6 | C, E | wbm | — |
| M21.10 | ✏️ | Le noyau équivalent de deux lissages successifs, et le champ récepteur d'une pile avec pas et dilatation | ★★ | 20 | §7 | C, E | wbm | — |
| M21.11 | ✏️ | Le pire cas d'une erreur de capteurs bornée : une forme linéaire sur les boules L∞ et L2 | ★ | 15 | §8 | C, E | wbm | — |
| M21.12 | ∂ | La convolution est commutative et associative ; la corrélation croisée ne l'est pas | ★★ | 25 | §1 | C | manuel | — |
| M21.13 | ∂ | Les applications linéaires qui commutent avec le décalage circulaire sont les convolutions circulaires ; la transposée d'une matrice circulante | ★★★ | 30 | §4 | C | manuel | — |
| M21.14 | ∂ | Le nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 quand la fenêtre tient, par un dénombrement | ★★ | 20 | §5 | C, E | manuel | — |
| M21.15 | ∂ | Le champ récepteur d'une pile de convolutions : récurrence et forme close | ★★ | 25 | §7 | C | manuel | — |
| M21.16 | ∂ | Le maximum d'une forme linéaire sur une boule L∞ vaut ε‖g‖₁, atteint en ε signe(g) | ★ | 10 | §8 | C | manuel | — |
| M21.17 | 🔗 | Pont : filtrer une grille à trois canaux comme les bibliothèques, formes (C, H, W), poids (C_out, C_in, k, k), et sans retournement | ★ | 25 | §2 §6 | C, E | wbm | — |
| M21.18 | 🗣️ | Expliquer avec une règle graduée et un pochoir pourquoi une convolution est équivariante, mais pas invariante | ★ | 10 | §4 | C, E | manuel | — |
| M21.E1 | 💼 | « Pourquoi une convolution est-elle une matrice de Toeplitz, et pourquoi ne la forme-t-on jamais ? » | ★ | 10 | §3 | C | manuel | — |
| M21.19 | 🔨 | La convolution de deux suites, dans les trois modes · `convolve` | ★★ | 30 | §1 §2 | C, E | pytest | — |
| M21.20 | 🔨 | La matrice de Toeplitz d'une convolution · `toeplitz_matrix` | ★★ | 25 | §3 | C, E | pytest | — |
| M21.21 | 🔨 | La convolution circulaire · `circular_convolve` | ★ | 20 | §4 | C | pytest | — |
| M21.22 | 🔨 | Reconnaître un noyau séparable et le factoriser · `separable_factors` | ★★ | 25 | §6 | C | pytest | — |
| M21.23 | 🔨 | Le noyau équivalent et le pas d'une pile de sommes glissantes · `equivalent_kernel` | ★★ | 30 | §7 | C, E | pytest | M21.19 |
| M21.24 | 🔮 | Prédire l'effet d'un décalage de l'entrée sur un filtrage avec pas, puis vérifier | ★ | 15 | §4 §5 | C, E | wbm | M21.19 |
| M21.25 | 🔬 | Le coût d'un filtrage direct ou séparable, selon la taille du noyau : mesurer, puis comparer à k² et 2k | ★★ | 30 | §6 | C | wbm | M21.19 |
| M21.26 | 🎨 | La carte des recouvrements d'une convolution transposée : un damier ou pas, selon k et s | ★ | 15 | §5 | C, E | manuel | — |
| M21.27 | 🐛 | Chasse à l'erreur : un noyau non retourné, des recouvrements supposés réguliers, un noyau de rang 2 « séparé » | ★ | 25 | §2 §5 §6 | C, E | wbm | — |
| M21.28 | 🛠️ | Un test de propriété : la matrice de Toeplitz fois x égale la convolution, pour des longueurs tirées au hasard | ★ | 20 | §3 | C | manuel | M21.20 |
| M21.29 | 🏆 | Défi : retrouver un noyau inconnu à partir d'un signal et de sa version filtrée bruitée, par les moindres carrés | ★★★ | 25 | §3 | C | wbm | M21.20 |

*Notes* : Frontières : le ∂ 21.7 (rétropropager dans une convolution 1D : ∂L/∂w comme somme sur les positions, ∂L/∂b, ∂L/∂x par la convolution pleine du noyau retourné, les zéros dans g pour un pas, les formules 2D à canaux), 21.R2 (un poids utilisé à plusieurs endroits), les quiz 21.Q3, 21.Q5, 21.Q6, 21.Q7, 21.Q9 et 21.Q11, 21.Q4 (le score maximal d'un filtre ±1, une forme linéaire sur un pavé), les ✏️ 21.1 à 21.6, 🧮 21.8 (VGG16), 📄 21.11 (LeNet-5), 21.17 (rayures), 21.20 (Conv1d contre Conv2d pleine largeur), 21.26 (MAC du pas contre le pooling), 21.29 (FGSM), 21.E2 et 21.E3, le rappel 22.R1 de workbookIA 22 (champs récepteurs d'une pile 1D et dilatations qui doublent), et, de workbookIA 24, qui n'a pas de chapitre de maths, 24.R2 (« same » de Keras avec un pas), 24.2, 24.3 et 24.Q9. M21 enseigne les outils hors réseau : signaux échantillonnés (un capteur, un son), grilles de mesures (températures, altitudes), polynômes et lois de dés, jamais une image d'un dataset de workbookIA, une couche, un filtre appris ni une attaque. La transposée de la matrice d'une convolution valide est celle de la convolution pleine par le noyau retourné, et réciproquement (en mode même taille, seulement pour un noyau de longueur impaire) : c'est énoncé, en convention mathématique et sur des signaux, sans gradient ni produit vecteur-jacobienne (c'est le contenu de 21.7 Q3 en convention des bibliothèques), et démontré seulement pour les matrices circulantes (∂ M21.13, où le noyau retourné est (h₀, h_{n−1}, …, h₁), et non le simple renversement : une erreur classique) ; M21 n'écrit jamais ∂L/∂x ni ∂L/∂w d'une convolution, ni « un pas, ce sont des zéros dans g ». La formule des tailles est démontrée comme un dénombrement (∂ M21.14, sous l'hypothèse n + 2p ≥ d(k − 1) + 1 que la fenêtre tienne), avec « même taille » sans pas et avec un pas (⌈n/s⌉ et un padding total réparti inégalement, la règle de 24.R2, sur d'autres nombres) ; le problème inverse de M21.6 ne demande pas « le plus petit et le plus grand p » qui donnent une taille (21.3 c-d) ; pour un noyau de longueur paire, le « même taille » de `np.convolve` (donc de `convolve`) et celui de PyTorch diffèrent d'un décalage (la case en trop n'est pas du même côté) : à dire dans la fiche, le 🔗 M21.17 et le 🐛 M21.27 ; la taille d'une convolution transposée vient de l'insertion de zéros (avec le padding de sortie) et une taille de sortie peut venir de deux tailles d'entrée ; le champ récepteur est démontré par récurrence (∂ M21.15) et calculé sur d'autres piles que celles de 21.5 et de CP5.2 de workbookIA, et la composition de deux convolutions est une convolution (M21.10, 🔨 M21.23), sans l'argument de VGG en nombre de poids. Le coût (une multiplication-addition par poids et par position) et les paramètres C_out(C_in/g · k_h k_w + 1) sont posés sur des filtrages de grilles de mesures, sans réseau entier ni comparaison avec une couche dense. « Noyau séparable » veut dire ici de rang 1 ; dans workbookIA 21, « convolution séparable » veut dire par canal puis 1 × 1 (MobileNet) : un encadré ⚠️ le dit, et M21.Q6 ne mêle pas les deux sens. L'équivariance est enseignée hors réseau (règle, pochoir, signaux), sans reprendre la relance de 21.E1 (« le pooling, le pas et le padding la cassent en partie »). La transformée de Fourier n'est qu'un encadré 💻 (aucun chapitre ne l'enseigne) : le 🔬 M21.25 compare le direct et le séparable. M21.3 prend un autre signal que l'exemple de `convolve`. L'injectivité d'une convolution pleine n'est que constatée sur un exemple (M21.4) : sa démonstration est l'un des sujets de CP5.8. Le §8 (une forme linéaire sur une boule) est l'outil de FGSM, pris sur des erreurs de capteurs, sans gradient d'une loss ni ε en k/255 ; la projection sur un pavé (`clamp`) est celle de M19. Évités (règle de partage) : les suites (2, 0, 1, 3) et (1, 2), (1, 2, 3, 4) et (1, 0, −1), la grille X 5 × 5 de 21.2 et le noyau de Sobel, le noyau de netteté (l'identité moins le laplacien) et le flou boîte 1/9, la luminance (0,299 ; 0,587 ; 0,114), le détecteur de jaune (R + G − B) et le neurone cyan, le filtre de rayure ±1 et son score 3, x = [[2, −1], [1, 3]] et le noyau 3 × 3 de 21.6, x = (1, 2, −1, 3) avec w = (2, −1) ou (1, −1) (∂ 21.7 et CP5.12 de workbookIA), la hiérarchie 600 → 300 → 100, les tailles 7 × 7 avec k = 3 et s = 2, 12 × 12 avec k = 5, 7 × 12, 28, 32 et 224, les champs récepteurs 3, 5, 7, 9, 11, 15, 35, 6 et 18 de leurs piles, les transposées 4 → 9, 7 → 14, 100 → 300 et 16 → 32, les cartes de recouvrements (k, s) = (3, 2) et (4, 2) de la fiche, VGG16, LeNet-5, MNIST, Fashion-MNIST, CIFAR-10, le convnet de Keras, 300 → 175 et 256 → 64 canaux, 16 filtres 5 × 5 sur 8 canaux, Conv2d(3, 64, 3, s = 2, p = 1), 6 canaux et 4 filtres 3 × 3, 20 mots de 50 nombres, ε = 0,03 sur 784 pixels. Conventions : la convolution des mathématiciens (noyau retourné, `np.convolve`) et la somme glissante des bibliothèques (sans retournement, celle de workbookIA) sont distinguées partout ; indices à partir de 0 ; une fenêtre est repérée par sa première case. `convolution` (et non `conv`, le module de `mylearn`) : NumPy permis, sauf `np.convolve`, `np.correlate`, `np.polymul`, `np.polynomial` et `np.fft`, et aucune fonction de SciPy (`convolution_matrix` et `circulant` donneraient deux des fonctions) ; de `np.linalg`, seulement `svd`, dans `separable_factors` ; aucune fonction de taille de sortie, de matrice des fenêtres, de pooling, de convolution transposée ni de gradient. Pas de MML (le livre ne traite pas la convolution), donc pas de 📖. 13,6 h au lieu des 10 h prévues : la fiche ajoute la matrice creuse, le coût, « même taille » avec un pas, la taille d'une convolution transposée et la forme linéaire sur une boule, que workbookIA 21 et 24 supposent.

<a id="m22"></a>
## M22 · Récurrences vectorielles, rayon spectral et normes de matrices

**Partie** V · **prépare** workbookIA 22 · **dossier** `chapitres/m22_recurrences/` · **MML** (§4.2) · **sessions de génération** 1

Les récurrences vectorielles et les produits de matrices : une récurrence linéaire avec entrée, sa solution par les puissances de la matrice et sa réponse impulsionnelle (la sortie est une convolution de l'entrée) ; les puissances d'une matrice, ses valeurs propres complexes, la forme exponentielle et les rotations ; le rayon spectral d'une matrice quelconque et la croissance transitoire ; les normes induites, leur sous-multiplicativité et ρ ≤ ‖A‖ ; les produits de matrices différentes et les facteurs dans [0, 1] ; les produits de jacobiennes le long d'une trajectoire ; la sensibilité à un paramètre utilisé à chaque pas, une somme sur le temps ; et borner un vecteur fait de plusieurs blocs. workbookIA 22 applique ces outils aux réseaux récurrents et au gradient qui s'évanouit ou explose.

**Temps** : 15,6 h en parcours complet, 11,8 h en parcours essentiel (lecture 160 min, 22 flashcards).

**Objectifs**

- Résoudre une récurrence linéaire vectorielle avec entrée, et lire sa réponse impulsionnelle comme une convolution.
- Calculer les puissances d'une matrice, ses valeurs propres complexes sous forme exponentielle, et reconnaître une rotation et une homothétie.
- Décider si Aᵗ tend vers 0 par le rayon spectral, et repérer une croissance transitoire.
- Calculer les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice, et majorer la norme d'un produit.
- Suivre un produit de facteurs dans [0, 1] et un produit de jacobiennes le long d'une trajectoire.
- Écrire la sensibilité de l'état final à un paramètre utilisé à chaque pas comme une somme sur le temps.
- Ramener sous un seuil un vecteur fait de plusieurs blocs sans changer sa direction.

**Sections de la fiche**

- §1 Récurrences linéaires vectorielles avec entrée : solution et réponse impulsionnelle
- §2 Puissances d'une matrice : valeurs propres complexes, forme exponentielle et rotations
- §3 Le rayon spectral : Aᵗ → 0 si et seulement si ρ(A) < 1, et la croissance transitoire
- §4 Normes de matrices : normes induites, sous-multiplicativité et ρ ≤ ‖A‖
- §5 Produits de matrices différentes, et des facteurs dans [0, 1]
- §6 Récurrences non linéaires : des produits de jacobiennes le long d'une trajectoire
- §7 La sensibilité à un paramètre utilisé à chaque pas : une somme sur le temps
- §8 Borner un vecteur fait de plusieurs blocs

**Notions enseignées** : récurrence linéaire vectorielle avec entrée x_{t+1} = A x_t + B u_t : solution, réponse impulsionnelle C Aᵏ B, sortie = convolution de l'entrée par la réponse impulsionnelle · puissances d'une matrice diagonalisable ; valeurs propres complexes d'une matrice réelle 2 × 2 : rotation et homothétie · nombres complexes : forme exponentielle r e^{iθ} (formule d'Euler admise), produit = rotation et homothétie, puissances (formule de Moivre) · rayon spectral d'une matrice quelconque ; Aᵗ → 0 si et seulement si ρ(A) < 1 (démontré pour une matrice diagonalisable sur ℂ) · croissance transitoire d'une matrice non normale · normes induites ‖·‖₁ (colonnes), ‖·‖∞ (lignes) et ‖·‖₂ = s_max ; sous-multiplicativité ; ‖Aᵀ‖₂ = ‖A‖₂ ; ‖diag(d)‖ = max |dᵢ| ; ρ(A) ≤ ‖A‖ pour ces trois normes (par un vecteur propre de ℂⁿ) ; formule de Gelfand (énoncée) · matrices orthogonales sous les puissances : normes conservées · produits de matrices différentes : ‖A_T ⋯ A_1‖ ≤ ‖A_T‖ ⋯ ‖A_1‖ ; produits de matrices diagonales · récurrence affine diagonale à facteurs dans [0, 1] : ce qui reste après n étapes, (1 − ε)ⁿ ≈ e^{−nε}, demi-vie · produits de facteurs aléatoires : moyenne géométrique et signe de E[ln a] · récurrence non linéaire : la jacobienne de x_T par rapport à x_t est un produit de jacobiennes ; contraction et point fixe attractif · sensibilité de l'état final à un paramètre utilisé à chaque pas : elle suit une récurrence linéaire avec entrée, dont la solution est une somme sur le temps ; somme tronquée · norme d'un vecteur fait de plusieurs blocs ; le projeter en entier sur une boule garde sa direction, projeter chaque bloc non (rappel de M19)

**Prérequis** : suites géométriques (R5) · exponentielle et logarithme (R6) · loi des grands nombres (M02c) · inégalité de Jensen (M06) · normes de vecteurs (M07) · matrices orthogonales (M12b) · diagonalisation, valeurs propres, le strict minimum sur les nombres complexes (M12c) · valeurs singulières, normes de Frobenius et spectrale (M12d) · (1 + x/n)ⁿ → eˣ (M14) · variances multipliées d'étage en étage (M16) · jacobienne, règle de la chaîne, longues compositions (M17) · somme sur les chemins d'un graphe de calcul (M18) · itérations linéaires et rayon spectral d'une matrice symétrique, récurrences d'ordre 2, module d'un produit de complexes, projection sur une boule (M19) · produits de jacobiennes proches de l'identité, exponentielle de matrice (M20) · convolution de deux suites (M21)

**mymath** : `recurrence.py` (signatures figées) : `linear_system_states`, `operator_norm`, `product_norms`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 22.6 ∂ Pourquoi le gradient s'évanouit : un produit de dérivées de tanh · 22.7 ∂ Le chemin additif de la cellule LSTM · 22.1 ✏️ Combien de fenêtres ? Températures, taches solaires et Holmes · 22.2 ✏️ Dérouler à la main une cellule RNN scalaire sur trois pas · 22.3 ✏️ Compter les poids : la cellule à 69 poids du livre, puis nn.RNN et nn.LSTM · 22.4 ✏️ Un pas de LSTM à la main · 22.5 ✏️ Softmax avec température à la main · 22.8 🧮 Fermi : les 17 millions de poids du CNN-LSTM et le prix d'une epoch · 22.9 🗣️ Expliquer l'état caché d'un RNN en cinq lignes · 22.11 📄 Lire Hochreiter et Schmidhuber (1997) : Long Short-Term Memory · 22.19 🔬 Mesurer la disparition du gradient : RNN tanh contre LSTM · 22.24 🔮 Température : prédire l'allure du texte généré · 22.26 📈 Lire la courbe de loss et la perplexité du générateur · 22.Q6 🧠 BPTT, gradients évanescents et explosifs, dépendances longues · 22.Q7 🧠 Une porte, c'est une multiplication · 22.Q8 🧠 Oublier, se souvenir, sélectionner · 22.Q9 🧠 LSTM ou GRU ? · 22.R2 🔁 Gradient clipping et optimiseurs adaptatifs · 22.E2 💼 Explique le gradient évanescent et deux façons d'y remédier · 24.6 ∂ Dropout inversé et max-norm : espérance et projection · 19.19 🔨 Warmup + cosinus et gradient clipping

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M22.Q1 | 🧠 | La solution d'une récurrence avec entrée : quelles puissances, quels termes ? | ★ | 4 | §1 | C, E | manuel | — |
| M22.Q2 | 🧠 | Valeurs propres complexes, module, forme exponentielle et rotation : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| M22.Q3 | 🧠 | Le rayon spectral décide-t-il de tout ? Le long terme et les premiers pas | ★ | 4 | §3 | C, E | manuel | — |
| M22.Q4 | 🧠 | Normes induites : laquelle se calcule à la main, laquelle borne quoi ? | ★ | 4 | §4 | C, E | manuel | — |
| M22.Q5 | 🧠 | Un produit de facteurs dans [0, 1] : ce qui reste après n étapes | ★ | 4 | §5 | C, E | manuel | — |
| M22.Q6 | 🧠 | Contraction et point fixe : lire une jacobienne | ★ | 4 | §6 | C, E | manuel | — |
| M22.Q7 | 🧠 | Une somme sur le temps, sur un modèle de pêche chiffré : vrai ou faux | ★ | 4 | §7 | C | manuel | — |
| M22.Q8 | 🧠 | Ramener un vecteur sous un seuil : le tout ou chaque bloc ? | ★ | 4 | §8 | C | manuel | — |
| M22.R1 | 🔁 | La diagonalisation et les puissances d'une matrice (M12c) | ★ | 8 | §2 | C, E | manuel | — |
| M22.R2 | 🔁 | Valeurs singulières et norme spectrale (M12d) | ★ | 5 | §4 | C, E | manuel | — |
| M22.R3 | 🔁 | La règle de la chaîne comme produit de jacobiennes (M17) | ★ | 5 | §6 | C, E | manuel | — |
| M22.1 | ✏️ | Une population à trois classes d'âge, avec des arrivées : trois pas à la main, et la solution écrite avec les puissances | ★★ | 25 | §1 | C, E | wbm | — |
| M22.2 | ✏️ | La réponse impulsionnelle de deux réservoirs en cascade, et la sortie comme convolution de l'entrée | ★★ | 25 | §1 | C, E | wbm | — |
| M22.3 | ✏️ | Une matrice de rotation et d'homothétie : valeurs propres complexes, forme exponentielle, puissances | ★★ | 20 | §2 | C, E | wbm | — |
| M22.4 | ✏️ | Le rayon spectral de trois matrices 2 × 2 non symétriques, et le comportement de leurs puissances | ★★ | 20 | §3 | C, E | wbm | — |
| M22.5 | ✏️ | Une matrice triangulaire de rayon spectral < 1 dont les puissances grandissent d'abord : Aᵗ en formule | ★★ | 30 | §3 | C, E | wbm | — |
| M22.6 | ✏️ | Les normes ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice 2 × 2, et trois majorations de ‖A⁵x‖ | ★★ | 25 | §4 | C, E | wbm | — |
| M22.7 | ✏️ | Trois équipements qui s'usent à des rythmes différents : une récurrence diagonale, ce qui reste, et la demi-vie | ★ | 15 | §5 | C, E | wbm | — |
| M22.8 | ✏️ | Les jacobiennes d'une application du plan en trois points d'une trajectoire, et leur produit | ★★ | 20 | §6 | C, E | wbm | — |
| M22.9 | ✏️ | Un capital placé à taux fixe avec des versements : la dérivée du capital final par rapport au taux, une somme sur les années | ★★ | 25 | §7 | C, E | wbm | — |
| M22.10 | ✏️ | La norme globale de trois blocs, et deux façons de les ramener sous un seuil | ★ | 15 | §8 | C, E | wbm | — |
| M22.11 | ∂ | Sous-multiplicativité, ‖Aᵀ‖₂ = ‖A‖₂, ‖diag(d)‖₂ = max |dᵢ| et ρ(A) ≤ ‖A‖ | ★★ | 35 | §4 | C, E | manuel | — |
| M22.12 | ∂ | La norme induite ‖·‖∞ est le maximum des sommes de lignes | ★★ | 20 | §4 | C | manuel | — |
| M22.13 | ∂ | Aᵗ → 0 si et seulement si ρ(A) < 1, pour une matrice diagonalisable sur ℂ | ★★ | 30 | §3 | C, E | manuel | — |
| M22.14 | ∂ | Une application contractante oublie son point de départ : l'écart entre deux trajectoires décroît géométriquement | ★★ | 20 | §6 | C | manuel | — |
| M22.15 | ∂ | La sensibilité de l'état final à un paramètre utilisé à chaque pas suit une récurrence avec entrée : sa solution est une somme sur le temps | ★★ | 25 | §7 | C | manuel | — |
| M22.16 | 🔗 | Pont : la convention ligne x_{t+1} = x_t A + u_t B, ses formes, et la jacobienne Aᵀ | ★ | 20 | §1 §6 | C, E | wbm | — |
| M22.17 | 📖 | MML §4.2 relu : les cinq applications du plan de la figure 4.4, leurs valeurs propres, et le comportement de leurs puissances | ★★ | 40 | §2 §3 | C | manuel | — |
| M22.18 | 🗣️ | Expliquer avec une image non mathématique pourquoi un système linéaire oublie son passé au rythme de ρ(A) | ★ | 10 | §3 | C, E | manuel | — |
| M22.E1 | 💼 | « Quelle différence entre le rayon spectral et la norme d'une matrice ? » | ★ | 10 | §3 §4 | C | manuel | — |
| M22.E2 | 💼 | « Pourquoi Aⁿ peut-il grandir longtemps alors que toutes les valeurs propres de A sont de module < 1 ? » | ★ | 10 | §3 | C | manuel | — |
| M22.19 | 🔨 | Les états d'une récurrence linéaire avec entrée · `linear_system_states` | ★ | 25 | §1 | C, E | pytest | — |
| M22.20 | 🔨 | Les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂ · `operator_norm` | ★★ | 30 | §4 | C, E | pytest | — |
| M22.21 | 🔨 | Les normes des produits cumulés, et leur majoration · `product_norms` | ★ | 25 | §5 §6 | C, E | pytest | — |
| M22.22 | 📦 | `np.linalg.eigvals` et `np.linalg.norm` : rayon spectral et normes de matrices tirées au hasard, et ρ ≤ ‖A‖ | ★ | 15 | §3 §4 | C | wbm | — |
| M22.23 | 🔮 | Prédire l'allure de ‖Aᵗ‖₂ pour une matrice non normale de rayon spectral 0,8, puis tracer | ★ | 20 | §3 | C, E | wbm | M22.20 |
| M22.24 | 🔬 | Des produits de matrices aléatoires : le taux de croissance (1/n) ln ‖Aₙ ⋯ A₁‖ | ★★ | 25 | §5 | C | wbm | M22.21 |
| M22.25 | 🎨 | Les spirales d'une récurrence 2 × 2 à valeurs propres complexes, selon leur module | ★ | 20 | §2 | C, E | manuel | — |
| M22.26 | 🐛 | Chasse à l'erreur : ρ(A) pris pour ‖A‖, un produit de jacobiennes dans le mauvais ordre, un seuil appliqué bloc par bloc | ★ | 25 | §3 §6 §8 | C, E | wbm | — |
| M22.27 | 🛠️ | Un test de propriété : ‖AB‖ ≤ ‖A‖ ‖B‖ et ρ(A) ≤ ‖A‖ sur des matrices tirées au hasard | ★ | 30 | §4 | C | manuel | M22.20 |
| M22.28 | 🏆 | Défi : une matrice 3 × 3 à coefficients dans [−3, 3], de rayon spectral 0,85, dont une puissance a une norme ‖·‖₂ supérieure à 100 | ★★★ | 25 | §3 | C | wbm | M22.20 |

*Notes* : Frontières : les ∂ 22.6 (le produit de dérivées de tanh, les bornes |w|^{T−t} et σ_max(W_hh)^{T−t}, la somme ∂L/∂w, la tanh composée) et 22.7 (le chemin additif, diag(Π f), le biais d'oubli, le GRU), 22.1 (fenêtres), 22.2 (dérouler une cellule), 22.3 (compter les poids), 22.4 (un pas de LSTM), 22.5 et 22.24 (température), 🧮 22.8, 🗣️ 22.9, 📄 22.11, 🔬 22.19, 📈 22.26, les quiz 22.Q6 à 22.Q9, 22.R2 (le clipping de (3, 4)) et 22.E2, et, de workbookIA 24, le ∂ 24.6 (la max-norm par canal, w = (3, 4, 12), c = 3 : projeter chaque bloc). M22 enseigne les outils hors réseau : populations par classes d'âge, réservoirs, placements, usure d'équipements, applications du plan, jamais une cellule, une porte, une sigmoïde, une tanh composée ni une loss. Ce que ∂ 22.6.5 admet est démontré en général (∂ M22.11 : sous-multiplicativité, ‖Aᵀ‖₂ = ‖A‖₂, ‖diag(d)‖₂ = max |dᵢ|, ρ ≤ ‖A‖), sans diag(1 − h²) ni W_hh ; aucun exercice ne borne un produit de facteurs diag(dₖ) M avec |dₖ| ≤ 1, ni n'itère une application φ(M x + c) appliquée coordonnée par coordonnée (de jacobienne diag(φ′) M) : c'est la structure de ∂ 22.6.5 ; les jacobiennes de M22.8 viennent d'une application du plan d'une autre forme (Hénon, proie-prédateur). La récurrence affine diagonale (§5) porte sur l'usure de trois équipements, avec (1 − ε)ⁿ ≈ e^{−nε} et la demi-vie (ni 0,9 ni 0,99 comme facteurs, nombres de 26.7.4), sans porte, sigmoïde, biais ni comparaison avec un « RNN simple » (∂ 22.7). La somme sur le temps (§7, ∂ M22.15) porte sur un capital placé à taux fixe et sur un modèle de pêche, sans δ_k ni « dépendances lointaines » (∂ 22.6.6) : ∂ M22.15 démontre que la sensibilité suit une récurrence avec entrée (le §1 donne alors la somme), et que les derniers pas dominent quand les produits décroissent n'est que constaté sur les nombres de M22.9, jamais énoncé en général (c'est l'explication que demande ∂ 22.6.6 ; précédent de M16.6) ; la somme tronquée aux K derniers pas est une remarque (la BPTT tronquée de workbookIA 22 et l'état porté de workbookIA 24 restent à workbookIA). Les nombres complexes : la forme exponentielle (formule d'Euler admise), le produit comme rotation et homothétie, les puissances (Moivre), à la suite de M12c §3 et M19 §6 ; MB3 s'en servira. Le rayon spectral d'une matrice non symétrique (M19 n'avait que le cas symétrique) : Aᵗ → 0 ⇔ ρ(A) < 1, démontré pour une matrice diagonalisable sur ℂ (∂ M22.13) et admis en général, la croissance transitoire d'une matrice non normale (M22.5, 🔮 M22.23, 🏆 M22.28), la formule de Gelfand énoncée. Le §8 reprend la projection sur une boule de M19 (∂ M19.13) pour un vecteur fait de plusieurs blocs : la norme globale, projeter le tout garde la direction, projeter chaque bloc non ; sans `clip_grad_norm_`, gradient, constante 10⁻⁶, vecteur (3, 4) ni seuils 1 et 0,25. Évités (règle de partage) : les puissances 0,7²⁰, 1,2²⁰, 0,95¹⁰⁰, 1,05¹⁰⁰, 0,9⁵⁰, 1,1⁵⁰, 1,5²⁰, 0,5¹⁹, 0,5¹⁰, 0,99¹⁰⁰, 0,9¹⁰⁰, 0,5²⁰, 0,73²⁰, 0,95⁵⁰ et 0,7311³⁰ et leurs valeurs (8 × 10⁻⁴, 38, 131, 0,006, 117, 0,0052, 3 325, 0,37, 2,7 × 10⁻⁵, 0,077, 10⁻⁷) ; σ(0) = 0,5 et σ(1) ≈ 0,73 comme facteurs ; le facteur 10 tous les 4 pas, T = 80 et H = 32, les distances 10, 40 et 79 ; la cellule tanh(0,7 x + 0,3 h), (u, w, b, v) = (1 ; 0,5 ; 0 ; 2) avec x = (2, 0, −1) ou (1, 1, 1), le point fixe h = tanh(1 + 0,5 h) ; les poids du LSTM de 22.4 et de CP5.3 de workbookIA, c = 2 ou 3 ; les logits (3 ; 1 ; 0,5), (1, 2, 3), (2, 1, 0) et (2 ; 2 ; 0) ; 69 poids, D = 50 et H = 20, (10, 8, 3) ; les fenêtres de 22.1 ; la tanh composée et ses pentes 0,42, 0,25, 0,096 et 0,012 ; l'initialisation orthogonale contre l'initialisation par défaut d'un réseau ; la boîte de pièces, le carnet du comptable, la balle, Holmes, Verne, les taches solaires (et le modèle AR(2) de Yule, qui porte sur elles), le sinus de période 24, « deux chats… ils ». ∂ M22.14 ne démontre que l'oubli du point de départ, ni l'existence du point fixe par une suite de Cauchy, ni une contraction en norme max d'un maximum d'applications affines (les deux moitiés de ∂ 26.8.3, Bellman, future frontière de M26). Le 🔬 M22.24 choisit des longueurs sans débordement, ou renormalise le produit à chaque pas en cumulant le logarithme de la norme. Conventions : colonnes (x_{t+1} = A x_t + B u_t, comme MML et M19) ; le pont M22.16 passe à la convention ligne de workbookIA (x A, de jacobienne Aᵀ). `recurrence` : NumPy permis, mais de `np.linalg` seulement `eigvalsh` (dans `operator_norm`) et `norm` (dans `product_norms`), et aucune fonction de SciPy (`matrix_norm`, `svdvals` et `scipy.linalg.norm` donneraient `operator_norm`) ; aucune fonction de cellule, de fenêtres, de température ni de clipping (`clip_grad_norm` est dans le `mylearn` de workbookIA 19) ; pas de fonction de réponse impulsionnelle (M22.2 la calcule à la main). MML : §4.2 relu (📖 M22.17 : la figure 4.4 et ses cinq applications du plan, dont la rotation, que la définition 4.6 laisse sans valeur propre réelle) ; MML ne traite ni les normes induites ni les produits de matrices. L'injectivité d'une convolution pleine et la série I + A + A² + … quand ‖A‖ < 1 ne sont pas démontrées ici : ce sont les sujets de CP5.8. 13,5 h au lieu des 10 h prévues : les normes induites et leurs propriétés, que ∂ 22.6.5 admet, et le rayon spectral d'une matrice non symétrique, que le corrigé de workbookIA 22 suppose.

<a id="cp5"></a>
## CP5 · Examen blanc de la partie V

**Partie** V · **prépare** — · **dossier** `checkpoints/partie_5/` · **MML** — · **sessions de génération** 1

Le bilan de la partie V (M21 et M22), juste avant le checkpoint V de workbookIA : un examen blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.

**Temps** : 3,1 h en parcours complet, 3,1 h en parcours essentiel (lecture 15 min, 0 flashcards).

**Objectifs**

- Vérifier en temps limité que les notions de la partie V sont acquises.
- Construire ta propre synthèse de la partie V.

**Sections de la fiche**

- §1 Examen blanc
- §2 Synthèse

**Notions enseignées** : révision de la partie V

**Prérequis** : toute la partie V (M22)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 21.R2 🔁 Le gradient d'un poids utilisé à plusieurs endroits · 21.Q3 🧠 Convolution ou corrélation croisée ? · 21.Q4 🧠 Détecteurs de motifs et hiérarchie de filtres · 21.Q5 🧠 Padding et stride : que devient la taille ? · 21.Q6 🧠 Canaux d'entrée, nombre de filtres, canaux de sortie · 21.Q7 🧠 Convolution 1D ou convolution 1×1 ? · 21.Q9 🧠 Convolution transposée : les mots piégés · 21.Q11 🧠 Exemples adversariaux : vrai ou faux ? · 21.1 ✏️ Le détecteur de jaune à la main · 21.2 ✏️ Une corrélation 5×5 par 3×3 à la main · 21.3 ✏️ Tailles de sortie : padding, stride et la hiérarchie 600 → 300 → 100 · 21.4 ✏️ Compter les paramètres : convolution contre couche dense · 21.5 ✏️ Champ récepteur effectif d'une pile convolution + pooling · 21.6 ✏️ Convolution transposée à la main : insérer des zéros puis corréler · 21.7 ∂ Rétropropager dans une convolution 1D : la somme sur les positions · 21.8 🧮 Fermi : paramètres, mémoire et calcul de VGG16 · 21.11 📄 Lire LeCun et coll. (1998) : LeNet-5 · 21.17 🎨 Reproduire la chasse aux rayures verticales (Fig. 21.14) · 21.20 🔮 Conv1d, noyau pleine largeur et 1×1 : prédire formes et paramètres · 21.26 🔬 Stride ou pooling : accuracy et temps sur CIFAR-10 · 21.29 📦 Attaque FGSM contre ton CNN Fashion-MNIST · 21.E2 💼 Taille de sortie et paramètres d'une Conv2d(3, 64, 3, stride=2, padding=1) sur une image 224×224 · 21.E3 💼 À quoi sert une convolution 1×1 ? · 22.1 ✏️ Combien de fenêtres ? Températures, taches solaires et Holmes · 22.2 ✏️ Dérouler à la main une cellule RNN scalaire sur trois pas · 22.3 ✏️ Compter les poids : la cellule à 69 poids du livre, puis nn.RNN et nn.LSTM · 22.4 ✏️ Un pas de LSTM à la main · 22.5 ✏️ Softmax avec température à la main · 22.6 ∂ Pourquoi le gradient s'évanouit : un produit de dérivées de tanh · 22.7 ∂ Le chemin additif de la cellule LSTM · 22.8 🧮 Fermi : les 17 millions de poids du CNN-LSTM et le prix d'une epoch · 22.9 🗣️ Expliquer l'état caché d'un RNN en cinq lignes · 22.11 📄 Lire Hochreiter et Schmidhuber (1997) : Long Short-Term Memory · 22.19 🔬 Mesurer la disparition du gradient : RNN tanh contre LSTM · 22.24 🔮 Température : prédire l'allure du texte généré · 22.26 📈 Lire la courbe de loss et la perplexité du générateur · 22.Q6 🧠 BPTT, gradients évanescents et explosifs, dépendances longues · 22.Q7 🧠 Une porte, c'est une multiplication · 22.Q8 🧠 Oublier, se souvenir, sélectionner · 22.Q9 🧠 LSTM ou GRU ? · 22.R1 🔁 Une convolution 1D peut-elle lire une séquence ? · 22.R2 🔁 Gradient clipping et optimiseurs adaptatifs · 22.E2 💼 Explique le gradient évanescent et deux façons d'y remédier · 24.R2 🔁 Taille de sortie d'une convolution à padding 'same' et stride 2 · 24.2 ✏️ Formes et paramètres du CNN à pooling du livre · 24.3 ✏️ Stride ou pooling : compter les multiplications · 24.6 ∂ Dropout inversé et max-norm : espérance et projection · 24.Q9 🧠 Motifs conv-conv-pool, stride contre pooling, batchnorm contre dropout

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| CP5.Q1 | 🧠 | Dix affirmations sur la partie V : vrai ou faux | ★ | 10 | §1 | C, E | manuel | — |
| CP5.1 | ✏️ | Convolution de deux suites, corrélation croisée et matrice de Toeplitz | ★★ | 10 | §1 | C, E | wbm | — |
| CP5.2 | ✏️ | Positions d'une fenêtre, pas, dilatation, et la convolution transposée d'un signal | ★★ | 10 | §1 | C, E | wbm | — |
| CP5.3 | ✏️ | Une grille filtrée par un noyau séparable : paramètres, coût et champ récepteur | ★★ | 10 | §1 | C, E | wbm | — |
| CP5.4 | ✏️ | Équivariance, matrice circulante et le pire cas d'une perturbation bornée | ★★ | 9 | §1 | C, E | wbm | — |
| CP5.5 | ✏️ | Une récurrence avec entrée : solution et réponse impulsionnelle | ★★ | 10 | §1 | C, E | wbm | — |
| CP5.6 | ✏️ | Valeurs propres complexes, rayon spectral, normes et croissance transitoire | ★★ | 10 | §1 | C, E | wbm | — |
| CP5.7 | ✏️ | Produits de jacobiennes le long d'une trajectoire, et sensibilité à un paramètre utilisé à chaque pas | ★★ | 9 | §1 | C, E | wbm | — |
| CP5.8 | ∂ | Une démonstration au choix : une convolution pleine est injective, ou la série I + A + A² + … quand ‖A‖ < 1 | ★★★ | 12 | §1 | C, E | manuel | — |
| CP5.9 | 🐛 | Corriger une copie : cinq erreurs | ★★ | 8 | §1 | C, E | wbm | — |
| CP5.10 | 🔗 | Problème de synthèse : un filtre récursif et un filtre à réponse finie, du signal à la stabilité | ★★ | 14 | §1 | C, E | wbm | — |
| CP5.11 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme CP4 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, 03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend le checkpoint V de workbookIA (`checkpoints/partie_5/` de workbookIA : les formes de Conv2d, MaxPool2d, LSTM et GRU de CP5.1, le CNN CIFAR-10 de CP5.2 (champ récepteur 18, 294 912 MAC, 24 234 paramètres), un pas de LSTM (CP5.3), les bugs de CP5.4, `rnn_forward` (CP5.5, graine 55), l'early stopping (CP5.6), les courbes (CP5.7), le Fermi d'un générateur de mots (CP5.8), la validation croisée et le gradient d'une couche dense (CP5.10), CP5.11 (168, 1 920, 32, 320 000) et la ∂ de CP5.12, une rétropropagation dans une convolution 1D (x = (1 ; 2 ; −1 ; 3), w = (1, −1)), frontière), qui se fait juste après, ni son mini-projet V (un classifieur CIFAR-10 : small_cnn, vgg, resnet, FGSM à ε = k/255). La synthèse ne recopie pas le tableau des 22 formules de la synthèse de workbookIA. CP5.8 donne le choix entre deux énoncés que M21 et M22 ne démontrent pas : une convolution pleine par un noyau non nul est injective (par la matrice de Toeplitz ou par les polynômes), ou, si ‖A‖ < 1 pour une norme induite, I − A est inversible, (I − A)⁻¹ = I + A + A² + … et ‖(I − A)⁻¹‖ ≤ 1/(1 − ‖A‖) ; aucune ne touche à un gradient de convolution ni à un produit de dérivées de tanh. CP5.10 relie les deux chapitres hors réseau : un filtre récursif à état de dimension 2 (une récurrence avec entrée, pour que le rayon spectral ne soit pas un simple |a|), sa réponse impulsionnelle, et un filtre à réponse finie (une convolution), jusqu'à la stabilité par le rayon spectral ; pas de lissage exponentiel b = 1 − a avec correction du biais, ni β = 0,9, 0,95, 0,99 ou 0,999 (∂ 19.8 et ∂ 26.7 de workbookIA).

<a id="m25a"></a>
## M25a · Gaussienne multivariée, conditionnement et divergence KL

**Partie** VI · **prépare** workbookIA 25 · **dossier** `chapitres/m25a_gaussienne/` · **MML** §6.5, §6.7, §9.3 · **sessions de génération** 2

La loi normale multivariée : sa densité (le déterminant et la distance de Mahalanobis), les transformations affines et le changement de variable multivarié (la loi de μ + Lε et l'échantillonnage par Cholesky), la géométrie (ellipses de niveau, masse d'une ellipse, loi de la norme), les matrices par blocs et le complément de Schur (lois marginales et conditionnelles, matrice de précision), Bayes avec des gaussiennes (produit de densités, modèle linéaire gaussien, régression linéaire bayésienne), le maximum de vraisemblance de μ et Σ, la divergence KL continue (Jensen, positivité, additivité, KL entre deux gaussiennes), et l'interpolation sphérique. workbookIA 25 s'en sert pour le prior et l'encodeur probabiliste du VAE, son terme KL et l'interpolation entre deux codes.

**Temps** : 20,3 h en parcours complet, 15,0 h en parcours essentiel (lecture 185 min, 24 flashcards).

**Objectifs**

- Écrire et évaluer la densité et la log-densité d'une loi normale multivariée, et y lire le rôle de det Σ et de la distance de Mahalanobis.
- Trouver la loi d'une transformation affine ou d'une somme de vecteurs gaussiens par le changement de variable multivarié, et tirer un vecteur de loi N(μ, Σ) sous la forme μ + Lε, par Cholesky.
- Tracer les ellipses de niveau d'une gaussienne, calculer la masse d'une ellipse en dimension 2, et décrire la loi de la norme d'un vecteur gaussien en dimension d.
- Calculer un complément de Schur, une loi marginale et une loi conditionnelle, et lire une matrice de précision.
- Multiplier deux densités gaussiennes, et calculer le posterior, la prédictive et l'évidence d'une régression linéaire bayésienne.
- Démontrer le maximum de vraisemblance de μ et Σ avec les gradients de ln det et de la trace.
- Définir la divergence KL continue, démontrer sa positivité (Jensen) et son additivité, et calculer la KL entre deux gaussiennes multivariées.
- Démontrer les propriétés de l'interpolation sphérique et l'appliquer à un trajet sur une sphère.

**Sections de la fiche**

- §1 La densité de la loi normale multivariée : de N(0, I) à N(μ, Σ), déterminant et distance de Mahalanobis
- §2 Transformations affines, sommes et changement de variable : la loi de μ + Lε et l'échantillonnage par Cholesky
- §3 Géométrie : ellipses de niveau, masse d'une ellipse et loi de la norme
- §4 Matrices par blocs et complément de Schur : lois marginales, lois conditionnelles et matrice de précision
- §5 Bayes avec des gaussiennes : produit de densités, modèle linéaire gaussien et régression linéaire bayésienne
- §6 Estimer μ et Σ : le maximum de vraisemblance et le gradient de ln det
- §7 La divergence KL continue : Jensen, positivité, additivité, et la KL entre deux gaussiennes
- §8 L'interpolation sphérique : rester sur la sphère, à vitesse angulaire constante

**Notions enseignées** : loi normale multivariée N(μ, Σ) : densité, rôle de det Σ et de la distance de Mahalanobis, log-densité ; N(0, I) : d coordonnées indépendantes de loi N(0, 1) · vecteur gaussien : toute combinaison linéaire de ses coordonnées est gaussienne ; deux marginales gaussiennes ne font pas un vecteur gaussien (contre-exemple) · changement de variable multivarié : densité de U(X) par le déterminant de la jacobienne de U⁻¹ (MML §6.7.2, admis en général) · transformations affines : AX + b ~ N(Aμ + b, AΣAᵀ) ; somme de deux vecteurs gaussiens indépendants · loi de μ + Lε quand ε ~ N(0, I) : N(μ, LLᵀ) ; échantillonnage par Cholesky ; le blanchiment comme chemin inverse (rappel de M12c) · ellipses (ellipsoïdes) de niveau : axes propres de Σ, demi-axes c√λᵢ, aire πc²√(det Σ) · masse d'une ellipse de Mahalanobis en dimension 2 : 1 − e^{−c²/2} (blanchir, puis les coordonnées polaires) ; le carré de la distance de Mahalanobis suit une loi du khi-deux à d degrés (nommée) · loi de la norme d'un vecteur de loi N(0, I_d) : densité proportionnelle à r^{d−1} e^{−r²/2}, mode √(d − 1) ; la densité est maximale au centre, la masse est sur une couronne (suite de M07) · matrices par blocs : inverse par blocs, complément de Schur, det M = det D · det(A − BD⁻¹C) · lois marginales d'un vecteur gaussien (les sous-blocs) ; loi conditionnelle : moyenne affine en la valeur observée, covariance égale au complément de Schur, qui ne dépend pas de cette valeur · pour un vecteur gaussien, décorrélé équivaut à indépendant ; matrice de précision Σ⁻¹ : un zéro hors de la diagonale veut dire l'indépendance conditionnelle sachant les autres coordonnées · produit de deux densités gaussiennes : une densité gaussienne à un facteur près (les précisions s'additionnent, la moyenne est pondérée par les précisions) ; fusion de mesures · modèle linéaire gaussien x ~ N(m, V), y = Ax + b + w : loi jointe, loi marginale de y, loi de x sachant y · régression linéaire bayésienne (MML §9.3) : posterior N(m_N, S_N), prédictive, vraisemblance marginale (évidence) ; avec m₀ = 0 et S₀ = τ²I, la moyenne a posteriori est la solution ridge de λ = σ²/τ² · maximum de vraisemblance de μ et Σ : μ̂ = x̄ et Σ̂ = (1/n) Σᵢ (xᵢ − x̄)(xᵢ − x̄)ᵀ, par les gradients de ln det et de la trace (M18) ; Σ̂ singulière quand n ≤ d · inégalité de Jensen pour une variable continue (démontrée par une tangente) · divergence KL continue KL(p ‖ q) = E_p[ln p − ln q] : positivité, nullité si et seulement si p = q, valeur infinie quand le support de q ne couvre pas celui de p, asymétrie ; additivité pour des lois produits · entropie différentielle de N(μ, Σ) : ½ ln((2πe)^d det Σ), qui peut être négative · KL entre deux gaussiennes multivariées N(μ₀, Σ₀) et N(μ₁, Σ₁), par le lemme E[(x − m)ᵀA(x − m)] = tr(AΣ) + (μ − m)ᵀA(μ − m) ; même covariance : la moitié du carré d'une distance de Mahalanobis · formules de soustraction sin(γ − ψ) et cos(γ − ψ), déduites de la forme exponentielle de M22 · interpolation sphérique (slerp) : formule, extrémités, norme conservée entre deux vecteurs de même norme, angle parcouru proportionnel à t, limite linéaire quand l'angle tend vers 0 ; arc et corde

**Prérequis** : cosinus, sinus, radians (R9) · intégration par parties, intégrales impropres (M02a) · loi normale, changement de variable en dimension 1, théorème de transfert, intégrale double et coordonnées polaires (M02b) · matrice de covariance empirique, estimateur biaisé en 1/n (M02c) · convexité : une fonction convexe est au-dessus de ses tangentes (M05a) · formule de Bayes : a priori, vraisemblance, évidence, a posteriori (M04) · divergence KL discrète, inégalité de Jensen discrète, entropie (M06) · produit scalaire, angle, norme d'un vecteur gaussien en grande dimension (M07) · inverse d'une matrice, résolution d'un système (M09a) · ridge vue comme MAP, régression vue comme maximum de vraisemblance (M09b) · base orthonormée d'un plan, Gram-Schmidt (M12b) · déterminant, trace, théorème spectral, matrices définies positives, Cholesky, covariance AΣAᵀ, blanchiment, distance de Mahalanobis (M12c) · maximum de vraisemblance, log-vraisemblance, indépendance conditionnelle (Naïve Bayes) (M13a) · jacobienne d'une application de ℝⁿ dans ℝⁿ (M17) · gradient par rapport à une matrice : ∇ ln det X et ∇ tr(AX) (M18) · forme exponentielle des complexes, e^{ia} e^{ib} = e^{i(a + b)} (M22)

**mymath** : `gaussian.py` (signatures figées) : `mvn_logpdf`, `sample_mvn`, `schur_complement`, `condition_gaussian`, `linreg_posterior`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 25.5 ∂ Dériver à travers un tirage : l'astuce de reparamétrisation · 25.7 ∂ La divergence KL entre N(μ, σ²) et N(0, 1) · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé) · 25.6 ✏️ Où tombent les tirages d'une gaussienne en grande dimension · 25.20 🔨 Interpoler entre deux codes : linéaire et sphérique · 25.28 🔨 La reparamétrisation en NumPy : passe avant et passe arrière · 25.29 🔨 Divergence KL gaussienne et son gradient · 25.33 🎨 Reproduire le nuage latent d'un VAE 2D et la grille −3…3 (fig. 25.67-25.68) · 25.Q12 🧠 Les trois exigences d'un VAE et l'astuce de reparamétrisation · 25.R3 🔁 La divergence KL, ce que mesure le terme de régularisation du VAE · 25.E3 💼 Expliquer l'astuce de reparamétrisation · B5.6 ∂ Forme fermée : deux pas de bruit gaussien n'en font qu'un, d'où q(x_t | x_0)

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M25a.Q1 | 🧠 | Lire une densité gaussienne multivariée : det Σ, distance de Mahalanobis et point le plus probable | ★ | 4 | §1 | C, E | manuel | — |
| M25a.Q2 | 🧠 | Ce qui reste gaussien : images affines, sommes, produits et normes ; deux marginales gaussiennes ne suffisent pas | ★ | 4 | §2 | C, E | manuel | — |
| M25a.Q3 | 🧠 | Ellipses de niveau et masse : quel axe, quel demi-axe, quelle proportion, en dimension 2 et au-delà | ★ | 4 | §3 | C, E | manuel | — |
| M25a.Q4 | 🧠 | Complément de Schur, loi marginale ou loi conditionnelle : quel bloc, quelle moyenne, quelle variance ? | ★ | 6 | §4 | C, E | manuel | — |
| M25a.Q5 | 🧠 | Fusionner des mesures et mettre à jour un a priori gaussien : précisions, moyennes pondérées et prédictive | ★ | 4 | §5 | C, E | manuel | — |
| M25a.Q6 | 🧠 | Le maximum de vraisemblance de μ et Σ : diviser par n, et une covariance singulière quand n ≤ d | ★ | 4 | §6 | C | manuel | — |
| M25a.Q7 | 🧠 | La divergence KL continue en situations : deux supports qui ne se couvrent pas, deux lois exponentielles, une loi produit, et les deux sens | ★ | 4 | §7 | C, E | manuel | — |
| M25a.Q8 | 🧠 | Ligne droite ou arc de grand cercle : extrémités, norme et angle parcouru | ★ | 4 | §8 | C, E | manuel | — |
| M25a.R1 | 🔁 | Le changement de variable en dimension 1 et les coordonnées polaires (M02b) | ★ | 6 | §2 §3 | C, E | manuel | — |
| M25a.R2 | 🔁 | Le théorème spectral, Cholesky et la covariance AΣAᵀ (M12c) | ★ | 6 | §2 §3 | C, E | manuel | — |
| M25a.R3 | 🔁 | Les gradients de ln det X et de tr(AX) par rapport à une matrice (M18) | ★ | 6 | §6 | C | manuel | — |
| M25a.1 | ✏️ | La densité d'un couple gaussien (température et humidité d'une serre) en deux points : distance de Mahalanobis contre distance euclidienne | ★ | 25 | §1 | C, E | wbm | — |
| M25a.2 | ✏️ | Trois mesures corrélées : la loi d'une somme pondérée et d'une différence, puis un tirage μ + Lε par Cholesky et sa covariance | ★★ | 35 | §2 | C, E | wbm | — |
| M25a.3 | ✏️ | Les ellipses à 90 % et à 95 % des composantes du vent sur un site : axes, demi-axes, aire, et la part des relevés dans l'ellipse de niveau c | ★★ | 30 | §3 | C, E | wbm | — |
| M25a.4 | ✏️ | Un capteur en panne estimé par ses deux voisins : complément de Schur, loi conditionnelle en dimension 3, et l'écart-type gagné | ★★ | 35 | §4 | C, E | wbm | — |
| M25a.5 | ✏️ | Fusionner trois mesures d'une même distance : le produit de densités gaussiennes, des précisions qui s'additionnent, un ordre sans importance | ★ | 20 | §5 | C, E | wbm | — |
| M25a.6 | ✏️ | Étalonner un thermomètre par la régression linéaire bayésienne : loi jointe, évidence, posterior de (a, b), et prédictive près et loin des points d'étalonnage | ★★ | 45 | §5 | C | wbm | — |
| M25a.7 | ✏️ | La divergence KL continue entre deux lois exponentielles et entre deux lois uniformes : les deux sens, une KL infinie, et deux durées de vie indépendantes | ★★ | 25 | §7 | C, E | wbm | — |
| M25a.8 | ✏️ | Deux réglages d'une machine de découpe, deux gaussiennes en dimension 2 des erreurs de position : la KL dans les deux sens, et le cas de même covariance | ★★ | 30 | §7 | C, E | wbm | — |
| M25a.9 | ✏️ | La route orthodromique entre deux villes : angle au centre, point au tiers du trajet par le slerp, et profondeur du milieu de la corde | ★★ | 30 | §8 | C, E | wbm | — |
| M25a.10 | ∂ | Le changement de variable multivarié : la densité de μ + Lε est celle de N(μ, LLᵀ), et AX + b reste gaussien pour A inversible | ★★ | 30 | §1 §2 | C, E | manuel | — |
| M25a.11 | ∂ | La masse d'une ellipse de Mahalanobis en dimension 2 vaut 1 − e^{−c²/2} ; la densité de la norme en dimension d, et son mode √(d − 1) | ★★ | 30 | §3 | C, E | manuel | — |
| M25a.12 | ∂ | Le maximum de vraisemblance d'une gaussienne multivariée : μ̂ = x̄ et Σ̂ = S/n, par les gradients de ln det et de la trace | ★★ | 40 | §6 | C | manuel | — |
| M25a.13 | ∂ | L'inégalité de Jensen pour une variable continue, la positivité de la KL continue, et l'additivité de la KL sur des lois produits | ★★ | 35 | §7 | C, E | manuel | — |
| M25a.14 | ∂ | La KL entre N(μ₀, Σ₀) et N(μ₁, Σ₁) en dimension d, par le lemme de la trace ; l'entropie différentielle de N(μ, Σ) | ★★★ | 45 | §7 | C, E | manuel | — |
| M25a.15 | ∂ | Le slerp entre deux vecteurs de même norme reste sur la sphère et avance d'un angle constant ; sa limite quand l'angle tend vers 0 | ★★ | 25 | §8 | C, E | manuel | — |
| M25a.16 | 🔗 | Pont : des vecteurs rangés en lignes (n, d) comme dans les bibliothèques : tirer n points d'un coup par E Lᵀ + μ, la log-densité de chaque ligne, et la moyenne en nats par coordonnée | ★ | 25 | §1 §2 | C, E | wbm | — |
| M25a.17 | 📖 | MML §6.5 et la fin de §6.7.2 : densité, marginales et conditionnelles, produit, sommes et transformations, échantillonnage et changement de variable multivarié, en anglais | ★★ | 45 | §1 §2 §4 §5 | C | manuel | — |
| M25a.18 | 📖 | MML §9.3 : régression linéaire bayésienne, prédictions a priori et a posteriori, vraisemblance marginale, en anglais | ★★ | 45 | §5 | C | manuel | — |
| M25a.19 | 🗣️ | Expliquer avec deux thermomètres voisins pourquoi lire l'un resserre l'estimation de l'autre, et pourquoi la valeur lue ne change pas cette incertitude | ★ | 10 | §4 | C, E | manuel | — |
| M25a.E1 | 💼 | « Comment tirer un vecteur gaussien de covariance donnée à partir de tirages indépendants, et pourquoi Cholesky ? » | ★ | 10 | §2 | C | manuel | — |
| M25a.20 | 🔨 | La log-densité d'une loi normale multivariée, par Cholesky · `mvn_logpdf` | ★★ | 40 | §1 | C, E | pytest | — |
| M25a.21 | 🔨 | Tirer des vecteurs de loi N(μ, Σ) par Cholesky · `sample_mvn` | ★ | 20 | §2 | C, E | pytest | — |
| M25a.22 | 🔨 | Le complément de Schur d'un bloc, et la loi conditionnelle d'un vecteur gaussien · `schur_complement, condition_gaussian` | ★★ | 40 | §4 | C, E | pytest | — |
| M25a.23 | 🔨 | Le posterior d'une régression linéaire bayésienne · `linreg_posterior` | ★★ | 35 | §5 | C | pytest | — |
| M25a.24 | 📦 | `scipy.stats.multivariate_normal`, `np.cov` et `scipy.integrate` : tes log-densités, le maximum de vraisemblance, et la KL de M25a.8 par une intégrale double | ★ | 30 | §1 §6 §7 | C, E | wbm | M25a.20, M25a.8 |
| M25a.25 | 🔮 | Prédire la part des tirages dans l'ellipsoïde de Mahalanobis de même niveau quand la dimension passe de 2 à 10, puis mesurer | ★ | 15 | §3 | C, E | wbm | M25a.21 |
| M25a.26 | 🔬 | Conditionner par simulation : garder les tirages dont une mesure tombe près d'une valeur, et comparer à la loi conditionnelle exacte | ★★ | 25 | §4 | C | wbm | M25a.21, M25a.22 |
| M25a.27 | 🎨 | Les ellipses de niveau d'une gaussienne en dimension 2, une tranche (la loi conditionnelle) et une projection (la loi marginale), selon la corrélation | ★ | 25 | §3 §4 | C, E | manuel | M25a.22 |
| M25a.28 | 🐛 | Chasse à l'erreur : un tirage par E L au lieu de E Lᵀ, ln det Σ sans le facteur 2, et une covariance conditionnelle qui dépend de la valeur observée | ★ | 25 | §1 §2 §4 | C, E | wbm | — |
| M25a.29 | 🛠️ | Un test de propriété : la moyenne et la covariance empiriques de tes tirages, à une tolérance fixée par l'erreur type | ★★ | 30 | §2 | C | manuel | M25a.21 |
| M25a.30 | 🏆 | Défi : reconstruire les températures manquantes le long d'une route par la loi conditionnelle d'une gaussienne, sous une erreur quadratique moyenne fixée | ★★★ | 35 | §4 | C | wbm | M25a.22 |

*Notes* : Frontières : le ∂ 25.5 (les dérivées de z = μ + σε par rapport à μ et à s = ln σ², ε fixé, et E[z²] dérivée avant ou après l'espérance), le ∂ 25.7 (KL(N(μ, σ²) ‖ N(0, 1)) par E[(z − μ)²] et E[z²], puis en s = ln σ², ses dérivées et ses valeurs), le ∂ 25.8 (autoencodeur linéaire et ACP, déjà frontière de M12d), le ✏️ 25.6 (E‖z‖² = d, la norme typique √d, P(‖z‖ ≤ r) = 1 − e^{−r²/2} en r = 1 et 3, le rayon médian, le milieu de deux tirages indépendants), les 🔨 25.20 (`interpolate_latents`), 25.28 (`reparameterize` et sa passe arrière) et 25.29 (`gaussian_kl`, `gaussian_kl_grad` et leur variante contre N(0, τ²)), le 🎨 25.33 (le nuage des μ d'un VAE à deux latents contre le prior), le quiz 25.Q12, le rappel 25.R3 (la KL discrète dans les deux sens, en bits), le 💼 25.E3, et, de workbookIA B5 (préparé par MB5), le ∂ B5.6 (deux pas de bruit gaussien n'en font qu'un : aucun exercice ne compose x ↦ √a x + √(1 − a) ε). M25a travaille hors réseau : la température et l'humidité d'une serre, les composantes du vent, des capteurs voisins, des thermomètres, des mesures d'une même distance, des durées de vie, des trajets sur la Terre ; jamais un encodeur, un code latent, un prior de VAE, une image ni un décodeur. **La KL** : M25a définit la KL continue, démontre Jensen pour une variable continue (par une tangente), la positivité et l'additivité sur des lois produits (∂ M25a.13), l'entropie différentielle de N(μ, Σ) et la KL entre deux gaussiennes multivariées quelconques par le lemme de la trace, avec le cas de même covariance (∂ M25a.14) : un énoncé plus général que ∂ 25.7 (BIBLE §8). Garde-fous : jamais le cas particulier contre N(0, I), N(0, 1) ou N(0, τ²), ni une covariance diagonale comparée à l'identité, ni la formule ½(μ² + σ² − 1 − ln σ²) écrite, ni s = ln σ² ou une log-variance, ni une dérivée de la KL, ni « à μ fixé, quel σ² la rend minimale », ni une KL gaussienne convertie en bits ; ✏️ M25a.8 prend des covariances pleines en dimension 2 et deux lois non centrées ; l'additivité s'applique à des durées de vie exponentielles indépendantes (✏️ M25a.7), jamais à des latents ; aucun quiz « nulle exactement pour μ = 0 et σ = 1 », et M25a.Q7 ne reprend pas en continu les trois vrai ou faux de 25.R3 b-d (« symétrique ? », « KL(P ‖ P) = 0 ? », « jamais négative ? ») : il passe par des situations (supports, lois exponentielles) ; l'invariance de la KL par un changement de variable inversible n'est pas enseignée (elle ramènerait au cas contre N(0, I)). Le sens de la KL dans une approximation (KL directe ou inverse, moyenne contre mode) est en M25b ; M25a calcule seulement les deux sens pour constater l'asymétrie, sans les additionner : la mesure d'une dérive (PSI, KL symétrisée) est en M27. **La reparamétrisation** : M25a ne donne que la loi de μ + Lε (∂ M25a.10, ✏️ M25a.2), avec L le facteur de Cholesky d'une Σ pleine, sans log-variance, sans produit élément par élément σ ⊙ ε et sans aucune dérivée ; la dérivée d'une espérance par rapport à un paramètre de la loi est en M25b, dans un autre cadre. `sample_mvn` tire une seule loi N(μ, Σ), ne rend pas ε et n'a pas de passe arrière (≠ `reparameterize`) ; les fonctions du 🐛 M25a.28 prennent une Σ pleine, jamais `(mu, log_var)` ni `(x, mean, var)` (les contrats de `reparameterize` et de `naive_bayes.log_gaussian_pdf`). **La géométrie** : ∂ M25a.11 démontre la masse d'une ellipse de Mahalanobis en dimension 2 (1 − e^{−c²/2}, en blanchissant puis par les coordonnées polaires de M02b ; le disque en est un cas particulier, que workbookIA 25 affirme sans le démontrer) et la densité de la norme en dimension d (constante admise, sauf en dimension 2 et 3), de mode √(d − 1) ; ✏️ M25a.3 l'applique au vent, aux niveaux 90 % et 95 % (c² = 2 ln 10 et 2 ln 20), avec une Σ non diagonale ; le 🔮 M25a.25 suit la masse d'un ellipsoïde de même niveau quand la dimension passe de 2 à 10. **Les blocs** : l'inverse par blocs, det M = det D · det(A − BD⁻¹C) et la loi conditionnelle par un résidu indépendant de la mesure sont démontrés dans la fiche (§4, dans un bloc `<details>`), sans exercice ∂ ; ✏️ M25a.4, le quiz M25a.Q4 et le 🔨 M25a.22 s'en servent. **Le slerp** est démontré (∂ M25a.15 : base orthonormée du plan par Gram-Schmidt, formule de sin(γ − ψ) tirée de e^{ia} e^{ib} = e^{i(a + b)}, M22 ; MB3 la reprendra) et appliqué à une route orthodromique (✏️ M25a.9 : deux villes, vecteurs unitaires de ℝ³, angle au centre, point au tiers du trajet, profondeur du milieu de la corde R(1 − cos(Ω/2)), avec un angle Ω différent de 90°) ; la limite quand Ω tend vers 0 est un calcul de limite (sin(tΩ)/sin Ω → t), pas une règle de code ; aucune fonction de slerp, ni dans `mymath` ni dans le notebook (c'est 🔨 25.20). **Promesses publiées tenues** : M18 (« le gradient de ln det reviendra avec la densité de la gaussienne multivariée » : ∂ M25a.12), M12c (det Σ dans la densité ; « M25a échantillonnera une loi normale multivariée » par Cholesky), M09b (« M25a la régression bayésienne complète », la moyenne a posteriori comme solution ridge), M14 (le couple gaussien de M14.13). **Partage avec M25b** (voir le rapport de session) : M25a enseigne la densité (`mvn_logpdf`), les transformations affines et le changement de variable multivarié, la loi de μ + Lε, la géométrie, le complément de Schur et le conditionnement (`schur_complement`, `condition_gaussian`), le produit de densités, le modèle linéaire gaussien, la régression bayésienne, le maximum de vraisemblance (non pondéré) de μ et Σ, Jensen continu, la KL continue et la KL entre gaussiennes, l'entropie différentielle, le slerp ; M25b les réutilise sans les redémontrer (l'ACP probabiliste applique le modèle linéaire gaussien et le conditionnement ; le pas M de l'EM pondère le maximum de vraisemblance ; l'ELBO se sert de la KL continue et de l'entropie) et garde les mélanges (dont les moments d'un mélange, le Théorème 6.12 de MML et la loi de la variance totale), l'EM, l'ELBO, l'ACP probabiliste, la dérivée d'une espérance, le sens de la KL, les angles principaux et β. **MML** : §6.5 en entier (le Théorème 6.12, au §6.5.3, et la loi de la variance totale se lisent en M25b, avec les mélanges ; (6.90) et (6.91) se survolent), la fin de §6.7.2 (Théorème 6.16 et Exemple 6.17, le changement de variable multivarié, que M02b.16 n'a pas lu), et §9.3 (§9.3.1 à §9.3.5) : 📖 M25a.17 et M25a.18 ; exercices du livre conseillés : 6.10 (produit de deux densités gaussiennes), 6.12 (un modèle linéaire gaussien), 6.5 (un pas du filtre de Kalman, pour aller plus loin). `correspondances.md` : §6.7 → M02b, M25a. **Conventions** : vecteurs colonnes dans la fiche ; plusieurs vecteurs rangés en lignes, de forme (n, d), dans `mymath` et le notebook, comme NumPy (le 🔗 M25a.16 passe d'une convention à l'autre : X = 1μᵀ + E Lᵀ) ; N(μ, Σ) avec Σ une covariance (jamais un écart-type) ; logarithmes népériens, KL et entropies en nats. `gaussian` : NumPy permis, mais de `np.linalg` seulement `cholesky` et `solve`, ni `multivariate_normal` de NumPy (le test AST refuse ce nom dans tout le module : `default_rng(seed).multivariate_normal(…, method="cholesky")` rend les tirages de `sample_mvn` bit pour bit), et aucune fonction de SciPy (`scipy.stats.multivariate_normal` donnerait `mvn_logpdf` et `sample_mvn`) ; les imports relatifs de ses propres modules sont permis (`eigen.cholesky` de M12c : les tirages sont comparés à 1e-12 près, pas bit pour bit) ; aucune fonction de KL, de slerp, de reparamétrisation (avec des log-variances, ou qui rend ε), de densité diagonale, ni de distance de Fréchet ou de Wasserstein (M27, 🔨 27.22). Écarts au plan : `mvn_pdf` devient `mvn_logpdf` (la densité est son exponentielle, et M25b la prend en log pour l'EM) ; `marginal_gaussian` est abandonnée (une sélection de sous-blocs, faite à la main en ✏️ M25a.4 et dans le 🎨 M25a.27) ; `linreg_posterior` est ajoutée (MML §9.3 ; distincte de `bayes_line_posterior` de workbookIA 9, une grille de droites). Les exemples du stub ne reviennent dans aucun exercice : la covariance [[2, 3], [3, 9]] de moyenne (1, −1), la matrice [[5, 2, 2], [2, 4, 0], [2, 0, 4]] de moyenne (1, 0, 2), Φ = [[1, 0], [1, 1], [1, 2]] avec y = (1, 2, 2) ; ✏️ M25a.4 n'en reprend pas la structure (deux voisins indépendants entre eux, un bloc Σ_bb diagonal). Le 🏆 M25a.30 reconstruit des températures manquantes le long d'une route par la loi conditionnelle d'une gaussienne de covariance exponentielle de la distance (pas une image, pas de « inpainting »). **Évités** (règle de partage, et reprises de ce dépôt) : la KL contre N(0, 1), N(0, I) ou N(0, τ²) et la formule ½(μ² + σ² − 1 − ln σ²) ; s = ln σ² et les dérivées μ et ½(e^s − 1) ; les couples (μ, σ²) = (2, 1), (0, e), (0 ; 0,01), (1, 4), (0,5 ; 2,5), les moyennes (1, 0, −1), s = ln 5, les variances 0,5 et 2 de la variante de 25.7 ; z = μ + σε avec (1,5 ; 0,5 ; −2), (0,2 ; 4 ; 0,5) et (0,2 ; 1 ; −1) ; E‖z‖² en d = 20, 64, 100, 512 et 784, les normes 4,47, 3,16, 8, 5,7, 10, 7,07, 22,63 ; le rapport 1/√2 ≈ 0,71 du milieu de deux tirages ; P(‖z‖ ≤ r) en dimension 2 pour r = 1, 2, 3 (0,393, 0,865, 0,989 ; 39 %, 86 %, 99 %) et le rayon médian 1,18 (r² = 2 ln 2) ; 34 %, 69 %, 90 % ; les 40 000 tirages de la figure de workbookIA 25 ; les slerps (1, 0) → (0, 1), (2, 0, 0) → (0, 2, 0), (3, 0) → (0, 4) (point (2,12 ; 2,83), norme 3,54), z → −z, les normes 23,2, 14,5 et 11,2, le seuil de repli 1e-6 et l'angle de repli 0,05 rad, « sept points » entre deux codes, le milieu (5, 3) de (2, 6) et (8, 0) (25.Q8 e), la dimension 64 et les normes 8 et 5,7 de 27.26 ; les tableaux mu, log_var et dz de 25.28 et 25.29, N(2, 9) et 200 000 tirages, (1,993 ; 8,978) ; les lois P = (0,5 ; 0,5) et Q = (0,25 ; 0,75) de 25.R3 ; « 68 % entre −1 et 1 » comme exemple ; la KL de deux gaussiennes de même variance ‖Δμ‖²/(2σ²) de workbookIA B5 et le bruitage √ᾱ x₀ + √(1 − ᾱ) ε ; la distance de Fréchet entre deux gaussiennes (27.22, M27) ; la grille 3 × 3 de droites et les points (1, 1) et (−1, 0) de 9.7, la figure 9.20 de 9.27 ; de MML, l'Exemple 6.6 (N([0, 2], [[0,3 ; −1], [−1 ; 5]]), x₂ = −1, N(0,6 ; 0,1), marginale N(0 ; 0,3)), l'Exemple 6.17 (refait avec d'autres nombres dans le 📖 seulement), les Exemples 9.7 et 9.8 (polynômes de degré 3, 5 et 7, prior N(0, ¼ I)), les exercices 6.2 et 6.4 du livre ; de ce dépôt, la matrice [[3, 1], [1, 2]] de 🔁 M09b.R1, les covariances [[4, 6], [6, 13]], [[9, 6], [6, 8]] et [[4, 2], [2, 5]] de M12c, (0,6 ; 0,5 ; 1,4) de M14.13, et la concentration en dimension 1 000 de M07 (écart-type 0,71, 29,8 à 33,5) ; MNIST, Fashion-MNIST, le VAE, le tigre, les manchots (workbookIA 2). **Durée** : 17,2 h au lieu des 14 h prévues (18,3 h avant les coupes du coordinateur : la démonstration par blocs, un 💼, des minutes de lecture) : la KL continue, Jensen continu, l'additivité et la KL entre gaussiennes (que workbookIA 25 suppose et que la planification ne comptait pas), la masse d'une ellipse et la loi de la norme, le slerp démontré, le maximum de vraisemblance (promesse de M18), et trois blocs de MML (§6.5, la fin de §6.7.2, §9.3). Deux sessions de génération : §1 à §4, puis §5 à §8.

<a id="m25b"></a>
## M25b · Variables latentes et ELBO

**Partie** VI · **prépare** workbookIA 25 · **dossier** `chapitres/m25b_variables_latentes/` · **MML** §8.4, §8.5, §10.7, ch. 11 · **sessions de génération** 2

Les variables latentes : un modèle génératif écrit comme un graphe orienté (loi jointe, tirage ancestral), la vraisemblance marginale et le posterior d'un latent, les moments d'un mélange ; les mélanges de gaussiennes (responsabilités en log, singularités) et l'algorithme EM ; la borne inférieure de l'évidence (ELBO), démontrée en général, dont l'EM est une montée par coordonnées ; l'ACP probabiliste (posterior exact, rotation, angles principaux, directions éteintes) ; l'inférence approchée (sens de la KL, inférence amortie, dériver une espérance par rapport à un paramètre de la loi) ; et β, le multiplicateur d'une contrainte d'information, avec le posterior agrégé et l'effondrement du code. workbookIA 25 s'en sert pour l'espace latent, l'ELBO et la loss du VAE, la reparamétrisation, le β-VAE et le lien entre autoencodeur linéaire et ACP.

**Temps** : 21,1 h en parcours complet, 16,5 h en parcours essentiel (lecture 165 min, 22 flashcards).

**Objectifs**

- Écrire la loi jointe d'un modèle à variables latentes selon son graphe orienté, en tirer un échantillon ancestral, et calculer la vraisemblance marginale et le posterior d'un latent.
- Définir l'espérance et la variance conditionnelles sachant une variable discrète, et calculer la moyenne et la covariance d'un mélange par les lois de l'espérance et de la variance totales.
- Calculer les responsabilités et la log-vraisemblance d'un mélange de gaussiennes en log, et expliquer pourquoi cette vraisemblance n'est pas bornée.
- Dériver les pas E et M de l'algorithme EM pour un mélange de gaussiennes, et démontrer qu'il ne fait jamais baisser la vraisemblance.
- Démontrer ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour toute loi q, en déduire la borne et le cas d'égalité, et lire l'EM comme une montée par coordonnées de l'ELBO.
- Écrire la loi marginale et le posterior de l'ACP probabiliste, en estimer les paramètres à partir des valeurs propres, et comparer deux sous-espaces par leurs angles principaux.
- Dériver une espérance par rapport à un paramètre de la loi par le chemin X = μ + σε, et choisir le sens de la KL dans une approximation.
- Interpréter β comme un multiplicateur de Lagrange, décomposer la KL moyenne au prior en information mutuelle et écart du posterior agrégé, et reconnaître un code effondré.

**Sections de la fiche**

- §1 Variables latentes et graphes orientés : processus génératif, loi jointe, tirage ancestral et indépendance conditionnelle
- §2 Marginaliser et inverser : vraisemblance marginale, posterior d'un latent, et les moments d'un mélange (espérance et variance conditionnelles, puis totales)
- §3 Mélanges de gaussiennes : responsabilités en log, log-vraisemblance, singularités et composantes à numérotation arbitraire
- §4 L'algorithme EM : le pas E, le pas M pondéré, la monotonie, et k-means comme limite
- §5 La borne inférieure de l'évidence (ELBO) : ln p(x) = ELBO + KL, l'EM comme montée par coordonnées, et le gradient de ln p(x)
- §6 L'ACP probabiliste : posterior exact, maximum de vraisemblance, rotation de W, angles principaux et directions éteintes
- §7 Inférence approchée : le sens de la KL, l'inférence amortie, et dériver une espérance par rapport à un paramètre de la loi
- §8 Pondérer la KL : β comme multiplicateur de Lagrange, information mutuelle, posterior agrégé et effondrement du code

**Notions enseignées** : variable latente, espace latent, processus génératif ; loi jointe p(x, z) = p(z) p(x | z) · modèle graphique orienté : factorisation selon les parents, tirage ancestral ; indépendance conditionnelle, chaîne, fourche et collision (d-séparation en survol, MML §8.5) ; une cause observée en disculpe une autre · vraisemblance marginale p(x) = Σ_z p(z) p(x | z) (ou une intégrale) ; posterior p(z | x) par Bayes ; l'évidence comme constante de normalisation · mélange de lois : densité, tirage ancestral ; espérance et variance conditionnelles sachant une variable discrète, définies ici (E[X | Z = k], la variable aléatoire E[X | Z] ; pour un mélange, E[X | Z = k] = μ_k et V[X | Z = k] = Σ_k) ; lois de l'espérance totale et de la variance totale (MML Théorème 6.12, §6.5.3) ; moyenne et covariance d'un mélange Σ π_k (Σ_k + μ_k μ_kᵀ) − μμᵀ ; part de la variance entre les groupes · mélange de gaussiennes : log-vraisemblance (le logarithme d'une somme), responsabilités calculées en log par log-sum-exp (M04, M05a) · singularités : vraisemblance non bornée quand une composante s'effondre sur un point, régularisation Σ_k + reg·I (le pas M ne maximise plus : l'EM régularisé n'est plus monotone à coup sûr) ; numérotation arbitraire des composantes : K! maxima équivalents · algorithme EM pour un mélange de gaussiennes : pas E (responsabilités), pas M (π_k = N_k/n par un multiplicateur de Lagrange, moyennes et covariances pondérées : le maximum de vraisemblance de M25a, pondéré) ; monotonie, maxima locaux, initialisations ; une proportion de mélange et des composantes inconnues (suite de M13a) · k-means comme limite de l'EM : covariances communes γI, γ → 0, responsabilités dures · borne inférieure de l'évidence (ELBO), démontrée en général pour un latent discret ou continu : ln p(x) = E_q[ln p(x, z) − ln q(z)] + KL(q ‖ p(z | x)) ; ELBO ≤ ln p(x), égalité si et seulement si q est le posterior ; la même borne par Jensen ; la forme E_q[ln p(x | z)] − KL(q ‖ p(z)) (une reconstruction moins une KL au prior) ; l'entropie de q · l'EM comme montée par coordonnées de l'ELBO : le pas E la maximise en q (q = posterior), le pas M en θ (Q(θ | θ_t) de MML §11.4.5) ; d'où la monotonie · gradient de la log-vraisemblance marginale : ∇_θ ln p(x) = E_{p(z | x)}[∇_θ ln p(x, z)] ; il égale le gradient de l'ELBO quand q est le posterior · ACP probabiliste (MML §10.7) : z ~ N(0, I_k), x = Wz + μ + ε, ε ~ N(0, σ²I) ; loi marginale N(μ, WWᵀ + σ²I) ; posterior N(M⁻¹Wᵀ(x − μ), σ²M⁻¹) avec M = WᵀW + σ²I, par le modèle linéaire gaussien de M25a ; l'autre forme, Wᵀ(WWᵀ + σ²I)⁻¹(x − μ) et I − Wᵀ(WWᵀ + σ²I)⁻¹W (MML §10.7.3), égale par Wᵀ(WWᵀ + σ²I)⁻¹ = (WᵀW + σ²I)⁻¹Wᵀ ; sa moyenne est une règle affine de x, sa covariance n'en dépend pas · maximum de vraisemblance de l'ACP probabiliste (Tipping et Bishop, énoncé) : σ² = moyenne des valeurs propres écartées, W = U_k (D_k − σ²I)^{1/2} R, D_k = diag(λ₁, …, λ_k) ; la limite σ² → 0 retrouve l'ACP de M12d ; quand σ² est fixé (connu), une direction de valeur propre λ ≤ σ² est éteinte (colonne de W nulle) · non-identifiabilité par rotation : W et WR (R orthogonale) donnent la même loi ; seul le sous-espace engendré par W est déterminé · angles principaux entre deux sous-espaces : cos φ_i = valeurs singulières de Q_Aᵀ Q_B pour des bases orthonormées Q_A et Q_B (M12b, M12d), min(k_A, k_B) angles ; ils ne dépendent pas des bases ; deux sous-espaces de même dimension sont égaux si et seulement si tous leurs angles sont nuls (en général, tous nuls si et seulement si le plus petit est contenu dans l'autre) · inférence approchée : famille de lois q, KL(q ‖ p) (évite de mettre de la masse là où p est faible, choisit un mode quand les bosses de p sont séparées) contre KL(p ‖ q) (couvre toute la masse ; pour une famille gaussienne, apparie les moments) ; maximiser l'ELBO, c'est minimiser KL(q ‖ p(z | x)) · inférence amortie : une règle x ↦ q(z | x) commune à toutes les observations ; écart d'amortissement : ELBO amortie ≤ meilleure ELBO par observation ≤ ln p(x) · dériver une espérance par rapport à un paramètre de la loi : le chemin X = μ + σε (ou μ + Lε, M25a), que workbookIA 25 appelle l'astuce de reparamétrisation (*reparameterization trick*) ; l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré, la convergence dominée admise), d/dθ E[f(g_θ(ε))] = E[f′(g_θ(ε)) ∂_θ g_θ(ε)] ; estimateur de Monte-Carlo sans biais à un tirage (M19) et sa variance ; une fonction dérivable presque partout, et une indicatrice 1{X > c} pour laquelle l'échange échoue (dérivée nulle presque partout, alors que d/dμ P(X > c) = N(c | μ, σ²), la densité en c) ; la méthode du score seulement nommée (MB8) · pondérer une KL : maximiser une vraisemblance de reconstruction sous un budget d'information, le lagrangien (M13b), β comme multiplicateur et pente de la meilleure valeur en fonction du budget ; avec un bruit gaussien de variance σ², changer σ² revient à changer β · posterior agrégé q(z) = E_x[q(z | x)], un mélange ; il égale le prior quand q(z | x) est le posterior exact et que x suit la loi marginale du modèle, p(x) = Σ_z p(z) p(x | z) · E_x KL(q(z | x) ‖ p(z)) = I(X ; Z) + KL(q(z) ‖ p(z)) ≥ I(X ; Z) (M06) ; une KL moyenne nulle veut dire un code indépendant de l'entrée (effondrement) · information mutuelle de deux variables continues, I(X ; Z) = h(Z) − h(Z | X) = KL(p(x, z) ‖ p(x)p(z)), entropie différentielle conditionnelle (suite de M06 et de M25a) ; celle d'une mesure gaussienne bruitée ½ ln(1 + s²/v), distorsion s² e^{−2I} ; le code s'éteint quand β est assez grand

**Prérequis** : intégration par parties (M02a) · espérance d'une variable continue, théorème de transfert, loi normale, fonction de répartition Φ, loi exponentielle (M02b) · formule de Bayes, probabilités totales, logarithme d'une somme (M04) · log-sum-exp stable (`logsumexp`) (M05a) · entropie, divergence KL discrète, information mutuelle, inégalité de Jensen discrète (M06) · distance euclidienne, k-means (M07) · gradient d'une forme quadratique (x − μ)ᵀA(x − μ) (M09b) · base orthonormée d'un sous-espace, Gram-Schmidt, projection orthogonale (M12b) · théorème spectral, valeurs propres d'une covariance (M12c) · SVD, ACP, approximation de rang faible, pseudo-inverse (M12d) · maximum de vraisemblance, log-vraisemblance, proportion d'un mélange à composantes connues (M13a) · multiplicateurs de Lagrange, KKT (M13b) · graphes orientés sans cycle, numérotation des nœuds où chaque parent précède ses enfants (M16) · gradient par rapport à une matrice : ∇ ln det X et ∇ tr(AX) (M18) · estimateur de Monte-Carlo sans biais d'un gradient, variance d'un estimateur (M19) · densité et log-densité de N(μ, Σ) (`mvn_logpdf`), modèle linéaire gaussien, loi conditionnelle, maximum de vraisemblance de μ et Σ, loi de μ + Lε, Jensen continu, KL continue et KL entre gaussiennes, entropie différentielle (M25a)

**mymath** : `latent.py` (signatures figées) : `gmm_e_step`, `gmm_m_step`, `gmm_log_likelihood`, `gmm_elbo`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 25.5 ∂ Dériver à travers un tirage : l'astuce de reparamétrisation · 25.7 ∂ La divergence KL entre N(μ, σ²) et N(0, 1) · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé) · 25.11 🗣️ Le VAE expliqué à un ami en cinq lignes · 25.13 📄 Lire Kingma et Welling (2013), « Auto-Encoding Variational Bayes » · 25.23 🔬 L'autoencodeur linéaire face à l'ACP de scikit-learn · 25.30 📦 Un VAE en PyTorch : reconstruction + KL · 25.31 🔮 Prédire : décoder des tirages N(0, I) avec un AE puis avec un VAE · 25.32 🔬 Un VAE est stochastique : sorties répétées, bruit relatif, interpolations · 25.33 🎨 Reproduire le nuage latent d'un VAE 2D et la grille −3…3 (fig. 25.67-25.68) · 25.34 📈 Diagnostiquer des courbes reconstruction/KL (effondrement du posterior) · 25.36 🔬 β-VAE : échanger la netteté contre la régularité · 25.38 🔨 Un VAE entièrement en NumPy avec mylearn · 25.Q9 🧠 Autoencodeur linéaire et ACP · 25.Q12 🧠 Les trois exigences d'un VAE et l'astuce de reparamétrisation · 25.R3 🔁 La divergence KL, ce que mesure le terme de régularisation du VAE · 25.E1 💼 Autoencodeur ou ACP : quand préférer l'un ou l'autre ? · 25.E2 💼 Pourquoi un VAE sait-il générer et pas un autoencodeur classique ? · 25.E3 💼 Expliquer l'astuce de reparamétrisation

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M25b.Q1 | 🧠 | Lire un graphe orienté : factoriser la loi jointe, l'ordre d'un tirage ancestral, et les variables qui deviennent dépendantes quand on observe leur effet commun | ★ | 4 | §1 | C, E | manuel | — |
| M25b.Q2 | 🧠 | Marginaliser ou conditionner : vraisemblance marginale, posterior d'un latent, moyenne et variance d'un mélange | ★ | 4 | §2 | C, E | manuel | — |
| M25b.Q3 | 🧠 | Un mélange de gaussiennes : responsabilités, logarithme d'une somme, vraisemblance infinie et composantes renumérotées | ★ | 4 | §3 | C, E | manuel | — |
| M25b.Q4 | 🧠 | L'EM : ce que font le pas E et le pas M, ce qui ne baisse jamais, ce qui n'est pas garanti, et k-means comme limite | ★ | 4 | §4 | C, E | manuel | — |
| M25b.Q5 | 🧠 | L'ELBO : une borne de quoi, une égalité quand, un écart égal à quelle KL ? | ★ | 4 | §5 | C, E | manuel | — |
| M25b.Q6 | 🧠 | L'ACP probabiliste : covariance marginale, rotation de W, angles principaux et directions éteintes | ★ | 5 | §6 | C, E | manuel | — |
| M25b.Q7 | 🧠 | KL directe ou inverse, inférence amortie et écart d'amortissement, et dériver sous l'espérance : quand le peut-on ? | ★ | 5 | §7 | C, E | manuel | — |
| M25b.Q8 | 🧠 | Pondérer la KL : multiplicateur, information mutuelle, posterior agrégé et code effondré | ★ | 4 | §8 | C, E | manuel | — |
| M25b.R1 | 🔁 | Bayes sur une variable cachée et log-sum-exp : probabilités totales, posterior, et une somme d'exponentielles sans dépassement (M04, M05a) | ★ | 6 | §2 §3 | C, E | manuel | — |
| M25b.R2 | 🔁 | L'inégalité de Jensen, la KL continue et l'information mutuelle (M06, M25a) | ★ | 6 | §5 §8 | C, E | manuel | — |
| M25b.R3 | 🔁 | La SVD, l'ACP et la projection orthogonale sur un sous-espace (M12b, M12d) | ★ | 8 | §6 | C, E | manuel | — |
| M25b.1 | ✏️ | Trois machines produisent des pièces de longueurs gaussiennes : le graphe, la loi jointe, un tirage ancestral à la main, la vraisemblance marginale d'une longueur et le posterior de la machine | ★★ | 25 | §1 §2 | C, E | wbm | — |
| M25b.2 | ✏️ | Deux variétés de grains de café (longueur, largeur) : moyenne et covariance du mélange par la variance totale, part de la variance entre variétés, et une corrélation qu'aucune variété n'a | ★★ | 25 | §2 | C, E | wbm | — |
| M25b.3 | ✏️ | Deux séries de résistances mélangées : les responsabilités de quatre mesures en log, un pas M (proportion, moyennes, variances), et la log-vraisemblance qui monte (suite de M13a, composantes inconnues) | ★★ | 55 | §3 §4 | C, E | wbm | — |
| M25b.4 | ∂ | Le pas M d'un mélange de gaussiennes : les poids N_k/n par un multiplicateur de Lagrange, les moyennes et les covariances comme maximum de vraisemblance pondéré | ★★ | 40 | §4 | C, E | manuel | — |
| M25b.5 | ∂ | L'ELBO en général : ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour un latent discret ou continu, la borne retrouvée par Jensen, et la forme E_q[ln p(x | z)] − KL(q ‖ p(z)) | ★★★ | 35 | §5 | C, E | manuel | — |
| M25b.6 | ✏️ | Une sonde de qualité de l'eau, un état caché à deux valeurs et une mesure gaussienne : ln p(x), l'ELBO pour trois lois q, et l'écart égal à la KL au posterior | ★★ | 25 | §5 | C, E | wbm | — |
| M25b.7 | ∂ | L'EM comme montée par coordonnées de l'ELBO : le pas E maximise en q, le pas M en θ, d'où la monotonie ; et ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] pour la moyenne d'une composante | ★★★ | 40 | §4 §5 | C, E | manuel | — |
| M25b.8 | ∂ | L'ACP probabiliste : la loi marginale N(μ, WWᵀ + σ²I), le posterior de z par le modèle linéaire gaussien, et W ou WR donnent la même loi | ★★ | 35 | §6 | C, E | manuel | — |
| M25b.9 | ✏️ | Trois épreuves d'un concours expliquées par une aptitude cachée : covariance marginale, posterior d'un candidat (une règle affine des notes), et maximum de vraisemblance à partir de valeurs propres données, dont une direction éteinte | ★★ | 35 | §6 §7 | C, E | wbm | — |
| M25b.10 | ✏️ | Les angles principaux entre deux plans de ℝ⁴ et entre deux droites de ℝ³ : bases orthonormées, SVD de Q_Aᵀ Q_B, et pourquoi le résultat ne dépend pas des bases choisies | ★★ | 40 | §6 | C, E | wbm | — |
| M25b.11 | ∂ | Dériver une espérance par rapport à un paramètre de la loi : l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré), la variance de l'estimateur à un tirage de ∂_σ E[e^X], et une indicatrice 1{X > c} pour laquelle l'échange échoue | ★★★ | 40 | §7 | C, E | manuel | — |
| M25b.12 | ✏️ | Le coût d'un stock c face à une demande gaussienne : E[(D − c)⁺], ses dérivées en μ et en σ par le chemin, puis par la formule fermée | ★★★ | 45 | §7 | C | wbm | — |
| M25b.13 | ✏️ | Une seule gaussienne pour la loi bimodale des temps de trajet par deux itinéraires : KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un itinéraire | ★★ | 35 | §7 | C, E | wbm | — |
| M25b.14 | ✏️ | Un code stochastique d'une source à trois symboles : posterior agrégé, information mutuelle, KL moyenne au prior décomposée en I(X ; Z) + KL(q(z) ‖ p(z)), puis le code qui s'effondre | ★★ | 30 | §8 | C, E | wbm | — |
| M25b.15 | ∂ | β comme multiplicateur de Lagrange : une mesure gaussienne codée avec du bruit, distorsion s² e^{−2I}, le lagrangien D + βI, et le code qui s'éteint quand β dépasse 2s² | ★★★ | 35 | §8 | C, E | manuel | — |
| M25b.16 | 📖 | MML §8.4 et §8.5 : modèles probabilistes, inférence bayésienne, modèles à variables latentes, graphes orientés et d-séparation (survol), en anglais | ★★ | 40 | §1 §2 | C | manuel | — |
| M25b.17 | 📖 | MML ch. 11 : mélange de gaussiennes, responsabilités, mises à jour, EM et point de vue latent, en anglais ; refaire l'Exemple 11.1 avec ses propres données | ★★ | 50 | §3 §4 §5 | C | manuel | — |
| M25b.18 | 📖 | MML §10.7 : l'ACP probabiliste, processus génératif, vraisemblance, loi jointe et posterior, en anglais | ★★ | 30 | §6 | C | manuel | — |
| M25b.19 | 🗣️ | Expliquer l'EM avec un bac de pièces venues de deux machines inconnues : deviner, réestimer, recommencer, sans jamais reculer | ★ | 10 | §4 | C, E | manuel | — |
| M25b.E1 | 💼 | « Pourquoi l'algorithme EM ne fait-il jamais baisser la vraisemblance, et vers quoi converge-t-il ? » | ★ | 10 | §4 §5 | C, E | manuel | — |
| M25b.20 | 🔨 | Les responsabilités d'un mélange de gaussiennes, calculées en log (le pas E) · `gmm_e_step` | ★★ | 35 | §3 | C, E | pytest | — |
| M25b.21 | 🔨 | Le pas M d'un mélange de gaussiennes : poids, moyennes et covariances pondérées, avec une régularisation · `gmm_m_step` | ★★ | 30 | §4 | C, E | pytest | — |
| M25b.22 | 🔨 | La log-vraisemblance d'un mélange de gaussiennes, et son ELBO pour des responsabilités quelconques · `gmm_log_likelihood, gmm_elbo` | ★★ | 30 | §3 §5 | C, E | pytest | — |
| M25b.23 | 🔗 | Pont : l'ELBO de n mesures rangées en lignes, écrite « reconstruction moins KL au prior » E_q[ln p(x | z)] − KL(q ‖ π), en nats par mesure, et ce que gagne chaque terme quand q devient le posterior | ★ | 30 | §5 | C, E | wbm | M25b.22 |
| M25b.24 | 📦 | `scipy.linalg.subspace_angles` et `np.linalg.eigh` : les angles principaux de M25b.10, et l'ACP probabiliste de mesures par leurs valeurs propres, contre la vraisemblance de `mvn_logpdf` | ★ | 30 | §6 | C, E | wbm | M25b.10 |
| M25b.25 | 🔮 | Prédire ce que devient la log-vraisemblance quand une composante centrée sur un point se resserre (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis avec une régularisation, et mesurer | ★ | 15 | §3 §4 | C | wbm | M25b.20, M25b.21, M25b.22 |
| M25b.26 | 🔬 | L'EM sur des longueurs de poissons de trois cohortes : la log-vraisemblance et l'ELBO après chaque demi-pas, sans régularisation, plusieurs initialisations et des maxima locaux | ★★ | 30 | §4 §5 | C, E | wbm | M25b.20, M25b.21, M25b.22 |
| M25b.27 | 🎨 | Une gaussienne ajustée à un mélange bimodal par KL(p ‖ q) puis par KL(q ‖ p) : les deux courbes, et les deux minima de la KL inverse | ★ | 30 | §7 | C | manuel | M25b.13 |
| M25b.28 | 🐛 | Chasse à l'erreur : des responsabilités sans log qui donnent 0/0, un pas M qui divise par n au lieu de N_k, et une ELBO sans l'entropie de q | ★ | 25 | §3 §4 §5 | C, E | wbm | — |
| M25b.29 | 🛠️ | Un test de propriété : sur des mélanges tirés au hasard, ELBO ≤ log-vraisemblance, égalité après le pas E, et un EM sans régularisation (reg = 0) qui ne descend jamais (à une tolérance près) | ★ | 30 | §4 §5 | C | manuel | M25b.20, M25b.21, M25b.22 |
| M25b.30 | 🏆 | Défi : retrouver trois populations de mesures en dimension 2 par l'EM, sous un seuil de log-vraisemblance moyenne sur des mesures de test | ★★★ | 35 | §4 | C | wbm | M25b.20, M25b.21, M25b.22 |

*Notes* : Frontières : le ∂ 25.5 (les dérivées de z = μ + σε par rapport à μ et à s = ln σ², ε fixé, E[z²] dérivée avant ou après l'espérance, l'estimateur à un tirage du VAE), le ∂ 25.7 (KL(N(μ, σ²) ‖ N(0, 1)), en s = ln σ², ses dérivées), le ∂ 25.8 (autoencodeur linéaire et ACP, déjà frontière de M12d), le 🗣️ 25.11 (ce qu'est un VAE), le 📄 25.13 (l'ELBO, AEVB et l'annexe B de Kingma et Welling), le 🔬 25.23 (autoencodeur linéaire contre ACP, angles entre sous-espaces, `subspace_angles_deg_23`), le 📦 25.30 (la loss « reconstruction + β KL » sommée, le β caché de 784), le 🔮 25.31 (décoder des tirages du prior), le 🔬 25.32 (sorties répétées, moyenne des sorties contre sortie de la moyenne), le 📈 25.34 et le 🔬 25.36 (effondrement du posterior, latents actifs, β montant, balayage de β), le 🎨 25.33 (le nuage des μ d'un VAE contre le prior, que le posterior agrégé du §8 explique), le 🔨 25.38 (gradient du VAE par deux chemins), les quiz 25.Q9 et 25.Q12, le rappel 25.R3 (la KL dans les deux sens : M25b enseigne le sens de la KL), les 💼 25.E1, 25.E2 et 25.E3. M25b travaille hors réseau : des machines et leurs pièces, des grains de café, des séries de résistances, des longueurs de poissons, une sonde de qualité de l'eau, les épreuves d'un concours, des plans de ℝ⁴, un stock face à une demande, des temps de trajet, une source à trois symboles, une mesure bruitée ; jamais un encodeur, un décodeur, un réseau, une image, ni un VAE (seulement nommé dans la fiche, comme ce que workbookIA 25 construira). **L'ELBO** est démontrée en général (∂ M25b.5 : pour un latent discret ou continu, par la décomposition en KL au posterior, puis par Jensen) et calculée là où tout se calcule : un latent à deux états et une mesure gaussienne (✏️ M25b.6), un mélange de gaussiennes (🔨 M25b.22, `gmm_elbo`), l'ACP probabiliste (posterior exact). Garde-fous : jamais l'ELBO d'un encodeur gaussien diagonal avec un prior N(0, I) et un décodeur de Bernoulli ou gaussien ; dans l'ACP probabiliste, l'écart à la vraisemblance s'écrit KL(q ‖ p(z | x)) entre deux gaussiennes dont aucune n'est le prior, et on ne calcule jamais KL(q(z | x) ‖ N(0, I)) ni une KL contre N(0, 1) ou N(0, τ²) (∂ 25.7, 🔨 25.29) ; la forme « reconstruction moins KL au prior » ne se calcule que pour un latent discret (KL(q ‖ π), 🔗 M25b.23) ; l'ELBO d'une chaîne de latents (diffusion) est à MB5. **L'EM** est une montée par coordonnées de l'ELBO (∂ M25b.7 ; MML §11.4.5 écrit Q(θ | θ_t)) ; ✏️ M25b.3 tient la promesse de M13a (estimer la proportion quand les composantes sont aussi inconnues), sans reprendre ses densités ni ses données ; k-means comme limite est dans la fiche (§4) et le quiz M25b.Q4 ; les singularités dans la fiche (§3), le quiz M25b.Q3 et le 🔮 M25b.25. Les courbes monotones (🔬 M25b.26, 🛠️ M25b.29) se tracent sans régularisation (reg = 0) : la régularisation ne sert qu'au 🔮 M25b.25 et au 🏆 M25b.30, et la fiche (§4) dit pourquoi (avec reg > 0, le pas M ne maximise plus, et l'EM peut faire baisser la log-vraisemblance et l'ELBO). Dans le 🔮 M25b.25, sans régularisation, la log-vraisemblance ne devient pas +∞ : `gmm_m_step` rend une covariance nulle (ou presque, à l'arrondi près), que `gmm_e_step` refuse quand Cholesky échoue ; l'expérience resserre donc à la main l'écart-type d'une composante centrée sur un point (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis applique reg. Le gradient de ln p(x) par l'identité ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] (∂ M25b.7) s'applique à la moyenne d'une composante d'un mélange, jamais à un réseau. **La dérivée d'une espérance** (la moitié « gradient » de la reparamétrisation ; la moitié « loi » est en M25a) se fait sur des coûts : ∂ M25b.11 démontre l'échange sous une hypothèse de domination, calcule la variance de l'estimateur à un tirage de ∂_σ E[e^X] et montre une indicatrice 1{X > c} pour laquelle l'échange échoue ; ✏️ M25b.12 dérive E[(D − c)⁺] pour un stock c (dérivées P(D > c) et σ N(c | μ, σ²), par le chemin puis par la formule fermée), avec θ = μ ou σ directement ; aucune comparaison « dériver avant ou après l'espérance » sur une fonction lisse (∂ 25.5.5) : la vérification par la formule fermée se fait sur le stock, une fonction seulement continue ; jamais z², ½(z − y)², s = ln σ², une log-variance, σ ⊙ ε, ni « un tirage par exemple dans un mini-batch » ; la méthode du score (∇ ln p) est seulement nommée (MB8). M25b.Q7 n'a aucun item « peut-on dériver à travers un tirage » (25.Q12 c, ∂ 25.5.4) : seulement les conditions de l'échange. **Le sens de la KL** : ✏️ M25b.13 et 🎨 M25b.27 approchent un mélange bimodal de temps de trajet par une seule gaussienne (KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un mode). **L'ACP probabiliste** applique le modèle linéaire gaussien et le conditionnement de M25a sans les redémontrer (∂ M25b.8) ; le maximum de vraisemblance de Tipping et Bishop est énoncé et appliqué à des valeurs propres données (✏️ M25b.9 : un facteur latent, trois épreuves, une direction éteinte quand le bruit est connu) ; l'inférence amortie s'y lit (la moyenne a posteriori est une règle affine des notes, valable pour tous les candidats) ; aucun autoencodeur linéaire, aucun « tr C − wᵀCw », ni cercle unité. **Les angles principaux** : ✏️ M25b.10 (deux plans de ℝ⁴, deux droites de ℝ³ d'un angle autre que 30°, par la SVD de Q_Aᵀ Q_B) et 📦 M25b.24 (`scipy.linalg.subspace_angles`) ; aucune fonction d'angles principaux dans `mymath` ni dans `latent.py` (le notebook les calcule en NumPy) ; l'indépendance vis-à-vis des bases se démontre (Q_A ↦ Q_A R_A), sans le contrôle « le même plan dans une autre base donne des angles nuls » ni une fonction qui convertit `subspace_angles` en degrés (`subspace_angles_deg_23` et ses deux contrôles, 25.23), et aucun angle n'est pris entre un W estimé et le sous-espace de l'ACP (la question du 🔬 25.23) ; M25b.Q6 ne reprend pas la QCM de 25.Q9 a (« les axes, le sous-espace, un sous-espace quelconque… »). **β** : ∂ M25b.15 le traite comme le multiplicateur d'un budget d'information sur une mesure gaussienne bruitée (I = ½ ln(1 + s²/v), D = s² e^{−2I}, le code s'éteint quand β ≥ 2s²), avec une variance de la source s² ≠ 1, l'information calculée par les entropies différentielles h(Z) − h(Z | X) de M25a et jamais par une KL contre une gaussienne centrée N(0, τ²) ; ✏️ M25b.14 décompose la KL moyenne au prior (posterior agrégé, information mutuelle, effondrement) sur des tableaux discrets, et prend la source égale à la loi marginale du modèle quand le posterior agrégé doit égaler le prior ; jamais de courbes d'entraînement, de seuil de latents actifs, de β = 1, 4, 16, 20 ou 100, ni de « KL annealing ». **Partage avec M25a** (voir les rapports) : M25a enseigne la densité (`mvn_logpdf`), les transformations affines et la loi de μ + Lε, le complément de Schur et le conditionnement, le modèle linéaire gaussien, le maximum de vraisemblance non pondéré, Jensen continu, la KL continue et la KL entre gaussiennes, l'entropie différentielle ; M25b les réutilise sans les redémontrer et garde les mélanges (moments, variance totale, MML Théorème 6.12), l'EM, l'ELBO, l'ACP probabiliste, la dérivée d'une espérance, le sens de la KL, les angles principaux, β, l'inférence amortie et le posterior agrégé. **Partage avec M26** : M25b définit l'espérance et la variance conditionnelles sachant une variable discrète et les lois de l'espérance et de la variance totales (les mélanges en ont besoin) ; M26, qui vient après, les rappelle et y ajoute la propriété de la tour et l'analyse au premier pas. **MML** : §8.4 (8.4.1 à 8.4.3) et §8.5 (8.5.1 ; la d-séparation de 8.5.2 en survol) avant §1 et §2 : 📖 M25b.16 ; §6.5.3 (le Théorème 6.12, les moments d'un mélange de deux gaussiennes) avant §2 ; ch. 11 (11.1 à 11.4) avant §3 à §5 : 📖 M25b.17 ; §10.7 (10.7.1 à 10.7.3) avant §6 : 📖 M25b.18. MML n'a pas l'ELBO (§11.4.5 s'arrête à Q(θ | θ_t)) : lecture libre conseillée, MacKay ch. 22 (EM, k-means doux) et ch. 33 (méthodes variationnelles). Exercices du livre conseillés : 6.11 (*Iterated Expectations*, l'espérance totale) et 6.2 (les moments d'un mélange de deux gaussiennes ; conseillé, jamais repris : ✏️ M25b.2 prend d'autres lois et d'autres nombres) ; les ch. 8, 10 et 11 n'en ont pas. **Conventions** : données rangées en lignes, de forme (n, d), dans `mymath` et le notebook (une mesure en dimension 1 est un tableau (n, 1)) ; poids (K,), moyennes (K, d), covariances (K, d, d) ; responsabilités (n, K) ; logarithmes népériens, ELBO, KL et informations en nats ; la fiche écrit les vecteurs en colonnes. `latent` : NumPy permis, de `np.linalg` seulement `cholesky` et `solve` (pour rien de plus que `gaussian`), ni `np.cov` ni `np.average` (avec `aweights` et `weights`, ils font le pas M, et ce sont les oracles des tests), aucune SciPy ; il importe `mvn_logpdf` de `gaussian` (M25a) et peut importer `logsumexp` d'`approx` (M05a), par des imports relatifs (tout import relatif de ses propres modules est permis) ; aucune fonction de KL, de reparamétrisation, d'angles principaux ni d'ACP probabiliste. Le notebook se sert aussi de `gaussian` : `sample_mvn` pour le tirage ancestral des données (🔬 M25b.26, 🏆 M25b.30), `mvn_logpdf` et `condition_gaussian` (le posterior de l'ACP probabiliste comme loi conditionnelle de la loi jointe de (z, x)) dans le 📦 M25b.24. Écarts au plan : `gmm_elbo` ajoutée (décision du coordinateur) ; MML §6.7 passe à M25a ; deux sessions de génération (§1 à §4, puis §5 à §8). Les exemples du stub ne reviennent dans aucun exercice : les mesures (0,5 ; 2 ; 3,5 ; 6) avec les poids (0,4 ; 0,6), les moyennes 1 et 5 et les variances 1 et 2, le point 1000 ; les points (0, 0), (1, 0), (0, 2), (4, 4), (5, 3) ; reg = 0,1 ; ✏️ M25b.3 (quatre mesures, comme l'exemple de `gmm_e_step`) prend d'autres poids que (0,4 ; 0,6), d'autres moyennes et d'autres variances. **Évités** (règle de partage, et reprises de ce dépôt) : l'ELBO d'un encodeur gaussien diagonal, d'un prior N(0, I) et d'un décodeur de Bernoulli ; la loss « reconstruction sommée + β KL » sur des images ; le facteur 784, « β caché de 784 », « 784 fois plus petite » ; β ∈ {0,5 ; 1 ; 4 ; 16} et {1, 20, 100, montant} ; 2, 3, 8, 10, 16, 20, 32, 50 et 64 latents ; le seuil de latents actifs 0,05 nat ; `HISTORY_34` ; les KL 17,6 → 2,2, 68,01 → 22,38, 45,6, 113,8 ; les reconstructions 171, 104 et 152 nats ; les covariances C = [[5, 2], [2, 2]] (valeurs propres 6 et 1, w = (2, 1)/√5) et [[3, 1], [1, 3]] (4 et 2) ; le cercle unité (C = ½ I, l'angle comme code) ; u = (0,6 ; 0,8) et x = (5, 0) ; les plans z = 0 et incliné de 30°, la base [[2, 1], [1, 3]], k = 16, les angles 1,6° et 6,4°, les cosinus 0,02 et 0,10, les erreurs 0,02727 et 0,02725, « k = 4, 2 epochs, 2 000 images » (25.23) ; 34 %, 69 %, 90 % contre 39 %, 86 %, 99 %, un nuage de moyennes comparé aux disques du prior (25.33) ; un tirage par exemple et le mini-batch de 100 de Kingma et Welling ; « moyenne des sorties contre sortie de la moyenne » d'un décodeur ; le PSNR moyen image par image ; la KL contre N(0, 1), N(0, I) ou N(0, τ²) et ½(μ² + σ² − 1 − ln σ²) ; s = ln σ² ; μ = 0,5, ln σ² = ln 0,25 et ε = −2 (workbookIA B5.R3) ; z = μ + σε avec (1,5 ; 0,5 ; −2) ; « 68 % entre −1 et 1 » ; la grille −3 à 3 et ses 80 tirages ; les 10 000 images, 60 000 exemples, 28 × 28, 512 × 512 × 3 et 64 × 64 × 4 ; le 99ᵉ centile ; de MML, (11.5) (0,5 N(−2, ½) + 0,2 N(1, 2) + 0,3 N(4, 1)), l'Exemple 11.1 (données {−3 ; −2,5 ; −1 ; 0 ; 2 ; 4 ; 5}, initialisation N(−4, 1), N(0 ; 0,2), N(8, 3), π = ⅓ ; refait avec d'autres données dans le 📖 seulement), les responsabilités (11.19), le mélange de l'exercice 6.2 (0,4 N((10, 2), I) + 0,6 N(0, [[8,4 ; 2] ; [2 ; 1,7]])), les figures de §10.7 ; de ce dépôt, l'exemple de mélange de M13a (f₀, f₁ et ses données), la matrice [[3, 1], [1, 2]] de 🔁 M09b.R1, les exemples des stubs `gaussian` (Σ = [[2, 3], [3, 9]], [[5, 2, 2], [2, 4, 0], [2, 0, 4]], Φ = [[1, 0], [1, 1], [1, 2]]) et `approx` ; MNIST, Fashion-MNIST, Frey Face, CIFAR-10 contre SVHN, l'anomalie MNIST contre Fashion-MNIST, le tigre. **Durée** : 21,1 h au lieu des 14 h prévues (essentiel 16,5 h ; lecture de la fiche 165 min au lieu de 150 après la session 63, durées des exercices recalées après les vérifications de la session 64) : l'ELBO démontrée en général, la dérivée d'une espérance, les angles principaux, β, le posterior agrégé et l'inférence amortie, que la planification ne comptait pas, et quatre blocs de MML (≈ 35 pages, trois 📖 au lieu de 1–2). COMPOSITION : trois 📖 (quatre blocs de MML de sujets distincts).

<a id="m26"></a>
## M26 · Chaînes de Markov et équation de Bellman

**Partie** VI · **prépare** workbookIA 26 · **dossier** `chapitres/m26_markov_bellman/` · **MML** — · **sessions de génération** 1

Les chaînes de Markov finies et ce qu'on calcule sur elles : la matrice de transition, la loi après n pas (en convention ligne) et la loi stationnaire (existence, unicité, convergence, vitesse, et le PageRank) ; l'espérance conditionnelle et l'analyse au premier pas (la probabilité d'être absorbé, la durée moyenne avant la fin) ; le retour actualisé comme variable aléatoire, le facteur γ vu comme une probabilité de continuer, les décisions et les politiques ; l'équation de Bellman d'une politique fixée, un système linéaire (I − γP)V = r, résolu exactement ou par l'itération d'une contraction ; un opérateur avec un maximum, sur un problème d'arrêt optimal ; enfin ce que deviennent ces équations quand on n'a que des échantillons : la moyenne de retours simulés, l'erreur TD et le biais du maximum. workbookIA 26 applique ces outils à l'apprentissage par renforcement.

**Temps** : 17,9 h en parcours complet, 13,1 h en parcours essentiel (lecture 170 min, 22 flashcards).

**Objectifs**

- Écrire la matrice de transition d'une chaîne de Markov, en convention ligne, et calculer la loi après n pas.
- Calculer une loi stationnaire, dire si elle est unique et si la loi de la chaîne y converge, et à quelle vitesse.
- Calculer une probabilité d'absorption et une durée moyenne par l'analyse au premier pas (espérance conditionnelle).
- Définir le retour actualisé et la valeur d'un état sous une politique fixée, et interpréter γ comme une probabilité de continuer.
- Écrire et résoudre le système de Bellman d'une politique fixée, et justifier qu'il a une unique solution.
- Itérer l'opérateur de Bellman, borner l'erreur et choisir le nombre d'itérations.
- Résoudre un problème d'arrêt optimal par un opérateur avec un maximum, et lire l'équation d'optimalité de Bellman.
- Relier la moyenne de retours simulés, l'erreur TD et le biais du maximum aux équations exactes.

**Sections de la fiche**

- §1 Chaînes de Markov : matrice de transition, graphe et loi à n pas
- §2 La loi stationnaire : existence, unicité, convergence et vitesse ; le PageRank
- §3 Espérance conditionnelle et analyse au premier pas : absorption et durée moyenne
- §4 Récompenses, retour actualisé et valeur d'un état ; décisions et politiques
- §5 L'équation de Bellman d'une politique fixée : un système linéaire
- §6 Itérer l'opérateur de Bellman : contraction, bornes d'erreur, itérations synchrones et en place
- §7 Un maximum dans l'opérateur : arrêt optimal et équation d'optimalité
- §8 Des échantillons au lieu de P : moyenne de retours, erreur TD et biais du maximum

**Notions enseignées** : chaîne de Markov finie : propriété de Markov, matrice de transition stochastique (lignes de somme 1), graphe de transition · convention ligne pour les lois : μ_{n+1} = μ_n P, loi à n pas μ₀Pⁿ, Chapman-Kolmogorov P^{m+n} = P^m P^n, (Pⁿ)_ij comme somme sur les chemins ; convention colonne pour les fonctions : E[f(S_{n+1}) | S_n = i] = (Pf)_i · ‖P‖∞ = 1 et ρ(P) = 1 ; loi stationnaire π = πP, Σπ = 1 : existence (Perron-Frobenius admis), calcul par un système linéaire ou par la méthode de la puissance · chaîne irréductible, apériodique : unicité de π et convergence de μ₀Pⁿ (énoncées) ; contre-exemples (chaîne périodique, chaîne à deux classes) ; vitesse de convergence fixée par |λ₂| · PageRank : le surfeur aléatoire et le facteur d'amortissement · espérance conditionnelle E[X | Y = y] et formule de l'espérance totale (rappel de M25b), propriété de la tour, appliquées à l'analyse au premier pas · états absorbants et transitoires ; analyse au premier pas : probabilités d'absorption h = Qh + b, durées moyennes t = 1 + Qt ; matrice fondamentale (I − Q)⁻¹ = Σ Qᵗ · retour actualisé G = Σ γᵗ r(S_t) comme variable aléatoire ; valeur V(s) = E[G | S₀ = s] ; γ comme probabilité de continuer : durée géométrique d'espérance 1/(1 − γ) · processus de décision markovien : états, actions, matrices P_a, récompenses r(s, a, s′) et leur moyenne r(s, a) ; politique déterministe ou stochastique ; chaîne induite P_π, r_π ; valeur d'une action Q^π(s, a) · équation de Bellman d'une politique fixée V = r + γPV : système linéaire (I − γP)V = r, inversible pour γ < 1 (‖γP‖∞ = γ), série de Neumann V = Σ γᵗPᵗr, loi d'occupation actualisée (1 − γ)(I − γP)⁻¹ ; une fin possible : matrice sous-stochastique, γ = 1 permis quand la fin est sûre · opérateur de Bellman, γ-contraction pour ‖·‖∞ ; convergence géométrique en γᵏ ; borne a posteriori γ/(1 − γ)‖V_k − V_{k−1}‖∞ et critère d'arrêt ; itérations synchrones (Richardson de pas 1) et en place (Gauss-Seidel) ; théorème du point fixe de Banach (énoncé) · un opérateur avec un maximum : |max x − max y| ≤ max |x − y| ; supremum d'une fonction bornée (plus petit majorant, symétrique de l'infimum de M13b) et |sup f − sup g| ≤ sup |f − g| ; arrêt optimal V = max(g, c + γPV), valeur de continuation et règle à seuil ; équation d'optimalité de Bellman, itération sur les valeurs et politique gloutonne (énoncées) · estimer une valeur par la moyenne de retours simulés, tronqués ; pas 1/n et pas constant ; conditions de Robbins-Monro Σαₜ = ∞, Σαₜ² < ∞ (énoncées) · erreur TD δ = r + γV(s′) − V(s) : son espérance conditionnelle est le résidu de Bellman ; Σ γᵏ δ_{t+k} = G_t − V(S_t) (télescopage) ; récompense ajoutée γΦ(s′) − Φ(s) · biais du maximum : E[max X̂ᵢ] ≥ max E[X̂ᵢ], E[max(Z₁, Z₂)] = 1/√π ; estimateur double (choisir sur un échantillon, mesurer sur l'autre)

**Prérequis** : suites géométriques et leur somme, actualisation, moyennes mobile et exponentielle (R5) · logarithmes : résoudre γᵏ ≤ ε (R6) · loi géométrique et son espérance, loi normale, linéarité de l'espérance (M02b) · loi des grands nombres, erreur type d'une moyenne (M02c) · probabilité conditionnelle, probabilités totales (M03) · inégalité de Jensen (M06) · systèmes linéaires, inverse d'une matrice (M09a) · ε-greedy (une politique stochastique) ; la moyenne incrémentale est celle de workbookIA 11, démontrée par son ∂ 11.2 (M11) · valeurs propres, diagonalisation et puissances, méthode de la puissance (M12c) · puissances d'une matrice d'adjacence : sommes sur les chemins d'un graphe (M16) · itérations linéaires, point fixe, itération de Richardson (M19) · tableaux à plusieurs axes, einsum (M20) · normes induites ‖·‖₁ et ‖·‖∞, ρ(A) ≤ ‖A‖, Aᵗ → 0 si ρ(A) < 1, applications contractantes et oubli du point de départ (M22) · espérance conditionnelle sachant une variable discrète, espérance et variance totales (M25b)

**mymath** : `markov.py` (signatures figées) : `n_step_distribution`, `stationary_distribution`, `bellman_linear_solve`, `bellman_fixed_point_iterates`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 26.7 ∂ Somme géométrique et horizon effectif de γ · 26.8 ∂ Équation de Bellman : le point fixe que vise le Q-learning · 26.1 ✏️ Retours total et actualisé d'une partie de six coups · 26.3 ✏️ Une mise à jour de Q-learning à la main · 26.4 ✏️ La même transition vue par SARSA · 26.5 ✏️ Probabilités d'action : ε-greedy (standard et version du livre) et softmax · 26.6 ✏️ Regarder la valeur remonter une chaîne d'états · 26.9 🧮 Mémoire d'une table Q : morpion 4×4, 5×5 et Go · 26.12 📄 Lire Mnih et coll. (2015), « Human-level control through deep reinforcement learning » · 26.14 🔨 Retours actualisés et retours à venir · 26.26 🔨 Itération sur les valeurs : la référence quand le modèle est connu · 26.Q6 🧠 Retour total, retour actualisé et rôle de γ · 26.Q8 🧠 La mise à jour du Q-learning : α, γ et la valeur de l'état suivant · 26.Q9 🧠 ε-greedy ou softmax : vrai ou faux · 26.Q10 🧠 Table initialisée à zéro : comment la valeur remonte et converge · 26.R3 🔁 Bandit à bras multiples, ε-greedy et UCB · 26.E2 💼 À quoi sert le facteur d'actualisation γ ? · 26.E4 💼 Pourquoi DQN utilise-t-il une mémoire de rejeu et un réseau cible ? · 11.2 ∂ Moyenne incrémentale : Qₙ₊₁ = Qₙ + (Rₙ − Qₙ)/n · 19.8 ∂ Moyenne mobile exponentielle : mémoire effective et biais initial · B8.Q4 🧠 Double DQN : d'où vient la surestimation des valeurs Q ? · B8.Q7 🧠 Avantage, erreur TD et GAE : ce que règle λ · B8.1 ✏️ Cible DQN à la main : état terminal, puis cible Double DQN · B8.4 ✏️ GAE à la main sur quatre pas, pour λ = 0, 0,95 et 1

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M26.Q1 | 🧠 | Matrice stochastique, convention ligne, loi à n pas et chemins du graphe : vrai ou faux | ★ | 4 | §1 | C, E | manuel | — |
| M26.Q2 | 🧠 | Une loi stationnaire existe-t-elle, est-elle unique, la loi de la chaîne y converge-t-elle ? Chaînes périodiques et à deux classes | ★ | 4 | §2 | C, E | manuel | — |
| M26.Q3 | 🧠 | Espérance conditionnelle, propriété de la tour et analyse au premier pas : quelle équation pour quel nombre ? | ★ | 4 | §3 | C, E | manuel | — |
| M26.Q4 | 🧠 | Le facteur γ : une actualisation, ou une probabilité de continuer ? Valeur d'un état et politique | ★ | 4 | §4 | C, E | manuel | — |
| M26.Q5 | 🧠 | Le système de Bellman d'une politique fixée : quelles matrices, pourquoi il est inversible, quand γ = 1 est permis | ★ | 4 | §5 | C, E | manuel | — |
| M26.Q6 | 🧠 | Contraction, bornes a priori et a posteriori, itérations synchrones ou en place : vrai ou faux | ★ | 5 | §6 | C, E | manuel | — |
| M26.Q7 | 🧠 | Un maximum dans l'opérateur : ce qui reste (contraction, point fixe unique), ce qui se perd (le système linéaire) | ★ | 4 | §7 | C, E | manuel | — |
| M26.Q8 | 🧠 | Des échantillons au lieu de P : moyenne de retours, pas 1/n ou constant, erreur TD, biais du maximum | ★ | 5 | §8 | C, E | manuel | — |
| M26.R1 | 🔁 | Puissances d'une matrice diagonalisable et méthode de la puissance (M12c) | ★ | 8 | §1 §2 | C, E | manuel | — |
| M26.R2 | 🔁 | La norme ‖·‖∞ d'une matrice, ρ(A) ≤ ‖A‖ et Aᵗ → 0 quand ρ(A) < 1 (M22), et la somme d'une série géométrique (R5) | ★ | 8 | §5 §6 | C, E | manuel | — |
| M26.R3 | 🔁 | Probabilités totales et espérance d'une loi géométrique (M03, M02b) | ★ | 5 | §3 §4 | C, E | manuel | — |
| M26.1 | ✏️ | Des vélos en libre-service entre trois stations : matrice de transition, graphe, loi après deux et trois jours, et coût moyen du lendemain (Pf) | ★ | 30 | §1 §3 | C, E | wbm | — |
| M26.2 | ✏️ | Trois opérateurs et leurs parts de marché : la loi stationnaire par un système linéaire, puis vérifier πP = π | ★★ | 30 | §2 | C, E | wbm | — |
| M26.3 | ✏️ | Trois chaînes qui posent problème, périodique, à deux classes et avec un état transitoire : lois stationnaires et comportement de Pⁿ | ★★ | 40 | §2 | C | wbm | — |
| M26.4 | ✏️ | Un cursus en trois années, avec redoublement et abandon : la probabilité d'être diplômé et la durée moyenne des études, par l'analyse au premier pas | ★★ | 45 | §3 | C, E | wbm | — |
| M26.5 | ✏️ | Un abonné qui peut résilier chaque mois : durée géométrique, revenu total moyen, et le même nombre comme revenu actualisé | ★ | 20 | §4 | C, E | wbm | — |
| M26.6 | ✏️ | Une machine qui s'use, deux politiques d'entretien : P_π et r_π, deux systèmes de Bellman 3 × 3, et la valeur d'une action | ★★ | 50 | §4 §5 | C, E | wbm | — |
| M26.7 | ✏️ | Les itérés de Bellman de la machine de M26.6 : trois pas synchrones puis en place, comparés à la solution, et le nombre d'itérations qui garantit 10⁻³ | ★★ | 40 | §6 | C, E | wbm | M26.6 |
| M26.8 | ✏️ | Vendre une voiture d'occasion : offres au hasard, coût d'attente, valeur de continuation et règle à seuil | ★★ | 30 | §7 | C, E | wbm | — |
| M26.9 | ✏️ | Le meilleur de deux fournisseurs sur des mesures bruitées : le maximum surestime, l'estimateur double non | ★★ | 35 | §8 | C | wbm | — |
| M26.10 | ∂ | L'analyse au premier pas démontrée : t = 1 + Qt et h = Qh + b, et I − Q inversible dès que la fin est possible depuis chaque état | ★★ | 35 | §3 | C | manuel | — |
| M26.11 | ∂ | V = Σ γᵗPᵗr est l'unique solution du système de Bellman : I − γP inversible, série de Neumann démontrée pour γP, et (1 − γ)(I − γP)⁻¹ stochastique | ★★ | 30 | §4 §5 | C, E | manuel | — |
| M26.12 | ∂ | L'opérateur de Bellman d'une politique fixée est une γ-contraction pour ‖·‖∞ ; bornes a priori et a posteriori ; le maximum est 1-lipschitzien | ★★ | 40 | §6 §7 | C, E | manuel | — |
| M26.13 | ∂ | L'erreur TD se télescope : Σ γᵏ δ_{t+k} = G_t − V(S_t) ; une récompense ajoutée γΦ(s′) − Φ(s) décale chaque valeur de −Φ(s) | ★★ | 20 | §8 | C | manuel | — |
| M26.14 | 🔗 | Pont : d'une politique stochastique à la chaîne qu'elle induit, P_π = Σ_a π(a | s) P_a et r_π avec des tableaux à trois axes (actions, états, états), puis Q^π(s, a) et r(s, a, s′) | ★★ | 35 | §4 §5 | C, E | wbm | — |
| M26.15 | 🗣️ | Expliquer avec une image hors informatique pourquoi une chaîne qui mélange oublie son état de départ | ★ | 10 | §2 | C, E | manuel | — |
| M26.E1 | 💼 | « Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que se passe-t-il pour γ = 1 ? » | ★ | 10 | §5 | C | manuel | — |
| M26.16 | 🔨 | La loi d'une chaîne après n pas, en convention ligne · `n_step_distribution` | ★ | 25 | §1 | C, E | pytest | — |
| M26.17 | 🔨 | La loi stationnaire par un système linéaire, et le refus d'une chaîne qui en a plusieurs · `stationary_distribution` | ★★ | 25 | §2 | C, E | pytest | — |
| M26.18 | 🔨 | Le système de Bellman d'une politique fixée, avec une fin possible (matrice sous-stochastique) et γ = 1 quand la fin est sûre · `bellman_linear_solve` | ★★ | 30 | §5 | C, E | pytest | — |
| M26.19 | 🔨 | Les itérés de l'opérateur de Bellman d'une politique fixée (Richardson de pas 1) · `bellman_fixed_point_iterates` | ★ | 25 | §6 | C, E | pytest | — |
| M26.20 | 📦 | La loi stationnaire de trois façons, `np.linalg.eig` sur Pᵀ, `scipy.linalg.null_space` et la méthode de la puissance, sur le surfeur aléatoire d'un web de six pages | ★ | 30 | §2 | C | wbm | — |
| M26.21 | 🔮 | Prédire la somme des lignes de (1 − γ)(I − γP)⁻¹, puis leur limite quand γ tend vers 1, et vérifier | ★ | 20 | §2 §5 | C, E | wbm | M26.17, M26.18 |
| M26.22 | 🔬 | Le biais du maximum par simulation : k fournisseurs de même qualité, n mesures chacun, le meilleur mesuré contre l'estimateur double | ★★ | 30 | §8 | C | wbm | — |
| M26.23 | 🎨 | La loi d'une chaîne au fil des pas depuis trois départs, et ‖μ_n − π‖₁ en échelle logarithmique contre |λ₂|ⁿ | ★ | 20 | §1 §2 | C | manuel | M26.16, M26.17 |
| M26.24 | 🐛 | Chasse à l'erreur : une matrice lue dans la mauvaise convention, une loi stationnaire non normalisée, un état final qui rapporte encore, γ = 1 sans fin | ★ | 30 | §1 §2 §5 | C, E | wbm | — |
| M26.25 | 🛠️ | Un test de propriété : πP = π, et pour `bellman_fixed_point_iterates`, V_k − V tenu par γᵏ‖V₀ − V‖∞ et V = r + γPV pour la limite, sur des chaînes tirées au hasard | ★ | 30 | §2 §6 | C | manuel | M26.17, M26.18, M26.19 |
| M26.26 | 🏆 | Défi : estimer la valeur d'un état à 0,01 près en simulant l'arrêt géométrique (continuer avec la probabilité γ) et en sommant les récompenses sans actualisation, sous un budget de pas simulés | ★★★ | 40 | §4 §8 | C | wbm | M26.18 |

*Notes* : Frontières : les ∂ 26.7 (la somme géométrique (1 − γⁿ)/(1 − γ), la borne r_max/(1 − γ), les horizons 2, 10 et 100, la demi-vie ln 2/(−ln γ), 0,2⁴ et 0,2⁶) et 26.8 (l'équation d'optimalité sur le MDP A, B, T, son système 2 × 2 sous une politique supposée optimale, la contraction de l'opérateur d'optimalité en norme max et la convergence vers une seule table, la cible du Q-learning comme échantillon et le rôle de α), les ✏️ 26.1 (les retours d'une partie de six coups), 26.3 et 26.4 (une mise à jour de Q-learning et de SARSA), 26.5 (les probabilités d'ε-greedy et de la softmax), 26.6 (la valeur qui remonte une chaîne, un état par épisode), 🧮 26.9 (la mémoire d'une table Q), 📄 26.12 (DQN, et sa variante Double Q-learning), 🔨 26.14 (retours et retours à venir) et 26.26 (`value_iteration`), les quiz 26.Q6 (retour d'une courte suite, horizon de 0,95), 26.Q8, 26.Q9 et 26.Q10 (la valeur qui remonte depuis une table nulle), le rappel 26.R3 (la mise à jour incrémentale d'un bandit), 26.E2 (à quoi sert γ) et 26.E4 (rejeu, réseau cible, surestimation corrigée par le Double DQN) ; de workbookIA 11 et 19, faits avant M26, ∂ 11.2 (la moyenne incrémentale) et ∂ 19.8 (la mémoire effective et le biais initial d'une moyenne exponentielle), énoncés et utilisés, jamais redémontrés ; de workbookIA B8, B8.Q4 (d'où vient la surestimation), B8.1 (cible DQN puis Double DQN), B8.Q7 et B8.4 (avantage, erreur TD et GAE : M26 n'écrit aucune somme pondérée par λ). M26 enseigne les outils hors apprentissage par renforcement : des vélos entre des stations, des parts de marché, un petit web, un cursus avec redoublement et abandon, un abonné qui peut résilier, une machine qui s'use et son entretien, un stock, la vente d'une voiture d'occasion, des fournisseurs mesurés avec du bruit ; jamais un agent, un jeu, un coup, une partie, une table Q, une cible r + γ max Q, un learning rate α appliqué à une table, ni Gymnasium (son format P[s][a] = [(p, s′, r, fin)], `terminated` et `truncated`). L'espérance conditionnelle sachant une variable discrète et la formule de l'espérance totale sont définies en M25b (les mélanges) : M26 les rappelle et y ajoute la propriété de la tour et l'analyse au premier pas. ∂ M26.11 démontre la série de Neumann pour γP en entier (‖γP‖∞ = γ < 1), sans renvoyer à CP5.8, un sujet au choix, ni à M22, qui ne l'écrit que dans un corrigé. Contraction et maximum (les deux moitiés de ∂ 26.8.3, que M22 a laissées à M26) : le §6 démontre la contraction de l'opérateur de Bellman d'une politique **fixée**, qui est affine (‖γP(V − W)‖∞ ≤ γ‖V − W‖∞ par ‖P‖∞ ≤ 1, M22), et les bornes a priori γᵏ‖V₀ − V‖∞ et a posteriori γ/(1 − γ)‖V_k − V_{k−1}‖∞ (∂ M26.12), sans avoir besoin de Banach (le point fixe existe : c'est la solution du système) ; l'existence du point fixe d'une contraction non linéaire (Banach) est énoncée et admise, comme en M22. Le §7 démontre le lemme |max x − max y| ≤ max |x − y| sur des vecteurs quelconques (l'indication que donne ∂ 26.8.3) et s'en sert sur un problème d'arrêt optimal à offres indépendantes (une seule équation pour la valeur de continuation, une règle à seuil) ; ∂ M26.12 démontre alors les bornes en entier, la contraction du balayage en place (que la fiche admet) et l'extension du lemme à la k-ième plus grande coordonnée et au sup d'une famille (décision de la session 65) ; que l'opérateur d'arrêt V ↦ max(g, c + γPV) est une γ-contraction est **énoncé**, sans démonstration : combiner le lemme et le §6 est ce que ∂ 26.8.3 fait pour l'opérateur d'optimalité : ni la grille de ∂ M26.12, ni la fiche, ni un quiz n'écrivent la chaîne |max(g, c + γPV) − max(g, c + γPW)| ≤ … ; M26.Q7 énonce la contraction de l'opérateur d'arrêt comme un fait, sans demander de justification ; dans M26.6, la valeur d'une action Q^π(s, a) ne sert ni à vérifier qu'une politique est gloutonne pour ses propres valeurs, ni à désigner la meilleure des deux (∂ 26.8.2). L'équation d'optimalité de Bellman, l'itération sur les valeurs et la politique gloutonne sont énoncées, jamais résolues sur un MDP à plusieurs actions : ni « supposer la politique optimale et résoudre » (∂ 26.8.2), ni table Q*. Le §8 relie l'erreur TD d'une politique fixée au résidu de Bellman (son espérance conditionnelle) et démontre le télescopage (∂ M26.13, que MB8 rappellera, sur des épisodes qui finissent, de valeur 0 à la fin : ni troncature avec amorçage, ni question sur la dépendance de la somme à V, B8.4 j, B8.Q7 e–f) ; il n'écrit aucune cible avec un max et ne discute pas α dans le Q-learning (∂ 26.8.4) : le pas 1/n et le pas constant portent sur des mesures ou des retours simulés, et Σαₜ = ∞, Σαₜ² < ∞ sont énoncées (Robbins-Monro), sans preuve. Le biais du maximum (E[max X̂ᵢ] ≥ max E[X̂ᵢ] ; E[max(Z₁, Z₂)] = 1/√π pour deux gaussiennes centrées réduites indépendantes ; l'estimateur double) porte sur des fournisseurs ou des réglages mesurés avec du bruit (la malédiction du vainqueur, et le score de validation optimiste d'un modèle choisi sur la validation), sans réseau, DQN, cible ni van Hasselt. Le facteur γ : M26 l'interprète comme une probabilité de continuer (arrêt avec la probabilité 1 − γ à chaque pas, durée géométrique d'espérance 1/(1 − γ), M02b), sur un abonné qui résilie (M26.5) ; il ne redémontre pas la somme géométrique (R5) et ne parle ni d'« horizon effectif » ni de demi-vie de γ (∂ 26.7) ; aucun quiz ne calcule le retour d'une courte suite de récompenses (26.Q6), et la valeur actuelle d'un échéancier (R5.11) n'est qu'un exemple de la fiche, sans fonction de `mymath` (🔨 26.14). Les γ des exercices de M26 sont pris parmi 0,6, 0,7, 0,85 et 0,96 : jamais 0,2, 0,5, 0,8, 0,9, 0,95 ni 0,99, les facteurs de workbookIA 26 (0,8 : sa fiche et le 🔨 26.20), ni 0,75 (les exemples de `markov`). La loi stationnaire ne sert aucun exercice de workbookIA 26 : un § court (existence par ‖P‖∞ = 1 et ρ(P) = 1 ; unicité et convergence pour une chaîne irréductible apériodique énoncées, avec deux contre-exemples ; vitesse |λ₂|ⁿ, la chaîne à deux états entièrement calculée dans la fiche ; PageRank), un seul ✏️ dans le parcours essentiel (M26.2), justifié dans la fiche par la promesse de M12c (§3 et §4 : le PageRank par la méthode de la puissance, la vitesse par la deuxième valeur propre), par la fréquence de visite des états, par MB5 (une chaîne qui converge vers sa loi stationnaire) et par MB8 (la loi d'occupation actualisée (1 − γ)μ₀(I − γP)⁻¹, dont les lignes tendent vers π quand γ → 1 : 🔮 M26.21). Conventions : π(a | s) est une politique (comme workbookIA 26) ; la loi stationnaire s'écrit π aux §1 à §3 et d_π pour celle de P_π à partir du §4, et un encadré 📐 le dit (la docstring de `stationary_distribution` garde π) ; les lois sont des lignes (μ_{n+1} = μ_nP, celle des probabilistes), les valeurs des colonnes ((PV)_i = E[V(S₁) | S₀ = i]) ; un encadré 📐 le dit au §1 et le relie à la convention colonne de M22 (μ₀Pⁿ est la récurrence de M22 pour Pᵀ, sans entrée). workbookIA 26 n'écrit jamais P comme une matrice (des sommes Σ_{s′} P(s′ | s, a), avec r(s, a, s′)) : le 🔗 M26.14 fait le passage. Une fin possible se code de deux façons qui donnent les mêmes valeurs : un état absorbant de récompense nulle, ou une ligne sous-stochastique (la masse manquante est la probabilité de finir) ; c'est le « le max vaut 0 quand s′ est terminal » de workbookIA 26, et γP est elle-même sous-stochastique (actualiser, c'est finir avec la probabilité 1 − γ). M26.6 et M26.7 portent sur la même machine (M26.7 itère vers la solution exacte de M26.6). `markov` : NumPy permis, mais de `np.linalg` seulement `solve` et `matrix_rank`, dans `stationary_distribution` et `bellman_linear_solve` ; ni `matrix_power`, `eig`, `eigvals`, `inv`, ni SciPy (oracles des tests : `np.linalg.matrix_power`, `np.linalg.eig` sur Pᵀ, `scipy.linalg.null_space`, `scipy.linalg.solve`, la série Σ γᵗPᵗr tronquée, la propriété V = r + γPV et la borne γᵏ‖V₀ − V‖∞ ; jamais une autre fonction de l'apprenant ; les tests de γ = 1 restent sur des cas bien conditionnés, cond(I − P) ≤ 10⁸, et un P ou un μ₀ non fini est refusé). `bellman_linear_solve` est l'oracle des tests de `value_iteration` dans workbookIA 26, avec un contrat distinct : la matrice m × m de la politique fixée (pas le dictionnaire de Gymnasium), un vecteur de récompenses, V seul (ni Q, ni max, ni actions). `bellman_fixed_point_iterates` est calqué sur `richardson_iterates` (M19) : sans max, sans seuil d'arrêt ni nombre maximal d'itérations, il ne remplace pas `value_iteration` (🔨 26.26) ; il calculerait les itérés de ✏️ 26.6 et de 26.Q10 sur leur chaîne, donc il ne sert à aucun exercice de M26 sur une chaîne qui avance d'un état par pas avec une seule récompense finale (26.6, 26.Q10, Évités). Aucune fonction de retour actualisé, de politique, de mise à jour, d'arrêt optimal ni de simulation. `markov_bound` (M11) est l'inégalité de Markov : la docstring du module le signale. Évités (règle de partage) : la chaîne 0 → 1 → 2 → 3 à récompense finale 1 avec γ = 0,9 (valeurs 1, 0,9 et 0,81), ses variantes (10 états ; γ = 0,5 → 0,25 ; α = 0,5 → 0,225 et 0,875) ; la chaîne P_26 de 26.26 (0 → 1 → 2, récompense 1 au dernier pas, l'action 1 ramène en 0, γ = 0,5, V* = (0,5 ; 1 ; 0), Q* = [[0,5 ; 0,25] ; [1 ; 0,25] ; [0 ; 0]]) ; le MDP A, B, T de ∂ 26.8 (rester, aller, finir, jouer ; récompenses 0, 0, 1 et 2 ; probabilité ½ ; γ = 0,9 ; 400/119, 360/119, 324/119, 0,595, 0,405 ; échantillons 2 ou 4,72, moyenne 3,36 ; variante 0,5 → 0,9, 0,81 et 0,905) ; l'exemple de `value_iteration` (rester 0 ou finir 1, γ = 0,9 → V = (1 ; 0), Q = [[0,9 ; 1] ; [0 ; 0]]) ; les récompenses (0, 0, 1), (2, 0, 1), (1, 0, 0, 2, 0, 4), (0, 3, 0, 1), (1, 1, 1, 1), (1, 0, 2) et (1, 1, 1) et leurs retours (0,81, 2,25, 1,375, 4,820, 5,24, 1,625, 1,875, 1,75, 1,5) ; REWARDS_15 (graine 2615) et ses retours 0,80 à 8,06 ; γ = 0,2, 0,5, 0,9, 0,95 et 0,99, les horizons 2, 10, 20 et 100, les demi-vies 6,58, 7, 13,5, 14, 68,97 et 69, 0,2³, 0,2⁴, 0,2⁵, 0,2⁶ et 1/(1 − 0,2) = 1,25 ; les lignes Q (0,1 ; 0,6 ; 0,3 ; 0,6), (1, 2, 4, 0), (1 ; 2 ; 4 ; 0,5) et [[0,2 ; 0,4] ; [1 ; 0,6] ; [0 ; 0]], r = 0,2 et Q = 0,5 (0,74, 0,24, 0,62, 0,35, 0,47, 0,485), Q = 0,4, r = 0,1, γ = 0,8 et max 0,5 (cible 0,5, δ = 0,1, 0,45), r = 0,5 et γ = 0,8 (1,3, 0,9, 0,85), Q = 0,4, max 0,8 → 0,6, le bandit 3, 5 et 0,25 → 3,5 ; ε = 0,2 avec 4 actions (0,85, 0,05, 0,80, 0,067), ε = 0,1 avec 5 actions (0,92), les températures 1, 2, 0,5 et 0,8 (0,831, 0,579, 0,979, 0,571) ; FrozenLake (16 états, V*(0) = 0,54 et 0,069, 73,2 % et 74,9 %), Flippers et son camion, le L-learning, CliffWalking, le morpion, CartPole, le go, AlphaGo, le backgammon, les robots, les ascenseurs, les cultures, le cuisinier et son minuteur, le compte en banque de la fiche de workbookIA 26 ; 2⁹, 3⁹, 3¹⁶, 3³⁶¹, 5 478, 255 168, 3²⁵ et les mémoires de 🧮 26.9 (4 octets, 16 Go, 2,8 Go, 85 To, 10⁹ mises à jour par seconde, 25 → 256 → 256 → 25 et 78 873 paramètres) ; le DQN de Mnih (84 × 84, 18 actions, 10 000 pas, un million, 32, ε de 1 à 0,1) ; le paradoxe des anniversaires (32 parmi 1 000, 0,39) ; les cinq graines (57, 35, 74, 74 et 38 %, [41,2 ; 70,6]). Évités aussi (reprises de ce dépôt) : les exemples des docstrings de `markov` ([[0,5 ; 0,5 ; 0] ; [0,25 ; 0,5 ; 0,25] ; [0 ; 0,5 ; 0,5]], [[0,6 ; 0,4] ; [0,2 ; 0,8]], [[0,5 ; 0,5] ; [0 ; 1]] avec r = (1, 2) et γ = 0,75, [[0,5 ; 0,25] ; [0,5 ; 0]]), la contraction de ∂ M22.14 (A = [[0,3 ; −0,3] ; [0,1 ; 0,3]], c = (1, 2)), les polluants du lac et la plante de M22, la barre qui tiédit et les deux ressorts de M19, les matrices de M12c §4 et §5, la population à pile ou face de M22 §5. Pas de MML (le livre ne traite pas les chaînes de Markov), donc pas de 📖 ; références libres : Blitzstein et Hwang, ch. 11 (chaînes de Markov) ; pour Bellman, Sutton et Barto (2ᵉ éd.), §3.5-3.6 et §4.1-4.4, cités par sections. 17,9 h au lieu des 12 h prévues (14,6 h au syllabus de la session 60 ; lecture 170 min et durées des exercices recalées après les vérifications de la session 65) : la propriété de la tour et l'analyse au premier pas, le cas d'une fin possible (γ = 1 quand la fin est sûre), l'arrêt optimal, l'erreur TD et le biais du maximum, que workbookIA 26 suppose ou que MB8 rappellera ; la loi stationnaire reste courte, Banach et la convergence d'une chaîne irréductible apériodique sont énoncés.

<a id="m27"></a>
## M27 · Jeux et distances entre lois

**Partie** VI · **prépare** workbookIA 27 · **dossier** `chapitres/m27_jeux_distances/` · **MML** §7.2 · **sessions de génération** 1

Les jeux à deux joueurs et les distances entre lois. D'abord les jeux à somme nulle : la matrice des gains, le maximin et le minimax (l'inégalité minimax de MML §7.2), les points selles et les stratégies dominées ; les stratégies mixtes, la stratégie d'indifférence d'un jeu 2 × 2 et le théorème minimax de von Neumann ; l'équilibre de Nash d'un jeu quelconque et l'induction arrière sur un arbre de jeu ; la descente-montée de gradient sur un jeu bilinéaire, qui tourne autour de l'équilibre ou s'en éloigne. Puis les lois : la probabilité a posteriori est le meilleur prédicteur pour la log-loss ; la divergence de Jensen-Shannon plafonne à ln 2 quand les supports se séparent ; les couplages et les distances de Wasserstein, calculées en dimension 1 par les fonctions de répartition et les quantiles, dont W₂ de deux gaussiennes ; la distance de Fréchet entre gaussiennes et le biais d'une distance estimée sur des échantillons ; enfin trois mesures d'une dérive (PSI, Kolmogorov-Smirnov, W₁). workbookIA 27 applique ces outils aux GAN, et workbookIA B7 à la surveillance d'un modèle en production.

**Temps** : 18,7 h en parcours complet, 12,8 h en parcours essentiel (lecture 165 min, 20 flashcards).

**Objectifs**

- Trouver le maximin, le minimax et les points selles d'une matrice de gains, et réduire un jeu par dominance.
- Calculer les stratégies optimales et la valeur d'un jeu 2 × 2 par indifférence, et énoncer le théorème minimax de von Neumann.
- Trouver les équilibres de Nash d'un jeu à deux joueurs, et la valeur d'un arbre de jeu par induction arrière.
- Prévoir, par les valeurs propres d'un pas, si la descente-montée tourne autour d'un équilibre ou s'en éloigne.
- Calculer la probabilité a posteriori qui minimise la log-loss espérée, et démontrer qu'elle la minimise.
- Calculer la divergence de Jensen-Shannon de deux lois, et expliquer pourquoi elle plafonne à ln 2.
- Écrire un couplage de deux lois discrètes, calculer son coût, et trouver le plan optimal sur la droite.
- Calculer W₁ et W₂ en dimension 1 par les fonctions de répartition ou par les quantiles, dont W₂ de deux gaussiennes.
- Calculer la distance de Fréchet de deux gaussiennes dans un cas commutatif, et le biais d'une distance estimée sur des échantillons.
- Mesurer une dérive par le PSI, la statistique de Kolmogorov-Smirnov et W₁, et dire ce que chacune mesure.

**Sections de la fiche**

- §1 Jeux à somme nulle : matrice des gains, maximin et minimax, point selle, stratégies dominées
- §2 Stratégies mixtes : gain espéré, indifférence et théorème minimax de von Neumann
- §3 Équilibre de Nash, jeux à somme non nulle, et arbres de jeu (induction arrière)
- §4 Jouer par gradients : descente-montée simultanée ou alternée sur un jeu bilinéaire
- §5 Le meilleur prédicteur pour la log-loss : la probabilité a posteriori
- §6 Jensen-Shannon revisitée : bornée par ln 2, aveugle quand les supports se séparent
- §7 Transporter une loi sur une autre : couplages, plans de transport et distances de Wasserstein
- §8 Wasserstein en dimension 1 : fonctions de répartition, quantiles, appariement trié, deux gaussiennes
- §9 La distance de Fréchet entre gaussiennes, et le biais d'une distance estimée
- §10 Mesurer une dérive : PSI, Kolmogorov-Smirnov et W₁

**Notions enseignées** : jeu à deux joueurs à somme nulle : matrice des gains, maximin et minimax en stratégies pures, maximin ≤ minimax (l'inégalité minimax, MML §7.2), point selle, stratégies dominées · l'ordre compte : le joueur qui annonce son coup en second a l'avantage ; la dualité faible lue comme un jeu · stratégies mixtes : gain espéré pᵀGq, stratégie d'indifférence d'un jeu 2 × 2 (démontrée optimale), valeur d'un jeu · théorème minimax de von Neumann (énoncé) ; un jeu fini est un programme linéaire (énoncé) · équilibre de Nash : définition générale, jeux à somme non nulle (dilemme du prisonnier, coordination), équilibres multiples, purs et mixtes ; dans un jeu à somme nulle, un couple de stratégies optimales · arbres de jeu : induction arrière, minimax d'un arbre · dynamique de gradients sur un jeu : descente-montée simultanée (une spirale qui s'éloigne) et alternée (une courbe fermée, une ellipse : x² + y² − ηxy reste constant sur xy) sur un jeu bilinéaire ; l'équilibre est un point selle de f · meilleur prédicteur pour la log-loss : la probabilité a posteriori P(Y = 1 | x) = π₁p₁(x)/(π₁p₁(x) + π₀p₀(x)) (Bayes, priors quelconques) ; la log-loss est une règle de score propre (*proper scoring rule*) ; le maximum de vraisemblance k ln p + (n − k) ln(1 − p) d'une loi de Bernoulli rappelé (M04.12, M13a.1), avec des comptes entiers · divergence de Jensen-Shannon revisitée : 0 ≤ JS ≤ ln 2, JS = ln 2 pour des supports disjoints, constante (sans pente) quand les supports se séparent ; la KL y est infinie · couplages et plans de transport sur des supports finis (marges imposées, couplage indépendant), coût d'un plan, distances de Wasserstein W_p ; le transport optimal est un programme linéaire · W₁ ≤ W₂ (Jensen sur un même couplage) ; dualité de Kantorovich-Rubinstein : W₁ comme un maximum sur les fonctions 1-lipschitziennes (énoncée) · W_p en dimension 1 : W₁ = ∫|F − G|, W_p^p = ∫₀¹|F⁻¹(u) − G⁻¹(u)|^p du (le couplage des quantiles, optimal) ; appariement trié optimal (argument d'échange) · W₂ de deux gaussiennes en dimension 1 : W₂² = (μ₁ − μ₂)² + (σ₁ − σ₂)² ; W_p d'une translation · distance de Fréchet (W₂) entre gaussiennes : formule (admise en général), Tr((Σ₁Σ₂)^{1/2}) = Σ√λᵢ(Σ₁Σ₂), Σ₁Σ₂ semblable à Σ₁^{1/2}Σ₂Σ₁^{1/2} (Σ₁ définie positive) ; cas commutatif démontré (une somme de W₂² en dimension 1) ; invariance par une rotation commune · biais d'une distance estimée : E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ ; comparer à tailles égales · mesurer une dérive : PSI = KL(p ‖ q) + KL(q ‖ p) (divergence de Jeffreys) sur des classes, et J = Σ(p_k − q_k) ln(p_k/q_k) ≈ Σ(p_k − q_k)²/q_k pour un petit décalage ; statistique de Kolmogorov-Smirnov sup|F − G|, W₁ = ∫|F − G| ; unités, invariances, W₁ ≤ (b − a)·KS sur [a, b]

**Prérequis** : intégrales, changement de variable, fonction de répartition et quantile F⁻¹(u) = inf{x : F(x) ≥ u} (M02a) · espérance d'une variable discrète, indépendance, fonction de répartition, loi normale et Φ, simulation par inversion F⁻¹(U) (M02b) · biais d'un estimateur, variance d'une moyenne, matrice de covariance (M02c) · formule de Bayes, a priori et a posteriori ; le maximum de vraisemblance d'une loi de Bernoulli est la fréquence (M04) · approximation affine, ln(1 + x) ≈ x (M05a) · point selle d'une fonction de deux variables, descente et montée de gradient (M05b) · divergence KL, inégalités de Jensen et de Gibbs, divergence de Jensen-Shannon (M06) · p-valeur d'un test (M08) · programmes linéaires (M10) · trace, matrices semblables, théorème spectral, racine carrée d'une matrice symétrique positive (M12c) · log-loss, la log-loss quand la probabilité prédite tend vers 0 (M13a) · lagrangien et dualité faible, MML §7.2 lu une première fois (M13b) · valeurs propres complexes d'une matrice 2 × 2, module, rotations et homothéties, puissances (M22) · KL entre deux lois continues, KL infinie quand le support de q ne couvre pas celui de p (M25a)

**mymath** : `distances.py` (signatures figées) : `pure_strategy_values`, `mixed_strategy_value_2x2`, `descent_ascent_iterates`, `w2_gaussians_1d`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 27.5 ∂ Le discriminateur optimal D* = p_data / (p_data + p_g) · 27.6 ∂ Pourquoi log(1 − D(G(z))) sature et pas −log D(G(z)) · 27.2 ✏️ Valeur minimax d'une petite matrice de gains · 27.3 ✏️ Losses BCE du discriminateur et du générateur à partir de sorties données · 27.4 ✏️ À l'équilibre, la loss vaut ln 2 et non 0,5 · 27.7 🧮 Croissance progressive : où passe le temps de calcul ? · 27.10 📄 Lire Goodfellow et coll. (2014), « Generative Adversarial Nets » · 27.11 🔨 Distance de Wasserstein 1D entre deux échantillons · 27.13 🔮 Prédire la moyenne et l'écart-type générés au fil des epochs · 27.14 📈 Lire les courbes d'un GAN : losses, D(x) et D(G(z)) · 27.18 🔬 Loss saturante ou non saturante : la dynamique du début · 27.22 🔨 Distance de Fréchet entre deux gaussiennes (la formule du FID) · 27.23 📦 Évaluer un générateur : distance de Fréchet sur les features d'un classifieur · 27.Q5 🧠 Coopératifs ou antagonistes : somme nulle, minimax et équilibre de Nash · 27.E1 💼 Expliquer l'entraînement d'un GAN et sa loss · 27.E4 💼 Comment évaluer un modèle génératif (FID et ses limites) ? · 27.E5 💼 Pourquoi l'entraînement des GAN est-il instable ? · B7.4 ✏️ Indice de stabilité de population (PSI) à la main sur quatre intervalles · B7.22 📈 Surveiller la dérive : PSI et test KS sur des images assombries ou bruitées, quand alerter ? · B7.Q11 🧠 Écart entraînement-production et dérive des données : vrai ou faux · B7.E4 💼 Comment surveilles-tu un modèle en production, et que fais-tu en cas de dérive ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M27.Q1 | 🧠 | Maximin, minimax et point selle : qui annonce son coup en premier, et qui y gagne ? | ★ | 5 | §1 | C, E | manuel | — |
| M27.Q2 | 🧠 | Stratégies mixtes, gain espéré et valeur d'un jeu : vrai ou faux | ★ | 5 | §2 | C, E | manuel | — |
| M27.Q3 | 🧠 | Équilibres de Nash, arbres de jeu et descente-montée : unique ou non, le meilleur pour tous ou non, converger ou tourner ? | ★ | 4 | §3 §4 | C, E | manuel | — |
| M27.Q4 | 🧠 | La probabilité a posteriori et la log-loss ; Jensen-Shannon et KL quand les supports se séparent | ★ | 5 | §5 §6 | C, E | manuel | — |
| M27.Q5 | 🧠 | Couplages et distances de Wasserstein : marges, translation, dilatation, et W₁ ≤ W₂ | ★ | 5 | §7 §8 | C, E | manuel | — |
| M27.Q6 | 🧠 | La distance de Fréchet et son estimation : rotation commune, covariances, taille des échantillons | ★ | 4 | §9 | C, E | manuel | — |
| M27.Q7 | 🧠 | Mesurer une dérive : PSI, KS ou W₁, leurs unités, et ce que chacun ne voit pas | ★ | 5 | §10 | C, E | manuel | — |
| M27.R1 | 🔁 | Le maximum de vraisemblance d'une loi de Bernoulli (des comptes entiers), et la log-loss quand la probabilité prédite tend vers 0 (M04, M13a) | ★ | 8 | §5 | C, E | manuel | — |
| M27.R2 | 🔁 | Les valeurs propres complexes d'une matrice réelle 2 × 2, leur module et les puissances (M22) | ★ | 7 | §4 | C, E | manuel | — |
| M27.R3 | 🔁 | La racine carrée d'une matrice symétrique positive, et la trace comme somme des valeurs propres (M12c) | ★ | 6 | §9 | C, E | manuel | — |
| M27.1 | ✏️ | Deux enseignes se partagent un marché : réduire une matrice 3 × 4 par dominance, trouver ses deux points selles et vérifier qu'ils ont la même valeur, et ce que la réduction ne change pas (maximin, minimax) | ★ | 30 | §1 | C, E | wbm | — |
| M27.2 | ✏️ | Tirs au but : la probabilité de tirer à gauche par indifférence, la réponse du gardien et la valeur du jeu | ★★ | 25 | §2 | C, E | wbm | — |
| M27.3 | ✏️ | Les équilibres de Nash d'un dilemme du prisonnier et d'un jeu de coordination (purs et mixte), puis la valeur d'un jeu d'allumettes par induction arrière | ★★ | 30 | §3 | C, E | wbm | — |
| M27.4 | ✏️ | Descente-montée sur f(x, y) = xy : la matrice d'un pas simultané puis alterné, leurs valeurs propres et leurs modules, et deux pas différents pour x et y | ★★ | 30 | §4 | C, E | wbm | — |
| M27.5 | ✏️ | Deux fournisseurs et un défaut noté sur quatre niveaux : la probabilité a posteriori, et la log-loss moyenne de trois prédicteurs (a priori, a posteriori, trop sûr de lui) | ★★ | 40 | §5 | C, E | wbm | — |
| M27.6 | ✏️ | Deux lois uniformes de même largeur, translatées : JS en fonction du décalage, la KL, et ce que le décalage lui-même mesure | ★★ | 25 | §6 | C, E | wbm | — |
| M27.7 | ✏️ | Trois dépôts et trois magasins le long d'une route : vérifier des couplages, leur coût, le couplage indépendant et le plan monotone (coin nord-ouest) | ★★ | 30 | §7 | C, E | wbm | — |
| M27.8 | ✏️ | W₁ et W₂ par l'aire entre les fonctions de répartition et par les quantiles : deux lois uniformes, puis W₂ de deux gaussiennes (et W₁ quand elles ont le même écart-type) | ★★ | 30 | §8 | C, E | wbm | — |
| M27.9 | ✏️ | La distance de Fréchet de deux gaussiennes du plan à covariances diagonales, puis tournées ensemble : la part des moyennes et celle des covariances | ★★ | 30 | §9 | C, E | wbm | — |
| M27.10 | ✏️ | Une dérive en deux mois d'une variable à trois catégories : la divergence de Jeffreys (le PSI) et JS, puis l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage ; enfin KS et W₁ entre deux petits échantillons de températures de même taille | ★★ | 35 | §10 | C, E | wbm | — |
| M27.11 | ∂ | Le maximin est au plus le minimax ; ils sont égaux si et seulement si le jeu a un point selle, et deux points selles ont la même valeur | ★★ | 20 | §1 | C, E | manuel | — |
| M27.12 | ∂ | La log-loss espérée est minimale pour la probabilité a posteriori : une preuve par l'inégalité de Gibbs | ★★ | 25 | §5 | C, E | manuel | — |
| M27.13 | ∂ | 0 ≤ JS ≤ ln 2, et JS = ln 2 si et seulement si les deux lois ont des supports disjoints | ★★ | 25 | §6 | C | manuel | — |
| M27.14 | ∂ | L'appariement trié est optimal : un argument d'échange sur deux paires, puis sur n paires, pour les coûts |x − y| et (x − y)² | ★★ | 40 | §8 | C | manuel | — |
| M27.15 | ∂ | E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ : une distance estimée sur deux échantillons est biaisée vers le haut | ★★ | 25 | §9 | C, E | manuel | — |
| M27.16 | 🔗 | Pont : la distance de Fréchet en dimension 1, W₂² = (Δμ)² + (Δσ)², entre deux lois résumées par leur moyenne et leur écart-type (deux séries d'une machine, avant et après réglage) : la part de la moyenne et celle de l'écart-type, et pourquoi workbookIA 27 l'écrit avec des covariances et en rend le carré | ★ | 20 | §8 §9 | C, E | wbm | — |
| M27.17 | 📖 | MML §7.2 relu : l'inégalité minimax (7.23) et sa preuve, la dualité faible (7.27) lue comme un jeu, et l'inégalité vérifiée sur une matrice de gains choisie | ★★ | 35 | §1 | C | manuel | — |
| M27.18 | 🗣️ | Expliquer avec une partie de cache-cache pourquoi jouer au hasard peut être la meilleure stratégie, et ce que le hasard garantit | ★ | 15 | §2 | C, E | manuel | — |
| M27.E1 | 💼 | « Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se recouvrent pas, et pas Jensen-Shannon ? » | ★ | 10 | §6 §8 | C, E | manuel | — |
| M27.E2 | 💼 | « Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et comment comparer deux mesures ? » | ★ | 10 | §9 §10 | C | manuel | — |
| M27.19 | 🔨 | Les valeurs d'un jeu en stratégies pures : maximin, minimax et coups prudents, points selles compris · `pure_strategy_values` | ★ | 25 | §1 | C, E | pytest | — |
| M27.20 | 🔨 | Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle · `mixed_strategy_value_2x2` | ★★ | 25 | §2 | C, E | pytest | M27.19 |
| M27.21 | 🔨 | Les itérés de la descente-montée simultanée ou alternée sur un jeu bilinéaire xᵀAy · `descent_ascent_iterates` | ★★ | 35 | §4 | C | pytest | — |
| M27.22 | 🔨 | W₂ de deux gaussiennes en dimension 1, à partir des moyennes et des écarts-types · `w2_gaussians_1d` | ★ | 15 | §8 | C, E | pytest | — |
| M27.23 | 📦 | `scipy.optimize.linprog` : le transport optimal entre deux lois discrètes de la droite comme programme linéaire, comparé au plan monotone et à l'aire entre les fonctions de répartition | ★★ | 35 | §7 §8 | C | wbm | — |
| M27.24 | 🔮 | Prédire la trajectoire de la descente-montée simultanée puis alternée sur xy, puis la tracer : spirale qui s'éloigne ou courbe fermée ? | ★ | 25 | §4 | C | wbm | M27.21 |
| M27.25 | 🔬 | Le biais d'une distance estimée : ‖x̄₁ − x̄₂‖² entre deux échantillons d'une même loi de ℝ³, selon leurs tailles, contre tr Σ₁/n₁ + tr Σ₂/n₂ | ★★ | 30 | §9 | C | wbm | — |
| M27.26 | 🎨 | Deux fonctions de répartition sur une même figure : l'aire entre elles (W₁) et leur plus grand écart vertical (KS), pour une translation puis une dilatation | ★ | 25 | §8 §10 | C, E | manuel | — |
| M27.27 | 🐛 | Chasse à l'erreur : une stratégie d'indifférence calculée sur ses propres gains, W₂ de deux gaussiennes avec des variances, des échantillons appariés sans être triés | ★ | 35 | §2 §8 | C | wbm | — |
| M27.28 | 🛠️ | Un test de propriété : la valeur d'un jeu 2 × 2 tiré au hasard est entre maximin et minimax, et devient v + c pour G + c et k v pour k G (k > 0) | ★ | 40 | §2 | C | manuel | M27.20 |
| M27.29 | 🏆 | Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂, et cette distance, à 10⁻³ près | ★★★ | 45 | §8 | C | wbm | — |

*Notes* : Frontières : les ∂ 27.5 (D* = p_data/(p_data + p_g) par le maximum de a ln y + b ln(1 − y), dérivée nulle puis dérivée seconde, l'intégrale maximisée point par point, V(D*, G) = −ln 4 + 2 JS, son minimum en p_g = p_data) et 27.6 (les dérivées −D et −(1 − D) de ln(1 − σ(a)) et de −ln σ(a), D = 0,01 et le rapport 99, la BCE avec logits ln(1 + e^{−a})), ✏️ 27.2 (maximin, minimax et point selle d'une matrice 3 × 3 ; « min_G max_D ou max_D min_G »), ✏️ 27.3 et 27.4 (les losses BCE d'un mini-batch, ln 2 et 2 ln 2 à l'équilibre, 0,607), 🧮 27.7, 📄 27.10 (Goodfellow et coll. 2014, −log 4), 🔨 27.11 (`wasserstein_1d`), 🔨 27.22 et 📦 27.23 (`frechet_distance`, le FID et sa dépendance au nombre d'images), la dynamique d'un GAN (🔮 27.13, 📈 27.14, 🔬 27.18, 💼 27.E5), 27.Q5 (somme nulle, poker, Nash, D = 0,5 à l'équilibre), 💼 27.E1 et 27.E4 ; et, de workbookIA B7, qui n'a pas de chapitre de maths et que le §10 prépare, ✏️ B7.4 (un PSI à la main sur quatre intervalles, l'intervalle vide et ε, les seuils), 📈 B7.22, B7.Q11 et 💼 B7.E4. M27 enseigne les outils hors réseau : un marché que deux enseignes se partagent, des tirs au but, une partie de cache-cache, le dilemme du prisonnier, un jeu de coordination, un jeu d'allumettes, des dépôts et des magasins, des fournisseurs, des séries de production, des relevés de capteurs ; jamais un générateur, un discriminateur, un faux, une loss de GAN ni un learning rate. « GAN : générateur et discriminateur, le jeu mathématique » est retiré des notions du plan : M27 n'écrit ni V(D, G) ni min_G max_D. Le maximum de vraisemblance k ln p + (n − k) ln(1 − p) d'une loi de Bernoulli, avec des comptes entiers (∂ M04.12, M13a.1), et la log-loss quand la probabilité prédite tend vers 0 (M13a.4) ne sont que des rappels (🔁 M27.R1, sur d'autres nombres) ; M27.R1 ne compare jamais −ln p et ln(1 − p) ni leurs dérivées en un même point (∂ 27.6) ; le §5 enseigne l'énoncé plus général « la probabilité a posteriori P(Y = 1 | x) = π₁p₁(x)/(π₁p₁(x) + π₀p₀(x)) minimise la log-loss espérée », démontré par l'inégalité de Gibbs (∂ M27.12) et non par f′ et f″, avec des priors inégaux et des lois d'un autre domaine (fournisseurs et défauts, ✏️ M27.5) : aucun exercice ne prend des priors égaux, n'appelle ce prédicteur un discriminateur, ne maximise une intégrale de deux densités point par point, ne calcule la valeur du minimum en formule (l'entropie conditionnelle H(Y | X)) ni ne la relie à Jensen-Shannon (c'est le cœur de ∂ 27.5.4) ; M27.5 en donne seulement des valeurs numériques, et M27.Q4 ne demande ni la valeur ½ où π₁p₁ = π₀p₀, ni la limite 1 quand p₀(x) → 0 (∂ 27.5.3). La saturation (∂ 27.6) n'est pas reprise : ni ln(1 − σ(a)) contre −ln σ(a), ni le facteur σ(1 − σ) comparé à σ − y (le ∂ 18.8.4 de workbookIA l'a déjà fait), ni « même minimiseur, gradients différents » en exercice. Les jeux : ✏️ M27.1 prend d'autres matrices que 27.2 et la fiche 27, sans les noms « Ligne » et « Colonne », et une matrice avec point selle (réduite par dominance) : aucune 3 × 3 sans point selle ne fait chercher maximin et minimax (27.2) ; au-delà de 27.2, M27 enseigne les stratégies mixtes (l'indifférence d'un 2 × 2, démontrée optimale dans la fiche ; la valeur), le théorème minimax de von Neumann (énoncé) et le lien avec la programmation linéaire (énoncé, MML §7.3.1 en option) ; l'avantage de jouer en second est enseigné sur des jeux hors réseau (Q1), jamais sur min_G max_D ; Nash sur un dilemme du prisonnier et un jeu de coordination (équilibres purs et mixte), pas sur le poker ni par les questions de 27.Q5 ; l'arbre sur un jeu d'allumettes, pas sur le morpion (fiche 26, 🔬 26.37, 27.R1). La dynamique (§4) porte sur le jeu bilinéaire f(x, y) = xᵀAy et sur xy : pas simultané (des valeurs propres de module > 1) contre alterné (de déterminant 1), et deux pas différents pour x et y (des pas inégaux ne suffisent pas) ; ni GAN, ni loss, ni les learning rates de 27.14 (10⁻⁴, 10⁻³, 10⁻²), ni TTUR nommé ; M27.4 évite η = 0,25 et η = 0,5 (ηa = 0,5, l'exemple du stub). Jensen-Shannon (§6) : 0 ≤ JS ≤ ln 2 (∂ M27.13), JS = ln 2 pour des supports disjoints, sur deux lois uniformes de même largeur translatées l'une de l'autre (✏️ M27.6) ; ni D*, ni −ln 4. Wasserstein (§7, §8) : couplages et plans de transport sur des supports finis, W_p, le programme linéaire (📦 M27.23), la dualité de Kantorovich-Rubinstein énoncée ; en dimension 1, W₁ = ∫|F − G| et W_p par les quantiles (le couplage des quantiles est optimal : démontré pour deux échantillons de même taille par un argument d'échange, ∂ M27.14, admis en général), W₂ de deux gaussiennes, W_p d'une translation ; l'optimalité de l'appariement trié, que 27.11 admet, est donc démontrée, mais aucun exercice ni aucune fonction ne calcule W₁ entre deux échantillons de tailles différentes (le cœur de 27.11) ; W₁ entre deux petits échantillons de même taille, à la main, seulement au §10 (M27.10) ; W₁ de deux gaussiennes d'écarts-types différents n'est pas calculé (E|a + bZ|, la variante de 27.11). Fréchet (§9) : la formule, admise en général, Tr((Σ₁Σ₂)^{1/2}) = Σ√λᵢ, Σ₁Σ₂ semblable à Σ₁^{1/2}Σ₂Σ₁^{1/2} pour Σ₁ définie positive (démontré dans la fiche, en trois lignes), le cas commutatif démontré (une somme de W₂² en dimension 1, invariante par une rotation commune ; ✏️ M27.9 sur des covariances diagonales du plan) ; aucun code ne calcule une distance de Fréchet avec `scipy.linalg.sqrtm` ni à partir de features (le contrat et l'oracle de 27.22) ; le biais d'une distance estimée porte sur les moyennes (∂ M27.15, 🔬 M27.25 : deux séries d'une même machine), sans FID, Inception, nombre d'images ni la suite 123,2 → 119,3 de 27.23 ; le 🔗 M27.16 porte sur une convention (la distance de Fréchet en dimension 1, que workbookIA 27 écrit avec des covariances et rend au carré), jamais sur des résumés relevés epoch par epoch (🔮 27.13, 📈 27.14). Dérive (§10, pour workbookIA B7 ; workbookIA 29 mesure le décalage par la performance d'un modèle, sans distance entre lois, et sa couverture passe à M02c et M03) : PSI = KL(p ‖ q) + KL(q ‖ p) (la divergence de Jeffreys) sur une variable à trois catégories (M27.10), sans quantiles de la référence, sans intervalle vide ni ε, sans seuils 0,1 et 0,25, ni contribution d'une catégorie, ni vérification de PSI = KL + KL en exercice (B7.4 : l'identité reste dans la fiche) ; M27.10 en tire l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage, que B7 n'a pas ; KS = sup|F − G| comme statistique, sa p-valeur seulement nommée (M08), sans « tout devient significatif sur de grands échantillons » (B7.Q11 c et la fiche B7) ; W₁ = ∫|F − G|, ses unités, W₁ ≤ (b − a)·KS ; ni images, ni luminosité, ni sorties softmax. Évités (règle de partage) : les matrices [[3, −1, 2], [1, 0, 4], [−2, 5, −3]] (maximin 0, minimax 3, maxima des colonnes 3, 5 et 4) et [[2, 4], [1, 0]] (point selle 2), les territoires 5, 10 et 20 ; Glenn et Dawn, les faux billets, le faux vin, le poker ; les sorties D = 0,9 ; 0,7 ; 0,8 ; 0,6 ; 0,3 ; 0,1 ; 0,2 et 0,4, D = 0,01 et le rapport 99, D = 0,9 et le rapport 9, D = 0,5 ; ln 2, 2 ln 2 ≈ 1,386, −ln 4 et 0,607 présentés comme valeurs d'un jeu ou d'une loss ; 𝒰[0, 1] contre 𝒰[0, 2] (2/3), les mélanges 0,6 𝒩(1,5 ; 0,8) + 0,4 𝒩(−1,5 ; 0,6) et 𝒩(0,3 ; 1,6) de la figure du D*, p_data = 0,3 et p_g = 0,1 (0,75, CP6.4 de workbookIA) ; les échantillons (4, 1) et (2, 2) (W₁ = 1,5), [3, 1, 2] et [2, 6, 4] (2,0), [5, −1, 2,5] et ses permutations, [0, 2] et [1] (1,0), [0, 1, 3] et [5, 6, 8] (5,0), [0, 1] et [0, 1, 2] (0,5), (0,4 ; 1,1 ; 1,7 ; 2,9) et (1,0 ; 2,2 ; 3,1 ; 3,6), 50 normales décalées de 0,5 ; les lois 𝒩(4 ; 1,25²), 𝒩(5 ; 1,25²), 𝒩(4 ; 2,5²), le Dirac en 4 et 1,25√(2/π), 𝒩(0, 1) contre 0 et √(2/π) ≈ 0,80, 𝒩(0 ; 4) contre 𝒩(1 ; 1) (W₂² = 2 : aucune paire de gaussiennes avec (Δμ, Δσ) = (1, 1)) ; les covariances diag(9, 1) et I (4), diag(1, 4) et diag(4, 1) (2), diag(4, 9) et I avec les moyennes (1, 2) (5), les moyennes (0, 0) et (3, 4) (25), les décalages de 1 et de 2 sur chaque axe d'un nuage de ℝ³ (3 et 12), les moyennes 0 et (1, 1, 1) (3) ; les résumés (moyenne, écart-type) des 📦 27.12, 🔮 27.13 et 📈 27.14 (4,03 et 0,98 ; 5,61 à 5,64 ; 4,50 et 0,95 ; 5,72 et 0,33 ; 3,94 et 0,73 ; 2,21 et 0,90), un modèle effondré sur un point ; la gaussienne du plan de centre (5, 5) et 39,3 %, l'anneau de 8 gaussiennes de rayon 2, la somme 16(4⁹ − 1)/3 et 75 % ; les distances de Fréchet 3,4 ; 119,3 à 123,2 ; 745 ; 638 ; 91 ; 1,7 ; 15,1 et 15,3 ; 50 000 images et 2 048 features ; MNIST, Fashion-MNIST, Inception, DINOv2 ; de workbookIA B7, la luminosité moyenne d'images, les parts 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 contre 0,2 (PSI 0,135, KL 0,0650 et 0,0704), les quartiles et les comptes 38/52/54/56, 96/62/30/12 et 120/56/24/0 sur 200 images, ε = 10⁻⁴ et 10⁻³, les seuils 0,1 et 0,25, les échantillons 0,31 ; 0,42 ; 0,47 ; 0,52 ; 0,58 et 0,22 ; 0,29 ; 0,35 ; 0,44 ; 0,61 (D = 0,4, p = 0,87), 10 000 valeurs décalées de 0,05 écart-type (D = 0,024, p = 0,008), 200 valeurs (D = 0,08, p = 0,55), 50 000 requêtes et p = 0,001, Bonferroni 0,05/m ; du checkpoint VI de workbookIA, la dérivation de D* (CP6.4) et la courbe d'un GAN 1D (lr 10⁻² et 10⁻⁵, CP6.7). Conventions : G[i, j] est le gain de la ligne (qui maximise) et ce que paie la colonne ; logarithme népérien, JS en nats (M06 la calculait en bits : 1 bit = ln 2 nats, et JS ≤ 1 bit) ; W_p désigne la distance et W_p^p le coût minimal ; F(x) = P(X ≤ x), F⁻¹(u) = inf{x : F(x) ≥ u} (M02a) ; `w2_gaussians_1d` prend des écarts-types. `distances` : NumPy et `math` permis, rien de `np.linalg` et aucune fonction de SciPy (`scipy.optimize.linprog` résout un jeu) ; `pure_strategy_values` (au lieu de `minimax_value` du plan : une valeur seule ne dit pas le coup, et le minimax d'un arbre est une autre chose) rend (maximin, minimax, ligne, colonne), les plus petits indices en cas d'égalité ; `mixed_strategy_value_2x2` rend les stratégies pures de `pure_strategy_values` quand il y a un point selle, sinon celles d'indifférence ; `descent_ascent_iterates` (ajoutée au plan : la brique du §4, calquée sur `richardson_iterates` ; son premier joueur minimise, comme dans MML (7.23), et sa docstring dit comment partir d'une matrice de gains G : A = −G, ou A = Gᵀ) ; `w2_gaussians_1d` prend des écarts-types et rend W₂, pas son carré : un contrat distinct du cas 1D de `frechet_distance` de workbookIA 27 (des covariances, et le carré d²) ; aucune fonction de W₁ empirique (27.11), de distance de Fréchet en dimension d (27.22), de KL, de JS (`mylearn` 6), de PSI ni de KS (B7.22 les écrit ou les appelle). Les exercices ne reprennent pas les exemples du stub ([[7, −4, 1], [−1, 5, 6]], [[1, 6, 2], [4, 5, 4], [0, 8, 3]], [[4, −2], [−1, 3]], [[−1, 2], [5, 6]], A = [[2]] avec η = 0,25, (10 ; 1 ; 2 ; 16) et (−1 ; 0,5 ; −1 ; 3,5)). MML : §7.2 relu (📖 M27.17 : l'inégalité minimax (7.23), sa preuve par (7.24), la dualité faible (7.27) lue comme un jeu où le joueur des multiplicateurs annonce en second ; M13b.21 l'a lu une première fois pour Lagrange) ; §7.3.1 (programmation linéaire) en option ; MML n'a ni stratégie mixte, ni Nash, ni Wasserstein. Référence libre possible, à vérifier en génération avant de la citer (annexes/ressources.md) : G. Peyré et M. Cuturi, Computational Optimal Transport, ch. 2 et 3. 14,4 h au lieu des 10 h prévues : la décision commune ajoute au plan les stratégies mixtes et von Neumann, les couplages et W_p, l'appariement trié, le biais d'une distance estimée, la dynamique d'un jeu bilinéaire et le § de la dérive (B7) ; la composition est au bas des fourchettes du §13 (15 ✏️/∂, 5 🔨/📦, un seul 🔬 et un seul 🔮) et les durées suivent les recalages de M21 et M22. **Durée** (session 66) : 18,7 h au lieu de 14,7 h (essentiel 12,8 h ; lecture de la fiche 165 min ; M27.10 f) et 📦 M27.23 c) retirées, 34 durées recalées après la re-résolution à l'aveugle, l'auteur des exercices et l'apprenant simulé).

<a id="m28"></a>
## M28 · Matrice de Gram, montée sur l'entrée et lois tronquées

**Partie** VI · **prépare** workbookIA 28 · **dossier** `chapitres/m28_gram_echantillonnage/` · **MML** — · **sessions de génération** 1

La matrice de Gram d'une famille de vecteurs, lue dans les deux sens (XXᵀ et XᵀX), divisée par le nombre d'échantillons pour devenir une matrice de moments d'ordre 2, et ce qu'elle coûte ; ce qu'elle détermine : toutes les longueurs et tous les angles, donc les distances, et la configuration à une isométrie près (double centrage, positions retrouvées à partir de distances) ; optimiser l'entrée d'une fonction à paramètres fixés : montée de gradient, pas normalisé, projection sur un pavé, coordonnées gelées, et ce que la montée trouve (un sommet du pavé, un vecteur propre) ; la variation totale d'une grille, forme quadratique d'un laplacien, son gradient et le lissage qu'elle produit, et les fréquences spatiales (période d'un motif, fréquence de Nyquist, gain d'un flou) ; les lois catégorielles modifiées : température sur des probabilités, top-k et top-p comme lois conditionnelles, le plus petit ensemble de masse donnée et le coût d'une troncature ; enfin une itération déterministe sur un ensemble fini, qui finit toujours par boucler. workbookIA 28 applique ces outils à la visualisation des réseaux, au transfert de style et à la génération de texte.

**Temps** : 13,6 h en parcours complet, 10,4 h en parcours essentiel (lecture 150 min, 16 flashcards).

**Objectifs**

- Calculer la matrice de Gram d'une famille de vecteurs dans les deux sens et la matrice des moments d'ordre 2, et choisir laquelle former selon son coût.
- Lire des distances dans une matrice de Gram, retrouver une matrice de Gram à partir de distances (double centrage), puis des positions à une isométrie près.
- Démontrer que deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie.
- Faire une montée de gradient projetée sur un pavé, avec un pas normalisé ou des coordonnées gelées, et prévoir où elle s'arrête pour une fonction linéaire, quadratique ou convexe.
- Écrire la variation totale d'une grille comme une forme quadratique, calculer son gradient et un pas de lissage, et comparer le carré et la valeur absolue.
- Lire la période et la fréquence d'un motif, situer la fréquence de Nyquist, et calculer ce qu'en font la variation totale et un flou.
- Tempérer une loi catégorielle, la tronquer par top-k ou top-p, et calculer le coût de la troncature en divergence KL.
- Trouver la prépériode et la période d'une itération sur un ensemble fini, et expliquer pourquoi le décodage glouton boucle.

**Sections de la fiche**

- §1 La matrice de Gram d'une famille de vecteurs : deux lectures, moments d'ordre 2 et coût
- §2 Ce que la matrice de Gram détermine : des distances aux positions, à une isométrie près
- §3 Optimiser l'entrée d'une fonction à paramètres fixés : montée projetée, pas normalisé, et ce que l'on trouve
- §4 La variation totale d'une grille et les fréquences spatiales
- §5 Modifier une loi catégorielle : température, top-k, top-p, et le coût d'une troncature
- §6 Une itération déterministe sur un ensemble fini finit par boucler

**Notions enseignées** : matrice de Gram d'une famille de vecteurs : XXᵀ (produits scalaires des lignes) et XᵀX (des colonnes), mêmes valeurs propres non nulles, symétrique semi-définie positive (rappels de M09a, M12c, M12d, M13b) ; coût n²d contre d²n : former la plus petite · matrice des moments d'ordre 2 : XXᵀ/N quand les N colonnes sont des échantillons ; centrer donne la covariance · distances et matrice de Gram : ‖xᵢ − xⱼ‖² = G_ii + G_jj − 2G_ij ; double centrage G = −½ J D⁽²⁾ J (positionnement multidimensionnel classique) ; une matrice de distances est euclidienne si et seulement si son double centrage est semi-défini positif (énoncé) · une matrice de Gram détermine la configuration à une isométrie près : invariance par une transformation orthogonale de l'espace (énoncée), réciproque démontrée ; des positions de matrice de Gram donnée par le théorème spectral (pour une Gram centrée, les scores d'une ACP) · optimiser l'entrée d'une fonction à paramètres fixés : montée de gradient, pas normalisé (g/‖g‖, par une moyenne quadratique, par le signe) et son invariance quand la fonction est multipliée par c > 0, montée projetée sur un pavé, coordonnées gelées (le gradient projeté sur un sous-espace de coordonnées) · ce que trouve la montée : une forme linéaire maximisée sur une boule ou sur un pavé, une forme quadratique sur la sphère (vecteur propre dominant ; la montée renormalisée est la méthode de la puissance de I + 2ηA pour f = xᵀAx), une fonction convexe sur un pavé (un sommet, des coordonnées saturées) · variation totale d'une grille : forme quadratique xᵀLx du laplacien de la grille (symétrique, semi-défini positif, de noyau les constantes), gradient 2Lx, un pas de descente est un lissage (une diffusion) et son pas critique ; le carré préfère les rampes, la valeur absolue garde les bords · fréquences spatiales : motif périodique, fréquence, période, fréquence de Nyquist (le damier), repliement ; un motif périodique est un vecteur propre du laplacien circulaire, sa variation totale rapportée à son énergie vaut 4 sin²(ω/2) par direction ; gain (1 + 2 cos ω)/3 d'une moyenne mobile : un filtre passe-bas · température sur des probabilités : p^{1/T} renormalisé, une loi de Boltzmann d'énergies −ln pᵢ (rappel de M17), limites T → 0 et T → ∞, issues de probabilité nulle gardées à 0 ; l'entropie croît avec T (énoncé) ; le tirage catégoriel (rappel de M02b) · top-k et top-p : lois conditionnelles sur un ensemble d'issues (M03) ; le plus petit ensemble de masse au moins p est fait des issues les plus probables ; la température garde l'ensemble du top-k, et refroidir fait rétrécir celui du top-p · coût d'une troncature : KL(p_S ‖ p) = −ln P(S) et ½‖p_S − p‖₁ = 1 − P(S) ; KL(p ‖ p_S) infinie ; la « distance en variation totale » entre deux lois n'est pas la variation totale d'une grille · itération déterministe sur un ensemble fini : principe des tiroirs, prépériode μ et période λ, μ + λ ≤ |E| ; un générateur glouton à contexte fini boucle ; détection par le lièvre et la tortue (Floyd, aperçu)

**Prérequis** : division euclidienne et reste (`//`, `%`) (R0) · cosinus, radians, périodicité (R9) · loi catégorielle, tirage catégoriel par inversion (M02b) · matrice de covariance, avec le facteur 1/n (M02c) · loi conditionnelle (M03) · convexité d'une fonction d'une variable, log-sum-exp (M05a) · gradient, montée et descente (M05b) · entropie, divergence KL, KL infinie quand le support manque (M06) · produit scalaire, normes, Cauchy-Schwarz, similarité cosinus (M07) · transposée, XᵀX et XXᵀ (M09a) · ridge : un terme de régularisation pondéré (M09b) · fonctions convexes de plusieurs variables (M10) · application linéaire, image, dimension (M12a) · bases orthonormées, matrices orthogonales, Gram-Schmidt, projection sur un sous-espace (M12b) · théorème spectral, quotient de Rayleigh, méthode de la puissance, matrices semi-définies positives, matrice de Gram XᵀX (M12c) · valeurs singulières, AᵀA et AAᵀ, approximation de rang faible, ACP quand n < p (M12d) · noyau polynomial et matrice de Gram d'un noyau (M13b) · principe des tiroirs (M16) · loi de Boltzmann et ses limites en température (M17) · gradient par rapport à toutes les entrées en un passage inverse (M18) · projection sur une boule et sur un pavé, pas critique 2/λmax (M19) · matrice de centrage (M20) · laplacien discret, moyenne mobile, convolutions circulaires, forme linéaire sur une boule (M21) · rayon spectral majoré par une norme induite (M22) · formules de soustraction sin(γ − ψ) et cos(γ − ψ), d'où cos(a − b) + cos(a + b) = 2 cos a cos b (M25a)

**mymath** : `sampling.py` (signatures figées) : `points_from_gram`, `temper`, `smallest_mass_set`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 28.3 ∂ Mélanger les positions ne change pas la matrice de Gram · 28.5 ∂ Le gradient de la loss de style · 28.2 ✏️ Une matrice de Gram à la main · 28.4 ✏️ Losses de contenu, de style et de variation totale sur un mini-exemple · 28.7 🧮 Vocabulaire de mots et taille de la couche de sortie d'un LSTM · 28.8 🗣️ Pourquoi la matrice de Gram capture le style, en cinq lignes · 28.10 📄 Lire Gatys, Ecker et Bethge (2015), « A Neural Algorithm of Artistic Style » · 28.12 🔮 Prédire l'image qui excite un filtre précoce, puis un filtre profond · 28.13 📦 Visualiser un filtre d'un réseau ImageNet : la montée de gradient du ch. 21 passe à l'échelle · 28.15 🔬 Régulariser la visualisation : décalages, flou, octaves · 28.16 📦 Deep dream sur une photo libre · 28.17 🔬 Choisir couches et poids, ne rêver que dans une zone · 28.18 📦 La matrice de Gram en PyTorch, vérifiée contre NumPy · 28.24 🔬 Poids contenu/style, variation totale et image de départ · 28.25 🔬 Au-delà de Gram : moyennes et écarts-types des canaux · 28.28 🔬 Glouton, température, top-k ou top-p : répétitions et diversité · 28.Q2 🧠 Montée de gradient sur l'entrée, poids gelés · 28.Q7 🧠 Ce que la matrice de Gram retient et ce qu'elle oublie · 28.Q10 🧠 Générer du texte mot à mot : ce qu'implique « le mot le plus probable » · 28.R2 🔁 Mélange de contenu contre mélange de représentations · 28.E2 💼 Expliquer le transfert de style neuronal et la matrice de Gram · 28.E3 💼 Quelles stratégies de décodage pour générer du texte ? · B4.Q5 🧠 Glouton, température, top-p : lequel pour extraire une date, lequel pour écrire un poème ? · B4.13 🔮 Prédire : dix générations du même prompt à température 0, 0,7 et 1,5

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M28.Q1 | 🧠 | Matrice de Gram : XXᵀ ou XᵀX, laquelle former, sa diagonale, et les distances qu'on y lit | ★ | 5 | §1 §2 | C, E | manuel | — |
| M28.Q2 | 🧠 | Monter sur l'entrée : pas normalisé, projection sur un pavé, coordonnées gelées, point d'arrivée | ★ | 6 | §3 | C, E | manuel | — |
| M28.Q3 | 🧠 | Variation totale et fréquences spatiales : quel motif coûte le plus, lequel traverse un flou ? | ★ | 6 | §4 | C, E | manuel | — |
| M28.Q4 | 🧠 | Température, top-k et top-p : ce qui change l'ensemble gardé, ce qui ne change que les probabilités | ★ | 4 | §5 | C, E | manuel | — |
| M28.Q5 | 🧠 | Une itération sur un ensemble fini : prépériode, période, et ce qui empêche de boucler | ★ | 5 | §6 | C, E | manuel | — |
| M28.R1 | 🔁 | Le quotient de Rayleigh et la méthode de la puissance (M12c) | ★ | 8 | §3 | C, E | manuel | — |
| M28.R2 | 🔁 | Le laplacien discret et la moyenne mobile d'un signal (M21) | ★ | 7 | §4 | C, E | manuel | — |
| M28.R3 | 🔁 | La loi de Boltzmann et ses limites en température (M17) | ★ | 5 | §5 | C, E | manuel | — |
| M28.1 | ✏️ | Quatre points du plan : leur matrice de Gram 4 × 4, leur matrice des moments d'ordre 2, et les distances lues dans la Gram | ★★ | 30 | §1 | C, E | wbm | — |
| M28.2 | ✏️ | Quatre villes aux sommets d'un losange : le double centrage des carrés des distances, puis une carte à une isométrie près | ★★ | 35 | §2 | C, E | wbm | — |
| M28.3 | ✏️ | Régler quatre émetteurs entre 0 et 1 : le maximum d'une réponse linéaire sur la boule et sur le pavé, d'une énergie quadratique sur la sphère, et deux pas de montée projetée | ★★ | 30 | §3 | C, E | wbm | — |
| M28.4 | ✏️ | Les températures le long d'une barre : la variation totale xᵀLx, son gradient 2Lx, un pas de lissage, et une marche étalée sur n pas, au carré ou en valeur absolue | ★★ | 30 | §4 | C, E | wbm | — |
| M28.5 | ✏️ | Des étoffes rayées : période, fréquence, fréquence de Nyquist, repliement, variation totale rapportée à l'énergie 4 sin²(ω/2), et gain d'une moyenne mobile | ★★ | 30 | §4 | C, E | wbm | — |
| M28.6 | ✏️ | La prévision d'un météorologue en six catégories : la refroidir, garder les trois plus probables, garder le plus petit ensemble de masse donnée, et le coût de chaque troncature | ★★ | 35 | §5 | C, E | wbm | — |
| M28.7 | ✏️ | Les décimales de a/n et l'itération x ↦ x² + c modulo n : prépériode et période à la main, et la borne du principe des tiroirs | ★ | 20 | §6 | C, E | wbm | — |
| M28.8 | ∂ | Deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie | ★★★ | 45 | §2 | C | manuel | — |
| M28.9 | ∂ | Le maximum d'une fonction convexe sur un pavé est atteint en un sommet | ★★ | 20 | §3 | C | manuel | — |
| M28.10 | ∂ | Les issues les plus probables, prises jusqu'à atteindre la masse p, forment un plus petit ensemble de masse au moins p, et la loi tronquée est à −ln P(S) de la loi de départ en divergence KL | ★★ | 30 | §5 | C, E | manuel | — |
| M28.11 | 🔗 | Pont : diviser des scores par T avant la softmax, ou élever les probabilités à la puissance 1/T, la même loi ; et le même top-k | ★ | 25 | §5 | C, E | wbm | — |
| M28.12 | 🗣️ | Expliquer avec une structure de barres rigides ce que la matrice de Gram d'une famille de vecteurs fixe, et ce qu'elle laisse libre | ★ | 10 | §2 | C, E | manuel | — |
| M28.E1 | 💼 | « Que perd-on, en divergence KL, à ne garder que les issues les plus probables d'une loi avant de tirer ? » | ★ | 10 | §5 | C | manuel | — |
| M28.13 | 🔨 | Une configuration de points de matrice de Gram donnée, par le théorème spectral · `points_from_gram` | ★★ | 40 | §2 | C | pytest | — |
| M28.14 | 🔨 | Tempérer une loi donnée par ses probabilités, et le plus petit ensemble de masse donnée · `temper, smallest_mass_set` | ★★ | 35 | §5 | C, E | pytest | — |
| M28.15 | 🔮 | Prédire ce que deviennent un pas η∇f et un pas normalisé quand la fonction est multipliée par 1 000, puis vérifier | ★ | 20 | §3 | C, E | wbm | — |
| M28.16 | 🎨 | Des motifs rayés de fréquence croissante jusqu'au damier : leur variation totale, et ce qu'en laissent un flou 3 × 3 et dix pas de descente sur la variation totale | ★ | 40 | §4 | C, E | manuel | — |
| M28.17 | 🐛 | Chasse à l'erreur : un double centrage fait sur les distances au lieu de leurs carrés, une montée qui coupe le gradient au lieu du point, une prépériode comptée dans la période | ★ | 25 | §2 §3 §6 | C, E | wbm | — |
| M28.18 | 🛠️ | Un test de propriété : la configuration rendue redonne la matrice de Gram et les distances, pour des points tirés au hasard | ★ | 30 | §2 | C | manuel | M28.13 |
| M28.19 | 🏆 | Défi : redessiner la carte de 30 villes quand un quart des distances manquent, à moins de 1 km en moyenne après alignement | ★★★ | 45 | §2 | C | wbm | M28.13 |

*Notes* : Frontières : les ∂ 28.3 (une permutation des positions, puis une matrice orthogonale, ne change pas FFᵀ ; un seul canal permuté la change ; C G_ii = μ² + σ² et la moyenne qu'elle ne fixe pas ; les tables d'ordre 3) et 28.5 (le gradient 4(FFᵀ − S)F de la loss de style), ✏️ 28.2 (une Gram 3 × 4 normalisée par CHW, cosinus, somme, retournement), ✏️ 28.4 (losses de contenu, de style et de variation totale sur un mini-exemple, `mse_loss`, poids α, β et λ), 🧮 28.7 (LSTM mot à mot, Zipf, perplexité), 🗣️ 28.8, 📄 28.10 (Gatys), 🔮 28.12 et 🔬 28.15 (périodes de filtres appris, part des hautes fréquences, flou, décalages, octaves), 📦 28.13 (pixels saturés d'une visualisation), 📦 28.16 (le deep dream : un gradient normalisé, indépendant de l'échelle des activations), 🔬 28.17 (couches, poids, un masque de zone), 📦 28.18 (Gram et variation totale en PyTorch contre `einsum` et `np.diff`), 🔬 28.24 (poids contenu/style et leur frontière), 🔬 28.25 (moyennes et écarts-types des canaux), 🔬 28.28 (glouton, température, top-k et top-p sur Verne, `pick_28`, répétitions), les quiz 28.Q2, 28.Q7 et 28.Q10, le rappel 28.R2, les entretiens 28.E2 et 28.E3, et, de workbookIA B4 (après M28), B4.Q5 et B4.13 (quelle stratégie de décodage pour quelle tâche ; dix générations à trois températures). M28 enseigne les outils hors réseau : nuages de points, villes et capteurs pour la matrice de Gram ; émetteurs réglables, énergies quadratiques et modes de vibration pour la montée ; barres chauffées, plaques, étoffes rayées et signaux échantillonnés pour la variation totale et les fréquences ; prévisions météorologiques, diagnostics et identifications d'espèces pour les lois tronquées ; décimales d'une fraction, itérations modulo n et automates pour les boucles ; jamais une carte d'activation, un filtre appris, une image d'un dataset, un pixel permuté, un « style », un logit de mot ni un texte généré. La matrice de Gram : les points sont les lignes de X (comme M13b) et G = XXᵀ ; la normalisation est celle d'une matrice de moments, 1/N pour N échantillons, jamais 1/(CHW) ni une forme (C, H, W) ; la double lecture XXᵀ/XᵀX, la symétrie et la positivité sont des rappels (M09a, M12c.17, M12d.12, M13b), et aucune fonction ne calcule une Gram (c'est `polynomial_kernel(X, X, 1, 0)` de M13b, et `gram_matrix_18` de 28.18). L'invariance par une transformation orthogonale de l'espace (X ↦ XRᵀ, tourner le repère) est énoncée en une ligne et utilisée ; la réciproque est démontrée (∂ M28.8 : une application linéaire définie sur l'espace engendré par les points, isométrique, prolongée par Gram-Schmidt), avec la construction par le théorème spectral (🔨 M28.13) ; aucun exercice ne permute les colonnes de X (positions ou échantillons), ne demande si permuter une seule ligne change G, ni ne relie la diagonale à μ² + σ² ou à une moyenne qu'elle ne fixe pas (∂ 28.3.4-5), et M28.Q1 lit la diagonale comme les carrés des normes des points, jamais comme une moyenne de carrés (28.Q7 d) ; pas de statistiques d'ordre 3 ; l'écart de Frobenius entre les matrices de moments de deux nuages, égal à une MMD de noyau (xᵀy)² (M13b), est au plus une remarque de la fiche, sans loss ni « style ». Aucun gradient d'une fonction de XXᵀ ou de XᵀX (ni ‖XXᵀ − S‖²_F, ni ‖XᵀX − I‖², paraphrase transposée de ∂ 28.5) : le seul gradient matriciel du chapitre est celui de la variation totale, 2Lx. Le double centrage est −½ J D⁽²⁾ J sur les **carrés** des distances, avec la matrice de centrage J de M20 ; ✏️ M28.2 prend quatre villes aux sommets d'un losange (une matrice de Gram à blocs, diagonalisable à la main), et ✏️ M28.3 une énergie quadratique de matrice à blocs 2 × 2 en dimension 4, diagonalisable à la main : les deux tiennent ainsi en 25 minutes. La montée sur l'entrée : f(x ; θ) à θ fixé, sur des fonctions écrites (réponses linéaires et quadratiques d'émetteurs réglables entre 0 et 1, énergies) ; le pas normalisé et son invariance quand f est multipliée par c > 0 sont démontrés en général, sans deep dream, octaves, masque d'image ni « activation » ; la montée projetée est celle de M19 §8 (`np.clip`) ; un gradient restreint à des coordonnées libres est la projection orthogonale de M12b, sans zone d'image (28.17) ; le maximum d'une fonction convexe sur un pavé (un sommet, ∂ M28.9) explique les coordonnées saturées, sans les pourcentages de pixels de 28.13 ; une moyenne de carrés de réponses linéaires est la forme quadratique xᵀAx avec A = WᵀW/m, et la montée renormalisée sur elle est la méthode de la puissance de I + 2ηA (le gradient vaut 2Ax) (M12c) ; aucun vrai ou faux « monter sur f, c'est descendre sur −f » ni « les paramètres sont gelés, le gradient par rapport à l'entrée existe quand même » (28.Q2 b et e). La variation totale : sur une grille de mesures (somme des carrés des différences entre voisins horizontaux et verticaux, comme workbookIA) et sur un signal, écrite xᵀLx avec le laplacien de la grille ((Lx)_ij = 4x_ij − la somme des voisins à l'intérieur : le pochoir de M21 au signe près), de gradient 2Lx ; un pas de descente est un pas de diffusion, de pas critique 1/λmax(L) (M19) ; la valeur absolue (variation totale de Rudin, Osher et Fatemi, nommée sans date) garde les bords, le carré préfère les rampes (h²/n contre h pour une marche étalée sur n pas) ; jamais la grille 3 × 3 de 28.4, une puissance 1,25, une image de scikit-learn ni une loss totale pondérée ; débruiter un signal par min ‖x − y‖² + λxᵀLx, soit (I + λL)x = y, est une remarque (gain 1/(1 + 4λ sin²(ω/2)) par fréquence, un compromis réglé par λ comme la ridge de M09b), sans courbe contenu/style. Les fréquences spatiales comblent une lacune (ni M21 ni R9 ne les enseignent ; workbookIA 28 s'en sert dans ses outils fournis et en 28.12, 28.14, 28.15 et 28.24) : un motif cos(2π(f₁i + f₂j) + φ), sa fréquence en cycles par case, sa période 1/√(f₁² + f₂²) dans la direction (f₁, f₂), la fréquence de Nyquist ½ (le damier) et le repliement (f et 1 − f donnent les mêmes échantillons) ; un motif périodique est un vecteur propre du laplacien circulaire (∂ M21.13 : les matrices circulantes), de valeur propre 4 sin²(ω/2) en dimension 1 (ω = 2πf) et la somme des deux en dimension 2, d'où sa variation totale rapportée à son énergie, un quotient de Rayleigh (M12c), maximale pour le damier ; la moyenne mobile de trois cases multiplie un motif par (1 + 2 cos ω)/3 et efface la période 3 ; sans transformée de Fourier discrète (un encadré 💻 au plus), sans « part de la variance au-dessus de la moitié de la fréquence de Nyquist » ni période dominante d'une image (les outils `high_freq_share` et `dominant_period` du notebook de workbookIA 28). Les lois catégorielles : données par leurs probabilités, jamais par des logits de mots ; la température sur des probabilités est la loi de Boltzmann des énergies −ln pᵢ (M17), les issues de probabilité nulle le restent ; le 🔗 M28.11 montre que diviser des scores par T avant la softmax donne la même loi, sur les scores d'un classifieur d'espèces (ni mots ni vocabulaire), sans refaire 17.6, 22.5 ni 26.5 ; la croissance de l'entropie avec T (dH/dT = Var(E)/T³) est énoncée et constatée, sa démonstration est l'un des sujets de CP6.8 ; top-k et top-p sont des lois conditionnelles (M03) sur l'ensemble gardé, le top-p étant le plus petit ensemble de masse au moins p (∂ M28.10 : un argument d'échange, puis KL(p_S ‖ p) = −ln P(S) et ½‖p_S − p‖₁ = 1 − P(S)) ; la température ne change pas l'ensemble du top-k (elle garde l'ordre) et, en refroidissant, la masse des j issues les plus probables croît, donc l'ensemble du top-p rétrécit ; un encadré ⚠️ distingue la variation totale d'une grille et la « distance en variation totale » ½‖p − q‖₁ entre deux lois ; le tirage lui-même est un rappel de M02b. Les boucles : une suite u_{t+1} = f(u_t) sur un ensemble de N éléments devient périodique, avec μ + λ ≤ N (principe des tiroirs de M16), démontré dans la fiche et appliqué aux décimales de a/n et à x ↦ x² + c modulo n (✏️ M28.7) ; un générateur glouton dont l'état est fait des w derniers symboles d'un alphabet de V symboles a au plus V^w états : il boucle ; un modèle à état continu (une cellule récurrente) n'entre pas dans le théorème, et la fiche le dit ; l'algorithme du lièvre et de la tortue (Floyd) est un encadré 💻, sans fonction `mymath` ; ni phrase générée, ni « de la de la », ni part de trigrammes répétés (28.28). Le 🐛 M28.17 n'a aucune des erreurs du corrigé de 28.28 (renormaliser avant de couper, trier dans le mauvais sens, un mot de moins que le seuil) ni de 28.21 (normalisation oubliée, Gram non normalisée, optimiseur sur les poids, bornes de `clamp_`). Évités (règle de partage) : les matrices F = [[3, 1], [0, 2]] (Gram [[2,5 ; 0,5], [0,5 ; 1]]), [[1, 0, 2, 1], [0, 3, 1, 1], [2, 0, 4, 2]] (FFᵀ [[6, 3, 12], [3, 11, 6], [12, 6, 24]], 0,917, 6,917, 0,369), [[2, 0, 1, 1], [1, 1, 0, 2]] (0,75 ; 0,5 ; 0,667), [[1, 0], [1, 0]] et [[1, 0], [0, 1]], [[1, 1], [0, 2]], [[2, 0], [0, 2]], [[1, 0], [1, 1]], et, du checkpoint VI, [[1, 0, 2, 1], [0, 1, 1, 0], [2, 1, 0, 1]] ([[6, 2, 3], [2, 2, 1], [3, 1, 6]]) ; les canaux (1, 1) et (0, √2) ; les vecteurs (1, 2, 0, 1), (1, 0, 1, 1) et (0, 1, 1, 1) ; la grille [[0, 1, 0], [1, 1, 1], [0, 1, 3]] et ses variations totales 14 et 10 ; α = 0,025, β = 1, λ = 10⁻⁴, 40, 0,8764, 12, 0,9375 (28.4) ; CHW = 401 408 et 1,6 × 10¹¹, 10,90, 512³ et 134 millions ; les tailles de VGG16 (3 211 264, 401 408, 262 144, 784, 131 328) et ses 224, 28 et 14 pixels, SqueezeNet ; 15,5 et 0,35 milliard de MAC, 138,4 M, 14,7 M, 123,6 M, 553 Mo ; la loi (0,5 ; 0,2 ; 0,15 ; 0,1 ; 0,05) avec p = 0,8, son cumul 0,85 et (0,588 ; 0,235 ; 0,176) ; les logits (2 ; 1 ; 0,5 ; 3 ; −1) et leur softmax, (3,1 ; 2,6 ; 2,2 ; 1,6 ; 1,5 ; 1,1 ; 0,8 ; 0,5 ; 0,2 ; −0,3), (1, 2, 3), (1, 5, 2), (3 ; 1 ; 0,5) de 22.5 et les scores 0,6 / 0,3 / 0,1 de 17.Q12 ; les seuils de top-p 0,75, 0,8, 0,9 et 0,01, les k = 1, 2 et 20, les températures 0,5 ; 0,7 ; 1,2 ; 1,5 et 2 (les ✏️ prennent T = 1/3, 1/4, 3 ou 4, des puissances exactes), 6 000 tirages et la tolérance 0,03 ; (1, 2, 3, 1, 2, 3, 1) et 0,4 ; 10 300 mots, 427 000 mots, 2 × 128 cellules, les perplexités 150, 439 et 113, la formule de Zipf ; la moyenne (0,485 ; 0,456 ; 0,406) et l'écart-type (0,229 ; 0,224 ; 0,225) d'ImageNet ; les filtres 5, 17 et 100, les périodes de 2, 4, 8, 13 et 16 pixels, les parts de hautes fréquences (0,75 pour un bruit blanc ; 71, 76, 83 et 91 %), les pixels saturés (≈ 50 %, 37 à 45 %, 98 %) ; l'interpolation de (0, 2) et (4, −2) à t = 0,25 ; Verne, Holmes, « Phileas Fogg », « le capitaine… », « de la de la », la grenouille, la pagode, la fleur, les images `china` et `flower`, les tableaux et leurs peintres ; et, de ce dépôt, la loi (0,1 ; 0,4 ; 0,35 ; 0,15) de M02b, les trois niveaux (0 ; 0,5 ; 2) et p = (0,5 ; 0,3 ; 0,2) de M17 ; la fiche ne reprend ni le losange de ✏️ M28.2 ni les exemples du stub. Conventions : points en lignes de X ; ω = 2πf en radians par case ; la variation totale est la somme des carrés (comme workbookIA), la version en valeur absolue est nommée chaque fois ; une loi est un vecteur de probabilités ; indices à partir de 0 ; entre deux probabilités égales, le plus petit indice d'abord (un tri stable). `sampling` : NumPy permis, de `np.linalg` seulement `eigh` (dans `points_from_gram`), aucune fonction de SciPy (`scipy.special.softmax` et `logsumexp` donneraient `temper`) ni de scikit-learn ; les fonctions prennent des probabilités (jamais des logits) et ne tirent rien : `temper` (T = 0 et T = ∞ compris, zéros gardés) a un autre contrat que `temperature_softmax` (logits, T > 0) de workbookIA 22, `smallest_mass_set` rend un ensemble d'indices, pas un tirage ni une loi prête à tirer (`sample_from_logits` de workbookIA 22, `pick_28` de 28.28, `sample_categorical` de workbookIA 2) ; la docstring ne donne ni la tranche du top-k ni la renormalisation suivie d'un tirage (l'indice 3 de 28.28), et aucun exercice ni la fiche ne les écrivent en code ; `smallest_mass_set` rend exactement l'ensemble que garde la branche top-p de `pick_28` (à 1e-9 près) : c'est la brique mathématique (∂ M28.10), assumée ; aucune fonction de matrice de Gram, de loss de style, de variation totale (`gram_matrix_18`, `tv_loss_18`) ni de période. Pas de MML : le livre ne traite ni la variation totale, ni les fréquences, ni les troncatures, ni les itérations sur un ensemble fini, et AAᵀ, AᵀA et la matrice de Gram d'un noyau ont été lus en M12d (§4.5) et M13b (§12.4) ; donc pas de 📖. COMPOSITION : prévu court (6 h au plan, 8 h visées en session 60), porté à 9,8 h par la lacune des fréquences spatiales, la réciproque de la matrice de Gram et des durées réalistes (relectures de M21 et M22) : la composition d'un chapitre court est gardée (5 quiz, 7 ✏️ et 3 ∂, 2 🔨, un 🔮 et un 🎨 sans 🔬, 16 flashcards). Parcours essentiel : les ∂ de la Gram et de la montée (M28.8, M28.9), le 💼, le 🔨 de la Gram, son 🛠️ et le 🏆 hors parcours ; ∂ M28.10 (le top-p) y est. **Durée** (session 67) : 13,6 h au lieu de 9,8 h (essentiel 10,4 h ; lecture de la fiche 150 min au lieu de 100 ; quatre allègements, M28.2 e), M28.4 d), M28.14 d) et la boucle du 🛠️ M28.18 fournie ; 24 durées recalées après la re-résolution à l'aveugle, l'auteur des exercices et l'apprenant simulé). Titres de ✏️ M28.6 (les trois plus probables) et de ∂ M28.10 (un plus petit ensemble) changés en session 67.

<a id="cp6"></a>
## CP6 · Examen blanc de la partie VI

**Partie** VI · **prépare** — · **dossier** `checkpoints/partie_6/` · **MML** — · **sessions de génération** 1

Le bilan de la partie VI (M25a, M25b, M26, M27 et M28), juste avant le checkpoint VI de workbookIA : un examen blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.

**Temps** : 3,1 h en parcours complet, 3,1 h en parcours essentiel (lecture 15 min, 0 flashcards).

**Objectifs**

- Vérifier en temps limité que les notions de la partie VI sont acquises.
- Construire ta propre synthèse de la partie VI.

**Sections de la fiche**

- §1 Examen blanc
- §2 Synthèse

**Notions enseignées** : révision de la partie VI

**Prérequis** : toute la partie VI (M28)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 25.5 ∂ Dériver à travers un tirage : l'astuce de reparamétrisation · 25.6 ✏️ Où tombent les tirages d'une gaussienne en grande dimension · 25.7 ∂ La divergence KL entre N(μ, σ²) et N(0, 1) · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé) · 25.11 🗣️ Le VAE expliqué à un ami en cinq lignes · 25.13 📄 Lire Kingma et Welling (2013), « Auto-Encoding Variational Bayes » · 25.20 🔨 Interpoler entre deux codes : linéaire et sphérique · 25.23 🔬 L'autoencodeur linéaire face à l'ACP de scikit-learn · 25.28 🔨 La reparamétrisation en NumPy : passe avant et passe arrière · 25.29 🔨 Divergence KL gaussienne et son gradient · 25.30 📦 Un VAE en PyTorch : reconstruction + KL · 25.31 🔮 Prédire : décoder des tirages N(0, I) avec un AE puis avec un VAE · 25.32 🔬 Un VAE est stochastique : sorties répétées, bruit relatif, interpolations · 25.33 🎨 Reproduire le nuage latent d'un VAE 2D et la grille −3…3 (fig. 25.67-25.68) · 25.34 📈 Diagnostiquer des courbes reconstruction/KL (effondrement du posterior) · 25.36 🔬 β-VAE : échanger la netteté contre la régularité · 25.38 🔨 Un VAE entièrement en NumPy avec mylearn · 25.Q9 🧠 Autoencodeur linéaire et ACP · 25.Q12 🧠 Les trois exigences d'un VAE et l'astuce de reparamétrisation · 25.R3 🔁 La divergence KL, ce que mesure le terme de régularisation du VAE · 25.E1 💼 Autoencodeur ou ACP : quand préférer l'un ou l'autre ? · 25.E2 💼 Pourquoi un VAE sait-il générer et pas un autoencodeur classique ? · 25.E3 💼 Expliquer l'astuce de reparamétrisation · 26.1 ✏️ Retours total et actualisé d'une partie de six coups · 26.3 ✏️ Une mise à jour de Q-learning à la main · 26.4 ✏️ La même transition vue par SARSA · 26.5 ✏️ Probabilités d'action : ε-greedy (standard et version du livre) et softmax · 26.6 ✏️ Regarder la valeur remonter une chaîne d'états · 26.7 ∂ Somme géométrique et horizon effectif de γ · 26.8 ∂ Équation de Bellman : le point fixe que vise le Q-learning · 26.9 🧮 Mémoire d'une table Q : morpion 4×4, 5×5 et Go · 26.12 📄 Lire Mnih et coll. (2015), « Human-level control through deep reinforcement learning » · 26.14 🔨 Retours actualisés et retours à venir · 26.26 🔨 Itération sur les valeurs : la référence quand le modèle est connu · 26.Q6 🧠 Retour total, retour actualisé et rôle de γ · 26.Q8 🧠 La mise à jour du Q-learning : α, γ et la valeur de l'état suivant · 26.Q9 🧠 ε-greedy ou softmax : vrai ou faux · 26.Q10 🧠 Table initialisée à zéro : comment la valeur remonte et converge · 26.R3 🔁 Bandit à bras multiples, ε-greedy et UCB · 26.E2 💼 À quoi sert le facteur d'actualisation γ ? · 26.E4 💼 Pourquoi DQN utilise-t-il une mémoire de rejeu et un réseau cible ? · 27.2 ✏️ Valeur minimax d'une petite matrice de gains · 27.3 ✏️ Losses BCE du discriminateur et du générateur à partir de sorties données · 27.4 ✏️ À l'équilibre, la loss vaut ln 2 et non 0,5 · 27.5 ∂ Le discriminateur optimal D* = p_data / (p_data + p_g) · 27.6 ∂ Pourquoi log(1 − D(G(z))) sature et pas −log D(G(z)) · 27.7 🧮 Croissance progressive : où passe le temps de calcul ? · 27.10 📄 Lire Goodfellow et coll. (2014), « Generative Adversarial Nets » · 27.11 🔨 Distance de Wasserstein 1D entre deux échantillons · 27.13 🔮 Prédire la moyenne et l'écart-type générés au fil des epochs · 27.14 📈 Lire les courbes d'un GAN : losses, D(x) et D(G(z)) · 27.18 🔬 Loss saturante ou non saturante : la dynamique du début · 27.22 🔨 Distance de Fréchet entre deux gaussiennes (la formule du FID) · 27.23 📦 Évaluer un générateur : distance de Fréchet sur les features d'un classifieur · 27.Q5 🧠 Coopératifs ou antagonistes : somme nulle, minimax et équilibre de Nash · 27.E1 💼 Expliquer l'entraînement d'un GAN et sa loss · 27.E4 💼 Comment évaluer un modèle génératif (FID et ses limites) ? · 27.E5 💼 Pourquoi l'entraînement des GAN est-il instable ? · 28.2 ✏️ Une matrice de Gram à la main · 28.3 ∂ Mélanger les positions ne change pas la matrice de Gram · 28.4 ✏️ Losses de contenu, de style et de variation totale sur un mini-exemple · 28.5 ∂ Le gradient de la loss de style · 28.7 🧮 Vocabulaire de mots et taille de la couche de sortie d'un LSTM · 28.8 🗣️ Pourquoi la matrice de Gram capture le style, en cinq lignes · 28.10 📄 Lire Gatys, Ecker et Bethge (2015), « A Neural Algorithm of Artistic Style » · 28.12 🔮 Prédire l'image qui excite un filtre précoce, puis un filtre profond · 28.13 📦 Visualiser un filtre d'un réseau ImageNet : la montée de gradient du ch. 21 passe à l'échelle · 28.15 🔬 Régulariser la visualisation : décalages, flou, octaves · 28.16 📦 Deep dream sur une photo libre · 28.17 🔬 Choisir couches et poids, ne rêver que dans une zone · 28.18 📦 La matrice de Gram en PyTorch, vérifiée contre NumPy · 28.24 🔬 Poids contenu/style, variation totale et image de départ · 28.25 🔬 Au-delà de Gram : moyennes et écarts-types des canaux · 28.28 🔬 Glouton, température, top-k ou top-p : répétitions et diversité · 28.Q2 🧠 Montée de gradient sur l'entrée, poids gelés · 28.Q7 🧠 Ce que la matrice de Gram retient et ce qu'elle oublie · 28.Q10 🧠 Générer du texte mot à mot : ce qu'implique « le mot le plus probable » · 28.R2 🔁 Mélange de contenu contre mélange de représentations · 28.E2 💼 Expliquer le transfert de style neuronal et la matrice de Gram · 28.E3 💼 Quelles stratégies de décodage pour générer du texte ? · B4.Q5 🧠 Glouton, température, top-p : lequel pour extraire une date, lequel pour écrire un poème ? · B4.13 🔮 Prédire : dix générations du même prompt à température 0, 0,7 et 1,5 · B5.6 ∂ Forme fermée : deux pas de bruit gaussien n'en font qu'un, d'où q(x_t | x_0) · B7.4 ✏️ Indice de stabilité de population (PSI) à la main sur quatre intervalles · B7.22 📈 Surveiller la dérive : PSI et test KS sur des images assombries ou bruitées, quand alerter ? · B7.Q11 🧠 Écart entraînement-production et dérive des données : vrai ou faux · B7.E4 💼 Comment surveilles-tu un modèle en production, et que fais-tu en cas de dérive ? · B8.Q4 🧠 Double DQN : d'où vient la surestimation des valeurs Q ? · B8.Q7 🧠 Avantage, erreur TD et GAE : ce que règle λ · B8.1 ✏️ Cible DQN à la main : état terminal, puis cible Double DQN · B8.4 ✏️ GAE à la main sur quatre pas, pour λ = 0, 0,95 et 1

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| CP6.Q1 | 🧠 | Dix affirmations sur la partie VI, deux par chapitre : vrai ou faux | ★ | 10 | §1 | C, E | manuel | — |
| CP6.1 | ✏️ | Un vecteur gaussien de dimension 2 : loi marginale, loi conditionnelle, et la loi de μ + Lε | ★★ | 10 | §1 | C, E | wbm | — |
| CP6.2 | ✏️ | La divergence KL entre deux gaussiennes de dimension 2, et une interpolation sphérique | ★★ | 9 | §1 | C, E | wbm | — |
| CP6.3 | ✏️ | Un mélange de deux gaussiennes de variances connues et trois mesures : responsabilités, un pas d'EM sur le poids et les moyennes, et l'écart à l'ELBO d'une affectation dure | ★★ | 10 | §1 | C, E | wbm | — |
| CP6.4 | ✏️ | Une chaîne de Markov à trois états : loi à deux pas, et la valeur d'une politique fixée par le système de Bellman, quand une ligne finit | ★★ | 9 | §1 | C, E | wbm | — |
| CP6.5 | ✏️ | Un jeu à somme nulle 2 × 2 en stratégies mixtes, et W₁ entre deux petits échantillons de même taille | ★★ | 9 | §1 | C, E | wbm | — |
| CP6.6 | ✏️ | Des distances aux positions : double centrage, matrice de Gram, et une configuration à une isométrie près | ★★ | 8 | §1 | C, E | wbm | — |
| CP6.7 | ✏️ | La distance de Fréchet de deux gaussiennes du plan de covariances proportionnelles, et le biais de la distance entre deux moyennes estimées | ★★ | 9 | §1 | C, E | wbm | — |
| CP6.8 | ∂ | Une démonstration au choix : l'entropie d'une loi tempérée croît avec la température, ou la loi de Boltzmann minimise l'énergie libre | ★★★ | 12 | §1 | C, E | manuel | — |
| CP6.9 | 🐛 | Corriger une copie : cinq erreurs, une par chapitre | ★★ | 9 | §1 | C, E | wbm | — |
| CP6.10 | 🔗 | Problème de synthèse : une file d'attente à trois états suivie de façon gloutonne, puis échantillonnée après la troncature top-p de ses transitions : lois conditionnelles, coût en KL et nouvelle loi stationnaire | ★★ | 16 | §1 | C, E | wbm | — |
| CP6.11 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme CP5 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, 03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md ; examen entièrement sur papier (calculatrice ou Python comme simple calculatrice, sans NumPy), notebook de vérification derrière `EXAM_OVER`, barème d'un point par minute prévue, chaque réponse avec son format. Aucune question ne reprend le checkpoint VI de workbookIA (`checkpoints/partie_6/` de workbookIA), qui se fait juste après, ni son mini-projet VI (`projets/partie_6_generatif/`) ; une même configuration, même avec d'autres nombres, est une reprise (règle de CP5). Ne sont donc pas posés : une matrice de Gram de cartes d'activation aplaties, normalisée par CHW, sa forme (C, C) et la permutation des positions (CP6.1 h et CP6.5 de workbookIA, ✏️ 28.2) ; un tirage reparamétrisé μ + σ ⊙ ε avec log σ², la KL de chaque latent contre 𝒩(0, 1), la dérivée ½σε et le cas log σ² = −10 (CP6.2) ; une mise à jour de Q-learning puis de SARSA sur une table, la probabilité d'une action ε-greedy (CP6.3) ; le discriminateur optimal par a ln y + b ln(1 − y), les losses 2 ln 2 et ln 2 à l'équilibre, la saturation de ln(1 − D) (CP6.4 : l'outil se teste dans un autre cadre, la fraction de Kelly p ln(1 + f) + (1 − p) ln(1 − f) par exemple, à vérifier contre M27) ; le retour actualisé d'une suite de récompenses et la mémoire d'une table Q en 3ⁿ (CP6.1 d, CP6.10) ; les courbes d'un VAE, d'un GAN et d'un Q-learning (CP6.7) ; une taille de sortie de convolution ou de convolution transposée, deux pas d'Adam (CP6.13) ; un facteur de compression 784/32 ; la mémoire d'un dataset N × H × W × C (✏️ 29.1) ; la distance de Fréchet entre features, l'entropie des classes prédites divisée par ln 10, la distance au plus proche voisin d'entraînement et le quantile de copie du mini-projet. Nombres évités, en plus de ceux des notes de M25a à M28 : 24,5 ; 0,81 ; (16, 4) ; 0,5, 1,386 et 0,693 ; (64, 64), 64 cartes de 14 × 14 et (196, 196) ; 70 000 et 60 000 ; μ = (0,5 ; −1), log σ² = (0 ; ln 0,25), ε = (1,2 ; −0,4), [1,7 ; −1,2], [0,1250 ; 0,8181], 0,9431, −0,1000, −10 et 4,5 ; la table (0,2 ; 0,4 ; 0,1 / 0,5 ; 0,3 ; 0,8 / 0,6 ; 0 ; 0), α = 0,5, γ = 0,9, 0,56, 0,72, 0,9, 1,17, 0,425, 0,45, ε = 0,2 et 0,8667 ; p_data = 0,3, p_g = 0,1 et 0,75 ; [[1, 0, 2, 1], [0, 1, 1, 0], [2, 1, 0, 1]], [[6, 2, 3], [2, 2, 1], [3, 1, 6]], 0,5 et 0,25 ; 506 plateaux, 3 000 parties, 100 coups, 20,2 %, 80 à 95 % et 2,7 coups ; β = 60, 208 et 120 nats, 0,004 nat ; 10⁻² et 10⁻⁵, −0,2 et 4 ; FrozenLake 8 × 8, 64 victoires, 3 000 épisodes, 60 pas ; 829,45, 2,75, 837,68, 16 images, d = 4, la graine 68 ; 𝒩(4 ; 1,25²), batch 64, 2 × 10⁻³, 1 500 pas, 4,05 et 1,26 ; 3⁹, 5 478, 3¹⁶, 0,71 Mo, 0,20 Mo, 2,755 Go, 24 848 ; (1, 3, 64, 64), 2 432, (1, 32, 32, 32), (1, 16, 64, 64), w₀ = 1, η = 0,01, g = (0,5 ; −0,1), 0,99 et 0,9849 ; CelebA (200 000 photos, 40 attributs) ; et, du mini-projet, 50 000 / 10 000 et la graine 2026, les graines 0, 1 et 2, β ∈ {0,5 ; 1 ; 4}, les latents 16 et 64, copy_quantile 1 %, le plancher 1,093, les repères 212,166 et 490,696, 214,888, 95,149, 37,27, 0,925, 0,9993, 0,111 et le seuil 1,6126. La synthèse a sa propre structure (une carte mentale et une fiche d'une page faites par l'apprenant) : elle ne recopie ni le tableau des 18 formules, ni la carte mentale à neuf nœuds, ni le tableau AE/VAE/GAN/diffusion, ni « le gradient par rapport à l'entrée : un même geste, quatre usages », ni la check-list des 8 points d'un dataset, ni le mode d'emploi en 90 minutes de la synthèse de workbookIA. Côté M28, l'examen pose la matrice de Gram d'une famille de **points** (double centrage, distances, configuration à une isométrie près, CP6.6) et la troncature top-p des lignes d'une chaîne, avec son coût en divergence KL (CP6.10) ; la température n'est que dans le ∂ au choix CP6.8 et le quiz ; la variation totale, les fréquences spatiales et la montée projetée ne sont que dans le quiz et le 🐛 ; jamais de carte, de pixel permuté ni de logit de mot. CP6.8 donne le choix entre un énoncé que M28 admet, l'entropie d'une loi tempérée croît avec la température (dH/dT = Var(E)/T³ ≥ 0, énoncé et constaté en M28), et un transfert de M25b, la loi de Boltzmann minimise l'« énergie libre » E_q[E] − T H(q) parmi les lois q (par la positivité de la KL : le calcul de ln p(x) = ELBO + KL, avec une température et sans variable latente) ; aucune ne touche à un discriminateur, à une reparamétrisation ni à une contraction de l'opérateur de Bellman avec un maximum (∂ 26.8). CP6.10 relie M26 et M28 hors réseau : une file d'attente à trois états (pas une météo : ✏️ M28.6 en est une) dont on suit l'état le plus probable (une itération déterministe : elle boucle, prépériode et période), puis qu'on échantillonne après avoir tronqué chaque ligne à ses issues les plus probables (lois conditionnelles, coût en KL d'une ligne, nouvelle loi stationnaire, que CP6.4 ne demande plus) ; ni mots, ni génération de texte, ni état terminal, ni récompense de jeu. Les titres de CP6.1 à CP6.7 suivent les entrées de M25a à M28 ; leurs cadres et leurs nombres se fixent à la génération, contre les entrées publiées de ces chapitres (aucune reprise de leurs exercices ni de leurs fiches, cf. CP5), règle qui vaut pour tout l'examen : CP6.6 n'est pas le losange de villes de ✏️ M28.2 ; CP6.7 porte sur des séries de mesures (jamais des features ni un FID) et n'est pas la configuration de ✏️ M27.9 (covariances diagonales, puis tournées ensemble) ; CP6.10 n'est pas la prévision météo de ✏️ M28.6 ; CP6.2 suit les garde-fous de M25a (deux covariances pleines, jamais contre N(0, I) ni une diagonale contre l'identité). **Équilibre** (relectures de la session 60) : chaque chapitre pèse de 16 à 22 minutes de l'examen (M25a : CP6.1 et CP6.2 ; M25b : CP6.3 et l'option B de CP6.8 ; M26 : CP6.4 et la moitié de CP6.10 ; M27 : CP6.5 et CP6.7 ; M28 : CP6.6, la moitié de CP6.10 et l'option A de CP6.8), plus deux affirmations par chapitre dans CP6.Q1 (pour M27 : JS de lois à supports disjoints, la descente-montée simultanée ; pour M25b : KL directe ou inverse, le posterior agrégé) et une erreur par chapitre dans le 🐛 CP6.9 (celles de M25b et de M27 sur d'autres objets que les 🐛 M25b.28 et M27.27). **Durées** (CP5 prévoyait 112 minutes, le candidat simulé en a mis environ 137) : CP6.3 avec deux composantes de variances connues, trois mesures, seulement le poids et les moyennes mis à jour, et l'écart à l'ELBO d'une affectation dure, −Σ ln r ; CP6.4 sur une chaîne dont le système de Bellman est triangulaire (une ligne qui finit), sans loi stationnaire ; CP6.5 avec deux échantillons de même taille (les tailles différentes sont à 27.11) ; CP6.10 à trois états.

<a id="mb2"></a>
## MB2 · Cooccurrences, PMI et embeddings

**Partie** VII · **prépare** workbookIA B2 · **dossier** `chapitres/mb2_cooccurrences/` · **MML** — · **sessions de génération** 1

Les outils mathématiques des embeddings construits par comptage, hors de tout texte : l'écriture d'un entier en base 2 et en base 16 (une lacune) ; l'information mutuelle ponctuelle (PMI) des cases d'une table jointe, son signe, sa borne, la PPMI, et l'information mutuelle de M06 comme sa moyenne ; le lissage d'une marge, une loi tempérée (rappel de M28), et ce qu'il fait à la PMI de chaque colonne ; la SVD tronquée d'une table non centrée (rappel de M12d) et la répartition des valeurs singulières entre deux facteurs, qui fixe le produit mais pas les angles ; le modèle logistique d'une paire, le logit d'un taux et le décalage de ln K quand on sous-échantillonne une classe (formule de Bayes) ; la géométrie des voisins et des analogies (cosinus, parallélogramme, et la borne qui explique l'exclusion des points de la question) ; retirer une direction d'un nuage ; la moyenne masquée et le coût des comparaisons par paires. Les cadres sont des oiseaux, des magasins, des publicités, des aliments, des mesures d'animaux et des capteurs de sol. workbookIA B2 applique ces outils aux tokenizers, à la PPMI suivie d'une SVD, à word2vec et aux embeddings de phrases.

**Temps** : 13,2 h en parcours complet, 9,8 h en parcours essentiel (lecture 135 min, 16 flashcards).

**Objectifs**

- Écrire un entier en base 2 et en base 16, lire un octet et une couleur, découper un mot de bits en champs, et compter les bits qu'il faut pour N valeurs.
- Calculer la PMI des cases d'une table jointe, la lire comme le logarithme d'un lift, en tirer la PPMI, et retrouver l'information mutuelle comme la moyenne des PMI.
- Démontrer la borne PMI(x, y) ≤ min(−ln p(x), −ln p(y)) et expliquer pourquoi les événements rares ont les PMI extrêmes et les plus bruitées.
- Lisser une marge par une puissance, la reconnaître comme une loi tempérée, et prévoir le décalage de la PMI de chaque colonne.
- Répartir les valeurs singulières d'une SVD tronquée entre deux facteurs, et démontrer ce qui dépend de ce choix (les angles entre lignes) et ce qui n'en dépend pas (le produit).
- Calculer le logit de vraisemblance maximale d'un taux, et corriger par ln K un sous-échantillonnage d'une classe (formule de Bayes).
- Mesurer le parallélogramme d'une analogie et expliquer, par une borne sur le cosinus, pourquoi on exclut les points de la question.
- Retirer d'un nuage une direction estimée, et dire quelles distances changent et lesquelles restent.
- Résumer des suites de vecteurs de longueurs différentes par une moyenne masquée, et comparer le coût des comparaisons par paires à celui d'un vecteur par élément.

**Sections de la fiche**

- §1 Bases 2 et 16 : écrire un entier, lire un octet, découper un mot de bits
- §2 La PMI d'une table jointe : signe, −∞, PPMI, borne des événements rares, et l'information mutuelle comme moyenne
- §3 Lisser une marge : une loi tempérée, et ce qu'elle fait à la PMI de chaque colonne
- §4 La SVD tronquée d'une table non centrée : répartir les valeurs singulières entre deux facteurs
- §5 Le modèle logistique d'une paire : le logit d'un taux, et le décalage de ln K quand on sous-échantillonne une classe
- §6 Voisins et analogies : cosinus, produit scalaire et parallélogramme
- §7 Retirer une direction : la projection sur le complément, et ce qui reste
- §8 D'éléments à des ensembles : la moyenne masquée et le coût des comparaisons par paires

**Notions enseignées** : numération en base 2 et en base 16 : divisions successives, groupes de 4 bits, un octet en deux chiffres hexadécimaux, une couleur #RRGGBB, un mot de bits découpé en champs (lacune : workbookIA B2 s'en sert pour UTF-8) ; ⌈log₂ N⌉ bits pour N valeurs (rappel de R6 §4 et M06 §7) · information mutuelle ponctuelle d'une table jointe, PMI(x, y) = ln p(x, y)/(p(x)p(y)) = ln P(y | x)/P(y) : signe, −∞ sur une case vide, logarithme du lift d'une règle « x ⇒ y », PPMI = max(0, PMI) ; une colonne indépendante des lignes a des PMI nulles · l'information mutuelle (M06) est la moyenne des PMI sous la loi jointe : positive, bien que des PMI soient négatives · borne PMI(x, y) ≤ min(−ln p(x), −ln p(y)), atteinte quand x n'arrive qu'avec y : les événements rares ont les PMI les plus grandes possibles ; PMI normalisée PMI/(−ln p(x, y)) ≤ 1 (démontré) · estimer une PMI sur un échantillon : une case rare donne une estimation très dispersée, parfois −∞ (constaté par l'expérience) · lisser une marge : p_α(y) ∝ n(y)^α avec 0 < α < 1, la loi tempérée de température 1/α (rappel de M28) ; elle remonte les colonnes rares et décale la PMI de chaque colonne de −ln(p_α(y)/p(y)), une constante par colonne ; lissée sur ses seules colonnes, une table symétrique ne l'est plus · SVD tronquée d'une table non centrée (rappels de M12d : SVD compacte, Eckart-Young) ; répartir les valeurs singulières : M_k = (U_k S_k^β)(V_k S_k^{1−β})ᵀ pour tout β ∈ [0, 1] ; le produit ne dépend pas de β, les produits scalaires et les cosinus entre lignes du premier facteur en dépendent en général ; β = 1 garde ceux des lignes de M_k, β = 0 ceux des lignes de U_k (démontré ; la non-unicité de toute factorisation de rang k est en MB4) · ne pas centrer une grande table creuse avant sa SVD tronquée : centrer la rend pleine (mémoire, coût), et la SVD non centrée approche la table elle-même · le modèle logistique d'une paire : σ(s) est la probabilité qu'une paire soit une vraie paire plutôt qu'une paire tirée au hasard ; le logit de vraisemblance maximale d'un taux observé (a succès, b échecs) est ln(a/b), le logit de la proportion (rappel de M13a, sur des comptes) · sous-échantillonner une classe (étude cas-témoins) : garder les positifs avec la probabilité s₁ et les négatifs avec s₀ multiplie la cote par s₁/s₀ (formule de Bayes) ; dans un modèle logistique, seule l'ordonnée à l'origine bouge, de ln(s₁/s₀) (démontré) ; le résultat de Levy et Goldberg est énoncé en une phrase dans la fiche, démontré dans workbookIA B2 · voisins : cosinus et normalisation, ‖a − b‖² = 2 − 2 cos(a, b) pour des vecteurs unitaires, donc le même classement (rappel de M07), produit scalaire contre cosinus (les vecteurs longs l'emportent) · analogie et parallélogramme : requête q = b − a + c, défaut ‖(b − a) − (d − c)‖ ; si ‖b − a‖ ≤ ε‖c‖ avec ε < 1, alors cos(q, c) ≥ √(1 − ε²) (démontré dans la fiche) : c a avec q un cosinus proche de 1 et reste en haut de la liste, d'où l'exclusion de a, b et c · retirer une direction : x − (x·u/u·u)u, la projection sur le complément de la droite (rappels de M07 et M12b) ; une direction estimée comme premier axe de différences (M12d, par la matrice de Gram de M28) ; Pythagore : seule la composante de la différence sur u disparaît ; retirer (1, …, 1), c'est centrer chaque vecteur (M20) · moyenne masquée Σ m_t h_t / Σ m_t d'une suite de vecteurs complétée par des zéros : invariance par le remplissage ; coût des comparaisons par paires, C(n, 2) (R8), contre un vecteur par élément et un produit matriciel · une table de vecteurs lue par une ligne one-hot (rappel de M09a, une ligne)

**Prérequis** : division euclidienne et reste (`//`, `%`) (R0) · puissances de 2 et de 10, moyenne pondérée (R1) · notations Σ (R4) · logarithmes ln et log₂, bits et nats, sigmoïde et σ(−x) = 1 − σ(x), cote et logit (R6) · combinaisons C(n, 2), simulation avec une graine (R8) · loi des grands nombres, erreur type d'une proportion (M02c) · probabilités jointes et marginales, tableau de contingence, indépendance, loi conditionnelle (M03) · formule de Bayes (M04) · entropie, information mutuelle d'un tableau (`info.mutual_information`) (M06) · produit scalaire, normes, similarité cosinus, Cauchy-Schwarz, projection sur une droite (M07) · produit matriciel, transposée, une ligne one-hot fois une matrice (M09a) · rang d'une matrice (M12a) · complément orthogonal, projection orthogonale, matrices orthogonales (M12b) · valeurs et vecteurs propres d'une matrice symétrique (théorème spectral), trace (M12c) · SVD compacte, approximation de rang faible (Eckart-Young), axes principaux (M12d) · maximum de vraisemblance de Bernoulli, régression logistique (le score est la log-cote) (M13a) · réductions le long d'un axe, diffusion, centrage comme projection (M20) · matrice de Gram d'une famille de vecteurs, température sur des probabilités (`temper`) (M28)

**mymath** : `cooccurrence.py` (signatures figées) : `pmi`, `case_control_logit`, `remove_direction`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B2.7 ∂ Skip-gram avec échantillonnage négatif : gradients par rapport au mot et au contexte · B2.1 ✏️ « Noël à Paris » en UTF-8 : octets, points de code, longueur · B2.2 ✏️ Analogie à la main : roi − homme + femme sur des vecteurs de dimension 3 · B2.5 ✏️ One-hot fois matrice : nn.Embedding à la main, et quelles lignes reçoivent un gradient · B2.6 ✏️ Co-occurrences et PPMI à la main (fenêtre de 1, quatre mots) · B2.9 🧮 Fermi : poids de la table d'embedding de GPT-2 et d'un LLM à 128 000 tokens · B2.11 ⚖️ Une taxe cachée sur certaines langues, des stéréotypes dans les vecteurs : tokenisation et biais · B2.22 🔨 cooccurrence_matrix et ppmi · B2.23 🔨 cosine_similarity_matrix et most_similar · B2.24 📦 Embeddings PPMI + SVD sur Holmes : les voisins de « Holmes », « Watson » et « letter » · B2.25 📦 word2vec (skip-gram, échantillonnage négatif) en PyTorch sur Verne · B2.28 📦 Embeddings de phrases (MiniLM, mean pooling) et recherche sémantique dans Holmes · B2.Q7 🧠 WordPiece, Unigram, SentencePiece : quel critère pour quelle méthode ? · B2.Q9 🧠 nn.Embedding : une table de consultation entraînable, pas une couche magique · B2.Q10 🧠 L'hypothèse distributionnelle : un mot se définit par ses voisins · B2.Q11 🧠 Statique ou contextuel : l'« avocat » du tribunal et celui du marché · B2.Q12 🧠 Cosinus ou distance euclidienne pour des embeddings normalisés ? · B2.E4 💼 Qu'est-ce qu'un embedding, et comment mesurer la similarité de deux textes ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| MB2.Q1 | 🧠 | Bases 2 et 16 : le nombre de chiffres d'un entier, la valeur d'un octet, les bits qu'il faut pour N valeurs | ★ | 4 | §1 | C, E | manuel | — |
| MB2.Q2 | 🧠 | La PMI d'une case : son signe, −∞, la PPMI, la borne des événements rares, et l'information mutuelle qui en est la moyenne | ★ | 6 | §2 | C, E | manuel | — |
| MB2.Q3 | 🧠 | Lisser une marge : quelles colonnes gagnent, de combien bouge la PMI d'une colonne, et quels classements le lissage garde | ★ | 5 | §3 | C, E | manuel | — |
| MB2.Q4 | 🧠 | Répartir les valeurs singulières entre deux facteurs : ce qui dépend de β, ce qui n'en dépend pas, et pourquoi ne pas centrer une table creuse | ★ | 6 | §4 | C, E | manuel | — |
| MB2.Q5 | 🧠 | Le logit d'un taux et le sous-échantillonnage : ce qui bouge (l'ordonnée à l'origine), de combien, dans quel sens | ★ | 4 | §5 | C, E | manuel | — |
| MB2.Q6 | 🧠 | Analogies, direction retirée et moyenne masquée : vrai ou faux, avec une raison | ★ | 5 | §6 §7 §8 | C, E | manuel | — |
| MB2.R1 | 🔁 | L'information mutuelle d'un tableau 2 × 2 (M06) | ★ | 8 | §2 | C, E | manuel | — |
| MB2.R2 | 🔁 | La meilleure approximation de rang 1 d'une matrice et son erreur (Eckart-Young, M12d) | ★ | 8 | §4 | C, E | manuel | — |
| MB2.R3 | 🔁 | Cosinus, projection sur une droite et prototype d'une classe (M07, workbookIA B1) | ★ | 7 | §6 §7 | C, E | manuel | — |
| MB2.1 | ✏️ | Des entiers en base 2 et en base 16 : conversions, une couleur #RRGGBB, les bits pour 5 000 codes, et un mot de 16 bits découpé en deux champs | ★ | 20 | §1 | C, E | wbm | — |
| MB2.2 | ✏️ | Cent oiseaux, trois milieux, quatre espèces : la PMI des cases, le lift d'une règle, la PPMI, l'espèce vue une seule fois, et l'information mutuelle comme moyenne | ★★ | 30 | §2 | C, E | wbm | — |
| MB2.3 | ✏️ | Lisser la marge des espèces de la même table (α = 1/3) : la loi lissée, le décalage de la PMI de chaque colonne, et le classement des espèces d'un milieu avant et après | ★★ | 25 | §3 | C, E | wbm | MB2.2 |
| MB2.4 | ✏️ | Quatre magasins, trois produits, une table de rang 2 de SVD donnée : les facteurs U S^β et V S^{1−β} pour β = 0, ½ et 1, leur produit, et le cosinus de deux magasins | ★★ | 35 | §4 | C, E | wbm | — |
| MB2.5 | ✏️ | Une bannière affichée 3 200 fois et cliquée 50 fois : le logit de vraisemblance maximale, puis un non-clic gardé sur 9, le décalage de ln 9 et sa correction | ★★ | 20 | §5 | C, E | wbm | — |
| MB2.6 | ✏️ | Yaourt et fromage blanc, nature et sucrés : mesurer le parallélogramme d'une analogie (défaut, rapport ε, borne du cosinus), et dire si d peut l'emporter sur c | ★★ | 25 | §6 | C, E | wbm | — |
| MB2.7 | ✏️ | Des mesures d'animaux en logarithme : la direction de taille estimée sur deux différences, la retirer de trois animaux, et les distances qui restent | ★★ | 25 | §7 | C, E | wbm | — |
| MB2.8 | ∂ | La PMI est majorée par −ln p(x) et par −ln p(y), avec égalité quand x n'arrive qu'avec y ; la PMI normalisée est donc au plus 1 | ★★ | 20 | §2 | C, E | manuel | — |
| MB2.9 | ∂ | Répartir les valeurs singulières entre deux facteurs : le produit ne dépend pas de β, les produits scalaires des lignes si | ★★★ | 30 | §4 | C | manuel | — |
| MB2.10 | ∂ | Sous-échantillonner une classe : par la formule de Bayes, la cote observée est celle de la population multipliée par le rapport des taux de sélection s₁/s₀ ; dans un modèle logistique, seule l'ordonnée à l'origine bouge, de ln(s₁/s₀) | ★★ | 25 | §5 | C, E | manuel | — |
| MB2.11 | 🔗 | Pont : résumer des séries de relevés de longueurs différentes par une moyenne masquée, montrer que le remplissage ne change rien, et compter les comparaisons par paires | ★ | 15 | §8 | C, E | wbm | — |
| MB2.12 | 🗣️ | Expliquer à un ornithologue ce que mesure la PMI d'un milieu et d'une espèce, et pourquoi une espèce vue une seule fois a la plus grande | ★ | 15 | §2 §3 | C, E | manuel | — |
| MB2.E1 | 💼 | « Pourquoi ne centre-t-on pas une grande table de comptages creuse avant de la factoriser par une SVD tronquée ? » | ★ | 10 | §4 | C | manuel | — |
| MB2.13 | 🔨 | La table des PMI d'une loi jointe, −∞ sur les cases vides · `pmi` | ★ | 35 | §2 | C, E | pytest | — |
| MB2.14 | 🔨 | Deux briques : le logit d'une population estimé sur un échantillon cas-témoins, et retirer une direction des lignes d'une matrice · `case_control_logit, remove_direction` | ★★ | 45 | §5 §7 | C, E | pytest | — |
| MB2.15 | 🔮 | Prédire puis mesurer la dispersion de la PMI estimée sur 400 observations, pour une case rare et une case fréquente, avec et sans lissage | ★★ | 35 | §2 §3 | C | wbm | — |
| MB2.16 | 🎨 | Des magasins dans le plan des deux facteurs U₂S₂^β, pour β = 0, ½ et 1 : ce qui s'étire, et les angles qui changent | ★ | 40 | §4 | C | manuel | — |
| MB2.17 | 🐛 | Chasse à l'erreur : une PMI calculée sans le total, des facteurs U S^β et V S^β, une direction retirée sans diviser par u·u | ★ | 30 | §2 §4 §7 | C, E | wbm | — |
| MB2.18 | 🛠️ | Un test de propriété de `pmi` sur des tables tirées au hasard : la borne, la transposition, et la moyenne qui redonne l'information mutuelle de M06 | ★ | 40 | §2 | C | manuel | MB2.13 |
| MB2.19 | 🏆 | Défi : retrouver, sur 3 000 observations, les cinq paires les plus associées d'une table cachée de 10 × 10, sans se laisser piéger par les cases rares | ★★★ | 50 | §2 §3 | C | wbm | MB2.13 |

*Notes* : Frontières : le ∂ B2.7 (les dérivées de −ln σ(±s) et σ′ = σ(1 − σ), les gradients par rapport à u_c, u_{n_k} et v_w, les lignes touchées, l'application chiffrée, la collision n₁ = c, l'optimum PMI − log K annulant ℓ′(x) avec les comptes #(w, c) et K #(w)#(c)/N, le lien avec la régression logistique), ✏️ B2.1 (« Noël à Paris » en UTF-8 : points de code, octets, motifs, NFD), ✏️ B2.2 (l'analogie roi − homme + femme : requête, cosinus, plus proche avec et sans exclusion, produit scalaire, normalisation), ✏️ B2.5 (one-hot fois la table, gradient de la table, SGD, `padding_idx`, weight decay), ✏️ B2.6 (cooccurrences d'une séquence par une fenêtre, PMI, PPMI lissée, symétrie perdue), 🧮 B2.9 (poids d'une table d'embedding), ⚖️ B2.11 (taxe des langues, biais des embeddings, direction de genre, neutralisation, tri de CV), 🔨 B2.22 et B2.23 (`cooccurrence_matrix`, `ppmi`, `cosine_similarity_matrix`, `most_similar`), 📦 B2.24 (PPMI puis SVD sur Holmes, U_d S_d^{1/2} normalisé, voisins), 📦 B2.25 (word2vec en PyTorch : sous-échantillonnage, loi des négatifs), 📦 B2.28 (mean pooling avec masque et recherche sémantique), les quiz B2.Q7 (score de WordPiece), B2.Q9 (`nn.Embedding`), B2.Q10 (hypothèse distributionnelle, signe et valeur d'une PMI), B2.Q11 (moyenne masquée de trois vecteurs), B2.Q12 (cosinus et distance de vecteurs unitaires, produit scalaire contre cosinus) et l'entretien B2.E4. MB2 enseigne les outils hors du texte : oiseaux et milieux, magasins et produits, publicités et clics, aliments et nutriments, mesures d'animaux, capteurs de sol ; jamais un mot, un token, un tokenizer, un corpus, une fenêtre glissante sur une séquence, une table d'embedding de modèle, un genre, une capitale, un CV ni un modèle de langue. §1 (lacune de workbookIA B2, qui convertit en hexadécimal et découpe des bits sans l'enseigner ; R6 n'a que les bits et M05a.8 le binaire d'un flottant, hors parcours essentiel) : divisions successives (R0), groupes de 4 bits, un octet en deux chiffres hexadécimaux, une couleur #RRGGBB, ⌈log₂ N⌉ bits pour N (un rappel de R6 §4 et M06 §7, erratum de la session 71 : ce n'est pas une lacune) valeurs, un mot de 16 bits découpé en champs (4 + 12) ; ni UTF-8, ni point de code, ni motif 110xxxxx, ni 0x10FFFF (✏️ B2.1, que workbookIA garde). §2 : la PMI d'une table jointe donnée (ou d'une table de contingence divisée par son total, M03), jamais d'une matrice construite par une fenêtre sur une séquence (✏️ B2.6, `cooccurrence_matrix`) ; la PPMI est définie et calculée à la main, jamais en code (c'est `ppmi` de `mylearn`) ; l'information mutuelle comme moyenne des PMI est un rappel de M06 (`info.mutual_information`) ; la borne et la PMI normalisée sont démontrées (∂ MB2.8) ; aucun quiz ne demande si une PMI négative signifie « moins souvent que l'indépendance » ni la PMI nulle de quatre comptes (B2.Q10 b et c), et la fiche ne nomme pas le score de WordPiece, la PMI sans le total (B2.Q7). ✏️ MB2.2 : 100 oiseaux, trois milieux (forêt 40, prairie 35, village 25) et quatre espèces (huppe 1, pic 8, grive 27, moineau 64), table [[0, 6, 14, 20], [1, 2, 10, 22], [0, 0, 3, 22]] : PMI(forêt, pic) = ln 1,875 ≈ 0,629 (lift 1,875), PMI(village, grive) = ln(4/9) ≈ −0,811, −∞ sur trois cases, PMI(prairie, huppe) = ln(100/35) ≈ 1,050 = −ln p(prairie), la plus grande de la table pour un seul oiseau (la borne est atteinte), cinq cases de PPMI positive, I(X ; Y) ≈ 0,0759 nat. §3 : le lissage d'une marge est `temper(p, 1/α)` de M28, appliqué aux colonnes ; ✏️ MB2.3 lisse les espèces de la table de MB2.2 avec α = 1/3 (racines cubiques exactes de 1, 8, 27 et 64 : la loi (0,1 ; 0,2 ; 0,3 ; 0,4)) ; chaque colonne décale ses PMI d'une constante (−ln 10 pour la huppe, +ln 1,6 pour le moineau) ; PMI_α(prairie, huppe) ≈ −1,253, le record de la table devenu négatif ; dans la forêt, le classement pic, grive, moineau devient moineau, grive, pic, alors que l'ordre des milieux dans une colonne ne change jamais ; la table est rectangulaire, la symétrie perdue d'une table carrée n'est dite que dans la fiche (une phrase), et aucun quiz ni exercice ne la demande (B2.6 g), ni ne demande si une PMI négative d'une colonne fréquente devient positive (B2.6 h) ; jamais α = 0,75, ni la loi des négatifs, ni les comptes 100 et 1. Le 🔮 MB2.15 tire 400 observations de la loi de cette table, plusieurs centaines de fois : la PMI estimée de (prairie, huppe) est très dispersée (et vaut parfois −∞), celle de (village, moineau) non ; le lissage décale la cible, sans réduire la dispersion (erratum de la session 71 : la note disait « réduit » ; la huppe n'étant vue qu'en prairie, l'estimation de (prairie, huppe) ne dépend que du nombre d'oiseaux de prairie et varie peu, et le lissage l'en fait dépendre davantage ; le 🔮 suit aussi (prairie, pic), la case rare dispersée). §4 : la SVD est un rappel de M12d (`svd`, `low_rank_approximation`, sa convention de signe) ; aucune fonction de `mymath` ne rend U_k S_k^β (le cœur de `ppmi_svd_24`, 📦 B2.24) ; l'exposant de répartition s'appelle β (p est une probabilité dans ce chapitre ; la fiche dit que workbookIA B2 le note p) et le rang k, comme M12d. ✏️ MB2.4 : quatre magasins × trois produits, M = [[50, 8, 26], [5, 44, 8], [88, 40, 49], [34, 40, 22]] de SVD donnée (colonnes de U : (2, 1, 4, 2)/5 et (−2, 4, −1, 2)/5 ; de V : (7, 4, 4)/9 et (−4, 8, −1)/9 ; valeurs singulières 135 et 45 ; erratum de la session 71 : ces bases sont des permutations signées de celles de M12b, que la liste des évités exclut ; la génération prend M = [[12, 96, 220], [78, 54, 5], [57, 114, 190], [132, 144, 140]], U : (4, 1, 4, 4)/7 et (−4, 4, −1, 4)/7, V : (6, 10, 15)/19 et (15, 6, −10)/19, valeurs singulières 399 et 133, aux mêmes cosinus ; la troncature et Eckart-Young sont le rappel MB2.R2, sur une autre matrice), une case vérifiée, facteurs pour β = 0, ½ et 1 et leur produit, cos(magasin 1, magasin 4) = 0, puis 0,5, puis 0,8 (égal au cosinus des lignes de M pour β = 1), cos(magasin 1, magasin 2) de −0,514 à 0,316 ; aucune normalisation des lignes ni recherche de voisins. ∂ MB2.9 démontre le cas général (et, pour une matrice symétrique semi-définie positive, que β = ½ donne deux facteurs égaux) ; la non-unicité de toute factorisation de rang k (deux factorisations diffèrent d'une matrice inversible) est démontrée en MB4, pas ici. Ne pas centrer une table creuse : Q4 et 💼 MB2.E1. Le 🎨 MB2.16 trace les lignes de U₂S₂^β d'une table plus grande de magasins, créée à la génération. §5 : le logit de vraisemblance maximale d'un taux observé, ln(a/b) pour a succès et b échecs, est un rappel de M13a, sur des comptes ; ∂ MB2.10 démontre le décalage par la formule de Bayes, jamais en minimisant une loss −a ln σ(x) − b ln σ(−x) ; aucun exercice ni la fiche n'écrivent cette loss avec des poids réels, ni ne multiplient le poids d'une classe par K ; cadres : publicités et clics, études cas-témoins ; garder les positifs avec la probabilité s₁ et les négatifs avec s₀ multiplie la cote par s₁/s₀, et dans un modèle logistique seule l'ordonnée à l'origine bouge, de ln(s₁/s₀) ; le résultat de Levy et Goldberg est énoncé une fois dans la fiche, en une phrase avec un renvoi à workbookIA B2, comme le fait sa fiche, jamais dérivé ni demandé par un quiz : aucun exercice ne pose a = #(w, c) et b = K #(w)#(c)/N, ne tire des négatifs selon une loi marginale, n'écrit u_c ou v_w, ne dérive la loss de l'échantillonnage négatif, ni ne relie ses termes aux entrées, labels et poids d'une régression logistique (∂ B2.7.2 à 7). ✏️ MB2.5 : 3 200 affichages, 50 clics ; logit ln(50/3 150) = −ln 63 ≈ −4,143 ; un non-clic gardé sur 9 : ln(50/350) = ln(1/7) ≈ −1,946, soit +ln 9, probabilité lue 1/8 au lieu de 1/64 ; la correction par ln 9 ; aucune repondération des négatifs (c'est l'énoncé de ∂ B2.7.6). §6 : la fiche rappelle le cosinus, ‖a − b‖² = 2 − 2 cos (M07, sans les nombres de B2.Q12) et le produit scalaire contre le cosinus, puis démontre la borne cos(q, c) ≥ √(1 − ε²) ; ✏️ MB2.6 (aliments en (protéines, glucides, lipides) pour 100 g : yaourt nature (4, 5, 3) et sucré (4, 10, 3), fromage blanc nature (8, 4, 3) et sucré (7, 9, 3)) mesure le parallélogramme : q = (8, 9, 3), défaut δ = 1, ε ≈ 0,530 et borne ≈ 0,848 pour c, cos(q, c) ≈ 0,931 ; la borne de la fiche appliquée à d, √(1 − δ²/‖d‖²) = √(138/139) ≈ 0,9964 (4 décimales : 0,996 est un nombre évité), garantit que d l'emporte sur c sans calculer cos(q, d) (≈ 0,998) ; alignement des décalages ≈ 0,981 ; puis la crème (2, 3, 30), où ε ≈ 0,165 et la borne ≈ 0,986 est presque atteinte (0,987) ; il ne classe pas une liste de candidats avec et sans exclusion, ne cherche pas le gagnant du produit scalaire et ne normalise pas d'abord les vecteurs (B2.2 d à g). §7 : `remove_direction` retire une direction donnée ; la direction est estimée comme premier axe de différences (à la main : deux différences de même norme ont pour premier axe leur somme, par la matrice de Gram 2 × 2) ; ✏️ MB2.7 : mesures d'animaux en logarithme, différences (2, 4, 3) et (4, 2, 3), premier axe (1, 1, 1)/√3 (retirer la taille revient à centrer, M20), trois animaux (2, 3, 4), (3,5 ; 4,5 ; 5,5) et (5, 3, 4) : les deux premiers se confondent, la distance du premier au troisième passe de 3 à √6 ; la fiche dit ce que retirer une direction ne fait pas (une information portée par d'autres directions corrélées reste), sans biais social, paires de genre, CV ni règlement (⚖️ B2.11). §8 : moyenne masquée de relevés de capteurs de sol (température, humidité ; les stations météo sont celles de M20), complétés par des zéros ; ni token, ni `[PAD]`, ni les h_t de B2.Q11 ; le coût des paires compare C(n, 2) comparaisons à n résumés et un produit matriciel, sans SBERT ni 10 000 phrases. Le 🐛 MB2.17 n'a aucune erreur du corrigé de 🔨 B2.22 (lissage sur les lignes, log₂), de 🔨 B2.23 (`eps`) ni de 🐛 B2.18 ; le 🛠️ MB2.18 ne teste pas « une table produit donne des PMI nulles » (la propriété documentée de `ppmi`) ; le 🏆 MB2.19 se vérifie sur trois tables cachées tirées à nouveau à chaque exécution, avec des cases rares de grande PMI qui piègent l'estimation directe, et un rayon et une tranche dominants dont la case commune, fréquente sans être associée, piège les cinq cases les plus vendues (apprenant simulé, session 71), et laisse la méthode libre (pseudo-comptes de M04, lissage, seuil sur les comptes) ; la règle de score et le seuil sont calés à la génération. Évités (règle de partage) : de la fiche de workbookIA B2, « Les chatons s'endorment paisiblement. » (37, 7, 11, 2,75, 1,2), Holmes et Verne (88 caractères, 7 819 et 8 793 mots, 105 849, 562 000, 13,5 %), « ç » U+00E7 = 231 = C3 A7, « 🙂 » F0 9F 99 82, « € » E2 82 AC, « Ça coûte 15 € » (13 points de code, 17 octets), 0x10FFFF, « chat » × 5, « chats » × 2, « chaton » × 3, « rat » × 4, « raton » × 2, 50 257 = 256 + 50 000 + 1, la Déclaration universelle, 32 768/1,12, « thé » et « café », « le vieux phare éclaire la côte », la matrice chien/chat/os [[0, 4, 1], [4, 0, 1], [1, 1, 2]] (N = 14, sommes 5, 5, 4 ; PMI 0,807, −0,357, 0,560 ; lissée 0,351, 0,297, 0,823), le skip-gram chiffré (d = 3, K = 2, (0,5 ; −1 ; 2), (1 ; 0 ; 0,5), (0 ; 1 ; 0), (−1 ; 0,5 ; 1), scores 1,5, −1 et 1, L ≈ 1,828), « éclaire », « fromage », « lundi », les comptes 100 et 1 (0,990/0,010 → 0,969/0,031, 100^0,75 ≈ 31,6), K de 5 à 20 et de 2 à 5, t ≈ 10⁻⁵ et 10⁻³, 1 % jeté 97 fois sur 100 (0,968), α = 0,75, GloVe f(X) = min(1, (X/100)^{3/4}), l'analogie France/Paris/Italie/Rome/Milan/Lyon ((0,1 ; 1 ; 0), (1 ; 1 ; 0,1), (0,1 ; 0 ; 1), (1 ; 0,1 ; 1), (0,6 ; 0 ; 1), (0,6 ; 1 ; 0), requête (1 ; 0 ; 1,1), 0,996, 0,981, 0,803, 0,527, 0,346, 0,067) et Madrid/Espagne, « father », « three », Bolukbasi (300 dimensions, dix paires), « glace », SBERT (10 000 phrases, 5 s contre 65 h, 50 millions de passes), MiniLM (384, 6 couches, 256 tokens, 30 522 × 384 = 11 720 448), e5, Qwen3, la requête « I can't log in to my account » (0,502, 0,293, 0,042) ; des exercices de workbookIA B2 : Q7 (20, 40, 100 et 30, 300, 200 ; 0,005 et 0,0005), Q9 ((8, 20), 1 000 × 64, 5 000 × 32 = 160 000, un token lu 3 fois), Q10 (1 000, 6, 30, 200, PMI nulle), Q11 ((1, 2), (3, 0), (2, 4), (0, 0), masque (1, 1, 1, 0), 2,0 et 1,5), Q12 (cos 0,8 → 0,4, √2 ≈ 1,414, (3, 4) et (−6, −8)), R3 ((1/2, 1/4, 1/8, 1/8), 1,75 bit), ✏️ B2.1 (« Noël à Paris », 12, 14, 0xC3 0xAB = 195, 171, 16 ; « œ » C5 93 = 197, 147 ; « Δ = b² − 4ac »), ✏️ B2.2 (roi (0,6 ; 1 ; 0,9), reine (0,8 ; −0,5 ; 0,9), homme (0,1 ; 1 ; 0,9), femme (0,1 ; −1 ; 0,9), prince (0,7 ; 0,8 ; 0,2), princesse (0,7 ; −0,6 ; 0,2), trône (3 ; 0 ; 0,5), q = (0,6 ; −1 ; 0,9), 1,79, 0,932, 0,941, 2,25, 0,900, 0,866), ✏️ B2.3 et B2.4 (« été », « étés », « pré », « prés » ; « chanter » et ses huit fusions), ✏️ B2.5 (E = [[1, 0, 2], [0, 1, −1], [2, −1, 0], [−1, 3, 1], [0, 2, 2]], (3, 0, 3, 1), w = (1 ; −2 ; 0,5), −13,5, η = 0,1), ✏️ B2.6 (« le chat court le chat le rat court », C = [[0, 1, 3, 0], [1, 0, 1, 1], [3, 1, 0, 1], [0, 1, 1, 0]], N = 14, 0,742, −0,069, 0,330, 0,821, 0,765, 0,279 ; fenêtre 2 : 26, 0,396), ∂ B2.7 (v_w = (2 ; −1), u_c = (1 ; 1), u_n1 = (0,5 ; 0,5), u_n2 = (−1 ; 2), scores 1, 0,5 et −4, L ≈ 1,3055, η = 0,5, K = 5 → −0,868), 🧮 B2.8 (90 000 mots, 250 par page, fertilités 1,3 et 1,6, 8 192, 300), 🧮 B2.9 (50 257 × 768, 128 256 × 4 096, 2 048, 32 000), 🔬 B2.20 (tailles 300, 500, 1 000, 2 000, 4 000, 8 000 ; bits par token 6,124, 7,499, 8,298, 8,715, 8,857, 8,843 ; octets par token 1,422, 2,045, 2,560, 3,001, 3,382, 3,641 ; bits par octet 4,306 à 2,429), les exemples des stubs et du notebook de B2.22 et B2.23 ([0, 1, 2, 1], [[0, 2, 1], [2, 0, 3], [1, 3, 0]] et ses PPMI 0,47, 0,5878, 0,5218, 0,3941, 0,5838, 0,6396, [0, 0, 0, 1], [[0, 2, 1, 0], [2, 0, 3, 0], [1, 3, 0, 0], [0, 0, 0, 0]], [[1, 0], [1, 1], [0, 0]] et 0,7071, [[1, 0], [0, 1], [1, 1], [−1, 0], [2 ; 0,1]] et 0,9988, `eps` 0,5 et 2, [[3, 4]] et [[6, 8]], 0,943 et 0,866, 120 lignes dont 40 copies, `default_rng(23)`), 📦 B2.24 (4 000 mots, fenêtre 2, d = 100, 0,80, 0,73), 📦 B2.25 (1 590 mots, t = 10⁻³, K = 5, batch de 512, 6 ln 2 ≈ 4,159, rang médian 9,5), 📈 B2.27 (0,14, −0,23, 48 sur 100), 📦 B2.28 (1 055 passages de 120 mots), 🔬 B2.29, 🏆 B2.31 (2 000 tokens), 💼 B2.E5 (200 000 documents, 5 millions de passages × 384 × 4 octets ≈ 7,7 Go) ; de workbookIA B1 (cosinus et prototypes) : (1, 0, 0), (4, 2, 2), (2, 1, 0), (0, 1, 1), q = (2, 1, 1), « pomme » (0,9 ; 0,1) et (0,7 ; 0,3), « poire » (0,2 ; 0,8) et (0,4 ; 0,8), q = (0,6 ; 0,5), 0,900 et 0,869, les cosinus 0,31, 0,27, 0,22 avec s = 100 et 1, (3, 0, 4), (0, 3, 4), (16, 2, 8), (2, 1, 2), (1, 2, 2), 0,24, 0,30, 0,28, 0,19, 4,60517, 2,6592, η = 10⁻³, γ = 0,3, λ = 0,2, θ₀ = −0,4 ; et, de ce dépôt, les bases orthonormées de M12b ((2, 2, 1)/3, (1, −2, 2)/3, (−2, 1, 2)/3, (2, 3, 6)/7, (6, 2, −3)/7, (3, −6, 2)/7, (4, 4, 7)/9, (1, −8, 4)/9, (1, 2, 2, 4)/5), les exemples de `mutual_information` et de `conditional_entropy` (M06), de `temper` (M28 : (0,5 ; 0,25 ; 0,25 ; 0) à T = 1/3 et 3) et les températures de workbookIA 28 que M28 évite (0,5 ; 0,7 ; 1,2 ; 1,5 ; 2), le logit de 0,55 et σ(1,6) de M13a ; ajoutés par la relecture de la session 71 : de workbookIA, le rôle des octets UTF-8 (0x7F, 0x80, 0xC0), le ∂ B2.7.4 au complet (gradients (−0,538 ; 0,269), (1,245 ; −0,622), (0,036 ; −0,018), (0,024 ; 0,078), u_n1 → (−0,122 ; 0,811)), les cosinus 0,816, 1, 0,913, 0,577 et les normes 0,781 et 0,825 de la fiche de B1, les cosinus de B2.29 et de sa variante (0,847/0,749, 0,824/0,803, 0,885/0,838, 0,878/0,849, 0,892/0,827, 0,945/0,909) ; de ce dépôt, le tableau 2 × 2 de M06 §8 (100 clients, 30/10/10/50, (0,4 ; 0,6), 0,256 bit, 0,971 → 0,715), l'ornithologue et les six espèces de M28 §5 (le merle, la mésange), les stations météo de M20 (4, 7, 24) et M20.1 (12, 28, 24), R6.Q3 (1 000 000 → 20), M06.Q7.5 (300 issues) et M06 §7 (20 issues → 5) ; le cadre du taux de clic de M04.3, M08.9 et M13a §1 est gardé pour ✏️ MB2.5 (titre figé, autres nombres, BIBLE §24) ; la fiche ne reprend ni la table des oiseaux, ni la table des magasins, ni les aliments des ✏️, ni les exemples du stub. Conventions : logarithme népérien partout (PMI et logits en nats), sauf les bits du §1 ; une table jointe a les valeurs de X en lignes (M03, M06) ; les points sont les lignes d'une matrice (M13b, M28) ; rang k et exposant β pour les facteurs de la SVD ; a et b sont des nombres d'exemples au §5, s₁ et s₀ des taux de sélection, 𝐚, 𝐛, 𝐜, 𝐝 des vecteurs (en gras) au §6. `cooccurrence` : NumPy et `math` seulement, aucune SciPy (`scipy.special.logit`, `xlogy`, `scipy.optimize`) ni scikit-learn (`mutual_info_score`, `LogisticRegression`), qui servent d'oracles aux tests ; `pmi` prend une table jointe de probabilités (somme 1), rend des nats et −∞ sur les cases nulles, sans max(0, ·), sans lissage, sans comptes ni `alpha` : un autre contrat que `ppmi(C, alpha)` de workbookIA B2 ; `case_control_logit` prend les nombres d'exemples d'un échantillon (nombres ou tableaux, diffusés) et deux taux de sélection dans ]0, 1], et rend ln(n₁/n₀) − ln(s₁/s₀) ; sa docstring passe par la formule de Bayes, sans la forme en σ, sans comptes « attendus » ni poids multiplié par K, et jamais avec des comptes #(w, c), #(w), #(c), N ; `remove_direction` retire une direction donnée, sans l'estimer ; aucune fonction de SVD ni de facteurs U S^β, d'analogie (`most_similar` avec ses exclusions résoudrait ✏️ B2.2), de cosinus entre lignes (`cosine_similarity_matrix`), de matrice de cooccurrences ni de moyenne masquée (`embed_28`). Pas de MML : le livre ne traite ni la PMI ni les embeddings, et Eckart-Young a été lu en M12d (§4.6) ; pas de 📖. COMPOSITION : 10 h au plan (8 h avant la session 69), 10,6 h avec la lacune des bases et des durées réalistes (les chapitres de la partie VI ont dépassé leurs estimations de 20 à 40 %) ; 6 quiz, 3 rappels, 7 ✏️ et 3 ∂, un 🔗, deux 🔨 et aucun 📦 (les comparaisons avec SciPy et scikit-learn sont dans les tests, la SVD par bibliothèque est en M12d), un 🔮 et aucun 🔬 (le temps), 🐛, 🎨, 🗣️, 💼, 🛠️, 🏆, 16 flashcards ; lecture 125 min (≈ 9 000 mots au rythme des fiches de la partie VI). Durées revues à la génération (session 71), après la re-résolution à l'aveugle, l'auteur des exercices et l'apprenant simulé : lecture 135 min (≈ 9 800 mots), exercices 623 min (papier 348, notebook 275), 13,2 h en tout et 9,8 h en parcours essentiel. Parcours essentiel : ∂ MB2.9, le 💼, le 🔮, le 🎨, le 🛠️ et le 🏆 hors parcours ; les ∂ de la borne (MB2.8) et du sous-échantillonnage (MB2.10) y sont. Corrections de la relecture (session 69) : R1-1 (la voie de Bayes, `case_control_logit`), R1-4, R1-7, R1-11, R1-14.

<a id="mb3"></a>
## MB3 · Rotations, moyennes pondérées et softmax en ligne

**Partie** VII · **prépare** workbookIA B3 · **dossier** `chapitres/mb3_rotations_attention/` · **MML** §3.9 · **sessions de génération** 1

Les rotations et les moyennes pondérées dont se sert le Transformer de workbookIA B3, travaillées hors réseau. D'abord les formules d'addition, démontrées par le produit scalaire de deux vecteurs unitaires (M22 et M25a les tiraient d'une règle admise), et ce qu'elles disent des rotations du plan : R_α R_β = R_{α+β}, l'inverse est la transposée, les longueurs et les angles sont conservés, et la multiplication par e^{iθ} ; puis les rotations de l'espace et de ℝⁿ (les rotations de Givens de MML §3.9), les matrices diagonales par blocs et ce qu'une permutation des coordonnées en change. Ensuite l'encodage d'une variable cyclique (une direction, un jour de l'année) par des horloges (cos, sin) : un décalage est une rotation, et le produit scalaire de deux encodages ne dépend que de l'écart. Enfin la moyenne pondérée par une softmax : une combinaison convexe, l'estimateur à noyau de Nadaraya-Watson et sa largeur de bande, les masques comme un conditionnement, l'équivariance par permutation, l'échelle des scores (la division par √n et la saturation), la softmax en ligne avec son invariant et la fusion de deux états, et le coût quadratique de toutes les paires. workbookIA B3 applique ces outils à l'attention, à ses masques, aux encodages de position, à RoPE et à FlashAttention.

**Temps** : 14,8 h en parcours complet, 11,9 h en parcours essentiel (lecture 150 min, 16 flashcards).

**Objectifs**

- Démontrer les formules d'addition du cosinus et du sinus, et s'en servir pour des valeurs exactes, des duplications et des produits de cosinus.
- Composer et inverser des rotations du plan (R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}), et les lire comme des multiplications par e^{iθ}.
- Écrire une rotation de Givens de ℝⁿ, dire quand deux rotations commutent, et lire une matrice diagonale par blocs de rotations et ce qu'une permutation des coordonnées en change.
- Encoder une variable cyclique par (cos, sin), lire un décalage comme une rotation, et exprimer le produit scalaire de deux encodages à plusieurs horloges en fonction de l'écart.
- Calculer une moyenne pondérée par une softmax et l'estimateur de Nadaraya-Watson, et prévoir l'effet de la largeur de bande.
- Restreindre une moyenne pondérée à un sous-ensemble par un masque (une loi conditionnelle), et démontrer qu'une moyenne pondérée sur un ensemble est équivariante par permutation.
- Expliquer pourquoi l'on divise par √n une somme de n contributions indépendantes, et mesurer la saturation d'une softmax quand l'échelle des scores grandit.
- Calculer une softmax en ligne par blocs, démontrer son invariant, fusionner deux états partiels, et compter ce que coûtent toutes les paires.

**Sections de la fiche**

- §1 Les formules d'addition, démontrées : le cosinus d'une différence par le produit scalaire, puis les autres
- §2 Les rotations du plan : composer, inverser, conserver ; la multiplication par e^{iθ}
- §3 Les rotations de ℝⁿ : l'espace, les rotations de Givens, les matrices diagonales par blocs et les permutations des coordonnées
- §4 Encoder une variable cyclique : des horloges (cos, sin), et un décalage est une rotation
- §5 Une moyenne pondérée par une softmax : combinaison convexe, estimateur de Nadaraya-Watson et largeur de bande
- §6 Masques et permutations : conditionner sur un sous-ensemble, ne regarder que le passé, l'équivariance par permutation
- §7 L'échelle des scores : diviser une somme de n contributions par √n, et la saturation de la softmax
- §8 La softmax en ligne : l'état (m, l, a), son invariant, et la fusion de deux états
- §9 Le coût quadratique (rappel de MB2 §8) : la mémoire de toutes les paires, et calculer par blocs

**Notions enseignées** : formules d'addition cos(a ± b) et sin(a ± b), démontrées : le cosinus d'une différence par le produit scalaire de deux vecteurs unitaires (R9), les autres par la parité et cos(π/2 − x) = sin x ; duplication ; produit de deux cosinus en somme, cos a cos b = ½[cos(a − b) + cos(a + b)] (M28 §4 s'en servait, tiré des formules de soustraction de M25a) ; la règle e^{iα}e^{iβ} = e^{i(α+β)}, que M22 admettait, en découle · rotations du plan : R_θ (MML §3.9.1) ; R_α R_β = R_{α+β} (les formules d'addition écrites en matrices), donc deux rotations du plan commutent ; R_θ⁻¹ = R_θᵀ = R_{−θ}, det R_θ = 1 ; une rotation conserve les normes, les produits scalaires, les distances et les angles (MML §3.9.4) ; une matrice orthogonale 2 × 2 de déterminant 1 est une rotation, de déterminant −1 une symétrie ; la multiplication par e^{iθ} (rappel de M22) et Re(z̄w) = le produit scalaire des deux vecteurs · rotations de l'espace autour des trois axes (MML §3.9.2) et rotations de Givens R_ij(θ) de ℝⁿ (MML §3.9.3) ; non commutatives dès la dimension 3, sauf dans des plans disjoints ; une matrice diagonale par blocs de rotations planes tourne chaque plan de son angle ; produit par blocs (généralise M09a §3, Σ colonne × ligne) : des blocs de colonnes fois des blocs de lignes donnent une somme de produits ; conjuguer par une matrice de permutation, PᵀRP, donne la même rotation dans d'autres plans de coordonnées · encodage d'une variable cyclique (une direction, un jour de l'année) par (cos ωt, sin ωt) : deux valeurs proches sur le cercle restent proches, ‖e(t) − e(t′)‖² = 2 − 2 cos ω(t − t′) ; un décalage de t est une rotation de l'encodage, la même pour tout t ; plusieurs horloges de périodes différentes : le produit scalaire de deux encodages vaut Σ_k cos ω_k(t − t′), une fonction du seul écart ; une horloge seule ne distingue pas t de t plus sa période ; direction moyenne (l'argument de la moyenne des vecteurs unitaires) · moyenne pondérée par une softmax de scores : une combinaison convexe (dans l'enveloppe convexe, M10), inchangée quand on ajoute une même constante à tous les scores ; poids exponentiels (M14) et loi de Boltzmann (M17) · estimateur à noyau de Nadaraya-Watson ŷ(x) = Σᵢ K(x, xᵢ) yᵢ / Σⱼ K(x, xⱼ) ; avec un noyau gaussien, une softmax des scores −‖x − xᵢ‖²/(2h²) ; la largeur de bande h comme une température (h → 0 : le plus proche voisin, h → ∞ : la moyenne des yᵢ) ; à normes égales, une softmax des produits scalaires x·xᵢ/h² · masques : un score −∞ avant la softmax restreint la loi à un sous-ensemble et la renormalise (une loi conditionnelle, rappel de M03 et M28) ; mettre un poids à 0 après la softmax ne donne pas une loi ; un masque triangulaire ne regarde que le passé (filtrer plutôt que lisser) et laisse T(T + 1)/2 cases ; un sous-ensemble vide n'a pas de loi (0/0) ; la moyenne exponentielle normalisée est une softmax, sur le passé, de scores linéaires en le temps · équivariance par permutation : une moyenne pondérée sur un ensemble, dont chaque score ne dépend que de la paire, commute avec toute renumérotation (matrice de permutation P, M16) ; softmax(Ps) = P softmax(s) ; un masque triangulaire, ou un score qui dépend du rang, la casse ; l'équivariance par translation de M21 est celle d'un autre groupe · échelle des scores : une somme de n contributions indépendantes centrées de variance v a pour écart-type √(nv) (rappels de M02b, et de la variance d'un produit de M16) ; la diviser par √n garde une échelle fixe ; multiplier les scores par c, c'est diviser la température par c (M17, M28) ; saturation : quand c grandit, la softmax tend vers le one-hot du plus grand score, et la sensibilité 1 − Σ pᵢ² (la trace de diag(p) − ppᵀ, l'impureté de Gini de M13a) tend vers 0, exponentiellement vite en c (démontré dans la fiche) · softmax en ligne : lire les scores par blocs en gardant l'état (m, l, a), le plus grand score lu, Σ e^{s_j − m} et Σ e^{s_j − m} v_j, remis à l'échelle par e^{m_ancien − m_nouveau} quand le maximum change ; l'invariant, démontré par récurrence : le résultat est exact, et m + ln l est le log-sum-exp (M05a) ; aucune exponentielle d'un nombre positif ; la fusion de deux états, associative et commutative, d'élément neutre (−∞, 0, 0) : couper le calcul entre plusieurs machines ; pour un ordre au hasard, le maximum change en moyenne H_N − 1 fois sur N blocs (les records, R8 et M02b) · coût quadratique : le coût des comparaisons par paires est un rappel de MB2 §8, en une ligne ; neuf : la mémoire d'une matrice n × n contre celle d'un calcul par blocs de B lignes (n·B), pour la même quantité de calcul ; doubler n multiplie cette mémoire par 4 (une pente 2 en échelles logarithmiques, R6)

**Prérequis** : Σ, sommes doubles, raisonnement par récurrence (R4) · suites géométriques, moyenne exponentielle (lissage) (R5) · exponentielle et logarithme, échelles logarithmiques (R6) · probabilités d'issues équiprobables (R8) · cercle trigonométrique, radians, cos et sin, cos² + sin² = 1, parité et périodicité, produit scalaire et angle de deux vecteurs (R9) · intégrale de 1/x : comparer une somme à une intégrale (M02a) · linéarité de l'espérance, variance d'une somme de variables indépendantes, loi normale (M02b) · loi conditionnelle (M03) · log-sum-exp et softmax stables, overflow et underflow (M05a) · produit scalaire, normes, angle, développement de ‖a − b‖², barycentre (M07) · validation croisée : principe (M08) · somme harmonique comparée à l'intégrale de 1/x (M11) · produit matriciel, transposée, (AB)ᵀ = BᵀAᵀ (M09a) · enveloppe convexe (M10) · matrice d'une composition, changement de base (M12a) · matrices orthogonales : normes et produits scalaires conservés (M12b) · matrice de rotation du plan, déterminant, le strict minimum sur les nombres complexes (M12c) · impureté de Gini 1 − Σ p_k² (M13a) · poids exponentiels et renormalisation (M14) · matrice de permutation (renuméroter des nœuds, P A Pᵀ), variance d'un produit de variables indépendantes et d'une somme de produits décorrélés (M16) · loi de Boltzmann et ses limites en température, la matrice diag(p) − ppᵀ (M17) · tableaux à plusieurs axes, réductions le long d'un axe, diffusion (M20) · équivariance par translation (M21) · forme exponentielle r e^{iθ}, produit = rotation et homothétie, e^{iα}e^{iβ} = e^{i(α+β)} et R_α R_β = R_{α+β} admises (M22) · formules de soustraction tirées de l'exponentielle complexe, matrices par blocs (M25a) · température sur des probabilités, top-k et top-p comme lois conditionnelles (M28) · coût des comparaisons par paires, C(n, 2), contre un vecteur par élément (MB2)

**mymath** : `positional.py` (signatures figées) : `givens_rotation`, `online_softmax`, `merge_softmax_states`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B3.6 ∂ Pourquoi √d_k : variance du produit scalaire de deux vecteurs aléatoires · B3.7 ∂ RoPE : la rotation rend q_m · k_n fonction de m − n seulement · B3.1 ✏️ L'attention à la main : trois tokens, d_k = 2, scores, softmax et sortie · B3.2 ✏️ Le même calcul avec un masque causal · B3.3 ✏️ Suivre les formes dans l'attention multi-têtes et compter ses paramètres · B3.4 ✏️ Encodage sinusoïdal : quelques valeurs et l'effet d'un décalage de position · B3.5 ✏️ Compter les paramètres d'un GPT et retrouver les 124 millions de GPT-2 small · B3.8 🧮 Fermi : FLOPs d'entraînement (≈ 6 N D), ton mini-GPT sur CPU, GPT-3, et la mémoire du KV cache · B3.12 🔨 causal_mask, padding_mask et scaled_dot_product_attention · B3.13 🔮 Prédire la carte d'attention quand une clé copie la requête, puis quand on retire la division par √d_k · B3.14 🔨 split_heads, merge_heads et multi_head_attention · B3.15 🔨 positional_encoding et apply_rope · B3.17 🐛 Trois masques qui mentent : convention inversée, masque transposé, padding compté dans la loss · B3.27 🔬 Temps et mémoire de l'attention selon la longueur du contexte (64 à 2 048) · B3.29 🛠️ Un test pytest qui prouve la causalité : modifier le futur ne change pas les logits passés · B3.Q2 🧠 Requête, clé, valeur : un dictionnaire où l'on cherche « à peu près » · B3.Q3 🧠 Pourquoi diviser les scores par √d_k ? · B3.Q4 🧠 Masque causal : qui a le droit de regarder qui ? · B3.Q7 🧠 Sans encodage de position, l'attention voit-elle l'ordre des mots ? · B3.Q12 🧠 Coût quadratique du contexte et ce que change FlashAttention · B3.E2 💼 Quel est le coût de l'auto-attention en fonction de la longueur, et comment traite-t-on les contextes longs ? · B3.E5 💼 Pourquoi un Transformer a-t-il besoin d'encodages de position, et qu'apporte RoPE ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| MB3.Q1 | 🧠 | Formules d'addition et rotations du plan : le bon signe, composer, inverser, rotation ou symétrie ? | ★ | 5 | §1 §2 | C, E | manuel | — |
| MB3.Q2 | 🧠 | Rotations de l'espace, de Givens et par blocs : commutent-elles, que fixent-elles, que change une permutation des coordonnées ? | ★ | 6 | §3 | C, E | manuel | — |
| MB3.Q3 | 🧠 | Encoder une direction ou un jour de l'année : une ou deux coordonnées, quelle période, quelle distance entre deux encodages ? | ★ | 5 | §4 | C, E | manuel | — |
| MB3.Q4 | 🧠 | Moyennes pondérées par une softmax : dans l'enveloppe convexe ou non, largeur de bande, masque avant ou après la softmax, et un sous-ensemble vide | ★ | 4 | §5 §6 | C, E | manuel | — |
| MB3.Q5 | 🧠 | Multiplier tous les scores par c, ou leur ajouter une constante : ce qui change dans les poids, le poids maximal et l'entropie, et ce qui ne change pas | ★ | 5 | §7 | C, E | manuel | — |
| MB3.Q6 | 🧠 | La softmax en ligne : ce que garde l'état, quand le remettre à l'échelle, et l'état vide | ★ | 5 | §8 | C, E | manuel | — |
| MB3.R1 | 🔁 | La forme exponentielle d'un complexe, et le produit comme rotation et homothétie (M22) | ★ | 7 | §2 | C, E | manuel | — |
| MB3.R2 | 🔁 | Le log-sum-exp et la softmax stable (M05a) | ★ | 6 | §8 | C, E | manuel | — |
| MB3.R3 | 🔁 | Tempérer et tronquer une loi : p^{1/T} renormalisée, top-k et top-p comme lois conditionnelles (M28) | ★ | 7 | §5 §6 | C, E | manuel | — |
| MB3.1 | ✏️ | Un bras articulé à deux segments : la position de la pince en valeurs exactes par les formules d'addition, les deux rotations enchaînées en une seule, et le retour par la rotation inverse | ★★ | 28 | §1 §2 | C, E | wbm | — |
| MB3.2 | ✏️ | Rotations de Givens : deux rotations de l'espace qui ne commutent pas, deux rotations de ℝ⁴ dans des plans disjoints qui commutent, leur matrice diagonale par blocs, et la même rotation après une permutation des coordonnées | ★★ | 30 | §3 | C, E | wbm | — |
| MB3.3 | ✏️ | La direction du vent : l'encoder par (cos, sin), la distance entre deux encodages, un vent qui tourne comme une rotation de l'encodage, et la direction moyenne de trois relevés | ★★ | 22 | §4 | C, E | wbm | — |
| MB3.4 | ✏️ | L'estimateur de Nadaraya-Watson : la température d'un refuge à partir de quatre stations de montagne pondérées par un noyau gaussien de l'écart d'altitude, pour deux largeurs de bande, et ses deux limites | ★★ | 28 | §5 | C, E | wbm | — |
| MB3.5 | ✏️ | Masques : une moyenne exponentielle normalisée vue comme une softmax sur les jours passés, puis la même quand un capteur tombe en panne un jour (un score −∞) | ★★ | 16 | §6 | C, E | wbm | — |
| MB3.6 | ✏️ | La saturation d'une softmax : trois scores multipliés par un facteur c croissant, le poids maximal, la sensibilité 1 − Σ pᵢ² et la borne (K − 1) e^{−cΔ} | ★★ | 22 | §7 | C, E | wbm | — |
| MB3.7 | ✏️ | La softmax en ligne à la main : neuf scores (des multiples de ln 2) et leurs valeurs lus par blocs de trois, l'état (m, l, a) après chaque bloc, la moyenne pondérée finale, puis la fusion de deux états calculés séparément | ★★ | 30 | §8 | C, E | wbm | — |
| MB3.8 | ∂ | Les formules d'addition par le produit scalaire de deux vecteurs unitaires ; puis R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}, et la règle e^{iα}e^{iβ} = e^{i(α+β)} que M22 admettait | ★★ | 40 | §1 §2 | C, E | manuel | — |
| MB3.9 | ∂ | Une moyenne pondérée par une softmax sur un ensemble de points commute avec toute renumérotation des points ; un masque triangulaire casse cette équivariance | ★★ | 25 | §6 | C | manuel | — |
| MB3.10 | ∂ | La softmax en ligne est exacte : l'invariant de l'état après chaque bloc, par récurrence ; puis la fusion de deux états est associative et commutative, d'élément neutre (−∞, 0, 0) | ★★ | 30 | §8 | C, E | manuel | — |
| MB3.11 | 🔗 | Pont : à normes égales, les poids d'un noyau gaussien sont une softmax des produits scalaires divisés par h² ; le vérifier sur quatre stations d'un même cercle, et lire 1/h² comme l'échelle des scores | ★ | 22 | §5 §7 | C, E | wbm | — |
| MB3.12 | 📖 | MML §3.9 lu : la rotation du plan (3.76), les rotations de l'espace (3.77)–(3.79), la rotation de Givens (3.80)–(3.81) et les propriétés du §3.9.4 ; R₂(θ) écrite comme une rotation de Givens, et deux rotations de l'espace qui ne commutent pas, sur un vecteur choisi | ★★ | 40 | §2 §3 | C | manuel | — |
| MB3.13 | 🗣️ | Expliquer, avec une caisse tenue dans une monnaie qui change, pourquoi la softmax en ligne donne exactement le résultat du calcul en une fois | ★ | 15 | §8 | C, E | manuel | — |
| MB3.E1 | 💼 | « Comment encoder une variable cyclique comme une heure ou une direction, et pourquoi pas par sa valeur ? » | ★ | 10 | §4 | C, E | manuel | — |
| MB3.14 | 🔨 | La matrice d'une rotation de Givens de ℝⁿ · `givens_rotation` | ★ | 25 | §3 | C, E | pytest | — |
| MB3.15 | 🔨 | La softmax en ligne : l'état (m, l, a) de scores et de valeurs lus par blocs, et l'état après chaque bloc · `online_softmax` | ★★ | 50 | §8 | C, E | pytest | — |
| MB3.16 | 🔨 | La fusion de deux états de la softmax en ligne · `merge_softmax_states` | ★★ | 30 | §8 | C, E | pytest | MB3.15 |
| MB3.17 | 🔮 | Prédire ce que deviennent les poids et la prévision de Nadaraya-Watson quand la largeur de bande est divisée ou multipliée par 10, puis tracer | ★ | 30 | §5 §7 | C, E | wbm | — |
| MB3.18 | 🔬 | La softmax en ligne selon l'ordre et la taille des blocs : le nombre de remises à l'échelle (les états après chaque bloc) pour des scores croissants, décroissants ou mélangés, comparé à H_N − 1, et la mémoire gardée | ★★ | 30 | §8 §9 | C | wbm | — |
| MB3.19 | 🎨 | Trois horloges (la journée, la semaine, l'année) : l'encodage d'une date sur trois cercles, un décalage comme trois rotations, et le produit scalaire de deux encodages en fonction de l'écart | ★ | 30 | §4 | C, E | manuel | — |
| MB3.20 | 🐛 | Chasse à l'erreur : deux rotations de l'espace composées dans le mauvais ordre, une direction moyenne prise comme la moyenne des angles, une softmax en ligne qui remet l à l'échelle mais pas l'accumulateur | ★ | 25 | §3 §4 §8 | C, E | wbm | — |
| MB3.21 | 🛠️ | Un test de propriété : la softmax en ligne ne dépend ni de la taille des blocs, ni d'une même permutation des scores et des valeurs, ni d'une constante ajoutée aux scores, et la fusion de trois états est associative | ★ | 35 | §8 | C | manuel | MB3.15, MB3.16 |
| MB3.22 | 🏆 | Défi : prévoir la production d'une éolienne par Nadaraya-Watson sur l'encodage cyclique de la direction du vent et du jour de l'année, la largeur de bande choisie par validation croisée « un de côté », sous une erreur quadratique moyenne donnée | ★★★ | 45 | §4 §5 | C | wbm | — |

*Notes* : Frontières : les ∂ B3.6 (Var(q·k) = d_k pour des coordonnées centrées réduites, la division par √d_k, σ_q et σ_k, la moyenne μ non nulle (E = d_k μ², Var(q_c k_c) = 1 + 2μ²) et l'invariance par translation, deux clés (s, 0) et p = σ(s) avec s = 8 et s = 1, la division par d_k, pourquoi fixer 1/√d_k) et B3.7 (⟨R_mθ q, R_nθ k⟩ = ⟨q, R_(n−m)θ k⟩, le développement ⟨q, R_φ k⟩ = (q·k) cos φ + (q₂k₁ − q₁k₂) sin φ, les écarts ±3, la version diagonale par blocs en dimension d_h, les normes conservées, l'encodage additif et ses quatre termes, le KV cache) ; ✏️ B3.1 et B3.2 (l'attention à la main sur trois tokens, sans puis avec un masque causal, les colonnes qui ne somment pas à 1, la renormalisation oubliée), ✏️ B3.4 (valeurs de l'encodage sinusoïdal, une paire décalée, PE₀·PE₂, PE₁₀₀·PE₁₀₂), ✏️ B3.3 et B3.5 (les formes et les paramètres d'une attention multi-têtes et d'un GPT), 🔨 B3.14 (`split_heads`, `merge_heads`, `multi_head_attention`), 🧮 B3.8 (6ND, GPT-3, Chinchilla, KV cache), 🔨 B3.12 et B3.15 (les fonctions `mylearn` des masques, de l'attention, de l'encodage sinusoïdal et de RoPE), 🔮 B3.13 (une clé copiée, la bascule 1 + e^{7,5}, la log-normale, le maximum de gaussiennes), 🐛 B3.17 (trois masques qui mentent), 🔬 B3.27 (temps et mémoire de l'attention en échelles logarithmiques), 🛠️ B3.29 (un test qui prouve la causalité : modifier le futur ne change pas le passé), les quiz B3.Q2 (scores (0 ; 0 ; ln 3)), B3.Q3 (√d_k), B3.Q4 (les cases d'un masque causal), B3.Q7 (ordre, positions, angle de RoPE) et B3.Q12 (coût quadratique et FlashAttention), les entretiens B3.E2 (coût et contextes longs) et B3.E5 (positions et RoPE). MB3 enseigne les outils hors réseau : un bras articulé, des rotations de l'espace, la direction du vent, le calendrier d'une série de relevés (la journée, la semaine, l'année), des stations de montagne et un refuge, des capteurs dont un tombe en panne, des scores faits de n contributions, une caisse tenue dans une monnaie qui change, une éolienne ; jamais un token, une requête, une clé ni une valeur au sens de workbookIA (la fiche ne les nomme que dans ses encadrés 🔗 et dans « Et maintenant, dans workbookIA »), ni W_Q, W_K, W_V, une tête, une position m ou n, la base 10 000, d_k, un KV cache, un FLOP par token, un modèle de langue. Les rotations (§1 à §3) : les formules d'addition sont démontrées (∂ MB3.8, par le produit scalaire de (cos a, sin a) et (cos b, sin b), R9 ; M22 et M25a les tiraient d'une règle admise), puis R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ} et e^{iα}e^{iβ} = e^{i(α+β)} ; une même rotation conserve le produit scalaire (MML §3.9.4). Aucun exercice ni la fiche ne calculent le produit scalaire de deux vecteurs quelconques tournés d'angles différents, ne l'écrivent ⟨u, R_{β−α} v⟩ ni ne développent u·R_φ v en cos φ et sin φ (∂ B3.7.1 et B3.7.2) ; le seul produit scalaire de deux vecteurs tournés d'angles différents est celui de deux vecteurs unitaires (cos a, sin a)·(cos b, sin b) = cos(a − b), qui est la formule du §1. Le bras articulé (✏️ MB3.1) a deux segments et des angles de 30°, 45°, 60° ou leurs sommes, en valeurs exactes (ni les 112,5° ni la matrice (3.74) de MML, ni les vecteurs (2, 3) et (0, −1) tournés de 30° de l'exercice 3.10 de MML, conseillé seulement). Les rotations de Givens (✏️ MB3.2, 🔨 MB3.14, 📖 MB3.12) : deux rotations de l'espace dont les plans se coupent ne commutent pas, deux rotations de ℝ⁴ dans des plans disjoints commutent et forment une matrice diagonale par blocs ; PᵀRP est la même rotation dans d'autres plans de coordonnées, énoncé en général et calculé sur une permutation de ℝ⁴ qui n'envoie pas les paires de coordonnées voisines sur les moitiés : aucun exercice ne passe des paires voisines aux moitiés (FB3:430, ∂ B3.7.4), ni ne tourne chaque paire d'un angle proportionnel à un indice, ni ne prend des fréquences base^{−2i/d} (RoPE) ; le produit par blocs ([A₁ … A_H] [W₁ ; … ; W_H] = Σ A_h W_h) est enseigné sur des matrices quelconques, sans têtes ni concaténation de sorties (✏️ B3.3 et 🔨 B3.14 de workbookIA). Les horloges (§4) : une variable cyclique d'un calendrier ou d'une boussole, encodée par (cos ωt, sin ωt) ; le décalage comme rotation et le produit scalaire Σ_k cos ω_k(t − t′) de plusieurs horloges sont dans la fiche (la décision commune les demande, dans un cadre de séries temporelles) et dans le 🎨 MB3.19 (la journée, la semaine, l'année : une courbe de l'écart, sans vérifier sur deux paires de dates de même écart l'égalité de leurs produits scalaires, ✏️ B3.4 g–h et FB3:377-386) ; aucun exercice ne calcule à la main le produit scalaire de deux encodages à plusieurs horloges, ni des valeurs d'un encodage à fréquences géométriques (✏️ B3.4) ; les ✏️ n'ont qu'une horloge (la direction du vent, ✏️ MB3.3, avec ‖e(t) − e(t′)‖² = 2 − 2 cos ω(t − t′) sur d'autres nombres que cos = 0,8 et 0,4, B2.Q12) ; ni « position », ni 10 000, ni matrice PE. L'horloge de 24 h du 🎨 MB3.19 encode un instant du calendrier, à deux conditions : l'unité est l'heure d'une journée (jamais des « pas ») ; aucune série échantillonnée et bruitée, aucune fenêtre de 8 valeurs, aucune prédiction (ce que M22 évitait est le sinus de période 24 pas, bruité, de 22.14 de workbookIA). Les moyennes pondérées (§5) : la softmax de scores, l'estimateur de Nadaraya-Watson (noyau gaussien de l'altitude, ✏️ MB3.4 ; la largeur de bande comme une température, 🔮 MB3.17), et, dans le 🔗 MB3.11, des stations sur un même cercle (x·xᵢ = ρ² cos(φ − φᵢ)) : à normes égales, le noyau gaussien est une softmax des produits scalaires divisés par h² ; ni √d_k, ni projections, ni trois tokens. Les masques (§6) : un score −∞ est un conditionnement (M03, M28) ; la moyenne exponentielle normalisée comme une softmax sur le passé et un capteur en panne retiré (✏️ MB3.5, des fractions exactes) ; les cases d'un masque triangulaire, T(T + 1)/2, dans la fiche seulement (B3.Q4 a) ; « mettre un poids à 0 après la softmax ne donne pas une loi » est dans la fiche et au plus un vrai ou faux de 🧠 MB3.Q4, jamais une erreur à corriger (l'erreur fréquente de ✏️ B3.2) ; ni masque transposé, ni convention inversée, ni padding dans une loss (🐛 B3.17) ; la causalité d'un filtre (le futur ne change pas le passé) est énoncée dans la fiche, jamais vérifiée par un test (🛠️ B3.29). L'équivariance par permutation (∂ MB3.9) est démontrée en général, avec des matrices de permutation (M16), pour une moyenne pondérée sur un ensemble de points (des élèves, des capteurs) ; FB3:359 l'énonce sans preuve ; aucun quiz ne demande si l'on « voit l'ordre » sans encodage (B3.Q7 a–b), ni « le chien mord l'homme ». Les quiz : MB3.Q5 porte sur l'échelle comme une température (multiplier les scores, leur ajouter une constante), jamais sur l'écart-type d'une somme ni sur ce qu'est une softmax saturée (B3.Q3) ; MB3.Q6 ne demande pas si la softmax en ligne est exacte ou approchée, ni ce qu'elle réduit (la mémoire, pas les opérations : B3.Q12 b–c), et ne compte aucune paire (B3.Q12 a : le facteur f² sur le nombre de paires est dans la fiche seulement) ; MB3.Q4 ne demande ni la forme d'une sortie (B3.Q2 e), ni si une moyenne pondérée « voit l'ordre » (B3.Q7). L'échelle des scores (§7) : l'écart-type √(nv) d'une somme de n contributions indépendantes centrées et la division par √n sont dans la fiche seulement, sans exercice (B3.Q3 a) ; ✏️ MB3.6 ne garde que la saturation ; la variance d'un produit de deux variables indépendantes est un rappel de M16, jamais recalculée pour une somme de produits de coordonnées (∂ B3.6.1-2) ; la saturation porte sur K = 3 scores au moins, multipliés par un facteur c, mesurée par le poids maximal et 1 − Σ pᵢ² ; jamais deux scores (s, 0) et σ(s), ni la dérivée p(1 − p) d'une sigmoïde comparée entre deux échelles (∂ B3.6.5-6) ; la borne 1 − p_max ≤ (K − 1) e^{−cΔ} (Δ, l'écart entre le plus grand score et le suivant) est dans la fiche, avec son idée de preuve. Le point facultatif de la décision commune, E[e^{σZ}] = e^{σ²/2} et le maximum de n gaussiennes, n'est pas retenu : il ne sert qu'au corrigé du 🔮 B3.13 (frontière), et le budget n'en laisse pas la place. La softmax en ligne (§8) : l'état (m, l, a), écrit (m, l, acc) dans le code comme dans la fiche de workbookIA B3 ; la fiche de B3 montre le code sans preuve, MB3 démontre l'invariant et l'associativité de la fusion (∂ MB3.10) ; ✏️ MB3.7 prend neuf scores multiples de ln 2 (des exponentielles qui sont des puissances de 2, des sommes exactes) lus par blocs de trois ; le 🔬 MB3.18 compte les remises à l'échelle (des scores croissants : à chaque bloc ; au hasard : H_N − 1 en moyenne sur N blocs, les records, démontré dans la fiche par des indicatrices) ; la 🗣️ MB3.13 compare l'état à une caisse tenue dans une monnaie qui change ; ni 1 000 clés par blocs de 128, ni `default_rng(1)`, ni l'échelle 4,0. Le coût (§9) : une ligne rappelle MB2 §8 (C(n, 2) comparaisons contre n vecteurs) ; le § ne garde que ce qui est neuf, la mémoire n × n contre n·B par blocs et la pente 2 en échelles logarithmiques, sur des matrices de distances entre clients ou entre villes ; ni FLOPs par token, ni 24d², 4Td, T/(12d), 49 152, ni mesure du temps de l'attention (🔬 B3.27), ni Gio d'un modèle. Le 💼 MB3.E1 porte sur l'encodage d'une variable cyclique (une question de feature engineering), pas sur les positions d'un Transformer (B3.E5). Les exercices ne reprennent ni les exemples de la fiche de MB3 ni ceux du stub. Évités (règle de partage) — de workbookIA B3 : l'exemple d'attention à quatre clés de la fiche (q = (1, 0, 1, 0), clés (1, 1, 0, 0), (0, 1, 1, 0), (2, 0, 2, 0), (0, 0, 0, 2), valeurs (1, 0), (0, 1), (2, 2), (−1, 1), scores 0,5 ; 0,5 ; 2 ; 0, exponentielles 1,6487 et 7,3891, sommes 11,6865 et 10,6865, poids 0,1411 ; 0,6323 ; 0,0856, et masqués 0,1543 ; 0,6914, sorties (1,3201 ; 1,4912) et (1,5372 ; 1,5372)) ; les trois tokens (1, 0), (0, 1), (1, 1) et W_Q = [[0, 1], [1, 1]], W_K = [[1, 0], [1, 2]], W_V = [[1, −1], [0, 2]] de ✏️ B3.1-B3.2 (QKᵀ = [[0, 2, 2], [1, 3, 4], [1, 5, 6]], 3,536, 0,324, (0,676 ; 1,286), 0,727, 0,4458 et 0,1084, 0,202, 1,075 et 1,723, 2,0281 ; 34,3133 ; 69,5914, (0 ; 0,0008 ; 0,9992), (0,196 ; 0,804 ; 0), (0,196 ; 1,413), (0,0743 ; 0,3057 ; 0) et 0,38, x₂ = (2, 0) et 0,8943) ; q = (1, 3), k = (2, 2) et 5,66, les scores (0 ; 0 ; ln 3) et 0,6 ; d_k = 4, 16, 64, 256, 512, 1 024 et les écarts-types 2, 4, 8, 16, 23, 32, la simulation de 100 000 produits (4,03 ; 64,09 ; 514,18 ; 1,007 ; 1,001 ; 1,004), deux scores (s, 0) avec s = 8 ou 1 (0,99966 ; 3,35 × 10⁻⁴ ; 0,7311 ; 0,1966 ; les rapports 586 et 73), σ(0,125) ≈ 0,531, 1 + 2μ², ‖k‖² ; l'encodage d = 8, base 10 000, ω_i = 10⁻ⁱ, la période 200π ≈ 628, sin 25 ≈ −0,132, sin 2,5 ≈ 0,5985, cos 2,5 ≈ −0,8011, la paire (0,6 ; 0,8) décalée de 10 (angle 1 rad, (0,9974 ; −0,0726)) ou de −5 ((0,1430 ; 0,9897)), PE₀·PE₂ ≈ 2,5637, arcsin(0,6)/0,1 ≈ 6,435, 20π, cos > 0,995 ; d = 16, T = 50, PE₅·PE₉ = PE₂₀·PE₂₄ ≈ 5,56, PE_p·PE_p = 8, 64 positions en dimension 64, les périodes 2π ≈ 6,3 et 20 000 positions ; RoPE : θ = 0,5 rad, q = (1, 2), k = (3, −1), (m, n) = (0, 3), (4, 7), (10, 13), (7, 4), 7,0532 et −6,9117, cos 1,5 ≈ 0,0707 et 7 sin 1,5 ≈ 6,9825 ; θ = π/6, q = (2, 1), k = (1, 1), (0, 0), (5, 2), (1, 4), (7, 10) et 3, 1, −1, −1 ; θ = π/4, q = (1, 0), k = (0, 1), (0, 2) et −1 ; A = [[1, 2], [0, 1]], x = (1, 1) et (3, 1) ; i = 16, la position 250, θ = 10⁻², 2,5 rad ; les bases 10 000, 500 000 et 1 000 000 ; q = (1, 0, 0, 0) en position 1 et (cos 1, 0, sin 1, 0) ; les exemples du stub `attention` (`positional_encoding(3, 4)`, `apply_rope(np.ones((3, 4)))`, (−0,3012 ; 0,99 ; 1,3818 ; 1,0099), q = [[1, 0]], k = I, v = [[1, 2], [3, 4]], (0,6698 ; 0,3302) et (1,6605 ; 2,6605), `causal_mask(2, 4)`, `padding_mask([2, 3], 4)`, `np.arange(12.0).reshape(1, 2, 6)` et H = 3) ; les logits (2 ; 1 ; 0,5 ; 0 ; −1) à T = 0,8 et k = 3 (0,6945 ; 0,1990 ; 0,1065) ; la softmax en ligne sur 1 000 clés de dimension 16 et des valeurs de dimension 8, par blocs de 128, échelle 4,0, `default_rng(1)` ; 5 tokens et 15 cases, `causal_mask(1, 9)`, les longueurs [3, 5] ; les comptes de paramètres (4d² + 4d, 12d² + 13d, 591 360, 394 240, 344 960, 2 099 712, GPT-2 small et medium, BERT-base, le mini-GPT à 4 blocs, d = 128, V = 88 et 820 992, d = 384 et H = 6, d = 512 et H = 8 ou 16, d = 256 et F = 1 024) ; T = 12d et 49 152, 24d² et 4Td, H = 32 et T = 8 192 (8 Gio), 131 072 (2 Tio), 6ND, GPT-3, Chinchilla et 20 tokens par paramètre, Llama 3 405B, Qwen3-8B, les KV caches (16 Gio, 128 Kio, 144 Kio, 512 Kio), 1,5 To/s et 20 Mo, 64 à 2 048 tokens et 64 Mio ; 0,9⁵⁰ ≈ 0,0052, la layer norm de (1, 2, 3, 6), log 65 ≈ 4,17 et log 50 257 ≈ 10,825 ; la clé copiée de 🔮 B3.13 (d_k = 64, 200 requêtes, S de 10 à 100 000, 1 + e^{7,5} ≈ 1 800, e^{1/2}, 8√(2 ln 10⁵) ≈ 38) ; « le chat que Marie a adopté dort », « le chien mord l'homme », Holmes, Watson, Verne, Fashion-MNIST, les patchs d'un ViT (P = 16, 196 patchs) ; le cache de B3.Q11 (2 couches, d = 64, 100 tokens, float32, 102 400 octets) et les 15 % de 200 tokens de B3.Q9 (30, puis 80 % : 24). De workbookIA B1 et B2 (des cosinus et des softmax) : a₀ = (1, 0, 0), a₁ = (4, 2, 2), a₂ = (2, 1, 0), a₃ = (0, 1, 1), q = (2, 1, 1) ; les prototypes (0,9 ; 0,1), (0,7 ; 0,3), (0,2 ; 0,8), (0,4 ; 0,8), q = (0,6 ; 0,5), 0,900 et 0,869 ; les cosinus 0,31 ; 0,27 ; 0,22 avec s = 100 (0,982 ; 0,018 ; 0,0001) et s = 1 (0,348 ; 0,334 ; 0,318), et 0,24 ; 0,30 ; 0,28 ; 0,19 avec logit_scale 4,60517 et 2,6592 ; e₀ = (3, 0, 4), e₁ = (0, 3, 4), e₂ = (16, 2, 8), e₃ = (2, 1, 2), e₄ = (1, 0, 0), e₅ = (0, 1, 1), q = (1, 2, 2) ; le planning en cosinus (η = 10⁻³ ou 2 × 10⁻³, γ = 0,3 ou 0,5, t_w = 4 ou 5, 105 pas) ; cos = 0,8 et ‖a − b‖² = 0,4, √2 pour deux vecteurs orthogonaux, (3, 4) et (−6, −8) ; la moyenne avec masque de (1, 2), (3, 0), (2, 4), (0, 0) (2,0 et 1,5) ; les comptes 100 et 1 (0,969 et 0,031) ; les scores (1, 2, 3), (1001, 1002, 1003) et T = 0,5 des docstrings de `softmax` et `temperature_softmax` (workbookIA 17 et 22). De ce dépôt : la matrice (3.74) et les 112,5° de MML, les vecteurs (2, 3) et (0, −1) de l'exercice 3.10 de MML ; la rotation-homothétie de M22.3 (θ = 2π/3, r = 0,6, x₀ = (2, 0)) et z² − 0,24 de la fiche M22 ; la caméra de M25a (u = (1, 1, 0)/√2, 60°, 0,577 ; 0,816 ; 0,299) ; v = (710, 708, 700) de M05a et les exemples de `approx.logsumexp` ([0, 0], [1000, 1000]) ; les énergies (0 ; 0,5 ; 2) de M17 ; les exemples de `temper` et `smallest_mass_set` et le météorologue de M28.6 ; u = (3 ; −1) et v = (−2 ; 4) de la fiche R9 ; les exemples du stub `positional` (π/3 dans le plan (1, 3) de ℝ⁴, 1,2 dans le plan (2, 0) de ℝ³, les scores (0, ln 4, ln 2) et les valeurs (10, 20, 40), (−800, −801, −799), les états (0 ; 1,5 ; 3) et (ln 2 ; 1 ; 4), les scores (1, 3, 3, 0) et les valeurs (2, 6, 4, 5)), comme nombres et comme configurations (un second état fait d'un seul score à m + ln 2). Ajoutés par la relecture de la session 72 : de workbookIA, 1,4142 et les scores (0 ; 1,4142) de la variante de ✏️ B3.2, 0,879 (B1), la question « modifier le futur change-t-il le passé ? » de B3.Q4 c (même en consigne de copie), deux paires de même écart (✏️ B3.4 h, même avec une seule horloge), et l'erreur fréquente de ✏️ B3.2 (un poids mis à 0 sans renormaliser), ni en erreur fréquente, ni en valeur fausse, ni en flashcard ; de ce dépôt, M28 §4 (le produit en somme, 1 − cos ω = 2 sin²(ω/2), (1 + 2 cos ω)/3) et M28.5 a (2 − √3 ≈ 0,268, période 12), M09a §3 (Σ colonne × ligne), M11.13 (la somme harmonique), le 🗣️ M17.13 (les monnaies) et le refuge de M25a §5 (1 520 m, un baromètre). Conventions : angles en radians (en degrés dans un énoncé qui le dit), positifs dans le sens inverse des aiguilles d'une montre ; vecteurs en colonne, R_θ x ; une rotation de Givens tourne e_i vers e_j (MML (3.81) pour i < j), indices à partir de 1 dans la fiche et dans MML, à partir de 0 dans le code ; e^{iθ} = cos θ + i sin θ (la formule d'Euler, admise en M22, est ici une définition) ; une loi est une softmax d'un vecteur de scores, et un masque met un score à −∞ ; le noyau gaussien est exp(−‖x − xᵢ‖²/(2h²)), sa constante n'importe pas ; l'état de la softmax en ligne est (m, l, acc), l'état vide (−∞, 0, acc nul ou None), de même nature que les états qu'il complète ; logarithme népérien. `positional` : NumPy et `math` permis, aucune fonction de SciPy (`scipy.special.softmax`, `logsumexp`, `scipy.spatial.transform.Rotation` sont les oracles des tests) ni `np.logaddexp`. `givens_rotation` (MML §3.9.3) contient le cas du plan (n = 2) : `rotation_matrix_2d` et `rotate_complex` du plan sont retirées (une ligne chacune) ; `online_softmax(scores, values=None, block_size=1, history=False)` rend l'**état** (m, l, acc), pas des poids ni une sortie d'attention : elle ne prend ni requête, ni clés, ni masque, ni échelle (le contrat de `scaled_dot_product_attention` de workbookIA B3), et accepte des scores −∞ ; avec `history=True`, elle rend la liste des états après chaque bloc, ce qui rend testables l'invariant de ∂ MB3.10, la lecture par blocs de 🔨 MB3.15 et les remises à l'échelle du 🔬 MB3.18 ; l'état vide n'est neutre que pour les états de même nature (acc `None`, nombre ou tableau), et l ≥ 1 reste exigé quand m est fini (vrai exactement en flottants pour un état produit par `online_softmax` ou par une fusion) ; `merge_softmax_states` (la fusion associative, sans équivalent dans `mylearn`) ; aucune fonction de masque (`masked_softmax` serait le cœur de 🔨 B3.12), de positions, de fréquences base^{−2i/d} ni d'encodage (🔨 B3.15), ni `block_rotation` (appliquée à m·freqs, ce serait RoPE) ; Nadaraya-Watson s'écrit dans les exercices, sans fonction `mymath`. Aucune fonction n'a le nom ni le contrat d'une fonction de `mylearn` (`causal_mask`, `padding_mask`, `scaled_dot_product_attention`, `split_heads`, `merge_heads`, `multi_head_attention`, `positional_encoding`, `apply_rope`, `transformer_block` en B3 ; `softmax` de workbookIA 17 rend des poids, pas un état). MML : §3.9 lu (📖 MB3.12), avec un guide de lecture : §3.9.1 avant le §2 de la fiche, §3.9.2 à §3.9.4 avant le §3 ; MML ne démontre pas les formules d'addition (§3.9.1 lit les images de e₁ et e₂ sur la figure 3.16, §3.9.4 énonce la commutativité dans le plan sans preuve) et ne parle ni des horloges, ni des moyennes pondérées, ni de la softmax en ligne ; l'exercice 3.10 de MML est conseillé. COMPOSITION : 3 🔨 et aucun 📦 (au lieu de 4 🔨/📦) : les trois 🔨 écrivent tout `positional`, et les bibliothèques qui feraient un 📦 (`scipy.special.softmax`, `logsumexp`, `Rotation`) sont les oracles des tests ; un 📦 « la décomposition QR par des rotations de Givens, comparée à `np.linalg.qr` » (25 min) a été écarté pour tenir le budget. 10 ✏️/∂, 6 quiz, un 💼, 16 flashcards : le bas des fourchettes du §13. Parcours essentiel : le 📖, ∂ MB3.9 (l'équivariance, énoncée), le 🔬, le 🛠️ et le 🏆 hors parcours. **Durée** (session 69) : 12,8 h (essentiel 10,6 h ; lecture de la fiche 150 min, neuf sections) au lieu des 12 h visées (13,0 h avant les relectures, qui ont retiré trois sous-questions frontières) : neuf notions nouvelles, dont trois démonstrations (les formules d'addition, lacune de R9 à M28 ; l'équivariance ; l'invariant de la softmax en ligne), MML §3.9 lu, et des durées relevées comme celles de M25a à M28. Génération (session 72) : le critère du 🏆 MB3.22 est relatif (au plus 1,3 fois l'erreur quadratique moyenne de la méthode de référence, sur le jeu du notebook et trois éoliennes cachées de bruit faible, moyen et fort tirées à chaque exécution ; générateur et méthode dans `solutions/challenges/mb3_22.py`, hors du notebook) ; ∂ MB3.8 q. 6 (det R_θ et duplication) ; durées revues après la re-résolution à l'aveugle, l'auteur des exercices et l'apprenant simulé : exercices 708 min, 14,8 h en tout et 11,9 h en parcours essentiel.

<a id="mb4"></a>
## MB4 · Rang faible et recherche d'information

**Partie** VII · **prépare** workbookIA B4 · **dossier** `chapitres/mb4_rang_faible/` · **MML** (§4.6) · **sessions de génération** 1

Les maths du rang faible et de la recherche d'information : la factorisation de rang (une matrice de rang r est le produit de r colonnes par r lignes, à une matrice inversible près), ce qu'elle coûte à stocker et ses nombres libres, le rang effectif d'une matrice mesurée (rappel d'Eckart-Young) et l'ordre des produits ; le poids d'un indice rare, de la surprise au log du rapport des cotes de Robertson et Spärck Jones ; la saturation et la normalisation par la longueur, étudiées comme des fonctions ; la fusion de classements par les scores ou par les rangs (Borda, somme des 1/(c + rang)) ; enfin recall@k, precision@k, MRR et la ligne de base d'un ordre tiré au hasard. workbookIA B4 applique ces outils à LoRA, à BM25, à la recherche hybride et à l'évaluation d'un RAG.

**Temps** : 9,0 h en parcours complet, 6,0 h en parcours essentiel (lecture 95 min, 12 flashcards).

**Objectifs**

- Factoriser une matrice de rang r en un produit C F de r colonnes par r lignes, en trouver une autre, et compter les nombres stockés et les nombres libres.
- Démontrer que deux factorisations de rang diffèrent d'une matrice inversible, et que le rang est le plus petit nombre de produits extérieurs dont une matrice est la somme.
- Mesurer le rang effectif d'une matrice de mesures par l'énergie de ses valeurs singulières, et appliquer une matrice factorisée dans l'ordre le moins coûteux.
- Calculer le poids d'un indice rare comme une surprise et comme le log d'un rapport de cotes corrigé par ½, et dire quand il devient négatif.
- Étudier la saturation x ↦ x(k₁ + 1)/(x + k₁) et la normalisation par la longueur, et prévoir l'effet de k₁ et de b.
- Fusionner des classements par les rangs (Borda, somme des 1/(c + rang)), démontrer qu'ils ne dépendent pas de l'échelle des scores, et trouver quand une double présence bat une première place.
- Définir recall@k, precision@k, taux de succès et MRR, et calculer leur valeur moyenne pour un ordre tiré au hasard (k/n, H_n/n).

**Sections de la fiche**

- §1 La factorisation de rang : une matrice de rang r est un produit C F, et ce qu'elle coûte à stocker
- §2 Le rang effectif d'une matrice mesurée, et l'ordre des produits : C(Fx) plutôt que (CF)x
- §3 Le poids d'un indice rare : surprise, cote, et le log du rapport des cotes corrigé par ½
- §4 Saturation et normalisation par la longueur : deux fonctions d'un score de pertinence
- §5 Fusionner des classements : par les scores ou par les rangs, Borda et la somme des 1/(c + rang)
- §6 Mesurer un classement : recall@k, precision@k, MRR, et ce que donne le hasard

**Notions enseignées** : factorisation de rang : une matrice m × n de rang r est un produit C F, C fait de r colonnes indépendantes de la matrice (ses colonnes pivots), F de ses r lignes non nulles de forme échelonnée réduite (l'identité dans les colonnes pivots) ; le rang est le plus petit nombre de produits extérieurs dont la matrice est la somme (rang(CF) ≤ r : rappel de M12a) · non-unicité : (CG)(G⁻¹F) pour toute G inversible r × r, et rien d'autre ; stockage r(m + n) contre mn ; r(m + n − r) nombres libres (la forme de F en fixe r²) · rang effectif d'une matrice mesurée : part de l'énergie ‖·‖²_F captée par les r premières valeurs singulières (Eckart-Young, rappel de M12d), rang numérique et tolérance (rappel de M12a), rang stable ‖M‖²_F/‖M‖²₂ · appliquer une matrice factorisée : C(Fx) coûte r(m + n) multiplications, former CF en coûte mnr et l'appliquer mn ; le même résultat en exact (associativité), un écart d'arrondi en flottants (rappels de M09a et M05a) · le poids d'un indice rare : surprise −ln(n/N) (rappel de M06), cote n/(N − n), log du rapport des cotes de présence chez les pertinents et chez les autres (poids de Robertson et Spärck Jones), correction ½ ; sans information de pertinence, ln((N − n + ½)/(n + ½)), négatif si et seulement si n > N/2 ; la variante ln(1 + (N − n + ½)/(n + ½)) = ln((N + 1)/(n + ½)), toujours positive · saturation x ↦ x(k₁ + 1)/(x + k₁) : croissante, concave, égale à 1 en x = 1 pour tout k₁, de limite k₁ + 1 ; k₁ → 0 donne la seule présence, k₁ → ∞ le compte brut (la forme de Michaelis et Menten) ; normalisation par la longueur 1 − b + bℓ (ℓ : longueur rapportée à la moyenne), une interpolation affine en b · fusionner des classements : par les scores (sensible à l'échelle de chaque système) ou par les rangs (invariante par toute transformation strictement croissante des scores) ; méthode de Borda (la somme des rangs) ; somme des 1/(c + rang) : j-ième pour deux listes bat premier pour une seule si et seulement si j < c + 2 ; quand c grandit, l'ordre du nombre de listes puis de la somme des rangs (Borda pour des classements complets) ; la recherche dense par cosinus (rappel de M07) · mesurer un classement : recall@k, precision@k, taux de succès@k, rang réciproque et MRR (définitions) ; la ligne de base d'un ordre tiré au hasard : E[recall@k] = k/n, E[precision@k] = q/n, la loi du rang du premier pertinent, E[1/R] = H_n/n pour un seul pertinent, H_n encadré par ln(n + 1) et 1 + ln n (rectangles, rappel de M02a)

**Prérequis** : dénombrement, combinaisons, espérance d'une variable discrète et sa linéarité (R8) · ln et ses propriétés, la cote et le logit (R6) · limites, dérivée, sens de variation (R7) · sommes de Riemann, encadrer une aire par des rectangles (M02a) · precision et recall comme probabilités conditionnelles, l'AUC invariante par une transformation croissante des scores (M03) · lissage de Laplace (pseudo-comptes) (M04) · dérivée seconde et concavité, 1/(1 + u) ≈ 1 − u, nombres flottants et erreurs d'arrondi (M05a) · information −log p d'un événement, en nats (M06) · cosinus, plus proches voisins (M07) · facteur de Bayes (M08) · pivot de Gauss, forme échelonnée réduite et colonnes pivots, coût d'un produit et ordre des parenthèses dans ABC (M09a) · indépendance, base, coordonnées, rang, rang(AB) ≤ min(rang A, rang B), rang numérique et tolérance (M12a) · somme harmonique comparée à l'intégrale de 1/x (M11) · SVD, normes de Frobenius et spectrale, approximation de rang faible et son erreur (Eckart-Young), nombres stockés d'une image en rang k (M12d) · ordre des contractions de trois tableaux (M20) · répartir les valeurs singulières entre deux facteurs ; une cote multipliée par un rapport de sélection (MB2) · nombre harmonique H_n et records (MB3)

**mymath** : `ranks.py` (signatures figées) : `rank_factorization`, `borda_scores`, `random_ranking_mrr`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B4.6 ∂ LoRA : ΔW = BA de rang au plus r, B nulle au départ, gradients de A et de B, facteur α/r · B4.2 ✏️ Recall@k et MRR pour cinq requêtes · B4.3 ✏️ LoRA : paramètres entraînables d'une couche 896×896 de rang 8, puis de tout un modèle · B4.5 ✏️ BM25 à la main : trois documents, une requête de deux mots · B4.11 📄 Hu et coll. (2021) : « LoRA: Low-Rank Adaptation of Large Language Models » · B4.17 🔨 chunk_text et BM25 : découper un roman et classer ses passages · B4.18 🔨 cosine_top_k, fusion de classements (RRF), recall@k et MRR · B4.25 📦 LoRA from scratch : une couche LoRALinear en PyTorch, vérifiée contre peft · B4.27 🔬 Rang, alpha et modules ciblés : perplexité contre paramètres entraînables · B4.Q8 🧠 Évaluer un LLM : exact match, juge LLM, contamination des benchmarks · B4.Q9 🧠 BM25 ou recherche dense : qui retrouve « Watson » et qui retrouve « le docteur » ? · B4.Q11 🧠 LoRA : ce qui est gelé, ce qui est appris, ce que l'on fusionne · B4.R3 🔁 Les k plus proches voisins et le choix de la distance · B4.E3 💼 Explique LoRA et pourquoi c'est si économique

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| MB4.Q1 | 🧠 | Rang, factorisation et stockage : vrai ou faux, et le rang d'une somme de produits extérieurs | ★ | 5 | §1 §2 | C, E | manuel | — |
| MB4.Q2 | 🧠 | Le poids d'un ingrédient rare, la saturation et la normalisation : signe, sens de variation, limites | ★ | 5 | §3 §4 | C, E | manuel | — |
| MB4.Q3 | 🧠 | Fusionner des classements : ce que change une nouvelle échelle de notes, ce que change la constante c | ★ | 5 | §5 | C, E | manuel | — |
| MB4.Q4 | 🧠 | recall@k, precision@k, taux de succès et MRR : définitions, et leurs valeurs pour un ordre tiré au hasard | ★ | 5 | §6 | C, E | manuel | — |
| MB4.R1 | 🔁 | Le rang d'un produit, d'un produit extérieur et d'une somme (M12a) | ★ | 6 | §1 | C, E | manuel | — |
| MB4.R2 | 🔁 | L'approximation de rang k par la SVD et son erreur de Frobenius (M12d, MML §4.6) | ★ | 6 | §2 | C, E | manuel | — |
| MB4.R3 | 🔁 | L'information −ln p d'un événement, la cote et le logit (M06, R6) | ★ | 6 | §3 | C, E | manuel | — |
| MB4.1 | ✏️ | Les ventes de quatre boulangeries sur cinq produits : le rang, la factorisation par les colonnes pivots, une seconde factorisation (CG)(G⁻¹F), et les nombres stockés ou libres | ★★ | 35 | §1 | C, E | wbm | — |
| MB4.2 | ✏️ | Un tableau de relevés de stations météo donné par ses valeurs singulières : énergie captée, rang effectif à 99 %, rang stable, puis le coût de C(Fx) et de (CF)x pour un et pour mille vecteurs | ★★ | 25 | §2 | C, E | wbm | — |
| MB4.3 | ✏️ | Les ingrédients d'un carnet de recettes : surprise, cote, poids corrigé par ½ et son signe, la variante toujours positive, puis la saturation et la normalisation d'une mention répétée | ★★ | 30 | §3 §4 | C, E | wbm | — |
| MB4.4 | ✏️ | Trois jurys classent cinq pâtissiers : les points de Borda, la somme des 1/(c + rang) pour c = 2 et c = 10, et la somme des notes qui change de gagnant quand un jury passe de 20 à 100 points | ★★ | 35 | §5 | C, E | wbm | — |
| MB4.5 | ∂ | Une matrice de rang r est un produit C F de r colonnes par r lignes ; deux telles factorisations diffèrent d'une matrice inversible ; le rang est le plus petit nombre de produits extérieurs dont elle est la somme | ★★ | 30 | §1 | C, E | manuel | — |
| MB4.6 | ∂ | Une fusion par les rangs ne change pas quand un jury change d'échelle ; j-ième pour deux jurys bat premier pour un seul si et seulement si j < c + 2 ; quand c grandit, la somme des 1/(c + rang) range selon le nombre de listes, puis la somme des rangs | ★★ | 30 | §5 | C | manuel | — |
| MB4.7 | 🗣️ | Expliquer à un pâtissier pourquoi un ingrédient présent dans toutes les recettes n'aide pas à retrouver la sienne, et pourquoi la dixième mention compte moins que la première | ★ | 15 | §3 §4 | C, E | manuel | — |
| MB4.E1 | 💼 | « Comment combiner les classements de deux systèmes dont les scores ne sont pas sur la même échelle ? » | ★ | 10 | §5 | C | manuel | — |
| MB4.8 | 🔨 | La factorisation de rang C F : les colonnes pivots de M et les lignes non nulles de sa forme échelonnée réduite · `rank_factorization` | ★ | 30 | §1 | C, E | pytest | — |
| MB4.9 | 🔨 | Les points de Borda de classements complets, et le MRR exact d'un ordre tiré au hasard, en fractions · `borda_scores, random_ranking_mrr` | ★★ | 35 | §5 §6 | C | pytest | — |
| MB4.10 | 🔮 | Prédire le MRR d'un ordre tiré au hasard parmi 10, 100 puis 1 000 candidats, puis le simuler et le comparer à H_n/n | ★ | 20 | §6 | C | wbm | — |
| MB4.11 | 🎨 | Les courbes de saturation x ↦ x(k₁ + 1)/(x + k₁) de k₁ = 0 à l'infini, et ce que la normalisation par la longueur leur fait | ★ | 30 | §4 | C | manuel | — |
| MB4.12 | 🐛 | Chasse à l'erreur : C pris dans la forme réduite au lieu de M, un classement lu comme la liste des rangs des candidats, un poids de rareté écrit ln(n/N) | ★ | 20 | §1 §3 §5 | C | wbm | — |
| MB4.13 | 🏆 | Défi : retrouver le rang caché de cinq tableaux bruités, cinq fois sur cinq, par leurs valeurs singulières | ★★★ | 40 | §2 | C | wbm | — |

*Notes* : Frontières : le ∂ B4.6 (ΔW = BA de rang au plus r par les colonnes de B, le seuil r(d + k) < dk, soit r < dk/(d + k) et r < d/2 pour d = k, B nulle au départ et le point d'équilibre A₀ = B₀ = 0, les gradients s g(Ax)ᵀ et s Bᵀg xᵀ, le premier pas de rang 1, le facteur α/r, SGD ∝ s², Adam ∝ s, √r et rsLoRA), ✏️ B4.2 (recall@1, @3, @5, MRR et taux de succès@3 de cinq requêtes, « recall@3 n'est pas le taux de succès », recall@1 ≤ MRR), ✏️ B4.3 (paramètres LoRA de couches 896 × 896 et 896 → 128 de rang 8, d'un modèle entier, `all-linear`, le seuil 448), ✏️ B4.5 (BM25 à la main sur trois documents, classement, b = 0, k₁ = 0, idf original négatif), 📄 B4.11 (Hu et coll. : comptes de GPT-3, projection de W_q sur les directions singulières de ΔW, facteur d'amplification, rang intrinsèque), 🔨 B4.17 (`chunk_text` et `BM25`), 🔨 B4.18 (`cosine_top_k`, `reciprocal_rank_fusion`, `recall_at_k`, `mean_reciprocal_rank`, et son corrigé : k = 0 contre k = 60, rangs comptés à partir de 0), 📦 B4.25 (`LoRALinear`), 🔬 B4.27 (perplexité contre rang), les quiz B4.Q8 (80 % de 100 questions), B4.Q9 (3ᵉ dans deux classements, k = 60) et B4.Q11 (ce qui est gelé, r = 4 sur 512 × 512, α/r), le rappel B4.R3 (cosinus et distance de vecteurs unitaires) et l'entretien B4.E3 (expliquer LoRA). B4.Q5 et B4.13 (stratégies de décodage) sont des frontières de M28, qui les a préparés : MB4 n'y revient pas, et la fiche renvoie à M28 §5 pour la température, top-k et top-p. MB4 travaille hors réseau et hors des cadres de workbookIA : boulangeries et produits, relevés de stations météo, carnets de recettes et ingrédients, jurys de concours de pâtisserie, listes de diagnostics ou d'objets perdus ; jamais un LLM, une couche, un adaptateur, une matrice gelée, un passage indexé, un chunk, un embedding de phrase, un prompt ni un document de workbookIA. §1 (factorisation) : M = CF avec C les colonnes pivots de M et F les lignes non nulles de sa forme échelonnée réduite (la factorisation CR), la non-unicité (CG)(G⁻¹F), le stockage r(m + n) et les r(m + n − r) nombres libres (F a l'identité dans les colonnes pivots ; le compte redonne mn quand r = min(m, n)). rang(CF) ≤ r est un rappel de ∂ M12a.18, jamais redémontré (c'est ∂ B4.6.1) : ∂ MB4.5 démontre l'existence (une base de l'espace des colonnes et les coordonnées), la non-unicité à une G inversible près (même espace des colonnes) et en déduit que le rang est le plus petit nombre de produits extérieurs. Aucun exercice ni la fiche ne cherchent le rang à partir duquel la factorisation cesse de faire gagner de la place (le seuil de ∂ B4.6.1 et de ✏️ B4.3 j, la demi-moyenne harmonique dk/(d + k) ; M12d.5 en a déjà fait la version « image » : il n'est pas refait) : ✏️ MB4.1 compare des nombres pour un tableau et un rang donnés, sans pourcentage d'un « modèle », sans liste de couches, sans correction ajoutée à une matrice fixe, sans initialisation, gradient, facteur d'échelle ni « pas ». La fiche peut dire, sans nombre, que le même compte r(m + n) vaut pour une correction de rang r, et que workbookIA B4 l'applique (la fiche de M12d, qui promettait ce compte à MB4, est corrigée par le coordinateur). §2 : le rang effectif (part de l'énergie, plus petit rang pour une part donnée, rang stable) sur un tableau de mesures donné par ses valeurs singulières, l'erreur par Eckart-Young (rappel, M12d.16) ; pas de projection d'une matrice sur les sous-espaces singuliers d'une autre (📄 B4.11.8) ; C(Fx) contre (CF)x est le rappel de M09a.4 (ordre des parenthèses) appliqué à une matrice factorisée, avec l'arrondi des flottants (M05a), jamais W x + C(F x). Le 🏆 MB4.13 cherche un rang caché par un écart dans les valeurs singulières (un seuil de bruit σ(√m + √n) peut être énoncé dans un 💻, admis), sans refaire M12d.37 (une part d'énergie et une part de nombres imposées). §3 et §4 (le poids d'un indice rare, la saturation, la normalisation) : des ingrédients dans N fiches de recettes ; la surprise −ln(n/N) (M06), la cote, le poids de Robertson et Spärck Jones ln[p(1 − q)/(q(1 − p))] tiré d'un tableau 2 × 2 (pertinent ou non, présent ou non), la correction ½ de chaque case, le cas sans information de pertinence ln((N − n + ½)/(n + ½)) et son signe (démontré en général dans ✏️ MB4.3 : négatif si et seulement si n > N/2, nul pour n = N/2), la variante ln((N + 1)/(n + ½)) ; la saturation est étudiée comme une fonction (une prime qui plafonne, la cinétique de Michaelis et Menten), la propriété s(1) = 1 pour tout k₁ est énoncée sur la courbe, jamais sous la forme « une occurrence dans un document de longueur moyenne contribue exactement l'idf » (la variante du corrigé de 🔨 B4.17) ; la saturation et la normalisation sont chiffrées seules, comme des fonctions (valeurs en x = 1, 2, 10, rapport de la dixième mention à la première, effet de b sur une fiche deux fois plus longue) ; jamais leur produit par un poids de rareté (une contribution de BM25 : ✏️ B4.5 c-d, 🔨 B4.17), jamais le score d'une fiche à plusieurs ingrédients, jamais un classement de fiches ni une longueur moyenne calculée sur un corpus (✏️ B4.5, 🔨 B4.17) ; k₁ ∈ {1, 2, 3} et b ∈ {¼, ½}, jamais le couple k₁ = 1,5, b = 0,75 ni k₁ = 1,2. Les erreurs fréquentes du corrigé de ✏️ MB4.3 et le 🐛 n'ont aucune des erreurs listées par workbookIA pour ✏️ B4.5 et 🔨 B4.17 (le « 1 + » oublié, n compté en occurrences, k₁ + 1 oublié, la longueur moyenne sur la requête). §5 (fusion) : des jurys qui classent des pâtissiers (classements complets) ; la somme des notes brutes change de gagnant quand un jury change d'échelle, la fusion par les rangs non (∂ MB4.6, rappel de l'invariance de l'AUC, M03.23) ; Borda ; la somme des 1/(c + rang), avec une constante notée c (k dans workbookIA B4 et chez Cormack et coll. : la fiche le dit une fois ; dans MB4, k est la coupure de recall@k et k₁ la constante de saturation) ; ✏️ MB4.4 prend c = 2 et c = 10, jamais c = 0 ni 60 ; ∂ MB4.6 démontre en général la condition j < c + 2 (deux listes contre une) et la limite quand c grandit (développement 1/(c + j) = 1/c − j/c² + …, M05a), c = 0 n'y est qu'un cas limite, sans nombres ; la seconde partie de ∂ MB4.6 porte sur des jurys qui ne classent que leurs premiers (un candidat absent d'une liste ne reçoit rien de ce jury), en lettres, sans liste chiffrée, et la limite de sa troisième partie (le nombre de listes) aussi ; aucun exercice ne fusionne des listes de documents, des listes partielles chiffrées d'identifiants ni les résultats de deux moteurs (🔨 B4.18, B4.Q9) ; la recherche dense est un rappel de la fiche (cosinus, M07), sans exercice. Le 💼 porte sur des systèmes dont les échelles diffèrent, pas sur un RAG. §6 (mesurer un classement) : 🧠 MB4.Q4 définit recall@k, precision@k, taux de succès et MRR et calcule leur valeur moyenne pour un ordre tiré au hasard (k/n, q/n, H_n/n) ; il ne demande ni si recall@k est le taux de succès, ni si le MRR majore recall@1 (✏️ B4.2 f et h), et aucun exercice ne calcule ces mesures sur des listes de requêtes ; la loi du premier pertinent, E[1/R] et l'encadrement de H_n par des rectangles (M02a) sont dans la fiche, chiffrés dans 🔨 MB4.9 et le 🔮 MB4.10 (n = 10, 100, 1 000 : environ ln n / n) ; pas d'incertitude d'une proportion (B4.Q8, 📦 B4.20 : M08 suffit). Le 🐛 MB4.12 : C pris dans la forme réduite au lieu de M (CF ≠ M), un classement lu comme la liste des rangs des candidats (la permutation au lieu de son inverse), un poids de rareté écrit ln(n/N) ; jamais les erreurs du corrigé de 🔨 B4.18 (rangs à partir de 0, recall divisé par k, argsort inversé, identifiant répété). Notations : M (m × n) de rang r (k en M12d et MB2 ; k est ici la coupure de recall@k), C (m × r), F (r × n), produits extérieurs c fᵀ ; au §3, N fiches et n fiches qui contiennent l'ingrédient ; au §4, k₁ ≥ 0, ℓ la longueur rapportée à la moyenne, b ∈ [0, 1] ; au §5, des candidats, des rangs j à partir de 1, la constante c ≥ 0, n − j points de Borda ; au §6, n objets dont q pertinents, R le rang du premier pertinent, H_n = 1 + 1/2 + … + 1/n. `ranks` (pas `retrieval`, le nom du module `mylearn` de B4 : le « rang » d'une matrice et le « rang » dans un classement, les deux moitiés du chapitre) : NumPy permis, `@` compris, rien de `np.linalg`, ni SciPy (`scipy.linalg`, `scipy.stats.rankdata`), ni SymPy ; `random_ranking_mrr` calcule en `fractions.Fraction` avec `math.comb`, sans énumérer les n! ordres (l'oracle des tests). Aucune fonction n'a le contrat d'une fonction `mylearn` de B4 : pas d'idf ni de contribution BM25 (d'où le retrait de `idf` et de `bm25_term_score` ; `rsj_weight` n'est pas retenue : une formule d'une ligne, dont le cas r = R = 0 est l'idf original de ✏️ B4.5 i), pas de découpage, pas de `cosine_top_k`, pas de fusion triée de listes partielles (la RRF), pas de recall@k ni de MRR moyennés sur des requêtes ; `borda_scores` prend des classements complets et rend des points par candidat, `random_ranking_mrr` une espérance exacte sous un ordre tiré au hasard ; `rank_factorization` reprend le `rref` de M09a (l'apprenant peut l'importer de `.matrices` ou le recopier : 🔨 MB4.8 passe en ★, 20 min) et les colonnes pivots de `column_space_basis` (M12a), un rappel espacé assumé ; dans `borda_scores`, ni `np.argsort` ni `np.lexsort` : l'apprenant inverse chaque classement lui-même (le 🐛 MB4.12 vise cette inversion) ; `lora_param_count` est retirée (le nom de ∂ B4.6, un contrat d'une ligne). MML : §4.6 (l'approximation de rang k comme somme de k matrices de rang 1, Eckart-Young) a été lu en M12d (📖 M12d.22, questions 5 et 6) ; MB4 le donne en relecture dans son guide et le rappelle par 🔁 MB4.R2 ; le livre ne traite ni l'idf, ni la fusion de classements, ni les métriques de recherche (référence libre : Manning, Raghavan et Schütze, Introduction to Information Retrieval, ch. 6, 8 et 11, cités par chapitres). COMPOSITION : chapitre court (7 h visées, 7,6 h) : 4 quiz, 3 rappels, 4 ✏️ et 2 ∂, 2 🔨, un 🔮, un 🎨, un 🐛, un 🗣️, un 💼, un 🏆, 12 flashcards ; pas de 📖 (§4.6 lu en M12d, voir ci-dessus) ; pas de 🛠️ (le test de propriété CF = M est celui de 🔨 MB4.8) ; pas de 🔗 (un calcul « du type de workbookIA B4 » serait un compte de paramètres LoRA, un score BM25 ou une RRF : ses frontières) ; pas de 🔬 (le 🔮 simule). Parcours essentiel : les quiz, les rappels, les quatre ✏️, ∂ MB4.5, le 🗣️ et 🔨 MB4.8 ; ∂ MB4.6, le 💼 et le reste du notebook hors parcours. **Durée** : 7,6 h au lieu de 7 (+0,6 h : quatre lacunes, la factorisation de rang, l'origine probabiliste de l'idf, l'agrégation de classements et la ligne de base au hasard, et des durées réalistes après les relectures de M25a à M28) ; lecture 95 min (≈ 6 500 mots) ; sans 🎨 MB4.11 ni ∂ MB4.6, 7,0 h. Génération (session 73) : le 🏆 MB4.13 se vérifie sur trois séries de cinq tableaux cachés tirées à chaque exécution (les « cinq fois sur cinq » du titre), servies par `solutions/challenges/mb4_13.py` dans un processus à part ; le 🔮 MB4.10 g) rend les écarts en erreurs types ; durées revues après la re-résolution à l'aveugle, les auteurs et l'apprenant simulé : exercices 423 min, 9,0 h en tout et 6,0 h en parcours essentiel. Évités (règle de partage), de workbookIA B4 : les modèles et leurs nombres (Qwen2.5-0.5B, 494 032 768, 24 couches, 896, 14/2 têtes, 32 768 ; SmolLM2-135M, 30 couches, 576, 9/3, 64, 49 152, 8 192, 134 515 008 ; Qwen3, 596 049 920, 28, 1 024, 16/8 ; distilgpt2, 81 912 576, 6, 768, 12/12, 1 024, 81 986 304 ; MiniLM, 22 713 216, 384, 256 ; e5, 117 653 760, 512 ; 268 098 176 ; 1 235 814 400 ; GPT-3, 12 288, 96 couches, 175 255,8 millions) ; le top-5 0,205 ; 0,104 ; 0,086 ; 0,065 ; 0,058 ; 2 000 milliards de tokens, 1,3 et 175 milliards, 700 millions ; 988 065 792 et 1 976 131 328 octets, 114 688 octets par token, 3,76 Go, 1,19 Go, 12 288 octets (B4.R1) ; les formats 1/8/23 bits, 10^±38, 65 504, le groupe (0,12 ; −0,50 ; 0,31 ; 0,02), s = 0,50/127 et (30 ; −127 ; 79 ; 5) ; 64 tokens, 8,4/8,7 s, 7,6/13,9 s, 8 tokens/s, 200 tokens en 25 s ; le train pour Lyon (21 h 15, voie 7), le vote (Lyon, Lyon, Paris, Lyon, None) ; 540 et 100 milliards, 17,9 points, 76 points ; 30 questions annotées, 70 % sur 50 (0,065, ± 13 points), 70 % contre 76 %, 80 % de 100 (0,040), √(0,25/30) ≈ 0,09, ± 3,5 points sur 400 ; les troncatures 256 et 512 ; le découpage (13 mots en morceaux de 5 avec un recouvrement de 2, débuts 0, 3, 6, 9 ; 200 et 50 ; 120 et 20, 1 045 morceaux pour 104 500 mots, 21 mots ; « a b c d e f g h i j » (4, 2), « abcdefg » (3, 1)) ; les quatre documents « holmes fume sa pipe »… (N = 4, longueur moyenne 4,75, poids ln 2 et 0,3567, 3,5066, 0,4942, 2,3224, 0,7462, (0,3840 ; 0,7485 ; 1,1301 ; 0), [2, 1, 0, 3]) ; les trois documents « nemo commande le nautilus »… (longueurs 4, 3, 8, moyenne 5, ln(8/7) = 0,1335, ln(8/3) = 0,9808, 0,1628, 0,1599, 1,2246, 0,1908, 1,1144, 0,5108, −1,9459, −1,577, et la variante 1,2137 ; 0,1597 ; 0,1571 ; 0,1643) ; le corpus « the cat sat / the dog sat down / a cat and a cat » (moyenne 4,0, 0,47, 0,9808, (0,5296 ; 0 ; 0,6215), (1,0592 ; 0,47 ; 0,6215)) et « violin music concert » (6,55 ; 5,87 ; 5,48 ; 5,83 ; 5,47) ; k₁ = 1,5 avec b = 0,75, k₁ = 1,2, « 1,2 à 2 » ; 20 à 100 résultats ; D = [[1, 3], [3, 1], [1, 0], [−1, −1]] et la requête (1, 1) (0,8944 ; 0,7071 ; 0,1056), les documents [[1, 0], [0, 1], [1, 1], [−1, 0]] et la requête (1 ; 0,2) (0,9806 ; 0,8321) ; a = (3, 4), b = (6, 8), cos 0,82 → 0,36, 50 000 × 768, 10 000 morceaux de dimension 384 ; la fusion avec k = 60, les classements [7, 2, 9, 4], [2, 5, 7, 1], [9, 7, 3] et [3, 1, 2], [1, 2, 4] ([2, 7, 5, 9, 1, 4], [7, 2, 9, 5, 3, 1, 4], [1, 2, 3, 4], [1, 3, 2, 4]), 1/62 + 1/61, 1/61 + 1/63, 2/63 = 0,0317, 1/61 ≈ 0,0164, k = 0 → 1,5 et 1,33 ; les trois questions (4, 8, 1, 3) {1}, (2, 6, 5, 0) {2, 9}, (7, 3, 0, 5) {6} (1/6, 0,5, 4/9), les cinq de ✏️ B4.2 ((3, 1, 4, 0, 2) {1}, (5, 9, 2, 6, 8) {2, 8}, (0, 7, 1, 2, 3) {0, 5}, (6, 4, 8, 9, 1) {7}, (2, 0, 9, 3, 7) {3, 4, 9} ; 0,100 ; 0,467 ; 0,633 ; 0,433 ; 0,800 ; 0,533 ; 0,267) et celles des docstrings ([[3, 1, 2], [0, 4, 5, 6]] avec [{1, 7}, {6}] : 0,25, 0,75, 0,375 ; [{9}, {0}] : 0,5) ; recall@5 0,533 / 0,517 / 0,600 et MRR 0,452 / 0,500 / 0,523 ; 400 M, 100 mots, 21 millions, 5 ou 10 passages, k de 3 à 10, 20 documents et 56,1 % ; 16 octets par paramètre (2 + 2 + 4 + 4 + 4), 9,5 Go, 7 milliards → 28 et 14 Go ; le rang 1 (1, 2, 3)ᵀ(2, 0, 1) = [[2, 0, 1], [4, 0, 2], [6, 0, 3]] et « 9 nombres, 6 suffisent », g = (1, 2) et u = (3, 0, 1), l'application de ∂ B4.6 (d = 3, k = 2, r = 1, α = 2, A₀ = (1, −1), x = (2, 1), g = (1, 0, −2), η = 0,1 ; (2, 0, −4), (−0,2 ; 0 ; 0,4), (−4, −2)) ; les formes et rangs de LoRA (512 × 512 et r = 4 → 4 096 sur 262 144 ; 896 × 896, 896 → 128, 896 → 4 864 et r = 8 → 14 336, 45 056, 1 081 344, 4 399 104, 540 672, 448 ; 1 024 → 2 048 et r = 16 → 49 152 sur 2 097 152 ; 4 096 × 4 096 et r = 8 → 65 536 au lieu de 16 777 216 ; d, k, r, α = 6, 4, 2, 4 ; 64 → 64 et 64 → 16, r = 4, α = 8 → 832, 1 472, 1 664 ; 12 → 10 ; 768 × 2 304 ; r = 16, α = 32, 4 587 520 sur 600 637 440 ; 73 728 ; 38 019 et 38 404 ; r de 1 à 64, 18 432 → 1 179 648, 202 752, 294 912 ; 18 874 368, 37 748 736, 37,7 Mo, 4 718 592 ; r = 16 et α = 8 → 0,5 ; α/√r, 8/√64) ; 0,32 / 21,67 / 0,02, 6,91 et 21,5 ; les perplexités 48,34 → 37,81 et 40,07 à 34,62 ; 0,820 et 0,868 ; 17/30, K = 4, 12/30 ; 0,8¹⁵ ≈ 0,035 ; 1 € et 4 € par million, 1 700 et 23 € ; 3 000 questions, 1 540 tokens ; Holmes, Watson, Baker Street, le violon et la pipe, Verne, le Nautilus et Nemo, « AX-7731 », 20 Newsgroups. De ce dépôt : R6.12 (N = 2 000 documents, présents dans 20 et 200, tf 2 et 5), R9.13 (les vecteurs d'ingrédients des crêpes, du quatre-quarts, des sablés et du pain au lait), M12d.5 (900 × 1 600, k = 40), M12d.37 (93,5 % de l'énergie, 5 % des nombres), M03.23, les exemples des stubs `matrices`, `linmaps` et `svd_pca`, et ceux du stub `ranks` ([[1, 3, 0, 1], [0, 0, 1, −1], [2, 6, 1, 1]], [[2, −4], [−3, 6]], [[2, 0, 1], [0, 2, 1], [2, 1, 0]] → (3, 1, 5), [[3, 1, 0, 2]], 25/48, (5, 2) → 77/120, (4, profondeur 2) → 3/8), que ni la fiche ni les exercices ne reprennent ; et les Évités de M28 (température, top-k, top-p).

<a id="mb5"></a>
## MB5 · Les maths de la diffusion

**Partie** VII · **prépare** workbookIA B5 · **dossier** `chapitres/mb5_diffusion/` · **MML** (§6.5) · **sessions de génération** 2

Les outils mathématiques des modèles de diffusion, travaillés hors réseaux : les récurrences linéaires gaussiennes (la loi sachant le départ, les produits cumulés, la loi stationnaire d'un processus autorégressif), le pont d'une marche aléatoire et des trajectoires différentes aux mêmes lois marginales, le rapport signal sur bruit (cotes, logit, décibels) et les cibles qui portent la même information ; la MSE qui apprend l'espérance conditionnelle, le score en x et la formule de Tweedie (le débruiteur optimal) ; l'ELBO d'une chaîne de variables latentes, démontrée ; la guidance comme produit de puissances de densités ; les équations différentielles (méthode d'Euler, point milieu, ordre de l'erreur) et le flow matching en dimension 1. workbookIA B5 s'en sert pour la forme fermée et les plannings du processus de bruitage, la loss de prédiction du bruit, l'ELBO de la diffusion, DDIM, la guidance sans classifieur et le flow matching.

**Temps** : 16,6 h en parcours complet, 13,0 h en parcours essentiel (lecture 160 min, 20 flashcards).

**Objectifs**

- Calculer la loi de x_t sachant x_0 ou sachant x_s pour une récurrence linéaire gaussienne à coefficients quelconques, encadrer le produit cumulé de ses coefficients, et trouver la loi stationnaire d'un processus autorégressif d'ordre 1.
- Calculer la loi d'un instant sachant deux instants qui l'encadrent (le pont d'une marche aléatoire), et construire des trajectoires différentes qui ont les mêmes lois marginales.
- Passer du rapport signal sur bruit à la part de variance du signal (cotes, logit, décibels), et d'une estimation du bruit à une estimation du signal, avec l'erreur qui l'accompagne.
- Démontrer que l'erreur quadratique moyenne est minimale pour l'espérance conditionnelle, et en lire les conséquences sur une cible à plusieurs modes.
- Définir le score en x d'une densité, démontrer la formule de Tweedie, calculer le débruiteur optimal d'un signal gaussien ou d'un mélange, et dire comment la dynamique de Langevin tire des points d'une densité à partir de son score.
- Démontrer la décomposition de l'ELBO d'une chaîne de latents en reconstruction, KL finale et KL des pas retour, et la calculer sur une petite chaîne discrète.
- Écrire une combinaison affine de scores comme le score d'un produit de puissances de densités, et calculer la loi guidée de deux gaussiennes avec sa condition d'existence.
- Suivre une équation différentielle par la méthode d'Euler et par celle du point milieu, dans les deux sens du temps, et relier l'erreur au pas et à la courbure de la trajectoire.
- Calculer le champ moyen d'un chemin droit entre un bruit et des données gaussiennes de dimension 1, et le suivre pour transporter le bruit sur la loi des données.

**Sections de la fiche**

- §1 Récurrences linéaires gaussiennes : la loi sachant le départ, les produits cumulés et la loi stationnaire
- §2 Conditionner sur deux instants, changer de couplage : le pont d'une marche aléatoire, et des trajectoires différentes aux mêmes lois marginales
- §3 Signal et bruit : rapport signal sur bruit, cotes et décibels, et trois cibles qui portent la même information
- §4 La MSE apprend l'espérance conditionnelle
- §5 Le débruiteur optimal : le score en x, la formule de Tweedie, et la dynamique de Langevin (aperçu)
- §6 L'ELBO d'une chaîne de variables latentes
- §7 Guider : combinaisons affines de scores et produits de puissances de densités
- §8 Équations différentielles : la méthode d'Euler, le point milieu, et l'erreur selon la courbure
- §9 Le flow matching en dimension 1 : un chemin droit, un champ moyen, et le transport d'une loi

**Notions enseignées** : rappels de M25a et de M25b, sans les refaire : somme et image affine de gaussiennes indépendantes, produit de deux densités gaussiennes, modèle linéaire gaussien et loi conditionnelle, KL entre deux gaussiennes de même covariance ; espérance et variance conditionnelles, lois totales, responsabilités en log, ELBO d'un latent · récurrence linéaire gaussienne x_t = a_t x_{t−1} + b_t ε_t à coefficients quelconques : x_t est une image affine du vecteur gaussien (x_0, ε_1, …, ε_t) ; loi de x_t sachant x_0, de moyenne (a_1 ⋯ a_t) x_0 et de variance Σ_k b_k² (a_{k+1} ⋯ a_t)² ; pour un coefficient constant, la loi sachant x_s ; propagation des moments m_t = a_t m_{t−1}, v_t = a_t² v_{t−1} + b_t² (la prédiction d'un filtre de Kalman de dimension 1) · produits cumulés : ln Π = Σ ln ; 1 − h ≤ e^{−h} (convexité, M05a) et ln(1 − h) ≥ −h − h² pour 0 ≤ h ≤ ½, d'où e^{−Σh_k − Σh_k²} ≤ Π(1 − h_k) ≤ e^{−Σh_k} ; risque cumulé et probabilité de survie à des risques successifs · processus autorégressif d'ordre 1, x_t = a x_{t−1} + b ε_t : pour |a| < 1, loi stationnaire N(0, b²/(1 − a²)) (somme géométrique, R5) et convergence depuis toute loi initiale (l'écart de moyenne en |a|^t, celui de variance en a^{2t}) : le processus oublie son départ ; pour |a| ≥ 1, pas de loi stationnaire (marche aléatoire, a = 1 : variance t b²) ; une chaîne de Markov à états continus (suite de M26) · pont d'une marche aléatoire (a = 1) : loi de x_s sachant x_0 et x_T par le modèle linéaire gaussien de M25a ; moyenne interpolée selon les variances cumulées V_s/V_T, variance V_s(V_T − V_s)/V_T, maximale au milieu pour des pas égaux · lois marginales et couplages : deux processus peuvent avoir la même loi à chaque instant et des trajectoires différentes ; si U et Z sont indépendants de loi N(0, 1) et 0 ≤ σ ≤ s, alors √(s² − σ²) U + σ Z suit N(0, s²) ; réutiliser un seul tirage (des trajectoires déterministes) ou ajouter un bruit frais ; la corrélation entre deux instants n'est pas fixée par les marginales ; une loss qui ne voit qu'un instant à la fois ne dépend que des lois marginales (énoncé) · rapport signal sur bruit d'une mesure y = a x + b n (x et n indépendants, de variance 1) : SNR = a²/b², part de variance du signal γ = a²/(a² + b²), SNR = γ/(1 − γ) (une cote), ln SNR = logit γ (R6), décibels 10 log₁₀ SNR ; un seuil r de SNR correspond à γ = r/(1 + r) ; c·y a le même SNR que y · trois cibles qui portent la même information : connaissant y, estimer le bruit n ou le signal x revient au même, x̂ = (y − b n̂)/a ; l'erreur sur x vaut l'erreur sur n divisée par √SNR ; une MSE sur x est une MSE sur n pondérée par 1/SNR ; toute combinaison c x + d n non proportionnelle à y convient aussi · la meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + E[(E[Y | X] − g(X))²], le terme croisé s'annulant par la propriété de la tour (M26) ; la MSE apprend l'espérance conditionnelle, et son minimum est E[V(Y | X)] ; sur un échantillon, la moyenne de chaque groupe ; une cible à deux modes donne une prédiction entre les modes ; la log-loss apprend la probabilité a posteriori (rappel de M27), la MAE une médiane conditionnelle (énoncé) · score d'une densité en x, ∇ₓ ln p(x) = ∇p(x)/p(x) : il pointe vers les régions plus probables, s'annule en un mode et ignore la constante de normalisation ; pour N(μ, σ²), −(x − μ)/σ² ; à ne pas confondre avec le score en θ, ∇_θ ln p_θ(x), de MB8, ni avec le score d'un classement ou d'un classifieur (le sens courant de MB2, MB3, MB4 et MB6) · formule de Tweedie : pour y = a x + b n, avec n de loi N(0, 1) indépendant de x de loi quelconque, E[x | y] = (y + b² (ln p_Y)′(y))/a et E[n | y] = −b (ln p_Y)′(y) (démontrée en dimension 1 en dérivant p_Y sous l'espérance, énoncée en dimension d avec le gradient) ; estimer le bruit, c'est estimer le score de la loi bruitée · débruiteur optimal d'un mélange de gaussiennes : responsabilités en log (une softmax, M25b) et moyennes a posteriori de chaque composante (M25a) ; pour un nuage de points (variances nulles) et a ≠ 0, il rend le point le plus proche de y/a quand le bruit tend vers 0 (il recopie les données ; à égale distance de deux points, une moyenne pondérée des deux) ; pour a = 0, la moyenne du nuage · dynamique de Langevin (aperçu) : x_{k+1} = x_k + (h/2) (ln p)′(x_k) + √h ε_k, une chaîne de Markov à états continus dont la loi stationnaire approche p quand h → 0 ; pour p = N(μ, σ²), c'est un processus autorégressif d'ordre 1 (§1) de coefficient 1 − h/(2σ²) et de loi stationnaire N(μ, σ²/(1 − h/(4σ²))) : partir d'un bruit et laisser converger la chaîne fabrique des tirages de p · ELBO d'une chaîne de latents : un processus aller q(z_1 | x) q(z_2 | z_1) ⋯ q(z_T | z_{T−1}), markovien et fixé, un modèle retour p(z_T) p(z_{T−1} | z_T) ⋯ p(x | z_1) ; chaque pas aller réécrit par Markov et Bayes, q(z_t | z_{t−1}, x) = q(z_{t−1} | z_t, x) q(z_t | x)/q(z_{t−1} | x), puis le télescopage : ELBO = E_q[ln p(x | z_1)] − KL(q(z_T | x) ‖ p(z_T)) − Σ_{t≥2} E_q[KL(q(z_{t−1} | z_t, x) ‖ p(z_{t−1} | z_t))] (démontrée, suite de M25b §5) · lecture des termes : une reconstruction, une KL finale sans paramètre quand p(z_T) est fixée, et pour chaque pas retour une KL contre le pas retour qui connaît x ; quand ces lois sont gaussiennes de même variance fixée σ², chaque KL vaut ‖μ_q − μ_p‖²/(2σ²) (M25a §7) : une MSE pondérée des moyennes, dont une loss simplifiée retire les poids (idée) · combinaison affine (1 + w) u − w v = u + w (u − v) : w ∈ [−1, 0] interpole, w > 0 extrapole au-delà de u, à l'opposé de v (un barycentre à coefficients hors de [0, 1], M07) · Bayes en log : ∇ₓ ln p(x | c) − ∇ₓ ln p(x) = ∇ₓ ln p(c | x) ; (1 + w) ∇ ln p_c − w ∇ ln p_u = ∇ ln(p_c^{1+w} p_u^{−w}) : une combinaison affine de scores est le score d'un produit de puissances de densités, p_c · p(c | x)^w à une constante près · produit de puissances de deux densités gaussiennes de dimension 1 : précision (1 + w)/σ_c² − w/σ_u², positive pour tout w ≥ 0 si σ_c ≤ σ_u, sinon jusqu'à un w limite au-delà duquel il n'y a plus de densité ; moyenne poussée au-delà de μ_c, à l'opposé de μ_u ; loi plus étroite que p_c quand σ_c < σ_u, plus large sinon ; avec une loi générale à plusieurs bosses, la masse quitte les autres bosses · équation différentielle x′(t) = f(t, x) à champ dépendant du temps : condition initiale, trajectoire, existence et unicité pour f lipschitzienne en x (théorème de Cauchy-Lipschitz, énoncé) ; solutions exactes de x′ = g(t) (une primitive), du refroidissement x′ = −k(x − c) et de la croissance logistique · méthode d'Euler pour un champ dépendant du temps (suite de M20 §6), dans les deux sens du temps (un pas négatif pour remonter) ; exacte pour une vitesse constante le long de la trajectoire ; erreur d'un pas ½ h² x″(ξ) (Taylor, M05a), qui vient de la courbure ; erreur au temps final d'ordre h (énoncée, avec l'idée de l'accumulation de T/h erreurs locales) ; pour x′ = g(t), Euler est la somme de Riemann à gauche et le point milieu la règle du point milieu (M02a) · méthode du point milieu : un demi-pas d'Euler, puis la vitesse lue au milieu ; deux évaluations du champ par pas, exacte pour une vitesse affine en t, erreur d'ordre h² (énoncée) ; comparer deux méthodes à nombre d'évaluations égal ; pentes 1 et 2 en échelle log-log · chemin droit entre une donnée x_0 et un bruit ε, x_s = (1 − s) x_0 + s ε (s = 0 : la donnée, s = 1 : le bruit) : vitesse ε − x_0, constante sur chaque chemin ; une mesure de gains 1 − s et s, de SNR ((1 − s)/s)² (§3) ; x_0 = x_s − s u et ε = x_s + (1 − s) u pour u = ε − x_0 · champ moyen v(x, s) = E[ε − x_0 | x_s = x] = (x − E[x_0 | x_s = x])/s, appris par la MSE (§4) et calculé par le débruiteur du §5 ; l'équation x′ = v(x, s), suivie de s = 1 à s = 0, transporte la loi de ε sur celle de x_0 (énoncé, vérifié pour des données gaussiennes) ; pour x_0 de loi N(m, τ²), v est affine en x, les trajectoires sont x(s) = (1 − s) m + σ(s) z avec σ(s)² = (1 − s)² τ² + s², courbes dès que τ > 0 ; un seul pas d'Euler depuis s = 1 rend m pour tout départ ; pour deux points, le champ n'est plus affine

**Prérequis** : somme télescopique (R4) · suite géométrique et sa somme, somme infinie (R5) · logarithme d'un produit, log₁₀, tanh, cote et logit (R6) · dérivée, tangente (R7) · primitive, intégrale, sommes de Riemann à gauche et au point milieu (M02a) · loi normale, densité, variance d'une transformation affine et d'une somme de variables indépendantes (M02b) · la moyenne et la médiane minimisent les écarts quadratiques et absolus (M02c) · formule de Bayes, probabilités totales (M04) · convexité : une fonction convexe est au-dessus de ses tangentes ; polynôme de Taylor d'ordre 2 et son reste ; ln(1 + x) ≈ x (M05a) · divergence KL discrète, entropie (M06) · barycentre ; la moyenne minimise la somme des carrés des écarts (M07) · inverse d'une matrice 2 × 2, ad − bc (M09a) · MSE, risque empirique (M09b) · feuille d'un arbre de régression, variance intra et inter (M13a) · (1 + x/n)ⁿ → eˣ (M14) · méthode d'Euler pour x′ = F(x), application proche de l'identité (M20) · récurrence linéaire avec entrée ; Aᵗ → 0 quand le rayon spectral est inférieur à 1 (M22) · transformations affines et sommes de gaussiennes indépendantes, produit de deux densités gaussiennes, modèle linéaire gaussien, loi conditionnelle, KL continue et KL entre deux gaussiennes (M25a) · graphe orienté et chaîne, tirage ancestral, espérance et variance conditionnelles, lois totales, mélanges et responsabilités en log, ELBO d'un latent, dériver sous l'espérance (M25b) · chaîne de Markov, loi stationnaire, propriété de la tour (M26) · meilleur prédicteur pour la log-loss ; distance de Wasserstein entre deux lois de dimension 1 et entre deux gaussiennes (M27) · estimateur de Nadaraya-Watson, sa limite h → 0 (MB3)

**mymath** : `gaussian_paths.py` (signatures figées) : `linear_gaussian_recursion`, `posterior_mean_mixture`, `euler_ode`, `midpoint_ode`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B5.6 ∂ Forme fermée : deux pas de bruit gaussien n'en font qu'un, d'où q(x_t | x_0) · B5.7 ∂ Moyenne et variance du posterior q(x_{t−1} | x_t, x_0) en dimension 1 · B5.1 ✏️ Guidance sans classifieur : combiner les deux prédictions pour w = 0, 1 et 3 · B5.2 ✏️ Planning linéaire : β_t, α_t et ᾱ_t pour T = 4, puis ᾱ_T pour T = 1 000 · B5.3 ✏️ Rapport signal sur bruit : à quel pas un chiffre devient-il illisible, planning linéaire ou cosinus ? · B5.4 ✏️ Un pas DDPM à la main, en dimension 1, avec un bruit prédit donné · B5.5 ✏️ Un pas DDIM à la main et l'image estimée x̂_0 · B5.11 📄 Ho, Jain et Abbeel (2020) : « Denoising Diffusion Probabilistic Models » · B5.12 🔨 linear_beta_schedule, cosine_beta_schedule et noise_schedule · B5.13 🔮 Prédire l'allure d'un chiffre bruité aux pas 100, 300 et 600, planning linéaire puis cosinus · B5.14 🔨 q_sample : bruiter un batch d'images à des pas différents · B5.15 📈 Lire ᾱ_t, le rapport signal sur bruit et la grille de bruitage des deux plannings · B5.16 🔨 q_posterior_mean_variance et predict_x0_from_eps · B5.17 🔨 ddpm_step et ddim_step · B5.18 🔬 Avec le vrai bruit, DDPM et DDIM retrouvent-ils x_0 ? Contrôle sur des données 2D · B5.20 🔬 Flow matching en 2D : même MLP, cible « vitesse » et intégration d'Euler · B5.22 🐛 Le DDPM qui ne produit que du gris : quatre bugs d'indices, de racines et d'échelle · B5.26 🔮 Prédire l'effet de w = 0, 1, 3 et 7 sur la netteté et la diversité · B5.28 🔬 Mémorisation : plus proches voisins des échantillons, entraînement sur 500 images contre 60 000 · B5.Q2 🧠 Pourquoi détruire l'image en mille petits pas de bruit plutôt qu'en un seul ? · B5.Q3 🧠 ᾱ_t : quelle part de l'image reste-t-il au pas t ? · B5.Q4 🧠 Prédire le bruit, l'image ou la vitesse : la même information ? · B5.Q8 🧠 DDIM : moins de pas avec le même réseau, vrai ou faux · B5.Q9 🧠 Guidance sans classifieur : ce que règle l'échelle w · B5.Q11 🧠 Diffusion latente, transformers de diffusion, flow matching : ce qui a changé depuis 2020 · B5.R3 🔁 L'astuce de reparamétrisation et le terme KL du VAE · B5.E2 💼 Pourquoi le réseau prédit-il le bruit plutôt que l'image ? · B5.E4 💼 Qu'est-ce que la guidance sans classifieur et quel compromis règle-t-elle ? · B5.E5 💼 Diffusion ou flow matching : qu'est-ce qui a changé dans les générateurs récents ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| MB5.Q1 | 🧠 | Une récurrence linéaire gaussienne : quelle moyenne, quelle variance, quand une loi stationnaire, et combien de pas pour oublier le départ ? | ★ | 5 | §1 | C, E | manuel | — |
| MB5.Q2 | 🧠 | Le pont et les couplages : où l'incertitude est la plus grande, ce que fixent les lois marginales et ce qu'elles laissent libre | ★ | 5 | §2 | C, E | manuel | — |
| MB5.Q3 | 🧠 | Signal et bruit : SNR, cotes, logit et décibels, et ce qu'un changement d'échelle ne change pas | ★ | 4 | §3 | C, E | manuel | — |
| MB5.Q4 | 🧠 | Ce que la MSE apprend : une moyenne conditionnelle, pas la valeur la plus probable ; et ce qu'apprennent la MAE et la log-loss | ★ | 5 | §4 | C, E | manuel | — |
| MB5.Q5 | 🧠 | Le score en x : où il pointe, la constante qu'il ignore, et ce que dit la formule de Tweedie | ★ | 5 | §5 | C, E | manuel | — |
| MB5.Q6 | 🧠 | L'ELBO d'une chaîne : quels termes dépendent du modèle, quelle KL compare quoi, et ce que devient une KL entre gaussiennes de même variance | ★ | 5 | §6 | C, E | manuel | — |
| MB5.Q7 | 🧠 | Guider : interpoler ou extrapoler, la différence de deux scores, et quand un produit de puissances n'est plus une densité | ★ | 4 | §7 | C, E | manuel | — |
| MB5.Q8 | 🧠 | Euler, point milieu et chemin droit : ce que coûte un pas, l'ordre de l'erreur, et le sens du temps | ★ | 5 | §8 §9 | C, E | manuel | — |
| MB5.R1 | 🔁 | Sommes et images affines de gaussiennes, produit de densités et modèle linéaire gaussien (M25a) | ★ | 6 | §1 §2 | C, E | manuel | — |
| MB5.R2 | 🔁 | Espérance et variance conditionnelles, lois totales, et l'ELBO d'un latent (M25b) | ★ | 6 | §4 §6 | C, E | manuel | — |
| MB5.R3 | 🔁 | Un pas d'Euler (M20), la loi stationnaire d'une chaîne finie (M26) et la cote d'une probabilité (R6) | ★ | 6 | §1 §3 §8 | C, E | manuel | — |
| MB5.1 | ✏️ | L'anomalie de température d'un lac, un processus autorégressif d'ordre 1 : sa loi dans k jours sachant aujourd'hui, sa loi stationnaire, le nombre de jours pour oublier le départ, et sa loi sachant un jour passé | ★★ | 30 | §1 | C, E | wbm | — |
| MB5.2 | ✏️ | La survie d'une ruche à six mois de risques différents : le produit exact, son logarithme, le risque mensuel constant équivalent, et l'encadrement par deux exponentielles | ★ | 20 | §1 | C, E | wbm | — |
| MB5.3 | ✏️ | Un phoque balisé entre deux relevés : sa loi à une heure intermédiaire (le pont d'une marche aléatoire) ; puis des scénarios de position aux mêmes lois à chaque heure, tirés avec un seul nombre au hasard ou avec un bruit frais, et leur corrélation | ★★ | 30 | §2 | C | wbm | — |
| MB5.4 | ✏️ | Une voix mêlée à un bruit de fond : SNR, part de variance de la voix, logit et décibels, puis la voix retrouvée à partir d'une estimation du bruit, et l'erreur amplifiée | ★★ | 20 | §3 | C, E | wbm | — |
| MB5.5 | ✏️ | Débruiter un signal reçu, d'abord gaussien, puis émis à deux niveaux ±c : E[x | y] par M25a et par la formule de Tweedie (une tanh), et ce que rend le débruiteur quand le bruit tend vers 0 | ★★ | 40 | §5 | C, E | wbm | — |
| MB5.6 | ✏️ | Un bit altéré par deux relais, puis reconstitué par un modèle retour : ln p(x), l'ELBO de la loi aller des relais, et sa décomposition en reconstruction, KL finale et KL d'un pas retour | ★★★ | 45 | §6 | C, E | wbm | — |
| MB5.7 | ✏️ | La date de floraison d'une variété et celle de tout le verger, deux lois gaussiennes : la loi p_v^{1+w} p_g^{−w} pour deux valeurs de w, son score, sa condition d'existence et le w limite | ★★ | 30 | §7 | C, E | wbm | — |
| MB5.8 | ✏️ | Une tasse de thé qui refroidit : Euler et point milieu contre la solution exacte, l'erreur quand le pas est divisé par deux, un courant de vitesse constante, et un calcul à rebours | ★★ | 30 | §8 | C, E | wbm | — |
| MB5.9 | ✏️ | Le chemin droit d'un bruit N(0, 1) vers une loi N(m, τ²) : le champ moyen (affine en x), un pas d'Euler depuis s = 1 qui rend m pour tout départ, puis deux pas, et l'écart-type obtenu contre τ | ★★★ | 40 | §9 | C, E | wbm | — |
| MB5.10 | ∂ | La récurrence linéaire gaussienne à coefficients quelconques : la loi de x_t sachant x_0 ; à coefficient constant |a| < 1, la loi sachant un instant passé, la loi stationnaire et la convergence depuis toute loi initiale ; aucune loi stationnaire si |a| ≥ 1 | ★★ | 40 | §1 | C, E | manuel | — |
| MB5.11 | ∂ | La meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + E[(E[Y | X] − g(X))²], donc g = E[Y | X] ; sur un échantillon, la moyenne de chaque groupe | ★★ | 20 | §4 | C, E | manuel | — |
| MB5.12 | ∂ | La formule de Tweedie : dériver la densité de y = a x + b n sous l'espérance, d'où E[x | y] et E[n | y] ; la vérification quand x est gaussien | ★★★ | 30 | §5 | C | manuel | — |
| MB5.13 | ∂ | L'ELBO d'une chaîne de latents : Markov et Bayes réécrivent chaque pas aller, la somme télescope ; puis chaque KL entre gaussiennes de même variance devient une MSE pondérée des moyennes | ★★★ | 40 | §6 | C | manuel | — |
| MB5.14 | 🔗 | Pont : une loss de débruitage à plusieurs niveaux de bruit, son minimiseur à chaque niveau, et pour des données gaussiennes les MSE minimales sur le signal et sur le bruit, dont le rapport est le SNR | ★ | 25 | §3 §4 §5 | C, E | wbm | — |
| MB5.15 | 🗣️ | Expliquer avec le jeu du téléphone pourquoi, après assez de relais qui atténuent et bruitent, le message reçu ne dit plus rien du message émis | ★ | 10 | §1 | C, E | manuel | — |
| MB5.E1 | 💼 | « Un modèle de régression entraîné à la MSE prédit-il le prix le plus probable ? Que prédit-il quand les prix d'un même profil se partagent en deux groupes, et quelle loss prendre pour une médiane ? » | ★ | 10 | §4 | C | manuel | — |
| MB5.16 | 🔨 | Propager la moyenne et la variance d'une récurrence linéaire gaussienne à coefficients quelconques · `linear_gaussian_recursion` | ★ | 30 | §1 | C, E | pytest | — |
| MB5.17 | 🔨 | Le débruiteur optimal d'une mesure bruitée quand le signal suit un mélange de gaussiennes, des points compris · `posterior_mean_mixture` | ★★ | 45 | §5 | C, E | pytest | — |
| MB5.18 | 🔨 | Suivre un champ de vitesses qui dépend du temps : la méthode d'Euler et celle du point milieu, dans les deux sens du temps · `euler_ode, midpoint_ode` | ★★ | 40 | §8 | C, E | pytest | — |
| MB5.19 | 📦 | `scipy.integrate.solve_ivp` : une croissance logistique suivie par tes deux méthodes, l'erreur au temps final selon le nombre de pas en échelle log-log, et les pentes 1 et 2 | ★ | 20 | §8 | C | wbm | MB5.18 |
| MB5.20 | 🔮 | Prédire ce que rend le débruiteur optimal de cinq relevés quand le bruit tend vers 0, pour une mesure proche d'un relevé puis à égale distance de deux, et mesurer | ★ | 15 | §5 | C, E | wbm | MB5.17 |
| MB5.21 | 🔬 | Le chemin droit vers une loi gaussienne : Euler et point milieu sur le champ moyen exact, de 1 à 32 pas, la moyenne et l'écart-type obtenus contre ceux de la cible | ★★ | 25 | §8 §9 | C, E | wbm | MB5.9, MB5.18 |
| MB5.22 | 🎨 | Des lois guidées p_c^{1+w} p_u^{−w} sur une grille : une loi générale à deux bosses, une loi de classe gaussienne, et ce que w resserre et déplace | ★ | 20 | §7 | C | manuel | MB5.7 |
| MB5.23 | 🐛 | Chasse à l'erreur : un pont aux poids inversés, un débruiteur qui oublie le bruit dans ses responsabilités, et un Euler dont le temps n'avance pas | ★ | 20 | §2 §5 §8 | C, E | wbm | — |
| MB5.24 | 🛠️ | Un test de propriété : Euler exact pour une vitesse constante, le point milieu exact pour une vitesse affine en t, et l'erreur d'Euler divisée par deux avec le pas | ★ | 30 | §8 | C | manuel | MB5.18 |
| MB5.25 | 🏆 | Défi : transporter un bruit N(0, 1) vers une loi à deux bosses par son champ moyen exact, en au plus huit évaluations du champ, sous une distance de Wasserstein fixée | ★★★ | 35 | §8 §9 | C | wbm | MB5.17, MB5.18 |

*Notes* : Frontières : les ∂ B5.6 (deux pas de bruit gaussien n'en font qu'un, la forme fermée q(x_t | x_0) par récurrence, la variance préservée, la variance qui explose sans le facteur d'atténuation, x_t | x_s ; déjà frontière de M25a et de CP6) et B5.7 (le posterior q(x_{t−1} | x_t, x_0) en dimension 1 : Bayes et Markov, les précisions, l'identité α_t(1 − ᾱ_{t−1}) + β_t = 1 − ᾱ_t, la substitution de x̂_0 qui donne la moyenne de l'algorithme 2 ; ∂ MB5.13 en écrit l'étape « Bayes et Markov », pour des latents quelconques et sans loi gaussienne de pas : c'est l'outil de l'ELBO d'une chaîne promise par M25b, voir §6) ; le ✏️ B5.1 (la combinaison (1 + w) ε_c − w ε_∅ de deux vecteurs pour w = 0, 1, 3, puis −1 et −0,5, et le coût de deux passes), le ✏️ B5.2 (un planning linéaire à T = 4, ses produits cumulés, Σβ et e^{−Σβ}, T = 400 et 1 000, des bornes mises à l'échelle, et dans la copie ln(1 − β) ≤ −β), le ✏️ B5.3 (le SNR des plannings linéaire et cosinus, les seuils 1 et 0,1 d'un chiffre lisible, la part des pas entre deux seuils), les ✏️ B5.4 et B5.5 (un pas DDPM et un pas DDIM à la main, β̃, l'écrêtage, la famille η), le 📄 B5.11 (Ho et coll. : les poids de l'équation 12, les deux choix de σ_t² et leurs cas extrêmes), les 🔨 B5.12, B5.14, B5.16 et B5.17 (les plannings, `q_sample`, le posterior, x̂_0, les pas DDPM et DDIM de `mylearn`), le 🔮 B5.13 (l'allure d'un chiffre bruité aux pas 100, 300 et 600, et son SNR), le 📈 B5.15 (lire ᾱ_t et le SNR de deux plannings), le 🔬 B5.18 (l'aller-retour exact avec le vrai bruit), le 🔬 B5.20 (flow matching contre DDIM en 2D, Euler à 1, 2, 5, 10, 20, 50 et 100 pas, la vitesse prise au milieu de l'intervalle), le 🐛 B5.22 (les quatre bugs d'indices, de racines et d'échelle, le débruiteur parfait), le 🔮 B5.26 (l'effet de w sur la netteté et la diversité), le 🔬 B5.28 (la mémorisation mesurée par le rapport r des plus proches voisins), les quiz B5.Q2 (un débruitage en un seul coup, trois cibles équiprobables, 2 000 pas), B5.Q3 (ᾱ_t = 0,64), B5.Q4 (x̂_0, la cible commode, la v-prédiction), B5.Q8 (DDIM), B5.Q9 (la guidance) et B5.Q11 (le flow matching), le rappel B5.R3 (la KL contre N(0, 1)) et les 💼 B5.E2 (pourquoi prédire le bruit), B5.E4 (le compromis de la guidance) et B5.E5 (diffusion ou flow matching). MB5 travaille hors réseau : l'anomalie de température d'un lac, la survie d'une ruche, un phoque balisé et des scénarios de position, un enregistrement de voix, des prix d'appartements, un signal reçu, un bit relayé, la date de floraison d'un verger, une tasse de thé qui refroidit, une population qui croît, des relevés de mesures, une loi à deux bosses ; jamais une image, un pixel, un réseau, un débruiteur appris, un pas de temps de diffusion, β_t, α_t, ᾱ_t, ε_θ, x̂_0, un planning nommé (linéaire de Ho, cosinus de Nichol et Dhariwal), ni un pas DDPM ou DDIM calculé. **Garde-fous de M25a, repris** : jamais un couple de coefficients a² + b² = 1 dans un exercice, un exemple, une docstring ou un test (ni même à moins de 0,05 de 1 : |a² + b² − 1| ≥ 0,05, sauf le couple (0, 1) du chemin droit en s = 1 ; il recomposerait x ↦ √α x + √(1 − α) ε ; le cas b² = 1 − a², variance stationnaire 1, est seulement énoncé, en une phrase, sans nombre ni composition de deux pas) ; jamais la KL contre N(0, 1), N(0, I) ou N(0, τ²) ; jamais la forme fermée de q(x_t | x_0) ni le posterior du pas. **§1** : la récurrence est démontrée pour des coefficients quelconques (∂ MB5.10 : un énoncé plus général que ∂ B5.6, BIBLE §8), jamais spécialisée à √(1 − β_t), sans « deux pas n'en font qu'un » ni variance « préservée » ; ✏️ MB5.1 prend un coefficient constant |a| < 1 et un b² ≠ 1 − a², jamais a = 0,8, 0,6 ou 0,9 (√0,64, √0,36, √0,81 de workbookIA) ; ✏️ MB5.2 (la survie) prend des risques qui ne sont pas en progression arithmétique, un nombre de périodes fixé (jamais « le même risque cumulé réparti sur plus de périodes », B5.2 j-l, B5.Q2 e), et demande l'encadrement par deux exponentielles, pas l'écart relatif de e^{−Σh} seule ; 1 − h ≤ e^{−h} est un rappel (M20 §6 écrit 1 + u ≤ e^u). Le 🔨 MB5.16 propage les moments (m_t, v_t) depuis une loi initiale quelconque : avec mean0 = 1 et var0 = 0, les moyennes sont des produits cumulés, mais la fonction ne prend jamais de β et ne rend aucune sortie nommée ᾱ ou √ᾱ ; ses tests ne lui passent jamais un β ni des coefficients √(1 − β_t), √β_t. Ni la fiche, ni un exercice, ni une solution, ni un test n'écrit l'identité Σ_k b_k² Π_{j>k} a_j² = 1 − Π a_j² quand b_k² = 1 − a_k², ni 1 − v_t = a_t²(1 − v_{t−1}) (le cœur de ∂ B5.6.2 et ∂ B5.6.7) ; les tests de `linear_gaussian_recursion` n'emploient jamais a_t² + b_t² = 1 ; la loi sachant un instant passé n'est demandée que pour un coefficient constant (✏️ MB5.1, ∂ MB5.10), et la docstring ne dit pas comment l'obtenir avec la fonction (l'indication de ∂ B5.6.7). **§2** : le pont est celui d'une marche aléatoire (a = 1), jamais d'une récurrence atténuée (ce serait ∂ B5.7 avec d'autres coefficients) ; il s'obtient par le modèle linéaire gaussien de M25a, sans « coefficient de x_0 et de x_t » ; les couplages sont un lemme général (√(s² − σ²) U + σ Z) appliqué à des scénarios de position ; l'usage qu'en fait DDIM (mêmes lois marginales, donc même entraînement) est énoncé dans l'encadré 🔗 de la fiche, sans σ de la famille η, sans « η = 1 donne β̃ » (B5.Q8) ni aller-retour avec le vrai bruit (B5.18). **§3** : y = a x + b n avec a² + b² ≠ 1 ; la normalisation y/√(a² + b²) est énoncée sans être écrite √γ x + √(1 − γ) n ; ✏️ MB5.4 prend des seuils en décibels autres que la paire « SNR 1 et 0,1 » et aucune courbe de SNR le long d'un planning (B5.3, B5.13, B5.15) ; retrouver le signal à partir d'une estimation du bruit se fait sur la voix, jamais avec ᾱ (B5.Q4 b) ; la v-prédiction de Salimans et Ho n'est pas enseignée, et la « vitesse » n'apparaît qu'au §9 ; aucun quiz « la somme des deux coefficients vaut-elle 1 ? » (B5.Q3 c) ni « le bruit est une cible commode parce que… » (B5.Q4 d). **§4** comble une lacune générale (« la MSE apprend une moyenne », que workbookIA B5 attribue au chapitre 9 et qu'aucun chapitre publié ne démontre) : ∂ MB5.11 pour X discrète, sur les prix d'appartements selon le quartier (la fiche) ; aucun quiz à trois cibles équiprobables, aucun débruitage « en un seul coup » qui rend une image floue (B5.Q2 a-c) ; le 💼 MB5.E1 est une question de régression. **§5** : le score est défini **en x** ; la fiche prévient que MB8 appellera score ∇_θ ln p_θ(x) (la méthode du score, nommée en M25b §7), et qu'ailleurs « score » a son sens courant, un score de classement ou de pertinence (MB2, MB3, MB4) ou le score S d'un classifieur (MB6) : une ligne ⚠️ de la fiche distingue les trois sens ; un paragraphe « dynamique de Langevin (aperçu) », sans exercice, tient la promesse de M26 (une chaîne de Markov qui converge vers sa loi stationnaire pour fabriquer des données) : pour p = N(μ, σ²), un AR(1) de coefficient 1 − h/(2σ²), où a² + b² = 1 + h(1 − 1/σ²) + h²/(4σ⁴) (qui vaut 1 pour h = 4σ²(1 − σ²) dès que σ² < 1 : la fiche reste en lettres, et aucun exercice, corrigé ou test ne chiffre Langevin à ce pas ; erratum de la session 74, l'ancienne note écrivait 1 + h²/(4σ⁴) ≠ 1, vrai pour σ² = 1 seulement), sans chiffre ni lien avec B5.E2, qui ne fait que nommer Langevin ; ∂ MB5.12 démontre Tweedie en dimension 1 (dériver sous l'espérance, M25b §7 ; une somme finie pour un x discret) ; ✏️ MB5.5 : un signal gaussien (Tweedie contre M25a), puis un signal à deux niveaux ±c équiprobables (une tanh), et la limite b → 0 ; la fiche en déduit « estimer le bruit, c'est estimer le score de la loi bruitée », sans le facteur √(1 − ᾱ_t), sans « pourquoi le réseau prédit le bruit plutôt que l'image » (B5.E2) ; le 🔮 MB5.20 prend cinq relevés de dimension 1, de poids égaux, inégalement espacés : quand le bruit tend vers 0, le débruiteur recopie le relevé le plus proche, et rend la moyenne de deux relevés pour une mesure à égale distance des deux ; sans rapport r, sans seuil 1/3 ni 1/2, sans image (B5.22, B5.28) ; la docstring de `posterior_mean_mixture` ne dit rien de la limite b → 0. **§6** comble ce que M25b a laissé à MB5 : ∂ MB5.13 démontre la décomposition (admise par workbookIA B5, fiche 205.4) pour des latents discrets ou continus ; ✏️ MB5.6 la calcule sur une chaîne binaire de deux pas (un bit altéré par deux relais, des tables données ; d'autres nombres que la chaudière de M25b) ; ✏️ MB5.6 donne la probabilité d'altération de chaque relais, calcule q(z₂ | x) comme le produit de deux matrices 2 × 2 (M26) et q(z₁ | z₂, x) par une table de Bayes ; il ne demande ni la loi de z_T pour T quelconque, ni sa limite, ni une formule fermée de la composition de T relais ; ∂ MB5.13 écrit, pour des latents quelconques, l'étape « Bayes et Markov » de ∂ B5.7.1 : c'est l'outil de l'ELBO promise par M25b, accepté, sans aucune loi gaussienne de pas ; aucune chaîne gaussienne n'est calculée (le posterior d'un pas serait ∂ B5.7) ; la KL de deux gaussiennes de même variance comme MSE pondérée s'énonce avec un σ² général, sans β_t, α_t ni ᾱ_t, sans aucun poids d'article (📄 B5.11 : β_t²/(2σ_t²α_t(1 − ᾱ_t)), β_t/(2α_t(1 − ᾱ_t)), 0,50, 0,010, 0,0055) et sans le nom L_simple. **§7** : ✏️ MB5.7 travaille sur des densités (deux lois gaussiennes de dates de floraison), jamais sur la combinaison de deux prévisions calculée pour plusieurs w (B5.1, B5.Q9), ni sur les conventions s = 1 + w (B5.E4), ni sur un compromis fidélité contre diversité (B5.E4, B5.26) ; MB5.Q7 n'a aucun item « w = 0 redonne… » ni « w = −1 redonne… » (B5.1 a et f) ; le 🎨 MB5.22 prend une loi générale à deux bosses de dimension 1, des w hors de {0, 1, 3, 7}, de 0,5 et de 2, sans écart-type moyen d'un nuage. **§8** : MB5.Q8 n'a aucun item « vitesse constante ⇒ un pas suffit » (B5.Q11 d) ; la propriété reste dans la fiche, dans ✏️ MB5.8 (le courant), dans la docstring d'`euler_ode` et dans le titre figé du 🛠️ MB5.24, jamais dans un quiz, une flashcard ni une annexe ; ✏️ MB5.8 (le refroidissement d'une tasse de thé) n'emploie ni x′ = x ni la suite 2 ; 2,25 ; 2,441 ; 2,594 (fiche de workbookIA B5), ni λ = −0,5 et la rotation de M20 ; le 📦 MB5.19 suit une croissance logistique ; le 🐛 MB5.23 n'a aucune des erreurs du corrigé de B5.20 (un pas d'Euler dans le mauvais sens, s tiré dans [0, 1), la cible x_0 − ε) ni de B5.22 (l'échelle, l'indice, la racine, le bruit au dernier pas) : ses trois erreurs sont des poids inversés dans un pont, des responsabilités calculées avec la variance du signal seule (sans le bruit), et un temps qui n'avance pas dans un Euler (invisible sur un champ qui ne dépend pas du temps). **§9** : x_0 de loi N(m, τ²) en dimension 1, temps s = 0 pour la donnée et s = 1 pour le bruit (la convention de workbookIA B5) ; le ✏️ MB5.9 et le 🔬 MB5.21 suivent le champ moyen exact avec 1, 2, 4, 8, 16 et 32 pas (des puissances de 2), sans comparaison à DDIM, sans anneau, sans MLP, sans « vitesse prise au milieu de l'intervalle » (variante de B5.20 ; le point milieu du §8 est la méthode d'ordre 2) ; le 🏆 MB5.25 transporte N(0, 1) vers un mélange de deux gaussiennes de dimension 1 par son champ moyen exact (`posterior_mean_mixture`), avec un budget d'évaluations du champ et une distance de Wasserstein (M27) mesurée sur un grand échantillon. **Partage** : M25a a les sommes, les images affines, le produit de densités, le modèle linéaire gaussien, le conditionnement et la KL entre gaussiennes ; M25b la chaîne et le tirage ancestral, l'espérance et la variance conditionnelles, les responsabilités, l'ELBO d'un latent et la dérivée d'une espérance ; MB5 les rappelle (🔁 MB5.R1, MB5.R2) sans les redémontrer. MB8 garde la méthode du score (en θ). Promesses tenues : M25a (« MB5 enchaîne produits et sommes de gaussiennes », « MB5 conditionne une loi gaussienne pour les modèles de diffusion »), M25b (« MB5 écrira l'ELBO d'une chaîne de latents »), M26 (« MB5 fera converger une chaîne de Markov vers sa loi stationnaire pour fabriquer des données » : l'AR(1) du §1 et la dynamique de Langevin du §5), M20 (Euler, premier contact). Une ligne ⚠️ de la fiche : la diffusion des modèles génératifs, pas la diffusion (*broadcasting*) des tableaux de M20. Les trois notions « locales » de workbookIA B5 (somme de gaussiennes indépendantes, produit de deux densités en dimension 1, méthode d'Euler pour suivre un champ de vitesses) sont couvertes : les deux premières par M25a, la troisième par M20 et MB5. **Conventions** : N(μ, v) avec une variance ; un bruit ε (ou n) de loi N(0, 1), indépendant du reste ; un champ f(t, x), le temps d'abord, comme SciPy ; logarithmes népériens, KL en nats ; la dimension 1 partout, sauf l'énoncé de Tweedie en dimension d. `gaussian_paths` : NumPy et `math` seulement, aucune SciPy (`solve_ivp`, `odeint`, `quad`, `norm`, `logsumexp`, `softmax` sont les oracles des tests) ; les imports relatifs de ses propres modules sont permis (`approx.logsumexp`, M05a) ; `linear_gaussian_recursion(a, b, mean0, var0)` rend (moyennes, variances) de x_0 à x_T (oracles : simulation à graine fixe, la récurrence en `fractions` sur de petits cas) ; `posterior_mean_mixture(y, a, b, weights, means, variances)` rend E[x | y] pour y = a x + b n et x un mélange de gaussiennes de dimension 1, des variances nulles permises (des points), a = 0 permis (la moyenne du mélange), b > 0 (oracles : `scipy.integrate.quad` sur la loi a posteriori, Tweedie par différences finies de ln p_Y) ; `euler_ode(f, x0, t0, t1, n_steps)` et `midpoint_ode` rendent les n_steps + 1 points, t1 < t0 permis (oracles : `solve_ivp` à tolérance serrée, solutions exactes, rapports d'erreurs 2 et 4). Aucune n'a le nom ni le contrat d'une fonction de `mylearn/diffusion.py` (pas de β, pas de dictionnaire de constantes, pas de tirage, pas de x̂_0, pas de pas d'échantillonnage) ; la boucle de B5.20 (`x - (1/n_steps) * v_model(x, k/n_steps)`) n'est pas le contrat d'`euler_ode`. Les exemples du stub ne reviennent dans aucun exercice : les coefficients (0,5 ; 2 ; 1) et (1 ; 0 ; 3) depuis 4, (0,5) et (−1) depuis N(2, 8) ; le mélange (0,3 ; 0,7) aux points −1 et 2, N(2, 3) avec a = b = 1, a = 0 avec b = 2 ; x′ = 2t + 1 de t = 1 à 3 en 4 pas, x′ = 2, x′ = −x/4 de t = 2 à 0 depuis (4, −8) (les exemples x′ = t sur [0, 1] en 4 pas étaient ceux de `riemann_sum`, M02a, et sont écartés). **Écarts au plan** : le module s'appelle `gaussian_paths.py`, pas `diffusion.py` (le nom du module `mylearn` de B5) ; `cumulative_alpha` (le contrat de `noise_schedule(betas)["alpha_bars"]`), `combine_gaussians` et `gaussian_product_1d` (déjà en M25a §2 et §5, et l'outil de ∂ B5.7) sont retirées ; `linear_gaussian_recursion`, `posterior_mean_mixture` et `midpoint_ode` ajoutées ; `guided_gaussian` n'est pas retenue (deux lignes de précisions, faites à la main en ✏️ MB5.7 et sur une grille dans le 🎨 MB5.22) ; les « plannings de bruit (linéaire, cosinus) » deviennent les produits cumulés et le SNR, et s'ajoutent la récurrence générale et la loi stationnaire, le pont et les couplages, la MSE et l'espérance conditionnelle, Tweedie et le score en x, le point milieu et l'ordre de l'erreur. **MML** : (§6.5), en relecture : §6.5.1 (marginales et conditionnelles) et §6.5.3 (sommes et transformations linéaires) avant les §1 et §2, §6.5.2 (produit de densités) avant le §7 ; MML n'a ni équations différentielles, ni processus autorégressif, ni diffusion. Lectures libres, citées par chapitres : Blitzstein et Hwang, ch. 9 (l'espérance conditionnelle et la prédiction) ; B. Efron, « Tweedie's Formula and Selection Bias », JASA, 2011 ; Süli et Mayers, *An Introduction to Numerical Analysis*, le chapitre sur les problèmes aux valeurs initiales ; Shumway et Stoffer, *Time Series Analysis and Its Applications*, ch. 3 (les modèles AR) ; jamais Weng 2021 ni Luo 2022, sources de workbookIA B5. COMPOSITION : pas de 📖 (§6.5 est lu en entier en M25a, avec le 📖 M25a.17, et le reste du chapitre n'est pas dans MML) ; un seul 💼 ; 9 ✏️ et 4 ∂ ; 3 🔨 et un 📦 ; un 🔬 et un 🔮. Parcours essentiel : sans ✏️ MB5.3 (pont et couplages), ∂ MB5.12 et MB5.13, le 💼, le 📦, le 🎨, le 🛠️ et le 🏆. **Durée** : 16,6 h (essentiel 13,0 h ; recalée à la génération, session 74, par l'auteur des exercices, la re-résolution à l'aveugle et l'apprenant simulé : 15,7 h et 12,3 h au syllabus ; lecture 160 min, dont 5 pour le paragraphe sur Langevin et les lignes ⚠️ ajoutés après relecture), pour 14 h au plan et 15 h visées : neuf sections, dont trois lacunes générales (la MSE et l'espérance conditionnelle, Tweedie et le score en x, les EDO au-delà d'Euler) et l'ELBO d'une chaîne démontrée ; durées comptées pour un apprenant qui rédige. Deux sessions de génération : §1 à §5 (🔨 MB5.16 et MB5.17), puis §6 à §9 (🔨 MB5.18). **Évités** (règle de partage, et reprises de ce dépôt) : les plannings jouets β = (0,02 ; 0,04 ; 0,06 ; 0,08 ; 0,10) (ᾱ = 0,98 ; 0,9408 ; 0,8844 ; 0,8136 ; 0,7322 ; √ᾱ = 0,9899 ; 0,9700 ; 0,9404 ; 0,9020 ; 0,8557 ; √(1 − ᾱ) = 0,1414 ; 0,2433 ; 0,3401 ; 0,4317 ; 0,5174), β = (0,05 ; 0,15 ; 0,25 ; 0,35) (ᾱ = 0,95 ; 0,8075 ; 0,605625 ; 0,39365625 ; 0,6274 ; 0,7787), β = (0,10 ; 0,20 ; 0,30 ; 0,40) (0,3024 ; 22 %) et β = (0,1 ; 0,2 ; 0,5) (ᾱ = 0,9 ; 0,72 ; 0,36 ; β̃ = 0 ; 0,0714 ; 0,2187), et toute suite de coefficients en progression arithmétique présentée comme un planning ; le planning linéaire de 10⁻⁴ à 0,02, T = 200, 400 et 1 000, Σβ = 2,01 ; 4,02 ; 10,05, e^{−0,8} = 0,4493, e^{−10,05} = 4,32 × 10⁻⁵, 4,04 × 10⁻⁵, 3,6 × 10⁻⁵, 0,66 %, 14 %, 0,1322, 0,134, 36 %, 1,7 × 10⁻², 1,5 × 10⁻⁸, 0,603, 7,7 × 10⁻⁶ ; le cosinus s = 0,008, le plafond 0,999, 1/127,5, 4,1 × 10⁻⁵, f(0) = 0,99984 ; les seuils 0,26 ; 0,50 ; 0,49 ; 0,80, S(500) = 2,535, les SNR 0,976 ; 0,086 ; 49 ; 2,73 ; 8,7 ; 0,66 ; 0,027 ; 34,8 ; 3,7 ; 0,52 ; 1,9 ; 1,8, les ln SNR −4,0 ; −10,1 ; −10,2 ; −19,8 et −10,05, la paire de seuils « SNR 1 et 0,1 », les pas 100, 300, 600, 497, 804 et 515 ; le pixel x_0 = 0,6 et ε = −0,5 (x_4 = 0,3253), ε_θ = −0,4, z = 1,2, 0,4165, 0,6838, 0,55214, μ̃_4 = 0,4358, β̃_4 = 0,0496, 0,4382 ; les cas de ✏️ B5.4 (x_3 = 0,8, ε_θ = 0,5, z = −1 ; x_3 = 1,5, ε_θ = −0,6 ; x_1 = 0,5, ε_θ = 0,2 ; 0,3981 ; 0,6939 ; 0,1220 ; 0,3446 ; 0,1939 ; 0,4671 ; 0,4737), de ✏️ B5.5 (x_4 = −0,5, ε_θ = −1,2 ; 0,6924 ; 0,4065 ; 0,0957 ; 0,2276 ; 0,2198 ; 0,0413 ; 0,2017 ; 0,1546), de ∂ B5.6 (0,1925 ; Var(x_0) = 0,5 et 0,8032 ; √10,05 ≈ 3,17 ; 0,4875 ; 0,6982 ; 0,7159 ; 0,6375 ; 0,3625 ; 1 + 3 + … + (2t − 1) = t²) et de ∂ B5.7 (x_0 = 0,4, x_2 = 0,1, 0,7595, 0,2395, 3/77, 0,3277, 0,1627) ; ᾱ_t = 0,64 et 0,81 (0,80 ; 0,60 ; 1,78 ; 0,475 ; 0,9 ; 0,44), donc jamais les couples de coefficients (0,8 ; 0,6) ni (0,9 ; 0,44) ; les guidances (0,4 ; −1,0) et (0,1 ; −0,6) avec w = 0,5 (0,55 ; −1,2), (0,8 ; −0,5) et (0,5 ; 0,1) avec w = 0, 1, 3, −1, −0,5 (4 ; 2,01 ; 100 ; 0,65 ; −0,2), 0,3 et 0,5 avec w = 2 (−0,1), les ensembles w = {0, 1, 3, 7}, w = 0,1 ; 0,3 ; ≥ 4, les conventions 7,5 ↔ 6,5, 3 ↔ 2, 4 ↔ 3, p_uncond = 0,1 ou 0,2, l'écart-type 0,33 → 0,27, les Fréchet 133,8 ; 51,4 ; 39,0 ; 65,1 ; N(1 ; 0,3²) + N(−2 ; 0,4²) = N(−1 ; 0,5²) (« 0,5 et pas 0,7 ») ; N(2, 1) × N(5 ; 0,5) → (4, 1/3) ; les cibles ±1 (MSE 1 et 2) et (−1, 0, 2) (0,33 ; 1,56) ; Euler sur y′ = y avec 1, 2, 4 et 10 pas (2 ; 2,25 ; 2,441 ; 2,594 ; e ≈ 2,718), la boucle `x - (1/n_steps) * v_model(x, k/n_steps)`, v = (1 ; −2), les distances de B5.20 (0,915 ; 0,371 ; 0,103 ; 0,081 ; 0,077 ; 0,075 et 6,81 ; 6,67 ; 0,424 ; 0,248 ; 0,171 ; 0,147 ; 0,140, au point milieu 0,222 ; 0,213 ; 0,079 ; 0,074), √ᾱ_{T−1} = 0,006 ; les moyennes exponentielles ρ = 0,9999 ; 0,999 ; 0,99 ; 0,98 avec 800 000, 9 375, 1 252 et 313 pas, 0,01^{1/1252} = 0,9963 ; d_F² de N(0, 1) contre N(1, 4) (= 2) ; la KL de N(0,5 ; 0,25) contre N(0, 1) (0,4431) et z = −0,50 ; le rapport r de mémorisation, les seuils 1/3 et 1/2, 500, 10 000 et 60 000 images ; l'anneau de 8 gaussiennes (rayon 1,5, écart-type 0,15, variance 1,15) et le mélange de trois gaussiennes en 2D ; d = 128, 6,28 et 54 400 (B5.R1) ; MNIST, Fashion-MNIST, CIFAR-10, 784, 28 × 28 ; les exemples des docstrings de `mylearn/diffusion.py` ((0,0001 ; 0,005075 ; 0,01005 ; 0,015025 ; 0,02), (0,1013 ; 0,2795 ; 0,4736 ; 0,7241 ; 0,999), x_0 = [[1, −1], [0,5 ; 0]], x_t = [[1,2649 ; −0,6325], [1,1 ; 0,8]], ε = [[0,3 ; −2], [1 ; 0,5]], x_0 = [[0,5 ; −1 ; 0,25]], t = 700) ; de ce dépôt, le pas d'Euler de M20 (λ = −0,5 et T = 1 : 0,5862 ; 0,6035 ; 0,6058 pour 4, 25 et 100 pas ; la rotation et ses 1,1289 et 1,0126 ; le demi-tour en 6, 12 et 48 pas), l'altitude du refuge N(1 520 ; 10²) et le baromètre, les deux pièces pesées ((40, 25), diag(4, 9), 72 g) et la KL de N(6, 4) contre N(8, 9) de M25a, la station (N(11, 4) et N(3, 9), ¼ et ¾, 8 °C) et la chaudière (ln 0,226) de M25b, les exemples des stubs `gaussian`, `latent` et `markov` ; ajoutés à la génération (session 74, relecture de partage) : l'échange des deux termes ou des deux puissances d'une guidance (corrigés de ✏️ B5.1 et 📦 B5.27) et le pas « dans le mauvais sens » (🔬 B5.20), jamais en valeur fausse, message, ⚠️ ni flashcard ; des risques mensuels (✏️ MB5.2) qui ne sont ni des β ni des 1 − β du planning jouet ; de ce dépôt, le concours et l'aptitude cachée de ✏️ M25b.9, les facteurs du lac de M22 §5 (0,97 ; 0,92 ; 0,6), les tables de CP6 j) ((0,84 ; 0,16), (0,34 ; 0,66), (0,59 ; 0,41)), les deux variétés de pommes de M27 §5 (N(150, 10²), N(170, 10²), 90 % et 10 %), la rivière de M25b (turbidité, conductivité), les émetteurs et l'antenne de M28.3.

<a id="mb6"></a>
## MB6 · Shapley, intégrales de chemin et équité

**Partie** VII · **prépare** workbookIA B6 · **dossier** `chapitres/mb6_shapley_equite/` · **MML** — · **sessions de génération** 1

Partager un gain, une variation ou une décision. D'abord les jeux coopératifs : la contribution marginale d'un joueur, sa moyenne sur les ordres d'arrivée (la valeur de Shapley), les poids des coalitions qui en découlent et ce que coûte le calcul ; les quatre axiomes, les jeux d'unanimité et les dividendes de Harsanyi, qui montrent qu'une interaction se partage également entre ses membres et que la valeur de Shapley est la seule à respecter ces axiomes. Puis fixer une variable d'une fonction de plusieurs variables : l'espérance marginale (la dépendance partielle) contre l'espérance conditionnelle, les courbes ICE et les interactions. Puis l'intégrale d'un champ de vecteurs le long d'un chemin, le théorème du gradient, et deux façons de partager une variation entre les coordonnées (le long du segment, ou par les chemins en escalier, dont la moyenne est une valeur de Shapley). Deux outils courts : l'interpolation bilinéaire d'une grille et la corrélation de rangs de Spearman. Enfin l'équité vue comme des indépendances : ce qui est incompatible quand les taux de base diffèrent, pour des décisions et pour des scores calibrés, puis tirer au sort entre deux seuils, repondérer, et mesurer l'écart de deux taux. workbookIA B6 applique ces outils à l'explication de modèles et à l'audit d'équité.

**Temps** : 13,0 h en parcours complet, 9,3 h en parcours essentiel (lecture 125 min, 15 flashcards).

**Objectifs**

- Calculer la valeur de Shapley d'un petit jeu coopératif par les ordres d'arrivée et par les poids des coalitions, dire ce que coûte chaque méthode, et combien d'ordres tirés au hasard suffisent.
- Vérifier les quatre axiomes sur un jeu, calculer ses dividendes de Harsanyi et en déduire la valeur de Shapley ; démontrer qu'elle est la seule à respecter les quatre axiomes.
- Distinguer la moyenne marginale (dépendance partielle) et la moyenne conditionnelle d'une fonction, les calculer pour deux variables gaussiennes corrélées, et relier des courbes ICE parallèles à l'absence d'interaction.
- Calculer l'intégrale d'un champ de vecteurs le long d'une ligne brisée ou d'un arc, reconnaître un champ de gradient (indépendance du chemin, test de Schwarz), et partager une variation de f entre les coordonnées le long du segment ou par les chemins en escalier.
- Agrandir une grille par interpolation bilinéaire dans les deux conventions d'alignement, et lire la moyenne d'un gradient sur une grille comme une dérivée directionnelle.
- Calculer une corrélation de rangs de Spearman, ex aequo compris, et dire ce qu'elle ne voit pas.
- Écrire les critères d'équité comme des indépendances, et démontrer ce qui est incompatible quand les taux de base diffèrent, pour des décisions et pour des scores calibrés.
- Atteindre un taux de détection en tirant au sort entre deux seuils, repondérer une table pour rendre groupe et label indépendants, et donner l'intervalle de l'écart de deux taux.

**Sections de la fiche**

- §1 Jeux coopératifs : contributions marginales, ordres d'arrivée et poids des coalitions
- §2 Les quatre axiomes, les jeux d'unanimité et les dividendes de Harsanyi
- §3 Fixer une variable : espérance marginale ou conditionnelle, courbes ICE et interactions
- §4 Intégrer un gradient le long d'un chemin, et partager une variation entre les coordonnées
- §5 Une grille : la moyenne d'un gradient, et l'agrandir par interpolation bilinéaire
- §6 La corrélation de rangs de Spearman
- §7 Les critères d'équité comme des indépendances, et ce qui est incompatible
- §8 Décider au hasard, repondérer, mesurer l'écart entre deux groupes

**Notions enseignées** : jeu coopératif à n joueurs : fonction caractéristique v sur les coalitions, contribution marginale v(S ∪ {i}) − v(S), valeur de Shapley comme moyenne sur les n! ordres d'arrivée · poids d'une coalition de taille s, s!(n − 1 − s)!/n!, en regroupant les ordres ; lecture probabiliste (une taille uniforme, puis une coalition uniforme de cette taille) et Σ_s C(n − 1, s) w(s) = 1 ; coût : n! ordres contre 2^(n−1) coalitions par joueur (rappels de R4 et R8) · estimer par des ordres tirés au hasard : une moyenne de contributions marginales, estimateur sans biais (M02c), nombre d'ordres par l'inégalité de Hoeffding quand les contributions sont bornées (M11) ; l'efficacité tient à chaque ordre (une somme télescopique) · jeux de vote pondéré [q ; w₁, …, w_n] et indice de Shapley-Shubik (le membre pivot) : le poids n'est pas le pouvoir ; jeux de partage de coûts et règle de l'aéroport · les quatre axiomes : efficacité Σφ_i = v(N) − v(∅), symétrie, joueur nul, additivité ; un jeu additif v(S) = c + Σ_{j∈S} a_j donne φ_i = a_i · jeux d'unanimité u_T, dividendes de Harsanyi d_T (inversion de Möbius sur les parties), v = Σ_T d_T u_T ; φ_i = Σ_{T∋i} d_T/|T| : chaque interaction est partagée également entre ses membres ; unicité de la valeur de Shapley (démontrée, ★★★) · espérance marginale E[f(v, X_{−j})] (la dépendance partielle) contre espérance conditionnelle E[f(X) | X_j = v] ; égales quand X_j est indépendante des autres variables ; calcul fermé pour un couple gaussien (rappel de M25a) ; la même opposition entre le jeu « marginal » et le jeu « conditionnel » d'une fonction (énoncée) · courbes ICE v ↦ f(v, x_{i,−j}), dont la dépendance partielle est la moyenne ; f = g(x_j) + h(x_{−j}) ⇔ courbes ICE parallèles ⇔ ∂²f/∂x_j∂x_k = 0 pour tout k ≠ j (f régulière sur un pavé, démontré) ; une moyenne peut cacher une interaction · chemin paramétré et dérivée de f le long d'un chemin, (f∘γ)′ = ∇f(γ) · γ′ (rappels de M05b et M17) ; intégrale d'un champ de vecteurs le long d'un chemin et d'une ligne brisée ; théorème du gradient ∫ ∇f · dγ = f(B) − f(A) : indépendance du chemin, intégrale nulle sur une boucle ; un champ qui n'est pas un gradient (dérivées croisées différentes, Schwarz) · sommes de Riemann, trapèzes et Simpson sur [0, 1] et leurs ordres d'erreur (rappel de M02a) · partager f(x) − f(r) entre les coordonnées : le long du segment (les parts ∫ ∂_i f dγ_i, dont la somme est f(x) − f(r)), ou le long d'un chemin en escalier (les contributions marginales dans un ordre) ; la moyenne des chemins en escalier est la valeur de Shapley du jeu v(S) = f(x_S, r_{S̄}) ; les deux partages coïncident pour une fonction multilinéaire (démontré par les jeux d'unanimité) et diffèrent en général ; ils dépendent de la référence r, et une coordonnée de dérivée nulle en x peut recevoir une part non nulle (saturation) · fonctions homogènes de degré k : identité d'Euler Σ x_i ∂_i f = k f ; depuis r = 0, la part de x_i le long du segment vaut x_i ∂_i f(x)/k · moyenne d'un gradient sur une grille : (1/(HW)) Σ ∂y/∂A_ij est la dérivée de y par un décalage uniforme de la grille, divisée par HW (une dérivée directionnelle) ; homogénéité positive de la partie positive, max(0, λz) = λ max(0, z) pour λ > 0 · interpolation linéaire et bilinéaire (deux interpolations linéaires, dans un ordre ou dans l'autre), exacte pour les fonctions affines ; agrandir une grille h × w en H × W : centres des cases alignés (u ↦ (u + ½) h/H − ½) ou coins alignés (u ↦ u (h − 1)/(H − 1)), écart d'au plus un demi-pas · corrélation de rangs de Spearman : rangs, ex aequo (rangs moyens), ρ = corrélation de Pearson des rangs, = 1 − 6 Σ d_i²/(n(n² − 1)) sans ex aequo (démontré dans la fiche) ; invariance par une transformation strictement croissante ; ce qu'elle ne voit pas (l'ampleur des écarts) · critères d'équité comme des (in)dépendances : indépendance Ŷ ⊥ G (parité des décisions), séparation Ŷ ⊥ G | Y (égalité des taux d'erreur), suffisance Y ⊥ G | Ŷ ou Y ⊥ G | S (parité des precisions, calibration par groupe) ; rappels des définitions de M03 §8 et de l'indépendance conditionnelle de M25b · l'identité de M03 §8 entre séparation et suffisance (rappelée, non redémontrée) ; indépendance et séparation incompatibles quand les taux de base diffèrent, sauf pour une décision indépendante de Y (démontré) · scores calibrés dans chaque groupe : E[S | G = g] = p_g, et p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; mêmes moyennes de scores chez les positifs et chez les négatifs de deux groupes : taux de base égaux ou score parfait (Kleinberg, Mullainathan et Raghavan, démontré) · décisions randomisées : tirer au sort entre deux seuils donne tout point de la corde entre deux points de la courbe ROC (TPR et FPR affines en la probabilité du tirage) · repondération w(g, y) = P(g)P(y)/P(g, y) : la loi pondérée garde les deux marges et rend G et Y indépendants (démontré) ; diviser par une probabilité, comme Horvitz-Thompson (M20) · écart de deux proportions indépendantes : erreur type √(p₁(1 − p₁)/n₁ + p₂(1 − p₂)/n₂) et intervalle de Wald de l'écart ; pour un taux de vrais positifs, n est le nombre de positifs ; bootstrap stratifié (tirer dans chaque groupe) contre bootstrap global (principe) ; bootstrap par groupes (tirer des groupes entiers quand les exemples sont dépendants, principe)

**Prérequis** : fonction affine passant par deux points (R3) · parties d'un ensemble et leur nombre 2^n, notations Σ et Π, rédiger une démonstration (R4) · principe multiplicatif, factorielle, combinaisons C(n, k), arbres (R8) · intégrale, théorème fondamental, méthodes des rectangles, des trapèzes et de Simpson (M02a) · espérance, linéarité de l'espérance, loi de Bernoulli et sa variance, variance d'une somme indépendante, formule du binôme (M02b) · corrélation de Pearson, estimateur sans biais, erreur type, bootstrap (M02c) · probabilités conditionnelles, indépendance, taux par groupe, calibration, courbe ROC, l'identité des taux de faux positifs de deux groupes (§8) (M03) · dérivées partielles, gradient, dérivée directionnelle, dérivées croisées et théorème de Schwarz (M05b) · intervalle d'une proportion (Wald) (M08) · base d'un espace vectoriel (∂ MB6.8) (M12a) · inégalité de Hoeffding et taille d'échantillon (M11) · règle de la chaîne le long d'une courbe, fonctions affines par morceaux (M17) · estimateur de Horvitz-Thompson : diviser par une probabilité (M20) · loi conditionnelle d'un couple gaussien : moyenne affine en la valeur observée (M25a) · indépendance conditionnelle, espérance conditionnelle et espérance totale (M25b) · rangs, rangs moyens des ex aequo (MB4)

**mymath** : `attribution.py` (signatures figées) : `coalition_weights`, `harsanyi_dividends`, `line_integral`, `spearman_rho`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B6.2 ∂ Modèle linéaire et fond indépendant : φ_i = w_i (x_i − E[x_i]) · B6.6 ∂ Impossibilité : taux de base différents, calibration et égalité des erreurs incompatibles · B6.1 ✏️ Valeurs de Shapley exactes à la main : trois features, huit coalitions · B6.3 ✏️ Gradients intégrés à la main sur f(x) = x₁² + 3x₂ et vérification de la complétude · B6.4 ✏️ Grad-CAM à la main : deux cartes 3×3 et leurs gradients · B6.5 ✏️ Audit à la main : deux groupes, deux matrices de confusion, cinq indicateurs · B6.7 🧮 Fermi : coût de Shapley exact, de KernelSHAP et de TreeSHAP pour 10, 20 et 50 features · B6.11 📄 Lundberg et Lee (2017) : « A Unified Approach to Interpreting Model Predictions » · B6.Q3 🧠 Dépendance partielle et courbes ICE : ce que montre la moyenne, ce qu'elle cache · B6.Q4 🧠 Les quatre propriétés de Shapley : efficacité, symétrie, joueur nul, additivité · B6.Q5 🧠 Changer le fond (background) change les valeurs SHAP : vrai ou faux · B6.Q6 🧠 Features corrélées : ce que SHAP répartit et ce qu'il ne dit pas · B6.Q7 🧠 Gradient, gradient × entrée, gradients intégrés : pourquoi une ligne de référence ? · B6.Q9 🧠 Une carte de saillance qui ne dépend pas du modèle : que prouve le test de randomisation ? · B6.Q11 🧠 Parité démographique, égalité des chances, calibration : peut-on tout avoir ? · B6.14 🔨 shapley_values : Shapley exact par énumération des coalitions · B6.18 🔨 integrated_gradients et grad_cam · B6.21 🐛 Grad-CAM à l'envers : mauvaise couche, mauvaise classe, ReLU oubliée, carte mal alignée · B6.22 🔬 Test de santé d'Adebayo : randomiser les poids couche par couche, la carte change-t-elle ? · B6.23 🔨 group_rates, demographic_parity_difference et equalized_odds_difference · B6.E2 💼 Qu'est-ce qu'une valeur SHAP, et quelles sont ses limites ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| MB6.Q1 | 🧠 | Jeux coopératifs : ordres ou coalitions, poids d'une coalition, et ce que garantit chaque axiome | ★ | 5 | §1 §2 | C, E | manuel | — |
| MB6.Q2 | 🧠 | Fixer une variable : moyenne marginale ou conditionnelle, courbes ICE parallèles ou non | ★ | 5 | §3 | C, E | manuel | — |
| MB6.Q3 | 🧠 | Intégrales de chemin : boucle fermée, chemin parcouru à l'envers, champ qui n'est pas un gradient, fonction homogène | ★ | 5 | §4 | C, E | manuel | — |
| MB6.Q4 | 🧠 | Grilles et rangs : interpolation bilinéaire, centres ou coins alignés, ex aequo et transformation strictement croissante | ★ | 4 | §5 §6 | C, E | manuel | — |
| MB6.Q5 | 🧠 | Indépendance, séparation, suffisance : quel critère pour quelle phrase, et lesquels se contredisent | ★ | 5 | §7 | C, E | manuel | — |
| MB6.Q6 | 🧠 | Tirer au sort entre deux seuils, repondérer, lire l'écart de deux taux : vrai ou faux | ★ | 4 | §8 | C, E | manuel | — |
| MB6.R1 | 🔁 | Parties d'un ensemble, factorielles et combinaisons (R4, R8) | ★ | 6 | §1 | C, E | manuel | — |
| MB6.R2 | 🔁 | La dérivée d'une fonction le long d'une courbe : gradient, vitesse et règle de la chaîne (M05b, M17) | ★ | 6 | §4 | C, E | manuel | — |
| MB6.R3 | 🔁 | La loi conditionnelle d'un couple gaussien : une moyenne affine en la valeur observée (M25a) | ★ | 6 | §3 | C, E | manuel | — |
| MB6.1 | ✏️ | Un conseil de quatre membres à vote pondéré : l'indice de Shapley-Shubik par les 24 ordres, un membre nul, deux membres de poids différents et de même pouvoir, et le nombre d'ordres tirés au hasard qui suffit (Hoeffding) | ★★ | 35 | §1 | C, E | wbm | — |
| MB6.2 | ✏️ | Trois hameaux partagent une conduite d'eau : la valeur de Shapley par les ordres, les dividendes de Harsanyi, le partage tronçon par tronçon, et les quatre axiomes vérifiés | ★★ | 30 | §2 | C, E | wbm | — |
| MB6.3 | ✏️ | Le rendement d'une parcelle selon la pluie et l'engrais : courbes ICE et dérivée croisée de deux modèles, puis la moyenne marginale et la moyenne conditionnelle quand pluie et engrais sont corrélés | ★★ | 30 | §3 | C, E | wbm | — |
| MB6.4 | ✏️ | Le travail de deux forces entre deux points : un champ de gradient le long de trois chemins, puis un champ qui n'en est pas un (Schwarz) le long de deux chemins | ★★ | 25 | §4 | C, E | wbm | — |
| MB6.5 | ✏️ | La variation d'un coût à trois facteurs (prix, quantité, taux de change) partagée entre les facteurs : le long du segment, puis par la moyenne des six chemins en escalier, et pourquoi les deux partages coïncident | ★★ | 35 | §4 | C | wbm | — |
| MB6.6 | ✏️ | Des relevés de capteurs sur une grille 3 × 4 : la dérivée d'un indice régional par un réchauffement uniforme, puis la grille agrandie deux fois par interpolation bilinéaire, centres ou coins alignés | ★★ | 30 | §5 | C, E | wbm | — |
| MB6.7 | ✏️ | Un contrôle de pièces sur deux lignes de production aux taux de défauts différents : les taux de rejet sous la séparation, un tirage au sort entre deux seuils pour atteindre un taux de détection, et les poids qui rendent ligne et défaut indépendants | ★★ | 30 | §7 §8 | C, E | wbm | — |
| MB6.8 | ∂ | Unicité de la valeur de Shapley : les jeux d'unanimité forment une base, et les quatre axiomes imposent φ_i = Σ_{T ∋ i} d_T / |T| | ★★★ | 40 | §2 | C | manuel | — |
| MB6.9 | ∂ | Un score calibré dans un groupe vérifie p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; si deux groupes ont les mêmes moyennes de scores chez leurs positifs et chez leurs négatifs, leurs taux de base sont égaux ou le score est parfait | ★★ | 25 | §7 | C, E | manuel | — |
| MB6.10 | ∂ | Indépendance et séparation ne tiennent ensemble, quand les taux de base diffèrent, que pour une décision qui ignore le label ; la repondération P(g)P(y)/P(g, y) rend groupe et label indépendants sans changer leurs marges | ★★ | 20 | §7 §8 | C, E | manuel | — |
| MB6.11 | 🔗 | Pont : l'écart des taux de détection de deux laboratoires et son intervalle, par l'erreur type d'une différence de deux proportions, qui se lit avec le nombre d'échantillons positifs de chacun | ★ | 15 | §8 | C, E | wbm | — |
| MB6.12 | 🗣️ | Expliquer avec trois amis qui partagent un taxi pourquoi on moyenne l'apport de chacun sur tous les ordres d'arrivée | ★ | 10 | §1 | C, E | manuel | — |
| MB6.E1 | 💼 | « La valeur de Shapley est la seule répartition qui respecte quatre règles simples : lesquelles, et pourquoi suffisent-elles ? » | ★ | 10 | §2 | C | manuel | — |
| MB6.13 | 🔨 | Les poids des coalitions dans la valeur de Shapley, exacts ou en flottants · `coalition_weights` | ★ | 15 | §1 | C, E | pytest | — |
| MB6.14 | 🔨 | Les dividendes de Harsanyi d'un jeu donné par sa fonction caractéristique · `harsanyi_dividends` | ★★ | 25 | §2 | C | pytest | — |
| MB6.15 | 🔨 | L'intégrale d'un champ de vecteurs le long d'une ligne brisée, par la méthode de Simpson sur chaque segment · `line_integral` | ★★ | 30 | §4 | C, E | pytest | — |
| MB6.16 | 🔨 | La corrélation de rangs de Spearman, ex aequo compris · `spearman_rho` | ★ | 20 | §6 | C, E | pytest | — |
| MB6.17 | 🔮 | Prédire l'intégrale d'un champ de gradient et d'un champ tournant le long d'une boucle triangulaire, dans un sens, dans l'autre et deux fois, puis vérifier | ★ | 15 | §4 | C | wbm | MB6.15 |
| MB6.18 | 🔬 | Deux mesures corrélées : la moyenne marginale (dépendance partielle) et la moyenne conditionnelle d'une même fonction, simulées pour plusieurs corrélations et comparées aux formules gaussiennes | ★★ | 25 | §3 | C, E | wbm | — |
| MB6.19 | 🎨 | Les lignes de niveau d'une fonction de deux variables, deux chemins entre les mêmes points, et l'intégrale du gradient cumulée le long de chacun | ★ | 25 | §4 | C | manuel | MB6.15 |
| MB6.20 | 🐛 | Chasse à l'erreur : des poids de coalition sans le facteur 1/n, des ex aequo classés dans l'ordre d'apparition, une interpolation linéaire aux poids échangés | ★ | 20 | §1 §5 §6 | C, E | wbm | — |
| MB6.21 | 🛠️ | Un test de propriété sur des lignes brisées tirées au hasard : le chemin inversé change le signe, un segment coupé en deux ne change rien, un champ de gradient donne f(fin) − f(début) | ★ | 25 | §4 | C | manuel | MB6.15 |
| MB6.22 | 🏆 | Défi : les indices de Shapley-Shubik exacts d'un conseil de 25 membres, sans parcourir ses coalitions une à une, en comptant par taille et par poids celles où chaque membre est pivot | ★★★ | 45 | §1 | C | wbm | MB6.13 |

*Notes* : Frontières : les ∂ B6.2 (φ_i = w_i (x_i − E[x_i]) d'un modèle linéaire avec un fond, la valeur de base f(b̄), le logit contre la probabilité, le produit x₁x₂ avec une ligne de fond et φ₁ = ½(x₁ − b₁)(x₂ + b₂), la ligne moyenne de ✏️ B6.1) et B6.6 (l'identité de Chouldechova par les effectifs puis par Bayes, son contrôle, le rapport des cotes à PPV et FNR égaux, la PPV croissante en p à FPR et FNR égaux, les issues, COMPAS, ce qu'ajoute Kleinberg) ; ✏️ B6.1 (Shapley exact à la main d'un modèle à trois features avec un fond de deux lignes), ✏️ B6.3 (gradients intégrés à la main, règles gauche, droite et trapèzes, le plus petit nombre de pas, la référence, captum), ✏️ B6.4 (Grad-CAM à la main), ✏️ B6.5 (audit de deux groupes, Δ_DP, Δ_EO, règle des quatre cinquièmes), 🧮 B6.7 (coût de Shapley exact, de KernelSHAP et de TreeSHAP), 📄 B6.11 (Lundberg et Lee, leurs deux jeux, le noyau de KernelSHAP), les quiz B6.Q3 (dépendance partielle de x₁x₂ à x₂ = ±1 et de 3x₁ + x₂²), B6.Q4 (les axiomes lus sur une explication base + Σφ), B6.Q5 (le fond), B6.Q6 (deux features corrélées ou copiées), B6.Q7 (min(x, 1) et la ligne de référence), B6.Q9 (randomisation, « Spearman = 1 ⇒ mêmes valeurs ? »), B6.Q11 (critères compatibles ?), les 🔨 B6.14 (`shapley_values`), B6.18 (`integrated_gradients`, `grad_cam`) et B6.23 (`group_rates` et les deux écarts), 🐛 B6.21 (Grad-CAM à l'envers, dont l'alignement `align_corners`), 🔬 B6.22 (le test de randomisation et la corrélation de Spearman), et 💼 B6.E2 (une valeur SHAP et ses limites). Vigilance sans frontière : 🔬 B6.27 (repondération et seuils par groupe sur Adult) et 📦 B6.24, 📈 B6.25 (intervalles d'un écart) côtoient le §8 : autres cadres, autres nombres, et aucun seuil choisi comme quantile des scores des positifs. MB6 travaille hors des réseaux et hors des données de personnes : des jeux (un conseil à vote pondéré, des hameaux qui partagent une conduite d'eau, trois amis et un taxi), des fonctions écrites (le rendement d'une parcelle, le travail d'une force, un coût à trois facteurs, un indice régional), des grilles de capteurs, deux topos d'escalade qui cotent les mêmes voies, des lignes de production, des laboratoires et des trains ; jamais un modèle entraîné, une feature, un fond (*background*) de données, un réseau, une image, un pixel, une carte d'activation, un canal, un logit, un client, un prêt, un candidat, des groupes de personnes ni un dataset de workbookIA. SHAP, KernelSHAP, TreeSHAP, LIME, gradients intégrés, saillance et Grad-CAM ne sont nommés que dans les encadrés 🔗 « Dans workbookIA » et 💻 de la fiche (au plus une phrase sur KernelSHAP, sans son noyau), jamais dans un énoncé. §1-§2 (jeux) : la valeur de Shapley est définie par les ordres d'arrivée, puis par les poids des coalitions (fiche : n = 3 et n = 5, jamais n = 4 comme exemple principal, l'encadré de la fiche de B6) ; l'estimation par des ordres tirés au hasard est un paragraphe du §1 (sans biais, efficacité exacte à chaque ordre, Hoeffding) et la dernière question de ✏️ MB6.1, sans fonction `mymath` ; aucun exercice ne demande seul le poids d'une coalition d'un joueur parmi trois (B6.1 d), le nombre de coalitions sans i pour n = 5 (B6.Q4 e), une valeur manquante d'une explication base + Σφ (B6.Q4 a), ni « f(a, b) = f(b, a) ⇒ mêmes parts ? » (B6.Q4 d) ; 🧠 MB6.Q1 porte sur des jeux abstraits (un conseil, un partage de coûts), jamais sur une explication f(x) = base + Σφ. ✏️ MB6.1 : un conseil à quatre membres où un membre est nul et deux membres de poids différents ont le même pouvoir (par exemple [7 ; 5, 3, 2, 1], total 11) ; les pivots se comptent sur les 24 ordres ; la symétrie des deux membres se vérifie sur v ; Hoeffding (M11) donne le nombre d'ordres tirés pour un indice à ± 0,05. ✏️ MB6.2 : trois hameaux aux besoins emboîtés (le coût d'une coalition est celui de son membre le plus éloigné, c(S) = max) : la valeur de Shapley par les six ordres, les dividendes (de signes alternés), la règle de l'aéroport retrouvée par l'additivité (une somme de jeux de tronçon), l'efficacité, la symétrie, le joueur nul vérifiés. Le jeu additif v(S) = c + Σ_{j∈S} a_j ⇒ φ_i = a_i est un énoncé de la fiche sur des jeux abstraits : aucun exercice ne l'applique à un modèle linéaire, à un fond ni à une fonction de deux variables avec une ligne de référence (∂ B6.2). L'unicité (∂ MB6.8, ★★★, hors parcours essentiel) est énoncée dans la fiche avec son idée ; le 💼 MB6.E1 en demande l'argument en une minute ; « une interaction se partage également entre ses membres » se lit sur φ_i = Σ_{T∋i} d_T/|T|, jamais sur un produit de deux facteurs. Le 🗣️ MB6.12 (le taxi) n'a pas de nombres. Le 🏆 MB6.22 : un conseil de 25 membres aux poids entiers (petits), les indices exacts par un comptage par taille et par poids (une programmation dynamique) et `coalition_weights`, comparés à des valeurs de référence enregistrées, en moins d'une seconde ; ce n'est pas l'énumération des coalitions de `shapley_values` (B6.14). §3 (fixer une variable) : la moyenne marginale E[f(v, X_{−j})] est la dépendance partielle de workbookIA ; la moyenne conditionnelle E[f(X) | X_j = v] lui est opposée, sur des fonctions écrites et des variables gaussiennes corrélées (M25a) ; la fiche relie cette opposition au jeu « marginal » E[f(x_S, X_{S̄})] et au jeu « conditionnel » d'une fonction, en une phrase, sans fond ni calcul de Shapley. ✏️ MB6.3 : deux modèles de rendement écrits, l'un séparable (une fonction de la pluie plus une fonction de l'engrais), l'autre non (une fonction de l'écart pluie − engrais, de dérivée croisée non nulle) ; les courbes ICE de l'engrais pour trois parcelles, la dérivée croisée, puis, pour le modèle séparable, affine en la pluie, la moyenne marginale sous une loi gaussienne de la pluie et la moyenne conditionnelle quand (pluie, engrais) est un couple gaussien corrélé : l'écart est affine en l'engrais, la moyenne conditionnelle lui prête l'effet de la pluie. Ni produit x₁x₂ à facteur centré, ni « la dépendance partielle est-elle plate ? », ni « combien de pentes ? » (B6.Q3 a, b), ni courbes centrées (B6.Q3 d), ni loi uniforme sur [−1, 1], ni indicatrice 𝟙[x₃ ≥ 0] (Goldstein). 🔬 MB6.18 : deux mesures corrélées d'un même objet (la hauteur et le diamètre d'arbres, ou la température et l'humidité d'une serre), une fonction écrite, ρ = 0 ; 0,5 ; 0,9, la moyenne conditionnelle estimée dans une fenêtre |x_j − v| ≤ h, comparée aux formules ; jamais `sklearn.inspection` (`partial_dependence`, B6.12), ni deux copies d'une même variable (B6.16, B6.Q6). 🧠 MB6.Q2 ne demande ni la forme de la dépendance partielle d'un produit, ni un nombre de pentes, ni une dépendance partielle en un point d'une fonction donnée (B6.Q3 a à c). §4 (chemins) : un chemin est paramétré par t ∈ [0, 1] (jamais α, la variable des gradients intégrés) ; le théorème du gradient et l'indépendance du chemin sont démontrés dans la fiche (TFA de M02a et chaîne de M17) ; les règles de Riemann, des trapèzes et de Simpson sont rappelées de M02a (ordres d'erreur, exactitude du trapèze pour une intégrande affine) sans exercice : aucun « plus petit nombre de pas », aucune table de quatre règles, aucun captum (✏️ B6.3). ✏️ MB6.4 : un champ de gradient polynomial le long d'un segment, d'un chemin en escalier et d'un arc de parabole, puis un champ aux dérivées croisées différentes (pas (y, 0), l'exemple du stub) le long de deux chemins de mêmes extrémités. ✏️ MB6.5 (parcours complet) : un coût = prix × quantité × taux de change entre deux dates (trois facteurs, référence non nulle) : les parts des facteurs le long du segment (trois intégrales de polynômes), puis la moyenne des six chemins en escalier (la valeur de Shapley du jeu de la fonction), qui coïncident (le théorème multilinéaire de la fiche, démontré par les jeux d'unanimité dans un bloc repliable) ; que deux partages diffèrent pour une fonction qui n'est pas multilinéaire est un exemple de la fiche (par exemple x²y entre deux points sans coordonnée nulle) et un item de 🧠 MB6.Q3, sans exercice de calcul. Jamais un produit de deux facteurs du premier degré avec une référence (∂ B6.2.8), ni dans un exercice, ni dans la fiche (exemple, corollaire ou bloc de la preuve du théorème multilinéaire), ni dans une flashcard, une solution ou une variante ; ni x y² ou x e^y (M05b), ni une sigmoïde, ni un minimum ou un plafond (la saturation reste un exemple de la fiche, sur un barème plafonné, sans exercice : B6.Q7), ni règle numérique ni nombre de pas. Euler (fonctions homogènes, depuis r = 0 la part x_i ∂_i f(x)/k ; une Cobb-Douglas dans la fiche) n'a qu'un item de 🧠 MB6.Q3 ; jamais « gradient × entrée ». Le 🔮 MB6.17 prend une boucle triangulaire et le champ tournant (−y, x) (deux fois l'aire) avec un champ de gradient, jamais le champ (y, 0) de la docstring ; le 🎨 MB6.19 trace les lignes de niveau d'une fonction écrite ; le 🛠️ MB6.21 écrit trois propriétés de `line_integral` (sens inversé, segment coupé en deux, champ de gradient). §5 (grilles) : la moyenne d'un gradient sur une grille est la dérivée par un décalage uniforme, divisée par HW ; ✏️ MB6.6 la calcule pour un indice régional écrit sur une grille 3 × 4 de températures (par exemple des degrés-jours pondérés, y = Σ c_ij max(0, T_ij − 10)), sous un réchauffement uniforme, puis agrandit la grille en 6 × 8 dans les deux conventions (centres alignés, coins alignés), avec l'écart entre les deux conventions (au plus un demi-pas ; ici un quart de pas aux bords) : on calcule les coordonnées d'origine de toutes les cases d'une ligne et les valeurs de quelques cases, pas les 48 ; jamais de canaux, de combinaison de cartes par des poids suivie d'une partie positive, de normalisation par le maximum, ni de carte agrandie 8, 24 ou 32 fois (✏️ B6.4, 🐛 B6.21) ; `align_corners` de PyTorch et `scipy.ndimage.zoom` sont nommés dans un 💻. §6, Spearman (lacune) : la fiche l'enseigne sur deux topos d'escalade qui cotent les mêmes huit voies (un ex aequo ; à la génération, session 75, au lieu des deux juges et des huit boulangeries du plan, cadre déjà pris en MB4), avec la formule 1 − 6Σd²/(n(n² − 1)) démontrée dans un bloc repliable ; 🧠 MB6.Q4 et 🔨 MB6.16 ; aucun « ρ = 1 ⇒ mêmes valeurs ? » ni le contre-exemple (1, 2, 3)/(10, 20, 30) (B6.Q9 d), aucun test de randomisation, SSIM ni carte de saillance (B6.22). Le 🐛 MB6.20 : des poids s!(n − 1 − s)!/(n − 1)! (sans le 1/n : leur somme pondérée vaut n), des rangs donnés dans l'ordre d'apparition aux ex aequo, une interpolation (1 − t) b + t a au lieu de (1 − t) a + t b ; pas d'erreur d'alignement des coins (🐛 B6.21). §7-§8 (équité) : groupes G (deux lignes de production, deux usines, deux lignes de trains, deux laboratoires), label Y (défaut, panne, retard, contamination), décision Ŷ, score S ; un ⚠️ de la fiche : le score S d'un classifieur (M03) n'a rien à voir avec le score en x de MB5 ni avec la fonction score de MB8 ; les définitions par groupe et l'identité de M03 §8 (FPR, prévalence, precision, recall) sont rappelées en une ligne par renvoi, jamais redémontrées ni appliquées à de nouveaux nombres : aucun rapport des cotes à PPV et FNR égaux (∂ B6.6.6), aucune PPV calculée à FPR et FNR égaux (∂ B6.6.7), aucun classifieur parfait ni Δ_DP (B6.Q11). MB6 ajoute les critères comme indépendances (M25b), l'incompatibilité indépendance et séparation et la repondération (∂ MB6.10, deux preuves de trois lignes), et Kleinberg et coll. pour des scores (∂ MB6.9 : l'identité p(1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] par l'espérance totale (M25b), puis l'impossibilité ; une petite table de scores calibrés en contrôle : à la génération, session 75, celle de la ligne 1 de ✏️ MB6.7, puisque la fiche §7 prend un service météo, au lieu des retards de trains du plan) : la fiche de B6 l'énonce et l'admet, ∂ B6.6.9 demande seulement ce qu'il ajoute à COMPAS, et MB6 ne parle pas de COMPAS. ✏️ MB6.7 : deux lignes de taux de défauts différents (par exemple 8 % et 20 %), un contrôle de mêmes TPR et FPR sur les deux : les taux de rejet diffèrent ; sur une ligne, deux points (FPR, TPR) donnés par deux seuils, la probabilité de tirage qui atteint un TPR visé et le FPR obtenu ; une table de comptes ligne × défaut, les poids P(g)P(y)/P(g, y) et les taux de défaut pondérés égaux. 🔗 MB6.11 : deux laboratoires qui détectent une contamination, avec peu et beaucoup d'échantillons contaminés : TPR, écart, erreur type, intervalle de Wald de l'écart, et ce que change un quadruplement du petit effectif ; le bootstrap stratifié en une phrase ; ni Adult, ni 2 000 ou 500 tirages, ni tableau d'audit (📦 B6.24, 📈 B6.25), ni Bonferroni. Évités (règle de partage), de workbookIA B6 : les modèles f = 2x₁ + x₁x₂ (x = (3, 2), fond (1, 0) et (1, 2), v = 3, 9, 4, 12, φ = (7, 2)), f = 2x₁ + x₁x₃ + x₂ (x = (2, 1, 3), fond (0, 2, 0) et (2, 2, 2), ligne moyenne (1, 2, 1), φ = (3,5 ; −1 ; 2,5) et (4 ; −1 ; 3), variante (2, 2, 0)), f = x₁ + 2x₂ + x₁x₂ (client (2, 1), fond (0, 1)), f = 2x₁ − 3x₂ (x = (4, 1), moyennes (3, 1) et (5, 2)), f = 2x₁ + 2x₂ et 4x₁ en (1,5 ; 1,5), f = 3x₁ + x₂² (x₂ ∈ {0, 1, 2}, 7,67), f = x₁x₂ à x₂ = ±1, les poids w = (1,5 ; −2 ; 0,5), (2, −1, 0,5), (0,5 ; −2 ; 0) avec w₀ = 1 et x = (4, 1, 7) ; les jeux fièvre/toux (2 et 5, φ = (1, 1)) et des trois hommes (5, 4, 0 ; φ = (3, 2, 0) ; variante (5, 5, 0)) ; f(x) = 0,72, base 0,40, φ = 0,15 ; −0,05 ; 0,22 ; les parts 0,3 et −0,1 ; n = 4 et ses poids 1/4 et 1/12 comme exemple principal (1, 3, 3, 1 coalitions, 16 coalitions, 8 arêtes) ; n = 3 et le poids 1/6 demandé seul ; n = 5 et 16 coalitions ; n = 8 et B = 50 (12 800), n = 12 (204 800), n ∈ {10, 20, 50}, 2n + 2 048, ≤ 2^n − 2, 150 000 lignes par seconde, 10! = 3 628 800, 12!, 40 320, 479 millions, 4 096, T = 100 arbres et L = 31 feuilles, `max_features=12`, `max_samples` 100 ; σ(x₁x₂ − 2) en (2, 3) (0,9820 ; 0,1192 ; 0,8628 ; 0,0530 ; 0,0353 ; 0,106 ; 0,212 ; 0,4314) ; f = x₁² + 3x₂ (en (2, −1) avec la référence 0 puis (1, 0), et en (1, 1)) ; f = x₀x₁ + x₂³ en (1, 2, −1) et ses parts ; f = x₀² + 3x₁ ; f = min(x, 1) en 3 (références 0 et 2) ; f = x³ en 2 (9 au lieu de 8) ; α³ avec n = 2 (0,0625 ; 0,5625 ; 0,21875 ; 0,3125) ; 5, 6, 7, 20, 100, 133, 134 et 200 intervalles, la table des quatre règles (0,8301 … 0,8628), « 20 à 300 pas à 5 % », n/(n + 1), α = 0,63, onze points ; les cartes de la fiche de B6 (A¹ = [[1, 0], [2, 1]], A² = [[0, 3], [1, 0]], A³ = [[2, 2], [0, 1]], α = (0,5 ; −1 ; 0,5), [[1,5 ; −2], [0 ; 1]], [[1 ; 0], [0 ; 0,67]]), de ✏️ B6.4 (A¹ = [[1, 0, 0], [2, 1, 0], [3, 2, 1]], A² = [[0, 1, 2], [0, 0, 1], [0, 0, 0]], leurs gradients, α = (1 ; −0,5), α′ = (−0,5 ; 1)) et de la docstring de `grad_cam` ([[1, 2], [0, 1]], [[0, 1], [3, 0]]) ; les agrandissements 8 × 8 et 72 × 72, 12 pixels, `layer4` ÷ 32 (1 × 1, 4 × 4, 7 × 7 ; 32, 96, 128, 160 et 224 pixels), `layer1` 56, les centres 16, 48 et 80, le décalage de 16 pixels, Sobel ; (1, 2, 3) contre (10, 20, 30), les corrélations de B6.20 et B6.22 (0,96 ; 0,97 ; 0,59 ; …), 9/48, 15/48 et 22/48 ; l'exemple de Goldstein (y = 0,2x₁ − 5x₂ + 10x₂𝟙[x₃ ≥ 0], pentes ±5, 3 000 points) et Friedman ; les tranches d'âge (n = 200, 500, 300 ; 20/20/10/150, 150/50/30/270, 60/30/21/189 ; taux de base 0,20, 0,40, 0,30 ; 0,21 ; 0,25 ; 0,0375 ; 0,839), les matrices F et H (72/48/19/361 et 256/64/40/280, variante 96/24/38/342), [[88, 12], [10, 40]], les docstrings de `group_rates` ([1, 0, 1, 0, 1, 1, 0, 0]…) ; les taux de base 0,6 et 0,25, 0,24 et 0,5, 0,2 et 0,4, 0,5 ; les paires (PPV, FNR) (0,7 ; 0,25), (0,8 ; 0,2), (0,8 ; 0,3), (0,75 ; 0,25), les FPR 0,080, 0,214, 0,055, 0,175, FPR = 0,1 avec FNR = 0,2, PPV 0,716 et 0,889, p ≈ 0,286 ; les poids de repondération 1,65 ; 0,8375 ; 0,825 et le taux pondéré 0,33, les groupes u × 6 et v × 4 (poids 0,75 ; 1,5 ; 2,0 ; 2/3) ; les TPR 0,856 et 0,912, FPR 0,158 et 0,256, le TPR visé 0,80 (quantile 0,2 ; 0,799 et 0,800 ; 0,113 et 0,126), les seuils 0,356 et 0,524, le TPR visé 0,638 ; Adult (3 165 et 350, 6 604 et 1 987, 0,569 ; 0,663 ; 12 positifs sur 1 647 ; 89 et 120 positifs, ± 0,088 ; 2 000 et 500 tirages ; Δ_EO < 0,07), la règle des quatre cinquièmes ; COMPAS, Gender Shades, Obermeyer, Amazon, NIST ; California, Penguins, CIFAR-10, le ResNet du B1, le loup et le husky, la radiographie, Mme D., le code postal, la fintech, les prêts ; de workbookIA B7 (voisin, sans chapitre de maths) : les six graines 71,2 ; 70,5 ; 72,1 ; 69,8 ; 71,6 ; 70,9, les cinq valeurs 64,2 … et 64,9 …, les dix latences 12, 15, 11, 14, 13, 40, 12, 16, 13, 12, 900 × 10 ms + 100 × 200 ms, les PSI et les luminosités ; et, de ce dépôt, l'exemple de M03 §8 (precision 0,6, recall 0,8, prévalences 30 % et 10 %, FPR 0,229 et 0,059 ; le désabonnement 0,8 ; 0,6 ; 0,3 ; 0,2 ; 0,1), la table de M03.15 (48/12/28/112 et 16/4/18/162), les fonctions x e^y, x y² en (1, 2) et (2, 1), x²y + y² et x²y + y³ de M05b, les exemples des docstrings de `integrate` (M02a), et ceux du stub `attribution` (n = 6 et ses poids 1/6, 1/30, 1/60 ; le jeu s ↦ s² et ses dividendes 1 et 2 ; 5 u_{1,2} ; le champ (3x² + y, x) de x³ + x y et le chemin (0, 0) → (1, 0) → (1, 2) ; le champ (y, 0) le long de (0, 0) → (1, 0) → (1, 1) et de (0, 0) → (0, 1) → (1, 1) ; 3x² de 1 à 3 puis à −1 (et l'ancien exemple, 3x² de 0 à 2 puis à 1, proche de `simpson(lambda x: x ** 3, 0, 2, 2)` de M02a) ; (0,5 ; 2 ; 1,5 ; 4) contre (1, 8, 27, 64) et ρ = 0,8 ; (2, 2, 5, 1) contre (4, 3, 6, 0) ; (7, 7, 7)) ; ajoutés à la génération (session 75, relecture de partage) : les bornes d'intervalles de B6.24 et B6.27 (0,058 ; 0,042 ; 0,150 ; 0,161 ; 0,147 ; 0,177 ; 0,011 ; 0,020 ; 0,067 ; 0,087) et les Δ_EO 0,076 ; 0,016 ; 0,012 ; le test d'usine de ✏️ M11 (3 %, 92 %, 6 %) ; la fonction de ✏️ M05b.7 (x³y² − e^{xy}) ; le 🗣️ M17.13 (taux de change entre monnaies) ; le ferry de M26.3 ; les boulangeries et les jurys de MB4 ; la serre de M25a.26 ; et les erreurs fréquentes des corrigés de B6.1, B6.5, ∂ B6.6, B6.14 et B6.23 (la fonction en la moyenne, des poids uniformes, une seule contribution marginale, un taux divisé par tout le groupe ou sur toutes les pièces, le taux de base pris pour le taux de décision, 0 au lieu de non défini) ne reviennent nulle part, ni en valeur fausse, ni en message, ni en ⚠️, ni en flashcard, ni en annexe. Conventions : joueurs numérotés de 0 à n − 1 dans le code, par des lettres ou de 1 à n sur papier ; N le grand groupe, S̄ le complément de S ; v(∅) quelconque, d'où l'efficacité Σφ_i = v(N) − v(∅) ; la référence d'un chemin est notée r (ni b, ni x′, ni « fond ») ; un chemin γ de paramètre t ∈ [0, 1] ; « taux de base » p_g, « taux de détection » pour le TPR ; ρ de Spearman noté ρ_S quand il voisine avec la corrélation ρ d'un couple gaussien. `attribution` : NumPy et les modules `math`, `fractions` et `itertools` ; ni SciPy (`scipy.stats.rankdata`, `spearmanr`, `pearsonr`, `scipy.integrate`), ni `np.corrcoef`, ni `np.cov`, ni le module `statistics` (`statistics.correlation(…, method='ranked')` est le ρ de Spearman), ni pandas ; les imports relatifs des modules de l'apprenant sont permis (`from .integrate import simpson`, M02a). Les fonctions écrivent les briques : `coalition_weights(n_players, exact=False)` (les poids s!(n − 1 − s)!/n!, en `Fraction` ou en flottants ; oracles `math.comb` et `Fraction`), `harsanyi_dividends(v, n_players)` (un jeu abstrait, v : frozenset → réel, appelé une fois par coalition ; un dict des 2^n dividendes ; oracle : le jeu reconstruit par v(S) = Σ_{T⊆S} d_T, et la valeur de Shapley moyennée sur les ordres par `itertools.permutations`), `line_integral(field, points, n_sub=20)` (un champ appelé point par point, une ligne brisée quelconque, Simpson sur chaque segment, un scalaire ; oracles `scipy.integrate.quad` et le théorème du gradient) et `spearman_rho(x, y)` (rangs moyens, `nan` quand un échantillon est constant ; oracle `scipy.stats.spearmanr`). Aucune fonction ne rend des valeurs de Shapley exactes (celles de B6.14 viennent d'un modèle f, d'un point x et d'un fond, par l'énumération des coalitions), ni les parts des coordonnées le long d'un segment : `line_integral` a un autre contrat que `integrated_gradients` de B6.18 (un gradient vectorisé, un point et une référence, quatre règles, `n_steps` intervalles, une attribution par coordonnée) ; aucune fonction de dépendance partielle (`partial_dependence` du plan est retirée : c'est le nom de `sklearn.inspection.partial_dependence`, que B6.12 appelle), de taux par groupe ni d'écart d'équité (B6.23). Les exercices ne reprennent pas les exemples du stub. Pas de MML : le livre ne traite ni les jeux coopératifs, ni les intégrales de chemin, ni l'équité ; donc pas de 📖. Références libres possibles, à vérifier en génération (annexes/ressources.md) : M. J. Osborne et A. Rubinstein, A Course in Game Theory, ch. 14 (la valeur de Shapley) ; S. Barocas, M. Hardt et A. Narayanan, Fairness and Machine Learning, ch. 3 (indépendance, séparation, suffisance ; workbookIA B6 le cite : renvoyer à ses sections sans reprendre ses exemples) ; J. Kleinberg, S. Mullainathan et M. Raghavan (2017) pour le §7 ; L. S. Shapley (1953) et J. C. Harsanyi (1963) pour le §2. Parcours essentiel : l'unicité (∂ MB6.8), le partage multilinéaire (✏️ MB6.5), le 💼, le 🔨 des dividendes, le 🔮, le 🎨, le 🛠️ et le 🏆 hors parcours. **Durée** : 13,0 h en parcours complet, 9,3 h en parcours essentiel, recalée à la génération (session 75) par l'auteur des exercices, la re-résolution à l'aveugle et l'apprenant simulé ; à la session 69 : 12,1 h en parcours complet, 8,8 h en parcours essentiel (lecture 125 min, soit une fiche d'environ 6 200 mots de prose ; 15 flashcards), au lieu des 8 h du plan et des 11 h visées : le chapitre comble quatre lacunes qu'aucun chapitre publié ne couvre (jeux coopératifs et valeur de Shapley, corrélation de rangs de Spearman, interpolation bilinéaire, écart de deux proportions indépendantes) et la forme « scores » de l'impossibilité, avec la composition du §13 au bas de chaque fourchette et des durées réalistes (les relectures de M25a à M28 ont relevé les durées de 20 à 40 %). Retirés du plan pour tenir : l'estimation par permutations comme section et comme fonction (`shapley_monte_carlo`), les fonctions de moyenne marginale et conditionnelle (une ligne de NumPy dans le 🔬), une ✏️ de Spearman (le 🔨 et le quiz suffisent), un exercice de saturation (B6.Q7). Après les relectures : le 🏆 MB6.22 passe de 30 à 40 min (+1,1 h au-dessus des 11 h visées, pour la raison écrite ci-dessus).

<a id="mb8"></a>
## MB8 · Gradient de politique

**Partie** VII · **prépare** workbookIA B8 · **dossier** `chapitres/mb8_gradient_politique/` · **MML** — · **sessions de génération** 1

Les outils statistiques du gradient de politique, hors de tout agent. D'abord la fonction score d'une loi, d'espérance nulle, et l'information de Fisher ; l'estimateur « score » de la dérivée d'une espérance, qui dérive une probabilité là où la dérivée par le chemin de M25b échoue ; la réduction de sa variance par une variable de contrôle, la baseline optimale et les baselines de groupe. Puis la valeur d'une politique softmax tabulaire, dérivée à partir du système de Bellman de M26 : la loi d'occupation actualisée et l'avantage, d'espérance nulle ; les retours à k pas et le λ-retour, démontrés à partir du télescopage de M26. Enfin l'échantillonnage d'importance (poids, taille effective, poids tronqués) et deux estimateurs de la KL par échantillons ; le modèle de Bradley-Terry des comparaisons par paires et la cote Elo ; le principe variationnel de Gibbs, la loi qui maximise une moyenne moins β fois une KL. workbookIA B8 applique ces outils à REINFORCE, à GAE, à PPO, au modèle de récompense et à DPO.

**Temps** : 14,8 h en parcours complet, 12,7 h en parcours essentiel (lecture 160 min, 16 flashcards).

**Objectifs**

- Calculer la fonction score d'une loi usuelle, vérifier qu'elle est d'espérance nulle, et calculer l'information de Fisher de deux façons.
- Dériver l'espérance d'une fonction, même discontinue, par rapport au paramètre d'une loi par la méthode du score, et dire quand la dérivée par le chemin est préférable.
- Réduire la variance d'une estimation de Monte-Carlo par une variable de contrôle, et calculer la baseline optimale d'un estimateur score.
- Distinguer une baseline sans biais (la moyenne des autres tirages) d'une baseline qui biaise (la moyenne du groupe, tirage compris).
- Calculer le gradient de la valeur d'une politique softmax tabulaire par le système de Bellman, et l'écrire avec la loi d'occupation actualisée et l'avantage.
- Écrire un retour à k pas et un λ-retour, les relier aux erreurs TD, et calculer leur biais quand les valeurs estimées sont fausses.
- Estimer une espérance sous une loi à partir de tirages d'une autre, calculer la taille effective, tronquer des poids, et estimer une KL par k₁ ou k₃.
- Ajuster un modèle de Bradley-Terry à un tournoi, dire quand ses forces existent et ce qu'elles identifient, et lire une mise à jour Elo comme un pas de gradient.
- Trouver la loi qui maximise une moyenne moins β fois la KL à une loi de référence, et sa valeur.

**Sections de la fiche**

- §1 La fonction score d'une loi : espérance nulle et information de Fisher
- §2 Dériver une espérance par le score, et comparer à la dérivée par le chemin (M25b)
- §3 Réduire la variance : variables de contrôle, baseline optimale et baselines de groupe
- §4 Le gradient de la valeur d'une politique, sous forme matricielle (après M26)
- §5 Retours à k pas et λ-retour
- §6 L'échantillonnage d'importance : poids, taille effective, poids tronqués ; estimer une KL par échantillons
- §7 Comparaisons par paires : le modèle de Bradley-Terry et la cote Elo
- §8 Le principe variationnel de Gibbs : maximiser une moyenne moins β fois une KL

**Notions enseignées** : fonction score d'une loi s_θ(x) = ∂_θ ln p_θ(x) (le score « en θ », à distinguer du score en x de MB5) ; scores des lois de Bernoulli, binomiale, de Poisson, exponentielle (taux) et normale (moyenne) ; E_θ[s_θ(X)] = 0 quand le support ne dépend pas de θ (contre-exemple : la loi uniforme sur [0, θ]) ; le score total d'un échantillon s'annule au maximum de vraisemblance (rappel M04, M13a) · information de Fisher I(θ) = Var(s_θ) = −E[∂²_θ ln p_θ] (démontrée sous l'échange de la dérivée et de l'intégrale, admis) ; I(θ) d'un échantillon i.i.d. = n I(θ) ; au second ordre, KL(p_θ ‖ p_θ′) ≈ ½ I(θ)(θ′ − θ)² · la dérivée d'une espérance par le score : d/dθ E_θ[f(X)] = E_θ[f(X) s_θ(X)] (lois discrètes, puis à densité), valable pour f discontinue (une indicatrice) ; l'estimateur de Monte-Carlo sans biais et sa variance ; comparée à la dérivée par le chemin de M25b §7 (rappel) : même espérance, variances différentes, le chemin nul sur une indicatrice · variables de contrôle (control variates) : f − c(h − E[h]) sans biais, c* = Cov(f, h)/Var(h), variance (1 − ρ²)Var(f) ; pour l'estimateur score, toute constante b donne (f − b)s sans biais (E[s] = 0) ; baseline optimale b* = E[f s²]/E[s²] (une moyenne de f pondérée par s²), différente de E[f] en général ; Var((f − b)s) est un trinôme en b, minimal en b* · baselines de groupe : sur n tirages i.i.d., la moyenne des n − 1 autres f est une baseline sans biais ; la moyenne des n, tirage compris, multiplie l'estimateur par (n − 1)/n ; diviser par l'écart-type du groupe garde le signe de chaque terme, mais l'espérance n'est plus exactement proportionnelle à la dérivée · le gradient de la valeur d'une politique softmax tabulaire (le prolongement promis par M26) : dériver V = r_π + γP_πV donne ∂V = (I − γP_π)⁻¹(∂r_π + γ(∂P_π)V) ; ∂V(s₀)/∂z(s, a) = ν_{s₀}(s)/(1 − γ) · π(a | s) A^π(s, a), avec la loi d'occupation actualisée ν_{s₀} de M26 §5 et l'avantage A^π = Q^π − V^π ; Σ_a π(a | s)A^π(s, a) = 0 ; la forme Σ_s ν(s) Σ_a π(a | s) ∂ln π(a | s) Q^π(s, a) ; la jacobienne de la softmax (la matrice de M17 §7, reconnue au chapitre 17 de workbookIA) ; la pondération (1 − γ)γᵗ des états visités, énoncée ; vérification par différences finies (M05a) · retours à k pas G^(k) = Σ_{j<k} γʲ R_{t+j} + γᵏ V(S_{t+k}) ; G^(k) − V(S_t) = Σ_{l<k} γˡ δ_{t+l} (le télescopage de M26 §8, tronqué) ; le λ-retour, moyenne des G^(k) de poids (1 − λ)λ^{k−1}, et G^λ − V(S_t) = Σ_l (γλ)ˡ δ_{t+l} (démontré) ; λ = 0 et λ = 1 ; E[δ_t | S_t = s, A_t = a] = A^π(s, a) quand V = V^π ; biais γᵏ(Pᵏ e)(s) d'une valeur estimée fausse de e, et une variance qui croît en général avec k · échantillonnage d'importance (importance sampling) : E_p[f] = E_q[(p/q) f] quand q > 0 là où p f ≠ 0 ; sans biais ; E_q[w] = 1 ; variance, et poids de variance infinie ; poids auto-normalisés (biaisés, consistants, et seuls possibles quand p n'est connue qu'à une constante près) ; taille effective (Σw)²/Σw² de Kish ; poids calculés en log, exp(ln p − ln q) ; poids tronqués min(w, c) : un biais contre une variance ; lien avec Horvitz-Thompson (M20 §5) · estimer KL(q ‖ p) par des tirages de q, avec w = p/q : k₁ = −ln w (sans biais, de signe quelconque) et k₃ = (w − 1) − ln w (sans biais car E_q[w] = 1, et ≥ 0 terme à terme : −ln est convexe, au-dessus de sa tangente en 1, M05a) · le modèle de Bradley-Terry : P(i bat j) = σ(β_i − β_j) ; vraisemblance d'un tournoi ; les forces ne sont identifiées qu'à une constante près (contrainte Σβ = 0) ; une régression logistique sans constante sur des différences d'indicatrices (M13a) ; équations du maximum de vraisemblance : victoires observées = victoires attendues ; existence (le graphe des victoires est fortement connexe, énoncé ; un invaincu n'a pas de force finie) ; l'algorithme de Zermelo (MM, monotone, admis) ; la cote Elo, un pas de gradient stochastique sur la log-vraisemblance d'un match · le principe variationnel de Gibbs : pour une loi de référence π_ref et β > 0, E_π[r] − β KL(π ‖ π_ref) = β ln Z − β KL(π ‖ π*), avec π* ∝ π_ref e^{r/β} et Z = E_ref[e^{r/β}] (démontré par KL ≥ 0, M06) ; le maximum β ln Z ; les limites β → 0 (le meilleur choix) et β → ∞ (π_ref) ; r déterminée par π* et π_ref à une constante près ; les cas particuliers déjà vus : Boltzmann (M17), Hedge (M14), la température d'une loi (M28)

**Prérequis** : fonction du second degré (trinôme) et son minimum (R3) · suite et série géométriques (R5) · dérivée d'un logarithme et d'une composée (R7) · intégration par parties ; une valeur moyenne estimée par Monte-Carlo (M02a) · lois de Bernoulli, binomiale, de Poisson, exponentielle et normale ; espérance, variance, variance d'une somme de variables indépendantes ; simulation par inversion (M02b) · estimateur sans biais, erreur type d'une moyenne, covariance et corrélation, loi des grands nombres (M02c) · maximum de vraisemblance, log-probabilités, famille exponentielle (aperçu) (M04) · différences finies centrées et choix du pas, Taylor d'ordre 2, une fonction convexe est au-dessus de ses tangentes, log-sum-exp (M05a) · divergence KL et sa positivité (inégalité de Gibbs), entropie (M06) · inégalité de Cauchy-Schwarz (M07) · sigmoïde, logit, log-loss, régression logistique comme modèle probabiliste ; la convexité de log-somme-exp (sa dérivée seconde est une variance) (M13a) · poids exponentiels : l'algorithme Hedge (M14) · puissances d'une matrice d'adjacence et chemins d'un graphe (M16) · loi de Boltzmann et température, la matrice diag(p) − ppᵀ, covariance d'un vecteur one-hot (workbookIA 17 y reconnaît la jacobienne de la softmax, ∂ 17.7) (M17) · règle du produit pour des fonctions à valeurs matricielles (M18) · gradient estimé sans biais sur un échantillon, variance d'une moyenne de B tirages (M19) · estimateur de Horvitz-Thompson ; tableaux à trois axes et einsum (M20) · dériver une espérance par rapport à un paramètre de la loi : la dérivée par le chemin, l'hypothèse de domination, l'indicatrice où l'échange échoue ; espérance conditionnelle et totale (M25b) · MDP, politique, chaîne induite P_π et r_π, valeur d'une action Q^π, système de Bellman d'une politique fixée, loi d'occupation actualisée, erreur TD et télescopage ; tableaux (actions, états, états) (M26) · la probabilité a posteriori minimise la log-loss espérée (la log-loss est une règle de score propre) (M27) · la température d'une loi donnée par ses probabilités (M28) · la saturation de la softmax quand ses scores s'écartent (MB3)

**mymath** : `policy_gradient.py` (signatures figées) : `score_function_gradient`, `policy_gradient_exact`, `importance_weights`, `bradley_terry_fit`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B8.7 ∂ Le gradient de politique en une étape : l'astuce de la log-dérivée, puis la baseline sans biais · B8.1 ✏️ Cible DQN à la main : état terminal, puis cible Double DQN · B8.3 ✏️ Gradient du log d'une politique softmax à trois actions · B8.4 ✏️ GAE à la main sur quatre pas, pour λ = 0, 0,95 et 1 · B8.5 ✏️ Objectif clippé de PPO : quatre cas, valeur et gradient nul ou non · B8.6 ✏️ Préférences : loss de Bradley-Terry puis loss DPO sur une paire de réponses · B8.Q4 🧠 Double DQN : d'où vient la surestimation des valeurs Q ? · B8.Q6 🧠 REINFORCE : pourquoi soustraire une baseline ne biaise pas le gradient · B8.Q7 🧠 Avantage, erreur TD et GAE : ce que règle λ · B8.Q11 🧠 RLHF, DPO, GRPO : qui a besoin d'un modèle de récompense ou d'un critique ? · B8.17 📦 REINFORCE avec et sans baseline : variance du gradient et vitesse d'apprentissage · B8.18 🔨 compute_gae et explained_variance · B8.19 🔨 clipped_surrogate : valeur et gradient par rapport au ratio · B8.25 🔨 bradley_terry_loss et dpo_loss · B8.11 📄 Schulman et coll. (2017) : « Proximal Policy Optimization Algorithms » · B8.E2 💼 Explique PPO et le rôle du clipping · B8.E4 💼 PPO avec un modèle de récompense ou DPO pour aligner un modèle de langue : que choisis-tu ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| MB8.Q1 | 🧠 | La fonction score : espérance nulle, information de Fisher, support qui dépend du paramètre, et dériver une espérance par le score ou par le chemin | ★ | 5 | §1 §2 | C, E | manuel | — |
| MB8.Q2 | 🧠 | Variables de contrôle et baselines : ce qui garde l'espérance, ce qui réduit la variance, ce qui biaise | ★ | 5 | §3 | C, E | manuel | — |
| MB8.Q3 | 🧠 | Le gradient de la valeur d'une politique et le λ-retour : la loi d'occupation actualisée, l'avantage d'espérance nulle, le poids de chaque retour à k pas | ★ | 5 | §4 §5 | C, E | manuel | — |
| MB8.Q4 | 🧠 | Échantillonnage d'importance et KL estimée : support, taille effective, poids tronqués, k₁ ou k₃ | ★ | 4 | §6 | C, E | manuel | — |
| MB8.Q5 | 🧠 | Bradley-Terry et Elo : ce que les forces identifient, quand elles existent, ce que fait une mise à jour | ★ | 4 | §7 | C, E | manuel | — |
| MB8.Q6 | 🧠 | Le principe de Gibbs : la loi optimale, ses limites en β, et ce que mesure β ln Z | ★ | 4 | §8 | C, E | manuel | — |
| MB8.R1 | 🔁 | La jacobienne de la softmax, diag(p) − ppᵀ, lue comme la covariance d'un vecteur one-hot, et la loi de Boltzmann (M17) | ★ | 6 | §4 | C, E | manuel | — |
| MB8.R2 | 🔁 | Le système de Bellman d'une politique fixée, la loi d'occupation actualisée et le télescopage des erreurs TD (M26) | ★ | 7 | §4 §5 | C, E | manuel | — |
| MB8.R3 | 🔁 | La dérivée par le chemin, son hypothèse de domination, et l'indicatrice où elle échoue (M25b) | ★ | 6 | §2 | C, E | manuel | — |
| MB8.1 | ✏️ | Une attente au téléphone de loi exponentielle de taux θ, et une pénalité au-delà de c minutes : d/dθ P(X > c) par la formule fermée, par l'estimateur score (son espérance calculée) et par le chemin X = ξ/θ ; la variance de l'estimateur score à un tirage | ★★ | 35 | §2 | C, E | wbm | — |
| MB8.2 | ✏️ | Deux graines par godet (une loi binomiale B(2, θ)) et un prix selon le nombre de pousses : la dérivée de la recette moyenne, puis l'estimateur score sans baseline, avec b = E[f] et avec la baseline optimale, et leurs variances | ★★ | 35 | §3 | C, E | wbm | — |
| MB8.3 | ✏️ | Un camion de crêpes entre deux emplacements, une politique softmax dans l'un d'eux : la chaîne induite, les valeurs, la loi d'occupation actualisée, les valeurs et les avantages des deux actions, puis le gradient de la valeur par rapport aux deux logits | ★★ | 40 | §4 | C, E | wbm | — |
| MB8.4 | ✏️ | L'état d'une route (bonne, usée, en travaux) et des valeurs estimées fausses : le biais des retours à 1 et 2 pas, les poids (1 − λ)λ^{k−1} d'un λ-retour, et son biais quand l'erreur est la même partout | ★★ | 30 | §5 | C, E | wbm | — |
| MB8.5 | ✏️ | Un panel en ligne dont les classes d'âge ne suivent pas le recensement : les poids p/q, la dépense moyenne repondérée, la taille effective de Kish d'un petit échantillon, des poids tronqués (le biais), puis KL(q ‖ p) exacte et ses estimateurs k₁ et k₃ classe par classe | ★★ | 40 | §6 | C, E | wbm | — |
| MB8.6 | ✏️ | Un tournoi de babyfoot entre trois clubs : deux clubs seuls (la différence de forces en forme fermée), puis vérifier les équations du maximum de vraisemblance pour des forces proposées, la probabilité qu'un club batte un autre, une mise à jour Elo, et un club invaincu | ★★ | 35 | §7 | C, E | wbm | — |
| MB8.7 | ✏️ | Trois plats à la cantine : la loi de service qui maximise la satisfaction moyenne moins β fois la KL à la loi actuelle, pour deux valeurs de β, sa valeur β ln Z, comparée à la loi actuelle et au meilleur plat seul | ★★ | 30 | §8 | C, E | wbm | — |
| MB8.8 | ∂ | Les deux identités du score, E[s_θ(X)] = 0 et Var(s_θ) = −E[∂²_θ ln p_θ(X)], pour une famille à densité dont le support ne dépend pas de θ ; leur application aux lois de Poisson et exponentielle ; puis la loi uniforme sur [0, θ], où elles tombent | ★★ | 35 | §1 | C, E | manuel | — |
| MB8.9 | ∂ | La baseline optimale b* = E[f s²]/E[s²] d'un estimateur score ; sur n tirages, la moyenne des autres est une baseline sans biais, et la moyenne du groupe multiplie l'estimateur par (n − 1)/n | ★★ | 30 | §3 | C | manuel | — |
| MB8.10 | ∂ | Le gradient de la valeur d'une politique sous forme matricielle : dériver V = r_π + γP_πV, faire apparaître la loi d'occupation actualisée et la valeur des actions, puis remplacer Q^π par l'avantage | ★★★ | 40 | §4 | C, E | manuel | — |
| MB8.11 | 🔗 | Pont : la « loss de substitution » −(1/n)Σ(f(x_i) − b) ln p_θ(x_i), dont la dérivée, les f(x_i) et b tenus fixes, est moins l'estimateur score : sur le taux d'une loi de Poisson, puis ce que changent des f standardisés dans le batch | ★ | 20 | §2 §3 | C, E | wbm | — |
| MB8.12 | 🗣️ | Expliquer avec un club d'échecs pourquoi une cote Elo ne dit que des écarts de niveau, et pourquoi battre plus fort que soi rapporte plus de points | ★ | 10 | §7 | C, E | manuel | — |
| MB8.E1 | 💼 | « Comment dériver la probabilité d'un événement par rapport au paramètre d'une loi quand on ne peut pas dériver à travers les tirages, et comment rendre l'estimation moins bruitée ? » | ★ | 10 | §2 §3 | C, E | manuel | — |
| MB8.13 | 🔨 | L'estimateur score d'une dérivée sur un échantillon, avec une baseline constante ou la moyenne des autres tirages, et son erreur type · `score_function_gradient` | ★ | 25 | §2 §3 | C, E | pytest | — |
| MB8.14 | 🔨 | Le gradient exact de la valeur d'une politique softmax tabulaire, par le système de Bellman · `policy_gradient_exact` | ★★ | 35 | §4 | C, E | pytest | — |
| MB8.15 | 🔨 | Des poids d'importance calculés en log, auto-normalisés ou tronqués, et la taille effective de l'échantillon · `importance_weights` | ★★ | 25 | §6 | C, E | pytest | — |
| MB8.16 | 🔨 | Les forces d'un modèle de Bradley-Terry par maximum de vraisemblance (l'algorithme de Zermelo), centrées, et le refus d'un tournoi où elles n'existent pas · `bradley_terry_fit` | ★★ | 35 | §7 | C, E | pytest | — |
| MB8.17 | 🔮 | Prédire l'ordre des écarts-types de l'estimateur score d'une même dérivée, sans baseline, avec la moyenne des autres tirages et avec la baseline optimale, puis les mesurer | ★ | 20 | §3 | C, E | wbm | MB8.13 |
| MB8.18 | 🔬 | Un événement rare, P(Z > 4) pour Z normale centrée réduite : Monte-Carlo naïf contre l'échantillonnage d'importance sous N(4, 1), la taille effective, puis des poids tronqués à c : le biais et la variance selon c | ★★ | 30 | §6 | C | wbm | MB8.15 |
| MB8.19 | 🐛 | Chasse à l'erreur : le score d'une loi exponentielle écrit pour la moyenne au lieu du taux, des poids d'importance inversés (q/p), une baseline qui contient le tirage lui-même, des forces de deux tournois sans joueur commun comparées sur une même échelle | ★ | 25 | §1 §3 §6 §7 | C, E | wbm | — |
| MB8.20 | 🛠️ | Un test de propriété pour le gradient exact : sur des MDP tirés au hasard, comparé à des différences finies centrées, et de somme nulle sur les actions de chaque état | ★ | 25 | §4 | C | manuel | MB8.14 |
| MB8.21 | 🏆 | Défi : estimer, avec un budget de tirages, la dérivée d'une probabilité de dépassement par rapport au paramètre d'une loi, assez précisément neuf fois sur dix (score, baseline, variable de contrôle) | ★★★ | 40 | §2 §3 | C | wbm | MB8.13 |

*Notes* : Frontières : ∂ B8.7 (le gradient de politique en une étape : la loi d'un épisode μ(s₀)Π π_θ(a_t | s_t)P(s_{t+1} | s_t, a_t), l'astuce de la log-dérivée pour une loi discrète et « où as-tu supposé p > 0 », l'environnement qui disparaît du log d'un produit, le score d'espérance nulle vérifié sur une softmax à deux actions (z₀, z₁), la causalité et la forme γᵗG_t, la baseline b(s) sans biais et pourquoi pas b(s, a), la variance sur un bandit à deux actions de logits (0, z) en z = 0, récompenses 2 et 4, minimale en b = 3), ✏️ B8.3 (le gradient du log-softmax à trois actions, un pas, l'entropie), ✏️ B8.4 (GAE à la main sur un rollout avec troncature), ✏️ B8.5 (l'objectif clippé de PPO, ses quatre cas, la fraction clippée), ✏️ B8.6 (la loss de Bradley-Terry d'une paire, sa dérivée, le choix inverse, +10 ; la loss DPO, la récompense implicite, la marge, β), 📦 B8.17 (la variance du gradient avec et sans baseline mesurée sur des politiques, « la baseline qui minimise la variance est une moyenne pondérée par ‖∇ln π‖² »), 🔨 B8.18, B8.19 et B8.25 (`compute_gae`, `explained_variance`, `clipped_surrogate`, `bradley_terry_loss`, `dpo_loss`), 📄 B8.11 (l'article de PPO), les quiz B8.Q6 (le score de face d'une pièce à θ = 0,3, les baselines qui biaisent), B8.Q7 (δ, les poids (γλ)ˡ de GAE, la troncature) et B8.Q11 (l'avantage GRPO d'un groupe (1 ; 0 ; 0 ; 0)), 💼 B8.E2 (PPO et le clip) et B8.E4 (PPO ou DPO) ; B8.1 (cible DQN puis Double DQN) et B8.Q4 (la surestimation) restent des frontières de M26, dont le §8 a le biais du maximum et l'estimateur double : MB8 n'y revient pas. MB8 enseigne les outils dans d'autres cadres : la fonction score en statistique (lois de Poisson, exponentielle, binomiale, normale) et l'estimateur score de la dérivée d'une espérance, comparé à la dérivée par le chemin de M25b ; la baseline optimale démontrée en général comme une variable de contrôle (∂ MB8.9, pour un paramètre réel et une loi quelconque, jamais sur un bandit ni une politique) ; le gradient de la valeur d'une politique obtenu en dérivant le système de Bellman de M26 (∂ MB8.10), une autre démonstration, sans trajectoire, sans log d'un produit et sans causalité ; le λ-retour comme moyenne des retours à k pas, démontré par le télescopage de M26 dans la fiche et chiffré en espérance sur une chaîne (✏️ MB8.4), sans rollout ; l'échantillonnage d'importance d'un sondage (✏️ MB8.5) et d'un événement rare (🔬 MB8.18), avec des poids tronqués min(w, c) de statisticien, jamais clip(ρ, 1 − ε, 1 + ε) ni un min de deux objectifs ; Bradley-Terry sur un tournoi (maximum de vraisemblance, identifiabilité, Elo), sans récompense ni paire « choisie, rejetée » ; le principe de Gibbs sur des menus. Cadres : des clients à un guichet, la durée d'un appel, une attente au téléphone, des graines en godet, un camion de crêpes, l'état d'une route, un panel de sondage, un tournoi de babyfoot, un club d'échecs, une cantine, un événement rare ; jamais un agent, un épisode de jeu, CartPole ni Atari, un bandit à deux bras, une pièce « pile ou face » de paramètre θ avec un gain 1 pour pile, un modèle de récompense, un modèle de langue, un token, une réponse « choisie » ou « rejetée », un prompt, ni PPO, DPO ou GRPO chiffrés (la fiche les nomme dans « Et maintenant »). Ce que fait chaque exercice délicat. ∂ MB8.8 démontre E[s_θ] = 0 et Var(s_θ) = −E[∂²_θ ln p_θ] pour une famille à densité dont le support ne dépend pas de θ, l'échange de la dérivée et de l'intégrale admis (sa justification par domination est celle de M25b §7), les applique aux lois de Poisson et exponentielle, puis montre ce qui tombe pour la loi uniforme sur [0, θ] (score −1/θ d'espérance non nulle, terme de bord f(θ)/θ) ; il ne traite pas une loi discrète en demandant où l'on suppose p > 0 (∂ B8.7.1) ni une softmax à deux actions (∂ B8.7.3). Les quiz : MB8.Q1 ne chiffre ni le score d'une issue d'une loi de Bernoulli ni son espérance sur les deux issues (B8.Q6 a–b ; la fiche peut définir le score sur une Bernoulli, sans exercice) ; MB8.Q2 ne reprend pas les options de B8.Q6 c–e (moyenne des épisodes précédents, critique, retour du même pas, b = 1 000) : ses baselines sont des nombres ou des moyennes de tirages ; MB8.Q3 ne demande ni le poids (γλ)ˡ d'une erreur TD, ni ce que devient l'estimation pour λ = 0 ou λ = 1, ni quel λ donne la plus forte variance (B8.Q7 b–e) : il porte sur la loi d'occupation, l'avantage d'espérance nulle et les poids (1 − λ)λ^{k−1} des retours à k pas, de somme 1 ; MB8.Q4 et MB8.Q5 n'ont ni ratio de PPO ni loss de paire. ✏️ MB8.1 prend une loi exponentielle de taux θ (score 1/θ − x) et un seuil c : d/dθ P(X > c) par la formule fermée, l'espérance de l'estimateur 1{X > c}(1/θ − X), la dérivée nulle par le chemin X = ξ/θ, et la variance à un tirage en forme fermée ; jamais la gaussienne et le seuil de M25b §7, ni l'ampoule de M25b (moyenne 2 ans, remplacement à 3 ans, θc = 1,5, e^{−1,5}). ✏️ MB8.2 prend une loi à trois issues, B(2, θ) avec θ ≠ 0,3 et θ ≠ ½, et un prix f qui n'est pas affine en x : b* = E[f s²]/E[s²] y diffère de E[f] et ne rend pas la variance nulle ; jamais une loi à deux issues où la baseline optimale annule la variance (∂ B8.7.6). ∂ MB8.9 démontre, pour un θ réel, que Var((f − b)s) est minimale en b*, puis les baselines de groupe : sur n tirages i.i.d., (1/n)Σ(f_i − f̄_{−i})s_i est sans biais, et (1/n)Σ(f_i − f̄)s_i en vaut exactement (n − 1)/n fois ; la fiche ajoute que diviser par l'écart-type du groupe garde le signe de chaque terme, sans exercice chiffré (B8.Q11 c). ✏️ MB8.3 : deux emplacements, une politique softmax dans l'un (deux actions, rester ou partir), une politique fixée dans l'autre, γ = 0,7 : P_π, r_π, V (un système 2 × 2), la colonne utile de (I − γP_π)⁻¹, Q et A des deux actions de l'état qui choisit, puis ∂V/∂z par la formule ; ses logits ne sont jamais (0, z) en z = 0, et les deux valeurs d'action servent à la formule, jamais à désigner la meilleure ni à supposer une politique optimale (∂ 26.8.2). ∂ MB8.10 dérive V = r_π + γP_πV et réécrit le résultat avec ν_{s₀}, Q^π puis A^π (Σ_a π(a | s)A^π(s, a) = 0) ; la fiche énonce que ν pèse un état visité au pas t par (1 − γ)γᵗ, et que l'estimateur de workbookIA B8 omet ce poids, sans exercice dessus (∂ B8.7.4). ✏️ MB8.4 calcule des espérances sur une chaîne connue : le biais γᵏ(Pᵏe)(s) des retours à 1 et 2 pas pour une erreur e sur les valeurs, les poids (1 − λ)λ^{k−1}, et le biais du λ-retour quand l'erreur vaut c partout (une série géométrique) ; aucun rollout, aucune suite de récompenses observées, aucun drapeau terminated ou truncated, aucune récurrence Â_t = δ_t + γλÂ_{t+1} déroulée sur une suite (c'est `compute_gae`). ✏️ MB8.5 : un panel en ligne (la loi q des classes d'âge) contre le recensement (la loi p), poids p/q, E_q[w] = 1, estimation repondérée, sa variance à un tirage, taille effective de Kish d'un petit échantillon, poids tronqués à c et leur biais, puis KL(q ‖ p), k₁ = −ln w et k₃ = (w − 1) − ln w classe par classe et leurs espérances ; jamais un ratio π_θ/π_old, un avantage, un ε de clip, ni les lois (0,5 ; 0,5) et (0,6 ; 0,4). ✏️ MB8.6 : un tournoi de babyfoot ; deux clubs (la différence de forces en forme fermée), puis trois clubs avec des forces proposées dont on vérifie les équations du maximum de vraisemblance, une probabilité de victoire, une mise à jour Elo (échelle 400/ln 10, coefficient k), et pourquoi un club invaincu n'a pas de force finie ; jamais la loss d'une paire et sa dérivée en chaîne (✏️ B8.6 a–e), ni un écart de 1,5, 1,2 ou 3,0, ni « ajouter 10 aux deux » comme question (l'identifiabilité passe par Σβ = 0). ✏️ MB8.7 : trois plats, une loi actuelle π_ref, des satisfactions r, deux valeurs de β ; la loi π* ∝ π_ref e^{r/β}, sa valeur β ln Z, comparée à π_ref (KL nulle) et au meilleur plat seul ; la fiche démontre le principe en cinq lignes par KL ≥ 0 (une extension de la loi de Boltzmann de M17, et du sujet B de CP6.8, au choix, dont MB8 ne dépend pas), et dit en une ligne que r est déterminée par π* et π_ref à une constante près ; aucun exercice ne calcule β ln(π*/π_ref) pour deux issues ni leur différence (la récompense implicite et la marge de ✏️ B8.6 f–j). 🔗 MB8.11 : la loss de substitution −(1/n)Σ(f(x_i) − b) ln p_θ(x_i) sur le taux d'une loi de Poisson, sa dérivée, les f(x_i) et b tenus fixes (ce que les bibliothèques appellent stop-gradient), puis des f standardisés dans le batch ; jamais ln π(a | s), G_t, un épisode ni un retour. Le 🔮 MB8.17, le 🔬 MB8.18 et le 🏆 MB8.21 portent sur des lois (une binomiale, une normale, une loi de Poisson ou exponentielle), jamais sur des politiques ni des épisodes. Rappels sans les refaire : M26 §4 et §5 (MDP, P_π, r_π, Q^π, le système de Bellman, la loi d'occupation actualisée ν_s = (1 − γ)e_s(I − γP)⁻¹ et V(s) = ν_s r/(1 − γ)) et §8 (l'erreur TD, son espérance, le télescopage, ∂ M26.13) : 🔁 MB8.R2 ; M25b §7 (la dérivée par le chemin, la domination, l'indicatrice où elle échoue et la méthode du score nommée pour MB8) : 🔁 MB8.R3 ; M17 §7 (Boltzmann, diag(p) − ppᵀ) : 🔁 MB8.R1, qui ne calcule ni le gradient de ln softmax(z)_a en des logits donnés ni un pas sur ces logits (✏️ B8.3) ; M13a (logistique, log-loss), M06 (KL ≥ 0), M05a (une fonction convexe au-dessus de sa tangente), M20 §5 (Horvitz-Thompson), M14 §4 (Hedge), M28 §5 (la température d'une loi) et M02c sont cités dans la fiche. GAE n'est pas dans M26 (son télescopage est le cas λ = 1) : MB8 ne le présente pas comme un rappel, et ne le nomme que dans « Et maintenant ». Conventions : s_θ(x) = ∂_θ ln p_θ(x), le score en θ, distinct du score en x de MB5 (∇ₓ ln p) : un encadré 📐 le dit ; la loi exponentielle par son taux θ (densité θe^{−θx}, moyenne 1/θ ; M25b la prenait par sa moyenne), un encadré ⚠️ le dit ; le MDP comme en M26.14 : P[a, s, t], r[a, s] = r(s, a) = Σ_t P[a, s, t] R[a, s, t] (M26.14 range les récompenses R[a, s, s2] de chaque transition), et les logits z[s, a] rangés comme pi[s, a] ; les lois en lignes et les valeurs en colonnes (M26) ; en échantillonnage d'importance, les tirages viennent de q (la loi de proposition) et w = p/q ; la KL estimée est KL(q ‖ p), avec des tirages de q ; Elo en base 10 et à l'échelle 400 (β = R ln 10/400). Les γ des exercices sont pris parmi 0,6 et 0,7, et λ parmi 0,6 et 0,7 : jamais γ = 0,5, 0,8, 0,9, 0,95, 0,99, ni 0,75 et 0,85 (les exemples de `markov` et la boutique de M26), jamais λ = 0,5, 0,8 ni 0,95, jamais γλ = 0,45, 0,855 ni 0,9405. `policy_gradient` (fonctions rangées dans l'ordre des sections) : NumPy et `math` permis, de `np.linalg` seulement `solve` et `matrix_rank` (dans `policy_gradient_exact`) ; ni SciPy ni scikit-learn ; un import relatif de `bellman_linear_solve` (M26) est permis. Oracles des tests : des sommes exactes et `fractions` pour `score_function_gradient` (et l'absence de biais vérifiée sur des lois discrètes par énumération) ; des différences finies centrées sur des valeurs calculées par `np.linalg.solve` pour `policy_gradient_exact` ; NumPy, `scipy.special.logsumexp` et l'invariance par un facteur commun pour `importance_weights` ; `scipy.optimize.minimize` sur la log-vraisemblance centrée et `sklearn.linear_model.LogisticRegression(fit_intercept=False, penalty=None)` sur les différences d'indicatrices pour `bradley_terry_fit` ; jamais une autre fonction de l'apprenant. Contrats distincts de `mylearn` B8 : `score_function_gradient` rend une moyenne de (f − b)s et son erreur type à partir de valeurs et de scores déjà calculés (ni épisode, ni log-probabilité d'action, ni retour) ; `policy_gradient_exact` est exacte, tabulaire, sans échantillon ; `importance_weights` prend deux log-densités (`log_target`, `log_proposal` : ni `ratio` ni `log_pi_old`) et rend des poids et une taille effective, sans avantage, sans clip(ρ, 1 − ε, 1 + ε) ni loss (`clipped_surrogate`) ; `bradley_terry_fit` rend des forces centrées ajustées sur une matrice de victoires, ni une loss ni un gradient (`bradley_terry_loss`). Aucune fonction de λ-retour (`lambda_return` serait `compute_gae` à une addition près), de KL estimée, de loi de Gibbs (`temper` de M28 et `hedge_weights` de M14 en sont des cas), ni de variance expliquée. Les exercices ne reprennent pas les exemples du stub : f = (3, 0, 2, 5) et s = (0,5 ; −1 ; 0 ; 1,5) (2,25 ; 1,7854 ; 2,0 ; 2,1667) ; le MDP où l'action 0 mène à l'état 0 et l'action 1 à l'état 1, r = [[1, 0], [0, 2]], logits nuls, γ = 0,6 (V = (1,625 ; 2,125), 0,30625, 0,43125) ; les log-densités (−1 ; −0,5 ; −0,5 ; −2) et (−1,5 ; −1 ; −1 ; −1) (3,4063) et la troncature à 2 (1,8) ; les tournois [[0, 4], [1, 0]] (ln 4 ; ±0,6931) et [[0, 4, 2], [1, 0, 3], [1, 2, 0]] (0,7464 ; −0,2949 ; −0,4516). Évités (règle de partage), de workbookIA B8 : CartPole et ses nombres (4,8 ; 0,4189 ; 2,4 et 12° ; 500 et 475 ; 22,3, 19, 8 et 119 ; 19,5 à 24,8 ; 11,8 et 1,2 ; la règle θ + 0,5θ̇ > 0 ; 42 et 202 ; 10⁴ et 10¹⁰⁰ cases), Atari, AlphaGo Zero, OpenAI Five, InstructGPT, DeepSeekMath, CleanRL, MuJoCo ; la pièce p_θ(pile) = θ avec le gain 1 pour pile (dérivée 1), θ = 0,3 et le score −1,43 ; pierre-feuille-ciseaux et pair ou impair ; le bandit gaussien 10 et 11 (σ = 1 ; 0,25 ; 5,27 ; 0,50 ; b = 10,5) ; le bandit déterministe 2 et 4 aux logits (0, z) en z = 0 (0,5 ; b = 3 ; 2,25 ; 1,5 ; variante 0,25) ; les logits (0,3 ; −0,2) (0,6225 ; 0,3775), (0,5 ; 1,5 ; −0,5) (0,2447 ; 0,6652 ; 0,0900 ; Â = −2 ; pas 0,1 ; −0,682 ; 0,0687 ; 0,1170) et (ln 2 ; ln 6 ; 0) (0,67) ; les entropies ln 2, 0,325, 0,056, 0,832, ln 3 et c = 0,01 ; les ratios (0,7 ; 1,1 ; 1,35) avec (−1 ; 2 ; −1) (−0,0167 ; −0,6667 ; 0,3333), (1,4 ; 0,6 ; 0,75 ; 1,35) avec (2,0 ; 1,5 ; −1,2 ; −0,8) (2,4 ; 0,9 ; −0,96 ; −1,08 ; −0,315 ; −0,375), (0,5 ; 1,0 ; 1,5) avec 1 (−0,9), ε = 0,1, 0,2, 0,3 et 0,4, le ratio 1,15, ρ = 1,5, e^{0,3} = 1,35 et les log-probabilités −0,9 et −1,2 ; la KL approchée de (0,5 ; 0,5) contre (0,6 ; 0,4) (0,0204 ; −0,182 ; 0,018) et les KL 0,027, 0,003, 0,02, 0,012, 0,004 et 0,0008 ; Bradley-Terry Δ = 1,5 (0,818 ; 0,201 ; −0,182), 2,3 et 1,1 (0,769 ; 0,263 ; −0,231 ; 1,463), d = 3,0 (0,953 ; 0,0486 ; −0,0474), (0, 0) → ln 2, (−1 000 ; 1 000) → 2 000, +10 ; DPO −20, −23, −21, −22 (0,2 ; 0,598 ; 1,0 ; 0,313), −35,2, −38,9, −36,0, −37,5 (0,08 ; 0,22 ; 0,589 ; 0,287 ; −0,0445), [−10 ; −12], [−11 ; −9], [−10,5 ; −11], [−10,5 ; −10] (0,1 ; −0,2 ; 0,7213), β = 0,02, 0,04, 0,1 et 0,5 ; le groupe (1 ; 0 ; 0 ; 0) (1,73 et 1,5), G = 64, 8 réponses ; GAE : r = 1, V = (2,0 ; 1,5 ; 0,8) (δ = (0,35 ; 0,22 ; 0,2), (0,4895 ; 0,31 ; 0,2), (2,71 ; 1,9 ; 1), 0,7 et 0,83), V = (4,0 ; 3,8 ; 2,0 ; 2,4) et (3,8 ; 3,6 ; 2,4 ; 2,6) (0,42 ; 0,44 ; 1,16 ; 0,94 ; 1,9637 ; 0,7962), (1, 1, 1) avec γ = 0,5 (1,75 ; 1,5 ; 1), V = 0,5 et (0,5 ; 0,5 ; 2,0) (1,3775 ; 0,95 ; 2,3), r = 1, γ = 0,9, V = 3,0 et 2,5 (δ = 0,25) ; la variance expliquée de (1 ; 2 ; 3 ; 4) contre (1,5 ; 1,5 ; 3,5 ; 3,5) (0,8), (6 ; 7 ; 8 ; 9), [1, 2, 3] contre [1, 2, 4] (0,8571) ; les cibles DQN (2,0 ; 3,5 ; 1,2) (4,15) et (4,1 ; 3,0 ; 0,5) (2,8), [[0,4 ; 3,9] ; [1,1 ; 2,0]], les tableaux de ✏️ B8.1 (γ = 0,99 ; 14,56 ; 42,18 ; 12,88 ; 40,80 ; 13,474) ; Huber x = (0,6 ; −2,4 ; 3,2) et δ = 1,5, x = 3 et le seuil 2, x = 0,5 ; le biais du maximum de 2, 4 et 10 gaussiennes (0,56 ; 1,03 ; 1,54) et trois estimations ±1 (0,75) ; (1 − 0,005)²⁰⁰ ≈ 0,37, la mémoire de 10 000 et les mini-batches de 64 ; les comptes et réglages (10 934, 67 586, 4 610, 4 545, 9 155, 976, 500 000, 2,5 × 10⁻⁴, c₁ = 0,5) et les Fermi de 🧮 B8.8 ; Christiano (900 comparaisons), 40 annotateurs, 4 à 9 réponses et 36 paires, 73 % ; de workbookIA B7 (MB8 ne compare pas de graines), les graines 71,2 ; 70,5 ; 72,1 ; 69,8 ; 71,6 ; 70,9 et 64,2 ; 65,0 ; 63,6 ; 64,8 ; 64,4. Évités aussi (reprises de ce dépôt) : l'ampoule de M25b §7 (moyenne 2 ans, remplacement à 3 ans ; 1,554 ; 0,442 ; e^{−1,5}), le stock gaussien de ✏️ M25b.12 et ∂_σ E[e^X] de ∂ M25b.11 ; la boutique de M26 (P_att, r = (−5 ; 7 ; 9), γ = 0,85, V ≈ (23,46 ; 28,13 ; 33,48), ν₂ ≈ (0,245 ; 0,274 ; 0,481)), la salle de sport de 🔗 M26.14 (P₀, P₁, 30 € et 21 €), la machine de ✏️ M26.6 ; la loi (0,5 ; 0,3 ; 0,2) et les énergies 0, 0,5 et 2 de M17 §7 ; les énergies (0, ln 3, 2 ln 3) à T = 1 de CP6.8 B ; les trois experts et η = 0,5 de Hedge (M14 §4) ; les avis de l'ornithologue et du garagiste (M28 §5) ; la forêt (120, 40, 300, 90, 60) de Horvitz-Thompson (M20 §5) ; ajoutés à la génération (session 76, relecture de partage) : la loi (0,4 ; 0,3 ; 0,2 ; 0,1) et KL(u ‖ π_ref) de CP1.11 du checkpoint I de workbookIA ; la gaussienne et le seuil de M25b §7 pour tout exercice (et pas seulement ✏️ MB8.1) ; le vecteur (0,2 ; 0,7 ; 0,1) d'un quiz de MB3 ; l'appel téléphonique exponentiel de taux 0,2 de ✏️ M02a ; la loi B(5 ; 0,8) de ✏️ M02b.1 ; le ratio ρ = 1,5 comme poids ; γλ = 0,42 (le δ₀ de ✏️ B8.4) ; et les erreurs fréquentes et « À retenir » des corrigés de B8, frontières et voisins, ne reviennent nulle part, même dans un autre cadre : « oublier de justifier p_θ > 0 » (∂ B8.7.1), « une mauvaise baseline augmente la variance » (∂ B8.7), « λ seul au lieu de γλ » (✏️ B8.4), « une baseline ne réduit la variance que si elle est proche des retours » (B8.Q6), l'argument de b(s) sans biais (flashcard 12 de B8), « la normalisation change aussi l'échelle » (🔮 B8.16), « une baseline calculée sur l'épisode lui-même » (📦 B8.17). Glossaire : « fonction score | score function | ∂_θ ln p_θ(x) | MB8 », et l'entrée « méthode du score » (M25b) renvoie à MB8. Pas de MML (le livre n'a ni fonction score, ni échantillonnage d'importance, ni apprentissage par renforcement), donc pas de 📖. Références libres, citées par sections et à vérifier en génération (annexes/ressources.md) : R. S. Sutton et A. G. Barto, Reinforcement Learning: An Introduction (2ᵉ éd., 2018), §12.1 (le λ-retour), §13.2 (le théorème du gradient de politique) et §13.4 (la baseline) ; A. B. Owen, Monte Carlo theory, methods and examples (en ligne), les chapitres sur les variables de contrôle et l'échantillonnage d'importance ; D. R. Hunter, « MM algorithms for generalized Bradley-Terry models », Annals of Statistics (2004), pour l'algorithme de Zermelo. Ni la triade mortelle ni la moyenne interquartile (facultatives au plan) : pas de place ; la loi de Little (workbookIA B7) non plus. COMPOSITION : 7 ✏️ et 3 ∂ (le bas de la fourchette : chaque section a son ✏️, les démonstrations courtes, Gibbs et le λ-retour, sont dans la fiche) ; ni 📦 (les quatre 🔨 et leurs oracles en tiennent lieu) ni 🎨 (le 🔮 et le 🔬 tracent leurs mesures) ; un seul 🔗 et un 💼. Parcours essentiel : tout sauf ∂ MB8.9 (la baseline optimale et les baselines de groupe : la fiche énonce le résultat), le 🔬, le 🛠️ et le 🏆. **Durée** : 14,8 h (parcours essentiel 12,7 h), recalée à la génération (session 76) par l'auteur des exercices, la re-résolution à l'aveugle et l'apprenant simulé ; à la session 69 : 13,3 h au lieu des 12 h visées (10 h au plan) : huit notions, dont quatre lacunes lourdes (la fonction score et Fisher, les variables de contrôle, l'échantillonnage d'importance, le principe de Gibbs) et la dérivation matricielle promise par M26, avec des durées d'apprenant qui rédige (les recalages de M25a à M28 : +20 à +40 %) ; déjà allégée (✏️ de Fisher fondu dans ∂ MB8.8, Gibbs et le λ-retour démontrés dans la fiche, ni 📦 ni 🎨, un seul 💼).

<a id="ps"></a>
## PS · Projet de synthèse

**Partie** fin · **prépare** — · **dossier** `projets/projet_synthese/` · **MML** — · **sessions de génération** 1

« Les maths d'un algorithme, de A à Z » : tu choisis un algorithme de workbookIA (régression logistique, rétropropagation d'un MLP, VAE, attention…) et tu écris un notebook-article qui dérive tout, l'implémente avec `mymath` et le vérifie contre une bibliothèque. Grille sur 20, pas de solution de référence, un exemple rédigé sur un autre algorithme. En même temps que le projet final de workbookIA.

**Temps** : 27,3 h en parcours complet, 27,3 h en parcours essentiel (lecture 90 min, 0 flashcards).

**Objectifs**

- Choisir un algorithme de workbookIA et en dériver toutes les formules, de l'objectif jusqu'à ce que le code calcule, chaque étape justifiée par un résultat d'un chapitre de maths et chaque forme vérifiée.
- Démontrer deux propriétés de l'algorithme avec leurs hypothèses, et montrer ce qui se passe quand l'une d'elles tombe.
- L'implémenter avec ta librairie `mymath`, et le vérifier contre une bibliothèque indépendante par des tests qui attrapent de vraies erreurs.
- Rédiger un notebook-article qu'un relecteur peut suivre et vérifier, et le présenter en cinq minutes, comme en entretien.

**Sections de la fiche**

- §1 Choisir et cadrer
- §2 Dériver
- §3 Implémenter et vérifier
- §4 Rédiger et présenter

**Notions enseignées** : rédiger une dérivation complète · vérifier une implémentation contre une bibliothèque

**Prérequis** : tout le parcours, en particulier les chapitres de l'algorithme choisi (MB8) · rédiger une démonstration courte (hypothèses, étapes justifiées, conclusion) (R4) · différences finies centrées et choix du pas (M05a) · gradient de la forme de la variable, lu dans la différentielle (M18)

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 7.7 ∂ La frontière du centroïde le plus proche est une droite · 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 9.6 ∂ Lasso en dimension 1 : le seuillage doux et les zéros exacts · 12.8 ∂ Variance d'une projection et axe de variance maximale · 13.8 ∂ Gradient de la log-loss de la régression logistique · 17.4 ∂ Dériver la sigmoïde, tanh et softplus · 17.7 ∂ La Jacobienne de la softmax · 18.6 ∂ La règle de la chaîne derrière les deltas · 18.7 ∂ Forme matricielle : XᵀΔ, ΔWᵀ et somme des lignes · 18.8 ∂ Softmax et cross-entropy : le gradient vaut p − y · 19.7 ∂ Sur une parabole, η doit rester sous 2/a · 19.8 ∂ Moyenne mobile exponentielle : mémoire effective et biais initial · 20.8 ∂ Le gradient de la batchnorm · 21.7 ∂ Rétropropager dans une convolution 1D : la somme sur les positions · 22.6 ∂ Pourquoi le gradient s'évanouit : un produit de dérivées de tanh · 22.7 ∂ Le chemin additif de la cellule LSTM · 25.5 ∂ Dériver à travers un tirage : l'astuce de reparamétrisation · 25.7 ∂ La divergence KL entre N(μ, σ²) et N(0, 1) · 26.7 ∂ Somme géométrique et horizon effectif de γ · 26.8 ∂ Équation de Bellman : le point fixe que vise le Q-learning · B2.7 ∂ Skip-gram avec échantillonnage négatif : gradients par rapport au mot et au contexte · B3.6 ∂ Pourquoi √d_k : variance du produit scalaire de deux vecteurs aléatoires · B3.7 ∂ RoPE : la rotation rend q_m · k_n fonction de m − n seulement · B5.6 ∂ Forme fermée : deux pas de bruit gaussien n'en font qu'un, d'où q(x_t | x_0) · B5.7 ∂ Moyenne et variance du posterior q(x_{t−1} | x_t, x_0) en dimension 1 · B8.7 ∂ Le gradient de politique en une étape : l'astuce de la log-dérivée, puis la baseline sans biais

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| PS.1 | 🗣️ | Cadrer : l'algorithme choisi, ce qu'il calcule, ses entrées et sorties, les notions de maths et leurs chapitres, l'oracle de la vérification et le plan de l'article | ★★ | 75 | §1 | C, E | manuel | — |
| PS.2 | ✏️ | Poser le problème : données, paramètres et leurs formes, objectif, hypothèses, tableau des notations et conventions | ★★ | 105 | §2 | C, E | manuel | PS.1 |
| PS.3 | ∂ | La dérivation complète, de l'objectif aux formules que le code calcule : chaque étape justifiée par un résultat cité, chaque forme vérifiée | ★★★★ | 270 | §2 | C, E | manuel | PS.2 |
| PS.4 | ∂ | Deux propriétés démontrées avec leurs hypothèses (convexité, unicité, invariance, espérance, borne, coût), et un cas où une hypothèse tombe | ★★★ | 210 | §2 | C, E | manuel | PS.3 |
| PS.5 | ✏️ | Un exemple à la main en dimension 2 ou 3 (en fractions quand c'est possible), retrouvé par le code | ★★★ | 120 | §2 §3 | C, E | manuel | PS.3 |
| PS.6 | 🛠️ | L'implémentation : un module documenté (contrat, formes, erreurs) qui appelle au moins trois fonctions de ta librairie `mymath`, sans bibliothèque de ML | ★★★★ | 210 | §3 | C, E | manuel | PS.3 |
| PS.7 | 📦 | La vérification : des tests contre une bibliothèque indépendante sur des cas tirés au hasard, les dérivées contre des différences finies, une propriété, et une erreur introduite exprès que les tests attrapent | ★★★★ | 210 | §3 | C, E | pytest | PS.6 |
| PS.8 | 🔬 | Une expérience numérique qui illustre une propriété démontrée (convergence, conditionnement, stabilité, effet d'un hyperparamètre) : une figure légendée et sa conclusion | ★★★ | 150 | §3 | C, E | manuel | PS.6 |
| PS.9 | 🛠️ | Rédiger l'article : introduction, plan, conclusion et limites, références par sections, LaTeX propre, notebook exécuté de bout en bout en moins de 5 minutes | ★★★ | 140 | §4 | C, E | manuel | PS.8 |
| PS.E1 | 💼 | Présenter l'algorithme en cinq minutes, puis répondre à cinq questions d'entretien sur ses maths | ★★★ | 60 | §4 | C, E | manuel | PS.9 |

*Notes* : Fichiers : `README.md` (le cahier des charges : contexte, liste des algorithmes, règles, jalons, les dix étapes avec livrable, critères et erreurs à éviter, la grille résumée, la correction), `GRILLE.md` (la grille sur 20, critère par critère, chacun observable, avec « Comment le vérifier » et une colonne de preuve), `04_indices.md` (trois niveaux par étape), `depart/` (le kit que `start_chapter.py PS` copie dans `mon_travail/projet_synthese/` : son mode d'emploi `README.md`, le modèle du notebook-article `synthese.ipynb`, le module `algo.py`, ses tests `test_algo.py` et leur `conftest.py` (option `--impl`, et `--mutant` qui remplace une fonction du module par sa copie fautive de `mutants.py`, pour la mutation de PS.7), le modèle du cadrage, ta copie de la grille pour l'auto-évaluation) et `exemple/` (l'exemple rédigé et vérifié : jamais copié par `start_chapter.py`). Pas de solution de référence : c'est ton projet. Points : PS.1 1, PS.2 1,5, PS.3 4, PS.4 2,5, PS.5 1,5, PS.6 3, PS.7 3, PS.8 1,5, PS.9 1, PS.E1 1 ; pénalités pour un passage recopié sans être cité et pour un notebook qui ne s'exécute pas de bout en bout. Correction : auto-évaluation sur la copie de la grille, preuve à l'appui, puis correction par Claude sur demande, en lecture seule de `mon_travail/projet_synthese/`. **L'exemple** porte sur un algorithme hors de la liste et hors de workbookIA : la régression de Poisson ajustée par la méthode de Newton (moindres carrés repondérés), sur des données synthétiques, vérifiée contre scikit-learn (`PoissonRegressor`) et SciPy ; il appelle des fonctions publiées de `mymath` (version de référence) et ne reprend aucun exercice ni aucun nombre de ce dépôt ou de workbookIA. Il sert d'étalon pour chaque critère de la grille (sa propre grille est remplie, preuve par preuve) ; l'apprenant l'ouvre une fois son cadrage ébauché. **Frontières** : les ∂ de workbookIA qui dérivent les algorithmes de la liste (champ `frontieres`) ne sont résolus ni dans le cahier des charges, ni dans la grille, ni dans les indices, ni dans l'exemple : c'est l'apprenant qui les redérive dans son projet, avec ses propres mots ; les indices restent des conseils de méthode (écrire la loss d'un exemple avant la somme, vérifier les formes ligne à ligne, lire le gradient dans la différentielle) et ne donnent aucun résultat propre à un algorithme de la liste. **Oracles** : NumPy, SciPy, SymPy, scikit-learn, et PyTorch dans le projet de l'apprenant seulement (installé pour workbookIA et sur Colab ; ce dépôt ne l'importe jamais) ; jamais une autre fonction de l'apprenant ni une formule écrite pour l'occasion. Durée : 27,3 h, lecture du cahier des charges, de la grille et de l'exemple survolé comprise (90 min), recalée à la génération par l'apprenant simulé (25 h au plan ; 2 à 4 h de plus si des modules de `mymath` manquent), en même temps que le projet final de workbookIA (quatre semaines). Le projet appartient aux deux parcours (BIBLE §12).

