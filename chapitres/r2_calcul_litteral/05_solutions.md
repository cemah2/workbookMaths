# R2 · Calcul littéral et équations — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R2.Q1 — Variables et substitution
1. **Faux** : $(-3)^2 = (-3) \times (-3) = 9$. Sans parenthèses, $-3^2$ vaudrait $-9$ : c'est pour cela qu'on substitue toujours avec des parenthèses.
2. **Faux** : pour $x = 1$, $2x = 2$ et $x^2 = 1$. Ils ne sont égaux que pour $x = 0$ et $x = 2$ : deux expressions égales « pour tout $x$ » doivent l'être partout.
3. **Faux** : $ab = a \times b = 10$. Les lettres côte à côte se multiplient ; ce ne sont pas des chiffres.
4. **Vrai** : $-x^2 = -(x^2) = -1$, et $-1 + (-1) = -2$.
5. **Faux** : $3x$ et $2x^2$ ne sont pas semblables ; la somme reste $2x^2 + 3x$.
6. **Vrai** : c'est la distributivité, $3(x + 2) = 3x + 6$.

### R2.Q2 — Développer ou factoriser ?
1. Factorisation, **juste** : $2x \times 2x - 2x \times 3 = 4x^2 - 6x$.
2. Développement, **juste** : $x^2 + 5x - x - 5 = x^2 + 4x - 5$.
3. Développement, **faux** : $3x(x + 2) = 3x^2 + 6x$ ; le $3x$ multiplie aussi le 2.
4. Factorisation, **fausse** : $x^2 - 25 = (x - 5)(x + 5)$ ; $(x - 5)^2 = x^2 - 10x + 25$.
5. Factorisation, **juste** : 3 est le PGCD de 6 et 9.
6. Développement, **faux** : $-2 \times (-3) = +6$, donc $-2x + 6$.

### R2.Q3 — Identités remarquables : vrai ou faux
1. **Faux** : $(x + 3)^2 = x^2 + 6x + 9$ ; il manque le double produit.
2. **Vrai** : $(a - b)^2$ avec $a = x$, $b = 1$.
3. **Vrai** : $(2x)^2 + 2 \times 2x \times 1 + 1^2$.
4. **Vrai** : une différence de deux carrés.
5. **Vrai** : $3 - x = -(x - 3)$, et un carré efface le signe : $(-u)^2 = u^2$.
6. **Faux** : $(x + 2)(x - 2) = x^2 - 4$. Une **somme** de deux carrés, $x^2 + 4$, ne se factorise pas avec les identités (elle ne s'annule jamais).
7. **Vrai** : $x^2 + 2x + 1 - x^2 = 2x + 1$.

### R2.Q4 — Équations : quelles opérations sont permises ?
1. **Oui** : on peut revenir en arrière en retirant 5.
2. **Non** : toute équation devient $0 = 0$, vraie pour tout $x$ ; on gagne des « solutions » qui n'en sont pas.
3. **Non** : si $x$ peut valoir 0, on divise par 0, et on perd la solution $x = 0$ (fiche §4, l'encadré).
4. **Oui** : $-2$ n'est pas nul ; on revient en arrière en divisant par $-2$.
5. **Non** : $x = 2$ n'a qu'une solution, $x^2 = 4$ en a deux ($-2$ aussi). On gagne des solutions.
6. **Oui** : ajouter ou retirer la même expression aux deux membres garde les solutions.

### R2.Q5 — Inéquations : quand le sens change
1. **Faux** : multiplier par $-1$ retourne le sens, $-2 > -5$.
2. **Vrai** : on divise par $-7$, négatif, le sens change : $x \ge -2$.
3. **Vrai** : on multiplie par $-2$, le sens change : $x < -2$.
4. **Vrai** : on retire 4, le sens ne change pas.
5. **Faux** : $5 - x > 0 \iff -x > -5 \iff x < 5$. Vérifie avec $x = 0$ : $5 > 0$, vrai, et 0 n'est pas supérieur à 5.
6. **Faux** : du côté de l'infini, le crochet est toujours ouvert : $[2 \;;\; +\infty[$.
7. **Faux** : « et » donne l'intersection, $]1 \;;\; 4[$. La réunion écrite contient tous les réels.

### R2.Q6 — Valeur absolue et distance
1. **Vrai** : $|-9| = 9$ ; une valeur absolue n'est jamais négative.
2. **Vrai** : $|3 - 10| = |-7| = 7$, la distance entre 3 et 10.
3. **Vrai** : $4$ et $-4$.
4. **Faux** : c'est la distance entre $x$ et $2$. La distance à $-2$ s'écrit $|x - (-2)| = |x + 2|$.
5. **Vrai**, par définition.
6. **Faux** : avec $a = 1$ et $b = -1$, $|a + b| = 0$ et $|a| + |b| = 2$. (On a seulement $|a + b| \le |a| + |b|$, l'inégalité triangulaire.)
7. **Faux** : $\operatorname{sign}(-2{,}7) = -1$ ; la fonction signe ne rend que $-1$, 0 ou 1.

### R2.Q7 — Une, aucune ou une infinité de solutions ?
1. **Aucune** : $x + y$ ne peut pas valoir 1 et 2 à la fois (deux droites parallèles).
2. **Une seule** : $(1, 0)$ ; les coefficients ne sont pas proportionnels ($D = -2$).
3. **Une infinité** : la seconde équation est la première multipliée par 2, second membre compris.
4. **Aucune** : deux droites de même pente 3, d'ordonnées à l'origine différentes, sont parallèles.
5. **Une seule** : $(2, 3)$.
6. **Non** : deux droites qui ont deux points communs distincts sont la même droite (par deux points passe une seule droite), et elles ont alors une infinité de points communs. Un système linéaire a 0, 1 ou une infinité de solutions, jamais 2.

### R2.Q8 — Quelle équation pour ce problème ?
1. **b** : $x + 7 = 3x$.
2. **b** : une baisse de 25 % multiplie par 0,75 ; la baisse porte sur $p$, donc $p = 40$ €. (c applique une hausse de 25 % à 30 €, ce qui donne 37,50 € : ce n'est pas le prix de départ, car la baisse portait sur $p$, pas sur 30 €.)
3. **a**.
4. **b** : le périmètre vaut $4c$.
5. **b** : Pierre a $x + 5$ ans, donc $x + (x + 5) = 41$.

<a id="rappels"></a>

## 🔁 Rappels

### R2.R1 — Fractions et puissances (R1)
1. $\frac{9}{12} - \frac{10}{12} = -\frac{1}{12}$.
2. $\frac{2}{3} \times \frac{9}{4} = \frac{18}{12} = \frac{3}{2}$.
3. $2^{3 + (-5)} = 2^{-2} = \frac{1}{4}$.
4. $x^3 \times x^4 = x^7$ ; $(2x)^3 = 2^3 x^3 = 8x^3$ (le cube porte sur le 2 aussi).
5. $10^{-2 + 5} = 10^3 = 1000$.

### R2.R2 — Pourcentages et coefficients multiplicateurs (R1)
1. $0{,}85$.
2. $80 \times 1{,}05 = 84$ €.
3. $1{,}2 \times 0{,}8 = 0{,}96$ : une baisse de 4 %.
4. $\frac{40 - 50}{50} = -0{,}2$ : $-20$ %.
5. $p \times 1{,}25 = 100$, donc $p = 80$ € (et non $100 - 25 = 75$ : la hausse portait sur $p$, pas sur 100).

### R2.R3 — Saisir un intervalle et une expression (R0)
1. `"]-oo ; 5]"`.
2. `"]-1 ; 0]"`.
3. `"3*x**2 - x"`, entre guillemets, avec `*` pour le produit et `**` pour la puissance.
4. `"]-oo ; 0[ U ]2 ; +oo["`.
5. L'infini n'est pas un nombre qu'on atteint : il n'appartient jamais à l'intervalle, et le crochet est toujours ouvert de son côté. `wbm.check` le dit dans son message.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R2.1 — Substituer et réduire

**Réponses** : a) `28` · b) `11` · c) `[1, -2, 1]` · d) `[7, 3]` · e) `-3`.

