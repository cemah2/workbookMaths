# M03 · Probabilités conditionnelles — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M03.Q1 — Jointe, marginale ou conditionnelle ?

<details><summary>Indice 1</summary>

Relis les trois sortes de probabilités du §1, puis le début du §2.

</details>
<details><summary>Indice 2</summary>

« et » : une jointe. « parmi ceux qui » ou « des destinataires qui » : une conditionnelle, sachant ce qui suit le « qui ». Une proportion de tout le monde : une marginale.

</details>
<details><summary>Indice 3</summary>

5 : si tout clic suit une ouverture, l'événement « clic » est inclus dans « ouvert ». Puis teste la règle du produit avec les phrases 2 et 3. 6 : dans le tableau de la fiche, additionne $P(\text{premium} \mid \text{mobile})$ et $P(\text{premium} \mid \text{ordinateur})$.

</details>

### M03.Q2 — P(A sachant B) et P(B sachant A)

<details><summary>Indice 1</summary>

Relis « L'ordre compte » et la règle du produit (fiche §2).

</details>
<details><summary>Indice 2</summary>

Écris les données avec la notation : $P(\text{technique}) = 0{,}4$, $P(\text{formation}) = 0{,}25$, $P(\text{technique} \mid \text{formation}) = 0{,}8$.

</details>
<details><summary>Indice 3</summary>

1 : la règle du produit avec la conditionnelle donnée. 2 : divise l'intersection par $P(\text{technique})$. 5 : essaie avec $A$ certain.

</details>

### M03.Q3 — Indépendants ou incompatibles ?

<details><summary>Indice 1</summary>

Relis « L'indépendance » (fiche §2) et son ⚠️.

</details>
<details><summary>Indice 2</summary>

Indépendants : $P(A \cap B) = P(A)\,P(B)$. Incompatibles : $P(A \cap B) = 0$.

</details>
<details><summary>Indice 3</summary>

1 : $A \cap B = \{2\}$. 5 : écris $P(E \cap \text{non } F) = P(E) - P(E \cap F)$. 6 : l'exemple des deux pièces.

</details>

### M03.Q4 — Quelle métrique pour quelle probabilité ?

<details><summary>Indice 1</summary>

Relis le tableau des mesures du §4.

</details>
<details><summary>Indice 2</summary>

Ce qui suit la barre « sachant » dit si l'on divise par une ligne (la vérité) ou par une colonne (la prédiction).

</details>
<details><summary>Indice 3</summary>

6 : les mesures qui conditionnent par la vérité ne dépendent pas de la proportion de positifs (fiche §6).

</details>

### M03.Q5 — Moyennes de métriques

<details><summary>Indice 1</summary>

Relis le §5 en entier.

</details>
<details><summary>Indice 2</summary>

$F_\beta$ donne au recall le poids $\frac{\beta^2}{1 + \beta^2}$. La balanced accuracy est la moyenne des recalls.

</details>
<details><summary>Indice 3</summary>

4 : la fin de « Plusieurs classes » (et M03.13). 5 : le paragraphe sur le MCC, et sa convention.

</details>

### M03.Q6 — ROC et AUC : vrai ou faux

<details><summary>Indice 1</summary>

Relis « L'aire sous la courbe : une proportion de paires » et ses trois conséquences (fiche §7).

</details>
<details><summary>Indice 2</summary>

L'AUC ne dépend que de l'ordre des scores dans chaque paire (positif, négatif).

</details>
<details><summary>Indice 3</summary>

1 : une AUC n'utilise aucun seuil. 4 : que devient l'AUC de $1 - s$ ? 6 : la precision dépend des valeurs des scores et de la prévalence.

</details>

### M03.Q7 — Calibré ou pas ?

<details><summary>Indice 1</summary>

Relis « Calibration et score de Brier » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Calibré : $P(Y = 1 \mid \text{score} = p) = p$, à chaque niveau $p$. Le score de Brier est la moyenne des $(p_i - y_i)^2$.

</details>
<details><summary>Indice 3</summary>

