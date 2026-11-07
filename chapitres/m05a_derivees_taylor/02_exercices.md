# M05a · Dérivées, Taylor et calcul numérique — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m05a_derivees_taylor/06_mes_reponses.md` (créée par `python tools/start_chapter.py M05a`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, estimation et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Garde les valeurs exactes (fractions, $e$, $\sqrt{10}$) jusqu'au bout, et n'arrondis qu'à la fin. Pour chaque approximation, écris aussi son erreur : c'est le fil du chapitre.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M05a.Q1 — Le signe de la dérivée seconde 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Si $f'' > 0$ sur un intervalle, comment varie $f'$ ? Quelle forme a la courbe ?
2. Vrai ou faux : une fonction convexe est croissante.
3. $f(x) = -\ln x$ sur $]0, +\infty[$ : convexe ou concave ?
4. Vrai ou faux : si $f''(2) = 0$, alors 2 est un point d'inflexion de $f$.
5. Vrai ou faux : la somme de deux fonctions convexes est convexe.
6. Sur quel intervalle la fonction cube, $x \mapsto x^3$, est-elle concave ?

### M05a.Q2 — Local ou global ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. $f$ est continue sur $[0, 3]$ et $f'(x) > 0$ pour tout $x$ de $]0, 3[$. Où est son maximum global ?
2. $f(x) = x^2 + 2x$ sur $[0, 5]$ : $f'$ s'annule en $-1$. Où est le minimum global de $f$ sur $[0, 5]$, et que vaut-il ?
3. Vrai ou faux : un maximum local est un maximum global.
4. $f$ est convexe sur $\mathbb{R}$ et $f'(c) = 0$. Que peut-on dire de $c$ ?
5. $f(x) = e^x$ a-t-elle un minimum global sur $\mathbb{R}$ ?
6. $f'(c) = 0$ et $f''(c) = 0$ : que peut-on conclure sur $c$ ?

### M05a.Q3 — Taylor : quel ordre, quelle précision ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Que représente géométriquement le polynôme de Taylor d'ordre 1 de $f$ en $a$ ?
2. Écris le polynôme de Taylor d'ordre 2 de $e^x$ en 0.
3. Quel est le coefficient de $x^3$ dans le polynôme de Taylor de $\sin$ en 0 ?
4. Vrai ou faux : $P_n$ et $f$ ont en $a$ la même valeur et les mêmes dérivées jusqu'à l'ordre $n$.
5. On sait que $|f'''| \le 2$ entre 0 et 0,1. Majore $|f(0{,}1) - P_2(0{,}1)|$, où $P_2$ est le polynôme de Taylor d'ordre 2 de $f$ en 0.
6. Vrai ou faux : en ajoutant assez de termes de la série de $\ln(1 + x)$ en 0, on obtient $\ln 3$ pour $x = 2$.

### M05a.Q4 — Newton converge-t-il ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C*

1. Fais un pas de Newton pour $f(x) = x^2 - 9$ depuis $x_0 = 4$.
2. Que se passe-t-il si $f'(x_k) = 0$ ?
3. Vrai ou faux : si $f$ a une racine, la méthode de Newton y converge depuis n'importe quel point de départ.
4. Près d'une racine simple, l'erreur vaut $10^{-2}$ à un pas. Quel ordre de grandeur attends-tu au pas suivant, puis au suivant (avec une constante de l'ordre de 1) ?
5. Pour $f(x) = x^3 - 2x + 2$ depuis $x_0 = 0$, que fait la suite ?
6. Pourquoi Newton est-il lent pour $f(x) = (x - 1)^2$ ?

### M05a.Q5 — Différence avant ou centrée ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Quel est l'ordre de la différence avant ? De la différence centrée ?
2. On divise $h$ par 10 : par combien l'erreur de troncature de la différence centrée est-elle divisée, à peu près ?
3. Pourquoi la différence centrée est-elle plus précise ? Quels termes du développement de Taylor disparaissent ?
4. Vrai ou faux : pour $f(x) = x^2$, la différence centrée donne exactement $f'(x)$, quel que soit $h$.
5. Écris la combinaison de Richardson de $D(h)$ et $D(h/2)$. Quel est son ordre ?
6. Vrai ou faux : la différence avant est exacte pour une fonction affine.

### M05a.Q6 — Les flottants : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. L'epsilon machine est le plus petit flottant positif.
2. $2^{53} + 1$ est exactement représentable en `float64`.
3. 0,5 est exactement représentable en `float64`.
4. L'addition des flottants est associative : $(a + b) + c = a + (b + c)$ toujours.
5. Un `float32` garde environ 7 chiffres significatifs.
6. Une seule opération en `float64` commet une erreur relative d'au plus $1{,}1 \times 10^{-16}$ environ.

### M05a.Q7 — Overflow, underflow, log-sum-exp 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. Que fait `math.exp(720)` ? Et `np.exp(720)` ?
2. Que vaut $\text{LSE}(3, 3)$ ?
3. Entre quelles valeurs se trouve $\text{LSE}(v_1, \ldots, v_n)$ ?
4. Pourquoi soustrait-on le **maximum** des scores, et pas leur minimum ?
5. Que vaut $\text{softmax}(\mathbf{v} + c)$, où $c$ est ajouté à chaque score ?
6. Écris le log-softmax de $v_i$ avec le log-sum-exp.

<a id="rappels"></a>

## 🔁 Rappels

### M05a.R1 — Dérivées et variations (R7) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

Soit $f(x) = x\ln x - x$ sur $]0, +\infty[$.
1. Calcule $f'(x)$.
2. Où $f'$ s'annule-t-elle ?
3. Dresse le tableau de variations de $f$. Quelle est sa valeur minimale ?
4. Écris l'équation de la tangente à la courbe en $x = e$.
5. Dérive $g(x) = (3x - 2)^4$.

### M05a.R2 — Suites définies par récurrence (R5) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

Soit $u_0 = 5$ et $u_{n+1} = 0{,}4\,u_n + 1{,}2$.
1. Calcule $u_1$ et $u_2$.
2. Si la suite converge, quelle est sa limite $\ell$ ? (Résous $\ell = 0{,}4\,\ell + 1{,}2$.)
3. Montre que $u_{n+1} - \ell = 0{,}4\,(u_n - \ell)$, et déduis-en $u_n - \ell$ en fonction de $n$.
4. Quel est le plus petit $n$ tel que $|u_n - \ell| < 0{,}01$ ?
5. L'erreur est multipliée par 0,4 à chaque pas. Comment appelle-t-on ce type de convergence, par opposition à celle de Newton ?

### M05a.R3 — Log-probabilités et log-sum-exp (M04) 🔁 ★ ⏱️ 5 min
*Fiche §8 · parcours C*

1. Que vaut $\ln\big(10^{-300} \times 10^{-300}\big)$ (2 décimales) ?
2. Le produit $10^{-300} \times 10^{-300}$ est-il représentable en `float64` ?
3. Deux hypothèses ont pour log-probabilités non normalisées $-5$ et $-6$. Normalise-les en probabilités (4 décimales).
4. Que vaut $\text{LSE}(-5, -6)$ (4 décimales) ?
5. Pourquoi M04 soustrayait-il le maximum des log-vraisemblances avant de prendre les exponentielles ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"7/9"` ; une expression en $x$ entre guillemets, comme `"2*x**3 - x"` ;
- une liste entre crochets, comme `[-1.5, 2.5]` ; un intervalle entre guillemets, comme `"[-4, 6]"` ; vrai ou faux par `True` ou `False` ; une lettre entre guillemets, comme `"B"` ; un texte entre guillemets, comme `"10.01"`.

### Ex M05a.1 — Dérivées secondes et convexité ✏️ ★ ⏱️ 20 min
**Objectif :** calculer des dérivées secondes, en déduire où une fonction est convexe ou concave, et vérifier l'inégalité de convexité sur un exemple.
**Prérequis :** fiche §1 ; R7 §6 et §7 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | pour $f(x) = x\,e^{2x}$ : $f''(0)$ | un entier |
| b | pour $g(x) = x^4 - 6x^2 + 1$ : le plus grand intervalle **fermé** sur lequel $g$ est concave | un intervalle entre guillemets |
| c | les abscisses des points d'inflexion de $g$, dans l'ordre croissant | une liste |
| d | pour $u(x) = \sqrt{1 + x^2}$ : $u''(1)$ | un nombre (4 décimales) |
| e | $u$ est-elle convexe sur tout $\mathbb{R}$ ? | `True` ou `False` |
| f | pour $h(x) = x\ln x$ sur $]0, +\infty[$ : $h''(2)$ | un nombre (1 décimale) |
| g | la valeur de $k$ pour laquelle $x^3 + k\,x^2 + 1$ a un point d'inflexion en $x = 2$ | un entier |
| h | pour l'exponentielle : l'écart $\frac{e^0 + e^2}{2} - e^1$, entre le milieu de la corde et la courbe | un nombre (4 décimales) |

Dans ta copie : pour $g$, dresse le tableau de signes de $g''$. Que dit le signe de h) ? Refais le calcul de h) pour la fonction concave $\ln$, avec les points 1 et 3 : quel est le signe de l'écart ?

### Ex M05a.2 — Extrema locaux et globaux sur un intervalle fermé ✏️ ★★ ⏱️ 20 min
**Objectif :** trouver les points critiques, les classer avec la dérivée seconde, et comparer avec les bords pour trouver les extrema globaux.
**Prérequis :** fiche §2 ; R7 §8 · **Parcours :** C, E

Soit $f(x) = 3x^4 - 4x^3 - 12x^2 + 5$.

| | Question | Réponse attendue |
|---|---|---|
| a | les points critiques de $f$, dans l'ordre croissant | une liste |
| b | les valeurs de $f$ en ces points, dans le même ordre | une liste |
| c | le point critique où $f$ a un maximum local | un entier |
| d | sur $[-2, 3]$ : la valeur du maximum global | un entier |
| e | l'abscisse où ce maximum global est atteint | un entier |
| f | sur $[-2, 3]$ : la valeur du minimum global | un entier |
| g | sur $[-1{,}5 ;\ 1{,}5]$ : la valeur du maximum global | un nombre (4 décimales) |
| h | $f$ a-t-elle un maximum global sur $\mathbb{R}$ ? | `True` ou `False` |

Dans ta copie : écris $f'(x)$ factorisée, et $f''$ en chaque point critique. Dresse le tableau de variations sur $[-2, 3]$. Pourquoi le maximum global de d) n'annule-t-il pas $f'$ ?

### Ex M05a.3 — Points d'inflexion et test de la dérivée seconde ✏️ ★★ ⏱️ 15 min
**Objectif :** voir où le test de la dérivée seconde ne conclut pas, et revenir au signe de la dérivée.
**Prérequis :** fiche §1 et §2 · **Parcours :** C

Soit $p(x) = x^5 - 5x^4$.

| | Question | Réponse attendue |
|---|---|---|
| a | les points critiques de $p$, dans l'ordre croissant | une liste |
| b | $p''(4)$ | un entier |
| c | $p''(0)$ | un entier |
| d | en $x = 0$, $p$ a : `"A"` un maximum local, `"B"` un minimum local, `"C"` ni l'un ni l'autre | une lettre |
| e | les abscisses des points d'inflexion de $p$ | une liste |
| f | $p(3)$ | un entier |
| g | $x^4$ a-t-elle un point d'inflexion en 0 ? | `True` ou `False` |

Dans ta copie : écris $p'$ et $p''$ factorisées, puis le tableau de signes de $p'$ et celui de $p''$. Pourquoi $p''(0) = 0$ ne donne-t-il pas un point d'inflexion en 0 ?

### Ex M05a.4 — Polynômes de Taylor de trois fonctions usuelles ✏️ ★ ⏱️ 20 min
**Objectif :** écrire des polynômes de Taylor, en 0 et en un autre point, et les évaluer.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | le polynôme de Taylor d'ordre 2 de $\cos$ en 0 | une expression en $x$ |
| b | le polynôme de Taylor d'ordre 3 de $\ln(1 + x)$ en 0 | une expression en $x$ |
| c | le polynôme de Taylor d'ordre 3 de $\frac{1}{1 - x}$ en 0 | une expression en $x$ |
| d | le polynôme de Taylor d'ordre 2 de $e^x$ **en $a = 1$**, évalué en $x = 1{,}1$ | un nombre (4 décimales) |
| e | le polynôme de b), évalué en $x = 0{,}1$ | un nombre (5 décimales) |
| f | le coefficient de $x^4$ dans le polynôme de Taylor de $\cos$ en 0 | une fraction irréductible |
| g | le polynôme de Taylor d'ordre 2 de $\sin$ en $a = \frac{\pi}{2}$, évalué en $x = \frac{\pi}{2} + 0{,}3$ | un nombre (3 décimales) |
| h | pour $q(x) = x^3 - 2x^2 + 1$ : le coefficient de $(x - 1)^2$ dans son polynôme de Taylor d'ordre 3 en $a = 1$ | un entier |

Dans ta copie : compare d), e) et g) aux valeurs exactes ($e^{1{,}1}$, $\ln 1{,}1$, $\cos 0{,}3$). Écris le polynôme de h) en entier, puis développe-le : que retrouves-tu, et pourquoi ?

### Ex M05a.5 — Le reste de Taylor : borner l'erreur d'une approximation ✏️ ★★ ⏱️ 20 min
**Objectif :** majorer l'erreur d'un polynôme de Taylor par le reste de Lagrange, la comparer à l'erreur vraie, et choisir un ordre pour une précision donnée.
**Prérequis :** fiche §3 · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | le polynôme de Taylor d'ordre 3 de $\sin$ en 0, évalué en $x = 0{,}5$ | un nombre (6 décimales) |
| b | l'erreur vraie $\lvert \sin 0{,}5 - P_3(0{,}5) \rvert$ | un nombre (7 décimales) |
| c | la borne de Lagrange de cette erreur, avec le reste d'ordre 4 (le terme en $x^4$ de $\sin$ est nul, donc $P_3 = P_4$) et $\lvert \sin^{(5)} \rvert \le 1$ | un nombre (7 décimales) |
| d | pour $e^x$ en 0, évalué en $x = 1$, avec $e^\xi \le 3$ : le plus petit ordre $n$ pour lequel la borne $\frac{3}{(n+1)!}$ est inférieure à $10^{-6}$ | un entier |
| e | pour $\ln(1 + x)$ en 0, d'ordre 2, évalué en $x = 0{,}1$ : la borne de Lagrange, avec $\lvert f'''(t) \rvert = \frac{2}{(1 + t)^3} \le 2$ pour $t \ge 0$ | un nombre (6 décimales) |
| f | pour $\cos$ en 0 d'ordre 2 (et donc 3) : la borne de Lagrange pour $\lvert x \rvert \le 0{,}2$ | un nombre (7 décimales) |
| g | le plus grand $x > 0$ pour lequel la borne $\frac{x^3}{6}$ de l'erreur de $\sin x \approx x$ reste inférieure à 0,001 | un nombre (4 décimales) |

Dans ta copie : pour b) et c), la borne est-elle loin de l'erreur vraie ? Pour d), écris les factorielles jusqu'à la bonne. Pourquoi peut-on utiliser le reste d'ordre 4 en c), et qu'y gagne-t-on ?

