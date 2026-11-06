"""Syllabus, part IV (before workbookIA chapters 16 to 20): planned."""

CHAPTERS = [
    {
        "id": "M16", "dir": "m16_couches_affines", "hours": 8, "generation_sessions": 1, "mml": ["§6.4"],
        "summary": "Un réseau comme composition d'applications affines (et pourquoi, sans non-linéarité, il reste "
                   "affine), les graphes orientés acycliques et l'ordre topologique, les conventions de forme et le "
                   "comptage des paramètres, la brisure de symétrie, et la variance à l'initialisation : la dérivation "
                   "des initialisations de Glorot et de He.",
        "teaches": ["composition d'applications affines", "rôle de la non-linéarité", "graphe orienté acyclique",
                    "ordre topologique", "conventions de forme (n_in, n_out)", "comptage des paramètres",
                    "brisure de symétrie", "variance d'une somme de produits indépendants",
                    "fan-in, fan-out", "initialisations LeCun, Glorot et He (dérivation)"],
        "after": ["M09a", "M12a", "M02b"],
        "mymath": {"module": "init.py",
                   "functions": ["compose_affine", "count_parameters", "topological_order", "glorot_std", "he_std"]},
    },
    {
        "id": "M17", "dir": "m17_jacobienne", "hours": 10, "generation_sessions": 1, "mml": ["§5.3"],
        "summary": "La jacobienne, les dérivées des activations (linéaires par morceaux et lisses), la saturation, la "
                   "softmax (translation, température), sa jacobienne, le log-softmax et la convexité du log-sum-exp.",
        "teaches": ["jacobienne", "dérivées des activations : ReLU et variantes, softplus, ELU, SiLU, GELU",
                    "saturation", "softmax, invariance par translation, température", "jacobienne de la softmax",
                    "log-softmax", "convexité du log-sum-exp", "softmax de Boltzmann en RL"],
        "after": ["M05b", "M06", "M05a"],
        "mymath": {"module": "jacobian.py",
                   "functions": ["numerical_jacobian", "softmax", "softmax_jacobian", "log_softmax"]},
    },
    {
        "id": "M18", "dir": "m18_retropropagation", "hours": 14, "generation_sessions": 1,
        "mml": ["§5.4", "§5.5", "§5.6"],
        "summary": "La règle de la chaîne multivariée, les gradients par rapport à une matrice et les identités utiles, "
                   "le graphe de calcul, les modes direct et inverse de la différentiation automatique, un "
                   "micro-autograd, les gradients des losses usuelles, le gradient d'un mini-batch, et la vérification "
                   "de gradient.",
        "teaches": ["règle de la chaîne multivariée (somme sur les chemins)", "gradients par rapport à une matrice",
                    "identités de calcul matriciel", "conventions de forme des gradients", "graphe de calcul",
                    "mode direct et mode inverse", "micro-autograd", "gradients de MSE, BCE sur logits, "
                    "cross-entropy softmax", "gradient d'un mini-batch (moyenne des gradients)",
                    "vérification de gradient", "gradient par rapport à l'entrée (FGSM)"],
        "after": ["M17", "M09a"],
        "mymath": {"module": "autodiff.py", "functions": ["Value", "gradient_check", "matmul_grads"]},
    },
    {
        "id": "M19", "dir": "m19_hessienne_convergence", "hours": 14, "generation_sessions": 1,
        "mml": ["§5.7", "§5.8", "§7.1", "§7.3"],
        "summary": "La hessienne et Taylor à plusieurs variables, le conditionnement, la convergence de la descente de "
                   "gradient sur une quadratique et le pas critique, la descente stochastique, le momentum et Nesterov "
                   "comme suites récurrentes, les pas adaptatifs (Adagrad, RMSprop, Adam) vus comme des moyennes "
                   "exponentielles avec correction du biais, AdamW, le clipping, et les fonctions convexes.",
        "teaches": ["hessienne", "Taylor à plusieurs variables", "géométrie d'une surface quadratique",
                    "conditionnement", "pas critique 2/λmax", "descente stochastique et mini-batch",
                    "momentum et Nesterov", "pas adaptatifs : Adagrad, RMSprop, Adadelta, Adam",
                    "correction du biais (1 − βᵗ)", "AdamW : weight decay découplé", "plannings de learning rate",
                    "gradient clipping par la norme", "fonctions convexes"],
        "after": ["M18", "M12c", "R5"],
        "mymath": {"module": "optim.py",
                   "functions": ["numerical_hessian", "critical_learning_rate", "momentum_iterates", "adam_step",
                                 "clip_by_norm"]},
    },
    {
        "id": "M20", "dir": "m20_tenseurs_normalisation", "hours": 8, "generation_sessions": 1, "mml": [],
        "summary": "Les tableaux à n dimensions et `einsum`, l'espérance et le dropout inversé, la batchnorm et la "
                   "layer norm (moyenne, variance, transformation affine), et pourquoi les connexions "
                   "résiduelles aident le gradient.",
        "teaches": ["tenseurs, axes et `einsum`", "dropout inversé : espérance conservée",
                    "batchnorm : moyenne, variance, transformation affine", "layer norm",
                    "connexions résiduelles et gradient (I + …)"],
        "after": ["M02c", "M19"],
        "mymath": {"module": "tensors.py",
                   "functions": ["einsum_matmul", "dropout_inverted", "batchnorm_forward", "layernorm_forward"]},
    },
    {
        "id": "CP4", "dir": "checkpoints/partie_4", "hours": 4, "generation_sessions": 1, "mml": [],
        "summary": "Examen blanc de la partie IV (M16 à M20) et synthèse, juste avant le checkpoint IV de workbookIA.",
        "teaches": ["révision de la partie IV"],
        "after": ["M20"],
    },
]
