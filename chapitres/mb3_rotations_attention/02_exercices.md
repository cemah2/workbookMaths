# MB3 · Rotations, moyennes pondérées et softmax en ligne — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/mb3_rotations_attention/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB3`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les angles sont en radians (en degrés quand l'énoncé le dit), positifs dans le sens inverse des aiguilles d'une montre ; les vecteurs sont des colonnes, et $\mathbf{R}_\theta$ est la rotation d'angle $\theta$ du plan ; $\mathbf{R}_{ij}(\theta)$ est la rotation de Givens qui tourne $\mathbf{e}_i$ vers $\mathbf{e}_j$, les coordonnées étant numérotées **à partir de 1** sur papier et à partir de 0 dans le code ; dans l'espace, $\mathbf{R}_{12}$ tourne autour de $\mathbf{e}_3$ et $\mathbf{R}_{23}$ autour de $\mathbf{e}_1$ ; la matrice $\mathbf{P}$ d'une permutation $\sigma$ a pour lignes $\mathbf{e}_{\sigma(1)}^\top, \ldots, \mathbf{e}_{\sigma(n)}^\top$ ; $e^{i\theta} = \cos\theta + i\sin\theta$ ; l'encodage d'une variable cyclique de période $\tau$ est $\mathbf{e}(t) = (\cos\omega t, \sin\omega t)$, avec $\omega = 2\pi/\tau$ ; des scores $s_j$ donnent les poids $p_j = e^{s_j}/\sum_ke^{s_k}$, et un masque met un score à $-\infty$ ; le noyau gaussien de largeur de bande $h$ est $\exp\big(-\lVert\mathbf{x} - \mathbf{x}_i\rVert^2/(2h^2)\big)$ ; l'état de la softmax en ligne est $(m, l, a)$, l'état vide $(-\infty, 0, 0)$ ; le logarithme est népérien. Dans le notebook, une matrice s'écrit comme la liste de ses lignes, un vecteur comme une liste ou un tableau **1-D**, et $-\infty$ comme `-np.inf`.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 à 5 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### MB3.Q1 — Formules d'addition et rotations du plan : le bon signe, composer, inverser, rotation ou symétrie ? 🧠 ★ ⏱️ 5 min
*Fiche §1 et §2 · parcours C, E*

1. Complète par $+$ ou $-$ : $\cos(a + b) = \cos a\cos b \ \square\ \sin a\sin b$ et $\sin(a - b) = \sin a\cos b \ \square\ \cos a\sin b$.
2. $\mathbf{R}_{2\pi/9}\,\mathbf{R}_{5\pi/18}$ est la rotation de quel angle ? Écris sa matrice.
3. Vrai ou faux : $\mathbf{R}_{\pi/7}^{-1} = \mathbf{R}_{\pi/7}^\top = \mathbf{R}_{13\pi/7}$.
4. $\mathbf{A} = \frac{1}{41}\begin{pmatrix} 9 & -40 \\ 40 & 9 \end{pmatrix}$ et $\mathbf{B} = \frac{1}{41}\begin{pmatrix} 9 & 40 \\ 40 & -9 \end{pmatrix}$ sont orthogonales. Laquelle est une rotation, laquelle une symétrie ? Quel vecteur la symétrie laisse-t-elle fixe ?
5. Vrai ou faux : pour tous angles $\alpha$ et $\beta$, $\mathbf{R}_\alpha\mathbf{R}_\beta = \mathbf{R}_\beta\mathbf{R}_\alpha$.

### MB3.Q2 — Rotations de l'espace, de Givens et par blocs : commutent-elles, que fixent-elles, que change une permutation des coordonnées ? 🧠 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Vrai ou faux : dans l'espace, la rotation autour de $\mathbf{e}_1$ et la rotation autour de $\mathbf{e}_3$ commutent, quels que soient leurs angles.
2. Dans $\mathbb{R}^5$, $\mathbf{R}_{13}(\alpha)$ et $\mathbf{R}_{24}(\beta)$ commutent-elles ? Et $\mathbf{R}_{13}(\alpha)$ et $\mathbf{R}_{35}(\beta)$, pour des angles qui ne sont pas des multiples de $\pi$ ?
3. Quels vecteurs de $\mathbb{R}^5$ la rotation $\mathbf{R}_{24}(\theta)$ laisse-t-elle fixes, pour $\theta$ qui n'est pas un multiple de $2\pi$ ?
4. $\mathbf{D} = \operatorname{diag}(\mathbf{R}_{\pi/2}, \mathbf{R}_{\pi/5}, \mathbf{R}_{3\pi/4})$ est une matrice $6 \times 6$ diagonale par blocs. Que vaut son déterminant ? Écris $\mathbf{D}^{-1}$ par blocs.
5. Dans $\mathbb{R}^3$, $\mathbf{P}$ échange les coordonnées 2 et 3. Dans quel plan tourne $\mathbf{P}^\top\mathbf{R}_{12}(\theta)\mathbf{P}$, et vers quel vecteur tourne-t-elle $\mathbf{e}_1$ ?

### MB3.Q3 — Encoder une direction ou un jour de l'année : une ou deux coordonnées, quelle période, quelle distance entre deux encodages ? 🧠 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

