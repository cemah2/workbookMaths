# R4 · Logique, ensembles, Σ et Π — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 ⚖️ 🗣️ Pont, esprit critique et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R4.Q1 — Vrai, faux, ou pas une proposition ?
1. **Fausse** : $91 = 7 \times 13$.
2. **Pas une proposition** : un ordre n'est ni vrai ni faux.
3. **Pas une proposition** : sa valeur dépend de $x$, qui n'est pas fixé (c'est un prédicat).
4. **Vraie** : le « ou » est inclusif, et $2 + 2 = 4$ suffit.
5. **Fausse** : 10 n'est pas divisible par 4, et « et » demande les deux.
6. **Fausse** : $7 > 2$ est vraie, donc sa négation est fausse.

### R4.Q2 — Réciproque ou contraposée ?
1. **Réciproque** : hypothèse et conclusion échangées.
2. **Contraposée** : échangées **et** niées.
3. **Ni l'une ni l'autre** : on a nié sans échanger. C'est la contraposée de la réciproque, qui a donc la valeur de la réciproque.
4. **La contraposée**, la phrase 2.
5. **Faux** : le sol peut être mouillé sans qu'il pleuve (un arrosage) ; la réciproque est une autre phrase.
6. « **Il pleut et le sol n'est pas mouillé.** »

### R4.Q3 — Nier une phrase avec « pour tout »
1. « **Au moins un élève n'a pas rendu son devoir.** » La troisième tournure est ambiguë, la première dit beaucoup plus.
2. $\exists x \in \mathbb{R},\ x^2 + 1 \le 0$ (et cette négation est fausse : la phrase de départ est vraie).
3. $\forall n \in \mathbb{N},\ n \le 100$ ou $n$ est impair (« et » devient « ou », par De Morgan).
4. **Faux** : la négation de $x > 2$ est $x \le 2$.
5. **Vrai** : à $x$ donné, $y = -x$ convient ; $y$ dépend de $x$, ce qui est permis dans $\forall x\, \exists y$.

### R4.Q4 — Ensembles : vrai ou faux
1. **Vrai**.
2. **Faux** : $\{4\}$ est un ensemble ; $\{4\} \subset A$, mais ce n'est pas un élément de $A$.
3. **Vrai** : l'ensemble vide est inclus dans tout ensemble.
4. **Faux** : $A \cap \varnothing = \varnothing$.
5. **Faux** : $\{1, 1, 4\} = \{1, 4\}$, de cardinal 2.
6. **Vrai**.
7. **Vrai** : 1 n'est pas dans $]0 \;;\; 1[$, et c'est le seul nombre de $[1 \;;\; 2]$ qui aurait pu y être.

### R4.Q5 — Lire une somme Σ
1. $10 - 4 + 1 = $ **7** termes.
2. $2 + 3 + 4 + 5$.
3. **Vrai** : l'indice est muet.
4. $7n$ : $n$ termes égaux à 7.
5. **Faux** : avec $a = b = (1, 1)$, la somme des produits vaut 2 et le produit des sommes 4.
6. **Faux** : $\prod (2 a_k) = 2^n \prod a_k$, car le 2 est dans chacun des $n$ facteurs.

### R4.Q6 — Quel raisonnement pour quelle affirmation ?
1. **Contre-exemple** : 3 n'est pas une somme de deux carrés (les carrés plus petits que 3 sont 0 et 1, et $0 + 0$, $0 + 1$, $1 + 1$ ne font pas 3).
2. **Par l'absurde** (la démonstration d'Euclide : on suppose qu'il y en a un plus grand, et on fabrique un nombre premier plus grand).
3. **Récurrence** (initialisation : $7^0 - 1 = 0$ ; hérédité : $7^{n+1} - 1 = 7(7^n - 1) + 6$).
4. **Contraposée** : « si $n$ est pair, alors $n^2$ est pair », qui se démontre directement.
5. **Direct** : $x^2 - 6x + 9 = (x - 3)^2 \ge 0$.
6. **Disjonction de cas** : si $x \ge 0$, les deux membres valent $x$ ; si $x < 0$, ils valent $-x$.

### R4.Q7 — Les deux étapes d'une récurrence
1. L'**initialisation** et l'**hérédité** (puis la conclusion).
2. On suppose $P(n)$ vraie pour un entier $n \ge n_0$ fixé (l'hypothèse de récurrence), et on démontre $P(n + 1)$.
3. **Faux** : rien ne dit que $P(101)$ est vraie.
4. Par $n = 3$.
5. **Vrai** : « $4^n$ est divisible par 3 » a une hérédité juste et n'est vraie pour aucun $n$ (fiche §7).

### R4.Q8 — Ce qui manque dans une démonstration
1. Des **exemples** au lieu d'un argument. Il faut : soient $a = 2k + 1$ et $b = 2\ell + 1$ ; $a + b = 2(k + \ell + 1)$.
2. Le texte démontre la **réciproque** : il part de « $n^2$ pair ». Il fallait partir de $n = 2k$ : $n^2 = 4k^2 = 2(2k^2)$.
3. Un **cas oublié** (et $n$ n'est pas introduit) : tout entier n'est pas de la forme $2k$. Il manque le cas $n = 2k + 1$, où $n^2 + 3n = 4k^2 + 10k + 4 = 2(2k^2 + 5k + 2)$.
4. Le texte **part de la conclusion** : des « donc » dans le mauvais sens. Une rédaction juste part d'un fait vrai : $(\sqrt{a} - \sqrt{b})^2 \ge 0$, donc $a - 2\sqrt{ab} + b \ge 0$, donc $\sqrt{ab} \le \frac{a + b}{2}$.

<a id="rappels"></a>

## 🔁 Rappels

### R4.R1 — Résoudre une inéquation (R2)
1. $7 - 3x < 1 \iff -3x < -6 \iff x > 2$ (division par $-3$ : le sens change). Solutions : $]2 \;;\; +\infty[$.
2. $2x - 2 \ge 5x + 4 \iff -3x \ge 6 \iff x \le -2$ : $]-\infty \;;\; -2]$.
3. La négation est $x < 2$, vérifiée par $]-\infty \;;\; 2[$ : c'est le **complémentaire** de $[2 \;;\; +\infty[$ dans $\mathbb{R}$.

### R4.R2 — Composer deux fonctions (R3)
1. $(f \circ g)(2) = f(5) = -2$ et $(g \circ f)(2) = g(1) = 2$.
2. $(f \circ g)(x) = 3 - (x^2 + 1) = 2 - x^2$ et $(g \circ f)(x) = (3 - x)^2 + 1 = x^2 - 6x + 10$.
3. **Faux** : $x = 2$ est un contre-exemple ($-2 \ne 2$).

### R4.R3 — Simplifier des fractions (R1)
1. $\frac{3}{6} + \frac{2}{6} + \frac{1}{6} = 1$.
2. $\frac{1}{3} - \frac{1}{4} = \frac{4 - 3}{12} = \frac{1}{12}$, et $\frac{1}{k} - \frac{1}{k + 1} = \frac{(k + 1) - k}{k(k + 1)} = \frac{1}{k(k + 1)}$.
3. Même dénominateur : $\frac{6}{12} + \frac{2}{12} + \frac{1}{12} = \frac{3}{4}$. Avec la question 2 : $\left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) = 1 - \frac{1}{4} = \frac{3}{4}$, une somme télescopique.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R4.1 — Tables de vérité de « et », « ou », « non » et de l'implication

