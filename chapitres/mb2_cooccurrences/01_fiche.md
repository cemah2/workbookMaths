# MB2 · Cooccurrences, PMI et embeddings — fiche de cours

> Ce chapitre réunit les outils mathématiques des embeddings construits par comptage, hors de tout texte : l'écriture d'un entier en **base 2** et en **base 16** ; l'**information mutuelle ponctuelle** (PMI), qui dit si deux événements arrivent ensemble plus souvent que par hasard : elle est **bornée** par $-\ln$ de la plus grande des deux probabilités, si bien que seuls les événements rares peuvent avoir une grande PMI, et sa moyenne est l'information mutuelle de M06 ; le **lissage d'une marge**, une loi tempérée de M28 ; la **SVD tronquée** d'une table non centrée, répartie entre deux facteurs ; le logit d'un taux, et le décalage de $\ln K$ quand on **sous-échantillonne** une classe ; les **voisins** et les **analogies**, le **retrait d'une direction**, la **moyenne masquée** et le coût des **comparaisons par paires**. Le chapitre B2 de workbookIA les applique aux tokenizers, à la PPMI suivie d'une SVD, à word2vec et aux embeddings de phrases.

| | |
|---|---|
| **Sections** | §1 à §8 |
| **Temps total estimé** | ≈ 10,7 h : lecture et calculs de la fiche ≈ 2 h 15, exercices ≈ 7 h 55, 16 flashcards ≈ 30 min (parcours essentiel ≈ 8,6 h) |
| **Prérequis** | R0 (division euclidienne et reste, `//` et `%`) ; R1 (puissances de 2 et de 10, moyenne pondérée) ; R4 (notation $\Sigma$) ; R6 ($\ln$ et $\log_2$, bits et nats, sigmoïde et $\sigma(-x) = 1 - \sigma(x)$, cote et logit) ; R8 ($\binom{n}{2}$, simulation avec une graine) ; M02c (loi des grands nombres, erreur type d'une proportion) ; M03 (lois jointes et marginales, tableau de contingence, indépendance, loi conditionnelle) ; M04 (formule de Bayes) ; M06 (entropie, information mutuelle d'un tableau) ; M07 (produit scalaire, normes, cosinus, Cauchy-Schwarz, projection sur une droite) ; M09a (produit matriciel, transposée, ligne one-hot fois une matrice) ; M12a (rang) ; M12b (complément orthogonal, projection orthogonale) ; M12c (valeurs et vecteurs propres d'une matrice symétrique, trace) ; M12d (SVD compacte, Eckart-Young, axes principaux) ; M13a (vraisemblance de Bernoulli, régression logistique, le score est la log-cote) ; M20 (réductions le long d'un axe, centrage comme projection) ; M28 (matrice de Gram, loi tempérée `temper`) |
| **Fichiers du chapitre** | `02_exercices.md` (quiz, papier) · `03_notebook.ipynb` · `04_indices.md` · `05_solutions.md` et `05_solutions.ipynb` · `06_mes_reponses.md` · `flashcards.csv` |
| **mymath** | `cooccurrence.py` : `pmi`, `case_control_logit`, `remove_direction` |
| **Références** | pas de MML (le livre ne traite ni la PMI ni les embeddings, et tu as lu Eckart-Young en M12d, MML §4.6) ; K. W. Church et P. Hanks (la PMI d'une association) ; G. Bouma (la PMI normalisée) ; R. L. Prentice et R. Pyke, G. King et L. Zeng (le sous-échantillonnage d'une classe) ; O. Levy et Y. Goldberg (cités au §5) |

## Comment utiliser ce chapitre

**Ordre conseillé.**
1. `python tools/start_chapter.py MB2` (sur Colab : `00_setup/COLAB.md` §2) : il copie le notebook, ta feuille de réponses et le squelette `mymath/cooccurrence.py`.
2. Section par section : lis **crayon en main** et refais chaque calcul, puis fais les exercices de la section, quiz 🧠 d'abord. Ce chapitre n'a pas de lecture de MML ; les références de « Pour aller plus loin » sont facultatives.
3. Les exercices ✏️ et 🔗 se font sur papier, dans ta copie de `06_mes_reponses.md`, puis se vérifient dans la **partie 0** du notebook. Les démonstrations ∂ se rédigent dans ta copie et se jugent avec la grille de relecture de `05_solutions.md`.

Les sections se lisent presque indépendamment : le §3 reprend l'exemple du §2, le §6 les couleurs du §1, et les autres ne demandent que les chapitres cités en prérequis.

| Section | Quiz 🧠 et rappels 🔁 | Papier et réflexion | Notebook |
|---|---|---|---|
| §1 Bases 2 et 16 | Q1 | MB2.1 ✏️ | |
| §2 La PMI d'une table jointe | Q2, R1 | MB2.2 ✏️, MB2.8 ∂, MB2.12 🗣️ | MB2.13 🔨, MB2.15 🔮, MB2.17 🐛, MB2.18 🛠️, MB2.19 🏆 |
| §3 Lisser une marge | Q3 | MB2.3 ✏️, MB2.12 🗣️ | MB2.15 🔮, MB2.19 🏆 |
| §4 SVD tronquée, deux facteurs | Q4, R2 | MB2.4 ✏️, MB2.9 ∂, MB2.E1 💼 | MB2.16 🎨, MB2.17 🐛 |
| §5 Le logit d'un taux, $\ln K$ | Q5 | MB2.5 ✏️, MB2.10 ∂ | MB2.14 🔨 |
| §6 Voisins et analogies | Q6, R3 | MB2.6 ✏️ | |
| §7 Retirer une direction | Q6, R3 | MB2.7 ✏️ | MB2.14 🔨, MB2.17 🐛 |
| §8 Moyenne masquée, paires | Q6 | MB2.11 🔗 | |

Parcours essentiel : tout sauf MB2.9, MB2.E1, MB2.15, MB2.16, MB2.18 et MB2.19.

