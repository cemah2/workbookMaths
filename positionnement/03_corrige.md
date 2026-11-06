# Test de positionnement — corrigé

> Lis ce corrigé **après** avoir reporté toutes tes réponses dans le notebook et lu ta grille. Pour chaque exercice : les réponses, une démarche courte, l'erreur la plus fréquente, et la section du chapitre qui enseigne la notion. Une question ratée ne te dit pas seulement « à revoir » : elle te dit **où**.

<a id="r1"></a>

## R1 · Nombres et calcul

### POS.1 — Calculer avec des priorités et des fractions
**Réponses** : a) `16` · b) `"23/12"` · c) `"2/3"` · d) `"3/8"`.

- a) La parenthèse d'abord : $2 - 5 = -3$ ; puis la multiplication : $3 \times (-3) = -9$ ; enfin $7 - (-9) = 16$.
- b) Au dénominateur commun 12 : $\frac{8}{12} + \frac{15}{12} = \frac{23}{12}$, irréductible.
- c) Diviser par une fraction, c'est multiplier par son inverse : $\frac{3}{5} \times \frac{10}{9} = \frac{30}{45} = \frac{2}{3}$.
- d) $1 - \frac{1}{4} = \frac{3}{4}$, puis $\frac{3}{4} \div 2 = \frac{3}{8}$.

**Erreur fréquente** : en a, calculer $(7 - 3) \times (2 - 5)$, ou oublier que $-(-9) = +9$. **Où c'est enseigné** : R1 §2 (priorités, nombres négatifs) et §3 (fractions).

### POS.2 — Puissances, racines et notation scientifique
**Réponses** : a) `3` · b) `6` · c) `20000000` · d) `0.0025`.

- a) $3^{6 + (-2) - 3} = 3^1 = 3$.
- b) $\sqrt{72} = \sqrt{36 \times 2} = 6\sqrt{2}$.
- c) $\frac{6}{3} \times 10^{5 - (-2)} = 2 \times 10^{7} = 20\,000\,000$.
- d) $10^{-3}$ est un millième : $2{,}5 \times 10^{-3} = 0{,}0025$ (la virgule recule de 3 rangs).

**Erreur fréquente** : en a, traiter $3^{-2}$ comme $3^{2}$ ; en c, soustraire $-2$ comme si c'était $+2$ ($2 \times 10^{3}$) ; en d, reculer la virgule de 4 rangs. **Où c'est enseigné** : R1 §4 (puissances), §5 (racines) et §6 (notation scientifique).

<a id="r2"></a>

## R2 · Calcul littéral et équations

### POS.3 — Développer, factoriser, résoudre une équation et une inéquation
**Réponses** : a) `[2, 5, -12]` · b) `5` · c) `5` · d) `"]-oo ; 2]"`.

- a) $2x \cdot x + 2x \cdot 4 - 3 \cdot x - 3 \cdot 4 = 2x^2 + 8x - 3x - 12 = 2x^2 + 5x - 12$, d'où $a = 2$, $b = 5$, $c = -12$.
- b) $(x - a)^2 = x^2 - 2ax + a^2$ ; le double produit $2a = 10$ donne $a = 5$, et $a^2 = 25$ confirme.
- c) $5x - 2x = 8 + 7$, donc $3x = 15$ et $x = 5$.
- d) $-3x \geq -6$ ; on divise par $-3$, un nombre **négatif** : l'inégalité se retourne, $x \leq 2$.

**Erreur fréquente** : en d, garder le sens de l'inégalité en divisant par un négatif. **Où c'est enseigné** : R2 §2 et §3 (développer, factoriser, identités remarquables), §4 (équations), §5 (inéquations et intervalles).

### POS.4 — Un système de deux équations à deux inconnues
**Réponses** : a) `[3, 2]` · b) `1` (aucune solution).

- a) La seconde équation donne $x = 1 + y$ ; dans la première : $2(1 + y) + 3y = 12$, donc $5y = 10$, $y = 2$, puis $x = 3$. Vérification : $6 + 6 = 12$ et $3 - 2 = 1$.
- b) La seconde équation, divisée par 2, donne $x + 3y = 2{,}5$, alors que la première impose $x + 3y = 2$ : c'est impossible. Les deux droites sont parallèles et distinctes.

**Erreur fréquente** : en b, répondre « une infinité » parce que les membres de gauche sont proportionnels ; il faut aussi que les membres de droite le soient. **Où c'est enseigné** : R2 §7.

