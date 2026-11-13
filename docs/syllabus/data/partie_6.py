"""Syllabus, part VI (before workbookIA chapters 25 to 29): detailed in session 60 (M25a, M25b, M26, M27, M28, CP6).

Format: tools/syllabus.py. Exercise tuple: (id, type, stars, minutes, title, covers, flags);
flags: E (essential track), c:wbm|pytest|manuel, f:02|03, p:prerequisites, m:mymath functions written.

Sharing rule (BIBLE §8, §24): every proof (∂) of the workbookIA chapter a math chapter prepares is a frontier
(tools/syllabus.py adds them); ``frontieres`` lists further workbookIA exercises not to solve nor paraphrase. A math
chapter teaches the tool in another setting and may state a result whose proof workbookIA asks. As in parts IV and V,
the math chapters work outside the networks: measurements, sensors, populations, machines, games, weather and maps;
never an encoder, a decoder, a VAE, an agent trained by Q-learning, a generator, a discriminator, a style loss or a
language model. workbookIA 29 has no math chapter (its distribution shift is read with M02c and M03). The notes of
each chapter list the data of workbookIA to avoid; CP6 is also compared with the checkpoint VI and the mini-project VI
of workbookIA.
"""

CHAPTERS = [
    {
        "id": "M25a", "dir": "m25a_gaussienne", "hours": 17.4, "generation_sessions": 2,
        "mml": ["§6.5", "§6.7", "§9.3"],
        "summary": "La loi normale multivariée : sa densité (le déterminant et la distance de Mahalanobis), les "
                   "transformations affines et le changement de variable multivarié (la loi de μ + Lε et l'échantillonnage "
                   "par Cholesky), la géométrie (ellipses de niveau, masse d'une ellipse, loi de la norme), les matrices "
                   "par blocs et le complément de Schur (lois marginales et conditionnelles, matrice de précision), Bayes "
                   "avec des gaussiennes (produit de densités, modèle linéaire gaussien, régression linéaire bayésienne), "
                   "le maximum de vraisemblance de μ et Σ, la divergence KL continue (Jensen, positivité, additivité, KL "
                   "entre deux gaussiennes), et l'interpolation sphérique. workbookIA 25 s'en sert pour le prior et "
                   "l'encodeur probabiliste du VAE, son terme KL et l'interpolation entre deux codes.",
        "objectives": [
            "Écrire et évaluer la densité et la log-densité d'une loi normale multivariée, et y lire le rôle de det Σ et "
            "de la distance de Mahalanobis.",
            "Trouver la loi d'une transformation affine ou d'une somme de vecteurs gaussiens par le changement de variable "
            "multivarié, et tirer un vecteur de loi N(μ, Σ) sous la forme μ + Lε, par Cholesky.",
            "Tracer les ellipses de niveau d'une gaussienne, calculer la masse d'une ellipse en dimension 2, et décrire la "
            "loi de la norme d'un vecteur gaussien en dimension d.",
            "Calculer un complément de Schur, une loi marginale et une loi conditionnelle, et lire une matrice de "
            "précision.",
            "Multiplier deux densités gaussiennes, et calculer le posterior, la prédictive et l'évidence d'une régression "
            "linéaire bayésienne.",
            "Démontrer le maximum de vraisemblance de μ et Σ avec les gradients de ln det et de la trace.",
            "Définir la divergence KL continue, démontrer sa positivité (Jensen) et son additivité, et calculer la KL "
            "entre deux gaussiennes multivariées.",
            "Démontrer les propriétés de l'interpolation sphérique et l'appliquer à un trajet sur une sphère.",
        ],
        "sections": [("§1", "La densité de la loi normale multivariée : de N(0, I) à N(μ, Σ), déterminant et distance de "
                            "Mahalanobis"),
                     ("§2", "Transformations affines, sommes et changement de variable : la loi de μ + Lε et "
                            "l'échantillonnage par Cholesky"),
                     ("§3", "Géométrie : ellipses de niveau, masse d'une ellipse et loi de la norme"),
                     ("§4", "Matrices par blocs et complément de Schur : lois marginales, lois conditionnelles et matrice "
                            "de précision"),
                     ("§5", "Bayes avec des gaussiennes : produit de densités, modèle linéaire gaussien et régression "
                            "linéaire bayésienne"),
                     ("§6", "Estimer μ et Σ : le maximum de vraisemblance et le gradient de ln det"),
                     ("§7", "La divergence KL continue : Jensen, positivité, additivité, et la KL entre deux gaussiennes"),
                     ("§8", "L'interpolation sphérique : rester sur la sphère, à vitesse angulaire constante")],
        "teaches": ["loi normale multivariée N(μ, Σ) : densité, rôle de det Σ et de la distance de Mahalanobis, "
                    "log-densité ; N(0, I) : d coordonnées indépendantes de loi N(0, 1)",
                    "vecteur gaussien : toute combinaison linéaire de ses coordonnées est gaussienne ; deux marginales "
                    "gaussiennes ne font pas un vecteur gaussien (contre-exemple)",
                    "changement de variable multivarié : densité de U(X) par le déterminant de la jacobienne de U⁻¹ "
                    "(MML §6.7.2, admis en général)",
                    "transformations affines : AX + b ~ N(Aμ + b, AΣAᵀ) ; somme de deux vecteurs gaussiens indépendants",
                    "loi de μ + Lε quand ε ~ N(0, I) : N(μ, LLᵀ) ; échantillonnage par Cholesky ; le blanchiment comme "
                    "chemin inverse (rappel de M12c)",
                    "ellipses (ellipsoïdes) de niveau : axes propres de Σ, demi-axes c√λᵢ, aire πc²√(det Σ)",
                    "masse d'une ellipse de Mahalanobis en dimension 2 : 1 − e^{−c²/2} (blanchir, puis les coordonnées "
                    "polaires) ; le carré de la distance de Mahalanobis suit une loi du khi-deux à d degrés (nommée)",
                    "loi de la norme d'un vecteur de loi N(0, I_d) : densité proportionnelle à r^{d−1} e^{−r²/2}, mode "
                    "√(d − 1) ; la densité est maximale au centre, la masse est sur une couronne (suite de M07)",
                    "matrices par blocs : inverse par blocs, complément de Schur, det M = det D · det(A − BD⁻¹C)",
                    "lois marginales d'un vecteur gaussien (les sous-blocs) ; loi conditionnelle : moyenne affine en la "
                    "valeur observée, covariance égale au complément de Schur, qui ne dépend pas de cette valeur",
                    "pour un vecteur gaussien, décorrélé équivaut à indépendant ; matrice de précision Σ⁻¹ : un zéro hors "
                    "de la diagonale veut dire l'indépendance conditionnelle sachant les autres coordonnées",
                    "produit de deux densités gaussiennes : une densité gaussienne à un facteur près (les précisions "
                    "s'additionnent, la moyenne est pondérée par les précisions) ; fusion de mesures",
                    "modèle linéaire gaussien x ~ N(m, V), y = Ax + b + w : loi jointe, loi marginale de y, loi de x "
                    "sachant y",
                    "régression linéaire bayésienne (MML §9.3) : posterior N(m_N, S_N), prédictive, vraisemblance "
                    "marginale (évidence) ; avec m₀ = 0 et S₀ = τ²I, la moyenne a posteriori est la solution ridge de "
                    "λ = σ²/τ²",
                    "maximum de vraisemblance de μ et Σ : μ̂ = x̄ et Σ̂ = (1/n) Σᵢ (xᵢ − x̄)(xᵢ − x̄)ᵀ, par les gradients "
                    "de ln det et de la trace (M18) ; Σ̂ singulière quand n ≤ d",
                    "inégalité de Jensen pour une variable continue (démontrée par une tangente)",
                    "divergence KL continue KL(p ‖ q) = E_p[ln p − ln q] : positivité, nullité si et seulement si p = q, "
                    "valeur infinie quand le support de q ne couvre pas celui de p, asymétrie ; additivité pour des lois "
                    "produits",
                    "entropie différentielle de N(μ, Σ) : ½ ln((2πe)^d det Σ), qui peut être négative",
                    "KL entre deux gaussiennes multivariées N(μ₀, Σ₀) et N(μ₁, Σ₁), par le lemme "
                    "E[(x − m)ᵀA(x − m)] = tr(AΣ) + (μ − m)ᵀA(μ − m) ; même covariance : la moitié du carré d'une "
                    "distance de Mahalanobis",
                    "formules de soustraction sin(γ − ψ) et cos(γ − ψ), déduites de la forme exponentielle de M22",
                    "interpolation sphérique (slerp) : formule, extrémités, norme conservée entre deux vecteurs de même "
                    "norme, angle parcouru proportionnel à t, limite linéaire quand l'angle tend vers 0 ; arc et corde"],
        "requires": [("cosinus, sinus, radians", "R9"),
                     ("intégration par parties, intégrales impropres", "M02a"),
                     ("loi normale, changement de variable en dimension 1, théorème de transfert, intégrale double et "
                      "coordonnées polaires", "M02b"),
                     ("matrice de covariance empirique, estimateur biaisé en 1/n", "M02c"),
                     ("convexité : une fonction convexe est au-dessus de ses tangentes", "M05a"),
                     ("formule de Bayes : a priori, vraisemblance, évidence, a posteriori", "M04"),
                     ("divergence KL discrète, inégalité de Jensen discrète, entropie", "M06"),
                     ("produit scalaire, angle, norme d'un vecteur gaussien en grande dimension", "M07"),
                     ("inverse d'une matrice, résolution d'un système", "M09a"),
                     ("ridge vue comme MAP, régression vue comme maximum de vraisemblance", "M09b"),
                     ("base orthonormée d'un plan, Gram-Schmidt", "M12b"),
                     ("déterminant, trace, théorème spectral, matrices définies positives, Cholesky, covariance AΣAᵀ, "
                      "blanchiment, distance de Mahalanobis", "M12c"),
                     ("maximum de vraisemblance, log-vraisemblance, indépendance conditionnelle (Naïve Bayes)", "M13a"),
                     ("jacobienne d'une application de ℝⁿ dans ℝⁿ", "M17"),
                     ("gradient par rapport à une matrice : ∇ ln det X et ∇ tr(AX)", "M18"),
                     ("forme exponentielle des complexes, e^{ia} e^{ib} = e^{i(a + b)}", "M22")],
        "frontieres": ["25.6", "25.20", "25.28", "25.29", "25.33", "25.Q12", "25.R3", "25.E3", "B5.6"],
        "mymath": {"module": "gaussian.py",
                   "functions": ["mvn_logpdf", "sample_mvn", "schur_complement", "condition_gaussian",
                                 "linreg_posterior"]},
        "reading_minutes": 185,
        "flashcards": 24,
        "notes": "Frontières : le ∂ 25.5 (les dérivées de z = μ + σε par rapport à μ et à s = ln σ², ε fixé, et E[z²] "
                 "dérivée avant ou après l'espérance), le ∂ 25.7 (KL(N(μ, σ²) ‖ N(0, 1)) par E[(z − μ)²] et E[z²], puis "
                 "en s = ln σ², ses dérivées et ses valeurs), le ∂ 25.8 (autoencodeur linéaire et ACP, déjà frontière de "
                 "M12d), le ✏️ 25.6 (E‖z‖² = d, la norme typique √d, P(‖z‖ ≤ r) = 1 − e^{−r²/2} en r = 1 et 3, le rayon "
                 "médian, le milieu de deux tirages indépendants), les 🔨 25.20 (`interpolate_latents`), 25.28 "
                 "(`reparameterize` et sa passe arrière) et 25.29 (`gaussian_kl`, `gaussian_kl_grad` et leur variante "
                 "contre N(0, τ²)), le 🎨 25.33 (le nuage des μ d'un VAE à deux latents contre le prior), le quiz 25.Q12, "
                 "le rappel 25.R3 (la KL discrète dans les deux sens, en bits), le 💼 25.E3, et, de workbookIA B5 (préparé "
                 "par MB5), le ∂ B5.6 (deux pas de bruit gaussien n'en font qu'un : aucun exercice ne compose "
                 "x ↦ √a x + √(1 − a) ε). M25a travaille hors réseau : la température et l'humidité d'une serre, les "
                 "composantes du vent, des capteurs voisins, des thermomètres, des mesures d'une même distance, des "
                 "durées de vie, des trajets sur la Terre ; jamais un encodeur, un code latent, un prior de VAE, une "
                 "image ni un décodeur. **La KL** : M25a définit la KL continue, démontre Jensen pour une variable "
                 "continue (par une tangente), la positivité et l'additivité sur des lois produits (∂ M25a.13), "
                 "l'entropie différentielle de N(μ, Σ) et la KL entre deux gaussiennes multivariées quelconques par le "
                 "lemme de la trace, avec le cas de même covariance (∂ M25a.14) : un énoncé plus général que ∂ 25.7 "
                 "(BIBLE §8). Garde-fous : jamais le cas particulier contre N(0, I), N(0, 1) ou N(0, τ²), ni une "
                 "covariance diagonale comparée à l'identité, ni la formule ½(μ² + σ² − 1 − ln σ²) écrite, ni "
                 "s = ln σ² ou une log-variance, ni une dérivée de la KL, ni « à μ fixé, quel σ² la rend minimale », ni "
                 "une KL gaussienne convertie en bits ; ✏️ M25a.8 prend des covariances pleines en dimension 2 et deux "
                 "lois non centrées ; l'additivité s'applique à des durées de vie exponentielles indépendantes "
                 "(✏️ M25a.7), jamais à des latents ; aucun quiz « nulle exactement pour μ = 0 et σ = 1 », et M25a.Q7 ne "
                 "reprend pas en continu les trois vrai ou faux de 25.R3 b-d (« symétrique ? », « KL(P ‖ P) = 0 ? », "
                 "« jamais négative ? ») : il passe par des situations (supports, lois exponentielles) ; l'invariance "
                 "de la KL par un changement de variable inversible n'est pas enseignée (elle ramènerait au cas contre "
                 "N(0, I)). Le sens de la KL dans une approximation (KL directe ou inverse, moyenne contre mode) est en "
                 "M25b ; M25a calcule seulement les deux sens pour constater l'asymétrie, sans les additionner : la "
                 "mesure d'une dérive (PSI, KL symétrisée) est en M27. **La reparamétrisation** : "
                 "M25a ne donne que la loi de μ + Lε (∂ M25a.10, ✏️ M25a.2), avec L le facteur de Cholesky d'une Σ "
                 "pleine, sans log-variance, sans produit élément par élément σ ⊙ ε et sans aucune dérivée ; la dérivée "
                 "d'une espérance par rapport à un paramètre de la loi est en M25b, dans un autre cadre. `sample_mvn` "
                 "tire une seule loi N(μ, Σ), ne rend pas ε et n'a pas de passe arrière (≠ `reparameterize`) ; les "
                 "fonctions du 🐛 M25a.28 prennent une Σ pleine, jamais `(mu, log_var)` ni `(x, mean, var)` (les "
                 "contrats de `reparameterize` et de `naive_bayes.log_gaussian_pdf`). **La "
                 "géométrie** : ∂ M25a.11 démontre la masse d'une ellipse de Mahalanobis en dimension 2 "
                 "(1 − e^{−c²/2}, en blanchissant puis par les coordonnées polaires de M02b ; le disque en est un cas "
                 "particulier, que workbookIA 25 affirme sans le démontrer) et la densité de la norme en dimension d "
                 "(constante admise, sauf en dimension 2 et 3), de mode √(d − 1) ; ✏️ M25a.3 l'applique au vent, aux "
                 "niveaux 90 % et 95 % (c² = 2 ln 10 et 2 ln 20), avec une Σ non diagonale ; le 🔮 M25a.25 suit la masse "
                 "d'un ellipsoïde de même niveau quand la dimension passe de 2 à 10. **Les blocs** : l'inverse par "
                 "blocs, det M = det D · det(A − BD⁻¹C) et la loi conditionnelle par un résidu indépendant de la mesure "
                 "sont démontrés dans la fiche (§4, dans un bloc `<details>`), sans exercice ∂ ; ✏️ M25a.4, le quiz "
                 "M25a.Q4 et le 🔨 M25a.22 s'en servent. **Le slerp** est démontré "
                 "(∂ M25a.15 : base orthonormée du plan par Gram-Schmidt, formule de sin(γ − ψ) tirée de "
                 "e^{ia} e^{ib} = e^{i(a + b)}, M22 ; MB3 la reprendra) et appliqué à une route orthodromique (✏️ M25a.9 : "
                 "deux villes, vecteurs unitaires de ℝ³, angle au centre, point au tiers du trajet, profondeur du milieu "
                 "de la corde R(1 − cos(Ω/2)), avec un angle Ω différent de 90°) ; la limite quand Ω tend vers 0 est un "
                 "calcul de limite (sin(tΩ)/sin Ω → t), pas une règle de code ; aucune fonction de slerp, ni dans "
                 "`mymath` ni dans le notebook (c'est 🔨 25.20). **Promesses publiées tenues** : M18 (« le gradient de "
                 "ln det reviendra avec la densité de la gaussienne multivariée » : ∂ M25a.12), M12c (det Σ dans la "
                 "densité ; « M25a échantillonnera une loi normale multivariée » par Cholesky), M09b (« M25a la "
                 "régression bayésienne complète », la moyenne a posteriori comme solution ridge), M14 (le couple "
                 "gaussien de M14.13). **Partage avec M25b** (voir le rapport de session) : M25a enseigne la densité "
                 "(`mvn_logpdf`), les transformations affines et le changement de variable multivarié, la loi de "
                 "μ + Lε, la géométrie, le complément de Schur et le conditionnement (`schur_complement`, "
                 "`condition_gaussian`), le produit de densités, le modèle linéaire gaussien, la régression bayésienne, "
                 "le maximum de vraisemblance (non pondéré) de μ et Σ, Jensen continu, la KL continue et la KL entre "
                 "gaussiennes, l'entropie différentielle, le slerp ; M25b les réutilise sans les redémontrer (l'ACP "
                 "probabiliste applique le modèle linéaire gaussien et le conditionnement ; le pas M de l'EM pondère le "
                 "maximum de vraisemblance ; l'ELBO se sert de la KL continue et de l'entropie) et garde les mélanges "
                 "(dont les moments d'un mélange, le Théorème 6.12 de MML et la loi de la variance totale), l'EM, "
                 "l'ELBO, l'ACP probabiliste, la dérivée d'une espérance, le sens de la KL, les angles principaux et β. "
                 "**MML** : §6.5 en entier (le Théorème 6.12, au §6.5.3, et la loi de la variance totale se lisent en "
                 "M25b, avec "
                 "les mélanges ; (6.90) et (6.91) se survolent), la fin de §6.7.2 (Théorème 6.16 et Exemple 6.17, le "
                 "changement de variable multivarié, que M02b.16 n'a pas lu), et §9.3 (§9.3.1 à §9.3.5) : 📖 M25a.17 et "
                 "M25a.18 ; exercices du livre conseillés : 6.10 (produit de deux densités gaussiennes), 6.12 (un modèle "
                 "linéaire gaussien), 6.5 (un pas du filtre de Kalman, pour aller plus loin). `correspondances.md` : "
                 "§6.7 → M02b, M25a. **Conventions** : vecteurs colonnes dans la fiche ; plusieurs vecteurs rangés en "
                 "lignes, de forme (n, d), dans `mymath` et le notebook, comme NumPy (le 🔗 M25a.16 passe d'une "
                 "convention à l'autre : X = 1μᵀ + E Lᵀ) ; N(μ, Σ) avec Σ une covariance (jamais un écart-type) ; "
                 "logarithmes népériens, KL et entropies en nats. `gaussian` : NumPy permis, mais de `np.linalg` "
                 "seulement `cholesky` et `solve`, ni `multivariate_normal` de NumPy (le test AST refuse ce nom dans "
                 "tout le module : `default_rng(seed).multivariate_normal(…, method=\"cholesky\")` rend les tirages de "
                 "`sample_mvn` bit pour bit), et aucune fonction de SciPy (`scipy.stats.multivariate_normal` "
                 "donnerait `mvn_logpdf` et `sample_mvn`) ; les imports relatifs de ses propres modules sont permis "
                 "(`eigen.cholesky` de M12c : les tirages sont comparés à 1e-12 près, pas bit pour bit) ; aucune fonction de KL, de slerp, de reparamétrisation (avec "
                 "des log-variances, ou qui rend ε), de densité diagonale, ni de distance de Fréchet ou de Wasserstein "
                 "(M27, 🔨 27.22). Écarts au plan : `mvn_pdf` devient `mvn_logpdf` (la densité est son exponentielle, "
                 "et M25b la prend en log pour l'EM) ; `marginal_gaussian` est abandonnée (une sélection de sous-blocs, "
                 "faite à la main en ✏️ M25a.4 et dans le 🎨 M25a.27) ; `linreg_posterior` est ajoutée (MML §9.3 ; "
                 "distincte de `bayes_line_posterior` de workbookIA 9, une grille de droites). Les exemples du stub ne "
                 "reviennent dans aucun exercice : la covariance [[2, 3], [3, 9]] de moyenne (1, −1), la matrice "
                 "[[5, 2, 2], [2, 4, 0], [2, 0, 4]] de moyenne (1, 0, 2), Φ = [[1, 0], [1, 1], [1, 2]] avec "
                 "y = (1, 2, 2) ; ✏️ M25a.4 n'en reprend pas la structure (deux voisins indépendants entre eux, un bloc "
                 "Σ_bb diagonal). Le 🏆 M25a.30 reconstruit des températures manquantes le long d'une route par la loi "
                 "conditionnelle d'une gaussienne de covariance exponentielle de la distance (pas une image, pas de "
                 "« inpainting »). **Évités** (règle de partage, et reprises de ce dépôt) : la KL contre N(0, 1), "
                 "N(0, I) ou N(0, τ²) et la formule ½(μ² + σ² − 1 − ln σ²) ; s = ln σ² et les dérivées μ et "
                 "½(e^s − 1) ; les couples (μ, σ²) = (2, 1), (0, e), (0 ; 0,01), (1, 4), (0,5 ; 2,5), les moyennes "
                 "(1, 0, −1), s = ln 5, les variances 0,5 et 2 de la variante de 25.7 ; z = μ + σε avec (1,5 ; 0,5 ; −2), "
                 "(0,2 ; 4 ; 0,5) et (0,2 ; 1 ; −1) ; E‖z‖² en d = 20, 64, 100, 512 et 784, les normes 4,47, 3,16, 8, "
                 "5,7, 10, 7,07, 22,63 ; le rapport 1/√2 ≈ 0,71 du milieu de deux tirages ; P(‖z‖ ≤ r) en dimension 2 "
                 "pour r = 1, 2, 3 (0,393, 0,865, 0,989 ; 39 %, 86 %, 99 %) et le rayon médian 1,18 (r² = 2 ln 2) ; "
                 "34 %, 69 %, 90 % ; les 40 000 tirages de la figure de workbookIA 25 ; les slerps (1, 0) → (0, 1), "
                 "(2, 0, 0) → (0, 2, 0), (3, 0) → (0, 4) (point (2,12 ; 2,83), norme 3,54), z → −z, les normes 23,2, "
                 "14,5 et 11,2, le seuil de repli 1e-6 et l'angle de repli 0,05 rad, « sept points » entre deux codes, "
                 "le milieu (5, 3) de (2, 6) et (8, 0) (25.Q8 e), la dimension 64 et les normes 8 "
                 "et 5,7 de 27.26 ; les tableaux mu, log_var et dz de 25.28 et 25.29, N(2, 9) et 200 000 tirages, "
                 "(1,993 ; 8,978) ; les lois P = (0,5 ; 0,5) et Q = (0,25 ; 0,75) de 25.R3 ; « 68 % entre −1 et 1 » "
                 "comme exemple ; la KL de deux gaussiennes de même variance ‖Δμ‖²/(2σ²) de workbookIA B5 et le "
                 "bruitage √ᾱ x₀ + √(1 − ᾱ) ε ; la distance de Fréchet entre deux gaussiennes (27.22, M27) ; la grille "
                 "3 × 3 de droites et les points (1, 1) et (−1, 0) de 9.7, la figure 9.20 de 9.27 ; de MML, l'Exemple 6.6 "
                 "(N([0, 2], [[0,3 ; −1], [−1 ; 5]]), x₂ = −1, N(0,6 ; 0,1), marginale N(0 ; 0,3)), l'Exemple 6.17 (refait avec d'autres nombres dans le 📖 seulement), les Exemples 9.7 "
                 "et 9.8 (polynômes de degré 3, 5 et 7, prior N(0, ¼ I)), les exercices 6.2 et 6.4 du livre ; de ce "
                 "dépôt, la matrice [[3, 1], [1, 2]] de 🔁 M09b.R1, les covariances [[4, 6], [6, 13]], [[9, 6], [6, 8]] "
                 "et [[4, 2], [2, 5]] de M12c, (0,6 ; 0,5 ; "
                 "1,4) de M14.13, et la concentration en dimension 1 000 de M07 (écart-type 0,71, 29,8 à 33,5) ; "
                 "MNIST, Fashion-MNIST, le VAE, le tigre, les manchots (workbookIA 2). **Durée** : 17,2 h au lieu des "
                 "14 h prévues (18,3 h avant les coupes du coordinateur : la démonstration par blocs, un 💼, des minutes "
                 "de lecture) : la KL continue, Jensen continu, l'additivité et la KL entre gaussiennes (que workbookIA "
                 "25 suppose et que la planification ne comptait pas), la masse d'une ellipse et la loi de la norme, le "
                 "slerp démontré, le maximum de vraisemblance (promesse de M18), et trois blocs de MML (§6.5, la fin de "
                 "§6.7.2, §9.3). Deux sessions de génération : §1 à §4, puis §5 à §8.",
        "exercises": [
            ("M25a.Q1", "🧠", 1, 4, "Lire une densité gaussienne multivariée : det Σ, distance de Mahalanobis et point le "
             "plus probable", "§1", "E"),
            ("M25a.Q2", "🧠", 1, 4, "Ce qui reste gaussien : images affines, sommes, produits et normes ; deux marginales "
             "gaussiennes ne suffisent pas", "§2", "E"),
            ("M25a.Q3", "🧠", 1, 4, "Ellipses de niveau et masse : quel axe, quel demi-axe, quelle proportion, en dimension "
             "2 et au-delà", "§3", "E"),
            ("M25a.Q4", "🧠", 1, 6, "Complément de Schur, loi marginale ou loi conditionnelle : quel bloc, quelle moyenne, "
             "quelle variance ?", "§4", "E"),
            ("M25a.Q5", "🧠", 1, 4, "Fusionner des mesures et mettre à jour un a priori gaussien : précisions, moyennes "
             "pondérées et prédictive", "§5", "E"),
            ("M25a.Q6", "🧠", 1, 4, "Le maximum de vraisemblance de μ et Σ : diviser par n, et une covariance singulière "
             "quand n ≤ d", "§6", ""),
            ("M25a.Q7", "🧠", 1, 4, "La divergence KL continue en situations : deux supports qui ne se couvrent pas, deux lois "
             "exponentielles, une loi produit, et les deux sens", "§7",
             "E"),
            ("M25a.Q8", "🧠", 1, 4, "Ligne droite ou arc de grand cercle : extrémités, norme et angle parcouru", "§8", "E"),
            ("M25a.R1", "🔁", 1, 6, "Le changement de variable en dimension 1 et les coordonnées polaires (M02b)", "§2 §3",
             "E"),
            ("M25a.R2", "🔁", 1, 6, "Le théorème spectral, Cholesky et la covariance AΣAᵀ (M12c)", "§2 §3", "E"),
            ("M25a.R3", "🔁", 1, 6, "Les gradients de ln det X et de tr(AX) par rapport à une matrice (M18)", "§6", ""),
            ("M25a.1", "✏️", 1, 25, "La densité d'un couple gaussien (température et humidité d'une serre) en deux points : "
             "distance de Mahalanobis contre distance euclidienne", "§1", "E"),
            ("M25a.2", "✏️", 2, 30, "Trois mesures corrélées : la loi d'une somme pondérée et d'une différence, puis un "
             "tirage μ + Lε par Cholesky et sa covariance", "§2", "E"),
            ("M25a.3", "✏️", 2, 30, "Les ellipses à 90 % et à 95 % des composantes du vent sur un site : axes, demi-axes, "
             "aire, et la part des relevés dans l'ellipse de niveau c", "§3", "E"),
            ("M25a.4", "✏️", 2, 35, "Un capteur en panne estimé par ses deux voisins : complément de Schur, loi "
             "conditionnelle en dimension 3, et l'écart-type gagné", "§4", "E"),
            ("M25a.5", "✏️", 1, 20, "Fusionner trois mesures d'une même distance : le produit de densités gaussiennes, des "
             "précisions qui s'additionnent, un ordre sans importance", "§5", "E"),
            ("M25a.6", "✏️", 2, 40, "Étalonner un thermomètre par la régression linéaire bayésienne : loi jointe, "
             "évidence, posterior de (a, b), et prédictive près et loin des points d'étalonnage", "§5", ""),
            ("M25a.7", "✏️", 2, 25, "La divergence KL continue entre deux lois exponentielles et entre deux lois "
             "uniformes : les deux sens, une KL infinie, et deux durées de vie indépendantes", "§7", "E"),
            ("M25a.8", "✏️", 2, 30, "Deux réglages d'une machine de découpe, deux gaussiennes en dimension 2 des erreurs "
             "de position : la KL dans les deux sens, et le cas de même covariance", "§7", "E"),
            ("M25a.9", "✏️", 2, 30, "La route orthodromique entre deux villes : angle au centre, point au tiers du trajet "
             "par le slerp, et profondeur du milieu de la corde", "§8", "E"),
            ("M25a.10", "∂", 2, 30, "Le changement de variable multivarié : la densité de μ + Lε est celle de N(μ, LLᵀ), "
             "et AX + b reste gaussien pour A inversible", "§1 §2", "E"),
            ("M25a.11", "∂", 2, 30, "La masse d'une ellipse de Mahalanobis en dimension 2 vaut 1 − e^{−c²/2} ; la densité "
             "de la norme en dimension d, et son mode √(d − 1)", "§3", "E"),
            ("M25a.12", "∂", 2, 40, "Le maximum de vraisemblance d'une gaussienne multivariée : μ̂ = x̄ et Σ̂ = S/n, par "
             "les gradients de ln det et de la trace", "§6", ""),
            ("M25a.13", "∂", 2, 35, "L'inégalité de Jensen pour une variable continue, la positivité de la KL continue, et "
             "l'additivité de la KL sur des lois produits", "§7", "E"),
            ("M25a.14", "∂", 3, 45, "La KL entre N(μ₀, Σ₀) et N(μ₁, Σ₁) en dimension d, par le lemme de la trace ; "
             "l'entropie différentielle de N(μ, Σ)", "§7", "E"),
            ("M25a.15", "∂", 2, 25, "Le slerp entre deux vecteurs de même norme reste sur la sphère et avance d'un angle "
             "constant ; sa limite quand l'angle tend vers 0", "§8", "E"),
            ("M25a.16", "🔗", 1, 25, "Pont : des vecteurs rangés en lignes (n, d) comme dans les bibliothèques : tirer n "
             "points d'un coup par E Lᵀ + μ, la log-densité de chaque ligne, et la moyenne en nats par coordonnée", "§1 §2", "E"),
            ("M25a.17", "📖", 2, 45, "MML §6.5 et la fin de §6.7.2 : densité, marginales et conditionnelles, produit, "
             "sommes et transformations, échantillonnage et changement de variable multivarié, en anglais",
             "§1 §2 §4 §5", ""),
            ("M25a.18", "📖", 2, 45, "MML §9.3 : régression linéaire bayésienne, prédictions a priori et a posteriori, "
             "vraisemblance marginale, en anglais", "§5", ""),
            ("M25a.19", "🗣️", 1, 10, "Expliquer avec deux thermomètres voisins pourquoi lire l'un resserre l'estimation de "
             "l'autre, et pourquoi la valeur lue ne change pas cette incertitude", "§4", "E"),
            ("M25a.E1", "💼", 1, 10, "« Comment tirer un vecteur gaussien de covariance donnée à partir de tirages "
             "indépendants, et pourquoi Cholesky ? »", "§2", ""),
            ("M25a.20", "🔨", 2, 30, "La log-densité d'une loi normale multivariée, par Cholesky", "§1",
             "E m:mvn_logpdf"),
            ("M25a.21", "🔨", 1, 20, "Tirer des vecteurs de loi N(μ, Σ) par Cholesky", "§2", "E m:sample_mvn"),
            ("M25a.22", "🔨", 2, 35, "Le complément de Schur d'un bloc, et la loi conditionnelle d'un vecteur gaussien",
             "§4", "E m:schur_complement,condition_gaussian"),
            ("M25a.23", "🔨", 2, 25, "Le posterior d'une régression linéaire bayésienne", "§5", "m:linreg_posterior"),
            ("M25a.24", "📦", 1, 25, "`scipy.stats.multivariate_normal`, `np.cov` et `scipy.integrate` : tes "
             "log-densités, le maximum de vraisemblance, et la KL de M25a.8 par une intégrale double", "§1 §6 §7",
             "E p:M25a.20,M25a.8"),
            ("M25a.25", "🔮", 1, 15, "Prédire la part des tirages dans l'ellipsoïde de Mahalanobis de même niveau quand la "
             "dimension passe de 2 à 10, puis mesurer", "§3", "E p:M25a.21"),
            ("M25a.26", "🔬", 2, 25, "Conditionner par simulation : garder les tirages dont une mesure tombe près d'une "
             "valeur, et comparer à la loi conditionnelle exacte", "§4", "p:M25a.21,M25a.22"),
            ("M25a.27", "🎨", 1, 20, "Les ellipses de niveau d'une gaussienne en dimension 2, une tranche (la loi "
             "conditionnelle) et une projection (la loi marginale), selon la corrélation", "§3 §4", "E p:M25a.22"),
            ("M25a.28", "🐛", 1, 20, "Chasse à l'erreur : un tirage par E L au lieu de E Lᵀ, ln det Σ sans le facteur 2, et "
             "une covariance conditionnelle qui dépend de la valeur observée", "§1 §2 §4", "E"),
            ("M25a.29", "🛠️", 1, 20, "Un test de propriété : la moyenne et la covariance empiriques de tes tirages, à une "
             "tolérance fixée par l'erreur type", "§2", "p:M25a.21"),
            ("M25a.30", "🏆", 3, 30, "Défi : reconstruire les températures manquantes le long d'une route par la loi "
             "conditionnelle d'une gaussienne, sous une erreur quadratique moyenne fixée", "§4", "p:M25a.22"),
        ],
    },
    {
        "id": "M25b", "dir": "m25b_variables_latentes", "hours": 16.8, "generation_sessions": 2,
        "mml": ["§8.4", "§8.5", "§10.7", "ch. 11"],
        "summary": "Les variables latentes : un modèle génératif écrit comme un graphe orienté (loi jointe, tirage "
                   "ancestral), la vraisemblance marginale et le posterior d'un latent, les moments d'un mélange ; les "
                   "mélanges de gaussiennes (responsabilités en log, singularités) et l'algorithme EM ; la borne "
                   "inférieure de l'évidence (ELBO), démontrée en général, dont l'EM est une montée par coordonnées ; "
                   "l'ACP probabiliste (posterior exact, rotation, angles principaux, directions éteintes) ; "
                   "l'inférence approchée (sens de la KL, inférence amortie, dériver une espérance par rapport à un "
                   "paramètre de la loi) ; et β, le multiplicateur d'une contrainte d'information, avec le posterior "
                   "agrégé et l'effondrement du code. workbookIA 25 s'en sert pour l'espace latent, l'ELBO et la loss du "
                   "VAE, la reparamétrisation, le β-VAE et le lien entre autoencodeur linéaire et ACP.",
        "objectives": [
            "Écrire la loi jointe d'un modèle à variables latentes selon son graphe orienté, en tirer un échantillon "
            "ancestral, et calculer la vraisemblance marginale et le posterior d'un latent.",
            "Définir l'espérance et la variance conditionnelles sachant une variable discrète, et calculer la "
            "moyenne et la covariance d'un mélange par les lois de l'espérance et de la variance totales.",
            "Calculer les responsabilités et la log-vraisemblance d'un mélange de gaussiennes en log, et expliquer "
            "pourquoi cette vraisemblance n'est pas bornée.",
            "Dériver les pas E et M de l'algorithme EM pour un mélange de gaussiennes, et démontrer qu'il ne fait "
            "jamais baisser la vraisemblance.",
            "Démontrer ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour toute loi q, en déduire la borne et le cas "
            "d'égalité, et lire l'EM comme une montée par coordonnées de l'ELBO.",
            "Écrire la loi marginale et le posterior de l'ACP probabiliste, en estimer les paramètres à partir des "
            "valeurs propres, et comparer deux sous-espaces par leurs angles principaux.",
            "Dériver une espérance par rapport à un paramètre de la loi par le chemin X = μ + σε, et choisir le sens "
            "de la KL dans une approximation.",
            "Interpréter β comme un multiplicateur de Lagrange, décomposer la KL moyenne au prior en information "
            "mutuelle et écart du posterior agrégé, et reconnaître un code effondré.",
        ],
        "sections": [("§1", "Variables latentes et graphes orientés : processus génératif, loi jointe, tirage ancestral "
                            "et indépendance conditionnelle"),
                     ("§2", "Marginaliser et inverser : vraisemblance marginale, posterior d'un latent, et les moments "
                            "d'un mélange (espérance et variance conditionnelles, puis totales)"),
                     ("§3", "Mélanges de gaussiennes : responsabilités en log, log-vraisemblance, singularités et "
                            "composantes à numérotation arbitraire"),
                     ("§4", "L'algorithme EM : le pas E, le pas M pondéré, la monotonie, et k-means comme limite"),
                     ("§5", "La borne inférieure de l'évidence (ELBO) : ln p(x) = ELBO + KL, l'EM comme montée par "
                            "coordonnées, et le gradient de ln p(x)"),
                     ("§6", "L'ACP probabiliste : posterior exact, maximum de vraisemblance, rotation de W, angles "
                            "principaux et directions éteintes"),
                     ("§7", "Inférence approchée : le sens de la KL, l'inférence amortie, et dériver une espérance "
                            "par rapport à un paramètre de la loi"),
                     ("§8", "Pondérer la KL : β comme multiplicateur de Lagrange, information mutuelle, posterior agrégé "
                            "et effondrement du code")],
        "teaches": ["variable latente, espace latent, processus génératif ; loi jointe p(x, z) = p(z) p(x | z)",
                    "modèle graphique orienté : factorisation selon les parents, tirage ancestral ; indépendance "
                    "conditionnelle, chaîne, fourche et collision (d-séparation en survol, MML §8.5) ; une cause "
                    "observée en disculpe une autre",
                    "vraisemblance marginale p(x) = Σ_z p(z) p(x | z) (ou une intégrale) ; posterior p(z | x) par "
                    "Bayes ; l'évidence comme constante de normalisation",
                    "mélange de lois : densité, tirage ancestral ; espérance et variance conditionnelles sachant une "
                    "variable discrète, définies ici (E[X | Z = k], la variable aléatoire E[X | Z] ; pour un mélange, "
                    "E[X | Z = k] = μ_k et V[X | Z = k] = Σ_k) ; lois de l'espérance totale et de la variance totale "
                    "(MML Théorème 6.12, §6.5.3) ; moyenne et covariance d'un mélange Σ π_k (Σ_k + μ_k μ_kᵀ) − μμᵀ ; "
                    "part de la variance entre les groupes",
                    "mélange de gaussiennes : log-vraisemblance (le logarithme d'une somme), responsabilités calculées "
                    "en log par log-sum-exp (M04, M05a)",
                    "singularités : vraisemblance non bornée quand une composante s'effondre sur un point, "
                    "régularisation Σ_k + reg·I (le pas M ne maximise plus : l'EM régularisé n'est plus monotone à coup "
                    "sûr) ; numérotation arbitraire des composantes : K! maxima équivalents",
                    "algorithme EM pour un mélange de gaussiennes : pas E (responsabilités), pas M (π_k = N_k/n par un "
                    "multiplicateur de Lagrange, moyennes et covariances pondérées : le maximum de vraisemblance de "
                    "M25a, pondéré) ; monotonie, maxima locaux, initialisations ; une proportion de mélange et des "
                    "composantes inconnues (suite de M13a)",
                    "k-means comme limite de l'EM : covariances communes εI, ε → 0, responsabilités dures",
                    "borne inférieure de l'évidence (ELBO), démontrée en général pour un latent discret ou continu : "
                    "ln p(x) = E_q[ln p(x, z) − ln q(z)] + KL(q ‖ p(z | x)) ; ELBO ≤ ln p(x), égalité si et seulement "
                    "si q est le posterior ; la même borne par Jensen ; la forme E_q[ln p(x | z)] − KL(q ‖ p(z)) "
                    "(une reconstruction moins une KL au prior) ; l'entropie de q",
                    "l'EM comme montée par coordonnées de l'ELBO : le pas E la maximise en q (q = posterior), le pas M "
                    "en θ (Q(θ | θ_t) de MML §11.4.5) ; d'où la monotonie",
                    "gradient de la log-vraisemblance marginale : ∇_θ ln p(x) = E_{p(z | x)}[∇_θ ln p(x, z)] ; il "
                    "égale le gradient de l'ELBO quand q est le posterior",
                    "ACP probabiliste (MML §10.7) : z ~ N(0, I_k), x = Wz + μ + ε, ε ~ N(0, σ²I) ; loi marginale "
                    "N(μ, WWᵀ + σ²I) ; posterior N(M⁻¹Wᵀ(x − μ), σ²M⁻¹) avec M = WᵀW + σ²I, par le modèle linéaire "
                    "gaussien de M25a ; l'autre forme, Wᵀ(WWᵀ + σ²I)⁻¹(x − μ) et I − Wᵀ(WWᵀ + σ²I)⁻¹W (MML §10.7.3), "
                    "égale par Wᵀ(WWᵀ + σ²I)⁻¹ = (WᵀW + σ²I)⁻¹Wᵀ ; sa moyenne est une règle affine de x, sa "
                    "covariance n'en dépend pas",
                    "maximum de vraisemblance de l'ACP probabiliste (Tipping et Bishop, énoncé) : σ² = moyenne des "
                    "valeurs propres écartées, W = U_k (Λ_k − σ²I)^{1/2} R ; la limite σ² → 0 retrouve l'ACP de M12d ; "
                    "quand σ² est fixé (connu), une direction de valeur propre λ ≤ σ² est éteinte (colonne de W nulle)",
                    "non-identifiabilité par rotation : W et WR (R orthogonale) donnent la même loi ; seul le "
                    "sous-espace engendré par W est déterminé",
                    "angles principaux entre deux sous-espaces : cos θ_i = valeurs singulières de Q_Aᵀ Q_B pour des "
                    "bases orthonormées Q_A et Q_B (M12b, M12d), min(k_A, k_B) angles ; ils ne dépendent pas des "
                    "bases ; deux sous-espaces de même dimension sont égaux si et seulement si tous leurs angles sont "
                    "nuls (en général, tous nuls si et seulement si le plus petit est contenu dans l'autre)",
                    "inférence approchée : famille de lois q, KL(q ‖ p) (évite de mettre de la masse là où p est "
                    "faible, choisit un mode) contre KL(p ‖ q) (couvre toute la masse ; pour une famille gaussienne, "
                    "apparie les moments) ; maximiser l'ELBO, c'est minimiser KL(q ‖ p(z | x))",
                    "inférence amortie : une règle x ↦ q(z | x) commune à toutes les observations ; écart "
                    "d'amortissement : ELBO amortie ≤ meilleure ELBO par observation ≤ ln p(x)",
                    "dériver une espérance par rapport à un paramètre de la loi : le chemin X = μ + σε (ou μ + Lε, "
                    "M25a), que workbookIA 25 appelle l'astuce de reparamétrisation (*reparameterization trick*) ; "
                    "l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré, la "
                    "convergence dominée admise), d/dθ E[f(g_θ(ε))] = E[f′(g_θ(ε)) ∂_θ g_θ(ε)] ; estimateur de "
                    "Monte-Carlo sans biais à un tirage (M19) et sa variance ; une fonction dérivable presque partout, "
                    "et une indicatrice 1{X > c} pour laquelle l'échange échoue (dérivée nulle presque partout, alors "
                    "que d/dμ P(X > c) = φ((c − μ)/σ)/σ) ; la méthode du score seulement nommée (MB8)",
                    "pondérer une KL : maximiser une vraisemblance de reconstruction sous un budget d'information, le "
                    "lagrangien (M13b), β comme multiplicateur et pente de la meilleure valeur en fonction du budget ; "
                    "avec un bruit gaussien de variance σ², changer σ² revient à changer β",
                    "posterior agrégé q(z) = E_x[q(z | x)], un mélange ; il égale le prior quand q(z | x) est le "
                    "posterior exact et que x suit la loi marginale du modèle, p(x) = Σ_z p(z) p(x | z)",
                    "E_x KL(q(z | x) ‖ p(z)) = I(X ; Z) + KL(q(z) ‖ p(z)) ≥ I(X ; Z) (M06) ; une KL moyenne nulle "
                    "veut dire un code indépendant de l'entrée (effondrement)",
                    "information mutuelle de deux variables continues, I(X ; Z) = h(Z) − h(Z | X) = "
                    "KL(p(x, z) ‖ p(x)p(z)), entropie différentielle conditionnelle (suite de M06 et de M25a) ; "
                    "celle d'une mesure gaussienne bruitée ½ ln(1 + s²/v), distorsion s² e^{−2I} ; le code s'éteint "
                    "quand β est assez grand"],
        "requires": [("espérance d'une variable continue, théorème de transfert, loi normale, fonction de "
                      "répartition Φ", "M02b"),
                     ("formule de Bayes, probabilités totales, logarithme d'une somme", "M04"),
                     ("log-sum-exp stable (`logsumexp`)", "M05a"),
                     ("entropie, divergence KL discrète, information mutuelle, inégalité de Jensen discrète", "M06"),
                     ("distance euclidienne, k-means", "M07"),
                     ("base orthonormée d'un sous-espace, Gram-Schmidt, projection orthogonale", "M12b"),
                     ("théorème spectral, valeurs propres d'une covariance", "M12c"),
                     ("SVD, ACP, approximation de rang faible", "M12d"),
                     ("maximum de vraisemblance, log-vraisemblance, proportion d'un mélange à composantes connues",
                      "M13a"),
                     ("multiplicateurs de Lagrange, KKT", "M13b"),
                     ("gradient par rapport à une matrice : ∇ ln det X et ∇ tr(AX)", "M18"),
                     ("estimateur de Monte-Carlo sans biais d'un gradient, variance d'un estimateur", "M19"),
                     ("densité et log-densité de N(μ, Σ) (`mvn_logpdf`), modèle linéaire gaussien, loi "
                      "conditionnelle, maximum de vraisemblance de μ et Σ, loi de μ + Lε, Jensen continu, KL continue "
                      "et KL entre gaussiennes, entropie différentielle", "M25a")],
        "frontieres": ["25.11", "25.13", "25.23", "25.30", "25.31", "25.32", "25.33", "25.34", "25.36", "25.38",
                       "25.Q9", "25.Q12", "25.R3", "25.E1", "25.E2", "25.E3"],
        "mymath": {"module": "latent.py",
                   "functions": ["gmm_e_step", "gmm_m_step", "gmm_log_likelihood", "gmm_elbo"]},
        "reading_minutes": 150,
        "flashcards": 22,
        "notes": "Frontières : le ∂ 25.5 (les dérivées de z = μ + σε par rapport à μ et à s = ln σ², ε fixé, E[z²] dérivée "
                 "avant ou après l'espérance, l'estimateur à un tirage du VAE), le ∂ 25.7 (KL(N(μ, σ²) ‖ N(0, 1)), en "
                 "s = ln σ², ses dérivées), le ∂ 25.8 (autoencodeur linéaire et ACP, déjà frontière de M12d), le 🗣️ "
                 "25.11 (ce qu'est un VAE), le 📄 25.13 (l'ELBO, AEVB et l'annexe B de Kingma et Welling), le 🔬 25.23 "
                 "(autoencodeur linéaire contre ACP, angles entre sous-espaces, `subspace_angles_deg_23`), le 📦 25.30 "
                 "(la loss « reconstruction + β KL » sommée, le β caché de 784), le 🔮 25.31 (décoder des tirages du "
                 "prior), le 🔬 25.32 (sorties répétées, moyenne des sorties contre sortie de la moyenne), le 📈 25.34 "
                 "et le 🔬 25.36 (effondrement du posterior, latents actifs, β montant, balayage de β), le 🎨 25.33 "
                 "(le nuage des μ d'un VAE contre le prior, que le posterior agrégé du §8 explique), le 🔨 25.38 "
                 "(gradient du VAE par deux chemins), les quiz 25.Q9 et 25.Q12, le rappel 25.R3 (la KL dans les deux "
                 "sens : M25b enseigne le sens de la KL), les 💼 25.E1, 25.E2 et 25.E3. M25b "
                 "travaille hors réseau : des machines et leurs pièces, des grains de café, des séries de résistances, "
                 "des longueurs de poissons, une sonde de qualité de l'eau, les épreuves d'un concours, des plans de "
                 "ℝ⁴, un stock face à une demande, des temps de trajet, une source à trois symboles, une mesure "
                 "bruitée ; jamais un encodeur, un décodeur, un réseau, une image, ni un VAE (seulement nommé dans "
                 "la fiche, comme ce que workbookIA 25 construira). **L'ELBO** est démontrée en général (∂ M25b.5 : "
                 "pour un latent discret ou continu, par la décomposition en KL au posterior, puis par Jensen) et "
                 "calculée là où tout se calcule : un latent à deux états et une mesure gaussienne (✏️ M25b.6), un "
                 "mélange de gaussiennes (🔨 M25b.22, `gmm_elbo`), l'ACP probabiliste (posterior exact). Garde-fous : "
                 "jamais l'ELBO d'un encodeur gaussien diagonal avec un prior N(0, I) et un décodeur de Bernoulli ou "
                 "gaussien ; dans l'ACP probabiliste, l'écart à la vraisemblance s'écrit KL(q ‖ p(z | x)) entre deux "
                 "gaussiennes dont aucune n'est le prior, et on ne calcule jamais KL(q(z | x) ‖ N(0, I)) ni une KL "
                 "contre N(0, 1) ou N(0, τ²) (∂ 25.7, 🔨 25.29) ; la forme « reconstruction moins KL au prior » ne "
                 "se calcule que pour un latent discret (KL(q ‖ π), 🔗 M25b.23) ; l'ELBO d'une chaîne de latents "
                 "(diffusion) est à MB5. **L'EM** est une montée par coordonnées de l'ELBO (∂ M25b.7 ; MML §11.4.5 "
                 "écrit Q(θ | θ_t)) ; ✏️ M25b.3 tient la promesse de M13a (estimer la proportion quand les "
                 "composantes sont aussi inconnues), sans reprendre ses densités ni ses données ; k-means comme "
                 "limite est dans la fiche (§4) et le quiz M25b.Q4 ; les singularités dans la fiche (§3), le quiz "
                 "M25b.Q3 et le 🔮 M25b.25. Les courbes monotones (🔬 M25b.26, 🛠️ M25b.29) se tracent sans "
                 "régularisation (reg = 0) : la régularisation ne sert qu'au 🔮 M25b.25 et au 🏆 M25b.30, et la fiche "
                 "(§4) dit pourquoi (avec reg > 0, le pas M ne maximise plus, et l'EM peut faire baisser la "
                 "log-vraisemblance et l'ELBO). Dans le 🔮 M25b.25, sans régularisation, la log-vraisemblance ne "
                 "devient pas +∞ : `gmm_m_step` rend une covariance nulle (ou presque, à l'arrondi près), que "
                 "`gmm_e_step` refuse quand Cholesky échoue ; l'expérience resserre donc à la main l'écart-type "
                 "d'une composante centrée sur un point (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis applique reg. Le gradient de "
                 "ln p(x) par l'identité "
                 "∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] (∂ M25b.7) s'applique à la moyenne d'une composante d'un "
                 "mélange, jamais à un réseau. **La dérivée d'une espérance** (la moitié « gradient » de la "
                 "reparamétrisation ; la moitié « loi » est en M25a) se fait sur des coûts : ∂ M25b.11 démontre "
                 "l'échange sous une hypothèse de domination, calcule la variance de l'estimateur à un tirage de "
                 "∂_σ E[e^X] et montre une indicatrice 1{X > c} pour laquelle l'échange échoue ; ✏️ M25b.12 dérive "
                 "E[(D − c)⁺] pour un stock c (dérivées P(D > c) et φ((c − μ)/σ), par le chemin puis par la formule "
                 "fermée), avec θ = μ ou σ directement ; aucune comparaison « dériver avant ou après l'espérance » "
                 "sur une fonction lisse (∂ 25.5.5) : la vérification par la formule fermée se fait sur le stock, "
                 "une fonction seulement continue ; jamais z², ½(z − y)², s = ln σ², une log-variance, σ ⊙ ε, ni « un "
                 "tirage par exemple dans un mini-batch » ; la méthode du score (∇ ln p) est seulement nommée (MB8). "
                 "M25b.Q7 n'a aucun item « peut-on dériver à travers un tirage » (25.Q12 c, ∂ 25.5.4) : seulement "
                 "les conditions de l'échange. "
                 "**Le sens de la KL** : ✏️ M25b.13 et 🎨 M25b.27 approchent un mélange bimodal de temps de trajet "
                 "par une seule gaussienne (KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un mode). **L'ACP "
                 "probabiliste** applique le modèle linéaire gaussien et le conditionnement de M25a sans les "
                 "redémontrer (∂ M25b.8) ; le maximum de vraisemblance de Tipping et Bishop est énoncé et appliqué à "
                 "des valeurs propres données (✏️ M25b.9 : un facteur latent, trois épreuves, une direction éteinte "
                 "quand le bruit est connu) ; l'inférence amortie s'y lit (la moyenne a posteriori est une règle "
                 "affine des notes, valable pour tous les candidats) ; aucun autoencodeur linéaire, aucun "
                 "« tr C − wᵀCw », ni cercle unité. **Les angles principaux** : ✏️ M25b.10 (deux plans de ℝ⁴, deux "
                 "droites de ℝ³ d'un angle autre que 30°, par la SVD de Q_Aᵀ Q_B) et 📦 M25b.24 "
                 "(`scipy.linalg.subspace_angles`) ; aucune fonction d'angles principaux dans `mymath` ni dans "
                 "`latent.py` (le notebook les calcule en NumPy) ; l'indépendance vis-à-vis des bases se démontre "
                 "(Q_A ↦ Q_A R_A), sans le contrôle « le même plan dans une autre base donne des angles nuls » ni une "
                 "fonction qui convertit `subspace_angles` en degrés (`subspace_angles_deg_23` et ses deux contrôles, "
                 "25.23), et aucun angle n'est pris entre un W estimé et le sous-espace de l'ACP (la question du "
                 "🔬 25.23) ; M25b.Q6 ne reprend pas la QCM de 25.Q9 a (« les axes, le sous-espace, un sous-espace "
                 "quelconque… »). **β** : ∂ M25b.15 le traite comme le multiplicateur "
                 "d'un budget d'information sur une mesure gaussienne bruitée (I = ½ ln(1 + s²/v), D = s² e^{−2I}, "
                 "le code s'éteint quand β ≥ 2s²), avec une variance de la source s² ≠ 1, l'information calculée par "
                 "les entropies différentielles h(Z) − h(Z | X) de M25a et jamais par une KL contre une gaussienne "
                 "centrée N(0, τ²) ; ✏️ M25b.14 décompose la KL "
                 "moyenne au prior (posterior agrégé, information mutuelle, effondrement) sur des tableaux discrets, "
                 "et prend la source égale à la loi marginale du modèle quand le posterior agrégé doit égaler le "
                 "prior ; "
                 "jamais de courbes d'entraînement, de seuil de latents actifs, de β = 1, 4, 16, 20 ou 100, ni de "
                 "« KL annealing ». **Partage avec M25a** (voir les rapports) : M25a enseigne la densité "
                 "(`mvn_logpdf`), les transformations affines et la loi de μ + Lε, le complément de Schur et le "
                 "conditionnement, le modèle linéaire gaussien, le maximum de vraisemblance non pondéré, Jensen "
                 "continu, la KL continue et la KL entre gaussiennes, l'entropie différentielle ; M25b les réutilise "
                 "sans les redémontrer et garde les mélanges (moments, variance totale, MML Théorème 6.12), l'EM, "
                 "l'ELBO, l'ACP probabiliste, la dérivée d'une espérance, le sens de la KL, les angles principaux, β, "
                 "l'inférence amortie et le posterior agrégé. **Partage avec M26** : M25b définit l'espérance et la "
                 "variance conditionnelles sachant une variable discrète et les lois de l'espérance et de la "
                 "variance totales (les mélanges en ont besoin) ; M26, qui vient après, les rappelle et y ajoute la "
                 "propriété de la tour et l'analyse au premier pas. **MML** : §8.4 (8.4.1 à 8.4.3) et §8.5 (8.5.1 ; "
                 "la d-séparation de 8.5.2 en survol) avant §1 et §2 : 📖 M25b.16 ; §6.5.3 (le Théorème 6.12, les "
                 "moments d'un mélange de deux gaussiennes) avant §2 ; ch. 11 (11.1 à 11.4) avant §3 à §5 : "
                 "📖 M25b.17 ; §10.7 (10.7.1 à "
                 "10.7.3) avant §6 : 📖 M25b.18. MML n'a pas l'ELBO (§11.4.5 s'arrête à Q(θ | θ_t)) : lecture libre "
                 "conseillée, MacKay ch. 22 (EM, k-means doux) et ch. 33 (méthodes variationnelles). Exercices du "
                 "livre conseillés : 6.11 (*Iterated Expectations*, l'espérance totale) et 6.2 (les moments d'un "
                 "mélange de deux gaussiennes ; conseillé, jamais repris : ✏️ M25b.2 prend d'autres lois et "
                 "d'autres nombres) ; les ch. 8, 10 et 11 n'en ont pas. **Conventions** : données rangées en lignes, "
                 "de forme (n, d), dans `mymath` et le notebook (une mesure en dimension 1 est un tableau (n, 1)) ; "
                 "poids (K,), moyennes (K, d), covariances (K, d, d) ; responsabilités (n, K) ; logarithmes "
                 "népériens, ELBO, KL et informations en nats ; la fiche écrit les vecteurs en colonnes. `latent` : "
                 "NumPy permis, de "
                 "`np.linalg` seulement `cholesky` et `solve` (pour rien de plus que `gaussian`), ni `np.cov` ni "
                 "`np.average` (avec `aweights` et `weights`, ils font le pas M, et ce sont les oracles des tests), "
                 "aucune SciPy ; il importe `mvn_logpdf` de `gaussian` (M25a) et peut importer `logsumexp` "
                 "d'`approx` (M05a), par des imports relatifs (tout import relatif de ses propres modules est "
                 "permis) ; aucune fonction de KL, de reparamétrisation, d'angles principaux ni d'ACP "
                 "probabiliste. Le notebook se sert aussi de `gaussian` : `sample_mvn` pour le tirage ancestral des "
                 "données (🔬 M25b.26, 🏆 M25b.30), `mvn_logpdf` et `condition_gaussian` (le posterior de l'ACP "
                 "probabiliste comme loi conditionnelle de la loi jointe de (z, x)) dans le 📦 M25b.24. Écarts au "
                 "plan : `gmm_elbo` ajoutée (décision du coordinateur) ; MML §6.7 passe à "
                 "M25a ; deux sessions de génération (§1 à §4, puis §5 à §8). Les exemples du stub ne reviennent "
                 "dans aucun exercice : les mesures (0,5 ; 2 ; 3,5 ; 6) avec les poids (0,4 ; 0,6), les moyennes 1 et "
                 "5 et les variances 1 et 2, le point 1000 ; les points (0, 0), (1, 0), (0, 2), (4, 4), (5, 3) ; "
                 "reg = 0,1 ; ✏️ M25b.3 (quatre mesures, comme l'exemple de `gmm_e_step`) prend d'autres poids que "
                 "(0,4 ; 0,6), d'autres moyennes et d'autres variances. "
                 "**Évités** (règle de partage, et reprises de ce dépôt) : l'ELBO d'un encodeur gaussien diagonal, "
                 "d'un prior N(0, I) et d'un décodeur de Bernoulli ; la loss « reconstruction sommée + β KL » sur des "
                 "images ; le facteur 784, « β caché de 784 », « 784 fois plus petite » ; β ∈ {0,5 ; 1 ; 4 ; 16} et "
                 "{1, 20, 100, montant} ; 2, 3, 8, 10, 16, 20, 32, 50 et 64 latents ; le seuil de latents actifs "
                 "0,05 nat ; `HISTORY_34` ; les KL 17,6 → 2,2, 68,01 → 22,38, 45,6, 113,8 ; les reconstructions 171, "
                 "104 et 152 nats ; les covariances C = [[5, 2], [2, 2]] (valeurs propres 6 et 1, w = (2, 1)/√5) et "
                 "[[3, 1], [1, 3]] (4 et 2) ; le cercle unité (C = ½ I, l'angle comme code) ; u = (0,6 ; 0,8) et "
                 "x = (5, 0) ; les plans z = 0 et incliné de 30°, la base [[2, 1], [1, 3]], k = 16, les angles 1,6° "
                 "et 6,4°, les cosinus 0,02 et 0,10, les erreurs 0,02727 et 0,02725, « k = 4, 2 epochs, 2 000 "
                 "images » (25.23) ; 34 %, 69 %, 90 % contre 39 %, 86 %, 99 %, un nuage de moyennes comparé aux "
                 "disques du prior (25.33) ; un tirage par exemple et le mini-batch de 100 de Kingma et Welling ; « moyenne des sorties "
                 "contre sortie de la moyenne » d'un décodeur ; le PSNR moyen image par image ; la KL contre N(0, 1), "
                 "N(0, I) ou N(0, τ²) et ½(μ² + σ² − 1 − ln σ²) ; s = ln σ² ; μ = 0,5, ln σ² = ln 0,25 et ε = −2 "
                 "(workbookIA B5.R3) ; z = μ + σε avec (1,5 ; 0,5 ; −2) ; « 68 % entre −1 et 1 » ; la grille −3 à 3 "
                 "et ses 80 tirages ; les 10 000 images, 60 000 exemples, 28 × 28, 512 × 512 × 3 et 64 × 64 × 4 ; "
                 "le 99ᵉ centile ; de MML, (11.5) (0,5 N(−2, ½) + 0,2 N(1, 2) + 0,3 N(4, 1)), l'Exemple 11.1 "
                 "(données {−3 ; −2,5 ; −1 ; 0 ; 2 ; 4 ; 5}, initialisation N(−4, 1), N(0 ; 0,2), N(8, 3), π = ⅓ ; "
                 "refait avec d'autres données dans le 📖 seulement), les responsabilités (11.19), le mélange de "
                 "l'exercice 6.2 (0,4 N((10, 2), I) + 0,6 N(0, [[8,4 ; 2] ; [2 ; 1,7]])), les figures de §10.7 ; de "
                 "ce dépôt, l'exemple de mélange de M13a "
                 "(f₀, f₁ et ses données), la matrice [[3, 1], [1, 2]] de 🔁 M09b.R1, les exemples des stubs "
                 "`gaussian` (Σ = [[2, 3], [3, 9]], "
                 "[[5, 2, 2], [2, 4, 0], [2, 0, 4]], Φ = [[1, 0], [1, 1], [1, 2]]) et `approx` ; MNIST, "
                 "Fashion-MNIST, Frey Face, CIFAR-10 contre SVHN, l'anomalie MNIST contre Fashion-MNIST, le tigre. "
                 "**Durée** : 16,8 h au lieu des 14 h prévues (essentiel 13,7 h) : l'ELBO démontrée en général, la "
                 "dérivée d'une espérance, les angles principaux, β, le posterior agrégé et l'inférence amortie, que "
                 "la planification ne comptait pas, et quatre blocs de MML (≈ 35 pages, trois 📖 au lieu de 1–2). "
                 "COMPOSITION : trois 📖 (quatre blocs de MML de sujets distincts).",
        "exercises": [
            ("M25b.Q1", "🧠", 1, 4, "Lire un graphe orienté : factoriser la loi jointe, l'ordre d'un tirage ancestral, et "
             "les variables qui deviennent dépendantes quand on observe leur effet commun", "§1", "E"),
            ("M25b.Q2", "🧠", 1, 4, "Marginaliser ou conditionner : vraisemblance marginale, posterior d'un latent, moyenne "
             "et variance d'un mélange", "§2", "E"),
            ("M25b.Q3", "🧠", 1, 4, "Un mélange de gaussiennes : responsabilités, logarithme d'une somme, vraisemblance "
             "infinie et composantes renumérotées", "§3", "E"),
            ("M25b.Q4", "🧠", 1, 4, "L'EM : ce que font le pas E et le pas M, ce qui ne baisse jamais, ce qui n'est pas "
             "garanti, et k-means comme limite", "§4", "E"),
            ("M25b.Q5", "🧠", 1, 4, "L'ELBO : une borne de quoi, une égalité quand, un écart égal à quelle KL ?", "§5", "E"),
            ("M25b.Q6", "🧠", 1, 4, "L'ACP probabiliste : covariance marginale, rotation de W, angles principaux et "
             "directions éteintes", "§6", "E"),
            ("M25b.Q7", "🧠", 1, 4, "KL directe ou inverse, inférence amortie et écart d'amortissement, et dériver sous "
             "l'espérance : quand le peut-on ?", "§7", "E"),
            ("M25b.Q8", "🧠", 1, 4, "Pondérer la KL : multiplicateur, information mutuelle, posterior agrégé et code "
             "effondré", "§8", "E"),
            ("M25b.R1", "🔁", 1, 6, "Bayes sur une variable cachée et log-sum-exp : probabilités totales, posterior, et "
             "une somme d'exponentielles sans dépassement (M04, M05a)", "§2 §3", "E"),
            ("M25b.R2", "🔁", 1, 6, "L'inégalité de Jensen, la KL continue et l'information mutuelle (M06, M25a)",
             "§5 §8", "E"),
            ("M25b.R3", "🔁", 1, 6, "La SVD, l'ACP et la projection orthogonale sur un sous-espace (M12b, M12d)", "§6",
             "E"),
            ("M25b.1", "✏️", 2, 20, "Trois machines produisent des pièces de longueurs gaussiennes : le graphe, la loi "
             "jointe, un tirage ancestral à la main, la vraisemblance marginale d'une longueur et le posterior de la "
             "machine", "§1 §2", "E"),
            ("M25b.2", "✏️", 2, 25, "Deux variétés de grains de café (longueur, largeur) : moyenne et covariance du "
             "mélange par la variance totale, part de la variance entre variétés, et une corrélation qu'aucune "
             "variété n'a", "§2", "E"),
            ("M25b.3", "✏️", 2, 35, "Deux séries de résistances mélangées : les responsabilités de quatre mesures en log, un "
             "pas M (proportion, moyennes, variances), et la log-vraisemblance qui monte (suite de M13a, composantes "
             "inconnues)", "§3 §4", "E"),
            ("M25b.4", "∂", 2, 30, "Le pas M d'un mélange de gaussiennes : les poids N_k/n par un multiplicateur de "
             "Lagrange, les moyennes et les covariances comme maximum de vraisemblance pondéré", "§4", "E"),
            ("M25b.5", "∂", 3, 30, "L'ELBO en général : ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour un latent discret ou "
             "continu, la borne retrouvée par Jensen, et la forme E_q[ln p(x | z)] − KL(q ‖ p(z))", "§5", "E"),
            ("M25b.6", "✏️", 2, 25, "Une sonde de qualité de l'eau, un état caché à deux valeurs et une mesure "
             "gaussienne : ln p(x), l'ELBO pour trois lois q, et l'écart égal à la KL au posterior", "§5", "E"),
            ("M25b.7", "∂", 3, 30, "L'EM comme montée par coordonnées de l'ELBO : le pas E maximise en q, le pas M en θ, "
             "d'où la monotonie ; et ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] pour la moyenne d'une composante",
             "§4 §5", "E"),
            ("M25b.8", "∂", 2, 30, "L'ACP probabiliste : la loi marginale N(μ, WWᵀ + σ²I), le posterior de z par le "
             "modèle linéaire gaussien, et W ou WR donnent la même loi", "§6", "E"),
            ("M25b.9", "✏️", 2, 30, "Trois épreuves d'un concours expliquées par une aptitude cachée : covariance "
             "marginale, posterior d'un candidat (une règle affine des notes), et maximum de vraisemblance à partir de "
             "valeurs propres données, dont une direction éteinte", "§6 §7", "E"),
            ("M25b.10", "✏️", 2, 25, "Les angles principaux entre deux plans de ℝ⁴ et entre deux droites de ℝ³ : bases "
             "orthonormées, SVD de Q_Aᵀ Q_B, et pourquoi le résultat ne dépend pas des bases choisies", "§6", "E"),
            ("M25b.11", "∂", 3, 25, "Dériver une espérance par rapport à un paramètre de la loi : l'échange de la dérivée et de "
             "l'espérance sous une hypothèse de domination (démontré), la variance de l'estimateur à un tirage de "
             "∂_σ E[e^X], et une indicatrice 1{X > c} pour laquelle l'échange échoue", "§7", "E"),
            ("M25b.12", "✏️", 3, 30, "Le coût d'un stock c face à une demande gaussienne : E[(D − c)⁺], ses dérivées en μ et "
             "en σ par le chemin, puis par la formule fermée", "§7", ""),
            ("M25b.13", "✏️", 2, 25, "Une seule gaussienne pour la loi bimodale des temps de trajet par deux itinéraires : "
             "KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un itinéraire", "§7", "E"),
            ("M25b.14", "✏️", 2, 30, "Un code stochastique d'une source à trois symboles : posterior agrégé, information "
             "mutuelle, KL moyenne au prior décomposée en I(X ; Z) + KL(q(z) ‖ p(z)), puis le code qui s'effondre",
             "§8", "E"),
            ("M25b.15", "∂", 3, 30, "β comme multiplicateur de Lagrange : une mesure gaussienne codée avec du bruit, "
             "distorsion s² e^{−2I}, le lagrangien D + βI, et le code qui s'éteint quand β dépasse 2s²", "§8", "E"),
            ("M25b.16", "📖", 2, 25, "MML §8.4 et §8.5 : modèles probabilistes, inférence bayésienne, modèles à variables "
             "latentes, graphes orientés et d-séparation (survol), en anglais", "§1 §2", ""),
            ("M25b.17", "📖", 2, 35, "MML ch. 11 : mélange de gaussiennes, responsabilités, mises à jour, EM et point de "
             "vue latent, en anglais ; refaire l'Exemple 11.1 avec ses propres données", "§3 §4 §5", ""),
            ("M25b.18", "📖", 2, 20, "MML §10.7 : l'ACP probabiliste, processus génératif, vraisemblance, loi jointe et "
             "posterior, en anglais", "§6", ""),
            ("M25b.19", "🗣️", 1, 10, "Expliquer l'EM avec un bac de pièces venues de deux machines inconnues : deviner, "
             "réestimer, recommencer, sans jamais reculer", "§4", "E"),
            ("M25b.E1", "💼", 1, 10, "« Pourquoi l'algorithme EM ne fait-il jamais baisser la vraisemblance, et vers quoi "
             "converge-t-il ? »", "§4 §5", "E"),
            ("M25b.20", "🔨", 2, 30, "Les responsabilités d'un mélange de gaussiennes, calculées en log (le pas E)", "§3",
             "E m:gmm_e_step"),
            ("M25b.21", "🔨", 2, 30, "Le pas M d'un mélange de gaussiennes : poids, moyennes et covariances pondérées, "
             "avec une régularisation", "§4", "E m:gmm_m_step"),
            ("M25b.22", "🔨", 2, 25, "La log-vraisemblance d'un mélange de gaussiennes, et son ELBO pour des "
             "responsabilités quelconques", "§3 §5", "E m:gmm_log_likelihood,gmm_elbo"),
            ("M25b.23", "🔗", 1, 20, "Pont : l'ELBO de n mesures rangées en lignes, écrite « reconstruction moins KL "
             "au prior » E_q[ln p(x | z)] − KL(q ‖ π), en nats par mesure, et ce que gagne chaque terme quand q "
             "devient le posterior", "§5", "E p:M25b.22"),
            ("M25b.24", "📦", 1, 20, "`scipy.linalg.subspace_angles` et `np.linalg.eigh` : les angles principaux de "
             "M25b.10, et l'ACP probabiliste de mesures par leurs valeurs propres, contre la vraisemblance de "
             "`mvn_logpdf`", "§6", "E p:M25b.10"),
            ("M25b.25", "🔮", 1, 15, "Prédire ce que devient la log-vraisemblance quand une composante centrée sur un "
             "point se resserre (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis avec une régularisation, et mesurer", "§3 §4",
             "p:M25b.20,M25b.21,M25b.22"),
            ("M25b.26", "🔬", 2, 25, "L'EM sur des longueurs de poissons de trois cohortes : la log-vraisemblance et "
             "l'ELBO après chaque demi-pas, sans régularisation, plusieurs initialisations et des maxima locaux", "§4 §5",
             "E p:M25b.20,M25b.21,M25b.22"),
            ("M25b.27", "🎨", 1, 20, "Une gaussienne ajustée à un mélange bimodal par KL(p ‖ q) puis par KL(q ‖ p) : les "
             "deux courbes, et les deux minima de la KL inverse", "§7", "p:M25b.13"),
            ("M25b.28", "🐛", 1, 20, "Chasse à l'erreur : des responsabilités sans log qui donnent 0/0, un pas M qui divise "
             "par n au lieu de N_k, et une ELBO sans l'entropie de q", "§3 §4 §5", "E"),
            ("M25b.29", "🛠️", 1, 15, "Un test de propriété : sur des mélanges tirés au hasard, ELBO ≤ log-vraisemblance, "
             "égalité après le pas E, et un EM sans régularisation (reg = 0) qui ne descend jamais (à une "
             "tolérance près)", "§4 §5",
             "p:M25b.20,M25b.21,M25b.22"),
            ("M25b.30", "🏆", 3, 25, "Défi : retrouver trois populations de mesures en dimension 2 par l'EM, sous un seuil "
             "de log-vraisemblance moyenne sur des mesures de test", "§4", "p:M25b.20,M25b.21,M25b.22"),
        ],
    },
    {
        "id": "M26", "dir": "m26_markov_bellman", "hours": 14.6, "generation_sessions": 1, "mml": [],
        "summary": "Les chaînes de Markov finies et ce qu'on calcule sur elles : la matrice de transition, la loi après n "
                   "pas (en convention ligne) et la loi stationnaire (existence, unicité, convergence, vitesse, et le "
                   "PageRank) ; l'espérance conditionnelle et l'analyse au premier pas (la probabilité d'être absorbé, la "
                   "durée moyenne avant la fin) ; le retour actualisé comme variable aléatoire, le facteur γ vu comme une "
                   "probabilité de continuer, les décisions et les politiques ; l'équation de Bellman d'une politique "
                   "fixée, un système linéaire (I − γP)V = r, résolu exactement ou par l'itération d'une contraction ; un "
                   "opérateur avec un maximum, sur un problème d'arrêt optimal ; enfin ce que deviennent ces équations "
                   "quand on n'a que des échantillons : la moyenne de retours simulés, l'erreur TD et le biais du maximum. "
                   "workbookIA 26 applique ces outils à l'apprentissage par renforcement.",
        "objectives": [
            "Écrire la matrice de transition d'une chaîne de Markov, en convention ligne, et calculer la loi après n pas.",
            "Calculer une loi stationnaire, dire si elle est unique et si la loi de la chaîne y converge, et à quelle "
            "vitesse.",
            "Calculer une probabilité d'absorption et une durée moyenne par l'analyse au premier pas (espérance "
            "conditionnelle).",
            "Définir le retour actualisé et la valeur d'un état sous une politique fixée, et interpréter γ comme une "
            "probabilité de continuer.",
            "Écrire et résoudre le système de Bellman d'une politique fixée, et justifier qu'il a une unique solution.",
            "Itérer l'opérateur de Bellman, borner l'erreur et choisir le nombre d'itérations.",
            "Résoudre un problème d'arrêt optimal par un opérateur avec un maximum, et lire l'équation d'optimalité de "
            "Bellman.",
            "Relier la moyenne de retours simulés, l'erreur TD et le biais du maximum aux équations exactes.",
        ],
        "sections": [("§1", "Chaînes de Markov : matrice de transition, graphe et loi à n pas"),
                     ("§2", "La loi stationnaire : existence, unicité, convergence et vitesse ; le PageRank"),
                     ("§3", "Espérance conditionnelle et analyse au premier pas : absorption et durée moyenne"),
                     ("§4", "Récompenses, retour actualisé et valeur d'un état ; décisions et politiques"),
                     ("§5", "L'équation de Bellman d'une politique fixée : un système linéaire"),
                     ("§6", "Itérer l'opérateur de Bellman : contraction, bornes d'erreur, itérations synchrones et en "
                            "place"),
                     ("§7", "Un maximum dans l'opérateur : arrêt optimal et équation d'optimalité"),
                     ("§8", "Des échantillons au lieu de P : moyenne de retours, erreur TD et biais du maximum")],
        "teaches": ["chaîne de Markov finie : propriété de Markov, matrice de transition stochastique (lignes de somme 1), "
                    "graphe de transition",
                    "convention ligne pour les lois : μ_{n+1} = μ_n P, loi à n pas μ₀Pⁿ, Chapman-Kolmogorov "
                    "P^{m+n} = P^m P^n, (Pⁿ)_ij comme somme sur les chemins ; convention colonne pour les fonctions : "
                    "E[f(S_{n+1}) | S_n = i] = (Pf)_i",
                    "‖P‖∞ = 1 et ρ(P) = 1 ; loi stationnaire π = πP, Σπ = 1 : existence (Perron-Frobenius admis), calcul "
                    "par un système linéaire ou par la méthode de la puissance",
                    "chaîne irréductible, apériodique : unicité de π et convergence de μ₀Pⁿ (énoncées) ; contre-exemples "
                    "(chaîne périodique, chaîne à deux classes) ; vitesse de convergence fixée par |λ₂|",
                    "PageRank : le surfeur aléatoire et le facteur d'amortissement",
                    "espérance conditionnelle E[X | Y = y] et formule de l'espérance totale (rappel de M25b), "
                    "propriété de la tour, appliquées à l'analyse au premier pas",
                    "états absorbants et transitoires ; analyse au premier pas : probabilités d'absorption h = Qh + b, "
                    "durées moyennes t = 1 + Qt ; matrice fondamentale (I − Q)⁻¹ = Σ Qᵗ",
                    "retour actualisé G = Σ γᵗ r(S_t) comme variable aléatoire ; valeur V(s) = E[G | S₀ = s] ; γ comme "
                    "probabilité de continuer : durée géométrique d'espérance 1/(1 − γ)",
                    "processus de décision markovien : états, actions, matrices P_a, récompenses r(s, a, s′) et leur "
                    "moyenne r(s, a) ; politique déterministe ou stochastique ; chaîne induite P_π, r_π ; valeur d'une "
                    "action Q^π(s, a)",
                    "équation de Bellman d'une politique fixée V = r + γPV : système linéaire (I − γP)V = r, inversible "
                    "pour γ < 1 (‖γP‖∞ = γ), série de Neumann V = Σ γᵗPᵗr, loi d'occupation actualisée "
                    "(1 − γ)(I − γP)⁻¹ ; une fin possible : matrice sous-stochastique, γ = 1 permis quand la fin est sûre",
                    "opérateur de Bellman, γ-contraction pour ‖·‖∞ ; convergence géométrique en γᵏ ; borne a posteriori "
                    "γ/(1 − γ)‖V_k − V_{k−1}‖∞ et critère d'arrêt ; itérations synchrones (Richardson de pas 1) et en "
                    "place (Gauss-Seidel) ; théorème du point fixe de Banach (énoncé)",
                    "un opérateur avec un maximum : |max x − max y| ≤ max |x − y| ; arrêt optimal V = max(g, c + γPV), "
                    "valeur de continuation et règle à seuil ; équation d'optimalité de Bellman, itération sur les valeurs "
                    "et politique gloutonne (énoncées)",
                    "estimer une valeur par la moyenne de retours simulés, tronqués ; pas 1/n et pas constant ; conditions "
                    "de Robbins-Monro Σαₜ = ∞, Σαₜ² < ∞ (énoncées)",
                    "erreur TD δ = r + γV(s′) − V(s) : son espérance conditionnelle est le résidu de Bellman ; "
                    "Σ γᵏ δ_{t+k} = G_t − V(S_t) (télescopage) ; récompense ajoutée γΦ(s′) − Φ(s)",
                    "biais du maximum : E[max X̂ᵢ] ≥ max E[X̂ᵢ], E[max(Z₁, Z₂)] = 1/√π ; estimateur double (choisir sur "
                    "un échantillon, mesurer sur l'autre)"],
        "requires": [("suites géométriques et leur somme, actualisation, moyennes mobile et exponentielle", "R5"),
                     ("logarithmes : résoudre γᵏ ≤ ε", "R6"),
                     ("loi géométrique et son espérance, loi normale, linéarité de l'espérance", "M02b"),
                     ("loi des grands nombres, erreur type d'une moyenne", "M02c"),
                     ("probabilité conditionnelle, probabilités totales", "M03"),
                     ("inégalité de Jensen", "M06"),
                     ("systèmes linéaires, inverse d'une matrice", "M09a"),
                     ("moyenne incrémentale, ε-greedy (une politique stochastique)", "M11"),
                     ("valeurs propres, diagonalisation et puissances, méthode de la puissance", "M12c"),
                     ("puissances d'une matrice d'adjacence : sommes sur les chemins d'un graphe", "M16"),
                     ("itérations linéaires, point fixe, itération de Richardson", "M19"),
                     ("tableaux à plusieurs axes, einsum", "M20"),
                     ("normes induites ‖·‖₁ et ‖·‖∞, ρ(A) ≤ ‖A‖, Aᵗ → 0 si ρ(A) < 1, applications contractantes et "
                      "oubli du point de départ", "M22"),
                     ("espérance conditionnelle sachant une variable discrète, espérance et variance totales", "M25b")],
        "frontieres": ["26.1", "26.3", "26.4", "26.5", "26.6", "26.9", "26.12", "26.14", "26.26", "26.Q6", "26.Q8",
                       "26.Q9", "26.Q10", "26.R3", "26.E2", "26.E4", "11.2", "19.8", "B8.Q4", "B8.Q7", "B8.1", "B8.4"],
        "mymath": {"module": "markov.py",
                   "functions": ["n_step_distribution", "stationary_distribution", "bellman_linear_solve",
                                 "bellman_fixed_point_iterates"]},
        "reading_minutes": 160,
        "flashcards": 22,
        "notes": "Frontières : les ∂ 26.7 (la somme géométrique (1 − γⁿ)/(1 − γ), la borne r_max/(1 − γ), les horizons "
                 "2, 10 et 100, la demi-vie ln 2/(−ln γ), 0,2⁴ et 0,2⁶) et 26.8 (l'équation d'optimalité sur le MDP A, B, "
                 "T, son système 2 × 2 sous une politique supposée optimale, la contraction de l'opérateur d'optimalité "
                 "en norme max et la convergence vers une seule table, la cible du Q-learning comme échantillon et le "
                 "rôle de α), les ✏️ 26.1 (les retours d'une partie de six coups), 26.3 et 26.4 (une mise à jour de "
                 "Q-learning et de SARSA), 26.5 (les probabilités d'ε-greedy et de la softmax), 26.6 (la valeur qui "
                 "remonte une chaîne, un état par épisode), 🧮 26.9 (la mémoire d'une table Q), 📄 26.12 (DQN, et sa "
                 "variante Double Q-learning), 🔨 26.14 (retours et retours à venir) et 26.26 (`value_iteration`), les "
                 "quiz 26.Q6 (retour d'une courte suite, horizon de 0,95), 26.Q8, 26.Q9 et 26.Q10 (la valeur qui remonte "
                 "depuis une table nulle), le rappel 26.R3 (la mise à jour incrémentale d'un bandit), 26.E2 (à quoi sert "
                 "γ) et 26.E4 (rejeu, réseau cible, surestimation corrigée par le Double DQN) ; de workbookIA 11 et 19, "
                 "faits avant M26, ∂ 11.2 (la moyenne incrémentale) et ∂ 19.8 (la mémoire effective et le biais initial "
                 "d'une moyenne exponentielle), énoncés et utilisés, jamais redémontrés ; de workbookIA B8, B8.Q4 (d'où "
                 "vient la surestimation), B8.1 (cible DQN puis Double DQN), B8.Q7 et B8.4 (avantage, erreur TD et "
                 "GAE : M26 n'écrit aucune somme pondérée par λ). "
                 "M26 enseigne les outils hors apprentissage par renforcement : des vélos entre des stations, des parts "
                 "de marché, un petit web, un cursus avec redoublement et abandon, un abonné qui peut résilier, une "
                 "machine qui s'use et son entretien, un stock, la vente d'une voiture d'occasion, des fournisseurs "
                 "mesurés avec du bruit ; jamais un agent, un jeu, un coup, une partie, une table Q, une cible "
                 "r + γ max Q, un learning rate α appliqué à une table, ni Gymnasium (son format "
                 "P[s][a] = [(p, s′, r, fin)], `terminated` et `truncated`). "
                 "L'espérance conditionnelle sachant une variable discrète et la formule de l'espérance totale sont "
                 "définies en M25b (les mélanges) : M26 les rappelle et y ajoute la propriété de la tour et l'analyse "
                 "au premier pas. ∂ M26.11 démontre la série de Neumann pour γP en entier (‖γP‖∞ = γ < 1), sans "
                 "renvoyer à CP5.8, un sujet au choix, ni à M22, qui ne l'écrit que dans un corrigé. "
                 "Contraction et maximum (les deux moitiés de ∂ 26.8.3, que M22 a laissées à M26) : le §6 démontre la "
                 "contraction de l'opérateur de Bellman d'une politique **fixée**, qui est affine "
                 "(‖γP(V − W)‖∞ ≤ γ‖V − W‖∞ par ‖P‖∞ ≤ 1, M22), et les bornes a priori γᵏ‖V₀ − V‖∞ et a posteriori "
                 "γ/(1 − γ)‖V_k − V_{k−1}‖∞ (∂ M26.12), sans avoir besoin de Banach (le point fixe existe : c'est la "
                 "solution du système) ; l'existence du point fixe d'une contraction non linéaire (Banach) est énoncée "
                 "et admise, comme en M22. Le §7 démontre le lemme |max x − max y| ≤ max |x − y| sur des vecteurs "
                 "quelconques (l'indication que donne ∂ 26.8.3) et s'en sert sur un problème d'arrêt optimal à offres "
                 "indépendantes (une seule équation pour la valeur de continuation, une règle à seuil) ; que l'opérateur "
                 "d'arrêt V ↦ max(g, c + γPV) est une γ-contraction est **énoncé**, sans démonstration : combiner le "
                 "lemme et le §6 est ce que ∂ 26.8.3 fait pour l'opérateur d'optimalité : ni la grille de ∂ M26.12, ni "
                 "la fiche, ni un quiz n'écrivent la chaîne |max(g, c + γPV) − max(g, c + γPW)| ≤ … ; M26.Q7 "
                 "énonce la contraction de l'opérateur d'arrêt comme un fait, sans demander de justification ; dans "
                 "M26.6, la valeur d'une action Q^π(s, a) ne sert ni à vérifier qu'une politique est gloutonne pour "
                 "ses propres valeurs, ni à désigner la meilleure des deux (∂ 26.8.2). L'équation d'optimalité de "
                 "Bellman, l'itération sur les valeurs et la politique gloutonne sont énoncées, jamais résolues sur un "
                 "MDP à plusieurs actions : ni « supposer la politique optimale et résoudre » (∂ 26.8.2), ni table Q*. "
                 "Le §8 relie l'erreur TD d'une politique fixée au résidu de Bellman (son espérance conditionnelle) et "
                 "démontre le télescopage (∂ M26.13, que MB8 rappellera, sur des épisodes qui finissent, de valeur 0 "
                 "à la fin : ni troncature avec amorçage, ni question sur la dépendance de la somme à V, B8.4 j, "
                 "B8.Q7 e–f) ; il n'écrit aucune cible avec un max et ne "
                 "discute pas α dans le Q-learning (∂ 26.8.4) : le pas 1/n et le pas constant portent sur des mesures "
                 "ou des retours simulés, et Σαₜ = ∞, Σαₜ² < ∞ sont énoncées (Robbins-Monro), sans preuve. Le biais du "
                 "maximum (E[max X̂ᵢ] ≥ max E[X̂ᵢ] ; E[max(Z₁, Z₂)] = 1/√π pour deux gaussiennes centrées réduites "
                 "indépendantes ; l'estimateur double) porte sur des fournisseurs ou des réglages mesurés avec du bruit "
                 "(la malédiction du vainqueur, et le score de validation optimiste d'un modèle choisi sur la "
                 "validation), sans réseau, DQN, cible ni van Hasselt. "
                 "Le facteur γ : M26 l'interprète comme une probabilité de continuer (arrêt avec la probabilité 1 − γ à "
                 "chaque pas, durée géométrique d'espérance 1/(1 − γ), M02b), sur un abonné qui résilie (M26.5) ; il "
                 "ne redémontre pas la somme géométrique (R5) et ne parle ni d'« horizon effectif » ni de demi-vie de γ "
                 "(∂ 26.7) ; aucun quiz ne calcule le retour d'une courte suite de récompenses (26.Q6), et la valeur "
                 "actuelle d'un échéancier (R5.11) n'est qu'un exemple de la fiche, sans fonction de `mymath` (🔨 26.14). "
                 "Les γ des exercices de M26 sont pris parmi 0,6, 0,7, 0,85 et 0,96 : jamais 0,2, 0,5, 0,8, 0,9, 0,95 "
                 "ni 0,99, les facteurs de workbookIA 26 (0,8 : sa fiche et le 🔨 26.20), ni 0,75 (les exemples de "
                 "`markov`). "
                 "La loi stationnaire ne sert aucun exercice de workbookIA 26 : un § court (existence par ‖P‖∞ = 1 et "
                 "ρ(P) = 1 ; unicité et convergence pour une chaîne irréductible apériodique énoncées, avec deux "
                 "contre-exemples ; vitesse |λ₂|ⁿ, la chaîne à deux états entièrement calculée dans la fiche ; PageRank), "
                 "un seul ✏️ dans le parcours essentiel (M26.2), justifié dans la fiche par la promesse de M12c (§3 et "
                 "§4 : le PageRank par la méthode de la puissance, la vitesse par la deuxième valeur propre), par la "
                 "fréquence de visite des états, par MB5 (une chaîne qui converge vers sa loi stationnaire) et par MB8 "
                 "(la loi d'occupation actualisée (1 − γ)μ₀(I − γP)⁻¹, dont les lignes tendent vers π quand γ → 1 : "
                 "🔮 M26.21). "
                 "Conventions : π(a | s) est une politique (comme workbookIA 26) ; la loi stationnaire s'écrit π aux "
                 "§1 à §3 et d_π pour celle de P_π à partir du §4, et un encadré 📐 le dit (la docstring de "
                 "`stationary_distribution` garde π) ; les lois sont des lignes (μ_{n+1} = μ_nP, celle des "
                 "probabilistes), les valeurs des "
                 "colonnes ((PV)_i = E[V(S₁) | S₀ = i]) ; un encadré 📐 le dit au §1 et le relie à la convention colonne "
                 "de M22 (μ₀Pⁿ est la récurrence de M22 pour Pᵀ, sans entrée). workbookIA 26 n'écrit jamais P comme une "
                 "matrice (des sommes Σ_{s′} P(s′ | s, a), avec r(s, a, s′)) : le 🔗 M26.14 fait le passage. Une fin "
                 "possible se code de deux façons qui donnent les mêmes valeurs : un état absorbant de récompense nulle, "
                 "ou une ligne sous-stochastique (la masse manquante est la probabilité de finir) ; c'est le « le max "
                 "vaut 0 quand s′ est terminal » de workbookIA 26, et γP est elle-même sous-stochastique (actualiser, "
                 "c'est finir avec la probabilité 1 − γ). M26.6 et M26.7 portent sur la même machine (M26.7 itère vers "
                 "la solution exacte de M26.6). "
                 "`markov` : NumPy permis, mais de `np.linalg` seulement `solve` et `matrix_rank`, dans "
                 "`stationary_distribution` et `bellman_linear_solve` ; ni `matrix_power`, `eig`, `eigvals`, `inv`, ni "
                 "SciPy (oracles des tests : `np.linalg.matrix_power`, `np.linalg.eig` sur Pᵀ, `scipy.linalg.null_space`, "
                 "`scipy.linalg.solve`, la série Σ γᵗPᵗr tronquée, la propriété V = r + γPV et la borne γᵏ‖V₀ − V‖∞ ; "
                 "jamais une autre fonction de l'apprenant ; les tests de γ = 1 restent sur des cas bien "
                 "conditionnés, cond(I − P) ≤ 10⁸, et un P ou un μ₀ non fini est refusé). `bellman_linear_solve` "
                 "est l'oracle des tests de "
                 "`value_iteration` dans workbookIA 26, avec un contrat distinct : la matrice m × m de la politique fixée "
                 "(pas le dictionnaire de Gymnasium), un vecteur de récompenses, V seul (ni Q, ni max, ni actions). "
                 "`bellman_fixed_point_iterates` est calqué sur `richardson_iterates` (M19) : sans max, sans seuil "
                 "d'arrêt ni nombre maximal d'itérations, il ne remplace pas `value_iteration` (🔨 26.26) ; il "
                 "calculerait les itérés de ✏️ 26.6 et de 26.Q10 sur leur chaîne, donc il ne sert à aucun exercice "
                 "de M26 sur une chaîne qui avance d'un état par pas avec une seule récompense finale (26.6, 26.Q10, "
                 "Évités). Aucune fonction "
                 "de retour actualisé, de politique, de mise à jour, d'arrêt optimal ni de simulation. `markov_bound` "
                 "(M11) est l'inégalité de Markov : la docstring du module le signale. "
                 "Évités (règle de partage) : la chaîne 0 → 1 → 2 → 3 à récompense finale 1 avec γ = 0,9 (valeurs 1, 0,9 "
                 "et 0,81), ses variantes (10 états ; γ = 0,5 → 0,25 ; α = 0,5 → 0,225 et 0,875) ; la chaîne P_26 de "
                 "26.26 (0 → 1 → 2, récompense 1 au dernier pas, l'action 1 ramène en 0, γ = 0,5, V* = (0,5 ; 1 ; 0), "
                 "Q* = [[0,5 ; 0,25] ; [1 ; 0,25] ; [0 ; 0]]) ; le MDP A, B, T de ∂ 26.8 (rester, aller, finir, jouer ; "
                 "récompenses 0, 0, 1 et 2 ; probabilité ½ ; γ = 0,9 ; 400/119, 360/119, 324/119, 0,595, 0,405 ; "
                 "échantillons 2 ou 4,72, moyenne 3,36 ; variante 0,5 → 0,9, 0,81 et 0,905) ; l'exemple de "
                 "`value_iteration` (rester 0 ou finir 1, γ = 0,9 → V = (1 ; 0), Q = [[0,9 ; 1] ; [0 ; 0]]) ; les "
                 "récompenses (0, 0, 1), (2, 0, 1), (1, 0, 0, 2, 0, 4), (0, 3, 0, 1), (1, 1, 1, 1), (1, 0, 2) et "
                 "(1, 1, 1) et leurs retours (0,81, 2,25, 1,375, 4,820, 5,24, 1,625, 1,875, 1,75, 1,5) ; REWARDS_15 "
                 "(graine 2615) et ses retours 0,80 à 8,06 ; γ = 0,2, 0,5, 0,9, 0,95 et 0,99, les horizons 2, 10, 20 et "
                 "100, les demi-vies 6,58, 7, 13,5, 14, 68,97 et 69, 0,2³, 0,2⁴, 0,2⁵, 0,2⁶ et 1/(1 − 0,2) = 1,25 ; les "
                 "lignes Q (0,1 ; 0,6 ; 0,3 ; 0,6), (1, 2, 4, 0), (1 ; 2 ; 4 ; 0,5) et [[0,2 ; 0,4] ; [1 ; 0,6] ; "
                 "[0 ; 0]], r = 0,2 et Q = 0,5 (0,74, 0,24, 0,62, 0,35, 0,47, 0,485), Q = 0,4, r = 0,1, γ = 0,8 et "
                 "max 0,5 (cible 0,5, δ = 0,1, 0,45), r = 0,5 et γ = 0,8 (1,3, 0,9, 0,85), Q = 0,4, max 0,8 → 0,6, le "
                 "bandit 3, 5 et 0,25 → 3,5 ; ε = 0,2 avec 4 actions (0,85, 0,05, 0,80, 0,067), ε = 0,1 avec 5 actions "
                 "(0,92), les températures 1, 2, 0,5 et 0,8 (0,831, 0,579, 0,979, 0,571) ; FrozenLake (16 états, "
                 "V*(0) = 0,54 et 0,069, 73,2 % et 74,9 %), Flippers et son camion, le L-learning, CliffWalking, le "
                 "morpion, CartPole, le go, AlphaGo, le backgammon, les robots, les ascenseurs, les cultures, le "
                 "cuisinier et son minuteur, le compte en banque de la fiche de workbookIA 26 ; 2⁹, 3⁹, 3¹⁶, 3³⁶¹, 5 478, "
                 "255 168, 3²⁵ et les mémoires de 🧮 26.9 (4 octets, 16 Go, 2,8 Go, 85 To, 10⁹ mises à jour par seconde, "
                 "25 → 256 → 256 → 25 et 78 873 paramètres) ; le DQN de Mnih (84 × 84, 18 actions, 10 000 pas, un "
                 "million, 32, ε de 1 à 0,1) ; le paradoxe des anniversaires (32 parmi 1 000, 0,39) ; les cinq graines "
                 "(57, 35, 74, 74 et 38 %, [41,2 ; 70,6]). Évités aussi (reprises de ce dépôt) : les exemples des "
                 "docstrings de `markov` ([[0,5 ; 0,5 ; 0] ; [0,25 ; 0,5 ; 0,25] ; [0 ; 0,5 ; 0,5]], "
                 "[[0,6 ; 0,4] ; [0,2 ; 0,8]], [[0,5 ; 0,5] ; [0 ; 1]] avec r = (1, 2) et γ = 0,75, "
                 "[[0,5 ; 0,25] ; [0,5 ; 0]]), la contraction de ∂ M22.14 (A = [[0,3 ; −0,3] ; [0,1 ; 0,3]], "
                 "c = (1, 2)), les polluants du lac et la plante de M22, la barre qui tiédit et les deux ressorts de M19, "
                 "les matrices de M12c §4 et §5, la population à pile ou face de M22 §5. "
                 "Pas de MML (le livre ne traite pas les chaînes de Markov), donc pas de 📖 ; références libres : "
                 "Blitzstein et Hwang, ch. 11 (chaînes de Markov) ; pour Bellman, Sutton et Barto (2ᵉ éd.), §3.5-3.6 et "
                 "§4.1-4.4, cités par sections. 14,6 h au lieu des 12 h prévues : la propriété de la tour et "
                 "l'analyse au premier pas, le cas d'une fin possible (γ = 1 quand la fin est sûre), l'arrêt optimal, "
                 "l'erreur TD et le biais du maximum, que workbookIA 26 suppose ou que MB8 rappellera ; la loi "
                 "stationnaire reste courte, Banach et la convergence d'une chaîne irréductible apériodique sont "
                 "énoncés.",
        "exercises": [
            ("M26.Q1", "🧠", 1, 4, "Matrice stochastique, convention ligne, loi à n pas et chemins du graphe : vrai ou faux",
             "§1", "E"),
            ("M26.Q2", "🧠", 1, 4, "Une loi stationnaire existe-t-elle, est-elle unique, la loi de la chaîne y "
             "converge-t-elle ? Chaînes périodiques et à deux classes", "§2", "E"),
            ("M26.Q3", "🧠", 1, 4, "Espérance conditionnelle, propriété de la tour et analyse au premier pas : quelle "
             "équation pour quel nombre ?", "§3", "E"),
            ("M26.Q4", "🧠", 1, 4, "Le facteur γ : une actualisation, ou une probabilité de continuer ? Valeur d'un état "
             "et politique", "§4", "E"),
            ("M26.Q5", "🧠", 1, 4, "Le système de Bellman d'une politique fixée : quelles matrices, pourquoi il est "
             "inversible, quand γ = 1 est permis", "§5", "E"),
            ("M26.Q6", "🧠", 1, 4, "Contraction, bornes a priori et a posteriori, itérations synchrones ou en place : vrai "
             "ou faux", "§6", "E"),
            ("M26.Q7", "🧠", 1, 4, "Un maximum dans l'opérateur : ce qui reste (contraction, point fixe unique), ce qui "
             "se perd (le système linéaire)", "§7", "E"),
            ("M26.Q8", "🧠", 1, 4, "Des échantillons au lieu de P : moyenne de retours, pas 1/n ou constant, erreur TD, "
             "biais du maximum", "§8", "E"),
            ("M26.R1", "🔁", 1, 5, "Puissances d'une matrice diagonalisable et méthode de la puissance (M12c)", "§1 §2",
             "E"),
            ("M26.R2", "🔁", 1, 8, "La norme ‖·‖∞ d'une matrice, ρ(A) ≤ ‖A‖ et Aᵗ → 0 quand ρ(A) < 1 (M22), et la "
             "somme d'une série géométrique (R5)",
             "§5 §6", "E"),
            ("M26.R3", "🔁", 1, 5, "Probabilités totales et espérance d'une loi géométrique (M03, M02b)", "§3 §4", "E"),
            ("M26.1", "✏️", 1, 25, "Des vélos en libre-service entre trois stations : matrice de transition, graphe, loi "
             "après deux et trois jours, et coût moyen du lendemain (Pf)", "§1 §3", "E"),
            ("M26.2", "✏️", 2, 25, "Trois opérateurs et leurs parts de marché : la loi stationnaire par un système "
             "linéaire, puis vérifier πP = π", "§2", "E"),
            ("M26.3", "✏️", 2, 25, "Trois chaînes qui posent problème, périodique, à deux classes et avec un état "
             "transitoire : lois stationnaires et comportement de Pⁿ", "§2", ""),
            ("M26.4", "✏️", 2, 30, "Un cursus en trois années, avec redoublement et abandon : la probabilité d'être "
             "diplômé et la durée moyenne des études, par l'analyse au premier pas", "§3", "E"),
            ("M26.5", "✏️", 1, 20, "Un abonné qui peut résilier chaque mois : durée géométrique, revenu total moyen, et "
             "le même nombre comme revenu actualisé", "§4", "E"),
            ("M26.6", "✏️", 2, 35, "Une machine qui s'use, deux politiques d'entretien : P_π et r_π, deux systèmes de "
             "Bellman 3 × 3, et la valeur d'une action", "§4 §5", "E"),
            ("M26.7", "✏️", 2, 30, "Les itérés de Bellman de la machine de M26.6 : trois pas synchrones puis en place, "
             "comparés à la solution, et le nombre d'itérations qui garantit 10⁻³", "§6", "E p:M26.6"),
            ("M26.8", "✏️", 2, 30, "Vendre une voiture d'occasion : offres au hasard, coût d'attente, valeur de "
             "continuation et règle à seuil", "§7", "E"),
            ("M26.9", "✏️", 2, 25, "Le meilleur de deux fournisseurs sur des mesures bruitées : le maximum surestime, "
             "l'estimateur double non", "§8", ""),
            ("M26.10", "∂", 2, 25, "L'analyse au premier pas démontrée : t = 1 + Qt et h = Qh + b, et I − Q inversible "
             "dès que la fin est possible depuis chaque état", "§3", ""),
            ("M26.11", "∂", 2, 25, "V = Σ γᵗPᵗr est l'unique solution du système de Bellman : I − γP inversible, série "
             "de Neumann démontrée pour γP, et (1 − γ)(I − γP)⁻¹ stochastique", "§4 §5", "E"),
            ("M26.12", "∂", 2, 25, "L'opérateur de Bellman d'une politique fixée est une γ-contraction pour ‖·‖∞ ; "
             "bornes a priori et a posteriori ; le maximum est 1-lipschitzien", "§6 §7", "E"),
            ("M26.13", "∂", 2, 20, "L'erreur TD se télescope : Σ γᵏ δ_{t+k} = G_t − V(S_t) ; une récompense ajoutée "
             "γΦ(s′) − Φ(s) décale chaque valeur de −Φ(s)", "§8", ""),
            ("M26.14", "🔗", 2, 25, "Pont : d'une politique stochastique à la chaîne qu'elle induit, P_π = Σ_a π(a | s) "
             "P_a et r_π avec des tableaux à trois axes (actions, états, états), puis Q^π(s, a) et r(s, a, s′)",
             "§4 §5", "E"),
            ("M26.15", "🗣️", 1, 10, "Expliquer avec une image hors informatique pourquoi une chaîne qui mélange oublie "
             "son état de départ", "§2", "E"),
            ("M26.E1", "💼", 1, 10, "« Pourquoi I − γP est-elle inversible quand P est stochastique et γ < 1, et que "
             "se passe-t-il pour γ = 1 ? »", "§5", ""),
            ("M26.16", "🔨", 1, 20, "La loi d'une chaîne après n pas, en convention ligne", "§1",
             "E m:n_step_distribution"),
            ("M26.17", "🔨", 2, 25, "La loi stationnaire par un système linéaire, et le refus d'une chaîne qui en a "
             "plusieurs", "§2", "E m:stationary_distribution"),
            ("M26.18", "🔨", 2, 25, "Le système de Bellman d'une politique fixée, avec une fin possible (matrice "
             "sous-stochastique) et γ = 1 quand la fin est sûre", "§5", "E m:bellman_linear_solve"),
            ("M26.19", "🔨", 1, 20, "Les itérés de l'opérateur de Bellman d'une politique fixée (Richardson de pas 1)",
             "§6", "E m:bellman_fixed_point_iterates"),
            ("M26.20", "📦", 1, 20, "La loi stationnaire de trois façons, `np.linalg.eig` sur Pᵀ, "
             "`scipy.linalg.null_space` et la méthode de la puissance, sur le surfeur aléatoire d'un web de six pages",
             "§2", ""),
            ("M26.21", "🔮", 1, 15, "Prédire la somme des lignes de (1 − γ)(I − γP)⁻¹, puis leur limite quand γ tend "
             "vers 1, et vérifier", "§2 §5", "E p:M26.17,M26.18"),
            ("M26.22", "🔬", 2, 20, "Le biais du maximum par simulation : k fournisseurs de même qualité, n mesures "
             "chacun, le meilleur mesuré contre l'estimateur double", "§8", ""),
            ("M26.23", "🎨", 1, 15, "La loi d'une chaîne au fil des pas depuis trois départs, et ‖μ_n − π‖₁ en échelle "
             "logarithmique contre |λ₂|ⁿ", "§1 §2", "p:M26.16,M26.17"),
            ("M26.24", "🐛", 1, 25, "Chasse à l'erreur : une matrice lue dans la mauvaise convention, une loi "
             "stationnaire non normalisée, un état final qui rapporte encore, γ = 1 sans fin", "§1 §2 §5", "E"),
            ("M26.25", "🛠️", 1, 20, "Un test de propriété : πP = π, et pour `bellman_fixed_point_iterates`, V_k − V tenu "
             "par γᵏ‖V₀ − V‖∞ et V = r + γPV pour la limite, sur des chaînes tirées au hasard", "§2 §6",
             "p:M26.17,M26.18,M26.19"),
            ("M26.26", "🏆", 3, 30, "Défi : estimer la valeur d'un état à 0,01 près en simulant l'arrêt géométrique "
             "(continuer avec la probabilité γ) et en sommant les récompenses sans actualisation, sous un budget de "
             "pas simulés", "§4 §8", "p:M26.18"),
        ],
    },
    {
        "id": "M27", "dir": "m27_jeux_distances", "hours": 14.4, "generation_sessions": 1, "mml": ["§7.2"],
        "summary": "Les jeux à deux joueurs et les distances entre lois. D'abord les jeux à somme nulle : la matrice des "
                   "gains, le maximin et le minimax (l'inégalité minimax de MML §7.2), les points selles et les "
                   "stratégies dominées ; les stratégies mixtes, la stratégie d'indifférence d'un jeu 2 × 2 et le "
                   "théorème minimax de von Neumann ; l'équilibre de Nash d'un jeu quelconque et l'induction arrière sur "
                   "un arbre de jeu ; la descente-montée de gradient sur un jeu bilinéaire, qui tourne autour de "
                   "l'équilibre ou s'en éloigne. Puis les lois : la probabilité a posteriori est le meilleur prédicteur "
                   "pour la log-loss ; la divergence de Jensen-Shannon plafonne à ln 2 quand les supports se séparent ; "
                   "les couplages et les distances de Wasserstein, calculées en dimension 1 par les fonctions de "
                   "répartition et les quantiles, dont W₂ de deux gaussiennes ; la distance de Fréchet entre gaussiennes "
                   "et le biais d'une distance estimée sur des échantillons ; enfin trois mesures d'une dérive (PSI, "
                   "Kolmogorov-Smirnov, W₁). workbookIA 27 applique ces outils aux GAN, et workbookIA B7 à la "
                   "surveillance d'un modèle en production.",
        "objectives": [
            "Trouver le maximin, le minimax et les points selles d'une matrice de gains, et réduire un jeu par "
            "dominance.",
            "Calculer les stratégies optimales et la valeur d'un jeu 2 × 2 par indifférence, et énoncer le théorème "
            "minimax de von Neumann.",
            "Trouver les équilibres de Nash d'un jeu à deux joueurs, et la valeur d'un arbre de jeu par induction "
            "arrière.",
            "Prévoir, par les valeurs propres d'un pas, si la descente-montée tourne autour d'un équilibre ou s'en "
            "éloigne.",
            "Calculer la probabilité a posteriori qui minimise la log-loss espérée, et démontrer qu'elle la minimise.",
            "Calculer la divergence de Jensen-Shannon de deux lois, et expliquer pourquoi elle plafonne à ln 2.",
            "Écrire un couplage de deux lois discrètes, calculer son coût, et trouver le plan optimal sur la droite.",
            "Calculer W₁ et W₂ en dimension 1 par les fonctions de répartition ou par les quantiles, dont W₂ de deux "
            "gaussiennes.",
            "Calculer la distance de Fréchet de deux gaussiennes dans un cas commutatif, et le biais d'une distance "
            "estimée sur des échantillons.",
            "Mesurer une dérive par le PSI, la statistique de Kolmogorov-Smirnov et W₁, et dire ce que chacune mesure.",
        ],
        "sections": [("§1", "Jeux à somme nulle : matrice des gains, maximin et minimax, point selle, stratégies dominées"),
                     ("§2", "Stratégies mixtes : gain espéré, indifférence et théorème minimax de von Neumann"),
                     ("§3", "Équilibre de Nash, jeux à somme non nulle, et arbres de jeu (induction arrière)"),
                     ("§4", "Jouer par gradients : descente-montée simultanée ou alternée sur un jeu bilinéaire"),
                     ("§5", "Le meilleur prédicteur pour la log-loss : la probabilité a posteriori"),
                     ("§6", "Jensen-Shannon revisitée : bornée par ln 2, aveugle quand les supports se séparent"),
                     ("§7", "Transporter une loi sur une autre : couplages, plans de transport et distances de "
                            "Wasserstein"),
                     ("§8", "Wasserstein en dimension 1 : fonctions de répartition, quantiles, appariement trié, deux "
                            "gaussiennes"),
                     ("§9", "La distance de Fréchet entre gaussiennes, et le biais d'une distance estimée"),
                     ("§10", "Mesurer une dérive : PSI, Kolmogorov-Smirnov et W₁")],
        "teaches": ["jeu à deux joueurs à somme nulle : matrice des gains, maximin et minimax en stratégies pures, "
                    "maximin ≤ minimax (l'inégalité minimax, MML §7.2), point selle, stratégies dominées",
                    "l'ordre compte : le joueur qui annonce son coup en second a l'avantage ; la dualité faible lue "
                    "comme un jeu",
                    "stratégies mixtes : gain espéré pᵀGq, stratégie d'indifférence d'un jeu 2 × 2 (démontrée optimale), "
                    "valeur d'un jeu",
                    "théorème minimax de von Neumann (énoncé) ; un jeu fini est un programme linéaire (énoncé)",
                    "équilibre de Nash : définition générale, jeux à somme non nulle (dilemme du prisonnier, "
                    "coordination), équilibres multiples, purs et mixtes ; dans un jeu à somme nulle, un couple de "
                    "stratégies optimales",
                    "arbres de jeu : induction arrière, minimax d'un arbre",
                    "dynamique de gradients sur un jeu : descente-montée simultanée (une spirale qui s'éloigne) et "
                    "alternée (une courbe fermée, une ellipse : x² + y² − ηxy reste constant sur xy) sur un jeu "
                    "bilinéaire ; l'équilibre est un point selle de f",
                    "meilleur prédicteur pour la log-loss : la probabilité a posteriori "
                    "P(Y = 1 | x) = π₁p₁(x)/(π₁p₁(x) + π₀p₀(x)) (Bayes, priors quelconques) ; le maximum de "
                    "vraisemblance k ln p + (n − k) ln(1 − p) d'une loi de Bernoulli rappelé (M04.12, M13a.1), avec "
                    "des comptes entiers",
                    "divergence de Jensen-Shannon revisitée : 0 ≤ JS ≤ ln 2, JS = ln 2 pour des supports disjoints, "
                    "constante (sans pente) quand les supports se séparent ; la KL y est infinie",
                    "couplages et plans de transport sur des supports finis (marges imposées, couplage indépendant), coût "
                    "d'un plan, distances de Wasserstein W_p ; le transport optimal est un programme linéaire",
                    "W₁ ≤ W₂ (Jensen sur un même couplage) ; dualité de Kantorovich-Rubinstein : W₁ comme un maximum sur "
                    "les fonctions 1-lipschitziennes (énoncée)",
                    "W_p en dimension 1 : W₁ = ∫|F − G|, W_p^p = ∫₀¹|F⁻¹(u) − G⁻¹(u)|^p du (le couplage des quantiles, "
                    "optimal) ; appariement trié optimal (argument d'échange)",
                    "W₂ de deux gaussiennes en dimension 1 : W₂² = (μ₁ − μ₂)² + (σ₁ − σ₂)² ; W_p d'une translation",
                    "distance de Fréchet (W₂) entre gaussiennes : formule (admise en général), "
                    "Tr((Σ₁Σ₂)^{1/2}) = Σ√λᵢ(Σ₁Σ₂), Σ₁Σ₂ semblable à Σ₁^{1/2}Σ₂Σ₁^{1/2} (Σ₁ définie positive) ; "
                    "cas commutatif démontré "
                    "(une somme de W₂² en dimension 1) ; invariance par une rotation commune",
                    "biais d'une distance estimée : E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ ; comparer à "
                    "tailles égales",
                    "mesurer une dérive : PSI = KL(p ‖ q) + KL(q ‖ p) (divergence de Jeffreys) sur des classes, et "
                    "J = Σ(p_k − q_k) ln(p_k/q_k) ≈ Σ(p_k − q_k)²/q_k pour un petit décalage ; "
                    "statistique de Kolmogorov-Smirnov sup|F − G|, W₁ = ∫|F − G| ; unités, invariances, "
                    "W₁ ≤ (b − a)·KS sur [a, b]"],
        "requires": [("intégrales, changement de variable, fonction de répartition et quantile "
                      "F⁻¹(u) = inf{x : F(x) ≥ u}", "M02a"),
                     ("espérance d'une variable discrète, indépendance, fonction de répartition, loi normale et Φ, "
                      "simulation par inversion F⁻¹(U)", "M02b"),
                     ("biais d'un estimateur, variance d'une moyenne, matrice de covariance", "M02c"),
                     ("formule de Bayes, a priori et a posteriori ; le maximum de vraisemblance d'une loi de Bernoulli "
                      "est la fréquence", "M04"),
                     ("point selle d'une fonction de deux variables, descente et montée de gradient", "M05b"),
                     ("divergence KL, inégalités de Jensen et de Gibbs, divergence de Jensen-Shannon", "M06"),
                     ("p-valeur d'un test", "M08"),
                     ("programmes linéaires", "M10"),
                     ("trace, matrices semblables, théorème spectral, racine carrée d'une matrice symétrique positive",
                      "M12c"),
                     ("log-loss, la log-loss quand la probabilité prédite tend vers 0", "M13a"),
                     ("lagrangien et dualité faible, MML §7.2 lu une première fois", "M13b"),
                     ("valeurs propres complexes d'une matrice 2 × 2, module, rotations et homothéties, puissances",
                      "M22"),
                     ("KL entre deux lois continues, KL infinie quand le support de q ne couvre pas celui de p", "M25a")],
        "frontieres": ["27.2", "27.3", "27.4", "27.7", "27.10", "27.11", "27.13", "27.14", "27.18", "27.22", "27.23",
                       "27.Q5", "27.E1", "27.E4", "27.E5", "B7.4", "B7.22", "B7.Q11", "B7.E4"],
        "mymath": {"module": "distances.py",
                   "functions": ["pure_strategy_values", "mixed_strategy_value_2x2", "descent_ascent_iterates",
                                 "w2_gaussians_1d"]},
        "reading_minutes": 150,
        "flashcards": 20,
        "notes": "Frontières : les ∂ 27.5 (D* = p_data/(p_data + p_g) par le maximum de a ln y + b ln(1 − y), dérivée "
                 "nulle puis dérivée seconde, l'intégrale maximisée point par point, V(D*, G) = −ln 4 + 2 JS, son minimum "
                 "en p_g = p_data) et 27.6 (les dérivées −D et −(1 − D) de ln(1 − σ(a)) et de −ln σ(a), D = 0,01 et le "
                 "rapport 99, la BCE avec logits ln(1 + e^{−a})), ✏️ 27.2 (maximin, minimax et point selle d'une "
                 "matrice 3 × 3 ; « min_G max_D ou max_D min_G »), ✏️ 27.3 et 27.4 (les losses BCE d'un mini-batch, "
                 "ln 2 et 2 ln 2 à l'équilibre, 0,607), 🧮 27.7, 📄 27.10 (Goodfellow et coll. 2014, −log 4), 🔨 27.11 "
                 "(`wasserstein_1d`), 🔨 27.22 et 📦 27.23 (`frechet_distance`, le FID et sa dépendance au nombre "
                 "d'images), la dynamique d'un GAN (🔮 27.13, 📈 27.14, 🔬 27.18, 💼 27.E5), 27.Q5 (somme nulle, "
                 "poker, Nash, D = 0,5 à l'équilibre), 💼 27.E1 et 27.E4 ; et, de workbookIA B7, qui n'a pas de chapitre "
                 "de maths et que le §10 prépare, ✏️ B7.4 (un PSI à la main sur quatre intervalles, l'intervalle vide "
                 "et ε, les seuils), 📈 B7.22, B7.Q11 et 💼 B7.E4. M27 enseigne les outils hors réseau : un marché que "
                 "deux enseignes se partagent, des tirs au but, une partie de cache-cache, le dilemme du prisonnier, un "
                 "jeu de coordination, un jeu d'allumettes, des dépôts et des magasins, des fournisseurs, des séries de "
                 "production, des relevés de capteurs ; jamais un générateur, un discriminateur, un faux, une loss de "
                 "GAN ni un learning rate. « GAN : générateur et discriminateur, le jeu mathématique » est retiré des "
                 "notions du plan : M27 n'écrit ni V(D, G) ni min_G max_D. Le maximum de vraisemblance "
                 "k ln p + (n − k) ln(1 − p) d'une loi de Bernoulli, avec des comptes entiers (∂ M04.12, M13a.1), et "
                 "la log-loss quand la probabilité prédite tend vers 0 (M13a.4) ne sont que des rappels (🔁 M27.R1, "
                 "sur d'autres nombres) ; M27.R1 ne compare jamais −ln p et ln(1 − p) ni leurs dérivées en un même "
                 "point (∂ 27.6) ; le §5 enseigne l'énoncé plus général « la probabilité a posteriori "
                 "P(Y = 1 | x) = π₁p₁(x)/(π₁p₁(x) + π₀p₀(x)) minimise la log-loss espérée », démontré par l'inégalité "
                 "de Gibbs (∂ M27.12) et non par f′ et f″, avec des priors inégaux et des lois d'un autre domaine "
                 "(fournisseurs et défauts, ✏️ M27.5) : aucun exercice ne prend des priors égaux, n'appelle ce "
                 "prédicteur un discriminateur, ne maximise une intégrale de deux densités point par point, ne calcule "
                 "la valeur du minimum en formule (l'entropie conditionnelle H(Y | X)) ni ne la relie à "
                 "Jensen-Shannon (c'est le cœur de ∂ 27.5.4) ; M27.5 en donne seulement des valeurs numériques, et "
                 "M27.Q4 ne demande ni la valeur ½ où π₁p₁ = π₀p₀, ni la limite 1 quand p₀(x) → 0 (∂ 27.5.3). La "
                 "saturation (∂ 27.6) n'est pas reprise : ni ln(1 − σ(a)) contre −ln σ(a), ni le facteur σ(1 − σ) "
                 "comparé à σ − y (le ∂ 18.8.4 de workbookIA l'a déjà fait), ni « même minimiseur, gradients "
                 "différents » en exercice. Les jeux : ✏️ M27.1 prend d'autres matrices que 27.2 et la fiche 27, sans "
                 "les noms « Ligne » et « Colonne », et une matrice avec point selle (réduite par dominance) : aucune "
                 "3 × 3 sans point selle ne fait chercher maximin et minimax (27.2) ; au-delà de 27.2, M27 enseigne les stratégies mixtes (l'indifférence "
                 "d'un 2 × 2, démontrée optimale dans la fiche ; la valeur), le théorème minimax de von Neumann (énoncé) "
                 "et le lien avec la programmation linéaire (énoncé, MML §7.3.1 en option) ; l'avantage de jouer en "
                 "second est enseigné sur des jeux hors réseau (Q1), jamais sur min_G max_D ; Nash sur un dilemme du "
                 "prisonnier et un jeu de coordination (équilibres purs et mixte), pas sur le poker ni par les questions "
                 "de 27.Q5 ; l'arbre sur un jeu d'allumettes, pas sur le morpion (fiche 26, 🔬 26.37, 27.R1). La "
                 "dynamique (§4) porte sur le jeu bilinéaire f(x, y) = xᵀAy et sur xy : pas simultané (des valeurs "
                 "propres de module > 1) contre alterné (de déterminant 1), et deux pas différents pour x et y (des pas "
                 "inégaux ne suffisent pas) ; ni GAN, ni loss, ni les learning rates de "
                 "27.14 (10⁻⁴, 10⁻³, 10⁻²), ni TTUR nommé ; M27.4 évite η = 0,25 et η = 0,5 (ηa = 0,5, l'exemple du "
                 "stub). "
                 "Jensen-Shannon (§6) : 0 ≤ JS ≤ ln 2 (∂ M27.13), JS = ln 2 pour des supports disjoints, sur deux lois "
                 "uniformes de même largeur translatées l'une de l'autre (✏️ M27.6) ; ni D*, ni −ln 4. Wasserstein (§7, §8) : couplages et plans de transport sur des supports "
                 "finis, W_p, le programme linéaire (📦 M27.23), la dualité de Kantorovich-Rubinstein énoncée ; en "
                 "dimension 1, W₁ = ∫|F − G| et W_p par les quantiles (le couplage des quantiles est optimal : démontré "
                 "pour deux échantillons de même taille par un argument d'échange, ∂ M27.14, admis en général), W₂ de "
                 "deux gaussiennes, W_p d'une translation ; l'optimalité de l'appariement trié, que 27.11 admet, est donc "
                 "démontrée, mais aucun exercice ni aucune fonction ne calcule W₁ entre deux échantillons de tailles "
                 "différentes (le cœur de 27.11) ; W₁ entre deux petits échantillons de même taille, à la main, "
                 "seulement au §10 (M27.10) ; W₁ de deux gaussiennes d'écarts-types différents n'est pas calculé "
                 "(E|a + bZ|, la variante de 27.11). Fréchet (§9) : la formule, admise en général, "
                 "Tr((Σ₁Σ₂)^{1/2}) = Σ√λᵢ, Σ₁Σ₂ semblable à Σ₁^{1/2}Σ₂Σ₁^{1/2} pour Σ₁ définie positive (démontré "
                 "dans la fiche, en trois "
                 "lignes), le cas commutatif démontré (une somme de W₂² en dimension 1, invariante par une rotation "
                 "commune ; ✏️ M27.9 sur des covariances diagonales du plan) ; aucun code ne calcule une distance de "
                 "Fréchet avec `scipy.linalg.sqrtm` ni à partir de features (le contrat et l'oracle de 27.22) ; le "
                 "biais d'une distance estimée porte sur les moyennes (∂ M27.15, 🔬 M27.25 : deux séries d'une même "
                 "machine), sans FID, Inception, nombre d'images ni la suite 123,2 → 119,3 de 27.23 ; le 🔗 M27.16 "
                 "porte sur une convention (la distance de Fréchet en dimension 1, que workbookIA 27 écrit avec des "
                 "covariances et rend au carré), jamais sur des résumés relevés epoch par epoch (🔮 27.13, 📈 27.14). "
                 "Dérive (§10, pour "
                 "workbookIA B7 ; workbookIA 29 mesure le décalage par la performance d'un modèle, sans distance entre "
                 "lois, et sa couverture passe à M02c et M03) : PSI = KL(p ‖ q) + KL(q ‖ p) (la divergence de Jeffreys) "
                 "sur une variable à trois catégories (M27.10), sans quantiles de la référence, sans intervalle vide ni "
                 "ε, sans seuils 0,1 et 0,25, ni contribution d'une catégorie, ni vérification de PSI = KL + KL en "
                 "exercice (B7.4 : l'identité reste dans la fiche) ; M27.10 en tire l'approximation "
                 "Σ(p_k − q_k)²/q_k d'un petit décalage, que B7 n'a pas ; KS = sup|F − G| comme statistique, sa p-valeur seulement nommée "
                 "(M08), sans « tout devient significatif sur de grands échantillons » (B7.Q11 c et la fiche B7) ; "
                 "W₁ = ∫|F − G|, ses unités, W₁ ≤ (b − a)·KS ; ni images, ni luminosité, ni sorties softmax. Évités "
                 "(règle de partage) : les matrices [[3, −1, 2], [1, 0, 4], [−2, 5, −3]] (maximin 0, minimax 3, maxima "
                 "des colonnes 3, 5 et 4) et [[2, 4], [1, 0]] (point selle 2), les territoires 5, 10 et 20 ; Glenn et "
                 "Dawn, les faux billets, le faux vin, le poker ; les sorties D = 0,9 ; 0,7 ; 0,8 ; 0,6 ; 0,3 ; 0,1 ; "
                 "0,2 et 0,4, D = 0,01 et le rapport 99, D = 0,9 et le rapport 9, D = 0,5 ; ln 2, 2 ln 2 ≈ 1,386, −ln 4 "
                 "et 0,607 présentés comme valeurs d'un jeu ou d'une loss ; 𝒰[0, 1] contre 𝒰[0, 2] (2/3), les mélanges "
                 "0,6 𝒩(1,5 ; 0,8) + 0,4 𝒩(−1,5 ; 0,6) et 𝒩(0,3 ; 1,6) de la figure du D*, p_data = 0,3 et p_g = 0,1 "
                 "(0,75, CP6.4 de workbookIA) ; les échantillons (4, 1) et (2, 2) (W₁ = 1,5), [3, 1, 2] et [2, 6, 4] "
                 "(2,0), [5, −1, 2,5] et ses permutations, [0, 2] et [1] (1,0), [0, 1, 3] et [5, 6, 8] (5,0), [0, 1] et "
                 "[0, 1, 2] (0,5), (0,4 ; 1,1 ; 1,7 ; 2,9) et (1,0 ; 2,2 ; 3,1 ; 3,6), 50 normales décalées de 0,5 ; "
                 "les lois 𝒩(4 ; 1,25²), 𝒩(5 ; 1,25²), 𝒩(4 ; 2,5²), le Dirac en 4 et 1,25√(2/π), 𝒩(0, 1) contre 0 et "
                 "√(2/π) ≈ 0,80, 𝒩(0 ; 4) contre 𝒩(1 ; 1) (W₂² = 2 : aucune paire de gaussiennes avec "
                 "(Δμ, Δσ) = (1, 1)) ; les covariances diag(9, 1) et I (4), diag(1, 4) et diag(4, 1) (2), diag(4, 9) et I "
                 "avec les moyennes (1, 2) (5), les moyennes (0, 0) et (3, 4) (25), les décalages de 1 et de 2 sur "
                 "chaque axe d'un nuage de ℝ³ (3 et 12), les moyennes 0 et (1, 1, 1) (3) ; les résumés (moyenne, "
                 "écart-type) des 📦 27.12, 🔮 27.13 et 📈 27.14 (4,03 et 0,98 ; 5,61 à 5,64 ; 4,50 et 0,95 ; 5,72 et "
                 "0,33 ; 3,94 et 0,73 ; 2,21 et 0,90), un modèle effondré sur un point ; la gaussienne du plan de "
                 "centre (5, 5) et 39,3 %, l'anneau de 8 gaussiennes de rayon 2, la somme 16(4⁹ − 1)/3 et 75 % ; les "
                 "distances de Fréchet 3,4 ; 119,3 à 123,2 ; 745 ; 638 ; 91 ; 1,7 ; 15,1 et 15,3 ; 50 000 images et "
                 "2 048 features ; MNIST, Fashion-MNIST, Inception, DINOv2 ; de workbookIA B7, la luminosité moyenne "
                 "d'images, les parts 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 contre 0,2 (PSI 0,135, KL 0,0650 et 0,0704), les "
                 "quartiles et les comptes 38/52/54/56, 96/62/30/12 et 120/56/24/0 sur 200 images, ε = 10⁻⁴ et 10⁻³, "
                 "les seuils 0,1 et 0,25, les échantillons 0,31 ; 0,42 ; 0,47 ; 0,52 ; 0,58 et 0,22 ; 0,29 ; 0,35 ; "
                 "0,44 ; 0,61 (D = 0,4, p = 0,87), 10 000 valeurs décalées de 0,05 écart-type (D = 0,024, p = 0,008), "
                 "200 valeurs (D = 0,08, p = 0,55), 50 000 requêtes et p = 0,001, Bonferroni 0,05/m ; du checkpoint VI "
                 "de workbookIA, la dérivation de D* (CP6.4) et la courbe d'un GAN 1D (lr 10⁻² et 10⁻⁵, CP6.7). "
                 "Conventions : G[i, j] est le gain de la ligne (qui maximise) et ce que paie la colonne ; logarithme "
                 "népérien, JS en nats (M06 la calculait en bits : 1 bit = ln 2 nats, et JS ≤ 1 bit) ; W_p désigne la "
                 "distance et W_p^p le coût minimal ; F(x) = P(X ≤ x), F⁻¹(u) = inf{x : F(x) ≥ u} (M02a) ; "
                 "`w2_gaussians_1d` prend des écarts-types. `distances` : NumPy et `math` permis, rien de `np.linalg` "
                 "et aucune fonction de SciPy (`scipy.optimize.linprog` résout un jeu) ; `pure_strategy_values` (au "
                 "lieu de `minimax_value` du plan : une valeur seule ne dit pas le coup, et le minimax d'un arbre est "
                 "une autre chose) rend (maximin, minimax, ligne, colonne), les plus petits indices en cas d'égalité ; "
                 "`mixed_strategy_value_2x2` rend les stratégies pures de `pure_strategy_values` quand il y a un point "
                 "selle, sinon celles d'indifférence ; `descent_ascent_iterates` (ajoutée au plan : la brique du §4, "
                 "calquée sur `richardson_iterates` ; son premier joueur minimise, comme dans MML (7.23), et sa "
                 "docstring dit comment partir d'une matrice de gains G : A = −G, ou A = Gᵀ) ; `w2_gaussians_1d` prend des écarts-types et rend W₂, pas son "
                 "carré : un contrat distinct du cas 1D de `frechet_distance` de workbookIA 27 (des covariances, et le "
                 "carré d²) ; aucune fonction de W₁ empirique (27.11), de distance de Fréchet en dimension d (27.22), "
                 "de KL, de JS (`mylearn` 6), de PSI ni de KS (B7.22 les écrit ou les appelle). Les exercices ne "
                 "reprennent pas les exemples du stub ([[7, −4, 1], [−1, 5, 6]], [[1, 6, 2], [4, 5, 4], [0, 8, 3]], "
                 "[[4, −2], [−1, 3]], [[−1, 2], [5, 6]], A = [[2]] avec η = 0,25, (10 ; 1 ; 2 ; 16) et "
                 "(−1 ; 0,5 ; −1 ; 3,5)). MML : §7.2 relu (📖 M27.17 : l'inégalité minimax (7.23), sa preuve par "
                 "(7.24), la dualité faible (7.27) lue comme un jeu où le joueur des multiplicateurs annonce en second ; "
                 "M13b.21 l'a lu une première fois pour Lagrange) ; §7.3.1 (programmation linéaire) en option ; MML n'a "
                 "ni stratégie mixte, ni Nash, ni Wasserstein. Référence libre possible, à vérifier en génération avant "
                 "de la citer (annexes/ressources.md) : G. Peyré et M. Cuturi, Computational Optimal Transport, ch. 2 "
                 "et 3. 14,4 h au lieu des 10 h prévues : la décision commune ajoute au plan les stratégies mixtes et "
                 "von Neumann, les couplages et W_p, l'appariement trié, le biais d'une distance estimée, la dynamique "
                 "d'un jeu bilinéaire et le § de la dérive (B7) ; la composition est au bas des fourchettes du §13 "
                 "(15 ✏️/∂, 5 🔨/📦, un seul 🔬 et un seul 🔮) et les durées suivent les recalages de M21 et M22.",
        "exercises": [
            ("M27.Q1", "🧠", 1, 4, "Maximin, minimax et point selle : qui annonce son coup en premier, et qui y gagne ?",
             "§1", "E"),
            ("M27.Q2", "🧠", 1, 4, "Stratégies mixtes, gain espéré et valeur d'un jeu : vrai ou faux", "§2", "E"),
            ("M27.Q3", "🧠", 1, 4, "Équilibres de Nash, arbres de jeu et descente-montée : unique ou non, le meilleur pour "
             "tous ou non, converger ou tourner ?", "§3 §4", "E"),
            ("M27.Q4", "🧠", 1, 4, "La probabilité a posteriori et la log-loss ; Jensen-Shannon et KL quand les supports se "
             "séparent", "§5 §6", "E"),
            ("M27.Q5", "🧠", 1, 4, "Couplages et distances de Wasserstein : marges, translation, dilatation, et W₁ ≤ W₂",
             "§7 §8", "E"),
            ("M27.Q6", "🧠", 1, 4, "La distance de Fréchet et son estimation : rotation commune, covariances, taille des "
             "échantillons", "§9", "E"),
            ("M27.Q7", "🧠", 1, 4, "Mesurer une dérive : PSI, KS ou W₁, leurs unités, et ce que chacun ne voit pas", "§10",
             "E"),
            ("M27.R1", "🔁", 1, 8, "Le maximum de vraisemblance d'une loi de Bernoulli (des comptes entiers), et la log-loss "
             "quand la probabilité prédite tend vers 0 (M04, M13a)", "§5", "E"),
            ("M27.R2", "🔁", 1, 5, "Les valeurs propres complexes d'une matrice réelle 2 × 2, leur module et les puissances "
             "(M22)", "§4", "E"),
            ("M27.R3", "🔁", 1, 5, "La racine carrée d'une matrice symétrique positive, et la trace comme somme des valeurs "
             "propres (M12c)", "§9", "E"),
            ("M27.1", "✏️", 1, 20, "Deux enseignes se partagent un marché : réduire une matrice 3 × 4 par dominance, "
             "trouver ses deux points selles et vérifier qu'ils ont la même valeur, et ce que la réduction ne change "
             "pas (maximin, minimax)", "§1", "E"),
            ("M27.2", "✏️", 2, 20, "Tirs au but : la probabilité de tirer à gauche par indifférence, la réponse du gardien "
             "et la valeur du jeu", "§2", "E"),
            ("M27.3", "✏️", 2, 25, "Les équilibres de Nash d'un dilemme du prisonnier et d'un jeu de coordination (purs et "
             "mixte), puis la valeur d'un jeu d'allumettes par induction arrière", "§3", "E"),
            ("M27.4", "✏️", 2, 25, "Descente-montée sur f(x, y) = xy : la matrice d'un pas simultané puis alterné, leurs "
             "valeurs propres et leurs modules, et deux pas différents pour x et y", "§4", "E"),
            ("M27.5", "✏️", 2, 25, "Deux fournisseurs et un défaut noté sur quatre niveaux : la probabilité a posteriori, "
             "et la log-loss moyenne de trois prédicteurs (a priori, a posteriori, trop sûr de lui)", "§5", "E"),
            ("M27.6", "✏️", 2, 20, "Deux lois uniformes de même largeur, translatées : JS en fonction du décalage, la KL, "
             "et ce que le décalage lui-même mesure", "§6", "E"),
            ("M27.7", "✏️", 2, 25, "Trois dépôts et trois magasins le long d'une route : vérifier des couplages, leur "
             "coût, le couplage indépendant et le plan monotone (coin nord-ouest)", "§7", "E"),
            ("M27.8", "✏️", 2, 25, "W₁ et W₂ par l'aire entre les fonctions de répartition et par les quantiles : deux "
             "lois uniformes, puis W₂ de deux gaussiennes (et W₁ quand elles ont le même écart-type)", "§8", "E"),
            ("M27.9", "✏️", 2, 20, "La distance de Fréchet de deux gaussiennes du plan à covariances diagonales, puis "
             "tournées ensemble : la part des moyennes et celle des covariances", "§9", "E"),
            ("M27.10", "✏️", 2, 25, "Une dérive en deux mois d'une variable à trois catégories : la divergence de Jeffreys "
             "(le PSI) et JS, puis l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage ; enfin KS et W₁ entre "
             "deux petits échantillons de températures de même taille", "§10", "E"),
            ("M27.11", "∂", 2, 20, "Le maximin est au plus le minimax ; ils sont égaux si et seulement si le jeu a un "
             "point selle, et deux points selles ont la même valeur", "§1", "E"),
            ("M27.12", "∂", 2, 20, "La log-loss espérée est minimale pour la probabilité a posteriori : une preuve par "
             "l'inégalité de Gibbs", "§5", "E"),
            ("M27.13", "∂", 2, 20, "0 ≤ JS ≤ ln 2, et JS = ln 2 si et seulement si les deux lois ont des supports "
             "disjoints", "§6", ""),
            ("M27.14", "∂", 2, 25, "L'appariement trié est optimal : un argument d'échange sur deux paires, puis sur n "
             "paires, pour les coûts |x − y| et (x − y)²", "§8", ""),
            ("M27.15", "∂", 2, 20, "E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ : une distance estimée sur deux "
             "échantillons est biaisée vers le haut", "§9", "E"),
            ("M27.16", "🔗", 1, 20, "Pont : la distance de Fréchet en dimension 1, W₂² = (Δμ)² + (Δσ)², entre deux lois "
             "résumées par leur moyenne et leur écart-type (deux séries d'une machine, avant et après réglage) : la "
             "part de la moyenne et celle de l'écart-type, et pourquoi workbookIA 27 l'écrit avec des covariances et "
             "en rend le carré", "§8 §9", "E"),
            ("M27.17", "📖", 2, 25, "MML §7.2 relu : l'inégalité minimax (7.23) et sa preuve, la dualité faible (7.27) lue "
             "comme un jeu, et l'inégalité vérifiée sur une matrice de gains choisie", "§1", ""),
            ("M27.18", "🗣️", 1, 10, "Expliquer avec une partie de cache-cache pourquoi jouer au hasard peut être la "
             "meilleure stratégie, et ce que le hasard garantit", "§2", "E"),
            ("M27.E1", "💼", 1, 10, "« Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se "
             "recouvrent pas, et pas Jensen-Shannon ? »", "§6 §8", "E"),
            ("M27.E2", "💼", 1, 10, "« Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et "
             "comment comparer deux mesures ? »", "§9 §10", ""),
            ("M27.19", "🔨", 1, 15, "Les valeurs d'un jeu en stratégies pures : maximin, minimax et coups prudents, points "
             "selles compris", "§1", "E m:pure_strategy_values"),
            ("M27.20", "🔨", 2, 20, "Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle", "§2",
             "E m:mixed_strategy_value_2x2 p:M27.19"),
            ("M27.21", "🔨", 2, 20, "Les itérés de la descente-montée simultanée ou alternée sur un jeu bilinéaire xᵀAy",
             "§4", "m:descent_ascent_iterates"),
            ("M27.22", "🔨", 1, 10, "W₂ de deux gaussiennes en dimension 1, à partir des moyennes et des écarts-types",
             "§8", "E m:w2_gaussians_1d"),
            ("M27.23", "📦", 2, 25, "`scipy.optimize.linprog` : le transport optimal entre deux lois discrètes de la droite "
             "comme programme linéaire, comparé au plan monotone et à l'aire entre les fonctions de répartition",
             "§7 §8", ""),
            ("M27.24", "🔮", 1, 15, "Prédire la trajectoire de la descente-montée simultanée puis alternée sur xy, puis la "
             "tracer : spirale qui s'éloigne ou courbe fermée ?", "§4", "p:M27.21"),
            ("M27.25", "🔬", 2, 20, "Le biais d'une distance estimée : ‖x̄₁ − x̄₂‖² entre deux échantillons d'une même loi "
             "de ℝ³, selon leurs tailles, contre tr Σ₁/n₁ + tr Σ₂/n₂", "§9", ""),
            ("M27.26", "🎨", 1, 20, "Deux fonctions de répartition sur une même figure : l'aire entre elles (W₁) et leur "
             "plus grand écart vertical (KS), pour une translation puis une dilatation", "§8 §10", "E"),
            ("M27.27", "🐛", 1, 25, "Chasse à l'erreur : une stratégie d'indifférence calculée sur ses propres gains, W₂ de "
             "deux gaussiennes avec des variances, des échantillons appariés sans être triés", "§2 §8", ""),
            ("M27.28", "🛠️", 1, 20, "Un test de propriété : la valeur d'un jeu 2 × 2 tiré au hasard est entre maximin et "
             "minimax, et devient v + c pour G + c et k v pour k G (k > 0)", "§2", "p:M27.20"),
            ("M27.29", "🏆", 3, 30, "Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂, et cette "
             "distance, à 10⁻³ près", "§8", ""),
        ],
    },
    {
        "id": "M28", "dir": "m28_gram_echantillonnage", "hours": 9.8, "generation_sessions": 1, "mml": [],
        "summary": "La matrice de Gram d'une famille de vecteurs, lue dans les deux sens (XXᵀ et XᵀX), divisée par le "
                   "nombre d'échantillons pour devenir une matrice de moments d'ordre 2, et ce qu'elle coûte ; ce qu'elle "
                   "détermine : toutes les longueurs et tous les angles, donc les distances, et la configuration à une "
                   "isométrie près (double centrage, positions retrouvées à partir de distances) ; optimiser l'entrée "
                   "d'une fonction à paramètres fixés : montée de gradient, pas normalisé, projection sur un pavé, "
                   "coordonnées gelées, et ce que la montée trouve (un sommet du pavé, un vecteur propre) ; la variation "
                   "totale d'une grille, forme quadratique d'un laplacien, son gradient et le lissage qu'elle produit, et "
                   "les fréquences spatiales (période d'un motif, fréquence de Nyquist, gain d'un flou) ; les lois "
                   "catégorielles modifiées : température sur des probabilités, top-k et top-p comme lois "
                   "conditionnelles, le plus petit ensemble de masse donnée et le coût d'une troncature ; enfin une "
                   "itération déterministe sur un ensemble fini, qui finit toujours par boucler. workbookIA 28 applique "
                   "ces outils à la visualisation des réseaux, au transfert de style et à la génération de texte.",
        "objectives": [
            "Calculer la matrice de Gram d'une famille de vecteurs dans les deux sens et la matrice des moments d'ordre 2, "
            "et choisir laquelle former selon son coût.",
            "Lire des distances dans une matrice de Gram, retrouver une matrice de Gram à partir de distances (double "
            "centrage), puis des positions à une isométrie près.",
            "Démontrer que deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une "
            "isométrie.",
            "Faire une montée de gradient projetée sur un pavé, avec un pas normalisé ou des coordonnées gelées, et "
            "prévoir où elle s'arrête pour une fonction linéaire, quadratique ou convexe.",
            "Écrire la variation totale d'une grille comme une forme quadratique, calculer son gradient et un pas de "
            "lissage, et comparer le carré et la valeur absolue.",
            "Lire la période et la fréquence d'un motif, situer la fréquence de Nyquist, et calculer ce qu'en font la "
            "variation totale et un flou.",
            "Tempérer une loi catégorielle, la tronquer par top-k ou top-p, et calculer le coût de la troncature en "
            "divergence KL.",
            "Trouver la prépériode et la période d'une itération sur un ensemble fini, et expliquer pourquoi le décodage "
            "glouton boucle.",
        ],
        "sections": [("§1", "La matrice de Gram d'une famille de vecteurs : deux lectures, moments d'ordre 2 et coût"),
                     ("§2", "Ce que la matrice de Gram détermine : des distances aux positions, à une isométrie près"),
                     ("§3", "Optimiser l'entrée d'une fonction à paramètres fixés : montée projetée, pas normalisé, et "
                            "ce que l'on trouve"),
                     ("§4", "La variation totale d'une grille et les fréquences spatiales"),
                     ("§5", "Modifier une loi catégorielle : température, top-k, top-p, et le coût d'une troncature"),
                     ("§6", "Une itération déterministe sur un ensemble fini finit par boucler")],
        "teaches": ["matrice de Gram d'une famille de vecteurs : XXᵀ (produits scalaires des lignes) et XᵀX (des "
                    "colonnes), mêmes valeurs propres non nulles, symétrique semi-définie positive (rappels de M09a, "
                    "M12c, M12d, M13b) ; coût n²d contre d²n : former la plus petite",
                    "matrice des moments d'ordre 2 : XXᵀ/N quand les N colonnes sont des échantillons ; centrer donne la "
                    "covariance",
                    "distances et matrice de Gram : ‖xᵢ − xⱼ‖² = G_ii + G_jj − 2G_ij ; double centrage G = −½ J D⁽²⁾ J "
                    "(positionnement multidimensionnel classique) ; une matrice de distances est euclidienne si et "
                    "seulement si son double centrage est semi-défini positif (énoncé)",
                    "une matrice de Gram détermine la configuration à une isométrie près : invariance par une "
                    "transformation orthogonale de l'espace (énoncée), réciproque démontrée ; des positions de matrice "
                    "de Gram donnée par le théorème spectral (pour une Gram centrée, les scores d'une ACP)",
                    "optimiser l'entrée d'une fonction à paramètres fixés : montée de gradient, pas normalisé (g/‖g‖, "
                    "par une moyenne quadratique, par le signe) et son invariance quand la fonction est multipliée par "
                    "c > 0, montée projetée sur un pavé, coordonnées gelées (le gradient projeté sur un sous-espace de "
                    "coordonnées)",
                    "ce que trouve la montée : une forme linéaire maximisée sur une boule ou sur un pavé, une forme "
                    "quadratique sur la sphère (vecteur propre dominant ; la montée renormalisée est la méthode de la "
                    "puissance de I + 2ηA pour f = xᵀAx), une fonction convexe sur un pavé (un sommet, des coordonnées "
                    "saturées)",
                    "variation totale d'une grille : forme quadratique xᵀLx du laplacien de la grille (symétrique, "
                    "semi-défini positif, de noyau les constantes), gradient 2Lx, un pas de descente est un lissage "
                    "(une diffusion) et son pas critique ; le carré préfère les rampes, la valeur absolue garde les bords",
                    "fréquences spatiales : motif périodique, fréquence, période, fréquence de Nyquist (le damier), "
                    "repliement ; un motif périodique est un vecteur propre du laplacien circulaire, sa variation totale "
                    "rapportée à son énergie vaut 4 sin²(ω/2) par direction ; gain (1 + 2 cos ω)/3 d'une moyenne "
                    "mobile : un filtre passe-bas",
                    "température sur des probabilités : p^{1/T} renormalisé, une loi de Boltzmann d'énergies −ln pᵢ "
                    "(rappel de M17), limites T → 0 et T → ∞, issues de probabilité nulle gardées à 0 ; l'entropie croît "
                    "avec T (énoncé) ; le tirage catégoriel (rappel de M02b)",
                    "top-k et top-p : lois conditionnelles sur un ensemble d'issues (M03) ; le plus petit ensemble de "
                    "masse au moins p est fait des issues les plus probables ; la température garde l'ensemble du top-k, "
                    "et refroidir fait rétrécir celui du top-p",
                    "coût d'une troncature : KL(p_S ‖ p) = −ln P(S) et ½‖p_S − p‖₁ = 1 − P(S) ; KL(p ‖ p_S) infinie ; "
                    "la « distance en variation totale » entre deux lois n'est pas la variation totale d'une grille",
                    "itération déterministe sur un ensemble fini : principe des tiroirs, prépériode μ et période λ, "
                    "μ + λ ≤ |E| ; un générateur glouton à contexte fini boucle ; détection par le lièvre et la tortue "
                    "(Floyd, aperçu)"],
        "requires": [("division euclidienne et reste (`//`, `%`)", "R0"), ("cosinus, radians, périodicité", "R9"),
                     ("loi catégorielle, tirage catégoriel par inversion", "M02b"), ("loi conditionnelle", "M03"),
                     ("convexité d'une fonction d'une variable, log-sum-exp", "M05a"),
                     ("gradient, montée et descente", "M05b"),
                     ("entropie, divergence KL, KL infinie quand le support manque", "M06"),
                     ("produit scalaire, normes, Cauchy-Schwarz, similarité cosinus", "M07"),
                     ("transposée, XᵀX et XXᵀ", "M09a"), ("ridge : un terme de régularisation pondéré", "M09b"),
                     ("fonctions convexes de plusieurs variables", "M10"),
                     ("bases orthonormées, matrices orthogonales, Gram-Schmidt, projection sur un sous-espace", "M12b"),
                     ("théorème spectral, quotient de Rayleigh, méthode de la puissance, matrices semi-définies "
                      "positives, matrice de Gram XᵀX", "M12c"),
                     ("valeurs singulières, AᵀA et AAᵀ, approximation de rang faible, ACP quand n < p", "M12d"),
                     ("noyau polynomial et matrice de Gram d'un noyau", "M13b"),
                     ("principe des tiroirs", "M16"), ("loi de Boltzmann et ses limites en température", "M17"),
                     ("gradient par rapport à toutes les entrées en un passage inverse", "M18"),
                     ("projection sur une boule et sur un pavé, pas critique 2/λmax", "M19"),
                     ("matrice de centrage", "M20"),
                     ("laplacien discret, moyenne mobile, convolutions circulaires, forme linéaire sur une boule", "M21")],
        "frontieres": ["28.2", "28.4", "28.7", "28.8", "28.10", "28.12", "28.13", "28.15", "28.16", "28.17",
                       "28.18", "28.24", "28.25", "28.28", "28.Q2", "28.Q7", "28.Q10", "28.R2", "28.E2", "28.E3", "B4.Q5", "B4.13"],
        "mymath": {"module": "sampling.py",
                   "functions": ["points_from_gram", "temper", "smallest_mass_set"]},
        "reading_minutes": 100,
        "flashcards": 16,
        "notes": "Frontières : les ∂ 28.3 (une permutation des positions, puis une matrice orthogonale, ne change pas FFᵀ ; "
                 "un seul canal permuté la change ; C G_ii = μ² + σ² et la moyenne qu'elle ne fixe pas ; les tables "
                 "d'ordre 3) et 28.5 (le gradient 4(FFᵀ − S)F de la loss de style), ✏️ 28.2 (une Gram 3 × 4 normalisée "
                 "par CHW, cosinus, somme, retournement), ✏️ 28.4 (losses de contenu, de style et de variation totale "
                 "sur un mini-exemple, `mse_loss`, poids α, β et λ), 🧮 28.7 (LSTM mot à mot, Zipf, perplexité), "
                 "🗣️ 28.8, 📄 28.10 (Gatys), 🔮 28.12 et 🔬 28.15 (périodes de filtres appris, part des hautes "
                 "fréquences, flou, décalages, octaves), 📦 28.13 (pixels saturés d'une visualisation), 📦 28.16 (le "
                 "deep dream : un gradient normalisé, indépendant de l'échelle des activations), 🔬 28.17 (couches, "
                 "poids, un masque de zone), 📦 28.18 (Gram et "
                 "variation totale en PyTorch contre `einsum` et `np.diff`), 🔬 28.24 (poids contenu/style et leur "
                 "frontière), 🔬 28.25 (moyennes et écarts-types des canaux), 🔬 28.28 (glouton, température, top-k et "
                 "top-p sur Verne, `pick_28`, répétitions), les quiz 28.Q2, 28.Q7 et 28.Q10, le rappel 28.R2, les "
                 "entretiens 28.E2 et 28.E3, et, de workbookIA B4 (après M28), B4.Q5 et B4.13 (quelle stratégie de "
                 "décodage pour quelle tâche ; dix générations à trois températures). M28 enseigne les outils hors "
                 "réseau : nuages de points, villes et capteurs pour la matrice de Gram ; émetteurs réglables, énergies "
                 "quadratiques et modes de vibration pour la montée ; barres chauffées, plaques, étoffes rayées et "
                 "signaux échantillonnés pour la variation totale et les fréquences ; prévisions météorologiques, "
                 "diagnostics et identifications d'espèces pour les lois tronquées ; décimales d'une fraction, "
                 "itérations modulo n et automates pour les boucles ; jamais une carte d'activation, un filtre appris, "
                 "une image d'un dataset, un pixel permuté, un « style », un logit de mot ni un texte généré. "
                 "La matrice de Gram : les points sont les lignes de X (comme M13b) et G = XXᵀ ; la normalisation est "
                 "celle d'une matrice de moments, 1/N pour N échantillons, jamais 1/(CHW) ni une forme (C, H, W) ; la "
                 "double lecture XXᵀ/XᵀX, la symétrie et la positivité sont des rappels (M09a, M12c.17, M12d.12, M13b), "
                 "et aucune fonction ne calcule une Gram (c'est `polynomial_kernel(X, X, 1, 0)` de M13b, et "
                 "`gram_matrix_18` de 28.18). L'invariance par une transformation orthogonale de l'espace (X ↦ XRᵀ, "
                 "tourner le repère) est énoncée en une ligne et utilisée ; la réciproque est démontrée (∂ M28.8 : une "
                 "application linéaire définie sur l'espace engendré par les points, isométrique, prolongée par "
                 "Gram-Schmidt), avec la construction par le théorème spectral (🔨 M28.13) ; aucun exercice ne permute "
                 "les colonnes de X (positions ou échantillons), ne demande si permuter une seule ligne change G, ni ne "
                 "relie la diagonale à μ² + σ² ou à une moyenne qu'elle ne fixe pas (∂ 28.3.4-5), et M28.Q1 lit la "
                 "diagonale comme les carrés des normes des points, jamais comme une moyenne de carrés (28.Q7 d) ; "
                 "pas de statistiques "
                 "d'ordre 3 ; l'écart de Frobenius entre les matrices de moments de deux nuages, égal à une MMD de noyau "
                 "(xᵀy)² (M13b), est au plus une remarque de la fiche, sans loss ni « style ». Aucun gradient d'une "
                 "fonction de XXᵀ ou de XᵀX (ni ‖XXᵀ − S‖²_F, ni ‖XᵀX − I‖², paraphrase transposée de ∂ 28.5) : le seul "
                 "gradient matriciel du chapitre est celui de la variation totale, 2Lx. Le double centrage est "
                 "−½ J D⁽²⁾ J sur les **carrés** des distances, avec la matrice de centrage J de M20 ; ✏️ M28.2 prend "
                 "quatre villes aux sommets d'un losange (une matrice de Gram à blocs, diagonalisable à la main), et "
                 "✏️ M28.3 une énergie quadratique de matrice à blocs 2 × 2 en dimension 4, diagonalisable à la main : "
                 "les deux tiennent ainsi en 25 minutes. "
                 "La montée sur l'entrée : f(x ; θ) à θ fixé, sur des fonctions écrites (réponses linéaires et "
                 "quadratiques d'émetteurs réglables entre 0 et 1, énergies) ; le pas normalisé et son invariance quand f "
                 "est multipliée par c > 0 sont démontrés en général, sans deep dream, octaves, masque d'image ni "
                 "« activation » ; la montée projetée est celle de M19 §8 (`np.clip`) ; un gradient restreint à des "
                 "coordonnées libres est la projection orthogonale de M12b, sans zone d'image (28.17) ; le maximum d'une "
                 "fonction convexe sur un pavé (un sommet, ∂ M28.9) explique les coordonnées saturées, sans les "
                 "pourcentages de pixels de 28.13 ; une moyenne de carrés de réponses linéaires est la forme "
                 "quadratique xᵀAx avec A = WᵀW/m, et la montée renormalisée sur elle est la méthode de la puissance "
                 "de I + 2ηA (le gradient vaut 2Ax) "
                 "(M12c) ; aucun vrai ou faux « monter sur f, c'est descendre sur −f » ni « les paramètres sont gelés, "
                 "le gradient par rapport à l'entrée existe quand même » (28.Q2 b et e). La variation totale : sur une "
                 "grille de mesures (somme des carrés des différences entre voisins horizontaux et verticaux, comme "
                 "workbookIA) et sur un signal, écrite xᵀLx avec le laplacien de la grille ((Lx)_ij = 4x_ij − la somme "
                 "des voisins à l'intérieur : le pochoir de M21 au signe près), de gradient 2Lx ; un pas de descente est "
                 "un pas de diffusion, de pas critique 1/λmax(L) (M19) ; la valeur absolue (variation totale de Rudin, "
                 "Osher et Fatemi, nommée sans date) garde les bords, le carré préfère les rampes (h²/n contre h pour "
                 "une marche étalée sur n pas) ; jamais la grille 3 × 3 de 28.4, une puissance 1,25, une image de "
                 "scikit-learn ni une loss totale pondérée ; débruiter un signal par min ‖x − y‖² + λxᵀLx, soit "
                 "(I + λL)x = y, est une remarque (gain 1/(1 + 4λ sin²(ω/2)) par fréquence, un compromis réglé par λ "
                 "comme la ridge de M09b), sans courbe contenu/style. Les fréquences spatiales comblent une lacune (ni "
                 "M21 ni R9 ne les enseignent ; workbookIA 28 s'en sert dans ses outils fournis et en 28.12, 28.14, "
                 "28.15 et 28.24) : un motif cos(2π(f₁i + f₂j) + φ), sa fréquence en cycles par case, sa période "
                 "1/√(f₁² + f₂²) dans la direction (f₁, f₂), la fréquence de Nyquist ½ (le damier) et le repliement (f et "
                 "1 − f donnent les mêmes échantillons) ; un motif périodique est un vecteur propre du laplacien "
                 "circulaire (∂ M21.13 : les matrices circulantes), de valeur propre 4 sin²(ω/2) en dimension 1 (ω = 2πf) "
                 "et la somme des deux en dimension 2, d'où sa variation totale rapportée à son énergie, un quotient de "
                 "Rayleigh (M12c), maximale pour le damier ; la moyenne mobile de trois cases multiplie un motif par "
                 "(1 + 2 cos ω)/3 et efface la période 3 ; sans transformée de Fourier discrète (un encadré 💻 au plus), "
                 "sans « part de la variance au-dessus de la moitié de la fréquence de Nyquist » ni période dominante "
                 "d'une image (les outils `high_freq_share` et `dominant_period` du notebook de workbookIA 28). Les lois "
                 "catégorielles : données par leurs probabilités, jamais par des logits de mots ; la température sur des "
                 "probabilités est la loi de Boltzmann des énergies −ln pᵢ (M17), les issues de probabilité nulle le "
                 "restent ; le 🔗 M28.11 montre que diviser des scores par T avant la softmax donne la même loi, sur les "
                 "scores d'un classifieur d'espèces (ni mots ni vocabulaire), sans refaire 17.6, 22.5 ni 26.5 ; la "
                 "croissance de l'entropie avec T (dH/dT = Var(E)/T³) est énoncée et constatée, sa démonstration est "
                 "l'un des sujets de CP6.8 ; top-k et top-p sont des lois conditionnelles (M03) sur l'ensemble gardé, le "
                 "top-p étant le plus petit ensemble de masse au moins p (∂ M28.10 : un argument d'échange, puis "
                 "KL(p_S ‖ p) = −ln P(S) et ½‖p_S − p‖₁ = 1 − P(S)) ; la température ne change pas l'ensemble du top-k "
                 "(elle garde l'ordre) et, en refroidissant, la masse des j issues les plus probables croît, donc "
                 "l'ensemble du top-p rétrécit ; un encadré ⚠️ distingue la variation totale d'une grille et la "
                 "« distance en variation totale » ½‖p − q‖₁ entre deux lois ; le tirage lui-même est un rappel de M02b. "
                 "Les boucles : une suite u_{t+1} = f(u_t) sur un ensemble de N éléments devient périodique, avec "
                 "μ + λ ≤ N (principe des tiroirs de M16), démontré dans la fiche et appliqué aux décimales de a/n et à "
                 "x ↦ x² + c modulo n (✏️ M28.7) ; un générateur glouton dont l'état est fait des w derniers symboles "
                 "d'un alphabet de V symboles a au plus V^w états : il boucle ; un modèle à état continu (une cellule "
                 "récurrente) n'entre pas dans le théorème, et la fiche le dit ; l'algorithme du lièvre et de la tortue "
                 "(Floyd) est un encadré 💻, sans fonction `mymath` ; ni phrase générée, ni « de la de la », ni part de "
                 "trigrammes répétés (28.28). Le 🐛 M28.17 n'a aucune des erreurs du corrigé de 28.28 (renormaliser "
                 "avant de couper, trier dans le mauvais sens, un mot de moins que le seuil) ni de 28.21 (normalisation "
                 "oubliée, Gram non normalisée, optimiseur sur les poids, bornes de `clamp_`). Évités (règle de "
                 "partage) : les matrices F = [[3, 1], [0, 2]] (Gram [[2,5 ; 0,5], [0,5 ; 1]]), [[1, 0, 2, 1], "
                 "[0, 3, 1, 1], [2, 0, 4, 2]] (FFᵀ [[6, 3, 12], [3, 11, 6], [12, 6, 24]], 0,917, 6,917, 0,369), "
                 "[[2, 0, 1, 1], [1, 1, 0, 2]] (0,75 ; 0,5 ; 0,667), [[1, 0], [1, 0]] et [[1, 0], [0, 1]], [[1, 1], "
                 "[0, 2]], [[2, 0], [0, 2]], [[1, 0], [1, 1]], et, du checkpoint VI, [[1, 0, 2, 1], [0, 1, 1, 0], "
                 "[2, 1, 0, 1]] ([[6, 2, 3], [2, 2, 1], [3, 1, 6]]) ; les canaux (1, 1) et (0, √2) ; les vecteurs "
                 "(1, 2, 0, 1), (1, 0, 1, 1) et (0, 1, 1, 1) ; la grille [[0, 1, 0], [1, 1, 1], [0, 1, 3]] et ses "
                 "variations totales 14 et 10 ; α = 0,025, β = 1, λ = 10⁻⁴, 40, 0,8764, 12, 0,9375 (28.4) ; "
                 "CHW = 401 408 et 1,6 × 10¹¹, 10,90, 512³ et 134 millions ; les tailles de VGG16 (3 211 264, 401 408, "
                 "262 144, 784, 131 328) et ses 224, 28 et 14 pixels, SqueezeNet ; 15,5 et 0,35 milliard de MAC, "
                 "138,4 M, 14,7 M, 123,6 M, 553 Mo ; la loi (0,5 ; 0,2 ; 0,15 ; 0,1 ; 0,05) avec p = 0,8, son cumul "
                 "0,85 et (0,588 ; 0,235 ; 0,176) ; les logits (2 ; 1 ; 0,5 ; 3 ; −1) et leur softmax, (3,1 ; 2,6 ; "
                 "2,2 ; 1,6 ; 1,5 ; 1,1 ; 0,8 ; 0,5 ; 0,2 ; −0,3), (1, 2, 3), (1, 5, 2), (3 ; 1 ; 0,5) de 22.5 et les "
                 "scores 0,6 / 0,3 / 0,1 de 17.Q12 ; les seuils de top-p 0,75, 0,8, 0,9 et 0,01, les k = 1, 2 et 20, les "
                 "températures 0,5 ; 0,7 ; 1,2 ; 1,5 et 2 (les ✏️ prennent T = 1/3, 1/4, 3 ou 4, des puissances "
                 "exactes), 6 000 tirages et la tolérance 0,03 ; (1, 2, 3, 1, 2, 3, 1) et 0,4 ; 10 300 mots, 427 000 "
                 "mots, 2 × 128 cellules, les perplexités 150, 439 et 113, la formule de Zipf ; la moyenne (0,485 ; "
                 "0,456 ; 0,406) et l'écart-type (0,229 ; 0,224 ; 0,225) d'ImageNet ; les filtres 5, 17 et 100, les "
                 "périodes de 2, 4, 8, 13 et 16 pixels, les parts de hautes fréquences (0,75 pour un bruit blanc ; 71, "
                 "76, 83 et 91 %), les pixels saturés (≈ 50 %, 37 à 45 %, 98 %) ; l'interpolation de (0, 2) et "
                 "(4, −2) à t = 0,25 ; Verne, Holmes, « Phileas Fogg », « le capitaine… », « de la de la », la grenouille, "
                 "la pagode, la fleur, les images `china` et `flower`, les tableaux et leurs peintres ; et, de ce dépôt, "
                 "la loi (0,1 ; 0,4 ; 0,35 ; 0,15) de M02b, les trois niveaux (0 ; 0,5 ; 2) et p = (0,5 ; 0,3 ; 0,2) de "
                 "M17 ; la fiche ne reprend ni le losange de ✏️ M28.2 ni les exemples du stub. Conventions : "
                 "points en lignes de X ; ω = 2πf en radians par case ; la variation totale est la somme des carrés "
                 "(comme workbookIA), la version en valeur absolue est nommée chaque fois ; une loi est un vecteur de "
                 "probabilités ; indices à partir de 0 ; entre deux probabilités égales, le plus petit indice d'abord "
                 "(un tri stable). `sampling` : NumPy permis, de `np.linalg` seulement "
                 "`eigh` (dans `points_from_gram`), aucune fonction de SciPy (`scipy.special.softmax` et `logsumexp` "
                 "donneraient `temper`) ni de scikit-learn ; les fonctions prennent des probabilités (jamais des logits) "
                 "et ne tirent rien : `temper` (T = 0 et T = ∞ compris, zéros gardés) a un autre contrat que "
                 "`temperature_softmax` (logits, T > 0) de workbookIA 22, `smallest_mass_set` rend un ensemble "
                 "d'indices, pas un tirage ni une loi prête à tirer (`sample_from_logits` de workbookIA 22, `pick_28` de "
                 "28.28, `sample_categorical` de workbookIA 2) ; la docstring ne donne ni la tranche du top-k ni la "
                 "renormalisation suivie d'un tirage (l'indice 3 de 28.28), et aucun exercice ni la fiche ne les "
                 "écrivent en code ; `smallest_mass_set` rend exactement l'ensemble que garde la branche top-p de "
                 "`pick_28` (à 1e-9 près) : c'est la brique mathématique (∂ M28.10), assumée ; aucune fonction de "
                 "matrice de Gram, de loss de style, de "
                 "variation totale (`gram_matrix_18`, `tv_loss_18`) ni de période. Pas de MML : le livre ne traite ni la "
                 "variation totale, ni les fréquences, ni les troncatures, ni les itérations sur un ensemble fini, et "
                 "AAᵀ, AᵀA et la matrice de Gram d'un noyau ont été lus en M12d (§4.5) et M13b (§12.4) ; donc pas de 📖. "
                 "COMPOSITION : prévu court (6 h au plan, 8 h visées en session 60), porté à 9,8 h par la lacune des "
                 "fréquences spatiales, la réciproque de la matrice de Gram et des durées réalistes (relectures de M21 et "
                 "M22) : la composition d'un chapitre court est gardée (5 quiz, 7 ✏️ et 3 ∂, 2 🔨, un 🔮 et un 🎨 sans "
                 "🔬, 16 flashcards). Parcours essentiel : les ∂ de la Gram et de la montée (M28.8, M28.9), le 💼, le "
                 "🔨 de la Gram, son 🛠️ et le 🏆 hors parcours ; ∂ M28.10 (le top-p) y est.",
        "exercises": [
            ("M28.Q1", "🧠", 1, 4, "Matrice de Gram : XXᵀ ou XᵀX, laquelle former, sa diagonale, et les distances qu'on y "
             "lit", "§1 §2", "E"),
            ("M28.Q2", "🧠", 1, 4, "Monter sur l'entrée : pas normalisé, projection sur un pavé, coordonnées gelées, point "
             "d'arrivée", "§3", "E"),
            ("M28.Q3", "🧠", 1, 4, "Variation totale et fréquences spatiales : quel motif coûte le plus, lequel traverse "
             "un flou ?", "§4", "E"),
            ("M28.Q4", "🧠", 1, 4, "Température, top-k et top-p : ce qui change l'ensemble gardé, ce qui ne change que les "
             "probabilités", "§5", "E"),
            ("M28.Q5", "🧠", 1, 4, "Une itération sur un ensemble fini : prépériode, période, et ce qui empêche de boucler",
             "§6", "E"),
            ("M28.R1", "🔁", 1, 5, "Le quotient de Rayleigh et la méthode de la puissance (M12c)", "§3", "E"),
            ("M28.R2", "🔁", 1, 5, "Le laplacien discret et la moyenne mobile d'un signal (M21)", "§4", "E"),
            ("M28.R3", "🔁", 1, 5, "La loi de Boltzmann et ses limites en température (M17)", "§5", "E"),
            ("M28.1", "✏️", 2, 20, "Quatre points du plan : leur matrice de Gram 4 × 4, leur matrice des moments d'ordre "
             "2, et les distances lues dans la Gram", "§1", "E"),
            ("M28.2", "✏️", 2, 25, "Quatre villes aux sommets d'un losange : le double centrage des carrés des distances, "
             "puis une carte à une isométrie près", "§2", "E"),
            ("M28.3", "✏️", 2, 25, "Régler quatre émetteurs entre 0 et 1 : le maximum d'une réponse linéaire sur la boule "
             "et sur le pavé, d'une énergie quadratique sur la sphère, et deux pas de montée projetée", "§3", "E"),
            ("M28.4", "✏️", 2, 25, "Les températures le long d'une barre : la variation totale xᵀLx, son gradient 2Lx, un "
             "pas de lissage, et une marche étalée sur n pas, au carré ou en valeur absolue", "§4", "E"),
            ("M28.5", "✏️", 2, 25, "Des étoffes rayées : période, fréquence, fréquence de Nyquist, repliement, variation "
             "totale rapportée à l'énergie 4 sin²(ω/2), et gain d'une moyenne mobile", "§4", "E"),
            ("M28.6", "✏️", 2, 25, "La prévision d'un météorologue en six catégories : la refroidir, garder les deux plus "
             "probables, garder le plus petit ensemble de masse donnée, et le coût de chaque troncature", "§5", "E"),
            ("M28.7", "✏️", 1, 15, "Les décimales de a/n et l'itération x ↦ x² + c modulo n : prépériode et période à la "
             "main, et la borne du principe des tiroirs", "§6", "E"),
            ("M28.8", "∂", 3, 30, "Deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une "
             "isométrie", "§2", ""),
            ("M28.9", "∂", 2, 15, "Le maximum d'une fonction convexe sur un pavé est atteint en un sommet", "§3", ""),
            ("M28.10", "∂", 2, 25, "Le plus petit ensemble de masse au moins p est fait des issues les plus probables, et "
             "la loi tronquée est à −ln P(S) de la loi de départ en divergence KL", "§5", "E"),
            ("M28.11", "🔗", 1, 15, "Pont : diviser des scores par T avant la softmax, ou élever les probabilités à la "
             "puissance 1/T, la même loi ; et le même top-k", "§5", "E"),
            ("M28.12", "🗣️", 1, 10, "Expliquer avec une structure de barres rigides ce que la matrice de Gram d'une "
             "famille de vecteurs fixe, et ce qu'elle laisse libre", "§2", "E"),
            ("M28.E1", "💼", 1, 10, "« Que perd-on, en divergence KL, à ne garder que les issues les plus probables d'une "
             "loi avant de tirer ? »", "§5", ""),
            ("M28.13", "🔨", 2, 25, "Une configuration de points de matrice de Gram donnée, par le théorème spectral", "§2",
             "m:points_from_gram"),
            ("M28.14", "🔨", 2, 30, "Tempérer une loi donnée par ses probabilités, et le plus petit ensemble de masse "
             "donnée", "§5", "E m:temper,smallest_mass_set"),
            ("M28.15", "🔮", 1, 15, "Prédire ce que deviennent un pas η∇f et un pas normalisé quand la fonction est "
             "multipliée par 1 000, puis vérifier", "§3", "E"),
            ("M28.16", "🎨", 1, 20, "Des motifs rayés de fréquence croissante jusqu'au damier : leur variation totale, et "
             "ce qu'en laissent un flou 3 × 3 et dix pas de descente sur la variation totale", "§4", "E"),
            ("M28.17", "🐛", 1, 20, "Chasse à l'erreur : un double centrage fait sur les distances au lieu de leurs "
             "carrés, une montée qui coupe le gradient au lieu du point, une prépériode comptée dans la période",
             "§2 §3 §6", "E"),
            ("M28.18", "🛠️", 1, 15, "Un test de propriété : la configuration rendue redonne la matrice de Gram et les "
             "distances, pour des points tirés au hasard", "§2", "p:M28.13"),
            ("M28.19", "🏆", 3, 30, "Défi : redessiner la carte de 30 villes quand un quart des distances manquent, à moins "
             "de 1 km en moyenne après alignement", "§2", "p:M28.13"),
        ],
    },
    {
        "id": "CP6", "dir": "checkpoints/partie_6", "hours": 3.1, "generation_sessions": 1, "mml": [],
        "summary": "Le bilan de la partie VI (M25a, M25b, M26, M27 et M28), juste avant le checkpoint VI de workbookIA : un "
                   "examen blanc d'environ 2 heures (sujet, notebook de vérification, corrigé détaillé, barème sur 20), "
                   "puis une synthèse (carte mentale et fiche d'une page). Pas de mini-projet.",
        "objectives": [
            "Vérifier en temps limité que les notions de la partie VI sont acquises.",
            "Construire ta propre synthèse de la partie VI.",
        ],
        "sections": [("§1", "Examen blanc"), ("§2", "Synthèse")],
        "teaches": ["révision de la partie VI"],
        "requires": [("toute la partie VI", "M28")],
        "frontieres": ["25.5", "25.6", "25.7", "25.8", "25.11", "25.13", "25.20", "25.23", "25.28", "25.29", "25.30",
                       "25.31", "25.32", "25.33", "25.34", "25.36", "25.38", "25.Q9", "25.Q12", "25.R3", "25.E1", "25.E2",
                       "25.E3", "26.1", "26.3", "26.4", "26.5", "26.6", "26.7", "26.8", "26.9", "26.12", "26.14",
                       "26.26", "26.Q6", "26.Q8", "26.Q9", "26.Q10", "26.R3", "26.E2", "26.E4", "27.2", "27.3", "27.4",
                       "27.5", "27.6", "27.7", "27.10", "27.11", "27.13", "27.14", "27.18", "27.22", "27.23", "27.Q5",
                       "27.E1", "27.E4", "27.E5", "28.2", "28.3", "28.4", "28.5", "28.7", "28.8", "28.10", "28.12",
                       "28.13", "28.15", "28.16", "28.17", "28.18", "28.24", "28.25", "28.28", "28.Q2", "28.Q7",
                       "28.Q10", "28.R2", "28.E2", "28.E3", "B4.Q5", "B4.13", "B5.6", "B7.4", "B7.22", "B7.Q11",
                       "B7.E4", "B8.Q4", "B8.Q7", "B8.1", "B8.4"],
        "reading_minutes": 15,
        "flashcards": 0,
        "notes": "Fichiers comme CP5 : 01_examen_sujet.md, 02_examen_notebook.ipynb, 03_examen_corrige.md, "
                 "03_examen_solutions.ipynb, 04_mes_reponses.md, 05_synthese.md, README.md ; examen entièrement sur "
                 "papier (calculatrice ou Python comme simple calculatrice, sans NumPy), notebook de vérification "
                 "derrière `EXAM_OVER`, barème d'un point par minute prévue, chaque réponse avec son format. Aucune "
                 "question ne reprend le checkpoint VI de workbookIA (`checkpoints/partie_6/` de workbookIA), qui se fait "
                 "juste après, ni son mini-projet VI (`projets/partie_6_generatif/`) ; une même configuration, même avec "
                 "d'autres nombres, est une reprise (règle de CP5). Ne sont donc pas posés : une matrice de Gram de "
                 "cartes d'activation aplaties, normalisée par CHW, sa forme (C, C) et la permutation des positions "
                 "(CP6.1 h et CP6.5 de workbookIA, ✏️ 28.2) ; un tirage reparamétrisé μ + σ ⊙ ε avec log σ², la KL de "
                 "chaque latent contre 𝒩(0, 1), la dérivée ½σε et le cas log σ² = −10 (CP6.2) ; une mise à jour de "
                 "Q-learning puis de SARSA sur une table, la probabilité d'une action ε-greedy (CP6.3) ; le "
                 "discriminateur optimal par a ln y + b ln(1 − y), les losses 2 ln 2 et ln 2 à l'équilibre, la "
                 "saturation de ln(1 − D) (CP6.4 : l'outil se teste dans un autre cadre, la fraction de Kelly "
                 "p ln(1 + f) + (1 − p) ln(1 − f) par exemple, à vérifier contre M27) ; le retour actualisé d'une suite "
                 "de récompenses et la mémoire d'une table Q en 3ⁿ (CP6.1 d, CP6.10) ; les courbes d'un VAE, d'un GAN et "
                 "d'un Q-learning (CP6.7) ; une taille de sortie de convolution ou de convolution transposée, deux pas "
                 "d'Adam (CP6.13) ; un facteur de compression 784/32 ; la mémoire d'un dataset N × H × W × C (✏️ 29.1) ; "
                 "la distance de Fréchet entre features, l'entropie des classes prédites divisée par ln 10, la distance "
                 "au plus proche voisin d'entraînement et le quantile de copie du mini-projet. Nombres évités, en plus "
                 "de ceux des notes de M25a à M28 : 24,5 ; 0,81 ; (16, 4) ; 0,5, 1,386 et 0,693 ; (64, 64), 64 cartes de "
                 "14 × 14 et (196, 196) ; 70 000 et 60 000 ; μ = (0,5 ; −1), log σ² = (0 ; ln 0,25), ε = (1,2 ; −0,4), "
                 "[1,7 ; −1,2], [0,1250 ; 0,8181], 0,9431, −0,1000, −10 et 4,5 ; la table (0,2 ; 0,4 ; 0,1 / 0,5 ; "
                 "0,3 ; 0,8 / 0,6 ; 0 ; 0), α = 0,5, γ = 0,9, 0,56, 0,72, 0,9, 1,17, 0,425, 0,45, ε = 0,2 et 0,8667 ; "
                 "p_data = 0,3, p_g = 0,1 et 0,75 ; [[1, 0, 2, 1], [0, 1, 1, 0], [2, 1, 0, 1]], [[6, 2, 3], [2, 2, 1], "
                 "[3, 1, 6]], 0,5 et 0,25 ; 506 plateaux, 3 000 parties, 100 coups, 20,2 %, 80 à 95 % et 2,7 coups ; "
                 "β = 60, 208 et 120 nats, 0,004 nat ; 10⁻² et 10⁻⁵, −0,2 et 4 ; FrozenLake 8 × 8, 64 victoires, "
                 "3 000 épisodes, 60 pas ; 829,45, 2,75, 837,68, 16 images, d = 4, la graine 68 ; 𝒩(4 ; 1,25²), "
                 "batch 64, 2 × 10⁻³, 1 500 pas, 4,05 et 1,26 ; 3⁹, 5 478, 3¹⁶, 0,71 Mo, 0,20 Mo, 2,755 Go, 24 848 ; "
                 "(1, 3, 64, 64), 2 432, (1, 32, 32, 32), (1, 16, 64, 64), w₀ = 1, η = 0,01, g = (0,5 ; −0,1), 0,99 et "
                 "0,9849 ; CelebA (200 000 photos, 40 attributs) ; et, du mini-projet, 50 000 / 10 000 et la graine "
                 "2026, les graines 0, 1 et 2, β ∈ {0,5 ; 1 ; 4}, les latents 16 et 64, copy_quantile 1 %, le plancher "
                 "1,093, les repères 212,166 et 490,696, 214,888, 95,149, 37,27, 0,925, 0,9993, 0,111 et le seuil "
                 "1,6126. La synthèse a sa propre structure (une carte mentale et une fiche d'une page faites par "
                 "l'apprenant) : elle ne recopie ni le tableau des 18 formules, ni la carte mentale à neuf nœuds, ni le "
                 "tableau AE/VAE/GAN/diffusion, ni « le gradient par rapport à l'entrée : un même geste, quatre usages », "
                 "ni la check-list des 8 points d'un dataset, ni le mode d'emploi en 90 minutes de la synthèse de "
                 "workbookIA. Côté M28, l'examen pose la matrice de Gram d'une famille de **points** (double centrage, "
                 "distances, configuration à une isométrie près, CP6.6) et la troncature top-p des lignes d'une "
                 "chaîne, avec son coût en divergence KL (CP6.10) ; la température n'est que dans le ∂ au choix "
                 "CP6.8 et le quiz ; la variation totale, les fréquences spatiales et la montée projetée ne sont que "
                 "dans le quiz et le 🐛 ; jamais de carte, de "
                 "pixel permuté ni de logit de mot. CP6.8 donne le choix entre un énoncé que M28 admet, l'entropie "
                 "d'une loi tempérée croît avec la température (dH/dT = Var(E)/T³ ≥ 0, énoncé et constaté en M28), et un "
                 "transfert de M25b, la loi de Boltzmann minimise l'« énergie libre » E_q[E] − T H(q) parmi les lois q "
                 "(par la positivité de la KL : le calcul de ln p(x) = ELBO + KL, avec une température et sans variable "
                 "latente) ; aucune ne touche à un "
                 "discriminateur, à une reparamétrisation ni à une contraction de l'opérateur de Bellman avec un "
                 "maximum (∂ 26.8). CP6.10 relie M26 et M28 hors réseau : une file d'attente à trois états (pas une "
                 "météo : ✏️ M28.6 en est une) dont on suit l'état le plus probable (une itération déterministe : "
                 "elle boucle, prépériode et période), puis qu'on échantillonne après avoir tronqué chaque ligne à ses "
                 "issues les plus probables (lois conditionnelles, coût en KL d'une ligne, nouvelle loi stationnaire, "
                 "que CP6.4 ne demande plus) ; ni mots, ni "
                 "génération de texte, ni état terminal, ni récompense de jeu. Les titres de CP6.1 à CP6.7 suivent "
                 "les entrées de M25a à M28 ; leurs cadres et leurs nombres se fixent à la génération, contre les "
                 "entrées publiées de ces chapitres (aucune reprise de leurs exercices ni de leurs fiches, cf. CP5), "
                 "règle qui vaut pour tout l'examen : CP6.6 n'est pas le losange de villes de ✏️ M28.2 ; CP6.7 "
                 "porte sur des séries de mesures (jamais des features ni un FID) et n'est pas la configuration de "
                 "✏️ M27.9 (covariances diagonales, puis tournées ensemble) ; CP6.10 n'est pas la prévision "
                 "météo de ✏️ M28.6 ; CP6.2 suit les garde-fous de M25a (deux covariances pleines, jamais contre "
                 "N(0, I) ni une diagonale contre l'identité). **Équilibre** (relectures de la session 60) : chaque "
                 "chapitre pèse de 16 à 22 minutes de l'examen (M25a : CP6.1 et CP6.2 ; M25b : CP6.3 et l'option B "
                 "de CP6.8 ; M26 : CP6.4 et la moitié de CP6.10 ; M27 : CP6.5 et CP6.7 ; M28 : CP6.6, la moitié de "
                 "CP6.10 et l'option A de CP6.8), plus deux affirmations par chapitre dans CP6.Q1 (pour M27 : JS de "
                 "lois à supports disjoints, la descente-montée simultanée ; pour M25b : KL directe ou inverse, le "
                 "posterior agrégé) et une erreur par chapitre dans le 🐛 CP6.9 (celles de M25b et de M27 sur "
                 "d'autres objets que les 🐛 M25b.28 et M27.27). **Durées** (CP5 prévoyait 112 minutes, le candidat "
                 "simulé en a mis environ 137) : CP6.3 avec deux composantes de variances connues, trois mesures, "
                 "seulement le poids et les moyennes mis à jour, et l'écart à l'ELBO d'une affectation dure, "
                 "−Σ ln r ; CP6.4 sur une chaîne dont le système de Bellman est triangulaire (une ligne qui finit), "
                 "sans loi stationnaire ; CP6.5 avec deux échantillons de même taille (les tailles différentes sont "
                 "à 27.11) ; CP6.10 à trois états.",
        "exercises": [
            ("CP6.Q1", "🧠", 1, 10, "Dix affirmations sur la partie VI, deux par chapitre : vrai ou faux", "§1", "E"),
            ("CP6.1", "✏️", 2, 10, "Un vecteur gaussien de dimension 2 : loi marginale, loi conditionnelle, et la loi de "
             "μ + Lε", "§1", "E"),
            ("CP6.2", "✏️", 2, 9, "La divergence KL entre deux gaussiennes de dimension 2, et une interpolation "
             "sphérique", "§1", "E"),
            ("CP6.3", "✏️", 2, 10, "Un mélange de deux gaussiennes de variances connues et trois mesures : "
             "responsabilités, un pas d'EM sur le poids et les moyennes, et l'écart à l'ELBO d'une affectation "
             "dure", "§1", "E"),
            ("CP6.4", "✏️", 2, 9, "Une chaîne de Markov à trois états : loi à deux pas, et la valeur d'une politique "
             "fixée par le système de Bellman, quand une ligne finit", "§1", "E"),
            ("CP6.5", "✏️", 2, 9, "Un jeu à somme nulle 2 × 2 en stratégies mixtes, et W₁ entre deux petits "
             "échantillons de même taille", "§1", "E"),
            ("CP6.6", "✏️", 2, 8, "Des distances aux positions : double centrage, matrice de Gram, et une configuration "
             "à une isométrie près", "§1", "E"),
            ("CP6.7", "✏️", 2, 9, "La distance de Fréchet de deux gaussiennes du plan de covariances "
             "proportionnelles, et le biais de la distance entre deux moyennes estimées", "§1", "E"),
            ("CP6.8", "∂", 3, 12, "Une démonstration au choix : l'entropie d'une loi tempérée croît avec la température, "
             "ou la loi de Boltzmann minimise l'énergie libre", "§1", "E"),
            ("CP6.9", "🐛", 2, 9, "Corriger une copie : cinq erreurs, une par chapitre", "§1", "E f:02"),
            ("CP6.10", "🔗", 2, 16, "Problème de synthèse : une file d'attente à trois états suivie de façon "
             "gloutonne, puis échantillonnée après la troncature top-p de ses transitions : lois conditionnelles, "
             "coût en KL et nouvelle loi stationnaire", "§1", "E"),
            ("CP6.11", "🗣️", 1, 60, "Ta carte mentale et ta fiche d'une page", "§2", "E"),
        ],
    },
]
