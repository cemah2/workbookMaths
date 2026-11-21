# M28 · Matrice de Gram, montée sur l'entrée et lois tronquées — fiche de cours

> Ce chapitre réunit six outils. La **matrice de Gram** d'une famille de vecteurs, lue dans les deux sens, devient une **matrice des moments d'ordre 2** quand on la divise par le nombre d'échantillons ; elle connaît toutes les longueurs et tous les angles, donc les **distances**, et l'on retrouve à partir des distances une **configuration** de points, à une isométrie près. **Optimiser l'entrée** d'une fonction dont les paramètres sont fixés : montée de gradient, **pas normalisé**, **projection sur un pavé**, coordonnées gelées, et ce que la montée trouve. La **variation totale** d'une grille, forme quadratique d'un laplacien, lisse ce qu'on lui donne ; les **fréquences spatiales** disent ce qu'elle pénalise et ce que laisse passer un flou. Une loi catégorielle se **tempère**, se **tronque** (top-k, top-p) et paie sa troncature en divergence KL. Enfin, une **itération déterministe sur un ensemble fini** finit toujours par boucler. Le chapitre 28 de workbookIA applique ces outils à la visualisation des réseaux, au transfert de style et à la génération de texte.

| | |
|---|---|
| **Sections** | §1 à §6 |
| **Temps total estimé** | ≈ 13,6 h : lecture et calculs de la fiche ≈ 2 h 30, exercices ≈ 10 h 30, 16 flashcards ≈ 30 min (parcours essentiel ≈ 10,4 h) |
| **Prérequis** | R0 (division euclidienne et reste) ; R9 (cosinus, radians, périodicité) ; M02b (loi catégorielle, tirage par inversion de la fonction de répartition) ; M02c (matrice de covariance, facteur $\frac1n$) ; M03 (loi conditionnelle) ; M05a (convexité d'une fonction d'une variable) ; M05b (gradient, montée et descente) ; M06 (entropie, divergence KL, infinie quand le support manque) ; M07 (produit scalaire, normes, Cauchy-Schwarz, cosinus) ; M09a (transposée, $\mathbf{X}^\top\mathbf{X}$ et $\mathbf{X}\mathbf{X}^\top$) ; M09b (ridge) ; M10 (fonctions convexes de plusieurs variables) ; M12a (application linéaire, image, dimension) ; M12b (matrices orthogonales, projection orthogonale) ; M12c (théorème spectral, quotient de Rayleigh, méthode de la puissance, matrices semi-définies positives) ; M12d ($\mathbf{A}^\top\mathbf{A}$ et $\mathbf{A}\mathbf{A}^\top$, approximation de rang faible, ACP quand $n < p$) ; M13b (matrice de Gram d'un noyau) ; M16 (principe des tiroirs) ; M17 (loi de Boltzmann et ses limites en température) ; M18 (gradient d'une forme quadratique, un passage inverse pour toutes les entrées) ; M19 (projection sur un pavé, pas critique $2/\lambda_{\max}$) ; M20 (matrice de centrage) ; M21 (laplacien discret, moyenne mobile, matrices circulantes) ; M22 ($\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert_\infty$) ; M25a (formules de soustraction, §8) |
| **Fichiers du chapitre** | `02_exercices.md` (quiz, papier) · `03_notebook.ipynb` · `04_indices.md` · `05_solutions.md` et `05_solutions.ipynb` · `06_mes_reponses.md` · `flashcards.csv` |
| **mymath** | `sampling.py` : `points_from_gram`, `temper`, `smallest_mass_set` |
| **Références** | pas de MML (le livre ne traite ni la variation totale, ni les fréquences, ni les troncatures, ni les itérations sur un ensemble fini, et tu as lu ses pages sur $\mathbf{A}^\top\mathbf{A}$ et sur la matrice de Gram d'un noyau en M12d et M13b) ; I. Borg et P. J. F. Groenen, *Modern Multidimensional Scaling*, ch. 12 ; A. Holtzman et coll., *The Curious Case of Neural Text Degeneration* ; D. E. Knuth, *The Art of Computer Programming*, vol. 2, §3.1 ; L. I. Rudin, S. Osher et E. Fatemi (variation totale en valeur absolue) |

## Comment utiliser ce chapitre

**Ordre conseillé.**
1. `python tools/start_chapter.py M28` (sur Colab : `00_setup/COLAB.md` §2) : il copie le notebook, ta feuille de réponses et le squelette `mymath/sampling.py`.
2. Section par section : lis **crayon en main** et refais chaque calcul, puis fais les exercices de la section, quiz 🧠 d'abord. Ce chapitre n'a pas de lecture de MML ; les références de « Pour aller plus loin » sont facultatives.
3. Les exercices ✏️ et 🔗 se font sur papier, dans ta copie de `06_mes_reponses.md`, puis se vérifient dans la **partie 0** du notebook. Les démonstrations ∂ se rédigent dans ta copie et se jugent avec la grille de relecture de `05_solutions.md`.

Les six sections se lisent presque indépendamment : le §2 s'appuie sur le §1, et les autres ne demandent que les chapitres cités en prérequis.

| Section | Quiz 🧠 et rappels 🔁 | Papier et réflexion | Notebook |
|---|---|---|---|
| §1 Gram, moments d'ordre 2, coût | Q1 | M28.1 ✏️ | |
| §2 Des distances aux positions | Q1 | M28.2 ✏️, M28.8 ∂, M28.12 🗣️ | M28.13 🔨, M28.17 🐛, M28.18 🛠️, M28.19 🏆 |
| §3 Monter sur l'entrée | Q2, R1 | M28.3 ✏️, M28.9 ∂ | M28.15 🔮, M28.17 🐛 |
| §4 Variation totale, fréquences | Q3, R2 | M28.4 ✏️, M28.5 ✏️ | M28.16 🎨 |
| §5 Température, top-k, top-p | Q4, R3 | M28.6 ✏️, M28.10 ∂, M28.11 🔗, M28.E1 💼 | M28.14 🔨 |
| §6 Une itération finie boucle | Q5 | M28.7 ✏️ | M28.17 🐛 |

Parcours essentiel : tout sauf M28.8, M28.9, M28.E1, M28.13, M28.18 et M28.19.

📐 **Notations.**
- **§1 et §2.** Les $n$ points (ou vecteurs) $\mathbf{x}_1, \ldots, \mathbf{x} _n$ de $\mathbb{R}^d$, numérotés à partir de 1 comme les lignes d'une matrice, sont les **lignes** de $\mathbf{X}$, de forme $(n, d)$, comme en M13b ; $\mathbf{G} = \mathbf{X}\mathbf{X}^\top$ et $G _{ij} = \mathbf{x}_i^\top\mathbf{x}_j$. Quand les $N$ colonnes de $\mathbf{X}$ sont des échantillons, $\mathbf{M} = \frac1N\mathbf{X}\mathbf{X}^\top$ : l'inverse de la convention des datasets, qui met les exemples en lignes (§1). $\mathbf{D}^{(2)}$ est la matrice des **carrés** des distances, $\mathbf{1}$ le vecteur dont toutes les coordonnées valent 1, $\mathbf{J} = \mathbf{I} - \frac1n\mathbf{1}\mathbf{1}^\top$ la matrice de centrage de M20 (qui la notait $\mathbf{C}$), $\mathbf{G} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ une diagonalisation, de valeurs propres $\lambda_1 \ge \cdots \ge \lambda_n$.
- **§3.** $f(\mathbf{x} ; \boldsymbol{\theta})$ est une fonction d'une entrée $\mathbf{x} \in \mathbb{R}^n$ et de paramètres $\boldsymbol{\theta}$ fixés ; $\mathbf{g} = \nabla f(\mathbf{x})$ est son gradient par rapport à $\mathbf{x}$, de la forme de $\mathbf{x}$ (la convention de l'optimisation, BIBLE §6) ; $\eta > 0$ est un pas ; $\operatorname{rms}(\mathbf{g}) = \sqrt{\frac1n\sum_i g_i^2}$ ; $\operatorname{sign}(\mathbf{g})$ se prend coordonnée par coordonnée ; $\mathbf{P}_F$ est la projection sur les coordonnées libres $F$ ; $m$ est un nombre de réponses linéaires ; les coordonnées de $\mathbf{x}$ sont numérotées à partir de 1, comme au §1.
- **§4.** Une grille $x_{ij}$ a ses lignes $i$ et ses colonnes $j$ numérotées à partir de 0 ; $\mathbf{L}$ est son laplacien. La **variation totale** $\mathrm{VT}(\mathbf{x})$ est la somme des **carrés** des différences entre voisins, comme dans workbookIA ; la version avec des valeurs absolues est toujours nommée « variation totale en valeur absolue ». $f$ est une fréquence en cycles par case, $\omega = 2\pi f$ la même en radians par case ; $\tau > 0$ règle un lissage.
- **§5.** Une loi est un **vecteur de probabilités** $\mathbf{p} = (p_0, \ldots, p_{K-1})$, jamais des scores ; ses issues sont numérotées à partir de 0, comme dans `sampling.py`, et, entre deux probabilités égales, la plus petite issue passe d'abord. $T \ge 0$ est une température, $\mathbf{p}^{(T)}$ la loi tempérée, $S$ un ensemble d'issues, $P(S) = \sum_{i \in S}p_i$ sa masse, $\mathbf{p}_S$ la loi conditionnelle, $m \in\ ]0, 1]$ le seuil d'un top-p (la lettre $p$ est déjà prise). Entropies et divergences KL sont en nats.
- **§6.** $E$ est un ensemble fini à $N$ éléments, $f : E \to E$, $u_{t+1} = f(u_t)$ ; $\mu$ est la prépériode et $\lambda$ la période.
- **Lettres à double sens.** $\lambda$ est une valeur propre aux §1 à §4 et une période au §6 ; $m$ un nombre de réponses au §3 et une masse au §5 ; $N$ un nombre d'échantillons au §1 et la taille de $E$ au §6 ; $f$ une fonction aux §3 et §6, une fréquence au §4 ; $\mathbf{A}$ la matrice d'une forme quadratique au §3 et la matrice d'adjacence d'une grille au §4, dont la matrice des degrés $\mathbf{D}$ n'a rien à voir avec $\mathbf{D}^{(2)}$. Le contexte tranche. De même, $E$ désigne des énergies au §5 et un ensemble au §6, $\mathbf{g}$ un gradient au §3 et la diagonale de $\mathbf{G}$ au §2, $c$ une constante et $\mathbf{c}$ un point au §3, $d$ une dimension et $d_{ij}$ une distance, $r$ un rayon au §3 et $r_i$ une moyenne au §2, $\mathbf{w}$ une forme linéaire au §3 et $w$ une longueur de contexte au §6, $\boldsymbol{\theta}$ des paramètres et $\theta_{ij}$ un angle ; A est aussi un capteur au §2.

