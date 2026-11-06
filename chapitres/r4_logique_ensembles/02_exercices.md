# R4 · Logique, ensembles, Σ et Π — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r4_logique_ensembles/06_mes_reponses.md` (créée par `python tools/start_chapter.py R4`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, ⚖️ et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 ⚖️ 🗣️ Pont, esprit critique et explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Sans calculatrice.** Tout ce fichier se fait à la main. Pour une table de vérité, écris toutes les lignes ; pour une somme, écris d'abord les premiers termes en extension ; pour une démonstration, écris des phrases.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R4.Q1 — Vrai, faux, ou pas une proposition ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Pour chaque phrase : vraie, fausse, ou pas une proposition ?
1. « 91 est un nombre premier. »
2. « Range ta chambre. »
3. « $x > 3$ »
4. « $2 + 2 = 4$ ou la Lune est en fromage. »
5. « 10 est pair et 10 est divisible par 4. »
6. « Non ($7 > 2$). »

### R4.Q2 — Réciproque ou contraposée ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

On part de l'implication « s'il pleut, alors le sol est mouillé ».
1. « Si le sol est mouillé, alors il pleut » : réciproque, contraposée, ou ni l'une ni l'autre ?
2. « Si le sol n'est pas mouillé, alors il ne pleut pas » : réciproque, contraposée, ou ni l'une ni l'autre ?
3. « S'il ne pleut pas, alors le sol n'est pas mouillé » : réciproque, contraposée, ou ni l'une ni l'autre ?
4. Laquelle de ces trois phrases a toujours la même valeur de vérité que l'implication de départ ?
5. Vrai ou faux : quand une implication est vraie, sa réciproque l'est aussi.
6. Écris la négation de l'implication de départ.

### R4.Q3 — Nier une phrase avec « pour tout » 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. La négation de « tous les élèves ont rendu leur devoir » est-elle « aucun élève n'a rendu son devoir », « au moins un élève n'a pas rendu son devoir », ou « tous les élèves n'ont pas rendu leur devoir » ?
2. Écris la négation de « $\forall x \in \mathbb{R},\ x^2 + 1 > 0$ ».
3. Écris la négation de « $\exists n \in \mathbb{N},\ n > 100$ et $n$ est pair ».
4. Vrai ou faux : la négation de « $x > 2$ » est « $x < 2$ ».
5. Vrai ou faux : « $\forall x \in \mathbb{R},\ \exists y \in \mathbb{R},\ x + y = 0$ ».

### R4.Q4 — Ensembles : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

On pose $A = \{1, 4, 9\}$. Vrai ou faux ?
1. $4 \in A$.
2. $\{4\} \in A$.
3. $\varnothing \subset A$.
4. $A \cap \varnothing = A$.
5. $\lvert \{1, 1, 4\} \rvert = 3$.
6. $\mathbb{N} \subset \mathbb{Z}$.
7. $]0 \;;\; 1[\, \cap\, [1 \;;\; 2] = \varnothing$.

### R4.Q5 — Lire une somme Σ 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Combien de termes compte $\sum_{k=4}^{10} a_k$ ?
2. Écris $\sum_{j=0}^{3} (j + 2)$ en extension, sans la calculer.
3. Vrai ou faux : $\sum_{i=1}^{5} i^2 = \sum_{k=1}^{5} k^2$.
4. Que vaut $\sum_{k=1}^{n} 7$ ?
5. Vrai ou faux : $\sum_{k=1}^{n} a_k b_k = \left(\sum_{k=1}^{n} a_k\right)\left(\sum_{k=1}^{n} b_k\right)$ pour tous nombres $a_k$, $b_k$.
6. Vrai ou faux : $\prod_{k=1}^{n} (2 a_k) = 2 \prod_{k=1}^{n} a_k$.

### R4.Q6 — Quel raisonnement pour quelle affirmation ? 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

Pour chaque affirmation, quel raisonnement choisirais-tu (direct, contraposée, absurde, contre-exemple, disjonction de cas, récurrence) ?
1. « Tout entier naturel est la somme de deux carrés d'entiers » (indice : c'est faux).
2. « Il n'existe pas de plus grand nombre premier. »
3. « Pour tout entier $n \ge 0$, $7^n - 1$ est divisible par 6. »
4. « Pour un entier $n$, si $n^2$ est impair, alors $n$ est impair » (en partant de $n$ plutôt que de $n^2$).
5. « Pour tout réel $x$, $x^2 - 6x + 9 \ge 0$. »
6. « Pour tout réel $x$, $\max(x, -x) = \lvert x \rvert$. »