**Réponses** : a) `[False, True, True, True]` · b) `[False, True, True, True]` · c) `True` · d) `[True, False, True, True]` · e) `[True, True, False, True]` · f) `[True, False, True, True]` · g) `"df"` · h) `8` · i) `3`.

**Démarche.**

| P | Q | non P | non Q | P et Q | a) non (P et Q) | b) (non P) ou (non Q) | d) P ⇒ Q | e) Q ⇒ P | f) non Q ⇒ non P |
|---|---|---|---|---|---|---|---|---|---|
| V | V | F | F | V | F | F | V | V | V |
| V | F | F | V | F | V | V | F | V | F |
| F | V | V | F | F | V | V | V | F | V |
| F | F | V | V | F | V | V | V | V | V |

- c) Les colonnes a et b sont égales : c'est une loi de De Morgan.
- d), e), f) Une implication n'est fausse que sur la ligne « hypothèse vraie, conclusion fausse » : VF pour d, FV pour e (hypothèse Q vraie, conclusion P fausse), VF pour f (non Q vraie, non P fausse). d et f ont la même colonne : une implication et sa contraposée sont équivalentes.
- h) $2^3 = 8$ lignes.
- i) « non R » ne garde que les 4 lignes où R est fausse ; parmi elles, « P ou Q » est vraie sauf quand P et Q sont fausses : 3 lignes (VVF, VFF, FVF).

**Erreurs fréquentes.** Lire « non (P et Q) » comme « ni P ni Q » ; mettre F sur les lignes où l'hypothèse est fausse ; écrire les lignes dans un autre ordre (la réponse dépend de l'ordre VV, VF, FV, FF).

**Variante.** La colonne de $P \Leftrightarrow Q$ ? *Réponse* : `[True, False, False, True]` : l'équivalence est vraie quand P et Q ont la même valeur.

### Ex R4.2 — Réciproque, contraposée, négation : écrire les trois

**Réponses** : a) `[True, False, True, False]` · b) `[False, True, False, True]` · c) `[False, False, False, True]` · d) `[True, True, True, False]` · e) `9` · f) `-6`.

**Démarche.**
- A. Réciproque : « pour tout entier $n$, si $n$ est divisible par 3, alors $n$ est divisible par 6 », fausse (9). Contraposée : « si $n$ n'est pas divisible par 3, alors $n$ n'est pas divisible par 6 », vraie comme l'implication ($n = 6m = 3 \times 2m$). Négation : « il existe un entier divisible par 6 et pas par 3 », fausse.
- B. L'implication est fausse : $x = -6$ donne $x^2 = 36 > 25$ et pourtant $x \le 5$. Réciproque : « si $x > 5$, alors $x^2 > 25$ », vraie (deux nombres positifs, et le carré est croissant sur les positifs). Contraposée : « si $x \le 5$, alors $x^2 \le 25$ », fausse (même contre-exemple). Négation : « il existe un réel $x$ tel que $x^2 > 25$ et $x \le 5$ », vraie.
- C. L'implication est fausse (9 est impair et vaut $3 \times 3$). Réciproque : « si $n$ est premier, alors $n$ est impair », fausse (2). Contraposée : « si $n$ n'est pas premier, alors $n$ est pair », fausse (9). Négation : « il existe un entier $n \ge 2$ impair et non premier », vraie.
- D. $3x - 2 = 10 \iff 3x = 12 \iff x = 4$ : l'implication et sa réciproque sont vraies (une équivalence), la contraposée aussi, la négation est fausse.
- e) Les impairs de 2 à 10 sont 3, 5, 7, 9 ; seul 9 n'est pas premier.
- f) Il faut $x^2 > 25$ et $x \le 5$, avec $x$ entier négatif : $x \le -6$. Le plus grand est $-6$ ($-5$ donne $x^2 = 25$, pas strictement plus grand).

**Erreurs fréquentes.** Nier une implication par une implication (« si non P alors non Q ») ; oublier le « pour tout » caché, qui devient « il existe » dans la négation ; oublier les nombres négatifs dans B.

**Variante.** « Pour tout réel $x$, si $x \ge 3$, alors $x^2 \ge 9$ » : valeurs de l'implication, de la réciproque, de la contraposée et de la négation ? *Réponse* : `[True, False, True, False]` (la réciproque tombe pour $x = -3$).

### Ex R4.3 — Nier des phrases à deux quantificateurs

**Réponses** : a) `2` · b) `True` · c) `1` · d) `False` · e) `[False, True]` · f) `1` · g) `True`.

