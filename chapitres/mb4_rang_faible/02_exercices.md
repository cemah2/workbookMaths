# MB4 · Rang faible et recherche d'information — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/mb4_rang_faible/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB4`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : $\mathbf{M}$ est une matrice de forme $(m, n)$ et de rang $r$, factorisée en $\mathbf{M} = \mathbf{C}\mathbf{F}$, avec $\mathbf{C}$ de forme $(m, r)$ et $\mathbf{F}$ de forme $(r, n)$ ; les colonnes sont numérotées **à partir de 1** sur papier et à partir de 0 dans le code ; les valeurs singulières sont rangées $s_1 \ge s_2 \ge \cdots$, l'**énergie** est $\lVert\mathbf{M}\rVert_F^2 = \sum_is_i^2$, $\mathbf{M}_r$ est la meilleure approximation de rang $r$ (Eckart-Young, M12d) et le rang stable est $\lVert\mathbf{M}\rVert_F^2/\lVert\mathbf{M}\rVert_2^2 = \sum_is_i^2/s_1^2$ ; un carnet a $N$ fiches de recettes, dont $n$ contiennent l'ingrédient, et le logarithme est népérien ; la saturation de $x$ mentions est $s(x) = \frac{x(k_1 + 1)}{x + k_1}$, et, pour une fiche de longueur $\ell$ fois la longueur moyenne, la normalisation $\nu = 1 - b + b\ell$ remplace $k_1$ par $k_1\nu$ au dénominateur ; un classement liste les candidats du meilleur au moins bon, le **rang** d'un candidat dans un classement commence à 1, et, parmi $n$ candidats, le rang $j$ rapporte $n - j$ points de Borda et $\frac{1}{c + j}$ à la somme des $\frac{1}{c + \text{rang}}$ ($c \ge 0$) ; au §6, $n$ objets dont $q$ pertinents sont rangés dans un ordre, $R$ est le rang du premier pertinent, $k$ la coupure de recall@$k$, et $H_n = 1 + \frac12 + \cdots + \frac1n$. Dans le notebook, une matrice s'écrit comme la liste de ses lignes, et un vecteur comme une liste ou un tableau **1-D**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 à 6 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### MB4.Q1 — Rang, factorisation et stockage : vrai ou faux, et le rang d'une somme de produits extérieurs 🧠 ★ ⏱️ 5 min
*Fiche §1 et §2 · parcours C, E*

1. Vrai ou faux : toute matrice de forme $(7, 11)$ et de rang 3 s'écrit $\mathbf{C}\mathbf{F}$, avec $\mathbf{C}$ de forme $(7, 3)$ et $\mathbf{F}$ de forme $(3, 11)$.
2. Vrai ou faux : si $\mathbf{M} = \mathbf{C}\mathbf{F} = \mathbf{C}'\mathbf{F}'$, où $\mathbf{C}$ et $\mathbf{C}'$ ont toutes deux $r$ colonnes, alors $\mathbf{C} = \mathbf{C}'$.
3. $\mathbf{u}_1 = (1, 0, 3, 0)$, $\mathbf{u}_2 = (0, 1, 0, 4)$ et $\mathbf{u}_3 = \mathbf{u}_1 + \mathbf{u}_2$ ; $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ est la base canonique de $\mathbb{R}^3$. Quel est le rang de $\mathbf{u}_1\mathbf{e}_1^\top + \mathbf{u}_2\mathbf{e}_2^\top + \mathbf{u}_3\mathbf{e}_3^\top$, une somme de trois produits extérieurs ?
4. Une matrice de forme $(40, 150)$ est de rang 2. Combien de nombres stocke une factorisation $\mathbf{C}\mathbf{F}$ ? Combien de ces nombres sont libres ?
5. Vrai ou faux : le rang stable d'une matrice non nulle est compris entre 1 et son rang.

### MB4.Q2 — Le poids d'un ingrédient rare, la saturation et la normalisation : signe, sens de variation, limites 🧠 ★ ⏱️ 5 min
*Fiche §3 et §4 · parcours C, E*

1. Vrai ou faux : à $N$ fixé, le poids corrigé $\ln\frac{N - n + 1/2}{n + 1/2}$ diminue quand le nombre $n$ de fiches qui contiennent l'ingrédient augmente.
2. Un ingrédient est dans les $N$ fiches. Quel est le signe de son poids corrigé ? Et celui de la variante $\ln\frac{N + 1}{n + 1/2}$ ?
3. Sans la correction $\frac12$, que vaudrait $\ln\frac{N - n}{n}$ pour un ingrédient présent dans toutes les fiches ? Et pour un ingrédient présent dans aucune ?
4. Que vaut $s(1)$ ? Vers quoi tend $s(x)$ quand $x \to \infty$ ? Comment varie $s$, et quelle est sa concavité ?
5. Pour $x \ge 1$ fixé, vers quoi tend $s(x)$ quand $k_1 \to 0$ ? Quand $k_1 \to \infty$ ? Et que devient la normalisation $1 - b + b\ell$ quand $b = 0$ ?

