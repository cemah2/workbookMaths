# M02c · Échantillons et estimation — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m02c_echantillons_estimation/06_mes_reponses.md` (créée par `python tools/start_chapter.py M02c`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, ⚖️, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Pour les quantiles d'une série, utilise la convention de la fiche (§1 : position $p(n - 1)$ dans la série triée, numérotée à partir de 0, puis interpolation linéaire) ; pour la loi normale, la table de $\Phi$ de M02b (§3) ; et dis toujours si tu divises par $n$ ou par $n - 1$.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M02c.Q1 — Résumer une série : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Vrai ou faux ?
1. La médiane d'une série est toujours l'une des valeurs de la série.
2. Si l'on ajoute 10 à toutes les valeurs d'une série, sa variance augmente de 10.
3. Si l'on multiplie toutes les valeurs par 3, l'écart-type est multiplié par 3.
4. Dans une série de 11 valeurs, changer une seule valeur peut déplacer la moyenne aussi loin qu'on veut, mais pas la médiane.
5. La somme des écarts à la moyenne, $\sum_i (x_i - \bar{x})$, vaut toujours 0.
6. L'écart interquartile d'une série peut être plus grand que son étendue (le maximum moins le minimum).

### M02c.Q2 — z-scores et valeurs aberrantes 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. Une valeur a un z-score de $-1{,}5$. Que dit ce nombre de sa position ?
2. Après standardisation, quelles sont la moyenne et l'écart-type d'une colonne ?
3. $Q_1 = 20$ et $Q_3 = 30$ : quelles sont les deux barrières de Tukey ?
4. Vrai ou faux : dans une série de 8 valeurs, une valeur énorme a forcément un z-score supérieur à 3.
5. Pourquoi la règle de Tukey résiste-t-elle mieux que la règle du z-score à une grosse valeur aberrante ?
6. Vrai ou faux : on standardise le jeu de test avec la moyenne et l'écart-type du jeu de test.

### M02c.Q3 — i.i.d. ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Pour chaque série, peut-on raisonnablement la modéliser comme un échantillon i.i.d. ? Si non, quelle(s) hypothèse(s) tombe(nt) : l'indépendance, la même loi, ou les deux ?
1. Les résultats de 100 lancers d'un dé.
2. La température à midi, pendant 30 jours consécutifs.
3. 10 cartes tirées sans remise d'un jeu de 52 cartes.
4. 1 000 personnes tirées au hasard, sans remise, parmi les 60 millions d'habitants d'un pays.
5. Un dataset de reconnaissance faciale : 10 photos de chacune de 200 personnes.
6. Vrai ou faux : dans un tirage sans remise, le deuxième tirage n'a pas la même loi que le premier.

### M02c.Q4 — Grands nombres et TCL : ce qu'ils disent, ce qu'ils ne disent pas 🧠 ★ ⏱️ 4 min
*Fiche §4 et §5 · parcours C, E*

1. Vrai ou faux : après 10 « pile » de suite avec une pièce équilibrée, « face » est plus probable au lancer suivant.
2. On passe de $n = 100$ à $n = 10\,000$ tirages : par combien l'écart-type de la moyenne est-il divisé ?
3. Vrai ou faux : d'après le théorème central limite, l'histogramme de 10 000 tirages d'une loi exponentielle a la forme d'une cloche.
4. Une loi a pour espérance 5 et pour écart-type 2. Quelle est la loi approchée de la moyenne de 100 tirages ?
5. Vrai ou faux : pour toute loi qui a une variance, $P(\lvert X - \mu \rvert \ge 2\sigma) \le 0{,}25$.
6. Vrai ou faux : la loi des grands nombres s'applique à n'importe quelle loi.

### M02c.Q5 — Biais, variance et ddof 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Un estimateur sans biais donne-t-il la bonne valeur sur chaque échantillon ?
2. Un estimateur a un biais de 2 et une variance de 5 : quelle est son erreur quadratique moyenne ?
3. Par quoi `np.var(x)` divise-t-il la somme des carrés des écarts ? Et `np.var(x, ddof=1)` ?
4. Pour $n = 4$ valeurs, par quel nombre faut-il multiplier $s_n^2$ pour obtenir $s^2$ ?
5. Vrai ou faux : entre deux estimateurs d'un même paramètre, on préfère toujours celui qui est sans biais.
6. Vrai ou faux : quand $n$ grandit, l'écart entre $s_n^2$ et $s^2$ devient négligeable.

