"""Syllabus, part II (before workbookIA chapters 7 to 11): detailed in session 26 (M07 to M11, CP2).

Format: tools/syllabus.py. Exercise tuple: (id, type, stars, minutes, title, covers, flags);
flags: E (essential track), c:wbm|pytest|manuel, f:02|03, p:prerequisites, m:mymath functions written.

Sharing rule (BIBLE §8, §24): every proof (∂) of the workbookIA chapter a math chapter prepares is a frontier
(tools/syllabus.py adds them); ``frontieres`` lists further workbookIA exercises not to solve nor paraphrase. A math
chapter teaches the tool in another setting and may state a result whose proof workbookIA asks. As in part I, MML
blocks are read in the 📖 exercises (the reading time is in those exercises). The notes of each chapter list the data
of workbookIA to avoid; CP2 is also compared with the checkpoint II and the mini-project II of workbookIA.
"""

CHAPTERS = [
    {
        "id": "M07", "dir": "m07_vecteurs_rn", "hours": 15.3, "generation_sessions": 1,
        "mml": ["§3.1", "§3.2.1", "§3.3", "§3.4"],
        "summary": "Les vecteurs de ℝⁿ : produit scalaire, normes L1, L2, L∞ et distances, angle et similarité "
                   "cosinus, inégalité de Cauchy-Schwarz, projection sur une droite, hyperplans et demi-espaces ; "
                   "le barycentre (la moyenne minimise la somme des carrés des distances), l'inertie, la silhouette "
                   "et le principe de k-means ; et les surprises de la grande dimension.",
        "objectives": [
            "Calculer avec des vecteurs de ℝⁿ : combinaisons linéaires, produit scalaire, vecteurs one-hot.",
            "Calculer les normes L1, L2 et L∞ et les distances associées, et démontrer l'inégalité triangulaire.",
            "Calculer un angle et une similarité cosinus, démontrer l'inégalité de Cauchy-Schwarz, projeter sur une "
            "droite.",
            "Décrire un hyperplan par son vecteur normal, dire de quel côté est un point et calculer sa distance.",
            "Démontrer que le barycentre minimise la somme des carrés des distances, et calculer une inertie, une "
            "silhouette et les probabilités de k-means++.",
            "Mesurer, à la main et par simulation, ce qui change quand la dimension grandit.",
        ],
        "sections": [("§1", "Vecteurs de ℝⁿ : un exemple est un vecteur"),
                     ("§2", "Produit scalaire"),
                     ("§3", "Normes et distances : L1, L2, L∞"),
                     ("§4", "Angle, similarité cosinus, Cauchy-Schwarz et projection"),
                     ("§5", "Hyperplans et demi-espaces"),
                     ("§6", "Barycentres : la moyenne, l'inertie, la silhouette et k-means"),
                     ("§7", "La grande dimension")],
        "teaches": ["vecteurs de ℝⁿ", "normes L1, L2, L∞", "distances", "produit scalaire", "angle",
                    "similarité cosinus", "inégalité de Cauchy-Schwarz", "inégalité triangulaire",
                    "projection sur une droite", "hyperplans et demi-espaces, distance à un hyperplan",
                    "frontière de décision linéaire", "barycentre et centroïde",
                    "classifieur du centroïde le plus proche (définition)",
                    "k-means : affectation et mise à jour (le principe)", "inertie et silhouette",
                    "grande dimension : diagonale du cube, vecteurs presque orthogonaux, norme d'un vecteur gaussien",
                    "le neurone comme produit scalaire plus biais", "vecteurs one-hot et base canonique",
                    "k-means++ : tirer selon le carré des distances"],
        "requires": [("vecteurs du plan, norme, produit scalaire, angle", "R9"), ("Σ, raisonnements", "R4"),
                     ("polynôme du second degré, discriminant", "R3"), ("moyenne et variance empiriques", "M02c"),
                     ("espérance, variance, loi uniforme, loi normale", "M02b"), ("gradient, point critique", "M05b"),
                     ("intégration par parties", "M02a"), ("inégalité de Bienaymé-Tchebychev", "M02c"),
                     ("approximation par la tangente", "M05a")],
        "frontieres": ["7.1", "7.2", "7.3", "7.4", "7.13", "7.14", "7.19", "7.20", "7.21", "7.25", "7.26", "7.28",
                       "7.R3"],
        "mymath": {"module": "vectors.py",
                   "functions": ["norm_p", "cosine_similarity", "project_onto_line", "centroid", "sum_sq_distances_to",
                                 "side_of_hyperplane", "distance_to_hyperplane"]},
        "reading_minutes": 180,
        "flashcards": 24,
        "notes": "Évités (règle de partage) : les œufs, les manchots, les deux lunes et les autres données de "
                 "workbookIA 7, et les mini-exemples de sa fiche (centroïdes (1, 1) et (3, 5) avec x = (6, 0) ; "
                 "a = (1, 2) et b = (3, 4) ; les points 0, 2, 3, 9, 11, 12 ; 0, 1, 5, 9 ; les clusters {0, 1, 2} et "
                 "{6, 7} ; la pureté 40 Adélie et 10 Chinstrap). Frontières : la densité n / bᵈ et le nombre "
                 "d'échantillons nécessaires (7.4), la boule dans le cube (7.6), l'hyper-orange (7.5), l'écorce "
                 "1 − (1 − ε)ᵈ, la distance au plus proche voisin et la concentration des distances (7.19, 7.20) : "
                 "M07 étudie la diagonale du cube, l'angle de deux vecteurs aléatoires (sans calculer la variance de leur "
                 "produit scalaire, ∂ B3.6) et la norme d'un vecteur gaussien (M07.13, qui démontre la variance de Z² "
                 "admise en M02c), d'où la concentration des distances entre deux vecteurs gaussiens, sans plus proche "
                 "voisin ni cube uniforme ; pas de changement d'échelle de (w, b) en entretien (10.3 f, 13.4 i) ; pas de choix de k (7.Q8, 7.E3), et M07.E1 ne reprend pas 0B.E2 (cosinus ou distance "
                 "euclidienne) ; la médiatrice comme frontière du centroïde le plus proche (7.7) est énoncée, pas "
                 "démontrée ; pas d'itération complète de k-means (7.3) : M07 démontre que l'inertie ne peut pas "
                 "augmenter et place un seul dépôt au barycentre ; pas de développement de ‖a − b‖² (7.R3) ni de "
                 "distances par paires vectorisées (7.13). Les distances par paires, le centroïde le plus proche, "
                 "k-means, k-means++ et la silhouette sont les fonctions de `mylearn` en workbookIA 7 ; `vectors` "
                 "écrit les briques (normes, cosinus, projection, barycentre, inertie, hyperplans). Coût : environ "
                 "15 h au lieu de 14 (19 notions).",
        "exercises": [
            ("M07.Q1", "🧠", 1, 4, "Vecteurs, coordonnées et one-hot", "§1", "E"),
            ("M07.Q2", "🧠", 1, 4, "Ce que mesure un produit scalaire", "§2", "E"),
            ("M07.Q3", "🧠", 1, 4, "Trois normes, trois boules unités", "§3", "E"),
            ("M07.Q4", "🧠", 1, 4, "Similarité cosinus : vrai ou faux", "§4", "E"),
            ("M07.Q5", "🧠", 1, 4, "Hyperplans : vecteur normal et côtés", "§5", "E"),
            ("M07.Q6", "🧠", 1, 4, "Moyenne, barycentre et inertie", "§6", ""),
            ("M07.Q7", "🧠", 1, 4, "Intuitions de la grande dimension", "§7", "E"),
            ("M07.R1", "🔁", 1, 5, "Produit scalaire et angle dans le plan (R9)", "§2", "E"),
            ("M07.R2", "🔁", 1, 5, "Moyenne et variance empiriques (M02c)", "§6", "E"),
            ("M07.R3", "🔁", 1, 5, "Gradient et point critique (M05b)", "§6", ""),
            ("M07.1", "✏️", 1, 15, "Combinaisons linéaires et vecteurs one-hot dans ℝ⁴", "§1", "E"),
            ("M07.2", "✏️", 1, 15, "Produits scalaires, ‖u + v‖² et l'identité du parallélogramme", "§2", "E"),
            ("M07.3", "✏️", 1, 20, "Normes L1, L2, L∞ et distances entre trois profils", "§3", "E"),
            ("M07.4", "✏️", 2, 20, "Similarité cosinus entre des profils d'écoute musicale", "§4", "E"),
            ("M07.5", "✏️", 2, 20, "Projeter sur une droite : composante parallèle et composante orthogonale", "§4",
             "E"),
            ("M07.6", "✏️", 2, 20, "Un plan de ℝ³ : vecteur normal, côté, distance signée", "§5", "E"),
            ("M07.7", "✏️", 1, 15, "Un score linéaire w · x + b : calculer, décider, lire le vecteur normal", "§2 §5",
             "E"),
            ("M07.8", "✏️", 2, 20, "Centroïde, inertie et formule de König-Huygens", "§6", "E"),
            ("M07.9", "✏️", 2, 15, "Où placer un dépôt : le barycentre pondéré des livraisons", "§6", ""),
            ("M07.10", "✏️", 2, 15, "La silhouette d'un point, à la main, en dimension 2", "§6", ""),
            ("M07.11", "✏️", 2, 15, "k-means++ : des probabilités de tirage proportionnelles à D²", "§6", ""),
            ("M07.12", "✏️", 1, 15, "La diagonale du cube unité et son angle avec les axes, quand d grandit", "§7",
             "E"),
            ("M07.13", "✏️", 2, 15, "La norme d'un vecteur gaussien : espérance, variance et concentration", "§7",
             ""),
            ("M07.14", "∂", 2, 25, "L'inégalité de Cauchy-Schwarz, par le discriminant", "§4", "E"),
            ("M07.15", "∂", 2, 20, "L'inégalité triangulaire pour L2, L1 et L∞", "§3 §4", ""),
            ("M07.16", "∂", 2, 20, "La moyenne minimise la somme des carrés des distances, en dimension n", "§6", "E"),
            ("M07.17", "∂", 2, 20, "La distance d'un point à un hyperplan vaut |w · x + b| / ‖w‖", "§5", "E"),
            ("M07.18", "∂", 3, 20, "Les deux étapes de k-means font baisser l'inertie, ou la laissent égale", "§6", ""),
            ("M07.19", "🔗", 1, 15, "Pont : changer l'unité d'une feature change le plus proche voisin", "§3", "E"),
            ("M07.20", "📖", 2, 30, "MML §3.1 et §3.2.1 : normes et produit scalaire, en anglais", "§2 §3", ""),
            ("M07.21", "📖", 2, 30, "MML §3.3 et §3.4 : longueurs, distances, angles et orthogonalité", "§4", ""),
            ("M07.22", "🧮", 1, 10, "Fermi : la mémoire d'un million d'embeddings", "§1", ""),
            ("M07.23", "🗣️", 1, 10, "Expliquer la similarité cosinus à quelqu'un qui a fait le lycée", "§4", "E"),
            ("M07.E1", "💼", 1, 10, "Que représente géométriquement le vecteur de poids d'un modèle linéaire ?",
             "§2 §5", ""),
            ("M07.24", "🔨", 1, 20, "Normes Lp et similarité cosinus", "§3 §4", "E m:norm_p,cosine_similarity"),
            ("M07.25", "🔨", 1, 15, "La projection sur une droite", "§4", "E m:project_onto_line"),
            ("M07.26", "🔨", 1, 20, "Barycentre et somme des carrés des distances", "§6",
             "E m:centroid,sum_sq_distances_to"),
            ("M07.27", "🔨", 1, 20, "Côté d'un hyperplan et distance à un hyperplan", "§5",
             "E m:side_of_hyperplane,distance_to_hyperplane p:M07.24"),
            ("M07.28", "📦", 1, 10, "`np.linalg.norm` (ord = 1, 2, inf) et `scipy.spatial.distance` contre tes "
             "fonctions", "§3", ""),
            ("M07.29", "🔮", 1, 10, "Prédire : l'angle de deux vecteurs tirés au hasard en dimension 1 000", "§7", "E"),
            ("M07.30", "🔬", 2, 20, "La norme d'un vecteur gaussien se concentre autour de √d", "§7", ""),
            ("M07.31", "🔬", 2, 20, "Médiane ou moyenne : le centre qui minimise les distances L1 ou leurs carrés, "
             "face à des points aberrants", "§3 §6", ""),
            ("M07.32", "🎨", 1, 20, "Les boules unités L1, L2, L∞ et Lp dans le plan", "§3", ""),
            ("M07.33", "🐛", 1, 15, "Chasse à l'erreur : une distance sans racine, un cosinus mal normalisé, une "
             "projection sur un vecteur non unitaire", "§3 §4", ""),
            ("M07.34", "🛠️", 1, 15, "Les normes de toutes les lignes d'un tableau : axis, keepdims et broadcasting",
             "§1 §3", ""),
            ("M07.35", "🏆", 3, 30, "Défi : le point qui minimise la somme des distances (non au carré) à 60 villes, à "
             "0,1 % près", "§3 §6", ""),
        ],
    },
    {
        "id": "M08", "dir": "m08_tests", "hours": 12.1, "generation_sessions": 1, "mml": ["§8.6"],
        "summary": "Les tests statistiques : hypothèses, statistique de test, p-valeur, test binomial exact, test par "
                   "permutation, erreurs de type I et II, puissance, intervalles d'une proportion (Wald, Wilson) et "
                   "d'une différence appariée (Student), comparaisons multiples (Bonferroni) ; puis la sélection de "
                   "modèle (AIC, BIC, facteur de Bayes) et la validation croisée vue comme une estimation bruitée.",
        "objectives": [
            "Poser une hypothèse nulle et une alternative, choisir une statistique et interpréter une p-valeur sans "
            "contresens.",
            "Calculer à la main la p-valeur exacte d'un test binomial et d'un petit test par permutation.",
            "Calculer les erreurs de type I et II et la puissance d'un test, et dimensionner un échantillon.",
            "Calculer un intervalle de Wald et de Wilson pour une proportion, et un intervalle de Student pour des "
            "mesures appariées.",
            "Corriger des comparaisons multiples par Bonferroni et en démontrer la garantie.",
            "Comparer des modèles par l'AIC, le BIC et un facteur de Bayes.",
        ],
        "sections": [("§1", "Le raisonnement d'un test : hypothèses, statistique, p-valeur"),
                     ("§2", "Un test exact : le test binomial"),
                     ("§3", "Le test par permutation"),
                     ("§4", "Erreurs de type I et II, puissance, taille d'échantillon"),
                     ("§5", "Intervalles : une proportion (Wald, Wilson), une différence appariée (Student)"),
                     ("§6", "Comparaisons multiples : Bonferroni"),
                     ("§7", "Choisir un modèle : AIC, BIC, facteur de Bayes, validation croisée")],
        "teaches": ["hypothèse nulle et alternative", "statistique de test", "p-valeur", "test binomial exact",
                    "test par permutation", "erreurs de type I et II", "puissance d'un test",
                    "taille d'échantillon", "intervalle d'une proportion : Wald et Wilson",
                    "intervalle d'une accuracy", "loi de Student (aperçu) et mesures appariées",
                    "comparaisons multiples (Bonferroni)", "comparer deux modèles (principe)",
                    "sélection de modèle : AIC, BIC, facteur de Bayes (aperçu)",
                    "validation croisée : principe statistique", "importance par permutation (principe)",
                    "évaluation sur plusieurs graines"],
        "requires": [("dénombrement, combinaisons", "R8"), ("loi binomiale, loi normale, Φ", "M02b"),
                     ("erreur type, intervalle de confiance, bootstrap", "M02c"), ("vraisemblance, Bayes", "M04"),
                     ("logarithmes", "R6"), ("polynôme du second degré", "R3")],
        "frontieres": ["8.1", "8.2", "8.4", "8.5", "8.23", "8.25", "8.26", "8.E2", "8.E3"],
        "mymath": {"module": "testing.py",
                   "functions": ["binomial_test", "permutation_test", "proportion_ci", "paired_difference_ci",
                                 "bonferroni", "aic_bic"]},
        "reading_minutes": 150,
        "flashcards": 22,
        "notes": "Évités (règle de partage) : les manchots, l'accuracy de 0,92 sur 250 exemples et la taille de test "
                 "minimale (8.4), les scores de deux modèles sur cinq folds (8.5), la loi du maximum de K scores "
                 "(∂ 8.6), les cinq désaccords (4 contre 1) du mini-exemple de la fiche, la comparaison de deux "
                 "modèles sur le même jeu de test par leurs désaccords et le bootstrap apparié (8.26, 8.E2 : M08 "
                 "définit la p-valeur et teste d'autres situations), la sélection de features sur du bruit avant la "
                 "validation croisée (8.25), le contexte « 91,2 % contre 90,5 % ». M08 enseigne le test binomial, le "
                 "test par permutation à deux échantillons (on rebat la répartition des valeurs entre les deux groupes), Wald et Wilson, "
                 "Student pour des mesures appariées (pas des folds), Bonferroni et l'AIC et le BIC, dans d'autres "
                 "cadres (temps de calcul, mesures physiques, taux de clics). La loi de Student n'est vue qu'en "
                 "aperçu (une table, ou `scipy.stats.t.ppf`). Coût : environ 12 h au lieu de 10 (17 notions).",
        "exercises": [
            ("M08.Q1", "🧠", 1, 4, "Ce qu'une p-valeur est, et ce qu'elle n'est pas", "§1", "E"),
            ("M08.Q2", "🧠", 1, 4, "Unilatéral ou bilatéral ?", "§2", ""),
            ("M08.Q3", "🧠", 1, 4, "Permuter quoi, et sous quelle hypothèse ?", "§3", "E"),
            ("M08.Q4", "🧠", 1, 4, "Erreurs de type I et II, puissance : associer", "§4", "E"),
            ("M08.Q5", "🧠", 1, 4, "Comparaisons multiples : vrai ou faux", "§6", "E"),
            ("M08.Q6", "🧠", 1, 4, "AIC, BIC, facteur de Bayes : qui pénalise quoi ?", "§7", ""),
            ("M08.R1", "🔁", 1, 5, "La loi binomiale (M02b)", "§2", "E"),
            ("M08.R2", "🔁", 1, 5, "L'intervalle de confiance d'une moyenne (M02c)", "§5", "E"),
            ("M08.R3", "🔁", 1, 5, "Vraisemblance et log-vraisemblance (M04)", "§7", ""),
            ("M08.1", "✏️", 1, 20, "Un test binomial à la main : un algorithme de compression est-il plus rapide sur "
             "douze fichiers ?", "§1 §2", "E"),
            ("M08.2", "✏️", 2, 25, "Un test par permutation exhaustif : deux groupes de trois mesures, vingt "
             "répartitions", "§3", "E"),
            ("M08.3", "✏️", 2, 20, "Erreur de type I, erreur de type II et puissance d'un test binomial", "§4", "E"),
            ("M08.4", "✏️", 2, 20, "Combien d'observations pour une puissance de 80 % ? (approximation normale)",
             "§4", ""),
            ("M08.5", "✏️", 2, 20, "L'intervalle d'une proportion : Wald contre Wilson, avec peu de succès", "§5",
             "E"),
            ("M08.6", "✏️", 2, 20, "L'intervalle de Student d'une différence appariée : un serveur avant et après une "
             "mise à jour", "§5", "E"),
            ("M08.7", "✏️", 1, 15, "Vingt tests au seuil de 5 % : les faux positifs attendus, puis Bonferroni", "§6",
             "E"),
            ("M08.8", "✏️", 1, 15, "L'AIC et le BIC de deux modèles, à partir de leurs log-vraisemblances", "§7", "E"),
            ("M08.9", "✏️", 2, 15, "Un facteur de Bayes entre deux taux de clics", "§7", ""),
            ("M08.10", "∂", 2, 20, "Sous H0, une p-valeur continue suit la loi uniforme", "§1 §4", ""),
            ("M08.11", "∂", 2, 20, "L'inégalité de Boole et la garantie de Bonferroni, sans hypothèse d'indépendance",
             "§6", "E"),
            ("M08.12", "∂", 3, 25, "L'intervalle de Wilson, en inversant le test d'une proportion", "§5", ""),
            ("M08.13", "🔗", 1, 15, "Pont : l'importance d'une feature par permutation, sur un petit tableau", "§3",
             ""),
            ("M08.14", "📖", 2, 30, "MML §8.6 : validation croisée imbriquée, sélection bayésienne de modèle et facteur "
             "de Bayes", "§7", ""),
            ("M08.15", "🗣️", 1, 10, "Expliquer une p-valeur sans dire « la probabilité que H0 soit vraie »", "§1",
             "E"),
            ("M08.E1", "💼", 1, 10, "« Votre test donne p = 0,03 : que concluez-vous, et que dites-vous à l'équipe "
             "produit ? »", "§1 §4", ""),
            ("M08.16", "🔨", 1, 15, "Le test binomial exact", "§2", "E m:binomial_test"),
            ("M08.17", "🔨", 2, 25, "Le test par permutation à deux échantillons", "§3", "E m:permutation_test"),
            ("M08.18", "🔨", 1, 20, "Les intervalles de Wilson et de Student", "§5",
             "E m:proportion_ci,paired_difference_ci"),
            ("M08.19", "🔨", 1, 10, "Bonferroni, l'AIC et le BIC", "§6 §7", "m:bonferroni,aic_bic"),
            ("M08.20", "📦", 1, 15, "`scipy.stats.binomtest`, `permutation_test` et `ttest_rel` contre tes fonctions",
             "§2 §3 §5", ""),
            ("M08.21", "🔮", 1, 10, "Prédire : sous H0, quelle part de 1 000 p-valeurs tombe sous 0,05 ?", "§1 §4",
             "E"),
            ("M08.22", "🔬", 2, 25, "La puissance d'un test par permutation, selon l'effet et la taille des groupes",
             "§4", ""),
            ("M08.23", "🎨", 1, 15, "La loi de la statistique sous H0, et la p-valeur comme une aire", "§1 §3", ""),
            ("M08.24", "🐛", 1, 15, "Chasse à l'erreur : une p-valeur nulle, un test unilatéral choisi après coup, "
             "Bonferroni à l'envers", "§3 §6", ""),
            ("M08.25", "🛠️", 1, 15, "Tester un test : un pytest qui vérifie l'uniformité des p-valeurs sous H0",
             "§1", ""),
            ("M08.26", "🏆", 3, 25, "Défi : retrouver les trois vraies features parmi cinquante, avec au plus un faux "
             "positif", "§6", ""),
        ],
    },
    {
        "id": "M09a", "dir": "m09a_matrices", "hours": 16.7, "generation_sessions": 2,
        "mml": ["§2.1", "§2.2", "§2.3"],
        "summary": "Les matrices et les systèmes linéaires : formes, produit matrice-vecteur et produit matriciel, "
                   "produit de Hadamard, transposée et matrice XᵀX, systèmes, pivot de Gauss et forme échelonnée "
                   "réduite, inverse, premier contact avec le rang ; la passe avant d'un réseau écrite comme un "
                   "produit matriciel.",
        "objectives": [
            "Lire un tableau de données comme une matrice et prévoir la forme de chaque produit.",
            "Calculer des produits matrice-vecteur et matriciels à la main, sous leurs deux lectures, et en compter "
            "le coût.",
            "Écrire une couche Z = XW + b et un embedding comme des produits matriciels.",
            "Appliquer les règles de la transposée et démontrer (AB)ᵀ = BᵀAᵀ.",
            "Résoudre un système par le pivot de Gauss et décrire toutes ses solutions.",
            "Calculer une inverse, un rang, et relier le rang au nombre de solutions.",
        ],
        "sections": [("§1", "Matrices : un tableau de données est une matrice"),
                     ("§2", "Le produit matrice-vecteur : deux lectures"),
                     ("§3", "Le produit matriciel, le produit de Hadamard et Z = XW + b"),
                     ("§4", "La transposée et la matrice XᵀX"),
                     ("§5", "Systèmes linéaires : zéro, une ou une infinité de solutions"),
                     ("§6", "Le pivot de Gauss et la forme échelonnée réduite"),
                     ("§7", "L'inverse d'une matrice"),
                     ("§8", "Le rang : premier contact")],
        "teaches": ["matrices, formes", "produit matrice-vecteur et matriciel", "coût d'un produit matriciel",
                    "produit de Hadamard", "transposée et ses règles", "systèmes linéaires",
                    "pivot de Gauss, forme échelonnée et forme échelonnée réduite", "inverse d'une matrice",
                    "rang (premier contact)", "matrice identité, matrices diagonales",
                    "un dataset est une matrice : opérer par ligne, par colonne, élément par élément",
                    "Z = XW + b : la convention des poids", "un embedding est un produit one-hot × matrice"],
        "requires": [("systèmes 2 × 2, calcul littéral", "R2"), ("Σ", "R4"),
                     ("vecteurs de ℝⁿ, produit scalaire, one-hot", "M07"), ("moyenne, écart-type", "M02c")],
        "frontieres": ["9.16", "9.17", "10.14", "10.15"],
        "mymath": {"module": "matrices.py",
                   "functions": ["matmul", "transpose", "rref", "rank", "solve", "inverse"]},
        "reading_minutes": 210,
        "flashcards": 26,
        "notes": "Évités (règle de partage) : le tempo de la boutique et California (workbookIA 9), le mini-exemple "
                 "(0 ; 1), (1 ; 2), (2 ; 4) de sa fiche, les poids nommés AD, BE… et la conversion vers PyTorch "
                 "(workbookIA 10.14, 10.15). M09a ne forme pas les équations normales (M09b). Z = XW + b suit la "
                 "convention de `mylearn` (W de forme (n_in, n_out)) et signale celle de PyTorch. `mymath` écrit "
                 "`rref` (la forme réduite, unique, donc testable contre SymPy) au lieu de `row_echelon` prévu. Deux "
                 "sessions de génération : §1 à §4 (matrices et produits), puis §5 à §8 (systèmes, Gauss, inverse, "
                 "rang).",
        "exercises": [
            ("M09a.Q1", "🧠", 1, 4, "Formes : ce qui se multiplie et ce qui ne se multiplie pas", "§1 §3", "E"),
            ("M09a.Q2", "🧠", 1, 4, "Le produit matrice-vecteur, deux lectures", "§2", "E"),
            ("M09a.Q3", "🧠", 1, 4, "Produit matriciel : vrai ou faux", "§3", "E"),
            ("M09a.Q4", "🧠", 1, 4, "Hadamard ou produit matriciel ?", "§3", ""),
            ("M09a.Q5", "🧠", 1, 4, "Les règles de la transposée", "§4", "E"),
            ("M09a.Q6", "🧠", 1, 4, "Combien de solutions ?", "§5", "E"),
            ("M09a.Q7", "🧠", 1, 4, "Les opérations permises sur les lignes", "§6", "E"),
            ("M09a.Q8", "🧠", 1, 4, "Inverse et rang", "§7 §8", "E"),
            ("M09a.R1", "🔁", 1, 5, "Les systèmes 2 × 2 (R2)", "§5", "E"),
            ("M09a.R2", "🔁", 1, 5, "Produit scalaire et normes (M07)", "§2", "E"),
            ("M09a.R3", "🔁", 1, 5, "Moyenne et écart-type empiriques (M02c)", "§1", ""),
            ("M09a.1", "✏️", 1, 15, "Un tableau de données vu comme une matrice : forme, lignes, colonnes, moyennes",
             "§1", "E"),
            ("M09a.2", "✏️", 1, 15, "Le produit matrice-vecteur, par les lignes puis par les colonnes", "§2", "E"),
            ("M09a.3", "✏️", 1, 20, "Produits matriciels à la main : formes compatibles et calculs", "§3", "E"),
            ("M09a.4", "✏️", 2, 15, "Le coût d'un produit, et l'ordre des parenthèses dans ABC", "§3", ""),
            ("M09a.5", "✏️", 1, 20, "Une couche dense Z = XW + b à la main : deux exemples, trois entrées, deux "
             "sorties", "§3", "E"),
            ("M09a.6", "✏️", 1, 10, "Un embedding : une ligne one-hot fois une matrice", "§3", ""),
            ("M09a.7", "✏️", 1, 15, "Transposées de produits, et la matrice symétrique XᵀX", "§4", "E"),
            ("M09a.8", "✏️", 2, 25, "Le pivot de Gauss sur un système 3 × 3 à solution unique", "§5 §6", "E"),
            ("M09a.9", "✏️", 2, 25, "Un système sans solution, un système à une infinité de solutions", "§5 §6", "E"),
            ("M09a.10", "✏️", 2, 20, "La forme échelonnée réduite d'une matrice 3 × 4 et la solution générale", "§6",
             ""),
            ("M09a.11", "✏️", 1, 15, "L'inverse d'une matrice 2 × 2, par la formule, puis vérifiée", "§7", "E"),
            ("M09a.12", "✏️", 2, 25, "L'inverse d'une matrice 3 × 3 par Gauss-Jordan", "§7", ""),
            ("M09a.13", "✏️", 2, 20, "Le rang de quatre matrices, et les colonnes redondantes", "§8", "E"),
            ("M09a.14", "✏️", 2, 20, "Mettre un problème en système : trois engrais pour trois nutriments", "§5", ""),
            ("M09a.15", "∂", 1, 15, "(AB)ᵀ = BᵀAᵀ, coefficient par coefficient", "§4", "E"),
            ("M09a.16", "∂", 2, 15, "L'inverse est unique, et (AB)⁻¹ = B⁻¹A⁻¹", "§7", ""),
            ("M09a.17", "∂", 2, 15, "Deux solutions distinctes entraînent une infinité de solutions", "§5", "E"),
            ("M09a.18", "∂", 2, 20, "Une matrice dont une colonne combine les autres n'est pas inversible", "§7 §8",
             ""),
            ("M09a.19", "🔗", 1, 15, "Pont : une passe avant à deux couches, deux produits matriciels et leurs formes",
             "§3", "E"),
            ("M09a.20", "🔗", 2, 15, "Pont : centrer et réduire un tableau en écriture matricielle", "§1 §3", ""),
            ("M09a.21", "📖", 2, 30, "MML §2.1 et §2.2 : systèmes et matrices, en anglais", "§1 §3 §5", ""),
            ("M09a.22", "📖", 2, 30, "MML §2.3 : résoudre un système, la forme échelonnée et le « Minus-1 trick »",
             "§6 §8", ""),
            ("M09a.23", "🧮", 1, 10, "Fermi : combien de multiplications pour une passe avant sur un million d'images ?",
             "§3", ""),
            ("M09a.24", "🗣️", 1, 10, "Expliquer pourquoi on ne calcule pas l'inverse pour résoudre un système", "§7",
             "E"),
            ("M09a.E1", "💼", 1, 10, "« Combien coûte un produit matriciel, et pourquoi les GPU l'accélèrent-ils ? »",
             "§3", ""),
            ("M09a.25", "🔨", 1, 20, "Le produit matriciel et la transposée", "§3 §4", "E m:matmul,transpose"),
            ("M09a.26", "🔨", 2, 35, "La forme échelonnée réduite et le rang", "§6 §8", "E m:rref,rank"),
            ("M09a.27", "🔨", 2, 30, "Résoudre un système par le pivot de Gauss", "§6", "E m:solve"),
            ("M09a.28", "🔨", 1, 20, "L'inverse par Gauss-Jordan", "§7", "m:inverse p:M09a.26"),
            ("M09a.29", "📦", 1, 15, "`@`, `*`, `.T`, `np.linalg.solve`, `matrix_rank` et `sympy.Matrix.rref` contre "
             "tes fonctions", "§3 §6 §8", "E"),
            ("M09a.30", "🔮", 1, 10, "Prédire la forme du résultat : `@`, `*` et broadcasting", "§1 §3", "E"),
            ("M09a.31", "🔬", 2, 20, "Le temps d'un produit matriciel en fonction de n : une pente de 3 en échelle "
             "log-log", "§3", ""),
            ("M09a.32", "🔬", 2, 20, "Pourquoi le pivot partiel : un petit pivot et les arrondis", "§6", ""),
            ("M09a.33", "🎨", 1, 20, "Une matrice 2 × 2 comme transformation du plan : la grille et le carré unité",
             "§2 §3", ""),
            ("M09a.34", "🐛", 1, 15, "Chasse à l'erreur : `*` au lieu de `@`, une transposée oubliée, un pivot nul",
             "§3 §6", ""),
            ("M09a.35", "🛠️", 1, 15, "Tester une propriété : un pytest pour (AB)ᵀ = BᵀAᵀ sur des matrices "
             "aléatoires", "§4", ""),
            ("M09a.36", "🏆", 3, 30, "Défi : un système 400 × 400 résolu par ton `solve`, à 1e−9 près de NumPy, en "
             "moins d'une seconde", "§6", ""),
        ],
    },
    {
        "id": "M09b", "dir": "m09b_moindres_carres", "hours": 17.0, "generation_sessions": 2,
        "mml": ["§5.5", "§8.1", "§8.2", "§9.1", "§9.2"],
        "summary": "La régression linéaire par les moindres carrés : risque empirique, MSE, MAE, Huber et R², "
                   "gradients de aᵀw et de wᵀAw, équations normales, projection et matrice chapeau, features "
                   "polynomiales, régularisation ridge (et ridge vue comme MAP), principe du lasso, régression vue "
                   "comme maximum de vraisemblance, décomposition biais-variance, aperçu de la double descente.",
        "objectives": [
            "Calculer les losses d'une régression (MSE, RMSE, MAE, Huber) et un R², et décomposer la variance.",
            "Calculer les gradients de aᵀw, de wᵀAw et de ‖y − Xw‖², et en déduire les équations normales en "
            "dimension p.",
            "Interpréter les moindres carrés comme une projection, avec la matrice chapeau.",
            "Compter les colonnes de features polynomiales.",
            "Résoudre un problème ridge, démontrer qu'il a toujours une solution et le relier à un prior gaussien.",
            "Démontrer que le bruit gaussien mène aux moindres carrés, et décomposer une erreur en biais², variance "
            "et bruit.",
        ],
        "sections": [("§1", "Le problème : modèle linéaire, risque empirique et losses (MSE, MAE, Huber, R²)"),
                     ("§2", "Calcul matriciel minimal : les gradients de aᵀw, wᵀAw et ‖y − Xw‖²"),
                     ("§3", "Les équations normales, la projection et la matrice chapeau"),
                     ("§4", "Features polynomiales : compter les monômes"),
                     ("§5", "La régression ridge, et ridge vue comme un MAP"),
                     ("§6", "Le lasso : le principe de la parcimonie"),
                     ("§7", "La régression comme maximum de vraisemblance"),
                     ("§8", "Biais, variance et double descente")],
        "teaches": ["risque empirique", "gradients de aᵀw et de wᵀAw (calcul matriciel minimal)", "moindres carrés",
                    "équations normales", "projection et matrice chapeau",
                    "features polynomiales : combien de monômes (combinaisons avec répétition)",
                    "régularisation ridge", "ridge comme MAP", "lasso (principe)", "MSE, MAE, loss de Huber, R², RMSE",
                    "décomposition biais-variance", "overfitting et underfitting vus par le biais et la variance",
                    "régression comme maximum de vraisemblance", "double descente (aperçu)",
                    "pénalité L2 et weight decay"],
        "requires": [("matrices, transposée, inverse, pivot de Gauss, rang", "M09a"),
                     ("normes, produit scalaire, projection sur une droite", "M07"), ("gradient, point critique", "M05b"),
                     ("vraisemblance, MAP", "M04"), ("loi normale", "M02b"),
                     ("biais et variance d'un estimateur", "M02c"), ("combinaisons", "R8")],
        "frontieres": ["9.1", "9.4", "9.7", "9.14", "9.15", "9.16", "9.17", "9.19", "9.23", "9.24", "9.26", "9.E3"],
        "mymath": {"module": "linreg.py",
                   "functions": ["normal_equations", "solve_least_squares", "hat_matrix", "residual_decomposition",
                                 "count_monomials", "huber_loss"]},
        "reading_minutes": 210,
        "flashcards": 26,
        "notes": "Frontières : les moindres carrés d'une droite par dérivées partielles (9.2), ridge (9.3) et lasso "
                 "(9.6) en dimension 1 ne sont pas démontrés ici : M09b travaille en dimension p, par les gradients "
                 "matriciels, et énonce le seuillage doux sans le dériver. Évités : le tempo de la boutique, "
                 "California, les mini-exemples de la fiche de workbookIA 9 (les points (0 ; 1), (1 ; 2), (2 ; 4) ; "
                 "les cibles 1, 4, 6 et les prédictions 2, 4, 3 ; Σxy = 6 et Σx² = 4 ; S(1,8 ; 0,5) ; les prédictions "
                 "1, 2 et 4 du biais-variance ; les dénombrements 9 pour p = 3 et d = 2, 285 pour p = 10 et d = 3), "
                 "la grille 3 × 3 de droites (9.7), les MSE et R² sur cinq points (9.1), le tableau de prédictions de "
                 "9.4. La régression bayésienne (MML §9.3) se lit en M25a, la projection sur un sous-espace (MML "
                 "§9.4) en M12b. MSE, MAE, R², features polynomiales, LinearRegression, Ridge, Lasso, soft_threshold "
                 "et la décomposition biais-variance sont les fonctions de `mylearn` en workbookIA 9 ; `linreg` écrit "
                 "les briques (équations normales, ridge qui pénalise tous les coefficients, matrice chapeau, sommes "
                 "de carrés, nombre de monômes, Huber). Deux sessions de génération : §1 à §4, puis §5 à §8.",
        "exercises": [
            ("M09b.Q1", "🧠", 1, 4, "MSE, RMSE, MAE, R² : ce que mesure chacune", "§1", "E"),
            ("M09b.Q2", "🧠", 1, 4, "Gradients matriciels : associer chaque fonction à son gradient", "§2", "E"),
            ("M09b.Q3", "🧠", 1, 4, "Équations normales : quand la solution est-elle unique ?", "§3", "E"),
            ("M09b.Q4", "🧠", 1, 4, "Linéaire en x ou linéaire en w ?", "§4", "E"),
            ("M09b.Q5", "🧠", 1, 4, "Ridge : vrai ou faux sur la pénalité L2", "§5", "E"),
            ("M09b.Q6", "🧠", 1, 4, "Lasso ou ridge : qui annule des poids ?", "§6", ""),
            ("M09b.Q7", "🧠", 1, 4, "Bruit gaussien et moindres carrés", "§7", "E"),
            ("M09b.Q8", "🧠", 1, 4, "Biais, variance, bruit : ce qui change quand le modèle se complique", "§8", "E"),
            ("M09b.R1", "🔁", 1, 5, "Le pivot de Gauss et l'inverse (M09a)", "§3", "E"),
            ("M09b.R2", "🔁", 1, 5, "Maximum de vraisemblance et MAP (M04)", "§5 §7", "E"),
            ("M09b.R3", "🔁", 1, 5, "Gradient et point critique (M05b)", "§2", "E"),
            ("M09b.1", "✏️", 1, 15, "MSE, RMSE, MAE et loss de Huber de quatre résidus", "§1", "E"),
            ("M09b.2", "✏️", 1, 20, "La décomposition SCT = SCE + SCR et le R² d'un ajustement donné", "§1 §3", ""),
            ("M09b.3", "✏️", 2, 20, "Les gradients de aᵀw, wᵀAw et ‖y − Xw‖², composante par composante en dimension "
             "2", "§2", "E"),
            ("M09b.4", "✏️", 2, 20, "Les équations normales d'un modèle à deux features, sans ordonnée à l'origine",
             "§3", "E"),
            ("M09b.5", "✏️", 2, 20, "La colonne de 1 : l'ordonnée à l'origine et des résidus de moyenne nulle", "§3",
             "E"),
            ("M09b.6", "✏️", 2, 20, "La matrice chapeau d'un petit tableau : H² = H et sa trace", "§3", ""),
            ("M09b.7", "✏️", 1, 15, "Compter les monômes des features polynomiales", "§4", "E"),
            ("M09b.8", "✏️", 2, 20, "Ridge en dimension 2 : résoudre (XᵀX + λI)w = Xᵀy pour trois valeurs de λ", "§5",
             "E"),
            ("M09b.9", "✏️", 2, 20, "Ridge comme MAP : un prior gaussien et λ = σ²/τ²", "§5 §7", ""),
            ("M09b.10", "✏️", 1, 15, "Les pénalités L1 et L2 de trois vecteurs de poids, et leurs boules", "§6", ""),
            ("M09b.11", "✏️", 2, 20, "La log-vraisemblance gaussienne d'un modèle linéaire et l'estimation de σ²",
             "§7", ""),
            ("M09b.12", "✏️", 2, 20, "L'estimateur rétréci c·x̄ : biais, variance et erreur quadratique", "§8", ""),
            ("M09b.13", "∂", 2, 20, "Le gradient de wᵀAw vaut (A + Aᵀ)w", "§2", "E"),
            ("M09b.14", "∂", 2, 25, "Les équations normales en dimension p, par le gradient", "§2 §3", "E"),
            ("M09b.15", "∂", 2, 20, "Le résidu est orthogonal aux colonnes de X ; H est symétrique et idempotente",
             "§3", ""),
            ("M09b.16", "∂", 2, 20, "XᵀX + λI est inversible pour tout λ > 0", "§5", "E"),
            ("M09b.17", "∂", 2, 20, "Un bruit gaussien mène aux moindres carrés : le maximum de vraisemblance", "§7",
             "E"),
            ("M09b.18", "∂", 3, 25, "La décomposition biais² + variance + bruit, démontrée", "§8", ""),
            ("M09b.19", "∂", 3, 25, "Le nombre de monômes de degré au plus d en p variables : C(p + d, d)", "§4", ""),
            ("M09b.20", "🔗", 1, 15, "Pont : la loss d'un modèle linéaire et son gradient pour un batch, prêts pour la "
             "descente de gradient", "§2", "E"),
            ("M09b.21", "🔗", 1, 15, "Pont : pourquoi standardiser les colonnes avant ridge", "§5", ""),
            ("M09b.22", "📖", 2, 30, "MML §5.5, §8.1 et §8.2 : identités de gradients et minimisation du risque "
             "empirique", "§1 §2", ""),
            ("M09b.23", "📖", 2, 30, "MML §9.1 et §9.2 : régression linéaire, maximum de vraisemblance et MAP",
             "§3 §5 §7", ""),
            ("M09b.24", "🧮", 1, 10, "Fermi : la taille de XᵀX pour des features polynomiales de degré 3 sur 100 "
             "variables", "§4", ""),
            ("M09b.25", "🗣️", 1, 10, "Expliquer la matrice chapeau : ce que veut dire « projeter y »", "§3", "E"),
            ("M09b.E1", "💼", 1, 10, "« Pourquoi ne pas inverser XᵀX, et que faire si des features sont colinéaires ? »",
             "§3 §5", ""),
            ("M09b.E2", "💼", 1, 10, "« Quel lien entre la régularisation L2 et un prior gaussien ? »", "§5 §7", ""),
            ("M09b.26", "🔨", 1, 25, "Équations normales et résolution, avec ou sans ridge", "§3 §5",
             "E m:normal_equations,solve_least_squares"),
            ("M09b.27", "🔨", 1, 20, "La matrice chapeau et les trois sommes de carrés", "§1 §3",
             "E m:hat_matrix,residual_decomposition p:M09b.26"),
            ("M09b.28", "🔨", 1, 15, "Compter les monômes, et la loss de Huber", "§1 §4", "m:count_monomials,huber_loss"),
            ("M09b.29", "📦", 1, 15, "`np.linalg.lstsq` et scikit-learn contre tes équations normales", "§3", "E"),
            ("M09b.30", "🔮", 1, 10, "Prédire : le R² d'entraînement quand on ajoute une feature de pur bruit",
             "§1 §4", "E"),
            ("M09b.31", "🔬", 2, 20, "Simuler l'estimateur rétréci c·x̄ : le c qui minimise l'erreur quadratique", "§8", ""),
            ("M09b.32", "🔬", 2, 20, "Le conditionnement de XᵀX avec des puissances non standardisées", "§4", ""),
            ("M09b.33", "🎨", 1, 20, "Les lignes de niveau de la loss des moindres carrés en dimension 2, et son "
             "gradient", "§2 §3", ""),
            ("M09b.34", "🐛", 1, 15, "Chasse à l'erreur : XXᵀ au lieu de XᵀX, un gradient de mauvais signe, un R² "
             "sans centrer", "§1 §2 §3", ""),
            ("M09b.35", "🛠️", 1, 15, "Vérifier un gradient matriciel avec SymPy et par différences finies", "§2", ""),
            ("M09b.36", "🏆", 3, 25, "Défi : approcher une fonction par un polynôme de degré au plus 5, avec une "
             "erreur maximale sous 1e−3", "§3 §4", ""),
        ],
    },
    {
        "id": "M10", "dir": "m10_separabilite_convexite", "hours": 8.1, "generation_sessions": 1, "mml": ["§12.1"],
        "summary": "Les ensembles convexes et l'enveloppe convexe, la séparation de deux nuages par un hyperplan, "
                   "l'astuce du biais et la marge géométrique, les récurrences sur une norme, et les fonctions "
                   "d'activation appliquées à un score linéaire : les outils que workbookIA 10 assemble pour le "
                   "perceptron.",
        "objectives": [
            "Reconnaître et démontrer qu'un ensemble est convexe.",
            "Construire l'enveloppe convexe d'un nuage du plan, à la main et en code.",
            "Démontrer que deux nuages séparables ont des enveloppes convexes disjointes, et tester la séparabilité.",
            "Calculer une marge géométrique, et passer d'un hyperplan affine à un hyperplan par l'origine (astuce du "
            "biais).",
            "Borner une suite de normes pas à pas.",
        ],
        "sections": [("§1", "Ensembles convexes"),
                     ("§2", "L'enveloppe convexe"),
                     ("§3", "Séparer deux nuages : séparabilité linéaire, astuce du biais, marge"),
                     ("§4", "Récurrences sur une norme : croissance linéaire contre croissance en √k"),
                     ("§5", "Activations : des fonctions d'une variable appliquées à un score")],
        "teaches": ["ensembles convexes", "fonctions convexes et strictement convexes de plusieurs variables (définition)",
                    "enveloppe convexe", "séparabilité linéaire (enveloppes convexes disjointes)",
                    "astuce du biais (une coordonnée en plus)", "marge géométrique",
                    "inégalités de récurrence sur une norme",
                    "fonctions d'activation : des fonctions d'une variable (rappel R3, R6)"],
        "requires": [("hyperplans, distance à un hyperplan, Cauchy-Schwarz", "M07"), ("produit matriciel", "M09a"),
                     ("raisonnement par récurrence", "R4"), ("sigmoïde, tanh", "R6"), ("fonctions, composition", "R3"),
                     ("convexité d'une fonction", "M05a")],
        "frontieres": ["10.1", "10.2", "10.3", "10.5", "10.6", "10.13", "10.19", "10.23"],
        "mymath": {"module": "convex.py",
                   "functions": ["convex_hull_2d", "is_linearly_separable", "margin_of_separator"]},
        "reading_minutes": 110,
        "flashcards": 16,
        "notes": "Frontières : XOR n'est pas séparable (10.4) et la convergence du perceptron (10.7) sont démontrés en "
                 "workbookIA 10 : M10 démontre l'énoncé général (deux nuages séparables ont des enveloppes convexes "
                 "disjointes) sans l'appliquer aux portes logiques, et enseigne les récurrences sur une norme sur une "
                 "suite quelconque, sans la règle du perceptron ni la borne (R/γ)². Évités : les portes logiques "
                 "(AND, OR, NOT, NAND, XOR), le perceptron et sa règle, les manchots, les chiffres de 20 × 20 pixels ; "
                 "la marge et l'astuce du biais sont vues en géométrie (10.2 et 10.23 restent à workbookIA). "
                 "COMPOSITION : chapitre court (8 h, puis 8,1 h quand l'apprenant simulé a allongé M10.2 et M10.16, "
                 "sans contenu nouveau) : la moitié de la composition, papier d'abord ; pas de 🔬 ni de 📦 (le 🔮 sur le "
                 "théorème de Cover et les deux 🔨 suffisent).",
        "exercises": [
            ("M10.Q1", "🧠", 1, 4, "Convexe ou non ?", "§1", "E"),
            ("M10.Q2", "🧠", 1, 4, "L'enveloppe convexe : vrai ou faux", "§2", "E"),
            ("M10.Q3", "🧠", 1, 4, "Séparable ou non ?", "§3", "E"),
            ("M10.Q4", "🧠", 1, 4, "Marge et astuce du biais", "§3", ""),
            ("M10.R1", "🔁", 1, 5, "Hyperplans et distance à un hyperplan (M07)", "§3", "E"),
            ("M10.R2", "🔁", 1, 5, "L'inégalité de Cauchy-Schwarz (M07)", "§4", "E"),
            ("M10.R3", "🔁", 1, 5, "La sigmoïde et tanh (R6)", "§5", ""),
            ("M10.1", "✏️", 1, 15, "Convexe ou non : segments, demi-plans, intersections", "§1", "E"),
            ("M10.2", "✏️", 1, 20, "L'enveloppe convexe de huit points, à la main", "§2", "E"),
            ("M10.3", "✏️", 2, 20, "Une droite qui sépare deux petits nuages, et sa marge", "§3", "E"),
            ("M10.4", "✏️", 1, 15, "L'astuce du biais : une droite du plan devient un plan de ℝ³ passant par "
             "l'origine", "§3", ""),
            ("M10.5", "✏️", 2, 15, "Borner une norme pas à pas : ‖v_{k+1}‖² ≤ ‖v_k‖² + c", "§4", ""),
            ("M10.6", "∂", 1, 15, "Un demi-espace est convexe, et une intersection de convexes aussi", "§1", "E"),
            ("M10.7", "∂", 2, 20, "Deux nuages séparés par un hyperplan ont des enveloppes convexes disjointes",
             "§2 §3", "E"),
            ("M10.8", "∂", 1, 15, "La marge géométrique ne change pas quand on multiplie (w, b) par un réel positif",
             "§3", ""),
            ("M10.9", "🔗", 1, 15, "Pont : seuil, sigmoïde, tanh et ReLU appliqués à un même score linéaire", "§5",
             "E"),
            ("M10.10", "📖", 2, 20, "MML §12.1 : les hyperplans séparateurs, en anglais", "§3", ""),
            ("M10.11", "🗣️", 1, 10, "Expliquer la convexité et l'enveloppe convexe avec un élastique", "§1 §2", "E"),
            ("M10.E1", "💼", 1, 10, "« Que veut dire « linéairement séparable », et comment le vérifier ? »", "§3", ""),
            ("M10.12", "🔨", 2, 25, "L'enveloppe convexe dans le plan : la chaîne monotone d'Andrew", "§2",
             "E m:convex_hull_2d"),
            ("M10.13", "🔨", 2, 25, "Séparabilité par programmation linéaire, et marge géométrique", "§3",
             "E m:is_linearly_separable,margin_of_separator"),
            ("M10.14", "🔮", 1, 10, "Prédire : n points aux labels tirés au hasard en dimension d sont-ils "
             "séparables ?", "§3", "E"),
            ("M10.15", "🎨", 1, 15, "Deux nuages, leurs enveloppes convexes et un hyperplan séparateur avec sa marge",
             "§2 §3", ""),
            ("M10.16", "🐛", 1, 15, "Chasse à l'erreur : un produit vectoriel de signe inversé, une marge non "
             "normalisée", "§2 §3", ""),
            ("M10.17", "🛠️", 1, 15, "Des tests de propriétés pour l'enveloppe convexe", "§2", ""),
            ("M10.18", "🏆", 3, 20, "Défi : la plus grande marge possible entre deux nuages donnés, à 1 % près",
             "§3", ""),
        ],
    },
    {
        "id": "M11", "dir": "m11_logique_concentration", "hours": 11.5, "generation_sessions": 1, "mml": [],
        "summary": "La logique au service du raisonnement (implication, contraposée, négation, validité, ensembles et "
                   "contre-exemples, induction et ses pièges) ; puis les inégalités de Markov, Tchebychev et Hoeffding, "
                   "le rayon de confiance d'une moyenne, et ce qu'elles disent des bandits : bornes supérieures de "
                   "confiance, ε-greedy, regret, échantillonnage de Thompson.",
        "objectives": [
            "Écrire la contraposée et la négation d'un énoncé, et décider par une table de vérité si un argument est "
            "valide.",
            "Traduire des phrases en inclusions d'ensembles et construire un contre-exemple.",
            "Repérer les pièges d'une induction (taux de base, échantillon biaisé, corrélation).",
            "Démontrer et appliquer les inégalités de Markov et de Tchebychev, et en déduire la loi faible des "
            "grands nombres.",
            "Appliquer l'inégalité de Hoeffding : rayon de confiance et taille d'échantillon.",
            "Expliquer d'où vient le bonus d'une borne supérieure de confiance, et calculer le regret attendu "
            "d'ε-greedy.",
        ],
        "sections": [("§1", "Raisonner juste : implication, contraposée, négation, validité"),
                     ("§2", "Ensembles, diagrammes de Venn et contre-exemples"),
                     ("§3", "L'induction et ses pièges"),
                     ("§4", "L'inégalité de Markov"),
                     ("§5", "L'inégalité de Tchebychev et la loi des grands nombres"),
                     ("§6", "L'inégalité de Hoeffding et le rayon de confiance"),
                     ("§7", "Explorer ou exploiter : bornes supérieures de confiance, ε-greedy, regret, Thompson")],
        "teaches": ["déduction, validité, solidité", "modus ponens, modus tollens et sophismes formels",
                    "ensembles et contre-exemples", "induction et ses pièges", "inégalité de Markov",
                    "inégalité de Tchebychev", "loi faible des grands nombres (démontrée)", "inégalité de Hoeffding",
                    "rayon de confiance d'une moyenne", "bornes supérieures de confiance (UCB, principe)",
                    "ε-greedy", "regret", "échantillonnage de Thompson"],
        "requires": [("propositions, quantificateurs, implication, ensembles, raisonnements", "R4"),
                     ("suites définies par récurrence (l'outil de la moyenne incrémentale)", "R5"), ("exp et ln", "R6"),
                     ("espérance, variance, lois exponentielle et binomiale", "M02b"),
                     ("moyenne empirique, TCL, intervalle de confiance", "M02c"), ("probabilités totales, taux de base", "M03"),
                     ("formule de Bayes, loi Beta a posteriori", "M04")],
        "frontieres": ["11.1", "11.3", "11.4", "11.5", "11.6", "11.7", "11.8", "11.15", "11.20", "11.23", "11.E2"],
        "mymath": {"module": "concentration.py",
                   "functions": ["markov_bound", "chebyshev_bound", "hoeffding_bound", "hoeffding_radius",
                                 "empirical_tail"]},
        "reading_minutes": 150,
        "flashcards": 22,
        "notes": "Frontière : la moyenne incrémentale (11.2) est démontrée par workbookIA ; M11 s'appuie sur les "
                 "suites de R5. Évités (règle de partage) : les syllogismes catégoriques de workbookIA 11 (Barbara, "
                 "les chats carnivores, Socrate, les formes A, E, I, O et leurs règles, les 256 mondes de Venn de "
                 "11.15), le phare (11.5), les pommes mûres (11.6), Holmes, le renforcement et la punition (11.7), le "
                 "bandit à la main de 11.8 et les nombres de la fiche (récompenses 4, 2, 6 ; ε = 0,1 et K = 4, qui "
                 "donnent 0,925 ; UCB avec c = 2 et t = 25 ; les moyennes 0,1, 0,4 et 0,7 du regret ; 48 spams sur "
                 "400). M11 enseigne la logique propositionnelle (tables de vérité, R4) et les ensembles plutôt que "
                 "les syllogismes, et les bandits par leurs outils (bornes, regret attendu, loi d'un tirage Beta), "
                 "sans agent ni boucle de jeu (les fonctions de `mylearn` en workbookIA 11). Pas de 📖 : MML ne "
                 "traite ni la logique ni les inégalités de concentration. Coût : environ 11 h au lieu de 10.",
        "exercises": [
            ("M11.Q1", "🧠", 1, 4, "Réciproque, contraposée, négation", "§1", "E"),
            ("M11.Q2", "🧠", 1, 4, "Un argument valide peut-il avoir une conclusion fausse ?", "§1", "E"),
            ("M11.Q3", "🧠", 1, 4, "Diagrammes de Venn et quantificateurs", "§2", ""),
            ("M11.Q4", "🧠", 1, 4, "Les pièges de l'induction", "§3", "E"),
            ("M11.Q5", "🧠", 1, 4, "Markov ou Tchebychev : quelle borne s'applique ?", "§4 §5", "E"),
            ("M11.Q6", "🧠", 1, 4, "Ce que garantit l'inégalité de Hoeffding, et ce qu'elle suppose", "§6", "E"),
            ("M11.Q7", "🧠", 1, 4, "Explorer ou exploiter : vrai ou faux", "§7", ""),
            ("M11.R1", "🔁", 1, 5, "Implication et contraposée (R4)", "§1", "E"),
            ("M11.R2", "🔁", 1, 5, "Espérance et variance (M02b)", "§4 §5", "E"),
            ("M11.R3", "🔁", 1, 5, "La loi Beta a posteriori (M04)", "§7", ""),
            ("M11.1", "✏️", 1, 20, "Tables de vérité : modus ponens, modus tollens et l'affirmation du conséquent",
             "§1", "E"),
            ("M11.2", "✏️", 1, 15, "Nier des phrases quantifiées sur des modèles et des datasets", "§1", "E"),
            ("M11.3", "✏️", 2, 15, "Des phrases traduites en inclusions d'ensembles, et un contre-exemple", "§2", ""),
            ("M11.4", "✏️", 2, 15, "Une induction trompeuse par oubli du taux de base, recalculée avec Bayes", "§3",
             "E"),
            ("M11.5", "✏️", 1, 15, "Markov : la queue d'une durée positive", "§4", "E"),
            ("M11.6", "✏️", 2, 20, "Tchebychev : combien d'observations pour une moyenne à ± 0,1 ?", "§5", "E"),
            ("M11.7", "✏️", 2, 20, "Hoeffding : rayon de confiance et taille d'échantillon d'une proportion", "§6",
             "E"),
            ("M11.8", "✏️", 2, 20, "Trois bornes pour une même question : Markov, Tchebychev, Hoeffding, et "
             "l'approximation normale", "§4 §5 §6", ""),
            ("M11.9", "✏️", 3, 20, "D'où vient le bonus d'UCB : Hoeffding avec un risque qui décroît avec t",
             "§6 §7", ""),
            ("M11.10", "✏️", 2, 15, "ε-greedy : la loi du bras joué et le regret attendu par pas", "§7", ""),
            ("M11.11", "∂", 1, 15, "L'inégalité de Markov", "§4", "E"),
            ("M11.12", "∂", 2, 20, "Tchebychev à partir de Markov, puis la loi faible des grands nombres", "§5", "E"),
            ("M11.13", "∂", 2, 20, "Avec ε fixé, le regret attendu d'ε-greedy croît au moins linéairement", "§7", ""),
            ("M11.14", "🔗", 1, 15, "Pont : combien d'exemples de test pour connaître une accuracy à ± 2 points, "
             "garanti par Hoeffding ?", "§6", "E"),
            ("M11.15", "⚖️", 2, 20, "Corrélation, causalité et induction : trois titres de presse à démonter", "§3",
             ""),
            ("M11.16", "🗣️", 1, 10, "Expliquer « l'optimisme face à l'incertitude » à partir d'un intervalle de "
             "confiance", "§7", "E"),
            ("M11.E1", "💼", 1, 10, "« À quoi sert l'inégalité de Hoeffding en apprentissage, et que suppose-t-elle ? »",
             "§6", ""),
            ("M11.17", "🔨", 1, 15, "Les bornes de Markov et de Tchebychev", "§4 §5",
             "E m:markov_bound,chebyshev_bound"),
            ("M11.18", "🔨", 1, 15, "La borne et le rayon de Hoeffding", "§6", "E m:hoeffding_bound,hoeffding_radius"),
            ("M11.19", "🔨", 1, 10, "La queue empirique d'un échantillon", "§4", "m:empirical_tail"),
            ("M11.20", "📦", 1, 15, "Les vraies queues d'une loi exponentielle et d'une binomiale (`scipy.stats`) "
             "contre les bornes", "§4 §5 §6", ""),
            ("M11.21", "🔮", 1, 10, "Prédire : laquelle des trois bornes est la plus serrée pour n = 100 ?", "§6", "E"),
            ("M11.22", "🔬", 2, 20, "La fréquence des écarts |x̄ − p| ≥ t comparée à la borne de Hoeffding, quand n "
             "grandit", "§6", ""),
            ("M11.23", "🔬", 2, 15, "La probabilité qu'un tirage d'une loi Beta dépasse celui d'une autre, par "
             "simulation", "§7", ""),
            ("M11.24", "🎨", 1, 15, "Les bornes de Markov, de Tchebychev et de Hoeffding contre la vraie queue, en "
             "échelle log", "§4 §5 §6", ""),
            ("M11.25", "🐛", 1, 15, "Chasse à l'erreur : Markov pour une variable négative, Hoeffding sans bornes, un "
             "rayon sans racine", "§4 §6", ""),
            ("M11.26", "🛠️", 1, 15, "Un test paramétré qui vérifie l'inégalité de Markov sur dix lois", "§4", ""),
            ("M11.27", "🏆", 3, 25, "Défi : la plus petite taille d'échantillon qui garantit une moyenne à ± 0,05 avec "
             "99 %, vérifiée sur une loi défavorable", "§6", ""),
        ],
    },
    {
        "id": "CP2", "dir": "checkpoints/partie_2", "hours": 3.2, "generation_sessions": 1, "mml": [],
        "summary": "Le bilan de la partie II (M07 à M11), juste avant le checkpoint II de workbookIA : un examen blanc "
                   "d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une "
                   "synthèse (carte mentale et fiche d'une page). Pas de mini-projet.",
        "objectives": [
            "Vérifier en temps limité que les notions de la partie II sont acquises.",
            "Construire ta propre synthèse de la partie II.",
        ],
        "sections": [("§1", "Examen blanc"), ("§2", "Synthèse")],
        "teaches": ["révision de la partie II"],
        "requires": [("toute la partie II", "M11")],
        "frontieres": ["7.5", "7.6", "7.7", "8.6", "9.2", "9.3", "9.6", "10.4", "10.7", "11.2"],
        "reading_minutes": 15,
        "flashcards": 0,
        "notes": "Fichiers comme CP1 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, "
                 "03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne "
                 "reprend le checkpoint II de workbookIA (`checkpoints/partie_2/` de workbookIA : un-contre-tous et "
                 "un-contre-un, une itération de k-means, densité et hyper-orange, plan d'évaluation, ridge en "
                 "dimension 1, courbes d'apprentissage, perceptron sur NAND, syllogismes, fuite d'une validation "
                 "croisée, ε-greedy et moyenne incrémentale), qui se fait juste après, ni son mini-projet II "
                 "(California).",
        "exercises": [
            ("CP2.Q1", "🧠", 1, 10, "Dix affirmations sur la partie II : vrai ou faux", "§1", "E"),
            ("CP2.1", "✏️", 2, 10, "Normes, cosinus, projection et distance à un hyperplan", "§1", "E"),
            ("CP2.2", "✏️", 2, 10, "Un test binomial et un intervalle de Wilson", "§1", "E"),
            ("CP2.3", "✏️", 2, 8, "Comparaisons multiples, AIC et BIC", "§1", "E"),
            ("CP2.4", "✏️", 2, 10, "Pivot de Gauss, rang et inverse", "§1", "E"),
            ("CP2.5", "✏️", 2, 10, "Les équations normales d'un petit modèle, avec et sans ridge", "§1", "E"),
            ("CP2.6", "✏️", 2, 8, "Biais, variance et erreur quadratique d'un estimateur", "§1", "E"),
            ("CP2.7", "✏️", 2, 8, "Convexité, enveloppe convexe et marge", "§1", "E"),
            ("CP2.8", "✏️", 2, 9, "Markov, Tchebychev et Hoeffding", "§1", "E"),
            ("CP2.9", "∂", 3, 12, "Une démonstration courte, au choix parmi deux", "§1", "E"),
            ("CP2.10", "🐛", 2, 8, "Corriger une copie : cinq erreurs", "§1", "E f:02"),
            ("CP2.11", "🔗", 2, 14, "Problème de synthèse : ajuster un modèle, mesurer son erreur, décider", "§1",
             "E"),
            ("CP2.12", "🗣️", 1, 60, "Ta carte mentale et ta fiche d'une page", "§2", "E"),
        ],
    },
]