### MB4.Q3 — Fusionner des classements : ce que change une nouvelle échelle de notes, ce que change la constante c 🧠 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

1. Vrai ou faux : un jury qui notait sur 20 divise toutes ses notes par 2 ; les points de Borda des candidats changent.
2. Un jury remplace chaque note $t > 0$ par $\sqrt t$. Laquelle de ces trois quantités peut changer : la somme des notes brutes, les points de Borda, la somme des $\frac{1}{c + \text{rang}}$ ?
3. Pour $c = 2$, que vaut la contribution d'une cinquième place, rapportée à celle d'une première place ? Et pour $c = 10$ ?
4. Vrai ou faux : pour des classements complets, quand $c$ devient très grand, la somme des $\frac{1}{c + \text{rang}}$ range les candidats dans l'ordre de leurs points de Borda.
5. Vrai ou faux : une fusion par les rangs tient compte de l'écart de notes entre deux candidats voisins.

### MB4.Q4 — recall@k, precision@k, taux de succès et MRR : définitions, et leurs valeurs pour un ordre tiré au hasard 🧠 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

1. Une liste ordonne 8 diagnostics ; les deux bons diagnostics sont aux rangs 3 et 6. Que valent recall@4, precision@4, le taux de succès@4 et le rang réciproque ?
2. 20 objets, dont 4 pertinents, sont rangés dans un ordre tiré au hasard. Que valent l'espérance de recall@5 et celle de precision@5 ?
3. Un seul objet pertinent parmi 3, dans un ordre tiré au hasard : quelle est la loi de $R$, et que vaut $\mathbb{E}[1/R]$ ?
4. 2 objets pertinents parmi 6, dans un ordre tiré au hasard : que valent $P(R = 1)$ et $P(R = 5)$ ?
5. Encadre $H_{40}$ entre $\ln 41$ et $1 + \ln 40$ (2 décimales). Que vaut, à peu près, le MRR d'un ordre tiré au hasard parmi 40 objets dont un seul est pertinent ?

<a id="rappels"></a>

## 🔁 Rappels

### MB4.R1 — Le rang d'un produit, d'un produit extérieur et d'une somme (M12a) 🔁 ★ ⏱️ 6 min
*Fiche §1 · parcours C, E*

1. La forme et le rang de $\mathbf{u}\mathbf{v}^\top$, pour $\mathbf{u} = (4, 0, -3, 2)$ et $\mathbf{v} = (3, -1, 5)$.
2. $\mathbf{A}$ a la forme $(6, 4)$ et le rang 4, $\mathbf{B}$ la forme $(4, 7)$ et le rang 3. Le rang de $\mathbf{A}\mathbf{B}$ est au plus combien ?
3. $\mathbf{u}_1 \ne \mathbf{0}$, $\mathbf{u}_2 = 3\mathbf{u}_1$, $\mathbf{v}_1 = (2, 0, 3)$ et $\mathbf{v}_2 = (0, 4, -1)$. Quel est le rang de $\mathbf{u}_1\mathbf{v}_1^\top + \mathbf{u}_2\mathbf{v}_2^\top$ ?
4. Vrai ou faux : le rang d'un produit $\mathbf{A}\mathbf{B}$ vaut toujours le plus petit des rangs de $\mathbf{A}$ et de $\mathbf{B}$.
5. $\mathbf{S}$ est carrée et inversible. Pourquoi $\mathbf{A}\mathbf{S}$ a-t-elle le même espace des colonnes que $\mathbf{A}$ ?

### MB4.R2 — L'approximation de rang k par la SVD et son erreur de Frobenius (M12d, MML §4.6) 🔁 ★ ⏱️ 6 min
*Fiche §2 · parcours C, E*

Une matrice $\mathbf{M}$ de forme $(3, 4)$ a pour valeurs singulières 7, 4 et 1. Comme en M12d, $\mathbf{M}_k$ est son approximation de rang $k$ par la SVD.
1. $\lVert\mathbf{M}\rVert_F^2$.
2. L'erreur $\lVert\mathbf{M} - \mathbf{M}_1\rVert_F$ (3 décimales).
3. L'erreur $\lVert\mathbf{M} - \mathbf{M}_1\rVert_2$, en norme spectrale.
4. La part de l'énergie gardée par $\mathbf{M}_2$ (3 décimales).
5. Comment MML §4.6 écrit-il $\mathbf{M}_k$ à l'aide des $\mathbf{u}_i$, des $\mathbf{v}_i$ et des $s_i$ ? Vrai ou faux : aucune matrice de rang 1 n'est plus proche de $\mathbf{M}$ que $\mathbf{M}_1$, en norme de Frobenius.

### MB4.R3 — L'information −ln p d'un événement, la cote et le logit (M06, R6) 🔁 ★ ⏱️ 6 min
*Fiche §3 · parcours C, E*

