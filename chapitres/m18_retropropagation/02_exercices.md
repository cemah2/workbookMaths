# M18 · Différentiation automatique et calcul matriciel — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m18_retropropagation/06_mes_reponses.md` (créée par `python tools/start_chapter.py M18`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Ponts, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : la **dérivée locale** d'une arête $u \to w$ d'un graphe de calcul est $\frac{\partial w}{\partial u}$, évaluée aux valeurs de la passe avant ; la **tangente** $\dot{u}$ d'un nœud est sa dérivée par rapport à l'entrée choisie (mode direct), son **adjoint** $\bar{u} = \frac{\partial y}{\partial u}$ la dérivée de la sortie par rapport à lui (mode inverse) ; un nombre dual $a + b\varepsilon$ vérifie $\varepsilon^2 = 0$. Le gradient d'une fonction réelle d'une matrice a **la forme de la matrice**. Les angles sont en radians. Une matrice s'écrit dans le notebook comme une liste de ses **lignes**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M18.Q1 — Lire un graphe de calcul : nœuds, arêtes, ordre d'évaluation 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Deux résistances $r_1$ et $r_2$ montées en parallèle ont la résistance équivalente $R = \frac{r_1r_2}{r_1 + r_2}$, calculée en trois opérations : $u_1 = r_1 \cdot r_2$, $u_2 = r_1 + r_2$, $R = u_1 / u_2$.

1. Combien le graphe de calcul a-t-il de nœuds (entrées comprises) et d'arêtes ?
2. Quels nœuds n'ont aucun prédécesseur ? Lequel n'a aucun successeur ?
3. Combien d'arêtes partent de $r_1$ ?
4. Vrai ou faux : on peut calculer $u_2$ avant $u_1$.
5. Donne deux ordres de calcul valides des cinq nœuds.
6. Vrai ou faux : dans un programme, `x = x + 1` crée un cycle dans le graphe de calcul.

### M18.Q2 — Combien de chemins, et quelle somme ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Un graphe de calcul a l'entrée $x$, les nœuds $a$, $b$, $c$ et la sortie $y$, et ces arêtes, avec leurs dérivées locales : $x \to a$ : $2$ ; $x \to b$ : $-1$ ; $a \to c$ : $3$ ; $b \to c$ : $4$ ; $a \to y$ : $1$ ; $c \to y$ : $0{,}5$.

1. Combien de chemins vont de $x$ à $y$ ?
2. Que vaut $\frac{\partial y}{\partial x}$ ?
3. Que vaut $\frac{\partial y}{\partial a}$, l'adjoint de $a$ ?
4. Une entrée est reliée aux 2 nœuds d'un premier étage ; chaque nœud d'un étage est relié aux 2 nœuds de l'étage suivant ; il y a 10 étages, et les 2 nœuds du dernier sont reliés à la sortie. Combien de chemins vont de l'entrée à la sortie ?
5. Vrai ou faux : pour calculer $\frac{\partial y}{\partial x}$, il faut lister tous les chemins.
6. Une arête a une dérivée locale nulle : que vaut la contribution des chemins qui passent par elle ?

### M18.Q3 — Calculer avec ε² = 0 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. $(3 + 2\varepsilon)(1 - \varepsilon)$ ?
2. $(1 + \varepsilon)^5$ ?
3. $\frac{1}{2 + \varepsilon}$ ?
4. $e^{3\varepsilon}$ ?
5. $\sin(\pi + \varepsilon)$ ?
6. Vrai ou faux : si $f(2 + \varepsilon) = 7 + 12\varepsilon$, alors $f(2) = 7$ et $f'(2) = 12$.
7. Vrai ou faux : comme $\varepsilon^2 = 0$, $\varepsilon = 0$.

### M18.Q4 — Le mode inverse : dans quel ordre visiter les nœuds ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

La résistance équivalente de M18.Q1, calculée dans l'ordre $r_1, r_2, u_1, u_2, R$.

1. Dans quel ordre la passe arrière visite-t-elle les nœuds ?
2. Quel est l'adjoint de la sortie $R$ ?
3. Vrai ou faux : on peut calculer $\bar{r}_1$ avant $\bar{u}_1$.
4. Quelles valeurs de la passe avant faut-il avoir gardées pour la passe arrière ?
5. Combien de contributions l'adjoint de $r_1$ reçoit-il ?
6. Vrai ou faux : une seule passe arrière donne $\frac{\partial R}{\partial r_1}$ et $\frac{\partial R}{\partial r_2}$.

### M18.Q5 — Direct ou inverse, pour n entrées et m sorties ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. $f : \mathbb{R}^{500} \to \mathbb{R}$. Combien de passes faut-il pour son gradient en mode direct ? En mode inverse ?
2. $\mathbf{f} : \mathbb{R}^2 \to \mathbb{R}^{300}$. Combien de passes pour sa jacobienne entière dans chaque mode ?
3. $\mathbf{f} : \mathbb{R}^{50} \to \mathbb{R}^{50}$ : même nombre de passes ; quel mode demande le moins de mémoire ?
4. Vrai ou faux : le mode inverse doit garder les valeurs de la passe avant.
5. Vrai ou faux : pour une fonction de $20\,000$ variables, le gradient en mode inverse coûte environ $20\,000$ fois le calcul de la fonction.
6. Combien d'évaluations de $f : \mathbb{R}^{500} \to \mathbb{R}$ demandent les différences centrées pour tout son gradient ?

### M18.Q6 — La forme d'un gradient par rapport à une matrice 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. $f : \mathbb{R}^{3 \times 5} \to \mathbb{R}$. Quelle est la forme de $\nabla_{\mathbf{X}}f$ dans NumPy ? Combien de dérivées partielles contient-il ?
2. Quel est le gradient de $f(\mathbf{X}) = X_{23}$ (un seul coefficient) ?
3. Quel est le gradient de $f(\mathbf{X}) = \sum_{ij}X_{ij}$ ?
4. Complète : $f(\mathbf{X} + \mathbf{H}) \approx f(\mathbf{X}) + \ldots$
5. Vrai ou faux : pour une matrice carrée, $\mathbf{G}$ et $\mathbf{G}^\top$ ont la même forme, donc on peut rendre l'une ou l'autre.
6. Quelle est la forme du gradient d'une fonction réelle d'un tableau de forme $(4, 2, 3)$ ?

