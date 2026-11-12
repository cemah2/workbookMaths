# M20 · Tenseurs, axes et estimateurs pondérés — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M20.Q1 — Forme, axes et nombre d'éléments
1. $(600, 800, 3)$ ; 3 axes ; $600 \times 800 \times 3 = 1\,440\,000$ éléments.
2. $(800, 3)$ : la ligne de pixels d'indice 100 (la 101ᵉ), ses 800 pixels avec leurs 3 intensités.
3. $(600, 800)$ : le canal d'indice 1, le vert, une intensité par pixel.
4. $(480\,000, 3)$ : une ligne par pixel, dans l'ordre de lecture (ligne par ligne), avec ses trois intensités.
5. Faux : le remodelage relit la file dans l'ordre C ; sa première « ligne » de 800 nombres contient les intensités des 266 premiers pixels et deux tiers, les trois canaux mélangés. Il faut `img.transpose(2, 0, 1)`.
6. $(0 \times 7 + 1) \times 24 + 0 = 24$.

### M20.Q2 — Réduire le long de quel axe ?
1. `N.mean(axis=1)`, de forme $(30,)$ : l'axe des matières disparaît.
2. `N.mean(axis=0)`, de forme $(8,)$.
3. Les axes $(0, 1)$ (stations et jours) ; le résultat a la forme $(24,)$.
4. $(1, 1, 24)$.
5. Oui : alignées à droite, les formes $(10, 365, 24)$ et $(10, 365)$ mettent face à face $24$ et $365$, ni égales ni égales à 1. `T - T.mean(axis=2, keepdims=True)` est la bonne écriture.
6. Vrai pour la moyenne (tous les groupes ont la même taille) ; faux pour la variance (il manque la variance des moyennes des groupes).

### M20.Q3 — Lire une formule d'einsum
1. Le produit $\mathbf{A}\mathbf{v}$.
2. $\sum_{i,j}A_{ij}B_{ij}$, un nombre : la forme `()`.
3. Le produit extérieur $\mathbf{u}\mathbf{v}^\top$, le tableau de tous les produits $u_iv_j$.
4. $\mathbf{A}\mathbf{B}^\top$ : $\sum_j A_{ij}B_{kj} = \sum_j A_{ij}(\mathbf{B}^\top)_{jk}$.
5. $b$ et $c$ (absentes de `ad`) ; $c$ est partagée, $b$ n'apparaît que dans le premier tableau.
6. $50 \times 20 \times 30 = 30\,000$.

### M20.Q4 — Diviser par une probabilité : sans biais ou biaisé ?
1. $1\,200/0{,}05 = 24\,000$ : la commune représente 20 communes.
2. Vrai.
3. Faux : il donne le total **en moyenne** sur les échantillons possibles.
4. (A) : les grandes entreprises sont sur-représentées dans l'échantillon, et la moyenne des chiffres d'affaires de l'échantillon dépasse celle de la population (si la variable étudiée n'avait aucun lien avec la taille, ce serait (C), à l'échantillon vide près).
5. 0 : l'unité est toujours tirée, son terme $y_i/\pi_i = y_i$ ne varie pas.
6. $\mathbb{E}[\hat Y] = Y - 40$ : l'unité $j$ n'est jamais tirée, son terme est toujours nul.

<a id="rappels"></a>

## 🔁 Rappels

### M20.R1 — Variance biaisée et non biaisée : ddof (M02c)
1. La moyenne vaut 6, les écarts $-2, 4, 1, -4, 1$, de carrés de somme 38 : $38/5 = 7{,}6$.
2. $38/4 = 9{,}5$.
3. $9{,}5$ : pandas utilise ddof = 1 par défaut.
4. Celui de ddof = 1, qui divise par $N - 1$ (le §4 de la fiche dit pourquoi).
5. $N > 1{,}05\,(N - 1)$ donne $N > 21$ : $N = 22$ ($\frac{22}{21} \approx 1{,}048$, alors que $\frac{21}{20} = 1{,}05$ n'est pas en dessous).

### M20.R2 — La projection orthogonale sur une droite (M12b)
1. $\mathbf{a}^\top\mathbf{x} = 3 + 0 + 6 = 9$, $\mathbf{a}^\top\mathbf{a} = 9$ : $\mathbf{p} = \mathbf{a} = (1, 2, 2)$.
2. $\mathbf{x} - \mathbf{p} = (2, -2, 1)$, et $\mathbf{a}^\top(2, -2, 1) = 2 - 4 + 2 = 0$.
3. $P_{11} = \frac19$ ; la trace vaut $\frac{\mathbf{a}^\top\mathbf{a}}{\mathbf{a}^\top\mathbf{a}} = 1$, la dimension de la droite.
4. $\frac{\mathbf{1}^\top\mathbf{x}}{\mathbf{1}^\top\mathbf{1}}\,\mathbf{1} = \frac63\,\mathbf{1} = (2, 2, 2)$ : la moyenne de $\mathbf{x}$ fois $\mathbf{1}$, la partie que le centrage retire.
5. Vrai.

### M20.R3 — La limite (1 + x/n)ⁿ → eˣ (M14)
1. $2{,}5937$, contre $e \approx 2{,}7183$.
2. $0{,}98^{100} \approx 0{,}1326$, contre $e^{-2} \approx 0{,}1353$.
3. $n\ln(1 + x/n) \approx x - \frac{x^2}{2n}$ : l'écart vaut $-\frac{x^2}{2n} = -0{,}02$ pour $x = -2$ et $n = 100$, et $e^{-0{,}02} \approx 0{,}980$ : $0{,}1353 \times 0{,}980 \approx 0{,}1326$, un écart relatif d'environ 2 %.
4. Vrai.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M20.1 — Un tableau de mesures (stations × jours × heures) : les formes après réductions et remodelages

**Réponses.** a) `8064` · b) `(12, 28)` · c) `(1, 28, 1)` · d) `2261` · e) `[1, 13, 16]` · f) `[3, 10, 5]` · g) `(12, 7, 24)` · h) `True` · i) `(24, 12, 28)`.

