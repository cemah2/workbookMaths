# M07 · Vecteurs et géométrie de ℝⁿ — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m07_vecteurs_rn/06_mes_reponses.md` (créée par `python tools/start_chapter.py M07`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Garde les valeurs exactes ($\sqrt{29}$, les fractions) jusqu'au bout, et n'arrondis qu'à la fin. Un **vecteur** s'écrit comme une liste de nombres, `[1, -2, 0.5]`.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M07.Q1 — Vecteurs, coordonnées et one-hot 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Un dataset a 500 lignes et 12 colonnes de nombres. Chaque exemple est un vecteur de quel espace ?
2. Vrai ou faux : on peut additionner un vecteur de $\mathbb{R}^3$ et un vecteur de $\mathbb{R}^4$.
3. Calcule $2\,(1, 0, -3) - (0, 4, 1)$.
4. Les moyens de transport {train, avion, bateau}, dans cet ordre, sont codés en one-hot. Écris le vecteur de « avion ».
5. Vrai ou faux : la somme des coordonnées d'un vecteur one-hot vaut toujours 1.
6. Écris $(4, -2, 5)$ comme une combinaison linéaire de $\mathbf{e}_1$, $\mathbf{e}_2$ et $\mathbf{e}_3$.

### M07.Q2 — Ce que mesure un produit scalaire 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. Calcule $(1, -2, 3) \cdot (4, 0, -1)$.
2. Vrai ou faux : le produit scalaire de deux vecteurs de $\mathbb{R}^5$ est un vecteur de $\mathbb{R}^5$.
3. On sait que $\mathbf{u} \cdot \mathbf{u} = 0$. Que vaut $\mathbf{u}$ ?
4. Que vaut $\mathbf{e}_2 \cdot (7, -3, 5)$ ?
5. Vrai ou faux : $(\mathbf{u} + \mathbf{v}) \cdot \mathbf{w} = \mathbf{u} \cdot \mathbf{w} + \mathbf{v} \cdot \mathbf{w}$.
6. Un neurone a les poids $\mathbf{w} = (2, -1)$ et le biais $b = 1$. Que vaut $z$ pour l'entrée $\mathbf{x} = (1, 3)$ ?

### M07.Q3 — Trois normes, trois boules unités 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Donne les normes L1, L2 et L∞ de $(0, -5, 0)$.
2. Quelle forme a la boule unité de L1 dans le plan ? Et celle de L∞ ?
3. Vrai ou faux : $\lVert \mathbf{x} \rVert_\infty \le \lVert \mathbf{x} \rVert_2 \le \lVert \mathbf{x} \rVert_1$ pour tout vecteur $\mathbf{x}$.
4. Exprime $\lVert -3\mathbf{x} \rVert$ en fonction de $\lVert \mathbf{x} \rVert$.
5. Quelle est la distance L1 entre $(1, 2)$ et $(6, 0)$ ?
6. Pourquoi la formule $\big(\sum_i |x_i|^{1/2}\big)^2$ ne définit-elle pas une norme ?

### M07.Q4 — Similarité cosinus : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. La similarité cosinus de deux vecteurs ne change pas quand on multiplie l'un d'eux par 10.
2. Elle ne change pas non plus quand on le multiplie par $-10$.
3. Un cosinus nul signifie que les deux vecteurs sont orthogonaux.
4. En dimension 4 ou plus, $|\mathbf{u} \cdot \mathbf{v}|$ peut dépasser $\lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert$.
5. Deux vecteurs non nuls dont toutes les coordonnées sont positives ou nulles ont un cosinus positif ou nul.
6. Deux vecteurs de cosinus 1 sont à une distance euclidienne nulle.

### M07.Q5 — Hyperplans : vecteur normal et côtés 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Dans $\mathbb{R}^4$, quelle est la dimension d'un hyperplan ?
2. Donne un vecteur normal à l'hyperplan $2x_1 - x_2 + 5x_3 = 7$ de $\mathbb{R}^3$.
3. De quel côté de l'hyperplan $x_1 + x_2 + x_3 - 1 = 0$ est l'origine : du côté où l'expression est positive ou négative ?
4. Vrai ou faux : $(\mathbf{w}, b)$ et $(3\mathbf{w}, 3b)$ décrivent le même hyperplan.
5. Vrai ou faux : $(\mathbf{w}, b)$ et $(-\mathbf{w}, -b)$ décrivent le même hyperplan, avec le même côté positif.
6. À quelle distance de l'origine passe l'hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ ?

### M07.Q6 — Moyenne, barycentre et inertie 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

1. Le barycentre des points $(0, 0)$, $(4, 0)$ et $(2, 6)$ ?
2. Vrai ou faux : le barycentre d'un nuage est toujours l'un de ses points.
3. En quel point $\mathbf{c}$ l'inertie $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2$ est-elle la plus petite ?
4. Que fait l'étape d'affectation de k-means ? Et l'étape de mise à jour ?
5. Vrai ou faux : une silhouette négative signale un point qui serait mieux dans le cluster voisin.
6. Avec k-means++, un point déjà choisi comme centre peut-il être tiré une seconde fois ?

### M07.Q7 — Intuitions de la grande dimension 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Quelle est la longueur de la diagonale du cube unité de $\mathbb{R}^{100}$ ?
2. Vrai ou faux : quand la dimension grandit, l'angle entre la diagonale du cube et un axe tend vers 90°.
3. On tire deux vecteurs de $\mathbb{R}^{10\,000}$ à coordonnées gaussiennes indépendantes. Leur cosinus est plutôt : (A) proche de 1 ; (B) proche de 0 ; (C) proche de $-1$ ; (D) n'importe quelle valeur entre $-1$ et 1, avec la même probabilité.
4. Un vecteur $\mathbf{X}$ de $\mathbb{R}^n$ a des coordonnées indépendantes de loi $\mathcal{N}(0, 1)$. Sa norme est d'environ combien ?
5. Vrai ou faux : en grande dimension, les distances entre points tirés au hasard dans le cube sont presque toutes égales, rapportées à leur taille.
6. Pourquoi ces constats gênent-ils les méthodes qui cherchent le plus proche voisin ?