1. Vrai ou faux : $\cos\frac{2\pi t}{365}$ seul donne un code différent à chaque jour $t = 0, \ldots, 364$ de l'année.
2. L'heure est encodée avec la période 24. Que vaut $\lVert\mathbf{e}(22) - \mathbf{e}(2)\rVert^2$, entre 22 h et 2 h ? Et entre 10 h et 14 h ?
3. Pour encoder le jour de la semaine (0 à 6), quelle période et quelle pulsation $\omega$ prends-tu ?
4. Quelle est la plus grande valeur possible de $\lVert\mathbf{e}(t) - \mathbf{e}(t')\rVert^2$, et pour quel écart $t - t'$ ?
5. Vrai ou faux : avec la seule horloge de période 365 jours, deux dates séparées d'exactement un an ont le même encodage.

### MB3.Q4 — Moyennes pondérées par une softmax : dans l'enveloppe convexe ou non, largeur de bande, masque avant ou après la softmax, et un sous-ensemble vide 🧠 ★ ⏱️ 5 min
*Fiche §5 et §6 · parcours C, E*

1. Vrai ou faux : une moyenne pondérée par une softmax des nombres 3, 8 et 11 peut valoir 12, pour des scores bien choisis.
2. Vrai ou faux : une moyenne pondérée par une softmax de points du plan est toujours dans leur enveloppe convexe.
3. Dans l'estimateur de Nadaraya-Watson, vers quoi tend la prévision quand $h \to 0$ ? Quand $h \to \infty$ ?
4. Trois poids valent $(0{,}2 ;\ 0{,}7 ;\ 0{,}1)$, et l'on veut exclure le deuxième. Que donne un score $-\infty$ avant la softmax ? Vrai ou faux : mettre le deuxième poids à 0 après la softmax donne une loi.
5. Tous les scores sont masqués. Que valent les poids ?

### MB3.Q5 — Multiplier tous les scores par c, ou leur ajouter une constante : ce qui change dans les poids, le poids maximal et l'entropie, et ce qui ne change pas 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Vrai ou faux : ajouter 5 à tous les scores change les poids.
2. Des scores donnent les poids $(0{,}5 ;\ 0{,}4 ;\ 0{,}1)$. On double tous les scores : quels sont les nouveaux poids ?
3. Multiplier les scores par $c = 4$ revient à quelle température ?
4. Quand $c$ grandit (scores non tous égaux, le plus grand unique), que deviennent le plus grand poids et l'entropie de la loi ? Et quand $c \to 0$ ?
5. On multiplie les scores par $c = -1$ : quel score reçoit le plus grand poids ?

### MB3.Q6 — La softmax en ligne : ce que garde l'état, quand le remettre à l'échelle, et l'état vide 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. Que valent $m$, $l$ et $a$ pour les scores $s_j$ et les nombres $v_j$ lus jusqu'ici ?
2. Quand faut-il remettre $l$ et $a$ à l'échelle, et par quel facteur ?
3. L'état vaut $(3, 2, 10)$. On lit un bloc d'un seul score, $3 + \ln 2$, de nombre $v = 7$. Quel est le nouvel état, et la moyenne pondérée ?
4. Comment lire, sur l'état final, le log-sum-exp des scores et le poids du score $s_j$ ?
5. Vrai ou faux : fusionner un état avec l'état vide $(-\infty, 0, 0)$ ne le change pas.

<a id="rappels"></a>

## 🔁 Rappels

### MB3.R1 — La forme exponentielle d'un complexe, et le produit comme rotation et homothétie (M22) 🔁 ★ ⏱️ 7 min
*Fiche §2 · parcours C, E*

$z = \sqrt3 - i$ et $w = 3\,e^{i\pi/6}$.
1. Le module et l'argument de $z$ (dans $]-\pi, \pi]$).
2. $zw$, sous forme exponentielle puis sous forme $x + iy$.
3. Multiplier un complexe par $w$ est quelle transformation du plan ? Écris sa matrice à l'aide de $\mathbf{R}_\theta$.
4. $z^6$, par la formule de Moivre.
5. Vrai ou faux : $\lvert e^{i\theta}z\rvert = \lvert z\rvert$ pour tout $\theta$.

### MB3.R2 — Le log-sum-exp et la softmax stable (M05a) 🔁 ★ ⏱️ 5 min
*Fiche §8 · parcours C, E*

Les scores valent $\mathbf{s} = (750, 748, 747)$.
1. $\operatorname{LSE}(\mathbf{s}) = \ln\sum_je^{s_j}$, en retranchant d'abord le plus grand score (4 décimales).
2. Que rend `np.exp(750.0)` en `float64` ?
3. La softmax de $\mathbf{s}$ (4 décimales).
4. Vrai ou faux : $\operatorname{softmax}(\mathbf{s} - 1\,500) = \operatorname{softmax}(\mathbf{s})$.
5. $\operatorname{LSE}(-750, -752, -753)$ (4 décimales). Que rend le calcul direct `np.log(np.sum(np.exp(s)))` ?

### MB3.R3 — Tempérer et tronquer une loi : p^{1/T} renormalisée, top-k et top-p comme lois conditionnelles (M28) 🔁 ★ ⏱️ 6 min
*Fiche §5 et §6 · parcours C, E*

Une loi sur quatre issues vaut $\mathbf{p} = (0{,}46 ;\ 0{,}29 ;\ 0{,}15 ;\ 0{,}10)$.
1. La loi tempérée à $T = \frac12$ (3 décimales).
2. La troncature top-2, renormalisée (fractions).
3. La troncature top-p de masse $0{,}8$ : le plus petit ensemble d'issues de masse au moins $0{,}8$, et la loi renormalisée (fractions).
4. Vrai ou faux : la troncature top-k est la loi conditionnelle de $\mathbf{p}$ sachant « l'issue est l'une des $k$ plus probables ».
5. Vers quelles lois tend la loi tempérée quand $T \to 0$ et quand $T \to \infty$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les cosinus, les exponentielles et les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une valeur exacte entre guillemets, avec `sqrt`, `pi` et des fractions, comme `"sqrt(5)/3"` ou `"pi/4"` ;
- une fraction irréductible entre guillemets, comme `"5/8"` ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ; une liste de valeurs exactes avec des fractions entre guillemets, comme `["1/6", 0, "5/6"]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- `True` ou `False` pour un vrai ou faux.

« Valeurs exactes » veut dire : tous les chiffres, sans arrondir (ces calculs tombent juste). Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex MB3.1 — Un bras articulé à deux segments : la position de la pince en valeurs exactes par les formules d'addition, les deux rotations enchaînées en une seule, et le retour par la rotation inverse ✏️ ★★ ⏱️ 30 min
**Objectif :** placer une pince par les formules d'addition, composer deux rotations du plan en une seule, et revenir en arrière par la transposée.
**Prérequis :** fiche §1 et §2 ; R9 (valeurs remarquables de cos et sin) · **Parcours :** C, E

Un bras articulé est fixé par l'épaule à l'origine. Le bras mesure 4 dm, l'avant-bras 2 dm ; au départ, les deux segments sont alignés sur l'axe des abscisses, la pince en $(6, 0)$. L'épaule tourne de 60°, ce qui fait tourner tout le bras ; puis le coude tourne l'avant-bras de 45° de plus par rapport au bras. L'avant-bras fait alors l'angle $60° + 45° = 105°$ avec l'axe des abscisses, et la pince est en
$$\mathbf{p} = \mathbf{R}_{60°}\begin{pmatrix} 4 \\ 0 \end{pmatrix} + \mathbf{R}_{105°}\begin{pmatrix} 2 \\ 0 \end{pmatrix}.$$
Une caméra fixée au bras voit la pince dans son propre repère, qui a tourné de 60° avec le bras.

| | Question | Réponse attendue |
|---|---|---|
| a | $\cos 105°$, par une formule d'addition | une valeur exacte |
| b | $\sin 105°$, par une formule d'addition | une valeur exacte |
| c | la position $\mathbf{p}$ de la pince | une liste de 2 nombres (3 décimales) |
| d | la matrice $\mathbf{R}_{60°}\mathbf{R}_{45°}$ | une matrice $2 \times 2$ (4 décimales) |
| e | vrai ou faux : $\mathbf{R}_{60°}\mathbf{R}_{45°} = \mathbf{R}_{45°}\mathbf{R}_{60°}$ | `True` ou `False` |
| f | $\mathbf{R}_{60°}^\top\,\mathbf{p}$, la pince vue par la caméra | une liste de 2 nombres (4 décimales) |
| g | la distance de l'épaule à la pince | un nombre (4 décimales) |

Dans ta copie : écris $\mathbf{p}$ en valeurs exactes ; dis ce que vaut f) en valeurs exactes et pourquoi on pouvait le prévoir sans calcul ; retrouve g) à partir de f).

### Ex MB3.2 — Rotations de Givens : deux rotations de l'espace qui ne commutent pas, deux rotations de ℝ⁴ dans des plans disjoints qui commutent, leur matrice diagonale par blocs, et la même rotation après une permutation des coordonnées ✏️ ★★ ⏱️ 25 min
**Objectif :** voir sur un vecteur que l'ordre de deux rotations de l'espace compte, écrire une matrice diagonale par blocs de rotations, et la réécrire dans d'autres plans par une permutation.
**Prérequis :** fiche §3 ; M16 (matrices de permutation) · **Parcours :** C, E

Dans l'espace, $\mathbf{R}_{23}(\frac\pi2)$ est le quart de tour autour de $\mathbf{e}_1$ et $\mathbf{R}_{12}(\frac\pi3)$ la rotation de $\frac\pi3$ autour de $\mathbf{e}_3$. Dans $\mathbb{R}^4$, on pose $\mathbf{D} = \mathbf{R}_{12}(\frac\pi3)\,\mathbf{R}_{34}(\frac\pi2)$, et l'on renumérote les coordonnées par la permutation $\sigma$ qui échange 2 et 4 ($\sigma(1) = 1$, $\sigma(2) = 4$, $\sigma(3) = 3$, $\sigma(4) = 2$), de matrice
$$\mathbf{P} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{R}_{23}(\frac\pi2)\,\mathbf{R}_{12}(\frac\pi3)\,\mathbf{e}_2$ (d'abord $\mathbf{R}_{12}$, puis $\mathbf{R}_{23}$) | une liste de 3 nombres (4 décimales) |
| b | $\mathbf{R}_{12}(\frac\pi3)\,\mathbf{R}_{23}(\frac\pi2)\,\mathbf{e}_2$ (d'abord $\mathbf{R}_{23}$, puis $\mathbf{R}_{12}$) | une liste de 3 nombres (4 décimales) |
| c | vrai ou faux : $\mathbf{R}_{23}(\frac\pi2)\mathbf{R}_{12}(\frac\pi3) = \mathbf{R}_{12}(\frac\pi3)\mathbf{R}_{23}(\frac\pi2)$ | `True` ou `False` |
| d | la matrice $\mathbf{D}$ | une matrice $4 \times 4$ (4 décimales) |
| e | vrai ou faux : $\mathbf{R}_{12}(\frac\pi3)\mathbf{R}_{34}(\frac\pi2) = \mathbf{R}_{34}(\frac\pi2)\mathbf{R}_{12}(\frac\pi3)$ | `True` ou `False` |
| f | la matrice $\mathbf{P}^\top\mathbf{D}\mathbf{P}$ | une matrice $4 \times 4$ (4 décimales) |
| g | l'angle $\theta$ tel que $\mathbf{P}^\top\mathbf{D}\mathbf{P} = \mathbf{R}_{14}(\frac\pi3)\,\mathbf{R}_{23}(\theta)$, dans $]-\pi, \pi]$ | une valeur exacte |

Dans ta copie : dis ce que b) montre de $\mathbf{R}_{12}$ ; vérifie f) par la propriété de la fiche (les plans $(\sigma(i), \sigma(j))$) ; dis pourquoi $\mathbf{P}^\top = \mathbf{P}$ ici.

### Ex MB3.3 — La direction du vent : l'encoder par (cos, sin), la distance entre deux encodages, un vent qui tourne comme une rotation de l'encodage, et la direction moyenne de trois relevés ✏️ ★★ ⏱️ 25 min
**Objectif :** encoder une direction par $(\cos, \sin)$, mesurer l'écart de deux encodages, lire un vent qui tourne comme une rotation, et moyenner des directions sur le cercle.
**Prérequis :** fiche §1 et §4 ; R9 (cercle trigonométrique) · **Parcours :** C, E

Une girouette donne la direction $\theta$ d'où vient le vent, en degrés, comptée comme sur le cercle trigonométrique : l'est vaut 0°, le nord 90°, l'ouest 180°, le sud 270°. On l'encode par $\mathbf{e}(\theta) = (\cos\theta, \sin\theta)$ (une horloge de période 360°).

| | Question | Réponse attendue |
|---|---|---|
| a | l'encodage $\mathbf{e}(150°)$ | une liste de 2 nombres (4 décimales) |
| b | $\lVert\mathbf{e}(340°) - \mathbf{e}(20°)\rVert^2$ | un nombre (4 décimales) |
| c | le vent de 150° tourne de 45° dans le sens inverse des aiguilles d'une montre : $\mathbf{R}_{45°}\,\mathbf{e}(150°)$ | une liste de 2 nombres (4 décimales) |
| d | vrai ou faux : la matrice qui envoie $\mathbf{e}(\theta)$ sur $\mathbf{e}(\theta + 45°)$ est la même pour tout $\theta$ | `True` ou `False` |
| e | la direction moyenne des trois relevés 330°, 20° et 70°, en degrés dans $[0, 360[$ | un nombre |
| f | la longueur $\rho$ du vecteur moyen de ces trois relevés | un nombre (3 décimales) |

Dans ta copie : compare b) à l'écart des nombres 340 et 20 ; montre que c) est $\mathbf{e}(195°)$ ; compare e) à la moyenne des trois nombres 330, 20 et 70.

### Ex MB3.4 — L'estimateur de Nadaraya-Watson : la température d'un refuge à partir de quatre stations de montagne pondérées par un noyau gaussien de l'écart d'altitude, pour deux largeurs de bande, et ses deux limites ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer une prévision de Nadaraya-Watson comme une moyenne pondérée par une softmax, et voir ce que la largeur de bande change.
**Prérequis :** fiche §5 ; M05a (softmax stable) · **Parcours :** C, E

Un refuge, à 2 300 m d'altitude, n'a pas de thermomètre. Quatre stations d'un même massif donnent, à midi, ces températures :

| station | Val | Bergerie | Col | Pic |
|---|---|---|---|---|
| altitude $x_i$ (m) | 1 700 | 2 100 | 2 700 | 3 100 |
| température $y_i$ (°C) | 10,4 | 6,3 | 2,2 | −1,7 |

On prévoit la température du refuge par l'estimateur de Nadaraya-Watson, avec le noyau gaussien de l'écart d'altitude, $\exp\big(-(x - x_i)^2/(2h^2)\big)$, où $x = 2\,300$ m. Les stations sont dans l'ordre du tableau.

| | Question | Réponse attendue |
|---|---|---|
| a | les quatre scores $-(x - x_i)^2/(2h^2)$, pour $h = 200$ m | une liste de 4 nombres |
| b | le poids de la Bergerie, pour $h = 200$ m | un nombre (3 décimales) |
| c | la température prévue au refuge, pour $h = 200$ m | un nombre (2 décimales) |
| d | les quatre poids, pour $h = 400$ m | une liste de 4 nombres (4 décimales) |
| e | la température prévue au refuge, pour $h = 400$ m | un nombre (2 décimales) |
| f | la limite de la prévision quand $h \to 0$ | un nombre (2 décimales) |
| g | la limite de la prévision quand $h \to \infty$ | un nombre (2 décimales) |

Dans ta copie : retranche le plus grand score avant de prendre les exponentielles ; dis en une phrase ce que la largeur de bande change.

### Ex MB3.5 — Masques : une moyenne exponentielle normalisée vue comme une softmax sur les jours passés, puis la même quand un capteur tombe en panne un jour (un score −∞) ✏️ ★★ ⏱️ 18 min
**Objectif :** écrire une moyenne exponentielle normalisée comme une softmax sur le passé, puis retirer un jour par un score $-\infty$ et reconnaître une loi conditionnelle.
**Prérequis :** fiche §6 ; R5 (moyenne exponentielle), M03 (loi conditionnelle) · **Parcours :** C, E

Un capteur relève chaque soir la température de l'eau d'un bassin, en °C : 18 le jour 1, 15 le jour 2, 21 le jour 3 et 17 le jour 4. Le soir du jour $t$, on lisse par la moyenne exponentielle normalisée de facteur $\lambda = \frac12$, qui donne au jour $u \le t$ le poids $\lambda^{t - u}$, normalisé : c'est la softmax des scores $s_u = u\ln 2$ sur les jours $u \le t$, les jours $u > t$ ayant le score $-\infty$.

| | Question | Réponse attendue |
|---|---|---|
| a | les poids des jours 1 à 4 pour le lissage du jour 4 | une liste de 4 nombres (valeurs exactes) |
| b | la valeur lissée du jour 4 | une fraction irréductible |
| c | les poids des jours 1 à 4 pour le lissage du jour 2 | une liste de 4 nombres (valeurs exactes) |
| d | le capteur est tombé en panne le jour 3 (son score passe à $-\infty$) : les poids des jours 1 à 4 pour le lissage du jour 4 | une liste de 4 nombres (valeurs exactes) |
| e | la valeur lissée du jour 4, avec la panne du jour 3 | une fraction irréductible |
| f | vrai ou faux : les poids de d) sont ceux de a), conditionnés par « le jour n'est pas le jour 3 » | `True` ou `False` |

Dans ta copie : dis pourquoi le lissage du jour 2 ne peut pas dépendre des jours 3 et 4.

### Ex MB3.6 — La saturation d'une softmax : trois scores multipliés par un facteur c croissant, le poids maximal, la sensibilité 1 − Σ pᵢ² et la borne (K − 1) e^{−cΔ} ✏️ ★★ ⏱️ 15 min
**Objectif :** mesurer la saturation d'une softmax quand on multiplie ses scores, et comparer à la borne de la fiche.
**Prérequis :** fiche §7 ; M13a (Gini), M17 ($\operatorname{diag}(\mathbf{p}) - \mathbf{p}\mathbf{p}^\top$) · **Parcours :** C, E

Une application propose un itinéraire parmi trois, tiré avec les poids $\operatorname{softmax}(c\,\mathbf{s})$, où les scores des itinéraires valent $\mathbf{s} = (1{,}3 ;\ 0{,}5 ;\ -0{,}8)$ et $c > 0$ règle la confiance de l'application. Ici $K = 3$, et $\Delta$ est l'écart entre le plus grand score et le suivant.

| | Question | Réponse attendue |
|---|---|---|
| a | le plus grand poids $p_{\max}$, pour $c = 1$, 2 et 6 | une liste de 3 nombres (4 décimales) |
| b | la sensibilité $1 - \sum_ip_i^2$, pour $c = 1$, 2 et 6 | une liste de 3 nombres (4 décimales) |
| c | la borne $(K - 1)\,e^{-c\Delta}$ de $1 - p_{\max}$, pour $c = 6$ | un nombre (5 décimales) |
| d | le plus petit $c$ pour lequel la borne garantit $p_{\max} \ge 0{,}99$ | un nombre (2 décimales) |
| e | vrai ou faux : quand $c \to \infty$, $1 - \sum_ip_i^2 \to 0$ | `True` ou `False` |

Dans ta copie : compare $1 - p_{\max}$ à c) pour $c = 6$ ; d) garantit-il que c'est le plus petit $c$ qui convient ?

### Ex MB3.7 — La softmax en ligne à la main : neuf scores (des multiples de ln 2) et leurs valeurs lus par blocs de trois, l'état (m, l, a) après chaque bloc, la moyenne pondérée finale, puis la fusion de deux états calculés séparément ✏️ ★★ ⏱️ 30 min
**Objectif :** faire tourner la softmax en ligne à la main, avec ses remises à l'échelle, puis fusionner deux états.
**Prérequis :** fiche §8 ; M05a (log-sum-exp) · **Parcours :** C, E

Une station reçoit, par paquets de trois, les relevés de neuf balises : chaque relevé a une valeur $v_j$ et un score de fiabilité $s_j = k_j\ln 2$, si bien que $e^{s_j} = 2^{k_j}$. On veut la moyenne des valeurs pondérée par $\operatorname{softmax}(\mathbf{s})$.

| relevé $j$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $k_j = s_j/\ln 2$ | 1 | 3 | 0 | 2 | −1 | 4 | 0 | 4 | 2 |
| valeur $v_j$ | 4 | 10 | 6 | 3 | 8 | 2 | 9 | 5 | 7 |

Un état $(m, l, a)$ s'écrit $[m/\ln 2, l, a]$ : son $m$ est toujours un multiple de $\ln 2$. Le bloc 1 contient les relevés 1 à 3, le bloc 2 les relevés 4 à 6, le bloc 3 les relevés 7 à 9.

| | Question | Réponse attendue |
|---|---|---|
| a | l'état après le bloc 1 | une liste de 3 nombres (valeurs exactes) |
| b | l'état après le bloc 2 | une liste de 3 nombres (valeurs exactes) |
| c | l'état après le bloc 3 | une liste de 3 nombres (valeurs exactes) |
| d | la moyenne pondérée finale $a/l$ | une fraction irréductible |
| e | une machine B lit seule les blocs 2 et 3, en partant de l'état vide : son état final | une liste de 3 nombres (valeurs exactes) |
| f | la fusion de l'état d'une machine A, qui a lu le bloc 1 seul, et de l'état de B | une liste de 3 nombres (valeurs exactes) |
| g | le log-sum-exp des neuf scores, $m + \ln l$ | un nombre (4 décimales) |

Dans ta copie : écris, pour chaque bloc, le facteur de remise à l'échelle ; compare f) à c).

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex MB3.8 — Les formules d'addition par le produit scalaire de deux vecteurs unitaires ; puis R_α R_β = R_{α+β}, R_θ⁻¹ = R_θᵀ = R_{−θ}, et la règle e^{iα}e^{iβ} = e^{i(α+β)} que M22 admettait ∂ ★★ ⏱️ 30 min
**Objectif :** démontrer les quatre formules d'addition sans rien admettre d'autre que la géométrie de R9, puis en tirer le groupe des rotations du plan et la règle des exponentielles.
**Prérequis :** fiche §1 et §2 ; R9 (cercle trigonométrique, parité, produit scalaire et angle, Al-Kashi), M07 ($\lVert\mathbf{u} - \mathbf{v}\rVert^2$) · **Parcours :** C, E

Pour un réel $a$, on note $\mathbf{u}_a = (\cos a, \sin a)$.
1. Soit $a$ et $b$ deux réels, et $\varphi \in [0, \pi]$ l'angle des vecteurs $\mathbf{u}_a$ et $\mathbf{u}_b$. Justifie que $\cos\varphi = \cos(a - b)$. Déduis-en $\cos(a - b) = \cos a\cos b + \sin a\sin b$, en calculant $\mathbf{u}_a\cdot\mathbf{u}_b$ de deux façons.
2. Déduis de 1 les formules de $\cos(a + b)$, de $\sin(a - b)$ et de $\sin(a + b)$. Tu pourras d'abord établir $\cos(\frac\pi2 - x) = \sin x$ et $\sin(\frac\pi2 - x) = \cos x$.
3. Montre que $\mathbf{R}_\alpha\mathbf{R}_\beta = \mathbf{R}_{\alpha + \beta}$ pour tous $\alpha$ et $\beta$, et déduis-en que deux rotations du plan commutent.
4. Montre que $\mathbf{R}_\theta^\top = \mathbf{R}_{-\theta}$, puis que $\mathbf{R}_\theta^\top\mathbf{R}_\theta = \mathbf{I}$ : $\mathbf{R}_\theta^{-1} = \mathbf{R}_\theta^\top = \mathbf{R}_{-\theta}$.
5. Avec la définition $e^{i\theta} = \cos\theta + i\sin\theta$, montre que $e^{i\alpha}e^{i\beta} = e^{i(\alpha + \beta)}$.

**Pour aller plus loin.** Montre que $\det\mathbf{R}_\theta = 1$, et que la duplication $\cos 2a = 2\cos^2a - 1$ découle de 2.

### Ex MB3.9 — Une moyenne pondérée par une softmax sur un ensemble de points commute avec toute renumérotation des points ; un masque triangulaire casse cette équivariance ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'équivariance par permutation d'une moyenne pondérée sur un ensemble de points, et voir sur un contre-exemple ce qui la casse.
**Prérequis :** fiche §3 et §6 ; M16 (matrices de permutation) · **Parcours :** C

Des capteurs $1, \ldots, n$ sont placés en $\mathbf{x}_1, \ldots, \mathbf{x}_n$ et mesurent $\mathbf{y}_1, \ldots, \mathbf{y}_n$, les lignes de $\mathbf{X}$ et de $\mathbf{Y}$. Une fonction $s$ donne le score $s(\mathbf{x}_i, \mathbf{x}_j)$ d'une paire de points ; $\mathbf{S}$ est la matrice de coefficients $S_{ij} = s(\mathbf{x}_i, \mathbf{x}_j)$, $\mathbf{C}$ la matrice dont chaque ligne est la softmax de la ligne correspondante de $\mathbf{S}$, et les sorties sont $\hat{\mathbf{Y}}(\mathbf{X}, \mathbf{Y}) = \mathbf{C}\mathbf{Y}$. $\sigma$ est une permutation de $\{1, \ldots, n\}$, de matrice $\mathbf{P}$ (lignes $\mathbf{e}_{\sigma(1)}^\top, \ldots, \mathbf{e}_{\sigma(n)}^\top$).
1. Montre que, pour un vecteur $\mathbf{s}$ de $\mathbb{R}^n$, $\operatorname{softmax}(\mathbf{P}\mathbf{s}) = \mathbf{P}\operatorname{softmax}(\mathbf{s})$.
2. Montre que la matrice des scores des points renumérotés, ceux de $\mathbf{P}\mathbf{X}$, est $\mathbf{P}\mathbf{S}\mathbf{P}^\top$.
3. Montre que la softmax ligne par ligne de $\mathbf{P}\mathbf{S}\mathbf{P}^\top$ est $\mathbf{P}\mathbf{C}\mathbf{P}^\top$. Déduis-en $\hat{\mathbf{Y}}(\mathbf{P}\mathbf{X}, \mathbf{P}\mathbf{Y}) = \mathbf{P}\,\hat{\mathbf{Y}}(\mathbf{X}, \mathbf{Y})$.
4. On ajoute un masque triangulaire : le capteur $i$ ne regarde que les capteurs $j \le i$ (les autres scores valent $-\infty$). Donne deux capteurs, un score $s$ et des mesures pour lesquels la relation de 3 est fausse quand on échange les deux capteurs.

### Ex MB3.10 — La softmax en ligne est exacte : l'invariant de l'état après chaque bloc, par récurrence ; puis la fusion de deux états est associative et commutative, d'élément neutre (−∞, 0, 0) ∂ ★★ ⏱️ 30 min
**Objectif :** démontrer que la softmax en ligne calcule exactement la moyenne pondérée et le log-sum-exp, puis les propriétés de la fusion qui permettent de partager le calcul.
**Prérequis :** fiche §8 ; R4 (récurrence), M05a (log-sum-exp) · **Parcours :** C, E

Pour un ensemble fini non vide $J$ d'indices dont un score au moins est fini, l'**état** de $J$ est $\operatorname{st}(J) = (m_J, l_J, a_J)$, avec $m_J = \max_{j \in J}s_j$, $l_J = \sum_{j \in J}e^{s_j - m_J}$ et $a_J = \sum_{j \in J}e^{s_j - m_J}v_j$. Les scores sont lus par blocs $\mathcal{B}_1, \mathcal{B}_2, \ldots, \mathcal{B}_N$, et l'état est mis à jour par la règle de la fiche. On suppose que chaque bloc contient au moins un score fini.
1. Soit $J$ et un bloc $\mathcal{B}$ disjoint de $J$. Montre que la mise à jour de $\operatorname{st}(J)$ par $\mathcal{B}$ donne $\operatorname{st}(J \cup \mathcal{B})$.
2. Déduis-en, par récurrence sur $b$, qu'après le bloc $b$ l'état est $\operatorname{st}(\mathcal{B}_1 \cup \cdots \cup \mathcal{B}_b)$. Conclus : à la fin, $a/l = \sum_jp_jv_j$ et $m + \ln l = \ln\sum_je^{s_j}$.
3. Montre que tous les exposants qui apparaissent dans les exponentielles sont négatifs ou nuls.
4. Montre que la fusion de $\operatorname{st}(J_1)$ et de $\operatorname{st}(J_2)$, pour $J_1$ et $J_2$ disjoints, est $\operatorname{st}(J_1 \cup J_2)$. Déduis-en que la fusion de tels états est commutative et associative.
5. Montre que l'état vide $(-\infty, 0, 0)$ est neutre : $(-\infty, 0, 0) \oplus (m, l, a) = (m, l, a)$ pour $m$ fini. Quelle convention sur $e^{-\infty}$ utilises-tu ? Pourquoi la fusion de deux états vides doit-elle être définie à part ?

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex MB3.11 — Pont : à normes égales, les poids d'un noyau gaussien sont une softmax des produits scalaires divisés par h² ; le vérifier sur quatre stations d'un même cercle, et lire 1/h² comme l'échelle des scores 🔗 ★ ⏱️ 20 min
**Objectif :** vérifier sur un exemple que, à normes égales, le noyau gaussien est une softmax des produits scalaires, et lire $\frac{1}{h^2}$ comme l'échelle des scores.
**Prérequis :** fiche §5 et §7 ; M07 (développer $\lVert\mathbf{a} - \mathbf{b}\rVert^2$) · **Parcours :** C, E

Un lac circulaire de rayon 5 km a son centre à l'origine. Quatre pluviomètres sont sur la rive, en $\mathbf{x}_1 = (5, 0)$, $\mathbf{x}_2 = (0, 5)$, $\mathbf{x}_3 = (-3, -4)$ et $\mathbf{x}_4 = (4, -3)$ (en km), et ont relevé 18, 30, 11 et 22 mm de pluie. On prévoit la pluie en un autre point de la rive, $\mathbf{x} = (3, -4)$, par l'estimateur de Nadaraya-Watson à noyau gaussien.

| | Question | Réponse attendue |
|---|---|---|
| a | les produits scalaires $\mathbf{x}\cdot\mathbf{x}_i$, pour $i = 1$ à 4 | une liste de 4 entiers |
| b | les carrés des distances $\lVert\mathbf{x} - \mathbf{x}_i\rVert^2$ | une liste de 4 entiers |
| c | les poids du noyau gaussien, pour $h = 5$ km | une liste de 4 nombres (4 décimales) |
| d | vrai ou faux : ces poids sont $\operatorname{softmax}(\mathbf{x}\cdot\mathbf{x}_i/h^2)$ | `True` ou `False` |
| e | la pluie prévue en $\mathbf{x}$, pour $h = 5$ km | un nombre (2 décimales) |
| f | le plus grand poids pour $h = 2{,}5$ km | un nombre (3 décimales) |
| g | vrai ou faux : l'égalité de d) reste vraie pour un point $\mathbf{x}$ à l'intérieur du lac | `True` ou `False` |

Dans ta copie : dis ce que devient l'échelle des scores quand $h$ est divisé par 2. Dans workbookIA B3, des poids sont aussi la softmax de produits scalaires multipliés par une échelle.

### Ex MB3.12 — MML §3.9 lu : la rotation du plan (3.76), les rotations de l'espace (3.77)–(3.79), la rotation de Givens (3.80)–(3.81) et les propriétés du §3.9.4 ; R₂(θ) écrite comme une rotation de Givens, et deux rotations de l'espace qui ne commutent pas, sur un vecteur choisi 📖 ★★ ⏱️ 30 min
**Objectif :** relire MML §3.9 en anglais avec la fiche, traduire ses matrices dans les notations du chapitre, et vérifier ses affirmations sur tes propres nombres.
**Prérequis :** fiche §2 et §3 · **Parcours :** C

Lis MML §3.9 (*Rotations*) en entier, en suivant le guide de lecture de la fiche. Réponds dans ta copie, en français, avec tes mots (ne recopie pas le livre).
1. En §3.9.1, d'où viennent les deux colonnes de $\mathbf{R}(\theta)$ dans (3.75) et (3.76) ? Le livre les lit sur la figure 3.16 : quelle propriété des rotations du plan ne démontre-t-il pas, et où la fiche la démontre-t-elle ?
2. En §3.9.2, quelle coordonnée chacune des matrices (3.77), (3.78) et (3.79) laisse-t-elle fixe ? Écris $\mathbf{R}_1(\theta)$ et $\mathbf{R}_3(\theta)$ comme des rotations de Givens $\mathbf{R}_{ij}(\theta)$. Montre que $\mathbf{R}_2(\theta) = \mathbf{R}_{13}(-\theta)$, et explique le signe avec la convention du livre (« regarder l'axe depuis sa pointe ») : vers quel vecteur $\mathbf{R}_2(\theta)$ tourne-t-elle $\mathbf{e}_3$ ?
3. En §3.9.3, écris la matrice $\mathbf{R}_{24}(\theta)$ de $\mathbb{R}^5$ par la définition 3.11 : que sont les blocs $\mathbf{I}_{i-1}$, $\mathbf{I}_{j-i-1}$ et $\mathbf{I}_{n-j}$ ? Vérifie que $n = 2$ redonne (3.76).
4. En §3.9.4, laquelle des propriétés découle de ce qu'une rotation est une matrice orthogonale, et comment (fiche §2) ? Le livre dit que des rotations en dimension 3 ou plus ne commutent pas « en général » : donne deux rotations de $\mathbb{R}^4$ qui commutent, puis choisis un vecteur $\mathbf{x}$ de $\mathbb{R}^3$ et calcule $\mathbf{R}_1(\frac\pi2)\mathbf{R}_3(\frac\pi2)\mathbf{x}$ et $\mathbf{R}_3(\frac\pi2)\mathbf{R}_1(\frac\pi2)\mathbf{x}$.
5. Relève cinq expressions anglaises du passage et leur traduction dans la fiche.

L'exercice 3.10 de MML est conseillé : fais-le avec les formules d'addition.

### Ex MB3.13 — Expliquer, avec une caisse tenue dans une monnaie qui change, pourquoi la softmax en ligne donne exactement le résultat du calcul en une fois 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule l'invariant de la softmax en ligne et la remise à l'échelle.
**Prérequis :** fiche §8 ; MB3.7 · **Parcours :** C, E

Une amie tient la caisse d'une association qui voyage : les recettes arrivent dans plusieurs monnaies, et elle tient toujours ses deux registres (le total des parts et le total des montants qu'elles pèsent) dans la monnaie la plus forte rencontrée jusqu'ici ; quand une monnaie plus forte arrive, elle convertit tout. Tu lui as parlé de la softmax en ligne, et elle te demande : « si l'on convertit en route, comment le résultat peut-il être exactement celui du calcul en une fois ? ».

Réponds-lui en 6 à 10 phrases, sans formule : ce que l'état garde (une monnaie de référence, le plus grand score lu, et deux totaux exprimés dans cette monnaie) ; ce qui se passe quand un bloc apporte un score plus grand ; pourquoi une conversion ne perd rien (et pourquoi le rapport des deux totaux ne dépend pas de la monnaie) ; pourquoi on convertit toujours vers la plus forte ; et ce que deviennent deux caisses tenues séparément. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### MB3.E1 — « Comment encoder une variable cyclique comme une heure ou une direction, et pourquoi pas par sa valeur ? » 💼 ★ ⏱️ 10 min
*Fiche §4 · parcours C, E*

« Comment encoder une variable cyclique comme une heure ou une direction, et pourquoi pas par sa valeur ? »

Ta réponse doit dire ce que la valeur brute fait aux distances et à un modèle (23 h et 0 h) ; l'encodage par $(\cos, \sin)$ et sa période ; pourquoi deux coordonnées ; ce que vaut la distance de deux encodages ; ce qu'on fait pour plusieurs périodes (la journée, la semaine, l'année) ; une alternative et ses limites ; et un piège.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/mb3_rotations_attention/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| MB3.14 | La matrice d'une rotation de Givens de ℝⁿ · `givens_rotation` | 🔨 | ★ | 15 | C, E |
| MB3.15 | La softmax en ligne : l'état (m, l, a) de scores et de valeurs lus par blocs, et l'état après chaque bloc · `online_softmax` | 🔨 | ★★ | 35 | C, E |
| MB3.16 | La fusion de deux états de la softmax en ligne · `merge_softmax_states` | 🔨 | ★★ | 25 | C, E |
| MB3.17 | Prédire ce que deviennent les poids et la prévision de Nadaraya-Watson quand la largeur de bande est divisée ou multipliée par 10, puis tracer | 🔮 | ★ | 20 | C, E |
| MB3.18 | La softmax en ligne selon l'ordre et la taille des blocs : le nombre de remises à l'échelle (les états après chaque bloc) pour des scores croissants, décroissants ou mélangés, comparé à H_N − 1, et la mémoire gardée | 🔬 | ★★ | 25 | C |
| MB3.19 | Trois horloges (la journée, la semaine, l'année) : l'encodage d'une date sur trois cercles, un décalage comme trois rotations, et le produit scalaire de deux encodages en fonction de l'écart | 🎨 | ★ | 20 | C, E |
| MB3.20 | Chasse à l'erreur : deux rotations de l'espace composées dans le mauvais ordre, une direction moyenne prise comme la moyenne des angles, une softmax en ligne qui remet l à l'échelle mais pas l'accumulateur | 🐛 | ★ | 25 | C, E |
| MB3.21 | Un test de propriété : la softmax en ligne ne dépend ni de la taille des blocs, ni d'une même permutation des scores et des valeurs, ni d'une constante ajoutée aux scores, et la fusion de trois états est associative | 🛠️ | ★ | 25 | C |
| MB3.22 | Défi : prévoir la production d'une éolienne par Nadaraya-Watson sur l'encodage cyclique de la direction du vent et du jour de l'année, la largeur de bande choisie par validation croisée « un de côté », sous une erreur quadratique moyenne donnée | 🏆 | ★★★ | 35 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les trois 🔨 complètent ta copie `mon_travail/mymath/positional.py` (**mymath :** `positional.py`), dont la docstring du module dit ce qui est permis : NumPy et le module `math`, mais aucune fonction de SciPy (`scipy.special.softmax`, `scipy.special.logsumexp`, `scipy.spatial.transform.Rotation`) ni `np.logaddexp` : les tests comparent tes résultats avec elles ; des indices de coordonnées à partir de 0 ; ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de sa fonction dans `tests/test_mb3_positional.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.positional.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier (le bras, les rotations de MB3.2, les vents, les stations, le bassin, les itinéraires, les balises, les pluviomètres) sont recopiées dans une cellule du notebook.

**MB3.14 · 🔨 `givens_rotation(n, i, j, theta)`.** Écris la fonction, en suivant sa docstring : contrôle $n$ (un entier $\ge 2$, ni un booléen ni un flottant comme `3.0`), $i$ et $j$ (deux entiers différents de $[0, n - 1]$) et $\theta$ (un réel fini, pas un booléen) ; pars de `np.eye(n)` et change les quatre coefficients du plan $(i, j)$. Lance le groupe de tests. Ensuite : a) les deux vecteurs de MB3.2 a) et b), avec `givens_rotation(3, 1, 2, np.pi / 2)` pour $\mathbf{R}_{23}(\frac\pi2)$ et `givens_rotation(3, 0, 1, np.pi / 3)` pour $\mathbf{R}_{12}(\frac\pi3)$ (une liste de 6 nombres, à comparer à ta copie) ; b) écris la matrice (3.78) de MML pour $\theta = 0{,}4$, puis cherche le couple $(i, j)$ tel que `givens_rotation(3, i, j, 0.4)` lui est égale (une liste de 2 entiers) ; c) la norme de Frobenius de $\mathbf{G}\mathbf{H} - \mathbf{H}\mathbf{G}$ pour `G = givens_rotation(5, 0, 2, 0.9)` et `H = givens_rotation(5, 2, 4, -0.6)`, puis pour le même `G` et `givens_rotation(5, 1, 3, -0.6)` (une liste de 2 nombres). Ce qu'il faut regarder : pourquoi le couple de b) n'est-il pas $(0, 2)$ ? Qu'ont en commun les plans des deux rotations qui ne commutent pas ?

