# M06 · Théorie de l'information — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m06_information/06_mes_reponses.md` (créée par `python tools/start_chapter.py M06`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Pont, estimation et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées : $\log_2 x = \frac{\ln x}{\ln 2}$. Garde les valeurs exactes (les fractions, $\log_2 3$) jusqu'au bout, et n'arrondis qu'à la fin. Sauf mention contraire, les informations et les entropies sont en **bits**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M06.Q1 — La surprise et la probabilité 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Combien de bits apporte un événement de probabilité $\frac{1}{256}$ ?
2. Un événement apporte 11 bits d'information. Quelle est sa probabilité ?
3. Deux événements indépendants apportent 1,5 bit et 2 bits. Combien apportent-ils ensemble ?
4. Vrai ou faux : l'information d'un événement peut être négative.
5. Un événement apporte 2 bits. Combien de nats (2 décimales) ?
6. Pourquoi l'information est-elle définie avec un logarithme, plutôt qu'avec $\frac{1}{p}$ par exemple ?

### M06.Q2 — L'entropie : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. L'entropie d'une loi peut être négative.
2. Une loi sur 8 issues a une entropie d'au plus 3 bits.
3. Ajouter à une loi une issue de probabilité 0 change son entropie.
4. Si l'on multiplie toutes les valeurs de $X$ par 2, l'entropie de $X$ double.
5. L'entropie de $(0{,}97 ;\ 0{,}03)$ est plus grande que celle de $(0{,}53 ;\ 0{,}47)$.
6. L'entropie de $X$ est l'espérance de $-\log_2 p(X)$.

### M06.Q3 — Conjointe et conditionnelle 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Écris la règle de la chaîne pour $H(X, Y)$, de deux façons.
2. Si $Y$ est une fonction de $X$, que vaut $H(Y \mid X)$ ?
3. Si $X$ et $Y$ sont indépendantes, que vaut $H(X, Y)$ ?
4. Vrai ou faux : $H(Y \mid X) = H(X \mid Y)$ pour tout couple.
5. Vrai ou faux : $H(X, Y) \ge H(X)$.
6. $H(X) = 1$, $H(Y) = 2$ et $H(X, Y) = 2{,}5$ : que valent $H(Y \mid X)$ et $H(X \mid Y)$ ?

### M06.Q4 — L'information mutuelle 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C*

1. Écris $I(X ; Y)$ de trois façons avec des entropies.
2. Vrai ou faux : $I(X ; Y) = I(Y ; X)$.
3. $I(X ; Y) = 0$ : que peux-tu dire de $X$ et $Y$ ?
4. $H(X) = 2$ et $H(X \mid Y) = 0{,}5$ : que vaut $I(X ; Y)$ ?
5. Vrai ou faux : $I(X ; Y)$ peut dépasser $H(X)$.
6. Vrai ou faux : si la corrélation de $X$ et $Y$ est nulle, leur information mutuelle l'est aussi.

