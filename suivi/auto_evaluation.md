# Auto-évaluation des compétences

> **Modèle tenu par Claude : ne le remplis pas ici.** Ta copie personnelle est `mon_travail/suivi/auto_evaluation.md`, créée par `python tools/start_chapter.py --init`. Si une section est ajoutée ici après ta copie, `start_chapter.py` l'ajoute à la fin de ta copie, sans toucher à ce que tu as écrit.

À remplir à la fin de chaque chapitre, puis à revoir avant chaque examen blanc. Sois honnête : c'est un outil pour savoir quoi réviser, pas une note.

| Niveau | Signification |
|:-:|---|
| **0** | Je ne sais pas encore de quoi il s'agit. |
| **1** | Je reconnais la notion et je peux la décrire avec le cours sous les yeux. |
| **2** | Je sais faire le calcul seul sur un exercice standard. |
| **3** | Je sais l'expliquer à quelqu'un, le démontrer quand c'est demandé, l'implémenter et dire à quoi il sert dans workbookIA. |

Chaque chapitre a sa section ci-dessous, dans l'ordre d'étude (test de positionnement, examens blancs et projet de synthèse compris) : une ligne par grand objectif du chapitre (la fiche d'un chapitre les détaille dans « Objectifs d'apprentissage »). Note le niveau et la date de chaque évaluation, en gardant les précédents pour voir ta progression : `2 → 3` dans la colonne du niveau, `10/11 → 02/12` dans celle de la date.

<!-- wbm:section setup -->
## Mise en place

| Compétence | Niveau |
|---|:-:|
| Ouvrir un notebook dans Colab et exécuter toutes les cellules | |
| Taper une réponse (nombre, fraction, expression, intervalle) et la vérifier avec `wbm.check` | |
| Utiliser `git pull` pour récupérer les mises à jour | |
| Lancer les tests `pytest` et lire leur résultat | |
<!-- wbm:end setup -->

<!-- wbm:section R0 -->
## R0 · Prise en main

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Exécuter un notebook du dépôt et y écrire tes réponses | | |
| Calculer avec Python en respectant ses priorités (`**`, `//`, `%`), et savoir pourquoi 0,1 + 0,2 n'y vaut pas exactement 0,3 | | |
| Taper un nombre, une fraction, une expression et un intervalle pour `wbm.check` | | |
| Vérifier un développement ou une simplification avec SymPy | | |
| Écrire une formule en LaTeX dans une cellule Markdown | | |
| Écrire une fonction de `mymath` et lancer ses tests | | |
<!-- wbm:end R0 -->

<!-- wbm:section POS -->
## POS · Test de positionnement

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Savoir quels chapitres de la remise à niveau tu peux sauter, survoler ou dois faire en entier | | |
| Repérer tes erreurs de calcul récurrentes avant de commencer | | |
<!-- wbm:end POS -->

<!-- wbm:section R1 -->
## R1 · Nombres et calcul

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer sans erreur avec des priorités, des nombres négatifs et des fractions, à la main puis en vérifiant avec Python | | |
| Appliquer les règles des puissances (exposants négatifs compris) et des racines carrées, et repérer les « règles » qui n'existent pas | | |
| Écrire un nombre en notation scientifique, l'arrondir à un nombre de chiffres significatifs et donner son ordre de grandeur | | |
| Calculer une évolution en pourcentage, des évolutions successives et une évolution réciproque | | |
| Calculer une moyenne pondérée, et reconnaître la somme pondérée qui fait le calcul d'un neurone | | |
| Estimer un ordre de grandeur à la manière de Fermi | | |
<!-- wbm:end R1 -->

<!-- wbm:section R2 -->
## R2 · Calcul littéral et équations

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Réduire, développer et factoriser une expression, identités remarquables comprises | | |
| Résoudre une équation et une inéquation du premier degré, et écrire l'ensemble des solutions avec des intervalles | | |
| Résoudre une équation avec une valeur absolue, en lisant \|a − b\| comme une distance | | |
| Résoudre un système 2 × 2 par substitution, par combinaison et par la formule de Cramer, et dire quand il a une seule solution | | |
| Mettre un problème concret en équation | | |
<!-- wbm:end R2 -->

<!-- wbm:section R3 -->
## R3 · Fonctions

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer des images et des antécédents, lire un graphique et déterminer un ensemble de définition | | |
| Déterminer une fonction affine à partir de deux points et interpréter sa pente et son ordonnée à l'origine | | |
| Mettre un polynôme du second degré sous forme canonique, trouver ses racines et son sommet | | |
| Étudier le sens de variation des fonctions de référence et trouver un extremum | | |
| Composer deux fonctions et trouver une réciproque, en sachant dans quel ordre on les applique | | |
<!-- wbm:end R3 -->

<!-- wbm:section R4 -->
## R4 · Logique, ensembles, Σ et Π

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Construire une table de vérité et nier une phrase qui contient des quantificateurs | | |
| Distinguer une implication, sa réciproque et sa contraposée | | |
| Manipuler les ensembles et leurs opérations, et lire la notation des ensembles de nombres | | |
| Lire, écrire et calculer des sommes Σ et des produits Π, et changer d'indice | | |
| Choisir un type de raisonnement et rédiger une démonstration courte, récurrence comprise | | |
<!-- wbm:end R4 -->

<!-- wbm:section R5 -->
## R5 · Suites

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer les termes d'une suite définie explicitement ou par récurrence | | |
| Reconnaître une suite arithmétique ou géométrique, et calculer un terme et une somme | | |
| Dire si une suite géométrique converge et calculer la somme d'une série géométrique | | |
| Calculer une moyenne mobile et une moyenne exponentielle, et relier leurs poids à une suite géométrique | | |
<!-- wbm:end R5 -->