**Démarche.** a) $12 \times 28 \times 24 = 8\,064$. b) L'axe 2 (les heures) disparaît. c) Les axes 0 et 2 restent, de longueur 1. d) Les pas de la file sont $28 \times 24 = 672$, $24$ et $1$ : $3 \times 672 + 10 \times 24 + 5 = 2\,016 + 240 + 5 = 2\,261$. e) $1\,000 = 1 \times 672 + 328$, puis $328 = 13 \times 24 + 16$ : $(1, 13, 16)$. f) Le remodelage découpe l'axe des jours en (semaine, jour de la semaine), et le jour vaut $7 \times 1 + 3 = 10$ ; les autres axes ne changent pas : $(3, 10, 5)$. g) L'axe 1 de `R` est celui des semaines : il disparaît. h) $(12, 28, 24)$ contre $(12, 24)$, alignés à droite : $24$ face à $24$, puis $28$ face à $12$ : incompatibles, erreur. i) Le nouvel axe $k$ est l'ancien axe numéro $(2, 0, 1)[k]$ : $(24, 12, 28)$.

Dans ta copie : `R.mean(axis=1)` contient, pour chaque station, chaque jour de la semaine (de 0 à 6) et chaque heure, la moyenne sur les 4 semaines : par exemple, la mesure moyenne des « troisièmes jours » de chaque semaine à 5 h. Le remodelage $(12, 4, 7, 24)$ écrit le jour $d = 7w + j$ (semaine $w$, jour de la semaine $j$), parce que l'ordre C met le jour de la semaine, plus rapide, après la semaine. Le remodelage $(12, 7, 4, 24)$ écrirait $d = 4b + r$ : 7 blocs de 4 jours consécutifs, et sa moyenne sur l'axe 2 serait la moyenne de chaque bloc de 4 jours, sans rapport avec les jours de la semaine. La version correcte de h) : `T - T.mean(axis=1, keepdims=True)`, des formes $(12, 28, 24)$ et $(12, 1, 24)$.

**Erreurs fréquentes.** Croire que `axis=2` donne une valeur par heure (b) : c'est l'axe qui disparaît. Calculer la position en ordre inverse, $5 \times 12 \times 28 + 10 \times 12 + 3 = 1\,803$ (l'ordre de Fortran, où le premier indice varie le plus vite). Écrire $d = 4 \times 1 + 3$ en f), en confondant le nombre de semaines et la longueur d'une semaine.

**Variante.** Le dernier élément, `T[11, 27, 23]`, est à la position $8\,063 = 8\,064 - 1$.

### Ex M20.2 — Écrire en notation d'Einstein : produit matriciel, trace, forme bilinéaire, produits de matrices empilées le long d'un axe

**Réponses.** a) `"ij,jk->ik"` · b) `-4` · c) `"ij,ji->"` · d) `12` · e) `12` · f) `3` · g) `[[3, 1], [4, -1], [-2, 3]]` · h) `1200` · i) `52500` · j) `525000`.

**Démarche.** $\mathbf{A}\mathbf{B} = \begin{pmatrix} 4 & -2 & 9 \\ -1 & 1 & -4 \\ 7 & -1 & 7 \end{pmatrix}$. b) La ligne 2 de $\mathbf{A}$, $(0, -1)$, par la colonne 3 de $\mathbf{B}$, $(1, 4)$ : $-4$. c) et d) $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \sum_i\sum_j A_{ij}B_{ji} = A_{ij}B_{ji}$ : avec les axes de $\mathbf{A}$ notés `ij`, ceux de $\mathbf{B}$ sont `ji`, et rien ne reste : `"ij,ji->"` ; la diagonale $(4, 1, 7)$ donne 12. e) $\mathbf{B}\mathbf{A} = \begin{pmatrix} 5 & 5 \\ 13 & 7 \end{pmatrix}$, de trace 12. f) $\mathbf{M}\mathbf{y} = (8 + 1,\ -3) = (9, -3)$, puis $\mathbf{x}^\top(9, -3) = 9 - 6 = 3$. g) Pour chaque $s$, $\sum_j (M_s)_{ij}(v_s)_j$ : $\mathbf{M}_1\mathbf{v}_1 = (3, 1)$, $\mathbf{M}_2\mathbf{v}_2 = (4, -1)$, $\mathbf{M}_3\mathbf{v}_3 = (-2, 3)$. h) $10 \times 4 \times 6 \times 5 = 1\,200$. i) $30 \times 300 \times 5 + 30 \times 5 \times 50 = 45\,000 + 7\,500$. j) $300 \times 5 \times 50 + 30 \times 300 \times 50 = 75\,000 + 450\,000$, dix fois plus.

Dans ta copie : $\operatorname{tr}(\mathbf{A}\mathbf{B}) = A_{ij}B_{ji}$ et $\operatorname{tr}(\mathbf{B}\mathbf{A}) = B_{ji}A_{ij}$ (en appelant $j$ l'indice des lignes de $\mathbf{B}$) : c'est la même somme des mêmes produits, seuls les noms des indices muets changent. Avec `einsum_pair`, deux appels : `einsum_pair("ij,j->i", M, y)` donne $\mathbf{M}\mathbf{y}$, puis `einsum_pair("i,i->", x, My)` le produit scalaire. g) est la liste des trois produits matrice-vecteur, $\mathbf{M}_s\mathbf{v}_s$, rangés en lignes.

