# MB2 · Cooccurrences, PMI et embeddings — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/mb2_cooccurrences/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB2`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : au §1, un nombre en base 2 ou en base 16 s'écrit avec ses chiffres, le chiffre de poids fort à gauche, et les chiffres hexadécimaux de 10 à 15 sont les lettres A à F ; aux §2 et §3, une table jointe a les valeurs de $X$ en **lignes** et celles de $Y$ en **colonnes**, $p(x)$ et $p(y)$ sont ses marges, $\operatorname{PMI}(x, y) = \ln\frac{p(x, y)}{p(x)\,p(y)}$ est en **nats**, elle vaut $-\infty$ sur une case de probabilité nulle, et $\operatorname{PPMI} = \max(0, \operatorname{PMI})$ ; le lissage d'exposant $\alpha$ remplace $p(y)$ par $p_\alpha(y) \propto n(y)^\alpha$, la loi tempérée de température $T = 1/\alpha$ de M28 ; au §4, $\mathbf{M} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$ est la SVD compacte de M12d, $\mathbf{U}_k$, $\mathbf{S}_k$ et $\mathbf{V}_k$ en gardent les $k$ premières colonnes, et les deux facteurs sont $\mathbf{U}_k\mathbf{S}_k^\beta$ et $\mathbf{V}_k\mathbf{S}_k^{1-\beta}$, pour $\beta \in [0, 1]$ ; au §5, $a$ et $b$ sont des nombres d'exemples (succès et échecs), $s_1$ et $s_0$ les taux de sélection des positifs et des négatifs, et les logits sont en nats ; aux §6 et §7, les vecteurs sont en gras, et les points sont les **lignes** d'une matrice. Dans le notebook, une matrice s'écrit comme la liste de ses lignes, un vecteur comme une liste ou un tableau **1-D**, et $-\infty$ comme `-np.inf`.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 à 6 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### MB2.Q1 — Bases 2 et 16 : le nombre de chiffres d'un entier, la valeur d'un octet, les bits qu'il faut pour N valeurs 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Combien de chiffres a l'entier $100\,000$ en base 2 ? Et en base 16 ?
2. Que valent, en base 10, les octets écrits 5A, 2E et D9 en base 16 ?
3. Combien de bits faut-il au moins pour donner un code distinct à chacune des 26 lettres de l'alphabet ? À chacune de 1 000 valeurs ?
4. Vrai ou faux : tout entier de 12 bits s'écrit avec exactement 3 chiffres hexadécimaux, en complétant au besoin par des zéros à gauche.

### MB2.Q2 — La PMI d'une case : son signe, −∞, la PPMI, la borne des événements rares, et l'information mutuelle qui en est la moyenne 🧠 ★ ⏱️ 6 min
*Fiche §2 · parcours C, E*

1. Une case a $p(x) = 0{,}25$, $p(y) = 0{,}2$, et la règle « $x \Rightarrow y$ » a un lift de 2,8. Que valent $p(x, y)$ et $\operatorname{PMI}(x, y)$ ?
2. Une case de la table n'est jamais observée : $p(x, y) = 0$. Que valent sa PMI et sa PPMI ?
3. Une ligne $x$ a $p(x) = 0{,}05$. Quelle est la plus grande PMI qu'une case de cette ligne puisse avoir, et dans quel cas est-elle atteinte ?
4. Vrai ou faux : la moyenne des PPMI sous la loi jointe, $\sum p(x, y)\operatorname{PPMI}(x, y)$, vaut l'information mutuelle $I(X ; Y)$.
5. Vrai ou faux : l'information mutuelle peut être négative, puisque certaines PMI le sont.

### MB2.Q3 — Lisser une marge : quelles colonnes gagnent, de combien bouge la PMI d'une colonne, et quels classements le lissage garde 🧠 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. Vrai ou faux : pour tout $\alpha \in\ ]0, 1[$, si la marge des colonnes non vides n'est pas uniforme, le lissage $p_\alpha(y) \propto p(y)^\alpha$ fait gagner de la probabilité à la colonne non vide la plus rare et en fait perdre à la plus fréquente.
2. Le lissage fait passer une colonne de $p(y) = 0{,}01$ à $p_\alpha(y) = 0{,}05$. De combien bouge la PMI de chacune de ses cases, et dans quel sens ?
3. Vrai ou faux : dans une colonne, le lissage ne change pas le classement des lignes par PMI.
4. Vrai ou faux : dans une ligne, le lissage ne change pas le classement des colonnes par PMI.
5. Vers quelle loi tend $p_\alpha$ quand $\alpha \to 0$, si la marge a une colonne vide ?

### MB2.Q4 — Répartir les valeurs singulières entre deux facteurs : ce qui dépend de β, ce qui n'en dépend pas, et pourquoi ne pas centrer une table creuse 🧠 ★ ⏱️ 6 min
*Fiche §4 · parcours C, E*

1. Vrai ou faux : le produit $(\mathbf{U}_k\mathbf{S}_k^\beta)(\mathbf{V}_k\mathbf{S}_k^{1-\beta})^\top$ dépend de $\beta$.
2. Une SVD tronquée garde $k = 2$ valeurs singulières, 6 et 2. Pour $\beta = 0$, $\frac12$ et 1, combien de fois la première colonne de $\mathbf{U}_2\mathbf{S}_2^\beta$ est-elle plus longue que la seconde ?
3. Vrai ou faux : pour $\beta = 1$, les produits scalaires entre les lignes de $\mathbf{U}_k\mathbf{S}_k^\beta$ sont ceux des lignes de $\mathbf{M}_k$.
4. Une table de $200\,000 \times 50\,000$ comptages a 0,05 % de cases non nulles. Combien de valeurs faut-il garder en mémoire (sans compter leurs positions) avant de centrer ses colonnes, et après ?
5. Vrai ou faux : la SVD tronquée d'une table **non centrée** donne sa meilleure approximation de rang $k$ au sens de la norme de Frobenius.

### MB2.Q5 — Le logit d'un taux et le sous-échantillonnage : ce qui bouge (l'ordonnée à l'origine), de combien, dans quel sens 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

1. Sur 480 essais, 120 succès et 360 échecs. Que vaut le logit de vraisemblance maximale du taux de succès ?
2. On garde tous les positifs et un négatif sur 40, au hasard. De combien, et dans quel sens, bouge le logit du taux observé ?
3. Un modèle logistique $\operatorname{logit} P(y = 1 \mid x) = \theta_0 + \theta_1x$ est ajusté sur un tel échantillon. Lesquels de ses paramètres diffèrent de ceux de la population, et de combien ?
4. Vrai ou faux : garder la moitié des positifs et la moitié des négatifs, au hasard, ne change pas la cote d'un positif.
5. Pour lire la probabilité d'un positif dans la population avec le modèle de 3, que fais-tu à son logit avant d'appliquer la sigmoïde ?

### MB2.Q6 — Analogies, direction retirée et moyenne masquée : vrai ou faux, avec une raison 🧠 ★ ⏱️ 5 min
*Fiche §6, §7 et §8 · parcours C, E*

1. Vrai ou faux : dans une analogie « $\mathbf{a}$ est à $\mathbf{b}$ ce que $\mathbf{c}$ est à ? », si $\lVert\mathbf{b} - \mathbf{a}\rVert$ est petit devant $\lVert\mathbf{c}\rVert$, $\mathbf{c}$ lui-même a avec la requête $\mathbf{q} = \mathbf{b} - \mathbf{a} + \mathbf{c}$ un cosinus proche de 1, quel que soit le point cherché.
2. Vrai ou faux : si le parallélogramme est parfait ($\mathbf{d} - \mathbf{c} = \mathbf{b} - \mathbf{a}$), aucun point n'a avec $\mathbf{q}$ un cosinus plus grand que $\mathbf{d}$.
3. Vrai ou faux : retirer d'un nuage la direction $\mathbf{u}$ change la norme de chacun de ses vecteurs.
4. Vrai ou faux : après avoir retiré une direction $\mathbf{u}$, plus rien dans les vecteurs ne permet de deviner leur coordonnée le long de $\mathbf{u}$.
5. Vrai ou faux : la moyenne masquée d'une série complétée par des zéros change quand on ajoute d'autres zéros de remplissage, de masque 0.

