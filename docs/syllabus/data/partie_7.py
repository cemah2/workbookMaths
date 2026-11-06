"""Syllabus, part VII (before the bonus chapters B1 to B8 of workbookIA): planned."""

CHAPTERS = [
    {
        "id": "MB2", "dir": "mb2_cooccurrences", "hours": 8, "generation_sessions": 1, "mml": [],
        "summary": "Des cooccurrences aux embeddings : l'information mutuelle ponctuelle (PMI, PPMI), la SVD tronquée "
                   "d'une matrice de cooccurrences, la géométrie des analogies, et le modèle logistique de word2vec.",
        "teaches": ["information mutuelle ponctuelle (PMI, PPMI)", "SVD tronquée d'une matrice de cooccurrences",
                    "géométrie des analogies", "word2vec : un modèle logistique", "recherche par similarité",
                    "un embedding est un produit one-hot × matrice", "embedding de phrase : moyenne et cosinus"],
        "after": ["M12d", "M06", "M13a"],
        "mymath": {"module": "cooccurrence.py",
                   "functions": ["cooccurrence_matrix", "ppmi", "truncated_svd_embeddings", "analogy"]},
    },
    {
        "id": "MB3", "dir": "mb3_rotations_attention", "hours": 10, "generation_sessions": 1, "mml": ["§3.9"],
        "summary": "Les formules trigonométriques et les rotations, les nombres complexes comme rotations (RoPE), les "
                   "encodages sinusoïdaux, la variance d'un produit scalaire et le facteur 1/√d, l'attention comme "
                   "moyenne pondérée, et le coût quadratique.",
        "teaches": ["formules trigonométriques", "rotations du plan", "nombres complexes comme rotations",
                    "encodages de position sinusoïdaux", "RoPE", "variance d'un produit scalaire, facteur 1/√d",
                    "l'attention comme moyenne pondérée", "attention multi-têtes (projections)", "coût quadratique",
                    "masques causal et de padding : −∞ avant la softmax"],
        "after": ["R9", "M17", "M02c", "M12a"],
        "mymath": {"module": "positional.py",
                   "functions": ["sinusoidal_encoding", "rotate_pairs", "scaled_dot_product_attention"]},
    },
    {
        "id": "MB4", "dir": "mb4_rang_faible", "hours": 6, "generation_sessions": 1, "mml": ["(§4.6)"],
        "summary": "L'adaptation de rang faible (LoRA) et son nombre de paramètres, BM25, la recherche dense et "
                   "hybride, et les métriques de recherche (recall@k, MRR).",
        "teaches": ["LoRA : mise à jour de rang faible", "nombre de paramètres de LoRA", "BM25",
                    "recherche dense et hybride", "recall@k et MRR"],
        "after": ["M12d", "M07"],
        "mymath": {"module": "retrieval.py",
                   "functions": ["lora_update", "bm25_scores", "recall_at_k", "mean_reciprocal_rank"]},
    },
    {
        "id": "MB5", "dir": "mb5_diffusion", "hours": 12, "generation_sessions": 1, "mml": ["(§6.5)"],
        "summary": "Les maths de la diffusion : sommes de gaussiennes et forme fermée du processus direct, plannings de "
                   "bruit, posterior gaussien, ELBO de la diffusion et loss de prédiction du bruit, DDIM, guidance "
                   "sans classifieur, puis les équations différentielles et la méthode d'Euler (flow matching).",
        "teaches": ["sommes de gaussiennes indépendantes", "processus direct : forme fermée",
                    "plannings de bruit linéaire et cosinus", "posterior gaussien", "ELBO de la diffusion",
                    "loss de prédiction du bruit", "DDPM et DDIM", "guidance sans classifieur",
                    "équations différentielles, méthode d'Euler", "flow matching (initiation)"],
        "after": ["M25a", "M25b", "M26"],
        "mymath": {"module": "diffusion.py",
                   "functions": ["cosine_schedule", "forward_sample", "posterior_params", "euler_ode"]},
    },
    {
        "id": "MB6", "dir": "mb6_shapley_equite", "hours": 8, "generation_sessions": 1, "mml": [],
        "summary": "Les valeurs de Shapley (combinatoire et axiomes), la dépendance partielle et ICE, les gradients "
                   "intégrés (intégrale le long d'un chemin), Grad-CAM, et le théorème d'impossibilité de l'équité.",
        "teaches": ["valeurs de Shapley : combinatoire et axiomes", "dépendance partielle et ICE (espérances)",
                    "gradients intégrés : intégrale le long d'un chemin", "Grad-CAM (gradients moyennés)",
                    "indicateurs d'équité par groupe", "théorème d'impossibilité de l'équité"],
        "after": ["R8", "M02a", "M18", "M03"],
        "mymath": {"module": "attribution.py",
                   "functions": ["shapley_values", "partial_dependence", "integrated_gradients", "group_rates"]},
    },
    {
        "id": "MB8", "dir": "mb8_gradient_politique", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "Le théorème du gradient de politique et l'astuce de la dérivée du logarithme, la baseline et la "
                   "réduction de variance, GAE, l'échantillonnage d'importance et le ratio de PPO, le modèle de "
                   "Bradley-Terry et la pénalité KL de RLHF.",
        "teaches": ["astuce de la dérivée du logarithme (score)", "théorème du gradient de politique",
                    "baseline et réduction de variance", "acteur-critique et GAE", "échantillonnage d'importance",
                    "ratio et clipping de PPO", "modèle de Bradley-Terry", "pénalité KL (RLHF, DPO)"],
        "after": ["M04", "M18", "M26", "M06"],
        "mymath": {"module": "policy_gradient.py",
                   "functions": ["discounted_returns", "gae", "importance_ratio", "bradley_terry_loss"]},
    },
]
