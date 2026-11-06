"""Syllabus, part II (before workbookIA chapters 7 to 11): planned (sharing rule: see partie_1.py)."""

CHAPTERS = [
    {
        "id": "M07", "dir": "m07_vecteurs_rn", "hours": 14, "generation_sessions": 1,
        "mml": ["§3.1", "§3.2.1", "§3.3", "§3.4"],
        "summary": "Les vecteurs de ℝⁿ : normes L1, L2, L∞, distances, produit scalaire, angle et similarité cosinus, "
                   "inégalité de Cauchy-Schwarz, hyperplans et demi-espaces ; le barycentre (rappel : la moyenne "
                   "minimise la somme des carrés des distances, cœur de k-means) ; et les surprises de la grande "
                   "dimension.",
        "teaches": ["vecteurs de ℝⁿ", "normes L1, L2, L∞", "distances", "produit scalaire", "angle",
                    "similarité cosinus", "inégalité de Cauchy-Schwarz", "inégalité triangulaire",
                    "projection sur une droite", "hyperplans et demi-espaces, distance à un hyperplan",
                    "frontière de décision linéaire", "barycentre et centroïde",
                    "k-means : affectation et mise à jour (le principe)", "inertie et silhouette",
                    "grande dimension, concentration des distances", "le neurone comme produit scalaire plus biais",
                    "vecteurs one-hot et base canonique", "k-means++ : tirer selon le carré des distances"],
        "after": ["R9", "M02c", "R4"],
        "mymath": {"module": "vectors.py",
                   "functions": ["norm_p", "project_onto_line", "centroid", "sum_sq_distances_to",
                                 "side_of_hyperplane", "distance_to_hyperplane"]},
        "notes": "Coût : 14 h au lieu de 12 (18 notions). Les distances par paires, k-means et la silhouette sont "
                 "les fonctions de `mylearn` en workbookIA 7.",
    },
    {
        "id": "M08", "dir": "m08_tests", "hours": 10, "generation_sessions": 1, "mml": ["§8.6"],
        "summary": "Les tests statistiques : hypothèses, statistique de test, p-valeur, test par permutation, erreurs "
                   "de type I et II, intervalle d'une accuracy, comparaisons multiples ; puis la sélection de modèle "
                   "(AIC, BIC, facteur de Bayes) et la validation croisée vues comme des estimations bruitées.",
        "teaches": ["hypothèse nulle et alternative", "statistique de test", "p-valeur", "test par permutation",
                    "erreurs de type I et II", "puissance d'un test", "intervalle d'une accuracy",
                    "comparaisons multiples (Bonferroni)", "comparer deux modèles",
                    "sélection de modèle : AIC, BIC, facteur de Bayes (aperçu)",
                    "validation croisée : principe statistique", "importance par permutation (principe)",
                    "évaluation sur plusieurs graines"],
        "after": ["M02c", "M03", "M04"],
        "mymath": {"module": "testing.py",
                   "functions": ["permutation_test", "proportion_ci", "bonferroni", "paired_difference_ci", "aic_bic"]},
    },
    {
        "id": "M09a", "dir": "m09a_matrices", "hours": 16, "generation_sessions": 2, "mml": ["§2.1", "§2.2", "§2.3"],
        "summary": "Les matrices et les systèmes linéaires : produit et formes, transposée, produit de Hadamard, "
                   "systèmes, pivot de Gauss et forme échelonnée, inverse, premier contact avec le rang ; la passe "
                   "avant d'un réseau écrite comme un produit matriciel.",
        "teaches": ["matrices, formes", "produit matrice-vecteur et matriciel", "produit de Hadamard",
                    "transposée et ses règles", "systèmes linéaires", "pivot de Gauss, forme échelonnée",
                    "inverse d'une matrice", "rang (premier contact)", "matrice identité, matrices diagonales",
                    "un dataset est une matrice : opérer par ligne, par colonne, élément par élément",
                    "Z = XW + b : la convention des poids", "un embedding est un produit one-hot × matrice"],
        "after": ["R2", "M07"],
        "mymath": {"module": "matrices.py",
                   "functions": ["matmul", "transpose", "row_echelon", "solve", "inverse", "rank"]},
    },
    {
        "id": "M09b", "dir": "m09b_moindres_carres", "hours": 16, "generation_sessions": 2,
        "mml": ["§8.1", "§8.2", "§9.1", "§9.2"],
        "summary": "La régression linéaire par les moindres carrés : gradients de aᵀw et de wᵀAw, équations "
                   "normales, régularisation ridge (et ridge vue comme MAP), lasso, MSE, MAE, Huber et R², "
                   "décomposition biais-variance, régression vue comme maximum de vraisemblance, features "
                   "polynomiales, aperçu de la double descente.",
        "teaches": ["risque empirique", "gradients de aᵀw et de wᵀAw (calcul matriciel minimal)", "moindres carrés",
                    "équations normales", "features polynomiales : combien de monômes (combinaisons avec répétition)",
                    "régularisation ridge", "ridge comme MAP", "lasso (principe)", "MSE, MAE, loss de Huber, R², RMSE",
                    "décomposition biais-variance", "overfitting et underfitting vus par le biais et la variance",
                    "régression comme maximum de vraisemblance", "double descente (aperçu)",
                    "pénalité L2 et weight decay"],
        "after": ["M09a", "M05b", "M02c", "M04"],
        "mymath": {"module": "linreg.py",
                   "functions": ["normal_equations", "solve_least_squares", "hat_matrix", "residual_decomposition"]},
        "notes": "Frontières : les moindres carrés par dérivées partielles en dimension 1, ridge et lasso en "
                 "dimension 1 (workbookIA 9.2, 9.3, 9.6) ne sont pas démontrés ici ; M09b travaille en dimension n, "
                 "par les gradients matriciels. La régression bayésienne (MML §9.3) se lit en M25a, la projection "
                 "(MML §9.4) en M12b.",
    },
    {
        "id": "M10", "dir": "m10_separabilite_convexite", "hours": 8, "generation_sessions": 1, "mml": ["§12.1"],
        "summary": "Les ensembles convexes et l'enveloppe convexe, la séparation de deux nuages par un hyperplan, "
                   "l'astuce du biais, et les outils de la preuve de convergence du perceptron (Cauchy-Schwarz, "
                   "récurrence sur ‖w‖²), que workbookIA 10 assemble.",
        "teaches": ["ensembles convexes", "enveloppe convexe", "séparabilité linéaire (enveloppes convexes disjointes)",
                    "astuce du biais (une coordonnée en plus)", "inégalités de récurrence sur une norme",
                    "fonctions d'activation : des fonctions d'une variable (rappel R3, R6)"],
        "after": ["M07", "R4"],
        "mymath": {"module": "convex.py",
                   "functions": ["convex_hull_2d", "is_linearly_separable", "margin_of_separator"]},
        "notes": "Frontières : XOR n'est pas séparable et la convergence du perceptron sont démontrés en workbookIA "
                 "10 (10.4, 10.7).",
    },
    {
        "id": "M11", "dir": "m11_logique_concentration", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "La logique au service du raisonnement (déduction, validité, syllogismes, induction et ses "
                   "sophismes) ; puis les inégalités de Markov, Tchebychev et Hoeffding, les rayons de confiance et "
                   "l'idée des bornes supérieures de confiance, ε-greedy et regret.",
        "teaches": ["déduction, validité, solidité", "syllogismes et sophismes", "induction et ses pièges",
                    "inégalité de Markov", "inégalité de Tchebychev", "inégalité de Hoeffding",
                    "rayon de confiance d'une moyenne", "bornes supérieures de confiance (UCB, principe)",
                    "ε-greedy", "regret", "échantillonnage de Thompson"],
        "after": ["R4", "M02c", "M04"],
        "mymath": {"module": "concentration.py",
                   "functions": ["markov_bound", "chebyshev_bound", "hoeffding_bound", "hoeffding_radius",
                                 "empirical_tail"]},
        "notes": "Frontière : la moyenne incrémentale (workbookIA 11.2) est démontrée par workbookIA ; M11 s'appuie "
                 "sur les suites de R5.",
    },
    {
        "id": "CP2", "dir": "checkpoints/partie_2", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie II (M07 à M11) et synthèse, juste avant le checkpoint II de workbookIA.",
        "teaches": ["révision de la partie II"],
        "after": ["M11"],
    },
]
