# Couverture des notions de workbookIA

*Généré par `python tools/syllabus.py build` : ne pas modifier à la main.*

Pour chaque chapitre de workbookIA, ses notions mathématiques et le chapitre de maths qui les enseigne **avant** lui dans l'ordre de travail commun (`syllabus.py check` le vérifie). Les notions de workbookIA sont lues dans une copie figée (`docs/syllabus/workbookia_notions.json`, commit ff7a37c). « Enseignée » veut dire : le chapitre de maths donne les outils dont la notion a besoin ; les démonstrations du chapitre de workbookIA restent les siennes (règle de partage, BIBLE §8 : la liste « Frontières » de chaque chapitre dans `docs/SYLLABUS.md`). Les notions sans chapitre de maths sont jugées non mathématiques (outils, pratique, vocabulaire du ML) : elles sont listées pour relecture.

**Bilan** : 347 notions mathématiques couvertes, 211 notions non mathématiques.

## workbookIA 0A · Python, notebooks et outils

Non mathématiques : Colab / Jupyter : cellules, Markdown, noyau, « Tout exécuter » · terminal : cd, chemins, lancer python et pytest · variables et types, f-strings · listes, tuples, dictionnaires, ensembles, collections.Counter · if/for/while, enumerate, zip, compréhensions · fonctions, valeurs par défaut, portée · *args, **kwargs, arguments keyword-only · lambda, fonctions en argument, Callable · fermetures (closures) · docstrings au format NumPy, annotations de type · modules et imports · exceptions (raise, try/except), lecture d'un traceback · fichiers texte, pathlib · json, pickle · expressions régulières (re) : bases · itertools, heapq (aperçu) · classes : __init__, attributs, méthodes · méthodes spéciales : __repr__, __len__, __getitem__, __call__, surcharge d'opérateurs (__add__, __radd__, __mul__, __eq__) · héritage et super() · itérables et générateurs (yield) · NumPy : arrays, dtype, shape, indexation, masques, vues/copies · NumPy : calcul vectorisé, broadcasting, réductions par axe, tri, argmax, unique · NumPy : reshape, transpose, empilement · np.random.default_rng, graine, permutation, choice · images en arrays (N, H, W), (N, C, H, W) · pandas : read_csv, head, info, describe, loc, iloc, filtres, isna, dropna, fillna, duplicated, value_counts, groupby, to_numpy · matplotlib : plot, scatter, hist, subplots, imshow, légendes ; wb.plot.show_images · git : clone, status, add, commit, push, pull --rebase, .gitignore, branches (aperçu) · pytest : assert, approx, raises, parametrize ; doctest · workbook : wb.check, wb.attempt, start_chapter.py, mylearn · mini-batches : iterate_minibatches, drop_last · one-hot, argmax, comptage de valeurs · récursivité · dataclasses (@dataclass)

## workbookIA 0B · Maths du lycée au ML

| Notion de workbookIA | Enseignée dans |
|---|---|
| puissances, racines, notation scientifique, ordres de grandeur | R1 |
| valeur absolue, inégalités, partie entière ⌊x⌋ et ⌈x⌉, fonction signe | R1, R2 |
| notations Σ et Π | R4 |
| moyenne pondérée, somme pondérée, moyenne mobile | R1, R5 |
| suites géométriques et leur somme (finie et infinie) | R5 |
| ensembles : union, intersection, complémentaire, cardinal | R4 |
| dénombrement, factorielle, coefficient binomial C(n, k) | R8 |
| fonctions affines et polynômes | R3 |
| exponentielle et logarithmes (ln, log₂, log₁₀), changement de base, bits et nats | R6 |
| sigmoïde et tanh : définitions, allure, symétries | R6 |
| cosinus (aperçu) | R9 |
| composition de fonctions | R3 |
| vecteurs : somme, produit par un scalaire, norme (L1, L2, L∞), distance euclidienne | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en R9, M07 |
| produit scalaire, similarité cosinus | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en R9, M07 |
| produit de Hadamard | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en M09a |
| matrices : forme, transposée, produit matrice-vecteur, produit matriciel, vérification des formes | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en M09a |
| matrice identité, inverse 2 × 2, système linéaire (idée) | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en R2, M09a |
| dérivée, taux d'accroissement, tangente | R7 |
| dérivées usuelles (puissances, exp, ln) et règles (somme, produit, quotient) | R7 |
| règle de la chaîne | R7 |
| variations, minimum et maximum (dérivée nulle) | R7 |
| fonctions de deux variables, lignes de niveau (lecture) | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en M05b |
| dérivées partielles, gradient, pas de descente | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en M05b |
| règle de la chaîne à plusieurs variables (somme sur les chemins, version simple) | workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en M17, M18 |
| probabilités : événement, complémentaire, union, indépendance | R8 |
| variable aléatoire discrète, espérance, variance, écart-type, linéarité de l'espérance | R8 |
| simulation et loi des grands nombres (intuition) | R8 |
| LaTeX dans Markdown | R0 |

