"""Syllabus, part III (before workbookIA chapters 12 to 15): detailed in session 35 (M12a to M14, CP3).

Format: tools/syllabus.py. Exercise tuple: (id, type, stars, minutes, title, covers, flags);
flags: E (essential track), c:wbm|pytest|manuel, f:02|03, p:prerequisites, m:mymath functions written.

Sharing rule (BIBLE §8, §24): every proof (∂) of the workbookIA chapter a math chapter prepares is a frontier
(tools/syllabus.py adds them); ``frontieres`` lists further workbookIA exercises not to solve nor paraphrase. A math
chapter teaches the tool in another setting and may state a result whose proof workbookIA asks. As in parts I and II,
MML blocks are read in the 📖 exercises (the reading time is in those exercises). The notes of each chapter list the
data of workbookIA to avoid; CP3 is also compared with the checkpoint III and the mini-project III of workbookIA.
"""

CHAPTERS = [
    {
        "id": "M12a", "dir": "m12a_espaces_vectoriels", "hours": 16.6, "generation_sessions": 2,
        "mml": ["§2.4", "§2.5", "§2.6", "§2.7", "§2.8"],
        "summary": "Les espaces vectoriels et les applications linéaires : sous-espaces, combinaisons linéaires et "
                   "familles génératrices, indépendance, base et dimension, coordonnées, rang, matrice d'une "
                   "application linéaire, noyau, image et théorème du rang, changement de base, applications et "
                   "espaces affines, transformation inverse.",
        "objectives": [
            "Reconnaître un sous-espace vectoriel et le décrire par une famille génératrice ou par des équations.",
            "Décider si une famille est libre, en extraire une base, et calculer des coordonnées dans une base.",
            "Calculer le rang d'une matrice et majorer celui d'un produit.",
            "Écrire la matrice d'une application linéaire, et composer des applications en multipliant leurs "
            "matrices.",
            "Calculer un noyau et une image, appliquer le théorème du rang, et décrire toutes les solutions de "
            "A x = b.",
            "Changer de base, et inverser une application affine.",
        ],
        "sections": [("§1", "Espaces vectoriels et sous-espaces"),
                     ("§2", "Combinaisons linéaires, familles génératrices et indépendance"),
                     ("§3", "Bases, dimension et coordonnées"),
                     ("§4", "Le rang, et le rang d'un produit"),
                     ("§5", "Applications linéaires et leur matrice"),
                     ("§6", "Noyau, image et théorème du rang"),
                     ("§7", "Changer de base"),
                     ("§8", "Applications affines et transformation inverse")],
        "teaches": ["espace vectoriel, sous-espace", "combinaison linéaire, famille génératrice",
                    "indépendance linéaire", "base et dimension", "coordonnées dans une base",
                    "rang, rang d'un produit", "application linéaire et sa matrice", "composition et produit",
                    "noyau et image", "théorème du rang", "changement de base", "applications et espaces affines",
                    "application réciproque, transformation inverse"],
        "requires": [("pivot de Gauss, forme échelonnée réduite, rang (premier contact), inverse", "M09a"),
                     ("vecteurs de ℝⁿ, combinaisons linéaires, produit scalaire", "M07"),
                     ("raisonnements, ensembles", "R4"), ("dérivée d'un polynôme", "R7"),
                     ("centrer et réduire", "M02c")],
        "frontieres": ["15.3"],
        "mymath": {"module": "linmaps.py",
                   "functions": ["is_independent", "column_space_basis", "null_space_basis", "coordinates",
                                 "change_of_basis"]},
        "reading_minutes": 210,
        "flashcards": 26,
        "notes": "Frontières : 15.3 (ramener une droite ajustée dans l'espace d'origine par la réciproque d'un "
                 "min-max), et les ∂ 12.6 (moyenne nulle et variance 1 des z-scores, invariance par x′ = ax + b) et "
                 "12.8 de workbookIA. M12a enseigne les applications affines et leur réciproque sur des "
                 "transformations du plan, sans min-max, z-score ni droite ajustée. Évités (règle de partage) : les "
                 "exemples et nombres de la fiche de workbookIA 12 (la météo en one-hot et `drop=\"first\"`, l'ordinal "
                 "faible, moyen, fort, la colonne 2, 4, 9, les températures et comptages de voitures de 12.4, les "
                 "étendues de 12.3, le tableau de 12.5, les îles et les sexes des manchots) ; la colinéarité d'un "
                 "one-hot avec la constante s'illustre ailleurs que sur ces catégories. M12a.6 montre que le rang d'un"
                 " tableau centré est au plus n − 1 (1ᵀX_c = 0), ce dont la fiche de workbookIA 12 se sert pour "
                 "compter les composantes d'une ACP. `linmaps` écrit les briques (indépendance, bases de l'espace des "
                 "colonnes et du noyau comme SymPy, coordonnées, S⁻¹AS) ; NumPy permis, pas `matrix_rank`, `svd`, "
                 "`qr`, `lstsq`, `pinv`, `inv` ni SymPy. La fiche énonce que la composée de deux applications affines "
                 "est affine (le ∂ 17.3.1 de workbookIA la démontre, avec sa matrice et son vecteur) : M12a.19 ne "
                 "démontre que l'inverse. Le Fermi M12a.24 évite les images 28 × 28 vers dix scores (7 850, réponse de"
                 " workbookIA 13.9). M12a.11 annonce les vecteurs propres de M12c sans les nommer. Parcours essentiel "
                 ": le théorème du rang et rang(AB) démontrés hors parcours. Deux sessions de génération : §1 à §4, "
                 "puis §5 à §8.",
        "exercises": [
            ("M12a.Q1", "🧠", 1, 4, "Sous-espace ou pas ?", "§1", "E"),
            ("M12a.Q2", "🧠", 1, 4, "Combinaison linéaire et famille génératrice", "§2", "E"),
            ("M12a.Q3", "🧠", 1, 4, "Libre ou liée ?", "§2", "E"),
            ("M12a.Q4", "🧠", 1, 4, "Base et dimension : vrai ou faux", "§3", "E"),
            ("M12a.Q5", "🧠", 1, 4, "Le rang d'une matrice, d'une transposée, d'un produit", "§4", "E"),
            ("M12a.Q6", "🧠", 1, 4, "Linéaire, affine, ou ni l'un ni l'autre ?", "§5 §8", "E"),
            ("M12a.Q7", "🧠", 1, 4, "Noyau et image : qui vit où ?", "§6", "E"),
            ("M12a.Q8", "🧠", 1, 4, "Changer de base : ce qui change et ce qui reste", "§7", ""),
            ("M12a.R1", "🔁", 1, 5, "Le pivot de Gauss et la forme échelonnée réduite (M09a)", "§2", "E"),
            ("M12a.R2", "🔁", 1, 5, "Produit matriciel et formes (M09a)", "§5", "E"),
            ("M12a.R3", "🔁", 1, 5, "Combinaisons linéaires et produit scalaire dans ℝⁿ (M07)", "§2", ""),
            ("M12a.1", "✏️", 1, 15, "Reconnaître des sous-espaces de ℝ³ et de l'espace des polynômes", "§1", "E"),
            ("M12a.2", "✏️", 1, 15, "Écrire un vecteur comme combinaison linéaire : un système à résoudre", "§2",
             "E"),
            ("M12a.3", "✏️", 1, 15, "L'indépendance de trois vecteurs de ℝ³ par le pivot de Gauss", "§2", "E"),
            ("M12a.4", "✏️", 2, 20, "Extraire une base d'une famille génératrice, compléter une famille libre", "§3",
             "E"),
            ("M12a.5", "✏️", 1, 15, "Les coordonnées d'un vecteur dans une base qui n'est pas la base canonique",
             "§3", "E"),
            ("M12a.6", "✏️", 2, 20, "Le rang par les colonnes et par les lignes, celui d'un produit, et celui d'un "
             "tableau centré", "§4", "E"),
            ("M12a.7", "✏️", 1, 15, "La matrice d'une application linéaire : les images des vecteurs de base", "§5",
             "E"),
            ("M12a.8", "✏️", 1, 15, "Composer deux applications du plan, c'est multiplier leurs matrices", "§5", ""),
            ("M12a.9", "✏️", 2, 25, "Noyau et image d'une matrice 3 × 4, et le théorème du rang", "§6", "E"),
            ("M12a.10", "✏️", 2, 20, "Toutes les solutions de A x = b : une solution particulière plus le noyau",
             "§6", "E"),
            ("M12a.11", "✏️", 2, 20, "Une base adaptée qui rend diagonale la matrice d'une application : "
             "S⁻¹AS", "§7", "E"),
            ("M12a.12", "✏️", 2, 20, "Une application affine du plan : partie linéaire, translation, inverse", "§8",
             "E"),
            ("M12a.13", "✏️", 2, 20, "La dérivation sur les polynômes de degré au plus 3 : matrice, noyau, image",
             "§3 §5 §6", ""),
            ("M12a.14", "∂", 1, 15, "L'intersection de deux sous-espaces en est un ; la réunion, presque jamais",
             "§1", "E"),
            ("M12a.15", "∂", 2, 20, "Les coordonnées dans une base sont uniques", "§3", ""),
            ("M12a.16", "∂", 2, 20, "Le noyau est un sous-espace, et une application linéaire est injective si et "
             "seulement si son noyau est {0}", "§6", "E"),
            ("M12a.17", "∂", 3, 25, "Le théorème du rang : dim ker + rang = nombre de colonnes", "§6", ""),
            ("M12a.18", "∂", 2, 20, "rang(AB) ≤ min(rang A, rang B)", "§4", ""),
            ("M12a.19", "∂", 2, 20, "L'inverse d'une application affine bijective est affine", "§8", ""),
            ("M12a.20", "🔗", 1, 15, "Pont : une feature somme de deux autres rend XᵀX singulière, et le noyau dit "
             "laquelle", "§4 §6", "E"),
            ("M12a.21", "🔗", 2, 15, "Pont : projeter sur un plan puis revenir, ce que la transformation inverse ne "
             "peut pas rendre", "§6 §8", ""),
            ("M12a.22", "📖", 2, 30, "MML §2.4 et §2.5 : espaces vectoriels, sous-espaces et indépendance, en anglais",
             "§1 §2", ""),
            ("M12a.23", "📖", 2, 45, "MML §2.6 à §2.8 : base, rang, applications linéaires, changement de base, "
             "espaces affines", "§3 §4 §5 §6 §7 §8", ""),
            ("M12a.24", "🧮", 1, 10, "Fermi : les paramètres d'une application linéaire, puis affine, d'images 32 × 32 "
             "en couleurs vers 100 classes", "§5 §8", ""),
            ("M12a.25", "🗣️", 1, 10, "Expliquer la dimension et le rang sans une seule formule", "§3 §4", "E"),
            ("M12a.E1", "💼", 1, 10, "« Que veut dire qu'une matrice est de rang plein, et pourquoi s'en soucier ? »",
             "§4 §6", ""),
            ("M12a.E2", "💼", 1, 10, "« Qu'est-ce que le noyau d'une matrice, et où le croise-t-on en ML ? »", "§6",
             ""),
            ("M12a.26", "🔨", 2, 20, "Tester l'indépendance et extraire une base de l'espace des "
             "colonnes", "§2 §3 §4", "E m:is_independent,column_space_basis"),
            ("M12a.27", "🔨", 2, 25, "Une base du noyau, colonne libre par colonne libre", "§6",
             "E m:null_space_basis p:M12a.26"),
            ("M12a.28", "🔨", 1, 20, "Coordonnées dans une base et changement de base", "§3 §7",
             "m:coordinates,change_of_basis p:M12a.26"),
            ("M12a.29", "📦", 1, 15, "`sympy.Matrix.nullspace`, `columnspace` et `rank` contre tes fonctions", "§4 §6",
             "E"),
            ("M12a.30", "🔮", 1, 10, "Prédire le rang : matrices aléatoires, produits, colonnes répétées", "§4", "E"),
            ("M12a.31", "🔬", 2, 20, "Le rang numérique : une colonne presque redondante et le choix de la tolérance",
             "§4", ""),
            ("M12a.32", "🎨", 1, 20, "Une application linéaire du plan : l'image du carré unité, et ce qu'elle écrase "
             "quand son noyau n'est pas nul", "§5 §6", "E"),
            ("M12a.33", "🐛", 1, 15, "Chasse à l'erreur : une « base » liée, un noyau faux, S⁻¹AS écrit à l'envers",
             "§2 §6 §7", ""),
            ("M12a.34", "🛠️", 1, 15, "Un test de propriété : A fois une base du noyau donne 0, et le théorème du rang "
             "sur des matrices aléatoires", "§6", ""),
            ("M12a.35", "🏆", 3, 30, "Défi : retrouver les relations linéaires exactes cachées entre les colonnes "
             "d'un tableau, sans en inventer", "§6", ""),
        ],
    },
    {
        "id": "M12b", "dir": "m12b_orthogonalite", "hours": 15.2, "generation_sessions": 1,
        "mml": ["§3.2.2", "§3.2.3", "§3.5", "§3.6", "§3.7", "§3.8", "§9.4"],
        "summary": "Les produits scalaires généraux, l'orthogonalité, les bases orthonormées et les matrices "
                   "orthogonales, le procédé de Gram-Schmidt, le complément orthogonal, la projection orthogonale sur "
                   "un sous-espace, les moindres carrés revus comme une projection, la décomposition QR, et le "
                   "produit scalaire de fonctions.",
        "objectives": [
            "Reconnaître un produit scalaire défini par une matrice symétrique, et calculer normes et angles avec.",
            "Calculer dans une base orthonormée, et reconnaître une matrice orthogonale.",
            "Orthonormaliser une famille par Gram-Schmidt.",
            "Calculer un complément orthogonal et une projection orthogonale, et démontrer que le projeté est le "
            "point le plus proche.",
            "Résoudre des moindres carrés par une projection, puis par la décomposition QR.",
            "Calculer un produit scalaire de fonctions et orthogonaliser des polynômes.",
        ],
        "sections": [("§1", "Produits scalaires généraux"),
                     ("§2", "Orthogonalité, bases orthonormées et matrices orthogonales"),
                     ("§3", "Le procédé de Gram-Schmidt"),
                     ("§4", "Le complément orthogonal"),
                     ("§5", "La projection orthogonale sur un sous-espace"),
                     ("§6", "Les moindres carrés vus comme une projection"),
                     ("§7", "La décomposition QR"),
                     ("§8", "Le produit scalaire de fonctions")],
        "teaches": ["produits scalaires généraux, matrices symétriques définies positives (en dimension 2)",
                    "bases orthonormées", "matrices orthogonales", "procédé de Gram-Schmidt", "complément orthogonal",
                    "projection orthogonale", "moindres carrés comme projection", "décomposition QR",
                    "produit scalaire de fonctions"],
        "requires": [("base, dimension, rang, noyau et image", "M12a"),
                     ("équations normales, matrice chapeau", "M09b"),
                     ("produit scalaire, normes, projection sur une droite, Cauchy-Schwarz", "M07"),
                     ("intégrales", "M02a")],
        "frontieres": ["12.7"],
        "mymath": {"module": "orthogonal.py",
                   "functions": ["gram_schmidt", "project", "qr", "least_squares_qr"]},
        "reading_minutes": 180,
        "flashcards": 24,
        "notes": "Frontières : 12.7 (l'erreur de reconstruction d'une ACP 2D, égale à la coordonnée orthogonale), et "
                 "les ∂ 12.6 et 12.8 de workbookIA. Évités : la projection de la fiche de workbookIA 12 (u = (0,6 ; "
                 "0,8), x = (2, 3), t = 3,6, distance 0,2, variance 10,72 = uᵀΣu) et ses coordonnées projetées ; la "
                 "propriété « l'erreur de reconstruction est la coordonnée orthogonale » de 12.7 n'est pas posée sur "
                 "un nuage 2D : M12b.19 la démontre pour k directions orthonormées quelconques, par Pythagore. Les "
                 "moindres carrés vus comme une projection (MML §9.4) reprennent M09b en dimension p, sans ses "
                 "exemples ni ceux de workbookIA 9. Parcours essentiel : QR et le produit scalaire de fonctions hors "
                 "parcours (workbookIA 12 n'en a pas besoin). `orthogonal` écrit Gram-Schmidt (classique et modifié), "
                 "la projection (par une base orthonormée, QQᵀv, pas par les équations normales de M09b), QR et les "
                 "moindres carrés par QR ; NumPy permis, pas `np.linalg.qr`, `lstsq`, `pinv` ni `inv`. Le "
                 "conditionnement n'est défini qu'en M12d : M12b parle de colonnes presque dépendantes, et la réponse "
                 "modèle de M12b.E1 cite Householder (LAPACK) et les arrondis que XᵀX amplifie (M09b.32), sans κ. Le 🏆"
                 " M12b.33 attend l'orthogonalisation de la matrice augmentée [X | y] (Björck), sur des données "
                 "bruitées et des colonnes presque dépendantes (à calibrer à la génération, entre les seuils où les "
                 "équations normales échouent et où `gram_schmidt` refuse) : `least_squares_qr` (Gram-Schmidt modifié "
                 "puis Qᵀy) n'y suffit pas.",
        "exercises": [
            ("M12b.Q1", "🧠", 1, 4, "Produit scalaire ou pas ? Symétrie et positivité", "§1", "E"),
            ("M12b.Q2", "🧠", 1, 4, "Orthogonale, orthonormée, matrice orthogonale", "§2", "E"),
            ("M12b.Q3", "🧠", 1, 4, "Gram-Schmidt : ce que chaque étape retire", "§3", "E"),
            ("M12b.Q4", "🧠", 1, 4, "Le complément orthogonal : vrai ou faux", "§4", "E"),
            ("M12b.Q5", "🧠", 1, 4, "Une matrice de projection : sur quoi, et quelles propriétés ?", "§5", "E"),
            ("M12b.Q6", "🧠", 1, 4, "Moindres carrés et projection", "§6", "E"),
            ("M12b.Q7", "🧠", 1, 4, "QR : formes et propriétés", "§7", ""),
            ("M12b.Q8", "🧠", 1, 4, "Des fonctions orthogonales", "§8", ""),
            ("M12b.R1", "🔁", 1, 5, "La projection sur une droite (M07)", "§5", "E"),
            ("M12b.R2", "🔁", 1, 5, "Les équations normales et la matrice chapeau (M09b)", "§6", "E"),
            ("M12b.R3", "🔁", 1, 5, "Base, rang et noyau (M12a)", "§4", "E"),
            ("M12b.1", "✏️", 1, 15, "Un produit scalaire défini par une matrice 2 × 2 : normes, angles, orthogonalité",
             "§1", "E"),
            ("M12b.2", "✏️", 1, 15, "Les coordonnées dans une base orthonormée : des produits scalaires au lieu "
             "d'un système", "§2", "E"),
            ("M12b.3", "✏️", 1, 15, "Une matrice orthogonale 3 × 3 conserve normes et angles", "§2", "E"),
            ("M12b.4", "✏️", 2, 20, "Gram-Schmidt sur trois vecteurs de ℝ³", "§3", "E"),
            ("M12b.5", "✏️", 2, 20, "Gram-Schmidt pour un produit scalaire qui n'est pas l'usuel", "§1 §3", ""),
            ("M12b.6", "✏️", 2, 20, "Une base du complément orthogonal d'un plan de ℝ⁴", "§4", "E"),
            ("M12b.7", "✏️", 2, 20, "Projeter sur un plan de ℝ³ : avec une base quelconque, puis orthonormée", "§5",
             "E"),
            ("M12b.8", "✏️", 2, 15, "La matrice de projection : P² = P, Pᵀ = P, trace et rang", "§5", ""),
            ("M12b.9", "✏️", 1, 15, "La distance d'un point à un sous-espace, et le résidu orthogonal", "§5 §6", "E"),
            ("M12b.10", "✏️", 2, 20, "Des moindres carrés comme une projection : y, son projeté et le résidu", "§6",
             "E"),
            ("M12b.11", "✏️", 2, 25, "La décomposition QR d'une matrice 3 × 2, puis les moindres carrés par R w = "
             "Qᵀy", "§7", ""),
            ("M12b.12", "✏️", 2, 25, "Le produit scalaire de fonctions sur [−1 ; 1] : orthogonaliser 1, x et x²",
             "§8", ""),
            ("M12b.13", "∂", 2, 20, "L'inégalité de Cauchy-Schwarz pour tout produit scalaire", "§1", ""),
            ("M12b.14", "∂", 1, 15, "Une famille orthogonale de vecteurs non nuls est libre", "§2", "E"),
            ("M12b.15", "∂", 2, 20, "Gram-Schmidt donne une base orthonormée du même sous-espace", "§3", ""),
            ("M12b.16", "∂", 2, 20, "L'orthogonal de l'image de A est le noyau de Aᵀ", "§4", "E"),
            ("M12b.17", "∂", 2, 20, "Le projeté orthogonal est le point le plus proche (Pythagore)", "§5 §6", "E"),
            ("M12b.18", "🔗", 1, 15, "Pont : retirer d'une feature ce qu'explique une autre, une projection puis un "
             "résidu", "§3 §5", "E"),
            ("M12b.19", "🔗", 2, 15, "Pont : projeter sur k directions orthonormées, reconstruire, et l'erreur par "
             "Pythagore", "§5", "E"),
            ("M12b.20", "📖", 2, 30, "MML §3.2, §3.5 à §3.7 : produits scalaires, orthogonalité, fonctions, en "
             "anglais", "§1 §2 §4 §8", ""),
            ("M12b.21", "📖", 2, 30, "MML §3.8 et §9.4 : projections, Gram-Schmidt et moindres carrés", "§3 §5 §6", ""),
            ("M12b.22", "🧮", 1, 10, "Fermi : le coût de Gram-Schmidt sur une matrice 100 000 × 50", "§3 §7", ""),
            ("M12b.23", "🗣️", 1, 10, "Expliquer pourquoi le projeté est le point le plus proche", "§5", "E"),
            ("M12b.E1", "💼", 1, 10, "« Pourquoi résoudre des moindres carrés par QR plutôt que par les équations "
             "normales ? »", "§6 §7", ""),
            ("M12b.E2", "💼", 1, 10, "« Qu'est-ce qu'une matrice orthogonale, et pourquoi est-elle agréable en calcul "
             "numérique ? »", "§2", ""),
            ("M12b.24", "🔨", 2, 25, "Gram-Schmidt, classique et modifié", "§3", "E m:gram_schmidt"),
            ("M12b.25", "🔨", 1, 15, "La projection orthogonale sur un sous-espace", "§5", "E m:project"),
            ("M12b.26", "🔨", 2, 25, "La décomposition QR et les moindres carrés par QR", "§7",
             "m:qr,least_squares_qr p:M12b.24"),
            ("M12b.27", "📦", 1, 15, "`np.linalg.qr` et `lstsq` contre ta projection et ta QR : les signes de Q et de "
             "R", "§7", ""),
            ("M12b.28", "🔮", 1, 10, "Prédire : Gram-Schmidt classique sur des vecteurs presque colinéaires, QᵀQ "
             "vaut-il encore I ?", "§3", "E"),
            ("M12b.29", "🔬", 2, 20, "Gram-Schmidt classique contre modifié : l'orthogonalité perdue quand les "
             "colonnes sont presque dépendantes", "§3 §7", ""),
            ("M12b.30", "🎨", 1, 20, "Projeter un nuage de ℝ³ sur un plan : les résidus orthogonaux en image", "§5",
             "E"),
            ("M12b.31", "🐛", 1, 15, "Chasse à l'erreur : une normalisation oubliée, QQᵀ sur une base non "
             "orthonormée, R w = Qᵀy résolu dans le mauvais sens", "§3 §5 §7", ""),
            ("M12b.32", "🛠️", 1, 15, "Un test de propriétés pour la projection : idempotente, symétrique, résidu "
             "orthogonal", "§5", ""),
            ("M12b.33", "🏆", 3, 30, "Défi : des colonnes presque dépendantes, des moindres carrés à 1e−8 près de "
             "`lstsq` par l'orthogonalisation de [X | y]", "§6 §7", ""),
        ],
    },
    {
        "id": "M12c", "dir": "m12c_valeurs_propres", "hours": 16.8, "generation_sessions": 2,
        "mml": ["§4.1", "§4.2", "§4.3", "§4.4"],
        "summary": "Le déterminant et la trace, les valeurs et vecteurs propres, la méthode de la puissance, la "
                   "diagonalisation et le théorème spectral, le quotient de Rayleigh, les matrices définies positives, "
                   "les formes quadratiques et la décomposition de Cholesky ; la matrice de covariance vue comme une "
                   "matrice symétrique positive, le blanchiment et la racine carrée d'une matrice.",
        "objectives": [
            "Calculer un déterminant, l'interpréter comme un volume orienté, et l'utiliser pour l'inversibilité.",
            "Calculer les valeurs et vecteurs propres d'une petite matrice, et diagonaliser.",
            "Appliquer le théorème spectral et le quotient de Rayleigh à une matrice symétrique.",
            "Approcher la plus grande valeur propre par la méthode de la puissance.",
            "Reconnaître une matrice définie positive et calculer sa décomposition de Cholesky.",
            "Transformer une matrice de covariance, et blanchir des données.",
        ],
        "sections": [("§1", "Le déterminant : volume orienté et inversibilité"),
                     ("§2", "La trace"),
                     ("§3", "Valeurs propres et vecteurs propres"),
                     ("§4", "La diagonalisation"),
                     ("§5", "La méthode de la puissance"),
                     ("§6", "Matrices symétriques : le théorème spectral et le quotient de Rayleigh"),
                     ("§7", "Matrices définies positives, formes quadratiques et Cholesky"),
                     ("§8", "La matrice de covariance, le blanchiment et la racine carrée d'une matrice")],
        "teaches": ["déterminant", "trace", "polynôme caractéristique", "valeurs et vecteurs propres",
                    "méthode de la puissance", "diagonalisation", "théorème spectral", "quotient de Rayleigh",
                    "matrices définies positives", "décomposition de Cholesky", "formes quadratiques",
                    "convexité à plusieurs variables par la hessienne semi-définie positive (la définition par les "
                    "cordes : M10)", "matrice de Gram XᵀX (semi-définie positive)",
                    "matrice de covariance symétrique positive", "covariance d'une transformation affine",
                    "blanchiment (whitening)", "racine carrée d'une matrice symétrique positive"],
        "requires": [("base, rang, noyau, changement de base", "M12a"),
                     ("bases orthonormées, matrices orthogonales", "M12b"),
                     ("matrice de covariance empirique", "M02c"), ("fonctions convexes de plusieurs variables", "M10"),
                     ("hessienne d'une fonction de deux variables", "M05b"), ("racines d'un polynôme", "R3")],
        "frontieres": ["12.7", "12.22", "12.29", "12.R3"],
        "mymath": {"module": "eigen.py",
                   "functions": ["det", "power_iteration", "rayleigh_quotient", "cholesky", "is_positive_definite",
                                 "sqrtm_psd", "whitening_matrix"]},
        "reading_minutes": 210,
        "flashcards": 26,
        "notes": "Frontières : 12.7 (ACP 2D à la main), 12.22 (« l'axe principal d'un nuage standardisé en 2D est à "
                 "45° et garde (1 + r)/2 »), 12.29 et 12.R3 (courbures de la MSE, pas critique 2/λ_max de la descente "
                 "de gradient), et les ∂ 12.6 et 12.8. M12c énonce le théorème spectral en dimension n (démontré quand"
                 " les valeurs propres sont distinctes), démontre le quotient de Rayleigh par QΛQᵀ (M12c.8 et M12c.18,"
                 " sans u = (cos t, sin t) ni l'enchaînement diagonale 2D, 3D puis rotation de 12.8), V(aᵀX) = aᵀΣa "
                 "pour un vecteur aléatoire et la positivité d'une matrice de Gram (M12c.17), et la trace par tr(QᵀAQ)"
                 " = tr(A). La diagonalisation (§4) vient avant la méthode de la puissance (§5), dont l'analyse "
                 "suppose une base de vecteurs propres. Évités : les matrices [[1, r], [r, 1]] et [[a, b], [b, a]] "
                 "(12.22), [[3, 1], [1, 3]] et le blanchiment « 3 devient 1,5 et 2,12 » (fiche de workbookIA 12), la "
                 "covariance [[4, 5], [5, 7]] des points (0, 1), (2, 2), (4, 6), la quadratique x² + 100y² (12.R3). "
                 "Conventions : la fiche montre les deux normalisations de Σ (1/n pour le `StandardScaler` et le "
                 "`covariance_matrix` de `mylearn`, 1/(n − 1) pour l'ACP de workbookIA 12) et le facteur (n − 1)/n ; "
                 "elle décrit le blanchiment de l'ACP (Λ^(−1/2)Qᵀ, celui de scikit-learn et de la PCA de `mylearn` en "
                 "12.27) et le blanchiment ZCA (Σ^(−1/2)), et M12c.13 calcule les deux en disant la convention ; "
                 "`whitening_matrix` n'écrit que ZCA et Cholesky. `eigen` : NumPy permis, `np.linalg.eigh` seulement "
                 "dans `sqrtm_psd` et `whitening_matrix`. Deux sessions de génération : §1 à §5, puis §6 à §8.",
        "exercises": [
            ("M12c.Q1", "🧠", 1, 4, "Ce que mesure un déterminant", "§1", "E"),
            ("M12c.Q2", "🧠", 1, 4, "Les propriétés du déterminant et de la trace : vrai ou faux", "§1 §2", "E"),
            ("M12c.Q3", "🧠", 1, 4, "Reconnaître un vecteur propre", "§3", "E"),
            ("M12c.Q4", "🧠", 1, 4, "Diagonalisable ou pas ?", "§4", "E"),
            ("M12c.Q5", "🧠", 1, 4, "Ce que garantit le théorème spectral", "§6", "E"),
            ("M12c.Q6", "🧠", 1, 4, "Définie positive, semi-définie positive ou indéfinie ?", "§7", "E"),
            ("M12c.Q7", "🧠", 1, 4, "Cholesky, racine carrée, blanchiment : qui est quoi ?", "§7 §8", ""),
            ("M12c.Q8", "🧠", 1, 4, "Trace, déterminant et valeurs propres", "§2 §3", "E"),
            ("M12c.R1", "🔁", 1, 5, "Le rang et le noyau (M12a)", "§3", "E"),
            ("M12c.R2", "🔁", 1, 5, "Bases orthonormées et matrices orthogonales (M12b)", "§6", "E"),
            ("M12c.R3", "🔁", 1, 5, "La matrice de covariance empirique (M02c)", "§8", "E"),
            ("M12c.1", "✏️", 1, 15, "Déterminants 2 × 2 et 3 × 3 : aire, volume et signe", "§1", "E"),
            ("M12c.2", "✏️", 2, 20, "Le déterminant d'une matrice 4 × 4 par élimination", "§1", ""),
            ("M12c.3", "✏️", 1, 15, "Les valeurs et vecteurs propres d'une matrice 2 × 2", "§3", "E"),
            ("M12c.4", "✏️", 2, 20, "Une matrice 3 × 3 triangulaire, puis une avec une valeur propre "
             "double", "§3 §4", "E"),
            ("M12c.5", "✏️", 2, 20, "Diagonaliser, puis calculer une puissance dixième", "§4", "E"),
            ("M12c.6", "✏️", 2, 15, "Une matrice non diagonalisable, et une rotation sans valeur propre "
             "réelle", "§3 §4", ""),
            ("M12c.7", "✏️", 1, 15, "Le théorème spectral sur une matrice symétrique 2 × 2 : Q, Λ et QΛQᵀ", "§6", "E"),
            ("M12c.8", "✏️", 2, 20, "Le quotient de Rayleigh : le maximum et le minimum de xᵀAx sur le cercle unité",
             "§6", "E"),
            ("M12c.9", "✏️", 1, 15, "Trois itérations de la méthode de la puissance à la main", "§5", ""),
            ("M12c.10", "✏️", 2, 20, "Définie positive ? Par les valeurs propres, les mineurs et la forme quadratique "
             "; une hessienne qui prouve la convexité", "§7", "E"),
            ("M12c.11", "✏️", 2, 20, "La décomposition de Cholesky d'une matrice 3 × 3", "§7", "E"),
            ("M12c.12", "✏️", 2, 20, "Une forme quadratique réduite à une somme de carrés, et ses lignes de niveau",
             "§6 §7", ""),
            ("M12c.13", "✏️", 2, 20, "La covariance d'un vecteur transformé, AΣAᵀ, et le blanchiment d'une "
             "covariance 2 × 2", "§8", "E"),
            ("M12c.14", "∂", 2, 20, "det A ≠ 0 si et seulement si A est inversible (det AB = det A det B admis)", "§1",
             ""),
            ("M12c.15", "∂", 2, 20, "Une matrice symétrique réelle : valeurs propres réelles, vecteurs propres de "
             "valeurs distinctes orthogonaux", "§6", "E"),
            ("M12c.16", "∂", 2, 20, "La somme des valeurs propres est la trace, leur produit le déterminant", "§2 §3",
             ""),
            ("M12c.17", "∂", 1, 15, "Une matrice de covariance, et toute matrice de Gram XᵀX, est symétrique "
             "semi-définie positive", "§8", "E"),
            ("M12c.18", "∂", 2, 20, "Le quotient de Rayleigh d'une matrice symétrique est entre λ_min et λ_max", "§6",
             ""),
            ("M12c.19", "∂", 2, 20, "½ xᵀAx − bᵀx, avec A définie positive, a un unique minimum, en A⁻¹b", "§7", "E"),
            ("M12c.20", "🔗", 1, 15, "Pont : la variance d'une somme pondérée de trois features, wᵀΣw, et pourquoi Σ "
             "doit être semi-définie positive", "§8", "E"),
            ("M12c.21", "🔗", 2, 15, "Pont : après un blanchiment, la covariance est l'identité", "§8", ""),
            ("M12c.22", "📖", 2, 30, "MML §4.1 et §4.2 : déterminant, trace, valeurs propres, en anglais", "§1 §2 §3",
             ""),
            ("M12c.23", "📖", 2, 30, "MML §4.3 et §4.4 : Cholesky, diagonalisation et décomposition "
             "spectrale", "§4 §6 §7", ""),
            ("M12c.24", "🧮", 1, 10, "Fermi : un déterminant 20 × 20 par cofacteurs ou par élimination, combien "
             "d'opérations ?", "§1", ""),
            ("M12c.25", "🗣️", 1, 10, "Expliquer un vecteur propre avec une image", "§3", "E"),
            ("M12c.E1", "💼", 1, 10, "« Que représentent les valeurs propres d'une matrice de covariance ? »", "§6 §8",
             ""),
            ("M12c.E2", "💼", 1, 10, "« Comment savoir qu'une matrice est définie positive, et pourquoi est-ce "
             "important en optimisation ? »", "§7", ""),
            ("M12c.26", "🔨", 1, 20, "Le déterminant par élimination", "§1", "E m:det"),
            ("M12c.27", "🔨", 2, 25, "La méthode de la puissance et le quotient de "
             "Rayleigh", "§5 §6", "E m:power_iteration,rayleigh_quotient"),
            ("M12c.28", "🔨", 2, 25, "La décomposition de Cholesky et le test « définie positive "
             "»", "§7", "E m:cholesky,is_positive_definite"),
            ("M12c.29", "🔨", 2, 25, "La racine carrée d'une matrice symétrique positive et la matrice de "
             "blanchiment", "§6 §8", "E m:sqrtm_psd,whitening_matrix p:M12c.28"),
            ("M12c.30", "📦", 1, 15, "`np.linalg.eigh`, `det`, `cholesky` et `scipy.linalg.sqrtm` contre tes "
             "fonctions", "§1 §6 §7", "E"),
            ("M12c.31", "🔮", 1, 10, "Prédire : la méthode de la puissance quand les deux plus grandes valeurs propres "
             "sont proches", "§5", "E"),
            ("M12c.32", "🔬", 2, 20, "La vitesse de la méthode de la puissance et le rapport |λ₂ / λ₁|", "§5", ""),
            ("M12c.33", "🎨", 1, 20, "Les lignes de niveau de xᵀAx : définie positive, semi-définie positive, "
             "indéfinie", "§6 §7", "E"),
            ("M12c.34", "🐛", 1, 15, "Chasse à l'erreur : det(A + B) = det A + det B, un vecteur propre nul, Cholesky "
             "d'une matrice non symétrique", "§1 §3 §7", ""),
            ("M12c.35", "🛠️", 1, 15, "Vérifier avec SymPy : polynôme caractéristique, valeurs propres exactes, "
             "diagonalisation", "§3 §4", ""),
            ("M12c.36", "🏆", 3, 30, "Défi : les trois plus grandes valeurs propres d'une matrice symétrique "
             "semi-définie positive 300 × 300, par la puissance avec déflation, à 1e−6 près", "§5 §6", ""),
        ],
    },
    {
        "id": "M12d", "dir": "m12d_svd_acp", "hours": 17.7, "generation_sessions": 2,
        "mml": ["§4.5", "§4.6", "§4.7", "§10.1", "§10.2", "§10.3", "§10.4", "§10.5", "§10.6"],
        "summary": "La décomposition en valeurs singulières et son interprétation géométrique, l'approximation de rang "
                   "faible, la pseudo-inverse et le conditionnement ; puis les axes principaux par le quotient de "
                   "Rayleigh, l'ACP (centrer, projeter, reconstruire), la variance expliquée, l'erreur de "
                   "reconstruction, l'ACP en grande dimension, et la place de t-SNE et d'UMAP.",
        "objectives": [
            "Calculer la SVD d'une petite matrice et l'interpréter comme rotation, étirement, rotation.",
            "Calculer une approximation de rang faible et son erreur (Eckart-Young).",
            "Calculer une pseudo-inverse et un conditionnement, et dire ce qu'ils signifient.",
            "Calculer les axes principaux d'un nuage, les scores, une reconstruction et la variance expliquée.",
            "Relier l'erreur de reconstruction aux valeurs propres oubliées.",
            "Situer l'ACP par rapport à t-SNE et UMAP.",
        ],
        "sections": [("§1", "La décomposition en valeurs singulières"),
                     ("§2", "Rotation, étirement, rotation : la géométrie de la SVD"),
                     ("§3", "L'approximation de rang faible"),
                     ("§4", "La pseudo-inverse et le conditionnement"),
                     ("§5", "Les axes principaux : maximiser la variance sur la sphère"),
                     ("§6", "L'ACP : centrer, projeter, reconstruire"),
                     ("§7", "Variance expliquée, erreur de reconstruction, grande dimension"),
                     ("§8", "Au-delà du linéaire : t-SNE et UMAP (aperçu)")],
        "teaches": ["décomposition en valeurs singulières", "interprétation géométrique",
                    "approximation de rang faible (Eckart-Young)", "pseudo-inverse", "conditionnement",
                    "axes principaux : maximiser uᵀCu sur la sphère (quotient de Rayleigh)", "ACP : projection",
                    "variance expliquée", "ACP en grande dimension", "erreur de reconstruction d'une projection",
                    "t-SNE et UMAP : préserver des voisinages (aperçu)",
                    "erreur de reconstruction et détection d'anomalies"],
        "requires": [("valeurs propres, théorème spectral, quotient de Rayleigh", "M12c"),
                     ("projection orthogonale, bases orthonormées", "M12b"), ("rang, noyau, image", "M12a"),
                     ("moyenne, matrice de covariance, standardisation", "M02c"),
                     ("moindres carrés", "M09b"), ("entropie, divergence KL", "M06")],
        "frontieres": ["12.7", "12.22", "12.27", "12.29", "25.8"],
        "mymath": {"module": "svd_pca.py",
                   "functions": ["svd", "low_rank_approximation", "pinv", "condition_number", "principal_axes",
                                 "explained_variance_ratio"]},
        "reading_minutes": 210,
        "flashcards": 26,
        "notes": "Frontières : 12.7 et 12.22 (ACP 2D à la main, axe à 45° d'un nuage standardisé), 12.27 (la PCA de "
                 "`mylearn` par SVD : centrage, signe, choix de k par un seuil, whitening, `inverse_transform`), 12.29"
                 " (conditionnement et pas de la descente de gradient), 25.8 (autoencodeur linéaire et ACP), et les ∂ "
                 "12.6 et 12.8 (variance d'une projection et axe de variance maximale). M12d passe par le quotient de "
                 "Rayleigh de M12c en dimension n, et fait ses ACP à la main en dimension 3, par le polynôme "
                 "caractéristique d'une covariance à structure par blocs (une valeur propre évidente), sans reprendre "
                 "la suite de 12.7 : M12d.9 demande l'erreur de reconstruction moyenne (la somme des variances "
                 "oubliées), pas la distance d'un point à sa reconstruction, et aucun blanchiment ; M12d.21 pose DΣD "
                 "en général. `principal_axes` prend une matrice de covariance (pas les données) et "
                 "`explained_variance_ratio` des valeurs propres, pour ne pas écrire la PCA de `mylearn` (ce sont des "
                 "briques, avec la même convention de signe). M12d.13 calcule les probabilités de voisinage de t-SNE "
                 "et leur perplexité 2^H (M06), sans MNIST ni perplexité 30. La SVD par AᵀA ne voit pas les valeurs "
                 "singulières sous 1e−6 · s_max : les comparaisons à `np.linalg.cond` se font pour κ < 1e6. MML §10.2 "
                 "dérive l'axe de variance maximale par Lagrange : cette dérivation se relit en M13b ; §10.7 (point de"
                 " vue latent) se lit en M25b. Évités : les nombres MNIST de workbookIA 12 (86, 321, 35, 78, 59 "
                 "composantes, 0,572, 0,911…), `load_digits`, les « 10 features, 3 directions et du bruit » de sa "
                 "fiche, le passage des kilogrammes aux grammes, les points A(1, 1) à E(7, 3) de 12.7, et pour "
                 "l'anomalie MNIST contre Fashion-MNIST, le seuil au 99ᵉ centile et la ROC-AUC (workbookIA 25). Le 🏆 "
                 "M12d.37 est calibré (session 41) sur la photo CC0 de la tasse de café (`data/cards/tasse_cafe.md`), "
                 "centrée : avec 5 % des nombres, la SVD globale garde 88,8 % de l'énergie, des tuiles de rang adapté "
                 "89,5 à 91,6 %, la seule moyenne de chaque rectangle de 4 × 5 pixels 93,3 %, l'ACP de ses carrés de 8 × 8 "
                 "pixels 94,1 % : l'objectif est donc 93,5 % (97 % demandait 14 à 26 % des nombres). Convention de "
                 "signe des axes comme scikit-learn et la PCA de "
                 "`mylearn` (la coordonnée de plus grande valeur absolue est positive). `svd_pca` : NumPy et "
                 "`np.linalg.eigh` permis, pas `np.linalg.svd`, `pinv`, `cond`, `lstsq` ni scikit-learn. Deux sessions"
                 " de génération : §1 à §4 (SVD), puis §5 à §8 (ACP).",
        "exercises": [
            ("M12d.Q1", "🧠", 1, 4, "La SVD : formes et propriétés", "§1", "E"),
            ("M12d.Q2", "🧠", 1, 4, "Valeurs singulières et valeurs propres", "§1 §2", "E"),
            ("M12d.Q3", "🧠", 1, 4, "Rang faible : ce qu'on garde, ce qu'on perd", "§3", "E"),
            ("M12d.Q4", "🧠", 1, 4, "Pseudo-inverse et conditionnement", "§4", "E"),
            ("M12d.Q5", "🧠", 1, 4, "Ce que maximise un axe principal", "§5", "E"),
            ("M12d.Q6", "🧠", 1, 4, "Centrer et standardiser avant une ACP ?", "§6", "E"),
            ("M12d.Q7", "🧠", 1, 4, "Variance expliquée et nombre de composantes", "§7", "E"),
            ("M12d.Q8", "🧠", 1, 4, "ACP, t-SNE ou UMAP : qui garde quoi ?", "§8", "E"),
            ("M12d.R1", "🔁", 1, 5, "Valeurs propres et théorème spectral (M12c)", "§1", "E"),
            ("M12d.R2", "🔁", 1, 5, "La projection orthogonale (M12b)", "§5", "E"),
            ("M12d.R3", "🔁", 1, 5, "Moyenne, covariance et standardisation (M02c)", "§6", "E"),
            ("M12d.1", "✏️", 2, 20, "La SVD d'une matrice 2 × 2 à la main, par AᵀA", "§1", "E"),
            ("M12d.2", "✏️", 2, 15, "La SVD compacte d'une matrice 3 × 2 de rang 1", "§1", ""),
            ("M12d.3", "✏️", 1, 15, "Le cercle unité devient une ellipse : axes et demi-axes", "§2", "E"),
            ("M12d.4", "✏️", 2, 20, "L'approximation de rang 1 d'une matrice 3 × 3 et son erreur", "§3", "E"),
            ("M12d.5", "✏️", 1, 10, "Compter les nombres stockés : une image en rang k", "§3", ""),
            ("M12d.6", "✏️", 2, 20, "La pseudo-inverse d'une matrice non inversible et la solution de norme "
             "minimale", "§4", "E"),
            ("M12d.7", "✏️", 2, 15, "Le conditionnement de trois matrices, et l'erreur relative sur une solution",
             "§4", "E"),
            ("M12d.8", "✏️", 2, 35, "Les axes principaux d'un nuage de ℝ³ : covariance, polynôme caractéristique, "
             "variances et axes", "§5 §6", "E"),
            ("M12d.9", "✏️", 2, 20, "Scores, reconstruction et erreur de reconstruction moyenne avec deux composantes "
             "sur trois", "§6 §7", "E"),
            ("M12d.10", "✏️", 1, 15, "La variance expliquée cumulée : combien de composantes pour 95 % ?", "§7", "E"),
            ("M12d.11", "✏️", 2, 20, "L'ACP par la SVD de la matrice centrée : s² / (n − 1) donne les variances",
             "§1 §6", ""),
            ("M12d.12", "✏️", 2, 20, "L'ACP quand n < p : passer par la petite matrice XXᵀ", "§7", ""),
            ("M12d.13", "✏️", 1, 15, "Les probabilités de voisinage de t-SNE sur quatre points, et leur perplexité "
             "2^H", "§8", "E"),
            ("M12d.14", "∂", 2, 20, "Les valeurs singulières sont les racines des valeurs propres de AᵀA", "§1", "E"),
            ("M12d.15", "∂", 2, 20, "La plus grande valeur singulière est le plus grand étirement : ‖A x‖ ≤ s₁ ‖x‖",
             "§2", ""),
            ("M12d.16", "∂", 3, 25, "L'erreur de l'approximation de rang k vaut la somme des s² oubliés (Frobenius)",
             "§3", ""),
            ("M12d.17", "∂", 2, 20, "La pseudo-inverse donne la solution des moindres carrés de plus petite norme",
             "§4", ""),
            ("M12d.18", "∂", 2, 20, "L'erreur de reconstruction moyenne est la somme des variances oubliées", "§7",
             "E"),
            ("M12d.19", "∂", 2, 15, "Les scores de deux composantes principales sont décorrélés", "§6", ""),
            ("M12d.20", "🔗", 1, 15, "Pont : détecter une anomalie par son erreur de reconstruction", "§7", "E"),
            ("M12d.21", "🔗", 2, 15, "Pont : un changement d'unités diagonal D change Σ en DΣD, et les axes principaux "
             "avec ; la standardisation non", "§6", ""),
            ("M12d.22", "📖", 2, 45, "MML §4.5 à §4.7 : SVD, approximation de rang faible, phylogénie des "
             "matrices", "§1 §2 §3 §4", ""),
            ("M12d.23", "📖", 2, 50, "MML §10.1 à §10.6 : l'ACP du livre (la dérivation par Lagrange de §10.2 se "
             "survole : M13b la relit)", "§5 §6 §7", ""),
            ("M12d.24", "🧮", 1, 10, "Fermi : la mémoire et le temps d'une ACP sur un million de clients et 250 "
             "features", "§6 §7", ""),
            ("M12d.25", "🗣️", 1, 10, "Expliquer la SVD comme « rotation, étirement, rotation »", "§2", "E"),
            ("M12d.E1", "💼", 1, 10, "« Comment choisissez-vous le nombre de composantes d'une ACP ? »", "§7", ""),
            ("M12d.E2", "💼", 1, 10, "« Que dit le conditionnement d'une matrice ? »", "§4", ""),
            ("M12d.26", "🔨", 2, 40, "La SVD par les valeurs propres de AᵀA", "§1", "E m:svd"),
            ("M12d.27", "🔨", 1, 20, "Approximation de rang faible et conditionnement", "§3 §4",
             "E m:low_rank_approximation,condition_number p:M12d.26"),
            ("M12d.28", "🔨", 1, 15, "La pseudo-inverse", "§4", "m:pinv p:M12d.26"),
            ("M12d.29", "🔨", 2, 25, "Les axes principaux d'une matrice de covariance, et la variance expliquée",
             "§5 §6 §7",
             "E m:principal_axes,explained_variance_ratio"),
            ("M12d.30", "📦", 1, 15, "`np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA` contre tes "
             "fonctions : les signes", "§1 §4 §6", "E"),
            ("M12d.31", "🔮", 1, 10, "Prédire l'allure des valeurs singulières d'une image, et le rang qui suffit",
             "§3", "E"),
            ("M12d.32", "🔬", 2, 20, "Compresser une image du domaine public : l'erreur en fonction du rang", "§3", ""),
            ("M12d.33", "🔬", 2, 20, "La SVD par AᵀA contre `np.linalg.svd` : ce qu'on perd quand κ est grand",
             "§1 §4", ""),
            ("M12d.34", "🎨", 1, 20, "La SVD en images : Vᵀ, Σ puis U appliqués au cercle unité, étape par étape", "§2",
             "E"),
            ("M12d.35", "🐛", 1, 15, "Chasse à l'erreur : une ACP sans centrer, n et n − 1 mélangés, des axes lus en "
             "lignes au lieu de colonnes", "§6", ""),
            ("M12d.36", "🛠️", 1, 15, "Un test : la reconstruction de rang plein redonne X, et l'erreur décroît avec k",
             "§3 §7", ""),
            ("M12d.37", "🏆", 3, 30, "Défi : compresser une image centrée en gardant 93,5 % de son énergie avec au plus "
             "5 % des nombres", "§3", ""),
        ],
    },
    {
        "id": "M13a", "dir": "m13a_vraisemblance_logistique", "hours": 13.8, "generation_sessions": 2,
        "mml": ["§8.3"],
        "summary": "Le maximum de vraisemblance (Bernoulli, catégorielle, gaussienne), la log-loss comme moins la "
                   "log-vraisemblance, la sigmoïde et la fonction softplus, la régression logistique comme modèle "
                   "probabiliste (et la sonde linéaire), Naïve Bayes comme modèle génératif, l'entropie, l'indice de "
                   "Gini, le gain d'information et la réduction de variance des arbres.",
        "objectives": [
            "Calculer et démontrer des estimateurs du maximum de vraisemblance (Bernoulli, catégorielle, "
            "gaussienne).",
            "Écrire la log-loss comme moins la log-vraisemblance, et la calculer.",
            "Calculer avec la sigmoïde et la softplus, et démontrer la convexité de la softplus.",
            "Lire un modèle logistique : probabilités, cote, frontière de décision.",
            "Calculer à la main un Naïve Bayes avec lissage, en log-probabilités.",
            "Calculer une entropie, un indice de Gini, un gain d'information et une réduction de variance.",
        ],
        "sections": [("§1", "Le maximum de vraisemblance, revisité"),
                     ("§2", "La log-loss est moins la log-vraisemblance"),
                     ("§3", "La sigmoïde et la softplus"),
                     ("§4", "La régression logistique, un modèle probabiliste"),
                     ("§5", "Naïve Bayes, un modèle génératif"),
                     ("§6", "Impureté : entropie, indice de Gini et gain d'information"),
                     ("§7", "Arbres de régression : la réduction de variance")],
        "teaches": ["maximum de vraisemblance", "log-vraisemblance", "log-loss = moins la log-vraisemblance",
                    "régression logistique : le modèle", "convexité de log-somme-exp et de log(1 + eᶻ)",
                    "Naïve Bayes : hypothèse d'indépendance", "impureté d'une distribution : entropie, Gini",
                    "gain d'information (information mutuelle)",
                    "réduction de variance (arbres de régression)", "linear probe"],
        "requires": [("vraisemblance, MAP, lissage de Laplace, log-sum-exp", "M04"),
                     ("entropie, cross-entropy, information mutuelle, inégalité de Gibbs", "M06"),
                     ("sigmoïde, logit, cote", "R6"),
                     ("dérivée seconde, convexité en 1D", "M05a"), ("fonctions convexes de plusieurs variables", "M10"),
                     ("gradient", "M05b"), ("loi normale", "M02b"), ("biais d'un estimateur", "M02c"),
                     ("hyperplans, produit scalaire", "M07")],
        "frontieres": ["13.2", "13.3", "13.6", "13.7", "13.12", "13.27"],
        "mymath": {"module": "likelihood.py",
                   "functions": ["bernoulli_log_likelihood", "bernoulli_mle", "categorical_mle", "gaussian_mle",
                                 "logistic_loss"]},
        "reading_minutes": 180,
        "flashcards": 24,
        "notes": "Frontières : 13.2 (interprétations de l'indice de Gini, maxima avec K = 3), 13.3 (recherche du "
                 "meilleur seuil d'un arbre et gain d'un split), 13.6 (Naïve Bayes multinomial et lissage sur des "
                 "lettres), 13.7 (posterior d'un Naïve Bayes gaussien à deux features), 13.12 et 13.27 (prédictions de"
                 " Naïve Bayes), et le ∂ 13.8 (σ′ = σ(1 − σ), dℓ/dz = p̂ − y, gradient (1/n)Xᵀ(p̂ − y), convexité par "
                 "d²ℓ/dz², pas de minimum sur des données séparables). M13a ne dérive aucun gradient de log-loss, et "
                 "σ′ n'y est ni démontrée ni utilisée (13.8.1, 17.4.1) : la convexité de log-somme-exp se démontre par"
                 " sa restriction à une droite, dont la dérivée seconde est une variance, sans écrire la hessienne "
                 "diag(p) − ppᵀ (le ∂ 17.7 de workbookIA, et M17) ni la dérivée seconde de la softplus (13.8.6) ; la "
                 "softplus en est la composée avec z ↦ (0, z) (M10). M13a.6 utilise l'écriture stable de la softplus "
                 "sans l'établir (le ∂ 18.8.5 de workbookIA la démontre ; 17.13 code une sigmoïde stable). Il reste à "
                 "l'impureté d'une distribution (maxima et concavité pour K quelconque), à l'information mutuelle d'un"
                 " tableau de contingence de deux variables catégorielles quelconques (pas les deux enfants d'un "
                 "split) et à la décomposition de la variance (intra plus inter), sans recherche de split ; Naïve "
                 "Bayes y est l'hypothèse d'indépendance conditionnelle et un modèle génératif (deux gaussiennes de "
                 "même variance donnent un a posteriori logistique), sans classer de mots ni de manchots ; la sonde "
                 "linéaire est le pont M13a.18. Évités : la feuille 10/90 et les nœuds 30/70, 80/20, (3, 1) et (1, 3) "
                 "de la fiche de workbookIA 13, les lois 0,5/0,3/0,2 et 25/75 (13.2), 50/50 (13.Q9) et 6/3/1 (14.R1), "
                 "la figure des trois impuretés d'une loi binaire, les cibles 2, 4, 9, le modèle w = (2, −1), b = 0,5,"
                 " σ(2) et σ′(2), la log-densité en x = 12, le logsumexp de (−1 000, −1 001), le lissage 1/250, le "
                 "nombre de paramètres d'un Naïve Bayes gaussien (13.Q11 c) et les 20 features binaires de la fiche, "
                 "les nageoires et becs des manchots, les lettres e, h, q, w, l'équivalence α = 1/(Cn) de 13.32 et "
                 "(checkpoint III de workbookIA, CP3.12 d) une feature en deux copies dans Naïve Bayes. `likelihood` "
                 "écrit les briques du maximum de vraisemblance et la log-loss à partir des scores ; `categorical_mle`"
                 " est la formule de `MultinomialNB` et `gaussian_mle` l'ajustement d'une classe de `GaussianNB` (des "
                 "briques, que workbookIA assemble) ; `mymath` a déjà `explog.sigmoid`, `approx.logsumexp` et "
                 "`info.mutual_information` (pas réécrits) ; les impuretés, le meilleur split, `log_gaussian_pdf`, "
                 "GaussianNB, MultinomialNB et LogisticRegression sont les fonctions de `mylearn` en workbookIA 13. "
                 "Conventions : log-loss en logarithme népérien, entropies des arbres en bits.",
        "exercises": [
            ("M13a.Q1", "🧠", 1, 4, "Vraisemblance, log-vraisemblance, maximum : le vocabulaire", "§1", "E"),
            ("M13a.Q2", "🧠", 1, 4, "Log-loss et cross-entropy : la même chose ?", "§2", "E"),
            ("M13a.Q3", "🧠", 1, 4, "Les propriétés de la sigmoïde et de la softplus", "§3", "E"),
            ("M13a.Q4", "🧠", 1, 4, "Ce que modélise un score w · x + b", "§4", "E"),
            ("M13a.Q5", "🧠", 1, 4, "Génératif ou discriminant ?", "§4 §5", "E"),
            ("M13a.Q6", "🧠", 1, 4, "Entropie et Gini : leurs propriétés", "§6", "E"),
            ("M13a.Q7", "🧠", 1, 4, "Variance intra et variance inter : les feuilles d'un arbre de régression", "§7",
             ""),
            ("M13a.Q8", "🧠", 1, 4, "Convexe ou pas ?", "§3 §4", ""),
            ("M13a.R1", "🔁", 1, 5, "Bayes et le lissage de Laplace (M04)", "§5", "E"),
            ("M13a.R2", "🔁", 1, 5, "Entropie, cross-entropy et information mutuelle (M06)", "§2 §6", "E"),
            ("M13a.R3", "🔁", 1, 5, "Fonctions convexes de plusieurs variables (M10)", "§3", "E"),
            ("M13a.1", "✏️", 1, 15, "Le maximum de vraisemblance d'une loi de Bernoulli et d'une loi catégorielle",
             "§1", "E"),
            ("M13a.2", "✏️", 2, 20, "Le maximum de vraisemblance d'une loi normale : μ̂ et σ̂²", "§1", "E"),
            ("M13a.3", "✏️", 1, 15, "La log-loss de quatre prédictions, puis la même en cross-entropy", "§2", "E"),
            ("M13a.4", "✏️", 1, 15, "Le poids d'un seul exemple mal prédit : la log-loss quand p tend vers 0",
             "§2", ""),
            ("M13a.5", "✏️", 1, 15, "La sigmoïde : valeurs, logit, cote et symétrie σ(−z) = 1 − σ(z)", "§3", "E"),
            ("M13a.6", "✏️", 1, 15, "La softplus : valeurs, asymptotes et comportement pour |z| grand", "§3", "E"),
            ("M13a.7", "✏️", 1, 15, "Un modèle logistique à deux features : probabilités, cote et frontière de "
             "décision", "§4", "E"),
            ("M13a.8", "✏️", 2, 25, "L'hypothèse naïve à la main : une loi jointe factorisée, comparée à la vraie",
             "§5", "E"),
            ("M13a.9", "✏️", 2, 20, "Deux classes gaussiennes de même variance : l'a posteriori est une sigmoïde "
             "d'un score affine", "§4 §5", ""),
            ("M13a.10", "✏️", 1, 15, "L'entropie et l'indice de Gini de quelques distributions", "§6", "E"),
            ("M13a.11", "✏️", 2, 25, "L'information mutuelle d'un tableau de contingence, et la baisse d'entropie "
             "qu'elle mesure", "§6", "E"),
            ("M13a.12", "✏️", 2, 15, "La variance d'un groupe coupé en deux : variance intra plus variance inter",
             "§7", ""),
            ("M13a.13", "∂", 2, 20, "Le maximum de vraisemblance d'une loi catégorielle, par l'inégalité de Gibbs",
             "§1", "E"),
            ("M13a.14", "∂", 1, 15, "La log-loss moyenne est moins la log-vraisemblance divisée par n", "§2", "E"),
            ("M13a.15", "∂", 3, 25, "Log-somme-exp est convexe : sur une droite, sa dérivée seconde est une variance "
             "; la softplus aussi", "§3 §4", "E"),
            ("M13a.16", "∂", 2, 20, "L'indice de Gini est maximal pour la loi uniforme", "§6", ""),
            ("M13a.17", "∂", 2, 15, "L'entropie est maximale pour la loi uniforme, par l'inégalité de Gibbs", "§6",
             ""),
            ("M13a.18", "🔗", 1, 25, "Pont : une sonde linéaire, un modèle logistique en NumPy sur un batch de "
             "représentations figées, jusqu'à la log-loss", "§4", "E"),
            ("M13a.19", "📖", 2, 30, "MML §8.3, relu après M04 : estimer des paramètres, et ce que la régression "
             "logistique y ajoute", "§1 §4", ""),
            ("M13a.20", "🧮", 1, 10, "Fermi : la loi jointe complète contre l'hypothèse naïve, combien de nombres pour "
             "30 features à 4 valeurs ?", "§5", ""),
            ("M13a.21", "🗣️", 1, 10, "Expliquer pourquoi on minimise la log-loss plutôt que le taux d'erreur",
             "§2 §4", "E"),
            ("M13a.E1", "💼", 1, 10, "« Pourquoi la cross-entropy est-elle une log-vraisemblance ? »", "§2", ""),
            ("M13a.E2", "💼", 1, 10, "« Qu'est-ce que le maximum de vraisemblance, et quel lien avec les losses que "
             "vous minimisez ? »", "§1 §2", ""),
            ("M13a.22", "🔨", 1, 15, "La log-vraisemblance et le maximum de vraisemblance d'une loi de Bernoulli",
             "§1", "E m:bernoulli_log_likelihood,bernoulli_mle"),
            ("M13a.23", "🔨", 1, 20, "Maximum de vraisemblance catégoriel, avec lissage, et gaussien", "§1 §5",
             "E m:categorical_mle,gaussian_mle"),
            ("M13a.24", "🔨", 2, 20, "La log-loss à partir des scores, sans débordement", "§2 §3", "E m:logistic_loss"),
            ("M13a.25", "📦", 1, 25, "`scipy.stats`, `scipy.special` et `sklearn.metrics.log_loss` contre tes "
             "fonctions", "§1 §2 §3", "E"),
            ("M13a.26", "🔮", 1, 10, "Prédire la log-loss d'un modèle qui répond toujours 0,5, puis toujours la "
             "fréquence des 1", "§2", "E"),
            ("M13a.27", "🔬", 2, 20, "La variabilité du maximum de vraisemblance d'une loi de Bernoulli d'un "
             "échantillon à l'autre", "§1", ""),
            ("M13a.28", "🎨", 1, 25, "L'entropie et l'indice de Gini sur les lois à trois issues : lignes de niveau et "
             "maximum au centre", "§6", "E"),
            ("M13a.29", "🐛", 1, 15, "Chasse à l'erreur : un ln 0, une sigmoïde qui déborde, une variance de maximum "
             "de vraisemblance divisée par n − 1", "§1 §2 §3", ""),
            ("M13a.30", "🛠️", 1, 15, "Vérifier avec SymPy le maximum de vraisemblance d'une loi géométrique et d'une "
             "loi de Poisson", "§1", ""),
            ("M13a.31", "🏆", 3, 25, "Défi : la proportion d'un mélange de deux lois connues par maximum de "
             "vraisemblance, à 1e−6 près du maximum (dichotomie ou Newton)", "§1", ""),
        ],
    },
    {
        "id": "M13b", "dir": "m13b_lagrange_svm", "hours": 16.1, "generation_sessions": 1,
        "mml": ["§7.2", "§7.3", "ch. 12"],
        "summary": "L'optimisation sous contraintes : multiplicateurs de Lagrange, conditions KKT, dualité, "
                   "optimisation convexe, et l'ACP relue par Lagrange ; puis les SVM : marge, problème primal à marge "
                   "dure et souple, hinge loss et sous-gradient, problème dual, vecteurs de support, noyaux et astuce "
                   "du noyau (polynomial, RBF).",
        "objectives": [
            "Résoudre un problème d'optimisation sous contraintes d'égalité par les multiplicateurs de Lagrange.",
            "Écrire les conditions KKT d'un problème avec inégalités, et sa fonction duale.",
            "Reconnaître un problème convexe et ce qu'il garantit.",
            "Écrire le problème d'une SVM à marge dure et à marge souple, et le relier à la hinge loss.",
            "Lire le problème dual d'une SVM et ses vecteurs de support.",
            "Calculer avec des noyaux polynomiaux et RBF, et reconnaître un noyau valide.",
        ],
        "sections": [("§1", "Optimiser sous une contrainte d'égalité : les multiplicateurs de Lagrange"),
                     ("§2", "Plusieurs contraintes, et l'ACP relue par Lagrange"),
                     ("§3", "Contraintes d'inégalité : les conditions KKT"),
                     ("§4", "La dualité (aperçu)"),
                     ("§5", "L'optimisation convexe"),
                     ("§6", "La SVM à marge dure"),
                     ("§7", "Marge souple, hinge loss et sous-gradient"),
                     ("§8", "Le problème dual, les vecteurs de support et les noyaux")],
        "teaches": ["optimisation sous contraintes", "multiplicateurs de Lagrange", "conditions KKT",
                    "dualité (aperçu)", "optimisation convexe", "relire MML §10.2 : l'ACP par Lagrange", "marge",
                    "SVM primal", "hinge loss", "sous-gradient", "SVM dual", "noyaux et astuce du noyau", "noyau RBF"],
        "requires": [("marge géométrique, astuce du biais, séparabilité, programmes linéaires", "M10"),
                     ("gradient, lignes de niveau", "M05b"),
                     ("matrices définies positives, quotient de Rayleigh, matrice de Gram", "M12c"),
                     ("axes principaux", "M12d"), ("distance à un hyperplan", "M07"), ("systèmes linéaires", "M09a")],
        "frontieres": ["13.4", "13.5", "13.17"],
        "mymath": {"module": "svm.py",
                   "functions": ["lagrange_equality_qp", "hinge_loss", "svm_subgradient", "rbf_kernel",
                                 "polynomial_kernel"]},
        "reading_minutes": 180,
        "flashcards": 24,
        "notes": "Frontières : 13.4 (vérifier une solution de SVM primal sur six points), 13.5 (le noyau (x · z)² et φ"
                 " = (x₁², √2 x₁x₂, x₂²)), 13.17 (des cercles relevés en 3D par x₁² + x₂²), et le ∂ 13.8. M13b résout "
                 "de petites SVM par les conditions KKT et le dual (un énoncé plus général que la vérification de "
                 "13.4) et enseigne l'astuce du noyau par (1 + x · z)², la matrice de Gram semi-définie positive et le"
                 " développement en série du noyau RBF. Conventions : marge = 1/‖w‖ (de la frontière au point le plus "
                 "proche, comme MML §12.2 et M10), largeur de la bande = 2/‖w‖ (le syllabus de workbookIA 13 écrit « "
                 "marge = 2/‖w‖ », sa fiche dit 1/‖w‖) ; RBF écrit avec γ ; contrainte de boîte 0 ≤ αᵢ ≤ C dans le "
                 "dual. Évités : l'exemple x₁ + 2x₂ − 4 = 0 et le point (3, 3), les valeurs du RBF à distance 1 (γ = "
                 "0,1, 1, 10), φ(2, 0) et φ(1, 1), et, pour motiver les noyaux, le ou exclusif, les cercles, le "
                 "relèvement |x| → (x, x²), les spirales et les demi-lunes ; les six coordonnées de φ en M13b.12 sont "
                 "un rappel de `linreg.count_monomials` (M09b), pas un comptage par étoiles et barres (workbookIA "
                 "15.4). Le 🏆 M13b.34 mesure l'optimisation : l'objectif J, à 1 % de celui de `SVC(kernel=\"linear\")` "
                 "au même C. workbookIA n'écrit pas de SVM (pas de `mylearn`) : `svm` écrit Lagrange sous contraintes "
                 "d'égalité, la hinge loss et son sous-gradient, et les noyaux ; NumPy permis, pas `scipy.optimize`, "
                 "`scipy.spatial` ni scikit-learn.",
        "exercises": [
            ("M13b.Q1", "🧠", 1, 4, "Lagrange : ce que dit ∇f = λ ∇g", "§1", "E"),
            ("M13b.Q2", "🧠", 1, 4, "Contrainte active ou inactive ?", "§3", "E"),
            ("M13b.Q3", "🧠", 1, 4, "Primal, dual, dualité faible", "§4", ""),
            ("M13b.Q4", "🧠", 1, 4, "Problème convexe ou pas ?", "§5", "E"),
            ("M13b.Q5", "🧠", 1, 4, "Ce que maximise une SVM, ce que minimise son problème", "§6", "E"),
            ("M13b.Q6", "🧠", 1, 4, "La hinge loss : vrai ou faux", "§7", "E"),
            ("M13b.Q7", "🧠", 1, 4, "Noyau valide ou pas ?", "§8", "E"),
            ("M13b.Q8", "🧠", 1, 4, "Primal ou dual : lequel résoudre, et quand ?", "§8", ""),
            ("M13b.R1", "🔁", 1, 5, "La marge géométrique et l'astuce du biais (M10)", "§6", "E"),
            ("M13b.R2", "🔁", 1, 5, "Gradient et lignes de niveau (M05b)", "§1", "E"),
            ("M13b.R3", "🔁", 1, 5, "Matrices définies positives (M12c)", "§5 §8", "E"),
            ("M13b.1", "✏️", 1, 15, "Lagrange à la main : un produit maximal sous une contrainte linéaire", "§1", "E"),
            ("M13b.2", "✏️", 2, 20, "La distance d'un point à un plan, retrouvée par Lagrange", "§1", ""),
            ("M13b.3", "✏️", 2, 20, "Un problème quadratique sous deux contraintes linéaires : le système de "
             "Lagrange", "§2", "E"),
            ("M13b.4", "✏️", 2, 20, "Relire l'ACP par Lagrange : maximiser uᵀCu sous ‖u‖ = 1", "§2", ""),
            ("M13b.5", "✏️", 2, 20, "Une contrainte d'inégalité : active ou non, les conditions KKT à la main", "§3",
             "E"),
            ("M13b.6", "✏️", 2, 20, "La fonction duale d'un petit problème quadratique, et la dualité faible", "§4",
             ""),
            ("M13b.7", "✏️", 1, 15, "Reconnaître un problème convexe : fonctions, contraintes, ensembles", "§5", "E"),
            ("M13b.8", "✏️", 2, 25, "Une SVM à marge dure sur trois points, résolue par les conditions KKT", "§6 §8",
             "E"),
            ("M13b.9", "✏️", 1, 15, "La hinge loss et l'objectif régularisé de quelques points", "§7", "E"),
            ("M13b.10", "✏️", 2, 15, "Un pas de sous-gradient sur l'objectif d'une SVM linéaire", "§7", ""),
            ("M13b.11", "✏️", 2, 20, "Le dual d'une SVM : lire les vecteurs de support et retrouver w", "§8", ""),
            ("M13b.12", "✏️", 2, 20, "Le noyau (1 + x · z)² en dimension 2 : sa fonction φ à six coordonnées", "§8",
             ""),
            ("M13b.13", "✏️", 1, 15, "La matrice de Gram d'un noyau RBF sur trois points, et l'effet de γ", "§8", "E"),
            ("M13b.14", "∂", 2, 20, "Au point optimal sous une contrainte d'égalité, ∇f est colinéaire à ∇g", "§1", ""),
            ("M13b.15", "∂", 2, 15, "La dualité faible : la fonction duale minore le minimum du primal", "§4", "E"),
            ("M13b.16", "∂", 2, 15, "Pour un problème convexe, un minimum local est global", "§5", "E"),
            ("M13b.17", "∂", 2, 20, "Maximiser la marge revient à minimiser ½ ‖w‖²", "§6", "E"),
            ("M13b.18", "∂", 2, 20, "Marge souple : la formulation avec des variables d'écart et celle avec la hinge "
             "loss sont équivalentes", "§7", ""),
            ("M13b.19", "∂", 3, 25, "La somme et le produit de deux noyaux sont des noyaux ; une matrice de Gram est "
             "semi-définie positive", "§8", ""),
            ("M13b.20", "🔗", 1, 15, "Pont : la décision d'une SVM à noyau, une somme pondérée sur les vecteurs de "
             "support", "§8", "E"),
            ("M13b.21", "📖", 2, 40, "MML §7.2 et §7.3 : Lagrange, dualité et optimisation convexe, en "
             "anglais", "§1 §3 §4 §5", ""),
            ("M13b.22", "📖", 2, 50, "MML §12.2 à §12.5 : marge, primal, dual et noyaux (§12.1 a été lu en "
             "M10)", "§6 §7 §8", ""),
            ("M13b.23", "🧮", 1, 10, "Fermi : la taille de la matrice de Gram d'une SVM à noyau sur 100 000 exemples",
             "§8", ""),
            ("M13b.24", "🗣️", 1, 10, "Expliquer un multiplicateur de Lagrange comme un prix", "§1 §4", "E"),
            ("M13b.E1", "💼", 1, 10, "« Qu'est-ce qu'un problème d'optimisation convexe, et pourquoi est-ce une bonne "
             "nouvelle ? »", "§5", ""),
            ("M13b.E2", "💼", 1, 10, "« Hinge loss ou log-loss : quelles différences ? »", "§7", ""),
            ("M13b.25", "🔨", 1, 20, "Un problème quadratique sous contraintes d'égalité, par le système de Lagrange",
             "§2", "E m:lagrange_equality_qp"),
            ("M13b.26", "🔨", 2, 25, "La hinge loss et un sous-gradient de l'objectif d'une SVM linéaire", "§7",
             "E m:hinge_loss,svm_subgradient"),
            ("M13b.27", "🔨", 1, 20, "Les noyaux RBF et polynomial", "§8", "E m:rbf_kernel,polynomial_kernel"),
            ("M13b.28", "📦", 1, 15, "`scipy.optimize.minimize` sous contraintes et les noyaux de scikit-learn contre "
             "tes fonctions", "§2 §8", "E"),
            ("M13b.29", "🔮", 1, 10, "Prédire : comment change le minimum quand on relâche la contrainte, et ce que "
             "dit λ", "§1 §4", "E"),
            ("M13b.30", "🔬", 2, 20, "La descente de sous-gradient sur la hinge loss : pas constant contre pas "
             "décroissant", "§7", ""),
            ("M13b.31", "🎨", 1, 20, "Lignes de niveau et contrainte : voir le point de Lagrange", "§1", "E"),
            ("M13b.32", "🐛", 1, 15, "Chasse à l'erreur : le signe d'un multiplicateur, une largeur de bande 1/‖w‖ au "
             "lieu de 2/‖w‖, une matrice de Gram non symétrique", "§3 §6 §8", ""),
            ("M13b.33", "🛠️", 1, 15, "Vérifier une solution KKT : faisabilité, stationnarité, complémentarité",
             "§3", ""),
            ("M13b.34", "🏆", 3, 30, "Défi : une SVM linéaire entraînée par sous-gradient, un objectif à 1 % de celui "
             "de scikit-learn au même C", "§7", ""),
        ],
    },
    {
        "id": "M14", "dir": "m14_ensembles", "hours": 7.2, "generation_sessions": 1, "mml": [],
        "summary": "Les outils des ensembles de modèles : la queue de la loi binomiale et sa borne de Chernoff, la "
                   "variance d'une moyenne "
                   "pondérée de variables corrélées, la limite (1 + x/n)ⁿ → eˣ, les poids exponentiels (l'algorithme "
                   "Hedge) et le gradient d'une loss par rapport aux prédictions. workbookIA 14 les applique au vote, "
                   "au bagging et au boosting.",
        "objectives": [
            "Calculer la queue d'une loi binomiale, et la majorer par la borne de Chernoff.",
            "Calculer la variance d'une moyenne pondérée de variables corrélées par leur matrice de covariance.",
            "Démontrer et utiliser la limite (1 + x/n)ⁿ → eˣ.",
            "Calculer des poids exponentiels renormalisés, et suivre le meilleur de plusieurs experts.",
            "Calculer le gradient d'une loss par rapport au vecteur des prédictions.",
        ],
        "sections": [("§1", "La queue d'une loi binomiale"),
                     ("§2", "La variance d'une moyenne de variables corrélées"),
                     ("§3", "La limite (1 + x/n)ⁿ → eˣ"),
                     ("§4", "Des poids exponentiels : l'algorithme Hedge"),
                     ("§5", "Le gradient d'une loss par rapport aux prédictions")],
        "teaches": ["queue de la loi binomiale", "borne de Chernoff (divergence KL)",
                    "variance d'une moyenne de variables corrélées",
                    "(1 + x/n)ⁿ → eˣ", "poids exponentiels et renormalisation",
                    "descente de gradient dans un espace de fonctions (idée)",
                    "forêt aléatoire : décorréler pour réduire la variance"],
        "requires": [("loi binomiale", "M02b"), ("covariance, variance d'une somme, matrice de covariance", "M02c"),
                     ("développements de Taylor, ln(1 + u)", "M05a"),
                     ("inégalité de Hoeffding, méthode de Chernoff, regret", "M11"), ("divergence KL", "M06"),
                     ("gradient", "M05b"), ("loss de Huber", "M09b"), ("log-loss", "M13a")],
        "frontieres": ["14.5", "14.6", "14.7", "14.13", "14.23"],
        "mymath": {"module": "ensembles.py",
                   "functions": ["chernoff_bound", "variance_of_average", "hedge_weights"]},
        "reading_minutes": 90,
        "flashcards": 12,
        "notes": "Réduit à 7 h. Frontières : 14.5 (la majorité de votants indépendants), 14.6 et 14.23 (une itération "
                 "d'AdaBoost, les mal classés qui pèsent la moitié), 14.7 (deux itérations de gradient boosting), "
                 "14.13 (des votants corrélés par un choc commun), et les ∂ 14.3 ((1 − 1/n)ⁿ → e⁻¹ dans le bootstrap) "
                 "et 14.4 (les résidus comme gradient de la MSE, la médiane pour la valeur absolue, y − p̂ pour la "
                 "log-loss). Hors des cadres de workbookIA : la queue binomiale sur la fiabilité de systèmes « k parmi"
                 " n » (calculée avec `testing.binomial_test` de M08) et la borne de Chernoff exp(−n KL(a ‖ p)), qui "
                 "généralise CP2.9 B et relie M06 à M11 (le théorème du jury en général) ; la limite (1 + x/n)ⁿ → eˣ "
                 "pour tout x (intérêts composés, survie) ; la variance d'une moyenne pondérée par aᵀΣa, sur des "
                 "prédictions continues et deux groupes de modèles (M14.9, M14.13) ; les poids exponentiels de "
                 "l'algorithme Hedge (des experts, avec un learning rate qui décroît quand l'horizon est inconnu, "
                 "M14.17) ; le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport aux "
                 "prédictions, d'où les poids exponentiels (M14.5). Le checkpoint III de workbookIA démontre ρσ² + (1 "
                 "− ρ)σ²/M (CP3.13, que la copie figée ne permet pas de lister ici) : M14 ne démontre ni ne chiffre ce"
                 " cas équicorrélé ; « la moyenne minimise les carrés » et « la médiane minimise les écarts absolus » "
                 "ne sont pas redémontrés. Évités : la redondance triple d'Apollo (2 parmi 3), 15 votants à 70 % "
                 "(14.Q1), 7 votants à 80 %, les q et M de 14.5 (0,7 pour 3, 5, 9 votants ; 0,6 et 11 ; 0,51 et 101 ; "
                 "0,45 et 25 ; 0,65 et 7), q = 0,58 (14.13), q = 42 %, 55 %, 65 %, ρ = 0,2 et 0,6, σ² = 1 et ρ = 0,5, "
                 "les valeurs de CP3.13 (σ² = 4, ρ = 0,25, M = 10 ; ρ = 0,1, σ² = 5), x = −1 dans la limite (0,9¹⁰, "
                 "0,999¹⁰⁰⁰, 100 ln 0,99, n = 5 et 0,328), a = 3/4 et p = 1/2 (CP2.9 B), AdaBoost à 20 exemples, les "
                 "cibles 3 et 4 du gradient boosting, l'hypergéométrique 32, 5, 2 (14.16). Le bootstrap qui oublie "
                 "36,8 % des points, les résidus comme gradient, la majorité qui se trompe, AdaBoost et le gradient "
                 "boosting à la main sont des exercices de workbookIA 14 ; `ensembles` n'écrit ni vote ni mise à jour "
                 "d'AdaBoost (`mylearn`), ni de queue binomiale exacte (`testing.binomial_test`, M08).",
        "exercises": [
            ("M14.Q1", "🧠", 1, 4, "La queue d'une loi binomiale et ses bornes : vrai ou faux", "§1", "E"),
            ("M14.Q2", "🧠", 1, 4, "Corrélation et variance d'une moyenne", "§2", "E"),
            ("M14.Q3", "🧠", 1, 4, "Des limites remarquables", "§3", "E"),
            ("M14.Q4", "🧠", 1, 4, "Des poids exponentiels", "§4", ""),
            ("M14.R1", "🔁", 1, 5, "La log-loss et la divergence KL (M13a, M06)", "§1 §5", "E"),
            ("M14.R2", "🔁", 1, 5, "La variance d'une somme et la matrice de covariance (M02c)", "§2", "E"),
            ("M14.R3", "🔁", 1, 5, "Taylor et ln(1 + u) (M05a)", "§3", "E"),
            ("M14.1", "✏️", 1, 15, "La fiabilité d'un système « k parmi n » : au moins k composants qui marchent",
             "§1", "E"),
            ("M14.2", "✏️", 1, 15, "La variance de la moyenne de trois mesures corrélées, par la matrice de "
             "covariance", "§2", "E"),
            ("M14.3", "✏️", 1, 10, "(1 + x/n)ⁿ pour quelques n, et des intérêts composés en continu", "§3", "E"),
            ("M14.4", "✏️", 1, 15, "Les poids exponentiels de cinq experts après trois tours", "§4", "E"),
            ("M14.5", "✏️", 2, 15, "Le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport "
             "aux prédictions, et les poids exponentiels qu'il fait apparaître", "§4 §5", ""),
            ("M14.6", "∂", 2, 20, "(1 + x/n)ⁿ → eˣ, par le logarithme et ln(1 + u) ≈ u", "§3", "E"),
            ("M14.7", "∂", 2, 15, "Une moyenne pondérée de variables de variance σ² a une variance au plus σ²", "§2",
             ""),
            ("M14.8", "∂", 3, 25, "La borne de Chernoff d'une queue binomiale : le meilleur λ donne exp(−n KL(a ‖ "
             "p))", "§1", ""),
            ("M14.9", "🔗", 1, 15, "Pont : ajouter des modèles très corrélés ne sert presque à rien, un plancher de "
             "variance sur deux groupes de modèles", "§2", "E"),
            ("M14.10", "🗣️", 1, 10, "Expliquer pourquoi une moyenne réduit la variance, et quand elle ne la réduit "
             "plus", "§2", "E"),
            ("M14.E1", "💼", 1, 10, "« Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est "
             "le meilleur ? »", "§4", ""),
            ("M14.11", "🔨", 1, 20, "La borne de Chernoff et la variance d'une moyenne "
             "pondérée", "§1 §2", "E m:chernoff_bound,variance_of_average"),
            ("M14.12", "🔨", 1, 15, "Les poids de l'algorithme Hedge", "§4", "m:hedge_weights"),
            ("M14.13", "🔬", 2, 20, "Simuler la moyenne de deux groupes de modèles corrélés, et retrouver aᵀΣa et son "
             "plancher", "§2", "E"),
            ("M14.14", "🎨", 1, 15, "Les poids exponentiels au fil des tours : quel expert domine, selon le learning "
             "rate", "§4", ""),
            ("M14.15", "🐛", 1, 15, "Chasse à l'erreur : P(X ≥ k) calculée comme P(X > k), des covariances oubliées, "
             "des poids non renormalisés", "§1 §2 §4", ""),
            ("M14.16", "🛠️", 1, 15, "Un test qui vérifie que la borne de Chernoff majore la queue exacte de "
             "`scipy.stats`, sur une grille de n, p et a", "§1", ""),
            ("M14.17", "🏆", 3, 25, "Défi : suivre le meilleur de dix experts avec Hedge sans connaître l'horizon, un "
             "regret sous la borne théorique sur 1 000 tours", "§4", ""),
        ],
    },
    {
        "id": "CP3", "dir": "checkpoints/partie_3", "hours": 3.1, "generation_sessions": 1, "mml": [],
        "summary": "Le bilan de la partie III (M12a à M14), juste avant le checkpoint III de workbookIA : un examen "
                   "blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis "
                   "une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.",
        "objectives": [
            "Vérifier en temps limité que les notions de la partie III sont acquises.",
            "Construire ta propre synthèse de la partie III.",
        ],
        "sections": [("§1", "Examen blanc"), ("§2", "Synthèse")],
        "teaches": ["révision de la partie III"],
        "requires": [("toute la partie III", "M14")],
        "frontieres": ["12.6", "12.7", "12.8", "12.22", "12.27", "12.29", "12.R3", "13.2", "13.3", "13.4", "13.5",
                       "13.6", "13.7", "13.8", "13.12", "13.17", "13.27", "14.3", "14.4", "14.5", "14.6", "14.7",
                       "14.13", "14.23", "15.3"],
        "reading_minutes": 15,
        "flashcards": 0,
        "notes": "Fichiers comme CP2 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, "
                 "03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend"
                 " le checkpoint III de workbookIA (`checkpoints/partie_3/` de workbookIA : prédictions de "
                 "scikit-learn, standardiser et encoder des becs de manchots, Gini et meilleur seuil sur six points, "
                 "kNN avant et après standardisation, une itération d'AdaBoost et une de gradient boosting, fuites "
                 "d'un script, seuil de coût minimal, courbes de validation et de boosting, l'astuce du noyau par une "
                 "parabole, calibration et déploiement, precision et folds stratifiés, Naïve Bayes avec une feature en"
                 " deux copies, variance d'une moyenne de modèles corrélés, coût d'une recherche en grille), qui se "
                 "fait juste après, ni son mini-projet III (recensement Adult, revenus, audit d'équité). CP3.10 "
                 "n'enchaîne pas la suite de 12.7 (un vecteur donné puis vérifié, la part expliquée, les coordonnées, "
                 "la reconstruction, le blanchiment), et CP3.7 ne porte pas sur la variance d'une moyenne de modèles "
                 "corrélés (CP3.13 de workbookIA).",
        "exercises": [
            ("CP3.Q1", "🧠", 1, 10, "Dix affirmations sur la partie III : vrai ou faux", "§1", "E"),
            ("CP3.1", "✏️", 2, 10, "Indépendance, base, rang et noyau", "§1", "E"),
            ("CP3.2", "✏️", 2, 10, "Gram-Schmidt, projection et moindres carrés", "§1", "E"),
            ("CP3.3", "✏️", 2, 10, "Valeurs propres, matrice définie positive et Cholesky", "§1", "E"),
            ("CP3.4", "✏️", 2, 10, "SVD, rang faible et variance expliquée", "§1", "E"),
            ("CP3.5", "✏️", 2, 9, "Maximum de vraisemblance, log-loss et entropie", "§1", "E"),
            ("CP3.6", "✏️", 2, 9, "Lagrange, hinge loss et noyau", "§1", "E"),
            ("CP3.7", "✏️", 2, 8, "Queue binomiale et borne de Chernoff, limite et poids exponentiels", "§1", "E"),
            ("CP3.8", "∂", 3, 12, "Une démonstration courte, au choix parmi deux", "§1", "E"),
            ("CP3.9", "🐛", 2, 8, "Corriger une copie : cinq erreurs", "§1", "E f:02"),
            ("CP3.10", "🔗", 2, 14, "Problème de synthèse : des données centrées, leurs axes principaux, un modèle "
             "sur les scores", "§1", "E"),
            ("CP3.11", "🗣️", 1, 60, "Ta carte mentale et ta fiche d'une page", "§2", "E"),
        ],
    },
]