**Démarche.**
- a) $2 \times (-3)^2 - 3 \times (-3) + 1 = 2 \times 9 + 9 + 1 = 28$.
- b) $a - b = 2 - (-1) = 3$, donc $(a - b)^2 = 9$ ; $ab = 2 \times (-1) = -2$ ; $9 - (-2) = 11$.
- c) Termes en $x^2$ : $2x^2 - x^2 = x^2$ ; en $x$ : $5x - 7x = -2x$ ; constantes : $-3 + 4 = 1$. D'où $x^2 - 2x + 1$ (qui vaut d'ailleurs $(x - 1)^2$).
- d) $4xy + 3xy = 7xy$ et $-2x + 5x = 3x$ : $7xy + 3x$. Les termes en $xy$ et en $x$ ne sont pas semblables.
- e) $\frac{1/2 + 1}{1/2 - 1} = \frac{3/2}{-1/2} = \frac{3}{2} \times (-2) = -3$.

**Erreurs fréquentes.**
- a) Écrire $2 \times -3^2 = -18$ : sans parenthèses, la puissance passe avant le signe moins. Ou $-3 \times (-3) = -9$ : moins par moins donne plus.
- b) Calculer $2 - 1 = 1$ au lieu de $2 - (-1) = 3$.
- c) Additionner $2x^2 + x^2$ : le terme $-x^2$ est soustrait.
- e) Oublier que le dénominateur est négatif.

**Variante.** Calcule $3x^2 - 5x + 2$ pour $x = -2$, et réduis $3a - 2b + 5 - a + 4b - 8$. *Réponses* : $12 + 10 + 2 = 24$ ; $2a + 2b - 3$.

### Ex R2.2 — Développer

**Réponses** : a) `[2, -11]` · b) `[3, -1, -10]` · c) `[2, -1, 5, 3]` · d) `[-1, 3, 4]` · e) `[1, 1, -2]`.

**Démarche.**
- a) $6x - 15 - 4x + 4 = 2x - 11$.
- b) $3x^2 + 5x - 6x - 10 = 3x^2 - x - 10$.
- c) Six produits : $2x \times x^2 = 2x^3$, $2x \times (-x) = -2x^2$, $2x \times 3 = 6x$, $1 \times x^2 = x^2$, $1 \times (-x) = -x$, $1 \times 3 = 3$. On réduit : $2x^3 - x^2 + 5x + 3$.
- d) $(x - 4)(x + 1) = x^2 + x - 4x - 4 = x^2 - 3x - 4$, puis le signe moins change **chaque** terme : $-x^2 + 3x + 4$.
- e) $a^2 - ab + 2ab - 2b^2 = a^2 + ab - 2b^2$.

**Vérifier par une valeur test.** Pour b) avec $x = 1$ : $(1 - 2)(3 + 5) = -8$, et $3 - 1 - 10 = -8$. Le test ne prouve pas que le développement est juste, mais un test raté prouverait une erreur.

**Erreurs fréquentes.**
- a) $-4 \times (-1) = -4$ : le moins devant la parenthèse change le signe de **tous** ses termes.
- b) Oublier les deux produits croisés ($3x^2 - 10$).
- c) S'arrêter à quatre produits.
- d) Ne changer que le signe du premier terme.

**Variante.** Développe $(2x - 3)(x + 4)$ et $-2(x + 1)(x - 3)$. *Réponses* : $2x^2 + 5x - 12$ ; $-2(x^2 - 2x - 3) = -2x^2 + 4x + 6$.

### Ex R2.3 — Factoriser par un facteur commun

**Réponses** : a) `[3, 2, 5]` · b) `[-2, 3]` · c) `[3, -2]` · d) `[1, 5]` · e) `[5, -3]` · f) `[1, 1]`.

**Démarche.**
- a) Le PGCD de 6 et 15 est 3, la plus petite puissance de $x$ est $x$ : $6x^2 + 15x = 3x(2x + 5)$.
- b) $4x^3 - 8x^2 + 12x = 4x(x^2 - 2x + 3)$ : on divise chaque terme par $4x$, avec son signe.
- c) Le facteur commun est $(x - 1)$ : $(x - 1)\big[(2x + 3) + (x - 5)\big] = (x - 1)(3x - 2)$.
- d) $(2x + 1)^2 = (2x + 1)(2x + 1)$, donc $(2x + 1)\big[(2x + 1) - (x - 4)\big] = (2x + 1)(2x + 1 - x + 4) = (2x + 1)(x + 5)$.
- e) $(x + 2)(5x - 3)$.
- f) $x(x - 7) + 1 \times (x - 7) = (x - 7)(x + 1)$.

**Vérifier en redéveloppant** : pour d), $(2x + 1)(x + 5) = 2x^2 + 11x + 5$, et $(4x^2 + 4x + 1) - (2x^2 - 7x - 4) = 2x^2 + 11x + 5$.

**Erreurs fréquentes.**
- a) Factoriser seulement par $x$ ou par 3 : c'est juste, mais pas « le plus grand facteur commun ».
- d) Écrire $(2x + 1) - x - 4$ : le moins devant la parenthèse $(x - 4)$ change aussi le signe de $-4$.
- f) Écrire $(x - 7) \times x + 0$ : le terme $x - 7$ « tout seul » vaut $1 \times (x - 7)$, il laisse un 1.