Non mathématiques : mylearn.linalg_basics

## workbookIA 1 · Introduction au machine learning et au deep learning

Non mathématiques : vocabulaire du machine learning · boucle d'entraînement · learning rate · généralisation · jeu de test · familles d'apprentissage · fils rouges du workbook · panorama 2026

## workbookIA 2 · Hasard et statistiques de base

| Notion de workbookIA | Enseignée dans |
|---|---|
| statistiques descriptives | M02c |
| variance et ddof | M02c |
| percentiles | M02a, M02c |
| z-score | M02c |
| lois usuelles | M02b |
| espérance | M02b |
| i.i.d. | M02c |
| échantillonnage avec ou sans remise | M02c |
| tirage catégoriel | M02b |
| bootstrap | M02c |
| intervalle de confiance | M02c |
| grande dimension | M02c |
| covariance | M02c |
| corrélation | M02c |
| matrice de covariance | M02c |
| matrice de corrélation | M02c |

Non mathématiques : reproductibilité (graine)

## workbookIA 3 · Probabilités et mesure de la qualité

| Notion de workbookIA | Enseignée dans |
|---|---|
| matrice de confusion | M03 |
| MCC | M02c, M03 |
| balanced accuracy | M03 |
| seuil de décision | M03 |
| probabilité conditionnelle | M03 |
| probabilité jointe | M03 |
| probabilité marginale | M03 |
| table de contingence | M03 |
| accuracy | M03 |
| precision | M03 |
| recall | M03 |
| spécificité | M03 |
| F1 | R1, M03 |
| F-beta | M03 |
| moyennes macro/micro/pondérée | R1, M03 |
| prévalence (base rate) | M03 |
| courbe ROC | M03 |
| AUC | M02a, M03 |
| courbe precision-recall | M03 |
| average precision | M03 |
| calibration | M03 |
| score de Brier | M03 |

## workbookIA 4 · Règle de Bayes

| Notion de workbookIA | Enseignée dans |
|---|---|
| règle de Bayes | M04 |
| prior | M04 |
| vraisemblance | M04 |
| évidence | M04 |
| posterior | M04 |
| mise à jour séquentielle | M04 |
| hypothèses multiples | M04 |
| log-probabilités | R6, M04 |
| underflow | R6, M04 |
| loi Beta (intuition) | M04 |
| MAP | M04 |
| intervalle de crédibilité | M04 |
| fréquentisme contre bayésianisme | M04 |

## workbookIA 5 · Courbes et surfaces

| Notion de workbookIA | Enseignée dans |
|---|---|
| learning rate | M05b |
| dérivée numérique | R7, M05a |
| différence centrée | M05a |
| choix du pas h | M05a |
| dérivée seconde | M05a |
| extrema locaux et globaux | M05a |
| gradient numérique | M05b |
| descente de gradient | M05b |
| montée de gradient | M05b |
| points critiques | M05b |
| point selle | M05b |
| lignes de niveau | M05b |

Non mathématiques : autograd (aperçu)

