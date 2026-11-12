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

## Probabilités (R8)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
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
| Ignorer une fonction qui explose dans l'intervalle | $\int_{-1}^1 \frac{dx}{x^2} = -2$ | $\frac{1}{x^2}$ n'est pas bornée près de 0, et $\int_0^1 \frac{dx}{x^2}$ diverge ($p = 2 \ge 1$) : l'intégrale diverge |
| Compter les extrémités entièrement dans les trapèzes | $h(f_0 + f_1 + \cdots + f_n)$ | les deux extrémités comptent pour moitié |
| Appliquer Simpson avec $n$ impair, ou des poids faux | poids $1, 2, 4, 2, 1$ | $n$ pair, poids $1, 4, 2, 4, \ldots, 4, 1$, le tout fois $\frac{h}{3}$ |
| Lire une densité comme une probabilité | $f(1) = 0{,}4$, « donc $P(X = 1) = 0{,}4$ » | $P(X = 1) = 0$ ; une probabilité est une aire sous $f$, et $f$ peut dépasser 1 |
| Oublier une condition de densité | « $x - 1$ sur $[0 ; 2]$ a une intégrale positive » | positive partout **et** d'aire totale 1 |
| Confondre $F(x)$ et $P(X > x)$ | $P(X > 2) = F(2)$ | $P(X > 2) = 1 - F(2)$ |
| Prendre un percentile pour une probabilité | « le percentile 90 vaut 0,9 » | c'est une valeur $x$ telle que $F(x) = 0{,}9$ |

## Variables aléatoires et lois usuelles (M02b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Confondre une variable aléatoire et sa loi | « $X$ et $Y$ ont la même loi, donc $X = Y$ » | une loi décrit des chances : $X$ et $1 - X$ (pièce équilibrée) ont la même loi et ne sont jamais égales |
| Oublier le coefficient binomial | $P(X = 2) = 0{,}2^2 \times 0{,}8^4$ pour $\mathcal{B}(6 ; 0{,}2)$ | $\binom{6}{2}\,0{,}2^2\,0{,}8^4$ : il y a $\binom{6}{2}$ suites à deux succès |
| Se tromper sur $P(X > k)$ d'une loi géométrique | $P(X > 3) = 1 - (1 - p)^3$ | $P(X > 3) = (1 - p)^3$ : les trois premiers essais échouent |
| Lire le second paramètre de $\mathcal{N}$ comme un écart-type | $\mathcal{N}(5, 4)$ : $z = \frac{x - 5}{4}$ | c'est la variance : $\sigma = 2$, $z = \frac{x - 5}{2}$ ; et NumPy, SciPy attendent $\sigma$ |
| Se tromper de signe avec $\Phi$ | $\Phi(-1) = -0{,}8413$ | $\Phi(-1) = 1 - \Phi(1) = 0{,}1587$ |
| Donner une probabilité à une valeur exacte d'une variable à densité | $T \sim \mathcal{E}(2)$ : $P(T = 1) = 2e^{-2}$ | $P(T = 1) = 0$ ; $f(1)$ est une densité |
| Croire que $\mathbb{E}[g(X)] = g(\mathbb{E}[X])$ | $\mathbb{E}[X^2] = \mathbb{E}[X]^2$ | vrai pour $g$ affine seulement ; utiliser le théorème de transfert |
| Mal transformer une variance | $\mathbb{V}(3X + 5) = 3\,\mathbb{V}(X) + 5$ | $9\,\mathbb{V}(X)$ : le facteur au carré, le décalage disparaît |
| Additionner des écarts-types | $\sigma(X + Y) = 3 + 4 = 7$ pour des variables indépendantes | additionner les variances : $\sqrt{9 + 16} = 5$ |
| Soustraire les variances d'une différence | $\mathbb{V}(X - Y) = \mathbb{V}(X) - \mathbb{V}(Y)$ | $\mathbb{V}(X) + \mathbb{V}(Y)$ pour des variables indépendantes |
| Traiter $2X$ comme deux copies indépendantes | $\mathbb{V}(2X) = 2\,\mathbb{V}(X)$ | $\mathbb{V}(2X) = 4\,\mathbb{V}(X)$ ; c'est $\mathbb{V}(X_1 + X_2)$ qui vaut $2\,\mathbb{V}(X)$ |
| Conclure à l'indépendance sur une seule case | « $P(X = 0, Y = 0) = P(X = 0)P(Y = 0)$, donc indépendantes » | vérifier toutes les cases ; une seule case fausse prouve la dépendance |
| Oublier le facteur d'un changement de variable | $Y = 3X - 1$ : $f_Y(y) = f_X\big(\frac{y + 1}{3}\big)$ | multiplier par $\frac{1}{3}$ : l'aire de la densité doit rester 1 |
| Se tromper sur `loc` et `scale` de `scipy.stats` | `stats.expon(2)` pour $\lambda = 2$ ; `stats.uniform(2, 8)` pour $[2 ; 8]$ | `stats.expon(scale=1/2)` ; `stats.uniform(loc=2, scale=6)` |

## Échantillons et estimation (M02c)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Lire la médiane sur la série non triée | la médiane de $42, 38, 51, 45$ est $\frac{38 + 51}{2}$ | trier d'abord : $38, 42, 45, 51$, médiane $\frac{42 + 45}{2} = 43{,}5$ |
| Ne pas dire par quoi on divise une variance | « la variance vaut 41 » sans préciser | $s_n^2$ divise par $n$ (`ddof=0`), $s^2$ par $n - 1$ (`ddof=1`) : les deux sont des réponses différentes |
| Une seule convention de quantile | « le premier quartile de 8 valeurs est la médiane de la première moitié » | plusieurs conventions existent ; NumPy interpole à la position $p(n - 1)$ |
| Se fier au seul z-score pour une valeur aberrante | « $\lvert z \rvert = 2{,}8 < 3$, donc rien d'anormal » | la valeur gonfle $s$ (effet de masque) ; vérifier avec la règle de Tukey, qui repose sur les quartiles |
| Standardiser le test avec ses propres statistiques | `(x_test - x_test.mean()) / x_test.std()` | utiliser la moyenne et l'écart-type du jeu d'entraînement |
| Oublier la racine de $n$ | $\sigma(\bar{X}) = \frac{\sigma}{n}$ | $\frac{\sigma}{\sqrt{n}}$ : 4 fois plus de données divisent l'erreur par 2 |
| Croire que le hasard compense | « après dix piles, face est plus probable » | les tirages sont indépendants ; la loi des grands nombres dilue les écarts, elle ne les corrige pas |
| Appliquer le théorème central limite aux données | « avec 10 000 valeurs, les durées sont normales » | il porte sur la **moyenne** (ou la somme) ; les données gardent leur loi |
| Oublier le carré du biais | $\text{EQM} = \text{biais} + \text{variance}$ | $\text{EQM} = \text{biais}^2 + \text{variance}$ |
| Confondre écart-type et erreur type | un intervalle $\bar{x} \pm 1{,}96\,s$ « pour la moyenne » | l'intervalle de la moyenne utilise $\frac{s}{\sqrt{n}}$ ; $\bar{x} \pm 1{,}96\,s$ décrit à peu près les valeurs elles-mêmes |
| Garder 1,96 pour tous les niveaux | intervalle à 99 % : $\bar{x} \pm 1{,}96\,\text{SE}$ | 1,645 à 90 %, 1,96 à 95 %, 2,576 à 99 % |
| Mal interpréter un intervalle de confiance | « $\mu$ a 95 % de chances d'être dans $[39 ; 41]$ » | 95 % des intervalles construits ainsi contiennent $\mu$ ; celui-ci la contient ou non |
| Diviser la covariance par le produit des variances | $r = \frac{\operatorname{Cov}}{\mathbb{V}(X)\mathbb{V}(Y)}$ | $r = \frac{\operatorname{Cov}}{\sigma_X\sigma_Y}$, les écarts-types |
| Oublier la covariance dans une variance de somme | $\mathbb{V}(X + Y) = \mathbb{V}(X) + \mathbb{V}(Y)$ pour des variables corrélées | ajouter $2\operatorname{Cov}(X, Y)$ (et le retrancher pour une différence) |
| Conclure à une causalité | « corrélées à 0,6, donc l'une cause l'autre » | chercher une variable de confusion ; seule une expérience contrôlée établit une cause |
| Croire que plus de données corrigent un biais d'échantillonnage | « un million d'exemples, donc l'estimation est fiable » | $n$ réduit la variance, pas le biais : se demander qui manque dans les données |

## Probabilités conditionnelles et évaluation d'un classifieur (M03)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Confondre $P(A \mid B)$ et $P(B \mid A)$ | « 99 % des malades ont un test positif, donc un test positif signifie 99 % de chances d'être malade » | c'est la formule de Bayes qui relie les deux ; la prévalence change tout (M03, M04) |
| Diviser une conditionnelle par le total du tableau | $P(\text{premium} \mid \text{mobile}) = \frac{30}{500}$ | diviser par le total de l'événement « sachant » : $\frac{30}{300}$ |
| Conclure à l'indépendance sur une seule case | une case égale au produit de ses marges, donc « indépendantes » | vérifier toutes les cases, ou que toutes les lignes ont la même loi conditionnelle |
| Croire que l'indépendance deux à deux suffit | trois événements indépendants deux à deux, donc mutuellement | deux pièces et « même côté » : $P(A \cap B \cap C) = \frac{1}{4} \ne \frac{1}{8}$ |
| Moyenner des taux sans les poids des groupes | 2 %, 5 % et 8 % : « 5 % en moyenne » | probabilités totales : $\sum_k P(A \mid B_k)\,P(B_k)$ ; et attention au paradoxe de Simpson |
| Lire la matrice de scikit-learn à l'envers | TP en haut à gauche | labels triés : `[[TN, FP], [FN, TP]]`, la vérité en lignes |
| Échanger recall et precision | recall $= \frac{TP}{TP + FP}$ | recall : sachant la vérité, $\frac{TP}{TP + FN}$ ; precision : sachant la prédiction, $\frac{TP}{TP + FP}$ |
| Garder la precision du test pour une autre population | 0,92 en test (20 % de positifs), donc 0,92 en production (2 %) | recalculer $\frac{r\pi}{r\pi + (1 - s)(1 - \pi)}$ : 0,48 |
| Juger sur l'accuracy quand une classe est rare | « rien n'est positif » : 95 %, un bon modèle | regarder la balanced accuracy, le MCC, le recall et la precision |
| Utiliser $\beta$ au lieu de $\beta^2$ dans $F_\beta$ | $F_2 = \frac{3PR}{2P + R}$ | $F_2 = \frac{5PR}{4P + R}$ |
| Compter un ex æquo comme bien ou mal classé | AUC des paires avec un ex æquo compté 1 (ou 0) | un ex æquo compte $\frac{1}{2}$ |
| Croire que l'AUC mesure les probabilités | AUC 0,95, donc des probabilités fiables | l'AUC ne voit que l'ordre ; la calibration se juge au diagramme de fiabilité et au score de Brier |
| Calculer l'average precision par les trapèzes | relier les points (recall, precision) par des segments | des rectangles : $\sum_j (R_j - R_{j-1})\,P_j$ |