### M02c.Q6 — Lire un intervalle de confiance 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Sur $n = 200$ sessions d'utilisateurs, l'intervalle de confiance à 95 % de la durée moyenne d'une session est $[12{,}1 ;\ 13{,}5]$ minutes.
1. « Il y a 95 % de chances que la vraie durée moyenne soit entre 12,1 et 13,5 minutes. » Cette phrase est-elle correcte ?
2. « 95 % des sessions durent entre 12,1 et 13,5 minutes. » Cette phrase est-elle correcte ?
3. Que vaut la durée moyenne des 200 sessions ?
4. Que vaut, environ, l'erreur type de cette moyenne ?
5. Avec 800 sessions au lieu de 200 (et à peu près la même dispersion), quelle serait la demi-largeur de l'intervalle ?
6. L'intervalle à 99 % calculé sur les mêmes 200 sessions est-il plus large ou plus étroit ?

### M02c.Q7 — Covariance et corrélation : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

1. Une corrélation de $-0{,}9$ indique une relation linéaire plus faible qu'une corrélation de $0{,}5$.
2. $\operatorname{Cov}(X, X) = \mathbb{V}(X)$.
3. Si $\operatorname{Cov}(X, Y) = 3$, alors $\operatorname{Cov}(2X, Y) = 6$.
4. $\mathbb{V}(X - Y) = \mathbb{V}(X) - \mathbb{V}(Y)$.
5. Chez les élèves d'une école primaire, la pointure et le score à un test de lecture sont corrélés à 0,6 ; donc avoir de grands pieds aide à lire.
6. Une matrice de covariance de 4 variables contient 16 nombres. Combien, au plus, sont différents ?

<a id="rappels"></a>

## 🔁 Rappels

### M02c.R1 — Espérance et variance d'une somme (M02b) 🔁 ★ ⏱️ 5 min
*Fiche §4 et §6 · parcours C, E*

$X$ et $Y$ sont indépendantes, avec $\mathbb{E}[X] = 3$, $\mathbb{V}(X) = 4$, $\mathbb{E}[Y] = -1$, $\mathbb{V}(Y) = 9$.
1. $\mathbb{E}[X + Y]$ et $\mathbb{V}(X + Y)$ ?
2. $\mathbb{V}(X - Y)$ ?
3. $\mathbb{V}(3X)$ et $\sigma(3X)$ ?
4. $X_1, \ldots, X_{25}$ sont indépendantes et de même loi que $X$ : espérance et variance de leur moyenne ?

### M02c.R2 — Loi normale et fonction Φ (M02b) 🔁 ★ ⏱️ 5 min
*Fiche §5 et §7 · parcours C, E*

$Z$ suit $\mathcal{N}(0, 1)$ ; utilise la table de $\Phi$ de M02b (§3).
1. $P(Z \le 1{,}96)$ ?
2. $P(-1{,}96 \le Z \le 1{,}96)$ ?
3. $X \sim \mathcal{N}(80, 6^2)$ : $P(X \le 89)$ ?
4. Le nombre $z > 0$ tel que $P(-z \le Z \le z) = 0{,}90$ ?
5. $P(Z > 2{,}33)$ ?

### M02c.R3 — Racines et puissances (R1) 🔁 ★ ⏱️ 5 min
*Fiche §7 · parcours C*

1. $\sqrt{64}$ et $\sqrt{0{,}0144}$ ?
2. $\frac{12}{\sqrt{36}}$ ?
3. Si $n$ est multiplié par 9, par combien $\sqrt{n}$ est-il multiplié ? Et $\frac{1}{\sqrt{n}}$ ?
4. Écris $\sqrt{\frac{2}{9}}$ sous la forme $\frac{\sqrt{a}}{b}$.
5. Résous $\frac{6}{\sqrt{n}} = 0{,}5$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/9"` ;
- une liste entre crochets, comme `[0.25, 0.75]` ; vrai ou faux par `True` ou `False` ; une lettre entre guillemets, comme `"B"`.

### Ex M02c.1 — Les statistiques d'une petite série : moyenne, médiane, quartiles, variance ✏️ ★ ⏱️ 20 min
**Objectif :** calculer à la main les statistiques descriptives d'une série, avec les deux variances et les quartiles de la convention de la fiche.
**Prérequis :** fiche §1 ; R4 (Σ) · **Parcours :** C, E

Un modèle de langage a produit 8 résumés ; leurs longueurs, en mots, sont :

$$42,\ 38,\ 51,\ 45,\ 40,\ 47,\ 39,\ 58.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne $\bar{x}$ | un nombre (2 décimales) |
| b | la médiane | un nombre (2 décimales) |
| c | la somme des carrés des écarts à la moyenne, $\sum_i (x_i - \bar{x})^2$ | un entier |
| d | la variance divisée par $n$, $s_n^2$ | un nombre (2 décimales) |
| e | la variance divisée par $n - 1$, $s^2$ | un nombre (3 décimales) |
| f | le premier quartile $Q_1$ (convention de la fiche) | un nombre (2 décimales) |
| g | le troisième quartile $Q_3$ | un nombre (2 décimales) |
| h | l'écart interquartile | un nombre (2 décimales) |

