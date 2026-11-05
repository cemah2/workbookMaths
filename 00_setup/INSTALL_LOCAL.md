# Installer workbookMaths sur ton ordinateur

Deux cas :

- **workbookIA est déjà installé sur ton ordinateur** : son environnement virtuel contient déjà presque tout. Suis le [cas A](#cas-a--réutiliser-lenvironnement-de-workbookia) (deux minutes).
- **Sinon** : suis le [cas B](#cas-b--installation-complète) (15 à 20 minutes, environ 1 Go). PyTorch n'est pas nécessaire ici, l'installation est donc bien plus légère que celle de workbookIA.

Tu peux aussi tout faire sur Google Colab ([COLAB.md](COLAB.md)).

> 💡 **Terminal** : c'est la fenêtre où l'on tape des commandes.
> - **Windows** : menu Démarrer → tape « PowerShell » → *Windows PowerShell*.
> - **Mac** : `Cmd + Espace` → tape « Terminal ».
> - **Linux** : `Ctrl + Alt + T`.
>
> Dans ce guide, une ligne dans un bloc gris est une commande : copie-la, colle-la dans le terminal, appuie sur Entrée.

---

## Cas A · Réutiliser l'environnement de workbookIA

Les deux dépôts ont été conçus pour vivre dans **le même environnement** : mêmes versions de NumPy, SciPy, matplotlib, pandas, scikit-learn et pytest, et des noms de paquets différents (`wbm` et `mymath` ici, `wb` et `mylearn` là-bas).

1. Range workbookMaths **à côté** de workbookIA (pas dedans) :
   ```bash
   cd ~
   git clone https://github.com/cemah2/workbookMaths.git
   ```
2. Active l'environnement de workbookIA :
   ```bash
   source ~/workbookIA/.venv/bin/activate          # Windows : ~\workbookIA\.venv\Scripts\Activate.ps1
   ```
3. Installe ce qui manque (SymPy est souvent déjà là, car PyTorch en dépend) et rends `wbm` importable :
   ```bash
   cd ~/workbookMaths
   pip install -r requirements.txt
   pip install -e .
   ```
   `pip` ne doit rien changer aux versions déjà installées ; s'il propose de remplacer un paquet, arrête-toi et signale-le (prompt de retour à Claude).
4. Passe aux [étapes communes](#étapes-communes).

---

## Cas B · Installation complète

### Étape 1 · Python 3.13

- **Windows** : télécharge le dernier **Python 3.13** sur <https://www.python.org/downloads/windows/> (*Windows installer 64-bit*), lance-le et **coche « Add python.exe to PATH »** avant *Install Now*. Ferme puis rouvre PowerShell et vérifie : `py -3.13 --version`.
- **Mac** : télécharge le dernier **Python 3.13** sur <https://www.python.org/downloads/macos/>, ouvre le `.pkg`, puis vérifie : `python3.13 --version`. Les Mac Intel conviennent aussi : ce dépôt n'utilise pas PyTorch.
- **Linux** : Python 3.12 ou 3.13 convient (`python3 --version`) ; sinon `sudo apt install -y python3 python3-venv python3-pip`.

### Étape 2 · Git

- **Windows** : <https://git-scm.com/download/win>, options par défaut, puis rouvre PowerShell.
- **Mac** : `git --version` (macOS propose d'installer les outils de ligne de commande : accepte).
- **Linux** : `sudo apt install -y git`

Puis, une seule fois :
```bash
git config --global user.name "Prénom Nom"
git config --global user.email "ton.email@example.com"
git config --global pull.rebase true
git config --global rebase.autoStash true
```

### Étape 3 · Le dépôt et son environnement virtuel

```bash
cd ~
git clone https://github.com/cemah2/workbookMaths.git
cd workbookMaths
```

| Système | Créer l'environnement (une fois) | L'activer (à chaque session) |
|---|---|---|
| Windows (PowerShell) | `py -3.13 -m venv .venv` | `.venv\Scripts\Activate.ps1` |
| Mac | `python3.13 -m venv .venv` | `source .venv/bin/activate` |
| Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |

Le début de la ligne du terminal affiche alors `(.venv)`.

> ⚠️ **Windows** : si PowerShell refuse `Activate.ps1`, tape une fois `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, réponds `O`, puis relance l'activation.

### Étape 4 · Les bibliothèques

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```
La première commande installe les versions exactes du workbook (celles de Colab, et de workbookIA) ; la seconde rend le package `wbm` importable depuis n'importe quel dossier.

---

## Étapes communes

### Vérifier l'installation

```bash
python 00_setup/check_env.py
```
Tout doit être ✅. Un seul ⚠️ est normal à ce stade : « mon_travail/mymath pas encore créé ».

### Créer ta librairie `mymath` et tes fichiers de suivi

```bash
python tools/start_chapter.py --init
```
Cela crée `mon_travail/mymath/` (ton code) et `mon_travail/suivi/` (tableau de bord, journal, auto-évaluation). Ensuite, `python tools/start_chapter.py R1` copie le notebook et les squelettes d'un chapitre, **sans jamais écraser** ce que tu as déjà écrit ; `python tools/start_chapter.py 12` prépare d'un coup tous les chapitres de maths à faire avant le chapitre 12 de workbookIA.

### Lancer Jupyter et la démo

```bash
jupyter lab
```
Ouvre `00_setup/demo.ipynb`, puis **Run → Run All Cells** : tout doit s'exécuter jusqu'au bout. Pour arrêter Jupyter : `Ctrl + C` dans le terminal.

---

## Au quotidien

```bash
cd ~/workbookMaths
source .venv/bin/activate          # ou l'environnement de workbookIA (cas A)
git pull                           # récupère les nouveaux chapitres
jupyter lab
```

## Problèmes fréquents

| Symptôme | Solution |
|---|---|
| `python` ou `py` « n'est pas reconnu » (Windows) | Python n'est pas dans le PATH : relance l'installateur, *Modify*, coche *Add Python to environment variables*, puis rouvre PowerShell. |
| `ModuleNotFoundError: No module named 'wbm'` | Environnement pas activé (pas de `(.venv)` en début de ligne), ou `pip install -e .` oublié dans le dossier workbookMaths. |
| `ModuleNotFoundError: No module named 'sympy'` | `pip install -r requirements.txt` depuis le dossier workbookMaths, environnement activé. |
| Conflit de versions pendant `pip install -r requirements.txt` | Cas A : signale-le, ne force rien. Cas B : supprime le dossier `.venv` et refais l'étape 3. |
| Jupyter n'utilise pas le bon Python | Lance `jupyter lab` depuis le terminal où l'environnement est actif. |
| `git pull` refuse de s'exécuter ou laisse des marqueurs `<<<<<<<` | Tu as modifié un fichier en dehors de `mon_travail/`. `git status` montre lequel ; `git restore --source=HEAD --staged --worktree <fichier>` reprend la version du dépôt (copie ta modification avant si tu y tiens). |
