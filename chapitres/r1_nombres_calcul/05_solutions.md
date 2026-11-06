# R1 · Nombres et calcul — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappel](#rappel) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Ponts, estimations, explications](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R1.Q1 — Quel ensemble ? Entiers, décimaux, rationnels, réels
1. **ℤ** : un entier négatif n'est pas un entier naturel.
2. **𝔻** : $\frac{3}{8} = 0{,}375$, l'écriture s'arrête (le dénominateur $8 = 2^3$ n'a que le facteur premier 2).
3. **ℚ** : $\frac{4}{6} = \frac{2}{3} = 0{,}666\ldots$, qui ne s'arrête pas (le facteur 3 du dénominateur l'empêche).
4. **ℕ** : $\sqrt{36} = 6$.
5. **ℝ** : 10 n'est pas un carré parfait, donc $\sqrt{10}$ est irrationnel.
6. **ℤ** : $-\frac{12}{4} = -3$. Simplifie toujours avant de classer.

### R1.Q2 — Priorités et signes : vrai ou faux
1. **Faux** : la multiplication d'abord, $12 - 8 = 4$.
2. **Vrai** : la puissance passe avant le signe moins, $-(3^2) = -9$.
3. **Faux** : de gauche à droite, $18 \div 6 = 3$, puis $3 \times 3 = 9$.
4. **Faux** : soustraire $-2$, c'est ajouter 2 : $7 + 2 = 9$.
5. **Vrai** : trois signes moins, un nombre impair, donc un résultat négatif : $-(2 \times 3 \times 1) = -6$.
6. **Vrai** : $4 - 9 = -5$, et $-(-5) = 5$ ; ou, en distribuant le moins, $-4 + 9 = 5$.

### R1.Q3 — Fractions : quelles opérations sont justes ?
1. **Faux** : même dénominateur, on additionne seulement les numérateurs : $\frac{3}{5}$.
2. **Juste** : $\frac{3 \times 2}{4 \times 9} = \frac{6}{36} = \frac{1}{6}$.
3. **Juste** : $\frac{1}{4} \times \frac{2}{1} = \frac{2}{4} = \frac{1}{2}$ ; un quart, c'est la moitié d'une moitié.
4. **Faux** : $\frac{6 + 5}{6} = \frac{11}{6}$. On ne « simplifie » pas un terme d'une somme par le dénominateur : seul un **facteur** commun au numérateur et au dénominateur se simplifie.
5. **Juste** : on divise en haut et en bas par 5.

### R1.Q4 — Règles des puissances : vrai ou faux
1. **Faux** : on additionne les exposants, $4^{3+2} = 4^5$.
2. **Vrai** : on multiplie les exposants, $5^{2 \times 3} = 5^6$.
3. **Faux** : $7^0 = 1$ (fiche §4, et R1.15 pour le pourquoi).
4. **Faux** : $2^{-4} = \frac{1}{2^4} = \frac{1}{16}$, un nombre positif.
5. **Vrai** : quatre facteurs $-3$, un nombre pair de signes moins.
6. **Vrai**, et c'est le piège : ici les deux termes sont **égaux**, donc $2^3 + 2^3 = 2 \times 2^3 = 2^4 = 16$. En général, $a^m + a^n$ ne se simplifie pas ; c'est la factorisation par $2^3$ qui marche ici.
7. **Faux** : $10^{5 - (-2)} = 10^7$.

### R1.Q5 — Racines carrées : vrai ou faux
1. **Faux** : par définition, $\sqrt{64} = 8$, toujours positif. ($-8$ a aussi pour carré 64, mais ce n'est pas « la racine carrée ».)
2. **Vrai** : $\sqrt{9}\sqrt{16} = 3 \times 4 = 12$, ou $\sqrt{144} = 12$.
3. **Faux** : $\sqrt{25 - 16} = \sqrt{9} = 3$. La racine ne se distribue pas sur une différence.
4. **Vrai** : $\sqrt{36} = 6$.
5. **Vrai** : par définition de la racine carrée.
6. **Vrai** : $\frac{\sqrt{1}}{\sqrt{4}} = \frac{1}{2}$.
7. **Faux** : $(2 + 3)\sqrt{5} = 5\sqrt{5}$ ; ce qui est sous la racine ne change pas.

### R1.Q6 — Notation scientifique et chiffres significatifs
1. **Vrai** : 6, 3 et le zéro final (les zéros de tête ne comptent pas, celui de la fin oui).
2. **Faux** : la mantisse 27 dépasse 10 ; c'est $2{,}7 \times 10^5$.
3. **Vrai** : la virgule recule de 3 rangs.
4. **Vrai** : 4, 8, puis 6 : le 8 monte à 9, et $48\,615 \approx 49\,000$.
5. **Faux** : $8\,200 = 8{,}2 \times 10^3$ et $8{,}2 \ge 3{,}16$ : l'ordre de grandeur est $10^4$.
6. **Faux** : `6.02e23` est un flottant (`float`), même s'il représente un très grand nombre.

### R1.Q7 — Les pièges des évolutions successives
1. **Faux** : $1{,}2 \times 1{,}3 = 1{,}56$, soit +56 %.
2. **Vrai** : $0{,}93 = 1 - 0{,}07$.
3. **Vrai** : coefficient $0{,}5$, réciproque $\frac{1}{0{,}5} = 2$, soit +100 %.
4. **Faux** : $\frac{50 - 40}{40} = 0{,}25$, soit +25 % ; on divise par la valeur de départ.
5. **Faux** : $0{,}9 \times 1{,}1 = 0{,}99$, soit −1 %.
6. **Faux** : il baisse de 2 **points** de pourcentage, mais de 25 % ($\frac{6 - 8}{8} = -0{,}25$).

### R1.Q8 — Moyenne, moyenne pondérée, moyenne harmonique
1. **Faux** : la moyenne vaut 28, loin des trois premières valeurs : la valeur extrême 100 la tire vers le haut.
2. **Vrai** : les coefficients 3 et 6 sont ceux de 1 et 2 multipliés par 3 ; multiplier tous les poids par le même nombre ne change rien.
3. **Faux** : elle reste toujours entre la plus petite et la plus grande valeur.
4. **Faux** : $\frac{2}{\frac{1}{20} + \frac{1}{30}} = \frac{2}{\frac{5}{60}} = 24$, moins que la moyenne arithmétique 25.
5. **Faux** : une somme pondérée ne divise pas par la somme des poids (et les poids peuvent être négatifs).

<a id="rappel"></a>

## 🔁 Rappel

### R1.R1 — Taper une fraction et un intervalle pour `wbm.check` (R0)
1. `"5/12"`, entre guillemets.
2. `"[-1 ; 4["` : crochet fermé du côté de −1 (inclus), ouvert du côté de 4 (exclu). La notation anglaise `"[-1, 4)"` passe aussi.
3. `"]0 ; +oo["` : 0 est exclu (« strictement »), et le crochet est toujours ouvert du côté de l'infini.
4. `"x**3 + 2*x"`, entre guillemets ; dans une chaîne, `"x^3 + 2x"` passe aussi.
5. Python calcule `2/7` en flottant, `0.2857142857142857`, une valeur approchée : `wbm.check` répond que c'est une valeur approchée de la bonne réponse et demande la fraction exacte, entre guillemets.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R1.1 — Placer des nombres sur la droite numérique et les ranger

**Réponses** : a) `"ACEDBF"` · b) `4` · c) `"C"` · d) `"B"`.

