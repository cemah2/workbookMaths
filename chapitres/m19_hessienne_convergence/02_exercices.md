# M19 · Hessienne, conditionnement et convergence — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m19_hessienne_convergence/06_mes_reponses.md` (créée par `python tools/start_chapter.py M19`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Ponts, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : la **hessienne** $\nabla^2 f$ est la matrice des dérivées secondes ; une **itération linéaire** s'écrit $\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$ et son **écart** est $\mathbf{e}_k = \mathbf{x}_k - \mathbf{x}^\star$ ; l'**itération de Richardson** pour $\mathbf{A}\mathbf{x} = \mathbf{b}$ est $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega(\mathbf{b} - \mathbf{A}\mathbf{x}_k)$, de pas $\omega$ ; le **conditionnement** d'une matrice symétrique définie positive est $\kappa = \lambda_{\max}/\lambda_{\min}$ ; une récurrence d'ordre 2 s'écrit $u_{k+2} = p\,u_{k+1} - q\,u_k$, de polynôme caractéristique $r^2 - pr + q$. « Gagner $d$ décimales », c'est diviser la norme de l'écart par $10^d$. Les angles sont en radians. Une matrice s'écrit dans le notebook comme une liste de ses **lignes**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M19.Q1 — La hessienne : de quelle taille, symétrique, de quoi ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Une fonction $f : \mathbb{R}^5 \to \mathbb{R}$ : quelle est la forme de sa hessienne ? Combien de dérivées secondes faut-il calculer, au plus, grâce à la symétrie ?
2. Vrai ou faux : la hessienne de $f$ est la jacobienne de son gradient.
3. La hessienne de $f(x, y, z) = xyz$ au point $(1, 2, 3)$ ?
4. La hessienne de $f(\mathbf{x}) = \frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$, pour $\mathbf{A}$ symétrique ?
5. Vrai ou faux : pour un polynôme de degré 2 en $n$ variables, le développement de Taylor d'ordre 2 est exact.
6. En un point où $\nabla^2 f = \operatorname{diag}(2, -4)$, la courbure de $f$ dans la direction unitaire $(0{,}6 ;\ 0{,}8)$ ?

### M19.Q2 — Minimum, maximum, selle ou direction plate ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

En un point critique, la hessienne a les valeurs propres indiquées. Réponds : minimum local, maximum local, point selle, ou le test ne conclut pas.

1. $3$ ; $1$ ; $0{,}5$.
2. $-2$ ; $-0{,}1$.
3. $4$ ; $-1$ ; $2$.
4. $2$ ; $0$ ; $5$.
5. La hessienne vaut $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ (sans calculer ses valeurs propres : son déterminant ?).
6. Vrai ou faux : en dimension 3, une hessienne de déterminant positif en un point critique signale un minimum.

### M19.Q3 — Converge ou pas : lire les valeurs propres de M 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

$\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$, avec $\mathbf{M}$ symétrique de valeurs propres données. L'itération converge-t-elle depuis tout départ ? Si oui, par quel facteur l'écart est-il multiplié, au pire, à chaque pas ?

1. $0{,}5$ et $-0{,}9$.
2. $1{,}1$ et $0{,}2$.
3. $-1$ et $0{,}3$.
4. $\mathbf{M} = 0{,}5\,\mathbf{I}$ : combien de pas pour diviser l'écart par 1 000 ?
5. Avec les valeurs propres $1{,}1$ et $0{,}2$, un départ dont l'écart est un vecteur propre de $0{,}2$ converge-t-il ?
6. Vrai ou faux : si toutes les valeurs propres de $\mathbf{M}$ sont de module $< 1$, la limite dépend du départ.

### M19.Q4 — Le pas de Richardson : lire la convergence sur les valeurs propres de I − ωA 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, de valeurs propres $2$ et $4$.

