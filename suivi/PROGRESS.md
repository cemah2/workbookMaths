# PROGRESS : état de la génération de workbookMaths

*Tenu par Claude à chaque session (BIBLE §19). Dernière mise à jour : 2026-11-06, session 8 (R4).*

## Prochaine étape

➡️ **Session 9 : R5** (Suites), puis **R6** à **R9** dans l'ordre (une session chacun, deux pour R7) et l'examen blanc **CP0**. Le contrat de chaque chapitre est sa section de `docs/SYLLABUS.md` : exercices, ID, ★, temps, parcours, sections de la fiche, fonctions `mymath` (stubs déjà publiés), sections de workbookIA 0A supposées connues, et **frontières** (exercices de workbookIA à ne pas résoudre). Avant d'écrire : relire le chapitre 0B de workbookIA (lecture seule) pour n'en reprendre ni exemple ni nombre.

Avant la génération de la partie I : **session de syllabus de la partie I** (détailler M02a à M06 et CP1 : exercices, stubs `mymath`, temps, frontières explicites), en tenant compte du calibrage de la partie 0. Rafraîchir d'abord la copie de workbookIA (`python tools/snapshot_workbookia.py <clone> --check`).

## Statut des chapitres

| Partie | Chapitres | Statut |
|---|---|---|
| 0 · Remise à niveau | R0, POS, R1 à R9, CP0 | R0 ✅, POS ✅, R1 ✅, R2 ✅, R3 ✅, R4 ✅ ; le reste 📅 |
| I · Fondations | M02a à M06, CP1 | 📅 planifié |
| II · Concepts | M07 à M11, CP2 | 📅 planifié |
| III · ML classique | M12a à M14, CP3 | 📅 planifié |
| IV · Réseaux | M16 à M20, CP4 | 📅 planifié |
| V · Architectures | M21, M22, CP5 | 📅 planifié |
| VI · Génératif et RL | M25a à M28, CP6 | 📅 planifié |
| VII · Bonus | MB2 à MB8 | 📅 planifié |
| Fin | PS | 📅 planifié |

✅ publié · 🛠️ en cours · 📅 planifié

## À valider sur Colab

- [ ] `00_setup/demo.ipynb` de bout en bout sur Colab (runtime du 2026-11-04 : NumPy 2.4.6, SymPy 1.14.0) : clonage dans `Mon Drive/workbookMaths`, rapport de versions sans ⚠️, quatre ✅.
- [ ] `start_chapter.py --init` depuis une cellule Colab.

## Calibrage

*(retours de l'apprenant et ajustements : vide pour l'instant)*

## Écarts par rapport à la bible

- R0.8 (🛠️ LaTeX) : drapeau `f:02` ajouté au syllabus (exercice de la feuille de réponses, pas du notebook) ; ID et contenu inchangés.
- R0.4 : titre changé (« Prédire : 0,5 + 0,25 et dix fois 0,1, exacts ou arrondis ? ») ; le 🔮 portait sur un résultat que la fiche et workbookIA 0A montraient déjà. ID inchangé.
- R0 : sections de workbookIA 0A supposées connues complétées (§100.2.2 chaînes, §100.3.1 listes).
- POS : titres changés pour POS.3 (« Développer, factoriser, résoudre une équation et une inéquation »), POS.7 (« Sommes avec Σ, somme double et produit avec Π », 7 min), POS.12 (« Résoudre des équations avec exp et ln ») et POS.14 (« Tangente, variations et une limite », 10 min) ; POS.4b répondu par un numéro (1, 2 ou 3) ; POS.3a par la liste des coefficients ; questions ajoutées POS.7d et POS.14d ; fichiers en plus de la note du syllabus : `README.md` (mode d'emploi) et `03_solutions.ipynb`. ID inchangés.

- R1 : R1.26 retitré (« Prédire : arrondir deux fois, est-ce arrondir une fois ? ») : le 🔮 sur `round(2.5)` et `round(3.5)` reprenait l'exemple de workbookIA 0A §100.2.3. R1.4 passe à 15 min et R1.16 à 25 min (R1 : 12,7 h en parcours complet, 9,7 h en parcours essentiel). R1.28 : calculs nommés A à E (les questions gardent a, b, c) ; R1.25c demande l'exposant de l'écart en flottants (au lieu d'un vrai/faux). ID inchangés.

