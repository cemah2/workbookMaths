"""Syllabus, part IV (before workbookIA chapters 16 to 20): planned (sharing rule: see partie_1.py)."""

CHAPTERS = [
    {
        "id": "M16", "dir": "m16_couches_affines", "hours": 8, "generation_sessions": 1, "mml": ["§6.4"],
        "summary": "Un réseau comme suite d'applications affines (matrices, formes, comptage de coordonnées), les "
                   "graphes orientés acycliques et l'ordre topologique, et la variance d'une somme de produits de "
                   "variables indépendantes : l'outil des règles d'initialisation que workbookIA 16 retrouve.",
        "teaches": ["composition d'applications affines (matrices et vecteurs)", "graphe orienté acyclique",
                    "ordre topologique", "conventions de forme (n_in, n_out)", "variance d'un produit de variables "
                    "indépendantes", "variance d'une somme pondérée", "fan-in, fan-out (définitions)",
                    "réseau feed-forward : la structure mathématique"],
        "after": ["M09a", "M12a", "M02b"],
        "mymath": {"module": "init.py",
                   "functions": ["compose_affine", "variance_of_product", "variance_of_weighted_sum"]},
        "frontieres": ["17.3"],
        "notes": "Frontières : la brisure de symétrie et les règles de LeCun, Glorot et He (workbookIA 16.6, 16.7) ; "
                 "« une composition d'affines reste affine, une ReLU casse tout » (17.3).",
    },
    {
        "id": "M17", "dir": "m17_jacobienne", "hours": 10, "generation_sessions": 1, "mml": ["§5.3"],
        "summary": "La jacobienne, la jacobienne diagonale d'une fonction appliquée coordonnée par coordonnée, les "
                   "dérivées de fonctions définies par morceaux et de composées avec exp, la saturation, la softmax "
                   "(translation, température), le log-softmax et la convexité du log-sum-exp.",
        "teaches": ["jacobienne", "jacobienne d'une fonction appliquée coordonnée par coordonnée : une matrice "
                    "diagonale", "produit jacobienne-vecteur", "dérivées de fonctions par morceaux et de composées "
                    "avec exp (outils)", "maxout : un maximum de fonctions affines", "saturation",
                    "softmax, invariance par translation, température", "log-softmax et logits",
                    "convexité du log-sum-exp", "softmax de Boltzmann en RL"],
        "after": ["M05b", "M06", "M05a", "M16"],
        "mymath": {"module": "jacobian.py",
                   "functions": ["numerical_jacobian", "diagonal_jacobian", "jacobian_vector_product"]},
        "notes": "Frontières : les dérivées de la sigmoïde, de tanh et de softplus et la jacobienne de la softmax "
                 "(workbookIA 17.4, 17.7), et les activations de `mylearn`.",
    },
    {
        "id": "M18", "dir": "m18_retropropagation", "hours": 14, "generation_sessions": 1,
        "mml": ["§5.4", "§5.5", "§5.6"],
        "summary": "La règle de la chaîne multivariée, les gradients par rapport à une matrice et les identités du "
                   "calcul matriciel sur des exemples hors réseaux, le graphe de calcul, les modes direct (nombres "
                   "duaux) et inverse de la différentiation automatique, le gradient d'une moyenne, et la "
                   "vérification de gradient.",
        "teaches": ["règle de la chaîne multivariée (somme sur les chemins)", "gradients par rapport à une matrice",
                    "identités de calcul matriciel (aᵀXb, tr(AX), ‖Xw − y‖²)", "conventions de forme des gradients",
                    "graphe de calcul", "mode direct : nombres duaux", "mode inverse (principe)",
                    "gradient d'une moyenne = moyenne des gradients", "vérification de gradient : erreur relative",
                    "gradient par rapport à l'entrée (FGSM)"],
        "after": ["M17", "M09a"],
        "mymath": {"module": "autodiff.py",
                   "functions": ["Dual", "dual_derivative", "numerical_matrix_gradient", "relative_error"]},
        "frontieres": ["18.14"],
        "notes": "workbookIA 18 écrit le mode inverse (`Value`, rétropropagation) ; M18 écrit le mode direct. "
                 "Frontières : les deltas, XᵀΔ, et le gradient p − y (18.6 à 18.8), les cross-entropies sur les "
                 "logits (18.14).",
    },
    {
        "id": "M19", "dir": "m19_hessienne_convergence", "hours": 14, "generation_sessions": 1,
        "mml": ["§5.7", "§5.8", "§7.1", "§7.3"],
        "summary": "La hessienne et Taylor à plusieurs variables, le conditionnement, la convergence de la descente de "
                   "gradient sur une quadratique de ℝⁿ et le pas critique 2/λmax, la descente stochastique, le "
                   "momentum comme suite récurrente linéaire, l'idée des pas adaptatifs, AdamW, le clipping, et les "
                   "fonctions convexes.",
        "teaches": ["hessienne", "Taylor à plusieurs variables", "géométrie d'une surface quadratique",
                    "conditionnement", "descente de gradient sur une quadratique de ℝⁿ : pas critique 2/λmax",
                    "descente stochastique et mini-batch : un gradient bruité sans biais",
                    "momentum comme suite récurrente linéaire", "pas adaptatifs : diviser par une moyenne des carrés "
                    "(idée)", "AdamW : weight decay découplé", "plannings de learning rate",
                    "gradient clipping par la norme", "fonctions convexes", "choisir un optimiseur : ce que disent "
                    "les maths"],
        "after": ["M18", "M12c", "R5"],
        "mymath": {"module": "optim.py",
                   "functions": ["numerical_hessian", "condition_number", "critical_learning_rate",
                                 "gd_quadratic_iterates"]},
        "notes": "Frontières : le pas sous 2/a sur une parabole et la mémoire effective et le biais initial d'une "
                 "moyenne exponentielle (workbookIA 19.7, 19.8) ; les optimiseurs de `mylearn`.",
    },
    {
        "id": "M20", "dir": "m20_tenseurs_normalisation", "hours": 8, "generation_sessions": 1, "mml": [],
        "summary": "Les tableaux à n dimensions et `einsum`, l'espérance d'un produit par une variable de Bernoulli, "
                   "moyennes et variances le long d'axes (normalisations par batch et par couche, vues comme des "
                   "applications affines), et la jacobienne d'une connexion résiduelle.",
        "teaches": ["tenseurs, axes et `einsum`", "espérance d'un produit par une variable de Bernoulli",
                    "moyenne et variance le long d'axes", "batchnorm et layer norm : centrer, réduire, transformation "
                    "affine", "connexions résiduelles : jacobienne I + J"],
        "after": ["M02c", "M19"],
        "mymath": {"module": "tensors.py",
                   "functions": ["einsum_matmul", "einsum_bilinear", "moments_along_axes"]},
        "notes": "Frontières : l'espérance du dropout et le gradient de la batchnorm (workbookIA 20.5, 20.8).",
    },
    {
        "id": "CP4", "dir": "checkpoints/partie_4", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie IV (M16 à M20) et synthèse, juste avant le checkpoint IV de workbookIA.",
        "teaches": ["révision de la partie IV"],
        "after": ["M20"],
    },
]
