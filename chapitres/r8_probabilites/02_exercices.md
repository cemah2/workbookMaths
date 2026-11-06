# R8 · Probabilités de base — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r8_probabilites/06_mes_reponses.md` (créée par `python tools/start_chapter.py R8`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🧮 et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Pont, estimation, explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Garde les fractions jusqu'au bout, et dessine un arbre dès qu'une expérience a plusieurs étapes.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R8.Q1 — Univers, issue, événement 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. On lance une pièce cinq fois, en notant la suite des résultats. Combien l'univers a-t-il d'issues ?
2. On tire une carte d'un jeu de 32 cartes. « Obtenir un roi » est-il une issue ou un événement ? Combien d'issues contient-il ?
3. On lance une pièce quatre fois. Quel est le contraire de « au moins deux piles » ?
4. Vrai ou faux : un événement et son contraire sont toujours incompatibles.
5. Vrai ou faux : deux événements incompatibles sont toujours contraires l'un de l'autre.
6. On lance un dé à 6 faces ; $A$ = « pair » et $B$ = « au moins 5 ». Écris $A \cap B$ et $A \cup B$.

### R8.Q2 — Propriétés d'une probabilité 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. Une probabilité peut-elle valoir 1,2 ? Et −0,1 ?
2. $P(A) = 0{,}35$ : que vaut $P(\bar{A})$ ?
3. $P(A) = 0{,}5$, $P(B) = 0{,}4$ et $P(A \cap B) = 0{,}1$ : que vaut $P(A \cup B)$ ?
4. Vrai ou faux : $P(A \cup B) = P(A) + P(B)$ pour tous événements $A$ et $B$.
5. Une famille a deux enfants ; on suppose que chaque enfant est une fille ou un garçon avec la même probabilité, indépendamment l'un de l'autre. « Deux filles », « deux garçons » et « une fille et un garçon » ont-ils la même probabilité ?
6. Vrai ou faux : avec une pièce équilibrée, 10 lancers donnent exactement 5 piles.

### R8.Q3 — Arrangement ou combinaison ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Pour chaque situation, dis si l'ordre compte, s'il peut y avoir des répétitions, et quel outil compte les possibilités ($n^k$, arrangements, $n!$ ou $\binom{n}{k}$). Ne calcule pas.
1. Le podium (or, argent, bronze) d'une course de 10 coureurs.
2. Une main de 5 cartes.
3. Le code à 4 chiffres d'une carte bancaire.
4. Le bureau d'une association : un président et un trésorier, deux personnes différentes.
5. Les 3 chapitres que tu révises ce soir parmi 8, sans ordre de préférence.
6. L'ordre de passage de 6 élèves à un oral.

### R8.Q4 — Lire un arbre pondéré 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Un sachet mélange des graines de deux variétés : 60 % de variété A, 40 % de variété B. Une graine de A germe dans 90 % des cas, une graine de B dans 70 % des cas. On plante une graine prise au hasard. Dessine l'arbre, puis :
1. Quelle probabilité porte la branche « ne germe pas » qui suit A ?
2. Que vaut $P(A \cap \text{germe})$ ?
3. Que vaut $P(\text{germe})$ ?
4. Vrai ou faux : la somme des probabilités des quatre chemins vaut 1.
5. Le nombre 0,9 est-il $P(\text{germe})$, $P(A \cap \text{germe})$ ou $P(\text{germe} \mid A)$ ?
6. Vrai ou faux : on additionne les probabilités le long d'un chemin.

### R8.Q5 — Indépendants ou incompatibles ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. On lance un dé : « obtenir 1 » et « obtenir 6 » sont-ils incompatibles ? indépendants ?
2. On lance deux fois une pièce : « le premier lancer donne pile » et « le second lancer donne pile » sont-ils indépendants ?
3. Vrai ou faux : deux événements incompatibles, de probabilités non nulles, sont indépendants.
4. $P(A) = 0{,}5$, $P(B) = 0{,}2$, et $A$ et $B$ sont indépendants : que vaut $P(A \cap B)$ ?
5. $P(A) = 0{,}3$, $P(B) = 0{,}5$ et $P(A \cap B) = 0{,}2$ : $A$ et $B$ sont-ils indépendants ?
6. On tire deux cartes d'un jeu, sans remise : « la première est un as » et « la seconde est un as » sont-ils indépendants ?