**MB3.15 · 🔨 `online_softmax(scores, values=None, block_size=1, history=False)`.** Écris la fonction, en suivant sa docstring : contrôle les scores (un tableau 1-D non vide de réels, $-\infty$ permis, ni `nan` ni $+\infty$), les valeurs ($n$ lignes, 1-D ou 2-D, finies), `block_size` (un entier $\ge 1$, pas un booléen) et `history` (un booléen) ; pars de l'état vide ; pour chaque bloc, saute-le si tous ses scores valent $-\infty$, sinon calcule le nouveau maximum, le facteur $e^{m - m'}$ et les poids $e^{s_j - m'}$ du bloc, puis mets $l$ et l'accumulateur à jour ; avec `history=True`, garde une copie de l'état après chaque bloc. Rends des `float` Python (et un `float` pour `acc` quand les valeurs sont 1-D). Lance le groupe de tests. Ensuite : a) les neuf balises de MB3.7, par blocs de 3 avec `history=True` : les trois états, avec $m$ divisé par $\ln 2$ (une liste de 9 nombres), puis vrai ou faux, ils sont égaux à tes réponses a) à c) de MB3.7 à $10^{-12}$ près ; b) vrai ou faux : l'état final est le même, à $10^{-12}$ près, pour des blocs de 1, 2, 3, 4 et 9 ; c) pour les scores $(-1\,203{,}5 ;\ -1\,201 ;\ -1\,204{,}2 ;\ -1\,202{,}5)$ : $m + \ln l$, puis ce que rend `np.log(np.sum(np.exp(s)))` ; d) quatre relevés de vent, de directions 300°, 330°, 20° et 70° et de scores de fiabilité $(0{,}8 ;\ 0 ;\ 1{,}2 ;\ -0{,}4)$, encodés par $(\cos, \sin)$ : avec ces encodages comme valeurs 2-D et des blocs de 2, la moyenne pondérée $a/l$ (2 nombres), puis sa direction en degrés dans $[0, 360[$. Ce qu'il faut regarder : combien de fois $m$ change-t-il dans a), et à quels blocs ? Pourquoi le calcul direct de c) échoue-t-il, et pas le tien ? Que vaudrait, pour d), la moyenne des quatre angles ?

**MB3.16 · 🔨 `merge_softmax_states(state1, state2)`.** Écris la fonction, en suivant sa docstring : contrôle les deux états (des triplets ; $m$ réel ou $-\infty$ ; $l$ fini, $\ge 1$ quand $m$ est fini ; $l = 0$ et `acc` nul ou `None` quand $m = -\infty$ ; des `acc` de même nature et de même longueur) ; deux états vides donnent l'état vide ; sinon, remets chaque état à l'échelle du maximum commun et additionne. Rends un nouveau tableau, sans modifier les arguments. Lance le groupe de tests. Ensuite : a) les balises de MB3.7 : l'état $A$ du bloc 1, l'état $B$ des blocs 2 et 3, chacun par `online_softmax`, et leur fusion, à comparer à ta réponse f) de MB3.7 ; puis vrai ou faux, cette fusion égale l'état final de MB3.15 a) à $10^{-12}$ près ; b) le notebook fournit `S_16` et `V_16`, douze scores et douze valeurs de longueur 2 : coupe-les en quatre morceaux de 2, 5, 1 et 4 scores, calcule leurs états, puis vrai ou faux, les groupements $(A \oplus B) \oplus (C \oplus D)$, $A \oplus (B \oplus (C \oplus D))$ et $(D \oplus C) \oplus (B \oplus A)$ égalent tous `online_softmax(S_16, V_16, block_size=5)` à $10^{-12}$ près, et la moyenne pondérée (2 nombres) ; c) vrai ou faux : l'état vide `(-np.inf, 0.0, np.zeros(2))` est neutre pour l'état $A$ de b), des deux côtés. Ce qu'il faut regarder : quel grand calcul ces égalités permettent-elles de partager, et entre quoi ?

