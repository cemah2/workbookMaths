"""Syllabus, part VII (before the bonus chapters B2 to B8 of workbookIA): detailed in session 69 (MB2, MB3, MB4, MB5,
MB6, MB8; no mock exam).

Format: tools/syllabus.py. Exercise tuple: (id, type, stars, minutes, title, covers, flags);
flags: E (essential track), c:wbm|pytest|manuel, f:02|03, p:prerequisites, m:mymath functions written.

Sharing rule (BIBLE §8, §24): every proof (∂) of the workbookIA chapter a math chapter prepares is a frontier
(tools/syllabus.py adds them); ``frontieres`` lists further workbookIA exercises not to solve nor paraphrase. A math
chapter teaches the tool in another setting and may state a result whose proof workbookIA asks. As in parts IV to VI,
the math chapters work outside the networks: shops, sensors, weather, tournaments, surveys, signals, queues, menus;
never a tokenizer, a Transformer, a language model, a diffusion model, an explainer of a network nor a trained agent.
workbookIA B1 and B7 have no math chapter (their notions are taught before; B7 states Little's law and admits it).
The mymath modules of part VII never take the name of a mylearn module (ranks.py, not retrieval.py; gaussian_paths.py,
not diffusion.py). The notes of each chapter list the data of workbookIA to avoid.
"""

