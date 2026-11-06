# R4 · Logique, ensembles, Σ et Π — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 ⚖️ 🗣️ Pont, esprit critique et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R4.Q1 — Vrai, faux, ou pas une proposition ?

<details><summary>Indice 1</summary>

Relis « Vrai ou faux, sans entre-deux » et « Les trois connecteurs » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une proposition a une valeur de vérité ; un ordre ou une phrase qui dépend d'une variable non fixée n'en a pas. « ou » est inclusif ; « et » demande les deux.

</details>
<details><summary>Indice 3</summary>

1 : $91 = 7 \times 13$, donc **fausse**. Pour 4, une des deux parties est vraie : que vaut « ou » ? Pour 5, 10 est-il divisible par 4 ?

</details>

### R4.Q2 — Réciproque ou contraposée ?

<details><summary>Indice 1</summary>

Relis « Réciproque, contraposée, négation » (fiche §2) et son tableau.

</details>
<details><summary>Indice 2</summary>

Réciproque : on échange hypothèse et conclusion. Contraposée : on échange **et** on nie les deux. La négation d'une implication n'est pas une implication.

</details>
<details><summary>Indice 3</summary>

1 échange « il pleut » et « le sol est mouillé » sans les nier : c'est la **réciproque**. Pour 3, on nie les deux sans les échanger : est-ce l'une des deux ? Pour 6, quand la promesse est-elle trahie ?

</details>

### R4.Q3 — Nier une phrase avec « pour tout »

<details><summary>Indice 1</summary>

Relis « Nier une phrase quantifiée » (fiche §3).

</details>
<details><summary>Indice 2</summary>

« Pour tout » devient « il existe », « il existe » devient « pour tout », et on nie la propriété ; « et » devient « ou ». Le contraire de $>$ est $\le$.

</details>
<details><summary>Indice 3</summary>

1 : il suffit d'un élève qui n'a pas rendu son devoir : « **au moins un** élève n'a pas rendu son devoir ». Pour 3, la négation de « $n > 100$ et $n$ pair » est « $n \le 100$ ou $n$ impair ».

</details>

### R4.Q4 — Ensembles : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Écrire un ensemble » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\in$ relie un **élément** à un ensemble, $\subset$ un **ensemble** à un ensemble. Un ensemble n'a pas de répétition.

</details>
<details><summary>Indice 3</summary>