<!-- wbm:section R6 -->
## R6 · Exponentielle et logarithmes

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Utiliser les propriétés de exp et de ln pour simplifier une expression et résoudre une équation | | |
| Passer d'une base de logarithme à une autre, et compter en bits | | |
| Comparer les croissances des puissances, des exponentielles et des logarithmes | | |
| Lire et tracer un graphique en échelle logarithmique | | |
| Étudier la sigmoïde et la tangente hyperbolique, et les écrire avec exp | | |
<!-- wbm:end R6 -->

<!-- wbm:section R7 -->
## R7 · Limites et dérivation

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer des limites simples et repérer une asymptote | | |
| Calculer un taux d'accroissement, en déduire le nombre dérivé et l'équation de la tangente | | |
| Dériver les fonctions usuelles avec les règles de somme, de produit, de quotient et de composition | | |
| Étudier les variations d'une fonction et trouver ses extremums avec la dérivée | | |
| Approcher un zéro par dichotomie et une dérivée par un taux d'accroissement en Python | | |
<!-- wbm:end R7 -->

<!-- wbm:section R8 -->
## R8 · Probabilités de base

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Décrire une expérience aléatoire et calculer des probabilités par équiprobabilité ou avec un arbre | | |
| Dénombrer avec le principe multiplicatif, les factorielles et les coefficients binomiaux | | |
| Reconnaître des événements indépendants | | |
| Calculer la loi, l'espérance, la variance et l'écart-type d'une variable aléatoire discrète | | |
| Estimer une probabilité par simulation et observer la loi des grands nombres | | |
<!-- wbm:end R8 -->

<!-- wbm:section R9 -->
## R9 · Géométrie du plan, vecteurs et trigonométrie

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer des coordonnées, des distances et des vecteurs dans un repère du plan | | |
| Additionner des vecteurs, les multiplier par un nombre et calculer leur norme | | |
| Écrire l'équation d'une droite et reconnaître des vecteurs orthogonaux | | |
| Calculer un produit scalaire et en déduire un angle | | |
| Passer des degrés aux radians, et lire cosinus et sinus sur le cercle trigonométrique | | |
| Refaire ces calculs avec des vecteurs à trois composantes et plus | | |
<!-- wbm:end R9 -->

<!-- wbm:section CP0 -->
## CP0 · Bilan de remise à niveau

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Vérifier en temps limité que la remise à niveau est acquise | | |
| Construire ta propre synthèse de la partie 0 | | |
<!-- wbm:end CP0 -->

<!-- wbm:section M02a -->
## M02a · Intégrales et densités

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Approcher une aire par des sommes de Riemann, et la calculer exactement par une primitive | | |
| Calculer une intégrale par linéarité, par parties ou par un changement de variable | | |
| Reconnaître une intégrale impropre convergente et la calculer | | |
| Programmer les méthodes des rectangles, des trapèzes et de Simpson, et comparer leurs erreurs | | |
| Vérifier qu'une fonction est une densité, en déduire des probabilités et sa fonction de répartition | | |
| Calculer un quantile, un percentile et la médiane d'une loi continue | | |
<!-- wbm:end M02a -->

<!-- wbm:section M02b -->
## M02b · Variables aléatoires et lois usuelles

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Reconnaître la loi qui modélise une situation (Bernoulli, binomiale, catégorielle, géométrique, Poisson, uniforme, exponentielle, normale) | | |
| Calculer des probabilités, une espérance et une variance, pour une loi discrète ou continue | | |
| Lire une loi jointe, ses marginales, et décider de l'indépendance de deux variables | | |
| Utiliser la linéarité de l'espérance et la variance d'une somme de variables indépendantes | | |
| Calculer une intégrale double simple et la loi d'une variable transformée | | |
| Simuler une loi par inversion de sa fonction de répartition | | |
<!-- wbm:end M02b -->

<!-- wbm:section M02c -->
## M02c · Échantillons et estimation

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Résumer une série (moyenne, médiane, quantiles, variance) et repérer ses valeurs aberrantes | | |
| Énoncer la loi des grands nombres et le théorème central limite, et s'en servir pour une probabilité | | |
| Calculer le biais, la variance et l'erreur quadratique d'un estimateur, et justifier le n − 1 | | |
| Calculer une erreur type et un intervalle de confiance pour une moyenne | | |
| Calculer une covariance, une corrélation et une matrice de covariance, et les interpréter | | |
| Reconnaître un biais d'échantillonnage et l'effet d'une imputation | | |
<!-- wbm:end M02c -->

<!-- wbm:section M03 -->
## M03 · Probabilités conditionnelles

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Lire dans un tableau de contingence des probabilités jointes, marginales et conditionnelles | | |
| Décider de l'indépendance de deux événements ou de deux variables par le calcul | | |
| Utiliser la formule des probabilités totales | | |
| Écrire accuracy, precision, recall et spécificité comme des probabilités, et calculer leurs moyennes | | |
| Mesurer l'effet de la prévalence et du seuil de décision sur ces métriques | | |
| Calculer une AUC comme une aire et comme une proportion de paires, une average precision et un score de Brier | | |
<!-- wbm:end M03 -->

<!-- wbm:section M04 -->
## M04 · Bayes, vraisemblance et loi Beta

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Appliquer la formule de Bayes à deux hypothèses ou plus, une fois ou en boucle | | |
| Écrire une vraisemblance et trouver son maximum | | |
| Calculer la densité, la moyenne, le mode et la variance d'une loi Beta | | |
| Mettre à jour une loi Beta par conjugaison, et en déduire le MAP, la moyenne a posteriori et la probabilité prédictive | | |
| Calculer avec des log-probabilités pour éviter l'underflow | | |
| Distinguer les points de vue fréquentiste et bayésien | | |
<!-- wbm:end M04 -->