**Démarche.**
- a) On change chaque quantificateur dans l'ordre (∀x devient ∃x, ∃y devient ∀y) et on nie $y > x$ en $y \le x$.
- b) Vraie : à $x$ donné, $y = x + 1$ convient. (Sa négation, « un réel plus grand ou égal à tous les réels », est fausse.)
- c) ∃M devient ∀M, ∀x devient ∃x, et $x^2 \le M$ devient $x^2 > M$.
- d) Fausse : pour tout $M$, $x = \lvert M \rvert + 1$ donne $x^2 \ge x > \lvert M \rvert \ge M$. Le carré n'est pas majoré.
- e) La première est fausse : $x = -1$ n'est le carré d'aucun réel. La seconde est vraie : $y = 0$ donne $x \times 0 = 0$ pour tout $x$. Un $\exists y\, \forall x$ peut être vrai, quand un même $y$ convient à tous les $x$.
- f) « Pour tout $\varepsilon > 0$ » devient « il existe $\varepsilon > 0$ » : la condition $\varepsilon > 0$ fait partie du domaine du quantificateur, elle ne se nie pas. « Il existe $N$ » devient « pour tout $N$ », et $\frac{1}{N} < \varepsilon$ devient $\frac{1}{N} \ge \varepsilon$.
- g) Vraie : à $\varepsilon > 0$ donné, tout entier $N > \frac{1}{\varepsilon}$ donne $\frac{1}{N} < \varepsilon$. C'est la phrase « $\frac{1}{N}$ devient aussi petit qu'on veut », que R5 appellera « $\frac{1}{N}$ tend vers 0 ».

**Erreurs fréquentes.** Ne changer que le premier quantificateur ; échanger l'ordre des variables ; nier la condition $\varepsilon > 0$ (phrase 3 de f) ; nier $\le$ en $\ge$ au lieu de $>$.

**Variante.** La négation de « $\forall n \in \mathbb{N},\ \exists m \in \mathbb{N},\ m = 2n$ » ? *Réponse* : « $\exists n \in \mathbb{N},\ \forall m \in \mathbb{N},\ m \ne 2n$ », fausse (la phrase de départ est vraie : $m = 2n$).

### Ex R4.4 — Union, intersection, complémentaire et cardinal

**Réponses** : a) `[]` · b) `14` · c) `[17, 19, 23]` · d) `16` · e) `15` · f) `[1, 4, 9, 16]` · g) `12` · h) `6`.

**Démarche.** $A = \{1, 4, 9, 16, 25\}$ (5 éléments), $B = \{2, 3, 5, 7, 11, 13, 17, 19, 23\}$ (9 éléments), $C = \{17, 18, \dots, 25\}$ (9 éléments).
- a) Un carré $k^2$ avec $k \ge 2$ a le diviseur $k$, et 1 n'est pas premier : $A \cap B = \varnothing$.
- b) $5 + 9 - 0 = 14$.
- c) Les premiers de 17 à 25 : 17, 19, 23.
- d) $25 - 9 = 16$.
- e) $9 + 9 - 3 = 15$ ; en listant : $\{2, 3, 5, 7, 11, 13\}$ et les 9 éléments de $C$, soit 15.
- f) On retire de $A$ ce qui est dans $C$, c'est-à-dire 25.
- g) $\lvert A \cup C \rvert = 5 + 9 - 1 = 13$ (25 est dans les deux), donc $\lvert \overline{A \cup C} \rvert = 25 - 13 = 12$. Par De Morgan, c'est aussi $\lvert \bar{A} \cap \bar{C} \rvert$ : les nombres de 1 à 16 qui ne sont pas des carrés, $16 - 4 = 12$.
- h) $17 + 12 - 5 = 24$ élèves font au moins une activité ; $30 - 24 = 6$.

**Erreurs fréquentes.** Compter 1 parmi les premiers ; oublier de retirer l'intersection (e, g) ; répondre $\lvert A \cup C \rvert$ au lieu de son complémentaire.

**Variante.** Combien d'éléments de $E$ ne sont ni premiers ni carrés ? *Réponse* : $25 - 14 = 11$.

### Ex R4.5 — Produit cartésien et couples

**Réponses** : a) `6` · b) `8` · c) `3` · d) `2` · e) `False` · f) `24` · g) `False`.

**Démarche.**
- a) $2 \times 3 = 6$ couples.
- b) $2 \times 2 \times 2 = 8$ triplets (ce sont les lignes d'une table de vérité à trois variables, avec 1 pour V et 0 pour F).
- c) $(1, 2)$, $(1, 3)$, $(2, 3)$.
- d) $(0, 2)$ et $(1, 1)$.
- e) La seconde coordonnée, 0, n'est pas dans $B$.
- f) $3 \times 4 \times 2 = 24$ menus.
- g) $(0, 2) \in A \times B$, mais $(0, 2) \notin B \times A$ (la première coordonnée d'un couple de $B \times A$ est dans $B$).

**Erreurs fréquentes.** Additionner au lieu de multiplier ; compter $(1, 1)$ dans c (l'inégalité est stricte) ; confondre le couple $(1, 0)$ et l'ensemble $\{0, 1\}$.

**Variante.** $\lvert B \times B \rvert$, et combien de ses couples ont deux coordonnées égales ? *Réponse* : 9 couples, dont 3 de la forme $(x, x)$.

### Ex R4.6 — Calculer des sommes Σ et des produits Π

**Réponses** : a) `51` · b) `54` · c) `1` · d) `"25/12"` · e) `5` · f) `60` · g) `16` · h) `-1` · i) `24`.