**Démarche.** On écrit tout en décimal : $A = -2{,}5$ ; $B = \frac{2}{3} = 0{,}666\ldots$ ; $C = -\sqrt{4} = -2$ ; $D = 0{,}6$ ; $E = -1{,}5$ ; $F = 1{,}75$.
- a) Les négatifs d'abord, du plus loin de 0 au plus proche : $-2{,}5 < -2 < -1{,}5$, soit $A, C, E$. Puis les positifs : $0{,}6 < 0{,}666\ldots < 1{,}75$, soit $D, B, F$. D'où `"ACEDBF"`.
- b) Les entiers strictement entre $-2{,}5$ et $1{,}75$ : $-2, -1, 0, 1$. Il y en a 4.
- c) Seul $C = -2$ est un entier relatif.
- d) $\frac{2}{3}$ n'est pas décimal (son écriture ne s'arrête pas). Les autres le sont : $-2{,}5$, $-2$, $0{,}6$, $-1{,}5$ et $1{,}75$ s'écrivent avec un nombre fini de chiffres.

**Erreurs fréquentes.**
- Placer $D$ après $B$ : $0{,}6$ semble « plus long » que $0{,}66$, mais $0{,}600 < 0{,}666$. Compare avec le même nombre de chiffres.
- Ranger les négatifs comme les positifs ($E$ avant $A$).
- b) Oublier 0, ou compter $-3$, qui est à gauche de $A$.
- c) Oublier que $-\sqrt{4}$ se simplifie en $-2$.

**Variante.** Range $-1{,}2$ ; $-\frac{5}{4}$ ; $\frac{1}{6}$ ; $0{,}16$. *Réponse* : $-\frac{5}{4} < -1{,}2 < 0{,}16 < \frac{1}{6}$ (car $-\frac{5}{4} = -1{,}25$ et $\frac{1}{6} = 0{,}1666\ldots$).

### Ex R1.2 — Calculer avec les priorités et les signes

**Réponses** : a) `8` · b) `3` · c) `-8` · d) `-16` · e) `25` · f) `-15` · g) `-1` · h) `-2`.

**Démarche.**
- a) $4 \times 3 = 12$ d'abord ; puis de gauche à droite : $18 - 12 = 6$, $6 + 2 = 8$.
- b) $-6 + 9 = 3$.
- c) $(-2) \times (-2) \times (-2)$ : trois signes moins, résultat négatif, $-8$.
- d) la puissance avant le signe moins : $-(2^4) = -16$.
- e) de gauche à droite : $20 \div 4 = 5$, puis $5 \times 5 = 25$.
- f) parenthèse : $4 - 7 = -3$ ; puissance : $(-3)^2 = 9$ ; multiplication : $2 \times 9 = 18$ ; soustraction : $3 - 18 = -15$.
- g) $(-12) \div (-3) = 4$, puis $4 - 5 = -1$.
- h) $5 - 11 = -6$, donc $-(-6) = 6$ ; $2 \times (-4) = -8$ ; $6 - 8 = -2$.

**Erreurs fréquentes.**
- a) Calculer $18 - (12 + 2) = 4$ : les soustractions et additions se font de gauche à droite, sans regrouper.
- d) Répondre 16 : sans parenthèses, le carré ne porte que sur 2.
- e) Calculer $20 \div 20 = 1$.
- f) Calculer $(3 - 2) \times 9 = 9$, ou écrire $(-3)^2 = -9$.

**Variante.** Calcule $15 - 3 \times (2 - 6)^2 \div 4$ et $-3^2 + (-3)^2$. *Réponses* : $15 - 3 \times 16 \div 4 = 15 - 12 = 3$ ; et $-9 + 9 = 0$.

### Ex R1.3 — Calcul mental avec la distributivité : 17 × 99, 23 × 101

**Réponses** : a) `1683` · b) `2323` · c) `900` · d) `1100` · e) `320`.

**Démarche.**
- a) $17 \times 99 = 17 \times (100 - 1) = 1700 - 17 = 1683$.
- b) $23 \times 101 = 23 \times (100 + 1) = 2300 + 23 = 2323$.
- c) on factorise par 9 : $9 \times (34 + 66) = 9 \times 100 = 900$.
- d) $25 \times 44 = 25 \times 4 \times 11 = 100 \times 11 = 1100$ (ou $25 \times (40 + 4) = 1000 + 100$).
- e) on factorise par 8 : $8 \times (47 - 7) = 8 \times 40 = 320$.

**Erreurs fréquentes.**
- a) et b) Oublier le second produit : $17 \times 99 \ne 1700$.
- c) et e) Calculer les deux produits séparément : c'est juste, mais on perd l'intérêt (et on se trompe plus).

**Variante.** Calcule de tête $34 \times 98$ et $12 \times 15 + 12 \times 85$. *Réponses* : $3400 - 68 = 3332$ ; $12 \times 100 = 1200$.

### Ex R1.4 — Simplifier des fractions avec le PGCD

**Réponses** : a) `15` · b) `"3/5"` · c) `18` · d) `"14/11"` · e) `"-4/7"` · f) `"13/17"`.

**Démarche.**
- a) $45 = 3^2 \times 5$ et $75 = 3 \times 5^2$ : les diviseurs communs sont 1, 3, 5, 15 ; le plus grand est 15. b) $\frac{45 \div 15}{75 \div 15} = \frac{3}{5}$.
- c) Euclide : $252 = 198 \times 1 + 54$ ; $198 = 54 \times 3 + 36$ ; $54 = 36 \times 1 + 18$ ; $36 = 18 \times 2 + 0$. Le dernier reste non nul est 18. d) $\frac{252 \div 18}{198 \div 18} = \frac{14}{11}$.
- e) $\operatorname{PGCD}(56, 98) = 14$ (car $56 = 14 \times 4$ et $98 = 14 \times 7$), donc $\frac{-56}{98} = -\frac{4}{7}$.
- f) Euclide : $1309 = 1001 \times 1 + 308$ ; $1001 = 308 \times 3 + 77$ ; $308 = 77 \times 4 + 0$. Le PGCD est 77, et $\frac{1001 \div 77}{1309 \div 77} = \frac{13}{17}$.

**Erreurs fréquentes.**
- Simplifier en plusieurs fois et s'arrêter trop tôt : $\frac{45}{75} = \frac{9}{15}$ (par 5), qui se simplifie encore par 3. `wbm.check` dit alors que la valeur est juste mais pas irréductible.
- c) S'arrêter à 36, l'avant-dernier reste : le PGCD est le dernier reste **non nul**.
- e) Perdre le signe moins.

