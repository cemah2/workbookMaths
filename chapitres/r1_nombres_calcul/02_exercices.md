# R1 · Nombres et calcul — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r1_nombres_calcul/06_mes_reponses.md` (créée par `python tools/start_chapter.py R1`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, le rappel et les exercices ∂, 🧮 et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappel](#rappel) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Ponts, estimations, explications](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Sans calculatrice.** Tout ce fichier se fait à la main : c'est le but du chapitre. Le notebook vérifie ensuite tes résultats.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R1.Q1 — Quel ensemble ? Entiers, décimaux, rationnels, réels 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Pour chaque nombre, donne le **plus petit** ensemble parmi ℕ, ℤ, 𝔻, ℚ et ℝ qui le contient.
1. $-8$
2. $\frac{3}{8}$
3. $\frac{4}{6}$
4. $\sqrt{36}$
5. $\sqrt{10}$
6. $-\frac{12}{4}$

### R1.Q2 — Priorités et signes : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. $12 - 4 \times 2 = 16$
2. $-3^2 = -9$
3. $18 \div 6 \times 3 = 1$
4. $7 - (-2) = 5$
5. $(-2) \times (-3) \times (-1) = -6$
6. $-(4 - 9) = 5$

### R1.Q3 — Fractions : quelles opérations sont justes ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Juste ou faux ?
1. $\frac{2}{5} + \frac{1}{5} = \frac{3}{10}$
2. $\frac{3}{4} \times \frac{2}{9} = \frac{1}{6}$
3. $\frac{1}{4} \div \frac{1}{2} = \frac{1}{2}$
4. $\frac{6 + 5}{6} = 5$
5. $\frac{10}{15} = \frac{2}{3}$

### R1.Q4 — Règles des puissances : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. $4^3 \times 4^2 = 4^6$
2. $(5^2)^3 = 5^6$
3. $7^0 = 0$
4. $2^{-4} = -16$
5. $(-3)^4 = 81$
6. $2^3 + 2^3 = 2^4$
7. $\frac{10^5}{10^{-2}} = 10^3$

### R1.Q5 — Racines carrées : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. $\sqrt{64} = 8$ ou $-8$
2. $\sqrt{9 \times 16} = 12$
3. $\sqrt{25 - 16} = 1$
4. $\sqrt{(-6)^2} = 6$
5. $(\sqrt{11})^2 = 11$
6. $\sqrt{\frac{1}{4}} = \frac{1}{2}$
7. $2\sqrt{5} + 3\sqrt{5} = 5\sqrt{10}$

### R1.Q6 — Notation scientifique et chiffres significatifs 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

Vrai ou faux ?
1. $0{,}006\,30$ a trois chiffres significatifs.
2. $27 \times 10^{4}$ est écrit en notation scientifique.
3. $4{,}1 \times 10^{-3} = 0{,}0041$.
4. Arrondi à deux chiffres significatifs, $48\,615$ devient $49\,000$.
5. L'ordre de grandeur de $8\,200$ est $10^3$.
6. En Python, `6.02e23` est un entier (`int`).

### R1.Q7 — Les pièges des évolutions successives 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Vrai ou faux ?
1. Une hausse de 20 % puis une hausse de 30 % font une hausse de 50 %.
2. Multiplier un prix par 0,93, c'est le baisser de 7 %.
3. Après une baisse de 50 %, il faut une hausse de 100 % pour revenir au prix de départ.
4. Un prix qui passe de 40 € à 50 € augmente de 20 %.
5. Une baisse de 10 % suivie d'une hausse de 10 % ramène au prix de départ.
6. Un taux de chômage qui passe de 8 % à 6 % baisse de 2 %.

### R1.Q8 — Moyenne, moyenne pondérée, moyenne harmonique 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

Vrai ou faux ?
1. La moyenne de 2, 4, 6 et 100 représente bien ces quatre valeurs.
2. Avec les coefficients 3 et 6, la moyenne pondérée de 10 et de 16 est la même qu'avec les coefficients 1 et 2.
3. Une moyenne pondérée (à poids positifs) peut dépasser la plus grande des valeurs.
4. La moyenne harmonique de 20 et de 30 vaut 25.
5. Dans le calcul d'un neurone, $z = \sum_i w_i x_i + b$, on divise par la somme des poids.