**Erreurs fréquentes.** Écrire `"ij,ij->"` pour la trace de $\mathbf{A}\mathbf{B}$ (c'est $\sum A_{ij}B_{ij}$, qui demanderait deux tableaux de même forme). Calculer $\mathbf{y}^\top\mathbf{M}\mathbf{x} = -6$ au lieu de $\mathbf{x}^\top\mathbf{M}\mathbf{y}$. Sommer sur le mauvais indice en g), ce qui donne $\mathbf{M}_s^\top\mathbf{v}_s$. Oublier la lettre $s$ dans le coût (h), 120). Ne compter qu'un des deux produits en i) (45 000).

**Variante.** `np.einsum("ij,ij->", A, A)` $= \sum_{i,j}A_{ij}^2 = 16$, le carré de la norme de Frobenius de $\mathbf{A}$.

### Ex M20.3 — La matrice de centrage, et une standardisation qui ne voit ni translation ni dilatation

**Réponses.** a) `"5/6"` · b) `"-1/6"` · c) `[-3, 1, -2, 3, -1, 2]` · d) `5` · e) `28` · f) `216` · g) `2.3664` · h) `0.8452` · i) `0.8452` · j) `-0.8452` · k) `False`.

**Démarche.** $\bar x = 36/6 = 6$. a) et b) $1 - \frac16$ et $-\frac16$. c) $\mathbf{x} - 6\,\mathbf{1}$. d) $6 \times \frac56$. e) $9 + 1 + 4 + 9 + 1 + 4 = 28$. f) $6 \times 6^2$. g) $s^2 = 28/5 = 5{,}6$, $s \approx 2{,}36643$. h) $z_6 = 2/2{,}36643 \approx 0{,}84515$. i) $a = 2{,}5 > 0$ : mêmes z-scores. j) $a = -2 < 0$ : z-scores opposés. k) Faux.

Dans ta copie : $\lVert\mathbf{x}\rVert^2 = 9 + 49 + 16 + 81 + 25 + 64 = 244 = 28 + 216$ : c'est le théorème de Pythagore pour $\mathbf{x} = \bar x\,\mathbf{1} + \mathbf{C}\mathbf{x}$, deux vecteurs orthogonaux (la formule de König-Huygens). La première ligne de $\mathbf{C}^2$ : $(\mathbf{C}^2)_{11} = \frac{25}{36} + 5 \times \frac1{36} = \frac56$ et $(\mathbf{C}^2)_{1j} = 2 \times \frac56 \times \left(-\frac16\right) + 4 \times \frac1{36} = -\frac16$ pour $j \ne 1$ : la même que celle de $\mathbf{C}$. i) et j) : la moyenne de $a\mathbf{x} + b\mathbf{1}$ est $a\bar x + b$, ses écarts $a(x_i - \bar x)$, son écart type $\lvert a\rvert s$, donc ses z-scores $\frac{a}{\lvert a\rvert}z_i$. k) Avec $x_1 = 13$, la moyenne passe à $7{,}67$ et l'écart type change : **tous** les z-scores changent, celui de la première coordonnée en tête.

**Erreurs fréquentes.** Prendre l'écart type avec ddof = 0 ($2{,}1602$, d'où $z_6 = 0{,}9258$). Oublier le signe moins hors de la diagonale. Croire que $a < 0$ ne change rien : la dilatation par un nombre négatif renverse l'ordre des valeurs.

**Variante.** $m = 4$ et $\mathbf{x} = (5, 1, 4, 6)$ : $\bar x = 4$, $\mathbf{C}\mathbf{x} = (1, -3, 0, 2)$, $\lVert\mathbf{C}\mathbf{x}\rVert^2 = 14$, $s = \sqrt{14/3} \approx 2{,}1602$ et $z_1 \approx 0{,}4629$.

### Ex M20.4 — Un sondage à probabilités inégales : l'estimateur de Horvitz-Thompson d'un total, son espérance et sa variance

**Réponses.** a) `1.55` · b) `6.667` · c) `133.333` · d) `70` · e) `60` · f) `1270.667` · g) `35.646` · h) `0.0012049` · i) `0.048329` · j) `5`.

**Démarche.** a) $0{,}05 + 0{,}1 + 0{,}3 + 0{,}9 + 0{,}15 + 0{,}05$. b) $1/0{,}15 = 20/3$. c) $\frac{2}{0{,}05} + \frac{30}{0{,}9} + \frac{3}{0{,}05} = 40 + 33{,}333 + 60 = \frac{400}{3}$. d) $6 \times \frac{2 + 30 + 3}{3} = 70$. e) L'estimateur est sans biais : $Y = 60$. f) Les termes $y_i^2\frac{1 - \pi_i}{\pi_i}$ valent $4 \times 19 = 76$, $25 \times 9 = 225$, $144 \times \frac73 = 336$, $900 \times \frac19 = 100$, $64 \times \frac{17}{3} = 362{,}667$ et $9 \times 19 = 171$ : $\frac{3812}{3}$. g) $\sqrt{1\,270{,}667} \approx 35{,}646$. h) $0{,}05 \times 0{,}9 \times 0{,}05 \times (0{,}9 \times 0{,}7 \times 0{,}85) = 0{,}002\,25 \times 0{,}5355 \approx 0{,}001\,204\,9$. i) $0{,}95 \times 0{,}9 \times 0{,}7 \times 0{,}1 \times 0{,}85 \times 0{,}95 \approx 0{,}048\,329$. j) Le plus grand des six termes de f) est $362{,}667$, celui de l'entreprise 5.