<a id="rappels"></a>

## 🔁 Rappels

### MB2.R1 — L'information mutuelle d'un tableau 2 × 2 (M06) 🔁 ★ ⏱️ 8 min
*Fiche §2 · parcours C, E*

Un club de randonnée note, pour chaque sortie, s'il a plu ($X$, en lignes : oui, non) et si la sortie a été écourtée ($Y$, en colonnes : oui, non). La loi jointe vaut
$$\begin{pmatrix} 0{,}20 & 0{,}04 \\ 0{,}14 & 0{,}62 \end{pmatrix}.$$
1. Les deux marges.
2. $H(X)$, $H(Y)$ et $H(X, Y)$, en bits (3 décimales).
3. $I(X ; Y) = H(X) + H(Y) - H(X, Y)$ en bits (3 décimales), puis en nats (3 décimales).
4. Vrai ou faux : $I(X ; Y) = 0$ si et seulement si $X$ et $Y$ sont indépendantes. La pluie et les sorties écourtées le sont-elles ?

### MB2.R2 — La meilleure approximation de rang 1 d'une matrice et son erreur (Eckart-Young, M12d) 🔁 ★ ⏱️ 8 min
*Fiche §4 · parcours C, E*

$\mathbf{M} = \begin{pmatrix} 2 & 2 \\ 4 & 4 \\ 3 & -3 \end{pmatrix}$.
1. $\mathbf{M}^\top\mathbf{M}$ et ses valeurs propres.
2. Les valeurs singulières de $\mathbf{M}$, et un vecteur singulier à droite $\mathbf{v}_1$ et à gauche $\mathbf{u}_1$ pour la plus grande.
3. La meilleure approximation de rang 1, $\mathbf{M}_1 = s_1\mathbf{u}_1\mathbf{v}_1^\top$.
4. $\lVert\mathbf{M} - \mathbf{M}_1\rVert_F$. Que dit le théorème d'Eckart-Young de toute autre matrice de rang 1 ?

### MB2.R3 — Cosinus, projection sur une droite et prototype d'une classe (M07, workbookIA B1) 🔁 ★ ⏱️ 7 min
*Fiche §6 et §7 · parcours C, E*

Des échantillons de sol sont décrits par leurs teneurs en sable et en argile, en dizaines de pour cent. Deux échantillons de la classe A, $(2, 7)$ et $(4, 5)$, deux de la classe B, $(7, 1)$ et $(9, 3)$, et un nouvel échantillon $\mathbf{q} = (6, 5)$.
1. Les prototypes (les moyennes) $\mathbf{m}_A$ et $\mathbf{m}_B$ des deux classes.
2. $\cos(\mathbf{q}, \mathbf{m}_A)$ et $\cos(\mathbf{q}, \mathbf{m}_B)$ (2 décimales) : à quelle classe le cosinus rattache-t-il $\mathbf{q}$ ?
3. La projection de $\mathbf{q}$ sur la droite dirigée par $\mathbf{m}_A$.
4. Les distances euclidiennes de $\mathbf{q}$ aux deux prototypes : donnent-elles la même classe ?
5. Vrai ou faux : remplacer $\mathbf{q}$ par $10\,\mathbf{q}$ peut changer la classe donnée par le cosinus.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les logarithmes, les racines et les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"5/8"` ;
- un nombre écrit en base 2 ou en base 16, comme un texte entre guillemets, avec ses seuls chiffres, comme `"1011"` ou `"3F"` (sans `0b` ni `0x`) ;
- une liste entre crochets, comme `[0.2, -1]`, dans l'ordre que dit la question ; une liste d'espèces comme la liste de leurs numéros ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- `True` ou `False` pour un vrai ou faux.

Quand la réponse attendue est « un nombre » sans décimales précisées, le calcul tombe juste : donne la valeur exacte. Garde au moins 6 chiffres significatifs dans tes calculs intermédiaires, et n'arrondis qu'à la fin.

### Ex MB2.1 — Des entiers en base 2 et en base 16 : conversions, une couleur #RRGGBB, les bits pour 5 000 codes, et un mot de 16 bits découpé en deux champs ✏️ ★ ⏱️ 20 min
**Objectif :** convertir un entier entre les bases 10, 2 et 16, lire un octet et une couleur, compter les bits d'un code, et découper un mot de bits en champs.
**Prérequis :** fiche §1 ; R0 (division euclidienne, `//` et `%`), R1 (puissances de 2), R6 ($\log_2$) ; R6 §4 et M06 §7 (les bits pour N valeurs) · **Parcours :** C, E

Un atelier d'impression numérote ses teintes et ses machines. Une couleur s'écrit #RRGGBB : trois octets en base 16, les intensités du rouge, du vert et du bleu, de 0 à 255. Chaque machine envoie des mots de 16 bits : les 4 premiers bits (le champ haut) donnent le numéro de la machine, les 12 derniers (le champ bas) un compteur.

| | Question | Réponse attendue |
|---|---|---|
| a | 214 en base 2 | un texte de 8 chiffres |
| b | 214 en base 16 | un texte de 2 chiffres hexadécimaux |
| c | l'octet $1100\,1011$ (en base 2), en base 10 | un entier |
| d | les trois intensités (rouge, vert, bleu) de la couleur `#4A7C59`, en base 10 | une liste de 3 entiers |
| e | le plus petit nombre de bits qui donne un code distinct à chacune de 5 000 teintes | un entier |
| f | les deux champs du mot $\texttt{0x6B4D}$ : le numéro de la machine, puis le compteur, en base 10 | une liste de 2 entiers |
| g | le mot de 16 bits de la machine 9 dont le compteur vaut 200, en base 16 | un texte de 4 chiffres hexadécimaux |

Dans ta copie : écris les divisions successives par 2 de a), et dis dans quel ordre se lisent les restes ; obtiens b) en groupant les bits de a) par 4, et vérifie-le par une division par 16 ; écris $1100\,1011$ comme une somme de puissances de 2 ; pour e), encadre 5 000 entre deux puissances de 2 consécutives ; pour f), écris le mot en base 2 et sépare ses 4 premiers bits ; pour g), dis pourquoi le champ bas s'écrit avec exactement 3 chiffres hexadécimaux, et ce que vaut le mot en base 10 ; enfin, combien de machines et quelle valeur de compteur au plus ce format permet-il ?

### Ex MB2.2 — Cent oiseaux, trois milieux, quatre espèces : la PMI des cases, le lift d'une règle, la PPMI, l'espèce vue une seule fois, et l'information mutuelle comme moyenne ✏️ ★★ ⏱️ 30 min
**Objectif :** calculer les PMI d'une table jointe, les lire comme des logarithmes de lifts, en tirer la PPMI, et retrouver l'information mutuelle comme la moyenne des PMI.
**Prérequis :** fiche §2 ; M03 (marginales, loi conditionnelle), M06 (information mutuelle) · **Parcours :** C, E

Un ornithologue a noté, pour 100 oiseaux, le milieu où il l'a vu ($X$, en lignes) et son espèce ($Y$, en colonnes). Les espèces sont numérotées de 0 à 3 : 0 huppe, 1 pic, 2 grive, 3 moineau. La loi jointe est la table des comptes divisée par 100.

| | huppe | pic | grive | moineau | total |
|---|---|---|---|---|---|
| forêt | 0 | 6 | 14 | 20 | 40 |
| prairie | 1 | 2 | 10 | 22 | 35 |
| village | 0 | 0 | 3 | 22 | 25 |
| total | 1 | 8 | 27 | 64 | 100 |

| | Question | Réponse attendue |
|---|---|---|
| a | le lift de la règle « forêt ⇒ pic », $P(\text{pic} \mid \text{forêt})/P(\text{pic})$ | un nombre |
| b | $\operatorname{PMI}(\text{forêt}, \text{pic})$ | un nombre (3 décimales) |
| c | $\operatorname{PMI}(\text{village}, \text{grive})$ | un nombre (3 décimales) |
| d | le nombre de cases de PMI égale à $-\infty$ | un entier |
| e | $\operatorname{PMI}(\text{prairie}, \text{huppe})$ | un nombre (3 décimales) |
| f | le nombre de cases de PPMI strictement positive | un entier |
| g | l'information mutuelle $I(X ; Y) = \sum p(x, y)\operatorname{PMI}(x, y)$, sur les cases non vides, en nats | un nombre (4 décimales) |