**Variante.** Trouve $\operatorname{PGCD}(391, 323)$ par Euclide, et simplifie $\frac{323}{391}$. *Réponses* : $391 = 323 + 68$, $323 = 4 \times 68 + 51$, $68 = 51 + 17$, $51 = 3 \times 17$ : le PGCD est 17, et $\frac{323}{391} = \frac{19}{23}$.

### Ex R1.5 — Additionner, multiplier et diviser des fractions

**Réponses** : a) `"17/30"` · b) `"-1/24"` · c) `"10/9"` · d) `"3/2"` · e) `"5/3"` · f) `90`.

**Démarche.**
- a) Dénominateur commun 30 : $\frac{9}{30} + \frac{8}{30} = \frac{17}{30}$, irréductible (17 est premier).
- b) Dénominateur commun 24 : $\frac{14}{24} - \frac{15}{24} = -\frac{1}{24}$.
- c) On simplifie avant de multiplier : $\frac{14}{21} = \frac{2}{3}$ et $\frac{25}{15} = \frac{5}{3}$, donc $\frac{2 \times 5}{3 \times 3} = \frac{10}{9}$.
- d) $\frac{7}{9} \times \frac{27}{14} = \frac{7 \times 27}{9 \times 14} = \frac{1 \times 3}{1 \times 2} = \frac{3}{2}$ (on simplifie 7 avec 14, et 27 avec 9).
- e) De l'intérieur vers l'extérieur : $1 + \frac{1}{2} = \frac{3}{2}$ ; $\frac{1}{3/2} = \frac{2}{3}$ ; $1 + \frac{2}{3} = \frac{5}{3}$.
- f) $\frac{3}{8} \times 240 = 3 \times 30 = 90$.

**Erreurs fréquentes.**
- a) Additionner « en haut et en bas » : $\frac{7}{25}$.
- b) Oublier le signe : $\frac{14}{24} - \frac{15}{24}$ est négatif.
- c) Multiplier d'abord ($\frac{350}{315}$), puis mal simplifier.
- d) Multiplier par $\frac{14}{27}$ au lieu de son inverse.
- e) Écrire $\frac{1}{3/2} = \frac{3}{2}$ : diviser 1 par une fraction donne son **inverse**.

**Variante.** Calcule $\frac{5}{6} - \frac{7}{9}$ et $\frac{9}{16} \div \frac{3}{4}$. *Réponses* : $\frac{15}{18} - \frac{14}{18} = \frac{1}{18}$ ; $\frac{9}{16} \times \frac{4}{3} = \frac{3}{4}$.

### Ex R1.6 — Comparer des fractions

**Réponses** : a) `"11/14"` · b) `"RQP"` · c) `"5/12"` · d) `False`.

**Démarche.**
- a) Produits en croix : $7 \times 14 = 98$ et $11 \times 9 = 99$. Comme $98 < 99$, $\frac{7}{9} < \frac{11}{14}$ (de justesse : $0{,}777\ldots$ contre $0{,}785\ldots$).
- b) Dénominateur commun 24 : $P = \frac{16}{24}$, $Q = \frac{15}{24}$, $R = \frac{14}{24}$. Dans l'ordre croissant : $R, Q, P$.
- c) $\frac{1}{3} = \frac{4}{12}$ et $\frac{1}{2} = \frac{6}{12}$ ; strictement entre les deux, avec le dénominateur 12 : seulement $\frac{5}{12}$.
- d) $13 \times 3 = 39 < 40 = 40 \times 1$, donc $\frac{13}{40} < \frac{1}{3}$ : c'est faux. (En décimal : $0{,}325 < 0{,}333\ldots$)

**Erreurs fréquentes.**
- Comparer les numérateurs seuls, ou les dénominateurs seuls ($\frac{11}{14}$ « parce que 11 > 7 » : bonne réponse, mauvaise raison).
- c) Répondre $\frac{4}{12}$ ou $\frac{6}{12}$ : « strictement » exclut les bornes.

**Variante.** Lequel est le plus grand, $\frac{8}{11}$ ou $\frac{13}{18}$ ? *Réponse* : $\frac{8}{11}$, car $8 \times 18 = 144 > 143 = 13 \times 11$.

### Ex R1.7 — Appliquer les règles des puissances

**Réponses** : a) `7` · b) `4` · c) `"1/5"` · d) `1000000` · e) `"27/8"` · f) `-1`.

**Démarche.**
- a) $7^{5 + (-2) - 2} = 7^1 = 7$.
- b) $(2^3)^2 = 2^6$, puis $2^{6 - 4} = 2^2 = 4$.
- c) $5^2 \times 5 = 5^3$ (car $5 = 5^1$), puis $5^{3 - 4} = 5^{-1} = \frac{1}{5}$.
- d) $4^3 \times 25^3 = (4 \times 25)^3 = 100^3 = 1\,000\,000$.
- e) $\frac{3^3}{2^3} = \frac{27}{8}$.
- f) L'exposant 2027 est impair, donc $(-1)^{2027} = -1$.

**Erreurs fréquentes.**
- a) Oublier le signe de $-2$ : $7^{5 + 2 - 2} = 7^5$.
- b) Additionner les exposants de $(2^3)^2$ ($2^5$).
- c) Oublier que $5$ seul vaut $5^1$.
- d) Écrire $(4 \times 25)^{3+3}$ : l'exposant reste 3.
- e) N'élever au cube que le numérateur.

**Variante.** Calcule $\frac{3^4 \times 3^{-1}}{3^5}$ et $2^3 \times 5^3$. *Réponses* : $3^{-2} = \frac{1}{9}$ ; $10^3 = 1000$.

### Ex R1.8 — Puissances négatives et puissances de 10

**Réponses** : a) `"1/16"` · b) `9` · c) `0.00001` · d) `[4, -6]` · e) `12` · f) `8` · g) `6`.

**Démarche.**
- a) $4^{-2} = \frac{1}{4^2} = \frac{1}{16}$.
- b) Un exposant négatif retourne la fraction : $\left(\frac{1}{3}\right)^{-2} = 3^2 = 9$.
- c) $10^{-2 + (-3)} = 10^{-5} = 0{,}000\,01$.
- d) $(2 \times 10^{-3})^2 = 2^2 \times (10^{-3})^2 = 4 \times 10^{-6}$.
- e) $10^{9 - (-3)} = 10^{12}$.
- f) $0{,}5 = \frac{1}{2}$, donc $0{,}5^{-3} = 2^3 = 8$.
- g) $\frac{10^{-3}}{10^{-9}} = 10^{-3 + 9} = 10^6$ : un million de nanosecondes dans une milliseconde.