<a id="r3"></a>

## R3 · Fonctions

### POS.5 — Lire un graphique de fonction
**Réponses** : a) `1` · b) `3` · c) `"[-1 ; 2]"` · d) `3`.

- a) La courbe coupe l'axe vertical à la hauteur 1.
- b) La droite horizontale $y = 1$ coupe la courbe trois fois : en $x = -2$, en $x = 0$, et à l'extrémité droite, en $x = 4$.
- c) La courbe descend de $x = -1$ à $x = 2$ : le plus grand intervalle de décroissance est $[-1 ; 2]$, bornes comprises. ($g$ décroît aussi sur $]-1 ; 2[$, mais ce n'est pas le plus grand intervalle.)
- d) Le point le plus haut est $(-1 ; 3)$ : le maximum vaut 3 (il est atteint en $x = -1$).

**Erreur fréquente** : en b, oublier la solution à l'extrémité de l'intervalle ; en d, donner l'abscisse $-1$ au lieu de la valeur 3. **Où c'est enseigné** : R3 §2 (lecture graphique) et §6 (variations, maximum).

### POS.6 — Racines et sommet d'un polynôme du second degré
**Réponses** : a) `100` · b) `[-3, 2]` · c) `"-1/2"` · d) `"-25/2"`.

- a) $\Delta = b^2 - 4ac = 2^2 - 4 \times 2 \times (-12) = 4 + 96 = 100$.
- b) $x = \frac{-2 \pm 10}{4}$ : $x_1 = -3$ et $x_2 = 2$.
- c) $\alpha = -\frac{b}{2a} = -\frac{2}{4} = -\frac{1}{2}$.
- d) $p\left(-\frac{1}{2}\right) = 2 \times \frac{1}{4} - 1 - 12 = -\frac{25}{2}$ ; c'est un minimum, car $a = 2 > 0$.

**Erreur fréquente** : en a, $-4ac$ avec $c$ négatif donne un nombre **positif**. **Où c'est enseigné** : R3 §5.

<a id="r4"></a>

## R4 · Logique, ensembles, Σ et Π

### POS.7 — Sommes avec Σ, somme double et produit avec Π
**Réponses** : a) `35` · b) `1111` · c) `18` · d) `48`.

- a) $3 + 5 + 7 + 9 + 11 = 35$.
- b) $1 + 10 + 100 + 1000 = 1111$ ($i$ commence à 0, et $10^0 = 1$).
- c) $\sum_{i=1}^{2} \sum_{j=1}^{3} ij = \left(\sum_{i=1}^{2} i\right)\left(\sum_{j=1}^{3} j\right) = 3 \times 6 = 18$ ; ou les six produits un par un : $1 + 2 + 3 + 2 + 4 + 6 = 18$.
- d) $\Pi$ multiplie : $2 \times 4 \times 6 = 48$.

**Erreur fréquente** : en a, ajouter le 1 une seule fois au lieu de cinq ; en b, commencer à $i = 1$ ; en d, additionner au lieu de multiplier. **Où c'est enseigné** : R4 §5.

### POS.8 — La négation d'une phrase avec « pour tout »
**Réponses** : a) `2` · b) `False`.

- a) Nier « pour tout $n$, $P(n)$ », c'est dire « il existe un $n$ pour lequel $P(n)$ est fausse » : ici, un entier $n$ tel que $n^2 + n$ est impair. (La phrase de départ est d'ailleurs vraie : $n^2 + n = n(n + 1)$ est le produit de deux entiers consécutifs, donc pair.)
- b) Faux : $x = -2$ vérifie $x^2 = 4$, et pourtant $x \neq 2$. Un seul contre-exemple suffit.

**Erreur fréquente** : en a, changer le quantificateur sans nier la conclusion (phrase 3), ou nier la conclusion en gardant « pour tout » (phrases 1 et 4, qui disent la même chose). **Où c'est enseigné** : R4 §2 (implication) et §3 (quantificateurs et négation).

<a id="r5"></a>

## R5 · Suites

### POS.9 — Terme et somme d'une suite géométrique
**Réponses** : a) `96` · b) `189` · c) `"3/2"`.