1. L'information d'un événement de probabilité 0,04, en nats puis en bits (3 décimales).
2. La cote d'un événement de probabilité 0,2.
3. Le logit de 0,2 (3 décimales).
4. Quelle probabilité a pour logit $\ln 3$ ?
5. Vrai ou faux : $\operatorname{logit}(1 - p) = -\operatorname{logit}(p)$ pour tout $p \in\ ]0, 1[$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les logarithmes et les racines), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/8"` ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]`.

« Valeurs exactes » veut dire : tous les chiffres, sans arrondir (ces calculs tombent juste). Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex MB4.1 — Les ventes de quatre boulangeries sur cinq produits : le rang, la factorisation par les colonnes pivots, une seconde factorisation (CG)(G⁻¹F), et les nombres stockés ou libres ✏️ ★★ ⏱️ 30 min
**Objectif :** factoriser un tableau de rang 2 par ses colonnes pivots, en trouver une autre factorisation, et compter ce que coûte chacune.
**Prérequis :** fiche §1 ; M09a (forme échelonnée réduite), M12a (rang, colonnes pivots) · **Parcours :** C, E

Quatre boulangeries d'une même ville ont vendu un samedi, en dizaines :

| | baguettes | croissants | pains de campagne | pains au chocolat | tartelettes |
|---|---|---|---|---|---|
| Port | 20 | 6 | 16 | 12 | 8 |
| Gare | 8 | 10 | 14 | 20 | 7 |
| Halles | 12 | 4 | 10 | 8 | 5 |
| Moulin | 16 | 2 | 10 | 4 | 5 |

$\mathbf{M}$ est ce tableau ($m = 4$ lignes, $n = 5$ colonnes), et $\mathbf{C}\mathbf{F}$ sa factorisation par les colonnes pivots : $\mathbf{C}$ est faite des colonnes pivots de $\mathbf{M}$, $\mathbf{F}$ des lignes non nulles de sa forme échelonnée réduite. On pose $\mathbf{G} = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le rang $r$ de $\mathbf{M}$ | un entier |
| b | la matrice $\mathbf{F}$ | une matrice $2 \times 5$ (valeurs exactes) |
| c | la matrice $\mathbf{C}\mathbf{G}$ | une matrice $4 \times 2$ |
| d | la matrice $\mathbf{G}^{-1}\mathbf{F}$ | une matrice $2 \times 5$ (valeurs exactes) |
| e | le nombre de nombres que stockent $\mathbf{C}$ et $\mathbf{F}$ | un entier |
| f | le nombre de nombres libres, $r(m + n - r)$ | un entier |
| g | une chaîne de 120 boulangeries vend 45 produits, et son tableau de ventes est de rang 3 : les nombres stockés par $\mathbf{C}$ et $\mathbf{F}$, puis les nombres libres | une liste de 2 entiers |

Dans ta copie : écris $\mathbf{C}$, et vérifie une ligne de $\mathbf{C}\mathbf{F}$.

