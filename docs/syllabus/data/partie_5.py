"""Syllabus, part V (before workbookIA chapters 21 to 24): detailed in session 56 (M21, M22, CP5).

Format: tools/syllabus.py. Exercise tuple: (id, type, stars, minutes, title, covers, flags);
flags: E (essential track), c:wbm|pytest|manuel, f:02|03, p:prerequisites, m:mymath functions written.

Sharing rule (BIBLE §8, §24): every proof (∂) of the workbookIA chapter a math chapter prepares is a frontier
(tools/syllabus.py adds them); ``frontieres`` lists further workbookIA exercises not to solve nor paraphrase. A math
chapter teaches the tool in another setting and may state a result whose proof workbookIA asks. As in part IV, the
math chapters work outside the networks: sampled signals, grids of measurements, polynomials and dice for the
convolution; populations, reservoirs, savings, wearing equipment and maps of the plane for the recurrences; never a
layer, a learned filter, a cell, a gate, an activation, a loss or an attack. workbookIA 23 and 24 have no math
chapter: M21 also prepares the convolution tools of workbookIA 24 (padding « same » with a stride, cost of a
convolution), M22 its carried state (a remark). The notes of each chapter list the data of workbookIA to avoid; CP5
is also compared with the checkpoint V and the mini-project V of workbookIA.
"""

