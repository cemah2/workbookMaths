# Erreurs de calcul fréquentes

Les erreurs classiques, celles que tout le monde fait un jour. Chaque chapitre de la remise à niveau a ses exercices 🐛 pour apprendre à les repérer dans ton propre travail ; les chapitres suivants ajoutent leurs pièges ici.

## Écrire des maths en Python (R0)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre `^` pour la puissance | `x^2` | `x**2` (`^` est le « ou exclusif » sur les bits, sans message d'erreur) |
| Sous-entendre la multiplication | `2x`, `3(x + 1)` | `2*x`, `3*(x + 1)` |
| Oublier que `**` passe avant le signe moins | croire que `-3**2` vaut 9 | `-3**2` vaut -9 ; écrire `(-3)**2` pour 9 |
| Mal parenthéser une fraction | `1/2*x` pour $\frac{1}{2x}$ | `1/(2*x)` ; `1/2*x` vaut $\frac{x}{2}$ |
| Comparer deux flottants avec `==` | `0.1 + 0.2 == 0.3` (faux) | `math.isclose(0.1 + 0.2, 0.3)`, ou `Fraction` pour un calcul exact |
| Croire que `//` arrondit vers zéro | `-23 // 4` vaut -5 | `//` arrondit vers $-\infty$ : -6 (et `-23 % 4` vaut 1) |
| Appliquer `math` à un tableau NumPy | `math.exp(xs)` | `np.exp(xs)` |
| Oublier les accolades en LaTeX | `x^10`, `\frac{a+b}2` | `x^{10}`, `\frac{a+b}{2}` |