### Ex MB4.2 — Un tableau de relevés de stations météo donné par ses valeurs singulières : énergie captée, rang effectif à 99 %, rang stable, puis le coût de C(Fx) et de (CF)x pour un et pour mille vecteurs ✏️ ★★ ⏱️ 25 min
**Objectif :** mesurer le rang effectif d'un tableau de mesures par l'énergie de ses valeurs singulières, puis appliquer sa version factorisée dans l'ordre le moins coûteux.
**Prérequis :** fiche §2 ; M12d (SVD, Eckart-Young), M09a (coût d'un produit) · **Parcours :** C, E

Un réseau de 60 stations relève chaque jour, à midi, la température de l'air, pendant 450 jours ; à chaque station, on retranche sa propre moyenne. Le tableau centré $\mathbf{M}$, de forme $(60, 450)$ (une ligne par station), a pour valeurs singulières 320, 150, 60 et 15, puis 56 valeurs toutes égales à 3. On remplace $\mathbf{M}$ par $\mathbf{M}_r$, stockée sous la forme $\mathbf{C}\mathbf{F}$, avec $\mathbf{C}$ de forme $(60, r)$ et $\mathbf{F}$ de forme $(r, 450)$, où $r$ est le rang de c) ; un vecteur $\mathbf{x}$ de $\mathbb{R}^{450}$ donne un poids à chaque jour (une moyenne sur une saison, par exemple), et l'on veut $\mathbf{M}_r\mathbf{x}$. On compte les multiplications.

| | Question | Réponse attendue |
|---|---|---|
| a | l'énergie $\lVert\mathbf{M}\rVert_F^2$ | un entier |
| b | la part de l'énergie captée par les deux premières valeurs singulières | un nombre (4 décimales) |
| c | le rang effectif à 99 % : le plus petit $r$ dont la part atteint 0,99 | un entier |
| d | l'erreur $\lVert\mathbf{M} - \mathbf{M}_r\rVert_F$, pour ce $r$ | un nombre (2 décimales) |
| e | le rang stable | un nombre (3 décimales) |
| f | le nombre de multiplications de $\mathbf{C}(\mathbf{F}\mathbf{x})$ | un entier |
| g | le nombre de multiplications de $(\mathbf{C}\mathbf{F})\mathbf{x}$, en formant d'abord $\mathbf{C}\mathbf{F}$ | un entier |
| h | pour mille vecteurs $\mathbf{x}$ : le nombre de multiplications de chaque méthode, $\mathbf{C}(\mathbf{F}\mathbf{x})$ puis $(\mathbf{C}\mathbf{F})\mathbf{x}$ ($\mathbf{C}\mathbf{F}$ formée une seule fois) | une liste de 2 entiers |

Dans ta copie : dis pourquoi le rang stable est entre 1 et le rang ; dis pourquoi $\mathbf{C}(\mathbf{F}\mathbf{x})$ et $(\mathbf{C}\mathbf{F})\mathbf{x}$ sont égaux sur papier, mais pas toujours au dernier chiffre près en flottants.

### Ex MB4.3 — Les ingrédients d'un carnet de recettes : surprise, cote, poids corrigé par ½ et son signe, la variante toujours positive, puis la saturation et la normalisation d'une mention répétée ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer le poids d'un ingrédient rare de trois façons, trouver quand le poids corrigé devient négatif, puis chiffrer la saturation et la normalisation comme des fonctions.
**Prérequis :** fiche §3 et §4 ; M06 (information), R6 (cote, logarithme) · **Parcours :** C, E

Un pâtissier a un carnet de $N = 80$ fiches de recettes. La fleur d'oranger figure dans 4 fiches, les œufs dans 62. Dans une fiche, un ingrédient peut être mentionné plusieurs fois (dans la liste et dans les étapes) : on amortit le nombre $x$ de mentions par la saturation $s$, avec $k_1 = 2$.

| | Question | Réponse attendue |
|---|---|---|
| a | la surprise $-\ln\frac{n}{N}$ de la fleur d'oranger | un nombre (4 décimales) |
| b | la cote de présence $\frac{n}{N - n}$ de la fleur d'oranger | une fraction irréductible |
| c | le poids corrigé $\ln\frac{N - n + 1/2}{n + 1/2}$ de la fleur d'oranger | un nombre (4 décimales) |
| d | le poids corrigé des œufs | un nombre (4 décimales) |
| e | dans ce carnet, le plus petit $n$ pour lequel le poids corrigé est négatif | un entier |
| f | la variante $\ln\frac{N + 1}{n + 1/2}$ pour les œufs | un nombre (4 décimales) |
| g | $s(1)$, $s(2)$ et $s(10)$ | une liste de 3 nombres (4 décimales) |
| h | ce qu'ajoute la dixième mention, $s(10) - s(9)$, rapporté à ce qu'ajoute la première, $s(1) - s(0)$ | une fraction irréductible |
| i | 3 mentions dans une fiche deux fois plus longue que la moyenne ($\ell = 2$) : la saturation normalisée $\frac{x(k_1 + 1)}{x + k_1\nu}$, avec $\nu = 1 - b + b\ell$, pour $b = \frac14$, puis pour $b = \frac12$ | une liste de 2 nombres (4 décimales) |

Dans ta copie : montre que, dans un carnet de $N$ fiches, le poids corrigé est négatif si et seulement si $n > \frac N2$, et nul pour $n = \frac N2$ ; montre que la variante est toujours positive.

### Ex MB4.4 — Trois jurys classent cinq pâtissiers : les points de Borda, la somme des 1/(c + rang) pour c = 2 et c = 10, et la somme des notes qui change de gagnant quand un jury passe de 20 à 100 points ✏️ ★★ ⏱️ 30 min
**Objectif :** fusionner trois classements par Borda et par la somme des $\frac{1}{c + \text{rang}}$, voir le rôle de $c$, et voir qu'une somme de notes dépend de l'échelle de chaque jury.
**Prérequis :** fiche §5 · **Parcours :** C, E

Au concours de pâtisserie d'une ville, trois jurys notent sur 20 les cinq finalistes, Anouk, Basile, Céleste, Dorian et Élise (A, B, C, D, E). Chaque jury classe les pâtissiers par notes décroissantes (il n'y a pas d'ex aequo). Pour b) et c), garde 6 décimales dans chaque terme $\frac{1}{c + j}$, et n'arrondis que la somme.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| jury des chefs | 17 | 15 | 12 | 11 | 8 |
| jury du public | 16 | 14 | 8 | 13 | 11 |
| jury de la presse | 6 | 14 | 18 | 10 | 13 |

| | Question | Réponse attendue |
|---|---|---|
| a | les points de Borda de A, B, C, D, E | une liste de 5 entiers |
| b | la somme des $\frac{1}{c + \text{rang}}$ de A, B, C, D, E, pour $c = 2$ | une liste de 5 nombres (4 décimales) |
| c | la même somme pour $c = 10$ | une liste de 5 nombres (4 décimales) |
| d | la somme des trois notes de A, B, C, D, E | une liste de 5 entiers |
| e | la même somme quand la presse note sur 100 (ses notes multipliées par 5) | une liste de 5 entiers |
| f | la valeur de $c$ pour laquelle A et B ont la même somme des $\frac{1}{c + \text{rang}}$ | un nombre |

Dans ta copie : écris les rangs de chaque pâtissier, puis le gagnant de chaque méthode (Borda, $c = 2$, $c = 10$, les deux sommes de notes).

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex MB4.5 — Une matrice de rang r est un produit C F de r colonnes par r lignes ; deux telles factorisations diffèrent d'une matrice inversible ; le rang est le plus petit nombre de produits extérieurs dont elle est la somme ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer l'existence de la factorisation de rang, sa non-unicité exacte, et en déduire une autre définition du rang.
**Prérequis :** fiche §1 ; M12a (base, coordonnées, rang, $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{B})$) · **Parcours :** C, E

