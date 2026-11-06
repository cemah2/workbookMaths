"""Syllabus, part VI (before workbookIA chapters 25 to 29): planned (sharing rule: see partie_1.py)."""

CHAPTERS = [
    {
        "id": "M25a", "dir": "m25a_gaussienne", "hours": 14, "generation_sessions": 1, "mml": ["§6.5", "§9.3"],
        "summary": "La loi gaussienne multivariée : densité et géométrie (ellipses), matrices par blocs et complément "
                   "de Schur, marginales et conditionnelles, transformations affines, échantillonnage par Cholesky, "
                   "produit de gaussiennes, régression linéaire bayésienne, et l'interpolation sphérique.",
        "teaches": ["gaussienne multivariée : densité", "géométrie : ellipses de niveau",
                    "matrices par blocs et complément de Schur", "marginales et conditionnelles",
                    "transformations affines d'une gaussienne", "échantillonnage par Cholesky",
                    "produit de gaussiennes", "régression linéaire bayésienne (MML §9.3)",
                    "interpolation sphérique (slerp)"],
        "after": ["M12c", "M02b", "M06", "M09b"],
        "mymath": {"module": "gaussian.py",
                   "functions": ["mvn_pdf", "sample_mvn", "marginal_gaussian", "condition_gaussian",
                                 "schur_complement"]},
        "notes": "Frontière : la divergence KL entre N(μ, σ²) et N(0, 1) (workbookIA 25.7) n'est pas calculée ici.",
    },
    {
        "id": "M25b", "dir": "m25b_variables_latentes", "hours": 14, "generation_sessions": 1,
        "mml": ["§6.7", "§8.4", "§8.5", "§10.7", "ch. 11"],
        "summary": "Les variables latentes et les modèles graphiques orientés, l'inégalité de Jensen (rappel de M06), "
                   "les mélanges de gaussiennes et l'algorithme EM, le point de vue latent de l'ACP, la borne inférieure "
                   "de l'évidence (ELBO), et le β-VAE.",
        "teaches": ["variables latentes, espace latent", "modèles graphiques orientés", "inégalité de Jensen (rappel)",
                    "mélanges de gaussiennes", "algorithme EM", "ACP probabiliste (MML §10.7)", "ELBO",
                    "β-VAE : pondérer le terme KL"],
        "after": ["M25a", "M04", "M06", "M12d"],
        "mymath": {"module": "latent.py",
                   "functions": ["gmm_e_step", "gmm_m_step", "gmm_log_likelihood"]},
        "notes": "Coût : 14 h au lieu de 12 (lectures de MML). Frontière : l'astuce de reparamétrisation (workbookIA "
                 "25.5) est démontrée par workbookIA.",
    },
    {
        "id": "M26", "dir": "m26_markov_bellman", "hours": 12, "generation_sessions": 1, "mml": [],
        "summary": "Les chaînes de Markov (matrice de transition, loi à n pas, loi stationnaire), le processus de "
                   "décision markovien, l'espérance conditionnelle, le retour actualisé, l'équation de Bellman d'une "
                   "politique fixée (système linéaire et point fixe d'une contraction), l'itération sur les valeurs, "
                   "et le biais du maximum. Référence libre : Blitzstein et Hwang.",
        "teaches": ["chaîne de Markov, matrice de transition", "loi à n pas", "loi stationnaire",
                    "processus de décision markovien", "politique", "espérance conditionnelle", "retour actualisé",
                    "équation de Bellman d'une politique fixée : système linéaire", "point fixe et contraction",
                    "itération sur les valeurs (principe)", "biais du maximum : E[max] ≥ max E (Double DQN)"],
        "after": ["M09a", "R5", "M02b", "M25b"],
        "mymath": {"module": "markov.py",
                   "functions": ["n_step_distribution", "stationary_distribution", "bellman_linear_solve",
                                 "bellman_fixed_point_iterates"]},
        "notes": "Frontières : l'horizon effectif de γ et le point fixe que vise le Q-learning (workbookIA 26.7, "
                 "26.8) ; l'itération sur les valeurs de `mylearn`.",
    },
    {
        "id": "M27", "dir": "m27_jeux_distances", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "Les jeux à somme nulle et le minimax, l'équilibre de Nash, maximiser a·ln t + b·ln(1 − t), "
                   "le comportement de ln près de 0, la divergence de Jensen-Shannon, la distance de Wasserstein entre "
                   "deux gaussiennes en dimension 1, la distance de Fréchet, et la mesure d'un décalage de "
                   "distribution.",
        "teaches": ["jeux à somme nulle, minimax", "équilibre de Nash (idée)", "maximiser a·ln t + b·ln(1 − t) sur "
                    "]0, 1[", "pentes de ln t et de ln(1 − t) près de 0", "divergence de Jensen-Shannon (rappel)",
                    "distance de Wasserstein : définition, cas de deux gaussiennes en dimension 1",
                    "distance de Fréchet entre gaussiennes (formule)", "décalage de distribution et dérive : les "
                    "mesurer", "GAN : générateur et discriminateur, le jeu mathématique"],
        "after": ["M06", "M25a", "M12c"],
        "mymath": {"module": "distances.py",
                   "functions": ["minimax_value", "mixed_strategy_value_2x2", "w2_gaussians_1d"]},
        "notes": "Frontières : le discriminateur optimal et la saturation de log(1 − D) (workbookIA 27.5, 27.6) ; "
                 "Wasserstein et Fréchet sur des données sont les fonctions de `mylearn`.",
    },
    {
        "id": "M28", "dir": "m28_gram_echantillonnage", "hours": 6, "generation_sessions": 1, "mml": [],
        "summary": "La matrice de Gram, la montée de gradient sur l'entrée, la variation totale d'une image, et "
                   "l'échantillonnage d'une loi catégorielle avec température, top-k et top-p.",
        "teaches": ["matrice de Gram", "montée de gradient sur l'entrée", "variation totale",
                    "échantillonner une loi catégorielle", "température", "top-k et top-p"],
        "after": ["M17", "M09a", "M18"],
        "mymath": {"module": "sampling.py",
                   "functions": ["gram_matrix", "apply_temperature", "top_k_filter", "top_p_filter"]},
        "notes": "Frontières : l'invariance de la matrice de Gram par permutation des positions et le gradient de "
                 "la loss de style (workbookIA 28.3, 28.5).",
    },
    {
        "id": "CP6", "dir": "checkpoints/partie_6", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie VI (M25a à M28) et synthèse, juste avant le checkpoint VI de "
                   "workbookIA.",
        "teaches": ["révision de la partie VI"],
        "after": ["M28"],
    },
]