<!-- wbm:section M05a -->
## M05a · Dérivées, Taylor et calcul numérique

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Étudier la convexité d'une fonction et classer ses extrema locaux et globaux | | |
| Écrire un polynôme de Taylor et borner son erreur | | |
| Résoudre une équation par la méthode de Newton, et dire quand elle converge vite | | |
| Calculer l'erreur d'une différence finie avant ou centrée, et choisir un pas | | |
| Expliquer comment un ordinateur représente un nombre réel, et ses limites | | |
| Calculer un log-sum-exp et une softmax sans overflow | | |
<!-- wbm:end M05a -->

<!-- wbm:section M05b -->
## M05b · Fonctions de plusieurs variables et gradient

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Lire une fonction de deux variables sur une surface et sur ses lignes de niveau | | |
| Calculer des dérivées partielles, un gradient et une dérivée directionnelle | | |
| Expliquer pourquoi le gradient donne la plus grande pente et coupe les lignes de niveau à angle droit | | |
| Écrire le plan tangent et s'en servir pour approcher une valeur | | |
| Trouver les points critiques d'une fonction de deux variables et les classer | | |
| Expliquer le principe de la descente et de la montée de gradient | | |
<!-- wbm:end M05b -->

<!-- wbm:section M06 -->
## M06 · Théorie de l'information

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer l'information d'un événement et l'entropie d'une loi, en bits et en nats | | |
| Calculer des entropies conjointe et conditionnelle et une information mutuelle à partir d'un tableau | | |
| Calculer une cross-entropy et une divergence KL, et démontrer que la KL est positive | | |
| Décider si des longueurs de code sont possibles (inégalité de Kraft) et comparer un code à l'entropie | | |
| Relier la log loss et la perplexité à la cross-entropy | | |
<!-- wbm:end M06 -->

<!-- wbm:section CP1 -->
## CP1 · Examen blanc de la partie I

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Vérifier en temps limité que les notions de la partie I sont acquises | | |
| Construire ta propre synthèse de la partie I | | |
<!-- wbm:end CP1 -->

<!-- wbm:section M07 -->
## M07 · Vecteurs et géométrie de ℝⁿ

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer avec des vecteurs de ℝⁿ : combinaisons linéaires, produit scalaire, vecteurs one-hot | | |
| Calculer les normes L1, L2 et L∞ et les distances associées, et démontrer l'inégalité triangulaire | | |
| Calculer un angle et une similarité cosinus, démontrer l'inégalité de Cauchy-Schwarz, projeter sur une droite | | |
| Décrire un hyperplan par son vecteur normal, dire de quel côté est un point et calculer sa distance | | |
| Démontrer que le barycentre minimise la somme des carrés des distances, et calculer une inertie, une silhouette et les probabilités de k-means++ | | |
| Mesurer, à la main et par simulation, ce qui change quand la dimension grandit | | |
<!-- wbm:end M07 -->

<!-- wbm:section M08 -->
## M08 · Tests statistiques

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Poser une hypothèse nulle et une alternative, choisir une statistique et interpréter une p-valeur sans contresens | | |
| Calculer à la main la p-valeur exacte d'un test binomial et d'un petit test par permutation | | |
| Calculer les erreurs de type I et II et la puissance d'un test, et dimensionner un échantillon | | |
| Calculer un intervalle de Wald et de Wilson pour une proportion, et un intervalle de Student pour des mesures appariées | | |
| Corriger des comparaisons multiples par Bonferroni et en démontrer la garantie | | |
| Comparer des modèles par l'AIC, le BIC et un facteur de Bayes | | |
<!-- wbm:end M08 -->

<!-- wbm:section M09a -->
## M09a · Matrices et systèmes linéaires

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Lire un tableau de données comme une matrice et prévoir la forme de chaque produit | | |
| Calculer des produits matrice-vecteur et matriciels à la main, sous leurs deux lectures, et en compter le coût | | |
| Écrire une couche Z = XW + b et un embedding comme des produits matriciels | | |
| Appliquer les règles de la transposée et démontrer (AB)ᵀ = BᵀAᵀ | | |
| Résoudre un système par le pivot de Gauss et décrire toutes ses solutions | | |
| Calculer une inverse, un rang, et relier le rang au nombre de solutions | | |
<!-- wbm:end M09a -->

<!-- wbm:section M09b -->
## M09b · Moindres carrés et régularisation

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer les losses d'une régression (MSE, RMSE, MAE, Huber) et un R², et décomposer la variance | | |
| Calculer les gradients de aᵀw, de wᵀAw et de ‖y − Xw‖², et en déduire les équations normales en dimension p | | |
| Interpréter les moindres carrés comme une projection, avec la matrice chapeau | | |
| Compter les colonnes de features polynomiales | | |
| Résoudre un problème ridge, démontrer qu'il a toujours une solution et le relier à un prior gaussien | | |
| Démontrer que le bruit gaussien mène aux moindres carrés, et décomposer une erreur en biais², variance et bruit | | |
<!-- wbm:end M09b -->

<!-- wbm:section M10 -->
## M10 · Séparabilité linéaire et convexité

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Reconnaître et démontrer qu'un ensemble est convexe | | |
| Construire l'enveloppe convexe d'un nuage du plan, à la main et en code | | |
| Démontrer que deux nuages séparables ont des enveloppes convexes disjointes, et tester la séparabilité | | |
| Calculer une marge géométrique, et passer d'un hyperplan affine à un hyperplan par l'origine (astuce du biais) | | |
| Borner une suite de normes pas à pas | | |
<!-- wbm:end M10 -->

