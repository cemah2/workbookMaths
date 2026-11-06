# R8 · Probabilités de base — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Pont, estimation, explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R8.Q1 — Univers, issue, événement
1. $2^5 = 32$ suites de cinq résultats (principe multiplicatif, fiche §3).
2. Un **événement** : l'ensemble des 4 issues {roi de pique, roi de trèfle, roi de cœur, roi de carreau}. Une issue, c'est une carte précise.
3. « Au plus un pile » : zéro pile ou un pile.
4. **Vrai** : $A \cap \bar{A} = \varnothing$, une issue ne peut pas être à la fois dans $A$ et hors de $A$.
5. **Faux** : sur un dé, « obtenir 1 » et « obtenir 2 » sont incompatibles, mais le contraire de « obtenir 1 » est « obtenir 2, 3, 4, 5 ou 6 ».
6. $C = \{1, 3, 5, 7\}$ et $D = \{6, 7, 8\}$ : $C \cap D = \{7\}$ et $C \cup D = \{1, 3, 5, 6, 7, 8\}$.

### R8.Q2 — Propriétés d'une probabilité
1. **Non** et **non** : une probabilité est toujours entre 0 et 1.
2. $1 - 0{,}35 = 0{,}65$.
3. $0{,}5 + 0{,}4 - 0{,}1 = 0{,}8$.
4. **Faux** : seulement quand $A$ et $B$ sont incompatibles ; sinon on retire $P(A \cap B)$.
5. **Non** : avec les 4 issues équiprobables FF, FG, GF, GG (on distingue l'aîné du cadet), « deux filles » et « deux garçons » ont chacun $\frac{1}{4}$, « une fille et un garçon » $\frac{2}{4} = \frac{1}{2}$.
6. **Faux** : 5 est le nombre de piles **moyen** ; exactement 5 n'arrive qu'environ une fois sur quatre ($\binom{10}{5} / 2^{10} = \frac{252}{1\,024}$).

### R8.Q3 — Arrangement ou combinaison ?
1. L'ordre compte, sans répétition : un **arrangement** de 3 coureurs parmi 10.
2. L'ordre ne compte pas, sans répétition : une **combinaison**, $\binom{32}{5}$ (R8.5 f).
3. L'ordre compte, **avec** répétition (un caractère peut revenir) : $36^8$.
4. L'ordre ne compte pas, sans répétition (une grille est un ensemble de 6 numéros) : $\binom{49}{6}$.
5. On range les 7 chapitres, l'ordre compte et sans répétition : $7!$ (ce sont aussi les arrangements des 7 chapitres parmi 7, une réponse juste aussi).
6. L'ordre compte, **avec** répétition (une boule remise peut ressortir) : $10^3$.

### R8.Q4 — Lire un arbre pondéré
1. $1 - 0{,}9 = 0{,}1$.
2. $0{,}6 \times 0{,}9 = 0{,}54$.
3. Deux chemins : $0{,}54 + 0{,}4 \times 0{,}7 = 0{,}54 + 0{,}28 = 0{,}82$.
4. **Vrai** : $0{,}54 + 0{,}06 + 0{,}28 + 0{,}12 = 1$.
5. $P(\text{germe} \mid A)$ : la probabilité de germer **sachant** que la graine est de variété A.
6. **Faux** : on **multiplie** le long d'un chemin, on additionne entre les chemins.

### R8.Q5 — Indépendants ou incompatibles ?
1. **Incompatibles**, et donc **pas indépendants** : $P(\{1\} \cap \{6\}) = 0$, alors que $\frac{1}{6} \times \frac{1}{6} > 0$.
2. **Oui** : la pièce n'a pas de mémoire ; $P(\text{PP}) = \frac{1}{4} = \frac{1}{2} \times \frac{1}{2}$.
3. **Vrai** (fiche §5) : $P(\bar{A} \cap B) = P(B) - P(A \cap B) = P(B) - P(A)\,P(B) = \big(1 - P(A)\big)\,P(B) = P(\bar{A})\,P(B)$.
4. $P(A \cap B) = P(A)\,P(B)$, donc $P(B) = \frac{0{,}1}{0{,}4} = 0{,}25$.
5. **Non** : $0{,}3 \times 0{,}5 = 0{,}15 \ne 0{,}2$.
6. **Oui** : si $P(A) = 0$, alors $A \cap B$, inclus dans $A$, a aussi la probabilité 0, et $P(A \cap B) = 0 = P(A)\,P(B)$.

### R8.Q6 — Espérance et variance : vrai ou faux
1. **Faux** : $S$ et $T$ de la fiche (§7) ont la même espérance 5, et des variances 2,5 et 8.
2. **Vrai** : $\mathbb{E}[X - 3Y] = \mathbb{E}[X] - 3\,\mathbb{E}[Y] = 4 - 3 = 1$ (linéarité, fiche §7 et R8.12).
3. **Faux** : une moyenne de carrés n'est jamais négative.
4. **Vrai** : $\sigma = \sqrt{9} = 3$.
5. **Faux** : ajouter une constante ne change pas la dispersion, $\mathbb{V}(X + 10) = \mathbb{V}(X)$.
6. **Faux** : $\mathbb{V}(-2X) = (-2)^2\,\mathbb{V}(X) = 4\,\mathbb{V}(X)$ ; une variance n'est jamais négative.
7. **Vrai** : tous les écarts à l'espérance sont nuls.

### R8.Q7 — Ce que dit la loi des grands nombres
1. **Faux** : les lancers sont indépendants ; le hasard n'a pas de mémoire (fiche §8).
2. Avec **10 000** lancers : la fréquence s'y écarte beaucoup moins de 0,5 (avec 10 lancers, il faudrait exactement 5 piles).
3. **Faux** : c'est la **fréquence** qui est proche de 0,5 ; le **nombre** de piles s'écarte typiquement de 5 000 d'une cinquantaine, et rester entre 4 990 et 5 010 n'arrive qu'environ une fois sur six.
4. **Faux** : les écarts diminuent comme $\frac{1}{\sqrt{n}}$ ; doubler $n$ les divise par $\sqrt{2} \approx 1{,}41$ seulement.
5. **Non** : sur 50 lancers, une pièce équilibrée s'écarte d'au moins 0,12 de 0,5 (31 piles ou plus, ou 19 ou moins) environ une fois sur huit. Ce résultat n'a rien d'exceptionnel ; il faudrait beaucoup plus de lancers pour soupçonner la pièce (M02c).
6. **Faux** : elle garantit que la fréquence s'en **rapproche**, pas qu'elle lui soit égale.

<a id="rappels"></a>

## 🔁 Rappels

### R8.R1 — Ensembles et complémentaire (R4)
1. $A \cap B = \{c\}$ et $A \cup B = \{a, b, c, d\}$. 2. $\bar{A} = \{d, e, f\}$. 3. $3 + 2 - 1 = 4$. 4. $\bar{A} \cap \bar{B} = \{e, f\}$, le complémentaire de $\{a, b, c, d\}$.

### R8.R2 — Σ et Π (R4)
1. $1 + 4 + 9 + 16 = 30$. 2. $0{,}5 + 0{,}9 + 2 = 3{,}4$. 3. $5! = 120$. 4. $0{,}9 \times 0{,}8 \times 0{,}7 = 0{,}504$.

### R8.R3 — Fractions (R1)
1. $\frac{2}{30} = \frac{1}{15}$. 2. $\frac{19}{27}$. 3. $\frac{3}{8} + \frac{2}{8} = \frac{5}{8}$. 4. $\frac{1}{6}$ (504 = 6 × 84). 5. $\frac{1}{32}$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R8.1 — Décrire univers et événements : cartes et pièces

**Réponses** : a) `16` · b) `6` · c) `15` · d) `5` · e) `2` · f) `18` · g) `14` · h) `False`.