### M06.Q5 — La KL n'est pas une distance 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Écris $\mathrm{KL}(p \,\|\, q)$ comme une différence d'une cross-entropy et d'une entropie.
2. Que vaut $\mathrm{KL}(p \,\|\, q)$ quand $q = p$ ?
3. $p = (\frac{1}{2}, \frac{1}{2}, 0)$ et $q = (\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$ : $\mathrm{KL}(p \,\|\, q)$ est-elle finie ? Et $\mathrm{KL}(q \,\|\, p)$ ?
4. Cite deux propriétés d'une distance que la divergence KL ne vérifie pas en général.
5. Vrai ou faux : $\mathrm{KL}(p \,\|\, q)$ peut être négative.
6. Dans $\mathrm{KL}(\text{données} \,\|\, \text{modèle})$, que mesure la KL, en bits par symbole ?

### M06.Q6 — L'inégalité de Jensen 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

1. Énonce l'inégalité de Jensen pour une fonction convexe $f$.
2. $X$ vaut 0 ou 4 avec la probabilité $\frac{1}{2}$ chacun, et $f(x) = x^2$ : que valent $\mathbb{E}[f(X)]$ et $f(\mathbb{E}[X])$ ?
3. Pour $f = \ln$, dans quel sens est l'inégalité ? Pourquoi ?
4. Quand y a-t-il égalité, pour une fonction strictement convexe ?
5. Vrai ou faux : pour une variable $X$ à valeurs strictement positives, $\mathbb{E}\big[\frac{1}{X}\big] \ge \frac{1}{\mathbb{E}[X]}$.
6. Que vaut l'écart de Jensen $\mathbb{E}[X^2] - (\mathbb{E}[X])^2$, sous un autre nom ?

### M06.Q7 — Codes préfixes 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Qu'est-ce qu'un code préfixe ? Pourquoi se lit-il sans séparateur ?
2. Le code $\{01, 10, 11, 001\}$ est-il préfixe ? Est-il complet ?
3. Le code $\{0, 1, 10\}$ est-il préfixe ?
4. Des longueurs $(1, 3, 3, 3)$ sont-elles possibles pour un code préfixe binaire ?
5. Combien de chiffres binaires faut-il à un code de longueur fixe pour 50 issues ?
6. Vrai ou faux : un code de longueur fixe dont les mots sont tous différents est toujours préfixe.

<a id="rappels"></a>

## 🔁 Rappels

### M06.R1 — Logarithmes en base 2 (R6) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. Calcule sans calculatrice $\log_2 512$, $\log_2 \frac{1}{4096}$ et $\log_2 \sqrt{2}$.
2. Calcule $\log_2 10$ (3 décimales) avec la touche $\ln$.
3. Simplifie $\log_2 24 - \log_2 3$.
4. Résous $2^x = 12$ (2 décimales).
5. Quel est le signe de $\log_2 p$ pour $0 < p < 1$ ? Que vaut $-p \log_2 p$ pour $p = \frac{1}{2}$ ?

### M06.R2 — Probabilités jointes et conditionnelles (M03) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

Sur 100 trajets, on a noté s'il pleuvait ($X$) et si le train était en retard ($Y$).

| | en retard | à l'heure |
|---|---|---|
| pluie | 12 | 18 |
| pas de pluie | 28 | 42 |

1. Écris la loi jointe de $(X, Y)$.
2. Calcule les lois marginales de $X$ et de $Y$.
3. Calcule $P(Y = \text{en retard} \mid X = \text{pluie})$ et $P(Y = \text{en retard} \mid X = \text{pas de pluie})$.
4. $X$ et $Y$ sont-elles indépendantes ? Justifie de deux façons.
5. Que vaudrait alors $H(Y \mid X)$, comparée à $H(Y)$ ?

### M06.R3 — Convexité (M05a) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C*

1. Donne la définition d'une fonction convexe avec ses cordes.
2. $f(x) = -\ln x$ est-elle convexe sur $]0, +\infty[$ ? Justifie avec sa dérivée seconde.
3. Même question pour $g(x) = x \ln x$.
4. La somme de deux fonctions convexes est-elle convexe ?
5. Pour une fonction concave, la corde est-elle au-dessus ou au-dessous de la courbe ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/9"` ;
- une liste entre crochets, comme `[-1.5, 2.5]` ; vrai ou faux par `True` ou `False` ; une lettre ou un nom entre guillemets, comme `"B"`.

### Ex M06.1 — L'information d'événements et l'entropie d'une loi à quatre issues ✏️ ★ ⏱️ 20 min
**Objectif :** calculer l'information d'événements en bits et en nats, l'additionner pour des événements indépendants, et calculer l'entropie d'une loi.
**Prérequis :** fiche §1 et §2 ; R6 · **Parcours :** C, E

Un serveur web répond à chaque requête par l'un de quatre codes : succès avec la probabilité $\frac{1}{2}$, redirection avec $\frac{1}{4}$, erreur du client avec $\frac{3}{16}$, erreur du serveur avec $\frac{1}{16}$.

| | Question | Réponse attendue |
|---|---|---|
| a | l'information apportée par « erreur du serveur » | un entier |
| b | l'information apportée par « succès » | un entier |
| c | l'information apportée par « erreur du client » | un nombre (3 décimales) |
| d | l'information apportée par « erreur du serveur », en **nats** | un nombre (3 décimales) |
| e | l'information apportée par deux requêtes indépendantes : un succès, puis une erreur du serveur | un entier |
| f | l'entropie de la loi des quatre codes | un nombre (3 décimales) |
| g | cette entropie, en nats | un nombre (3 décimales) |
| h | l'entropie de la loi à trois issues obtenue en regroupant les deux erreurs en une seule issue « erreur » | un nombre (1 décimale) |

Dans ta copie : pourquoi f) est-elle plus petite que 2 bits ? Pourquoi h) est-elle plus petite que f) : qu'a-t-on perdu en regroupant les deux erreurs ? Écris l'écart f) − h) comme $\frac{1}{4}$ fois l'entropie d'une loi à deux issues, que tu préciseras.