Dans ta copie : vérifie que la somme des écarts à la moyenne est nulle, et recalcule d) par la formule $s_n^2 = \overline{x^2} - \bar{x}^2$. Laquelle des deux méthodes est la plus sûre à la main ?

### Ex M02c.2 — z-scores, écart interquartile et valeurs aberrantes ✏️ ★ ⏱️ 15 min
**Objectif :** juger une valeur suspecte par son z-score et par la règle de Tukey, et voir l'effet de masque.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

La consommation d'un serveur, en kWh par jour, sur 10 jours :

$$12,\ 14,\ 13,\ 15,\ 14,\ 16,\ 13,\ 15,\ 14,\ 31.$$

Dans tout l'exercice, l'écart-type est celui qui divise par $n$ ($s_n$).

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne | un nombre (1 décimale) |
| b | l'écart-type $s_n$ | un nombre (3 décimales) |
| c | le z-score de 31 | un nombre (2 décimales) |
| d | la règle $\lvert z \rvert > 3$ signale-t-elle 31 ? | `True` ou `False` |
| e | le premier quartile $Q_1$ (convention de la fiche) | un nombre (2 décimales) |
| f | la barrière haute de Tukey, $Q_3 + 1{,}5\,\text{EI}$ | un nombre (3 décimales) |
| g | la règle de Tukey signale-t-elle 31 ? | `True` ou `False` |
| h | le z-score de 31 calculé avec la moyenne et l'écart-type ($s_n$) des **9 autres** valeurs | un nombre (1 décimale) |

Dans ta copie : pourquoi c) et h) sont-ils si différents ? Avec 10 valeurs, quel est le plus grand z-score possible (fiche §2) ?

### Ex M02c.3 — Imputer par la moyenne ou la médiane : ce qui change ✏️ ★ ⏱️ 15 min
**Objectif :** mesurer ce qu'une imputation fait à la moyenne, à la médiane et à la dispersion d'une série.
**Prérequis :** fiche §1 et §9 · **Parcours :** C

On demande à 8 utilisateurs combien d'heures de vidéo ils ont regardées la semaine dernière. Six répondent :

$$4,\ 6,\ 7,\ 9,\ 10,\ 24,$$

et deux ne répondent pas. Les variances divisent par le nombre de valeurs ($s_n^2$).

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne des 6 réponses | un nombre (2 décimales) |
| b | la médiane des 6 réponses | un nombre (2 décimales) |
| c | la variance des 6 réponses | un nombre (2 décimales) |
| d | on impute les 2 valeurs manquantes par la moyenne : moyenne des 8 valeurs | un nombre (2 décimales) |
| e | variance des 8 valeurs après cette imputation | un nombre (2 décimales) |
| f | l'écart-type après imputation divisé par l'écart-type avant | un nombre (3 décimales) |
| g | on impute plutôt par la médiane : moyenne des 8 valeurs | un nombre (2 décimales) |
| h | médiane des 8 valeurs après imputation par la médiane | un nombre (2 décimales) |

Dans ta copie : retrouve e) et f) par la formule de la fiche, sans recalculer la somme des carrés. Laquelle des deux imputations choisirais-tu ici, et pourquoi ? Les deux personnes qui n'ont pas répondu regardent-elles autant de vidéos que les autres ?

### Ex M02c.4 — Avec ou sans remise : la variance de la moyenne ✏️ ★★ ⏱️ 20 min
**Objectif :** comparer la variance de la moyenne d'un échantillon tiré avec et sans remise, et calculer le facteur de correction de population finie.
**Prérequis :** fiche §3 ; M02b §6 · **Parcours :** C

Une urne contient 5 boules, numérotées $2, 4, 6, 8, 10$. On en tire $n = 2$ au hasard, l'une après l'autre : $X_1$ est le numéro de la première, $X_2$ celui de la seconde, et $\bar{X} = \frac{X_1 + X_2}{2}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la variance $\sigma^2$ de la population (divisée par $N = 5$) | un entier |
| b | $\mathbb{V}(\bar{X})$ pour deux tirages **avec** remise | un entier |
| c | sans remise, le nombre de paires de boules possibles (sans tenir compte de l'ordre) | un entier |
| d | sans remise, $\mathbb{E}[\bar{X}]$ | un entier |
| e | sans remise, $\mathbb{V}(\bar{X})$ | un entier |
| f | sans remise, $\operatorname{Cov}(X_1, X_2)$ | un entier |
| g | $\mathbb{V}(\bar{X})$ sans remise divisée par $\mathbb{V}(\bar{X})$ avec remise | une fraction irréductible |
| h | le facteur $\frac{N - n}{N - 1}$ pour un sondage de $n = 100$ personnes dans une population de $N = 10\,000$ | un nombre (4 décimales) |

Dans ta copie : vérifie e) en écrivant les paires de c) et la moyenne de chacune, puis en calculant directement la variance de ces moyennes. Que dit h) sur un sondage dans une grande population ?