**Démarche.**
- a) Chaque pièce a 2 issues, et l'on note la suite : $2^4 = 16$.
- b) On place les deux P parmi les quatre positions : PPFF, PFPF, PFFP, FPPF, FPFP, FFPP.
- c) Le contraire, « aucun pile », est la seule suite FFFF : $16 - 1 = 15$.
- d) Zéro pile (FFFF) ou un pile (4 suites, selon la position du P) : $1 + 4 = 5$.
- e) Les as noirs : l'as de pique et l'as de trèfle.
- f) $\lvert A \cup B \rvert = 4 + 16 - 2 = 18$.
- g) « Ni as, ni noire » est le contraire de $A \cup B$ : $32 - 18 = 14$ (les cœurs et les carreaux qui ne sont pas des as).
- h) **Faux** : l'as de cœur et l'as de carreau sont des as rouges ; les deux événements ont des issues communes.

**Erreurs fréquentes.** Prendre le nombre de piles pour une issue (répondre 5 en a) ; compter deux fois les as noirs en f ; confondre « au plus un » et « au moins un » en d ; en g, retirer les 4 as des cartes rouges (12), alors que seuls les as rouges en font partie.

**Variante.** Avec cinq pièces, combien d'issues pour « exactement deux piles » ? *Réponse* : 10 (deux positions parmi cinq, $\binom{5}{2}$, §3).

### Ex R8.2 — Probabilités par équiprobabilité

**Réponses** : a) `"2/11"` · b) `"5/11"` · c) `"4/11"` · d) `24` · e) `"1/6"` · f) `"1/8"` · g) `"7/12"` · h) `"3/4"`.

**Démarche.**
- a) à c) Les 11 positions sont équiprobables : P, R, O, B, A, B, I, L, I, T, É. Deux B ; cinq voyelles (O, A, I, I, É) ; les autres consonnes sont P, R, L, T.
- d) $6 \times 4 = 24$ couples (dé à 6 faces, dé à 4 faces), équiprobables.
- e) Somme 5 : (1, 4), (2, 3), (3, 2), (4, 1), soit $\frac{4}{24} = \frac{1}{6}$.
- f) Somme 9 ou 10 : (5, 4), (6, 3), (6, 4), soit $\frac{3}{24} = \frac{1}{8}$.
- g) On compte selon le dé à 4 faces : s'il donne 1, le dé à 6 faces doit donner 2 à 6 (5 couples), puis 4, 3 et 2 couples. $\frac{5 + 4 + 3 + 2}{24} = \frac{14}{24} = \frac{7}{12}$.
- h) Le produit est impair seulement si les deux nombres le sont : $3 \times 2 = 6$ couples. $P = 1 - \frac{6}{24} = \frac{3}{4}$.

**Erreurs fréquentes.** Compter une seule fois une lettre qui revient, ou oublier le É ; oublier qu'un couple (2, 3) et un couple (3, 2) sont deux issues ; prendre deux dés à 6 faces en e ($\frac{4}{36}$) ; inclure les égalités en g.

**Variante.** La probabilité que la somme des deux dés soit paire ? *Réponse* : les deux pairs ($3 \times 2$) ou les deux impairs ($3 \times 2$) : $\frac{12}{24} = \frac{1}{2}$.

### Ex R8.3 — P(A ∪ B) et le complémentaire

**Réponses** : a) `0.6` · b) `0.4` · c) `0.3` · d) `0.45` · e) `False` · f) `0.25` · g) `"15/16"` · h) `0.2`.

**Démarche.**
- a) $0{,}45 + 0{,}3 - 0{,}15 = 0{,}6$.
- b) « Ni $A$ ni $B$ » est le contraire de « $A$ ou $B$ » (De Morgan) : $1 - 0{,}6 = 0{,}4$.
- c) $A$ se partage entre $A \cap B$ et $A \cap \bar{B}$ : $0{,}45 - 0{,}15 = 0{,}3$.
- d) Incompatibles : $0{,}65 = 0{,}2 + P(B)$, donc $P(B) = 0{,}45$.
- e) **Faux** : incompatibles, ils donneraient $P(A \cup B) = 0{,}7 + 0{,}6 = 1{,}3 > 1$.
- f) $P(\text{appli ou newsletter}) = 1 - 0{,}2 = 0{,}8 = 0{,}6 + 0{,}45 - P(\text{les deux})$, donc $P(\text{les deux}) = 0{,}25$.
- g) Le contraire de « au moins un face » est « que des piles », PPPP, une seule suite sur 16 : $1 - \frac{1}{16} = \frac{15}{16}$.
- h) $0{,}7 = 0{,}55 + 0{,}35 - P(A \cap B)$, donc $P(A \cap B) = 0{,}2$.