Dans ta copie : écris les marges ; écris la table complète des douze PMI (3 décimales, $-\infty$ compris), et entoure les cases de PPMI non nulle ; dis ce que signifie un lift de a) supérieur à 1 ; vérifie que e) vaut $-\ln p(\text{prairie})$, dis pourquoi (que vaut $P(\text{prairie} \mid \text{huppe})$ ?), et que c'est la plus grande PMI de la table ; dis pourquoi $I(X ; Y)$ est positive alors que quatre PMI finies sont négatives.

### Ex MB2.3 — Lisser la marge des espèces de la même table (α = 1/3) : la loi lissée, le décalage de la PMI de chaque colonne, et le classement des espèces d'un milieu avant et après ✏️ ★★ ⏱️ 25 min
**Objectif :** lisser une marge par une puissance, prévoir le décalage de la PMI de chaque colonne, et voir quels classements le lissage change.
**Prérequis :** fiche §3 ; MB2.2, M28 (loi tempérée) · **Parcours :** C, E

On reprend la table des oiseaux de MB2.2. On lisse la marge des espèces avec $\alpha = \frac13$ : $p_\alpha(y) \propto n(y)^{1/3}$, où $n(y)$ est le nombre d'oiseaux de l'espèce $y$, puis $\operatorname{PMI}_\alpha(x, y) = \ln\frac{p(x, y)}{p(x)\,p_\alpha(y)}$ : la loi jointe et la marge des milieux ne changent pas.

| | Question | Réponse attendue |
|---|---|---|
| a | la loi lissée $p_\alpha$, dans l'ordre des espèces 0 à 3 | une liste de 4 nombres |
| b | le décalage $\operatorname{PMI}_\alpha(x, y) - \operatorname{PMI}(x, y)$ de chaque colonne, dans l'ordre des espèces | une liste de 4 nombres (4 décimales) |
| c | $\operatorname{PMI}_\alpha(\text{prairie}, \text{huppe})$ | un nombre (3 décimales) |
| d | $\operatorname{PMI}_\alpha(\text{forêt}, y)$ pour le pic, la grive et le moineau, dans cet ordre | une liste de 3 nombres (3 décimales) |
| e | les espèces observées en forêt, par $\operatorname{PMI}_\alpha$ décroissante | une liste de numéros d'espèces |
| f | vrai ou faux : dans chaque colonne, le classement des milieux par PMI est le même avant et après le lissage | `True` ou `False` |

Dans ta copie : écris les racines cubiques des quatre comptes et leur somme ; dis quelles espèces gagnent de la probabilité, lesquelles en perdent, et pourquoi la huppe gagne le plus ; montre que le décalage d'une colonne ne dépend pas de la ligne ; compare c) à e) de MB2.2 : que devient le record de la table ? ; écris le classement des espèces de la forêt avant le lissage (MB2.2), et dis pourquoi il s'inverse ; reconnais $p_\alpha$ comme la loi tempérée de M28, et donne sa température.

### Ex MB2.4 — Quatre magasins, trois produits, une table de rang 2 de SVD donnée : les facteurs U S^β et V S^{1−β} pour β = 0, ½ et 1, leur produit, et le cosinus de deux magasins ✏️ ★★ ⏱️ 35 min
**Objectif :** répartir les valeurs singulières d'une SVD tronquée entre deux facteurs, vérifier que leur produit ne change pas, et mesurer ce qui change : les angles entre les lignes.
**Prérequis :** fiche §4 ; M07 (cosinus), M12d (SVD compacte) · **Parcours :** C, E

Une enseigne compte les ventes hebdomadaires (en dizaines d'articles) de trois produits, numérotés de 1 à 3, dans quatre magasins, numérotés de 1 à 4 : $\mathbf{M}$ a une ligne par magasin et une colonne par produit, dans l'ordre de leurs numéros.
$$\mathbf{M} = \begin{pmatrix} 12 & 96 & 220 \\ 78 & 54 & 5 \\ 57 & 114 & 190 \\ 132 & 144 & 140 \end{pmatrix},\qquad \mathbf{U}_2 = \frac17\begin{pmatrix} 4 & -4 \\ 1 & 4 \\ 4 & -1 \\ 4 & 4 \end{pmatrix},\qquad \mathbf{S}_2 = \begin{pmatrix} 399 & 0 \\ 0 & 133 \end{pmatrix},\qquad \mathbf{V}_2 = \frac{1}{19}\begin{pmatrix} 6 & 15 \\ 10 & 6 \\ 15 & -10 \end{pmatrix}.$$
On admet que $\mathbf{M} = \mathbf{U}_2\mathbf{S}_2\mathbf{V}_2^\top$ (la troisième valeur singulière est nulle) et que ces vecteurs singuliers suivent la convention de signe de M12d. Pour $\beta \in [0, 1]$, on pose $\mathbf{A}_\beta = \mathbf{U}_2\mathbf{S}_2^\beta$ (une ligne par magasin) et $\mathbf{B}_\beta = \mathbf{V}_2\mathbf{S}_2^{1-\beta}$ (une ligne par produit).

| | Question | Réponse attendue |
|---|---|---|
| a | les contributions des deux termes $s_1\mathbf{u}_1\mathbf{v}_1^\top$ et $s_2\mathbf{u}_2\mathbf{v}_2^\top$ à la case (magasin 3, produit 2) | une liste de 2 nombres |
| b | $\mathbf{A}_1$ | une matrice $4 \times 2$ |
| c | $\mathbf{B}_0$ | une matrice $3 \times 2$ |
| d | $\cos(\text{magasin 1}, \text{magasin 4})$, entre les lignes de $\mathbf{A}_\beta$, pour $\beta = 0$, $\frac12$ et 1 | une liste de 3 nombres |
| e | $\cos(\text{magasin 1}, \text{magasin 2})$, entre les lignes de $\mathbf{A}_\beta$, pour $\beta = 0$, $\frac12$ et 1 | une liste de 3 nombres (4 décimales) |
| f | vrai ou faux : $\mathbf{A}_\beta\mathbf{B}_\beta^\top = \mathbf{M}$ pour tout $\beta \in [0, 1]$ | `True` ou `False` |

Dans ta copie : écris la première ligne de $\mathbf{A}_{1/2}$ et celle de $\mathbf{B}_{1/2}$ (3 décimales), et vérifie que leur produit scalaire redonne $M_{11}$ ; calcule le cosinus des lignes 1 et 4 de $\mathbf{M}$ elle-même, et compare-le à d) : pour quelle valeur de $\beta$ le retrouve-t-on, et pourquoi ? ; dis ce que $\beta$ change à la forme du nuage des quatre magasins dans le plan des deux colonnes de $\mathbf{A}_\beta$.

### Ex MB2.5 — Une bannière affichée 3 200 fois et cliquée 50 fois : le logit de vraisemblance maximale, puis un non-clic gardé sur 9, le décalage de ln 9 et sa correction ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer le logit de vraisemblance maximale d'un taux, puis le décalage que crée un sous-échantillonnage des négatifs, et le corriger.
**Prérequis :** fiche §5 ; R6 (logit, sigmoïde), M13a (maximum de vraisemblance de Bernoulli) · **Parcours :** C, E

Une bannière publicitaire a été affichée 3 200 fois et cliquée 50 fois. Pour alléger ses fichiers, la régie ne garde que des échantillons : tous les clics, et chaque non-clic avec la probabilité $\frac19$, au hasard. On suppose qu'elle garde exactement un non-clic sur 9.

| | Question | Réponse attendue |
|---|---|---|
| a | le taux de clic observé sur les 3 200 affichages | une fraction irréductible |
| b | le logit de vraisemblance maximale de ce taux | un nombre (3 décimales) |
| c | le logit du taux de clic de l'échantillon gardé | un nombre (3 décimales) |
| d | l'écart entre le logit de c) et celui de b) | un nombre (3 décimales) |
| e | la probabilité de clic que lirait, pour cette bannière, un modèle ajusté sur l'échantillon, sans correction | une fraction irréductible |
| f | ce modèle lit la probabilité 0,2 pour une autre bannière : la probabilité de clic corrigée, pour la population | une fraction irréductible |