## Bayes, vraisemblance et loi Beta (M04)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre la vraisemblance pour l'a posteriori | « le capteur détecte 90 % des roulements usés, donc une alerte signifie 90 % de chances d'usure » | diviser vraisemblance × a priori par l'évidence ; un événement rare donne surtout de fausses alertes |
| Oublier une partie de l'évidence | $P(\text{alerte}) = 0{,}02 \times 0{,}9$ | additionner toutes les façons d'observer : $\sum_j P(O \mid H_j)\,P(H_j)$ |
| Repartir de l'a priori de départ à chaque observation | trois mises à jour, chacune avec l'a priori 0,5 | l'a posteriori d'une étape est l'a priori de la suivante |
| Croire que la vraisemblance est une densité en $\theta$ | « $\theta = \frac{1}{6}$ a la probabilité 0,0045 » | c'est la probabilité des données ; son intégrale en $\theta$ ne vaut pas 1 |
| Confondre $B(a, b)$ avec des factorielles de $a$ et $b$ | $B(3, 6) = \frac{3!\,6!}{9!}$ | $\Gamma(n) = (n - 1)!$ : $B(3, 6) = \frac{2!\,5!}{8!}$ |
| Confondre le mode et la moyenne d'une loi Beta | MAP de $\mathrm{Beta}(4, 18)$ : $\frac{4}{22}$ | mode $\frac{a - 1}{a + b - 2} = \frac{3}{20}$ ; moyenne $\frac{a}{a + b}$ |
| Appliquer la formule du mode hors de son domaine | mode de $\mathrm{Beta}(0{,}6 ;\ 3)$ : $\frac{-0{,}4}{1{,}6}$ | la formule vaut pour $a, b > 1$ ; sinon étudier la monotonie (mode 0 ou 1, ou pas de mode unique) |
| Mettre à jour une loi Beta à l'envers | 5 défauts sur 60 : $\mathrm{Beta}(a + 55,\ b + 5)$ pour le taux de défaut | dire d'abord ce que compte $a$ : ici les défauts ; $\mathrm{Beta}(a + 5,\ b + 55)$ |
| Ajouter $n$ à $b$ au lieu des échecs | $\mathrm{Beta}(a + k,\ b + n)$ | $\mathrm{Beta}(a + k,\ b + n - k)$ |
| Croire que deux succès futurs ont la probabilité « moyenne au carré » | $\big(\frac{a}{a + b}\big)^2$ | mettre à jour entre les deux : $\frac{a}{a + b}\cdot\frac{a + 1}{a + b + 1}$ |
| Annoncer un maximum de vraisemblance sur très peu de données | 0 achat sur 9 visites : « taux nul » | un a priori, par exemple Laplace : $\frac{1}{11}$ |
| Multiplier de nombreuses probabilités en flottants | $0{,}3^{700}$ donne 0 | additionner les logarithmes, normaliser par log-sum-exp |
| Prendre les exponentielles de log-probabilités sans soustraire le maximum | `np.exp([-1000, -1001])` donne `[0, 0]` | soustraire d'abord le maximum : `np.exp(l - l.max())` |
| Calculer $\Gamma$ ou $B$ directement pour de grands paramètres | `math.gamma(700)` : `OverflowError` | `math.lgamma`, `scipy.special.betaln`, et l'exponentielle à la fin |
| Écrire `k * math.log(p)` avec $p = 0$ | `ValueError` même pour $k = 0$ | traiter $p = 0$ et $p = 1$ à part : $0 \times \ln 0 = 0$ par convention |
| Lire un intervalle de crédibilité comme un intervalle de confiance (ou l'inverse) | « 95 % des études répétées contiendraient θ », pour un intervalle de crédibilité | crédibilité : une probabilité sur le paramètre, sachant les données ; confiance : une propriété de la méthode |

## Dérivées, Taylor et calcul numérique (M05a)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre tout point où $f'' = 0$ pour un point d'inflexion | « $(x^4)''(0) = 0$, donc 0 est un point d'inflexion » | vérifier que $f''$ change de signe : $12x^2$ ne change pas de signe, $x^4$ est convexe partout |
| Conclure « ni maximum ni minimum » quand $f''(c) = 0$ | $x^4$ en 0 | le test de la dérivée seconde ne conclut pas : étudier le signe de $f'$ autour de $c$ |
| Chercher les extrema globaux parmi les seuls points critiques | $x^2 e^{-x}$ sur $[-1, 4]$ : « maximum global $4e^{-2}$, en 2 » | comparer aussi les bords : $f(-1) = e$ est plus grand |
| Confondre convexe et croissante | « $e^{-x}$ décroît, donc elle n'est pas convexe » | la convexité dit que la pente augmente : $(e^{-x})'' = e^{-x} > 0$ |
| Oublier les factorielles, ou centrer en 0 au lieu de $a$ | $\cos x \approx 1 - x^2$ ; $P_2$ de $e^x$ en 1 avec des puissances de $x$ | $\frac{f^{(k)}(a)}{k!}(x - a)^k$ |
| Croire qu'une série de Taylor converge partout | $\ln 3 = 2 - \frac{4}{2} + \frac{8}{3} - \cdots$ | la série de $\ln(1 + x)$ ne converge que pour $-1 < x \le 1$ |
| Écrire le pas de Newton à l'envers | $x_{k+1} = x_k - \frac{f'(x_k)}{f(x_k)}$ | $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$, avec un test de $f'(x_k) \ne 0$ et un nombre maximal d'itérations |
| Croire que Newton converge toujours | $x^3 - 2x + 2$ depuis 0 | la suite cycle entre 0 et 1 : changer de point de départ, ou encadrer la racine d'abord |
| Diviser la différence centrée par $h$ | $\frac{f(x + h) - f(x - h)}{h}$ | les deux points sont à $2h$ l'un de l'autre : diviser par $2h$ |
| Prendre un pas $h$ minuscule « pour être précis » | $h = 10^{-15}$ dans une différence finie | l'arrondi grandit en $\frac{\delta}{h}$ : prendre le pas qui minimise la borne d'erreur |
| Prendre l'epsilon machine pour le plus petit flottant | « en `float64`, rien n'est plus petit que $2{,}2 \times 10^{-16}$ » | $\varepsilon$ est l'écart après 1 ; le plus petit `float64` positif est vers $5 \times 10^{-324}$ |
| Comparer des flottants calculés avec `==` | `0.1 + 0.2 == 0.3` donne `False` | une tolérance : `math.isclose(a, b, rel_tol=..., abs_tol=...)` |
| Soustraire deux nombres presque égaux | `(1e8 + 0.1) - 1e8` en `float32` ; $\sqrt{x + 1} - \sqrt{x}$ pour $x = 10^{12}$ | réécrire la formule : $\frac{1}{\sqrt{x + 1} + \sqrt{x}}$, `math.log1p`, `math.expm1` |
| Calculer $\ln(1 + x)$ par `math.log(1 + x)` pour $x$ minuscule | `math.log(1 + 1e-10)` n'a que 7 chiffres justes | `math.log1p(1e-10)` |
| Prendre l'exponentielle de grands scores | `math.exp(710)` : `OverflowError` ; `np.exp(710)` : `inf`, puis `nan` dans la softmax | soustraire le **maximum** des scores, puis le rajouter au log-sum-exp |
| Calculer le log-softmax par le logarithme de la softmax | une probabilité qui s'efface donne `math.log(0.0)` | $\ln\text{softmax}(\mathbf{v})_i = v_i - \text{LSE}(\mathbf{v})$, directement à partir des scores |

## Fonctions de plusieurs variables et gradient (M05b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier la variable « fixée » dans une dérivée partielle | $\frac{\partial}{\partial x}(x^3 y) = 3x^2$ | $y$ est une constante qui reste en facteur : $3x^2 y$ |
| Prendre une direction donnée par un vecteur non unitaire | la pente de $f$ dans la direction $(7, 24)$, avec $\nabla f = (6, 9)$ : « $42 + 216 = 258$ » | diviser d'abord par la norme : $\mathbf{u} = (0{,}28 ;\ 0{,}96)$, et la pente vaut $10{,}32$ |
| Croire que le gradient vise le sommet, ou suit les lignes de niveau | sur le dôme $100 - x^2 - 2y^2$, « en $(3, 1)$, le gradient pointe vers $(0, 0)$ » | il suit la montée la plus raide sur le moment, à angle droit des lignes de niveau : $(-6, -4)$ passe à côté de l'origine |
| Écrire le plan tangent sans les décalages | $z = f(a, b) + f_x(a, b)\,x + f_y(a, b)\,y$ | $z = f(a, b) + f_x(a, b)\,(x - a) + f_y(a, b)\,(y - b)$ : le plan passe par le point de contact |
| Prendre $f_{xy}$ pour le produit $f_x \times f_y$ | pour $x^3 y + 2y^2$ en $(1, 2)$ : « $f_{xy} = 6 \times 9$ » | $f_{xy}$ est la dérivée de $f_x$ par rapport à $y$ : $3x^2 = 3$ |
| Oublier le facteur 2 du terme croisé dans la courbure | dans la direction $\frac{(1, -1)}{\sqrt{2}}$ : « $\frac{12 - 3 + 4}{2}$ » | $f_{xx}u_1^2 + 2f_{xy}u_1u_2 + f_{yy}u_2^2 = \frac{12 - 6 + 4}{2} = 5$ |
| Conclure « minimum » parce que $f_{xx} > 0$ et $f_{yy} > 0$ | $f_{xx} = f_{yy} = 1$, $f_{xy} = 2$ | calculer $D = f_{xx}f_{yy} - f_{xy}^2 = 1 - 4 < 0$ : un point selle |
| Appliquer le test du second ordre quand $D = 0$ | « $x^4 + y^2$ n'a pas de minimum en $(0, 0)$, puisque $D = 0$ » | $D = 0$ : le test ne dit rien, regarder la fonction ($x^4 + y^2 \ge 0$ : c'est un minimum) |
| Oublier les bords pour un extremum global sur un domaine borné | le minimum de $f$ sur un segment cherché seulement là où $\nabla f = \mathbf{0}$ | paramétrer le segment, se ramener à une variable, comparer les points critiques **et** les extrémités |
| Se tromper de signe dans le pas de descente | $\mathbf{x} + \eta\,\nabla f(\mathbf{x})$ pour minimiser | descendre : $\mathbf{x} - \eta\,\nabla f(\mathbf{x})$ ; $+$ monte |
| Confondre $\min f$ et $\arg\min f$ | pour $(x - 3)^2 + 2(y + 1)^2$ : « $\arg\min f = 0$ » | $\min f = 0$ (une valeur), $\arg\min f = (3, -1)$ (un point) |