### Ex M02c.5 — Combien d'observations pour une moyenne précise à 1 % ? ✏️ ★★ ⏱️ 20 min
**Objectif :** relier la taille de l'échantillon à la précision de la moyenne, avec le théorème central limite puis avec l'inégalité de Bienaymé-Tchebychev.
**Prérequis :** fiche §4, §5 et §7 · **Parcours :** C, E

La consommation électrique d'un modèle pendant une inférence varie d'une mesure à l'autre, avec un écart-type $\sigma = 2$ W, autour d'une moyenne $\mu$ inconnue, voisine de 50 W. On fait $n$ mesures indépendantes et on veut estimer $\mu$ **à 1 % près**, c'est-à-dire à $\pm 0{,}5$ W.

| | Question | Réponse attendue |
|---|---|---|
| a | l'écart-type de $\bar{X}$ pour $n = 16$ | un nombre (2 décimales) |
| b | la demi-largeur de l'intervalle à 95 % pour $n = 16$ | un nombre (2 décimales) |
| c | le plus petit $n$ pour lequel la demi-largeur à 95 % est au plus 0,5 W | un entier |
| d | pour ce $n$, la borne de Bienaymé-Tchebychev sur $P(\lvert \bar{X} - \mu \rvert \ge 0{,}5)$ | un nombre (3 décimales) |
| e | le plus petit $n$ pour lequel cette borne est au plus 0,05 | un entier |
| f | par combien faut-il multiplier $n$ pour diviser la demi-largeur par 2 ? | un entier |
| g | l'écart-type de $\bar{X}$ pour $n = 400$ | un nombre (2 décimales) |
| h | le plus petit $n$ de la question c) si l'écart-type était $\sigma = 4$ W | un entier |

Dans ta copie : c) et e) garantissent-ils la même chose ? Pourquoi Bienaymé-Tchebychev demande-t-il tant de mesures de plus ?

### Ex M02c.6 — Le théorème central limite à la main : une somme de 100 variables ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer l'espérance et l'écart-type d'une somme, puis des probabilités approchées par le théorème central limite.
**Prérequis :** fiche §5 ; M02b §4 et §6 · **Parcours :** C, E

Chaque jour, un système de recommandation fait gagner à une petite boutique un montant net $X$, en euros, de loi :

| $x$ | $-1$ | $0$ | $4$ |
|---|---|---|---|
| $P(X = x)$ | 0,5 | 0,3 | 0,2 |

Les gains des différents jours sont indépendants, et $S$ est le gain total sur 100 jours. Pour e), f) et h), approche **directement** la loi de la somme par la loi normale de même espérance et de même écart-type, comme dans l'exemple de la fiche (§5), sans autre correction.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{E}[X]$ | un nombre (2 décimales) |
| b | $\mathbb{V}(X)$ | un nombre (2 décimales) |
| c | $\mathbb{E}[S]$ | un nombre (1 décimale) |
| d | $\sigma(S)$ | un nombre (1 décimale) |
| e | $P(S > 49)$, par le théorème central limite | un nombre (4 décimales) |
| f | $P(11 \le S \le 49)$, par le théorème central limite | un nombre (3 décimales) |
| g | l'écart-type du gain moyen par jour sur les 100 jours | un nombre (2 décimales) |
| h | le plus petit nombre de jours $n$ pour lequel, d'après le théorème central limite, le gain total $S_n$ sur $n$ jours vérifie $P(S_n > 0) \ge 0{,}975$ | un entier |

Dans ta copie : $X$ est très asymétrique. Pourquoi peut-on quand même utiliser la loi normale pour $S$ ? Pourquoi serait-ce une mauvaise idée pour le gain d'un seul jour ?

### Ex M02c.7 — Biais, variance et erreur quadratique de trois estimateurs ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer le biais, la variance et l'erreur quadratique moyenne d'estimateurs simples, et voir qu'un estimateur biaisé peut être le meilleur.
**Prérequis :** fiche §6 ; M02b §6 · **Parcours :** C, E

$X_1$, $X_2$, $X_3$ sont i.i.d., d'espérance $\mu$ inconnue et de variance $\sigma^2 = 9$. On compare trois estimateurs de $\mu$ :

$$T_1 = X_1, \qquad T_2 = \frac{X_1 + X_2 + X_3}{3}, \qquad T_3 = \frac{X_1 + X_2 + X_3}{4}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | le biais de $T_3$ quand $\mu = 6$ | un nombre (2 décimales) |
| b | $\mathbb{V}(T_2)$ | un entier |
| c | $\mathbb{V}(T_3)$ | une fraction irréductible |
| d | l'erreur quadratique moyenne de $T_3$ quand $\mu = 6$ | un nombre (4 décimales) |
| e | quand $\mu = 6$, le numéro (1, 2 ou 3) de l'estimateur d'erreur quadratique la plus petite | un entier |
| f | l'erreur quadratique moyenne de $T_3$ quand $\mu = 2$ | un nombre (4 décimales) |
| g | quand $\mu = 2$, le numéro de l'estimateur d'erreur quadratique la plus petite | un entier |
| h | la valeur $m > 0$ telle que $T_3$ bat $T_2$ exactement quand $\lvert \mu \rvert < m$ | un nombre (3 décimales) |

