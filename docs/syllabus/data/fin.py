"""Syllabus, end: the synthesis project (PS), detailed in session 77."""

CHAPTERS = [
    {
        "id": "PS", "dir": "projets/projet_synthese", "hours": 25, "generation_sessions": 1, "mml": [],
        "summary": "« Les maths d'un algorithme, de A à Z » : tu choisis un algorithme de workbookIA (régression "
                   "logistique, rétropropagation d'un MLP, VAE, attention…) et tu écris un notebook-article qui dérive "
                   "tout, l'implémente avec `mymath` et le vérifie contre une bibliothèque. Grille sur 20, pas de "
                   "solution de référence, un exemple rédigé sur un autre algorithme. En même temps que le projet "
                   "final de workbookIA.",
        "objectives": [
            "Choisir un algorithme de workbookIA et en dériver toutes les formules, de l'objectif jusqu'à ce que le "
            "code calcule, chaque étape justifiée par un résultat d'un chapitre de maths et chaque forme vérifiée.",
            "Démontrer deux propriétés de l'algorithme avec leurs hypothèses, et montrer ce qui se passe quand l'une "
            "d'elles tombe.",
            "L'implémenter avec ta librairie `mymath`, et le vérifier contre une bibliothèque indépendante par des "
            "tests qui attrapent de vraies erreurs.",
            "Rédiger un notebook-article qu'un relecteur peut suivre et vérifier, et le présenter en cinq minutes, "
            "comme en entretien.",
        ],
        "sections": [("§1", "Choisir et cadrer"), ("§2", "Dériver"), ("§3", "Implémenter et vérifier"),
                     ("§4", "Rédiger et présenter")],
        "teaches": ["rédiger une dérivation complète", "vérifier une implémentation contre une bibliothèque"],
        "requires": [("tout le parcours, en particulier les chapitres de l'algorithme choisi", "MB8"),
                     ("rédiger une démonstration courte (hypothèses, étapes justifiées, conclusion)", "R4"),
                     ("différences finies centrées et choix du pas", "M05a"),
                     ("gradient de la forme de la variable, lu dans la différentielle", "M18")],
        "after": ["MB8"],
        "frontieres": ["7.7", "9.2", "9.3", "9.6", "12.8", "13.8", "17.7", "18.6", "18.7", "18.8", "19.7", "19.8",
                       "20.8", "21.7", "22.6", "22.7", "25.5", "25.7", "26.7", "26.8", "B2.7", "B3.6", "B3.7",
                       "B5.6", "B5.7", "B8.7"],
        "reading_minutes": 60,
        "flashcards": 0,
        "exercises": [
            ("PS.1", "🗣️", 2, 60, "Cadrer : l'algorithme choisi, ce qu'il calcule, ses entrées et sorties, les notions "
             "de maths et leurs chapitres, l'oracle de la vérification et le plan de l'article", "§1", "E"),
            ("PS.2", "✏️", 2, 90, "Poser le problème : données, paramètres et leurs formes, objectif, hypothèses, "
             "tableau des notations et conventions", "§2", "E c:manuel p:PS.1"),
            ("PS.3", "∂", 4, 270, "La dérivation complète, de l'objectif aux formules que le code calcule : chaque "
             "étape justifiée par un résultat cité, chaque forme vérifiée", "§2", "E p:PS.2"),
            ("PS.4", "∂", 3, 180, "Deux propriétés démontrées avec leurs hypothèses (convexité, unicité, invariance, "
             "espérance, borne, coût), et un cas où une hypothèse tombe", "§2", "E p:PS.3"),
            ("PS.5", "✏️", 3, 120, "Un exemple à la main en dimension 2 ou 3 (en fractions quand c'est possible), "
             "retrouvé par le code", "§2 §3", "E c:manuel p:PS.3"),
            ("PS.6", "🛠️", 4, 210, "L'implémentation : un module documenté (contrat, formes, erreurs) qui appelle au "
             "moins trois fonctions de ta librairie `mymath`, sans bibliothèque de ML", "§3", "E p:PS.3"),
            ("PS.7", "📦", 4, 180, "La vérification : des tests contre une bibliothèque indépendante sur des cas tirés "
             "au hasard, les dérivées contre des différences finies, une propriété, et une erreur introduite exprès "
             "que les tests attrapent", "§3", "E c:pytest p:PS.6"),
            ("PS.8", "🔬", 3, 150, "Une expérience numérique qui illustre une propriété démontrée (convergence, "
             "conditionnement, stabilité, effet d'un hyperparamètre) : une figure légendée et sa conclusion", "§3",
             "E c:manuel p:PS.6"),
            ("PS.9", "🛠️", 3, 120, "Rédiger l'article : introduction, plan, conclusion et limites, références par "
             "sections, LaTeX propre, notebook exécuté de bout en bout en moins de 5 minutes", "§4", "E p:PS.8"),
            ("PS.E1", "💼", 3, 60, "Présenter l'algorithme en cinq minutes, puis répondre à cinq questions "
             "d'entretien sur ses maths", "§4", "E p:PS.9"),
        ],
        "notes": "Fichiers : `README.md` (le cahier des charges : contexte, liste des algorithmes, règles, jalons, les dix "
                 "étapes avec livrable, critères et erreurs à éviter, la grille résumée, la correction), `GRILLE.md` "
                 "(la grille sur 20, critère par critère, chacun observable, avec « Comment le vérifier » et une colonne "
                 "de preuve), `04_indices.md` (trois niveaux par étape), `depart/` (le kit que `start_chapter.py PS` "
                 "copie dans `mon_travail/projet_synthese/` : le modèle du notebook-article `synthese.ipynb`, le module "
                 "`algo.py`, ses tests `test_algo.py` et leur `conftest.py`, le modèle du cadrage, ta copie de la grille "
                 "pour l'auto-évaluation) et `exemple/` (l'exemple rédigé et vérifié : jamais copié par "
                 "`start_chapter.py`). Pas de solution de référence : c'est ton projet. Points : PS.1 1, PS.2 1,5, PS.3 "
                 "4, PS.4 2,5, PS.5 1,5, PS.6 3, PS.7 3, PS.8 1,5, PS.9 1, PS.E1 1 ; pénalités pour un passage recopié "
                 "sans être cité et pour un notebook qui ne s'exécute pas de bout en bout. Correction : auto-évaluation "
                 "sur la copie de la grille, preuve à l'appui, puis correction par Claude sur demande, en lecture seule "
                 "de `mon_travail/projet_synthese/`. **L'exemple** porte sur un algorithme hors de la liste et hors de "
                 "workbookIA : la régression de Poisson ajustée par la méthode de Newton (moindres carrés repondérés), "
                 "sur des données synthétiques, vérifiée contre scikit-learn (`PoissonRegressor`) et SciPy ; il "
                 "appelle des fonctions publiées de `mymath` (version de référence) et ne reprend aucun exercice ni "
                 "aucun nombre de ce dépôt ou de workbookIA. Il montre le niveau attendu, il n'est pas un modèle à "
                 "recopier : on le lit après une première version de son cadrage. **Frontières** : les ∂ de workbookIA "
                 "qui dérivent les algorithmes de la liste (champ `frontieres`) ne sont résolus ni dans le cahier des "
                 "charges, ni dans la grille, ni dans les indices, ni dans l'exemple : c'est l'apprenant qui les "
                 "redérive dans son projet, avec ses propres mots ; les indices restent des conseils de méthode "
                 "(écrire la loss d'un exemple avant la somme, vérifier les formes ligne à ligne, lire le gradient dans "
                 "la différentielle) et ne donnent aucun résultat propre à un algorithme de la liste. **Oracles** : "
                 "NumPy, SciPy, SymPy, scikit-learn, et PyTorch dans le projet de l'apprenant seulement (installé pour "
                 "workbookIA et sur Colab ; ce dépôt ne l'importe jamais) ; jamais une autre fonction de l'apprenant ni "
                 "une formule écrite pour l'occasion. Durée : 25 h, lecture du cahier des charges et de l'exemple "
                 "comprise (60 min), en même temps que le projet final de workbookIA (quatre semaines). Le projet "
                 "appartient aux deux parcours (BIBLE §12).",
    },
]