<!-- wbm:section M11 -->
## M11 · Logique, induction et inégalités de concentration

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Écrire la contraposée et la négation d'un énoncé, et décider par une table de vérité si un argument est valide | | |
| Traduire des phrases en inclusions d'ensembles et construire un contre-exemple | | |
| Repérer les pièges d'une induction (taux de base, échantillon biaisé, corrélation) | | |
| Démontrer et appliquer les inégalités de Markov et de Tchebychev, et en déduire la loi faible des grands nombres | | |
| Appliquer l'inégalité de Hoeffding : rayon de confiance et taille d'échantillon | | |
| Expliquer d'où vient le bonus d'une borne supérieure de confiance, et calculer le regret attendu d'ε-greedy | | |
<!-- wbm:end M11 -->

<!-- wbm:section CP2 -->
## CP2 · Examen blanc de la partie II

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Vérifier en temps limité que les notions de la partie II sont acquises | | |
| Construire ta propre synthèse de la partie II | | |
<!-- wbm:end CP2 -->

<!-- wbm:section M12a -->
## M12a · Espaces vectoriels et applications linéaires

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Reconnaître un sous-espace vectoriel et le décrire par une famille génératrice ou par des équations | | |
| Décider si une famille est libre, en extraire une base, et calculer des coordonnées dans une base | | |
| Calculer le rang d'une matrice et majorer celui d'un produit | | |
| Écrire la matrice d'une application linéaire, et composer des applications en multipliant leurs matrices | | |
| Calculer un noyau et une image, appliquer le théorème du rang, et décrire toutes les solutions de A x = b | | |
| Changer de base, et inverser une application affine | | |
<!-- wbm:end M12a -->

<!-- wbm:section M12b -->
## M12b · Orthogonalité et projections

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Reconnaître un produit scalaire défini par une matrice symétrique, et calculer normes et angles avec | | |
| Calculer dans une base orthonormée, et reconnaître une matrice orthogonale | | |
| Orthonormaliser une famille par Gram-Schmidt | | |
| Calculer un complément orthogonal et une projection orthogonale, et démontrer que le projeté est le point le plus proche | | |
| Résoudre des moindres carrés par une projection, puis par la décomposition QR | | |
| Calculer un produit scalaire de fonctions et orthogonaliser des polynômes | | |
<!-- wbm:end M12b -->

<!-- wbm:section M12c -->
## M12c · Valeurs propres et matrices symétriques

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer un déterminant, l'interpréter comme un volume orienté, et l'utiliser pour l'inversibilité | | |
| Calculer les valeurs et vecteurs propres d'une petite matrice, et diagonaliser | | |
| Appliquer le théorème spectral et le quotient de Rayleigh à une matrice symétrique | | |
| Approcher la plus grande valeur propre par la méthode de la puissance | | |
| Reconnaître une matrice définie positive et calculer sa décomposition de Cholesky | | |
| Transformer une matrice de covariance, et blanchir des données | | |
<!-- wbm:end M12c -->

<!-- wbm:section M12d -->
## M12d · SVD et analyse en composantes principales

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer la SVD d'une petite matrice et l'interpréter comme rotation, étirement, rotation | | |
| Calculer une approximation de rang faible et son erreur (Eckart-Young) | | |
| Calculer une pseudo-inverse et un conditionnement, et dire ce qu'ils signifient | | |
| Calculer les axes principaux d'un nuage, les scores, une reconstruction et la variance expliquée | | |
| Relier l'erreur de reconstruction aux valeurs propres oubliées | | |
| Situer l'ACP par rapport à t-SNE et UMAP | | |
<!-- wbm:end M12d -->

<!-- wbm:section M13a -->
## M13a · Vraisemblance et régression logistique

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer et démontrer des estimateurs du maximum de vraisemblance (Bernoulli, catégorielle, gaussienne) | | |
| Écrire la log-loss comme moins la log-vraisemblance, et la calculer | | |
| Calculer avec la sigmoïde et la softplus, et démontrer la convexité de la softplus | | |
| Lire un modèle logistique : probabilités, cote, frontière de décision | | |
| Calculer à la main un Naïve Bayes avec lissage, en log-probabilités | | |
| Calculer une entropie, un indice de Gini, un gain d'information et une réduction de variance | | |
<!-- wbm:end M13a -->

<!-- wbm:section M13b -->
## M13b · Optimisation sous contraintes et SVM

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Résoudre un problème d'optimisation sous contraintes d'égalité par les multiplicateurs de Lagrange | | |
| Écrire les conditions KKT d'un problème avec inégalités, et sa fonction duale | | |
| Reconnaître un problème convexe et ce qu'il garantit | | |
| Écrire le problème d'une SVM à marge dure et à marge souple, et le relier à la hinge loss | | |
| Lire le problème dual d'une SVM et ses vecteurs de support | | |
| Calculer avec des noyaux polynomiaux et RBF, et reconnaître un noyau valide | | |
<!-- wbm:end M13b -->

<!-- wbm:section M14 -->
## M14 · Les maths des ensembles

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer la queue d'une loi binomiale, et la majorer par la borne de Chernoff | | |
| Calculer la variance d'une moyenne pondérée de variables corrélées par leur matrice de covariance | | |
| Démontrer et utiliser la limite (1 + x/n)ⁿ → eˣ | | |
| Calculer des poids exponentiels renormalisés, et suivre le meilleur de plusieurs experts | | |
| Calculer le gradient d'une loss par rapport au vecteur des prédictions | | |
<!-- wbm:end M14 -->

<!-- wbm:section CP3 -->
## CP3 · Examen blanc de la partie III

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Vérifier en temps limité que les notions de la partie III sont acquises | | |
| Construire ta propre synthèse de la partie III | | |
<!-- wbm:end CP3 -->