## workbookIA 6 · Théorie de l'information

| Notion de workbookIA | Enseignée dans |
|---|---|
| information de Shannon | M06 |
| bits et nats | R6, M06 |
| codes de longueur fixe | M06 |
| codes adaptatifs | M06 |
| code de Huffman | M06 |
| entropie | M06 |
| cross-entropy | M06 |
| divergence KL | M06 |
| divergence de Jensen-Shannon | M06 |
| lissage de Laplace | M04 |
| log loss | M06 |
| perplexité | M06 |
| entropie conditionnelle | M06 |

## workbookIA 7 · Classification

| Notion de workbookIA | Enseignée dans |
|---|---|
| k-means++ | M02b, M07 |
| frontière de décision | M07 |
| classifieur du centroïde le plus proche | M07 |
| k-means (Lloyd) | M07 |
| inertie | M07 |
| coefficient de silhouette | M07 |
| malédiction de la dimension | M07 |
| concentration des distances | M07 |
| un-contre-un (OvO) | R8 |

Non mathématiques : classification binaire et multi-classe · politique de seuil · un-contre-tous (OvR) · DBSCAN et HDBSCAN (usage)

## workbookIA 8 · Entraînement et test

| Notion de workbookIA | Enseignée dans |
|---|---|
| erreur type d'un score | M02c, M08 |
| test par permutation | M08 |
| p-valeur | M08 |
| validation croisée k-fold | M08 |

Non mathématiques : boucle d'entraînement · epoch · raccourcis appris · jeu de test · fuite de données · jeu de validation · recherche d'hyperparamètres · k-fold stratifiée · clone · cross_val_score · GroupKFold et TimeSeriesSplit (usage)

## workbookIA 9 · Overfitting et underfitting

| Notion de workbookIA | Enseignée dans |
|---|---|
| overfitting | M09b |
| underfitting | M09b |
| régularisation L2 (Ridge) | M09b |
| régularisation L1 (Lasso) | M09b |
| seuillage doux | M09b |
| moindres carrés | M09b |
| MAE | M09b |
| R² | M09b |
| features polynomiales | R3, M09b |
| décomposition biais-variance | M09b |
| ajustement bayésien d'une droite | M04, M09b |
| double descente | M09b |

Non mathématiques : courbes de validation · courbes d'apprentissage · early stopping (patience)

## workbookIA 10 · Neurones

| Notion de workbookIA | Enseignée dans |
|---|---|
| fonction d'activation | R3, R6 |
| biais | M07 |
| convention des poids | M07, M09a |
| neurone artificiel | M07 |
| perceptron | M10 |
| règle d'apprentissage du perceptron | M10 |
| séparabilité linéaire | M10 |
| XOR | M10 |
| astuce du biais | M10 |
| théorème de convergence du perceptron | M10 |

Non mathématiques : neurone biologique (modèle simplifié)

## workbookIA 11 · Apprentissage et raisonnement

| Notion de workbookIA | Enseignée dans |
|---|---|
| déduction | R4, M11 |
| induction | M11 |
| syllogismes | M11 |
| validité et solidité | M11 |
| sophismes syllogistiques | M11 |
| sophismes inductifs | M11 |
| biais d'échantillonnage | M02c |
| bandit manchot | M11 |
| ε-greedy | M11 |
| UCB | M11 |
| échantillonnage de Thompson | M04, M11 |
| regret | M11 |
| moyenne incrémentale | R4, R5 |

Non mathématiques : représentation, évaluation, optimisation · No Free Lunch · conditionnement opérant

## workbookIA 12 · Préparation des données

| Notion de workbookIA | Enseignée dans |
|---|---|
| valeurs aberrantes | M02c |
| imputation | M02c |
| sélection de features | M02c, M06 |
| one-hot encoding | M07 |
| samplewise/featurewise/elementwise | M09a |
| UMAP | M12d |
| standardisation | M02c |
| normalisation min-max | R3 |
| PCA | M12d |
| variance expliquée | M12d |
| whitening | M12c |
| transformation inverse | M12a |
| matrice de covariance | M12c |
| t-SNE | M06, M12d |