Dans ta copie : écris le nombre de non-clics et le nombre d'exemples de l'échantillon ; montre que b) vaut $-\ln 63$ et c) $-\ln 7$ ; dis pourquoi l'écart d) vaut $\ln 9$ (la cote est multipliée par 9) ; écris la correction : que retranche-t-on au logit lu par le modèle ? ; vérifie f) en passant par la cote ; dis ce qui arriverait à la correction si la régie gardait plus de non-clics le soir que le matin.

### Ex MB2.6 — Yaourt et fromage blanc, nature et sucrés : mesurer le parallélogramme d'une analogie (défaut, rapport ε, borne du cosinus), et dire si d peut l'emporter sur c ✏️ ★★ ⏱️ 25 min
**Objectif :** mesurer le parallélogramme d'une analogie, appliquer la borne du cosinus de la fiche à $\mathbf{c}$ et à $\mathbf{d}$, et comprendre pourquoi on exclut les points de la question.
**Prérequis :** fiche §6 ; M07 (cosinus, normes) · **Parcours :** C, E

Quatre aliments sont décrits par leurs teneurs en protéines, glucides et lipides, en grammes pour 100 g : le yaourt nature $\mathbf{a} = (4, 5, 3)$, le yaourt sucré $\mathbf{b} = (4, 10, 3)$, le fromage blanc nature $\mathbf{c} = (8, 4, 3)$ et le fromage blanc sucré $\mathbf{d} = (7, 9, 3)$. L'analogie « le yaourt nature est au yaourt sucré ce que le fromage blanc nature est à ? » a pour requête $\mathbf{q} = \mathbf{b} - \mathbf{a} + \mathbf{c}$. La fiche montre que si $\lVert\mathbf{b} - \mathbf{a}\rVert \le \varepsilon\lVert\mathbf{c}\rVert$ avec $\varepsilon < 1$, alors $\cos(\mathbf{q}, \mathbf{c}) \ge \sqrt{1 - \varepsilon^2}$.

| | Question | Réponse attendue |
|---|---|---|
| a | la requête $\mathbf{q}$ | une liste de 3 nombres |
| b | le défaut du parallélogramme, $\delta = \lVert(\mathbf{b} - \mathbf{a}) - (\mathbf{d} - \mathbf{c})\rVert$ | un nombre |
| c | $\varepsilon = \lVert\mathbf{b} - \mathbf{a}\rVert / \lVert\mathbf{c}\rVert$, puis la borne $\sqrt{1 - \varepsilon^2}$ | une liste de 2 nombres (3 décimales) |
| d | $\cos(\mathbf{q}, \mathbf{c})$ | un nombre (3 décimales) |
| e | la borne de la fiche appliquée à $\mathbf{d}$, avec $\mathbf{q} = \mathbf{d} + \big((\mathbf{b} - \mathbf{a}) - (\mathbf{d} - \mathbf{c})\big)$ : $\sqrt{1 - \delta^2/\lVert\mathbf{d}\rVert^2}$ | un nombre (4 décimales) |
| f | vrai ou faux : $\cos(\mathbf{q}, \mathbf{d}) > \cos(\mathbf{q}, \mathbf{c})$ | `True` ou `False` |
| g | l'alignement des deux décalages, $\cos(\mathbf{b} - \mathbf{a}, \mathbf{d} - \mathbf{c})$ | un nombre (4 décimales) |
| h | on remplace $\mathbf{c}$ par la crème fraîche, $(2, 3, 30)$ : $\varepsilon$, la borne $\sqrt{1 - \varepsilon^2}$, puis $\cos(\mathbf{q}, \text{crème})$, avec la nouvelle requête | une liste de 3 nombres (4 décimales) |

Dans ta copie : justifie f) **sans** calculer $\cos(\mathbf{q}, \mathbf{d})$, avec d) et e) ; dis ce que mesure g), et ce qu'il vaudrait pour un parallélogramme parfait ; pour h), compare la borne et le cosinus, et dis pourquoi, dans une recherche de voisins, on exclut $\mathbf{a}$, $\mathbf{b}$ et $\mathbf{c}$ des candidats.

### Ex MB2.7 — Des mesures d'animaux en logarithme : la direction de taille estimée sur deux différences, la retirer de trois animaux, et les distances qui restent ✏️ ★★ ⏱️ 25 min
**Objectif :** estimer une direction comme le premier axe de différences, la retirer d'un nuage, et dire quelles distances changent.
**Prérequis :** fiche §7 ; M07 (projection sur une droite), M12b (complément orthogonal), M12d (premier axe), M28 (matrice de Gram) · **Parcours :** C, E

Un zoologiste décrit des petits mammifères par trois longueurs : le corps, la queue et l'oreille, en centimètres, et en prend les logarithmes en base 2. Grandir sans changer de forme multiplie les trois longueurs par un même facteur, donc ajoute une même constante aux trois logarithmes. Pour estimer la direction de taille, il compare deux paires d'animaux de même espèce, un grand et un petit : leurs différences de logarithmes sont $\mathbf{d}_1 = (2, 4, 3)$ et $\mathbf{d}_2 = (4, 2, 3)$, les lignes de $\mathbf{D}$, de forme $(2, 3)$. La direction de taille est le premier axe $\mathbf{u}$ des lignes de $\mathbf{D}$ (non centrées), le vecteur unitaire qui maximise $\lVert\mathbf{D}\mathbf{u}\rVert$, de première coordonnée positive. Trois animaux ont pour logarithmes $\mathbf{x}_1 = (2, 3, 4)$, $\mathbf{x}_2 = (3{,}5 ;\ 4{,}5 ;\ 5{,}5)$ et $\mathbf{x}_3 = (5, 3, 4)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice de Gram $\mathbf{G} = \mathbf{D}\mathbf{D}^\top$ des deux différences | une matrice $2 \times 2$ |
| b | la plus grande valeur propre de $\mathbf{G}$ | un nombre |
| c | le premier axe $\mathbf{u}$ | une liste de 3 nombres (3 décimales) |
| d | les trois animaux après le retrait de la direction $\mathbf{u}$, $\mathbf{x} \mapsto \mathbf{x} - (\mathbf{x}\cdot\mathbf{u})\,\mathbf{u}$, une ligne par animal | une matrice $3 \times 3$ |
| e | la distance de l'animal 1 à l'animal 3, avant puis après le retrait | une liste de 2 nombres (4 décimales) |
| f | $\big((\mathbf{x}_1 - \mathbf{x}_3)\cdot\mathbf{u}\big)^2$ | un nombre |

Dans ta copie : trouve un vecteur propre de $\mathbf{G}$ pour b), et déduis $\mathbf{u}$ de $\mathbf{D}^\top$ fois ce vecteur (M28 : on travaille avec la plus petite des deux matrices de Gram) ; montre que retirer $\mathbf{u}$ revient à soustraire à chaque animal la moyenne de ses trois coordonnées (M20) ; dis ce que deviennent les animaux 1 et 2, et pourquoi ; vérifie le théorème de Pythagore avec e) et f) ; dis ce que le retrait de la taille ne retire pas : si la longueur de la queue est corrélée à la taille dans une autre direction, que reste-t-il ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex MB2.8 — La PMI est majorée par −ln p(x) et par −ln p(y), avec égalité quand x n'arrive qu'avec y ; la PMI normalisée est donc au plus 1 ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la borne des événements rares et l'encadrement de la PMI normalisée, et voir pourquoi les événements rares ont les PMI les plus grandes possibles.
**Prérequis :** fiche §2 ; R6 (croissance de ln), M03 (marginales, loi conditionnelle) · **Parcours :** C, E