1. Les valeurs propres de $\mathbf{I} - \omega\mathbf{A}$ pour $\omega = 0{,}075$ ? Richardson converge-t-elle ?
2. Le pas critique ?
3. Pour $\omega = 0{,}6$ : les valeurs propres de $\mathbf{I} - \omega\mathbf{A}$, et la conclusion ?
4. Pour $\omega = -0{,}1$ : même question.
5. Le meilleur pas $\omega^\star$ de la fiche (§5), et le facteur de convergence qu'il donne ?
6. Vrai ou faux : si $0 < \omega < 2/\lambda_{\max}$, toutes les valeurs propres de $\mathbf{I} - \omega\mathbf{A}$ sont dans $]-1, 1[$.

### M19.Q5 — Le conditionnement : ce qui ralentit, ce qui ne change rien 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. $\mathbf{A}$ symétrique définie positive a pour valeurs propres extrêmes $0{,}5$ et $50$ : son conditionnement ?
2. On multiplie $\mathbf{A}$ et $\mathbf{b}$ par 10. Qu'est-ce qui change : le conditionnement, le pas critique, le nombre d'itérations au meilleur pas ?
3. Le facteur de Richardson au meilleur pas pour $\kappa = 100$ (3 décimales) ?
4. Pour gagner 6 décimales avec ce facteur, il faut environ : (A) 7 itérations ; (B) 70 ; (C) 700 ; (D) 7 000.
5. $\mathbf{A} = \begin{pmatrix} 9 & 0{,}9 \\ 0{,}9 & 1 \end{pmatrix}$ : la matrice $\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$ du préconditionnement diagonal, et son conditionnement ?
6. Vrai ou faux : remplacer les inconnues par $\mathbf{x} = \mathbf{Q}\mathbf{y}$, avec $\mathbf{Q}$ orthogonale, change le conditionnement.

### M19.Q6 — Module d'un nombre complexe et racines d'un trinôme 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. $\lvert 8 - 15i\rvert$ ?
2. Le conjugué de $2 + 7i$, et le produit de $2 + 7i$ par son conjugué ?
3. Les racines de $r^2 - 4r + 13$ ? Leur somme, leur produit, leur module ?
4. $\lvert(0{,}6 + 0{,}8i)^{10}\rvert$ ?
5. Vrai ou faux : les racines non réelles d'un trinôme à coefficients réels sont conjuguées.
6. Le module des racines de $r^2 - 0{,}2r + 0{,}49$ ?

### M19.Q7 — Un gradient estimé sur un échantillon : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

On estime le gradient d'une moyenne de $N$ termes par la moyenne des gradients de $B$ termes tirés au hasard, uniformément et avec remise (sauf au 5.).

1. Tirés uniformément avec remise, l'espérance de l'estimation est le vrai gradient.
2. Doubler $B$ divise par 2 la variance de l'estimation.
3. Doubler $B$ divise par 2 l'erreur type.
4. Pour diviser l'erreur type par 10, il faut multiplier $B$ par 100.
5. Sans remise, avec $B = N$, l'estimation est exacte.
6. Une estimation sans biais ne peut pas avoir le signe contraire du vrai gradient.

### M19.Q8 — Boule ou pavé : la direction est-elle gardée ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

1. La projection de $(0, 9)$ sur la boule de rayon 3 ?
2. La projection de $(7 ;\ 1{,}2)$ sur le pavé $[-2, 2]^2$ ? La direction est-elle gardée ?
3. La projection de $(5, -5)$ sur le pavé $[-2, 2]^2$ ? La direction est-elle gardée ?
4. La projection de $(2 ;\ -1{,}5)$ sur la boule de rayon 4 ?
5. Vrai ou faux : projeter deux fois de suite sur la même boule donne le même point que projeter une fois.
6. Vrai ou faux : couper chaque coordonnée à $\pm r$ projette sur la boule de rayon $r$.

<a id="rappels"></a>

## 🔁 Rappels

### M19.R1 — Le théorème spectral et les valeurs propres d'une matrice symétrique (M12c) 🔁 ★ ⏱️ 5 min
*Fiche §2 et §3 · parcours C, E*

$\mathbf{S} = \begin{pmatrix} 6 & 2 \\ 2 & 3 \end{pmatrix}$.

1. Les valeurs propres de $\mathbf{S}$ (trace et déterminant) ?
2. Un vecteur propre unitaire pour chacune ?
3. Vrai ou faux : pour toute matrice symétrique $2 \times 2$ à deux valeurs propres distinctes, les vecteurs propres associés sont orthogonaux.
4. Les valeurs propres de $\mathbf{S}^3$ ?
5. $\mathbf{S}$ est-elle définie positive ?
6. Écris $\mathbf{x}^\top\mathbf{S}\mathbf{x}$ avec les coordonnées $y_1$, $y_2$ de $\mathbf{x}$ dans la base des vecteurs propres.

### M19.R2 — Suites géométriques et récurrences d'ordre 1 (R5) 🔁 ★ ⏱️ 5 min
*Fiche §3 et §6 · parcours C, E*

1. $u_{k+1} = 0{,}7\,u_k$, $u_0 = 4$ : $u_3$ ?
2. Vers quoi tend $u_k$ ?
3. $v_{k+1} = 0{,}5\,v_k + 3$ : son point fixe ? L'expression de $v_k$ en fonction de $v_0$ ?
4. Le plus petit $k$ tel que $0{,}7^k < 0{,}01$ ?
5. Vrai ou faux : $w_{k+1} = -1{,}2\,w_k + 1$ converge depuis tout départ.

### M19.R3 — Le conditionnement par la SVD (M12d) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C*

1. Une matrice a pour valeurs singulières $8$ ; $2$ ; $0{,}5$ : son conditionnement ?
2. Pourquoi, pour une matrice symétrique définie positive, les valeurs singulières sont-elles les valeurs propres ?
3. Le conditionnement de $3\mathbf{A}$, connaissant celui de $\mathbf{A}$ ?
4. Le conditionnement d'une matrice orthogonale ?
5. $\mathbf{A} = \operatorname{diag}(3 ;\ -0{,}5)$ : son conditionnement ? Richardson converge-t-elle pour un pas $\omega > 0$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- `True` ou `False` pour un vrai ou faux.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M19.1 — La hessienne d'une fonction de trois variables, et son développement de Taylor d'ordre 2 ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un gradient et une hessienne, écrire le développement de Taylor d'ordre 2 et le comparer à la vraie valeur, puis lire une courbure.
**Prérequis :** fiche §1 ; M05b, M12c · **Parcours :** C, E

$f(x, y, z) = x^2z + yz^2 - 3xy + e^{x - y}$, au point $\mathbf{p} = (1, 1, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\nabla f(\mathbf{p})$ | une liste de 3 nombres |
| b | $\nabla^2 f(\mathbf{p})$ | une matrice |
| c | l'approximation de Taylor d'ordre 1 de $f(1{,}1 ;\ 0{,}8 ;\ 2{,}1)$ | un nombre |
| d | l'approximation de Taylor d'ordre 2 de $f(1{,}1 ;\ 0{,}8 ;\ 2{,}1)$ | un nombre |
| e | la vraie valeur $f(1{,}1 ;\ 0{,}8 ;\ 2{,}1)$ | un nombre (3 décimales) |
| f | la courbure de $f$ en $\mathbf{p}$ dans la direction unitaire $\mathbf{u} = \frac13(2, -1, 2)$ | un nombre |
| g | le déterminant du bloc $2 \times 2$ en haut à gauche de $\nabla^2 f(\mathbf{p})$ | un nombre |
| h | vrai ou faux : $\nabla^2 f(\mathbf{p})$ est définie positive | `True` ou `False` |

Dans ta copie : écris les six dérivées secondes distinctes. Compare les erreurs des approximations c) et d) : de quel ordre sont-elles en $\lVert\mathbf{h}\rVert$ ? Explique h) avec g) (critère de Sylvester, M12c §7), puis avec deux directions de courbures de signes contraires. La direction $\mathbf{u}$ est-elle un vecteur propre de la hessienne ? Entre quelles bornes la courbure dans une direction unitaire est-elle toujours comprise ?