### M18.Q7 — Identités de trace : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

Les matrices ont les formes qui rendent chaque produit possible.

1. $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$, pour $\mathbf{A}$ de forme $(2, 3)$ et $\mathbf{B}$ de forme $(3, 2)$.
2. $\operatorname{tr}(\mathbf{A}\mathbf{B}\mathbf{C}) = \operatorname{tr}(\mathbf{B}\mathbf{A}\mathbf{C})$.
3. $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{A})\operatorname{tr}(\mathbf{B})$.
4. $\mathbf{a}^\top\mathbf{X}\mathbf{b} = \operatorname{tr}(\mathbf{b}\mathbf{a}^\top\mathbf{X})$.
5. $\sum_{ij}G_{ij}H_{ij} = \operatorname{tr}(\mathbf{G}^\top\mathbf{H})$.
6. Si $\mathrm{d}f = \operatorname{tr}(\mathbf{M}\,\mathrm{d}\mathbf{X})$, alors $\nabla_{\mathbf{X}}f = \mathbf{M}$.

### M18.Q8 — Gradient d'une moyenne, moyenne des gradients 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. $F = \frac14(f_1 + f_2 + f_3 + f_4)$, et en $\boldsymbol{\theta}$ les gradients des $f_k$ valent $(1, 0)$, $(3, 2)$, $(-1, 4)$ et $(1, -2)$. Que vaut $\nabla F(\boldsymbol{\theta})$ ?
2. Vrai ou faux : le gradient d'une somme de 100 fonctions est la somme de leurs 100 gradients.
3. $F(\mathbf{p})$ est la moyenne des carrés des distances de $\mathbf{p}$ aux points $(1, 3)$ et $(3, -1)$. Que vaut $\nabla F(0, 0)$ ?
4. Où $\nabla F$ s'annule-t-il ?
5. Vrai ou faux : pour vérifier un gradient matriciel, la direction $\mathbf{H} = \mathbf{I}$ suffit.
6. $\mathbf{X}$ a la forme $(100, 100)$. Combien d'évaluations de $f$ demande la vérification le long d'une direction par une différence centrée ? Et toutes les cases une à une ?

<a id="rappels"></a>

## 🔁 Rappels

### M18.R1 — La jacobienne d'une composée (M17) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

$\mathbf{f}(x, y) = (x - y,\ xy)$ et $g(u, v) = uv + v^2$ ; $h = g \circ \mathbf{f}$, au point $(3, 1)$.

1. $\mathbf{f}(3, 1)$ ?
2. $\mathbf{J}_{\mathbf{f}}(3, 1)$ ?
3. $\mathbf{J}_g$ au point où on l'applique ?
4. Le gradient de $h$ en $(3, 1)$, en ligne ?
5. Vérifie 4. en écrivant $h(x, y)$ et en dérivant directement.

### M18.R2 — Le gradient de wᵀAw (M09b) 🔁 ★ ⏱️ 5 min
*Fiche §7 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 1 & 3 \\ -1 & 2 \end{pmatrix}$ et $\mathbf{w} = (2, 1)$.

1. $\mathbf{w}^\top\mathbf{A}\mathbf{w}$ ?
2. $\nabla_{\mathbf{w}}(\mathbf{w}^\top\mathbf{A}\mathbf{w})$ en $\mathbf{w}$ ?
3. Vrai ou faux : ce gradient vaut $2\mathbf{A}\mathbf{w}$.
4. Le gradient de $\mathbf{w} \mapsto \mathbf{a}^\top\mathbf{w}$ pour $\mathbf{a} = (4, -3)$ ?
5. Quelle matrice symétrique donne la même forme quadratique que $\mathbf{A}$ ?

### M18.R3 — Différences centrées et choix du pas (M05a) 🔁 ★ ⏱️ 5 min
*Fiche §8 · parcours C*

1. Écris la différence centrée qui approche $f'(x)$ avec un pas $h$. De quel ordre en $h$ est son erreur de troncature ?
2. Pour $f(x) = x^3$ en 1 avec $h = 0{,}1$, que vaut-elle ? Quelle est l'erreur ?
3. En `float64`, vers quel ordre de grandeur se trouve le meilleur pas d'une différence centrée ?
4. Vrai ou faux : diminuer $h$ améliore toujours une dérivée numérique.
5. De quel ordre en $h$ est l'erreur de la différence avant $\frac{f(x + h) - f(x)}{h}$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit.

### Ex M18.1 — Le graphe de calcul d'une formule de physique, et l'ordre de ses calculs ✏️ ★ ⏱️ 15 min
**Objectif :** décomposer une formule en opérations élémentaires, dessiner son graphe de calcul et l'évaluer dans un ordre valide.
**Prérequis :** fiche §1 ; M16 · **Parcours :** C, E

Un pendule de masse $m$ (en kg), au bout d'un fil de longueur $\ell$ (en m), écarté de l'angle $\theta$ de la verticale et tournant à la vitesse angulaire $\omega$ (en rad/s), a l'énergie mécanique
$$E = \tfrac12\,m\,\ell^2\omega^2 + m\,g\,\ell\,(1 - \cos\theta), \qquad g = 10,$$
calculée en onze opérations : $u_1 = \ell^2$, $u_2 = \omega^2$, $u_3 = u_1u_2$, $u_4 = m\,u_3$, $u_5 = u_4/2$, $u_6 = \cos\theta$, $u_7 = 1 - u_6$, $u_8 = m\,\ell$, $u_9 = 10\,u_8$, $u_{10} = u_9u_7$, $E = u_5 + u_{10}$ (le carré est une opération à un argument). On prend $m = 2$, $\ell = 0{,}5$, $\theta = \frac{\pi}{3}$, $\omega = 4$.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs $[u_1, \ldots, u_{10}]$ | une liste de 10 nombres |
| b | $E$ | un nombre |
| c | le nombre d'arêtes du graphe | un entier |
| d | le nombre de nœuds qui ont plus d'un successeur | un entier |
| e | le nombre d'étapes du calcul si chaque étape fait **en même temps** toutes les opérations dont les arguments sont prêts | un entier |