$X$ et $Y$ ont une loi jointe $p(x, y)$, de marges $p(x)$ et $p(y)$. On fixe une case $(x, y)$ telle que $p(x, y) > 0$ (donc $p(x) > 0$ et $p(y) > 0$).
1. Montre que $p(x, y) \le p(x)$ et $p(x, y) \le p(y)$. Déduis-en $\operatorname{PMI}(x, y) \le -\ln p(y)$ et $\operatorname{PMI}(x, y) \le -\ln p(x)$, donc $\operatorname{PMI}(x, y) \le \min\big(-\ln p(x), -\ln p(y)\big)$.
2. Montre que $\operatorname{PMI}(x, y) = -\ln p(y)$ si et seulement si $P(Y = y \mid X = x) = 1$, c'est-à-dire si $x$ n'arrive qu'avec $y$.
3. Soit $c > 0$. Déduis de 1 qu'une case de PMI au moins $c$ a $p(x) \le e^{-c}$ et $p(y) \le e^{-c}$ : seules deux valeurs rares peuvent avoir une grande PMI.
4. On suppose $p(x, y) < 1$ et l'on pose $\operatorname{NPMI}(x, y) = \operatorname{PMI}(x, y)/\big(-\ln p(x, y)\big)$, la PMI normalisée. Montre que $\operatorname{NPMI}(x, y) \le 1$, avec égalité si et seulement si $p(x, y) = p(x) = p(y)$, c'est-à-dire si $x$ et $y$ arrivent toujours ensemble.

**Pour aller plus loin.** Montre que $\operatorname{NPMI}(x, y) > -1$.

### Ex MB2.9 — Répartir les valeurs singulières entre deux facteurs : le produit ne dépend pas de β, les produits scalaires des lignes si ∂ ★★★ ⏱️ 30 min
**Objectif :** démontrer ce qui dépend du choix de $\beta$ et ce qui n'en dépend pas, et le cas d'une matrice symétrique semi-définie positive.
**Prérequis :** fiche §4 ; M12c (théorème spectral), M12d (SVD compacte), M28 (matrice de Gram) · **Parcours :** C

$\mathbf{M}$, de forme $(m, n)$ et de rang $r$, a pour SVD compacte $\mathbf{M} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$, avec $\mathbf{U}^\top\mathbf{U} = \mathbf{V}^\top\mathbf{V} = \mathbf{I}_r$ et $\mathbf{S} = \operatorname{diag}(s_1, \ldots, s_r)$, $s_1 \ge \cdots \ge s_r > 0$. Pour $k \le r$, $\mathbf{U}_k$, $\mathbf{S}_k$ et $\mathbf{V}_k$ gardent les $k$ premières colonnes (et valeurs singulières), $\mathbf{M}_k = \mathbf{U}_k\mathbf{S}_k\mathbf{V}_k^\top$, et, pour $\beta \in [0, 1]$, $\mathbf{A}_\beta = \mathbf{U}_k\mathbf{S}_k^\beta$ et $\mathbf{B}_\beta = \mathbf{V}_k\mathbf{S}_k^{1-\beta}$.
1. Montre que $\mathbf{A}_\beta\mathbf{B}_\beta^\top = \mathbf{M}_k$ pour tout $\beta$.
2. Montre que $\mathbf{A}_\beta\mathbf{A}_\beta^\top = \mathbf{U}_k\mathbf{S}_k^{2\beta}\mathbf{U}_k^\top$. Déduis-en que les produits scalaires entre les lignes de $\mathbf{A}_1$ sont ceux des lignes de $\mathbf{M}_k$, et que ceux des lignes de $\mathbf{A}_0$ sont ceux des lignes de $\mathbf{U}_k$.
3. Montre que, si $s_1 = \cdots = s_k$, les cosinus entre les lignes de $\mathbf{A}_\beta$ ne dépendent pas de $\beta$. Avec les magasins de MB2.4, donne deux lignes dont le cosinus en dépend.
4. On suppose $\mathbf{M}$ carrée, symétrique et semi-définie positive (M12c). Montre qu'on peut prendre $\mathbf{V} = \mathbf{U}$ dans sa SVD compacte, puis que $\mathbf{A}_{1/2} = \mathbf{B}_{1/2}$ et $\mathbf{M}_k = \mathbf{A}_{1/2}\mathbf{A}_{1/2}^\top$ : les lignes de $\mathbf{A}_{1/2}$ sont des points dont $\mathbf{M}_k$ est la matrice de Gram (M28).

### Ex MB2.10 — Sous-échantillonner une classe : par la formule de Bayes, la cote observée est celle de la population multipliée par le rapport des taux de sélection s₁/s₀ ; dans un modèle logistique, seule l'ordonnée à l'origine bouge, de ln(s₁/s₀) ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer par la formule de Bayes l'effet d'une étude cas-témoins sur la cote et sur un modèle logistique, et en tirer la correction.
**Prérequis :** fiche §5 ; R6 (cote, logit), M04 (formule de Bayes), M13a (régression logistique, maximum de vraisemblance de Bernoulli) · **Parcours :** C, E

Dans une population, chaque exemple a des features $\mathbf{x}$ et un label $y \in \{0, 1\}$ ; on note $\pi(\mathbf{x}) = P(y = 1 \mid \mathbf{x})$. Une étude **cas-témoins** garde chaque positif avec la probabilité $s_1$ et chaque négatif avec la probabilité $s_0$ ($0 < s_0, s_1 \le 1$), indépendamment de $\mathbf{x}$ et des autres exemples ; $G$ est l'événement « l'exemple est gardé ».
1. Écris $P(y = 1 \mid \mathbf{x}, G)$ en fonction de $\pi(\mathbf{x})$, $s_1$ et $s_0$, par la formule de Bayes.
2. Déduis-en que la cote d'un positif dans l'échantillon est celle de la population multipliée par $\frac{s_1}{s_0}$, puis que $\operatorname{logit} P(y = 1 \mid \mathbf{x}, G) = \operatorname{logit}\pi(\mathbf{x}) + \ln\frac{s_1}{s_0}$.
3. On suppose que la population suit un modèle logistique, $\operatorname{logit}\pi(\mathbf{x}) = \theta_0 + \boldsymbol{\theta}^\top\mathbf{x}$. Montre que l'échantillon suit encore un modèle logistique, de mêmes poids $\boldsymbol{\theta}$, et d'ordonnée à l'origine $\theta_0 + \ln\frac{s_1}{s_0}$.
4. Sans features, l'échantillon compte $a$ positifs et $b$ négatifs ($a, b > 0$), et le logit de vraisemblance maximale du taux de l'échantillon est $\ln\frac{a}{b}$ (M13a). Déduis-en un estimateur du logit de la population.
5. On suppose maintenant que le taux de sélection des négatifs dépend de $\mathbf{x}$, avec $\ln s_0(\mathbf{x}) = \gamma_0 + \boldsymbol{\gamma}^\top\mathbf{x}$. Reprends 2 et 3 : montre que l'échantillon suit encore un modèle logistique, et donne ses poids et son ordonnée à l'origine. Que se passe-t-il si $\ln s_0(\mathbf{x})$ n'est pas une fonction affine de $\mathbf{x}$ ?

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex MB2.11 — Pont : résumer des séries de relevés de longueurs différentes par une moyenne masquée, montrer que le remplissage ne change rien, et compter les comparaisons par paires 🔗 ★ ⏱️ 15 min
**Objectif :** calculer une moyenne masquée de vecteurs, voir pourquoi le remplissage ne la change pas, et comparer le coût de comparaisons par paires à celui d'un résumé par élément.
**Prérequis :** fiche §8 ; R1 (moyenne pondérée), R8 (combinaisons), M20 (réductions le long d'un axe) · **Parcours :** C, E

Trois capteurs plantés dans un champ envoient des séries de relevés (température du sol en °C, humidité du sol en %) de longueurs différentes. Pour les ranger dans un même tableau $\mathbf{H}$ de forme $(3, 4, 2)$, on complète chaque série par des relevés $(0, 0)$, et un masque $m_t$ vaut 1 pour un vrai relevé et 0 pour un relevé de remplissage. Le résumé d'un capteur est la moyenne masquée $\frac{\sum_tm_t\mathbf{h}_t}{\sum_tm_t}$.
- capteur A : $(12, 80)$, $(15, 71)$, $(18, 62)$, puis un relevé de remplissage ;
- capteur B : $(9, 88)$, $(11, 84)$, puis deux relevés de remplissage ;
- capteur C : $(20, 55)$, $(22, 49)$, $(19, 58)$, $(23, 46)$.

Pour comparer les capteurs d'un réseau, deux méthodes : un modèle **par paires** lit deux séries ensemble et rend leur ressemblance, en un passage par paire ; un modèle **de résumé** lit chaque série une fois, en un passage par capteur, puis toutes les ressemblances se calculent d'un coup, par un produit matriciel des résumés.

| | Question | Réponse attendue |
|---|---|---|
| a | la moyenne masquée du capteur A | une liste de 2 nombres |
| b | la moyenne masquée du capteur B | une liste de 2 nombres |
| c | vrai ou faux : compléter les trois séries jusqu'à 6 relevés ne change aucune moyenne masquée | `True` ou `False` |
| d | pour un réseau de 300 capteurs, le nombre de passages du modèle par paires, pour comparer toutes les paires | un entier |
| e | combien de fois plus de passages le modèle par paires demande-t-il que le modèle de résumé, pour ces 300 capteurs ? | un nombre |

Dans ta copie : écris la moyenne **sans** masque du capteur A complété, et dis ce qui la fausse ; montre en une ligne que les relevés de masque 0 ne comptent ni au numérateur ni au dénominateur ; écris le produit matriciel qui donne, à partir de la matrice $\mathbf{R}$ des résumés (une ligne par capteur, de forme $(300, 2)$), tous les produits scalaires entre capteurs, et compte ses multiplications ; dis comment e) grandit avec le nombre de capteurs. Dans workbookIA B2, la même moyenne masquée résume une suite de vecteurs de longueur variable, et le même compte de paires explique pourquoi l'on calcule un vecteur par élément avant de comparer.