**Variante.** Factorise $9x^3 - 6x^2$ et $(x + 3)^2 - 2(x + 3)$. *Réponses* : $3x^2(3x - 2)$ ; $(x + 3)(x + 3 - 2) = (x + 3)(x + 1)$.

### Ex R2.4 — Identités remarquables dans les deux sens

**Réponses** : a) `[1, 10, 25]` · b) `[9, -24, 16]` · c) `[4, 0, -49]` · d) `7` · e) `[5, 3]` · f) `[2, 5]` · g) `10201` · h) `3599`.

**Démarche.**
- a) $x^2 + 2 \times x \times 5 + 25$.
- b) $a = 3x$, $b = 4$ : $(3x)^2 - 2 \times 3x \times 4 + 4^2 = 9x^2 - 24x + 16$.
- c) $(2x)^2 - 7^2 = 4x^2 - 49$ : le coefficient de $x$ est 0.
- d) $(x - a)^2 = x^2 - 2ax + a^2$ ; on identifie $2a = 14$ et $a^2 = 49$ : $a = 7$ (les deux conditions sont compatibles).
- e) $25x^2 - 9 = (5x)^2 - 3^2 = (5x - 3)(5x + 3)$.
- f) $4x^2 = (2x)^2$, $25 = 5^2$, et le terme du milieu est bien $2 \times 2x \times 5 = 20x$ : $(2x + 5)^2$.
- g) $(100 + 1)^2 = 10\,000 + 200 + 1 = 10\,201$.
- h) $(60 - 1)(60 + 1) = 3600 - 1 = 3599$.

**Erreurs fréquentes.**
- b) Écrire $3x^2$ au lieu de $9x^2$ : le carré porte sur tout $3x$. Ou oublier que le double produit de $(a - b)^2$ est négatif.
- c) Écrire $+49$.
- d) Répondre 14 (le double produit) ou 49 (le carré).
- f) Avant de factoriser en carré, vérifier le terme du milieu : $4x^2 + 10x + 25$ n'est **pas** un carré.

**Variante.** Développe $(5x - 1)^2$, factorise $49x^2 - 1$, calcule $98 \times 102$ de tête. *Réponses* : $25x^2 - 10x + 1$ ; $(7x - 1)(7x + 1)$ ; $100^2 - 2^2 = 9996$.

### Ex R2.5 — Équations du premier degré

**Réponses** : a) `-2` · b) `-3` · c) `13` · d) `18` · e) `1` (aucune solution) · f) `3` (une infinité).

**Démarche.**
- a) $4x = 1 - 9 = -8$, donc $x = -2$. Vérification : $-8 + 9 = 1$.
- b) $-2x - 3x = 20 - 5$, soit $-5x = 15$, $x = -3$. Vérification : $5 + 6 = 11$ et $-9 + 20 = 11$.
- c) $3x - 6 = 2x + 8 - 1 = 2x + 7$, donc $x = 13$. Vérification : $3 \times 11 = 33$ et $2 \times 17 - 1 = 33$.
- d) On multiplie par 6 : $4x - 6 = 3(x + 4) = 3x + 12$, donc $x = 18$. Vérification : $12 - 1 = 11$ et $\frac{22}{2} = 11$.
- e) $3x - 3 + 5 = 3x + 4$, soit $3x + 2 = 3x + 4$, puis $2 = 4$ : faux pour tout $x$, **aucune** solution.
- f) $4x - 4 + 6 = 4x + 2$, et $2(2x + 1) = 4x + 2$ : $4x + 2 = 4x + 2$ est vrai pour tout $x$, **une infinité** de solutions (tous les réels).

**Erreurs fréquentes.**
- c) Développer $3(x - 2)$ en $3x - 2$.
- d) Multiplier $\frac{x + 4}{2}$ par 6 en $3x + 4$ : le 3 multiplie tout le numérateur. Ou oublier de multiplier le $-1$.
- e) et f) Conclure « $x = 0$ » quand les $x$ disparaissent : il faut regarder si l'égalité qui reste est vraie ou fausse.

**Variante.** Résous $2(x + 5) = 5x - 2$ et $\frac{x - 1}{4} = \frac{x}{6}$. *Réponses* : $3x = 12$, $x = 4$ ; $\times 12$ : $3x - 3 = 2x$, $x = 3$.

### Ex R2.6 — Équations produit nul et équations avec des fractions

**Réponses** : a) `[4, -1.5]` · b) `[0, 9/4]` · c) `[1/3]` · d) `[-4/3, 4/3]` · e) `1` · f) `[5/2]` · g) `[8]`.

**Démarche.**
- a) $x - 4 = 0$ ou $2x + 3 = 0$ : $x = 4$ ou $x = -\frac{3}{2}$.
- b) $4x^2 - 9x = 0$, soit $x(4x - 9) = 0$ : $x = 0$ ou $x = \frac{9}{4}$.
- c) $(3x - 1)^2 = 0 \iff 3x - 1 = 0 \iff x = \frac{1}{3}$ : une seule solution.
- d) $(3x)^2 - 4^2 = (3x - 4)(3x + 4) = 0$ : $x = \frac{4}{3}$ ou $x = -\frac{4}{3}$.
- e) Le dénominateur $x - 1$ s'annule pour $x = 1$ : c'est la valeur interdite.
- f) Pour $x \ne 1$, on multiplie par $x - 1$ : $x + 2 = 3(x - 1) = 3x - 3$, donc $2x = 5$, $x = \frac{5}{2}$, qui n'est pas interdit. Vérification : $\frac{4{,}5}{1{,}5} = 3$.
- g) On multiplie par 12 : $3x - 2(x - 2) = 12$, soit $3x - 2x + 4 = 12$, $x = 8$. Vérification : $2 - 1 = 1$.

**Erreurs fréquentes.**
- b) Diviser par $x$ et perdre la solution 0 (fiche §4).
- c) Donner deux solutions opposées : seul $u = 0$ vérifie $u^2 = 0$.
- d) Oublier la solution négative, ou s'arrêter à $x^2 = \frac{16}{9}$.
- f) Écrire $x + 2 = 3x - 1$ : le 3 multiplie tout $x - 1$.
- g) Écrire $-2x - 4$ : le moins devant la fraction porte sur tout le numérateur.

**Variante.** Résous $25x^2 - 4 = 0$ et $\frac{2}{x - 3} = \frac{1}{x}$. *Réponses* : $x = \pm\frac{2}{5}$ ; valeurs interdites 0 et 3, puis $2x = x - 3$, $x = -3$, qui n'est pas interdit.

### Ex R2.7 — Inéquations et intervalles

**Réponses** : a) `"]-oo ; 6["` · b) `"]-oo ; -3]"` · c) `"[3 ; +oo["` · d) `"]-3 ; 3]"` · e) `"]-12 ; +oo["`.