<a id="rappel"></a>

## 🔁 Rappel

### R1.R1 — Taper une fraction et un intervalle pour `wbm.check` (R0) 🔁 ★ ⏱️ 5 min
*Fiche R0 §3 · parcours C, E*

Sans regarder R0, écris ce que tu taperais dans le notebook pour que `wbm.check` accepte :
1. la fraction $\frac{5}{12}$ ;
2. les réels supérieurs ou égaux à $-1$ et strictement inférieurs à 4 ;
3. les réels strictement positifs ;
4. l'expression $x^3 + 2x$.

5. Que se passe-t-il si tu tapes `2/7`, sans guillemets, pour la fraction $\frac{2}{7}$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main**, en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook** : une fraction entre guillemets (`"5/12"`), un décimal avec un point (`0.75`), une liste entre crochets (`[7.25, 7]`), un texte entre guillemets (`"ACE"`).

### Ex R1.1 — Placer des nombres sur la droite numérique et les ranger ✏️ ★ ⏱️ 10 min
**Objectif :** comparer des nombres écrits de façons différentes, négatifs compris, et les classer par ensemble.
**Prérequis :** fiche §1 · **Parcours :** C, E

On donne six nombres :

$$A = -2{,}5 \qquad B = \frac{2}{3} \qquad C = -\sqrt{4} \qquad D = 0{,}6 \qquad E = -\frac{3}{2} \qquad F = \frac{7}{4}$$

| | Question | Réponse attendue |
|---|---|---|
| a | les six lettres, dans l'ordre **croissant** des nombres | un texte, par exemple `"FEDCBA"` |
| b | combien d'entiers relatifs sont **strictement** compris entre $A$ et $F$ ? | un nombre |
| c | la ou les lettres des nombres qui sont des entiers relatifs | un texte |
| d | la ou les lettres des nombres qui ne sont **pas** décimaux | un texte |

### Ex R1.2 — Calculer avec les priorités et les signes ✏️ ★ ⏱️ 10 min
**Objectif :** appliquer l'ordre des opérations et la règle des signes sans erreur.
**Prérequis :** fiche §2 · **Parcours :** C, E

| | Calcul |
|---|---|
| a | $18 - 4 \times 3 + 2$ |
| b | $-6 - (-9)$ |
| c | $(-2)^3$ |
| d | $-2^4$ |
| e | $20 \div 4 \times 5$ |
| f | $3 - 2 \times (4 - 7)^2$ |
| g | $(-12) \div (-3) - 5$ |
| h | $-(5 - 11) + 2 \times (-4)$ |

### Ex R1.3 — Calcul mental avec la distributivité : 17 × 99, 23 × 101 ✏️ ★ ⏱️ 10 min
**Objectif :** se servir de la distributivité, dans les deux sens, pour calculer de tête.
**Prérequis :** fiche §2 · **Parcours :** C