**Erreurs fréquentes.**
- a) et f) Rendre le nombre négatif ($-16$, $-8$) : l'exposant négatif veut dire « inverse ».
- c) Multiplier les exposants ($10^6$ ou $10^{-6}$).
- d) Oublier d'élever 2 au carré, ou écrire $(10^{-3})^2 = 10^{-5}$.
- g) Diviser dans le mauvais sens ($10^{-6}$).

**Variante.** Calcule $\left(\frac{2}{3}\right)^{-3}$ et $10^{-4} \times 10^{7}$. *Réponses* : $\frac{27}{8}$ ; $10^3$.

### Ex R1.9 — Simplifier des racines carrées

**Réponses** : a) `10` · b) `5` · c) `6` · d) `7` · e) `0.7` · f) `3` · g) `9`.

**Démarche.**
- a) $\sqrt{200} = \sqrt{100 \times 2} = 10\sqrt{2}$.
- b) $\sqrt{75} = \sqrt{25 \times 3} = 5\sqrt{3}$.
- c) $\sqrt{12} \times \sqrt{3} = \sqrt{36} = 6$.
- d) $\frac{\sqrt{98}}{\sqrt{2}} = \sqrt{49} = 7$.
- e) $0{,}7^2 = 0{,}49$, et $0{,}7 \ge 0$, donc $\sqrt{0{,}49} = 0{,}7$.
- f) $\sqrt{20} = 2\sqrt{5}$ et $\sqrt{45} = 3\sqrt{5}$, donc $3 \times 2\sqrt{5} - 3\sqrt{5} = 6\sqrt{5} - 3\sqrt{5} = 3\sqrt{5}$.
- g) $(-9)^2 = 81$ et $\sqrt{81} = 9$.

**Erreurs fréquentes.**
- a) à d) Oublier de prendre la racine du carré parfait sorti (répondre 100, 25, 36, 49).
- e) Répondre $0{,}07$ : $0{,}07^2 = 0{,}0049$. Vérifie toujours en élevant au carré.
- g) Répondre $-9$ : une racine carrée n'est jamais négative.

**Variante.** Simplifie $\sqrt{180}$ et calcule $\sqrt{8} \times \sqrt{18}$. *Réponses* : $6\sqrt{5}$ ; $\sqrt{144} = 12$.

### Ex R1.10 — Écrire en notation scientifique et arrondir

**Réponses** : a) `[7.25, 7]` · b) `[9.06, -5]` · c) `310000` · d) `0.0078` · e) `-4` · f) `[7, -8]`.

**Démarche.**
- a) La virgule recule de 7 rangs : $7{,}25 \times 10^7$.
- b) La virgule avance de 5 rangs jusqu'au 9 : $9{,}06 \times 10^{-5}$.
- c) Deux chiffres significatifs : 3 et 1 ; le suivant est 4, on ne monte pas : $310\,000$.
- d) Les chiffres significatifs commencent au 7 : 7, 8, puis 4 ; on ne monte pas : $0{,}0078$.
- e) $0{,}000\,3 = 3 \times 10^{-4}$, et $3 < 3{,}16$ : l'ordre de grandeur est $10^{-4}$.
- f) $\frac{8{,}4}{1{,}2} = 7$ et $\frac{10^{-3}}{10^{5}} = 10^{-8}$ : $7 \times 10^{-8}$.

**Erreurs fréquentes.**
- a) Écrire $72{,}5 \times 10^6$ : juste en valeur, mais la mantisse doit être entre 1 et 10.
- b) Un exposant positif pour un nombre plus petit que 1.
- c) Répondre 31 : l'arrondi garde la taille du nombre, les zéros tiennent la place des unités.
- d) Arrondir en deux fois ($0{,}00785$ puis $0{,}0079$) : on arrondit une seule fois, depuis la valeur complète.
- f) Ajouter les exposants au lieu de les soustraire ($10^{2}$).

**Variante.** Écris $0{,}000\,004\,07$ en notation scientifique, arrondis $9\,876$ à deux chiffres significatifs, et donne l'ordre de grandeur de $23\,000$. *Réponses* : $4{,}07 \times 10^{-6}$ ; $9\,900$ ; $10^4$ (car $2{,}3 < 3{,}16$).

### Ex R1.11 — Partie entière, arrondi au plus proche, arrondi supérieur

**Réponses** : a) `4` · b) `-5` · c) `0` · d) `7` · e) `-1` · f) `9` · g) `-4`.

**Démarche.**
- a) Le plus grand entier inférieur ou égal à 4,6 : 4.
- b) Pour $-4{,}6$, l'entier juste en dessous (à gauche sur la droite) est $-5$.
- c) Pour $-0{,}4$, l'entier juste au-dessus (à droite) est 0.
- d) 7 est un entier : c'est son propre plafond.
- e) $-1{,}49$ est plus près de $-1$ que de $-2$ (le chiffre des dixièmes, 4, est inférieur à 5).
- f) $\frac{100}{12} \approx 8{,}33$ ; 8 boîtes ne rangent que 96 œufs : il en faut $\lceil 8{,}33 \rceil = 9$.
- g) `int` coupe vers 0 : `int(-4.6)` vaut $-4$, alors que $\lfloor -4{,}6 \rfloor = -5$.

**Erreurs fréquentes.**
- b) et c) Traiter les négatifs comme les positifs ($-4$ et $-1$).
- f) Arrondir au plus proche (8) : on ne laisse pas d'œufs sans boîte.
- g) Confondre `int` avec un plancher.

**Variante.** Calcule $\lfloor -0{,}01 \rfloor$, $\lceil 2{,}0001 \rceil$, et le nombre de cars de 50 places pour 230 personnes. *Réponses* : $-1$ ; 3 ; $\lceil 4{,}6 \rceil = 5$.

### Ex R1.12 — Évolutions successives et évolution réciproque

**Réponses** : a) `72` · b) `-20` · c) `32` · d) `-27.1` · e) `-37.5` · f) `42.86`.

**Démarche.**
- a) $64 \times 1{,}125 = 72$ €.
- b) $\frac{1000 - 1250}{1250} = \frac{-250}{1250} = -0{,}2$, soit −20 %.
- c) $1{,}1 \times 1{,}2 = 1{,}32$, soit +32 %.
- d) $0{,}9^3 = 0{,}729$, soit $0{,}729 - 1 = -0{,}271$ : −27,1 %.
- e) $\frac{1}{1{,}6} = 0{,}625$, soit $0{,}625 - 1 = -0{,}375$ : −37,5 %.
- f) $\frac{1}{0{,}7} \approx 1{,}428\,57$, soit +42,86 %.

**Erreurs fréquentes.**
- a) Ajouter 12,5 € au lieu de 12,5 % du prix.
- b) Diviser par la valeur d'arrivée ($\frac{-250}{1000} = -25\,\%$).
- c) et d) Additionner les taux (+30 %, −30 %).
- e) et f) Prendre l'opposé du taux (−60 %, +30 %) au lieu de l'inverse du coefficient.