**Démarche.**
- a) $2x < 12$, $x < 6$.
- b) $-5x \ge 15$ ; on divise par $-5$, **le sens change** : $x \le -3$.
- c) $2x + 2 \le 5x - 7 \iff 9 \le 3x \iff x \ge 3$ (en regroupant les $x$ à droite, on divise par 3, positif : pas de changement de sens).
- d) $-6 < 2x \le 6$, puis $-3 < x \le 3$ : chaque borne garde son inégalité.
- e) On multiplie par 6, positif : $3x + 6 > 2(x - 3) = 2x - 6$, donc $x > -12$.

**Vérifier avec une valeur.** Pour b) : $x = -4$ donne $3 + 20 = 23 \ge 18$, vrai ; $x = 0$ donne $3 \ge 18$, faux. L'intervalle trouvé contient bien $-4$ et pas 0.

**Erreurs fréquentes.** Garder le sens en divisant par un négatif (b) ; un crochet fermé pour une inégalité stricte (a) ; oublier la parenthèse autour de $x - 3$ (e).

**Variante.** Résous $5 - 2x \le 11$ et $-1 \le \frac{x + 1}{2} < 3$. *Réponses* : $[-3 \;;\; +\infty[$ ; $-2 \le x + 1 < 6$, soit $[-3 \;;\; 5[$.

### Ex R2.8 — Réunion et intersection d'intervalles

**Réponses** : a) `"[1 ; 5]"` · b) `"[0 ; 3["` · c) `"[-4 ; 6["` · d) `"vide"` · e) `"]-oo ; -2[ U [3 ; +oo["` · f) `"]2 ; 5["`.

**Démarche.** Dessine chaque fois les deux intervalles sur une même droite (comme la figure de la fiche §5).
- a) Les nombres à la fois dans $[-2 ; 5]$ et dans $[1 ; 8]$ : de 1 à 5, bornes comprises.
- b) De 0 (inclus dans les deux intervalles) à 3 (exclu de $]-\infty ; 3[$).
- c) Les deux intervalles se chevauchent sur $[0 ; 1]$ : leur réunion va de $-4$ (inclus) à 6 (exclu).
- d) Aucun nombre n'est à la fois $\le -1$ et $\ge 2$ : $\varnothing$.
- e) « ou » : la réunion de $]-\infty ; -2[$ et de $[3 ; +\infty[$, qui ne se simplifie pas.
- f) $2x - 1 > 3 \iff x > 2$ et $3x < 15 \iff x < 5$ ; « et » : l'intersection $]2 ; 5[$.

**Erreurs fréquentes.** Confondre $\cap$ et $\cup$ ; garder un crochet fermé pour une borne exclue de l'un des deux intervalles (b) ; laisser la réunion c) en deux morceaux qui se chevauchent.

**Variante.** $[0 ; 4[ \cap\, ]2 ; 7]$ et $[0 ; 4[ \cup\, ]2 ; 7]$ ? *Réponses* : $]2 ; 4[$ ; $[0 ; 7]$.

### Ex R2.9 — Équations et inéquations avec une valeur absolue, et la fonction signe

**Réponses** : a) `[-1, 7]` · b) `[-5, 4]` · c) `[]` (aucune solution) · d) `"[-4 ; 2]"` · e) `"]-oo ; -3[ U ]7 ; +oo["` · f) `6.5` · g) `-1`.

**Démarche.**
- a) Les points à distance 4 de 3 : $3 - 4 = -1$ et $3 + 4 = 7$.
- b) $2x + 1 = 9$ ou $2x + 1 = -9$ : $x = 4$ ou $x = -5$.
- c) Une valeur absolue n'est jamais négative : aucune solution, la liste vide.
- d) $|x + 1| = |x - (-1)|$ : les points à au plus 3 de $-1$, de $-4$ à 2.
- e) Les points à plus de 5 de 2 : à gauche de $-3$ ou à droite de 7, bornes exclues.
- f) $|-4{,}5 - 2| = |-6{,}5| = 6{,}5$.
- g) $(-2)^2 - 9 = -5 < 0$, donc le signe vaut $-1$.

**Erreurs fréquentes.** Une seule solution en a) ou b) ; lire $|x + 1|$ comme la distance à 1 (d) ; prendre l'intérieur au lieu de l'extérieur en e) ; répondre $-5$ en g) au lieu du **signe** de $-5$.

**Variante.** Résous $|x + 4| = 1$ et $|x - 1| < 2$. *Réponses* : $\{-5 ; -3\}$ ; $]-1 \;;\; 3[$.

### Ex R2.10 — Système 2 × 2 par substitution et par combinaison

**Réponses** : a) `[2, 3]` · b) `[1, -2]` · c) `[2, -3]` · d) `[6, 3]`.

**Démarche.**
- a) Substitution : la seconde donne $y = 3x - 3$ ; la première devient $x + 6x - 6 = 8$, soit $x = 2$, puis $y = 3$. Vérification : $2 + 6 = 8$ et $6 - 3 = 3$.
- b) Combinaison : la première multipliée par 2 donne $10x + 4y = 2$ ; on soustrait la seconde : $7x = 7$, $x = 1$ ; puis $2y = 1 - 5$, $y = -2$. Vérification : $3 - 8 = -5$.
- c) Substitution : $y = 1 - 2x$ ; $4x - 3(1 - 2x) = 17$, soit $10x = 20$, $x = 2$, $y = -3$. Vérification : $8 + 9 = 17$.
- d) On chasse les fractions (× 6) : $3x + 2y = 24$ ; avec $x = y + 3$ : $5y + 9 = 24$, $y = 3$, $x = 6$. Vérification : $3 + 1 = 4$.

**Erreurs fréquentes.** Donner $[y, x]$ ; oublier de multiplier le second membre en combinant ; ne vérifier le couple que dans une seule équation (celle qui a servi à calculer la seconde inconnue le vérifie forcément).

**Variante.** $\begin{cases} 2x + y = 7 \\ x - 3y = 7 \end{cases}$. *Réponse* : $y = 7 - 2x$, puis $7x - 21 = 7$, $x = 4$, $y = -1$.

### Ex R2.11 — Système 2 × 2 par la formule de Cramer

**Réponses** : a) `-17` · b) `[3, -1]` · c) `3` (une infinité) · d) `1` (aucune).

**Démarche.**
- a) $a = 2$, $b = 5$, $c = 3$, $d = -1$ : $D = 2 \times (-1) - 5 \times 3 = -17$.
- b) $x = \frac{ed - bf}{D} = \frac{1 \times (-1) - 5 \times 10}{-17} = \frac{-51}{-17} = 3$ et $y = \frac{af - ec}{D} = \frac{2 \times 10 - 1 \times 3}{-17} = \frac{17}{-17} = -1$. Vérification : $6 - 5 = 1$ et $9 + 1 = 10$.
- c) $D = 2 \times 6 - (-3) \times (-4) = 12 - 12 = 0$. La seconde équation est la première multipliée par $-2$, second membre compris ($4 \times (-2) = -8$) : la même droite, une infinité de solutions.
- d) Même déterminant nul, mais $4 \times (-2) = -8 \ne 1$ : deux droites parallèles distinctes, aucune solution.

