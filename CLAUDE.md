# Consignes pour Claude (sessions de génération de workbookMaths)

1. **Lis `docs/BIBLE.md` en entier** avant toute action : c'est la spécification qui fait foi (en cas de conflit avec un prompt, la bible l'emporte sauf « DÉROGATION »). Puis lis `suivi/PROGRESS.md` (état, étape en cours, calibrage) et, à partir de la session 2, `docs/SYLLABUS.md` (le contrat).
2. **N'écris jamais dans `mon_travail/`** : c'est l'espace de l'apprenant. Tu peux seulement y lire (correction).
3. **Ne modifie jamais workbookIA** (`cemah2/workbookIA`) : il est seulement lu, en lecture seule, pour connaître les notions requises par chacun de ses chapitres et pour éviter doublons et fuites (BIBLE §8, règle de partage). Clone-le à part (`git clone --depth 1 https://github.com/cemah2/workbookia /home/claude/cemah2/workbookia`), jamais dans ce dépôt.
4. Un stub `mymath` publié n'est jamais modifié ; `templates/mymath_stubs/MANIFEST.json` ne fait que grandir. Les ID d'exercices sont stables.
5. Toute décision ou dérogation → une ligne dans `docs/BIBLE.md` §24.

## Identifiants (BIBLE §8)

- Chapitres : `R0`–`R9` (remise à niveau), puis le numéro du chapitre de workbookIA préparé, avec une lettre s'il y en a plusieurs (`M02a`, `M12c`, `MB3`) ; examens blancs `CP0`–`CP6` ; `POS` (positionnement), `PS` (projet de synthèse). Source unique : `src/wbm/chapters.py` (ordre d'étude, titres, parties, ordre commun avec workbookIA).
- Dossiers : `chapitres/<id en minuscules>_<nom>` (`r7_limites_derivation`, `m12c_valeurs_propres`).
- Exercices : `R7.4`, `M12c.Q2` (quiz), `M12c.R1` (rappel), `M12c.E1` (entretien) ; sous-ID de vérification `M12c.4a`. Tests : `tests/test_<id minuscule>_<module>.py`.

## Environnement de génération

```bash
# Python 3.13 comme Colab ; PyPI n'est joignable qu'en passant par le proxy
export SSL_CERT_FILE=/root/.ccr/ca-bundle.crt REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt
unset NO_PROXY no_proxy
uv venv --python /usr/local/bin/python3.13 ~/venv313 && source ~/venv313/bin/activate
uv pip install -r requirements.txt && uv pip install -e .
```
- Si le réseau est coupé (proxy 403), le dire à l'utilisateur ; les dépôts GitHub publics restent accessibles par `git clone`.
- Pas de PyTorch : `wbm.setup()` ne l'importe jamais.

## Commandes de vérification

```bash
python -m pytest -q                         # infra + mymath (mode learner : skips normaux)
python -m pytest -q --impl=ref              # la référence doit être verte
python -m pytest -q --impl=stubs tests/test_*.py   # les tests de mymath doivent ÉCHOUER (⏳) : ils ne sont pas vides
python tools/run_all_notebooks.py chapitres/<dossier>/05_solutions.ipynb --inplace   # exécute, garde les sorties
python tools/build_answers.py               # régénère src/wbm/answers.json depuis les solutions exécutées
                                            # (refuse si une BONNE réponse change : vérifier, puis --accept-answer-changes)
python tools/build_answers.py --check
python tools/run_all_notebooks.py chapitres/<dossier>/03_notebook.ipynb   # « Run all » sans rien remplir
python tools/export_flashcards.py --check
python 00_setup/check_env.py
```
```bash
python tools/syllabus.py check      # cohérence des données du syllabus (0 erreur, 0 avertissement attendus)
python tools/syllabus.py build      # régénère docs/SYLLABUS.md, docs/PARCOURS.md, docs/syllabus/COUVERTURE_IA.md,
                                    # le tableau du README et le modèle du tableau de bord
python tools/syllabus.py stats
```
- Source du syllabus : `docs/syllabus/data/partie_*.py` et `fin.py` (jamais les `.md` générés). Une partie est **détaillée** (chaque exercice) dans une session de syllabus juste avant sa génération ; avant, elle est seulement **planifiée** (notions, prérequis, MML, fonctions `mymath` prévues, qui peuvent encore changer). Détailler une partie : écrire ses exercices, ses stubs `mymath` et leur ligne dans `MANIFEST.json`, relire la couverture de workbookIA, puis `check` et `build`.
- Couverture de workbookIA : `docs/syllabus/data/ia_coverage.py` relie chaque notion mathématique d'un chapitre de workbookIA (copie figée `docs/syllabus/workbookia_notions.json`) au chapitre de maths qui l'enseigne avant lui. Si workbookIA évolue : `python tools/snapshot_workbookia.py /home/claude/cemah2/workbookia` (lecture seule ; `--check` dit seulement si la copie est à jour), puis `check`.