2 : une prévision constante classe tous les exemples ex æquo. 6 : relis la fin de « Classes déséquilibrées » (fiche §6).

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M03.R1 — Arbres pondérés (R8)

<details><summary>Indice 1</summary>

Relis les trois règles des arbres pondérés de R8.

</details>
<details><summary>Indice 2</summary>

Un chemin : le produit de ses branches. Un événement : la somme des chemins qui y mènent.

</details>
<details><summary>Indice 3</summary>

4 : $\frac{3}{5} \times \frac{1}{2} + \frac{2}{5} \times \frac{1}{6}$, au même dénominateur 30.

</details>

### M03.R2 — Moyenne harmonique et moyenne pondérée (R1)

<details><summary>Indice 1</summary>

Relis les moyennes de R1.

</details>
<details><summary>Indice 2</summary>

Moyenne harmonique de $a$ et $b$ : $\frac{2}{\frac{1}{a} + \frac{1}{b}} = \frac{2ab}{a + b}$.

</details>
<details><summary>Indice 3</summary>

5 : les poids normalisés sont $\frac{1}{5}$ et $\frac{4}{5}$ ; calcule $\frac{1}{5} \times \frac{1}{0{,}5} + \frac{4}{5} \times \frac{1}{1}$, puis son inverse.

</details>

### M03.R3 — Aire par la méthode des trapèzes (M02a)

<details><summary>Indice 1</summary>

Relis la méthode des trapèzes de M02a §5.

</details>
<details><summary>Indice 2</summary>

Aire d'un trapèze : largeur × moyenne des deux hauteurs.

</details>
<details><summary>Indice 3</summary>

3 : les points $(0, 0)$, $(0{,}5 ;\ 0{,}25)$ et $(1, 1)$. 4 : seuls les deux paliers horizontaux comptent.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M03.1 — Un tableau de contingence : jointes, marginales, conditionnelles

<details><summary>Indice 1</summary>

Relis les §1 et §2, avec l'exemple des 500 utilisateurs.

</details>
<details><summary>Indice 2</summary>

Commence par ajouter au tableau la ligne et la colonne des totaux. Puis, pour chaque question, écris la probabilité avec « sachant » et entoure le total par lequel tu divises.

</details>
<details><summary>Indice 3</summary>

d : le total de la colonne « avec photo », 120. e : le total de la ligne « 4 ou 5 étoiles », 220. h : $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

</details>

### Ex M03.2 — L'indépendance, vérifiée dans un tableau

<details><summary>Indice 1</summary>

Relis « L'indépendance » et le tableau des effectifs attendus (fiche §2).

</details>
<details><summary>Indice 2</summary>

Compare la probabilité de clic dans chaque version à la probabilité de clic globale. Pour le tableau 2, compare une case au produit de ses deux marges.

</details>
<details><summary>Indice 3</summary>

h : $\frac{\text{total de la ligne} \times \text{total de la colonne}}{\text{total}}$, avec la ligne « soir » (300) et la colonne « achat » (90).

</details>

### Ex M03.3 — Probabilités totales avec trois cas

<details><summary>Indice 1</summary>

Relis l'exemple des sources de visites (fiche §3).

</details>
<details><summary>Indice 2</summary>

Dessine l'arbre : un premier niveau pour le serveur, un second pour « erreur » ou non. $P(E)$ est la somme des trois chemins qui mènent à « erreur ».

</details>
<details><summary>Indice 3</summary>

e : divise le chemin de b) par $P(E)$ de a). g : les nouvelles parts du trafic sont 45 %, 45 % et 10 %.

</details>

### Ex M03.4 — Une matrice de confusion lue comme des probabilités

<details><summary>Indice 1</summary>

Relis le §4 et son tableau des mesures.

</details>
<details><summary>Indice 2</summary>

Remplis d'abord la matrice : TP = 64 ; les faux négatifs sont les défauts non signalés ; les faux positifs, les pièces signalées sans défaut ; le reste est TN.

</details>
<details><summary>Indice 3</summary>