**Erreurs fréquentes.** Oublier le signe de $d = -1$ ; calculer $ad + bc$ ; conclure « une solution » sans regarder le déterminant ; diviser par un $D$ nul.

**Variante.** $\begin{cases} 4x + 3y = 10 \\ 2x - y = 0 \end{cases}$ par Cramer. *Réponse* : $D = -10$, $x = \frac{-10}{-10} = 1$, $y = \frac{-20}{-10} = 2$.

### Ex R2.12 — Mettre en équation : trois problèmes

**Réponses** : a) `120` (cm²) · b) `70` (€) · c) `10`.

**Démarche.**
- a) Inconnue : la largeur $\ell$, en cm ; la longueur vaut $\ell + 7$. Périmètre : $2(\ell + \ell + 7) = 46$, soit $4\ell + 14 = 46$, $\ell = 8$, puis la longueur 15. Vérification : $2 \times (8 + 15) = 46$. Réponse : l'aire vaut $8 \times 15 = 120$ cm².
- b) Inconnue : le prix $p$ avant la baisse. Une baisse de 20 % multiplie par 0,8 : $0{,}8\,p = 56$, $p = 70$. Vérification : 20 % de 70 valent 14, et $70 - 14 = 56$. Réponse : le casque coûtait 70 €.
- c) Inconnues : $q$ tables de 4 places, $s$ tables de 6. $q + s = 22$ et $4q + 6s = 108$. Par substitution, $4(22 - s) + 6s = 108$, soit $2s = 20$, $s = 10$, puis $q = 12$. Vérification : $48 + 60 = 108$. Réponse : il y a 10 tables de 6 places.

**Erreurs fréquentes.** a) Écrire le périmètre $\ell + (\ell + 7) = 46$, ou répondre la longueur au lieu de l'aire. b) Calculer $56 \times 1{,}2$ : la baisse de 20 % portait sur le prix de départ, pas sur 56 €. c) Répondre 12, le nombre de tables de **4** places.

**Variante.** Après une hausse de 30 %, un abonnement coûte 104 € : quel était son prix ? *Réponse* : $1{,}3\,p = 104$, $p = 80$ €.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R2.13 — Démontrer les identités remarquables

**Démonstration.**
1. Par double distributivité, $(a + b)(a + b) = a \times a + a \times b + b \times a + b \times b$. La multiplication est **commutative** : $b \times a = a \times b$, donc les deux termes du milieu font $2ab$, et $(a + b)^2 = a^2 + 2ab + b^2$.
2. On applique 1 à $a$ et à $-b$ (1 est vraie pour **tous** réels) : $(a + (-b))^2 = a^2 + 2a(-b) + (-b)^2 = a^2 - 2ab + b^2$, car $(-b)^2 = b^2$.
3. $(a + b)(a - b) = a^2 - ab + ba - b^2 = a^2 - b^2$, les deux termes du milieu s'annulant (commutativité encore).
4. $(n + 1)^2 - n^2 = n^2 + 2n + 1 - n^2 = 2n + 1$ : c'est un entier impair (de la forme $2k + 1$ avec $k = n$). Et $99 \times 101 = (100 - 1)(100 + 1) = 100^2 - 1^2 = 9999$ : la question 3 transforme le produit en une différence de carrés faciles.
5. On part du carré de côté $a$ (aire $a^2$) et on veut le carré de côté $a - b$, dans un coin. On retire une bande de $a \times b$ le long d'un côté, puis une autre le long du côté perpendiculaire. Le petit carré $b \times b$ du coin commun aux deux bandes a été retiré **deux fois** : il faut le rajouter une fois. Il reste $(a - b)^2 = a^2 - 2ab + b^2$.

**Grille de relecture.**
- 1 nomme la propriété utilisée (la commutativité) pour regrouper $ab$ et $ba$.
- 2 **réutilise** 1 au lieu de redévelopper, en disant pourquoi c'est permis (1 vaut pour tous réels, donc pour $-b$).
- 3 développe les quatre produits et montre que les deux termes du milieu s'annulent.
- 4 écrit le résultat sous la forme $2k + 1$ et dit pourquoi c'est impair ; l'exemple $99 \times 101$ utilise 3 explicitement.
- 5 explique pourquoi le carré $b^2$ revient (compté deux fois dans les bandes).

**Erreurs fréquentes.** Vérifier l'identité sur des exemples ($a = 1$, $b = 2$) au lieu de la démontrer : des exemples ne prouvent pas une égalité « pour tous ». En 2, écrire $(-b)^2 = -b^2$.

**Variante.** Démontre que $(a - b)(a^2 + ab + b^2) = a^3 - b^3$. *Réponse* : $a^3 + a^2 b + ab^2 - a^2 b - ab^2 - b^3 = a^3 - b^3$.

### Ex R2.14 — Pourquoi multiplier par un nombre négatif retourne l'inégalité

**Démonstration.** Par hypothèse, $b - a > 0$.
1. $(b + c) - (a + c) = b - a > 0$, donc $a + c < b + c$.
2. $kb - ka = k(b - a)$ : un produit de deux nombres strictement positifs, donc strictement positif. Ainsi $ka < kb$.
3. $kb - ka = k(b - a)$ : un nombre strictement négatif fois un nombre strictement positif, donc strictement négatif. Ainsi $kb - ka < 0$, c'est-à-dire $ka - kb > 0$ : $ka > kb$.
4. Si $0 < a < b$, alors $b = a + (b - a)$ est la somme de deux nombres strictement positifs, donc $b > 0$. Puis $ab > 0$ (produit de deux positifs), et $\frac{1}{ab} > 0$ : il n'est pas nul, et s'il était négatif, le produit $ab \times \frac{1}{ab} = 1$ serait négatif. D'après 2, multiplier $a < b$ par $\frac{1}{ab}$ garde le sens : $\frac{a}{ab} < \frac{b}{ab}$, soit $\frac{1}{b} < \frac{1}{a}$.
5. Contre-exemple : $a = -3 < b = 1$, mais $a^2 = 9 > b^2 = 1$. Si $0 \le a < b$ : $b^2 - a^2 = (b - a)(b + a)$ ; $b - a > 0$, et $b + a > 0$ (d'abord $b > 0$ : si $a = 0$, $b = b - a > 0$, sinon comme en 4 ; puis $b + a$ vaut $b$ si $a = 0$, et sinon c'est une somme de deux positifs). Le produit est positif, donc $a^2 < b^2$.