- a) $u_5 = u_0 \times q^5 = 3 \times 32 = 96$.
- b) Six termes, de $u_0$ à $u_5$ : $u_0 \frac{1 - q^6}{1 - q} = 3 \times \frac{1 - 64}{1 - 2} = 189$ (ou $3 + 6 + 12 + 24 + 48 + 96$).
- c) Raison $\frac{1}{3}$, premier terme 1 : $\frac{1}{1 - \frac{1}{3}} = \frac{3}{2}$.

**Erreur fréquente** : compter cinq termes au lieu de six, de $u_0$ à $u_5$. **Où c'est enseigné** : R5 §3 (suites géométriques), §4 (sommes) et §5 (somme infinie).

### POS.10 — Une suite définie par récurrence : premiers termes et limite
**Réponses** : a) `[4, 5, 5.5]` · b) `6`.

- a) $v_1 = 1 + 3 = 4$, $v_2 = 2 + 3 = 5$, $v_3 = 2{,}5 + 3 = 5{,}5$.
- b) Les termes s'approchent de 6 (5,75 ; 5,875…). Si la suite tend vers $\ell$, la relation de récurrence passe à la limite : $\ell = \frac{\ell}{2} + 3$, d'où $\ell = 6$.

**Erreur fréquente** : en a, multiplier par 2 au lieu de prendre la moitié. **Où c'est enseigné** : R5 §1 (suites par récurrence) et §5 (limite).

<a id="r6"></a>

## R6 · Exponentielle et logarithmes

### POS.11 — Propriétés de l'exponentielle et du logarithme
**Réponses** : a) `1` · b) `7` · c) `"1/2"` · d) `6`.

- a) $e^{3 + (-1) - 2} = e^{0} = 1$.
- b) $\ln 21 - \ln 3 = \ln \frac{21}{3} = \ln 7$.
- c) $\sqrt{e} = e^{1/2}$, et $\ln$ défait $\exp$ : $\ln\left(e^{1/2}\right) = \frac{1}{2}$.
- d) $2^6 = 64$, donc $\log_2 64 = 6$.

**Erreur fréquente** : $\ln a - \ln b = \ln(a - b)$ (faux : c'est un quotient) ; en c, oublier que la racine carrée est la puissance $\frac{1}{2}$. **Où c'est enseigné** : R6 §1 (exponentielle), §3 (logarithme népérien) et §4 (base 2).

### POS.12 — Résoudre des équations avec exp et ln
**Réponses** : a) `"ln(7)"` · b) `"exp(-1)"` · c) `2`.

- a) On applique $\ln$ aux deux membres : $x = \ln 7$ (environ 1,95).
- b) On applique $\exp$ aux deux membres : $x = e^{-1} = \frac{1}{e}$ (environ 0,37). `"1/e"` passe aussi.
- c) $e^{y} = 1$ seulement pour $y = 0$ : $3x - 6 = 0$, donc $x = 2$.

**Erreur fréquente** : en b, perdre le signe ($e^{1}$) ou répondre un nombre négatif (une exponentielle est toujours positive) ; en c, poser $3x - 6 = 1$. **Où c'est enseigné** : R6 §1 et §3.

<a id="r7"></a>

## R7 · Limites et dérivation

### POS.13 — Dériver trois fonctions, dont une composée
**Réponses** : a) `"10*x**4 - 6*x"` · b) `"x*exp(x)"` · c) `"-6*(5 - 2*x)**2"`.

- a) $(x^5)' = 5x^4$ et $(x^2)' = 2x$ : $2 \times 5x^4 - 3 \times 2x = 10x^4 - 6x$ ; la dérivée de la constante 1 est 0.
- b) Produit : $(uv)' = u'v + uv'$ avec $u = x - 1$ et $v = e^x$ : $e^x + (x - 1)e^x = x\,e^x$.
- c) Règle de la chaîne : $3(5 - 2x)^2 \times (-2) = -6(5 - 2x)^2$.

**Erreur fréquente** : en b, dériver chaque facteur et multiplier ($1 \times e^x$) ; en c, oublier le facteur $-2$, la dérivée de l'intérieur, ou son signe. **Où c'est enseigné** : R7 §5 (dérivées usuelles), §6 (produit) et §7 (règle de la chaîne).

### POS.14 — Tangente, variations et une limite
**Réponses** : a) `[9, -16]` · b) `"[-1 ; 1]"` · c) `2` · d) `3`.

