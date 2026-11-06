# Travailler sur Google Colab (avec Google Drive)

Colab exécute les notebooks dans ton navigateur, sur une machine de Google où toutes les bibliothèques sont déjà installées. Le dépôt est gardé dans ton **Google Drive** : ton travail y est sauvegardé et `git pull` y récupère les nouveaux chapitres. Les maths n'ont jamais besoin de GPU.

## 1. Première ouverture

1. Connecte-toi à ton compte Google.
2. Ouvre la démo : [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cemah2/workbookMaths/blob/main/00_setup/demo.ipynb)
   (ou, sur <https://colab.research.google.com> : *Fichier → Ouvrir un notebook → GitHub*, saisis `cemah2/workbookMaths`, choisis `00_setup/demo.ipynb`).
3. Exécute la première cellule (**setup**, `Maj + Entrée`). Colab demande l'accès à Google Drive : accepte.
4. La cellule **clone le dépôt** dans `Mon Drive/workbookMaths` (une seule fois), puis affiche un rapport de l'environnement.
5. *Exécution → Tout exécuter* : tout doit aller jusqu'au bout.

Ce que fait la cellule de setup, à chaque ouverture de n'importe quel notebook :

| Action | Détail |
|---|---|
| monte Google Drive | dans `/content/drive/MyDrive` |
| met le dépôt à jour | `git pull --rebase --autostash` dans `Mon Drive/workbookMaths` (ou le clone la première fois) : tes fichiers de `mon_travail/` sont mis de côté pendant la mise à jour puis remis en place |
| rend `wbm` importable | ajoute `workbookMaths/src` au chemin de Python |
| `wbm.setup(seed=42)` | graines aléatoires, style des graphiques, rapport des versions |

Rien n'est installé : Colab a déjà NumPy, SciPy, SymPy, matplotlib et pandas. workbookIA et workbookMaths sont deux dossiers distincts de ton Drive (`Mon Drive/workbookIA` et `Mon Drive/workbookMaths`).

## 2. Démarrer un chapitre

Dans n'importe quel notebook où le setup a tourné, crée une cellule et exécute, par exemple :

```python
!python /content/drive/MyDrive/workbookMaths/tools/start_chapter.py R1
```

(`… start_chapter.py 12` prépare tous les chapitres de maths à faire avant le chapitre 12 de workbookIA.) Puis, dans Google Drive, ouvre `workbookMaths/mon_travail/r1_…/03_notebook.ipynb` → clic droit → *Ouvrir avec → Google Colaboratory*. Ce notebook est **ta copie**, enregistrée automatiquement dans ton Drive. Le badge « Open in Colab » d'un notebook, lui, ouvre la version du dépôt sur GitHub : ce que tu y écris n'est pas enregistré. De même pour le test de positionnement (`start_chapter.py POS`, ta copie : `mon_travail/positionnement/02_notebook.ipynb`) et pour un examen blanc (`start_chapter.py CP1`, ta copie : `mon_travail/checkpoints/partie_1/02_examen_notebook.ipynb`).

La première fois (ou avec `--init`), `start_chapter.py` crée aussi `mon_travail/suivi/` (tableau de bord, journal, auto-évaluation) et `mon_travail/mymath/` (ta librairie).

### Modifier tes fichiers `.py` et `.md` dans Colab

Ta librairie (`mon_travail/mymath/*.py`), tes réponses papier (`06_mes_reponses.md`) et ton suivi ne sont pas des notebooks. Dans Colab, ouvre le panneau **Fichiers** (icône 📁 à gauche), puis `drive/MyDrive/workbookMaths/mon_travail/…`, et **double-clique** sur le fichier : il s'ouvre dans un éditeur à droite (`Ctrl+S` pour enregistrer). Relance ensuite la cellule de vérification : elle recharge ta librairie.

> ⚠️ Travaille toujours dans `mon_travail/`. Si tu modifies un fichier ailleurs (par exemple `chapitres/`), le prochain `git pull` pourra refuser de s'exécuter.

Pour tester ta librairie `mymath` depuis Colab :
```python
!cd /content/drive/MyDrive/workbookMaths && python -m pytest tests/ -q -m mymath
```

## 3. Sauvegarder ton travail sur GitHub (optionnel)

Même procédure que pour workbookIA (`COLAB.md` de workbookIA, section 5), avec un token limité au dépôt `workbookMaths` et le chemin `/content/drive/MyDrive/workbookMaths`.

## 4. Problèmes fréquents

| Symptôme | Solution |
|---|---|
| « ⚠️ Tes modifications de … entrent en conflit » ou « ⚠️ git pull a échoué » | Un fichier **hors de `mon_travail/`** a été modifié. `!git -C /content/drive/MyDrive/workbookMaths status` montre lequel ; `!git -C /content/drive/MyDrive/workbookMaths restore --source=HEAD --staged --worktree <fichier>` reprend la version du dépôt. |
| `Unable to create '.../.git/index.lock': File exists` | Une session coupée pendant une opération git a laissé un verrou : `!rm /content/drive/MyDrive/workbookMaths/.git/index.lock`, puis relance la cellule de setup. |
| `fatal: destination path ... already exists` | Un dossier `workbookMaths` existe déjà dans ton Drive sans être un dépôt git : renomme-le, puis relance la cellule de setup. |
| « Drive already mounted » | Normal quand on relance la cellule : ce n'est pas une erreur. |
| Une version différente est signalée ⚠️ | Colab a mis à jour ses bibliothèques. En général ça fonctionne ; signale-le à Claude pour mettre le workbook à jour. NumPy 2.1 et 2.4 sont toutes deux acceptées. |