Dans ta copie : l'entreprise 5 a une valeur moyenne ($y = 8$) et une petite probabilité ($0{,}15$) ; l'entreprise 4, la plus grande ($y = 30$), est presque toujours tirée ($\pi = 0{,}9$), et son terme ne vaut que 100 ; puis vient l'entreprise 3 ($336$). Des probabilités proportionnelles aux $y_i$ et de somme $1{,}55$ : $\pi_i = 1{,}55\,y_i/60$, soit environ $(0{,}052 ;\ 0{,}129 ;\ 0{,}31 ;\ 0{,}775 ;\ 0{,}207 ;\ 0{,}078)$, toutes $\le 1$ ; chaque entreprise tirée apporterait alors $y_i/\pi_i = 60/1{,}55 \approx 38{,}7$, et l'estimation vaudrait $38{,}7 \times n$ : ce qui reste aléatoire, c'est le nombre $n$ d'entreprises tirées. Avec le tirage de Poisson, la variance ne baisse d'ailleurs qu'à $\frac{60^2}{1{,}55} - \sum_i y_i^2 \approx 1\,177$ : il faut un tirage de taille fixe pour en profiter (🏆 M20.18). Enfin, c) est à plus de deux écarts types du total ($\frac{133{,}3 - 60}{35{,}6} \approx 2{,}06$) : sans biais veut dire juste **en moyenne**, et, avec moins de deux entreprises tirées en moyenne, une estimation isolée peut être très loin ; ici, les entreprises 1 et 6, tirées malgré leurs probabilités de $0{,}05$, pèsent chacune 20 fois leur valeur.

**Erreurs fréquentes.** Multiplier par $\pi_i$ au lieu de diviser (c) donnerait $27{,}25$). Sommer $y_i/\pi_i$ sur **toutes** les entreprises ($276{,}7$). Oublier les facteurs $1 - \pi_j$ des entreprises non tirées dans la probabilité d'un échantillon ($0{,}002\,25$). Prendre $\mathbb{E}[\hat Y]$ pour l'estimation obtenue. Désigner en j) l'entreprise 4, la plus grande : presque toujours tirée, elle apporte peu de variance.

**Variante.** Sur l'échantillon $\{3, 4\}$, $\hat Y = 40 + 33{,}333 = 73{,}333$ et l'estimation naïve vaut $6 \times 21 = 126$.

### Ex M20.5 — Un schéma d'Euler en L pas : la jacobienne d'un pas, celle de L pas, et la limite (1 + λT/L)ᴸ

**Réponses.** a) `0.4` · b) `0.52` · c) `0.0380` · d) `0.0855` · e) `0.0907` · f) `[[1, -0.2], [0.2, 1]]` · g) `1.217` · h) `1.020` · i) `1` · j) `[[1, 0.05], [-0.025, 1]]` · k) `1.00125`.

**Démarche.** a) $2/5$. b) $1 + 0{,}4 \times (-1{,}2)$. c) $0{,}52^5 \approx 0{,}038\,02$. d) $h = 0{,}04$, $(1 - 0{,}048)^{50} \approx 0{,}085\,48$. e) $e^{-2{,}4} \approx 0{,}090\,72$. f) $h = 0{,}1$ : $\mathbf{I} + 0{,}1\,\mathbf{J}$. g) $(\mathbf{I} + h\mathbf{J})^\top(\mathbf{I} + h\mathbf{J}) = \begin{pmatrix} 1 & 2h \\ -2h & 1 \end{pmatrix}\begin{pmatrix} 1 & -2h \\ 2h & 1 \end{pmatrix} = (1 + 4h^2)\,\mathbf{I}$ : un pas est une rotation multipliée par $\sqrt{1 + 4h^2}$, et le produit de 10 pas une rotation multipliée par $(1{,}04)^{5} \approx 1{,}216\,65$, d'où $1{,}217$. h) $h = 0{,}01$ : $(1{,}0004)^{50} \approx 1{,}020\,20$. i) $(1 + 4T^2/L^2)^{L/2} \to 1$, les valeurs singulières de $e^{T\mathbf{J}}$, une rotation. j) $\mathbf{J}_F = \begin{pmatrix} 0 & 1 \\ -\cos x & 0 \end{pmatrix}$, avec $\cos\frac\pi3 = \frac12$ : $\mathbf{I} + 0{,}05\,\mathbf{J}_F = \begin{pmatrix} 1 & 0{,}05 \\ -0{,}025 & 1 \end{pmatrix}$. k) $1 + 0{,}05 \times 0{,}025 = 1{,}00125$, soit $1 + h^2\cos x$.

Dans ta copie : depuis $\mathbf{x}_0 = (\frac\pi3,\ 1)$, $\mathbf{x}_1 = \mathbf{x}_0 + 0{,}05\left(1,\ -\sin\frac\pi3\right) \approx (1{,}0972 ;\ 0{,}9567)$, où $\cos x_1 \approx 0{,}4561$. La jacobienne de deux pas est $\mathbf{J}_{\Phi_h}(\mathbf{x}_1)\,\mathbf{J}_{\Phi_h}(\mathbf{x}_0) = \begin{pmatrix} 1 & 0{,}05 \\ -0{,}0228 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0{,}05 \\ -0{,}025 & 1 \end{pmatrix} \approx \begin{pmatrix} 0{,}99875 & 0{,}1 \\ -0{,}0478 & 0{,}99886 \end{pmatrix}$, celle du second pas à gauche ; dans l'autre ordre, les deux coefficients diagonaux s'échangent : le produit n'est pas le même. $\mathbf{J}_F = \begin{pmatrix} 0 & 1 \\ -\cos x & 0 \end{pmatrix}$ a pour valeurs singulières $1$ et $\lvert\cos x\rvert$ : $K = 1$, $hK = 0{,}05$, et les valeurs singulières de la jacobienne de deux pas sont entre $0{,}95^2 = 0{,}9025$ et $1{,}05^2 = 1{,}1025$ (elles valent environ $0{,}975$ et $1{,}028$).