**Démarche.**
- a) $1 + 4 + 7 + 10 + 13 + 16 = 51$.
- b) $4 + 9 + 16 + 25 = 54$.
- c) $1 - 1 + 1 - 1 + 1 = 1$ (5 termes, de $i = 0$ à 4).
- d) $\frac{12}{12} + \frac{6}{12} + \frac{4}{12} + \frac{3}{12} = \frac{25}{12}$.
- e) $\frac{2}{1} \times \frac{3}{2} \times \frac{4}{3} \times \frac{5}{4} = 5$ : chaque numérateur se simplifie avec le dénominateur suivant (un produit télescopique).
- f) $3 \times 4 \times 5 = 60$.
- g) 8 termes égaux à 2 : 16.
- h) $(-1)^5 = -1$.
- i) $30 - 7 + 1 = 24$.

**Erreurs fréquentes.** Oublier une borne (b, g, i) ; ne retirer le $-2$ qu'une fois dans a ; additionner au lieu de multiplier dans h.

**Variante.** $\prod_{k=1}^{4} \frac{k + 1}{k}$ ? *Réponse* : $\frac{2}{1} \times \frac{3}{2} \times \frac{4}{3} \times \frac{5}{4} = 5$ : le même produit, écrit avec un autre indice.

### Ex R4.7 — Développer, réindexer et découper une somme Σ ; calculer une somme double

**Réponses** : a) `140` · b) `155` · c) `385` · d) `"n**2 + 4*n"` · e) `[1, 6]` · f) `52` · g) `70` · h) `"9/10"`.

**Démarche.**
- a) $2 \sum_{k=1}^{10} k + \sum_{k=1}^{10} 3 = 2 \times 55 + 30 = 140$.
- b) $\sum_{k=1}^{20} k - \sum_{k=1}^{10} k = 210 - 55 = 155$.
- c) Avec $k = j + 1$, quand $j$ va de 0 à 9, $k$ va de 1 à 10 : $\sum_{k=1}^{10} k^2 = \frac{10 \times 11 \times 21}{6} = 385$.
- d) $2 \times \frac{n(n+1)}{2} + 3n = n^2 + n + 3n = n^2 + 4n$. Contrôle : pour $n = 10$, $100 + 40 = 140$, comme en a.
- e) Avec $j = k - 2$ : quand $k$ va de 3 à 8, $j$ va de 1 à 6.
- f) À $i$ fixé, $\sum_{j=1}^{4} (i + 2j) = 4i + 2 \times 10 = 4i + 20$ ; puis $24 + 28 = 52$.
- g) Le terme est un produit d'un facteur en $i$ et d'un facteur en $j$ : $\left(\sum_{i=1}^{4} i\right)\left(\sum_{j=0}^{2} 2^j\right) = 10 \times 7 = 70$.
- h) Somme télescopique : $1 - \frac{1}{10} = \frac{9}{10}$.

**Erreurs fréquentes.** Ajouter la constante une seule fois (a, d) ; retirer la somme jusqu'à 11 au lieu de 10 (b) ; garder les anciennes bornes après un changement d'indice (c, e) ; oublier $2^0 = 1$ (g).

**Variante.** $\sum_{k=1}^{n} (6k - 1)$ en fonction de $n$ ? *Réponse* : $3n(n + 1) - n = 3n^2 + 2n$.

### Ex R4.8 — Trouver un contre-exemple

**Réponses** : a) `2` · b) `4` · c) `"]0 ; 1["` · d) `12` · e) `5` · f) `[0]`.

**Démarche.**
- a) $n = 1$ : $2 > 1$, vrai ; $n = 2$ : $4 > 4$, faux (l'inégalité est stricte).
- b) $n = 2$ : 3, $n = 3$ : 7, premiers ; $n = 4$ : $15 = 3 \times 5$.
- c) $x^2 < x \iff x^2 - x < 0 \iff x(x - 1) < 0$, vrai quand les deux facteurs sont de signes contraires : $0 < x < 1$.
- d) 12 est divisible par 4 et par 6, pas par 24. (Divisible par 4 et par 6, c'est être divisible par 12, leur plus petit multiple commun.)
- e) Une somme impaire demande un premier pair, donc 2 : la plus petite est $2 + 3 = 5$.
- f) $(x + 1)^2 = x^2 + 2x + 1$, donc l'égalité équivaut à $2x = 0$ : seulement $x = 0$.

**Erreurs fréquentes.** Oublier que l'inégalité de a est stricte ; répondre $[0 \;;\; 1]$ en c (en 0 et en 1, $x^2 = x$, donc $x^2 \ge x$ est vraie) ; répondre 24 en d.

**Variante.** « Pour tout entier $n \ge 1$, $n^2 + 1$ est premier » : le plus petit contre-exemple ? *Réponse* : 3 ($n = 1$ donne 2, $n = 2$ donne 5, mais $n = 3$ donne $10 = 2 \times 5$).

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R4.9 — Démonstration directe : la somme de deux nombres pairs est paire

**Démonstration.**
1. « Pour tous entiers $a$ et $b$, si $a$ et $b$ sont pairs, alors $a + b$ est pair. »
2. Soient $a$ et $b$ deux entiers pairs. Par définition, il existe des entiers $k$ et $\ell$ tels que $a = 2k$ et $b = 2\ell$. Alors $a + b = 2k + 2\ell = 2(k + \ell)$. Comme $k + \ell$ est un entier, $a + b$ est pair. ∎ Deux lettres sont nécessaires : avec $a = 2k$ et $b = 2k$, on aurait supposé $a = b$, et démontré seulement que $2a$ est pair.
3. Soient $a = 2k$ pair et $b = 2\ell + 1$ impair. Alors $a + b = 2(k + \ell) + 1$, impair. ∎
4. Soient $a = 2k$ pair et $b$ un entier quelconque. Alors $ab = 2(kb)$, et $kb$ est un entier : $ab$ est pair. ∎
5. Deux exemples ne couvrent pas tous les couples d'entiers pairs : une propriété peut être vraie sur des exemples et fausse ailleurs (R4.21).

**Grille de relecture.**
- L'énoncé est écrit avec un quantificateur (« pour tous entiers »).
- Les objets sont introduits (« Soient… ») avec leur hypothèse, et la définition de « pair » est **utilisée** (il existe $k$ tel que…), avec deux lettres différentes.
- Le calcul aboutit à la forme $2 \times (\text{entier})$, et la phrase dit pourquoi c'est un entier.
- Une conclusion, et un signe de fin.