### R8.Q6 — Espérance et variance : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §6 et §7 · parcours C, E*

Vrai ou faux ?
1. L'espérance d'une variable aléatoire est toujours l'une de ses valeurs.
2. Si $\mathbb{E}[X] = 4$, alors $\mathbb{E}[2X - 3] = 5$.
3. Une variance peut être négative.
4. Si $\mathbb{V}(X) = 9$, alors $\sigma(X) = 3$.
5. $\mathbb{V}(X + 10) = \mathbb{V}(X) + 10$.
6. $\mathbb{V}(-2X) = -2\,\mathbb{V}(X)$.
7. Une variable aléatoire constante a une variance nulle.

### R8.Q7 — Ce que dit la loi des grands nombres 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

1. Vrai ou faux : après six faces de suite, une pièce équilibrée a plus d'une chance sur deux de donner pile au lancer suivant.
2. On lance une pièce équilibrée 10 fois, puis, dans une autre expérience, 10 000 fois. Dans laquelle la fréquence des piles a-t-elle le plus de chances d'être entre 0,45 et 0,55 ?
3. Vrai ou faux : sur 10 000 lancers d'une pièce équilibrée, on obtient toujours entre 4 990 et 5 010 piles.
4. Par combien faut-il multiplier le nombre d'essais pour diviser par 10 l'écart typique entre une fréquence et la probabilité ?
5. Deux simulations lancées avec la même graine donnent-elles la même fréquence ? Et avec deux graines différentes ?
6. Vrai ou faux : la loi des grands nombres garantit que, sur un million d'essais, la fréquence est égale à la probabilité.

<a id="rappels"></a>

## 🔁 Rappels

### R8.R1 — Ensembles et complémentaire (R4) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

Dans $\Omega = \{a, b, c, d, e, f\}$, on pose $A = \{a, b, c\}$ et $B = \{c, d\}$.
1. $A \cap B$ et $A \cup B$ ?
2. $\bar{A}$ ?
3. Retrouve $|A \cup B|$ avec la formule $|A| + |B| - |A \cap B|$.
4. $\bar{A} \cap \bar{B}$, et vérifie qu'il est égal au complémentaire de $A \cup B$.

### R8.R2 — Σ et Π (R4) 🔁 ★ ⏱️ 5 min
*Fiche §7 · parcours C, E*

1. $\sum_{k=1}^{4} k^2$ ?
2. $\sum_{i=1}^{3} x_i\,p_i$ pour $x = (-1, 0, 2)$ et $p = (0{,}2 ;\ 0{,}5 ;\ 0{,}3)$ ?
3. $\prod_{k=1}^{5} k$ ?
4. $\prod_{k=1}^{3} \left(1 - \frac{k}{10}\right)$ ?

### R8.R3 — Fractions (R1) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C*

Donne chaque résultat sous forme de fraction irréductible.
1. $\frac{2}{6} \times \frac{1}{5}$
2. $1 - \frac{8}{27}$
3. $\frac{3}{8} + \frac{1}{4}$
4. $\frac{84}{504}$
5. $\left(\frac{1}{2}\right)^5$

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.5`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/7"` ;
- une liste de nombres entre crochets, comme `[0.25, 0.5, 0.25]` ; vrai ou faux par `True` ou `False`.

### Ex R8.1 — Décrire univers et événements : dés, cartes, pièces ✏️ ★ ⏱️ 10 min
**Objectif :** décrire un univers, compter les issues d'un événement, et traduire « et », « ou », « ni… ni… » en opérations sur les ensembles.
**Prérequis :** fiche §1 ; R4 (ensembles) · **Parcours :** C, E

On lance quatre pièces, en notant la suite des résultats (P ou F). Puis, séparément, on tire une carte d'un jeu de 32 cartes : 4 couleurs (pique ♠ et trèfle ♣ sont noirs, cœur ♥ et carreau ♦ sont rouges), et 8 hauteurs par couleur (7, 8, 9, 10, valet, dame, roi, as). Pour la carte, $A$ = « un as » et $B$ = « une carte noire ».

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre d'issues de l'univers des quatre pièces | un entier |
| b | le nombre d'issues de « exactement deux piles » | un entier |
| c | le nombre d'issues de « au moins un pile » | un entier |
| d | le nombre d'issues de « au plus un pile » | un entier |
| e | $\lvert A \cap B \rvert$ | un entier |
| f | $\lvert A \cup B \rvert$ | un entier |
| g | le nombre de cartes qui ne sont ni un as ni une carte noire | un entier |
| h | $A$ et « une carte rouge » sont-ils incompatibles ? | vrai ou faux |