CHAPTERS = [
    {
        "id": "M21", "dir": "m21_convolution", "hours": 14.8, "generation_sessions": 1, "mml": [],
        "summary": "La convolution, d'abord entre deux suites (le produit de deux polynômes, la loi de la somme de deux "
                   "dés, une moyenne mobile), puis la corrélation croisée des bibliothèques, qui ne retourne pas le "
                   "noyau, et les pochoirs de différences finies ; la convolution comme application linéaire, de "
                   "matrice de Toeplitz creuse ; l'équivariance par translation, les convolutions circulaires et le "
                   "pooling ; le pas, la dilatation, le padding, le nombre de positions d'une fenêtre (un "
                   "dénombrement) et la convolution transposée ; les grilles de mesures à plusieurs canaux, les noyaux "
                   "séparables, les paramètres et le coût ; la composition de convolutions et le champ récepteur ; "
                   "enfin le pire cas d'une petite perturbation, une forme linéaire maximisée sur une boule. "
                   "workbookIA 21 applique ces outils aux réseaux convolutifs.",
        "objectives": [
            "Calculer à la main la convolution et la corrélation croisée de deux suites, dans les modes plein, valide "
            "et même taille, et passer d'une convention à l'autre.",
            "Écrire la matrice de Toeplitz d'une convolution, compter ses coefficients non nuls, et lire son rang.",
            "Démontrer et utiliser l'équivariance par translation, et reconnaître une convolution circulaire.",
            "Compter les positions d'une fenêtre avec pas, dilatation et padding, et calculer la taille d'une "
            "convolution transposée.",
            "Compter les paramètres et le coût d'un filtrage à plusieurs canaux, et séparer un noyau de rang 1.",
            "Composer des convolutions en une seule, et calculer un champ récepteur.",
            "Trouver le pire cas d'une perturbation bornée d'une forme linéaire, pour les normes L∞ et L2.",
        ],
        "sections": [("§1", "La convolution de deux suites : polynômes, dés et moyennes mobiles"),
                     ("§2", "Corrélation croisée, retournement, modes et pochoirs"),
                     ("§3", "La convolution comme application linéaire : matrices de Toeplitz et matrices creuses"),
                     ("§4", "Équivariance par translation : décalages, convolutions circulaires et pooling"),
                     ("§5", "Pas, dilatation, padding : compter les positions, et la convolution transposée"),
                     ("§6", "Grilles de mesures et canaux : noyaux séparables, paramètres et coût"),
                     ("§7", "Composer des convolutions : noyau équivalent et champ récepteur"),
                     ("§8", "Le pire cas d'une petite perturbation : une forme linéaire sur une boule")],
        "teaches": ["convolution de deux suites : produit de polynômes, loi de la somme de deux variables discrètes "
                    "indépendantes, moyenne mobile ; commutative, associative, linéaire",
                    "corrélation croisée (sans retournement, celle des bibliothèques) et convolution (noyau "
                    "retourné) ; modes plein, valide et même taille ; conventions d'indices",
                    "pochoirs de différences finies : dérivée, dérivée seconde, laplacien discret",
                    "matrice de Toeplitz d'une convolution ; matrice creuse : coefficients non nuls, coût d'un produit",
                    "matrice des fenêtres (im2col, la notion) : une convolution est un produit matriciel",
                    "transposée de la matrice d'une convolution : énoncée en général, démontrée pour les matrices "
                    "circulantes",
                    "équivariance par translation ; convolution circulaire, matrices circulantes ; une application "
                    "linéaire qui commute avec le décalage circulaire est une convolution circulaire",
                    "pooling moyen (une convolution suivie d'un sous-échantillonnage) et pooling max (non linéaire, "
                    "invariance locale)",
                    "pas, dilatation, padding : nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 démontré comme "
                    "un dénombrement ; padding « même taille », avec ou sans pas (⌈n/s⌉)",
                    "sous-échantillonnage et insertion de zéros, deux matrices transposées l'une de l'autre ; "
                    "convolution transposée : taille, recouvrements, damier ; une taille de sortie vient de "
                    "plusieurs tailles d'entrée",
                    "convolution 2D sur des grilles de mesures à plusieurs canaux, convolution 1 × 1, convolutions "
                    "groupées et par canal : paramètres C_out(C_in/g · k_h k_w + 1), coût et mémoire",
                    "noyau séparable : un noyau de rang 1 (produit extérieur) s'applique en deux convolutions 1D",
                    "composition de convolutions : noyau équivalent (associativité), pas produit, champ récepteur "
                    "(récurrence et forme close)",
                    "maximum d'une forme linéaire sur une boule : ε‖g‖₁ en ε signe(g) pour la norme L∞, ε‖g‖₂ pour "
                    "la norme L2"],
        "requires": [("partie entière ⌊x⌋ et ⌈x⌉", "R1"), ("fonction signe", "R2"), ("polynômes", "R3"),
                     ("sommes Σ, raisonnement par récurrence", "R4"), ("moyenne mobile", "R5"),
                     ("loi d'un couple de variables discrètes, indépendance", "M02b"),
                     ("différences finies avant et centrée", "M05a"),
                     ("normes L1, L2 et L∞, Cauchy-Schwarz", "M07"),
                     ("produit matriciel, transposée, coût d'un produit", "M09a"), ("moindres carrés", "M09b"),
                     ("matrice d'une application linéaire, noyau, rang", "M12a"),
                     ("rang 1, décomposition en valeurs singulières", "M12d"),
                     ("approximation au premier ordre f(x + δ) ≈ f(x) + ∇f(x) · δ", "M05b"),
                     ("tableaux à plusieurs axes, formes, einsum", "M20")],
        "frontieres": ["21.R2", "21.Q3", "21.Q4", "21.Q5", "21.Q6", "21.Q7", "21.Q9", "21.Q11", "21.1", "21.2",
                       "21.3", "21.4", "21.5", "21.6", "21.8", "21.11", "21.12", "21.16", "21.17", "21.20", "21.26",
                       "21.29", "21.E2", "21.E3", "22.R1", "24.R2", "24.2", "24.3", "24.Q9"],
        "mymath": {"module": "convolution.py",
                   "functions": ["convolve", "toeplitz_matrix", "circular_convolve", "equivalent_kernel",
                                 "separable_factors"]},
        "reading_minutes": 160,
        "flashcards": 22,
        "notes": "Frontières : le ∂ 21.7 (rétropropager dans une convolution 1D : ∂L/∂w comme somme sur les positions, "
                 "∂L/∂b, ∂L/∂x par la convolution pleine du noyau retourné, les zéros dans g pour un pas, les "
                 "formules 2D à canaux), 21.R2 (un poids utilisé à plusieurs endroits), les quiz 21.Q3, 21.Q5, 21.Q6, "
                 "21.Q7, 21.Q9 et 21.Q11, 21.Q4 (le score maximal d'un filtre ±1, une forme linéaire sur un pavé), les ✏️ 21.1 à 21.6, 🧮 21.8 (VGG16), 📄 21.11 (LeNet-5), 21.17 (rayures), "
                 "21.20 (Conv1d contre Conv2d pleine largeur), 21.26 (MAC du pas contre le pooling), 21.29 (FGSM), "
                 "21.E2 et 21.E3, le rappel 22.R1 de workbookIA 22 (champs récepteurs d'une pile 1D et dilatations qui doublent), et, de workbookIA 24, qui n'a pas de chapitre de maths, 24.R2 (« same » de Keras "
                 "avec un pas), 24.2, 24.3 et 24.Q9. M21 enseigne les outils hors réseau : signaux échantillonnés "
                 "(un capteur, un son), grilles de mesures (températures, altitudes), polynômes et lois de dés, "
                 "jamais une image d'un dataset de workbookIA, une couche, un filtre appris ni une attaque. La "
                 "transposée de la matrice d'une convolution valide est celle de la convolution pleine par le noyau "
                 "retourné, et réciproquement (en mode même taille, seulement pour un noyau de longueur impaire) : "
                 "c'est énoncé, en convention mathématique et sur des signaux, sans gradient ni produit "
                 "vecteur-jacobienne (c'est le contenu de 21.7 Q3 en convention des bibliothèques), et démontré "
                 "seulement pour les matrices circulantes (∂ M21.13, où le noyau retourné est (h₀, h_{n−1}, …, h₁), "
                 "et non le simple renversement : une erreur classique) ; M21 n'écrit jamais "
                 "∂L/∂x ni ∂L/∂w d'une convolution, ni « un pas, ce sont des zéros dans g ». La formule des tailles "
                 "est démontrée comme un dénombrement (∂ M21.14, sous l'hypothèse n + 2p ≥ d(k − 1) + 1 que la "
                 "fenêtre tienne), avec « même taille » sans pas et avec un pas "
                 "(⌈n/s⌉ et un padding total réparti inégalement, la règle de 24.R2, sur d'autres nombres) ; le problème inverse de M21.6 ne demande pas « le plus petit et le plus grand p » qui donnent une taille (21.3 c-d) ; pour un noyau de longueur paire, le « même taille » de `np.convolve` (donc de `convolve`) et celui de PyTorch diffèrent d'un décalage (la case en trop n'est pas du même côté) : à dire dans la fiche, le 🔗 M21.17 et le 🐛 M21.27 ; la "
                 "taille d'une convolution transposée vient de l'insertion de zéros (avec le padding de sortie) et "
                 "une taille de sortie peut venir de deux tailles d'entrée ; le champ récepteur est démontré par "
                 "récurrence (∂ M21.15) et calculé sur d'autres piles que celles de 21.5 et de CP5.2 de workbookIA, "
                 "et la composition de deux convolutions est une convolution (M21.10, 🔨 M21.23), sans l'argument de "
                 "VGG en nombre de poids. Le coût (une multiplication-addition par poids et par position) et les "
                 "paramètres C_out(C_in/g · k_h k_w + 1) sont posés sur des filtrages de grilles de mesures, sans "
                 "réseau entier ni comparaison avec une couche dense. « Noyau séparable » veut dire ici de rang 1 ; dans workbookIA 21, « convolution séparable » veut dire par canal puis 1 × 1 (MobileNet) : un encadré ⚠️ le dit, et M21.Q6 ne mêle pas les deux sens. L'équivariance est enseignée hors réseau (règle, pochoir, signaux), sans reprendre la relance de 21.E1 (« le pooling, le pas et le padding la cassent en partie »). La transformée de Fourier n'est qu'un encadré 💻 (aucun chapitre ne l'enseigne) : le 🔬 M21.25 compare le direct et le séparable. M21.3 prend un autre signal que l'exemple de `convolve`. L'injectivité d'une convolution pleine n'est que "
                 "constatée sur un exemple (M21.4) : sa démonstration est l'un des sujets de CP5.8. Le §8 (une forme "
                 "linéaire sur une boule) est l'outil de FGSM, pris sur des erreurs de capteurs, sans gradient d'une "
                 "loss ni ε en k/255 ; la projection sur un pavé (`clamp`) est celle de M19. Évités (règle de "
                 "partage) : les suites (2, 0, 1, 3) et (1, 2), (1, 2, 3, 4) et (1, 0, −1), la grille X 5 × 5 de 21.2 "
                 "et le noyau de Sobel, le noyau de netteté (l'identité moins le laplacien) et le flou boîte 1/9, la "
                 "luminance (0,299 ; 0,587 ; 0,114), le détecteur de jaune (R + G − B) et le neurone cyan, le filtre "
                 "de rayure ±1 et son score 3, x = [[2, −1], [1, 3]] et le noyau 3 × 3 de 21.6, x = (1, 2, −1, 3) "
                 "avec w = (2, −1) ou (1, −1) (∂ 21.7 et CP5.12 de workbookIA), la hiérarchie 600 → 300 → 100, les "
                 "tailles 7 × 7 avec k = 3 et s = 2, 12 × 12 avec k = 5, 7 × 12, 28, 32 et 224, les champs récepteurs "
                 "3, 5, 7, 9, 11, 15, 35, 6 et 18 de leurs piles, les transposées 4 → 9, 7 → 14, 100 → 300 et 16 → "
                 "32, les cartes de recouvrements (k, s) = (3, 2) et (4, 2) de la fiche, VGG16, LeNet-5, MNIST, "
                 "Fashion-MNIST, CIFAR-10, le convnet de Keras, 300 → 175 et 256 → 64 canaux, 16 filtres 5 × 5 sur "
                 "8 canaux, Conv2d(3, 64, 3, s = 2, p = 1), 6 canaux et 4 filtres 3 × 3, 20 mots de 50 nombres, "
                 "ε = 0,03 sur 784 pixels. Conventions : la convolution des mathématiciens (noyau retourné, "
                 "`np.convolve`) et la somme glissante des bibliothèques (sans retournement, celle de workbookIA) "
                 "sont distinguées partout ; indices à partir de 0 ; une fenêtre est repérée par sa première case. "
                 "`convolution` (et non `conv`, le module de `mylearn`) : NumPy permis, sauf `np.convolve`, "
                 "`np.correlate`, `np.polymul`, `np.polynomial` et `np.fft`, et aucune fonction de SciPy "
                 "(`convolution_matrix` et `circulant` donneraient deux des fonctions) ; de `np.linalg`, seulement "
                 "`svd`, dans `separable_factors` ; aucune fonction de taille de sortie, de matrice "
                 "des fenêtres, de pooling, de convolution transposée ni de gradient. Pas de MML (le livre ne traite "
                 "pas la convolution), donc pas de 📖. 13,6 h au lieu des 10 h prévues : la fiche ajoute la matrice "
                 "creuse, le coût, « même taille » avec un pas, la taille d'une convolution transposée et la forme "
                 "linéaire sur une boule, que workbookIA 21 et 24 supposent.",
        "exercises": [
            ("M21.Q1", "🧠", 1, 4, "Convolution ou corrélation : retourner, glisser, sommer", "§1 §2", "E"),
            ("M21.Q2", "🧠", 1, 4, "Les propriétés de la convolution : vrai ou faux", "§1", "E"),
            ("M21.Q3", "🧠", 1, 4, "Lire une matrice de Toeplitz : diagonales, coefficients non nuls, nombre de lignes",
             "§3", "E"),
            ("M21.Q4", "🧠", 1, 4, "Équivariant, invariant, ou ni l'un ni l'autre ? Décalages, bords, pas et pooling",
             "§4", "E"),
            ("M21.Q5", "🧠", 1, 4, "Combien de positions ? Pas, dilatation, padding et insertion de zéros", "§5", "E"),
            ("M21.Q6", "🧠", 1, 4, "Canaux, groupes, convolution 1 × 1 et noyaux séparables : compter", "§6", "E"),
            ("M21.Q7", "🧠", 1, 4, "Composer des convolutions : noyau, pas et champ récepteur", "§7", "E"),
            ("M21.Q8", "🧠", 1, 4, "Le pire cas d'une perturbation bornée : quelle norme, quel vecteur ?", "§8", ""),
            ("M21.R1", "🔁", 1, 5, "La moyenne mobile d'une suite (R5)", "§1", "E"),
            ("M21.R2", "🔁", 1, 5, "La matrice d'une application linéaire, son noyau et son rang (M12a)", "§3", "E"),
            ("M21.R3", "🔁", 1, 5, "Le rang d'un produit extérieur u vᵀ et la décomposition en valeurs singulières "
             "(M12d)", "§6", ""),
            ("M21.1", "✏️", 1, 20, "Deux dés truqués et un produit de polynômes : la même convolution", "§1", "E"),
            ("M21.2", "✏️", 2, 20, "Convoluer et corréler un signal à la main, dans les trois modes", "§2", "E"),
            ("M21.3", "✏️", 2, 15, "Des pochoirs de différences finies : dérivée et dérivée seconde d'un signal "
             "échantillonné", "§2", "E"),
            ("M21.4", "✏️", 2, 20, "La matrice de Toeplitz d'une convolution pleine et d'une convolution valide : "
             "coefficients non nuls, rang et noyau", "§3", "E"),
            ("M21.5", "✏️", 2, 15, "Décaler puis filtrer, ou filtrer puis décaler : l'équivariance, ses bords et son "
             "pas", "§4", "E"),
            ("M21.6", "✏️", 2, 25, "Compter les positions d'une fenêtre : pas, dilatation, padding, « même taille » "
             "avec un pas, et le problème inverse", "§5", "E"),
            ("M21.7", "✏️", 2, 25, "Sous-échantillonner et insérer des zéros : la convolution transposée d'un signal "
             "et ses recouvrements", "§5", "E"),
            ("M21.8", "✏️", 2, 30, "Une carte de températures filtrée par un laplacien discret et par un lissage "
             "séparable", "§6", "E"),
            ("M21.9", "✏️", 2, 20, "Paramètres et coût d'un filtrage à plusieurs canaux : standard, groupé, par canal, "
             "1 × 1", "§6", "E"),
            ("M21.10", "✏️", 2, 20, "Le noyau équivalent de deux lissages successifs, et le champ récepteur d'une "
             "pile avec pas et dilatation", "§7", "E"),
            ("M21.11", "✏️", 1, 15, "Le pire cas d'une erreur de capteurs bornée : une forme linéaire sur les boules "
             "L∞ et L2", "§8", "E"),
            ("M21.12", "∂", 2, 25, "La convolution est commutative et associative ; la corrélation croisée ne l'est "
             "pas", "§1", ""),
            ("M21.13", "∂", 3, 30, "Les applications linéaires qui commutent avec le décalage circulaire sont les "
             "convolutions circulaires ; la transposée d'une matrice circulante", "§4", ""),
            ("M21.14", "∂", 2, 20, "Le nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 quand la fenêtre tient, par un "
             "dénombrement",
             "§5", "E"),
            ("M21.15", "∂", 2, 25, "Le champ récepteur d'une pile de convolutions : récurrence et forme close", "§7",
             ""),
            ("M21.16", "∂", 1, 10, "Le maximum d'une forme linéaire sur une boule L∞ vaut ε‖g‖₁, atteint en "
             "ε signe(g)", "§8", ""),
            ("M21.17", "🔗", 1, 25, "Pont : filtrer une grille à trois canaux comme les bibliothèques, formes "
             "(C, H, W), poids (C_out, C_in, k, k), et sans retournement", "§2 §6", "E"),
            ("M21.18", "🗣️", 1, 10, "Expliquer avec une règle graduée et un pochoir pourquoi une convolution est "
             "équivariante, mais pas invariante", "§4", "E"),
            ("M21.E1", "💼", 1, 10, "« Pourquoi une convolution est-elle une matrice de Toeplitz, et pourquoi ne la "
             "forme-t-on jamais ? »", "§3", ""),
            ("M21.19", "🔨", 2, 30, "La convolution de deux suites, dans les trois modes", "§1 §2", "E m:convolve"),
            ("M21.20", "🔨", 2, 25, "La matrice de Toeplitz d'une convolution", "§3", "E m:toeplitz_matrix"),
            ("M21.21", "🔨", 1, 20, "La convolution circulaire", "§4", "m:circular_convolve"),
            ("M21.22", "🔨", 2, 25, "Reconnaître un noyau séparable et le factoriser", "§6", "m:separable_factors"),
            ("M21.23", "🔨", 2, 30, "Le noyau équivalent et le pas d'une pile de sommes glissantes", "§7",
             "E m:equivalent_kernel p:M21.19"),
            ("M21.24", "🔮", 1, 15, "Prédire l'effet d'un décalage de l'entrée sur un filtrage avec pas, puis vérifier",
             "§4 §5", "E p:M21.19"),
            ("M21.25", "🔬", 2, 30, "Le coût d'un filtrage direct ou séparable, selon la taille du noyau : mesurer, puis "
             "comparer à k² et 2k", "§6", "p:M21.19"),
            ("M21.26", "🎨", 1, 15, "La carte des recouvrements d'une convolution transposée : un damier ou pas, selon "
             "k et s", "§5", "E"),
            ("M21.27", "🐛", 1, 25, "Chasse à l'erreur : un noyau non retourné, des recouvrements supposés réguliers, "
             "un noyau de rang 2 « séparé »", "§2 §5 §6", "E"),
            ("M21.28", "🛠️", 1, 20, "Un test de propriété : la matrice de Toeplitz fois x égale la convolution, pour "
             "des longueurs tirées au hasard", "§3", "p:M21.20"),
            ("M21.29", "🏆", 3, 25, "Défi : retrouver un noyau inconnu à partir d'un signal et de sa version filtrée "
             "bruitée, par les moindres carrés", "§3", "p:M21.20"),
        ],
    },
    {
        "id": "M22", "dir": "m22_recurrences", "hours": 15.6, "generation_sessions": 1, "mml": ["(§4.2)"],
        "summary": "Les récurrences vectorielles et les produits de matrices : une récurrence linéaire avec entrée, sa "
                   "solution par les puissances de la matrice et sa réponse impulsionnelle (la sortie est une "
                   "convolution de l'entrée) ; les puissances d'une matrice, ses valeurs propres complexes, la forme "
                   "exponentielle et les rotations ; le rayon spectral d'une matrice quelconque et la croissance "
                   "transitoire ; les normes induites, leur sous-multiplicativité et ρ ≤ ‖A‖ ; les produits de "
                   "matrices différentes et les facteurs dans [0, 1] ; les produits de jacobiennes le long d'une "
                   "trajectoire ; la sensibilité à un paramètre utilisé à chaque pas, une somme sur le temps ; et "
                   "borner un vecteur fait de plusieurs blocs. workbookIA 22 applique ces outils aux réseaux "
                   "récurrents et au gradient qui s'évanouit ou explose.",
        "objectives": [
            "Résoudre une récurrence linéaire vectorielle avec entrée, et lire sa réponse impulsionnelle comme une "
            "convolution.",
            "Calculer les puissances d'une matrice, ses valeurs propres complexes sous forme exponentielle, et "
            "reconnaître une rotation et une homothétie.",
            "Décider si Aᵗ tend vers 0 par le rayon spectral, et repérer une croissance transitoire.",
            "Calculer les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice, et majorer la norme d'un produit.",
            "Suivre un produit de facteurs dans [0, 1] et un produit de jacobiennes le long d'une trajectoire.",
            "Écrire la sensibilité de l'état final à un paramètre utilisé à chaque pas comme une somme sur le temps.",
            "Ramener sous un seuil un vecteur fait de plusieurs blocs sans changer sa direction.",
        ],
        "sections": [("§1", "Récurrences linéaires vectorielles avec entrée : solution et réponse impulsionnelle"),
                     ("§2", "Puissances d'une matrice : valeurs propres complexes, forme exponentielle et rotations"),
                     ("§3", "Le rayon spectral : Aᵗ → 0 si et seulement si ρ(A) < 1, et la croissance transitoire"),
                     ("§4", "Normes de matrices : normes induites, sous-multiplicativité et ρ ≤ ‖A‖"),
                     ("§5", "Produits de matrices différentes, et des facteurs dans [0, 1]"),
                     ("§6", "Récurrences non linéaires : des produits de jacobiennes le long d'une trajectoire"),
                     ("§7", "La sensibilité à un paramètre utilisé à chaque pas : une somme sur le temps"),
                     ("§8", "Borner un vecteur fait de plusieurs blocs")],
        "teaches": ["récurrence linéaire vectorielle avec entrée x_{t+1} = A x_t + B u_t : solution, réponse "
                    "impulsionnelle C Aᵏ B, sortie = convolution de l'entrée par la réponse impulsionnelle",
                    "puissances d'une matrice diagonalisable ; valeurs propres complexes d'une matrice réelle 2 × 2 : "
                    "rotation et homothétie",
                    "nombres complexes : forme exponentielle r e^{iθ} (formule d'Euler admise), produit = rotation et "
                    "homothétie, puissances (formule de Moivre)",
                    "rayon spectral d'une matrice quelconque ; Aᵗ → 0 si et seulement si ρ(A) < 1 (démontré pour une "
                    "matrice diagonalisable sur ℂ)",
                    "croissance transitoire d'une matrice non normale",
                    "normes induites ‖·‖₁ (colonnes), ‖·‖∞ (lignes) et ‖·‖₂ = s_max ; sous-multiplicativité ; "
                    "‖Aᵀ‖₂ = ‖A‖₂ ; ‖diag(d)‖ = max |dᵢ| ; ρ(A) ≤ ‖A‖ pour ces trois normes (par un vecteur propre de ℂⁿ) ; "
                    "formule de Gelfand (énoncée)",
                    "matrices orthogonales sous les puissances : normes conservées",
                    "produits de matrices différentes : ‖A_T ⋯ A_1‖ ≤ ‖A_T‖ ⋯ ‖A_1‖ ; produits de matrices "
                    "diagonales",
                    "récurrence affine diagonale à facteurs dans [0, 1] : ce qui reste après n étapes, "
                    "(1 − ε)ⁿ ≈ e^{−nε}, demi-vie",
                    "produits de facteurs aléatoires : moyenne géométrique et signe de E[ln a]",
                    "récurrence non linéaire : la jacobienne de x_T par rapport à x_t est un produit de jacobiennes ; "
                    "contraction et point fixe attractif",
                    "sensibilité de l'état final à un paramètre utilisé à chaque pas : elle suit une récurrence linéaire "
                    "avec entrée, dont la solution est une somme sur le temps ; somme tronquée",
                    "norme d'un vecteur fait de plusieurs blocs ; le projeter en entier sur une boule garde sa "
                    "direction, projeter chaque bloc non (rappel de M19)"],
        "requires": [("suites géométriques", "R5"), ("exponentielle et logarithme", "R6"),
                     ("loi des grands nombres", "M02c"), ("inégalité de Jensen", "M06"), ("normes de vecteurs", "M07"),
                     ("matrices orthogonales", "M12b"),
                     ("diagonalisation, valeurs propres, le strict minimum sur les nombres complexes", "M12c"),
                     ("valeurs singulières, normes de Frobenius et spectrale", "M12d"),
                     ("(1 + x/n)ⁿ → eˣ", "M14"), ("variances multipliées d'étage en étage", "M16"),
                     ("jacobienne, règle de la chaîne, longues compositions", "M17"),
                     ("somme sur les chemins d'un graphe de calcul", "M18"),
                     ("itérations linéaires et rayon spectral d'une matrice symétrique, récurrences d'ordre 2, "
                      "module d'un produit de complexes, projection sur une boule", "M19"),
                     ("produits de jacobiennes proches de l'identité, exponentielle de matrice", "M20"),
                     ("convolution de deux suites", "M21")],
        "frontieres": ["22.1", "22.2", "22.3", "22.4", "22.5", "22.8", "22.9", "22.11", "22.19", "22.24", "22.26",
                       "22.Q6", "22.Q7", "22.Q8", "22.Q9", "22.R2", "22.E2", "24.6", "19.19"],
        "mymath": {"module": "recurrence.py",
                   "functions": ["linear_system_states", "operator_norm", "product_norms"]},
        "reading_minutes": 160,
        "flashcards": 22,
        "notes": "Frontières : les ∂ 22.6 (le produit de dérivées de tanh, les bornes |w|^{T−t} et "
                 "σ_max(W_hh)^{T−t}, la somme ∂L/∂w, la tanh composée) et 22.7 (le chemin additif, diag(Π f), le "
                 "biais d'oubli, le GRU), 22.1 (fenêtres), 22.2 (dérouler une cellule), 22.3 (compter les poids), "
                 "22.4 (un pas de LSTM), 22.5 et 22.24 (température), 🧮 22.8, 🗣️ 22.9, 📄 22.11, 🔬 22.19, 📈 22.26, "
                 "les quiz 22.Q6 à 22.Q9, 22.R2 (le clipping de (3, 4)) et 22.E2, et, de workbookIA 24, le ∂ 24.6 (la max-norm par canal, w = (3, 4, 12), c = 3 : projeter chaque bloc). M22 enseigne les outils hors "
                 "réseau : populations par classes d'âge, réservoirs, placements, usure d'équipements, applications "
                 "du plan, jamais une cellule, une porte, une sigmoïde, une tanh composée ni une loss. Ce que "
                 "∂ 22.6.5 admet est démontré en général (∂ M22.11 : sous-multiplicativité, ‖Aᵀ‖₂ = ‖A‖₂, "
                 "‖diag(d)‖₂ = max |dᵢ|, ρ ≤ ‖A‖), sans diag(1 − h²) ni W_hh ; aucun exercice ne borne un produit de facteurs diag(dₖ) M avec |dₖ| ≤ 1, ni n'itère une application φ(M x + c) appliquée coordonnée par coordonnée (de jacobienne diag(φ′) M) : c'est la structure de ∂ 22.6.5 ; les jacobiennes de M22.8 viennent d'une application du plan d'une autre forme (Hénon, proie-prédateur). La récurrence affine diagonale (§5) "
                 "porte sur l'usure de trois équipements, avec (1 − ε)ⁿ ≈ e^{−nε} et la demi-vie (ni 0,9 ni 0,99 "
                 "comme facteurs, nombres de 26.7.4), sans porte, "
                 "sigmoïde, biais ni comparaison avec un « RNN simple » (∂ 22.7). La somme sur le temps (§7, "
                 "∂ M22.15) porte sur un capital placé à taux fixe et sur un modèle de pêche, sans δ_k ni "
                 "« dépendances lointaines » (∂ 22.6.6) : ∂ M22.15 démontre que la sensibilité suit une récurrence "
                 "avec entrée (le §1 donne alors la somme), et que les derniers pas dominent quand les produits "
                 "décroissent n'est que constaté sur les nombres de M22.9, jamais énoncé en général (c'est "
                 "l'explication que demande ∂ 22.6.6 ; précédent de M16.6) ; la somme tronquée aux K derniers pas est une remarque (la "
                 "BPTT tronquée de workbookIA 22 et l'état porté de workbookIA 24 restent à workbookIA). Les nombres "
                 "complexes : la forme exponentielle (formule d'Euler admise), le produit comme rotation et "
                 "homothétie, les puissances (Moivre), à la suite de M12c §3 et M19 §6 ; MB3 s'en servira. Le rayon "
                 "spectral d'une matrice non symétrique (M19 n'avait que le cas symétrique) : Aᵗ → 0 ⇔ ρ(A) < 1, "
                 "démontré pour une matrice diagonalisable sur ℂ (∂ M22.13) et admis en général, la croissance "
                 "transitoire d'une matrice non normale (M22.5, 🔮 M22.23, 🏆 M22.28), la formule de Gelfand "
                 "énoncée. Le §8 reprend la projection sur une boule de M19 (∂ M19.13) pour un vecteur fait de "
                 "plusieurs blocs : la norme globale, projeter le tout garde la direction, projeter chaque bloc non ; "
                 "sans `clip_grad_norm_`, gradient, constante 10⁻⁶, vecteur (3, 4) ni seuils 1 et 0,25. Évités "
                 "(règle de partage) : les puissances 0,7²⁰, 1,2²⁰, 0,95¹⁰⁰, 1,05¹⁰⁰, 0,9⁵⁰, 1,1⁵⁰, 1,5²⁰, 0,5¹⁹, "
                 "0,5¹⁰, 0,99¹⁰⁰, 0,9¹⁰⁰, 0,5²⁰, 0,73²⁰, 0,95⁵⁰ et 0,7311³⁰ et leurs valeurs (8 × 10⁻⁴, 38, 131, "
                 "0,006, 117, 0,0052, 3 325, 0,37, 2,7 × 10⁻⁵, 0,077, 10⁻⁷) ; σ(0) = 0,5 et σ(1) ≈ 0,73 comme "
                 "facteurs ; le facteur 10 tous les 4 pas, T = 80 et H = 32, les distances 10, 40 et 79 ; la cellule "
                 "tanh(0,7 x + 0,3 h), (u, w, b, v) = (1 ; 0,5 ; 0 ; 2) avec x = (2, 0, −1) ou (1, 1, 1), le point "
                 "fixe h = tanh(1 + 0,5 h) ; les poids du LSTM de 22.4 et de CP5.3 de workbookIA, c = 2 ou 3 ; les "
                 "logits (3 ; 1 ; 0,5), (1, 2, 3), (2, 1, 0) et (2 ; 2 ; 0) ; 69 poids, D = 50 et H = 20, (10, 8, 3) ; "
                 "les fenêtres de 22.1 ; la tanh composée et ses pentes 0,42, 0,25, 0,096 et 0,012 ; "
                 "l'initialisation orthogonale contre l'initialisation par défaut d'un réseau ; la boîte de pièces, "
                 "le carnet du comptable, la balle, Holmes, Verne, les taches solaires (et le modèle AR(2) de Yule, "
                 "qui porte sur elles), le sinus de période 24, « deux chats… ils ». ∂ M22.14 ne démontre que l'oubli du point de départ, ni l'existence du point fixe par "
                 "une suite de Cauchy, ni une contraction en norme max d'un maximum d'applications affines (les deux "
                 "moitiés de ∂ 26.8.3, Bellman, future frontière de M26). Le 🔬 M22.24 choisit des longueurs sans "
                 "débordement, ou renormalise le produit à chaque pas en cumulant le logarithme de la norme. "
                 "Conventions : colonnes "
                 "(x_{t+1} = A x_t + B u_t, comme MML et M19) ; le pont M22.16 passe à la convention ligne de "
                 "workbookIA (x A, de jacobienne Aᵀ). `recurrence` : NumPy permis, mais de `np.linalg` seulement `eigvalsh` (dans "
                 "`operator_norm`) et `norm` (dans `product_norms`), et aucune fonction de SciPy (`matrix_norm`, "
                 "`svdvals` et `scipy.linalg.norm` donneraient `operator_norm`) ; aucune fonction de cellule, de fenêtres, de température ni de clipping "
                 "(`clip_grad_norm` est dans le `mylearn` de workbookIA 19) ; pas de fonction de réponse "
                 "impulsionnelle (M22.2 la calcule à la main). MML : §4.2 relu (📖 M22.17 : la figure 4.4 et ses "
                 "cinq applications du plan, dont la rotation, que la définition 4.6 laisse sans valeur propre "
                 "réelle) ; MML ne traite ni les normes induites ni les produits de matrices. L'injectivité d'une "
                 "convolution pleine et la série I + A + A² + … quand ‖A‖ < 1 ne sont pas démontrées ici : ce sont "
                 "les sujets de CP5.8. 13,5 h au lieu des 10 h prévues : les normes induites et leurs propriétés, "
                 "que ∂ 22.6.5 admet, et le rayon spectral d'une matrice non symétrique, que le corrigé de workbookIA "
                 "22 suppose.",
        "exercises": [
            ("M22.Q1", "🧠", 1, 4, "La solution d'une récurrence avec entrée : quelles puissances, quels termes ?", "§1",
             "E"),
            ("M22.Q2", "🧠", 1, 4, "Valeurs propres complexes, module, forme exponentielle et rotation : vrai ou faux",
             "§2", "E"),
            ("M22.Q3", "🧠", 1, 4, "Le rayon spectral décide-t-il de tout ? Le long terme et les premiers pas", "§3",
             "E"),
            ("M22.Q4", "🧠", 1, 4, "Normes induites : laquelle se calcule à la main, laquelle borne quoi ?", "§4", "E"),
            ("M22.Q5", "🧠", 1, 4, "Un produit de facteurs dans [0, 1] : ce qui reste après n étapes", "§5", "E"),
            ("M22.Q6", "🧠", 1, 4, "Contraction et point fixe : lire une jacobienne", "§6", "E"),
            ("M22.Q7", "🧠", 1, 4, "Une somme sur le temps, sur un modèle de pêche chiffré : vrai ou faux", "§7", ""),
            ("M22.Q8", "🧠", 1, 4, "Ramener un vecteur sous un seuil : le tout ou chaque bloc ?", "§8", ""),
            ("M22.R1", "🔁", 1, 8, "La diagonalisation et les puissances d'une matrice (M12c)", "§2", "E"),
            ("M22.R2", "🔁", 1, 5, "Valeurs singulières et norme spectrale (M12d)", "§4", "E"),
            ("M22.R3", "🔁", 1, 5, "La règle de la chaîne comme produit de jacobiennes (M17)", "§6", "E"),
            ("M22.1", "✏️", 2, 25, "Une population à trois classes d'âge, avec des arrivées : trois pas à la main, et "
             "la solution écrite avec les puissances", "§1", "E"),
            ("M22.2", "✏️", 2, 25, "La réponse impulsionnelle de deux réservoirs en cascade, et la sortie comme "
             "convolution de l'entrée", "§1", "E"),
            ("M22.3", "✏️", 2, 20, "Une matrice de rotation et d'homothétie : valeurs propres complexes, forme "
             "exponentielle, puissances", "§2", "E"),
            ("M22.4", "✏️", 2, 20, "Le rayon spectral de trois matrices 2 × 2 non symétriques, et le comportement de "
             "leurs puissances", "§3", "E"),
            ("M22.5", "✏️", 2, 30, "Une matrice triangulaire de rayon spectral < 1 dont les puissances grandissent "
             "d'abord : Aᵗ en formule", "§3", "E"),
            ("M22.6", "✏️", 2, 25, "Les normes ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice 2 × 2, et trois majorations de "
             "‖A⁵x‖", "§4", "E"),
            ("M22.7", "✏️", 1, 15, "Trois équipements qui s'usent à des rythmes différents : une récurrence "
             "diagonale, ce qui reste, et la demi-vie", "§5", "E"),
            ("M22.8", "✏️", 2, 20, "Les jacobiennes d'une application du plan en trois points d'une trajectoire, et "
             "leur produit", "§6", "E"),
            ("M22.9", "✏️", 2, 25, "Un capital placé à taux fixe avec des versements : la dérivée du capital final "
             "par rapport au taux, une somme sur les années", "§7", "E"),
            ("M22.10", "✏️", 1, 15, "La norme globale de trois blocs, et deux façons de les ramener sous un seuil",
             "§8", "E"),
            ("M22.11", "∂", 2, 35, "Sous-multiplicativité, ‖Aᵀ‖₂ = ‖A‖₂, ‖diag(d)‖₂ = max |dᵢ| et ρ(A) ≤ ‖A‖",
             "§4", "E"),
            ("M22.12", "∂", 2, 20, "La norme induite ‖·‖∞ est le maximum des sommes de lignes", "§4", ""),
            ("M22.13", "∂", 2, 30, "Aᵗ → 0 si et seulement si ρ(A) < 1, pour une matrice diagonalisable sur ℂ", "§3",
             "E"),
            ("M22.14", "∂", 2, 20, "Une application contractante oublie son point de départ : l'écart entre deux "
             "trajectoires décroît géométriquement", "§6", ""),
            ("M22.15", "∂", 2, 25, "La sensibilité de l'état final à un paramètre utilisé à chaque pas suit une "
             "récurrence avec entrée : sa solution est une somme sur le temps", "§7", ""),
            ("M22.16", "🔗", 1, 20, "Pont : la convention ligne x_{t+1} = x_t A + u_t B, ses formes, et la jacobienne "
             "Aᵀ", "§1 §6", "E"),
            ("M22.17", "📖", 2, 40, "MML §4.2 relu : les cinq applications du plan de la figure 4.4, leurs valeurs "
             "propres, et le comportement de leurs puissances", "§2 §3", ""),
            ("M22.18", "🗣️", 1, 10, "Expliquer avec une image non mathématique pourquoi un système linéaire oublie "
             "son passé au rythme de ρ(A)", "§3", "E"),
            ("M22.E1", "💼", 1, 10, "« Quelle différence entre le rayon spectral et la norme d'une matrice ? »",
             "§3 §4", ""),
            ("M22.E2", "💼", 1, 10, "« Pourquoi Aⁿ peut-il grandir longtemps alors que toutes les valeurs propres de "
             "A sont de module < 1 ? »", "§3", ""),
            ("M22.19", "🔨", 1, 25, "Les états d'une récurrence linéaire avec entrée", "§1",
             "E m:linear_system_states"),
            ("M22.20", "🔨", 2, 30, "Les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂", "§4", "E m:operator_norm"),
            ("M22.21", "🔨", 1, 25, "Les normes des produits cumulés, et leur majoration", "§5 §6", "E m:product_norms"),
            ("M22.22", "📦", 1, 15, "`np.linalg.eigvals` et `np.linalg.norm` : rayon spectral et normes de matrices "
             "tirées au hasard, et ρ ≤ ‖A‖", "§3 §4", ""),
            ("M22.23", "🔮", 1, 20, "Prédire l'allure de ‖Aᵗ‖₂ pour une matrice non normale de rayon spectral 0,8, "
             "puis tracer", "§3", "E p:M22.20"),
            ("M22.24", "🔬", 2, 25, "Des produits de matrices aléatoires : le taux de croissance (1/n) ln ‖Aₙ ⋯ A₁‖",
             "§5", "p:M22.21"),
            ("M22.25", "🎨", 1, 20, "Les spirales d'une récurrence 2 × 2 à valeurs propres complexes, selon leur "
             "module", "§2", "E"),
            ("M22.26", "🐛", 1, 25, "Chasse à l'erreur : ρ(A) pris pour ‖A‖, un produit de jacobiennes dans le mauvais "
             "ordre, un seuil appliqué bloc par bloc", "§3 §6 §8", "E"),
            ("M22.27", "🛠️", 1, 30, "Un test de propriété : ‖AB‖ ≤ ‖A‖ ‖B‖ et ρ(A) ≤ ‖A‖ sur des matrices tirées au "
             "hasard", "§4", "p:M22.20"),
            ("M22.28", "🏆", 3, 25, "Défi : une matrice 3 × 3 à coefficients dans [−3, 3], de rayon spectral 0,85, dont "
             "une puissance a une norme ‖·‖₂ supérieure à 100", "§3", "p:M22.20"),
        ],
    },
    {
        "id": "CP5", "dir": "checkpoints/partie_5", "hours": 3.1, "generation_sessions": 1, "mml": [],
        "summary": "Le bilan de la partie V (M21 et M22), juste avant le checkpoint V de workbookIA : un examen blanc "
                   "d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), puis une "
                   "synthèse (carte mentale et fiche d'une page). Pas de mini-projet.",
        "objectives": [
            "Vérifier en temps limité que les notions de la partie V sont acquises.",
            "Construire ta propre synthèse de la partie V.",
        ],
        "sections": [("§1", "Examen blanc"), ("§2", "Synthèse")],
        "teaches": ["révision de la partie V"],
        "requires": [("toute la partie V", "M22")],
        "frontieres": ["21.R2", "21.Q3", "21.Q4", "21.Q5", "21.Q6", "21.Q7", "21.Q9", "21.Q11", "21.1", "21.2", "21.3", "21.4",
                       "21.5", "21.6", "21.7", "21.8", "21.11", "21.17", "21.20", "21.26", "21.29", "21.E2", "21.E3",
                       "22.1", "22.2", "22.3", "22.4", "22.5", "22.6", "22.7", "22.8", "22.9", "22.11", "22.19",
                       "22.24", "22.26", "22.Q6", "22.Q7", "22.Q8", "22.Q9", "22.R1", "22.R2", "22.E2", "24.R2",
                       "24.2", "24.3", "24.6", "24.Q9"],
        "reading_minutes": 15,
        "flashcards": 0,
        "notes": "Fichiers comme CP4 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, "
                 "03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md. Aucune question ne reprend"
                 " le checkpoint V de workbookIA (`checkpoints/partie_5/` de workbookIA : les formes de Conv2d, "
                 "MaxPool2d, LSTM et GRU de CP5.1, le CNN CIFAR-10 de CP5.2 (champ récepteur 18, 294 912 MAC, "
                 "24 234 paramètres), un pas de LSTM (CP5.3), les bugs de CP5.4, `rnn_forward` (CP5.5, graine 55), "
                 "l'early stopping (CP5.6), les courbes (CP5.7), le Fermi d'un générateur de mots (CP5.8), la "
                 "validation croisée et le gradient d'une couche dense (CP5.10), CP5.11 (168, 1 920, 32, 320 000) et "
                 "la ∂ de CP5.12, une rétropropagation dans une convolution 1D (x = (1 ; 2 ; −1 ; 3), w = (1, −1)), "
                 "frontière), qui se fait juste après, ni son mini-projet V (un classifieur CIFAR-10 : small_cnn, vgg, "
                 "resnet, FGSM à ε = k/255). La synthèse ne recopie pas le tableau des 22 formules de la synthèse de "
                 "workbookIA. CP5.8 donne le choix entre deux énoncés que M21 et M22 ne démontrent pas : une "
                 "convolution pleine par un noyau non nul est injective (par la matrice de Toeplitz ou par les "
                 "polynômes), ou, si ‖A‖ < 1 pour une norme induite, I − A est inversible, (I − A)⁻¹ = I + A + A² + … "
                 "et ‖(I − A)⁻¹‖ ≤ 1/(1 − ‖A‖) ; aucune ne touche à un gradient de convolution ni à un produit de "
                 "dérivées de tanh. CP5.10 relie les deux chapitres hors réseau : un filtre récursif à état de dimension 2 "
                 "(une récurrence avec entrée, pour que le rayon spectral ne soit pas un simple |a|), sa réponse "
                 "impulsionnelle, et un filtre à réponse finie (une convolution), jusqu'à la stabilité par le "
                 "rayon spectral ; pas de lissage exponentiel b = 1 − a avec correction du biais, ni β = 0,9, 0,95, "
                 "0,99 ou 0,999 (∂ 19.8 et ∂ 26.7 de workbookIA).",
        "exercises": [
            ("CP5.Q1", "🧠", 1, 10, "Dix affirmations sur la partie V : vrai ou faux", "§1", "E"),
            ("CP5.1", "✏️", 2, 10, "Convolution de deux suites, corrélation croisée et matrice de Toeplitz", "§1", "E"),
            ("CP5.2", "✏️", 2, 10, "Positions d'une fenêtre, pas, dilatation, et la convolution transposée d'un "
             "signal", "§1", "E"),
            ("CP5.3", "✏️", 2, 10, "Une grille filtrée par un noyau séparable : paramètres, coût et champ récepteur",
             "§1", "E"),
            ("CP5.4", "✏️", 2, 9, "Équivariance, matrice circulante et le pire cas d'une perturbation bornée", "§1",
             "E"),
            ("CP5.5", "✏️", 2, 10, "Une récurrence avec entrée : solution et réponse impulsionnelle", "§1", "E"),
            ("CP5.6", "✏️", 2, 10, "Valeurs propres complexes, rayon spectral, normes et croissance transitoire", "§1",
             "E"),
            ("CP5.7", "✏️", 2, 9, "Produits de jacobiennes le long d'une trajectoire, et sensibilité à un paramètre "
             "utilisé à chaque pas", "§1", "E"),
            ("CP5.8", "∂", 3, 12, "Une démonstration au choix : une convolution pleine est injective, ou la série "
             "I + A + A² + … quand ‖A‖ < 1", "§1", "E"),
            ("CP5.9", "🐛", 2, 8, "Corriger une copie : cinq erreurs", "§1", "E f:02"),
            ("CP5.10", "🔗", 2, 14, "Problème de synthèse : un filtre récursif et un filtre à réponse finie, du signal "
             "à la stabilité", "§1", "E"),
            ("CP5.11", "🗣️", 1, 60, "Ta carte mentale et ta fiche d'une page", "§2", "E"),
        ],
    },
]