TN $= 2\,000 - 64 - 16 - 96$. f : le total de la colonne « non signalée ». h : $\frac{2\,TP}{2\,TP + FP + FN}$.

</details>

### Ex M03.5 — F-beta : quel β pour quel coût d'erreur ?

<details><summary>Indice 1</summary>

Relis « F-beta : une moyenne harmonique pondérée » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$F_\beta = \frac{(1 + \beta^2)PR}{\beta^2 P + R}$. Attention : c'est $\beta^2$ qui apparaît, et devant $P$ au dénominateur.

</details>
<details><summary>Indice 3</summary>

d : au dénominateur avec les comptages, $\beta^2$ multiplie FN. f : quand $\beta$ est très grand, divise le numérateur et le dénominateur par $\beta^2$.

</details>

### Ex M03.6 — Balanced accuracy et MCC sur un problème déséquilibré

<details><summary>Indice 1</summary>

Relis « Balanced accuracy et MCC » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Écris les deux matrices de confusion. Pour B : 120 clients signalés, dont 35 vrais positifs, donc 85 faux positifs ; 50 positifs en tout, donc 15 faux négatifs.

</details>
<details><summary>Indice 3</summary>

g : $\frac{TP \cdot TN - FP \cdot FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}$, avec les totaux 120, 50, 950 et 880.

</details>

### Ex M03.7 — Changer de population : recalculer la precision quand la prévalence change

<details><summary>Indice 1</summary>

Relis « La precision dépend de la prévalence » (fiche §6).

</details>
<details><summary>Indice 2</summary>

precision $= \frac{r\pi}{r\pi + (1 - s)(1 - \pi)}$. Ou bien : un tableau de 10 000 comptes, avec $10\,000\pi$ comptes piratés.

</details>
<details><summary>Indice 3</summary>

c, d : 200 comptes piratés et 9 800 sains. g : écris l'équation precision $= 0{,}8$ et isole $\pi$. h : precision 0,8 avec 180 vrais positifs donne le nombre de faux positifs.

</details>

### Ex M03.8 — Une courbe ROC à la main, et son aire par les trapèzes

<details><summary>Indice 1</summary>

Relis « La courbe ROC » et l'exemple des huit disques (fiche §7).

</details>
<details><summary>Indice 2</summary>

Trie les dix scores dans l'ordre décroissant. Un positif : un pas vers le haut de $\frac{1}{5}$ ; un négatif : un pas vers la droite de $\frac{1}{5}$.

</details>
<details><summary>Indice 3</summary>

b : au seuil 0,6, compte les positifs et les négatifs de score au moins 0,6. d : seuls les paliers horizontaux ont une aire. g : le nouveau négatif dépasse les 5 positifs.

</details>

### Ex M03.9 — L'AUC comme proportion de paires bien classées

<details><summary>Indice 1</summary>

Relis l'encadré « L'AUC comme probabilité » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Fais le tableau 4 × 3 des paires : 1 si le positif a le plus grand score, ½ en cas d'égalité, 0 sinon.

</details>
<details><summary>Indice 3</summary>

e : inverser les scores échange les 1 et les 0, et laisse les ½. f : la nouvelle ligne du positif 0,6, puis divise par 15.

</details>

### Ex M03.10 — Courbe precision-recall et average precision à la main

<details><summary>Indice 1</summary>

Relis « La courbe precision-recall et l'average precision » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Fais un tableau avec une colonne par seuil : TP, FP, precision $\frac{TP}{TP + FP}$, recall $\frac{TP}{3}$, F1.

</details>
<details><summary>Indice 3</summary>

d : seuls les seuils où le recall augmente comptent, chacun avec un gain de $\frac{1}{3}$ multiplié par la precision à ce seuil. h : refais l'ordre des 7 films, puis la même somme.

</details>

### Ex M03.11 — Score de Brier et calibration de huit prévisions

<details><summary>Indice 1</summary>

Relis « Calibration et score de Brier » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Écris la colonne des $(p_i - y_i)^2$, puis fais-en la moyenne. Pour la calibration, sépare les colis en deux paquets selon la probabilité annoncée.