Vocabulaire anglais de ce chapitre : *Gram matrix*, *second-moment matrix*, *classical multidimensional scaling*, *double centering*, *Euclidean distance matrix*, *configuration*, *up to an isometry*, *gradient ascent*, *normalized gradient*, *root mean square*, *sign gradient*, *projected gradient ascent*, *box constraints*, *frozen coordinates*, *power iteration*, *total variation*, *graph Laplacian*, *diffusion*, *critical step size*, *spatial frequency*, *period*, *phase*, *Nyquist frequency*, *aliasing*, *checkerboard*, *low-pass filter*, *gain*, *discrete Fourier transform*, *temperature*, *tempered distribution*, *top-k sampling*, *nucleus sampling*, *highest-probability set*, *truncation*, *total variation distance*, *eventually periodic*, *preperiod*, *cycle length*, *cycle detection*, *tortoise and hare*, *greedy decoding*.

## Objectifs d'apprentissage

À la fin du chapitre, tu sais :
- **calculer** la matrice de Gram d'une famille de vecteurs dans les deux sens et la matrice des moments d'ordre 2, et **choisir** laquelle former selon son coût ;
- **lire** des distances dans une matrice de Gram, **retrouver** une matrice de Gram à partir de distances (double centrage), puis des positions à une isométrie près ;
- **énoncer**, puis **démontrer** (∂ M28.8), que deux familles de vecteurs de même matrice de Gram se déduisent l'une de l'autre par une isométrie ;
- **faire** une montée de gradient projetée sur un pavé, avec un pas normalisé ou des coordonnées gelées, et **prévoir** où elle s'arrête pour une fonction linéaire, quadratique ou convexe ;
- **écrire** la variation totale d'une grille comme une forme quadratique, **calculer** son gradient et un pas de lissage, et **comparer** le carré et la valeur absolue ;
- **lire** la période et la fréquence d'un motif, **situer** la fréquence de Nyquist, et **calculer** ce qu'en font la variation totale et un flou ;
- **tempérer** une loi catégorielle, la **tronquer** par top-k ou top-p, et **calculer** le coût de la troncature en divergence KL ;
- **trouver** la prépériode et la période d'une itération sur un ensemble fini, et **expliquer** pourquoi un décodage glouton à état fini boucle.

## L'essentiel en 8 lignes

1. **Gram** : $\mathbf{G} = \mathbf{X}\mathbf{X}^\top$ (produits scalaires des lignes, $n \times n$) et $\mathbf{X}^\top\mathbf{X}$ (des colonnes, $d \times d$) ont les mêmes valeurs propres non nulles ; symétriques, semi-définies positives. Si les $N$ colonnes sont des échantillons, $\mathbf{M} = \frac1N\mathbf{X}\mathbf{X}^\top$ est la matrice des moments d'ordre 2, la covariance après centrage des lignes. Former la plus petite : $n^2d$ contre $d^2n$.
2. **Distances** : $\lVert\mathbf{x} _i - \mathbf{x} _j\rVert^2 = G _{ii} + G  _{jj} - 2G _{ij}$ ; pour des points centrés, $\mathbf{G} = -\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$, et des distances sont euclidiennes si et seulement si cette matrice est semi-définie positive ; les colonnes $\sqrt{\lambda_k}\thinspace\mathbf{q}_k$ donnent des positions ; même matrice de Gram, même configuration à une isométrie près (∂ M28.8).
3. **Monter sur l'entrée** : $\mathbf{x} \leftarrow \mathbf{x} + \eta\thinspace\mathbf{g}$ ; les pas normalisés $\mathbf{g}/\lVert\mathbf{g}\rVert$, $\mathbf{g}/\operatorname{rms}(\mathbf{g})$ et $\operatorname{sign}(\mathbf{g})$ ne changent pas quand $f$ est multipliée par $c > 0$ ; sur un pavé, on coupe le **point** après le pas ; des coordonnées gelées : $\mathbf{P}_F\mathbf{g}$, la meilleure direction permise.
4. **Ce qu'on trouve** : une forme linéaire, $r\thinspace\mathbf{w}/\lVert\mathbf{w}\rVert$ sur une boule et un sommet sur un pavé ; $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ sur la sphère, le vecteur propre dominant (montée renormalisée = méthode de la puissance de $\mathbf{I} + 2\eta\mathbf{A}$) ; une fonction convexe sur un pavé, un sommet (∂ M28.9), pas forcément le meilleur.
5. **Variation totale** $= \sum$ (différences entre voisins)$^2 = \mathbf{x}^\top\mathbf{L}\mathbf{x}$, gradient $2\mathbf{L}\mathbf{x}$ ; un pas de descente est une diffusion, stable pour $\eta < 1/\lambda_{\max}(\mathbf{L})$ ; une marche étalée sur $n$ pas coûte $h^2/n$ au carré (il préfère les rampes) et $h$ en valeur absolue (elle garde les bords).
6. **Fréquences** : $\cos(2\pi(f_1i + f_2j) + \varphi)$ a pour période $1/\sqrt{f_1^2 + f_2^2}$ ; Nyquist $\frac12$ (le damier) ; $f$ et $1 - f$ se replient l'une sur l'autre ; variation totale / énergie $= 4\sin^2(\omega/2)$ par direction ; une moyenne mobile de trois cases a pour gain $\frac{1 + 2\cos\omega}{3}$.
7. **Lois** : $p_i^{(T)} \propto p_i^{1/T}$, Boltzmann des énergies $-\ln p_i$ ; les zéros restent nuls ; $T \to 0$ : les plus probables, $T \to \infty$ : uniforme sur le support ; l'entropie croît avec $T$. Top-k et top-p conditionnent sur $S$ ; les issues les plus probables, prises jusqu'à atteindre $m$, forment un plus petit ensemble de masse $\ge m$ (∂ M28.10) ; $T$ garde le top-k, refroidir rétrécit le top-p ; $\mathrm{KL}(\mathbf{p}_S \thinspace\Vert\thinspace \mathbf{p}) = -\ln P(S)$, $\frac12\lVert\mathbf{p}_S - \mathbf{p}\rVert_1 = 1 - P(S)$.
8. **Boucles** : sur un ensemble fini de $N$ éléments, $u_{t+1} = f(u_t)$ devient périodique, avec $\mu + \lambda \le N$ ; un générateur glouton à contexte fini boucle donc ; Floyd trouve $\mu$ et $\lambda$ avec deux valeurs en mémoire.

## §1 · La matrice de Gram d'une famille de vecteurs : deux lectures, moments d'ordre 2 et coût

### Tous les produits scalaires d'une famille

Trois sondes d'un entrepôt frigorifique relèvent, chaque heure pendant cinq heures, leur écart à la température de consigne, en °C. Chaque sonde donne un vecteur de $\mathbb{R}^5$ ; on les range en lignes :
```math
\mathbf{X} = \begin{pmatrix} 2 & 1 & 0 & -1 & -2 \cr 1 & 2 & 0 & -2 & -1 \cr -1 & 0 & 2 & 0 & -1 \end{pmatrix}.
```

> **Définition.** La **matrice de Gram** (*Gram matrix*) d'une famille de vecteurs $\mathbf{x}_1, \ldots, \mathbf{x} _n$ de $\mathbb{R}^d$, rangés en lignes d'une matrice $\mathbf{X}$ de forme $(n, d)$, est la matrice $n \times n$ de leurs produits scalaires :
> $$\mathbf{G} = \mathbf{X}\mathbf{X}^\top, \qquad G _{ij} = \mathbf{x}_i^\top\mathbf{x}_j .$$

Pour les sondes, $G_{12} = 2 \times 1 + 1 \times 2 + 0 + (-1)(-2) + (-2)(-1) = 8$, et en tout
```math
\mathbf{G} = \begin{pmatrix} 10 & 8 & 0 \cr 8 & 10 & 0 \cr 0 & 0 & 6 \end{pmatrix}.
```

Tu connais déjà ses propriétés. Elle est symétrique. Elle est **semi-définie positive** : $\mathbf{v}^\top\mathbf{G}\mathbf{v} = \lVert\mathbf{X}^\top\mathbf{v}\rVert^2 \ge 0$ (M12c.17). Sa diagonale porte les carrés des normes, $G_{ii} = \lVert\mathbf{x}_i\rVert^2$. Son rang est celui de $\mathbf{X}$, au plus $\min(n, d)$. Et c'est la matrice de Gram du noyau linéaire de M13b, `polynomial_kernel(X, X, 1, 0)`. Le §2 montre la réciproque : toute matrice symétrique semi-définie positive est une matrice de Gram.

### Deux lectures : XXᵀ et XᵀX

La même matrice $\mathbf{X}$ donne une seconde matrice de Gram, $\mathbf{X}^\top\mathbf{X}$, de forme $(d, d)$ : celle des **colonnes**. Pour les sondes, chaque colonne est une heure, un vecteur de $\mathbb{R}^3$ (les trois écarts de cette heure-là), et $\mathbf{X}^\top\mathbf{X}$ est $5 \times 5$.

> **Propriété** (M12d). $\mathbf{X}\mathbf{X}^\top$ et $\mathbf{X}^\top\mathbf{X}$ ont les mêmes valeurs propres non nulles, avec les mêmes multiplicités ; leurs autres valeurs propres sont nulles.

L'idée : si $\mathbf{X}\mathbf{X}^\top\mathbf{v} = \lambda\mathbf{v}$ avec $\lambda \ne 0$, alors $\mathbf{w} = \mathbf{X}^\top\mathbf{v}$ n'est pas nul et $\mathbf{X}^\top\mathbf{X}\thinspace\mathbf{w} = \mathbf{X}^\top(\mathbf{X}\mathbf{X}^\top\mathbf{v}) = \lambda\mathbf{w}$. Pour les sondes, le bloc $`\begin{pmatrix} 10 & 8 \cr 8 & 10 \end{pmatrix}`$ a pour valeurs propres $18$ (vecteur $(1, 1){}$) et $2$ (vecteur $(1, -1){}$), et la troisième sonde ajoute $6$ : $\mathbf{G}$ a pour valeurs propres 18, 6 et 2, et $\mathbf{X}^\top\mathbf{X}$ a 18, 6, 2, 0 et 0. Les deux traces valent 26, la somme des carrés des quinze nombres de $\mathbf{X}$.

### Diviser par le nombre d'échantillons : la matrice des moments d'ordre 2

Lisons maintenant les colonnes comme des **échantillons** : à l'heure $k$, le vecteur $(x_{1k}, \ldots, x_{nk})$ des $n$ sondes est une observation d'un vecteur aléatoire de $\mathbb{R}^n$.

> **Définition.** Quand les $N$ colonnes de $\mathbf{X}$ sont des échantillons, la **matrice des moments d'ordre 2** (*second-moment matrix*) est
> $$\mathbf{M} = \frac1N\thinspace\mathbf{X}\mathbf{X}^\top, \qquad M_{ij} = \frac1N\sum_{k=1}^{N}x_{ik}\thinspace x_{jk} :$$
> la moyenne, sur les échantillons, du produit des mesures $i$ et $j$.

