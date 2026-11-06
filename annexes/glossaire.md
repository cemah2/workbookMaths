# Glossaire français ↔ anglais

Les termes mathématiques sont en français dans les fiches, avec l'anglais en glose à leur première apparition : c'est l'anglais que tu liras dans MML. Les termes du machine learning gardent l'usage de workbookIA (loss, learning rate, batch, feature… restent en anglais). Chaque chapitre ajoute ses termes ; la colonne « Chapitre » renvoie à celui qui le définit.

| Français | Anglais | Définition courte | Chapitre |
|---|---|---|---|
| antécédent, image | preimage, image | $f(x)$ est l'image de $x$ ; un antécédent de $y$ est un $x$ tel que $f(x) = y$ | R3 |
| application linéaire | linear map, linear mapping | fonction entre espaces vectoriels qui respecte sommes et multiplications par un nombre | M12a |
| argmax, argmin | argmax, argmin | la valeur de $x$ où une fonction atteint son maximum (son minimum), pas la valeur de ce maximum | R3, M05b |
| arrondi, troncature | rounding, truncation | arrondir garde le nombre le plus proche ; tronquer coupe sans regarder la suite | R1 |
| base (d'un espace vectoriel) | basis | famille de vecteurs indépendants qui engendre tout l'espace | M12a |
| biais (d'un neurone) | bias | nombre $b$ ajouté à la somme pondérée d'un neurone, appris comme les poids | R1 |
| borne, intervalle | bound, interval | ensemble des réels compris entre deux bornes, incluses (crochet fermé) ou non (crochet ouvert) ; une borne peut être infinie | R2 |
| calcul symbolique | symbolic computation | calcul exact sur des expressions avec des lettres (SymPy), sans valeurs approchées | R0 |
| cellule (d'un notebook) | cell | bloc de code ou de texte qu'on exécute d'un coup | R0 |
| chiffres significatifs | significant figures | les chiffres d'un nombre à partir du premier chiffre non nul | R1 |
| coefficient | coefficient | nombre qui multiplie la partie littérale d'un terme : 7 dans $7x^2$ | R2 |
| coefficient multiplicateur | multiplier, growth factor | nombre $1 + t$ par lequel une évolution de taux $t$ multiplie une valeur | R1 |
| combinaison linéaire | linear combination | somme de vecteurs multipliés par des nombres | M12a |
| composée (de deux fonctions) | composition, composite function | $(f \circ g)(x) = f(g(x))$ : on applique $g$, puis $f$ | R3 |
| convexe | convex | dont tout segment entre deux points reste au-dessus de la courbe (fonction) ou dans l'ensemble | M05a, M10 |
| courbe représentative | graph (of a function) | l'ensemble des points $(x, f(x))$ | R3 |
| croissante, décroissante | increasing, decreasing | qui conserve (retourne) l'ordre sur un intervalle : $a < b \Rightarrow f(a) \le f(b)$ ($\ge$) | R3 |
| densité de probabilité | probability density function (pdf) | fonction dont l'aire sous la courbe donne une probabilité | M02a |
| dérivée | derivative | pente de la tangente, taux de variation instantané | R7 |
| dérivée partielle | partial derivative | dérivée par rapport à une variable, les autres fixées | M05b |
| déterminant | determinant | le nombre $ad - bc$ d'un système 2 × 2, non nul exactement quand il a une seule solution (R2) ; facteur de changement d'aire ou de volume d'une application linéaire (M12c) | R2, M12c |
| développer, factoriser | expand, factor | transformer un produit en somme ; transformer une somme en produit | R2 |
| discriminant | discriminant | $\Delta = b^2 - 4ac$ ; son signe donne le nombre de racines de $ax^2 + bx + c$ | R3 |
| division euclidienne | Euclidean division, integer division | $a = bq + r$ avec $0 \le r < b$ ; en Python, `a // b` donne $q$ et `a % b` donne $r$ | R0 |
| écart-type | standard deviation | racine carrée de la variance | R8 |
| empreinte | hash | code calculé à partir d'une donnée, d'où l'on ne peut pas la retrouver ; sert à comparer sans stocker | R0 |
| ensemble | set | collection d'éléments distincts | R4 |
| ensemble de définition | domain | l'ensemble des $x$ pour lesquels $f(x)$ a un sens | R3 |
| ensemble des solutions | solution set | l'ensemble de toutes les valeurs qui rendent une équation (ou une inéquation) vraie | R2 |
| entier naturel, entier relatif | natural number, integer | ℕ = {0, 1, 2…} ; ℤ ajoute les entiers négatifs | R1 |
| équation | equation | égalité qui contient une inconnue ; la résoudre, c'est trouver toutes ses solutions | R2 |
| équations équivalentes | equivalent equations | équations qui ont exactement les mêmes solutions | R2 |
| espace vectoriel | vector space | ensemble où l'on peut additionner des vecteurs et les multiplier par des nombres | M12a |
| espérance | expected value, expectation | moyenne théorique d'une variable aléatoire | R8 |
| estimateur | estimator | formule qui estime un paramètre à partir de données | M02c |
| estimation de Fermi | Fermi estimate | ordre de grandeur obtenu en découpant une question en facteurs faciles à estimer | R1 |
| exposant | exponent | le nombre $n$ de $a^n$ ; en notation scientifique, la puissance de 10 | R1 |
| expression littérale, variable | algebraic expression, variable | expression où des lettres, les variables, représentent des nombres | R2 |
| flottant (nombre à virgule flottante) | floating-point number, float | nombre à virgule rangé avec un nombre fixe de chiffres binaires, donc souvent arrondi | R0 |
| fonction | function | règle qui associe à chaque élément de son ensemble de définition une seule image | R3 |
| fonction affine, linéaire | affine function, linear function | $x \mapsto mx + c$ ; linéaire quand $c = 0$ | R3 |
| fonction de répartition | cumulative distribution function (cdf) | $F(x) = P(X \le x)$ | M02a |
| fonction définie par morceaux | piecewise function | une formule sur chaque partie de l'ensemble de définition : $\max(0, x)$, la marche, $\lvert x \rvert$ | R3 |
| fonction signe | sign function | $\operatorname{sign}(x)$ vaut $-1$, 0 ou 1 selon que $x$ est négatif, nul ou positif | R2 |
| forme canonique | vertex form, completed-square form | $a(x - \alpha)^2 + \beta$, qui montre le sommet d'une parabole | R3 |
| formule de Cramer | Cramer's rule | la solution d'un système de déterminant non nul, écrite comme quotients de déterminants | R2 |
| fraction irréductible | irreducible fraction, fraction in lowest terms | fraction dont numérateur et dénominateur n'ont plus d'autre diviseur commun que 1 | R1 |
| gradient | gradient | vecteur des dérivées partielles | M05b |
| hessienne | Hessian | matrice des dérivées secondes | M19 |
| identité remarquable | special product, algebraic identity | égalité vraie pour tous $a$ et $b$, comme $(a + b)^2 = a^2 + 2ab + b^2$ | R2 |
| inégalité, inéquation | inequality | comparaison avec $<$, $\le$, $>$ ou $\ge$ ; une inéquation est une inégalité qui contient une inconnue | R2 |
| intégrale | integral | aire signée sous une courbe | M02a |
| intersection, réunion | intersection, union | $A \cap B$ : les éléments à la fois dans $A$ et dans $B$ ; $A \cup B$ : ceux qui sont dans l'un ou dans l'autre | R2, R4 |
| jacobienne | Jacobian | matrice des dérivées partielles d'une fonction à valeurs vectorielles | M17 |
| loi (de probabilité) | (probability) distribution | façon dont une variable aléatoire répartit ses valeurs | R8, M02b |
| loi normale (gaussienne) | normal (Gaussian) distribution | loi en cloche, $\mathcal{N}(\mu, \sigma^2)$ | M02b |
| mal conditionné | ill-conditioned | se dit d'un problème dont la solution change beaucoup quand les données changent un peu | R2 |
| mantisse | significand, mantissa | le nombre $m$ de la notation scientifique $m \times 10^k$, avec $1 \le |m| < 10$ | R1 |
| marche (fonction de Heaviside) | step function, Heaviside function | vaut 0 avant 0 et 1 après ; la valeur en 0 est une convention | R3 |
| matrice | matrix | tableau de nombres à lignes et colonnes | M09a |
| maximum, minimum, extremum | maximum, minimum, extremum (extrema) | la plus grande (petite) valeur d'une fonction sur un ensemble | R3 |
| mise en équation | setting up an equation, translating a word problem | traduire un énoncé en équation (ou en système) en choisissant les inconnues | R2 |
| moindres carrés | least squares | méthode qui minimise la somme des carrés des écarts | M09b |
| moyenne harmonique | harmonic mean | inverse de la moyenne des inverses ; vitesse moyenne, score F1 | R1 |
| moyenne pondérée | weighted mean, weighted average | $\frac{\sum w_i x_i}{\sum w_i}$ : chaque valeur compte selon son poids | R1 |
| nombre décimal | decimal number, terminating decimal | nombre qui s'écrit avec un nombre fini de chiffres après la virgule (ensemble 𝔻) | R1 |
| nombre rationnel, irrationnel | rational, irrational number | quotient de deux entiers (ℚ) ; un réel qui n'en est pas un, comme $\sqrt{2}$ ou $\pi$ | R1 |
| normalisation min-max | min-max scaling | la fonction affine $\frac{x - \min}{\max - \min}$, qui ramène des données entre 0 et 1 | R3 |
| norme | norm | longueur d'un vecteur | R9, M07 |
| noyau (d'un notebook) | kernel | la mémoire qui exécute les cellules et garde leurs variables | R0 |
| noyau (d'une application linéaire) | kernel, null space | vecteurs envoyés sur zéro | M12a |
| numérateur, dénominateur | numerator, denominator | le nombre du haut et celui du bas d'une fraction | R1 |
| octet | byte | 8 bits ; 1 ko = $10^3$ octets, 1 Mo = $10^6$, 1 Go = $10^9$ | R1 |
| oracle (d'un test) | test oracle | bibliothèque de confiance à laquelle un test compare ta fonction | R0 |
| ordre de grandeur | order of magnitude | la puissance de 10 la plus proche d'un nombre | R1 |
| parabole, sommet | parabola, vertex | la courbe d'un second degré ; son sommet $(\alpha, \beta)$ est son point le plus bas (ou le plus haut) | R3 |
| partie entière, plancher, plafond | floor, ceiling | $\lfloor x \rfloor$, le plus grand entier $\le x$ ; $\lceil x \rceil$, le plus petit entier $\ge x$ | R1 |
| pente, ordonnée à l'origine | slope, intercept | dans $mx + c$, $m$ est la variation pour $x + 1$, et $c = f(0)$ | R3 |
| PGCD, PPCM | GCD (greatest common divisor), LCM (least common multiple) | plus grand diviseur commun, plus petit multiple commun de deux entiers | R1 |
| point de pourcentage | percentage point | écart entre deux pourcentages, obtenu en les soustrayant (de 4 % à 5 % : un point) | R1 |
| polynôme, degré | polynomial, degree | somme de puissances entières de $x$ multipliées par des coefficients ; le degré est la plus grande puissance | R3 |
| probabilité conditionnelle | conditional probability | $P(A \mid B)$ | M03 |
| produit nul (règle du) | zero-product property | un produit est nul si et seulement si l'un au moins de ses facteurs est nul | R2 |
| produit scalaire | dot product, inner product | $\sum_i x_i y_i$ ; mesure d'alignement de deux vecteurs | R9, M07 |
| puissance | power | $a^n$, produit de $n$ facteurs égaux à $a$ | R1 |
| quotient, reste | quotient, remainder | les deux résultats de la division euclidienne | R0 |
| racine (d'une fonction) | root, zero | un $x$ tel que $f(x) = 0$ | R3 |
| racine carrée | square root | nombre positif ou nul dont le carré vaut $a$ | R1 |
| rang | rank | nombre de directions indépendantes d'une matrice | M12a |
| réciproque (fonction) | inverse function | la fonction $f^{-1}$ qui défait $f$ : $f^{-1}(f(x)) = x$ ; ce n'est pas $\frac{1}{f}$ | R3 |
| récurrence (raisonnement par) | (proof by) induction | démontrer pour 0, puis de $n$ à $n+1$ | R4 |
| schéma de Horner | Horner's method | évaluer un polynôme en multipliant par $x$ et en ajoutant le coefficient suivant, sans puissances | R3 |
| second degré (polynôme du) | quadratic (polynomial, function) | $ax^2 + bx + c$ avec $a \ne 0$ | R3 |
| somme pondérée | weighted sum | $\sum w_i x_i + b$, sans division ; le calcul d'un neurone | R1 |
| substituer | substitute, plug in | remplacer une lettre par une valeur (ou par une expression) | R2 |
| suite | sequence | liste infinie de nombres $u_0, u_1, \dots$ | R5 |
| système linéaire | system of linear equations, linear system | plusieurs équations du premier degré à résoudre ensemble ; leurs solutions communes | R2 |
| taux d'évolution | rate of change, percentage change | $\frac{V_a - V_d}{V_d}$, la variation rapportée à la valeur de départ | R1 |
| termes semblables, réduire | like terms, collect like terms | termes de même partie littérale ; réduire, c'est les additionner en additionnant leurs coefficients | R2 |
| valeur absolue | absolute value | $\lvert x \rvert$, le nombre sans son signe ; $\lvert a - b \rvert$ est la distance entre $a$ et $b$ | R2 |
| valeur interdite | excluded value | valeur de l'inconnue qui annule un dénominateur | R2 |
| valeur propre, vecteur propre | eigenvalue, eigenvector | $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ : une direction que $\mathbf{A}$ ne fait qu'étirer | M12c |
| variable aléatoire | random variable | grandeur dont la valeur dépend du hasard | R8 |
| variance | variance | moyenne des carrés des écarts à l'espérance | R8 |
| vraisemblance | likelihood | probabilité des données, vue comme fonction des paramètres | M04 |