</details>
<details><summary>Indice 3</summary>

c : la proportion de colis en retard est $\frac{3}{8}$, et une prévision constante $\pi$ a pour score $\pi(1 - \pi)$. h : le colis le plus mal prévu.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M03.12 — L'aire sous la courbe ROC compte les paires bien classées

<details><summary>Indice 1</summary>

Relis l'escalier et la grille des paires de la figure du §7.

</details>
<details><summary>Indice 2</summary>

Découpe l'aire en rectangles verticaux, un par pas horizontal, donc un par négatif. Quelle est la hauteur de la courbe pendant ce pas ?

</details>
<details><summary>Indice 3</summary>

3 : au moment où le seuil passe $t_j$, les positifs déjà déclarés positifs sont ceux de score $s_i > t_j$. 5 : une diagonale coupe un rectangle en deux triangles de même aire.

</details>

### Ex M03.13 — En multiclasse, micro-precision, micro-recall et accuracy sont égaux

<details><summary>Indice 1</summary>

Relis « Plusieurs classes : macro, micro, pondérée » (fiche §5) et l'exemple des feuilles de vigne.

</details>
<details><summary>Indice 2</summary>

Chaque case hors de la diagonale $C_{kl}$ ($k \ne l$) est une erreur : pour quelle classe est-elle un faux positif ? Pour quelle classe un faux négatif ?

</details>
<details><summary>Indice 3</summary>

2 : en sommant les colonnes hors diagonale sur toutes les classes, chaque case hors diagonale est comptée exactement une fois. 3 : $\sum_k (TP_k + FP_k) = n$.

</details>

<a id="reflexion"></a>

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M03.14 — Un seuil sur un score : trois seuils, trois matrices de confusion

<details><summary>Indice 1</summary>

Relis « Le seuil de décision » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour chaque seuil, compte les positifs et les négatifs de score au moins égal au seuil : ce sont TP et FP ; le reste donne FN et TN.

</details>
<details><summary>Indice 3</summary>

g : $3 \times FN + 1 \times FP$ au seuil 0,5. h : calcule ce coût pour les trois seuils.

</details>

### Ex M03.15 — Équité : les taux de faux positifs de deux groupes

<details><summary>Indice 1</summary>

Relis « Taux par groupe : un premier regard sur l'équité » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Taux de faux positifs : $\frac{FP}{FP + TN}$ ; precision : $\frac{TP}{TP + FP}$ ; part signalée : $\frac{TP + FP}{n}$.

</details>
<details><summary>Indice 3</summary>

h : l'identité de la fiche avec la prévalence de B ($\frac{20}{200}$), le recall 0,8 et la precision visée $\frac{48}{76}$.

</details>

### Ex M03.16 — MML §6.3 : règle de la somme, règle du produit et vocabulaire, en anglais

<details><summary>Indice 1</summary>

Lis la section avec la fiche ouverte au §1 et au §2 : la règle de la somme est la marginalisation, la règle du produit celle du §2.

</details>
<details><summary>Indice 2</summary>

Cherche les mots *sum rule*, *marginalization*, *product rule*, *factorized*, et la phrase sur les difficultés de calcul.

</details>
<details><summary>Indice 3</summary>

2 : la somme porte sur toutes les valeurs des 29 autres variables binaires. 6 : enchaîne la règle du produit deux fois.

</details>

### Ex M03.17 — Un taux de réussite trompeur : le paradoxe de Simpson

<details><summary>Indice 1</summary>

Relis « Le paradoxe de Simpson » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Calcule les six taux, puis écris chaque taux global comme une moyenne pondérée des deux taux du même groupe.

</details>
<details><summary>Indice 3</summary>

3 et 4 : quelle question chaque comparaison permet-elle de trancher ? La variable « département » est-elle une cause commune, ou une étape du mécanisme ?

</details>

### Ex M03.18 — Expliquer pourquoi P(A sachant B) n'est pas P(B sachant A)

