"""Syllabus, part V (before workbookIA chapters 21 to 24): planned."""

CHAPTERS = [
    {
        "id": "M21", "dir": "m21_convolution", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "La convolution et la corrélation croisée en 1D et 2D, la convolution comme application linéaire "
                   "(matrice de Toeplitz) et im2col, l'équivariance par translation, les tailles de sortie (padding, "
                   "stride, dilatation), le pooling, la transposée d'une convolution et le champ récepteur.",
        "teaches": ["convolution et corrélation croisée en 1D et 2D", "matrice de Toeplitz", "im2col",
                    "équivariance par translation", "tailles de sortie : padding, stride, dilatation",
                    "max et average pooling", "transposée d'une convolution", "rétropropagation d'une convolution",
                    "champ récepteur"],
        "after": ["M12a", "M09a", "M18"],
        "mymath": {"module": "conv.py",
                   "functions": ["conv1d", "correlate2d", "toeplitz_1d", "output_size", "maxpool2d"]},
    },
    {
        "id": "M22", "dir": "m22_recurrences", "hours": 10, "generation_sessions": 1, "mml": ["(§4.2)"],
        "summary": "Les suites récurrentes vectorielles, les puissances d'une matrice et le rayon spectral, les normes "
                   "de matrices, les produits de jacobiennes de la rétropropagation dans le temps, le gradient "
                   "évanescent ou explosif, et le clipping.",
        "teaches": ["suites récurrentes vectorielles", "puissances d'une matrice", "rayon spectral",
                    "normes de matrices", "produits de jacobiennes (BPTT)", "gradient évanescent ou explosif",
                    "clipping", "portes du LSTM et du GRU : sigmoïdes et produits de Hadamard"],
        "after": ["M12c", "M18"],
        "mymath": {"module": "recurrence.py",
                   "functions": ["matrix_power_iterates", "spectral_radius", "operator_norm",
                                 "jacobian_product_norms"]},
    },
    {
        "id": "CP5", "dir": "checkpoints/partie_5", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie V (M21 et M22) et synthèse, juste avant le checkpoint V de workbookIA.",
        "teaches": ["révision de la partie V"],
        "after": ["M22"],
    },
]
