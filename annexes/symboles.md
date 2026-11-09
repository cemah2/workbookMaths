# Lire une formule : les symboles

Une formule se lit comme une phrase. Ce tableau donne, pour chaque symbole, **comment le lire à voix haute**, ce qu'il veut dire, un petit exemple, et le chapitre qui l'enseigne. Garde-le ouvert les premières semaines, et chaque fois que MML (en anglais) emploie une notation nouvelle. La colonne « en anglais » donne la lecture que tu entendras dans les vidéos et les cours. Les trois symboles dont le chapitre est M12c ($\det$, $\operatorname{tr}$, $\lambda$ valeur propre) arrivent avec la partie III ; ils sont là pour que tu les reconnaisses en lisant MML.

## Nombres et opérations

| Symbole | Se lit | En anglais | Signifie | Exemple | Chapitre |
|---|---|---|---|---|---|
| $=$, $\ne$ | « égale », « différent de » | equals, is not equal to | même valeur, valeurs différentes | $2 + 2 = 4$, $3 \ne 4$ | R1 |
| $\approx$ | « environ égal à » | approximately equal to | valeur approchée | $\pi \approx 3{,}14$ | R1 |
| $:=$ | « est défini comme » | is defined as | on donne un nom à une expression | $f(x) := x^2$ | R4 |
| $<$, $\le$ ($>$, $\ge$) | « strictement inférieur à », « inférieur ou égal à » (« supérieur ») | less than, less than or equal to (greater than) | comparaison | $2 \le 2$ est vrai, $2 < 2$ est faux | R2 |
| $\pm$ | « plus ou moins » | plus or minus | deux valeurs à la fois | $x = \pm 3$ : $x = 3$ ou $x = -3$ | R2 |
| $a^n$ | « a puissance n » | a to the power n | produit de $n$ facteurs égaux à $a$ | $5^3 = 125$ | R1 |
| $a^{-n}$ | « a puissance moins n » | a to the minus n | l'inverse de $a^n$ | $3^{-2} = \frac{1}{9}$ | R1 |
| $m \times 10^k$, `me k` | « m fois dix puissance k » | m times ten to the k | notation scientifique ; en Python `3.72e-5` | $3{,}72 \times 10^{-5}$ | R1 |
| $\sqrt{a}$ | « racine carrée de a » | square root of a | le nombre positif dont le carré vaut $a$ | $\sqrt{9} = 3$ | R1 |
| $\lvert x \rvert$ | « valeur absolue de x » | absolute value of x | $x$ sans son signe ; distance de $x$ à 0 | $\lvert -3 \rvert = 3$ | R2 |
| $\operatorname{sign}(x)$ | « signe de x » | sign of x | $-1$, 0 ou 1 selon le signe de $x$ ; $x = \operatorname{sign}(x) \lvert x \rvert$ | $\operatorname{sign}(-8) = -1$ | R2 |
| $\lfloor x \rfloor$, $\lceil x \rceil$ | « partie entière (inférieure, supérieure) de x » | floor, ceiling of x | arrondi vers le bas, vers le haut | $\lfloor 2{,}4 \rfloor = 2$, $\lceil 2{,}4 \rceil = 3$, $\lfloor -1{,}6 \rfloor = -2$ | R1 |
| $n!$ | « factorielle n » | n factorial | $1 \times 2 \times \dots \times n$ | $4! = 24$ | R8 |
| $\binom{n}{k}$ | « k parmi n » | n choose k | nombre de façons de choisir $k$ objets parmi $n$ | $\binom{4}{2} = 6$ | R8 |
| $\infty$ | « l'infini » | infinity | plus grand que tout nombre (pas un nombre) | $[2 ; +\infty[$, $x \to +\infty$ | R2, R5 |

## Sommes, produits, ensembles et logique

| Symbole | Se lit | En anglais | Signifie | Exemple | Chapitre |
|---|---|---|---|---|---|
| $\sum_{i=1}^{n} x_i$ | « somme pour i allant de 1 à n de x indice i » | sum over i from 1 to n | $x_1 + x_2 + \dots + x_n$ | $\sum_{i=1}^{3} i = 6$ | R4 |
| $\prod_{i=1}^{n} x_i$ | « produit pour i allant de 1 à n » | product over i | $x_1 \times x_2 \times \dots \times x_n$ | $\prod_{i=1}^{3} i = 6$ | R4 |
| $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{D}$, $\mathbb{Q}$, $\mathbb{R}$ | « N, Z, D, Q, R » | naturals, integers, decimals, rationals, reals | entiers naturels, relatifs, décimaux, rationnels, réels | $-2 \in \mathbb{Z}$, $-2 \notin \mathbb{N}$ | R1, R4 |
| $\in$, $\notin$ | « appartient à », « n'appartient pas à » | is in, is an element of | un élément dans un ensemble | $3 \in \{1, 2, 3\}$ | R4 |
| $\subset$ ou $\subseteq$ | « est inclus dans » | is a subset of | tous les éléments du premier sont dans le second | $\{1, 2\} \subset \{1, 2, 3\}$ | R4 |
| $A \cup B$, $A \cap B$ | « A union B », « A inter B » | union, intersection | dans l'un ou l'autre, dans les deux | $\{1,2\} \cap \{2,3\} = \{2\}$, $[0 ; 3] \cap [2 ; 5] = [2 ; 3]$ | R2, R4 |
| $\varnothing$ | « l'ensemble vide » | the empty set | aucun élément | $\{1\} \cap \{2\} = \varnothing$ | R2, R4 |
| $\bar{A}$, $A \setminus B$ | « complémentaire de A », « A privé de B » | complement of A, A minus B | les éléments de l'univers qui ne sont pas dans $A$ ; ceux de $A$ qui ne sont pas dans $B$ | $\{1, 2, 3\} \setminus \{2\} = \{1, 3\}$ | R4 |
| $\lvert A \rvert$ (ou $\operatorname{card} A$) | « cardinal de A » | cardinality of A | le nombre d'éléments d'un ensemble fini | $\lvert \{2, 4, 6\} \rvert = 3$ | R4 |
| $n!$ | « factorielle n » | n factorial | $n \times (n - 1) \times \cdots \times 1$, les rangements de $n$ objets ; $0! = 1$ | $3! = 6$ | R8 |
| $\binom{n}{k}$ (au lycée $C_n^k$) | « k parmi n » | n choose k | les façons de choisir $k$ objets parmi $n$, sans ordre | $\binom{9}{3} = 84$ | R8 |
| $A \times B$, $(a, b)$ | « A croix B », « le couple a, b » | Cartesian product, ordered pair | les couples $(a, b)$ avec $a \in A$ et $b \in B$ ; un couple est ordonné | $(1, 2) \ne (2, 1)$ | R4 |
| $\{x \in E \mid P(x)\}$ | « l'ensemble des x de E tels que P(x) » | the set of x in E such that P(x) | un ensemble décrit par une propriété (on écrit aussi « : » pour la barre) | $\{n \in \mathbb{N} \mid n < 3\} = \{0, 1, 2\}$ | R4 |
| $[a ; b]$, $]a ; b[$ | « intervalle fermé, ouvert, de a à b » | closed, open interval | les réels entre $a$ et $b$, bornes comprises ou non (en anglais : $[a, b]$, $(a, b)$) | $1 \in [1 ; 2]$, $1 \notin \,]1 ; 2]$ | R2 |
| $\forall$ | « pour tout » | for all | la propriété vaut pour chaque élément | $\forall x \in \mathbb{R},\ x^2 \ge 0$ | R4 |
| $\exists$ | « il existe » | there exists | au moins un élément vérifie la propriété | $\exists x \in \mathbb{R},\ x^2 = 2$ | R4 |
| $\Rightarrow$ | « implique », « donc » | implies | si la gauche est vraie, la droite aussi | $x = 2 \Rightarrow x^2 = 4$ | R4 |
| $\Leftrightarrow$ | « équivaut à », « si et seulement si » | if and only if (iff) | les deux sont vraies ou fausses ensemble (aussi $\iff$) | $2x = 6 \Leftrightarrow x = 3$ | R2, R4 |
| $\neg P$, $P \land Q$, $P \lor Q$ | « non P », « P et Q », « P ou Q » | not, and, or | les connecteurs logiques ; le « ou » est inclusif | $\neg(x > 2) \Leftrightarrow x \le 2$ | R4 |
| ∎ (ou □, CQFD) | « ce qu'il fallait démontrer » | QED, end of proof | la fin d'une démonstration | | R4 |