## Calcul et algèbre (R1, R2)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Le carré d'une somme n'est pas la somme des carrés | $(a+b)^2 = a^2 + b^2$ | $(a+b)^2 = a^2 + 2ab + b^2$ ; vérifie avec $a = b = 1$ : $4 \ne 2$ |
| La racine d'une somme n'est pas la somme des racines | $\sqrt{4 + 9} = 2 + 3$ | $\sqrt{13} \approx 3{,}6 \ne 5$ |
| Additionner des fractions « en haut et en bas » | $\frac{1}{2} + \frac{1}{3} = \frac{2}{5}$ | même dénominateur d'abord : $\frac{3}{6} + \frac{2}{6} = \frac{5}{6}$ |
| Simplifier un terme d'une somme | $\frac{x + 2}{2} = x + 1$ | on ne simplifie que des **facteurs** : $\frac{x+2}{2} = \frac{x}{2} + 1$ |
| Oublier les parenthèses autour d'un nombre négatif | $-3^2 = 9$ | $-3^2 = -9$, mais $(-3)^2 = 9$ (et en Python, `-3**2` vaut `-9`) |
| Diviser par une quantité qui peut être nulle | $x^2 = x \Rightarrow x = 1$ | $x^2 - x = 0 \Leftrightarrow x(x-1) = 0$ : $x = 0$ ou $x = 1$ |
| Garder le sens d'une inégalité en multipliant par un négatif | $-2x < 6 \Rightarrow x < -3$ | multiplier ou diviser par un négatif **retourne** l'inégalité : $x > -3$ |
| Pourcentages qui s'additionnent | +10 % puis +10 % = +20 % | les coefficients se multiplient : $1{,}1 \times 1{,}1 = 1{,}21$, soit +21 % |
| Ranger les négatifs comme les positifs | $-2 < -7$ | sur la droite, $-7$ est à gauche : $-7 < -2$ |
| Calculer × et ÷ de droite à gauche | $24 \div 4 \times 2 = 3$ | même priorité, de gauche à droite : $6 \times 2 = 12$ |
| Diviser par une fraction sans prendre l'inverse | $\frac{10}{3} \div \frac{5}{6} = \frac{50}{18}$ | multiplier par l'inverse : $\frac{10}{3} \times \frac{6}{5} = 4$ |
| Additionner les exposants d'une somme | $3^2 + 3^3 = 3^5$ | seul le **produit** additionne les exposants : $3^2 \times 3^3 = 3^5$ |
| Croire qu'un exposant négatif rend négatif | $3^{-2} = -9$ | $3^{-2} = \frac{1}{9}$ : « inverse », pas « opposé » |
| Oublier qu'une racine carrée est positive | $\sqrt{(-4)^2} = -4$ | $\sqrt{(-4)^2} = 4$ |
| Une mantisse hors de [1 ; 10[ | $45{,}2 \times 10^3$ | $4{,}52 \times 10^4$ |
| Arrondir un arrondi | 3,46 → 3,5 → 4 | arrondir une seule fois, depuis la valeur complète : 3 |
| Prendre `int` pour un plancher | `int(-1.6)` vaut $\lfloor -1{,}6 \rfloor$ | `int` coupe vers 0 ($-1$) ; $\lfloor -1{,}6 \rfloor = -2$ |
| Diviser par la valeur d'arrivée | de 250 à 210 : $\frac{-40}{210}$ | le taux d'évolution divise par la valeur de départ : $\frac{-40}{250} = -16\,\%$ |
| Prendre l'opposé du taux pour revenir au départ | après −20 %, +20 % | le coefficient réciproque est l'inverse : $\frac{1}{0{,}8} = 1{,}25$, soit +25 % |
| Faire la moyenne de deux moyennes | moyenne de 12 (10 élèves) et de 8 (30 élèves) = 10 | pondérer par les effectifs : $\frac{120 + 240}{40} = 9$ |
| Oublier des produits en développant | $(x + 3)(2x - 5) = 2x^2 - 15$ | chaque terme par chaque terme : quatre produits, $2x^2 + x - 15$ |
| Un moins devant une parenthèse qui ne change qu'un signe | $-(x - 4) = -x - 4$ | il change le signe de **chaque** terme : $-x + 4$ |
| Le carré d'un produit | $(2x)^2 = 2x^2$ | le carré porte sur tout le produit : $4x^2$ |
| Multiplier une fraction sans parenthèses | $\frac{x - 1}{2} \times 6 = 3x - 1$ | le 3 multiplie tout le numérateur : $3(x - 1) = 3x - 3$ |
| Conclure « $x = 0$ » quand les $x$ disparaissent | $2(x + 1) = 2x + 5$, « donc $x = 0$ » | regarder l'égalité qui reste : $2 = 5$ est faux, aucune solution ; $6 = 6$ serait vrai, tous les réels |
| Un crochet fermé du côté de l'infini | $[1 ; +\infty]$ | toujours ouvert : $[1 ; +\infty[$ |
| Confondre « et » et « ou » | « $x > 1$ et $x < 4$ » donne une réunion | « et » : intersection, $]1 ; 4[$ ; « ou » : réunion |
| Une seule solution à une équation avec valeur absolue | $\lvert x + 2 \rvert = 5 \Rightarrow x = 3$ | deux points à distance 5 de $-2$ : $-7$ et $3$ |
| Distribuer la valeur absolue sur une somme | $\lvert a + b \rvert = \lvert a \rvert + \lvert b \rvert$ | faux pour $a = 1$, $b = -1$ ; seulement $\lvert a + b \rvert \le \lvert a \rvert + \lvert b \rvert$ |
| Un système à déterminant nul « a une solution » | $D = 0$, « une solution » | aucune ou une infinité : comparer les seconds membres |
| Lire `[]` de `sympy.solve` comme « aucune solution » | `sp.solve(3*(x - 2) - (3*x - 6), x)` vaut `[]` | aussi pour une équation vraie pour tout $x$ ; `sp.solveset(..., x, sp.S.Reals)` distingue `EmptySet` et `Reals` |

## Logique, ensembles et sommes (R4)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Nier un « et » en gardant « et » | non ($a > 0$ et $b > 0$) = ($a \le 0$ et $b \le 0$) | De Morgan : ($a \le 0$ **ou** $b \le 0$) |
| Prendre la réciproque pour l'implication | « les rectangles ont quatre angles droits, donc une figure à quatre angles droits est un carré » | la réciproque est une autre phrase, à démontrer à part |
| Nier une implication par une implication | non (s'il fait beau, je sors) = (s'il ne fait pas beau, je ne sors pas) | « il fait beau et je ne sors pas » |
| Nier « pour tout » par « aucun » | non (tous les nombres sont pairs) = aucun n'est pair | il existe un nombre impair |
| Nier une inégalité stricte | non ($t > 5$) = $t < 5$ | $t \le 5$ |
| Confondre élément et sous-ensemble | $\{a\} \in \{a, b\}$ | $a \in \{a, b\}$ et $\{a\} \subset \{a, b\}$ |
| Oublier l'intersection dans un cardinal | $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert$ | retirer $\lvert A \cap B \rvert$, comptée deux fois |
| Compter les termes d'une somme | $\sum_{k=5}^{9}$ a 4 termes | $9 - 5 + 1 = 5$ termes |
| Séparer un produit dans une somme | $\sum a_k b_k = \left(\sum a_k\right)\left(\sum b_k\right)$ | faux en général ; seule une somme **double** $\sum_i \sum_j x_i y_j$ se factorise |
| Sortir une constante d'un produit | $\prod_{k=1}^{n} 3a_k = 3 \prod a_k$ | $3^n \prod a_k$ |
| Une borne de `range` | $\sum_{k=1}^{n}$ codée `range(1, n)` | `range(1, n + 1)` |
| Démontrer par des exemples | « vrai pour 1, 2, 3, donc pour tout $n$ » | un argument pour tous les $n$ (ou une récurrence) |
| Une récurrence sans initialisation | une hérédité juste suffit | vérifier aussi le premier cas |

## Suites (R5)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Confondre rang et valeur | $u_{n+1} = u_n + 1$ | $u_{n+1}$ est le terme suivant ; $u_n + 1$ est le terme augmenté de 1 |
| Oublier le premier rang | $a_n = a_1 + n\,r$ pour une suite qui commence à $a_1$ | $a_n = a_1 + (n - 1)\,r$ |
| Calculer une suite géométrique comme une arithmétique | $u_n = u_0 \times q \times n$ | $u_n = u_0\,q^n$ |
| Mettre le premier terme sous la puissance | $5 \times 3^n = 15^n$ | la puissance ne porte que sur la raison |
| Ne garder qu'une raison | $q^2 = 9$ donne $q = 3$ | $q = 3$ ou $q = -3$ |
| Compter les écarts au lieu des termes | $5 + 8 + \dots + 50$ a 15 termes | 15 écarts, donc 16 termes |
| Mettre le dernier rang en exposant | $\sum_{k=0}^{6} q^k = \frac{1 - q^6}{1 - q}$ | 7 termes : $\frac{1 - q^7}{1 - q}$ |
| Oublier le premier terme d'une somme | $\sum_{k=1}^{+\infty} q^k = \frac{1}{1 - q}$ | premier terme $q$ : $\frac{q}{1 - q}$ |
| Une somme infinie avec $\lvert q \rvert \ge 1$ | $1 + 3 + 9 + \dots = \frac{1}{1 - 3} = -\frac{1}{2}$ | pas de valeur finie : la formule exige $\lvert q \rvert < 1$ |
| Croire que des termes qui tendent vers 0 suffisent | $1 + \frac{1}{2} + \frac{1}{3} + \dots$ est finie | elle grandit sans fin |
| Prendre le point fixe pour la limite sans vérifier | $u_{n+1} = 2u_n - 3$ « tend vers 3 » | le point fixe n'est la limite que si la suite converge ($\lvert a \rvert < 1$) |
| Composer des pourcentages en les additionnant | trois hausses de 20 % = +60 % | $1{,}2^3 = 1{,}728$ : +72,8 % |
| Actualiser en multipliant | valeur actuelle de 5 000 € dans 3 ans : $5\,000 \times 1{,}02^3$ | diviser : $\frac{5\,000}{1{,}02^3}$ |
| Démarrer une moyenne exponentielle à la première valeur | $v_1 = x_1$ | $v_0 = 0$, donc $v_1 = (1 - \beta)\,x_1$ |
| Inverser le rôle de $\beta$ | $v_t = (1 - \beta)\,v_{t-1} + \beta\,x_t$ | $\beta$ multiplie l'ancienne moyenne |
| Une moyenne mobile de trop ou de moins | 4 moyennes sur une fenêtre de 3 et 5 valeurs | $N - k + 1 = 3$ moyennes |

## Fonctions, exponentielle, logarithme (R3, R6)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Confondre image et antécédent | « les antécédents de 2 » : calculer $f(2)$ | une image se calcule ; des antécédents se cherchent en résolvant $f(x) = 2$ |
| Oublier un antécédent | $x^2 = 4 \Rightarrow x = 2$ | deux antécédents : $-2$ et $2$ |
| Mélanger l'ordre des points | $m = \frac{y_2 - y_1}{x_1 - x_2}$ | même ordre en haut et en bas : $\frac{y_2 - y_1}{x_2 - x_1}$ |
| Un sens de variation sans intervalle | « $x^2$ est croissante » | croissante sur $[0 \;;\; +\infty[$ |
| L'image d'un intervalle par ses bornes | carré de $[-3 \;;\; 1]$ = $[1 \;;\; 9]$ | la courbe passe par 0 : $[0 \;;\; 9]$ |
| Le signe dans la forme canonique | $(x + 5)^2 - 2$ : sommet en $x = 5$ | $(x + 5)^2 = (x - (-5))^2$ : sommet en $x = -5$ |
| Diviser seulement la racine par $2a$ | $-b \pm \frac{\sqrt{\Delta}}{2a}$ | tout le numérateur : $\frac{-b \pm \sqrt{\Delta}}{2a}$ |
| Maximum et argmax | « le maximum est 3 » quand 3 est une valeur de $x$ | le maximum est une valeur de $f$ ; l'argmax, une valeur de $x$ |
| Un extremum hors de l'intervalle | le sommet de la parabole comme maximum sur $[0 \;;\; 1]$ alors qu'il est en $x = 4$ | regarder les variations sur l'intervalle, comparer les bornes |
| L'ordre d'une composée | $(f \circ g)(x)$ : $f$ puis $g$ | $g$ d'abord : $f(g(x))$ |
| Une réciproque sans restriction | « la réciproque du carré est la racine » sur $\mathbb{R}$ | seulement sur $[0 \;;\; +\infty[$, où chaque valeur a un seul antécédent |
| Le logarithme d'une somme | $\ln(a + b) = \ln a + \ln b$ | c'est pour un **produit** : $\ln(ab) = \ln a + \ln b$ |
| L'exponentielle d'une somme | $e^{a+b} = e^a + e^b$ | $e^{a+b} = e^a \times e^b$ |
| Confondre réciproque et inverse | $f^{-1}(x) = \frac{1}{f(x)}$ | $f^{-1}$ défait $f$ : $\ln$ est la réciproque de $\exp$, pas $\frac{1}{\exp}$ |
| Le logarithme d'un nombre négatif ou nul | $\ln(-1)$ | $\ln$ n'est défini que pour $x > 0$ |
| Multiplier les exposants d'un produit | $e^{2x} \times e^{3} = e^{6x}$ | on les additionne : $e^{2x + 3}$ |
| Additionner les exposants d'une puissance | $(e^{3})^{2} = e^{5}$ | on les multiplie : $e^{6}$ |
| Lire un exposant fractionnaire comme un produit | $27^{2/3} = 27 \times \frac{2}{3}$ | la racine cubique, puis le carré : 9 |
| Un exposant négatif rend négatif | $27^{-1/3} = -3$ | il donne l'inverse : $\frac{1}{3}$ |
| Le carré d'un logarithme | $(\ln a)^2 = 2 \ln a$ | c'est $\ln(a^2)$ qui vaut $2 \ln a$ |
| Le logarithme d'un quotient | $\ln \frac{a}{b} = \frac{\ln a}{\ln b}$ | $\ln a - \ln b$ |
| Une équation exponentielle sans solution | $e^x = -2 \iff x = \ln(-2)$ | pas de solution : $e^x > 0$ |
| Diviser par un logarithme négatif | $0{,}8^n < 0{,}1 \iff n < \frac{\ln 0{,}1}{\ln 0{,}8}$ | $\ln 0{,}8 < 0$ : le sens change, $n > \dots$ |
| Le changement de base à l'envers | $\log_5 30 = \frac{\ln 5}{\ln 30}$ | $\frac{\ln 30}{\ln 5}$ |
| Des bits aux nats | 4 bits $= \frac{4}{\ln 2}$ nats | on multiplie par $\ln 2$ : $4 \ln 2 \approx 2{,}77$ nats |
| `np.log` pris pour le logarithme décimal | `np.log(1000)` vaut 3 | `np.log` est $\ln$ ; le décimal est `np.log10` |
| Croire qu'une puissance bat une exponentielle | $x^5 > 1{,}1^x$ en $x = 100$, donc toujours | l'exponentielle finit par gagner (ici vers 299) |
| La symétrie de la sigmoïde | $\sigma(-x) = -\sigma(x)$ | $\sigma(-x) = 1 - \sigma(x)$ ; c'est tanh qui est impaire |
| Le logit | $\operatorname{logit}(p) = \ln p$ | $\ln \frac{p}{1 - p}$ |
| Un produit de probabilités en flottants | multiplier des milliers de probabilités | additionner leurs logarithmes : le produit devient 0 |

## Dérivées (R7)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier la dérivée de l'intérieur (composée) | $(e^{x^2})' = e^{x^2}$ | $(e^{x^2})' = 2x\,e^{x^2}$ : multiplier par la dérivée de ce qui est « dedans » |
| Dériver un produit facteur par facteur | $(uv)' = u'v'$ | $(uv)' = u'v + uv'$ |
| Dériver un quotient sans la formule | $\left(\frac{u}{v}\right)' = \frac{u'}{v'}$ | $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ |
| Inverser l'ordre au numérateur du quotient | $\left(\frac{u}{v}\right)' = \frac{uv' - u'v}{v^2}$ | $u'v$ en premier : le signe du résultat change sinon |
| Lever une forme indéterminée « à l'œil » | $\infty - \infty = 0$, $\frac{\infty}{\infty} = 1$ | mettre en facteur le terme qui domine, ou factoriser |
| Chercher l'asymptote verticale au numérateur | $\frac{3x - 2}{x + 1}$ : asymptote $x = \frac{2}{3}$ | là où le **dénominateur** s'annule (et pas le numérateur) |
| Oublier $f(a)$ dans la tangente | $y = f'(a)(x - a)$ | $y = f(a) + f'(a)(x - a)$ |
| Dériver $\sqrt{x}$ ou $\frac{1}{x}$ de travers | $(\sqrt{x})' = \frac{1}{\sqrt{x}}$, $\left(\frac{1}{x}\right)' = \ln x$ | $\frac{1}{2\sqrt{x}}$ et $-\frac{1}{x^2}$ |
| Confondre l'ordre de deux composées | $(e^x)^2$ et $e^{x^2}$ : même dérivée | $2e^{2x}$ et $2x\,e^{x^2}$ |
| Conclure à un extremum dès que $f' = 0$ | $(x^5)' = 0$ en 0, donc extremum | il faut que $f'$ change de signe |
| Oublier les bords d'un intervalle fermé | maximum sur $[a ; b]$ cherché seulement où $f' = 0$ | comparer aussi $f(a)$ et $f(b)$ |
| Donner l'abscisse au lieu de la valeur | « le maximum vaut 2 » quand il est atteint en $x = 2$ | le maximum est $f(2)$ ; l'abscisse est l'argmax |

## Géométrie, vecteurs et trigonométrie (R9)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Additionner les écarts pour une distance | $AB = (x_B - x_A) + (y_B - y_A)$, ou $\sqrt{a^2 + b^2} = a + b$ | $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$ |
| Inverser les coordonnées d'un vecteur | $\overrightarrow{AB} = A - B$ | arrivée moins départ : $B - A$ |
| Additionner deux vecteurs en Python avec `+` sur des tuples | `(3, -1) + (-2, 4)` donne `(3, -1, -2, 4)` | additionner coordonnée par coordonnée, ou passer par NumPy |
| Garder le signe dans une norme | $\lVert -2\vec{u} \rVert = -2\,\lVert \vec{u} \rVert$ | $\lvert -2 \rvert\,\lVert \vec{u} \rVert = 2\,\lVert \vec{u} \rVert$ |
| Croire que la norme d'une somme est la somme des normes | $\lVert \vec{u} + \vec{v} \rVert = \lVert \vec{u} \rVert + \lVert \vec{v} \rVert$ | seulement $\le$ (inégalité triangulaire), avec égalité si l'un est nul ou s'ils ont même direction et même sens |
| Prendre $(a ; b)$ pour un vecteur directeur de $ax + by + c = 0$ | $(2 ; -1)$ dirige $2x - y - 3 = 0$ | $(-b ; a) = (1 ; 2)$ la dirige ; $(a ; b)$ lui est normal |
| Croire qu'un produit scalaire est un vecteur | $(3 ; -1) \cdot (-2 ; 4) = (-6 ; -4)$ | c'est un nombre : $-6 - 4 = -10$ |
| Passer des degrés à `math.cos` | `math.cos(30)` pour $\cos 30°$ | `math.cos(math.radians(30))` : Python attend des radians |
| Convertir à l'envers | $30° = 30 \times \frac{180}{\pi}$ rad | $\times \frac{\pi}{180}$ : 180° doivent donner $\pi$ |
| Confondre les valeurs remarquables | $\cos\frac{\pi}{3} = \frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ ; c'est $\sin\frac{\pi}{3}$ qui vaut $\frac{\sqrt{3}}{2}$ |
| Oublier le signe d'un cosinus ou d'un sinus | $\sin\frac{7\pi}{6} = \frac{1}{2}$ | dessiner le point sur le cercle : sous l'axe horizontal, le sinus est négatif |
| Croire que $\arccos(\cos\theta) = \theta$ toujours | $\arccos\left(\cos\left(-\frac{\pi}{6}\right)\right) = -\frac{\pi}{6}$ | $\arccos$ rend un angle de $[0 ; \pi]$ : ici $\frac{\pi}{6}$ |
| Oublier de diviser par les normes pour un angle | $\cos\theta = \vec{u} \cdot \vec{v}$ | $\cos\theta = \frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert\,\lVert \vec{v} \rVert}$ |
| Tester l'orthogonalité de flottants avec `==` | `0.1 * 2.1 + 0.7 * (-0.3) == 0` vaut `False` | comparer à 0 avec une tolérance absolue : `math.isclose(x, 0, abs_tol=1e-9)` |

## Intégrales et densités (M02a)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Confondre intégrale et aire géométrique | $\int_0^{2\pi} \sin x\,dx = 0$, « donc l'aire est nulle » | les parties sous l'axe comptent négativement : découper là où $f$ change de signe, et additionner les valeurs absolues |
| Inverser les bornes du crochet | $\big[x^3\big]_0^2 = 0 - 8$ | $F(b) - F(a)$ : la borne du haut d'abord |
| Appliquer la formule des puissances à $x^{-1}$ | $\int \frac{dx}{x} = \frac{x^0}{0}$ | $\ln \lvert x \rvert$ |
| Oublier le facteur d'une primitive composée | une primitive de $e^{3x}$ est $e^{3x}$ | $\frac{e^{3x}}{3}$ : dériver la réponse pour vérifier |
| Intégrer un produit facteur par facteur | $\int x\,e^x\,dx = \frac{x^2}{2}e^x$ | par parties : $x\,e^x - e^x$ |
| Changer de variable sans changer les bornes | $\int_0^1 2x\,(x^2 + 1)^3\,dx = \int_0^1 u^3\,du$ | $u = x^2 + 1$ va de 1 à 2 : $\int_1^2 u^3\,du$ |
| Conclure qu'une intégrale converge parce que $f \to 0$ | $\int_1^{+\infty} \frac{dx}{x}$ converge | il faut décroître assez vite : $\frac{1}{x^p}$ converge vers $+\infty$ si et seulement si $p > 1$ |
| Ignorer une fonction qui explose dans l'intervalle | $\int_{-1}^1 \frac{dx}{x^2} = -2$ | $\frac{1}{x^2}$ n'est pas définie en 0 : l'intégrale diverge |
| Compter les extrémités entièrement dans les trapèzes | $h(f_0 + f_1 + \cdots + f_n)$ | les deux extrémités comptent pour moitié |
| Appliquer Simpson avec $n$ impair, ou des poids faux | poids $1, 2, 4, 2, 1$ | $n$ pair, poids $1, 4, 2, 4, \ldots, 4, 1$, le tout fois $\frac{h}{3}$ |
| Lire une densité comme une probabilité | $f(1) = 0{,}4$, « donc $P(X = 1) = 0{,}4$ » | $P(X = 1) = 0$ ; une probabilité est une aire sous $f$, et $f$ peut dépasser 1 |
| Oublier une condition de densité | « $x - 1$ sur $[0 ; 2]$ a une intégrale positive » | positive partout **et** d'aire totale 1 |
| Confondre $F(x)$ et $P(X > x)$ | $P(X > 2) = F(2)$ | $P(X > 2) = 1 - F(2)$ |
| Prendre un percentile pour une probabilité | « le percentile 90 vaut 0,9 » | c'est une valeur $x$ telle que $F(x) = 0{,}9$ |

## Matrices (M09a et suite)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Croire que le produit est commutatif | $\mathbf{AB} = \mathbf{BA}$ | en général $\mathbf{AB} \ne \mathbf{BA}$ : l'ordre compte |
| Transposer un produit sans inverser l'ordre | $(\mathbf{AB})^\top = \mathbf{A}^\top\mathbf{B}^\top$ | $(\mathbf{AB})^\top = \mathbf{B}^\top\mathbf{A}^\top$ |
| Multiplier des matrices de formes incompatibles | $(2 \times 3)$ fois $(2 \times 3)$ | le nombre de colonnes de la première doit égaler le nombre de lignes de la seconde |

## Probabilités (R8, M03)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Confondre $P(A \mid B)$ et $P(B \mid A)$ | « 99 % des malades ont un test positif, donc un test positif signifie 99 % de chances d'être malade » | c'est la formule de Bayes qui relie les deux ; la prévalence change tout (M03, M04) |
| Additionner des probabilités d'événements qui ne s'excluent pas | $P(A \cup B) = P(A) + P(B)$ | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Multiplier des probabilités d'événements dépendants | $P(A \cap B) = P(A)P(B)$ toujours | seulement si $A$ et $B$ sont indépendants |
| Choisir un univers dont les issues ne sont pas équiprobables | deux pièces : 0, 1 ou 2 piles, chacun $\frac{1}{3}$ | distinguer les deux pièces : PP, PF, FP, FF ; un seul pile a la probabilité $\frac{1}{2}$ |
| Additionner pour « au moins un » | au moins un 4 en deux lancers d'un dé à 4 faces : $\frac{1}{4} + \frac{1}{4}$ | passer par le contraire : $1 - \left(\frac{3}{4}\right)^2 = \frac{7}{16}$ |
| Compter un comité comme un podium | 3 personnes parmi 9 : $9 \times 8 \times 7$ | sans ordre : diviser par $3!$, $\binom{9}{3} = 84$ |
| Croire que $0! = 0$ | $\binom{n}{n} = \frac{n!}{n! \times 0!}$ impossible | $0! = 1$, le produit vide |
| Garder les mêmes probabilités sans remise | 2 morceaux préférés sur 6, deux tirages sans remise : $\left(\frac{2}{6}\right)^2$ | ce qui est tiré ne revient pas : $\frac{2}{6} \times \frac{1}{5}$ |
| Additionner le long d'un chemin d'arbre | $0{,}3 + 0{,}4$ pour « pluie et retard » | multiplier le long d'un chemin ($0{,}3 \times 0{,}4$), additionner entre les chemins |
| Confondre incompatibles et indépendants | « incompatibles, donc $P(A \cap B) = P(A)\,P(B)$ » | incompatibles : $P(A \cap B) = 0$, donc dépendants (si $P(A), P(B) > 0$) |
| Confondre $\mathbb{E}[X^2]$ et $\mathbb{E}[X]^2$ | $\mathbb{V}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]$ | $\mathbb{V}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2$, la moyenne des carrés moins le carré de la moyenne |
| Mal changer d'échelle une variance | $\mathbb{V}(10X - 4) = 10\,\mathbb{V}(X) - 4$ | $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$ |
| Croire que le hasard compense | après cinq piles, face est « dû » | les lancers sont indépendants ; la loi des grands nombres dilue les écarts |