Non mathématiques : encodage ordinal · fuite de données · dates avec pandas (to_datetime, dt) · merge et pivot_table · SQL de base (sqlite3, pd.read_sql)

## workbookIA 13 · Classifieurs

| Notion de workbookIA | Enseignée dans |
|---|---|
| arbre de décision | M13a |
| arbre de régression | M02c, M13a |
| kNN | M07 |
| distances | M07 |
| SVM | M13b |
| marge | M13b |
| noyau RBF | M13b |
| astuce du noyau | M13b |
| Gini | M13a |
| entropie | M06, M13a |
| gain d'information | M13a |
| Naïve Bayes | M13a |
| lissage de Laplace | M04 |
| logsumexp | M05a |
| régression logistique | M13a |
| sigmoïde | R6, M13a |
| log-loss | M13a |
| TF-IDF (TfidfVectorizer) | R6 |

Non mathématiques : élagage · paramétrique vs non paramétrique

## workbookIA 14 · Ensembles

| Notion de workbookIA | Enseignée dans |
|---|---|
| forêt aléatoire | M14 |
| vote pondéré | M14 |
| vote souple | M14 |
| bootstrap | M02c, M14 |
| out-of-bag | M14 |
| bagging | M14 |
| AdaBoost | M14 |
| SAMME | M14 |
| gradient boosting | M14 |
| learning rate (boosting) | M14 |
| importance par permutation | M08 |

Non mathématiques : ensemble · ExtraTrees · souche · early stopping (boosting) · XGBoost · LightGBM · HistGradientBoosting · stacking

## workbookIA 15 · scikit-learn

| Notion de workbookIA | Enseignée dans |
|---|---|
| PolynomialFeatures | M09b |
| classes déséquilibrées : class_weight, rééchantillonnage | M03 |
| seuil de décision | M03 |
| predict_proba | R6, M13a |
| silhouette | M07 |

Non mathématiques : API scikit-learn · get_params/set_params/clone · decision_function · cross_validate · StratifiedKFold · GridSearchCV · RandomizedSearchCV · cv_results_ · Pipeline · ColumnTransformer · set_output · DecisionBoundaryDisplay · persistance joblib · lecture de dépréciations

## workbookIA 16 · Réseaux feed-forward

| Notion de workbookIA | Enseignée dans |
|---|---|
| réseau feed-forward / MLP | M16 |
| graphe orienté acyclique | M16 |
| ordre topologique | M16 |
| passe avant matricielle | M09a, M16 |
| convention W (n_in, n_out) | M09a, M16 |
| comptage des paramètres | M16 |
| initialisation des poids (LeCun, Glorot, He) | M02b, M16 |
| brisure de symétrie | M05b |
| conservation de la variance | M16 |
| fan-in / fan-out | M16 |

Non mathématiques : flux synchrone et asynchrone

## workbookIA 17 · Fonctions d'activation

| Notion de workbookIA | Enseignée dans |
|---|---|
| rôle de la non-linéarité | M12a, M16 |
| activations linéaires par morceaux (ReLU et variantes, maxout) | M13b, M17 |
| activations lisses (softplus, ELU, sigmoïde, tanh, SiLU, GELU) | R6, M02b, M13a, M17 |
| dérivées des activations | R7, M17 |
| saturation et neurones morts | M17 |
| softmax, log-softmax, température | M05a, M17 |
| Jacobienne de la softmax | M17 |
| stabilité numérique (log-sum-exp) | M05a |

Non mathématiques : tests paramétrés pytest

## workbookIA 18 · Rétropropagation

| Notion de workbookIA | Enseignée dans |
|---|---|
| saturation et neurones morts | M17 |
| learning rate | M05b |
| rétropropagation | M18 |
| delta d'un neurone | M17, M18 |
| règle de la chaîne multivariée | M17, M18 |
| forme matricielle des gradients | M18 |
| losses et leurs gradients (MSE, BCE sur logits, cross-entropy softmax) | M05a, M09b, M13a, M14 |
| vérification du gradient | M05a, M18 |
| mini-batches | M18 |
| différentiation automatique en mode inverse | M18 |
| micro-autograd (Value) | M18 |