### Ex R8.2 — Probabilités par équiprobabilité ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des probabilités en comptant des issues équiprobables, et passer par le contraire.
**Prérequis :** fiche §2 · **Parcours :** C, E

On choisit au hasard l'une des 11 lettres du mot PROBABILITE (chaque position a la même chance d'être choisie). Puis, séparément, on lance un dé équilibré à 6 faces et un dé équilibré à 4 faces.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(\text{la lettre est un B})$ | une fraction |
| b | $P(\text{la lettre est une voyelle})$ (A, E, I, O, U, Y) | une fraction |
| c | $P(\text{la lettre est une consonne autre que B})$ | une fraction |
| d | le nombre d'issues de l'univers des deux dés | un entier |
| e | $P(\text{la somme des deux dés vaut } 5)$ | une fraction |
| f | $P(\text{la somme vaut au moins } 9)$ | une fraction |
| g | $P(\text{le dé à 6 faces donne un nombre strictement plus grand que le dé à 4 faces})$ | une fraction |
| h | $P(\text{le produit des deux nombres est pair})$ (passe par le contraire) | une fraction |

### Ex R8.3 — P(A ∪ B) et le complémentaire ✏️ ★★ ⏱️ 15 min
**Objectif :** utiliser la formule de la réunion, le complémentaire et les lois de De Morgan.
**Prérequis :** fiche §2 ; R4 (De Morgan) · **Parcours :** C, E

$A$ et $B$ sont deux événements d'une même expérience. Réponses à 2 décimales, sauf en g.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(A) = 0{,}45$, $P(B) = 0{,}3$ et $P(A \cap B) = 0{,}15$ : $P(A \cup B)$ | un nombre |
| b | avec les mêmes données, $P(\bar{A} \cap \bar{B})$ (« ni $A$ ni $B$ ») | un nombre |
| c | avec les mêmes données, $P(A \cap \bar{B})$ (« $A$ mais pas $B$ ») | un nombre |
| d | $A$ et $B$ sont incompatibles, $P(A) = 0{,}2$ et $P(A \cup B) = 0{,}65$ : $P(B)$ | un nombre |
| e | $P(A) = 0{,}7$ et $P(B) = 0{,}6$ : $A$ et $B$ peuvent-ils être incompatibles ? | vrai ou faux |
| f | 60 % des utilisateurs d'un site ont son appli mobile, 45 % reçoivent sa newsletter, et 20 % n'ont ni l'une ni l'autre. On choisit un utilisateur au hasard : la probabilité qu'il ait l'appli **et** la newsletter | un nombre |
| g | on lance quatre pièces : $P(\text{au moins un face})$ | une fraction |
| h | $P(A) = 0{,}55$, $P(B) = 0{,}35$ et $P(A \cup B) = 0{,}7$ : $P(A \cap B)$ | un nombre |

### Ex R8.4 — Principe multiplicatif et factorielles ✏️ ★ ⏱️ 15 min
**Objectif :** compter des choix successifs, avec ou sans répétition, et calculer avec des factorielles.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de mots de passe de 6 lettres minuscules (26 lettres, une lettre peut revenir) | un entier |
| b | le même nombre, quand les 6 lettres sont toutes différentes | un entier |
| c | $7!$ | un entier |
| d | le nombre de podiums (or, argent, bronze) possibles dans une course de 8 coureurs | un entier |
| e | un restaurant propose 4 entrées, 5 plats et 3 desserts : le nombre de menus entrée-plat-dessert | un entier |
| f | le nombre d'ordres possibles pour exécuter 5 tâches, quand la tâche A doit passer en premier | un entier |
| g | $\frac{9!}{7!}$ (simplifie avant de calculer) | un entier |
| h | le nombre d'immatriculations formées de 2 lettres puis 3 chiffres (toutes les lettres et tous les chiffres sont permis) | un entier |