Dans ta copie : écris le biais et l'erreur quadratique de $T_3$ en fonction de $\mu$. Pourquoi ne peut-on pas utiliser $T_3$ en pratique pour choisir entre les trois, alors qu'il est parfois le meilleur ?

### Ex M02c.8 — Erreur type et intervalle de confiance d'une moyenne ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une erreur type et des intervalles de confiance pour une moyenne et pour une accuracy.
**Prérequis :** fiche §7 · **Parcours :** C, E

On mesure le temps de calcul d'un modèle de détection sur 49 images : moyenne $\bar{x} = 120{,}5$ ms, écart-type $s = 14$ ms (divisé par $n - 1$).

| | Question | Réponse attendue |
|---|---|---|
| a | l'erreur type de la moyenne | un nombre (2 décimales) |
| b | l'intervalle de confiance à 95 % de la moyenne, `[borne basse, borne haute]` | une liste de 2 nombres (2 décimales) |
| c | la largeur de cet intervalle | un nombre (2 décimales) |
| d | la demi-largeur de l'intervalle à 90 % | un nombre (2 décimales) |
| e | le plus petit nombre d'images pour une demi-largeur à 95 % d'au plus 2 ms (en gardant $s = 14$) | un entier |

Le même modèle classe correctement 360 images d'un jeu de test de 400.

| | Question | Réponse attendue |
|---|---|---|
| f | l'erreur type de son accuracy | un nombre (3 décimales) |
| g | la demi-largeur de l'intervalle à 95 % de son accuracy | un nombre (4 décimales) |
| h | un autre modèle obtient 0,92 sur le même jeu de test : l'écart de 0,02 dépasse-t-il la demi-largeur g) ? | `True` ou `False` |

Dans ta copie : rédige en une phrase correcte ce que veut dire l'intervalle de b). Que faudrait-il pour départager les deux modèles de h) ?

### Ex M02c.9 — La variance d'une somme et la covariance : V(X + Y), V(X − Y) ✏️ ★★ ⏱️ 20 min
**Objectif :** utiliser les règles de calcul de la covariance, puis calculer une covariance et une corrélation empiriques.
**Prérequis :** fiche §8 · **Parcours :** C, E

$\mathbb{V}(X) = 4$, $\mathbb{V}(Y) = 9$ et $\operatorname{Cov}(X, Y) = 3$.

| | Question | Réponse attendue |
|---|---|---|
| a | la corrélation $\rho(X, Y)$ | un nombre (2 décimales) |
| b | $\mathbb{V}(X + Y)$ | un entier |
| c | $\mathbb{V}(X - Y)$ | un entier |
| d | $\mathbb{V}(2X - Y)$ | un entier |
| e | $\operatorname{Cov}(2X + 1,\ Y - 3)$ | un entier |

Quatre points $(x_i, y_i)$ : $(1, 3)$, $(2, 2)$, $(4, 6)$, $(5, 9)$. Les covariances et variances divisent par $n = 4$.

| | Question | Réponse attendue |
|---|---|---|
| f | la covariance empirique de $x$ et $y$ | un nombre (2 décimales) |
| g | leur corrélation $r$ | un nombre (3 décimales) |
| h | la variance de la série $x_i + y_i$ | un nombre (2 décimales) |

Dans ta copie : retrouve h) avec la formule de la variance d'une somme. Dessine les quatre points : la valeur de g) te paraît-elle raisonnable ?

### Ex M02c.10 — La matrice de covariance de trois variables : la lire et la vérifier ✏️ ★★ ⏱️ 20 min
**Objectif :** lire une matrice de covariance, en tirer corrélations et variances de combinaisons, et reconnaître un tableau qui ne peut pas en être une.
**Prérequis :** fiche §8 · **Parcours :** C

Trois features $X_1$, $X_2$, $X_3$ ont pour matrice de covariance

$$\boldsymbol{\Sigma} = \begin{pmatrix} 4 & 2 & -1 \\ 2 & 9 & 0 \\ -1 & 0 & 1 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{V}(X_2)$ | un entier |
| b | $\operatorname{Cov}(X_1, X_3)$ | un entier |
| c | la corrélation de $X_1$ et $X_2$ | une fraction irréductible |
| d | $X_2$ et $X_3$ sont-elles non corrélées ? | `True` ou `False` |
| e | $\mathbb{V}(X_1 + X_2 + X_3)$ | un entier |
| f | $\mathbb{V}(X_1 - X_3)$ | un entier |
| g | parmi les trois tableaux ci-dessous, la lettre du seul qui peut être une matrice de covariance | une lettre |
| h | $\mathbb{V}(w_1X_1 + w_2X_2 + w_3X_3)$ pour $\mathbf{w} = (1, -1, 2)$, la double somme $\sum_i\sum_j w_iw_j\Sigma_{ij}$ | un entier |