Pour les sondes, $N = 5$ et
```math
\mathbf{M} = \begin{pmatrix} 2 & 1{,}6 & 0 \cr 1{,}6 & 2 & 0 \cr 0 & 0 & 1{,}2 \end{pmatrix} \ (\text{°C}^2).
```
Ici chaque ligne de $\mathbf{X}$ est de moyenne nulle : ce sont des écarts dont la somme sur les cinq heures vaut 0. Alors $\mathbf{M}$ est exactement la **matrice de covariance** des trois sondes, avec le facteur $\frac1N$ (M02c). En général, on centre d'abord chaque ligne (on lui retire sa moyenne sur les $N$ échantillons) pour obtenir la covariance. Le coefficient $1{,}6$ dit que les sondes 1 et 2 varient ensemble ; le 0 dit que la troisième varie sans lien linéaire avec elles.

Diviser par $N$ rend comparables des séries de longueurs différentes : une somme de produits grandit avec le nombre d'échantillons, une moyenne non. Avec les échantillons en lignes, comme dans un dataset, la même matrice s'écrit $\frac1N\tilde{\mathbf{X}}^\top\tilde{\mathbf{X}}$, où $\tilde{\mathbf{X}} = \mathbf{X}^\top$.

### Ce que coûte une matrice de Gram

$\mathbf{X}\mathbf{X}^\top$ a $n^2$ coefficients (la moitié suffit, par symétrie), chacun une somme de $d$ produits : de l'ordre de $n^2d$ multiplications et $n^2$ nombres en mémoire. $\mathbf{X}^\top\mathbf{X}$ en demande $d^2n$ et $d^2$. Comme leurs valeurs propres non nulles sont les mêmes, on **forme la plus petite**. Pour 2 000 sondes relevées à $10^6$ instants, $\mathbf{M}$ est une matrice $2\thinspace000 \times 2\thinspace000$ : $4 \times 10^6$ nombres et environ $4 \times 10^{12}$ multiplications. La matrice des instants, $10^6 \times 10^6$, aurait $10^{12}$ coefficients, 8 To en `float64`, et coûterait $2 \times 10^{15}$ multiplications. C'est la même idée que l'ACP quand il y a moins d'exemples que de features (M12d.12), où c'est la matrice des exemples qui est la plus petite : on forme toujours la plus petite des deux.

⚠️ **Erreur classique.** Diviser par le nombre de lignes au lieu du nombre d'échantillons ; confondre $\mathbf{X}\mathbf{X}^\top$ ($n \times n$, les lignes) et $\mathbf{X}^\top\mathbf{X}$ ($d \times d$, les colonnes) : écris la forme avant de calculer.

🔗 **Dans workbookIA** — le chapitre 28 forme des matrices de Gram de familles de vecteurs très longs ; ce paragraphe dit ce qu'elles contiennent et ce qu'elles coûtent.

## §2 · Ce que la matrice de Gram détermine : des distances aux positions, à une isométrie près

### Des longueurs, des angles, des distances

La matrice de Gram donne les longueurs, $\lVert\mathbf{x}  _i\rVert = \sqrt{G  _{ii}}$, les angles, $\cos\theta  _{ij} = G  _{ij}/\sqrt{G _{ii}G _{jj}}$ (M07), et donc les distances : en développant $(\mathbf{x}_i - \mathbf{x}_j)^\top(\mathbf{x}_i - \mathbf{x} _j)$,
$$\lVert\mathbf{x} _i - \mathbf{x} _j\rVert^2 = G _{ii} + G _{jj} - 2G _{ij}.$$
Entre les séries des sondes 1 et 2 : $10 + 10 - 2 \times 8 = 4$, une distance de 2 °C, ce que donne aussi leur différence $(1, -1, 0, 1, -1)$.

> **Invariance** (énoncée). Tourner le repère, avec ou sans symétrie ($\mathbf{x}_i \mapsto \mathbf{R}\mathbf{x}_i$ pour tous les $i$, $\mathbf{R}$ orthogonale), ne change pas $\mathbf{G}$ : une matrice orthogonale conserve les produits scalaires (M12b). Translater tous les points d'un même vecteur ne change pas les distances, mais change en général $\mathbf{G}$ (les normes changent).

Le mieux qu'on puisse espérer des distances est donc la configuration **à une isométrie près** (*up to an isometry*) : une rotation, une symétrie, une translation. On l'obtient :

> **Réciproque** (∂ M28.8). Si deux familles $\mathbf{x}_1, \ldots, \mathbf{x}_n$ et $\mathbf{y}_1, \ldots, \mathbf{y}_n$ de $\mathbb{R}^d$ ont la même matrice de Gram, il existe une matrice orthogonale $\mathbf{R}$ telle que $\mathbf{y}_i = \mathbf{R}\mathbf{x}_i$ pour tout $i$.

Avec le double centrage qui suit, on en tire : deux configurations qui ont les mêmes distances se déduisent l'une de l'autre par une isométrie.

### Des distances à la matrice de Gram : le double centrage

On ne connaît que les distances, mesurées au télémètre. Plaçons l'origine au centre de gravité des points, $\sum_i\mathbf{x}_i = \mathbf{0}$ : la matrice de Gram de cette configuration centrée est alors déterminée.

> **Propriété** (double centrage, *double centering*). Si les points sont centrés,
> $$\mathbf{G} = -\frac12\thinspace\mathbf{J}\thinspace\mathbf{D}^{(2)}\thinspace\mathbf{J}, \qquad \mathbf{J} = \mathbf{I} - \frac1n\mathbf{1}\mathbf{1}^\top,$$
> où $\mathbf{D}^{(2)}$ est la matrice des **carrés** des distances. Coefficient par coefficient : $G_{ij} = -\frac12\big(D^{(2)}_{ij} - r_i - r_j + s\big)$, avec $r_i$ la moyenne de la ligne $i$ de $\mathbf{D}^{(2)}$ et $s$ la moyenne de tous ses coefficients.

*Démonstration.* Notons $\mathbf{g}$ le vecteur de la diagonale de $\mathbf{G}$. La formule des distances s'écrit $\mathbf{D}^{(2)} = \mathbf{g}\mathbf{1}^\top + \mathbf{1}\mathbf{g}^\top - 2\mathbf{G}$. Comme $\mathbf{J}\mathbf{1} = \mathbf{0}$, les deux premiers termes disparaissent : $\mathbf{J}\mathbf{D}^{(2)}\mathbf{J} = -2\thinspace\mathbf{J}\mathbf{G}\mathbf{J}$. Les points étant centrés, $\mathbf{X}^\top\mathbf{1} = \sum_i\mathbf{x}_i = \mathbf{0}$, donc $\mathbf{G}\mathbf{1} = \mathbf{0}$ et $\mathbf{1}^\top\mathbf{G} = \mathbf{0}^\top$ : $\mathbf{J}\mathbf{G}\mathbf{J} = \mathbf{G}$. $\square$

**Exemple : trois capteurs.** Trois capteurs A, B et C sont posés sur un terrain : AB $= 8$ m, AC $=$ BC $= 5$ m. Alors
```math
\mathbf{D}^{(2)} = \begin{pmatrix} 0 & 64 & 25 \cr 64 & 0 & 25 \cr 25 & 25 & 0 \end{pmatrix}, \qquad r = \Big(\frac{89}{3}, \frac{89}{3}, \frac{50}{3}\Big), \qquad s = \frac{228}{9} = \frac{76}{3}.
```
$G_{11} = -\frac12\big(0 - \frac{178}{3} + \frac{76}{3}\big) = 17$, $G_{12} = -\frac12\big(64 - \frac{178}{3} + \frac{76}{3}\big) = -\frac12(64 - 34) = -15$, $G_{13} = -\frac12\big(25 - \frac{139}{3} + \frac{76}{3}\big) = -\frac12(25 - 21) = -2$, $G_{33} = -\frac12\big(0 - \frac{100}{3} + \frac{76}{3}\big) = 4$, et les autres par la symétrie entre A et B :
```math
\mathbf{G} = \begin{pmatrix} 17 & -15 & -2 \cr -15 & 17 & -2 \cr -2 & -2 & 4 \end{pmatrix}.
```
Chaque ligne a une somme nulle, comme il se doit pour des points centrés.

### De la matrice de Gram aux positions

> **Propriété** (des positions de matrice de Gram donnée). Soit $\mathbf{G}$ symétrique semi-définie positive, diagonalisée en $\mathbf{G} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ (théorème spectral, M12c), $\lambda_1 \ge \cdots \ge \lambda_n \ge 0$. La matrice $\mathbf{X}$ dont la colonne $k$ est $\sqrt{\lambda_k}\thinspace\mathbf{q}_k$ vérifie $\mathbf{X}\mathbf{X}^\top = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top = \mathbf{G}$ : ses lignes sont des points de matrice de Gram $\mathbf{G}$. On garde autant de colonnes que de valeurs propres non nulles, le rang de $\mathbf{G}$ : c'est la dimension de la configuration.

Pour les capteurs, les valeurs propres sont 32, 6 et 0, de vecteurs propres unitaires $\mathbf{q}_1 = \frac{1}{\sqrt2}(1, -1, 0)$ et $\mathbf{q}_2 = \frac{1}{\sqrt6}(1, 1, -2)$ (vérifie : $\mathbf{G}(1, -1, 0) = (32, -32, 0){}$). Les colonnes $\sqrt{32}\thinspace\mathbf{q}_1 = (4, -4, 0)$ et $\sqrt6\thinspace\mathbf{q}_2 = (1, 1, -2)$ donnent $A = (4, 1)$, $B = (-4, 1)$, $C = (0, -2)$ : AB $= 8$ et AC $= \sqrt{16 + 9} = 5$. La troisième valeur propre est nulle : la configuration est plane. La carte est juste à une isométrie près, et son symétrique par rapport à l'axe horizontal convient tout autant. C'est ce que calcule `points_from_gram` (🔨 M28.13), qui fixe le signe de chaque colonne. Double centrage des carrés des distances, puis théorème spectral : c'est le **positionnement multidimensionnel classique** (*classical multidimensional scaling*), le chapitre 12 de Borg et Groenen.

Pour une matrice de Gram centrée, ces colonnes sont les **scores de l'ACP** des points (M12d) : la première suit la direction où le nuage s'étale le plus, ici la base AB.