**Erreurs fréquentes.** Oublier le signe de $\lambda$ ($1{,}48$). Prendre $e^{\lambda}$ au lieu de $e^{\lambda T}$ ($0{,}3012$). Répondre g) avec la valeur d'un seul pas ($1{,}020$, qui est aussi, par hasard, la réponse de h)). Oublier l'identité dans la jacobienne d'un pas, ou dériver $-\sin x$ en $+\cos x$.

**Variante.** Pour $\lambda = 0{,}5$, $T = 2$, $L = 4$ : $(1 + 0{,}25)^4 \approx 2{,}4414$, pour la limite $e \approx 2{,}7183$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M20.6 — La matrice de centrage est la projection orthogonale sur l'orthogonal de 1

**Démonstration.**
1. $\mathbf{C}^\top = \mathbf{I}^\top - \frac1m(\mathbf{1}\mathbf{1}^\top)^\top = \mathbf{I} - \frac1m\mathbf{1}\mathbf{1}^\top = \mathbf{C}$. Puis $\mathbf{C}^2 = \mathbf{I} - \frac2m\mathbf{1}\mathbf{1}^\top + \frac1{m^2}\mathbf{1}(\mathbf{1}^\top\mathbf{1})\mathbf{1}^\top = \mathbf{I} - \frac2m\mathbf{1}\mathbf{1}^\top + \frac{m}{m^2}\mathbf{1}\mathbf{1}^\top = \mathbf{C}$.
2. $\mathbf{C}\mathbf{1} = \mathbf{1} - \frac1m\mathbf{1}(\mathbf{1}^\top\mathbf{1}) = \mathbf{1} - \mathbf{1} = \mathbf{0}$. Pour $\mathbf{v} \in H$, $\mathbf{C}\mathbf{v} = \mathbf{v} - \frac1m\mathbf{1}(\mathbf{1}^\top\mathbf{v}) = \mathbf{v}$.
3. $\mathbf{1}^\top\mathbf{C}\mathbf{x} = (\mathbf{C}\mathbf{1})^\top\mathbf{x} = 0$ ($\mathbf{C}$ symétrique) : $\mathbf{C}\mathbf{x} \in H$. Et $\mathbf{x} - \mathbf{C}\mathbf{x} = \frac1m\mathbf{1}\mathbf{1}^\top\mathbf{x} = \bar x\,\mathbf{1}$ ; pour $\mathbf{v} \in H$, $\mathbf{v}^\top(\bar x\,\mathbf{1}) = \bar x\,(\mathbf{1}^\top\mathbf{v}) = 0$. Un point de $H$ dont la différence avec $\mathbf{x}$ est orthogonale à $H$ est la projection orthogonale de $\mathbf{x}$ sur $H$ (M12b). Le lien : $\frac1m\mathbf{1}\mathbf{1}^\top = \frac{\mathbf{1}\mathbf{1}^\top}{\mathbf{1}^\top\mathbf{1}}$ est la matrice de la projection sur la droite $\mathbb{R}\mathbf{1}$ ; $\mathbf{C} = \mathbf{I} - \mathbf{P}_{\mathbf{1}}$ projette sur l'orthogonal de cette droite.
4. $\mathbf{C}\mathbf{1} = 0 \cdot \mathbf{1}$ : la valeur propre 0, de vecteur propre $\mathbf{1}$. Tout $\mathbf{v} \in H$ non nul vérifie $\mathbf{C}\mathbf{v} = 1 \cdot \mathbf{v}$ ; $H$, noyau de la forme linéaire non nulle $\mathbf{v} \mapsto \mathbf{1}^\top\mathbf{v}$, est de dimension $m - 1$. La valeur propre 1 a donc la multiplicité $m - 1$, la valeur propre 0 la multiplicité 1 (les dimensions font $m$). La trace, somme des valeurs propres, vaut $m - 1$ (comme $m(1 - \frac1m)$ sur la diagonale) ; le rang, dimension de l'image $H$, vaut $m - 1$.
5. $\mathbf{x} = \bar x\,\mathbf{1} + \mathbf{C}\mathbf{x}$, avec $\bar x\,\mathbf{1} \perp \mathbf{C}\mathbf{x}$ (question 3). Pythagore : $\lVert\mathbf{x}\rVert^2 = \lVert\bar x\,\mathbf{1}\rVert^2 + \lVert\mathbf{C}\mathbf{x}\rVert^2 = m\,\bar x^2 + \sum_i (x_i - \bar x)^2$.
6. La colonne $k$ de $\mathbf{C}_m\mathbf{X}$ est $\mathbf{C}_m$ fois la colonne $k$ de $\mathbf{X}$ : chaque colonne est centrée, `X - X.mean(axis=0, keepdims=True)`. Par transposition, $\mathbf{X}\mathbf{C}_n = (\mathbf{C}_n\mathbf{X}^\top)^\top$ centre chaque ligne : `X - X.mean(axis=1, keepdims=True)`.