$\mathbf{M}$ est une matrice de forme $(m, n)$ et de rang $r \ge 1$. Tu peux utiliser sans le redémontrer ce que M12a établit : le rang est la dimension de l'espace des colonnes, et $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{B})$.
1. Soit $\mathbf{c}_1, \ldots, \mathbf{c}_r$ une base de l'espace des colonnes de $\mathbf{M}$, et $\mathbf{C}$ la matrice de colonnes $\mathbf{c}_1, \ldots, \mathbf{c}_r$. Montre que chaque colonne $\mathbf{m}_j$ de $\mathbf{M}$ s'écrit $\mathbf{C}\mathbf{f}_j$ pour un seul vecteur $\mathbf{f}_j$ de $\mathbb{R}^r$, puis que $\mathbf{M} = \mathbf{C}\mathbf{F}$, où $\mathbf{F}$ a pour colonnes $\mathbf{f}_1, \ldots, \mathbf{f}_n$. Montre que $\mathbf{C}$ et $\mathbf{F}$ sont de rang $r$.
2. Soit $\mathbf{G}$ une matrice $r \times r$ inversible : montre que $(\mathbf{C}\mathbf{G})(\mathbf{G}^{-1}\mathbf{F}) = \mathbf{M}$. Réciproquement, soit $\mathbf{M} = \mathbf{C}'\mathbf{F}'$, avec $\mathbf{C}'$ de forme $(m, r)$ et $\mathbf{F}'$ de forme $(r, n)$. Montre que les colonnes de $\mathbf{C}'$ forment une base de l'espace des colonnes de $\mathbf{M}$, déduis-en une matrice $\mathbf{G}$ de forme $(r, r)$ telle que $\mathbf{C}' = \mathbf{C}\mathbf{G}$, montre qu'elle est inversible, puis que $\mathbf{F}' = \mathbf{G}^{-1}\mathbf{F}$.
3. Montre que $\mathbf{M}$ est la somme des $r$ produits extérieurs $\mathbf{c}_i\mathbf{g}_i^\top$, où $\mathbf{g}_i^\top$ est la ligne $i$ de $\mathbf{F}$. Montre que, si $\mathbf{M}$ est la somme de $p$ produits extérieurs $\mathbf{u}_i\mathbf{v}_i^\top$, alors $p \ge r$. Conclus.

### Ex MB4.6 — Une fusion par les rangs ne change pas quand un jury change d'échelle ; j-ième pour deux jurys bat premier pour un seul si et seulement si j < c + 2 ; quand c grandit, la somme des 1/(c + rang) range selon le nombre de listes, puis la somme des rangs ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer ce qui rend la fusion par les rangs robuste, et ce que règle la constante $c$.
**Prérequis :** fiche §5 ; M03 (l'AUC ne dépend que de l'ordre des scores), M05a ($\frac{1}{1 + u} = 1 - u + \ldots$) · **Parcours :** C

Les points de Borda et la somme des $\frac{1}{c + \text{rang}}$ sont ceux de la fiche ; $c \ge 0$.
1. Un jury donne des notes sans ex aequo et classe les candidats par notes décroissantes. On remplace chaque note $t$ par $\varphi(t)$, où $\varphi$ est strictement croissante. Montre que le rang de chaque candidat dans ce classement ne change pas, et déduis-en que les points de Borda et la somme des $\frac{1}{c + \text{rang}}$ ne changent pas. Montre, sur un exemple en lettres à deux jurys et deux candidats, que le gagnant de la somme des notes brutes peut changer quand un seul jury change d'échelle.
2. Désormais, chaque jury ne classe que ses premiers : un candidat absent de la liste d'un jury ne reçoit rien de ce jury. Le candidat X est premier pour le jury 1 et absent de la liste du jury 2 ; le candidat Y est $j$-ième pour les deux jurys ($j \ge 2$). Montre que Y devance X si et seulement si $j < c + 2$, et qu'ils sont à égalité pour $j = c + 2$. Que dit cette condition dans le cas limite $c = 0$ ?
3. Soit un candidat présent dans $L$ listes, de rangs $j_1, \ldots, j_L$, de somme $S = j_1 + \cdots + j_L$. Montre que, pour $c > 0$, $\frac{1}{c + j} = \frac1c - \frac{j}{c^2} + \frac{j^2}{c^2(c + j)}$, et déduis-en que sa somme des $\frac{1}{c + \text{rang}}$ vaut $\frac Lc - \frac{S}{c^2}$ à un reste près, compris entre 0 et $\frac{1}{c^3}(j_1^2 + \cdots + j_L^2)$. Déduis-en que, pour $c$ assez grand, le candidat présent dans le plus de listes l'emporte, et qu'à nombre de listes égal, la plus petite somme des rangs l'emporte. Que devient cet ordre pour des classements complets ?

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB4.7 — Expliquer à un pâtissier pourquoi un ingrédient présent dans toutes les recettes n'aide pas à retrouver la sienne, et pourquoi la dixième mention compte moins que la première 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule le poids d'un ingrédient rare et la saturation.
**Prérequis :** fiche §3 et §4 ; MB4.3 · **Parcours :** C, E