**Grille de relecture.**
- Chaque question revient à la **définition** : on calcule une différence et on étudie son signe.
- 2 et 3 factorisent la différence par $k$ et citent la règle des signes utilisée.
- 4 justifie que $\frac{1}{ab}$ est positif avant de l'utiliser, et réutilise 2.
- 5 donne un contre-exemple chiffré **et** identifie l'hypothèse qui manquait ($a \ge 0$).

**Erreurs fréquentes.** Utiliser le résultat à démontrer (« on divise par $k < 0$, donc le sens change ») ; oublier, en 4, de montrer que $b > 0$.

**Variante.** Montre que si $a < b$ et $c < d$, alors $a + c < b + d$. *Réponse* : $(b + d) - (a + c) = (b - a) + (d - c)$, somme de deux nombres strictement positifs, donc strictement positive.

### Ex R2.15 — Quand un système 2 × 2 a-t-il une seule solution ?

**Démonstration.**
1. Si $(x, y)$ est solution, $d(ax + by) - b(cx + dy) = de - bf$, soit $adx + bdy - bcx - bdy = de - bf$ : les termes en $y$ s'annulent, et $(ad - bc)x = ed - bf$, c'est-à-dire $D\,x = ed - bf$. De même, $a(cx + dy) - c(ax + by) = af - ce$ donne $(ad - bc)y = af - ec$.
2. Si $D \ne 0$, toute solution vérifie $x = \frac{ed - bf}{D}$ et $y = \frac{af - ec}{D}$ : il y en a **au plus** une. Réciproquement, ce couple est solution : $a \cdot \frac{ed - bf}{D} + b \cdot \frac{af - ec}{D} = \frac{aed - abf + abf - bec}{D} = \frac{e(ad - bc)}{D} = e$. (La seconde : $c(ed - bf) + d(af - ec) = f(ad - bc)$, donc elle vaut $f$.) Le système a donc **exactement une** solution.
3. On suppose $D = 0$ et $a \ne 0$ ; on pose $k = \frac{c}{a}$, donc $c = ka$. De $ad = bc = b \cdot ka$, on tire, en divisant par $a \ne 0$, $d = kb$. La seconde équation s'écrit $kax + kby = f$, soit $k(ax + by) = f$.
4. Si $f = ke$ : tout couple qui vérifie $ax + by = e$ vérifie $k(ax + by) = ke = f$, donc la seconde équation. Or la première a une infinité de solutions (une droite, puisque $a \ne 0$ : pour chaque $y$, $x = \frac{e - by}{a}$). Une infinité de solutions. Si $f \ne ke$ : un couple solution donnerait $f = k(ax + by) = ke$, ce qui est faux. Aucune solution. (Le cas $k = 0$ est compris : la seconde équation devient $0 = f$.)
5. Avec 2, 3 et 4 : si $D \ne 0$, une seule solution ; si $D = 0$ et $a \ne 0$, aucune ou une infinité. Les cas admis se ramènent à celui-là : si $a = 0$ et $c \ne 0$, on échange les deux équations ; si $a = c = 0$, $x$ n'apparaît plus, et le système en $y$ seul ($by = e$, $dy = f$) a aucune solution ou une infinité (toutes les valeurs de $x$ conviennent dès qu'un $y$ convient). Donc « une seule solution » équivaut à $D \ne 0$. Pour le système proposé, $D = 6 \times 6 - (-4) \times (-9) = 0$ et $k = -\frac{9}{6} = -\frac{3}{2}$ (on vérifie $d = kb$ : $-\frac{3}{2} \times (-4) = 6$). Une infinité de solutions exactement quand $m = ke = -\frac{3}{2} \times 2 = -3$.

**Grille de relecture.**
- 1 écrit les deux combinaisons **et** montre que l'autre inconnue disparaît.
- 2 sépare les deux sens : « au plus une » (unicité, par 1) **et** « au moins une » (existence, par substitution).
- 3 justifie la division par $a$, et 4 traite les deux sous-cas ($f = ke$ et $f \ne ke$).
- 5 conclut par une équivalence (« si et seulement si ») qui rassemble les trois cas.

**Erreurs fréquentes.** Croire que 1 suffit à prouver l'existence d'une solution (1 suppose qu'une solution existe) ; diviser par $D$ sans avoir supposé $D \ne 0$ ; en 5, chercher la valeur de $m$ qui annule le déterminant (il est nul pour tout $m$).

**Variante.** Montre que si $D \ne 0$, le système $\begin{cases} ax + by = 0 \\ cx + dy = 0 \end{cases}$ n'a que la solution $(0, 0)$. *Réponse* : par 1, $D\,x = 0$ et $D\,y = 0$, donc $x = y = 0$ ; et $(0, 0)$ est bien solution.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R2.16 — Deux mesures, deux inconnues : retrouver a et b dans y = ax + b par un système

**Réponses** : a) `[25, -8]` · b) `27` · c) `-0.5` · d) `1` (aucun couple).

**Démarche.**
- a) Chaque mesure donne une équation d'inconnues $a$ et $b$ : $0{,}8\,a + b = 12$ et $2a + b = 42$. En soustrayant la première de la seconde, $1{,}2\,a = 30$, donc $a = 25$ ; puis $b = 12 - 0{,}8 \times 25 = -8$. Vérification : $2 \times 25 - 8 = 42$.
- b) $T = 25 \times 1{,}4 - 8 = 27$ °C.
- c) Le modèle prédit $25 \times 2{,}4 - 8 = 52$ °C ; l'écart vaut $51{,}5 - 52 = -0{,}5$ °C.
- d) La troisième équation, $2{,}4\,a + b = 51{,}5$, n'est pas vérifiée par l'unique couple $(25, -8)$ des deux premières : aucun couple ne vérifie les trois. Trois points qui ne sont pas alignés ne sont sur aucune droite.

**Ce que disent c et d.** Avec deux mesures, on trouve toujours une droite qui passe exactement par les deux points (si leurs $u$ diffèrent). Avec plus de mesures, toutes un peu bruitées, aucune droite ne passe par tous les points : le système a plus d'équations que d'inconnues, et pas de solution. On cherche alors la droite qui rend les écarts (comme celui de c) **les plus petits possible** dans leur ensemble : c'est la méthode des moindres carrés, que workbookIA développe (régression linéaire, chapitre 9), et l'écart de c s'appelle un **résidu**.

**Erreurs fréquentes.** Prendre $u$ et $T$ pour les inconnues ; donner $[b, a]$ ; un écart de signe opposé (prédiction moins mesure).

**Variante.** Avec les mesures $(1 ; 30)$ et $(3 ; 70)$, trouve $a$ et $b$. *Réponse* : $2a = 40$, $a = 20$, $b = 10$.

### Ex R2.17 — Expliquer ce que veut dire « résoudre une équation »

**Exemple de réponse.**

