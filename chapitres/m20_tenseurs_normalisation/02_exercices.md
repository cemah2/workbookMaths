# M20 · Tenseurs, axes et estimateurs pondérés — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m20_tenseurs_normalisation/06_mes_reponses.md` (créée par `python tools/start_chapter.py M20`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les axes d'un tableau sont numérotés à partir de 0, et les tableaux sont rangés dans l'**ordre C** ; une **forme** s'écrit comme NumPy l'affiche, `(12, 28)`, ou `(5,)` pour un seul axe ; `ddof` est la correction de la variance, qui divise par $N - \text{ddof}$ ; $\mathbf{1}$ est le vecteur dont toutes les coordonnées valent 1 et $\mathbf{C} = \mathbf{I} - \frac1m\mathbf{1}\mathbf{1}^\top$ la matrice de centrage ; dans un sondage, $\pi_i$ est la probabilité d'inclusion de l'unité $i$, $S$ l'échantillon tiré, $\hat Y = \sum_{i \in S} y_i/\pi_i$ l'estimateur de Horvitz-Thompson du total, et, sauf mention contraire, les unités sont tirées **indépendamment** (tirage de Poisson). Quand un énoncé numérote les unités ou les coordonnées, il les numérote **à partir de 1**, comme en mathématiques ; les indices d'un tableau NumPy, eux, partent de 0, et les **positions dans la file** aussi, comme dans la fiche. Une matrice s'écrit dans le notebook comme une liste de ses **lignes**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M20.Q1 — Forme, axes et nombre d'éléments 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Une photo en couleur de 600 lignes et 800 colonnes est rangée dans `img`, de forme (hauteur, largeur, canaux).

1. La forme de `img`, son nombre d'axes et son nombre d'éléments ?
2. La forme de `img[100]` ? Que contient-il ?
3. La forme de `img[:, :, 1]` ? Que contient-il ?
4. La forme de `img.reshape(-1, 3)` ? Que contient chacune de ses lignes ?
5. Vrai ou faux : `img.reshape(3, 600, 800)` donne la même image, les canaux rangés en premier.
6. Dans un tableau de forme $(4, 7, 24)$, quelle est la position, dans la file (ordre C), de l'élément $[0, 1, 0]$ ?

### M20.Q2 — Réduire le long de quel axe ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

`N`, de forme $(30, 8)$, contient les notes de 30 élèves dans 8 matières ; `T`, de forme $(10, 365, 24)$, les températures horaires de 10 stations pendant un an.

1. La moyenne de chaque élève : `N.mean(axis=?)`, et la forme du résultat ?
2. La moyenne de chaque matière : même question.
3. Le profil horaire moyen, toutes stations et tous jours confondus : sur quels axes réduire `T`, et quelle est la forme du résultat ?
4. La forme de `T.mean(axis=(0, 1), keepdims=True)` ?
5. `T - T.mean(axis=2)` lève-t-il une erreur ? Pourquoi ?
6. Vrai ou faux : réduire `T` sur les axes 1 et 2 d'un coup ou l'un après l'autre donne la même **moyenne** ; et la même **variance** ?

### M20.Q3 — Lire une formule d'einsum 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Que calcule `np.einsum("ij,j->i", A, v)` ?
2. Et `np.einsum("ij,ij->", A, B)` ? Quelle est sa forme ?
3. Et `np.einsum("i,j->ij", u, v)` ?
4. Et `np.einsum("ij,kj->ik", A, B)`, en notation matricielle ?
5. Dans `"abc,cd->ad"`, quelles lettres sont sommées ?
6. Combien de multiplications fait `"ij,jk->ik"`, calculé par des boucles, pour des tableaux de formes $(50, 20)$ et $(20, 30)$ ?

