"""Syllabus, part VII (before the bonus chapters B1 to B8 of workbookIA): planned (sharing rule: see partie_1.py)."""

CHAPTERS = [
    {
        "id": "MB2", "dir": "mb2_cooccurrences", "hours": 8, "generation_sessions": 1, "mml": [],
        "summary": "Des cooccurrences aux embeddings : l'information mutuelle ponctuelle (PMI), la SVD tronquée d'une "
                   "matrice, la géométrie des analogies, le modèle logistique de word2vec, et les embeddings de phrases "
                   "par moyenne et cosinus.",
        "teaches": ["information mutuelle ponctuelle (PMI, PPMI)", "SVD tronquée d'une matrice de cooccurrences",
                    "géométrie des analogies", "word2vec : un modèle logistique", "recherche par similarité",
                    "un embedding est un produit one-hot × matrice (rappel M09a)",
                    "embedding de phrase : moyenne et cosinus"],
        "after": ["M12d", "M06", "M13a", "M09a"],
        "mymath": {"module": "cooccurrence.py",
                   "functions": ["pmi", "truncated_svd_embeddings", "analogy"]},
        "notes": "Frontière : les gradients du skip-gram avec échantillonnage négatif (workbookIA B2.7) ; la matrice "
                 "de cooccurrences et la PPMI sont les fonctions de `mylearn`.",
    },
    {
        "id": "MB3", "dir": "mb3_rotations_attention", "hours": 10, "generation_sessions": 1, "mml": ["§3.9"],
        "summary": "Les formules trigonométriques et les rotations du plan, les nombres complexes comme rotations "
                   "(rappel de M22), les encodages sinusoïdaux, la variance d'une somme de produits (rappel de M16), "
                   "l'attention comme moyenne pondérée, les masques, le coût quadratique et la softmax en ligne.",
        "teaches": ["formules trigonométriques", "rotations du plan, R(a)R(b) = R(a + b)",
                    "nombres complexes comme rotations (rappel)", "encodages de position sinusoïdaux",
                    "variance d'une somme de produits indépendants (rappel)",
                    "l'attention comme moyenne pondérée", "attention multi-têtes (projections)", "coût quadratique",
                    "masques causal et de padding : −∞ avant la softmax",
                    "softmax en ligne (online softmax, principe de FlashAttention)"],
        "after": ["R9", "M16", "M17", "M02c", "M12a", "M22"],
        "mymath": {"module": "positional.py",
                   "functions": ["rotation_matrix_2d", "rotate_complex", "online_softmax"]},
        "notes": "Frontières : pourquoi √d_k et la propriété relative de RoPE (workbookIA B3.6, B3.7) ; l'attention, "
                 "les encodages et RoPE sont les fonctions de `mylearn`.",
    },
    {
        "id": "MB4", "dir": "mb4_rang_faible", "hours": 6, "generation_sessions": 1, "mml": ["(§4.6)"],
        "summary": "Le rang d'un produit et le nombre de paramètres d'une adaptation de rang faible, la pondération "
                   "IDF et la formule de BM25, la recherche dense et hybride, et les métriques de recherche.",
        "teaches": ["rang d'un produit de matrices (rappel M12a)", "nombre de paramètres d'une mise à jour de rang "
                    "faible", "IDF et BM25 : la formule", "recherche dense et hybride", "recall@k et MRR (définitions)"],
        "after": ["M12d", "M07"],
        "mymath": {"module": "retrieval.py",
                   "functions": ["lora_param_count", "idf", "bm25_term_score"]},
        "notes": "Frontière : LoRA, son rang, son initialisation et ses gradients (workbookIA B4.6) ; recall@k et MRR "
                 "sont les fonctions de `mylearn`.",
    },
    {
        "id": "MB5", "dir": "mb5_diffusion", "hours": 14, "generation_sessions": 1, "mml": ["(§6.5)"],
        "summary": "Les outils de la diffusion : sommes de gaussiennes indépendantes, produit de deux densités "
                   "gaussiennes, produits cumulés de coefficients, rapport signal sur bruit, l'ELBO d'une chaîne de "
                   "variables latentes, puis les équations différentielles et la méthode d'Euler (flow matching).",
        "teaches": ["sommes de gaussiennes indépendantes (rappel de M25a)", "produit de deux densités gaussiennes en dimension 1 (rappel de M25a)",
                    "produits cumulés et plannings de bruit (linéaire, cosinus)", "rapport signal sur bruit",
                    "ELBO d'une chaîne de variables latentes (principe)", "loss de prédiction du bruit (idée)",
                    "DDPM et DDIM : ce qui change mathématiquement", "guidance sans classifieur (combinaison affine)",
                    "équations différentielles, méthode d'Euler (premier contact en M20 §6)", "flow matching (initiation)"],
        "after": ["M25a", "M25b", "M26"],
        "mymath": {"module": "diffusion.py",
                   "functions": ["cumulative_alpha", "combine_gaussians", "gaussian_product_1d", "euler_ode"]},
        "notes": "Coût : 14 h au lieu de 12. Frontières : la forme fermée de q(x_t | x_0) et le posterior "
                 "q(x_{t−1} | x_t, x_0) (workbookIA B5.6, B5.7) ; les plannings et les pas de `mylearn`.",
    },
    {
        "id": "MB6", "dir": "mb6_shapley_equite", "hours": 8, "generation_sessions": 1, "mml": [],
        "summary": "Les valeurs de Shapley (combinatoire des coalitions et axiomes), la dépendance partielle et ICE, "
                   "une intégrale le long d'un chemin (gradients intégrés), Grad-CAM, et les définitions des "
                   "indicateurs d'équité par groupe.",
        "teaches": ["valeurs de Shapley : poids des coalitions et axiomes", "dépendance partielle et ICE (espérances)",
                    "intégrale le long d'un chemin (gradients intégrés)", "Grad-CAM (gradients moyennés)",
                    "indicateurs d'équité par groupe : taux de base, calibration, taux d'erreur (définitions)"],
        "after": ["R8", "M02a", "M18", "M03"],
        "mymath": {"module": "attribution.py",
                   "functions": ["coalition_weights", "partial_dependence", "path_integral"]},
        "notes": "Frontières : Shapley d'un modèle linéaire et le théorème d'impossibilité (workbookIA B6.2, B6.6) ; "
                 "Shapley, gradients intégrés et taux par groupe sont les fonctions de `mylearn`.",
    },
    {
        "id": "MB8", "dir": "mb8_gradient_politique", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "La fonction score d'une loi et son espérance nulle, la réduction de variance par une variable de "
                   "contrôle, l'échantillonnage d'importance, le modèle de Bradley-Terry, la pénalité KL et "
                   "l'avantage relatif à un groupe : les outils statistiques de RLHF, DPO et GRPO.",
        "teaches": ["fonction score d'une loi (statistique), espérance nulle", "variable de contrôle et réduction de "
                    "variance", "échantillonnage d'importance, ratio", "clipping d'un ratio (idée)",
                    "modèle de Bradley-Terry", "pénalité KL (RLHF, DPO)", "GRPO : avantage relatif à un groupe",
                    "retours actualisés et GAE (rappel M26)"],
        "after": ["M04", "M18", "M26", "M06"],
        "mymath": {"module": "policy_gradient.py",
                   "functions": ["score_function_gradient", "importance_weights", "bradley_terry_probability"]},
        "notes": "Frontière : le gradient de politique en une étape et la baseline sans biais (workbookIA B8.7) ; "
                 "GAE et les losses de `mylearn`.",
    },
]