Calcule **de tête** (écris seulement l'étape clé), en développant ou en factorisant.

| | Calcul |
|---|---|
| a | $17 \times 99$ |
| b | $23 \times 101$ |
| c | $9 \times 34 + 9 \times 66$ |
| d | $25 \times 44$ |
| e | $8 \times 47 - 8 \times 7$ |

### Ex R1.4 — Simplifier des fractions avec le PGCD ✏️ ★ ⏱️ 10 min
**Objectif :** trouver un PGCD (par les diviseurs ou par l'algorithme d'Euclide) et rendre une fraction irréductible.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{PGCD}(45, 75)$ | un entier |
| b | $\frac{45}{75}$ sous forme irréductible | une fraction |
| c | $\operatorname{PGCD}(252, 198)$, par l'algorithme d'Euclide | un entier |
| d | $\frac{252}{198}$ sous forme irréductible | une fraction |
| e | $\frac{-56}{98}$ sous forme irréductible | une fraction |
| f | $\frac{1001}{1309}$ sous forme irréductible (Euclide t'évite de chercher les diviseurs) | une fraction |

### Ex R1.5 — Additionner, multiplier et diviser des fractions ✏️ ★★ ⏱️ 20 min
**Objectif :** enchaîner les quatre opérations sur les fractions et rendre un résultat irréductible.
**Prérequis :** fiche §3 · **Parcours :** C, E

Donne chaque résultat sous forme **irréductible**.

| | Calcul |
|---|---|
| a | $\dfrac{3}{10} + \dfrac{4}{15}$ |
| b | $\dfrac{7}{12} - \dfrac{5}{8}$ |
| c | $\dfrac{14}{15} \times \dfrac{25}{21}$ |
| d | $\dfrac{7}{9} \div \dfrac{14}{27}$ |
| e | $1 + \dfrac{1}{1 + \frac{1}{2}}$ |
| f | les $\frac{3}{8}$ de 240 (un entier) |

### Ex R1.6 — Comparer des fractions ✏️ ★ ⏱️ 10 min
**Objectif :** comparer des fractions par un dénominateur commun ou par les produits en croix.
**Prérequis :** fiche §3 · **Parcours :** C

On pose $P = \frac{2}{3}$, $Q = \frac{5}{8}$ et $R = \frac{7}{12}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la plus grande des deux fractions $\frac{7}{9}$ et $\frac{11}{14}$ | une fraction |
| b | les lettres $P$, $Q$, $R$ dans l'ordre croissant | un texte, par exemple `"PQR"` |
| c | l'unique fraction de dénominateur 12 strictement comprise entre $\frac{1}{3}$ et $\frac{1}{2}$ | une fraction |
| d | $\frac{13}{40} > \frac{1}{3}$ ? | `True` ou `False` |

### Ex R1.7 — Appliquer les règles des puissances ✏️ ★ ⏱️ 15 min
**Objectif :** simplifier une expression avec les règles des puissances avant de calculer.
**Prérequis :** fiche §4 · **Parcours :** C, E

Simplifie d'abord avec les règles, puis donne la valeur.

| | Calcul | Réponse attendue |
|---|---|---|
| a | $\dfrac{7^5 \times 7^{-2}}{7^2}$ | un entier |
| b | $(2^3)^2 \times 2^{-4}$ | un entier |
| c | $\dfrac{5^2 \times 5}{5^4}$ | une fraction |
| d | $4^3 \times 25^3$ | un entier |
| e | $\left(\dfrac{3}{2}\right)^3$ | une fraction |
| f | $(-1)^{2027}$ | un entier |

### Ex R1.8 — Puissances négatives et puissances de 10 ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer avec des exposants négatifs et manipuler des puissances de 10.
**Prérequis :** fiche §4 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $4^{-2}$ | une fraction |
| b | $\left(\dfrac{1}{3}\right)^{-2}$ | un entier |
| c | $10^{-2} \times 10^{-3}$, en écriture décimale | un décimal |
| d | $(2 \times 10^{-3})^2$ en notation scientifique $m \times 10^k$ | la liste `[m, k]` |
| e | l'entier $k$ tel que $\dfrac{10^{9}}{10^{-3}} = 10^k$ | un entier |
| f | $0{,}5^{-3}$ | un entier |
| g | combien de nanosecondes dans une milliseconde ? Donne l'entier $k$ tel que la réponse soit $10^k$. | un entier |

### Ex R1.9 — Simplifier des racines carrées ✏️ ★ ⏱️ 15 min
**Objectif :** simplifier une racine en sortant le plus grand carré parfait, et calculer avec les règles des racines.
**Prérequis :** fiche §5 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | l'entier $a$ tel que $\sqrt{200} = a\sqrt{2}$ | un entier |
| b | l'entier $a$ tel que $\sqrt{75} = a\sqrt{3}$ | un entier |
| c | $\sqrt{12} \times \sqrt{3}$ | un entier |
| d | $\dfrac{\sqrt{98}}{\sqrt{2}}$ | un entier |
| e | $\sqrt{0{,}49}$ | un décimal |
| f | l'entier $a$ tel que $3\sqrt{20} - \sqrt{45} = a\sqrt{5}$ | un entier |
| g | $\sqrt{(-9)^2}$ | un entier |

### Ex R1.10 — Écrire en notation scientifique et arrondir ✏️ ★ ⏱️ 10 min
**Objectif :** passer d'une écriture décimale à la notation scientifique, arrondir à des chiffres significatifs et donner un ordre de grandeur.
**Prérequis :** fiche §6 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $72\,500\,000$ en notation scientifique $m \times 10^k$ | la liste `[m, k]` |
| b | $0{,}000\,090\,6$ en notation scientifique | la liste `[m, k]` |
| c | $314\,159$ arrondi à deux chiffres significatifs, en écriture décimale | un entier |
| d | $0{,}007\,849$ arrondi à deux chiffres significatifs | un décimal |
| e | l'ordre de grandeur de $0{,}000\,3$ : l'entier $k$ tel qu'il vaille $10^k$ | un entier |
| f | $\dfrac{8{,}4 \times 10^{-3}}{1{,}2 \times 10^{5}}$ en notation scientifique | la liste `[m, k]` |

### Ex R1.11 — Partie entière, arrondi au plus proche, arrondi supérieur ✏️ ★ ⏱️ 10 min
**Objectif :** calculer plancher, plafond et arrondi, y compris pour des négatifs, et choisir le bon dans un problème.
**Prérequis :** fiche §6 · **Parcours :** C, E

| | Question |
|---|---|
| a | $\lfloor 4{,}6 \rfloor$ |
| b | $\lfloor -4{,}6 \rfloor$ |
| c | $\lceil -0{,}4 \rceil$ |
| d | $\lceil 7 \rceil$ |
| e | $-1{,}49$ arrondi à l'unité la plus proche |
| f | des boîtes contiennent 12 œufs : combien de boîtes faut-il pour ranger 100 œufs ? |
| g | la valeur que Python affiche pour `int(-4.6)` |

### Ex R1.12 — Évolutions successives et évolution réciproque ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer avec des coefficients multiplicateurs : évolution, évolutions successives, évolution réciproque.
**Prérequis :** fiche §7 · **Parcours :** C, E

Donne les taux **en pourcentage, avec leur signe** : `-20` pour une baisse de 20 %, `32` pour une hausse de 32 %.

| | Question | Réponse attendue |
|---|---|---|
| a | un article à 64 € augmente de 12,5 % : son nouveau prix, en euros | un nombre |
| b | une population passe de 1 250 à 1 000 habitants : son taux d'évolution | un pourcentage |
| c | une hausse de 10 % suivie d'une hausse de 20 % : le taux d'évolution global | un pourcentage |
| d | trois baisses successives de 10 % : le taux global, arrondi au dixième | un pourcentage |
| e | l'évolution réciproque d'une hausse de 60 %, arrondie au dixième | un pourcentage |
| f | après une baisse de 30 %, la hausse qui ramène au départ, arrondie au centième | un pourcentage |

### Ex R1.13 — Règle de trois et proportionnalité ✏️ ★ ⏱️ 10 min
**Objectif :** reconnaître une situation de proportionnalité et calculer une quatrième proportionnelle.
**Prérequis :** fiche §7 · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | 3 kg de pommes coûtent 7,20 € : le prix de 5 kg, en euros | un nombre |
| b | un tableau de proportionnalité contient les colonnes $(4 ; 10)$ et $(6 ; y)$ : la valeur de $y$ | un nombre |
| c | une recette pour 4 personnes demande 300 g de farine : la masse pour 10 personnes, en grammes | un nombre |
| d | une voiture parcourt 135 km en 1 h 30 à vitesse constante : sa vitesse, en km/h | un nombre |
| e | le tableau de colonnes $(2 ; 5)$, $(6 ; 15)$ et $(9 ; 21)$ est-il un tableau de proportionnalité ? | `True` ou `False` |

### Ex R1.14 — Moyenne pondérée : la note finale et la somme pondérée d'un neurone ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer une moyenne pondérée, la retourner pour trouver une note manquante, et calculer une somme pondérée.
**Prérequis :** fiche §8 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | les notes 13 (coefficient 4), 9 (coefficient 1) et 16 (coefficient 3) : la moyenne pondérée | un décimal |
| b | un quatrième contrôle, de coefficient 2, s'ajoute aux trois notes de a : la note qu'il faut y avoir pour une moyenne de 14 | un décimal |
| c | la sortie $z = \sum_i w_i x_i + b$ d'un neurone, avec $\mathbf{w} = (1{,}5 \;;\; -2 \;;\; 0{,}5)$, $\mathbf{x} = (2 \;;\; 0{,}5 \;;\; 6)$ et $b = -1$ | un nombre |
| d | une cycliste monte un col à 15 km/h et redescend par la même route à 45 km/h : sa vitesse moyenne sur l'aller-retour, en km/h | un décimal |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut. La solution donne une **grille de relecture** pour juger la tienne.

### Ex R1.15 — Pourquoi a⁰ = 1 et a⁻ⁿ = 1/aⁿ : prolonger les règles des puissances ∂ ★★ ⏱️ 25 min
**Objectif :** comprendre que les définitions de $a^0$ et de $a^{-n}$ sont les seules qui gardent les règles des puissances vraies.
**Prérequis :** fiche §4 · **Parcours :** C, E

Soit $a$ un réel non nul. On veut donner un sens à $a^0$ et à $a^{-n}$ ($n$ entier, $n \ge 1$) de façon que la règle

$$a^m \times a^p = a^{m+p}$$

reste vraie pour **tous** les entiers $m$ et $p$, positifs, nuls ou négatifs.

1. En appliquant la règle avec $m = 1$ et $p = 0$, montre que $a^0$ ne peut valoir que 1.
2. En appliquant la règle avec $m = n$ et $p = -n$, montre que $a^{-n}$ ne peut valoir que $\frac{1}{a^n}$.
3. Avec ces définitions, vérifie que $\frac{a^m}{a^p} = a^{m-p}$ reste vraie quand $m < p$ : d'abord pour $m = 2$ et $p = 5$, puis en général (pour $m < p$ entiers positifs).
4. Pourquoi a-t-on exigé $a \ne 0$ ? Que vaudrait $0^{-1}$ ?

### Ex R1.16 — Pourquoi on n'additionne pas les dénominateurs ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la règle d'addition des fractions à partir de la définition d'une fraction, et voir ce que calcule la « fausse règle ».
**Prérequis :** fiche §3 · **Parcours :** C

On rappelle la définition : pour $b \ne 0$, $\frac{a}{b}$ est l'unique nombre $x$ tel que $b \times x = a$.

1. Montre par un contre-exemple que l'égalité $\frac{a}{b} + \frac{c}{d} = \frac{a + c}{b + d}$ est fausse en général.
2. Démontre, à partir de la définition, que $\frac{a}{d} + \frac{c}{d} = \frac{a + c}{d}$ (pour $d \ne 0$) : multiplie la somme par $d$.
3. Déduis-en que $\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}$ (pour $b \ne 0$ et $d \ne 0$).
4. ★ La « fausse règle » calcule un vrai nombre, la **médiante** $\frac{a + c}{b + d}$. Pour des nombres $a, b, c, d$ strictement positifs, avec $\frac{a}{b} < \frac{c}{d}$, montre qu'elle est toujours **entre** les deux fractions. Exemple concret : un joueur réussit 3 tirs sur 5 le samedi et 7 sur 10 le dimanche ; que représente $\frac{3 + 7}{5 + 10}$ ?

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Ponts, estimations, explications

### Ex R1.17 — Combien de paramètres, combien d'octets ? Un réseau en notation scientifique 🔗 ★★ ⏱️ 20 min
**Objectif :** compter les paramètres d'un petit réseau, puis estimer la mémoire qu'il occupe en notation scientifique.
**Prérequis :** fiche §6 et §8 · **Parcours :** C, E

Un réseau de neurones reçoit 300 nombres en entrée. Sa première couche a 200 neurones, la deuxième 50, et la couche de sortie 4. Chaque neurone calcule une somme pondérée $z = \sum_i w_i x_i + b$ de **toutes** les sorties de la couche précédente (les 300 entrées pour la première couche) : il a donc un poids par entrée, et un biais. Les poids et les biais s'appellent ensemble les **paramètres** du réseau.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de paramètres de la première couche | un entier |
| b | le nombre total de paramètres du réseau | un entier |
| c | l'ordre de grandeur de ce total : l'entier $k$ tel qu'il vaille $10^k$ | un entier |
| d | la mémoire occupée si chaque paramètre est un `float32` (4 octets), en notation scientifique à deux chiffres significatifs | la liste `[m, k]` (en octets) |
| e | un modèle de langage a $1{,}3 \times 10^{11}$ paramètres, stockés sur 16 bits (2 octets) chacun : la mémoire nécessaire, en Go ($1 \text{ Go} = 10^9$ octets) | un entier |

### Ex R1.18 — Fermi : combien de mots lis-tu dans une vie ? 🧮 ★★ ⏱️ 20 min
**Objectif :** mener une estimation de Fermi complète : découper, estimer, multiplier, juger.
**Prérequis :** fiche §9 · **Parcours :** C

Estime le nombre de mots que tu lis dans une vie : livres, écrans, messages, tout compte.
1. Découpe la question en quatre ou cinq facteurs (par exemple : mots lus par minute de lecture, minutes de lecture par jour, jours par an, années de lecture).
2. Estime chaque facteur, en disant d'où vient ton estimation.
3. Calcule le produit en notation scientifique, et arrondis-le à un chiffre significatif.
4. Juge ton résultat : la Bible compte environ $8 \times 10^5$ mots. Combien de « Bibles » lis-tu dans une vie ? Est-ce plausible ?
5. Quel facteur est le plus incertain ? De combien ton résultat changerait-il s'il était deux fois plus grand ?

### Ex R1.19 — Fermi : la place que prend un dataset de photos 🧮 ★★ ⏱️ 20 min
**Objectif :** estimer en ordres de grandeur la taille d'un dataset, et décider s'il tient sur une machine.
**Prérequis :** fiche §9 et §6 · **Parcours :** C, E

Une application de partage de photos a environ 2 millions d'utilisateurs actifs. Elle veut entraîner un modèle sur **toutes** les photos postées en un an.
1. Estime le nombre de photos postées en un an (combien de photos par utilisateur et par semaine ?).
2. Une photo de téléphone compressée pèse quelques mégaoctets : choisis une valeur et justifie-la. Estime la taille totale du dataset, en notation scientifique, puis en To ($1 \text{ To} = 10^{12}$ octets).
3. Un ordinateur portable a un disque de 1 To. Combien de disques faudrait-il ? Un serveur avec 100 To suffirait-il ?
4. Pour entraîner le modèle, on réduit chaque photo à $224 \times 224$ pixels, 3 couleurs, 1 octet par couleur. Combien pèse une photo réduite ? Le dataset réduit tient-il sur le serveur ?

### Ex R1.20 — Expliquer pourquoi +10 % puis −10 % ne ramène pas au départ 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement pourquoi des pourcentages successifs ne s'additionnent pas.
**Prérequis :** fiche §7 · **Parcours :** C, E

Un ami s'étonne : « Mon loyer a augmenté de 10 % l'an dernier, puis il a baissé de 10 % cette année. Il devrait être revenu au même prix, mais il est plus bas. Le propriétaire s'est trompé ? »

Réponds-lui **en cinq lignes au plus**, sans formule compliquée. Ta réponse doit dire : sur quelle valeur porte chaque pourcentage, ce qu'il paie maintenant par rapport au départ (avec un exemple chiffré de ton choix), et ce qu'il aurait fallu comme baisse pour revenir au loyer de départ.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r1_nombres_calcul/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R1.21 | PGCD par l'algorithme d'Euclide et fraction irréductible · `gcd`, `simplify_fraction` | 🔨 | ★★ | 40 | C, E |
| R1.22 | Additionner deux fractions sans passer par les décimaux · `add_fractions` | 🔨 | ★★ | 30 | C, E |
| R1.25 | Calculer exactement avec `fractions.Fraction` | 📦 | ★ | 10 | C, E |
| R1.28 | Chasse à l'erreur : cinq calculs de fractions et de puissances | 🐛 | ★ | 15 | C, E |
| R1.29 | Chasse à l'erreur : `-3**2` et les parenthèses | 🐛 | ★ | 10 | C, E |
| R1.23 | La notation scientifique à n chiffres significatifs · `scientific_notation` | 🔨 | ★★ | 40 | C |
| R1.26 | Prédire : arrondir deux fois, est-ce arrondir une fois ? | 🔮 | ★ | 10 | C |
| R1.30 | Les ordres de grandeur sur une échelle : de l'atome aux paramètres d'un LLM | 🎨 | ★ | 15 | C |
| R1.24 | Évolutions successives et moyenne pondérée · `successive_changes`, `weighted_mean` | 🔨 | ★ | 30 | C, E |
| R1.27 | Après n hausses de 10 % : tracer et comparer à une hausse de 10n % | 🔬 | ★★ | 20 | C |
| R1.31 | Écrire la docstring d'une fonction (format NumPy) | 🛠️ | ★ | 15 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