### R4.Q7 — Les deux étapes d'une récurrence 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

1. Comment s'appellent les deux étapes d'une démonstration par récurrence ?
2. Dans l'hérédité, que suppose-t-on, et que démontre-t-on ?
3. Vrai ou faux : vérifier $P(1), P(2), \dots, P(100)$ démontre $P(n)$ pour tout $n \ge 1$.
4. Pour démontrer une propriété « pour tout $n \ge 3$ », par quelle valeur de $n$ commence l'initialisation ?
5. Vrai ou faux : avec une hérédité juste mais sans initialisation, on peut « démontrer » une propriété fausse.

### R4.Q8 — Ce qui manque dans une démonstration 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

Que reproches-tu à chacune de ces « démonstrations » ?
1. « La somme de deux impairs est paire : $3 + 5 = 8$, $7 + 11 = 18$, $1 + 1 = 2$. »
2. « Montrons que si $n$ est pair, alors $n^2$ est pair. On suppose $n^2$ pair ; alors $n^2 = 2k$, donc $n$ est pair. »
3. « Montrons que pour tout réel $x$, $\lvert x - 1 \rvert \le \lvert x \rvert + 1$. On a $x \ge 1$, donc $\lvert x - 1 \rvert = x - 1 \le x + 1 = \lvert x \rvert + 1$. »
4. « Montrons que pour tous réels $a, b \ge 0$, $\sqrt{ab} \le \frac{a + b}{2}$. On a $\sqrt{ab} \le \frac{a + b}{2}$, donc $4ab \le (a + b)^2$, donc $0 \le (a - b)^2$, ce qui est vrai. »

<a id="rappels"></a>

## 🔁 Rappels

