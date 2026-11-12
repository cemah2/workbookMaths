# M22 · Récurrences vectorielles, rayon spectral et normes de matrices — fiche de cours

> Des étudiants qui passent d'une année à l'autre, une population qui reçoit des arrivants, un lac qui reçoit des rejets : à chaque pas, un **état** est transformé par une même matrice, et une **entrée** s'y ajoute. Ce chapitre résout ces **récurrences linéaires avec entrée** : la solution s'écrit avec les **puissances** de la matrice, et la sortie est la **convolution** de l'entrée par une **réponse impulsionnelle** (M21). Il étudie ensuite ces puissances : les **valeurs propres complexes** et la **forme exponentielle** $r\,e^{i\theta}$, qui font tourner et grandir ou rétrécir ; le **rayon spectral**, qui décide si $\mathbf{A}^t$ tend vers 0 ; la **croissance transitoire** des matrices **non normales**, qui grandissent d'abord. Il mesure une matrice par ses **normes induites**, **sous-multiplicatives** et toujours au moins égales au rayon spectral, et s'en sert pour majorer des **produits de matrices différentes**, des produits de **facteurs dans [0, 1]** et des **produits de jacobiennes** le long de la trajectoire d'une récurrence non linéaire. Il finit par deux outils : la **sensibilité** de l'état final à un paramètre utilisé à chaque pas, une **somme sur le temps**, et la façon de ramener sous un seuil un vecteur fait de **plusieurs blocs**. Les exemples viennent des populations, des lacs, de la pêche, de la mécanique et de la géométrie du plan ; le chapitre 22 de workbookIA appliquera ces outils aux réseaux récurrents.

| | |
|---|---|
| **Sections** | §1 à §8 |
| **Temps total estimé** | ≈ 13,5 h : lecture et calculs de la fiche ≈ 2 h 40, exercices ≈ 10 h 05, 22 flashcards ≈ 45 min (parcours essentiel ≈ 10,4 h) |
| **Prérequis** | R4 (récurrence, notations $\Sigma$ et $\Pi$) ; R5 (suites géométriques, récurrence affine) ; R6 (exponentielle, ln, demi-vie) ; M12c (valeurs propres, diagonalisation, puissances, le strict minimum sur les nombres complexes) ; M19 (itérations linéaires et rayon spectral d'une matrice symétrique, module des racines et forme trigonométrique, projection sur une boule) ; M12d (valeurs singulières, normes spectrale et de Frobenius) ; M07 (normes L1, L2 et L∞) ; M09a (produit de Hadamard) ; M12b (matrices orthogonales) ; M17 (jacobienne, règle de la chaîne) ; M18 (somme sur les chemins) ; M20 (produits de jacobiennes proches de l'identité) ; M21 (convolution de deux suites) ; M02c (loi des grands nombres) ; M06 (inégalité de Jensen) ; M14 ($(1 + x/n)^n \to e^x$) ; M16 (espérance d'un produit, variances multipliées d'étage en étage) |
| **Fichiers du chapitre** | `02_exercices.md` (quiz, papier) · `03_notebook.ipynb` · `04_indices.md` · `05_solutions.md` et `05_solutions.ipynb` · `06_mes_reponses.md` · `flashcards.csv` |
| **mymath** | `recurrence.py` : `linear_system_states`, `operator_norm`, `product_norms` |
| **MML** | §4.2 (*Eigenvalues and Eigenvectors*), relu ; sa figure 4.4 |

## Comment utiliser ce chapitre

**Ordre conseillé.**
1. `python tools/start_chapter.py M22` (sur Colab : `00_setup/COLAB.md` §2) : il copie le notebook, ta feuille de réponses et le squelette `mymath/recurrence.py`.
2. Section par section : lis **crayon en main**, refais chaque calcul ; puis fais les exercices de la section, quiz 🧠 d'abord.
3. Les exercices ✏️ et 🔗 se font sur papier, dans ta copie de `06_mes_reponses.md`, puis se vérifient dans la **partie 0** du notebook. Les démonstrations ∂ se rédigent dans ta copie et se jugent avec la grille de relecture de `05_solutions.md`.

Les §1 et §2 forment le socle (résoudre une récurrence, calculer des puissances) ; les §3 et §4 comparent deux mesures d'une matrice, le rayon spectral, qui dit le long terme, et les normes induites, qui bornent chaque pas ; les §5 à §7 passent aux produits de matrices différentes (des facteurs dans [0, 1], des jacobiennes, une somme sur le temps) ; le §8 est un outil court, qui ne demande que M07 et M19 §8.

| Section | Quiz 🧠 et rappels 🔁 | Papier et réflexion | Notebook |
|---|---|---|---|
| §1 Récurrences linéaires avec entrée | Q1 | M22.1 ✏️, M22.2 ✏️, M22.16 🔗 | M22.19 🔨 |
| §2 Puissances, valeurs propres complexes, rotations | Q2, R1 | M22.3 ✏️, M22.17 📖 | M22.25 🎨 |
| §3 Le rayon spectral et la croissance transitoire | Q3 | M22.4 ✏️, M22.5 ✏️, M22.13 ∂, M22.17 📖, M22.18 🗣️, M22.E1 💼, M22.E2 💼 | M22.22 📦, M22.23 🔮, M22.26 🐛, M22.28 🏆 |
| §4 Normes induites | Q4, R2 | M22.6 ✏️, M22.11 ∂, M22.12 ∂, M22.E1 💼 | M22.20 🔨, M22.22 📦, M22.27 🛠️ |
| §5 Produits de matrices, facteurs dans [0, 1] | Q5 | M22.7 ✏️ | M22.21 🔨, M22.24 🔬 |
| §6 Produits de jacobiennes | Q6, R3 | M22.8 ✏️, M22.14 ∂, M22.16 🔗 | M22.21 🔨, M22.26 🐛 |
| §7 Une somme sur le temps | Q7 | M22.9 ✏️, M22.15 ∂ | |
| §8 Un vecteur fait de plusieurs blocs | Q8 | M22.10 ✏️ | M22.26 🐛 |

Parcours essentiel : tout sauf M22.Q7, M22.Q8, M22.12, M22.14, M22.15, M22.17, M22.E1, M22.E2, M22.22, M22.24, M22.27 et M22.28.

## Guide de lecture de MML

**MML §4.2** (*Eigenvalues and Eigenvectors*), déjà lu en M12c : relis-le **après le §2** de cette fiche et **avant le §3**.
- Le début de la section (la définition des valeurs et vecteurs propres, la liste des énoncés équivalents, les multiplicités et les premiers exemples) se relit vite : c'est M12c §3 et §4.
- Le passage qui compte pour ce chapitre est *Graphical Intuition in Two Dimensions*, avec sa **figure 4.4** : cinq matrices $2 \times 2$, l'effet de chacune sur une grille de points du plan, et leurs valeurs propres. Lis chaque description en te demandant ce que deviendrait la grille si l'on appliquait la matrice encore et encore ; le 📖 M22.17 te le fait calculer.
- Le reste se survole : l'exemple sur un réseau de neurones biologique, les théorèmes sur l'indépendance des vecteurs propres, le théorème spectral, le déterminant et la trace (M12c §3 et §6), et l'exemple de PageRank (M26).

MML ne parle ni de rayon spectral, ni de croissance transitoire, ni de normes induites (sauf la norme spectrale, au §4.6, lue en M12d), ni de produits de matrices différentes, ni de récurrences avec entrée : pour les §1 et §3 à §8, la fiche est le cours. Les exercices de MML sur les valeurs propres, en fin de chapitre 4, sont conseillés, pas obligatoires.

📐 **Notations.**
- MML (définition 4.6) cherche une valeur propre réelle et un vecteur propre de $\mathbb{R}^n$ ; la fiche, comme M12c, accepte des valeurs propres complexes et des vecteurs propres de $\mathbb{C}^n$. MML écrit $\mathbf{x}$ un vecteur propre, la fiche $\mathbf{v}$. La figure 4.4 écrit les valeurs propres complexes à la manière de Python, avec un `j` à la place de notre $i$.
- MML appelle *induced norm* (§3.3) la norme qui vient d'un produit scalaire ; ici, une **norme induite** est la norme d'une **matrice** induite par une norme de vecteurs (*operator norm*), §4.
- La fiche écrit $\rho(\mathbf{A})$ le rayon spectral, $\lVert\mathbf{A}\rVert_1$, $\lVert\mathbf{A}\rVert_2 = s_{\max}(\mathbf{A})$ et $\lVert\mathbf{A}\rVert_\infty$ les normes induites, $\lVert\mathbf{A}\rVert_F$ la norme de Frobenius, $\mathbf{P}_t = \mathbf{A}_t\cdots\mathbf{A}_1$ un produit de matrices ; une diagonalisation s'écrit $\mathbf{A} = \mathbf{V}\mathbf{D}\mathbf{V}^{-1}$ (M12c écrivait $\mathbf{P}$, réservé ici aux produits). Les états sont des **colonnes**, comme dans MML et M19.

Vocabulaire anglais de ce chapitre : *state*, *input*, *output*, *state-space model*, *linear time-invariant system*, *free response*, *forced response*, *impulse response*, *superposition*, *Leslie matrix*, *complex number*, *modulus*, *argument*, *polar form*, *exponential form*, *Euler's formula*, *De Moivre's formula*, *rotation*, *scaling*, *spiral*, *similar matrices*, *spectral radius*, *nilpotent matrix*, *Jordan block*, *normal matrix*, *non-normal matrix*, *transient growth*, *induced norm*, *operator norm*, *submultiplicativity*, *spectral norm*, *Frobenius norm*, *Gelfand's formula*, *Hadamard product*, *half-life*, *geometric mean*, *growth rate*, *Lyapunov exponent*, *trajectory*, *contraction*, *fixed point*, *attracting fixed point*, *repelling fixed point*, *sensitivity*, *truncation*, *block vector*, *global norm*, *projection*, *threshold*.

## Objectifs d'apprentissage

À la fin du chapitre, tu sais :
- **résoudre** une récurrence linéaire vectorielle avec entrée, et **lire** sa sortie comme la convolution de l'entrée par la réponse impulsionnelle ;
- **calculer** les puissances d'une matrice, ses valeurs propres complexes sous forme exponentielle, et **reconnaître** une rotation et une homothétie ;
- **décider** si $\mathbf{A}^t$ tend vers 0 par le rayon spectral, et **repérer** une croissance transitoire ;
- **calculer** les normes induites $\lVert\cdot\rVert_1$, $\lVert\cdot\rVert_\infty$ et $\lVert\cdot\rVert_2$ d'une matrice, et **majorer** la norme d'un produit ;
- **suivre** un produit de facteurs dans [0, 1] et un produit de jacobiennes le long d'une trajectoire ;
- **écrire** la sensibilité de l'état final à un paramètre utilisé à chaque pas comme une somme sur le temps ;
- **ramener** sous un seuil un vecteur fait de plusieurs blocs sans changer sa direction.

## L'essentiel en 10 lignes