### M20.Q4 — Diviser par une probabilité : sans biais ou biaisé ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Une commune tirée avec la probabilité $\pi = 0{,}05$ compte 1 200 habitants. Que vaut son terme dans l'estimateur de Horvitz-Thompson du nombre total d'habitants ?
2. Vrai ou faux : l'estimateur de Horvitz-Thompson est sans biais quelles que soient les probabilités $\pi_i > 0$.
3. Vrai ou faux : « sans biais » veut dire qu'il donne le total exact sur chaque échantillon.
4. On veut le chiffre d'affaires total de $N$ entreprises ; les grandes, qui ont un plus grand chiffre d'affaires, ont plus de chances d'être tirées que les petites. $N$ fois la moyenne des chiffres d'affaires de l'échantillon va en général : (A) surestimer le total ; (B) le sous-estimer ; (C) l'estimer sans biais.
5. Une unité a $\pi_i = 1$. Que vaut son terme dans la variance de $\hat Y$ ?
6. Une unité de valeur $y_j = 40$ a $\pi_j = 0$ ; toutes les autres ont $\pi_i > 0$. Que vaut $\mathbb{E}[\hat Y]$, en fonction du total $Y$ ?

<a id="rappels"></a>

## 🔁 Rappels

### M20.R1 — Variance biaisée et non biaisée : ddof (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

Les valeurs $4, 10, 7, 2, 7$.

1. `np.var([4, 10, 7, 2, 7])` ?
2. `np.var([4, 10, 7, 2, 7], ddof=1)` ?
3. `pd.Series([4, 10, 7, 2, 7]).var()` ?
4. Lequel des deux est l'estimateur sans biais de la variance de la loi d'où viennent des tirages indépendants ?
5. Le rapport des deux variances vaut $\frac{N}{N - 1}$ pour $N$ valeurs. Le plus petit $N$ pour lequel il est sous $1{,}05$ ?

### M20.R2 — La projection orthogonale sur une droite (M12b) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

$\mathbf{a} = (1, 2, 2)$ et $\mathbf{x} = (3, 0, 3)$.

1. La projection orthogonale de $\mathbf{x}$ sur la droite engendrée par $\mathbf{a}$ ?
2. Le reste $\mathbf{x} - \mathbf{p}$ ? Vérifie qu'il est orthogonal à $\mathbf{a}$.
3. La matrice de cette projection, $\mathbf{P} = \frac{\mathbf{a}\mathbf{a}^\top}{\mathbf{a}^\top\mathbf{a}}$ : son coefficient $P_{11}$ et sa trace ?
4. La projection du même $\mathbf{x}$ sur la droite engendrée par $\mathbf{1} = (1, 1, 1)$ ?
5. Vrai ou faux : la matrice d'une projection orthogonale vérifie $\mathbf{P}^\top = \mathbf{P}$ et $\mathbf{P}^2 = \mathbf{P}$.

### M20.R3 — La limite (1 + x/n)ⁿ → eˣ (M14) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C*

1. $(1 + 1/10)^{10}$ (4 décimales), et $e$ ?
2. $(1 - 2/100)^{100}$ (4 décimales), et $e^{-2}$ ?
3. Le logarithme de $(1 + x/n)^n$ vaut $n\ln(1 + x/n)$. Avec $\ln(1 + u) \approx u - u^2/2$, son écart à $x$ ? Retrouve l'écart relatif de la question 2.
4. Vrai ou faux : $(1 + x/n)^n \to e^x$ aussi pour $x < 0$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une forme comme NumPy l'affiche, `(12, 28)` ou `(5,)` ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit ;
- une formule d'`einsum` entre guillemets, comme `"ij,j->i"`, avec les lettres que l'énoncé impose ;
- `True` ou `False` pour un vrai ou faux.

Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex M20.1 — Un tableau de mesures (stations × jours × heures) : les formes après réductions et remodelages ✏️ ★ ⏱️ 15 min
**Objectif :** suivre la forme d'un tableau à trois axes à travers des réductions, un remodelage et une transposition, et retrouver la place d'un élément dans la file.
**Prérequis :** fiche §1, §2 · **Parcours :** C, E