## Écrire un chapitre

- **Avant d'écrire** : relire le chapitre de workbookIA préparé (sa fiche, son `docs/syllabus/data/chXX.json`, ses exercices) pour (1) enseigner toutes les notions mathématiques qu'il utilise, (2) n'en reprendre ni exemple, ni donnée, ni nombre, ni réponse (BIBLE §8, règle de partage ; §20). La section du chapitre dans `docs/SYLLABUS.md` liste ses **frontières** (les ∂ du chapitre préparé et d'autres exercices de workbookIA : ne pas les résoudre ni les paraphraser ; enseigner l'outil dans un autre cadre) et, pour la partie 0, les sections de workbookIA 0A supposées connues (pas de Python au-delà).
- **MML** : renvoyer aux sections (« MML §4.5 »), jamais aux pages ; ne jamais recopier ni paraphraser de près ; les exercices de MML sont seulement conseillés. Le guide de lecture de la fiche dit quel bloc du livre lire avant quelle partie de la fiche.
- Construire les notebooks avec `tools/nbbuild.py` (`md`, `code`, `setup_cell("exercise", chapter="M12c")` ou `setup_cell("solution")`, `badge`, `write_notebook`) et le kit `tools/chapters/chapter_kit.py`, un script `tools/chapters/build_<id>.py` par chapitre qui écrit les **deux** notebooks à partir d'une seule source (modèle : `tools/chapters/build_demo.py`). Figures de la fiche : `tools/chapters/figures_<id>.py` → `chapitres/<dossier>/figures/`.
- Vérification des réponses : `wbm.record(id, valeur, decimals=…, mistakes={message: mauvaise valeur})` côté solutions ; types maths : `kind="fraction"` (`simplified=True` si la forme irréductible est exigée), `kind="expr"` (`variables=("x",)`, `up_to_constant=True` pour une primitive), `kind="interval"`. L'apprenant appelle toujours `wbm.check(id, sa_réponse)`. `mistakes` associe un **message** à la mauvaise valeur, jamais l'inverse.
- Notebook d'exercices : cellules TODO qui ne font que **définir** ; tout appel au code de l'apprenant dans `with wbm.attempt("M12c.4"):` ; « Run all » doit aller au bout. Cellules de vérification : outils de `wbm.nbtools`. Pas de `!` ni de `%`.
- Stubs `mymath` : signatures figées au syllabus ; référence dans `solutions/mymath_ref/` (imports relatifs, mêmes signatures) ; tests `tests/test_<id>_<module>.py` par la fixture `mymath_module("eigen")`, oracle NumPy, SciPy, SymPy ou `fractions`, jamais une autre fonction de l'apprenant ; première ligne de chaque message d'échec = ce qui était attendu.
- Budget : notebook de solutions < 5 min sur CPU, aucune cellule > 1 min.
- Vérification indépendante (BIBLE §20) : un sous-agent re-résout ✏️/∂/🧮 à l'aveugle, un autre joue l'apprenant sur le notebook.
- Définition du « terminé » : BIBLE §20. Commit `<id>: …`, puis mise à jour de `suivi/PROGRESS.md`.

## Git

- Branche `main`, dépôt `cemah2/workbookMaths` (remote `https://github.com/cemah2/workbookmaths`).
- Avant de pousser depuis un clone superficiel : `git fetch origin main` puis rebase si besoin.
- Ne jamais versionner de PDF (MML) ni de données lourdes (voir `.gitignore`).