**Grille de relecture.** Le calcul de $\mathbf{C}^2$ utilise $\mathbf{1}^\top\mathbf{1} = m$. L'appartenance à $H$ et l'orthogonalité du reste sont établies toutes les deux, avec le critère de M12b nommé. Les multiplicités sont justifiées par la dimension de $H$, et la trace est reliée aux $m - 1$ degrés de liberté. König-Huygens est déduit de Pythagore. Les deux écritures NumPy ont `keepdims=True` ou une forme qui diffuse bien.

**Variante.** Pour $m = 2$, $\mathbf{C} = \frac12\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$ : la projection sur la droite engendrée par $(1, -1)$, la figure du §4.

### Ex M20.7 — L'estimateur de Horvitz-Thompson est sans biais, et sa variance quand les inclusions sont indépendantes

**Démonstration.**
1. $I_i$ ne prend que les valeurs 0 et 1 : $\mathbb{E}[I_i] = \mathbb{P}(I_i = 1) = \pi_i$. Par linéarité de l'espérance, qui ne demande aucune indépendance, $\mathbb{E}[\hat Y] = \sum_i\frac{y_i}{\pi_i}\,\mathbb{E}[I_i] = \sum_i y_i = Y$.
2. Les $\frac{y_i}{\pi_i}I_i$ sont indépendantes : la variance de leur somme est la somme de leurs variances (M02b). $\operatorname{Var}(I_i) = \pi_i(1 - \pi_i)$ (Bernoulli), et $\operatorname{Var}(cX) = c^2\operatorname{Var}(X)$ : $\operatorname{Var}\left(\frac{y_i}{\pi_i}I_i\right) = \frac{y_i^2}{\pi_i^2}\,\pi_i(1 - \pi_i) = y_i^2\,\frac{1 - \pi_i}{\pi_i}$. D'où la formule.
3. $\hat V = \sum_i I_i\,y_i^2\,\frac{1 - \pi_i}{\pi_i^2}$, et, par linéarité, $\mathbb{E}[\hat V] = \sum_i\pi_i\,y_i^2\,\frac{1 - \pi_i}{\pi_i^2} = \sum_i y_i^2\,\frac{1 - \pi_i}{\pi_i} = \operatorname{Var}(\hat Y)$. C'est la même idée qu'au 1 : chaque terme de la variance, divisé par sa probabilité d'être observé. La formule du 2 demande les $y_i$ de **toutes** les unités, alors qu'on ne connaît que ceux de l'échantillon.
4. Chaque unité tirée apporte $\frac{y_i}{c\,y_i} = \frac1c$, la même chose : $\hat Y = n/c$, où $n = \sum_i I_i$ est le nombre d'unités tirées. Par la question 2, $\operatorname{Var}(\hat Y) = \sum_i y_i^2\,\frac{1 - c\,y_i}{c\,y_i} = \sum_i\left(\frac{y_i}{c} - y_i^2\right) = \frac Yc - \sum_i y_i^2$. Elle n'est pas nulle (sauf si toutes les $\pi_i$ valent 1) parce que $n$ est aléatoire avec un tirage de Poisson : c'est $\operatorname{Var}(n)/c^2$. Un tirage qui prend exactement $n$ unités, chacune avec la probabilité $\pi_i$, la rendrait nulle (🏆 M20.18).
5. L'unité $j$ n'est jamais dans $S$ : elle n'apparaît jamais dans la somme. Les autres termes ont pour espérance leur $y_i$ (question 1) : $\mathbb{E}[\hat Y] = Y - y_j$. L'estimateur reste sans biais si et seulement si $y_j = 0$.

**Grille de relecture.** Le 1 dit que la linéarité ne demande pas l'indépendance ; le 2 dit où l'indépendance sert. La variance d'une Bernoulli et le carré de la constante sont écrits. Le 3 explique pourquoi la formule exacte n'est pas calculable. Le 4 trouve un terme constant et attribue la variance restante au nombre d'unités tirées. Le 5 donne l'espérance, pas seulement « biaisé ».

**Variante.** Si l'on tire exactement $n$ unités parmi $N$, sans remise et toutes avec la même probabilité, $\pi_i = n/N$ et $\hat Y = N\,\bar y_S$ : les deux estimateurs coïncident, et l'espérance, par la question 1, vaut toujours $Y$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M20.8 — Pont : où workbookIA 20 divise par une probabilité

**Réponses.** a) `"C"` · b) `"C"`.

**Démarche.** La fiche de workbookIA 20 divise par une probabilité dans la sous-section sur le **dropout** ; dans cette fiche-ci, c'est l'estimateur de Horvitz-Thompson (§5) qui divise par une probabilité.

Dans ta copie : la sous-section « Le dropout » (§20.4.3 de la fiche de workbookIA 20), pour la version utilisée par les bibliothèques, dite « inversée ».

**Erreurs fréquentes.** Chercher la division dans la batchnorm : elle divise par un écart type, pas par une probabilité.

**Variante.** Dans un sondage, on divise aussi par $\pi_i$ pour estimer la variance (∂ M20.7, question 3).

### Ex M20.9 — Expliquer ce qu'est un axe d'un tableau à quelqu'un qui ne connaît que les tableurs

**Réponse modèle (8 lignes).** Imagine un classeur de 12 onglets, un par station ; dans chaque onglet, 28 lignes, une par jour, et 24 colonnes, une par heure. Le tableau a trois **axes**, trois directions de lecture : changer d'onglet, descendre d'une ligne, passer à la colonne suivante ; sa forme $(12, 28, 24)$ dit la longueur de chacune. « La moyenne le long de l'axe 1 », c'est, dans chaque onglet, la moyenne de chaque colonne, recopiée vers la droite : l'axe des jours **disparaît**, et il reste un résultat par station et par heure, $(12, 24)$. Pour soustraire à chaque mesure la moyenne de sa station, il faut savoir à quelle case du classeur chaque moyenne s'applique : on garde une « ligne fantôme » de longueur 1 à la place des jours, et la moyenne se recopie sur les 28 lignes, comme une référence absolue `$`. Avec un quatrième axe (par exemple plusieurs polluants), il faudrait un classeur de classeurs : l'image du tableur s'arrête, mais les règles (un axe nommé disparaît, une longueur 1 se recopie) restent les mêmes.