### Ex M06.2 — L'entropie maximale : comparer trois lois à trois issues ✏️ ★★ ⏱️ 15 min
**Objectif :** comparer les entropies de plusieurs lois sur le même nombre d'issues, et voir quand l'entropie augmente.
**Prérequis :** fiche §2 · **Parcours :** C

Trois lois sur trois issues : $A = (\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$, $B = (\frac{1}{2}, \frac{1}{2}, 0)$ et $C = (0{,}7 ;\ 0{,}2 ;\ 0{,}1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $H(A)$ | un nombre (3 décimales) |
| b | $H(B)$ | un entier |
| c | $H(C)$ | un nombre (3 décimales) |
| d | la loi qui a la plus grande entropie | une lettre |
| e | l'entropie de $(0{,}45 ;\ 0{,}35 ;\ 0{,}2)$ | un nombre (3 décimales) |
| f | l'entropie de $(0{,}6 ;\ 0{,}25 ;\ 0{,}15)$, obtenue à partir de $C$ en retirant 0,1 à la première issue pour en donner 0,05 à chacune des deux autres | un nombre (3 décimales) |
| g | la plus grande entropie possible pour une loi sur trois issues, en **nats** | un nombre (3 décimales) |

Dans ta copie : range les lois $A$, $B$, $C$, celle de e) et celle de f) par entropie croissante. Que fait l'entropie quand on rapproche les probabilités les unes des autres ? Quelle est la plus petite entropie possible sur trois issues, et pour quelles lois ?

### Ex M06.3 — Entropies conjointe et conditionnelle d'un tableau 2 × 3 ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une entropie conjointe, des entropies conditionnelles à une valeur et en moyenne, et voir que connaître une valeur particulière peut augmenter l'incertitude.
**Prérequis :** fiche §3 ; M03 · **Parcours :** C, E

Une application a des utilisateurs gratuits et payants ($X$), dont on mesure l'usage ($Y$ : faible, moyen ou fort). La loi jointe :

| | faible | moyen | fort |
|---|---|---|---|
| gratuit | $\frac{1}{2}$ | 0 | 0 |
| payant | $\frac{1}{8}$ | $\frac{1}{8}$ | $\frac{1}{4}$ |

| | Question | Réponse attendue |
|---|---|---|
| a | $H(X, Y)$ | un nombre (2 décimales) |
| b | $H(Y \mid X = \text{payant})$ | un nombre (1 décimale) |
| c | $H(Y \mid X)$ | un nombre (2 décimales) |
| d | $H(Y)$ | un nombre (3 décimales) |
| e | $H(X \mid Y)$ | un nombre (3 décimales) |
| f | savoir qu'un utilisateur est payant augmente-t-il l'incertitude sur son usage, par rapport à ne rien savoir ? | `True` ou `False` |

Dans ta copie : vérifie la règle de la chaîne de deux façons. Pourquoi $H(Y \mid X = \text{gratuit})$ est-elle nulle ? Comment f) se concilie-t-il avec le fait que, en moyenne, savoir ne rend pas moins sûr ?

### Ex M06.4 — La règle de la chaîne de l'entropie, vérifiée ✏️ ★ ⏱️ 15 min
**Objectif :** calculer les deux entropies conditionnelles d'un tableau 2 × 2 et vérifier la règle de la chaîne dans les deux sens.
**Prérequis :** fiche §3 · **Parcours :** C