**MB3.17 · 🔮 Prédire puis tracer l'effet de la largeur de bande.** Le notebook fournit `X_17` et `Y_17`, les altitudes (en km, de 1,0 à 2,6) et les températures de midi de 24 stations d'un massif. On prévoit la température en une altitude $x$ par Nadaraya-Watson à noyau gaussien, avec une largeur de bande de référence $h = 0{,}25$ km, puis $h/10 = 0{,}025$ km et $10h = 2{,}5$ km. **Avant d'exécuter**, prédis : a) quand $h$ est divisé par 10, le plus grand poids à 1,85 km : (A) proche de 1 ; (B) proche de $\frac{1}{24}$ ; (C) à peu près le même qu'avec $h$ ; b) quand $h$ est multiplié par 10, la courbe des prévisions de 1,0 à 2,6 km : (A) elle passe près de chaque station, en dents de scie ; (B) elle est presque plate, près de la moyenne des températures ; (C) c'est la droite qui suit la baisse de la température avec l'altitude ; c) quand $h$ est divisé par 10, l'erreur quadratique moyenne de la prévision aux altitudes des stations elles-mêmes : (A) proche de 0 ; (B) proche de celle obtenue avec $h$ ; (C) plus grande qu'avec $h$. Puis écris `nw_predict_17(x, X, Y, h)` (la prévision en un tableau d'altitudes `x`, par une softmax stable) et `draw_bandwidths_17(ax, X, Y, hs)`, qui trace les stations et une courbe de prévision par largeur de `hs` sur une grille de 1,0 à 2,6 km, dans les axes reçus, avec une légende et des noms d'axes, et rend la liste des courbes tracées. Relève, pour $h = 0{,}025$ ; $0{,}25$ ; $2{,}5$ km : d) le plus grand poids à 1,85 km ; e) la prévision à 1,85 km ; f) l'erreur quadratique moyenne aux stations ; g) l'amplitude (le maximum moins le minimum) de la courbe sur une grille de 321 altitudes de 1,0 à 2,6 km (chaque fois une liste de 3 nombres). La vérification essaie aussi tes fonctions sur d'autres stations et d'autres largeurs. Ce qu'il faut regarder (après l'expérience) : à quoi ressemblent les trois courbes, et laquelle choisirais-tu ? Que dit d) sur la température du modèle ?