## Fonctions et analyse

| Symbole | Se lit | En anglais | Signifie | Exemple | Chapitre |
|---|---|---|---|---|---|
| $f : A \to B$ | « f va de A dans B » | f maps A to B | à chaque élément de $A$, $f$ associe un élément de $B$ | $f : \mathbb{R} \to \mathbb{R}$ | R3 |
| $x \mapsto x^2$ | « x a pour image x au carré » | x maps to x squared | la règle de la fonction | $f : x \mapsto x^2$ | R3 |
| $f \circ g$ | « f rond g » | f composed with g | appliquer $g$, puis $f$ : $(f \circ g)(x) = f(g(x))$ | $\sqrt{\cdot} \circ (x \mapsto x+1)$ | R3 |
| $\mathbb{R} \setminus \{a\}$ | « R privé de a » | R minus a | tous les réels sauf $a$ | $\mathbb{R} \setminus \{0\} = \,]-\infty ; 0[ \cup ]0 ; +\infty[$ | R3 |
| $f^{-1}$ | « f moins un », « réciproque de f » | inverse of f | la fonction qui défait $f$ (attention : pas $1/f$) | $\exp^{-1} = \ln$ | R3 |
| $e$, $\exp(x)$, $e^x$ | « e », « exponentielle de x » | e, exp of x | le nombre $e \approx 2{,}718$ et sa fonction puissance | $e^0 = 1$ | R6 |
| $\ln x$, $\log_2 x$ | « logarithme népérien », « log en base 2 » | natural log, log base 2 | l'exposant qu'il faut donner à $e$ (ou à 2) pour obtenir $x$ ; dans MML, $\log$ = $\ln$ | $\log_2 32 = 5$ | R6 |
| $\log_b x$, $\log_{10} x$ | « logarithme en base b de x », « log décimal » | log base b of x, common log | l'exposant qu'il faut donner à $b$ pour obtenir $x$ ; $\log_b x = \frac{\ln x}{\ln b}$ | $\log_{10} 100\,000 = 5$ | R6 |
| $\sigma(x)$ | « sigma de x », « sigmoïde de x » | sigmoid of x | $\frac{1}{1 + e^{-x}}$ ; ailleurs, $\sigma$ est aussi un écart-type | $\sigma(0) = \frac{1}{2}$ | R6 |
| $\tanh x$ | « tangente hyperbolique de x » | hyperbolic tangent, « tanch » | $\frac{e^x - e^{-x}}{e^x + e^{-x}}$ | $\tanh 0 = 0$ | R6 |
| $\lfloor x \rfloor$ | « partie entière de x » | floor of x | le plus grand entier inférieur ou égal à $x$ | $\lfloor 4{,}7 \rfloor = 4$ | R1, R6 |
| $u_n$, $(u_n)$ | « u indice n », « la suite u n » | u sub n, the sequence u_n | le terme de rang $n$ ; la suite entière | $u_n = n^2$ donne $u_3 = 9$ | R5 |
| $\lim_{n \to +\infty} u_n = \ell$, $u_n \to \ell$ | « limite de u n quand n tend vers plus l'infini », « u n tend vers ℓ » | limit of u_n as n tends to infinity | les termes finissent par rester aussi près de $\ell$ qu'on veut | $\lim_{n \to +\infty} \frac{1}{n} = 0$ | R5 |
| $\sum_{k=0}^{+\infty} u_k$ | « somme pour k allant de 0 à plus l'infini » | infinite sum, series | la limite des sommes partielles | $\sum_{k=0}^{+\infty} 0{,}6^k = 2{,}5$ | R5 |
| $\lim_{x \to a} f(x)$ | « limite de f(x) quand x tend vers a » | limit as x tends to a | la valeur dont $f(x)$ s'approche | $\lim_{x \to 2} (x^2 + 1) = 5$ | R7 |
| $\lim_{x \to a^+}$, $\lim_{x \to a^-}$ | « limite quand x tend vers a par la droite (par la gauche) » | right-hand (left-hand) limit | $x$ s'approche de $a$ en restant plus grand (plus petit) que $a$ | $\lim_{x \to 0^+} \frac{1}{x} = +\infty$ | R7 |
| $f'(x)$, $\frac{df}{dx}$ | « f prime de x », « d f sur d x » | f prime, df by dx | dérivée : la pente de la tangente | $(x^2)' = 2x$ | R7 |
| $f''(x)$, $\frac{d^2 f}{dx^2}$ | « f seconde de x », « d deux f sur d x deux » | f double prime, second derivative | la dérivée de $f'$ : son signe dit si la courbe est convexe ou concave | $(x^3)'' = 6x$ | M05a |
| $f^{(k)}(x)$ | « f indice k entre parenthèses », « dérivée k-ième de f » | k-th derivative of f | $f$ dérivée $k$ fois ; $f^{(0)} = f$ | $\sin^{(4)} = \sin$ | M05a |
| $P_n(x)$, $T_n(x)$ | « P n de x », « polynôme de Taylor d'ordre n » | Taylor polynomial of degree n | $\sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k$ | $e^x \approx 1 + x + \frac{x^2}{2}$ | M05a |
| $\text{fl}(x)$ | « flottant de x » | float of x | le flottant le plus proche de $x$, celui que la machine range | $\text{fl}(0{,}1) \ne 0{,}1$ | M05a |
| $\varepsilon$ (machine), $u$ | « epsilon machine », « unité d'arrondi » | machine epsilon, unit roundoff | l'écart entre 1 et le flottant suivant ; la moitié, l'erreur relative maximale d'une opération | $\varepsilon = 2^{-52}$ en `float64` | M05a |
| $\text{LSE}(\mathbf{v})$ | « log-sum-exp de v » | log-sum-exp of v | $\ln \sum_i e^{v_i}$, calculé comme $m + \ln\sum_i e^{v_i - m}$ avec $m = \max_i v_i$ | $\text{LSE}(0, 0) = \ln 2$ | M04, M05a |
| $\frac{\partial f}{\partial x}$ | « d rond f sur d rond x », « dérivée partielle de f par rapport à x » | partial f partial x | dérivée en $x$, les autres variables fixées | $\frac{\partial}{\partial x}(xy) = y$ | M05b |
| $\nabla f$ | « nabla f », « gradient de f » | gradient of f, del f | le vecteur des dérivées partielles | $\nabla (x^2 + y^2) = (2x, 2y)$ | M05b |
| $D_{\mathbf{u}} f(\mathbf{p})$ | « dérivée directionnelle de f en p dans la direction u » | directional derivative of f along u | la pente de $f$ en $\mathbf{p}$ dans la direction du vecteur unitaire $\mathbf{u}$ : $\nabla f(\mathbf{p}) \cdot \mathbf{u}$ | $\nabla f = (6, 9)$, $\mathbf{u} = (0{,}28 ;\ 0{,}96)$ : $10{,}32$ | M05b |
| $f_x$, $f_{xx}$, $f_{xy}$ | « f indice x », « f indice x x », « f indice x y » | f sub x, f sub xx, f sub xy | $\frac{\partial f}{\partial x}$ ; la dérivée de $f_x$ par rapport à $x$, puis par rapport à $y$ (dérivée croisée) | $x^3 y + 2y^2$ : $f_{xy} = 3x^2$ | M05b |
| $\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial y\,\partial x}$ | « d rond deux f sur d rond x deux », « d rond deux f sur d rond y d rond x » | second partial derivative | les mêmes dérivées secondes, $f_{xx}$ et $f_{xy}$, notées comme des fractions | $\frac{\partial^2}{\partial x^2}(x^3 y) = 6xy$ | M05b |
| $\int_a^b f(x)\,dx$ | « intégrale de a à b de f(x) d x » | integral from a to b of f | aire (signée) sous la courbe | $\int_0^1 x\,dx = \frac{1}{2}$ | M02a |
| $\int f(x)\,dx$ | « intégrale de f(x) d x », « primitive de f » | indefinite integral, antiderivative of f | une primitive quelconque, écrite avec une constante $+ C$ | $\int x^2\,dx = \frac{x^3}{3} + C$ | M02a |
| $\big[F(x)\big]_a^b$ | « F(x) pris entre a et b » | F evaluated from a to b | $F(b) - F(a)$, la borne du haut d'abord | $\big[x^2\big]_1^3 = 9 - 1 = 8$ | M02a |
| $\int_a^{+\infty} f(x)\,dx$ | « intégrale de a à plus l'infini » | improper integral to infinity | la limite de $\int_a^b f$ quand $b \to +\infty$ | $\int_1^{+\infty} \frac{dx}{x^2} = 1$ | M02a |
| $\propto$ | « proportionnel à » | proportional to | égal à une constante près | $p(\theta \mid x) \propto p(x \mid \theta)\,p(\theta)$ | M04 |
| $O(n^2)$ | « grand O de n carré » | big O of n squared | croît au plus comme $n^2$ | coût du produit de deux matrices $n \times n$ : $O(n^3)$ | R7 |
| $\arg\max_x f(x)$, $\arg\min_x f(x)$ | « argument du maximum (du minimum) de f » | arg max, arg min | la valeur de $x$ (pas la valeur de $f$) où $f$ est maximale (minimale) | $\arg\min_x (x-3)^2 = 3$ | R3, M04, M05b |
| $\cos\theta$, $\sin\theta$ | « cosinus de thêta », « sinus de thêta » | cosine, sine of theta | l'abscisse et l'ordonnée du point d'angle $\theta$ du cercle trigonométrique | $\cos\frac{\pi}{3} = \frac{1}{2}$ | R9 |
| $\cos^2\theta$ | « cosinus carré de thêta » | cos squared theta | $(\cos\theta)^2$ | $\cos^2\theta + \sin^2\theta = 1$ | R9 |
| $\arccos x$ | « arc cosinus de x » | arccosine of x | l'angle de $[0 ; \pi]$ dont le cosinus vaut $x$ | $\arccos 0 = \frac{\pi}{2}$ | R9 |
| rad, ° | « radian », « degré » | radian, degree | deux unités d'angle : $\pi$ rad $= 180°$ | $\frac{\pi}{4}$ rad $= 45°$ | R9 |
| $\hat{C}$ | « angle C » | angle C | l'angle d'un triangle au sommet $C$ | $c^2 = a^2 + b^2 - 2ab\cos\hat{C}$ | R9 |