Une campagne envoie un message par e-mail ou par SMS ($X$, une fois sur deux chacun), et l'on note s'il est ouvert ($Y$). La loi jointe :

| | ouvert | pas ouvert |
|---|---|---|
| e-mail | 0,35 | 0,15 |
| SMS | 0,2 | 0,3 |

| | Question | Réponse attendue |
|---|---|---|
| a | $H(X)$ | un entier |
| b | $H(Y \mid X = \text{e-mail})$ | un nombre (3 décimales) |
| c | $H(Y \mid X = \text{SMS})$ | un nombre (3 décimales) |
| d | $H(Y \mid X)$ | un nombre (3 décimales) |
| e | $H(X, Y)$, calculée par sa définition (la somme sur les quatre cases) | un nombre (3 décimales) |
| f | $H(Y)$ | un nombre (3 décimales) |
| g | $H(X \mid Y)$ | un nombre (3 décimales) |

Dans ta copie : vérifie que $H(X) + H(Y \mid X)$ et $H(Y) + H(X \mid Y)$ redonnent e). Lequel des deux canaux rend l'ouverture la plus prévisible ?

### Ex M06.5 — L'information mutuelle de deux variables ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une information mutuelle à partir d'un tableau 3 × 2, par une baisse d'entropie, et en déduire l'autre entropie conditionnelle.
**Prérequis :** fiche §3 et §4 · **Parcours :** C, E

À un carrefour, on note la couleur du feu quand une voiture arrive ($X$) et si elle freine ($Y$). La loi jointe :

| | freine | ne freine pas |
|---|---|---|
| vert | $\frac{1}{16}$ | $\frac{7}{16}$ |
| orange | $\frac{1}{8}$ | $\frac{1}{8}$ |
| rouge | $\frac{1}{4}$ | 0 |

| | Question | Réponse attendue |
|---|---|---|
| a | $P(Y = \text{freine})$ | une fraction irréductible |
| b | $H(Y)$ | un nombre (3 décimales) |
| c | $H(Y \mid X = \text{vert})$ | un nombre (3 décimales) |
| d | $H(Y \mid X)$ | un nombre (3 décimales) |
| e | $I(X ; Y)$ | un nombre (3 décimales) |
| f | $H(X)$ | un nombre (1 décimale) |
| g | $H(X \mid Y)$ | un nombre (3 décimales) |
| h | $X$ et $Y$ sont-elles indépendantes ? | `True` ou `False` |

Dans ta copie : calcule aussi $I(X ; Y)$ par $H(X) + H(Y) - H(X, Y)$. Quelle case du tableau contribue le plus à la somme $\sum p(x, y) \log_2 \frac{p(x, y)}{p(x)\,p(y)}$, et quelles cases y contribuent négativement ?

### Ex M06.6 — Cross-entropy et KL en bits perdus : un code fait pour la mauvaise loi ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une cross-entropy et une divergence KL, et les lire comme des bits par symbole et des bits perdus.
**Prérequis :** fiche §5 · **Parcours :** C, E

Une application enregistre cinq types d'événements. Son compresseur a été réglé sur l'ancienne version, où ils suivaient la loi $q = (\frac{1}{2}, \frac{1}{8}, \frac{1}{8}, \frac{1}{8}, \frac{1}{8})$ : chaque type $i$ y reçoit un mot de $-\log_2 q_i$ bits. Aujourd'hui, les événements suivent la loi $p = (\frac{1}{4}, \frac{1}{4}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8})$.

| | Question | Réponse attendue |
|---|---|---|
| a | $H(p)$ | un nombre (2 décimales) |
| b | la longueur du mot du premier type, avec ce compresseur | un entier |
| c | $H(p, q)$, la longueur moyenne d'un mot avec ce compresseur, sur les données d'aujourd'hui | un nombre (1 décimale) |
| d | $\mathrm{KL}(p \,\|\, q)$ | un nombre (2 décimales) |
| e | le nombre de bits perdus, par rapport au meilleur code, sur 1 000 événements d'aujourd'hui | un entier |
| f | $\mathrm{KL}(p \,\|\, q)$, en **nats** | un nombre (4 décimales) |
| g | le terme du premier type dans la somme $\sum_i p_i \log_2 \frac{p_i}{q_i}$ | un nombre (2 décimales) |
| h | si l'ancienne loi avait donné la probabilité 0 au cinquième type, $H(p, q)$ serait-elle infinie ? | `True` ou `False` |

