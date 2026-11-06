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

## Dérivées (R7)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
| Oublier la dérivée de l'intérieur (composée) | $(e^{x^2})' = e^{x^2}$ | $(e^{x^2})' = 2x\,e^{x^2}$ : multiplier par la dérivée de ce qui est « dedans » |
| Dériver un produit facteur par facteur | $(uv)' = u'v'$ | $(uv)' = u'v + uv'$ |
| Dériver un quotient sans la formule | $\left(\frac{u}{v}\right)' = \frac{u'}{v'}$ | $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ |

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