### Ex R8.5 — Combinaisons et triangle de Pascal ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des coefficients binomiaux, utiliser leur symétrie et le triangle de Pascal, et s'en servir pour une probabilité.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\binom{7}{3}$ | un entier |
| b | 15 personnes se serrent la main, chacune une fois avec chaque autre : le nombre de poignées de main | un entier |
| c | $\binom{20}{18}$ (sers-toi de la symétrie) | un entier |
| d | la ligne $n = 7$ du triangle de Pascal, de $\binom{7}{0}$ à $\binom{7}{7}$ | une liste |
| e | la somme des nombres de la ligne $n = 9$ du triangle (sans la calculer terme à terme) | un entier |
| f | le nombre de mains de 5 cartes dans un jeu de 32 cartes | un entier |
| g | la probabilité qu'une main de 5 cartes, tirée au hasard dans un jeu de 32, contienne les 4 as | une fraction |
| h | le nombre de chemins sur un quadrillage de 4 × 4 cases, du coin en bas à gauche au coin en haut à droite, en ne se déplaçant que d'un côté de case vers la droite ou vers le haut | un entier |

### Ex R8.6 — Arbres pondérés : tirages successifs ✏️ ★★ ⏱️ 20 min
**Objectif :** construire un arbre pondéré, calculer des probabilités de chemins et d'événements, avec et sans remise.
**Prérequis :** fiche §4 · **Parcours :** C, E

