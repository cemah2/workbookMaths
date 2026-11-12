"""Syllabus, part IV (before workbookIA chapters 16 to 20): detailed in session 48 (M16 to M20, CP4).

Format: tools/syllabus.py. Exercise tuple: (id, type, stars, minutes, title, covers, flags);
flags: E (essential track), c:wbm|pytest|manuel, f:02|03, p:prerequisites, m:mymath functions written.

Sharing rule (BIBLE §8, §24): every proof (∂) of the workbookIA chapter a math chapter prepares is a frontier
(tools/syllabus.py adds them); ``frontieres`` lists further workbookIA exercises not to solve nor paraphrase. A math
chapter teaches the tool in another setting and may state a result whose proof workbookIA asks. Part IV is where
workbookIA builds networks: the math chapters work on affine maps of the plane, graphs of streets and tasks, formulas
of physics, linear systems, surveys and arrays of measurements, never on a layer, an activation, a loss of
classification or an optimizer. MML blocks are read in the 📖 exercises (the reading time is in those exercises). The
notes of each chapter list the data of workbookIA to avoid; CP4 is also compared with the checkpoint IV and the
mini-project IV of workbookIA.
"""

CHAPTERS = [
    {
        "id": "M16", "dir": "m16_couches_affines", "hours": 8.0, "generation_sessions": 1, "mml": [],
        "summary": "Les outils d'un réseau feed-forward, pris hors des réseaux : les applications affines dans les deux "
                   "conventions (x W + b et W x + b) et leurs formes, leur composition par les coordonnées homogènes, "
                   "les graphes orientés lus sur leur matrice d'adjacence (degrés, chemins comptés par les puissances, "
                   "graphe sans cycle et matrice nilpotente, numérotation qui la rend triangulaire, somme sur les "
                   "chemins), puis l'espérance et la variance d'un produit de variables indépendantes, la variance "
                   "d'une somme de produits seulement décorrélés, et des variances qui se multiplient d'étage en étage. "
                   "workbookIA 16 les applique aux couches, à l'ordre topologique et à l'initialisation.",
        "objectives": [
            "Écrire une application affine de ℝⁿ dans ℝᵐ dans les deux conventions (x W + b et W x + b), avec la forme "
            "de chaque objet, et compter ses paramètres.",
            "Composer des applications affines en multipliant leurs matrices en coordonnées homogènes.",
            "Lire un graphe orienté sur sa matrice d'adjacence : degrés entrants et sortants, chemins de longueur k "
            "comptés par Aᵏ.",
            "Reconnaître un graphe sans cycle par la nilpotence de sa matrice d'adjacence, numéroter ses nœuds pour la "
            "rendre triangulaire, et sommer sur ses chemins.",
            "Calculer l'espérance et la variance d'un produit de variables indépendantes, et la variance d'une somme "
            "de variables seulement décorrélées.",
            "Suivre une variance multipliée par le même facteur à chaque étage, et prévoir son explosion ou son "
            "extinction.",
        ],
        "sections": [("§1", "Applications affines : formes et conventions"),
                     ("§2", "Composer des applications affines : les coordonnées homogènes"),
                     ("§3", "Graphes orientés et matrice d'adjacence"),
                     ("§4", "Graphes sans cycle : nilpotence, numérotation triangulaire, somme sur les chemins"),
                     ("§5", "Espérance et variance d'un produit de variables indépendantes"),
                     ("§6", "Sommes de produits : décorrélées suffit"),
                     ("§7", "Des variances qui se multiplient d'étage en étage")],
        "teaches": ["application affine de ℝⁿ dans ℝᵐ : conventions ligne (x W + b) et colonne (W x + b), formes",
                    "nombre de paramètres d'une application affine (n m + m)",
                    "coordonnées homogènes : composer des applications affines, c'est multiplier des matrices",
                    "graphe orienté : degrés entrant et sortant, matrice d'adjacence",
                    "chemins de longueur k : les puissances de la matrice d'adjacence",
                    "graphe sans cycle ⇔ matrice d'adjacence nilpotente ⇔ numérotation qui la rend triangulaire",
                    "somme sur les chemins des produits de poids : (I − A)⁻¹ = I + A + … + Aⁿ⁻¹",
                    "espérance et variance d'un produit de variables indépendantes",
                    "covariance nulle sans indépendance ; variance d'une somme de variables décorrélées",
                    "multiplicateurs aléatoires centrés : des produits εᵢ xᵢ décorrélés même quand les xᵢ sont "
                    "corrélés",
                    "variance multipliée par un facteur g à chaque étage : gᴸ"],
        "requires": [("Z = XW + b : la convention des poids, produit matriciel, formes, coût d'un produit", "M09a"),
                     ("produit de Hadamard", "M09a"),
                     ("applications affines, composition et produit de matrices, réciproque", "M12a"),
                     ("matrices triangulaires, valeurs propres d'une matrice triangulaire", "M12c"),
                     ("variance, indépendance, variance d'une somme de variables indépendantes, lois uniforme et "
                      "normale", "M02b"),
                     ("covariance, corrélation", "M02c"), ("suites géométriques", "R5"),
                     ("raisonnement par récurrence", "R4"), ("dénombrement", "R8")],
        "frontieres": ["16.1", "16.2", "16.3", "16.4", "16.8", "16.Q10", "16.15", "16.19", "16.23", "17.1", "17.3"],
        "mymath": {"module": "affine.py",
                   "functions": ["homogeneous_matrix", "sum_over_paths", "variance_of_product"]},
        "reading_minutes": 80,
        "flashcards": 12,
        "notes": "Frontières : les ∂ 16.6 (la symétrie des neurones jumeaux) et 16.7 (retrouver LeCun, Glorot et He), "
                 "16.1 (compter les paramètres d'un MLP), 16.2 (une passe avant 2-2-1), 16.3 (formes et diffusion "
                 "d'un mini-batch), 16.4 (Kahn à la main, compter les ordres topologiques), 16.8 (Fermi d'un MLP pour "
                 "MNIST), 16.Q10 (écarts-types de LeCun, Glorot et He), 16.15 (hauteurs de densité), 16.19 (jumeaux "
                 "sur un XOR), 16.23 (profils d'écart-type sur 20 couches), 17.1 (la couche équivalente d'un réseau "
                 "linéaire) et le ∂ 17.3 (une composée d'affines est affine, sa matrice et son biais, la "
                 "caractérisation des fonctions affines, le nombre de morceaux d'un réseau ReLU). M16 enseigne les "
                 "outils hors réseau. Les applications affines sont des transformations du plan et de l'espace "
                 "(rotations, homothéties, translations) ; que la composée de deux applications affines soit affine "
                 "est énoncé (M12a l'énonçait aussi ; ∂ 17.3.1 le démontre) et calculé en coordonnées homogènes, sans "
                 "formule générale du biais équivalent d'une suite de couches. Les graphes sont des rues à sens "
                 "unique, des tâches et des prérequis, lus sur leur matrice d'adjacence (chemins comptés par Aᵏ, sans "
                 "cycle ⇔ nilpotente ⇔ numérotation triangulaire, somme sur les chemins, qui prépare la règle de la "
                 "chaîne de M18), sans l'algorithme de Kahn ni `graphlib` (la fiche de workbookIA 16 et "
                 "`mylearn.nn.layers.topological_order`). La variance d'un produit est prise avec des moyennes non "
                 "nulles (un prix fois une quantité), la décorrélation de produits εᵢ xᵢ (εᵢ centrés, indépendants de "
                 "mesures xᵢ corrélées) sur des signes aléatoires, sans poids, fan-in, ni variance réglée pour se "
                 "conserver d'une couche à l'autre : le §6 énonce ce lemme sans le démontrer (c'est la première étape de "
                 "∂ 16.7.1, et l'encadré de la fiche 16 l'énonce aussi), et M16.6 prend des Var(εᵢ) et des E[xᵢ²] "
                 "différents, pour que le résultat ne soit pas n Var(ε) E[x²] ; la croissance gᴸ sur une chaîne "
                 "d'amplificateurs bruités. « Décorrélées sans être indépendantes » n'est pas un 🗣️ (workbookIA 2.E4, "
                 "frontière de M02c). M16.10 reste sur l'algèbre de X W + 1bᵀ, sans piège de forme du biais (16.3, "
                 "16.20) ; M16.18 n'est pas un `a @ W.T` (16.20) ; M16.19 vérifie sur des images de points "
                 "(f₂(f₁(x)) contre [x, 1] H₁ H₂), sans former W₁W₂ ni b₁W₂ + b₂. Le "
                 "moment d'ordre 2 d'une variable rectifiée n'est pas traité (∂ 16.7.3). La variance de la loi "
                 "uniforme est connue (M02b, (b − a)²/12). Évités (règle de partage) : les réseaux et graphes de "
                 "workbookIA 16 (3-4-4-2, 784-…, 10-8-6-3, 1000-500-100-10, A → C …, U → A …, P, Q, R, S, T, x, h1, "
                 "h2, y), les matrices de sa fiche et de 16.2, 16.13 et 16.17, les neurones R, G, B, les lois 𝒰(±0,05),"
                 " 𝒰(±0,1), 𝒰(±0,2) et 𝒩(0 ; 0,1²), les couches 300 × 300, 400 × 100, 600 × 400 et 200 × 200, les "
                 "gains 1,25, 0,8, 1,5 et 0,5 sur 9, 10, 20 ou 30 étages, le DAG à 4 nœuds et 6 arêtes, la chaîne "
                 "d'usine, le parquet et l'effet Larsen. Conventions de workbookIA suivies : vecteurs en lignes, W de "
                 "forme (n_in, n_out), x W + b, avec le passage à W x + b de MML par transposition ; « degré entrant » "
                 "est le fan-in de workbookIA. Le Hadamard annoncé par M09a sert aux multiplicateurs aléatoires "
                 "(§6). `affine` : NumPy permis, pas `matrix_power`, `inv` ni `solve` dans `sum_over_paths`. 8 h comme"
                 " prévu au §8 : pas de 📖 (MML §6.4 a été lu en M02b et M02c) ni de 🧮.",
        "exercises": [
            ("M16.Q1", "🧠", 1, 4, "Les formes de W, de b et de x W + b, dans chaque convention", "§1", "E"),
            ("M16.Q2", "🧠", 1, 4, "Coordonnées homogènes et composition : vrai ou faux", "§2", "E"),
            ("M16.Q3", "🧠", 1, 4, "Lire une matrice d'adjacence : degrés, arêtes, chemins, cycles", "§3 §4", "E"),
            ("M16.Q4", "🧠", 1, 4, "Indépendantes, décorrélées, ou ni l'un ni l'autre ?", "§5 §6", "E"),
            ("M16.R1", "🔁", 1, 5, "Le produit matriciel, ses formes et son coût (M09a)", "§1", "E"),
            ("M16.R2", "🔁", 1, 5, "La variance d'une somme de variables indépendantes (M02b)", "§5", "E"),
            ("M16.R3", "🔁", 1, 5, "Les valeurs propres d'une matrice triangulaire (M12c)", "§4", ""),
            ("M16.1", "✏️", 1, 15, "Une application affine de ℝ³ dans ℝ² dans les deux conventions : formes, "
             "transposée, nombre de paramètres", "§1", "E"),
            ("M16.2", "✏️", 2, 20, "Rotation, homothétie puis translation du plan : la matrice homogène de la "
             "composée, et celle de la réciproque", "§2", "E"),
            ("M16.3", "✏️", 1, 15, "Des rues à sens unique : degrés, matrice d'adjacence, et chemins de longueur 2 et "
             "3 par ses puissances", "§3", "E"),
            ("M16.4", "✏️", 2, 25, "Un planning de tâches : l'absence de cycle par les puissances de A, une "
             "numérotation qui la rend triangulaire, et le nombre de chemins entre deux tâches", "§4", "E"),
            ("M16.5", "✏️", 2, 15, "Un prix aléatoire fois une quantité indépendante : espérance et variance du "
             "produit", "§5", "E"),
            ("M16.6", "✏️", 2, 20, "Des signes aléatoires d'amplitudes différentes sur des mesures corrélées : la "
             "variance d'une somme de produits", "§6", "E"),
            ("M16.7", "∂", 2, 15, "(Aᵏ)ᵢⱼ compte les chemins de longueur k de i à j, par récurrence", "§3", ""),
            ("M16.8", "∂", 2, 20, "Un graphe est sans cycle si et seulement si sa matrice d'adjacence est "
             "nilpotente", "§4", "E"),
            ("M16.9", "∂", 2, 15, "La variance d'un produit de deux variables indépendantes", "§5", ""),
            ("M16.10", "🔗", 1, 15, "Pont : n points rangés en lignes, X W + 1bᵀ, et la diffusion de b", "§1", "E"),
            ("M16.11", "🗣️", 1, 10, "Expliquer, sur un exemple, pourquoi la variance d'un produit n'est pas le "
             "produit des variances", "§5", "E"),
            ("M16.E1", "💼", 1, 10, "« Pourquoi l'écart-type d'une somme de n termes indépendants grandit-il comme "
             "√n ? »", "§6 §7", ""),
            ("M16.12", "🔨", 1, 15, "La matrice homogène d'une application affine", "§2", "E m:homogeneous_matrix"),
            ("M16.13", "🔨", 2, 20, "Sommer sur les chemins d'un graphe sans cycle par les puissances de sa matrice",
             "§3 §4", "E m:sum_over_paths"),
            ("M16.14", "🔨", 1, 15, "Espérance et variance d'un produit de variables indépendantes", "§5",
             "m:variance_of_product"),
            ("M16.15", "🔮", 1, 10, "Prédire l'écart-type d'une somme de produits aléatoires, mesures corrélées ou "
             "non, puis simuler", "§6 §7", "E"),
            ("M16.16", "🔬", 2, 20, "Une variance multipliée d'étage en étage : simuler une chaîne d'amplificateurs "
             "bruités", "§7", ""),
            ("M16.17", "🎨", 1, 15, "L'image d'une figure par une suite d'applications affines du plan, en "
             "coordonnées homogènes", "§2", "E p:M16.12"),
            ("M16.18", "🐛", 1, 15, "Chasse à l'erreur : une matrice homogène écrite pour des colonnes et appliquée à "
             "des lignes, Var(XY) = Var X · Var Y, et (I − A)⁻¹ sur un graphe qui a un cycle", "§1 §4 §5", "E"),
            ("M16.19", "🛠️", 1, 15, "Un test de propriété : la matrice homogène d'une composée est le produit des "
             "matrices homogènes", "§2", "p:M16.12"),
            ("M16.20", "🏆", 3, 25, "Défi : la loi du produit de deux uniformes indépendantes, sa densité et ses deux "
             "premiers moments", "§5", ""),
        ],
    },
    {
        "id": "M17", "dir": "m17_jacobienne", "hours": 10.2, "generation_sessions": 1, "mml": ["§5.3"],
        "summary": "La dérivée d'une application de ℝⁿ dans ℝᵐ : la jacobienne (une ligne par sortie, une colonne par "
                   "entrée), diagonale pour une fonction appliquée coordonnée par coordonnée, la règle de la chaîne "
                   "comme produit de jacobiennes, les deux conventions de gradient (en ligne pour MML, de la forme de "
                   "la variable pour NumPy), les produits jacobienne-vecteur et vecteur-jacobienne qui évitent de "
                   "former la matrice ; puis les fonctions définies par morceaux et les longues compositions, dont la "
                   "dérivée est un produit de dérivées, et la loi de Boltzmann (translation des énergies, "
                   "température), dont la matrice diag(p) − ppᵀ est la covariance d'un vecteur one-hot. workbookIA 17 "
                   "applique ces outils aux activations et à la softmax.",
        "objectives": [
            "Calculer la jacobienne d'une application de ℝⁿ dans ℝᵐ, et s'en servir comme approximation linéaire.",
            "Reconnaître une jacobienne diagonale, et la calculer avec une seule paire d'évaluations.",
            "Dériver une composée par le produit des jacobiennes, dans le bon ordre et avec les bonnes formes.",
            "Passer du gradient en ligne de MML au gradient de la forme de la variable de NumPy.",
            "Calculer un produit jacobienne-vecteur ou vecteur-jacobienne sans former la jacobienne.",
            "Dériver une fonction définie par morceaux, et suivre la dérivée d'une longue composition.",
            "Calculer une loi de Boltzmann et ses limites en température, et la covariance diag(p) − ppᵀ d'un vecteur "
            "one-hot.",
        ],
        "sections": [("§1", "La jacobienne d'une application de ℝⁿ dans ℝᵐ"),
                     ("§2", "Fonctions appliquées coordonnée par coordonnée : une jacobienne diagonale"),
                     ("§3", "La règle de la chaîne : un produit de jacobiennes"),
                     ("§4", "Gradient en ligne ou de la forme de la variable"),
                     ("§5", "Produits jacobienne-vecteur et vecteur-jacobienne"),
                     ("§6", "Fonctions définies par morceaux et longues compositions"),
                     ("§7", "La loi de Boltzmann et la matrice diag(p) − ppᵀ")],
        "teaches": ["jacobienne (lignes = sorties, colonnes = entrées)",
                    "approximation linéaire d'une application de ℝⁿ dans ℝᵐ",
                    "jacobienne diagonale d'une fonction appliquée coordonnée par coordonnée, et produit de Hadamard",
                    "règle de la chaîne multivariée : J_{g∘f} = J_g J_f, somme sur les variables intermédiaires",
                    "gradient en ligne (MML) et gradient de la forme de la variable (NumPy) : ∇(L∘f) = J_fᵀ ∇L",
                    "produit jacobienne-vecteur, produit vecteur-jacobienne",
                    "dérivées à gauche et à droite, fonctions affines par morceaux",
                    "saturation : une dérivée qui tend vers 0 loin de l'origine (arctan′)",
                    "dérivée d'une longue composition : un produit de dérivées, qui s'éteint ou explose",
                    "loi de Boltzmann : invariance par translation des énergies, limites en température",
                    "matrice diag(p) − ppᵀ : covariance d'un vecteur one-hot, symétrique, semi-définie positive, "
                    "noyau contenant 1"],
        "requires": [("dérivées partielles, gradient (vecteur ligne), dérivée directionnelle", "M05b"),
                     ("règle de la chaîne en une variable, dérivées usuelles, |x| et max(0, x)", "R7"),
                     ("exponentielle, logarithme, tanh", "R6"),
                     ("produit matriciel et formes, produit de Hadamard, transposée", "M09a"),
                     ("matrice d'une application linéaire, composition", "M12a"),
                     ("matrices semi-définies positives, valeurs propres, déterminant", "M12c"),
                     ("matrice de covariance", "M02c"), ("loi catégorielle", "M02b"),
                     ("vecteurs one-hot et base canonique", "M07"),
                     ("softmax de trois scores, log-sum-exp, différences finies centrées", "M05a"),
                     ("sous-gradient, un maximum de fonctions affines est convexe", "M13b"),
                     ("applications affines, coordonnées homogènes", "M16")],
        "frontieres": ["17.1", "17.2", "17.5", "17.6", "17.8", "17.16", "17.19", "17.21", "17.23", "17.Q11", "17.Q12"],
        "mymath": {"module": "jacobian.py",
                   "functions": ["numerical_jacobian", "diagonal_jacobian", "jacobian_vector_product"]},
        "reading_minutes": 130,
        "flashcards": 16,
        "notes": "Frontières : les ∂ 17.3 (composée d'affines), 17.4 (dérivées de la sigmoïde, de tanh, de softplus et "
                 "de SiLU) et 17.7 (la jacobienne de la softmax), 17.1, 17.2 (valeurs de neuf activations), 17.5 "
                 "(maxout, cuvette et bosse), 17.6 (softmax à la main), 17.8 (Fermi d'une activation), 17.16 (la "
                 "jacobienne de la softmax en NumPy), 17.19 (température et entropie), 17.21 (saturation sur des "
                 "histogrammes), 17.23 (produit des dérivées sur 10 couches), 17.Q11 et 17.Q12 (softmax translatée, "
                 "dilatée, rapports). M17 n'écrit ni ne dérive aucune "
                 "activation de `mylearn` (ReLU et ses variantes, marches, sigmoïde, tanh, softplus, ELU, SiLU, GELU, "
                 "softmax) : ses exemples sont les coordonnées polaires et sphériques, la normalisation x/‖x‖, "
                 "arctan, t³, sin, cos, et l'itération de cos. La règle de la chaîne multivariée (forme jacobienne) "
                 "est ici et non en M18, car workbookIA 17 s'en sert (∂ 17.7.4, 🔬 17.23), comme l'annonçait M05b. "
                 "La loi de Boltzmann est celle de la physique (niveaux d'énergie, température) : la fiche en énonce "
                 "l'invariance par translation des énergies et les limites T → 0 et T → ∞, sans logits, scores ni "
                 "classes, et sans la dériver ; ses exercices posent des questions de physique (rapports de "
                 "populations e^{−ΔE/T}, énergie moyenne et ses limites, température où le niveau fondamental garde "
                 "la moitié, recuit simulé), jamais la suite « tout décaler, refroidir, chauffer » de 17.6, ni un vrai "
                 "ou faux de translation et de dilatation (17.Q11, 17.Q12), ni un agent qui choisit ses actions "
                 "(workbookIA 26) ; la matrice diag(p) − ppᵀ y est étudiée comme la covariance d'un "
                 "vecteur one-hot (symétrique, semi-définie positive, de noyau contenant 1, de rang K − 1 quand tous "
                 "les pᵢ sont > 0), ce qui tient la note de M13a sans faire ∂ 17.7 : p est une ligne et la matrice "
                 "s'écrit diag(p) − pᵀp (convention de workbookIA), et aucune solution ne calcule (diag(p) − pᵀp) v "
                 "= p ⊙ (v − p · v) (∂ 17.7.6). M17.4 (la jacobienne de x/‖x‖) ne fait aucun lien avec la "
                 "standardisation ni avec le centrage (∂ 20.8). Les produits de dérivées d'une "
                 "longue composition sont pris sur des itérations de point fixe d'une variable, sans le facteur 1/4 "
                 "ni (1/4)ᴸ (CP4.5 de workbookIA), sans dix copies ou dix couches (🔬 17.23, L = 10 de CP4.5), sans "
                 "demander si une composée de fonctions affines par morceaux l'est encore ni compter ses morceaux "
                 "(∂ 17.3.5–6), et sans la phrase « calculer en z, pas en a ». Évités : 47A + 6B + "
                 "61C, h = (2x + 1, −x + 3) et 4x − 4,5, les points ln 2, ln 3 et ln 4, les scores et températures de "
                 "17.6, 17.12 et 17.19, les vecteurs p = (0,1 ; 0,9) et (1/6, 1/3, 1/2), K = 50 000, les limites "
                 "709,78 et 88,7, les escaliers ⌊4z⌋/4 et ⌊5z⌋/5, le train articulé et l'origami ; 💼 M17.E1 ne prend "
                 "pas la softmax ni K = 50 000 comme exemple (∂ 17.7.6). Conventions : "
                 "jacobienne à une ligne par sortie et une colonne par entrée (MML §5.3, comme workbookIA) ; gradient "
                 "en ligne chez MML (M05b) et de la forme de la variable dans NumPy, les deux écrits ; vecteurs en "
                 "lignes pour x W + b. `jacobian` : NumPy permis, pas SymPy ni `scipy.differentiate`. Parcours "
                 "essentiel : la jacobienne diagonale démontrée hors parcours.",
        "exercises": [
            ("M17.Q1", "🧠", 1, 4, "La forme d'une jacobienne", "§1", "E"),
            ("M17.Q2", "🧠", 1, 4, "Diagonale ou pleine ?", "§2", "E"),
            ("M17.Q3", "🧠", 1, 4, "Dans quel ordre multiplier les jacobiennes ?", "§3", "E"),
            ("M17.Q4", "🧠", 1, 4, "Gradient en ligne ou de la forme de la variable", "§4", "E"),
            ("M17.Q5", "🧠", 1, 4, "Jacobienne-vecteur ou vecteur-jacobienne : combien d'opérations ?", "§5", ""),
            ("M17.Q6", "🧠", 1, 4, "La loi de Boltzmann : populations relatives et énergie moyenne", "§7", "E"),
            ("M17.R1", "🔁", 1, 5, "Dérivées partielles et gradient (M05b)", "§1", "E"),
            ("M17.R2", "🔁", 1, 5, "La règle de la chaîne en une variable (R7)", "§3", "E"),
            ("M17.R3", "🔁", 1, 5, "La matrice de covariance (M02c)", "§7", ""),
            ("M17.1", "✏️", 1, 15, "La jacobienne des coordonnées polaires, son déterminant, et l'approximation "
             "linéaire près d'un point", "§1", "E"),
            ("M17.2", "✏️", 1, 15, "Une fonction appliquée coordonnée par coordonnée : la jacobienne diagonale, et son "
             "produit par un vecteur", "§2", "E"),
            ("M17.3", "✏️", 2, 20, "Dériver une composée de trois applications par le produit de leurs jacobiennes",
             "§3", "E"),
            ("M17.4", "✏️", 2, 20, "La normalisation x/‖x‖ : sa jacobienne (I − uuᵀ)/‖x‖, et la direction qu'elle "
             "écrase", "§3 §5", ""),
            ("M17.5", "✏️", 1, 15, "Le gradient d'une fonction scalaire d'une composée, dans les deux conventions : "
             "J_fᵀ ∇L", "§4", "E"),
            ("M17.6", "✏️", 2, 15, "Dérivées à gauche et à droite d'une fonction définie par morceaux, et la dérivée "
             "d'une composée de sept copies d'une fonction lisse", "§6", "E"),
            ("M17.7", "✏️", 2, 15, "Une loi de Boltzmann à quatre niveaux d'énergie : rapports de populations, énergie "
             "moyenne, et la température où le niveau fondamental garde la moitié", "§7", "E"),
            ("M17.8", "∂", 3, 20, "La règle de la chaîne pour des applications de ℝⁿ dans ℝᵐ, à partir de "
             "l'approximation linéaire", "§3", "E"),
            ("M17.9", "∂", 1, 15, "Une fonction appliquée coordonnée par coordonnée a une jacobienne diagonale, et "
             "J v = g′(x) ⊙ v", "§2", ""),
            ("M17.10", "∂", 2, 20, "diag(p) − ppᵀ est la covariance d'un vecteur one-hot : symétrique, semi-définie "
             "positive, de noyau contenant 1", "§7", "E"),
            ("M17.11", "✏️", 2, 15, "Le recuit simulé : une loi de Boltzmann sur cinq configurations, dont on baisse "
             "la température", "§7", ""),
            ("M17.12", "📖", 2, 35, "MML §5.3 : gradients de fonctions à valeurs vectorielles, en anglais",
             "§1 §3 §4", ""),
            ("M17.13", "🗣️", 1, 10, "Expliquer la règle de la chaîne multivariée avec des taux de change entre "
             "monnaies", "§3", "E"),
            ("M17.E1", "💼", 1, 10, "« Qu'est-ce qu'une jacobienne ? Donne un exemple hors du machine learning. »",
             "§1 §5", ""),
            ("M17.14", "🔨", 2, 20, "La jacobienne par différences centrées, colonne par colonne", "§1",
             "E m:numerical_jacobian"),
            ("M17.15", "🔨", 1, 15, "Une jacobienne diagonale avec une seule paire d'évaluations", "§2",
             "E m:diagonal_jacobian p:M17.14"),
            ("M17.16", "🔨", 1, 15, "Un produit jacobienne-vecteur sans former la jacobienne", "§5",
             "m:jacobian_vector_product p:M17.14"),
            ("M17.17", "📦", 1, 15, "`sympy.Matrix.jacobian` et `scipy.differentiate.jacobian` contre ta jacobienne "
             "numérique", "§1 §3", "E p:M17.14"),
            ("M17.18", "🔮", 1, 10, "Prédire la forme et les zéros de la jacobienne d'une composée, puis vérifier",
             "§3", "E"),
            ("M17.19", "🔬", 2, 20, "Une longue composition : une dérivée qui s'éteint ou explose selon la pente au "
             "point fixe", "§6", ""),
            ("M17.20", "🎨", 1, 20, "Une grille du plan déformée par une application non linéaire, et par son "
             "approximation linéaire", "§1", "E"),
            ("M17.21", "🐛", 1, 15, "Chasse à l'erreur : une jacobienne transposée, un produit dans le mauvais ordre, "
             "une jacobienne évaluée au mauvais point", "§3 §4", "E"),
            ("M17.22", "🛠️", 1, 15, "Un test de propriété : J_{g∘f} = J_g J_f sur des applications tirées au hasard",
             "§3", "p:M17.14"),
            ("M17.23", "🏆", 3, 25, "Défi : la jacobienne de l'inversion X ↦ X⁻¹, vue comme une application de "
             "ℝ^{n²} dans ℝ^{n²}", "§3 §5", ""),
        ],
    },
    {
        "id": "M18", "dir": "m18_retropropagation", "hours": 14.0, "generation_sessions": 1,
        "mml": ["§5.4", "§5.5", "§5.6"],
        "summary": "Dériver un calcul entier : le graphe de calcul d'une formule et la règle de la chaîne comme somme "
                   "sur les chemins, le mode direct par les nombres duaux, le mode inverse par des adjoints accumulés "
                   "dans l'ordre inverse, et ce que coûte chaque mode ; puis les gradients par rapport à un vecteur et "
                   "à une matrice (de la forme de la variable), la différentielle df = tr(Gᵀ dX), les identités de MML "
                   "§5.5 (traces, formes bilinéaires, log det), le gradient d'une moyenne, et la vérification d'un "
                   "gradient matriciel par différences centrées. workbookIA 18 en fait la rétropropagation.",
        "objectives": [
            "Écrire le graphe de calcul d'une formule, et dériver sa sortie par la somme, sur les chemins, des "
            "produits des dérivées locales.",
            "Propager à la main des dérivées en mode direct (nombres duaux) et des adjoints en mode inverse.",
            "Choisir le mode selon le nombre d'entrées et de sorties, et en estimer le coût.",
            "Calculer le gradient d'une fonction d'une matrice, de la forme de cette matrice, par les coordonnées "
            "puis par la différentielle.",
            "Dériver une moyenne de fonctions, et vérifier un gradient matriciel par différences centrées.",
        ],
        "sections": [("§1", "Le graphe de calcul d'une formule"),
                     ("§2", "La règle de la chaîne sur un graphe : une somme sur les chemins"),
                     ("§3", "Le mode direct : les nombres duaux"),
                     ("§4", "Le mode inverse : des adjoints, dans l'ordre inverse"),
                     ("§5", "Ce que coûte chaque mode"),
                     ("§6", "Gradients par rapport à une matrice : la forme de la variable"),
                     ("§7", "Les identités du calcul matriciel : traces, formes bilinéaires, log det"),
                     ("§8", "Le gradient d'une moyenne, et vérifier un gradient matriciel")],
        "teaches": ["graphe de calcul d'une formule, variables intermédiaires",
                    "règle de la chaîne sur un graphe : somme sur les chemins des produits des dérivées locales",
                    "mode direct : nombres duaux a + bε, ε² = 0",
                    "mode inverse : adjoints, ordre inverse, accumulation sur les chemins",
                    "coût des modes direct et inverse selon les nombres d'entrées et de sorties ; principe du "
                    "gradient bon marché",
                    "gradient par rapport à un vecteur et à une matrice : la convention de la forme de la variable",
                    "différentielle d'une fonction de matrice : df = tr(Gᵀ dX)",
                    "identités : ∇ aᵀXb, ∇ tr(AX), ∇ tr(XᵀAX), ∇ ‖X‖²_F, ∇ log det X",
                    "comatrice : X com(X)ᵀ = det X · I (énoncée)",
                    "gradient d'une moyenne = moyenne des gradients",
                    "vérifier un gradient matriciel par différences centrées"],
        "requires": [("règle de la chaîne multivariée, jacobiennes, produits jacobienne-vecteur et "
                      "vecteur-jacobienne", "M17"),
                     ("gradient en ligne et gradient de la forme de la variable", "M17"),
                     ("somme sur les chemins d'un graphe sans cycle, numérotation triangulaire", "M16"),
                     ("gradients de aᵀw et wᵀAw", "M09b"), ("trace, déterminant, tr(A x xᵀ)", "M12c"),
                     ("différences finies centrées, erreur relative, choix du pas", "M05a"),
                     ("gradient, dérivée directionnelle", "M05b"), ("produit de Hadamard, transposée", "M09a"),
                     ("centroïde : la moyenne minimise la somme des carrés des distances", "M07"),
                     ("classes Python et surcharge d'opérateurs", "IA:0A")],
        "frontieres": ["18.1", "18.2", "18.3", "18.4", "18.5", "18.9", "18.14", "18.15", "18.16", "18.17", "18.26",
                       "18.27", "18.Q2", "18.E2"],
        "mymath": {"module": "autodiff.py",
                   "functions": ["Dual", "dual_derivative", "forward_gradient", "gradient_from_differential"]},
        "reading_minutes": 160,
        "flashcards": 22,
        "notes": "Frontières : les ∂ 18.6 (les deltas), 18.7 (XᵀΔ, ΔWᵀ, la somme des lignes, la moyenne des gradients "
                 "d'exemples) et 18.8 (le gradient p − y), 18.1, 18.2, 18.3 (la parabole et le learning rate), 18.4 "
                 "et 18.5 (le réseau minuscule à la main), 18.9 (Fermi), 18.14 (les cross-entropies sur les logits), "
                 "18.15 (`dense_backward`), 18.16 (`gradient_check`), 18.17 (les erreurs relatives 1/3, 1 et 5/7), "
                 "18.26 (`Value`), 18.27, 18.Q2 (un million de poids, un million de passes) et 18.E2 (pourquoi pas "
                 "des différences finies poids par poids) : le coût des modes se compare sur des fonctions de ℝⁿ dans "
                 "ℝᵐ (simulations, formules), jamais sur un « modèle » et ses « paramètres ». M18 dérive des formules de physique, de géométrie et d'algèbre linéaire, "
                 "jamais un réseau ni une loss de classification : pas de delta, ni de « ce qui entre fois le delta », "
                 "ni de règle générale ∂L/∂W = Xᵀ ∂L/∂Z. La somme sur les chemins prolonge celle de M16 (des "
                 "dérivées locales sur les arêtes). Le mode inverse est fait à la main sur des graphes de formules et "
                 "démontré en général (les adjoints), et seul le mode direct est programmé (`Dual`, sans `backward` : "
                 "`mylearn.Value` est le mode inverse de workbookIA 18) ; ses exemples ne reprennent ni ab + a en "
                 "(2, −3), ni x² + 2x en 3, ni tanh(x³ − 4x) en 2, ni (ab + c)a en (3, −1, 4), ni `multiplier(2)`. Le "
                 "coût des deux modes est énoncé par le principe du gradient bon marché (Baur et Strassen), sans « deux "
                 "passes avant » ni 2P passes. Les identités sont celles de MML §5.5 (traces, aᵀXb, log det), sans "
                 "‖XW − Y‖² ni ‖Xw − y‖² (M09b, ∂ 18.7) ; la moyenne des gradients est faite sur des fonctions "
                 "quelconques (la médiane géométrique de villes), sans le contre-exemple de la moyenne des produits "
                 "(∂ 18.7.5). Le 🔨 matriciel lit le gradient dans la différentielle (G[i, j] = df(E_ij)) : "
                 "le gradient numérique d'un tableau est `mylearn.calculus.numerical_gradient` de workbookIA 5, à ne "
                 "pas réécrire ; la vérification d'un gradient matriciel se fait par une dérivée le long d'une "
                 "direction H comparée à tr(GᵀH) (la fonction de M05b, ou deux évaluations), sans l'erreur relative "
                 "de `gradient_check` (M05a.28 l'a déjà ; ni les seuils 10⁻⁷ et 10⁻³, ni |k − 1|/(k + 1)), ni la "
                 "matrice [[1, −2], [0,5, 3]] (🔨 19.16). ∇ log det X = X⁻ᵀ (M18.14) s'appuie sur X com(X)ᵀ = "
                 "det X · I, énoncé au §7. Le 🐛 M18.27 corrige un calcul d'adjoints écrit ligne à ligne pour une "
                 "formule donnée, sans classe ni graphe générique (le `+=` de `Value`, 🔨 18.26). La descente sur une "
                 "parabole (encadré et 18.3 de workbookIA) n'est pas traitée : M19 étudie la convergence des "
                 "itérations. Évités aussi : la loss quadratique et ses deltas (0,6 ; −1,2), E(o) = (o − 2)², les "
                 "logits (2 ; 0 ; −1), z = 3, 5, 40 et 1 000, le réseau 2-2-4-3-2, les lunes, Karpathy et les dates "
                 "1970 et 1986. Conventions : gradient de la forme de la variable (NumPy, PyTorch), écrit à côté de "
                 "la convention en ligne de MML ; df = tr(Gᵀ dX). `autodiff` : `math` et NumPy permis, pas SymPy. Pour le 📦 "
                 "M18.23 : `sympy.MatrixSymbol` dérive tr(AX), tr(XᵀAX) et aᵀXb (sans indexer [0, 0]), mais rend 0 "
                 "pour log det X (SymPy 1.14) : passer alors par une matrice de symboles 2 × 2. "
                 "Parcours essentiel : log det et la démonstration du mode inverse hors parcours.",
        "exercises": [
            ("M18.Q1", "🧠", 1, 4, "Lire un graphe de calcul : nœuds, arêtes, ordre d'évaluation", "§1", "E"),
            ("M18.Q2", "🧠", 1, 4, "Combien de chemins, et quelle somme ?", "§2", "E"),
            ("M18.Q3", "🧠", 1, 4, "Calculer avec ε² = 0", "§3", "E"),
            ("M18.Q4", "🧠", 1, 4, "Le mode inverse : dans quel ordre visiter les nœuds ?", "§4", "E"),
            ("M18.Q5", "🧠", 1, 4, "Direct ou inverse, pour n entrées et m sorties ?", "§5", "E"),
            ("M18.Q6", "🧠", 1, 4, "La forme d'un gradient par rapport à une matrice", "§6", "E"),
            ("M18.Q7", "🧠", 1, 4, "Identités de trace : vrai ou faux", "§7", ""),
            ("M18.Q8", "🧠", 1, 4, "Gradient d'une moyenne, moyenne des gradients", "§8", "E"),
            ("M18.R1", "🔁", 1, 5, "La jacobienne d'une composée (M17)", "§2", "E"),
            ("M18.R2", "🔁", 1, 5, "Le gradient de wᵀAw (M09b)", "§7", "E"),
            ("M18.R3", "🔁", 1, 5, "Différences centrées et choix du pas (M05a)", "§8", ""),
            ("M18.1", "✏️", 1, 15, "Le graphe de calcul d'une formule de physique, et l'ordre de ses calculs", "§1",
             "E"),
            ("M18.2", "✏️", 2, 20, "Dériver par la somme sur les chemins : une variable qui sert deux fois", "§2",
             "E"),
            ("M18.3", "✏️", 2, 20, "Le mode direct à la main : des nombres duaux sur une fonction de deux variables",
             "§3", "E"),
            ("M18.4", "✏️", 2, 20, "Le mode inverse à la main : les adjoints d'un graphe de six nœuds", "§4", "E"),
            ("M18.5", "✏️", 2, 20, "Le même gradient par les deux modes, et le compte des opérations", "§3 §4 §5",
             "E"),
            ("M18.6", "✏️", 1, 15, "Le gradient de aᵀXb, de la forme de X", "§6", "E"),
            ("M18.7", "✏️", 2, 20, "Les gradients de tr(AX) et de tr(XᵀAX), coordonnée par coordonnée", "§7", "E"),
            ("M18.8", "✏️", 2, 20, "Le gradient de log det X sur une matrice 2 × 2, à la main puis par la formule",
             "§7", ""),
            ("M18.9", "✏️", 2, 15, "Le gradient d'une moyenne de distances : le point qui minimise la somme des "
             "distances à des villes", "§8", "E"),
            ("M18.10", "✏️", 2, 20, "La différentielle d'une fonction de matrice, df = tr(Gᵀ dX), et le gradient G "
             "qu'on y lit", "§6 §7", ""),
            ("M18.11", "∂", 2, 20, "La règle de la chaîne sur un graphe sans cycle : la somme sur les chemins, nœud "
             "par nœud dans l'ordre de la numérotation", "§2", "E"),
            ("M18.12", "∂", 2, 20, "Les nombres duaux calculent la dérivée : f(a + bε) = f(a) + b f′(a) ε, pour les "
             "sommes, les produits et les composées", "§3", "E"),
            ("M18.13", "∂", 3, 20, "Le mode inverse calcule tout le gradient en un passage : l'adjoint d'un nœud est "
             "la somme, sur ses successeurs, des adjoints fois les dérivées locales", "§4", ""),
            ("M18.14", "∂", 3, 20, "∇ log det X = X⁻ᵀ, par le développement du déterminant selon une ligne", "§7",
             ""),
            ("M18.15", "🔗", 1, 15, "Pont : workbookIA 18 programme le mode inverse ; pour une simulation de ℝ²⁰⁰⁰ dans "
             "ℝ³, combien de passages dans chaque mode ?", "§5", "E"),
            ("M18.16", "🔗", 1, 15, "Pont : de la convention de MML (gradient en ligne) à celle de NumPy et des "
             "bibliothèques de deep learning", "§6", ""),
            ("M18.17", "📖", 2, 40, "MML §5.4 et §5.5 : gradients par rapport à des matrices et identités utiles, en "
             "anglais", "§6 §7", ""),
            ("M18.18", "📖", 2, 35, "MML §5.6 : rétropropagation et différentiation automatique, en anglais",
             "§1 §2 §4 §5", ""),
            ("M18.19", "🗣️", 1, 10, "Expliquer le mode inverse à quelqu'un qui connaît la règle de la chaîne en une "
             "variable", "§4", "E"),
            ("M18.E1", "💼", 1, 10, "« Différentiation automatique, symbolique ou numérique : quelles différences ? »",
             "§3 §4 §5", ""),
            ("M18.E2", "💼", 1, 10, "« Quand le mode direct est-il préférable au mode inverse ? »", "§5", ""),
            ("M18.20", "🔨", 2, 30, "Les nombres duaux : la classe `Dual`, et la dérivée d'une fonction d'une "
             "variable", "§3", "E m:Dual,dual_derivative"),
            ("M18.21", "🔨", 1, 20, "Le gradient en mode direct : n passages avec des nombres duaux", "§3 §5",
             "m:forward_gradient p:M18.20"),
            ("M18.22", "🔨", 1, 15, "Lire le gradient dans la différentielle : G[i, j] = df(E_ij), de la forme de la "
             "variable", "§6 §7", "E m:gradient_from_differential"),
            ("M18.23", "📦", 1, 15, "SymPy : dériver une fonction de matrice symbolique, et comparer aux identités",
             "§7", ""),
            ("M18.24", "🔮", 1, 10, "Prédire le nombre d'opérations de chaque mode, puis le compter", "§5",
             "E p:M18.20"),
            ("M18.25", "🔬", 2, 20, "Différences finies contre nombres duaux : l'erreur selon le pas h", "§3 §8",
             "p:M18.20"),
            ("M18.26", "🎨", 1, 20, "Dessiner un graphe de calcul, avec les dérivées locales sur les arêtes et les "
             "adjoints sur les nœuds", "§1 §4", ""),
            ("M18.27", "🐛", 1, 15, "Chasse à l'erreur : un gradient transposé, un adjoint compté sur un seul chemin, "
             "un pas h trop petit", "§4 §6 §8", "E"),
            ("M18.28", "🛠️", 1, 15, "Tester une classe par ses propriétés : distributivité et dérivées connues des "
             "nombres duaux", "§3", "p:M18.20"),
            ("M18.29", "🏆", 3, 30, "Défi : dériver une boucle, la méthode de Newton pour √a, en mode direct", "§3",
             "p:M18.20"),
        ],
    },
    {
        "id": "M19", "dir": "m19_hessienne_convergence", "hours": 13.8, "generation_sessions": 1,
        "mml": ["§5.7", "§5.8", "§7.1"],
        "summary": "La courbure d'une fonction de n variables, puis la convergence des méthodes itératives : la "
                   "hessienne et Taylor d'ordre 2, la nature d'un point critique par les signes des valeurs propres ; "
                   "les itérations linéaires x ← M x + c, qui convergent quand toutes les valeurs propres de M "
                   "(symétrique) sont de module < 1 ; l'itération de Richardson pour un système A x = b, son pas "
                   "critique 2/λmax, le conditionnement qui fixe la vitesse et le préconditionnement diagonal ; les "
                   "récurrences linéaires d'ordre 2 et le module de leurs racines (le strict minimum sur les nombres "
                   "complexes) ; un gradient estimé sans biais sur un échantillon ; la projection sur une boule et sur "
                   "un pavé. workbookIA 19 en tire le learning rate critique, le momentum, les pas adaptatifs et le "
                   "clipping.",
        "objectives": [
            "Calculer une hessienne, écrire le développement de Taylor d'ordre 2, et classer un point critique de ℝⁿ "
            "par les signes des valeurs propres de la hessienne.",
            "Décider de la convergence d'une itération linéaire x ← M x + c par les valeurs propres de M symétrique.",
            "Choisir le pas de l'itération de Richardson pour un système à matrice symétrique définie positive, et "
            "prévoir le nombre d'itérations par le conditionnement.",
            "Préconditionner un système par une matrice diagonale.",
            "Résoudre une récurrence linéaire d'ordre 2, et décider de sa convergence par le module des racines de "
            "son polynôme caractéristique.",
            "Montrer qu'un gradient estimé sur un échantillon tiré au hasard est sans biais, et calculer sa variance.",
            "Projeter un vecteur sur une boule et sur un pavé, et comparer les directions obtenues.",
        ],
        "sections": [("§1", "La hessienne et Taylor d'ordre 2 en n variables"),
                     ("§2", "Points critiques en dimension n : les signes des valeurs propres"),
                     ("§3", "Itérations linéaires : quand convergent-elles ?"),
                     ("§4", "L'itération de Richardson et le pas critique 2/λmax"),
                     ("§5", "Conditionnement, vitesse et préconditionnement diagonal"),
                     ("§6", "Récurrences linéaires d'ordre 2 et module des racines"),
                     ("§7", "Un gradient estimé sur un échantillon : sans biais, et sa variance"),
                     ("§8", "Projeter sur une boule ou sur un pavé")],
        "teaches": ["hessienne d'une fonction de n variables, symétrique (Schwarz, admis)",
                    "Taylor d'ordre 2 à plusieurs variables",
                    "nature d'un point critique par les valeurs propres de la hessienne (minimum, maximum, selle, "
                    "direction plate)",
                    "itération linéaire x ← M x + c : point fixe, erreur eₖ₊₁ = M eₖ",
                    "convergence pour M symétrique : toutes les valeurs propres de module < 1, vitesse max |λ|",
                    "itération de Richardson pour A x = b (A symétrique définie positive) : 0 < ω < 2/λmax",
                    "conditionnement κ = λmax/λmin et nombre d'itérations ; pas optimal et facteur (κ − 1)/(κ + 1) "
                    "(énoncés)",
                    "préconditionnement diagonal (Jacobi)",
                    "fonctions de courbure bornée (valeurs propres de la hessienne dans [μ, L]) : le pas sous 2/L "
                    "(énoncé)",
                    "récurrence linéaire d'ordre 2 : polynôme caractéristique, matrice compagnon",
                    "nombres complexes : module, conjugué, racines complexes d'un trinôme réel, somme et produit des "
                    "racines (strict minimum)",
                    "convergence d'une récurrence d'ordre 2 : |q| < 1 et |p| < 1 + q",
                    "gradient sur un échantillon : estimateur sans biais, variance en 1/B",
                    "projection sur une boule (direction gardée) et sur un pavé (direction changée)"],
        "requires": [("dérivées partielles secondes, points critiques en dimension 2", "M05b"),
                     ("Taylor en une variable, choix du pas des différences finies", "M05a"),
                     ("valeurs propres, théorème spectral, formes quadratiques, définie positive, hessienne et "
                      "convexité", "M12c"),
                     ("conditionnement", "M12d"),
                     ("suites géométriques, récurrences d'ordre 1, moyenne exponentielle", "R5"),
                     ("trinôme du second degré, discriminant, racines, factorisation", "R3"),
                     ("espérance, variance d'une moyenne, erreur type", "M02c"),
                     ("projection orthogonale, point le plus proche", "M12b"), ("normes L2 et L∞", "M07"),
                     ("gradient de wᵀAw, moindres carrés", "M09b"), ("jacobienne", "M17"),
                     ("gradient d'une moyenne", "M18")],
        "frontieres": ["18.3", "19.2", "19.3", "19.4", "19.5", "19.6", "19.9", "19.Q3", "19.Q5", "19.Q6", "19.Q9",
                       "19.R3", "19.12", "19.14", "19.20", "19.21"],
        "mymath": {"module": "iterative.py",
                   "functions": ["numerical_hessian", "critical_step_size", "richardson_iterates",
                                 "linear_recurrence"]},
        "reading_minutes": 160,
        "flashcards": 22,
        "notes": "Frontières : les ∂ 19.7 (le pas sous 2/a, la quadratique diagonale, le pas optimal, la base propre, "
                 "le momentum) et 19.8 (moyenne exponentielle : mémoire et biais initial), 18.3 (la parabole de "
                 "workbookIA 18), 19.2 à 19.6 (momentum, Nesterov, Adagrad, RMSprop, Adam, AdamW à la main), 19.9 "
                 "(Fermi de la mémoire des optimiseurs), 19.Q3, 19.Q5, 19.Q6, 19.Q9, 19.R3, 19.12, 19.14, 19.20 et "
                 "19.21. M19 démontre le théorème général des itérations linéaires x ← M x + c (M symétrique : "
                 "convergence pour tout départ ⇔ toutes les |λ| < 1) et l'applique à l'itération de Richardson pour "
                 "A x = b ; il énonce seulement qu'un pas de Richardson est un pas de descente de gradient sur "
                 "½ xᵀA x − bᵀx (∂ 19.7 fait la démonstration pour une loss), énonce le pas optimal 2/(λmin + λmax) et "
                 "le facteur (κ − 1)/(κ + 1) sans les démontrer (∂ 19.7.4), et démontre le critère général de "
                 "convergence d'une récurrence d'ordre 2 (|q| < 1 et |p| < 1 + q) sans le spécialiser au momentum "
                 "(∂ 19.7.6) : aucun exercice, ni CP4, n'étudie la méthode de la bille lourde (Frankel, Polyak) "
                 "x ← x + ω(b − A x) + β(x − x₋₁), qui est le momentum ; le défi M19.28 est une récurrence de la "
                 "mécanique (le schéma saute-mouton), dont les racines sont de module 1. Le pont M19.14 énonce sans "
                 "calcul (hors parcours essentiel), et M19.Q4 se lit sur des matrices 2 × 2, sans les quatre "
                 "comportements en dimension 1 (∂ 19.7.1, 19.Q5). Le strict minimum sur les nombres complexes (module, conjugué, racines complexes d'un "
                 "trinôme réel, produit des racines) est ici ; M22 fait le reste (valeurs propres complexes, rayon "
                 "spectral). Le gradient estimé sur un échantillon est étudié comme un estimateur (sans biais, "
                 "variance en 1/B), sur une pente de moindres carrés, sans compter epochs ni mises à jour. La "
                 "projection sur une boule et sur un pavé est faite en géométrie (M07, M12b), sans norme globale de "
                 "gradients ni constante 10⁻⁶ (`mylearn.clip_grad_norm`). Ni optimiseur, ni planning de learning "
                 "rate, ni moyenne exponentielle corrigée du biais (workbookIA 19 et R5), ni nouvelle étude de la "
                 "convexité (M10, M12c, M13b) ; MML §7.3 a été lu en M13b. Évités : les paraboles 5w², w² depuis 1, "
                 "2(w − 1)² depuis 3, 0,05(w − 1)², 5(w + 2)² et 8w², la vallée 1 − e^{−8w²}, Rosenbrock, les "
                 "quadratiques de coefficients (10, 1) et de courbures 1 et 20, κ = 9 et η = 1,8/a₁, κ = 4 × 10⁶ "
                 "(mètres et proportion), les selles x² − y² et 2x² − y², x² + 3y², −x² − y² et une fonction constante (19.Q2), les gradients et hyperparamètres de 19.2 à "
                 "19.6 et de CP4.3 de workbookIA, les vecteurs (6 ; 8), (3 ; 4), (6 ; 0,5), (1 ; 2) et (0,3 ; −0,4) "
                 "et les seuils 5, 1 et 1,5, la comparaison d'angles des notes de 🔨 19.19 (M19.9 compare des "
                 "directions sans angle chiffré de workbookIA), la bille et la vallée étroite. Le pont M19.15 ne "
                 "reprend pas « un learning rate par poids » (19.Q11). Deux « Richardson » dans `mymath` "
                 "(`approx.richardson_derivative` de M05a, `iterative.richardson_iterates`) : la fiche le signale. Le "
                 "module s'appelle `iterative` (et non "
                 "`optim`, le module d'optimiseurs de `mylearn`) ; `condition_number` existe déjà (M12d) et n'est pas "
                 "réécrit ; NumPy permis, `np.linalg.eigvalsh` dans `critical_step_size` seulement, pas "
                 "`np.linalg.solve`, `inv`, `scipy.optimize` ni `scipy.sparse.linalg`. Parcours essentiel : le "
                 "critère d'ordre 2 et la projection démontrés hors parcours.",
        "exercises": [
            ("M19.Q1", "🧠", 1, 4, "La hessienne : de quelle taille, symétrique, de quoi ?", "§1", "E"),
            ("M19.Q2", "🧠", 1, 4, "Minimum, maximum, selle ou direction plate ?", "§2", "E"),
            ("M19.Q3", "🧠", 1, 4, "Converge ou pas : lire les valeurs propres de M", "§3", "E"),
            ("M19.Q4", "🧠", 1, 4, "Le pas de Richardson : lire la convergence sur les valeurs propres de I − ωA",
             "§4", "E"),
            ("M19.Q5", "🧠", 1, 4, "Le conditionnement : ce qui ralentit, ce qui ne change rien", "§5", "E"),
            ("M19.Q6", "🧠", 1, 4, "Module d'un nombre complexe et racines d'un trinôme", "§6", "E"),
            ("M19.Q7", "🧠", 1, 4, "Un gradient estimé sur un échantillon : vrai ou faux", "§7", "E"),
            ("M19.Q8", "🧠", 1, 4, "Boule ou pavé : la direction est-elle gardée ?", "§8", ""),
            ("M19.R1", "🔁", 1, 5, "Le théorème spectral et les valeurs propres d'une matrice symétrique (M12c)",
             "§2 §3", "E"),
            ("M19.R2", "🔁", 1, 5, "Suites géométriques et récurrences d'ordre 1 (R5)", "§3 §6", "E"),
            ("M19.R3", "🔁", 1, 5, "Le conditionnement par la SVD (M12d)", "§5", ""),
            ("M19.1", "✏️", 2, 20, "La hessienne d'une fonction de trois variables, et son développement de Taylor "
             "d'ordre 2", "§1", "E"),
            ("M19.2", "✏️", 2, 20, "Classer les points critiques d'une fonction de trois variables", "§2", "E"),
            ("M19.3", "✏️", 2, 20, "Une itération linéaire 2 × 2 : point fixe, erreur, et convergence par les valeurs "
             "propres", "§3", "E"),
            ("M19.4", "✏️", 2, 20, "Résoudre un système 2 × 2 par l'itération de Richardson : trois pas à la main, et "
             "le pas critique", "§4", "E"),
            ("M19.5", "✏️", 2, 20, "Le meilleur pas de Richardson (énoncé), et le nombre d'itérations pour gagner six "
             "décimales", "§4 §5", "E"),
            ("M19.6", "✏️", 2, 20, "Une récurrence d'ordre 2 à racines réelles : terme général et convergence", "§6",
             "E"),
            ("M19.7", "✏️", 2, 20, "Une récurrence d'ordre 2 à racines complexes : module et oscillation amortie",
             "§6", "E"),
            ("M19.8", "✏️", 2, 20, "Une pente estimée sur B points tirés au hasard : espérance et variance de "
             "l'estimation", "§7", "E"),
            ("M19.9", "✏️", 1, 15, "Projeter un même vecteur sur une boule et sur un pavé : deux points, deux "
             "directions", "§8", "E"),
            ("M19.10", "∂", 3, 25, "Une itération linéaire de matrice symétrique converge pour tout départ si et "
             "seulement si ses valeurs propres sont de module < 1", "§3", "E"),
            ("M19.11", "∂", 2, 15, "L'itération de Richardson converge si et seulement si 0 < ω < 2/λmax", "§4",
             "E"),
            ("M19.12", "∂", 3, 25, "Une récurrence d'ordre 2 converge si et seulement si ses racines sont de module "
             "< 1 : le critère |q| < 1 et |p| < 1 + q", "§6", ""),
            ("M19.13", "∂", 2, 15, "La projection sur une boule est son point le plus proche, et elle garde la "
             "direction", "§8", ""),
            ("M19.14", "🔗", 1, 10, "Pont : un pas de Richardson est un pas de descente sur ½ xᵀA x − bᵀx (énoncé, sans "
             "calcul)", "§4", ""),
            ("M19.15", "🔗", 1, 15, "Pont : le préconditionnement diagonal, une idée commune à plusieurs méthodes de "
             "workbookIA 19", "§5", ""),
            ("M19.16", "📖", 2, 35, "MML §5.7 et §5.8 : dérivées d'ordre supérieur et Taylor à plusieurs variables, en "
             "anglais", "§1", ""),
            ("M19.17", "📖", 2, 40, "MML §7.1 : la descente de gradient, le pas, le momentum et la version "
             "stochastique, en anglais", "§3 §4 §7", ""),
            ("M19.18", "🗣️", 1, 10, "Expliquer, sur un dessin de lignes de niveau, pourquoi un système mal "
             "conditionné converge lentement", "§5", "E"),
            ("M19.E1", "💼", 1, 10, "« Que nous apprend la hessienne en un minimum ? »", "§1 §2", ""),
            ("M19.E2", "💼", 1, 10, "« Pourquoi un mauvais conditionnement ralentit-il une méthode itérative ? »",
             "§5", ""),
            ("M19.19", "🔨", 2, 25, "La hessienne par différences centrées", "§1", "E m:numerical_hessian"),
            ("M19.20", "🔨", 2, 25, "Le pas critique d'une matrice symétrique définie positive, et les itérés de "
             "Richardson", "§4", "E m:critical_step_size,richardson_iterates"),
            ("M19.21", "🔨", 1, 15, "Une récurrence linéaire d'ordre d", "§6", "m:linear_recurrence"),
            ("M19.22", "📦", 1, 15, "`scipy.sparse.linalg.cg` : le gradient conjugué contre Richardson", "§5",
             "p:M19.20"),
            ("M19.23", "🔮", 1, 10, "Prédire le nombre d'itérations de Richardson selon ω, puis vérifier", "§4 §5",
             "E p:M19.20"),
            ("M19.24", "🔬", 2, 20, "Le nombre d'itérations contre le conditionnement : une droite en échelle "
             "logarithmique", "§5", "p:M19.20"),
            ("M19.25", "🎨", 1, 20, "Les itérés de Richardson sur les lignes de niveau d'une forme quadratique",
             "§4 §5", "E p:M19.20"),
            ("M19.26", "🐛", 1, 15, "Chasse à l'erreur : un pas réglé sur λmin, une hessienne non symétrique, le module "
             "d'une racine complexe", "§2 §4 §6", "E"),
            ("M19.27", "🛠️", 1, 15, "Un critère d'arrêt : le résidu relatif ‖b − A x‖/‖b‖ et un nombre maximal "
             "d'itérations", "§4", "p:M19.20"),
            ("M19.28", "🏆", 3, 30, "Défi : le schéma saute-mouton d'un oscillateur, x_{k+1} = (2 − h²Ω²) x_k − "
             "x_{k−1}, borné si et seulement si hΩ < 2", "§6", "p:M19.21"),
        ],
    },
    {
        "id": "M20", "dir": "m20_tenseurs_normalisation", "hours": 7.7, "generation_sessions": 1, "mml": [],
        "summary": "Les tableaux à k dimensions et leurs axes (forme, remodelage, réductions, diffusion), la notation "
                   "d'Einstein et `einsum`, les moyennes et variances le long d'axes (ddof), le centrage vu comme une "
                   "projection orthogonale et la standardisation invariante par translation et dilatation, "
                   "l'estimateur de Horvitz-Thompson (une observation divisée par sa probabilité d'inclusion : sans "
                   "biais, et sa variance), et les applications proches de l'identité x ↦ x + hF(x), dont la "
                   "jacobienne I + hJ garde des produits proches de 1. workbookIA 20 en tire le dropout, les "
                   "normalisations et les connexions résiduelles.",
        "objectives": [
            "Décrire un tableau à k dimensions par sa forme et ses axes, le remodeler, et le réduire le long d'axes "
            "choisis.",
            "Écrire produits, traces et contractions en notation d'Einstein, et les calculer avec `einsum`.",
            "Calculer moyennes et variances le long d'axes, avec le bon ddof, et centrer par diffusion.",
            "Reconnaître le centrage comme une projection orthogonale, et les invariances de la standardisation.",
            "Construire un estimateur sans biais en divisant par une probabilité d'inclusion, et calculer sa "
            "variance.",
            "Calculer la jacobienne d'une application proche de l'identité, et suivre le produit de L telles "
            "jacobiennes.",
        ],
        "sections": [("§1", "Tableaux à k dimensions : forme, axes, remodelage"),
                     ("§2", "Réductions et diffusion le long d'axes"),
                     ("§3", "La notation d'Einstein et `einsum`"),
                     ("§4", "Centrer et réduire : une projection et des invariances"),
                     ("§5", "Diviser par la probabilité d'inclusion : l'estimateur de Horvitz-Thompson"),
                     ("§6", "Des applications proches de l'identité : I + hJ")],
        "teaches": ["tableau à k dimensions (tenseur) : forme, axes, nombre d'éléments, remodelage en ordre C",
                    "réductions le long d'axes, keepdims, diffusion",
                    "notation d'Einstein, einsum, coût d'une contraction",
                    "moyenne et variance le long d'axes, ddof",
                    "matrice de centrage I − (1/m) 11ᵀ : projection orthogonale",
                    "standardisation invariante par translation et par dilatation",
                    "estimateur de Horvitz-Thompson : espérance et variance d'une observation divisée par sa "
                    "probabilité d'inclusion",
                    "application proche de l'identité x ↦ x + hF(x) : jacobienne I + hJ_F, produit de L facteurs, "
                    "(1 + hλ)ᴸ"],
        "requires": [("NumPy : arrays, formes, axis, broadcasting", "IA:0A"),
                     ("moyenne, variance, ddof, z-score, standardisation", "M02c"),
                     ("loi de Bernoulli, espérance, variance d'une somme de variables indépendantes", "M02b"),
                     ("projection orthogonale, matrice de projection", "M12b"),
                     ("produit matriciel, coût d'un produit", "M09a"), ("trace", "M12c"),
                     ("jacobienne, règle de la chaîne", "M17"), ("(1 + x/n)ⁿ → eˣ", "M14"),
                     ("2ⁿ sous-ensembles, dénombrement", "R8"), ("valeurs singulières", "M12d")],
        "frontieres": ["20.3", "20.4", "20.6", "20.7", "20.9", "20.Q5", "20.Q6", "20.17", "20.22", "20.30"],
        "mymath": {"module": "tensors.py",
                   "functions": ["einsum_pair", "moments_along_axes", "horvitz_thompson_total"]},
        "reading_minutes": 90,
        "flashcards": 12,
        "notes": "Frontières : les ∂ 20.5 (espérance et variance du dropout, sous-réseaux, règle du test, Jensen sur une "
                 "ReLU) et 20.8 (le gradient de la batchnorm), 20.3 (dropout à la main), 20.4 (batchnorm à la main), "
                 "20.6 et 20.9 (VGG16), 20.7 (connexion résiduelle et layer norm à la main), 20.Q5, 20.Q6, 20.17 "
                 "(layer norm, RMSNorm), 20.22 et 20.30 (30 couches). M20 enseigne l'estimateur de Horvitz-Thompson "
                 "sur des sondages (communes, entreprises, arbres d'une forêt) : c'est l'outil du dropout inversé "
                 "(diviser par la probabilité d'être gardé), sans neurone, masque ni probabilité de coupure, et sans "
                 "les probabilités 0,5, 0,6, 0,75 et 0,8 ; le centrage est une projection orthogonale (M12b), et la "
                 "standardisation est invariante par translation et dilatation, sans γ, β, statistiques glissantes, "
                 "ε ni dérivée de la standardisation (∂ 20.8) ; I + hJ est la jacobienne d'un pas d'Euler, et le "
                 "produit de L pas, à horizon T = hL fixé, tend vers une exponentielle (M14), sans 0,5³⁰, 1,01³⁰ ni "
                 "0,9 et 44 couches. Le pont M20.8 dit seulement où workbookIA 20 divise par une probabilité, sans "
                 "correspondance π ↔ 1 − p ni formule en p (∂ 20.5.1). Ni la fiche ni un exercice ne composent la "
                 "normalisation x/‖x‖ de M17.4 avec la matrice de centrage, ni ne tirent des invariances de la "
                 "standardisation une propriété de sa jacobienne ou d'un gradient (∂ 20.8.3 et 20.8.5). Les "
                 "tableaux sont des mesures (stations × jours × heures), des notes (élèves × "
                 "matières) et des images en (hauteur, largeur, canaux), sans les formes de workbookIA 20 ((32, 3, 28, "
                 "28), (32, 1, 28, 28), (1, 512, 7, 7), (10, 3, 5), arange(150), arange(30), arange(20)), ni VGG16, "
                 "ni les vecteurs (1, 2, 3, 6), (2, 4, 6, 8), (2 ; 6 ; 8 ; 12), (2, 2, 8, 8) et le tableau 4 × 2 de "
                 "20.4. `einsum` ne sert pas à workbookIA 19 et 20 (il arrive en 21, B3, B6 et 28) : M20 le prépare. "
                 "`tensors` : `einsum_pair` écrit `einsum` pour deux tableaux par des boucles (pas `np.einsum`, "
                 "`tensordot`, `@`, `dot`, `inner` ni `outer`), `moments_along_axes` rend moyenne et variance sans "
                 "normaliser (pas `np.var` ni `np.std`), `horvitz_thompson_total` l'estimation d'un total. Pas de 📖 "
                 "(MML n'a pas de section sur les tenseurs). Réduit à 8 h (§8).",
        "exercises": [
            ("M20.Q1", "🧠", 1, 4, "Forme, axes et nombre d'éléments", "§1", "E"),
            ("M20.Q2", "🧠", 1, 4, "Réduire le long de quel axe ?", "§2", "E"),
            ("M20.Q3", "🧠", 1, 4, "Lire une formule d'einsum", "§3", "E"),
            ("M20.Q4", "🧠", 1, 4, "Diviser par une probabilité : sans biais ou biaisé ?", "§5", "E"),
            ("M20.R1", "🔁", 1, 5, "Variance biaisée et non biaisée : ddof (M02c)", "§2", "E"),
            ("M20.R2", "🔁", 1, 5, "La projection orthogonale sur une droite (M12b)", "§4", "E"),
            ("M20.R3", "🔁", 1, 5, "La limite (1 + x/n)ⁿ → eˣ (M14)", "§6", ""),
            ("M20.1", "✏️", 1, 15, "Un tableau de mesures (stations × jours × heures) : les formes après réductions "
             "et remodelages", "§1 §2", "E"),
            ("M20.2", "✏️", 1, 15, "Écrire en notation d'Einstein : produit matriciel, trace, forme bilinéaire, "
             "produits de matrices empilées le long d'un axe", "§3", "E"),
            ("M20.3", "✏️", 2, 20, "La matrice de centrage, et une standardisation qui ne voit ni translation ni "
             "dilatation", "§4", "E"),
            ("M20.4", "✏️", 2, 20, "Un sondage à probabilités inégales : l'estimateur de Horvitz-Thompson d'un total, "
             "son espérance et sa variance", "§5", "E"),
            ("M20.5", "✏️", 2, 20, "Un schéma d'Euler en L pas : la jacobienne d'un pas, celle de L pas, et la limite "
             "(1 + λT/L)ᴸ", "§6", "E"),
            ("M20.6", "∂", 2, 15, "La matrice de centrage est la projection orthogonale sur l'orthogonal de 1", "§4",
             ""),
            ("M20.7", "∂", 2, 20, "L'estimateur de Horvitz-Thompson est sans biais, et sa variance quand les "
             "inclusions sont indépendantes", "§5", "E"),
            ("M20.8", "🔗", 1, 10, "Pont : où workbookIA 20 divise par une probabilité", "§5", "E"),
            ("M20.9", "🗣️", 1, 10, "Expliquer ce qu'est un axe d'un tableau à quelqu'un qui ne connaît que les "
             "tableurs", "§1 §2", "E"),
            ("M20.E1", "💼", 1, 10, "« Pourquoi standardiser des données décalées ou dilatées donne-t-il le même "
             "résultat ? »", "§4", ""),
            ("M20.10", "🔨", 2, 30, "`einsum` pour deux tableaux, avec des boucles", "§3", "E m:einsum_pair"),
            ("M20.11", "🔨", 1, 15, "Moyennes et variances le long d'axes choisis", "§2", "E m:moments_along_axes"),
            ("M20.12", "🔨", 1, 10, "L'estimateur de Horvitz-Thompson d'un total", "§5",
             "m:horvitz_thompson_total"),
            ("M20.13", "🔮", 1, 10, "Prédire la forme d'une réduction ou d'un einsum, puis vérifier", "§1 §3", "E"),
            ("M20.14", "🔬", 2, 20, "Simuler un sondage : Horvitz-Thompson contre la moyenne naïve, biais et "
             "variance", "§5", "p:M20.12"),
            ("M20.15", "🎨", 1, 20, "Le produit de L jacobiennes I + hJ : ses valeurs singulières extrêmes quand L "
             "grandit, à hL fixé", "§6", "E"),
            ("M20.16", "🐛", 1, 15, "Chasse à l'erreur : une moyenne sur le mauvais axe, une diffusion silencieuse, un "
             "ddof oublié", "§2", "E"),
            ("M20.17", "🛠️", 1, 15, "Un test de propriété : réduire sur deux axes d'un coup, ou l'un après l'autre",
             "§2", "p:M20.11"),
            ("M20.18", "🏆", 3, 25, "Défi : des probabilités d'inclusion proportionnelles à la taille, et un "
             "estimateur presque sans variance", "§5", ""),
        ],
    },
    {
        "id": "CP4", "dir": "checkpoints/partie_4", "hours": 3.1, "generation_sessions": 1, "mml": [],
        "summary": "Le bilan de la partie IV (M16 à M20), juste avant le checkpoint IV de workbookIA : un examen blanc "
                   "d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une "
                   "synthèse (carte mentale et fiche d'une page). Pas de mini-projet.",
        "objectives": [
            "Vérifier en temps limité que les notions de la partie IV sont acquises.",
            "Construire ta propre synthèse de la partie IV.",
        ],
        "sections": [("§1", "Examen blanc"), ("§2", "Synthèse")],
        "teaches": ["révision de la partie IV"],
        "requires": [("toute la partie IV", "M20")],
        "frontieres": ["16.1", "16.2", "16.3", "16.4", "16.6", "16.7", "16.8", "16.Q10", "16.15", "16.19", "16.23",
                       "17.1", "17.2", "17.3", "17.4", "17.5", "17.6", "17.7", "17.8", "17.16", "17.19", "17.21",
                       "17.23", "18.1", "18.2", "18.3", "18.4", "18.5", "18.6", "18.7", "18.8", "18.9", "18.14",
                       "18.15", "18.16", "18.17", "18.26", "18.27", "19.2", "19.3", "19.4", "19.5", "19.6", "19.7",
                       "19.8", "19.9", "19.Q3", "19.Q5", "19.Q6", "19.Q9", "19.R3", "19.12", "19.14", "19.20",
                       "19.21", "20.3", "20.4", "20.5", "20.6", "20.7", "20.8", "20.9", "20.Q5", "20.Q6", "20.17",
                       "20.22", "20.30"],
        "reading_minutes": 15,
        "flashcards": 0,
        "notes": "Fichiers comme CP3 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, "
                 "03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend"
                 " le checkpoint IV de workbookIA (`checkpoints/partie_4/` de workbookIA : le comptage d'un MLP "
                 "20-64-32-3, un réseau 2-2-1 à ReLU à la main, momentum, Adam et AdamW sur deux gradients, dropout "
                 "et batchnorm à la main, le gradient à travers des sigmoïdes empilées et L = 10, le Fermi d'un MLP "
                 "784-1 024-1 024-10 avec AdamW, les bugs d'une boucle PyTorch, des courbes d'entraînement, une epoch "
                 "d'AdamW avec clipping, les manchots et la ridge des parties I à III), qui se fait juste après, ni "
                 "son mini-projet IV (un mini-framework NumPy validé contre PyTorch). La synthèse ne recopie pas le "
                 "tableau des 24 formules de la synthèse de workbookIA. CP4.2 n'est pas une chaîne de fonctions "
                 "d'une variable à dérivée bornée (CP4.5 de workbookIA) ; CP4.6 n'étudie pas la bille lourde (le "
                 "momentum, ∂ 19.7.6) ; CP4.8 donne le choix entre deux énoncés neufs : une matrice symétrique qui "
                 "raccourcit tout vecteur non nul (‖M x‖ < ‖x‖) a ses valeurs propres dans ]−1, 1[, ou "
                 "Var(XY) ≥ Var X · Var Y pour X et Y indépendantes, avec le cas d'égalité ; aucune ne compose la "
                 "normalisation avec le centrage (∂ 20.8). CP4.10 ajuste une loi exponentielle à trois mesures prises "
                 "ailleurs qu'en x = 1, 2, 3 (CP4.12 d de workbookIA), hors réseau : graphe de calcul, gradient par le "
                 "mode inverse, hessienne et pas critique.",
        "exercises": [
            ("CP4.Q1", "🧠", 1, 10, "Dix affirmations sur la partie IV : vrai ou faux", "§1", "E"),
            ("CP4.1", "✏️", 2, 10, "Coordonnées homogènes, chemins d'un graphe et variance d'un produit", "§1", "E"),
            ("CP4.2", "✏️", 2, 10, "Jacobienne d'une composée et produit vecteur-jacobienne", "§1", "E"),
            ("CP4.3", "✏️", 2, 10, "Mode direct et mode inverse sur un graphe de calcul", "§1", "E"),
            ("CP4.4", "✏️", 2, 9, "Gradients par rapport à une matrice", "§1", "E"),
            ("CP4.5", "✏️", 2, 10, "Hessienne, Taylor d'ordre 2 et nature d'un point critique", "§1", "E"),
            ("CP4.6", "✏️", 2, 9, "Itération de Richardson et récurrence d'ordre 2", "§1", "E"),
            ("CP4.7", "✏️", 2, 8, "Moments le long d'axes, einsum et estimateur de Horvitz-Thompson", "§1", "E"),
            ("CP4.8", "∂", 3, 12, "Une démonstration au choix : une matrice qui raccourcit les vecteurs, ou "
             "Var(XY) ≥ Var X · Var Y", "§1", "E"),
            ("CP4.9", "🐛", 2, 8, "Corriger une copie : cinq erreurs", "§1", "E f:02"),
            ("CP4.10", "🔗", 2, 14, "Problème de synthèse : ajuster une loi exponentielle, du graphe de calcul au pas "
             "critique", "§1", "E"),
            ("CP4.11", "🗣️", 1, 60, "Ta carte mentale et ta fiche d'une page", "§2", "E"),
        ],
    },
]