## Vecteurs et matrices

| Symbole | Se lit | En anglais | Signifie | Exemple | Chapitre |
|---|---|---|---|---|---|
| $\mathbf{x}$ (gras) | « le vecteur x » | vector x | une liste de nombres (en colonne) | $\mathbf{x} = (1, 2)$ | R9, M07 |
| $\overrightarrow{AB}$, $\vec{u}$ | « vecteur A B », « vecteur u » | vector AB, vector u | le déplacement de $A$ vers $B$ : $(x_B - x_A ; y_B - y_A)$ | $A(-2 ; 1)$, $B(6 ; 16)$ : $\overrightarrow{AB} = (8 ; 15)$ | R9 |
| $M(x ; y)$ | « M de coordonnées x, y » | point M (x, y) | le point d'abscisse $x$ et d'ordonnée $y$ ; en Python, `(x, y)` | $O(0 ; 0)$, l'origine | R9 |
| $x_i$ | « x indice i » | x sub i | la $i$-ième composante de $\mathbf{x}$ | $x_2 = 2$ | R4 |
| $\mathbb{R}^n$ | « R n » | R n | les vecteurs à $n$ composantes réelles | $(1, 2, 3) \in \mathbb{R}^3$ | R9, M07 |
| $\lVert \mathbf{x} \rVert$ | « norme de x » | norm of x | longueur du vecteur | $\lVert (3, 4) \rVert = 5$ | R9, M07 |
| $\lVert \mathbf{x} \rVert_1$, $\lVert \mathbf{x} \rVert_\infty$ | « norme un de x », « norme infinie de x » | L1 norm, infinity norm | $\sum_i \lvert x_i \rvert$ ; $\max_i \lvert x_i \rvert$ | $\lVert (-6, 2) \rVert_1 = 8$ | R9, M07 |
| $\mathbf{x} \cdot \mathbf{y}$, $\langle \mathbf{x}, \mathbf{y} \rangle$ | « x scalaire y », « produit scalaire de x et y » | dot product, inner product | $\sum_i x_i y_i$ | $(1,2) \cdot (3,4) = 11$ | R9, M07 |
| $\perp$ | « orthogonal à », « perpendiculaire à » | orthogonal to, perpendicular to | de produit scalaire nul | $(3, -1) \perp (1, 3)$ | R9, M07 |
| $\langle \mathbf{x}, \mathbf{y} \rangle_{\mathbf{M}}$ | « produit scalaire de x et y pour M » | inner product defined by M | $\mathbf{x}^\top\mathbf{M}\mathbf{y}$, avec $\mathbf{M}$ symétrique définie positive | $\langle \mathbf{e}_1, \mathbf{e}_2 \rangle_{\mathbf{M}} = M_{12}$ | M12b |
| $U^\perp$ | « U orthogonal » | U perp, orthogonal complement of U | les vecteurs orthogonaux à tout $U$ | $\{\mathbf{0}\}^\perp = \mathbb{R}^n$ | M12b |
| $\pi_U(\mathbf{v})$ | « projeté de v sur U » | orthogonal projection of v onto U | le point de $U$ le plus proche de $\mathbf{v}$ | $\pi_U(\mathbf{v}) = \mathbf{Q}\mathbf{Q}^\top\mathbf{v}$ | M12b |
| $\mathbf{Q}\mathbf{Q}^\top$ | « Q Q transposée » | Q Q transpose | la matrice de projection sur l'espace des colonnes de $\mathbf{Q}$ (colonnes orthonormées) ; $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$ | $\frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ projette sur $\operatorname{Vect}\big((1, 1)\big)$ | M12b |
| $\mathbf{A} = \mathbf{Q}\mathbf{R}$ | « décomposition QR de A » | QR decomposition | $\mathbf{Q}$ à colonnes orthonormées, $\mathbf{R}$ triangulaire supérieure | $\begin{pmatrix} 5 \\ 12 \end{pmatrix} = \frac{1}{13}\begin{pmatrix} 5 \\ 12 \end{pmatrix}(13)$ | M12b |
| $\lVert \mathbf{x} \rVert_p$ | « norme p de x » | p-norm of x | $\big(\sum_i \lvert x_i \rvert^p\big)^{1/p}$, une norme pour $p \ge 1$ | $\lVert (1, -1) \rVert_4 = 2^{1/4}$ | M07 |
| $\mathbf{e}_i$ | « e i » | i-th standard basis vector | le vecteur de $\mathbb{R}^n$ qui a un 1 à la place $i$ et des 0 ailleurs | $\mathbf{e}_2 = (0, 1, 0)$ dans $\mathbb{R}^3$ | M07 |
| $\mathbf{0}$, $\mathbf{1}$ | « vecteur nul », « vecteur des uns » | zero vector, all-ones vector | le vecteur dont toutes les coordonnées valent 0, ou 1 | $\lVert \mathbf{1} \rVert = \sqrt{n}$ dans $\mathbb{R}^n$ | M07 |
| $\mathbf{x}^\top \mathbf{y}$ | « x transposé y » | x transpose y | le produit scalaire $\mathbf{x} \cdot \mathbf{y}$, écrit comme un produit de matrices (la notation de MML) | $(1, 2)^\top (3, 4) = 11$ | M07, M09a |
| $\bar{\mathbf{x}}$ | « x barre » (en gras) | centroid, mean vector | le barycentre d'un nuage de points, la moyenne coordonnée par coordonnée | le barycentre de $(0, 0)$ et $(2, 4)$ est $(1, 2)$ | M07 |
| $d(\mathbf{x}, H)$ | « distance de x à H » | distance from x to H | la distance d'un point à un hyperplan : $\frac{\lvert \mathbf{w} \cdot \mathbf{x} + b \rvert}{\lVert \mathbf{w} \rVert}$ | $d(\mathbf{0}, H) = \frac{\lvert b \rvert}{\lVert \mathbf{w} \rVert}$ | M07 |
| $a(i)$, $b(i)$, $s(i)$ | « a de i », « b de i », « silhouette de i » | silhouette components | les distances moyennes du point $i$ aux autres points de son cluster, et au cluster voisin ; sa silhouette $\frac{b - a}{\max(a, b)}$ | $s(i) < 0$ : mieux dans le cluster voisin | M07 |
| $\mathbf{A}$ (gras majuscule) | « la matrice A » | matrix A | un tableau de nombres | $\mathbf{A} \in \mathbb{R}^{2 \times 3}$ : 2 lignes, 3 colonnes | M09a |
| $\mathbf{A}^\top$ ou $\mathbf{A}^T$ | « A transposée » | A transpose | lignes et colonnes échangées | une forme $(2, 3)$ devient $(3, 2)$ | M09a |
| $\mathbf{A}\mathbf{B}$ | « A B », « produit de A par B » | matrix product | produit matriciel (l'ordre compte) | $(n, p) \times (p, m) \to (n, m)$ | M09a |
| $\odot$ | « produit terme à terme » | Hadamard product | multiplier élément par élément | $(1,2) \odot (3,4) = (3, 8)$ | M09a |
| $\mathbf{A}^{-1}$ | « A inverse » | A inverse | la matrice qui défait $\mathbf{A}$ : $\mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$ | l'inverse de $\operatorname{diag}(2, 4)$ est $\operatorname{diag}(0{,}5 ;\ 0{,}25)$ | M09a |
| $\mathbf{I}$, $\mathbf{I}_n$ | « la matrice identité (de taille n) » | identity matrix | des 1 sur la diagonale, 0 ailleurs | $\mathbf{I}_n\mathbf{A} = \mathbf{A}$ pour $\mathbf{A}$ à $n$ lignes | M09a |
| $a_{ij}$ | « a i j » | entry (i, j) | l'élément de la ligne $i$ et de la colonne $j$ (indices à partir de 1 ; `A[i - 1, j - 1]` en Python) | $a_{23}$ : ligne 2, colonne 3 | M09a |
| $\mathbb{R}^{m \times n}$, $(m, n)$ | « R m fois n », « forme m, n » | m by n matrices, shape | les matrices de $m$ lignes et $n$ colonnes ; leur forme, lignes d'abord | un dataset de 500 exemples à 12 features : $(500, 12)$ | M09a |
| $\operatorname{diag}(d_1, \ldots, d_n)$ | « diag d un… d n » | diagonal matrix | la matrice diagonale de diagonale $d_1, \ldots, d_n$ | $\operatorname{diag}(1, 1) = \mathbf{I}_2$ | M09a |
| $[\mathbf{A} \mid \mathbf{b}]$ | « A augmentée de b » | augmented matrix | la matrice des coefficients suivie de la colonne des seconds membres | $x - y = 1$, $3y = 6$ : $\left(\begin{array}{cc|c} 1 & -1 & 1 \\ 0 & 3 & 6 \end{array}\right)$ | M09a |
| $L_i \leftarrow L_i - \lambda L_j$ | « L i devient L i moins lambda L j » | row operation | remplacer la ligne $i$ par elle-même moins $\lambda$ fois la ligne $j$ (une opération élémentaire) | $L_2 \leftarrow L_2 - 2L_1$ | M09a |
| $\operatorname{rg}(\mathbf{A})$, $\operatorname{rk}(\mathbf{A})$ | « rang de A » | rank of A | le nombre de pivots, la dimension de l'espace des colonnes, au plus $\min(m, n)$ | $\operatorname{rg}(\mathbf{I}_3) = 3$ | M09a, M12a |
| $\nabla_{\mathbf{w}} f$ | « gradient de f par rapport à w » | gradient with respect to w | le vecteur des dérivées partielles de $f$ par rapport aux coordonnées de $\mathbf{w}$, de la forme de $\mathbf{w}$ | $\nabla_{\mathbf{w}}(\mathbf{a}^\top\mathbf{w}) = \mathbf{a}$ | M09b |
| $\hat{\mathbf{y}}$ | « y chapeau » (en gras) | fitted values, predictions | le vecteur des prédictions d'un modèle, $\mathbf{X}\mathbf{w}$ | $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$ | M09b |
| $\mathbf{H}$, $h_{ii}$ | « la matrice chapeau », « h i i » | hat matrix, leverage | $\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, la projection sur l'espace des colonnes de $\mathbf{X}$ ; ses nombres diagonaux sont les leviers | $\operatorname{tr}\mathbf{H} = p$ | M09b |
| $\operatorname{conv}(S)$ | « enveloppe convexe de S » | convex hull of S | le plus petit convexe qui contient $S$ | $\operatorname{conv}(\{0, 5\}) = [0, 5]$ | M10 |
| $\mathbf{u} \times \mathbf{v}$ (plan) | « u vectoriel v », « produit vectoriel de u et v » | cross product | $u_1v_2 - u_2v_1$, positif si l'on tourne à gauche | $(1, 0) \times (0, 1) = 1$ | M10 |
| $\tilde{\mathbf{x}}$, $\tilde{\mathbf{w}}$ | « x tilde », « w tilde » | x tilde, augmented vector | le vecteur augmenté de l'astuce du biais : $(1, \mathbf{x})$ et $(b, \mathbf{w})$ | $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}} = \mathbf{w} \cdot \mathbf{x} + b$ | M10 |
| $\gamma(\mathbf{w}, b)$, $\gamma^\star$ | « gamma de w et b », « gamma étoile » | margin, maximum margin | la marge géométrique d'un séparateur, la plus grande possible | $\gamma^\star = \frac{1}{2}\operatorname{dist}(\operatorname{conv} A, \operatorname{conv} B)$ | M10 |
| $\operatorname{Vect}(\mathbf{v}_1, \ldots, \mathbf{v}_k)$, $\operatorname{span}[\ldots]$ | « vect de v un, …, v k », « sous-espace engendré par… » | span of v one, …, v k | l'ensemble des combinaisons linéaires de ces vecteurs | $\operatorname{Vect}\big((1, 0, 0), (0, 1, 0)\big)$ : le plan $z = 0$ | M12a |
| $\dim V$ | « dimension de V » | dimension of V | le nombre de vecteurs d'une base de $V$ | $\dim\mathbb{R}^4 = 4$ | M12a |
| $\mathbb{R}_d[x]$ | « R d de x » | polynomials of degree at most d | les polynômes de degré au plus $d$, un espace de dimension $d + 1$ | $1 + 2x - x^2 \in \mathbb{R}_2[x]$ | M12a |
| $\ker f$, $\ker\mathbf{A}$ | « noyau de f » | kernel of f, null space | les vecteurs envoyés sur $\mathbf{0}$ | $\ker\begin{pmatrix} 1 & 1 \end{pmatrix} = \operatorname{Vect}\big((1, -1)\big)$ | M12a |
| $\operatorname{Im} f$, $\operatorname{Im}\mathbf{A}$ | « image de f » | image of f, range | les vecteurs atteints ; pour une matrice, l'espace de ses colonnes | $\operatorname{Im}\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ : l'axe des abscisses | M12a |
| $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ | « S moins un A S » | change of basis, similar matrix | la matrice de $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$ dans la base des colonnes de $\mathbf{S}$ (à lire de droite à gauche) | si $\mathbf{A}\mathbf{s}_1 = 2\,\mathbf{s}_1$, sa première colonne est $(2, 0, \ldots)$ | M12a |
| $\det(\mathbf{A})$, $\lvert\mathbf{A}\rvert$ | « déterminant de A » | determinant | facteur (signé) de changement d'aire ou de volume ; non nul si et seulement si $\mathbf{A}$ est inversible | $\det \mathbf{I} = 1$, $\det\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = -2$ | M12c |
| $\operatorname{tr}(\mathbf{A})$ | « trace de A » | trace | somme des éléments de la diagonale | $\operatorname{tr} \mathbf{I}_3 = 3$ | M12c |
| $\lambda$ | « lambda » | lambda | souvent une valeur propre (*eigenvalue*), ou la force d'une régularisation | $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$ | M12c |
| $p_{\mathbf{A}}(\lambda)$ | « p de A, de lambda » | characteristic polynomial of A | le polynôme caractéristique $\det(\mathbf{A} - \lambda\mathbf{I})$ | $p_{\mathbf{I}_2}(\lambda) = (1 - \lambda)^2$ | M12c |
| $\lambda_{\max}$, $\lambda_{\min}$ | « lambda max », « lambda min » | largest, smallest eigenvalue | la plus grande et la plus petite valeur propre d'une matrice symétrique | $\lambda_{\max}\big(\operatorname{diag}(3, 1)\big) = 3$ | M12c |
| $\boldsymbol{\Lambda}$, $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ | « grand lambda », « Q lambda Q transposée » | Lambda, eigendecomposition | la matrice diagonale des valeurs propres ; la décomposition spectrale d'une matrice symétrique | $\operatorname{diag}(4, 1)$ pour une matrice de valeurs propres 4 et 1 | M12c |
| $R(\mathbf{x})$ | « R de x », « quotient de Rayleigh » | Rayleigh quotient | $\frac{\mathbf{x}^\top\mathbf{A}\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}$ | $R(\mathbf{e}_1) = a_{11}$ | M12c |
| $\mathbf{A} \succ 0$, $\mathbf{A} \succeq 0$ | « A définie positive », « A semi-définie positive » | A is positive definite, positive semidefinite | $\mathbf{x}^\top\mathbf{A}\mathbf{x} > 0$ pour $\mathbf{x} \ne \mathbf{0}$ ; $\ge 0$ pour tout $\mathbf{x}$ | $\mathbf{I} \succ 0$ | M12c |
| $\mathbf{L}\mathbf{L}^\top$ | « L L transposée » | Cholesky factorization | la décomposition de Cholesky, $\mathbf{L}$ triangulaire inférieure à diagonale positive | $\begin{pmatrix} 16 & 8 \\ 8 & 13 \end{pmatrix} = \mathbf{L}\mathbf{L}^\top$, $\mathbf{L} = \begin{pmatrix} 4 & 0 \\ 2 & 3 \end{pmatrix}$ | M12c |
| $\mathbf{A}^{1/2}$, $\boldsymbol{\Sigma}^{-1/2}$ | « A puissance un demi », « sigma puissance moins un demi » | matrix square root, inverse square root | la racine carrée symétrique $\mathbf{Q}\boldsymbol{\Lambda}^{1/2}\mathbf{Q}^\top$, et son inverse, le blanchiment ZCA | $\operatorname{diag}(9, 4)^{1/2} = \operatorname{diag}(3, 2)$ | M12c |
| $\mathbf{U}\mathbf{S}\mathbf{V}^\top$, $s_i$ ($\sigma_i$) | « U S V transposée », « s indice i » (« sigma i ») | singular value decomposition, singular values | la SVD ; les valeurs singulières, notées $\sigma_i$ et la matrice $\boldsymbol{\Sigma}$ dans MML | $\operatorname{diag}(3, -5)$ a pour valeurs singulières 5 et 3 | M12d |
| $\mathbf{A}_k$ | « A indice k » | rank-k approximation of A | l'approximation de rang $k$, $\sum_{i \le k} s_i\mathbf{u}_i\mathbf{v}_i^\top$ | $\operatorname{diag}(3, 1)_1 = \operatorname{diag}(3, 0)$ | M12d |
| $\lVert \mathbf{A} \rVert_F$ | « norme de Frobenius de A » | Frobenius norm of A | $\sqrt{\sum_{i,j} a_{ij}^2} = \sqrt{\sum s_i^2}$ | $\lVert \mathbf{I}_4 \rVert_F = 2$ | M12d |
| $\lVert \mathbf{A} \rVert_2$ | « norme deux de A », « norme spectrale de A » | spectral norm of A | le plus grand étirement $\max \lVert \mathbf{A}\mathbf{x} \rVert/\lVert \mathbf{x} \rVert = s_1$ | $\lVert \operatorname{diag}(2, -7) \rVert_2 = 7$ | M12d |
| $\mathbf{A}^+$ | « A plus », « pseudo-inverse de A » | A plus, pseudo-inverse of A | $\sum_{i \le r}\frac{1}{s_i}\mathbf{v}_i\mathbf{u}_i^\top$, de forme $(n, m)$ | $\operatorname{diag}(2, 0)^+ = \operatorname{diag}(\frac{1}{2}, 0)$ | M12d |
| $\kappa(\mathbf{A})$ | « kappa de A » | condition number of A | le conditionnement $s_{\max}/s_{\min}$ | $\kappa\big(\operatorname{diag}(10, 0{,}1)\big) = 100$ | M12d |
| $\mathbf{X}_c$, $\mathbf{W}_k$, $\mathbf{Z}$, $t_{ij}$ | « X c », « W k », « Z », « t i j » | centered data, the first k principal axes, scores | les données centrées ; les $k$ premiers axes principaux en colonnes ; les scores $\mathbf{X}_c\mathbf{W}_k$, de terme $t_{ij} = \mathbf{u}_j^\top(\mathbf{x}_i - \boldsymbol{\mu})$ | $\hat{\mathbf{X}} = \mathbf{Z}\mathbf{W}_k^\top + \boldsymbol{\mu}$ | M12d |
| $p_{j \mid i}$, $p_{ij}$ | « p de j sachant i », « p i j » | conditional, joint neighbor probabilities | la probabilité que $\mathbf{x}_i$ choisisse $\mathbf{x}_j$ pour voisin (t-SNE) ; sa version symétrisée $\frac{p_{j \mid i} + p_{i \mid j}}{2n}$ | $\sum_{j \ne i} p_{j \mid i} = 1$ | M12d |

## Probabilités et statistique

| Symbole | Se lit | En anglais | Signifie | Exemple | Chapitre |
|---|---|---|---|---|---|
| $\Omega$ | « oméga », « l'univers » | sample space | l'ensemble des issues d'une expérience aléatoire | trois pièces : $\lvert \Omega \rvert = 8$ | R8 |
| $P(A)$ | « probabilité de A » | probability of A | entre 0 et 1 | $P(\text{pile}) = \frac{1}{2}$ | R8 |
| $P(A \mid B)$ (au lycée $P_B(A)$) | « probabilité de A sachant B » | probability of A given B | probabilité de $A$ quand on sait que $B$ s'est produit | la branche d'un arbre pondéré | R8, M03 |
| $P(A \cap B)$, $P(A, B)$ | « probabilité de A et B » | probability of A and B, joint probability | la probabilité que $A$ et $B$ se produisent ensemble | $P(\text{mobile}, \text{premium}) = 0{,}06$ | R8, M03 |
| $Y$, $\hat{Y}$ | « Y », « Y chapeau » | true label, predicted label | la vraie classe d'un exemple et la classe prédite par un modèle | recall $= P(\hat{Y} = 1 \mid Y = 1)$ | M03 |
| TP, FP, FN, TN | « vrais positifs, faux positifs, faux négatifs, vrais négatifs » | true / false positives / negatives | les quatre cases d'une matrice de confusion binaire | precision $= \frac{TP}{TP + FP}$ | M03 |
| $F_\beta$ | « F bêta » | F-beta score | moyenne harmonique pondérée de la precision et du recall | $F_1 = \frac{2PR}{P + R}$ | M03 |
| TPR, FPR | « taux de vrais positifs », « taux de faux positifs » | true / false positive rate | le recall, et $1 - $ spécificité : les deux axes de la courbe ROC | | M03 |
| $\pi$ (en classification) | « pi », « la prévalence » | prevalence, base rate | $P(Y = 1)$, la proportion de positifs (pas le nombre 3,14…) | precision $= \frac{r\pi}{r\pi + (1 - s)(1 - \pi)}$ | M03 |
| $X \sim \mathcal{N}(\mu, \sigma^2)$ | « X suit une loi normale de moyenne mu et de variance sigma carré » | X is distributed as a normal | la loi de la variable aléatoire $X$ | $\mathcal{N}(505, 5^2)$ : écart-type 5 | M02b |
| $\mathcal{B}(n, p)$, $\mathcal{P}(\lambda)$, $\mathcal{E}(\lambda)$, $\mathcal{U}([a ; b])$ | « binomiale n p », « Poisson lambda », « exponentielle lambda », « uniforme sur a b » | binomial, Poisson, exponential, uniform | les lois usuelles et leurs paramètres | $X \sim \mathcal{P}(3)$ : 3 événements en moyenne | M02b |
| $\varphi(z)$, $\Phi(z)$ | « phi de z », « grand phi de z » | standard normal pdf and cdf | la densité et la fonction de répartition de $\mathcal{N}(0, 1)$ | $\Phi(0) = \frac{1}{2}$, $\Phi(-z) = 1 - \Phi(z)$ | M02b |
| $P(X = x, Y = y)$ | « probabilité que X vaille x et Y vaille y » | joint probability | la loi jointe d'un couple, case par case | | M02b |
| $\iint_D f(x, y)\,dx\,dy$ | « intégrale double sur D de f » | double integral | le volume sous la surface $z = f(x, y)$, au-dessus de $D$ | $\iint_{[0 ; 2] \times [0 ; 1]} 1\,dx\,dy = 2$ | M02b |
| $F^{-1}(u)$ | « F moins un de u » | inverse cdf, quantile function | la valeur $x$ telle que $F(x) = u$ : le quantile d'ordre $u$ | | M02a, M02b |
| $p(x)$ | « p de x », « densité en x » | density (or pmf) at x | la loi d'une variable, point par point | | M02a, M02b |
| $F(x)$, $F_X(x)$ | « F de x », « fonction de répartition en x » | cdf at x | $P(X \le x)$, l'aire à gauche de $x$ sous la densité | $F(\text{médiane}) = \frac{1}{2}$ | M02a |
| $q_p$ | « quantile d'ordre p » | p-quantile | le plus petit $x$ tel que $F(x) \ge p$ ; $q_{0{,}5}$ est la médiane | percentile 90 : $q_{0{,}9}$ | M02a |
| $\mathbb{E}[X]$ | « espérance de X » | expected value of X | la moyenne théorique, pondérée par les probabilités | somme de deux dés à 4 faces : $\mathbb{E}[S] = 5$ | R8, M02b |
| $\mathbb{V}(X)$, $\operatorname{Var}(X)$ | « variance de X » | variance | dispersion autour de l'espérance | $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$ | R8, M02b |
| $\sigma(X)$ | « sigma de X », « écart-type de X » | standard deviation | la racine carrée de la variance, dans l'unité de $X$ | $\mathbb{V}(X) = 9$ donne $\sigma(X) = 3$ | R8 |
| $\operatorname{Cov}(X, Y)$ | « covariance de X et Y » | covariance | $\mathbb{E}[XY] - \mathbb{E}[X]\,\mathbb{E}[Y]$ : tendance à varier ensemble ; nulle pour des variables indépendantes | | M02b, M02c |
| $\hat{\theta}$ | « théta chapeau » | theta hat | une estimation de $\theta$ calculée sur des données (et $\hat{y}$, une prédiction) | $\hat{p} = \frac{360}{400}$, une accuracy | M02c |
| $\bar{x}$, $\bar{X}_n$ | « x barre », « X barre n » | x bar, sample mean | la moyenne de l'échantillon (une valeur) ; la moyenne de $n$ variables (une variable aléatoire) | $\mathbb{E}[\bar{X}_n] = \mu$ | M02c |
| $s_n^2$, $s^2$ | « s n carré », « s carré » | sample variance | la variance d'une série divisée par $n$, ou par $n - 1$ (sans biais) | $s^2 = \frac{n}{n - 1}s_n^2$ | M02c |
| $Q_1$, $Q_3$, EI | « premier quartile », « troisième quartile », « écart interquartile » | first and third quartiles, IQR | les quantiles d'ordre 0,25 et 0,75 d'une série, et leur écart | barrières de Tukey : $Q_1 - 1{,}5\,\text{EI}$ et $Q_3 + 1{,}5\,\text{EI}$ | M02c |
| $x_{(k)}$ | « x indice k entre parenthèses » | k-th order statistic | la $k$-ième valeur de la série triée (numérotée à partir de 0 dans le workbook) | $x_{(0)}$ est le minimum | M02c |
| SE | « erreur type » | standard error | l'écart-type d'un estimateur ; pour une moyenne, $\frac{s}{\sqrt{n}}$ | | M02c |
| $\rho(X, Y)$, $r$ | « rhô de X et Y », « r » | correlation | la corrélation de deux variables, ou de deux séries (coefficient de Pearson) | entre $-1$ et 1 | M02c |
| $\boldsymbol{\Sigma}$, $\Sigma_{ij}$ | « grand sigma (gras) », « sigma i j » | covariance matrix | la matrice de covariance, et sa case $(i, j)$ : $\operatorname{Cov}(X_i, X_j)$ | $\Sigma_{ii} = \mathbb{V}(X_i)$ | M02c |
| $\theta$ | « thêta » | theta | les paramètres d'un modèle | | M04 |
| $L(\theta)$, $\mathcal{L}(\theta)$ | « L de thêta », « vraisemblance » | likelihood | la probabilité des données observées, vue comme une fonction des paramètres | $L(\theta) = \theta^2(1 - \theta)^{10}$ | M04, M13a |
| $\ell(\theta)$ | « petit l de thêta », « log-vraisemblance » | log-likelihood | $\ln L(\theta)$ : même maximum que $L$, et une somme au lieu d'un produit | $\ell(\theta) = 2\ln\theta + 10\ln(1 - \theta)$ | M04 |
| $\hat{\theta}_{\text{MAP}}$ | « thêta chapeau MAP » | MAP estimate | le maximum de l'a posteriori, $\arg\max_\theta f(\theta \mid \text{données})$ | $\frac{3}{20}$ pour $\mathrm{Beta}(4, 18)$ | M04 |
| $\Gamma(x)$ | « gamma de x » | Gamma function | prolonge la factorielle : $\Gamma(n) = (n - 1)!$, $\Gamma(x + 1) = x\,\Gamma(x)$ | $\Gamma(5) = 24$ | M04 |
| $B(a, b)$ | « B de a, b », « fonction bêta » | Beta function | $\frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)} = \int_0^1 \theta^{a - 1}(1 - \theta)^{b - 1}\,d\theta$ | $B(3, 6) = \frac{1}{168}$ | M04 |
| $\Theta \sim \mathrm{Beta}(a, b)$ | « thêta suit une loi bêta a, b » | Beta distribution | une proportion de densité $\frac{\theta^{a - 1}(1 - \theta)^{b - 1}}{B(a, b)}$ sur $[0, 1]$ | $\mathrm{Beta}(1, 1)$ est uniforme | M04 |
| $H(X)$, $H(p)$ | « H de X », « entropie de p » | entropy of X, of p | l'incertitude moyenne d'une variable ou d'une loi, en bits (ou en nats) | $H\big(\frac{1}{2}, \frac{1}{2}\big) = 1$ bit | M06 |
| $H(X, Y)$ | « H de X, Y », « entropie conjointe de X et Y » | joint entropy of X and Y | l'entropie de la loi jointe du couple | $H(X, Y) \le H(X) + H(Y)$ | M06 |
| $H(Y \mid X)$ | « H de Y sachant X » | conditional entropy of Y given X | l'incertitude qui reste sur $Y$ quand on connaît $X$, en moyenne | 0 si $Y$ est une fonction de $X$ | M06 |
| $I(X ; Y)$ | « information mutuelle de X et Y » | mutual information of X and Y | ce que l'une des deux variables apprend sur l'autre | $I(X ; X) = H(X)$ | M06 |
| $H(p, q)$ | « cross-entropy de p et q » | cross-entropy of p and q | la longueur moyenne d'un code fait pour $q$, sur des données de loi $p$ | $H(p, p) = H(p)$ | M06 |
| $D_{\mathrm{KL}}(p \parallel q)$, $\mathrm{KL}(p \parallel q)$ | « divergence KL de p à q » | KL divergence of p from q | l'écart de $q$ à $p$, en bits perdus par symbole ; pas symétrique | $\mathrm{KL}(p \parallel p) = 0$ | M06 |
| $\mathrm{JS}(p, q)$ | « divergence de Jensen-Shannon de p et q » | Jensen-Shannon divergence | une divergence symétrique et toujours finie | $\mathrm{JS}(p, p) = 0$ | M06 |
| $\bar{L}$ | « L barre », « longueur moyenne » | expected (code) length | la longueur moyenne $\sum p_i \ell_i$ des mots d'un code | $\bar{L} \ge H$ pour un code préfixe | M06 |
| $H_0$, $H_1$ | « H zéro », « H un » | null hypothesis, alternative hypothesis | l'hypothèse nulle d'un test et son alternative | $H_0 : p = \frac{1}{2}$ | M08 |
| $\alpha$, $\beta$, $1 - \beta$ | « alpha », « bêta », « un moins bêta » | significance level, type II error rate, power | le risque de type I, le risque de type II, la puissance d'un test | $\alpha = 0{,}05$ | M08 |
| $z_{1-\alpha}$ | « z un moins alpha » | standard normal quantile | le quantile d'ordre $1 - \alpha$ de la loi normale centrée réduite : $\Phi(z_{1-\alpha}) = 1 - \alpha$ | $z_{0{,}975} \approx 1{,}96$ | M08 |
| $t_{n-1}$ | « t à n moins un degrés de liberté » | Student t quantile | un quantile de la loi de Student à $n - 1$ degrés de liberté (celui d'ordre 0,975 pour un intervalle à 95 %) | $t_4 \approx 2{,}776$ | M08 |
| $\mathrm{AIC}$, $\mathrm{BIC}$ | « A I C », « B I C » | Akaike, Bayesian information criterion | $2k - 2\ln L$ et $k\ln n - 2\ln L$ : le plus petit gagne | $k = 3$, $\ln L = -10$, $n = 50$ : $\mathrm{AIC} = 26$ | M08 |
| $\mathrm{BF}_{12}$ | « facteur de Bayes de 1 contre 2 » | Bayes factor | $\frac{p(\mathcal{D} \mid M_1)}{p(\mathcal{D} \mid M_2)}$, le rapport des évidences | $\mathrm{BF}_{12} = 3$ : les données favorisent $M_1$ | M08 |
| $R^2$ | « R deux » | R squared, coefficient of determination | $1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$, la part de la variation des cibles expliquée par le modèle | $R^2 = 0{,}8$ : 80 % de la variation expliquée | M09b |
| $\mathrm{SCT}$, $\mathrm{SCE}$, $\mathrm{SCR}$ | « somme des carrés totale, expliquée, résiduelle » | SST, SSE, SSR | les trois sommes de carrés d'un ajustement, autour de $\bar{y}$ | $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$ avec une colonne de 1 | M09b |
| $\ell_\delta(r)$ | « loss de Huber de r » | Huber loss | $\frac{r^2}{2}$ si $\lvert r \rvert \le \delta$, $\delta(\lvert r \rvert - \frac{\delta}{2})$ sinon | $\ell_1(3) = 2{,}5$ | M09b |
| $\mathbf{1}_{X \ge a}$, $\mathbf{1}_A$ | « indicatrice de X supérieur ou égal à a », « indicatrice de A » | indicator | la variable qui vaut 1 si l'événement a lieu et 0 sinon ; son espérance est sa probabilité | $a\,\mathbf{1}_{X \ge a} \le X$ pour $X \ge 0$ | M11 |
| $\delta$ (un risque) | « delta » | failure probability | le risque toléré d'un intervalle ou d'une borne de confiance, de niveau $1 - \delta$ | $\delta = 0{,}05$ : 95 % | M11 |
| $\mu^\star$, $\Delta_k$ | « mu étoile », « delta k » | best mean, gap | la meilleure moyenne parmi les options, et l'écart de l'option $k$ à elle | $\Delta_k = \mu^\star - \mu_k$ | M11 |
| $N_k(T)$ | « N k de T » | number of pulls of arm k | le nombre de fois que l'option $k$ a été choisie en $T$ pas | $\sum_k N_k(T) = T$ | M11 |
| $R_T$ | « R T », « regret après T pas » | regret | $\sum_k \Delta_k\,\mathbb{E}[N_k(T)]$ | linéaire en $T$ pour ε-greedy à ε fixé | M11 |

## Les lettres grecques

| Minuscule | Majuscule | Nom | Usage fréquent |
|:-:|:-:|---|---|
| $\alpha$ | | alpha | un niveau de test, un coefficient |
| $\beta$ | | bêta | un coefficient, le momentum et la moyenne exponentielle, la loi Beta |
| $\gamma$ | $\Gamma$ | gamma | le facteur d'actualisation en RL |
| $\delta$ | $\Delta$ | delta | une petite variation ($\Delta x$) |
| $\varepsilon$ | | epsilon | une petite quantité, un bruit, l'écart toléré dans la définition d'une limite |
| $\eta$ | | êta | le learning rate |
| $\theta$ | $\Theta$ | thêta | les paramètres d'un modèle |
| $\lambda$ | $\Lambda$ | lambda | une valeur propre, une régularisation |
| $\mu$ | | mu | une moyenne, une espérance |
| $\pi$ | $\Pi$ | pi | 3,14… ; une politique en RL ; $\Pi$ : un produit |
| $\rho$ | | rhô | une corrélation, le rayon spectral |
| $\sigma$ | $\Sigma$ | sigma | un écart-type, la sigmoïde ; $\Sigma$ : une somme ou une matrice de covariance |
| $\phi$ ou $\varphi$ | $\Phi$ | phi | une transformation des features ; $\Phi$ : la fonction de répartition de la loi normale |
| $\omega$ | $\Omega$ | oméga | un résultat d'une expérience ; $\Omega$ : l'univers |