Dans ta copie : quels types coûtent plus cher qu'avec le meilleur code, et lesquels moins ? Quel est le signe de chaque terme de la somme de d), et pourquoi le total ne peut-il pas être négatif ?

### Ex M06.7 — L'inégalité de Jensen sur trois exemples ✏️ ★ ⏱️ 15 min
**Objectif :** calculer $\mathbb{E}[f(X)]$ et $f(\mathbb{E}[X])$ pour des fonctions convexes et concaves, et lire le signe de l'écart de Jensen.
**Prérequis :** fiche §6 ; M02b · **Parcours :** C

Trois variables discrètes :
- $X_1$ vaut 1, 3 ou 5 avec les probabilités $\frac{1}{4}$, $\frac{1}{2}$, $\frac{1}{4}$, et $f(x) = x^2$ ;
- $X_2$ vaut 0 ou 1 avec la probabilité $\frac{1}{2}$ chacun, et $f(x) = e^x$ ;
- $X_3$ vaut 1 ou 4 avec la probabilité $\frac{1}{2}$ chacun, et $f(x) = \log_2 x$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{E}[X_1]$ | un entier |
| b | $\mathbb{E}[X_1^2]$ | un entier |
| c | l'écart de Jensen $\mathbb{E}[f(X_1)] - f(\mathbb{E}[X_1])$ | un entier |
| d | l'écart de Jensen pour $X_2$ et $e^x$ | un nombre (4 décimales) |
| e | $\mathbb{E}[\log_2 X_3]$ | un nombre (1 décimale) |
| f | $\log_2 \mathbb{E}[X_3]$ | un nombre (4 décimales) |
| g | l'écart de Jensen pour $X_3$ et $\log_2$ | un nombre (4 décimales) |
| h | l'écart de c) est-il égal à la variance de $X_1$ ? | `True` ou `False` |

Dans ta copie : pour chaque exemple, dis si $f$ est convexe ou concave, et vérifie que le signe de l'écart est celui qu'annonce Jensen.

### Ex M06.8 — Kraft : ces longueurs de code sont-elles possibles ? ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des sommes de Kraft, décider si des longueurs sont possibles pour un code préfixe, et distinguer cette question de celle d'un code donné.
**Prérequis :** fiche §7 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la somme de Kraft $\sum_i 2^{-\ell_i}$ des longueurs $(1, 2, 3, 4)$ | une fraction irréductible |
| b | celle des longueurs $(2, 2, 2, 2, 3)$ | une fraction irréductible |
| c | celle des longueurs $(1, 2, 2, 3, 4)$ | une fraction irréductible |
| d | celle des longueurs $(1, 3, 3, 3, 4, 4)$ | un entier |
| e | la somme de Kraft $\sum_i 3^{-\ell_i}$ des longueurs $(1, 1, 2, 2, 2)$, pour un alphabet de trois symboles | un entier |
| f | un code préfixe binaire a déjà deux mots, de longueurs 1 et 2 : combien de mots de longueur 3 peut-on lui ajouter, au plus ? | un entier |
| g | le code $\{1, 10, 01\}$ est-il préfixe ? | `True` ou `False` |
| h | la somme de Kraft des longueurs du code de g) | un entier |

Dans ta copie : pour a) à e), dis si un code préfixe de ces longueurs existe ; pour ceux qui existent, écris-en un. Pourquoi h) ne contredit-il pas g) ?

### Ex M06.9 — La longueur moyenne d'un code, comparée à l'entropie ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la longueur moyenne d'un code, la comparer à l'entropie, et construire les longueurs de Shannon.
**Prérequis :** fiche §7 · **Parcours :** C

Une source émet cinq symboles avec les probabilités $p = (0{,}45 ;\ 0{,}25 ;\ 0{,}15 ;\ 0{,}10 ;\ 0{,}05)$, codés par le code préfixe $\{0, 10, 110, 1110, 1111\}$, dans cet ordre.