![Trois panneaux. À gauche, sept capteurs placés au hasard sur un terrain de 100 m sur 60 m, numérotés de 1 à 7. Au centre, les positions retrouvées à partir des seules distances (les deux colonnes √λ₁ q₁ et √λ₂ q₂), centrées en (0, 0) : la même carte, retournée par une symétrie et tournée d'environ 7° : chaque capteur est aux mêmes distances des autres, mais la symétrie renverse leur ordre quand on tourne autour du centre. À droite, les sept valeurs propres de −½ J D⁽²⁾ J : environ 8 355 et 2 792 m², puis cinq valeurs nulles, ce qui dit que les points sont dans un plan](figures/gram_carte.png)

> **Une matrice de distances est-elle euclidienne ?** (*Euclidean distance matrix* ; Schoenberg, admis). Des nombres $d_{ij} \ge 0$, avec $d_{ii} = 0$ et $d_{ij} = d_{ji}$, sont les distances de points d'un espace euclidien si et seulement si $-\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ est semi-définie positive. La plus petite dimension possible est alors son rang.

**Exemple.** Un carrefour, le point 1, est relié par trois routes de 1 km à trois villages 2, 3 et 4, qui ne sont reliés qu'en passant par lui : par la route, deux villages sont à 2 km. Les moyennes des lignes de $\mathbf{D}^{(2)}$ valent $r_1 = \frac34$ et $r_2 = r_3 = r_4 = \frac94$, et $s = \frac{15}{8}$ ; alors $G_{11} = -\frac12\big(0 - \frac32 + \frac{15}{8}\big) = -\frac{3}{16} < 0$. Un carré de norme négatif : aucun nuage de points, en aucune dimension, n'a ces distances (les valeurs propres sont $-\frac14$, 0, 2 et 2), qui respectent pourtant l'inégalité triangulaire. Trois villages à 1 km du carrefour et à 2 km l'un de l'autre seraient deux à deux diamétralement opposés, ce qui est impossible à trois.

Avec des distances mesurées, donc un peu fausses, de petites valeurs propres négatives apparaissent : on garde les plus grandes, positives : c'est la meilleure matrice de Gram de rang fixé (Eckart-Young, M12d, quand les valeurs négatives sont petites).

⚠️ **Erreur classique.** Faire le double centrage sur les distances au lieu de leurs **carrés** : $-\frac12\mathbf{J}\mathbf{D}\mathbf{J}$ n'est pas une matrice de Gram. Comparer deux configurations par leurs coordonnées : elles peuvent différer d'une rotation ou d'une symétrie ; compare des distances ou des matrices de Gram. Oublier que les distances ne donnent que la matrice de Gram des points **centrés**.

🔗 **Dans workbookIA** — le chapitre 28 résume des familles de vecteurs par leurs matrices de Gram ; ce paragraphe montre, dans un cadre géométrique, ce qu'une matrice de Gram connaît d'une famille de vecteurs.

## §3 · Optimiser l'entrée d'une fonction à paramètres fixés : montée projetée, pas normalisé, et ce que l'on trouve

### Une fonction à paramètres fixés, une entrée à régler

Une fonction $f(\mathbf{x} ; \boldsymbol{\theta})$ dépend d'une entrée $\mathbf{x}$ et de paramètres $\boldsymbol{\theta}$. Quand $\boldsymbol{\theta}$ est fixé, $f$ n'est plus qu'une fonction de $\mathbf{x}$, et l'on cherche l'entrée qui la rend grande. La **montée de gradient** (*gradient ascent*, M05b) s'écrit
$$\mathbf{x}_{t+1} = \mathbf{x}_t + \eta\thinspace\mathbf{g}_t, \qquad \mathbf{g}_t = \nabla f(\mathbf{x}_t).$$
Quand $f$ est une composition de fonctions simples, un seul passage inverse donne le gradient par rapport à toutes les coordonnées de $\mathbf{x}$ à la fois (M18).

**Exemple : trois placements.** Un épargnant met sur trois placements une fraction $x_i$ du plafond de chacun, entre 0 et 1 : le premier et le troisième rapportent, le deuxième, aux frais trop élevés, fait perdre. Son gain annuel, en centaines d'euros, est
$$f(\mathbf{x}) = 4x_1 - x_2 + 8x_3 = \mathbf{w}^\top\mathbf{x},$$
avec des coefficients estimés une fois pour toutes (ce sont les paramètres). Le gradient est constant : $\mathbf{g} = \mathbf{w} = (4, -1, 8)$, de norme 9.

### Le pas normalisé

Le pas ordinaire $\eta\thinspace\mathbf{g}$ suit la taille du gradient : exprime $f$ en euros au lieu de centaines d'euros, et tous les pas sont multipliés par 100. Un **pas normalisé** (*normalized gradient*) fixe la longueur et garde la direction, ou presque :
- $\mathbf{g}/\lVert\mathbf{g}\rVert$, de norme 1 : ici $\big(\frac49, -\frac19, \frac89\big) \approx (0{,}444 ;\ -0{,}111 ;\ 0{,}889)$ ;
- $\mathbf{g}/\operatorname{rms}(\mathbf{g})$, avec la **moyenne quadratique** (*root mean square*) $\operatorname{rms}(\mathbf{g}) = \sqrt{\frac1n\sum_ig_i^2}$, ici $\frac{9}{\sqrt3} = 3\sqrt3 \approx 5{,}20$ : la même direction, de norme $\sqrt n$, des coordonnées de l'ordre de 1 quel que soit $n$ ;
- $\operatorname{sign}(\mathbf{g})$ (*sign gradient*), coordonnée par coordonnée : $(1, -1, 1)$, de norme $\sqrt3$ aussi, mais d'une autre direction (cosinus $\frac{13}{9\sqrt3} \approx 0{,}834$ avec $\mathbf{g}$, un angle d'environ 33°).