## Théorie de l'information (M06)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Calculer en nats en croyant calculer en bits | « $-\ln \frac{1}{8} \approx 2{,}08$ bits » | bits : $\log_2$, soit $-\log_2 \frac{1}{8} = 3$ bits ; nats : $\ln$ ; scikit-learn et PyTorch calculent en nats |
| Laisser $0 \log 0$ donner `nan` | `-np.sum(p * np.log2(p))` avec une probabilité nulle : `nan` | $0 \log 0 = 0$ : ne garder que les $p > 0$, ou utiliser `scipy.special.xlogy` |
| Prendre l'entropie d'une ligne sans la diviser par sa probabilité | pour la ligne $(0{,}12 ;\ 0{,}28)$, l'entropie « de 0,12 et 0,28 » | la loi conditionnelle est la ligne divisée par $p(x) = 0{,}4$ : $(0{,}3 ;\ 0{,}7)$ |
| Faire la moyenne simple des entropies des lignes | $H(Y \mid X) = \frac{H_1 + H_2}{2}$ alors que $p(x_1) = 0{,}8$ | pondérer par les probabilités des lignes : $0{,}8\,H_1 + 0{,}2\,H_2$ |
| Croire que chaque valeur de $X$ diminue l'incertitude sur $Y$ | « $H(Y \mid X = x) \le H(Y)$ pour tout $x$ » | c'est vrai seulement en moyenne, $H(Y \mid X) \le H(Y)$ ; une valeur particulière peut l'augmenter |
| Prendre $H(X) + H(Y)$ pour $H(X, Y)$ | sans vérifier que $X$ et $Y$ sont indépendantes | $H(X, Y) = H(X) + H(Y) - I(X ; Y)$ : l'égalité n'a lieu que pour des variables indépendantes |
| Conclure à l'indépendance d'une corrélation nulle | $X$ uniforme sur $\{-1, 0, 1\}$ et $Y = X^2$ : « corrélation nulle, donc $I(X ; Y) = 0$ » | la corrélation ne voit que les liens linéaires ; ici $I(X ; Y) = H(Y) > 0$ |
| Échanger les deux lois de la divergence KL | $D_{\mathrm{KL}}(\text{modèle} \parallel \text{données})$ au lieu de $D_{\mathrm{KL}}(\text{données} \parallel \text{modèle})$ | l'ordre compte : les poids sont ceux des données ; l'autre sens peut même être infini |
| Appeler la divergence KL une distance | « la distance KL entre $p$ et $q$ » | une divergence : pas symétrique, pas d'inégalité triangulaire ; Jensen-Shannon, elle, est symétrique |
| Écrire l'inégalité de Jensen dans le mauvais sens | « $\mathbb{E}[\ln X] \ge \ln \mathbb{E}[X]$ » | $\ln$ est concave : $\mathbb{E}[\ln X] \le \ln \mathbb{E}[X]$ ; le sens « $\ge$ » est celui des fonctions convexes |
| Croire qu'une somme de Kraft au plus 1 rend un code préfixe | « $\{0, 01, 11\}$ : $\frac{1}{2} + \frac{1}{4} + \frac{1}{4} = 1$, donc préfixe » | Kraft dit qu'**il existe** un code préfixe de ces longueurs (0, 10, 11), pas que celui-ci l'est : 0 est le début de 01 |
| Arrondir les longueurs de Shannon à l'entier le plus proche | $-\log_2 0{,}4 \approx 1{,}32$, « donc 1 » | à l'entier supérieur, $\lceil 1{,}32 \rceil = 2$ : sinon la somme de Kraft peut dépasser 1 |
| Croire sans biais l'entropie des fréquences observées | l'entropie des fréquences de 10 tirages prise pour la vraie entropie | elle la sous-estime en moyenne (et l'information mutuelle estimée la surestime) : plus de données, ou une correction |

## Vecteurs et géométrie de ℝⁿ (M07)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier la racine d'une distance euclidienne | `np.sum((a - b) ** 2)` pris pour $\lVert \mathbf{a} - \mathbf{b} \rVert$ | c'est son **carré** : `np.sqrt(np.sum((a - b) ** 2))` ; le carré suffit pour comparer des distances, pas pour les additionner |
| Diviser par une seule norme dans un cosinus | `(u @ v) / np.sqrt(u @ u)` | diviser par les **deux** normes : $\frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert}$ |
| Projeter avec $\lVert \mathbf{u} \rVert$ au lieu de $\lVert \mathbf{u} \rVert^2$ | $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert}\,\mathbf{u}$ avec $\mathbf{u}$ non unitaire | $\frac{\mathbf{x} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}$ ; $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert}$ est la **composante** (une longueur), $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert^2}$ le **coefficient** |
| Croire qu'un cosinus de 1 veut dire des vecteurs égaux | $\mathbf{u}$ et $2\mathbf{u}$ « identiques » car de cosinus 1 | même direction, longueurs différentes : à la distance $\lVert \mathbf{u} \rVert$ |
| Prendre le score pour la distance à l'hyperplan | la distance de $\mathbf{x}$ à $\mathbf{w} \cdot \mathbf{x} + b = 0$ vaut « $\lvert \mathbf{w} \cdot \mathbf{x} + b \rvert$ » | diviser par $\lVert \mathbf{w} \rVert$ ; sinon multiplier $\mathbf{w}$ et $b$ par 10 changerait la distance |
| Croire que $(-\mathbf{w}, -b)$ garde le même côté positif | « même hyperplan, donc mêmes côtés » | même hyperplan, mais les côtés sont échangés |
| Additionner des distances au lieu de leurs carrés pour l'inertie | $\sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert$ | l'inertie est $\sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2$ ; c'est elle que minimise le barycentre |
| Oublier le facteur $m$ dans König-Huygens | $\sum \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2 + \lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$ | $+\,m\,\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$ (ou $\Omega$ avec des poids) : chaque point compte |
| Compter le point lui-même dans $a(i)$ | $a(i)$ divisé par la taille du cluster, avec une distance nulle | la moyenne sur les **autres** points du cluster |
| Comparer des distances avec des features d'unités différentes | puissance en chevaux et masse en tonnes dans la même distance | standardiser chaque feature (avec les statistiques du jeu d'entraînement) avant de calculer des distances |
| Coder des catégories par des entiers | vélo 1, bus 2, métro 3, marche 4 | un vecteur one-hot : sinon on invente un ordre et des distances entre catégories |
| Oublier `axis` ou `keepdims` | `X / np.sqrt(np.sum(X ** 2, axis=1))` | `keepdims=True` (forme `(n, 1)`) pour diviser chaque **ligne** ; sans lui, NumPy divise les colonnes quand `X` est carré |
| Croire que l'intuition de la dimension 2 vaut en dimension 1 000 | « deux vecteurs au hasard font un angle quelconque » | en grande dimension, ils sont presque orthogonaux, et toutes les distances se ressemblent |

## Tests statistiques (M08)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Lire la p-valeur comme la probabilité que $H_0$ soit vraie | « $p = 0{,}03$ : 3 % de chances que le changement soit inutile » | elle se calcule **en supposant** $H_0$ vraie : la probabilité d'un écart au moins aussi grand, si rien ne changeait |
| Conclure à l'absence d'effet après un test non significatif | « $p = 0{,}4$, donc la mise à jour ne change rien » | « pas d'effet détecté » ; regarder la puissance et l'intervalle de confiance, qui peut contenir de grands effets |
| Confondre significatif et important | « $p = 10^{-6}$, donc un gain énorme » | une p-valeur mélange la taille de l'effet et la quantité de données : donner l'effet et son intervalle |
| Choisir le sens du test après avoir vu les données | un test unilatéral dans le sens observé, sans l'avoir prévu | fixer $H_1$ avant ; sinon le risque de type I réel est le double du seuil annoncé |
| Doubler une p-valeur binomiale unilatérale pour une loi dissymétrique | $2P(K \ge 5)$ pour $p_0 = 0{,}1$ | additionner les issues au plus aussi probables que l'observation, des deux côtés |
| Annoncer une p-valeur nulle après un test par permutation | « aucune des 999 permutations n'atteint l'écart : $p = 0$ » | $\frac{C + 1}{B + 1}$ : la répartition observée compte ; $p \ge \frac{1}{B + 1}$ |
| Rebattre des mesures appariées comme deux groupes | mélanger les serveurs « avant » et « après » | échanger les deux mesures **dans** chaque paire (changer le signe des différences) |
| Traiter des mesures appariées comme indépendantes | l'erreur type $\sqrt{s_a^2/n + s_b^2/n}$ pour des mesures avant et après | travailler sur les différences : $\frac{s_d}{\sqrt{n}}$, bien plus petite |
| Prendre 1,96 avec peu de mesures | $\bar{d} \pm 1{,}96\,\frac{s_d}{\sqrt{5}}$ | le quantile de Student à $n - 1$ degrés de liberté (2,776 pour 5 mesures) |
| Utiliser l'intervalle de Wald avec peu de succès | $[0, 0]$ après 0 succès sur 10, ou une borne négative | l'intervalle de Wilson, toujours dans $[0, 1]$ |
| Diviser les p-valeurs par $m$ au lieu de les multiplier | p-valeur ajustée $\frac{p}{m}$ | $\min(1, m\,p)$ ; ou garder $p$ et comparer au seuil $\frac{\alpha}{m}$ |
| Prendre pour $m$ le nombre de résultats montrés | Bonferroni avec les 3 plus petites p-valeurs sur 50 tests faits | $m$ = le nombre de tests **faits** |
| Arrondir au-dessous une taille d'échantillon | $n = 68{,}7$ arrondi à 68 | arrondir au-dessus : avec moins de mesures, la puissance n'est pas atteinte |
| Préférer le plus grand AIC, ou prendre $\log_{10}$ dans le BIC | « AIC = 464,8 contre 461,8 : le premier gagne » | le plus **petit** critère gagne ; $\ln$ népérien |
| Ne publier que le test le plus significatif | 25 indicateurs testés, seul celui de p-valeur 0,02 est publié | compter les 25 tests (Bonferroni), ou confirmer sur de nouvelles données |

## Matrices (M09a et suite)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Croire que le produit est commutatif | $\mathbf{AB} = \mathbf{BA}$ | en général $\mathbf{AB} \ne \mathbf{BA}$ : l'ordre compte |
| Transposer un produit sans inverser l'ordre | $(\mathbf{AB})^\top = \mathbf{A}^\top\mathbf{B}^\top$ | $(\mathbf{AB})^\top = \mathbf{B}^\top\mathbf{A}^\top$ |
| Multiplier des matrices de formes incompatibles | $(2 \times 3)$ fois $(2 \times 3)$ | le nombre de colonnes de la première doit égaler le nombre de lignes de la seconde |
| Lire $a_{ij}$ colonne d'abord | $a_{32}$ lu à la ligne 2, colonne 3 | la ligne d'abord, puis la colonne ; en Python, `A[i - 1, j - 1]` |
| Écrire `*` pour un produit matriciel | `X * W` pour une couche dense | `X @ W` ; `*` multiplie élément par élément, et le broadcasting peut cacher l'erreur |
| Ajouter le biais d'une couche à une seule ligne, ou dans le mauvais sens | $b_1$ ajouté à l'exemple 1 et $b_2$ à l'exemple 2 | $b_j$ s'ajoute à la colonne $j$ (le neurone $j$), sur chaque ligne |
| Calculer $\mathbf{X}\mathbf{X}^\top$ au lieu de $\mathbf{X}^\top\mathbf{X}$ | `X @ X.T` pour la matrice des features | `X.T @ X`, de forme $(p, p)$ ; `X @ X.T` est $(n, n)$, une case par paire d'exemples |
| Choisir les parenthèses au hasard dans un produit de trois matrices | $\mathbf{A}(\mathbf{B}\mathbf{C})$ avec $\mathbf{B}\mathbf{C}$ énorme | compter $n\,p\,m$ pour chaque ordre ; devant un vecteur, multiplier de droite à gauche |
| Simplifier $\mathbf{A}\mathbf{B} = \mathbf{A}\mathbf{C}$ en $\mathbf{B} = \mathbf{C}$ | $\mathbf{A}$ singulière, $\mathbf{B} \ne \mathbf{C}$ | on ne simplifie que par une matrice inversible : multiplier à gauche par $\mathbf{A}^{-1}$ |
| Inverser un produit ou une somme terme à terme | $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{A}^{-1}\mathbf{B}^{-1}$, $(\mathbf{A} + \mathbf{B})^{-1} = \mathbf{A}^{-1} + \mathbf{B}^{-1}$ | $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$ ; pas de règle pour une somme |
| Oublier le second membre dans une opération sur les lignes | $L_2 - 2L_1$ appliqué aux seuls coefficients | travailler sur la matrice augmentée : chaque opération porte sur toute la ligne |
| Faire deux opérations en même temps, ou multiplier une ligne par 0 | $L_1 \leftarrow L_1 - L_2$ et $L_2 \leftarrow L_2 - L_1$ d'un coup | une opération à la fois, avec une **autre** ligne, et un facteur non nul |
| S'arrêter à la forme échelonnée quand on veut la réduite | un nombre non nul au-dessus d'un pivot | annuler aussi au-dessus de chaque pivot, et diviser chaque ligne par son pivot |
| Garder un pivot minuscule | éliminer avec $\varepsilon = 10^{-18}$ comme pivot | le pivot partiel : la plus grande valeur absolue de la colonne |
| Lire une ligne nulle comme « pas de solution » | $(0 \;\; 0 \;\; 0 \mid 0)$ : « impossible » | $0 = 0$ est toujours vrai : une équation de moins ; seule $(0 \cdots 0 \mid c)$ avec $c \ne 0$ est impossible |
| Compter les lignes non nulles pour le rang avant l'élimination | rang 3 pour trois lignes dont l'une est la somme des deux autres | échelonner d'abord, puis compter les pivots |
| Résoudre un système par l'inverse | `np.linalg.inv(A) @ b` | `np.linalg.solve(A, b)` : moins de calculs et moins d'arrondis |