<details><summary>Indice 1</summary>

Relis « L'ordre compte » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Écris les deux probabilités avec « sachant » : laquelle est donnée, laquelle est conclue ?

</details>
<details><summary>Indice 3</summary>

Invente un tableau 2 × 2 de 1 000 utilisateurs où peu se désabonnent mais beaucoup ouvrent rarement l'application ; calcule les deux conditionnelles.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M03.E1 — Une variable indépendante de la cible peut-elle aider un modèle ?

<details><summary>Indice 1</summary>

Relis « Indépendance deux à deux ou mutuelle » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Dans l'exemple des deux pièces, « même côté » est indépendant de chaque pièce, mais connu dès qu'on connaît les deux.

</details>
<details><summary>Indice 3</summary>

Prends $Y = X_1$ XOR $X_2$ pour deux bits équilibrés indépendants ; calcule $P(Y = 1 \mid X_1 = 0)$ et $P(Y = 1 \mid X_1 = 1)$, puis $P(Y = 1 \mid X_1, X_2)$.

</details>

<a id="notebook"></a>

## Notebook

### Ex M03.19 — Jointe, marginales et conditionnelles à partir d'un tableau de comptages · `joint_from_counts, marginal, conditional`

<details><summary>Indice 1</summary>

Relis les §1 et §2, puis la docstring de chaque fonction en entier, en particulier ses **Raises**.

</details>
<details><summary>Indice 2</summary>

Écris d'abord `_check_joint(joint)` : `np.asarray(joint, dtype=float)`, puis une `ValueError` par règle (deux dimensions, cases positives, somme 1 à $10^{-9}$ près). `marginal` est alors une ligne : `table.sum(axis=axis)`.

</details>
<details><summary>Indice 3</summary>

`conditional` : `if (given_row is None) == (given_column is None): raise ValueError(...)` ; puis `line = table[given_row]` (ou `table[:, given_column]`) après avoir vérifié l'indice, et `line / line.sum()` si `line.sum() > 0`.

</details>

### Ex M03.20 — Tester l'indépendance avec une tolérance · `are_independent`

<details><summary>Indice 1</summary>

Relis la définition de l'indépendance de deux variables (fiche §2).

</details>
<details><summary>Indice 2</summary>

Les marginales : `table.sum(axis=1)` (loi de X) et `table.sum(axis=0)` (loi de Y). `np.outer(a, b)` donne le tableau des produits `a[i] * b[j]`.

</details>
<details><summary>Indice 3</summary>

`bool(np.all(np.abs(table - np.outer(rows, cols)) <= tol))`.

</details>

### Ex M03.21 — L'AUC en comptant les paires · `auc_by_pairs`

<details><summary>Indice 1</summary>

Relis l'encadré « L'AUC comme probabilité » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Convertis en arrays, vérifie qu'aucun n'est vide, puis compte les paires où le positif gagne et les ex æquo.

</details>
<details><summary>Indice 3</summary>

`diff = pos[:, None] - neg[None, :]` ; `wins = np.sum(diff > 0)` ; `ties = np.sum(diff == 0)` ; `float((wins + 0.5 * ties) / diff.size)`.

</details>

### Ex M03.22 — `sklearn.metrics.roc_auc_score` contre le comptage des paires, ex æquo compris

<details><summary>Indice 1</summary>

Lis `help(roc_auc_score)` et `help(roc_curve)` : l'ordre des arguments, et ce que renvoie `roc_curve`.

</details>
<details><summary>Indice 2</summary>

c : `(S_22 >= 0.5).astype(int)` donne des prédictions 0/1 ; passe-les à `roc_auc_score` à la place des scores. e : `len(thresholds)`.

</details>
<details><summary>Indice 3</summary>

Pour comprendre c = d : trace à la main la courbe ROC de prédictions 0/1 (trois points) et calcule son aire.

</details>

### Ex M03.23 — Prédire : l'AUC après une transformation croissante des scores

<details><summary>Indice 1</summary>

Relis les trois conséquences de l'AUC comme proportion de paires (fiche §7).

