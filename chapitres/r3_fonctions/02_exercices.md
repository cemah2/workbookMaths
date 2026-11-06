# R3 · Fonctions — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r3_fonctions/06_mes_reponses.md` (créée par `python tools/start_chapter.py R3`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️, 📈 et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂ et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ 📈 Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Sans calculatrice.** Tout ce fichier se fait à la main. Trace une courbe à main levée chaque fois qu'elle peut t'aider, et vérifie chaque résultat **avant** de le reporter dans le notebook : une racine en la remplaçant dans l'équation, une forme canonique en la redéveloppant, une réciproque en calculant $f^{-1}(f(x))$.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R3.Q1 — Image, antécédent, ensemble de définition 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

On pose $f(x) = x^2 - 5$. Vrai ou faux ?
1. L'image de $-3$ par $f$ est 4.
2. Le nombre 4 a deux antécédents par $f$.
3. Le nombre $-6$ a un antécédent par $f$.
4. Un nombre peut avoir deux images par une même fonction.
5. L'ensemble de définition de $x \mapsto \frac{1}{x + 1}$ est $]-1 \;;\; +\infty[$.
6. L'ensemble de définition de $x \mapsto \sqrt{x - 2}$ est $[2 \;;\; +\infty[$.

### R3.Q2 — Lire un graphique 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Sur la figure « Lire une image et des antécédents sur une courbe » de la fiche (§2), vrai ou faux ?
1. $f(1) = 1$.
2. Sur la fenêtre tracée, le nombre 1 a exactement deux antécédents.
3. $f$ est croissante sur $[0 \;;\; 3]$.
4. Le minimum de $f$ sur $[0 \;;\; 4]$ vaut $-1$.
5. L'équation $f(x) = -2$ a une solution dans $[0 \;;\; 4]$.
6. $f(2) > f(3)$.

### R3.Q3 — Pente et ordonnée à l'origine 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Vrai ou faux ?
1. La droite $y = -2x + 5$ a pour ordonnée à l'origine 5.
2. La droite $y = 3 - x$ monte quand $x$ augmente.
3. La droite qui passe par $(1, 2)$ et $(3, 8)$ a pour pente 3.
4. Une droite de pente 0 est verticale.
5. $x \mapsto 4x$ est une fonction affine.
6. Si $f$ est affine avec $f(0) = 1$ et $f(2) = 7$, alors $f(1) = 4$.

### R3.Q4 — Fonctions de référence : allure et variations 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Vrai ou faux ?
1. $x \mapsto x^2$ est croissante sur $\mathbb{R}$.
2. Si $0 < a < b$, alors $\frac{1}{a} > \frac{1}{b}$.
3. $\sqrt{x}$ est définie pour $x = -4$.
4. Pour tout réel $x$, $\sqrt{x^2} = x$.
5. $x \mapsto |x|$ est décroissante sur $]-\infty \;;\; 0]$.
6. $\max(0, x) = x$ pour tout $x \ge 0$.
7. $-3 < -1$, donc $(-3)^2 < (-1)^2$.

### R3.Q5 — Discriminant : combien de racines ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Combien de racines réelles ? Réponds par **aucune**, **une** ou **deux**, en calculant le moins possible.
1. $x^2 - 4x + 3$
2. $x^2 + 2x + 5$
3. $4x^2 - 4x + 1$
4. $-2x^2 + x + 1$
5. $x^2 + 7$
6. un polynôme du second degré dont la parabole est tournée vers le haut et a pour sommet $(2 \;;\; -3)$
7. $3x^2 + bx - 5$, quel que soit le nombre $b$

### R3.Q6 — Croissante, décroissante, extremum 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