**MB3.18 · 🔬 Les remises à l'échelle selon l'ordre et la taille des blocs.** Le notebook fournit `S_18`, 600 scores, et `V_18`, leurs valeurs, de forme $(600, 3)$. Une remise à l'échelle a lieu quand $m$ change d'un état au suivant (après le premier bloc). Écris `count_rescalings_18(states)`, qui la compte sur une liste d'états rendue par `online_softmax(..., history=True)`. Pour des blocs de $B = 1$, 6 et 60 scores (soit $N = 600$, 100 et 10 blocs), relève : a) le nombre de remises à l'échelle quand les scores sont lus en ordre croissant ; b) en ordre décroissant ; c) leur moyenne sur 300 ordres tirés au hasard par `rng = np.random.default_rng(7318)` (un `rng.permutation(600)` par ordre, la même pour les trois tailles de blocs, les valeurs permutées avec leurs scores) ; d) $H_N - 1$ pour chaque $N$ ; e) le nombre de flottants que la lecture garde à la fois : l'état ($2 + 3$ nombres) et un bloc ($B$ scores et $B$ valeurs de longueur 3), à comparer aux $600 \times 4$ d'une lecture qui garde tout ; f) vrai ou faux : les neuf états finaux (trois ordres, trois tailles) sont égaux à $10^{-12}$ près. Trace c) et d) en fonction de $N$, en abscisse logarithmique. Ce qu'il faut regarder : comment la moyenne de c) grandit-elle avec $N$ ? Qu'est-ce que l'ordre change, et qu'est-ce qu'il ne change pas ?