</details>
<details><summary>Indice 2</summary>

Pour chaque transformation, demande-toi si elle garde l'ordre de deux scores quelconques.

</details>
<details><summary>Indice 3</summary>

e : le score de Brier compare la **valeur** de chaque score à 0 ou à 1.

</details>

### Ex M03.24 — Simuler pour estimer une probabilité conditionnelle

<details><summary>Indice 1</summary>

Relis la définition de la probabilité conditionnelle (fiche §2) : on restreint l'univers aux tirages où la condition est vraie.

</details>
<details><summary>Indice 2</summary>

`event[given]` garde les valeurs de `event` aux tirages où `given` est vrai ; `np.mean` d'un tableau de booléens est une proportion. Les événements : `total = DICE_24.sum(axis=1)`, `(DICE_24 == 6).any(axis=1)`.

</details>
<details><summary>Indice 3</summary>

`if not np.any(given): raise ValueError(...)` avant le calcul, puis `float(np.mean(np.asarray(event)[np.asarray(given)]))`.

</details>

### Ex M03.25 — La courbe ROC en escalier : une case par paire

<details><summary>Indice 1</summary>

Relis « La courbe ROC » (fiche §7) et refais à la main la courbe de M03.9.

</details>
<details><summary>Indice 2</summary>

Les seuils sont les scores distincts, du plus grand au plus petit : `np.unique(...)[::-1]`. Pour chacun, FPR $=$ la proportion de négatifs de score $\ge$ seuil, recall $=$ celle des positifs.

</details>
<details><summary>Indice 3</summary>

`fpr, tpr = zip(*roc_points(...))`, puis `ax.plot(fpr, tpr)`, `ax.plot([0, 1], [0, 1], "--")`, `ax.set_xlabel(...)`, `ax.set_ylabel(...)` et `ax.set_title(f"AUC = {...:.4f}")`.

</details>

### Ex M03.26 — Chasse à l'erreur : conditionnelle inversée, marginale oubliée

<details><summary>Indice 1</summary>

Relis les ⚠️ des §2 et §3, et le tableau des pièges classiques.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, écris ce que le calcul donne vraiment avec la notation $P(\ldots \mid \ldots)$, et compare au commentaire.

</details>
<details><summary>Indice 3</summary>

Une conditionnelle se calcule par $\frac{P(\text{intersection})}{P(\text{condition})}$ ; un taux global par les probabilités totales. Une des lignes donne plus de 1.

</details>

### Ex M03.27 — Une fonction qui refuse un tableau invalide (`ValueError`)

<details><summary>Indice 1</summary>

Relis la docstring du module, en tête de `mymath/conditional.py` : elle dit ce qu'est une loi jointe valide.

</details>
<details><summary>Indice 2</summary>

Une vérification par règle, chacune avec `raise ValueError("...")` et son propre message. Essaie `float("nan") < 0` et `abs(float("nan") - 1) > 1e-9` dans une cellule.

</details>
<details><summary>Indice 3</summary>

Dans l'ordre : `array.ndim != 2 or array.size == 0`, `not np.all(np.isfinite(array))`, `np.any(array < 0)`, `abs(array.sum() - 1) > tol`.

</details>

### Ex M03.28 — Défi : retrouver un tableau de contingence à partir de quelques probabilités

<details><summary>Indice 1</summary>

Traduis chaque information en effectifs : 600 visites, donc $P(\text{appli}) = 0{,}4$ donne 240 visites sur l'appli.

</details>
<details><summary>Indice 2</summary>

L'information 4 porte sur la ligne « appli », l'information 6 sur la ligne « site », l'information 5 sur la colonne « abandon ». Trouve d'abord les cases qu'une seule information suffit à fixer.

</details>
<details><summary>Indice 3</summary>

appli-achat $= 0{,}625 \times 240$ ; site-rien $= \frac{360}{6}$ ; puis les marges donnent site-achat et site-abandon, et l'information 5 donne appli-abandon par une équation à une inconnue.

</details>
