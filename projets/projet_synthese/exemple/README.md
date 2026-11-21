# Projet de synthèse · L'exemple rédigé

> Un projet de synthèse écrit de bout en bout, sur **la régression de Poisson ajustée par la méthode de Newton** (moindres carrés repondérés) : cadrage, notebook-article exécuté, module, tests, mutations et grille remplie. Il sert d'**étalon** : à chaque étape, tu y vois jusqu'où vont une dérivation, une preuve, un test. Son algorithme est hors de la liste et hors de workbookIA, exprès, et il n'est pas accepté comme projet : ton article ne lui emprunte que la méthode.

## Quand le lire

**Une fois ton cadrage écrit une première fois** (`cadrage.md`, PS.1) : ouvert plus tôt, il risque de donner sa forme à ton projet au lieu de laisser ton algorithme la décider. Lis-le une fois en entier (environ 30 minutes, comptées dans les 25 h du projet), puis reprends ton cadrage. Reviens ensuite à la section qui correspond à l'étape où tu en es.

## Étape par étape

| Étape | Où regarder | Ce que tu y trouves |
|---|---|---|
| PS.1 | [`cadrage.md`](cadrage.md) | une page : pourquoi l'algorithme convient, les notions et leurs sections, l'oracle et ses réglages, le plan avec les propriétés visées |
| PS.2 | §2 de [`exemple.ipynb`](exemple.ipynb) | une phrase, une formule, le tableau des notations avec formes et domaines, des hypothèses numérotées (H1) à (H4), les conventions annoncées |
| PS.3 | §3 | chaque étape suivie de sa justification (chapitre et section) et des formes ; la même formule obtenue deux fois (règle de la chaîne, puis différentielle) ; les points délicats (comptage nul, overflow, matrice non inversible) ; la table des formules finales, chacune avec sa fonction et sa docstring |
| PS.4 | §4 et sa cellule « cas limite » | un lemme, deux propriétés rédigées avec « où servent les hypothèses » et « ce qu'elle garantit en pratique », un théorème qui dit quand le maximum existe (et ses conséquences, avec un contre-exemple), et trois hypothèses qui tombent, sur des nombres |
| PS.5 | §5 et sa cellule « vérification de l'exemple » | le premier pas calculé en fractions, un contrôle de vraisemblance annoncé avant le calcul, un pas plein refusé par le garde-fou, le résultat retrouvé par le module à une tolérance justifiée |
| PS.6 | [`poisson_newton.py`](poisson_newton.py) ; §6 et sa cellule « Contrôle du module » | des docstrings qui citent leur équation, cinq fonctions de `mymath` utiles au calcul, des erreurs qui disent ce qui était attendu (et un test pour chacune), aucune boucle sur les exemples |
| PS.7 | [`test_poisson_newton.py`](test_poisson_newton.py), [`mutants.py`](mutants.py) ; §7 | deux oracles indépendants, des différences finies au pas justifié, des tests de propriétés, deux mutations, et ce que chacune enseigne (une mutation que les valeurs de l'exemple à la main ne voient pas) |
| PS.8 | §8 ; [`figures/`](figures/) | une prédiction chiffrée écrite avant (une pente, un nombre de pas), trois graines, des figures aux axes nommés, une conclusion qui confronte la prédiction aux valeurs lues |
| PS.9 | le résumé, §1, §9, les références | un article qui se lit seul, des limites honnêtes (ce qui est admis, ce que les oracles ne vérifient pas), des références par sections |
| PS.E1 | l'annexe | un plan de cinq minutes, le texte de l'exposé, cinq questions d'entretien et leurs réponses, avec ce qui n'est pas démontré, et la façon de le vérifier |
| la grille | [`grille.md`](grille.md) | chaque critère coché avec sa preuve : une section, une cellule, un test ou une commande, que tu peux refaire |

## Le lancer

Le notebook est déjà exécuté, sorties conservées : il se lit tel quel sur GitHub. Pour le réexécuter (une quinzaine de secondes sur CPU), ouvre `projets/projet_synthese/exemple/exemple.ipynb` dans Jupyter depuis le dossier de workbookMaths, ou sur Colab, puis « Run all » ; ses figures s'écrivent dans `figures/`, à côté du notebook exécuté (dans une copie du dossier, c'est la copie qui les reçoit). Les tests et les mutations, depuis le dossier de workbookMaths :

```bash
python -m pytest -q projets/projet_synthese/exemple/test_poisson_newton.py --impl=ref                            # 107 tests
python -m pytest -q projets/projet_synthese/exemple/test_poisson_newton.py --impl=ref --mutant=newton_direction  # des tests échouent
python -m pytest -q projets/projet_synthese/exemple/test_poisson_newton.py --impl=ref --mutant=hessian
```

`conftest.py` est celui du kit, recopié (seul le nom du module change) : il accepte `--impl {learner,ref,stubs}` et `--mutant=<nom>`. L'exemple tourne sur la **référence** de `mymath` (`--impl=ref`, et le setup de solution dans le notebook). Le notebook se reconstruit depuis sa source, `tools/chapters/ps_exemple.py`, par `python tools/chapters/build_ps.py --only exemple`.

## En quoi ton projet en diffère

- **Ta librairie, pas la référence.** Ton module appelle les fonctions de `mymath` que tu as écrites ; dans l'exemple, la cellule « Contrôle du module » les marque « référence », dans ton projet elle doit les marquer « à toi » (un critère de PS.6 que l'exemple, par construction, ne remplit pas).
- **Ta répétition, chronométrée.** L'annexe de l'exemple estime la durée de l'exposé par son nombre de mots ; toi, tu chronomètres une vraie répétition.
- **Ton algorithme, tes mots.** Les dérivations des algorithmes de la liste (les ∂ de workbookIA cités dans le cahier des charges) ne sont écrites nulle part dans ce dépôt, ni ici ni ailleurs : c'est toi qui les rédiges. Ce qui se transpose de l'exemple, c'est la méthode (une étape, sa justification, ses formes ; une prédiction avant l'expérience ; une preuve par critère), pas son contenu.
- **Une mutation suffit.** L'exemple en montre deux, pour comparer ce que chacune révèle des tests.