Les trois tableaux de la question g) :

$$\mathbf{A} = \begin{pmatrix} 4 & 1 \\ 2 & 9 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix}, \qquad \mathbf{C} = \begin{pmatrix} 4 & 7 \\ 7 & 9 \end{pmatrix}.$$

Dans ta copie : écris la matrice de corrélation de $X_1$, $X_2$, $X_3$. Pour chaque tableau refusé en g), dis quelle propriété il viole.

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex M02c.11 — Pourquoi diviser par n − 1 : E[S²] = σ² ∂ ★★★ ⏱️ 30 min
**Objectif :** démontrer que la variance de l'échantillon divisée par $n$ est biaisée, et que la diviser par $n - 1$ corrige exactement ce biais.
**Prérequis :** fiche §1, §3 et §6 ; M02b §4 et §6 · **Parcours :** C

$X_1, \ldots, X_n$ ($n \ge 2$) sont i.i.d., d'espérance $\mu$ et de variance $\sigma^2$. On note $\bar{X} = \frac{1}{n}\sum_i X_i$, $S_n^2 = \frac{1}{n}\sum_i (X_i - \bar{X})^2$ et $S^2 = \frac{1}{n - 1}\sum_i (X_i - \bar{X})^2$.
1. Démontre que $\sum_{i=1}^{n}(X_i - \bar{X})^2 = \sum_{i=1}^{n}(X_i - \mu)^2 - n(\bar{X} - \mu)^2$ (l'identité du §1, avec $c = \mu$ ; refais le calcul).
2. Que valent $\mathbb{E}\big[(X_i - \mu)^2\big]$ et $\mathbb{E}\big[(\bar{X} - \mu)^2\big]$ ? Justifie chacune.
3. Déduis-en $\mathbb{E}\Big[\sum_i (X_i - \bar{X})^2\Big] = (n - 1)\,\sigma^2$, puis $\mathbb{E}[S_n^2]$ et $\mathbb{E}[S^2]$.
4. Quel est le biais de $S_n^2$ ? Que devient-il quand $n \to +\infty$ ?
5. Que valent $S_n^2$ et $S^2$ quand $n = 1$ ? Explique pourquoi aucune estimation de la dispersion n'est possible avec une seule valeur.
6. À quelle étape l'indépendance des $X_i$ a-t-elle servi ? (Une étape suffit.)
7. Pour aller plus loin : si $\mu$ était **connu**, montre que $\frac{1}{n}\sum_i (X_i - \mu)^2$ est un estimateur sans biais de $\sigma^2$. Pourquoi le $n - 1$ vient-il de ce qu'on a dû estimer $\mu$ ?

### Ex M02c.12 — La variance de la moyenne : V(X̄) = σ²/n, et l'erreur type ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la formule de la variance de la moyenne, en comprendre le rôle de l'indépendance, et voir ce qu'elle devient pour des variables corrélées.
**Prérequis :** fiche §3, §5, §7 et §8 · **Parcours :** C, E

$X_1, \ldots, X_n$ ont toutes l'espérance $\mu$ et la variance $\sigma^2$, et $\bar{X} = \frac{1}{n}\sum_i X_i$.
1. Démontre que $\mathbb{E}[\bar{X}] = \mu$. Quelle propriété utilises-tu ? A-t-elle besoin de l'indépendance ?
2. On suppose les $X_i$ indépendantes. Démontre que $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}$, en justifiant chaque étape.
3. Explique pourquoi l'erreur type $\frac{s}{\sqrt{n}}$ estime l'écart-type de $\bar{X}$, et ce que deviennent l'écart-type des données et l'erreur type quand $n$ est multiplié par 100.
4. On ne suppose plus l'indépendance : chaque paire $X_i, X_j$ ($i \ne j$) a la même corrélation $\rho$. En développant $\mathbb{V}\big(\sum_i X_i\big)$ avec les covariances (fiche §8), démontre que
$$\mathbb{V}(\bar{X}) = \sigma^2\Big(\frac{1}{n} + \Big(1 - \frac{1}{n}\Big)\rho\Big).$$
5. Que devient $\mathbb{V}(\bar{X})$ quand $n \to +\infty$, pour $\rho > 0$ ? Interprète : moyenner les prédictions de 1 000 modèles très corrélés réduit-il beaucoup leur variance ?
6. Pour aller plus loin : avec $\rho = -\frac{1}{N - 1}$, retrouve la formule des tirages sans remise de la fiche (§3).