**Erreurs fréquentes.** Une seule lettre $k$ pour les deux nombres ; s'arrêter à $2k + 2\ell$ sans factoriser ; oublier de dire que $k + \ell$ est un entier.

**Variante.** Démontrer que la somme de deux impairs est paire. *Réponse* : $(2k + 1) + (2\ell + 1) = 2(k + \ell + 1)$.

### Ex R4.10 — Par contraposée : si n² est pair, alors n est pair

**Démonstration.**
1. « Pour tout entier $n$, si $n$ est impair, alors $n^2$ est impair » (non pair = impair).
2. Soit $n$ un entier impair : $n = 2k + 1$ avec $k$ entier. Alors $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, impair. La contraposée est démontrée ; comme elle est équivalente à l'implication, celle-ci est vraie : si $n^2$ est pair, alors $n$ est pair. ∎
3. La réciproque, « si $n$ est pair, alors $n^2$ est pair », est vraie (R4.9, question 4, avec $b = n$). Donc : pour tout entier $n$, $n$ est pair $\Leftrightarrow$ $n^2$ est pair.
4. De $n^2 = 2k$, on ne sait pas exprimer $n$ (écrire $n = \sqrt{2k}$ ne dit rien de sa parité) ; la contraposée part de $n$, dont on connaît la forme.
5. Contraposée : « si $n$ n'est pas divisible par 3, alors $n^2$ n'est pas divisible par 3 ». Soit $n$ non divisible par 3. *Premier cas* : $n = 3k + 1$, alors $n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$. *Second cas* : $n = 3k + 2$, alors $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$. Dans les deux cas, $n^2$ laisse le reste 1 dans la division par 3 : il n'est pas divisible par 3. ∎

**Grille de relecture.**
- La contraposée est écrite **avant** d'être démontrée, et le texte dit qu'elle équivaut à l'implication.
- Le calcul part de $n = 2k + 1$ et aboutit à $2(\dots) + 1$.
- La réciproque est étudiée à part, et l'équivalence écrite avec ⇔.
- En 5, les deux cas sont annoncés, couvrent tous les entiers non divisibles par 3, et sont traités.

**Erreurs fréquentes.** Démontrer la réciproque (« si $n$ est pair, $n^2$ l'est ») en croyant démontrer l'implication ; oublier le cas $3k + 2$.

**Variante.** Démontrer que si $n^2$ est impair, alors $n$ est impair. *Réponse* : contraposée, « si $n$ est pair, alors $n^2$ est pair », vraie par R4.9.

### Ex R4.11 — Par l'absurde : √2 n'est pas une fraction

**Démonstration.**
1. Une fraction $\frac{p}{q}$ se simplifie en divisant $p$ et $q$ par leur plus grand diviseur commun (R1) ; on obtient la même valeur, avec une fraction irréductible.
2. Supposons par l'absurde $\sqrt{2} = \frac{p}{q}$, avec $p$ et $q$ entiers sans diviseur commun autre que 1 et $-1$, et $q \ne 0$. En élevant au carré : $2 = \frac{p^2}{q^2}$, donc $p^2 = 2q^2$. $p^2$ est pair, donc $p$ est pair (R4.10).
3. Écrivons $p = 2r$. Alors $4r^2 = 2q^2$, donc $q^2 = 2r^2$ : $q^2$ est pair, donc $q$ est pair (R4.10).
4. $p$ et $q$ sont pairs : 2 est un diviseur commun, ce qui contredit l'irréductibilité. L'hypothèse est donc fausse : $\sqrt{2}$ n'est pas une fraction (c'est un nombre irrationnel). ∎
5. Supposons $\sqrt{3} = \frac{p}{q}$, irréductible. Alors $p^2 = 3q^2$ : $p^2$ est divisible par 3, donc $p$ aussi (R4.10, question 5). Avec $p = 3r$ : $9r^2 = 3q^2$, donc $q^2 = 3r^2$, et $q$ est divisible par 3. Contradiction. ∎
6. Avec $\sqrt{4}$ : $p^2 = 4q^2$ donne bien $p$ pair, $p = 2r$, puis $4r^2 = 4q^2$, soit $q^2 = r^2$, qui ne dit rien de la parité de $q$. L'étape 3 échoue, et c'est heureux : $\sqrt{4} = 2 = \frac{2}{1}$ est une fraction.

**Grille de relecture.**
- L'hypothèse absurde est écrite clairement, avec « irréductible » et $q \ne 0$, et la raison pour laquelle on peut la supposer.
- Les deux usages de R4.10 sont cités.
- La contradiction est nommée (« 2 divise $p$ et $q$ »), puis la conclusion revient à l'énoncé.