Un ami pâtissier cherche une recette dans son grand carnet en donnant quelques ingrédients ; un programme classe les fiches. Il te demande : « pourquoi le programme ne s'intéresse-t-il presque pas aux œufs, et pourquoi une fiche qui cite dix fois la vanille ne passe-t-elle pas dix fois devant une fiche qui la cite une fois ? ».

Réponds-lui en 5 à 8 phrases, sans formule : ce que dit un ingrédient présent dans presque toutes les fiches ; pourquoi un ingrédient rare dit beaucoup, et pourquoi on mesure cette rareté par un logarithme plutôt que par une proportion ; pourquoi la première mention compte le plus et la dixième si peu ; et pourquoi une fiche longue doit mentionner un ingrédient plus souvent pour compter autant.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### MB4.E1 — « Comment combiner les classements de deux systèmes dont les scores ne sont pas sur la même échelle ? » 💼 ★ ⏱️ 10 min
*Fiche §5 · parcours C*

« Comment combiner les classements de deux systèmes dont les scores ne sont pas sur la même échelle ? »

Ta réponse doit dire pourquoi additionner les scores bruts est risqué ; ce que donnerait une normalisation des scores, et sa limite ; ce que fait une fusion par les rangs (Borda, somme des $\frac{1}{c + \text{rang}}$) et pourquoi elle ne dépend pas des échelles ; ce que règle $c$ ; ce que l'on perd en ne gardant que les rangs ; et comment choisir entre ces méthodes.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/mb4_rang_faible/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| MB4.8 | La factorisation de rang C F : les colonnes pivots de M et les lignes non nulles de sa forme échelonnée réduite · `rank_factorization` | 🔨 | ★ | 20 | C, E |
| MB4.9 | Les points de Borda de classements complets, et le MRR exact d'un ordre tiré au hasard, en fractions · `borda_scores`, `random_ranking_mrr` | 🔨 | ★★ | 25 | C |
| MB4.10 | Prédire le MRR d'un ordre tiré au hasard parmi 10, 100 puis 1 000 candidats, puis le simuler et le comparer à H_n/n | 🔮 | ★ | 15 | C |
| MB4.11 | Les courbes de saturation x ↦ x(k₁ + 1)/(x + k₁) de k₁ = 0 à l'infini, et ce que la normalisation par la longueur leur fait | 🎨 | ★ | 15 | C |
| MB4.12 | Chasse à l'erreur : C pris dans la forme réduite au lieu de M, un classement lu comme la liste des rangs des candidats, un poids de rareté écrit ln(n/N) | 🐛 | ★ | 15 | C |
| MB4.13 | Défi : retrouver le rang caché de cinq tableaux bruités, cinq fois sur cinq, par leurs valeurs singulières | 🏆 | ★★★ | 25 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les deux 🔨 complètent ta copie `mon_travail/mymath/ranks.py` (**mymath :** `ranks.py`), dont la docstring du module dit ce qui est permis : NumPy (`@` compris), mais rien de `np.linalg`, ni SciPy (`scipy.linalg`, `scipy.stats.rankdata`), ni SymPy : les tests comparent tes résultats avec eux ; dans `borda_scores`, ni `np.argsort` ni `np.lexsort` ; `random_ranking_mrr` calcule en `fractions.Fraction`, avec `math.comb`, sans énumérer les $n!$ ordres ; les candidats sont numérotés à partir de 0, un rang commence à 1 ; ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de sa fonction dans `tests/test_mb4_ranks.py`, puis s'en sert ; dans le notebook, tu l'appelles par `mymath.ranks.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy. Les données des exercices papier (le tableau des boulangeries, les valeurs singulières des stations, les classements des trois jurys) sont recopiées dans une cellule du notebook.

**MB4.8 · 🔨 `rank_factorization(M, tol=1e-10)`.** Écris la fonction, en suivant sa docstring : contrôle $\mathbf{M}$ (un tableau 2-D non vide de nombres finis) et `tol` (un réel $\ge 0$, ni `nan` ni un booléen) ; réduis une copie en flottants comme le fait `rref` de M09a (tu peux importer `rref` de `.matrices`, ou le recopier dans une fonction privée `_rref`), et garde ses colonnes pivots ; $\mathbf{C}$ est faite des colonnes pivots de $\mathbf{M}$ elle-même, $\mathbf{F}$ des $r$ premières lignes de la forme réduite. Lance le groupe de tests. Ensuite : a) `rank_factorization(M_1)`, où `M_1` est le tableau des boulangeries de MB4.1 : la matrice $\mathbf{F}$ (à comparer à ta copie) ; b) le notebook fournit `M_8`, les ventes moyennes d'une semaine de 6 boulangeries sur 5 produits, calculées à partir d'un tableau de rang 2, puis arrondies au millième : le rang trouvé avec `tol=1e-10`, puis avec `tol=1e-2` (une liste de 2 entiers) ; c) avec `tol=1e-2`, le plus grand écart $\lvert(\mathbf{C}\mathbf{F})_{ij} - (\mathbf{M}_8)_{ij}\rvert$ (un nombre). Ce qu'il faut regarder : pourquoi la tolérance $10^{-10}$ trouve-t-elle un autre rang ? D'où vient l'écart de c), et quel ordre de grandeur pouvait-on prévoir ?

**MB4.9 · 🔨 `borda_scores(rankings)` et `random_ranking_mrr(n, n_relevant=1, depth=None)`.** Écris les deux fonctions, en suivant leurs docstrings : pour `borda_scores`, contrôle le tableau (2-D, non vide, des entiers, chaque ligne une permutation de $0, \ldots, n - 1$), puis donne au candidat placé à la position $p$ d'une ligne (positions à partir de 0) $n - 1 - p$ points, et additionne sur les lignes ; pour `random_ranking_mrr`, contrôle les trois arguments (des entiers, pas des booléens, chacun dans son domaine), puis additionne $P(R = j)/j$ en fractions, pour les rangs $j$ qui comptent. Lance les deux groupes de tests. Ensuite : a) `RANKINGS_4`, les classements des trois jurys de MB4.4 (les pâtissiers A à E numérotés de 0 à 4) : les points de Borda (une liste de 5 entiers, à comparer à ta copie) ; b) `RANKINGS_9`, les classements de 7 juges qui classent 9 candidats : les points de Borda (une liste de 9 entiers) ; c) `random_ranking_mrr(8)`, `random_ranking_mrr(8, n_relevant=3)` et `random_ranking_mrr(12, depth=3)` (une liste de 3 fractions, des `Fraction` ou des chaînes `"p/q"`) ; d) vrai ou faux : `random_ranking_mrr(n)` est égal à $H_n/n$, en fractions exactes, pour $n = 1$ à 40. Ce qu'il faut regarder : le classement des 9 candidats par leurs points de Borda est-il celui de la somme de leurs rangs ? Combien d'ordres faudrait-il énumérer pour c) avec $n = 12$, et combien de termes additionne ta fonction ?

**MB4.10 · 🔮 Le MRR d'un ordre tiré au hasard.** Un seul des $n$ candidats est pertinent, et l'ordre est tiré au hasard parmi les $n!$ ordres. **Avant d'exécuter**, prédis : a) pour $n = 10$, le MRR est le plus proche de : (A) 0,1 ; (B) 0,5 ; (C) 0,3 ; b) de $n = 100$ à $n = 1\,000$, le MRR est divisé par environ : (A) 7 ; (B) 10 ; (C) 3 ; c) de $n = 10$ à $n = 1\,000$, le produit $n \times \text{MRR}$ : (A) ne change presque pas ; (B) augmente de 4 à 5 ; (C) est multiplié par environ 100. Puis simule : avec `rng = np.random.default_rng(7510)`, pour $n = 10$, 100 puis 1 000, dans cet ordre, tire 20 000 fois `order = rng.permutation(n)` ; le pertinent est l'objet 0, et son rang est `int(np.flatnonzero(order == 0)[0]) + 1`. Relève, chaque fois pour $n = 10$, 100 et 1 000 (une liste de 3 nombres) : d) la moyenne simulée de $1/R$ ; e) $H_n/n$ ; f) $\frac{\ln n}{n}$ ; puis g) vrai ou faux : chaque moyenne simulée est à moins de 3 erreurs types de $H_n/n$. Ce qu'il faut regarder (après l'expérience) : pourquoi le MRR n'est-il pas divisé par 10 quand $n$ est multiplié par 10 ? Quelle ligne de base un classement doit-il battre parmi 1 000 candidats ?

**MB4.11 · 🎨 Les courbes de saturation.** Écris `saturation_11(x, k1)`, qui rend $s(x)$ pour un tableau `x` de nombres $\ge 0$ (avec $k_1 = 0$, la seule présence : 1 pour $x > 0$, 0 pour $x = 0$ ; avec `k1=np.inf`, le compte brut $x$) ; puis `draw_saturations_11(ax, k1s, xmax)`, qui trace dans les axes reçus, sur 241 points de $[0, x_{\max}]$, une courbe pour chaque $k_1$ de `k1s`, avec une légende qui nomme chaque $k_1$ et des noms d'axes, et rend la liste des tableaux tracés ; puis `draw_lengths_11(ax, k1, b, ells, xmax)`, qui trace de même, pour chaque $\ell$ de `ells`, la courbe de la saturation normalisée $x \mapsto \frac{x(k_1 + 1)}{x + k_1\nu}$, avec $\nu = 1 - b + b\ell$. Les fonctions dessinent dans les axes reçus, sans ouvrir de figure. La vérification les appelle avec $k_1 = 0$, 1, 2, 3 et l'infini, puis avec $k_1 = 1$, $b = \frac12$ et $\ell = \frac12$, 1, 2, sur $[0, 12]$. Relève : a) $s(6)$ pour $k_1 = 1$, 2 et 3 (une liste de 3 nombres) ; b) pour $k_1 = 1$, 2 et 3, la valeur de $x$ où $s$ atteint 90 % de sa limite (une liste de 3 nombres) ; c) pour $k_1 = 1$ et $b = \frac12$, la valeur en $x = 4$ pour $\ell = \frac12$, 1 et 2 (une liste de 3 nombres) ; d) vrai ou faux : pour $\ell = 1$, toutes les courbes passent par le point $(1, 1)$. Ce qu'il faut regarder : entre quelles deux courbes extrêmes se placent les autres ? Que fait une fiche longue à sa courbe, et une fiche courte ?

**MB4.12 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `rank_factorization_bad(M)` doit rendre la factorisation par les colonnes pivots ; elle prend $\mathbf{C}$ dans les colonnes pivots de la **forme réduite** au lieu de celles de $\mathbf{M}$. Il l'a vérifiée sur une matrice déjà sous forme échelonnée réduite.
- (2) `borda_bad(rankings)` doit rendre les points de Borda ; elle lit chaque ligne comme la liste des **rangs** des candidats (la valeur d'indice $c$ comme la position du candidat $c$), au lieu de la liste des candidats dans l'ordre. Il l'a vérifiée sur trois jurys, `[[1, 0, 2], [0, 2, 1], [2, 1, 0]]`.
- (3) `rarity_bad(n, N)` doit rendre la surprise d'un ingrédient présent dans $n$ fiches sur $N$ ; elle rend $\ln\frac nN$. Il l'a vérifiée sur un ingrédient présent dans toutes les fiches, de poids nul.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `rank_factorization_fixed`, `borda_fixed` et `rarity_fixed`, avec les mêmes arguments, sans `mymath`), puis réponds : a) pour le tableau `M_1` des boulangeries, le plus grand écart $\lvert(\mathbf{C}\mathbf{F})_{ij} - M_{ij}\rvert$ par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres) ; b) pour les classements `RANK_12` de 4 juges et 6 candidats, les points de Borda par la fonction corrigée, puis par la fonction fautive (une liste de 2 listes de 6 entiers) ; c) les surprises d'ingrédients présents dans 3 et dans 30 fiches sur 90, par la fonction corrigée, puis par la fonction fautive (une liste de 4 nombres). Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : d'autres tableaux, dont des tableaux de rang 1 et des tableaux dont les colonnes pivots ne sont pas les premières, des classements dont aucune ligne n'est sa propre inverse, et d'autres carnets.

**MB4.13 · 🏆 Défi : le rang caché de cinq tableaux bruités.** Le notebook fournit `TABLES_13`, cinq tableaux de mesures de formes différentes. Chacun est la somme d'un tableau de rang $r$ (caché) et d'un bruit : chaque case reçoit un bruit indépendant, de moyenne nulle et de même écart-type $\sigma$ dans tout le tableau ; $\sigma$ change d'un tableau à l'autre, et n'est pas donné. Écris `hidden_rank_13(M)`, qui rend le rang caché d'un tableau (un entier $\ge 0$ : un tableau peut n'avoir aucun signal), en lisant ses valeurs singulières ; tout NumPy et SciPy sont permis (`np.linalg.svd(M, compute_uv=False)` donne les valeurs singulières). **Critère de réussite** (les « cinq fois sur cinq » du titre) **:** le bon rang pour cinq tableaux cachés, tirés à nouveau à chaque exécution (l'un facile, l'un dont le signal dépasse à peine le bruit, l'un dont les valeurs singulières du signal s'étalent sur un facteur 10 ou plus, l'un très allongé, et l'un sans signal ou à une échelle extrême), en moins de 10 secondes en tout, et le bon rang pour les cinq tableaux du notebook : la vérification recalcule ta réponse a) avec ta fonction. Relève : a) les rangs que rend ta fonction pour les cinq tableaux (une liste de 5 entiers) ; b) `np.linalg.matrix_rank` de chacun (une liste de 5 entiers) ; c) le rang effectif à 99 % de chacun (une liste de 5 entiers). Point de départ : le bruit seul a des valeurs singulières qui ne dépassent guère $\sigma(\sqrt m + \sqrt n)$ (fiche §2) ; $\sigma$ n'est pas donné, mais ce que le rang laisse de côté est presque tout du bruit, et tu sais ce que vaut son énergie (Eckart-Young).