Dans ta copie : dessine le graphe (les 4 entrées à gauche, $E$ à droite). Quels sont les nœuds qui ont plus d'un successeur ? Donne deux ordres de calcul valides. Pourquoi le graphe ne peut-il pas avoir de cycle ? Quel chemin fixe la réponse e) ?

### Ex M18.2 — Dériver par la somme sur les chemins : une variable qui sert deux fois ✏️ ★★ ⏱️ 20 min
**Objectif :** dériver une formule par la somme, sur les chemins de son graphe, des produits des dérivées locales.
**Prérequis :** fiche §2 ; R7 · **Parcours :** C, E

Un générateur de force électromotrice $E$ (en V) et de résistance interne $r$ (en Ω) alimente une résistance $R$ (en Ω), qui reçoit la puissance $P = \frac{E^2R}{(R + r)^2}$ (en W). On la calcule par $u_1 = E^2$, $u_2 = R + r$, $u_3 = u_2^2$, $u_4 = u_1 \cdot R$, $P = u_4 / u_3$, en $E = 12$, $R = 4$, $r = 2$.

| | Question | Réponse attendue |
|---|---|---|
| a | $P$ | un nombre |
| b | la contribution du chemin $R \to u_4 \to P$ à $\frac{\partial P}{\partial R}$ | un nombre |
| c | la contribution du chemin $R \to u_2 \to u_3 \to P$ | une fraction entre guillemets (irréductible) |
| d | $\frac{\partial P}{\partial R}$ | une fraction entre guillemets (irréductible) |
| e | $\frac{\partial P}{\partial E}$ | une fraction entre guillemets (irréductible) |
| f | $\frac{\partial P}{\partial r}$ | une fraction entre guillemets (irréductible) |
| g | la résistance $R$ qui rend $P$ maximale, $E = 12$ et $r = 2$ étant fixés | un nombre |

Dans ta copie : dessine le graphe et pose les dérivées locales sur ses arêtes. Pourquoi $R$ a-t-il deux chemins vers $P$, et $E$ un seul ? Vérifie d) en dérivant $P(R) = \frac{144R}{(R + 2)^2}$ directement. Pour g), écris $\frac{\partial P}{\partial R}$ pour un $R$ quelconque ; que dit le résultat de la meilleure résistance à brancher sur un générateur ?

### Ex M18.3 — Le mode direct à la main : des nombres duaux sur une fonction de deux variables ✏️ ★★ ⏱️ 20 min
**Objectif :** dériver une fonction de deux variables en mode direct, avec des nombres duaux, une passe par graine.
**Prérequis :** fiche §3 · **Parcours :** C, E

$f(x, y) = x^2y + \ln(x + y)$, au point $(2, -1)$. Chaque réponse est un nombre dual $a + b\varepsilon$, à écrire comme la liste `[a, b]`.

| | Question | Réponse attendue |
|---|---|---|
| a | $(2 + \varepsilon)^2$ | une liste de 2 nombres |
| b | $x^2y$ avec la graine sur $x$ : $x = 2 + \varepsilon$, $y = -1$ | une liste de 2 nombres |
| c | $\ln(x + y)$ avec la même graine | une liste de 2 nombres |
| d | $f(x, y)$ avec la graine sur $x$ | une liste de 2 nombres |
| e | $f(x, y)$ avec la graine sur $y$ : $x = 2$, $y = -1 + \varepsilon$ | une liste de 2 nombres |
| f | $f(x, y)$ avec $x = 2 + \varepsilon$ et $y = -1 + 2\varepsilon$ | une liste de 2 nombres |
| g | $\frac{3 + 2\varepsilon}{1 - \varepsilon}$ | une liste de 2 nombres |

Dans ta copie : écris le gradient de $f$ en $(2, -1)$ et vérifie-le en dérivant directement. Combien de passes a-t-il fallu ? Que représente la partie en $\varepsilon$ de f) (relie-la à M17 §5) ? Pour g), retrouve le résultat par la règle du quotient de la fiche, puis en multipliant le haut et le bas par $1 + \varepsilon$.

### Ex M18.4 — Le mode inverse à la main : les adjoints d'un graphe de six nœuds ✏️ ★★ ⏱️ 20 min
**Objectif :** faire une passe avant, puis une passe arrière, et accumuler les adjoints d'un nœud qui sert deux fois.
**Prérequis :** fiche §4 · **Parcours :** C, E

$f(p, q) = pq\sqrt{pq + q}$, calculée par $u_1 = p \cdot q$, $u_2 = u_1 + q$, $u_3 = \sqrt{u_2}$, $f = u_1 \cdot u_3$, au point $(p, q) = (1, 2)$. Le graphe a six nœuds : $p$, $q$, $u_1$, $u_2$, $u_3$, $f$.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs de la passe avant $[u_1, u_2, u_3, f]$ | une liste de 4 nombres |
| b | les adjoints $[\bar{u}_3, \bar{u}_2]$ | une liste de 2 nombres |
| c | l'adjoint $\bar{u}_1$ | un nombre |
| d | le gradient $[\bar{p}, \bar{q}]$ | une liste de 2 nombres |
| e | le changement de $f$ prévu par le gradient quand $(p, q)$ passe à $(1{,}02 ;\ 1{,}99)$ | un nombre |
| f | le vrai changement $f(1{,}02 ;\ 1{,}99) - f(1, 2)$ | un nombre (4 décimales) |