<a id="rappels"></a>

## 🔁 Rappels

### M07.R1 — Produit scalaire et angle dans le plan (R9) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

1. $(2 ; 5) \cdot (-1 ; 3)$ ?
2. L'angle entre $(1 ; 0)$ et $(-1 ; \sqrt{3})$, en degrés ?
3. Un vecteur non nul orthogonal à $(5 ; -2)$ ?
4. Le vecteur unitaire de même direction et de même sens que $(-5 ; 12)$ ?
5. La projection de $(2 ; 6)$ sur la direction de $(1 ; 0)$ ?

### M07.R2 — Moyenne et variance empiriques (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

Les valeurs 4, 7, 7, 10, 12.
1. Leur moyenne ?
2. Leur variance, en divisant par $n$ ($\mathrm{ddof} = 0$) ?
3. Leur variance en divisant par $n - 1$ ($\mathrm{ddof} = 1$) ?
4. La somme des carrés des écarts à la moyenne ?
5. En quel nombre $c$ la somme $\sum_i (x_i - c)^2$ est-elle la plus petite ? Pourquoi ?

### M07.R3 — Gradient et point critique (M05b) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C*

Soit $f(c_1, c_2) = (c_1 - 2)^2 + (c_1 - 6)^2 + (c_2 - 1)^2 + (c_2 - 5)^2$.
1. Calcule $\frac{\partial f}{\partial c_1}$ et $\frac{\partial f}{\partial c_2}$.
2. Trouve le point critique de $f$.
3. Est-ce un minimum, un maximum ou un point selle ?
4. Que représente ce point par rapport aux points $(2, 1)$ et $(6, 5)$ ?
5. Que vaut $f$ en ce point ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"7/9"` ;
- une liste entre crochets, comme `[-1.5, 2.5, 0]` (un vecteur, un point, une liste de valeurs) ; vrai ou faux par `True` ou `False` ; une lettre entre guillemets, comme `"K"`.

### Ex M07.1 — Combinaisons linéaires et vecteurs one-hot dans ℝ⁴ ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des combinaisons linéaires de vecteurs de $\mathbb{R}^4$, retrouver des coefficients, et compter avec des vecteurs one-hot.
**Prérequis :** fiche §1 · **Parcours :** C, E

Soit $\mathbf{u} = (1, -2, 0, 4)$, $\mathbf{v} = (3, 1, -1, 2)$ et $\mathbf{w} = (0, 2, 5, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{u} + \mathbf{v}$ | une liste de 4 entiers |
| b | $2\mathbf{u} - 3\mathbf{v}$ | une liste de 4 entiers |
| c | $\mathbf{u} - \mathbf{v} + \mathbf{w}$ | une liste de 4 entiers |
| d | les réels $a$ et $b$ tels que $a\,\mathbf{u} + b\,\mathbf{v} = (5, -3, -1, 10)$ | la liste `[a, b]` |

Une application de covoiturage code le mode de chaque trajet en one-hot, dans l'ordre (vélo, bus, métro, marche).

| | Question | Réponse attendue |
|---|---|---|
| e | le vecteur de « métro » | une liste de 4 entiers |
| f | la somme des vecteurs one-hot de dix trajets : 4 à vélo, 3 en bus, aucun en métro et 3 à pied | une liste de 4 entiers |
| g | ce vecteur divisé par le nombre de trajets | une liste de 4 nombres |

Dans ta copie : pour d), écris le système de quatre équations ; combien d'équations suffisaient à trouver $a$ et $b$, et à quoi servent les autres ? Pourquoi ne code-t-on pas les quatre modes par 1, 2, 3, 4 ?

### Ex M07.2 — Produits scalaires, ‖u + v‖² et l'identité du parallélogramme ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des produits scalaires et des normes au carré, développer $\lVert \mathbf{u} + \mathbf{v} \rVert^2$, et retrouver un produit scalaire à partir de longueurs.
**Prérequis :** fiche §2 · **Parcours :** C, E

Soit $\mathbf{u} = (2, 1, -2, 0)$ et $\mathbf{v} = (1, 3, 1, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{u} \cdot \mathbf{v}$ | un entier |
| b | $\lVert \mathbf{u} \rVert^2$ | un entier |
| c | $\lVert \mathbf{v} \rVert^2$ | un entier |
| d | $\lVert \mathbf{u} + \mathbf{v} \rVert^2$ | un entier |
| e | le réel $t$ pour lequel $\mathbf{u} + t\,\mathbf{v}$ est orthogonal à $\mathbf{v}$ | une fraction irréductible |
| f | deux vecteurs $\mathbf{a}$ et $\mathbf{b}$ vérifient $\lVert \mathbf{a} + \mathbf{b} \rVert^2 = 50$ et $\lVert \mathbf{a} - \mathbf{b} \rVert^2 = 18$ : que vaut $\mathbf{a} \cdot \mathbf{b}$ ? | un entier |
| g | vrai ou faux : si $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$ et $\mathbf{u} \ne \mathbf{0}$, alors $\mathbf{v} = \mathbf{w}$ | `True` ou `False` |

Dans ta copie : calcule d) de deux façons, directement et avec le développement de la fiche. Pour g), donne un contre-exemple dans $\mathbb{R}^2$ ou une démonstration.

### Ex M07.3 — Normes L1, L2, L∞ et distances entre trois profils ✏️ ★ ⏱️ 20 min
**Objectif :** calculer des normes et des distances L1, L2 et L∞ en dimension 4, et voir que le plus proche voisin dépend de la norme.
**Prérequis :** fiche §3 · **Parcours :** C, E

Trois clients d'une banque sont décrits par quatre features standardisées : $P = (1, -2, 2, 0)$, $Q = (1, -5, 2, 0)$ et $R = (2, -3, 3, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les normes $[\lVert P \rVert_1, \lVert P \rVert_2, \lVert P \rVert_\infty]$ | une liste de 3 nombres |
| b | les distances $[d_1(P, R), d_2(P, R), d_\infty(P, R)]$ | une liste de 3 nombres |
| c | la distance euclidienne $d_2(Q, R)$ | un nombre (3 décimales) |
| d | le plus proche de $P$, parmi $Q$ et $R$, pour la distance L1 | une lettre, Q ou R |
| e | le plus proche de $P$, parmi $Q$ et $R$, pour la distance L2 | une lettre, Q ou R |
| f | le vecteur unitaire (pour L2) de même direction et de même sens que $P$ | une liste (4 décimales) |
| g | le membre de droite de l'inégalité triangulaire $d_2(P, Q) \le d_2(P, R) + d_2(R, Q)$ | un nombre (3 décimales) |

Dans ta copie : calcule aussi $d_1(P, Q)$, $d_2(P, Q)$ et $d_\infty(P, Q)$. Pourquoi les trois distances entre $P$ et $Q$ sont-elles égales ? Quel genre d'écart (concentré sur une coordonnée, ou réparti sur toutes) la distance L1 pénalise-t-elle le plus, et la distance L∞ ?

### Ex M07.4 — Similarité cosinus entre des profils d'écoute musicale ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des similarités cosinus, un angle et des distances, et voir que le cosinus ignore les longueurs.
**Prérequis :** fiche §3 et §4 · **Parcours :** C, E

Un service de musique décrit chaque auditeur par ses heures d'écoute de la semaine en (rock, jazz, rap, classique) : $A = (2, 0, 4, 4)$, $C = (0, 3, 0, 4)$ et $E = (4, 0, 8, 8)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert A \rVert$ | un entier |
| b | la similarité cosinus de $A$ et $C$ | une fraction irréductible |
| c | l'angle entre $A$ et $C$, en degrés | un nombre (2 décimales) |
| d | la distance euclidienne entre $A$ et $C$ | un nombre (4 décimales) |
| e | la similarité cosinus de $A$ et $E$ | un nombre |
| f | la distance euclidienne entre $A$ et $E$ | un nombre |
| g | le plus proche de $A$, parmi $C$ et $E$, pour la distance euclidienne | une lettre, C ou E |
| h | le plus proche de $A$, parmi $C$ et $E$, pour la similarité cosinus | une lettre, C ou E |

Dans ta copie : quel auditeur a les goûts les plus proches de ceux de $A$ ? Laquelle des deux mesures répond à cette question, et pourquoi l'autre se trompe-t-elle ? Quelle mesure choisirais-tu pour recommander des morceaux ?

### Ex M07.5 — Projeter sur une droite : composante parallèle et composante orthogonale ✏️ ★★ ⏱️ 20 min
**Objectif :** projeter un vecteur de $\mathbb{R}^4$ sur une droite, vérifier que le reste est orthogonal, et retrouver Pythagore.
**Prérequis :** fiche §4 · **Parcours :** C, E

Soit $\mathbf{x} = (5, -1, 2, 3)$ et $\mathbf{u} = (2, 0, 1, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{x} \cdot \mathbf{u}$ | un entier |
| b | le coefficient $t = \frac{\mathbf{x} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}$ | un nombre |
| c | la projection $\mathbf{p}$ de $\mathbf{x}$ sur la droite dirigée par $\mathbf{u}$ | une liste de 4 nombres |
| d | le reste $\mathbf{r} = \mathbf{x} - \mathbf{p}$ | une liste de 4 nombres |
| e | $\mathbf{r} \cdot \mathbf{u}$ | un nombre |
| f | $\lVert \mathbf{p} \rVert^2 + \lVert \mathbf{r} \rVert^2$ | un nombre |
| g | la projection de $\mathbf{x}$ sur la droite dirigée par $-3\mathbf{u}$ | une liste de 4 nombres |
| h | la composante de $\mathbf{x}$ le long de $\mathbf{u}$, $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert}$ | un nombre |

Dans ta copie : que vaut $\lVert \mathbf{x} \rVert^2$, et pourquoi le résultat de f) était-il prévisible ? Quel est le point de la droite le plus proche de $\mathbf{x}$, et à quelle distance est-il ?

### Ex M07.6 — Un plan de ℝ³ : vecteur normal, côté, distance signée ✏️ ★★ ⏱️ 20 min
**Objectif :** lire un vecteur normal, situer des points par rapport à un plan, calculer des distances signées et un point projeté.
**Prérequis :** fiche §5 · **Parcours :** C, E

Soit le plan $H$ d'équation $2x - y + 2z - 5 = 0$, et les points $A = (1, 1, 2)$, $B = (3, 0, 1)$, $O = (0, 0, 0)$ et $C = (-1, 2, 0)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le vecteur normal $\mathbf{w}$ qui se lit sur l'équation | une liste de 3 entiers |
| b | le point $A$ est-il sur $H$ ? | `True` ou `False` |
| c | le côté de $B$ : le signe de $2x - y + 2z - 5$ en $B$ | 1, −1 ou 0 |
| d | la distance signée de $B$ à $H$ | un nombre |
| e | la distance signée de $O$ à $H$ | une fraction irréductible |
| f | la distance de $C$ à $H$ | un nombre |
| g | le point de $H$ le plus proche de $B$ | une liste (4 décimales) |
| h | le nombre $b'$ tel que le plan $2x - y + 2z + b' = 0$, parallèle à $H$, passe par $B$ | un entier |

Dans ta copie : $O$ et $C$ sont-ils du même côté de $H$ ? Vérifie que le point trouvé en g) est bien sur $H$. Que vaut la distance entre les deux plans parallèles de h) ?

### Ex M07.7 — Un score linéaire w · x + b : calculer, décider, lire le vecteur normal ✏️ ★ ⏱️ 15 min
**Objectif :** calculer un score linéaire, en déduire une décision, et relier le vecteur des poids à la frontière.
**Prérequis :** fiche §2 et §5 · **Parcours :** C, E

Une usine décide d'arrêter une machine pour maintenance quand le score $z = \mathbf{w} \cdot \mathbf{x} + b$ est strictement positif, avec $\mathbf{w} = (1{,}5 ;\ 2 ;\ -0{,}5)$ et $b = -2$. Les trois features $\mathbf{x}$ sont la température, les vibrations et le temps depuis la dernière révision, chacune ramenée à une échelle commune. Trois machines : $M_1 = (1 ;\ 0{,}5 ;\ 2)$, $M_2 = (2, 1, 1)$ et $M_3 = (0, 1, 0)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le score de $M_1$ | un nombre |
| b | le score de $M_2$ | un nombre |
| c | la décision pour $M_1$ : 1 (arrêter) ou 0 (continuer) | 1 ou 0 |
| d | le score de $M_3$ | un nombre |
| e | de combien le score augmente-t-il quand les vibrations augmentent de 0,5, le reste étant fixé ? | un nombre |
| f | le vecteur unitaire dans la direction où le score augmente le plus vite | une liste (3 décimales) |
| g | la distance de $M_2$ à la frontière $z = 0$ | un nombre (4 décimales) |

Dans ta copie : où est $M_3$ par rapport à la frontière ? Que signifie le poids négatif de la troisième feature ? Si l'on multiplie $\mathbf{w}$ et $b$ par 10, que deviennent les décisions et la distance de g) ?

### Ex M07.8 — Centroïde, inertie et formule de König-Huygens ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un barycentre et des inerties, à la main puis avec la formule de König-Huygens.
**Prérequis :** fiche §6 · **Parcours :** C, E

Les cinq points du plan $(1, 3)$, $(2, -1)$, $(4, 2)$, $(0, 0)$ et $(3, 1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | leur barycentre $\bar{\mathbf{x}}$ | une liste de 2 nombres |
| b | l'inertie autour du barycentre, $\sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2$ | un nombre |
| c | l'inertie autour de l'origine | un nombre |
| d | l'inertie autour du point $(4, 3)$, avec la formule de König-Huygens | un nombre |
| e | la moyenne des carrés des distances au barycentre | un nombre |

On ajoute un sixième point, $(8, 7)$.

| | Question | Réponse attendue |
|---|---|---|
| f | le nouveau barycentre | une liste de 2 nombres |
| g | la nouvelle inertie autour du nouveau barycentre | un nombre |

Dans ta copie : vérifie c) avec la formule de König-Huygens. Pour g), utilise König-Huygens pour les cinq anciens points, sans recalculer leurs distances une à une. Pourquoi un seul point lointain fait-il autant grandir l'inertie ?

### Ex M07.9 — Où placer un dépôt : le barycentre pondéré des livraisons ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer un barycentre pondéré et voir qu'il minimise une somme pondérée de carrés de distances.
**Prérequis :** fiche §6 ; Ex M07.8 · **Parcours :** C

Une boulangerie livre trois magasins, situés (en km) en $S_1 = (0, 0)$, $S_2 = (6, 0)$ et $S_3 = (2, 4)$, qui reçoivent respectivement 3, 1 et 2 livraisons par jour. On cherche l'emplacement $\mathbf{c}$ du dépôt qui minimise le coût $\sum_i \omega_i \lVert S_i - \mathbf{c} \rVert^2$, où $\omega_i$ est le nombre de livraisons du magasin $i$.

| | Question | Réponse attendue |
|---|---|---|
| a | la somme des poids | un entier |
| b | le barycentre pondéré des magasins | une liste (4 décimales) |
| c | le coût en ce point | une fraction irréductible |
| d | le coût si le dépôt est au barycentre **non pondéré** des trois magasins | une fraction irréductible |
| e | vrai ou faux : doubler toutes les livraisons change l'emplacement optimal | `True` ou `False` |

Dans ta copie : écris la formule de König-Huygens avec des poids, et utilise-la pour d) ($\omega_i$ fois les carrés). Le coût choisi pénalise les grandes distances bien plus que les petites : est-ce raisonnable pour des livraisons ? Quel coût prendrais-tu à la place, et quel point le minimiserait (M07.31 et M07.35) ?

### Ex M07.10 — La silhouette d'un point, à la main, en dimension 2 ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer les distances moyennes $a$ et $b$ et la silhouette de points d'un petit découpage.
**Prérequis :** fiche §3 et §6 · **Parcours :** C

Un découpage en deux clusters : $\{A = (0, 0),\ B = (2, 0),\ C = (1, 2)\}$ et $\{D = (6, 1),\ F = (7, 3)\}$. Les distances sont euclidiennes.

| | Question | Réponse attendue |
|---|---|---|
| a | $a(A)$, la distance moyenne de $A$ aux autres points de son cluster | un nombre (4 décimales) |
| b | $b(A)$, la distance moyenne de $A$ aux points de l'autre cluster | un nombre (4 décimales) |
| c | la silhouette $s(A)$ | un nombre (3 décimales) |
| d | la silhouette $s(D)$ | un nombre (3 décimales) |
| e | on déplace $B$ dans le second cluster, sans bouger aucun point : la nouvelle silhouette de $B$ | un nombre (3 décimales) |
| f | la silhouette d'un point seul dans son cluster (la convention de la fiche) | un nombre |

Dans ta copie : le signe de e) était-il prévisible avant tout calcul ? Compare $a(D)$ à $a(A)$, puis $b(D)$ à $b(A)$ : lequel des deux nombres explique que $s(D)$ soit plus petite que $s(A)$ ?

### Ex M07.11 — k-means++ : des probabilités de tirage proportionnelles à D² ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer les probabilités de tirage de k-means++ pour le deuxième et le troisième centre, et les comparer à un tirage uniforme.
**Prérequis :** fiche §6 ; R8 (probabilités) · **Parcours :** C

Cinq points : $P_1 = (0, 0)$, $P_2 = (1, 0)$, $P_3 = (0, 3)$, $P_4 = (4, 2)$ et $P_5 = (5, 5)$. Le premier centre tiré est $P_1$.

| | Question | Réponse attendue |
|---|---|---|
| a | les carrés des distances $D^2$ des cinq points au premier centre, de $P_1$ à $P_5$ | une liste de 5 entiers |
| b | la probabilité que $P_5$ soit le deuxième centre | une fraction irréductible |
| c | la probabilité que $P_2$ soit le deuxième centre | une fraction irréductible |
| d | $P_5$ a été tiré. Les nouveaux $D^2$ (distance au centre le plus proche), de $P_1$ à $P_5$ | une liste de 5 entiers |
| e | la probabilité que $P_4$ soit le troisième centre | une fraction irréductible |
| f | avec un tirage **uniforme** parmi les quatre points restants, la probabilité que le deuxième centre soit $P_2$ | une fraction irréductible |

Dans ta copie : pourquoi $P_2$ est-il un mauvais deuxième centre ? Comparer c) et f) : que gagne k-means++ ? Que se passerait-il si un point très éloigné était une erreur de mesure ?

### Ex M07.12 — La diagonale du cube unité et son angle avec les axes, quand d grandit ✏️ ★ ⏱️ 15 min
**Objectif :** calculer la longueur de la diagonale du cube et ses angles avec les axes, et voir l'angle tendre vers 90°.
**Prérequis :** fiche §4 et §7 · **Parcours :** C, E

On note $\mathbf{1} = (1, \ldots, 1)$ le vecteur de $\mathbb{R}^d$ dont toutes les coordonnées valent 1 : la diagonale du cube unité $[0, 1]^d$ va de $\mathbf{0}$ à $\mathbf{1}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la longueur de la diagonale en dimension 4 | un nombre |
| b | la longueur de la diagonale en dimension 50 | un nombre (4 décimales) |
| c | l'angle entre la diagonale et l'axe $\mathbf{e}_1$ en dimension 4, en degrés | un nombre |
| d | le même angle en dimension 100, en degrés | un nombre (2 décimales) |
| e | la plus petite dimension $d$ pour laquelle cet angle dépasse 80° | un entier |
| f | le cosinus de l'angle entre $\mathbf{1}$ et le vecteur $(1, \ldots, 1, -1)$ (la dernière coordonnée change de signe), en dimension 10 | une fraction irréductible |

Dans ta copie : écris le cosinus de f) en fonction de $d$ ; vers quoi tend-il ? Deux sommets voisins d'une même face du cube, vus depuis son centre, font-ils un grand ou un petit angle en grande dimension ?

### Ex M07.13 — La distance au carré moyenne de deux points tirés dans le cube [0, 1]ᵈ ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer l'espérance du carré de la distance entre deux points uniformes du cube, et la comparer à la diagonale.
**Prérequis :** fiche §7 ; M02a (intégrales) ; M02b (espérance, variance, loi uniforme) · **Parcours :** C

$U$ et $V$ sont deux variables indépendantes de loi uniforme sur $[0, 1]$. $\mathbf{X}$ et $\mathbf{Y}$ sont deux points indépendants du cube $[0, 1]^d$, dont les $2d$ coordonnées sont des variables indépendantes de loi uniforme sur $[0, 1]$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{E}[U^2]$ | une fraction irréductible |
| b | $\mathbb{E}[UV]$ | une fraction irréductible |
| c | $\mathbb{E}[(U - V)^2]$ | une fraction irréductible |
| d | $\mathbb{E}\big[\lVert \mathbf{X} - \mathbf{Y} \rVert^2\big]$ en dimension 12 | un nombre |
| e | la distance typique $\sqrt{\mathbb{E}\big[\lVert \mathbf{X} - \mathbf{Y} \rVert^2\big]}$ en dimension 600 | un nombre |
| f | le rapport de cette distance typique à la longueur de la diagonale, $\sqrt{d}$ | un nombre (3 décimales) |

Dans ta copie : retrouve c) d'une seconde façon, avec $\mathbb{E}[U - V]$ et $\mathbb{V}(U - V)$. Le rapport f) dépend-il de $d$ ? Qu'en conclus-tu sur la place qu'occupent deux points pris au hasard dans un cube de grande dimension ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M07.14 — L'inégalité de Cauchy-Schwarz, par le discriminant ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer l'inégalité de Cauchy-Schwarz et son cas d'égalité en dimension quelconque, et en tirer une inégalité entre normes.
**Prérequis :** fiche §2 et §4 ; R3 (discriminant) · **Parcours :** C, E

Soit $\mathbf{u}$ et $\mathbf{v}$ deux vecteurs de $\mathbb{R}^n$, avec $\mathbf{v} \ne \mathbf{0}$.
1. Pour un réel $t$, développe $q(t) = \lVert \mathbf{u} + t\,\mathbf{v} \rVert^2$ : écris-le sous la forme $\alpha t^2 + \beta t + \gamma$, avec $\alpha$, $\beta$ et $\gamma$ exprimés à l'aide de produits scalaires.
2. Pourquoi $q(t) \ge 0$ pour tout $t$ ? Déduis-en le signe du discriminant de $q$, puis l'inégalité $|\mathbf{u} \cdot \mathbf{v}| \le \lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert$.
3. Que se passe-t-il quand $\mathbf{v} = \mathbf{0}$ ?
4. Montre que l'égalité a lieu si et seulement si $\mathbf{u}$ et $\mathbf{v}$ sont colinéaires. (Indication : un discriminant nul signifie que $q$ s'annule pour un certain $t$.)
5. Avec $\mathbf{v} = (1, \ldots, 1)$ et $\mathbf{u} = (|x_1|, \ldots, |x_n|)$, montre que $\lVert \mathbf{x} \rVert_1 \le \sqrt{n}\,\lVert \mathbf{x} \rVert_2$. Pour quels vecteurs y a-t-il égalité ?
6. Vérifie l'inégalité de 2 et celle de 5 sur $\mathbf{u} = (1, -1, 3)$ et $\mathbf{v} = (2, 0, 1)$.

### Ex M07.15 — L'inégalité triangulaire pour L2, L1 et L∞ ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'inégalité triangulaire des trois normes, sa forme renversée, et l'échec de la formule pour $p = \frac{1}{2}$.
**Prérequis :** fiche §3 ; Ex M07.14 · **Parcours :** C

Soit $\mathbf{u}$ et $\mathbf{v}$ deux vecteurs de $\mathbb{R}^n$.
1. Développe $\lVert \mathbf{u} + \mathbf{v} \rVert_2^2$, majore le double produit avec l'inégalité de Cauchy-Schwarz, et conclus que $\lVert \mathbf{u} + \mathbf{v} \rVert_2 \le \lVert \mathbf{u} \rVert_2 + \lVert \mathbf{v} \rVert_2$.
2. Démontre la même inégalité pour la norme L1, à partir de $|a + b| \le |a| + |b|$ pour deux réels.
3. Démontre-la pour la norme L∞.
4. Déduis de 1 l'**inégalité triangulaire renversée** : $\big|\,\lVert \mathbf{u} \rVert_2 - \lVert \mathbf{v} \rVert_2\,\big| \le \lVert \mathbf{u} - \mathbf{v} \rVert_2$. (Indication : écris $\mathbf{u} = (\mathbf{u} - \mathbf{v}) + \mathbf{v}$.)
5. Montre que la formule $N(\mathbf{x}) = \big(\sqrt{|x_1|} + \sqrt{|x_2|}\big)^2$ de $\mathbb{R}^2$ vérifie la positivité et l'homogénéité, mais pas l'inégalité triangulaire.

### Ex M07.16 — La moyenne minimise la somme des carrés des distances, en dimension n ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule de König-Huygens en dimension $n$, en déduire que le barycentre minimise l'inertie, et retrouver ce résultat avec le gradient.
**Prérequis :** fiche §2 et §6 ; M05b · **Parcours :** C, E

Soit $\mathbf{x}_1, \ldots, \mathbf{x}_m$ des points de $\mathbb{R}^n$, de barycentre $\bar{\mathbf{x}}$, et $\mathbf{c}$ un point de $\mathbb{R}^n$.
1. Montre que $\sum_{i=1}^{m} (\mathbf{x}_i - \bar{\mathbf{x}}) = \mathbf{0}$.
2. En écrivant $\mathbf{x}_i - \mathbf{c} = (\mathbf{x}_i - \bar{\mathbf{x}}) + (\bar{\mathbf{x}} - \mathbf{c})$, démontre la formule de König-Huygens : $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2 + m\,\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$.
3. Déduis-en que $\bar{\mathbf{x}}$ est l'unique point qui minimise $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2$.
4. Avec des poids $\omega_i \ge 0$ de somme $\Omega > 0$ et le barycentre pondéré $\bar{\mathbf{x}}_\omega$, énonce et démontre la formule correspondante.
5. Retrouve le résultat de 3 autrement : calcule le gradient de $J(\mathbf{c}) = \sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2$ par rapport aux coordonnées de $\mathbf{c}$, trouve son unique point critique, et explique pourquoi c'est un minimum.

### Ex M07.17 — La distance d'un point à un hyperplan vaut |w · x + b| / ‖w‖ ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule de la distance d'un point à un hyperplan et trouver le point le plus proche.
**Prérequis :** fiche §2, §4 et §5 · **Parcours :** C, E

Soit $H$ l'hyperplan d'équation $\mathbf{w} \cdot \mathbf{x} + b = 0$ de $\mathbb{R}^n$, avec $\mathbf{w} \ne \mathbf{0}$, et $\mathbf{x}_0$ un point de $\mathbb{R}^n$.
1. On cherche le point de la forme $\mathbf{x}_0 - t\,\mathbf{w}$ qui est sur $H$. Trouve $t$, puis le point $\mathbf{x}_H$.
2. Calcule $\lVert \mathbf{x}_0 - \mathbf{x}_H \rVert$.
3. Soit $\mathbf{y}$ un point quelconque de $H$. Montre que $\mathbf{x}_H - \mathbf{y}$ est orthogonal à $\mathbf{w}$, puis que $\lVert \mathbf{x}_0 - \mathbf{y} \rVert^2 = \lVert \mathbf{x}_0 - \mathbf{x}_H \rVert^2 + \lVert \mathbf{x}_H - \mathbf{y} \rVert^2$. Conclus que $\mathbf{x}_H$ est le point de $H$ le plus proche de $\mathbf{x}_0$, et que $d(\mathbf{x}_0, H) = \frac{|\mathbf{w} \cdot \mathbf{x}_0 + b|}{\lVert \mathbf{w} \rVert}$.
4. Montre que cette distance ne change pas quand on remplace $(\mathbf{w}, b)$ par $(\lambda\mathbf{w}, \lambda b)$, pour tout réel $\lambda \ne 0$.
5. Déduis de 3 la distance entre deux hyperplans parallèles $\mathbf{w} \cdot \mathbf{x} + b_1 = 0$ et $\mathbf{w} \cdot \mathbf{x} + b_2 = 0$.

### Ex M07.18 — Les deux étapes de k-means font baisser l'inertie, ou la laissent égale ∂ ★★★ ⏱️ 20 min
**Objectif :** démontrer qu'aucune étape de k-means n'augmente l'inertie, en déduire que l'algorithme s'arrête, et voir qu'il peut s'arrêter sur un mauvais découpage.
**Prérequis :** fiche §6 ; Ex M07.16 · **Parcours :** C

On note $J(c, \boldsymbol{\mu}) = \sum_{i=1}^{m} \lVert \mathbf{x}_i - \boldsymbol{\mu}_{c_i} \rVert^2$ l'inertie d'une affectation $c = (c_1, \ldots, c_m)$, où $c_i \in \{1, \ldots, k\}$ est le cluster du point $i$, et de centres $\boldsymbol{\mu} = (\boldsymbol{\mu}_1, \ldots, \boldsymbol{\mu}_k)$.
1. Les centres étant fixés, montre que l'étape d'affectation donne une inertie au plus égale à celle de l'affectation précédente.
2. L'affectation étant fixée, montre que l'étape de mise à jour donne une inertie au plus égale à celle des centres précédents. (Indication : regroupe les termes de $J$ par cluster et utilise M07.16 ; que faire d'un cluster vide ?)
3. Pourquoi la suite des inerties converge-t-elle ? On convient qu'un point garde son centre en cas d'égalité, et que l'algorithme s'arrête quand aucune affectation ne change. Montre qu'il s'arrête après un nombre fini d'étapes. (Indication : combien y a-t-il d'affectations possibles ?)
4. Quatre points, aux sommets d'un rectangle : $(0, 0)$, $(0, 1)$, $(5, 0)$ et $(5, 1)$, avec $k = 2$. Montre que les centres $(2{,}5 ;\ 0)$ et $(2{,}5 ;\ 1)$ ne bougent plus (ils sont un point fixe de l'algorithme), et compare leur inertie à celle du découpage en $\{(0, 0), (0, 1)\}$ et $\{(5, 0), (5, 1)\}$. Qu'en conclus-tu ?

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M07.19 — Pont : changer l'unité d'une feature change le plus proche voisin 🔗 ★ ⏱️ 15 min
**Objectif :** voir sur un exemple que le plus proche voisin dépend des unités, et que la standardisation règle le problème.
**Prérequis :** fiche §3 ; M02c (écart-type) · **Parcours :** C, E

Un site de vente de voitures d'occasion décrit chaque modèle par sa puissance (en chevaux) et sa masse. On cherche, pour la voiture $q$ de puissance 100 ch et de masse 1,2 t, la plus proche parmi $A$ (110 ch ; 1,9 t) et $B$ (130 ch ; 1,25 t), au sens de la distance euclidienne.

| | Question | Réponse attendue |
|---|---|---|
| a | la distance entre $q$ et $A$, avec la masse en tonnes | un nombre (2 décimales) |
| b | la distance entre $q$ et $B$, avec la masse en tonnes | un nombre (2 décimales) |
| c | la plus proche de $q$, avec la masse en tonnes | une lettre, A ou B |
| d | la plus proche de $q$, avec la masse en kilogrammes | une lettre, A ou B |
| e | les distances de $q$ à $A$ et à $B$ après standardisation, en divisant chaque écart par l'écart-type de sa feature dans le catalogue (20 ch pour la puissance, 0,25 t pour la masse) | une liste de 2 nombres (3 décimales) |
| f | la plus proche de $q$ après standardisation | une lettre, A ou B |

Dans ta copie : pourquoi la réponse change-t-elle entre c) et d) ? Pourquoi la standardisation donne-t-elle la même réponse quelle que soit l'unité de départ ? Quelles méthodes de workbookIA 7 sont concernées ?

### Ex M07.20 — MML §3.1 et §3.2.1 : normes et produit scalaire, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la définition d'une norme et du produit scalaire, et refaire les exemples du livre avec ses propres vecteurs.
**Prérequis :** fiche §2 et §3 · **Parcours :** C

Lis MML §3.1, puis §3.2.1. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Quelles sont les trois propriétés qui définissent une norme dans le livre ? Donne leur nom anglais, puis traduis-les avec les mots de la fiche.
2. Le livre présente deux exemples de normes. Lesquels ? Calcule-les pour le vecteur $(1, -3, 2, -1)$.
3. Le livre dessine, pour chacune, l'ensemble des vecteurs de norme 1 dans le plan. Décris ces deux figures. Laquelle des deux normes donne la plus grande valeur, pour un même vecteur, et comment le voit-on sur les figures ?
4. Comment le livre écrit-il le produit scalaire usuel au §3.2.1 ? Écris $(1, -3, 2, -1) \cdot (2, 1, 0, 4)$ avec cette notation et calcule-le.
5. Le livre annonce que le produit scalaire est un cas particulier d'une notion plus générale (§3.2.2). Laquelle ? Quelles propriétés de la fiche (§2) reconnais-tu dans sa définition ? (Survole seulement le §3.2.2.)
6. Note trois mots ou tournures en anglais de ces sections qui étaient nouveaux pour toi, avec leur traduction.

### Ex M07.21 — MML §3.3 et §3.4 : longueurs, distances, angles et orthogonalité 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais comment le livre déduit la longueur, la distance et l'angle d'un produit scalaire, et refaire ses exemples avec d'autres vecteurs.
**Prérequis :** fiche §3 et §4 ; Ex M07.20 · **Parcours :** C

Lis MML §3.3, puis §3.4 (jusqu'aux matrices orthogonales, que tu peux survoler). Réponds dans ta copie, avec tes mots.
1. Comment le livre définit-il la longueur d'un vecteur et la distance entre deux vecteurs à partir d'un produit scalaire ? Quel nom donne-t-il à une fonction de distance, et quelles sont ses trois propriétés ?
2. Où l'inégalité de Cauchy-Schwarz apparaît-elle, et à quoi sert-elle au §3.4 ?
3. Le livre calcule l'angle entre deux vecteurs du plan. Refais le calcul avec $(1, 2, 2)$ et $(2, -1, 2)$ de $\mathbb{R}^3$ : que vaut l'angle ?
4. Comment le livre définit-il deux vecteurs orthogonaux, et deux vecteurs orthonormés ?
5. Le livre montre que deux vecteurs orthogonaux pour le produit scalaire usuel peuvent ne pas l'être pour un autre produit scalaire. Vérifie-le avec $\mathbf{x} = (1, 1)$, $\mathbf{y} = (1, -1)$ et le produit scalaire $\langle \mathbf{x}, \mathbf{y} \rangle = 2x_1y_1 + x_2y_2$ : $\mathbf{x}$ et $\mathbf{y}$ sont-ils orthogonaux pour l'un, pour l'autre ? Quel angle font-ils pour le second ?
6. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M07.22 — Fermi : la mémoire d'un million d'embeddings 🧮 ★ ⏱️ 10 min
**Objectif :** estimer la mémoire et le temps de calcul d'une recherche par similarité cosinus dans un million de vecteurs.
**Prérequis :** fiche §1 et §4 · **Parcours :** C

Un moteur de recherche de documents représente chacun d'un million de documents par un *embedding*, un vecteur de $\mathbb{R}^{768}$, stocké en nombres à virgule flottante de 4 octets (`float32`).
1. Quelle mémoire occupent tous les vecteurs ? Et en `float16` (2 octets par nombre) ?
2. Pour une question, on calcule son produit scalaire avec chaque document (les vecteurs sont normalisés à l'avance, le cosinus est donc un produit scalaire). Combien de multiplications ?
3. Un ordinateur portable fait environ $10^{10}$ multiplications-additions par seconde. Combien de temps prend une recherche exacte ? Et pour un milliard de documents ?
4. Pourquoi normaliser les vecteurs **une fois** à l'avance, plutôt que de diviser par les normes à chaque question ?

Donne des ordres de grandeur, avec une puissance de 10, et explique chaque étape.

### Ex M07.23 — Expliquer la similarité cosinus à quelqu'un qui a fait le lycée 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, sans formule, ce que mesure une similarité cosinus et pourquoi elle ignore la longueur.
**Prérequis :** fiche §4 · **Parcours :** C, E

Une amie qui a fait des maths au lycée te demande : « Ton appli de musique dit que mes goûts ressemblent à 0,93 à ceux de mon frère, alors qu'il écoute dix fois plus que moi. Ça veut dire quoi ? »

Réponds-lui **en huit lignes au plus**, sans formule. Ta réponse doit dire ce que représente chaque profil (une flèche), ce que mesure le cosinus, pourquoi le temps d'écoute total ne compte pas, et ce que voudrait dire une similarité de 0.

<a id="entretien"></a>

## 💼 Entretien

### M07.E1 — Distance euclidienne ou similarité cosinus : laquelle pour comparer des textes ? 💼 ★ ⏱️ 10 min
*Fiche §3 et §4 · parcours C*

« Pour retrouver des documents proches d'une requête, vous utiliseriez la distance euclidienne ou la similarité cosinus ? Pourquoi ? Et si les vecteurs sont normalisés ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire ce que chaque mesure compare, l'effet de la longueur des documents, et ce qui se passe quand tous les vecteurs ont la norme 1 (développe $\lVert \mathbf{u} - \mathbf{v} \rVert^2$ pour deux vecteurs unitaires). Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m07_vecteurs_rn/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M07.24 | Normes Lp et similarité cosinus · `norm_p, cosine_similarity` | 🔨 | ★ | 20 | C, E |
| M07.25 | La projection sur une droite · `project_onto_line` | 🔨 | ★ | 15 | C, E |
| M07.26 | Barycentre et somme des carrés des distances · `centroid, sum_sq_distances_to` | 🔨 | ★ | 20 | C, E |
| M07.27 | Côté d'un hyperplan et distance à un hyperplan · `side_of_hyperplane, distance_to_hyperplane` | 🔨 | ★ | 20 | C, E |
| M07.28 | `np.linalg.norm` (ord = 1, 2, inf) et `scipy.spatial.distance` contre tes fonctions | 📦 | ★ | 10 | C |
| M07.29 | Prédire : l'angle de deux vecteurs tirés au hasard en dimension 1 000 | 🔮 | ★ | 10 | C, E |
| M07.30 | La norme d'un vecteur gaussien se concentre autour de √d | 🔬 | ★★ | 20 | C |
| M07.31 | Médiane ou moyenne : le centre qui minimise les distances L1 ou leurs carrés, face à des points aberrants | 🔬 | ★★ | 20 | C |
| M07.32 | Les boules unités L1, L2, L∞ et Lp dans le plan | 🎨 | ★ | 20 | C |
| M07.33 | Chasse à l'erreur : une distance sans racine, un cosinus mal normalisé, une projection sur un vecteur non unitaire | 🐛 | ★ | 15 | C |
| M07.34 | Les normes de toutes les lignes d'un tableau : axis, keepdims et broadcasting | 🛠️ | ★ | 15 | C |
| M07.35 | Défi : le point qui minimise la somme des distances (non au carré) à 60 villes, à 0,1 % près | 🏆 | ★★★ | 30 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