### R4.R1 — Résoudre une inéquation (R2) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Résous $7 - 3x < 1$ et donne l'ensemble des solutions sous forme d'intervalle.
2. Résous $2(x - 1) \ge 5x + 4$.
3. Écris la négation de « $x \ge 2$ », puis l'ensemble des réels qui la vérifient : comment s'appelle cet ensemble par rapport à $[2 \;;\; +\infty[$ ?

### R4.R2 — Composer deux fonctions (R3) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C*

On pose $f(x) = 3 - x$ et $g(x) = x^2 + 1$.
1. Calcule $(f \circ g)(2)$ et $(g \circ f)(2)$.
2. Donne une expression de $(f \circ g)(x)$ et de $(g \circ f)(x)$.
3. Vrai ou faux : « pour tout réel $x$, $(f \circ g)(x) = (g \circ f)(x)$ ». Justifie par un contre-exemple ou une démonstration.

### R4.R3 — Additionner des fractions (R1) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

1. Calcule $\frac{1}{2} + \frac{1}{3} + \frac{1}{6}$.
2. Vérifie que $\frac{1}{3} - \frac{1}{4} = \frac{1}{12}$, puis que $\frac{1}{k} - \frac{1}{k + 1} = \frac{1}{k(k + 1)}$ pour tout entier $k \ge 1$.
3. Calcule $\frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4}$ de deux façons : en réduisant au même dénominateur, puis avec la question 2.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main**, en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- une **colonne de table de vérité** par la liste de ses valeurs, dans l'ordre des lignes VV, VF, FV, FF (pour trois propositions : VVV, VVF, VFV, VFF, FVV, FVF, FFV, FFF), écrites `True` et `False` (ou les lettres V et F, entre guillemets) ;
- vrai ou faux par `True` ou `False` ;
- un numéro de réponse proposée par un nombre entier ;
- un **ensemble** par la liste de ses éléments, dans l'ordre que tu veux, la liste vide pour $\varnothing$ ;
- un nombre avec un point décimal, une fraction exacte entre guillemets (`"5/7"`), une expression entre guillemets (`"3*n**2 + 1"`), un intervalle entre guillemets (`"]-1 ; 4]"`).

### Ex R4.1 — Tables de vérité de « et », « ou », « non » et de l'implication ✏️ ★ ⏱️ 15 min
**Objectif :** construire des tables de vérité, et s'en servir pour reconnaître deux propositions équivalentes.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

Dresse dans ta copie la table de vérité de chaque proposition, puis donne sa colonne.

| | Question | Réponse attendue |
|---|---|---|
| a | la colonne de « non (P et Q) » | une liste de 4 valeurs |
| b | la colonne de « (non P) ou (non Q) » | une liste de 4 valeurs |
| c | a et b ont-elles la même colonne ? | vrai ou faux |
| d | la colonne de $P \Rightarrow Q$ | une liste de 4 valeurs |
| e | la colonne de $Q \Rightarrow P$ | une liste de 4 valeurs |
| f | la colonne de $(\text{non } Q) \Rightarrow (\text{non } P)$ | une liste de 4 valeurs |
| g | parmi d, e et f, les lettres des deux propositions qui ont la même colonne | un texte, comme `"ab"` |
| h | le nombre de lignes de la table de vérité d'une proposition qui dépend de trois propositions P, Q et R | un nombre entier |
| i | le nombre de lignes de cette table où « (P ou Q) et (non R) » est vraie | un nombre entier |

### Ex R4.2 — Réciproque, contraposée, négation : écrire les trois ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire la réciproque, la contraposée et la négation d'une implication, et trouver leurs valeurs de vérité.
**Prérequis :** fiche §2 et §3 · **Parcours :** C, E

Pour chacune des quatre implications, écris dans ta copie, en français, sa réciproque, sa contraposée et sa négation (n'oublie pas le « pour tout » dans la négation), puis donne la liste `[implication, réciproque, contraposée, négation]` de leurs valeurs de vérité.
- A : « Pour tout entier $n$, si $n$ est divisible par 6, alors $n$ est divisible par 3. »
- B : « Pour tout réel $x$, si $x^2 > 25$, alors $x > 5$. »
- C : « Pour tout entier $n \ge 2$, si $n$ est impair, alors $n$ est premier. »
- D : « Pour tout réel $x$, si $3x - 2 = 10$, alors $x = 4$. »

| | Question | Réponse attendue |
|---|---|---|
| a | les quatre valeurs de vérité pour A | une liste de 4 valeurs |
| b | les quatre valeurs de vérité pour B | une liste de 4 valeurs |
| c | les quatre valeurs de vérité pour C | une liste de 4 valeurs |
| d | les quatre valeurs de vérité pour D | une liste de 4 valeurs |
| e | l'unique contre-exemple de C compris entre 2 et 10 | un nombre entier |
| f | le plus grand entier négatif qui contredit B | un nombre entier |

### Ex R4.3 — Nier des phrases à deux quantificateurs ✏️ ★★ ⏱️ 20 min
**Objectif :** nier une phrase qui contient plusieurs quantificateurs, et décider si elle est vraie.
**Prérequis :** fiche §3 · **Parcours :** C, E

**a)** Quelle est la négation de « $\forall x \in \mathbb{R},\ \exists y \in \mathbb{R},\ y > x$ » ?
1. $\forall x \in \mathbb{R},\ \exists y \in \mathbb{R},\ y \le x$
2. $\exists x \in \mathbb{R},\ \forall y \in \mathbb{R},\ y \le x$
3. $\exists x \in \mathbb{R},\ \exists y \in \mathbb{R},\ y \le x$
4. $\exists y \in \mathbb{R},\ \forall x \in \mathbb{R},\ y > x$

**b)** La phrase de départ de a) est-elle vraie ?