### Ex M19.2 — Classer les points critiques d'une fonction de trois variables ✏️ ★★ ⏱️ 20 min
**Objectif :** trouver les points critiques d'une fonction de trois variables et les classer par les signes des valeurs propres de la hessienne.
**Prérequis :** fiche §2 ; M05b, M12c · **Parcours :** C, E

$f(x, y, z) = x^3 + 3xy^2 - 15x - 12y + z^2 - 2z$.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de points critiques | un entier |
| b | les points critiques, rangés par $x$ croissant | une liste de listes de 3 nombres |
| c | les valeurs propres de la hessienne en $(2, 1, 1)$, en ordre croissant | une liste de 3 nombres |
| d | les valeurs propres de la hessienne en $(-2, -1, 1)$, en ordre croissant | une liste de 3 nombres |
| e | le nombre de valeurs propres négatives de la hessienne en chaque point critique, dans l'ordre de b) | une liste de 4 entiers |
| f | la valeur de $f$ en son minimum local | un nombre |
| g | vrai ou faux : $(-2, -1, 1)$ est un maximum local | `True` ou `False` |

Dans ta copie : montre que $(x, y)$ vérifie $x^2 + y^2 = 5$ et $xy = 2$, et trouve les quatre solutions. Les valeurs propres de $\begin{pmatrix} 6x & 6y \\ 6y & 6x \end{pmatrix}$ sont $6x \pm 6y$ : pour quels vecteurs propres ? Pourquoi $f$ n'a-t-elle aucun maximum local ? Pour chaque point selle, donne une direction où $f$ descend. Le minimum est-il global ?

### Ex M19.3 — Une itération linéaire 2 × 2 : point fixe, erreur, et convergence par les valeurs propres ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer le point fixe et les itérés d'une itération linéaire, décomposer l'écart sur les vecteurs propres, et en tirer la vitesse de convergence.
**Prérequis :** fiche §3 ; M12c ; R5 · **Parcours :** C, E

$\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$, avec $\mathbf{M} = \begin{pmatrix} 0{,}5 & 0{,}2 \\ 0{,}2 & 0{,}2 \end{pmatrix}$ et $\mathbf{c} = (1{,}6 ;\ 0{,}8)$. Les vecteurs $\mathbf{q}_1 = (2, 1)$ et $\mathbf{q}_2 = (1, -2)$ sont des vecteurs propres de $\mathbf{M}$ (non normés).

| | Question | Réponse attendue |
|---|---|---|
| a | le point fixe $\mathbf{x}^\star$ | une liste de 2 nombres |
| b | $\mathbf{x}_1$ et $\mathbf{x}_2$ depuis $\mathbf{x}_0 = (0, 0)$ | une liste de 2 listes de 2 nombres |
| c | les valeurs propres de $\mathbf{M}$ associées à $\mathbf{q}_1$ puis à $\mathbf{q}_2$ | une liste de 2 nombres |
| d | depuis $\mathbf{x}_0 = (4, 7)$ : les coefficients $[a, b]$ de l'écart $\mathbf{e}_0 = a\,\mathbf{q}_1 + b\,\mathbf{q}_2$ | une liste de 2 nombres |
| e | $\mathbf{x}_3$ depuis $\mathbf{x}_0 = (4, 7)$ | une liste de 2 nombres |
| f | le plus petit nombre de pas qui divise par 1 000 la norme de l'écart, quel que soit le départ | un entier |
| g | vrai ou faux : depuis $\mathbf{x}_0 = (5, 0)$, la norme de l'écart est divisée exactement par 10 à chaque pas | `True` ou `False` |

Dans ta copie : vérifie que $\mathbf{x}_2 - \mathbf{x}^\star$ est un multiple de $\mathbf{x}_0 - \mathbf{x}^\star$ dans b), et explique pourquoi. Écris $\mathbf{e}_k$ en fonction de $k$ pour le départ de d). Pourquoi f) ne dépend-il que de la plus grande valeur propre ? Depuis quels départs l'écart diminue-t-il plus vite que ce que dit f) ?

### Ex M19.4 — Résoudre un système 2 × 2 par l'itération de Richardson : trois pas à la main, et le pas critique ✏️ ★★ ⏱️ 20 min
**Objectif :** faire trois pas de Richardson à la main, puis lire la convergence sur les valeurs propres de $\mathbf{I} - \omega\mathbf{A}$.
**Prérequis :** fiche §4 · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 5 & 3 \\ 3 & 5 \end{pmatrix}$ et $\mathbf{b} = (2 ;\ 6)$. On part de $\mathbf{x}_0 = \mathbf{0}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la solution $\mathbf{x}^\star$ de $\mathbf{A}\mathbf{x} = \mathbf{b}$ | une liste de 2 nombres |
| b | $\mathbf{x}_1$, $\mathbf{x}_2$, $\mathbf{x}_3$ avec $\omega = 0{,}08$ | une liste de 3 listes de 2 nombres (6 décimales) |
| c | le résidu $\mathbf{b} - \mathbf{A}\mathbf{x}_3$ | une liste de 2 nombres (6 décimales) |
| d | les valeurs propres de $\mathbf{A}$, en ordre décroissant | une liste de 2 nombres |
| e | les valeurs propres de $\mathbf{I} - 0{,}08\,\mathbf{A}$, dans le même ordre que d) | une liste de 2 nombres |
| f | le pas critique | un nombre |
| g | avec $\omega = 0{,}3$ : la valeur propre de $\mathbf{I} - \omega\mathbf{A}$ de plus grand module | un nombre |
| h | vrai ou faux : avec $\omega = 0{,}3$, l'itération partie de $\mathbf{x}_0 = \mathbf{x}^\star + (1, -1)$ converge | `True` ou `False` |

