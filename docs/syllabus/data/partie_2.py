"""Syllabus, part II (before workbookIA chapters 7 to 11): planned."""

CHAPTERS = [
    {
        "id": "M07", "dir": "m07_vecteurs_rn", "hours": 12, "generation_sessions": 1,
        "mml": ["§3.1", "§3.3", "§3.4"],
        "summary": "Les vecteurs de ℝⁿ : normes L1, L2, L∞, distances, produit scalaire, angle et similarité cosinus, "
                   "inégalité de Cauchy-Schwarz, hyperplans et demi-espaces ; le barycentre (la moyenne minimise la "
                   "somme des carrés des distances, cœur de k-means) ; et les surprises de la grande dimension.",
        "teaches": ["vecteurs de ℝⁿ", "normes L1, L2, L∞", "distances", "produit scalaire", "angle",
                    "similarité cosinus", "inégalité de Cauchy-Schwarz", "inégalité triangulaire",
                    "hyperplans et demi-espaces", "frontière de décision linéaire", "barycentre et centroïde",
                    "la moyenne minimise la somme des carrés des distances", "k-means : affectation et mise à jour",
                    "inertie et silhouette", "grande dimension, concentration des distances",
                    "le neurone comme produit scalaire plus biais", "vecteurs one-hot et base canonique",
                    "k-means++ : tirer selon le carré des distances"],
        "after": ["R9", "M02c", "R4"],
        "mymath": {"module": "vectors.py",
                   "functions": ["norm_p", "distance_matrix", "cosine_similarity", "centroid", "assign_to_nearest",
                                 "side_of_hyperplane"]},
    },
    {
        "id": "M08", "dir": "m08_tests", "hours": 10, "generation_sessions": 1, "mml": ["§8.6"],
        "summary": "Les tests statistiques : hypothèses, statistique de test, p-valeur, test par permutation, erreurs "
                   "de type I et II, intervalle d'une accuracy, comparaisons multiples ; puis la sélection de modèle "
                   "et la validation croisée vues comme des estimations bruitées.",
        "teaches": ["hypothèse nulle et alternative", "statistique de test", "p-valeur", "test par permutation",
                    "erreurs de type I et II", "puissance d'un test", "intervalle d'une accuracy",
                    "comparaisons multiples (Bonferroni)", "comparer deux modèles", "validation croisée : principe "
                    "statistique", "importance par permutation (principe)", "évaluation sur plusieurs graines"],
        "after": ["M02c", "M03"],
        "mymath": {"module": "testing.py",
                   "functions": ["permutation_test", "proportion_ci", "bonferroni", "paired_difference_ci"]},
    },
    {
        "id": "M09a", "dir": "m09a_matrices", "hours": 16, "generation_sessions": 2, "mml": ["§2.1", "§2.2", "§2.3"],
        "summary": "Les matrices et les systèmes linéaires : produit et formes, transposée, produit de Hadamard, "
                   "systèmes, pivot de Gauss et forme échelonnée, inverse, premier contact avec le rang ; la passe "
                   "avant d'un réseau écrite comme un produit matriciel.",
        "teaches": ["matrices, formes", "produit matrice-vecteur et matriciel", "produit de Hadamard",
                    "transposée et ses règles", "systèmes linéaires", "pivot de Gauss, forme échelonnée",
                    "inverse d'une matrice", "rang (premier contact)", "matrice identité, matrices diagonales",
                    "un dataset est une matrice ; la passe avant est un produit"],
        "after": ["R2", "M07"],
        "mymath": {"module": "matrices.py",
                   "functions": ["matmul", "transpose", "row_echelon", "solve", "inverse", "rank"]},
    },
    {
        "id": "M09b", "dir": "m09b_moindres_carres", "hours": 14, "generation_sessions": 1,
        "mml": ["§8.1", "§8.2", "ch. 9"],
        "summary": "La régression linéaire par les moindres carrés : équations normales, ridge (et ridge vue comme MAP), "
                   "lasso et seuillage doux, MSE, MAE et R², décomposition biais-variance, régression vue comme "
                   "maximum de vraisemblance, aperçu de la régression bayésienne et de la double descente.",
        "teaches": ["risque empirique", "moindres carrés", "équations normales", "features polynomiales",
                    "régularisation ridge", "ridge comme MAP", "lasso et seuillage doux", "MSE, MAE, R²",
                    "décomposition biais-variance", "régression comme maximum de vraisemblance",
                    "régression bayésienne (aperçu)", "double descente (aperçu)", "pénalité L2 et weight decay"],
        "after": ["M09a", "M05b", "M02c", "M04"],
        "mymath": {"module": "linreg.py",
                   "functions": ["least_squares", "ridge", "soft_threshold", "lasso_coordinate_descent", "r2_score"]},
    },
    {
        "id": "M10", "dir": "m10_separabilite_convexite", "hours": 8, "generation_sessions": 1, "mml": ["§12.1"],
        "summary": "Les ensembles convexes et l'enveloppe convexe, la séparation de deux nuages par un hyperplan, "
                   "l'impossibilité pour XOR, l'astuce du biais, et la démonstration du théorème de convergence du "
                   "perceptron.",
        "teaches": ["ensembles convexes", "enveloppe convexe", "séparabilité linéaire", "XOR n'est pas séparable",
                    "astuce du biais (une coordonnée en plus)", "règle du perceptron", "théorème de convergence du "
                    "perceptron (démonstration)"],
        "after": ["M07", "R4"],
        "mymath": {"module": "convex.py",
                   "functions": ["convex_hull_2d", "is_linearly_separable", "perceptron_bound"]},
    },
    {
        "id": "M11", "dir": "m11_logique_concentration", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "La logique au service du raisonnement (déduction, validité, syllogismes, induction et ses "
                   "sophismes) ; puis les bandits : moyenne incrémentale, inégalités de Markov, Tchebychev et "
                   "Hoeffding, bornes de confiance (UCB), ε-greedy et regret.",
        "teaches": ["déduction, validité, solidité", "syllogismes et sophismes", "induction et ses pièges",
                    "moyenne incrémentale", "inégalité de Markov", "inégalité de Tchebychev",
                    "inégalité de Hoeffding", "bornes de confiance (UCB)", "ε-greedy", "regret",
                    "échantillonnage de Thompson"],
        "after": ["R4", "M02c", "M04"],
        "mymath": {"module": "concentration.py",
                   "functions": ["incremental_mean", "markov_bound", "chebyshev_bound", "hoeffding_bound",
                                 "ucb_index"]},
    },
    {
        "id": "CP2", "dir": "checkpoints/partie_2", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie II (M07 à M11) et synthèse, juste avant le checkpoint II de workbookIA.",
        "teaches": ["révision de la partie II"],
        "after": ["M11"],
    },
]