## Moindres carrés et régularisation (M09b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Calculer un $R^2$ sans centrer | $1 - \frac{\sum r_i^2}{\sum y_i^2}$ | $1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$, avec $\mathrm{SCT} = \sum (y_i - \bar{y})^2$ |
| Comparer une MSE à une MAE | « MSE 25, MAE 4 : la MAE est meilleure » | la MSE est dans l'unité au carré : comparer la RMSE (5) et la MAE |
| Croire que $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$ pour toute droite | la décomposition appliquée à une droite tracée à la main | elle ne vaut que pour les moindres carrés avec une colonne de 1 |
| Prendre $2\mathbf{A}\mathbf{w}$ pour le gradient de $\mathbf{w}^\top\mathbf{A}\mathbf{w}$ | $\mathbf{A}$ non symétrique | $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ |
| Oublier le signe moins du gradient des moindres carrés | $\nabla\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 = 2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ | $-2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ : un pas de descente ajoute $2\eta\mathbf{X}^\top\mathbf{r}$ |
| Inverser $\mathbf{X}^\top\mathbf{X}$ pour résoudre | `np.linalg.inv(X.T @ X) @ X.T @ y` | `np.linalg.solve(X.T @ X, X.T @ y)`, ou `np.linalg.lstsq(X, y)` |
| Oublier la colonne de 1 | une droite forcée à passer par l'origine | ajouter une colonne de 1 (ou centrer $\mathbf{X}$ et $\mathbf{y}$) |
| Croire qu'un modèle polynomial n'est pas linéaire | « $w_0 + w_1x + w_2x^2$ ne se résout pas par les équations normales » | il est linéaire en $\mathbf{w}$ : les colonnes $1, x, x^2$, mêmes équations |
| Combiner des puissances non standardisées | $x$ entre 0 et 20, colonnes $x, \ldots, x^6$ | ramener $x$ à $[-1, 1]$, ou standardiser : sinon $\mathbf{X}^\top\mathbf{X}$ est presque singulière |
| Appliquer ridge sans standardiser | une distance en mètres à côté d'une feature sans unité | standardiser les colonnes : la pénalité dépend de l'unité |
| Pénaliser l'ordonnée à l'origine sans le vouloir | ridge sur $\mathbf{X}$ avec sa colonne de 1 | centrer, résoudre sans colonne de 1, puis $b = \bar{y} - \bar{\mathbf{x}} \cdot \mathbf{w}$ |
| Écrire $\lambda = \frac{\sigma}{\tau}$ ou $\frac{\tau^2}{\sigma^2}$ | un prior large qui renforce la pénalité | $\lambda = \frac{\sigma^2}{\tau^2}$ : des variances, bruit au numérateur |
| Prendre $\frac{\mathrm{SCR}}{n}$ pour un estimateur sans biais de $\sigma^2$ | « $\hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$ est sans biais » | il sous-estime ; $\frac{\mathrm{SCR}}{n - p}$ est sans biais |
| Juger un modèle à son $R^2$ d'entraînement | ajouter des features de bruit, et voir le $R^2$ monter | le $R^2$ d'entraînement ne baisse jamais : mesurer sur des données de validation |
| Oublier le signe dans le seuillage doux | $S(-1{,}4 ;\ 0{,}3) = -1{,}7$ | rapprocher de 0 : $\operatorname{signe}(z)\max(\lvert z \rvert - \gamma, 0) = -1{,}1$ |

## Séparabilité linéaire et convexité (M10)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Croire qu'une réunion de convexes est convexe | « deux disques convexes, donc leur réunion aussi » | seule l'intersection garde la convexité : un segment entre les deux disques sort de la réunion |
| Prendre la courbe d'une fonction convexe pour un ensemble convexe | « la parabole $y = x^2$ est convexe » | c'est la région au-dessus d'elle (l'épigraphe) qui est un ensemble convexe |
| Garder un point au milieu d'un côté comme sommet | chaîne monotone avec le test $< 0$ | retirer le dernier sommet quand le produit vectoriel est $\le 0$ |
| Inverser le produit vectoriel | $u_2v_1 - u_1v_2$ | $u_1v_2 - u_2v_1$ : positif quand on tourne à gauche ; sinon l'enveloppe sort dans le sens des aiguilles d'une montre |
| Conclure « non séparable » sur des droites dessinées | « aucune des dix droites tracées ne marche » | il en reste une infinité : écrire un témoin, un point dont on montre (poids positifs, de somme 1) qu'il est dans les deux enveloppes, ou lancer le programme linéaire |
| Tester la séparabilité avec $\ge 0$ | le programme linéaire $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 0$ | exiger $\ge 1$ : avec $\ge 0$, $\mathbf{w} = \mathbf{0}$ et $b = 0$ conviennent toujours |
| Laisser les bornes par défaut de `linprog` | des inconnues forcées à être positives | `bounds=(None, None)` : les poids et le biais sont libres |
| Chercher un séparateur sans terme constant | $\mathbf{w} \cdot \mathbf{x} > 0$ sur une classe, $< 0$ sur l'autre | seuls les hyperplans par l'origine sont alors essayés : ajouter la coordonnée constante 1, en tête (astuce du biais) |
| Prendre la marge fonctionnelle pour une distance | marge $\min_i y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ | diviser par $\lVert \mathbf{w} \rVert$ ; doubler $(\mathbf{w}, b)$ ne doit rien changer |
| Une marge en valeur absolue | $\min_i \frac{\lvert \mathbf{w} \cdot \mathbf{x}_i + b \rvert}{\lVert \mathbf{w} \rVert}$ | multiplier par le label $y_i$ : la marge est négative quand un point est du mauvais côté |
| Confondre la borne triangulaire et la borne pas à pas | $\lVert \mathbf{v}_k \rVert \le \sqrt{\lVert \mathbf{v}_0 \rVert^2 + kL^2}$ pour des pas quelconques | sans condition, seulement $\lVert \mathbf{v}_0 \rVert + kL$ ; la borne en $\sqrt{k}$ demande $\mathbf{v}_k \cdot \mathbf{d}_k \le 0$ à chaque pas |
| Croire qu'une activation change la frontière | « avec une sigmoïde, la frontière se courbe » | une activation croissante garde l'hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ |

## Logique, induction et inégalités de concentration (M11)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Juger un argument sur la vérité de sa conclusion | « si $f$ est continue en 0, elle est dérivable en 0 ; $\lvert x \rvert$ est continue en 0 ; donc $\lvert x \rvert$ est dérivable en 0 » déclaré non valide | il est valide (*modus ponens*) mais pas solide : c'est la première prémisse qui est fausse ($\lvert x \rvert$ fait un coin en 0) |
| Affirmer le conséquent | « si la batterie est vide, l'ordinateur ne démarre pas ; il ne démarre pas ; donc la batterie est vide » | non valide : la ligne « $P$ faux, $Q$ vrai » (une autre cause) le réfute |
| Prouver une phrase en « pour tout » par des exemples | « $n^2 + n + 41$ est premier pour $n = 0$ à 39, donc pour tout $n$ » | $n = 40$ donne $41^2$ : il faut un raisonnement pour tout $n$, et un contre-exemple suffit à réfuter |
| Enchaîner deux phrases en « au moins un » | « $4 \in A \cap B$ et $10 \in B \cap C$, donc $A \cap C \ne \varnothing$ » | les témoins peuvent différer ; seules les inclusions se transmettent ($A \subset B \subset C$) |
| Lire $P(\text{signal} \mid \text{cas})$ comme $P(\text{cas} \mid \text{signal})$ | « le détecteur repère 95 % des plagiats, donc une copie signalée est plagiée à 95 % » | Bayes, avec le taux de base (2 %) : environ 0,39 |
| Croire qu'un grand échantillon efface un biais de sélection | 10 000 notes d'examen saisies par les inscrits eux-mêmes, ceux qui ont 8 les saisissant quatre fois plus que ceux qui ont 4 | la moyenne des notes saisies tend vers 7,2 au lieu de 6 : changer la façon de recueillir les notes (un tirage au hasard des inscrits, des relances) |
| Conclure « probabilité nulle » après zéro événement | « aucune panne en 150 essais, donc le taux de panne est nul » | règle de trois : seulement $p < 2\,\%$ environ, à 95 % |
| Appliquer Markov à une variable qui peut être négative | $X = \pm 10$ avec $\mathbb{E}[X] = 0$ : « $P(X \ge 5) \le 0$ » | se ramener à une variable positive : $\lvert X \rvert$, $(X - \mu)^2$ ou $X - m$ si $X \ge m$ |
| Tchebychev avec $t$ au lieu de $t^2$ | « $P(\lvert N - 40 \rvert \ge 160) \le \frac{100}{160}$ » | $\frac{\sigma^2}{t^2} = \frac{100}{160^2} \approx 0{,}0039$ ; contrôle : diviser $t$ par 2 multiplie $n$ par 4 |
| Appliquer Hoeffding sans bornes connues, ou sans indépendance | un revenu par client sans plafond, des mesures successives d'une série temporelle | vérifier un intervalle $[a, b]$ fixé à l'avance et des tirages indépendants ; sinon, Tchebychev (avec une variance) ou rien |
| Un rayon sans racine carrée, ou sans le facteur 2 du bilatéral | $n = 500$, $\delta = 0{,}05$ : « $r = \frac{\ln 40}{1\,000} \approx 0{,}0037$ » | $r = \sqrt{\frac{\ln 40}{1\,000}} \approx 0{,}061$ ; pour un seul côté, $\ln(1/\delta)$ |
| Le rayon du meilleur de $K$ modèles calculé comme pour un seul | le meilleur de 20 modèles évalués sur le même jeu de test, rayon au risque 5 % | chaque rayon au risque $\frac{\delta}{K}$ (borne de l'union) |
| Croire qu'une partie chanceuse a un regret négatif | « on a gagné plus que la meilleure moyenne fois $T$, donc $R_T < 0$ » | $R_T = \sum_k \Delta_k\,\mathbb{E}[N_k(T)] \ge 0$ : une espérance qui compare des moyennes, pas les récompenses tirées |
| Croire qu'un ε fixé finit par ne plus coûter | « ε-greedy trouve la meilleure option, donc son regret se stabilise » | chaque option reste choisie avec la probabilité $\frac{\varepsilon}{K}$ : regret au moins linéaire ; faire décroître $\varepsilon$ |

## Espaces vectoriels et applications linéaires (M12a)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre pour un sous-espace un ensemble qui ne contient pas $\mathbf{0}$ | « le plan $x + y - z = 2$ est un sous-espace de $\mathbb{R}^3$ » | tester d'abord $\mathbf{0}$ : c'est un sous-espace **affine**, un sous-espace déplacé |
| Vérifier seulement la stabilité par addition | « le demi-plan $x \ge 0$ est stable par somme, donc c'est un sous-espace » | tester aussi la multiplication, par $-1$ en particulier |
| Conclure « libre » parce qu'aucun vecteur n'est multiple d'un autre | $(1, 2, 0)$, $(0, 1, 3)$, $(1, 3, 3)$ « deux à deux non colinéaires, donc libres » | calculer le rang : le troisième est la somme des deux premiers |
| Ranger une base en lignes pour calculer des coordonnées | résoudre $\mathbf{B}^\top\mathbf{c} = \mathbf{v}$ | les vecteurs de base dans les **colonnes** : $\mathbf{B}\mathbf{c} = \mathbf{v}$, puis vérifier $c_1\mathbf{b}_1 + \cdots = \mathbf{v}$ |
| Oublier le terme constant dans une dimension | « les polynômes de degré au plus 3 forment un espace de dimension 3 » | $1, x, x^2, x^3$ : dimension 4 |
| Prendre la borne du rang d'un produit pour sa valeur | « $\operatorname{rg}(\mathbf{A}) = 2$, $\operatorname{rg}(\mathbf{B}) = 3$, donc $\operatorname{rg}(\mathbf{A}\mathbf{B}) = 2$ » | ce n'est qu'un maximum : le produit perd les directions de $\operatorname{Im}\mathbf{B}$ qui tombent dans $\ker\mathbf{A}$ |
| Ranger $f(\mathbf{e}_j)$ dans la ligne $j$ | la matrice de $(x, y) \mapsto (x + y, x - y, 2x)$ écrite de forme $(2, 3)$ | $f(\mathbf{e}_j)$ est la **colonne** $j$ ; la forme est (arrivée, départ) |
| Écrire la matrice de « $f$, puis $g$ » dans l'ordre de lecture | $\mathbf{A}\mathbf{B}$ pour « appliquer $\mathbf{A}$, puis $\mathbf{B}$ » | $\mathbf{B}\mathbf{A}$ : la dernière appliquée est à gauche, la plus proche de $\mathbf{x}$ à droite |
| Chercher le noyau dans l'espace d'arrivée | pour $\mathbf{A}$ de forme $(2, 4)$, un vecteur du noyau à 2 coordonnées | le noyau vit au départ : 4 coordonnées ; l'image, à l'arrivée |
| Prendre la base de l'image dans la forme réduite | $(1, 0, 0)$ et $(0, 1, 0)$ comme base de l'image | les colonnes **de $\mathbf{A}$** dont l'indice porte un pivot |
| Oublier le signe moins dans un vecteur du noyau | $x_p = R_{ij}$ | $x_p = -R_{ij}$ ; vérifier toujours $\mathbf{A}\mathbf{x} = \mathbf{0}$ |
| Conclure « une infinité de solutions » dès qu'il y a une variable libre | $\mathbf{A}$ de rang 2 à 4 colonnes, $\mathbf{b}$ quelconque | vérifier d'abord que $\mathbf{b} \in \operatorname{Im}\mathbf{A}$ ; sinon, aucune solution |
| Écrire $\mathbf{S}\mathbf{A}\mathbf{S}^{-1}$ pour la matrice dans la base $\mathbf{S}$ | `S @ A @ np.linalg.inv(S)` | $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$, `np.linalg.solve(S, A @ S)` ; vérifier sur $\mathbf{A}'\mathbf{e}_1$ |
| Inverser une application affine en oubliant que la translation est transformée | $\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}\mathbf{y} - \mathbf{b}$ | $\mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$ : retirer $\mathbf{b}$ d'abord ; vérifier $\varphi^{-1}(\mathbf{b}) = \mathbf{0}$ |
| Croire qu'un rang calculé en flottants est exact | « `matrix_rank` dit 3, donc aucune colonne n'est redondante » | dire la tolérance ; une relation vraie à $10^{-12}$ près est redondante pour des mesures ; mettre les colonnes à la même échelle |