Un réseau de 12 stations relève la qualité de l'air à chaque heure pendant 28 jours : le tableau `T` a la forme $(12, 28, 24)$, et `T[s, d, h]` est la mesure de la station `s`, le jour `d`, à l'heure `h`.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre d'éléments de `T` | un entier |
| b | la forme de `T.mean(axis=2)` | une forme |
| c | la forme de `T.mean(axis=(0, 2), keepdims=True)` | une forme |
| d | la position, dans la file (ordre C, comptée à partir de 0), de l'élément `T[3, 10, 5]` | un entier |
| e | les indices de l'élément qui occupe la position 1 000 de la file | une liste de 3 entiers |
| f | on remodèle `R = T.reshape(12, 4, 7, 24)` (4 semaines de 7 jours) : les indices dans `T` de l'élément `R[3, 1, 3, 5]` | une liste de 3 entiers |
| g | la forme de `R.mean(axis=1)` | une forme |
| h | vrai ou faux : `T - T.mean(axis=1)` lève une erreur | `True` ou `False` |
| i | la forme de `T.transpose(2, 0, 1)` | une forme |

Dans ta copie : que contient `R.mean(axis=1)`, en mots ? Pour obtenir ce résultat, pourquoi faut-il remodeler en $(12, 4, 7, 24)$ et non en $(12, 7, 4, 24)$, et que contiendrait la moyenne sur l'axe 2 de ce second remodelage ? Écris une version correcte de h), qui retire à chaque mesure la moyenne de sa station à la même heure sur les 28 jours.

### Ex M20.2 — Écrire en notation d'Einstein : produit matriciel, trace, forme bilinéaire, produits de matrices empilées le long d'un axe ✏️ ★ ⏱️ 15 min
**Objectif :** traduire des calculs matriciels en notation d'Einstein et en formules d'`einsum`, les calculer à la main, et compter leur coût.
**Prérequis :** fiche §3 ; M09a, M12c · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 0 & -1 \\ 3 & 1 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 2 & 0 & 1 \\ 1 & -1 & 4 \end{pmatrix}, \qquad \mathbf{M} = \begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix}, \qquad \mathbf{x} = (1, 2), \quad \mathbf{y} = (4, -1).$$
Le tableau `Ms` de forme $(3, 2, 2)$ empile les trois matrices $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$, $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, et `vs` de forme $(3, 2)$ les trois vecteurs $(1, 1)$, $(2, -1)$, $(3, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la formule d'`einsum` de $\mathbf{A}\mathbf{B}$, les axes de $\mathbf{A}$ notés `ij` et ceux de $\mathbf{B}$ notés `jk` | une formule |
| b | le coefficient de $\mathbf{A}\mathbf{B}$ en ligne 2, colonne 3 | un entier |
| c | la formule d'`einsum` de $\operatorname{tr}(\mathbf{A}\mathbf{B})$, les axes de $\mathbf{A}$ notés `ij` | une formule |
| d | $\operatorname{tr}(\mathbf{A}\mathbf{B})$ | un entier |
| e | $\operatorname{tr}(\mathbf{B}\mathbf{A})$ | un entier |
| f | $x_iM_{ij}y_j$ | un entier |
| g | le résultat de `np.einsum("sij,sj->si", Ms, vs)` | une matrice |
| h | le nombre de multiplications de `"sij,sjk->sik"`, calculé par des boucles, pour des formes $(10, 4, 6)$ et $(10, 6, 5)$ | un entier |
| i | pour $\mathbf{P}$, $\mathbf{Q}$, $\mathbf{R}$ de formes $(30, 300)$, $(300, 5)$, $(5, 50)$ : le nombre de multiplications de $(\mathbf{P}\mathbf{Q})\mathbf{R}$ | un entier |
| j | même question pour $\mathbf{P}(\mathbf{Q}\mathbf{R})$ | un entier |

Dans ta copie : écris $\operatorname{tr}(\mathbf{A}\mathbf{B})$ et $\operatorname{tr}(\mathbf{B}\mathbf{A})$ en notation d'Einstein, et explique pourquoi elles sont égales alors que $\mathbf{A}\mathbf{B}$ est $3 \times 3$ et $\mathbf{B}\mathbf{A}$ est $2 \times 2$. La fonction `einsum_pair` du notebook ne prend que deux tableaux : en combien d'appels, et avec quelles formules, calcules-tu f) ? Que donne g) en notation matricielle, ligne par ligne ?

