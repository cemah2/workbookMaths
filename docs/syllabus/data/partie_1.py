"""Syllabus, part I (before workbookIA chapters 1 to 6): planned. Exercises detailed before the part is generated.

Sharing rule (BIBLE §8, §24): every proof (∂) of the workbookIA chapter a math chapter prepares is a frontier
(tools/syllabus.py adds them); ``frontieres`` lists further workbookIA exercises not to solve in advance. A math
chapter teaches the tool in another setting and may state a result whose proof workbookIA asks.
"""

CHAPTERS = [
    {
        "id": "M02a", "dir": "m02a_integrales_densites", "hours": 14, "generation_sessions": 1,
        "mml": ["(prérequis de §6.2)"],
        "summary": "L'intégrale comme aire sous une courbe, les primitives et les méthodes de calcul, les intégrales "
                   "impropres, les méthodes numériques ; puis la densité de probabilité, la fonction de répartition et "
                   "les quantiles, sans lesquels les lois continues de workbookIA 2 restent des boîtes noires.",
        "teaches": ["aire sous une courbe, sommes de Riemann", "primitives", "intégrale, théorème fondamental",
                    "intégration par parties", "changement de variable", "intégrales impropres",
                    "intégrale de Gauss (valeur admise, vérifiée numériquement ; démontrée en M02b)",
                    "méthodes des rectangles, des trapèzes et de Simpson", "densité de probabilité",
                    "fonction de répartition", "quantiles et percentiles", "l'AUC est une aire"],
        "after": ["R7", "R8", "R6"],
        "mymath": {"module": "integrate.py",
                   "functions": ["riemann_sum", "trapezoid", "simpson", "cdf_from_pdf", "quantile"]},
        "notes": "Parcours essentiel : intégration par parties, changement de variable et Simpson hors parcours "
                 "(workbookIA 2 n'en a pas besoin).",
    },
    {
        "id": "M02b", "dir": "m02b_variables_aleatoires", "hours": 14, "generation_sessions": 1,
        "mml": ["§6.1", "§6.2", "§6.4", "§6.7"],
        "summary": "Les variables aléatoires discrètes et continues et leurs lois usuelles, l'espérance et la variance, "
                   "les couples de variables (loi jointe, marginales, indépendance, variance d'une somme), une première "
                   "intégrale double, le changement de variable et la simulation par inversion.",
        "teaches": ["espace probabilisé (aperçu)", "lois discrètes : Bernoulli, binomiale, catégorielle, géométrique, "
                    "Poisson", "lois continues : uniforme, exponentielle, normale", "espérance d'une variable continue",
                    "variance, propriétés", "couples de variables discrètes : loi jointe, marginales",
                    "indépendance de deux variables aléatoires", "linéarité de l'espérance",
                    "variance d'une somme de variables indépendantes",
                    "intégrale double sur un rectangle, densité jointe, marginale par intégration (premier contact)",
                    "l'intégrale de Gauss par une intégrale double", "théorème de transfert", "changement de variable",
                    "simulation par inversion", "tirage catégoriel"],
        "after": ["M02a", "R8"],
        "mymath": {"module": "distributions.py",
                   "functions": ["binomial_pmf", "poisson_pmf", "normal_pdf", "normal_cdf", "inverse_transform_sample"]},
    },
    {
        "id": "M02c", "dir": "m02c_echantillons_estimation", "hours": 14, "generation_sessions": 1,
        "mml": ["§6.4"],
        "summary": "De la loi à l'échantillon : variables i.i.d., tirages avec et sans remise, loi des grands nombres "
                   "et théorème central limite, estimateurs, leur biais et leur erreur quadratique (le ddof), erreur "
                   "type, intervalles de confiance et bootstrap ; puis la covariance et la corrélation, et une première "
                   "matrice de covariance.",
        "teaches": ["statistiques descriptives : moyenne, médiane, variance, quantiles", "z-score, standardisation",
                    "échantillon i.i.d.", "tirages avec et sans remise", "loi des grands nombres",
                    "théorème central limite", "estimateur, biais, ddof", "erreur quadratique d'un estimateur",
                    "erreur type", "intervalle de confiance", "bootstrap (principe)",
                    "covariance et corrélation", "matrice de covariance (première rencontre)",
                    "valeurs aberrantes : z-score et écart interquartile", "imputer par la moyenne ou la médiane : "
                    "ce que cela change", "biais d'échantillonnage", "grande dimension (premières surprises)",
                    "percentiles d'une mesure (latence)"],
        "after": ["M02b", "R9", "R4"],
        "mymath": {"module": "estimation.py",
                   "functions": ["sample_means", "estimator_bias", "estimator_mse", "standard_error",
                                 "confidence_interval_mean"]},
        "notes": "mymath étudie les estimateurs (biais, erreur quadratique, théorème central limite par simulation) ; "
                 "les fonctions de statistiques descriptives et de bootstrap sont celles de `mylearn` en workbookIA 2.",
    },
    {
        "id": "M03", "dir": "m03_probabilites_conditionnelles", "hours": 12, "generation_sessions": 1,
        "mml": ["§6.3"],
        "summary": "Les probabilités jointes, marginales et conditionnelles, les tableaux de contingence, "
                   "l'indépendance et la formule des probabilités totales ; puis les métriques de classification vues "
                   "comme des probabilités conditionnelles, leurs moyennes, la prévalence, et l'AUC comme une aire et "
                   "comme une probabilité.",
        "teaches": ["probabilité jointe", "probabilité marginale", "tableau de contingence", "probabilité "
                    "conditionnelle", "indépendance", "probabilités totales (énoncée et utilisée)",
                    "precision, recall, spécificité, accuracy comme probabilités", "F-beta (moyenne harmonique pondérée)",
                    "moyennes macro, micro et pondérée", "prévalence et classes déséquilibrées : repondérer",
                    "courbe ROC et AUC", "AUC comme probabilité de bien classer une paire", "courbe precision-recall",
                    "average precision : une aire sous la courbe precision-recall", "calibration et score de Brier",
                    "taux par groupe (équité, premier contact)", "matrice de confusion : un tableau de contingence",
                    "balanced accuracy : la moyenne des rappels", "MCC : une corrélation entre deux variables binaires",
                    "seuil de décision et compromis"],
        "after": ["R8", "M02a", "M02c"],
        "mymath": {"module": "conditional.py",
                   "functions": ["joint_from_counts", "marginal", "conditional", "are_independent", "auc_by_pairs"]},
    },
    {
        "id": "M04", "dir": "m04_bayes_beta", "hours": 12, "generation_sessions": 1,
        "mml": ["§6.3", "§6.6", "§8.3"],
        "summary": "La formule de Bayes en profondeur : a priori, vraisemblance, évidence, a posteriori, mises à jour "
                   "successives, hypothèses multiples ; la loi Beta, la conjugaison avec la binomiale et un aperçu de la "
                   "famille exponentielle, le lissage de Laplace, le MAP, les log-probabilités et les intervalles de "
                   "crédibilité.",
        "teaches": ["formule de Bayes", "a priori, vraisemblance, évidence, a posteriori", "mise à jour séquentielle",
                    "hypothèses multiples", "argmax et MAP", "loi Beta", "conjugaison Beta-binomiale",
                    "famille exponentielle (aperçu : Bernoulli, gaussienne, Beta)", "lissage de Laplace",
                    "log-probabilités et underflow", "intervalle de crédibilité", "fréquentiste et bayésien",
                    "échantillonnage de Thompson (premier contact)"],
        "after": ["M03", "M02b"],
        "mymath": {"module": "bayes.py",
                   "functions": ["beta_pdf", "beta_moments", "conjugate_beta_update", "posterior_predictive",
                                 "map_estimate_beta"]},
        "notes": "mymath écrit les formules de la loi Beta et de la conjugaison ; le posterior sur une grille et "
                 "l'intervalle de crédibilité sont les fonctions de `mylearn` en workbookIA 4.",
    },
    {
        "id": "M05a", "dir": "m05a_derivees_taylor", "hours": 14, "generation_sessions": 1,
        "mml": ["§5.1"],
        "summary": "La dérivée seconde et la convexité en une variable, les polynômes de Taylor, la méthode de Newton, "
                   "l'erreur des différences finies et le choix du pas, les nombres flottants, les erreurs d'arrondi, "
                   "l'overflow et l'underflow, et le log-sum-exp qui rend les calculs stables.",
        "teaches": ["dérivée seconde", "convexité en une variable", "extrema locaux et globaux",
                    "polynômes de Taylor, reste", "méthode de Newton", "différences finies avant et centrée : l'erreur "
                    "par Taylor (cas général)", "choix du pas h : troncature et arrondi", "nombres flottants",
                    "erreurs d'arrondi", "overflow et underflow", "log-sum-exp et stabilité numérique"],
        "after": ["R7", "R5"],
        "mymath": {"module": "approx.py",
                   "functions": ["taylor_polynomial", "newton", "finite_difference_errors", "best_step", "logsumexp"]},
    },
    {
        "id": "M05b", "dir": "m05b_gradient", "hours": 14, "generation_sessions": 1,
        "mml": ["§5.2"],
        "summary": "Les fonctions de deux variables et plus : surfaces et lignes de niveau, dérivées partielles, "
                   "gradient et dérivée directionnelle, plan tangent, dérivées partielles secondes et classement d'un "
                   "point critique en dimension 2, et la descente de gradient vue comme « descendre la plus grande "
                   "pente ».",
        "teaches": ["fonctions de plusieurs variables", "surfaces et lignes de niveau", "dérivées partielles",
                    "gradient", "dérivée directionnelle", "plus grande pente", "plan tangent",
                    "dérivées partielles secondes, courbure dans une direction",
                    "points critiques : minimum, maximum, selle (test en dimension 2)",
                    "descente et montée de gradient (principe)", "argmin et argmax"],
        "after": ["M05a", "R9"],
        "mymath": {"module": "multivar.py",
                   "functions": ["partial_derivative", "directional_derivative", "steepest_ascent_direction",
                                 "tangent_plane"]},
        "notes": "Le gradient numérique, la descente de gradient et le classement d'un point critique sont les "
                 "fonctions de `mylearn` en workbookIA 5 ; mymath écrit les briques (dérivée partielle, dérivée "
                 "directionnelle, plan tangent). Coût : 14 h au lieu de 12 (test du second ordre ajouté).",
    },
    {
        "id": "M06", "dir": "m06_information", "hours": 12, "generation_sessions": 1, "mml": [],
        "summary": "La théorie de l'information : quantité d'information, entropie, entropies conjointe et "
                   "conditionnelle, information mutuelle, cross-entropy, divergence KL et sa positivité (inégalité de "
                   "Jensen), Jensen-Shannon, codes et inégalité de Kraft, perplexité. Référence libre : MacKay.",
        "teaches": ["information de Shannon", "bits et nats", "entropie", "entropie conjointe et conditionnelle",
                    "information mutuelle", "cross-entropy, log loss", "divergence KL", "inégalité de Jensen",
                    "positivité de la divergence KL", "divergence de Jensen-Shannon",
                    "codes de longueur fixe et variable", "inégalité de Kraft, code de Huffman", "perplexité",
                    "sélectionner des features par l'information mutuelle (idée)"],
        "after": ["M02b", "M03", "M05a", "R6"],
        "mymath": {"module": "info.py",
                   "functions": ["joint_entropy", "conditional_entropy", "mutual_information", "kraft_sum",
                                 "jensen_gap"]},
        "notes": "Entropie, cross-entropy, KL et perplexité sont les fonctions de `mylearn` en workbookIA 6 ; mymath "
                 "écrit ce qui les entoure (entropies conjointe et conditionnelle, information mutuelle, Kraft, "
                 "écart de Jensen).",
    },
    {
        "id": "CP1", "dir": "checkpoints/partie_1", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie I (M02a à M06) et synthèse, juste avant le checkpoint I de workbookIA.",
        "teaches": ["révision de la partie I"],
        "after": ["M06"],
    },
]