**Variante.** Deux baisses successives de 20 % : quel taux global, et quelle hausse ramène au départ ? *Réponses* : $0{,}8^2 = 0{,}64$, soit −36 % ; puis $\frac{1}{0{,}64} = 1{,}5625$, soit +56,25 %.

### Ex R1.13 — Règle de trois et proportionnalité

**Réponses** : a) `12` · b) `15` · c) `750` · d) `90` · e) `False`.

**Démarche.**
- a) 1 kg coûte $7{,}20 \div 3 = 2{,}40$ €, donc 5 kg coûtent $12$ €.
- b) Le coefficient vaut $\frac{10}{4} = 2{,}5$, donc $y = 6 \times 2{,}5 = 15$.
- c) $\frac{300}{4} \times 10 = 750$ g.
- d) 1 h 30 = 1,5 h, donc $\frac{135}{1{,}5} = 90$ km/h.
- e) Les quotients $\frac{5}{2} = 2{,}5$, $\frac{15}{6} = 2{,}5$, mais $\frac{21}{9} \approx 2{,}33$ : ils ne sont pas tous égaux.

**Erreurs fréquentes.**
- d) Écrire 1 h 30 = 1,3 h : une demi-heure, c'est 0,5 h.
- e) Ne vérifier que les deux premières colonnes.

**Variante.** Une voiture consomme 8 L aux 100 km : combien pour 340 km ? *Réponse* : $8 \times 3{,}4 = 27{,}2$ L.

### Ex R1.14 — Moyenne pondérée : la note finale et la somme pondérée d'un neurone

**Réponses** : a) `13.625` · b) `15.5` · c) `4` · d) `22.5`.

**Démarche.**
- a) $\frac{13 \times 4 + 9 \times 1 + 16 \times 3}{4 + 1 + 3} = \frac{52 + 9 + 48}{8} = \frac{109}{8} = 13{,}625$.
- b) Avec la note $x$ de coefficient 2 : $\frac{109 + 2x}{10} = 14$, donc $109 + 2x = 140$, $2x = 31$, $x = 15{,}5$.
- c) $1{,}5 \times 2 + (-2) \times 0{,}5 + 0{,}5 \times 6 + (-1) = 3 - 1 + 3 - 1 = 4$.
- d) Sur une distance $d$ : la montée dure $\frac{d}{15}$, la descente $\frac{d}{45}$, en tout $\frac{3d + d}{45} = \frac{4d}{45}$ ; la vitesse moyenne vaut $\frac{2d}{4d/45} = \frac{90}{4} = 22{,}5$ km/h. C'est la moyenne harmonique de 15 et 45.

**Erreurs fréquentes.**
- a) Faire la moyenne simple des trois notes (12,67).
- b) Compter le coefficient 2 dans la somme des notes mais pas dans la somme des coefficients (on trouve 17).
- c) Oublier le biais (5), ou le signe du poids négatif (6).
- d) Faire la moyenne des vitesses (30) : la cycliste passe trois fois plus de temps à monter.

**Variante.** Les notes 10 (coefficient 1) et 15 (coefficient 4) ; et un neurone avec $\mathbf{w} = (2 \;;\; -1)$, $\mathbf{x} = (1 \;;\; 3)$, $b = 0{,}5$. *Réponses* : $\frac{10 + 60}{5} = 14$ ; $z = 2 - 3 + 0{,}5 = -0{,}5$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R1.15 — Pourquoi a⁰ = 1 et a⁻ⁿ = 1/aⁿ : prolonger les règles des puissances

**Démonstration.**
1. Avec $m = 1$ et $p = 0$, la règle donne $a^1 \times a^0 = a^{1 + 0} = a^1$, c'est-à-dire $a \times a^0 = a$. Comme $a \ne 0$, on peut diviser les deux membres par $a$ : $a^0 = 1$. Aucune autre valeur ne convient.
2. Avec $m = n$ et $p = -n$ : $a^n \times a^{-n} = a^{n + (-n)} = a^0 = 1$ (d'après 1). Comme $a^n \ne 0$ (un produit de facteurs non nuls n'est pas nul), on divise par $a^n$ : $a^{-n} = \frac{1}{a^n}$.
3. Pour $m = 2$ et $p = 5$ : $\frac{a^2}{a^5} = \frac{a \times a}{a \times a \times a \times a \times a} = \frac{1}{a^3}$ (on simplifie deux facteurs $a$), et $a^{2 - 5} = a^{-3} = \frac{1}{a^3}$ : les deux côtés coïncident. En général, pour $m < p$ : on simplifie les $m$ facteurs du numérateur avec $m$ des $p$ facteurs du dénominateur ; il reste $\frac{1}{a^{p - m}}$, qui vaut bien $a^{-(p - m)} = a^{m - p}$ par la définition de 2.
4. On a divisé par $a$ (en 1) et par $a^n$ (en 2) : il fallait que $a \ne 0$. Et $0^{-1}$ vaudrait $\frac{1}{0}$, qui n'existe pas. (Pour $0^0$, il n'y a pas de valeur imposée par les règles ; on convient souvent que $0^0 = 1$, et Python aussi : `0 ** 0` vaut 1.)

**Grille de relecture.** Une démonstration correcte :
- part de la règle $a^m \times a^p = a^{m+p}$ **supposée** vraie, et l'applique avec des valeurs choisies (sans utiliser ce qu'on veut démontrer) ;
- **dit** pourquoi on a le droit de diviser ($a \ne 0$, puis $a^n \ne 0$) ;
- conclut que la valeur est **imposée** (« ne peut valoir que »), pas seulement qu'elle « marche » ;
- en 3, vérifie l'exemple **puis** le cas général, avec un argument de simplification de facteurs.

**Erreurs fréquentes.** Démontrer $a^0 = 1$ en écrivant $a^0 = a^{1-1} = \frac{a}{a}$ : c'est juste, mais cela utilise la règle du quotient, qu'il faudrait elle aussi justifier pour des exposants négatifs ou nuls. Oublier de dire que $a \ne 0$.

**Variante.** Avec la même méthode, montre que $(a^{-1})^{-1} = a$. *Réponse* : $a^{-1} = \frac{1}{a}$, et $(a^{-1})^{-1} = \frac{1}{1/a} = a$ ; ou par la règle $(a^m)^n = a^{mn}$, $a^{(-1)(-1)} = a^1$.

### Ex R1.16 — Pourquoi on n'additionne pas les dénominateurs