### Ex M05a.6 — Newton à la main : une racine carrée en trois pas ✏️ ★ ⏱️ 20 min
**Objectif :** faire des pas de Newton exacts, voir l'erreur élevée au carré, et repérer un point de départ interdit.
**Prérequis :** fiche §4 ; R5 · **Parcours :** C, E

On cherche $\sqrt{10}$ en résolvant $f(x) = x^2 - 10 = 0$ par la méthode de Newton, depuis $x_0 = 3$.

| | Question | Réponse attendue |
|---|---|---|
| a | $x_1$ | une fraction irréductible |
| b | $x_2$ | une fraction irréductible |
| c | $x_3$ | un nombre (10 décimales) |
| d | l'erreur $x_2 - \sqrt{10}$, multipliée par $10^6$ | un nombre (2 décimales) |
| e | le rapport $\frac{x_2 - \sqrt{10}}{(x_1 - \sqrt{10})^2}$ | un nombre (3 décimales) |
| f | la limite de la suite si l'on part de $x_0 = -3$ | un nombre (4 décimales) |
| g | peut-on partir de $x_0 = 0$ ? | `True` ou `False` |
| h | un pas de Newton pour $g(x) = \ln x - 1$ depuis $x_0 = 2$ : $x_1$ | un nombre (4 décimales) |

