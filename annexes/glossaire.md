# Glossaire français ↔ anglais

Les termes mathématiques sont en français dans les fiches, avec l'anglais en glose à leur première apparition : c'est l'anglais que tu liras dans MML. Les termes du machine learning gardent l'usage de workbookIA (loss, learning rate, batch, feature… restent en anglais). Chaque chapitre ajoute ses termes ; la colonne « Chapitre » renvoie à celui qui le définit.

| Français | Anglais | Définition courte | Chapitre |
|---|---|---|---|
| application linéaire | linear map, linear mapping | fonction entre espaces vectoriels qui respecte sommes et multiplications par un nombre | M12a |
| base (d'un espace vectoriel) | basis | famille de vecteurs indépendants qui engendre tout l'espace | M12a |
| borne, intervalle | bound, interval | | R2 |
| calcul symbolique | symbolic computation | calcul exact sur des expressions avec des lettres (SymPy), sans valeurs approchées | R0 |
| cellule (d'un notebook) | cell | bloc de code ou de texte qu'on exécute d'un coup | R0 |
| combinaison linéaire | linear combination | somme de vecteurs multipliés par des nombres | M12a |
| convexe | convex | dont tout segment entre deux points reste au-dessus de la courbe (fonction) ou dans l'ensemble | M05a, M10 |
| densité de probabilité | probability density function (pdf) | fonction dont l'aire sous la courbe donne une probabilité | M02a |
| dérivée | derivative | pente de la tangente, taux de variation instantané | R7 |
| dérivée partielle | partial derivative | dérivée par rapport à une variable, les autres fixées | M05b |
| déterminant | determinant | facteur de changement d'aire ou de volume d'une application linéaire | M12c |
| division euclidienne | Euclidean division, integer division | $a = bq + r$ avec $0 \le r < b$ ; en Python, `a // b` donne $q$ et `a % b` donne $r$ | R0 |
| écart-type | standard deviation | racine carrée de la variance | R8 |
| empreinte | hash | code calculé à partir d'une donnée, d'où l'on ne peut pas la retrouver ; sert à comparer sans stocker | R0 |
| ensemble | set | collection d'éléments distincts | R4 |
| espace vectoriel | vector space | ensemble où l'on peut additionner des vecteurs et les multiplier par des nombres | M12a |
| espérance | expected value, expectation | moyenne théorique d'une variable aléatoire | R8 |
| estimateur | estimator | formule qui estime un paramètre à partir de données | M02c |
| flottant (nombre à virgule flottante) | floating-point number, float | nombre à virgule rangé avec un nombre fixe de chiffres binaires, donc souvent arrondi | R0 |
| fonction de répartition | cumulative distribution function (cdf) | $F(x) = P(X \le x)$ | M02a |
| gradient | gradient | vecteur des dérivées partielles | M05b |
| hessienne | Hessian | matrice des dérivées secondes | M19 |
| inégalité | inequality | | R2 |
| intégrale | integral | aire signée sous une courbe | M02a |
| jacobienne | Jacobian | matrice des dérivées partielles d'une fonction à valeurs vectorielles | M17 |
| loi (de probabilité) | (probability) distribution | façon dont une variable aléatoire répartit ses valeurs | R8, M02b |
| loi normale (gaussienne) | normal (Gaussian) distribution | loi en cloche, $\mathcal{N}(\mu, \sigma^2)$ | M02b |
| matrice | matrix | tableau de nombres à lignes et colonnes | M09a |
| moindres carrés | least squares | méthode qui minimise la somme des carrés des écarts | M09b |
| norme | norm | longueur d'un vecteur | R9, M07 |
| noyau (d'un notebook) | kernel | la mémoire qui exécute les cellules et garde leurs variables | R0 |
| noyau (d'une application linéaire) | kernel, null space | vecteurs envoyés sur zéro | M12a |
| oracle (d'un test) | test oracle | bibliothèque de confiance à laquelle un test compare ta fonction | R0 |
| probabilité conditionnelle | conditional probability | $P(A \mid B)$ | M03 |
| produit scalaire | dot product, inner product | $\sum_i x_i y_i$ ; mesure d'alignement de deux vecteurs | R9, M07 |
| quotient, reste | quotient, remainder | les deux résultats de la division euclidienne | R0 |
| rang | rank | nombre de directions indépendantes d'une matrice | M12a |
| récurrence (raisonnement par) | (proof by) induction | démontrer pour 0, puis de $n$ à $n+1$ | R4 |
| suite | sequence | liste infinie de nombres $u_0, u_1, \dots$ | R5 |
| valeur propre, vecteur propre | eigenvalue, eigenvector | $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ : une direction que $\mathbf{A}$ ne fait qu'étirer | M12c |
| variable aléatoire | random variable | grandeur dont la valeur dépend du hasard | R8 |
| variance | variance | moyenne des carrés des écarts à l'espérance | R8 |
| vraisemblance | likelihood | probabilité des données, vue comme fonction des paramètres | M04 |