<a id="reflexion"></a>

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M02c.13 — Le 99e percentile d'une latence : l'estimer et dire son incertitude 🔗 ★★ ⏱️ 20 min
**Objectif :** calculer un percentile élevé d'une mesure de latence, et chiffrer pourquoi il est plus incertain qu'une médiane.
**Prérequis :** fiche §1 et §7 ; M02b §2 (binomiale) et §3 (loi exponentielle) · **Parcours :** C, E

On a mesuré la latence de $n = 1\,000$ réponses d'un service de prédiction. Triées dans l'ordre croissant et numérotées de 0 à 999, les **onze plus grandes** valeurs, $x_{(989)}$ à $x_{(999)}$, sont (en ms) :

$$179,\ 182,\ 186,\ 191,\ 197,\ 205,\ 214,\ 228,\ 247,\ 290,\ 412.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la position $h$ du percentile 99 (convention de la fiche) | un nombre (2 décimales) |
| b | le percentile 99 (le « p99 ») | un nombre (2 décimales) |
| c | le percentile 99,9 | un nombre (3 décimales) |
| d | le nombre **moyen** de mesures, parmi les 1 000, qui dépassent le vrai quantile $q_{0{,}99}$ de la loi des latences | un entier |
| e | l'écart-type de ce nombre (fiche §1, la binomiale) | un nombre (3 décimales) |
| f | si les latences suivaient une loi exponentielle d'espérance 40 ms, le vrai quantile $q_{0{,}99}$ | un nombre (2 décimales) |
| g | le plus petit nombre de mesures pour que, en moyenne, 10 mesures dépassent le vrai quantile $q_{0{,}999}$ | un entier |

Dans ta copie : sur quelles valeurs repose le p99,9 de c) ? Pourquoi un tableau de bord qui affiche le p99,9 sur 1 000 mesures varie-t-il beaucoup d'une heure à l'autre ? Que proposerais-tu ?

### Ex M02c.14 — Standardiser des features avec les statistiques du seul train 🔗 ★ ⏱️ 15 min
**Objectif :** standardiser une feature avec les statistiques du jeu d'entraînement, et mesurer ce qui change si le test s'en mêle.
**Prérequis :** fiche §1 et §2 · **Parcours :** C

Une feature vaut $10, 12, 14, 16, 18$ sur les 5 exemples du jeu d'entraînement, et $20$ et $13$ sur les 2 exemples du jeu de test. Les écarts-types divisent par le nombre de valeurs ($s_n$, comme `StandardScaler`).

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne du jeu d'entraînement | un nombre (2 décimales) |
| b | son écart-type $s_n$ | un nombre (3 décimales) |
| c | la valeur standardisée de l'exemple de test 20 | un nombre (3 décimales) |
| d | la valeur standardisée de l'exemple de test 13 | un nombre (3 décimales) |
| e | **par erreur**, on calcule la moyenne sur les 7 valeurs : laquelle ? | un nombre (3 décimales) |
| f | avec la moyenne et l'écart-type $s_n$ des 7 valeurs, la valeur standardisée de 20 | un nombre (3 décimales) |
| g | la moyenne des 5 valeurs d'entraînement standardisées avec les statistiques **du train** | un nombre (2 décimales) |

Dans ta copie : pourquoi f) est-il plus petit que c) ? En production, un seul exemple arrive à la fois : avec quelles statistiques le standardiser ? Pourquoi standardiser avec le test fausse-t-il l'évaluation ?

### Ex M02c.15 — MML §6.4 : moyennes et covariances empiriques, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais les définitions des moyennes et covariances empiriques, et l'interprétation de la covariance comme produit scalaire.
**Prérequis :** fiche §1 et §8 ; R9 (produit scalaire, norme, angle) · **Parcours :** C

Relis MML §6.4.1, puis lis §6.4.2 et §6.4.6. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. En §6.4.1, quelles autres façons de résumer une loi que l'espérance le livre cite-t-il ? Pour la série de M02c.1, donne celles qui ont un sens pour des données.
2. En §6.4.2, comment le livre définit-il la moyenne empirique et la covariance empirique d'un dataset ? Par quoi divise-t-il ? Que dit-il de la version en $N - 1$ ?
3. Le livre écrit ses données comme des vecteurs $\mathbf{x}_n \in \mathbb{R}^D$. Pour $D = 1$, vérifie que sa covariance empirique est la variance $s_n^2$ de la fiche. Pour $D = 2$, quelle est la taille de la matrice obtenue, et que contient chaque case ?
4. En §6.4.6, à quoi le livre compare-t-il la covariance, la variance et l'écart-type ? Qu'est-ce qui joue le rôle du cosinus d'un angle ?
5. Avec les quatre points de la fiche (§8), vérifie l'affirmation de la question 4 : calcule l'angle (en degrés) entre les deux vecteurs d'écarts.
6. Que signifient alors, en termes d'angle, une corrélation nulle et une corrélation de $-1$ ?
7. Note trois mots ou tournures en anglais de ces sections qui étaient nouveaux pour toi, avec leur traduction.