**Démonstration.**
1. Contre-exemple : $\frac{1}{2} + \frac{1}{2} = 1$, alors que la « règle » donnerait $\frac{1 + 1}{2 + 2} = \frac{2}{4} = \frac{1}{2}$. Un seul contre-exemple suffit à montrer qu'une égalité « pour tous les nombres » est fausse.
2. Posons $S = \frac{a}{d} + \frac{c}{d}$. Par définition, $d \times \frac{a}{d} = a$ et $d \times \frac{c}{d} = c$. Par distributivité, $d \times S = d \times \frac{a}{d} + d \times \frac{c}{d} = a + c$. Donc $S$ est le nombre qui, multiplié par $d$, donne $a + c$ : par définition, $S = \frac{a + c}{d}$.
3. On met les deux fractions au même dénominateur $bd$ : $\frac{a}{b} = \frac{ad}{bd}$ et $\frac{c}{d} = \frac{cb}{bd}$ (on multiplie numérateur et dénominateur par le même nombre non nul). D'après 2, leur somme vaut $\frac{ad + cb}{bd}$.
4. On suppose $\frac{a}{b} < \frac{c}{d}$, avec des nombres positifs ; en multipliant par $bd > 0$, cela s'écrit $ad < bc$. Montrons $\frac{a}{b} < \frac{a + c}{b + d}$ : en multipliant par $b(b + d) > 0$, c'est $a(b + d) < b(a + c)$, soit $ab + ad < ab + bc$, soit $ad < bc$ : vrai. De même, $\frac{a + c}{b + d} < \frac{c}{d}$ revient à $d(a + c) < c(b + d)$, soit $ad < bc$ : vrai. La médiante est donc entre les deux fractions. Pour le joueur, $\frac{3 + 7}{5 + 10} = \frac{10}{15}$ est son taux de réussite **sur le week-end** (10 tirs réussis sur 15), entre 60 % et 70 % : c'est un vrai nombre, mais pas la somme des deux taux.

**Grille de relecture.**
- 1 donne des valeurs **précises** et calcule les deux côtés.
- 2 part de la définition (« le nombre qui, multiplié par $d$, donne… ») et utilise la distributivité ; sans définition, il n'y a pas de démonstration.
- 3 justifie la mise au même dénominateur, puis **réutilise** 2.
- 4 transforme chaque inégalité en une inégalité équivalente en multipliant par un nombre **positif** (sinon le sens changerait), et retombe sur l'hypothèse $ad < bc$.

**Variante.** Démontre de la même façon que $\frac{a}{b} \times \frac{c}{d} = \frac{ac}{bd}$. *Réponse* : $bd \times \left(\frac{a}{b} \times \frac{c}{d}\right) = \left(b \times \frac{a}{b}\right) \times \left(d \times \frac{c}{d}\right) = ac$, donc le produit est le nombre qui, multiplié par $bd$, donne $ac$ : c'est $\frac{ac}{bd}$.

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Ponts, estimations, explications

### Ex R1.17 — Combien de paramètres, combien d'octets ? Un réseau en notation scientifique

**Réponses** : a) `60200` · b) `70454` · c) `5` · d) `[2.8, 5]` · e) `260`.

**Démarche.**
- a) Chacun des 200 neurones a 300 poids et 1 biais : $200 \times (300 + 1) = 60\,200$.
- b) Deuxième couche : $50 \times (200 + 1) = 10\,050$ ; sortie : $4 \times (50 + 1) = 204$. Total : $60\,200 + 10\,050 + 204 = 70\,454$.
- c) $70\,454 \approx 7{,}05 \times 10^4$, et $7{,}05 \ge 3{,}16$ : l'ordre de grandeur est $10^5$.
- d) $70\,454 \times 4 = 281\,816$ octets $\approx 2{,}8 \times 10^5$ octets, soit environ 280 ko.
- e) $1{,}3 \times 10^{11} \times 2 = 2{,}6 \times 10^{11}$ octets $= 260 \times 10^9$ octets $= 260$ Go.

**Erreurs fréquentes.** Oublier les biais ; ne compter que la première couche ; oublier que la couche suivante reçoit les **sorties** de la précédente (200, pas 300) ; en e), confondre bits et octets (16 bits font 2 octets).

**Ce que ça montre.** Presque tous les paramètres sont dans la première couche, celle qui relie le plus de neurones. Et un vrai modèle de langage est un million de fois plus gros que ce petit réseau : il ne tient pas dans la mémoire d'un ordinateur portable ordinaire.

**Variante.** Un réseau $100 \to 10 \to 1$ : combien de paramètres ? *Réponse* : $10 \times 101 + 1 \times 11 = 1\,021$.

### Ex R1.18 — Fermi : combien de mots lis-tu dans une vie ?