Dans ta copie : la solution est loin de $\mathbf{x}_3$ ; quelle composante de l'écart diminue lentement, et pourquoi ? Avec $\omega = 0{,}3$, décris ce que font les itérés depuis $\mathbf{0}$. Explique h) : pourquoi le théorème du §3 parle-t-il de « tout départ » ?

### Ex M19.5 — Le meilleur pas de Richardson (énoncé), et le nombre d'itérations pour gagner six décimales ✏️ ★★ ⏱️ 20 min
**Objectif :** appliquer les formules du meilleur pas et du facteur de convergence, et chiffrer le nombre d'itérations selon le pas et le conditionnement.
**Prérequis :** fiche §4 et §5 · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 7 & 6 & 0 \\ 6 & 7 & 0 \\ 0 & 0 & 7 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\mathbf{A}$, en ordre croissant | une liste de 3 nombres |
| b | le pas critique | une fraction irréductible, entre guillemets |
| c | le meilleur pas $\omega^\star$ | une fraction irréductible, entre guillemets |
| d | le facteur de convergence au meilleur pas | une fraction irréductible, entre guillemets |
| e | le plus petit nombre d'itérations qui gagne 6 décimales au meilleur pas | un entier |
| f | le facteur de convergence avec le pas prudent $\omega = 1/\lambda_{\max}$ | une fraction irréductible, entre guillemets |
| g | le plus petit nombre d'itérations qui gagne 6 décimales avec ce pas | un entier |
| h | pour une matrice de valeurs propres extrêmes $1$ et $110$, le plus petit nombre d'itérations qui gagne 6 décimales au meilleur pas | un entier |

Dans ta copie : vérifie d) avec la formule $\rho(\omega) = \max(\lvert 1 - \omega\lambda_{\min}\rvert, \lvert 1 - \omega\lambda_{\max}\rvert)$ du §4 ; pourquoi la valeur propre 7 ne compte-t-elle pas ? Compare e) et h) à l'approximation $1{,}15\,\kappa\,d$ de la fiche. Le pas prudent coûte combien de fois plus d'itérations ?

### Ex M19.6 — Une récurrence d'ordre 2 à racines réelles : terme général et convergence ✏️ ★★ ⏱️ 20 min
**Objectif :** résoudre une récurrence d'ordre 2 par son polynôme caractéristique, et trouver un départ qui converge malgré une racine de module $> 1$.
**Prérequis :** fiche §6 ; R3, R5 · **Parcours :** C, E

$u_{k+2} = 0{,}7\,u_{k+1} - 0{,}1\,u_k$, avec $u_0 = 3$ et $u_1 = 1{,}2$ ; puis $v_{k+2} = 1{,}5\,v_{k+1} + v_k$.

| | Question | Réponse attendue |
|---|---|---|
| a | les racines du polynôme caractéristique de $(u_k)$, en ordre décroissant | une liste de 2 nombres |
| b | les coefficients $[\alpha, \beta]$ de $u_k = \alpha\,r_1^k + \beta\,r_2^k$, $r_1$ étant la plus grande racine | une liste de 2 nombres |
| c | $[u_2, u_3]$ | une liste de 2 nombres |
| d | $u_{10}$ | un nombre (6 décimales) |
| e | les racines du polynôme caractéristique de $(v_k)$, en ordre décroissant | une liste de 2 nombres |
| f | la valeur de $v_1$ pour laquelle, avec $v_0 = 2$, $v_k$ tend vers 0 | un nombre |
| g | vrai ou faux : $(p, q)$ de la récurrence $(u_k)$ vérifie $\lvert q\rvert < 1$ et $\lvert p\rvert < 1 + q$ | `True` ou `False` |

Dans ta copie : vérifie c) par la formule de b). Quel terme de $u_k$ l'emporte quand $k$ grandit, et que vaut $u_{k+1}/u_k$ à la limite ? Pour $(v_k)$, quel coefficient doit être nul dans f) ? Que se passerait-il, sur ordinateur, si $v_1$ était arrondi à une valeur voisine ?

### Ex M19.7 — Une récurrence d'ordre 2 à racines complexes : module et oscillation amortie ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer les racines complexes d'une récurrence d'ordre 2, leur module et leur angle, et en tirer une oscillation amortie.
**Prérequis :** fiche §6 · **Parcours :** C, E

$u_{k+2} = 0{,}5\,u_{k+1} - 0{,}4225\,u_k$, avec $u_0 = 1$ et $u_1 = 0{,}25$.

| | Question | Réponse attendue |
|---|---|---|
| a | le discriminant du polynôme caractéristique | un nombre |
| b | la partie réelle des racines, puis leur partie imaginaire positive | une liste de 2 nombres |
| c | le module des racines | un nombre |
| d | l'angle $\theta \in\ ]0, \pi[$ tel que $\cos\theta = \frac{p}{2\sqrt q}$ | un nombre (4 décimales) |
| e | $[u_2, u_3, u_4, u_5]$ | une liste de 4 nombres (6 décimales) |
| f | les coefficients $[A, B]$ de $u_k = 0{,}65^k(A\cos k\theta + B\sin k\theta)$ | une liste de 2 nombres |
| g | le plus petit $k$ tel que $0{,}65^k < 10^{-3}$ | un entier |
| h | la période de l'oscillation, en pas | un nombre (2 décimales) |

Dans ta copie : vérifie $u_4$ par la formule de f). Pourquoi $\lvert u_k\rvert \le 0{,}65^k$ ici ? Sur un dessin, place les deux racines dans le plan, avec leur module et leur angle.

### Ex M19.8 — Une pente estimée sur B points tirés au hasard : espérance et variance de l'estimation ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer le gradient exact d'une moyenne et la dispersion des gradients individuels, puis la variance et l'erreur type d'une estimation sur un échantillon, avec et sans remise.
**Prérequis :** fiche §7 ; M02c, M09b · **Parcours :** C, E