**Grille.** Le classeur et les trois directions ; la forme ; l'axe qui disparaît ; la longueur 1 qui se recopie ; la limite à 4 axes.

<a id="entretien"></a>

## 💼 Entretien

### M20.E1 — « Pourquoi standardiser des données décalées ou dilatées donne-t-il le même résultat ? »

**Réponse modèle (60 secondes).** « On obtient exactement les mêmes z-scores. Standardiser, c'est retirer la moyenne, puis diviser par l'écart type. Passer des Celsius aux Fahrenheit, c'est multiplier par 1,8 et ajouter 32. Le 32 décale toutes les valeurs et la moyenne de la même quantité : il disparaît quand on retire la moyenne. Le 1,8 multiplie tous les écarts à la moyenne et l'écart type par 1,8 : il disparaît dans le quotient. Une translation et une dilatation de toute la série, par un facteur positif, ne changent donc rien ; un facteur négatif changerait seulement le signe. En revanche, la standardisation ne gomme pas une modification de quelques valeurs seulement : changer une seule mesure change la moyenne, l'écart type et tous les z-scores, et une valeur aberrante pèse sur tous les autres. Géométriquement, centrer, c'est projeter sur les vecteurs de somme nulle. En pratique, c'est ce qui rend un modèle indépendant des unités choisies par celui qui a saisi les données. »

