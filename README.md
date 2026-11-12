# workbookMaths : les maths du machine learning, au rythme de workbookIA

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cemah2/workbookMaths/blob/main/00_setup/demo.ipynb)

Un cahier d'exercices de mathématiques, en français, qui accompagne [workbookIA](https://github.com/cemah2/workbookIA) **pas à pas** : chaque chapitre de maths se fait juste avant le chapitre de workbookIA qui en a besoin, et porte son numéro (M12a à M12d avant le chapitre 12, MB3 avant le bonus B3). Il part d'un niveau **lycée lointain** (une remise à niveau R0 à R9, faite pendant le chapitre 0A de workbookIA) et va jusqu'aux mathématiques du machine learning : algèbre linéaire, calcul différentiel, probabilités, statistique, information, optimisation.

Il suit le livre **« Mathematics for Machine Learning »** de M. P. Deisenroth, A. A. Faisal et C. S. Ong (Cambridge University Press, 2020), dans l'ordre où workbookIA en a besoin, et reprend le format de workbookIA : fiches de cours, exercices papier, notebooks vérifiés automatiquement, indices, solutions, flashcards, et une librairie construite de tes mains (`mymath`).

> Le livre n'est pas inclus dans ce dépôt : son PDF est gratuit pour un usage personnel sur le site du livre, mais sa notice en interdit la redistribution. Les fiches et les exercices sont originaux ; ils renvoient aux sections sous la forme « (MML §4.5) ». Voir [Crédits et licences](#crédits-et-licences).

**État** : les parties 0 à IV sont publiées (R0 à M20 et les examens blancs CP0 à CP4) ; les parties V à VII et le projet de synthèse sont planifiés dans [`docs/SYLLABUS.md`](docs/SYLLABUS.md), et chacun sera détaillé juste avant sa génération. Les chapitres arrivent dans l'ordre de travail ci-dessous.

## 🔀 Ordre de travail commun

La règle : **la remise à niveau (R0 à R9) pendant le chapitre 0A de workbookIA, puis, avant chaque chapitre k de workbookIA, les chapitres de maths qui portent son numéro.** L'examen blanc de maths d'une partie se fait juste avant le checkpoint de workbookIA de la même partie.