### Ex MB2.12 — Expliquer à un ornithologue ce que mesure la PMI d'un milieu et d'une espèce, et pourquoi une espèce vue une seule fois a la plus grande 🗣️ ★ ⏱️ 15 min
**Objectif :** expliquer sans formule ce que mesure une PMI, et pourquoi les événements rares ont les PMI les plus grandes et les moins sûres.
**Prérequis :** fiche §2 et §3 ; MB2.2 · **Parcours :** C, E

L'ornithologue de MB2.2 a vu une table de PMI, où la case (prairie, huppe) arrive en tête, et te demande ce que cela veut dire : « la huppe est-elle vraiment l'oiseau de la prairie ? ».

Réponds-lui en 6 à 10 phrases, sans formule : ce que mesure la PMI d'un milieu et d'une espèce (combien de fois plus souvent on les voit ensemble que si l'espèce ne dépendait pas du milieu) ; ce que veulent dire une PMI positive, nulle, négative, et une case jamais observée ; pourquoi une espèce vue une seule fois obtient la plus grande PMI possible pour son milieu ; pourquoi ce record ne dit presque rien (une seule huppe : une deuxième, vue ailleurs, le ferait tomber) ; et ce qu'on fait pour s'en protéger (le lissage, qui fait baisser les espèces rares, ou un nombre minimal d'observations). Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

Réponds **à voix haute**, en une minute, comme face à un recruteur ; puis compare avec la « réponse modèle en 60 secondes » de `05_solutions.md`.

### MB2.E1 — « Pourquoi ne centre-t-on pas une grande table de comptages creuse avant de la factoriser par une SVD tronquée ? » 💼 ★ ⏱️ 10 min
*Fiche §4 · parcours C*

« Pourquoi ne centre-t-on pas une grande table de comptages creuse avant de la factoriser par une SVD tronquée ? »

Ta réponse doit dire ce que coûte le centrage (la table devient pleine : un ordre de grandeur chiffré de la mémoire, avant et après) ; ce que fait la SVD tronquée d'une table non centrée (la meilleure approximation de la table elle-même, par Eckart-Young, et non de ses écarts à la moyenne) ; ce que capte alors le premier axe (le profil moyen, la « taille » des lignes) ; ce que ce premier axe fait aux cosinus entre lignes (commun à toutes, il les rapproche de 1, d'autant plus que β est grand) et comment l'atténuer (un β plus petit, ou ne garder que les axes suivants) ; et comment centrer sans écrire la table pleine si on le veut vraiment (la table moins une matrice de rang 1, en ne formant que des produits par un vecteur).

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/mb2_cooccurrences/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et au 🔗 ci-dessus. **Dans le notebook, donne les valeurs que rend le calcul, sans les arrondir** : les décimales demandées ci-dessous sont celles à écrire dans ta copie.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| MB2.13 | La table des PMI d'une loi jointe, −∞ sur les cases vides · `pmi` | 🔨 | ★ | 35 | C, E |
| MB2.14 | Deux briques : le logit d'une population estimé sur un échantillon cas-témoins, et retirer une direction des lignes d'une matrice · `case_control_logit`, `remove_direction` | 🔨 | ★★ | 45 | C, E |
| MB2.15 | Prédire puis mesurer la dispersion de la PMI estimée sur 400 observations, pour une case rare et une case fréquente, avec et sans lissage | 🔮 | ★★ | 35 | C |
| MB2.16 | Des magasins dans le plan des deux facteurs U₂S₂^β, pour β = 0, ½ et 1 : ce qui s'étire, et les angles qui changent | 🎨 | ★ | 40 | C |
| MB2.17 | Chasse à l'erreur : une PMI calculée sans le total, des facteurs U S^β et V S^β, une direction retirée sans diviser par u·u | 🐛 | ★ | 30 | C, E |
| MB2.18 | Un test de propriété de `pmi` sur des tables tirées au hasard : la borne, la transposition, et la moyenne qui redonne l'information mutuelle de M06 | 🛠️ | ★ | 40 | C |
| MB2.19 | Défi : retrouver, sur 3 000 observations, les cinq paires les plus associées d'une table cachée de 10 × 10, sans se laisser piéger par les cases rares | 🏆 | ★★★ | 50 | C |

Ce que tu feras dans chacun (l'énoncé complet, avec ses cellules, est dans le notebook). Les deux 🔨 complètent ta copie `mon_travail/mymath/cooccurrence.py` (**mymath :** `cooccurrence.py`), dont la docstring du module dit ce qui est permis : NumPy et le module `math`, mais aucune fonction de SciPy (`scipy.special.logit`, `scipy.special.xlogy`) ni de scikit-learn (`mutual_info_score`) : les tests comparent tes résultats avec elles ; des logarithmes népériens ; une loi jointe de probabilités, jamais des comptes ; ne jamais modifier les tableaux reçus. Chaque 🔨 lance le groupe de tests de ses fonctions dans `tests/test_mb2_cooccurrence.py`, puis s'en sert ; dans le notebook, tu les appelles par `mymath.cooccurrence.<nom>(…)`. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy, et de tes fonctions de M06 (`info`), de M12d (`svd_pca`) et de M28 (`sampling`). Les données des exercices papier (les oiseaux, les magasins, la bannière, les animaux) sont recopiées dans une cellule du notebook.

**MB2.13 · 🔨 `pmi(joint)`.** Écris la fonction, en suivant sa docstring : contrôle la table (2-D, non vide, des nombres finis $\ge 0$, pas des booléens, de somme 1 à $10^{-9}$ près) ; calcule les marges $p(x)$ (sommes des lignes) et $p(y)$ (sommes des colonnes), en colonne et en ligne pour qu'elles se diffusent (M20) ; pars d'une table remplie de `-np.inf`, et calcule le logarithme du rapport sur les seules cases de probabilité non nulle, sans avertissement de NumPy ; rends un tableau de flottants de la forme de la table. Lance le groupe de tests. Ensuite : a) la table des PMI de la loi des oiseaux de MB2.2, à comparer à ta copie ; b) la moyenne $\sum p(x, y)\operatorname{PMI}(x, y)$ sur les cases non vides, puis vrai ou faux : elle est égale, à $10^{-12}$ près, à `mymath.info.mutual_information(P, base=math.e)` (M06 compte en bits par défaut) ; c) vrai ou faux : `pmi(P.T)` est égale à la transposée de `pmi(P)`, à $10^{-12}$ près, avec $-\infty$ aux mêmes places ; d) pour la loi $\mathbf{Q} = \begin{pmatrix} 0{,}25 & 0 & 0{,}15 \\ 0 & 0 & 0 \\ 0{,}2 & 0 & 0{,}4 \end{pmatrix}$, qui a une ligne et une colonne vides : le nombre de cases de PMI $-\infty$. Ce qu'il faut regarder : que font une ligne vide et une colonne vide ? Que fait à la table des PMI la transposition de la loi ? La moyenne des PMI est-elle l'information mutuelle de M06, et que change l'unité du logarithme ?