| | Question | Réponse attendue |
|---|---|---|
| a | $H(p)$ | un nombre (3 décimales) |
| b | la longueur moyenne $\bar{L}$ de ce code | un nombre (1 décimale) |
| c | la somme de Kraft de ce code | un entier |
| d | les longueurs de Shannon $\lceil -\log_2 p_i \rceil$, dans l'ordre des symboles | une liste de 5 entiers |
| e | leur somme de Kraft | une fraction irréductible |
| f | la longueur moyenne d'un code qui a les longueurs de Shannon | un nombre (1 décimale) |
| g | a-t-on $H(p) \le$ f) $< H(p) + 1$ ? | `True` ou `False` |
| h | l'écart $\bar{L} - H(p)$ du code donné | un nombre (3 décimales) |

Dans ta copie : écris un code préfixe qui a les longueurs de Shannon. Lequel des deux codes est le meilleur, et pourquoi le code de Shannon laisse-t-il de la place inutilisée (regarde e)) ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex M06.10 — I(X ; Y) = H(X) − H(X | Y), et l'information mutuelle est positive ∂ ★★ ⏱️ 20 min
**Objectif :** relier les trois écritures de l'information mutuelle, et en déduire qu'en moyenne, savoir ne rend pas moins sûr.
**Prérequis :** fiche §3 à §6 · **Parcours :** C

On part de la définition $I(X ; Y) = \sum_{x, y} p(x, y) \log_2 \frac{p(x, y)}{p(x)\,p(y)}$, la somme portant sur les cases où $p(x, y) > 0$.
1. En écrivant $p(x, y) = p(y)\,p(x \mid y)$, montre que $I(X ; Y) = H(X) - H(X \mid Y)$.
2. Montre de même que $I(X ; Y) = H(Y) - H(Y \mid X)$, puis que $I(X ; Y) = H(X) + H(Y) - H(X, Y)$.
3. Montre que $I(X ; Y) = \mathrm{KL}\big(p_{XY} \,\|\, p_X\,p_Y\big)$, où $p_X\,p_Y$ est la loi $(x, y) \mapsto p(x)\,p(y)$. On admet l'inégalité de Gibbs (fiche §6, démontrée en M06.11) : en déduire que $I(X ; Y) \ge 0$, avec égalité si et seulement si $X$ et $Y$ sont indépendantes.
4. En déduire que $H(X \mid Y) \le H(X)$, et que $H(X, Y) \le H(X) + H(Y)$. Quand y a-t-il égalité ?
5. Montre que $I(X ; X) = H(X)$.
6. Donne un exemple de tableau 2 × 2 où, pour une valeur $y$, $H(X \mid Y = y) > H(X)$. Pourquoi ne contredit-il pas la question 4 ?

### Ex M06.11 — La KL est positive : la preuve par l'inégalité de Jensen ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer l'inégalité de Gibbs avec l'inégalité de Jensen, étudier son cas d'égalité, et en tirer des conséquences.
**Prérequis :** fiche §5 et §6 ; M05a §1 · **Parcours :** C