**MB3.19 · 🎨 Trois horloges : la journée, la semaine, l'année.** Une date est repérée par $t$, le nombre d'heures écoulées depuis le lundi 1ᵉʳ janvier à 0 h d'une année de 365 jours. Elle est encodée par trois horloges de périodes 24 h, 168 h et 8 760 h, de pulsations $\omega_k = 2\pi/\tau_k$ : `encode_19(t)` rend les six nombres $(\cos\omega_1t, \sin\omega_1t, \cos\omega_2t, \sin\omega_2t, \cos\omega_3t, \sin\omega_3t)$. Écris `encode_19(t)`, puis `draw_clocks_19(axes, times, labels, shift)`, qui reçoit une ligne de trois axes (une horloge par axe) et y trace le cercle unité, le point de chaque date de `times` avec son nom (pris dans `labels`), une même échelle sur les deux axes, et une flèche de la première date à cette date décalée de `shift` heures ; puis `draw_dot_curve_19(ax, deltas)`, qui trace $\mathbf{E}(0)\cdot\mathbf{E}(\delta)$ en fonction de l'écart $\delta$, en jours sur l'axe des abscisses. Les fonctions dessinent dans les axes reçus et rendent les tableaux tracés. La vérification appelle `draw_clocks_19` avec le 3 mars à 8 h ($t = 1\,472$), le 3 mars à 20 h, le 10 mars à 8 h et le 3 septembre à 8 h, et un décalage de 30 h, puis `draw_dot_curve_19` avec $\delta = 0, 1, \ldots, 8\,760$ h. Relève : a) `encode_19(1472)` (6 nombres) ; b) $\mathbf{E}(0)\cdot\mathbf{E}(\delta)$ pour $\delta = 12$, 84, 4 380 et 8 760 h (4 nombres) ; c) l'écart $\delta \in \{1, \ldots, 8\,760\}$ (en heures entières) où ce produit scalaire est le plus grand, puis sa valeur ; d) vrai ou faux : `encode_19(1472 + 30)` égale $\mathbf{M}$ fois `encode_19(1472)` à $10^{-12}$ près, où $\mathbf{M}$ est le produit des trois rotations `givens_rotation(6, 0, 1, 30 * w[0])`, `givens_rotation(6, 2, 3, 30 * w[1])` et `givens_rotation(6, 4, 5, 30 * w[2])`. Ce qu'il faut regarder : quelle horloge sépare le 3 mars à 8 h du 3 mars à 20 h ? Et du 3 septembre ? Pourquoi le produit scalaire ne revient-il pas à 3 après un an exactement, et quand s'en approche-t-il ?