Dans ta copie : dessine le graphe avec les valeurs et les adjoints. Quels nœuds reçoivent deux contributions, et pourquoi ? Vérifie d) en dérivant $f$ directement. Pourquoi e) et f) sont-ils proches ?

### Ex M18.5 — Le même gradient par les deux modes, et le compte des opérations ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un même gradient en mode direct et en mode inverse, et compter ce que coûte chacun.
**Prérequis :** fiche §3, §4 et §5 · **Parcours :** C, E

$f(x_1, x_2, x_3) = (x_1 + x_2)(x_2 + x_3)(x_3 + x_1)$, calculée par $u_1 = x_1 + x_2$, $u_2 = x_2 + x_3$, $u_3 = x_3 + x_1$, $u_4 = u_1u_2$, $f = u_4u_3$, au point $(1, 2, 3)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $f(1, 2, 3)$ | un nombre |
| b | les tangentes $\dot{f}$ des trois passes directes, avec les graines $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$ | une liste de 3 nombres |
| c | les adjoints $[\bar{u}_4, \bar{u}_3]$ | une liste de 2 nombres |
| d | les adjoints $[\bar{u}_1, \bar{u}_2]$ | une liste de 2 nombres |
| e | le gradient par la passe arrière, $[\bar{x}_1, \bar{x}_2, \bar{x}_3]$ | une liste de 3 nombres |
| f | le nombre de passes pour le gradient en mode direct, puis en mode inverse (sans compter la passe avant) | une liste de 2 entiers |
| g | le nombre de produits « dérivée locale × tangente » de toutes les passes directes, puis de produits « adjoint × dérivée locale » de la passe arrière | une liste de 2 entiers |

Dans ta copie : écris les dérivées locales des dix arêtes. Pour g), combien de fois chaque arête sert-elle dans chaque mode ? Que deviendraient ces deux nombres pour une fonction de 100 variables calculée avec 1 000 arêtes ?

### Ex M18.6 — Le gradient de aᵀXb, de la forme de X ✏️ ★ ⏱️ 15 min
**Objectif :** calculer le gradient d'une forme bilinéaire par rapport à une matrice, coordonnée par coordonnée, et le ranger comme la matrice.
**Prérequis :** fiche §6 · **Parcours :** C, E

$\mathbf{a} = (1, -2, 3)$, $\mathbf{b} = (2 ;\ 0{,}5)$, $\mathbf{X} = \begin{pmatrix} 1 & 0 \\ 2 & -1 \\ 0 & 4 \end{pmatrix}$, et $f(\mathbf{X}) = \mathbf{a}^\top\mathbf{X}\mathbf{b} = \sum_{ij}a_iX_{ij}b_j$.

| | Question | Réponse attendue |
|---|---|---|
| a | $f(\mathbf{X})$ | un nombre |
| b | $\frac{\partial f}{\partial X_{21}}$ | un nombre |
| c | $\nabla_{\mathbf{X}}f$ | une matrice |
| d | sa forme | une liste de 2 entiers |
| e | le changement prévu par le gradient pour le déplacement $\mathbf{H} = \begin{pmatrix} 0 & 0 \\ 0 & 0{,}1 \\ -0{,}2 & 0 \end{pmatrix}$ | un nombre |
| f | $f(\mathbf{X} + \mathbf{H})$ | un nombre |

Dans ta copie : écris $\frac{\partial f}{\partial X_{ij}}$ en général et reconnais $\mathbf{a}\mathbf{b}^\top$. Pourquoi le gradient ne dépend-il pas de $\mathbf{X}$ ? Pourquoi la prévision e) est-elle exacte ici ?

### Ex M18.7 — Les gradients de tr(AX) et de tr(XᵀAX), coordonnée par coordonnée ✏️ ★★ ⏱️ 20 min
**Objectif :** établir les gradients de deux traces en écrivant les sommes, puis les vérifier par les identités de la fiche.
**Prérequis :** fiche §7 ; M12c · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$, $\mathbf{X} = \begin{pmatrix} 1 & 2 \\ 0 & -1 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{tr}(\mathbf{A}\mathbf{X})$ | un nombre |
| b | $\nabla_{\mathbf{X}}\operatorname{tr}(\mathbf{A}\mathbf{X})$ | une matrice |
| c | $\frac{\partial}{\partial X_{12}}\operatorname{tr}(\mathbf{A}\mathbf{X})$ | un nombre |
| d | $\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X})$ | un nombre |
| e | $\nabla_{\mathbf{X}}\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X})$ | une matrice |
| f | la dérivée en 0 de $s \mapsto \operatorname{tr}\big((\mathbf{X} + s\mathbf{H})^\top\mathbf{A}(\mathbf{X} + s\mathbf{H})\big)$ pour $\mathbf{H} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | un nombre |

Dans ta copie : écris $\operatorname{tr}(\mathbf{A}\mathbf{X}) = \sum_{i,j}A_{ji}X_{ij}$ et déduis-en b) ; écris $\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X}) = \sum_k\sum_{i,j}X_{ik}A_{ij}X_{jk}$ et dérive par rapport à $X_{pq}$. Pourquoi $2\mathbf{A}\mathbf{X}$ serait-il faux ici ? Que devient e) quand $\mathbf{X}$ n'a qu'une colonne (M09b) ?

### Ex M18.8 — Le gradient de log det X sur une matrice 2 × 2, à la main puis par la formule ✏️ ★★ ⏱️ 20 min
**Objectif :** dériver le déterminant et son logarithme coordonnée par coordonnée, puis retrouver la formule $\mathbf{X}^{-\top}$.
**Prérequis :** fiche §6 et §7 ; M09a · **Parcours :** C

$\mathbf{X} = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$, et $\ln$ est le logarithme népérien (le « log det » de MML et de NumPy).