- R2 : R2.9c répondu par une liste de solutions (vide) au lieu d'un nombre ; R2.16d formulé avec la légende 1/2/3 ; R2.19b vérifie `(0, 3, ">")` (toute la droite) ; R2.18b et R2.18c comparent avec `[]` et `"all"` ; R2.26 a une cellule de vérifications automatiques (droites et titre dans l'axe donné, déterminant nul) ; durée 13,6 h (13,5 h prévues). ID inchangés.

- R3 : R3.23 retitré (« Prédire f∘g et g∘f pour « valeur absolue » et « moins 3 » ») ; R3.2 (📈) lit un autre graphique que celui de la première version (relecture à l'aveugle) ; R3.10b répondu par un flottant (pour diagnostiquer 1/f) ; R3.21 dessine dans les axes reçus (`plot_reference(axes)`, comme R3.22 et R3.26) et a des vérifications automatiques ; R3.19a vérifié sur `quadratic_roots(-2, 7, -3)` ; durée 12,8 h (13 h prévues). ID inchangés.

- R4 : R4.4 retitré (« Opérations sur des ensembles et dénombrement ») et R4.R3 (« Additionner des fractions ») ; R4.R2 rattaché au §6 ; R4.14 réécrit (il reprenait workbookIA 9.1, ajouté aux frontières) ; frontières : 0B.3, 0B.5 et 9.1 ; lecture de la fiche à 195 min (13,2 h en parcours complet, 9,9 h en parcours essentiel, au lieu de 12,4 h et 9,1 h) ; notebook rangé dans l'ordre des ID (A : R4.17 à R4.19, B : R4.20 à R4.23, C : R4.24, R4.25). ID inchangés.

**À retenir pour R5 à R9** (R4) : chercher aussi les doublons dans les chapitres de workbookIA **après** 0B (R4.14 reprenait 9.1 : lire la liste des exercices de la copie figée `docs/syllabus/workbookia_notions.json` pour le thème du chapitre) ; une valeur que la fonction de l'apprenant peut rendre sous plusieurs types (None, False, un entier) se vérifie par son `repr` ; une vérification qui compare à une première valeur ne se fait que si celle-ci est juste (`wbm.check(...).passed`) ; un exercice sur des opérateurs (`&` contre `and`) doit avoir des données où le mauvais opérateur donne une mauvaise réponse ; ne rien écrire avant un 🔮 (objectifs du notebook, introduction de la partie, fiche) qui en donne l'issue ; les messages d'erreur classique ne donnent ni un calcul de la réponse (« 30 − 7 + 1 ») ni la valeur qui la contredit.

**À retenir pour R4 à R9** (en plus de la liste qui suit) : une fonction de tracé reçoit ses axes et se vérifie avec `drawn` (de `wbm.nbtools`) ; une sortie triée ou ordonnée se vérifie sur une entrée où l'ordre naturel est faux ; inutile d'enregistrer les valeurs arrondies d'une réponse exacte (6 décimales ou plus) ni les écarts de plusieurs lignes d'un 🐛 (`bug_letters_mistakes` les couvre) ; une prédiction (🔮) n'a que ses `mistakes` comme indices ; dans les tests, chaque appel passe par un `_result` (voir `tests/test_r3_functions.py`) et les cas paramétrés ont des `ids` ; calculer les valeurs des erreurs classiques en exécutant le code fautif (une valeur impossible ne se déclenche jamais).

**À retenir pour R3 à R9** : les vérifications qui appellent le code de l'apprenant passent par `checked` (de `wbm.nbtools`), pour qu'une erreur de son code ne bloque pas « Run all » ; un ensemble de solutions s'enregistre avec 6 décimales quand une fraction non décimale est attendue ; tester aussi les cas dégénérés pour **tous** les sens ou toutes les branches (un test oublié laisse passer un code faux) ; une réponse qu'il faut **arrondir** (ou un décimal exact) s'enregistre en `kind="fraction"` (ou avec plus de décimales que demandé), sinon une valeur non arrondie passe ; un exemple de forme ne doit être la réponse d'aucune question du chapitre (`tests/infra/test_examples_are_not_answers.py`) ; un test d'algorithme dont la version naïve ne finit jamais passe par `_within` (limite de temps, voir `tests/test_r1_arith.py`) ; chaque groupe de tests lancé par le notebook inclut le test qui interdit les outils tout faits (`or test_arith_uses`) ; les cas `ValueError` passent par `_expect_value_error` (une autre exception dit d'abord ce qui était attendu).