### Ex M02c.16 — Le biais du survivant : des données qui ne montrent que ceux qui restent ⚖️ ★ ⏱️ 15 min
**Objectif :** reconnaître un biais du survivant dans un dataset, en mesurer les conséquences, et proposer des remèdes.
**Prérequis :** fiche §6 et §9 · **Parcours :** C

Une banque veut prédire si un client remboursera son prêt. Elle entraîne un modèle sur l'historique de ses prêts des cinq dernières années : pour chaque prêt **accordé**, elle sait s'il a été remboursé. Les demandes refusées n'apparaissent pas dans les données, puisqu'on ne sait pas ce qui se serait passé. Le modèle obtient une très bonne accuracy sur un jeu de test tiré de ce même historique.

Réponds dans ta copie, en une dizaine de lignes :
1. Quelle population le modèle a-t-il vue, et sur quelle population sera-t-il utilisé ? Pourquoi est-ce un biais du survivant ?
2. Pourquoi l'excellente accuracy de test ne rassure-t-elle pas ? (Pense à la population dont est tiré le jeu de test.)
3. Les anciens refus venaient de règles qui défavorisaient certains profils (un quartier, un âge). Que risque le nouveau modèle pour ces profils ? Pourquoi est-ce un problème d'équité, et pas seulement de précision ?
4. Un million d'exemples de plus, tirés du même historique, régleraient-ils le problème ? Réponds avec le vocabulaire du §6 (biais et variance).
5. Propose deux remèdes, en disant ce que chacun coûte.

### Ex M02c.17 — Expliquer le théorème central limite avec un histogramme 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement ce que dit le théorème central limite, et ce qu'il ne dit pas.
**Prérequis :** fiche §5 · **Parcours :** C, E

Un collègue regarde la figure de la fiche (§5) et te dit : « Donc, si j'ai assez de données, elles finissent par suivre une loi normale ? C'est pour ça qu'on suppose toujours que tout est gaussien ? »

Réponds-lui **en huit lignes au plus**, sans formule compliquée. Ta réponse doit dire de quoi le théorème parle (et de quoi il ne parle pas), ce qui change quand $n$ grandit (le centre, la largeur, la forme), une condition pour qu'il s'applique, et pourquoi il justifie pourtant les intervalles de confiance.

<a id="entretien"></a>

## 💼 Entretien

### M02c.E1 — L'erreur type décroît en 1/√n : qu'est-ce que cela change pour un jeu de test ? 💼 ★ ⏱️ 10 min
*Fiche §7 · parcours C, E*

« Votre modèle obtient 87 % d'accuracy sur un jeu de test de 500 exemples, et la version précédente 85 %. Le chef de produit veut annoncer une amélioration. Qu'en pensez-vous ? Et combien d'exemples de test faudrait-il pour trancher ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit chiffrer l'erreur type (un ordre de grandeur suffit), dire ce que la décroissance en $\frac{1}{\sqrt{n}}$ implique pour la taille du jeu de test, et citer une meilleure façon de comparer deux modèles sur les mêmes exemples. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m02c_echantillons_estimation/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M02c.18 | La distribution des moyennes d'échantillons · `sample_means` | 🔨 | ★ | 20 | C, E |
| M02c.19 | Biais et erreur quadratique d'un estimateur, par simulation · `estimator_bias, estimator_mse` | 🔨 | ★★ | 25 | C |
| M02c.20 | Erreur type et intervalle de confiance · `standard_error, confidence_interval_mean` | 🔨 | ★ | 20 | C, E |
| M02c.21 | NumPy et SciPy : `ddof`, `np.percentile`, `scipy.stats.sem` | 📦 | ★ | 15 | C |
| M02c.22 | Prédire : l'histogramme des moyennes d'une loi exponentielle quand n grandit | 🔮 | ★ | 10 | C, E |
| M02c.23 | Couverture : 95 % des intervalles contiennent-ils la vraie moyenne ? | 🔬 | ★★ | 20 | C, E |
| M02c.24 | Grande dimension : le cube dont le centre est vide | 🔬 | ★★ | 20 | C |
| M02c.25 | Voir le théorème central limite : histogrammes et densité normale | 🎨 | ★ | 20 | C |
| M02c.26 | Chasse à l'erreur : un intervalle de confiance mal calculé | 🐛 | ★ | 15 | C |
| M02c.27 | Tester une fonction aléatoire : une tolérance en erreurs types | 🛠️ | ★ | 15 | C |
| M02c.28 | Défi : un intervalle à 95 % avec dix valeurs d'une loi asymétrique | 🏆 | ★★★ | 30 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