## Orthogonalité et projections (M12b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre une matrice symétrique à coefficients positifs pour un produit scalaire | « $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ définit un produit scalaire » | vérifier $a > 0$ et $ac - b^2 > 0$ ; ici $ac - b^2 = -1$, et $(3, -2)$ donne $-2$ |
| Dire « orthogonaux » sans préciser le produit scalaire | « $(1, -1)$ et $(0, 1)$ ne sont jamais orthogonaux » | pour $\mathbf{M} = \begin{pmatrix} 3 & 1 \\ 1 & 1 \end{pmatrix}$, ils le sont ; l'orthogonalité dépend du produit scalaire |
| Appeler orthogonale une matrice à colonnes seulement orthogonales | $\begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix}$ « orthogonale, donc son inverse est sa transposée » | il faut des colonnes **orthonormées** : $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$ |
| Lire des coordonnées par produits scalaires dans une base non orthonormée | $c_4 = \mathbf{x} \cdot (2\mathbf{u}_4)$ | diviser par $\lVert 2\mathbf{u}_4 \rVert^2$, ou résoudre le système |
| Oublier de normer dans Gram-Schmidt | $\mathbf{q}_2 = \mathbf{a}_2 - (\mathbf{a}_2 \cdot \mathbf{q}_1)\,\mathbf{q}_1$ | diviser $\mathbf{v}_2$ par sa norme, puis vérifier $\lVert \mathbf{q}_2 \rVert = 1$ |
| Projeter sur les $\mathbf{a}_j$ au lieu des $\mathbf{q}_j$ | $\mathbf{v}_2 = \mathbf{a}_2 - (\mathbf{a}_2 \cdot \mathbf{q}_1)\,\mathbf{a}_1$ | retirer la projection sur le vecteur **unitaire** $\mathbf{q}_1$ |
| Confondre $U^\perp$ et le complémentaire de $U$ | « $U^\perp$ contient tous les vecteurs hors du plan » | $U^\perp$ est un sous-espace (un noyau), de dimension $n - \dim U$ |
| Former la projection avec une base non orthonormée | `P = A @ A.T` | `Q = gram_schmidt(A)` puis `Q @ Q.T`, ou $\mathbf{A}(\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top$ |
| Prendre $\lVert \mathbf{p} \rVert$ pour la distance à $U$ | la distance de $\mathbf{v}$ au plan égale à la longueur du projeté | $\lVert \mathbf{v} - \mathbf{p} \rVert$, la norme du résidu |
| Conclure « projection orthogonale » de la seule idempotence | $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ « vérifie $\mathbf{M}^2 = \mathbf{M}$, donc projette orthogonalement » | vérifier aussi $\mathbf{M}^\top = \mathbf{M}$ ; sinon, c'est une projection oblique |
| Voir les résidus des moindres carrés perpendiculaires à la droite | dessiner les écarts à angle droit de la droite ajustée | ils sont verticaux ; l'angle droit est dans $\mathbb{R}^n$, entre $\mathbf{y} - \hat{\mathbf{y}}$ et les colonnes de $\mathbf{X}$ |
| Résoudre $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$ depuis la première ligne | `for i in range(p): w[i] = (z[i] - R[i, :i] @ w[:i]) / R[i, i]` | $\mathbf{R}$ est triangulaire supérieure : remonter depuis la dernière ligne |
| Comparer directement sa QR à celle de NumPy | « `np.linalg.qr` donne $r_{11} < 0$, ma fonction est fausse » | QR est unique au signe près : comparer après $\mathbf{D} = \operatorname{diag}(\operatorname{signe}(r_{kk}))$ |
| Faire confiance à Gram-Schmidt classique sur des colonnes presque dépendantes | des features polynomiales de degré 10 : $\mathbf{Q}^\top\mathbf{Q}$ « vaut $\mathbf{I}$ » | mesurer $\max \lvert \mathbf{Q}^\top\mathbf{Q} - \mathbf{I} \rvert$ ; procédé modifié, ou orthogonaliser deux fois |
| Croire qu'une orthogonalité de fonctions ne dépend pas de l'intervalle | « $x$ et $x^2$ sont orthogonales » | vrai sur $[-1 ; 1]$, faux sur $[0 ; 1]$ ($\int_0^1 x^3\,dx = \frac{1}{4}$) |

## Valeurs propres et matrices symétriques (M12c)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Croire le déterminant additif | « $\det(\mathbf{A} + \mathbf{B}) = \det\mathbf{A} + \det\mathbf{B}$ » | il est multiplicatif, pas additif : calculer $\det(\mathbf{A} + \mathbf{B})$ ; et $\det(c\mathbf{A}) = c^n\det\mathbf{A}$ |
| Oublier le signe des échanges de lignes | un déterminant calculé par élimination avec un échange, sans changer le signe | compter les échanges : $(-1)^{\text{échanges}} \times$ le produit des pivots |
| Lire un petit déterminant comme « presque singulière » | « $\det = 10^{-9}$, la matrice est presque non inversible » | $\det(0{,}1\,\mathbf{I}_9) = 10^{-9}$ : regarder le conditionnement (M12d) |
| Lire les valeurs propres sur la diagonale d'une matrice non triangulaire | $\begin{pmatrix} 5 & 2 \\ 1 & 4 \end{pmatrix}$ « a pour valeurs propres 5 et 4 » | résoudre $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ (ici 6 et 3) ; la diagonale suffit seulement pour une matrice triangulaire |
| Prendre la trace d'un produit pour le produit des traces | « $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}\mathbf{A}\,\operatorname{tr}\mathbf{B}$ » | seule $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$ est vraie |
| Accepter un vecteur propre nul | `np.linalg.solve(A - lam * np.eye(n), np.zeros(n))` rend le vecteur nul | un vecteur propre est non nul : prendre un vecteur du noyau de $\mathbf{A} - \lambda\mathbf{I}$ (à la main, ou `np.linalg.eig`) |
| Conclure « diagonalisable » d'une valeur propre double, ou l'inverse | « $\begin{pmatrix} 5 & 1 \\ 0 & 5 \end{pmatrix}$ a la valeur propre 5, donc $\mathbf{P} = \mathbf{I}$ convient » ; « une valeur propre double empêche la diagonalisation » | comparer la dimension de l'espace propre à la multiplicité : ici 1 contre 2, défective ; $\mathbf{I}$, elle, est diagonale |
| Calculer $\mathbf{A}^k$ terme à terme | « $\mathbf{A}^{10}$ = la matrice des puissances dixièmes des éléments » | $\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$ ; seule une matrice diagonale se met à la puissance élément par élément |
| Oublier la convention de signe de la méthode de la puissance | avec $\lambda_1 < 0$, $\mathbf{x}_k$ change de signe à chaque pas et l'arrêt n'arrive jamais | fixer le signe (la coordonnée de plus grande valeur absolue positive) avant de comparer deux itérés |
| Rendre $\lVert \mathbf{A}\mathbf{x} \rVert$ comme valeur propre | `value = np.linalg.norm(A @ x)` : toujours positive | le quotient de Rayleigh $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ pour $\mathbf{x}$ unitaire, qui garde le signe |
| Croire « valeurs propres réelles » équivalent à « symétrique » | « $\begin{pmatrix} 2 & 1 \\ 0 & 4 \end{pmatrix}$ a des valeurs propres réelles, donc ses vecteurs propres sont orthogonaux » | le théorème spectral demande la symétrie ; ici $(1, 0)$ et $(1, 2)$ ne sont pas orthogonaux |
| Juger « définie positive » sur la diagonale ou sur le signe des éléments | « $\begin{pmatrix} 4 & 6 \\ 6 & 7 \end{pmatrix}$ est définie positive » | les mineurs principaux : $28 - 36 < 0$, indéfinie |
| Prendre le plus grand élément pour le maximum de $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ sur la sphère | « le maximum de $\mathbf{x}^\top\mathbf{A}\mathbf{x}$, $\lVert \mathbf{x} \rVert = 1$, est $\max a_{ij}$ » | c'est $\lambda_{\max}$, atteint au vecteur propre ; un élément diagonal n'est qu'un quotient de Rayleigh parmi d'autres |
| Allonger l'ellipse le long de la grande valeur propre | « $\mathbf{x}^\top\mathbf{A}\mathbf{x} = c$ est la plus allongée selon $\mathbf{q}_{\max}$ » | les demi-axes valent $\sqrt{c/\lambda_i}$ : la plus allongée selon le vecteur propre de la **plus petite** valeur propre |
| Rendre $\mathbf{L}^\top$ au lieu de $\mathbf{L}$ | un facteur de Cholesky triangulaire supérieur | $\mathbf{L}$ est triangulaire **inférieure**, $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$ |
| Faire confiance à `np.linalg.cholesky` sur une matrice non symétrique | `np.linalg.cholesky([[9, 3], [-6, 5]])` rend un facteur, sans erreur | elle ne lit que le triangle inférieur : vérifier la symétrie avant |
| Prendre la racine carrée d'une matrice élément par élément | `np.sqrt(Sigma)` comme $\boldsymbol{\Sigma}^{1/2}$ | $\mathbf{Q}\,\operatorname{diag}(\sqrt{\lambda_i})\,\mathbf{Q}^\top$ (`eigh`), ou `scipy.linalg.sqrtm` |
| Oublier les covariances dans la variance d'une somme | « $\mathbb{V}(x_1 + x_2) = \mathbb{V}(x_1) + \mathbb{V}(x_2)$ » pour des features corrélées | $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ : ajouter $2\operatorname{Cov}(x_1, x_2)$ |
| Blanchir sans regarder les petites valeurs propres | $\lambda_i = 10^{-4}$ : la coordonnée sur cet axe est multipliée par 100, et le bruit de mesure pèse autant que le reste | regarder le spectre avant de blanchir ; une valeur propre minuscule signale du bruit ou des features presque identiques |
| Confondre les blanchiments | $\mathbf{W} = \mathbf{L}$, ou $\mathbf{L}^{-\top}$, ou $\boldsymbol{\Sigma}^{1/2}$ | vérifier $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ : $\mathbf{L}^{-1}$, $\boldsymbol{\Sigma}^{-1/2}$ ou $\boldsymbol{\Lambda}^{-1/2}\mathbf{Q}^\top$ |

## SVD et analyse en composantes principales (M12d)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre les valeurs propres de $\mathbf{A}$ pour ses valeurs singulières | « $\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ n'a pas de valeur singulière réelle » | les valeurs singulières sont les racines des valeurs propres de $\mathbf{A}^\top\mathbf{A}$, toujours positives : ici 2 et 2 |
| Oublier la racine carrée | « $\mathbf{A}^\top\mathbf{A}$ a pour valeurs propres 25 et 4, donc $s = 25$ et $4$ » | $s_i = \sqrt{\lambda_i}$ : 5 et 2 |
| Ne pas diviser $\mathbf{A}\mathbf{v}_i$ par $s_i$ | $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i$, de norme $s_i$ | $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i/s_i$, unitaire |
| Lire les $\mathbf{v}_i$ en colonnes de `Vt` | `Vt[:, 0]` pris pour $\mathbf{v}_1$ | `np.linalg.svd` rend $\mathbf{V}^\top$ : $\mathbf{v}_1$ est la ligne `Vt[0]` |
| Changer le signe d'un seul vecteur singulier | $\mathbf{v}_1 \to -\mathbf{v}_1$ sans toucher à $\mathbf{u}_1$ | changer $\mathbf{u}_i$ et $\mathbf{v}_i$ ensemble ; fixer une convention avant de comparer deux SVD |
| Calculer l'erreur de rang $k$ avec les $s_i$ | « $\lVert \mathbf{A} - \mathbf{A}_1 \rVert_F = s_2 + s_3$ » | $\sqrt{s_2^2 + s_3^2}$ (Eckart-Young) |
| Mesurer l'énergie d'une image non centrée | « le rang 1 garde 95 % de l'énergie, la compression est excellente » | retirer d'abord le niveau moyen ; regarder aussi l'image |
| Transposer la pseudo-inverse | $\mathbf{A}^+$ de la forme de $\mathbf{A}$ | $\mathbf{A}^+ = \mathbf{V}\mathbf{S}^{-1}\mathbf{U}^\top$ est de forme $(n, m)$ |
| Inverser une valeur singulière minuscule | `1 / s` avec $s = 10^{-12}$ (du bruit) | tronquer sous un seuil relatif (`rcond`) ou régulariser (ridge) |
| Juger le conditionnement par le déterminant | « $\det = 1$, le système est bien posé » | $\kappa = s_{\max}/s_{\min}$ : une matrice de déterminant 1 peut avoir $\kappa = 10^4$ |
| Former $\mathbf{A}^\top\mathbf{A}$ pour une matrice mal conditionnée | les équations normales avec $\kappa = 10^7$ | $\kappa(\mathbf{A}^\top\mathbf{A}) = \kappa^2$ : QR ou SVD sur $\mathbf{A}$ |
| Une ACP sans centrer | les vecteurs propres de $\mathbf{X}^\top\mathbf{X}$ | centrer : sinon le premier axe pointe vers la moyenne |
| Prendre le premier vecteur de `eigh` pour le premier axe | `axes = vectors[:, 0]` | `eigh` range par ordre **croissant** : la dernière colonne, ou retourner l'ordre |
| Lire les axes en lignes | `vectors[order]` pour réordonner les axes | les vecteurs propres sont les **colonnes** : `vectors[:, order]` (et `components_` de scikit-learn les range en lignes) |
| Mélanger $n$ et $n - 1$ | des variances de scores avec `np.var` (en $n$) comparées à une covariance en $n - 1$ | dire la convention, et la garder partout : `np.var(..., ddof=1)`, $\lambda_j = s_j^2/(n - 1)$ |
| Oublier `rowvar=False` | `np.cov(X)` avec les exemples en lignes : une matrice $n \times n$ | `np.cov(X, rowvar=False)` |
| Calculer les parts sur les $k$ premières variances | « avec 2 axes sur 5, les parts sont 70 % et 30 % » | diviser par la somme de **toutes** les variances |
| Standardiser sans y penser, ou ne pas standardiser | des pixels réduits à variance 1 ; des euros et des kilomètres seulement centrés | standardiser si les unités diffèrent ; sinon centrer seulement |
| Juger l'erreur de reconstruction sur l'entraînement | un seuil d'anomalie fixé sur les données qui ont servi aux axes | calculer les axes sur l'entraînement, mesurer et fixer les seuils sur d'autres données |
| Lire des distances sur une carte t-SNE | « ces deux groupes sont deux fois plus éloignés que ceux-là » | la divergence KL ne contraint presque pas l'écart entre deux groupes séparés : une carte montre des voisinages, elle ne mesure pas |

## Vraisemblance et régression logistique (M13a)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Dériver la vraisemblance au lieu de la log-vraisemblance | dériver $p^{12}(1 - p)^{30}$ par la règle du produit | passer au logarithme : $12\ln p + 30\ln(1 - p)$, même maximum |
| Diviser par $n - 1$ le maximum de vraisemblance d'une variance | `np.var(x, ddof=1)` pour $\hat{\sigma}^2$ | $\frac{1}{n}$ pour le maximum de vraisemblance (`np.var(x)`), $\frac{1}{n-1}$ pour l'estimation sans biais |
| Une probabilité 0 pour une valeur jamais vue | $\hat{p}_k = \frac{0}{N}$, puis $\ln 0 = -\infty$ sur une observation nouvelle | lisser : $\frac{n_k + \alpha}{N + K\alpha}$ |
| Lisser le numérateur seulement | $\frac{n_k + 1}{N}$ | $\frac{n_k + 1}{N + K}$ : les probabilités doivent sommer à 1 |
| $-\ln\hat{p}$ pour un label 0 | le terme de $(y, \hat{p}) = (0 ;\ 0{,}3)$ pris égal à $-\ln 0{,}3$ | $-\ln(1 - \hat{p}) = -\ln 0{,}7$ |
| Mélanger nats et bits | une log-loss de `sklearn` comparée à une entropie de M06 | les bibliothèques sont en nats ; diviser par $\ln 2$ pour des bits |
| Calculer $\ln(1 + e^z)$ tel quel | `np.log(1 + np.exp(900))` donne `inf` | $\max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$, avec `np.log1p` |
| Calculer la log-loss à partir de $\sigma(z)$ arrondi | $\sigma(45)$ arrondi à 1, puis $\ln(1 - 1) = -\infty$ | écrire le terme avec le score : $s(z) - yz$ |
| Lire un poids logistique comme un effet sur la probabilité | « $w_j = 0{,}5$ : la probabilité monte de 0,5 » | la log-cote monte de $w_j$, la cote est multipliée par $e^{w_j}$ |
| Confondre indépendance et indépendance conditionnelle | « Naïve Bayes suppose les features indépendantes » | indépendantes **sachant la classe** |
| Oublier les proportions des classes | comparer seulement $p(\mathbf{x} \mid k)$ entre les classes | comparer $\pi_k\,p(\mathbf{x} \mid k)$ (en logarithmes) |
| Moyenner des impuretés sans pondérer | la moyenne simple des entropies de deux groupes de 2 et 98 exemples | pondérer par les tailles des groupes |
| Prendre le taux d'erreur pour l'indice de Gini | « $(0{,}9 ;\ 0{,}05 ;\ 0{,}05)$ a un Gini de 0,1 » | $G = 1 - \sum_k p_k^2 = 0{,}185$ ; $1 - \max_k p_k$ est le taux d'erreur |
| Mélanger $\frac{1}{n}$ et $\frac{1}{n - 1}$ dans la décomposition de la variance | la variance totale en $\frac{1}{n-1}$, celles des groupes en $\frac{1}{n}$ | la même convention partout ($\frac{1}{n}$) pour que total = intra + inter |

## Optimisation sous contraintes et SVM (M13b)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre un point de Lagrange pour un minimum | « $\nabla f + \lambda\nabla g = \mathbf{0}$, donc c'est le minimum » | la condition est nécessaire : comparer les candidats, ou invoquer la convexité |
| Oublier de tester le minimum libre | supposer une inégalité active alors que le minimum libre est admissible | regarder d'abord le minimum libre ; s'il est admissible, $\mu = 0$ |
| Accepter un multiplicateur d'inégalité négatif | « $\mu = -\frac43$ : la solution est sur le bord » | $\mu < 0$ dit que la contrainte ne doit pas être active : changer d'ensemble actif |
| Mélanger les conventions de signe | lagrangien $f - \lambda g$ dans un calcul, $f + \lambda g$ dans l'autre | fixer la convention ($g \le 0$, $f + \sum_i \mu_i g_i$, $\mu_i \ge 0$) et s'y tenir |
| Croire que la fonction duale peut dépasser le minimum | « $D(12) = 30 > f^*$ » | $D \le f^*$ toujours (dualité faible) : une valeur plus grande signale une erreur de calcul |
| Juger la convexité sur l'objectif seul | « $\min x$ sous $x^2 + y^2 = 4$ est convexe : l'objectif est linéaire » | vérifier aussi chaque contrainte : une égalité doit être affine |
| Confondre marge et largeur de la bande | « $\lVert\mathbf{w}\rVert = 0{,}5$ : marge de 4 » | $\rho = \frac{1}{\lVert\mathbf{w}\rVert} = 2$ ; la bande a une largeur $2\rho$ |
| $C$ fois la moyenne des hinges au lieu de la somme | $J = \frac12\lVert\mathbf{w}\rVert^2 + C \cdot \frac1n\sum_i \ell_i$ | $J = \frac12\lVert\mathbf{w}\rVert^2 + C\sum_i \ell_i$, ou la forme moyenne avec $\lambda = \frac{1}{nC}$ |
| Compter dans le sous-gradient les exemples bien au-delà de la marge | soustraire $C y_i\mathbf{x}_i$ pour tous les exemples | seuls les exemples de marge fonctionnelle strictement inférieure à 1 comptent |
| Lire $b$ sur un vecteur de support borné | $b = y_i - \mathbf{w} \cdot \mathbf{x}_i$ avec $\alpha_i = C$ | le lire sur un vecteur libre ($0 < \alpha_i < C$), qui est exactement sur le bord |
| Oublier les labels dans $\mathbf{w}$ | $\mathbf{w} = \sum_i \alpha_i\mathbf{x}_i$ | $\mathbf{w} = \sum_i \alpha_i y_i\mathbf{x}_i$ |
| Oublier le carré dans le noyau RBF | $e^{-\gamma\lVert\mathbf{x} - \mathbf{z}\rVert}$ | $e^{-\gamma\lVert\mathbf{x} - \mathbf{z}\rVert^2}$ (`sklearn` aussi) |
| Oublier les monômes de bas degré du noyau polynomial | « $(1 + \mathbf{x} \cdot \mathbf{z})^2$ en dimension $p$ : $\binom{p + 1}{2}$ coordonnées » | $\binom{p + 2}{2}$ : les monômes de degré **au plus** 2, constante comprise |
| Prendre n'importe quelle fonction de deux points pour un noyau | « $\lVert\mathbf{x} - \mathbf{z}\rVert^2$ compare deux points : c'est un noyau » | un noyau est symétrique et a des matrices de Gram semi-définies positives ; ce n'est pas le cas ici |

## Les maths des ensembles (M14)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Prendre $P(X > k)$ pour $P(X \ge k)$ | « au moins 7 sur 9 » : `binom.sf(7, 9, p)` | `binom.sf(k - 1, n, p)`, car `sf(m)` rend $P(X > m)$ |
| Inverser la divergence de Chernoff | $e^{-n\,\mathrm{KL}(p \Vert a)}$ | $\mathrm{KL}(a \Vert p)$ : la proportion de l'événement d'abord, le paramètre de la loi ensuite |
| Croire qu'une borne pour $a \le p$ dit quelque chose | « Chernoff donne 1, donc l'événement est sûr » | pour $a \le p$, la borne vaut 1 : elle ne dit rien, et l'événement n'est pas rare |
| Oublier les covariances dans la variance d'une moyenne | $\mathbb{V}\big(\sum_i w_iX_i\big) = \sum_i w_i^2\,\mathbb{V}(X_i)$ pour des variables corrélées | $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$, toutes les cases de la matrice |
| Diviser par $M$ des modèles corrélés | « 50 modèles de variance 2 : variance 0,04 » | le terme en $\frac{1}{M}$ ne porte que sur les parts propres ; les covariances laissent un plancher |
| Croire $(1 + x/n)^n \approx e^x$ dès que $n$ est « grand » | $n = 30$ pour $x = 3$ : « à 1 % près » | l'erreur relative vaut environ $-\frac{x^2}{2n}$ : il faut $n$ grand devant $x^2$ |
| Oublier de renormaliser les poids de Hedge | $w_t[k] = e^{-\eta L_t[k]}$ | diviser par la somme ; les poids sont une loi sur les experts |
| Laisser déborder l'exponentielle | `np.exp(-eta * L)` avec $\eta L$ de l'ordre de 1 000 : $\frac{0}{0}$ | retrancher $\min_j L_t[j]$ avant l'exponentielle (log-somme-exp) |
| Se tromper de signe dans les poids exponentiels | $w \propto e^{+\eta L}$ | une grande loss donne un **petit** poids : $e^{-\eta L}$ |
| Utiliser la loss du tour au lieu de la loss cumulée | $w_t[k] \propto e^{-\eta\ell_{t-1}[k]}$ | $L_t[k] = \sum_{s < t}\ell_s[k]$, la somme des tours précédents |
| Confondre le gradient par rapport aux prédictions et aux paramètres | « le gradient de la loss exponentielle a autant de coordonnées que le modèle a de coefficients » | $\nabla_{\mathbf{F}}\mathcal{L}$ a une coordonnée par exemple ; la règle de la chaîne mène aux paramètres |
| Ne pas couper le gradient de Huber | $-(y - F)$ pour un résidu de 2,7 avec $\delta = 0{,}8$ | $-\operatorname{clip}(y - F, -\delta, \delta)$ : au plus $\delta$ en valeur absolue |

## Applications affines, graphes et variance d'un produit (M16)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Ranger $\mathbf{W}$ dans la mauvaise convention | une application de $\mathbb{R}^3$ dans $\mathbb{R}^3$ écrite en colonnes et calculée par `x @ W` : aucune erreur, mais c'est l'application de $\mathbf{W}^\top$ | en lignes, $\mathbf{W}$ a la forme (entrées, sorties) ; vérifier une sortie sur un point connu, comme $(1, 0, \ldots, 0)$ |
| Mélanger les rangements d'une matrice homogène | la translation dans la dernière colonne, puis $[\mathbf{x}, 1]\,\mathbf{H}$ | en lignes, $\mathbf{b}$ sur la dernière **ligne** et $(0, \ldots, 0, 1)$ en dernière colonne ; en colonnes, l'inverse |
| Multiplier les matrices homogènes dans le mauvais ordre | $f_1$ puis $f_2$ en lignes : $\mathbf{H}_2\mathbf{H}_1$ | en lignes, la première appliquée est à gauche : $\mathbf{H}_1\mathbf{H}_2$ (à droite avec des colonnes) |
| Lire $(\mathbf{A}^k)_{ij}$ comme « il existe un chemin » | « $(\mathbf{A}^2)_{14} = 0$, donc 4 est inaccessible depuis 1 » | $(\mathbf{A}^k)_{ij}$ compte les chemins d'exactement $k$ arêtes ; regarder toutes les longueurs |
| Confondre ligne et colonne de la matrice d'adjacence | le degré entrant de $j$ lu sur la ligne $j$ | ligne $i$ : les arêtes qui partent de $i$ ; colonne $j$ : celles qui arrivent en $j$ |
| Calculer $(\mathbf{I} - \mathbf{A})^{-1}$ sur un graphe qui a un cycle | `np.linalg.inv(np.eye(n) - A)` appelé « somme sur les chemins » | vérifier d'abord l'absence de cycle (puissances de $\mathbf{A}$, ou une numérotation triangulaire) |
| Oublier deux termes de la variance d'un produit | $\mathbb{V}(XY) = \mathbb{V}(X)\,\mathbb{V}(Y)$ pour des variables non centrées | $\mathbb{V}(X)\,\mathbb{V}(Y) + \mathbb{V}(X)\,\mathbb{E}[Y]^2 + \mathbb{V}(Y)\,\mathbb{E}[X]^2$, pour des variables **indépendantes** |
| Mettre $\mathbb{V}(x_i)$ à la place de $\mathbb{E}[x_i^2]$ | $\mathbb{V}(\varepsilon x) = \mathbb{V}(x)$ pour $x$ de moyenne 2 | $\mathbb{V}(\varepsilon x) = \mathbb{V}(\varepsilon)\,\mathbb{E}[x^2]$ quand $\varepsilon$ est centré et indépendant de $x$ |
| Croire que décorrélées veut dire indépendantes | « covariance nulle, donc $\mathbb{E}[X^2Y^2] = \mathbb{E}[X^2]\,\mathbb{E}[Y^2]$ » | décorrélées suffit pour additionner des variances, pas pour factoriser n'importe quelle espérance |
| Additionner des écarts-types | 25 termes indépendants d'écart-type 1 : « écart-type 25 » | les variances s'ajoutent : écart-type $\sqrt{25} = 5$ ; 25 seulement si les termes sont égaux |

## Jacobienne et règle de la chaîne (M17)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Transposer la jacobienne | une ligne par **entrée** : $(n, m)$ pour une application de $\mathbb{R}^n$ dans $\mathbb{R}^m$ | une ligne par sortie, une colonne par entrée : $(m, n)$ |
| Prendre $\mathbf{W}$ pour la jacobienne de $\mathbf{x} \mapsto \mathbf{x}\mathbf{W} + \mathbf{b}$ | « la jacobienne d'une application en lignes est $\mathbf{W}$ » | c'est $\mathbf{W}^\top$ : la sortie $k$ est $\sum_jx_jW_{jk}$ |
| Multiplier les jacobiennes dans l'ordre d'application | $\mathbf{J}_{\mathbf{f}}\mathbf{J}_{\mathbf{g}}$ pour $\mathbf{g} \circ \mathbf{f}$ | $\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}$ : la dernière appliquée à gauche |
| Évaluer une jacobienne au mauvais point | $\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))$ : au point intermédiaire ; calculer d'abord tous les points intermédiaires |
| Oublier la transposée du gradient en colonne | $\nabla_{\mathbf{x}}(L \circ \mathbf{f}) = \mathbf{J}_{\mathbf{f}}\nabla_{\mathbf{y}}L$ | $\mathbf{J}_{\mathbf{f}}^\top\nabla_{\mathbf{y}}L$ (en colonne) ou $\nabla_{\mathbf{y}}L\,\mathbf{J}_{\mathbf{f}}$ (en ligne) |
| Utiliser le raccourci diagonal sur une application quelconque | $\frac{\mathbf{A}(\mathbf{x} + h\mathbf{1}) - \mathbf{A}(\mathbf{x} - h\mathbf{1})}{2h}$ pris pour la diagonale de $\mathbf{A}$ | il donne $\mathbf{A}\mathbf{1}$ ; il ne vaut que pour une fonction appliquée coordonnée par coordonnée |
| Former la jacobienne pour un produit par un vecteur | `numerical_jacobian(f, x) @ v` pour $n = 10^4$ | `jacobian_vector_product(f, x, v)` : 2 évaluations au lieu de $2n$ |
| Donner une seule dérivée en un point anguleux | « la dérivée de l'impôt en 30 k€ vaut 0,3 » | deux dérivées latérales, 0,2 et 0,4 ; des sous-gradients seulement pour une fonction convexe |
| Évaluer toutes les dérivées d'une longue composition au départ | $\frac{\mathrm{d}x_L}{\mathrm{d}x_0} = \varphi'(x_0)^L$ | $\prod_k\varphi'(x_k)$, le long de la trajectoire |
| Oublier la normalisation d'une loi de Boltzmann | $p_i = e^{-E_i/T}$ | diviser par $Z = \sum_je^{-E_j/T}$ ; seuls les rapports se passent de $Z$ |
| Confondre $\mathbf{p}^\top\mathbf{p}$ et $\mathbf{p}\,\mathbf{p}^\top$ pour une ligne $\mathbf{p}$ | $\operatorname{diag}(\mathbf{p}) - \sum_ip_i^2$ | $\mathbf{p}^\top\mathbf{p}$ est la matrice $K \times K$ des produits $p_ip_j$ |