**Erreurs fréquentes.** Additionner sans retirer l'intersection ; prendre le contraire de $A \cap B$ pour « ni $A$ ni $B$ » ; en f, croire que « l'appli ou la newsletter » a la probabilité 1, ou multiplier 0,6 par 0,45 comme si les deux étaient indépendantes (0,27).

**Variante.** $P(A) = 0{,}6$, $P(B) = 0{,}5$ et $P(\bar{A} \cap \bar{B}) = 0{,}1$ : que vaut $P(A \cap B)$ ? *Réponse* : $P(A \cup B) = 0{,}9$, donc $0{,}6 + 0{,}5 - 0{,}9 = 0{,}2$.

### Ex R8.4 — Principe multiplicatif et factorielles

**Réponses** : a) `308915776` · b) `71288256` · c) `5040` · d) `336` · e) `60` · f) `24` · g) `72` · h) `676000`.

**Démarche.**
- a) $26^6$ : 26 possibilités à chacune des 6 positions.
- b) 6 voyelles pour la première lettre, puis 26 possibilités pour chacune des 5 autres : $6 \times 26^5 = 71\,288\,256$.
- c) $7! = 1 \times 2 \times \cdots \times 7 = 5\,040$.
- d) $8 \times 7 \times 6 = 336$ : l'or, puis l'argent, puis le bronze.
- e) $4 \times 5 \times 3 = 60$.
- f) A est fixée en premier ; on range les 4 autres : $4! = 24$.
- g) $\frac{9!}{7!} = 9 \times 8 = 72$ : les facteurs de 1 à 7 se simplifient.
- h) $26 \times 26 \times 10 \times 10 \times 10 = 676\,000$.

**Erreurs fréquentes.** Additionner au lieu de multiplier (e) ; contraindre les six lettres à être des voyelles en b ; traiter un podium comme une combinaison (d) ; ranger aussi la tâche fixée (f).

**Variante.** Combien de codes de 4 chiffres tous différents, dont le premier n'est pas 0 ? *Réponse* : $9 \times 9 \times 8 \times 7 = 4\,536$.

### Ex R8.5 — Combinaisons et triangle de Pascal

**Réponses** : a) `35` · b) `105` · c) `190` · d) `[1, 7, 21, 35, 35, 21, 7, 1]` · e) `512` · f) `201376` · g) `"1/7192"` · h) `70`.

**Démarche.**
- a) $\frac{7 \times 6 \times 5}{3!} = \frac{210}{6} = 35$.
- b) Une poignée de main par paire : $\binom{15}{2} = \frac{15 \times 14}{2} = 105$.
- c) $\binom{20}{18} = \binom{20}{2} = \frac{20 \times 19}{2} = 190$.
- d) À partir de la ligne 6 (1, 6, 15, 20, 15, 6, 1), chaque nombre est la somme des deux au-dessus : 1, 7, 21, 35, 35, 21, 7, 1.
- e) La somme de la ligne $n$ vaut $2^n$ : $2^9 = 512$.
- f) $\binom{32}{5} = \frac{32 \times 31 \times 30 \times 29 \times 28}{120} = 201\,376$.
- g) Une main qui contient les 4 as se complète par une 5ᵉ carte parmi les 28 autres : 28 mains favorables. $\frac{28}{201\,376} = \frac{1}{7\,192}$.
- h) Un chemin est une suite de 8 pas, dont 4 vers la droite ; il suffit de choisir lesquels : $\binom{8}{4} = 70$.

**Erreurs fréquentes.** Oublier de diviser par $k!$ (répondre 210 en a ou en b) ; commencer à compter les lignes à 1 au lieu de 0 ; en g, croire qu'il n'y a qu'une main favorable, ou diviser par le nombre de mains de 4 cartes ; en h, compter 3 pas de chaque sorte au lieu de 4 (20).

**Variante.** La probabilité qu'une main de 5 cartes parmi 32 contienne exactement 2 as ? *Réponse* : $\frac{\binom{4}{2}\binom{28}{3}}{\binom{32}{5}} = \frac{6 \times 3\,276}{201\,376} = \frac{351}{3\,596} \approx 0{,}098$.

### Ex R8.6 — Arbres pondérés : épreuves successives

**Réponses** : a) `0.06` · b) `0.16` · c) `0.3` · d) `0.56` · e) `0.29` · f) `0.71` · g) `0.15` · h) `"37/64"`.

**Démarche.**
- a) $0{,}6 \times 0{,}1 = 0{,}06$.
- b) Deux chemins mènent au retard : $0{,}06 + 0{,}4 \times 0{,}25 = 0{,}06 + 0{,}1 = 0{,}16$.
- c) $0{,}4 \times 0{,}75 = 0{,}3$.
- d) Réussi, puis réussi : $0{,}7 \times 0{,}8 = 0{,}56$.
- e) Réussi puis manqué, ou manqué puis réussi : $0{,}7 \times 0{,}2 + 0{,}3 \times 0{,}5 = 0{,}14 + 0{,}15 = 0{,}29$.
- f) Deux chemins finissent par une réussite : $0{,}56 + 0{,}15 = 0{,}71$.
- g) Manqué, puis manqué : $0{,}3 \times 0{,}5 = 0{,}15$. Vérification : $0{,}56 + 0{,}29 + 0{,}15 = 1$.
- h) Le contraire est « trois mauvaises réponses » : $1 - \left(\frac{3}{4}\right)^3 = 1 - \frac{27}{64} = \frac{37}{64}$.

Dans ta copie : f vaut 0,71, un peu plus que les 0,7 du premier lancer. La joueuse réussit son second lancer avec la probabilité 0,8 après une réussite, et 0,5 seulement après un échec ; comme elle réussit le premier sept fois sur dix, c'est la branche à 0,8 qui pèse le plus : $0{,}7 \times 0{,}8 + 0{,}3 \times 0{,}5$.

**Erreurs fréquentes.** Garder 0,7 au second lancer, comme si les deux étaient indépendants (0,49 en d) ; oublier un des deux chemins en e et en f ; faire la moyenne des deux branches en f (0,65) au lieu de les pondérer ; additionner $\frac{1}{4}$ trois fois en h.