<!-- wbm:section M16 -->
## M16 · Applications affines, graphes et variance d'un produit

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Écrire une application affine de ℝⁿ dans ℝᵐ dans les deux conventions (x W + b et W x + b), avec la forme de chaque objet, et compter ses paramètres | | |
| Composer des applications affines en multipliant leurs matrices en coordonnées homogènes | | |
| Lire un graphe orienté sur sa matrice d'adjacence : degrés entrants et sortants, chemins de longueur k comptés par Aᵏ | | |
| Reconnaître un graphe sans cycle par la nilpotence de sa matrice d'adjacence, numéroter ses nœuds pour la rendre triangulaire, et sommer sur ses chemins | | |
| Calculer l'espérance et la variance d'un produit de variables indépendantes, et la variance d'une somme de variables seulement décorrélées | | |
| Suivre une variance multipliée par le même facteur à chaque étage, et prévoir son explosion ou son extinction | | |
<!-- wbm:end M16 -->

<!-- wbm:section M17 -->
## M17 · Jacobienne et règle de la chaîne

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer la jacobienne d'une application de ℝⁿ dans ℝᵐ, et s'en servir comme approximation linéaire | | |
| Reconnaître une jacobienne diagonale, et la calculer avec une seule paire d'évaluations | | |
| Dériver une composée par le produit des jacobiennes, dans le bon ordre et avec les bonnes formes | | |
| Passer du gradient en ligne de MML au gradient de la forme de la variable de NumPy | | |
| Calculer un produit jacobienne-vecteur ou vecteur-jacobienne sans former la jacobienne | | |
| Dériver une fonction définie par morceaux, et suivre la dérivée d'une longue composition | | |
| Calculer une loi de Boltzmann et ses limites en température, et la covariance diag(p) − ppᵀ d'un vecteur one-hot | | |
<!-- wbm:end M17 -->

<!-- wbm:section M18 -->
## M18 · Différentiation automatique et calcul matriciel

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Écrire le graphe de calcul d'une formule, et dériver sa sortie par la somme, sur les chemins, des produits des dérivées locales | | |
| Propager à la main des dérivées en mode direct (nombres duaux) et des adjoints en mode inverse | | |
| Choisir le mode selon le nombre d'entrées et de sorties, et en estimer le coût | | |
| Calculer le gradient d'une fonction d'une matrice, de la forme de cette matrice, par les coordonnées puis par la différentielle | | |
| Dériver une moyenne de fonctions, et vérifier un gradient matriciel par différences centrées | | |
<!-- wbm:end M18 -->

<!-- wbm:section M19 -->
## M19 · Hessienne, conditionnement et convergence

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer une hessienne, écrire le développement de Taylor d'ordre 2, et classer un point critique de ℝⁿ par les signes des valeurs propres de la hessienne | | |
| Décider de la convergence d'une itération linéaire x ← M x + c par les valeurs propres de M symétrique | | |
| Choisir le pas de l'itération de Richardson pour un système à matrice symétrique définie positive, et prévoir le nombre d'itérations par le conditionnement | | |
| Préconditionner un système par une matrice diagonale | | |
| Résoudre une récurrence linéaire d'ordre 2, et décider de sa convergence par le module des racines de son polynôme caractéristique | | |
| Montrer qu'un gradient estimé sur un échantillon tiré au hasard est sans biais, et calculer sa variance | | |
| Projeter un vecteur sur une boule et sur un pavé, et comparer les directions obtenues | | |
<!-- wbm:end M19 -->

<!-- wbm:section M20 -->
## M20 · Tenseurs, axes et estimateurs pondérés

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Décrire un tableau à k dimensions par sa forme et ses axes, le remodeler, et le réduire le long d'axes choisis | | |
| Écrire produits, traces et contractions en notation d'Einstein, et les calculer avec `einsum` | | |
| Calculer moyennes et variances le long d'axes, avec le bon ddof, et centrer par diffusion | | |
| Reconnaître le centrage comme une projection orthogonale, et les invariances de la standardisation | | |
| Construire un estimateur sans biais en divisant par une probabilité d'inclusion, et calculer sa variance | | |
| Calculer la jacobienne d'une application proche de l'identité, et suivre le produit de L telles jacobiennes | | |
<!-- wbm:end M20 -->

<!-- wbm:section CP4 -->
## CP4 · Examen blanc de la partie IV

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Vérifier en temps limité que les notions de la partie IV sont acquises | | |
| Construire ta propre synthèse de la partie IV | | |
<!-- wbm:end CP4 -->

<!-- wbm:section M21 -->
## M21 · Convolution, matrices de Toeplitz et équivariance

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer à la main la convolution et la corrélation croisée de deux suites, dans les modes plein, valide et même taille, et passer d'une convention à l'autre | | |
| Écrire la matrice de Toeplitz d'une convolution, compter ses coefficients non nuls, et lire son rang | | |
| Démontrer et utiliser l'équivariance par translation, et reconnaître une convolution circulaire | | |
| Compter les positions d'une fenêtre avec pas, dilatation et padding, et calculer la taille d'une convolution transposée | | |
| Compter les paramètres et le coût d'un filtrage à plusieurs canaux, et séparer un noyau de rang 1 | | |
| Composer des convolutions en une seule, et calculer un champ récepteur | | |
| Trouver le pire cas d'une perturbation bornée d'une forme linéaire, pour les normes L∞ et L2 | | |
<!-- wbm:end M21 -->

<!-- wbm:section M22 -->
## M22 · Récurrences vectorielles, rayon spectral et normes de matrices

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Résoudre une récurrence linéaire vectorielle avec entrée, et lire sa réponse impulsionnelle comme une convolution | | |
| Calculer les puissances d'une matrice, ses valeurs propres complexes sous forme exponentielle, et reconnaître une rotation et une homothétie | | |
| Décider si Aᵗ tend vers 0 par le rayon spectral, et repérer une croissance transitoire | | |
| Calculer les normes induites ‖·‖₁, ‖·‖∞ et ‖·‖₂ d'une matrice, et majorer la norme d'un produit | | |
| Suivre un produit de facteurs dans [0, 1] et un produit de jacobiennes le long d'une trajectoire | | |
| Écrire la sensibilité de l'état final à un paramètre utilisé à chaque pas comme une somme sur le temps | | |
| Ramener sous un seuil un vecteur fait de plusieurs blocs sans changer sa direction | | |
<!-- wbm:end M22 -->