## Différentiation automatique et calcul matriciel (M18)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier un chemin dans un graphe de calcul | $\frac{\partial y}{\partial t}$ calculé par le seul chemin $t \to u_2 \to u_3 \to y$, quand $t$ sert aussi dans $u_4 = t^2$ | sommer sur **tous** les chemins ; un nœud qui sert deux fois a deux arêtes sortantes |
| Une seule arête pour $t \cdot t$ | dérivée locale $t$ pour $u = t \cdot t$ | $2t$ : une opération qui prend deux fois le même argument a deux arêtes vers lui |
| Mettre la graine sur deux entrées pour une dérivée partielle | $x = 2 + \varepsilon$, $y = -1 + \varepsilon$ pour $\frac{\partial f}{\partial x}$ | une graine par passe ($y = -1$) ; deux graines donnent la dérivée dans la direction $(1, 1)$ |
| Ne garder qu'une contribution à un adjoint | $\bar{t} = \bar{u}_2\,v$, en oubliant $\bar{u}_4 \times 2t$ quand $t$ sert aussi dans $u_4 = t^2$ | sommer les contributions de **tous** les successeurs du nœud |
| Utiliser un adjoint incomplet | calculer $\bar{u}_1$ avant d'avoir $\bar{u}_2$, alors que $u_1 \to u_2$ | visiter les nœuds dans l'ordre inverse du calcul |
| Choisir le mode direct pour un gradient de beaucoup de variables | $n = 10^4$ passes directes pour une fonction réelle | une passe arrière (le gradient bon marché) |
| Rendre la transposée d'un gradient matriciel | $\nabla_{\mathbf{X}}\operatorname{tr}(\mathbf{A}\mathbf{X}) = \mathbf{A}$ ; $\nabla\ln\det\mathbf{X} = \mathbf{X}^{-1}$ | $\mathbf{A}^\top$ et $\mathbf{X}^{-\top}$ : $\mathrm{d}f = \operatorname{tr}(\mathbf{M}\,\mathrm{d}\mathbf{X})$ donne $\mathbf{G} = \mathbf{M}^\top$ |
| Écrire $2\mathbf{A}\mathbf{X}$ pour $\mathbf{A}$ quelconque | $\nabla\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X}) = 2\mathbf{A}\mathbf{X}$ | $(\mathbf{A} + \mathbf{A}^\top)\mathbf{X}$ |
| Changer l'ordre des facteurs dans une différentielle | $\mathrm{d}(\mathbf{X}^2) = 2\mathbf{X}\,\mathrm{d}\mathbf{X}$ | $\mathrm{d}\mathbf{X}\,\mathbf{X} + \mathbf{X}\,\mathrm{d}\mathbf{X}$ : les matrices ne commutent pas |
| Vérifier un gradient avec une direction symétrique | $\mathbf{H} = \mathbf{I}$ ou la matrice pleine de 1 : un gradient transposé passe | une direction tirée au hasard, non symétrique, et plusieurs |
| Vérifier avec un pas trop petit | $h = 10^{-13}$ : les arrondis divisés par $2h$ font croire à une erreur | $h$ de l'ordre de $10^{-5}$ pour une différence centrée en `float64` |
| Sommer au lieu de faire la moyenne | $\nabla\frac1N\sum_kf_k = \sum_k\nabla f_k$ | $\frac1N\sum_k\nabla f_k$ |