On veut la résistance $a$ d'un composant, dont la tension vaut $U = a\,I$ (loi d'Ohm), à partir de quatre mesures $(I_k, U_k)$ : $(1, 2)$, $(2, 3)$, $(2, 5)$, $(3, 7)$. On minimise $F(a) = \frac14\sum_k(a\,I_k - U_k)^2$, et l'on note $g_k(a) = 2I_k(a\,I_k - U_k)$ la dérivée du terme $k$. On se place en $a = 2$.

| | Question | Réponse attendue |
|---|---|---|
| a | $F'(2)$ | un nombre |
| b | les quatre dérivées $[g_1(2), g_2(2), g_3(2), g_4(2)]$ | une liste de 4 nombres |
| c | la dispersion $\sigma^2 = \frac14\sum_k\big(g_k(2) - F'(2)\big)^2$ | un nombre |
| d | la variance de l'estimation sur $B = 2$ mesures tirées avec remise | un nombre |
| e | son erreur type | un nombre (4 décimales) |
| f | le plus petit $B$, avec remise, pour une erreur type au plus égale à $0{,}5$ | un entier |
| g | la variance de l'estimation sur $B = 2$ mesures distinctes tirées sans remise | un nombre (4 décimales) |
| h | la probabilité que l'estimation sur $B = 2$ mesures tirées avec remise soit strictement positive | une fraction irréductible, entre guillemets |
| i | la valeur $a^\star$ qui minimise $F$ | une fraction irréductible, entre guillemets |

Dans ta copie : que dit le signe de $F'(2)$ ? Énumère les 16 couples de tirages pour h). Pourquoi une estimation positive est-elle trompeuse ici ? Que deviennent $F'$ et l'estimation en $a = a^\star$ ?

### Ex M19.9 — Projeter un même vecteur sur une boule et sur un pavé : deux points, deux directions ✏️ ★ ⏱️ 15 min
**Objectif :** projeter un vecteur sur une boule et sur un pavé, et comparer les distances et les directions obtenues.
**Prérequis :** fiche §8 ; M07 · **Parcours :** C, E

$\mathbf{x} = (6, -3, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert\mathbf{x}\rVert$ | un nombre |
| b | la projection de $\mathbf{x}$ sur la boule de centre $\mathbf{0}$ et de rayon $2{,}8$ | une liste de 3 nombres |
| c | la projection de $\mathbf{x}$ sur le pavé $[-2, 2]^3$ | une liste de 3 nombres |
| d | les distances de $\mathbf{x}$ à ses projections b) et c) | une liste de 2 nombres (4 décimales) |
| e | le cosinus de l'angle entre $\mathbf{x}$ et sa projection c) | un nombre (4 décimales) |
| f | vrai ou faux : la projection de $(4, -4, 4)$ sur $[-2, 2]^3$ a la même direction que $(4, -4, 4)$ | `True` ou `False` |

Dans ta copie : pourquoi la projection sur la boule a-t-elle un cosinus égal à 1 avec $\mathbf{x}$ ? Le pavé contient-il la projection b) ? La boule contient-elle la projection c) ? Quel est le plus petit rayon d'une boule qui contient le pavé ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M19.10 — Une itération linéaire de matrice symétrique converge pour tout départ si et seulement si ses valeurs propres sont de module < 1 ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer le théorème des itérations linéaires du §3, par la décomposition dans une base de vecteurs propres.
**Prérequis :** fiche §3 ; M12c (théorème spectral, puissances) · **Parcours :** C, E

$\mathbf{M}$ est symétrique, de valeurs propres $\lambda_1, \ldots, \lambda_n$ et de vecteurs propres orthonormés $\mathbf{q}_1, \ldots, \mathbf{q}_n$ ; $\rho = \max_i\lvert\lambda_i\rvert$.

1. On suppose $\rho < 1$. Montre que $1$ n'est pas valeur propre de $\mathbf{M}$, et déduis-en que $\mathbf{I} - \mathbf{M}$ est inversible : l'itération a un unique point fixe $\mathbf{x}^\star$.
2. Montre que $\mathbf{e}_k = \mathbf{M}^k\mathbf{e}_0$, puis, en écrivant $\mathbf{e}_0 = \sum_iy_i\mathbf{q}_i$, que $\mathbf{e}_k = \sum_i\lambda_i^ky_i\mathbf{q}_i$.
3. Déduis-en $\lVert\mathbf{e}_k\rVert^2 = \sum_i\lambda_i^{2k}y_i^2 \le \rho^{2k}\lVert\mathbf{e}_0\rVert^2$, et conclus que $\mathbf{x}_k \to \mathbf{x}^\star$ depuis tout départ. Quand y a-t-il égalité ?
4. Réciproquement, on suppose que l'itération converge vers un même point $\boldsymbol{\ell}$ depuis tout départ. Montre que $\boldsymbol{\ell}$ est un point fixe. Puis, en partant de $\boldsymbol{\ell} + \mathbf{q}_j$, montre que $\lambda_j^k\mathbf{q}_j$ doit tendre vers $\mathbf{0}$, donc que $\lvert\lambda_j\rvert < 1$. Pourquoi l'hypothèse « un même point » est-elle nécessaire (pense à $\mathbf{M} = \mathbf{I}$) ?
5. Où la symétrie de $\mathbf{M}$ a-t-elle servi ? Pour $\mathbf{M} = \begin{pmatrix} 0{,}5 & 10 \\ 0 & 0{,}5 \end{pmatrix}$, calcule $\mathbf{M}^2\mathbf{e}_0$ pour $\mathbf{e}_0 = (0, 1)$ : la majoration du 3. vaut-elle encore ?

### Ex M19.11 — L'itération de Richardson converge si et seulement si 0 < ω < 2/λmax ∂ ★★ ⏱️ 15 min
**Objectif :** appliquer le théorème des itérations linéaires à Richardson, et en tirer le pas critique.
**Prérequis :** fiche §4 ; Ex M19.10 · **Parcours :** C, E