> **Propriété** (invariance d'échelle). Pour $c > 0$, les trois pas normalisés de $cf$ sont ceux de $f$ ; le pas ordinaire est multiplié par $c$.

*Démonstration.* $\nabla(cf) = c\thinspace\nabla f$. Or $\lVert c\mathbf{g}\rVert = c\lVert\mathbf{g}\rVert$, $\operatorname{rms}(c\mathbf{g}) = c\operatorname{rms}(\mathbf{g})$ et $\operatorname{sign}(c\mathbf{g}) = \operatorname{sign}(\mathbf{g})$ puisque $c > 0$ : $c$ se simplifie dans les trois quotients. $\square$

Avec un pas normalisé, $\eta$ devient une longueur dans l'unité de $\mathbf{x}$, quelle que soit l'unité de $f$. Le revers : près d'un maximum, où $\mathbf{g}$ tend vers $\mathbf{0}$, il ne raccourcit pas ; avec $\eta$ fixe, les itérés oscillent autour du maximum, et l'on diminue $\eta$ en route.

### Rester dans un pavé : la montée projetée

Les fractions doivent rester dans $[0, 1]$. Après chaque pas, on projette le point sur le pavé $[\mathbf{l}, \mathbf{u}]$ (*box constraints*, M19 §8) :
$$\mathbf{x}_{t+1} = \operatorname{clip}(\mathbf{x}_t + \eta\thinspace\mathbf{g}_t,\ \mathbf{l},\ \mathbf{u}),$$
coordonnée par coordonnée (`np.clip`) : c'est la **montée projetée** (*projected gradient ascent*). Pour l'épargnant, depuis $\mathbf{x}_0 = (0{,}5 ;\ 0{,}5 ;\ 0{,}5)$ avec $\eta = 0{,}1$ : $\mathbf{x}_0 + \eta\thinspace\mathbf{g} = (0{,}9 ;\ 0{,}4 ;\ 1{,}3)$, coupé en $\mathbf{x}_1 = (0{,}9 ;\ 0{,}4 ;\ 1)$. La deuxième fraction baisse ensuite de 0,1 par pas : au bout de cinq pas, la montée est en $(1, 0, 1)$, où la projection ramène chaque pas au même point. Elle s'arrête sur un **sommet** du pavé.

### Geler des coordonnées

Certaines coordonnées ne doivent parfois pas bouger : une épargne bloquée. Notons $F$ l'ensemble des coordonnées **libres** et $\mathbf{P} _F$ la matrice diagonale qui vaut 1 sur $F$ et 0 ailleurs : c'est la projection orthogonale sur le sous-espace des vecteurs nuls hors de $F$ (M12b). Le pas devient $\mathbf{x} _{t+1} = \mathbf{x}_t + \eta\thinspace\mathbf{P}_F\thinspace\mathbf{g}_t$ : les coordonnées **gelées** (*frozen coordinates*) ne bougent pas, les autres suivent leur gradient.

> **Propriété.** Parmi les directions unitaires $\mathbf{d}$ qui ne bougent pas les coordonnées gelées, la pente $\mathbf{g}^\top\mathbf{d}$ de $f$ dans la direction $\mathbf{d}$ (M05b) est maximale pour $\mathbf{d} = \mathbf{P}_F\mathbf{g}/\lVert\mathbf{P}_F\mathbf{g}\rVert$.

*Démonstration.* Une telle direction vérifie $\mathbf{d} = \mathbf{P}_F\mathbf{d}$, donc $\mathbf{g}^\top\mathbf{d} = \mathbf{g}^\top\mathbf{P}_F\mathbf{d} = (\mathbf{P}_F\mathbf{g})^\top\mathbf{d}$ ($\mathbf{P}_F$ est symétrique) $\le \lVert\mathbf{P}_F\mathbf{g}\rVert\thinspace\lVert\mathbf{d}\rVert$ (Cauchy-Schwarz, M07), avec égalité quand $\mathbf{d}$ est dans la direction de $\mathbf{P}_F\mathbf{g}$. $\square$

Si le placement 2 est bloqué, la montée suit $\mathbf{P}_F\mathbf{g} = (4, 0, 8)$.

### Ce que trouve la montée

Dans trois cas, on sait d'avance où la montée arrive.

**Une forme linéaire** $f(\mathbf{x}) = \mathbf{w}^\top\mathbf{x}$. Sur la boule $\lVert\mathbf{x}\rVert \le r$, le maximum vaut $r\lVert\mathbf{w}\rVert$, atteint en $r\thinspace\mathbf{w}/\lVert\mathbf{w}\rVert$ (Cauchy-Schwarz ; M21 a fait la boule L∞). Sur le pavé $[0, 1]^n$, les termes $w_ix_i$ sont indépendants : $x_i = 1$ si $w_i > 0$, $x_i = 0$ si $w_i < 0$, un sommet. Pour l'épargnant : $(1, 0, 1)$ et 12 centaines d'euros sur le pavé. Si la seule contrainte était $\lVert\mathbf{x}\rVert \le 1$, ce serait $\big(\frac49, -\frac19, \frac89\big)$ et 9 centaines d'euros, avec une fraction négative, impossible ici.

**Une forme quadratique sur la sphère** $f(\mathbf{x}) = \mathbf{x}^\top\mathbf{A}\mathbf{x}$, $\mathbf{A}$ symétrique. Sur la sphère $\lVert\mathbf{x}\rVert = 1$, le maximum vaut $\lambda_{\max}$, atteint en un vecteur propre unitaire de $\lambda_{\max}$ (quotient de Rayleigh, M12c). C'est la forme qu'on obtient en moyennant des carrés de réponses linéaires : $\frac1m\sum_{k=1}^{m}(\mathbf{w}_k^\top\mathbf{x})^2 = \mathbf{x}^\top\mathbf{A}\mathbf{x}$ avec $\mathbf{A} = \frac1m\mathbf{W}^\top\mathbf{W}$, où $\mathbf{W}$ a pour lignes les $\mathbf{w}_k$. Deux capteurs de vibration lisent les réponses $z_1 = x_1 + 4x_2$ et $z_2 = 3x_1$ d'une excitation $\mathbf{x}$ de norme 1 :
```math
\tfrac12(z_1^2 + z_2^2) = 5x_1^2 + 4x_1x_2 + 8x_2^2 = \mathbf{x}^\top\mathbf{A}\mathbf{x}, \qquad \mathbf{A} = \begin{pmatrix} 5 & 2 \cr 2 & 8 \end{pmatrix} = \frac12\mathbf{W}^\top\mathbf{W}, \quad \mathbf{W} = \begin{pmatrix} 1 & 4 \cr 3 & 0 \end{pmatrix}.
```
Ses valeurs propres sont 9 et 4 (trace 13, déterminant 36), et le maximum, 9, est atteint en $\pm\frac{1}{\sqrt5}(1, 2)$ : $\mathbf{A}(1, 2) = (9, 18)$.

> **Propriété.** La montée de gradient sur $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ suivie d'une renormalisation, $\mathbf{y} = \mathbf{x}_t + \eta\cdot 2\mathbf{A}\mathbf{x} _t$ puis $\mathbf{x} _{t+1} = \mathbf{y}/\lVert\mathbf{y}\rVert$, est la **méthode de la puissance** (*power iteration*, M12c) pour la matrice $\mathbf{I} + 2\eta\mathbf{A}$.

En effet $\mathbf{y} = (\mathbf{I} + 2\eta\mathbf{A})\thinspace\mathbf{x} _t$. Si $\mathbf{A}$ est semi-définie positive, $\mathbf{I} + 2\eta\mathbf{A}$ a les mêmes vecteurs propres, de valeurs propres $1 + 2\eta\lambda_k > 0$, dont la plus grande est $1 + 2\eta\lambda _{\max}$ : les itérés convergent vers le vecteur propre dominant de $\mathbf{A}$ (si $\mathbf{x} _0$ ne lui est pas orthogonal), et le rapport des autres composantes à la sienne est multiplié à chaque pas par au plus $\frac{1 + 2\eta\lambda_2}{1 + 2\eta\lambda _{\max}}$. Pour les capteurs, avec $\eta = \frac14$, $\mathbf{I} + \frac12\mathbf{A}$ a pour valeurs propres $5{,}5$ et $3$ : un facteur $\frac{6}{11}$ par pas. Depuis $(1, 0)$ : $(3{,}5 ;\ 1)/\lVert\cdot\rVert \approx (0{,}962 ;\ 0{,}275)$, puis la suite tourne vers $\frac{1}{\sqrt5}(1, 2) \approx (0{,}447 ;\ 0{,}894)$. Un pas plus grand va plus vite : quand $\eta$ grandit, le facteur tend vers $\frac{4}{9}$, celui de la méthode de la puissance de $\mathbf{A}$.

**Une fonction convexe sur un pavé.**

> **Propriété** (∂ M28.9). Le maximum d'une fonction convexe sur un pavé est atteint en un sommet.

D'où des **coordonnées saturées** : une montée projetée sur une fonction convexe pousse les coordonnées contre les bornes. Mais pas forcément vers le meilleur sommet. Un drone, dans un hangar carré de 10 m de côté, $[0, 10]^2$, veut s'éloigner au plus d'une source de chaleur placée en $\mathbf{c} = (4, 6)$ : il maximise $f(\mathbf{x}) = \lVert\mathbf{x} - \mathbf{c}\rVert^2$, convexe. Aux sommets, $f$ vaut 72 m² en $(10, 0)$, 52 en $(0, 0)$ et en $(10, 10)$, 32 en $(0, 10)$. Le gradient $2(\mathbf{x} - \mathbf{c})$ éloigne chaque coordonnée de celle de $\mathbf{c}$ : une montée projetée finit au sommet de la région, délimitée par les droites $x_1 = 4$ et $x_2 = 6$, où elle part, et chaque sommet est un maximum local. Partie de $(3, 8)$, elle s'arrête en $(0, 10)$, le pire des quatre : 32 m² au lieu de 72.

![À gauche, le hangar [0, 10]² coloré selon ‖x − c‖², avec c = (4, 6) marqué d'une croix et les deux droites x₁ = 4 et x₂ = 6 en pointillés ; quatre montées projetées, une par région, partent d'un petit carré et finissent chacune au sommet de leur région, en glissant le long d'un bord une fois une coordonnée saturée ; les valeurs aux sommets sont 72 m² en (10, 0), 52 en (0, 0) et (10, 10), 32 en (0, 10). À droite, le cercle unité, les droites des vecteurs propres de A = [[5, 2], [2, 8]], (1, 2)/√5 pour λ = 9 et (2, −1)/√5 pour λ = 4, et les itérés de la montée renormalisée de pas 1/4, partis de x₀ = (1, 0), qui remontent le cercle vers (1, 2)/√5](figures/montee.png)

⚠️ **Erreur classique.** Couper le gradient au lieu du point (🐛 M28.17) : $\operatorname{clip}(\mathbf{g})$ ne garde pas $\mathbf{x}$ dans le pavé ; c'est le point obtenu après le pas qu'on projette. Garder un pas normalisé fixe et attendre qu'il s'arrête. Prendre le sommet atteint pour le maximum : c'est un maximum local.

🔗 **Dans workbookIA** — le chapitre 28 fait monter l'entrée d'un réseau dont les poids ne bougent plus, avec des contraintes sur cette entrée ; ce paragraphe étudie la montée, ses pas et ses contraintes sur des fonctions que l'on sait écrire.

## §4 · La variation totale d'une grille et les fréquences spatiales

### La variation totale d'une grille

Des mesures rangées sur une grille, les températures d'une plaque ou les altitudes d'un terrain : $x_{ij}$, ligne $i$, colonne $j$.

> **Définition.** La **variation totale** (*total variation*) d'une grille additionne les carrés des différences entre cases voisines, horizontales et verticales :
> $$\mathrm{VT}(\mathbf{x}) = \sum_{i,j}(x_{i+1,j} - x_{ij})^2 + \sum_{i,j}(x_{i,j+1} - x_{ij})^2 ,$$
> où l'on ne compte que les paires de cases voisines qui sont dans la grille. Pour un signal (une seule ligne), $\mathrm{VT}(\mathbf{x}) = \sum_j(x_{j+1} - x_j)^2$. La **variation totale en valeur absolue** remplace les carrés par des valeurs absolues (pour un signal, c'est la variation totale de Rudin, Osher et Fatemi ; sur une grille, ils additionnent plutôt, case par case, $\sqrt{a^2 + b^2}$ pour ses deux différences $a$ et $b$).

**Exemple : une plaque chauffée dans un coin.** Ses températures, en °C, sur une grille $2 \times 3$ :
```math
\mathbf{x} = \begin{pmatrix} 1 & 2 & 4 \cr 1 & 3 & 7 \end{pmatrix}.
```
Différences horizontales : 1 et 2 sur la première ligne, 2 et 4 sur la seconde, d'où $1 + 4 + 4 + 16 = 25$ ; verticales : 0, 1 et 3, d'où $0 + 1 + 9 = 10$. Donc $\mathrm{VT}(\mathbf{x}) = 35$.

### Une forme quadratique : le laplacien de la grille

Chaque paire de voisins est une arête $(a, b)$ d'un graphe, et $(x_a - x_b)^2 = x_a^2 + x_b^2 - 2x_ax_b$. En sommant sur les arêtes, chaque $x_a^2$ revient autant de fois que la case $a$ a de voisins, son **degré** $\deg a$.

> **Propriété.** $\mathrm{VT}(\mathbf{x}) = \mathbf{x}^\top\mathbf{L}\mathbf{x}$, où $\mathbf{L} = \mathbf{D} - \mathbf{A}$ est le **laplacien de la grille** (*graph Laplacian*) : $\mathbf{D}$ la matrice diagonale des degrés, $\mathbf{A}$ la matrice d'adjacence (1 entre deux voisins, 0 sinon). Ainsi
> $$(\mathbf{L}\mathbf{x})  _a = \deg(a)\thinspace x_a - \sum  _{b \text{ voisin de } a}x_b ,$$
> et pour une case intérieure, $(\mathbf{L}\mathbf{x})  _{ij} = 4x  _{ij} - x _{i-1,j} - x _{i+1,j} - x _{i,j-1} - x _{i,j+1}$ : le pochoir du laplacien discret de M21 (pour un pas de grille de 1), au signe près.

$\mathbf{L}$ est symétrique, semi-définie positive ($\mathbf{x}^\top\mathbf{L}\mathbf{x}$ est une somme de carrés), et son noyau est fait des grilles **constantes** : $\mathrm{VT}(\mathbf{x}) = 0$ si et seulement si tous les voisins sont égaux, et la grille est d'un seul tenant. Son gradient vaut $\nabla\mathrm{VT}(\mathbf{x}) = 2\mathbf{L}\mathbf{x}$ (M18). Pour la plaque :
```math
\mathbf{L}\mathbf{x} = \begin{pmatrix} -1 & -2 & -1 \cr -2 & -1 & 7 \end{pmatrix}
```
(par exemple, au coin chaud, $2 \times 7 - (4 + 3) = 7$). Vérifie : $\mathbf{x}^\top\mathbf{L}\mathbf{x} = -1 - 4 - 4 - 2 - 3 + 49 = 35$, et la somme des coefficients de $\mathbf{L}\mathbf{x}$ est nulle ($\mathbf{1}^\top\mathbf{L} = \mathbf{0}^\top$).

### Descendre sur la variation totale : lisser

Un pas de descente, $\mathbf{x} \leftarrow \mathbf{x} - \eta\cdot 2\mathbf{L}\mathbf{x}$, donne à une case intérieure la valeur $(1 - 8\eta)\thinspace x_{ij} + 2\eta\thinspace(x_{i-1,j} + x_{i+1,j} + x_{i,j-1} + x_{i,j+1})$ : pour $\eta \le \frac18$, une moyenne pondérée de la case et de ses voisines. C'est un pas de **diffusion** (*diffusion*) : la chaleur se répand vers les cases plus froides, et la moyenne ne change pas ($\mathbf{1}^\top\mathbf{L}\mathbf{x} = 0$). Pour la plaque, avec $\eta = 0{,}1$ :
```math
\mathbf{x} - 0{,}2\thinspace\mathbf{L}\mathbf{x} = \begin{pmatrix} 1{,}2 & 2{,}4 & 4{,}2 \cr 1{,}4 & 3{,}2 & 5{,}6 \end{pmatrix} :
```
le coin chaud passe de 7 à 5,6 °C, les autres cases se réchauffent, la moyenne reste 3 °C, et la variation totale tombe de 35 à 16,32.

> **Pas critique** (*critical step size*, M19). La hessienne de $\mathrm{VT}$ est $2\mathbf{L}$ : la descente est stable si et seulement si $\eta < \frac{2}{\lambda_{\max}(2\mathbf{L})} = \frac{1}{\lambda_{\max}(\mathbf{L})}$. Comme $\lambda_{\max}(\mathbf{L}) \le \lVert\mathbf{L}\rVert_\infty = 2\max_a\deg a$ (M22), $\lambda_{\max}(\mathbf{L}) \le 4$ pour un signal et $\le 8$ pour une grille. Pour la plaque, $\lambda_{\max}(\mathbf{L}) = 5$ (calcul numérique) : il faut $\eta < 0{,}2$. Au-delà, le motif le plus agité change de signe et grandit à chaque pas.

### Le carré ou la valeur absolue

Une marche de hauteur $h$, étalée régulièrement sur $n$ pas ($n$ différences égales à $\frac hn$), a une variation totale de $n\big(\frac hn\big)^2 = \frac{h^2}{n}$ : elle diminue quand $n$ grandit. Le carré **préfère les rampes** : un bord net ($n = 1$) lui coûte $h^2$, le plus cher, et le lisser l'étale. En valeur absolue, la même marche coûte $n \cdot \frac hn = h$ quel que soit $n$, et plus généralement $h$ pour tout chemin qui monte sans redescendre : la valeur absolue est indifférente à la forme de la montée, et **garde les bords** quand les mesures en montrent un.

![Un signal de 80 cases qui saute de 0 à 1 à la case 40, avec un bruit d'écart-type 0,12 (points gris) ; la marche sans bruit en pointillés. Lissé par la variation totale au carré, (I + τL)x = y avec τ = 6, il suit encore le bruit et monte de 0 à 1 en six cases environ : le bord est étalé. Lissé par la variation totale en valeur absolue, il est fait de paliers presque plats et saute de 0 à 1 en une ou deux cases : le bord est gardé](figures/marche_lissee.png)

**Remarque : débruiter** (*denoise*). Pour lisser des mesures $\mathbf{y}$, on peut minimiser $\lVert\mathbf{x} - \mathbf{y}\rVert^2 + \tau\thinspace\mathbf{x}^\top\mathbf{L}\mathbf{x}$ : le gradient $2(\mathbf{x} - \mathbf{y}) + 2\tau\mathbf{L}\mathbf{x}$ s'annule pour $(\mathbf{I} + \tau\mathbf{L})\thinspace\mathbf{x} = \mathbf{y}$, un système linéaire ; $\tau$ règle le compromis entre fidélité et douceur, comme le $\lambda$ de la ridge (M09b). En valeur absolue, il n'y a plus de formule : on minimise par un algorithme itératif, comme pour la figure.

### Motifs périodiques et fréquences

Une étoffe rayée est un motif répété ; on le relève sur une grille, une valeur par case. En dimension 1, $x_j = \cos(\omega j + \varphi)$ avec $\omega = 2\pi f$ : $f$ est la **fréquence spatiale** (*spatial frequency*), en cycles par case, $\frac1f$ la **période** (*period*), en cases, et $\varphi$ la **phase** (*phase*).

**Le repliement.** Avec une valeur par case, les fréquences $f$ et $f + 1$ donnent les mêmes échantillons ($2\pi j$ est un nombre entier de tours), et $f$ et $1 - f$ aussi, au signe de la phase près : $\cos(2\pi(1 - f)j + \varphi) = \cos(2\pi fj - \varphi)$. Toute fréquence se ramène ainsi dans $[0, \frac12]$. Un motif de fréquence $\frac56$, relevé une fois par case, ne se distingue pas d'un motif de période 6 : c'est le **repliement** (*aliasing*). La plus haute fréquence visible est $\frac12$, l'alternance $(+1, -1, +1, \ldots)$, de période 2 cases : c'est la **fréquence de Nyquist** (*Nyquist frequency*). Un motif n'est relevé sans repli que si sa période dépasse 2 cases : plus de deux valeurs par période.

**En dimension 2**, $x_{ij} = \cos(2\pi(f_1i + f_2j) + \varphi)$ est constant le long des droites $f_1i + f_2j = $ constante : des rayures perpendiculaires à $(f_1, f_2)$, de période $1/\sqrt{f_1^2 + f_2^2}$ dans cette direction. Pour $(f_1, f_2) = (0{,}15 ;\ 0{,}2)$ : une période de $1/0{,}25 = 4$ cases, dans la direction $\frac15(3, 4)$. La plus haute fréquence, $(\frac12, \frac12)$, donne $x_{ij} = \cos(\pi(i + j)) = (-1)^{i+j}$ : le **damier** (*checkerboard*).

### Un motif périodique est un vecteur propre du laplacien

Pour éviter les bords, refermons le signal en un anneau de $n$ cases, la case $n - 1$ voisine de la case 0 : $(\mathbf{L}\mathbf{x}) _j = 2x_j - x  _{j-1} - x _{j+1}$, indices modulo $n$, une matrice circulante (M21).

> **Propriété.** Si $\omega = \frac{2\pi k}{n}$ (le motif fait exactement $k$ tours sur l'anneau), $x_j = \cos(\omega j + \varphi)$ vérifie
> $$\mathbf{L}\mathbf{x} = 4\sin^2\frac\omega2\mkern5mu \mathbf{x}, \qquad \text{donc}\qquad \frac{\mathrm{VT}(\mathbf{x})}{\lVert\mathbf{x}\rVert^2} = 4\sin^2\frac\omega2 .$$

*Démonstration.* Les formules de soustraction de M25a §8, avec $b$ puis $-b$ ($\cos$ est paire et $\sin$ impaire, R9), donnent $\cos(a - b) + \cos(a + b) = 2\cos a\cos b$, donc $x_{j-1} + x_{j+1} = 2\cos\omega\mkern5mu  x_j$, y compris aux deux bouts de l'anneau puisque le motif est de période $n$. Ainsi $(\mathbf{L}\mathbf{x})_j = (2 - 2\cos\omega)\thinspace x_j$, et $1 - \cos\omega = 2\sin^2\frac\omega2$ (la même formule, avec $\frac\omega2$ et $-\frac\omega2$). $\square$

M21 (💻 du §4) a annoncé que toutes les matrices circulantes ont les mêmes vecteurs propres ; ces cosinus en sont des versions réelles, pour le laplacien. Le rapport variation totale / énergie est un quotient de Rayleigh de $\mathbf{L}$ (M12c) : environ $\omega^2$ pour un motif lent, et maximal, égal à 4, à la fréquence de Nyquist (sur un anneau de longueur paire). Sur une grille refermée dans les deux directions, $\cos(\omega_1i + \omega_2j + \varphi)$ est un vecteur propre de valeur propre $4\sin^2\frac{\omega_1}{2} + 4\sin^2\frac{\omega_2}{2}$, au plus 8, pour le damier. Sur une grille à bords libres, la relation reste exacte aux cases qui ne touchent pas le bord, mais pas sur le bord : le rapport n'est plus qu'approché, d'autant mieux que la grille est grande. Des rayures de période 8 le long des lignes ont un rapport $4\sin^2\frac\pi8 = 2 - \sqrt2 \approx 0{,}586$ ; les rayures obliques $(0{,}15 ;\ 0{,}2)$, $4\sin^2(0{,}15\pi) + 4\sin^2(0{,}2\pi) \approx 0{,}824 + 1{,}382 \approx 2{,}21$, plus que des rayures de même période 4 alignées sur un axe ($4\sin^2\frac\pi4 = 2$) : la variation totale ne regarde que les différences horizontales et verticales, et ne traite pas toutes les directions de la même façon.

![À gauche, quatre motifs de 16 × 16 cases, découpés dans une grille refermée de 40 × 40 : des rayures verticales de fréquence (0 ; 0,125), soit une période de 8 cases (rapport variation totale / énergie 0,586), d'autres de fréquence (0 ; 0,2), une période de 5 cases (1,382), des rayures obliques (0,15 ; 0,2), une période de 4 cases (2,206), et le damier (0,5 ; 0,5) (8,000). À droite, la carte de 4 sin²(πf₁) + 4 sin²(πf₂) sur le carré des fréquences [0, ½]², claire près de (0, 0) et sombre vers (½, ½), avec les quatre motifs placés dessus](figures/motifs_raies.png)

Un pas de descente sur la variation totale multiplie un tel motif par $1 - 2\eta \cdot 4\sin^2\frac\omega2 = 1 - 8\eta\sin^2\frac\omega2$ : les motifs rapides perdent le plus, la diffusion est un **filtre passe-bas** (*low-pass filter*). Son pas critique se lit à la fréquence de Nyquist, $\lvert 1 - 8\eta\rvert < 1$, soit $\eta < \frac14$ sur un anneau de longueur paire. Et le débruitage $(\mathbf{I} + \tau\mathbf{L})\mathbf{x} = \mathbf{y}$ divise chaque motif par $1 + 4\tau\sin^2\frac\omega2$.

### Le gain d'un flou

La moyenne mobile de trois cases (R5, M21), $y_j = \frac13(x_{j-1} + x_j + x_{j+1})$, transforme le motif, par la même formule d'addition, en
$$y_j = \frac{1 + 2\cos\omega}{3}\mkern5mu  x_j .$$
Ce facteur est son **gain** (*gain*) : 1 pour $\omega = 0$ (les constantes passent), 0 pour $\omega = \frac{2\pi}{3}$ (la période 3 est **effacée**), $-\frac13$ à la fréquence de Nyquist (l'alternance revient inversée et divisée par 3). Elle aussi est un **filtre passe-bas** : son gain vaut 1 pour les constantes et reste au plus $\frac13$ en valeur absolue au-delà de la période 3. Pour la période 8, $\frac{1 + \sqrt2}{3} \approx 0{,}805$. Un **flou** (*blur*) $3 \times 3$ (la moyenne des neuf cases autour) est une moyenne mobile le long des lignes puis le long des colonnes : il multiplie $\cos(\omega_1i + \omega_2j + \varphi)$ par le produit des deux gains, et le damier par $\frac19$.

![À gauche, le gain (1 + 2 cos ω)/3 de la moyenne mobile de trois cases, en fonction de la fréquence f de 0 à ½ : il part de 1, vaut environ 0,805 pour la période 8, s'annule pour la période 3 (f = 1/3) et finit à −1/3 en f = ½. À droite, un signal refermé de 48 cases, somme d'un motif de période 24 et d'un motif de période 3 d'amplitude 0,5 (en gris, en dents de scie) ; sa moyenne mobile se confond avec 0,977 fois le seul motif de période 24 : la période 3 a disparu](figures/gain_moyenne.png)

💻 **Aujourd'hui en pratique** — pour connaître les fréquences d'un signal ou d'une grille quelconque, on le décompose en motifs cosinus et sinus de toutes les fréquences $\frac kn$ : c'est la **transformée de Fourier discrète** (*discrete Fourier transform*), que la FFT calcule en $n\log n$ opérations environ (`np.fft.fft`, `np.fft.fft2`, et `np.fft.fftfreq` pour les fréquences en cycles par case). Un filtre circulaire y devient une multiplication, fréquence par fréquence, par son gain (M21).

⚠️ **Erreur classique.** Mettre $f$ (en cycles par case) dans $4\sin^2\frac\omega2$, qui attend $\omega = 2\pi f$ en radians par case. Prendre $\frac{1}{f_1}$, ou $\frac{1}{f_1} + \frac{1}{f_2}$, pour la période d'un motif en dimension 2 : c'est $1/\sqrt{f_1^2 + f_2^2}$. Lire une fréquence au-dessus de $\frac12$ sans la replier en $1 - f$. Oublier de dire « en valeur absolue » quand ce n'est pas la somme des carrés.

🔗 **Dans workbookIA** — le chapitre 28 parle de motifs de haute fréquence et ajoute une variation totale pour les atténuer ; ce paragraphe donne le sens précis de ces mots, et dit ce que laisse passer un flou.

## §5 · Modifier une loi catégorielle : température, top-k, top-p, et le coût d'une troncature

### Une loi, avant le tirage

Dans toute cette section, une loi est un vecteur de probabilités. Les transformations qui suivent fabriquent une **nouvelle loi**, qui sert ensuite à un tirage catégoriel, par inversion de la fonction de répartition (M02b). Rien ici ne tire au hasard.

À l'écoute d'un chant, un ornithologue hésite entre six espèces, numérotées de 0 à 5 (0 le rouge-gorge, 1 le pinson, 2 le rossignol, 3 la mésange, 4 la fauvette, 5 le merle), et donne son avis sous forme de probabilités :
$$\mathbf{p} = (0{,}11 ;\ 0{,}28 ;\ 0{,}07 ;\ 0{,}24 ;\ 0{,}09 ;\ 0{,}21).$$

### La température

> **Définition.** La loi $\mathbf{p}$ à la **température** (*temperature*) $T > 0$ est la **loi tempérée** (*tempered distribution*)
> $$p_i^{(T)} = \frac{p_i^{1/T}}{\sum_jp_j^{1/T}} .$$

> **Propriétés.**
> - C'est la loi de Boltzmann (M17) des énergies $E_i = -\ln p_i$ : $e^{-E_i/T} = p_i^{1/T}$. $T = 1$ redonne $\mathbf{p}$.
> - Les rapports sont élevés à la puissance $\frac1T$ : $p_i^{(T)}/p_j^{(T)} = (p_i/p_j)^{1/T}$. L'ordre des issues ne change donc jamais, et une issue de probabilité nulle (d'énergie infinie) garde une probabilité nulle.
> - Quand $T \to 0$, la loi tend vers la loi uniforme sur les issues les plus probables ; quand $T \to \infty$, vers la loi uniforme sur les issues de probabilité **non nulle**, pas sur toutes (M17 : pour $0 < p_i < p_j$, $(p_i/p_j)^{1/T}$ tend vers 0 quand $T \to 0$ et vers 1 quand $T \to \infty$).
> - L'**entropie** $H(\mathbf{p}^{(T)})$ croît avec $T$ (énoncé) : $\frac{\mathrm{d}H}{\mathrm{d}T} = \frac{\mathbb{V}(E)}{T^3} \ge 0$, où $\mathbb{V}(E)$ est la variance des énergies sous $\mathbf{p}^{(T)}$ ; elle est constante seulement si $\mathbf{p}$ est uniforme sur son support (ses issues de probabilité non nulle).

**Exemple : refroidir l'avis de l'ornithologue.** À $T = \frac14$, on élève à la puissance 4 : $0{,}11^4 \approx 0{,}000\thinspace146$, $0{,}28^4 \approx 0{,}006\thinspace147$, $0{,}07^4 \approx 0{,}000\thinspace024$, $0{,}24^4 \approx 0{,}003\thinspace318$, $0{,}09^4 \approx 0{,}000\thinspace066$, $0{,}21^4 \approx 0{,}001\thinspace945$, de somme $\approx 0{,}011\thinspace645$, d'où
$$\mathbf{p}^{(1/4)} \approx (0{,}013 ;\ 0{,}528 ;\ 0{,}002 ;\ 0{,}285 ;\ 0{,}006 ;\ 0{,}167).$$
Le rapport pinson/mésange, $\frac{0{,}28}{0{,}24} = \frac76$, devient $\big(\frac76\big)^4 \approx 1{,}85$. À $T = 4$ (des racines quatrièmes), $\mathbf{p}^{(4)} \approx (0{,}154 ;\ 0{,}194 ;\ 0{,}137 ;\ 0{,}187 ;\ 0{,}146 ;\ 0{,}181)$. L'entropie vaut $1{,}091$ nat à $T = \frac14$, $1{,}672$ à $T = 1$, $1{,}783$ à $T = 4$, et tend vers $\ln 6 \approx 1{,}792$.

![À gauche, les probabilités des six espèces (0 rouge-gorge, 1 pinson, 2 rossignol, 3 mésange, 4 fauvette, 5 merle) à quatre températures, en barres groupées : à T = 1/4, le pinson prend 0,528 et la mésange 0,285, le rossignol presque rien ; à T = 1, l'avis de départ ; à T = 4, des barres entre 0,137 et 0,194 ; à T = ∞, 1/6 partout. À droite, l'entropie en fonction de T, sur une échelle logarithmique de 0,025 à 100 : elle part de 0, croît, vaut 1,091 à T = 1/4, 1,672 à T = 1 et 1,783 à T = 4, et approche ln 6 ≈ 1,792](figures/temperature.png)

workbookIA applique la température à des scores, avant la softmax ; le 🔗 M28.11 montre que c'est la même loi.

### Tronquer, c'est conditionner

Tronquer (*truncation*) une loi, c'est garder un ensemble $S$ d'issues et y redistribuer la probabilité :
$$p_{S,i} = \frac{p_i}{P(S)} \ \text{ si } i \in S, \qquad p_{S,i} = 0 \ \text{ sinon}, \qquad P(S) = \sum_{i \in S}p_i :$$
c'est la **loi conditionnelle** sachant l'événement $S$ (M03). Deux choix de $S$ :
- le **top-k** (*top-k sampling*) garde les $k$ issues les plus probables (entre deux probabilités égales, la plus petite issue d'abord) ;
- le **top-p** (*nucleus sampling*, Holtzman et coll.) fixe un seuil $m$ et prend les issues dans le même ordre, une à une, jusqu'à ce que leur masse $P(S)$ atteigne $m$.

> **Propriété** (∂ M28.10). L'ensemble $S$ du top-p a le moins d'issues possible : aucun ensemble qui en a moins n'atteint la masse $m$, et parmi ceux qui en ont autant, aucun n'a une masse plus grande. Ce n'est pas toujours le seul de sa taille à atteindre $m$. C'est l'ensemble que rend `smallest_mass_set(p, m)` (🔨 M28.14), un plus petit ensemble de masse au moins $m$ (*highest-probability set*).

Le top-4 de l'ornithologue garde les espèces 1, 3, 5 et 0, de probabilités 0,28, 0,24, 0,21 et 0,11 : $S = \lbrace0, 1, 3, 5\rbrace$.

**Exemple : un top-p.** Devant une voiture qui ne démarre pas, l'outil de diagnostic d'un garagiste donne cinq causes possibles, numérotées de 0 à 4 (0 le démarreur, 1 la batterie, 2 le carburant, 3 l'allumage, 4 l'électronique), avec les probabilités
$$\mathbf{p} = (0{,}05 ;\ 0{,}37 ;\ 0{,}12 ;\ 0{,}27 ;\ 0{,}19).$$
L'ordre est 1 (0,37), 3 (0,27), 4 (0,19), 2 (0,12), 0 (0,05), de probabilités cumulées 0,37 ; 0,64 ; 0,83 ; 0,95 ; 1. Le top-p de seuil $m = 0{,}7$ garde $S = \lbrace1, 3, 4\rbrace$ : $0{,}64 < 0{,}7 \le 0{,}83$. Il en faut trois, puisque deux causes pèsent au plus $0{,}64$ ; mais $\lbrace1, 2, 3\rbrace$, de masse $0{,}76$, atteint aussi le seuil avec trois causes : le nombre minimal d'issues est unique, l'ensemble ne l'est pas toujours. La loi tronquée est
$$\mathbf{p}_S = \Big(0 ;\ \frac{37}{83} ;\ 0 ;\ \frac{27}{83} ;\ \frac{19}{83}\Big).$$

### Température et troncatures

> **Propriété** (énoncé). Pour $0 < T < \infty$, l'ensemble du top-k ne dépend pas de $T$ (l'ordre des issues ne change pas). Refroidir ne fait jamais baisser, pour aucun $j$, la masse des $j$ issues les plus probables : l'ensemble du top-p **rétrécit** quand $T$ baisse et grandit quand $T$ monte, au sens large : il peut aussi garder sa taille.

Pour l'ornithologue, avec $m = 0{,}7$ : à $T = \frac14$, le pinson et la mésange suffisent ($0{,}528$, puis $0{,}813$ à deux) ; à $T = 1$, il faut trois espèces ($0{,}52$ à deux, $0{,}73$ à trois) ; à $T = 4$, quatre ($0{,}562$ à trois, $0{,}716$ à quatre). Le top-4 reste $\lbrace0, 1, 3, 5\rbrace$ à toute température $0 < T < \infty$. À la limite $T = \infty$, les six espèces ont la même probabilité, et c'est la règle « la plus petite issue d'abord » qui décide : $\lbrace0, 1, 2, 3\rbrace$.

![Trois panneaux, un par température (1/4, 1 et 4), avec les six espèces triées par probabilité décroissante (1 pinson, 3 mésange, 5 merle, 0 rouge-gorge, 4 fauvette, 2 rossignol) en barres, la probabilité cumulée en escalier et le seuil m = 0,7 en tirets. À T = 1/4, le cumul passe de 0,528 à 0,813 à la deuxième : deux espèces gardées. À T = 1, de 0,52 à 0,73 à la troisième : trois espèces. À T = 4, de 0,562 à 0,716 à la quatrième : quatre espèces. Les barres gardées sont en couleur, les autres en gris](figures/top_p.png)

### Le coût d'une troncature

> **Propriété** (∂ M28.10). $\mathrm{KL}(\mathbf{p}_S \thinspace\Vert\thinspace \mathbf{p}) = -\ln P(S)$ et $\frac12\lVert\mathbf{p}_S - \mathbf{p}\rVert_1 = 1 - P(S)$. Dans l'autre sens, $\mathrm{KL}(\mathbf{p} \thinspace\Vert\thinspace \mathbf{p}_S) = +\infty$ dès que $S$ laisse de côté une issue de probabilité non nulle (M06 : le support de $\mathbf{p}_S$ ne couvre plus celui de $\mathbf{p}$).

Pour le top-p du diagnostic : $\mathrm{KL}(\mathbf{p}_S \thinspace\Vert\thinspace \mathbf{p}) = -\ln 0{,}83 \approx 0{,}186$ nat, et $\frac12\lVert\mathbf{p}_S - \mathbf{p}\rVert_1 = 0{,}17$. Un top-p de seuil $m$ garde une masse $P(S) \ge m$ : quelle que soit la loi, sa troncature coûte au plus $-\ln m$ en divergence KL ($\approx 0{,}357$ nat pour $m = 0{,}7$), et au plus $1 - m$ en demi-norme L1.

⚠️ **Erreur classique.** Confondre deux « variations totales ». Celle d'une grille (§4) additionne des carrés de différences entre cases voisines. La **distance en variation totale** (*total variation distance*) entre deux lois, $\frac12\lVert\mathbf{p} - \mathbf{q}\rVert_1 = \frac12\sum_i\lvert p_i - q_i\rvert$, est la plus grande différence de probabilité que les deux lois donnent à un même événement. Elles n'ont en commun que le nom. Autres pièges : multiplier les probabilités par $\frac1T$ au lieu de les élever à cette puissance ; croire que $T \to \infty$ donne l'uniforme sur toutes les issues ; écrire $\mathrm{KL}(\mathbf{p} \thinspace\Vert\thinspace \mathbf{p}_S)$, infinie, pour le coût d'une troncature.

🔗 **Dans workbookIA** — le chapitre 28 génère du texte avec une température, un top-k ou un top-p ; ce paragraphe étudie, sur des probabilités et sans mots, les lois que ces réglages préparent avant le tirage.

## §6 · Une itération déterministe sur un ensemble fini finit par boucler

### Une suite qui revient sur ses pas

Partons de $u_0 = 15$ et remplaçons chaque nombre par la somme des carrés de ses chiffres : $1 + 25 = 26$, puis $4 + 36 = 40$, puis 16, et ainsi de suite :
$$15,\ 26,\ 40,\ 16,\ 37,\ 58,\ 89,\ 145,\ 42,\ 20,\ 4,\ 16,\ 37, \ldots$$
À partir de $u_3 = 16$, les huit valeurs 16, 37, 58, 89, 145, 42, 20, 4 reviennent sans fin. C'était inévitable : un nombre d'au plus trois chiffres donne au plus $3 \times 81 = 243$, donc la suite reste dans $E = \lbrace1, \ldots, 999\rbrace$, un ensemble fini, et chaque terme est déterminé par le précédent.

> **Définition.** Une suite $u_{t+1} = f(u_t)$ est **ultimement périodique** (*eventually periodic*) s'il existe $\mu \ge 0$ et $\lambda \ge 1$ tels que $u_{t+\lambda} = u_t$ pour tout $t \ge \mu$. Les plus petits sont la **prépériode** $\mu$ (*preperiod*, la longueur de la queue) et la **période** $\lambda$ (la longueur du cycle, *cycle length*).

Ici $\mu = 3$ (15, 26 et 40 ne reviennent jamais) et $\lambda = 8$. Le dessin a la forme d'un $\rho$.

![Le parcours de la suite partie de 15 : une queue de trois nombres (15, 26, 40) monte jusqu'à 16, puis un cycle de huit nombres (16, 37, 58, 89, 145, 42, 20, 4) dessiné en cercle revient à 16 : la forme d'un ρ, avec la prépériode μ = 3 et la période λ = 8. En gris, deux autres queues rejoignent le même cycle : 3, 9, 81, 65, 61 entre en 37, et 11, 2 entre en 4](figures/rho.png)

> **Théorème.** Soit $E$ un ensemble fini à $N$ éléments et $f : E \to E$. Toute suite $u_{t+1} = f(u_t)$ est ultimement périodique, et $\mu + \lambda \le N$.

*Démonstration.* Les $N + 1$ termes $u_0, \ldots, u_N$ prennent leurs valeurs dans $E$, qui en a $N$ : deux sont égaux (principe des tiroirs, M16). Soit $j$ le premier indice dont la valeur est déjà apparue : $u_j = u_i$ avec $i < j$, et $u_0, \ldots, u_{j-1}$ sont deux à deux distincts ; donc $j \le N$. Comme $f$ est une fonction, $u_i = u_j$ entraîne $u_{i+1} = f(u_i) = f(u_j) = u_{j+1}$, et par récurrence $u_{i+t} = u_{j+t}$ pour tout $t \ge 0$ : à partir de l'indice $i$, la suite est périodique de période $j - i$. Elle ne prend plus alors que les valeurs $u_i, \ldots, u_{j-1}$, et $u_0, \ldots, u_{i-1}$, distinctes de celles-là, ne reviennent jamais : la prépériode vaut $i$. Aucune période plus courte que $j - i$ n'est possible, puisque $u_i, \ldots, u_{j-1}$ sont distincts. Donc $\mu = i$, $\lambda = j - i$ et $\mu + \lambda = j \le N$. $\square$

Pour 15 : $j = 11$ ($u_{11} = 16 = u_3$), $i = 3$, et $\mu + \lambda = 11 \le 999$. La borne dit seulement que la boucle arrive au plus tard au terme $N$.

**Si $f$ est une bijection de $E$, $\mu = 0$** : chaque valeur a un seul antécédent, donc $u_i = u_j$ avec $i \ge 1$ entraîne $u_{i-1} = u_{j-1}$, et la première répétition ne peut concerner que $u_0$. Exemple : un automate écrit des 0 et des 1, chaque nouveau symbole étant la somme modulo 2 du premier et du deuxième des trois derniers, $s_{t+3} = (s_t + s_{t+1}) \bmod 2$. Son **état**, les trois derniers symboles, vit dans un ensemble de $2^3 = 8$ éléments, et le passage d'un état au suivant est une bijection (on retrouve le symbole oublié par $s_t = (s_{t+3} + s_{t+1}) \bmod 2$). Depuis 0, 0, 1, il écrit $0, 0, 1, 0, 1, 1, 1, 0, 0, 1, \ldots$ : une période de 7, sans queue. L'état 000 est un point fixe, et les sept autres forment un seul cycle.

### Un générateur glouton boucle

Un générateur **glouton** (*greedy decoding*) écrit des symboles d'un alphabet de $V$ symboles. Son état est fait des $w$ derniers symboles écrits, et à chaque pas il écrit le symbole le plus probable sachant cet état : une règle déterministe. Les états forment un ensemble d'au plus $V^w$ éléments, et l'état suivant ne dépend que de l'état présent : d'après le théorème, la suite des symboles écrits devient périodique, avec $\mu + \lambda \le V^w$. Avec 4 symboles et un contexte de 5, il s'est mis à se répéter au bout de $4^5 = 1\thinspace024$ symboles au plus.

Deux limites. Si le symbole suivant est **tiré au hasard** (§5), l'état suit une chaîne de Markov (M26) : rien n'oblige plus à boucler. Et un modèle dont l'état est un vecteur de nombres réels (une cellule récurrente) n'est pas une fonction sur un ensemble fini : le théorème n'en dit rien (en nombres flottants, l'ensemble des états est fini, mais si grand que la borne $N$ ne sert à rien). Si un tel modèle boucle, c'est pour une autre raison.

💻 **Aujourd'hui en pratique** — pour trouver $\mu$ et $\lambda$ (*cycle detection*) sans garder tous les termes, on utilise l'algorithme du **lièvre et de la tortue** (*tortoise and hare*) de R. W. Floyd (Knuth, TAOCP vol. 2, §3.1, exercice 6). La tortue calcule $u_t$, le lièvre $u_{2t}$, jusqu'au premier $t \ge 1$ où $u_t = u_{2t}$ ; ce $t$ est un multiple de $\lambda$ compris entre $\mu$ et $\mu + \lambda$. On repart alors de $u_0$ et de $u_t$, au même pas : les deux suites se rencontrent pour la première fois à l'indice $\mu$. Un tour de cycle donne ensuite $\lambda$. Deux valeurs en mémoire suffisent. Pour 15 : $u_8 = u_{16} = 42$, puis $u_3 = u_{11} = 16$, d'où $\mu = 3$, et un tour de huit pas ramène à 16.

⚠️ **Erreur classique.** Compter la prépériode dans la période (🐛 M28.17) : la période est la longueur du cycle, $j - i$, et non l'indice $j$ de la première répétition. Croire qu'une longue période veut dire « pas de répétition ». Appliquer le théorème à un état continu, ou à un choix tiré au hasard.

🔗 **Dans workbookIA** — le chapitre 28 constate qu'un décodage glouton tourne en boucle ; ce paragraphe démontre que c'est inévitable pour un générateur déterministe à état fini, et dit pourquoi le théorème ne couvre pas un réseau récurrent.

## Les pièges classiques ⚠️ (récapitulatif)

- **Gram** : $\mathbf{X}\mathbf{X}^\top$ pour les lignes, $\mathbf{X}^\top\mathbf{X}$ pour les colonnes ; diviser par le nombre d'**échantillons** ; former la plus petite.
- **Double centrage** : sur les **carrés** des distances ; il donne la matrice de Gram des points centrés ; comparer des distances, pas des coordonnées.
- **Montée** : couper le point, pas le gradient ; un pas normalisé fixe ne s'arrête pas ; un sommet atteint n'est qu'un maximum local.
- **Variation totale** : une somme de carrés, qui étale les bords ; la valeur absolue les garde, et se nomme.
- **Fréquences** : $\omega = 2\pi f$ dans $4\sin^2\frac\omega2$ ; période $1/\sqrt{f_1^2 + f_2^2}$ en dimension 2 ; au-delà de $\frac12$, la fréquence se replie.
- **Lois** : la puissance $\frac1T$ ; $T \to \infty$ donne l'uniforme sur le support ; le coût d'une troncature est $\mathrm{KL}(\mathbf{p}_S \thinspace\Vert\thinspace \mathbf{p}) = -\ln P(S)$ ; la distance en variation totale entre lois n'est pas la variation totale d'une grille.
- **Boucles** : la période est la longueur du cycle, sans la queue ; il faut un état fini et une règle déterministe.

## Et maintenant

**Dans ce dépôt** : l'examen blanc CP6 reprend toute la partie VI. La partie VII commence avec MB2, qui retrouvera des produits scalaires entre vecteurs et une approximation de rang faible.

**Dans workbookIA** : le chapitre 28 visualise ce que voient les réseaux en faisant monter leur entrée, transfère un style avec des matrices de Gram et une variation totale, et génère du texte avec une température, un top-k ou un top-p. Plus loin, les bonus B3 et B4 reparleront de température, de top-k et de top-p.

## Pour aller plus loin

- I. Borg et P. J. F. Groenen, *Modern Multidimensional Scaling: Theory and Applications* (2ᵉ éd., Springer, 2005, collection *Springer Series in Statistics*) : ch. 12 (*Classical Scaling*), le double centrage et le positionnement multidimensionnel classique.
- L. I. Rudin, S. Osher et E. Fatemi, « Nonlinear total variation based noise removal algorithms », *Physica D: Nonlinear Phenomena*, vol. 60, 1992 : la variation totale en valeur absolue, pour débruiter.
- A. Holtzman, J. Buys, L. Du, M. Forbes et Y. Choi, « The Curious Case of Neural Text Degeneration », ICLR 2020 (version gratuite sur arXiv, 1904.09751) : le top-p.
- D. E. Knuth, *The Art of Computer Programming*, vol. 2, *Seminumerical Algorithms* (3ᵉ éd., Addison-Wesley, 1997), §3.1, exercice 6 : les suites ultimement périodiques sur un ensemble fini et l'algorithme de Floyd.
- `annexes/symboles.md`, `annexes/formulaire.md` et `annexes/erreurs_frequentes.md`.