Vrai ou faux ?
1. $f(x) = (x - 1)^2 + 2$ a pour minimum 2.
2. $g(x) = -(x + 3)^2 + 4$ a pour maximum 4, atteint en $x = 3$.
3. Sur $[1 \;;\; 5]$, le minimum de $x \mapsto x^2$ est 0.
4. Une fonction affine de pente $-2$ est décroissante sur $\mathbb{R}$.
5. Le maximum de $f$ et l'argmax de $f$ désignent la même chose.
6. Si $f$ est croissante sur $[0 \;;\; 4]$, son maximum sur $[0 \;;\; 4]$ est $f(4)$.

### R3.Q7 — f∘g ou g∘f ? 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

On pose $f(x) = \sqrt{x}$ et $g(x) = x + 9$. Vrai ou faux ?
1. $(f \circ g)(0) = 3$.
2. $(g \circ f)(0) = 3$.
3. $(f \circ g)(x) = \sqrt{x} + 9$.
4. $f \circ g$ est définie en $x = -5$.
5. $g \circ f$ est définie en $x = -5$.
6. Pour deux fonctions quelconques, $f \circ g = g \circ f$.

### R3.Q8 — Réciproque et inverse : ne pas confondre 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

On pose $f(x) = 2x + 6$. Vrai ou faux ?
1. $f^{-1}(y) = \frac{y - 6}{2}$.
2. $f^{-1}(x) = \frac{1}{2x + 6}$.
3. $f^{-1}(f(5)) = 5$.
4. $x \mapsto x^2$, définie sur $\mathbb{R}$, a une réciproque.
5. La réciproque de $x \mapsto \sqrt{x}$ (sur $[0 \;;\; +\infty[$) est $x \mapsto x^2$ sur $[0 \;;\; +\infty[$.
6. Les courbes de $f$ et de $f^{-1}$ sont symétriques par rapport à l'axe des abscisses.

<a id="rappels"></a>

## 🔁 Rappels

### R3.R1 — Identités remarquables (R2) 🔁 ★ ⏱️ 5 min
*Fiche R2 §3 · parcours C, E*

Sans regarder R2 :
1. développe $(x - 7)^2$ ;
2. développe $(3x + 2)^2$ ;
3. factorise $x^2 + 10x + 25$ ;
4. factorise $16x^2 - 9$ ;
5. quel nombre faut-il ajouter à $x^2 - 8x$ pour obtenir un carré parfait $(x - \ldots)^2$ ?

### R3.R2 — Inéquations et intervalles (R2) 🔁 ★ ⏱️ 5 min
*Fiche R2 §5 et §6 · parcours C, E*

Donne chaque ensemble en intervalle (ou en réunion d'intervalles).
1. Les solutions de $3x - 2 > 7$.
2. Les solutions de $-2x + 5 \ge 1$.
3. $[-1 \;;\; 4] \cap\, ]2 \;;\; 6]$.
4. Les réels différents de 3.
5. Les solutions de $|x - 1| < 4$.

### R3.R3 — Puissances et racines (R1) 🔁 ★ ⏱️ 5 min
*Fiche R1 §4 et §5 · parcours C*

1. $\sqrt{49}$
2. $\sqrt{\dfrac{9}{16}}$
3. $(-2)^3$
4. $\sqrt{48}$, sous la forme $a\sqrt{3}$
5. $\sqrt{a^2}$ quand $a < 0$ : $a$ ou $-a$ ?

<a id="papier"></a>

## ✏️ 📈 Papier-crayon

Fais-les **à la main**, en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée (les mêmes qu'en R2) :
- un nombre avec un point décimal, `-1.5` ; une fraction exacte entre guillemets, `"5/7"` ;
- une **liste de coefficients**, du plus haut degré au terme constant, sans oublier les zéros : pour $2x^2 - 5$, on écrirait `[2, 0, -5]` ;
- une **liste de valeurs** (solutions, antécédents, racines), dans l'ordre que tu veux, la liste vide s'il n'y en a aucune ; une fraction s'y écrit comme un calcul, sans guillemets : `[-2/7, 6]` ;
- un **intervalle** entre guillemets, `"]-1 ; 4]"`, `"[0 ; +oo["`, une réunion `"]-oo ; 0] U ]1 ; +oo["` ;
- une **fonction affine** $x \mapsto mx + c$ par la liste `[m, c]` ; une forme canonique $a(x - \alpha)^2 + \beta$ par la liste `[a, alpha, beta]` ;
- vrai ou faux par `True` ou `False`.

### Ex R3.1 — Images, antécédents et ensemble de définition ✏️ ★ ⏱️ 15 min
**Objectif :** calculer une image, chercher des antécédents en résolvant une équation, déterminer un ensemble de définition.
**Prérequis :** fiche §1 · **Parcours :** C, E

On pose $f(x) = 3x^2 - x - 4$, $g(x) = \dfrac{2x + 1}{x - 3}$, $h(x) = x^2 + 1$ et $k(x) = 4x - 5$.

| | Question | Réponse attendue |
|---|---|---|
| a | l'image de $-2$ par $f$ | un nombre |
| b | l'image de $\frac{1}{2}$ par $g$ | une fraction |
| c | les antécédents de 10 par $h$ | une liste |
| d | les antécédents de $-3$ par $h$ | une liste |
| e | l'antécédent de 7 par $k$ | un nombre |
| f | l'ensemble de définition de $x \mapsto \dfrac{1}{x - 4}$ | une réunion d'intervalles |
| g | l'ensemble de définition de $x \mapsto \sqrt{6 - 2x}$ | un intervalle |
| h | l'ensemble de définition de $x \mapsto \dfrac{\sqrt{x + 2}}{x - 1}$ | une réunion d'intervalles |

### Ex R3.2 — Lire des valeurs, des solutions et des variations sur un graphique 📈 ★ ⏱️ 15 min
**Objectif :** lire une image, des antécédents, un extremum, un sens de variation et les solutions d'une inéquation sur une courbe.
**Prérequis :** fiche §2 et §6 · **Parcours :** C, E

Voici la courbe d'une fonction $f$ définie sur $[-4 \;;\; 5]$. Toutes les réponses se lisent exactement sur le quadrillage.

![La courbe de f sur [−4 ; 5] : une ligne brisée de quatre segments, sur un quadrillage d'unité 1](figures/r3_2_graphique.png)

| | Question | Réponse attendue |
|---|---|---|
| a | $f(-2)$ | un nombre |
| b | $f(0)$ | un nombre |
| c | les antécédents de 1 | une liste |
| d | les solutions de $f(x) = -1$ | une liste |
| e | le maximum de $f$ sur $[-4 \;;\; 5]$ | un nombre |
| f | les valeurs de $x$ où ce maximum est atteint | une liste |
| g | le plus grand intervalle sur lequel $f$ est décroissante | un intervalle |
| h | les solutions de $f(x) \ge 1$ | une réunion d'intervalles |

### Ex R3.3 — La fonction affine qui passe par deux points ✏️ ★ ⏱️ 15 min
**Objectif :** calculer une pente et une ordonnée à l'origine, et s'en servir.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la fonction affine dont la courbe passe par $(2, 1)$ et $(6, 9)$ | la liste `[m, c]` |
| b | la fonction affine dont la courbe passe par $(-3, 7)$ et $(1, -1)$ | la liste `[m, c]` |
| c | la fonction affine dont la courbe passe par $(0, 4)$ et $(5, 6)$ | la liste `[m, c]` |
| d | la racine de la fonction de b (où sa droite coupe l'axe horizontal) | un nombre |
| e | $f$ est affine, avec $f(10) = 25$ et $f(30) = 35$ : la valeur de $f(50)$ | un nombre |
| f | le point $(4, 5)$ est-il sur la droite de a ? | `True` ou `False` |
| g | une course de taxi coûte 11 € pour 5 km et 19,40 € pour 12 km ; le prix est une fonction affine de la distance : le prix au kilomètre et la prise en charge (le prix pour 0 km) | la liste `[m, c]` |

### Ex R3.4 — Ramener des données entre 0 et 1 avec une fonction affine (min-max) ✏️ ★★ ⏱️ 20 min
**Objectif :** construire une normalisation min-max, calculer avec elle, et la défaire.
**Prérequis :** fiche §3 et §8 · **Parcours :** C, E

Les appartements d'un dataset ont des surfaces de 20 m² (la plus petite) à 120 m² (la plus grande). On veut une fonction affine $N$ qui envoie 20 sur 0 et 120 sur 1.

| | Question | Réponse attendue |
|---|---|---|
| a | la fonction $N$ | la liste `[m, c]` |
| b | la valeur normalisée d'un appartement de 65 m² | un nombre |
| c | la réciproque $N^{-1}$, qui ramène une valeur normalisée à une surface | la liste `[m, c]` |
| d | la surface dont la valeur normalisée est 0,8 | un nombre (en m²) |
| e | on préfère une note entre 0 et 10 : la fonction $S = 10 \times N$ | la liste `[m, c]` |

### Ex R3.5 — Variations et signe des fonctions de référence ✏️ ★ ⏱️ 15 min
**Objectif :** se servir des variations des fonctions de référence pour comparer et résoudre.
**Prérequis :** fiche §4 et §6 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | le plus grand intervalle sur lequel $x \mapsto x^2$ est décroissante | un intervalle |
| b | les solutions de $x^2 < 9$ | un intervalle |
| c | les solutions de $\dfrac{1}{x} > 2$ | un intervalle |
| d | les solutions de $\sqrt{x} \le 3$ | un intervalle |
| e | les solutions de $\lvert x \rvert \ge 2$ | une réunion d'intervalles |
| f | l'ensemble des valeurs prises par $x^2$ quand $x$ parcourt $[-2 \;;\; 1]$ | un intervalle |
| g | a-t-on $\dfrac{1}{-0{,}3} > \dfrac{1}{-0{,}2}$ ? | `True` ou `False` |

### Ex R3.6 — Forme canonique et sommet d'une parabole ✏️ ★★ ⏱️ 20 min
**Objectif :** mettre un polynôme du second degré sous forme canonique et en lire le sommet.
**Prérequis :** fiche §5 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la forme canonique de $x^2 + 6x + 2$ | la liste `[a, alpha, beta]` |
| b | la forme canonique de $2x^2 - 12x + 13$ | la liste `[a, alpha, beta]` |
| c | la forme canonique de $-x^2 + 4x + 1$ | la liste `[a, alpha, beta]` |
| d | le sommet de la parabole $y = 3x^2 + 6x - 2$ | la liste `[alpha, beta]` |
| e | la parabole de sommet $(-2 \;;\; 3)$ et de coefficient $a = 2$, sous forme développée $ax^2 + bx + c$ | la liste `[a, b, c]` |
| f | le nombre $a$ pour lequel la parabole $y = a(x - 1)^2 + 4$ passe par le point $(3, 12)$ | un nombre |

### Ex R3.7 — Racines par le discriminant et factorisation ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un discriminant, en déduire les racines, la factorisation et le signe.
**Prérequis :** fiche §5 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | le discriminant de $3x^2 - 5x - 2$ | un nombre |
| b | les racines de $3x^2 - 5x - 2$ | une liste |
| c | sa forme factorisée $a(x - x_1)(x - x_2)$, avec $x_1 < x_2$ | la liste `[a, x1, x2]` |
| d | les racines de $x^2 - 6x + 9$ | une liste |
| e | les racines de $2x^2 + x + 5$ | une liste |
| f | les racines de $-x^2 + 2x + 8$ | une liste |
| g | les solutions de $3x^2 - 5x - 2 < 0$ | un intervalle |

### Ex R3.8 — Trouver le maximum d'une aire ou d'un bénéfice ✏️ ★★ ⏱️ 20 min
**Objectif :** mettre un problème d'optimisation sous la forme d'un second degré, puis trouver son sommet.
**Prérequis :** fiche §5 et §6 ; R2 §8 · **Parcours :** C, E

**Un enclos.** On dispose de 40 m de grillage pour fermer un enclos rectangulaire le long d'un mur : le grillage ne fait que trois côtés. On note $x$ la longueur (en m) des deux côtés perpendiculaires au mur.

**Une recette.** Un vendeur de paniers repas constate que, s'il vend son panier $p$ euros, il en vend $200 - 4p$ par jour.

| | Question | Réponse attendue |
|---|---|---|
| a | l'aire maximale de l'enclos | un nombre (en m²) |
| b | la valeur de $x$ qui donne cette aire | un nombre (en m) |
| c | les valeurs de $x$ pour lesquelles l'aire vaut 150 m² | une liste |
| d | le prix qui rend la recette du vendeur maximale | un nombre (en €) |
| e | cette recette maximale | un nombre (en €) |

### Ex R3.9 — Composer deux fonctions dans les deux ordres ✏️ ★ ⏱️ 15 min
**Objectif :** calculer une composée en un point et sa formule, dans les deux ordres.
**Prérequis :** fiche §7 · **Parcours :** C, E

On pose $f(x) = x - 4$ et $g(x) = 2x^2 + 1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $(f \circ g)(2)$ | un nombre |
| b | $(g \circ f)(2)$ | un nombre |
| c | $(f \circ g)(x)$, développé | une liste de coefficients |
| d | $(g \circ f)(x)$, développé | une liste de coefficients |
| e | $(f \circ f)(x)$ | une liste de coefficients |
| f | $h(x) = (3x - 2)^3$ s'écrit $u(v(x))$ avec $u(t) = t^3$ : la fonction affine $v$ | la liste `[m, c]` |
| g | les valeurs de $x$ pour lesquelles $(g \circ f)(x) = (f \circ g)(x)$ | une liste |
| h | avec $p(x) = 3x - 2$ et $q(x) = -x + 5$, la composée $p \circ q$ | une liste de coefficients |

### Ex R3.10 — Trouver une réciproque et son ensemble de définition ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une réciproque en résolvant $y = f(x)$, et dire où elle est définie.
**Prérequis :** fiche §8 · **Parcours :** C, E

On pose $f(x) = 4x - 3$ sur $\mathbb{R}$, $g(x) = \dfrac{2}{x - 1}$ pour $x \ne 1$, et $h(x) = x^2 + 3$ sur $[0 \;;\; +\infty[$.

| | Question | Réponse attendue |
|---|---|---|
| a | la réciproque $f^{-1}$ | la liste `[m, c]` |
| b | $f^{-1}(9)$ | un nombre |
| c | $g^{-1}(4)$ | un nombre |
| d | l'ensemble de définition de $g^{-1}$ | une réunion d'intervalles |
| e | l'ensemble de définition de $h^{-1}$ | un intervalle |
| f | $h^{-1}(7)$ | un nombre |
| g | $x \mapsto x^2$, définie sur $\mathbb{R}$ tout entier, a-t-elle une réciproque ? | `True` ou `False` |

### Ex R3.11 — Fonctions par morceaux et argmax : max(0, x), |x|, la marche, et où une fonction atteint son maximum ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer avec des fonctions définies par morceaux, et distinguer un maximum de l'endroit où il est atteint.
**Prérequis :** fiche §4 et §6 · **Parcours :** C, E

On note $r(x) = \max(0, x)$ et $H$ la marche, avec la convention $H(0) = 1$ ($H(x) = 0$ si $x < 0$, $H(x) = 1$ si $x \ge 0$). On pose enfin $q(x) = -(x - 2)^2 + 3$.

| | Question | Réponse attendue |
|---|---|---|
| a | $r(-2{,}5)$ | un nombre |
| b | $r(3) + r(-3)$ | un nombre |
| c | les réels $x$ tels que $r(x) = 0$ | un intervalle |
| d | $H(0) + H(-0{,}1)$ | un nombre |
| e | $r(x) + r(-x)$, écrit plus simplement | une expression en `x`, entre guillemets |
| f | le maximum de $q$ sur $[3 \;;\; 6]$ | un nombre |
| g | l'argmax de $q$ sur $[3 \;;\; 6]$ | un nombre |
| h | la position du maximum de la liste $[6, 2, 9, 4, 9]$, en comptant à partir de 0 et en prenant la première, comme NumPy | un entier |

### Ex R3.12 — Évaluer un polynôme par le schéma de Horner ✏️ ★ ⏱️ 10 min
**Objectif :** appliquer le schéma de Horner à la main, et compter ce qu'il économise.
**Prérequis :** fiche §9 · **Parcours :** C

On pose $p(x) = 2x^3 - 3x^2 + 4x - 5$ et $q(x) = x^4 - 2x^2 + 3x - 1$.

| | Question | Réponse attendue |
|---|---|---|
| a | $p(2)$, par le schéma de Horner | un nombre |
| b | les valeurs courantes successives du schéma de Horner pour $p(2)$ (la première est le premier coefficient) | une liste, dans l'ordre |
| c | $q(-1)$, par le schéma de Horner (attention au coefficient nul) | un nombre |
| d | le nombre de multiplications que fait le schéma de Horner pour calculer $q(-1)$ | un entier |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut. La solution donne une **grille de relecture** pour juger la tienne.

### Ex R3.13 — Démontrer la formule des racines du second degré ∂ ★★ ⏱️ 35 min
**Objectif :** démontrer, à partir de la forme canonique, les trois cas du discriminant et les formules des racines.
**Prérequis :** fiche §5 ; R2 §3 · **Parcours :** C

Soient $a$, $b$, $c$ trois réels avec $a \ne 0$, et $\Delta = b^2 - 4ac$.
1. Démontre que, pour tout réel $x$, $ax^2 + bx + c = a\left[\left(x + \dfrac{b}{2a}\right)^2 - \dfrac{\Delta}{4a^2}\right]$ (tu peux développer le membre de droite).
2. On suppose $\Delta < 0$. Montre que le crochet est strictement positif pour tout $x$, et conclus que $ax^2 + bx + c$ n'a pas de racine réelle.
3. On suppose $\Delta = 0$. Montre que $ax^2 + bx + c = 0$ a une seule solution, que tu donneras.
4. On suppose $\Delta > 0$. Écris le crochet comme une différence de deux carrés, factorise-le avec une identité remarquable, et déduis-en les deux racines $x_1 = \dfrac{-b - \sqrt{\Delta}}{2a}$ et $x_2 = \dfrac{-b + \sqrt{\Delta}}{2a}$, ainsi que la factorisation $a(x - x_1)(x - x_2)$.
5. Toujours avec $\Delta > 0$, démontre que $x_1 + x_2 = -\dfrac{b}{a}$ et $x_1 x_2 = \dfrac{c}{a}$. Sers-t'en pour contrôler, sans les recalculer, les racines que tu as trouvées en R3.7 b.

### Ex R3.14 — Une fonction affine de pente positive est croissante ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer un sens de variation à partir de la définition, pour une fonction affine, puis pour la racine carrée et pour une composée.
**Prérequis :** fiche §3 et §6 ; R2.14 (règles des inégalités) · **Parcours :** C

On rappelle la définition : $f$ est strictement croissante sur $I$ si, pour tous $a < b$ dans $I$, $f(a) < f(b)$.
1. Soit $f(x) = mx + c$ avec $m > 0$, et $a < b$ deux réels. Calcule $f(b) - f(a)$ et montre que $f$ est strictement croissante sur $\mathbb{R}$.
2. Que se passe-t-il si $m < 0$ ? Et si $m = 0$ ?
3. Réciproquement, montre que si une fonction affine $f(x) = mx + c$ est croissante sur $\mathbb{R}$, alors $m \ge 0$ (regarde $f(0)$ et $f(1)$).
4. Montre que $x \mapsto \sqrt{x}$ est strictement croissante sur $[0 \;;\; +\infty[$ : pour $0 \le a < b$, écris $\sqrt{b} - \sqrt{a} = \dfrac{b - a}{\sqrt{b} + \sqrt{a}}$ (justifie cette égalité) et conclus.
5. Soient $f$ et $g$ deux fonctions définies sur $\mathbb{R}$. Montre que si $f$ et $g$ sont croissantes, alors $f \circ g$ est croissante ; et que si $f$ est croissante et $g$ décroissante, alors $f \circ g$ est décroissante.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R3.15 — Une fonction de coût donnée par une formule : une parabole et son sommet 🔗 ★★ ⏱️ 20 min
**Objectif :** lire une fonction de coût du second degré : sa valeur, son minimum, où il est atteint, et où elle reste sous un seuil.
**Prérequis :** fiche §5 et §6 · **Parcours :** C, E

Une ingénieure entraîne un modèle et mesure, après chaque epoch, son erreur sur des données de validation. Sur ses mesures, elle ajuste la formule

$$E(t) = 0{,}02\,t^2 - 1{,}2\,t + 25$$

où $t \ge 0$ est le nombre d'epochs et $E(t)$ l'erreur, en pourcentage.

| | Question | Réponse attendue |
|---|---|---|
| a | l'erreur après 10 epochs | un nombre |
| b | le nombre d'epochs qui rend l'erreur minimale (l'argmin) | un nombre |
| c | cette erreur minimale | un nombre |
| d | l'intervalle de $[0 \;;\; +\infty[$ sur lequel l'erreur diminue | un intervalle |
| e | les nombres d'epochs pour lesquels l'erreur ne dépasse pas 9 % | un intervalle |

Dans ta copie, explique en deux phrases ce que veut dire le fait que $E$ remonte après son minimum, et ce qu'une ingénieure en ferait.

### Ex R3.16 — Expliquer ce qu'est une fonction à quelqu'un qui n'aime pas les maths 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement ce qu'est une fonction, et ce qui n'en est pas une.
**Prérequis :** fiche §1 · **Parcours :** C, E

Une amie te dit : « Les fonctions, je n'ai jamais compris. C'est quoi, au fond ? »

Réponds-lui **en huit lignes au plus**, sans formule si possible. Ta réponse doit contenir : une image concrète (une machine, une recette, un tarif…), un exemple de la vie courante, la règle « une seule sortie pour chaque entrée » avec un exemple de règle qui n'est **pas** une fonction, et ce qu'est un antécédent.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r3_fonctions/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️, 📈 et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R3.21 | Tracer et lire les fonctions de référence | 📦 | ★ | 15 | C, E |
| R3.26 | Un graphique propre : titre, axes, légende | 🛠️ | ★ | 15 | C |
| R3.18 | La fonction affine qui passe par deux points · `affine_from_points` | 🔨 | ★ | 25 | C, E |
| R3.19 | Racines et sommet d'un polynôme du second degré · `quadratic_roots`, `quadratic_vertex` | 🔨 | ★★ | 40 | C, E |
| R3.22 | Faire varier a, b et c : déformer une parabole | 🎨 | ★★ | 20 | C, E |
| R3.24 | Combien de racines ? Le signe du discriminant sur une grille de paramètres | 🔬 | ★★ | 20 | C |
| R3.20 | Composer deux fonctions · `compose` | 🔨 | ★ | 25 | C, E |
| R3.23 | Prédire f∘g et g∘f pour « valeur absolue » et « moins 3 » | 🔮 | ★ | 10 | C |
| R3.25 | Chasse à l'erreur : composition, réciproque et racines | 🐛 | ★★ | 20 | C, E |
| R3.17 | Évaluer un polynôme par Horner · `polyval` | 🔨 | ★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