1 : 4 est un élément de $A$, **vrai**. Pour 2, $\{4\}$ est un ensemble : est-il un élément de $A$ ? Pour 7, 1 est-il dans $]0 \;;\; 1[$ ?

</details>

### R4.Q5 — Lire une somme Σ

<details><summary>Indice 1</summary>

Relis « Lire une somme » et « Calculer avec Σ » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Le nombre de termes de $\sum_{k=m}^{n}$ est $n - m + 1$ ; l'indice est muet ; une constante dans un produit sort à la puissance $n$.

</details>
<details><summary>Indice 3</summary>

1 : $10 - 4 + 1 = 7$ termes. Pour 2, remplace $j$ par 0, 1, 2 et 3. Pour 5, essaie avec deux termes : $a_1 b_1 + a_2 b_2$ contre $(a_1 + a_2)(b_1 + b_2)$.

</details>

### R4.Q6 — Quel raisonnement pour quelle affirmation ?

<details><summary>Indice 1</summary>

Relis le §6 en entier, puis le §7 pour la récurrence.

</details>
<details><summary>Indice 2</summary>

Un « pour tout » faux se réfute par un contre-exemple ; une non-existence se prête à l'absurde ; un « pour tout $n \ge n_0$ » qui passe de $n$ à $n + 1$ à la récurrence ; une valeur absolue ou un max à une disjonction de cas.

</details>
<details><summary>Indice 3</summary>

1 : c'est faux, donc un **contre-exemple** (essaie 3). Pour 5, reconnais une identité remarquable. Pour 6, que vaut $\max(x, -x)$ selon le signe de $x$ ?

</details>

### R4.Q7 — Les deux étapes d'une récurrence

<details><summary>Indice 1</summary>

Relis « Le principe des dominos » et « Les deux étapes sont indispensables » (fiche §7).

</details>
<details><summary>Indice 2</summary>

L'initialisation fait tomber le premier domino ; l'hérédité fait tomber chaque domino suivant. Des vérifications, même nombreuses, ne sont pas une hérédité.

</details>
<details><summary>Indice 3</summary>

1 : **initialisation** et **hérédité**. Pour 2, on suppose $P(n)$ pour un $n$ fixé, et on démontre … ? Pour 5, relis l'exemple « $4^n$ est divisible par 3 ».

</details>

### R4.Q8 — Ce qui manque dans une démonstration

<details><summary>Indice 1</summary>

Relis « Les fautes de rédaction les plus fréquentes » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Cherche : des exemples à la place d'un argument ; la réciproque démontrée à la place de l'implication ; une variable non introduite ou un cas oublié ; des implications dans le mauvais sens.

</details>
<details><summary>Indice 3</summary>

1 : trois exemples ne démontrent pas un « pour tout ». Pour 2, d'où part le texte, et d'où devait-il partir ? Pour 3, tout entier est-il de la forme $2k$ ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### R4.R1 — Résoudre une inéquation (R2)

<details><summary>Indice 1</summary>

Relis les règles des inégalités de R2 (fiche de R2, §5).

</details>
<details><summary>Indice 2</summary>

On isole $x$ ; en multipliant ou en divisant par un nombre négatif, le sens de l'inégalité change.

</details>
<details><summary>Indice 3</summary>

1 : $7 - 3x < 1 \iff -3x < -6 \iff x > 2$. Pour 2, développe, puis regroupe les $x$ d'un côté. Pour 3, la négation de « $x \ge 2$ » est « $x < 2$ ».

</details>

### R4.R2 — Composer deux fonctions (R3)

<details><summary>Indice 1</summary>

Relis « Enchaîner deux fonctions » (fiche de R3, §7).

</details>
<details><summary>Indice 2</summary>

$(f \circ g)(x) = f(g(x))$ : on applique $g$ d'abord. Pour réfuter un « pour tout », un contre-exemple suffit.

</details>
<details><summary>Indice 3</summary>

1 : $g(2) = 5$, puis $f(5) = -2$. Pour 2, remplace $x$ par $x^2 + 1$ dans $f$. Pour 3, la question 1 donne déjà deux valeurs différentes en $x = 2$.

</details>

### R4.R3 — Simplifier des fractions (R1)

<details><summary>Indice 1</summary>

Relis l'addition des fractions (fiche de R1, §3).

</details>
<details><summary>Indice 2</summary>

Même dénominateur, puis on additionne les numérateurs. Pour 2, réduis $\frac{1}{k} - \frac{1}{k + 1}$ au dénominateur $k(k + 1)$.

</details>
<details><summary>Indice 3</summary>

1 : $\frac{3}{6} + \frac{2}{6} + \frac{1}{6} = 1$. Pour 3, écris chaque terme comme une différence : $\frac{1}{1 \times 2} = 1 - \frac{1}{2}$, puis regarde ce qui se simplifie.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R4.1 — Tables de vérité de « et », « ou », « non » et de l'implication

<details><summary>Indice 1</summary>

Relis « Les trois connecteurs », « Nier « et » et « ou » » (fiche §1) et la table de $P \Rightarrow Q$ (fiche §2).

</details>
<details><summary>Indice 2</summary>

Écris quatre lignes VV, VF, FV, FF, une colonne par étape (non P, non Q, P et Q…), puis la colonne demandée. Une implication n'est fausse que sur la ligne « hypothèse vraie, conclusion fausse ».

</details>
<details><summary>Indice 3</summary>

a : « P et Q » vaut V, F, F, F, donc sa négation vaut F, V, V, V. Pour e, l'hypothèse est Q et la conclusion P : seule la ligne où Q est vraie et P fausse donne F. Pour i, ne garde que les lignes où R est fausse.

</details>

### Ex R4.2 — Réciproque, contraposée, négation : écrire les trois

<details><summary>Indice 1</summary>

Relis « Réciproque, contraposée, négation » (fiche §2) et « Nier une phrase quantifiée » (fiche §3).

</details>
<details><summary>Indice 2</summary>

La contraposée a toujours la valeur de l'implication, la négation la valeur contraire ; seule la réciproque est à étudier à part. La négation de « pour tout $n$, si P alors Q » est « il existe $n$ tel que P et non Q ».

</details>
<details><summary>Indice 3</summary>

A est vraie, donc sa contraposée aussi, et sa négation est fausse ; sa réciproque « divisible par 3 ⇒ divisible par 6 » est fausse (essaie 9). Pour B, essaie un nombre négatif. Pour D, résous $3x - 2 = 10$.

</details>

### Ex R4.3 — Nier des phrases à deux quantificateurs

<details><summary>Indice 1</summary>

Relis « Nier une phrase quantifiée » et « L'ordre des quantificateurs » (fiche §3).

</details>
<details><summary>Indice 2</summary>

De gauche à droite : chaque ∀ devient ∃, chaque ∃ devient ∀, l'ordre des variables ne change pas, et on nie la propriété finale. La condition qui accompagne un quantificateur (« $\varepsilon > 0$ ») ne se nie pas.

</details>
<details><summary>Indice 3</summary>

a : ∀x devient ∃x, ∃y devient ∀y, et $y > x$ devient $y \le x$ : c'est la phrase 2. Pour e, cherche un $x$ qui n'a pas de racine carrée réelle, puis un $y$ qui annule tous les produits $xy$.

</details>

### Ex R4.4 — Union, intersection, complémentaire et cardinal

<details><summary>Indice 1</summary>

Relis « Les opérations » et « Compter une union » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Écris d'abord $A$, $B$ et $C$ en extension. Pour un cardinal d'union, $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$ ; pour un complémentaire, $\lvert \bar{A} \rvert = \lvert E \rvert - \lvert A \rvert$.

</details>
<details><summary>Indice 3</summary>

$A = \{1, 4, 9, 16, 25\}$ et $B = \{2, 3, 5, 7, 11, 13, 17, 19, 23\}$ : a, un carré peut-il être premier ? Pour g, calcule d'abord $\lvert A \cup C \rvert$ (25 est dans les deux). Pour h, représente la classe par un diagramme de Venn.

</details>

### Ex R4.5 — Produit cartésien et couples

<details><summary>Indice 1</summary>

Relis « Le produit cartésien » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\lvert A \times B \rvert = \lvert A \rvert \times \lvert B \rvert$ ; un couple est ordonné, et sa première coordonnée est dans le premier ensemble. Pour compter, liste les couples dans un tableau.

</details>
<details><summary>Indice 3</summary>

a : $2 \times 3$. Pour c, liste les 9 couples de $B \times B$ et garde ceux où $x < y$, strictement. Pour g, $(0, 2)$ est-il dans $B \times A$ ?

</details>

### Ex R4.6 — Calculer des sommes Σ et des produits Π

<details><summary>Indice 1</summary>

Relis « Lire une somme » et « Le produit Π » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Écris chaque somme en extension : remplace l'indice par chaque valeur, de la borne du bas à celle du haut, **les deux incluses**.

</details>
<details><summary>Indice 3</summary>

a : $1 + 4 + 7 + 10 + 13 + 16$. Pour e, écris les facteurs $\frac{2}{1} \times \frac{3}{2} \times \dots$ et regarde ce qui se simplifie. Pour g, combien de termes de 3 à 10 ?

</details>

### Ex R4.7 — Développer, réindexer et découper une somme Σ ; calculer une somme double

<details><summary>Indice 1</summary>

Relis « Calculer avec Σ », « Deux sommes à connaître » et « Les sommes doubles » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Linéarité : $\sum (2k + 3) = 2\sum k + \sum 3$, et $\sum_{k=1}^{10} 3 = 30$. Découpage : de 11 à 20, c'est de 1 à 20 moins de 1 à 10. Changement d'indice : les bornes bougent avec l'indice.

</details>
<details><summary>Indice 3</summary>

a : $2 \times 55 + 30$. Pour c, pose $k = j + 1$ : quand $j$ va de 0 à 9, $k$ va de … à … . Pour f, calcule la somme intérieure sur $j$ à $i$ fixé, puis ajoute pour $i = 1$ et $i = 2$. Pour h, c'est une somme télescopique.

</details>

### Ex R4.8 — Trouver un contre-exemple

<details><summary>Indice 1</summary>

Relis « Le contre-exemple » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Essaie les valeurs dans l'ordre, une par une, et écris les deux membres. Pour c et f, résous l'inéquation ou l'équation au lieu d'essayer.

</details>
<details><summary>Indice 3</summary>

a : $n = 1$ donne $2 > 1$, vrai ; essaie $n = 2$ (attention, l'inégalité est stricte). Pour c, $x^2 < x \iff x(x - 1) < 0$. Pour f, développe $(x + 1)^2$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R4.9 — Démonstration directe : la somme de deux nombres pairs est paire

<details><summary>Indice 1</summary>

Relis « Raisonnement direct » (fiche §6) et « Ce qu'une démonstration doit contenir » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Introduis deux entiers pairs $a$ et $b$, traduis « pair » par la définition avec deux lettres différentes, calcule $a + b$, et reconnais la forme $2 \times (\text{un entier})$.

</details>
<details><summary>Indice 3</summary>

« Soient $a$ et $b$ deux entiers pairs. Il existe des entiers $k$ et $\ell$ tels que $a = 2k$ et $b = 2\ell$. Alors $a + b = 2k + 2\ell = \dots$ » Termine, puis fais de même pour 3 et 4.

</details>

### Ex R4.10 — Par contraposée : si n² est pair, alors n est pair

<details><summary>Indice 1</summary>

Relis « Raisonnement par contraposée » et « Raisonnement direct » (fiche §6).

</details>
<details><summary>Indice 2</summary>

La contraposée est : « si $n$ est impair, alors $n^2$ est impair ». La démonstration directe du §6 sur le produit de deux impairs fait presque tout le travail.

</details>
<details><summary>Indice 3</summary>

« Soit $n$ un entier impair : $n = 2k + 1$. Alors $n^2 = 4k^2 + 4k + 1 = 2(\dots) + 1$. » Pour 5, traite les deux cas $n = 3k + 1$ et $n = 3k + 2$ : calcule $n^2$ et écris-le $3(\dots) + 1$.

</details>

### Ex R4.11 — Par l'absurde : √2 n'est pas une fraction

<details><summary>Indice 1</summary>

Relis « Raisonnement par l'absurde » (fiche §6) et ta démonstration de R4.10.

</details>
<details><summary>Indice 2</summary>

Suppose $\sqrt{2} = \frac{p}{q}$, fraction irréductible ; élève au carré pour obtenir $p^2 = 2q^2$ ; R4.10 dit alors que $p$ est pair ; recommence avec $q$.

</details>
<details><summary>Indice 3</summary>

De $p = 2r$ et $p^2 = 2q^2$, on tire $4r^2 = 2q^2$, donc $q^2 = 2r^2$ : $q^2$ est pair, donc $q$ aussi. Or $p$ et $q$ pairs ont 2 comme diviseur commun. Pour $\sqrt{4}$, regarde quelle étape repose sur R4.10.

</details>

### Ex R4.12 — Par récurrence : 1 + 2 + … + n = n(n + 1)/2

<details><summary>Indice 1</summary>

Relis « Un exemple de somme » (fiche §7) : la structure est la même.

</details>
<details><summary>Indice 2</summary>

Hérédité : $\sum_{k=1}^{n+1} k = \sum_{k=1}^{n} k + (n + 1)$, puis remplace la somme jusqu'à $n$ grâce à l'hypothèse de récurrence, et factorise par $(n + 1)$.

</details>
<details><summary>Indice 3</summary>

$\frac{n(n+1)}{2} + (n + 1) = (n + 1)\left(\frac{n}{2} + 1\right) = \dots$ ; vérifie que tu obtiens $\frac{(n + 1)(n + 2)}{2}$, c'est-à-dire $P(n + 1)$. Pour 5, $\sum (4k + 1) = 4\sum k + \sum 1$.

</details>

### Ex R4.13 — Par récurrence : 2ⁿ ≥ n + 1

<details><summary>Indice 1</summary>

Relis « Un exemple de divisibilité » et « Les deux étapes sont indispensables » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Hérédité : $2^{n+1} = 2 \times 2^n \ge 2(n + 1)$ grâce à l'hypothèse, puis compare $2(n + 1)$ à $n + 2$. Pour la seconde récurrence, même schéma avec $2n^2 \ge (n + 1)^2$.

</details>
<details><summary>Indice 3</summary>

$2(n + 1) - (n + 2) = n \ge 0$. Pour 4, $2n^2 - (n + 1)^2 = n^2 - 2n - 1 = (n - 1)^2 - 2$, positif dès que $(n - 1)^2 \ge 2$. Pour 3, compare $2^3$ et $3^2$.

</details>

<a id="reflexion"></a>

## 🔗 ⚖️ 🗣️ Pont, esprit critique et explication

### Ex R4.14 — Écrire la loss moyenne d'un modèle avec Σ

<details><summary>Indice 1</summary>

Relis « Lire une somme » et l'encadré « Dans workbookIA » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Calcule d'abord les cinq erreurs $e_i = \hat{y}_i - y_i$, avec leur signe ; puis leurs carrés et leurs valeurs absolues ; enfin les moyennes (divise par 5).

</details>
<details><summary>Indice 3</summary>

$e = (1, 0, -1, -2, 0)$. La MSE est $\frac{1 + 0 + 1 + 4 + 0}{5}$. Pour d et e, seule la cinquième erreur change : elle vaut maintenant $16 - 6$. Pour f, divise chaque nouvelle valeur par l'ancienne.

</details>

### Ex R4.15 — Repérer un raisonnement fautif dans une phrase de presse

<details><summary>Indice 1</summary>

Relis « Réciproque, contraposée, négation » (fiche §2), « Nier une phrase quantifiée » (fiche §3) et « Le contre-exemple » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour chaque phrase, écris la règle sous la forme « si P, alors Q » ou « pour tout… », puis regarde ce que le texte en déduit : la réciproque ? une négation mal formée ? un « pour tout » tiré d'exemples ?

</details>
<details><summary>Indice 3</summary>

1 : la règle est « efficace ⇒ les patients vont mieux » ; le texte conclut « les patients vont mieux ⇒ efficace », la **réciproque**. Pour 3, le contraire d'« augmenter » n'est pas « baisser ».

</details>

### Ex R4.16 — Expliquer la différence entre « si » et « si et seulement si »

<details><summary>Indice 1</summary>

Relis « Équivalence, condition nécessaire, condition suffisante » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Cherche une implication de la vie courante dont la réciproque est fausse (un animal, une ville, un diplôme…), puis une phrase qui marche dans les deux sens.

</details>
<details><summary>Indice 3</summary>

Par exemple : « si c'est un chat, alors c'est un mammifère » est vraie, mais un mammifère n'est pas toujours un chat. Pour l'équation, pense à $x^2 = 9$ et $x = 3$.

</details>

<a id="notebook"></a>

## Notebook

### Ex R4.17 — Tables de vérité et implication · `truth_table`, `implies`

<details><summary>Indice 1</summary>

Relis la cellule `itertools.product` de la fiche §1 et la table de $P \Rightarrow Q$ (fiche §2).

</details>
<details><summary>Indice 2</summary>

`truth_table` : la `ValueError` d'abord, puis une boucle `for values in itertools.product([True, False], repeat=n):` qui ajoute à une liste le couple `(values, formula(*values))`. `implies` : une ligne.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
if n < 1:
    raise ValueError("...")
rows = []
for values in itertools.product(...):
    rows.append((values, ...))
return rows
```
Pour `implies`, la table de $P \Rightarrow Q$ est celle de « (non P) ou Q ».

</details>

### Ex R4.19 — Chercher un contre-exemple de 0 à N · `find_counterexample`

<details><summary>Indice 1</summary>

Relis « Le contre-exemple » et la cellule Python de la fin du §6.

</details>
<details><summary>Indice 2</summary>

Une boucle `for n in range(...)` qui s'arrête au premier `n` pour lequel `predicate(n)` est faux, et `return n` ; après la boucle, `return None`. Les deux bornes 0 et `n_max` sont essayées.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
for n in range(n_max + 1):
    if not predicate(n):
        return ...
return None
```

</details>

### Ex R4.21 — Prédire : n² + n + 41 est-il toujours un nombre premier ?

<details><summary>Indice 1</summary>

Relis l'encadré « Des exemples ne démontrent pas un « pour tout » » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour prédire, calcule encore deux ou trois valeurs à la main, puis demande-toi si quelques succès suffisent à affirmer « pour tout $n$ ».

</details>
<details><summary>Indice 3</summary>

Pour c, compte les nombres premiers affichés (ou utilise `sum(is_prime(...) for n in range(40))`). Pour la copie, écris $41^2 + 41 + 41$ en mettant 41 en facteur.

</details>

### Ex R4.20 — Les ensembles de Python : `set`, `|`, `&`, `-`

<details><summary>Indice 1</summary>

Relis la cellule Python du §4 et workbookIA 0A §100.3.4.

</details>
<details><summary>Indice 2</summary>

`set("mot")` donne les lettres sans répétition ; `len` les compte ; `A & B`, `A | B`, `A - B`, `B <= A` font le reste, chacun en une ligne.

</details>
<details><summary>Indice 3</summary>

a : `len(set("anticonstitutionnellement"))`. Pour b, `A & B` est déjà un ensemble : donne-le tel quel. Pour f, compare deux `set(...)` avec `==`.

</details>

### Ex R4.23 — Diagrammes de Venn

<details><summary>Indice 1</summary>

Relis « Les opérations » et les lois de De Morgan (fiche §4).

</details>
<details><summary>Indice 2</summary>

Sur des tableaux NumPy, `not`, `and` et `or` ne marchent pas point par point : utilise `~`, `&` et `|`, avec des parenthèses autour de chaque morceau.

</details>
<details><summary>Indice 3</summary>

Le premier tableau est `~in_a & ~in_b` ; le deuxième nie l'union : `~(in_a | in_b)`. Écris les deux autres de la même façon, puis `return [premier, deuxième, troisième, quatrième]`.

</details>

### Ex R4.18 — Σ et Π en Python · `sum_over`, `prod_over`

<details><summary>Indice 1</summary>

Relis « Lire une somme » et « Le produit Π » (fiche §5), et la cellule Python de la fin du §5.

</details>
<details><summary>Indice 2</summary>

Un total, une boucle `for k in range(start, stop + 1):` qui le met à jour avec `f(k)`, puis `return`. Une somme part de 0, un produit de 1 : ce sont aussi les valeurs d'une somme et d'un produit vides.

</details>
<details><summary>Indice 3</summary>

Squelette de `sum_over` :
```python
total = 0
for k in range(start, stop + 1):
    total = total + ...
return total
```
`prod_over` a la même forme, avec un autre départ et une multiplication.

</details>

### Ex R4.22 — Vérifier une formule de somme de 1 à 1 000, puis la démontrer

<details><summary>Indice 1</summary>

Relis « Deux sommes à connaître » (fiche §5) et « Un exemple de somme » (fiche §7).

</details>
<details><summary>Indice 2</summary>

`sum_of_cubes` : `sum(k**3 for k in range(1, n + 1))`. Les deux formules se recopient avec `//`, en mettant des parenthèses autour de chaque produit.

</details>
<details><summary>Indice 3</summary>

`formula_a(n)` : `(n * (n + 1) // 2) ** 2`. Pour la démonstration, l'hérédité donne $\frac{n^2(n+1)^2}{4} + (n + 1)^3 = \frac{(n + 1)^2}{4}\left(n^2 + 4(n + 1)\right)$ : reconnais un carré dans la parenthèse.

</details>

### Ex R4.24 — Chasse à l'erreur : une « démonstration » par récurrence qui prouve le faux

<details><summary>Indice 1</summary>

Relis « Les deux étapes sont indispensables » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Preuve 1 : cherche l'étape absente, puis calcule $5^n + 1$ pour $n = 0, 1, 2$ et regarde le reste dans la division par 4. Preuve 2 : déroule l'hérédité pour $n = 1$, avec deux boules.

</details>
<details><summary>Indice 3</summary>

Pour $n = 1$, les « boules 1 à $n$ » sont la seule boule 1, et les « boules 2 à $n + 1$ » la seule boule 2. Quelle ligne affirme que ces deux groupes ont une boule commune ?

</details>

### Ex R4.25 — Rédiger une démonstration propre en LaTeX

<details><summary>Indice 1</summary>

Relis « Écrire une démonstration en LaTeX » (fiche §8) et ta démonstration de R4.12.

</details>
<details><summary>Indice 2</summary>

Un paragraphe par étape, chacun titré en italique (`*Initialisation.*`) ; le calcul de l'hérédité entre `$$` sur sa propre ligne.

</details>
<details><summary>Indice 3</summary>

Commence par : `*Démonstration.* Pour tout entier $n \ge 1$, notons $P(n)$ la propriété « $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ ».` Puis l'initialisation en $n = 1$.

</details>