### Ex M20.3 — La matrice de centrage, et une standardisation qui ne voit ni translation ni dilatation ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire la matrice de centrage, vérifier sur un exemple qu'elle se comporte comme une projection, et utiliser les invariances de la standardisation.
**Prérequis :** fiche §4 ; M02c, M12b · **Parcours :** C, E

$m = 6$ et $\mathbf{x} = (3, 7, 4, 9, 5, 8)$. La standardisation utilise ici l'écart type avec **ddof = 1**.

| | Question | Réponse attendue |
|---|---|---|
| a | le coefficient $C_{11}$ de la matrice de centrage | une fraction |
| b | le coefficient $C_{12}$ | une fraction |
| c | $\mathbf{C}\mathbf{x}$ | une liste de 6 nombres |
| d | $\operatorname{tr}\mathbf{C}$ | un entier |
| e | $\lVert\mathbf{C}\mathbf{x}\rVert^2$ | un nombre |
| f | $\lVert\bar x\,\mathbf{1}\rVert^2$ | un nombre |
| g | l'écart type $s$ de $\mathbf{x}$ (ddof = 1) | un nombre (4 décimales) |
| h | le z-score $z_6$ de la sixième coordonnée | un nombre (4 décimales) |
| i | le z-score de la sixième coordonnée de $2{,}5\,\mathbf{x} - 4\,\mathbf{1}$ | un nombre (4 décimales) |
| j | le z-score de la sixième coordonnée de $-2\,\mathbf{x} + \mathbf{1}$ | un nombre (4 décimales) |
| k | vrai ou faux : ajouter 10 à la seule première coordonnée de $\mathbf{x}$ ne change pas ses z-scores | `True` ou `False` |

Dans ta copie : vérifie que $\lVert\mathbf{x}\rVert^2$ est la somme de e) et f), et nomme le théorème. Calcule la première ligne de $\mathbf{C}^2$ et compare-la à celle de $\mathbf{C}$. Justifie i) et j) sans refaire le calcul. Pour k), quels z-scores changent ?

### Ex M20.4 — Un sondage à probabilités inégales : l'estimateur de Horvitz-Thompson d'un total, son espérance et sa variance ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une estimation de Horvitz-Thompson, son espérance et sa variance, et la comparer à l'estimateur naïf.
**Prérequis :** fiche §5 ; M02b · **Parcours :** C, E

Un institut veut le chiffre d'affaires total de 6 entreprises, qu'il ne connaît pas : $\mathbf{y} = (2, 5, 12, 30, 8, 3)$, en millions d'euros. Il tire chaque entreprise indépendamment, avec les probabilités $\boldsymbol\pi = (0{,}05 ;\ 0{,}1 ;\ 0{,}3 ;\ 0{,}9 ;\ 0{,}15 ;\ 0{,}05)$, fixées d'après leurs effectifs. Il obtient l'échantillon $S = \{1, 4, 6\}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la taille moyenne de l'échantillon, $\sum_i \pi_i$ | un nombre |
| b | le poids de sondage de l'entreprise 5 | un nombre (3 décimales) |
| c | l'estimation de Horvitz-Thompson du total, sur $S$ | un nombre (3 décimales) |
| d | l'estimation naïve $N\,\bar y_S$ (6 fois la moyenne des valeurs tirées) | un nombre |
| e | $\mathbb{E}[\hat Y]$ | un nombre |
| f | $\operatorname{Var}(\hat Y)$ | un nombre (3 décimales) |
| g | l'écart type de $\hat Y$ | un nombre (3 décimales) |
| h | la probabilité de tirer exactement l'échantillon $S$ | un nombre (7 décimales) |
| i | la probabilité que l'échantillon soit vide | un nombre (6 décimales) |
| j | vrai ou faux : multiplier toutes les probabilités par 1,1 diminue la variance de $\hat Y$ | `True` ou `False` |

