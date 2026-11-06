# PROGRESS : état de la génération de workbookMaths

*Tenu par Claude à chaque session (BIBLE §19). Dernière mise à jour : 2026-11-06, session 4 (POS).*

## Prochaine étape

➡️ **Session 5 : R1** (Nombres et calcul), puis **R2** à **R9** dans l'ordre (une session chacun, deux pour R7) et l'examen blanc **CP0**. Le contrat de chaque chapitre est sa section de `docs/SYLLABUS.md` : exercices, ID, ★, temps, parcours, sections de la fiche, fonctions `mymath` (stubs déjà publiés), sections de workbookIA 0A supposées connues, et **frontières** (exercices de workbookIA à ne pas résoudre). Avant d'écrire : relire le chapitre 0B de workbookIA (lecture seule) pour n'en reprendre ni exemple ni nombre.

Avant la génération de la partie I : **session de syllabus de la partie I** (détailler M02a à M06 et CP1 : exercices, stubs `mymath`, temps, frontières explicites), en tenant compte du calibrage de la partie 0. Rafraîchir d'abord la copie de workbookIA (`python tools/snapshot_workbookia.py <clone> --check`).

## Statut des chapitres

| Partie | Chapitres | Statut |
|---|---|---|
| 0 · Remise à niveau | R0, POS, R1 à R9, CP0 | R0 ✅, POS ✅ ; le reste 📅 |
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

**À retenir pour R1 à R9** : ne reprendre aucun nombre ni aucune donnée du test de positionnement (sujet : `positionnement/01_sujet.md`) ; en R5, le 🔮 prévu sur une suite uₙ₊₁ = ½uₙ + 1 est proche de POS.10 (vₙ₊₁ = ½vₙ + 3) : changer ses nombres. Les messages génériques de `wbm` hérités de workbookIA parlent parfois ML ou Python (« indice (1,) », « arrondis avec round() », « vérifie-le avec SymPy ») : les adapter à la partie 0 si un chapitre en souffre.

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