**Variante.** Un troisième lancer suit la même règle (0,8 après une réussite, 0,5 après un échec) : la probabilité de réussir les trois ? *Réponse* : $0{,}7 \times 0{,}8 \times 0{,}8 = 0{,}448$.

### Ex R8.7 — Indépendant ou pas ? Le décider par le calcul, avec des cartes et des pièces

**Réponses** : a) `"1/32"` · b) `True` · c) `False` · d) `True` · e) `"1/4"` · f) `False` · g) `"3/4"` · h) `False`.

**Démarche.**
- a) et b) $A \cap B$ est l'as de cœur : $\frac{1}{32} = \frac{4}{32} \times \frac{8}{32} = \frac{1}{8} \times \frac{1}{4}$. Indépendants.
- c) Une carte n'est jamais à la fois un as et un roi : $P(A \cap C) = 0 \ne \frac{1}{8} \times \frac{1}{8}$. Incompatibles, donc pas indépendants : savoir que la carte est un as rend « roi » impossible.
- d) $A \cap D$ = {as de pique, as de trèfle} : $\frac{2}{32} = \frac{1}{16} = \frac{1}{8} \times \frac{1}{2}$. Indépendants : il y a autant d'as parmi les noires que parmi toutes les cartes (un sur huit).
- e) et f) $E$ = {PFF, FPF, FFP} et $F$ = {FPP, FPF, FFP, FFF} : $E \cap F$ = {FPF, FFP}, de probabilité $\frac{2}{8} = \frac{1}{4}$, alors que $P(E)\,P(F) = \frac{3}{8} \times \frac{1}{2} = \frac{3}{16}$. Pas indépendants : savoir qu'il y a exactement un pile rend « la première donne face » plus probable ($\frac{2}{3}$ au lieu de $\frac{1}{2}$).
- g) et h) $G \cap H$ contient toutes les issues sauf PPP et FFF : $\frac{6}{8} = \frac{3}{4}$, alors que $P(G)\,P(H) = \frac{7}{8} \times \frac{7}{8} = \frac{49}{64}$. Pas indépendants : savoir qu'il y a au moins un pile rend « au moins un face » un peu moins probable ($\frac{6}{7}$ au lieu de $\frac{7}{8}$), car FFF est exclu.

**Erreurs fréquentes.** Conclure « incompatibles, donc indépendants » en c ; décider sans calculer, sur l'impression d'un « lien » (d, f) ; comparer des arrondis au lieu des fractions exactes ($\frac{3}{4}$ et $\frac{49}{64}$ sont proches, mais différents).

**Variante.** La roue de 8 secteurs, $A$ = « pair », $B$ = « au plus 4 » : indépendants ? *Réponse* : $P(A \cap B) = P(\{2, 4\}) = \frac{1}{4} = \frac{1}{2} \times \frac{1}{2}$ : **oui**.

### Ex R8.8 — La loi d'une variable aléatoire

**Réponses** : a) `[0.125, 0.375, 0.375, 0.125]` · b) `0.5` · c) `[0.0625, 0.1875, 0.3125, 0.4375]` · d) `0.25` · e) `0.3` · f) `0.85` · g) `[0.5, 0.375, 0.125]` · h) `0.875`.

**Démarche.**
- a) Sur les 8 suites, 1 a zéro pile, 3 en ont un, 3 en ont deux, 1 en a trois : $\frac{1}{8}, \frac{3}{8}, \frac{3}{8}, \frac{1}{8}$.
- b) $\frac{3}{8} + \frac{1}{8} = \frac{1}{2}$.
- c) Sur les 16 couples, le plus grand vaut 1 pour (1, 1) seulement ; 2 pour (1, 2), (2, 1), (2, 2) ; en général, $k^2 - (k - 1)^2 = 2k - 1$ couples ont un maximum égal à $k$ : 1, 3, 5, 7 sur 16.
- d) $\frac{1 + 3}{16} = 0{,}25$ : les deux numéros valent au plus 2.
- e) $1 - 0{,}15 - 0{,}35 - 0{,}2 = 0{,}3$.
- f) $1 - P(Z = 1) = 0{,}85$.
- g) 16 cartes ne sont ni des as ni des figures, 12 sont des figures, 4 sont des as : $\frac{16}{32}, \frac{12}{32}, \frac{4}{32}$.
- h) $1 - P(W = 5) = 1 - 0{,}125 = 0{,}875$.

**Erreurs fréquentes.** Croire les valeurs de $X$ équiprobables ; donner la loi du plus petit numéro en c ; oublier $P(Z = 3)$, qui n'est pas donnée, en f (0,55) ; compter deux figures par couleur en g.

**Variante.** La loi du plus **petit** des deux numéros de c ? *Réponse* : $\frac{7}{16}, \frac{5}{16}, \frac{3}{16}, \frac{1}{16}$ pour 1, 2, 3, 4.

### Ex R8.9 — Espérance, variance (avec V = E[X²] − E[X]²) et écart-type

**Réponses** : a) `0.25` · b) `1.5` · c) `5.5` · d) `1.225` · e) `-1` · f) `2.449` · g) `"1/3"` · h) `2`.

**Démarche.**
- a) Deux équations : la somme des probabilités, $0{,}5 + p_2 + p_4 = 1$, et l'espérance, $1 \times 0{,}5 + 2p_2 + 4p_4 = 2$. La première donne $p_2 = 0{,}5 - p_4$ ; dans la seconde, $0{,}5 + 1 - 2p_4 + 4p_4 = 2$, donc $p_4 = 0{,}25$ (et $p_2 = 0{,}25$).
- b) Les écarts à 2 valent −1, 0 et 2 : $\mathbb{V}(X) = 1 \times 0{,}5 + 0 \times 0{,}25 + 4 \times 0{,}25 = 1{,}5$.
- c) $\mathbb{E}[X^2] = 1 \times 0{,}5 + 4 \times 0{,}25 + 16 \times 0{,}25 = 5{,}5$, et $5{,}5 - 2^2 = 1{,}5$ : les deux méthodes concordent.
- d) $\sigma(X) = \sqrt{1{,}5} \approx 1{,}225$.
- e) $\mathbb{E}[3 - 2X] = 3 - 2 \times 2 = -1$.
- f) $\sigma(Y) = \lvert -2 \rvert \times \sigma(X) = 2\sqrt{1{,}5} \approx 2{,}449$ (et $\mathbb{V}(Y) = 4 \times 1{,}5 = 6$).
- g) $\mathbb{E}[W] = 2p + (-1)(1 - p) = 3p - 1 = 0$, donc $p = \frac{1}{3}$.
- h) $\mathbb{V}(W) = \mathbb{E}[W^2] - 0^2 = 4 \times \frac{1}{3} + 1 \times \frac{2}{3} = 2$.