Dans ta copie : quelle entreprise apporte le plus grand terme à la variance, et pourquoi ? Propose des probabilités proportionnelles aux $y_i$, de même somme que $\boldsymbol\pi$ ; restent-elles $\le 1$ ? Que vaudrait alors le terme $y_i/\pi_i$ de chaque entreprise tirée ? Pourquoi l'estimation c) est-elle si loin du total, alors que l'estimateur est sans biais ?

### Ex M20.5 — Un schéma d'Euler en L pas : la jacobienne d'un pas, celle de L pas, et la limite (1 + λT/L)ᴸ ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la jacobienne d'un pas d'Euler et le produit de $L$ telles jacobiennes, et voir sa limite à horizon fixé.
**Prérequis :** fiche §6 ; M14, M17, M12d · **Parcours :** C, E

**En dimension 1.** $x' = \lambda x$ avec $\lambda = -1{,}2$, sur l'horizon $T = 2$, en $L$ pas de durée $h = T/L$.

**Une rotation.** $\mathbf{x}' = \mathbf{J}\mathbf{x}$ avec $\mathbf{J} = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix}$, sur l'horizon $T = 1$.

**Un pendule.** $F(x, v) = (v,\ -\sin x)$ ($x$ l'angle, $v$ la vitesse angulaire), un pas $\Phi_h(x, v) = (x, v) + h\,F(x, v)$ avec $h = 0{,}05$.

| | Question | Réponse attendue |
|---|---|---|
| a | dimension 1, $L = 5$ : le pas $h$ | un nombre |
| b | le facteur $1 + h\lambda$ d'un pas | un nombre |
| c | $x_5/x_0$ | un nombre (4 décimales) |
| d | $x_L/x_0$ pour $L = 50$ | un nombre (4 décimales) |
| e | la limite de $x_L/x_0$ quand $L \to \infty$ | un nombre (4 décimales) |
| f | la rotation, $L = 10$ : la matrice $\mathbf{I} + h\mathbf{J}$ d'un pas | une matrice |
| g | les valeurs singulières du produit des 10 matrices (elles sont égales : donne-en une) | un nombre (3 décimales) |
| h | même question pour $L = 100$ | un nombre (3 décimales) |
| i | leur limite quand $L \to \infty$ | un nombre |
| j | le pendule : la jacobienne de $\Phi_h$ au point $(\pi/3,\ 0)$ | une matrice |
| k | son déterminant | un nombre |

Dans ta copie : pour la rotation, montre que $(\mathbf{I} + h\mathbf{J})^\top(\mathbf{I} + h\mathbf{J}) = (1 + 4h^2)\,\mathbf{I}$ et déduis-en g). Pour le pendule, pars cette fois de $\mathbf{x}_0 = (\pi/3,\ 1)$ : calcule $\mathbf{x}_1 = \Phi_h(\mathbf{x}_0)$, puis écris la jacobienne de deux pas depuis $\mathbf{x}_0$ comme un produit de deux matrices, dans le bon ordre, et compare-le au produit dans l'autre ordre. Calcule $K$, le maximum de $\lVert\mathbf{J}_F\rVert$ ; que dit la fiche sur les valeurs singulières de la jacobienne de deux pas, en fonction de $hK$ ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque preuve dans ta copie, puis relis-la avec la grille de `05_solutions.md`.

### Ex M20.6 — La matrice de centrage est la projection orthogonale sur l'orthogonal de 1 ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer que le centrage est une projection orthogonale, et en tirer la trace, les valeurs propres et la formule de König-Huygens.
**Prérequis :** fiche §4 ; M12b, M12c · **Parcours :** C