## Hessienne, conditionnement et convergence (M19)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier le $\frac12$ du terme d'ordre 2 | $f(\mathbf{x} + \mathbf{h}) \approx f + \nabla f^\top\mathbf{h} + \mathbf{h}^\top\mathbf{H}\mathbf{h}$ | $\frac12\mathbf{h}^\top\mathbf{H}\mathbf{h}$, comme le $\frac12f''h^2$ d'une variable |
| Calculer $H_{ij}$ et $H_{ji}$ séparément dans une hessienne numérique | deux formules qui diffèrent par les arrondis, puis `np.linalg.eigvalsh`, qui ne lit qu'un triangle | calculer chaque case au-dessus de la diagonale une fois, puis la recopier |
| Classer un point critique par la diagonale de la hessienne | $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ « positive », donc un minimum | les signes des **valeurs propres** ($3$ et $-1$ : une selle) |
| Conclure par le déterminant en dimension 3 | $\det\mathbf{H} = 6 > 0$, donc un minimum, pour des valeurs propres $(-1, -2, 3)$ | regarder toutes les valeurs propres |
| Regarder la plus grande valeur propre signée | valeurs propres $0{,}5$ et $-1{,}2$ : « tout est sous 1, ça converge » | le plus grand **module** : $1{,}2 > 1$, l'itération diverge |
| Régler le pas sur la plus petite valeur propre | $\omega = 2/\lambda_{\min}$ | $\omega < 2/\lambda_{\max}$ : c'est la plus grande valeur propre qui fixe le pas critique |
| Croire qu'un facteur près de 1 suffit | $\rho = 0{,}99$ « converge vite » | environ 230 itérations par décimale gagnée : regarder $\frac{\ln 10}{-\ln\rho}$ |
| Croire que multiplier le système change le conditionnement | multiplier $\mathbf{A}$ et $\mathbf{b}$ par 100 « pour aller plus vite » | le pas critique est divisé par 100, $\kappa$ et le nombre d'itérations ne changent pas ; mettre les **inconnues** à l'échelle peut le changer |
| Se tromper de signe sur $q$ | $u_{k+2} = 1{,}5\,u_{k+1} + u_k$ écrit $r^2 - 1{,}5r + 1$ | $u_{k+2} = a\,u_{k+1} + b\,u_k$ donne $r^2 - ar - b$ |
| Prendre la partie réelle pour le module | racines $0{,}4 \pm 0{,}4\sqrt3\,i$ « de module $0{,}4$ » | $\sqrt{0{,}4^2 + 0{,}48} = 0{,}8 = \sqrt q$ |
| Diviser l'erreur type par $B$ | estimation sur $B = 4$ termes : erreur type $\sigma/4$ | $\sigma/\sqrt B = \sigma/2$ ; la **variance** est divisée par $B$ |
| Projeter sur la boule en coupant les coordonnées | $(15, -8)$ sur la boule de rayon $3{,}4$ : $(3{,}4 ;\ -3{,}4)$ | $\mathbf{x}\min(1, r/\lVert\mathbf{x}\rVert) = (3 ;\ -1{,}6)$ ; couper les coordonnées projette sur un pavé |