**Erreurs fréquentes.** N'écrire qu'une équation en a ; confondre $\mathbb{E}[X^2]$ et $\mathbb{E}[X]^2$ ; multiplier l'écart-type par $a^2$, ou garder le signe de $a$, en f ; croire qu'une espérance nulle rend les deux valeurs équiprobables en g.

**Variante.** Une variable $V$ vaut −2 ou 3, d'espérance nulle : $P(V = 3)$ et $\mathbb{V}(V)$ ? *Réponse* : $3q - 2(1 - q) = 0$, donc $q = \frac{2}{5}$ ; $\mathbb{V}(V) = 9 \times \frac{2}{5} + 4 \times \frac{3}{5} = 6$.

### Ex R8.10 — Deux jeux de hasard : équité et risque

**Réponses** : a) `-0.5` · b) `8.25` · c) `2.87` · d) `5` · e) `3.54` · f) `0.75` · g) `3.03` · h) `3`.

**Démarche.**
- a) Deux piles $\frac{1}{4}$, un de chaque $\frac{1}{2}$ (PF ou FP), deux faces $\frac{1}{4}$ : $3 \times \frac{1}{4} + 0 \times \frac{1}{2} + (-5) \times \frac{1}{4} = -0{,}5$ €.
- b) $\mathbb{E}[G^2] = 9 \times \frac{1}{4} + 25 \times \frac{1}{4} = 8{,}5$, donc $\mathbb{V} = 8{,}5 - (-0{,}5)^2 = 8{,}25$.
- c) $\sqrt{8{,}25} \approx 2{,}87$ €.
- d) Avec un gain $x$ pour deux piles : $\frac{x}{4} - \frac{5}{4} = 0$, donc $x = 5$ €.
- e) Le gain vaut 5, 0 ou −5, d'espérance nulle : $\mathbb{V} = \frac{25}{4} + \frac{25}{4} = 12{,}5$, et $\sigma = \sqrt{12{,}5} \approx 3{,}54$ €.
- f) 4 doubles parmi les 16 couples : $6 \times \frac{1}{4} + (-1) \times \frac{3}{4} = 0{,}75$ €.
- g) $\mathbb{E}[G^2] = 36 \times \frac{1}{4} + 1 \times \frac{3}{4} = 9{,}75$, donc $\mathbb{V} = 9{,}75 - 0{,}75^2 = 9{,}1875$ et $\sigma \approx 3{,}03$ €.
- h) Avec un gain $x$ pour un double : $\frac{x}{4} - \frac{3}{4} = 0$, donc $x = 3$ €.

Dans ta copie : le jeu B rendu équitable fait gagner 3 € ou perdre 1 €, avec $\mathbb{V} = \frac{9}{4} + \frac{3}{4} = 3$ et $\sigma = \sqrt{3} \approx 1{,}73$ €, contre 3,54 € pour le jeu A équitable. Les deux ont la même espérance, 0 ; le jeu A est deux fois plus dispersé : on y gagne ou perd 5 € une fois sur deux. Préférer l'un ou l'autre est une question de goût du risque, que l'espérance ne mesure pas, et que l'écart-type résume.

**Erreurs fréquentes.** Prendre « deux piles », « deux faces » et « un de chaque » pour équiprobables (−0,67 en a) ; oublier de retirer le carré de l'espérance en b et en g ; ajouter au gain de deux piles le manque de 0,5 € en d (3,5), alors qu'un euro de plus sur ce gain n'ajoute qu'un quart d'euro à l'espérance.

**Variante.** Jeu C : on lance trois pièces ; trois piles font gagner 7 €, sinon on perd 1 €. L'espérance et la variance du gain ? *Réponse* : $7 \times \frac{1}{8} - \frac{7}{8} = 0$ € (équitable) ; $\frac{49}{8} + \frac{7}{8} - 0 = 7$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R8.11 — Démontrer C(n, k) = C(n − 1, k − 1) + C(n − 1, k)

**Réponse modèle.**
1. $\binom{6}{3} = 20$, $\binom{5}{2} = 10$ et $\binom{5}{3} = 10$ : $10 + 10 = 20$.
2. Avec $k! = k \times (k - 1)!$ et $(n - k)! = (n - k) \times (n - k - 1)!$ :
$$\binom{n - 1}{k - 1} + \binom{n - 1}{k} = \frac{(n - 1)!}{(k - 1)!\,(n - k)!} + \frac{(n - 1)!}{k!\,(n - k - 1)!} = \frac{(n - 1)!\,k}{k!\,(n - k)!} + \frac{(n - 1)!\,(n - k)}{k!\,(n - k)!} = \frac{(n - 1)!\,n}{k!\,(n - k)!} = \frac{n!}{k!\,(n - k)!}.$$
3. Parmi les $\binom{n}{k}$ façons de choisir $k$ objets parmi $n$, celles qui **contiennent** le premier objet se complètent par $k - 1$ objets parmi les $n - 1$ autres : il y en a $\binom{n - 1}{k - 1}$. Celles qui **ne le contiennent pas** prennent leurs $k$ objets parmi les $n - 1$ autres : $\binom{n - 1}{k}$. Chaque choix est dans exactement un des deux cas, d'où la formule.
4. $\binom{n}{k}$ compte les sous-ensembles à $k$ éléments d'un ensemble à $n$ éléments ; en additionnant sur $k$ de 0 à $n$, on compte **tous** ses sous-ensembles. Or un sous-ensemble se construit en décidant, pour chacun des $n$ éléments, s'il est pris ou non : $2 \times 2 \times \cdots \times 2 = 2^n$ façons (principe multiplicatif).
5. Pour $k = 0$ ou $k = n$, l'un des deux termes de droite n'a pas de sens sans convention ($\binom{n - 1}{-1}$, $\binom{n - 1}{n}$). Avec la convention $\binom{m}{j} = 0$ hors de $0 \le j \le m$, la formule reste vraie : $\binom{n}{0} = 1 = 0 + \binom{n - 1}{0}$.

