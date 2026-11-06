"""Syllabus, part VI (before workbookIA chapters 25 to 29): planned."""

CHAPTERS = [
    {
        "id": "M25a", "dir": "m25a_gaussienne", "hours": 14, "generation_sessions": 1, "mml": ["§6.5"],
        "summary": "La loi gaussienne multivariée : densité et géométrie (ellipses), marginales et conditionnelles, "
                   "transformations affines, échantillonnage par Cholesky, produit de gaussiennes, divergence KL entre "
                   "gaussiennes, et l'interpolation sphérique.",
        "teaches": ["gaussienne multivariée : densité", "géométrie : ellipses de niveau", "marginales et "
                    "conditionnelles", "transformations affines d'une gaussienne", "échantillonnage par Cholesky",
                    "produit de gaussiennes", "divergence KL entre gaussiennes", "interpolation sphérique (slerp)"],
        "after": ["M12c", "M02b", "M06"],
        "mymath": {"module": "gaussian.py",
                   "functions": ["mvn_pdf", "sample_mvn", "condition_gaussian", "kl_gaussians", "slerp"]},
    },
    {
        "id": "M25b", "dir": "m25b_variables_latentes", "hours": 12, "generation_sessions": 1,
        "mml": ["§6.7", "§8.4", "§8.5", "ch. 11"],
        "summary": "Les variables latentes et les modèles graphiques orientés, l'inégalité de Jensen, les mélanges de "
                   "gaussiennes et l'algorithme EM, la borne inférieure de l'évidence (ELBO), l'astuce de "
                   "reparamétrisation et le β-VAE.",
        "teaches": ["variables latentes, espace latent", "modèles graphiques orientés", "inégalité de Jensen",
                    "mélanges de gaussiennes", "algorithme EM", "ELBO", "astuce de reparamétrisation",
                    "β-VAE : pondérer le terme KL"],
        "after": ["M25a", "M04"],
        "mymath": {"module": "latent.py",
                   "functions": ["gmm_e_step", "gmm_m_step", "elbo_gaussian", "reparameterize"]},
    },
    {
        "id": "M26", "dir": "m26_markov_bellman", "hours": 12, "generation_sessions": 1, "mml": [],
        "summary": "Les chaînes de Markov (matrice de transition, loi à n pas, loi stationnaire), le processus de "
                   "décision markovien, l'espérance conditionnelle, le retour actualisé, l'équation de Bellman "
                   "(système linéaire et point fixe), l'itération sur les valeurs, le Q-learning et le biais du "
                   "maximum. Référence libre : Blitzstein et Hwang.",
        "teaches": ["chaîne de Markov, matrice de transition", "loi à n pas", "loi stationnaire",
                    "processus de décision markovien", "politique", "espérance conditionnelle", "retour actualisé",
                    "équation de Bellman : système linéaire", "point fixe et contraction",
                    "itération sur les valeurs", "Q-learning et SARSA comme approximations du point fixe",
                    "biais du maximum : E[max] ≥ max E (Double DQN)"],
        "after": ["M09a", "R5", "M02b", "M25b"],
        "mymath": {"module": "markov.py",
                   "functions": ["n_step_distribution", "stationary_distribution", "policy_evaluation",
                                 "value_iteration"]},
    },
    {
        "id": "M27", "dir": "m27_jeux_distances", "hours": 10, "generation_sessions": 1, "mml": [],
        "summary": "Les jeux à somme nulle et le minimax, l'équilibre de Nash, le discriminateur optimal d'un GAN, "
                   "la divergence de Jensen-Shannon, la distance de Wasserstein en 1D, la distance de Fréchet entre "
                   "gaussiennes, et la mesure d'un décalage de distribution.",
        "teaches": ["jeux à somme nulle, minimax", "équilibre de Nash (idée)", "discriminateur optimal (dérivation)",
                    "divergence de Jensen-Shannon", "distance de Wasserstein en 1D", "distance de Fréchet entre "
                    "gaussiennes", "décalage de distribution et dérive : les mesurer"],
        "after": ["M06", "M25a", "M12c"],
        "mymath": {"module": "distances.py",
                   "functions": ["minimax_value", "wasserstein_1d", "frechet_distance"]},
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
    },
    {
        "id": "CP6", "dir": "checkpoints/partie_6", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie VI (M25a à M28) et synthèse, juste avant le checkpoint VI de "
                   "workbookIA.",
        "teaches": ["révision de la partie VI"],
        "after": ["M28"],
    },
]