> Résoudre une équation, c'est trouver **toutes** ses solutions, pas seulement une. Dans ta première résolution, tu as divisé par $x$, mais $x$ peut valoir 0, et justement $0^2 = 6 \times 0$ : tu as perdu la solution 0. Il fallait écrire $x^2 - 6x = 0$, soit $x(x - 6) = 0$, donc $x = 0$ ou $x = 6$. Dans la seconde, tu as vérifié que 4 marche : c'est bien une solution, mais rien ne dit qu'il n'y en a pas d'autres. En résolvant ($3x = 12$), on montre que 4 est la **seule**. La vérification sert à attraper une erreur de calcul ; elle ne remplace pas la résolution.

**Grille.** Une bonne réponse dit : (1) résoudre, c'est trouver l'ensemble de **toutes** les solutions ; (2) la division par $x$ perd la solution 0, et on factorise à la place ; (3) une vérification confirme une solution, mais ne prouve pas qu'il n'y en a pas d'autres ; (4) elle reste courte et sans jargon (pas d'« équivalence » sans l'expliquer).

<a id="notebook"></a>

## Notebook

### Ex R2.22 — Vérifier développements et factorisations avec SymPy

**Réponses** : a) `[3, 10, -11, 2]` · b) `"BC"` · c) `[3, -4]`.

**Démarche.** a) `sp.expand((3*x - 2)*(x**2 + 4*x - 1))` donne $3x^3 + 10x^2 - 11x + 2$, et `sp.Poly(..., x).all_coeffs()` la liste. b) `sp.expand(gauche - droite)` vaut 0 pour B et C ; il vaut $18 - 6x$ pour A et 4 pour D. c) `sp.factor(x**2 + x - 12)` donne $(x - 3)(x + 4)$, qui s'annule en 3 et en $-4$.

**Erreurs fréquentes.** Lire les coefficients à l'envers (`all_coeffs` commence par le plus haut degré) ; tester une égalité sur une seule valeur de $x$ au lieu de développer l'écart ; en c), donner les nombres des parenthèses avec leur signe ($-3$ et 4) au lieu des valeurs qui les annulent.

**Variante.** Que renvoie `sp.expand((x + 2)*(x**2 - 2*x + 4))` ? *Réponse* : `x**3 + 8`, la somme de deux cubes.

### Ex R2.27 — Chasse à l'erreur : six erreurs de calcul littéral

**Réponses** : a) `"ACDFGH"` · b) `[-1, 11]` · c) `"]-2.5 ; +oo["` · d) `[0, 2]`.

**Démarche.**
- A : $(x - 5)^2 = x^2 - 10x + 25$, le double produit manque.
- B est juste : le moins change les deux signes.
- C : $(3x)^2 = 9x^2$.
- D : $2x + 8 - 3x + 3 = -x + 11$ ; le calcul faux a écrit $-3$ au lieu de $+3$.
- E est juste : $(a + b)(a - b) = a^2 - b^2$.
- F : on divise par $-4$, négatif, le sens change : $x > -2{,}5$.
- G : $3x^2 - 6x = 3x(x - 2) = 0$, donc $x = 0$ ou $x = 2$ ; diviser par $x$ a perdu 0.
- H : $\frac{x + 1}{2} \times 4 = 2(x + 1) = 2x + 2$.

**Erreurs fréquentes.** Déclarer B fausse (le résultat a bien les deux signes changés) ; corriger F en gardant $x < -2{,}5$ ; en d), oublier la solution 0.

### Ex R2.18 — Résoudre ax + b = 0 dans tous les cas · `solve_linear`

**Réponses** : `solve_linear(-5, 2)` vaut `[0.4]` ; `solve_linear(0, -3)` vaut `[]` ; `solve_linear(0, 0)` vaut exactement `"all"` (la vérification compare avec `==`).

**Démarche.** `if a == 0: return "all" if b == 0 else []`, puis `return [-b / a]`. Le test de `a == 0` vient **avant** la division.

**Erreurs fréquentes.** Diviser d'abord (`ZeroDivisionError` pour `a == 0`) ; renvoyer `[b / a]` (le signe) ou `[-a / b]` ; renvoyer `[]` pour « tous les réels », ou `None` au lieu de `[]` ; renvoyer un nombre au lieu d'une liste.

**Variante.** Que renvoient `solve_linear(4, 0)` et `solve_linear(0, -0.5)` ? *Réponses* : `[0.0]` (la solution est 0 : $b = 0$ ne veut pas dire « aucune solution ») ; `[]`.

### Ex R2.19 — Résoudre ax + b ≤ 0 et rendre l'intervalle des solutions · `solve_linear_inequality`

**Réponses** : `solve_linear_inequality(-4, -6, ">=")` vaut `(False, -inf, -1.5, True)`, soit $]-\infty \;;\; -1{,}5]$ ; `solve_linear_inequality(0, 3, ">")` vaut `(False, -inf, inf, False)`, toute la droite ($3 > 0$ est vrai pour tout $x$).

**Démarche.** Pour $-4x - 6 \ge 0$ : la borne est $-\frac{-6}{-4} = -1{,}5$ ; $a < 0$, donc `">="` devient `"<="`, et l'ensemble est $]-\infty ; -1{,}5]$. Le code complet (un dictionnaire pour retourner le sens, un autre pour le cas $a = 0$) est dans `05_solutions.ipynb`.

**Erreurs fréquentes.** Oublier de retourner le sens quand `a < 0` ; un crochet fermé à l'infini (`True` en première position avec `-inf`) ; ne pas lever `ValueError` pour un sens inconnu ; traiter `a == 0` en divisant, ou en ne pensant qu'aux sens `"<"` et `"<="` (pour `">"`, c'est $b > 0$ qu'il faut tester) ; oublier `import math` (le squelette ne l'importe pas).

**Variante.** `solve_linear_inequality(2, -5, ">")` ? *Réponse* : `(False, 2.5, inf, False)`, soit $]2{,}5 \;;\; +\infty[$.

### Ex R2.20 — Résoudre |x − a| = c · `solve_abs_equation`

**Réponses** : `solve_abs_equation(-1.5, 4)` vaut `[-5.5, 2.5]` ; `solve_abs_equation(7, 0)` vaut `[7.0]`.

**Démarche.** `c < 0` : `[]` ; `c == 0` : `[float(a)]` ; sinon `[float(a - c), float(a + c)]`, déjà dans l'ordre croissant puisque $c > 0$.

**Erreurs fréquentes.** Renvoyer `[a, a]` quand $c = 0$ ; oublier le cas $c < 0$ ; rendre `[a + c, a - c]` (ordre décroissant).

**Variante.** `solve_abs_equation(-2, 0.5)` ? *Réponse* : `[-2.5, -1.5]`.

### Ex R2.23 — Résoudre avec `sympy.solve` et lire son résultat

**Réponses** : a) `4` · b) `0` · c) `Reals`, soit $]-\infty \;;\; +\infty[$ · d) `[1, 2]`.

