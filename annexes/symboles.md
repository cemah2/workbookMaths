# Lire une formule : les symboles

Une formule se lit comme une phrase. Ce tableau donne, pour chaque symbole, **comment le lire à voix haute**, ce qu'il veut dire, un petit exemple, et le chapitre qui l'enseigne. Garde-le ouvert les premières semaines, et chaque fois que MML (en anglais) emploie une notation nouvelle. La colonne « en anglais » donne la lecture que tu entendras dans les vidéos et les cours.

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
| $\frac{\partial f}{\partial x}$ | « d rond f sur d rond x », « dérivée partielle de f par rapport à x » | partial f partial x | dérivée en $x$, les autres variables fixées | $\frac{\partial}{\partial x}(xy) = y$ | M05b |
| $\nabla f$ | « nabla f », « gradient de f » | gradient of f, del f | le vecteur des dérivées partielles | $\nabla (x^2 + y^2) = (2x, 2y)$ | M05b |
| $\int_a^b f(x)\,dx$ | « intégrale de a à b de f(x) d x » | integral from a to b of f | aire (signée) sous la courbe | $\int_0^1 x\,dx = \frac{1}{2}$ | M02a |
| $\propto$ | « proportionnel à » | proportional to | égal à une constante près | $p(\theta \mid x) \propto p(x \mid \theta)\,p(\theta)$ | M04 |
| $O(n^2)$ | « grand O de n carré » | big O of n squared | croît au plus comme $n^2$ | coût du produit de deux matrices $n \times n$ : $O(n^3)$ | R7 |
| $\arg\max_x f(x)$, $\arg\min_x f(x)$ | « argument du maximum (du minimum) de f » | arg max, arg min | la valeur de $x$ (pas la valeur de $f$) où $f$ est maximale (minimale) | $\arg\min_x (x-3)^2 = 3$ | R3, M05b |

## Vecteurs et matrices

| Symbole | Se lit | En anglais | Signifie | Exemple | Chapitre |
|---|---|---|---|---|---|
| $\mathbf{x}$ (gras) | « le vecteur x » | vector x | une liste de nombres (en colonne) | $\mathbf{x} = (1, 2)$ | R9, M07 |
| $x_i$ | « x indice i » | x sub i | la $i$-ième composante de $\mathbf{x}$ | $x_2 = 2$ | R4 |
| $\mathbb{R}^n$ | « R n » | R n | les vecteurs à $n$ composantes réelles | $(1, 2, 3) \in \mathbb{R}^3$ | M07 |
| $\lVert \mathbf{x} \rVert$ | « norme de x » | norm of x | longueur du vecteur | $\lVert (3, 4) \rVert = 5$ | R9, M07 |
| $\mathbf{x} \cdot \mathbf{y}$, $\langle \mathbf{x}, \mathbf{y} \rangle$ | « x scalaire y », « produit scalaire de x et y » | dot product, inner product | $\sum_i x_i y_i$ | $(1,2) \cdot (3,4) = 11$ | R9, M07 |
| $\mathbf{A}$ (gras majuscule) | « la matrice A » | matrix A | un tableau de nombres | | M09a |
| $\mathbf{A}^\top$ ou $\mathbf{A}^T$ | « A transposée » | A transpose | lignes et colonnes échangées | | M09a |
| $\mathbf{A}\mathbf{B}$ | « A B », « produit de A par B » | matrix product | produit matriciel (l'ordre compte) | | M09a |
| $\odot$ | « produit terme à terme » | Hadamard product | multiplier élément par élément | $(1,2) \odot (3,4) = (3, 8)$ | M09a |
| $\mathbf{A}^{-1}$ | « A inverse » | A inverse | la matrice qui défait $\mathbf{A}$ : $\mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$ | | M09a |
| $\mathbf{I}$ | « la matrice identité » | identity matrix | des 1 sur la diagonale, 0 ailleurs | | M09a |
| $\det(\mathbf{A})$ | « déterminant de A » | determinant | facteur de changement d'aire (ou de volume) | $\det \mathbf{I} = 1$ | M12c |
| $\operatorname{tr}(\mathbf{A})$ | « trace de A » | trace | somme des éléments de la diagonale | $\operatorname{tr} \mathbf{I}_3 = 3$ | M12c |
| $\lambda$ | « lambda » | lambda | souvent une valeur propre (*eigenvalue*), ou la force d'une régularisation | $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$ | M12c |

## Probabilités et statistique

| Symbole | Se lit | En anglais | Signifie | Exemple | Chapitre |
|---|---|---|---|---|---|
| $P(A)$ | « probabilité de A » | probability of A | entre 0 et 1 | $P(\text{pile}) = \frac{1}{2}$ | R8 |
| $P(A \mid B)$ | « probabilité de A sachant B » | probability of A given B | probabilité de $A$ quand on sait que $B$ s'est produit | | M03 |
| $X \sim \mathcal{N}(\mu, \sigma^2)$ | « X suit une loi normale de moyenne mu et de variance sigma carré » | X is distributed as a normal | la loi de la variable aléatoire $X$ | | M02b |
| $p(x)$ | « p de x », « densité en x » | density (or pmf) at x | la loi d'une variable, point par point | | M02a, M02b |
| $\mathbb{E}[X]$ | « espérance de X » | expected value of X | la moyenne théorique | dé : $\mathbb{E}[X] = 3{,}5$ | R8, M02b |
| $\mathbb{V}[X]$, $\operatorname{Var}(X)$ | « variance de X » | variance | dispersion autour de l'espérance | | R8, M02b |
| $\operatorname{Cov}(X, Y)$ | « covariance de X et Y » | covariance | tendance à varier ensemble | | M02c |
| $\hat{\theta}$ | « théta chapeau » | theta hat | une estimation de $\theta$ calculée sur des données (et $\hat{y}$, une prédiction) | | M02c |
| $\bar{x}$ | « x barre » | x bar | la moyenne de l'échantillon | | M02c |
| $\theta$ | « thêta » | theta | les paramètres d'un modèle | | M04 |
| $\mathcal{L}(\theta)$ | « L de thêta », « vraisemblance » | likelihood | à quel point les paramètres expliquent les données | | M04, M13a |
| $H(p)$, $D_{\mathrm{KL}}(p \parallel q)$ | « entropie de p », « divergence KL de p à q » | entropy, KL divergence | incertitude d'une loi ; écart entre deux lois | | M06 |

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