Non mathématiques : boucle d'entraînement from scratch

## workbookIA 19 · Optimiseurs

| Notion de workbookIA | Enseignée dans |
|---|---|
| choix d'un optimiseur | M19 |
| géométrie de la surface d'erreur | M05b, M12c, M19 |
| learning rate critique | M19 |
| plannings de learning rate | R1, R5, R9 |
| batch / stochastique / mini-batch | M19 |
| momentum | R5, M19 |
| Nesterov | M19 |
| Adagrad | M19 |
| RMSprop | R5, M19 |
| Adadelta | R5, M19 |
| Adam | R5, M19 |
| AdamW (weight decay découplé) | M09b, M14 |
| warmup + cosinus | R9 |
| gradient clipping | M07, M19 |

## workbookIA 20 · Deep learning et premiers pas en PyTorch

| Notion de workbookIA | Enseignée dans |
|---|---|
| tenseurs PyTorch | M20 |
| dropout | M06, M20 |
| batchnorm | M02c, M20 |
| layer norm | M02c, M20 |
| pénalité L2 et weight decay | M09b |
| connexions résiduelles | M20 |

Non mathématiques : architecture d'un réseau profond · autograd PyTorch · nn.Module · Dataset / DataLoader · boucle d'entraînement PyTorch · device (CPU/GPU) · early stopping · survey des couches (conv, pooling, RNN, utilitaires) · modèle pré-entraîné torchvision · sauvegarde et reproductibilité · explicabilité et dérive

## workbookIA 21 · Réseaux convolutifs (CNN)

| Notion de workbookIA | Enseignée dans |
|---|---|
| convolution 2D (corrélation croisée) | M21 |
| padding, stride, dilatation, groupes | M21 |
| im2col | M21 |
| max et average pooling | M21 |
| convolution transposée | M21 |
| rétropropagation d'une convolution | M17, M18, M21 |
| champ récepteur | M21 |
| attaque adversariale FGSM | M18, M21 |
| visualisation de filtres et de cartes d'activation | M05b, M18 |

Non mathématiques : CNN PyTorch (nn.Conv2d, nn.MaxPool2d)

## workbookIA 22 · Réseaux récurrents (RNN, LSTM, GRU)

| Notion de workbookIA | Enseignée dans |
|---|---|
| LSTM et GRU (ordre des portes PyTorch) | M09a, M17, M22 |
| cellule RNN et BPTT | M16, M18, M22 |
| gradient évanescent et clipping | M19, M22 |
| génération de texte avec température | M02b, M17 |
| perplexité | M06 |

Non mathématiques : fenêtres de séries temporelles · vocabulaire caractères/mots, encodage · nn.RNN, nn.LSTM, nn.GRU · prévision de série temporelle avec baseline · CNN-LSTM

## workbookIA 23 · PyTorch en pratique 1 : du dataset au modèle sauvegardé

| Notion de workbookIA | Enseignée dans |
|---|---|
| CrossEntropyLoss et logits | M06, M13a, M17 |
| schedulers de learning rate | R1, R5, R9 |

Non mathématiques : workflow PyTorch complet · Dataset, DataLoader, transforms · normalisation et découpage stratifié · nn.Sequential, nn.Flatten, nn.Linear · fonction fit() avec historique · analyse d'erreurs · inférence avec eval et inference_mode · state_dict et checkpoints · modèle pré-entraîné torchvision · early stopping et meilleur checkpoint · fiche modèle

## workbookIA 24 · PyTorch en pratique 2 : améliorer, chercher, CNN et RNN