1. **Récurrence avec entrée** $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t$ : $\mathbf{x}_t = \mathbf{A}^t\mathbf{x}_0 + \sum_{k=0}^{t-1}\mathbf{A}^{t-1-k}\mathbf{B}\mathbf{u}_k$ ; l'entrée reçue au pas $k$ est portée par $\mathbf{A}^{t-1-k}$.
2. **Réponse impulsionnelle** $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$ : pour $\mathbf{x}_0 = \mathbf{0}$, la sortie $y_t = \mathbf{C}\mathbf{x}_t$ vérifie $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$, la convolution de M21.
3. **Complexes** : $z = r\,e^{i\theta} = r(\cos\theta + i\sin\theta)$ ; un produit multiplie les modules et additionne les arguments ; $z^t = r^t e^{it\theta}$ (Moivre).
4. $\begin{pmatrix} a & -b \\ b & a \end{pmatrix} = r\,\mathbf{R}_\theta$ est la multiplication par $a + ib$ : une **rotation** d'angle $\theta$ et une **homothétie** de rapport $r$. Une matrice réelle $2 \times 2$ de valeurs propres $r\,e^{\pm i\theta}$ ($r = \sqrt{\det\mathbf{A}}$) fait des spirales : $\mathbf{A}^t$ tourne de $t\theta$ et se multiplie par $r^t$, dans un repère oblique.
5. **Rayon spectral** $\rho(\mathbf{A}) = \max_i\lvert\lambda_i\rvert$ (valeurs propres complexes comprises) ; $\mathbf{A}^t \to \mathbf{0}$ **si et seulement si** $\rho(\mathbf{A}) < 1$.
6. Une matrice **non normale** ($\mathbf{A}^\top\mathbf{A} \ne \mathbf{A}\mathbf{A}^\top$) peut voir $\lVert\mathbf{A}^t\rVert$ grandir pendant de nombreux pas avant de décroître (**croissance transitoire**) ; pour une matrice normale, $\lVert\mathbf{A}^t\rVert_2 = \rho(\mathbf{A})^t$.
7. **Normes induites** $\lVert\mathbf{A}\rVert = \max_{\mathbf{x} \ne \mathbf{0}}\lVert\mathbf{A}\mathbf{x}\rVert/\lVert\mathbf{x}\rVert$ : $\lVert\mathbf{A}\rVert_1$ = plus grande somme des $\lvert a_{ij}\rvert$ d'une **colonne**, $\lVert\mathbf{A}\rVert_\infty$ d'une **ligne**, $\lVert\mathbf{A}\rVert_2 = s_{\max}$. Elles vérifient $\lVert\mathbf{A}\mathbf{B}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{B}\rVert$, $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert$ et $\lVert\mathbf{A}^t\rVert^{1/t} \to \rho(\mathbf{A})$ ; la norme de Frobenius n'est pas induite.
8. **Produits** : $\lVert\mathbf{A}_t\cdots\mathbf{A}_1\rVert \le \lVert\mathbf{A}_t\rVert\cdots\lVert\mathbf{A}_1\rVert$. Des facteurs $a_k \in [0, 1]$ laissent $\prod_k a_k$ ; $(1 - \varepsilon)^t \approx e^{-t\varepsilon}$, demi-vie $\approx \frac{\ln 2}{\varepsilon}$ ; des facteurs aléatoires s'éteignent si $\mathbb{E}[\ln a] < 0$, même quand $\mathbb{E}[a] > 1$.
9. **Récurrence non linéaire** $\mathbf{x}_{t+1} = f(\mathbf{x}_t)$ : $\frac{\partial\mathbf{x}_T}{\partial\mathbf{x}_t} = \mathbf{J}_f(\mathbf{x}_{T-1})\cdots\mathbf{J}_f(\mathbf{x}_t)$, le dernier pas à gauche. Une **contraction** de facteur $q < 1$ oublie son départ : $\lVert\mathbf{x}_t - \tilde{\mathbf{x}}_t\rVert \le q^t\lVert\mathbf{x}_0 - \tilde{\mathbf{x}}_0\rVert$. La **sensibilité** $\mathbf{s}_t = \partial\mathbf{x}_t/\partial\beta$ à un paramètre utilisé à chaque pas vérifie $\mathbf{s}_{t+1} = \mathbf{J}_t\mathbf{s}_t + \mathbf{b}_t$, d'où une **somme sur le temps**.
10. **Blocs** : $\lVert\mathbf{w}\rVert^2 = \sum_k\lVert\mathbf{w}_k\rVert^2$ ; $\mathbf{w}\min\big(1, \frac{c}{\lVert\mathbf{w}\rVert}\big)$ ramène le tout sous $c$ **sans changer sa direction** ; ramener chaque bloc sous $c$ change la direction et laisse une norme globale jusqu'à $c\sqrt{p}$ pour $p$ blocs.

## §1 · Récurrences linéaires vectorielles avec entrée : solution et réponse impulsionnelle

### Un état, une entrée, une règle fixe

R5 étudiait $u_{t+1} = a\,u_t + b$, et M19 §3 l'itération $\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$ : une règle fixe, appliquée encore et encore, avec un terme **constant**. Beaucoup de systèmes reçoivent à chaque pas une **entrée** différente : des inscriptions, des naissances, des pluies, des versements. On décrit le système à l'instant $t$ par un vecteur, son **état** (*state*) $\mathbf{x}_t \in \mathbb{R}^n$, et ce qu'il reçoit par un vecteur $\mathbf{u}_t \in \mathbb{R}^m$, l'**entrée** (*input*).

> **Définition.** Une **récurrence linéaire avec entrée** (un *state-space model* ; on dit aussi un système linéaire invariant dans le temps, *linear time-invariant system*) est
> $$\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t, \qquad t = 0, 1, 2, \ldots, \qquad \mathbf{A} \text{ de forme } (n, n),\ \mathbf{B} \text{ de forme } (n, m),$$
> l'état initial $\mathbf{x}_0$ étant donné. On observe souvent une **sortie** (*output*) $y_t = \mathbf{C}\mathbf{x}_t$ ; dans ce chapitre, une seule grandeur observée : $\mathbf{C}$ est une ligne, de forme $(1, n)$.

Les matrices $\mathbf{A}$, $\mathbf{B}$ et $\mathbf{C}$ ne changent pas avec $t$ : la règle est la même à chaque pas (le §5 lèvera cette hypothèse).

**Exemple : un cursus en deux ans.** Au début de l'année $t$, un cursus compte $x_{t,1}$ étudiants en première année et $x_{t,2}$ en seconde : l'état est $\mathbf{x}_t = (x_{t,1}, x_{t,2})$. Pendant l'année, en première année, 20 % redoublent, 60 % passent en seconde, les autres partent ; en seconde année, 10 % redoublent, 80 % obtiennent leur diplôme, les autres partent. Les $u_t$ inscrits de l'année $t$ commencent l'année suivante en première année. Le nombre de diplômés de l'année $t$ est $y_t = 0{,}8\,x_{t,2}$. Donc
$$\mathbf{x}_{t+1} = \underbrace{\begin{pmatrix} 0{,}2 & 0 \\ 0{,}6 & 0{,}1 \end{pmatrix}}_{\mathbf{A}}\mathbf{x}_t + \underbrace{\begin{pmatrix} 1 \\ 0 \end{pmatrix}}_{\mathbf{B}}u_t, \qquad y_t = \underbrace{\begin{pmatrix} 0 & 0{,}8 \end{pmatrix}}_{\mathbf{C}}\mathbf{x}_t .$$
Le cursus ouvre ($\mathbf{x}_0 = \mathbf{0}$) et reçoit $u_0 = 100$, $u_1 = 120$, $u_2 = 80$ inscrits. Pas à pas : $\mathbf{x}_1 = (100, 0)$ ; $\mathbf{x}_2 = (0{,}2 \times 100 + 120,\ 0{,}6 \times 100) = (140, 60)$ ; $\mathbf{x}_3 = (0{,}2 \times 140 + 80,\ 0{,}6 \times 140 + 0{,}1 \times 60) = (108, 90)$. Les diplômés : $y_1 = 0$, $y_2 = 48$, $y_3 = 72$.

**La même forme, ailleurs.** Une population rangée en trois **classes d'âge** évolue par une **matrice de Leslie** (*Leslie matrix*)
$$\mathbf{A} = \begin{pmatrix} \varphi_1 & \varphi_2 & \varphi_3 \\ \sigma_1 & 0 & 0 \\ 0 & \sigma_2 & 0 \end{pmatrix} :$$
la première ligne compte les naissances (les **fécondités** $\varphi_i$ de chaque classe), la sous-diagonale les survivants qui passent dans la classe suivante (les **taux de survie** $\sigma_i$) ; des arrivants forment l'entrée. Des **réservoirs en cascade** (chaque bassin garde une partie de son eau et en verse une autre dans le suivant ; la pluie est l'entrée) ont une matrice $\mathbf{A}$ triangulaire, comme le cursus.

### La solution : des puissances de A

En déroulant : $\mathbf{x}_1 = \mathbf{A}\mathbf{x}_0 + \mathbf{B}\mathbf{u}_0$, puis $\mathbf{x}_2 = \mathbf{A}^2\mathbf{x}_0 + \mathbf{A}\mathbf{B}\mathbf{u}_0 + \mathbf{B}\mathbf{u}_1$, puis $\mathbf{x}_3 = \mathbf{A}^3\mathbf{x}_0 + \mathbf{A}^2\mathbf{B}\mathbf{u}_0 + \mathbf{A}\mathbf{B}\mathbf{u}_1 + \mathbf{B}\mathbf{u}_2$.

> **Théorème.** Pour tout $t \ge 0$,
> $$\mathbf{x}_t = \mathbf{A}^t\mathbf{x}_0 + \sum_{k=0}^{t-1}\mathbf{A}^{t-1-k}\,\mathbf{B}\mathbf{u}_k .$$

Par récurrence (R4) : pour $t = 0$, la somme est vide. Si la formule vaut pour $t$, alors $\mathbf{x}_{t+1} = \mathbf{A}\mathbf{x}_t + \mathbf{B}\mathbf{u}_t = \mathbf{A}^{t+1}\mathbf{x}_0 + \sum_{k=0}^{t-1}\mathbf{A}^{t-k}\mathbf{B}\mathbf{u}_k + \mathbf{B}\mathbf{u}_t$, et le dernier terme est celui de $k = t$, avec $\mathbf{A}^0 = \mathbf{I}$.

Comment la lire :
- $\mathbf{A}^t\mathbf{x}_0$ est la **réponse libre** (*free response*) : ce que deviendrait l'état initial sans aucune entrée ;
- la somme est la **réponse forcée** (*forced response*) : l'entrée $\mathbf{u}_k$, reçue au pas $k$, est portée jusqu'au pas $t$ par $\mathbf{A}^{t-1-k}$. Plus elle est récente, plus la puissance est petite ; la dernière, $\mathbf{u}_{t-1}$, est multipliée par $\mathbf{A}^0 = \mathbf{I}$. Il y a $t$ termes, un par entrée reçue ;
- l'état est **linéaire** en $(\mathbf{x}_0, \mathbf{u}_0, \ldots, \mathbf{u}_{t-1})$ : la réponse à une somme d'entrées est la somme des réponses (le **principe de superposition**, *superposition*).

Sur le cursus : $\mathbf{A}\mathbf{B} = (0{,}2 ;\ 0{,}6)$ et $\mathbf{A}^2\mathbf{B} = (0{,}04 ;\ 0{,}18)$, donc $\mathbf{x}_3 = 100\,(0{,}04 ;\ 0{,}18) + 120\,(0{,}2 ;\ 0{,}6) + 80\,(1, 0) = (108, 90)$ : le calcul pas à pas.

### La réponse impulsionnelle, et la sortie comme convolution

Prenons une seule entrée ($m = 1$), une seule sortie, et $\mathbf{x}_0 = \mathbf{0}$. Une **impulsion**, $u_0 = 1$ et toutes les autres entrées nulles, donne $\mathbf{x}_t = \mathbf{A}^{t-1}\mathbf{B}$ et $y_t = \mathbf{C}\mathbf{A}^{t-1}\mathbf{B}$ pour $t \ge 1$.

> **Définition.** La **réponse impulsionnelle** (*impulse response*) du système est la suite $\mathbf{h} = (h_0, h_1, h_2, \ldots)$, avec $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$ : la sortie $k + 1$ pas après une entrée unité.
>
> **Propriété.** Pour $\mathbf{x}_0 = \mathbf{0}$ et toute suite d'entrées $\mathbf{u}$,
> $$y_{t+1} = \sum_{k=0}^{t} h_{t-k}\,u_k = (\mathbf{h} * \mathbf{u})_t :$$
> la sortie est la **convolution** de l'entrée par la réponse impulsionnelle (M21 §1, indices à partir de 0), décalée d'un pas.

C'est le théorème multiplié à gauche par $\mathbf{C}$ : $y_{t+1} = \mathbf{C}\mathbf{x}_{t+1} = \sum_{k=0}^{t}\mathbf{C}\mathbf{A}^{t-k}\mathbf{B}\,u_k$. La convolution de M21 avait un noyau fini ; celui-ci est infini, mais la récurrence le calcule avec seulement $n$ nombres en mémoire, l'état : c'est un **filtre récursif**. Hors de ce chapitre, avec plusieurs entrées et sorties, $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$ est une matrice, et la formule reste la même.

**Exemple.** Pour le cursus : $h_0 = \mathbf{C}\mathbf{B} = 0$ (personne n'est diplômé l'année de son entrée), $h_1 = \mathbf{C}\mathbf{A}\mathbf{B} = 0{,}8 \times 0{,}6 = 0{,}48$, $h_2 = 0{,}8 \times 0{,}18 = 0{,}144$, $h_3 = 0{,}0336$ : sur 100 inscrits, 48 sont diplômés deux ans après leur inscription, 14,4 trois ans après, puis 3,36 quatre ans après… La convolution de $\mathbf{h}$ par $\mathbf{u} = (100, 120, 80)$ commence par $(0 ;\ 48 ;\ 72 ;\ 59{,}04 ;\ \ldots)$ : on retrouve $y_1 = 0$, $y_2 = 48$, $y_3 = 72$, et $y_4 = h_3u_0 + h_2u_1 + h_1u_2 = 3{,}36 + 17{,}28 + 38{,}4 = 59{,}04$. Chaque promotion d'inscrits apporte sa copie de $\mathbf{h}$, décalée et multipliée par son effectif ; les copies s'additionnent.