| | Question | Réponse attendue |
|---|---|---|
| a | $\det\mathbf{X}$ | un nombre |
| b | $\nabla_{\mathbf{X}}\det\mathbf{X}$, coordonnée par coordonnée | une matrice |
| c | $\nabla_{\mathbf{X}}\ln\det\mathbf{X}$ | une matrice |
| d | $\mathbf{X}^{-1}$ | une matrice |
| e | la dérivée en 0 de $s \mapsto \ln\det(\mathbf{X} + s\mathbf{H})$ pour $\mathbf{H} = \begin{pmatrix} 1 & 2 \\ 0 & -1 \end{pmatrix}$ | un nombre |
| f | $\ln\det(\mathbf{X} + 0{,}01\,\mathbf{H}) - \ln\det\mathbf{X}$ | un nombre (5 décimales) |

Dans ta copie : comparer c) et d) : lequel est la transposée de l'autre, et pourquoi ce n'est pas un hasard ? Reconnais la comatrice dans b). Pourquoi f) est-il proche de $0{,}01 \times$ e) ?

### Ex M18.9 — Le gradient d'une moyenne de distances : le point qui minimise la somme des distances à des villes ✏️ ★★ ⏱️ 15 min
**Objectif :** dériver une moyenne de distances par la moyenne de leurs gradients, et reconnaître son minimum là où ces vecteurs unitaires s'équilibrent.
**Prérequis :** fiche §8 ; M07 · **Parcours :** C, E

Quatre villes ont pour coordonnées (en km) $A = (0, 0)$, $B = (8, 0)$, $C = (6, 6)$ et $D = (0, 4)$. On cherche où construire un entrepôt $\mathbf{p}$ pour minimiser la distance moyenne aux villes, $F(\mathbf{p}) = \frac14\sum_k\lVert\mathbf{p} - \mathbf{x}_k\rVert$.

| | Question | Réponse attendue |
|---|---|---|
| a | $F(3, 1)$ | un nombre (3 décimales) |
| b | le gradient de $\mathbf{p} \mapsto \lVert\mathbf{p} - A\rVert$ en $(3, 1)$ | une liste de 2 nombres (4 décimales) |
| c | $\nabla F(3, 1)$ | une liste de 2 nombres (3 décimales) |
| d | $\nabla F$ au point d'intersection des diagonales $[AC]$ et $[BD]$ | une liste de 2 nombres |
| e | la valeur minimale de $F$ | un nombre (4 décimales) |
| f | de combien la distance moyenne au centroïde des quatre villes dépasse-t-elle ce minimum ? | un nombre (3 décimales) |

Dans ta copie : trouve le point d'intersection des diagonales. Pourquoi les gradients des distances à $A$ et à $C$ s'y annulent-ils deux à deux, comme ceux de $B$ et $D$ ? Pourquoi ce point est-il le minimum, sachant que $F$ est convexe (on l'admet) ? Pourquoi le centroïde, minimum de la moyenne des **carrés** des distances (fiche §8), ne convient-il pas ici ?

### Ex M18.10 — La différentielle d'une fonction de matrice, df = tr(Gᵀ dX), et le gradient G qu'on y lit ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des différentielles avec la règle du produit, et y lire des gradients qui demandent une transposée.
**Prérequis :** fiche §6 et §7 · **Parcours :** C

$\mathbf{X} = \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix}$, $\mathbf{a} = (1, 0)$, $\mathbf{b} = (0, 1)$. On étudie $f(\mathbf{X}) = \operatorname{tr}(\mathbf{X}^2)$ et $g(\mathbf{X}) = \mathbf{a}^\top\mathbf{X}^2\mathbf{b}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $f(\mathbf{X})$ | un nombre |
| b | $\nabla_{\mathbf{X}}f$ | une matrice |
| c | $\frac{\partial f}{\partial X_{12}}$ | un nombre |
| d | $g(\mathbf{X})$ | un nombre |
| e | $\nabla_{\mathbf{X}}g$ | une matrice |
| f | la dérivée en 0 de $s \mapsto f(\mathbf{X} + s\mathbf{H})$ pour $\mathbf{H} = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix}$ | un nombre |

Dans ta copie : montre que $\mathrm{d}f = 2\operatorname{tr}(\mathbf{X}\,\mathrm{d}\mathbf{X})$ (règle du produit, puis cyclicité de la trace) et lis $\nabla f = 2\mathbf{X}^\top$. Vérifie c) en écrivant $\operatorname{tr}(\mathbf{X}^2) = \sum_{i,j}X_{ij}X_{ji}$. Montre que $\mathrm{d}g = \operatorname{tr}(\mathbf{X}\mathbf{b}\mathbf{a}^\top\mathrm{d}\mathbf{X}) + \operatorname{tr}(\mathbf{b}\mathbf{a}^\top\mathbf{X}\,\mathrm{d}\mathbf{X})$ et déduis-en $\nabla g = \mathbf{a}\mathbf{b}^\top\mathbf{X}^\top + \mathbf{X}^\top\mathbf{a}\mathbf{b}^\top$. Vérifie e) sur $g(\mathbf{X}) = (\mathbf{X}^2)_{12} = X_{11}X_{12} + X_{12}X_{22}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M18.11 — La règle de la chaîne sur un graphe sans cycle : la somme sur les chemins, nœud par nœud dans l'ordre de la numérotation ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule de la somme sur les chemins, par récurrence dans l'ordre du calcul.
**Prérequis :** fiche §1 et §2 ; M16, M17 ; R4 (récurrence) · **Parcours :** C, E

Un calcul a les nœuds $u_1, \ldots, u_N$, numérotés dans un ordre de calcul : $u_1, \ldots, u_n$ sont les entrées, et chaque $u_k$ ($k > n$) vaut $\varphi_k$ de ses prédécesseurs, qui ont tous un numéro plus petit ; les $\varphi_k$ sont dérivables, et $y = u_N$. On fixe une entrée $x = u_i$ et on note $\dot{u}_k$ la dérivée de $u_k$ par rapport à $x$, les autres entrées restant fixes. $D_{jk} = \frac{\partial\varphi_k}{\partial u_j}$ est la dérivée locale de l'arête $u_j \to u_k$ (et $D_{jk} = 0$ sans arête).