| Notion de workbookIA | Enseignée dans |
|---|---|
| dropout et max-norm en PyTorch | M07, M19, M20 |
| nn.Conv2d, nn.MaxPool2d, nn.BatchNorm2d | M20, M21 |
| sorties de nn.LSTM et état porté | M22 |
| LSTM pour séries (fenêtres, scaler, RMSE) | M09b |

Non mathématiques : démarche expérimentale et journal d'expériences · estimateur scikit-learn autour d'un réseau PyTorch · validation croisée et recherche d'hyperparamètres · torchvision.transforms.v2 · Dataset généré à la volée · génération de texte par caractère et par mot · forward() avec branches et bloc résiduel · précision mixte et torch.compile

## workbookIA 25 · Autoencodeurs et VAE

| Notion de workbookIA | Enseignée dans |
|---|---|
| autoencodeur (encodeur, décodeur, goulot) | M12d |
| détection d'anomalies par reconstruction | M12d |
| espace latent | M25b |
| PSNR | R6 |
| autoencodeur linéaire et ACP | M12d |
| VAE | M25b |
| astuce de reparamétrisation | M02b, M25a |
| divergence KL entre gaussiennes | M06, M25a |
| ELBO | M25b |
| β-VAE | M25b |
| interpolation sphérique (slerp) | M25a |

Non mathématiques : autoencodeur convolutif · autoencodeur débruiteur

## workbookIA 26 · Apprentissage par renforcement

| Notion de workbookIA | Enseignée dans |
|---|---|
| politique | M26 |
| retour actualisé et facteur γ | R5, M26 |
| Q-learning tabulaire | M26 |
| SARSA | M26 |
| ε-greedy et softmax (Boltzmann) | M11, M17 |
| équation de Bellman | M26 |
| itération sur les valeurs | M26 |

Non mathématiques : boucle agent-environnement · API gymnasium (reset, step, terminated, truncated) · on-policy / off-policy · experience replay · conception de la récompense · masques d'actions · discrétisation d'un état continu · self-play · reproductibilité en RL (graines multiples)

## workbookIA 27 · Réseaux antagonistes génératifs (GAN)

| Notion de workbookIA | Enseignée dans |
|---|---|
| GAN : générateur et discriminateur | M27 |
| loss minimax et loss non saturante | M27 |
| discriminateur optimal | M27 |
| distance de Wasserstein 1D | M27 |
| distance de Fréchet (FID) | M27 |
| équilibre de Nash (idée) | M27 |

Non mathématiques : boucle d'entraînement alternée (detach, deux optimiseurs) · DCGAN · GAN conditionnel · effondrement de mode

## workbookIA 28 · Applications créatives

| Notion de workbookIA | Enseignée dans |
|---|---|
| maximisation d'activation | M28 |
| montée de gradient sur l'entrée | M28 |
| matrice de Gram | M28 |
| losses de contenu, de style et de variation totale | M28 |
| stratégies de décodage (glouton, température, top-k, top-p) | M28 |

Non mathématiques : hooks PyTorch · deep dream · transfert de style neuronal · génération de texte mot à mot · documentation de provenance et de licences

## workbookIA 29 · Datasets et préparation du projet final

| Notion de workbookIA | Enseignée dans |
|---|---|
| décalage de distribution | M27 |

Non mathématiques : sources de datasets (HF Hub, Kaggle, OpenML, UCI) · API scikit-learn / torchvision / Hugging Face datasets · licences et retraits de datasets · audit de qualité · doublons et fuites entre découpages · data card / datasheet · téléchargement reproductible (révision, SHA-256)

## workbookIA B1 · Transfer learning et modèles pré-entraînés

| Notion de workbookIA | Enseignée dans |
|---|---|
| zéro-shot CLIP | M07, M17 |
| few-shot par prototypes | M07 |
| linear probe | M13a |

Non mathématiques : transfer learning · extraction de features · fine-tuning partiel et complet · learning rates discriminatifs · dégel progressif · modèles de fondation (DINOv2, CLIP) · oubli catastrophique · latence et taille des modèles · fiche modèle d'un modèle dérivé

## workbookIA B2 · Tokenisation et embeddings