Soit $m \ge 2$, $\mathbf{C} = \mathbf{I} - \frac1m\mathbf{1}\mathbf{1}^\top$ et $H = \{\mathbf{v} \in \mathbb{R}^m : \mathbf{1}^\top\mathbf{v} = 0\}$.

1. Montre que $\mathbf{C}^\top = \mathbf{C}$ et que $\mathbf{C}^2 = \mathbf{C}$ (utilise $\mathbf{1}^\top\mathbf{1} = m$).
2. Montre que $\mathbf{C}\mathbf{1} = \mathbf{0}$ et que $\mathbf{C}\mathbf{v} = \mathbf{v}$ pour tout $\mathbf{v} \in H$.
3. Déduis-en que, pour tout $\mathbf{x}$, $\mathbf{C}\mathbf{x} \in H$ et $\mathbf{x} - \mathbf{C}\mathbf{x}$ est orthogonal à $H$ : $\mathbf{C}\mathbf{x}$ est la projection orthogonale de $\mathbf{x}$ sur $H$ (M12b). Quel lien avec la projection sur la droite engendrée par $\mathbf{1}$ ?
4. Donne les valeurs propres de $\mathbf{C}$ avec leurs multiplicités, sa trace et son rang.
5. Démontre $\sum_i x_i^2 = m\,\bar x^2 + \sum_i (x_i - \bar x)^2$.
6. Pour un tableau $\mathbf{X}$ de forme $(m, n)$, que calculent $\mathbf{C}_m\mathbf{X}$ et $\mathbf{X}\mathbf{C}_n$ (où $\mathbf{C}_k$ est la matrice de centrage de taille $k$) ? Écris chacun avec une moyenne NumPy et la diffusion.

### Ex M20.7 — L'estimateur de Horvitz-Thompson est sans biais, et sa variance quand les inclusions sont indépendantes ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer les deux résultats du §5, et construire un estimateur sans biais de la variance.
**Prérequis :** fiche §5 ; M02b · **Parcours :** C, E

Une population de $N$ unités de valeurs $y_1, \ldots, y_N$, de total $Y$ ; l'unité $i$ entre dans l'échantillon avec la probabilité $\pi_i$ ; $I_i$ est son indicatrice et $\hat Y = \sum_i I_i\,y_i/\pi_i$.

1. On suppose seulement $\mathbb{P}(I_i = 1) = \pi_i > 0$ pour tout $i$, sans hypothèse sur la dépendance entre les tirages. Montre que $\mathbb{E}[\hat Y] = Y$.
2. On suppose maintenant les $I_i$ indépendantes. Montre que $\operatorname{Var}(\hat Y) = \sum_i y_i^2\,\frac{1 - \pi_i}{\pi_i}$.
3. Montre que $\hat V = \sum_{i \in S} y_i^2\,\frac{1 - \pi_i}{\pi_i^2}$ est un estimateur sans biais de $\operatorname{Var}(\hat Y)$. Pourquoi ne peut-on pas simplement calculer la formule de la question 2 ?
4. Les $y_i$ sont $> 0$, et l'on prend $\pi_i = c\,y_i \le 1$ pour toutes les unités. Que vaut chaque terme $y_i/\pi_i$ d'une unité tirée ? Écris $\operatorname{Var}(\hat Y)$ en fonction de $Y$, $c$ et $\sum_i y_i^2$. Pourquoi n'est-elle pas nulle avec un tirage de Poisson ?
5. Une unité $j$ a $\pi_j = 0$ (les autres $\pi_i > 0$) ; on garde $\hat Y = \sum_{i \in S} y_i/\pi_i$, l'unité $j$ n'étant jamais dans $S$. Que vaut $\mathbb{E}[\hat Y]$ ? À quelle condition sur $y_j$ l'estimateur reste-t-il sans biais ?

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M20.8 — Pont : où workbookIA 20 divise par une probabilité 🔗 ★ ⏱️ 10 min
**Objectif :** repérer, dans le chapitre de workbookIA que M20 prépare, l'endroit où l'idée du §5 sert.
**Prérequis :** fiche §5 ; la fiche de workbookIA 20 (sections sur les couches) · **Parcours :** C, E