**Grille.** Une bonne démonstration : (1) vérifie la formule sur un exemple ; (2) en 2, réduit au même dénominateur en justifiant les deux égalités de factorielles, puis factorise $(n - 1)!$ et reconnaît $k + (n - k) = n$ ; (3) en 3, partage les choix en deux cas **disjoints** et qui couvrent tout, et compte chacun ; (4) en 4, dit ce que comptent les deux membres ; (5) explique le rôle de la condition $1 \le k \le n - 1$.

### Ex R8.12 — L'espérance d'une somme : E[X + Y] = E[X] + E[Y], même pour des variables liées

**Réponse modèle.**
1. Avec la loi : $\mathbb{E}[X] = 0 \times \frac{1}{8} + 1 \times \frac{3}{8} + 2 \times \frac{3}{8} + 3 \times \frac{1}{8} = \frac{12}{8} = 1{,}5$. Avec les issues (PPP → 3, PPF → 2, PFP → 2, PFF → 1, FPP → 2, FPF → 1, FFP → 1, FFF → 0), chacune de poids $\frac{1}{8}$ : $\frac{3 + 2 + 2 + 1 + 2 + 1 + 1 + 0}{8} = \frac{12}{8}$. En général : les événements $\{X = x\}$, pour les différentes valeurs $x$, partagent $\Omega$ en morceaux disjoints. Dans la somme sur les issues, on regroupe celles de chaque morceau : leur contribution est $\sum_{\omega : X(\omega) = x} x\,p(\omega) = x \sum_{\omega : X(\omega) = x} p(\omega) = x\,P(X = x)$, et la somme de ces contributions sur toutes les valeurs $x$ est $\sum_x x\,P(X = x) = \mathbb{E}[X]$.
2. $\mathbb{E}[X + Y] = \sum_\omega \big(X(\omega) + Y(\omega)\big)\,p(\omega) = \sum_\omega X(\omega)\,p(\omega) + \sum_\omega Y(\omega)\,p(\omega) = \mathbb{E}[X] + \mathbb{E}[Y]$ (une somme se sépare, R4 ; et 1 appliqué à $X + Y$, à $X$ et à $Y$). On n'a **jamais** supposé $X$ et $Y$ indépendantes : la formule vaut pour des variables liées.
3. Pour $n = 2$, c'est 2. Si la formule est vraie pour $n$ variables, alors pour $n + 1$ : $X_1 + \cdots + X_{n+1} = (X_1 + \cdots + X_n) + X_{n+1}$ est la somme de **deux** variables aléatoires, donc, par 2, $\mathbb{E}[X_1 + \cdots + X_{n+1}] = \mathbb{E}[X_1 + \cdots + X_n] + \mathbb{E}[X_{n+1}]$, puis, par l'hypothèse de récurrence, $= \mathbb{E}[X_1] + \cdots + \mathbb{E}[X_n] + \mathbb{E}[X_{n+1}]$. La formule est vraie pour tout $n \ge 2$.
4. $N = X_1 + X_2 + \cdots + X_{20}$, et $\mathbb{E}[X_i] = 0 \times \frac{3}{4} + 1 \times \frac{1}{4} = \frac{1}{4}$. Par 3, $\mathbb{E}[N] = 20 \times \frac{1}{4} = 5$ bonnes réponses en moyenne, sans calculer la loi de $N$.
5. $XY = X^2 = X$ (0 ou 1), donc $\mathbb{E}[XY] = \frac{1}{2}$, alors que $\mathbb{E}[X]\,\mathbb{E}[Y] = \frac{1}{4}$.

**Grille.** Une bonne démonstration : (1) calcule l'exemple des deux façons, et justifie l'égalité générale en partageant $\Omega$ selon les valeurs de $X$ ; (2) écrit $\mathbb{E}[X + Y]$ comme une somme sur les issues, la sépare en deux, et remarque qu'aucune indépendance n'a servi ; (3) rédige une récurrence complète : initialisation, hérédité qui écrit la somme de $n + 1$ termes comme la somme de deux variables, conclusion ; (4) décompose $N$ en une somme de variables qui valent 0 ou 1 ; (5) donne un contre-exemple chiffré pour le produit.

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Pont, estimation, explication

### Ex R8.13 — Comparer toutes les paires : un tournoi, C(n, 2) et une croissance en n²

**Réponses** : a) `120` · b) `240` · c) `499500` · d) `100` · e) `138.9` · f) `161700`.

**Démarche.**
- a) $\binom{16}{2} = \frac{16 \times 15}{2} = 120$.
- b) Deux matchs par paire : 240 (ce sont les couples ordonnés, $16 \times 15$).
- c) $\binom{1\,000}{2} = \frac{1\,000 \times 999}{2} = 499\,500$.
- d) $\frac{10\,000 \times 9\,999}{1\,000 \times 999} \approx 100{,}09$, soit 100.
- e) $\binom{10^6}{2} \approx 5 \times 10^{11}$ comparaisons, soit $499\,999{,}5$ secondes, ou environ 138,9 heures (près de 6 jours).
- f) $\binom{100}{3} = \frac{100 \times 99 \times 98}{6} = 161\,700$.

Dans ta copie : $\binom{n}{2} = \frac{n(n - 1)}{2}$, et pour $n$ grand, $n - 1 \approx n$. Multiplier $n$ par 10 multiplie la durée par environ 100 (près de deux mois), et le nombre de groupes de 3 par environ 1 000 ($\binom{n}{3} \approx \frac{n^3}{6}$).

**Erreurs fréquentes.** Compter les couples ordonnés en a et en c ; croire que le travail est multiplié par 10 quand $n$ l'est (d) ; se tromper d'unité en e.

**Variante.** Combien de paires dans un dataset de 50 000 exemples ? *Réponse* : $\frac{50\,000 \times 49\,999}{2} = 1\,249\,975\,000$, plus d'un milliard.

### Ex R8.14 — Fermi : la probabilité de croiser quelqu'un que l'on connaît dans le métro