<!-- wbm:section CP5 -->
## CP5 · Examen blanc de la partie V

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Vérifier en temps limité que les notions de la partie V sont acquises | | |
| Construire ta propre synthèse de la partie V | | |
<!-- wbm:end CP5 -->

<!-- wbm:section M25a -->
## M25a · Gaussienne multivariée, conditionnement et divergence KL

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Écrire et évaluer la densité et la log-densité d'une loi normale multivariée, et y lire le rôle de det Σ et de la distance de Mahalanobis | | |
| Trouver la loi d'une transformation affine ou d'une somme de vecteurs gaussiens par le changement de variable multivarié, et tirer un vecteur de loi N(μ, Σ) sous la forme μ + Lε, par Cholesky | | |
| Tracer les ellipses de niveau d'une gaussienne, calculer la masse d'une ellipse en dimension 2, et décrire la loi de la norme d'un vecteur gaussien en dimension d | | |
| Calculer un complément de Schur, une loi marginale et une loi conditionnelle, et lire une matrice de précision | | |
| Multiplier deux densités gaussiennes, et calculer le posterior, la prédictive et l'évidence d'une régression linéaire bayésienne | | |
| Démontrer le maximum de vraisemblance de μ et Σ avec les gradients de ln det et de la trace | | |
| Définir la divergence KL continue, démontrer sa positivité (Jensen) et son additivité, et calculer la KL entre deux gaussiennes multivariées | | |
| Démontrer les propriétés de l'interpolation sphérique et l'appliquer à un trajet sur une sphère | | |
<!-- wbm:end M25a -->

<!-- wbm:section M25b -->
## M25b · Variables latentes et ELBO

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Écrire la loi jointe d'un modèle à variables latentes selon son graphe orienté, en tirer un échantillon ancestral, et calculer la vraisemblance marginale et le posterior d'un latent | | |
| Définir l'espérance et la variance conditionnelles sachant une variable discrète, et calculer la moyenne et la covariance d'un mélange par les lois de l'espérance et de la variance totales | | |
| Calculer les responsabilités et la log-vraisemblance d'un mélange de gaussiennes en log, et expliquer pourquoi cette vraisemblance n'est pas bornée | | |
| Dériver les pas E et M de l'algorithme EM pour un mélange de gaussiennes, et démontrer qu'il ne fait jamais baisser la vraisemblance | | |
| Démontrer ln p(x) = ELBO(q) + KL(q ‖ p(z \| x)) pour toute loi q, en déduire la borne et le cas d'égalité, et lire l'EM comme une montée par coordonnées de l'ELBO | | |
| Écrire la loi marginale et le posterior de l'ACP probabiliste, en estimer les paramètres à partir des valeurs propres, et comparer deux sous-espaces par leurs angles principaux | | |
| Dériver une espérance par rapport à un paramètre de la loi par le chemin X = μ + σε, et choisir le sens de la KL dans une approximation | | |
| Interpréter β comme un multiplicateur de Lagrange, décomposer la KL moyenne au prior en information mutuelle et écart du posterior agrégé, et reconnaître un code effondré | | |
<!-- wbm:end M25b -->

<!-- wbm:section M26 -->
## M26 · Chaînes de Markov et équation de Bellman

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Écrire la matrice de transition d'une chaîne de Markov, en convention ligne, et calculer la loi après n pas | | |
| Calculer une loi stationnaire, dire si elle est unique et si la loi de la chaîne y converge, et à quelle vitesse | | |
| Calculer une probabilité d'absorption et une durée moyenne par l'analyse au premier pas (espérance conditionnelle) | | |
| Définir le retour actualisé et la valeur d'un état sous une politique fixée, et interpréter γ comme une probabilité de continuer | | |
| Écrire et résoudre le système de Bellman d'une politique fixée, et justifier qu'il a une unique solution | | |
| Itérer l'opérateur de Bellman, borner l'erreur et choisir le nombre d'itérations | | |
| Résoudre un problème d'arrêt optimal par un opérateur avec un maximum, et lire l'équation d'optimalité de Bellman | | |
| Relier la moyenne de retours simulés, l'erreur TD et le biais du maximum aux équations exactes | | |
<!-- wbm:end M26 -->

<!-- wbm:section M27 -->
## M27 · Jeux et distances entre lois

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Trouver le maximin, le minimax et les points selles d'une matrice de gains, et réduire un jeu par dominance | | |
| Calculer les stratégies optimales et la valeur d'un jeu 2 × 2 par indifférence, et énoncer le théorème minimax de von Neumann | | |
| Trouver les équilibres de Nash d'un jeu à deux joueurs, et la valeur d'un arbre de jeu par induction arrière | | |
| Prévoir, par les valeurs propres d'un pas, si la descente-montée tourne autour d'un équilibre ou s'en éloigne | | |
| Calculer la probabilité a posteriori qui minimise la log-loss espérée, et démontrer qu'elle la minimise | | |
| Calculer la divergence de Jensen-Shannon de deux lois, et expliquer pourquoi elle plafonne à ln 2 | | |
| Écrire un couplage de deux lois discrètes, calculer son coût, et trouver le plan optimal sur la droite | | |
| Calculer W₁ et W₂ en dimension 1 par les fonctions de répartition ou par les quantiles, dont W₂ de deux gaussiennes | | |
| Calculer la distance de Fréchet de deux gaussiennes dans un cas commutatif, et le biais d'une distance estimée sur des échantillons | | |
| Mesurer une dérive par le PSI, la statistique de Kolmogorov-Smirnov et W₁, et dire ce que chacune mesure | | |
<!-- wbm:end M27 -->