**Une solution modèle** (tes nombres peuvent différer : seule la démarche et l'ordre de grandeur comptent).
1. Facteurs : mots lus par minute de lecture ; minutes de lecture par jour (livres, écrans, messages, panneaux) ; jours par an ; années de lecture.
2. Estimations : on lit environ 200 à 300 mots par minute (prenons $2{,}5 \times 10^2$) ; une à deux heures de lecture par jour, tout compris (prenons 90 min, soit $9 \times 10^1$) ; 365 jours ($3{,}65 \times 10^2$) ; de 6 à 80 ans, environ 75 ans ($7{,}5 \times 10^1$).
3. Produit : mantisses $2{,}5 \times 9 \times 3{,}65 \times 7{,}5 \approx 22{,}5 \times 3{,}65 \times 7{,}5 \approx 82 \times 7{,}5 \approx 600$ ; puissances $10^{2 + 1 + 2 + 1} = 10^6$. Résultat : $6 \times 10^2 \times 10^6 = 6 \times 10^8$ mots environ.
4. $\frac{6 \times 10^8}{8 \times 10^5} \approx 750$ Bibles dans une vie, soit une dizaine par an. Plausible pour un lecteur moyen d'aujourd'hui, si l'on compte tout ce qu'il lit sur écran.
5. Le temps de lecture par jour est le plus incertain (il varie d'un facteur 5 d'une personne à l'autre). S'il double, le résultat double : $1{,}2 \times 10^9$. L'ordre de grandeur reste entre $10^8$ et $10^9$.

**Ce qu'on attend.** Des facteurs clairs, une estimation justifiée pour chacun, un produit en notation scientifique, un résultat à un chiffre significatif, et un jugement de vraisemblance. Une réponse entre $10^8$ et $10^9$ est raisonnable.

### Ex R1.19 — Fermi : la place que prend un dataset de photos

**Une solution modèle.**
1. Si un utilisateur actif poste en moyenne 2 photos par semaine : $2 \times 10^6 \times 2 \times 52 \approx 2 \times 10^8$ photos par an.
2. Une photo de téléphone compressée pèse environ 3 Mo, soit $3 \times 10^6$ octets. Total : $2 \times 10^8 \times 3 \times 10^6 = 6 \times 10^{14}$ octets, soit 600 To.
3. Il faudrait environ 600 disques de 1 To ; un serveur de 100 To ne suffit pas (il en faudrait six).
4. Une photo réduite pèse $224 \times 224 \times 3 \approx 1{,}5 \times 10^5$ octets (150 ko). Le dataset réduit : $2 \times 10^8 \times 1{,}5 \times 10^5 = 3 \times 10^{13}$ octets, soit 30 To : il tient sur le serveur.

**Ce qu'on attend.** Une hypothèse explicite sur le nombre de photos (entre 0,5 et 10 par semaine donne entre $5 \times 10^7$ et $10^9$ photos), une taille par photo justifiée (de 1 à 5 Mo), et la conclusion : le dataset brut se compte en centaines de To, le dataset réduit en dizaines. Réduire les images avant l'entraînement est exactement ce que font les vrais pipelines.

### Ex R1.20 — Expliquer pourquoi +10 % puis −10 % ne ramène pas au départ

**Une réponse modèle** (cinq lignes).

> Chaque pourcentage se calcule sur le loyer **du moment**, pas sur le loyer de départ. Avec un loyer de 1 000 €, la hausse de 10 % ajoute 100 € : 1 100 €. La baisse de 10 % retire 10 % de 1 100 €, soit 110 € : tu paies 990 €, 1 % de moins qu'au départ. Le propriétaire ne s'est pas trompé : la baisse porte sur un loyer plus élevé, donc elle retire plus que la hausse n'avait ajouté. Pour revenir à 1 000 €, il aurait fallu une baisse d'environ 9,1 % (100 € sur 1 100 €).

**Ce qu'on attend.** L'idée clé (chaque pourcentage porte sur la valeur du moment), un exemple chiffré juste, le résultat (−1 %), et la baisse qui ramène au départ ($\frac{1}{1{,}1} \approx 0{,}909$, soit −9,1 %).

<a id="notebook"></a>

## Notebook

### Ex R1.21 — PGCD par l'algorithme d'Euclide et fraction irréductible · `gcd`, `simplify_fraction`

**Réponses** : `gcd(2310, 1092)` vaut `42` ; `simplify_fraction(-1092, 2310)` vaut `(-26, 55)`.

**Démarche.** `gcd` : on passe aux valeurs sans signe, puis tant que `b != 0`, on remplace `(a, b)` par `(b, a % b)` ; à la fin, `a` contient le dernier reste non nul. `simplify_fraction` : on vérifie que le dénominateur n'est pas nul (`raise ValueError(...)`), on divise numérateur et dénominateur par le PGCD avec `//`, puis, si le dénominateur est négatif, on change les deux signes. Le code complet est dans `05_solutions.ipynb`.

**Erreurs fréquentes.**
- Renvoyer `b` à la fin de la boucle : il vaut 0.
- Diviser avec `/` : on obtient des flottants (`-26.0`), et les tests demandent des entiers.
- Oublier les signes : `gcd(-9, 6)` doit valoir 3, et `simplify_fraction(84, -36)` doit valoir `(-7, 3)`.
- Chercher le PGCD en essayant tous les diviseurs : juste, mais beaucoup trop lent sur de grands nombres (un test le vérifie).

**Variante.** Que valent `gcd(-48, 180)` et `simplify_fraction(48, -180)` ? *Réponses* : `12` ; `(-4, 15)`.

### Ex R1.22 — Additionner deux fractions sans passer par les décimaux · `add_fractions`

**Réponse** : `add_fractions((7, 15), (-3, 10))` vaut `(1, 6)`.

**Démarche.** $\frac{7}{15} + \frac{-3}{10} = \frac{7 \times 10 + (-3) \times 15}{15 \times 10} = \frac{25}{150}$, que `simplify_fraction` réduit en $\frac{1}{6}$. En code : `return simplify_fraction(p1 * q2 + p2 * q1, q1 * q2)`, après avoir vérifié les dénominateurs.

**Erreurs fréquentes.** Renvoyer `(25, 150)` sans simplifier ; passer par `p1 / q1 + p2 / q2` (un flottant, et un test sur de grands dénominateurs échoue) ; réécrire le PGCD au lieu de réutiliser `simplify_fraction`.

**Variante.** `add_fractions((2, 9), (5, 6))` ? *Réponse* : $\frac{4}{18} + \frac{15}{18} = \frac{19}{18}$, donc `(19, 18)`.

### Ex R1.25 — Calculer exactement avec `fractions.Fraction`

**Réponses** : a) `Fraction(7381, 2520)` · b) `Fraction(1, 10)` · c) `False`.

**Démarche.** a) une boucle `total += Fraction(1, k)` pour `k` de 1 à 10. b) `product *= 1 - Fraction(1, k)` pour `k` de 2 à 10 : le produit se télescope, $\frac{1}{2} \times \frac{2}{3} \times \dots \times \frac{9}{10} = \frac{1}{10}$. c) en flottants, chaque `1 - 1/k` est arrondi, et le produit vaut `0.10000000000000002` : `== 0.1` répond `False`.

**Erreurs fréquentes.** `range(1, 10)` s'arrête à 9 (il manque $\frac{1}{10}$) ; `Fraction(1/k)` convertit un flottant déjà arrondi (écris `Fraction(1, k)`).

**Variante.** Calcule exactement $\frac{1}{2} + \frac{1}{4} + \dots + \frac{1}{1024}$. *Réponse* : `Fraction(1023, 1024)`.

### Ex R1.28 — Chasse à l'erreur : cinq calculs de fractions et de puissances

**Réponses** : a) `"ace"` · b) `4` · c) `"22/15"`.

**Démarche.**
- a est faux : on a additionné les numérateurs et les dénominateurs ; $\frac{10}{15} + \frac{12}{15} = \frac{22}{15}$.
- b est juste : $\frac{3 \times 8}{4 \times 9} = \frac{24}{36} = \frac{2}{3}$.
- c est faux : on additionne les exposants en gardant la base, $5^5$, et non $25^5$.
- d est juste : l'exposant $-1$ retourne la fraction.
- e est faux : il faut multiplier par l'inverse, $\frac{10}{3} \times \frac{6}{5} = \frac{60}{15} = 4$ ; le camarade a multiplié par $\frac{5}{6}$.

**Erreurs fréquentes.** Croire b faux parce que $\frac{24}{36}$ « n'est pas $\frac{2}{3}$ » : simplifie par 12.

**Variante.** Juste ou faux : $\left(\frac{3}{4}\right)^2 = \frac{9}{16}$ ; $2^{-2} \times 2^5 = 2^3$ ; $\frac{1}{2} + \frac{1}{3} = \frac{2}{5}$ ? *Réponses* : juste, juste, faux ($\frac{5}{6}$).

### Ex R1.29 — Chasse à l'erreur : `-3**2` et les parenthèses

**Réponses** : a) `[1, 4, 7]` · b) `line4(3)` vaut `0.5`.

**Démarche.**
- Ligne 1, fausse : `-x**2` vaut $-(x^2)$ ; pour $(-x)^2$, il faut `(-x)**2`. Avec $x = 3$ : $-9$ au lieu de 9.
- Ligne 4, fausse : `x / 2 * 3` se calcule de gauche à droite, $\frac{x}{2} \times 3 = \frac{3x}{2}$ ; pour $\frac{x}{6}$, il faut `x / (2 * 3)` ou `x / 6`.
- Ligne 7, fausse : `1 / 2 + x` vaut $\frac{1}{2} + x$ ; pour $\frac{1}{2 + x}$, il faut `1 / (2 + x)`.
- Les lignes 2, 3, 5 et 6 sont justes.

