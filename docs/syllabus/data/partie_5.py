"""Syllabus, part V (before workbookIA chapters 21 to 24): planned (sharing rule: see partie_1.py)."""

CHAPTERS = [
    {
        "id": "M21", "dir": "m21_convolution", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "La convolution et la corrélation croisée en 1D et 2D, la convolution comme application linéaire "
                   "(matrice de Toeplitz) et sa transposée, l'équivariance par translation, les tailles de sortie "
                   "(padding, stride, dilatation, groupes), le pooling, les noyaux séparables et le champ récepteur.",
        "teaches": ["convolution et corrélation croisée en 1D et 2D", "matrice de Toeplitz et sa transposée", "im2col",
                    "équivariance par translation", "tailles de sortie : padding, stride, dilatation",
                    "convolutions groupées et en profondeur : compter les paramètres", "max et average pooling",
                    "noyaux séparables (rang 1)", "champ récepteur"],
        "after": ["M12a", "M09a", "M18"],
        "mymath": {"module": "conv.py",
                   "functions": ["conv1d", "toeplitz_1d", "receptive_field", "is_separable_kernel"]},
        "notes": "Frontière : la rétropropagation dans une convolution 1D (workbookIA 21.7) ; les fonctions de "
                 "convolution 2D sont celles de `mylearn`.",
    },
    {
        "id": "M22", "dir": "m22_recurrences", "hours": 10, "generation_sessions": 1, "mml": ["(§4.2)"],
        "summary": "Les suites récurrentes vectorielles, les puissances d'une matrice, les nombres complexes juste ce "
                   "qu'il faut pour le rayon spectral, les normes de matrices, les produits de jacobiennes de la "
                   "rétropropagation dans le temps, le gradient évanescent ou explosif, et le clipping.",
        "teaches": ["suites récurrentes vectorielles", "puissances d'une matrice",
                    "nombres complexes : module, forme exponentielle, rotations (après M12c §3 et M19 §6)",
                    "valeurs propres complexes, rayon spectral", "normes de matrices, norme d'opérateur = σmax",
                    "produits de jacobiennes (BPTT)", "gradient évanescent ou explosif", "clipping",
                    "produits de Hadamard par des facteurs dans [0, 1] : ce qui reste après n étapes"],
        "after": ["M12c", "M12d", "M18"],
        "mymath": {"module": "recurrence.py",
                   "functions": ["matrix_power_iterates", "spectral_radius", "operator_norm",
                                 "jacobian_product_norms"]},
        "notes": "Frontières : le produit de dérivées de tanh et le chemin additif de la cellule LSTM (workbookIA "
                 "22.6, 22.7).",
    },
    {
        "id": "CP5", "dir": "checkpoints/partie_5", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie V (M21 et M22) et synthèse, juste avant le checkpoint V de workbookIA.",
        "teaches": ["révision de la partie V"],
        "after": ["M22"],
    },
]