- a) $f(2) = 8 - 6 = 2$ et $f'(x) = 3x^2 - 3$, donc $f'(2) = 9$. La tangente : $y = 9(x - 2) + 2 = 9x - 16$.
- b) $f'(x) = 3(x - 1)(x + 1)$ est négative entre $-1$ et $1$ et s'annule en $-1$ et en $1$ : le plus grand intervalle de décroissance est $[-1 ; 1]$.
- c) $f$ croît sur $]-\infty ; -1]$ puis décroît sur $[-1 ; 1]$ : le maximum local vaut $f(-1) = -1 + 3 = 2$.
- d) En $+\infty$, on factorise par le terme de plus haut degré : $\frac{x^2 (3 - \frac{1}{x})}{x^2 (1 + \frac{5}{x^2})} = \frac{3 - \frac{1}{x}}{1 + \frac{5}{x^2}}$, qui tend vers $\frac{3}{1} = 3$.

**Erreur fréquente** : en a, prendre $p = f(2)$ sans développer ; en d, conclure « $\frac{\infty}{\infty}$ » sans lever l'indétermination. **Où c'est enseigné** : R7 §1 (limites), §4 (tangente) et §8 (variations, extremums).

<a id="r8"></a>

## R8 · Probabilités de base

### POS.15 — Une probabilité avec un arbre
**Réponses** : a) `"3/10"` · b) `"3/5"`.

- a) $P(R_1 \cap R_2) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10}$ : au second tirage, il reste 2 rouges sur 4 boules.
- b) Rouge puis bleue, ou bleue puis rouge : $\frac{3}{5} \times \frac{2}{4} + \frac{2}{5} \times \frac{3}{4} = \frac{6}{20} + \frac{6}{20} = \frac{3}{5}$.

**Erreur fréquente** : calculer comme avec remise ($\frac{3}{5} \times \frac{3}{5}$), ou oublier un des deux ordres en b. **Où c'est enseigné** : R8 §4 (arbres pondérés).

### POS.16 — L'espérance et la variance d'une variable aléatoire
**Réponses** : a) `0.3` · b) `0.81`.

- a) $\mathbb{E}[X] = -2 \times 0{,}1 + 0 \times 0{,}4 + 1 \times 0{,}5 = 0{,}3$.
- b) $\mathbb{E}[X^2] = 4 \times 0{,}1 + 0 + 1 \times 0{,}5 = 0{,}9$, et $\mathbb{V}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = 0{,}9 - 0{,}09 = 0{,}81$.

**Erreur fréquente** : en a, faire la moyenne des valeurs sans les pondérer ; en b, oublier de soustraire $\mathbb{E}[X]^2$. **Où c'est enseigné** : R8 §6 et §7.

<a id="r9"></a>

## R9 · Géométrie du plan, vecteurs et trigonométrie

### POS.17 — Distance et produit scalaire dans le plan
**Réponses** : a) `13` · b) `10` · c) `True`.

- a) $AB = \sqrt{(7 - 2)^2 + (11 - (-1))^2} = \sqrt{25 + 144} = \sqrt{169} = 13$.
- b) $\vec{u} \cdot \vec{v} = 3 \times 4 + (-2) \times 1 = 10$.
- c) $\vec{u} \cdot \vec{w} = 3 \times 2 + (-2) \times 3 = 0$ : ils sont orthogonaux.

**Erreur fréquente** : en a, additionner les écarts ($5 + 12 = 17$) au lieu de passer par Pythagore, ou calculer $11 - 1$ au lieu de $11 - (-1)$. **Où c'est enseigné** : R9 §1 (distance) et §5 (produit scalaire).

### POS.18 — Cosinus d'un angle et radians
**Réponses** : a) `"5/6"` · b) `"1/2"` · c) `60`.

- a) $180°$ correspondent à $\pi$ : $150° = \frac{150}{180}\pi = \frac{5}{6}\pi$.
- b) $\frac{\pi}{6}$ correspond à $30°$, et $\sin 30° = \frac{1}{2}$.
- c) $\vec{u} \cdot \vec{v} = 2$, $\|\vec{u}\| = 2$ et $\|\vec{v}\| = \sqrt{1 + 3} = 2$ : $\cos\theta = \frac{2}{2 \times 2} = \frac{1}{2}$, donc $\theta = 60°$.

**Erreur fréquente** : en a, inverser le rapport ($\frac{6}{5}$) ; en c, répondre le cosinus au lieu de l'angle, ou confondre cosinus et sinus ($30°$). **Où c'est enseigné** : R9 §6 (radians, cosinus) et §7 (angle entre deux vecteurs).