**Exemple de réponse** (chaque nombre est une hypothèse, à un facteur 2 ou 3 près).
1. Je reconnais environ 300 personnes ; un jour donné, une sur dix prend le métro de la ville : environ 30.
2. Le métro d'une très grande ville transporte quelques millions de voyageurs par jour, disons 4 millions : $q \approx \frac{30}{4 \times 10^6} \approx 7{,}5 \times 10^{-6}$.
3. Pendant un trajet, je croise quelques centaines de personnes (ma rame, les quais, les couloirs) : $N \approx 500$.
4. $1 - (1 - q)^N \approx 1 - (1 - 7{,}5 \times 10^{-6})^{500} \approx 0{,}0037$, environ 0,4 % par trajet. Quand $Nq$ est petit, $(1 - q)^N \approx 1 - Nq$ (les termes suivants sont négligeables), d'où $1 - (1 - q)^N \approx Nq = 0{,}00375$.
5. Sur une année de 400 trajets : $1 - (1 - 0{,}0037)^{400} \approx 0{,}77$ : il est probable de croiser au moins une connaissance dans l'année. L'hypothèse la plus fragile : des voyageurs « tirés au hasard » parmi tous les usagers. En réalité, tes connaissances vivent et travaillent souvent près de chez toi, sur tes lignes, à tes horaires : la probabilité réelle est plus grande.

**Grille.** Une bonne estimation : (1) écrit chaque hypothèse avec son ordre de grandeur ; (2) calcule $q$ comme un rapport ; (3) passe par le contraire pour « au moins une rencontre » ; (4) justifie l'approximation $Nq$ ; (5) critique l'hypothèse d'indépendance ou d'uniformité.

### Ex R8.15 — Expliquer la différence entre probabilité et fréquence

**Exemple de réponse.**

> Une probabilité est une prévision : un nombre entre 0 et 1 qui dit à quel point on s'attend à un événement, avant de l'observer. Une fréquence est un constat : la proportion des fois où l'événement s'est vraiment produit, dans une série d'observations. La fréquence change d'une série à l'autre (une autre année, d'autres jours de pluie) ; la probabilité, elle, ne dépend pas de la série. Les deux se rejoignent quand on répète beaucoup : sur un grand nombre de jours annoncés à 30 %, il devrait pleuvoir environ 3 jours sur 10 ; c'est la loi des grands nombres, et c'est ainsi qu'on vérifie qu'une météo est fiable. Mais demain n'arrive qu'une fois : « 30 % » ne se vérifie pas sur un seul jour. Quant à ton parapluie, ta fréquence de 7 sur 10 mesure autre chose : les jours où tu l'as pris sans qu'il pleuve.

**Grille.** Une bonne réponse : (1) une probabilité est une prévision, entre 0 et 1 ; (2) une fréquence est une proportion observée ; (3) la fréquence varie d'une série à l'autre ; (4) les deux se rapprochent sur un grand nombre de répétitions (loi des grands nombres) ; (5) un événement unique ne se « vérifie » pas par sa fréquence ; (6) aucune formule, huit lignes au plus.

<a id="notebook"></a>

## Notebook

### Ex R8.16 — Factorielle et combinaisons · `factorial`, `binomial`

**Réponses** : a) `[1, 1, 40320, 6227020800]` · b) `"ValueError"` · c) `[1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]` · d) `[0, 0]` · e) `"int"`.

**Démarche.** `factorial` : lever la `ValueError` si `n < 0`, puis multiplier `result` (qui part de 1) par 2, 3, …, `n` ; pour `n = 0` ou `1`, la boucle ne tourne pas et le résultat reste 1. `binomial` : renvoyer 0 hors de $0 \le k \le n$, puis calculer $\frac{n(n - 1)\cdots(n - k + 1)}{k!}$ en alternant multiplication et division entière `//` (chaque étape donne un entier, qui est un coefficient binomial). Pour la copie : `factorial(20) // factorial(18)` vaut $20 \times 19 = 380$ ; pour $\binom{10\,000}{3}$, trois multiplications suffisent, au lieu de trois factorielles géantes.

**Erreurs fréquentes.** `range(1, n)`, qui oublie le facteur `n` ; démarrer le produit à 0 ; la division `/`, qui renvoie un flottant arrondi pour les grands nombres.

### Ex R8.17 — Une probabilité exacte par énumération · `enumerate_probability`

**Réponses** : a) `5/32` · b) `5/8` · c) `271/1000` · d) `"ValueError"` · e) `"Fraction"`.

**Démarche.** Une seule boucle sur `outcomes`, qui compte les issues et les issues favorables (`if event(outcome)`), puis `Fraction(favourable, total)` ; une `ValueError` si `total == 0`. La boucle marche aussi pour un générateur, qui n'a pas de `len()`. Pour la copie : 10 triplets de somme 6 (les 3 rangements de (1, 1, 4), les 6 de (1, 2, 3), et (2, 2, 2)), soit $\frac{10}{64}$ ; trois numéros différents : $4 \times 3 \times 2 = 24$ triplets, d'où $1 - \frac{24}{64} = \frac{5}{8}$.

**Erreurs fréquentes.** `len(outcomes)` sur un générateur ; parcourir deux fois un générateur (la seconde fois, il est vide) ; renvoyer `favourable / total`, un flottant.

### Ex R8.18 — Espérance et variance d'une loi · `expectation`, `variance`

**Réponses** : a) `1/3` · b) `5/18` · c) `0.175` · d) `2.2069` · e) `"ValueError"` · f) `"ValueError"` · g) `"Fraction"`.

**Démarche.** D'abord vérifier la loi (longueurs, signes, somme à $10^{-9}$ près : `abs(sum(probabilities) - 1) > 1e-9`), puis `sum(x * p for x, p in zip(values, probabilities))`. Pour la variance : l'espérance `m`, puis `sum((x - m) ** 2 * p ...)`. Un résultat calculé avec des entiers et des `Fraction` est déjà une `Fraction` : il suffit de ne pas le convertir. Pour la copie : $\mathbb{E}[X^2] = \frac{10 + 4}{36} = \frac{7}{18}$, et $\mathbb{V} = \frac{7}{18} - \frac{1}{9} = \frac{5}{18}$.

**Erreurs fréquentes.** Ne pas vérifier les longueurs (`zip` s'arrête sans rien dire) ; tester `sum(...) == 1` sur des flottants (0,1 × 10 ne fait pas exactement 1) ; oublier le carré dans la variance.

### Ex R8.19 — Estimer une probabilité par simulation · `simulate_frequency`

**Réponses** : a) `0.238` · b) `True` · c) `True` · d) `"ValueError"` · e) `True`.

