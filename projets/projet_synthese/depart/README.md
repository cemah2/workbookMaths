# Projet de synthèse · Le kit de départ

Tout ton projet tient dans ce dossier. `python tools/start_chapter.py PS` l'a copié dans `mon_travail/projet_synthese/` ; Claude n'y écrit jamais, et une nouvelle copie n'écrase aucun de tes fichiers. Le cahier des charges est `projets/projet_synthese/README.md`, la grille `projets/projet_synthese/GRILLE.md`, les indices `projets/projet_synthese/04_indices.md`.

## Ce qu'il contient

| Fichier | Ce que tu en fais | Étapes |
|---|---|---|
| `cadrage.md` | ton cadrage, une page | PS.1 |
| `synthese.ipynb` | ton notebook-article : remplace les blocs 📝, remplis les cellules `TODO` | PS.2 à PS.9, PS.E1 |
| `algo.py` | le module de ton algorithme (NumPy, la bibliothèque standard et `mymath` seulement) | PS.6 |
| `test_algo.py` | tes tests : des squelettes sautés avec ⏳, à écrire | PS.7 |
| `mutants.py` | une copie fautive d'une fonction de `algo.py`, pour vérifier que tes tests l'attrapent | PS.7 |
| `conftest.py` | ce que pytest fournit à tes tests ; tu n'as pas à le modifier | PS.7 |
| `grille.md` | ta copie de la grille : cases et colonne « Preuve », pour l'auto-évaluation | toutes |
| `figures/` | créé par l'expérience de §8 | PS.8 |

## Les commandes

Depuis le dossier de workbookMaths (ou depuis ce dossier, en retirant le chemin, sauf la dernière commande) :

```bash
python -m pytest -q mon_travail/projet_synthese/test_algo.py                     # tes tests, avec ta mymath
python -m pytest -q -rfs mon_travail/projet_synthese/test_algo.py                # la raison de chaque test sauté ou en échec
python -m pytest -q mon_travail/projet_synthese/test_algo.py --impl=ref          # avec la mymath de référence : le bug vient-il de ta librairie ?
python -m pytest -q mon_travail/projet_synthese/test_algo.py --mutant=<nom>      # PS.7 : algo.<nom> remplacée par mutants.<nom>
python -m pytest -q tests/test_m12c_eigen.py                                     # les tests d'un module de ta librairie (ici M12c)
```

Le notebook s'ouvre dans Jupyter depuis ce dossier, ou sur Colab depuis ton Drive (`workbookMaths/mon_travail/projet_synthese/synthese.ipynb`) : sa première cellule de code retrouve le dépôt, la deuxième ce dossier. « Run all » va au bout dès le départ, avec des ⏳ là où ton travail manque.

## Trois règles à garder en tête

- **Ton module appelle ta librairie** : au moins trois fonctions de `mymath` que tu as écrites, chacune utile au calcul. La cellule « Contrôle du module » de §6 marque chaque fonction « à toi » ou « référence » (un module absent de `mon_travail/mymath/` est pris dans la référence, et un module recopié de la référence est marqué « copie de la référence » : ni l'un ni l'autre ne compte).
- **Tes tests ont un oracle indépendant** : NumPy, SciPy, SymPy, scikit-learn ou PyTorch, jamais une autre de tes fonctions ni ta formule recopiée. Ils appellent `algo.<fonction>(...)` par la fixture `algo` (jamais `from algo import ...`, que la mutation n'atteindrait pas).
- **Le code est prêt** quand `pytest -rfs` ne saute plus rien, que la mutation fait échouer un test, et que « Run all » finit sans erreur en moins de 5 minutes, sorties conservées.