$\mathbf{A}$ est symétrique définie positive, de valeurs propres $0 < \lambda_{\min} = \lambda_1 \le \cdots \le \lambda_n = \lambda_{\max}$.

1. Écris l'itération de Richardson sous la forme $\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$. Montre que, pour $\omega \ne 0$, son unique point fixe est la solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$.
2. Montre que $\mathbf{M}$ est symétrique, et que ses valeurs propres sont les $1 - \omega\lambda_i$, avec les mêmes vecteurs propres que $\mathbf{A}$.
3. Montre que $\lvert 1 - \omega\lambda\rvert < 1$ équivaut à $0 < \omega\lambda < 2$. Conclus : l'itération converge vers la solution depuis tout départ si et seulement si $0 < \omega < 2/\lambda_{\max}$. (Pour $\omega = 0$, chaque départ est un point fixe.)
4. Montre que $\max_i\lvert 1 - \omega\lambda_i\rvert = \max(\lvert1 - \omega\lambda_{\min}\rvert, \lvert1 - \omega\lambda_{\max}\rvert)$.
5. Que se passe-t-il pour $\omega = 2/\lambda_{\max}$ exactement, depuis un départ dont l'écart a une composante sur le vecteur propre de $\lambda_{\max}$ ?

### Ex M19.12 — Une récurrence d'ordre 2 converge si et seulement si ses racines sont de module < 1 : le critère |q| < 1 et |p| < 1 + q ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer que toutes les solutions d'une récurrence d'ordre 2 tendent vers 0 exactement quand ses racines sont de module $< 1$, et lire cette condition sur ses coefficients.
**Prérequis :** fiche §6 ; R3 · **Parcours :** C

$u_{k+2} = p\,u_{k+1} - q\,u_k$, de polynôme $P(r) = r^2 - pr + q$ et de racines $r_1$, $r_2$ (réelles ou complexes conjuguées).