<!-- wbm:section M28 -->
## M28 · Matrice de Gram, montée sur l'entrée et lois tronquées

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer la matrice de Gram d'une famille de vecteurs dans les deux sens et la matrice des moments d'ordre 2, et choisir laquelle former selon son coût | | |
| Lire des distances dans une matrice de Gram, retrouver une matrice de Gram à partir de distances (double centrage), puis des positions à une isométrie près | | |
| Démontrer que deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie | | |
| Faire une montée de gradient projetée sur un pavé, avec un pas normalisé ou des coordonnées gelées, et prévoir où elle s'arrête pour une fonction linéaire, quadratique ou convexe | | |
| Écrire la variation totale d'une grille comme une forme quadratique, calculer son gradient et un pas de lissage, et comparer le carré et la valeur absolue | | |
| Lire la période et la fréquence d'un motif, situer la fréquence de Nyquist, et calculer ce qu'en font la variation totale et un flou | | |
| Tempérer une loi catégorielle, la tronquer par top-k ou top-p, et calculer le coût de la troncature en divergence KL | | |
| Trouver la prépériode et la période d'une itération sur un ensemble fini, et expliquer pourquoi le décodage glouton boucle | | |
<!-- wbm:end M28 -->

<!-- wbm:section CP6 -->
## CP6 · Examen blanc de la partie VI

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Vérifier en temps limité que les notions de la partie VI sont acquises | | |
| Construire ta propre synthèse de la partie VI | | |
<!-- wbm:end CP6 -->

<!-- wbm:section MB2 -->
## MB2 · Cooccurrences, PMI et embeddings

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Écrire un entier en base 2 et en base 16, lire un octet et une couleur, découper un mot de bits en champs, et compter les bits qu'il faut pour N valeurs | | |
| Calculer la PMI des cases d'une table jointe, la lire comme le logarithme d'un lift, en tirer la PPMI, et retrouver l'information mutuelle comme la moyenne des PMI | | |
| Démontrer la borne PMI(x, y) ≤ min(−ln p(x), −ln p(y)) et expliquer pourquoi les événements rares ont les PMI extrêmes et les plus bruitées | | |
| Lisser une marge par une puissance, la reconnaître comme une loi tempérée, et prévoir le décalage de la PMI de chaque colonne | | |
| Répartir les valeurs singulières d'une SVD tronquée entre deux facteurs, et démontrer ce qui dépend de ce choix (les angles entre lignes) et ce qui n'en dépend pas (le produit) | | |
| Calculer le logit de vraisemblance maximale d'un taux, et corriger par ln K un sous-échantillonnage d'une classe (formule de Bayes) | | |
| Mesurer le parallélogramme d'une analogie et expliquer, par une borne sur le cosinus, pourquoi on exclut les points de la question | | |
| Retirer d'un nuage une direction estimée, et dire quelles distances changent et lesquelles restent | | |
| Résumer des suites de vecteurs de longueurs différentes par une moyenne masquée, et comparer le coût des comparaisons par paires à celui d'un vecteur par élément | | |
<!-- wbm:end MB2 -->

<!-- wbm:section MB3 -->
## MB3 · Rotations, moyennes pondérées et softmax en ligne

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Démontrer les formules d'addition du cosinus et du sinus, et s'en servir pour des valeurs exactes, des duplications et des produits de cosinus | | |
| Composer et inverser des rotations du plan (R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}), et les lire comme des multiplications par e^{iθ} | | |
| Écrire une rotation de Givens de ℝⁿ, dire quand deux rotations commutent, et lire une matrice diagonale par blocs de rotations et ce qu'une permutation des coordonnées en change | | |
| Encoder une variable cyclique par (cos, sin), lire un décalage comme une rotation, et exprimer le produit scalaire de deux encodages à plusieurs horloges en fonction de l'écart | | |
| Calculer une moyenne pondérée par une softmax et l'estimateur de Nadaraya-Watson, et prévoir l'effet de la largeur de bande | | |
| Restreindre une moyenne pondérée à un sous-ensemble par un masque (une loi conditionnelle), et démontrer qu'une moyenne pondérée sur un ensemble est équivariante par permutation | | |
| Expliquer pourquoi l'on divise par √n une somme de n contributions indépendantes, et mesurer la saturation d'une softmax quand l'échelle des scores grandit | | |
| Calculer une softmax en ligne par blocs, démontrer son invariant, fusionner deux états partiels, et compter ce que coûtent toutes les paires | | |
<!-- wbm:end MB3 -->

<!-- wbm:section MB4 -->
## MB4 · Rang faible et recherche d'information

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Factoriser une matrice de rang r en un produit C F de r colonnes par r lignes, en trouver une autre, et compter les nombres stockés et les nombres libres | | |
| Démontrer que deux factorisations de rang diffèrent d'une matrice inversible, et que le rang est le plus petit nombre de produits extérieurs dont une matrice est la somme | | |
| Mesurer le rang effectif d'une matrice de mesures par l'énergie de ses valeurs singulières, et appliquer une matrice factorisée dans l'ordre le moins coûteux | | |
| Calculer le poids d'un indice rare comme une surprise et comme le log d'un rapport de cotes corrigé par ½, et dire quand il devient négatif | | |
| Étudier la saturation x ↦ x(k₁ + 1)/(x + k₁) et la normalisation par la longueur, et prévoir l'effet de k₁ et de b | | |
| Fusionner des classements par les rangs (Borda, somme des 1/(c + rang)), démontrer qu'ils ne dépendent pas de l'échelle des scores, et trouver quand une double présence bat une première place | | |
| Définir recall@k, precision@k, taux de succès et MRR, et calculer leur valeur moyenne pour un ordre tiré au hasard (k/n, H_n/n) | | |
<!-- wbm:end MB4 -->

