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
| [M07](#m07) | Vecteurs et géométrie de ℝⁿ | 7 | §3.1, §3.2.1, §3.3, §3.4 | ≈ 14 h (estimé) | plan | 1 |
| [M08](#m08) | Tests statistiques | 8 | §8.6 | ≈ 10 h (estimé) | plan | 1 |
| [M09a](#m09a) | Matrices et systèmes linéaires | 9 | §2.1, §2.2, §2.3 | ≈ 16 h (estimé) | plan | 2 |
| [M09b](#m09b) | Moindres carrés et régularisation | 9 | §8.1, §8.2, §9.1, §9.2 | ≈ 16 h (estimé) | plan | 2 |
| [M10](#m10) | Séparabilité linéaire et convexité | 10 | §12.1 | ≈ 8 h (estimé) | plan | 1 |
| [M11](#m11) | Logique, induction et inégalités de concentration | 11 | — | ≈ 10 h (estimé) | plan | 1 |
| [CP2](#cp2) | Examen blanc de la partie II | — | — | ≈ 4 h (estimé) | plan | 1 |
| [M12a](#m12a) | Espaces vectoriels et applications linéaires | 12 | §2.4, §2.5, §2.6, §2.7, §2.8 | ≈ 16 h (estimé) | plan | 2 |
| [M12b](#m12b) | Orthogonalité et projections | 12 | §3.2.2, §3.2.3, §3.5, §3.6, §3.7, §3.8, §9.4 | ≈ 14 h (estimé) | plan | 1 |
| [M12c](#m12c) | Valeurs propres et matrices symétriques | 12 | §4.1, §4.2, §4.3, §4.4 | ≈ 16 h (estimé) | plan | 2 |
| [M12d](#m12d) | SVD et analyse en composantes principales | 12 | §4.5, §4.6, §4.7, §10.1, §10.2, §10.3, §10.4, §10.5, §10.6 | ≈ 16 h (estimé) | plan | 2 |
| [M13a](#m13a) | Vraisemblance et régression logistique | 13 | §8.3 | ≈ 12 h (estimé) | plan | 1 |
| [M13b](#m13b) | Optimisation sous contraintes et SVM | 13 | §7.2, §7.3, ch. 12 | ≈ 14 h (estimé) | plan | 1 |
| [M14](#m14) | Les maths des ensembles | 14 | — | ≈ 6 h (estimé) | plan | 1 |
| [CP3](#cp3) | Examen blanc de la partie III | — | — | ≈ 4 h (estimé) | plan | 1 |
| [M16](#m16) | Couches affines et variance à l'initialisation | 16 | §6.4 | ≈ 8 h (estimé) | plan | 1 |
| [M17](#m17) | Jacobienne et fonctions d'activation | 17 | §5.3 | ≈ 10 h (estimé) | plan | 1 |
| [M18](#m18) | Règle de la chaîne, calcul matriciel et différentiation automatique | 18 | §5.4, §5.5, §5.6 | ≈ 14 h (estimé) | plan | 1 |
| [M19](#m19) | Hessienne, convexité et convergence | 19 | §5.7, §5.8, §7.1, §7.3 | ≈ 14 h (estimé) | plan | 1 |
| [M20](#m20) | Tenseurs, dropout et normalisation | 20 | — | ≈ 8 h (estimé) | plan | 1 |
| [CP4](#cp4) | Examen blanc de la partie IV | — | — | ≈ 4 h (estimé) | plan | 1 |
| [M21](#m21) | Convolution | 21 | — | ≈ 10 h (estimé) | plan | 1 |
| [M22](#m22) | Récurrences et gradient évanescent | 22 | (§4.2) | ≈ 10 h (estimé) | plan | 1 |
| [CP5](#cp5) | Examen blanc de la partie V | — | — | ≈ 4 h (estimé) | plan | 1 |
| [M25a](#m25a) | Gaussienne multivariée | 25 | §6.5, §9.3 | ≈ 14 h (estimé) | plan | 1 |
| [M25b](#m25b) | Variables latentes et ELBO | 25 | §6.7, §8.4, §8.5, §10.7, ch. 11 | ≈ 14 h (estimé) | plan | 1 |
| [M26](#m26) | Chaînes de Markov et équation de Bellman | 26 | — | ≈ 12 h (estimé) | plan | 1 |
| [M27](#m27) | Jeux et distances entre lois | 27 | — | ≈ 10 h (estimé) | plan | 1 |
| [M28](#m28) | Matrice de Gram et échantillonnage | 28 | — | ≈ 6 h (estimé) | plan | 1 |
| [CP6](#cp6) | Examen blanc de la partie VI | — | — | ≈ 4 h (estimé) | plan | 1 |
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
| II · Concepts | 7 | — | ≈ 78 h (estimé) | à détailler |
| III · ML classique | 8 | — | ≈ 98 h (estimé) | à détailler |
| IV · Réseaux | 6 | — | ≈ 58 h (estimé) | à détailler |
| V · Architectures | 3 | — | ≈ 24 h (estimé) | à détailler |
| VI · Génératif et RL | 6 | — | ≈ 60 h (estimé) | à détailler |
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

**Notions enseignées** : information de Shannon · bits et nats · entropie · entropie conjointe et conditionnelle · information mutuelle · cross-entropy, log loss · divergence KL · inégalité de Jensen · positivité de la divergence KL · divergence de Jensen-Shannon · codes de longueur fixe et variable · inégalité de Kraft, code de Huffman · perplexité · sélectionner des features par l'information mutuelle (idée)

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
| M06.1 | ✏️ | L'information d'événements et l'entropie d'une loi à quatre issues | ★ | 20 | §1 §2 | C, E | wbm | — |
| M06.2 | ✏️ | L'entropie maximale : comparer trois lois à trois issues | ★★ | 15 | §2 | C | wbm | — |
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
| M06.21 | 🔮 | Prédire : l'information mutuelle de X et 2X, de X et X² | ★ | 10 | §4 | C, E | wbm | — |
| M06.22 | 🔬 | Estimer une entropie à partir d'un échantillon : le biais des petits échantillons | ★★ | 20 | §2 | C | wbm | — |
| M06.23 | 🎨 | Un diagramme de l'information : H(X), H(Y), H(X | Y), I(X ; Y) | ★ | 20 | §3 §4 | C | manuel | — |
| M06.24 | 🐛 | Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers | ★ | 15 | §5 | C | wbm | — |
| M06.25 | 🛠️ | Calculer 0 log 0 proprement (`scipy.special.xlogy`) | ★ | 10 | §2 | C | manuel | — |
| M06.26 | 🏆 | Défi : deviner un nombre de 1 à 100 en un minimum de questions | ★★★ | 25 | §1 §2 | C | wbm | — |

*Notes* : Entropie, cross-entropy, KL, Jensen-Shannon, Huffman et perplexité sont les fonctions de `mylearn` en workbookIA 6 ; mymath écrit ce qui les entoure (entropies conjointe et conditionnelle, information mutuelle, Kraft, codes préfixes, écart de Jensen). Le code de Huffman est énoncé, pas construit à la main ni programmé (workbookIA 6.6 et 6.23) ; ni Morse, ni pièce, ni dé, ni textes littéraires (workbookIA 6.1 à 6.4) ; la KL est calculée dans un seul sens, comme des bits perdus (workbookIA 6.5 la calcule dans les deux). COMPOSITION : pas de 📖 (MML ne traite pas l'information) ; lecture conseillée : MacKay, chapitres 1, 2 et 5. Parcours essentiel : Kraft, Jensen-Shannon et démonstrations hors parcours.

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
| CP1.4 | ✏️ | Estimer une moyenne : erreur type et intervalle de confiance | ★★ | 9 | §1 | C, E | wbm | — |
| CP1.5 | ✏️ | Un tableau de contingence et des métriques comme probabilités | ★★ | 9 | §1 | C, E | wbm | — |
| CP1.6 | ✏️ | Bayes et la loi Beta : une mise à jour conjuguée | ★★ | 9 | §1 | C, E | wbm | — |
| CP1.7 | ✏️ | Taylor, Newton et un calcul stable | ★★ | 9 | §1 | C, E | wbm | — |
| CP1.8 | ✏️ | Gradient, dérivée directionnelle et point critique | ★★ | 10 | §1 | C, E | wbm | — |
| CP1.9 | ✏️ | Entropie, information mutuelle et KL | ★★ | 9 | §1 | C, E | wbm | — |
| CP1.10 | ∂ | Une démonstration courte, au choix parmi deux | ★★★ | 12 | §1 | C, E | manuel | — |
| CP1.11 | 🐛 | Corriger une copie : cinq erreurs | ★★ | 8 | §1 | C, E | wbm | — |
| CP1.12 | 🔗 | Problème de synthèse : estimer un paramètre de bout en bout (vraisemblance, maximum, Newton, incertitude) | ★★ | 12 | §1 | C, E | wbm | — |
| CP1.13 | 🗣️ | Ta carte mentale et ta fiche d'une page | ★ | 60 | §2 | C, E | manuel | — |

*Notes* : Fichiers comme CP0 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, 03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend le checkpoint I de workbookIA (`checkpoints/partie_1/` de workbookIA), qui se fait juste après.

<a id="m07"></a>
## M07 · Vecteurs et géométrie de ℝⁿ

**Partie** II · **prépare** workbookIA 7 · **dossier** `chapitres/m07_vecteurs_rn/` · **MML** §3.1, §3.2.1, §3.3, §3.4 · **sessions de génération** 1

Les vecteurs de ℝⁿ : normes L1, L2, L∞, distances, produit scalaire, angle et similarité cosinus, inégalité de Cauchy-Schwarz, hyperplans et demi-espaces ; le barycentre (rappel : la moyenne minimise la somme des carrés des distances, cœur de k-means) ; et les surprises de la grande dimension.

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : vecteurs de ℝⁿ · normes L1, L2, L∞ · distances · produit scalaire · angle · similarité cosinus · inégalité de Cauchy-Schwarz · inégalité triangulaire · projection sur une droite · hyperplans et demi-espaces, distance à un hyperplan · frontière de décision linéaire · barycentre et centroïde · k-means : affectation et mise à jour (le principe) · inertie et silhouette · grande dimension, concentration des distances · le neurone comme produit scalaire plus biais · vecteurs one-hot et base canonique · k-means++ : tirer selon le carré des distances

**Après** : R9, M02c, R4

**mymath** : `vectors.py` (fonctions prévues) : `norm_p`, `project_onto_line`, `centroid`, `sum_sq_distances_to`, `side_of_hyperplane`, `distance_to_hyperplane`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 7.5 ∂ Le rayon de l'hyper-orange : r(d) = √d − 1 · 7.6 ∂ Boule dans un cube : rapport des volumes par récurrence · 7.7 ∂ La frontière du centroïde le plus proche est une droite

*Notes* : Coût : 14 h au lieu de 12 (18 notions). Les distances par paires, k-means et la silhouette sont les fonctions de `mylearn` en workbookIA 7.

<a id="m08"></a>
## M08 · Tests statistiques

**Partie** II · **prépare** workbookIA 8 · **dossier** `chapitres/m08_tests/` · **MML** §8.6 · **sessions de génération** 1

Les tests statistiques : hypothèses, statistique de test, p-valeur, test par permutation, erreurs de type I et II, intervalle d'une accuracy, comparaisons multiples ; puis la sélection de modèle (AIC, BIC, facteur de Bayes) et la validation croisée vues comme des estimations bruitées.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : hypothèse nulle et alternative · statistique de test · p-valeur · test par permutation · erreurs de type I et II · puissance d'un test · intervalle d'une accuracy · comparaisons multiples (Bonferroni) · comparer deux modèles · sélection de modèle : AIC, BIC, facteur de Bayes (aperçu) · validation croisée : principe statistique · importance par permutation (principe) · évaluation sur plusieurs graines

**Après** : M02c, M03, M04

**mymath** : `testing.py` (fonctions prévues) : `permutation_test`, `proportion_ci`, `bonferroni`, `paired_difference_ci`, `aic_bic`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 8.6 ∂ Le biais d'optimisme du meilleur de K modèles

<a id="m09a"></a>
## M09a · Matrices et systèmes linéaires

**Partie** II · **prépare** workbookIA 9 · **dossier** `chapitres/m09a_matrices/` · **MML** §2.1, §2.2, §2.3 · **sessions de génération** 2

Les matrices et les systèmes linéaires : produit et formes, transposée, produit de Hadamard, systèmes, pivot de Gauss et forme échelonnée, inverse, premier contact avec le rang ; la passe avant d'un réseau écrite comme un produit matriciel.

**Durée estimée** : ≈ 16 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : matrices, formes · produit matrice-vecteur et matriciel · produit de Hadamard · transposée et ses règles · systèmes linéaires · pivot de Gauss, forme échelonnée · inverse d'une matrice · rang (premier contact) · matrice identité, matrices diagonales · un dataset est une matrice : opérer par ligne, par colonne, élément par élément · Z = XW + b : la convention des poids · un embedding est un produit one-hot × matrice

**Après** : R2, M07

**mymath** : `matrices.py` (fonctions prévues) : `matmul`, `transpose`, `row_echelon`, `solve`, `inverse`, `rank`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 9.6 ∂ Lasso en dimension 1 : le seuillage doux et les zéros exacts

<a id="m09b"></a>
## M09b · Moindres carrés et régularisation

**Partie** II · **prépare** workbookIA 9 · **dossier** `chapitres/m09b_moindres_carres/` · **MML** §8.1, §8.2, §9.1, §9.2 · **sessions de génération** 2

La régression linéaire par les moindres carrés : gradients de aᵀw et de wᵀAw, équations normales, régularisation ridge (et ridge vue comme MAP), lasso, MSE, MAE, Huber et R², décomposition biais-variance, régression vue comme maximum de vraisemblance, features polynomiales, aperçu de la double descente.

**Durée estimée** : ≈ 16 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : risque empirique · gradients de aᵀw et de wᵀAw (calcul matriciel minimal) · moindres carrés · équations normales · features polynomiales : combien de monômes (combinaisons avec répétition) · régularisation ridge · ridge comme MAP · lasso (principe) · MSE, MAE, loss de Huber, R², RMSE · décomposition biais-variance · overfitting et underfitting vus par le biais et la variance · régression comme maximum de vraisemblance · double descente (aperçu) · pénalité L2 et weight decay

**Après** : M09a, M05b, M02c, M04

**mymath** : `linreg.py` (fonctions prévues) : `normal_equations`, `solve_least_squares`, `hat_matrix`, `residual_decomposition`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 9.2 ∂ Moindres carrés : la meilleure droite par dérivées partielles · 9.3 ∂ Ridge en dimension 1 : w* = Σxy / (Σx² + λ) · 9.6 ∂ Lasso en dimension 1 : le seuillage doux et les zéros exacts

*Notes* : Frontières : les moindres carrés par dérivées partielles en dimension 1, ridge et lasso en dimension 1 (workbookIA 9.2, 9.3, 9.6) ne sont pas démontrés ici ; M09b travaille en dimension n, par les gradients matriciels. La régression bayésienne (MML §9.3) se lit en M25a, la projection (MML §9.4) en M12b.

<a id="m10"></a>
## M10 · Séparabilité linéaire et convexité

**Partie** II · **prépare** workbookIA 10 · **dossier** `chapitres/m10_separabilite_convexite/` · **MML** §12.1 · **sessions de génération** 1

Les ensembles convexes et l'enveloppe convexe, la séparation de deux nuages par un hyperplan, l'astuce du biais, et les outils de la preuve de convergence du perceptron (Cauchy-Schwarz, récurrence sur ‖w‖²), que workbookIA 10 assemble.

**Durée estimée** : ≈ 8 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : ensembles convexes · enveloppe convexe · séparabilité linéaire (enveloppes convexes disjointes) · astuce du biais (une coordonnée en plus) · inégalités de récurrence sur une norme · fonctions d'activation : des fonctions d'une variable (rappel R3, R6)

**Après** : M07, R4

**mymath** : `convex.py` (fonctions prévues) : `convex_hull_2d`, `is_linearly_separable`, `margin_of_separator`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 10.4 ∂ Pourquoi un seul perceptron ne peut pas calculer XOR · 10.7 ∂ Le théorème de convergence du perceptron, guidé pas à pas

*Notes* : Frontières : XOR n'est pas séparable et la convergence du perceptron sont démontrés en workbookIA 10 (10.4, 10.7).

<a id="m11"></a>
## M11 · Logique, induction et inégalités de concentration

**Partie** II · **prépare** workbookIA 11 · **dossier** `chapitres/m11_logique_concentration/` · **MML** — · **sessions de génération** 1

La logique au service du raisonnement (déduction, validité, syllogismes, induction et ses sophismes) ; puis les inégalités de Markov, Tchebychev et Hoeffding, les rayons de confiance et l'idée des bornes supérieures de confiance, ε-greedy et regret.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : déduction, validité, solidité · syllogismes et sophismes · induction et ses pièges · inégalité de Markov · inégalité de Tchebychev · inégalité de Hoeffding · rayon de confiance d'une moyenne · bornes supérieures de confiance (UCB, principe) · ε-greedy · regret · échantillonnage de Thompson

**Après** : R4, M02c, M04

**mymath** : `concentration.py` (fonctions prévues) : `markov_bound`, `chebyshev_bound`, `hoeffding_bound`, `hoeffding_radius`, `empirical_tail`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 11.2 ∂ Moyenne incrémentale : Qₙ₊₁ = Qₙ + (Rₙ − Qₙ)/n

*Notes* : Frontière : la moyenne incrémentale (workbookIA 11.2) est démontrée par workbookIA ; M11 s'appuie sur les suites de R5.

<a id="cp2"></a>
## CP2 · Examen blanc de la partie II

**Partie** II · **prépare** — · **dossier** `checkpoints/partie_2/` · **MML** — · **sessions de génération** 1

Examen blanc de la partie II (M07 à M11) et synthèse, juste avant le checkpoint II de workbookIA.

**Durée estimée** : ≈ 4 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : révision de la partie II

**Après** : M11

<a id="m12a"></a>
## M12a · Espaces vectoriels et applications linéaires

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12a_espaces_vectoriels/` · **MML** §2.4, §2.5, §2.6, §2.7, §2.8 · **sessions de génération** 2

Les espaces vectoriels et les applications linéaires : sous-espaces, indépendance, base, dimension, rang, matrice d'une application, noyau, image, théorème du rang, changement de base, applications affines et transformation inverse.

**Durée estimée** : ≈ 16 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : espace vectoriel, sous-espace · combinaison linéaire, famille génératrice · indépendance linéaire · base et dimension · rang, rang d'un produit · application linéaire et sa matrice · noyau et image · théorème du rang · changement de base · applications affines · application réciproque, transformation inverse

**Après** : M09a

**mymath** : `linmaps.py` (fonctions prévues) : `is_independent`, `column_space_basis`, `null_space_basis`, `change_of_basis`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale

*Notes* : Parcours essentiel : le théorème du rang et le changement de base démontrés hors parcours.

<a id="m12b"></a>
## M12b · Orthogonalité et projections

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12b_orthogonalite/` · **MML** §3.2.2, §3.2.3, §3.5, §3.6, §3.7, §3.8, §9.4 · **sessions de génération** 1

Les produits scalaires généraux, les bases orthonormées et Gram-Schmidt, le complément orthogonal, la projection orthogonale, les moindres carrés revus comme une projection, la décomposition QR et le produit scalaire de fonctions.

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : produits scalaires généraux, matrices symétriques définies positives · bases orthonormées · procédé de Gram-Schmidt · complément orthogonal · projection orthogonale · moindres carrés comme projection · décomposition QR · produit scalaire de fonctions

**Après** : M12a, M09b

**mymath** : `orthogonal.py` (fonctions prévues) : `gram_schmidt`, `project`, `qr`, `least_squares_qr`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale

*Notes* : Parcours essentiel : QR et le produit scalaire de fonctions hors parcours (workbookIA 12 n'en a pas besoin).

<a id="m12c"></a>
## M12c · Valeurs propres et matrices symétriques

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12c_valeurs_propres/` · **MML** §4.1, §4.2, §4.3, §4.4 · **sessions de génération** 2

Le déterminant et la trace, les valeurs et vecteurs propres, la diagonalisation et le théorème spectral, les matrices définies positives et Cholesky, les formes quadratiques et la convexité à plusieurs variables, la matrice de covariance vue comme matrice symétrique positive, le blanchiment et la racine carrée d'une matrice.

**Durée estimée** : ≈ 16 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : déterminant · trace · polynôme caractéristique · valeurs et vecteurs propres · méthode de la puissance · diagonalisation · théorème spectral · quotient de Rayleigh · matrices définies positives · décomposition de Cholesky · formes quadratiques · convexité à plusieurs variables : cordes et hessienne semi-définie positive (premier contact) · matrice de covariance symétrique positive · blanchiment (whitening) · racine carrée d'une matrice symétrique positive

**Après** : M12b, R7

**mymath** : `eigen.py` (fonctions prévues) : `det`, `power_iteration`, `is_positive_definite`, `cholesky`, `whiten`, `sqrtm_psd`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale

<a id="m12d"></a>
## M12d · SVD et analyse en composantes principales

**Partie** III · **prépare** workbookIA 12 · **dossier** `chapitres/m12d_svd_acp/` · **MML** §4.5, §4.6, §4.7, §10.1, §10.2, §10.3, §10.4, §10.5, §10.6 · **sessions de génération** 2

La SVD et son interprétation géométrique, l'approximation de rang faible, la pseudo-inverse et le conditionnement ; puis les axes principaux par le quotient de Rayleigh, la variance expliquée, l'erreur de reconstruction d'une projection, et la place de t-SNE et d'UMAP.

**Durée estimée** : ≈ 16 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : décomposition en valeurs singulières · interprétation géométrique · approximation de rang faible (Eckart-Young) · pseudo-inverse · conditionnement · axes principaux : maximiser uᵀCu sur la sphère (quotient de Rayleigh) · ACP : projection · variance expliquée · ACP en grande dimension · erreur de reconstruction d'une projection · t-SNE et UMAP : préserver des voisinages (aperçu) · erreur de reconstruction et détection d'anomalies

**Après** : M12c, M02c

**mymath** : `svd_pca.py` (fonctions prévues) : `svd`, `low_rank_approximation`, `pinv`, `principal_axes`, `explained_variance_ratio`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 12.6 ∂ Montrer que la standardisation donne moyenne 0 et variance 1 · 12.8 ∂ Variance d'une projection et axe de variance maximale · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé)

*Notes* : MML §10.2 dérive l'axe de variance maximale par Lagrange : M12d passe par le quotient de Rayleigh, la dérivation de MML se relit en M13b ; §10.7 (point de vue latent) se lit en M25b. Frontières : variance d'une projection et axe de variance maximale (workbookIA 12.8), autoencodeur linéaire et ACP (25.8).

<a id="m13a"></a>
## M13a · Vraisemblance et régression logistique

**Partie** III · **prépare** workbookIA 13 · **dossier** `chapitres/m13a_vraisemblance_logistique/` · **MML** §8.3 · **sessions de génération** 1

Le maximum de vraisemblance (Bernoulli, catégorielle, gaussienne), la log-loss comme moins la log-vraisemblance, la sigmoïde, la convexité de log(1 + eᶻ), la régression logistique comme modèle ; Naïve Bayes comme modèle génératif ; l'entropie, l'indice de Gini et la réduction de variance des arbres.

**Durée estimée** : ≈ 12 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : maximum de vraisemblance · log-vraisemblance · log-loss = moins la log-vraisemblance · régression logistique : le modèle · convexité de log(1 + eᶻ) · Naïve Bayes : hypothèse d'indépendance · impureté d'une distribution : entropie, Gini · réduction de variance (arbres de régression) · linear probe

**Après** : M04, M06, M05b, M12c

**mymath** : `likelihood.py` (fonctions prévues) : `bernoulli_log_likelihood`, `bernoulli_mle`, `categorical_mle`, `gaussian_mle`, `logistic_loss`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 13.8 ∂ Gradient de la log-loss de la régression logistique

*Notes* : Frontière : le gradient de la log-loss de la régression logistique (workbookIA 13.8). Les impuretés et le meilleur découpage sont les fonctions de `mylearn` en workbookIA 13.

<a id="m13b"></a>
## M13b · Optimisation sous contraintes et SVM

**Partie** III · **prépare** workbookIA 13 · **dossier** `chapitres/m13b_lagrange_svm/` · **MML** §7.2, §7.3, ch. 12 · **sessions de génération** 1

L'optimisation sous contraintes : multiplicateurs de Lagrange, dualité, optimisation convexe ; puis les SVM : marge, problème primal et dual, hinge loss, noyaux et astuce du noyau (RBF).

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : optimisation sous contraintes · multiplicateurs de Lagrange · dualité (aperçu) · optimisation convexe · relire MML §10.2 : l'ACP par Lagrange · marge · SVM primal · hinge loss · SVM dual · noyaux et astuce du noyau · noyau RBF

**Après** : M10, M05b, M12c, M12d

**mymath** : `svm.py` (fonctions prévues) : `lagrange_equality_qp`, `hinge_loss`, `svm_subgradient`, `rbf_kernel`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 13.8 ∂ Gradient de la log-loss de la régression logistique

<a id="m14"></a>
## M14 · Les maths des ensembles

**Partie** III · **prépare** workbookIA 14 · **dossier** `chapitres/m14_ensembles/` · **MML** — · **sessions de génération** 1

Les outils des ensembles de modèles : la queue de la loi binomiale, la variance d'une moyenne de variables corrélées, la limite (1 + x/n)ⁿ → eˣ, des poids exponentiels, et l'idée d'une descente de gradient dans un espace de fonctions. workbookIA 14 les applique au vote, au bagging et au boosting.

**Durée estimée** : ≈ 6 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : queue de la loi binomiale · variance d'une moyenne de variables corrélées · (1 + x/n)ⁿ → eˣ · poids exponentiels et renormalisation · descente de gradient dans un espace de fonctions (idée) · forêt aléatoire : décorréler pour réduire la variance

**Après** : M02c, R8, M05b, M05a

**mymath** : `ensembles.py` (fonctions prévues) : `binomial_tail`, `variance_of_mean_correlated`, `normalize_exponential_weights`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 14.3 ∂ Probabilité d'être oublié par un bootstrap : vers 36,8 % · 14.4 ∂ Ajuster les résidus, c'est descendre le gradient de la MSE · 14.5 ✏️ Quand la majorité de votants indépendants se trompe · 14.6 ✏️ Une itération d'AdaBoost à la main · 14.7 ✏️ Deux itérations de gradient boosting sur cinq points

*Notes* : Réduit à 6 h : le bootstrap qui oublie 36,8 % des points, les résidus comme gradient, la majorité qui se trompe, AdaBoost et le gradient boosting à la main sont des exercices de workbookIA 14.

<a id="cp3"></a>
## CP3 · Examen blanc de la partie III

**Partie** III · **prépare** — · **dossier** `checkpoints/partie_3/` · **MML** — · **sessions de génération** 1

Examen blanc de la partie III (M12a à M14) et synthèse, juste avant le checkpoint III de workbookIA.

**Durée estimée** : ≈ 4 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : révision de la partie III

**Après** : M14

<a id="m16"></a>
## M16 · Couches affines et variance à l'initialisation

**Partie** IV · **prépare** workbookIA 16 · **dossier** `chapitres/m16_couches_affines/` · **MML** §6.4 · **sessions de génération** 1

Un réseau comme suite d'applications affines (matrices, formes, comptage de coordonnées), les graphes orientés acycliques et l'ordre topologique, et la variance d'une somme de produits de variables indépendantes : l'outil des règles d'initialisation que workbookIA 16 retrouve.

**Durée estimée** : ≈ 8 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : composition d'applications affines (matrices et vecteurs) · graphe orienté acyclique · ordre topologique · conventions de forme (n_in, n_out) · variance d'un produit de variables indépendantes · variance d'une somme pondérée · fan-in, fan-out (définitions) · réseau feed-forward : la structure mathématique

**Après** : M09a, M12a, M02b

**mymath** : `init.py` (fonctions prévues) : `compose_affine`, `variance_of_product`, `variance_of_weighted_sum`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 16.6 ∂ Symétrie : pourquoi une initialisation constante ne se brise jamais · 16.7 ∂ Conserver la variance : retrouver les règles de LeCun, Glorot et He · 17.3 ∂ Une composition d'affines reste affine ; une ReLU casse tout

*Notes* : Frontières : la brisure de symétrie et les règles de LeCun, Glorot et He (workbookIA 16.6, 16.7) ; « une composition d'affines reste affine, une ReLU casse tout » (17.3).

<a id="m17"></a>
## M17 · Jacobienne et fonctions d'activation

**Partie** IV · **prépare** workbookIA 17 · **dossier** `chapitres/m17_jacobienne/` · **MML** §5.3 · **sessions de génération** 1

La jacobienne, la jacobienne diagonale d'une fonction appliquée coordonnée par coordonnée, les dérivées de fonctions définies par morceaux et de composées avec exp, la saturation, la softmax (translation, température), le log-softmax et la convexité du log-sum-exp.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : jacobienne · jacobienne d'une fonction appliquée coordonnée par coordonnée : une matrice diagonale · produit jacobienne-vecteur · dérivées de fonctions par morceaux et de composées avec exp (outils) · maxout : un maximum de fonctions affines · saturation · softmax, invariance par translation, température · log-softmax et logits · convexité du log-sum-exp · softmax de Boltzmann en RL

**Après** : M05b, M06, M05a, M16

**mymath** : `jacobian.py` (fonctions prévues) : `numerical_jacobian`, `diagonal_jacobian`, `jacobian_vector_product`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 17.3 ∂ Une composition d'affines reste affine ; une ReLU casse tout · 17.4 ∂ Dériver la sigmoïde, tanh et softplus · 17.7 ∂ La Jacobienne de la softmax

*Notes* : Frontières : les dérivées de la sigmoïde, de tanh et de softplus et la jacobienne de la softmax (workbookIA 17.4, 17.7), et les activations de `mylearn`.

<a id="m18"></a>
## M18 · Règle de la chaîne, calcul matriciel et différentiation automatique

**Partie** IV · **prépare** workbookIA 18 · **dossier** `chapitres/m18_retropropagation/` · **MML** §5.4, §5.5, §5.6 · **sessions de génération** 1

La règle de la chaîne multivariée, les gradients par rapport à une matrice et les identités du calcul matriciel sur des exemples hors réseaux, le graphe de calcul, les modes direct (nombres duaux) et inverse de la différentiation automatique, le gradient d'une moyenne, et la vérification de gradient.

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : règle de la chaîne multivariée (somme sur les chemins) · gradients par rapport à une matrice · identités de calcul matriciel (aᵀXb, tr(AX), ‖Xw − y‖²) · conventions de forme des gradients · graphe de calcul · mode direct : nombres duaux · mode inverse (principe) · gradient d'une moyenne = moyenne des gradients · vérification de gradient : erreur relative · gradient par rapport à l'entrée (FGSM)

**Après** : M17, M09a

**mymath** : `autodiff.py` (fonctions prévues) : `Dual`, `dual_derivative`, `numerical_matrix_gradient`, `relative_error`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 18.6 ∂ La règle de la chaîne derrière les deltas · 18.7 ∂ Forme matricielle : XᵀΔ, ΔWᵀ et somme des lignes · 18.8 ∂ Softmax et cross-entropy : le gradient vaut p − y · 18.14 🔨 Cross-entropies calculées sur les logits (binaire et softmax)

*Notes* : workbookIA 18 écrit le mode inverse (`Value`, rétropropagation) ; M18 écrit le mode direct. Frontières : les deltas, XᵀΔ, et le gradient p − y (18.6 à 18.8), les cross-entropies sur les logits (18.14).

<a id="m19"></a>
## M19 · Hessienne, convexité et convergence

**Partie** IV · **prépare** workbookIA 19 · **dossier** `chapitres/m19_hessienne_convergence/` · **MML** §5.7, §5.8, §7.1, §7.3 · **sessions de génération** 1

La hessienne et Taylor à plusieurs variables, le conditionnement, la convergence de la descente de gradient sur une quadratique de ℝⁿ et le pas critique 2/λmax, la descente stochastique, le momentum comme suite récurrente linéaire, l'idée des pas adaptatifs, AdamW, le clipping, et les fonctions convexes.

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : hessienne · Taylor à plusieurs variables · géométrie d'une surface quadratique · conditionnement · descente de gradient sur une quadratique de ℝⁿ : pas critique 2/λmax · descente stochastique et mini-batch : un gradient bruité sans biais · momentum comme suite récurrente linéaire · pas adaptatifs : diviser par une moyenne des carrés (idée) · AdamW : weight decay découplé · plannings de learning rate · gradient clipping par la norme · fonctions convexes · choisir un optimiseur : ce que disent les maths

**Après** : M18, M12c, R5

**mymath** : `optim.py` (fonctions prévues) : `numerical_hessian`, `condition_number`, `critical_learning_rate`, `gd_quadratic_iterates`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 19.7 ∂ Sur une parabole, η doit rester sous 2/a · 19.8 ∂ Moyenne mobile exponentielle : mémoire effective et biais initial

*Notes* : Frontières : le pas sous 2/a sur une parabole et la mémoire effective et le biais initial d'une moyenne exponentielle (workbookIA 19.7, 19.8) ; les optimiseurs de `mylearn`.

<a id="m20"></a>
## M20 · Tenseurs, dropout et normalisation

**Partie** IV · **prépare** workbookIA 20 · **dossier** `chapitres/m20_tenseurs_normalisation/` · **MML** — · **sessions de génération** 1

Les tableaux à n dimensions et `einsum`, l'espérance d'un produit par une variable de Bernoulli, moyennes et variances le long d'axes (normalisations par batch et par couche, vues comme des applications affines), et la jacobienne d'une connexion résiduelle.

**Durée estimée** : ≈ 8 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : tenseurs, axes et `einsum` · espérance d'un produit par une variable de Bernoulli · moyenne et variance le long d'axes · batchnorm et layer norm : centrer, réduire, transformation affine · connexions résiduelles : jacobienne I + J

**Après** : M02c, M19

**mymath** : `tensors.py` (fonctions prévues) : `einsum_matmul`, `einsum_bilinear`, `moments_along_axes`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 20.5 ∂ Dropout : espérance, sous-réseaux et règle du test · 20.8 ∂ Le gradient de la batchnorm

*Notes* : Frontières : l'espérance du dropout et le gradient de la batchnorm (workbookIA 20.5, 20.8).

<a id="cp4"></a>
## CP4 · Examen blanc de la partie IV

**Partie** IV · **prépare** — · **dossier** `checkpoints/partie_4/` · **MML** — · **sessions de génération** 1

Examen blanc de la partie IV (M16 à M20) et synthèse, juste avant le checkpoint IV de workbookIA.

**Durée estimée** : ≈ 4 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : révision de la partie IV

**Après** : M20

<a id="m21"></a>
## M21 · Convolution

**Partie** V · **prépare** workbookIA 21 · **dossier** `chapitres/m21_convolution/` · **MML** — · **sessions de génération** 1

La convolution et la corrélation croisée en 1D et 2D, la convolution comme application linéaire (matrice de Toeplitz) et sa transposée, l'équivariance par translation, les tailles de sortie (padding, stride, dilatation, groupes), le pooling, les noyaux séparables et le champ récepteur.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : convolution et corrélation croisée en 1D et 2D · matrice de Toeplitz et sa transposée · im2col · équivariance par translation · tailles de sortie : padding, stride, dilatation · convolutions groupées et en profondeur : compter les paramètres · max et average pooling · noyaux séparables (rang 1) · champ récepteur

**Après** : M12a, M09a, M18

**mymath** : `conv.py` (fonctions prévues) : `conv1d`, `toeplitz_1d`, `receptive_field`, `is_separable_kernel`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 21.7 ∂ Rétropropager dans une convolution 1D : la somme sur les positions

*Notes* : Frontière : la rétropropagation dans une convolution 1D (workbookIA 21.7) ; les fonctions de convolution 2D sont celles de `mylearn`.

<a id="m22"></a>
## M22 · Récurrences et gradient évanescent

**Partie** V · **prépare** workbookIA 22 · **dossier** `chapitres/m22_recurrences/` · **MML** (§4.2) · **sessions de génération** 1

Les suites récurrentes vectorielles, les puissances d'une matrice, les nombres complexes juste ce qu'il faut pour le rayon spectral, les normes de matrices, les produits de jacobiennes de la rétropropagation dans le temps, le gradient évanescent ou explosif, et le clipping.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : suites récurrentes vectorielles · puissances d'une matrice · nombres complexes : module, forme exponentielle, rotations (premier contact) · valeurs propres complexes, rayon spectral · normes de matrices, norme d'opérateur = σmax · produits de jacobiennes (BPTT) · gradient évanescent ou explosif · clipping · produits de Hadamard par des facteurs dans [0, 1] : ce qui reste après n étapes

**Après** : M12c, M12d, M18

**mymath** : `recurrence.py` (fonctions prévues) : `matrix_power_iterates`, `spectral_radius`, `operator_norm`, `jacobian_product_norms`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 22.6 ∂ Pourquoi le gradient s'évanouit : un produit de dérivées de tanh · 22.7 ∂ Le chemin additif de la cellule LSTM

*Notes* : Frontières : le produit de dérivées de tanh et le chemin additif de la cellule LSTM (workbookIA 22.6, 22.7).

<a id="cp5"></a>
## CP5 · Examen blanc de la partie V

**Partie** V · **prépare** — · **dossier** `checkpoints/partie_5/` · **MML** — · **sessions de génération** 1

Examen blanc de la partie V (M21 et M22) et synthèse, juste avant le checkpoint V de workbookIA.

**Durée estimée** : ≈ 4 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : révision de la partie V

**Après** : M22

<a id="m25a"></a>
## M25a · Gaussienne multivariée

**Partie** VI · **prépare** workbookIA 25 · **dossier** `chapitres/m25a_gaussienne/` · **MML** §6.5, §9.3 · **sessions de génération** 1

La loi gaussienne multivariée : densité et géométrie (ellipses), matrices par blocs et complément de Schur, marginales et conditionnelles, transformations affines, échantillonnage par Cholesky, produit de gaussiennes, régression linéaire bayésienne, et l'interpolation sphérique.

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : gaussienne multivariée : densité · géométrie : ellipses de niveau · matrices par blocs et complément de Schur · marginales et conditionnelles · transformations affines d'une gaussienne · échantillonnage par Cholesky · produit de gaussiennes · régression linéaire bayésienne (MML §9.3) · interpolation sphérique (slerp)

**Après** : M12c, M02b, M06, M09b

**mymath** : `gaussian.py` (fonctions prévues) : `mvn_pdf`, `sample_mvn`, `marginal_gaussian`, `condition_gaussian`, `schur_complement`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 25.5 ∂ Dériver à travers un tirage : l'astuce de reparamétrisation · 25.7 ∂ La divergence KL entre N(μ, σ²) et N(0, 1) · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé)

*Notes* : Frontière : la divergence KL entre N(μ, σ²) et N(0, 1) (workbookIA 25.7) n'est pas calculée ici.

<a id="m25b"></a>
## M25b · Variables latentes et ELBO

**Partie** VI · **prépare** workbookIA 25 · **dossier** `chapitres/m25b_variables_latentes/` · **MML** §6.7, §8.4, §8.5, §10.7, ch. 11 · **sessions de génération** 1

Les variables latentes et les modèles graphiques orientés, l'inégalité de Jensen (rappel de M06), les mélanges de gaussiennes et l'algorithme EM, le point de vue latent de l'ACP, la borne inférieure de l'évidence (ELBO), et le β-VAE.

**Durée estimée** : ≈ 14 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : variables latentes, espace latent · modèles graphiques orientés · inégalité de Jensen (rappel) · mélanges de gaussiennes · algorithme EM · ACP probabiliste (MML §10.7) · ELBO · β-VAE : pondérer le terme KL

**Après** : M25a, M04, M06, M12d

**mymath** : `latent.py` (fonctions prévues) : `gmm_e_step`, `gmm_m_step`, `gmm_log_likelihood`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 25.5 ∂ Dériver à travers un tirage : l'astuce de reparamétrisation · 25.7 ∂ La divergence KL entre N(μ, σ²) et N(0, 1) · 25.8 ∂ Un autoencodeur linéaire retrouve l'ACP (cas 2D guidé)

*Notes* : Coût : 14 h au lieu de 12 (lectures de MML). Frontière : l'astuce de reparamétrisation (workbookIA 25.5) est démontrée par workbookIA.

<a id="m26"></a>
## M26 · Chaînes de Markov et équation de Bellman

**Partie** VI · **prépare** workbookIA 26 · **dossier** `chapitres/m26_markov_bellman/` · **MML** — · **sessions de génération** 1

Les chaînes de Markov (matrice de transition, loi à n pas, loi stationnaire), le processus de décision markovien, l'espérance conditionnelle, le retour actualisé, l'équation de Bellman d'une politique fixée (système linéaire et point fixe d'une contraction), l'itération sur les valeurs, et le biais du maximum. Référence libre : Blitzstein et Hwang.

**Durée estimée** : ≈ 12 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : chaîne de Markov, matrice de transition · loi à n pas · loi stationnaire · processus de décision markovien · politique · espérance conditionnelle · retour actualisé · équation de Bellman d'une politique fixée : système linéaire · point fixe et contraction · itération sur les valeurs (principe) · biais du maximum : E[max] ≥ max E (Double DQN)

**Après** : M09a, R5, M02b, M25b

**mymath** : `markov.py` (fonctions prévues) : `n_step_distribution`, `stationary_distribution`, `bellman_linear_solve`, `bellman_fixed_point_iterates`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 26.7 ∂ Somme géométrique et horizon effectif de γ · 26.8 ∂ Équation de Bellman : le point fixe que vise le Q-learning

*Notes* : Frontières : l'horizon effectif de γ et le point fixe que vise le Q-learning (workbookIA 26.7, 26.8) ; l'itération sur les valeurs de `mylearn`.

<a id="m27"></a>
## M27 · Jeux et distances entre lois

**Partie** VI · **prépare** workbookIA 27 · **dossier** `chapitres/m27_jeux_distances/` · **MML** — · **sessions de génération** 1

Les jeux à somme nulle et le minimax, l'équilibre de Nash, maximiser a·ln t + b·ln(1 − t), le comportement de ln près de 0, la divergence de Jensen-Shannon, la distance de Wasserstein entre deux gaussiennes en dimension 1, la distance de Fréchet, et la mesure d'un décalage de distribution.

**Durée estimée** : ≈ 10 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : jeux à somme nulle, minimax · équilibre de Nash (idée) · maximiser a·ln t + b·ln(1 − t) sur ]0, 1[ · pentes de ln t et de ln(1 − t) près de 0 · divergence de Jensen-Shannon (rappel) · distance de Wasserstein : définition, cas de deux gaussiennes en dimension 1 · distance de Fréchet entre gaussiennes (formule) · décalage de distribution et dérive : les mesurer · GAN : générateur et discriminateur, le jeu mathématique

**Après** : M06, M25a, M12c

**mymath** : `distances.py` (fonctions prévues) : `minimax_value`, `mixed_strategy_value_2x2`, `w2_gaussians_1d`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 27.5 ∂ Le discriminateur optimal D* = p_data / (p_data + p_g) · 27.6 ∂ Pourquoi log(1 − D(G(z))) sature et pas −log D(G(z))

*Notes* : Frontières : le discriminateur optimal et la saturation de log(1 − D) (workbookIA 27.5, 27.6) ; Wasserstein et Fréchet sur des données sont les fonctions de `mylearn`.

<a id="m28"></a>
## M28 · Matrice de Gram et échantillonnage

**Partie** VI · **prépare** workbookIA 28 · **dossier** `chapitres/m28_gram_echantillonnage/` · **MML** — · **sessions de génération** 1

La matrice de Gram, la montée de gradient sur l'entrée, la variation totale d'une image, et l'échantillonnage d'une loi catégorielle avec température, top-k et top-p.

**Durée estimée** : ≈ 6 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : matrice de Gram · montée de gradient sur l'entrée · variation totale · échantillonner une loi catégorielle · température · top-k et top-p

**Après** : M17, M09a, M18

**mymath** : `sampling.py` (fonctions prévues) : `gram_matrix`, `apply_temperature`, `top_k_filter`, `top_p_filter`

**Frontières** (exercices de workbookIA à ne pas résoudre ni paraphraser ici : la notion est enseignée dans un autre cadre, un résultat peut être énoncé et utilisé ; les démonstrations ∂ du chapitre préparé y sont toujours) : 28.3 ∂ Mélanger les positions ne change pas la matrice de Gram · 28.5 ∂ Le gradient de la loss de style

*Notes* : Frontières : l'invariance de la matrice de Gram par permutation des positions et le gradient de la loss de style (workbookIA 28.3, 28.5).

<a id="cp6"></a>
## CP6 · Examen blanc de la partie VI

**Partie** VI · **prépare** — · **dossier** `checkpoints/partie_6/` · **MML** — · **sessions de génération** 1

Examen blanc de la partie VI (M25a à M28) et synthèse, juste avant le checkpoint VI de workbookIA.

**Durée estimée** : ≈ 4 h. Exercices détaillés avant la génération de la partie.

**Notions enseignées** : révision de la partie VI

**Après** : M28

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

**Notions enseignées** : sommes de gaussiennes indépendantes · produit de deux densités gaussiennes en dimension 1 · produits cumulés et plannings de bruit (linéaire, cosinus) · rapport signal sur bruit · ELBO d'une chaîne de variables latentes (principe) · loss de prédiction du bruit (idée) · DDPM et DDIM : ce qui change mathématiquement · guidance sans classifieur (combinaison affine) · équations différentielles, méthode d'Euler · flow matching (initiation)

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