1. Racines distinctes : montre que, pour tous $u_0$, $u_1$, il existe un unique couple $(\alpha, \beta)$, éventuellement complexe, tel que $u_k = \alpha r_1^k + \beta r_2^k$ pour $k = 0$ et $k = 1$, puis, par récurrence, pour tout $k$.
2. Montre que toutes les solutions réelles tendent vers 0 si et seulement si $\lvert r_1\rvert < 1$ et $\lvert r_2\rvert < 1$. Pour la réciproque, choisis un départ qui donne $(\alpha, \beta) = (1, 0)$ ; si les racines sont complexes, utilise plutôt la partie réelle de la suite $r_1^k$, qui est une solution réelle. Traite aussi la racine double $r \ne 0$ : vérifie que $k\,r^k$ est solution, puis que $u_k = (\alpha + \beta k)r^k$ (on admet que $k\,s^k \to 0$ pour $0 \le s < 1$).
3. Racines complexes ($p^2 < 4q$) : montre que $\lvert r_1\rvert = \lvert r_2\rvert = \sqrt q$, puis que la condition équivaut à $q < 1$, et qu'alors $\lvert p\rvert < 2\sqrt q \le 1 + q$.
4. Racines réelles ($p^2 \ge 4q$) : montre que les deux racines sont dans $]-1, 1[$ si et seulement si $P(1) > 0$, $P(-1) > 0$ et $-1 < \frac p2 < 1$. Traduis $P(1) > 0$ et $P(-1) > 0$ en $\lvert p\rvert < 1 + q$, puis montre que, avec $p^2 \ge 4q$, ces conditions donnent $\lvert q\rvert < 1$.
5. Conclus : les deux racines sont de module $< 1$ si et seulement si $\lvert q\rvert < 1$ et $\lvert p\rvert < 1 + q$. Dessine la région dans le plan $(p, q)$.

### Ex M19.13 — La projection sur une boule est son point le plus proche, et elle garde la direction ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer les formules de projection sur une boule et sur un pavé, et dire quand la seconde garde la direction.
**Prérequis :** fiche §8 ; M07 (inégalité triangulaire) · **Parcours :** C

On note $B_r = \{\mathbf{y} : \lVert\mathbf{y}\rVert \le r\}$ et $\mathbf{x}$ un vecteur avec $\lVert\mathbf{x}\rVert > r$.

1. Montre que, pour tout $\mathbf{y} \in B_r$, $\lVert\mathbf{x} - \mathbf{y}\rVert \ge \lVert\mathbf{x}\rVert - r$ (inégalité triangulaire).
2. Montre que $\mathbf{y}^\star = r\,\mathbf{x}/\lVert\mathbf{x}\rVert$ atteint cette borne : c'est un point le plus proche.
3. Montre que c'est le seul : s'il y a égalité au 1., $\mathbf{y}$ est un multiple positif de $\mathbf{x}$ de norme $r$ (on admet le cas d'égalité de l'inégalité triangulaire : $\lVert\mathbf{a} + \mathbf{b}\rVert = \lVert\mathbf{a}\rVert + \lVert\mathbf{b}\rVert$ seulement si $\mathbf{a}$ et $\mathbf{b}$ sont des multiples positifs l'un de l'autre, ou si l'un est nul).
4. Pour le pavé $[-c, c]^n$, montre que $\lVert\mathbf{x} - \mathbf{y}\rVert^2 = \sum_i(x_i - y_i)^2$ est minimal pour $y_i = \min(\max(x_i, -c), c)$.
5. Pour $\mathbf{x}$ hors du pavé, montre que sa projection est un multiple $t\,\mathbf{x}$ de $\mathbf{x}$ si et seulement si toutes les coordonnées non nulles de $\mathbf{x}$ ont la même valeur absolue.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M19.14 — Pont : un pas de Richardson est un pas de descente sur ½ xᵀA x − bᵀx (énoncé, sans calcul) 🔗 ★ ⏱️ 10 min
**Objectif :** relier l'itération de Richardson à la descente de gradient, et traduire son vocabulaire dans celui de workbookIA 19.
**Prérequis :** fiche §4 ; M12c §7 · **Parcours :** C

$\mathbf{A}$ est symétrique définie positive, et $f(\mathbf{x}) = \frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$. Réponds par une lettre, sauf au g).

| | Question | Réponse attendue |
|---|---|---|
| a | $\nabla f(\mathbf{x})$ : (A) $\mathbf{b} - \mathbf{A}\mathbf{x}$ ; (B) $\mathbf{A}\mathbf{x} - \mathbf{b}$ ; (C) $\frac12\mathbf{A}\mathbf{x} - \mathbf{b}$ ; (D) $\mathbf{A}^\top\mathbf{b}$ | une lettre entre guillemets |
| b | $\nabla^2 f$ : (A) $\mathbf{b}$ ; (B) $\frac12\mathbf{A}$ ; (C) $\mathbf{A}$ ; (D) $2\mathbf{A}$ | une lettre entre guillemets |
| c | le pas de Richardson $\mathbf{x} + \omega(\mathbf{b} - \mathbf{A}\mathbf{x})$ s'écrit : (A) $\mathbf{x} - \omega\nabla f(\mathbf{x})$ ; (B) $\mathbf{x} + \omega\nabla f(\mathbf{x})$ ; (C) $\mathbf{x} - \omega f(\mathbf{x})$ ; (D) $\mathbf{x} - \omega\nabla^2 f\,\mathbf{x}$ | une lettre entre guillemets |
| d | dans le vocabulaire de workbookIA 19, $\omega$ est : (A) le learning rate ; (B) la taille du mini-batch ; (C) le nombre d'itérations ; (D) le conditionnement | une lettre entre guillemets |
| e | le pas au-dessus duquel la descente sur $f$ diverge pour certains départs : (A) $1/\lambda_{\max}$ ; (B) $2/\lambda_{\max}$ ; (C) $2/\lambda_{\min}$ ; (D) $\frac{2}{\lambda_{\min} + \lambda_{\max}}$ | une lettre entre guillemets |
| f | le résidu $\mathbf{b} - \mathbf{A}\mathbf{x}$ est : (A) le gradient de $f$ ; (B) l'opposé du gradient de $f$ ; (C) la hessienne de $f$ ; (D) la valeur de $f$ | une lettre entre guillemets |
| g | vrai ou faux : le minimum de $f$ est la solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$ | `True` ou `False` |

Dans ta copie : pour les deux ressorts de la fiche, que représente $f$ ? Pourquoi le résidu est-il perpendiculaire aux lignes de niveau de $f$ (M05b) ? Quelle hypothèse sur $\mathbf{A}$ garantit que $f$ a un unique minimum ?

### Ex M19.15 — Pont : le préconditionnement diagonal, une idée commune à plusieurs méthodes de workbookIA 19 🔗 ★ ⏱️ 15 min
**Objectif :** mesurer ce que gagne une mise à l'échelle diagonale, et ce qu'elle ne peut pas corriger.
**Prérequis :** fiche §5 ; Ex M19.5 · **Parcours :** C

Un système $\mathbf{A}\mathbf{x} = \mathbf{b}$ a pour matrice $\mathbf{A} = \begin{pmatrix} 16 & 1 \\ 1 & 0{,}25 \end{pmatrix}$ : ses deux inconnues vivent à des échelles très différentes. On note $\mathbf{D} = \operatorname{diag}(16 ;\ 0{,}25)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\mathbf{A}$, en ordre décroissant | une liste de 2 nombres (3 décimales) |
| b | le conditionnement de $\mathbf{A}$ | un nombre (1 décimale) |
| c | la matrice $\tilde{\mathbf{A}} = \mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$ | une matrice |
| d | le conditionnement de $\tilde{\mathbf{A}}$ | un nombre |
| e | le plus petit nombre d'itérations qui gagne 6 décimales au meilleur pas, pour $\mathbf{A}$ puis pour $\tilde{\mathbf{A}}$ | une liste de 2 entiers |
| f | les nouvelles inconnues $\mathbf{y} = \mathbf{D}^{1/2}\mathbf{x}$ pour $\mathbf{x} = (0{,}5 ;\ 2)$ | une liste de 2 nombres |

Dans ta copie : écris le pas de Richardson sur $\tilde{\mathbf{A}}$ dans les inconnues $\mathbf{x}$ : chaque coordonnée du résidu est divisée par quoi ? Pour $\begin{pmatrix} 1 & 0{,}9 \\ 0{,}9 & 1 \end{pmatrix}$, que fait la mise à l'échelle diagonale à son conditionnement, et pourquoi ? Le chapitre 19 de workbookIA retrouvera l'idée d'une mise à l'échelle diagonale : résume en une phrase, pour la relire alors, ce qu'elle peut et ne peut pas changer au conditionnement d'un système.

### Ex M19.16 — MML §5.7 et §5.8 : dérivées d'ordre supérieur et Taylor à plusieurs variables, en anglais 📖 ★★ ⏱️ 35 min
**Objectif :** lire deux sections de MML en anglais, et relier leurs notations à celles de la fiche.
**Prérequis :** fiche §1 · **Parcours :** C

Lis MML §5.7 (*Higher-Order Derivatives*) et §5.8 (*Linearization and Multivariate Taylor Series*), crayon en main, puis réponds dans ta copie, en français :
1. Quelles notations MML utilise-t-il pour les dérivées secondes et pour la hessienne ? Que dit-il de sa symétrie, et sous quelle hypothèse ?
2. Quelle est la forme de la hessienne d'une fonction de $\mathbb{R}^n$ dans $\mathbb{R}^m$, d'après le §5.7 ? Pourquoi la fiche se limite-t-elle à $m = 1$ ?
3. Comment MML écrit-il le terme d'ordre $k$ de la série de Taylor, avec $D^k_{\mathbf{x}}f$ et $\boldsymbol{\delta}^k$ ? Écris les termes d'ordre 1 et 2 avec les notations de la fiche.
4. Refais l'exemple de la fin du §5.8 jusqu'à l'ordre 2 en un autre point de ton choix, et vérifie ta hessienne dans le notebook.
5. Relève trois expressions anglaises de ces sections et leur traduction dans la fiche.

### Ex M19.17 — MML §7.1 : la descente de gradient, le pas, le momentum et la version stochastique, en anglais 📖 ★★ ⏱️ 40 min
**Objectif :** lire la section de MML sur la descente de gradient, et la relier à Richardson, au conditionnement et au gradient estimé.
**Prérequis :** fiche §3 à §7 · **Parcours :** C

Lis MML §7.1 (*Optimization Using Gradient Descent*), crayon en main, puis réponds dans ta copie, en français :
1. Comment MML note-t-il le pas ? Que dit-il d'un pas trop petit, d'un pas trop grand ?
2. Son exemple porte sur une forme quadratique $\frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$ en dimension 2. Calcule les valeurs propres de sa matrice, son conditionnement et le pas critique de la fiche. Le pas qu'il choisit est-il sous ce pas critique ?
3. Que dit sa remarque sur le conditionnement ? Quel remède propose-t-il, et quel est son lien avec le §5 de la fiche ?
4. Le §7.1.2 ajoute un terme à la mise à jour : que garde-t-elle en mémoire d'un pas à l'autre ? (N'étudie pas cette méthode : workbookIA 19 le fera.)
5. Le §7.1.3 estime le gradient sur une partie des données. Pourquoi l'estimation est-elle sans biais ? Relie-le au §7 de la fiche.
6. Relève trois expressions anglaises de la section et leur traduction dans la fiche.

### Ex M19.18 — Expliquer, sur un dessin de lignes de niveau, pourquoi un système mal conditionné converge lentement 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, avec un dessin et des mots, pourquoi le conditionnement fixe la vitesse d'une méthode itérative.
**Prérequis :** fiche §5 · **Parcours :** C, E

Un ami programme une méthode itérative pour calculer l'équilibre d'une structure de poutres ; elle converge, mais en des milliers d'itérations. Dessine pour lui les lignes de niveau de $\frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$ pour une matrice de conditionnement 1, puis 50, et réponds-lui en 6 à 10 phrases, sans formule : la forme des lignes de niveau, la direction du résidu, ce qui limite la taille du pas, ce qui se passe le long de l'axe long, pourquoi le nombre d'itérations grandit avec l'allongement, et ce qu'une mise à l'échelle des inconnues peut changer. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M19.E1 — « Que nous apprend la hessienne en un minimum ? » 💼 ★ ⏱️ 10 min
*Fiche §1 et §2 · parcours C*

« Que nous apprend la hessienne en un minimum ? »

Prépare une réponse orale de **60 secondes**. Elle doit dire ce qu'est la hessienne (les dérivées secondes, symétrique), ce qu'elle décrit (la courbure dans chaque direction, le terme d'ordre 2 de Taylor), ce que disent ses valeurs propres en un point critique (minimum, maximum, selle, cas douteux), ce qu'elles disent de la forme des lignes de niveau autour d'un minimum (des ellipses, leurs axes et leur allongement), et ce qu'elle coûte à calculer en grande dimension ($n^2$ coefficients, d'où des méthodes qui ne la forment jamais). Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M19.E2 — « Pourquoi un mauvais conditionnement ralentit-il une méthode itérative ? » 💼 ★ ⏱️ 10 min
*Fiche §5 · parcours C*

« Pourquoi un mauvais conditionnement ralentit-il une méthode itérative ? »

Prépare une réponse orale de **60 secondes** : la définition du conditionnement (pour une matrice symétrique définie positive), ce qui fixe le pas maximal, ce qui fixe la vitesse dans la direction la plus plate, l'ordre de grandeur du nombre d'itérations ($\kappa$, ou $\sqrt\kappa$ pour le gradient conjugué), ce qui ne change pas le conditionnement (multiplier par un nombre, tourner) et ce qui peut le changer (préconditionner, mettre les inconnues à l'échelle), avec un exemple concret hors de l'apprentissage automatique. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m19_hessienne_convergence/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M19.19 | La hessienne par différences centrées · `numerical_hessian` | 🔨 | ★★ | 35 | C, E |
| M19.20 | Le pas critique d'une matrice symétrique définie positive, et les itérés de Richardson · `critical_step_size, richardson_iterates` | 🔨 | ★★ | 30 | C, E |
| M19.21 | Une récurrence linéaire d'ordre d · `linear_recurrence` | 🔨 | ★ | 15 | C |
| M19.22 | `scipy.sparse.linalg.cg` : le gradient conjugué contre Richardson | 📦 | ★ | 15 | C |
| M19.23 | Prédire le nombre d'itérations de Richardson selon ω, puis vérifier | 🔮 | ★ | 10 | C, E |
| M19.24 | Le nombre d'itérations contre le conditionnement : une droite en échelle logarithmique | 🔬 | ★★ | 20 | C |
| M19.25 | Les itérés de Richardson sur les lignes de niveau d'une forme quadratique | 🎨 | ★ | 20 | C, E |
| M19.26 | Chasse à l'erreur : un pas réglé sur λmin, une hessienne non symétrique, le module d'une racine complexe | 🐛 | ★ | 25 | C, E |
| M19.27 | Un critère d'arrêt : le résidu relatif ‖b − A x‖/‖b‖ et un nombre maximal d'itérations | 🛠️ | ★ | 15 | C |
| M19.28 | Défi : le schéma saute-mouton d'un oscillateur, x_{k+1} = (2 − h²Ω²) x_k − x_{k−1}, borné si et seulement si hΩ < 2 | 🏆 | ★★★ | 30 | C |