**MB2.14 · 🔨 `case_control_logit(n_positive, n_negative, keep_positive=1.0, keep_negative=1.0)` et `remove_direction(X, u)`.** Écris les deux fonctions, en suivant leurs docstrings. `case_control_logit` : contrôle les deux taux (dans $]0, 1]$, ni `nan` ni booléen), puis les nombres d'exemples (finis, $\ge 0$, pas des booléens, refusés avant la conversion en flottants) ; diffuse-les (`np.broadcast_arrays`) ; traite les trois cas case par case (les deux nombres positifs : le logarithme du rapport, moins celui des taux ; seul $n_1 > 0$ : $+\infty$ ; seul $n_0 > 0$ : $-\infty$), et refuse une case où les deux sont nuls ; rends un `float` quand la forme diffusée est `()`. `remove_direction` : contrôle $\mathbf{X}$ (1-D ou 2-D, non vide, des nombres finis) et $\mathbf{u}$ (1-D, de la longueur des lignes, non nul) ; calcule les coefficients $\mathbf{x}\cdot\mathbf{u}/\mathbf{u}\cdot\mathbf{u}$ de toutes les lignes en un produit matrice-vecteur, puis retire coefficient fois $\mathbf{u}$ à chaque ligne (un produit extérieur, ou la diffusion). Lance les deux groupes de tests. Ensuite : a) la bannière de MB2.5 : `case_control_logit(50, 350, keep_negative=1/9)`, à comparer à ta réponse b) de MB2.5 ; b) trois bannières d'un même échantillon, de 50, 12 et 0 clics, et de 350, 40 et 25 non-clics gardés, avec le même taux $\frac19$ : les trois logits de la population, en un appel ; c) une étude cas-témoins garde chaque positif avec la probabilité 0,8 et chaque négatif avec la probabilité 0,025, et compte 30 positifs et 120 négatifs : le logit de la population, puis la probabilité d'un positif dans la population ; d) les trois animaux de MB2.7 sans la direction $(1, 1, 1)$, à comparer à ta réponse d), puis vrai ou faux : la direction $(-2, -2, -2)$ donne le même résultat ; e) $\lVert\mathbf{x}_1 - \mathbf{x}_3\rVert^2 - \lVert\mathbf{r}_1 - \mathbf{r}_3\rVert^2$, où $\mathbf{r}_i$ est l'animal $i$ après le retrait. Ce qu'il faut regarder : que devient le logit d'une bannière sans clic, avant et après la correction ? Que demande la correction d'un sous-échantillonnage fort des négatifs ? Le retrait d'une direction dépend-il de la longueur de $\mathbf{u}$, et de son sens ?

**MB2.15 · 🔮 Prédire puis mesurer la dispersion de la PMI estimée sur 400 observations.** La loi des oiseaux de MB2.2 est celle d'une région. Un observateur n'y voit que 400 oiseaux, tirés au hasard selon cette loi, et estime les PMI par `pmi(comptes / 400)`, puis, avec le lissage de MB2.3, par $\ln\frac{\hat p(x, y)}{\hat p(x)\,\hat p_\alpha(y)}$, où $\hat p_\alpha$ est la marge des espèces de l'échantillon tempérée à $T = 3$ (`mymath.sampling.temper`). On suit trois cases : (prairie, huppe), dont l'espèce est rare et n'est vue qu'en prairie ; (prairie, pic), une case rare d'une espèce présente ailleurs ; (village, moineau), une case fréquente. **Avant d'exécuter**, prédis : a) la probabilité qu'un échantillon de 400 oiseaux ne contienne aucune huppe, ce qui rend $-\infty$ la PMI estimée de (prairie, huppe) (un nombre, 3 décimales, que tu calcules à la main) ; b) celle des trois cases dont la PMI estimée (finie) est la plus dispersée : (A) (prairie, huppe) ; (B) (prairie, pic) ; (C) (village, moineau) ; c) avec le lissage, l'écart-type de la PMI estimée de (prairie, huppe) : (A) diminue nettement ; (B) reste à peu près le même ; (C) augmente nettement. Puis écris `pmi_samples_15(rng, n_rep, n_obs=400)`, qui tire `n_rep` échantillons, chacun par `rng.multinomial(n_obs, P.ravel())` remis à la forme $(3, 4)$, et rend deux tableaux de forme `(n_rep, 3)` : les PMI estimées des trois cases, dans l'ordre ci-dessus, sans puis avec lissage ($-\infty$ compris). `pmi_samples_15` lit `P` au moment de l'appel ; la vérification l'essaie sur des appels cachés, dont un sur une autre loi. Avec `rng = np.random.default_rng(7115)` et 1 000 échantillons, relève : d) la proportion des échantillons où la PMI estimée de (prairie, huppe) vaut $-\infty$ ; e) l'écart-type (`ddof=1`) des valeurs finies de chaque case, sans puis avec lissage, une ligne par case ; f) les vraies valeurs, $\operatorname{PMI}$ et $\operatorname{PMI}_\alpha$ de la loi de la région, une ligne par case ; g) vrai ou faux : pour les deux cases rares, la moyenne des estimations lissées **finies** est **plus proche** de la vraie $\operatorname{PMI}_\alpha$ que de la vraie PMI. Ce qu'il faut regarder (après l'expérience) : qu'est-ce qui rend une estimation dispersée ? Comment se comportent les deux cases rares, (prairie, huppe) et (prairie, pic), quand la huppe est vue et quand elle ne l'est pas ? Que fait le lissage à la cible, et à la dispersion ?

**MB2.16 · 🎨 Des magasins dans le plan des deux facteurs U₂S₂^β.** Le notebook fournit `M_16`, les ventes hebdomadaires (en dizaines d'articles) de cinq produits (pain, fruits, œufs, vis, peinture) dans dix magasins : trois épiceries, trois quincailleries et quatre bazars, et `SHOPS_16`, leurs noms. Écris `factor_rows_16(M, beta, k=2)`, qui rend $\mathbf{U}_k\mathbf{S}_k^\beta$ par ta fonction `mymath.svd_pca.svd` (M12d, avec sa convention de signe), puis `draw_factors_16(axes, M, betas, names)`, qui reçoit une ligne de trois axes et, pour chaque $\beta$ de `betas`, place les magasins dans le plan des deux colonnes de $\mathbf{U}_2\mathbf{S}_2^\beta$ (un point et le nom de chaque magasin, pris dans `names`, une même échelle sur les deux axes (`ax.set_aspect("equal")`), des noms d'axes, et en titre $\beta$ et le rapport des longueurs (normes) de la première et de la seconde colonne) ; elle rend la liste des trois tableaux tracés. Les deux fonctions dessinent dans les axes reçus, sans ouvrir de figure. La vérification appelle `draw_factors_16` avec $\beta = 0$, $\frac12$ et 1, affiche la figure, compare tes tableaux aux réponses enregistrées, et essaie tes fonctions sur une autre table, d'autres $\beta$ et $k = 3$. Relève : a) les trois plus grandes valeurs singulières de `M_16` (2 décimales) ; b) le cosinus de l'épicerie A et de la quincaillerie A entre les lignes de $\mathbf{U}_2\mathbf{S}_2^\beta$, pour $\beta = 0$, $\frac12$ et 1 (3 décimales) ; c) le même pour les bazars A et B ; d) le rapport des longueurs des deux colonnes de $\mathbf{U}_2\mathbf{S}_2^\beta$, pour les trois $\beta$ (3 décimales) ; e) vrai ou faux : les cosinus entre les lignes de $\mathbf{U}_2\mathbf{S}_2$ sont ceux des lignes de $\mathbf{M}_2$, l'approximation de rang 2 (`mymath.svd_pca.low_rank_approximation`), à $10^{-9}$ près ; f) vrai ou faux : ce sont ceux des lignes de `M_16` elle-même, à $10^{-9}$ près. Ce qu'il faut regarder : que devient le nuage quand $\beta$ monte, et le long de quel axe ? Les magasins semblent-ils se rapprocher ou s'éloigner les uns des autres ? Quels angles $\beta = 1$ garde-t-il ?

