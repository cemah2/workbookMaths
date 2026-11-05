# PROGRESS : état de la génération de workbookMaths

*Tenu par Claude à chaque session (BIBLE §19). Dernière mise à jour : 2026-11-06, session 1 (mise en place).*

## Prochaine étape

➡️ **Session 2 : syllabus détaillé.** Pour chacun des 49 chapitres, des examens blancs, du test de positionnement et du projet de synthèse : les exercices (ID, type, ★, durée, prérequis, parcours), les sections de MML couvertes, les notions requises par le chapitre de workbookIA préparé (lues dans son `docs/syllabus/data/`, en lecture seule) et la preuve qu'elles sont toutes enseignées avant, les signatures figées de `mymath` (tous les stubs et `MANIFEST.json`), les temps d'étude recalculés. Outil : `tools/syllabus.py` adapté de workbookIA (`check`, `build`), qui génère `docs/SYLLABUS.md`, `docs/PARCOURS.md`, le modèle du tableau de bord et les tableaux du README. Relecture pédagogique indépendante (sous-agent), puis relecture par l'apprenant.

Ensuite : la remise à niveau R0 à R9 (l'apprenant commence par elle, en parallèle de workbookIA 0A), le test de positionnement, l'examen CP0.

## Statut des chapitres

| Partie | Chapitres | Statut |
|---|---|---|
| 0 · Remise à niveau | POS, R0 à R9, CP0 | 📅 planifié |
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

*(aucun)*

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
