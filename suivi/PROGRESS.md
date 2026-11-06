# PROGRESS : état de la génération de workbookMaths

*Tenu par Claude à chaque session (BIBLE §19). Dernière mise à jour : 2026-11-06, session 2 (syllabus).*

## Prochaine étape

➡️ **Session 3 : chapitre R0** (prise en main), puis **R1** à **R9** dans l'ordre (une session chacun, deux pour R7), le test de positionnement **POS** juste après la partie 0, et l'examen blanc **CP0**. Le contrat de chaque chapitre est sa section de `docs/SYLLABUS.md` (exercices, ID, ★, temps, parcours, sections de la fiche, fonctions `mymath` dont les stubs sont déjà publiés). Avant d'écrire R1 à R9 : relire workbookIA 0B (lecture seule) pour ne reprendre aucun de ses exemples ni de ses nombres.

Avant la génération de la partie I : **session de syllabus de la partie I** (détailler M02a à M06 et CP1 : exercices, stubs `mymath`, temps), en tenant compte du calibrage de la partie 0.

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