Soit $p$ et $q$ deux lois sur les mêmes issues, $S$ l'ensemble des issues où $p(x) > 0$, et l'on suppose $q(x) > 0$ sur $S$. On admet l'inégalité de Jensen (fiche §6), avec son cas d'égalité pour une fonction strictement concave.
1. Montre que $\log_2$ est strictement concave sur $]0, +\infty[$.
2. On considère la variable $Z$ qui vaut $\frac{q(x)}{p(x)}$ avec la probabilité $p(x)$, pour $x \in S$. Écris $\mathbb{E}[\log_2 Z]$ et $\log_2 \mathbb{E}[Z]$ avec des sommes sur $S$.
3. Avec l'inégalité de Jensen, montre que $-\mathrm{KL}(p \,\|\, q) \le \log_2 \sum_{x \in S} q(x) \le 0$.
4. Montre que $\mathrm{KL}(p \,\|\, q) = 0$ si et seulement si $p = q$ : étudie les deux inégalités de la question 3, et à quelle condition chacune est une égalité.
5. En déduire que la divergence de Jensen-Shannon est positive ou nulle, et nulle seulement si $p = q$.
6. Que devient la question 3 si l'on ne suppose plus $q(x) > 0$ sur $S$ ? Que vaut alors $\mathrm{KL}(p \,\|\, q)$ ?

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Pont, estimation et explication

### Ex M06.12 — La log loss d'un classifieur, une cross-entropy moyenne 🔗 ★ ⏱️ 15 min
**Objectif :** calculer la log loss d'un classifieur à trois classes comme une moyenne de cross-entropies, en nats et en bits, et la comparer à celle d'un modèle qui ne sait rien.
**Prérequis :** fiche §5 et §8 · **Parcours :** C, E

Un classifieur range des images en trois classes (A, B, C). Sur quatre images, il a prédit :

| image | vraie classe | probabilités prédites (A, B, C) |
|---|---|---|
| 1 | A | (0,5 ; 0,3 ; 0,2) |
| 2 | B | (0,1 ; 0,8 ; 0,1) |
| 3 | C | (0,6 ; 0,15 ; 0,25) |
| 4 | A | (0,9 ; 0,05 ; 0,05) |

| | Question | Réponse attendue |
|---|---|---|
| a | la cross-entropy de l'image 3, en nats | un nombre (4 décimales) |
| b | la log loss sur les quatre images, en nats | un nombre (4 décimales) |
| c | cette log loss, en bits | un nombre (4 décimales) |
| d | la log loss, en nats, d'un modèle qui prédirait toujours $(\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$ | un nombre (4 décimales) |
| e | le classifieur fait-il mieux que ce modèle ? | `True` ou `False` |
| f | l'exponentielle de b) | un nombre (4 décimales) |

Dans ta copie : quelle image coûte le plus cher, et pourquoi ? Comment se lit f), à la manière d'une perplexité (fiche §8) ? Que vaudrait la cross-entropy de l'image 3 si le modèle avait donné la probabilité 0 à la classe C ?

### Ex M06.13 — Choisir une feature par l'information mutuelle 🔗 ★★ ⏱️ 20 min
**Objectif :** calculer l'information mutuelle de plusieurs features avec une cible à partir de comptages, les classer, et voir la limite de ce classement.
**Prérequis :** fiche §4 et §8 · **Parcours :** C