## Tenseurs, axes et estimateurs pondérés (M20)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Remodeler pour réordonner des axes | `img.reshape(3, 480, 640)` pour mettre les canaux d'une image $(480, 640, 3)$ en premier | `img.transpose(2, 0, 1)` ; `reshape` garde l'ordre de la file et mélange les canaux |
| Se tromper d'axe | `N.mean(axis=0)` pour la moyenne de chaque élève d'un tableau (élèves, matières) | l'axe nommé **disparaît** : `N.mean(axis=1)` |
| Oublier `keepdims` avant de soustraire | `T - T.mean(axis=2)` pour un tableau (stations, jours, heures) | `T - T.mean(axis=2, keepdims=True)` |
| La diffusion silencieuse | `u - v` avec `u` de forme $(5,)$ et `v` de forme $(5, 1)$ : un tableau $(5, 5)$, sans erreur | vérifier la forme ; `u - v.ravel()` |
| Composer des variances | la variance sur deux axes calculée comme la variance des variances | la variance sur les deux axes d'un coup, `x.var(axis=(1, 2))` ; ou, pour des groupes de même taille, la moyenne des variances plus la variance des moyennes |
| Mélanger les ddof | `np.var` (divise par $N$) comparé à `pd.Series.var` (divise par $N - 1$) | écrire `ddof` explicitement |
| Oublier qu'une lettre absente du résultat est sommée | `np.einsum("ij,jk->ijk", A, B)` pour un produit matriciel | `"ij,jk->ik"` ; et toujours la forme explicite, avec `->` |
| Croire que la standardisation gomme tout changement | ajouter 10 à une seule valeur « ne change pas les z-scores » | seule une transformation $a\mathbf{x} + b\mathbf{1}$ de **toute** la série, $a > 0$, les laisse inchangés |
| Croire qu'un estimateur sans biais est exact | une estimation de Horvitz-Thompson à deux écarts types du total « est fausse » | sans biais = juste **en moyenne** sur les échantillons possibles |
| Multiplier toutes les valeurs par les indicatrices | `np.sum(y * included / pi)` quand les valeurs non tirées sont des `nan` | `np.sum(y[included] / pi[included])` |
| La moyenne naïve avec des probabilités inégales | `N * y[S].mean()` quand les grandes unités sont tirées plus souvent : biaisée | $\sum_{i \in S} y_i/\pi_i$ |
| Multiplier les jacobiennes dans le mauvais ordre | $\mathbf{J}(\mathbf{x}_0)\,\mathbf{J}(\mathbf{x}_1)$ pour deux pas | $\mathbf{J}(\mathbf{x}_1)\,\mathbf{J}(\mathbf{x}_0)$ : le dernier pas à gauche |

## Convolution, matrices de Toeplitz et équivariance (M21)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Passer à `np.convolve` les poids d'une corrélation | `np.convolve(x, [-1, 0, 1], "valid")` pour la différence centrée $f_{i+1} - f_{i-1}$ : le signe est inversé | retourner les poids, `np.convolve(x, w[::-1], "valid")`, ou `np.correlate(x, w, "valid")` ; et dire laquelle des deux opérations on calcule |
| Écrire la convolution avec $b_{m+i}$ | $\sum_i a_i\,b_{m+i}$ « pour la convolution » | c'est la corrélation ; la convolution est $\sum_i a_i\,b_{m-i}$ (les indices ont une somme constante) |
| Se tromper de longueur | $(1, -2, 4) * (3, 1)$ « a 3 termes, comme la plus longue suite » | $n + k - 1 = 4$ termes : $(3, -5, 10, 4)$ ; additionner **toute** chaque anti-diagonale du tableau des produits |
| Comparer deux « même taille » avec un noyau pair | `np.convolve(x, [3, 1], "same")` « égal » à la corrélation de poids $(1, 3)$ avec `padding="same"` de PyTorch | elles sont décalées d'une case : $(6, 20, 9, 16)$ contre $(20, 9, 16, 5)$ pour $\mathbf{x} = (2, 6, 1, 5)$ |
| Croire qu'un filtrage valide ne perd rien | « la différence $(-1, 1)$ en mode valide est injective » | une convolution valide a un $\ker$ de dimension au moins $k - 1$ : la différence efface les signaux constants, $(1, -2, 1)$ les signaux affines |
| Dire « invariante » pour « équivariante » | « une convolution est invariante par translation » | sa sortie se **déplace** avec l'entrée : elle est équivariante ; seul le pooling global est invariant |
| Oublier le pas dans l'équivariance | avec un pas de 2, décaler l'entrée d'une case « décale la sortie d'une demi-case » | seuls les décalages multiples de $s$ décalent la sortie (de $\frac ts$) ; un autre décalage donne une autre sortie : $(3, 1, 0)$ devient $(0, -5, 1)$ |
| Traiter le pooling max comme linéaire | « le max d'une somme est la somme des max » | $\max(1, 0) + \max(0, 1) = 2$, mais le maximum de $(1, 1)$ vaut 1 ; seul le pooling moyen est linéaire |
| Retourner un noyau circulaire en le renversant | $\mathbf{h} = (4, 1, 0, 2)$ : « $\check{\mathbf{h}} = (2, 0, 1, 4)$ » | $\check{\mathbf{h}} = (h_0, h_{n-1}, \ldots, h_1) = (4, 2, 0, 1)$ : $h_0$ reste en tête |
| Arrondir vers le haut le nombre de positions | $n = 26$, $k = 4$, $s = 3$ : « $\lceil\frac{22}{3}\rceil + 1 = 9$ positions » | $\lfloor\frac{22}{3}\rfloor + 1 = 8$ : la fenêtre incomplète n'existe pas, la case 25 n'est jamais lue |
| Oublier le $+1$, le 2 de $2p$ ou la dilatation | $n = 50$, $k = 4$, $s = 3$, $p = 1$ : « $\lfloor\frac{50 + 1 - 3 - 1}{3}\rfloor = 15$ » | $\lfloor\frac{50 + 2 - 3 - 1}{3}\rfloor + 1 = 17$ ; avec $d = 2$, remplacer $k - 1$ par $d(k - 1)$ : 16 ; et vérifier d'abord que la fenêtre tient, $n + 2p \ge d(k - 1) + 1$ |
| Confondre dilatation et convolution transposée | « la dilatation insère des zéros entre les valeurs du signal » | la dilatation espace les **poids** (la fenêtre lit une case sur $d$) ; la convolution transposée insère $s - 1$ zéros entre les valeurs d'**entrée** |
| Donner une seule taille à une convolution transposée | $m = 5$, $k = 4$, $s = 3$, $p = 0$ : « 16 valeurs » | 16, 17 ou 18 selon $p_{\text{out}} \in \{0, 1, 2\}$ : sans $p_{\text{out}}$, on n'obtient que la plus petite |
| Prendre la convolution transposée pour un inverse | la transposée de la moyenne de 2 valeurs avec un pas de 2 « retrouve » $(6, 2, 5, 9)$ à partir de $(4, 7)$ | elle donne $(2 ;\ 2 ;\ 3{,}5 ;\ 3{,}5)$ : $\mathbf{C}$ n'a pas d'inverse, et $\mathbf{C}^\top$ n'en est pas un |
| Attendre des recouvrements réguliers | une convolution transposée avec $(k, s) = (4, 3)$ « couvre chaque case autant de fois » | les cases reçoivent $(1, 1, 1, 2, 1, 1, 2, 1, 1, 1)$ tampons : réguliers seulement si $s$ divise $k$, sinon un damier en 2D |
| Mêler les deux sens de « séparable » | appeler « noyau séparable » une convolution par canal suivie d'une $1 \times 1$ | un noyau séparable est de rang 1 (il sépare les deux **axes**) ; la « convolution séparable » de workbookIA 21 sépare les **canaux** |
| Séparer un noyau qui n'est pas de rang 1 | prendre la première ligne et la première colonne du laplacien comme facteurs | vérifier le rang (SVD : $s_2 = 0$) ; le laplacien, de rang 2, est une **somme** de deux noyaux séparables |
| Oublier le biais ou les groupes | $10 \times 4 \times 9 = 360$ paramètres pour 4 → 10 canaux, noyaux $3 \times 3$ | $10 \times (4 \times 9 + 1) = 370$ ; avec $g$ groupes, $\frac{C_{\text{in}}}{g}$ au lieu de $C_{\text{in}}$ |
| Lier les paramètres à la taille de la grille | « une grille quatre fois plus petite a quatre fois moins de paramètres » | les paramètres ne dépendent pas de la grille ; le **coût** est proportionnel à l'aire de la sortie (1 080 000 contre 4 320 000) |
| Additionner les noyaux pour le champ récepteur | $(k, s, d) = (4, 2, 1), (3, 2, 1), (3, 1, 2)$ : « $1 + 3 + 2 + 4 = 10$ cases » | chaque étage ajoute $d_\ell(k_\ell - 1)$ fois le produit des pas **précédents** : $1 + 3 + 2 \times 2 + 4 \times 4 = 24$ |
| Associer la boule L∞ à la norme L∞ | pire cas « $\varepsilon\lVert\mathbf{g}\rVert_\infty$ » quand chaque erreur est bornée par $\varepsilon$ | $\varepsilon\lVert\mathbf{g}\rVert_1$ (la norme duale) ; $\varepsilon\lVert\mathbf{g}\rVert_\infty$ est le pire cas sur la boule L1 |
| Prendre $\varepsilon\,\mathbf{g}$ pour le pire cas L∞ | $\boldsymbol{\delta} = 0{,}05\,(3, -1, 2, -2)$ | une coordonnée vaut $0{,}15 > \varepsilon$ : il sort de la boule ; le pire cas est $\varepsilon\operatorname{signe}(\mathbf{g})$, qui ne regarde que les signes |