<!-- wbm:readme ordre -->
| Dans workbookIA | Fais d'abord, dans workbookMaths |
|---|---|
| 0A · Python, notebooks et outils *(en parallèle de la remise à niveau ; synchronisation : [PARCOURS](docs/PARCOURS.md#sync-0a))* | **R0** · Prise en main<br>**POS** · Test de positionnement<br>**R1** · Nombres et calcul<br>**R2** · Calcul littéral et équations<br>**R3** · Fonctions<br>**R4** · Logique, ensembles, Σ et Π<br>**R5** · Suites<br>**R6** · Exponentielle et logarithmes<br>**R7** · Limites et dérivation<br>**R8** · Probabilités de base<br>**R9** · Géométrie du plan, vecteurs et trigonométrie |
| 0B · Maths du lycée au ML | **CP0** · Bilan de remise à niveau |
| 1 · Introduction au machine learning et au deep learning | — (rien de nouveau) |
| 2 · Hasard et statistiques de base | **M02a** · Intégrales et densités<br>**M02b** · Variables aléatoires et lois usuelles<br>**M02c** · Échantillons et estimation |
| 3 · Probabilités et mesure de la qualité | **M03** · Probabilités conditionnelles |
| 4 · Règle de Bayes | **M04** · Bayes, vraisemblance et loi Beta |
| 5 · Courbes et surfaces | **M05a** · Dérivées, Taylor et calcul numérique<br>**M05b** · Fonctions de plusieurs variables et gradient |
| 6 · Théorie de l'information | **M06** · Théorie de l'information |
| CP1 · checkpoint de la partie I | **CP1** · Examen blanc de la partie I |
| 7 · Classification | **M07** · Vecteurs et géométrie de ℝⁿ |
| 8 · Entraînement et test | **M08** · Tests statistiques |
| 9 · Overfitting et underfitting | **M09a** · Matrices et systèmes linéaires<br>**M09b** · Moindres carrés et régularisation |
| 10 · Neurones | **M10** · Séparabilité linéaire et convexité |
| 11 · Apprentissage et raisonnement | **M11** · Logique, induction et inégalités de concentration |
| CP2 · checkpoint de la partie II | **CP2** · Examen blanc de la partie II |
| 12 · Préparation des données | **M12a** · Espaces vectoriels et applications linéaires<br>**M12b** · Orthogonalité et projections<br>**M12c** · Valeurs propres et matrices symétriques<br>**M12d** · SVD et analyse en composantes principales |
| 13 · Classifieurs | **M13a** · Vraisemblance et régression logistique<br>**M13b** · Optimisation sous contraintes et SVM |
| 14 · Ensembles | **M14** · Les maths des ensembles |
| 15 · scikit-learn | — (rien de nouveau) |
| CP3 · checkpoint de la partie III | **CP3** · Examen blanc de la partie III |
| 16 · Réseaux feed-forward | **M16** · Applications affines, graphes et variance d'un produit |
| 17 · Fonctions d'activation | **M17** · Jacobienne et règle de la chaîne |
| 18 · Rétropropagation | **M18** · Différentiation automatique et calcul matriciel |
| 19 · Optimiseurs | **M19** · Hessienne, conditionnement et convergence |
| 20 · Deep learning et premiers pas en PyTorch | **M20** · Tenseurs, axes et estimateurs pondérés |
| CP4 · checkpoint de la partie IV | **CP4** · Examen blanc de la partie IV |
| 21 · Réseaux convolutifs (CNN) | **M21** · Convolution, matrices de Toeplitz et équivariance |
| 22 · Réseaux récurrents (RNN, LSTM, GRU) | **M22** · Récurrences vectorielles, rayon spectral et normes de matrices |
| 23 · PyTorch en pratique 1 : du dataset au modèle sauvegardé | — (rien de nouveau) |
| 24 · PyTorch en pratique 2 : améliorer, chercher, CNN et RNN | — (rien de nouveau) |
| CP5 · checkpoint de la partie V | **CP5** · Examen blanc de la partie V |
| 25 · Autoencodeurs et VAE | **M25a** · Gaussienne multivariée<br>**M25b** · Variables latentes et ELBO |
| 26 · Apprentissage par renforcement | **M26** · Chaînes de Markov et équation de Bellman |
| 27 · Réseaux antagonistes génératifs (GAN) | **M27** · Jeux et distances entre lois |
| 28 · Applications créatives | **M28** · Matrice de Gram et échantillonnage |
| 29 · Datasets et préparation du projet final | — (rien de nouveau) |
| CP6 · checkpoint de la partie VI | **CP6** · Examen blanc de la partie VI |
| B1 · Transfer learning et modèles pré-entraînés | — (rien de nouveau) |
| B2 · Tokenisation et embeddings | **MB2** · Cooccurrences, PMI et embeddings |
| B3 · Attention et Transformers : un mini-GPT from scratch | **MB3** · Rotations et attention |
| B4 · LLM en pratique : Hugging Face, prompting, RAG et LoRA | **MB4** · Rang faible et recherche d'information |
| B5 · Modèles de diffusion : un DDPM minimal | **MB5** · Les maths de la diffusion |
| B6 · Explicabilité, équité et éthique | **MB6** · Shapley, intégrales de chemin et équité |
| B7 · Du notebook à la production | — (rien de nouveau) |
| B8 · RL moderne : DQN, gradient de politique, PPO et RLHF | **MB8** · Gradient de politique |
| PF · projet final | **PS** · Projet de synthèse |
<!-- wbm:end ordre -->

`python tools/start_chapter.py 12` prépare d'un coup tous les chapitres de maths à faire avant le chapitre 12 de workbookIA. Le détail de chaque chapitre (contenu, sections de MML, durée estimée) est dans [`docs/BIBLE.md` §8](docs/BIBLE.md#8-plan--chapitre-par-chapitre-de-workbookia).

**Volume estimé** : 49 chapitres, environ 646 h pour le parcours complet (environ 456 h pour le parcours essentiel, la suite étant estimée dans la même proportion que les parties 0 à V), à ajouter aux environ 920 h de workbookIA. Le test de positionnement peut retirer une partie de la remise à niveau.

## 🚀 Démarrage rapide sur Google Colab

1. Clique sur le badge **Open in Colab** ci-dessus (notebook `00_setup/demo.ipynb`).
2. Lance la première cellule (**setup**) et autorise l'accès à Google Drive. Le dépôt est cloné dans `Mon Drive/workbookMaths` ; aux ouvertures suivantes, la même cellule fait un `git pull`.
3. Menu **Exécution → Tout exécuter** : tout doit aller jusqu'au bout.

Guide détaillé : [`00_setup/COLAB.md`](00_setup/COLAB.md).

## 💻 Démarrage en local

Si workbookIA est déjà installé, son environnement suffit (les deux dépôts partagent les mêmes versions) : [`00_setup/INSTALL_LOCAL.md`](00_setup/INSTALL_LOCAL.md), cas A. Sinon, en résumé (Linux/macOS, Python 3.13) :

```bash
git clone https://github.com/cemah2/workbookMaths.git
cd workbookMaths
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python 00_setup/check_env.py          # tout doit être ✅ (un ⚠️ normal : mymath pas encore créé)
python tools/start_chapter.py --init  # crée ta librairie mon_travail/mymath et tes fichiers de suivi
jupyter lab                           # ouvre 00_setup/demo.ipynb
```

## 🔁 Routine pour chaque chapitre

1. `python tools/start_chapter.py R3` (ou `12` pour tous les chapitres de maths d'un chapitre de workbookIA) : copie le notebook et les squelettes `mymath` dans `mon_travail/`, sans jamais écraser ton travail.
2. Ouvre la fiche (`01_fiche.md`) et suis son **ordre conseillé** : à partir du chapitre M02a, un bloc de MML, la partie de la fiche qui lui correspond, puis les quiz 🧠 et les exercices papier ✏️ et ∂ de ce bloc. La remise à niveau n'a pas de livre : la fiche est le cours.
3. Écris tes réponses papier dans `mon_travail/<chapitre>/06_mes_reponses.md`, et vérifie les calculs dans la partie 0 du notebook : `wbm.check` dit si ta réponse est juste (un nombre, une fraction, une expression, un intervalle) sans la révéler.
4. Notebook : à chaque 🔮, écris ta prédiction **avant** d'exécuter ; puis `python -m pytest tests/test_<chapitre>_<module>.py -q` compare tes fonctions `mymath` à NumPy, SciPy ou SymPy.
5. Corrige avec les indices (`04_indices.md`) puis les solutions, importe les flashcards dans Anki (`python tools/export_flashcards.py --chapter R3`).
6. Note ta séance dans `mon_travail/suivi/journal.md` et coche tes exercices dans `mon_travail/suivi/tableau_de_bord.md`. Puis passe au chapitre de workbookIA.

## 🗂️ Structure du dépôt

```
workbookMaths/
├── 00_setup/          installation (Colab, local), check_env.py, notebook de démonstration
├── positionnement/    test de positionnement : ce que tu peux sauter dans la remise à niveau
├── chapitres/         un dossier par chapitre (r0_… à r9_…, m02a_… à m28_…, mb2_… à mb8_…) :
│                      01_fiche, 02_exercices, 03_notebook, 04_indices, 05_solutions (.md et .ipynb exécuté),
│                      06_mes_reponses, flashcards.csv, figures/
├── checkpoints/       partie_0 … partie_6 : examen blanc (sujet, notebook, corrigé, copie) et synthèse
├── projets/           le projet de synthèse
├── annexes/           glossaire FR ↔ EN, symboles, formulaire, erreurs fréquentes, correspondances, cheatsheets, Anki, ressources
├── src/wbm/           outils : setup, wbm.check (nombres, fractions, expressions, intervalles), chapitres, graphiques
├── templates/mymath_stubs/   squelettes de mymath (figés, MANIFEST.json)
├── solutions/mymath_ref/     implémentation de référence de mymath
├── tests/             tests de mymath et de l'outillage (tests/infra/)
├── data/              données légères versionnées et leurs fiches (data/cards/)
├── docs/              BIBLE.md (la spécification), METHODE.md
├── suivi/             PROGRESS.md (génération), modèles de ton tableau de bord, journal, auto-évaluation
├── tools/             scripts (voir Outils) ; tools/chapters/ : un script de construction par chapitre
└── mon_travail/       TON espace : copies des notebooks, ta librairie mymath, ton suivi (Claude n'y écrit jamais)
```

## 🧰 Outils

| Commande | Rôle |
|---|---|
| `python 00_setup/check_env.py` | vérifie ton installation |
| `python tools/start_chapter.py R3` | démarre un chapitre ; `12` : tous les chapitres de maths avant le ch. 12 de workbookIA ; `CP1` : un examen blanc ; `POS` : le test de positionnement ; `PS` : le projet de synthèse ; `--init` : crée `mon_travail/mymath` et ton suivi |
| `python -m pytest tests/ -q -m mymath` | teste toute ta librairie (`--impl=ref` : la référence) |
| `python tools/export_flashcards.py` | fusionne les flashcards en un deck Anki (`--chapter M12c` : un chapitre ; `--apkg` : un paquet `.apkg`, avec genanki) |
| `python tools/run_all_notebooks.py` | outil de génération : exécute les notebooks du dépôt (jamais tes copies de `mon_travail/`) |
| `python tools/build_answers.py` | outil de génération : construit `src/wbm/answers.json` à partir des notebooks de solutions exécutés |

## ⭐ Règles d'or

1. **Calcule à la main d'abord.** Le notebook vérifie ton calcul ; il ne le remplace pas.
2. **Règle des 15 minutes** : bloqué 15 min → indice 1 ; encore 5 min → indice 2, puis l'indice 3.
3. **Prédis avant d'exécuter** (🔮) : écris ton hypothèse, puis compare.
4. **Travaille uniquement dans `mon_travail/`** : les autres dossiers sont mis à jour par `git pull`.
5. **Un chapitre de maths, puis le chapitre de workbookIA qu'il prépare** : c'est là que la notion prend tout son sens.
6. **Révise tes flashcards chaque jour**, même 10 minutes (deux decks : workbookIA et workbookMaths).

## Versions

Python 3.13 et les versions préinstallées sur Colab ; pour les paquets communs, exactement celles de workbookIA (un seul environnement pour les deux dépôts). Détail : [`docs/BIBLE.md` §22](docs/BIBLE.md#22-versions-figées). Pas de PyTorch.

## Crédits et licences

- **Le livre** : M. P. Deisenroth, A. A. Faisal et C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020. Son PDF est gratuit pour un usage personnel ; sa notice interdit la redistribution, la revente et les œuvres dérivées. Le dépôt n'en recopie aucun passage et ne contient jamais le PDF.
- **Ressources libres citées par les fiches** : la liste vérifiée, avec leurs licences, est dans [`annexes/ressources.md`](annexes/ressources.md).
- **L'outillage** (`wbm`, les scripts de `tools/`, les tests d'infrastructure) est adapté de celui de workbookIA, du même auteur.
- **Les bibliothèques** : NumPy, SciPy, SymPy, matplotlib, pandas, scikit-learn, pytest et genanki (facultatif), chacune sous sa propre licence.