**c)** Quelle est la négation de « $\exists M \in \mathbb{R},\ \forall x \in \mathbb{R},\ x^2 \le M$ » ?
1. $\forall M \in \mathbb{R},\ \exists x \in \mathbb{R},\ x^2 > M$
2. $\forall M \in \mathbb{R},\ \forall x \in \mathbb{R},\ x^2 > M$
3. $\exists M \in \mathbb{R},\ \exists x \in \mathbb{R},\ x^2 > M$
4. $\forall M \in \mathbb{R},\ \exists x \in \mathbb{R},\ x^2 \ge M$

**d)** La phrase de départ de c) est-elle vraie ?

**e)** Donne la liste des valeurs de vérité des deux phrases « $\forall x \in \mathbb{R},\ \exists y \in \mathbb{R},\ y^2 = x$ » et « $\exists y \in \mathbb{R},\ \forall x \in \mathbb{R},\ x\,y = 0$ », dans cet ordre.

**f)** Quelle est la négation de « pour tout $\varepsilon > 0$, il existe un entier $N \ge 1$ tel que $\frac{1}{N} < \varepsilon$ » ?
1. Il existe $\varepsilon > 0$ tel que, pour tout entier $N \ge 1$, $\frac{1}{N} \ge \varepsilon$.
2. Pour tout $\varepsilon > 0$ et tout entier $N \ge 1$, $\frac{1}{N} \ge \varepsilon$.
3. Il existe $\varepsilon \le 0$ tel que, pour tout entier $N \ge 1$, $\frac{1}{N} \ge \varepsilon$.
4. Il existe $\varepsilon > 0$ et un entier $N \ge 1$ tels que $\frac{1}{N} \ge \varepsilon$.

**g)** La phrase de départ de f) est-elle vraie ?

Pour a, c et f, la réponse est le numéro choisi ; pour b, d et g, vrai ou faux ; pour e, une liste de deux valeurs.

### Ex R4.4 — Opérations sur des ensembles et dénombrement ✏️ ★ ⏱️ 15 min
**Objectif :** décrire en extension des ensembles définis par une propriété, les combiner, et compter leurs éléments sans tout lister.
**Prérequis :** fiche §4 · **Parcours :** C, E

Dans l'univers $E = \{1, 2, \dots, 25\}$, on pose $A$ l'ensemble des carrés parfaits de $E$ (les carrés d'entiers), $B$ celui des nombres premiers de $E$ (1 n'est pas premier) et $C = \{n \in E \mid n \ge 17\}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $A \cap B$ | un ensemble |
| b | $\lvert A \cup B \rvert$ | un nombre entier |
| c | $B \cap C$ | un ensemble |
| d | $\lvert \bar{B} \rvert$ (complémentaire dans $E$) | un nombre entier |
| e | $\lvert B \cup C \rvert$ | un nombre entier |
| f | $A \setminus C$ | un ensemble |
| g | $\lvert \overline{A \cup C} \rvert$ | un nombre entier |
| h | dans une association de 40 membres, 22 ont un vélo, 15 ont une voiture et 8 ont les deux : combien n'ont ni vélo ni voiture ? | un nombre entier |

### Ex R4.5 — Produit cartésien et couples ✏️ ★ ⏱️ 10 min
**Objectif :** dénombrer les couples d'un produit cartésien, et ne pas confondre couple et ensemble.
**Prérequis :** fiche §4 · **Parcours :** C