Dans ta copie : écris l'itération $x_{k+1} = \frac{1}{2}\big(x_k + \frac{10}{x_k}\big)$ à partir de la formule de Newton. Compare e) à $\frac{1}{2\sqrt{10}}$ (fiche §4) ; montre même que $x_{k+1} - \sqrt{10} = \frac{(x_k - \sqrt{10})^2}{2x_k}$ exactement. Quelle racine h) cherche-t-elle ?

### Ex M05a.7 — L'erreur d'une différence avant et d'une différence centrée, par Taylor ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer deux différences finies, et comparer leurs erreurs aux prévisions de Taylor.
**Prérequis :** fiche §5 · **Parcours :** C, E

Soit $f(x) = \sqrt{x}$, au point $x = 4$, avec le pas $h = 0{,}2$.

| | Question | Réponse attendue |
|---|---|---|
| a | $f'(4)$ | une fraction irréductible |
| b | la différence avant $\frac{f(4{,}2) - f(4)}{0{,}2}$ | un nombre (5 décimales) |
| c | son erreur, différence avant moins $f'(4)$ | un nombre (5 décimales) |
| d | la prévision de Taylor $\frac{h}{2}f''(4)$ | un nombre (6 décimales) |
| e | la différence centrée $\frac{f(4{,}2) - f(3{,}8)}{0{,}4}$ | un nombre (6 décimales) |
| f | la prévision de Taylor $\frac{h^2}{6}f'''(4)$ de son erreur | une fraction irréductible |
| g | par combien l'erreur de la différence centrée est-elle divisée, à peu près, si l'on divise $h$ par 2 ? | un entier |
| h | la différence seconde $\frac{f(4{,}2) - 2f(4) + f(3{,}8)}{h^2}$ | un nombre (5 décimales) |

Dans ta copie : écris $f'$, $f''$ et $f'''$. Calcule l'erreur de e), et compare-la à f). Que doit approcher h), et à quel ordre ?