![À gauche, la réponse impulsionnelle du cursus en deux ans, h = (0 ; 0,48 ; 0,144 ; 0,0336 ; …) ; à droite, les diplômés de chaque année pour 100, 120 puis 80 inscrits, en barres empilées : la part de chaque promotion est une copie de h décalée et multipliée, et leur somme donne 0, 48, 72, 59,04…](figures/reponse_impulsionnelle.png)

📐 **Notations.** Convention **colonne**, comme MML et M19 : $\mathbf{x}_t$ est une colonne, et $\mathbf{A}$ la multiplie à gauche. Les bibliothèques d'apprentissage rangent les états en **lignes** et écrivent $\mathbf{x}_{t+1} = \mathbf{x}_t\mathbf{A} + \mathbf{u}_t\mathbf{B}$ : le 🔗 M22.16 fait le pont entre les deux conventions.

💻 **Aujourd'hui en pratique** — on simule un tel système pas à pas, une multiplication par $\mathbf{A}$ par pas, sans jamais calculer $\mathbf{A}^t$ : c'est ce que fait `linear_system_states` (🔨 M22.19), et `scipy.signal.dlsim` dans SciPy. Pour une seule entrée et une seule sortie, `scipy.signal.lfilter` applique directement une récurrence sur les sorties passées : un filtre récursif.

⚠️ **Erreur classique.** Écrire $\mathbf{A}^{t-k}$ au lieu de $\mathbf{A}^{t-1-k}$ : la dernière entrée, $\mathbf{u}_{t-1}$, n'est pas multipliée par $\mathbf{A}$. Oublier la réponse libre $\mathbf{A}^t\mathbf{x}_0$ quand $\mathbf{x}_0 \ne \mathbf{0}$ ; écrire $\mathbf{B}\mathbf{A}$ au lieu de $\mathbf{A}\mathbf{B}$ (les formes ne s'enchaînent pas dès que $m \ne n$) ; ou oublier le décalage d'un pas entre la sortie et la convolution.

🔗 **Dans workbookIA** — le chapitre 22 met à jour un état à chaque élément d'une séquence, toujours avec la même règle ; quand cette règle est linéaire, c'est cette récurrence, écrite en convention ligne.

## §2 · Puissances d'une matrice : valeurs propres complexes, forme exponentielle et rotations

### Les puissances d'une matrice diagonalisable (rappel de M12c)

Si $\mathbf{A} = \mathbf{V}\mathbf{D}\mathbf{V}^{-1}$, avec les vecteurs propres en colonnes de $\mathbf{V}$ et les valeurs propres sur la diagonale de $\mathbf{D}$, alors $\mathbf{A}^t = \mathbf{V}\mathbf{D}^t\mathbf{V}^{-1}$ (M12c §4). Autrement dit, si $\mathbf{x}_0 = \alpha_1\mathbf{v}_1 + \cdots + \alpha_n\mathbf{v}_n$, alors
$$\mathbf{A}^t\mathbf{x}_0 = \alpha_1\lambda_1^t\,\mathbf{v}_1 + \cdots + \alpha_n\lambda_n^t\,\mathbf{v}_n :$$
chaque coordonnée dans la base des vecteurs propres est multipliée par sa valeur propre à chaque pas, $n$ suites géométriques indépendantes (M19 §3).

**Exemple.** La matrice du cursus est triangulaire, de valeurs propres $0{,}2$ (vecteur propre $(1, 6)$) et $0{,}1$ (vecteur propre $(0, 1)$). On trouve
$$\mathbf{A}^t = \begin{pmatrix} 0{,}2^t & 0 \\ 6\,(0{,}2^t - 0{,}1^t) & 0{,}1^t \end{pmatrix}, \qquad\text{d'où}\qquad h_k = \mathbf{C}\mathbf{A}^k\mathbf{B} = 4{,}8\,(0{,}2^k - 0{,}1^k),$$
qui redonne $h_1 = 0{,}48$ et $h_2 = 4{,}8 \times 0{,}03 = 0{,}144$.

Quand les valeurs propres sont complexes, la formule reste vraie, avec des nombres complexes partout : les paragraphes suivants disent comment les lire.

### La forme exponentielle d'un nombre complexe

M12c §3 a introduit $z = a + ib$, son conjugué $\bar z = a - ib$ et son module $\lvert z\rvert = \sqrt{a^2 + b^2}$ ; M19 §6, le module d'un produit et la forme trigonométrique $z = r(\cos\theta + i\sin\theta)$, avec $r = \lvert z\rvert$. On complète.

- L'**argument** (*argument*) de $z \ne 0$ est l'angle $\theta$ que fait le vecteur $(a, b)$ du plan avec l'axe des abscisses : $\cos\theta = \frac{a}{r}$ et $\sin\theta = \frac{b}{r}$. Il est défini à un multiple de $2\pi$ près (on le prend souvent entre $-\pi$ et $\pi$).
- La **formule d'Euler** (*Euler's formula*), admise : $e^{i\theta} = \cos\theta + i\sin\theta$. Le nombre $e^{i\theta}$ est sur le cercle de rayon 1, et tout complexe non nul s'écrit $z = r\,e^{i\theta}$ : sa **forme exponentielle** (*exponential form*, ou *polar form*).
- La règle des exponentielles reste vraie, $e^{i\theta_1}e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$ (on l'admet ; elle équivaut aux formules d'addition du cosinus et du sinus). Donc, pour un **produit**, $(r_1e^{i\theta_1})(r_2e^{i\theta_2}) = r_1r_2\,e^{i(\theta_1 + \theta_2)}$ : **les modules se multiplient, les arguments s'additionnent**.
- Les **puissances** (formule de **Moivre**, *De Moivre's formula*) : $(r\,e^{i\theta})^t = r^t e^{it\theta}$. Le module de $z^t$ est $r^t$, qui tend vers 0 si et seulement si $r < 1$. Le conjugué est $\bar z = r\,e^{-i\theta}$.

**Exemples.** $1 + i$ a pour module $\sqrt2$ et pour argument $\frac\pi4$ ($\cos\theta = \sin\theta = \frac{1}{\sqrt2}$) : $1 + i = \sqrt2\,e^{i\pi/4}$. De même, $1 + i\sqrt3 = 2\,e^{i\pi/3}$, $i = e^{i\pi/2}$ et $-1 = e^{i\pi}$. Leur produit : $(1 + i)(1 + i\sqrt3) = 2\sqrt2\,e^{i7\pi/12}$ ; en développant, $(1 - \sqrt3) + i(1 + \sqrt3)$, dont le module au carré vaut bien $(1 - \sqrt3)^2 + (1 + \sqrt3)^2 = 8$. Enfin $(1 + i)^8 = (\sqrt2)^8\,e^{i2\pi} = 16$ ; vérification : $(1 + i)^2 = 2i$, puis $(2i)^4 = 16$.

### Multiplier par un complexe : une rotation et une homothétie

Identifions le complexe $z = x + iy$ au point $(x, y)$ du plan. Multiplier par un complexe fixé $\mu = a + ib$ donne $(a + ib)(x + iy) = (ax - by) + i(bx + ay)$ : c'est une application linéaire du plan, de matrice
$$\mathbf{M}_\mu = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} = r\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = r\,\mathbf{R}_\theta, \qquad \mu = r\,e^{i\theta}.$$
$\mathbf{R}_\theta$ est la **rotation** d'angle $\theta$ (M12c §3) ; multiplier tous les vecteurs par $r$ est une **homothétie** de rapport $r$ (*scaling*). Le polynôme caractéristique de $\mathbf{M}_\mu$ est $\lambda^2 - 2a\lambda + r^2$ : ses valeurs propres sont $a \pm ib$, le nombre $\mu$ et son conjugué.

**Les puissances.** Deux rotations s'enchaînent en une seule, $\mathbf{R}_{\theta_1}\mathbf{R}_{\theta_2} = \mathbf{R}_{\theta_1+\theta_2}$ (c'est la règle des arguments), donc $\mathbf{M}_\mu^t = r^t\,\mathbf{R}_{t\theta}$ : la formule de Moivre, écrite avec des matrices. La **trajectoire** (*trajectory*) $\mathbf{x}_t = \mathbf{M}_\mu^t\mathbf{x}_0$ tourne de $\theta$ à chaque pas, et sa distance à l'origine est multipliée par $r$ : une **spirale** qui rentre vers l'origine si $r < 1$, un cercle si $r = 1$, une spirale qui sort si $r > 1$.

**Exemple.** $\mu = 1 + i$ donne $\mathbf{M} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \sqrt2\,\mathbf{R}_{\pi/4}$. Depuis $\mathbf{x}_0 = (1, 0)$ : $(1, 1)$, $(0, 2)$, $(-2, 2)$, $(-4, 0)$, … et $\mathbf{x}_8 = (16, 0)$ : $\mathbf{M}^8 = 16\,\mathbf{I}$, huit huitièmes de tour et un facteur $(\sqrt2)^8$.

**Les matrices orthogonales.** Pour $r = 1$, $\mathbf{R}_\theta$ est orthogonale (M12b) : elle conserve les normes, $\lVert\mathbf{R}_\theta\mathbf{x}\rVert = \lVert\mathbf{x}\rVert$. Plus généralement, les puissances d'une matrice orthogonale $\mathbf{Q}$ sont orthogonales ($(\mathbf{Q}^t)^\top\mathbf{Q}^t = \mathbf{I}$), donc $\lVert\mathbf{Q}^t\mathbf{x}\rVert = \lVert\mathbf{x}\rVert$ pour tout $t$ : ni extinction ni explosion. Ses valeurs propres, complexes en général, sont toutes de module 1 (on l'admet).

### Une matrice réelle 2 × 2 à valeurs propres complexes

Le polynôme caractéristique d'une matrice $2 \times 2$ est $\lambda^2 - (\operatorname{tr}\mathbf{A})\,\lambda + \det\mathbf{A}$ (M12c §3). Si son discriminant $(\operatorname{tr}\mathbf{A})^2 - 4\det\mathbf{A}$ est négatif, ses racines sont deux complexes conjugués $r\,e^{\pm i\theta}$, de produit $r^2 = \det\mathbf{A}$ et de somme $2r\cos\theta = \operatorname{tr}\mathbf{A}$ (M19 §6) :
$$r = \sqrt{\det\mathbf{A}}, \qquad \cos\theta = \frac{\operatorname{tr}\mathbf{A}}{2\sqrt{\det\mathbf{A}}}.$$

> **Propriété** (admise). Si une matrice réelle $\mathbf{A}$ de forme $(2, 2)$ a les valeurs propres $a \pm ib$, avec $b \ne 0$, il existe une matrice réelle inversible $\mathbf{V}$ telle que
> $$\mathbf{A} = \mathbf{V}\begin{pmatrix} a & -b \\ b & a \end{pmatrix}\mathbf{V}^{-1} = r\,\mathbf{V}\mathbf{R}_\theta\mathbf{V}^{-1}, \qquad\text{donc}\qquad \mathbf{A}^t = r^t\,\mathbf{V}\mathbf{R}_{t\theta}\mathbf{V}^{-1}.$$
> Les colonnes de $\mathbf{V}$ sont la partie réelle et l'opposée de la partie imaginaire d'un vecteur propre de $a + ib$.

$\mathbf{A}$ est donc **semblable** (M12c §4) à une rotation-homothétie : dans le repère oblique formé par les colonnes de $\mathbf{V}$, elle tourne de $\theta$ et multiplie par $r$ ; la trajectoire est l'image par $\mathbf{V}$ d'une spirale circulaire, une **spirale elliptique**. Chaque coordonnée de $\mathbf{x}_t$ est $r^t$ fois une combinaison de $\cos t\theta$ et de $\sin t\theta$, comme les solutions des récurrences d'ordre 2 de M19 §6.