CHAPTERS = [
    {
        "id": "MB2", "dir": "mb2_cooccurrences", "hours": 13.2, "generation_sessions": 1, "mml": [],
        "summary": "Les outils mathématiques des embeddings construits par comptage, hors de tout texte : l'écriture d'un "
                   "entier en base 2 et en base 16 (une lacune) ; l'information mutuelle ponctuelle (PMI) des cases d'une "
                   "table jointe, son signe, sa borne, la PPMI, et l'information mutuelle de M06 comme sa moyenne ; le "
                   "lissage d'une marge, une loi tempérée (rappel de M28), et ce qu'il fait à la PMI de chaque colonne ; "
                   "la SVD tronquée d'une table non centrée (rappel de M12d) et la répartition des valeurs singulières "
                   "entre deux facteurs, qui fixe le produit mais pas les angles ; le modèle logistique d'une paire, le "
                   "logit d'un taux et le décalage de ln K quand on sous-échantillonne une classe (formule de Bayes) ; la "
                   "géométrie des voisins et des analogies (cosinus, parallélogramme, et la borne qui explique "
                   "l'exclusion des points de la question) ; retirer une direction d'un nuage ; la moyenne masquée et le "
                   "coût des comparaisons par paires. Les cadres sont des oiseaux, des magasins, des publicités, des "
                   "aliments, des mesures d'animaux et des capteurs de sol. workbookIA B2 applique ces outils aux "
                   "tokenizers, à la PPMI suivie d'une SVD, à word2vec et aux embeddings de phrases.",
        "objectives": [
            "Écrire un entier en base 2 et en base 16, lire un octet et une couleur, découper un mot de bits en champs, et "
            "compter les bits qu'il faut pour N valeurs.",
            "Calculer la PMI des cases d'une table jointe, la lire comme le logarithme d'un lift, en tirer la PPMI, et "
            "retrouver l'information mutuelle comme la moyenne des PMI.",
            "Démontrer la borne PMI(x, y) ≤ min(−ln p(x), −ln p(y)) et expliquer pourquoi les événements rares ont les PMI "
            "extrêmes et les plus bruitées.",
            "Lisser une marge par une puissance, la reconnaître comme une loi tempérée, et prévoir le décalage de la PMI "
            "de chaque colonne.",
            "Répartir les valeurs singulières d'une SVD tronquée entre deux facteurs, et démontrer ce qui dépend de ce "
            "choix (les angles entre lignes) et ce qui n'en dépend pas (le produit).",
            "Calculer le logit de vraisemblance maximale d'un taux, et corriger par ln K un sous-échantillonnage d'une "
            "classe (formule de Bayes).",
            "Mesurer le parallélogramme d'une analogie et expliquer, par une borne sur le cosinus, pourquoi on exclut les "
            "points de la question.",
            "Retirer d'un nuage une direction estimée, et dire quelles distances changent et lesquelles restent.",
            "Résumer des suites de vecteurs de longueurs différentes par une moyenne masquée, et comparer le coût des "
            "comparaisons par paires à celui d'un vecteur par élément.",
        ],
        "sections": [("§1", "Bases 2 et 16 : écrire un entier, lire un octet, découper un mot de bits"),
                     ("§2", "La PMI d'une table jointe : signe, −∞, PPMI, borne des événements rares, et l'information "
                            "mutuelle comme moyenne"),
                     ("§3", "Lisser une marge : une loi tempérée, et ce qu'elle fait à la PMI de chaque colonne"),
                     ("§4", "La SVD tronquée d'une table non centrée : répartir les valeurs singulières entre deux "
                            "facteurs"),
                     ("§5", "Le modèle logistique d'une paire : le logit d'un taux, et le décalage de ln K quand on "
                            "sous-échantillonne une classe"),
                     ("§6", "Voisins et analogies : cosinus, produit scalaire et parallélogramme"),
                     ("§7", "Retirer une direction : la projection sur le complément, et ce qui reste"),
                     ("§8", "D'éléments à des ensembles : la moyenne masquée et le coût des comparaisons par paires")],
        "teaches": ["numération en base 2 et en base 16 : divisions successives, groupes de 4 bits, un octet en deux "
                    "chiffres hexadécimaux, une couleur #RRGGBB, un mot de bits découpé en champs (lacune : workbookIA B2 "
                    "s'en sert pour UTF-8) ; ⌈log₂ N⌉ bits pour N valeurs (rappel de R6 §4 et M06 §7)",
                    "information mutuelle ponctuelle d'une table jointe, PMI(x, y) = ln p(x, y)/(p(x)p(y)) = "
                    "ln P(y | x)/P(y) : signe, −∞ sur une case vide, logarithme du lift d'une règle « x ⇒ y », "
                    "PPMI = max(0, PMI) ; une colonne indépendante des lignes a des PMI nulles",
                    "l'information mutuelle (M06) est la moyenne des PMI sous la loi jointe : positive, bien que des PMI "
                    "soient négatives",
                    "borne PMI(x, y) ≤ min(−ln p(x), −ln p(y)), atteinte quand x n'arrive qu'avec y : les événements rares "
                    "ont les PMI les plus grandes possibles ; PMI normalisée PMI/(−ln p(x, y)) ≤ 1 (démontré)",
                    "estimer une PMI sur un échantillon : une case rare donne une estimation très dispersée, parfois −∞ "
                    "(constaté par l'expérience)",
                    "lisser une marge : p_α(y) ∝ n(y)^α avec 0 < α < 1, la loi tempérée de température 1/α (rappel de "
                    "M28) ; elle remonte les colonnes rares et décale la PMI de chaque colonne de −ln(p_α(y)/p(y)), une "
                    "constante par colonne ; lissée sur ses seules colonnes, une table symétrique ne l'est plus",
                    "SVD tronquée d'une table non centrée (rappels de M12d : SVD compacte, Eckart-Young) ; répartir les "
                    "valeurs singulières : M_k = (U_k S_k^β)(V_k S_k^{1−β})ᵀ pour tout β ∈ [0, 1] ; le produit ne dépend "
                    "pas de β, les produits scalaires et les cosinus entre lignes du premier facteur en dépendent en "
                    "général ; β = 1 garde ceux "
                    "des lignes de M_k, β = 0 ceux des lignes de U_k (démontré ; la non-unicité de toute factorisation de "
                    "rang k est en MB4)",
                    "ne pas centrer une grande table creuse avant sa SVD tronquée : centrer la rend pleine (mémoire, coût), "
                    "et la SVD non centrée approche la table elle-même",
                    "le modèle logistique d'une paire : σ(s) est la probabilité qu'une paire soit une vraie paire plutôt "
                    "qu'une paire tirée au hasard ; le logit de vraisemblance maximale d'un taux observé (a succès, b "
                    "échecs) est ln(a/b), le logit de la proportion (rappel de M13a, sur des comptes)",
                    "sous-échantillonner une classe (étude cas-témoins) : garder les positifs avec la probabilité s₁ et "
                    "les négatifs avec s₀ multiplie la cote par s₁/s₀ (formule de Bayes) ; dans un modèle logistique, "
                    "seule l'ordonnée à l'origine bouge, de ln(s₁/s₀) (démontré) ; le résultat de Levy et Goldberg est "
                    "énoncé en une phrase dans la fiche, démontré dans workbookIA B2",
                    "voisins : cosinus et normalisation, ‖a − b‖² = 2 − 2 cos(a, b) pour des vecteurs unitaires, donc le "
                    "même classement (rappel de M07), produit scalaire contre cosinus (les vecteurs longs l'emportent)",
                    "analogie et parallélogramme : requête q = b − a + c, défaut ‖(b − a) − (d − c)‖ ; si "
                    "‖b − a‖ ≤ ε‖c‖ avec ε < 1, alors cos(q, c) ≥ √(1 − ε²) (démontré dans la fiche) : c a avec q un "
                    "cosinus proche de 1 et reste en haut de la liste, d'où l'exclusion de a, b et c",
                    "retirer une direction : x − (x·u/u·u)u, la projection sur le complément de la droite (rappels de M07 "
                    "et M12b) ; une direction estimée comme premier axe de différences (M12d, par la matrice de Gram de "
                    "M28) ; Pythagore : seule la composante de la différence sur u disparaît ; retirer (1, …, 1), c'est "
                    "centrer chaque vecteur (M20)",
                    "moyenne masquée Σ m_t h_t / Σ m_t d'une suite de vecteurs complétée par des zéros : invariance par "
                    "le remplissage ; coût des comparaisons par paires, C(n, 2) (R8), contre un vecteur par élément et un "
                    "produit matriciel",
                    "une table de vecteurs lue par une ligne one-hot (rappel de M09a, une ligne)"],
        "requires": [("division euclidienne et reste (`//`, `%`)", "R0"),
                     ("puissances de 2 et de 10, moyenne pondérée", "R1"),
                     ("notations Σ", "R4"),
                     ("logarithmes ln et log₂, bits et nats, sigmoïde et σ(−x) = 1 − σ(x), cote et logit", "R6"),
                     ("combinaisons C(n, 2), simulation avec une graine", "R8"),
                     ("loi des grands nombres, erreur type d'une proportion", "M02c"),
                     ("probabilités jointes et marginales, tableau de contingence, indépendance, loi conditionnelle", "M03"),
                     ("formule de Bayes", "M04"),
                     ("entropie, information mutuelle d'un tableau (`info.mutual_information`)", "M06"),
                     ("produit scalaire, normes, similarité cosinus, Cauchy-Schwarz, projection sur une droite", "M07"),
                     ("produit matriciel, transposée, une ligne one-hot fois une matrice", "M09a"),
                     ("rang d'une matrice", "M12a"),
                     ("complément orthogonal, projection orthogonale, matrices orthogonales", "M12b"),
                     ("valeurs et vecteurs propres d'une matrice symétrique (théorème spectral), trace", "M12c"),
                     ("SVD compacte, approximation de rang faible (Eckart-Young), axes principaux", "M12d"),
                     ("maximum de vraisemblance de Bernoulli, régression logistique (le score est la log-cote)", "M13a"),
                     ("réductions le long d'un axe, diffusion, centrage comme projection", "M20"),
                     ("matrice de Gram d'une famille de vecteurs, température sur des probabilités (`temper`)", "M28")],
        "frontieres": ["B2.1", "B2.2", "B2.5", "B2.6", "B2.9", "B2.11", "B2.22", "B2.23", "B2.24", "B2.25", "B2.28",
                       "B2.Q7", "B2.Q9", "B2.Q10", "B2.Q11", "B2.Q12", "B2.E4"],
        "mymath": {"module": "cooccurrence.py",
                   "functions": ["pmi", "case_control_logit", "remove_direction"]},
        "reading_minutes": 135,
        "flashcards": 16,
        "notes": "Frontières : le ∂ B2.7 (les dérivées de −ln σ(±s) et σ′ = σ(1 − σ), les gradients par rapport à u_c, "
                 "u_{n_k} et v_w, les lignes touchées, l'application chiffrée, la collision n₁ = c, l'optimum "
                 "PMI − log K annulant ℓ′(x) avec les comptes #(w, c) et K #(w)#(c)/N, le lien avec la régression "
                 "logistique), ✏️ B2.1 (« Noël à Paris » en UTF-8 : points de code, octets, motifs, NFD), ✏️ B2.2 "
                 "(l'analogie roi − homme + femme : requête, cosinus, plus proche avec et sans exclusion, produit "
                 "scalaire, normalisation), ✏️ B2.5 (one-hot fois la table, gradient de la table, SGD, `padding_idx`, "
                 "weight decay), ✏️ B2.6 (cooccurrences d'une séquence par une fenêtre, PMI, PPMI lissée, symétrie "
                 "perdue), 🧮 B2.9 (poids d'une table d'embedding), ⚖️ B2.11 (taxe des langues, biais des embeddings, "
                 "direction de genre, neutralisation, tri de CV), 🔨 B2.22 et B2.23 (`cooccurrence_matrix`, `ppmi`, "
                 "`cosine_similarity_matrix`, `most_similar`), 📦 B2.24 (PPMI puis SVD sur Holmes, U_d S_d^{1/2} "
                 "normalisé, voisins), 📦 B2.25 (word2vec en PyTorch : sous-échantillonnage, loi des négatifs), 📦 B2.28 "
                 "(mean pooling avec masque et recherche sémantique), les quiz B2.Q7 (score de WordPiece), B2.Q9 "
                 "(`nn.Embedding`), B2.Q10 (hypothèse distributionnelle, signe et valeur d'une PMI), B2.Q11 (moyenne "
                 "masquée de trois vecteurs), B2.Q12 (cosinus et distance de vecteurs unitaires, produit scalaire contre "
                 "cosinus) et l'entretien B2.E4. MB2 enseigne les outils hors du texte : oiseaux et milieux, magasins et "
                 "produits, publicités et clics, aliments et nutriments, mesures d'animaux, capteurs de sol ; jamais un "
                 "mot, un token, un tokenizer, un corpus, une fenêtre glissante sur une séquence, une table d'embedding de "
                 "modèle, un genre, une capitale, un CV ni un modèle de langue. "
                 "§1 (lacune de workbookIA B2, qui convertit en hexadécimal et découpe des bits sans l'enseigner ; R6 n'a "
                 "que les bits et M05a.8 le binaire d'un flottant, hors parcours essentiel) : divisions successives (R0), "
                 "groupes de 4 bits, un octet en deux chiffres hexadécimaux, une couleur #RRGGBB, ⌈log₂ N⌉ bits pour N "
                 "(un rappel de R6 §4 et M06 §7, erratum de la session 71 : ce n'est pas une lacune) "
                 "valeurs, un mot de 16 bits découpé en champs (4 + 12) ; ni UTF-8, ni point de code, ni motif "
                 "110xxxxx, ni 0x10FFFF (✏️ B2.1, que workbookIA garde). "
                 "§2 : la PMI d'une table jointe donnée (ou d'une table de contingence divisée par son total, M03), jamais "
                 "d'une matrice construite par une fenêtre sur une séquence (✏️ B2.6, `cooccurrence_matrix`) ; la PPMI "
                 "est définie et calculée à la main, jamais en code (c'est `ppmi` de `mylearn`) ; l'information "
                 "mutuelle comme moyenne des PMI est un rappel de M06 (`info.mutual_information`) ; la borne et la PMI "
                 "normalisée sont démontrées (∂ MB2.8) ; aucun quiz ne demande si une PMI négative signifie « moins "
                 "souvent que l'indépendance » ni la PMI nulle de quatre comptes (B2.Q10 b et c), et la fiche ne nomme pas "
                 "le score de WordPiece, la PMI sans le total (B2.Q7). ✏️ MB2.2 : 100 oiseaux, "
                 "trois milieux (forêt 40, prairie 35, village 25) et quatre espèces (huppe 1, pic 8, grive 27, moineau "
                 "64), table [[0, 6, 14, 20], [1, 2, 10, 22], [0, 0, 3, 22]] : PMI(forêt, pic) = ln 1,875 ≈ 0,629 "
                 "(lift 1,875), PMI(village, grive) = ln(4/9) ≈ −0,811, −∞ sur trois cases, PMI(prairie, huppe) = "
                 "ln(100/35) ≈ 1,050 = −ln p(prairie), la plus grande de la table pour un seul oiseau (la borne est "
                 "atteinte), cinq cases de PPMI positive, I(X ; Y) ≈ 0,0759 nat. "
                 "§3 : le lissage d'une marge est `temper(p, 1/α)` de M28, appliqué aux colonnes ; ✏️ MB2.3 lisse les "
                 "espèces de la table de MB2.2 avec α = 1/3 (racines cubiques exactes de 1, 8, 27 et 64 : la loi "
                 "(0,1 ; 0,2 ; 0,3 ; 0,4)) ; chaque colonne décale ses PMI d'une constante (−ln 10 pour la huppe, "
                 "+ln 1,6 pour le moineau) ; PMI_α(prairie, huppe) ≈ −1,253, le record de la table devenu négatif ; dans "
                 "la forêt, le classement pic, grive, moineau devient moineau, grive, pic, alors que l'ordre des milieux "
                 "dans une colonne ne change jamais ; la table est rectangulaire, la symétrie perdue d'une table carrée "
                 "n'est dite que dans la fiche (une phrase), et aucun quiz ni exercice ne la demande (B2.6 g), ni ne "
                 "demande si une PMI négative d'une colonne fréquente devient positive (B2.6 h) ; jamais α = 0,75, ni la "
                 "loi des négatifs, ni les comptes 100 et 1. Le 🔮 MB2.15 tire 400 observations de la loi de cette table, "
                 "plusieurs centaines de fois : la PMI estimée de (prairie, huppe) est très dispersée (et vaut parfois "
                 "−∞), celle de (village, moineau) non ; le lissage décale la cible, sans réduire la dispersion "
                 "(erratum de la session 71 : la note disait « réduit » ; la huppe n'étant vue qu'en prairie, "
                 "l'estimation de (prairie, huppe) ne dépend que du nombre d'oiseaux de prairie et varie peu, et le "
                 "lissage l'en fait dépendre davantage ; le 🔮 suit aussi (prairie, pic), la case rare dispersée). "
                 "§4 : la SVD est un rappel de M12d (`svd`, `low_rank_approximation`, sa convention de signe) ; aucune "
                 "fonction de `mymath` ne rend U_k S_k^β (le cœur de `ppmi_svd_24`, 📦 B2.24) ; l'exposant de "
                 "répartition s'appelle β (p est une probabilité dans ce chapitre ; la fiche dit que workbookIA B2 le "
                 "note p) et le rang k, comme M12d. ✏️ MB2.4 : quatre magasins × trois produits, M = [[50, 8, 26], "
                 "[5, 44, 8], [88, 40, 49], [34, 40, 22]] de SVD donnée (colonnes de U : (2, 1, 4, 2)/5 et "
                 "(−2, 4, −1, 2)/5 ; de V : (7, 4, 4)/9 et (−4, 8, −1)/9 ; valeurs singulières 135 et 45 ; erratum de "
                 "la session 71 : ces bases sont des permutations signées de celles de M12b, que la liste des évités "
                 "exclut ; la génération prend M = [[12, 96, 220], [78, 54, 5], [57, 114, 190], [132, 144, 140]], U : "
                 "(4, 1, 4, 4)/7 et (−4, 4, −1, 4)/7, V : (6, 10, 15)/19 et (15, 6, −10)/19, valeurs singulières 399 et "
                 "133, aux mêmes cosinus ; la troncature "
                 "et Eckart-Young sont le rappel MB2.R2, sur une autre matrice), une case vérifiée, facteurs pour "
                 "β = 0, ½ et 1 et leur produit, cos(magasin 1, magasin 4) = 0, puis 0,5, puis 0,8 "
                 "(égal au cosinus des lignes de M pour β = 1), cos(magasin 1, magasin 2) de −0,514 à 0,316 ; aucune "
                 "normalisation des lignes ni recherche de voisins. ∂ MB2.9 démontre le cas général (et, pour une "
                 "matrice symétrique semi-définie positive, que β = ½ donne deux facteurs égaux) ; la non-unicité de toute "
                 "factorisation de rang k (deux factorisations diffèrent d'une matrice inversible) est démontrée en MB4, "
                 "pas ici. Ne pas centrer une "
                 "table creuse : Q4 et 💼 MB2.E1. Le 🎨 MB2.16 trace les lignes de U₂S₂^β d'une table plus grande de "
                 "magasins, créée à la génération. "
                 "§5 : le logit de vraisemblance maximale d'un taux observé, ln(a/b) pour a succès et b échecs, est un "
                 "rappel de M13a, sur des comptes ; ∂ MB2.10 démontre le décalage par la formule de Bayes, jamais en "
                 "minimisant une loss −a ln σ(x) − b ln σ(−x) ; aucun exercice ni la fiche n'écrivent cette loss avec des "
                 "poids réels, ni ne multiplient le poids d'une classe par K ; cadres : publicités et clics, études "
                 "cas-témoins ; garder les positifs avec la probabilité s₁ et les négatifs avec s₀ multiplie la cote par "
                 "s₁/s₀, et dans un modèle logistique seule l'ordonnée à l'origine bouge, de ln(s₁/s₀) ; le résultat de "
                 "Levy et Goldberg est énoncé une fois dans la fiche, en une phrase avec un renvoi à workbookIA B2, comme "
                 "le fait sa fiche, jamais dérivé ni demandé par un quiz : aucun exercice ne pose a = #(w, c) et "
                 "b = K #(w)#(c)/N, ne tire des négatifs selon une loi marginale, n'écrit u_c ou v_w, ne dérive la loss "
                 "de l'échantillonnage négatif, ni ne relie ses termes aux entrées, labels et poids d'une régression "
                 "logistique (∂ B2.7.2 à 7). ✏️ MB2.5 : 3 200 affichages, 50 clics ; logit ln(50/3 150) = −ln 63 ≈ "
                 "−4,143 ; un non-clic gardé sur 9 : ln(50/350) = ln(1/7) ≈ −1,946, soit +ln 9, probabilité lue 1/8 au "
                 "lieu de 1/64 ; la correction par ln 9 ; aucune repondération des négatifs (c'est l'énoncé de ∂ B2.7.6). "
                 "§6 : la fiche rappelle le cosinus, ‖a − b‖² = 2 − 2 cos (M07, sans les nombres de B2.Q12) et le "
                 "produit scalaire contre le cosinus, puis démontre la borne cos(q, c) ≥ √(1 − ε²) ; ✏️ MB2.6 (aliments "
                 "en (protéines, glucides, lipides) pour 100 g : yaourt nature (4, 5, 3) et sucré (4, 10, 3), fromage "
                 "blanc nature (8, 4, 3) et sucré (7, 9, 3)) mesure le parallélogramme : q = (8, 9, 3), défaut δ = 1, "
                 "ε ≈ 0,530 et borne ≈ 0,848 pour c, cos(q, c) ≈ 0,931 ; la borne de la fiche appliquée à d, "
                 "√(1 − δ²/‖d‖²) = √(138/139) ≈ 0,9964 (4 décimales : 0,996 est un nombre évité), garantit que d l'emporte sur c sans calculer cos(q, d) "
                 "(≈ 0,998) ; alignement des "
                 "décalages ≈ 0,981 ; puis la crème (2, 3, 30), où ε ≈ 0,165 et la borne ≈ 0,986 est presque atteinte "
                 "(0,987) ; il ne classe pas une liste de candidats avec et sans exclusion, ne cherche pas le gagnant du "
                 "produit scalaire et ne normalise pas d'abord les vecteurs (B2.2 d à g). "
                 "§7 : `remove_direction` retire une direction donnée ; la direction est estimée comme premier axe de "
                 "différences (à la main : deux différences de même norme ont pour premier axe leur somme, par la "
                 "matrice de Gram 2 × 2) ; ✏️ MB2.7 : mesures d'animaux en logarithme, différences (2, 4, 3) et "
                 "(4, 2, 3), premier axe (1, 1, 1)/√3 (retirer la taille revient à centrer, M20), trois animaux (2, 3, 4), "
                 "(3,5 ; 4,5 ; 5,5) et (5, 3, 4) : les deux premiers se confondent, la distance du premier au troisième "
                 "passe de 3 à √6 ; la fiche dit ce que retirer une direction ne fait pas (une information portée par "
                 "d'autres directions corrélées reste), sans biais social, paires de genre, CV ni règlement (⚖️ B2.11). "
                 "§8 : moyenne masquée de relevés de capteurs de sol (température, humidité ; les stations météo sont celles "
                 "de M20), complétés par des zéros ; "
                 "ni token, ni `[PAD]`, ni les h_t de B2.Q11 ; le coût des paires compare C(n, 2) comparaisons à n "
                 "résumés et un produit matriciel, sans SBERT ni 10 000 phrases. "
                 "Le 🐛 MB2.17 n'a aucune erreur du corrigé de 🔨 B2.22 (lissage sur les lignes, log₂), de 🔨 B2.23 "
                 "(`eps`) ni de 🐛 B2.18 ; le 🛠️ MB2.18 ne teste pas « une table produit donne des PMI nulles » (la "
                 "propriété documentée de `ppmi`) ; le 🏆 MB2.19 se vérifie sur trois tables cachées tirées à "
                 "nouveau à chaque exécution, avec des cases rares de grande PMI qui piègent l'estimation directe, et un "
                 "rayon et une tranche dominants dont la case commune, fréquente sans être associée, piège les cinq cases "
                 "les plus vendues (apprenant simulé, session 71), et laisse la méthode libre (pseudo-comptes de "
                 "M04, lissage, seuil sur les comptes) ; la règle de score et le seuil sont calés à la génération. "
                 "Évités (règle de partage) : de la fiche de workbookIA B2, « Les chatons s'endorment paisiblement. » "
                 "(37, 7, 11, 2,75, 1,2), Holmes et Verne (88 caractères, 7 819 et 8 793 mots, 105 849, 562 000, "
                 "13,5 %), « ç » U+00E7 = 231 = C3 A7, « 🙂 » F0 9F 99 82, « € » E2 82 AC, « Ça coûte 15 € » (13 points "
                 "de code, 17 octets), 0x10FFFF, « chat » × 5, « chats » × 2, « chaton » × 3, « rat » × 4, « raton » × 2, "
                 "50 257 = 256 + 50 000 + 1, la Déclaration universelle, 32 768/1,12, « thé » et « café », « le vieux "
                 "phare éclaire la côte », la matrice chien/chat/os [[0, 4, 1], [4, 0, 1], [1, 1, 2]] (N = 14, sommes "
                 "5, 5, 4 ; PMI 0,807, −0,357, 0,560 ; lissée 0,351, 0,297, 0,823), le skip-gram chiffré (d = 3, K = 2, "
                 "(0,5 ; −1 ; 2), (1 ; 0 ; 0,5), (0 ; 1 ; 0), (−1 ; 0,5 ; 1), scores 1,5, −1 et 1, L ≈ 1,828), « éclaire », "
                 "« fromage », « lundi », les comptes 100 et 1 (0,990/0,010 → 0,969/0,031, 100^0,75 ≈ 31,6), K de 5 à "
                 "20 et de 2 à 5, t ≈ 10⁻⁵ et 10⁻³, 1 % jeté 97 fois sur 100 (0,968), α = 0,75, GloVe "
                 "f(X) = min(1, (X/100)^{3/4}), l'analogie France/Paris/Italie/Rome/Milan/Lyon ((0,1 ; 1 ; 0), "
                 "(1 ; 1 ; 0,1), (0,1 ; 0 ; 1), (1 ; 0,1 ; 1), (0,6 ; 0 ; 1), (0,6 ; 1 ; 0), requête (1 ; 0 ; 1,1), "
                 "0,996, 0,981, 0,803, 0,527, 0,346, 0,067) et Madrid/Espagne, « father », « three », Bolukbasi (300 "
                 "dimensions, dix paires), « glace », SBERT (10 000 phrases, 5 s contre 65 h, 50 millions de passes), "
                 "MiniLM (384, 6 couches, 256 tokens, 30 522 × 384 = 11 720 448), e5, Qwen3, la requête « I can't log in "
                 "to my account » (0,502, 0,293, 0,042) ; des exercices de workbookIA B2 : Q7 (20, 40, 100 et 30, 300, "
                 "200 ; 0,005 et 0,0005), Q9 ((8, 20), 1 000 × 64, 5 000 × 32 = 160 000, un token lu 3 fois), Q10 "
                 "(1 000, 6, 30, 200, PMI nulle), Q11 ((1, 2), (3, 0), (2, 4), (0, 0), masque (1, 1, 1, 0), 2,0 et 1,5), "
                 "Q12 (cos 0,8 → 0,4, √2 ≈ 1,414, (3, 4) et (−6, −8)), R3 ((1/2, 1/4, 1/8, 1/8), 1,75 bit), ✏️ B2.1 "
                 "(« Noël à Paris », 12, 14, 0xC3 0xAB = 195, 171, 16 ; « œ » C5 93 = 197, 147 ; « Δ = b² − 4ac »), "
                 "✏️ B2.2 (roi (0,6 ; 1 ; 0,9), reine (0,8 ; −0,5 ; 0,9), homme (0,1 ; 1 ; 0,9), femme (0,1 ; −1 ; 0,9), "
                 "prince (0,7 ; 0,8 ; 0,2), princesse (0,7 ; −0,6 ; 0,2), trône (3 ; 0 ; 0,5), q = (0,6 ; −1 ; 0,9), "
                 "1,79, 0,932, 0,941, 2,25, 0,900, 0,866), ✏️ B2.3 et B2.4 (« été », « étés », « pré », « prés » ; "
                 "« chanter » et ses huit fusions), ✏️ B2.5 (E = [[1, 0, 2], [0, 1, −1], [2, −1, 0], [−1, 3, 1], "
                 "[0, 2, 2]], (3, 0, 3, 1), w = (1 ; −2 ; 0,5), −13,5, η = 0,1), ✏️ B2.6 (« le chat court le chat le rat "
                 "court », C = [[0, 1, 3, 0], [1, 0, 1, 1], [3, 1, 0, 1], [0, 1, 1, 0]], N = 14, 0,742, −0,069, 0,330, "
                 "0,821, 0,765, 0,279 ; fenêtre 2 : 26, 0,396), ∂ B2.7 (v_w = (2 ; −1), u_c = (1 ; 1), u_n1 = "
                 "(0,5 ; 0,5), u_n2 = (−1 ; 2), scores 1, 0,5 et −4, L ≈ 1,3055, η = 0,5, K = 5 → −0,868), 🧮 B2.8 "
                 "(90 000 mots, 250 par page, fertilités 1,3 et 1,6, 8 192, 300), 🧮 B2.9 (50 257 × 768, 128 256 × "
                 "4 096, 2 048, 32 000), 🔬 B2.20 (tailles 300, 500, 1 000, 2 000, 4 000, 8 000 ; bits par token 6,124, "
                 "7,499, 8,298, 8,715, 8,857, 8,843 ; octets par token 1,422, 2,045, 2,560, 3,001, 3,382, 3,641 ; bits "
                 "par octet 4,306 à 2,429), les exemples des stubs et du notebook de B2.22 et B2.23 ([0, 1, 2, 1], "
                 "[[0, 2, 1], [2, 0, 3], [1, 3, 0]] et ses PPMI 0,47, 0,5878, 0,5218, 0,3941, 0,5838, 0,6396, "
                 "[0, 0, 0, 1], [[0, 2, 1, 0], [2, 0, 3, 0], [1, 3, 0, 0], [0, 0, 0, 0]], [[1, 0], [1, 1], [0, 0]] et "
                 "0,7071, [[1, 0], [0, 1], [1, 1], [−1, 0], [2 ; 0,1]] et 0,9988, `eps` 0,5 et 2, [[3, 4]] et [[6, 8]], "
                 "0,943 et 0,866, 120 lignes dont 40 copies, `default_rng(23)`), 📦 B2.24 (4 000 mots, fenêtre 2, "
                 "d = 100, 0,80, 0,73), 📦 B2.25 (1 590 mots, t = 10⁻³, K = 5, batch de 512, 6 ln 2 ≈ 4,159, rang médian "
                 "9,5), 📈 B2.27 (0,14, −0,23, 48 sur 100), 📦 B2.28 (1 055 passages de 120 mots), 🔬 B2.29, 🏆 B2.31 "
                 "(2 000 tokens), 💼 B2.E5 (200 000 documents, 5 millions de passages × 384 × 4 octets ≈ 7,7 Go) ; de "
                 "workbookIA B1 (cosinus et prototypes) : (1, 0, 0), (4, 2, 2), (2, 1, 0), "
                 "(0, 1, 1), q = (2, 1, 1), « pomme » (0,9 ; 0,1) et (0,7 ; 0,3), « poire » (0,2 ; 0,8) et "
                 "(0,4 ; 0,8), q = (0,6 ; 0,5), 0,900 et 0,869, les cosinus 0,31, 0,27, 0,22 avec s = 100 et 1, "
                 "(3, 0, 4), (0, 3, 4), (16, 2, 8), (2, 1, 2), (1, 2, 2), 0,24, 0,30, 0,28, 0,19, 4,60517, 2,6592, "
                 "η = 10⁻³, γ = 0,3, λ = 0,2, θ₀ = −0,4 ; et, de ce dépôt, les bases orthonormées de M12b "
                 "((2, 2, 1)/3, (1, −2, 2)/3, (−2, 1, 2)/3, (2, 3, 6)/7, (6, 2, −3)/7, (3, −6, 2)/7, (4, 4, 7)/9, "
                 "(1, −8, 4)/9, (1, 2, 2, 4)/5), les exemples de `mutual_information` et de `conditional_entropy` (M06), "
                 "de `temper` (M28 : (0,5 ; 0,25 ; 0,25 ; 0) à T = 1/3 et 3) et les températures de workbookIA 28 que "
                 "M28 évite (0,5 ; 0,7 ; 1,2 ; 1,5 ; 2), le logit de 0,55 et σ(1,6) de M13a ; ajoutés par la relecture de "
                 "la session 71 : de workbookIA, le rôle des octets UTF-8 (0x7F, 0x80, 0xC0), le ∂ B2.7.4 au complet "
                 "(gradients (−0,538 ; 0,269), (1,245 ; −0,622), (0,036 ; −0,018), (0,024 ; 0,078), u_n1 → "
                 "(−0,122 ; 0,811)), les cosinus 0,816, 1, 0,913, 0,577 et les normes 0,781 et 0,825 de la fiche de B1, "
                 "les cosinus de B2.29 et de sa variante (0,847/0,749, 0,824/0,803, 0,885/0,838, 0,878/0,849, "
                 "0,892/0,827, 0,945/0,909) ; de ce dépôt, le tableau 2 × 2 de M06 §8 (100 clients, 30/10/10/50, "
                 "(0,4 ; 0,6), 0,256 bit, 0,971 → 0,715), l'ornithologue et les six espèces de M28 §5 (le merle, la "
                 "mésange), les stations météo de M20 (4, 7, 24) et M20.1 (12, 28, 24), R6.Q3 (1 000 000 → 20), "
                 "M06.Q7.5 (300 issues) et M06 §7 (20 issues → 5) ; le cadre du taux de clic de M04.3, M08.9 et M13a §1 "
                 "est gardé pour ✏️ MB2.5 (titre figé, autres nombres, BIBLE §24) ; la fiche ne reprend ni la "
                 "table des oiseaux, ni la table des magasins, ni les aliments des ✏️, ni les exemples du stub. "
                 "Conventions : logarithme népérien partout (PMI et logits en nats), sauf les bits du §1 ; une table "
                 "jointe a les valeurs de X en lignes (M03, M06) ; les points sont les lignes d'une matrice (M13b, M28) ; "
                 "rang k et exposant β pour les facteurs de la SVD ; a et b sont des nombres d'exemples au §5, s₁ et s₀ des "
                 "taux de sélection, 𝐚, 𝐛, 𝐜, 𝐝 "
                 "des vecteurs (en gras) au §6. `cooccurrence` : NumPy et `math` seulement, aucune SciPy "
                 "(`scipy.special.logit`, `xlogy`, `scipy.optimize`) ni scikit-learn (`mutual_info_score`, "
                 "`LogisticRegression`), qui servent d'oracles aux tests ; `pmi` prend une table jointe de probabilités "
                 "(somme 1), rend des nats et −∞ sur les cases nulles, sans max(0, ·), sans lissage, sans comptes ni "
                 "`alpha` : un autre contrat que `ppmi(C, alpha)` de workbookIA B2 ; `case_control_logit` prend les "
                 "nombres d'exemples d'un échantillon (nombres ou tableaux, diffusés) et deux taux de sélection dans "
                 "]0, 1], et rend ln(n₁/n₀) − ln(s₁/s₀) ; sa docstring passe par la formule de Bayes, sans la forme en σ, "
                 "sans comptes « attendus » ni poids multiplié par K, et jamais avec des comptes #(w, c), #(w), #(c), N ; "
                 "`remove_direction` retire une direction donnée, sans l'estimer ; aucune fonction de SVD ni de "
                 "facteurs U S^β, d'analogie (`most_similar` avec ses exclusions résoudrait ✏️ B2.2), de cosinus entre "
                 "lignes (`cosine_similarity_matrix`), de matrice de cooccurrences ni de moyenne masquée (`embed_28`). "
                 "Pas de MML : le livre ne traite ni la PMI ni les embeddings, et Eckart-Young a été lu en M12d (§4.6) ; "
                 "pas de 📖. COMPOSITION : 10 h au plan (8 h avant la session 69), 10,6 h avec la lacune des bases et des "
                 "durées réalistes (les chapitres de la partie VI ont dépassé leurs estimations de 20 à 40 %) ; 6 quiz, "
                 "3 rappels, 7 ✏️ et 3 ∂, un 🔗, deux 🔨 et aucun 📦 (les comparaisons avec SciPy et scikit-learn sont "
                 "dans les tests, la SVD par bibliothèque est en M12d), un 🔮 et aucun 🔬 (le temps), 🐛, 🎨, 🗣️, 💼, "
                 "🛠️, 🏆, 16 flashcards ; lecture 125 min (≈ 9 000 mots au rythme des fiches de la partie VI). Durées revues "
                 "à la génération (session 71), après la re-résolution à l'aveugle, l'auteur des exercices et l'apprenant "
                 "simulé : lecture 135 min (≈ 9 800 mots), exercices 623 min (papier 348, notebook 275), 13,2 h en tout "
                 "et 9,8 h en parcours essentiel. Parcours "
                 "essentiel : ∂ MB2.9, le 💼, le 🔮, le 🎨, le 🛠️ et le 🏆 hors parcours ; les ∂ de la borne (MB2.8) et "
                 "du sous-échantillonnage (MB2.10) y sont. Corrections de la relecture (session 69) : R1-1 (la voie de "
                 "Bayes, `case_control_logit`), R1-4, R1-7, R1-11, R1-14.",
        "exercises": [
            ("MB2.Q1", "🧠", 1, 4, "Bases 2 et 16 : le nombre de chiffres d'un entier, la valeur d'un octet, les bits qu'il "
             "faut pour N valeurs", "§1", "E"),
            ("MB2.Q2", "🧠", 1, 6, "La PMI d'une case : son signe, −∞, la PPMI, la borne des événements rares, et "
             "l'information mutuelle qui en est la moyenne", "§2", "E"),
            ("MB2.Q3", "🧠", 1, 5, "Lisser une marge : quelles colonnes gagnent, de combien bouge la PMI d'une colonne, et "
             "quels classements le lissage garde", "§3", "E"),
            ("MB2.Q4", "🧠", 1, 6, "Répartir les valeurs singulières entre deux facteurs : ce qui dépend de β, ce qui n'en "
             "dépend pas, et pourquoi ne pas centrer une table creuse", "§4", "E"),
            ("MB2.Q5", "🧠", 1, 4, "Le logit d'un taux et le sous-échantillonnage : ce qui bouge (l'ordonnée à "
             "l'origine), de combien, dans quel sens", "§5", "E"),
            ("MB2.Q6", "🧠", 1, 5, "Analogies, direction retirée et moyenne masquée : vrai ou faux, avec une raison",
             "§6 §7 §8", "E"),
            ("MB2.R1", "🔁", 1, 8, "L'information mutuelle d'un tableau 2 × 2 (M06)", "§2", "E"),
            ("MB2.R2", "🔁", 1, 8, "La meilleure approximation de rang 1 d'une matrice et son erreur (Eckart-Young, M12d)",
             "§4", "E"),
            ("MB2.R3", "🔁", 1, 7, "Cosinus, projection sur une droite et prototype d'une classe (M07, workbookIA B1)",
             "§6 §7", "E"),
            ("MB2.1", "✏️", 1, 20, "Des entiers en base 2 et en base 16 : conversions, une couleur #RRGGBB, les bits pour "
             "5 000 codes, et un mot de 16 bits découpé en deux champs", "§1", "E"),
            ("MB2.2", "✏️", 2, 30, "Cent oiseaux, trois milieux, quatre espèces : la PMI des cases, le lift d'une règle, "
             "la PPMI, l'espèce vue une seule fois, et l'information mutuelle comme moyenne", "§2", "E"),
            ("MB2.3", "✏️", 2, 25, "Lisser la marge des espèces de la même table (α = 1/3) : la loi lissée, le décalage "
             "de la PMI de chaque colonne, et le classement des espèces d'un milieu avant et après", "§3", "E p:MB2.2"),
            ("MB2.4", "✏️", 2, 35, "Quatre magasins, trois produits, une table de rang 2 de SVD donnée : les facteurs "
             "U S^β et V S^{1−β} pour β = 0, ½ et 1, leur produit, et le cosinus de deux magasins", "§4", "E"),
            ("MB2.5", "✏️", 2, 20, "Une bannière affichée 3 200 fois et cliquée 50 fois : le logit de vraisemblance "
             "maximale, puis un non-clic gardé sur 9, le décalage de ln 9 et sa correction", "§5", "E"),
            ("MB2.6", "✏️", 2, 25, "Yaourt et fromage blanc, nature et sucrés : mesurer le parallélogramme d'une analogie "
             "(défaut, rapport ε, borne du cosinus), et dire si d peut l'emporter sur c", "§6", "E"),
            ("MB2.7", "✏️", 2, 25, "Des mesures d'animaux en logarithme : la direction de taille estimée sur deux "
             "différences, la retirer de trois animaux, et les distances qui restent", "§7", "E"),
            ("MB2.8", "∂", 2, 20, "La PMI est majorée par −ln p(x) et par −ln p(y), avec égalité quand x n'arrive qu'avec "
             "y ; la PMI normalisée est donc au plus 1", "§2", "E"),
            ("MB2.9", "∂", 3, 30, "Répartir les valeurs singulières entre deux facteurs : le produit ne dépend pas de β, "
             "les produits scalaires des lignes si", "§4", ""),
            ("MB2.10", "∂", 2, 25, "Sous-échantillonner une classe : par la formule de Bayes, la cote observée est celle "
             "de la population multipliée par le rapport des taux de sélection s₁/s₀ ; dans un modèle logistique, seule "
             "l'ordonnée à l'origine bouge, de ln(s₁/s₀)", "§5", "E"),
            ("MB2.11", "🔗", 1, 15, "Pont : résumer des séries de relevés de longueurs différentes par une moyenne "
             "masquée, montrer que le remplissage ne change rien, et compter les comparaisons par paires", "§8", "E"),
            ("MB2.12", "🗣️", 1, 15, "Expliquer à un ornithologue ce que mesure la PMI d'un milieu et d'une espèce, et "
             "pourquoi une espèce vue une seule fois a la plus grande", "§2 §3", "E"),
            ("MB2.E1", "💼", 1, 10, "« Pourquoi ne centre-t-on pas une grande table de comptages creuse avant de la "
             "factoriser par une SVD tronquée ? »", "§4", ""),
            ("MB2.13", "🔨", 1, 35, "La table des PMI d'une loi jointe, −∞ sur les cases vides", "§2",
             "E m:pmi"),
            ("MB2.14", "🔨", 2, 45, "Deux briques : le logit d'une population estimé sur un échantillon cas-témoins, et "
             "retirer une direction des lignes d'une matrice", "§5 §7", "E m:case_control_logit,remove_direction"),
            ("MB2.15", "🔮", 2, 35, "Prédire puis mesurer la dispersion de la PMI estimée sur 400 observations, pour une "
             "case rare et une case fréquente, avec et sans lissage", "§2 §3", ""),
            ("MB2.16", "🎨", 1, 40, "Des magasins dans le plan des deux facteurs U₂S₂^β, pour β = 0, ½ et 1 : ce qui "
             "s'étire, et les angles qui changent", "§4", ""),
            ("MB2.17", "🐛", 1, 30, "Chasse à l'erreur : une PMI calculée sans le total, des facteurs U S^β et V S^β, une "
             "direction retirée sans diviser par u·u", "§2 §4 §7", "E"),
            ("MB2.18", "🛠️", 1, 40, "Un test de propriété de `pmi` sur des tables tirées au hasard : la borne, la "
             "transposition, et la moyenne qui redonne l'information mutuelle de M06", "§2", "p:MB2.13"),
            ("MB2.19", "🏆", 3, 50, "Défi : retrouver, sur 3 000 observations, les cinq paires les plus associées d'une "
             "table cachée de 10 × 10, sans se laisser piéger par les cases rares", "§2 §3", "p:MB2.13"),
        ],
    },
    {
        "id": "MB3", "dir": "mb3_rotations_attention", "hours": 14.8, "generation_sessions": 1, "mml": ["§3.9"],
        "summary": "Les rotations et les moyennes pondérées dont se sert le Transformer de workbookIA B3, travaillées hors "
                   "réseau. D'abord les formules d'addition, démontrées par le produit scalaire de deux vecteurs unitaires "
                   "(M22 et M25a les tiraient d'une règle admise), et ce qu'elles disent des rotations du plan : R_α R_β = R_{α+β}, "
                   "l'inverse est la transposée, les longueurs et les angles sont conservés, et la multiplication par "
                   "e^{iθ} ; puis les rotations de l'espace et de ℝⁿ (les rotations de Givens de MML §3.9), les matrices "
                   "diagonales par blocs et ce qu'une permutation des coordonnées en change. Ensuite l'encodage d'une "
                   "variable cyclique (une direction, un jour de l'année) par des horloges (cos, sin) : un décalage est "
                   "une rotation, et le produit scalaire de deux encodages ne dépend que de l'écart. Enfin la moyenne "
                   "pondérée par une softmax : une combinaison convexe, l'estimateur à noyau de Nadaraya-Watson et sa "
                   "largeur de bande, les masques comme un conditionnement, l'équivariance par permutation, l'échelle des "
                   "scores (la division par √n et la saturation), la softmax en ligne avec son invariant et la fusion de "
                   "deux états, et le coût quadratique de toutes les paires. workbookIA B3 applique ces outils à "
                   "l'attention, à ses masques, aux encodages de position, à RoPE et à FlashAttention.",
        "objectives": [
            "Démontrer les formules d'addition du cosinus et du sinus, et s'en servir pour des valeurs exactes, des "
            "duplications et des produits de cosinus.",
            "Composer et inverser des rotations du plan (R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}), et les lire comme des "
            "multiplications par e^{iθ}.",
            "Écrire une rotation de Givens de ℝⁿ, dire quand deux rotations commutent, et lire une matrice diagonale par "
            "blocs de rotations et ce qu'une permutation des coordonnées en change.",
            "Encoder une variable cyclique par (cos, sin), lire un décalage comme une rotation, et exprimer le produit "
            "scalaire de deux encodages à plusieurs horloges en fonction de l'écart.",
            "Calculer une moyenne pondérée par une softmax et l'estimateur de Nadaraya-Watson, et prévoir l'effet de la "
            "largeur de bande.",
            "Restreindre une moyenne pondérée à un sous-ensemble par un masque (une loi conditionnelle), et démontrer "
            "qu'une moyenne pondérée sur un ensemble est équivariante par permutation.",
            "Expliquer pourquoi l'on divise par √n une somme de n contributions indépendantes, et mesurer la saturation "
            "d'une softmax quand l'échelle des scores grandit.",
            "Calculer une softmax en ligne par blocs, démontrer son invariant, fusionner deux états partiels, et compter "
            "ce que coûtent toutes les paires.",
        ],
        "sections": [("§1", "Les formules d'addition, démontrées : le cosinus d'une différence par le produit scalaire, "
                            "puis les autres"),
                     ("§2", "Les rotations du plan : composer, inverser, conserver ; la multiplication par e^{iθ}"),
                     ("§3", "Les rotations de ℝⁿ : l'espace, les rotations de Givens, les matrices diagonales par blocs et "
                            "les permutations des coordonnées"),
                     ("§4", "Encoder une variable cyclique : des horloges (cos, sin), et un décalage est une rotation"),
                     ("§5", "Une moyenne pondérée par une softmax : combinaison convexe, estimateur de Nadaraya-Watson et "
                            "largeur de bande"),
                     ("§6", "Masques et permutations : conditionner sur un sous-ensemble, ne regarder que le passé, "
                            "l'équivariance par permutation"),
                     ("§7", "L'échelle des scores : diviser une somme de n contributions par √n, et la saturation de la "
                            "softmax"),
                     ("§8", "La softmax en ligne : l'état (m, l, a), son invariant, et la fusion de deux états"),
                     ("§9", "Le coût quadratique (rappel de MB2 §8) : la mémoire de toutes les paires, et calculer par "
                            "blocs")],
        "teaches": ["formules d'addition cos(a ± b) et sin(a ± b), démontrées : le cosinus d'une différence par le produit "
                    "scalaire de deux vecteurs unitaires (R9), les autres par la parité et cos(π/2 − x) = sin x ; "
                    "duplication ; produit de deux cosinus en somme, cos a cos b = ½[cos(a − b) + cos(a + b)] (M28 §4 s'en "
                    "servait, tiré des formules de soustraction de M25a) ; la règle "
                    "e^{iα}e^{iβ} = e^{i(α+β)}, que M22 admettait, en découle",
                    "rotations du plan : R_θ (MML §3.9.1) ; R_α R_β = R_{α+β} (les formules d'addition écrites en "
                    "matrices), donc deux rotations du plan commutent ; R_θ⁻¹ = R_θᵀ = R_{−θ}, det R_θ = 1 ; une rotation "
                    "conserve les normes, les produits scalaires, les distances et les angles (MML §3.9.4) ; une matrice "
                    "orthogonale 2 × 2 de déterminant 1 est une rotation, de déterminant −1 une symétrie ; la "
                    "multiplication par e^{iθ} (rappel de M22) et Re(z̄w) = le produit scalaire des deux vecteurs",
                    "rotations de l'espace autour des trois axes (MML §3.9.2) et rotations de Givens R_ij(θ) de ℝⁿ (MML "
                    "§3.9.3) ; non commutatives dès la dimension 3, sauf dans des plans disjoints ; une matrice "
                    "diagonale par blocs de rotations planes tourne chaque plan de son angle ; produit par blocs (généralise M09a §3, Σ colonne × ligne) : des "
                    "blocs de colonnes fois des blocs de lignes donnent une somme de produits ; conjuguer par une matrice "
                    "de permutation, PᵀRP, donne la même rotation dans d'autres plans de coordonnées",
                    "encodage d'une variable cyclique (une direction, un jour de l'année) par (cos ωt, sin ωt) : deux "
                    "valeurs proches sur le cercle restent proches, ‖e(t) − e(t′)‖² = 2 − 2 cos ω(t − t′) ; un décalage "
                    "de t est une rotation de l'encodage, la même pour tout t ; plusieurs horloges de périodes "
                    "différentes : le produit scalaire de deux encodages vaut Σ_k cos ω_k(t − t′), une fonction du seul "
                    "écart ; une horloge seule ne distingue pas t de t plus sa période ; direction moyenne (l'argument de "
                    "la moyenne des vecteurs unitaires)",
                    "moyenne pondérée par une softmax de scores : une combinaison convexe (dans l'enveloppe convexe, "
                    "M10), inchangée quand on ajoute une même constante à tous les scores ; poids exponentiels (M14) et "
                    "loi de Boltzmann (M17)",
                    "estimateur à noyau de Nadaraya-Watson ŷ(x) = Σᵢ K(x, xᵢ) yᵢ / Σⱼ K(x, xⱼ) ; avec un noyau gaussien, "
                    "une softmax des scores −‖x − xᵢ‖²/(2h²) ; la largeur de bande h comme une température (h → 0 : le "
                    "plus proche voisin, h → ∞ : la moyenne des yᵢ) ; à normes égales, une softmax des produits scalaires "
                    "x·xᵢ/h²",
                    "masques : un score −∞ avant la softmax restreint la loi à un sous-ensemble et la renormalise (une loi "
                    "conditionnelle, rappel de M03 et M28) ; mettre un poids à 0 après la softmax ne donne pas une loi ; "
                    "un masque triangulaire ne regarde que le passé (filtrer plutôt que lisser) et laisse T(T + 1)/2 cases ; "
                    "un sous-ensemble vide n'a pas de loi (0/0) ; la moyenne exponentielle normalisée est une softmax, "
                    "sur le passé, de scores linéaires en le temps",
                    "équivariance par permutation : une moyenne pondérée sur un ensemble, dont chaque score ne dépend que "
                    "de la paire, commute avec toute renumérotation (matrice de permutation P, M16) ; softmax(Ps) = "
                    "P softmax(s) ; un masque triangulaire, ou un score qui dépend du rang, la casse ; l'équivariance par "
                    "translation de M21 est celle d'un autre groupe",
                    "échelle des scores : une somme de n contributions indépendantes centrées de variance v a pour "
                    "écart-type √(nv) (rappels de M02b, et de la variance d'un produit de M16) ; la diviser par √n garde "
                    "une échelle fixe ; multiplier les scores par c, c'est diviser la température par c (M17, M28) ; "
                    "saturation : quand c grandit, la softmax tend vers le one-hot du plus grand score, et la sensibilité "
                    "1 − Σ pᵢ² (la trace de diag(p) − ppᵀ, l'impureté de Gini de M13a) tend vers 0, exponentiellement vite "
                    "en c (énoncé, avec une idée de preuve)",
                    "softmax en ligne : lire les scores par blocs en gardant l'état (m, l, a), le plus grand score lu, "
                    "Σ e^{s_j − m} et Σ e^{s_j − m} v_j, remis à l'échelle par e^{m_ancien − m_nouveau} quand le maximum "
                    "change ; l'invariant, démontré par récurrence : le résultat est exact, et m + ln l est le log-sum-exp "
                    "(M05a) ; aucune exponentielle d'un nombre positif ; la fusion de deux états, associative et "
                    "commutative, d'élément neutre (−∞, 0, 0) : couper le calcul entre plusieurs machines ; pour un ordre "
                    "au hasard, le maximum change en moyenne H_N − 1 fois sur N blocs (les records, R8 et M02b)",
                    "coût quadratique : le coût des comparaisons par paires est un rappel de MB2 §8, en une ligne ; neuf : "
                    "la mémoire d'une matrice n × n contre celle d'un calcul par blocs de B lignes (n·B), pour la même "
                    "quantité de calcul ; doubler n multiplie cette mémoire par 4 (une pente 2 en échelles logarithmiques, "
                    "R6)"],
        "requires": [("Σ, sommes doubles, raisonnement par récurrence", "R4"),
                     ("suites géométriques, moyenne exponentielle (lissage)", "R5"),
                     ("exponentielle et logarithme, échelles logarithmiques", "R6"),
                     ("probabilités d'issues équiprobables", "R8"),
                     ("cercle trigonométrique, radians, cos et sin, cos² + sin² = 1, parité et périodicité, produit "
                      "scalaire et angle de deux vecteurs", "R9"),
                     ("intégrale de 1/x : comparer une somme à une intégrale", "M02a"),
                     ("linéarité de l'espérance, variance d'une somme de variables indépendantes, loi normale", "M02b"),
                     ("loi conditionnelle", "M03"),
                     ("log-sum-exp et softmax stables, overflow et underflow", "M05a"),
                     ("produit scalaire, normes, angle, développement de ‖a − b‖², barycentre", "M07"),
                     ("validation croisée : principe", "M08"),
                     ("somme harmonique comparée à l'intégrale de 1/x", "M11"),
                     ("produit matriciel, transposée, (AB)ᵀ = BᵀAᵀ", "M09a"),
                     ("enveloppe convexe", "M10"),
                     ("matrice d'une composition, changement de base", "M12a"),
                     ("matrices orthogonales : normes et produits scalaires conservés", "M12b"),
                     ("matrice de rotation du plan, déterminant, le strict minimum sur les nombres complexes", "M12c"),
                     ("impureté de Gini 1 − Σ p_k²", "M13a"),
                     ("poids exponentiels et renormalisation", "M14"),
                     ("matrice de permutation (renuméroter des nœuds, P A Pᵀ), variance d'un produit de variables "
                      "indépendantes et d'une somme de produits décorrélés", "M16"),
                     ("loi de Boltzmann et ses limites en température, la matrice diag(p) − ppᵀ", "M17"),
                     ("tableaux à plusieurs axes, réductions le long d'un axe, diffusion", "M20"),
                     ("équivariance par translation", "M21"),
                     ("forme exponentielle r e^{iθ}, produit = rotation et homothétie, e^{iα}e^{iβ} = e^{i(α+β)} et "
                      "R_α R_β = R_{α+β} admises", "M22"),
                     ("formules de soustraction tirées de l'exponentielle complexe, matrices par blocs", "M25a"),
                     ("température sur des probabilités, top-k et top-p comme lois conditionnelles", "M28"),
                     ("coût des comparaisons par paires, C(n, 2), contre un vecteur par élément", "MB2")],
        "frontieres": ["B3.1", "B3.2", "B3.3", "B3.4", "B3.5", "B3.8", "B3.12", "B3.13", "B3.14", "B3.15", "B3.17",
                       "B3.27", "B3.29", "B3.Q2", "B3.Q3", "B3.Q4", "B3.Q7", "B3.Q12", "B3.E2", "B3.E5"],
        "mymath": {"module": "positional.py",
                   "functions": ["givens_rotation", "online_softmax", "merge_softmax_states"]},
        "reading_minutes": 150,
        "flashcards": 16,
        "notes": "Frontières : les ∂ B3.6 (Var(q·k) = d_k pour des coordonnées centrées réduites, la division par √d_k, "
                 "σ_q et σ_k, la moyenne μ non nulle (E = d_k μ², Var(q_c k_c) = 1 + 2μ²) et l'invariance par translation, "
                 "deux clés (s, 0) et p = σ(s) avec s = 8 et s = 1, la division par d_k, pourquoi fixer 1/√d_k) et B3.7 "
                 "(⟨R_mθ q, R_nθ k⟩ = ⟨q, R_(n−m)θ k⟩, le développement ⟨q, R_φ k⟩ = (q·k) cos φ + (q₂k₁ − q₁k₂) sin φ, "
                 "les écarts ±3, la version diagonale par blocs en dimension d_h, les normes conservées, l'encodage additif "
                 "et ses quatre termes, le KV cache) ; ✏️ B3.1 et B3.2 (l'attention à la main sur trois tokens, sans puis "
                 "avec un masque causal, les colonnes qui ne somment pas à 1, la renormalisation oubliée), ✏️ B3.4 (valeurs "
                 "de l'encodage sinusoïdal, une paire décalée, PE₀·PE₂, PE₁₀₀·PE₁₀₂), ✏️ B3.3 et B3.5 (les formes et les "
                 "paramètres d'une attention multi-têtes et d'un GPT), 🔨 B3.14 (`split_heads`, `merge_heads`, "
                 "`multi_head_attention`), 🧮 B3.8 (6ND, GPT-3, Chinchilla, "
                 "KV cache), 🔨 B3.12 et B3.15 (les fonctions `mylearn` des masques, de l'attention, de l'encodage "
                 "sinusoïdal et de RoPE), 🔮 B3.13 (une clé copiée, la bascule 1 + e^{7,5}, la log-normale, le maximum de "
                 "gaussiennes), 🐛 B3.17 (trois masques qui mentent), 🔬 B3.27 (temps et mémoire de l'attention en "
                 "échelles logarithmiques), 🛠️ B3.29 (un test qui prouve la causalité : modifier le futur ne change pas "
                 "le passé), les quiz B3.Q2 (scores (0 ; 0 ; ln 3)), B3.Q3 (√d_k), B3.Q4 (les cases d'un masque causal), "
                 "B3.Q7 (ordre, positions, angle de RoPE) et B3.Q12 (coût quadratique et FlashAttention), les entretiens "
                 "B3.E2 (coût et contextes longs) et B3.E5 (positions et RoPE). MB3 enseigne les outils hors réseau : un "
                 "bras articulé, des rotations de l'espace, la direction du vent, le calendrier d'une série de relevés "
                 "(la journée, la semaine, l'année), des stations de montagne et un refuge, des capteurs dont un tombe en "
                 "panne, des scores faits de n contributions, une caisse tenue dans une monnaie qui change, une éolienne ; "
                 "jamais un token, une requête, une clé ni une valeur au sens de workbookIA (la fiche ne les nomme que "
                 "dans ses encadrés 🔗 et dans « Et maintenant, dans workbookIA »), ni W_Q, W_K, W_V, une tête, une "
                 "position m ou n, la base 10 000, d_k, un KV cache, un FLOP par token, un modèle de langue. "
                 "Les rotations (§1 à §3) : les formules d'addition sont démontrées (∂ MB3.8, par le produit scalaire de "
                 "(cos a, sin a) et (cos b, sin b), R9 ; M22 et M25a les tiraient d'une règle admise), puis "
                 "R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ} et e^{iα}e^{iβ} = e^{i(α+β)} ; une même rotation conserve le "
                 "produit scalaire (MML §3.9.4). Aucun exercice ni la fiche ne calculent le produit scalaire de deux "
                 "vecteurs quelconques tournés d'angles différents, ne l'écrivent ⟨u, R_{β−α} v⟩ ni ne développent "
                 "u·R_φ v en cos φ et sin φ (∂ B3.7.1 et B3.7.2) ; le seul produit scalaire de deux vecteurs tournés "
                 "d'angles différents est celui de deux vecteurs unitaires (cos a, sin a)·(cos b, sin b) = cos(a − b), "
                 "qui est la formule du §1. Le bras articulé (✏️ MB3.1) a deux segments et des angles de 30°, 45°, 60° "
                 "ou leurs sommes, en valeurs exactes (ni les 112,5° ni la matrice (3.74) de MML, ni les vecteurs (2, 3) "
                 "et (0, −1) tournés de 30° de l'exercice 3.10 de MML, conseillé seulement). Les rotations de Givens "
                 "(✏️ MB3.2, 🔨 MB3.14, 📖 MB3.12) : deux rotations de l'espace dont les plans se coupent ne commutent "
                 "pas, deux rotations de ℝ⁴ dans des plans disjoints commutent et forment une matrice diagonale par "
                 "blocs ; PᵀRP est la même rotation dans d'autres plans de coordonnées, énoncé en général et calculé sur "
                 "une permutation de ℝ⁴ qui n'envoie pas les paires de coordonnées voisines sur les moitiés : aucun "
                 "exercice ne passe des paires voisines aux moitiés (FB3:430, ∂ B3.7.4), ni ne tourne "
                 "chaque paire d'un angle proportionnel à un indice, ni ne prend des fréquences base^{−2i/d} (RoPE) ; le "
                 "produit par blocs ([A₁ … A_H] [W₁ ; … ; W_H] = Σ A_h W_h) est enseigné sur des matrices quelconques, "
                 "sans têtes ni concaténation de sorties (✏️ B3.3 et 🔨 B3.14 de workbookIA). "
                 "Les horloges (§4) : une variable cyclique d'un calendrier ou d'une boussole, encodée par "
                 "(cos ωt, sin ωt) ; le décalage comme rotation et le produit scalaire Σ_k cos ω_k(t − t′) de plusieurs "
                 "horloges sont dans la fiche (la décision commune les demande, dans un cadre de séries temporelles) et "
                 "dans le 🎨 MB3.19 (la journée, la semaine, l'année : une courbe de l'écart, sans vérifier sur deux "
                 "paires de dates de même écart l'égalité de leurs produits scalaires, ✏️ B3.4 g–h et FB3:377-386) ; "
                 "aucun exercice ne calcule à la main le produit scalaire de deux encodages à plusieurs horloges, ni des "
                 "valeurs d'un encodage à fréquences géométriques (✏️ B3.4) ; les ✏️ n'ont qu'une horloge (la direction "
                 "du vent, ✏️ MB3.3, avec ‖e(t) − e(t′)‖² = 2 − 2 cos ω(t − t′) sur d'autres nombres que cos = 0,8 et 0,4, "
                 "B2.Q12) ; ni « position », ni 10 000, ni matrice PE. L'horloge de 24 h du 🎨 MB3.19 encode un instant du "
                 "calendrier, à deux conditions : l'unité est l'heure d'une journée (jamais des « pas ») ; aucune série "
                 "échantillonnée et bruitée, aucune fenêtre de 8 valeurs, aucune prédiction (ce que M22 évitait est le "
                 "sinus de période 24 pas, bruité, de 22.14 de workbookIA). "
                 "Les moyennes pondérées (§5) : la softmax de scores, l'estimateur de Nadaraya-Watson (noyau gaussien de "
                 "l'altitude, ✏️ MB3.4 ; la largeur de bande comme une température, 🔮 MB3.17), et, dans le 🔗 MB3.11, "
                 "des stations sur un même cercle (x·xᵢ = ρ² cos(φ − φᵢ)) : à normes égales, le noyau gaussien est une "
                 "softmax des produits scalaires divisés par h² ; ni √d_k, ni projections, ni trois tokens. "
                 "Les masques (§6) : un score −∞ est un conditionnement (M03, M28) ; la moyenne exponentielle normalisée "
                 "comme une softmax sur le passé et un capteur en panne retiré (✏️ MB3.5, des fractions exactes) ; les "
                 "cases d'un masque triangulaire, T(T + 1)/2, dans la fiche seulement (B3.Q4 a) ; « mettre un poids à 0 après "
                 "la softmax ne donne pas une loi » est dans la fiche et au plus un vrai ou faux de 🧠 MB3.Q4, jamais une "
                 "erreur à corriger (l'erreur fréquente de ✏️ B3.2) ; ni masque transposé, ni convention inversée, ni "
                 "padding dans une loss (🐛 B3.17) ; la causalité d'un filtre (le futur ne change pas le passé) est "
                 "énoncée dans la fiche, jamais vérifiée par un test (🛠️ B3.29). L'équivariance par permutation "
                 "(∂ MB3.9) est démontrée en général, avec des matrices de permutation (M16), pour une moyenne pondérée "
                 "sur un ensemble de points (des élèves, des capteurs) ; FB3:359 l'énonce sans preuve ; aucun quiz ne "
                 "demande si l'on « voit l'ordre » sans encodage (B3.Q7 a–b), ni « le chien mord l'homme ». "
                 "Les quiz : MB3.Q5 porte sur l'échelle comme une température (multiplier les scores, leur ajouter une "
                 "constante), jamais sur l'écart-type d'une somme ni sur ce qu'est une softmax saturée (B3.Q3) ; MB3.Q6 ne "
                 "demande pas si la softmax en ligne est exacte ou approchée, ni ce qu'elle réduit (la mémoire, pas les "
                 "opérations : B3.Q12 b–c), et ne compte aucune paire (B3.Q12 a : le facteur f² sur le nombre de paires est "
                 "dans la fiche seulement) ; MB3.Q4 ne demande ni la forme d'une sortie (B3.Q2 e), ni si une moyenne pondérée « voit "
                 "l'ordre » (B3.Q7). "
                 "L'échelle des scores (§7) : l'écart-type √(nv) d'une somme de n contributions indépendantes centrées et "
                 "la division par √n sont dans la fiche seulement, sans exercice (B3.Q3 a) ; ✏️ MB3.6 ne garde que la "
                 "saturation ; la variance d'un produit de deux variables "
                 "indépendantes est un rappel de M16, jamais recalculée pour une somme de produits de coordonnées "
                 "(∂ B3.6.1-2) ; la saturation porte sur K = 3 scores au moins, multipliés par un facteur c, mesurée par "
                 "le poids maximal et 1 − Σ pᵢ² ; jamais deux scores (s, 0) et σ(s), ni la dérivée p(1 − p) d'une "
                 "sigmoïde comparée entre deux échelles (∂ B3.6.5-6) ; la borne 1 − p_max ≤ (K − 1) e^{−cΔ} (Δ, l'écart "
                 "entre le plus grand score et le suivant) est dans la fiche, avec son idée de preuve. Le point "
                 "facultatif de la décision commune, E[e^{σZ}] = e^{σ²/2} et le maximum de n gaussiennes, n'est pas "
                 "retenu : il ne sert qu'au corrigé du 🔮 B3.13 (frontière), et le budget n'en laisse pas la place. "
                 "La softmax en ligne (§8) : l'état (m, l, a), écrit (m, l, acc) dans le code comme dans la fiche de "
                 "workbookIA B3 ; la fiche de B3 montre le code sans preuve, MB3 démontre l'invariant et l'associativité "
                 "de la fusion (∂ MB3.10) ; ✏️ MB3.7 prend neuf scores multiples de ln 2 (des exponentielles qui sont "
                 "des puissances de 2, des sommes exactes) lus par blocs de trois ; le 🔬 MB3.18 compte les remises à "
                 "l'échelle (des scores croissants : à chaque bloc ; au hasard : H_N − 1 en moyenne sur N blocs, les "
                 "records, démontré dans la fiche par des indicatrices) ; la 🗣️ MB3.13 compare l'état à une caisse tenue "
                 "dans une monnaie qui change ; ni 1 000 clés par blocs de 128, ni `default_rng(1)`, ni l'échelle 4,0. "
                 "Le coût (§9) : une ligne rappelle MB2 §8 (C(n, 2) comparaisons contre n vecteurs) ; le § ne garde que ce "
                 "qui est neuf, la mémoire n × n contre n·B par blocs et la pente 2 en échelles logarithmiques, sur des "
                 "matrices de distances entre clients ou entre villes ; ni FLOPs par token, ni "
                 "24d², 4Td, T/(12d), 49 152, ni mesure du temps de l'attention (🔬 B3.27), ni Gio d'un modèle. Le "
                 "💼 MB3.E1 porte sur l'encodage d'une variable cyclique (une question de feature engineering), pas sur "
                 "les positions d'un Transformer (B3.E5). Les exercices ne reprennent ni les exemples de la fiche de MB3 "
                 "ni ceux du stub. "
                 "Évités (règle de partage) — de workbookIA B3 : l'exemple d'attention à quatre clés de la fiche "
                 "(q = (1, 0, 1, 0), clés (1, 1, 0, 0), (0, 1, 1, 0), (2, 0, 2, 0), (0, 0, 0, 2), valeurs (1, 0), (0, 1), "
                 "(2, 2), (−1, 1), scores 0,5 ; 0,5 ; 2 ; 0, exponentielles 1,6487 et 7,3891, sommes 11,6865 et 10,6865, "
                 "poids 0,1411 ; 0,6323 ; 0,0856, et masqués 0,1543 ; 0,6914, sorties (1,3201 ; 1,4912) et "
                 "(1,5372 ; 1,5372)) ; les trois tokens (1, 0), (0, 1), (1, 1) et W_Q = [[0, 1], [1, 1]], "
                 "W_K = [[1, 0], [1, 2]], W_V = [[1, −1], [0, 2]] de ✏️ B3.1-B3.2 (QKᵀ = [[0, 2, 2], [1, 3, 4], "
                 "[1, 5, 6]], 3,536, 0,324, (0,676 ; 1,286), 0,727, 0,4458 et 0,1084, 0,202, 1,075 et 1,723, 2,0281 ; "
                 "34,3133 ; 69,5914, (0 ; 0,0008 ; 0,9992), (0,196 ; 0,804 ; 0), (0,196 ; 1,413), (0,0743 ; 0,3057 ; 0) "
                 "et 0,38, x₂ = (2, 0) et 0,8943) ; q = (1, 3), k = (2, 2) et 5,66, les scores (0 ; 0 ; ln 3) et 0,6 ; "
                 "d_k = 4, 16, 64, 256, 512, 1 024 et les écarts-types 2, 4, 8, 16, 23, 32, la simulation de 100 000 "
                 "produits (4,03 ; 64,09 ; 514,18 ; 1,007 ; 1,001 ; 1,004), deux scores (s, 0) avec s = 8 ou 1 (0,99966 ; "
                 "3,35 × 10⁻⁴ ; 0,7311 ; 0,1966 ; les rapports 586 et 73), σ(0,125) ≈ 0,531, 1 + 2μ², ‖k‖² ; "
                 "l'encodage d = 8, base 10 000, ω_i = 10⁻ⁱ, la période 200π ≈ 628, sin 25 ≈ −0,132, sin 2,5 ≈ 0,5985, "
                 "cos 2,5 ≈ −0,8011, la paire (0,6 ; 0,8) décalée de 10 (angle 1 rad, (0,9974 ; −0,0726)) ou de −5 "
                 "((0,1430 ; 0,9897)), PE₀·PE₂ ≈ 2,5637, arcsin(0,6)/0,1 ≈ 6,435, 20π, cos > 0,995 ; d = 16, T = 50, "
                 "PE₅·PE₉ = PE₂₀·PE₂₄ ≈ 5,56, PE_p·PE_p = 8, 64 positions en dimension 64, les périodes 2π ≈ 6,3 et "
                 "20 000 positions ; RoPE : θ = 0,5 rad, q = (1, 2), k = (3, −1), (m, n) = (0, 3), (4, 7), (10, 13), "
                 "(7, 4), 7,0532 et −6,9117, cos 1,5 ≈ 0,0707 et 7 sin 1,5 ≈ 6,9825 ; θ = π/6, q = (2, 1), k = (1, 1), "
                 "(0, 0), (5, 2), (1, 4), (7, 10) et 3, 1, −1, −1 ; θ = π/4, q = (1, 0), k = (0, 1), (0, 2) et −1 ; "
                 "A = [[1, 2], [0, 1]], x = (1, 1) et (3, 1) ; i = 16, la position 250, θ = 10⁻², 2,5 rad ; les bases "
                 "10 000, 500 000 et 1 000 000 ; q = (1, 0, 0, 0) en position 1 et (cos 1, 0, sin 1, 0) ; les exemples du "
                 "stub `attention` (`positional_encoding(3, 4)`, `apply_rope(np.ones((3, 4)))`, (−0,3012 ; 0,99 ; "
                 "1,3818 ; 1,0099), q = [[1, 0]], k = I, v = [[1, 2], [3, 4]], (0,6698 ; 0,3302) et (1,6605 ; 2,6605), "
                 "`causal_mask(2, 4)`, `padding_mask([2, 3], 4)`, `np.arange(12.0).reshape(1, 2, 6)` et H = 3) ; les "
                 "logits (2 ; 1 ; 0,5 ; 0 ; −1) à T = 0,8 et k = 3 (0,6945 ; 0,1990 ; 0,1065) ; la softmax en ligne sur "
                 "1 000 clés de dimension 16 et des valeurs de dimension 8, par blocs de 128, échelle 4,0, "
                 "`default_rng(1)` ; 5 tokens et 15 cases, `causal_mask(1, 9)`, les longueurs [3, 5] ; les comptes de "
                 "paramètres (4d² + 4d, 12d² + 13d, 591 360, 394 240, 344 960, 2 099 712, GPT-2 small et medium, "
                 "BERT-base, le mini-GPT à 4 blocs, d = 128, V = 88 et 820 992, d = 384 et H = 6, d = 512 et H = 8 ou 16, "
                 "d = 256 et F = 1 024) ; T = 12d et 49 152, 24d² et 4Td, H = 32 et T = 8 192 (8 Gio), 131 072 (2 Tio), "
                 "6ND, GPT-3, Chinchilla et 20 tokens par paramètre, Llama 3 405B, Qwen3-8B, les KV caches (16 Gio, "
                 "128 Kio, 144 Kio, 512 Kio), 1,5 To/s et 20 Mo, 64 à 2 048 tokens et 64 Mio ; 0,9⁵⁰ ≈ 0,0052, la layer "
                 "norm de (1, 2, 3, 6), log 65 ≈ 4,17 et log 50 257 ≈ 10,825 ; la clé copiée de 🔮 B3.13 (d_k = 64, "
                 "200 requêtes, S de 10 à 100 000, 1 + e^{7,5} ≈ 1 800, e^{1/2}, 8√(2 ln 10⁵) ≈ 38) ; « le chat que "
                 "Marie a adopté dort », « le chien mord l'homme », Holmes, Watson, Verne, Fashion-MNIST, les patchs "
                 "d'un ViT (P = 16, 196 patchs) ; le cache de B3.Q11 (2 couches, d = 64, 100 tokens, float32, 102 400 "
                 "octets) et les 15 % de 200 tokens de B3.Q9 (30, puis 80 % : 24). De workbookIA B1 et B2 (des cosinus et des softmax) : a₀ = (1, 0, 0), "
                 "a₁ = (4, 2, 2), a₂ = (2, 1, 0), a₃ = (0, 1, 1), q = (2, 1, 1) ; les prototypes (0,9 ; 0,1), "
                 "(0,7 ; 0,3), (0,2 ; 0,8), (0,4 ; 0,8), q = (0,6 ; 0,5), 0,900 et 0,869 ; les cosinus 0,31 ; 0,27 ; 0,22 "
                 "avec s = 100 (0,982 ; 0,018 ; 0,0001) et s = 1 (0,348 ; 0,334 ; 0,318), et 0,24 ; 0,30 ; 0,28 ; 0,19 "
                 "avec logit_scale 4,60517 et 2,6592 ; e₀ = (3, 0, 4), e₁ = (0, 3, 4), e₂ = (16, 2, 8), e₃ = (2, 1, 2), "
                 "e₄ = (1, 0, 0), e₅ = (0, 1, 1), q = (1, 2, 2) ; le planning en cosinus (η = 10⁻³ ou 2 × 10⁻³, "
                 "γ = 0,3 ou 0,5, t_w = 4 ou 5, 105 pas) ; cos = 0,8 et ‖a − b‖² = 0,4, √2 pour deux vecteurs "
                 "orthogonaux, (3, 4) et (−6, −8) ; la moyenne avec masque de (1, 2), (3, 0), (2, 4), (0, 0) (2,0 et "
                 "1,5) ; les comptes 100 et 1 (0,969 et 0,031) ; les scores (1, 2, 3), (1001, 1002, 1003) et T = 0,5 des "
                 "docstrings de `softmax` et `temperature_softmax` (workbookIA 17 et 22). De ce dépôt : la matrice "
                 "(3.74) et les 112,5° de MML, les vecteurs (2, 3) et (0, −1) de l'exercice 3.10 de MML ; la rotation-"
                 "homothétie de M22.3 (θ = 2π/3, r = 0,6, x₀ = (2, 0)) et z² − 0,24 de la fiche M22 ; la caméra de M25a "
                 "(u = (1, 1, 0)/√2, 60°, 0,577 ; 0,816 ; 0,299) ; v = (710, 708, 700) de M05a et les exemples de "
                 "`approx.logsumexp` ([0, 0], [1000, 1000]) ; les énergies (0 ; 0,5 ; 2) de M17 ; les exemples de "
                 "`temper` et `smallest_mass_set` et le météorologue de M28.6 ; u = (3 ; −1) et v = (−2 ; 4) de la fiche "
                 "R9 ; les exemples du stub `positional` (π/3 dans le plan (1, 3) de ℝ⁴, 1,2 dans le plan (2, 0) de ℝ³, "
                 "les scores (0, ln 4, ln 2) et les valeurs (10, 20, 40), (−800, −801, −799), les états (0 ; 1,5 ; 3) et "
                 "(ln 2 ; 1 ; 4), les scores (1, 3, 3, 0) et les valeurs (2, 6, 4, 5)), comme nombres et comme "
                 "configurations (un second état fait d'un seul score à m + ln 2). Ajoutés par la relecture de la "
                 "session 72 : de workbookIA, 1,4142 et les scores (0 ; 1,4142) de la variante de ✏️ B3.2, 0,879 (B1), "
                 "la question « modifier le futur change-t-il le passé ? » de B3.Q4 c (même en consigne de copie), deux "
                 "paires de même écart (✏️ B3.4 h, même avec une seule horloge), et l'erreur fréquente de ✏️ B3.2 (un "
                 "poids mis à 0 sans renormaliser), ni en erreur fréquente, ni en valeur fausse, ni en flashcard ; de ce "
                 "dépôt, M28 §4 (le produit en somme, 1 − cos ω = 2 sin²(ω/2), (1 + 2 cos ω)/3) et M28.5 a (2 − √3 ≈ "
                 "0,268, période 12), M09a §3 (Σ colonne × ligne), M11.13 (la somme harmonique), le 🗣️ M17.13 (les "
                 "monnaies) et le refuge de M25a §5 (1 520 m, un baromètre). "
                 "Conventions : angles en radians (en degrés dans un énoncé qui le dit), positifs dans le sens inverse des "
                 "aiguilles d'une montre ; vecteurs en colonne, R_θ x ; une rotation de Givens tourne e_i vers e_j "
                 "(MML (3.81) pour i < j), indices à partir de 1 dans la fiche et dans MML, à partir de 0 dans le code ; "
                 "e^{iθ} = cos θ + i sin θ (la formule d'Euler, admise en M22, est ici une définition) ; une loi est "
                 "une softmax d'un vecteur de scores, et un masque met un score à −∞ ; le noyau gaussien est "
                 "exp(−‖x − xᵢ‖²/(2h²)), sa constante n'importe pas ; l'état de la softmax en ligne est (m, l, acc), "
                 "l'état vide (−∞, 0, acc nul ou None), de même nature que les états qu'il complète ; logarithme "
                 "népérien. "
                 "`positional` : NumPy et `math` permis, aucune fonction de SciPy (`scipy.special.softmax`, `logsumexp`, "
                 "`scipy.spatial.transform.Rotation` sont les oracles des tests) ni `np.logaddexp`. `givens_rotation` "
                 "(MML §3.9.3) contient le cas du plan (n = 2) : `rotation_matrix_2d` et `rotate_complex` du plan sont "
                 "retirées (une ligne chacune) ; `online_softmax(scores, values=None, block_size=1, history=False)` rend "
                 "l'**état** "
                 "(m, l, acc), pas des poids ni une sortie d'attention : elle ne prend ni requête, ni clés, ni masque, ni "
                 "échelle (le contrat de `scaled_dot_product_attention` de workbookIA B3), et accepte des scores −∞ ; avec "
                 "`history=True`, elle rend la liste des états après chaque bloc, ce qui rend testables l'invariant de "
                 "∂ MB3.10, la lecture par blocs de 🔨 MB3.15 et les remises à l'échelle du 🔬 MB3.18 ; l'état vide n'est "
                 "neutre que pour les états de même nature (acc `None`, nombre ou tableau), et l ≥ 1 reste exigé quand m "
                 "est fini (vrai exactement en flottants pour un état produit par `online_softmax` ou par une fusion) ; "
                 "`merge_softmax_states` (la fusion associative, sans équivalent dans `mylearn`) ; aucune fonction de "
                 "masque (`masked_softmax` serait le cœur de 🔨 B3.12), de positions, de fréquences base^{−2i/d} ni "
                 "d'encodage (🔨 B3.15), ni `block_rotation` (appliquée à m·freqs, ce serait RoPE) ; Nadaraya-Watson "
                 "s'écrit dans les exercices, sans fonction `mymath`. Aucune fonction n'a le nom ni le contrat d'une "
                 "fonction de `mylearn` (`causal_mask`, `padding_mask`, `scaled_dot_product_attention`, `split_heads`, "
                 "`merge_heads`, `multi_head_attention`, `positional_encoding`, `apply_rope`, `transformer_block` en B3 ; "
                 "`softmax` de workbookIA 17 rend des poids, pas un état). "
                 "MML : §3.9 lu (📖 MB3.12), avec un guide de lecture : §3.9.1 avant le §2 de la fiche, §3.9.2 à §3.9.4 "
                 "avant le §3 ; MML ne démontre pas les formules d'addition (§3.9.1 lit les images de e₁ et e₂ sur la figure 3.16, "
                 "§3.9.4 énonce la commutativité dans le plan sans preuve) et ne parle ni "
                 "des horloges, ni des moyennes pondérées, ni de la softmax en ligne ; l'exercice 3.10 de MML est "
                 "conseillé. "
                 "COMPOSITION : 3 🔨 et aucun 📦 (au lieu de 4 🔨/📦) : les trois 🔨 écrivent tout `positional`, et les "
                 "bibliothèques qui feraient un 📦 (`scipy.special.softmax`, `logsumexp`, `Rotation`) sont les oracles "
                 "des tests ; un 📦 « la décomposition QR par des rotations de Givens, comparée à `np.linalg.qr` » "
                 "(25 min) a été écarté pour tenir le budget. 10 ✏️/∂, 6 quiz, un 💼, 16 flashcards : le bas des "
                 "fourchettes du §13. Parcours essentiel : le 📖, ∂ MB3.9 (l'équivariance, énoncée), le 🔬, le 🛠️ et le 🏆 "
                 "hors parcours. "
                 "**Durée** (session 69) : 12,8 h (essentiel 10,6 h ; lecture de la fiche 150 min, neuf sections) au "
                 "lieu des 12 h visées (13,0 h avant les relectures, qui ont retiré trois sous-questions frontières) : "
                 "neuf notions nouvelles, dont trois démonstrations (les formules d'addition, "
                 "lacune de R9 à M28 ; l'équivariance ; l'invariant de la softmax en ligne), MML §3.9 lu, et des durées "
                 "relevées comme celles de M25a à M28. Génération (session 72) : le critère du 🏆 MB3.22 est relatif (au plus 1,3 "
                 "fois l'erreur quadratique moyenne de la méthode de référence, sur le jeu du notebook et trois éoliennes "
                 "cachées de bruit faible, moyen et fort tirées à chaque exécution ; générateur et méthode dans "
                 "`solutions/challenges/mb3_22.py`, hors du notebook) ; ∂ MB3.8 q. 6 (det R_θ et duplication) ; durées "
                 "revues après la re-résolution à l'aveugle, l'auteur des exercices et l'apprenant simulé : exercices "
                 "708 min, 14,8 h en tout et 11,9 h en parcours essentiel.",
        "exercises": [
            ("MB3.Q1", "🧠", 1, 5, "Formules d'addition et rotations du plan : le bon signe, composer, inverser, rotation "
             "ou symétrie ?", "§1 §2", "E"),
            ("MB3.Q2", "🧠", 1, 6, "Rotations de l'espace, de Givens et par blocs : commutent-elles, que fixent-elles, que "
             "change une permutation des coordonnées ?", "§3", "E"),
            ("MB3.Q3", "🧠", 1, 5, "Encoder une direction ou un jour de l'année : une ou deux coordonnées, quelle période, "
             "quelle distance entre deux encodages ?", "§4", "E"),
            ("MB3.Q4", "🧠", 1, 4, "Moyennes pondérées par une softmax : dans l'enveloppe convexe ou non, largeur de bande, "
             "masque avant ou après la softmax, et un sous-ensemble vide", "§5 §6", "E"),
            ("MB3.Q5", "🧠", 1, 5, "Multiplier tous les scores par c, ou leur ajouter une constante : ce qui change dans les "
             "poids, le poids maximal et l'entropie, et ce qui ne change pas", "§7", "E"),
            ("MB3.Q6", "🧠", 1, 5, "La softmax en ligne : ce que garde l'état, quand le remettre à l'échelle, et l'état "
             "vide", "§8", "E"),
            ("MB3.R1", "🔁", 1, 7, "La forme exponentielle d'un complexe, et le produit comme rotation et homothétie (M22)",
             "§2", "E"),
            ("MB3.R2", "🔁", 1, 6, "Le log-sum-exp et la softmax stable (M05a)", "§8", "E"),
            ("MB3.R3", "🔁", 1, 7, "Tempérer et tronquer une loi : p^{1/T} renormalisée, top-k et top-p comme lois "
             "conditionnelles (M28)", "§5 §6", "E"),
            ("MB3.1", "✏️", 2, 28, "Un bras articulé à deux segments : la position de la pince en valeurs exactes par les "
             "formules d'addition, les deux rotations enchaînées en une seule, et le retour par la rotation inverse",
             "§1 §2", "E"),
            ("MB3.2", "✏️", 2, 30, "Rotations de Givens : deux rotations de l'espace qui ne commutent pas, deux rotations de "
             "ℝ⁴ dans des plans disjoints qui commutent, leur matrice diagonale par blocs, et la même rotation après une "
             "permutation des coordonnées", "§3", "E"),
            ("MB3.3", "✏️", 2, 22, "La direction du vent : l'encoder par (cos, sin), la distance entre deux encodages, un "
             "vent qui tourne comme une rotation de l'encodage, et la direction moyenne de trois relevés", "§4", "E"),
            ("MB3.4", "✏️", 2, 28, "L'estimateur de Nadaraya-Watson : la température d'un refuge à partir de quatre "
             "stations de montagne pondérées par un noyau gaussien de l'écart d'altitude, pour deux largeurs de bande, "
             "et ses deux limites", "§5", "E"),
            ("MB3.5", "✏️", 2, 16, "Masques : une moyenne exponentielle normalisée vue comme une softmax sur les jours "
             "passés, puis la même quand un capteur tombe en panne un jour (un score −∞)", "§6", "E"),
            ("MB3.6", "✏️", 2, 22, "La saturation d'une softmax : trois scores multipliés par un facteur c croissant, le "
             "poids maximal, la sensibilité 1 − Σ pᵢ² et la borne (K − 1) e^{−cΔ}", "§7", "E"),
            ("MB3.7", "✏️", 2, 30, "La softmax en ligne à la main : neuf scores (des multiples de ln 2) et leurs valeurs lus "
             "par blocs de trois, l'état (m, l, a) après chaque bloc, la moyenne pondérée finale, puis la fusion de deux "
             "états calculés séparément", "§8", "E"),
            ("MB3.8", "∂", 2, 40, "Les formules d'addition par le produit scalaire de deux vecteurs unitaires ; puis "
             "R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}, et la règle e^{iα}e^{iβ} = e^{i(α+β)} que M22 admettait",
             "§1 §2", "E"),
            ("MB3.9", "∂", 2, 25, "Une moyenne pondérée par une softmax sur un ensemble de points commute avec toute "
             "renumérotation des points ; un masque triangulaire casse cette équivariance", "§6", ""),
            ("MB3.10", "∂", 2, 30, "La softmax en ligne est exacte : l'invariant de l'état après chaque bloc, par "
             "récurrence ; puis la fusion de deux états est associative et commutative, d'élément neutre (−∞, 0, 0)",
             "§8", "E"),
            ("MB3.11", "🔗", 1, 22, "Pont : à normes égales, les poids d'un noyau gaussien sont une softmax des produits "
             "scalaires divisés par h² ; le vérifier sur quatre stations d'un même cercle, et lire 1/h² comme l'échelle "
             "des scores", "§5 §7", "E"),
            ("MB3.12", "📖", 2, 40, "MML §3.9 lu : la rotation du plan (3.76), les rotations de l'espace (3.77)–(3.79), la "
             "rotation de Givens (3.80)–(3.81) et les propriétés du §3.9.4 ; R₂(θ) écrite comme une rotation de Givens, "
             "et deux rotations de l'espace qui ne commutent pas, sur un vecteur choisi", "§2 §3", ""),
            ("MB3.13", "🗣️", 1, 15, "Expliquer, avec une caisse tenue dans une monnaie qui change, pourquoi la softmax en "
             "ligne donne exactement le résultat du calcul en une fois", "§8", "E"),
            ("MB3.E1", "💼", 1, 10, "« Comment encoder une variable cyclique comme une heure ou une direction, et pourquoi "
             "pas par sa valeur ? »", "§4", "E"),
            ("MB3.14", "🔨", 1, 25, "La matrice d'une rotation de Givens de ℝⁿ", "§3", "E m:givens_rotation"),
            ("MB3.15", "🔨", 2, 50, "La softmax en ligne : l'état (m, l, a) de scores et de valeurs lus par blocs, et "
             "l'état après chaque bloc", "§8",
             "E m:online_softmax"),
            ("MB3.16", "🔨", 2, 30, "La fusion de deux états de la softmax en ligne", "§8",
             "E m:merge_softmax_states p:MB3.15"),
            ("MB3.17", "🔮", 1, 30, "Prédire ce que deviennent les poids et la prévision de Nadaraya-Watson quand la largeur "
             "de bande est divisée ou multipliée par 10, puis tracer", "§5 §7", "E"),
            ("MB3.18", "🔬", 2, 30, "La softmax en ligne selon l'ordre et la taille des blocs : le nombre de remises à "
             "l'échelle (les états après chaque bloc) pour des scores croissants, décroissants ou mélangés, comparé à "
             "H_N − 1, et la mémoire gardée",
             "§8 §9", ""),
            ("MB3.19", "🎨", 1, 30, "Trois horloges (la journée, la semaine, l'année) : l'encodage d'une date sur trois "
             "cercles, un décalage comme trois rotations, et le produit scalaire de deux encodages en fonction de l'écart",
             "§4", "E"),
            ("MB3.20", "🐛", 1, 25, "Chasse à l'erreur : deux rotations de l'espace composées dans le mauvais ordre, une "
             "direction moyenne prise comme la moyenne des angles, une softmax en ligne qui remet l à l'échelle mais pas "
             "l'accumulateur", "§3 §4 §8", "E"),
            ("MB3.21", "🛠️", 1, 35, "Un test de propriété : la softmax en ligne ne dépend ni de la taille des blocs, ni "
             "d'une même permutation des scores et des valeurs, ni d'une constante ajoutée aux scores, et la fusion de "
             "trois états est associative", "§8", "p:MB3.15,MB3.16"),
            ("MB3.22", "🏆", 3, 45, "Défi : prévoir la production d'une éolienne par Nadaraya-Watson sur l'encodage "
             "cyclique de la direction du vent et du jour de l'année, la largeur de bande choisie par validation "
             "croisée « un de côté », sous une erreur quadratique moyenne donnée", "§4 §5", ""),
        ],
    },
    {
        "id": "MB4", "dir": "mb4_rang_faible", "hours": 7.6, "generation_sessions": 1, "mml": ["(§4.6)"],
        "summary": "Les maths du rang faible et de la recherche d'information : la factorisation de rang (une matrice de "
                   "rang r est le produit de r colonnes par r lignes, à une matrice inversible près), ce qu'elle coûte à "
                   "stocker et ses nombres libres, le rang effectif d'une matrice mesurée (rappel d'Eckart-Young) et "
                   "l'ordre des produits ; le poids d'un indice rare, de la surprise au log du rapport des cotes de "
                   "Robertson et Spärck Jones ; la saturation et la normalisation par la longueur, étudiées comme des "
                   "fonctions ; la fusion de classements par les scores ou par les rangs (Borda, somme des 1/(c + rang)) ; "
                   "enfin recall@k, precision@k, MRR et la ligne de base d'un ordre tiré au hasard. workbookIA B4 "
                   "applique ces outils à LoRA, à BM25, à la recherche hybride et à l'évaluation d'un RAG.",
        "objectives": [
            "Factoriser une matrice de rang r en un produit C F de r colonnes par r lignes, en trouver une autre, et "
            "compter les nombres stockés et les nombres libres.",
            "Démontrer que deux factorisations de rang diffèrent d'une matrice inversible, et que le rang est le plus "
            "petit nombre de produits extérieurs dont une matrice est la somme.",
            "Mesurer le rang effectif d'une matrice de mesures par l'énergie de ses valeurs singulières, et appliquer "
            "une matrice factorisée dans l'ordre le moins coûteux.",
            "Calculer le poids d'un indice rare comme une surprise et comme le log d'un rapport de cotes corrigé par ½, "
            "et dire quand il devient négatif.",
            "Étudier la saturation x ↦ x(k₁ + 1)/(x + k₁) et la normalisation par la longueur, et prévoir l'effet de "
            "k₁ et de b.",
            "Fusionner des classements par les rangs (Borda, somme des 1/(c + rang)), démontrer qu'ils ne dépendent pas "
            "de l'échelle des scores, et trouver quand une double présence bat une première place.",
            "Définir recall@k, precision@k, taux de succès et MRR, et calculer leur valeur moyenne pour un ordre tiré au "
            "hasard (k/n, H_n/n).",
        ],
        "sections": [("§1", "La factorisation de rang : une matrice de rang r est un produit C F, et ce qu'elle coûte à "
                            "stocker"),
                     ("§2", "Le rang effectif d'une matrice mesurée, et l'ordre des produits : C(Fx) plutôt que (CF)x"),
                     ("§3", "Le poids d'un indice rare : surprise, cote, et le log du rapport des cotes corrigé par ½"),
                     ("§4", "Saturation et normalisation par la longueur : deux fonctions d'un score de pertinence"),
                     ("§5", "Fusionner des classements : par les scores ou par les rangs, Borda et la somme des "
                            "1/(c + rang)"),
                     ("§6", "Mesurer un classement : recall@k, precision@k, MRR, et ce que donne le hasard")],
        "teaches": ["factorisation de rang : une matrice m × n de rang r est un produit C F, C fait de r colonnes "
                    "indépendantes de la matrice (ses colonnes pivots), F de ses r lignes non nulles de forme échelonnée "
                    "réduite (l'identité dans les colonnes pivots) ; le rang est le plus petit nombre de produits "
                    "extérieurs dont la matrice est la somme (rang(CF) ≤ r : rappel de M12a)",
                    "non-unicité : (CG)(G⁻¹F) pour toute G inversible r × r, et rien d'autre ; stockage r(m + n) "
                    "contre mn ; r(m + n − r) nombres libres (la forme de F en fixe r²)",
                    "rang effectif d'une matrice mesurée : part de l'énergie ‖·‖²_F captée par les r premières valeurs "
                    "singulières (Eckart-Young, rappel de M12d), rang numérique et tolérance (rappel de M12a), rang "
                    "stable ‖M‖²_F/‖M‖²₂",
                    "appliquer une matrice factorisée : C(Fx) coûte r(m + n) multiplications, former CF en coûte mnr et "
                    "l'appliquer mn ; le même résultat en exact (associativité), un écart d'arrondi en flottants "
                    "(rappels de M09a et M05a)",
                    "le poids d'un indice rare : surprise −ln(n/N) (rappel de M06), cote n/(N − n), log du rapport des "
                    "cotes de présence chez les pertinents et chez les autres (poids de Robertson et Spärck Jones), "
                    "correction ½ ; sans information de pertinence, ln((N − n + ½)/(n + ½)), négatif si et seulement si "
                    "n > N/2 ; la variante ln(1 + (N − n + ½)/(n + ½)) = ln((N + 1)/(n + ½)), toujours positive",
                    "saturation x ↦ x(k₁ + 1)/(x + k₁) : croissante, concave, égale à 1 en x = 1 pour tout k₁, de limite "
                    "k₁ + 1 ; k₁ → 0 donne la seule présence, k₁ → ∞ le compte brut (la forme de Michaelis et Menten) ; "
                    "normalisation par la longueur 1 − b + bℓ (ℓ : longueur rapportée à la moyenne), une interpolation "
                    "affine en b",
                    "fusionner des classements : par les scores (sensible à l'échelle de chaque système) ou par les "
                    "rangs (invariante par toute transformation strictement croissante des scores) ; méthode de Borda "
                    "(la somme des rangs) ; somme des 1/(c + rang) : j-ième pour deux listes bat premier pour une seule "
                    "si et seulement si j < c + 2 ; quand c grandit, l'ordre du nombre de listes puis de la somme des "
                    "rangs (Borda pour des classements complets) ; la recherche dense par cosinus (rappel de M07)",
                    "mesurer un classement : recall@k, precision@k, taux de succès@k, rang réciproque et MRR "
                    "(définitions) ; la ligne de base d'un ordre tiré au hasard : E[recall@k] = k/n, E[precision@k] = "
                    "q/n, la loi du rang du premier pertinent, E[1/R] = H_n/n pour un seul pertinent, H_n encadré par "
                    "ln(n + 1) et 1 + ln n (rectangles, rappel de M02a)"],
        "requires": [("dénombrement, combinaisons, espérance d'une variable discrète et sa linéarité", "R8"),
                     ("ln et ses propriétés, la cote et le logit", "R6"),
                     ("limites, dérivée, sens de variation", "R7"),
                     ("sommes de Riemann, encadrer une aire par des rectangles", "M02a"),
                     ("precision et recall comme probabilités conditionnelles, l'AUC invariante par une transformation "
                      "croissante des scores", "M03"),
                     ("dérivée seconde et concavité, 1/(1 + u) ≈ 1 − u, nombres flottants et erreurs d'arrondi", "M05a"),
                     ("information −log p d'un événement, en nats", "M06"),
                     ("cosinus, plus proches voisins", "M07"),
                     ("pivot de Gauss, forme échelonnée réduite et colonnes pivots, coût d'un produit et ordre des "
                      "parenthèses dans ABC", "M09a"),
                     ("indépendance, base, coordonnées, rang, rang(AB) ≤ min(rang A, rang B), rang numérique et "
                      "tolérance", "M12a"),
                     ("SVD, normes de Frobenius et spectrale, approximation de rang faible et son erreur (Eckart-Young), "
                      "nombres stockés d'une image en rang k", "M12d")],
        "frontieres": ["B4.2", "B4.3", "B4.5", "B4.11", "B4.17", "B4.18", "B4.25", "B4.27", "B4.Q8", "B4.Q9",
                       "B4.Q11", "B4.R3", "B4.E3"],
        "mymath": {"module": "ranks.py", "functions": ["rank_factorization", "borda_scores", "random_ranking_mrr"]},
        "reading_minutes": 95,
        "flashcards": 12,
        "notes": "Frontières : le ∂ B4.6 (ΔW = BA de rang au plus r par les colonnes de B, le seuil r(d + k) < dk, soit "
                 "r < dk/(d + k) et r < d/2 pour d = k, B nulle au départ et le point d'équilibre A₀ = B₀ = 0, les "
                 "gradients s g(Ax)ᵀ et s Bᵀg xᵀ, le premier pas de rang 1, le facteur α/r, SGD ∝ s², Adam ∝ s, √r et "
                 "rsLoRA), ✏️ B4.2 (recall@1, @3, @5, MRR et taux de succès@3 de cinq requêtes, « recall@3 n'est pas le "
                 "taux de succès », recall@1 ≤ MRR), ✏️ B4.3 (paramètres LoRA de couches 896 × 896 et 896 → 128 de rang "
                 "8, d'un modèle entier, `all-linear`, le seuil 448), ✏️ B4.5 (BM25 à la main sur trois documents, "
                 "classement, b = 0, k₁ = 0, idf original négatif), 📄 B4.11 (Hu et coll. : comptes de GPT-3, "
                 "projection de W_q sur les directions singulières de ΔW, facteur d'amplification, rang intrinsèque), "
                 "🔨 B4.17 (`chunk_text` et `BM25`), 🔨 B4.18 (`cosine_top_k`, `reciprocal_rank_fusion`, `recall_at_k`, "
                 "`mean_reciprocal_rank`, et son corrigé : k = 0 contre k = 60, rangs comptés à partir de 0), 📦 B4.25 "
                 "(`LoRALinear`), 🔬 B4.27 (perplexité contre rang), les quiz B4.Q8 (80 % de 100 questions), B4.Q9 (3ᵉ "
                 "dans deux classements, k = 60) et B4.Q11 (ce qui est gelé, r = 4 sur 512 × 512, α/r), le rappel B4.R3 "
                 "(cosinus et distance de vecteurs unitaires) et l'entretien B4.E3 (expliquer LoRA). B4.Q5 et B4.13 "
                 "(stratégies de décodage) sont des frontières de M28, qui les a préparés : MB4 n'y revient pas, et la "
                 "fiche renvoie à M28 §5 pour la température, top-k et top-p. MB4 travaille hors réseau et hors des "
                 "cadres de workbookIA : boulangeries et produits, relevés de stations météo, carnets de recettes et "
                 "ingrédients, jurys de concours de pâtisserie, listes de diagnostics ou d'objets perdus ; jamais un "
                 "LLM, une couche, un adaptateur, une matrice gelée, un passage indexé, un chunk, un embedding de "
                 "phrase, un prompt ni un document de workbookIA. "
                 "§1 (factorisation) : M = CF avec C les colonnes pivots de M et F les lignes non nulles de sa forme "
                 "échelonnée réduite (la factorisation CR), la non-unicité (CG)(G⁻¹F), le stockage r(m + n) et les "
                 "r(m + n − r) nombres libres (F a l'identité dans les colonnes pivots ; le compte redonne mn quand r = "
                 "min(m, n)). rang(CF) ≤ r est un rappel de ∂ M12a.18, jamais redémontré (c'est ∂ B4.6.1) : ∂ MB4.5 "
                 "démontre l'existence (une base de l'espace des colonnes et les coordonnées), la non-unicité à une G "
                 "inversible près (même espace des colonnes) et en déduit que le rang est le plus petit nombre de "
                 "produits extérieurs. Aucun exercice ni la fiche ne cherchent le rang à partir duquel la factorisation "
                 "cesse de faire gagner de la place (le seuil de ∂ B4.6.1 et de ✏️ B4.3 j, la demi-moyenne harmonique "
                 "dk/(d + k) ; M12d.5 en a déjà fait la version « image » : il n'est pas refait) : ✏️ MB4.1 compare des "
                 "nombres pour un tableau et un rang donnés, sans pourcentage d'un « modèle », sans liste de couches, "
                 "sans correction ajoutée à une matrice fixe, sans initialisation, gradient, facteur d'échelle ni « pas ». "
                 "La fiche peut dire, sans nombre, que le même compte r(m + n) vaut pour une correction de rang r, et que "
                 "workbookIA B4 l'applique (la fiche de M12d, qui promettait ce compte à MB4, est corrigée par le "
                 "coordinateur). "
                 "§2 : le rang effectif (part de l'énergie, plus petit rang pour une part donnée, rang stable) sur un "
                 "tableau de mesures donné par ses valeurs singulières, l'erreur par Eckart-Young (rappel, M12d.16) ; "
                 "pas de projection d'une matrice sur les sous-espaces singuliers d'une autre (📄 B4.11.8) ; C(Fx) contre "
                 "(CF)x est le rappel de M09a.4 (ordre des parenthèses) appliqué à une matrice factorisée, avec "
                 "l'arrondi des flottants (M05a), jamais W x + C(F x). Le 🏆 MB4.13 cherche un rang caché par un écart "
                 "dans les valeurs singulières (un seuil de bruit σ(√m + √n) peut être énoncé dans un 💻, admis), sans "
                 "refaire M12d.37 (une part d'énergie et une part de nombres imposées). "
                 "§3 et §4 (le poids d'un indice rare, la saturation, la normalisation) : des ingrédients dans N "
                 "fiches de recettes ; la surprise −ln(n/N) (M06), la cote, le poids de Robertson et Spärck Jones "
                 "ln[p(1 − q)/(q(1 − p))] tiré d'un tableau 2 × 2 (pertinent ou non, présent ou non), la correction ½ "
                 "de chaque case, le cas sans information de pertinence ln((N − n + ½)/(n + ½)) et son signe (démontré "
                 "en général dans ✏️ MB4.3 : négatif si et seulement si n > N/2, nul pour n = N/2), la variante "
                 "ln((N + 1)/(n + ½)) ; la saturation est étudiée comme une fonction (une prime qui plafonne, la "
                 "cinétique de Michaelis et Menten), la propriété s(1) = 1 pour tout k₁ est énoncée sur la courbe, "
                 "jamais sous la forme « une occurrence dans un document de longueur moyenne contribue exactement "
                 "l'idf » (la variante du corrigé de 🔨 B4.17) ; la saturation et la normalisation sont chiffrées seules, "
                 "comme des fonctions (valeurs en x = 1, 2, 10, rapport de la dixième mention à la première, effet de b "
                 "sur une fiche deux fois plus longue) ; jamais leur produit par un poids de rareté (une contribution de "
                 "BM25 : ✏️ B4.5 c-d, 🔨 B4.17), jamais le score d'une fiche à plusieurs ingrédients, jamais un "
                 "classement de fiches ni une longueur moyenne calculée sur un corpus (✏️ B4.5, 🔨 B4.17) ; k₁ ∈ {1, 2, "
                 "3} et b ∈ {¼, ½}, jamais le couple k₁ = 1,5, b = 0,75 ni k₁ = 1,2. Les erreurs fréquentes du corrigé "
                 "de ✏️ MB4.3 et le 🐛 n'ont aucune des erreurs listées par workbookIA pour ✏️ B4.5 et 🔨 B4.17 (le « 1 + » "
                 "oublié, n compté en occurrences, k₁ + 1 oublié, la longueur moyenne sur la requête). "
                 "§5 (fusion) : des jurys qui classent des pâtissiers (classements complets) ; la somme des notes "
                 "brutes change de gagnant quand un jury change d'échelle, la fusion par les rangs non (∂ MB4.6, "
                 "rappel de l'invariance de l'AUC, M03.23) ; Borda ; la somme des 1/(c + rang), avec une constante notée "
                 "c (k dans workbookIA B4 et chez Cormack et coll. : la fiche le dit une fois ; dans MB4, k est la "
                 "coupure de recall@k et k₁ la constante de saturation) ; ✏️ MB4.4 prend c = 2 et c = 10, jamais c = 0 "
                 "ni 60 ; ∂ MB4.6 démontre en général la condition j < c + 2 (deux listes contre une) et la limite quand "
                 "c grandit (développement 1/(c + j) = 1/c − j/c² + …, M05a), c = 0 n'y est qu'un cas limite, sans "
                 "nombres ; la seconde partie de ∂ MB4.6 porte sur des jurys qui ne classent que leurs premiers (un "
                 "candidat absent d'une liste ne reçoit rien de ce jury), en lettres, sans liste chiffrée, et la limite "
                 "de sa troisième partie (le nombre de listes) aussi ; aucun exercice ne fusionne des listes de "
                 "documents, des listes partielles chiffrées d'identifiants ni "
                 "les résultats de deux moteurs (🔨 B4.18, B4.Q9) ; la recherche dense est un rappel de la fiche "
                 "(cosinus, M07), sans exercice. Le 💼 porte sur des systèmes dont les échelles diffèrent, pas sur un "
                 "RAG. "
                 "§6 (mesurer un classement) : 🧠 MB4.Q4 définit recall@k, precision@k, taux de succès et MRR et "
                 "calcule leur valeur moyenne pour un ordre tiré au hasard (k/n, q/n, H_n/n) ; il ne demande ni si "
                 "recall@k est le taux de succès, ni si le MRR majore recall@1 (✏️ B4.2 f et h), et aucun exercice ne "
                 "calcule ces mesures sur des listes de requêtes ; la loi du premier pertinent, E[1/R] et l'encadrement "
                 "de H_n par des rectangles (M02a) sont dans la fiche, chiffrés dans 🔨 MB4.9 et le 🔮 MB4.10 (n = 10, "
                 "100, 1 000 : environ ln n / n) ; pas d'incertitude d'une proportion (B4.Q8, 📦 B4.20 : M08 suffit). "
                 "Le 🐛 MB4.12 : C pris dans la forme réduite au lieu de M (CF ≠ M), un classement lu comme la liste "
                 "des rangs des candidats (la permutation au lieu de son inverse), un poids de rareté écrit ln(n/N) ; "
                 "jamais les erreurs du corrigé de 🔨 B4.18 (rangs à partir de 0, recall divisé par k, argsort inversé, "
                 "identifiant répété). "
                 "Notations : M (m × n) de rang r (k en M12d et MB2 ; k est ici la coupure de recall@k), C (m × r), "
                 "F (r × n), produits extérieurs c fᵀ ; au §3, N fiches "
                 "et n fiches qui contiennent l'ingrédient ; au §4, k₁ ≥ 0, ℓ la longueur rapportée à la moyenne, "
                 "b ∈ [0, 1] ; au §5, des candidats, des rangs j à partir de 1, la constante c ≥ 0, n − j points de "
                 "Borda ; au §6, n objets dont q pertinents, R le rang du premier pertinent, H_n = 1 + 1/2 + … + 1/n. "
                 "`ranks` (pas `retrieval`, le nom du module `mylearn` de B4 : le « rang » d'une matrice et le "
                 "« rang » dans un classement, les deux moitiés du chapitre) : NumPy permis, `@` compris, rien de "
                 "`np.linalg`, ni SciPy (`scipy.linalg`, `scipy.stats.rankdata`), ni SymPy ; `random_ranking_mrr` "
                 "calcule en `fractions.Fraction` avec `math.comb`, sans énumérer les n! ordres (l'oracle des tests). "
                 "Aucune fonction n'a le contrat d'une fonction `mylearn` de B4 : pas d'idf ni de contribution BM25 "
                 "(d'où le retrait de `idf` et de `bm25_term_score` ; `rsj_weight` n'est pas retenue : une formule "
                 "d'une ligne, dont le cas r = R = 0 est l'idf original de ✏️ B4.5 i), pas de découpage, pas de "
                 "`cosine_top_k`, pas de fusion triée de listes partielles (la RRF), pas de recall@k ni de MRR "
                 "moyennés sur des requêtes ; `borda_scores` prend des classements complets et rend des points par "
                 "candidat, `random_ranking_mrr` une espérance exacte sous "
                 "un ordre tiré au hasard ; `rank_factorization` reprend le `rref` de M09a (l'apprenant peut l'importer de "
                 "`.matrices` ou le recopier : 🔨 MB4.8 passe en ★, 20 min) et les colonnes pivots de "
                 "`column_space_basis` (M12a), un rappel espacé assumé ; dans `borda_scores`, ni `np.argsort` ni "
                 "`np.lexsort` : l'apprenant inverse chaque classement lui-même (le 🐛 MB4.12 vise cette inversion) ; "
                 "`lora_param_count` est retirée (le nom de ∂ "
                 "B4.6, un contrat d'une ligne). MML : §4.6 (l'approximation de rang k comme somme de k matrices de "
                 "rang 1, Eckart-Young) a été lu en M12d (📖 M12d.22, questions 5 et 6) ; MB4 le donne en relecture "
                 "dans son guide et le rappelle par 🔁 MB4.R2 ; le livre ne traite ni l'idf, ni la fusion de "
                 "classements, ni les métriques de recherche (référence libre : Manning, Raghavan et Schütze, "
                 "Introduction to Information "
                 "Retrieval, ch. 6, 8 et 11, cités par chapitres). "
                 "COMPOSITION : chapitre court (7 h visées, 7,6 h) : 4 quiz, 3 rappels, 4 ✏️ et 2 ∂, 2 🔨, un 🔮, un 🎨, "
                 "un 🐛, un 🗣️, un 💼, un 🏆, 12 flashcards ; pas de 📖 (§4.6 lu en M12d, voir ci-dessus) ; pas de 🛠️ "
                 "(le test de propriété CF = M est celui de 🔨 MB4.8) ; pas de 🔗 (un calcul « du type de workbookIA B4 » "
                 "serait un compte de paramètres LoRA, un score BM25 ou une RRF : ses frontières) ; pas de 🔬 (le 🔮 "
                 "simule). Parcours essentiel : les quiz, les rappels, les quatre ✏️, ∂ MB4.5, le 🗣️ et 🔨 MB4.8 ; "
                 "∂ MB4.6, le 💼 et le reste du notebook hors parcours. **Durée** : 7,6 h au lieu de 7 (+0,6 h : "
                 "quatre lacunes, la factorisation de rang, l'origine probabiliste de l'idf, l'agrégation de "
                 "classements et la ligne de base au hasard, et des durées réalistes après les relectures de M25a à "
                 "M28) ; lecture 95 min (≈ 6 500 mots) ; sans 🎨 MB4.11 ni ∂ MB4.6, 7,0 h. "
                 "Évités (règle de partage), de workbookIA B4 : les modèles et leurs nombres (Qwen2.5-0.5B, "
                 "494 032 768, 24 couches, 896, 14/2 têtes, 32 768 ; SmolLM2-135M, 30 couches, 576, 9/3, 64, 49 152, "
                 "8 192, 134 515 008 ; Qwen3, 596 049 920, 28, 1 024, 16/8 ; distilgpt2, 81 912 576, 6, 768, 12/12, "
                 "1 024, 81 986 304 ; MiniLM, 22 713 216, 384, 256 ; e5, 117 653 760, 512 ; 268 098 176 ; "
                 "1 235 814 400 ; GPT-3, 12 288, 96 couches, 175 255,8 millions) ; le top-5 0,205 ; 0,104 ; 0,086 ; "
                 "0,065 ; 0,058 ; 2 000 milliards de tokens, 1,3 et 175 milliards, 700 millions ; 988 065 792 et "
                 "1 976 131 328 octets, 114 688 octets par token, 3,76 Go, 1,19 Go, 12 288 octets (B4.R1) ; les "
                 "formats 1/8/23 bits, 10^±38, 65 504, le groupe (0,12 ; −0,50 ; 0,31 ; 0,02), s = 0,50/127 et (30 ; "
                 "−127 ; 79 ; 5) ; 64 tokens, 8,4/8,7 s, 7,6/13,9 s, 8 tokens/s, 200 tokens en 25 s ; le train pour Lyon "
                 "(21 h 15, voie 7), le vote (Lyon, Lyon, Paris, Lyon, None) ; 540 et 100 milliards, 17,9 points, 76 "
                 "points ; 30 questions annotées, 70 % sur 50 (0,065, ± 13 points), 70 % contre 76 %, 80 % de 100 "
                 "(0,040), √(0,25/30) ≈ 0,09, ± 3,5 points sur 400 ; les troncatures 256 et 512 ; le découpage (13 mots "
                 "en morceaux de 5 avec un recouvrement de 2, débuts 0, 3, 6, 9 ; 200 et 50 ; 120 et 20, 1 045 morceaux "
                 "pour 104 500 mots, 21 mots ; « a b c d e f g h i j » (4, 2), « abcdefg » (3, 1)) ; les quatre "
                 "documents « holmes fume sa pipe »… (N = 4, longueur moyenne 4,75, poids ln 2 et 0,3567, 3,5066, "
                 "0,4942, 2,3224, 0,7462, (0,3840 ; 0,7485 ; 1,1301 ; 0), [2, 1, 0, 3]) ; les trois documents « nemo "
                 "commande le nautilus »… (longueurs 4, 3, 8, moyenne 5, ln(8/7) = 0,1335, ln(8/3) = 0,9808, 0,1628, "
                 "0,1599, 1,2246, 0,1908, 1,1144, 0,5108, −1,9459, −1,577, et la variante 1,2137 ; 0,1597 ; 0,1571 ; "
                 "0,1643) ; le corpus « the cat sat / the dog sat down / a cat and a cat » (moyenne 4,0, 0,47, 0,9808, "
                 "(0,5296 ; 0 ; 0,6215), (1,0592 ; 0,47 ; 0,6215)) et « violin music concert » (6,55 ; 5,87 ; 5,48 ; "
                 "5,83 ; 5,47) ; k₁ = 1,5 avec b = 0,75, k₁ = 1,2, « 1,2 à 2 » ; 20 à 100 résultats ; D = [[1, 3], [3, 1], "
                 "[1, 0], [−1, −1]] et la requête (1, 1) (0,8944 ; 0,7071 ; 0,1056), les documents [[1, 0], [0, 1], "
                 "[1, 1], [−1, 0]] et la requête (1 ; 0,2) (0,9806 ; 0,8321) ; a = (3, 4), b = (6, 8), cos 0,82 → 0,36, "
                 "50 000 × 768, 10 000 morceaux de dimension 384 ; la fusion avec k = 60, les classements [7, 2, 9, 4], "
                 "[2, 5, 7, 1], [9, 7, 3] et [3, 1, 2], [1, 2, 4] ([2, 7, 5, 9, 1, 4], [7, 2, 9, 5, 3, 1, 4], [1, 2, 3, "
                 "4], [1, 3, 2, 4]), 1/62 + 1/61, 1/61 + 1/63, 2/63 = 0,0317, 1/61 ≈ 0,0164, k = 0 → 1,5 et 1,33 ; les "
                 "trois questions (4, 8, 1, 3) {1}, (2, 6, 5, 0) {2, 9}, (7, 3, 0, 5) {6} (1/6, 0,5, 4/9), les cinq de "
                 "✏️ B4.2 ((3, 1, 4, 0, 2) {1}, (5, 9, 2, 6, 8) {2, 8}, (0, 7, 1, 2, 3) {0, 5}, (6, 4, 8, 9, 1) {7}, "
                 "(2, 0, 9, 3, 7) {3, 4, 9} ; 0,100 ; 0,467 ; 0,633 ; 0,433 ; 0,800 ; 0,533 ; 0,267) et celles des "
                 "docstrings ([[3, 1, 2], [0, 4, 5, 6]] avec [{1, 7}, {6}] : 0,25, 0,75, 0,375 ; [{9}, {0}] : 0,5) ; "
                 "recall@5 0,533 / 0,517 / 0,600 et MRR 0,452 / 0,500 / 0,523 ; 400 M, 100 mots, 21 millions, 5 ou 10 "
                 "passages, k de 3 à 10, 20 documents et 56,1 % ; 16 octets par paramètre (2 + 2 + 4 + 4 + 4), 9,5 Go, "
                 "7 milliards → 28 et 14 Go ; le rang 1 (1, 2, 3)ᵀ(2, 0, 1) = [[2, 0, 1], [4, 0, 2], [6, 0, 3]] et « 9 "
                 "nombres, 6 suffisent », g = (1, 2) et u = (3, 0, 1), l'application de ∂ B4.6 (d = 3, k = 2, r = 1, "
                 "α = 2, A₀ = (1, −1), x = (2, 1), g = (1, 0, −2), η = 0,1 ; (2, 0, −4), (−0,2 ; 0 ; 0,4), (−4, −2)) ; les "
                 "formes et rangs de LoRA (512 × 512 et r = 4 → 4 096 sur 262 144 ; 896 × 896, 896 → 128, 896 → 4 864 "
                 "et r = 8 → 14 336, 45 056, 1 081 344, 4 399 104, 540 672, 448 ; 1 024 → 2 048 et r = 16 → 49 152 sur "
                 "2 097 152 ; 4 096 × 4 096 et r = 8 → 65 536 au lieu de 16 777 216 ; d, k, r, α = 6, 4, 2, 4 ; 64 → 64 "
                 "et 64 → 16, r = 4, α = 8 → 832, 1 472, 1 664 ; 12 → 10 ; 768 × 2 304 ; r = 16, α = 32, 4 587 520 sur "
                 "600 637 440 ; 73 728 ; 38 019 et 38 404 ; r de 1 à 64, 18 432 → 1 179 648, 202 752, 294 912 ; "
                 "18 874 368, 37 748 736, 37,7 Mo, 4 718 592 ; r = 16 et α = 8 → 0,5 ; α/√r, 8/√64) ; 0,32 / 21,67 / "
                 "0,02, 6,91 et 21,5 ; les perplexités 48,34 → 37,81 et 40,07 à 34,62 ; 0,820 et 0,868 ; 17/30, K = 4, "
                 "12/30 ; 0,8¹⁵ ≈ 0,035 ; 1 € et 4 € par million, 1 700 et 23 € ; 3 000 questions, 1 540 tokens ; Holmes, "
                 "Watson, Baker Street, le violon et la pipe, Verne, le Nautilus et Nemo, « AX-7731 », 20 Newsgroups. "
                 "De ce dépôt : R6.12 (N = 2 000 documents, présents dans 20 et 200, tf 2 et 5), R9.13 (les vecteurs "
                 "d'ingrédients des crêpes, du quatre-quarts, des sablés et du pain au lait), M12d.5 (900 × 1 600, "
                 "k = 40), M12d.37 (93,5 % de l'énergie, 5 % des nombres), M03.23, les exemples des stubs `matrices`, "
                 "`linmaps` et `svd_pca`, et ceux du stub `ranks` ([[1, 3, 0, 1], [0, 0, 1, −1], [2, 6, 1, 1]], "
                 "[[2, −4], [−3, 6]], [[2, 0, 1], [0, 2, 1], [2, 1, 0]] → (3, 1, 5), [[3, 1, 0, 2]], 25/48, (5, 2) → "
                 "77/120, (4, profondeur 2) → 3/8), que ni la fiche ni les exercices ne reprennent ; et les Évités de "
                 "M28 (température, top-k, top-p).",
        "exercises": [
            ("MB4.Q1", "🧠", 1, 5, "Rang, factorisation et stockage : vrai ou faux, et le rang d'une somme de produits "
             "extérieurs", "§1 §2", "E"),
            ("MB4.Q2", "🧠", 1, 5, "Le poids d'un ingrédient rare, la saturation et la normalisation : signe, sens de "
             "variation, limites", "§3 §4", "E"),
            ("MB4.Q3", "🧠", 1, 5, "Fusionner des classements : ce que change une nouvelle échelle de notes, ce que "
             "change la constante c", "§5", "E"),
            ("MB4.Q4", "🧠", 1, 5, "recall@k, precision@k, taux de succès et MRR : définitions, et leurs valeurs pour un "
             "ordre tiré au hasard", "§6", "E"),
            ("MB4.R1", "🔁", 1, 6, "Le rang d'un produit, d'un produit extérieur et d'une somme (M12a)", "§1", "E"),
            ("MB4.R2", "🔁", 1, 6, "L'approximation de rang k par la SVD et son erreur de Frobenius (M12d, MML §4.6)",
             "§2", "E"),
            ("MB4.R3", "🔁", 1, 6, "L'information −ln p d'un événement, la cote et le logit (M06, R6)", "§3", "E"),
            ("MB4.1", "✏️", 2, 30, "Les ventes de quatre boulangeries sur cinq produits : le rang, la factorisation par "
             "les colonnes pivots, une seconde factorisation (CG)(G⁻¹F), et les nombres stockés ou libres", "§1", "E"),
            ("MB4.2", "✏️", 2, 25, "Un tableau de relevés de stations météo donné par ses valeurs singulières : énergie "
             "captée, rang effectif à 99 %, rang stable, puis le coût de C(Fx) et de (CF)x pour un et pour mille "
             "vecteurs", "§2", "E"),
            ("MB4.3", "✏️", 2, 30, "Les ingrédients d'un carnet de recettes : surprise, cote, poids corrigé par ½ et son "
             "signe, la variante toujours positive, puis la saturation et la normalisation d'une mention répétée",
             "§3 §4", "E"),
            ("MB4.4", "✏️", 2, 30, "Trois jurys classent cinq pâtissiers : les points de Borda, la somme des 1/(c + rang) "
             "pour c = 2 et c = 10, et la somme des notes qui change de gagnant quand un jury passe de 20 à 100 "
             "points", "§5", "E"),
            ("MB4.5", "∂", 2, 25, "Une matrice de rang r est un produit C F de r colonnes par r lignes ; deux telles "
             "factorisations diffèrent d'une matrice inversible ; le rang est le plus petit nombre de produits "
             "extérieurs dont elle est la somme", "§1", "E"),
            ("MB4.6", "∂", 2, 25, "Une fusion par les rangs ne change pas quand un jury change d'échelle ; j-ième pour "
             "deux jurys bat premier pour un seul si et seulement si j < c + 2 ; quand c grandit, la somme des "
             "1/(c + rang) range selon le nombre de listes, puis la somme des rangs", "§5", ""),
            ("MB4.7", "🗣️", 1, 10, "Expliquer à un pâtissier pourquoi un ingrédient présent dans toutes les recettes "
             "n'aide pas à retrouver la sienne, et pourquoi la dixième mention compte moins que la première", "§3 §4",
             "E"),
            ("MB4.E1", "💼", 1, 10, "« Comment combiner les classements de deux systèmes dont les scores ne sont pas sur "
             "la même échelle ? »", "§5", ""),
            ("MB4.8", "🔨", 1, 20, "La factorisation de rang C F : les colonnes pivots de M et les lignes non nulles de sa "
             "forme échelonnée réduite", "§1", "E m:rank_factorization"),
            ("MB4.9", "🔨", 2, 25, "Les points de Borda de classements complets, et le MRR exact d'un ordre tiré au "
             "hasard, en fractions", "§5 §6", "m:borda_scores,random_ranking_mrr"),
            ("MB4.10", "🔮", 1, 15, "Prédire le MRR d'un ordre tiré au hasard parmi 10, 100 puis 1 000 candidats, puis le "
             "simuler et le comparer à H_n/n", "§6", ""),
            ("MB4.11", "🎨", 1, 15, "Les courbes de saturation x ↦ x(k₁ + 1)/(x + k₁) de k₁ = 0 à l'infini, et ce que la "
             "normalisation par la longueur leur fait", "§4", ""),
            ("MB4.12", "🐛", 1, 15, "Chasse à l'erreur : C pris dans la forme réduite au lieu de M, un classement lu comme "
             "la liste des rangs des candidats, un poids de rareté écrit ln(n/N)", "§1 §3 §5", ""),
            ("MB4.13", "🏆", 3, 25, "Défi : retrouver le rang caché de cinq tableaux bruités, cinq fois sur cinq, par leurs "
             "valeurs singulières", "§2", ""),
        ],
    },
    {
        "id": "MB5", "dir": "mb5_diffusion", "hours": 15.7, "generation_sessions": 2, "mml": ["(§6.5)"],
        "summary": "Les outils mathématiques des modèles de diffusion, travaillés hors réseaux : les récurrences linéaires "
                   "gaussiennes (la loi sachant le départ, les produits cumulés, la loi stationnaire d'un processus "
                   "autorégressif), le pont d'une marche aléatoire et des trajectoires différentes aux mêmes lois "
                   "marginales, le rapport signal sur bruit (cotes, logit, décibels) et les cibles qui portent la même "
                   "information ; la MSE qui apprend l'espérance conditionnelle, le score en x et la formule de Tweedie (le "
                   "débruiteur optimal) ; l'ELBO d'une chaîne de variables latentes, démontrée ; la guidance comme produit de "
                   "puissances de densités ; les équations différentielles (méthode d'Euler, point milieu, ordre de "
                   "l'erreur) et le flow matching en dimension 1. workbookIA B5 s'en sert pour la forme fermée et les "
                   "plannings du processus de bruitage, la loss de prédiction du bruit, l'ELBO de la diffusion, DDIM, la "
                   "guidance sans classifieur et le flow matching.",
        "objectives": [
            "Calculer la loi de x_t sachant x_0 ou sachant x_s pour une récurrence linéaire gaussienne à coefficients "
            "quelconques, encadrer le produit cumulé de ses coefficients, et trouver la loi stationnaire d'un processus "
            "autorégressif d'ordre 1.",
            "Calculer la loi d'un instant sachant deux instants qui l'encadrent (le pont d'une marche aléatoire), et "
            "construire des trajectoires différentes qui ont les mêmes lois marginales.",
            "Passer du rapport signal sur bruit à la part de variance du signal (cotes, logit, décibels), et d'une "
            "estimation du bruit à une estimation du signal, avec l'erreur qui l'accompagne.",
            "Démontrer que l'erreur quadratique moyenne est minimale pour l'espérance conditionnelle, et en lire les "
            "conséquences sur une cible à plusieurs modes.",
            "Définir le score en x d'une densité, démontrer la formule de Tweedie, calculer le débruiteur optimal d'un "
            "signal gaussien ou d'un mélange, et dire comment la dynamique de Langevin tire des points d'une densité à "
            "partir de son score.",
            "Démontrer la décomposition de l'ELBO d'une chaîne de latents en reconstruction, KL finale et KL des pas "
            "retour, et la calculer sur une petite chaîne discrète.",
            "Écrire une combinaison affine de scores comme le score d'un produit de puissances de densités, et calculer la "
            "loi guidée de deux gaussiennes avec sa condition d'existence.",
            "Suivre une équation différentielle par la méthode d'Euler et par celle du point milieu, dans les deux sens du "
            "temps, et relier l'erreur au pas et à la courbure de la trajectoire.",
            "Calculer le champ moyen d'un chemin droit entre un bruit et des données gaussiennes de dimension 1, et le "
            "suivre pour transporter le bruit sur la loi des données.",
        ],
        "sections": [("§1", "Récurrences linéaires gaussiennes : la loi sachant le départ, les produits cumulés et la loi "
                            "stationnaire"),
                     ("§2", "Conditionner sur deux instants, changer de couplage : le pont d'une marche aléatoire, et des "
                            "trajectoires différentes aux mêmes lois marginales"),
                     ("§3", "Signal et bruit : rapport signal sur bruit, cotes et décibels, et trois cibles qui portent la "
                            "même information"),
                     ("§4", "La MSE apprend l'espérance conditionnelle"),
                     ("§5", "Le débruiteur optimal : le score en x, la formule de Tweedie, et la dynamique de Langevin "
                            "(aperçu)"),
                     ("§6", "L'ELBO d'une chaîne de variables latentes"),
                     ("§7", "Guider : combinaisons affines de scores et produits de puissances de densités"),
                     ("§8", "Équations différentielles : la méthode d'Euler, le point milieu, et l'erreur selon la "
                            "courbure"),
                     ("§9", "Le flow matching en dimension 1 : un chemin droit, un champ moyen, et le transport d'une loi")],
        "teaches": ["rappels de M25a et de M25b, sans les refaire : somme et image affine de gaussiennes indépendantes, "
                    "produit de deux densités gaussiennes, modèle linéaire gaussien et loi conditionnelle, KL entre deux "
                    "gaussiennes de même covariance ; espérance et variance conditionnelles, lois totales, responsabilités "
                    "en log, ELBO d'un latent",
                    "récurrence linéaire gaussienne x_t = a_t x_{t−1} + b_t ε_t à coefficients quelconques : x_t est une "
                    "image affine du vecteur gaussien (x_0, ε_1, …, ε_t) ; loi de x_t sachant x_0, de moyenne (a_1 ⋯ a_t) x_0 "
                    "et de variance Σ_k b_k² (a_{k+1} ⋯ a_t)² ; pour un coefficient constant, la loi sachant x_s ; "
                    "propagation des moments "
                    "m_t = a_t m_{t−1}, v_t = a_t² v_{t−1} + b_t² (la prédiction d'un filtre de Kalman de dimension 1)",
                    "produits cumulés : ln Π = Σ ln ; 1 − h ≤ e^{−h} (convexité, M05a) et ln(1 − h) ≥ −h − h² pour "
                    "0 ≤ h ≤ ½, d'où e^{−Σh_k − Σh_k²} ≤ Π(1 − h_k) ≤ e^{−Σh_k} ; risque cumulé et probabilité de survie à "
                    "des risques successifs",
                    "processus autorégressif d'ordre 1, x_t = a x_{t−1} + b ε_t : pour |a| < 1, loi stationnaire "
                    "N(0, b²/(1 − a²)) (somme géométrique, R5) et convergence depuis toute loi initiale (l'écart de moyenne "
                    "en |a|^t, celui de variance en a^{2t}) : le processus oublie son départ ; pour |a| ≥ 1, pas de loi "
                    "stationnaire (marche aléatoire, a = 1 : variance t b²) ; une chaîne de Markov à états continus (suite "
                    "de M26)",
                    "pont d'une marche aléatoire (a = 1) : loi de x_s sachant x_0 et x_T par le modèle linéaire gaussien de "
                    "M25a ; moyenne interpolée selon les variances cumulées V_s/V_T, variance V_s(V_T − V_s)/V_T, maximale "
                    "au milieu pour des pas égaux",
                    "lois marginales et couplages : deux processus peuvent avoir la même loi à chaque instant et des "
                    "trajectoires différentes ; si U et Z sont indépendants de loi N(0, 1) et 0 ≤ σ ≤ s, alors "
                    "√(s² − σ²) U + σ Z suit N(0, s²) ; réutiliser un seul tirage (des trajectoires déterministes) ou "
                    "ajouter un bruit frais ; la corrélation entre deux instants n'est pas fixée par les marginales ; une "
                    "loss qui ne voit qu'un instant à la fois ne dépend que des lois marginales (énoncé)",
                    "rapport signal sur bruit d'une mesure y = a x + b n (x et n indépendants, de variance 1) : SNR = a²/b², "
                    "part de variance du signal γ = a²/(a² + b²), SNR = γ/(1 − γ) (une cote), ln SNR = logit γ (R6), "
                    "décibels 10 log₁₀ SNR ; un seuil r de SNR correspond à γ = r/(1 + r) ; c·y a le même SNR que y",
                    "trois cibles qui portent la même information : connaissant y, estimer le bruit n ou le signal x revient "
                    "au même, x̂ = (y − b n̂)/a ; l'erreur sur x vaut l'erreur sur n divisée par √SNR ; une MSE sur x est une "
                    "MSE sur n pondérée par 1/SNR ; toute combinaison c x + d n non proportionnelle à y convient aussi",
                    "la meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + E[(E[Y | X] − g(X))²], le terme "
                    "croisé s'annulant par la propriété de la tour (M26) ; la MSE apprend l'espérance conditionnelle, et son "
                    "minimum est E[V(Y | X)] ; sur un échantillon, la moyenne de chaque groupe ; une cible à deux modes donne "
                    "une prédiction entre les modes ; la log-loss apprend la probabilité a posteriori (rappel de M27), la "
                    "MAE une médiane conditionnelle (énoncé)",
                    "score d'une densité en x, ∇ₓ ln p(x) = ∇p(x)/p(x) : il pointe vers les régions plus probables, s'annule "
                    "en un mode et ignore la constante de normalisation ; pour N(μ, σ²), −(x − μ)/σ² ; à ne pas confondre "
                    "avec le score en θ, ∇_θ ln p_θ(x), de MB8, ni avec le score d'un classement ou d'un classifieur (le sens "
                    "courant de MB2, MB3, MB4 et MB6)",
                    "formule de Tweedie : pour y = a x + b n, avec n de loi N(0, 1) indépendant de x de loi quelconque, "
                    "E[x | y] = (y + b² (ln p_Y)′(y))/a et E[n | y] = −b (ln p_Y)′(y) (démontrée en dimension 1 en dérivant "
                    "p_Y sous l'espérance, énoncée en dimension d avec le gradient) ; estimer le bruit, c'est estimer le "
                    "score de la loi bruitée",
                    "débruiteur optimal d'un mélange de gaussiennes : responsabilités en log (une softmax, M25b) et moyennes "
                    "a posteriori de chaque composante (M25a) ; pour un nuage de points (variances nulles) et a ≠ 0, il rend "
                    "le point le plus proche de y/a quand le bruit tend vers 0 (il recopie les données ; à égale distance "
                    "de deux points, une moyenne pondérée des deux) ; pour a = 0, la moyenne du nuage",
                    "dynamique de Langevin (aperçu) : x_{k+1} = x_k + (h/2) (ln p)′(x_k) + √h ε_k, une chaîne de Markov à "
                    "états continus dont la loi stationnaire approche p quand h → 0 ; pour p = N(μ, σ²), c'est un processus "
                    "autorégressif d'ordre 1 (§1) de coefficient 1 − h/(2σ²) et de loi stationnaire "
                    "N(μ, σ²/(1 − h/(4σ²))) : partir d'un bruit et laisser converger la chaîne fabrique des tirages de p",
                    "ELBO d'une chaîne de latents : un processus aller q(z_1 | x) q(z_2 | z_1) ⋯ q(z_T | z_{T−1}), "
                    "markovien et fixé, un modèle retour p(z_T) p(z_{T−1} | z_T) ⋯ p(x | z_1) ; chaque pas aller réécrit "
                    "par Markov et Bayes, q(z_t | z_{t−1}, x) = q(z_{t−1} | z_t, x) q(z_t | x)/q(z_{t−1} | x), puis le "
                    "télescopage : ELBO = E_q[ln p(x | z_1)] − KL(q(z_T | x) ‖ p(z_T)) − "
                    "Σ_{t≥2} E_q[KL(q(z_{t−1} | z_t, x) ‖ p(z_{t−1} | z_t))] (démontrée, suite de M25b §5)",
                    "lecture des termes : une reconstruction, une KL finale sans paramètre quand p(z_T) est fixée, et pour "
                    "chaque pas retour une KL contre le pas retour qui connaît x ; quand ces lois sont gaussiennes de même "
                    "variance fixée σ², chaque KL vaut ‖μ_q − μ_p‖²/(2σ²) (M25a §7) : une MSE pondérée des moyennes, dont "
                    "une loss simplifiée retire les poids (idée)",
                    "combinaison affine (1 + w) u − w v = u + w (u − v) : w ∈ [−1, 0] interpole, w > 0 extrapole au-delà "
                    "de u, à l'opposé de v (un barycentre à coefficients hors de [0, 1], M07)",
                    "Bayes en log : ∇ₓ ln p(x | c) − ∇ₓ ln p(x) = ∇ₓ ln p(c | x) ; (1 + w) ∇ ln p_c − w ∇ ln p_u = "
                    "∇ ln(p_c^{1+w} p_u^{−w}) : une combinaison affine de scores est le score d'un produit de puissances de "
                    "densités, p_c · p(c | x)^w à une constante près",
                    "produit de puissances de deux densités gaussiennes de dimension 1 : précision (1 + w)/σ_c² − w/σ_u², "
                    "positive pour tout w ≥ 0 si σ_c ≤ σ_u, sinon jusqu'à un w limite au-delà duquel il n'y a plus de "
                    "densité ; moyenne poussée au-delà de μ_c, à l'opposé de μ_u ; loi plus étroite que p_c quand "
                    "σ_c < σ_u, plus large sinon ; avec une loi générale à plusieurs bosses, la masse quitte les autres "
                    "bosses",
                    "équation différentielle x′(t) = f(t, x) à champ dépendant du temps : condition initiale, trajectoire, "
                    "existence et unicité pour f lipschitzienne en x (théorème de Cauchy-Lipschitz, énoncé) ; solutions "
                    "exactes de x′ = g(t) (une primitive), du refroidissement x′ = −k(x − c) et de la croissance "
                    "logistique",
                    "méthode d'Euler pour un champ dépendant du temps (suite de M20 §6), dans les deux sens du temps (un pas "
                    "négatif pour remonter) ; exacte pour une vitesse constante le long de la trajectoire ; erreur d'un pas "
                    "½ h² x″(ξ) (Taylor, M05a), qui vient de la courbure ; erreur au temps final d'ordre h (énoncée, avec "
                    "l'idée de l'accumulation de T/h erreurs locales) ; pour x′ = g(t), Euler est la somme de Riemann à "
                    "gauche et le point milieu la règle du point milieu (M02a)",
                    "méthode du point milieu : un demi-pas d'Euler, puis la vitesse lue au milieu ; deux évaluations du "
                    "champ par pas, exacte pour une vitesse affine en t, erreur d'ordre h² (énoncée) ; comparer deux "
                    "méthodes à nombre d'évaluations égal ; pentes 1 et 2 en échelle log-log",
                    "chemin droit entre une donnée x_0 et un bruit ε, x_s = (1 − s) x_0 + s ε (s = 0 : la donnée, s = 1 : "
                    "le bruit) : vitesse ε − x_0, constante sur chaque chemin ; une mesure de gains 1 − s et s, de SNR "
                    "((1 − s)/s)² (§3) ; x_0 = x_s − s u et ε = x_s + (1 − s) u pour u = ε − x_0",
                    "champ moyen v(x, s) = E[ε − x_0 | x_s = x] = (x − E[x_0 | x_s = x])/s, appris par la MSE (§4) et "
                    "calculé par le débruiteur du §5 ; l'équation x′ = v(x, s), suivie de s = 1 à s = 0, transporte la loi "
                    "de ε sur celle de x_0 (énoncé, vérifié pour des données gaussiennes) ; pour x_0 de loi N(m, τ²), v est "
                    "affine en x, les trajectoires sont x(s) = (1 − s) m + σ(s) z avec σ(s)² = (1 − s)² τ² + s², courbes "
                    "dès que τ > 0 ; un seul pas d'Euler depuis s = 1 rend m pour tout départ ; pour deux points, le champ "
                    "n'est plus affine"],
        "requires": [("suite géométrique et sa somme, somme infinie", "R5"),
                     ("logarithme d'un produit, log₁₀, tanh, cote et logit", "R6"),
                     ("dérivée, tangente", "R7"),
                     ("primitive, intégrale, sommes de Riemann à gauche et au point milieu", "M02a"),
                     ("loi normale, densité, variance d'une transformation affine et d'une somme de variables "
                      "indépendantes", "M02b"),
                     ("formule de Bayes, probabilités totales", "M04"),
                     ("convexité : une fonction convexe est au-dessus de ses tangentes ; polynôme de Taylor d'ordre 2 et "
                      "son reste ; ln(1 + x) ≈ x", "M05a"),
                     ("divergence KL discrète, entropie", "M06"),
                     ("barycentre ; la moyenne minimise la somme des carrés des écarts", "M07"),
                     ("MSE, risque empirique", "M09b"),
                     ("(1 + x/n)ⁿ → eˣ", "M14"),
                     ("méthode d'Euler pour x′ = F(x), application proche de l'identité", "M20"),
                     ("récurrence linéaire avec entrée ; Aᵗ → 0 quand le rayon spectral est inférieur à 1", "M22"),
                     ("transformations affines et sommes de gaussiennes indépendantes, produit de deux densités "
                      "gaussiennes, modèle linéaire gaussien, loi conditionnelle, KL continue et KL entre deux gaussiennes",
                      "M25a"),
                     ("graphe orienté et chaîne, tirage ancestral, espérance et variance conditionnelles, lois totales, "
                      "mélanges et responsabilités en log, ELBO d'un latent, dériver sous l'espérance", "M25b"),
                     ("chaîne de Markov, loi stationnaire, propriété de la tour", "M26"),
                     ("meilleur prédicteur pour la log-loss ; distance de Wasserstein entre deux lois de dimension 1 et "
                      "entre deux gaussiennes", "M27")],
        "frontieres": ["B5.1", "B5.2", "B5.3", "B5.4", "B5.5", "B5.11", "B5.12", "B5.13", "B5.14", "B5.15", "B5.16", "B5.17",
                       "B5.18", "B5.20", "B5.22", "B5.26", "B5.28", "B5.Q2", "B5.Q3", "B5.Q4", "B5.Q8", "B5.Q9",
                       "B5.Q11", "B5.R3", "B5.E2", "B5.E4", "B5.E5"],
        "mymath": {"module": "gaussian_paths.py",
                   "functions": ["linear_gaussian_recursion", "posterior_mean_mixture", "euler_ode", "midpoint_ode"]},
        "reading_minutes": 160,
        "flashcards": 20,
        "notes": "Frontières : les ∂ B5.6 (deux pas de bruit gaussien n'en font qu'un, la forme fermée q(x_t | x_0) par "
                 "récurrence, la variance préservée, la variance qui explose sans le facteur d'atténuation, x_t | x_s ; déjà "
                 "frontière de M25a et de CP6) et B5.7 (le posterior q(x_{t−1} | x_t, x_0) en dimension 1 : Bayes et Markov, "
                 "les précisions, l'identité α_t(1 − ᾱ_{t−1}) + β_t = 1 − ᾱ_t, la substitution de x̂_0 qui donne la moyenne "
                 "de l'algorithme 2 ; ∂ MB5.13 en écrit l'étape « Bayes et Markov », pour des latents quelconques et sans loi "
                 "gaussienne de pas : c'est l'outil de l'ELBO d'une chaîne promise par M25b, voir §6) ; le ✏️ B5.1 (la combinaison (1 + w) ε_c − w ε_∅ de deux vecteurs pour w = 0, 1, 3, "
                 "puis −1 et −0,5, et le coût de deux passes), le ✏️ B5.2 (un planning linéaire à T = 4, ses produits "
                 "cumulés, Σβ et e^{−Σβ}, T = 400 et 1 000, des bornes mises à l'échelle, et dans la copie ln(1 − β) ≤ −β), "
                 "le ✏️ B5.3 (le SNR des plannings linéaire et cosinus, les seuils 1 et 0,1 d'un chiffre lisible, la part "
                 "des pas entre deux seuils), les ✏️ B5.4 et B5.5 (un pas DDPM et un pas DDIM à la main, β̃, l'écrêtage, "
                 "la famille η), le 📄 B5.11 (Ho et coll. : les poids de l'équation 12, les deux choix de σ_t² et leurs cas "
                 "extrêmes), les 🔨 B5.12, B5.14, B5.16 et B5.17 (les plannings, `q_sample`, le posterior, x̂_0, les pas "
                 "DDPM et DDIM de `mylearn`), le 🔮 B5.13 (l'allure d'un chiffre bruité aux pas 100, 300 et 600, et son SNR), le 📈 B5.15 (lire ᾱ_t et le "
                 "SNR de deux plannings), le 🔬 B5.18 (l'aller-retour "
                 "exact avec le vrai bruit), le 🔬 B5.20 (flow matching contre DDIM en 2D, Euler à 1, 2, 5, 10, 20, 50 et "
                 "100 pas, la vitesse prise au milieu de l'intervalle), le 🐛 B5.22 (les quatre bugs d'indices, de racines "
                 "et d'échelle, le débruiteur parfait), le 🔮 B5.26 (l'effet de w sur la netteté et la diversité), le "
                 "🔬 B5.28 (la mémorisation mesurée par le rapport r des plus proches voisins), les quiz B5.Q2 (un "
                 "débruitage en un seul coup, trois cibles équiprobables, 2 000 pas), B5.Q3 (ᾱ_t = 0,64), B5.Q4 (x̂_0, la "
                 "cible commode, la v-prédiction), B5.Q8 (DDIM), B5.Q9 (la guidance) et B5.Q11 (le flow matching), le "
                 "rappel B5.R3 (la KL contre N(0, 1)) et les 💼 B5.E2 (pourquoi prédire le bruit), B5.E4 (le compromis de "
                 "la guidance) et B5.E5 (diffusion ou flow matching). "
                 "MB5 travaille hors réseau : l'anomalie de température d'un lac, la survie d'une ruche, un phoque balisé "
                 "et des scénarios de position, un enregistrement de voix, des prix d'appartements, un signal reçu, un bit "
                 "relayé, la date de floraison d'un verger, une tasse de thé qui refroidit, une population qui croît, des "
                 "relevés de mesures, une loi à deux bosses ; jamais une image, un pixel, un réseau, un débruiteur appris, "
                 "un pas de temps de diffusion, β_t, α_t, ᾱ_t, ε_θ, x̂_0, un planning nommé (linéaire de Ho, cosinus de "
                 "Nichol et Dhariwal), ni un pas DDPM ou DDIM calculé. "
                 "**Garde-fous de M25a, repris** : jamais un couple de coefficients a² + b² = 1 dans un exercice, un "
                 "exemple, une docstring ou un test (il recomposerait x ↦ √α x + √(1 − α) ε ; le cas b² = 1 − a², variance "
                 "stationnaire 1, est seulement énoncé, en une phrase, sans nombre ni composition de deux pas) ; jamais la "
                 "KL contre N(0, 1), N(0, I) ou N(0, τ²) ; jamais la forme fermée de q(x_t | x_0) ni le posterior du pas. "
                 "**§1** : la récurrence est démontrée pour des coefficients quelconques (∂ MB5.10 : un énoncé plus général "
                 "que ∂ B5.6, BIBLE §8), jamais spécialisée à √(1 − β_t), sans « deux pas n'en font qu'un » ni variance "
                 "« préservée » ; ✏️ MB5.1 prend un coefficient constant |a| < 1 et un b² ≠ 1 − a², jamais a = 0,8, 0,6 ou "
                 "0,9 (√0,64, √0,36, √0,81 de workbookIA) ; ✏️ MB5.2 (la survie) prend des risques qui ne sont pas en "
                 "progression arithmétique, un nombre de périodes fixé (jamais « le même risque cumulé réparti sur plus de "
                 "périodes », B5.2 j-l, B5.Q2 e), et demande l'encadrement par deux exponentielles, pas l'écart relatif de "
                 "e^{−Σh} seule ; 1 − h ≤ e^{−h} est un rappel (M20 §6 écrit 1 + u ≤ e^u). Le 🔨 MB5.16 propage les "
                 "moments (m_t, v_t) depuis une loi initiale quelconque : avec mean0 = 1 et var0 = 0, les moyennes sont des "
                 "produits cumulés, mais la fonction ne prend jamais de β et ne rend aucune sortie nommée ᾱ ou √ᾱ ; ses "
                 "tests ne lui passent jamais un β ni des coefficients √(1 − β_t), √β_t. Ni la fiche, ni un exercice, ni "
                 "une solution, ni un test n'écrit l'identité Σ_k b_k² Π_{j>k} a_j² = 1 − Π a_j² quand b_k² = 1 − a_k², ni "
                 "1 − v_t = a_t²(1 − v_{t−1}) (le cœur de ∂ B5.6.2 et ∂ B5.6.7) ; les tests de "
                 "`linear_gaussian_recursion` n'emploient jamais a_t² + b_t² = 1 ; la loi sachant un instant passé n'est "
                 "demandée que pour un coefficient constant (✏️ MB5.1, ∂ MB5.10), et la docstring ne dit pas comment "
                 "l'obtenir avec la fonction (l'indication de ∂ B5.6.7). "
                 "**§2** : le pont est celui d'une marche aléatoire (a = 1), jamais d'une récurrence atténuée (ce serait "
                 "∂ B5.7 avec d'autres coefficients) ; il s'obtient par le modèle linéaire gaussien de M25a, sans "
                 "« coefficient de x_0 et de x_t » ; les couplages sont un lemme général (√(s² − σ²) U + σ Z) appliqué à des "
                 "scénarios de position ; l'usage qu'en fait DDIM (mêmes lois marginales, donc même entraînement) est "
                 "énoncé dans l'encadré 🔗 de la fiche, sans σ de la famille η, sans « η = 1 donne β̃ » (B5.Q8) ni "
                 "aller-retour avec le vrai bruit (B5.18). "
                 "**§3** : y = a x + b n avec a² + b² ≠ 1 ; la normalisation y/√(a² + b²) est énoncée sans être écrite "
                 "√γ x + √(1 − γ) n ; ✏️ MB5.4 prend des seuils en décibels autres que la paire « SNR 1 et 0,1 » et aucune "
                 "courbe de SNR le long d'un planning (B5.3, B5.13, B5.15) ; retrouver le signal à partir d'une estimation du "
                 "bruit se fait sur la voix, jamais avec ᾱ (B5.Q4 b) ; la v-prédiction de Salimans et Ho n'est pas "
                 "enseignée, et la « vitesse » n'apparaît qu'au §9 ; aucun quiz « la somme des deux coefficients vaut-elle "
                 "1 ? » (B5.Q3 c) ni « le bruit est une cible commode parce que… » (B5.Q4 d). "
                 "**§4** comble une lacune générale (« la MSE apprend une moyenne », que workbookIA B5 attribue au "
                 "chapitre 9 et qu'aucun chapitre publié ne démontre) : ∂ MB5.11 pour X discrète, sur les prix "
                 "d'appartements selon le quartier (la fiche) ; aucun quiz à trois cibles équiprobables, aucun débruitage « en "
                 "un seul coup » qui rend une image floue (B5.Q2 a-c) ; le 💼 MB5.E1 est une question de régression. "
                 "**§5** : le score est défini **en x** ; la fiche prévient que MB8 appellera score ∇_θ ln p_θ(x) (la "
                 "méthode du score, nommée en M25b §7), et qu'ailleurs « score » a son sens courant, un score de classement "
                 "ou de pertinence (MB2, MB3, MB4) ou le score S d'un classifieur (MB6) : une ligne ⚠️ de la fiche "
                 "distingue les trois sens ; un paragraphe « dynamique de Langevin (aperçu) », sans exercice, tient la "
                 "promesse de M26 (une chaîne de Markov qui converge vers sa loi stationnaire pour fabriquer des données) : "
                 "pour p = N(μ, σ²), un AR(1) de coefficient 1 − h/(2σ²), où a² + b² = 1 + h²/(4σ⁴) ≠ 1 (compatible avec "
                 "le garde-fou), sans chiffre ni lien avec B5.E2, qui ne fait que nommer Langevin ; ∂ MB5.12 démontre Tweedie en dimension 1 (dériver sous "
                 "l'espérance, M25b §7 ; une somme finie pour un x discret) ; ✏️ MB5.5 : un signal gaussien (Tweedie "
                 "contre M25a), puis un signal à deux niveaux ±c équiprobables (une tanh), et la limite b → 0 ; la fiche en "
                 "déduit « estimer le bruit, c'est estimer le score de la loi bruitée », sans le facteur √(1 − ᾱ_t), sans "
                 "« pourquoi le réseau prédit le bruit plutôt que l'image » (B5.E2) ; le 🔮 MB5.20 prend cinq relevés de "
                 "dimension 1, de poids égaux, inégalement espacés : quand le bruit tend vers 0, le débruiteur recopie le "
                 "relevé le plus proche, et rend la moyenne de deux relevés pour une mesure à égale distance des deux ; "
                 "sans rapport r, sans seuil 1/3 ni 1/2, sans image (B5.22, B5.28) ; la docstring de "
                 "`posterior_mean_mixture` ne dit rien de la limite b → 0. "
                 "**§6** comble ce que M25b a laissé à MB5 : ∂ MB5.13 démontre la décomposition (admise par workbookIA B5, "
                 "fiche 205.4) pour des latents discrets ou continus ; ✏️ MB5.6 la calcule sur une chaîne binaire de deux "
                 "pas (un bit altéré par deux relais, des tables données ; d'autres nombres que la chaudière de M25b) ; "
                 "✏️ MB5.6 donne la probabilité d'altération de chaque relais, calcule q(z₂ | x) comme le produit de deux "
                 "matrices 2 × 2 (M26) et q(z₁ | z₂, x) par une table de Bayes ; il ne demande ni la loi de z_T pour T "
                 "quelconque, ni sa limite, ni une formule fermée de la composition de T relais ; ∂ MB5.13 écrit, pour des "
                 "latents quelconques, l'étape « Bayes et Markov » de ∂ B5.7.1 : c'est l'outil de l'ELBO promise par M25b, "
                 "accepté, sans aucune loi gaussienne de pas ; aucune chaîne gaussienne n'est calculée (le posterior d'un "
                 "pas serait ∂ B5.7) ; la KL de deux gaussiennes "
                 "de même variance comme MSE pondérée s'énonce avec un σ² général, sans β_t, α_t ni ᾱ_t, sans aucun poids "
                 "d'article (📄 B5.11 : β_t²/(2σ_t²α_t(1 − ᾱ_t)), β_t/(2α_t(1 − ᾱ_t)), 0,50, 0,010, 0,0055) et sans le nom "
                 "L_simple. "
                 "**§7** : ✏️ MB5.7 travaille sur des densités (deux lois gaussiennes de dates de floraison), jamais sur la "
                 "combinaison de deux prévisions calculée pour plusieurs w (B5.1, B5.Q9), ni sur les conventions s = 1 + w "
                 "(B5.E4), ni sur un compromis fidélité contre diversité (B5.E4, B5.26) ; MB5.Q7 n'a aucun item « w = 0 "
                 "redonne… » ni « w = −1 redonne… » (B5.1 a et f) ; le 🎨 MB5.22 prend une loi générale à deux bosses de "
                 "dimension 1, des w hors de {0, 1, 3, 7}, de 0,5 et de 2, sans écart-type moyen d'un nuage. "
                 "**§8** : MB5.Q8 n'a aucun item « vitesse constante ⇒ un pas suffit » (B5.Q11 d) ; la propriété reste dans "
                 "la fiche, dans ✏️ MB5.8 (le courant) et dans la docstring d'`euler_ode` ; ✏️ MB5.8 (le refroidissement "
                 "d'une tasse de thé) n'emploie ni x′ = x ni la suite 2 ; 2,25 ; "
                 "2,441 ; 2,594 (fiche de workbookIA B5), ni λ = −0,5 et la rotation de M20 ; le 📦 MB5.19 suit une "
                 "croissance logistique ; le 🐛 MB5.23 n'a aucune des erreurs du corrigé de B5.20 (un pas d'Euler dans le "
                 "mauvais sens, s tiré dans [0, 1), la cible x_0 − ε) ni de B5.22 (l'échelle, l'indice, la racine, le bruit "
                 "au dernier pas) : ses trois erreurs sont des poids inversés dans un pont, des responsabilités calculées "
                 "avec la variance du signal seule (sans le bruit), et un temps qui n'avance pas dans un Euler (invisible "
                 "sur un champ qui ne dépend pas du temps). "
                 "**§9** : x_0 de loi N(m, τ²) en dimension 1, temps s = 0 pour la donnée et s = 1 pour le bruit (la "
                 "convention de workbookIA B5) ; le ✏️ MB5.9 et le 🔬 MB5.21 suivent le champ moyen exact avec 1, 2, 4, 8, "
                 "16 et 32 pas (des puissances de 2), sans comparaison à DDIM, sans anneau, sans MLP, sans « vitesse prise au "
                 "milieu de l'intervalle » (variante de B5.20 ; le point milieu du §8 est la méthode d'ordre 2) ; le "
                 "🏆 MB5.25 transporte N(0, 1) vers un mélange de deux gaussiennes de dimension 1 par son champ moyen "
                 "exact (`posterior_mean_mixture`), avec un budget d'évaluations du champ et une distance de Wasserstein "
                 "(M27) mesurée sur un grand échantillon. "
                 "**Partage** : M25a a les sommes, les images affines, le produit de densités, le modèle linéaire gaussien, "
                 "le conditionnement et la KL entre gaussiennes ; M25b la chaîne et le tirage ancestral, l'espérance et la "
                 "variance conditionnelles, les responsabilités, l'ELBO d'un latent et la dérivée d'une espérance ; MB5 "
                 "les rappelle (🔁 MB5.R1, MB5.R2) sans les redémontrer. MB8 garde la méthode du score (en θ). Promesses "
                 "tenues : M25a (« MB5 enchaîne produits et sommes de gaussiennes », « MB5 conditionne une loi gaussienne "
                 "pour les modèles de diffusion »), M25b (« MB5 écrira l'ELBO d'une chaîne de latents »), M26 (« MB5 fera "
                 "converger une chaîne de Markov vers sa loi stationnaire pour fabriquer des données » : l'AR(1) du §1 et la "
                 "dynamique de Langevin du §5), M20 (Euler, premier contact). Une ligne ⚠️ de la fiche : la diffusion des "
                 "modèles génératifs, pas la diffusion (*broadcasting*) des tableaux de M20. Les trois notions « locales » de workbookIA B5 (somme de gaussiennes indépendantes, "
                 "produit de deux densités en dimension 1, méthode d'Euler pour suivre un champ de vitesses) sont "
                 "couvertes : les deux premières par M25a, la troisième par M20 et MB5. "
                 "**Conventions** : N(μ, v) avec une variance ; un bruit ε (ou n) de loi N(0, 1), indépendant du reste ; "
                 "un champ f(t, x), le temps d'abord, comme SciPy ; logarithmes népériens, KL en nats ; la dimension 1 "
                 "partout, sauf l'énoncé de Tweedie en dimension d. `gaussian_paths` : NumPy et `math` seulement, aucune "
                 "SciPy (`solve_ivp`, `odeint`, `quad`, `norm`, `logsumexp`, `softmax` sont les oracles des tests) ; les "
                 "imports relatifs de ses propres modules sont permis (`approx.logsumexp`, M05a) ; "
                 "`linear_gaussian_recursion(a, b, mean0, var0)` rend (moyennes, variances) de x_0 à x_T (oracles : "
                 "simulation à graine fixe, la récurrence en `fractions` sur de petits cas) ; "
                 "`posterior_mean_mixture(y, a, b, weights, means, variances)` rend E[x | y] pour y = a x + b n et x un "
                 "mélange de gaussiennes de dimension 1, des variances nulles permises (des points), a = 0 permis (la "
                 "moyenne du mélange), b > 0 (oracles : `scipy.integrate.quad` sur la loi a posteriori, Tweedie par "
                 "différences finies de ln p_Y) ; `euler_ode(f, x0, t0, t1, n_steps)` et `midpoint_ode` rendent les "
                 "n_steps + 1 points, t1 < t0 permis (oracles : `solve_ivp` à tolérance serrée, solutions exactes, rapports "
                 "d'erreurs 2 et 4). Aucune n'a le nom ni le contrat d'une fonction de `mylearn/diffusion.py` (pas de β, pas "
                 "de dictionnaire de constantes, pas de tirage, pas de x̂_0, pas de pas d'échantillonnage) ; la boucle de "
                 "B5.20 (`x - (1/n_steps) * v_model(x, k/n_steps)`) n'est pas le contrat d'`euler_ode`. Les exemples du "
                 "stub ne reviennent dans aucun exercice : les coefficients (0,5 ; 2 ; 1) et (1 ; 0 ; 3) depuis 4, (0,5) et "
                 "(−1) depuis N(2, 8) ; le mélange (0,3 ; 0,7) aux points −1 et 2, N(2, 3) avec a = b = 1, a = 0 avec b = 2 ; x′ = 2t + 1 "
                 "de t = 1 à 3 en 4 pas, x′ = 2, x′ = −x/4 de t = 2 à 0 depuis (4, −8) (les exemples x′ = t sur [0, 1] en "
                 "4 pas étaient ceux de `riemann_sum`, M02a, et sont écartés). "
                 "**Écarts au plan** : le module s'appelle `gaussian_paths.py`, pas `diffusion.py` (le nom du module "
                 "`mylearn` de B5) ; `cumulative_alpha` (le contrat de `noise_schedule(betas)[\"alpha_bars\"]`), "
                 "`combine_gaussians` et `gaussian_product_1d` (déjà en M25a §2 et §5, et l'outil de ∂ B5.7) sont "
                 "retirées ; `linear_gaussian_recursion`, `posterior_mean_mixture` et `midpoint_ode` ajoutées ; "
                 "`guided_gaussian` n'est pas retenue (deux lignes de précisions, faites à la main en ✏️ MB5.7 et sur une "
                 "grille dans le 🎨 MB5.22) ; les « plannings de bruit (linéaire, cosinus) » deviennent les produits "
                 "cumulés et le SNR, et s'ajoutent la récurrence générale et la loi stationnaire, le pont et les couplages, "
                 "la MSE et l'espérance conditionnelle, Tweedie et le score en x, le point milieu et l'ordre de l'erreur. "
                 "**MML** : (§6.5), en relecture : §6.5.1 (marginales et conditionnelles) et §6.5.3 (sommes et "
                 "transformations linéaires) avant les §1 et §2, §6.5.2 (produit de densités) avant le §7 ; MML n'a ni "
                 "équations différentielles, ni processus autorégressif, ni diffusion. Lectures libres, citées par "
                 "chapitres : Blitzstein et Hwang, ch. 9 (l'espérance conditionnelle et la prédiction) ; B. Efron, "
                 "« Tweedie's Formula and Selection Bias », JASA, 2011 ; Süli et Mayers, *An Introduction to Numerical "
                 "Analysis*, le chapitre sur les problèmes aux valeurs initiales ; Shumway et Stoffer, *Time Series "
                 "Analysis and Its Applications*, ch. 3 (les modèles AR) ; jamais Weng 2021 ni Luo 2022, sources de "
                 "workbookIA B5. COMPOSITION : pas de 📖 (§6.5 est lu en entier en M25a, avec le 📖 M25a.17, et le reste du "
                 "chapitre n'est pas dans MML) ; un seul 💼 ; 9 ✏️ et 4 ∂ ; 3 🔨 et un 📦 ; un 🔬 et un 🔮. Parcours "
                 "essentiel : sans ✏️ MB5.3 (pont et couplages), ∂ MB5.12 et MB5.13, le 💼, le 📦, le 🎨, le 🛠️ et le 🏆. "
                 "**Durée** : 15,7 h (essentiel 12,3 h ; lecture 160 min, dont 5 pour le paragraphe sur Langevin et les "
                 "lignes ⚠️ ajoutés après relecture), pour 14 h au plan et 15 h visées : neuf sections, dont trois "
                 "lacunes générales (la MSE et l'espérance conditionnelle, Tweedie et le score en x, les EDO au-delà d'Euler) "
                 "et l'ELBO d'une chaîne démontrée ; durées comptées pour un apprenant qui rédige. Deux sessions de "
                 "génération : §1 à §5 (🔨 MB5.16 et MB5.17), puis §6 à §9 (🔨 MB5.18). "
                 "**Évités** (règle de partage, et reprises de ce dépôt) : les plannings jouets β = (0,02 ; 0,04 ; 0,06 ; "
                 "0,08 ; 0,10) (ᾱ = 0,98 ; 0,9408 ; 0,8844 ; 0,8136 ; 0,7322 ; √ᾱ = 0,9899 ; 0,9700 ; 0,9404 ; 0,9020 ; "
                 "0,8557 ; √(1 − ᾱ) = 0,1414 ; 0,2433 ; 0,3401 ; 0,4317 ; 0,5174), β = (0,05 ; 0,15 ; 0,25 ; 0,35) "
                 "(ᾱ = 0,95 ; 0,8075 ; 0,605625 ; 0,39365625 ; 0,6274 ; 0,7787), β = (0,10 ; 0,20 ; 0,30 ; 0,40) (0,3024 ; "
                 "22 %) et β = (0,1 ; 0,2 ; 0,5) (ᾱ = 0,9 ; 0,72 ; 0,36 ; β̃ = 0 ; 0,0714 ; 0,2187), et toute suite de "
                 "coefficients en progression arithmétique présentée comme un planning ; le planning linéaire de 10⁻⁴ à "
                 "0,02, T = 200, 400 et 1 000, Σβ = 2,01 ; 4,02 ; 10,05, e^{−0,8} = 0,4493, e^{−10,05} = 4,32 × 10⁻⁵, "
                 "4,04 × 10⁻⁵, 3,6 × 10⁻⁵, 0,66 %, 14 %, 0,1322, 0,134, 36 %, 1,7 × 10⁻², 1,5 × 10⁻⁸, 0,603, 7,7 × 10⁻⁶ ; "
                 "le cosinus s = 0,008, le plafond 0,999, 1/127,5, 4,1 × 10⁻⁵, f(0) = 0,99984 ; les seuils 0,26 ; 0,50 ; "
                 "0,49 ; 0,80, S(500) = 2,535, les SNR 0,976 ; 0,086 ; 49 ; 2,73 ; 8,7 ; 0,66 ; 0,027 ; 34,8 ; 3,7 ; 0,52 ; "
                 "1,9 ; 1,8, les ln SNR −4,0 ; −10,1 ; −10,2 ; −19,8 et −10,05, la paire de seuils « SNR 1 et 0,1 », les "
                 "pas 100, 300, 600, 497, 804 et 515 ; le pixel x_0 = 0,6 et ε = −0,5 (x_4 = 0,3253), ε_θ = −0,4, z = 1,2, "
                 "0,4165, 0,6838, 0,55214, μ̃_4 = 0,4358, β̃_4 = 0,0496, 0,4382 ; les cas de ✏️ B5.4 (x_3 = 0,8, ε_θ = 0,5, "
                 "z = −1 ; x_3 = 1,5, ε_θ = −0,6 ; x_1 = 0,5, ε_θ = 0,2 ; 0,3981 ; 0,6939 ; 0,1220 ; 0,3446 ; 0,1939 ; "
                 "0,4671 ; 0,4737), de ✏️ B5.5 (x_4 = −0,5, ε_θ = −1,2 ; 0,6924 ; 0,4065 ; 0,0957 ; 0,2276 ; 0,2198 ; "
                 "0,0413 ; 0,2017 ; 0,1546), de ∂ B5.6 (0,1925 ; Var(x_0) = 0,5 et 0,8032 ; √10,05 ≈ 3,17 ; 0,4875 ; "
                 "0,6982 ; 0,7159 ; 0,6375 ; 0,3625 ; 1 + 3 + … + (2t − 1) = t²) et de ∂ B5.7 (x_0 = 0,4, x_2 = 0,1, "
                 "0,7595, 0,2395, 3/77, 0,3277, 0,1627) ; ᾱ_t = 0,64 et 0,81 (0,80 ; 0,60 ; 1,78 ; 0,475 ; 0,9 ; 0,44), "
                 "donc jamais les couples de coefficients (0,8 ; 0,6) ni (0,9 ; 0,44) ; les guidances (0,4 ; −1,0) et "
                 "(0,1 ; −0,6) avec w = 0,5 (0,55 ; −1,2), (0,8 ; −0,5) et (0,5 ; 0,1) avec w = 0, 1, 3, −1, −0,5 (4 ; "
                 "2,01 ; 100 ; 0,65 ; −0,2), 0,3 et 0,5 avec w = 2 (−0,1), les ensembles w = {0, 1, 3, 7}, w = 0,1 ; 0,3 ; "
                 "≥ 4, les conventions 7,5 ↔ 6,5, 3 ↔ 2, 4 ↔ 3, p_uncond = 0,1 ou 0,2, l'écart-type 0,33 → 0,27, les "
                 "Fréchet 133,8 ; 51,4 ; 39,0 ; 65,1 ; N(1 ; 0,3²) + N(−2 ; 0,4²) = N(−1 ; 0,5²) (« 0,5 et pas 0,7 ») ; "
                 "N(2, 1) × N(5 ; 0,5) → (4, 1/3) ; les cibles ±1 (MSE 1 et 2) et (−1, 0, 2) (0,33 ; 1,56) ; Euler sur "
                 "y′ = y avec 1, 2, 4 et 10 pas (2 ; 2,25 ; 2,441 ; 2,594 ; e ≈ 2,718), la boucle `x - (1/n_steps) * "
                 "v_model(x, k/n_steps)`, v = (1 ; −2), les distances de B5.20 (0,915 ; 0,371 ; 0,103 ; 0,081 ; 0,077 ; "
                 "0,075 et 6,81 ; 6,67 ; 0,424…, au point milieu 0,222 ; 0,213 ; 0,079 ; 0,074), √ᾱ_{T−1} = 0,006 ; les "
                 "moyennes exponentielles ρ = 0,9999 ; 0,999 ; 0,99 ; 0,98 avec 800 000, 9 375, 1 252 et 313 pas, "
                 "0,01^{1/1252} = 0,9963 ; d_F² de N(0, 1) contre N(1, 4) (= 2) ; la KL de N(0,5 ; 0,25) contre N(0, 1) "
                 "(0,4431) et z = −0,50 ; le rapport r de mémorisation, les seuils 1/3 et 1/2, 500, 10 000 et 60 000 "
                 "images ; l'anneau de 8 gaussiennes (rayon 1,5, écart-type 0,15, variance 1,15) et le mélange de trois "
                 "gaussiennes en 2D ; d = 128, 6,28 et 54 400 (B5.R1) ; MNIST, Fashion-MNIST, CIFAR-10, 784, 28 × 28 ; les "
                 "exemples des docstrings de `mylearn/diffusion.py` ((0,0001 ; 0,005075 ; 0,01005 ; 0,015025 ; 0,02), "
                 "(0,1013 ; 0,2795 ; 0,4736 ; 0,7241 ; 0,999), x_0 = [[1, −1], [0,5 ; 0]], x_t = [[1,2649 ; −0,6325], "
                 "[1,1 ; 0,8]], ε = [[0,3 ; −2], [1 ; 0,5]], x_0 = [[0,5 ; −1 ; 0,25]], t = 700) ; de ce dépôt, le pas "
                 "d'Euler de M20 (λ = −0,5 et T = 1 : 0,5862 ; 0,6035 ; 0,6058 pour 4, 25 et 100 pas ; la rotation et ses "
                 "1,1289 et 1,0126 ; le demi-tour en 6, 12 et 48 pas), l'altitude du refuge N(1 520 ; 10²) et le baromètre, "
                 "les deux pièces pesées ((40, 25), diag(4, 9), 72 g) et la KL de N(6, 4) contre N(8, 9) de M25a, la "
                 "station (N(11, 4) et N(3, 9), ¼ et ¾, 8 °C) et la chaudière (ln 0,226) de M25b, les exemples des stubs "
                 "`gaussian`, `latent` et `markov`.",
        "exercises": [
            ("MB5.Q1", "🧠", 1, 5, "Une récurrence linéaire gaussienne : quelle moyenne, quelle variance, quand une loi "
             "stationnaire, et combien de pas pour oublier le départ ?", "§1", "E"),
            ("MB5.Q2", "🧠", 1, 5, "Le pont et les couplages : où l'incertitude est la plus grande, ce que fixent les lois "
             "marginales et ce qu'elles laissent libre", "§2", "E"),
            ("MB5.Q3", "🧠", 1, 4, "Signal et bruit : SNR, cotes, logit et décibels, et ce qu'un changement d'échelle ne "
             "change pas", "§3", "E"),
            ("MB5.Q4", "🧠", 1, 5, "Ce que la MSE apprend : une moyenne conditionnelle, pas la valeur la plus probable ; et ce "
             "qu'apprennent la MAE et la log-loss", "§4", "E"),
            ("MB5.Q5", "🧠", 1, 5, "Le score en x : où il pointe, la constante qu'il ignore, et ce que dit la formule de "
             "Tweedie", "§5", "E"),
            ("MB5.Q6", "🧠", 1, 5, "L'ELBO d'une chaîne : quels termes dépendent du modèle, quelle KL compare quoi, et ce que "
             "devient une KL entre gaussiennes de même variance", "§6", "E"),
            ("MB5.Q7", "🧠", 1, 4, "Guider : interpoler ou extrapoler, la différence de deux scores, et quand un produit de "
             "puissances n'est plus une densité", "§7", "E"),
            ("MB5.Q8", "🧠", 1, 5, "Euler, point milieu et chemin droit : ce que coûte un pas, l'ordre de l'erreur, et le "
             "sens du temps", "§8 §9", "E"),
            ("MB5.R1", "🔁", 1, 6, "Sommes et images affines de gaussiennes, produit de densités et modèle linéaire gaussien "
             "(M25a)", "§1 §2", "E"),
            ("MB5.R2", "🔁", 1, 6, "Espérance et variance conditionnelles, lois totales, et l'ELBO d'un latent (M25b)",
             "§4 §6", "E"),
            ("MB5.R3", "🔁", 1, 6, "Un pas d'Euler (M20), la loi stationnaire d'une chaîne finie (M26) et la cote d'une "
             "probabilité (R6)", "§1 §3 §8", "E"),
            ("MB5.1", "✏️", 2, 30, "L'anomalie de température d'un lac, un processus autorégressif d'ordre 1 : sa loi dans "
             "k jours sachant aujourd'hui, sa loi stationnaire, le nombre de jours pour oublier le départ, et sa loi sachant "
             "un jour passé", "§1", "E"),
            ("MB5.2", "✏️", 1, 20, "La survie d'une ruche à six mois de risques différents : le produit exact, son "
             "logarithme, le risque mensuel constant équivalent, et l'encadrement par deux exponentielles", "§1", "E"),
            ("MB5.3", "✏️", 2, 30, "Un phoque balisé entre deux relevés : sa loi à une heure intermédiaire (le pont d'une "
             "marche aléatoire) ; puis des scénarios de position aux mêmes lois à chaque heure, tirés avec un seul nombre au "
             "hasard ou avec un bruit frais, et leur corrélation", "§2", ""),
            ("MB5.4", "✏️", 2, 20, "Une voix mêlée à un bruit de fond : SNR, part de variance de la voix, logit et décibels, "
             "puis la voix retrouvée à partir d'une estimation du bruit, et l'erreur amplifiée", "§3", "E"),
            ("MB5.5", "✏️", 2, 35, "Débruiter un signal reçu, d'abord gaussien, puis émis à deux niveaux ±c : E[x | y] par "
             "M25a et par la formule de Tweedie (une tanh), et ce que rend le débruiteur quand le bruit tend vers 0",
             "§5", "E"),
            ("MB5.6", "✏️", 3, 40, "Un bit altéré par deux relais, puis reconstitué par un modèle retour : ln p(x), l'ELBO "
             "de la loi aller des relais, et sa décomposition en reconstruction, KL finale et KL d'un pas retour", "§6",
             "E"),
            ("MB5.7", "✏️", 2, 30, "La date de floraison d'une variété et celle de tout le verger, deux lois gaussiennes : "
             "la loi p_v^{1+w} p_g^{−w} pour deux valeurs de w, son score, sa condition d'existence et le w limite", "§7",
             "E"),
            ("MB5.8", "✏️", 2, 30, "Une tasse de thé qui refroidit : Euler et point milieu contre la solution exacte, "
             "l'erreur quand le pas est divisé par deux, un courant de vitesse constante, et un calcul à rebours", "§8",
             "E"),
            ("MB5.9", "✏️", 3, 35, "Le chemin droit d'un bruit N(0, 1) vers une loi N(m, τ²) : le champ moyen (affine en x), "
             "un pas d'Euler depuis s = 1 qui rend m pour tout départ, puis deux pas, et l'écart-type obtenu contre τ",
             "§9", "E"),
            ("MB5.10", "∂", 2, 30, "La récurrence linéaire gaussienne à coefficients quelconques : la loi de x_t sachant x_0 ; "
             "à coefficient constant |a| < 1, la loi sachant un instant passé, la loi stationnaire et la convergence depuis "
             "toute loi initiale ; aucune loi stationnaire si |a| ≥ 1", "§1", "E"),
            ("MB5.11", "∂", 2, 20, "La meilleure prédiction quadratique : E[(Y − g(X))²] = E[V(Y | X)] + "
             "E[(E[Y | X] − g(X))²], donc g = E[Y | X] ; sur un échantillon, la moyenne de chaque groupe", "§4", "E"),
            ("MB5.12", "∂", 3, 30, "La formule de Tweedie : dériver la densité de y = a x + b n sous l'espérance, d'où "
             "E[x | y] et E[n | y] ; la vérification quand x est gaussien", "§5", ""),
            ("MB5.13", "∂", 3, 40, "L'ELBO d'une chaîne de latents : Markov et Bayes réécrivent chaque pas aller, la somme "
             "télescope ; puis chaque KL entre gaussiennes de même variance devient une MSE pondérée des moyennes", "§6",
             ""),
            ("MB5.14", "🔗", 1, 25, "Pont : une loss de débruitage à plusieurs niveaux de bruit, son minimiseur à chaque "
             "niveau, et pour des données gaussiennes les MSE minimales sur le signal et sur le bruit, dont le rapport est "
             "le SNR", "§3 §4 §5", "E"),
            ("MB5.15", "🗣️", 1, 10, "Expliquer avec le jeu du téléphone pourquoi, après assez de relais qui atténuent et "
             "bruitent, le message reçu ne dit plus rien du message émis", "§1", "E"),
            ("MB5.E1", "💼", 1, 10, "« Un modèle de régression entraîné à la MSE prédit-il le prix le plus probable ? Que "
             "prédit-il quand les prix d'un même profil se partagent en deux groupes, et quelle loss prendre pour une "
             "médiane ? »", "§4", ""),
            ("MB5.16", "🔨", 1, 25, "Propager la moyenne et la variance d'une récurrence linéaire gaussienne à coefficients "
             "quelconques", "§1", "E m:linear_gaussian_recursion"),
            ("MB5.17", "🔨", 2, 35, "Le débruiteur optimal d'une mesure bruitée quand le signal suit un mélange de "
             "gaussiennes, des points compris", "§5", "E m:posterior_mean_mixture"),
            ("MB5.18", "🔨", 2, 35, "Suivre un champ de vitesses qui dépend du temps : la méthode d'Euler et celle du point "
             "milieu, dans les deux sens du temps", "§8", "E m:euler_ode,midpoint_ode"),
            ("MB5.19", "📦", 1, 20, "`scipy.integrate.solve_ivp` : une croissance logistique suivie par tes deux méthodes, "
             "l'erreur au temps final selon le nombre de pas en échelle log-log, et les pentes 1 et 2", "§8", "p:MB5.18"),
            ("MB5.20", "🔮", 1, 15, "Prédire ce que rend le débruiteur optimal de cinq relevés quand le bruit tend vers 0, "
             "pour une mesure proche d'un relevé puis à égale distance de deux, et mesurer", "§5", "E p:MB5.17"),
            ("MB5.21", "🔬", 2, 25, "Le chemin droit vers une loi gaussienne : Euler et point milieu sur le champ moyen "
             "exact, de 1 à 32 pas, la moyenne et l'écart-type obtenus contre ceux de la cible", "§8 §9",
             "E p:MB5.9,MB5.18"),
            ("MB5.22", "🎨", 1, 20, "Des lois guidées p_c^{1+w} p_u^{−w} sur une grille : une loi générale à deux bosses, une "
             "loi de classe gaussienne, et ce que w resserre et déplace", "§7", "p:MB5.7"),
            ("MB5.23", "🐛", 1, 20, "Chasse à l'erreur : un pont aux poids inversés, un débruiteur qui oublie le bruit dans "
             "ses responsabilités, et un Euler dont le temps n'avance pas", "§2 §5 §8", "E"),
            ("MB5.24", "🛠️", 1, 25, "Un test de propriété : Euler exact pour une vitesse constante, le point milieu exact "
             "pour une vitesse affine en t, et l'erreur d'Euler divisée par deux avec le pas", "§8", "p:MB5.18"),
            ("MB5.25", "🏆", 3, 30, "Défi : transporter un bruit N(0, 1) vers une loi à deux bosses par son champ moyen "
             "exact, en au plus huit évaluations du champ, sous une distance de Wasserstein fixée", "§8 §9",
             "p:MB5.17,MB5.18"),
        ],
    },
    {
        "id": "MB6", "dir": "mb6_shapley_equite", "hours": 12.1, "generation_sessions": 1, "mml": [],
        "summary": "Partager un gain, une variation ou une décision. D'abord les jeux coopératifs : la contribution "
                   "marginale d'un joueur, sa moyenne sur les ordres d'arrivée (la valeur de Shapley), les poids des "
                   "coalitions qui en découlent et ce que coûte le calcul ; les quatre axiomes, les jeux d'unanimité et "
                   "les dividendes de Harsanyi, qui montrent qu'une interaction se partage également entre ses membres et "
                   "que la valeur de Shapley est la seule à respecter ces axiomes. Puis fixer une variable d'une fonction "
                   "de plusieurs variables : l'espérance marginale (la dépendance partielle) contre l'espérance "
                   "conditionnelle, les courbes ICE et les interactions. Puis l'intégrale d'un champ de vecteurs le long "
                   "d'un chemin, le théorème du gradient, et deux façons de partager une variation entre les coordonnées "
                   "(le long du segment, ou par les chemins en escalier, dont la moyenne est une valeur de Shapley). Deux "
                   "outils courts : l'interpolation bilinéaire d'une grille et la corrélation de rangs de Spearman. Enfin "
                   "l'équité vue comme des indépendances : ce qui est incompatible quand les taux de base diffèrent, pour "
                   "des décisions et pour des scores calibrés, puis tirer au sort entre deux seuils, repondérer, et "
                   "mesurer l'écart de deux taux. workbookIA B6 applique ces outils à l'explication de modèles et à "
                   "l'audit d'équité.",
        "objectives": [
            "Calculer la valeur de Shapley d'un petit jeu coopératif par les ordres d'arrivée et par les poids des "
            "coalitions, dire ce que coûte chaque méthode, et combien d'ordres tirés au hasard suffisent.",
            "Vérifier les quatre axiomes sur un jeu, calculer ses dividendes de Harsanyi et en déduire la valeur de "
            "Shapley ; démontrer qu'elle est la seule à respecter les quatre axiomes.",
            "Distinguer la moyenne marginale (dépendance partielle) et la moyenne conditionnelle d'une fonction, les "
            "calculer pour deux variables gaussiennes corrélées, et relier des courbes ICE parallèles à l'absence "
            "d'interaction.",
            "Calculer l'intégrale d'un champ de vecteurs le long d'une ligne brisée ou d'un arc, reconnaître un champ de "
            "gradient (indépendance du chemin, test de Schwarz), et partager une variation de f entre les coordonnées le "
            "long du segment ou par les chemins en escalier.",
            "Agrandir une grille par interpolation bilinéaire dans les deux conventions d'alignement, et lire la moyenne "
            "d'un gradient sur une grille comme une dérivée directionnelle.",
            "Calculer une corrélation de rangs de Spearman, ex aequo compris, et dire ce qu'elle ne voit pas.",
            "Écrire les critères d'équité comme des indépendances, et démontrer ce qui est incompatible quand les taux de "
            "base diffèrent, pour des décisions et pour des scores calibrés.",
            "Atteindre un taux de détection en tirant au sort entre deux seuils, repondérer une table pour rendre groupe "
            "et label indépendants, et donner l'intervalle de l'écart de deux taux.",
        ],
        "sections": [("§1", "Jeux coopératifs : contributions marginales, ordres d'arrivée et poids des coalitions"),
                     ("§2", "Les quatre axiomes, les jeux d'unanimité et les dividendes de Harsanyi"),
                     ("§3", "Fixer une variable : espérance marginale ou conditionnelle, courbes ICE et interactions"),
                     ("§4", "Intégrer un gradient le long d'un chemin, et partager une variation entre les coordonnées"),
                     ("§5", "Une grille : la moyenne d'un gradient, et l'agrandir par interpolation bilinéaire"),
                     ("§6", "La corrélation de rangs de Spearman"),
                     ("§7", "Les critères d'équité comme des indépendances, et ce qui est incompatible"),
                     ("§8", "Décider au hasard, repondérer, mesurer l'écart entre deux groupes")],
        "teaches": ["jeu coopératif à n joueurs : fonction caractéristique v sur les coalitions, contribution marginale "
                    "v(S ∪ {i}) − v(S), valeur de Shapley comme moyenne sur les n! ordres d'arrivée",
                    "poids d'une coalition de taille s, s!(n − 1 − s)!/n!, en regroupant les ordres ; lecture probabiliste "
                    "(une taille uniforme, puis une coalition uniforme de cette taille) et Σ_s C(n − 1, s) w(s) = 1 ; coût : "
                    "n! ordres contre 2^(n−1) coalitions par joueur (rappels de R4 et R8)",
                    "estimer par des ordres tirés au hasard : une moyenne de contributions marginales, estimateur sans biais "
                    "(M02c), nombre d'ordres par l'inégalité de Hoeffding quand les contributions sont bornées (M11) ; "
                    "l'efficacité tient à chaque ordre (une somme télescopique)",
                    "jeux de vote pondéré [q ; w₁, …, w_n] et indice de Shapley-Shubik (le membre pivot) : le poids n'est "
                    "pas le pouvoir ; jeux de partage de coûts et règle de l'aéroport",
                    "les quatre axiomes : efficacité Σφ_i = v(N) − v(∅), symétrie, joueur nul, additivité ; un jeu additif "
                    "v(S) = c + Σ_{j∈S} a_j donne φ_i = a_i",
                    "jeux d'unanimité u_T, dividendes de Harsanyi d_T (inversion de Möbius sur les parties), v = Σ_T d_T u_T ; "
                    "φ_i = Σ_{T∋i} d_T/|T| : chaque interaction est partagée également entre ses membres ; unicité de la "
                    "valeur de Shapley (démontrée, ★★★)",
                    "espérance marginale E[f(v, X_{−j})] (la dépendance partielle) contre espérance conditionnelle "
                    "E[f(X) | X_j = v] ; égales quand X_j est indépendante des autres variables ; calcul fermé pour un couple "
                    "gaussien (rappel de M25a) ; la même opposition entre le jeu « marginal » et le jeu « conditionnel » "
                    "d'une fonction (énoncée)",
                    "courbes ICE v ↦ f(v, x_{i,−j}), dont la dépendance partielle est la moyenne ; f = g(x_j) + h(x_{−j}) ⇔ "
                    "courbes ICE parallèles ⇔ ∂²f/∂x_j∂x_k = 0 pour tout k ≠ j (f régulière sur un pavé, démontré) ; une "
                    "moyenne peut cacher une interaction",
                    "chemin paramétré et dérivée de f le long d'un chemin, (f∘γ)′ = ∇f(γ) · γ′ (rappels de M05b et M17) ; "
                    "intégrale d'un champ de vecteurs le long d'un chemin et d'une ligne brisée ; théorème du gradient "
                    "∫ ∇f · dγ = f(B) − f(A) : indépendance du chemin, intégrale nulle sur une boucle ; un champ qui n'est "
                    "pas un gradient (dérivées croisées différentes, Schwarz)",
                    "sommes de Riemann, trapèzes et Simpson sur [0, 1] et leurs ordres d'erreur (rappel de M02a)",
                    "partager f(x) − f(r) entre les coordonnées : le long du segment (les parts ∫ ∂_i f dγ_i, dont la somme "
                    "est f(x) − f(r)), ou le long d'un chemin en escalier (les contributions marginales dans un ordre) ; la "
                    "moyenne des chemins en escalier est la valeur de Shapley du jeu v(S) = f(x_S, r_{S̄}) ; les deux partages "
                    "coïncident pour une fonction multilinéaire (démontré par les jeux d'unanimité) et diffèrent en général ; "
                    "ils dépendent de la référence r, et une coordonnée de dérivée nulle en x peut recevoir une part non "
                    "nulle (saturation)",
                    "fonctions homogènes de degré k : identité d'Euler Σ x_i ∂_i f = k f ; depuis r = 0, la part de x_i le long "
                    "du segment vaut x_i ∂_i f(x)/k",
                    "moyenne d'un gradient sur une grille : (1/(HW)) Σ ∂y/∂A_ij est la dérivée de y par un décalage uniforme "
                    "de la grille, divisée par HW (une dérivée directionnelle) ; homogénéité positive de la partie positive, "
                    "max(0, λz) = λ max(0, z) pour λ > 0",
                    "interpolation linéaire et bilinéaire (deux interpolations linéaires, dans un ordre ou dans l'autre), "
                    "exacte pour les fonctions affines ; agrandir une grille h × w en H × W : centres des cases alignés "
                    "(u ↦ (u + ½) h/H − ½) ou coins alignés (u ↦ u (h − 1)/(H − 1)), écart d'au plus un demi-pas",
                    "corrélation de rangs de Spearman : rangs, ex aequo (rangs moyens), ρ = corrélation de Pearson des rangs, "
                    "= 1 − 6 Σ d_i²/(n(n² − 1)) sans ex aequo (démontré dans la fiche) ; invariance par une transformation "
                    "strictement croissante ; ce qu'elle ne voit pas (l'ampleur des écarts)",
                    "critères d'équité comme des (in)dépendances : indépendance Ŷ ⊥ G (parité des décisions), séparation "
                    "Ŷ ⊥ G | Y (égalité des taux d'erreur), suffisance Y ⊥ G | Ŷ ou Y ⊥ G | S (parité des precisions, "
                    "calibration par groupe) ; rappels des définitions de M03 §8 et de l'indépendance conditionnelle de M25b",
                    "l'identité de M03 §8 entre séparation et suffisance (rappelée, non redémontrée) ; indépendance et "
                    "séparation incompatibles quand les taux de base diffèrent, sauf pour une décision indépendante de Y "
                    "(démontré)",
                    "scores calibrés dans chaque groupe : E[S | G = g] = p_g, et p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; "
                    "mêmes moyennes de scores chez les positifs et chez les négatifs de deux groupes : taux de base égaux ou "
                    "score parfait (Kleinberg, Mullainathan et Raghavan, démontré)",
                    "décisions randomisées : tirer au sort entre deux seuils donne tout point de la corde entre deux points "
                    "de la courbe ROC (TPR et FPR affines en la probabilité du tirage)",
                    "repondération w(g, y) = P(g)P(y)/P(g, y) : la loi pondérée garde les deux marges et rend G et Y "
                    "indépendants (démontré) ; diviser par une probabilité, comme Horvitz-Thompson (M20)",
                    "écart de deux proportions indépendantes : erreur type √(p₁(1 − p₁)/n₁ + p₂(1 − p₂)/n₂) et intervalle "
                    "de Wald de l'écart ; pour un taux de vrais positifs, n est le nombre de positifs ; bootstrap stratifié "
                    "(tirer dans chaque groupe) contre bootstrap global (principe)"],
        "requires": [("fonction affine passant par deux points", "R3"),
                     ("parties d'un ensemble et leur nombre 2^n, notations Σ et Π, rédiger une démonstration", "R4"),
                     ("principe multiplicatif, factorielle, combinaisons C(n, k), arbres", "R8"),
                     ("intégrale, théorème fondamental, méthodes des rectangles, des trapèzes et de Simpson", "M02a"),
                     ("espérance, linéarité de l'espérance, loi de Bernoulli et sa variance", "M02b"),
                     ("corrélation de Pearson, estimateur sans biais, erreur type, bootstrap", "M02c"),
                     ("probabilités conditionnelles, indépendance, taux par groupe, calibration, courbe ROC, l'identité des "
                      "taux de faux positifs de deux groupes (§8)", "M03"),
                     ("dérivées partielles, gradient, dérivée directionnelle, dérivées croisées et théorème de Schwarz",
                      "M05b"),
                     ("intervalle d'une proportion (Wald)", "M08"),
                     ("inégalité de Hoeffding et taille d'échantillon", "M11"),
                     ("règle de la chaîne le long d'une courbe, fonctions affines par morceaux", "M17"),
                     ("estimateur de Horvitz-Thompson : diviser par une probabilité", "M20"),
                     ("loi conditionnelle d'un couple gaussien : moyenne affine en la valeur observée", "M25a"),
                     ("indépendance conditionnelle, espérance conditionnelle et espérance totale", "M25b")],
        "frontieres": ["B6.1", "B6.3", "B6.4", "B6.5", "B6.7", "B6.11", "B6.Q3", "B6.Q4", "B6.Q5", "B6.Q6", "B6.Q7",
                       "B6.Q9", "B6.Q11", "B6.14", "B6.18", "B6.21", "B6.22", "B6.23", "B6.E2"],
        "mymath": {"module": "attribution.py",
                   "functions": ["coalition_weights", "harsanyi_dividends", "line_integral", "spearman_rho"]},
        "reading_minutes": 125,
        "flashcards": 15,
        "notes": "Frontières : les ∂ B6.2 (φ_i = w_i (x_i − E[x_i]) d'un modèle linéaire avec un fond, la valeur de base f(b̄), "
                 "le logit contre la probabilité, le produit x₁x₂ avec une ligne de fond et φ₁ = ½(x₁ − b₁)(x₂ + b₂), la ligne "
                 "moyenne de ✏️ B6.1) et B6.6 (l'identité de Chouldechova par les effectifs puis par Bayes, son contrôle, le "
                 "rapport des cotes à PPV et FNR égaux, la PPV croissante en p à FPR et FNR égaux, les issues, COMPAS, ce "
                 "qu'ajoute Kleinberg) ; ✏️ B6.1 (Shapley exact à la main d'un modèle à trois features avec un fond de deux "
                 "lignes), ✏️ B6.3 (gradients intégrés à la main, règles gauche, droite et trapèzes, le plus petit nombre de "
                 "pas, la référence, captum), ✏️ B6.4 (Grad-CAM à la main), ✏️ B6.5 (audit de deux groupes, Δ_DP, Δ_EO, "
                 "règle des quatre cinquièmes), 🧮 B6.7 (coût de Shapley exact, de KernelSHAP et de TreeSHAP), 📄 B6.11 "
                 "(Lundberg et Lee, leurs deux jeux, le noyau de KernelSHAP), les quiz B6.Q3 (dépendance partielle de x₁x₂ à "
                 "x₂ = ±1 et de 3x₁ + x₂²), B6.Q4 (les axiomes lus sur une explication base + Σφ), B6.Q5 (le fond), B6.Q6 "
                 "(deux features corrélées ou copiées), B6.Q7 (min(x, 1) et la ligne de référence), B6.Q9 (randomisation, "
                 "« Spearman = 1 ⇒ mêmes valeurs ? »), B6.Q11 (critères compatibles ?), les 🔨 B6.14 (`shapley_values`), B6.18 "
                 "(`integrated_gradients`, `grad_cam`) et B6.23 (`group_rates` et les deux écarts), 🐛 B6.21 (Grad-CAM à l'envers, dont l'alignement `align_corners`), 🔬 B6.22 (le test de randomisation et la corrélation de Spearman), et 💼 B6.E2 (une valeur "
                 "SHAP et ses limites). Vigilance sans frontière : 🔬 B6.27 (repondération et seuils par groupe sur Adult) et "
                 "📦 B6.24, 📈 B6.25 (intervalles d'un écart) côtoient le §8 : autres cadres, autres nombres, et aucun seuil "
                 "choisi comme quantile des scores des positifs. "
                 "MB6 travaille hors des réseaux et hors des données de personnes : des jeux (un conseil à vote pondéré, des "
                 "hameaux qui partagent une conduite d'eau, trois amis et un taxi), des fonctions écrites (le rendement d'une "
                 "parcelle, le travail d'une force, un coût à trois facteurs, un indice régional), des grilles de capteurs, "
                 "deux juges qui classent des boulangeries, des lignes de production, des laboratoires et des trains ; jamais "
                 "un modèle entraîné, une feature, un fond (*background*) de données, un réseau, une image, un pixel, une "
                 "carte d'activation, un canal, un logit, un client, un prêt, un candidat, des groupes de personnes ni un dataset "
                 "de workbookIA. SHAP, KernelSHAP, TreeSHAP, LIME, gradients intégrés, saillance et Grad-CAM ne "
                 "sont nommés que dans les encadrés 🔗 « Dans workbookIA » et 💻 de la fiche (au plus une phrase sur "
                 "KernelSHAP, sans son noyau), jamais dans un énoncé. "
                 "§1-§2 (jeux) : la valeur de Shapley est définie par les ordres d'arrivée, puis par les poids des coalitions "
                 "(fiche : n = 3 et n = 5, jamais n = 4 comme exemple principal, l'encadré de la fiche de B6) ; l'estimation "
                 "par des ordres tirés au hasard est un paragraphe du §1 (sans biais, efficacité exacte à chaque ordre, "
                 "Hoeffding) et la dernière question de ✏️ MB6.1, sans fonction `mymath` ; aucun exercice ne demande seul le "
                 "poids d'une coalition d'un joueur parmi trois (B6.1 d), le nombre de coalitions sans i pour n = 5 (B6.Q4 e), "
                 "une valeur manquante d'une explication base + Σφ (B6.Q4 a), ni « f(a, b) = f(b, a) ⇒ mêmes parts ? » "
                 "(B6.Q4 d) ; 🧠 MB6.Q1 porte sur des jeux abstraits (un conseil, un partage de coûts), jamais sur une "
                 "explication f(x) = base + Σφ. ✏️ MB6.1 : un conseil à quatre membres où un membre est nul et deux membres de poids différents "
                 "ont le même pouvoir (par exemple [7 ; 5, 3, 2, 1], total 11) ; les pivots se comptent sur les 24 ordres ; "
                 "la symétrie des deux membres se vérifie sur v ; Hoeffding (M11) donne le nombre d'ordres tirés pour un "
                 "indice à ± 0,05. ✏️ MB6.2 : trois hameaux aux besoins emboîtés (le coût d'une coalition est celui de son "
                 "membre le plus éloigné, c(S) = max) : la valeur de Shapley par les six ordres, les dividendes (de signes "
                 "alternés), la règle de l'aéroport retrouvée par l'additivité (une somme de jeux de tronçon), l'efficacité, "
                 "la symétrie, le joueur nul vérifiés. Le jeu additif v(S) = c + Σ_{j∈S} a_j ⇒ φ_i = a_i est un énoncé de la "
                 "fiche sur des jeux abstraits : aucun exercice ne l'applique à un modèle linéaire, à un fond ni à une "
                 "fonction de deux variables avec une ligne de référence (∂ B6.2). L'unicité (∂ MB6.8, ★★★, hors parcours "
                 "essentiel) est énoncée dans la fiche avec son idée ; le 💼 MB6.E1 en demande l'argument en une minute ; "
                 "« une interaction se partage également entre ses membres » se lit sur φ_i = Σ_{T∋i} d_T/|T|, jamais sur un "
                 "produit de deux facteurs. Le 🗣️ MB6.12 (le taxi) n'a pas de nombres. Le 🏆 MB6.22 : un conseil de 25 "
                 "membres aux poids entiers (petits), les indices exacts par un comptage par taille et par poids (une "
                 "programmation dynamique) et `coalition_weights`, comparés à des valeurs de référence enregistrées, en moins "
                 "d'une seconde ; ce n'est pas l'énumération des coalitions de `shapley_values` (B6.14). "
                 "§3 (fixer une variable) : la moyenne marginale E[f(v, X_{−j})] est la dépendance partielle de workbookIA ; "
                 "la moyenne conditionnelle E[f(X) | X_j = v] lui est opposée, sur des fonctions écrites et des variables "
                 "gaussiennes corrélées (M25a) ; la fiche relie cette opposition au jeu « marginal » E[f(x_S, X_{S̄})] et au "
                 "jeu « conditionnel » d'une fonction, en une phrase, sans fond ni calcul de Shapley. ✏️ MB6.3 : deux modèles "
                 "de rendement écrits, l'un séparable (une fonction de la pluie plus une fonction de l'engrais), l'autre non "
                 "(une fonction de l'écart pluie − engrais, de dérivée croisée non nulle) ; les courbes ICE de l'engrais pour "
                 "trois parcelles, la dérivée croisée, puis, pour le modèle séparable, affine en la pluie, la moyenne marginale sous une loi "
                 "gaussienne de la pluie et la moyenne conditionnelle quand (pluie, engrais) est un couple gaussien "
                 "corrélé : l'écart est affine en l'engrais, la moyenne conditionnelle lui prête l'effet de la pluie. Ni "
                 "produit x₁x₂ à facteur centré, ni « la dépendance partielle est-elle plate ? », ni « combien de pentes ? » "
                 "(B6.Q3 a, b), ni courbes centrées (B6.Q3 d), ni loi uniforme sur [−1, 1], ni indicatrice 𝟙[x₃ ≥ 0] "
                 "(Goldstein). 🔬 MB6.18 : deux mesures corrélées d'un même objet (la hauteur et le diamètre d'arbres, ou la "
                 "température et l'humidité d'une serre), une fonction écrite, ρ = 0 ; 0,5 ; 0,9, la moyenne conditionnelle "
                 "estimée dans une fenêtre |x_j − v| ≤ h, comparée aux formules ; jamais `sklearn.inspection` "
                 "(`partial_dependence`, B6.12), ni deux copies d'une même variable (B6.16, B6.Q6). 🧠 MB6.Q2 ne demande ni la forme de la dépendance partielle d'un produit, ni un nombre de pentes, ni une dépendance partielle en un point d'une fonction donnée (B6.Q3 a à c). "
                 "§4 (chemins) : un chemin est paramétré par t ∈ [0, 1] (jamais α, la variable des gradients intégrés) ; le "
                 "théorème du gradient et l'indépendance du chemin sont démontrés dans la fiche (TFA de M02a et chaîne de "
                 "M17) ; les règles de Riemann, des trapèzes et de Simpson sont rappelées de M02a (ordres d'erreur, "
                 "exactitude du trapèze pour une intégrande affine) sans exercice : aucun « plus petit nombre de pas », "
                 "aucune table de quatre règles, aucun captum (✏️ B6.3). ✏️ MB6.4 : un champ de gradient polynomial le long "
                 "d'un segment, d'un chemin en escalier et d'un arc de parabole, puis un champ aux dérivées croisées "
                 "différentes (pas (y, 0), l'exemple du stub) le long de deux chemins de mêmes extrémités. ✏️ MB6.5 (parcours complet) : un coût = prix × quantité × "
                 "taux de change entre deux dates (trois facteurs, référence non nulle) : les parts des facteurs le long du "
                 "segment (trois intégrales de polynômes), puis la moyenne des six chemins en escalier (la valeur de "
                 "Shapley du jeu de la fonction), qui coïncident (le théorème multilinéaire de la fiche, démontré par les "
                 "jeux d'unanimité dans un bloc repliable) ; que deux partages diffèrent pour une fonction qui n'est pas "
                 "multilinéaire est un exemple de la fiche (par exemple x²y entre deux points sans coordonnée nulle) et un "
                 "item de 🧠 MB6.Q3, sans exercice de calcul. Jamais un produit de deux facteurs du premier degré avec une référence (∂ B6.2.8), ni dans un "
                 "exercice, ni dans la fiche (exemple, corollaire ou bloc de la preuve du théorème multilinéaire), ni dans "
                 "une flashcard, une solution ou une variante ; ni x y² ou x e^y (M05b), ni une sigmoïde, ni un minimum ou un plafond (la saturation reste un exemple de la "
                 "fiche, sur un barème plafonné, sans exercice : B6.Q7), ni règle numérique ni nombre de pas. Euler (fonctions "
                 "homogènes, depuis r = 0 la part x_i ∂_i f(x)/k ; une Cobb-Douglas dans la fiche) n'a qu'un item de "
                 "🧠 MB6.Q3 ; jamais « gradient × entrée ». Le 🔮 MB6.17 prend une boucle triangulaire et le champ tournant "
                 "(−y, x) (deux fois l'aire) avec un champ de gradient, jamais le champ (y, 0) de la docstring ; le "
                 "🎨 MB6.19 trace les lignes de niveau d'une fonction écrite ; le 🛠️ MB6.21 écrit trois propriétés de "
                 "`line_integral` (sens inversé, segment coupé en deux, champ de gradient). "
                 "§5 (grilles) : la moyenne d'un gradient sur une grille est la dérivée par un décalage uniforme, "
                 "divisée par HW ; ✏️ MB6.6 la calcule pour un indice régional écrit sur une grille 3 × 4 de températures "
                 "(par exemple des degrés-jours pondérés, y = Σ c_ij max(0, T_ij − 10)), sous un réchauffement uniforme, "
                 "puis agrandit la grille en 6 × 8 dans les deux "
                 "conventions (centres alignés, coins alignés), avec l'écart entre les deux conventions (au plus un demi-pas ; ici un quart de pas aux bords) : on calcule les coordonnées "
                 "d'origine de toutes les cases d'une ligne et les valeurs de quelques cases, pas les 48 ; jamais de canaux, de combinaison "
                 "de cartes par des poids suivie d'une partie positive, de normalisation par le maximum, ni de carte agrandie "
                 "8, 24 ou 32 fois (✏️ B6.4, 🐛 B6.21) ; `align_corners` de PyTorch et `scipy.ndimage.zoom` sont nommés dans "
                 "un 💻. §6, Spearman (lacune) : la fiche l'enseigne sur deux juges qui classent huit boulangeries (un ex aequo), "
                 "avec la formule 1 − 6Σd²/(n(n² − 1)) démontrée dans un bloc repliable ; 🧠 MB6.Q4 et 🔨 MB6.16 ; aucun "
                 "« ρ = 1 ⇒ mêmes valeurs ? » ni le contre-exemple (1, 2, 3)/(10, 20, 30) (B6.Q9 d), aucun test de "
                 "randomisation, SSIM ni carte de saillance (B6.22). Le 🐛 MB6.20 : des poids s!(n − 1 − s)!/(n − 1)! (sans "
                 "le 1/n : leur somme pondérée vaut n), des rangs donnés dans l'ordre d'apparition aux ex aequo, une "
                 "interpolation (1 − t) b + t a au lieu de (1 − t) a + t b ; pas d'erreur d'alignement des coins (🐛 B6.21). "
                 "§7-§8 (équité) : groupes G (deux lignes de production, deux usines, deux lignes de trains, deux "
                 "laboratoires), label Y (défaut, panne, retard, contamination), décision Ŷ, score S ; un ⚠️ de la fiche : le score S d'un classifieur (M03) n'a rien à voir avec le score en x de MB5 ni avec la fonction score de MB8 ; les définitions "
                 "par groupe et l'identité de M03 §8 (FPR, prévalence, precision, recall) sont rappelées en une ligne par "
                 "renvoi, jamais redémontrées ni appliquées à de nouveaux nombres : aucun rapport des cotes à PPV et FNR "
                 "égaux (∂ B6.6.6), aucune PPV calculée à FPR et FNR égaux (∂ B6.6.7), aucun classifieur parfait ni "
                 "Δ_DP (B6.Q11). MB6 ajoute les critères comme indépendances (M25b), l'incompatibilité indépendance et "
                 "séparation et la repondération (∂ MB6.10, deux preuves de trois lignes), et Kleinberg et coll. pour des "
                 "scores (∂ MB6.9 : l'identité p(1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] par l'espérance totale (M25b), "
                 "puis l'impossibilité ; une petite table de scores calibrés de retards de trains en contrôle) : la fiche de "
                 "B6 l'énonce et l'admet, ∂ B6.6.9 demande seulement ce qu'il ajoute à COMPAS, et MB6 ne parle pas de "
                 "COMPAS. ✏️ MB6.7 : deux lignes de taux de défauts différents (par exemple 8 % et 20 %), un contrôle de "
                 "mêmes TPR et FPR sur les deux : les taux de rejet diffèrent ; sur une ligne, deux points (FPR, TPR) donnés "
                 "par deux seuils, la probabilité de tirage qui atteint un TPR visé et le FPR obtenu ; une table de comptes "
                 "ligne × défaut, les poids P(g)P(y)/P(g, y) et les taux de défaut pondérés égaux. 🔗 MB6.11 : deux "
                 "laboratoires qui détectent une contamination, avec peu et beaucoup d'échantillons contaminés : TPR, écart, "
                 "erreur type, intervalle de Wald de l'écart, et ce que change un quadruplement du petit effectif ; le "
                 "bootstrap stratifié en une phrase ; ni Adult, ni 2 000 ou 500 tirages, ni tableau d'audit (📦 B6.24, "
                 "📈 B6.25), ni Bonferroni. "
                 "Évités (règle de partage), de workbookIA B6 : les modèles f = 2x₁ + x₁x₂ (x = (3, 2), fond (1, 0) et (1, 2), "
                 "v = 3, 9, 4, 12, φ = (7, 2)), f = 2x₁ + x₁x₃ + x₂ (x = (2, 1, 3), fond (0, 2, 0) et (2, 2, 2), ligne "
                 "moyenne (1, 2, 1), φ = (3,5 ; −1 ; 2,5) et (4 ; −1 ; 3), variante (2, 2, 0)), f = x₁ + 2x₂ + x₁x₂ (client "
                 "(2, 1), fond (0, 1)), f = 2x₁ − 3x₂ (x = (4, 1), moyennes (3, 1) et (5, 2)), f = 2x₁ + 2x₂ et 4x₁ en "
                 "(1,5 ; 1,5), f = 3x₁ + x₂² (x₂ ∈ {0, 1, 2}, 7,67), f = x₁x₂ à x₂ = ±1, les poids w = (1,5 ; −2 ; 0,5), "
                 "(2, −1, 0,5), (0,5 ; −2 ; 0) avec w₀ = 1 et x = (4, 1, 7) ; les jeux fièvre/toux (2 et 5, φ = (1, 1)) et des "
                 "trois hommes (5, 4, 0 ; φ = (3, 2, 0) ; variante (5, 5, 0)) ; f(x) = 0,72, base 0,40, φ = 0,15 ; −0,05 ; "
                 "0,22 ; les parts 0,3 et −0,1 ; n = 4 et ses poids 1/4 et 1/12 comme exemple principal (1, 3, 3, 1 "
                 "coalitions, 16 coalitions, 8 arêtes) ; n = 3 et le poids 1/6 demandé seul ; n = 5 et 16 coalitions ; n = 8 "
                 "et B = 50 (12 800), n = 12 (204 800), n ∈ {10, 20, 50}, 2n + 2 048, ≤ 2^n − 2, 150 000 lignes par seconde, "
                 "10! = 3 628 800, 12!, 40 320, 479 millions, 4 096, T = 100 arbres et L = 31 feuilles, `max_features=12`, "
                 "`max_samples` 100 ; σ(x₁x₂ − 2) en (2, 3) (0,9820 ; 0,1192 ; 0,8628 ; 0,0530 ; 0,0353 ; 0,106 ; 0,212 ; "
                 "0,4314) ; f = x₁² + 3x₂ (en (2, −1) avec la référence 0 puis (1, 0), et en (1, 1)) ; f = x₀x₁ + x₂³ en "
                 "(1, 2, −1) et ses parts ; f = x₀² + 3x₁ ; f = min(x, 1) en 3 (références 0 et 2) ; f = x³ en 2 (9 au lieu "
                 "de 8) ; α³ avec n = 2 (0,0625 ; 0,5625 ; 0,21875 ; 0,3125) ; 5, 6, 7, 20, 100, 133, 134 et 200 intervalles, "
                 "la table des quatre règles (0,8301 … 0,8628), « 20 à 300 pas à 5 % », n/(n + 1), α = 0,63, onze points ; les "
                 "cartes de la fiche de B6 (A¹ = [[1, 0], [2, 1]], A² = [[0, 3], [1, 0]], A³ = [[2, 2], [0, 1]], α = (0,5 ; "
                 "−1 ; 0,5), [[1,5 ; −2], [0 ; 1]], [[1 ; 0], [0 ; 0,67]]), de ✏️ B6.4 (A¹ = [[1, 0, 0], [2, 1, 0], [3, 2, 1]], "
                 "A² = [[0, 1, 2], [0, 0, 1], [0, 0, 0]], leurs gradients, α = (1 ; −0,5), α′ = (−0,5 ; 1)) et de la docstring "
                 "de `grad_cam` ([[1, 2], [0, 1]], [[0, 1], [3, 0]]) ; les agrandissements 8 × 8 et 72 × 72, 12 pixels, "
                 "`layer4` ÷ 32 (1 × 1, 4 × 4, 7 × 7 ; 32, 96, 128, 160 et 224 pixels), `layer1` 56, les centres 16, 48 et 80, "
                 "le décalage de 16 pixels, Sobel ; (1, 2, 3) contre (10, 20, 30), les corrélations de B6.20 et B6.22 (0,96 ; "
                 "0,97 ; 0,59 ; …), 9/48, 15/48 et 22/48 ; l'exemple de Goldstein (y = 0,2x₁ − 5x₂ + 10x₂𝟙[x₃ ≥ 0], pentes "
                 "±5, 3 000 points) et Friedman ; les tranches d'âge (n = 200, 500, 300 ; 20/20/10/150, 150/50/30/270, "
                 "60/30/21/189 ; taux de base 0,20, 0,40, 0,30 ; 0,21 ; 0,25 ; 0,0375 ; 0,839), les matrices F et H "
                 "(72/48/19/361 et 256/64/40/280, variante 96/24/38/342), [[88, 12], [10, 40]], les docstrings de "
                 "`group_rates` ([1, 0, 1, 0, 1, 1, 0, 0]…) ; les taux de base 0,6 et 0,25, 0,24 et 0,5, 0,2 et 0,4, 0,5 ; les "
                 "paires (PPV, FNR) (0,7 ; 0,25), (0,8 ; 0,2), (0,8 ; 0,3), (0,75 ; 0,25), les FPR 0,080, 0,214, 0,055, 0,175, "
                 "FPR = 0,1 avec FNR = 0,2, PPV 0,716 et 0,889, p ≈ 0,286 ; les poids de repondération 1,65 ; 0,8375 ; 0,825 "
                 "et le taux pondéré 0,33, les groupes u × 6 et v × 4 (poids 0,75 ; 1,5 ; 2,0 ; 2/3) ; les TPR 0,856 et 0,912, "
                 "FPR 0,158 et 0,256, le TPR visé 0,80 (quantile 0,2 ; 0,799 et 0,800 ; 0,113 et 0,126), les seuils 0,356 et "
                 "0,524, le TPR visé 0,638 ; Adult (3 165 et 350, 6 604 et 1 987, 0,569 ; 0,663 ; 12 positifs sur 1 647 ; 89 "
                 "et 120 positifs, ± 0,088 ; 2 000 et 500 tirages ; Δ_EO < 0,07), la règle des quatre cinquièmes ; COMPAS, "
                 "Gender Shades, Obermeyer, Amazon, NIST ; California, Penguins, CIFAR-10, le ResNet du B1, le loup et le "
                 "husky, la radiographie, Mme D., le code postal, la fintech, les prêts ; de workbookIA B7 (voisin, sans "
                 "chapitre de maths) : les six graines 71,2 ; 70,5 ; 72,1 ; 69,8 ; 71,6 ; 70,9, les cinq valeurs 64,2 … et "
                 "64,9 …, les dix latences 12, 15, 11, 14, 13, 40, 12, 16, 13, 12, 900 × 10 ms + 100 × 200 ms, les PSI et les "
                 "luminosités ; et, de ce dépôt, l'exemple de M03 §8 (precision 0,6, recall 0,8, prévalences 30 % et 10 %, "
                 "FPR 0,229 et 0,059 ; le désabonnement 0,8 ; 0,6 ; 0,3 ; 0,2 ; 0,1), la table de M03.15 (48/12/28/112 et "
                 "16/4/18/162), les fonctions x e^y, x y² en (1, 2) et (2, 1), x²y + y² et x²y + y³ de M05b, les exemples des "
                 "docstrings de `integrate` (M02a), et ceux du stub `attribution` (n = 6 et ses poids 1/6, 1/30, 1/60 ; le "
                 "jeu s ↦ s² et ses dividendes 1 et 2 ; 5 u_{1,2} ; le champ (3x² + y, x) de x³ + x y et le chemin (0, 0) → "
                 "(1, 0) → (1, 2) ; le champ (y, 0) le long de (0, 0) → (1, 0) → (1, 1) et de (0, 0) → (0, 1) → (1, 1) ; 3x² de 1 à 3 puis à −1 (et l'ancien exemple, 3x² de 0 à 2 puis à 1, proche de `simpson(lambda x: x ** 3, 0, 2, 2)` de M02a) ; (0,5 ; 2 ; 1,5 ; 4) contre "
                 "(1, 8, 27, 64) et ρ = 0,8 ; (2, 2, 5, 1) contre (4, 3, 6, 0) ; (7, 7, 7)). "
                 "Conventions : joueurs numérotés de 0 à n − 1 dans le code, par des lettres ou de 1 à n sur papier ; "
                 "N le grand groupe, S̄ le complément de S ; v(∅) quelconque, d'où l'efficacité Σφ_i = v(N) − v(∅) ; la "
                 "référence d'un chemin est notée r (ni b, ni x′, ni « fond ») ; un chemin γ de paramètre t ∈ [0, 1] ; "
                 "« taux de base » p_g, « taux de détection » pour le TPR ; ρ de Spearman noté ρ_S quand il voisine avec la "
                 "corrélation ρ d'un couple gaussien. "
                 "`attribution` : NumPy et les modules `math`, `fractions` et `itertools` ; ni SciPy (`scipy.stats.rankdata`, "
                 "`spearmanr`, `pearsonr`, `scipy.integrate`), ni `np.corrcoef`, ni `np.cov`, ni le module `statistics` (`statistics.correlation(…, method='ranked')` est le ρ de Spearman), ni pandas ; les imports relatifs des modules de l'apprenant sont permis (`from .integrate import simpson`, M02a). Les fonctions écrivent les "
                 "briques : `coalition_weights(n_players, exact=False)` (les poids s!(n − 1 − s)!/n!, en `Fraction` ou en "
                 "flottants ; oracles `math.comb` et `Fraction`), `harsanyi_dividends(v, n_players)` (un jeu abstrait, "
                 "v : frozenset → réel, appelé une fois par coalition ; un dict des 2^n dividendes ; oracle : le jeu "
                 "reconstruit par v(S) = Σ_{T⊆S} d_T, et la valeur de Shapley moyennée sur les ordres par "
                 "`itertools.permutations`), `line_integral(field, points, n_sub=20)` (un champ appelé point par point, une "
                 "ligne brisée quelconque, Simpson sur chaque segment, un scalaire ; oracles `scipy.integrate.quad` et le "
                 "théorème du gradient) et `spearman_rho(x, y)` (rangs moyens, `nan` quand un échantillon est constant ; "
                 "oracle `scipy.stats.spearmanr`). Aucune fonction ne rend des valeurs de Shapley exactes (celles de B6.14 "
                 "viennent d'un modèle f, d'un point x et d'un fond, par l'énumération des coalitions), ni les parts des "
                 "coordonnées le long d'un segment : `line_integral` a un autre contrat que `integrated_gradients` de B6.18 "
                 "(un gradient vectorisé, un point et une référence, quatre règles, `n_steps` intervalles, une attribution "
                 "par coordonnée) ; aucune fonction de dépendance partielle (`partial_dependence` du plan est retirée : c'est "
                 "le nom de `sklearn.inspection.partial_dependence`, que B6.12 appelle), de taux par groupe ni d'écart "
                 "d'équité (B6.23). Les exercices ne reprennent pas les exemples du stub. "
                 "Pas de MML : le livre ne traite ni les jeux coopératifs, ni les intégrales de chemin, ni l'équité ; donc pas "
                 "de 📖. Références libres possibles, à vérifier en génération (annexes/ressources.md) : M. J. Osborne et "
                 "A. Rubinstein, A Course in Game Theory, ch. 14 (la valeur de Shapley) ; S. Barocas, M. Hardt et "
                 "A. Narayanan, Fairness and Machine Learning, ch. 3 (indépendance, séparation, suffisance ; workbookIA B6 le "
                 "cite : renvoyer à ses sections sans reprendre ses exemples) ; J. Kleinberg, S. Mullainathan et M. Raghavan "
                 "(2017) pour le §7 ; L. S. Shapley (1953) et J. C. Harsanyi (1963) pour le §2. "
                 "Parcours essentiel : l'unicité (∂ MB6.8), le partage multilinéaire (✏️ MB6.5), le 💼, le 🔨 des dividendes, "
                 "le 🔮, le 🎨, le 🛠️ et le 🏆 hors parcours. "
                 "**Durée** (session 69) : 12,1 h en parcours complet, 8,8 h en parcours essentiel (lecture 125 min, soit une "
                 "fiche d'environ 6 200 mots de prose ; 15 flashcards), au lieu des 8 h du plan et des 11 h visées : le "
                 "chapitre comble quatre lacunes qu'aucun chapitre publié ne couvre (jeux coopératifs et valeur de Shapley, "
                 "corrélation de rangs de Spearman, interpolation bilinéaire, écart de deux proportions indépendantes) et la "
                 "forme « scores » de l'impossibilité, avec la composition du §13 au bas de chaque fourchette et des durées "
                 "réalistes (les relectures de M25a à M28 ont relevé les durées de 20 à 40 %). Retirés du plan pour tenir : "
                 "l'estimation par permutations comme section et comme fonction (`shapley_monte_carlo`), les fonctions de "
                 "moyenne marginale et conditionnelle (une ligne de NumPy dans le 🔬), une ✏️ de Spearman (le 🔨 et le quiz "
                 "suffisent), un exercice de saturation (B6.Q7). Après les relectures : le 🏆 MB6.22 passe de 30 à 40 min (+1,1 h au-dessus des 11 h visées, pour la raison écrite ci-dessus).",
        "exercises": [
            ("MB6.Q1", "🧠", 1, 5, "Jeux coopératifs : ordres ou coalitions, poids d'une coalition, et ce que garantit chaque "
             "axiome", "§1 §2", "E"),
            ("MB6.Q2", "🧠", 1, 5, "Fixer une variable : moyenne marginale ou conditionnelle, courbes ICE parallèles ou "
             "non", "§3", "E"),
            ("MB6.Q3", "🧠", 1, 5, "Intégrales de chemin : boucle fermée, chemin parcouru à l'envers, champ qui n'est pas un "
             "gradient, fonction homogène", "§4", "E"),
            ("MB6.Q4", "🧠", 1, 4, "Grilles et rangs : interpolation bilinéaire, centres ou coins alignés, ex aequo et "
             "transformation strictement croissante", "§5 §6", "E"),
            ("MB6.Q5", "🧠", 1, 5, "Indépendance, séparation, suffisance : quel critère pour quelle phrase, et lesquels se "
             "contredisent", "§7", "E"),
            ("MB6.Q6", "🧠", 1, 4, "Tirer au sort entre deux seuils, repondérer, lire l'écart de deux taux : vrai ou faux",
             "§8", "E"),
            ("MB6.R1", "🔁", 1, 6, "Parties d'un ensemble, factorielles et combinaisons (R4, R8)", "§1", "E"),
            ("MB6.R2", "🔁", 1, 6, "La dérivée d'une fonction le long d'une courbe : gradient, vitesse et règle de la "
             "chaîne (M05b, M17)", "§4", "E"),
            ("MB6.R3", "🔁", 1, 6, "La loi conditionnelle d'un couple gaussien : une moyenne affine en la valeur observée "
             "(M25a)", "§3", "E"),
            ("MB6.1", "✏️", 2, 30, "Un conseil de quatre membres à vote pondéré : l'indice de Shapley-Shubik par les 24 "
             "ordres, un membre nul, deux membres de poids différents et de même pouvoir, et le nombre d'ordres tirés au "
             "hasard qui suffit (Hoeffding)", "§1", "E"),
            ("MB6.2", "✏️", 2, 30, "Trois hameaux partagent une conduite d'eau : la valeur de Shapley par les ordres, les "
             "dividendes de Harsanyi, le partage tronçon par tronçon, et les quatre axiomes vérifiés", "§2", "E"),
            ("MB6.3", "✏️", 2, 30, "Le rendement d'une parcelle selon la pluie et l'engrais : courbes ICE et dérivée croisée "
             "de deux modèles, puis la moyenne marginale et la moyenne conditionnelle quand pluie et engrais sont "
             "corrélés", "§3", "E"),
            ("MB6.4", "✏️", 2, 20, "Le travail de deux forces entre deux points : un champ de gradient le long de trois "
             "chemins, puis un champ qui n'en est pas un (Schwarz) le long de deux chemins", "§4", "E"),
            ("MB6.5", "✏️", 2, 30, "La variation d'un coût à trois facteurs (prix, quantité, taux de change) partagée entre "
             "les facteurs : le long du segment, puis par la moyenne des six chemins en escalier, et pourquoi les deux "
             "partages coïncident", "§4", ""),
            ("MB6.6", "✏️", 2, 25, "Des relevés de capteurs sur une grille 3 × 4 : la dérivée d'un indice régional par un "
             "réchauffement uniforme, puis la grille agrandie deux fois par interpolation bilinéaire, centres ou coins "
             "alignés", "§5", "E"),
            ("MB6.7", "✏️", 2, 30, "Un contrôle de pièces sur deux lignes de production aux taux de défauts différents : "
             "les taux de rejet sous la séparation, un tirage au sort entre deux seuils pour atteindre un taux de "
             "détection, et les poids qui rendent ligne et défaut indépendants", "§7 §8", "E"),
            ("MB6.8", "∂", 3, 35, "Unicité de la valeur de Shapley : les jeux d'unanimité forment une base, et les quatre "
             "axiomes imposent φ_i = Σ_{T ∋ i} d_T / |T|", "§2", ""),
            ("MB6.9", "∂", 2, 25, "Un score calibré dans un groupe vérifie p (1 − E[S | Y = 1]) = (1 − p) E[S | Y = 0] ; si "
             "deux groupes ont les mêmes moyennes de scores chez leurs positifs et chez leurs négatifs, leurs taux de "
             "base sont égaux ou le score est parfait", "§7", "E"),
            ("MB6.10", "∂", 2, 15, "Indépendance et séparation ne tiennent ensemble, quand les taux de base diffèrent, que "
             "pour une décision qui ignore le label ; la repondération P(g)P(y)/P(g, y) rend groupe et label "
             "indépendants sans changer leurs marges", "§7 §8", "E"),
            ("MB6.11", "🔗", 1, 15, "Pont : l'écart des taux de détection de deux laboratoires et son intervalle, par "
             "l'erreur type d'une différence de deux proportions, qui se lit avec le nombre d'échantillons positifs de "
             "chacun", "§8", "E"),
            ("MB6.12", "🗣️", 1, 10, "Expliquer avec trois amis qui partagent un taxi pourquoi on moyenne l'apport de "
             "chacun sur tous les ordres d'arrivée", "§1", "E"),
            ("MB6.E1", "💼", 1, 10, "« La valeur de Shapley est la seule répartition qui respecte quatre règles simples : "
             "lesquelles, et pourquoi suffisent-elles ? »", "§2", ""),
            ("MB6.13", "🔨", 1, 10, "Les poids des coalitions dans la valeur de Shapley, exacts ou en flottants", "§1",
             "E m:coalition_weights"),
            ("MB6.14", "🔨", 2, 25, "Les dividendes de Harsanyi d'un jeu donné par sa fonction caractéristique", "§2",
             "m:harsanyi_dividends"),
            ("MB6.15", "🔨", 2, 25, "L'intégrale d'un champ de vecteurs le long d'une ligne brisée, par la méthode de "
             "Simpson sur chaque segment", "§4", "E m:line_integral"),
            ("MB6.16", "🔨", 1, 20, "La corrélation de rangs de Spearman, ex aequo compris", "§6", "E m:spearman_rho"),
            ("MB6.17", "🔮", 1, 15, "Prédire l'intégrale d'un champ de gradient et d'un champ tournant le long d'une boucle "
             "triangulaire, dans un sens, dans l'autre et deux fois, puis vérifier", "§4", "p:MB6.15"),
            ("MB6.18", "🔬", 2, 25, "Deux mesures corrélées : la moyenne marginale (dépendance partielle) et la moyenne "
             "conditionnelle d'une même fonction, simulées pour plusieurs corrélations et comparées aux formules "
             "gaussiennes", "§3", "E"),
            ("MB6.19", "🎨", 1, 20, "Les lignes de niveau d'une fonction de deux variables, deux chemins entre les mêmes "
             "points, et l'intégrale du gradient cumulée le long de chacun", "§4", "p:MB6.15"),
            ("MB6.20", "🐛", 1, 20, "Chasse à l'erreur : des poids de coalition sans le facteur 1/n, des ex aequo classés "
             "dans l'ordre d'apparition, une interpolation linéaire aux poids échangés", "§1 §5 §6", "E"),
            ("MB6.21", "🛠️", 1, 20, "Un test de propriété sur des lignes brisées tirées au hasard : le chemin inversé "
             "change le signe, un segment coupé en deux ne change rien, un champ de gradient donne f(fin) − f(début)",
             "§4", "p:MB6.15"),
            ("MB6.22", "🏆", 3, 40, "Défi : les indices de Shapley-Shubik exacts d'un conseil de 25 membres, sans parcourir "
             "ses coalitions une à une, en comptant par taille et par poids celles où chaque membre est pivot", "§1",
             "p:MB6.13"),
        ],
    },
    {
        "id": "MB8", "dir": "mb8_gradient_politique", "hours": 13.3, "generation_sessions": 1, "mml": [],
        "summary": "Les outils statistiques du gradient de politique, hors de tout agent. D'abord la fonction score d'une "
                   "loi, d'espérance nulle, et l'information de Fisher ; l'estimateur « score » de la dérivée d'une "
                   "espérance, qui dérive une probabilité là où la dérivée par le chemin de M25b échoue ; la réduction de "
                   "sa variance par une variable de contrôle, la baseline optimale et les baselines de groupe. Puis la "
                   "valeur d'une politique softmax tabulaire, dérivée à partir du système de Bellman de M26 : la loi "
                   "d'occupation actualisée et l'avantage, d'espérance nulle ; les retours à k pas et le λ-retour, "
                   "démontrés à partir du télescopage de M26. Enfin l'échantillonnage d'importance (poids, taille "
                   "effective, poids tronqués) et deux estimateurs de la KL par échantillons ; le modèle de Bradley-Terry "
                   "des comparaisons par paires et la cote Elo ; le principe variationnel de Gibbs, la loi qui maximise "
                   "une moyenne moins β fois une KL. workbookIA B8 applique ces outils à REINFORCE, à GAE, à PPO, au "
                   "modèle de récompense et à DPO.",
        "objectives": [
            "Calculer la fonction score d'une loi usuelle, vérifier qu'elle est d'espérance nulle, et calculer "
            "l'information de Fisher de deux façons.",
            "Dériver l'espérance d'une fonction, même discontinue, par rapport au paramètre d'une loi par la méthode du "
            "score, et dire quand la dérivée par le chemin est préférable.",
            "Réduire la variance d'une estimation de Monte-Carlo par une variable de contrôle, et calculer la baseline "
            "optimale d'un estimateur score.",
            "Distinguer une baseline sans biais (la moyenne des autres tirages) d'une baseline qui biaise (la moyenne du "
            "groupe, tirage compris).",
            "Calculer le gradient de la valeur d'une politique softmax tabulaire par le système de Bellman, et l'écrire "
            "avec la loi d'occupation actualisée et l'avantage.",
            "Écrire un retour à k pas et un λ-retour, les relier aux erreurs TD, et calculer leur biais quand les valeurs "
            "estimées sont fausses.",
            "Estimer une espérance sous une loi à partir de tirages d'une autre, calculer la taille effective, tronquer "
            "des poids, et estimer une KL par k₁ ou k₃.",
            "Ajuster un modèle de Bradley-Terry à un tournoi, dire quand ses forces existent et ce qu'elles identifient, "
            "et lire une mise à jour Elo comme un pas de gradient.",
            "Trouver la loi qui maximise une moyenne moins β fois la KL à une loi de référence, et sa valeur.",
        ],
        "sections": [("§1", "La fonction score d'une loi : espérance nulle et information de Fisher"),
                     ("§2", "Dériver une espérance par le score, et comparer à la dérivée par le chemin (M25b)"),
                     ("§3", "Réduire la variance : variables de contrôle, baseline optimale et baselines de groupe"),
                     ("§4", "Le gradient de la valeur d'une politique, sous forme matricielle (après M26)"),
                     ("§5", "Retours à k pas et λ-retour"),
                     ("§6", "L'échantillonnage d'importance : poids, taille effective, poids tronqués ; estimer une KL par "
                            "échantillons"),
                     ("§7", "Comparaisons par paires : le modèle de Bradley-Terry et la cote Elo"),
                     ("§8", "Le principe variationnel de Gibbs : maximiser une moyenne moins β fois une KL")],
        "teaches": ["fonction score d'une loi s_θ(x) = ∂_θ ln p_θ(x) (le score « en θ », à distinguer du score en x de "
                    "MB5) ; scores des lois de Bernoulli, binomiale, de Poisson, exponentielle (taux) et normale (moyenne) "
                    "; E_θ[s_θ(X)] = 0 quand le support ne dépend pas de θ (contre-exemple : la loi uniforme sur [0, θ]) ; "
                    "le score total d'un échantillon s'annule au maximum de vraisemblance (rappel M04, M13a)",
                    "information de Fisher I(θ) = Var(s_θ) = −E[∂²_θ ln p_θ] (démontrée sous l'échange de la dérivée et de "
                    "l'intégrale, admis) ; I(θ) d'un échantillon i.i.d. = n I(θ) ; au second ordre, KL(p_θ ‖ p_θ′) ≈ ½ "
                    "I(θ)(θ′ − θ)²",
                    "la dérivée d'une espérance par le score : d/dθ E_θ[f(X)] = E_θ[f(X) s_θ(X)] (lois discrètes, puis à "
                    "densité), valable pour f discontinue (une indicatrice) ; l'estimateur de Monte-Carlo sans biais et sa "
                    "variance ; comparée à la dérivée par le chemin de M25b §7 (rappel) : même espérance, variances "
                    "différentes, le chemin nul sur une indicatrice",
                    "variables de contrôle (control variates) : f − c(h − E[h]) sans biais, c* = Cov(f, h)/Var(h), "
                    "variance (1 − ρ²)Var(f) ; pour l'estimateur score, toute constante b donne (f − b)s sans biais (E[s] "
                    "= 0) ; baseline optimale b* = E[f s²]/E[s²] (une moyenne de f pondérée par s²), différente de E[f] en "
                    "général ; une mauvaise baseline augmente la variance",
                    "baselines de groupe : sur n tirages i.i.d., la moyenne des n − 1 autres f est une baseline sans biais "
                    "; la moyenne des n, tirage compris, multiplie l'estimateur par (n − 1)/n ; diviser par l'écart-type "
                    "du groupe garde le signe de chaque terme, mais l'espérance n'est plus exactement proportionnelle à la "
                    "dérivée",
                    "le gradient de la valeur d'une politique softmax tabulaire (le prolongement promis par M26) : dériver "
                    "V = r_π + γP_πV donne ∂V = (I − γP_π)⁻¹(∂r_π + γ(∂P_π)V) ; ∂V(s₀)/∂z(s, a) = ν_{s₀}(s)/(1 − γ) · π(a "
                    "| s) A^π(s, a), avec la loi d'occupation actualisée ν_{s₀} de M26 §5 et l'avantage A^π = Q^π − V^π ; "
                    "Σ_a π(a | s)A^π(s, a) = 0 ; la forme Σ_s ν(s) Σ_a π(a | s) ∂ln π(a | s) Q^π(s, a) ; la jacobienne de "
                    "la softmax (rappel M17) ; la pondération (1 − γ)γᵗ des états visités, énoncée ; vérification par "
                    "différences finies (M05a)",
                    "retours à k pas G^(k) = Σ_{j<k} γʲ R_{t+j} + γᵏ V(S_{t+k}) ; G^(k) − V(S_t) = Σ_{l<k} γˡ δ_{t+l} (le "
                    "télescopage de M26 §8, tronqué) ; le λ-retour, moyenne des G^(k) de poids (1 − λ)λ^{k−1}, et G^λ − "
                    "V(S_t) = Σ_l (γλ)ˡ δ_{t+l} (démontré) ; λ = 0 et λ = 1 ; E[δ_t | S_t = s, A_t = a] = A^π(s, a) quand "
                    "V = V^π ; biais γᵏ(Pᵏ e)(s) d'une valeur estimée fausse de e, et une variance qui croît en général "
                    "avec k",
                    "échantillonnage d'importance (importance sampling) : E_p[f] = E_q[(p/q) f] quand q > 0 là où p f ≠ 0 "
                    "; sans biais ; E_q[w] = 1 ; variance, et poids de variance infinie ; poids auto-normalisés (biaisés, "
                    "consistants, et seuls possibles quand p n'est connue qu'à une constante près) ; taille effective "
                    "(Σw)²/Σw² de Kish ; poids calculés en log, exp(ln p − ln q) ; poids tronqués min(w, c) : un biais "
                    "contre une variance ; lien avec Horvitz-Thompson (M20 §5)",
                    "estimer KL(q ‖ p) par des tirages de q, avec w = p/q : k₁ = −ln w (sans biais, de signe quelconque) "
                    "et k₃ = (w − 1) − ln w (sans biais car E_q[w] = 1, et ≥ 0 terme à terme : −ln est convexe, au-dessus "
                    "de sa tangente en 1, M05a)",
                    "le modèle de Bradley-Terry : P(i bat j) = σ(β_i − β_j) ; vraisemblance d'un tournoi ; les forces ne "
                    "sont identifiées qu'à une constante près (contrainte Σβ = 0) ; une régression logistique sans "
                    "constante sur des différences d'indicatrices (M13a) ; équations du maximum de vraisemblance : "
                    "victoires observées = victoires attendues ; existence (le graphe des victoires est fortement connexe, "
                    "énoncé ; un invaincu n'a pas de force finie) ; l'algorithme de Zermelo (MM, monotone, admis) ; la "
                    "cote Elo, un pas de gradient stochastique sur la log-vraisemblance d'un match",
                    "le principe variationnel de Gibbs : pour une loi de référence π_ref et β > 0, E_π[r] − β KL(π ‖ "
                    "π_ref) = β ln Z − β KL(π ‖ π*), avec π* ∝ π_ref e^{r/β} et Z = E_ref[e^{r/β}] (démontré par KL ≥ 0, "
                    "M06) ; le maximum β ln Z ; les limites β → 0 (le meilleur choix) et β → ∞ (π_ref) ; r déterminée par "
                    "π* et π_ref à une constante près ; les cas particuliers déjà vus : Boltzmann (M17), Hedge (M14), la "
                    "température d'une loi (M28)"],
        "requires": [("dérivée d'un logarithme et d'une composée", "R7"),
                     ("lois de Bernoulli, binomiale, de Poisson, exponentielle et normale ; espérance, variance, variance "
                      "d'une somme de variables indépendantes", "M02b"),
                     ("estimateur sans biais, erreur type d'une moyenne, covariance et corrélation, loi des grands nombres",
                      "M02c"),
                     ("maximum de vraisemblance, log-probabilités, famille exponentielle (aperçu)", "M04"),
                     ("différences finies centrées et choix du pas, Taylor d'ordre 2, une fonction convexe est au-dessus "
                      "de ses tangentes, log-sum-exp", "M05a"),
                     ("divergence KL et sa positivité (inégalité de Gibbs), entropie", "M06"),
                     ("sigmoïde, logit, log-loss, régression logistique comme modèle probabiliste ; la convexité de "
                      "log-somme-exp (sa dérivée seconde est une variance)", "M13a"),
                     ("poids exponentiels : l'algorithme Hedge", "M14"),
                     ("puissances d'une matrice d'adjacence et chemins d'un graphe", "M16"),
                     ("loi de Boltzmann et température, jacobienne de la softmax diag(p) − ppᵀ", "M17"),
                     ("gradient estimé sans biais sur un échantillon, variance d'une moyenne de B tirages", "M19"),
                     ("estimateur de Horvitz-Thompson ; tableaux à trois axes et einsum", "M20"),
                     ("dériver une espérance par rapport à un paramètre de la loi : la dérivée par le chemin, l'hypothèse "
                      "de domination, l'indicatrice où l'échange échoue ; espérance conditionnelle et totale", "M25b"),
                     ("MDP, politique, chaîne induite P_π et r_π, valeur d'une action Q^π, système de Bellman d'une "
                      "politique fixée, loi d'occupation actualisée, erreur TD et télescopage ; tableaux (actions, états, "
                      "états)", "M26"),
                     ("la probabilité a posteriori minimise la log-loss espérée (la log-loss est une règle de score propre)",
                      "M27"),
                     ("la température d'une loi donnée par ses probabilités", "M28")],
        "frontieres": ["B8.1", "B8.3", "B8.4", "B8.5", "B8.6", "B8.Q4", "B8.Q6", "B8.Q7", "B8.Q11", "B8.17", "B8.18",
                       "B8.19", "B8.25", "B8.11", "B8.E2", "B8.E4"],
        "mymath": {"module": "policy_gradient.py",
                   "functions": ["score_function_gradient", "policy_gradient_exact", "importance_weights",
                                 "bradley_terry_fit"]},
        "reading_minutes": 160,
        "flashcards": 16,
        "notes": "Frontières : ∂ B8.7 (le gradient de politique en une étape : la loi d'un épisode μ(s₀)Π π_θ(a_t | "
                 "s_t)P(s_{t+1} | s_t, a_t), l'astuce de la log-dérivée pour une loi discrète et « où as-tu supposé p > 0 "
                 "», l'environnement qui disparaît du log d'un produit, le score d'espérance nulle vérifié sur une softmax "
                 "à deux actions (z₀, z₁), la causalité et la forme γᵗG_t, la baseline b(s) sans biais et pourquoi pas "
                 "b(s, a), la variance sur un bandit à deux actions de logits (0, z) en z = 0, récompenses 2 et 4, "
                 "minimale en b = 3), ✏️ B8.3 (le gradient du log-softmax à trois actions, un pas, l'entropie), ✏️ B8.4 "
                 "(GAE à la main sur un rollout avec troncature), ✏️ B8.5 (l'objectif clippé de PPO, ses quatre cas, la "
                 "fraction clippée), ✏️ B8.6 (la loss de Bradley-Terry d'une paire, sa dérivée, le choix inverse, +10 ; la "
                 "loss DPO, la récompense implicite, la marge, β), 📦 B8.17 (la variance du gradient avec et sans baseline "
                 "mesurée sur des politiques, « la baseline qui minimise la variance est une moyenne pondérée par ‖∇ln π‖² "
                 "»), 🔨 B8.18, B8.19 et B8.25 (`compute_gae`, `explained_variance`, `clipped_surrogate`, "
                 "`bradley_terry_loss`, `dpo_loss`), 📄 B8.11 (l'article de PPO), les quiz B8.Q6 (le score de face d'une "
                 "pièce à θ = 0,3, les baselines qui biaisent), B8.Q7 (δ, les poids (γλ)ˡ de GAE, la troncature) et B8.Q11 "
                 "(l'avantage GRPO d'un groupe (1 ; 0 ; 0 ; 0)), 💼 B8.E2 (PPO et le clip) et B8.E4 (PPO ou DPO) ; B8.1 "
                 "(cible DQN puis Double DQN) et B8.Q4 (la surestimation) restent des frontières de M26, dont le §8 a le "
                 "biais du maximum et l'estimateur double : MB8 n'y revient pas. MB8 enseigne les outils dans d'autres "
                 "cadres : la fonction score en statistique (lois de Poisson, exponentielle, binomiale, normale) et "
                 "l'estimateur score de la dérivée d'une espérance, comparé à la dérivée par le chemin de M25b ; la "
                 "baseline optimale démontrée en général comme une variable de contrôle (∂ MB8.9, pour un paramètre réel "
                 "et une loi quelconque, jamais sur un bandit ni une politique) ; le gradient de la valeur d'une politique "
                 "obtenu en dérivant le système de Bellman de M26 (∂ MB8.10), une autre démonstration, sans trajectoire, "
                 "sans log d'un produit et sans causalité ; le λ-retour comme moyenne des retours à k pas, démontré par le "
                 "télescopage de M26 dans la fiche et chiffré en espérance sur une chaîne (✏️ MB8.4), sans rollout ; "
                 "l'échantillonnage d'importance d'un sondage (✏️ MB8.5) et d'un événement rare (🔬 MB8.18), avec des poids "
                 "tronqués min(w, c) de statisticien, jamais clip(ρ, 1 − ε, 1 + ε) ni un min de deux objectifs ; "
                 "Bradley-Terry sur un tournoi (maximum de vraisemblance, identifiabilité, Elo), sans récompense ni paire "
                 "« choisie, rejetée » ; le principe de Gibbs sur des menus. Cadres : des clients à un guichet, la durée "
                 "d'un appel, une attente au téléphone, des graines en godet, un camion de crêpes, l'état d'une route, un "
                 "panel de sondage, un tournoi de babyfoot, un club d'échecs, une cantine, un événement rare ; jamais un "
                 "agent, un épisode de jeu, CartPole ni Atari, un bandit à deux bras, une pièce « pile ou face » de "
                 "paramètre θ avec un gain 1 pour pile, un modèle de récompense, un modèle de langue, un token, une "
                 "réponse « choisie » ou « rejetée », un prompt, ni PPO, DPO ou GRPO chiffrés (la fiche les nomme dans « "
                 "Et maintenant »). Ce que fait chaque exercice délicat. ∂ MB8.8 démontre E[s_θ] = 0 et Var(s_θ) = −E[∂²_θ "
                 "ln p_θ] pour une famille à densité dont le support ne dépend pas de θ, l'échange de la dérivée et de "
                 "l'intégrale admis (sa justification par domination est celle de M25b §7), les applique aux lois de "
                 "Poisson et exponentielle, puis montre ce qui tombe pour la loi uniforme sur [0, θ] (score −1/θ "
                 "d'espérance non nulle, terme de bord f(θ)/θ) ; il ne traite pas une loi discrète en demandant où l'on "
                 "suppose p > 0 (∂ B8.7.1) ni une softmax à deux actions (∂ B8.7.3). Les quiz : MB8.Q1 ne chiffre ni le "
                 "score d'une issue d'une loi de Bernoulli ni son espérance sur les deux issues (B8.Q6 a–b ; la fiche peut "
                 "définir le score sur une Bernoulli, sans exercice) ; MB8.Q2 ne reprend pas les options de B8.Q6 c–e "
                 "(moyenne des épisodes précédents, critique, retour du même pas, b = 1 000) : ses baselines sont des "
                 "nombres ou des moyennes de tirages ; MB8.Q3 ne demande ni le poids (γλ)ˡ d'une erreur TD, ni ce que "
                 "devient l'estimation pour λ = 0 ou λ = 1, ni quel λ donne la plus forte variance (B8.Q7 b–e) : il porte "
                 "sur la loi d'occupation, l'avantage d'espérance nulle et les poids (1 − λ)λ^{k−1} des retours à k pas, "
                 "de somme 1 ; MB8.Q4 et MB8.Q5 n'ont ni ratio de PPO ni loss de paire. ✏️ MB8.1 prend une loi "
                 "exponentielle de taux θ (score 1/θ − x) et un seuil c : d/dθ P(X > c) par la formule fermée, l'espérance "
                 "de l'estimateur 1{X > c}(1/θ − X), la dérivée nulle par le chemin X = ξ/θ, et la variance à un tirage en "
                 "forme fermée ; jamais la gaussienne et le seuil de M25b §7, ni l'ampoule de M25b (moyenne 2 ans, "
                 "remplacement à 3 ans, θc = 1,5, e^{−1,5}). ✏️ MB8.2 prend une loi à trois issues, B(2, θ) avec θ ≠ 0,3 "
                 "et θ ≠ ½, et un prix f qui n'est pas affine en x : b* = E[f s²]/E[s²] y diffère de E[f] et ne rend pas "
                 "la variance nulle ; jamais une loi à deux issues où la baseline optimale annule la variance (∂ B8.7.6). "
                 "∂ MB8.9 démontre, pour un θ réel, que Var((f − b)s) est minimale en b*, puis les baselines de groupe : "
                 "sur n tirages i.i.d., (1/n)Σ(f_i − f̄_{−i})s_i est sans biais, et (1/n)Σ(f_i − f̄)s_i en vaut exactement "
                 "(n − 1)/n fois ; la fiche ajoute que diviser par l'écart-type du groupe garde le signe de chaque terme, "
                 "sans exercice chiffré (B8.Q11 c). ✏️ MB8.3 : deux emplacements, une politique softmax dans l'un (deux "
                 "actions, rester ou partir), une politique fixée dans l'autre, γ = 0,7 : P_π, r_π, V (un système 2 × 2), "
                 "la colonne utile de (I − γP_π)⁻¹, Q et A des deux actions de l'état qui choisit, puis ∂V/∂z par la "
                 "formule ; ses logits ne sont jamais (0, z) en z = 0, et les deux valeurs d'action servent à la formule, "
                 "jamais à désigner la meilleure ni à supposer une politique optimale (∂ 26.8.2). ∂ MB8.10 dérive V = r_π "
                 "+ γP_πV et réécrit le résultat avec ν_{s₀}, Q^π puis A^π (Σ_a π(a | s)A^π(s, a) = 0) ; la fiche énonce "
                 "que ν pèse un état visité au pas t par (1 − γ)γᵗ, et que l'estimateur de workbookIA B8 omet ce poids, "
                 "sans exercice dessus (∂ B8.7.4). ✏️ MB8.4 calcule des espérances sur une chaîne connue : le biais "
                 "γᵏ(Pᵏe)(s) des retours à 1 et 2 pas pour une erreur e sur les valeurs, les poids (1 − λ)λ^{k−1}, et le "
                 "biais du λ-retour quand l'erreur vaut c partout (une série géométrique) ; aucun rollout, aucune suite de "
                 "récompenses observées, aucun drapeau terminated ou truncated, aucune récurrence Â_t = δ_t + γλÂ_{t+1} "
                 "déroulée sur une suite (c'est `compute_gae`). ✏️ MB8.5 : un panel en ligne (la loi q des classes d'âge) "
                 "contre le recensement (la loi p), poids p/q, E_q[w] = 1, estimation repondérée, sa variance à un tirage, "
                 "taille effective de Kish d'un petit échantillon, poids tronqués à c et leur biais, puis KL(q ‖ p), k₁ = "
                 "−ln w et k₃ = (w − 1) − ln w classe par classe et leurs espérances ; jamais un ratio π_θ/π_old, un "
                 "avantage, un ε de clip, ni les lois (0,5 ; 0,5) et (0,6 ; 0,4). ✏️ MB8.6 : un tournoi de babyfoot ; deux "
                 "clubs (la différence de forces en forme fermée), puis trois clubs avec des forces proposées dont on "
                 "vérifie les équations du maximum de vraisemblance, une probabilité de victoire, une mise à jour Elo "
                 "(échelle 400/ln 10, coefficient k), et pourquoi un club invaincu n'a pas de force finie ; jamais la loss "
                 "d'une paire et sa dérivée en chaîne (✏️ B8.6 a–e), ni un écart de 1,5, 1,2 ou 3,0, ni « ajouter 10 aux "
                 "deux » comme question (l'identifiabilité passe par Σβ = 0). ✏️ MB8.7 : trois plats, une loi actuelle "
                 "π_ref, des satisfactions r, deux valeurs de β ; la loi π* ∝ π_ref e^{r/β}, sa valeur β ln Z, comparée à "
                 "π_ref (KL nulle) et au meilleur plat seul ; la fiche démontre le principe en cinq lignes par KL ≥ 0 (une "
                 "extension de la loi de Boltzmann de M17, et du sujet B de CP6.8, au choix, dont MB8 ne dépend pas), et "
                 "dit en une ligne que r est déterminée par π* et π_ref à une constante près ; aucun exercice ne calcule β "
                 "ln(π*/π_ref) pour deux issues ni leur différence (la récompense implicite et la marge de ✏️ B8.6 f–j). 🔗 "
                 "MB8.11 : la loss de substitution −(1/n)Σ(f(x_i) − b) ln p_θ(x_i) sur le taux d'une loi de Poisson, sa "
                 "dérivée, les f(x_i) et b tenus fixes (ce que les bibliothèques appellent stop-gradient), puis des f "
                 "standardisés dans le batch ; jamais ln π(a | s), G_t, un épisode ni un retour. Le 🔮 MB8.17, le 🔬 MB8.18 et "
                 "le 🏆 MB8.21 portent sur des lois (une binomiale, une normale, une loi de Poisson ou exponentielle), "
                 "jamais sur des politiques ni des épisodes. Rappels sans les refaire : M26 §4 et §5 (MDP, P_π, r_π, Q^π, "
                 "le système de Bellman, la loi d'occupation actualisée ν_s = (1 − γ)e_s(I − γP)⁻¹ et V(s) = ν_s r/(1 − "
                 "γ)) et §8 (l'erreur TD, son espérance, le télescopage, ∂ M26.13) : 🔁 MB8.R2 ; M25b §7 (la dérivée par le "
                 "chemin, la domination, l'indicatrice où elle échoue et la méthode du score nommée pour MB8) : 🔁 MB8.R3 ; "
                 "M17 §7 (Boltzmann, diag(p) − ppᵀ) : 🔁 MB8.R1, qui ne calcule ni le gradient de ln softmax(z)_a en des "
                 "logits donnés ni un pas sur ces logits (✏️ B8.3) ; M13a (logistique, log-loss), M06 (KL ≥ 0), M05a (une "
                 "fonction convexe au-dessus de sa tangente), M20 §5 (Horvitz-Thompson), M14 §4 (Hedge), M28 §5 (la "
                 "température d'une loi) et M02c sont cités dans la fiche. GAE n'est pas dans M26 (son télescopage est le "
                 "cas λ = 1) : MB8 ne le présente pas comme un rappel, et ne le nomme que dans « Et maintenant ». "
                 "Conventions : s_θ(x) = ∂_θ ln p_θ(x), le score en θ, distinct du score en x de MB5 (∇ₓ ln p) : un "
                 "encadré 📐 le dit ; la loi exponentielle par son taux θ (densité θe^{−θx}, moyenne 1/θ ; M25b la prenait "
                 "par sa moyenne), un encadré ⚠️ le dit ; le MDP comme en M26.14 : P[a, s, t], r[a, s] = r(s, a) = Σ_t P[a, s, t] R[a, s, t] "
                 "(M26.14 range les récompenses R[a, s, s2] de chaque transition), et les logits z[s, a] rangés comme pi[s, "
                 "a] ; les lois en lignes et les valeurs en colonnes (M26) ; en échantillonnage "
                 "d'importance, les tirages viennent de q (la loi de proposition) et w = p/q ; la KL estimée est KL(q ‖ "
                 "p), avec des tirages de q ; Elo en base 10 et à l'échelle 400 (β = R ln 10/400). Les γ des exercices "
                 "sont pris parmi 0,6 et 0,7, et λ parmi 0,6 et 0,7 : jamais γ = 0,5, 0,8, 0,9, 0,95, 0,99, ni 0,75 et "
                 "0,85 (les exemples de `markov` et la boutique de M26), jamais λ = 0,5, 0,8 ni 0,95, jamais γλ = 0,45, "
                 "0,855 ni 0,9405. `policy_gradient` (fonctions rangées dans l'ordre des sections) : NumPy et `math` "
                 "permis, de `np.linalg` seulement `solve` et `matrix_rank` (dans `policy_gradient_exact`) ; ni SciPy ni "
                 "scikit-learn ; un import relatif de `bellman_linear_solve` (M26) est permis. Oracles des tests : des "
                 "sommes exactes et `fractions` pour `score_function_gradient` (et l'absence de biais vérifiée sur des "
                 "lois discrètes par énumération) ; des différences finies centrées sur des valeurs calculées par "
                 "`np.linalg.solve` pour `policy_gradient_exact` ; NumPy, `scipy.special.logsumexp` et l'invariance par un "
                 "facteur commun pour `importance_weights` ; `scipy.optimize.minimize` sur la log-vraisemblance centrée et "
                 "`sklearn.linear_model.LogisticRegression(fit_intercept=False, penalty=None)` sur les différences "
                 "d'indicatrices pour `bradley_terry_fit` ; jamais une autre fonction de l'apprenant. Contrats distincts "
                 "de `mylearn` B8 : `score_function_gradient` rend une moyenne de (f − b)s et son erreur type à partir de "
                 "valeurs et de scores déjà calculés (ni épisode, ni log-probabilité d'action, ni retour) ; "
                 "`policy_gradient_exact` est exacte, tabulaire, sans échantillon ; `importance_weights` prend deux "
                 "log-densités (`log_target`, `log_proposal` : ni `ratio` ni `log_pi_old`) et rend des poids et une taille "
                 "effective, sans avantage, sans clip(ρ, 1 − ε, 1 + ε) ni loss (`clipped_surrogate`) ; `bradley_terry_fit` "
                 "rend des forces centrées ajustées sur une matrice de victoires, ni une loss ni un gradient "
                 "(`bradley_terry_loss`). Aucune fonction de λ-retour (`lambda_return` serait `compute_gae` à une addition "
                 "près), de KL estimée, de loi de Gibbs (`temper` de M28 et `hedge_weights` de M14 en sont des cas), ni de "
                 "variance expliquée. Les exercices ne reprennent pas les exemples du stub : f = (3, 0, 2, 5) et s = (0,5 "
                 "; −1 ; 0 ; 1,5) (2,25 ; 1,7854 ; 2,0 ; 2,1667) ; le MDP où l'action 0 mène à l'état 0 et l'action 1 à "
                 "l'état 1, r = [[1, 0], [0, 2]], logits nuls, γ = 0,6 (V = (1,625 ; 2,125), 0,30625, 0,43125) ; les "
                 "log-densités (−1 ; −0,5 ; −0,5 ; −2) et (−1,5 ; −1 ; −1 ; −1) (3,4063) et la troncature à 2 (1,8) ; les "
                 "tournois [[0, 4], [1, 0]] (ln 4 ; ±0,6931) et [[0, 4, 2], [1, 0, 3], [1, 2, 0]] (0,7464 ; −0,2949 ; −0,4516). "
                 "Évités (règle de partage), de workbookIA B8 : CartPole et ses nombres (4,8 ; 0,4189 ; 2,4 et 12° ; 500 "
                 "et 475 ; 22,3, 19, 8 et 119 ; 19,5 à 24,8 ; 11,8 et 1,2 ; la règle θ + 0,5θ̇ > 0 ; 42 et 202 ; 10⁴ et "
                 "10¹⁰⁰ cases), Atari, AlphaGo Zero, OpenAI Five, InstructGPT, DeepSeekMath, CleanRL, MuJoCo ; la pièce "
                 "p_θ(pile) = θ avec le gain 1 pour pile (dérivée 1), θ = 0,3 et le score −1,43 ; pierre-feuille-ciseaux "
                 "et pair ou impair ; le bandit gaussien 10 et 11 (σ = 1 ; 0,25 ; 5,27 ; 0,50 ; b = 10,5) ; le bandit "
                 "déterministe 2 et 4 aux logits (0, z) en z = 0 (0,5 ; b = 3 ; 2,25 ; 1,5 ; variante 0,25) ; les logits "
                 "(0,3 ; −0,2) (0,6225 ; 0,3775), (0,5 ; 1,5 ; −0,5) (0,2447 ; 0,6652 ; 0,0900 ; Â = −2 ; pas 0,1 ; −0,682 "
                 "; 0,0687 ; 0,1170) et (ln 2 ; ln 6 ; 0) (0,67) ; les entropies ln 2, 0,325, 0,056, 0,832, ln 3 et c = "
                 "0,01 ; les ratios (0,7 ; 1,1 ; 1,35) avec (−1 ; 2 ; −1) (−0,0167 ; −0,6667 ; 0,3333), (1,4 ; 0,6 ; 0,75 "
                 "; 1,35) avec (2,0 ; 1,5 ; −1,2 ; −0,8) (2,4 ; 0,9 ; −0,96 ; −1,08 ; −0,315 ; −0,375), (0,5 ; 1,0 ; 1,5) "
                 "avec 1 (−0,9), ε = 0,1, 0,2, 0,3 et 0,4, le ratio 1,15, ρ = 1,5, e^{0,3} = 1,35 et les log-probabilités "
                 "−0,9 et −1,2 ; la KL approchée de (0,5 ; 0,5) contre (0,6 ; 0,4) (0,0204 ; −0,182 ; 0,018) et les KL "
                 "0,027, 0,003, 0,02, 0,012, 0,004 et 0,0008 ; Bradley-Terry Δ = 1,5 (0,818 ; 0,201 ; −0,182), 2,3 et 1,1 "
                 "(0,769 ; 0,263 ; −0,231 ; 1,463), d = 3,0 (0,953 ; 0,0486 ; −0,0474), (0, 0) → ln 2, (−1 000 ; 1 000) → "
                 "2 000, +10 ; DPO −20, −23, −21, −22 (0,2 ; 0,598 ; 1,0 ; 0,313), −35,2, −38,9, −36,0, −37,5 (0,08 ; 0,22 "
                 "; 0,589 ; 0,287 ; −0,0445), [−10 ; −12], [−11 ; −9], [−10,5 ; −11], [−10,5 ; −10] (0,1 ; −0,2 ; 0,7213), "
                 "β = 0,02, 0,04, 0,1 et 0,5 ; le groupe (1 ; 0 ; 0 ; 0) (1,73 et 1,5), G = 64, 8 réponses ; GAE : r = 1, "
                 "V = (2,0 ; 1,5 ; 0,8) (δ = (0,35 ; 0,22 ; 0,2), (0,4895 ; 0,31 ; 0,2), (2,71 ; 1,9 ; 1), 0,7 et 0,83), V "
                 "= (4,0 ; 3,8 ; 2,0 ; 2,4) et (3,8 ; 3,6 ; 2,4 ; 2,6) (0,42 ; 0,44 ; 1,16 ; 0,94 ; 1,9637 ; 0,7962), (1, "
                 "1, 1) avec γ = 0,5 (1,75 ; 1,5 ; 1), V = 0,5 et (0,5 ; 0,5 ; 2,0) (1,3775 ; 0,95 ; 2,3), r = 1, γ = 0,9, "
                 "V = 3,0 et 2,5 (δ = 0,25) ; la variance expliquée de (1 ; 2 ; 3 ; 4) contre (1,5 ; 1,5 ; 3,5 ; 3,5) "
                 "(0,8), (6 ; 7 ; 8 ; 9), [1, 2, 3] contre [1, 2, 4] (0,8571) ; les cibles DQN (2,0 ; 3,5 ; 1,2) (4,15) et "
                 "(4,1 ; 3,0 ; 0,5) (2,8), [[0,4 ; 3,9] ; [1,1 ; 2,0]], les tableaux de ✏️ B8.1 (γ = 0,99 ; 14,56 ; 42,18 "
                 "; 12,88 ; 40,80 ; 13,474) ; Huber x = (0,6 ; −2,4 ; 3,2) et δ = 1,5, x = 3 et le seuil 2, x = 0,5 ; le "
                 "biais du maximum de 2, 4 et 10 gaussiennes (0,56 ; 1,03 ; 1,54) et trois estimations ±1 (0,75) ; (1 − "
                 "0,005)²⁰⁰ ≈ 0,37, la mémoire de 10 000 et les mini-batches de 64 ; les comptes et réglages (10 934, 67 "
                 "586, 4 610, 4 545, 9 155, 976, 500 000, 2,5 × 10⁻⁴, c₁ = 0,5) et les Fermi de 🧮 B8.8 ; Christiano (900 "
                 "comparaisons), 40 annotateurs, 4 à 9 réponses et 36 paires, 73 % ; de workbookIA B7 (MB8 ne compare pas "
                 "de graines), les graines 71,2 ; 70,5 ; 72,1 ; 69,8 ; 71,6 ; 70,9 et 64,2 ; 65,0 ; 63,6 ; 64,8 ; 64,4. "
                 "Évités aussi (reprises de ce dépôt) : l'ampoule de M25b §7 (moyenne 2 ans, remplacement à 3 ans ; 1,554 "
                 "; 0,442 ; e^{−1,5}), le stock gaussien de ✏️ M25b.12 et ∂_σ E[e^X] de ∂ M25b.11 ; la boutique de M26 "
                 "(P_att, r = (−5 ; 7 ; 9), γ = 0,85, V ≈ (23,46 ; 28,13 ; 33,48), ν₂ ≈ (0,245 ; 0,274 ; 0,481)), la salle "
                 "de sport de 🔗 M26.14 (P₀, P₁, 30 € et 21 €), la machine de ✏️ M26.6 ; la loi (0,5 ; 0,3 ; 0,2) et les "
                 "énergies 0, 0,5 et 2 de M17 §7 ; les énergies (0, ln 3, 2 ln 3) à T = 1 de CP6.8 B ; les trois experts "
                 "et η = 0,5 de Hedge (M14 §4) ; les avis de l'ornithologue et du garagiste (M28 §5) ; la forêt (120, 40, "
                 "300, 90, 60) de Horvitz-Thompson (M20 §5). Glossaire : « fonction score | score function | ∂_θ ln p_θ(x) | MB8 », et "
                 "l'entrée « méthode du score » (M25b) renvoie à MB8. Pas de MML (le livre n'a ni fonction score, ni "
                 "échantillonnage d'importance, ni apprentissage par renforcement), donc pas de 📖. Références libres, "
                 "citées par sections et à vérifier en génération (annexes/ressources.md) : R. S. Sutton et A. G. Barto, "
                 "Reinforcement Learning: An Introduction (2ᵉ éd., 2018), §12.1 (le λ-retour), §13.2 (le théorème du "
                 "gradient de politique) et §13.4 (la baseline) ; A. B. Owen, Monte Carlo theory, methods and examples (en "
                 "ligne), les chapitres sur les variables de contrôle et l'échantillonnage d'importance ; D. R. Hunter, « "
                 "MM algorithms for generalized Bradley-Terry models », Annals of Statistics (2004), pour l'algorithme de "
                 "Zermelo. Ni la triade mortelle ni la moyenne interquartile (facultatives au plan) : pas de place ; la "
                 "loi de Little (workbookIA B7) non plus. COMPOSITION : 7 ✏️ et 3 ∂ (le bas de la fourchette : chaque "
                 "section a son ✏️, les démonstrations courtes, Gibbs et le λ-retour, sont dans la fiche) ; ni 📦 (les "
                 "quatre 🔨 et leurs oracles en tiennent lieu) ni 🎨 (le 🔮 et le 🔬 tracent leurs mesures) ; un seul 🔗 et un "
                 "💼. Parcours essentiel : tout sauf ∂ MB8.9 (la baseline optimale et les baselines de groupe : la fiche "
                 "énonce le résultat), le 🔬, le 🛠️ et le 🏆. **Durée** : 13,3 h au lieu des 12 h visées (10 h au plan) : "
                 "huit notions, dont quatre lacunes lourdes (la fonction score et Fisher, les variables de contrôle, "
                 "l'échantillonnage d'importance, le principe de Gibbs) et la dérivation matricielle promise par M26, avec "
                 "des durées d'apprenant qui rédige (les recalages de M25a à M28 : +20 à +40 %) ; déjà allégée (✏️ de "
                 "Fisher fondu dans ∂ MB8.8, Gibbs et le λ-retour démontrés dans la fiche, ni 📦 ni 🎨, un seul 💼).",
        "exercises": [
            ("MB8.Q1", "🧠", 1, 5, "La fonction score : espérance nulle, information de Fisher, support qui dépend du "
             "paramètre, et dériver une espérance par le score ou par le chemin", "§1 §2", "E"),
            ("MB8.Q2", "🧠", 1, 5, "Variables de contrôle et baselines : ce qui garde l'espérance, ce qui réduit la "
             "variance, ce qui biaise", "§3", "E"),
            ("MB8.Q3", "🧠", 1, 5, "Le gradient de la valeur d'une politique et le λ-retour : la loi d'occupation "
             "actualisée, l'avantage d'espérance nulle, le poids de chaque retour à k pas", "§4 §5", "E"),
            ("MB8.Q4", "🧠", 1, 4, "Échantillonnage d'importance et KL estimée : support, taille effective, poids tronqués, "
             "k₁ ou k₃", "§6", "E"),
            ("MB8.Q5", "🧠", 1, 4, "Bradley-Terry et Elo : ce que les forces identifient, quand elles existent, ce que fait "
             "une mise à jour", "§7", "E"),
            ("MB8.Q6", "🧠", 1, 4, "Le principe de Gibbs : la loi optimale, ses limites en β, et ce que mesure β ln Z",
             "§8", "E"),
            ("MB8.R1", "🔁", 1, 6, "La jacobienne de la softmax, diag(p) − ppᵀ, lue comme la covariance d'un vecteur "
             "one-hot, et la loi de Boltzmann (M17)", "§4", "E"),
            ("MB8.R2", "🔁", 1, 7, "Le système de Bellman d'une politique fixée, la loi d'occupation actualisée et le "
             "télescopage des erreurs TD (M26)", "§4 §5", "E"),
            ("MB8.R3", "🔁", 1, 6, "La dérivée par le chemin, son hypothèse de domination, et l'indicatrice où elle échoue "
             "(M25b)", "§2", "E"),
            ("MB8.1", "✏️", 2, 30, "Une attente au téléphone de loi exponentielle de taux θ, et une pénalité au-delà de c "
             "minutes : d/dθ P(X > c) par la formule fermée, par l'estimateur score (son espérance calculée) et par le "
             "chemin X = ξ/θ ; la variance de l'estimateur score à un tirage", "§2", "E"),
            ("MB8.2", "✏️", 2, 30, "Deux graines par godet (une loi binomiale B(2, θ)) et un prix selon le nombre de "
             "pousses : la dérivée de la recette moyenne, puis l'estimateur score sans baseline, avec b = E[f] et avec la "
             "baseline optimale, et leurs variances", "§3", "E"),
            ("MB8.3", "✏️", 2, 35, "Un camion de crêpes entre deux emplacements, une politique softmax dans l'un d'eux : "
             "la chaîne induite, les valeurs, la loi d'occupation actualisée, les valeurs et les avantages des deux "
             "actions, puis le gradient de la valeur par rapport aux deux logits", "§4", "E"),
            ("MB8.4", "✏️", 2, 25, "L'état d'une route (bonne, usée, en travaux) et des valeurs estimées fausses : le "
             "biais des retours à 1 et 2 pas, les poids (1 − λ)λ^{k−1} d'un λ-retour, et son biais quand l'erreur est la "
             "même partout", "§5", "E"),
            ("MB8.5", "✏️", 2, 35, "Un panel en ligne dont les classes d'âge ne suivent pas le recensement : les poids "
             "p/q, la dépense moyenne repondérée, la taille effective de Kish d'un petit échantillon, des poids tronqués "
             "(le biais), puis KL(q ‖ p) exacte et ses estimateurs k₁ et k₃ classe par classe", "§6", "E"),
            ("MB8.6", "✏️", 2, 30, "Un tournoi de babyfoot entre trois clubs : deux clubs seuls (la différence de forces "
             "en forme fermée), puis vérifier les équations du maximum de vraisemblance pour des forces proposées, la "
             "probabilité qu'un club batte un autre, une mise à jour Elo, et un club invaincu", "§7", "E"),
            ("MB8.7", "✏️", 2, 25, "Trois plats à la cantine : la loi de service qui maximise la satisfaction moyenne "
             "moins β fois la KL à la loi actuelle, pour deux valeurs de β, sa valeur β ln Z, comparée à la loi actuelle "
             "et au meilleur plat seul", "§8", "E"),
            ("MB8.8", "∂", 2, 30, "Les deux identités du score, E[s_θ(X)] = 0 et Var(s_θ) = −E[∂²_θ ln p_θ(X)], pour une "
             "famille à densité dont le support ne dépend pas de θ ; leur application aux lois de Poisson et exponentielle "
             "; puis la loi uniforme sur [0, θ], où elles tombent", "§1", "E"),
            ("MB8.9", "∂", 2, 25, "La baseline optimale b* = E[f s²]/E[s²] d'un estimateur score ; sur n tirages, la "
             "moyenne des autres est une baseline sans biais, et la moyenne du groupe multiplie l'estimateur par (n − 1)/n",
             "§3", ""),
            ("MB8.10", "∂", 3, 30, "Le gradient de la valeur d'une politique sous forme matricielle : dériver V = r_π + "
             "γP_πV, faire apparaître la loi d'occupation actualisée et la valeur des actions, puis remplacer Q^π par "
             "l'avantage", "§4", "E"),
            ("MB8.11", "🔗", 1, 15, "Pont : la « loss de substitution » −(1/n)Σ(f(x_i) − b) ln p_θ(x_i), dont la dérivée, "
             "les f(x_i) et b tenus fixes, est moins l'estimateur score : sur le taux d'une loi de Poisson, puis ce que "
             "changent des f standardisés dans le batch", "§2 §3", "E"),
            ("MB8.12", "🗣️", 1, 10, "Expliquer avec un club d'échecs pourquoi une cote Elo ne dit que des écarts de "
             "niveau, et pourquoi battre plus fort que soi rapporte plus de points", "§7", "E"),
            ("MB8.E1", "💼", 1, 10, "« Comment dériver la probabilité d'un événement par rapport au paramètre d'une loi "
             "quand on ne peut pas dériver à travers les tirages, et comment rendre l'estimation moins bruitée ? »",
             "§2 §3", "E"),
            ("MB8.13", "🔨", 1, 20, "L'estimateur score d'une dérivée sur un échantillon, avec une baseline constante ou la "
             "moyenne des autres tirages, et son erreur type", "§2 §3", "E m:score_function_gradient"),
            ("MB8.14", "🔨", 2, 30, "Le gradient exact de la valeur d'une politique softmax tabulaire, par le système de "
             "Bellman", "§4", "E m:policy_gradient_exact"),
            ("MB8.15", "🔨", 2, 25, "Des poids d'importance calculés en log, auto-normalisés ou tronqués, et la taille "
             "effective de l'échantillon", "§6", "E m:importance_weights"),
            ("MB8.16", "🔨", 2, 35, "Les forces d'un modèle de Bradley-Terry par maximum de vraisemblance (l'algorithme de "
             "Zermelo), centrées, et le refus d'un tournoi où elles n'existent pas", "§7", "E m:bradley_terry_fit"),
            ("MB8.17", "🔮", 1, 20, "Prédire l'ordre des écarts-types de l'estimateur score d'une même dérivée, sans "
             "baseline, avec la moyenne des autres tirages et avec la baseline optimale, puis les mesurer",
             "§3", "E p:MB8.13"),
            ("MB8.18", "🔬", 2, 25, "Un événement rare, P(Z > 4) pour Z normale centrée réduite : Monte-Carlo naïf contre "
             "l'échantillonnage d'importance sous N(4, 1), la taille effective, puis des poids tronqués à c : le biais et "
             "la variance selon c", "§6", "p:MB8.15"),
            ("MB8.19", "🐛", 1, 20, "Chasse à l'erreur : le score d'une loi exponentielle écrit pour la moyenne au lieu du "
             "taux, des poids d'importance inversés (q/p), une baseline qui contient le tirage lui-même, des forces de "
             "deux tournois sans joueur commun comparées sur une même échelle", "§1 §3 §6 §7", "E"),
            ("MB8.20", "🛠️", 1, 20, "Un test de propriété pour le gradient exact : sur des MDP tirés au hasard, comparé à "
             "des différences finies centrées, et de somme nulle sur les actions de chaque état", "§4", "p:MB8.14"),
            ("MB8.21", "🏆", 3, 35, "Défi : estimer, avec un budget de tirages, la dérivée d'une probabilité de dépassement "
             "par rapport au paramètre d'une loi, assez précisément neuf fois sur dix (score, baseline, variable de "
             "contrôle)", "§2 §3", "p:MB8.13"),
        ],
    },
]