### Ex M05a.8 — Les flottants : 0,1 en binaire, epsilon machine, nombres représentables ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire des nombres en binaire, et calculer des écarts entre flottants consécutifs à partir de la représentation.
**Prérequis :** fiche §6 · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | 0,625 écrit en binaire | un texte avec un point, comme `"0.11"` |
| b | 0,1 a-t-il un développement binaire fini ? | `True` ou `False` |
| c | 0,1 s'écrit en binaire « 0,0 » suivi d'un bloc de 4 chiffres répété sans fin : ce bloc | un texte de 4 chiffres |
| d | l'exposant $k$ tel que l'epsilon machine de `float64` vaut $2^k$ | un entier |
| e | l'exposant $k$ tel que l'écart entre 1 024 et le `float64` suivant vaut $2^k$ | un entier |
| f | le plus petit entier positif qui n'est pas exactement représentable en `float64` | un entier |
| g | l'epsilon machine de `float16` | une fraction irréductible |
| h | l'exposant $k$ tel que l'erreur relative d'arrondi maximale d'une opération en `float32` (la moitié de son epsilon) vaut $2^k$ | un entier |

Dans ta copie : écris les multiplications par 2 qui donnent a) et c). Pourquoi l'écart entre deux flottants consécutifs double-t-il à chaque puissance de 2 ? Combien y a-t-il de `float64` entre 1 et 2 ?