1. Montre que $\dot{u}_k = \sum_{j < k}D_{jk}\,\dot{u}_j$ pour $k > n$ (règle de la chaîne de M17), et donne $\dot{u}_j$ pour les entrées.
2. On note $S_k$ la somme, sur les chemins de $x$ à $u_k$, des produits des dérivées locales (avec la convention : le chemin vide de $x$ à lui-même compte pour 1). Montre par récurrence sur $k$ que $\dot{u}_k = S_k$. Pour l'hérédité, classe les chemins de $x$ à $u_k$ selon leur **dernière** arête.
3. Conclus pour $\frac{\partial y}{\partial x}$.
4. Où la numérotation sert-elle dans la récurrence ? Que se passerait-il avec un cycle ?
5. Écris le vecteur $\dot{\mathbf{u}} = (\dot{u}_1, \ldots, \dot{u}_N)$ comme solution de $\dot{\mathbf{u}} = \mathbf{e}_i + \mathbf{D}^\top\dot{\mathbf{u}}$, et déduis-en que $\frac{\partial y}{\partial x_i}$ est le coefficient $(i, N)$ de $(\mathbf{I} - \mathbf{D})^{-1}$ (M16 §4).

### Ex M18.12 — Les nombres duaux calculent la dérivée : f(a + bε) = f(a) + b f′(a) ε, pour les sommes, les produits et les composées ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que l'arithmétique des nombres duaux suit les règles de dérivation, et que la partie en ε d'un calcul est la dérivée.
**Prérequis :** fiche §3 ; R7 · **Parcours :** C, E

