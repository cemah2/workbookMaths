"""Syllabus, part III (before workbookIA chapters 12 to 15): planned."""

CHAPTERS = [
    {
        "id": "M12a", "dir": "m12a_espaces_vectoriels", "hours": 16, "generation_sessions": 2,
        "mml": ["§2.4", "§2.5", "§2.6", "§2.7", "§2.8"],
        "summary": "Les espaces vectoriels et les applications linéaires : sous-espaces, indépendance, base, dimension, "
                   "rang, matrice d'une application, noyau, image, théorème du rang, changement de base, applications "
                   "affines et transformation inverse.",
        "teaches": ["espace vectoriel, sous-espace", "combinaison linéaire, famille génératrice",
                    "indépendance linéaire", "base et dimension", "rang", "application linéaire et sa matrice",
                    "noyau et image", "théorème du rang", "changement de base", "applications affines",
                    "application réciproque, transformation inverse"],
        "after": ["M09a"],
        "mymath": {"module": "linmaps.py",
                   "functions": ["is_independent", "column_space_basis", "null_space_basis", "change_of_basis"]},
    },
    {
        "id": "M12b", "dir": "m12b_orthogonalite", "hours": 14, "generation_sessions": 1,
        "mml": ["§3.2", "§3.5", "§3.6", "§3.7", "§3.8"],
        "summary": "Les produits scalaires généraux, les bases orthonormées et Gram-Schmidt, le complément orthogonal, "
                   "la projection orthogonale, les moindres carrés revus comme une projection, la décomposition QR et "
                   "le produit scalaire de fonctions.",
        "teaches": ["produits scalaires généraux", "bases orthonormées", "procédé de Gram-Schmidt",
                    "complément orthogonal", "projection orthogonale", "moindres carrés comme projection",
                    "décomposition QR", "produit scalaire de fonctions"],
        "after": ["M12a", "M09b"],
        "mymath": {"module": "orthogonal.py",
                   "functions": ["gram_schmidt", "project", "qr", "least_squares_qr"]},
    },
    {
        "id": "M12c", "dir": "m12c_valeurs_propres", "hours": 16, "generation_sessions": 2,
        "mml": ["§4.1", "§4.2", "§4.3", "§4.4"],
        "summary": "Le déterminant et la trace, les valeurs et vecteurs propres, la diagonalisation et le théorème "
                   "spectral, les matrices définies positives et Cholesky, les formes quadratiques, la matrice de "
                   "covariance vue comme matrice symétrique positive, le blanchiment et la racine carrée d'une "
                   "matrice.",
        "teaches": ["déterminant", "trace", "polynôme caractéristique", "valeurs et vecteurs propres",
                    "méthode de la puissance", "diagonalisation", "théorème spectral", "matrices définies positives",
                    "décomposition de Cholesky", "formes quadratiques", "matrice de covariance symétrique positive",
                    "blanchiment (whitening)", "racine carrée d'une matrice symétrique positive"],
        "after": ["M12b", "R7"],
        "mymath": {"module": "eigen.py",
                   "functions": ["det", "power_iteration", "is_positive_definite", "cholesky", "whiten", "sqrtm_psd"]},
    },
    {
        "id": "M12d", "dir": "m12d_svd_acp", "hours": 14, "generation_sessions": 1,
        "mml": ["§4.5", "§4.6", "§4.7", "ch. 10"],
        "summary": "La SVD et son interprétation géométrique, l'approximation de rang faible, la pseudo-inverse et le "
                   "conditionnement ; puis l'ACP sous ses deux angles (variance maximale, projection), la variance "
                   "expliquée, l'autoencodeur linéaire, et la place de t-SNE.",
        "teaches": ["décomposition en valeurs singulières", "interprétation géométrique", "approximation de rang "
                    "faible (Eckart-Young)", "pseudo-inverse", "conditionnement", "ACP : variance maximale",
                    "ACP : projection", "variance expliquée", "ACP en grande dimension", "autoencodeur linéaire et ACP",
                    "t-SNE et UMAP : préserver des voisinages (aperçu)",
                    "erreur de reconstruction et détection d'anomalies"],
        "after": ["M12c", "M02c"],
        "mymath": {"module": "svd_pca.py",
                   "functions": ["svd", "low_rank_approximation", "pinv", "pca_fit", "explained_variance_ratio"]},
    },
    {
        "id": "M13a", "dir": "m13a_vraisemblance_logistique", "hours": 12, "generation_sessions": 1,
        "mml": ["§8.3"],
        "summary": "Le maximum de vraisemblance, la log-loss comme moins la log-vraisemblance, la sigmoïde et sa "
                   "dérivée, la convexité de la log-loss et la régression logistique ; Naïve Bayes comme modèle "
                   "génératif ; l'entropie, l'indice de Gini et le gain d'information des arbres.",
        "teaches": ["maximum de vraisemblance", "log-vraisemblance", "log-loss = moins la log-vraisemblance",
                    "régression logistique", "gradient de la log-loss", "convexité de la log-loss",
                    "Naïve Bayes : hypothèse d'indépendance", "indice de Gini", "gain d'information", "réduction de variance (arbres de régression)",
                    "linear probe"],
        "after": ["M04", "M06", "M05b"],
        "mymath": {"module": "likelihood.py",
                   "functions": ["bernoulli_mle", "logistic_loss", "logistic_gradient", "gini", "information_gain"]},
    },
    {
        "id": "M13b", "dir": "m13b_lagrange_svm", "hours": 14, "generation_sessions": 1,
        "mml": ["§7.2", "§7.3", "ch. 12"],
        "summary": "L'optimisation sous contraintes : multiplicateurs de Lagrange, dualité, optimisation convexe ; puis "
                   "les SVM : marge, problème primal et dual, hinge loss, noyaux et astuce du noyau (RBF).",
        "teaches": ["optimisation sous contraintes", "multiplicateurs de Lagrange", "dualité (aperçu)",
                    "optimisation convexe", "marge", "SVM primal", "hinge loss", "SVM dual",
                    "noyaux et astuce du noyau", "noyau RBF"],
        "after": ["M10", "M05b", "M12b"],
        "mymath": {"module": "svm.py",
                   "functions": ["lagrange_equality_qp", "hinge_loss", "svm_subgradient", "rbf_kernel"]},
    },
    {
        "id": "M14", "dir": "m14_ensembles", "hours": 8, "generation_sessions": 1, "mml": [],
        "summary": "Les maths des ensembles de modèles : le vote majoritaire et la loi binomiale, la variance d'une "
                   "moyenne de modèles corrélés, le bootstrap et la limite (1 − 1/n)ⁿ → 1/e (out-of-bag), les "
                   "pondérations exponentielles d'AdaBoost, et le gradient boosting comme une descente de gradient.",
        "teaches": ["vote majoritaire et loi binomiale", "vote pondéré et vote souple",
                    "variance d'une moyenne de modèles corrélés", "bootstrap et out-of-bag : (1 − 1/n)ⁿ → 1/e",
                    "pondérations exponentielles d'AdaBoost (SAMME)", "gradient boosting : descente de gradient sur "
                    "les prédictions", "learning rate du boosting"],
        "after": ["M02c", "R8", "M05b"],
        "mymath": {"module": "ensembles.py",
                   "functions": ["majority_vote_accuracy", "variance_of_mean", "oob_fraction", "adaboost_weights"]},
    },
    {
        "id": "CP3", "dir": "checkpoints/partie_3", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie III (M12a à M14) et synthèse, juste avant le checkpoint III de "
                   "workbookIA.",
        "teaches": ["révision de la partie III"],
        "after": ["M14"],
    },
]