### Ex M05a.9 — Le meilleur pas par le calcul : minimiser une borne d'erreur ✏️ ★★ ⏱️ 20 min
**Objectif :** trouver le pas qui minimise une borne d'erreur (troncature + bruit), pour une différence avant et une différence centrée.
**Prérequis :** fiche §5 et §7 ; R7 §8 · **Parcours :** C, E

Un capteur mesure une grandeur $f(t)$ avec une erreur d'au plus $\delta = 10^{-6}$ (en unités de $f$). On veut sa dérivée $f'(t)$ par une différence finie de pas $h$. On sait que $|f''| \le M_2 = 2$ et $|f'''| \le M_3 = 3$. Les bornes d'erreur sont celles de la fiche (§7) :

$$E_{\text{avant}}(h) = \frac{M_2}{2}h + \frac{2\delta}{h}, \qquad E_{\text{centrée}}(h) = \frac{M_3}{6}h^2 + \frac{\delta}{h}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | le pas $h^*$ qui minimise $E_{\text{avant}}$, multiplié par 1 000 | un nombre (3 décimales) |
| b | $E_{\text{avant}}(h^*)$, multipliée par 1 000 | un nombre (3 décimales) |
| c | le pas $h^*$ qui minimise $E_{\text{centrée}}$ | un nombre (3 décimales) |
| d | $E_{\text{centrée}}(h^*)$, multipliée par $10^4$ | un nombre (2 décimales) |
| e | avec un capteur 1 000 fois plus précis ($\delta = 10^{-9}$) : par combien le $h^*$ de la différence centrée est-il multiplié ? | un nombre (1 décimale) |
| f | et par combien $E_{\text{centrée}}(h^*)$ est-elle multipliée ? | un nombre (2 décimales) |
| g | pour la différence seconde, avec la borne $E(h) = h^2 + \frac{4\delta}{h^2}$ et $\delta = 10^{-6}$ : le pas qui la minimise | un nombre (4 décimales) |
| h | avec ce capteur ($\delta = 10^{-6}$), la différence centrée à son meilleur pas est-elle plus précise que la différence avant à son meilleur pas ? | `True` ou `False` |

Dans ta copie : écris la dérivée de chaque borne et résous $E'(h) = 0$. Vérifie que c'est un minimum. Montre que, pour la différence centrée, l'erreur au meilleur pas varie comme $\delta^{2/3}$.

### Ex M05a.10 — log-sum-exp à la main : la softmax stable de trois scores ✏️ ★ ⏱️ 15 min
**Objectif :** calculer un log-sum-exp, une softmax et un log-softmax sans overflow, à la main.
**Prérequis :** fiche §8 · **Parcours :** C, E

Un modèle donne trois scores (*logits*) $\mathbf{v} = (802,\ 800,\ 795)$.

| | Question | Réponse attendue |
|---|---|---|
| a | `math.exp(802)` lève-t-il une `OverflowError` ? | `True` ou `False` |
| b | le maximum $m$ des scores | un entier |
| c | $\text{LSE}(\mathbf{v})$ | un nombre (4 décimales) |
| d | la softmax de $\mathbf{v}$ | une liste de 3 nombres (4 décimales) |
| e | le log-softmax du deuxième score | un nombre (4 décimales) |
| f | la cross-entropy si la bonne classe est la troisième : $-\ln \text{softmax}(\mathbf{v})_3$ | un nombre (4 décimales) |
| g | $\text{LSE}(802, 802, 802)$ | un nombre (4 décimales) |

Dans ta copie : écris les étapes de c) (soustraire le maximum, les exponentielles, la somme, le logarithme, rajouter le maximum). Vérifie que c) est entre $m$ et $m + \ln 3$, et que g) atteint la borne de droite.

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex M05a.11 — La différence centrée est d'ordre 2 : le calcul par Taylor (cas général) ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer les ordres des différences avant, centrée et seconde pour une fonction quelconque assez dérivable, puis l'effet de Richardson.
**Prérequis :** fiche §3 et §5 · **Parcours :** C

Soit $f$ trois fois dérivable, de dérivée troisième continue, sur un intervalle qui contient $[x - h, x + h]$ ($h > 0$), et $M_3$ un majorant de $|f'''|$ sur cet intervalle. On note $D_+(h) = \frac{f(x + h) - f(x)}{h}$ et $D_0(h) = \frac{f(x + h) - f(x - h)}{2h}$.
1. Écris le développement de Taylor d'ordre 2 de $f(x + h)$ et de $f(x - h)$ en $x$, avec le reste de Lagrange (deux points $\xi_+$ et $\xi_-$, à situer).
2. Déduis-en $D_0(h) - f'(x) = \frac{h^2}{12}\big(f'''(\xi_+) + f'''(\xi_-)\big)$.
3. Montre que $|D_0(h) - f'(x)| \le \frac{M_3}{6}h^2$.
4. Avec un développement d'ordre 1, montre de même que $|D_+(h) - f'(x)| \le \frac{M_2}{2}h$, si $|f''| \le M_2$.
5. On suppose maintenant $f$ quatre fois dérivable, avec $|f^{(4)}| \le M_4$. Montre que $\Big|\frac{f(x + h) - 2f(x) + f(x - h)}{h^2} - f''(x)\Big| \le \frac{M_4}{12}h^2$.
6. Montre que $\frac{D_0(h) - f'(x)}{h^2}$ tend vers $\frac{f'''(x)}{6}$ quand $h \to 0$. Déduis-en que, si $f'''(x) \ne 0$, diviser $h$ par 2 divise l'erreur par environ 4.
7. On admet que, pour $f$ assez dérivable, $D_0(h) = f'(x) + c_2 h^2 + c_4 h^4 + O(h^6)$. Montre que $\frac{4D_0(h/2) - D_0(h)}{3} = f'(x) - \frac{c_4}{4}h^4 + O(h^6)$.

### Ex M05a.12 — Newton double les décimales justes : l'erreur au carré (racine simple) ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer la convergence quadratique de la méthode de Newton près d'une racine simple, et voir ce qui change pour une racine double.
**Prérequis :** fiche §3 et §4 ; R5 · **Parcours :** C

Soit $f$ deux fois dérivable, de dérivée seconde continue, et $r$ une racine **simple** : $f(r) = 0$ et $f'(r) \ne 0$. On note $e_k = x_k - r$ l'erreur de la suite de Newton.
1. Écris le développement de Taylor d'ordre 1 de $f$ en $x_k$, évalué en $r$, avec le reste de Lagrange (un point $\xi_k$ entre $x_k$ et $r$).
2. Déduis-en $e_{k+1} = \frac{f''(\xi_k)}{2f'(x_k)}\,e_k^2$ (si $f'(x_k) \ne 0$).
3. On suppose que, sur un intervalle $I$ qui contient $r$ et les $x_k$, $|f''| \le M$ et $|f'| \ge m > 0$. Avec $C = \frac{M}{2m}$, montre que $|e_{k+1}| \le C\,e_k^2$.
4. Montre par récurrence que $C|e_k| \le (C|e_0|)^{2^k}$. Si $C|e_0| = 0{,}1$, à partir de quel pas $k$ a-t-on $C|e_k| \le 10^{-16}$ ?
5. Pour $f(x) = x^2 - c$ ($c > 0$), montre que $e_{k+1} = \frac{e_k^2}{2x_k}$ exactement. Déduis-en que, depuis n'importe quel $x_0 > 0$, on a $x_k \ge \sqrt{c}$ pour tout $k \ge 1$.
6. Pour $f(x) = (x - r)^2$, une racine **double**, montre que $e_{k+1} = \frac{e_k}{2}$. Comment s'appelle cette convergence ? Combien de pas faut-il pour gagner une décimale ?
7. Pour aller plus loin : pour **minimiser** $g$, on applique Newton à $g'$ : $x_{k+1} = x_k - \frac{g'(x_k)}{g''(x_k)}$. Montre que, pour $g(x) = a x^2 + b x + c$ avec $a > 0$, un seul pas mène au minimum, depuis n'importe quel point.

### Ex M05a.13 — Encadrer le log-sum-exp : max ≤ LSE ≤ max + ln n ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'encadrement du log-sum-exp et ses propriétés, et mesurer l'écart au maximum.
**Prérequis :** fiche §8 ; R6 · **Parcours :** C

Soit $\mathbf{v} = (v_1, \ldots, v_n)$ des réels, $m = \max_i v_i$, et $\text{LSE}(\mathbf{v}) = \ln\sum_i e^{v_i}$.
1. Montre que $m \le \text{LSE}(\mathbf{v}) \le m + \ln n$.
2. Quand l'inégalité de droite est-elle une égalité ? Celle de gauche peut-elle l'être pour $n \ge 2$ ?
3. Montre que $\text{LSE}(\mathbf{v} + c) = \text{LSE}(\mathbf{v}) + c$ pour tout réel $c$ (ajouté à chaque $v_i$), puis que $\text{softmax}(\mathbf{v} + c) = \text{softmax}(\mathbf{v})$.
4. Montre que si $v_i \le w_i$ pour tout $i$, alors $\text{LSE}(\mathbf{v}) \le \text{LSE}(\mathbf{w})$.
5. Pour $n = 2$, montre que $\text{LSE}(t, 0) - \max(t, 0) = \ln\big(1 + e^{-|t|}\big)$. Déduis-en que cet écart est au plus $\ln 2$, et qu'il tend vers 0 quand $|t| \to +\infty$.
6. On note $g = m - v_{(2)}$ l'écart entre le plus grand score et le deuxième. Avec $\ln(1 + u) \le u$, montre que $\text{LSE}(\mathbf{v}) - m \le (n - 1)\,e^{-g}$. Applique à $\mathbf{v} = (10, 3, 2)$ : compare la borne à l'écart vrai.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, estimation et explication

### Ex M05a.14 — Pourquoi les bibliothèques de ML calculent log(softmax) d'un seul coup 🔗 ★ ⏱️ 15 min
**Objectif :** calculer un log-softmax et une cross-entropy par le log-sum-exp, et voir ce que donne le calcul en deux temps quand une probabilité s'efface.
**Prérequis :** fiche §6 et §8 ; Ex M05a.10 · **Parcours :** C, E

Un classifieur à trois classes donne les scores $\mathbf{z} = (780,\ 20,\ -30)$ pour un exemple dont la bonne classe est la **deuxième**. La loss (la cross-entropy) de cet exemple est $-\ln \text{softmax}(\mathbf{z})_2$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\text{LSE}(\mathbf{z})$ | un nombre (2 décimales) |
| b | le log-softmax de la deuxième classe, $z_2 - \text{LSE}(\mathbf{z})$ | un nombre (2 décimales) |
| c | la probabilité $\text{softmax}(\mathbf{z})_2$, calculée **sans overflow** par $\frac{e^{z_2 - m}}{\sum_j e^{z_j - m}}$ en `float64` : vaut-elle exactement 0 ? | `True` ou `False` |
| d | la loss calculée par le log-softmax | un nombre (1 décimale) |
| e | la loss calculée en deux temps, `-math.log(p2)` avec la probabilité de c) : est-elle un nombre fini ? | `True` ou `False` |
| f | pour des scores plus raisonnables, $\mathbf{z}' = (2,\ 0,\ -1)$ : le log-softmax de la troisième classe | un nombre (4 décimales) |

Dans ta copie : pourquoi la loss de d) est-elle si grande, et pourquoi est-elle quand même utile à l'entraînement (le modèle se trompe lourdement sur cet exemple) ? Explique en deux phrases pourquoi une bibliothèque calcule la loss à partir des scores, par un log-softmax, plutôt qu'à partir des probabilités.

### Ex M05a.15 — MML §5.1 : dérivée d'une fonction d'une variable et série de Taylor (lecture guidée) 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la définition de la dérivée et des polynômes de Taylor, et refaire les exemples du livre avec d'autres fonctions.
**Prérequis :** fiche §1 et §3 · **Parcours :** C, E

Lis MML §5.1 (le quotient différentiel, la dérivée, puis le §5.1.1 sur Taylor et le §5.1.2 sur les règles de dérivation). Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Comment le livre définit-il le quotient différentiel (*difference quotient*), puis la dérivée ? Quel lien avec la sécante et la tangente ?
2. Écris la définition du polynôme de Taylor de degré $n$ et de la série de Taylor, avec les notations du livre ($x_0$). Quelle condition le livre pose-t-il sur $f$ pour parler de série de Taylor ?
3. Le livre calcule le polynôme de Taylor d'un **polynôme**. Refais-le avec $f(x) = x^3$ en $x_0 = 2$, pour les degrés 1 à 4. Que se passe-t-il à partir du degré 3, et pourquoi ?
4. Le livre développe en série une fonction trigonométrique. Refais l'exercice avec $\cos x - \sin x$ en 0, jusqu'au terme de degré 4.
5. Le livre rappelle les règles de dérivation (somme, produit, quotient, chaîne). Dérive $\frac{x}{1 + x^2}$ par la règle du quotient, puis compare le résultat à la dérivée seconde de $g(x) = \ln(1 + x^2)$ (fiche §1). Quel lien y a-t-il entre $\frac{x}{1 + x^2}$ et $g$ ?
6. Que dit le livre (ou une note de bas de page) de l'égalité entre une fonction et sa série de Taylor ? Donne, avec la fiche, un exemple où elle n'a lieu que sur un intervalle.
7. Note trois mots ou tournures en anglais de cette section qui étaient nouveaux pour toi, avec leur traduction.

### Ex M05a.16 — Fermi : l'erreur d'arrondi d'une somme d'un million de nombres 🧮 ★ ⏱️ 10 min
**Objectif :** estimer l'ordre de grandeur de l'erreur d'arrondi accumulée dans une longue somme, en `float64` et en `float32`.
**Prérequis :** fiche §6 · **Parcours :** C

On additionne, un par un, $n = 10^6$ nombres positifs de l'ordre de 1 (des montants, les losses de batches…). Chaque addition arrondit la somme partielle avec une erreur relative d'au plus $u$ ($u \approx 1{,}1 \times 10^{-16}$ en `float64`, $u \approx 6 \times 10^{-8}$ en `float32`). Donne des ordres de grandeur, en justifiant chaque étape.
1. De quel ordre est la somme finale ? Et une somme partielle typique ?
2. Dans le pire cas, toutes les erreurs ont le même signe : majore l'erreur **relative** de la somme finale en `float64`, puis en `float32`.
3. Si les erreurs sont de signes aléatoires, elles se compensent en partie, comme une marche au hasard : l'erreur grandit comme $\sqrt{n}$ fois une erreur. Refais l'estimation.
4. Combien de chiffres justes reste-t-il, dans chaque cas, en `float32` ?
5. `numpy.sum` additionne par paires (un arbre de sommes), si bien que chaque nombre ne traverse qu'environ $\log_2 n$ additions. Que devient la borne du pire cas ?
6. Pourquoi cela compte-t-il quand on additionne les losses d'un très grand nombre de batches en `float32` ?

### Ex M05a.17 — Expliquer la convexité et pourquoi elle rassure quand on minimise 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement ce qu'est une fonction convexe et ce qu'elle garantit pour une minimisation.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

Une collègue qui débute te demande : « On me dit que la log-loss de la régression logistique est convexe, et que c'est une bonne nouvelle. Convexe, ça veut dire quoi, et pourquoi c'est une bonne nouvelle ? »

Réponds-lui **en huit lignes au plus**, sans formule compliquée. Ta réponse doit donner une image de la convexité (la corde, la cuvette ou la tangente), dire ce qu'elle garantit pour la recherche d'un minimum, et donner un contre-exemple d'une fonction qui n'est pas convexe, où une descente peut se tromper.

<a id="entretien"></a>

## 💼 Entretien

### M05a.E1 — Pourquoi soustraire le maximum avant de calculer une softmax ? 💼 ★ ⏱️ 10 min
*Fiche §6 et §8 · parcours C, E*

« Dans une implémentation de la softmax, on voit souvent `z - z.max()` avant l'exponentielle. Pourquoi ? Est-ce que ça change le résultat ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire le problème évité (avec un ordre de grandeur), pourquoi le résultat ne change pas, ce qu'on garde du côté des petites valeurs, et le lien avec le log-softmax et la loss. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m05a_derivees_taylor/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M05a.18 | Évaluer un polynôme de Taylor · `taylor_polynomial` | 🔨 | ★ | 20 | C, E |
| M05a.19 | La méthode de Newton, avec ses cas d'échec · `newton` | 🔨 | ★ | 20 | C, E |
| M05a.20 | L'extrapolation de Richardson : annuler le terme d'erreur en h² · `richardson_derivative` | 🔨 | ★★ | 20 | C |
| M05a.21 | L'epsilon machine, en float64, float32 et float16 · `machine_epsilon` | 🔨 | ★ | 15 | C |
| M05a.22 | Un log-sum-exp stable · `logsumexp` | 🔨 | ★ | 15 | C, E |
| M05a.23 | SymPy `series` et `numpy.finfo` contre tes fonctions | 📦 | ★ | 15 | C |
| M05a.24 | Prédire : Newton depuis un mauvais point de départ | 🔮 | ★ | 10 | C |
| M05a.25 | Taylor de plus en plus loin : où le polynôme décroche | 🔬 | ★★ | 20 | C |
| M05a.26 | Une fonction et ses polynômes de Taylor d'ordre 1, 2 et 3 | 🎨 | ★ | 20 | C, E |
| M05a.27 | Chasse à l'erreur : une softmax qui renvoie `nan` | 🐛 | ★ | 15 | C |
| M05a.28 | Erreur relative ou absolue : choisir la tolérance d'un test | 🛠️ | ★ | 10 | C |
| M05a.29 | Défi : une racine cubique à 10⁻¹² en le moins d'itérations possible | 🏆 | ★★★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
