"""Syllabus, part III (before workbookIA chapters 12 to 15): planned (sharing rule: see partie_1.py)."""

CHAPTERS = [
    {
        "id": "M12a", "dir": "m12a_espaces_vectoriels", "hours": 16, "generation_sessions": 2,
        "mml": ["§2.4", "§2.5", "§2.6", "§2.7", "§2.8"],
        "summary": "Les espaces vectoriels et les applications linéaires : sous-espaces, indépendance, base, dimension, "
                   "rang, matrice d'une application, noyau, image, théorème du rang, changement de base, applications "
                   "affines et transformation inverse.",
        "teaches": ["espace vectoriel, sous-espace", "combinaison linéaire, famille génératrice",
                    "indépendance linéaire", "base et dimension", "rang, rang d'un produit", "application linéaire et "
                    "sa matrice", "noyau et image", "théorème du rang", "changement de base", "applications affines",
                    "application réciproque, transformation inverse"],
        "after": ["M09a"],
        "mymath": {"module": "linmaps.py",
                   "functions": ["is_independent", "column_space_basis", "null_space_basis", "change_of_basis"]},
        "notes": "Parcours essentiel : le théorème du rang et le changement de base démontrés hors parcours.",
    },
    {
        "id": "M12b", "dir": "m12b_orthogonalite", "hours": 14, "generation_sessions": 1,
        "mml": ["§3.2.2", "§3.2.3", "§3.5", "§3.6", "§3.7", "§3.8", "§9.4"],
        "summary": "Les produits scalaires généraux, les bases orthonormées et Gram-Schmidt, le complément orthogonal, "
                   "la projection orthogonale, les moindres carrés revus comme une projection, la décomposition QR et "
                   "le produit scalaire de fonctions.",
        "teaches": ["produits scalaires généraux, matrices symétriques définies positives", "bases orthonormées",
                    "procédé de Gram-Schmidt", "complément orthogonal", "projection orthogonale",
                    "moindres carrés comme projection", "décomposition QR", "produit scalaire de fonctions"],
        "after": ["M12a", "M09b"],
        "mymath": {"module": "orthogonal.py",
                   "functions": ["gram_schmidt", "project", "qr", "least_squares_qr"]},
        "notes": "Parcours essentiel : QR et le produit scalaire de fonctions hors parcours (workbookIA 12 n'en a pas "
                 "besoin).",
    },
    {
        "id": "M12c", "dir": "m12c_valeurs_propres", "hours": 16, "generation_sessions": 2,
        "mml": ["§4.1", "§4.2", "§4.3", "§4.4"],
        "summary": "Le déterminant et la trace, les valeurs et vecteurs propres, la diagonalisation et le théorème "
                   "spectral, les matrices définies positives et Cholesky, les formes quadratiques et la convexité à "
                   "plusieurs variables, la matrice de covariance vue comme matrice symétrique positive, le "
                   "blanchiment et la racine carrée d'une matrice.",
        "teaches": ["déterminant", "trace", "polynôme caractéristique", "valeurs et vecteurs propres",
                    "méthode de la puissance", "diagonalisation", "théorème spectral", "quotient de Rayleigh",
                    "matrices définies positives", "décomposition de Cholesky", "formes quadratiques",
                    "convexité à plusieurs variables : cordes et hessienne semi-définie positive (premier contact)",
                    "matrice de covariance symétrique positive", "blanchiment (whitening)",
                    "racine carrée d'une matrice symétrique positive"],
        "after": ["M12b", "R7"],
        "mymath": {"module": "eigen.py",
                   "functions": ["det", "power_iteration", "is_positive_definite", "cholesky", "whiten", "sqrtm_psd"]},
    },
    {
        "id": "M12d", "dir": "m12d_svd_acp", "hours": 16, "generation_sessions": 2,
        "mml": ["§4.5", "§4.6", "§4.7", "§10.1", "§10.2", "§10.3", "§10.4", "§10.5", "§10.6"],
        "summary": "La SVD et son interprétation géométrique, l'approximation de rang faible, la pseudo-inverse et le "
                   "conditionnement ; puis les axes principaux par le quotient de Rayleigh, la variance expliquée, "
                   "l'erreur de reconstruction d'une projection, et la place de t-SNE et d'UMAP.",
        "teaches": ["décomposition en valeurs singulières", "interprétation géométrique", "approximation de rang "
                    "faible (Eckart-Young)", "pseudo-inverse", "conditionnement",
                    "axes principaux : maximiser uᵀCu sur la sphère (quotient de Rayleigh)", "ACP : projection",
                    "variance expliquée", "ACP en grande dimension", "erreur de reconstruction d'une projection",
                    "t-SNE et UMAP : préserver des voisinages (aperçu)",
                    "erreur de reconstruction et détection d'anomalies"],
        "after": ["M12c", "M02c"],
        "mymath": {"module": "svd_pca.py",
                   "functions": ["svd", "low_rank_approximation", "pinv", "principal_axes", "explained_variance_ratio"]},
        "frontieres": ["25.8"],
        "notes": "MML §10.2 dérive l'axe de variance maximale par Lagrange : M12d passe par le quotient de Rayleigh, "
                 "la dérivation de MML se relit en M13b ; §10.7 (point de vue latent) se lit en M25b. Frontières : "
                 "variance d'une projection et axe de variance maximale (workbookIA 12.8), autoencodeur linéaire et "
                 "ACP (25.8).",
    },
    {
        "id": "M13a", "dir": "m13a_vraisemblance_logistique", "hours": 12, "generation_sessions": 1,
        "mml": ["§8.3"],
        "summary": "Le maximum de vraisemblance (Bernoulli, catégorielle, gaussienne), la log-loss comme moins la "
                   "log-vraisemblance, la sigmoïde, la convexité de log(1 + eᶻ), la régression logistique comme modèle ; "
                   "Naïve Bayes comme modèle génératif ; l'entropie, l'indice de Gini et la réduction de variance des "
                   "arbres.",
        "teaches": ["maximum de vraisemblance", "log-vraisemblance", "log-loss = moins la log-vraisemblance",
                    "régression logistique : le modèle", "convexité de log(1 + eᶻ)",
                    "Naïve Bayes : hypothèse d'indépendance", "impureté d'une distribution : entropie, Gini",
                    "réduction de variance (arbres de régression)", "linear probe"],
        "after": ["M04", "M06", "M05b", "M12c"],
        "mymath": {"module": "likelihood.py",
                   "functions": ["bernoulli_log_likelihood", "bernoulli_mle", "categorical_mle", "gaussian_mle",
                                 "logistic_loss"]},
        "notes": "Frontière : le gradient de la log-loss de la régression logistique (workbookIA 13.8). Les "
                 "impuretés et le meilleur découpage sont les fonctions de `mylearn` en workbookIA 13.",
    },
    {
        "id": "M13b", "dir": "m13b_lagrange_svm", "hours": 14, "generation_sessions": 1,
        "mml": ["§7.2", "§7.3", "ch. 12"],
        "summary": "L'optimisation sous contraintes : multiplicateurs de Lagrange, dualité, optimisation convexe ; puis "
                   "les SVM : marge, problème primal et dual, hinge loss, noyaux et astuce du noyau (RBF).",
        "teaches": ["optimisation sous contraintes", "multiplicateurs de Lagrange", "dualité (aperçu)",
                    "optimisation convexe", "relire MML §10.2 : l'ACP par Lagrange", "marge", "SVM primal",
                    "hinge loss", "SVM dual", "noyaux et astuce du noyau", "noyau RBF"],
        "after": ["M10", "M05b", "M12c", "M12d"],
        "mymath": {"module": "svm.py",
                   "functions": ["lagrange_equality_qp", "hinge_loss", "svm_subgradient", "rbf_kernel"]},
    },
    {
        "id": "M14", "dir": "m14_ensembles", "hours": 6, "generation_sessions": 1, "mml": [],
        "summary": "Les outils des ensembles de modèles : la queue de la loi binomiale, la variance d'une moyenne de "
                   "variables corrélées, la limite (1 + x/n)ⁿ → eˣ, des poids exponentiels, et l'idée d'une descente "
                   "de gradient dans un espace de fonctions. workbookIA 14 les applique au vote, au bagging et au "
                   "boosting.",
        "teaches": ["queue de la loi binomiale", "variance d'une moyenne de variables corrélées",
                    "(1 + x/n)ⁿ → eˣ", "poids exponentiels et renormalisation",
                    "descente de gradient dans un espace de fonctions (idée)", "forêt aléatoire : décorréler pour "
                    "réduire la variance"],
        "after": ["M02c", "R8", "M05b", "M05a"],
        "mymath": {"module": "ensembles.py",
                   "functions": ["binomial_tail", "variance_of_mean_correlated", "normalize_exponential_weights"]},
        "frontieres": ["14.5", "14.6", "14.7"],
        "notes": "Réduit à 6 h : le bootstrap qui oublie 36,8 % des points, les résidus comme gradient, la majorité "
                 "qui se trompe, AdaBoost et le gradient boosting à la main sont des exercices de workbookIA 14.",
    },
    {
        "id": "CP3", "dir": "checkpoints/partie_3", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie III (M12a à M14) et synthèse, juste avant le checkpoint III de "
                   "workbookIA.",
        "teaches": ["révision de la partie III"],
        "after": ["M14"],
    },
]
