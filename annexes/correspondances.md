# Correspondances : workbookIA ↔ workbookMaths ↔ MML

Trois tables pour se repérer entre les deux workbooks et le livre. Elles suivent `src/wbm/chapters.py` et le plan de `docs/BIBLE.md` §8.

## 1. Pour chaque chapitre de workbookIA, les chapitres de maths à faire juste avant

| workbookIA | Chapitres de maths | Sections de MML |
|---|---|---|
| 0A · Python, notebooks et outils | R0, POS, R1 à R9, en parallèle | — |
| 0B · Maths du lycée au ML | (R0 à R9 faits) puis CP0 | — |
| 1 · Introduction au machine learning et au deep learning | — (rien de nouveau) | — |
| 2 · Hasard et statistiques de base | M02a, M02b, M02c | (prérequis de §6.2) ; §6.1–6.2, §6.4, §6.7 ; §6.4 |
| 3 · Probabilités et mesure de la qualité | M03 | §6.3 |
| 4 · Règle de Bayes | M04 | §6.3, §6.6, §8.3 |
| 5 · Courbes et surfaces | M05a, M05b | §5.1 ; §5.2 |
| 6 · Théorie de l'information | M06 | — (MacKay) |
| 7 · Classification | M07 | §3.1, §3.2.1, §3.3–3.4 |
| 8 · Entraînement et test | M08 | §8.6 |
| 9 · Overfitting et underfitting | M09a, M09b | §2.1–2.3 ; §5.5, §8.1–8.2, §9.1–9.2 |
| 10 · Neurones | M10 | §12.1 |
| 11 · Apprentissage et raisonnement | M11 | — (Hammack ; Blitzstein et Hwang ; Lattimore et Szepesvári) |
| 12 · Préparation des données | M12a, M12b, M12c, M12d | §2.4–2.8 ; §3.2.2–3.2.3, §3.5–3.8, §9.4 ; §4.1–4.4 ; §4.5–4.7, §10.1–10.6 |
| 13 · Classifieurs | M13a, M13b | §8.3 ; §7.2–7.3, ch. 12 |
| 14 · Ensembles | M14 | — |
| 15 · scikit-learn | — (rien de nouveau) | — |
| 16 · Réseaux feed-forward | M16 | (§2.8, §6.4) |
| 17 · Fonctions d'activation | M17 | §5.3 |
| 18 · Rétropropagation | M18 | §5.4–5.6 |
| 19 · Optimiseurs | M19 | §5.7–5.8, §7.1 |
| 20 · Deep learning et premiers pas en PyTorch | M20 | — |
| 21 · Réseaux convolutifs (CNN) | M21 | — (Dumoulin et Visin ; Gray) |
| 22 · Réseaux récurrents (RNN, LSTM, GRU) | M22 | (§4.2, figure 4.4) (Trefethen et Embree ; Horn et Johnson) |
| 23 · PyTorch en pratique 1 : du dataset au modèle sauvegardé | — (rien de nouveau) | — |
| 24 · PyTorch en pratique 2 : améliorer, chercher, CNN et RNN | — (rien de nouveau) | — |
| 25 · Autoencodeurs et VAE | M25a, M25b | §6.5, fin de §6.7.2 (Théorème 6.16, Exemple 6.17), §9.3 (Bishop ; Murphy ; Cover et Thomas) ; §8.4–8.5 (8.5.2 en survol), §6.5.3 (Théorème 6.12), ch. 11 (§11.1–11.4 ; le §11.5 cité pour les singularités ; M25a en cite le Théorème 11.2 pour l'estimation de $\boldsymbol{\Sigma}$), §10.7 (10.7.1–10.7.3 ; §10.8 cité pour Tipping et Bishop) (MacKay ch. 22 et 33 ; Bishop ; Tipping et Bishop ; Mohamed et al. ; Cover et Thomas) |
| 26 · Apprentissage par renforcement | M26 | — : pas de MML, le livre ne traite pas les chaînes de Markov (Blitzstein et Hwang, ch. 9 et 11 ; Sutton et Barto, §3.5–3.6 et §4.1–4.4 ; Norris ; Levin et Peres ; Ferguson) |
| 27 · Réseaux antagonistes génératifs (GAN) | M27 | (§7.2, relu : l'inégalité minimax (7.23) et sa preuve (7.24), la dualité faible (7.27) lue comme un jeu ; §7.3.1 en option, le dual d'un programme linéaire) (Ferguson ; Peyré et Cuturi, ch. 2 et 3) |
| 28 · Applications créatives | M28 | — : pas de MML, le livre ne traite ni la variation totale, ni les fréquences, ni les troncatures, ni les itérations sur un ensemble fini ($\mathbf{A}^\top\mathbf{A}$, $\mathbf{A}\mathbf{A}^\top$ et la matrice de Gram d'un noyau, §4.5 et §12.4, ont été lus en M12d et M13b) (Borg et Groenen, ch. 12 ; Rudin, Osher et Fatemi ; Holtzman et coll. ; Knuth, vol. 2, §3.1) |
| 29 · Datasets et préparation du projet final | — (rien de nouveau) | — |
| B1 · Transfer learning et modèles pré-entraînés | — (rien de nouveau) | — |
| B2 · Tokenisation et embeddings | MB2 (bases 2 et 16 ; PMI, PPMI et lissage d'une marge ; SVD tronquée et ses deux facteurs ; modèle logistique d'une paire et décalage de $\ln K$ ; cosinus et analogies ; retrait d'une direction ; moyenne masquée et coût des paires) | — : pas de MML, le livre ne traite ni la PMI ni les embeddings (la SVD et Eckart-Young, §4.5–4.6, ont été lus en M12d) (Church et Hanks ; Bouma ; Prentice et Pyke ; King et Zeng ; Levy et Goldberg) |
| B3 · Attention et Transformers : un mini-GPT from scratch | MB3 (formules d'addition démontrées ; rotations du plan et de $\mathbb{R}^n$, rotations de Givens, matrices diagonales par blocs et permutations des coordonnées ; horloges d'une variable cyclique et direction moyenne ; moyenne pondérée par une softmax et estimateur de Nadaraya-Watson ; masques comme conditionnement et équivariance par permutation ; échelle des scores et saturation ; softmax en ligne et fusion de deux états ; mémoire de toutes les paires et calcul par blocs) | §3.9 (§3.9.1 avant le §2 de la fiche, §3.9.2–3.9.4 avant le §3 ; exercice 3.10 conseillé) ; pour les §4 à §9, la fiche est le cours (Nadaraya ; Watson ; Givens ; Mardia et Jupp ; Milakov et Gimelshein ; Knuth, vol. 1, §1.2.10) |
| B4 · LLM en pratique : Hugging Face, prompting, RAG et LoRA | MB4 (factorisation de rang, nombres stockés et nombres libres ; rang effectif, rang stable et ordre des produits ; poids d'un indice rare, de la surprise au log du rapport des cotes corrigé par ½ ; saturation et normalisation par la longueur, étudiées comme des fonctions ; fusion de classements, Borda et somme des $\frac{1}{c + \text{rang}}$ ; recall@$k$, precision@$k$, MRR et ligne de base d'un ordre tiré au hasard ; la température, le top-k et le top-p sont dans M28 §5, fait avant le ch. 28) | (§4.6, lu en M12d : à relire après le §1 de la fiche, avant le §2 ; §2.5, autour de (2.66), cité pour les colonnes pivots) ; pour les §1 et §3 à §6, la fiche est le cours (Strang et Moler ; Rudelson et Vershynin ; Gavish et Donoho ; Spärck Jones ; Robertson et Spärck Jones ; Croft et Harper ; Robertson et Zaragoza ; Michaelis et Menten ; Borda ; Cormack, Clarke et Büttcher ; Voorhees ; Manning, Raghavan et Schütze, ch. 6, 8 et 11) |
| B5 · Modèles de diffusion : un DDPM minimal | MB5 (récurrences linéaires gaussiennes, produits cumulés et loi stationnaire d'un processus autorégressif ; pont d'une marche aléatoire et couplages aux mêmes lois marginales ; rapport signal sur bruit, cotes et décibels, et cibles qui portent la même information ; la MSE et l'espérance conditionnelle ; score en $x$, formule de Tweedie, débruiteur optimal d'un mélange et dynamique de Langevin (aperçu) ; ELBO d'une chaîne de latents ; guidance comme produit de puissances de densités ; équations différentielles, méthodes d'Euler et du point milieu ; flow matching en dimension 1 ; la somme de gaussiennes indépendantes et le produit de deux densités gaussiennes sont dans M25a, la chaîne de Markov dans M26, la méthode d'Euler pour $x' = F(x)$ dans M20 §6) | (§6.5, lu en M25a : à relire, §6.5.3 et §6.5.1 avant les §1 et §2 de la fiche, §6.5.2 avant le §7 ; exercice 6.5 conseillé) ; pour le reste, la fiche est le cours (Kalman ; Shumway et Stoffer, ch. 3 ; Blitzstein et Hwang, ch. 9 ; Efron ; Süli et Mayers, ch. 12) |
| B6 · Explicabilité, équité et éthique | MB6 (jeux coopératifs : contributions marginales, valeur de Shapley par les ordres et par les poids des coalitions, estimation par des ordres tirés au hasard et Hoeffding ; vote pondéré et indice de Shapley-Shubik, partage de coûts et règle de l'aéroport ; quatre axiomes, jeux d'unanimité, dividendes de Harsanyi et unicité ; moyennes marginale et conditionnelle d'une fonction, courbes ICE et interactions ; intégrale d'un champ le long d'un chemin, théorème du gradient, partage d'une variation le long du segment ou par les chemins en escalier, fonctions multilinéaires et homogènes ; moyenne d'un gradient sur une grille, interpolation bilinéaire et deux conventions pour agrandir une grille ; corrélation de rangs de Spearman ; critères d'équité comme des indépendances, et ce qui est incompatible pour des décisions et pour des scores calibrés ; décision tirée au sort entre deux seuils, repondération, écart de deux proportions et bootstrap stratifié ; les taux par groupe, la calibration et la relation entre FPR, prévalence, precision et recall sont dans M03 §8, les rangs moyens dans MB4 §5, les rectangles, les trapèzes et Simpson dans M02a §5) | — : pas de MML, le livre ne traite ni les jeux coopératifs, ni les intégrales de chemin, ni l'équité (Shapley ; Shapley et Shubik ; Harsanyi ; Littlechild et Owen ; Osborne et Rubinstein, ch. 14 ; Aumann et Shapley ; Spearman ; Barocas, Hardt et Narayanan, ch. 3 ; Kleinberg, Mullainathan et Raghavan ; Hardt, Price et Srebro ; Kamiran et Calders ; Agresti et Caffo) |
| B7 · Du notebook à la production | — (rien de nouveau : la mesure d'une dérive, le PSI et la statistique de Kolmogorov-Smirnov sont dans M27 §10, fait avant le ch. 27) | — |
| B8 · RL moderne : DQN, gradient de politique, PPO et RLHF | MB8 | — |

Entre parenthèses, dans la dernière colonne : pas de lecture nouvelle, mais des sections déjà lues pour un chapitre précédent, à relire, ou ce que le chapitre prépare (« prérequis de §6.2 ») ; juste après une section, ce qu'on en lit (« fin de §6.7.2 (Théorème 6.16, Exemple 6.17) ») ; en fin de case, les autres lectures, livres et articles, détaillées dans `ressources.md` (« (Ferguson ; Peyré et Cuturi, ch. 2 et 3) ») ; « — » : pas de lecture de MML pour ce chapitre.

## 2. Pour chaque section de MML, le chapitre qui la couvre

Le livre se lit dans l'ordre de workbookIA, donc dans le désordre : cette table permet de vérifier qu'aucune section n'est oubliée.

| MML | Chapitre(s) |
|---|---|
| §2.1–2.3 Systèmes linéaires, matrices, résolution | M09a |
| §2.4–2.8 Espaces vectoriels, indépendance, base, rang, applications linéaires, espaces affines | M12a |
| §3.1, §3.2.1, §3.3–3.4 Normes, produit scalaire usuel, longueurs et distances, angles et orthogonalité | M07 |
| §3.2.2–3.2.3, §3.5–3.8 Produits scalaires généraux, bases orthonormées, complément orthogonal, produit scalaire de fonctions, projections | M12b |
| §3.9 Rotations | MB3 (§3.9.1 avant le §2 de la fiche, §3.9.2–3.9.4 avant le §3) |
| §4.1–4.4 Déterminant et trace, valeurs propres, Cholesky, diagonalisation | M12c (§4.2 relu en M22, avec sa figure 4.4) |
| §4.5–4.7 SVD, approximation de matrices, « phylogénie » des matrices | M12d (§4.6 relu en MB4, avant le §2 de sa fiche) |
| §5.1 Dérivation d'une variable (dont Taylor) | M05a (R7 en donne les bases, sans renvoyer au livre) |
| §5.2 Dérivées partielles et gradient | M05b |
| §5.3 Gradients de fonctions à valeurs vectorielles (jacobienne) | M17 |
| §5.4–5.6 Gradients de matrices, identités, rétropropagation et différentiation automatique | M09b (§5.5), M18 |
| §5.7–5.8 Dérivées d'ordre supérieur, Taylor multivariée | M19 |
| §6.1–6.2 Espace probabilisé, lois discrètes et continues | M02a (la partie continue de §6.2), M02b |
| §6.3 Règles de la somme et du produit, Bayes | M03, M04 |
| §6.4 Statistiques résumées et indépendance | M02b, M02c, M16 ; la remarque qui nomme la divergence KL, à la fin de §6.4.6 : M25a |
| §6.5 Loi gaussienne | M25a, sauf le Théorème 6.12 et la loi de la variance totale (§6.5.3), lus en M25b (et la loi normale en 1D : M02b) ; relu en MB5 (§6.5.3 et §6.5.1 avant les §1 et §2 de sa fiche, §6.5.2 avant le §7) |
| §6.6 Conjugaison et famille exponentielle | M04 |
| §6.7 Changement de variable | M02b (sauf la fin de §6.7.2), M25a (la fin de §6.7.2 : Théorème 6.16, Exemple 6.17) |
| §7.1 Descente de gradient | M19 |
| §7.2 Optimisation sous contraintes, multiplicateurs de Lagrange | M13b, M27 (relu : l'inégalité minimax (7.23) et sa preuve (7.24), la dualité faible (7.25)–(7.27) lue comme un jeu) |
| §7.3 Optimisation convexe | M13b (M27 relit le §7.3.1, *Linear Programming*, en option : le dual d'un programme linéaire, (7.39) à (7.43)) |
| §8.1–8.2 Données, modèles, minimisation du risque empirique | M09b |
| §8.3 Estimation des paramètres (maximum de vraisemblance, MAP) | M04, M13a |
| §8.4–8.5 Modélisation probabiliste, modèles graphiques orientés | M25b (8.4.1–8.4.3 et 8.5.1 ; la d-séparation de 8.5.2 en survol) |
| §8.6 Sélection de modèle | M08 |
| ch. 9 Régression linéaire | M09b (§9.1–9.2), M25a (§9.3), M12b (§9.4) |
| ch. 10 Analyse en composantes principales | M12d (§10.1–10.6), M25b (§10.7 ; le maximum de vraisemblance de Tipping et Bishop, (10.77)–(10.79), cité d'après le §10.8, *Further Reading*) |
| ch. 11 Mélanges de gaussiennes | M25b (§11.1–11.4 ; le §11.5, *Further Reading*, pour les singularités) (M25a cite le Théorème 11.2, §11.2.3, pour l'estimation de $\boldsymbol{\Sigma}$) |
| ch. 12 Machines à vecteurs de support | M10 (§12.1), M13b |

## 3. Les notions que MML ne couvre pas

| Notion | Chapitre | Ressource libre (voir `ressources.md`) |
|---|---|---|
| Remise à niveau du collège à la terminale | R0 à R9 | manuels Sésamath, Maths et tiques, Khan Academy |
| Limites, intégrales | R7, M02a | Exo7, Maths et tiques |
| Théorèmes limites, estimation, tests | M02c, M08 | Blitzstein et Hwang, OpenIntro Statistics |
| Logique, inégalités de concentration, bandits | M11 | Hammack, Blitzstein et Hwang, Lattimore et Szepesvári |
| Théorie de l'information | M06 | MacKay |
| Chaînes de Markov (matrice de transition, loi à $n$ pas, loi stationnaire, PageRank), propriété de la tour et analyse au premier pas, retour actualisé et équation de Bellman d'une politique fixée, contraction et itérations, arrêt optimal, erreur TD et biais du maximum | M26 | Blitzstein et Hwang (ch. 9 et 11), Norris (ch. 1), Levin et Peres (ch. 4 et 12), Sutton et Barto (§3.5–3.6, §4.1–4.4), Ferguson (ch. 3 et 4), documentations de NumPy et de SciPy (`numpy.random.Generator.choice`, `numpy.random.Generator.geometric`, `numpy.linalg.eig`, `scipy.linalg.null_space`) |
| Convolution, matrices de Toeplitz et circulantes | M21 | Dumoulin et Visin, Gray, documentations de NumPy et de SciPy |
| Récurrences linéaires avec entrée, rayon spectral d'une matrice quelconque, croissance transitoire, normes induites, produits de matrices différentes | M22 | Trefethen et Embree, Horn et Johnson, Furstenberg et Kesten, documentations de NumPy et de SciPy |
| Masse d'une ellipse et loi de la norme d'un vecteur gaussien (khi-deux, khi), divergence KL continue, Jensen pour une variable à densité, entropie différentielle, interpolation sphérique (slerp) | M25a | Cover et Thomas (ch. 2 et 8), documentation de SciPy (`scipy.stats.chi2`, `scipy.stats.chi`, `scipy.spatial.transform.Slerp`) |
| ELBO démontrée en général et EM comme montée par coordonnées (MML s'arrête à $Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(t)})$), angles principaux entre deux sous-espaces, sens de la KL et inférence amortie, dérivée par le chemin (et la méthode du score, nommée), β comme multiplicateur d'un budget d'information, posterior agrégé, information mutuelle continue et débit-distorsion | M25b | MacKay (ch. 22 et 33), Bishop (ch. 9, §10.1, §12.2), Tipping et Bishop, Mohamed et al., Cover et Thomas (ch. 8 et 10), documentations de SciPy et de scikit-learn (`scipy.linalg.subspace_angles`, `sklearn.mixture.GaussianMixture`) |
| Jeux à deux joueurs (stratégies mixtes, principe d'indifférence, théorème minimax de von Neumann, équilibre de Nash, induction arrière), descente-montée sur un jeu bilinéaire, couplages et transport optimal, distances de Wasserstein (dimension 1, couplage des quantiles, gaussiennes, distance de Fréchet), biais d'une distance estimée, mesures d'une dérive (PSI, Kolmogorov-Smirnov) | M27 | Ferguson (*Game Theory*, parties I à III), Peyré et Cuturi (ch. 2 et 3), documentations de SciPy et de NumPy (`scipy.optimize.linprog`, `scipy.stats.ks_2samp`, `scipy.special.rel_entr`, `scipy.stats.norm`) |
| Configuration de points retrouvée à partir de distances (double centrage, positionnement multidimensionnel classique, matrices de distances euclidiennes), montée sur l'entrée d'une fonction à paramètres fixés (pas normalisés, montée projetée sur un pavé, coordonnées gelées), variation totale d'une grille et laplacien d'un graphe, fréquences spatiales (repliement, fréquence de Nyquist, gain d'un flou), température et troncatures d'une loi (top-k, top-p, coût en divergence KL), suites ultimement périodiques et détection de cycle | M28 | Borg et Groenen (ch. 12), Rudin, Osher et Fatemi, Holtzman et coll. (§3), Knuth (vol. 2, §3.1, exercice 6), documentations de NumPy et de SciPy (`numpy.meshgrid`, `scipy.linalg.orthogonal_procrustes`, `scipy.stats.entropy`) |
| Bases 2 et 16 (octets, couleurs, champs de bits), information mutuelle ponctuelle (PMI, PPMI, lift d'une règle d'association, borne des événements rares, PMI normalisée), lissage d'une marge par une loi tempérée, répartition des valeurs singulières d'une SVD tronquée entre deux facteurs, étude cas-témoins et correction de l'ordonnée à l'origine, géométrie des analogies (parallélogramme, borne du cosinus), retrait d'une direction et premier axe de différences, moyenne masquée et coût des comparaisons par paires | MB2 | Church et Hanks, Bouma, Prentice et Pyke, King et Zeng (§4.1), Levy et Goldberg, documentations de Python et de SciPy (fonctions natives `bin`, `hex`, `int` ; `scipy.sparse`, `scipy.sparse.linalg.svds`) |
| Démonstration des formules d'addition par le produit scalaire, horloges d'une variable cyclique (décalage comme rotation, produit scalaire de plusieurs horloges, direction moyenne), moyenne pondérée par une softmax et estimateur de Nadaraya-Watson (largeur de bande, validation croisée « un de côté »), masques comme conditionnement et filtre causal, équivariance par permutation, saturation d'une softmax, softmax en ligne (invariant, fusion associative, records et nombres harmoniques), mémoire d'une matrice $n \times n$ et calcul par blocs | MB3 | Nadaraya, Watson, Mardia et Jupp, Milakov et Gimelshein, Knuth (vol. 1, §1.2.10), documentations de NumPy, de SciPy, de scikit-learn et de pandas (`numpy.arctan2`, `scipy.stats.circmean`, `scipy.spatial.transform.Rotation`, `scipy.special.logsumexp`, `scipy.spatial.distance.cdist`, `sklearn.metrics.pairwise_distances_chunked`, `pandas.Series.ewm`) |
| Factorisation de rang (factorisation CR, non-unicité à une matrice inversible près, nombres libres), rang effectif et rang stable d'une matrice mesurée, niveau du bruit, poids d'un indice rare (surprise, log du rapport des cotes de Robertson et Spärck Jones, correction ½, cas sans information de pertinence), saturation et normalisation par la longueur, fusion de classements (Borda, somme des $\frac{1}{c + \text{rang}}$, invariance par une transformation croissante des notes), recall@$k$, precision@$k$, taux de succès et MRR, ligne de base d'un ordre tiré au hasard et loi du premier pertinent | MB4 | Strang et Moler, Rudelson et Vershynin, Gavish et Donoho, Spärck Jones, Robertson et Spärck Jones, Croft et Harper, Robertson et Zaragoza, Michaelis et Menten, Borda, Cormack, Clarke et Büttcher, Voorhees, Manning, Raghavan et Schütze (ch. 6, 8 et 11), documentations de NumPy, de SciPy et de scikit-learn (`scipy.linalg.qr`, `numpy.linalg.matrix_rank`, `numpy.linalg.multi_dot`, `scipy.stats.contingency.odds_ratio`, `scipy.stats.rankdata`, `sklearn.metrics.top_k_accuracy_score`) |
| Récurrences linéaires gaussiennes à coefficients quelconques (pas de prédiction d'un filtre de Kalman), produits cumulés et survie à des risques successifs (encadrement par deux exponentielles), loi stationnaire d'un processus autorégressif d'ordre 1, pont d'une marche aléatoire, couplages aux mêmes lois marginales et nombres aléatoires communs, rapport signal sur bruit (cote, logit, décibels) et changement de cible, la MSE et l'espérance conditionnelle (et la médiane conditionnelle pour la MAE), score en $x$, formule de Tweedie et biais du maximum (le biais de sélection d'Efron), débruiteur optimal d'un mélange et d'un nuage de points, dynamique de Langevin (aperçu), ELBO d'une chaîne de latents, guidance comme produit de puissances de densités, équations différentielles (Cauchy-Lipschitz, méthodes d'Euler et du point milieu, ordre de l'erreur), flow matching en dimension 1 | MB5 | Kalman, Shumway et Stoffer (ch. 3), Blitzstein et Hwang (ch. 9), Efron, Süli et Mayers (ch. 12), documentations de SciPy et de scikit-learn (`scipy.integrate.solve_ivp`, `scipy.integrate.odeint`, `scipy.integrate.quad`, `sklearn.tree.DecisionTreeRegressor`) |
| Jeux coopératifs (contributions marginales, valeur de Shapley par les ordres et par les poids des coalitions, estimation par des ordres tirés au hasard, vote pondéré et indice de Shapley-Shubik, jeu de l'aéroport, quatre axiomes, jeux d'unanimité, dividendes de Harsanyi et unicité), moyennes marginale et conditionnelle d'une fonction et courbes ICE, intégrale d'un champ le long d'un chemin et théorème du gradient, partage d'une variation (le long du segment, par les chemins en escalier ; fonctions multilinéaires et homogènes, identité d'Euler), moyenne d'un gradient sur une grille et interpolation bilinéaire (centres ou coins alignés), corrélation de rangs de Spearman, critères d'équité comme des indépendances (indépendance, séparation, suffisance) et leurs impossibilités (indépendance et séparation, scores calibrés), décision tirée au sort entre deux seuils, repondération, écart de deux proportions et bootstrap stratifié | MB6 | Shapley, Shapley et Shubik, Harsanyi, Littlechild et Owen, Osborne et Rubinstein (ch. 14), Aumann et Shapley, Spearman, Barocas, Hardt et Narayanan (ch. 3), Kleinberg, Mullainathan et Raghavan, Hardt, Price et Srebro, Kamiran et Calders, Agresti et Caffo, documentations de SciPy (`scipy.stats.spearmanr`, `scipy.ndimage.zoom`, `scipy.integrate.quad`) |
| Démonstrations | R4 et suite | Hammack, *Book of Proof* |
