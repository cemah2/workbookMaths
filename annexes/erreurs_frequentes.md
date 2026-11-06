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

## Fonctions, exponentielle, logarithme (R3, R6)

| Erreur | Exemple faux | Ce qu'il faut faire |
|---|---|---|
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