**Grille.** La formule ; la translation effacée par le centrage ; la dilatation effacée par la division ; le signe d'un facteur négatif ; ce qui n'est pas effacé ; l'intérêt pratique.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **M20.10 🔨** `einsum_pair` : la formule découpée et vérifiée (des lettres seulement, sans espace), la longueur de chaque lettre, puis, pour chaque indice du résultat (`np.ndindex`), la somme des produits sur toutes les valeurs des lettres sommées (`itertools.product`). Sur les températures synthétiques $(3, 5, 24)$, `daily_10` coïncide avec `np.einsum`, et a) la moyenne pondérée de la station 2, le jour 4, vaut $8{,}6675$ (contre $8{,}0083$ pour la moyenne simple : les heures de jour, plus chaudes, comptent double). La forme bilinéaire en deux contractions : b) `"ij,j->i"` donne $\mathbf{M}\mathbf{y}$, c) `"i,i->"` le contracte avec $\mathbf{x}$, d) $\mathbf{x}^\top\mathbf{M}\mathbf{y} = 22{,}5$ (et $\mathbf{y}^\top\mathbf{M}\mathbf{x} = -16{,}5$ : l'ordre compte). e) Vrai : les produits de matrices empilées `"sij,sjk->sik"` s'écartent de `np.matmul` de $9 \cdot 10^{-16}$ au plus. Le coût est le produit des longueurs de toutes les lettres : 360 multiplications pour `daily_10`, 144 pour e) ; `"sdh,h->s"` somme aussi sur les 5 jours, et donne 5 fois la moyenne des moyennes journalières.
- **M20.11 🔨** `moments_along_axes` : $N$, le produit des longueurs des axes réduits, puis `np.sum(..., keepdims=True)` divisé par $N$, et la somme des carrés des écarts divisée par $N - \text{ddof}$. Les notes de 40 élèves dans 6 matières, standardisées matière par matière (le long de l'axe 0, ddof = 1), coïncident avec le calcul direct de NumPy : a) l'élève 17, qui a 7,5 en philosophie, a la note standardisée $-0{,}6288$. b) Vrai : la classe renotée (maths sur 100, anglais + 2) donne le même tableau à $4 \cdot 10^{-16}$ près, chaque colonne étant $a\mathbf{x} + b\mathbf{1}$ avec $a > 0$. c) Avec ddof = 0, $-0{,}6368$ : toutes les notes standardisées sont multipliées par $\sqrt{40/39} \approx 1{,}0127$. Deux points de plus en anglais pour un seul élève augmenteraient la moyenne de l'anglais de $\frac{2}{40} = 0{,}05$ point.
- **M20.12 🔨** `horvitz_thompson_total` : la somme des $y_i/\pi_i$ sur les seules unités tirées (un `nan` hors de l'échantillon ne gêne pas). Sur l'échantillon tiré (les communes 3, 4 et 5, indices NumPy), a) l'estimation vaut $39\,471{,}89$ habitants pour un vrai total de 33 960 ; b) l'espérance exacte, sur les 256 échantillons pondérés par leur probabilité, vaut $33\,960{,}00$ : l'estimateur est sans biais. La variance par énumération, $1{,}4715 \cdot 10^8$ (un écart type de 12 131 habitants), est celle de la formule de la fiche ; la commune de 8 600 habitants, tirée avec la probabilité 0,55, en apporte 41 %.
- **M20.13 🔮** a) $(3,)$, une moyenne par canal ; b) $(120, 160, 1)$, l'axe réduit gardé ; c) $(120, 160)$, la lettre $c$ sommée ; d) $(6, 31, 24)$, la moyenne de chaque station diffusée ; e) $(6,)$, $d$ et $h$ sommés ; f) $(6, 744)$, les $31 \times 24$ relevés de chaque station ; g) $(25, 25)$, la diffusion silencieuse d'un vecteur $(25,)$ contre une colonne $(25, 1)$ (on voulait `NOTES_13 - NOTES_13.mean(axis=1, keepdims=True)`, de forme $(25, 4)$) ; h) $(31, 144)$, une ligne par jour, les 24 relevés de chaque station l'un après l'autre : `T_13.reshape(31, -1)` a la même forme, mais sa première ligne contient les six premiers jours de la station 0.
- **M20.14 🔬** 400 entreprises, 3 000 tirages de Poisson par plan. Avec $\pi \propto$ effectif, l'effectif moyen des entreprises tirées est de 125, contre 47 dans la population : c) l'estimateur naïf $N\,\bar y_S$ surestime le total de 163,2 %. Les deux estimateurs de Horvitz-Thompson sont sans biais (0,44 % et $-0{,}13$ % ; d) vrai : 1,7 erreur type pour `ht_14`), mais a) l'écart type relatif vaut 14,27 % avec $\pi \propto$ effectif, contre b) 29,17 % avec $\pi$ proportionnel à l'âge, une taille sans lien avec le chiffre d'affaires (la formule de la fiche donne 14,18 % et 29,45 %). Avec $\pi_i \propto x_i$, $y_i/\pi_i$ varie peu ; l'écart type qui reste vient surtout du nombre d'entreprises tirées, de 24 à 60.
- **M20.15 🎨** Pour $\mathbf{J} = \begin{pmatrix} -0{,}3 & -1{,}7 \\ 0{,}95 & -0{,}35 \end{pmatrix}$ et $T = 2$ : $K = \lVert\mathbf{J}\rVert_2 \approx 1{,}7401$, la borne haute $e^{KT} \approx 32{,}5$, et la borne basse $(1 - hK)^L$, qui n'existe que pour $hK < 1$ (dès $L = 4$) et croît vers $e^{-KT} \approx 0{,}031$. a) $e^{T\mathbf{J}}$ a pour valeurs singulières $0{,}6165$ et $0{,}4420$ (ses valeurs propres, de module $0{,}522$, sont autre chose : $\mathbf{J}$ n'est pas symétrique). b) Pour $L = 1\,024$, $\sigma_{\max} \approx 0{,}6181$, à $2 \cdot 10^{-3}$ de la limite. c) Pour $L = 16$, $hK \approx 0{,}2175$ et la borne basse vaut $(1 - hK)^{16} \approx 0{,}0198$. Pour $L = 1$ et $2$, les pas sont trop grands et le produit étire ($3{,}42$, puis $2{,}64$) ; dès $L = 8$, les deux courbes sont près de leur limite, et doubler $L$ ne les change presque plus : à horizon fixé, le produit de $L$ facteurs proches de l'identité ne tend ni vers 0 ni vers l'infini. Le produit des jacobiennes d'un oscillateur amorti non linéaire, le long des points d'Euler, se stabilise de même.
- **M20.16 🐛** (1) Une moyenne sur l'axe 1 au lieu de l'axe 0 : invisible à une vérification de forme sur un tableau carré ; a) les moyennes des 3 matières valent $[11{,}3333 ;\ 10{,}75 ;\ 13{,}5833]$ (le collègue rend les 6 moyennes des élèves). (2) `T[:, 12] - T.mean(axis=1, keepdims=True)` est un tableau $(5, 5)$ de toutes les différences $T[j, 12] - \bar T_i$ ; quatre stations au même profil le rendent constant, et cachent l'erreur. b) L'écart moyen de midi vaut $3{,}1258$, contre $5{,}4125$ chez le collègue. (3) `np.std` divise par $n$ : un facteur $\sqrt{(n - 1)/n}$, invisible sur 100 000 tirages ; c) l'écart type des 5 mesures vaut $1{,}7678$ mm, contre $1{,}5811$ chez le collègue ($\sqrt{5/4} \approx 1{,}118$ fois moins).
- **M20.17 🛠️** `check_two_axes` compare, par la seule fonction `moments` testée, la moyenne d'un coup à la moyenne le long de $a$ puis de $b$, et la variance d'un coup (ddof = 0) à la moyenne des variances plus la variance des moyennes, deux `assert` ; `property_test_17` la lance sur 100 tableaux tirés au hasard. La décomposition est exacte avec ddof = 0 (le terme croisé est nul) ; avec ddof = 1, les dénominateurs $n_an_b - 1$, $n_a - 1$ et $n_b - 1$ ne se recombinent pas, et l'écart relatif va de 0,13 à 0,75. Le test attrape les trois fonctions fausses dès le premier cas : `wrong_count_17` par la propriété des moyennes, `ignores_ddof_17` et `variance_of_variances_17` par la décomposition seule.
- **M20.18 🏆** `pps_probabilities` prend d'office les communes dont la probabilité dépasserait 1, répartit à nouveau le reste, et recommence : trois communes dépassent avant toute répartition, une quatrième après, d'où a) 4 communes prises d'office (les suivantes ont $\pi \approx 0{,}90$, $0{,}83$ et $0{,}77$). Pour les 146 autres, $y_i/\pi_i$ reste entre 41 391 et 50 919, et le tirage systématique en prend exactement 17 : b) l'écart type relatif de Horvitz-Thompson n'est que de 0,42 % (biais relatif de 0,008 %), contre c) 34,2 % avec des probabilités égales $\frac{21}{150}$. Des probabilités proportionnelles à une bonne taille et un échantillon de taille fixe rendent l'estimateur sans biais presque exact ; un générateur recréé à chaque tirage donnerait 2 000 tirages identiques, et un écart type nul.