**Erreurs fréquentes.** Croire la ligne 2 fausse : `(x + 1) / 2 * x` vaut $\frac{x + 1}{2} \times x$, qui est bien $\frac{(x+1)x}{2}$.

**Variante.** Que calcule `1 / 2 * x`, et comment écrire $\frac{1}{2x}$ ? *Réponse* : $\frac{x}{2}$ ; `1 / (2 * x)`.

### Ex R1.23 — La notation scientifique à n chiffres significatifs · `scientific_notation`

**Réponses** : `scientific_notation(299792458, digits=4)` vaut `(2.998, 8)` ; `scientific_notation(-0.0009996)` vaut `(-1.0, -3)`.

**Démarche.** L'exposant : `math.floor(math.log10(abs(x)))` ; la mantisse : `x / 10**k` (ou `x * 10**(-k)` pour un exposant négatif), corrigée d'un rang si elle n'est pas entre 1 et 10 (cela arrive tout près d'une puissance de 10, à cause des arrondis de `log10`). Puis `round(m, digits - 1)`. Enfin, le piège : $-0{,}0009996 = -9{,}996 \times 10^{-4}$, dont la mantisse arrondie à trois chiffres donne $-10{,}0$ ; on écrit alors $-1{,}00 \times 10^{-3}$.

**Erreurs fréquentes.** Oublier le cas `x == 0` (`log10(0)` lève une erreur) ; oublier `abs` pour un nombre négatif ; oublier le débordement de l'arrondi (on renvoie `(-10.0, -4)`).

**Variante.** `scientific_notation(0.0005, digits=1)` ? *Réponse* : `(5.0, -4)`.

### Ex R1.26 — Prédire : arrondir deux fois, est-ce arrondir une fois ?

**Réponses** : a) `4` · b) `3`.

**Démarche.** a) `round(3.46, 1)` donne 3,5 (le chiffre des centièmes, 6, fait monter le dixième) ; puis `round(3.5)` donne 4 (3,5 est pile au milieu, et Python va au pair, 4 ; la règle du papier donne aussi 4). b) `round(3.46)` donne 3, car 3,46 est plus près de 3 que de 4. Arrondir deux fois a éloigné le résultat de la vraie valeur.

**Erreurs fréquentes.** Prédire la même valeur pour a et b : c'est justement ce que l'expérience dément.

**Variante.** Prédis `round(round(7.448, 2), 1)` et `round(7.448, 1)`. *Réponses* : 7,45 puis 7,5 ; mais 7,4 en une seule fois.

### Ex R1.30 — Les ordres de grandeur sur une échelle : de l'atome aux paramètres d'un LLM

**Réponse attendue.** Une figure qui place chaque quantité à l'abscisse de son exposant (de $-10$ pour l'atome à $12$ pour les paramètres du modèle), avec un nom lisible pour chaque point, un titre, un axe nommé et une graduation par puissance de 10 (voir `05_solutions.ipynb`). Lecture : de l'épaisseur d'un cheveu ($7 \times 10^{-5}$, exposant environ $-4{,}2$) aux paramètres ($10^{12}$), il y a environ **16 puissances de 10** : un facteur dix millions de milliards, même si les deux nombres ne mesurent pas la même chose.

**Erreurs fréquentes.** Placer les valeurs elles-mêmes au lieu de leur exposant (tous les points s'écrasent près de zéro, sauf le dernier) ; oublier les noms des points.

### Ex R1.24 — Évolutions successives et moyenne pondérée · `successive_changes`, `weighted_mean`

**Réponses** : `successive_changes([0.3, -0.2, 0.05])` vaut environ `0.092` ; `weighted_mean([11, 17, 8], [2, 3, 5])` vaut `11.3`.

**Démarche.** a) le coefficient global $1{,}3 \times 0{,}8 \times 1{,}05 = 1{,}092$, donc un taux de $+9{,}2\,\%$ : on part de `coefficient = 1.0`, on multiplie par `1 + rate` à chaque tour (après avoir vérifié `rate >= -1`), on renvoie `coefficient - 1`. b) $\frac{22 + 51 + 40}{10} = 11{,}3$, après les trois vérifications de la docstring.

**Erreurs fréquentes.** Additionner les taux (0,15) ; renvoyer le coefficient (1,092) au lieu du taux ; diviser par le nombre de valeurs ; tester seulement `sum(weights) == 0` sans vérifier les poids négatifs.

**Variante.** `successive_changes([-0.5, 1.0])` et `weighted_mean([4, 10], [3, 1])` ? *Réponses* : `0.0` (diviser par deux puis doubler) ; `5.5`.

### Ex R1.27 — Après n hausses de 10 % : tracer et comparer à une hausse de 10n %

**Réponses** : a) `8` · b) `17.45`.

**Démarche.** a) $1{,}1^7 \approx 1{,}95 < 2$ et $1{,}1^8 \approx 2{,}14 \ge 2$ : le prix double pendant la huitième année. b) $1{,}1^{30} \approx 17{,}45$, contre $1 + 0{,}1 \times 30 = 4$ pour les taux additionnés. Les deux courbes se confondent presque pendant les premières années, puis la puissance s'envole.

**Erreurs fréquentes.** a) Répondre 10 (« 10 × 10 % = 100 % ») : c'est la logique des taux additionnés. Ou 7, en lisant mal la boucle.

**Variante.** À 5 % par an, au bout de combien d'années le prix double-t-il ? *Réponse* : 15 ($1{,}05^{14} \approx 1{,}98$, $1{,}05^{15} \approx 2{,}08$).

### Ex R1.31 — Écrire la docstring d'une fonction (format NumPy)

**Une docstring modèle** (en anglais, comme tout le code du dépôt) :

```python
def harmonic_mean(values):
    """Return the harmonic mean of positive numbers: the inverse of the mean of their inverses.

    Parameters
    ----------
    values : sequence of float
        Strictly positive numbers (a speed, a rate...).

    Returns
    -------
    float
        ``n / (1/x1 + ... + 1/xn)``, never larger than the arithmetic mean.

    Raises
    ------
    ValueError
        If ``values`` is empty, or if a value is zero or negative.

    Examples
    --------
    >>> harmonic_mean([90, 60])
    72.0
    >>> harmonic_mean([5, 5, 5])
    5.0
    """
```

**Ce qu'on attend.** Une première ligne qui dit ce que fait la fonction ; les quatre sections avec leur soulignement de tirets ; les deux cas d'erreur du code dans `Raises` ; des exemples dont le résultat est exactement ce que Python affiche (`72.0`, pas `72`).

**Erreurs fréquentes.** Un exemple dont le résultat est mal écrit (`72` au lieu de `72.0`) : `doctest` le signale ; oublier un cas d'erreur ; écrire la docstring après le code au lieu de juste sous la ligne `def`.