**À retenir pour R1 à R9** : ne reprendre aucun nombre ni aucune donnée du test de positionnement (sujet : `positionnement/01_sujet.md`) ; en R5, le 🔮 prévu sur une suite uₙ₊₁ = ½uₙ + 1 est proche de POS.10 (vₙ₊₁ = ½vₙ + 3) : changer ses nombres. Les messages génériques de `wbm` hérités de workbookIA parlent parfois ML ou Python (« indice (1,) », « arrondis avec round() », « vérifie-le avec SymPy ») : les adapter à la partie 0 si un chapitre en souffre.

## Session 8 (2026-11-06) : chapitre R4 ✅

**Fait** : `chapitres/r4_logique_ensembles/` : fiche en 8 sections (≈ 7 200 mots, 4 figures par `tools/chapters/figures_r4.py` : diagrammes de Venn, escalier de Σk, tableau d'une somme double, dominos, exemples `>>>` vérifiés), 36 exercices (8 quiz, 3 rappels, 8 ✏️, 5 ∂, 🔗, ⚖️, 🗣️, 3 🔨, 📦, 🔮, 🔬, 🎨, 🐛, 🛠️), notebooks par `tools/chapters/build_r4.py` (partie 0 : 67 vérifications papier ; parties A à C : 9 exercices ; solutions en 4 s), 108 indices, solutions avec grilles de relecture des ∂, feuille de réponses, 22 flashcards ; `solutions/mymath_ref/logic.py` et `tests/test_r4_logic.py` (45 tests, oracles SymPy `summation` et `product`, `math.prod`, évaluation directe) ; 93 réponses ajoutées à `answers.json` (488 au total) ; glossaire (+21 termes), symboles, formulaire, erreurs fréquentes.

**Vérification indépendante** (sous-agents) : re-résolution à l'aveugle (toutes les réponses retrouvées ; 11 groupes de remarques, dont un doublon avec workbookIA 9.1 et des exemples proches de 0B) ; apprenant simulé (notebook rempli avec des écritures variées et des erreurs classiques, `logic.py` écrit avec des bugs de débutant ; 15 remarques). Corrigés : R4.14 réécrit, exemples et titres proches de 0B remplacés, messages qui donnaient la réponse, vérifications de R4.19 que `False == 0` trompait, données de R4.20 où `and` et `or` donnaient la bonne réponse, issue du 🔮 R4.21 annoncée avant la prédiction, vérifications de R4.22 et R4.23 qui accusaient la mauvaise fonction, `wbm` plus clair (BIBLE §24).

## Session 7 (2026-11-06) : chapitre R3 ✅

**Fait** : `chapitres/r3_fonctions/` : fiche en 9 sections (≈ 5 900 mots, 7 figures par `tools/chapters/figures_r3.py`, exemples `>>>` vérifiés), 37 exercices (8 quiz, 3 rappels, 11 ✏️, 📈, 2 ∂, 🔗, 🗣️, 4 🔨, 📦, 🎨, 🔬, 🔮, 🐛, 🛠️), notebooks par `tools/chapters/build_r3.py` (partie 0 : 85 vérifications papier ; parties A à C : 10 exercices ; solutions en 5 s), 111 indices, solutions avec grilles de relecture des ∂, feuille de réponses, 25 flashcards ; `solutions/mymath_ref/functions.py` et `tests/test_r3_functions.py` (38 tests, oracles `numpy.polyval`, `numpy.polyfit` et SymPy) ; 107 réponses ajoutées à `answers.json` (395 au total) ; glossaire, symboles, formulaire, erreurs fréquentes.

**Vérification indépendante** (sous-agents) : re-résolution à l'aveugle (toutes les réponses retrouvées ; 18 remarques) ; apprenant simulé (notebook rempli avec des écritures variées et des erreurs classiques, `functions.py` écrit avec des bugs de débutant ; 18 remarques). Corrigés : R3.2 réécrit, énoncés et grilles précisés (R3.9f, R3.10d, R3.14) ; une erreur classique impossible (R3.24a) ; une vérification de figure qui refusait `ax.scatter` et ne voyait pas une figure ouverte par l'apprenant ; R3.19a qui laissait passer des racines non triées ; erreurs classiques ajoutées (ordre `[c, m]`, 1/f, priorités, Horner qui part de 1, exceptions autres que `ValueError`, écarts de plusieurs lignes d'un 🐛) ; `wbm` plus clair (valeurs exactes arrondies, virgules décimales, prédictions sans indice de signe, messages d'erreur et résumé de pytest en français ; BIBLE §24).

## Session 6 (2026-11-06) : chapitre R2 ✅

**Fait** : `chapitres/r2_calcul_litteral/` : fiche en 8 sections (≈ 5 100 mots, 4 figures par `tools/chapters/figures_r2.py`, exemples `>>>` vérifiés), 39 exercices (8 quiz, 3 rappels, 12 ✏️, 3 ∂, 🔗, 🗣️, 4 🔨, 2 📦, 🔮, 🔬, 🎨, 🐛, 🛠️), notebooks par `tools/chapters/build_r2.py` (partie 0 : 70 vérifications papier ; parties A à C : 11 exercices ; solutions en 7 s), 117 indices, solutions avec grilles de relecture des ∂, feuille de réponses, 25 flashcards ; `solutions/mymath_ref/algebra.py` et `tests/test_r2_algebra.py` (45 tests, oracles SymPy `solveset` et `numpy.linalg.solve`) ; 97 réponses ajoutées à `answers.json` (288 au total) ; glossaire, symboles, formulaire, erreurs fréquentes.

**Vérification indépendante** (sous-agents) : re-résolution à l'aveugle (les 70 réponses papier retrouvées ; 13 remarques) ; apprenant simulé (notebook rempli avec des écritures variées et des erreurs classiques, `algebra.py` écrit avec des bugs de débutant ; 18 remarques). Corrigés : données de workbookIA 0B (système de la fiche, trois items de quiz), condition « droite » de la fiche, R2.9c ambigu, valeurs arrondies acceptées, fractions entre guillemets refusées dans une liste, erreurs du code de l'apprenant qui bloquaient « Run all » (`checked`), ❌ au lieu de ⏳ dans les tests de `ValueError`, un `solve_linear_inequality` faux qui passait tous les tests (cas `a = 0` pour `>` et `>=`), R2.26 vérifié automatiquement, messages de `wbm` sans jargon, preuves R2.14 et R2.15 complétées (BIBLE §24).

## Session 5 (2026-11-06) : chapitre R1 ✅

**Fait** : `chapitres/r1_nombres_calcul/` : fiche en 9 sections (≈ 7 600 mots, 5 figures par `tools/chapters/figures_r1.py`, exemples `>>>` vérifiés), 40 exercices (8 quiz, 1 rappel, 14 ✏️, 2 ∂, 🔗, 2 🧮, 🗣️, 4 🔨, 📦, 🔮, 🔬, 2 🐛, 🎨, 🛠️), notebooks par `tools/chapters/build_r1.py` (partie 0 : 86 vérifications papier ; parties A à C : 11 exercices ; solutions en 3,5 s), 120 indices, solutions avec grilles de relecture des ∂, feuille de réponses, 25 flashcards ; `solutions/mymath_ref/arith.py` et `tests/test_r1_arith.py` (54 tests, oracles `math.gcd`, `Fraction`, `Decimal`) ; 105 réponses ajoutées à `answers.json` (191 au total) ; glossaire, symboles, formulaire, erreurs fréquentes.

**Vérification indépendante** (sous-agents) : re-résolution à l'aveugle (toutes les réponses retrouvées ; 17 remarques) ; apprenant simulé (notebook, six fonctions écrites avec des bugs de débutant ; 21 remarques). Corrigés : docstring modèle fausse de R1.31 et vérification qui ne comptait pas les exemples faux, exemples de forme qui donnaient des réponses (test ajouté), valeurs non arrondies acceptées (réponses exactes en `kind="fraction"`), mantisses traitées comme des entiers, messages qui donnaient la réponse (R1.9, R1.27), nouvelles erreurs classiques, zéros significatifs, nombres premiers définis, tests plus stricts (poids négatif, −100 % permis, listes au lieu de tuples, PGCD naïf limité à 2 s, `np.gcd` interdit), `wbm` (signe et valeur fausses, rang « 1ᵉʳ » d'un élément, ordre écrit avec `<`, `"4/-7"` irréductible, couple `(3, 5)` expliqué).