**Démarche.** Lever la `ValueError` si `n_trials <= 0`, créer `rng = np.random.default_rng(seed)` **une fois**, puis compter les essais où `experiment(rng)` est vrai, et diviser par `n_trials`. Pour la copie : 1 000 essais donnent une fréquence proche de $\frac{1}{4}$, à quelques centièmes près, jamais exactement (loi des grands nombres). Un générateur recréé dans la boucle avec la même graine redonne le même tirage à chaque essai : la « fréquence » vaut 0 ou 1.

**Erreurs fréquentes.** Recréer le générateur dans la boucle ; ignorer `seed` (`default_rng()` sans argument) ; utiliser le module `random` de Python au lieu du générateur passé à l'expérience.

### Ex R8.20 — Prédire : dans une classe de 30, deux élèves ont-ils le même anniversaire ?

**Réponses** : a) `3` · b) `1` · c) `3` · d) `0.706` · e) `23`.

**Démarche.** La simulation donne des fréquences proches de 0,12 (10 élèves), 0,52 (23), 0,71 (30) et 0,99 (60). `p_shared(n)` : partir de `all_different = 1.0`, multiplier par `(365 - k) / 365` pour `k` de 0 à `n - 1`, et renvoyer `1 - all_different`. e) se trouve par une boucle (`next(n for n in range(1, 366) if p_shared(n) > 0.5)`). Pour la copie : une classe de 30 contient $\binom{30}{2} = 435$ paires d'élèves ; chacune n'a qu'une chance sur 365 de partager un anniversaire, mais avec 435 paires, il est probable que l'une au moins y parvienne. L'intuition pense à **son propre** anniversaire (une personne parmi 29 qui serait née le même jour que soi : environ 8 %), pas à toutes les paires.

**Erreurs fréquentes.** Calculer la probabilité que tous les anniversaires soient différents, sans passer au contraire ; répondre 22 en e (le dernier qui reste en dessous de 0,5) ; diviser 30 par 365.

### Ex R8.21 — La loi des grands nombres : fréquence et nombre d'essais

**Réponses** : a) `[0.694, 0.288, 0.0, 0.0]` · b) `0.3333` · c) `0`.

**Démarche.** Une boucle sur `sizes`, un seul générateur créé avant elle, et à chaque tour la ligne de l'énoncé, puis `far.append(...)` ; on garde les fréquences de $n = 100$ et $n = 10\,000$ dans un dictionnaire pour les histogrammes. L'histogramme pour $n = 10\,000$ est beaucoup plus resserré autour de $\frac{1}{3}$ que celui pour $n = 100$. Pour la copie : la loi des grands nombres dit que la probabilité d'un écart donné entre fréquence et probabilité tend vers 0 quand $n$ grandit ; elle ne dit pas que la fréquence **égale** la probabilité, ni à partir de quel $n$. Pour un écart de 0,01 avec $n = 10\,000$, environ 3 % des séries resteraient au-delà : la proportion de a) ne tombe à 0 que pour des $n$ plus grands.

**Erreurs fréquentes.** Recréer le générateur à chaque tour de boucle ; oublier `np.abs` (seuls les écarts positifs comptent alors) ; confondre la fréquence des 500 séries avec la proportion de séries qui s'écartent.

### Ex R8.22 — Le diagramme en bâtons d'une loi

**Démarche.** `ax.bar(values, probabilities, width=0.2)`, l'espérance `sum(v * p for v, p in zip(values, probabilities))` calculée dans la fonction, `ax.axvline(mean, linestyle="--")`, puis le titre et les axes. Pour la copie : la loi est symétrique autour de 2 (1, 4, 6, 4, 1 sur 16), donc l'espérance vaut 2 sans calcul ; elle n'est pas plate, car chaque valeur regroupe un nombre différent de suites équiprobables, les coefficients $\binom{4}{k}$.

**Erreurs fréquentes.** Ouvrir une figure dans la fonction (`plt.figure`) au lieu de dessiner dans l'axe reçu ; écrire l'espérance en dur (2) au lieu de la calculer ; des bâtons de largeur 1 qui ressemblent à un histogramme.

### Ex R8.23 — Chasse à l'erreur : trois raisonnements de probabilités faux

**Réponses** : a) `"ABE"` · b) `[0.4375, 0.5, 0]`.

**Démarche.** (A) Les deux « 4 » peuvent arriver ensemble : on n'additionne pas. Par le contraire, $1 - \left(\frac{3}{4}\right)^2 = \frac{7}{16}$. (B) Les trois nombres de piles ne sont pas équiprobables : sur les 4 suites PP, PF, FP, FF, deux ont un seul pile, $\frac{1}{2}$. (E) Incompatibles, $A$ et $B$ ne se réalisent jamais ensemble : $P(A \cap B) = 0$ ; ils ne sont pas indépendants. (C) applique la définition de l'indépendance ; (D) additionne deux événements incompatibles : tous deux sont justes. (D) pouvait sembler faux parce qu'il additionne, comme (A) ; la différence est que rouge et vert ne peuvent pas arriver ensemble.

**Erreurs fréquentes.** Accuser (D) parce qu'il additionne ; croire (E) juste parce que la multiplication « ressemble » à l'indépendance.

### Ex R8.24 — Reproductibilité : générateur aléatoire et graine

**Démarche.** `rng = np.random.default_rng(seed)` avant la boucle, puis `[measure(rng) for _ in range(n_runs)]`. Les 5 mesures de `run_experiments(5, 42)` varient de quelques points (0,875, 0,86, 0,865, 0,84, 0,805) ; celles de `buggy_runs` sont toutes égales, car le générateur est recréé avec la même graine à chaque tour : il repart du même point. Pour la copie : l'écart entre les 5 mesures est la fluctuation d'un score mesuré sur 200 exemples ; une différence de cet ordre entre deux modèles peut venir du seul hasard, d'où l'intérêt de répéter les mesures avec plusieurs graines.

**Erreurs fréquentes.** Créer le générateur dans la boucle ; créer un générateur sans graine (`default_rng()`), qui donne d'autres mesures à chaque exécution.