**Erreurs fréquentes.** Oublier de supposer la fraction irréductible (il n'y a alors plus de contradiction) ; écrire « $p^2$ pair donc $p$ pair » sans justification ; conclure « $\sqrt{2}$ n'existe pas » au lieu de « n'est pas une fraction ».

**Variante.** $\sqrt{2} + 1$ est-il une fraction ? *Réponse* : non : si $\sqrt{2} + 1 = \frac{a}{b}$, alors $\sqrt{2} = \frac{a - b}{b}$ serait une fraction.

### Ex R4.12 — Par récurrence : 1 + 2 + … + n = n(n + 1)/2

**Démonstration.**
1. $P(1)$ : $1 = \frac{1 \times 2}{2}$ ; $P(2)$ : $3 = \frac{2 \times 3}{2}$ ; $P(3)$ : $6 = \frac{3 \times 4}{2}$. Cela ne suffit pas : trois cas ne disent rien du quatrième.
2. *Initialisation.* Pour $n = 1$, la somme a un seul terme, 1, et $\frac{1 \times 2}{2} = 1$ : $P(1)$ est vraie.
3. *Hérédité.* Soit $n \ge 1$ tel que $P(n)$ est vraie. Alors
$$\sum_{k=1}^{n+1} k = \sum_{k=1}^{n} k + (n + 1) = \frac{n(n+1)}{2} + (n + 1) = (n + 1)\left(\frac{n}{2} + 1\right) = \frac{(n + 1)(n + 2)}{2},$$
en utilisant $P(n)$ à la deuxième égalité. C'est $P(n + 1)$.
4. *Conclusion.* Par récurrence, $P(n)$ est vraie pour tout entier $n \ge 1$. ∎
5. $\sum_{k=1}^{n} (4k + 1) = 4 \times \frac{n(n+1)}{2} + n = 2n^2 + 3n$.

**Grille de relecture.**
- $P(n)$ est défini, avec le domaine de $n$.
- L'initialisation calcule les **deux** membres en $n = 1$.
- L'hérédité dit « soit $n \ge 1$ tel que $P(n)$ », isole le dernier terme, dit où l'hypothèse de récurrence sert, et aboutit exactement à la formule de $P(n + 1)$.
- La conclusion cite le principe de récurrence.

**Erreurs fréquentes.** Supposer $P(n)$ « pour tout $n$ » dans l'hérédité (c'est supposer ce qu'on démontre) ; oublier le terme $n + 1$ ; s'arrêter à $\frac{n(n+1)}{2} + n + 1$ sans retrouver la forme attendue.

**Variante.** Une autre démonstration, directe (celle de la figure de la fiche) : écris $S = 1 + 2 + \dots + n$ et $S = n + (n - 1) + \dots + 1$, additionne terme à terme. *Réponse* : chaque colonne vaut $n + 1$, il y en a $n$, donc $2S = n(n + 1)$.

### Ex R4.13 — Par récurrence : 2ⁿ ≥ n + 1

**Démonstration.**
1. *Initialisation* : $2^0 = 1 \ge 0 + 1$. *Hérédité* : soit $n \ge 0$ tel que $2^n \ge n + 1$. Alors $2^{n+1} = 2 \times 2^n \ge 2(n + 1)$ (on multiplie par 2, positif). Or $2(n + 1) - (n + 2) = n \ge 0$, donc $2(n + 1) \ge n + 2$, et $2^{n+1} \ge (n + 1) + 1$. *Conclusion* : par récurrence, $2^n \ge n + 1$ pour tout $n \ge 0$. ∎
2. Pour $n = 0$ ($1 = 1$) et $n = 1$ ($2 = 2$). Dès $n \ge 1$, l'hérédité donne $2^{n+1} \ge 2(n + 1) > n + 2$ (car $n > 0$) : l'inégalité est stricte pour $n \ge 2$.
3. $2^n$ : 1, 2, 4, 8, 16, 32 ; $n^2$ : 0, 1, 4, 9, 16, 25. En $n = 3$, $8 < 9$ : $P(3)$ est fausse, on ne peut pas initialiser là. En $n = 4$ : $16 \ge 16$.
4. $2n^2 - (n + 1)^2 = n^2 - 2n - 1 = (n - 1)^2 - 2$. Pour $n \ge 3$, $(n - 1)^2 \ge 4 > 2$, donc $2n^2 \ge (n + 1)^2$.
5. *Initialisation* : $2^4 = 16 \ge 4^2$. *Hérédité* : soit $n \ge 4$ tel que $2^n \ge n^2$. Alors $2^{n+1} = 2 \times 2^n \ge 2n^2 \ge (n + 1)^2$, d'après la question 4 (on a bien $n \ge 3$). *Conclusion* : $2^n \ge n^2$ pour tout $n \ge 4$. ∎

**Grille de relecture.**
- Chaque inégalité est justifiée (multiplier par un positif, signe d'une différence).
- L'hérédité de la question 5 utilise **et** l'hypothèse de récurrence **et** la question 4, en vérifiant que $n \ge 3$.
- Le point de départ est justifié par le calcul de la question 3.

**Erreurs fréquentes.** Écrire $2^{n+1} = 2^n + 1$ ; initialiser la seconde récurrence en $n = 0$ (elle est vraie pour $n = 0, 1, 2$, fausse pour $n = 3$ : la chaîne casse) ; utiliser la question 4 pour $n = 2$, où elle est fausse.

**Variante.** Pour tout $n \ge 1$, $3^n \ge 2n + 1$ ? *Réponse* : oui ; hérédité : $3^{n+1} \ge 3(2n + 1) = 6n + 3 \ge 2n + 3$.

<a id="reflexion"></a>

## 🔗 ⚖️ 🗣️ Pont, esprit critique et explication

### Ex R4.14 — Écrire la loss moyenne d'un modèle avec Σ

**Réponses** : a) `-2` · b) `"6/5"` (ou `1.2`) · c) `"4/5"` (ou `0.8`) · d) `"106/5"` (ou `21.2`) · e) `"14/5"` (ou `2.8`) · f) `1`.

**Démarche.** $\text{MSE} = \frac{1}{n}\sum_{i=1}^{n} (\hat{y}_i - y_i)^2$ et $\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} \lvert \hat{y}_i - y_i \rvert$. Les erreurs sont $e = (1, 0, -1, -2, 0)$.
- a) $1 + 0 - 1 - 2 + 0 = -2$.
- b) $\frac{1 + 0 + 1 + 4 + 0}{5} = \frac{6}{5}$.
- c) $\frac{1 + 0 + 1 + 2 + 0}{5} = \frac{4}{5}$.
- d) La cinquième erreur devient $16 - 6 = 10$ : $\frac{6 + 100}{5} = \frac{106}{5}$.
- e) $\frac{4 + 10}{5} = \frac{14}{5}$.
- f) La MSE est multipliée par $\frac{106}{6} \approx 17{,}7$, la MAE par $\frac{14}{4} = 3{,}5$.

La moyenne des erreurs signées ne mesure rien : des erreurs de signes contraires se compensent, et un modèle qui se trompe de $+10$ puis de $-10$ aurait une erreur moyenne nulle. La MSE élève au carré : elle donne un poids énorme aux grosses erreurs, donc aux valeurs aberrantes.