## Session 4 (2026-11-06) : test de positionnement ✅

**Fait** : `positionnement/` : sujet de 18 exercices (deux par chapitre de R1 à R9, 57 questions, ≈ 2 h), figure par `tools/chapters/figures_pos.py`, notebook de vérification et notebook de solutions par `tools/chapters/build_pos.py` (la dernière cellule calcule la grille ; messages des valeurs fausses retenus jusqu'à `FINISHED = True`), corrigé avec « où c'est enseigné » pour chaque exercice, feuille de réponses, grille des verdicts (`05_grille.md` : ce qu'il faut faire quand même pour un chapitre sauté), mode d'emploi. 57 réponses vérifiées dans `answers.json` (86 au total). Test `tests/infra/test_positionnement.py` : aucun exemple d'écriture n'est une réponse.

**Vérification** : comparaison avec workbookIA 0A et 0B (lecture seule), dix questions changées ; relecture à l'aveugle (55 réponses justes, 13 remarques) ; apprenant simulé (scénarios vide, tout juste sous d'autres écritures, réponses fausses typiques ; 16 remarques). Corrigés : exemples qui donnaient des réponses, intervalles ouverts justes refusés, POS.17a qui acceptait ±0,5, forme factorisée acceptée en POS.3a, messages qui guidaient la correction, erreurs de forme comptées fausses ; `wbm` plus indulgent sur l'écriture (BIBLE §24).

## Session 3 (2026-11-06) : chapitre R0 ✅

**Fait** : `chapitres/r0_prise_en_main/` (fiche en 7 sections et 3 figures par `tools/chapters/figures_r0.py`, exercices, notebook et corrigé exécuté par `tools/chapters/build_r0.py`, indices, solutions, feuille de réponses, 10 flashcards) ; 24 réponses vérifiées dans `answers.json` ; corrigé exécuté en 2,8 s ; notebook vide « Run all » sans erreur ; glossaire et erreurs fréquentes complétés ; démo : la suite indique R0 puis POS.

**Vérification indépendante** (sous-agent : re-résolution à l'aveugle des quiz et de R0.1, toutes justes ; apprenant simulé, 28 vérifications ✅ avec d'autres écritures que le corrigé) : 26 points corrigés (BIBLE §24) : nombres repris de workbookIA 0A.1 et de l'exemple de 0B remplacés, 🔮 R0.4 refait, messages d'erreur sans chiffre de la réponse, R0.5 et R0.6 répondus par des nombres et des listes, messages des tests de `mean` (ce qui était attendu d'abord), `run_pytest_group` qui signale les tests en attente, Python supposé connu précisé (chaînes, listes, `len`, `sum`).

## Session 2 (2026-11-06) : syllabus ✅

**Fait** :
- `tools/syllabus.py` (`check`, `build`, `stats`) et les données `docs/syllabus/data/` : la **partie 0 détaillée** (R0, POS, R1 à R9, CP0 : 363 exercices, 114 h en parcours complet, 90 h en parcours essentiel), les **parties I à VII et le projet de synthèse planifiés** (notions, prérequis, sections de MML, fonctions `mymath` prévues, frontières). Documents générés : `docs/SYLLABUS.md`, `docs/PARCOURS.md` (avec la synchronisation avec workbookIA 0A), `docs/syllabus/COUVERTURE_IA.md`, le tableau du README et le modèle du tableau de bord.
- Copie figée de workbookIA (`tools/snapshot_workbookia.py`, lecture seule, commit ff7a37c) ; preuve de couverture : 341 notions mathématiques de workbookIA enseignées avant leur chapitre, 217 jugées non mathématiques et listées.
- Stubs `mymath` de la partie 0 publiés (`arith`, `algebra`, `functions`, `logic`, `sequences`, `explog`, `deriv`, `proba_basics`, `plane`) et `MANIFEST.json` ; leurs exemples de docstrings vérifiés par une implémentation de brouillon.
- **Relecture pédagogique indépendante** (sous-agent, 33 points), appliquée : frontières de la règle de partage (σ′, moyenne incrémentale, correction de biais, « la moyenne minimise les carrés »… ne sont plus résolus d'avance), `mymath` qui ne double plus `mylearn`, synchronisation Python avec 0A, test de positionnement déplacé après R0, notions manquantes (droites en R2, argmax et fonctions par morceaux en R3, logit et nats en R6, arccos en R9…), parcours essentiel revu, temps relevés, plan des parties I à VII réordonné. Détail : BIBLE §24.
- BIBLE (§0, §8, §9, §11, §18, §23, §24), `CLAUDE.md`, `docs/METHODE.md`, README mis à jour ; `tests/infra/test_syllabus.py` (52 tests).

**À relire par l'apprenant** : `docs/SYLLABUS.md` (la partie 0 en détail, le plan du reste) et `docs/PARCOURS.md`. C'est le moment de tout changer : rien n'est encore généré.

## Session 1 (2026-11-06) : mise en place ✅

**Fait** :
- Spécification `docs/BIBLE.md` v1, validée par l'apprenant : plan calé sur workbookIA (remise à niveau R0 à R9 pendant 0A, puis les chapitres de maths juste avant le chapitre de workbookIA qu'ils préparent), lecture de MML intégrée comme Glassner, temps sans limite ; §22 (versions) et §24 (décisions de la session) remplis.
- Versions vérifiées sur le dernier runtime publié de Colab (googlecolab/backend-info, 2026-11-04) : Python 3.13.18, SciPy 1.16.3, SymPy 1.14.0, matplotlib 3.10.0, pandas 2.2.3, scikit-learn 1.6.1 ; NumPy figé à 2.1.3 comme workbookIA (Colab : 2.4.6, acceptée aussi). `requirements.txt` et `pyproject.toml`, sans PyTorch.
- Outillage copié depuis workbookIA (lu en lecture seule, jamais modifié) et adapté : package `wbm` (`setup`, `check`/`record`/`attempt`, `nbtools`, `plot`, `synth`, `testing`, `impl` avec `load_mymath`), `src/wbm/chapters.py` (source unique des ID, de l'ordre d'étude et de l'ordre commun avec workbookIA), outils `start_chapter.py` (accepte un numéro de workbookIA), `build_answers.py`, `run_all_notebooks.py`, `export_flashcards.py`, `nbbuild.py`, kit des constructeurs ; `tests/conftest.py` (`--impl=learner|ref|stubs`) ; `mymath` (`_example`, `MANIFEST.json`).
- `wbm.check` étendu aux maths (`src/wbm/mathcheck.py`) : fractions exactes, expressions (SymPy, empreintes de valeurs en points rationnels fixés), intervalles et réunions ; 40 tests.
- Démo `00_setup/demo.ipynb` et `demo_solutions.ipynb` (exécutée, 4 réponses dans `answers.json`), `check_env.py`, guides Colab et local (réutiliser l'environnement de workbookIA ou installer à part).
- Documentation : README (avec l'ordre de travail commun), `CLAUDE.md`, `docs/METHODE.md` (et des modèles de demandes), annexes (symboles, glossaire, erreurs de calcul fréquentes, formulaire, correspondances workbookIA ↔ maths ↔ MML, ressources vérifiées, Anki, cheatsheets NumPy, SymPy et matplotlib), suivi (tableau de bord avec l'ordre commun à cocher, journal, auto-évaluation, remédiation).
- Ressources secondaires vérifiées par recherche web (annexes/ressources.md) : Blitzstein et Hwang, OpenIntro (CC BY-SA 3.0), Book of Proof (CC BY-NC-ND 4.0), Maths et tiques, Khan Academy en français, Exo7 ; MacKay et Sésamath à confirmer avant leur première citation.
- Vérification : 441 tests verts avec `--impl=ref` ; mode apprenant vert (les tests de `mymath` ignorés, normal) ; `--impl=stubs` : le test d'exemple échoue bien (5 ⏳) ; `check_env.py` sans problème ; démo exécutée en 2,5 s.