Sur 20 clients d'une boutique, on note s'ils achètent ($Y$) et trois features : $F_1$ (a déjà acheté avant), $F_2$ (est venu par une publicité) et $F_3$ (tranche d'âge). Les comptages :

| | achète | n'achète pas |
|---|---|---|
| $F_1$ = oui | 7 | 3 |
| $F_1$ = non | 3 | 7 |

| | achète | n'achète pas |
|---|---|---|
| $F_2$ = oui | 6 | 4 |
| $F_2$ = non | 4 | 6 |

| | achète | n'achète pas |
|---|---|---|
| $F_3$ = jeune | 4 | 0 |
| $F_3$ = moyen | 2 | 4 |
| $F_3$ = senior | 4 | 6 |

| | Question | Réponse attendue |
|---|---|---|
| a | $I(F_1 ; Y)$ | un nombre (4 décimales) |
| b | $I(F_2 ; Y)$ | un nombre (4 décimales) |
| c | $I(F_3 ; Y)$ | un nombre (4 décimales) |
| d | la feature la plus informative sur l'achat | un nom, comme `"F2"` |
| e | $H(Y \mid F_3)$ | un nombre (4 décimales) |
| f | $I(F_1 ; Y)$, en **nats** (l'unité de scikit-learn) | un nombre (4 décimales) |
| g | une feature qui serait le numéro de chaque client (20 valeurs différentes) aurait-elle, sur ces données, une information mutuelle avec $Y$ égale à $H(Y)$ ? | `True` ou `False` |

Dans ta copie : pourquoi la feature de g) serait-elle pourtant inutile pour prédire l'achat d'un nouveau client ? Pourquoi $F_3$ part-elle avec un avantage sur $F_1$ et $F_2$ ?

### Ex M06.14 — Fermi : combien de bits pour un génome humain ? 🧮 ★ ⏱️ 10 min
**Objectif :** estimer la taille d'un génome selon la façon de le coder, du code de longueur fixe à la description des différences.
**Prérequis :** fiche §2 et §7 · **Parcours :** C

Le génome humain s'écrit avec quatre lettres (A, C, G, T) et compte environ $3 \times 10^9$ paires de bases par jeu de chromosomes. Donne des ordres de grandeur, en justifiant chaque étape.
1. Avec un code de longueur fixe, combien de bits par base ? Combien de bits, puis de méga-octets, pour un jeu de chromosomes ?
2. Les lettres ne sont pas tout à fait équiprobables (environ 30 % de A et de T chacun, 20 % de C et de G chacun). Quelle est l'entropie par base de cette loi ? Combien gagnerait-on par rapport à 1. ?
3. Les compresseurs spécialisés descendent vers 1,6 à 1,9 bit par base. Qu'exploitent-ils, que l'entropie de 2. ne voit pas ?
4. Deux humains ne diffèrent que sur environ 0,1 % des bases. Si l'on connaît déjà un génome de référence, combien de différences faut-il décrire ? En comptant environ 32 bits pour la position d'une différence et 2 bits pour la nouvelle base, combien de méga-octets ?
5. Compare avec la taille d'une photo de téléphone (quelques méga-octets).
6. Quelle idée du chapitre la question 4 illustre-t-elle ?

### Ex M06.15 — Expliquer l'information mutuelle avec deux capteurs 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, sans formule, ce que mesure l'information mutuelle, avec un exemple concret.
**Prérequis :** fiche §4 · **Parcours :** C, E

Une amie installe chez elle deux capteurs : un thermomètre dans le salon et un autre dans la chambre voisine ; plus tard, un détecteur d'ouverture de la porte d'entrée. Elle te demande : « Que veut dire, pour mes capteurs, que l'information mutuelle est grande ou nulle ? »

Réponds-lui **en huit lignes au plus**, sans formule. Ta réponse doit dire ce que mesure l'incertitude sur un capteur, ce que la lecture de l'un apprend sur l'autre, pourquoi la mesure est la même dans les deux sens, à quel couple de capteurs correspond une information mutuelle grande, et à quoi correspond une information mutuelle nulle.

<a id="entretien"></a>

## 💼 Entretien

### M06.E1 — Information mutuelle ou corrélation : laquelle détecte quoi ? 💼 ★ ⏱️ 10 min
*Fiche §4 · parcours C*

« Pour mesurer le lien entre une feature et la cible, vous utilisez la corrélation ou l'information mutuelle ? Quelle différence ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire ce que chacune mesure, donner un exemple où la corrélation est nulle alors que la dépendance est forte, et citer au moins un avantage de la corrélation. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m06_information/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M06.16 | Entropies conjointe et conditionnelle d'un tableau · `joint_entropy, conditional_entropy` | 🔨 | ★ | 20 | C, E |
| M06.17 | L'information mutuelle · `mutual_information` | 🔨 | ★ | 15 | C, E |
| M06.18 | Codes préfixes et somme de Kraft · `kraft_sum, is_prefix_code` | 🔨 | ★ | 15 | C |
| M06.19 | L'écart de Jensen d'une loi discrète · `jensen_gap` | 🔨 | ★ | 15 | C |
| M06.20 | `sklearn.metrics.mutual_info_score` contre ta fonction, en nats | 📦 | ★ | 15 | C |
| M06.21 | Prédire : l'information mutuelle de X et 2X, de X et X² | 🔮 | ★ | 10 | C, E |
| M06.22 | Estimer une entropie à partir d'un échantillon : le biais des petits échantillons | 🔬 | ★★ | 20 | C |
| M06.23 | Un diagramme de l'information : H(X), H(Y), H(X \| Y), I(X ; Y) | 🎨 | ★ | 20 | C |
| M06.24 | Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers | 🐛 | ★ | 15 | C |
| M06.25 | Calculer 0 log 0 proprement (`scipy.special.xlogy`) | 🛠️ | ★ | 10 | C |
| M06.26 | Défi : deviner un nombre de 1 à 100 en un minimum de questions | 🏆 | ★★★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