**MB3.20 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `rotate_e3_then_e1(x, alpha, beta)` doit tourner $\mathbf{x}$ d'abord de $\alpha$ autour de $\mathbf{e}_3$, puis de $\beta$ autour de $\mathbf{e}_1$ ; elle rend `R12(alpha) @ R23(beta) @ x`, où `R12` et `R23` sont ces deux rotations. Il l'a vérifiée avec $\alpha = \beta = \pi$.
- (2) `mean_direction_bad(angles)` doit rendre la direction moyenne de directions données en degrés, dans $[0, 360[$ ; elle rend `np.mean(angles) % 360`. Il l'a vérifiée sur les relevés 40°, 60° et 80°.
- (3) `online_softmax_bad(scores, values, block_size)` doit rendre l'état de la softmax en ligne ; quand le maximum change, elle remet $l$ à l'échelle, mais pas l'accumulateur. Il l'a vérifiée en comparant $a/l$ à la moyenne pondérée calculée en une fois, pour des scores rangés en ordre décroissant.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `rotate_e3_then_e1_fixed`, `mean_direction_fixed` et `online_softmax_fixed`, avec les mêmes arguments), puis réponds : a) pour $\mathbf{x} = (2, 0, 1)$, $\alpha = \frac\pi6$ et $\beta = \frac\pi2$ : le résultat de la fonction corrigée, puis de la fonction fautive (une liste de 6 nombres) ; b) la direction moyenne des relevés 340°, 10°, 25° et 355°, par la fonction corrigée, puis par la fonction fautive ; c) pour les scores $(0{,}4 ;\ 2 ;\ 1{,}1 ;\ 3{,}2 ;\ -0{,}5 ;\ 2{,}7)$, les valeurs $(5, 1, 4, 2, 6, 3)$ et des blocs de 2 : $a/l$ par la fonction corrigée, puis par la fonction fautive. Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : d'autres angles et d'autres vecteurs, des directions de part et d'autre de 0°, des scores dans un ordre quelconque et des valeurs 2-D.