**Erreurs fréquentes.** Calculer $y_i - \hat{y}_i$ (le signe de a change, les carrés non) ; oublier de diviser par $n$ ; élever au carré la somme au lieu de chaque terme.

**Variante.** Avec les cinq erreurs $(2, -2, 2, -2, 0)$, que valent la moyenne des erreurs et la MAE ? *Réponse* : 0 et $\frac{8}{5}$.

### Ex R4.15 — Repérer un raisonnement fautif dans une phrase de presse

**Réponses possibles.**
1. **La réciproque prise pour l'implication.** La règle « efficace ⇒ les patients vont mieux » ne permet pas de conclure « les patients vont mieux ⇒ efficace » : ils pouvaient aller mieux sans le traitement. Phrase juste : « Nos patients vont mieux, ce qui est compatible avec un traitement efficace ; il faut un groupe témoin pour conclure. »
2. **La réciproque, encore.** « Gagner ⇒ avoir acheté un billet » est vrai ; « avoir acheté un billet ⇒ gagner » est faux. Acheter un billet est une condition nécessaire, pas suffisante. Phrase juste : « Sans billet, on ne peut pas gagner. »
3. **Une négation mal formée.** La négation de « promettre d'augmenter » est « ne pas promettre d'augmenter », qui laisse trois possibilités (baisser, garder, ne rien dire). Phrase juste : « Le maire n'a pas promis d'augmenter les impôts. »
4. **La négation de « pour tout ».** La négation de « tous les adolescents lisent peu » est « **au moins un** adolescent lit beaucoup », pas « aucun ne lit peu ». Phrase juste : « Certains adolescents lisent beaucoup. »
5. **Des exemples pris pour une démonstration** (et un « pour tout » tiré de trois cas). Phrase juste : « Notre méthode a marché dans les trois écoles testées ; il faudra d'autres essais pour savoir si elle marche ailleurs. »

**Grille.** Pour chaque phrase : la règle écrite sous forme logique, le nom de l'erreur, une phrase corrigée qui ne dit que ce qui est justifié.

### Ex R4.16 — Expliquer la différence entre « si » et « si et seulement si »

**Exemple de réponse.**

> « Si », c'est une flèche dans un seul sens. « Si c'est un chat, alors c'est un mammifère » est vrai, mais un mammifère n'est pas forcément un chat : la phrase à l'envers, la réciproque, est fausse. « Si et seulement si », c'est la flèche dans les deux sens : « un nombre est pair si et seulement si son dernier chiffre est 0, 2, 4, 6 ou 8 » marche dans un sens comme dans l'autre. Dire « P si et seulement si Q », c'est dire deux choses : si P alors Q, et si Q alors P. Pour une équation, ça change tout : $x = 3$ entraîne $x^2 = 9$, mais $x^2 = 9$ n'entraîne pas $x = 3$ (il y a aussi $-3$). Quand une étape n'est qu'un « si », il faut vérifier les solutions trouvées.

**Grille.** Une bonne réponse : (1) une implication courante dont la réciproque est fausse ; (2) une équivalence ; (3) « dans les deux sens » dit avec ses mots ; (4) la conséquence pour les équations ; (5) huit lignes au plus.

<a id="notebook"></a>

## Notebook

### Ex R4.17 — Tables de vérité et implication · `truth_table`, `implies`

**Réponses** : la colonne de « (p et q) ⇒ r » est `[True, False, True, True, True, True, True, True]` ; une table à 4 variables a 16 lignes ; `truth_table(formula, 0)` lève `ValueError`.

**Démarche.** « (p et q) ⇒ r » n'est fausse que si p et q sont vraies et r fausse : la ligne VVF, la deuxième dans l'ordre de `itertools.product`. En code : la `ValueError` d'abord, puis `for values in itertools.product([True, False], repeat=n):` et `rows.append((values, formula(*values)))`. `implies(p, q)` vaut `(not p) or q`.

**Erreurs fréquentes.** L'ordre `[False, True]`, qui donne les lignes à l'envers ; `implies` écrit `p and q`, ou `(not q) or p` (la réciproque) ; `formula(values)` au lieu de `formula(*values)` (la formule reçoit un seul argument, le tuple).

### Ex R4.19 — Chercher un contre-exemple de 0 à N · `find_counterexample`

**Réponses** : a) `10` ($9! = 362\,880 < 10^6 \le 10! = 3\,628\,800$) · b) `None`, donc `True` · c) `0` · d) `20`.

**Démarche.** `for n in range(n_max + 1):` puis `if not predicate(n): return n`, et `return None` après la boucle. Pour la copie : $n^3 - n = (n - 1)\,n\,(n + 1)$ est le produit de trois entiers consécutifs ; l'un d'eux est divisible par 3 (selon que $n$ laisse le reste 0, 1 ou 2, c'est $n$, $n - 1$ ou $n + 1$), donc le produit aussi. La réponse de b) ne démontrait rien au-delà de 1 000.

**Erreurs fréquentes.** `range(1, n_max + 1)` (0 n'est pas essayé), `range(n_max)` ($n_{\max}$ n'est pas essayé) ; rendre `False` au lieu de `None` ; rendre le dernier $n$ où la propriété est vraie.

### Ex R4.21 — Prédire : n² + n + 41 est-il toujours un nombre premier ?

**Réponses** : a) `False` · b) `40` · c) `40`.

**Démarche.** Les valeurs pour $n = 0$ à 39 sont toutes premières ; pour $n = 40$, $40^2 + 40 + 41 = 40 \times 41 + 41 = 41^2 = 1\,681$. Pour $n = 41$ : $41^2 + 41 + 41 = 41 \times 43$, divisible par 41 sans calcul. Quarante succès de suite, et la phrase « pour tout $n$ » est fausse.

**Erreurs fréquentes.** Conclure « toujours premier » après quelques essais ; compter 39 nombres de 0 à 39.

