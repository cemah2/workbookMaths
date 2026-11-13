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
| 25 · Autoencodeurs et VAE | M25a, M25b | §6.5, fin de §6.7.2 (Théorème 6.16, Exemple 6.17), §9.3 (Bishop ; Murphy ; Cover et Thomas) ; §8.4–8.5, §10.7, ch. 11 (dont le Théorème 11.2, que M25a cite pour l'estimation de $\boldsymbol{\Sigma}$) |
| 26 · Apprentissage par renforcement | M26 | — (Blitzstein et Hwang) |
| 27 · Réseaux antagonistes génératifs (GAN) | M27 | §7.2 (relu) |
| 28 · Applications créatives | M28 | — |
| 29 · Datasets et préparation du projet final | — (rien de nouveau) | — |
| B1 · Transfer learning et modèles pré-entraînés | — (rien de nouveau) | — |
| B2 · Tokenisation et embeddings | MB2 | — |
| B3 · Attention et Transformers : un mini-GPT from scratch | MB3 | §3.9 |
| B4 · LLM en pratique : Hugging Face, prompting, RAG et LoRA | MB4 | (§4.6) |
| B5 · Modèles de diffusion : un DDPM minimal | MB5 | (§6.5) |
| B6 · Explicabilité, équité et éthique | MB6 | — |
| B7 · Du notebook à la production | — (rien de nouveau) | — |
| B8 · RL moderne : DQN, gradient de politique, PPO et RLHF | MB8 | — |

Entre parenthèses, dans la dernière colonne : pas de lecture nouvelle, mais des sections déjà lues pour un chapitre précédent, à relire, ou ce que le chapitre prépare (« prérequis de §6.2 ») ; « — » : pas de lecture de MML pour ce chapitre.

## 2. Pour chaque section de MML, le chapitre qui la couvre

Le livre se lit dans l'ordre de workbookIA, donc dans le désordre : cette table permet de vérifier qu'aucune section n'est oubliée.

| MML | Chapitre(s) |
|---|---|
| §2.1–2.3 Systèmes linéaires, matrices, résolution | M09a |
| §2.4–2.8 Espaces vectoriels, indépendance, base, rang, applications linéaires, espaces affines | M12a |
| §3.1, §3.2.1, §3.3–3.4 Normes, produit scalaire usuel, longueurs et distances, angles et orthogonalité | M07 |
| §3.2.2–3.2.3, §3.5–3.8 Produits scalaires généraux, bases orthonormées, complément orthogonal, produit scalaire de fonctions, projections | M12b |
| §3.9 Rotations | MB3 |
| §4.1–4.4 Déterminant et trace, valeurs propres, Cholesky, diagonalisation | M12c (§4.2 relu en M22, avec sa figure 4.4) |
| §4.5–4.7 SVD, approximation de matrices, « phylogénie » des matrices | M12d |
| §5.1 Dérivation d'une variable (dont Taylor) | M05a (R7 en donne les bases, sans renvoyer au livre) |
| §5.2 Dérivées partielles et gradient | M05b |
| §5.3 Gradients de fonctions à valeurs vectorielles (jacobienne) | M17 |
| §5.4–5.6 Gradients de matrices, identités, rétropropagation et différentiation automatique | M09b (§5.5), M18 |
| §5.7–5.8 Dérivées d'ordre supérieur, Taylor multivariée | M19 |
| §6.1–6.2 Espace probabilisé, lois discrètes et continues | M02a (la partie continue de §6.2), M02b |
| §6.3 Règles de la somme et du produit, Bayes | M03, M04 |
| §6.4 Statistiques résumées et indépendance | M02b, M02c, M16 ; la remarque qui nomme la divergence KL, à la fin de §6.4.6 : M25a |
| §6.5 Loi gaussienne | M25a, sauf le Théorème 6.12 et la loi de la variance totale (§6.5.3), lus en M25b (et la loi normale en 1D : M02b) |
| §6.6 Conjugaison et famille exponentielle | M04 |
| §6.7 Changement de variable | M02b (sauf la fin de §6.7.2), M25a (la fin de §6.7.2 : Théorème 6.16, Exemple 6.17) |
| §7.1 Descente de gradient | M19 |
| §7.2 Optimisation sous contraintes, multiplicateurs de Lagrange | M13b, M27 (l'inégalité minimax) |
| §7.3 Optimisation convexe | M13b |
| §8.1–8.2 Données, modèles, minimisation du risque empirique | M09b |
| §8.3 Estimation des paramètres (maximum de vraisemblance, MAP) | M04, M13a |
| §8.4–8.5 Modélisation probabiliste, modèles graphiques orientés | M25b |
| §8.6 Sélection de modèle | M08 |
| ch. 9 Régression linéaire | M09b (§9.1–9.2), M25a (§9.3), M12b (§9.4) |
| ch. 10 Analyse en composantes principales | M12d (§10.1–10.6), M25b (§10.7) |
| ch. 11 Mélanges de gaussiennes | M25b (M25a cite le Théorème 11.2, §11.2.3, pour l'estimation de $\boldsymbol{\Sigma}$) |
| ch. 12 Machines à vecteurs de support | M10 (§12.1), M13b |

## 3. Les notions que MML ne couvre pas

| Notion | Chapitre | Ressource libre (voir `ressources.md`) |
|---|---|---|
| Remise à niveau du collège à la terminale | R0 à R9 | manuels Sésamath, Maths et tiques, Khan Academy |
| Limites, intégrales | R7, M02a | Exo7, Maths et tiques |
| Théorèmes limites, estimation, tests | M02c, M08 | Blitzstein et Hwang, OpenIntro Statistics |
| Logique, inégalités de concentration, bandits | M11 | Hammack, Blitzstein et Hwang, Lattimore et Szepesvári |
| Théorie de l'information | M06 | MacKay |
| Chaînes de Markov | M26 | Blitzstein et Hwang |
| Convolution, matrices de Toeplitz et circulantes | M21 | Dumoulin et Visin, Gray, documentations de NumPy et de SciPy |
| Récurrences linéaires avec entrée, rayon spectral d'une matrice quelconque, croissance transitoire, normes induites, produits de matrices différentes | M22 | Trefethen et Embree, Horn et Johnson, Furstenberg et Kesten, documentations de NumPy et de SciPy |
| Masse d'une ellipse et loi de la norme d'un vecteur gaussien (khi-deux, khi), divergence KL continue, Jensen pour une variable à densité, entropie différentielle, interpolation sphérique (slerp) | M25a | Cover et Thomas (ch. 2 et 8), documentation de SciPy (`scipy.stats.chi2`, `scipy.stats.chi`, `scipy.spatial.transform.Slerp`) |
| Démonstrations | R4 et suite | Hammack, *Book of Proof* |