<!-- wbm:section MB5 -->
## MB5 · Les maths de la diffusion

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer la loi de x_t sachant x_0 ou sachant x_s pour une récurrence linéaire gaussienne à coefficients quelconques, encadrer le produit cumulé de ses coefficients, et trouver la loi stationnaire d'un processus autorégressif d'ordre 1 | | |
| Calculer la loi d'un instant sachant deux instants qui l'encadrent (le pont d'une marche aléatoire), et construire des trajectoires différentes qui ont les mêmes lois marginales | | |
| Passer du rapport signal sur bruit à la part de variance du signal (cotes, logit, décibels), et d'une estimation du bruit à une estimation du signal, avec l'erreur qui l'accompagne | | |
| Démontrer que l'erreur quadratique moyenne est minimale pour l'espérance conditionnelle, et en lire les conséquences sur une cible à plusieurs modes | | |
| Définir le score en x d'une densité, démontrer la formule de Tweedie, calculer le débruiteur optimal d'un signal gaussien ou d'un mélange, et dire comment la dynamique de Langevin tire des points d'une densité à partir de son score | | |
| Démontrer la décomposition de l'ELBO d'une chaîne de latents en reconstruction, KL finale et KL des pas retour, et la calculer sur une petite chaîne discrète | | |
| Écrire une combinaison affine de scores comme le score d'un produit de puissances de densités, et calculer la loi guidée de deux gaussiennes avec sa condition d'existence | | |
| Suivre une équation différentielle par la méthode d'Euler et par celle du point milieu, dans les deux sens du temps, et relier l'erreur au pas et à la courbure de la trajectoire | | |
| Calculer le champ moyen d'un chemin droit entre un bruit et des données gaussiennes de dimension 1, et le suivre pour transporter le bruit sur la loi des données | | |
<!-- wbm:end MB5 -->

<!-- wbm:section MB6 -->
## MB6 · Shapley, intégrales de chemin et équité

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer la valeur de Shapley d'un petit jeu coopératif par les ordres d'arrivée et par les poids des coalitions, dire ce que coûte chaque méthode, et combien d'ordres tirés au hasard suffisent | | |
| Vérifier les quatre axiomes sur un jeu, calculer ses dividendes de Harsanyi et en déduire la valeur de Shapley ; démontrer qu'elle est la seule à respecter les quatre axiomes | | |
| Distinguer la moyenne marginale (dépendance partielle) et la moyenne conditionnelle d'une fonction, les calculer pour deux variables gaussiennes corrélées, et relier des courbes ICE parallèles à l'absence d'interaction | | |
| Calculer l'intégrale d'un champ de vecteurs le long d'une ligne brisée ou d'un arc, reconnaître un champ de gradient (indépendance du chemin, test de Schwarz), et partager une variation de f entre les coordonnées le long du segment ou par les chemins en escalier | | |
| Agrandir une grille par interpolation bilinéaire dans les deux conventions d'alignement, et lire la moyenne d'un gradient sur une grille comme une dérivée directionnelle | | |
| Calculer une corrélation de rangs de Spearman, ex aequo compris, et dire ce qu'elle ne voit pas | | |
| Écrire les critères d'équité comme des indépendances, et démontrer ce qui est incompatible quand les taux de base diffèrent, pour des décisions et pour des scores calibrés | | |
| Atteindre un taux de détection en tirant au sort entre deux seuils, repondérer une table pour rendre groupe et label indépendants, et donner l'intervalle de l'écart de deux taux | | |
<!-- wbm:end MB6 -->

<!-- wbm:section MB8 -->
## MB8 · Gradient de politique

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Calculer la fonction score d'une loi usuelle, vérifier qu'elle est d'espérance nulle, et calculer l'information de Fisher de deux façons | | |
| Dériver l'espérance d'une fonction, même discontinue, par rapport au paramètre d'une loi par la méthode du score, et dire quand la dérivée par le chemin est préférable | | |
| Réduire la variance d'une estimation de Monte-Carlo par une variable de contrôle, et calculer la baseline optimale d'un estimateur score | | |
| Distinguer une baseline sans biais (la moyenne des autres tirages) d'une baseline qui biaise (la moyenne du groupe, tirage compris) | | |
| Calculer le gradient de la valeur d'une politique softmax tabulaire par le système de Bellman, et l'écrire avec la loi d'occupation actualisée et l'avantage | | |
| Écrire un retour à k pas et un λ-retour, les relier aux erreurs TD, et calculer leur biais quand les valeurs estimées sont fausses | | |
| Estimer une espérance sous une loi à partir de tirages d'une autre, calculer la taille effective, tronquer des poids, et estimer une KL par k₁ ou k₃ | | |
| Ajuster un modèle de Bradley-Terry à un tournoi, dire quand ses forces existent et ce qu'elles identifient, et lire une mise à jour Elo comme un pas de gradient | | |
| Trouver la loi qui maximise une moyenne moins β fois la KL à une loi de référence, et sa valeur | | |
<!-- wbm:end MB8 -->

<!-- wbm:section PS -->
## PS · Projet de synthèse

| Compétence | Niveau (0 à 3) | Date |
|---|:-:|:-:|
| Choisir un algorithme de workbookIA et en dériver toutes les formules, de l'objectif jusqu'à ce que le code calcule, chaque étape justifiée par un résultat d'un chapitre de maths et chaque forme vérifiée | | |
| Démontrer deux propriétés de l'algorithme avec leurs hypothèses, et montrer ce qui se passe quand l'une d'elles tombe | | |
| L'implémenter avec ta librairie `mymath`, et le vérifier contre une bibliothèque indépendante par des tests qui attrapent de vraies erreurs | | |
| Rédiger un notebook-article qu'un relecteur peut suivre et vérifier, et le présenter en cinq minutes, comme en entretien | | |
<!-- wbm:end PS -->