On dit qu'une fonction $f$ (dérivable sur un intervalle) est **compatible** si $f(a + b\varepsilon) = f(a) + b\,f'(a)\,\varepsilon$ pour tous les réels $a$ (de l'intervalle) et $b$. On pose $g(a + b\varepsilon) = g(a) + g'(a)\,b\,\varepsilon$ pour $g = \exp$, $\ln$, $\sin$, $\cos$ : ces fonctions sont compatibles par définition.

1. Montre que $(a + b\varepsilon)(c + d\varepsilon) = ac + (ad + bc)\,\varepsilon$, et que $\frac{a + b\varepsilon}{c + d\varepsilon} = \frac{a}{c} + \frac{bc - ad}{c^2}\,\varepsilon$ pour $c \ne 0$ (vérifie en multipliant par $c + d\varepsilon$).
2. Montre que $x \mapsto x$ et les constantes sont compatibles ; puis que, si $f$ et $g$ sont compatibles, $f + g$, $fg$ et $f/g$ (là où $g \ne 0$) le sont.
3. Montre que, si $f$ et $g$ sont compatibles, $g \circ f$ l'est.
4. Conclus : pour toute fonction $f$ construite à partir de $x$ et de constantes par sommes, produits, quotients et les quatre fonctions ci-dessus, $f(a + \varepsilon) = f(a) + f'(a)\,\varepsilon$.
5. Montre directement, avec la formule du binôme, que $(a + b\varepsilon)^n = a^n + n\,a^{n-1}b\,\varepsilon$ pour tout entier $n \ge 1$.
6. Pourquoi la définition $e^{a + b\varepsilon} = e^a + e^ab\,\varepsilon$ est-elle naturelle ? (Écris $e^{a + b\varepsilon} = e^ae^{b\varepsilon}$ et utilise la série de l'exponentielle.)

### Ex M18.13 — Le mode inverse calcule tout le gradient en un passage : l'adjoint d'un nœud est la somme, sur ses successeurs, des adjoints fois les dérivées locales ∂ ★★★ ⏱️ 20 min
**Objectif :** démontrer la formule des adjoints, et en tirer qu'une seule passe arrière donne tout le gradient.
**Prérequis :** fiche §4 ; Ex M18.11 · **Parcours :** C

Mêmes notations qu'en M18.11. Pour chaque nœud $u_j$, on note $A_j$ la somme, sur les chemins de $u_j$ à $y = u_N$, des produits des dérivées locales ($A_N = 1$, le chemin vide).

1. Montre que $A_j = \sum_{k > j}D_{jk}\,A_k$, en classant les chemins de $u_j$ à $y$ selon leur **première** arête.
2. Montre qu'en calculant les $A_j$ pour $j = N, N - 1, \ldots, 1$, chaque $A_k$ du membre de droite est déjà connu.
3. Déduis de M18.11 que $A_i = \frac{\partial y}{\partial x_i}$ pour chaque entrée : une seule passe arrière donne tout le gradient.
4. Montre que, pour un nœud intermédiaire, $A_j$ est la dérivée de $y$ par rapport à $u_j$ quand on considère $u_j$ comme une entrée libre et qu'on recalcule tout ce qui vient après lui : c'est l'adjoint $\bar{u}_j$.
5. Écris $\mathbf{A} = (A_1, \ldots, A_N)$ comme solution de $\mathbf{A} = \mathbf{e}_N + \mathbf{D}\mathbf{A}$. Quelle **colonne** de $(\mathbf{I} - \mathbf{D})^{-1}$ obtient-on ? Quelle **ligne** une passe directe donne-t-elle (M18.11) ?
6. Combien de fois chaque arête sert-elle dans la passe arrière ? Quelles valeurs de la passe avant faut-il avoir gardées ?

### Ex M18.14 — ∇ log det X = X⁻ᵀ, par le développement du déterminant selon une ligne ∂ ★★★ ⏱️ 20 min
**Objectif :** démontrer que le gradient du déterminant est la comatrice, et en déduire le gradient de $\ln\det$.
**Prérequis :** fiche §7 ; M12c · **Parcours :** C

$\mathbf{X}$ est une matrice carrée $n \times n$ ; $C_{ij}$ est son cofacteur $(i, j)$, et $\operatorname{com}(\mathbf{X})$ la matrice des cofacteurs. On admet le développement selon une ligne, $\det\mathbf{X} = \sum_jX_{ij}C_{ij}$ pour chaque $i$, et l'identité $\mathbf{X}\operatorname{com}(\mathbf{X})^\top = \det\mathbf{X}\;\mathbf{I}$ (fiche §7).

1. Pourquoi $C_{ij}$ ne dépend-il d'aucun coefficient de la ligne $i$ de $\mathbf{X}$ ?
2. Déduis-en $\frac{\partial\det\mathbf{X}}{\partial X_{ij}} = C_{ij}$, c'est-à-dire $\nabla_{\mathbf{X}}\det\mathbf{X} = \operatorname{com}(\mathbf{X})$.
3. Pour $\det\mathbf{X} \ne 0$, montre que $\operatorname{com}(\mathbf{X}) = \det\mathbf{X}\;\mathbf{X}^{-\top}$.
4. Déduis-en $\nabla_{\mathbf{X}}\ln\det\mathbf{X} = \mathbf{X}^{-\top}$ pour $\det\mathbf{X} > 0$. Que dire de $\ln\lvert\det\mathbf{X}\rvert$ quand $\det\mathbf{X} < 0$ ?
5. Vérifie 2. et 4. sur $\mathbf{X} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
6. Déduis-en la différentielle $\mathrm{d}(\det\mathbf{X}) = \det\mathbf{X}\,\operatorname{tr}(\mathbf{X}^{-1}\mathrm{d}\mathbf{X})$.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M18.15 — Pont : workbookIA 18 programme le mode inverse ; pour une simulation de ℝ²⁰⁰⁰ dans ℝ³, combien de passages dans chaque mode ? 🔗 ★ ⏱️ 15 min
**Objectif :** choisir le mode de différentiation d'un calcul d'après ses nombres d'entrées et de sorties, et chiffrer le temps et la mémoire.
**Prérequis :** fiche §5 · **Parcours :** C, E

Une simulation de la qualité de l'air d'une ville prend 2 000 nombres en entrée (les émissions de 2 000 rues) et rend 3 nombres (les concentrations moyennes de trois polluants). Elle fait $10^6$ opérations élémentaires.

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de la jacobienne de la simulation | une liste de 2 entiers |
| b | le nombre de passages pour la jacobienne entière, en mode direct puis en mode inverse | une liste de 2 entiers |
| c | le nombre de passages pour le gradient d'un seul polluant, en mode direct puis en mode inverse | une liste de 2 entiers |
| d | le nombre d'évaluations de la simulation pour la jacobienne entière par différences centrées | un entier |
| e | en supposant qu'un passage coûte autant dans les deux modes, combien de fois le mode direct est-il plus long que le mode inverse pour la jacobienne entière ? | un nombre (1 décimale) |
| f | la mémoire de la passe avant gardée par le mode inverse, si chaque opération y laisse un flottant de 8 octets, en mégaoctets (1 Mo = $10^6$ octets) | un nombre |

Dans ta copie : quel mode choisirais-tu pour cette simulation, et pourquoi ? Le chapitre 18 de workbookIA dérive un calcul qui a un très grand nombre d'entrées et une seule sortie : quel mode lui faut-il, et que lui coûte-t-il en mémoire ?

### Ex M18.16 — Pont : de la convention de MML (gradient en ligne) à celle de NumPy et des bibliothèques de deep learning 🔗 ★ ⏱️ 15 min
**Objectif :** passer d'une convention de gradient à l'autre, pour un vecteur puis pour une matrice.
**Prérequis :** fiche §6 ; M17 §4 · **Parcours :** C

$f(\mathbf{x}) = \mathbf{x}^\top\mathbf{A}\mathbf{x} + \mathbf{b}^\top\mathbf{x}$ avec $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$, $\mathbf{b} = (1, -1)$, au point $\mathbf{x} = (1, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le gradient de $f$ dans la convention de MML (une ligne) | une matrice d'une ligne : `[[a, b]]` |
| b | la forme de ce gradient dans NumPy, pour `x` de forme `(2,)` | une liste d'un entier |
| c | pour une fonction réelle d'une matrice de forme $(3, 4)$ : la forme de son gradient dans NumPy, puis celle de sa jacobienne si l'on aplatit la matrice en un vecteur de 12 coordonnées | une liste de 2 listes de 2 entiers |
| d | le point $\mathbf{x} - \eta\,\nabla f(\mathbf{x})$ après un pas de descente de gradient, avec $\eta = 0{,}1$ | une liste de 2 nombres |
| e | la forme du gradient d'une fonction réelle d'un tableau de forme $(5, 3, 2)$ dans NumPy | une liste de 3 entiers |

Dans ta copie : écris le gradient de a) en ligne, $\mathbf{x}^\top(\mathbf{A} + \mathbf{A}^\top) + \mathbf{b}^\top$, puis en colonne. Pourquoi faut-il transposer la ligne de MML avant de faire le pas d) ? Dans le chapitre 18 de workbookIA, chaque gradient a la forme de son tableau : quelle règle simple vérifie-t-on alors sur chaque formule ?

### Ex M18.17 — MML §5.4 et §5.5 : gradients par rapport à des matrices et identités utiles, en anglais 📖 ★★ ⏱️ 40 min
**Objectif :** lire deux sections de MML en anglais, et relier leurs notations et leurs identités à celles de la fiche.
**Prérequis :** fiche §6 et §7 · **Parcours :** C

Lis MML §5.4 (*Gradients of Matrices*) et §5.5 (*Useful Identities for Computing Gradients*), crayon en main, puis réponds dans ta copie, en français :
1. Quelle forme MML donne-t-il à la dérivée d'une matrice $m \times n$ par rapport à une matrice $p \times q$ ? Quelles sont les deux façons de la calculer qu'il propose ?
2. Comment MML range-t-il le gradient d'une fonction réelle d'une matrice dans ses identités du §5.5 ? Est-ce la convention de la fiche (§6) ?
3. Retrouve dans le §5.5 les identités de la fiche (§7) : lesquelles y sont, et sous quelle forme ? Y en a-t-il une que la fiche n'a pas démontrée ? Démontre-la avec les règles de la différentielle.
4. Refais à la main un exemple du §5.4 avec tes propres nombres (des matrices $2 \times 2$), et vérifie-le dans le notebook.
5. Relève trois expressions anglaises de ces sections et leur traduction dans la fiche.

### Ex M18.18 — MML §5.6 : rétropropagation et différentiation automatique, en anglais 📖 ★★ ⏱️ 35 min
**Objectif :** lire la section de MML sur la différentiation automatique, et refaire son exemple avec un graphe de calcul.
**Prérequis :** fiche §1 à §5 · **Parcours :** C

Lis MML §5.6 (*Backpropagation and Automatic Differentiation*), crayon en main ; tu peux survoler le §5.6.1 (un réseau profond, que workbookIA 18 traitera). Puis réponds dans ta copie, en français :
1. Comment MML appelle-t-il les nœuds intermédiaires d'un calcul ? Quel graphe dessine-t-il pour son exemple ?
2. Quels noms MML donne-t-il aux deux modes ? Dans quel sens chacun parcourt-il le graphe ?
3. Refais l'exemple du §5.6.2 en un point de ton choix : écris le graphe, ses dérivées locales, puis la dérivée par la somme sur les chemins et par les adjoints. Vérifie-la en dérivant la formule directement.
4. D'après la section, que coûte le calcul du gradient, comparé au calcul de la fonction ? Relie-le au §5 de la fiche.
5. Refais la même dérivée en mode direct avec un nombre dual (fiche §3), au même point : retrouve-t-on les mêmes nombres, nœud par nœud ?
6. Relève trois expressions anglaises de la section et leur traduction dans la fiche.

### Ex M18.19 — Expliquer le mode inverse à quelqu'un qui connaît la règle de la chaîne en une variable 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, avec des mots, pourquoi le mode inverse donne toutes les dérivées en une seule passe.
**Prérequis :** fiche §4 · **Parcours :** C, E

Une amie a fait la règle de la chaîne en terminale : $(g \circ f)'(x) = g'(f(x))\,f'(x)$. Elle demande comment un ordinateur obtient d'un coup les dérivées d'un résultat par rapport à des milliers de données d'entrée. Réponds-lui en 6 à 10 phrases, sans formule, en t'appuyant sur une image concrète (une recette, un réseau de rivières, une chaîne de fournisseurs…) : ce que mesure l'adjoint d'une étape (« de combien le résultat bouge si cette étape bouge un peu »), pourquoi on part de la fin, pourquoi une étape qui sert à plusieurs suivantes additionne ce qu'elle reçoit, pourquoi il faut avoir gardé les valeurs de l'aller, et pourquoi une seule remontée suffit pour toutes les entrées. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M18.E1 — « Différentiation automatique, symbolique ou numérique : quelles différences ? » 💼 ★ ⏱️ 10 min
*Fiche §3, §4 et §5 · parcours C*

« Différentiation automatique, symbolique ou numérique : quelles différences ? »

Prépare une réponse orale de **60 secondes**. Elle doit dire ce que fait chacune (la formule de la dérivée par des règles de réécriture, comme SymPy ; une approximation par des différences finies ; les règles de dérivation appliquées aux nombres, opération par opération, pendant le calcul), ce que chacune rend (une expression, un nombre approché, un nombre exact aux arrondis près), leurs défauts (expressions qui gonflent ; erreur qui dépend du pas $h$ et $2n$ évaluations pour un gradient ; mémoire du mode inverse), et pourquoi les bibliothèques de deep learning choisissent la différentiation automatique en mode inverse. Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M18.E2 — « Quand le mode direct est-il préférable au mode inverse ? » 💼 ★ ⏱️ 10 min
*Fiche §5 · parcours C*

« Quand le mode direct est-il préférable au mode inverse ? »

Prépare une réponse orale de **60 secondes** : ce que donne un passage de chaque mode (une colonne ou une ligne de la jacobienne), la règle de choix selon les nombres d'entrées et de sorties, un exemple concret de chaque cas hors des réseaux de neurones, la question de la mémoire, et le cas d'un produit jacobienne-vecteur (une seule direction). Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m18_retropropagation/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M18.20 | Les nombres duaux : la classe `Dual`, et la dérivée d'une fonction d'une variable · `Dual, dual_derivative` | 🔨 | ★★ | 30 | C, E |
| M18.21 | Le gradient en mode direct : n passages avec des nombres duaux · `forward_gradient` | 🔨 | ★ | 20 | C |
| M18.22 | Lire le gradient dans la différentielle : G[i, j] = df(E_ij), de la forme de la variable · `gradient_from_differential` | 🔨 | ★ | 15 | C, E |
| M18.23 | SymPy : dériver une fonction de matrice symbolique, et comparer aux identités | 📦 | ★ | 15 | C |
| M18.24 | Prédire le nombre d'opérations de chaque mode, puis le compter | 🔮 | ★ | 10 | C, E |
| M18.25 | Différences finies contre nombres duaux : l'erreur selon le pas h | 🔬 | ★★ | 20 | C |
| M18.26 | Dessiner un graphe de calcul, avec les dérivées locales sur les arêtes et les adjoints sur les nœuds | 🎨 | ★ | 20 | C |
| M18.27 | Chasse à l'erreur : un gradient transposé, un adjoint compté sur un seul chemin, un pas h trop petit | 🐛 | ★ | 15 | C, E |
| M18.28 | Tester une classe par ses propriétés : distributivité et dérivées connues des nombres duaux | 🛠️ | ★ | 15 | C |
| M18.29 | Défi : dériver une boucle, la méthode de Newton pour √a, en mode direct | 🏆 | ★★★ | 30 | C |