Une appli de navigation propose l'itinéraire A dans 60 % des cas, l'itinéraire B sinon. Par A, on arrive en retard dans 10 % des cas ; par B, dans 25 % des cas. Réponses de a à c à 2 décimales.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(A \cap \text{retard})$ | un nombre |
| b | $P(\text{retard})$ | un nombre |
| c | $P(B \cap \text{à l'heure})$ | un nombre |

Un tiroir contient 4 chaussettes noires et 6 grises. On en prend deux au hasard, l'une après l'autre, **sans remise**. Puis un QCM de 3 questions, chacune à 4 choix dont un seul est juste. Réponses de d à h en fractions irréductibles.

| | Question | Réponse attendue |
|---|---|---|
| d | $P(\text{deux chaussettes noires})$ | une fraction |
| e | $P(\text{deux chaussettes de la même couleur})$ | une fraction |
| f | $P(\text{la seconde chaussette est noire})$ | une fraction |
| g | $P(\text{deux chaussettes noires})$ si l'on remet la première dans le tiroir avant de tirer la seconde | une fraction |
| h | on répond au QCM au hasard : $P(\text{au moins une bonne réponse})$ | une fraction |

Dans ta copie : compare f à la probabilité que la **première** chaussette soit noire. Est-ce une coïncidence ?

### Ex R8.7 — Indépendance : tester P(A ∩ B) = P(A) P(B) avec des cartes et des pièces ✏️ ★★ ⏱️ 15 min
**Objectif :** décider de l'indépendance de deux événements par le calcul, et distinguer indépendance et incompatibilité.
**Prérequis :** fiche §5 · **Parcours :** C, E

On tire une carte au hasard dans un jeu de 32 cartes (celui de R8.1) : $A$ = « un as », $B$ = « un cœur », $C$ = « une figure » (valet, dame ou roi) et $D$ = « une carte rouge ». Puis on lance deux pièces : $E$ = « la première pièce donne pile », $F$ = « les deux pièces tombent du même côté ». Enfin, on lance trois pièces : $G$ = « au moins deux piles », $H$ = « la première pièce donne pile ».

| | Question | Réponse attendue |
|---|---|---|
| a | $P(A \cap B)$ | une fraction |
| b | $A$ et $B$ sont-ils indépendants ? | vrai ou faux |
| c | $A$ et $C$ sont-ils indépendants ? | vrai ou faux |
| d | $B$ et $D$ sont-ils indépendants ? | vrai ou faux |
| e | $P(E \cap F)$ | une fraction |
| f | $E$ et $F$ sont-ils indépendants ? | vrai ou faux |
| g | $P(G \cap H)$ | une fraction |
| h | $G$ et $H$ sont-ils indépendants ? | vrai ou faux |

Dans ta copie : pour chaque couple non indépendant, dis si savoir que le premier événement s'est réalisé rend le second plus ou moins probable.

### Ex R8.8 — La loi d'une variable aléatoire ✏️ ★ ⏱️ 15 min
**Objectif :** établir la loi d'une variable aléatoire discrète, et s'en servir pour calculer des probabilités.
**Prérequis :** fiche §6 · **Parcours :** C, E

On lance trois pièces, et $X$ est le nombre de piles. Puis on lance deux fois un dé à 4 faces, et $Y$ est le plus grand des deux numéros obtenus (ce numéro, s'ils sont égaux). Les lois se donnent comme des listes, dans l'ordre croissant des valeurs.

| | Question | Réponse attendue |
|---|---|---|
| a | la loi de $X$ : $[P(X = 0), P(X = 1), P(X = 2), P(X = 3)]$ | une liste (3 décimales) |
| b | $P(X \ge 2)$ | un nombre (3 décimales) |
| c | la loi de $Y$ : $[P(Y = 1), P(Y = 2), P(Y = 3), P(Y = 4)]$ | une liste (4 décimales) |
| d | $P(Y \le 2)$ | un nombre (2 décimales) |

Une variable $Z$ prend les valeurs 1, 2, 3 et 4, avec $P(Z = 1) = 0{,}15$, $P(Z = 2) = 0{,}35$ et $P(Z = 4) = 0{,}2$. Puis on tire une carte d'un jeu de 32 : on gagne 5 € pour un as, 2 € pour une figure (valet, dame ou roi), et on perd 1 € sinon ; $W$ est le gain.

| | Question | Réponse attendue |
|---|---|---|
| e | $P(Z = 3)$ | un nombre (2 décimales) |
| f | $P(Z > 1)$ | un nombre (2 décimales) |
| g | la loi de $W$ : $[P(W = -1), P(W = 2), P(W = 5)]$ | une liste (3 décimales) |
| h | $P(W \le 2)$ | un nombre (3 décimales) |

### Ex R8.9 — Espérance, variance (avec V = E[X²] − E[X]²) et écart-type ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer l'espérance, la variance et l'écart-type d'une variable discrète, et l'effet d'un changement d'échelle.
**Prérequis :** fiche §7 ; Ex R8.8 · **Parcours :** C, E

Le nombre $X$ de buts marqués par une équipe de hockey sur glace pendant un match suit la loi :

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $P(X = x)$ | 0,2 | 0,4 | 0,3 | 0,1 |

Un classement donne à l'équipe 10 points par but, moins une pénalité fixe de 4 points par match : son score est $S = 10X - 4$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{E}[X]$ | un nombre (2 décimales) |
| b | $\mathbb{E}[X^2]$ | un nombre (2 décimales) |
| c | $\mathbb{V}(X)$, avec la formule $\mathbb{E}[X^2] - \mathbb{E}[X]^2$ | un nombre (2 décimales) |
| d | $\sigma(X)$ | un nombre (2 décimales) |
| e | $\mathbb{E}[S]$ | un nombre (2 décimales) |
| f | $\mathbb{V}(S)$ | un nombre (2 décimales) |
| g | $\mathbb{E}[Y]$, pour la variable $Y$ de R8.8 (le plus grand de deux lancers d'un dé à 4 faces) | une fraction |
| h | $\mathbb{V}(Y)$ | une fraction |

### Ex R8.10 — Un jeu est-il équitable ? ✏️ ★★ ⏱️ 20 min
**Objectif :** juger un jeu par son espérance, trouver la mise qui le rend équitable, et comparer deux jeux par leur dispersion.
**Prérequis :** fiche §7 · **Parcours :** C

**Jeu A** : on lance deux pièces ; deux piles font gagner 8 €, un seul pile 1 €, aucun pile rien. **Jeu B** : on lance un dé à 6 faces ; un 6 rapporte 6 €, sinon rien. La somme gagnée s'appelle le **prix** ; la **mise**, payée avant chaque partie, n'est jamais rendue, et le gain net est le prix moins la mise. Réponses à 2 décimales.

| | Question | Réponse attendue |
|---|---|---|
| a | l'espérance du prix du jeu A, en euros | un nombre |
| b | le gain net moyen par partie du jeu A, quand la mise est de 3 € | un nombre |
| c | avec cette mise, ce que l'organisateur gagne en moyenne sur 200 parties, en euros | un nombre |
| d | la variance du prix du jeu A | un nombre |
| e | l'écart-type du prix du jeu A | un nombre |
| f | l'espérance du prix du jeu B | un nombre |
| g | la variance du prix du jeu B | un nombre |
| h | le prix à offrir pour un 6 pour que le jeu B soit équitable avec une mise de 1,50 € | un nombre |

Dans ta copie : chaque jeu est rendu équitable (la mise est égale à l'espérance du prix). Lequel des deux préfères-tu jouer, et pourquoi ? Que mesure la différence entre leurs écarts-types ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex R8.11 — Démontrer C(n, k) = C(n − 1, k − 1) + C(n − 1, k) ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer la formule de Pascal de deux façons, par le calcul et par un raisonnement de comptage.
**Prérequis :** fiche §3 · **Parcours :** C

Soient $n \ge 2$ et $k$ deux entiers, avec $1 \le k \le n - 1$.
1. Vérifie la formule sur un exemple : calcule $\binom{6}{3}$, $\binom{5}{2}$ et $\binom{5}{3}$.
2. **Par le calcul.** Écris $\binom{n - 1}{k - 1}$ et $\binom{n - 1}{k}$ avec des factorielles, mets-les au même dénominateur $k!\,(n - k)!$ (utilise $k! = k \times (k - 1)!$ et $(n - k)! = (n - k) \times (n - k - 1)!$), puis additionne.
3. **Par le comptage.** On choisit $k$ objets parmi $n$, et l'on regarde un objet particulier, le premier. Combien de choix le contiennent ? Combien ne le contiennent pas ? Conclus.
4. Montre, par un raisonnement de comptage, que la somme de la ligne $n$ du triangle, $\sum_{k=0}^{n} \binom{n}{k}$, vaut $2^n$ (que compte chacun des deux membres ?).
5. Pourquoi l'énoncé demande-t-il $1 \le k \le n - 1$ ? Que devient la formule pour $k = 0$ avec la convention $\binom{n - 1}{-1} = 0$ ?

### Ex R8.12 — L'espérance d'une somme : E[X + Y] = E[X] + E[Y], même pour des variables liées ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer la linéarité de l'espérance en sommant sur les issues, et s'en servir pour calculer une espérance sans connaître la loi.
**Prérequis :** fiche §6 et §7 ; R4 (Σ) · **Parcours :** C, E

Un univers fini $\Omega$ porte une probabilité, de poids $p(\omega)$ pour chaque issue $\omega$. On admet que l'espérance d'une variable aléatoire $X$ s'écrit aussi comme une somme sur les **issues** :
$$\mathbb{E}[X] = \sum_{\omega \in \Omega} X(\omega)\,p(\omega).$$
1. On lance trois pièces, et $X$ est le nombre de piles. Calcule $\mathbb{E}[X]$ de deux façons : avec la loi de $X$ (somme sur les valeurs), puis avec la somme sur les 8 issues. Explique pourquoi les deux sommes sont toujours égales (regroupe les issues qui donnent la même valeur de $X$).
2. $X$ et $Y$ sont deux variables aléatoires définies sur le même univers. Démontre que $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$. As-tu supposé que $X$ et $Y$ sont indépendantes ?
3. Déduis-en que $\mathbb{E}[aX + bY + c] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y] + c$ pour tous réels $a$, $b$ et $c$. Quel cas particulier redonne la formule $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$ de la fiche ?
4. On lance 10 fois une pièce équilibrée. Pour $i$ de 1 à 10, $X_i$ vaut 1 si le $i$-ème lancer donne pile, 0 sinon. Écris le nombre $N$ de piles à l'aide des $X_i$, et déduis $\mathbb{E}[N]$ de 2, sans calculer la loi de $N$.
5. L'espérance d'un **produit** n'est pas toujours le produit des espérances : on lance une seule pièce, et $X = Y$ vaut 1 si elle donne pile, 0 sinon. Compare $\mathbb{E}[XY]$ et $\mathbb{E}[X]\,\mathbb{E}[Y]$.

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Pont, estimation, explication

### Ex R8.13 — Comparer toutes les paires : un tournoi, C(n, 2) et une croissance en n² 🔗 ★ ⏱️ 10 min
**Objectif :** compter les paires d'un ensemble, et voir pourquoi ce nombre grandit comme le carré de la taille.
**Prérequis :** fiche §3 · **Parcours :** C, E

Un tournoi réunit 16 équipes, et chaque équipe rencontre chaque autre une fois. Puis, dans un dataset de $n$ exemples, on compare chaque exemple à chaque autre, une fois par paire (pour repérer des doublons, ou chercher les plus proches voisins).

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de matchs du tournoi | un entier |
| b | le nombre de matchs si chaque paire d'équipes joue un match aller et un match retour | un entier |
| c | le nombre de comparaisons pour $n = 1\,000$ | un entier |
| d | le rapport entre le nombre de comparaisons pour $n = 10\,000$ et celui pour $n = 1\,000$ | un entier (arrondi à l'unité) |
| e | chaque comparaison prend une microseconde : la durée de toutes les comparaisons pour $n = 1\,000\,000$, en heures | un nombre (1 décimale) |
| f | le nombre de groupes de 3 exemples pour $n = 100$ | un entier |

Dans ta copie : pourquoi $\binom{n}{2} \approx \frac{n^2}{2}$ quand $n$ est grand ? Que devient la durée de e si $n$ est multiplié par 10 ? Et le nombre de groupes de 3 ?

### Ex R8.14 — Fermi : la probabilité de croiser quelqu'un que l'on connaît dans le métro 🧮 ★★ ⏱️ 20 min
**Objectif :** estimer une probabilité par des ordres de grandeur, avec le complémentaire et des répétitions indépendantes.
**Prérequis :** fiche §2 et §5 · **Parcours :** C

Tu prends le métro dans une grande ville. Quelle est la probabilité de croiser, pendant un trajet, au moins une personne que tu connais ? Fais une estimation de Fermi, en écrivant chaque hypothèse et son ordre de grandeur :
1. combien de personnes connais-tu assez pour les reconnaître et les saluer, et combien d'entre elles prennent ce métro un jour donné ?
2. combien de personnes le métro transporte-t-il par jour ? Déduis-en la probabilité $q$ qu'un voyageur croisé au hasard soit l'une de tes connaissances ;
3. combien de voyageurs croises-tu pendant un trajet (dans ta rame, sur les quais, dans les couloirs) ?
4. en supposant ces rencontres indépendantes, calcule $1 - (1 - q)^N$ ; compare avec $N \times q$ quand $N q$ est petit, et explique pourquoi les deux sont proches ;
5. sur une année de trajets, quelle est la probabilité d'au moins une telle rencontre ? Quelle hypothèse de ton modèle te semble la plus fragile ?

### Ex R8.15 — Expliquer la différence entre probabilité et fréquence 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement ce qui distingue une probabilité d'une fréquence, et ce qui les relie.
**Prérequis :** fiche §2 et §8 · **Parcours :** C, E

Un ami te dit : « La météo annonce 30 % de chances de pluie demain. Et mon appli dit que j'ai mis mon parapluie pour rien 7 fois sur 10 cette année. C'est pareil, non ? »

Réponds-lui **en huit lignes au plus, sans formule**. Ta réponse doit dire : ce qu'est une probabilité, ce qu'est une fréquence, laquelle change d'une série d'observations à l'autre, ce qui les relie quand les répétitions sont nombreuses (la loi des grands nombres), et une limite de cette idée pour la pluie de demain, qui n'arrive qu'une fois.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r8_probabilites/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R8.16 | Factorielle et combinaisons · `factorial`, `binomial` | 🔨 | ★ | 15 | C, E |
| R8.17 | Une probabilité exacte par énumération · `enumerate_probability` | 🔨 | ★★ | 25 | C |
| R8.18 | Espérance et variance d'une loi · `expectation`, `variance` | 🔨 | ★ | 15 | C, E |
| R8.19 | Estimer une probabilité par simulation · `simulate_frequency` | 🔨 | ★★ | 20 | C, E |
| R8.20 | Prédire : dans une classe de 30, deux élèves ont-ils le même anniversaire ? | 🔮 | ★★ | 15 | C, E |
| R8.21 | La loi des grands nombres : fréquence et nombre de lancers | 🔬 | ★★ | 20 | C, E |
| R8.22 | Le diagramme en bâtons d'une loi | 🎨 | ★ | 10 | C |
| R8.23 | Chasse à l'erreur : trois raisonnements de probabilités faux | 🐛 | ★★ | 20 | C, E |
| R8.24 | Reproductibilité : générateur aléatoire et graine | 🛠️ | ★ | 15 | C, E |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