**Exemple.** $\mathbf{A} = \begin{pmatrix} 1 & -1 \\ 0{,}8 & 0{,}2 \end{pmatrix}$ : $\operatorname{tr}\mathbf{A} = 1{,}2$, $\det\mathbf{A} = 0{,}2 + 0{,}8 = 1$, discriminant $1{,}44 - 4 < 0$. Donc $r = 1$, $\cos\theta = 0{,}6$, $\theta \approx 0{,}927$ rad (environ 53°), et les valeurs propres sont $0{,}6 \pm 0{,}8\,i$. La première ligne de $(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ donne le vecteur propre $\mathbf{v} = (1 ;\ 0{,}4 - 0{,}8\,i)$ pour $\lambda = 0{,}6 + 0{,}8\,i$, d'où $\mathbf{V} = \begin{pmatrix} 1 & 0 \\ 0{,}4 & 0{,}8 \end{pmatrix}$ (vérifie que $\mathbf{A}\mathbf{V} = \mathbf{V}\mathbf{R}_\theta$). Depuis $\mathbf{x}_0 = (1, 0)$ : $\mathbf{x}_1 = (1 ;\ 0{,}8)$, $\mathbf{x}_2 = (0{,}2 ;\ 0{,}96)$, $\mathbf{x}_3 = (-0{,}76 ;\ 0{,}352)$… Les points restent sur une **ellipse**, sans s'éteindre ni exploser ; multiplier $\mathbf{A}$ par $0{,}96$ ou par $1{,}03$ multiplie les valeurs propres par ce nombre, et la trajectoire devient une spirale qui rentre ou qui sort.

![Les trajectoires depuis (1, 0) de x ↦ 0,96 A x (une spirale qui rentre), de x ↦ A x (une ellipse, image par V du cercle que parcourt la rotation R_θ, dessiné en tirets) et de x ↦ 1,03 A x (une spirale qui sort), avec A de lignes (1, −1) et (0,8 ; 0,2), de valeurs propres 0,6 ± 0,8i](figures/spirales.png)

💻 **Aujourd'hui en pratique** — `np.linalg.eigvals(A)` rend `array([0.6+0.8j, 0.6-0.8j])` pour cette matrice : Python écrit `j` pour $i$. `np.abs` donne les modules, `np.angle` les arguments (entre $-\pi$ et $\pi$), et `np.exp(1j * theta)` calcule $e^{i\theta}$.

⚠️ **Erreur classique.** Prendre la partie réelle $\frac{\operatorname{tr}\mathbf{A}}{2}$ pour le module : ici elle vaut $0{,}6$, alors que le module vaut $\sqrt{\det\mathbf{A}} = 1$, et la trajectoire ne s'éteint pas. Ou croire qu'une trajectoire qui ne s'éteint pas reste à distance constante de l'origine : sur une ellipse, la norme de $\mathbf{x}_t$ monte et descend.

## §3 · Le rayon spectral : Aᵗ → 0 si et seulement si ρ(A) < 1, et la croissance transitoire

### Le rayon spectral

> **Définition.** Le **rayon spectral** (*spectral radius*) d'une matrice carrée $\mathbf{A}$, de valeurs propres complexes $\lambda_1, \ldots, \lambda_n$ (comptées avec leur multiplicité), est
> $$\rho(\mathbf{A}) = \max_i\,\lvert\lambda_i\rvert,$$
> le rayon du plus petit disque du plan complexe, centré en 0, qui contient toutes les valeurs propres.

M19 §3 l'a défini pour une matrice symétrique, dont les valeurs propres sont réelles ; la définition vaut pour toute matrice carrée. Exemples : le cursus, $\rho = 0{,}2$ ; la matrice $\mathbf{M}$ du §2, de valeurs propres $1 \pm i$, $\rho = \sqrt2$ ; la matrice $\begin{pmatrix} 1 & -1 \\ 0{,}8 & 0{,}2 \end{pmatrix}$ du §2, $\rho = 1$. Trois remarques :
- une matrice non nulle peut avoir un rayon spectral nul : $\mathbf{N} = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix}$, triangulaire de diagonale nulle, vérifie $\mathbf{N}^2 = \mathbf{0}$ (une matrice **nilpotente**, M16 §4), et $\rho(\mathbf{N}) = 0$ ;
- $\rho$ n'a de sens que pour une matrice **carrée** (une matrice rectangulaire n'a ni valeurs propres ni puissances) ;
- les valeurs propres de $\mathbf{A}^t$ sont les $\lambda_i^t$ (on l'admet en général ; M12c §3 le montre sur un vecteur propre), donc $\rho(\mathbf{A}^t) = \rho(\mathbf{A})^t$.

### Aᵗ tend vers 0 si et seulement si ρ(A) < 1

> **Théorème** (admis en général ; ∂ M22.13 le démontre pour une matrice diagonalisable sur $\mathbb{C}$). Pour une matrice carrée $\mathbf{A}$, $\mathbf{A}^t \to \mathbf{0}$ (chaque coefficient tend vers 0) **si et seulement si** $\rho(\mathbf{A}) < 1$. Alors $\mathbf{A}^t\mathbf{x}_0 \to \mathbf{0}$ pour tout $\mathbf{x}_0$.

« Diagonalisable sur $\mathbb{C}$ » veut dire $\mathbf{A} = \mathbf{V}\mathbf{D}\mathbf{V}^{-1}$ avec $\mathbf{V}$ et $\mathbf{D}$ éventuellement complexes : c'est le cas dès que les $n$ valeurs propres sont distinctes (M12c §4), comme pour une rotation d'angle autre que 0 et $\pi$. L'idée de la preuve dans ce cas : $\mathbf{A}^t = \mathbf{V}\mathbf{D}^t\mathbf{V}^{-1}$, et les coefficients de $\mathbf{D}^t$ sont les $\lambda_i^t$, de modules $\lvert\lambda_i\rvert^t$. Dans l'autre sens, une valeur propre de module au moins 1 a un vecteur propre $\mathbf{v}$ (complexe peut-être) que $\mathbf{A}^t$ multiplie par $\lambda^t$, qui ne tend pas vers 0.

**Ce que cela dit d'une récurrence avec entrée.** Si $\rho(\mathbf{A}) < 1$, la réponse libre $\mathbf{A}^t\mathbf{x}_0$ tend vers 0 : le système **oublie son état initial**. Deux trajectoires qui reçoivent les mêmes entrées se rapprochent, puisque leur écart vérifie $\boldsymbol{\delta}_t = \mathbf{A}^t\boldsymbol{\delta}_0$ ; et la réponse impulsionnelle $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$ tend vers 0. Pour le cursus, $\rho = 0{,}2$ : dès $t = 4$, les coefficients de $\mathbf{A}^t$ sont plus petits que $0{,}01$.

### Les cas limites

- **$\rho = 1$.** $\mathbf{A}^t$ ne tend pas vers $\mathbf{0}$, mais tout peut arriver. La matrice du §2 reste bornée : sa trajectoire tourne sur une ellipse. Le cisaillement $\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$, de valeur propre double 1, non diagonalisable, a pour puissances $\begin{pmatrix} 1 & 3t \\ 0 & 1 \end{pmatrix}$ : il grandit sans fin, linéairement.
- **Non diagonalisable, $\rho < 1$.** Un **bloc de Jordan** (*Jordan block*) $\begin{pmatrix} \lambda & \gamma \\ 0 & \lambda \end{pmatrix} = \lambda\mathbf{I} + \mathbf{U}$, avec $\gamma \ne 0$, où $\mathbf{U} = \begin{pmatrix} 0 & \gamma \\ 0 & 0 \end{pmatrix}$ vérifie $\mathbf{U}^2 = \mathbf{0}$. Comme $\lambda\mathbf{I}$ et $\mathbf{U}$ commutent, la formule du binôme s'applique, et tous ses termes à partir de $\mathbf{U}^2$ sont nuls :
$$\begin{pmatrix} \lambda & \gamma \\ 0 & \lambda \end{pmatrix}^t = \lambda^t\mathbf{I} + t\lambda^{t-1}\mathbf{U} = \begin{pmatrix} \lambda^t & t\gamma\lambda^{t-1} \\ 0 & \lambda^t \end{pmatrix} \qquad (t \ge 1).$$
Pour $\lvert\lambda\rvert < 1$, $t\lambda^{t-1} \to 0$ (croissances comparées, R6 §5) : le théorème s'applique, avec un facteur $t$ qui retarde la décroissance. En dimension $n$, une matrice triangulaire de diagonale nulle $\mathbf{U}$ vérifie $\mathbf{U}^n = \mathbf{0}$, ce qui arrête de même la somme du binôme.
- **$\rho > 1$.** La composante sur un vecteur propre de module maximal grandit comme $\rho^t$ : la trajectoire de $\mathbf{M}$ s'éloigne comme $(\sqrt2)^t$.

### La croissance transitoire

Le théorème parle de la **limite**, pas des premiers pas. Prenons
$$\mathbf{A} = \begin{pmatrix} 0{,}75 & 6 \\ 0 & 0{,}6 \end{pmatrix}, \qquad \rho(\mathbf{A}) = 0{,}75 < 1 .$$
Pour une matrice $2 \times 2$ triangulaire supérieure $\begin{pmatrix} \lambda_1 & \gamma \\ 0 & \lambda_2 \end{pmatrix}$, avec $\lambda_1 \ne \lambda_2$, le coefficient en haut à droite de $\mathbf{A}^t$ vaut $\gamma\,\frac{\lambda_1^t - \lambda_2^t}{\lambda_1 - \lambda_2}$ (par récurrence : ✏️ M22.5) ; ici
$$\mathbf{A}^t = \begin{pmatrix} 0{,}75^t & 40\,(0{,}75^t - 0{,}6^t) \\ 0 & 0{,}6^t \end{pmatrix}.$$
Ce coefficient vaut $6$, puis $8{,}1$, puis $8{,}235$ pour $t = 1, 2, 3$, et ne redescend sous 1 qu'à $t = 13$ ; $\lVert\mathbf{A}^t\rVert_2$ (la norme spectrale de M12d) le suit de près : $6{,}08$ ; $8{,}13$ ; $8{,}25$ ; $7{,}48$… Le vecteur $\mathbf{e}_2 = (0, 1)$, de norme 1, devient $\mathbf{A}^3\mathbf{e}_2 = (8{,}235 ;\ 0{,}216)$, de norme $8{,}24$, avant de tendre vers 0. C'est la **croissance transitoire** (*transient growth*).

**Pourquoi.** Les vecteurs propres sont $\mathbf{e}_1$ (pour $0{,}75$) et $\mathbf{v}_2 = (-40, 1)$ (pour $0{,}6$) : presque parallèles, à $1{,}4$° l'un de l'autre. Le petit vecteur $\mathbf{e}_2$ est la différence de deux grands, $\mathbf{e}_2 = \mathbf{v}_2 + 40\,\mathbf{e}_1$, qui se compensent presque. Ils décroissent à des vitesses différentes, $\mathbf{A}^t\mathbf{e}_2 = 0{,}6^t\,\mathbf{v}_2 + 40 \times 0{,}75^t\,\mathbf{e}_1$, et la compensation cesse : la différence grandit, avant que les deux termes ne s'éteignent.

> **Définition.** Une matrice carrée réelle est **normale** (*normal matrix*) si $\mathbf{A}^\top\mathbf{A} = \mathbf{A}\mathbf{A}^\top$. Les matrices symétriques, orthogonales, et les matrices $r\,\mathbf{R}_\theta$ du §2 sont normales. Pour une matrice normale, $\lVert\mathbf{A}^t\rVert_2 = \rho(\mathbf{A})^t$ pour tout $t$ (admis : ses vecteurs propres, dans $\mathbb{C}^n$, peuvent être choisis orthogonaux) : pas de croissance transitoire.

MML §4.7 (*Matrix Phylogeny*, figure 4.13) place les matrices normales dans son arbre des matrices carrées. Ici $\mathbf{A}^\top\mathbf{A} = \begin{pmatrix} 0{,}5625 & 4{,}5 \\ 4{,}5 & 36{,}36 \end{pmatrix} \ne \mathbf{A}\mathbf{A}^\top = \begin{pmatrix} 36{,}5625 & 3{,}6 \\ 3{,}6 & 0{,}36 \end{pmatrix}$ : $\mathbf{A}$ est **non normale** (*non-normal matrix*). La matrice diagonale $\operatorname{diag}(0{,}75 ;\ 0{,}6)$, de mêmes valeurs propres, est normale, et $\lVert\operatorname{diag}(0{,}75 ;\ 0{,}6)^t\rVert_2 = 0{,}75^t$ décroît dès le premier pas. Pour une matrice non normale, **le rayon spectral dit le long terme, pas les premiers pas** ; le §4 montrera que $\lVert\mathbf{A}^t\rVert \ge \rho(\mathbf{A})^t$ toujours.

![À gauche, en échelle logarithmique, la norme ‖Aᵗ‖₂ de la matrice triangulaire de lignes (0,75 ; 6) et (0 ; 0,6) : elle monte jusqu'à 8,25 à t = 3 et ne redescend sous 1 qu'à t = 13, alors que ρᵗ = 0,75ᵗ décroît dès le début ; à droite, les deux grands termes 40 × 0,75ᵗ et 40 × 0,6ᵗ qui se compensent au départ, et leur différence, la première coordonnée de Aᵗe₂](figures/croissance_transitoire.png)

⚠️ **Erreur classique.** Conclure de $\rho(\mathbf{A}) < 1$ que $\lVert\mathbf{A}^t\mathbf{x}\rVert$ diminue à chaque pas : c'est vrai en norme 2 pour une matrice normale, faux en général. Ou, dans l'autre sens, conclure d'un premier pas qui allonge que les puissances explosent.

## §4 · Normes de matrices : normes induites, sous-multiplicativité et ρ ≤ ‖A‖

### Le plus grand facteur d'allongement

M12d a montré que $\lVert\mathbf{A}\mathbf{x}\rVert_2 \le s_{\max}\lVert\mathbf{x}\rVert_2$, avec égalité pour le premier vecteur singulier : $s_{\max}$ est le plus grand facteur par lequel $\mathbf{A}$ allonge un vecteur, sa **norme spectrale**. On fait de même avec n'importe quelle norme de vecteurs.

> **Définition.** Soit une norme de vecteurs $\lVert\cdot\rVert$ (la même sur $\mathbb{R}^n$ et sur $\mathbb{R}^m$). La **norme induite** (*induced norm*, *operator norm*) d'une matrice $\mathbf{A}$ de forme $(m, n)$ est
> $$\lVert\mathbf{A}\rVert = \max_{\mathbf{x} \ne \mathbf{0}}\frac{\lVert\mathbf{A}\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} = \max_{\lVert\mathbf{x}\rVert = 1}\lVert\mathbf{A}\mathbf{x}\rVert$$
> (le maximum existe : on l'admet).

Donc $\lVert\mathbf{A}\mathbf{x}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{x}\rVert$ pour **tout** $\mathbf{x}$, avec égalité pour au moins un $\mathbf{x} \ne \mathbf{0}$ : $\lVert\mathbf{A}\rVert$ est le plus petit nombre qui ait cette propriété. En image, la boule unité a pour image une partie de la boule de rayon $\lVert\mathbf{A}\rVert$, qui en touche le bord. C'est une norme sur les matrices (positivité, homogénéité, inégalité triangulaire), et toute norme induite donne $\lVert\mathbf{I}\rVert = 1$. La matrice peut être rectangulaire.

### Trois normes induites qui se calculent

> **Formules.** Avec les normes L1, L∞ et L2 de M07 :
> - $\lVert\mathbf{A}\rVert_1 = \max_j\sum_i\lvert a_{ij}\rvert$ : la plus grande somme des valeurs absolues d'une **colonne** ;
> - $\lVert\mathbf{A}\rVert_\infty = \max_i\sum_j\lvert a_{ij}\rvert$ : la plus grande somme des valeurs absolues d'une **ligne** ;
> - $\lVert\mathbf{A}\rVert_2 = s_{\max}(\mathbf{A}) = \sqrt{\lambda_{\max}(\mathbf{A}^\top\mathbf{A})}$ (M12d).

**Pourquoi les colonnes pour $\lVert\cdot\rVert_1$.** Pour tout $\mathbf{x}$, l'inégalité triangulaire donne
$$\lVert\mathbf{A}\mathbf{x}\rVert_1 = \sum_i\Big\lvert\sum_j a_{ij}x_j\Big\rvert \le \sum_j\Big(\sum_i\lvert a_{ij}\rvert\Big)\lvert x_j\rvert \le \Big(\max_j\sum_i\lvert a_{ij}\rvert\Big)\lVert\mathbf{x}\rVert_1,$$
et l'égalité est atteinte pour $\mathbf{x} = \mathbf{e}_{j^\star}$, le vecteur de base de la meilleure colonne : $\mathbf{A}\mathbf{e}_{j^\star}$ est cette colonne. Pour $\lVert\cdot\rVert_\infty$, ce sont les lignes, et l'égalité est atteinte en un vecteur de signes (∂ M22.12). Moyen mnémotechnique : le 1 est vertical comme une colonne, le $\infty$ est couché comme une ligne. Et $\lVert\mathbf{A}^\top\rVert_1 = \lVert\mathbf{A}\rVert_\infty$ : les colonnes de $\mathbf{A}^\top$ sont les lignes de $\mathbf{A}$.

**Exemple.** $\mathbf{A} = \begin{pmatrix} 2 & 1 \\ -2 & 4 \end{pmatrix}$.
- Colonnes : $2 + 2 = 4$ et $1 + 4 = 5$, donc $\lVert\mathbf{A}\rVert_1 = 5$, atteint en $\mathbf{e}_2$ : $\mathbf{A}\mathbf{e}_2 = (1, 4)$.
- Lignes : $3$ et $6$, donc $\lVert\mathbf{A}\rVert_\infty = 6$, atteint en $\mathbf{x} = (-1, 1)$, les signes de la seconde ligne : $\mathbf{A}\mathbf{x} = (-1, 6)$.
- $\mathbf{A}^\top\mathbf{A} = \begin{pmatrix} 8 & -6 \\ -6 & 17 \end{pmatrix}$, de valeurs propres 20 et 5, donc $\lVert\mathbf{A}\rVert_2 = \sqrt{20} = 2\sqrt5 \approx 4{,}47$, atteint en $\mathbf{x} = \frac{1}{\sqrt5}(1, -2)$ : $\mathbf{A}\mathbf{x} = \frac{1}{\sqrt5}(0, -10)$, de norme $2\sqrt5$.

![Pour la matrice de lignes (2, 1) et (−2, 4) : à gauche, la boule unité L1 (un losange), son image (un parallélogramme) et le losange agrandi 5 fois, qui la touche en (1, 4) et (−1, −4) ; au milieu, le disque unité, son image (une ellipse) et le cercle de rayon 2√5 ≈ 4,47 ; à droite, le carré unité, son image et le carré agrandi 6 fois, qui la touche en (−1, 6) et (1, −6)](figures/boules_images.png)

On calcule $\lVert\cdot\rVert_1$ et $\lVert\cdot\rVert_\infty$ à la main en quelques additions ; $\lVert\cdot\rVert_2$ demande une valeur propre de $\mathbf{A}^\top\mathbf{A}$. On admet une majoration qui se calcule à la main : $\lVert\mathbf{A}\rVert_2 \le \sqrt{\lVert\mathbf{A}\rVert_1\lVert\mathbf{A}\rVert_\infty}$ (ici $4{,}47 \le \sqrt{30} \approx 5{,}48$).

### Sous-multiplicativité, transposée, matrices diagonales

> **Propriétés** (∂ M22.11 démontre les quatre premières : la sous-multiplicativité, la matrice diagonale, $\rho \le \lVert\mathbf{A}\rVert$ et la transposée en norme 2).
> - Pour chacune des trois normes induites :
>   - **sous-multiplicativité** (*submultiplicativity*) : $\lVert\mathbf{A}\mathbf{B}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{B}\rVert$, donc $\lVert\mathbf{A}^t\rVert \le \lVert\mathbf{A}\rVert^t$ ;
>   - $\lVert\operatorname{diag}(\mathbf{d})\rVert = \max_i\lvert d_i\rvert$ ;
>   - $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert$ pour $\mathbf{A}$ carrée.
> - En norme 2 seulement :
>   - $\lVert\mathbf{A}^\top\rVert_2 = \lVert\mathbf{A}\rVert_2$ (en normes 1 et ∞, la transposée les échange : $\lVert\mathbf{A}^\top\rVert_1 = \lVert\mathbf{A}\rVert_\infty$) ;
>   - pour $\mathbf{Q}$ orthogonale, $\lVert\mathbf{Q}\rVert_2 = 1$ et $\lVert\mathbf{Q}\mathbf{A}\rVert_2 = \lVert\mathbf{A}\mathbf{Q}\rVert_2 = \lVert\mathbf{A}\rVert_2$ (M12b, M12d).

Les idées : pour la sous-multiplicativité, appliquer deux fois $\lVert\mathbf{M}\mathbf{x}\rVert \le \lVert\mathbf{M}\rVert\,\lVert\mathbf{x}\rVert$ à $\mathbf{A}(\mathbf{B}\mathbf{x})$ ; pour la matrice diagonale, $\operatorname{diag}(\mathbf{d})\,\mathbf{x} = (d_1x_1, \ldots, d_nx_n)$ ; pour la transposée, $\mathbf{A}$ et $\mathbf{A}^\top$ ont les mêmes valeurs singulières (M12d) ; pour $\rho \le \lVert\mathbf{A}\rVert$, un vecteur propre $\mathbf{v}$ de $\lambda$, avec $\lvert\lambda\rvert = \rho(\mathbf{A})$, vérifie $\lVert\mathbf{A}\mathbf{v}\rVert = \lvert\lambda\rvert\,\lVert\mathbf{v}\rVert$. Ce vecteur peut être complexe : les trois normes se définissent aussi sur $\mathbb{C}^n$ (avec les modules des coordonnées), et $\lVert\mathbf{A}\mathbf{z}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{z}\rVert$ reste vrai pour $\mathbf{z} \in \mathbb{C}^n$ et $\mathbf{A}$ réelle (∂ M22.11 le justifie).

Sur l'exemple, les valeurs propres de $\mathbf{A}$ sont $3 \pm i$ (trace 6, déterminant 10), donc $\rho(\mathbf{A}) = \sqrt{10} \approx 3{,}16$, sous chacune des trois normes : $3{,}16 \le 4{,}47 \le 5 \le 6$.

**Deux usages.**
- **Une condition suffisante, vérifiable à la main.** Si l'une des normes induites vérifie $\lVert\mathbf{A}\rVert < 1$, alors $\lVert\mathbf{A}^t\rVert \le \lVert\mathbf{A}\rVert^t \to 0$, et $\mathbf{A}^t \to \mathbf{0}$. Une seule suffit : $\begin{pmatrix} 0{,}6 & 0{,}5 \\ 0 & 0{,}1 \end{pmatrix}$ a $\lVert\cdot\rVert_1 = 0{,}6$, même si $\lVert\cdot\rVert_\infty = 1{,}1$. La condition n'est pas nécessaire : la matrice du §3 a $\rho = 0{,}75$, et ses trois normes dépassent 6.
- **Majorer une trajectoire.** $\lVert\mathbf{A}^t\mathbf{x}\rVert \le \lVert\mathbf{A}\rVert^t\,\lVert\mathbf{x}\rVert$, dans **une même norme** des deux côtés. Pour $\mathbf{x} = (1, 1)$ : $\mathbf{A}\mathbf{x} = (3, 2)$, $\mathbf{A}^2\mathbf{x} = (8, 2)$, $\mathbf{A}^3\mathbf{x} = (18, -8)$. En norme 1 : $26 \le 5^3 \times 2 = 250$ ; en norme $\infty$ : $18 \le 6^3 \times 1 = 216$ ; en norme 2 : $\sqrt{388} \approx 19{,}7 \le (2\sqrt5)^3\sqrt2 \approx 126{,}5$. Ces bornes valent pour tous les $\mathbf{x}$ à la fois : elles peuvent être larges.

### Le rayon spectral et les normes : la formule de Gelfand

Appliquée à $\mathbf{A}^t$, l'inégalité $\rho \le \lVert\cdot\rVert$ donne $\rho(\mathbf{A})^t = \rho(\mathbf{A}^t) \le \lVert\mathbf{A}^t\rVert$, soit $\rho(\mathbf{A}) \le \lVert\mathbf{A}^t\rVert^{1/t}$ pour tout $t$. À la limite, c'est une égalité :

> **Formule de Gelfand** (*Gelfand's formula*, admise). Pour chacune des trois normes induites, $\lVert\mathbf{A}^t\rVert^{1/t} \to \rho(\mathbf{A})$ quand $t \to \infty$.

Le rayon spectral est donc le **facteur moyen par pas, à long terme** ; une norme borne **chaque** pas. Sur l'exemple, $\lVert\mathbf{A}^t\rVert_2^{1/t}$ vaut $4{,}47$ pour $t = 1$, $3{,}19$ pour $t = 10$, $3{,}18$ pour $t = 100$ : il descend, lentement, vers $\sqrt{10} \approx 3{,}16$. Pour une matrice normale (symétrique, orthogonale…), $\lVert\mathbf{A}\rVert_2 = \rho(\mathbf{A})$ dès $t = 1$ : c'est le cas de M19.

**Le rayon spectral n'est pas une norme.** $\mathbf{N} = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix} \ne \mathbf{0}$ a $\rho(\mathbf{N}) = 0$ ; et $\rho(\mathbf{N}) = \rho(\mathbf{N}^\top) = 0$, alors que $\mathbf{N} + \mathbf{N}^\top = \begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix}$ a pour valeurs propres $\pm3$ : pas d'inégalité triangulaire.

### La norme de Frobenius n'est pas induite

La norme de Frobenius $\lVert\mathbf{A}\rVert_F = \sqrt{\sum_{i,j}a_{ij}^2}$ (M12d) est une norme sur les matrices, sous-multiplicative elle aussi (admis), et $s_{\max}(\mathbf{A}) \le \lVert\mathbf{A}\rVert_F$ (ici $4{,}47 \le 5$). Mais elle n'est induite par **aucune** norme de vecteurs : toute norme induite donne $\lVert\mathbf{I}\rVert = 1$, alors que $\lVert\mathbf{I}_n\rVert_F = \sqrt n > 1$ dès $n \ge 2$.

💻 **Aujourd'hui en pratique** — `np.linalg.norm(A, 1)`, `np.linalg.norm(A, np.inf)` et `np.linalg.norm(A, 2)` (par une SVD) donnent les trois normes induites, `np.linalg.norm(A, "fro")` la norme de Frobenius ; **sans `ord`, `np.linalg.norm(A)` d'un tableau à deux axes est la norme de Frobenius**, pas $\lVert\mathbf{A}\rVert_2$. Le rayon spectral : `np.abs(np.linalg.eigvals(A)).max()`. Pour une très grande matrice creuse, on estime $\lVert\mathbf{A}\rVert_2$ par la méthode de la puissance sur $\mathbf{A}^\top\mathbf{A}$ (M12c §5).

⚠️ **Erreur classique.** Prendre $\rho(\mathbf{A})$ pour une norme. Prendre la plus grande valeur propre (en module) pour le plus grand allongement : ce n'est vrai qu'en norme 2, et pour une matrice normale. Mélanger les normes : $\lVert\mathbf{A}\mathbf{x}\rVert_2 \le \lVert\mathbf{A}\rVert_1\lVert\mathbf{x}\rVert_2$ est **faux** en général ($\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ a $\lVert\cdot\rVert_1 = 1$, et envoie $\frac{1}{\sqrt2}(1, 1)$, de norme 1, sur $(\sqrt2, 0)$). Confondre colonnes et lignes entre $\lVert\cdot\rVert_1$ et $\lVert\cdot\rVert_\infty$.

🔗 **Dans workbookIA** — le chapitre 22 majore des normes de produits de matrices avec $\lVert\cdot\rVert_2$ et les propriétés de ce paragraphe.

## §5 · Produits de matrices différentes, et des facteurs dans [0, 1]

### Le produit des matrices de chaque pas

Quand la matrice change à chaque pas, $\mathbf{x}_t = \mathbf{A}_t\mathbf{x}_{t-1}$ pour $t \ge 1$, l'état est $\mathbf{x}_t = \mathbf{P}_t\mathbf{x}_0$, avec
$$\mathbf{P}_t = \mathbf{A}_t\mathbf{A}_{t-1}\cdots\mathbf{A}_1 :$$
la matrice du **dernier** pas est à **gauche**, comme dans la règle de la chaîne (M17 §3).

> **Majoration.** Pour chacune des trois normes induites, $\lVert\mathbf{P}_t\rVert \le \lVert\mathbf{A}_t\rVert\,\lVert\mathbf{A}_{t-1}\rVert\cdots\lVert\mathbf{A}_1\rVert$ (la sous-multiplicativité, $t - 1$ fois). Si toutes les normes sont au plus $q$, alors $\lVert\mathbf{P}_t\rVert \le q^t$, qui tend vers 0 pour $q < 1$.

C'est ce que compare `product_norms` (🔨 M22.21) : les normes des produits et leurs majorations. Deux mises en garde.
- **La majoration peut être très large.** $\operatorname{diag}(2, 0)$ et $\operatorname{diag}(0, 2)$ ont chacune la norme 2, et leur produit est nul. Dans l'autre sens, M20 §6 minorait la plus petite valeur singulière d'un produit : $s_{\min}(\mathbf{A}\mathbf{B}) \ge s_{\min}(\mathbf{A})\,s_{\min}(\mathbf{B})$.
- **Les rayons spectraux des facteurs ne disent rien du produit.** $\mathbf{N}_1 = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$ et $\mathbf{N}_2 = \begin{pmatrix} 0 & 0 \\ 2 & 0 \end{pmatrix}$, nilpotentes, ont $\rho = 0$. Prenons-les en alternance, $\mathbf{A}_t = \mathbf{N}_1$ aux pas impairs et $\mathbf{A}_t = \mathbf{N}_2$ aux pas pairs : $\mathbf{P}_2 = \mathbf{N}_2\mathbf{N}_1 = \begin{pmatrix} 0 & 0 \\ 0 & 4 \end{pmatrix}$, et $\lVert\mathbf{P}_t\rVert_2 = 2^t$. Le produit explose, et la majoration par les normes, $2^t$, est atteinte.

### Des matrices diagonales

$\operatorname{diag}(\mathbf{a})\operatorname{diag}(\mathbf{b}) = \operatorname{diag}(\mathbf{a} \odot \mathbf{b})$, avec $\odot$ le produit coordonnée par coordonnée (Hadamard, M09a) : des matrices diagonales commutent, et leur produit est la matrice diagonale des **produits des coefficients**. Chaque coordonnée évolue seule ; la récurrence vectorielle est faite de $n$ récurrences de R5 côte à côte.

**Une récurrence affine diagonale.** $\mathbf{x}_t = \mathbf{a}_t \odot \mathbf{x}_{t-1} + \mathbf{b}_t$, avec des facteurs $\mathbf{a}_t \in [0, 1]^n$ : au pas $t$, on garde la fraction $a_{t,i}$ de la quantité $i$, et l'on ajoute $\mathbf{b}_t$. En déroulant comme au §1 (par récurrence ; le théorème du §1 supposait une matrice fixe), on obtient
$$\mathbf{x}_t = \Big(\prod_{k=1}^{t}\mathbf{a}_k\Big) \odot \mathbf{x}_0 + \sum_{k=1}^{t}\Big(\prod_{j=k+1}^{t}\mathbf{a}_j\Big) \odot \mathbf{b}_k$$
(les produits coordonnée par coordonnée ; un produit vide vaut 1). De ce qui était là au départ, il **reste** $\prod_k a_{k,i}$ ; de ce qui a été ajouté au pas $k$, il reste le produit des facteurs des pas suivants. Attention au décalage d'indice : ici $\mathbf{a}_t$ et $\mathbf{b}_t$ produisent $\mathbf{x}_t$, alors qu'au §1 l'entrée $\mathbf{u}_t$ produisait $\mathbf{x}_{t+1}$ ; c'est la convention de $\mathbf{P}_t = \mathbf{A}_t\cdots\mathbf{A}_1$ et de `product_norms`. Le §7 reviendra à celle du §1.

### Des facteurs dans [0, 1] : ce qui reste

**Exemple : trois polluants dans un lac.** Chaque mois, le lac élimine (par son exutoire, par décomposition) une fraction $\varepsilon_i$ de chaque polluant : 3 %, 8 % et 40 %. Les facteurs sont constants, $\mathbf{a} = (0{,}97 ;\ 0{,}92 ;\ 0{,}6)$. Sans nouveau rejet, il reste au bout de 24 mois $0{,}97^{24} \approx 0{,}481$, $0{,}92^{24} \approx 0{,}135$ et $0{,}6^{24} \approx 4{,}7 \times 10^{-6}$ de la quantité initiale.

- **L'approximation exponentielle.** Pour un petit $\varepsilon$, $(1 - \varepsilon)^t \approx e^{-t\varepsilon}$ (parce que $\ln(1 - \varepsilon) \approx -\varepsilon$, R6 ; c'est la limite $(1 + x/n)^n \to e^x$ de M14). Ici $e^{-0{,}72} \approx 0{,}487$, $e^{-1{,}92} \approx 0{,}147$ et $e^{-9{,}6} \approx 6{,}8 \times 10^{-5}$ : bonne pour 3 %, passable pour 8 %, fausse d'un facteur 14 pour 40 %. Comme $1 - \varepsilon \le e^{-\varepsilon}$, elle surestime toujours ce qui reste.
- **La demi-vie** (R6 §3) : la durée au bout de laquelle il reste la moitié, $t_{1/2} = \frac{\ln 2}{-\ln(1 - \varepsilon)} \approx \frac{\ln 2}{\varepsilon}$. Ici $22{,}8$, $8{,}3$ et $1{,}36$ mois (l'approximation donne $23{,}1$, $8{,}7$ et $1{,}7$).
- **Avec des rejets constants** $b_i$ par mois, chaque polluant tend vers l'équilibre $x_i^\star = \frac{b_i}{\varepsilon_i}$, le point fixe de $x = (1 - \varepsilon_i)\,x + b_i$ (R5 §5) : 0,4 tonne par mois du second polluant mène à 5 tonnes.

Avec des facteurs dans $]0, 1]$ qui changent d'un pas à l'autre, ce qui reste est $\prod_k a_k$, et son logarithme est une **somme** : $\ln\prod_k a_k = \sum_k\ln a_k$ (R6 §3). Chaque terme est négatif ou nul, puisque $0 < a_k \le 1$ : ce qui reste ne peut pas augmenter (et un facteur nul efface tout d'un coup).

### Des facteurs au hasard : la moyenne géométrique

Une plante annuelle pousse dans un milieu instable : chaque année, à pile ou face, indépendamment, sa population est multipliée par $a = 2{,}5$ (bonne année) ou par $a = 0{,}3$ (mauvaise année). Après $t$ ans, elle est multipliée par $\prod_{k=1}^t a_k$.
- **En moyenne**, elle croît : les facteurs étant indépendants, $\mathbb{E}\big[\prod_k a_k\big] = \mathbb{E}[a]^t = 1{,}4^t$ (l'espérance d'un produit de variables indépendantes, M16 §5).
- **Typiquement**, elle s'éteint : $\frac1t\ln\prod_k a_k = \frac1t\sum_k\ln a_k$ est une moyenne de variables indépendantes de même loi, qui tend vers $\mathbb{E}[\ln a] = \frac{\ln 2{,}5 + \ln 0{,}3}{2} = \frac12\ln 0{,}75 \approx -0{,}144$ (la loi des grands nombres, M02c). Donc $\prod_k a_k \approx e^{-0{,}144\,t} \to 0$.

La **moyenne géométrique** (*geometric mean*) des facteurs, $G = e^{\mathbb{E}[\ln a]} = \sqrt{2{,}5 \times 0{,}3} \approx 0{,}866$, est inférieure à leur moyenne $\mathbb{E}[a] = 1{,}4$ : c'est l'inégalité de Jensen (M06), $\ln$ étant concave. Après 16 ans, une trajectoire typique (8 bonnes années, 8 mauvaises) est multipliée par $0{,}75^8 \approx 0{,}10$, alors que la moyenne l'est par $1{,}4^{16} \approx 218$ : la moyenne est tirée par de rares trajectoires très chanceuses (16 bonnes années : un facteur $2{,}5^{16} \approx 2{,}3 \times 10^6$, avec la probabilité $2^{-16}$). **Le signe de $\mathbb{E}[\ln a]$ décide**, pas celui de $\mathbb{E}[a] - 1$. M16 §7 multipliait de même des variances d'étage en étage.

Pour des matrices aléatoires indépendantes de même loi, $\frac1t\ln\lVert\mathbf{A}_t\cdots\mathbf{A}_1\rVert$ converge aussi (théorème de Furstenberg et Kesten, admis) : c'est le **taux de croissance** (*growth rate*) du produit (on dit aussi son exposant de Lyapunov, *Lyapunov exponent*), que le 🔬 M22.24 mesure.

![À gauche, en échelle logarithmique, ce qui reste des trois polluants, 0,97ᵗ, 0,92ᵗ et 0,6ᵗ, avec en pointillés les approximations e^(−tε), et par des points les trois demi-vies ; à droite, en abscisse logarithmique, le taux de croissance (1/t) ln(a₁ ⋯ aₜ) de six trajectoires d'une population multipliée chaque année par 2,5 ou 0,3 : ils se rapprochent tous de l'espérance de ln a, environ −0,144, négative (la population s'éteint), loin du logarithme de l'espérance de a, environ 0,336](figures/facteurs_produits.png)

💻 **Aujourd'hui en pratique** — un produit de centaines de facteurs déborde vite des nombres à virgule de l'ordinateur (en `float64`, vers $10^{-308}$ et $10^{308}$). On additionne alors des logarithmes ; pour un produit de matrices appliqué à un vecteur, on renormalise à chaque pas ($\mathbf{x} \leftarrow \mathbf{A}_k\mathbf{x}$, on cumule $\ln\lVert\mathbf{x}\rVert$, puis $\mathbf{x} \leftarrow \mathbf{x}/\lVert\mathbf{x}\rVert$).

⚠️ **Erreur classique.** Conclure qu'un produit de facteurs aléatoires grandit parce que $\mathbb{E}[a] > 1$. Mettre le premier facteur à gauche du produit. Ou croire que des facteurs de rayon spectral $< 1$ donnent un produit qui tend vers 0 : seules les normes se multiplient.

## §6 · Récurrences non linéaires : des produits de jacobiennes le long d'une trajectoire

### La jacobienne d'un état par rapport à un état antérieur

Soit $f : \mathbb{R}^n \to \mathbb{R}^n$ dérivable, et la trajectoire $\mathbf{x}_{t+1} = f(\mathbf{x}_t)$. L'état $\mathbf{x}_T$ dépend de $\mathbf{x}_t$ par $T - t$ applications de $f$. La règle de la chaîne pour plusieurs étages (M17 §3) donne :

> $$\frac{\partial\mathbf{x}_T}{\partial\mathbf{x}_t} = \mathbf{J}_f(\mathbf{x}_{T-1})\,\mathbf{J}_f(\mathbf{x}_{T-2})\cdots\mathbf{J}_f(\mathbf{x}_t),$$
> une matrice $(n, n)$ : chaque jacobienne est évaluée au point où $f$ est appliquée, et celle du dernier pas est à gauche.

C'est un produit de matrices différentes, celui du §5 avec $\mathbf{A}_k = \mathbf{J}_f(\mathbf{x}_{k-1})$. Au premier ordre (M17 §1), un petit écart $\boldsymbol{\delta}$ sur $\mathbf{x}_t$ déplace $\mathbf{x}_T$ d'environ $\frac{\partial\mathbf{x}_T}{\partial\mathbf{x}_t}\boldsymbol{\delta}$. La majoration du §5 s'applique : $\big\lVert\frac{\partial\mathbf{x}_T}{\partial\mathbf{x}_t}\big\rVert \le \prod_{k=t}^{T-1}\lVert\mathbf{J}_f(\mathbf{x}_k)\rVert$, et si $\lVert\mathbf{J}_f\rVert \le q$ le long de la trajectoire, $\le q^{T-t}$. Pour une application affine de partie linéaire $\mathbf{A}$, toutes les jacobiennes valent $\mathbf{A}$ et le produit est $\mathbf{A}^{T-t}$ : le §3. Avec une entrée, $\mathbf{x}_{t+1} = f(\mathbf{x}_t, \mathbf{u}_t)$, on prend les jacobiennes par rapport à $\mathbf{x}$, aux points $(\mathbf{x}_k, \mathbf{u}_k)$.

M17 §6 faisait ce calcul en dimension 1 (un produit de dérivées) ; M20 §6, avec des facteurs proches de l'identité. Ici les facteurs sont des matrices quelconques, qui en général ne commutent pas.

### Un exemple : une application du plan

$$f(x, y) = (x^2 - y^2 - 0{,}24,\ 2xy), \qquad \mathbf{J}_f(x, y) = \begin{pmatrix} 2x & -2y \\ 2y & 2x \end{pmatrix}.$$
En notation complexe, $z = x + iy$ : comme $(x + iy)^2 = x^2 - y^2 + 2ixy$, c'est $f(z) = z^2 - 0{,}24$, et la jacobienne en $z$ est la matrice de la multiplication par $2z$ (§2) : une rotation d'angle $\arg z$ et une homothétie de rapport $2\lvert z\rvert$, donc $\lVert\mathbf{J}_f\rVert_2 = 2\lvert z\rvert$.

Depuis $z_0 = 0{,}2 + 0{,}4\,i$ : $z_1 = 0{,}04 - 0{,}16 - 0{,}24 + 0{,}16\,i = -0{,}36 + 0{,}16\,i$, puis $z_2 = -0{,}136 - 0{,}1152\,i$, $z_3 \approx -0{,}2348 + 0{,}0313\,i$… La trajectoire s'approche de $-0{,}2$. Les jacobiennes :
$$\mathbf{J}_0 = \begin{pmatrix} 0{,}4 & -0{,}8 \\ 0{,}8 & 0{,}4 \end{pmatrix},\quad \mathbf{J}_1 = \begin{pmatrix} -0{,}72 & -0{,}32 \\ 0{,}32 & -0{,}72 \end{pmatrix},\quad \mathbf{J}_2 = \begin{pmatrix} -0{,}272 & 0{,}2304 \\ -0{,}2304 & -0{,}272 \end{pmatrix},$$
de normes $0{,}894$, $0{,}788$ et $0{,}356$. La jacobienne de $\mathbf{x}_0 \mapsto \mathbf{x}_3$ est $\mathbf{J}_2\mathbf{J}_1\mathbf{J}_0$, la multiplication par $8z_0z_1z_2 \approx 0{,}0447 + 0{,}2472\,i$, de norme $0{,}251$ : exactement le produit des trois normes. C'est une **exception** : ces jacobiennes sont des rotations-homothéties ; chacune multiplie **toutes** les longueurs par le même facteur $2\lvert z_k\rvert$, donc leur produit aussi, et la majoration est atteinte. Commuter n'y suffirait pas : $\operatorname{diag}(2, 0)$ et $\operatorname{diag}(0, 2)$ commutent, et leur produit est nul (§5). En général, l'ordre compte, et le produit des normes surestime la norme du produit.

### Applications contractantes et points fixes

> **Définition.** $f$ est **contractante** (*contraction*) sur une partie $\mathcal{D}$ de $\mathbb{R}^n$ qu'elle envoie dans elle-même, pour une norme, s'il existe $q < 1$ tel que $\lVert f(\mathbf{x}) - f(\tilde{\mathbf{x}})\rVert \le q\,\lVert\mathbf{x} - \tilde{\mathbf{x}}\rVert$ pour tous $\mathbf{x}, \tilde{\mathbf{x}} \in \mathcal{D}$.
>
> **Propriété** (∂ M22.14). Deux trajectoires $(\mathbf{x}_t)$ et $(\tilde{\mathbf{x}}_t)$ qui partent de $\mathcal{D}$ se rapprochent alors géométriquement : $\lVert\mathbf{x}_t - \tilde{\mathbf{x}}_t\rVert \le q^t\,\lVert\mathbf{x}_0 - \tilde{\mathbf{x}}_0\rVert$. La récurrence **oublie son point de départ**. En particulier, $f$ a au plus un **point fixe** (*fixed point*) $\mathbf{x}^\star = f(\mathbf{x}^\star)$ dans $\mathcal{D}$, et s'il existe, toute trajectoire issue de $\mathcal{D}$ y converge : $\lVert\mathbf{x}_t - \mathbf{x}^\star\rVert \le q^t\lVert\mathbf{x}_0 - \mathbf{x}^\star\rVert$.

On admet que ce point fixe existe quand $\mathcal{D}$ est fermé et non vide (théorème du point fixe de Banach).

**Lire une jacobienne.**
- Si $\lVert\mathbf{J}_f(\mathbf{x})\rVert \le q < 1$ en tout point d'une partie convexe $\mathcal{D}$ que $f$ envoie dans elle-même, $f$ y est contractante de facteur $q$ (inégalité des accroissements finis, admise).
- En un point fixe, si $\rho\big(\mathbf{J}_f(\mathbf{x}^\star)\big) < 1$, les trajectoires qui partent assez près convergent vers $\mathbf{x}^\star$ : un point fixe **attractif** (*attracting fixed point* ; admis ; c'est le §3 pour l'approximation linéaire). Si $\rho\big(\mathbf{J}_f(\mathbf{x}^\star)\big) > 1$, des trajectoires voisines s'en éloignent : le point fixe est **instable**. Il est **répulsif** (*repelling fixed point* ; M17 disait « repoussant » en dimension 1) quand **toutes** les valeurs propres de $\mathbf{J}_f(\mathbf{x}^\star)$ sont de module $> 1$ : alors toutes les trajectoires voisines (sauf celle du point fixe lui-même) finissent par s'en éloigner. Pour $f(\mathbf{x}) = \operatorname{diag}(2 ;\ 0{,}5)\,\mathbf{x}$, de point fixe $\mathbf{0}$ et de rayon spectral 2, le point fixe est instable mais pas répulsif : les points de l'axe vertical convergent vers $\mathbf{0}$.
- Attention : $\rho\big(\mathbf{J}_f(\mathbf{x}^\star)\big) < 1$ ne fait pas de $f$ une contraction pour $\lVert\cdot\rVert_2$ près de $\mathbf{x}^\star$ quand la jacobienne n'est pas normale : l'écart peut d'abord grandir (§3), puis décroître.

**Sur l'exemple.** Les points fixes vérifient $z^2 - z - 0{,}24 = 0$ : $z = -0{,}2$ et $z = 1{,}2$. En $-0{,}2$, la jacobienne est la multiplication par $-0{,}4$ : $\rho = 0{,}4$, point fixe attractif, et l'écart change de signe à chaque pas. En $1{,}2$, la multiplication par $2{,}4$, de valeurs propres $2{,}4$ et $2{,}4$ : répulsif. Sur le disque $\mathcal{D} = \{\lvert z\rvert \le 0{,}46\}$, $\lvert z^2 - 0{,}24\rvert \le 0{,}46^2 + 0{,}24 = 0{,}4516 \le 0{,}46$ : $f$ envoie $\mathcal{D}$ dans lui-même, et $\lvert f(z) - f(w)\rvert = \lvert z + w\rvert\,\lvert z - w\rvert \le 0{,}92\,\lvert z - w\rvert$ : une contraction de facteur $0{,}92$. Comme $\lvert z_0\rvert \approx 0{,}447$, $\lvert z_t + 0{,}2\rvert \le 0{,}92^t\,\lvert z_0 + 0{,}2\rvert$ ; près du point fixe, l'écart décroît en fait comme $0{,}4^t$.

![À gauche, la trajectoire de z ↦ z² − 0,24 depuis 0,2 + 0,4i, dans le disque de rayon 0,46 où l'application est contractante, vers le point fixe attractif −0,2 ; le point fixe répulsif 1,2 est hors du disque. À droite, en échelle logarithmique, la norme du produit des jacobiennes le long de la trajectoire, égale ici au produit des normes, la borne 0,92ᵗ du disque, et la pente 0,4ᵗ du point fixe](figures/trajectoire_jacobiennes.png)

⚠️ **Erreur classique.** Multiplier les jacobiennes dans l'ordre du temps, $\mathbf{J}_f(\mathbf{x}_t)$ à gauche (🐛 M22.26) ; les évaluer aux mauvais points ($\mathbf{x}_{k+1}$ au lieu de $\mathbf{x}_k$) ; ou croire qu'une jacobienne de norme $< 1$ **au point fixe** rend $f$ contractante partout.

🔗 **Dans workbookIA** — le chapitre 22 itère une même application non linéaire le long d'une séquence, et regarde comment un état dépend des états plus anciens : par des produits de jacobiennes comme celui-ci.

## §7 · La sensibilité à un paramètre utilisé à chaque pas : une somme sur le temps

### Une récurrence pour la dérivée

Soit $\mathbf{x}_{t+1} = f(\mathbf{x}_t, \beta)$, où le paramètre réel $\beta$ sert **à chaque pas**, et où $\mathbf{x}_0$ ne dépend pas de $\beta$. Comment $\mathbf{x}_T$ change-t-il quand $\beta$ change ? On note
$$\mathbf{s}_t = \frac{\partial\mathbf{x}_t}{\partial\beta} \in \mathbb{R}^n \qquad (\text{la **sensibilité**, } \textit{sensitivity}), \qquad \mathbf{s}_0 = \mathbf{0}.$$
En dérivant $\mathbf{x}_{t+1} = f(\mathbf{x}_t, \beta)$ par rapport à $\beta$ (M17 §3), deux chemins apparaissent (M18 §2) : $\beta$ agit sur $\mathbf{x}_{t+1}$ à travers $\mathbf{x}_t$, et directement, au pas $t$.

> $$\mathbf{s}_{t+1} = \mathbf{J}_t\,\mathbf{s}_t + \mathbf{b}_t, \qquad \mathbf{J}_t = \frac{\partial f}{\partial\mathbf{x}}(\mathbf{x}_t, \beta) \ (\text{forme } (n, n)), \qquad \mathbf{b}_t = \frac{\partial f}{\partial\beta}(\mathbf{x}_t, \beta) \in \mathbb{R}^n .$$

La sensibilité suit une **récurrence linéaire avec entrée** (§1), dont la matrice $\mathbf{J}_t$ change à chaque pas (§5) et dont l'entrée est $\mathbf{b}_t$.

### La somme sur le temps

> **Propriété** (∂ M22.15). $$\mathbf{s}_T = \sum_{k=0}^{T-1}\mathbf{J}_{T-1}\mathbf{J}_{T-2}\cdots\mathbf{J}_{k+1}\,\mathbf{b}_k,$$ le produit étant l'identité pour $k = T - 1$.

Comment la lire : le terme $k$ est l'effet de l'usage de $\beta$ au pas $k$, $\mathbf{b}_k$, porté jusqu'au pas $T$ par le produit des jacobiennes des pas suivants (§6). C'est la somme sur les chemins de M18 : un chemin par pas où $\beta$ sert. Quand les jacobiennes sont toutes égales à une matrice $\mathbf{A}$ (un modèle affine en $\mathbf{x}$), on retrouve exactement la formule du §1, $\mathbf{s}_T = \sum_k\mathbf{A}^{T-1-k}\mathbf{b}_k$. Pour un paramètre vectoriel, chaque coordonnée a sa sensibilité et sa somme. Le même schéma s'applique à un capital placé à taux fixe, dérivé par rapport au taux (✏️ M22.9).

### Exemple : une pêcherie

Le stock de poissons $x_t$ (en milliers de tonnes) évolue chaque année selon le **modèle de Schaefer** : une croissance naturelle logistique, de capacité 100, et une pêche qui prélève la fraction $\beta$ du stock :
$$x_{t+1} = f(x_t, \beta) = x_t + 0{,}6\,x_t\Big(1 - \frac{x_t}{100}\Big) - \beta\,x_t .$$
Ici $J(x) = \frac{\partial f}{\partial x} = 1{,}6 - 0{,}012\,x - \beta$ et $b(x) = \frac{\partial f}{\partial\beta} = -x$. Avec $\beta = 0{,}2$ et $x_0 = 50$ :

| $t$ | $x_t$ | $J_t = 1{,}4 - 0{,}012\,x_t$ | $b_t = -x_t$ | $s_t$ |
|---|---|---|---|---|
| 0 | 50 | 0,8 | −50 | 0 |
| 1 | 55 | 0,74 | −55 | −50 |
| 2 | 58,85 | 0,6938 | −58,85 | 0,74 × (−50) − 55 = −92 |
| 3 | 61,61 | | | 0,6938 × (−92) − 58,85 ≈ −122,68 |

En somme sur le temps : $s_3 = b_2 + J_2b_1 + J_2J_1b_0 = -58{,}85 - 38{,}16 - 25{,}67 \approx -122{,}68$, un terme par année où le taux a servi. Lecture : passer de $\beta = 0{,}20$ à $0{,}21$ change $x_3$ d'environ $0{,}01 \times (-122{,}68) \approx -1{,}23$ millier de tonnes (le calcul exact donne $-1{,}22$).

### Tronquer la somme

Pour économiser des calculs, on peut **tronquer** la somme (*truncation*) : ne garder que les $K$ derniers termes, $k = T - K, \ldots, T - 1$ : $K$ produits de jacobiennes au lieu de $T$. L'erreur commise est exactement la somme des termes retirés ; il faut l'estimer avant de s'en contenter.

⚠️ **Erreur classique.** Oublier le terme direct $\mathbf{b}_t$ (seul le chemin à travers $\mathbf{x}_t$ resterait, et $\mathbf{s}_t$ resterait nul), ou le chemin indirect (on n'aurait que $\mathbf{b}_{T-1}$) ; évaluer $\mathbf{J}_t$ et $\mathbf{b}_t$ ailleurs qu'au point $\mathbf{x}_t$ de la trajectoire.

🔗 **Dans workbookIA** — au chapitre 22, une même matrice sert à chaque pas d'une séquence ; la dérivée par rapport à elle se calcule comme une somme sur le temps de ce type.

## §8 · Borner un vecteur fait de plusieurs blocs

### La norme d'un vecteur fait de blocs

Un vecteur peut être fait de plusieurs **blocs** mis bout à bout (un *block vector*) : $\mathbf{w} = (\mathbf{w}_1, \ldots, \mathbf{w}_p)$, avec $\mathbf{w}_k \in \mathbb{R}^{n_k}$. Sa norme L2 regroupe les carrés de toutes ses coordonnées, bloc par bloc :
$$\lVert\mathbf{w}\rVert^2 = \lVert\mathbf{w}_1\rVert^2 + \cdots + \lVert\mathbf{w}_p\rVert^2, \qquad \lVert\mathbf{w}\rVert = \sqrt{\textstyle\sum_k\lVert\mathbf{w}_k\rVert^2},$$
la **norme globale** (*global norm*) : le théorème de Pythagore, appliqué aux normes des blocs.

**Exemple.** Un chariot sur un rail (une vitesse) et deux drones (trois coordonnées chacun) : $\mathbf{w}_1 = (-2)$, $\mathbf{w}_2 = (4, 4, -2)$, $\mathbf{w}_3 = (-4, 7, 4)$ m/s, de normes 2, 6 et 9. La norme globale vaut $\sqrt{4 + 36 + 81} = 11$, pas $2 + 6 + 9 = 17$. (Pour des masses égales $m$, $\frac12 m\lVert\mathbf{w}\rVert^2$ est l'énergie cinétique de l'ensemble.)

### Ramener sous un seuil : le tout, ou chaque bloc

Une consigne de sécurité impose un **seuil** (*threshold*) : $\lVert\mathbf{w}\rVert \le c = 4{,}4$. Deux façons de ralentir :

- **Le tout** : $\mathbf{w} \mapsto \mathbf{w}\,\min\big(1, \frac{c}{\lVert\mathbf{w}\rVert}\big)$, la projection sur la boule de rayon $c$ de M19 §8, dans l'espace de toutes les coordonnées (un vecteur nul reste nul : il n'y a rien à ramener). Ici, tout est multiplié par $\frac{4{,}4}{11} = 0{,}4$ : $(-0{,}8)$, $(1{,}6 ;\ 1{,}6 ;\ -0{,}8)$, $(-1{,}6 ;\ 2{,}8 ;\ 1{,}6)$, de norme globale $4{,}4$. La **direction** est gardée : les trois engins ralentissent dans la même proportion, et les normes des blocs restent dans le rapport $2 : 6 : 9$.
- **Chaque bloc** : $\mathbf{w}_k \mapsto \mathbf{w}_k\,\min\big(1, \frac{c}{\lVert\mathbf{w}_k\rVert}\big)$. Un bloc nul reste nul. Ici, le chariot ne bouge pas ($2 \le 4{,}4$), les drones sont ramenés à la norme $4{,}4$ : normes $2$ ; $4{,}4$ ; $4{,}4$, et une norme globale $\sqrt{4 + 2 \times 4{,}4^2} \approx 6{,}54 > c$. La direction a tourné d'environ 13° (cosinus $0{,}974$) : le chariot va désormais, en proportion, bien plus vite que les drones.

Pour garantir $\lVert\mathbf{w}\rVert \le c$ bloc par bloc, il faudrait un seuil $\frac{c}{\sqrt p}$ par bloc ($p$ blocs de normes au plus $\frac{c}{\sqrt p}$ donnent au plus $c$) : ici $\frac{4{,}4}{\sqrt3} \approx 2{,}54$, d'où des normes 2 ; 2,54 ; 2,54 et une norme globale $\approx 4{,}11$, sous le seuil, mais toujours dans une autre direction.

> **Propriété.** Ramener le tout sous $c$ garde la direction de $\mathbf{w}$ et les proportions entre ses blocs. Ramener chaque bloc sous $c$ ne la garde que si tous les blocs sont multipliés par le même facteur (les blocs non nuls ; par exemple, si aucun ne dépasse, ou s'ils ont tous la même norme), et laisse une norme globale qui peut atteindre $c\sqrt p$.

Les deux opérations sont des projections (M19 §8), sur deux ensembles convexes différents : la boule de rayon $c$, ou le produit des boules de rayon $c$ de chaque bloc. Le pavé de M19 est le cas de blocs d'une seule coordonnée. Elles ne touchent pas un vecteur déjà dans l'ensemble, et, ici, n'allongent jamais : chaque bloc est multiplié par un facteur au plus égal à 1 (une projection sur un ensemble convexe qui ne contient pas $\mathbf{0}$ peut, elle, allonger un vecteur).

⚠️ **Erreur classique.** Appliquer le seuil bloc par bloc en croyant borner le tout ; calculer la norme globale comme la somme des normes des blocs (17 au lieu de 11) ou comme leur maximum ; multiplier par $\frac{c}{\lVert\mathbf{w}\rVert}$ même quand $\lVert\mathbf{w}\rVert < c$, ce qui allonge le vecteur.

🔗 **Dans workbookIA** — les chapitres 19 et 22 ramènent sous un seuil la norme globale du gradient, un vecteur qui a une coordonnée par paramètre du modèle, rangées bloc par bloc (un bloc par tableau de poids) : c'est le clipping par la norme, dont ce paragraphe donne la géométrie.

## Les pièges classiques ⚠️ (récapitulatif)

- **La solution d'une récurrence avec entrée.** $\mathbf{A}^{t-1-k}$ devant $\mathbf{B}\mathbf{u}_k$, pas $\mathbf{A}^{t-k}$ ; la réponse libre $\mathbf{A}^t\mathbf{x}_0$ ; un pas de décalage entre la sortie et la convolution $\mathbf{h} * \mathbf{u}$.
- **Le module, pas la partie réelle.** Les valeurs propres complexes d'une matrice $2 \times 2$ ont pour module $\sqrt{\det\mathbf{A}}$, pas $\frac{\operatorname{tr}\mathbf{A}}{2}$.
- **Le long terme et les premiers pas.** $\rho(\mathbf{A}) < 1$ garantit $\mathbf{A}^t \to \mathbf{0}$, pas une décroissance à chaque pas : une matrice non normale peut d'abord grandir beaucoup.
- **$\rho = 1$** ne dit pas si les puissances restent bornées : une rotation, oui ; un cisaillement, non.
- **Le rayon spectral n'est pas une norme.** $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert$ pour les trois normes induites, avec égalité en norme 2 quand $\mathbf{A}$ est normale (pas en normes 1 et ∞ : $\mathbf{R}_{\pi/4}$ a $\rho = 1$ et $\lVert\mathbf{R}_{\pi/4}\rVert_1 = \sqrt2$) ; une matrice non nulle peut avoir $\rho = 0$.
- **Colonnes ou lignes.** $\lVert\cdot\rVert_1$ : les colonnes ; $\lVert\cdot\rVert_\infty$ : les lignes ; et toujours la même norme des deux côtés de $\lVert\mathbf{A}\mathbf{x}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{x}\rVert$.
- **`np.linalg.norm(A)`** sans `ord` est la norme de Frobenius, qui n'est pas induite.
- **Les produits.** Le dernier facteur à gauche ; seules les normes se multiplient, pas les rayons spectraux ; la majoration peut être très large.
- **Des facteurs aléatoires** : c'est le signe de $\mathbb{E}[\ln a]$ qui décide, pas $\mathbb{E}[a]$.
- **Les jacobiennes** se multiplient dans l'ordre inverse du temps, chacune évaluée en son point.
- **La sensibilité** a deux chemins : à travers l'état, et directement à chaque pas.
- **Le tout ou chaque bloc.** La norme globale est $\sqrt{\sum_k\lVert\mathbf{w}_k\rVert^2}$ ; seul le seuil appliqué au tout garde la direction.

## Et maintenant

**Dans ce dépôt** : l'examen blanc CP5 clôt la partie V. Plus loin, M26 retrouvera les puissances d'une matrice (une matrice de transition) et un point fixe, et MB3 les nombres complexes et les rotations.

**Dans workbookIA** : le chapitre 22 fait passer une séquence, élément après élément, dans une même cellule qui met à jour un état ; il regarde comment l'information et les dérivées se propagent le long de longues séquences, compare des architectures qui les conservent plus ou moins bien, et limite la norme de son gradient. Les chapitres 23 et 24 passent à PyTorch.

## Pour aller plus loin

- MML §4.2 (le 📖 M22.17) ; MML §3.9 (*Rotations*), que MB3 lira.
- L. N. Trefethen et M. Embree, *Spectra and Pseudospectra: The Behavior of Nonnormal Matrices and Operators*, Princeton University Press, 2005 : la croissance transitoire des matrices non normales, et ce que les valeurs propres ne disent pas.
- R. A. Horn et C. R. Johnson, *Matrix Analysis*, 2ᵉ éd., Cambridge University Press, 2013, chapitre 5 : les normes de matrices, les normes induites et la formule de Gelfand.
- H. Furstenberg et H. Kesten, « Products of random matrices », *The Annals of Mathematical Statistics* 31 (1960), p. 457–469 : le taux de croissance d'un produit de matrices aléatoires.
- La documentation de NumPy (`numpy.linalg.norm`, `numpy.linalg.eigvals`, `numpy.linalg.matrix_power`) et de SciPy (`scipy.signal.dlsim`, `scipy.signal.lfilter`).
- `annexes/symboles.md` (lire $\rho(\mathbf{A})$, $\lVert\mathbf{A}\rVert_1$, $\lVert\mathbf{A}\rVert_\infty$, $e^{i\theta}$, $\arg z$, $\odot$ et $\prod$ à voix haute), `annexes/formulaire.md` et `annexes/erreurs_frequentes.md`.