📐 **Notations.**
- **§1.** Un entier $N$ s'écrit en base $b$ avec $k$ chiffres $c_i$ de 0 à $b - 1$ ; le préfixe `0x` marque l'hexadécimal, comme en Python (`0x9D`), et `#RRGGBB` une couleur ; $w$ est un mot de bits et $\ell$ la largeur d'un champ. $\lfloor t \rfloor$ et $\lceil t \rceil$ sont les parties entières inférieure et supérieure.
- **§2 et §3.** Deux variables $X$ et $Y$, de valeurs $x$ et $y$ ; une **table jointe** $p(x, y)$ a les valeurs de $X$ en lignes, comme en M03 et M06 ; $p(x)$ et $p(y)$ sont ses marges (sommes des lignes et des colonnes). $N$ est le nombre d'observations, $n(x, y)$, $n(x)$ et $n(y)$ des comptes. Logarithmes népériens : la PMI est en **nats** ; les bits ne servent qu'au §1. $\alpha \in\ ]0, 1[$ est l'exposant de lissage, $p_\alpha$ la marge lissée, $T = 1/\alpha$ sa température.
- **§4.** $\mathbf{M}$ est une table $(m, n)$ ; sa SVD compacte est $\mathbf{U}\mathbf{S}\mathbf{V}^\top$, de valeurs singulières $s_1 \ge s_2 \ge \cdots$ (M12d) ; $\mathbf{U}_k$, $\mathbf{S}_k$, $\mathbf{V}_k$ en gardent les $k$ premières colonnes et valeurs singulières : $k$ est le **rang** gardé, comme en M12d. L'exposant de répartition est $\beta \in [0, 1]$ ; workbookIA B2 le note $p$, une lettre réservée ici aux probabilités, et note $d$ le rang.
- **§5.** Le label vaut 1 (positif) ou 0 (négatif) ; $a$ et $b$ sont des **nombres d'exemples** positifs et négatifs ; $s_1$ et $s_0$ sont les **taux de sélection** des deux classes, et $K = s_1/s_0$ ; $z$ est un score, $\sigma(z) = 1/(1 + e^{-z})$ la sigmoïde, $\theta_0$ et $\theta_1$ les paramètres d'un modèle logistique $z = \theta_0 + \theta_1x$.
- **§6 et §7.** Des vecteurs en gras : $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$, $\mathbf{d}$ ceux d'une analogie, $\mathbf{q} = \mathbf{b} - \mathbf{a} + \mathbf{c}$ la requête, $\hat{\mathbf{x}} = \mathbf{x}/\lVert\mathbf{x}\rVert$ le vecteur unitaire de $\mathbf{x}$, $\varphi$ un angle ; $\mathbf{u}$ la direction retirée, $\mathbf{D}$ la matrice dont les lignes $\mathbf{d}_i$ sont des différences, $\mathbf{g}$ un vecteur propre de sa matrice de Gram ; $L$ et $m$ la longueur et la masse d'un poisson.
- **§8.** $\mathbf{h}_1, \ldots, \mathbf{h}_L$ une suite de vecteurs complétée jusqu'à la longueur $L$, $m_t \in \{0, 1\}$ son masque, $\bar{\mathbf{h}}$ sa moyenne masquée, $n$ un nombre d'éléments, $\mathbf{R}$ la matrice $(n, d)$ de leurs résumés normalisés.
- **Lettres à double sens.** $k$ est un nombre de chiffres ou de bits au §1 et le rang gardé au §4 ; $b$ est une base au §1 et un nombre de négatifs au §5, alors que $a$ y est un nombre de positifs, et $\mathbf{a}$ et $\mathbf{b}$ (en gras) sont des vecteurs au §6 ; $c_i$ est un chiffre au §1, $\mathbf{c}$ un vecteur au §6 et $c$ un réel non nul au §7 ; $s_i$ est une valeur singulière au §4, mais $s_1$ et $s_0$ sont des taux de sélection au §5 ; $N$ est l'entier écrit en base $b$ et un nombre de valeurs au §1, un nombre d'observations au §2 ; $n$ compte des colonnes au §4 et des éléments au §8, et $n(y)$ des observations ; $m$ compte les lignes de $\mathbf{M}$ au §4, c'est une masse au §7, et $m_t$ est un masque au §8 ; $\mathbf{u}_i$ est un vecteur singulier au §4 et $\mathbf{u}$ la direction retirée au §7 ; $\mathbf{d}$ est le quatrième point d'une analogie au §6, $\mathbf{d}_i$ une différence au §7, et $d$ la longueur des résumés au §8 ; $x$ est une valeur de $X$ au §2, une feature au §5, et $\mathbf{x}$ un vecteur aux §6 et §7 ; $w$ est un mot de bits au §1, $\mathbf{w}$ une couleur au §6 et la direction du complément au §7 ; $\mathbf{e}$ est une couleur au §6, $\mathbf{e}_i$ un vecteur one-hot au §4 ; $L$ est la longueur d'un poisson au §7 et celle des suites complétées au §8 ; $r$ est un rang au §4, $\mathbf{r}$ un reste au §7 et $\mathbf{R}$ la matrice des résumés au §8. $K$ (§5) et $k$ (§1, §4) ne se confondent pas. Le contexte tranche.

Vocabulaire anglais de ce chapitre : *binary*, *hexadecimal*, *bit*, *byte*, *bit field*, *bit mask*, *shift*, *pointwise mutual information (PMI)*, *positive PMI (PPMI)*, *lift*, *association rule*, *normalized PMI*, *mutual information*, *smoothing*, *tempered distribution*, *truncated SVD*, *compact SVD*, *low-rank approximation*, *sparse matrix*, *dense matrix*, *centering*, *odds*, *log-odds*, *intercept*, *case-control study*, *subsampling*, *prior correction*, *cosine similarity*, *dot product*, *unit vector*, *nearest neighbor*, *analogy*, *parallelogram*, *query*, *orthogonal complement*, *allometry*, *condition factor*, *padding*, *mask*, *masked mean*, *pairwise comparisons*.

## Objectifs d'apprentissage

À la fin du chapitre, tu sais :
- **écrire** un entier en base 2 et en base 16, **lire** un octet et une couleur, **découper** un mot de bits en champs, et **compter** les bits qu'il faut pour $N$ valeurs ;
- **calculer** la PMI des cases d'une table jointe, la **lire** comme le logarithme d'un lift, en **tirer** la PPMI, et **retrouver** l'information mutuelle comme la moyenne des PMI ;
- **énoncer**, puis **démontrer** (∂ MB2.8), la borne $\operatorname{PMI}(x, y) \le \min(-\ln p(x), -\ln p(y))$, et **expliquer** pourquoi les événements rares ont les PMI extrêmes et les plus bruitées ;
- **lisser** une marge par une puissance, la **reconnaître** comme une loi tempérée, et **prévoir** le décalage de la PMI de chaque colonne ;
- **répartir** les valeurs singulières d'une SVD tronquée entre deux facteurs, et **dire** ce qui dépend de ce choix (les angles entre lignes) et ce qui n'en dépend pas (le produit), puis le **démontrer** (∂ MB2.9) ;
- **calculer** le logit de vraisemblance maximale d'un taux, et **corriger** par $\ln K$ un sous-échantillonnage d'une classe (∂ MB2.10, par la formule de Bayes) ;
- **mesurer** le parallélogramme d'une analogie et **expliquer**, par une borne sur le cosinus, pourquoi on exclut les points de la question ;
- **retirer** d'un nuage une direction estimée, et **dire** quelles distances changent et lesquelles restent ;
- **résumer** des suites de vecteurs de longueurs différentes par une moyenne masquée, et **comparer** le coût des comparaisons par paires à celui d'un vecteur par élément.

## L'essentiel en 8 lignes

1. **Bases** : $N = \sum_i c_i b^i$ ; les chiffres sont les restes des divisions successives par $b$, lus du dernier au premier ; $N \ge 1$ a $\lfloor\log_b N\rfloor + 1$ chiffres ; un chiffre hexadécimal vaut 4 bits, un octet deux chiffres ; $N$ valeurs demandent $\lceil\log_2 N\rceil$ bits ; un champ de $\ell$ bits à partir du bit $i$ vaut $\lfloor w/2^i\rfloor \bmod 2^\ell$.
2. **PMI** : $\operatorname{PMI}(x, y) = \ln\frac{p(x, y)}{p(x)p(y)} = \ln\frac{P(y \mid x)}{P(y)}$, le logarithme du lift de « $x \Rightarrow y$ » ; positive, nulle ou négative selon que $x$ et $y$ arrivent ensemble plus, autant ou moins souvent que par hasard ; $-\infty$ sur une case vide ; $\operatorname{PPMI} = \max(0, \operatorname{PMI})$ ; $I(X ; Y) = \sum_{p(x, y) > 0} p(x, y)\operatorname{PMI}(x, y) \ge 0$.
3. **Borne** (∂ MB2.8) : $\operatorname{PMI}(x, y) \le \min(-\ln p(x), -\ln p(y))$, atteinte quand le plus rare des deux n'arrive qu'avec l'autre ; seuls les événements rares ont de grandes PMI, et leurs PMI estimées sont les plus dispersées ; la PMI normalisée $\operatorname{PMI}/(-\ln p(x, y))$ est au plus 1.
4. **Lissage** : $p_\alpha(y) \propto n(y)^\alpha$ est la loi tempérée de température $1/\alpha$ (M28) ; la PMI de la colonne $y$ se décale de $-\ln\frac{p_\alpha(y)}{p(y)}$ : l'ordre des lignes dans une colonne ne change jamais, celui des colonnes dans une ligne peut changer.
5. **SVD** : $\mathbf{M}_k = \mathbf{U}_k\mathbf{S}_k\mathbf{V}_k^\top$ est la meilleure approximation de rang $k$ (Eckart-Young) ; $\mathbf{M}_k = (\mathbf{U}_k\mathbf{S}_k^\beta)(\mathbf{V}_k\mathbf{S}_k^{1-\beta})^\top$ pour tout $\beta$ ; le produit ne dépend pas de $\beta$, les cosinus entre lignes du premier facteur en général si (∂ MB2.9) ; on ne centre pas une grande table creuse.
6. **Paires et taux** : $\sigma(z)$ est la probabilité qu'une paire soit vraie ; le logit de vraisemblance maximale d'un taux de $a$ succès et $b$ échecs est $\ln(a/b)$ ; garder les positifs avec la probabilité $s_1$ et les négatifs avec $s_0$ multiplie la cote par $K = s_1/s_0$, et seule l'ordonnée à l'origine bouge, de $\ln K$ (∂ MB2.10).
7. **Voisins et analogies** : le produit scalaire favorise les vecteurs longs, le cosinus non ; $\lVert\hat{\mathbf{x}} - \hat{\mathbf{y}}\rVert^2 = 2 - 2\cos(\mathbf{x}, \mathbf{y})$ ; si $\lVert\mathbf{q} - \mathbf{x}\rVert \le \varepsilon\lVert\mathbf{x}\rVert$ avec $\varepsilon < 1$, $\cos(\mathbf{q}, \mathbf{x}) \ge \sqrt{1 - \varepsilon^2}$ : $\mathbf{c}$ reste près de $\mathbf{q} = \mathbf{b} - \mathbf{a} + \mathbf{c}$, d'où l'exclusion de $\mathbf{a}$, $\mathbf{b}$ et $\mathbf{c}$.
8. **Directions et ensembles** : $\mathbf{x} - \frac{\mathbf{x}\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u}$ retire $\mathbf{u}$, et seule la composante sur $\mathbf{u}$ des différences disparaît (Pythagore) ; la moyenne masquée $\sum m_t\mathbf{h}_t/\sum m_t$ ne voit pas le remplissage ; $n$ éléments font $\binom{n}{2}$ paires, contre $n$ résumés et un produit matriciel.

## §1 · Bases 2 et 16 : écrire un entier, lire un octet, découper un mot de bits

### Les chiffres d'un entier

En base 10, $3\,708 = 3 \times 10^3 + 7 \times 10^2 + 0 \times 10 + 8$ : chaque chiffre compte autant de fois la puissance de 10 de sa position. Rien n'oblige à prendre 10.

> **Définition.** Soit $b \ge 2$. Écrire un entier $N \ge 0$ en **base** $b$, c'est trouver ses **chiffres** $c_0, c_1, \ldots, c_{k-1}$, entiers de $0$ à $b - 1$, tels que
> $$N = c_{k-1}b^{k-1} + \cdots + c_1b + c_0 = \sum_{i=0}^{k-1}c_ib^i .$$
> En **base 2** (*binary*), les chiffres sont 0 et 1 : ce sont des **bits** (*binary digits*). En **base 16** (*hexadecimal*), les chiffres sont 0 à 9 puis A (10), B (11), C (12), D (13), E (14) et F (15).

L'écriture existe, et elle est unique si l'on interdit les zéros en tête ($c_{k-1} \ne 0$ quand $N \ge 1$) ; une écriture de longueur fixée, comme un octet ou un champ de bits, se complète à gauche par des zéros. Le dernier chiffre $c_0$ est le **reste** de la division de $N$ par $b$ (R0), et le **quotient** s'écrit avec les autres chiffres : $N = b \times (c_{k-1}b^{k-2} + \cdots + c_1) + c_0$. On recommence sur le quotient, jusqu'à un quotient nul : ce sont les **divisions successives**, et l'on lit les restes **du dernier au premier**.

**Exemple : 157 en base 2.**

| Division | Quotient | Reste |
|---|---|---|
| 157 = 2 × 78 + 1 | 78 | 1 |
| 78 = 2 × 39 + 0 | 39 | 0 |
| 39 = 2 × 19 + 1 | 19 | 1 |
| 19 = 2 × 9 + 1 | 9 | 1 |
| 9 = 2 × 4 + 1 | 4 | 1 |
| 4 = 2 × 2 + 0 | 2 | 0 |
| 2 = 2 × 1 + 0 | 1 | 0 |
| 1 = 2 × 0 + 1 | 0 | 1 |

En lisant les restes de bas en haut : $157 = 1001\,1101$ en base 2. Vérifie dans l'autre sens : $128 + 16 + 8 + 4 + 1 = 157$.

**Le nombre de chiffres.** Un entier $N \ge 1$ a $k$ chiffres en base $b$ quand $b^{k-1} \le N < b^k$, c'est-à-dire $k = \lfloor\log_b N\rfloor + 1$. Ici $2^7 = 128 \le 157 < 256 = 2^8$ : 8 bits.

### Base 16 : un chiffre pour quatre bits

Comme $16 = 2^4$, un chiffre hexadécimal correspond exactement à un groupe de **4 bits** : de $0000 = 0$ à $1111 = 15 = \mathrm{F}$. Pour passer de la base 2 à la base 16, on groupe les bits par quatre **en partant de la droite** : $1001\,1101$ donne $1001 = 9$ et $1101 = 13 = \mathrm{D}$, donc $157 = \texttt{0x9D}$. Vérifie : $9 \times 16 + 13 = 157$, ce que donnent aussi les divisions successives par 16. Dans l'autre sens, chaque chiffre se développe en 4 bits : $\texttt{0x78} = 0111\,1000 = 7 \times 16 + 8 = 120$.

Un **octet** (*byte*) compte 8 bits : deux chiffres hexadécimaux, de $\texttt{0x00} = 0$ à $\texttt{0xFF} = 255$, soit $2^8 = 256$ valeurs. Une **couleur** `#RRGGBB` aligne trois octets, le rouge, le vert et le bleu : `#781E28` est $(\texttt{0x78}, \texttt{0x1E}, \texttt{0x28}) = (120, 30, 40)$, un rouge sombre. Trois octets font $2^{24} = 16\,777\,216$ couleurs.

### Combien de bits pour N valeurs ?

$k$ bits forment $2^k$ mots différents. Pour donner un numéro à chacune de $N \ge 2$ valeurs, il faut $2^k \ge N$ ; le plus petit $k$ qui convient est
$$k = \lceil\log_2 N\rceil .$$
Pour 700 valeurs, $\log_2 700 \approx 9{,}45$ : $2^9 = 512$ ne suffit pas, il faut 10 bits. Pour $65\,536 = 2^{16}$ valeurs, exactement 16 bits. C'est la longueur d'un code de longueur fixe. L'entropie de M06 dit qu'aucun code ne descend en moyenne sous $\log_2 N$ bits quand les $N$ valeurs sont équiprobables ; le code de longueur fixe en est à moins d'un bit, et l'atteint quand $N$ est une puissance de 2.

### Découper un mot de bits en champs

Un écran à $65\,536$ couleurs range chaque couleur dans un mot de 16 bits, au format **RGB565** : 5 bits de rouge, 6 de vert (l'œil y est plus sensible) et 5 de bleu, dans cet ordre. Chaque morceau est un **champ** (*bit field*). Pour coder `#781E28`, on garde les bits de poids fort de chaque octet : $\lfloor 120/8\rfloor = 15$ sur 5 bits, $\lfloor 30/4\rfloor = 7$ sur 6 bits, $\lfloor 40/8\rfloor = 5$ sur 5 bits. Le mot vaut
$$w = 15 \times 2^{11} + 7 \times 2^5 + 5 = 30\,949 = \underbrace{01111}_{15}\,\underbrace{000111}_{7}\,\underbrace{00101}_{5} = \texttt{0x78E5} .$$
Pour le relire, on enlève les champs de droite par une division et l'on coupe ceux de gauche par un reste :

> **Propriété.** Le champ de $\ell$ bits qui commence au bit $i$ (le bit 0 est le plus à droite) d'un mot $w$ vaut
> $$\Big\lfloor\frac{w}{2^i}\Big\rfloor \bmod 2^\ell .$$

Ici $\lfloor 30\,949/2^{11}\rfloor = 15$, $\lfloor 30\,949/2^5\rfloor \bmod 64 = 967 \bmod 64 = 7$ et $30\,949 \bmod 32 = 5$. Revenue sur trois octets, la couleur devient $(15 \times 8, 7 \times 4, 5 \times 8) = (120, 28, 40)$ : le vert a perdu ses deux bits de poids faible.

💻 **Aujourd'hui en pratique** — `bin(157)` et `hex(157)` rendent `'0b10011101'` et `'0x9d'`, `int("78", 16)` rend 120, et `f"{157:08b}"` écrit les 8 bits. Les programmes découpent les champs par des **décalages** (*shift*) et des **masques** (*bit mask*) : `(w >> 5) & 0b111111` est $\lfloor w/2^5\rfloor \bmod 2^6$.

⚠️ **Erreur classique.** Lire les restes du premier au dernier : on obtient les bits à l'envers. Grouper les bits par quatre en partant de la gauche quand leur nombre n'est pas un multiple de 4. Confondre le nombre de bits **de l'entier** $N$, $\lfloor\log_2 N\rfloor + 1$, et le nombre de bits qu'il faut pour **numéroter $N$ valeurs**, $\lceil\log_2 N\rceil$ : pour 256 valeurs, 8 bits suffisent (de 0 à 255), alors que l'entier 256 en a 9.

🔗 **Dans workbookIA** — le chapitre B2 écrit des octets en hexadécimal et découpe des octets en champs de bits pour coder des caractères ; ce paragraphe en donne les outils, sur des couleurs.

## §2 · La PMI d'une table jointe : signe, −∞, PPMI, borne des événements rares, et l'information mutuelle comme moyenne

### Plus souvent que par hasard ?

Un capteur acoustique surveille une pompe. Pendant 98 heures, on note à chaque heure le **régime** de la pompe (lent, normal ou rapide) et le **signal** du capteur : un arrêt d'urgence, une alerte, ou rien à signaler (RAS). Les comptes $n(x, y)$, avec leurs marges :

| Régime \ signal | arrêt | alerte | RAS | $n(x)$ |
|---|---|---|---|---|
| lent | 0 | 2 | 47 | 49 |
| normal | 0 | 8 | 26 | 34 |
| rapide | 1 | 6 | 8 | 15 |
| $n(y)$ | 1 | 16 | 81 | $N = 98$ |

Divisée par $N$, c'est une **table jointe** (M03) : $p(x, y) = n(x, y)/N$. L'alerte arrive-t-elle plus souvent en régime rapide que si régime et signal étaient indépendants ? À l'indépendance, $p(x, y) = p(x)p(y)$ : il suffit de comparer les deux.

> **Définition.** L'**information mutuelle ponctuelle** (*pointwise mutual information*, PMI) de la case $(x, y)$ d'une table jointe est
> $$\operatorname{PMI}(x, y) = \ln\frac{p(x, y)}{p(x)\,p(y)} = \ln\frac{P(Y = y \mid X = x)}{P(Y = y)} = \ln\frac{P(X = x \mid Y = y)}{P(X = x)} .$$
> Elle est **positive** quand $x$ et $y$ arrivent ensemble plus souvent qu'à l'indépendance, **nulle** quand c'est aussi souvent, **négative** quand c'est moins souvent. Une case vide, $p(x, y) = 0$, a par convention une PMI de $-\infty$. La **PPMI** (*positive PMI*) est $\operatorname{PPMI}(x, y) = \max(0, \operatorname{PMI}(x, y))$ : elle vaut 0 sur les cases négatives et sur les cases vides.

Le rapport $\frac{P(y \mid x)}{P(y)}$ a un nom dans l'analyse des tickets de caisse. Une **règle d'association** (*association rule*) « $x \Rightarrow y$ » (« qui achète $x$ achète $y$ ») a pour **confiance** (*confidence*) $P(y \mid x)$ et pour **lift** $P(y \mid x)/P(y)$ : combien la règle fait mieux que de deviner $y$ au hasard. La PMI est le logarithme du lift.

**Exemple : la règle « rapide ⇒ alerte ».** En régime rapide, 6 heures sur 15 ont une alerte : $P(\text{alerte} \mid \text{rapide}) = 0{,}4$, contre $P(\text{alerte}) = 16/98 \approx 0{,}163$ en tout. Le lift vaut $0{,}4 \times 98/16 = 2{,}45$ et
$$\operatorname{PMI}(\text{rapide}, \text{alerte}) = \ln\frac{n(x, y)\,N}{n(x)\,n(y)} = \ln\frac{6 \times 98}{15 \times 16} = \ln 2{,}45 \approx 0{,}896 .$$
La forme avec les comptes, où le total $N$ apparaît une fois en haut, évite de calculer les trois probabilités. Les neuf cases :

| PMI | arrêt | alerte | RAS |
|---|---|---|---|
| lent | $-\infty$ | $\ln\frac14 \approx -1{,}386$ | $\approx 0{,}149$ |
| normal | $-\infty$ | $\approx 0{,}365$ | $\approx -0{,}078$ |
| rapide | $\ln\frac{98}{15} \approx 1{,}877$ | $\approx 0{,}896$ | $\approx -0{,}438$ |

En régime lent, une alerte arrive quatre fois moins souvent que par hasard ($2 \times 98/(49 \times 16) = \frac14$). Quatre cases ont une PMI positive ; la PPMI garde ces quatre valeurs et met 0 partout ailleurs. Si une colonne était **indépendante** des lignes, $P(y \mid x) = P(y)$ pour tout $x$, toute sa colonne de PMI serait nulle. `pmi(joint)` (🔨 MB2.13) calcule cette table à partir de la table jointe, avec $-\infty$ sur les cases vides ; elle ne prend pas le maximum avec 0.

### L'information mutuelle, moyenne des PMI

> **Rappel** (M06). L'information mutuelle est la **moyenne des PMI** sous la loi jointe :
> $$I(X ; Y) = \sum_{p(x, y) > 0}p(x, y)\,\ln\frac{p(x, y)}{p(x)\,p(y)} = \sum_{p(x, y) > 0}p(x, y)\operatorname{PMI}(x, y),$$
> la somme ne portant que sur les cases non vides. C'est la divergence KL entre la loi jointe et le produit de ses marges : elle est **positive**, nulle seulement à l'indépendance, bien que certaines PMI soient négatives.

Pour la pompe, les sept termes sont, en nats, $-0{,}028$ et $0{,}071$ (lent), $0{,}030$ et $-0{,}021$ (normal), $0{,}019$, $0{,}055$ et $-0{,}036$ (rapide) : $I(X ; Y) \approx 0{,}0906$ nat (0,090 avec les termes arrondis), soit $\approx 0{,}131$ bit. La case de l'arrêt a la plus grande PMI, mais elle ne pèse que $\frac{1}{98}$ dans la moyenne. `mutual_information(joint)` de M06 rend des **bits** par défaut ; en nats, c'est `mutual_information(joint, base=math.e)`.

![À gauche, la table des PMI de la pompe en carte de couleurs, avec la valeur de chaque case : en rouge les cases positives, dont 1,877 pour (rapide, arrêt) et 0,896 pour (rapide, alerte) ; en bleu les négatives, dont −1,386 pour (lent, alerte) ; en gris hachuré les deux cases vides, à −∞. À droite, chaque case non vide placée selon la plus grande de ses deux marges, en abscisse logarithmique, et sa PMI ; la courbe −ln p trace la borne : tous les points sont sous la courbe, sauf (rapide, arrêt), qui est sur la courbe, à 1,877 ; les trois cases de la colonne RAS restent sous 0,191, la borne d'une colonne fréquente](figures/pmi_borne.png)

### La borne des événements rares

> **Propriété** (∂ MB2.8). $\operatorname{PMI}(x, y) \le \min\big(-\ln p(x),\ -\ln p(y)\big)$. La borne est atteinte quand le plus rare des deux événements n'arrive qu'avec l'autre. La **PMI normalisée** (*normalized PMI*) $\operatorname{PMI}(x, y)/(-\ln p(x, y))$, définie pour $0 < p(x, y) < 1$, est au plus 1, et vaut 1 quand $x$ et $y$ arrivent toujours ensemble.

Le seul arrêt d'urgence a eu lieu en régime rapide : la borne $\min(-\ln\frac{15}{98}, -\ln\frac{1}{98}) = \min(1{,}877 ;\ 4{,}585) = 1{,}877$ est **atteinte**, et c'est la plus grande PMI de la table, appuyée sur une seule heure. Sa PMI normalisée vaut $1{,}877/\ln 98 \approx 0{,}409$, loin de 1 : l'arrêt n'arrive qu'en régime rapide, mais le régime rapide n'amène presque jamais l'arrêt.

La borne dit surtout qui **ne peut pas** avoir une grande PMI. La colonne RAS, de probabilité $\frac{81}{98}$, ne dépasse jamais $-\ln\frac{81}{98} \approx 0{,}191$, quelle que soit la ligne : un événement fréquent ne peut pas être beaucoup plus fréquent qu'à l'indépendance. Les très grandes PMI sont réservées aux événements **rares**.

### Une PMI estimée sur peu d'observations

La table n'est qu'un échantillon de 98 heures. Une probabilité estimée $\hat{p} = n/N$ a une erreur relative de l'ordre de $\sqrt{(1 - p)/(Np)}$ (l'erreur type de M02c divisée par $p$). Pour l'alerte, $Np = 16$ et l'erreur relative vaut $\approx 0{,}23$ ; pour l'arrêt, $Np \approx 1$ et elle vaut $\approx 0{,}99$, autant que la valeur elle-même. Pire : si la vraie probabilité d'un arrêt est $\frac{1}{98}$, 98 autres heures n'en montrent **aucun** avec la probabilité $(1 - \frac{1}{98})^{98} \approx 0{,}366$, et la PMI estimée de la case passe à $-\infty$. D'un échantillon à l'autre, la PMI d'une case rare saute entre $-\infty$ et des valeurs proches de sa borne : les cases rares ont à la fois les PMI les plus grandes et les plus mal estimées. Le 🔮 MB2.15 le mesure ; le §3 dit ce que le lissage change, et ce qu'il ne change pas.

⚠️ **Erreur classique.** Oublier le total $N$ : $\frac{n(x, y)}{n(x)\,n(y)}$ n'est pas le lift, il lui manque le facteur $N$ (🐛 MB2.17). Prendre $\log_2$ ou $\log_{10}$ au lieu de $\ln$ : la PMI change d'unité, pas de signe. Faire la moyenne des **PPMI** pour obtenir l'information mutuelle : c'est la moyenne des PMI, termes négatifs compris. Croire qu'une PMI de $-\infty$ signale une erreur de calcul : c'est une case qui n'est jamais arrivée.

🔗 **Dans workbookIA** — le chapitre B2 calcule la PMI et la PPMI de grandes tables de comptes qu'il construit lui-même ; ce paragraphe étudie la PMI d'une table jointe donnée, et dit d'avance pourquoi les colonnes rares y dominent.

## §3 · Lisser une marge : une loi tempérée, et ce qu'elle fait à la PMI de chaque colonne

### Remonter les colonnes rares

Pour retirer aux colonnes rares leur avantage, on **lisse** (*smoothing*) la marge des colonnes avant de calculer la PMI.

> **Définition.** Pour $0 < \alpha < 1$, la marge lissée est
> $$p_\alpha(y) = \frac{n(y)^\alpha}{\sum_{y'}n(y')^\alpha},$$
> et la PMI lissée est $\operatorname{PMI}_\alpha(x, y) = \ln\dfrac{p(x, y)}{p(x)\,p_\alpha(y)}$ : seule la marge des colonnes change.

Comme $n(y) = N\,p(y)$, $p_\alpha(y) \propto p(y)^\alpha = p(y)^{1/T}$ avec $T = 1/\alpha > 1$ : c'est la **loi tempérée** de M28 à la température $T$, `temper(p_y, 1 / alpha)`. Tu connais ses propriétés : l'ordre des colonnes ne change pas, les rapports $p_\alpha(y)/p_\alpha(y')$ sont ceux de $p$ élevés à la puissance $\alpha$, donc plus proches de 1 ; les colonnes rares **gagnent**, les fréquentes **perdent**, et une colonne vide reste vide.

**Exemple : $\alpha = \frac14$, donc $T = 4$.** Les comptes des colonnes, 1, 16 et 81, ont pour racines quatrièmes 1, 2 et 3, de somme 6 :
$$p = \Big(\frac{1}{98} ;\ \frac{16}{98} ;\ \frac{81}{98}\Big), \qquad p_{1/4} = \Big(\frac16 ;\ \frac13 ;\ \frac12\Big).$$
La probabilité de l'arrêt est multipliée par $\frac{98}{6} \approx 16{,}3$, celle de RAS par $\frac{49}{81} \approx 0{,}605$.

### Une constante par colonne

$$\operatorname{PMI}_\alpha(x, y) = \operatorname{PMI}(x, y) - \ln\frac{p_\alpha(y)}{p(y)} :$$
le **décalage** $-\ln\frac{p_\alpha(y)}{p(y)}$ ne dépend que de la colonne. Ici : $-\ln\frac{98}{6} \approx -2{,}793$ pour l'arrêt, $-\ln\frac{98}{48} \approx -0{,}714$ pour l'alerte, $+\ln\frac{81}{49} \approx +0{,}503$ pour RAS. La table devient

| $\operatorname{PMI}_{1/4}$ | arrêt | alerte | RAS |
|---|---|---|---|
| lent | $-\infty$ | $\approx -2{,}100$ | $\approx 0{,}651$ |
| normal | $-\infty$ | $\approx -0{,}348$ | $\approx 0{,}425$ |
| rapide | $\ln 0{,}4 \approx -0{,}916$ | $\ln 1{,}2 \approx 0{,}182$ | $\ln\frac{16}{15} \approx 0{,}065$ |

Deux conséquences, qui valent pour toute table.
- **Dans une colonne**, toutes les cases bougent de la même quantité : l'ordre des lignes ne change jamais. Le régime rapide reste celui de l'alerte.
- **Dans une ligne**, les cases bougent de quantités différentes : l'ordre des colonnes peut changer. En régime rapide, l'ordre arrêt (1,877), alerte (0,896), RAS (−0,438) devient alerte (0,182), RAS (0,065), arrêt (−0,916) : l'arrêt, premier sur une seule heure, passe dernier, et sa PPMI tombe à 0.

Une table **carrée et symétrique**, dont les lignes et les colonnes sont les mêmes événements, n'est plus symétrique une fois lissée sur ses seules colonnes : $\operatorname{PMI}_\alpha(x, y)$ et $\operatorname{PMI}_\alpha(y, x)$ ne reçoivent pas le même décalage dès que $p(x) \ne p(y)$.

Le lissage ne rend pas plus précise l'estimation de $p(x, y)$ : il retire aux colonnes rares l'avantage que leur donnait la borne du §2. Avec $\alpha \to 0$, la marge lissée tend vers la loi uniforme sur les colonnes non vides ; avec $\alpha = 1$, rien ne change.

![À gauche, la marge lissée p_α des trois colonnes (arrêt, alerte, RAS) en fonction de α, de 1 à 0 : 1/98, 16/98 et 81/98 en α = 1, (1/6, 1/3, 1/2) en α = 1/4, marqué en pointillés, et 1/3 chacune en α = 0. À droite, les trois PMI lissées de la ligne « rapide » en fonction de α : l'arrêt part de 1,877 et descend, il croise l'alerte puis RAS, et vaut −0,916 en α = 1/4, où l'alerte (0,182) est en tête, devant RAS (0,065) ; plus à droite, RAS passe à son tour devant l'alerte](figures/lissage.png)

⚠️ **Erreur classique.** Multiplier les comptes par $\alpha$ au lieu de les élever à la puissance $\alpha$ : après normalisation, rien n'a changé. Oublier de renormaliser $n(y)^\alpha$. Lisser la table jointe $p(x, y)$ au lieu de la marge : la PMI n'aurait plus son sens.

🔗 **Dans workbookIA** — le chapitre B2 lisse la marge des colonnes avant la PMI ; ce paragraphe montre que c'est une loi tempérée et dit ce que le lissage fait à chaque colonne.

## §4 · La SVD tronquée d'une table non centrée : répartir les valeurs singulières entre deux facteurs

### Rappel : SVD compacte et Eckart-Young

Une table $\mathbf{M}$ de forme $(m, n)$ et de rang $r$ s'écrit $\mathbf{M} = \mathbf{U}\mathbf{S}\mathbf{V}^\top = \sum_{i=1}^r s_i\,\mathbf{u}_i\mathbf{v}_i^\top$ (SVD compacte, M12d). En ne gardant que les $k$ premiers termes,
$$\mathbf{M}_k = \sum_{i=1}^{k}s_i\,\mathbf{u}_i\mathbf{v}_i^\top = \mathbf{U}_k\mathbf{S}_k\mathbf{V}_k^\top$$
est la **SVD tronquée** (*truncated SVD*), la meilleure approximation de rang $k$ au sens de la norme de Frobenius, d'erreur au carré $\sum_{i > k}s_i^2$ (Eckart-Young, M12d §3). Ce sont `svd` et `low_rank_approximation` de M12d, avec leur convention de signe : la coordonnée de plus grande valeur absolue de chaque $\mathbf{v}_i$ est positive.

**Exemple : trois mangeoires.** Un matin, on compte les visites de trois espèces (verdier, mésange, sittelle) à trois mangeoires A, B et C, de la plus proche des maisons à la plus proche du bois :
$$\mathbf{M} = \begin{pmatrix} 8 & 9 & 10 \\ 4 & 8 & 12 \\ 0 & 7 & 14 \end{pmatrix}.$$
La ligne B est la moyenne des lignes A et C : $\mathbf{M}$ est de rang 2. Sa SVD compacte a pour valeurs singulières $s_1 = 4\sqrt{42} \approx 25{,}92$ et $s_2 = \sqrt{42} \approx 6{,}48$, avec
$$\mathbf{u}_1 = \tfrac{1}{\sqrt3}(1, 1, 1), \quad \mathbf{u}_2 = \tfrac{1}{\sqrt2}(1, 0, -1), \qquad \mathbf{v}_1 = \tfrac{1}{\sqrt{14}}(1, 2, 3), \quad \mathbf{v}_2 = \tfrac{1}{\sqrt{21}}(4, 1, -2).$$
Vérifie une case : $M_{A,\text{verdier}} = 4\sqrt{42}\cdot\frac{1}{\sqrt3}\cdot\frac{1}{\sqrt{14}} + \sqrt{42}\cdot\frac{1}{\sqrt2}\cdot\frac{4}{\sqrt{21}} = 4 + 4 = 8$. La première couche, $s_1\mathbf{u}_1\mathbf{v}_1^\top = 4\,(1, 1, 1)^\top(1, 2, 3)$, répète la ligne $(4, 8, 12)$, la moyenne des trois lignes ; son erreur au carré vaut $s_2^2 = 42$.

### Deux facteurs, un exposant

On veut un vecteur par **ligne** de la table (une mangeoire) et un vecteur par **colonne** (une espèce), dont les produits scalaires redonnent $\mathbf{M}_k$. Toute répartition des valeurs singulières convient :

> **Propriété** (∂ MB2.9). Pour tout $\beta \in [0, 1]$, avec $\mathbf{S}_k^\beta = \operatorname{diag}(s_1^\beta, \ldots, s_k^\beta)$,
> $$\mathbf{M}_k = (\mathbf{U}_k\mathbf{S}_k^\beta)(\mathbf{V}_k\mathbf{S}_k^{1-\beta})^\top .$$
> Le produit ne dépend pas de $\beta$. Les produits scalaires et les cosinus entre lignes du premier facteur, eux, en dépendent en général : pour $\beta = 1$, ce sont ceux des lignes de $\mathbf{M}_k$ ; pour $\beta = 0$, ceux des lignes de $\mathbf{U}_k$.

Le vecteur de la ligne $i$ est la ligne $i$ du premier facteur, $\mathbf{e}_i^\top(\mathbf{U}_k\mathbf{S}_k^\beta)$, où $\mathbf{e}_i$ est le vecteur one-hot de la ligne $i$ (M09a). Dans ces vecteurs, $\beta = 1$ donne aux couches tout leur poids $s_i$, $\beta = 0$ le même poids à chacune, et $\beta = \frac12$ partage. Ce que deux factorisations de rang $k$ quelconques ont en commun est l'affaire de MB4.

**Exemple : les mangeoires pour $\beta = 0$, $\frac12$ et 1.** Les lignes de $\mathbf{U}_2$ sont $(\frac{1}{\sqrt3}, \frac{1}{\sqrt2})$, $(\frac{1}{\sqrt3}, 0)$ et $(\frac{1}{\sqrt3}, -\frac{1}{\sqrt2})$. On multiplie la première colonne par $s_1^\beta$ et la seconde par $s_2^\beta$. Comme $s_1/s_2 = 4$, les lignes de $\mathbf{U}_2\mathbf{S}_2^\beta$ sont, à un facteur positif commun près qui ne change aucun cosinus,
$$A : (\sqrt2 \cdot 4^\beta,\ \sqrt3), \qquad B : (\sqrt2 \cdot 4^\beta,\ 0), \qquad C : (\sqrt2 \cdot 4^\beta,\ -\sqrt3),$$
d'où $\cos(A, C) = \dfrac{2 \cdot 16^\beta - 3}{2 \cdot 16^\beta + 3}$ :

| $\beta$ | 0 | ½ | 1 |
|---|---|---|---|
| $\cos(A, C)$ | $-\frac15 = -0{,}2$ | $\frac{5}{11} \approx 0{,}455$ | $\frac{29}{35} \approx 0{,}829$ |
| $\cos(A, B)$ | $\sqrt{2/5} \approx 0{,}632$ | $\sqrt{8/11} \approx 0{,}853$ | $\sqrt{32/35} \approx 0{,}956$ |

Pour $\beta = 1$, on retrouve le cosinus des lignes de $\mathbf{M}$ : $\frac{(8, 9, 10)\cdot(0, 7, 14)}{\sqrt{245}\sqrt{245}} = \frac{203}{245} = \frac{29}{35}$. Avec $\beta = 1$, la grande première couche, le niveau commun, domine : les trois mangeoires se ressemblent. Avec $\beta = 0$, l'opposition verdier-sittelle de la seconde couche pèse autant, et A et C font un angle obtus. Le produit, lui, redonne toujours $\mathbf{M}$.

![Trois panneaux, un par valeur de β (0, 1/2 et 1), avec les lignes de U₂S₂^β des mangeoires A, B et C en flèches depuis l'origine. À β = 0, les flèches font des angles nets : cos(A, C) = −0,2. À β = 1/2, la première coordonnée a été étirée : cos(A, C) ≈ 0,455. À β = 1, les flèches se resserrent autour de l'axe horizontal : cos(A, C) ≈ 0,829, le cosinus des lignes de M. B est toujours sur l'axe horizontal, au milieu](figures/facteurs_beta.png)

### Ne pas centrer une grande table creuse

L'ACP (M12d) centre les colonnes avant la SVD. Avec une grande table de comptes, on ne le fait pas, pour deux raisons.

- **Une table creuse** (*sparse matrix*) **le resterait.** Une table de 5 000 magasins × 40 000 produits a $2 \times 10^8$ cases. Si 0,1 % seulement sont non nulles, on ne stocke que ces $2 \times 10^5$ cases, avec leur position : environ 2,4 Mo (8 octets par valeur, 4 par numéro de colonne). Centrer retire à chaque case la moyenne de sa colonne : les zéros deviennent des nombres négatifs, la table devient **pleine** (*dense matrix*), et coûte 1,6 Go en `float64`, environ 670 fois plus.
- **On veut approcher la table elle-même**, pas ses écarts à la moyenne. Dans une table de comptes positive, la première couche de la SVD non centrée porte souvent le niveau moyen, comme dans l'exemple, où elle est exactement la ligne moyenne $(4, 8, 12)$ : retirer cette couche, c'était ici centrer.

💻 **Aujourd'hui en pratique** — `scipy.sparse` stocke une table creuse par ses cases non nulles, et `scipy.sparse.linalg.svds(M, k)` calcule les $k$ plus grandes valeurs singulières par une méthode itérative qui ne touche la table que par des produits $\mathbf{M}\mathbf{v}$ et $\mathbf{M}^\top\mathbf{u}$, dont le coût suit le nombre de cases non nulles. `np.linalg.svd` ne sert qu'aux petites tables pleines.

⚠️ **Erreur classique.** Écrire les deux facteurs $\mathbf{U}_k\mathbf{S}_k^\beta$ et $\mathbf{V}_k\mathbf{S}_k^\beta$ : leur produit vaut $\mathbf{U}_k\mathbf{S}_k^{2\beta}\mathbf{V}_k^\top$, qui n'est $\mathbf{M}_k$ que pour $\beta = \frac12$ (🐛 MB2.17). Comparer des vecteurs de lignes obtenus avec deux $\beta$ différents. Centrer une grande table creuse « pour faire une ACP ».

🔗 **Dans workbookIA** — le chapitre B2 factorise une grande table de PPMI par une SVD tronquée pour donner un vecteur à chaque ligne, avec un exposant qu'il note $p$ ; ce paragraphe montre, sur une petite table, ce que change cet exposant.

## §5 · Le modèle logistique d'une paire : le logit d'un taux, et le décalage de ln K quand on sous-échantillonne une classe

### Vraies paires et paires tirées au hasard

Une autre façon d'obtenir des vecteurs est d'**apprendre** à reconnaître les paires. Chaque exemple est une paire $(x, y)$ de deux objets, un milieu et une espèce, un magasin et un produit. Certaines paires ont été **observées** ensemble : ce sont les vraies paires, de label 1. D'autres ont été **tirées au hasard**, en prenant $x$ et $y$ sans lien : label 0. Un modèle donne à chaque paire un score $z(x, y)$, et

$$\sigma\big(z(x, y)\big) = P(\text{vraie paire} \mid x, y).$$

C'est une **régression logistique** (M13a) dont les exemples sont des paires : le score est la **log-cote** de « vraie », $z = \ln\frac{P(1 \mid x, y)}{P(0 \mid x, y)}$, et $1 - \sigma(z) = \sigma(-z)$ (R6) est la probabilité de « tirée au hasard ». La suite de la section étudie la log-cote d'une classe dans un cadre plus simple, où les exemples sont des photos.

### Le logit d'un taux

Un piège photographique se déclenche au moindre mouvement. Sur une saison, de jour, 1 250 photos : 25 montrent un animal (label 1), 1 225 sont vides (label 0).

> **Rappel** (M13a). Pour $a$ succès et $b$ échecs indépendants de même probabilité $p$, la vraisemblance $p^a(1 - p)^b$ est maximale en $\hat{p} = \frac{a}{a + b}$. Son logit, le **logit de vraisemblance maximale**, est
> $$\ln\frac{\hat{p}}{1 - \hat{p}} = \ln\frac{a}{b} .$$

De jour, $\hat{p} = \frac{25}{1\,250} = 0{,}02$ et le logit vaut $\ln\frac{25}{1\,225} = -\ln 49 \approx -3{,}892$. De nuit, 100 animaux et 1 225 photos vides : $\ln\frac{100}{1\,225} = \ln\frac{4}{49} \approx -2{,}506$. Un modèle logistique $z = \theta_0 + \theta_1x$, avec $x = 1$ la nuit et $x = 0$ le jour, a un paramètre par groupe : son maximum de vraisemblance redonne les deux logits, $\hat{\theta}_0 = -\ln 49$ et $\hat{\theta}_1 = \ln\frac{4}{49} + \ln 49 = \ln 4 \approx 1{,}386$. La nuit multiplie la cote par 4.

### Sous-échantillonner une classe : l'étude cas-témoins

Trier les photos coûte cher. On garde **toutes** les photos avec un animal et l'on **sous-échantillonne** (*subsampling*) les autres : **une photo vide sur 25**, tirée au hasard, sans regarder si elle est de jour ou de nuit. En médecine, on appelle cela une **étude cas-témoins** (*case-control study*) : on garde les **cas** (label 1) avec la probabilité $s_1$ et les **témoins** (label 0) avec la probabilité $s_0$, sans regarder les features. Ici $s_1 = 1$ et $s_0 = \frac{1}{25}$.

En moyenne, l'échantillon garde, de jour, 25 animaux et $\frac{1\,225}{25} = 49$ photos vides ; de nuit, 100 et 49. Les logits observés deviennent $\ln\frac{25}{49} \approx -0{,}673$ et $\ln\frac{100}{49} \approx 0{,}713$ : tous deux ont augmenté de $\ln 25 \approx 3{,}219$, et leur écart vaut toujours $\ln 4$. Ajusté sur l'échantillon, le modèle trouve $\hat{\theta}_0 = \ln\frac{25}{49}$ et le même $\hat{\theta}_1 = \ln 4$. Lu tel quel, il annonce de jour une probabilité $\sigma(\ln\frac{25}{49}) = \frac{25}{74} \approx 0{,}338$ au lieu de 0,02.

> **Propriété** (∂ MB2.10, par la formule de Bayes). Si l'on garde chaque positif avec la probabilité $s_1$ et chaque négatif avec la probabilité $s_0$, indépendamment des features, la cote d'un positif dans l'échantillon est celle de la population multipliée par $K = s_1/s_0$. Dans un modèle logistique, seule l'**ordonnée à l'origine** (*intercept*) bouge, de $\ln K$ ; les autres coefficients ne changent pas. Garder un négatif sur $K$ et tous les positifs décale donc l'ordonnée à l'origine de $+\ln K$, et l'on corrige en retirant $\ln K$.

La condition compte : si la sélection dépendait aussi de $x$ (garder plus de photos vides de nuit), la pente bougerait aussi. Un échantillon tiré au hasard, $s_1 = s_0$, ne change rien. `case_control_logit(a, b, s1, s0)` (🔨 MB2.14) rend le logit de la population estimé sur l'échantillon, $\ln\frac{a}{b} - \ln\frac{s_1}{s_0}$ : pour le jour, $\ln\frac{25}{49} - \ln 25 = -\ln 49$.

💻 **Aujourd'hui en pratique** — en épidémiologie, on ajuste la régression logistique sur l'échantillon cas-témoins : les pentes, des logarithmes de rapports de cotes, s'interprètent sans correction (Prentice et Pyke, 1979), et l'on corrige l'ordonnée à l'origine quand on veut des probabilités, ce que King et Zeng (2001) appellent la *prior correction*.

⚠️ **Erreur classique.** Lire les probabilités d'un modèle entraîné sur un échantillon sous-échantillonné sans corriger : elles sont trop grandes pour la classe gardée en entier. Corriger aussi les pentes : seule l'ordonnée à l'origine a bougé. Se tromper de sens : quand les positifs sont surreprésentés ($K > 1$), on **retire** $\ln K$.

🔗 **Dans workbookIA** — le chapitre B2 entraîne word2vec, une régression logistique qui sépare de vraies paires de paires tirées au hasard ; O. Levy et Y. Goldberg (2014) ont montré qu'à l'optimum, le score d'une paire vaut sa PMI moins le logarithme du nombre de paires tirées au hasard pour une vraie paire, et workbookIA B2 le démontre.

## §6 · Voisins et analogies : cosinus, produit scalaire et parallélogramme

### Cosinus, normalisation, produit scalaire

Les couleurs du §1 sont des vecteurs de $\mathbb{R}^3$. Le cosinus de deux couleurs, $\cos(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x}\cdot\mathbf{y}}{\lVert\mathbf{x}\rVert\lVert\mathbf{y}\rVert}$ (M07), ne regarde que leur **teinte** : une couleur et la même deux fois plus sombre ont un cosinus de 1. Le produit scalaire, lui, vaut $\lVert\mathbf{x}\rVert\lVert\mathbf{y}\rVert\cos(\mathbf{x}, \mathbf{y})$ : à cosinus égal, il préfère les vecteurs **longs**.

**Exemple.** On cherche la couleur la plus proche de $\mathbf{q} = (120, 20, 64)$, de norme $\sqrt{18\,896} \approx 137{,}5$, entre $\mathbf{e} = \frac12\mathbf{q} = (60, 10, 32)$, la même teinte plus sombre, et un lilas très pâle, `#DCC8E6`, $\mathbf{w} = (220, 200, 230)$. Le produit scalaire choisit le lilas : $\mathbf{q}\cdot\mathbf{w} = 45\,120$ contre $\mathbf{q}\cdot\mathbf{e} = 9\,448$. Le cosinus choisit $\mathbf{e}$ : 1, contre $\cos(\mathbf{q}, \mathbf{w}) = \frac{45\,120}{\sqrt{18\,896}\,\sqrt{141\,300}} \approx 0{,}873$.

Pour des **vecteurs unitaires** $\hat{\mathbf{x}} = \mathbf{x}/\lVert\mathbf{x}\rVert$, en développant le carré (M07),
$$\lVert\hat{\mathbf{x}} - \hat{\mathbf{y}}\rVert^2 = 1 + 1 - 2\,\hat{\mathbf{x}}\cdot\hat{\mathbf{y}} = 2 - 2\cos(\mathbf{x}, \mathbf{y}).$$
Classer des voisins par cosinus décroissant, ou leurs vecteurs unitaires par distance croissante, donne le **même classement**, donc le même **plus proche voisin** (*nearest neighbor*). Pour $\mathbf{q}$ et $\mathbf{w}$ : $\lVert\hat{\mathbf{q}} - \hat{\mathbf{w}}\rVert^2 = 2 - 2 \times 0{,}873 \approx 0{,}254$.

### Le parallélogramme d'une analogie

Dans une **analogie** (*analogy*), « $\mathbf{a}$ est à $\mathbf{b}$ ce que $\mathbf{c}$ est à $\mathbf{d}$ » : si la relation est un même **décalage**, $\mathbf{b} - \mathbf{a} = \mathbf{d} - \mathbf{c}$, les quatre points forment un **parallélogramme** (*parallelogram*), et $\mathbf{d} = \mathbf{b} - \mathbf{a} + \mathbf{c}$. Pour chercher le quatrième point, on forme la **requête** (*query*)
$$\mathbf{q} = \mathbf{b} - \mathbf{a} + \mathbf{c}$$
et l'on cherche le point le plus proche de $\mathbf{q}$ au sens du cosinus. Le **défaut** du parallélogramme, $\delta = \lVert(\mathbf{b} - \mathbf{a}) - (\mathbf{d} - \mathbf{c})\rVert = \lVert\mathbf{q} - \mathbf{d}\rVert$, est nul quand il est exact.

**Exemple : quatre couleurs.** `#C89628` est un jaune moutarde, $\mathbf{a} = (200, 150, 40)$, et `#C88C40` le même avec un peu moins de vert et plus de bleu, $\mathbf{b} = (200, 140, 64)$ : $\mathbf{b} - \mathbf{a} = (0, -10, 24)$. Quelle couleur est au rouge sombre `#781E28`, $\mathbf{c} = (120, 30, 40)$, ce que $\mathbf{b}$ est à $\mathbf{a}$ ? La requête vaut $\mathbf{q} = (120, 20, 64)$, `#781440`. Une couleur du nuancier, `#7A183C`, soit $\mathbf{d} = (122, 24, 60)$, a pour décalage $\mathbf{d} - \mathbf{c} = (2, -6, 20)$ et pour défaut $\delta = \lVert(-2, -4, 4)\rVert = 6$ ; $\cos(\mathbf{q}, \mathbf{d}) \approx 0{,}9991$.

### Pourquoi on exclut a, b et c

Mais $\mathbf{c}$ lui-même est très proche de $\mathbf{q}$ : $\cos(\mathbf{q}, \mathbf{c}) = \frac{17\,560}{\sqrt{18\,896} \times 130} \approx 0{,}983$. Ce n'est pas un hasard.

> **Lemme.** Soit $\mathbf{x} \ne \mathbf{0}$ et $\mathbf{q}$ tel que $\lVert\mathbf{q} - \mathbf{x}\rVert \le \varepsilon\lVert\mathbf{x}\rVert$, avec $0 \le \varepsilon < 1$. Alors
> $$\cos(\mathbf{q}, \mathbf{x}) \ge \sqrt{1 - \varepsilon^2}.$$
> Pour une analogie, avec $\mathbf{x} = \mathbf{c}$ et $\mathbf{q} - \mathbf{c} = \mathbf{b} - \mathbf{a}$ : si $\lVert\mathbf{b} - \mathbf{a}\rVert \le \varepsilon\lVert\mathbf{c}\rVert$, alors $\cos(\mathbf{q}, \mathbf{c}) \ge \sqrt{1 - \varepsilon^2}$.

*Démonstration.* D'abord $\mathbf{q} \ne \mathbf{0}$, puisque $\lVert\mathbf{q}\rVert \ge \lVert\mathbf{x}\rVert - \lVert\mathbf{q} - \mathbf{x}\rVert \ge (1 - \varepsilon)\lVert\mathbf{x}\rVert > 0$. Soit $\varphi \in [0, \pi]$ l'angle de $\mathbf{q}$ et $\mathbf{x}$. La distance de $\mathbf{x}$ à la droite $\mathbb{R}\mathbf{q}$ vaut $\lVert\mathbf{x}\rVert\sin\varphi$ : c'est la norme de l'écart entre $\mathbf{x}$ et sa projection sur la droite (M07). Comme $\mathbf{q}$ est un point de cette droite, cette distance est au plus $\lVert\mathbf{x} - \mathbf{q}\rVert \le \varepsilon\lVert\mathbf{x}\rVert$ : donc $\sin\varphi \le \varepsilon$. D'autre part, par Cauchy-Schwarz, $\mathbf{q}\cdot\mathbf{x} = \lVert\mathbf{x}\rVert^2 + (\mathbf{q} - \mathbf{x})\cdot\mathbf{x} \ge \lVert\mathbf{x}\rVert^2 - \varepsilon\lVert\mathbf{x}\rVert^2 > 0$ : l'angle est aigu, et $\cos\varphi = \sqrt{1 - \sin^2\varphi} \ge \sqrt{1 - \varepsilon^2}$. $\square$

Géométriquement, $\mathbf{q}$ est dans la boule de rayon $\varepsilon\lVert\mathbf{x}\rVert$ autour de $\mathbf{x}$, et cette boule est vue depuis l'origine sous un demi-angle $\arcsin\varepsilon$, l'angle de $[0, \frac{\pi}{2}]$ dont le sinus vaut $\varepsilon$. L'égalité a lieu quand $\mathbf{q}$ est sur le bord de la boule, à l'endroit où une demi-droite issue de l'origine la touche.

Pour les couleurs, $\lVert\mathbf{b} - \mathbf{a}\rVert = 26$ et $\lVert\mathbf{c}\rVert = 130$ : $\varepsilon = 0{,}2$, et le lemme garantit $\cos(\mathbf{q}, \mathbf{c}) \ge \sqrt{0{,}96} \approx 0{,}980$, sans rien calculer d'autre. Ici $\mathbf{d}$ passe devant $\mathbf{c}$, parce que son défaut est petit. Mais quand la relation $\mathbf{b} - \mathbf{a}$ est courte devant les vecteurs, ce qui est la règle, $\mathbf{c}$, et souvent $\mathbf{a}$ et $\mathbf{b}$, occupent le haut de la liste des voisins de $\mathbf{q}$, et la réponse $\mathbf{c}$ ne dit rien. D'où la règle : on **exclut** $\mathbf{a}$, $\mathbf{b}$ et $\mathbf{c}$ des candidats. Le lemme vaut pour n'importe quel candidat $\mathbf{x}$ assez proche de $\mathbf{q}$, $\mathbf{d}$ compris.

![À gauche, un parallélogramme dans le plan : les points a, b, c, la requête q = b − a + c et un point d proche de q, avec les décalages b − a et q − c égaux. À droite, le lemme : un vecteur x depuis l'origine, le disque de rayon ε‖x‖ autour de x (ε = 0,4 sur le dessin), les deux demi-droites tangentes issues de l'origine, à l'angle arcsin ε ≈ 23,6° de x, et plusieurs points q du disque : tous font avec x un angle d'au plus arcsin ε, donc un cosinus d'au moins √(1 − ε²) ≈ 0,917](figures/analogie.png)

⚠️ **Erreur classique.** Classer les voisins par produit scalaire en croyant classer par similarité : les vecteurs longs l'emportent. Oublier d'exclure $\mathbf{a}$, $\mathbf{b}$ et $\mathbf{c}$, et conclure que l'analogie a échoué. Prendre un cosinus élevé avec $\mathbf{q}$ pour une preuve que l'analogie est juste : le lemme montre qu'il est presque garanti.

🔗 **Dans workbookIA** — le chapitre B2 cherche les voisins d'un vecteur par le cosinus et résout des analogies par la requête $\mathbf{b} - \mathbf{a} + \mathbf{c}$ ; ce paragraphe en donne la géométrie, et la raison de l'exclusion.

## §7 · Retirer une direction : la projection sur le complément, et ce qui reste

### Projeter sur le complément d'une droite

Retirer d'un vecteur $\mathbf{x}$ sa composante le long d'une direction $\mathbf{u} \ne \mathbf{0}$, c'est lui retirer sa projection sur la droite $\mathbb{R}\mathbf{u}$ (M07) :
$$\mathbf{r} = \mathbf{x} - \frac{\mathbf{x}\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\,\mathbf{u}.$$
C'est la **projection orthogonale sur le complément** de la droite (*orthogonal complement*, M12b). Tu connais ses propriétés : $\mathbf{r}$ est orthogonal à $\mathbf{u}$ ; retirer deux fois la même direction ne change rien ; un vecteur parallèle à $\mathbf{u}$ devient nul ; $c\,\mathbf{u}$ donne le même résultat pour tout $c \ne 0$. Et la distance se partage selon Pythagore :

> **Propriété.** Si $\mathbf{r}_\mathbf{x}$ et $\mathbf{r}_\mathbf{y}$ sont les restes de $\mathbf{x}$ et $\mathbf{y}$,
> $$\lVert\mathbf{x} - \mathbf{y}\rVert^2 = \lVert\mathbf{r}_\mathbf{x} - \mathbf{r}_\mathbf{y}\rVert^2 + \frac{\big((\mathbf{x} - \mathbf{y})\cdot\mathbf{u}\big)^2}{\mathbf{u}\cdot\mathbf{u}} :$$
> seule la composante de la différence le long de $\mathbf{u}$ disparaît.

En effet $\mathbf{r}_\mathbf{x} - \mathbf{r}_\mathbf{y}$ est le reste de $\mathbf{x} - \mathbf{y}$, orthogonal à sa projection. Retirer $\mathbf{u} = (1, \ldots, 1)$ revient à **centrer** chaque vecteur : $\mathbf{x} - \bar{x}\,(1, \ldots, 1)$, où $\bar{x}$ est la moyenne de ses coordonnées (M20). `remove_direction(X, u)` (🔨 MB2.14) retire une direction donnée de chaque ligne d'une matrice.

### Estimer la direction : le premier axe de différences

Souvent, la direction n'est pas donnée : on l'estime. Chez les poissons d'un même étang, la masse croît à peu près comme le cube de la longueur : en logarithmes, $\ln m \approx 3\ln L + \text{constante}$. C'est une **allométrie** (*allometry*). Mesurons trois paires de truites, chaque fois une petite et une grande, en $(\ln L, \ln m)$, avec $L$ en cm et $m$ en g. Les trois différences « grande − petite » forment les lignes de
$$\mathbf{D} = \begin{pmatrix} 0{,}08 & 0{,}14 \\ 0{,}10 & 0{,}30 \\ 0{,}02 & 0{,}16 \end{pmatrix}.$$
Le **premier axe** des différences est la direction unitaire $\mathbf{u}$ qui rend $\sum_i(\mathbf{d}_i\cdot\mathbf{u})^2 = \mathbf{u}^\top\mathbf{D}^\top\mathbf{D}\,\mathbf{u}$ maximal : un vecteur propre unitaire de la plus grande valeur propre de $\mathbf{D}^\top\mathbf{D}$, comme l'axe principal de M12d, mais sans centrage, car une différence nulle a un sens. Ici
$$\mathbf{D}^\top\mathbf{D} = \begin{pmatrix} 0{,}0168 & 0{,}0444 \\ 0{,}0444 & 0{,}1352 \end{pmatrix}, \qquad \mathbf{D}^\top\mathbf{D}\begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 0{,}15 \\ 0{,}45 \end{pmatrix} = 0{,}15\begin{pmatrix} 1 \\ 3 \end{pmatrix} :$$
$\mathbf{u} = \frac{1}{\sqrt{10}}(1, 3)$, de valeur propre 0,15 ; l'autre vaut $0{,}1520 - 0{,}15 = 0{,}002$ (la trace). La pente 3 de l'allométrie est retrouvée. Quand les différences sont peu nombreuses et les coordonnées très nombreuses, on forme plutôt leur matrice de Gram $\mathbf{D}\mathbf{D}^\top$, la plus petite des deux (M28) : elle a les mêmes valeurs propres non nulles, et si $\mathbf{g}$ est un vecteur propre de sa plus grande valeur propre, l'axe est dirigé par $\mathbf{D}^\top\mathbf{g}$.

### Ce qui reste

Trois truites : $\mathbf{x}_1 = (3{,}0 ;\ 4{,}5)$, $\mathbf{x}_2 = (3{,}2 ;\ 5{,}1)$ et $\mathbf{x}_3 = (3{,}1 ;\ 5{,}1)$, soit environ 20 cm et 90 g, 25 cm et 164 g, 22 cm et 164 g. On retire la direction de taille $\mathbf{u}$. Le reste est porté par $\mathbf{w} = \frac{1}{\sqrt{10}}(3, -1)$ : $\mathbf{r} = (\mathbf{x}\cdot\mathbf{w})\,\mathbf{w}$, et
$$\mathbf{r}_1 = \mathbf{r}_2 = \tfrac{4{,}5}{10}(3, -1) = (1{,}35 ;\ -0{,}45), \qquad \mathbf{r}_3 = \tfrac{4{,}2}{10}(3, -1) = (1{,}26 ;\ -0{,}42).$$
Les truites 1 et 2 se confondent : $\mathbf{x}_2 - \mathbf{x}_1 = 0{,}2\,(1, 3)$ est tout entier le long de $\mathbf{u}$, et leur distance passe de $0{,}2\sqrt{10} \approx 0{,}632$ à 0. Entre les truites 1 et 3, elle passe de $\sqrt{0{,}37} \approx 0{,}608$ à $\frac{0{,}3}{\sqrt{10}} \approx 0{,}095$, et Pythagore se vérifie : $0{,}37 = 0{,}009 + \frac{1{,}9^2}{10}$. Ce qui reste est la **corpulence** : la coordonnée $\mathbf{x}\cdot\mathbf{w} = (3\ln L - \ln m)/\sqrt{10}$ est, au signe, à un facteur et à une constante près, le logarithme du **coefficient de condition** de Fulton (*condition factor*) $100\,m/L^3$, qui vaut environ 1,11 pour les truites 1 et 2 et 1,50 pour la truite 3, plus ronde.

**Ce que le retrait ne fait pas.** Il efface la composante le long de $\mathbf{u}$, et elle seule. Si la taille se lit aussi ailleurs, par une mesure de plus qui grandit avec elle sans être exactement le long de $\mathbf{u}$ (l'âge, la longueur d'une nageoire), elle reste devinable après le retrait : on retire une **direction**, pas une information. Et une direction estimée sur peu de différences n'est elle-même qu'une estimation.

![Trois panneaux. À gauche, les trois différences d₁, d₂, d₃ en flèches depuis l'origine, dans le plan des différences de ln L et de ln m, et la droite de leur premier axe, u = (1, 3)/√10, de pente 3 : λ₁ = 0,150 et λ₂ = 0,002. Au centre, les trois truites dans le plan (ln L, ln m) et les droites de direction u qui passent par elles : les truites 1 et 2 sont sur la même droite, la truite 3 sur une autre. À droite, ce qui reste après le retrait de u, sur la droite R(3, −1) : les truites 1 et 2 tombent au même point (1,35 ; −0,45), la truite 3 à côté, en (1,26 ; −0,42)](figures/direction.png)

⚠️ **Erreur classique.** Oublier de diviser par $\mathbf{u}\cdot\mathbf{u}$ quand $\mathbf{u}$ n'est pas unitaire (🐛 MB2.17) : le reste n'est plus orthogonal à $\mathbf{u}$. Croire que toutes les distances sont gardées, ou qu'elles diminuent toutes de la même quantité. Centrer les différences avant de chercher leur premier axe : elles perdraient leur sens.

🔗 **Dans workbookIA** — le chapitre B2 discute du retrait d'une direction d'un nuage de vecteurs ; ce paragraphe dit ce que l'opération fait aux distances, et ce qu'elle ne fait pas.

## §8 · D'éléments à des ensembles : la moyenne masquée et le coût des comparaisons par paires

### La moyenne masquée

Des capteurs de ruches relèvent, chaque jour, la température intérieure (°C) et la masse de la ruche (kg). Les ruches n'ont pas le même nombre de relevés. Pour les ranger dans un même tableau de forme $(\text{ruches}, L, 2)$, on **complète** chaque suite par des zéros jusqu'à la longueur $L$ de la plus longue (*padding*), et l'on garde un **masque** (*mask*) $m_t$, qui vaut 1 pour un vrai relevé et 0 pour un zéro ajouté.

> **Définition.** La **moyenne masquée** (*masked mean*) d'une suite complétée $\mathbf{h}_1, \ldots, \mathbf{h}_L$ de masque $m_1, \ldots, m_L$, avec au moins un $m_t = 1$, est
> $$\bar{\mathbf{h}} = \frac{\sum_{t=1}^{L}m_t\,\mathbf{h}_t}{\sum_{t=1}^{L}m_t} .$$
> Elle ne dépend pas du remplissage : ajouter des $\mathbf{h}_t$ de masque 0, quels qu'ils soient, ne change ni le numérateur ni le dénominateur.

**Exemple.** Une ruche a quatre relevés, $(34, 41)$, $(35, 42)$, $(35, 43)$ et $(36, 42)$, complétés par deux zéros pour atteindre $L = 6$, de masque $(1, 1, 1, 1, 0, 0)$. La moyenne masquée vaut $\frac14(140, 168) = (35, 42)$. La moyenne des six lignes, $\frac16(140, 168) \approx (23{,}3 ;\ 28)$, mélange les vrais relevés aux zéros : une ruche à 23 °C serait morte. Pour toutes les ruches à la fois, c'est une somme le long de l'axe des relevés, divisée par la somme du masque le long du même axe (M20).

### Le coût des comparaisons par paires

Pour trouver les ruches qui se ressemblent, on peut comparer leurs séries **par paires** (*pairwise comparisons*), par une procédure qui regarde les deux séries ensemble. Avec $n$ ruches, il y a
$$\binom{n}{2} = \frac{n(n - 1)}{2}$$
paires (R8) : un coût **quadratique**. On peut aussi **résumer** chaque série une fois en un vecteur (sa moyenne masquée, par exemple), puis obtenir tous les cosinus d'un coup : on normalise les résumés, on les range en lignes d'une matrice $\mathbf{R}$ de forme $(n, d)$, et $\mathbf{R}\mathbf{R}^\top$, la matrice de Gram de M28, contient les $n^2$ produits scalaires.

Pour 1 200 ruches, $\binom{1\,200}{2} = 719\,400$ paires : à 2 ms par comparaison de deux séries, environ 1 439 s, soit 24 minutes. Les 1 200 résumés, à 2 ms chacun, prennent 2,4 s, puis le produit matriciel quelques millièmes de seconde. En contrepartie, une comparaison qui voit les deux séries ensemble peut les aligner, ce qu'un résumé fait séparément ne peut plus faire.

⚠️ **Erreur classique.** Diviser par la longueur $L$ du tableau au lieu du nombre de vrais relevés $\sum_t m_t$. Oublier que le masque sert aussi à toute autre réduction : un maximum sur des températures négatives serait faussé par les zéros ajoutés. Compter $n^2$ paires au lieu de $\binom{n}{2}$, ou oublier que le nombre de paires croît comme $n^2/2$.

🔗 **Dans workbookIA** — le chapitre B2 résume des suites de vecteurs de longueurs différentes par une moyenne masquée, et compare deux façons de mesurer la ressemblance de deux éléments ; ce paragraphe donne la moyenne, son invariance et le décompte.

## Les pièges classiques ⚠️ (récapitulatif)

- **Bases** : lire les restes du dernier au premier ; grouper les bits par quatre en partant de la droite ; $\lceil\log_2 N\rceil$ bits pour numéroter $N$ valeurs, $\lfloor\log_2 N\rfloor + 1$ bits pour écrire l'entier $N$.
- **PMI** : le total $N$ dans le lift ; $\ln$, en nats ; l'information mutuelle est la moyenne des PMI, pas des PPMI ; $-\infty$ n'est pas une erreur.
- **Événements rares** : la borne $\min(-\ln p(x), -\ln p(y))$ réserve les grandes PMI aux cases rares, qui sont aussi les plus mal estimées.
- **Lissage** : élever les comptes à la puissance $\alpha$, renormaliser, et ne lisser que la marge ; l'ordre des lignes dans une colonne ne change jamais.
- **SVD** : $\mathbf{U}_k\mathbf{S}_k^\beta$ et $\mathbf{V}_k\mathbf{S}_k^{1-\beta}$, jamais deux fois $\beta$ ; les cosinus dépendent en général de $\beta$ ; ne pas centrer une grande table creuse.
- **Sous-échantillonnage** : seule l'ordonnée à l'origine bouge, de $\ln(s_1/s_0)$ ; on la corrige avant de lire des probabilités.
- **Voisins** : cosinus et non produit scalaire ; exclure $\mathbf{a}$, $\mathbf{b}$ et $\mathbf{c}$.
- **Directions et masques** : diviser par $\mathbf{u}\cdot\mathbf{u}$ ; seule la composante sur $\mathbf{u}$ disparaît ; diviser par $\sum_t m_t$, pas par $L$.

## Et maintenant

**Dans ce dépôt** : MB3 reprend les moyennes pondérées, avec des poids donnés par une softmax, et les masques comme conditionnement ; MB4 factorise des matrices de rang faible, montre que deux factorisations de rang $k$ diffèrent d'une matrice inversible, et pèse un indice rare par le logarithme d'un rapport de cotes.

**Dans workbookIA** : le chapitre B2 découpe des textes en tokens, à partir de leurs octets ; il construit des vecteurs de mots en comptant, puis en factorisant une table de PPMI lissée par une SVD tronquée ; il les apprend aussi avec word2vec, une régression logistique sur des paires ; il cherche des voisins et des analogies par le cosinus, discute du retrait d'une direction, et résume des phrases par une moyenne masquée pour chercher des passages semblables.

## Pour aller plus loin

- K. W. Church et P. Hanks, « Word Association Norms, Mutual Information, and Lexicography », *Computational Linguistics*, vol. 16, n° 1, 1990, p. 22-29 : la PMI comme mesure d'association.
- G. Bouma, « Normalized (Pointwise) Mutual Information in Collocation Extraction », *Proceedings of the Biennial GSCL Conference*, 2009 : la PMI normalisée.
- R. L. Prentice et R. Pyke, « Logistic Disease Incidence Models and Case-Control Studies », *Biometrika*, vol. 66, n° 3, 1979, p. 403-411 : la régression logistique sur un échantillon cas-témoins, où seule l'ordonnée à l'origine est faussée.
- G. King et L. Zeng, « Logistic Regression in Rare Events Data », *Political Analysis*, vol. 9, n° 2, 2001, p. 137-163 : la correction de l'ordonnée à l'origine (*prior correction*) quand on sous-échantillonne une classe.
- O. Levy et Y. Goldberg, « Neural Word Embedding as Implicit Matrix Factorization », *Advances in Neural Information Processing Systems 27* (NIPS 2014) : le résultat cité au §5.
- `annexes/symboles.md`, `annexes/formulaire.md` et `annexes/erreurs_frequentes.md`.