| Notion de workbookIA | Enseignée dans |
|---|---|
| nn.Embedding | MB2 |
| embeddings de phrases | MB2 |
| PPMI + SVD | MB2 |
| word2vec skip-gram | MB2 |
| similarité cosinus et analogies | MB2 |
| recherche sémantique | M07 |

Non mathématiques : Unicode et UTF-8 · normalisation de texte · BPE from scratch · BPE au niveau octet · bibliothèque tokenizers · fertilité et coût des tokens

## workbookIA B3 · Attention et Transformers : un mini-GPT from scratch

| Notion de workbookIA | Enseignée dans |
|---|---|
| masques causal et de padding | MB3 |
| attention par produit scalaire | MB3 |
| attention multi-têtes | MB3 |
| encodages de position (sinusoïdal, RoPE) | MB3 |
| perplexité | M06 |
| top-k et top-p | M28 |
| coût quadratique et FlashAttention | MB3 |

Non mathématiques : bloc Transformer pré-LN · architectures BERT/GPT/T5 · mini-GPT PyTorch from scratch · KV cache · Vision Transformer

## workbookIA B4 · LLM en pratique : Hugging Face, prompting, RAG et LoRA

| Notion de workbookIA | Enseignée dans |
|---|---|
| BM25 | MB4 |
| recherche dense et hybride | MB4 |
| recall@k et MRR | MB4 |
| LoRA from scratch | MB4 |

Non mathématiques : transformers en pratique (5.x) · chat templates · prompting et sortie structurée · évaluation de LLM · RAG avec citations · peft · classification de textes · injection de prompt · reproductibilité d'un pipeline LLM

## workbookIA B5 · Modèles de diffusion : un DDPM minimal

| Notion de workbookIA | Enseignée dans |
|---|---|
| processus direct et forme fermée | MB5 |
| plannings de bruit linéaire et cosinus | MB5 |
| posterior gaussien | MB5 |
| loss de prédiction du bruit | MB5 |
| échantillonnage DDPM | MB5 |
| DDIM | MB5 |
| EMA des poids | R5, M19 |
| guidance sans classifieur | MB5 |
| évaluation par distance de Fréchet | M27 |
| flow matching (initiation) | MB5 |

Non mathématiques : U-Net conditionné par le temps · mémorisation

## workbookIA B6 · Explicabilité, équité et éthique

| Notion de workbookIA | Enseignée dans |
|---|---|
| SHAP (TreeExplainer, graphiques) | MB6 |
| dépendance partielle et ICE | MB6 |
| valeurs de Shapley exactes | MB6 |
| gradients intégrés | MB6 |
| Grad-CAM par hooks | MB6 |
| indicateurs d'équité par groupe | M03, MB6 |
| théorème d'impossibilité | M03, MB6 |

Non mathématiques : tests de santé des explications · atténuation des biais · fiche modèle équité et explicabilité · RGPD et AI Act appliqués

## workbookIA B7 · Du notebook à la production

| Notion de workbookIA | Enseignée dans |
|---|---|
| mesure de latence | M02c |
| surveillance de la dérive | M27 |

Non mathématiques : structure d'un projet Python · argparse et logging · configuration typée · reproductibilité · suivi d'expériences · tests pour le ML · intégration continue · artefact de modèle · API de prédiction · torch.export · Dockerfile

## workbookIA B8 · RL moderne : DQN, gradient de politique, PPO et RLHF

| Notion de workbookIA | Enseignée dans |
|---|---|
| DQN et ses stabilisateurs | M26 |
| Double DQN | M26 |
| théorème du gradient de politique | MB8 |
| REINFORCE avec baseline | MB8 |
| acteur-critique et GAE | MB8 |
| PPO from scratch | MB8 |
| évaluation multi-graines | M08 |
| modèle de récompense Bradley-Terry | MB8 |
| RLHF, DPO, GRPO | MB8 |

Non mathématiques : environnements vectorisés gymnasium · diagnostic par les journaux RL · piratage de la récompense (reward hacking)

