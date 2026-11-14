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
| [M25b](#m25b) | Variables latentes et ELBO | 25 | §8.4, §8.5, §10.7, ch. 11 | 17,1 h | ✅ exercices | 2 |
| [M26](#m26) | Chaînes de Markov et équation de Bellman | 26 | — | 14,6 h | ✅ exercices | 1 |
| [M27](#m27) | Jeux et distances entre lois | 27 | §7.2 | 14,4 h | ✅ exercices | 1 |
| [M28](#m28) | Matrice de Gram, montée sur l'entrée et lois tronquées | 28 | — | 9,8 h | ✅ exercices | 1 |
| [CP6](#cp6) | Examen blanc de la partie VI | — | — | 3,1 h | ✅ exercices | 1 |
| [MB2](#mb2) | Cooccurrences, PMI et embeddings | B2 | — | ≈ 8 h (estimé) | plan | 1 |
| [MB3](#mb3) | Rotations et attention | B3 | §3.9 | ≈ 10 h (estimé) | plan | 1 |
| [MB4](#mb4) | Rang faible et recherche d'information | B4 | (§4.6) | ≈ 6 h (estimé) | plan | 1 |
| [MB5](#mb5) | Les maths de la diffusion | B5 | (§6.5) | ≈ 14 h (estimé) | plan | 1 |
| [MB6](#mb6) | Shapley, intégrales de chemin et équité | B6 | — | ≈ 8 h (estimé) | plan | 1 |
| [MB8](#mb8) | Gradient de politique | B8 | — | ≈ 10 h (estimé) | plan | 1 |
| [PS](#ps) | Projet de synthèse | — | — | ≈ 25 h (estimé) | plan | 1 |

## Totaux par partie

| Partie | Chapitres | Exercices détaillés | Durée (complet) | Durée (essentiel) |
|---|---|---|---|---|
| 0 · Remise à niveau | 12 | 363 | 116,5 h | 93,3 h |
| I · Fondations | 9 | 319 | 107,6 h | 69,7 h |
| II · Concepts | 7 | 256 | 83,9 h | 54,0 h |
| III · ML classique | 8 | 321 | 107,5 h | 71,2 h |
| IV · Réseaux | 6 | 182 | 58,8 h | 41,9 h |
| V · Architectures | 3 | 94 | 33,5 h | 25,9 h |
| VI · Génératif et RL | 6 | 203 | 79,3 h | 61,4 h |
| VII · Bonus | 6 | — | ≈ 56 h (estimé) | à détailler |
| fin · Fin | 1 | — | ≈ 25 h (estimé) | à détailler |

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

**Temps** : 17,1 h en parcours complet, 14,0 h en parcours essentiel (lecture 165 min, 22 flashcards).

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

**Notions enseignées** : variable latente, espace latent, processus génératif ; loi jointe p(x, z) = p(z) p(x | z) · modèle graphique orienté : factorisation selon les parents, tirage ancestral ; indépendance conditionnelle, chaîne, fourche et collision (d-séparation en survol, MML §8.5) ; une cause observée en disculpe une autre · vraisemblance marginale p(x) = Σ_z p(z) p(x | z) (ou une intégrale) ; posterior p(z | x) par Bayes ; l'évidence comme constante de normalisation · mélange de lois : densité, tirage ancestral ; espérance et variance conditionnelles sachant une variable discrète, définies ici (E[X | Z = k], la variable aléatoire E[X | Z] ; pour un mélange, E[X | Z = k] = μ_k et V[X | Z = k] = Σ_k) ; lois de l'espérance totale et de la variance totale (MML Théorème 6.12, §6.5.3) ; moyenne et covariance d'un mélange Σ π_k (Σ_k + μ_k μ_kᵀ) − μμᵀ ; part de la variance entre les groupes · mélange de gaussiennes : log-vraisemblance (le logarithme d'une somme), responsabilités calculées en log par log-sum-exp (M04, M05a) · singularités : vraisemblance non bornée quand une composante s'effondre sur un point, régularisation Σ_k + reg·I (le pas M ne maximise plus : l'EM régularisé n'est plus monotone à coup sûr) ; numérotation arbitraire des composantes : K! maxima équivalents · algorithme EM pour un mélange de gaussiennes : pas E (responsabilités), pas M (π_k = N_k/n par un multiplicateur de Lagrange, moyennes et covariances pondérées : le maximum de vraisemblance de M25a, pondéré) ; monotonie, maxima locaux, initialisations ; une proportion de mélange et des composantes inconnues (suite de M13a) · k-means comme limite de l'EM : covariances communes γI, γ → 0, responsabilités dures · borne inférieure de l'évidence (ELBO), démontrée en général pour un latent discret ou continu : ln p(x) = E_q[ln p(x, z) − ln q(z)] + KL(q ‖ p(z | x)) ; ELBO ≤ ln p(x), égalité si et seulement si q est le posterior ; la même borne par Jensen ; la forme E_q[ln p(x | z)] − KL(q ‖ p(z)) (une reconstruction moins une KL au prior) ; l'entropie de q · l'EM comme montée par coordonnées de l'ELBO : le pas E la maximise en q (q = posterior), le pas M en θ (Q(θ | θ_t) de MML §11.4.5) ; d'où la monotonie · gradient de la log-vraisemblance marginale : ∇_θ ln p(x) = E_{p(z | x)}[∇_θ ln p(x, z)] ; il égale le gradient de l'ELBO quand q est le posterior · ACP probabiliste (MML §10.7) : z ~ N(0, I_k), x = Wz + μ + ε, ε ~ N(0, σ²I) ; loi marginale N(μ, WWᵀ + σ²I) ; posterior N(M⁻¹Wᵀ(x − μ), σ²M⁻¹) avec M = WᵀW + σ²I, par le modèle linéaire gaussien de M25a ; l'autre forme, Wᵀ(WWᵀ + σ²I)⁻¹(x − μ) et I − Wᵀ(WWᵀ + σ²I)⁻¹W (MML §10.7.3), égale par Wᵀ(WWᵀ + σ²I)⁻¹ = (WᵀW + σ²I)⁻¹Wᵀ ; sa moyenne est une règle affine de x, sa covariance n'en dépend pas · maximum de vraisemblance de l'ACP probabiliste (Tipping et Bishop, énoncé) : σ² = moyenne des valeurs propres écartées, W = U_k (D_k − σ²I)^{1/2} R, D_k = diag(λ₁, …, λ_k) ; la limite σ² → 0 retrouve l'ACP de M12d ; quand σ² est fixé (connu), une direction de valeur propre λ ≤ σ² est éteinte (colonne de W nulle) · non-identifiabilité par rotation : W et WR (R orthogonale) donnent la même loi ; seul le sous-espace engendré par W est déterminé · angles principaux entre deux sous-espaces : cos φ_i = valeurs singulières de Q_Aᵀ Q_B pour des bases orthonormées Q_A et Q_B (M12b, M12d), min(k_A, k_B) angles ; ils ne dépendent pas des bases ; deux sous-espaces de même dimension sont égaux si et seulement si tous leurs angles sont nuls (en général, tous nuls si et seulement si le plus petit est contenu dans l'autre) · inférence approchée : famille de lois q, KL(q ‖ p) (évite de mettre de la masse là où p est faible, choisit un mode) contre KL(p ‖ q) (couvre toute la masse ; pour une famille gaussienne, apparie les moments) ; maximiser l'ELBO, c'est minimiser KL(q ‖ p(z | x)) · inférence amortie : une règle x ↦ q(z | x) commune à toutes les observations ; écart d'amortissement : ELBO amortie ≤ meilleure ELBO par observation ≤ ln p(x) · dériver une espérance par rapport à un paramètre de la loi : le chemin X = μ + σε (ou μ + Lε, M25a), que workbookIA 25 appelle l'astuce de reparamétrisation (*reparameterization trick*) ; l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré, la convergence dominée admise), d/dθ E[f(g_θ(ε))] = E[f′(g_θ(ε)) ∂_θ g_θ(ε)] ; estimateur de Monte-Carlo sans biais à un tirage (M19) et sa variance ; une fonction dérivable presque partout, et une indicatrice 1{X > c} pour laquelle l'échange échoue (dérivée nulle presque partout, alors que d/dμ P(X > c) = N(c | μ, σ²), la densité en c) ; la méthode du score seulement nommée (MB8) · pondérer une KL : maximiser une vraisemblance de reconstruction sous un budget d'information, le lagrangien (M13b), β comme multiplicateur et pente de la meilleure valeur en fonction du budget ; avec un bruit gaussien de variance σ², changer σ² revient à changer β · posterior agrégé q(z) = E_x[q(z | x)], un mélange ; il égale le prior quand q(z | x) est le posterior exact et que x suit la loi marginale du modèle, p(x) = Σ_z p(z) p(x | z) · E_x KL(q(z | x) ‖ p(z)) = I(X ; Z) + KL(q(z) ‖ p(z)) ≥ I(X ; Z) (M06) ; une KL moyenne nulle veut dire un code indépendant de l'entrée (effondrement) · information mutuelle de deux variables continues, I(X ; Z) = h(Z) − h(Z | X) = KL(p(x, z) ‖ p(x)p(z)), entropie différentielle conditionnelle (suite de M06 et de M25a) ; celle d'une mesure gaussienne bruitée ½ ln(1 + s²/v), distorsion s² e^{−2I} ; le code s'éteint quand β est assez grand

**Prérequis** : intégration par parties (M02a) · espérance d'une variable continue, théorème de transfert, loi normale, fonction de répartition Φ, loi exponentielle (M02b) · formule de Bayes, probabilités totales, logarithme d'une somme (M04) · log-sum-exp stable (`logsumexp`) (M05a) · entropie, divergence KL discrète, information mutuelle, inégalité de Jensen discrète (M06) · distance euclidienne, k-means (M07) · base orthonormée d'un sous-espace, Gram-Schmidt, projection orthogonale (M12b) · théorème spectral, valeurs propres d'une covariance (M12c) · SVD, ACP, approximation de rang faible (M12d) · maximum de vraisemblance, log-vraisemblance, proportion d'un mélange à composantes connues (M13a) · multiplicateurs de Lagrange, KKT (M13b) · graphes orientés sans cycle, numérotation des nœuds où chaque parent précède ses enfants (M16) · gradient par rapport à une matrice : ∇ ln det X et ∇ tr(AX) (M18) · estimateur de Monte-Carlo sans biais d'un gradient, variance d'un estimateur (M19) · densité et log-densité de N(μ, Σ) (`mvn_logpdf`), modèle linéaire gaussien, loi conditionnelle, maximum de vraisemblance de μ et Σ, loi de μ + Lε, Jensen continu, KL continue et KL entre gaussiennes, entropie différentielle (M25a)

**mymath** : `latent.py` (signatures figées) : `gmm_e_step`, `gmm_m_step`, `gmm_log_likelihood`, `gmm_elbo`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 25.5 ∂ Dériver à travers un tirage : l'astuce de reparamétrisation · 25.7 ∂ La divergence KL entre N(μ, σ²) et N(0, 1) · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé) · 25.11 🗣️ Le VAE expliqué à un ami en cinq lignes · 25.13 📄 Lire Kingma et Welling (2013), « Auto-Encoding Variational Bayes » · 25.23 🔬 L'autoencodeur linéaire face à l'ACP de scikit-learn · 25.30 📦 Un VAE en PyTorch : reconstruction + KL · 25.31 🔮 Prédire : décoder des tirages N(0, I) avec un AE puis avec un VAE · 25.32 🔬 Un VAE est stochastique : sorties répétées, bruit relatif, interpolations · 25.33 🎨 Reproduire le nuage latent d'un VAE 2D et la grille −3…3 (fig. 25.67-25.68) · 25.34 📈 Diagnostiquer des courbes reconstruction/KL (effondrement du posterior) · 25.36 🔬 β-VAE : échanger la netteté contre la régularité · 25.38 🔨 Un VAE entièrement en NumPy avec mylearn · 25.Q9 🧠 Autoencodeur linéaire et ACP · 25.Q12 🧠 Les trois exigences d'un VAE et l'astuce de reparamétrisation · 25.R3 🔁 La divergence KL, ce que mesure le terme de régularisation du VAE · 25.E1 💼 Autoencodeur ou ACP : quand préférer l'un ou l'autre ? · 25.E2 💼 Pourquoi un VAE sait-il générer et pas un autoencodeur classique ? · 25.E3 💼 Expliquer l'astuce de reparamétrisation

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M25b.Q1 | 🧠 | Lire un graphe orienté : factoriser la loi jointe, l'ordre d'un tirage ancestral, et les variables qui deviennent dépendantes quand on observe leur effet commun | ★ | 4 | §1 | C, E | manuel | — |
| M25b.Q2 | 🧠 | Marginaliser ou conditionner : vraisemblance marginale, posterior d'un latent, moyenne et variance d'un mélange | ★ | 4 | §2 | C, E | manuel | — |
| M25b.Q3 | 🧠 | Un mélange de gaussiennes : responsabilités, logarithme d'une somme, vraisemblance infinie et composantes renumérotées | ★ | 4 | §3 | C, E | manuel | — |
| M25b.Q4 | 🧠 | L'EM : ce que font le pas E et le pas M, ce qui ne baisse jamais, ce qui n'est pas garanti, et k-means comme limite | ★ | 4 | §4 | C, E | manuel | — |
| M25b.Q5 | 🧠 | L'ELBO : une borne de quoi, une égalité quand, un écart égal à quelle KL ? | ★ | 4 | §5 | C, E | manuel | — |
| M25b.Q6 | 🧠 | L'ACP probabiliste : covariance marginale, rotation de W, angles principaux et directions éteintes | ★ | 4 | §6 | C, E | manuel | — |
| M25b.Q7 | 🧠 | KL directe ou inverse, inférence amortie et écart d'amortissement, et dériver sous l'espérance : quand le peut-on ? | ★ | 4 | §7 | C, E | manuel | — |
| M25b.Q8 | 🧠 | Pondérer la KL : multiplicateur, information mutuelle, posterior agrégé et code effondré | ★ | 4 | §8 | C, E | manuel | — |
| M25b.R1 | 🔁 | Bayes sur une variable cachée et log-sum-exp : probabilités totales, posterior, et une somme d'exponentielles sans dépassement (M04, M05a) | ★ | 6 | §2 §3 | C, E | manuel | — |
| M25b.R2 | 🔁 | L'inégalité de Jensen, la KL continue et l'information mutuelle (M06, M25a) | ★ | 6 | §5 §8 | C, E | manuel | — |
| M25b.R3 | 🔁 | La SVD, l'ACP et la projection orthogonale sur un sous-espace (M12b, M12d) | ★ | 6 | §6 | C, E | manuel | — |
| M25b.1 | ✏️ | Trois machines produisent des pièces de longueurs gaussiennes : le graphe, la loi jointe, un tirage ancestral à la main, la vraisemblance marginale d'une longueur et le posterior de la machine | ★★ | 20 | §1 §2 | C, E | wbm | — |
| M25b.2 | ✏️ | Deux variétés de grains de café (longueur, largeur) : moyenne et covariance du mélange par la variance totale, part de la variance entre variétés, et une corrélation qu'aucune variété n'a | ★★ | 25 | §2 | C, E | wbm | — |
| M25b.3 | ✏️ | Deux séries de résistances mélangées : les responsabilités de quatre mesures en log, un pas M (proportion, moyennes, variances), et la log-vraisemblance qui monte (suite de M13a, composantes inconnues) | ★★ | 35 | §3 §4 | C, E | wbm | — |
| M25b.4 | ∂ | Le pas M d'un mélange de gaussiennes : les poids N_k/n par un multiplicateur de Lagrange, les moyennes et les covariances comme maximum de vraisemblance pondéré | ★★ | 30 | §4 | C, E | manuel | — |
| M25b.5 | ∂ | L'ELBO en général : ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour un latent discret ou continu, la borne retrouvée par Jensen, et la forme E_q[ln p(x | z)] − KL(q ‖ p(z)) | ★★★ | 30 | §5 | C, E | manuel | — |
| M25b.6 | ✏️ | Une sonde de qualité de l'eau, un état caché à deux valeurs et une mesure gaussienne : ln p(x), l'ELBO pour trois lois q, et l'écart égal à la KL au posterior | ★★ | 25 | §5 | C, E | wbm | — |
| M25b.7 | ∂ | L'EM comme montée par coordonnées de l'ELBO : le pas E maximise en q, le pas M en θ, d'où la monotonie ; et ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] pour la moyenne d'une composante | ★★★ | 30 | §4 §5 | C, E | manuel | — |
| M25b.8 | ∂ | L'ACP probabiliste : la loi marginale N(μ, WWᵀ + σ²I), le posterior de z par le modèle linéaire gaussien, et W ou WR donnent la même loi | ★★ | 30 | §6 | C, E | manuel | — |
| M25b.9 | ✏️ | Trois épreuves d'un concours expliquées par une aptitude cachée : covariance marginale, posterior d'un candidat (une règle affine des notes), et maximum de vraisemblance à partir de valeurs propres données, dont une direction éteinte | ★★ | 30 | §6 §7 | C, E | wbm | — |
| M25b.10 | ✏️ | Les angles principaux entre deux plans de ℝ⁴ et entre deux droites de ℝ³ : bases orthonormées, SVD de Q_Aᵀ Q_B, et pourquoi le résultat ne dépend pas des bases choisies | ★★ | 25 | §6 | C, E | wbm | — |
| M25b.11 | ∂ | Dériver une espérance par rapport à un paramètre de la loi : l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré), la variance de l'estimateur à un tirage de ∂_σ E[e^X], et une indicatrice 1{X > c} pour laquelle l'échange échoue | ★★★ | 25 | §7 | C, E | manuel | — |
| M25b.12 | ✏️ | Le coût d'un stock c face à une demande gaussienne : E[(D − c)⁺], ses dérivées en μ et en σ par le chemin, puis par la formule fermée | ★★★ | 30 | §7 | C | wbm | — |
| M25b.13 | ✏️ | Une seule gaussienne pour la loi bimodale des temps de trajet par deux itinéraires : KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un itinéraire | ★★ | 25 | §7 | C, E | wbm | — |
| M25b.14 | ✏️ | Un code stochastique d'une source à trois symboles : posterior agrégé, information mutuelle, KL moyenne au prior décomposée en I(X ; Z) + KL(q(z) ‖ p(z)), puis le code qui s'effondre | ★★ | 30 | §8 | C, E | wbm | — |
| M25b.15 | ∂ | β comme multiplicateur de Lagrange : une mesure gaussienne codée avec du bruit, distorsion s² e^{−2I}, le lagrangien D + βI, et le code qui s'éteint quand β dépasse 2s² | ★★★ | 30 | §8 | C, E | manuel | — |
| M25b.16 | 📖 | MML §8.4 et §8.5 : modèles probabilistes, inférence bayésienne, modèles à variables latentes, graphes orientés et d-séparation (survol), en anglais | ★★ | 25 | §1 §2 | C | manuel | — |
| M25b.17 | 📖 | MML ch. 11 : mélange de gaussiennes, responsabilités, mises à jour, EM et point de vue latent, en anglais ; refaire l'Exemple 11.1 avec ses propres données | ★★ | 35 | §3 §4 §5 | C | manuel | — |
| M25b.18 | 📖 | MML §10.7 : l'ACP probabiliste, processus génératif, vraisemblance, loi jointe et posterior, en anglais | ★★ | 20 | §6 | C | manuel | — |
| M25b.19 | 🗣️ | Expliquer l'EM avec un bac de pièces venues de deux machines inconnues : deviner, réestimer, recommencer, sans jamais reculer | ★ | 10 | §4 | C, E | manuel | — |
| M25b.E1 | 💼 | « Pourquoi l'algorithme EM ne fait-il jamais baisser la vraisemblance, et vers quoi converge-t-il ? » | ★ | 10 | §4 §5 | C, E | manuel | — |
| M25b.20 | 🔨 | Les responsabilités d'un mélange de gaussiennes, calculées en log (le pas E) · `gmm_e_step` | ★★ | 30 | §3 | C, E | pytest | — |
| M25b.21 | 🔨 | Le pas M d'un mélange de gaussiennes : poids, moyennes et covariances pondérées, avec une régularisation · `gmm_m_step` | ★★ | 30 | §4 | C, E | pytest | — |
| M25b.22 | 🔨 | La log-vraisemblance d'un mélange de gaussiennes, et son ELBO pour des responsabilités quelconques · `gmm_log_likelihood, gmm_elbo` | ★★ | 25 | §3 §5 | C, E | pytest | — |
| M25b.23 | 🔗 | Pont : l'ELBO de n mesures rangées en lignes, écrite « reconstruction moins KL au prior » E_q[ln p(x | z)] − KL(q ‖ π), en nats par mesure, et ce que gagne chaque terme quand q devient le posterior | ★ | 20 | §5 | C, E | wbm | M25b.22 |
| M25b.24 | 📦 | `scipy.linalg.subspace_angles` et `np.linalg.eigh` : les angles principaux de M25b.10, et l'ACP probabiliste de mesures par leurs valeurs propres, contre la vraisemblance de `mvn_logpdf` | ★ | 20 | §6 | C, E | wbm | M25b.10 |
| M25b.25 | 🔮 | Prédire ce que devient la log-vraisemblance quand une composante centrée sur un point se resserre (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis avec une régularisation, et mesurer | ★ | 15 | §3 §4 | C | wbm | M25b.20, M25b.21, M25b.22 |
| M25b.26 | 🔬 | L'EM sur des longueurs de poissons de trois cohortes : la log-vraisemblance et l'ELBO après chaque demi-pas, sans régularisation, plusieurs initialisations et des maxima locaux | ★★ | 25 | §4 §5 | C, E | wbm | M25b.20, M25b.21, M25b.22 |
| M25b.27 | 🎨 | Une gaussienne ajustée à un mélange bimodal par KL(p ‖ q) puis par KL(q ‖ p) : les deux courbes, et les deux minima de la KL inverse | ★ | 20 | §7 | C | manuel | M25b.13 |
| M25b.28 | 🐛 | Chasse à l'erreur : des responsabilités sans log qui donnent 0/0, un pas M qui divise par n au lieu de N_k, et une ELBO sans l'entropie de q | ★ | 20 | §3 §4 §5 | C, E | wbm | — |
| M25b.29 | 🛠️ | Un test de propriété : sur des mélanges tirés au hasard, ELBO ≤ log-vraisemblance, égalité après le pas E, et un EM sans régularisation (reg = 0) qui ne descend jamais (à une tolérance près) | ★ | 15 | §4 §5 | C | manuel | M25b.20, M25b.21, M25b.22 |
| M25b.30 | 🏆 | Défi : retrouver trois populations de mesures en dimension 2 par l'EM, sous un seuil de log-vraisemblance moyenne sur des mesures de test | ★★★ | 25 | §4 | C | wbm | M25b.20, M25b.21, M25b.22 |

*Notes* : Frontières : le ∂ 25.5 (les dérivées de z = μ + σε par rapport à μ et à s = ln σ², ε fixé, E[z²] dérivée avant ou après l'espérance, l'estimateur à un tirage du VAE), le ∂ 25.7 (KL(N(μ, σ²) ‖ N(0, 1)), en s = ln σ², ses dérivées), le ∂ 25.8 (autoencodeur linéaire et ACP, déjà frontière de M12d), le 🗣️ 25.11 (ce qu'est un VAE), le 📄 25.13 (l'ELBO, AEVB et l'annexe B de Kingma et Welling), le 🔬 25.23 (autoencodeur linéaire contre ACP, angles entre sous-espaces, `subspace_angles_deg_23`), le 📦 25.30 (la loss « reconstruction + β KL » sommée, le β caché de 784), le 🔮 25.31 (décoder des tirages du prior), le 🔬 25.32 (sorties répétées, moyenne des sorties contre sortie de la moyenne), le 📈 25.34 et le 🔬 25.36 (effondrement du posterior, latents actifs, β montant, balayage de β), le 🎨 25.33 (le nuage des μ d'un VAE contre le prior, que le posterior agrégé du §8 explique), le 🔨 25.38 (gradient du VAE par deux chemins), les quiz 25.Q9 et 25.Q12, le rappel 25.R3 (la KL dans les deux sens : M25b enseigne le sens de la KL), les 💼 25.E1, 25.E2 et 25.E3. M25b travaille hors réseau : des machines et leurs pièces, des grains de café, des séries de résistances, des longueurs de poissons, une sonde de qualité de l'eau, les épreuves d'un concours, des plans de ℝ⁴, un stock face à une demande, des temps de trajet, une source à trois symboles, une mesure bruitée ; jamais un encodeur, un décodeur, un réseau, une image, ni un VAE (seulement nommé dans la fiche, comme ce que workbookIA 25 construira). **L'ELBO** est démontrée en général (∂ M25b.5 : pour un latent discret ou continu, par la décomposition en KL au posterior, puis par Jensen) et calculée là où tout se calcule : un latent à deux états et une mesure gaussienne (✏️ M25b.6), un mélange de gaussiennes (🔨 M25b.22, `gmm_elbo`), l'ACP probabiliste (posterior exact). Garde-fous : jamais l'ELBO d'un encodeur gaussien diagonal avec un prior N(0, I) et un décodeur de Bernoulli ou gaussien ; dans l'ACP probabiliste, l'écart à la vraisemblance s'écrit KL(q ‖ p(z | x)) entre deux gaussiennes dont aucune n'est le prior, et on ne calcule jamais KL(q(z | x) ‖ N(0, I)) ni une KL contre N(0, 1) ou N(0, τ²) (∂ 25.7, 🔨 25.29) ; la forme « reconstruction moins KL au prior » ne se calcule que pour un latent discret (KL(q ‖ π), 🔗 M25b.23) ; l'ELBO d'une chaîne de latents (diffusion) est à MB5. **L'EM** est une montée par coordonnées de l'ELBO (∂ M25b.7 ; MML §11.4.5 écrit Q(θ | θ_t)) ; ✏️ M25b.3 tient la promesse de M13a (estimer la proportion quand les composantes sont aussi inconnues), sans reprendre ses densités ni ses données ; k-means comme limite est dans la fiche (§4) et le quiz M25b.Q4 ; les singularités dans la fiche (§3), le quiz M25b.Q3 et le 🔮 M25b.25. Les courbes monotones (🔬 M25b.26, 🛠️ M25b.29) se tracent sans régularisation (reg = 0) : la régularisation ne sert qu'au 🔮 M25b.25 et au 🏆 M25b.30, et la fiche (§4) dit pourquoi (avec reg > 0, le pas M ne maximise plus, et l'EM peut faire baisser la log-vraisemblance et l'ELBO). Dans le 🔮 M25b.25, sans régularisation, la log-vraisemblance ne devient pas +∞ : `gmm_m_step` rend une covariance nulle (ou presque, à l'arrondi près), que `gmm_e_step` refuse quand Cholesky échoue ; l'expérience resserre donc à la main l'écart-type d'une composante centrée sur un point (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis applique reg. Le gradient de ln p(x) par l'identité ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] (∂ M25b.7) s'applique à la moyenne d'une composante d'un mélange, jamais à un réseau. **La dérivée d'une espérance** (la moitié « gradient » de la reparamétrisation ; la moitié « loi » est en M25a) se fait sur des coûts : ∂ M25b.11 démontre l'échange sous une hypothèse de domination, calcule la variance de l'estimateur à un tirage de ∂_σ E[e^X] et montre une indicatrice 1{X > c} pour laquelle l'échange échoue ; ✏️ M25b.12 dérive E[(D − c)⁺] pour un stock c (dérivées P(D > c) et σ N(c | μ, σ²), par le chemin puis par la formule fermée), avec θ = μ ou σ directement ; aucune comparaison « dériver avant ou après l'espérance » sur une fonction lisse (∂ 25.5.5) : la vérification par la formule fermée se fait sur le stock, une fonction seulement continue ; jamais z², ½(z − y)², s = ln σ², une log-variance, σ ⊙ ε, ni « un tirage par exemple dans un mini-batch » ; la méthode du score (∇ ln p) est seulement nommée (MB8). M25b.Q7 n'a aucun item « peut-on dériver à travers un tirage » (25.Q12 c, ∂ 25.5.4) : seulement les conditions de l'échange. **Le sens de la KL** : ✏️ M25b.13 et 🎨 M25b.27 approchent un mélange bimodal de temps de trajet par une seule gaussienne (KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un mode). **L'ACP probabiliste** applique le modèle linéaire gaussien et le conditionnement de M25a sans les redémontrer (∂ M25b.8) ; le maximum de vraisemblance de Tipping et Bishop est énoncé et appliqué à des valeurs propres données (✏️ M25b.9 : un facteur latent, trois épreuves, une direction éteinte quand le bruit est connu) ; l'inférence amortie s'y lit (la moyenne a posteriori est une règle affine des notes, valable pour tous les candidats) ; aucun autoencodeur linéaire, aucun « tr C − wᵀCw », ni cercle unité. **Les angles principaux** : ✏️ M25b.10 (deux plans de ℝ⁴, deux droites de ℝ³ d'un angle autre que 30°, par la SVD de Q_Aᵀ Q_B) et 📦 M25b.24 (`scipy.linalg.subspace_angles`) ; aucune fonction d'angles principaux dans `mymath` ni dans `latent.py` (le notebook les calcule en NumPy) ; l'indépendance vis-à-vis des bases se démontre (Q_A ↦ Q_A R_A), sans le contrôle « le même plan dans une autre base donne des angles nuls » ni une fonction qui convertit `subspace_angles` en degrés (`subspace_angles_deg_23` et ses deux contrôles, 25.23), et aucun angle n'est pris entre un W estimé et le sous-espace de l'ACP (la question du 🔬 25.23) ; M25b.Q6 ne reprend pas la QCM de 25.Q9 a (« les axes, le sous-espace, un sous-espace quelconque… »). **β** : ∂ M25b.15 le traite comme le multiplicateur d'un budget d'information sur une mesure gaussienne bruitée (I = ½ ln(1 + s²/v), D = s² e^{−2I}, le code s'éteint quand β ≥ 2s²), avec une variance de la source s² ≠ 1, l'information calculée par les entropies différentielles h(Z) − h(Z | X) de M25a et jamais par une KL contre une gaussienne centrée N(0, τ²) ; ✏️ M25b.14 décompose la KL moyenne au prior (posterior agrégé, information mutuelle, effondrement) sur des tableaux discrets, et prend la source égale à la loi marginale du modèle quand le posterior agrégé doit égaler le prior ; jamais de courbes d'entraînement, de seuil de latents actifs, de β = 1, 4, 16, 20 ou 100, ni de « KL annealing ». **Partage avec M25a** (voir les rapports) : M25a enseigne la densité (`mvn_logpdf`), les transformations affines et la loi de μ + Lε, le complément de Schur et le conditionnement, le modèle linéaire gaussien, le maximum de vraisemblance non pondéré, Jensen continu, la KL continue et la KL entre gaussiennes, l'entropie différentielle ; M25b les réutilise sans les redémontrer et garde les mélanges (moments, variance totale, MML Théorème 6.12), l'EM, l'ELBO, l'ACP probabiliste, la dérivée d'une espérance, le sens de la KL, les angles principaux, β, l'inférence amortie et le posterior agrégé. **Partage avec M26** : M25b définit l'espérance et la variance conditionnelles sachant une variable discrète et les lois de l'espérance et de la variance totales (les mélanges en ont besoin) ; M26, qui vient après, les rappelle et y ajoute la propriété de la tour et l'analyse au premier pas. **MML** : §8.4 (8.4.1 à 8.4.3) et §8.5 (8.5.1 ; la d-séparation de 8.5.2 en survol) avant §1 et §2 : 📖 M25b.16 ; §6.5.3 (le Théorème 6.12, les moments d'un mélange de deux gaussiennes) avant §2 ; ch. 11 (11.1 à 11.4) avant §3 à §5 : 📖 M25b.17 ; §10.7 (10.7.1 à 10.7.3) avant §6 : 📖 M25b.18. MML n'a pas l'ELBO (§11.4.5 s'arrête à Q(θ | θ_t)) : lecture libre conseillée, MacKay ch. 22 (EM, k-means doux) et ch. 33 (méthodes variationnelles). Exercices du livre conseillés : 6.11 (*Iterated Expectations*, l'espérance totale) et 6.2 (les moments d'un mélange de deux gaussiennes ; conseillé, jamais repris : ✏️ M25b.2 prend d'autres lois et d'autres nombres) ; les ch. 8, 10 et 11 n'en ont pas. **Conventions** : données rangées en lignes, de forme (n, d), dans `mymath` et le notebook (une mesure en dimension 1 est un tableau (n, 1)) ; poids (K,), moyennes (K, d), covariances (K, d, d) ; responsabilités (n, K) ; logarithmes népériens, ELBO, KL et informations en nats ; la fiche écrit les vecteurs en colonnes. `latent` : NumPy permis, de `np.linalg` seulement `cholesky` et `solve` (pour rien de plus que `gaussian`), ni `np.cov` ni `np.average` (avec `aweights` et `weights`, ils font le pas M, et ce sont les oracles des tests), aucune SciPy ; il importe `mvn_logpdf` de `gaussian` (M25a) et peut importer `logsumexp` d'`approx` (M05a), par des imports relatifs (tout import relatif de ses propres modules est permis) ; aucune fonction de KL, de reparamétrisation, d'angles principaux ni d'ACP probabiliste. Le notebook se sert aussi de `gaussian` : `sample_mvn` pour le tirage ancestral des données (🔬 M25b.26, 🏆 M25b.30), `mvn_logpdf` et `condition_gaussian` (le posterior de l'ACP probabiliste comme loi conditionnelle de la loi jointe de (z, x)) dans le 📦 M25b.24. Écarts au plan : `gmm_elbo` ajoutée (décision du coordinateur) ; MML §6.7 passe à M25a ; deux sessions de génération (§1 à §4, puis §5 à §8). Les exemples du stub ne reviennent dans aucun exercice : les mesures (0,5 ; 2 ; 3,5 ; 6) avec les poids (0,4 ; 0,6), les moyennes 1 et 5 et les variances 1 et 2, le point 1000 ; les points (0, 0), (1, 0), (0, 2), (4, 4), (5, 3) ; reg = 0,1 ; ✏️ M25b.3 (quatre mesures, comme l'exemple de `gmm_e_step`) prend d'autres poids que (0,4 ; 0,6), d'autres moyennes et d'autres variances. **Évités** (règle de partage, et reprises de ce dépôt) : l'ELBO d'un encodeur gaussien diagonal, d'un prior N(0, I) et d'un décodeur de Bernoulli ; la loss « reconstruction sommée + β KL » sur des images ; le facteur 784, « β caché de 784 », « 784 fois plus petite » ; β ∈ {0,5 ; 1 ; 4 ; 16} et {1, 20, 100, montant} ; 2, 3, 8, 10, 16, 20, 32, 50 et 64 latents ; le seuil de latents actifs 0,05 nat ; `HISTORY_34` ; les KL 17,6 → 2,2, 68,01 → 22,38, 45,6, 113,8 ; les reconstructions 171, 104 et 152 nats ; les covariances C = [[5, 2], [2, 2]] (valeurs propres 6 et 1, w = (2, 1)/√5) et [[3, 1], [1, 3]] (4 et 2) ; le cercle unité (C = ½ I, l'angle comme code) ; u = (0,6 ; 0,8) et x = (5, 0) ; les plans z = 0 et incliné de 30°, la base [[2, 1], [1, 3]], k = 16, les angles 1,6° et 6,4°, les cosinus 0,02 et 0,10, les erreurs 0,02727 et 0,02725, « k = 4, 2 epochs, 2 000 images » (25.23) ; 34 %, 69 %, 90 % contre 39 %, 86 %, 99 %, un nuage de moyennes comparé aux disques du prior (25.33) ; un tirage par exemple et le mini-batch de 100 de Kingma et Welling ; « moyenne des sorties contre sortie de la moyenne » d'un décodeur ; le PSNR moyen image par image ; la KL contre N(0, 1), N(0, I) ou N(0, τ²) et ½(μ² + σ² − 1 − ln σ²) ; s = ln σ² ; μ = 0,5, ln σ² = ln 0,25 et ε = −2 (workbookIA B5.R3) ; z = μ + σε avec (1,5 ; 0,5 ; −2) ; « 68 % entre −1 et 1 » ; la grille −3 à 3 et ses 80 tirages ; les 10 000 images, 60 000 exemples, 28 × 28, 512 × 512 × 3 et 64 × 64 × 4 ; le 99ᵉ centile ; de MML, (11.5) (0,5 N(−2, ½) + 0,2 N(1, 2) + 0,3 N(4, 1)), l'Exemple 11.1 (données {−3 ; −2,5 ; −1 ; 0 ; 2 ; 4 ; 5}, initialisation N(−4, 1), N(0 ; 0,2), N(8, 3), π = ⅓ ; refait avec d'autres données dans le 📖 seulement), les responsabilités (11.19), le mélange de l'exercice 6.2 (0,4 N((10, 2), I) + 0,6 N(0, [[8,4 ; 2] ; [2 ; 1,7]])), les figures de §10.7 ; de ce dépôt, l'exemple de mélange de M13a (f₀, f₁ et ses données), la matrice [[3, 1], [1, 2]] de 🔁 M09b.R1, les exemples des stubs `gaussian` (Σ = [[2, 3], [3, 9]], [[5, 2, 2], [2, 4, 0], [2, 0, 4]], Φ = [[1, 0], [1, 1], [1, 2]]) et `approx` ; MNIST, Fashion-MNIST, Frey Face, CIFAR-10 contre SVHN, l'anomalie MNIST contre Fashion-MNIST, le tigre. **Durée** : 17,1 h au lieu des 14 h prévues (essentiel 14,0 h ; lecture de la fiche 165 min au lieu de 150 après la session 63) : l'ELBO démontrée en général, la dérivée d'une espérance, les angles principaux, β, le posterior agrégé et l'inférence amortie, que la planification ne comptait pas, et quatre blocs de MML (≈ 35 pages, trois 📖 au lieu de 1–2). COMPOSITION : trois 📖 (quatre blocs de MML de sujets distincts).

<a id="m26"></a>
## M26 · Chaînes de Markov et équation de Bellman

**Partie** VI · **prépare** workbookIA 26 · **dossier** `chapitres/m26_markov_bellman/` · **MML** — · **sessions de génération** 1

Les chaînes de Markov finies et ce qu'on calcule sur elles : la matrice de transition, la loi après n pas (en convention ligne) et la loi stationnaire (existence, unicité, convergence, vitesse, et le PageRank) ; l'espérance conditionnelle et l'analyse au premier pas (la probabilité d'être absorbé, la durée moyenne avant la fin) ; le retour actualisé comme variable aléatoire, le facteur γ vu comme une probabilité de continuer, les décisions et les politiques ; l'équation de Bellman d'une politique fixée, un système linéaire (I − γP)V = r, résolu exactement ou par l'itération d'une contraction ; un opérateur avec un maximum, sur un problème d'arrêt optimal ; enfin ce que deviennent ces équations quand on n'a que des échantillons : la moyenne de retours simulés, l'erreur TD et le biais du maximum. workbookIA 26 applique ces outils à l'apprentissage par renforcement.

**Temps** : 14,6 h en parcours complet, 11,1 h en parcours essentiel (lecture 160 min, 22 flashcards).

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

**Notions enseignées** : chaîne de Markov finie : propriété de Markov, matrice de transition stochastique (lignes de somme 1), graphe de transition · convention ligne pour les lois : μ_{n+1} = μ_n P, loi à n pas μ₀Pⁿ, Chapman-Kolmogorov P^{m+n} = P^m P^n, (Pⁿ)_ij comme somme sur les chemins ; convention colonne pour les fonctions : E[f(S_{n+1}) | S_n = i] = (Pf)_i · ‖P‖∞ = 1 et ρ(P) = 1 ; loi stationnaire π = πP, Σπ = 1 : existence (Perron-Frobenius admis), calcul par un système linéaire ou par la méthode de la puissance · chaîne irréductible, apériodique : unicité de π et convergence de μ₀Pⁿ (énoncées) ; contre-exemples (chaîne périodique, chaîne à deux classes) ; vitesse de convergence fixée par |λ₂| · PageRank : le surfeur aléatoire et le facteur d'amortissement · espérance conditionnelle E[X | Y = y] et formule de l'espérance totale (rappel de M25b), propriété de la tour, appliquées à l'analyse au premier pas · états absorbants et transitoires ; analyse au premier pas : probabilités d'absorption h = Qh + b, durées moyennes t = 1 + Qt ; matrice fondamentale (I − Q)⁻¹ = Σ Qᵗ · retour actualisé G = Σ γᵗ r(S_t) comme variable aléatoire ; valeur V(s) = E[G | S₀ = s] ; γ comme probabilité de continuer : durée géométrique d'espérance 1/(1 − γ) · processus de décision markovien : états, actions, matrices P_a, récompenses r(s, a, s′) et leur moyenne r(s, a) ; politique déterministe ou stochastique ; chaîne induite P_π, r_π ; valeur d'une action Q^π(s, a) · équation de Bellman d'une politique fixée V = r + γPV : système linéaire (I − γP)V = r, inversible pour γ < 1 (‖γP‖∞ = γ), série de Neumann V = Σ γᵗPᵗr, loi d'occupation actualisée (1 − γ)(I − γP)⁻¹ ; une fin possible : matrice sous-stochastique, γ = 1 permis quand la fin est sûre · opérateur de Bellman, γ-contraction pour ‖·‖∞ ; convergence géométrique en γᵏ ; borne a posteriori γ/(1 − γ)‖V_k − V_{k−1}‖∞ et critère d'arrêt ; itérations synchrones (Richardson de pas 1) et en place (Gauss-Seidel) ; théorème du point fixe de Banach (énoncé) · un opérateur avec un maximum : |max x − max y| ≤ max |x − y| ; arrêt optimal V = max(g, c + γPV), valeur de continuation et règle à seuil ; équation d'optimalité de Bellman, itération sur les valeurs et politique gloutonne (énoncées) · estimer une valeur par la moyenne de retours simulés, tronqués ; pas 1/n et pas constant ; conditions de Robbins-Monro Σαₜ = ∞, Σαₜ² < ∞ (énoncées) · erreur TD δ = r + γV(s′) − V(s) : son espérance conditionnelle est le résidu de Bellman ; Σ γᵏ δ_{t+k} = G_t − V(S_t) (télescopage) ; récompense ajoutée γΦ(s′) − Φ(s) · biais du maximum : E[max X̂ᵢ] ≥ max E[X̂ᵢ], E[max(Z₁, Z₂)] = 1/√π ; estimateur double (choisir sur un échantillon, mesurer sur l'autre)

**Prérequis** : suites géométriques et leur somme, actualisation, moyennes mobile et exponentielle (R5) · logarithmes : résoudre γᵏ ≤ ε (R6) · loi géométrique et son espérance, loi normale, linéarité de l'espérance (M02b) · loi des grands nombres, erreur type d'une moyenne (M02c) · probabilité conditionnelle, probabilités totales (M03) · inégalité de Jensen (M06) · systèmes linéaires, inverse d'une matrice (M09a) · moyenne incrémentale, ε-greedy (une politique stochastique) (M11) · valeurs propres, diagonalisation et puissances, méthode de la puissance (M12c) · puissances d'une matrice d'adjacence : sommes sur les chemins d'un graphe (M16) · itérations linéaires, point fixe, itération de Richardson (M19) · tableaux à plusieurs axes, einsum (M20) · normes induites ‖·‖₁ et ‖·‖∞, ρ(A) ≤ ‖A‖, Aᵗ → 0 si ρ(A) < 1, applications contractantes et oubli du point de départ (M22) · espérance conditionnelle sachant une variable discrète, espérance et variance totales (M25b)

**mymath** : `markov.py` (signatures figées) : `n_step_distribution`, `stationary_distribution`, `bellman_linear_solve`, `bellman_fixed_point_iterates`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 26.7 ∂ Somme géométrique et horizon effectif de γ · 26.8 ∂ Équation de Bellman : le point fixe que vise le Q-learning · 26.1 ✏️ Retours total et actualisé d'une partie de six coups · 26.3 ✏️ Une mise à jour de Q-learning à la main · 26.4 ✏️ La même transition vue par SARSA · 26.5 ✏️ Probabilités d'action : ε-greedy (standard et version du livre) et softmax · 26.6 ✏️ Regarder la valeur remonter une chaîne d'états · 26.9 🧮 Mémoire d'une table Q : morpion 4×4, 5×5 et Go · 26.12 📄 Lire Mnih et coll. (2015), « Human-level control through deep reinforcement learning » · 26.14 🔨 Retours actualisés et retours à venir · 26.26 🔨 Itération sur les valeurs : la référence quand le modèle est connu · 26.Q6 🧠 Retour total, retour actualisé et rôle de γ · 26.Q8 🧠 La mise à jour du Q-learning : α, γ et la valeur de l'état suivant · 26.Q9 🧠 ε-greedy ou softmax : vrai ou faux · 26.Q10 🧠 Table initialisée à zéro : comment la valeur remonte et converge · 26.R3 🔁 Bandit à bras multiples, ε-greedy et UCB · 26.E2 💼 À quoi sert le facteur d'actualisation γ ? · 26.E4 💼 Pourquoi DQN utilise-t-il une mémoire de rejeu et un réseau cible ? · 11.2 ∂ Moyenne incrémentale : Qₙ₊₁ = Qₙ + (Rₙ − Qₙ)/n · 19.8 ∂ Moyenne mobile exponentielle : mémoire effective et biais initial · B8.Q4 🧠 Double DQN : d'où vient la surestimation des valeurs Q ? · B8.Q7 🧠 Avantage, erreur TD et GAE : ce que règle λ · B8.1 ✏️ Cible DQN à la main : état terminal, puis cible Double DQN · B8.4 ✏️ GAE à la main sur quatre pas, pour λ = 0, 0,95 et 1

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M26.Q1 | 🧠 | Matrice stochastique, convention ligne, loi à n pas et chemins du graphe : vrai ou faux | ★ | 4 | §1 | C, E | manuel | — |
| M26.Q2 | 🧠 | Une loi stationnaire existe-t-elle, est-elle unique, la loi de la chaîne y converge-t-elle ? Chaînes périodiques et à deux classes | ★ | 4 | §2 | C, E | manuel | — |
| M26.Q3 | 🧠 | Espérance conditionnelle, propriété de la tour et analyse au premier pas : quelle équation pour quel nombre ? | ★ | 4 | §3 | C, E | manuel | — |
| M26.Q4 | 🧠 | Le facteur γ : une actualisation, ou une probabilité de continuer ? Valeur d'un état et politique | ★ | 4 | §4 | C, E | manuel | — |
| M26.Q5 | 🧠 | Le système de Bellman d'une politique fixée : quelles matrices, pourquoi il est inversible, quand γ = 1 est permis | ★ | 4 | §5 | C, E | manuel | — |
| M26.Q6 | 🧠 | Contraction, bornes a priori et a posteriori, itérations synchrones ou en place : vrai ou faux | ★ | 4 | §6 | C, E | manuel | — |
| M26.Q7 | 🧠 | Un maximum dans l'opérateur : ce qui reste (contraction, point fixe unique), ce qui se perd (le système linéaire) | ★ | 4 | §7 | C, E | manuel | — |
| M26.Q8 | 🧠 | Des échantillons au lieu de P : moyenne de retours, pas 1/n ou constant, erreur TD, biais du maximum | ★ | 4 | §8 | C, E | manuel | — |
| M26.R1 | 🔁 | Puissances d'une matrice diagonalisable et méthode de la puissance (M12c) | ★ | 5 | §1 §2 | C, E | manuel | — |
| M26.R2 | 🔁 | La norme ‖·‖∞ d'une matrice, ρ(A) ≤ ‖A‖ et Aᵗ → 0 quand ρ(A) < 1 (M22), et la somme d'une série géométrique (R5) | ★ | 8 | §5 §6 | C, E | manuel | — |
| M26.R3 | 🔁 | Probabilités totales et espérance d'une loi géométrique (M03, M02b) | ★ | 5 | §3 §4 | C, E | manuel | — |
| M26.1 | ✏️ | Des vélos en libre-service entre trois stations : matrice de transition, graphe, loi après deux et trois jours, et coût moyen du lendemain (Pf) | ★ | 25 | §1 §3 | C, E | wbm | — |
| M26.2 | ✏️ | Trois opérateurs et leurs parts de marché : la loi stationnaire par un système linéaire, puis vérifier πP = π | ★★ | 25 | §2 | C, E | wbm | — |
| M26.3 | ✏️ | Trois chaînes qui posent problème, périodique, à deux classes et avec un état transitoire : lois stationnaires et comportement de Pⁿ | ★★ | 25 | §2 | C | wbm | — |
| M26.4 | ✏️ | Un cursus en trois années, avec redoublement et abandon : la probabilité d'être diplômé et la durée moyenne des études, par l'analyse au premier pas | ★★ | 30 | §3 | C, E | wbm | — |
| M26.5 | ✏️ | Un abonné qui peut résilier chaque mois : durée géométrique, revenu total moyen, et le même nombre comme revenu actualisé | ★ | 20 | §4 | C, E | wbm | — |
| M26.6 | ✏️ | Une machine qui s'use, deux politiques d'entretien : P_π et r_π, deux systèmes de Bellman 3 × 3, et la valeur d'une action | ★★ | 35 | §4 §5 | C, E | wbm | — |
| M26.7 | ✏️ | Les itérés de Bellman de la machine de M26.6 : trois pas synchrones puis en place, comparés à la solution, et le nombre d'itérations qui garantit 10⁻³ | ★★ | 30 | §6 | C, E | wbm | M26.6 |
| M26.8 | ✏️ | Vendre une voiture d'occasion : offres au hasard, coût d'attente, valeur de continuation et règle à seuil | ★★ | 30 | §7 | C, E | wbm | — |
| M26.9 | ✏️ | Le meilleur de deux fournisseurs sur des mesures bruitées : le maximum surestime, l'estimateur double non | ★★ | 25 | §8 | C | wbm | — |
| M26.10 | ∂ | L'analyse au premier pas démontrée : t = 1 + Qt et h = Qh + b, et I − Q inversible dès que la fin est possible depuis chaque état | ★★ | 25 | §3 | C | manuel | — |
| M26.11 | ∂ | V = Σ γᵗPᵗr est l'unique solution du système de Bellman : I − γP inversible, série de Neumann démontrée pour γP, et (1 − γ)(I − γP)⁻¹ stochastique | ★★ | 25 | §4 §5 | C, E | manuel | — |
| M26.12 | ∂ | L'opérateur de Bellman d'une politique fixée est une γ-contraction pour ‖·‖∞ ; bornes a priori et a posteriori ; le maximum est 1-lipschitzien | ★★ | 25 | §6 §7 | C, E | manuel | — |
| M26.13 | ∂ | L'erreur TD se télescope : Σ γᵏ δ_{t+k} = G_t − V(S_t) ; une récompense ajoutée γΦ(s′) − Φ(s) décale chaque valeur de −Φ(s) | ★★ | 20 | §8 | C | manuel | — |
| M26.14 | 🔗 | Pont : d'une politique stochastique à la chaîne qu'elle induit, P_π = Σ_a π(a | s) P_a et r_π avec des tableaux à trois axes (actions, états, états), puis Q^π(s, a) et r(s, a, s′) | ★★ | 25 | §4 §5 | C, E | wbm | — |
| M26.15 | 🗣️ | Expliquer avec une image hors informatique pourquoi une chaîne qui mélange oublie son état de départ | ★ | 10 | §2 | C, E | manuel | — |
| M26.E1 | 💼 | « Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que se passe-t-il pour γ = 1 ? » | ★ | 10 | §5 | C | manuel | — |
| M26.16 | 🔨 | La loi d'une chaîne après n pas, en convention ligne · `n_step_distribution` | ★ | 20 | §1 | C, E | pytest | — |
| M26.17 | 🔨 | La loi stationnaire par un système linéaire, et le refus d'une chaîne qui en a plusieurs · `stationary_distribution` | ★★ | 25 | §2 | C, E | pytest | — |
| M26.18 | 🔨 | Le système de Bellman d'une politique fixée, avec une fin possible (matrice sous-stochastique) et γ = 1 quand la fin est sûre · `bellman_linear_solve` | ★★ | 25 | §5 | C, E | pytest | — |
| M26.19 | 🔨 | Les itérés de l'opérateur de Bellman d'une politique fixée (Richardson de pas 1) · `bellman_fixed_point_iterates` | ★ | 20 | §6 | C, E | pytest | — |
| M26.20 | 📦 | La loi stationnaire de trois façons, `np.linalg.eig` sur Pᵀ, `scipy.linalg.null_space` et la méthode de la puissance, sur le surfeur aléatoire d'un web de six pages | ★ | 20 | §2 | C | wbm | — |
| M26.21 | 🔮 | Prédire la somme des lignes de (1 − γ)(I − γP)⁻¹, puis leur limite quand γ tend vers 1, et vérifier | ★ | 15 | §2 §5 | C, E | wbm | M26.17, M26.18 |
| M26.22 | 🔬 | Le biais du maximum par simulation : k fournisseurs de même qualité, n mesures chacun, le meilleur mesuré contre l'estimateur double | ★★ | 20 | §8 | C | wbm | — |
| M26.23 | 🎨 | La loi d'une chaîne au fil des pas depuis trois départs, et ‖μ_n − π‖₁ en échelle logarithmique contre |λ₂|ⁿ | ★ | 15 | §1 §2 | C | manuel | M26.16, M26.17 |
| M26.24 | 🐛 | Chasse à l'erreur : une matrice lue dans la mauvaise convention, une loi stationnaire non normalisée, un état final qui rapporte encore, γ = 1 sans fin | ★ | 25 | §1 §2 §5 | C, E | wbm | — |
| M26.25 | 🛠️ | Un test de propriété : πP = π, et pour `bellman_fixed_point_iterates`, V_k − V tenu par γᵏ‖V₀ − V‖∞ et V = r + γPV pour la limite, sur des chaînes tirées au hasard | ★ | 20 | §2 §6 | C | manuel | M26.17, M26.18, M26.19 |
| M26.26 | 🏆 | Défi : estimer la valeur d'un état à 0,01 près en simulant l'arrêt géométrique (continuer avec la probabilité γ) et en sommant les récompenses sans actualisation, sous un budget de pas simulés | ★★★ | 30 | §4 §8 | C | wbm | M26.18 |

*Notes* : Frontières : les ∂ 26.7 (la somme géométrique (1 − γⁿ)/(1 − γ), la borne r_max/(1 − γ), les horizons 2, 10 et 100, la demi-vie ln 2/(−ln γ), 0,2⁴ et 0,2⁶) et 26.8 (l'équation d'optimalité sur le MDP A, B, T, son système 2 × 2 sous une politique supposée optimale, la contraction de l'opérateur d'optimalité en norme max et la convergence vers une seule table, la cible du Q-learning comme échantillon et le rôle de α), les ✏️ 26.1 (les retours d'une partie de six coups), 26.3 et 26.4 (une mise à jour de Q-learning et de SARSA), 26.5 (les probabilités d'ε-greedy et de la softmax), 26.6 (la valeur qui remonte une chaîne, un état par épisode), 🧮 26.9 (la mémoire d'une table Q), 📄 26.12 (DQN, et sa variante Double Q-learning), 🔨 26.14 (retours et retours à venir) et 26.26 (`value_iteration`), les quiz 26.Q6 (retour d'une courte suite, horizon de 0,95), 26.Q8, 26.Q9 et 26.Q10 (la valeur qui remonte depuis une table nulle), le rappel 26.R3 (la mise à jour incrémentale d'un bandit), 26.E2 (à quoi sert γ) et 26.E4 (rejeu, réseau cible, surestimation corrigée par le Double DQN) ; de workbookIA 11 et 19, faits avant M26, ∂ 11.2 (la moyenne incrémentale) et ∂ 19.8 (la mémoire effective et le biais initial d'une moyenne exponentielle), énoncés et utilisés, jamais redémontrés ; de workbookIA B8, B8.Q4 (d'où vient la surestimation), B8.1 (cible DQN puis Double DQN), B8.Q7 et B8.4 (avantage, erreur TD et GAE : M26 n'écrit aucune somme pondérée par λ). M26 enseigne les outils hors apprentissage par renforcement : des vélos entre des stations, des parts de marché, un petit web, un cursus avec redoublement et abandon, un abonné qui peut résilier, une machine qui s'use et son entretien, un stock, la vente d'une voiture d'occasion, des fournisseurs mesurés avec du bruit ; jamais un agent, un jeu, un coup, une partie, une table Q, une cible r + γ max Q, un learning rate α appliqué à une table, ni Gymnasium (son format P[s][a] = [(p, s′, r, fin)], `terminated` et `truncated`). L'espérance conditionnelle sachant une variable discrète et la formule de l'espérance totale sont définies en M25b (les mélanges) : M26 les rappelle et y ajoute la propriété de la tour et l'analyse au premier pas. ∂ M26.11 démontre la série de Neumann pour γP en entier (‖γP‖∞ = γ < 1), sans renvoyer à CP5.8, un sujet au choix, ni à M22, qui ne l'écrit que dans un corrigé. Contraction et maximum (les deux moitiés de ∂ 26.8.3, que M22 a laissées à M26) : le §6 démontre la contraction de l'opérateur de Bellman d'une politique **fixée**, qui est affine (‖γP(V − W)‖∞ ≤ γ‖V − W‖∞ par ‖P‖∞ ≤ 1, M22), et les bornes a priori γᵏ‖V₀ − V‖∞ et a posteriori γ/(1 − γ)‖V_k − V_{k−1}‖∞ (∂ M26.12), sans avoir besoin de Banach (le point fixe existe : c'est la solution du système) ; l'existence du point fixe d'une contraction non linéaire (Banach) est énoncée et admise, comme en M22. Le §7 démontre le lemme |max x − max y| ≤ max |x − y| sur des vecteurs quelconques (l'indication que donne ∂ 26.8.3) et s'en sert sur un problème d'arrêt optimal à offres indépendantes (une seule équation pour la valeur de continuation, une règle à seuil) ; que l'opérateur d'arrêt V ↦ max(g, c + γPV) est une γ-contraction est **énoncé**, sans démonstration : combiner le lemme et le §6 est ce que ∂ 26.8.3 fait pour l'opérateur d'optimalité : ni la grille de ∂ M26.12, ni la fiche, ni un quiz n'écrivent la chaîne |max(g, c + γPV) − max(g, c + γPW)| ≤ … ; M26.Q7 énonce la contraction de l'opérateur d'arrêt comme un fait, sans demander de justification ; dans M26.6, la valeur d'une action Q^π(s, a) ne sert ni à vérifier qu'une politique est gloutonne pour ses propres valeurs, ni à désigner la meilleure des deux (∂ 26.8.2). L'équation d'optimalité de Bellman, l'itération sur les valeurs et la politique gloutonne sont énoncées, jamais résolues sur un MDP à plusieurs actions : ni « supposer la politique optimale et résoudre » (∂ 26.8.2), ni table Q*. Le §8 relie l'erreur TD d'une politique fixée au résidu de Bellman (son espérance conditionnelle) et démontre le télescopage (∂ M26.13, que MB8 rappellera, sur des épisodes qui finissent, de valeur 0 à la fin : ni troncature avec amorçage, ni question sur la dépendance de la somme à V, B8.4 j, B8.Q7 e–f) ; il n'écrit aucune cible avec un max et ne discute pas α dans le Q-learning (∂ 26.8.4) : le pas 1/n et le pas constant portent sur des mesures ou des retours simulés, et Σαₜ = ∞, Σαₜ² < ∞ sont énoncées (Robbins-Monro), sans preuve. Le biais du maximum (E[max X̂ᵢ] ≥ max E[X̂ᵢ] ; E[max(Z₁, Z₂)] = 1/√π pour deux gaussiennes centrées réduites indépendantes ; l'estimateur double) porte sur des fournisseurs ou des réglages mesurés avec du bruit (la malédiction du vainqueur, et le score de validation optimiste d'un modèle choisi sur la validation), sans réseau, DQN, cible ni van Hasselt. Le facteur γ : M26 l'interprète comme une probabilité de continuer (arrêt avec la probabilité 1 − γ à chaque pas, durée géométrique d'espérance 1/(1 − γ), M02b), sur un abonné qui résilie (M26.5) ; il ne redémontre pas la somme géométrique (R5) et ne parle ni d'« horizon effectif » ni de demi-vie de γ (∂ 26.7) ; aucun quiz ne calcule le retour d'une courte suite de récompenses (26.Q6), et la valeur actuelle d'un échéancier (R5.11) n'est qu'un exemple de la fiche, sans fonction de `mymath` (🔨 26.14). Les γ des exercices de M26 sont pris parmi 0,6, 0,7, 0,85 et 0,96 : jamais 0,2, 0,5, 0,8, 0,9, 0,95 ni 0,99, les facteurs de workbookIA 26 (0,8 : sa fiche et le 🔨 26.20), ni 0,75 (les exemples de `markov`). La loi stationnaire ne sert aucun exercice de workbookIA 26 : un § court (existence par ‖P‖∞ = 1 et ρ(P) = 1 ; unicité et convergence pour une chaîne irréductible apériodique énoncées, avec deux contre-exemples ; vitesse |λ₂|ⁿ, la chaîne à deux états entièrement calculée dans la fiche ; PageRank), un seul ✏️ dans le parcours essentiel (M26.2), justifié dans la fiche par la promesse de M12c (§3 et §4 : le PageRank par la méthode de la puissance, la vitesse par la deuxième valeur propre), par la fréquence de visite des états, par MB5 (une chaîne qui converge vers sa loi stationnaire) et par MB8 (la loi d'occupation actualisée (1 − γ)μ₀(I − γP)⁻¹, dont les lignes tendent vers π quand γ → 1 : 🔮 M26.21). Conventions : π(a | s) est une politique (comme workbookIA 26) ; la loi stationnaire s'écrit π aux §1 à §3 et d_π pour celle de P_π à partir du §4, et un encadré 📐 le dit (la docstring de `stationary_distribution` garde π) ; les lois sont des lignes (μ_{n+1} = μ_nP, celle des probabilistes), les valeurs des colonnes ((PV)_i = E[V(S₁) | S₀ = i]) ; un encadré 📐 le dit au §1 et le relie à la convention colonne de M22 (μ₀Pⁿ est la récurrence de M22 pour Pᵀ, sans entrée). workbookIA 26 n'écrit jamais P comme une matrice (des sommes Σ_{s′} P(s′ | s, a), avec r(s, a, s′)) : le 🔗 M26.14 fait le passage. Une fin possible se code de deux façons qui donnent les mêmes valeurs : un état absorbant de récompense nulle, ou une ligne sous-stochastique (la masse manquante est la probabilité de finir) ; c'est le « le max vaut 0 quand s′ est terminal » de workbookIA 26, et γP est elle-même sous-stochastique (actualiser, c'est finir avec la probabilité 1 − γ). M26.6 et M26.7 portent sur la même machine (M26.7 itère vers la solution exacte de M26.6). `markov` : NumPy permis, mais de `np.linalg` seulement `solve` et `matrix_rank`, dans `stationary_distribution` et `bellman_linear_solve` ; ni `matrix_power`, `eig`, `eigvals`, `inv`, ni SciPy (oracles des tests : `np.linalg.matrix_power`, `np.linalg.eig` sur Pᵀ, `scipy.linalg.null_space`, `scipy.linalg.solve`, la série Σ γᵗPᵗr tronquée, la propriété V = r + γPV et la borne γᵏ‖V₀ − V‖∞ ; jamais une autre fonction de l'apprenant ; les tests de γ = 1 restent sur des cas bien conditionnés, cond(I − P) ≤ 10⁸, et un P ou un μ₀ non fini est refusé). `bellman_linear_solve` est l'oracle des tests de `value_iteration` dans workbookIA 26, avec un contrat distinct : la matrice m × m de la politique fixée (pas le dictionnaire de Gymnasium), un vecteur de récompenses, V seul (ni Q, ni max, ni actions). `bellman_fixed_point_iterates` est calqué sur `richardson_iterates` (M19) : sans max, sans seuil d'arrêt ni nombre maximal d'itérations, il ne remplace pas `value_iteration` (🔨 26.26) ; il calculerait les itérés de ✏️ 26.6 et de 26.Q10 sur leur chaîne, donc il ne sert à aucun exercice de M26 sur une chaîne qui avance d'un état par pas avec une seule récompense finale (26.6, 26.Q10, Évités). Aucune fonction de retour actualisé, de politique, de mise à jour, d'arrêt optimal ni de simulation. `markov_bound` (M11) est l'inégalité de Markov : la docstring du module le signale. Évités (règle de partage) : la chaîne 0 → 1 → 2 → 3 à récompense finale 1 avec γ = 0,9 (valeurs 1, 0,9 et 0,81), ses variantes (10 états ; γ = 0,5 → 0,25 ; α = 0,5 → 0,225 et 0,875) ; la chaîne P_26 de 26.26 (0 → 1 → 2, récompense 1 au dernier pas, l'action 1 ramène en 0, γ = 0,5, V* = (0,5 ; 1 ; 0), Q* = [[0,5 ; 0,25] ; [1 ; 0,25] ; [0 ; 0]]) ; le MDP A, B, T de ∂ 26.8 (rester, aller, finir, jouer ; récompenses 0, 0, 1 et 2 ; probabilité ½ ; γ = 0,9 ; 400/119, 360/119, 324/119, 0,595, 0,405 ; échantillons 2 ou 4,72, moyenne 3,36 ; variante 0,5 → 0,9, 0,81 et 0,905) ; l'exemple de `value_iteration` (rester 0 ou finir 1, γ = 0,9 → V = (1 ; 0), Q = [[0,9 ; 1] ; [0 ; 0]]) ; les récompenses (0, 0, 1), (2, 0, 1), (1, 0, 0, 2, 0, 4), (0, 3, 0, 1), (1, 1, 1, 1), (1, 0, 2) et (1, 1, 1) et leurs retours (0,81, 2,25, 1,375, 4,820, 5,24, 1,625, 1,875, 1,75, 1,5) ; REWARDS_15 (graine 2615) et ses retours 0,80 à 8,06 ; γ = 0,2, 0,5, 0,9, 0,95 et 0,99, les horizons 2, 10, 20 et 100, les demi-vies 6,58, 7, 13,5, 14, 68,97 et 69, 0,2³, 0,2⁴, 0,2⁵, 0,2⁶ et 1/(1 − 0,2) = 1,25 ; les lignes Q (0,1 ; 0,6 ; 0,3 ; 0,6), (1, 2, 4, 0), (1 ; 2 ; 4 ; 0,5) et [[0,2 ; 0,4] ; [1 ; 0,6] ; [0 ; 0]], r = 0,2 et Q = 0,5 (0,74, 0,24, 0,62, 0,35, 0,47, 0,485), Q = 0,4, r = 0,1, γ = 0,8 et max 0,5 (cible 0,5, δ = 0,1, 0,45), r = 0,5 et γ = 0,8 (1,3, 0,9, 0,85), Q = 0,4, max 0,8 → 0,6, le bandit 3, 5 et 0,25 → 3,5 ; ε = 0,2 avec 4 actions (0,85, 0,05, 0,80, 0,067), ε = 0,1 avec 5 actions (0,92), les températures 1, 2, 0,5 et 0,8 (0,831, 0,579, 0,979, 0,571) ; FrozenLake (16 états, V*(0) = 0,54 et 0,069, 73,2 % et 74,9 %), Flippers et son camion, le L-learning, CliffWalking, le morpion, CartPole, le go, AlphaGo, le backgammon, les robots, les ascenseurs, les cultures, le cuisinier et son minuteur, le compte en banque de la fiche de workbookIA 26 ; 2⁹, 3⁹, 3¹⁶, 3³⁶¹, 5 478, 255 168, 3²⁵ et les mémoires de 🧮 26.9 (4 octets, 16 Go, 2,8 Go, 85 To, 10⁹ mises à jour par seconde, 25 → 256 → 256 → 25 et 78 873 paramètres) ; le DQN de Mnih (84 × 84, 18 actions, 10 000 pas, un million, 32, ε de 1 à 0,1) ; le paradoxe des anniversaires (32 parmi 1 000, 0,39) ; les cinq graines (57, 35, 74, 74 et 38 %, [41,2 ; 70,6]). Évités aussi (reprises de ce dépôt) : les exemples des docstrings de `markov` ([[0,5 ; 0,5 ; 0] ; [0,25 ; 0,5 ; 0,25] ; [0 ; 0,5 ; 0,5]], [[0,6 ; 0,4] ; [0,2 ; 0,8]], [[0,5 ; 0,5] ; [0 ; 1]] avec r = (1, 2) et γ = 0,75, [[0,5 ; 0,25] ; [0,5 ; 0]]), la contraction de ∂ M22.14 (A = [[0,3 ; −0,3] ; [0,1 ; 0,3]], c = (1, 2)), les polluants du lac et la plante de M22, la barre qui tiédit et les deux ressorts de M19, les matrices de M12c §4 et §5, la population à pile ou face de M22 §5. Pas de MML (le livre ne traite pas les chaînes de Markov), donc pas de 📖 ; références libres : Blitzstein et Hwang, ch. 11 (chaînes de Markov) ; pour Bellman, Sutton et Barto (2ᵉ éd.), §3.5-3.6 et §4.1-4.4, cités par sections. 14,6 h au lieu des 12 h prévues : la propriété de la tour et l'analyse au premier pas, le cas d'une fin possible (γ = 1 quand la fin est sûre), l'arrêt optimal, l'erreur TD et le biais du maximum, que workbookIA 26 suppose ou que MB8 rappellera ; la loi stationnaire reste courte, Banach et la convergence d'une chaîne irréductible apériodique sont énoncés.

<a id="m27"></a>
## M27 · Jeux et distances entre lois

**Partie** VI · **prépare** workbookIA 27 · **dossier** `chapitres/m27_jeux_distances/` · **MML** §7.2 · **sessions de génération** 1

Les jeux à deux joueurs et les distances entre lois. D'abord les jeux à somme nulle : la matrice des gains, le maximin et le minimax (l'inégalité minimax de MML §7.2), les points selles et les stratégies dominées ; les stratégies mixtes, la stratégie d'indifférence d'un jeu 2 × 2 et le théorème minimax de von Neumann ; l'équilibre de Nash d'un jeu quelconque et l'induction arrière sur un arbre de jeu ; la descente-montée de gradient sur un jeu bilinéaire, qui tourne autour de l'équilibre ou s'en éloigne. Puis les lois : la probabilité a posteriori est le meilleur prédicteur pour la log-loss ; la divergence de Jensen-Shannon plafonne à ln 2 quand les supports se séparent ; les couplages et les distances de Wasserstein, calculées en dimension 1 par les fonctions de répartition et les quantiles, dont W₂ de deux gaussiennes ; la distance de Fréchet entre gaussiennes et le biais d'une distance estimée sur des échantillons ; enfin trois mesures d'une dérive (PSI, Kolmogorov-Smirnov, W₁). workbookIA 27 applique ces outils aux GAN, et workbookIA B7 à la surveillance d'un modèle en production.

**Temps** : 14,4 h en parcours complet, 10,5 h en parcours essentiel (lecture 150 min, 20 flashcards).

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

**Notions enseignées** : jeu à deux joueurs à somme nulle : matrice des gains, maximin et minimax en stratégies pures, maximin ≤ minimax (l'inégalité minimax, MML §7.2), point selle, stratégies dominées · l'ordre compte : le joueur qui annonce son coup en second a l'avantage ; la dualité faible lue comme un jeu · stratégies mixtes : gain espéré pᵀGq, stratégie d'indifférence d'un jeu 2 × 2 (démontrée optimale), valeur d'un jeu · théorème minimax de von Neumann (énoncé) ; un jeu fini est un programme linéaire (énoncé) · équilibre de Nash : définition générale, jeux à somme non nulle (dilemme du prisonnier, coordination), équilibres multiples, purs et mixtes ; dans un jeu à somme nulle, un couple de stratégies optimales · arbres de jeu : induction arrière, minimax d'un arbre · dynamique de gradients sur un jeu : descente-montée simultanée (une spirale qui s'éloigne) et alternée (une courbe fermée, une ellipse : x² + y² − ηxy reste constant sur xy) sur un jeu bilinéaire ; l'équilibre est un point selle de f · meilleur prédicteur pour la log-loss : la probabilité a posteriori P(Y = 1 | x) = π₁p₁(x)/(π₁p₁(x) + π₀p₀(x)) (Bayes, priors quelconques) ; le maximum de vraisemblance k ln p + (n − k) ln(1 − p) d'une loi de Bernoulli rappelé (M04.12, M13a.1), avec des comptes entiers · divergence de Jensen-Shannon revisitée : 0 ≤ JS ≤ ln 2, JS = ln 2 pour des supports disjoints, constante (sans pente) quand les supports se séparent ; la KL y est infinie · couplages et plans de transport sur des supports finis (marges imposées, couplage indépendant), coût d'un plan, distances de Wasserstein W_p ; le transport optimal est un programme linéaire · W₁ ≤ W₂ (Jensen sur un même couplage) ; dualité de Kantorovich-Rubinstein : W₁ comme un maximum sur les fonctions 1-lipschitziennes (énoncée) · W_p en dimension 1 : W₁ = ∫|F − G|, W_p^p = ∫₀¹|F⁻¹(u) − G⁻¹(u)|^p du (le couplage des quantiles, optimal) ; appariement trié optimal (argument d'échange) · W₂ de deux gaussiennes en dimension 1 : W₂² = (μ₁ − μ₂)² + (σ₁ − σ₂)² ; W_p d'une translation · distance de Fréchet (W₂) entre gaussiennes : formule (admise en général), Tr((Σ₁Σ₂)^{1/2}) = Σ√λᵢ(Σ₁Σ₂), Σ₁Σ₂ semblable à Σ₁^{1/2}Σ₂Σ₁^{1/2} (Σ₁ définie positive) ; cas commutatif démontré (une somme de W₂² en dimension 1) ; invariance par une rotation commune · biais d'une distance estimée : E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ ; comparer à tailles égales · mesurer une dérive : PSI = KL(p ‖ q) + KL(q ‖ p) (divergence de Jeffreys) sur des classes, et J = Σ(p_k − q_k) ln(p_k/q_k) ≈ Σ(p_k − q_k)²/q_k pour un petit décalage ; statistique de Kolmogorov-Smirnov sup|F − G|, W₁ = ∫|F − G| ; unités, invariances, W₁ ≤ (b − a)·KS sur [a, b]

**Prérequis** : intégrales, changement de variable, fonction de répartition et quantile F⁻¹(u) = inf{x : F(x) ≥ u} (M02a) · espérance d'une variable discrète, indépendance, fonction de répartition, loi normale et Φ, simulation par inversion F⁻¹(U) (M02b) · biais d'un estimateur, variance d'une moyenne, matrice de covariance (M02c) · formule de Bayes, a priori et a posteriori ; le maximum de vraisemblance d'une loi de Bernoulli est la fréquence (M04) · point selle d'une fonction de deux variables, descente et montée de gradient (M05b) · divergence KL, inégalités de Jensen et de Gibbs, divergence de Jensen-Shannon (M06) · p-valeur d'un test (M08) · programmes linéaires (M10) · trace, matrices semblables, théorème spectral, racine carrée d'une matrice symétrique positive (M12c) · log-loss, la log-loss quand la probabilité prédite tend vers 0 (M13a) · lagrangien et dualité faible, MML §7.2 lu une première fois (M13b) · valeurs propres complexes d'une matrice 2 × 2, module, rotations et homothéties, puissances (M22) · KL entre deux lois continues, KL infinie quand le support de q ne couvre pas celui de p (M25a)

**mymath** : `distances.py` (signatures figées) : `pure_strategy_values`, `mixed_strategy_value_2x2`, `descent_ascent_iterates`, `w2_gaussians_1d`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 27.5 ∂ Le discriminateur optimal D* = p_data / (p_data + p_g) · 27.6 ∂ Pourquoi log(1 − D(G(z))) sature et pas −log D(G(z)) · 27.2 ✏️ Valeur minimax d'une petite matrice de gains · 27.3 ✏️ Losses BCE du discriminateur et du générateur à partir de sorties données · 27.4 ✏️ À l'équilibre, la loss vaut ln 2 et non 0,5 · 27.7 🧮 Croissance progressive : où passe le temps de calcul ? · 27.10 📄 Lire Goodfellow et coll. (2014), « Generative Adversarial Nets » · 27.11 🔨 Distance de Wasserstein 1D entre deux échantillons · 27.13 🔮 Prédire la moyenne et l'écart-type générés au fil des epochs · 27.14 📈 Lire les courbes d'un GAN : losses, D(x) et D(G(z)) · 27.18 🔬 Loss saturante ou non saturante : la dynamique du début · 27.22 🔨 Distance de Fréchet entre deux gaussiennes (la formule du FID) · 27.23 📦 Évaluer un générateur : distance de Fréchet sur les features d'un classifieur · 27.Q5 🧠 Coopératifs ou antagonistes : somme nulle, minimax et équilibre de Nash · 27.E1 💼 Expliquer l'entraînement d'un GAN et sa loss · 27.E4 💼 Comment évaluer un modèle génératif (FID et ses limites) ? · 27.E5 💼 Pourquoi l'entraînement des GAN est-il instable ? · B7.4 ✏️ Indice de stabilité de population (PSI) à la main sur quatre intervalles · B7.22 📈 Surveiller la dérive : PSI et test KS sur des images assombries ou bruitées, quand alerter ? · B7.Q11 🧠 Écart entraînement-production et dérive des données : vrai ou faux · B7.E4 💼 Comment surveilles-tu un modèle en production, et que fais-tu en cas de dérive ?

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M27.Q1 | 🧠 | Maximin, minimax et point selle : qui annonce son coup en premier, et qui y gagne ? | ★ | 4 | §1 | C, E | manuel | — |
| M27.Q2 | 🧠 | Stratégies mixtes, gain espéré et valeur d'un jeu : vrai ou faux | ★ | 4 | §2 | C, E | manuel | — |
| M27.Q3 | 🧠 | Équilibres de Nash, arbres de jeu et descente-montée : unique ou non, le meilleur pour tous ou non, converger ou tourner ? | ★ | 4 | §3 §4 | C, E | manuel | — |
| M27.Q4 | 🧠 | La probabilité a posteriori et la log-loss ; Jensen-Shannon et KL quand les supports se séparent | ★ | 4 | §5 §6 | C, E | manuel | — |
| M27.Q5 | 🧠 | Couplages et distances de Wasserstein : marges, translation, dilatation, et W₁ ≤ W₂ | ★ | 4 | §7 §8 | C, E | manuel | — |
| M27.Q6 | 🧠 | La distance de Fréchet et son estimation : rotation commune, covariances, taille des échantillons | ★ | 4 | §9 | C, E | manuel | — |
| M27.Q7 | 🧠 | Mesurer une dérive : PSI, KS ou W₁, leurs unités, et ce que chacun ne voit pas | ★ | 4 | §10 | C, E | manuel | — |
| M27.R1 | 🔁 | Le maximum de vraisemblance d'une loi de Bernoulli (des comptes entiers), et la log-loss quand la probabilité prédite tend vers 0 (M04, M13a) | ★ | 8 | §5 | C, E | manuel | — |
| M27.R2 | 🔁 | Les valeurs propres complexes d'une matrice réelle 2 × 2, leur module et les puissances (M22) | ★ | 5 | §4 | C, E | manuel | — |
| M27.R3 | 🔁 | La racine carrée d'une matrice symétrique positive, et la trace comme somme des valeurs propres (M12c) | ★ | 5 | §9 | C, E | manuel | — |
| M27.1 | ✏️ | Deux enseignes se partagent un marché : réduire une matrice 3 × 4 par dominance, trouver ses deux points selles et vérifier qu'ils ont la même valeur, et ce que la réduction ne change pas (maximin, minimax) | ★ | 20 | §1 | C, E | wbm | — |
| M27.2 | ✏️ | Tirs au but : la probabilité de tirer à gauche par indifférence, la réponse du gardien et la valeur du jeu | ★★ | 20 | §2 | C, E | wbm | — |
| M27.3 | ✏️ | Les équilibres de Nash d'un dilemme du prisonnier et d'un jeu de coordination (purs et mixte), puis la valeur d'un jeu d'allumettes par induction arrière | ★★ | 25 | §3 | C, E | wbm | — |
| M27.4 | ✏️ | Descente-montée sur f(x, y) = xy : la matrice d'un pas simultané puis alterné, leurs valeurs propres et leurs modules, et deux pas différents pour x et y | ★★ | 25 | §4 | C, E | wbm | — |
| M27.5 | ✏️ | Deux fournisseurs et un défaut noté sur quatre niveaux : la probabilité a posteriori, et la log-loss moyenne de trois prédicteurs (a priori, a posteriori, trop sûr de lui) | ★★ | 25 | §5 | C, E | wbm | — |
| M27.6 | ✏️ | Deux lois uniformes de même largeur, translatées : JS en fonction du décalage, la KL, et ce que le décalage lui-même mesure | ★★ | 20 | §6 | C, E | wbm | — |
| M27.7 | ✏️ | Trois dépôts et trois magasins le long d'une route : vérifier des couplages, leur coût, le couplage indépendant et le plan monotone (coin nord-ouest) | ★★ | 25 | §7 | C, E | wbm | — |
| M27.8 | ✏️ | W₁ et W₂ par l'aire entre les fonctions de répartition et par les quantiles : deux lois uniformes, puis W₂ de deux gaussiennes (et W₁ quand elles ont le même écart-type) | ★★ | 25 | §8 | C, E | wbm | — |
| M27.9 | ✏️ | La distance de Fréchet de deux gaussiennes du plan à covariances diagonales, puis tournées ensemble : la part des moyennes et celle des covariances | ★★ | 20 | §9 | C, E | wbm | — |
| M27.10 | ✏️ | Une dérive en deux mois d'une variable à trois catégories : la divergence de Jeffreys (le PSI) et JS, puis l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage ; enfin KS et W₁ entre deux petits échantillons de températures de même taille | ★★ | 25 | §10 | C, E | wbm | — |
| M27.11 | ∂ | Le maximin est au plus le minimax ; ils sont égaux si et seulement si le jeu a un point selle, et deux points selles ont la même valeur | ★★ | 20 | §1 | C, E | manuel | — |
| M27.12 | ∂ | La log-loss espérée est minimale pour la probabilité a posteriori : une preuve par l'inégalité de Gibbs | ★★ | 20 | §5 | C, E | manuel | — |
| M27.13 | ∂ | 0 ≤ JS ≤ ln 2, et JS = ln 2 si et seulement si les deux lois ont des supports disjoints | ★★ | 20 | §6 | C | manuel | — |
| M27.14 | ∂ | L'appariement trié est optimal : un argument d'échange sur deux paires, puis sur n paires, pour les coûts |x − y| et (x − y)² | ★★ | 25 | §8 | C | manuel | — |
| M27.15 | ∂ | E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ : une distance estimée sur deux échantillons est biaisée vers le haut | ★★ | 20 | §9 | C, E | manuel | — |
| M27.16 | 🔗 | Pont : la distance de Fréchet en dimension 1, W₂² = (Δμ)² + (Δσ)², entre deux lois résumées par leur moyenne et leur écart-type (deux séries d'une machine, avant et après réglage) : la part de la moyenne et celle de l'écart-type, et pourquoi workbookIA 27 l'écrit avec des covariances et en rend le carré | ★ | 20 | §8 §9 | C, E | wbm | — |
| M27.17 | 📖 | MML §7.2 relu : l'inégalité minimax (7.23) et sa preuve, la dualité faible (7.27) lue comme un jeu, et l'inégalité vérifiée sur une matrice de gains choisie | ★★ | 25 | §1 | C | manuel | — |
| M27.18 | 🗣️ | Expliquer avec une partie de cache-cache pourquoi jouer au hasard peut être la meilleure stratégie, et ce que le hasard garantit | ★ | 10 | §2 | C, E | manuel | — |
| M27.E1 | 💼 | « Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se recouvrent pas, et pas Jensen-Shannon ? » | ★ | 10 | §6 §8 | C, E | manuel | — |
| M27.E2 | 💼 | « Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et comment comparer deux mesures ? » | ★ | 10 | §9 §10 | C | manuel | — |
| M27.19 | 🔨 | Les valeurs d'un jeu en stratégies pures : maximin, minimax et coups prudents, points selles compris · `pure_strategy_values` | ★ | 15 | §1 | C, E | pytest | — |
| M27.20 | 🔨 | Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle · `mixed_strategy_value_2x2` | ★★ | 20 | §2 | C, E | pytest | M27.19 |
| M27.21 | 🔨 | Les itérés de la descente-montée simultanée ou alternée sur un jeu bilinéaire xᵀAy · `descent_ascent_iterates` | ★★ | 20 | §4 | C | pytest | — |
| M27.22 | 🔨 | W₂ de deux gaussiennes en dimension 1, à partir des moyennes et des écarts-types · `w2_gaussians_1d` | ★ | 10 | §8 | C, E | pytest | — |
| M27.23 | 📦 | `scipy.optimize.linprog` : le transport optimal entre deux lois discrètes de la droite comme programme linéaire, comparé au plan monotone et à l'aire entre les fonctions de répartition | ★★ | 25 | §7 §8 | C | wbm | — |
| M27.24 | 🔮 | Prédire la trajectoire de la descente-montée simultanée puis alternée sur xy, puis la tracer : spirale qui s'éloigne ou courbe fermée ? | ★ | 15 | §4 | C | wbm | M27.21 |
| M27.25 | 🔬 | Le biais d'une distance estimée : ‖x̄₁ − x̄₂‖² entre deux échantillons d'une même loi de ℝ³, selon leurs tailles, contre tr Σ₁/n₁ + tr Σ₂/n₂ | ★★ | 20 | §9 | C | wbm | — |
| M27.26 | 🎨 | Deux fonctions de répartition sur une même figure : l'aire entre elles (W₁) et leur plus grand écart vertical (KS), pour une translation puis une dilatation | ★ | 20 | §8 §10 | C, E | manuel | — |
| M27.27 | 🐛 | Chasse à l'erreur : une stratégie d'indifférence calculée sur ses propres gains, W₂ de deux gaussiennes avec des variances, des échantillons appariés sans être triés | ★ | 25 | §2 §8 | C | wbm | — |
| M27.28 | 🛠️ | Un test de propriété : la valeur d'un jeu 2 × 2 tiré au hasard est entre maximin et minimax, et devient v + c pour G + c et k v pour k G (k > 0) | ★ | 20 | §2 | C | manuel | M27.20 |
| M27.29 | 🏆 | Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂, et cette distance, à 10⁻³ près | ★★★ | 30 | §8 | C | wbm | — |

*Notes* : Frontières : les ∂ 27.5 (D* = p_data/(p_data + p_g) par le maximum de a ln y + b ln(1 − y), dérivée nulle puis dérivée seconde, l'intégrale maximisée point par point, V(D*, G) = −ln 4 + 2 JS, son minimum en p_g = p_data) et 27.6 (les dérivées −D et −(1 − D) de ln(1 − σ(a)) et de −ln σ(a), D = 0,01 et le rapport 99, la BCE avec logits ln(1 + e^{−a})), ✏️ 27.2 (maximin, minimax et point selle d'une matrice 3 × 3 ; « min_G max_D ou max_D min_G »), ✏️ 27.3 et 27.4 (les losses BCE d'un mini-batch, ln 2 et 2 ln 2 à l'équilibre, 0,607), 🧮 27.7, 📄 27.10 (Goodfellow et coll. 2014, −log 4), 🔨 27.11 (`wasserstein_1d`), 🔨 27.22 et 📦 27.23 (`frechet_distance`, le FID et sa dépendance au nombre d'images), la dynamique d'un GAN (🔮 27.13, 📈 27.14, 🔬 27.18, 💼 27.E5), 27.Q5 (somme nulle, poker, Nash, D = 0,5 à l'équilibre), 💼 27.E1 et 27.E4 ; et, de workbookIA B7, qui n'a pas de chapitre de maths et que le §10 prépare, ✏️ B7.4 (un PSI à la main sur quatre intervalles, l'intervalle vide et ε, les seuils), 📈 B7.22, B7.Q11 et 💼 B7.E4. M27 enseigne les outils hors réseau : un marché que deux enseignes se partagent, des tirs au but, une partie de cache-cache, le dilemme du prisonnier, un jeu de coordination, un jeu d'allumettes, des dépôts et des magasins, des fournisseurs, des séries de production, des relevés de capteurs ; jamais un générateur, un discriminateur, un faux, une loss de GAN ni un learning rate. « GAN : générateur et discriminateur, le jeu mathématique » est retiré des notions du plan : M27 n'écrit ni V(D, G) ni min_G max_D. Le maximum de vraisemblance k ln p + (n − k) ln(1 − p) d'une loi de Bernoulli, avec des comptes entiers (∂ M04.12, M13a.1), et la log-loss quand la probabilité prédite tend vers 0 (M13a.4) ne sont que des rappels (🔁 M27.R1, sur d'autres nombres) ; M27.R1 ne compare jamais −ln p et ln(1 − p) ni leurs dérivées en un même point (∂ 27.6) ; le §5 enseigne l'énoncé plus général « la probabilité a posteriori P(Y = 1 | x) = π₁p₁(x)/(π₁p₁(x) + π₀p₀(x)) minimise la log-loss espérée », démontré par l'inégalité de Gibbs (∂ M27.12) et non par f′ et f″, avec des priors inégaux et des lois d'un autre domaine (fournisseurs et défauts, ✏️ M27.5) : aucun exercice ne prend des priors égaux, n'appelle ce prédicteur un discriminateur, ne maximise une intégrale de deux densités point par point, ne calcule la valeur du minimum en formule (l'entropie conditionnelle H(Y | X)) ni ne la relie à Jensen-Shannon (c'est le cœur de ∂ 27.5.4) ; M27.5 en donne seulement des valeurs numériques, et M27.Q4 ne demande ni la valeur ½ où π₁p₁ = π₀p₀, ni la limite 1 quand p₀(x) → 0 (∂ 27.5.3). La saturation (∂ 27.6) n'est pas reprise : ni ln(1 − σ(a)) contre −ln σ(a), ni le facteur σ(1 − σ) comparé à σ − y (le ∂ 18.8.4 de workbookIA l'a déjà fait), ni « même minimiseur, gradients différents » en exercice. Les jeux : ✏️ M27.1 prend d'autres matrices que 27.2 et la fiche 27, sans les noms « Ligne » et « Colonne », et une matrice avec point selle (réduite par dominance) : aucune 3 × 3 sans point selle ne fait chercher maximin et minimax (27.2) ; au-delà de 27.2, M27 enseigne les stratégies mixtes (l'indifférence d'un 2 × 2, démontrée optimale dans la fiche ; la valeur), le théorème minimax de von Neumann (énoncé) et le lien avec la programmation linéaire (énoncé, MML §7.3.1 en option) ; l'avantage de jouer en second est enseigné sur des jeux hors réseau (Q1), jamais sur min_G max_D ; Nash sur un dilemme du prisonnier et un jeu de coordination (équilibres purs et mixte), pas sur le poker ni par les questions de 27.Q5 ; l'arbre sur un jeu d'allumettes, pas sur le morpion (fiche 26, 🔬 26.37, 27.R1). La dynamique (§4) porte sur le jeu bilinéaire f(x, y) = xᵀAy et sur xy : pas simultané (des valeurs propres de module > 1) contre alterné (de déterminant 1), et deux pas différents pour x et y (des pas inégaux ne suffisent pas) ; ni GAN, ni loss, ni les learning rates de 27.14 (10⁻⁴, 10⁻³, 10⁻²), ni TTUR nommé ; M27.4 évite η = 0,25 et η = 0,5 (ηa = 0,5, l'exemple du stub). Jensen-Shannon (§6) : 0 ≤ JS ≤ ln 2 (∂ M27.13), JS = ln 2 pour des supports disjoints, sur deux lois uniformes de même largeur translatées l'une de l'autre (✏️ M27.6) ; ni D*, ni −ln 4. Wasserstein (§7, §8) : couplages et plans de transport sur des supports finis, W_p, le programme linéaire (📦 M27.23), la dualité de Kantorovich-Rubinstein énoncée ; en dimension 1, W₁ = ∫|F − G| et W_p par les quantiles (le couplage des quantiles est optimal : démontré pour deux échantillons de même taille par un argument d'échange, ∂ M27.14, admis en général), W₂ de deux gaussiennes, W_p d'une translation ; l'optimalité de l'appariement trié, que 27.11 admet, est donc démontrée, mais aucun exercice ni aucune fonction ne calcule W₁ entre deux échantillons de tailles différentes (le cœur de 27.11) ; W₁ entre deux petits échantillons de même taille, à la main, seulement au §10 (M27.10) ; W₁ de deux gaussiennes d'écarts-types différents n'est pas calculé (E|a + bZ|, la variante de 27.11). Fréchet (§9) : la formule, admise en général, Tr((Σ₁Σ₂)^{1/2}) = Σ√λᵢ, Σ₁Σ₂ semblable à Σ₁^{1/2}Σ₂Σ₁^{1/2} pour Σ₁ définie positive (démontré dans la fiche, en trois lignes), le cas commutatif démontré (une somme de W₂² en dimension 1, invariante par une rotation commune ; ✏️ M27.9 sur des covariances diagonales du plan) ; aucun code ne calcule une distance de Fréchet avec `scipy.linalg.sqrtm` ni à partir de features (le contrat et l'oracle de 27.22) ; le biais d'une distance estimée porte sur les moyennes (∂ M27.15, 🔬 M27.25 : deux séries d'une même machine), sans FID, Inception, nombre d'images ni la suite 123,2 → 119,3 de 27.23 ; le 🔗 M27.16 porte sur une convention (la distance de Fréchet en dimension 1, que workbookIA 27 écrit avec des covariances et rend au carré), jamais sur des résumés relevés epoch par epoch (🔮 27.13, 📈 27.14). Dérive (§10, pour workbookIA B7 ; workbookIA 29 mesure le décalage par la performance d'un modèle, sans distance entre lois, et sa couverture passe à M02c et M03) : PSI = KL(p ‖ q) + KL(q ‖ p) (la divergence de Jeffreys) sur une variable à trois catégories (M27.10), sans quantiles de la référence, sans intervalle vide ni ε, sans seuils 0,1 et 0,25, ni contribution d'une catégorie, ni vérification de PSI = KL + KL en exercice (B7.4 : l'identité reste dans la fiche) ; M27.10 en tire l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage, que B7 n'a pas ; KS = sup|F − G| comme statistique, sa p-valeur seulement nommée (M08), sans « tout devient significatif sur de grands échantillons » (B7.Q11 c et la fiche B7) ; W₁ = ∫|F − G|, ses unités, W₁ ≤ (b − a)·KS ; ni images, ni luminosité, ni sorties softmax. Évités (règle de partage) : les matrices [[3, −1, 2], [1, 0, 4], [−2, 5, −3]] (maximin 0, minimax 3, maxima des colonnes 3, 5 et 4) et [[2, 4], [1, 0]] (point selle 2), les territoires 5, 10 et 20 ; Glenn et Dawn, les faux billets, le faux vin, le poker ; les sorties D = 0,9 ; 0,7 ; 0,8 ; 0,6 ; 0,3 ; 0,1 ; 0,2 et 0,4, D = 0,01 et le rapport 99, D = 0,9 et le rapport 9, D = 0,5 ; ln 2, 2 ln 2 ≈ 1,386, −ln 4 et 0,607 présentés comme valeurs d'un jeu ou d'une loss ; 𝒰[0, 1] contre 𝒰[0, 2] (2/3), les mélanges 0,6 𝒩(1,5 ; 0,8) + 0,4 𝒩(−1,5 ; 0,6) et 𝒩(0,3 ; 1,6) de la figure du D*, p_data = 0,3 et p_g = 0,1 (0,75, CP6.4 de workbookIA) ; les échantillons (4, 1) et (2, 2) (W₁ = 1,5), [3, 1, 2] et [2, 6, 4] (2,0), [5, −1, 2,5] et ses permutations, [0, 2] et [1] (1,0), [0, 1, 3] et [5, 6, 8] (5,0), [0, 1] et [0, 1, 2] (0,5), (0,4 ; 1,1 ; 1,7 ; 2,9) et (1,0 ; 2,2 ; 3,1 ; 3,6), 50 normales décalées de 0,5 ; les lois 𝒩(4 ; 1,25²), 𝒩(5 ; 1,25²), 𝒩(4 ; 2,5²), le Dirac en 4 et 1,25√(2/π), 𝒩(0, 1) contre 0 et √(2/π) ≈ 0,80, 𝒩(0 ; 4) contre 𝒩(1 ; 1) (W₂² = 2 : aucune paire de gaussiennes avec (Δμ, Δσ) = (1, 1)) ; les covariances diag(9, 1) et I (4), diag(1, 4) et diag(4, 1) (2), diag(4, 9) et I avec les moyennes (1, 2) (5), les moyennes (0, 0) et (3, 4) (25), les décalages de 1 et de 2 sur chaque axe d'un nuage de ℝ³ (3 et 12), les moyennes 0 et (1, 1, 1) (3) ; les résumés (moyenne, écart-type) des 📦 27.12, 🔮 27.13 et 📈 27.14 (4,03 et 0,98 ; 5,61 à 5,64 ; 4,50 et 0,95 ; 5,72 et 0,33 ; 3,94 et 0,73 ; 2,21 et 0,90), un modèle effondré sur un point ; la gaussienne du plan de centre (5, 5) et 39,3 %, l'anneau de 8 gaussiennes de rayon 2, la somme 16(4⁹ − 1)/3 et 75 % ; les distances de Fréchet 3,4 ; 119,3 à 123,2 ; 745 ; 638 ; 91 ; 1,7 ; 15,1 et 15,3 ; 50 000 images et 2 048 features ; MNIST, Fashion-MNIST, Inception, DINOv2 ; de workbookIA B7, la luminosité moyenne d'images, les parts 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 contre 0,2 (PSI 0,135, KL 0,0650 et 0,0704), les quartiles et les comptes 38/52/54/56, 96/62/30/12 et 120/56/24/0 sur 200 images, ε = 10⁻⁴ et 10⁻³, les seuils 0,1 et 0,25, les échantillons 0,31 ; 0,42 ; 0,47 ; 0,52 ; 0,58 et 0,22 ; 0,29 ; 0,35 ; 0,44 ; 0,61 (D = 0,4, p = 0,87), 10 000 valeurs décalées de 0,05 écart-type (D = 0,024, p = 0,008), 200 valeurs (D = 0,08, p = 0,55), 50 000 requêtes et p = 0,001, Bonferroni 0,05/m ; du checkpoint VI de workbookIA, la dérivation de D* (CP6.4) et la courbe d'un GAN 1D (lr 10⁻² et 10⁻⁵, CP6.7). Conventions : G[i, j] est le gain de la ligne (qui maximise) et ce que paie la colonne ; logarithme népérien, JS en nats (M06 la calculait en bits : 1 bit = ln 2 nats, et JS ≤ 1 bit) ; W_p désigne la distance et W_p^p le coût minimal ; F(x) = P(X ≤ x), F⁻¹(u) = inf{x : F(x) ≥ u} (M02a) ; `w2_gaussians_1d` prend des écarts-types. `distances` : NumPy et `math` permis, rien de `np.linalg` et aucune fonction de SciPy (`scipy.optimize.linprog` résout un jeu) ; `pure_strategy_values` (au lieu de `minimax_value` du plan : une valeur seule ne dit pas le coup, et le minimax d'un arbre est une autre chose) rend (maximin, minimax, ligne, colonne), les plus petits indices en cas d'égalité ; `mixed_strategy_value_2x2` rend les stratégies pures de `pure_strategy_values` quand il y a un point selle, sinon celles d'indifférence ; `descent_ascent_iterates` (ajoutée au plan : la brique du §4, calquée sur `richardson_iterates` ; son premier joueur minimise, comme dans MML (7.23), et sa docstring dit comment partir d'une matrice de gains G : A = −G, ou A = Gᵀ) ; `w2_gaussians_1d` prend des écarts-types et rend W₂, pas son carré : un contrat distinct du cas 1D de `frechet_distance` de workbookIA 27 (des covariances, et le carré d²) ; aucune fonction de W₁ empirique (27.11), de distance de Fréchet en dimension d (27.22), de KL, de JS (`mylearn` 6), de PSI ni de KS (B7.22 les écrit ou les appelle). Les exercices ne reprennent pas les exemples du stub ([[7, −4, 1], [−1, 5, 6]], [[1, 6, 2], [4, 5, 4], [0, 8, 3]], [[4, −2], [−1, 3]], [[−1, 2], [5, 6]], A = [[2]] avec η = 0,25, (10 ; 1 ; 2 ; 16) et (−1 ; 0,5 ; −1 ; 3,5)). MML : §7.2 relu (📖 M27.17 : l'inégalité minimax (7.23), sa preuve par (7.24), la dualité faible (7.27) lue comme un jeu où le joueur des multiplicateurs annonce en second ; M13b.21 l'a lu une première fois pour Lagrange) ; §7.3.1 (programmation linéaire) en option ; MML n'a ni stratégie mixte, ni Nash, ni Wasserstein. Référence libre possible, à vérifier en génération avant de la citer (annexes/ressources.md) : G. Peyré et M. Cuturi, Computational Optimal Transport, ch. 2 et 3. 14,4 h au lieu des 10 h prévues : la décision commune ajoute au plan les stratégies mixtes et von Neumann, les couplages et W_p, l'appariement trié, le biais d'une distance estimée, la dynamique d'un jeu bilinéaire et le § de la dérive (B7) ; la composition est au bas des fourchettes du §13 (15 ✏️/∂, 5 🔨/📦, un seul 🔬 et un seul 🔮) et les durées suivent les recalages de M21 et M22.

<a id="m28"></a>
## M28 · Matrice de Gram, montée sur l'entrée et lois tronquées

**Partie** VI · **prépare** workbookIA 28 · **dossier** `chapitres/m28_gram_echantillonnage/` · **MML** — · **sessions de génération** 1

La matrice de Gram d'une famille de vecteurs, lue dans les deux sens (XXᵀ et XᵀX), divisée par le nombre d'échantillons pour devenir une matrice de moments d'ordre 2, et ce qu'elle coûte ; ce qu'elle détermine : toutes les longueurs et tous les angles, donc les distances, et la configuration à une isométrie près (double centrage, positions retrouvées à partir de distances) ; optimiser l'entrée d'une fonction à paramètres fixés : montée de gradient, pas normalisé, projection sur un pavé, coordonnées gelées, et ce que la montée trouve (un sommet du pavé, un vecteur propre) ; la variation totale d'une grille, forme quadratique d'un laplacien, son gradient et le lissage qu'elle produit, et les fréquences spatiales (période d'un motif, fréquence de Nyquist, gain d'un flou) ; les lois catégorielles modifiées : température sur des probabilités, top-k et top-p comme lois conditionnelles, le plus petit ensemble de masse donnée et le coût d'une troncature ; enfin une itération déterministe sur un ensemble fini, qui finit toujours par boucler. workbookIA 28 applique ces outils à la visualisation des réseaux, au transfert de style et à la génération de texte.

**Temps** : 9,8 h en parcours complet, 7,7 h en parcours essentiel (lecture 100 min, 16 flashcards).

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

**Prérequis** : division euclidienne et reste (`//`, `%`) (R0) · cosinus, radians, périodicité (R9) · loi catégorielle, tirage catégoriel par inversion (M02b) · loi conditionnelle (M03) · convexité d'une fonction d'une variable, log-sum-exp (M05a) · gradient, montée et descente (M05b) · entropie, divergence KL, KL infinie quand le support manque (M06) · produit scalaire, normes, Cauchy-Schwarz, similarité cosinus (M07) · transposée, XᵀX et XXᵀ (M09a) · ridge : un terme de régularisation pondéré (M09b) · fonctions convexes de plusieurs variables (M10) · bases orthonormées, matrices orthogonales, Gram-Schmidt, projection sur un sous-espace (M12b) · théorème spectral, quotient de Rayleigh, méthode de la puissance, matrices semi-définies positives, matrice de Gram XᵀX (M12c) · valeurs singulières, AᵀA et AAᵀ, approximation de rang faible, ACP quand n < p (M12d) · noyau polynomial et matrice de Gram d'un noyau (M13b) · principe des tiroirs (M16) · loi de Boltzmann et ses limites en température (M17) · gradient par rapport à toutes les entrées en un passage inverse (M18) · projection sur une boule et sur un pavé, pas critique 2/λmax (M19) · matrice de centrage (M20) · laplacien discret, moyenne mobile, convolutions circulaires, forme linéaire sur une boule (M21)

**mymath** : `sampling.py` (signatures figées) : `points_from_gram`, `temper`, `smallest_mass_set`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 28.3 ∂ Mélanger les positions ne change pas la matrice de Gram · 28.5 ∂ Le gradient de la loss de style · 28.2 ✏️ Une matrice de Gram à la main · 28.4 ✏️ Losses de contenu, de style et de variation totale sur un mini-exemple · 28.7 🧮 Vocabulaire de mots et taille de la couche de sortie d'un LSTM · 28.8 🗣️ Pourquoi la matrice de Gram capture le style, en cinq lignes · 28.10 📄 Lire Gatys, Ecker et Bethge (2015), « A Neural Algorithm of Artistic Style » · 28.12 🔮 Prédire l'image qui excite un filtre précoce, puis un filtre profond · 28.13 📦 Visualiser un filtre d'un réseau ImageNet : la montée de gradient du ch. 21 passe à l'échelle · 28.15 🔬 Régulariser la visualisation : décalages, flou, octaves · 28.16 📦 Deep dream sur une photo libre · 28.17 🔬 Choisir couches et poids, ne rêver que dans une zone · 28.18 📦 La matrice de Gram en PyTorch, vérifiée contre NumPy · 28.24 🔬 Poids contenu/style, variation totale et image de départ · 28.25 🔬 Au-delà de Gram : moyennes et écarts-types des canaux · 28.28 🔬 Glouton, température, top-k ou top-p : répétitions et diversité · 28.Q2 🧠 Montée de gradient sur l'entrée, poids gelés · 28.Q7 🧠 Ce que la matrice de Gram retient et ce qu'elle oublie · 28.Q10 🧠 Générer du texte mot à mot : ce qu'implique « le mot le plus probable » · 28.R2 🔁 Mélange de contenu contre mélange de représentations · 28.E2 💼 Expliquer le transfert de style neuronal et la matrice de Gram · 28.E3 💼 Quelles stratégies de décodage pour générer du texte ? · B4.Q5 🧠 Glouton, température, top-p : lequel pour extraire une date, lequel pour écrire un poème ? · B4.13 🔮 Prédire : dix générations du même prompt à température 0, 0,7 et 1,5

| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |
|---|---|---|---|---|---|---|---|---|
| M28.Q1 | 🧠 | Matrice de Gram : XXᵀ ou XᵀX, laquelle former, sa diagonale, et les distances qu'on y lit | ★ | 4 | §1 §2 | C, E | manuel | — |
| M28.Q2 | 🧠 | Monter sur l'entrée : pas normalisé, projection sur un pavé, coordonnées gelées, point d'arrivée | ★ | 4 | §3 | C, E | manuel | — |
| M28.Q3 | 🧠 | Variation totale et fréquences spatiales : quel motif coûte le plus, lequel traverse un flou ? | ★ | 4 | §4 | C, E | manuel | — |
| M28.Q4 | 🧠 | Température, top-k et top-p : ce qui change l'ensemble gardé, ce qui ne change que les probabilités | ★ | 4 | §5 | C, E | manuel | — |
| M28.Q5 | 🧠 | Une itération sur un ensemble fini : prépériode, période, et ce qui empêche de boucler | ★ | 4 | §6 | C, E | manuel | — |
| M28.R1 | 🔁 | Le quotient de Rayleigh et la méthode de la puissance (M12c) | ★ | 5 | §3 | C, E | manuel | — |
| M28.R2 | 🔁 | Le laplacien discret et la moyenne mobile d'un signal (M21) | ★ | 5 | §4 | C, E | manuel | — |
| M28.R3 | 🔁 | La loi de Boltzmann et ses limites en température (M17) | ★ | 5 | §5 | C, E | manuel | — |
| M28.1 | ✏️ | Quatre points du plan : leur matrice de Gram 4 × 4, leur matrice des moments d'ordre 2, et les distances lues dans la Gram | ★★ | 20 | §1 | C, E | wbm | — |
| M28.2 | ✏️ | Quatre villes aux sommets d'un losange : le double centrage des carrés des distances, puis une carte à une isométrie près | ★★ | 25 | §2 | C, E | wbm | — |
| M28.3 | ✏️ | Régler quatre émetteurs entre 0 et 1 : le maximum d'une réponse linéaire sur la boule et sur le pavé, d'une énergie quadratique sur la sphère, et deux pas de montée projetée | ★★ | 25 | §3 | C, E | wbm | — |
| M28.4 | ✏️ | Les températures le long d'une barre : la variation totale xᵀLx, son gradient 2Lx, un pas de lissage, et une marche étalée sur n pas, au carré ou en valeur absolue | ★★ | 25 | §4 | C, E | wbm | — |
| M28.5 | ✏️ | Des étoffes rayées : période, fréquence, fréquence de Nyquist, repliement, variation totale rapportée à l'énergie 4 sin²(ω/2), et gain d'une moyenne mobile | ★★ | 25 | §4 | C, E | wbm | — |
| M28.6 | ✏️ | La prévision d'un météorologue en six catégories : la refroidir, garder les deux plus probables, garder le plus petit ensemble de masse donnée, et le coût de chaque troncature | ★★ | 25 | §5 | C, E | wbm | — |
| M28.7 | ✏️ | Les décimales de a/n et l'itération x ↦ x² + c modulo n : prépériode et période à la main, et la borne du principe des tiroirs | ★ | 15 | §6 | C, E | wbm | — |
| M28.8 | ∂ | Deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie | ★★★ | 30 | §2 | C | manuel | — |
| M28.9 | ∂ | Le maximum d'une fonction convexe sur un pavé est atteint en un sommet | ★★ | 15 | §3 | C | manuel | — |
| M28.10 | ∂ | Le plus petit ensemble de masse au moins p est fait des issues les plus probables, et la loi tronquée est à −ln P(S) de la loi de départ en divergence KL | ★★ | 25 | §5 | C, E | manuel | — |
| M28.11 | 🔗 | Pont : diviser des scores par T avant la softmax, ou élever les probabilités à la puissance 1/T, la même loi ; et le même top-k | ★ | 15 | §5 | C, E | wbm | — |
| M28.12 | 🗣️ | Expliquer avec une structure de barres rigides ce que la matrice de Gram d'une famille de vecteurs fixe, et ce qu'elle laisse libre | ★ | 10 | §2 | C, E | manuel | — |
| M28.E1 | 💼 | « Que perd-on, en divergence KL, à ne garder que les issues les plus probables d'une loi avant de tirer ? » | ★ | 10 | §5 | C | manuel | — |
| M28.13 | 🔨 | Une configuration de points de matrice de Gram donnée, par le théorème spectral · `points_from_gram` | ★★ | 25 | §2 | C | pytest | — |
| M28.14 | 🔨 | Tempérer une loi donnée par ses probabilités, et le plus petit ensemble de masse donnée · `temper, smallest_mass_set` | ★★ | 30 | §5 | C, E | pytest | — |
| M28.15 | 🔮 | Prédire ce que deviennent un pas η∇f et un pas normalisé quand la fonction est multipliée par 1 000, puis vérifier | ★ | 15 | §3 | C, E | wbm | — |
| M28.16 | 🎨 | Des motifs rayés de fréquence croissante jusqu'au damier : leur variation totale, et ce qu'en laissent un flou 3 × 3 et dix pas de descente sur la variation totale | ★ | 20 | §4 | C, E | manuel | — |
| M28.17 | 🐛 | Chasse à l'erreur : un double centrage fait sur les distances au lieu de leurs carrés, une montée qui coupe le gradient au lieu du point, une prépériode comptée dans la période | ★ | 20 | §2 §3 §6 | C, E | wbm | — |
| M28.18 | 🛠️ | Un test de propriété : la configuration rendue redonne la matrice de Gram et les distances, pour des points tirés au hasard | ★ | 15 | §2 | C | manuel | M28.13 |
| M28.19 | 🏆 | Défi : redessiner la carte de 30 villes quand un quart des distances manquent, à moins de 1 km en moyenne après alignement | ★★★ | 30 | §2 | C | wbm | M28.13 |

*Notes* : Frontières : les ∂ 28.3 (une permutation des positions, puis une matrice orthogonale, ne change pas FFᵀ ; un seul canal permuté la change ; C G_ii = μ² + σ² et la moyenne qu'elle ne fixe pas ; les tables d'ordre 3) et 28.5 (le gradient 4(FFᵀ − S)F de la loss de style), ✏️ 28.2 (une Gram 3 × 4 normalisée par CHW, cosinus, somme, retournement), ✏️ 28.4 (losses de contenu, de style et de variation totale sur un mini-exemple, `mse_loss`, poids α, β et λ), 🧮 28.7 (LSTM mot à mot, Zipf, perplexité), 🗣️ 28.8, 📄 28.10 (Gatys), 🔮 28.12 et 🔬 28.15 (périodes de filtres appris, part des hautes fréquences, flou, décalages, octaves), 📦 28.13 (pixels saturés d'une visualisation), 📦 28.16 (le deep dream : un gradient normalisé, indépendant de l'échelle des activations), 🔬 28.17 (couches, poids, un masque de zone), 📦 28.18 (Gram et variation totale en PyTorch contre `einsum` et `np.diff`), 🔬 28.24 (poids contenu/style et leur frontière), 🔬 28.25 (moyennes et écarts-types des canaux), 🔬 28.28 (glouton, température, top-k et top-p sur Verne, `pick_28`, répétitions), les quiz 28.Q2, 28.Q7 et 28.Q10, le rappel 28.R2, les entretiens 28.E2 et 28.E3, et, de workbookIA B4 (après M28), B4.Q5 et B4.13 (quelle stratégie de décodage pour quelle tâche ; dix générations à trois températures). M28 enseigne les outils hors réseau : nuages de points, villes et capteurs pour la matrice de Gram ; émetteurs réglables, énergies quadratiques et modes de vibration pour la montée ; barres chauffées, plaques, étoffes rayées et signaux échantillonnés pour la variation totale et les fréquences ; prévisions météorologiques, diagnostics et identifications d'espèces pour les lois tronquées ; décimales d'une fraction, itérations modulo n et automates pour les boucles ; jamais une carte d'activation, un filtre appris, une image d'un dataset, un pixel permuté, un « style », un logit de mot ni un texte généré. La matrice de Gram : les points sont les lignes de X (comme M13b) et G = XXᵀ ; la normalisation est celle d'une matrice de moments, 1/N pour N échantillons, jamais 1/(CHW) ni une forme (C, H, W) ; la double lecture XXᵀ/XᵀX, la symétrie et la positivité sont des rappels (M09a, M12c.17, M12d.12, M13b), et aucune fonction ne calcule une Gram (c'est `polynomial_kernel(X, X, 1, 0)` de M13b, et `gram_matrix_18` de 28.18). L'invariance par une transformation orthogonale de l'espace (X ↦ XRᵀ, tourner le repère) est énoncée en une ligne et utilisée ; la réciproque est démontrée (∂ M28.8 : une application linéaire définie sur l'espace engendré par les points, isométrique, prolongée par Gram-Schmidt), avec la construction par le théorème spectral (🔨 M28.13) ; aucun exercice ne permute les colonnes de X (positions ou échantillons), ne demande si permuter une seule ligne change G, ni ne relie la diagonale à μ² + σ² ou à une moyenne qu'elle ne fixe pas (∂ 28.3.4-5), et M28.Q1 lit la diagonale comme les carrés des normes des points, jamais comme une moyenne de carrés (28.Q7 d) ; pas de statistiques d'ordre 3 ; l'écart de Frobenius entre les matrices de moments de deux nuages, égal à une MMD de noyau (xᵀy)² (M13b), est au plus une remarque de la fiche, sans loss ni « style ». Aucun gradient d'une fonction de XXᵀ ou de XᵀX (ni ‖XXᵀ − S‖²_F, ni ‖XᵀX − I‖², paraphrase transposée de ∂ 28.5) : le seul gradient matriciel du chapitre est celui de la variation totale, 2Lx. Le double centrage est −½ J D⁽²⁾ J sur les **carrés** des distances, avec la matrice de centrage J de M20 ; ✏️ M28.2 prend quatre villes aux sommets d'un losange (une matrice de Gram à blocs, diagonalisable à la main), et ✏️ M28.3 une énergie quadratique de matrice à blocs 2 × 2 en dimension 4, diagonalisable à la main : les deux tiennent ainsi en 25 minutes. La montée sur l'entrée : f(x ; θ) à θ fixé, sur des fonctions écrites (réponses linéaires et quadratiques d'émetteurs réglables entre 0 et 1, énergies) ; le pas normalisé et son invariance quand f est multipliée par c > 0 sont démontrés en général, sans deep dream, octaves, masque d'image ni « activation » ; la montée projetée est celle de M19 §8 (`np.clip`) ; un gradient restreint à des coordonnées libres est la projection orthogonale de M12b, sans zone d'image (28.17) ; le maximum d'une fonction convexe sur un pavé (un sommet, ∂ M28.9) explique les coordonnées saturées, sans les pourcentages de pixels de 28.13 ; une moyenne de carrés de réponses linéaires est la forme quadratique xᵀAx avec A = WᵀW/m, et la montée renormalisée sur elle est la méthode de la puissance de I + 2ηA (le gradient vaut 2Ax) (M12c) ; aucun vrai ou faux « monter sur f, c'est descendre sur −f » ni « les paramètres sont gelés, le gradient par rapport à l'entrée existe quand même » (28.Q2 b et e). La variation totale : sur une grille de mesures (somme des carrés des différences entre voisins horizontaux et verticaux, comme workbookIA) et sur un signal, écrite xᵀLx avec le laplacien de la grille ((Lx)_ij = 4x_ij − la somme des voisins à l'intérieur : le pochoir de M21 au signe près), de gradient 2Lx ; un pas de descente est un pas de diffusion, de pas critique 1/λmax(L) (M19) ; la valeur absolue (variation totale de Rudin, Osher et Fatemi, nommée sans date) garde les bords, le carré préfère les rampes (h²/n contre h pour une marche étalée sur n pas) ; jamais la grille 3 × 3 de 28.4, une puissance 1,25, une image de scikit-learn ni une loss totale pondérée ; débruiter un signal par min ‖x − y‖² + λxᵀLx, soit (I + λL)x = y, est une remarque (gain 1/(1 + 4λ sin²(ω/2)) par fréquence, un compromis réglé par λ comme la ridge de M09b), sans courbe contenu/style. Les fréquences spatiales comblent une lacune (ni M21 ni R9 ne les enseignent ; workbookIA 28 s'en sert dans ses outils fournis et en 28.12, 28.14, 28.15 et 28.24) : un motif cos(2π(f₁i + f₂j) + φ), sa fréquence en cycles par case, sa période 1/√(f₁² + f₂²) dans la direction (f₁, f₂), la fréquence de Nyquist ½ (le damier) et le repliement (f et 1 − f donnent les mêmes échantillons) ; un motif périodique est un vecteur propre du laplacien circulaire (∂ M21.13 : les matrices circulantes), de valeur propre 4 sin²(ω/2) en dimension 1 (ω = 2πf) et la somme des deux en dimension 2, d'où sa variation totale rapportée à son énergie, un quotient de Rayleigh (M12c), maximale pour le damier ; la moyenne mobile de trois cases multiplie un motif par (1 + 2 cos ω)/3 et efface la période 3 ; sans transformée de Fourier discrète (un encadré 💻 au plus), sans « part de la variance au-dessus de la moitié de la fréquence de Nyquist » ni période dominante d'une image (les outils `high_freq_share` et `dominant_period` du notebook de workbookIA 28). Les lois catégorielles : données par leurs probabilités, jamais par des logits de mots ; la température sur des probabilités est la loi de Boltzmann des énergies −ln pᵢ (M17), les issues de probabilité nulle le restent ; le 🔗 M28.11 montre que diviser des scores par T avant la softmax donne la même loi, sur les scores d'un classifieur d'espèces (ni mots ni vocabulaire), sans refaire 17.6, 22.5 ni 26.5 ; la croissance de l'entropie avec T (dH/dT = Var(E)/T³) est énoncée et constatée, sa démonstration est l'un des sujets de CP6.8 ; top-k et top-p sont des lois conditionnelles (M03) sur l'ensemble gardé, le top-p étant le plus petit ensemble de masse au moins p (∂ M28.10 : un argument d'échange, puis KL(p_S ‖ p) = −ln P(S) et ½‖p_S − p‖₁ = 1 − P(S)) ; la température ne change pas l'ensemble du top-k (elle garde l'ordre) et, en refroidissant, la masse des j issues les plus probables croît, donc l'ensemble du top-p rétrécit ; un encadré ⚠️ distingue la variation totale d'une grille et la « distance en variation totale » ½‖p − q‖₁ entre deux lois ; le tirage lui-même est un rappel de M02b. Les boucles : une suite u_{t+1} = f(u_t) sur un ensemble de N éléments devient périodique, avec μ + λ ≤ N (principe des tiroirs de M16), démontré dans la fiche et appliqué aux décimales de a/n et à x ↦ x² + c modulo n (✏️ M28.7) ; un générateur glouton dont l'état est fait des w derniers symboles d'un alphabet de V symboles a au plus V^w états : il boucle ; un modèle à état continu (une cellule récurrente) n'entre pas dans le théorème, et la fiche le dit ; l'algorithme du lièvre et de la tortue (Floyd) est un encadré 💻, sans fonction `mymath` ; ni phrase générée, ni « de la de la », ni part de trigrammes répétés (28.28). Le 🐛 M28.17 n'a aucune des erreurs du corrigé de 28.28 (renormaliser avant de couper, trier dans le mauvais sens, un mot de moins que le seuil) ni de 28.21 (normalisation oubliée, Gram non normalisée, optimiseur sur les poids, bornes de `clamp_`). Évités (règle de partage) : les matrices F = [[3, 1], [0, 2]] (Gram [[2,5 ; 0,5], [0,5 ; 1]]), [[1, 0, 2, 1], [0, 3, 1, 1], [2, 0, 4, 2]] (FFᵀ [[6, 3, 12], [3, 11, 6], [12, 6, 24]], 0,917, 6,917, 0,369), [[2, 0, 1, 1], [1, 1, 0, 2]] (0,75 ; 0,5 ; 0,667), [[1, 0], [1, 0]] et [[1, 0], [0, 1]], [[1, 1], [0, 2]], [[2, 0], [0, 2]], [[1, 0], [1, 1]], et, du checkpoint VI, [[1, 0, 2, 1], [0, 1, 1, 0], [2, 1, 0, 1]] ([[6, 2, 3], [2, 2, 1], [3, 1, 6]]) ; les canaux (1, 1) et (0, √2) ; les vecteurs (1, 2, 0, 1), (1, 0, 1, 1) et (0, 1, 1, 1) ; la grille [[0, 1, 0], [1, 1, 1], [0, 1, 3]] et ses variations totales 14 et 10 ; α = 0,025, β = 1, λ = 10⁻⁴, 40, 0,8764, 12, 0,9375 (28.4) ; CHW = 401 408 et 1,6 × 10¹¹, 10,90, 512³ et 134 millions ; les tailles de VGG16 (3 211 264, 401 408, 262 144, 784, 131 328) et ses 224, 28 et 14 pixels, SqueezeNet ; 15,5 et 0,35 milliard de MAC, 138,4 M, 14,7 M, 123,6 M, 553 Mo ; la loi (0,5 ; 0,2 ; 0,15 ; 0,1 ; 0,05) avec p = 0,8, son cumul 0,85 et (0,588 ; 0,235 ; 0,176) ; les logits (2 ; 1 ; 0,5 ; 3 ; −1) et leur softmax, (3,1 ; 2,6 ; 2,2 ; 1,6 ; 1,5 ; 1,1 ; 0,8 ; 0,5 ; 0,2 ; −0,3), (1, 2, 3), (1, 5, 2), (3 ; 1 ; 0,5) de 22.5 et les scores 0,6 / 0,3 / 0,1 de 17.Q12 ; les seuils de top-p 0,75, 0,8, 0,9 et 0,01, les k = 1, 2 et 20, les températures 0,5 ; 0,7 ; 1,2 ; 1,5 et 2 (les ✏️ prennent T = 1/3, 1/4, 3 ou 4, des puissances exactes), 6 000 tirages et la tolérance 0,03 ; (1, 2, 3, 1, 2, 3, 1) et 0,4 ; 10 300 mots, 427 000 mots, 2 × 128 cellules, les perplexités 150, 439 et 113, la formule de Zipf ; la moyenne (0,485 ; 0,456 ; 0,406) et l'écart-type (0,229 ; 0,224 ; 0,225) d'ImageNet ; les filtres 5, 17 et 100, les périodes de 2, 4, 8, 13 et 16 pixels, les parts de hautes fréquences (0,75 pour un bruit blanc ; 71, 76, 83 et 91 %), les pixels saturés (≈ 50 %, 37 à 45 %, 98 %) ; l'interpolation de (0, 2) et (4, −2) à t = 0,25 ; Verne, Holmes, « Phileas Fogg », « le capitaine… », « de la de la », la grenouille, la pagode, la fleur, les images `china` et `flower`, les tableaux et leurs peintres ; et, de ce dépôt, la loi (0,1 ; 0,4 ; 0,35 ; 0,15) de M02b, les trois niveaux (0 ; 0,5 ; 2) et p = (0,5 ; 0,3 ; 0,2) de M17 ; la fiche ne reprend ni le losange de ✏️ M28.2 ni les exemples du stub. Conventions : points en lignes de X ; ω = 2πf en radians par case ; la variation totale est la somme des carrés (comme workbookIA), la version en valeur absolue est nommée chaque fois ; une loi est un vecteur de probabilités ; indices à partir de 0 ; entre deux probabilités égales, le plus petit indice d'abord (un tri stable). `sampling` : NumPy permis, de `np.linalg` seulement `eigh` (dans `points_from_gram`), aucune fonction de SciPy (`scipy.special.softmax` et `logsumexp` donneraient `temper`) ni de scikit-learn ; les fonctions prennent des probabilités (jamais des logits) et ne tirent rien : `temper` (T = 0 et T = ∞ compris, zéros gardés) a un autre contrat que `temperature_softmax` (logits, T > 0) de workbookIA 22, `smallest_mass_set` rend un ensemble d'indices, pas un tirage ni une loi prête à tirer (`sample_from_logits` de workbookIA 22, `pick_28` de 28.28, `sample_categorical` de workbookIA 2) ; la docstring ne donne ni la tranche du top-k ni la renormalisation suivie d'un tirage (l'indice 3 de 28.28), et aucun exercice ni la fiche ne les écrivent en code ; `smallest_mass_set` rend exactement l'ensemble que garde la branche top-p de `pick_28` (à 1e-9 près) : c'est la brique mathématique (∂ M28.10), assumée ; aucune fonction de matrice de Gram, de loss de style, de variation totale (`gram_matrix_18`, `tv_loss_18`) ni de période. Pas de MML : le livre ne traite ni la variation totale, ni les fréquences, ni les troncatures, ni les itérations sur un ensemble fini, et AAᵀ, AᵀA et la matrice de Gram d'un noyau ont été lus en M12d (§4.5) et M13b (§12.4) ; donc pas de 📖. COMPOSITION : prévu court (6 h au plan, 8 h visées en session 60), porté à 9,8 h par la lacune des fréquences spatiales, la réciproque de la matrice de Gram et des durées réalistes (relectures de M21 et M22) : la composition d'un chapitre court est gardée (5 quiz, 7 ✏️ et 3 ∂, 2 🔨, un 🔮 et un 🎨 sans 🔬, 16 flashcards). Parcours essentiel : les ∂ de la Gram et de la montée (M28.8, M28.9), le 💼, le 🔨 de la Gram, son 🛠️ et le 🏆 hors parcours ; ∂ M28.10 (le top-p) y est.

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

Des cooccurrences aux embeddings : l'information mutuelle ponctuelle (PMI), la SVD tronquée d'une matrice, la géométrie des analogies, le modèle logistique de word2vec, et les embeddings de phrases par moyenne et cosinus.

**Durée estimée** : ≈ 8 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : information mutuelle ponctuelle (PMI, PPMI) · SVD tronquée d'une matrice de cooccurrences · géométrie des analogies · word2vec : un modèle logistique · recherche par similarité · un embedding est un produit one-hot × matrice (rappel M09a) · embedding de phrase : moyenne et cosinus

**Après** : M12d, M06, M13a, M09a

**mymath** : `cooccurrence.py` (fonctions prévues) : `pmi`, `truncated_svd_embeddings`, `analogy`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B2.7 ∂ Skip-gram avec échantillonnage négatif : gradients par rapport au mot et au contexte

*Notes* : Frontière : les gradients du skip-gram avec échantillonnage négatif (workbookIA B2.7) ; la matrice de cooccurrences et la PPMI sont les fonctions de `mylearn`.

<a id="mb3"></a>
## MB3 · Rotations et attention

**Partie** VII · **prépare** workbookIA B3 · **dossier** `chapitres/mb3_rotations_attention/` · **MML** §3.9 · **sessions de génération** 1

Les formules trigonométriques et les rotations du plan, les nombres complexes comme rotations (rappel de M22), les encodages sinusoïdaux, la variance d'une somme de produits (rappel de M16), l'attention comme moyenne pondérée, les masques, le coût quadratique et la softmax en ligne.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : formules trigonométriques · rotations du plan, R(a)R(b) = R(a + b) · nombres complexes comme rotations (rappel) · encodages de position sinusoïdaux · variance d'une somme de produits indépendants (rappel) · l'attention comme moyenne pondérée · attention multi-têtes (projections) · coût quadratique · masques causal et de padding : −∞ avant la softmax · softmax en ligne (online softmax, principe de FlashAttention)

**Après** : R9, M16, M17, M02c, M12a, M22

**mymath** : `positional.py` (fonctions prévues) : `rotation_matrix_2d`, `rotate_complex`, `online_softmax`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B3.6 ∂ Pourquoi √d_k : variance du produit scalaire de deux vecteurs aléatoires · B3.7 ∂ RoPE : la rotation rend q_m · k_n fonction de m − n seulement

*Notes* : Frontières : pourquoi √d_k et la propriété relative de RoPE (workbookIA B3.6, B3.7) ; l'attention, les encodages et RoPE sont les fonctions de `mylearn`.

<a id="mb4"></a>
## MB4 · Rang faible et recherche d'information

**Partie** VII · **prépare** workbookIA B4 · **dossier** `chapitres/mb4_rang_faible/` · **MML** (§4.6) · **sessions de génération** 1

Le rang d'un produit et le nombre de paramètres d'une adaptation de rang faible, la pondération IDF et la formule de BM25, la recherche dense et hybride, et les métriques de recherche.

**Durée estimée** : ≈ 6 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : rang d'un produit de matrices (rappel M12a) · nombre de paramètres d'une mise à jour de rang faible · IDF et BM25 : la formule · recherche dense et hybride · recall@k et MRR (définitions)

**Après** : M12d, M07

**mymath** : `retrieval.py` (fonctions prévues) : `lora_param_count`, `idf`, `bm25_term_score`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B4.6 ∂ LoRA : ΔW = BA de rang au plus r, B nulle au départ, gradients de A et de B, facteur α/r

*Notes* : Frontière : LoRA, son rang, son initialisation et ses gradients (workbookIA B4.6) ; recall@k et MRR sont les fonctions de `mylearn`.

<a id="mb5"></a>
## MB5 · Les maths de la diffusion

**Partie** VII · **prépare** workbookIA B5 · **dossier** `chapitres/mb5_diffusion/` · **MML** (§6.5) · **sessions de génération** 1

Les outils de la diffusion : sommes de gaussiennes indépendantes, produit de deux densités gaussiennes, produits cumulés de coefficients, rapport signal sur bruit, l'ELBO d'une chaîne de variables latentes, puis les équations différentielles et la méthode d'Euler (flow matching).

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : sommes de gaussiennes indépendantes (rappel de M25a) · produit de deux densités gaussiennes en dimension 1 (rappel de M25a) · produits cumulés et plannings de bruit (linéaire, cosinus) · rapport signal sur bruit · ELBO d'une chaîne de variables latentes (principe) · loss de prédiction du bruit (idée) · DDPM et DDIM : ce qui change mathématiquement · guidance sans classifieur (combinaison affine) · équations différentielles, méthode d'Euler (premier contact en M20 §6) · flow matching (initiation)

**Après** : M25a, M25b, M26

**mymath** : `diffusion.py` (fonctions prévues) : `cumulative_alpha`, `combine_gaussians`, `gaussian_product_1d`, `euler_ode`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B5.6 ∂ Forme fermée : deux pas de bruit gaussien n'en font qu'un, d'où q(x_t | x_0) · B5.7 ∂ Moyenne et variance du posterior q(x_{t−1} | x_t, x_0) en dimension 1

*Notes* : Coût : 14 h au lieu de 12. Frontières : la forme fermée de q(x_t | x_0) et le posterior q(x_{t−1} | x_t, x_0) (workbookIA B5.6, B5.7) ; les plannings et les pas de `mylearn`.

<a id="mb6"></a>
## MB6 · Shapley, intégrales de chemin et équité

**Partie** VII · **prépare** workbookIA B6 · **dossier** `chapitres/mb6_shapley_equite/` · **MML** — · **sessions de génération** 1

Les valeurs de Shapley (combinatoire des coalitions et axiomes), la dépendance partielle et ICE, une intégrale le long d'un chemin (gradients intégrés), Grad-CAM, et les définitions des indicateurs d'équité par groupe.

**Durée estimée** : ≈ 8 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : valeurs de Shapley : poids des coalitions et axiomes · dépendance partielle et ICE (espérances) · intégrale le long d'un chemin (gradients intégrés) · Grad-CAM (gradients moyennés) · indicateurs d'équité par groupe : taux de base, calibration, taux d'erreur (définitions)

**Après** : R8, M02a, M18, M03

**mymath** : `attribution.py` (fonctions prévues) : `coalition_weights`, `partial_dependence`, `path_integral`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B6.2 ∂ Modèle linéaire et fond indépendant : φ_i = w_i (x_i − E[x_i]) · B6.6 ∂ Impossibilité : taux de base différents, calibration et égalité des erreurs incompatibles

*Notes* : Frontières : Shapley d'un modèle linéaire et le théorème d'impossibilité (workbookIA B6.2, B6.6) ; Shapley, gradients intégrés et taux par groupe sont les fonctions de `mylearn`.

<a id="mb8"></a>
## MB8 · Gradient de politique

**Partie** VII · **prépare** workbookIA B8 · **dossier** `chapitres/mb8_gradient_politique/` · **MML** — · **sessions de génération** 1

La fonction score d'une loi et son espérance nulle, la réduction de variance par une variable de contrôle, l'échantillonnage d'importance, le modèle de Bradley-Terry, la pénalité KL et l'avantage relatif à un groupe : les outils statistiques de RLHF, DPO et GRPO.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : fonction score d'une loi (statistique), espérance nulle · variable de contrôle et réduction de variance · échantillonnage d'importance, ratio · clipping d'un ratio (idée) · modèle de Bradley-Terry · pénalité KL (RLHF, DPO) · GRPO : avantage relatif à un groupe · retours actualisés et GAE (rappel M26)

**Après** : M04, M18, M26, M06

**mymath** : `policy_gradient.py` (fonctions prévues) : `score_function_gradient`, `importance_weights`, `bradley_terry_probability`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : B8.7 ∂ Le gradient de politique en une étape : l'astuce de la log-dérivée, puis la baseline sans biais

*Notes* : Frontière : le gradient de politique en une étape et la baseline sans biais (workbookIA B8.7) ; GAE et les losses de `mylearn`.

<a id="ps"></a>
## PS · Projet de synthèse

**Partie** fin · **prépare** — · **dossier** `projets/projet_synthese/` · **MML** — · **sessions de génération** 1

« Les maths d'un algorithme, de A à Z » : tu choisis un algorithme de workbookIA (régression logistique, rétropropagation d'un MLP, VAE, attention…) et tu écris un notebook-article qui dérive tout, l'implémente avec `mymath` et le vérifie contre une bibliothèque. Grille sur 20, pas de solution de référence, un exemple rédigé sur un autre algorithme. En même temps que le projet final de workbookIA.

**Durée estimée** : ≈ 25 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : rédiger une dérivation complète · vérifier une implémentation contre une bibliothèque

**Après** : MB8