On pose $A = \{0, 1\}$ et $B = \{1, 2, 3\}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lvert A \times B \rvert$ | un nombre entier |
| b | $\lvert A \times A \times A \rvert$ (les triplets d'éléments de $A$) | un nombre entier |
| c | le nombre de couples $(x, y)$ de $B \times B$ tels que $x < y$ | un nombre entier |
| d | le nombre de couples $(a, b)$ de $A \times B$ tels que $a + b = 2$ | un nombre entier |
| e | $(1, 0) \in A \times B$ ? | vrai ou faux |
| f | un restaurant propose 3 entrées, 4 plats et 2 desserts : combien de menus (entrée, plat, dessert) différents ? | un nombre entier |
| g | $A \times B = B \times A$ ? | vrai ou faux |

### Ex R4.6 — Calculer des sommes Σ et des produits Π ✏️ ★ ⏱️ 15 min
**Objectif :** écrire une somme Σ ou un produit Π en extension, avec les bonnes bornes et le bon nombre de termes, puis la calculer.
**Prérequis :** fiche §5 · **Parcours :** C, E

Écris d'abord chaque somme ou produit **en extension** dans ta copie, puis calcule.

| | Calcul | Réponse attendue |
|---|---|---|
| a | $\sum_{k=1}^{6} (3k - 2)$ | un nombre entier |
| b | $\sum_{j=2}^{5} j^2$ | un nombre entier |
| c | $\sum_{i=0}^{4} (-1)^i$ | un nombre entier |
| d | $\sum_{k=1}^{4} \frac{1}{k}$ | une fraction |
| e | $\prod_{k=2}^{5} \frac{k}{k - 1}$ | un nombre entier |
| f | $\prod_{i=1}^{3} (i + 2)$ | un nombre entier |
| g | $\sum_{k=3}^{10} 2$ | un nombre entier |
| h | $\prod_{k=1}^{5} (-1)$ | un nombre entier |
| i | le nombre de termes de $\sum_{k=7}^{30} a_k$ | un nombre entier |

### Ex R4.7 — Développer, réindexer et découper une somme Σ ; calculer une somme double ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des sommes sans les écrire en entier, grâce à la linéarité, au découpage, au changement d'indice et aux sommes connues.
**Prérequis :** fiche §5 ; R4.6 · **Parcours :** C, E

On admet, pour tout entier $n \ge 1$ : $\displaystyle\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ et $\displaystyle\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\sum_{k=1}^{10} (2k + 3)$, avec la linéarité | un nombre entier |
| b | $\sum_{k=11}^{20} k$, avec le découpage | un nombre entier |
| c | $\sum_{j=0}^{9} (j + 1)^2$, avec un changement d'indice | un nombre entier |
| d | $\sum_{k=1}^{n} (2k + 3)$, en fonction de $n$ | une expression en `n` |
| e | on écrit $\sum_{k=3}^{8} a_{k-2} = \sum_{j=p}^{q} a_j$ : la liste `[p, q]` des nouvelles bornes | une liste de 2 nombres |
| f | $\sum_{i=1}^{2} \sum_{j=1}^{4} (i + 2j)$ | un nombre entier |
| g | $\sum_{i=1}^{4} \sum_{j=0}^{2} i \cdot 2^j$, en factorisant | un nombre entier |
| h | $\sum_{k=1}^{9} \left(\frac{1}{k} - \frac{1}{k+1}\right)$ | une fraction |

### Ex R4.8 — Trouver un contre-exemple ✏️ ★ ⏱️ 10 min
**Objectif :** réfuter une phrase « pour tout » par un contre-exemple, et décrire tous les contre-exemples quand c'est possible.
**Prérequis :** fiche §6 · **Parcours :** C, E

Chacune de ces affirmations est fausse.

| | Affirmation | Question | Réponse attendue |
|---|---|---|---|
| a | « Pour tout entier $n \ge 1$, $2^n > n^2$. » | le plus petit contre-exemple | un nombre entier |
| b | « Pour tout entier $n \ge 2$, $2^n - 1$ est premier. » | le plus petit contre-exemple | un nombre entier |
| c | « Pour tout réel $x$, $x^2 \ge x$. » | l'ensemble de **tous** les contre-exemples | un intervalle |
| d | « Pour tout entier $n \ge 1$, si $n$ est divisible par 4 et par 6, alors $n$ est divisible par 24. » | le plus petit contre-exemple | un nombre entier |
| e | « La somme de deux nombres premiers est toujours paire. » | la plus petite somme impaire de deux nombres premiers | un nombre entier |
| f | « Pour tout réel $x$, $(x + 1)^2 = x^2 + 1$. » | l'ensemble des réels pour lesquels l'égalité est **vraie** | un ensemble |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (fiche §8). La solution donne une **grille de relecture** pour juger la tienne. On rappelle qu'un entier $n$ est pair s'il existe un entier $k$ tel que $n = 2k$, impair s'il existe un entier $k$ tel que $n = 2k + 1$, et que tout entier est pair ou impair, jamais les deux.

### Ex R4.9 — Démonstration directe : la somme de deux nombres pairs est paire ∂ ★★ ⏱️ 20 min
**Objectif :** rédiger une démonstration directe complète, à partir d'une définition.
**Prérequis :** fiche §6 et §8 · **Parcours :** C, E

1. Écris l'énoncé « la somme de deux entiers pairs est paire » avec un quantificateur : « pour tous entiers… ».
2. Démontre-le, en introduisant les deux entiers et en utilisant la définition d'un entier pair. Pourquoi faut-il deux lettres différentes ($k$ et $\ell$) ?
3. Démontre de même que la somme d'un entier pair et d'un entier impair est impaire.
4. Démontre que le produit d'un entier pair par un entier quelconque est pair.
5. Un camarade écrit : « $2 + 4 = 6$ et $10 + 12 = 22$, donc la somme de deux pairs est paire. » Explique en une phrase pourquoi ce n'est pas une démonstration.

### Ex R4.10 — Par contraposée : si n² est pair, alors n est pair ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer une implication par sa contraposée, puis par une disjonction de cas.
**Prérequis :** fiche §2 et §6 ; R4.9 · **Parcours :** C, E

1. Écris la contraposée de « pour tout entier $n$, si $n^2$ est pair, alors $n$ est pair ».
2. Démontre cette contraposée, puis conclus.
3. La réciproque est-elle vraie ? Déduis-en une équivalence, que tu écriras avec ⇔.
4. Pourquoi une démonstration directe (partir de « $n^2 = 2k$ ») est-elle difficile ici ?
5. Démontre de même, par contraposée et par une disjonction de cas, que pour tout entier $n$, si $n^2$ est divisible par 3, alors $n$ est divisible par 3. Indice : un entier qui n'est pas divisible par 3 s'écrit $3k + 1$ ou $3k + 2$.

### Ex R4.11 — Par l'absurde : √2 n'est pas une fraction ∂ ★★★ ⏱️ 40 min
**Objectif :** mener une démonstration par l'absurde classique, en s'appuyant sur un résultat déjà démontré.
**Prérequis :** fiche §6 ; R4.10 ; R1 (fractions irréductibles) · **Parcours :** C

On veut démontrer qu'il n'existe pas d'entiers $p$ et $q$ ($q \ne 0$) tels que $\sqrt{2} = \frac{p}{q}$.
1. Supposons le contraire : $\sqrt{2} = \frac{p}{q}$ avec $p$ et $q$ entiers, $q \ne 0$. Explique pourquoi on peut supposer la fraction **irréductible** : $p$ et $q$ n'ont pas de diviseur commun autre que 1 et −1.
2. Montre que $p^2 = 2q^2$, puis que $p$ est pair (cite R4.10).
3. On écrit $p = 2r$. Montre que $q^2 = 2r^2$, puis que $q$ est pair.
4. Où est la contradiction ? Conclus en une phrase.
5. Adapte la démonstration pour montrer que $\sqrt{3}$ n'est pas une fraction (sers-toi de R4.10, question 5).
6. Que se passe-t-il si tu essaies la même démonstration avec $\sqrt{4}$ ? À quelle étape échoue-t-elle, et pourquoi est-ce heureux ?

### Ex R4.12 — Par récurrence : 1 + 2 + … + n = n(n + 1)/2 ∂ ★★ ⏱️ 35 min
**Objectif :** rédiger une démonstration par récurrence complète sur une somme.
**Prérequis :** fiche §5 et §7 · **Parcours :** C, E

Pour tout entier $n \ge 1$, on note $P(n)$ : « $\displaystyle\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ ».
1. Vérifie $P(1)$, $P(2)$ et $P(3)$ en calculant les deux membres. Cela suffit-il ?
2. Rédige l'initialisation.
3. Rédige l'hérédité : suppose $P(n)$ vraie pour un entier $n \ge 1$ fixé, isole le dernier terme de $\sum_{k=1}^{n+1} k$, et montre $P(n + 1)$.
4. Rédige la conclusion.
5. Déduis-en, sans nouvelle récurrence, une formule pour $\sum_{k=1}^{n} (4k + 1)$ (utilise la linéarité).

### Ex R4.13 — Par récurrence : 2ⁿ ≥ n + 1 ∂ ★★ ⏱️ 35 min
**Objectif :** démontrer une inégalité par récurrence, et choisir le bon point de départ.
**Prérequis :** fiche §7 ; R2 (inégalités) · **Parcours :** C

1. Démontre par récurrence que, pour tout entier $n \ge 0$, $2^n \ge n + 1$. Dans l'hérédité, tu auras besoin de montrer que $2(n + 1) \ge n + 2$ : justifie-le.
2. Pour quels entiers $n$ a-t-on l'égalité $2^n = n + 1$ ?
3. On veut démontrer que, pour tout entier $n \ge 4$, $2^n \ge n^2$. Calcule $2^n$ et $n^2$ pour $n = 0$ à $5$ : pourquoi l'initialisation ne peut-elle pas se faire en $n = 3$ ?
4. Montre que, pour tout entier $n \ge 3$, $2n^2 \ge (n + 1)^2$ (étudie le signe de $n^2 - 2n - 1$, ou écris-le $(n - 1)^2 - 2$).
5. Démontre par récurrence que $2^n \ge n^2$ pour tout $n \ge 4$.

<a id="reflexion"></a>

## 🔗 ⚖️ 🗣️ Pont, esprit critique et explication

### Ex R4.14 — Écrire la loss moyenne d'un modèle avec Σ 🔗 ★★ ⏱️ 15 min
**Objectif :** écrire une erreur moyenne avec Σ, la calculer, et se servir des règles de calcul de Σ pour prévoir l'effet d'un décalage des prédictions.
**Prérequis :** fiche §5 · **Parcours :** C, E

Un modèle prédit la durée de cinq trajets (en dizaines de minutes). Les vraies durées sont $y = (5, 3, 7, 6, 2)$, les prédictions $\hat{y} = (7, 2, 7, 3, 3)$. On note $e_i = \hat{y}_i - y_i$ l'erreur sur le trajet $i$, et $n$ le nombre de trajets.

1. Écris dans ta copie, avec Σ et pour $n$ trajets, l'**erreur quadratique moyenne** MSE (la moyenne des carrés des erreurs) et l'**erreur absolue moyenne** MAE (la moyenne des valeurs absolues des erreurs).
2. Calcule les réponses du tableau.

| | Question | Réponse attendue |
|---|---|---|
| a | $\sum_{i=1}^{5} e_i$ | un nombre entier |
| b | $\sum_{i=1}^{5} e_i^2$ | un nombre entier |
| c | la MSE | un nombre (ou une fraction) |
| d | la MAE | un nombre (ou une fraction) |
| e | $\sum_{i=1}^{5} e_i^2 = \left(\sum_{i=1}^{5} e_i\right)^2$ ? | vrai ou faux |
| f | on ajoute 1 à chaque prédiction : la nouvelle somme $\sum_{i=1}^{5} (e_i + 1)$, calculée avec la linéarité, sans recalculer les erreurs | un nombre entier |
| g | la nouvelle MSE, en développant $(e_i + 1)^2$ et en utilisant a et b | un nombre (ou une fraction) |

3. Dans ta copie, en deux phrases : pourquoi n'utilise-t-on pas la moyenne des erreurs $\frac{1}{n}\sum e_i$ comme mesure d'erreur ? Et pourquoi la MSE ne peut-elle être nulle que si toutes les erreurs le sont ?

### Ex R4.15 — Repérer un raisonnement fautif dans une phrase de presse ⚖️ ★ ⏱️ 15 min
**Objectif :** reconnaître les erreurs de logique les plus courantes dans un texte : réciproque prise pour l'implication, négation mal formée, exemples pris pour une démonstration.
**Prérequis :** fiche §2, §3 et §6 · **Parcours :** C

Pour chaque phrase, dis quelle règle de logique est enfreinte (réciproque, négation, quantificateur, exemples, faux « ou »…), puis réécris une phrase correcte.
1. « Si un traitement est efficace, les patients vont mieux. Nos patients vont mieux : le traitement est donc efficace. »
2. « Tous les gagnants du loto avaient acheté un billet. Achetez un billet, et vous gagnerez. »
3. « Le maire n'a pas promis d'augmenter les impôts : il s'est donc engagé à les baisser. »
4. « Il est faux que tous les adolescents lisent peu. Aucun adolescent ne lit donc peu. »
5. « Notre méthode a marché dans les trois écoles où nous l'avons testée : elle marche partout. »

### Ex R4.16 — Expliquer la différence entre « si » et « si et seulement si » 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement la différence entre une implication et une équivalence.
**Prérequis :** fiche §2 · **Parcours :** C, E

Un ami te dit : « En maths, "si" ou "si et seulement si", c'est la même chose, non ? »

Réponds-lui **en huit lignes au plus**. Ta réponse doit contenir : un exemple de la vie courante d'implication vraie dont la réciproque est fausse, un exemple d'équivalence, la phrase « P si et seulement si Q veut dire P ⇒ Q et Q ⇒ P » dite avec tes mots, et ce que cela change quand on résout une équation.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r4_logique_ensembles/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R4.17 | Tables de vérité et implication · `truth_table`, `implies` | 🔨 | ★ | 30 | C |
| R4.18 | Σ et Π en Python · `sum_over`, `prod_over` | 🔨 | ★ | 25 | C, E |
| R4.19 | Chercher un contre-exemple de 0 à N · `find_counterexample` | 🔨 | ★★ | 30 | C, E |
| R4.20 | Les ensembles de Python : `set`, `\|`, `&`, `-` | 📦 | ★ | 10 | C, E |
| R4.21 | Prédire : n² + n + 41 est-il toujours un nombre premier ? | 🔮 | ★ | 15 | C, E |
| R4.22 | Vérifier une formule de somme de 1 à 1 000, puis la démontrer | 🔬 | ★★ | 20 | C |
| R4.23 | Diagrammes de Venn | 🎨 | ★ | 15 | C |
| R4.24 | Chasse à l'erreur : une « démonstration » par récurrence qui prouve le faux | 🐛 | ★★ | 20 | C, E |
| R4.25 | Rédiger une démonstration propre en LaTeX | 🛠️ | ★ | 20 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