Feuillette la fiche du chapitre 20 de workbookIA (`chapitres/ch20_deep_learning/01_fiche.md` dans ce dépôt-là), sans faire ses exercices.

| | Question | Réponse attendue |
|---|---|---|
| a | dans quelle couche la fiche de workbookIA 20 divise-t-elle par une probabilité ? (A) la batchnorm ; (B) la layer norm ; (C) le dropout ; (D) la couche dense | une lettre entre guillemets |
| b | l'outil de cette fiche-ci qui divise aussi par une probabilité : (A) `einsum` ; (B) la matrice de centrage ; (C) l'estimateur de Horvitz-Thompson ; (D) le schéma d'Euler | une lettre entre guillemets |

Dans ta copie : dans quelle sous-section de la fiche de workbookIA 20 la division apparaît-elle, et pour quelle version de la couche ?

### Ex M20.9 — Expliquer ce qu'est un axe d'un tableau à quelqu'un qui ne connaît que les tableurs 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans jargon les axes, les réductions et la diffusion.
**Prérequis :** fiche §1, §2 · **Parcours :** C, E

Dans ta copie, en 8 lignes au plus et sans formule, explique à quelqu'un qui manie bien un tableur (des lignes, des colonnes, des onglets) ce qu'est un tableau de forme $(12, 28, 24)$ (stations, jours, heures), ce que veut dire « la moyenne le long de l'axe 1 », et pourquoi « soustraire la moyenne de chaque station » demande de garder un axe de longueur 1. Appuie-toi sur un geste du tableur (une formule recopiée vers la droite, un onglet par station…). Puis relis-toi : as-tu dit quel axe **disparaît** ? Où l'analogie avec le tableur s'arrête-t-elle quand on passe à 4 axes ?

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### M20.E1 — « Pourquoi standardiser des données décalées ou dilatées donne-t-il le même résultat ? » 💼 ★ ⏱️ 10 min
*Fiche §4 · parcours C*

« On vous donne des températures, une fois en degrés Celsius, une fois en degrés Fahrenheit. Vous standardisez les deux séries. Qu'obtenez-vous, et pourquoi ? Y a-t-il des changements de données que la standardisation ne gomme pas ? »

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m20_tenseurs_normalisation/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M20.10 | `einsum` pour deux tableaux, avec des boucles · `einsum_pair` | 🔨 | ★★ | 30 | C, E |
| M20.11 | Moyennes et variances le long d'axes choisis · `moments_along_axes` | 🔨 | ★ | 15 | C, E |
| M20.12 | L'estimateur de Horvitz-Thompson d'un total · `horvitz_thompson_total` | 🔨 | ★ | 10 | C |
| M20.13 | Prédire la forme d'une réduction ou d'un einsum, puis vérifier | 🔮 | ★ | 10 | C, E |
| M20.14 | Simuler un sondage : Horvitz-Thompson contre la moyenne naïve, biais et variance | 🔬 | ★★ | 20 | C |
| M20.15 | Le produit de L jacobiennes I + hJ : ses valeurs singulières extrêmes quand L grandit, à hL fixé | 🎨 | ★ | 20 | C, E |
| M20.16 | Chasse à l'erreur : une moyenne sur le mauvais axe, une diffusion silencieuse, un ddof oublié | 🐛 | ★ | 15 | C, E |
| M20.17 | Un test de propriété : réduire sur deux axes d'un coup, ou l'un après l'autre | 🛠️ | ★ | 15 | C |
| M20.18 | Défi : des probabilités d'inclusion proportionnelles à la taille, et un estimateur presque sans variance | 🏆 | ★★★ | 25 | C |