**MB3.21 · 🛠️ Un test de propriété.** Le notebook fournit la boucle du test, `softmax_property_test_21(n_trials, rng, func=None, merge=None, rtol=1e-9, checks=None)` : quand `func` vaut `None`, elle prend `mymath.positional.online_softmax` **au moment de l'appel**, quand `merge` vaut `None`, `mymath.positional.merge_softmax_states`, et, quand `checks` vaut `None`, ta fonction `failed_checks_21`. Pour chacun des `n_trials` essais, dans cet ordre, elle tire `n = int(rng.integers(3, 13))`, `scores = rng.normal(0, 3, n)`, puis, si `rng.random() < 0.3`, met à $-\infty$ les scores où `rng.random(n) < 0.25` et redonne au score d'indice `int(rng.integers(n))` la valeur `float(rng.normal(0, 3))` ; puis `values = rng.normal(0, 1, (n, 2))`, `block_size = int(rng.integers(1, n + 1))`, `perm = rng.permutation(n)`, `shift = float(rng.normal(0, 20))` et deux coupures `i < j` tirées par `sorted(rng.choice(np.arange(1, n), 2, replace=False))` ; elle appelle `checks(scores, values, block_size, perm, shift, (i, j), f, m, rtol)`, où `f` et `m` sont les fonctions testées, et ajoute 1 au compteur de chaque nom rendu ; elle rend le dictionnaire des quatre compteurs `"blocks"`, `"permutation"`, `"shift"` et `"associative"`. Écris les contrôles, `failed_checks_21(scores, values, block_size, perm, shift, cuts, func, merge, rtol=1e-9)`, qui rend l'ensemble des noms des contrôles qui échouent, avec `ref = func(scores, values, block_size=1)` : `"blocks"` échoue si l'état lu par blocs de `block_size` diffère de `ref` ; `"permutation"` si l'état de `scores[perm]` et `values[perm]`, lu par blocs de 1, diffère de `ref` ; `"shift"` si l'état de `scores + shift`, lu par blocs de 1, diffère de $(m + \text{shift}, l, a)$, où $(m, l, a)$ = `ref` ; `"associative"` si, avec les états des trois morceaux `scores[:i]`, `scores[i:j]` et `scores[j:]` (et de leurs valeurs), lus par `func` avec des blocs de 1, `merge(merge(A, B), C)` diffère de `merge(A, merge(B, C))`. Deux états « diffèrent » si leurs $m$ ne sont pas tous deux $-\infty$ et s'écartent de plus de $\texttt{rtol}\cdot\max(1, \lvert m\rvert)$, si leurs $l$ s'écartent de plus de $\texttt{rtol}\cdot\max(1, l)$, ou si leurs accumulateurs ne sont pas égaux par `np.allclose(rtol=rtol, atol=rtol * max(1, abs(acc).max()))`. Une exception levée fait échouer les quatre contrôles. Le notebook fournit aussi quatre versions fausses : `rescale_l_only` (la softmax en ligne du 🐛 MB3.20), `centered` (une softmax en ligne qui retranche d'abord aux scores la moyenne des scores finis), `merge_no_rescale` (une fusion qui additionne les $l$ et les accumulateurs sans les remettre à l'échelle) et `merge_mean` (une fusion qui fait la moyenne des deux états remis à l'échelle au lieu de leur somme). a) Avec `rng = np.random.default_rng(7321)` et 200 essais, avec les bonnes fonctions et tes contrôles : vrai ou faux, les quatre compteurs sont nuls ; b) avec le même départ et chacune des quatre versions fausses (les deux premières pour `func`, les deux dernières pour `merge`) : les quatre compteurs, dans l'ordre `"blocks"`, `"permutation"`, `"shift"`, `"associative"` (un nouveau `default_rng(7321)` chaque fois) ; c) lesquelles passent un contrôle, ou tous, et pourquoi c'est normal : qu'est-ce qui, dans le dépôt, vérifie ce qu'elles ont de faux ? La vérification lance aussi ton test sur deux départs cachés de 40 essais, avec les bonnes fonctions (compteurs nuls) et avec des versions fausses cachées, dont une qui lève une erreur sur des scores tous égaux à $-\infty$ et une qui se trompe seulement sur des valeurs 2-D ; elle remplace aussi un instant `mymath.positional.online_softmax` par l'une d'elles, pour l'appel sans `func`. Ce qu'il faut retenir : chaque contrôle attrape certaines erreurs et en laisse passer d'autres ; un test se juge aux erreurs qu'il attrape, et à celles qu'il ne peut pas attraper.

**MB3.22 · 🏆 Défi : la production d'une éolienne.** Une éolienne reçoit surtout un vent dominant venu des directions proches de 0°, qui souffle le plus fort en hiver. Le notebook fournit `TRAIN_22`, 400 relevés de l'année passée, de forme $(400, 3)$ : la direction d'où vient le vent $\theta$ (en degrés, de 0 à 360 ; 0° et 360° sont la même direction), le jour de l'année $d$ (de 0 à 365) et la production moyenne de l'heure $y$ (en kW) ; et `TEST_22`, de forme $(400, 2)$, les directions et les jours de 400 heures à prévoir, autour du nouvel an, par vent dominant. Écris `predict_22(train, test)`, qui rend 400 prévisions par Nadaraya-Watson à noyau gaussien sur l'encodage cyclique des deux variables, $(\cos\theta, \sin\theta, \cos\frac{2\pi d}{365}, \sin\frac{2\pi d}{365})$, avec une largeur de bande choisie par validation croisée « un de côté » (fiche §5) sur une grille d'une trentaine de valeurs en progression géométrique, par exemple de 0,03 à 1,5. Tout NumPy et SciPy sont permis. La cellule fournie donne aussi `mse_22(predictions)`, qui rend l'erreur quadratique moyenne de 400 prévisions de `TEST_22` par rapport à la production moyenne attendue, sans montrer la loi cachée. **Critère de réussite :** sur `TEST_22`, et sur trois jeux cachés tirés à nouveau à chaque exécution (une autre éolienne du même type, ses relevés et ses heures à prévoir), une erreur quadratique moyenne au plus 1,3 fois celle de la méthode de la vérification (Nadaraya-Watson sur le même encodage, sa largeur choisie sur 30 valeurs de 0,03 à 1,5) sur le même jeu, en moins de 10 secondes en tout. Relève : a) la largeur de bande que choisit ta validation croisée sur `TRAIN_22` ; b) `mse_22` de tes prévisions ; c) `mse_22` de la même méthode appliquée aux nombres bruts $(\theta, d)$, sa largeur choisie de la même façon, sur une grille de 1 à 200 ; d) la largeur que choisirait ta validation croisée si tu ne laissais pas chaque relevé de côté. Point de départ : regarde où sont les heures à prévoir, et ce que deviennent 359° et 1°, ou le jour 364 et le jour 0, dans chaque représentation.