**MB2.17 · 🐛 Chasse à l'erreur.** Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe.
- (1) `pmi_from_counts(C)` doit rendre la table des PMI d'une table de **comptes** ; elle calcule `np.log(C / np.outer(C.sum(1), C.sum(0)))` sur les cases non nulles, et $-\infty$ ailleurs. Il l'a vérifiée sur une loi jointe : elle redonne `pmi`.
- (2) `split_factors(U, s, Vt, beta)` doit rendre les deux facteurs $\mathbf{U}\mathbf{S}^\beta$ et $\mathbf{V}\mathbf{S}^{1-\beta}$ d'une SVD compacte ; elle rend `U * s ** beta, Vt.T * s ** beta`. Il l'a vérifiée avec $\beta = \frac12$ sur les magasins de MB2.4 : le produit des deux facteurs redonne $\mathbf{M}$.
- (3) `remove_direction_bad(X, u)` doit retirer la direction $\mathbf{u}$ de chaque ligne de $\mathbf{X}$ ; elle rend `X - np.outer(X @ u, u)`. Il l'a vérifiée avec $\mathbf{u} = (0 ;\ 0{,}6 ;\ 0{,}8)$ sur les animaux de MB2.7 : elle redonne `remove_direction`.

Trouve et corrige chaque erreur (les fonctions corrigées s'appellent `pmi_from_counts_fixed`, `split_factors_fixed` et `remove_direction_fixed`, avec les mêmes arguments), puis réponds : a) pour la table des comptes des oiseaux de MB2.2, $\operatorname{PMI}(\text{forêt}, \text{pic})$ par `pmi_from_counts_fixed`, puis par `pmi_from_counts` ; b) pour les magasins de MB2.4, avec $\beta = 1$ : la case (1, 1) (en haut à gauche) du produit des deux facteurs de `split_factors_fixed`, puis de `split_factors` (la SVD par `mymath.svd_pca.svd`) ; c) l'animal 1 de MB2.7 sans la direction $(1, 1, 1)$, par `remove_direction_fixed`, puis par `remove_direction_bad` (une liste de 6 nombres). Pour chacune des trois erreurs, dis aussi pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : des tables de comptes de totaux variés, d'autres $\beta$ et d'autres matrices, des directions de normes diverses.

**MB2.18 · 🛠️ Un test de propriété.** Le notebook fournit la boucle du test, `pmi_property_test_18(n_trials, rng, func=None, rtol=1e-9, checks=None)` : quand `func` vaut `None`, elle prend `mymath.cooccurrence.pmi` **au moment de l'appel**, et, quand `checks` vaut `None`, ta fonction `failed_checks_18` ; pour chacun des `n_trials` essais, dans cet ordre, elle tire `m = int(rng.integers(1, 6))`, `n = int(rng.integers(1, 6))`, `W = rng.random((m, n)) ** 2`, puis, si `rng.random() < 0.4`, met à 0 les cases où `rng.random((m, n)) < 0.3` (des cases vides) ; si `W` est nulle, elle met `W[0, 0] = 1` ; elle divise `W` par sa somme, appelle `checks(P, f, rtol)`, où `f` est la fonction testée, et ajoute 1 au compteur de chaque nom rendu ; elle rend le dictionnaire des trois compteurs d'essais `"bound"`, `"transpose"` et `"mean"`. Écris les contrôles, `failed_checks_18(P, func, rtol=1e-9)`, qui rend l'ensemble des noms des contrôles qui échouent pour la loi `P` : avec `T = func(P)`, `"bound"` échoue si `T` n'a pas la forme de `P`, si une case de probabilité non nulle a une PMI non finie, ou si l'une d'elles dépasse $\min(-\ln p(x), -\ln p(y))$ de plus de $\texttt{rtol}\cdot\max(1, \lvert\text{borne}\rvert)$ ; `"transpose"` échoue si `func(P.T)` n'a pas la forme de `T.T`, n'a pas ses $-\infty$ aux mêmes places, ou s'en écarte ailleurs de plus de `rtol` (`np.allclose` avec `rtol` et `atol` égaux à `rtol`) ; `"mean"` échoue si $\sum p(x, y)\,T(x, y)$, sur les cases non vides, s'écarte de `mymath.info.mutual_information(P, base=math.e)` de plus de $\texttt{rtol}\cdot\max(1, \lvert\text{moyenne}\rvert)$ (ou n'est pas finie). Une exception levée par `func` fait échouer les trois contrôles. Le notebook fournit aussi quatre versions fausses de `pmi` : `decimal` (le logarithme en base 10), `conditional` ($\ln P(Y = y \mid X = x)$, sans diviser par $p(y)$), `zeros_to_zero` (0 au lieu de $-\infty$ sur les cases vides) et `lift` (le lift, sans le logarithme, 0 sur les cases vides). a) Avec `rng = np.random.default_rng(7118)` et 300 essais, avec la bonne fonction et tes contrôles : vrai ou faux, les trois compteurs sont nuls ; b) avec le même départ et chacune des quatre versions fausses : les trois compteurs, dans l'ordre `"bound"`, `"transpose"`, `"mean"` (un nouveau `default_rng(7118)` chaque fois, dans l'ordre `decimal`, `conditional`, `zeros_to_zero`, `lift`) ; c) lesquelles passent le test, ou passent l'un des contrôles, et pourquoi c'est normal : qu'est-ce qui, dans le dépôt, vérifie ce qu'elles ont de faux ? La vérification lance aussi ton test sur deux départs cachés de 40 essais, avec la référence (compteurs nuls) et avec sept versions fausses cachées, qui faussent chacune une ou plusieurs des propriétés : l'une d'elles met $-\infty$ sur une case non vide, une autre lève une erreur sur une table d'une ligne, une troisième ne s'écarte de la PMI que de $2 \cdot 10^{-7}$ fois sa valeur (moins que la tolérance par défaut de `np.allclose`) ; elle remplace aussi un instant `mymath.cooccurrence.pmi` par l'une d'elles, pour l'appel sans `func`. Ce qu'il faut retenir : ce test ajoute à ceux de `tests/test_mb2_cooccurrence.py` des tables de formes et de cases vides tirées au hasard ; chacun de ses contrôles attrape certaines erreurs et en laisse passer d'autres ; un test se juge aux erreurs qu'il attrape, et à celles qu'il ne peut pas attraper.

**MB2.19 · 🏆 Défi : les cinq paires les plus associées d'une table cachée.** Une table jointe cachée de $10 \times 10$ décrit, pour les articles vendus par un hypermarché, le rayon de l'article (10 rayons, en lignes) et la tranche horaire de la vente (10 tranches, en colonnes) ; quelques rayons et quelques tranches sont rares, un rayon et une tranche sont très fréquents. Les « cinq paires les plus associées » sont les cinq cases de plus grande PMI de la table cachée, toutes de probabilité nettement non nulle. Le notebook fournit `COUNTS_19`, les comptes, de forme $(10, 10)$, de 3 000 ventes tirées selon une telle table. Écris `top_pairs_19(counts)`, qui reçoit une table de comptes de 3 000 observations et rend une liste de 5 paires `(ligne, colonne)`, numérotées à partir de 0. Tout NumPy et SciPy sont permis, et ta `pmi`. La cellule fournie donne aussi `pairs_found_19(pairs)`, qui compte combien des 5 paires données sont parmi les cinq paires cachées, sans rien montrer d'elles. **Critère de réussite :** au moins 4 des 5 paires trouvées pour la table du notebook, et pour chacune de trois tables cachées tirées à nouveau à chaque exécution, comme leurs 3 000 ventes, en moins de 10 secondes en tout. Les tables cachées viennent d'un processus à part, qui ne rend que le nombre de paires trouvées ; la vérification refuse une fonction qui lit la vérification au lieu de calculer (sa pile d'appels, ses noms, `pairs_found_19`). Relève : a) le nombre de paires que ta méthode trouve pour la table du notebook, par `pairs_found_19` (la vérification le recalcule avec ta fonction) ; b) le nombre de paires que trouve l'estimation directe (les cinq plus grandes valeurs de `pmi(COUNTS_19 / 3000)`) ; c) les comptes des cinq cases qu'elle choisit, par PMI estimée décroissante. Point de départ : regarde les cases que choisit l'estimation directe, et leurs comptes ; la fiche (§2 et §3) et M04 (les pseudo-comptes) donnent des idées, et la méthode est libre.