**Démarche.** a) `sp.solve(4*x - 7 - (x + 5), x)` renvoie `[4]`, dont on prend le premier élément. b) SymPy simplifie $3(x - 2) - (3x - 6)$ en 0, et `sp.solve(0, x)` renvoie `[]` : une liste vide, comme pour $5(x - 1) = 5x - 2$, qui n'a **aucune** solution, alors que la première équation en a une **infinité**. c) `sp.solveset` distingue les deux cas : `Reals` pour la première, `EmptySet` pour la seconde. d) `sp.solve([7*x - 2*y - 3, x + y - 3], [x, y])` renvoie `{x: 1, y: 2}`.

**Erreurs fréquentes.** Donner `A` à `sp.solve` au lieu de `A - B` ; conclure de `[]` qu'il n'y a pas de solution ; donner le dictionnaire au lieu de la liste.

### Ex R2.28 — Écrire un test pytest pour une fonction qui résout une équation

**Une solution** (d'autres choix de cas sont justes) :

```python
def check_solve_linear(solve_linear):
    for a, b in [(3, -7), (-2, 5), (0.5, 4)]:            # one solution: substitute it back
        result = solve_linear(a, b)
        assert isinstance(result, list) and len(result) == 1, f"one solution expected for {a}x + {b} = 0"
        assert abs(a * result[0] + b) < 1e-9, f"{result[0]} is not a solution of {a}x + {b} = 0"
    assert solve_linear(0, 4) == [], "0x + 4 = 0 has no solution"
    assert solve_linear(0, 0) == "all", "0x + 0 = 0 holds for every x"
```

**Démarche.** Chaque version fausse rate un cas : `solve_linear_wrong_sign` est attrapée par la substitution (si $b \ne 0$), `solve_linear_divides_by_zero` lève `ZeroDivisionError` dès le cas `a == 0`, `solve_linear_forgets_all` échoue sur `"all"`.

**Erreurs fréquentes.** Ne tester que des cas où $b = 0$ (la solution 0 ne trahit pas l'erreur de signe) ; oublier un des deux cas dégénérés ; comparer la solution à une valeur calculée de tête (et fausse).

### Ex R2.21 — Système 2 × 2 par la formule de Cramer · `solve_2x2`

**Réponses** : `solve_2x2([[3, 4], [5, -2]], [5.5, 13.5])` vaut `(2.5, -0.5)` ; pour un déterminant nul, l'erreur levée est `ValueError`.

**Démarche.** $D = 3 \times (-2) - 4 \times 5 = -26$ ; $x = \frac{5{,}5 \times (-2) - 4 \times 13{,}5}{-26} = \frac{-65}{-26} = 2{,}5$ ; $y = \frac{3 \times 13{,}5 - 5{,}5 \times 5}{-26} = \frac{13}{-26} = -0{,}5$. En code : `if det == 0: raise ValueError("the determinant is zero: no unique solution")`, puis les deux quotients, rendus dans un tuple.

**Erreurs fréquentes.** Diviser sans tester $D$ (`ZeroDivisionError`) ; confondre `b`, la liste des seconds membres, avec le coefficient $b$ ; inverser l'ordre d'un produit dans un numérateur ; rendre une liste au lieu d'un tuple.

**Variante.** `solve_2x2([[1, 2], [3, 4]], [5, 6])` ? *Réponse* : $D = -2$, `(-4.0, 4.5)`.

### Ex R2.26 — Un système, deux droites : voir la solution

**Réponse** : les deux droites se coupent en $(-1 \;;\; 2)$ ; la seconde, $2x = -2$, est la droite verticale $x = -1$. La figure de référence est dans `05_solutions.ipynb`.

**Ce qu'on regarde dans ta figure.** Deux droites distinctes (styles ou couleurs), la verticale tracée avec `axvline`, le point commun marqué, un titre qui donne ses coordonnées, une légende avec les deux équations, des axes nommés et une fenêtre fixe ($[-5 ; 5]$ en $x$ et en $y$). La cellule de vérifications automatiques regarde seulement que les deux droites et le titre sont dans l'axe donné, même pour un déterminant nul.

**Erreurs fréquentes.** Diviser par le coefficient de $y$ quand il est nul (un avertissement « divide by zero », et la droite manque) ; appeler `np.linalg.solve` quand le déterminant est nul (`LinAlgError: Singular matrix`) ; créer une nouvelle figure alors qu'un `ax` est fourni ; écrire le titre avec `plt.title` au lieu de `ax.set_title` (il va sur une autre figure, et R2.24 lit `ax.get_title()`).

### Ex R2.24 — Prédire le nombre de solutions de trois systèmes, puis tracer leurs droites

**Réponses** : $S_1$ : `1` (aucune) · $S_2$ : `2` (une seule) · $S_3$ : `3` (une infinité).

**Démarche.** $S_1$ : les coefficients de la seconde équation sont le double de ceux de la première, mais $7 \ne 2 \times 2$ : droites parallèles. $S_2$ : $1 \times (-1) - 2 \times 3 = -7 \ne 0$, une seule solution, $(2 \;;\; 1)$. $S_3$ : la seconde équation est la première multipliée par $-2$, second membre compris : la même droite.

**Erreur fréquente.** S'arrêter à « les coefficients sont proportionnels, donc aucune solution » sans comparer les seconds membres ($S_3$).

### Ex R2.25 — Expérience : un système presque dégénéré, un coefficient bouge de 0,001 et la solution s'envole

**Réponses** : a) `[1, 1]` · b) `[1.5, 0.5]` · c) `0.001` · d) `10`.

**Démarche.** Par Cramer, $D = c - 1$ et $y = \frac{2{,}001 - 2}{c - 1} = \frac{0{,}001}{c - 1}$, puis $x = 2 - y$. Pour $c = 1{,}001$ : $y = 1$ ; pour $c = 1{,}002$ : $y = 0{,}5$ ; pour $c = 1{,}0001$ : $y = 10$ et $x = -8$. Sur la figure en échelles logarithmiques, les points forment une droite de pente $-1$ : $y$ est inversement proportionnel au déterminant.

**Ce qu'il faut retenir.** Un déterminant minuscule devant les coefficients est un signal d'alarme : la solution existe, mais une petite erreur sur les données (une mesure, un arrondi) la change énormément. On dit que le système est **mal conditionné**. Géométriquement, les deux droites sont presque parallèles, et leur point commun glisse très loin quand l'une tourne à peine.

**Erreurs fréquentes.** Prendre 2 comme second membre de la seconde équation ; mettre $c$ comme coefficient de $x$ ; calculer le déterminant $1 - c$.
