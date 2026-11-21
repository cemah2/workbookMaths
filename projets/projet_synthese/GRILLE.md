# Projet de synthèse · La grille d'évaluation (sur 20)

> **Deux usages.** Toi d'abord : dans ta copie, `grille.md` (dossier `mon_travail/projet_synthese/`), tu coches `[x]` chaque critère que ton travail tient et tu écris sa preuve (une section et une équation de l'article, un nom de test, une sortie de cellule, un fichier) ; sans preuve, pas de points. Puis Claude, si tu le lui demandes (prompt du [README](README.md#correction)) : il refait sur une copie de ton dossier, sans rien écrire dans `mon_travail/`, chaque vérification de la colonne « Comment le vérifier », et il note étape par étape. Barème d'un critère : tous ses points s'il est tenu, la moitié s'il l'est à moitié, zéro en dessous.

**Lire la grille.** Aucun critère ne repose sur ta parole : une lecture, une commande ou la sortie d'une cellule le montre. « L'article » est ton notebook `synthese.ipynb` ; ses sections ont les numéros du modèle du kit : résumé, §1 Introduction et plan, §2 Le problème, §3 La dérivation, §4 Deux propriétés et un cas limite, §5 Un exemple à la main, §6 L'implémentation, §7 La vérification, §8 L'expérience, §9 Conclusion et limites, Références, Annexe (la présentation). « Le module » est `algo.py`, et ses tests sont dans `test_algo.py` (l'exemple a ses propres noms de fichiers). Exemples de preuves : « §3, éq. (3.2) à (3.7) », « `test_algo.py::test_matches_oracle` », « sortie de la cellule « Contrôle du module » de §6 », « `figures/convergence.png` ».

**Les vérifications communes**, à lancer d'abord, depuis le dossier de workbookMaths. Elles tournent sur une copie de ton dossier : `mon_travail/` n'est pas touché.

```bash
export PYTHONDONTWRITEBYTECODE=1 WBM_ROOT="$PWD"        # aucun fichier .pyc écrit, le dépôt retrouvé depuis la copie
rm -rf /tmp/ps_copie && cp -r mon_travail/projet_synthese /tmp/ps_copie
(cd /tmp/ps_copie && python -m pytest -q -rfs -p no:cacheprovider test_algo.py)                  # PS.7 : tout passe, rien n'est sauté
(cd /tmp/ps_copie && python -m pytest -q -p no:cacheprovider test_algo.py --mutant=<nom>)        # PS.7 : la mutation fait échouer au moins un test
python tools/run_all_notebooks.py /tmp/ps_copie/synthese.ipynb                                  # PS.9 : « Run all » sans erreur ; durée totale < 300 s, cellule la plus lente < 60 s (ignore la colonne « Budget », réglée pour les chapitres)
python -m pytest -q -rs -p no:cacheprovider tests/test_<id>_<module>.py   # PS.6 : pour chaque module appelé (liste dans §6) : des passed, aucun skipped (un module absent donne « N skipped » et le code 0)
```

Le nom de la mutation (`<nom>`) est celui de la fonction de `mutants.py` (le kit), écrit dans §7.

## PS.1 — Cadrer (1 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | `cadrage.md` ne dépasse pas une page (600 mots au plus, sans compter le gabarit) et dit l'algorithme choisi (sa ligne de la liste du README, ou, hors liste, pourquoi il convient : une dérivation d'au moins une page et un oracle indépendant), ce qu'il calcule, ses entrées et ses sorties avec leurs formes | 0,25 | lecture ; `python -c "import sys; w=lambda p: sum(len(l.split()) for l in open(p,encoding='utf-8') if not l.startswith('>')); print(w(sys.argv[1]) - w(sys.argv[2]))" /tmp/ps_copie/cadrage.md projets/projet_synthese/depart/cadrage.md` donne au plus 600 (les mots du cadrage moins ceux du gabarit, les lignes de consigne `>` retirées des deux) | |
| [ ] | les notions de maths dont la dérivation a besoin, chacune avec le chapitre et la section de ce dépôt qui l'enseigne (« M18 §7 ») et, s'il y en a une, la section de MML | 0,25 | lecture ; ouvrir trois renvois au hasard : la section citée enseigne bien la notion | |
| [ ] | l'oracle de la vérification : la bibliothèque, la fonction et les réglages qui la rendent comparable à ton algorithme, et ce que cet oracle ne vérifie pas | 0,25 | lecture ; la fonction existe dans la documentation de la bibliothèque | |
| [ ] | le plan de l'article, avec les deux propriétés visées pour PS.4, le cas limite pressenti et l'expérience visée pour PS.8 | 0,25 | lecture | |

## PS.2 — Poser le problème (1,5 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | §2 dit ce qu'est un exemple, ce que sont les paramètres et ce que l'algorithme calcule ou minimise, en une phrase, puis en une formule | 0,25 | lecture de §2 | |
| [ ] | un tableau des notations : chaque symbole, son sens, sa forme (`(n, p)`, `(p,)`, scalaire) et son domaine | 0,5 | lecture ; trois symboles pris au hasard dans §3 sont dans le tableau, avec la même forme | |
| [ ] | les hypothèses (sur les données, sur les paramètres : rang, positivité, indépendance, domaine de définition) écrites et numérotées, pour être citées en §3 et en §4 | 0,25 | lecture ; §3 ou §4 cite au moins une hypothèse par son numéro | |
| [ ] | les conventions annoncées : vecteurs lignes ou colonnes, gradient en ligne (convention jacobienne) ou de la forme de la variable, somme ou moyenne sur les exemples | 0,25 | lecture de §2 | |
| [ ] | les notations du dépôt ($n$ exemples, $p$ features, $\mathbf{X}$ de forme $(n, p)$, vecteurs et matrices en gras, $\ln$), ou chaque écart signalé | 0,25 | lecture | |

## PS.3 — La dérivation complète (4 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | la dérivation part de l'objectif de §2 et arrive aux formules exactes que le code calcule : chaque formule finale porte un numéro, et la docstring de la fonction qui la calcule cite ce numéro | 1 | lecture croisée de §3 et des docstrings du module (la sortie « API » de §6) : aucune formule finale sans fonction, aucune fonction de calcul sans formule | |
| [ ] | chaque étape cite le résultat qui la justifie : chapitre et section de ce dépôt (« M17 §3 », « M12c §7 ») ou section de MML (« MML §5.5 »), et le résultat cité dit bien ce qui est utilisé | 1 | lecture ; ouvrir trois renvois au hasard | |
| [ ] | la forme de chaque objet est écrite, et chaque produit est vérifié (`(n, p)` fois `(p,)` donne `(n,)`) | 0,5 | lecture ; trois équations prises au hasard | |
| [ ] | la convention annoncée en §2 est tenue partout : pas de gradient tantôt ligne, tantôt colonne, pas de transposée qui apparaît sans être justifiée | 0,5 | lecture | |
| [ ] | aucune étape sautée : chaque ligne applique une règle, et aucune phrase ne remplace un calcul (« on voit que », « il est facile de voir », « après calcul », « évident », « clairement ») | 0,5 | lecture ; `python -c "import json,sys; nb=json.load(open(sys.argv[1],encoding='utf-8')); t=' '.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='markdown').lower(); print(sum(t.count(w) for w in ('on voit','facile de voir','après calcul','évident','clairement')))" /tmp/ps_copie/synthese.ipynb` compte ces mots dans le Markdown ; chaque occurrence se lit : le critère tombe si l'une remplace un calcul de §3 ou §4 | |
| [ ] | les points délicats du domaine sont dits et réglés : division par zéro, logarithme de 0, fonction non dérivable en un point, matrice non inversible (une hypothèse, une convention, un sous-gradient, une régularisation) | 0,5 | lecture | |

## PS.4 — Deux propriétés et un cas limite (2,5 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | propriété 1 : un énoncé complet (hypothèses citées par leur numéro de §2, conclusion) et une démonstration rédigée (hypothèses, étapes justifiées, conclusion) où chaque hypothèse sert | 0,75 | lecture de §4 : retirer une hypothèse casse une étape précise | |
| [ ] | propriété 2 : mêmes exigences | 0,75 | lecture de §4 | |
| [ ] | les deux propriétés portent sur l'algorithme (convexité, unicité, invariance, espérance, borne, coût…), pas sur un outil seul, et l'article dit ce que chacune garantit en pratique ; pour la régression logistique (n° 1), au moins une des deux n'est l'analogue d'aucune propriété de l'exemple (concavité et unicité, somme des valeurs ajustées égale à celle des observations quand il y a une colonne de 1, existence du maximum) | 0,25 | lecture ; pour le n° 1, les propriétés comparées à celles de §4 de l'exemple | |
| [ ] | le cas où une hypothèse tombe : l'hypothèse nommée, et un contre-exemple chiffré ou une expérience qui montre ce qui casse (une conclusion fausse, une itération qui diverge, plusieurs solutions), calculé par la cellule « cas limite » de §4 | 0,5 | lecture ; la sortie de la cellule | |
| [ ] | chaque propriété est aussi vérifiée numériquement (un test de propriété de PS.7 ou l'expérience de PS.8), et §4 renvoie à cette vérification | 0,25 | le renvoi dans §4 ; le test ou la figure existe | |

## PS.5 — Un exemple à la main (1,5 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | un exemple en petite dimension (2 ou 3, quelques exemples), dont toutes les données sont écrites dans §5 | 0,25 | lecture de §5 | |
| [ ] | le calcul complet, étape par étape, avec les formules de §3 (citées par leur numéro), en fractions exactes quand c'est possible, sinon avec le nombre de chiffres gardés | 0,5 | lecture : les résultats intermédiaires sont écrits, pas seulement le résultat final | |
| [ ] | la cellule de vérification de §5 retrouve le résultat à la main par le module, à une tolérance écrite et justifiée (en fractions : égalité exacte ; en flottants : pourquoi cet ordre de grandeur) | 0,5 | la sortie de la cellule : ✅ et l'écart le plus grand | |
| [ ] | un contrôle de vraisemblance annoncé avant le calcul : un ordre de grandeur, un signe, un cas dont le résultat est connu d'avance (un paramètre nul, une symétrie) | 0,25 | lecture | |

## PS.6 — L'implémentation avec `mymath` (3 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | chaque fonction publique du module a une docstring en anglais : ce qu'elle calcule, ses paramètres avec leurs formes, ce qu'elle rend et sa forme, les erreurs qu'elle lève | 0,75 | la sortie « API » de la cellule « Contrôle du module » de §6 ; lecture du module | |
| [ ] | le module appelle au moins trois fonctions de `mymath`, chacune utile au calcul (pas un appel dont le résultat ne sert à rien) | 0,5 | la sortie « mymath » de la cellule « Contrôle du module » ; lecture | |
| [ ] | ces trois fonctions sont les tiennes : leurs modules sont dans `mon_travail/mymath/` (la cellule les marque « à toi », jamais « référence » ni « copie de la référence »), et leurs tests passent avec ton code | 0,75 | la sortie « mymath » ; `python -m pytest -q -rs tests/test_<id>_<module>.py` pour chaque module : des `passed`, aucun `skipped` ; `python -c "import ast,sys; f=lambda p: ast.dump(ast.parse(open(p,encoding='utf-8').read())); print('copie' if f(sys.argv[1])==f(sys.argv[2]) else 'differ')" mon_travail/mymath/<module>.py solutions/mymath_ref/<module>.py` affiche « differ » (un code identique à la référence, aux commentaires et aux espaces près, n'est pas à toi) | |
| [ ] | les imports du module : NumPy, la bibliothèque standard et `mymath` ; ni scikit-learn, ni PyTorch, ni SciPy, ni SymPy (ce sont les oracles de PS.7) | 0,25 | la sortie « imports » de la cellule ; `grep -n -e "^ *import " -e "^ *from " algo.py` | |
| [ ] | une entrée invalide (formes incompatibles, valeur hors du domaine des hypothèses de §2) lève l'erreur que la docstring annonce, avec un message qui dit ce qui était attendu | 0,25 | lecture ; un test de `test_algo.py` le vérifie | |
| [ ] | le code se lit à côté des équations (mêmes noms, une équation par bloc) et ne boucle pas en Python sur les exemples ou les coordonnées quand une opération de NumPy le fait (une boucle sur les itérations ou sur le temps est normale, comme une boucle sur un petit nombre d'exemples autour d'une fonction de `mymath` qui ne prend qu'un nombre, si §6 le dit) | 0,5 | lecture | |

## PS.7 — La vérification contre une bibliothèque (3 points)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | `test_algo.py` compare l'algorithme à un oracle (NumPy, SciPy, SymPy, scikit-learn ou PyTorch) sur des cas tirés au hasard : au moins trois tailles et trois graines, en tests paramétrés aux noms lisibles | 0,75 | `python -m pytest test_algo.py -v` dans la copie : les cas sont listés | |
| [ ] | l'oracle est indépendant : jamais une autre fonction du module ni de `mymath`, ni une formule de §3 recopiée dans le test ; ses réglages (tolérance d'un optimiseur, régularisation retirée, même initialisation) sont écrits et justifiés | 0,5 | lecture des tests | |
| [ ] | les dérivées que le code calcule sont comparées à des différences finies centrées écrites dans le test, avec le pas et la tolérance justifiés ; un algorithme dont le code ne calcule aucune dérivée vérifie à la place une condition d'optimalité de sa dérivation (par différences finies) ou un second oracle exact (fractions, énumération) | 0,5 | lecture des tests | |
| [ ] | un test de propriété (une propriété de §4, une invariance, une identité, une borne) sur des cas tirés au hasard | 0,25 | lecture des tests | |
| [ ] | la mutation : une copie d'une fonction avec une erreur plausible (dans `mutants.py`), que les tests attrapent ; la sortie de pytest qui échoue est dans §7, avec le nom du test qui l'attrape | 0,5 | la sortie de la cellule « mutation » de §7 ; `python -m pytest -q test_algo.py --mutant=<nom>` donne au moins un `failed` (pas seulement des `errors`) dans la copie, alors que sans `--mutant` tout passe | |
| [ ] | chaque message d'échec dit sur sa première ligne ce qui était attendu ; tous les tests passent, aucun n'est sauté | 0,5 | vérifications communes (`-rfs` : aucune ligne `SKIPPED`) ; lecture de trois `assert` | |

## PS.8 — Une expérience numérique (1,5 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | la question et la prédiction sont écrites avant l'exécution (`PREDICTION` dans §8 : une phrase, et un nombre, une pente ou un sens de variation quand c'est possible), et reliées à une propriété de §4 ou à la dérivation | 0,5 | lecture de §8 : la prédiction est datée, chiffrée quand c'est possible, et la conclusion la confronte au résultat ; une prédiction qui recopie la valeur lue sur la figure ne compte pas | |
| [ ] | une figure lisible : les deux axes nommés avec leurs unités, une légende, un titre, une échelle adaptée (logarithmique pour une erreur qui décroît vite), enregistrée dans `figures/` | 0,5 | la sortie de la cellule de §8 (elle signale un axe sans nom ou une légende absente) ; le fichier dans `figures/` | |
| [ ] | la conclusion dit si la prédiction tient, avec la valeur lue sur la figure, et ce qui expliquerait un écart ; plusieurs graines quand le résultat dépend du hasard | 0,5 | lecture de §8 | |

## PS.9 — Rédiger l'article (1 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | l'article se lit seul : un résumé, une introduction qui dit ce qu'on dérive et pourquoi, un plan, une conclusion, des limites (ce que l'article ne montre pas) | 0,25 | lecture du résumé, de §1 et de §9 ; `grep -c "📝" /tmp/ps_copie/synthese.ipynb` donne 0 | |
| [ ] | des références par sections (« MML §5.5 », « M18 §7 », le chapitre de workbookIA), rassemblées en fin d'article ; toute source qui a inspiré un passage est citée | 0,25 | lecture des références | |
| [ ] | un LaTeX propre : chaque formule s'affiche, aucune ligne de code ni de texte brut à la place d'une formule | 0,25 | ouvrir le notebook dans Jupyter, Colab ou sur GitHub s'il est publié ; sinon lire le Markdown : `$` et `$$` appariés, aucune commande hors de MathJax (`\newcommand`, `\begin{align}` dans `$$`), `\tag` sur chaque équation citée | |
| [ ] | « Run all » finit en moins de 5 minutes sur CPU, aucune cellule ne dépasse une minute, et le notebook livré garde ses sorties | 0,25 | vérifications communes : la durée totale (< 300 s) et la cellule la plus lente (< 60 s) que donne `run_all_notebooks.py` ; les sorties présentes dans `mon_travail/projet_synthese/synthese.ipynb` | |

## PS.E1 — Présenter (1 point)

| Fait | Critère | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | le plan de l'exposé de cinq minutes dans l'annexe de l'article : les parties et la durée de chacune | 0,25 | lecture de l'annexe | |
| [ ] | la durée mesurée d'une répétition, entre 4 et 6 minutes | 0,25 | lecture de l'annexe (la date et la durée) ; le seul critère déclaratif de la grille : la présentation simulée (README, « La correction », 3) le confirme quand elle a lieu | |
| [ ] | cinq questions d'entretien (de la banque du README ou les tiennes) et tes réponses écrites, de quelques lignes chacune, qui renvoient à une équation, une propriété ou une figure de l'article, et qui, à défaut de réponse sûre, disent quel test, quelle expérience ou quelle section de MML trancherait | 0,5 | lecture de l'annexe | |

## Les pénalités

| Fait | Pénalité | Pts | Comment le vérifier | Preuve |
|---|---|---|---|---|
| [ ] | un passage recopié ou paraphrasé de près sans être cité : un corrigé de workbookIA ou de ce dépôt, MML, un livre, un article, une page web (une citation entre guillemets avec sa source ne compte pas) | −3 | lecture à côté de la source soupçonnée : des phrases, un ordre d'exposition, des notations ou des erreurs repris tels quels (une même suite de calculs, inévitable dans une dérivation juste, ne suffit pas) | |
| [ ] | un notebook livré qui ne s'exécute pas de bout en bout : le notebook livré contient une sortie d'erreur, ou son exécution dans la copie (`run_all_notebooks.py`) s'arrête sur une erreur | −2 | lecture des sorties ; vérifications communes | |

## La note et les seuils

| | |
|---|---|
| Somme des dix étapes | / 20 |
| Pénalités (à retrancher) | − |
| **Note finale** | **/ 20** |

- **À partir de 14/20** : ton article peut se montrer (portfolio, entretien) ; son lien a sa place dans ton CV, à côté du projet final de workbookIA.
- **De 10 à 14/20 (14 exclu)** : commence par les critères à zéro de PS.3, PS.6 et PS.7, qui pèsent le plus.
- **Sous 10/20** : refais, dans l'ordre du projet, les étapes que la correction désigne, puis demande une nouvelle correction.

**Pour le correcteur.** Seules comptent les preuves que tu as vérifiées toi-même, dans la copie des vérifications communes ; `mon_travail/` reste intact. Un critère refusé s'accompagne de ce qui le montre (section, cellule, test ou commande). Tu ne corriges pas à la place de l'apprenant et tu ne donnes pas la dérivation : montre l'étape fausse ou sautée et nomme la règle qui manque (le chapitre et la section où elle s'enseigne). Lis chaque étape des démonstrations de §3 et de §4, pas seulement la formule finale : une formule finale juste après une étape fausse ne vaut pas les points de l'étape. Une dérivation recopiée, même citée, ne vaut pas les points de PS.3 et PS.4 : la citation évite la pénalité, pas la note. Un algorithme hors de la liste du README n'est accepté que si `cadrage.md` le justifie (une dérivation d'au moins une page, un oracle indépendant). Ne sont pas acceptés : la régression de Poisson (l'exemple), un algorithme sans dérivation, la régression logistique par la seule méthode de Newton. Un projet sur un algorithme refusé ne se note pas : la correction le dit, en une ligne, et s'arrête. Une pénalité ne s'applique que si sa propre vérification la montre.