### Ex R4.20 — Les ensembles de Python : `set`, `|`, `&`, `-`

**Réponses** : a) `11` · b) `{'a', 'e', 'i', 'q', 's', 't', 'u'}` · c) `9` · d) `True` · e) `{'h', 'm'}` · f) `True`.

**Démarche.** Chaque réponse tient en une ligne : `len(set("anticonstitutionnellement"))`, `A & B`, `len(A | B)`, `B <= A`, `A - B`, `set("algorithme") == set("logarithme")`. Comme $B \subset A$, $A \cup B = A$ : c) vaut $\lvert A \rvert = 9$.

**Erreurs fréquentes.** `len("anticonstitutionnellement")` (25, les répétitions comptées) ; `A + B`, qui n'existe pas pour des ensembles ; confondre `A - B` et `B - A` (qui est vide ici).

### Ex R4.23 — Diagrammes de Venn

**Réponse.** `[~in_a & ~in_b, ~(in_a | in_b), ~in_a | ~in_b, ~(in_a & in_b)]`. Les régions 1 et 2 coïncident, et 3 et 4 aussi : ce sont les lois de De Morgan, $\overline{A \cup B} = \bar{A} \cap \bar{B}$ et $\overline{A \cap B} = \bar{A} \cup \bar{B}$.

**Erreurs fréquentes.** `not in_a` ou `in_a and in_b` sur des tableaux NumPy (une erreur : `and`, `or` et `not` veulent un seul booléen) ; oublier les parenthèses, `~in_a & ~in_b` étant juste mais `~in_a | in_b & ...` mélangeant les priorités.

### Ex R4.18 — Σ et Π en Python · `sum_over`, `prod_over`

**Réponses** : a) `[70, 0, 1024, 1]` · b) `0.9990234375` ($1 - \frac{1}{1\,024}$).

**Démarche.** `total = 0`, puis `for k in range(start, stop + 1): total = total + f(k)` ; `prod_over` part de `1` et multiplie. Une somme vide reste à 0, un produit vide à 1, sans cas particulier à écrire.

**Erreurs fréquentes.** `range(start, stop)`, qui oublie le dernier terme ; un produit qui part de 0 ; un total qui part de `0.0` (le résultat devient un flottant).

### Ex R4.22 — Vérifier une formule de somme de 1 à 1 000, puis la démontrer

**Réponses** : a) `250500250000` (c'est $500\,500^2$) · b) `0` · c) `4`.

**Démarche.** `sum_of_cubes(n)` : `sum(k**3 for k in range(1, n + 1))` ; `formula_a(n)` : `(n * (n + 1) // 2) ** 2` ; `formula_b(n)` : `n**2 * (n + 1) ** 2 // 4 + (n - 1) * (n - 2) * (n - 3)`. La formule B est juste en $n = 1, 2, 3$, où le produit $(n - 1)(n - 2)(n - 3)$ est nul, puis fausse dès $n = 4$.

**Démonstration de la formule A** (par récurrence). *Initialisation* : $1^3 = 1 = \left(\frac{1 \times 2}{2}\right)^2$. *Hérédité* : soit $n \ge 1$ tel que $\sum_{k=1}^{n} k^3 = \frac{n^2(n+1)^2}{4}$. Alors
$$\sum_{k=1}^{n+1} k^3 = \frac{n^2(n+1)^2}{4} + (n + 1)^3 = \frac{(n + 1)^2}{4}\left(n^2 + 4n + 4\right) = \frac{(n + 1)^2 (n + 2)^2}{4},$$
c'est la formule au rang $n + 1$. *Conclusion* : par récurrence, elle est vraie pour tout $n \ge 1$. ∎ Remarque : $\sum k^3 = \left(\sum k\right)^2$.

**Erreurs fréquentes.** `n * (n + 1) // 2 ** 2` (la puissance passe avant la division : on divise par 4, pas au carré) ; `range(1, n)` ; conclure de b) que la formule A est démontrée.

### Ex R4.24 — Chasse à l'erreur : une « démonstration » par récurrence qui prouve le faux

**Réponses** : a) `1` · b) `0` · c) `"F"` · d) `1` · e) `False`.

**Démarche.**
- Preuve 1 : il manque l'**initialisation**. Elle échoue : $5^0 + 1 = 2$. En fait $5 = 4 + 1$, donc $5^n$ laisse le reste 1 dans la division par 4, et $5^n + 1$ le reste 2 : la propriété n'est vraie pour **aucun** $n$. L'hérédité est juste, mais elle transmet une propriété que personne n'a : rien à réparer, l'énoncé est faux.
- Preuve 2 : pour $n = 1$, un groupe de 2 boules donne les groupes « boule 1 » et « boule 2 », qui n'ont aucune boule en commun ; la ligne F affirme le contraire. Pour $n \ge 2$, la ligne F est juste (la boule 2 est bien dans les deux groupes), mais la chaîne est cassée dès le premier maillon : de $P(1)$ on ne passe jamais à $P(2)$, qui est fausse (deux boules de couleurs différentes).

**Erreurs fréquentes.** Accuser les lignes D ou E, qui appliquent correctement l'hypothèse de récurrence ; croire qu'une hérédité « presque toujours » vraie suffit.

### Ex R4.25 — Rédiger une démonstration propre en LaTeX

**Ce qu'on attend.** L'énoncé avec son quantificateur et la définition de $P(n)$ ; trois paragraphes *Initialisation*, *Hérédité*, *Conclusion* ; le calcul de l'hérédité centré entre `$$`, avec la somme jusqu'à $n$ et l'endroit où l'hypothèse de récurrence sert ; un signe de fin. Le modèle est dans `05_solutions.ipynb`.

**Erreurs fréquentes.** Un `$` oublié, qui affiche le LaTeX en clair ; `\sum_{k=1}^n+1` au lieu de `\sum_{k=1}^{n+1}` (sans accolades, seul le premier caractère passe en exposant) ; un seul bloc de texte sans paragraphes.
