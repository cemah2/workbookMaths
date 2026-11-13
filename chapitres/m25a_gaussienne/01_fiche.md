# M25a · Gaussienne multivariée, conditionnement et divergence KL — fiche de cours

> L'erreur d'un récepteur GPS, les retards d'un bus à plusieurs arrêts, les poids mal connus d'un modèle linéaire : quand plusieurs grandeurs incertaines varient **ensemble**, la loi normale devient la **loi normale multivariée** $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. Ce chapitre écrit sa densité, la tire par Cholesky et lit sa géométrie ; il la conditionne par le **complément de Schur**, fait la règle de Bayes avec elle jusqu'à la **régression linéaire bayésienne**, l'estime par le maximum de vraisemblance, définit la **divergence KL** entre deux lois continues, et finit par l'**interpolation sphérique**. Le chapitre 25 de workbookIA appliquera ces outils aux modèles génératifs.

| | |
|---|---|
| **Sections** | §1 à §8 |
| **Temps total estimé** | ≈ 17,4 h : lecture et calculs de la fiche ≈ 3 h 05, exercices ≈ 13 h 30, 24 flashcards ≈ 50 min (parcours essentiel ≈ 13,2 h) |
| **Prérequis** | R9 (cosinus, sinus, radians) ; M02a (intégration par parties, intégrales impropres) ; M02b (loi normale, changement de variable en dimension 1, théorème de transfert, intégrale double et coordonnées polaires) ; M02c (matrice de covariance empirique, estimateur en $1/n$) ; M04 (règle de Bayes : a priori, vraisemblance, évidence, a posteriori) ; M05a (convexité : une fonction convexe est au-dessus de ses tangentes) ; M06 (divergence KL discrète, inégalité de Jensen discrète, entropie) ; M07 (produit scalaire, angle, norme d'un vecteur gaussien en grande dimension) ; M09a (inverse d'une matrice, systèmes) ; M09b (ridge vue comme un MAP, régression vue comme un maximum de vraisemblance) ; M12b (base orthonormée d'un plan, Gram-Schmidt) ; M12c (déterminant, trace, théorème spectral, matrices définies positives, Cholesky, covariance $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$, blanchiment, distance de Mahalanobis) ; M13a (maximum de vraisemblance, indépendance conditionnelle) ; M17 (jacobienne) ; M18 (gradients de $\ln\det$ et de la trace par rapport à une matrice) ; M22 (forme exponentielle des nombres complexes) |
| **Fichiers du chapitre** | `02_exercices.md` (quiz, papier) · `03_notebook.ipynb` · `04_indices.md` · `05_solutions.md` et `05_solutions.ipynb` · `06_mes_reponses.md` · `flashcards.csv` |
| **mymath** | `gaussian.py` : `mvn_logpdf`, `sample_mvn`, `schur_complement`, `condition_gaussian`, `linreg_posterior` |
| **MML** | §6.5 (*Gaussian Distribution*) ; la fin de §6.7.2 (*Change of Variables* : Théorème 6.16, Exemple 6.17) ; §9.3 (*Bayesian Linear Regression*) |

## Comment utiliser ce chapitre

**Ordre conseillé.**
1. `python tools/start_chapter.py M25a` (sur Colab : `00_setup/COLAB.md` §2) : il copie le notebook, ta feuille de réponses et le squelette `mymath/gaussian.py`.
2. Section par section : lis **crayon en main**, refais chaque calcul ; lis le passage de MML que le guide ci-dessous place après la section ; puis fais les exercices de la section, quiz 🧠 d'abord.
3. Les exercices ✏️ et 🔗 se font sur papier, dans ta copie de `06_mes_reponses.md`, puis se vérifient dans la **partie 0** du notebook. Les démonstrations ∂ se rédigent dans ta copie et se jugent avec la grille de relecture de `05_solutions.md`.

Le §8 (l'interpolation sphérique) ne demande que R9, M07, M12b et M22 : il peut se lire à part.

| Section | Quiz 🧠 et rappels 🔁 | Papier et réflexion | Notebook |
|---|---|---|---|
| §1 La densité | Q1 | M25a.1 ✏️, M25a.10 ∂, M25a.16 🔗, M25a.17 📖 | M25a.20 🔨, M25a.24 📦, M25a.28 🐛 |
| §2 Transformations affines, μ + Lε | Q2, R1, R2 | M25a.2 ✏️, M25a.10 ∂, M25a.16 🔗, M25a.17 📖, M25a.E1 💼 | M25a.21 🔨, M25a.28 🐛, M25a.29 🛠️ |
| §3 Ellipses, masse, loi de la norme | Q3, R1, R2 | M25a.3 ✏️, M25a.11 ∂ | M25a.25 🔮, M25a.27 🎨 |
| §4 Blocs, Schur, conditionnement | Q4 | M25a.4 ✏️, M25a.17 📖, M25a.19 🗣️ | M25a.22 🔨, M25a.26 🔬, M25a.27 🎨, M25a.28 🐛, M25a.30 🏆 |
| §5 Bayes avec des gaussiennes | Q5 | M25a.5 ✏️, M25a.6 ✏️, M25a.17 📖, M25a.18 📖 | M25a.23 🔨 |
| §6 Maximum de vraisemblance | Q6, R3 | M25a.12 ∂ | M25a.24 📦 |
| §7 La divergence KL continue | Q7 | M25a.7 ✏️, M25a.8 ✏️, M25a.13 ∂, M25a.14 ∂ | M25a.24 📦 |
| §8 L'interpolation sphérique | Q8 | M25a.9 ✏️, M25a.15 ∂ | |

Parcours essentiel : tout sauf M25a.Q6, M25a.R3, M25a.6, M25a.12, M25a.17, M25a.18, M25a.E1, M25a.23, M25a.26, M25a.29 et M25a.30.

## Guide de lecture de MML

MML admet la plupart des formules de §6.5 ; la fiche les démontre ou dit d'où elles viennent. Lis chaque morceau **après** la partie de la fiche qui le prépare.

- **Après le §1** : le début de **§6.5** (la densité (6.63), la figure 6.7, et la figure 6.8, des tirages en dimension 1 et 2).
- **Après le §2** : **§6.5.3** et **§6.5.4** (sommes, images linéaires, tirage par Cholesky), puis la **fin de §6.7.2** : le **Théorème 6.16** et l'**Exemple 6.17**, que le 📖 M25a.17 te fait refaire avec tes nombres. Saute le **Théorème 6.12** (les moments d'un mélange) et le paragraphe sur la loi de la variance totale (M25b) ; survole (6.89) à (6.91).
- **Après le §4** : **§6.5.1**, (6.64) à (6.68), que MML admet ; l'**Exemple 6.6** et la figure 6.9 se lisent sans refaire leurs nombres. La remarque sur le filtre de Kalman, les processus gaussiens et l'ACP probabiliste annonce M25b.
- **Pendant le §5**, après « Le produit de deux densités » : **§6.5.2**.
- **Après le §5** : **§9.3** en entier (le modèle (9.35), les prédictions a priori (9.37) à (9.40), le **Théorème 9.1** démontré en complétant le carré, la recette (9.51) à (9.56), les prédictions a posteriori (9.57), la vraisemblance marginale (9.60) à (9.64)) ; les Exemples 9.7 et 9.8 se regardent sans être refaits.

Pour les §3, §6, §7 et §8, la fiche est le cours : MML ne traite ni la masse d'une ellipse, ni la loi de la norme, ni l'entropie différentielle, ni le slerp ; il ne fait le maximum de vraisemblance de $\boldsymbol{\Sigma}$ qu'au §11.2.3 (Théorème 11.2, avec des poids : M25b), et ne fait que nommer la divergence KL (à la fin de §6.4.6). Exercices du livre conseillés : 6.10 (le produit de deux densités), 6.12 (un modèle linéaire gaussien : refais la dérivation en détail, puis la partie c) et, pour aller plus loin, 6.5 (un pas du filtre de Kalman).

📐 **Notations.**
- MML note $D$ la dimension, $N$ le nombre de données, $|\boldsymbol{\Sigma}|$ le déterminant et $\log$ le logarithme népérien ; la fiche écrit $d$, $n$, $\det\boldsymbol{\Sigma}$ et $\ln$.
- Le second paramètre de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ est une **covariance** ; $\mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}, \boldsymbol{\Sigma})$ est la valeur de sa densité en $\mathbf{x}$. Le gras $\boldsymbol{\Sigma}$ est la covariance, le $\sum$ d'une somme n'est jamais en gras.
- La distance de Mahalanobis s'écrit $\Delta(\mathbf{x})$ : la lettre $d$ est réservée à la dimension.
- $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ est la **matrice de précision** (§4). M12c notait $\boldsymbol{\Lambda}$ la diagonale des valeurs propres ; ici, on écrit $\boldsymbol{\Sigma} = \mathbf{Q}\operatorname{diag}(\lambda_1, \ldots, \lambda_d)\mathbf{Q}^\top$, avec $\lambda_1 \ge \cdots \ge \lambda_d$.
- $\mathbf{L}$ est le facteur de Cholesky ($\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$, M12c) ; $\boldsymbol{\varepsilon}$ est toujours un vecteur de loi $\mathcal{N}(\mathbf{0}, \mathbf{I})$ ; le bruit d'un modèle, que MML note $\boldsymbol{\epsilon}$, s'écrit $\mathbf{w}$.
- Les blocs s'indexent $a$ et $b$ ($\mathbf{x}_a$, $\boldsymbol{\Sigma}_{ab}$), comme dans la docstring de `condition_gaussian` ; MML (6.64) les appelle $\mathbf{x}$ et $\mathbf{y}$ ($\boldsymbol{\Sigma}_{xy}$, $\boldsymbol{\mu}_{x \mid y}$).
- Les vecteurs de la fiche sont des **colonnes** ; dans NumPy et `mymath`, plusieurs vecteurs sont les **lignes** d'un tableau $(n, d)$ (§2).

Vocabulaire anglais de ce chapitre : *multivariate normal distribution*, *covariance matrix*, *standard normal distribution*, *Gaussian random vector*, *Mahalanobis distance*, *log-density*, *degenerate distribution*, *change of variables*, *Jacobian determinant*, *Cholesky factor*, *sampling*, *whitening*, *level set*, *chi-squared distribution*, *chi distribution*, *Rayleigh distribution*, *mode*, *block matrix*, *Schur complement*, *marginal distribution*, *conditional distribution*, *cross-covariance*, *precision matrix*, *conditional independence*, *linear Gaussian model*, *Kalman filter*, *Bayesian linear regression*, *posterior predictive distribution*, *marginal likelihood*, *evidence*, *completing the square*, *scatter matrix*, *Kullback-Leibler divergence*, *support*, *differential entropy*, *Jensen's inequality*, *spherical linear interpolation (slerp)*, *great circle*, *chord*.

## Objectifs d'apprentissage

À la fin du chapitre, tu sais :
- **écrire** et **évaluer** la densité et la log-densité d'une loi normale multivariée, et y **lire** le rôle de $\det\boldsymbol{\Sigma}$ et de la distance de Mahalanobis ;
- **trouver** la loi d'une transformation affine ou d'une somme de vecteurs gaussiens, et **tirer** un vecteur de loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ sous la forme $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ ;
- **tracer** les ellipses de niveau d'une gaussienne, **calculer** la masse d'une ellipse en dimension 2, et **décrire** la loi de la norme d'un vecteur gaussien en dimension $d$ ;
- **calculer** un complément de Schur, une loi marginale et une loi conditionnelle, et **lire** une matrice de précision ;
- **multiplier** deux densités gaussiennes, et **calculer** la loi a posteriori, la prédictive et l'évidence d'une régression linéaire bayésienne ;
- **estimer** $\boldsymbol{\mu}$ et $\boldsymbol{\Sigma}$ par le maximum de vraisemblance, avec les gradients de $\ln\det$ et de la trace ;
- **définir** la divergence KL continue, **justifier** sa positivité et son additivité, et **calculer** la KL entre deux gaussiennes ;
- **construire** l'interpolation sphérique entre deux vecteurs et en **démontrer** les propriétés.

## L'essentiel en 10 lignes

1. **Densité** de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ ($\boldsymbol{\Sigma}$ définie positive) : $p(\mathbf{x}) = (2\pi)^{-d/2}(\det\boldsymbol{\Sigma})^{-1/2}\exp\big(-\tfrac12\Delta^2(\mathbf{x})\big)$, avec $\Delta^2(\mathbf{x}) = (\mathbf{x} - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ ; $\ln p = -\tfrac12\big[d\ln(2\pi) + \ln\det\boldsymbol{\Sigma} + \Delta^2\big]$, et $\ln\det\boldsymbol{\Sigma} = 2\sum_i\ln L_{ii}$. $\mathcal{N}(\mathbf{0}, \mathbf{I})$ : $d$ coordonnées indépendantes de loi $\mathcal{N}(0, 1)$.
2. **Vecteur gaussien** : toute combinaison $\boldsymbol{\alpha}^\top\mathbf{x}$ est gaussienne ; donc $\mathbf{A}\mathbf{x} + \mathbf{b} \sim \mathcal{N}(\mathbf{A}\boldsymbol{\mu} + \mathbf{b}, \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top)$, et la somme de deux vecteurs gaussiens indépendants additionne moyennes et covariances. Deux coordonnées gaussiennes ne font pas toujours un vecteur gaussien.
3. **Changement de variable** : si $\mathbf{y} = U(\mathbf{x})$, $p_{\mathbf{y}}(\mathbf{y}) = p_{\mathbf{x}}\big(U^{-1}(\mathbf{y})\big)\,\big\lvert\det\mathbf{J}_{U^{-1}}(\mathbf{y})\big\rvert$. Si $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, alors $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{L}\mathbf{L}^\top)$ : on tire par Cholesky, et $\mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ blanchit. En lignes : $\mathbf{X} = \mathbf{1}\boldsymbol{\mu}^\top + \mathbf{E}\mathbf{L}^\top$.
4. **Ellipses** $\Delta(\mathbf{x}) = c$ : axes les vecteurs propres de $\boldsymbol{\Sigma}$, demi-axes $c\sqrt{\lambda_i}$, aire $\pi c^2\sqrt{\det\boldsymbol{\Sigma}}$ ; en dimension 2, masse $1 - e^{-c^2/2}$ ; en dimension $d$, $\Delta^2$ suit la loi du khi-deux à $d$ degrés.
5. **Norme** de $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_d)$ : densité proportionnelle à $r^{d-1}e^{-r^2/2}$, de mode $\sqrt{d - 1}$ ; la densité de $\boldsymbol{\varepsilon}$ est maximale au centre, mais sa masse est sur une couronne.
6. **Blocs** : $\mathbf{x}_a \sim \mathcal{N}(\boldsymbol{\mu}_a, \boldsymbol{\Sigma}_{aa})$ ; $\mathbf{x}_a \mid \mathbf{x}_b \sim \mathcal{N}\big(\boldsymbol{\mu}_a + \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}(\mathbf{x}_b - \boldsymbol{\mu}_b),\ \boldsymbol{\Sigma}_{aa} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}\big)$ : une moyenne affine en la valeur lue, une covariance, le **complément de Schur**, qui n'en dépend pas. $\det\mathbf{M} = \det\mathbf{M}_{bb}\,\det(\mathbf{M}/\mathbf{M}_{bb})$.
7. **Précision** $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ : $\boldsymbol{\Sigma}_{a \mid b} = \boldsymbol{\Lambda}_{aa}^{-1}$ ; $\Lambda_{ij} = 0$ si et seulement si $x_i$ et $x_j$ sont indépendantes sachant les autres. Pour un vecteur gaussien, décorrélé équivaut à indépendant.
8. **Bayes gaussien** : les précisions s'additionnent, les moyennes se pondèrent par les précisions. Régression bayésienne : $\mathbf{S}_N = (\mathbf{S}_0^{-1} + \sigma^{-2}\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}$, $\mathbf{m}_N = \mathbf{S}_N(\mathbf{S}_0^{-1}\mathbf{m}_0 + \sigma^{-2}\boldsymbol{\Phi}^\top\mathbf{y})$ ; prédictive $\mathcal{N}(\boldsymbol{\phi}^\top\mathbf{m}_N, \boldsymbol{\phi}^\top\mathbf{S}_N\boldsymbol{\phi} + \sigma^2)$ ; évidence $\mathcal{N}(\mathbf{y} \mid \boldsymbol{\Phi}\mathbf{m}_0, \boldsymbol{\Phi}\mathbf{S}_0\boldsymbol{\Phi}^\top + \sigma^2\mathbf{I})$ ; avec $\mathbf{m}_0 = \mathbf{0}$ et $\mathbf{S}_0 = \tau^2\mathbf{I}$, $\mathbf{m}_N$ est la solution ridge de pénalité $\sigma^2/\tau^2$.
9. **Maximum de vraisemblance** : $\hat{\boldsymbol{\mu}} = \bar{\mathbf{x}}$, $\hat{\boldsymbol{\Sigma}} = \mathbf{S}/n$ (gradients de $\ln\det$ et de la trace) ; biaisée, singulière si $n \le d$. **KL** : $\mathrm{KL}(p \,\|\, q) = \mathbb{E}_p[\ln p - \ln q] \ge 0$, nulle si et seulement si $p = q$, infinie si $q$ s'annule sur une région où $p$ a une masse positive, asymétrique, additive sur des lois produits ; entre $\mathcal{N}(\boldsymbol{\mu}_0, \boldsymbol{\Sigma}_0)$ et $\mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)$, $\tfrac12\big[\operatorname{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0) + \boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta} - d + \ln\frac{\det\boldsymbol{\Sigma}_1}{\det\boldsymbol{\Sigma}_0}\big]$ avec $\boldsymbol{\delta} = \boldsymbol{\mu}_1 - \boldsymbol{\mu}_0$ ; entropie différentielle $\tfrac12\ln\big((2\pi e)^d\det\boldsymbol{\Sigma}\big)$.
10. **Slerp** : $\frac{\sin((1 - t)\Omega)}{\sin\Omega}\mathbf{u} + \frac{\sin(t\Omega)}{\sin\Omega}\mathbf{v}$, avec $\cos\Omega = \frac{\mathbf{u}^\top\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}$ : il relie $\mathbf{u}$ à $\mathbf{v}$, garde la norme commune, tourne de $t\Omega$, et tend vers la ligne droite quand $\Omega \to 0$ ; le milieu de la corde, lui, est à la distance $\cos(\Omega/2)$ du centre de la sphère unité.

## §1 · La densité de la loi normale multivariée : de N(0, I) à N(μ, Σ), déterminant et distance de Mahalanobis

### De N(0, 1) à N(0, I)

M02b a défini la loi $\mathcal{N}(0, 1)$, de densité $\frac{1}{\sqrt{2\pi}}e^{-z^2/2}$. Prenons $d$ variables $\varepsilon_1, \ldots, \varepsilon_d$ **indépendantes**, chacune de loi $\mathcal{N}(0, 1)$, et rangeons-les dans un vecteur $\boldsymbol{\varepsilon}$. Leur densité jointe est le produit des densités (M02b §7) :
$$p(\boldsymbol{\varepsilon}) = \prod_{i=1}^d \frac{1}{\sqrt{2\pi}}e^{-\varepsilon_i^2/2} = (2\pi)^{-d/2}\exp\Big(-\frac12\lVert\boldsymbol{\varepsilon}\rVert^2\Big).$$
C'est la **loi normale standard** de dimension $d$, notée $\mathcal{N}(\mathbf{0}, \mathbf{I})$ (*standard normal distribution*) : moyenne $\mathbf{0}$, covariance $\mathbf{I}$. Sa densité ne dépend que de la **norme** $\lVert\boldsymbol{\varepsilon}\rVert$ : ses lignes de niveau sont des cercles (des sphères en dimension 3), et elle est la même dans toutes les directions.

### Vecteur gaussien, N(μ, Σ) et sa densité

> **Définition.** Un vecteur aléatoire $\mathbf{x}$ de $\mathbb{R}^d$ est un **vecteur gaussien** (*Gaussian random vector*) si **toute** combinaison linéaire $\boldsymbol{\alpha}^\top\mathbf{x} = \alpha_1x_1 + \cdots + \alpha_dx_d$ de ses coordonnées suit une loi normale. On compte une constante comme une loi normale de variance nulle (une loi **dégénérée**). Sa loi est alors entièrement fixée par sa moyenne $\boldsymbol{\mu} = \mathbb{E}[\mathbf{x}]$ et sa covariance $\boldsymbol{\Sigma} = \operatorname{Cov}(\mathbf{x})$ (admis) : on la note $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, la **loi normale multivariée** (*multivariate normal distribution*).

Par exemple, $\mathcal{N}(\mathbf{0}, \mathbf{I})$ est bien la loi d'un vecteur gaussien : une combinaison $\boldsymbol{\alpha}^\top\boldsymbol{\varepsilon}$ de variables normales indépendantes est normale (M02b §6), de variance $\lVert\boldsymbol{\alpha}\rVert^2$. Une covariance est toujours symétrique semi-définie positive (M12c §8). Quand elle est **définie** positive, la loi a une densité :

> **Densité** (admise ici ; le §2 la retrouve). Si $\boldsymbol{\Sigma}$ est symétrique définie positive, $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ a pour densité
> $$p(\mathbf{x}) = \mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}, \boldsymbol{\Sigma}) = \frac{1}{(2\pi)^{d/2}\sqrt{\det\boldsymbol{\Sigma}}}\exp\Big(-\frac12\Delta^2(\mathbf{x})\Big), \qquad \Delta^2(\mathbf{x}) = (\mathbf{x} - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu}).$$
> La racine $\Delta(\mathbf{x}) \ge 0$ est la **distance de Mahalanobis** (*Mahalanobis distance*) de $\mathbf{x}$ à $\boldsymbol{\mu}$ (M12c §8).

Pour $\boldsymbol{\mu} = \mathbf{0}$ et $\boldsymbol{\Sigma} = \mathbf{I}$, on retrouve la densité ci-dessus ; pour $d = 1$, $\Delta^2 = \frac{(x - \mu)^2}{\sigma^2}$ et c'est la densité de $\mathcal{N}(\mu, \sigma^2)$ de M02b. Le facteur se lit aussi $\frac{1}{\sqrt{\det(2\pi\boldsymbol{\Sigma})}}$, puisque $\det(2\pi\boldsymbol{\Sigma}) = (2\pi)^d\det\boldsymbol{\Sigma}$ (M12c §1).

**Exemple : l'erreur d'un récepteur GPS.** Un récepteur fixe, posé sur une borne dont la position exacte est connue, donne chaque minute une position. Son erreur $\mathbf{x} = (x_1, x_2)$, en mètres, vers l'est et vers le nord, suit $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ avec
$$\boldsymbol{\mu} = \begin{pmatrix} 2 \\ -4 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 16 & 4 \\ 4 & 10 \end{pmatrix}, \qquad \det\boldsymbol{\Sigma} = 144, \qquad \boldsymbol{\Sigma}^{-1} = \frac{1}{144}\begin{pmatrix} 10 & -4 \\ -4 & 16 \end{pmatrix}.$$
Le récepteur a un **biais** (2 m vers l'est, 4 m vers le sud), des écarts-types de 4 m et $\sqrt{10}$ m (un peu plus de 3 m), et des erreurs un peu liées (corrélation $\frac{4}{4\sqrt{10}} \approx 0{,}316$). La densité est maximale en $\mathbf{x} = \boldsymbol{\mu}$, où l'exponentielle vaut 1 : $p(\boldsymbol{\mu}) = \frac{1}{2\pi \times 12} = \frac{1}{24\pi} \approx 0{,}01326$ par mètre carré. On dit souvent que $\boldsymbol{\mu}$ est le « point le plus probable » ; c'est le point de densité maximale (le **mode**). Une densité n'est pas une probabilité : la probabilité qu'une erreur tombe dans un petit carré de 10 cm de côté autour de $\boldsymbol{\mu}$ vaut environ $0{,}01326 \times 0{,}01 \approx 1{,}3 \times 10^{-4}$, et celle de tomber **exactement** en $\boldsymbol{\mu}$ est nulle.

### Ce que disent det Σ et la distance de Mahalanobis

- **$\Delta$ dit où l'on est.** La densité décroît quand $\Delta$ grandit ; ses lignes de niveau $\Delta(\mathbf{x}) = c$ sont des **ellipses** centrées en $\boldsymbol{\mu}$ (§3). $\Delta$ mesure l'écart à la moyenne **à l'échelle de la dispersion dans chaque direction** : un même écart en mètres compte peu là où les erreurs sont grandes, beaucoup là où elles sont petites.
- **$\det\boldsymbol{\Sigma}$ dit combien la loi s'étale.** Le facteur $\frac{1}{\sqrt{\det\boldsymbol{\Sigma}}}$ garantit une intégrale égale à 1 : $\sqrt{\det\boldsymbol{\Sigma}}$ est, à un facteur près, l'aire des ellipses (le volume des ellipsoïdes en dimension $d$, §3), et une loi plus étalée a un pic plus bas. Multiplier $\boldsymbol{\Sigma}$ par 4 en dimension 2 multiplie $\det\boldsymbol{\Sigma}$ par 16 et divise la hauteur du pic par 4.

**Exemple.** Les points $\mathbf{x}_A = \boldsymbol{\mu} + (4, 2) = (6, -2)$ et $\mathbf{x}_B = \boldsymbol{\mu} + (2, -4) = (4, -8)$ sont à la même distance euclidienne de $\boldsymbol{\mu}$, $\sqrt{20}$ m (environ 4,5 m). Mais
$$\Delta^2(\mathbf{x}_A) = \frac{10 \times 16 - 2 \times 4 \times 4 \times 2 + 16 \times 4}{144} = \frac{160}{144} = \frac{10}{9}, \qquad \Delta^2(\mathbf{x}_B) = \frac{10 \times 4 + 2 \times 4 \times 2 \times 4 + 16 \times 16}{144} = \frac{360}{144} = \frac52 .$$
$\mathbf{x}_A$ est à la distance de Mahalanobis $1{,}054$, dans une direction où le récepteur se trompe beaucoup ; $\mathbf{x}_B$ à $1{,}581$, dans une direction où il se trompe peu. Les densités, $p(\mathbf{x}_A) = \frac{1}{24\pi}e^{-5/9} \approx 0{,}00761$ et $p(\mathbf{x}_B) = \frac{1}{24\pi}e^{-5/4} \approx 0{,}00380$, valent 57 % et 29 % du pic.

![À gauche, 1 500 erreurs tirées de N(μ, Σ) (μ = (2, −4), Σ de lignes (16, 4) et (4, 10)), les ellipses à 80 % et à 98 %, les axes propres q₁ et q₂ (flèches c₈₀√18 et c₈₀√8, c₈₀ étant le niveau de l'ellipse à 80 %), le cercle de rayon √20 autour de μ, et les points x_A (Δ² = 10/9) et x_B (Δ² = 5/2) ; à droite, les mêmes tirages blanchis par L⁻¹ : un nuage rond, des cercles de rayons 1,79 et 2,80, et les images de x_A et de x_B, de normes 1,054 et 1,581](figures/ellipses_cholesky.png)

### La log-densité, par Cholesky

On calcule presque toujours le **logarithme** de la densité (*log-density*) : en dimension 50, la densité de $\mathcal{N}(\mathbf{0}, \mathbf{I})$ en un tirage typique est de l'ordre de $10^{-31}$, et un produit de milliers de densités sort des flottants (M04 §7), alors que leur logarithme reste un nombre ordinaire.
$$\ln p(\mathbf{x}) = -\frac12\Big[d\ln(2\pi) + \ln\det\boldsymbol{\Sigma} + \Delta^2(\mathbf{x})\Big].$$
Pour comparer des lois de dimensions différentes, on divise la somme des log-densités de $n$ points par $nd$ : une log-vraisemblance moyenne, en nats par coordonnée (🔗 M25a.16).

On n'inverse jamais $\boldsymbol{\Sigma}$ pour calculer $\ln p$. Avec son facteur de Cholesky (*Cholesky factor*), $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$ (M12c §7) :
- $\det\boldsymbol{\Sigma} = (\det\mathbf{L})^2 = \prod_iL_{ii}^2$, donc $\ln\det\boldsymbol{\Sigma} = 2\sum_i\ln L_{ii}$ ;
- $\Delta^2(\mathbf{x}) = (\mathbf{x} - \boldsymbol{\mu})^\top(\mathbf{L}^\top)^{-1}\mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu}) = \lVert\mathbf{y}\rVert^2$, où $\mathbf{y}$ résout le système **triangulaire** $\mathbf{L}\mathbf{y} = \mathbf{x} - \boldsymbol{\mu}$ (une descente, M12c §7).

Pour le GPS, $\mathbf{L} = \begin{pmatrix} 4 & 0 \\ 1 & 3 \end{pmatrix}$ ($l_{11} = \sqrt{16}$, $l_{21} = \frac44$, $l_{22} = \sqrt{10 - 1}$). Donc $\ln\det\boldsymbol{\Sigma} = 2(\ln 4 + \ln 3) = \ln 144$. Pour $\mathbf{x}_A$, $\mathbf{L}\mathbf{y} = (4, 2)$ donne $y_1 = 1$, puis $y_2 = \frac{2 - 1}{3} = \frac13$, et $\lVert\mathbf{y}\rVert^2 = 1 + \frac19 = \frac{10}{9}$ : la valeur trouvée plus haut. Avec $\ln(2\pi) \approx 1{,}8379$ et $\frac12\ln 144 \approx 2{,}4849$ : $\ln p(\boldsymbol{\mu}) \approx -4{,}3228$ et $\ln p(\mathbf{x}_A) = \ln p(\boldsymbol{\mu}) - \frac{5}{9} \approx -4{,}8783$.

### Les cas limites

- **$\boldsymbol{\Sigma}$ semi-définie, pas définie.** Si $\boldsymbol{\Sigma}$ a une valeur propre nulle, de vecteur propre $\mathbf{q}$, alors $\mathbb{V}(\mathbf{q}^\top\mathbf{x}) = \mathbf{q}^\top\boldsymbol{\Sigma}\mathbf{q} = 0$ : la combinaison $\mathbf{q}^\top\mathbf{x}$ est constante, et $\mathbf{x}$ reste dans un sous-espace affine de dimension plus petite. Il n'y a plus de densité ($\det\boldsymbol{\Sigma} = 0$, et $\boldsymbol{\Sigma}^{-1}$ n'existe pas), mais la loi existe : c'est une **gaussienne dégénérée** (*degenerate distribution*). Exemple : $z \sim \mathcal{N}(0, 1)$ et $\mathbf{x} = (z, 2z)$ ont pour covariance $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, de déterminant nul ; tous les tirages sont sur la droite $x_2 = 2x_1$. En dimension 1, $\mathcal{N}(\mu, 0)$ est la loi de la constante $\mu$.
- **$\boldsymbol{\Sigma}$ diagonale** : $\Delta^2 = \sum_i\frac{(x_i - \mu_i)^2}{\sigma_i^2}$ et $\det\boldsymbol{\Sigma} = \prod_i\sigma_i^2$, donc la densité est le produit des $d$ densités $\mathcal{N}(\mu_i, \sigma_i^2)$ : les coordonnées sont indépendantes (le §4 en fera un théorème).

💻 **Aujourd'hui en pratique** — `scipy.stats.multivariate_normal(mean, cov).logpdf(x)` rend la log-densité (un tableau si `x` a une ligne par point), et `np.linalg.slogdet` rend $\ln\lvert\det\rvert$ sans former le déterminant. Les bibliothèques passent par une factorisation et des systèmes triangulaires (`scipy.linalg.solve_triangular`), jamais par `np.linalg.inv`, comme ton `mvn_logpdf` (🔨 M25a.20).

⚠️ **Erreur classique.** Écrire $\frac{1}{\sqrt{2\pi\det\boldsymbol{\Sigma}}}$ en dimension $d \ge 2$ : le facteur $2\pi$ est à la puissance $\frac d2$. Oublier le facteur 2 de $\ln\det\boldsymbol{\Sigma} = 2\sum_i\ln L_{ii}$ (🐛 M25a.28). Prendre la distance euclidienne pour la distance de Mahalanobis. Lire le second paramètre de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ comme un écart-type.

🔗 **Dans workbookIA** — le chapitre 25 évalue des densités gaussiennes de grande dimension à covariance diagonale, et surtout leurs logarithmes.

## §2 · Transformations affines, sommes et changement de variable : la loi de μ + Lε et l'échantillonnage par Cholesky

### Les transformations affines restent gaussiennes

> **Propriété.** Si $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ dans $\mathbb{R}^d$, $\mathbf{A}$ est une matrice de forme $(k, d)$ et $\mathbf{b} \in \mathbb{R}^k$, alors
> $$\mathbf{A}\mathbf{x} + \mathbf{b} \sim \mathcal{N}(\mathbf{A}\boldsymbol{\mu} + \mathbf{b},\ \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top).$$

Que ce soit un vecteur gaussien découle de la définition : une combinaison $\boldsymbol{\alpha}^\top(\mathbf{A}\mathbf{x} + \mathbf{b}) = (\mathbf{A}^\top\boldsymbol{\alpha})^\top\mathbf{x} + \boldsymbol{\alpha}^\top\mathbf{b}$ est une combinaison des coordonnées de $\mathbf{x}$ plus une constante, donc normale. La moyenne et la covariance viennent de M12c §8. Aucune hypothèse sur $\mathbf{A}$ : elle peut être rectangulaire, et $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$ singulière (la loi est alors dégénérée).

**Exemple.** Le long d'une clôture rectiligne de direction $\boldsymbol{\alpha} = (0{,}8 ;\ -0{,}6)$ (un vecteur unitaire), l'erreur du GPS est $\boldsymbol{\alpha}^\top\mathbf{x}$, de loi $\mathcal{N}(\boldsymbol{\alpha}^\top\boldsymbol{\mu},\ \boldsymbol{\alpha}^\top\boldsymbol{\Sigma}\boldsymbol{\alpha})$ :
$$\boldsymbol{\alpha}^\top\boldsymbol{\mu} = 1{,}6 + 2{,}4 = 4, \qquad \boldsymbol{\alpha}^\top\boldsymbol{\Sigma}\boldsymbol{\alpha} = 0{,}64 \times 16 - 2 \times 0{,}48 \times 4 + 0{,}36 \times 10 = 10 .$$
Le long de la clôture, l'erreur suit $\mathcal{N}(4, 10)$ : une seule coordonnée, et toutes les probabilités de M02b s'appliquent.

### Le changement de variable multivarié

M02b §8 donnait la densité de $Y = g(X)$ pour $g$ strictement monotone : $f_Y(y) = f_X(g^{-1}(y))\,\lvert(g^{-1})'(y)\rvert$. Le facteur $\lvert(g^{-1})'\rvert$ compense l'étirement des longueurs. En dimension $d$, une application étire les **volumes**, d'un facteur que mesure le déterminant de sa jacobienne (*Jacobian determinant* ; M12c §1, M17 §1).

> **Théorème du changement de variable** (*change of variables* ; MML Théorème 6.16, admis). Soit $\mathbf{x}$ un vecteur aléatoire de densité $p_{\mathbf{x}}$, et $U : \mathbb{R}^d \to \mathbb{R}^d$ une application **inversible**, dérivable, d'inverse dérivable. Alors $\mathbf{y} = U(\mathbf{x})$ a pour densité
> $$p_{\mathbf{y}}(\mathbf{y}) = p_{\mathbf{x}}\big(U^{-1}(\mathbf{y})\big)\,\big\lvert\det\mathbf{J}_{U^{-1}}(\mathbf{y})\big\rvert,$$
> où $\mathbf{J}_{U^{-1}}(\mathbf{y})$ est la jacobienne de $U^{-1}$ au point $\mathbf{y}$.

La recette est celle de la dimension 1 (où le déterminant est la dérivée $(U^{-1})'(y)$) : l'antécédent, la densité de départ en ce point, la valeur absolue du déterminant de la jacobienne de l'inverse. Pour une application **affine** inversible, $U(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}$ avec $\det\mathbf{A} \ne 0$ : $U^{-1}(\mathbf{y}) = \mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$, de jacobienne constante $\mathbf{A}^{-1}$, de déterminant $\frac{1}{\det\mathbf{A}}$, donc
$$p_{\mathbf{y}}(\mathbf{y}) = \frac{1}{\lvert\det\mathbf{A}\rvert}\,p_{\mathbf{x}}\big(\mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})\big).$$
Un petit pavé de volume $v$ devient un parallélépipède de volume $\lvert\det\mathbf{A}\rvert\,v$ : la densité est divisée d'autant.

### La loi de μ + Lε, et tirer par Cholesky

> **Propriété** (∂ M25a.10). Si $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ et si $\mathbf{L}$ est inversible, alors $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ a la densité de $\mathcal{N}(\boldsymbol{\mu}, \mathbf{L}\mathbf{L}^\top)$. Plus généralement, pour $\mathbf{A}$ carrée inversible, $\mathbf{A}\mathbf{x} + \mathbf{b}$ a la densité de $\mathcal{N}(\mathbf{A}\boldsymbol{\mu} + \mathbf{b}, \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top)$.

Le ∂ M25a.10 applique le théorème à $U(\boldsymbol{\varepsilon}) = \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ : il faut son inverse, le déterminant de la jacobienne de celle-ci, et réécrire la norme de l'antécédent avec $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$. C'est ce qui justifie la densité du §1 : une loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec $\boldsymbol{\Sigma}$ définie positive, est l'image de $\mathcal{N}(\mathbf{0}, \mathbf{I})$ par $\boldsymbol{\varepsilon} \mapsto \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$.

**Vérification sur le GPS**, au point $\mathbf{x}_A$ : son antécédent est $\mathbf{L}^{-1}(\mathbf{x}_A - \boldsymbol{\mu}) = (1, \frac13)$ (calculé au §1), et $\det\mathbf{L} = 12$. La formule donne $p(\mathbf{x}_A) = \frac{1}{12}\cdot\frac{1}{2\pi}e^{-\frac12(1 + 1/9)} = \frac{1}{24\pi}e^{-5/9}$ : la densité du §1.

**Tirer un vecteur de loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$** (*sampling*), MML §6.5.4 :
1. calculer une fois $\mathbf{L}$, le facteur de Cholesky de $\boldsymbol{\Sigma}$ ;
2. tirer $d$ nombres indépendants de loi $\mathcal{N}(0, 1)$ : un vecteur $\boldsymbol{\varepsilon}$ ;
3. rendre $\mathbf{x} = \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$.

Sa moyenne est $\boldsymbol{\mu}$, sa covariance $\mathbf{L}\mathbf{I}\mathbf{L}^\top = \boldsymbol{\Sigma}$ (le « chemin inverse » de M12c §8), et sa loi est gaussienne. Pour le GPS, $\boldsymbol{\varepsilon} = (1{,}2 ;\ -0{,}5)$ donne $\mathbf{L}\boldsymbol{\varepsilon} = (4 \times 1{,}2 ;\ 1{,}2 - 3 \times 0{,}5) = (4{,}8 ;\ -0{,}3)$, et l'erreur $\mathbf{x} = (6{,}8 ;\ -4{,}3)$. Dans l'autre sens, $\boldsymbol{\varepsilon} = \mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ **blanchit** (*whitening*, M12c §8 ; la figure du §1, à droite).

**Pourquoi Cholesky ?** N'importe quelle matrice $\mathbf{T}$ telle que $\mathbf{T}\mathbf{T}^\top = \boldsymbol{\Sigma}$ convient : $\boldsymbol{\Sigma}^{1/2}$, ou $\mathbf{Q}\operatorname{diag}(\sqrt{\lambda_1}, \ldots, \sqrt{\lambda_d})$ (M12c §8). Deux choix donnent des tirages différents pour un même $\boldsymbol{\varepsilon}$, mais la même loi. Cholesky est le moins cher (de l'ordre de $d^3/3$ opérations, sans valeurs propres), stable pour une matrice définie positive ; il donne $\ln\det\boldsymbol{\Sigma}$ au passage (§1), et son échec signale une $\boldsymbol{\Sigma}$ qui n'est pas définie positive.

📐 **Notations.** Avec des vecteurs **en lignes**, comme dans NumPy et `mymath` : on tire d'un coup un tableau $\mathbf{E}$ de forme $(n, d)$, dont chaque ligne est un $\boldsymbol{\varepsilon}^\top$. La ligne $i$ du résultat doit être $(\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}_i)^\top = \boldsymbol{\mu}^\top + \boldsymbol{\varepsilon}_i^\top\mathbf{L}^\top$, donc
$$\mathbf{X} = \mathbf{1}\boldsymbol{\mu}^\top + \mathbf{E}\mathbf{L}^\top \qquad (\texttt{mean + E @ L.T}),$$
où $\mathbf{1}$ est une colonne de $n$ uns (NumPy l'écrit par diffusion, M20). Avec les lignes $(1{,}2 ;\ -0{,}5)$ et $(0, 1)$, les lignes de $\mathbf{X}$ sont $(6{,}8 ;\ -4{,}3)$ et $(2, -1)$. Le 🔗 M25a.16 fait passer d'une convention à l'autre.

### Sommes de vecteurs gaussiens indépendants

> **Propriété.** Si $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}_{\mathbf{x}}, \boldsymbol{\Sigma}_{\mathbf{x}})$ et $\mathbf{y} \sim \mathcal{N}(\boldsymbol{\mu}_{\mathbf{y}}, \boldsymbol{\Sigma}_{\mathbf{y}})$ sont **indépendants**, de même dimension, alors $\mathbf{x} + \mathbf{y} \sim \mathcal{N}(\boldsymbol{\mu}_{\mathbf{x}} + \boldsymbol{\mu}_{\mathbf{y}},\ \boldsymbol{\Sigma}_{\mathbf{x}} + \boldsymbol{\Sigma}_{\mathbf{y}})$.

Le vecteur $(\mathbf{x}, \mathbf{y})$, mis bout à bout, est gaussien (admis pour deux vecteurs gaussiens indépendants), de covariance diagonale par blocs ; et $\mathbf{x} + \mathbf{y} = \begin{pmatrix} \mathbf{I} & \mathbf{I} \end{pmatrix}\begin{pmatrix} \mathbf{x} \\ \mathbf{y} \end{pmatrix}$ est une image linéaire. Ce sont les **covariances** qui s'additionnent, comme les variances en dimension 1 (M02b §6).

**Exemple.** Les signaux reçus par le GPS se réfléchissent parfois sur les immeubles voisins, ce qui ajoute une erreur indépendante de loi $\mathcal{N}(\mathbf{0}, 2\mathbf{I})$. L'erreur totale suit $\mathcal{N}\big(\boldsymbol{\mu}, \begin{pmatrix} 18 & 4 \\ 4 & 12 \end{pmatrix}\big)$. Ajouter $2\mathbf{I}$ ne change pas les vecteurs propres et ajoute 2 à chaque valeur propre (si $\boldsymbol{\Sigma}\mathbf{q} = \lambda\mathbf{q}$, alors $(\boldsymbol{\Sigma} + 2\mathbf{I})\mathbf{q} = (\lambda + 2)\mathbf{q}$) : 20 et 10 au lieu de 18 et 8 (§3).

### Ce qui ne reste pas gaussien

- **Deux coordonnées gaussiennes ne font pas un vecteur gaussien.** Soit $x \sim \mathcal{N}(0, 1)$ et $s$ un signe $\pm 1$ tiré à pile ou face, indépendant de $x$ ; posons $y = s\,x$. Par symétrie de la cloche, $y \sim \mathcal{N}(0, 1)$. Mais $x + y$ vaut 0 avec la probabilité $\frac12$ sans être constante : ce n'est pas une variable normale, et $(x, y)$ n'est pas un vecteur gaussien. De plus, $\operatorname{Cov}(x, y) = \mathbb{E}[s]\,\mathbb{E}[x^2] = 0$, alors que $\lvert y\rvert = \lvert x\rvert$ : décorrélées et dépendantes, ce qui est impossible dans un vecteur gaussien (§4).
- **Le produit** de deux variables normales indépendantes n'est pas normal : pour $x, y \sim \mathcal{N}(0, 1)$, $xy$ est centrée, de variance 1, mais $\mathbb{E}[(xy)^4] = 9 \ne 3$, le moment d'ordre 4 de $\mathcal{N}(0, 1)$ (M07.13, ou M02c §9, qui a admis $\mathbb{V}(Z^2) = 2$). Le **produit de deux densités** gaussiennes (§5), lui, est gaussien à un facteur près.
- **La norme** $\lVert\mathbf{x}\rVert$ n'est normale que si $\mathbf{x}$ est constant : elle est positive, alors qu'une loi normale non dégénérée donne une probabilité positive aux nombres négatifs. Sa loi est au §3.

💻 **Aujourd'hui en pratique** — avec `rng = np.random.default_rng(seed)`, `rng.multivariate_normal(mean, cov, size=n, method="cholesky")` tire $n$ vecteurs d'un coup (sans `method`, il passe par une SVD). Tu écris `sample_mvn` en 🔨 M25a.21, avec un seul appel `rng.standard_normal((n, d))`, et tu la testes par ses moments en 🛠️ M25a.29.

⚠️ **Erreur classique.** Écrire `E @ L` au lieu de `E @ L.T` (🐛 M25a.28) : la covariance obtenue est $\mathbf{L}^\top\mathbf{L}$, qui n'est pas $\boldsymbol{\Sigma}$ en général. Multiplier par $\boldsymbol{\Sigma}$ au lieu de $\mathbf{L}$ : $\boldsymbol{\mu} + \boldsymbol{\Sigma}\boldsymbol{\varepsilon}$ a pour covariance $\boldsymbol{\Sigma}^2$. Écrire $\mathbf{A}\boldsymbol{\Sigma}$ au lieu de $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$. Additionner des écarts-types au lieu de covariances.

🔗 **Dans workbookIA** — le chapitre 25 tire des vecteurs gaussiens à covariance diagonale à partir de tirages de $\mathcal{N}(\mathbf{0}, \mathbf{I})$ : c'est la loi de $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ avec $\mathbf{L}$ diagonale. Il en fait aussi un outil pour dériver, que M25b préparera.

## §3 · Géométrie : ellipses de niveau, masse d'une ellipse et loi de la norme

### Les ellipses de niveau

Écrivons $\boldsymbol{\Sigma} = \mathbf{Q}\operatorname{diag}(\lambda_1, \ldots, \lambda_d)\mathbf{Q}^\top$ (le théorème spectral, M12c §6), avec $\mathbf{Q}$ orthogonale de colonnes $\mathbf{q}_i$ et toutes les $\lambda_i > 0$. Alors $\boldsymbol{\Sigma}^{-1} = \mathbf{Q}\operatorname{diag}\big(\frac{1}{\lambda_1}, \ldots, \frac{1}{\lambda_d}\big)\mathbf{Q}^\top$, et avec les coordonnées $\mathbf{y} = \mathbf{Q}^\top(\mathbf{x} - \boldsymbol{\mu})$ dans la base des vecteurs propres,
$$\Delta^2(\mathbf{x}) = \frac{y_1^2}{\lambda_1} + \cdots + \frac{y_d^2}{\lambda_d}.$$

> **Propriété.** La ligne de niveau $\Delta(\mathbf{x}) = c$, pour $c > 0$, est une **ellipse** (un **ellipsoïde** en dimension $d$, *level set*) de centre $\boldsymbol{\mu}$, d'axes les vecteurs propres $\mathbf{q}_i$ de $\boldsymbol{\Sigma}$, et de **demi-axes** $c\sqrt{\lambda_i}$. En dimension 2, son aire est $\pi c^2\sqrt{\lambda_1\lambda_2} = \pi c^2\sqrt{\det\boldsymbol{\Sigma}}$ ; en dimension $d$, le volume de l'ellipsoïde est proportionnel à $c^d\sqrt{\det\boldsymbol{\Sigma}}$.

En effet, $\frac{y_1^2}{(c\sqrt{\lambda_1})^2} + \frac{y_2^2}{(c\sqrt{\lambda_2})^2} = 1$ est l'équation d'une ellipse de demi-axes $c\sqrt{\lambda_1}$ et $c\sqrt{\lambda_2}$ le long des axes de $\mathbf{y}$, et l'aire d'une ellipse est $\pi$ fois le produit de ses demi-axes : c'est $\sqrt{\det\boldsymbol{\Sigma}}$, et non $\det\boldsymbol{\Sigma}$, qui mesure cette aire (ce volume en dimension $d$). Le grand axe va dans la direction où la variance est la plus grande ($\lambda_1$, M12c §6).

**Pour le GPS.** $\boldsymbol{\Sigma} - 18\mathbf{I} = \begin{pmatrix} -2 & 4 \\ 4 & -8 \end{pmatrix}$ et $\boldsymbol{\Sigma} - 8\mathbf{I} = \begin{pmatrix} 8 & 4 \\ 4 & 2 \end{pmatrix}$ : les valeurs propres sont 18 et 8 (de produit 144 et de somme 26), de vecteurs propres $\mathbf{q}_1 = \frac{1}{\sqrt5}(2, 1)$ et $\mathbf{q}_2 = \frac{1}{\sqrt5}(1, -2)$. Les ellipses de niveau ont leur grand axe incliné d'environ 26,6° au-dessus de l'est (la pente $\frac12$), des demi-axes $c\sqrt{18} \approx 4{,}243\,c$ et $c\sqrt8 \approx 2{,}828\,c$ mètres, et une aire de $12\pi c^2$ m². Les points $\mathbf{x}_A$ et $\mathbf{x}_B$ du §1 sont sur les deux axes, et $\Delta^2(\mathbf{x}_A) = \frac{20}{18}$, $\Delta^2(\mathbf{x}_B) = \frac{20}{8}$ : on retrouve $\frac{10}{9}$ et $\frac52$.

### La masse d'une ellipse en dimension 2

Quelle proportion des erreurs tombe à l'intérieur de l'ellipse $\Delta \le c$ ? Blanchir répond : $\boldsymbol{\varepsilon} = \mathbf{L}^{-1}(\mathbf{x} - \boldsymbol{\mu})$ suit $\mathcal{N}(\mathbf{0}, \mathbf{I})$, et $\Delta(\mathbf{x}) = \lVert\boldsymbol{\varepsilon}\rVert$ (§1). L'ellipse devient le disque de rayon $c$, et il reste à intégrer la densité de $\mathcal{N}(\mathbf{0}, \mathbf{I})$ sur ce disque, en coordonnées polaires (M02b §7).

> **Propriété** (∂ M25a.11). En dimension 2, pour tout $c \ge 0$,
> $$P\big(\Delta(\mathbf{x}) \le c\big) = 1 - e^{-c^2/2}.$$
> La masse ne dépend ni de $\boldsymbol{\mu}$ ni de $\boldsymbol{\Sigma}$, seulement du niveau $c$. Dans l'autre sens, l'ellipse de masse $1 - \beta$ a pour niveau $c^2 = -2\ln\beta$.

Le disque de rayon $c$ autour de l'origine, pour $\mathcal{N}(\mathbf{0}, \mathbf{I})$, en est le cas $\boldsymbol{\Sigma} = \mathbf{I}$. Deux conséquences :
- $\Delta^2$ suit, en dimension 2, la loi exponentielle de paramètre $\frac12$ : $P(\Delta^2 \le s) = 1 - e^{-s/2}$ (M02b §3).
- À niveau égal, une ellipse du plan contient **moins** qu'un intervalle de la droite. Pour $c = 1{,}5$ : $P(\lvert Z\rvert \le 1{,}5) \approx 0{,}866$ en dimension 1 ($Z \sim \mathcal{N}(0, 1)$), mais $1 - e^{-1{,}125} \approx 0{,}675$ en dimension 2.

**Pour le GPS**, l'ellipse qui contient 80 % des erreurs a pour niveau $c^2 = 2\ln 5 \approx 3{,}219$ ($c \approx 1{,}794$) : demi-axes $\sqrt{18 \times 3{,}219} \approx 7{,}61$ m et $\sqrt{8 \times 3{,}219} \approx 5{,}07$ m, aire $12\pi \times 2\ln 5 \approx 121{,}3$ m². Celle à 98 % a pour niveau $c^2 = 2\ln 50 \approx 7{,}824$ ($c \approx 2{,}797$) : demi-axes 11,87 m et 7,91 m, aire 295,0 m². Sur les 1 500 tirages de la figure du §1, 1 202 tombent dans la première (80,1 %) et 1 479 dans la seconde (98,6 %).

### En dimension d : le khi-deux, et la loi de la norme

En dimension $d$, $\Delta^2(\mathbf{x}) = \lVert\boldsymbol{\varepsilon}\rVert^2 = \varepsilon_1^2 + \cdots + \varepsilon_d^2$ est une somme de $d$ carrés de variables $\mathcal{N}(0, 1)$ indépendantes. Sa loi porte un nom : la **loi du khi-deux à $d$ degrés de liberté** (*chi-squared distribution*), notée $\chi^2_d$ ; M02b §8 en a calculé le cas $d = 1$, et le cas $d = 2$ est la loi exponentielle ci-dessus. La masse d'un ellipsoïde de niveau $c$ est $P(\chi^2_d \le c^2)$ : elle ne dépend que de $d$ et de $c$. Le 🔮 M25a.25 te fait prédire, puis mesurer, ce qu'elle devient quand la dimension augmente.

La norme $r = \lVert\boldsymbol{\varepsilon}\rVert$ elle-même suit la loi du khi (*chi distribution*) :

> **Propriété** (∂ M25a.11). La norme d'un vecteur de loi $\mathcal{N}(\mathbf{0}, \mathbf{I}_d)$ a une densité de la forme
> $$f_d(r) = C_d\,r^{d-1}e^{-r^2/2} \qquad (r \ge 0),$$
> avec $C_2 = 1$ (la **loi de Rayleigh**, *Rayleigh distribution* : $f_2(r) = r\,e^{-r^2/2}$), $C_3 = \sqrt{2/\pi}$ (la **loi de Maxwell**, celle de la vitesse d'une molécule de gaz), et une constante $C_d$ admise en général. Son **mode**, le $r$ où $f_d$ est maximale, est $\sqrt{d - 1}$.

D'où vient le facteur $r^{d-1}$ : la densité de $\boldsymbol{\varepsilon}$ vaut $(2\pi)^{-d/2}e^{-r^2/2}$ sur toute la sphère de rayon $r$, et l'« aire » de cette sphère est proportionnelle à $r^{d-1}$ (un périmètre $2\pi r$ en dimension 2, une aire $4\pi r^2$ en dimension 3). Deux effets se combattent : la densité baisse quand $r$ grandit, la place disponible augmente.

Le mode est un peu en dessous de $\sqrt d$, la racine de $\mathbb{E}\big[\lVert\boldsymbol{\varepsilon}\rVert^2\big] = d$ (M07 §7) : en dimension 5, 2 contre $\sqrt5 \approx 2{,}24$ ; en dimension 26, 5 contre $\sqrt{26} \approx 5{,}10$. Dans ce dernier cas, la densité de $\boldsymbol{\varepsilon}$ au centre est $e^{25/2} \approx 2{,}7 \times 10^5$ fois plus forte que sur la sphère de rayon 5 ; pourtant la boule de rayon 1 ne contient qu'environ $10^{-14}$ de la masse, et la couronne $4 \le r \le 6$ environ 84 % : **la densité est maximale au centre, la masse est sur une couronne** (la concentration de M07 §7).

![À gauche, la masse d'un intervalle |Z| ≤ c en dimension 1 et celle d'une ellipse de niveau c en dimension 2 (1 − e^(−c²/2)) : 0,866 contre 0,675 pour c = 1,5, et les niveaux c ≈ 1,794 et 2,797 des ellipses à 80 % et 98 % ; à droite, la densité de la norme d'un tirage de N(0, I_d) pour d = 2, 5 et 26, de modes 1, 2 et 5](figures/masse_ellipse.png)

💻 **Aujourd'hui en pratique** — `scipy.stats.chi2(d).ppf(1 - beta)` donne le niveau $c^2$ de l'ellipsoïde de masse $1 - \beta$ en dimension $d$, et `scipy.stats.chi(d)` la loi de la norme. Pour tracer une ellipse de niveau $c$, on applique $\boldsymbol{\varepsilon} \mapsto \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ au cercle de rayon $c$ (🎨 M25a.27).

⚠️ **Erreur classique.** Des demi-axes en $c\,\lambda_i$, ou en $\frac{c}{\sqrt{\lambda_i}}$ : ce dernier vaut pour les lignes de niveau de $\mathbf{x}^\top\boldsymbol{\Sigma}\mathbf{x}$ (M12c §7), pas de $\mathbf{x}^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}$ ; ici, le grand axe suit la **grande** valeur propre. Appliquer $1 - e^{-c^2/2}$ en dimension 3 ou plus, ou en dimension 1. Croire que les tirages se massent près du point de densité maximale.

🔗 **Dans workbookIA** — le chapitre 25 s'appuie sur la loi de la norme d'un tirage de $\mathcal{N}(\mathbf{0}, \mathbf{I})$ en grande dimension, et sur le cas du plan, pour comparer deux façons d'aller d'un tirage à un autre (§8).

## §4 · Matrices par blocs et complément de Schur : lois marginales, lois conditionnelles et matrice de précision

### Découper un vecteur en deux blocs

On sépare les coordonnées de $\mathbf{x} \in \mathbb{R}^d$ en deux groupes, non vides : celles qu'on cherche, le bloc $a$ (de taille $d_a$), et les autres, le bloc $b$ (de taille $d_b = d - d_a$), souvent celles qu'on observe. Quitte à renuméroter, on écrit $\mathbf{x}$ et $\boldsymbol{\Sigma}$ par blocs (*block matrix*) :
$$\mathbf{x} = \begin{pmatrix} \mathbf{x}_a \\ \mathbf{x}_b \end{pmatrix}, \qquad \boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_a \\ \boldsymbol{\mu}_b \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} \boldsymbol{\Sigma}_{aa} & \boldsymbol{\Sigma}_{ab} \\ \boldsymbol{\Sigma}_{ba} & \boldsymbol{\Sigma}_{bb} \end{pmatrix},$$
avec $\boldsymbol{\Sigma}_{aa} = \operatorname{Cov}(\mathbf{x}_a)$, $\boldsymbol{\Sigma}_{bb} = \operatorname{Cov}(\mathbf{x}_b)$, et la **covariance croisée** (*cross-covariance*) $\boldsymbol{\Sigma}_{ab} = \operatorname{Cov}(\mathbf{x}_a, \mathbf{x}_b) = \mathbb{E}\big[(\mathbf{x}_a - \boldsymbol{\mu}_a)(\mathbf{x}_b - \boldsymbol{\mu}_b)^\top\big]$, de forme $(d_a, d_b)$ ; $\boldsymbol{\Sigma}_{ba} = \boldsymbol{\Sigma}_{ab}^\top$. Les blocs d'une matrice $\mathbf{M}$ quelconque s'écrivent de même $\mathbf{M}_{aa}$, $\mathbf{M}_{ab}$, $\mathbf{M}_{ba}$, $\mathbf{M}_{bb}$.

**Exemple : les retards d'un bus.** Un bus passe par trois arrêts ; ses retards $x_1$, $x_2$, $x_3$, en minutes, s'accumulent : $x_1 \sim \mathcal{N}(2, 1)$, puis chaque trajet ajoute un retard indépendant, de loi $\mathcal{N}(1, 1)$ jusqu'au deuxième arrêt et $\mathcal{N}(2, 2)$ jusqu'au troisième. Alors $x_2 = x_1 + (\text{retard du premier trajet})$, $x_3 = x_2 + (\text{retard du second})$, et (M02b §6, M12c §8)
$$\boldsymbol{\mu} = \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 4 \end{pmatrix}, \qquad \mathbf{L} = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & \sqrt2 \end{pmatrix}, \qquad \det\boldsymbol{\Sigma} = 2 .$$
Par exemple, $\operatorname{Cov}(x_1, x_3) = \mathbb{V}(x_1) = 1$ : les retards ajoutés ensuite sont indépendants de $x_1$. On observe le deuxième arrêt : $a = \{1, 3\}$ et $b = \{2\}$, d'où $\boldsymbol{\Sigma}_{aa} = \begin{pmatrix} 1 & 1 \\ 1 & 4 \end{pmatrix}$, $\boldsymbol{\Sigma}_{ab} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ et $\boldsymbol{\Sigma}_{bb} = (2)$.

### Le complément de Schur ; inverse et déterminant par blocs

> **Définition.** Si le bloc $\mathbf{M}_{bb}$ est inversible, le **complément de Schur** (*Schur complement*) de $\mathbf{M}_{bb}$ dans $\mathbf{M}$ est la matrice $(d_a, d_a)$
> $$\mathbf{M}/\mathbf{M}_{bb} = \mathbf{M}_{aa} - \mathbf{M}_{ab}\,\mathbf{M}_{bb}^{-1}\,\mathbf{M}_{ba}.$$
>
> **Théorème** (démonstration ci-dessous). Si $\mathbf{M}_{bb}$ est inversible :
> 1. $\det\mathbf{M} = \det\mathbf{M}_{bb}\cdot\det(\mathbf{M}/\mathbf{M}_{bb})$ ;
> 2. $\mathbf{M}$ est inversible si et seulement si $\mathbf{M}/\mathbf{M}_{bb}$ l'est, et alors les blocs $aa$ et $ab$ de $\mathbf{M}^{-1}$ sont
> $$(\mathbf{M}^{-1})_{aa} = (\mathbf{M}/\mathbf{M}_{bb})^{-1}, \qquad (\mathbf{M}^{-1})_{ab} = -(\mathbf{M}/\mathbf{M}_{bb})^{-1}\mathbf{M}_{ab}\mathbf{M}_{bb}^{-1}.$$

En dimension 2, avec des blocs $1 \times 1$, $\mathbf{M} = \begin{pmatrix} m_{11} & m_{12} \\ m_{21} & m_{22} \end{pmatrix}$ et $m_{22} \ne 0$ : le complément de Schur de $m_{22}$ est le nombre $m_{11} - \frac{m_{12}m_{21}}{m_{22}}$, et $m_{22}\big(m_{11} - \frac{m_{12}m_{21}}{m_{22}}\big) = m_{11}m_{22} - m_{12}m_{21} = \det\mathbf{M}$. Le coin supérieur gauche de $\mathbf{M}^{-1}$ vaut $\frac{m_{22}}{\det\mathbf{M}}$ (M09a), l'inverse de ce complément.

<details><summary>Démonstration (élimination par blocs)</summary>

Posons $\mathbf{G} = \begin{pmatrix} \mathbf{I} & -\mathbf{M}_{ab}\mathbf{M}_{bb}^{-1} \\ \mathbf{0} & \mathbf{I} \end{pmatrix}$ et $\mathbf{H} = \begin{pmatrix} \mathbf{I} & \mathbf{0} \\ -\mathbf{M}_{bb}^{-1}\mathbf{M}_{ba} & \mathbf{I} \end{pmatrix}$. Multiplier à gauche par $\mathbf{G}$ retire au bloc de lignes $a$ la combinaison $\mathbf{M}_{ab}\mathbf{M}_{bb}^{-1}$ du bloc de lignes $b$, comme une étape du pivot de Gauss (M09a) :
$$\mathbf{G}\mathbf{M} = \begin{pmatrix} \mathbf{M}_{aa} - \mathbf{M}_{ab}\mathbf{M}_{bb}^{-1}\mathbf{M}_{ba} & \mathbf{M}_{ab} - \mathbf{M}_{ab} \\ \mathbf{M}_{ba} & \mathbf{M}_{bb} \end{pmatrix} = \begin{pmatrix} \mathbf{M}/\mathbf{M}_{bb} & \mathbf{0} \\ \mathbf{M}_{ba} & \mathbf{M}_{bb} \end{pmatrix}, \qquad \mathbf{G}\mathbf{M}\mathbf{H} = \begin{pmatrix} \mathbf{M}/\mathbf{M}_{bb} & \mathbf{0} \\ \mathbf{0} & \mathbf{M}_{bb} \end{pmatrix}.$$
Le déterminant d'une matrice triangulaire par blocs est le produit des déterminants de ses blocs diagonaux (admis ; c'est le cas par blocs de M12c §1). Donc $\det\mathbf{G} = \det\mathbf{H} = 1$, et $\det\mathbf{M} = \det(\mathbf{M}/\mathbf{M}_{bb})\,\det\mathbf{M}_{bb}$ : c'est le point 1. Il en découle que $\mathbf{M}$ est inversible si et seulement si $\mathbf{M}/\mathbf{M}_{bb}$ l'est (M12c §1). Alors, de $\mathbf{M} = \mathbf{G}^{-1}\operatorname{diag}(\mathbf{M}/\mathbf{M}_{bb}, \mathbf{M}_{bb})\,\mathbf{H}^{-1}$, on tire
$$\mathbf{M}^{-1} = \mathbf{H}\begin{pmatrix} (\mathbf{M}/\mathbf{M}_{bb})^{-1} & \mathbf{0} \\ \mathbf{0} & \mathbf{M}_{bb}^{-1} \end{pmatrix}\mathbf{G},$$
et le produit des trois matrices par blocs donne les quatre blocs de $\mathbf{M}^{-1}$. Fais-le : les blocs $aa$ et $ab$ de l'énoncé viennent en une ligne chacun, puis $(\mathbf{M}^{-1})_{ba} = -\mathbf{M}_{bb}^{-1}\mathbf{M}_{ba}(\mathbf{M}/\mathbf{M}_{bb})^{-1}$ et $(\mathbf{M}^{-1})_{bb} = \mathbf{M}_{bb}^{-1} + \mathbf{M}_{bb}^{-1}\mathbf{M}_{ba}(\mathbf{M}/\mathbf{M}_{bb})^{-1}\mathbf{M}_{ab}\mathbf{M}_{bb}^{-1}$.

</details>

**Sur le bus**, le complément de Schur de $\boldsymbol{\Sigma}_{bb} = (2)$ est
$$\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{bb} = \begin{pmatrix} 1 & 1 \\ 1 & 4 \end{pmatrix} - \frac12\begin{pmatrix} 1 \\ 2 \end{pmatrix}\begin{pmatrix} 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 - \frac12 & 1 - 1 \\ 1 - 1 & 4 - 2 \end{pmatrix} = \begin{pmatrix} 0{,}5 & 0 \\ 0 & 2 \end{pmatrix},$$
et l'on vérifie $\det\boldsymbol{\Sigma} = 2 \times (0{,}5 \times 2) = 2$.

📐 **Notations.** La docstring de `schur_complement` écrit $\mathbf{M}$ en quatre blocs $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$ (le bloc $\mathbf{D}$ étant celui qu'on élimine) et le complément $\mathbf{A} - \mathbf{B}\mathbf{D}^{-1}\mathbf{C}$ : c'est $\mathbf{M}/\mathbf{M}_{bb}$, avec $\mathbf{D} = \mathbf{M}_{bb}$. La fiche garde les indices $a$ et $b$, pour que les lettres $\mathbf{A}$ et $\mathbf{b}$ restent celles d'une transformation affine : $\boldsymbol{\Sigma}_{bb}$ est un bloc, $\mathbf{b}$ une translation.

### Les lois marginales : garder les sous-blocs

> **Propriété.** $\mathbf{x}_a \sim \mathcal{N}(\boldsymbol{\mu}_a, \boldsymbol{\Sigma}_{aa})$ : la **loi marginale** (*marginal distribution*) d'un bloc s'obtient en gardant ses moyennes et sa sous-matrice de covariance.

C'est le §2, avec la matrice $\begin{pmatrix} \mathbf{I} & \mathbf{0} \end{pmatrix}$ qui garde les coordonnées du bloc $a$. MML (6.68) l'écrit comme l'intégrale de la densité jointe sur $\mathbf{x}_b$ ; ici, aucune intégrale n'est à calculer. Pour le bus, le retard au troisième arrêt suit $\mathcal{N}(5, 4)$, et le couple $(x_1, x_3)$ suit $\mathcal{N}\big((2, 5), \boldsymbol{\Sigma}_{aa}\big)$.

### Décorrélé équivaut à indépendant

> **Propriété.** Pour un vecteur gaussien, $\mathbf{x}_a$ et $\mathbf{x}_b$ sont indépendants si et seulement si $\boldsymbol{\Sigma}_{ab} = \mathbf{0}$.

L'indépendance donne toujours une covariance nulle. Dans l'autre sens (pour $\boldsymbol{\Sigma}$ définie positive ; le cas dégénéré est admis) : si $\boldsymbol{\Sigma}_{ab} = \mathbf{0}$, alors $\boldsymbol{\Sigma}^{-1} = \operatorname{diag}(\boldsymbol{\Sigma}_{aa}^{-1}, \boldsymbol{\Sigma}_{bb}^{-1})$ et $\det\boldsymbol{\Sigma} = \det\boldsymbol{\Sigma}_{aa}\det\boldsymbol{\Sigma}_{bb}$, donc $\Delta^2$ se coupe en deux termes, $(\mathbf{x}_a - \boldsymbol{\mu}_a)^\top\boldsymbol{\Sigma}_{aa}^{-1}(\mathbf{x}_a - \boldsymbol{\mu}_a) + (\mathbf{x}_b - \boldsymbol{\mu}_b)^\top\boldsymbol{\Sigma}_{bb}^{-1}(\mathbf{x}_b - \boldsymbol{\mu}_b)$, et la densité jointe est le produit des deux densités marginales : c'est l'indépendance (M02b §7). Le contre-exemple du §2 montre que l'hypothèse « vecteur gaussien » ne peut pas être remplacée par « coordonnées gaussiennes ».

### La loi conditionnelle

Pour des variables à densité, la **loi conditionnelle** (*conditional distribution*) de $\mathbf{x}_a$ sachant $\mathbf{x}_b$ a pour densité $p(\mathbf{x}_a \mid \mathbf{x}_b) = \frac{p(\mathbf{x}_a, \mathbf{x}_b)}{p(\mathbf{x}_b)}$ : la **coupe** de la densité jointe à $\mathbf{x}_b$ fixé, divisée par son aire pour que l'intégrale vaille 1 (la version continue de M03).

> **Théorème.** Si $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ avec $\boldsymbol{\Sigma}_{bb}$ inversible, la loi de $\mathbf{x}_a$ sachant $\mathbf{x}_b$ est normale :
> $$\mathbf{x}_a \mid \mathbf{x}_b \sim \mathcal{N}(\boldsymbol{\mu}_{a \mid b}, \boldsymbol{\Sigma}_{a \mid b}), \qquad \boldsymbol{\mu}_{a \mid b} = \boldsymbol{\mu}_a + \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}(\mathbf{x}_b - \boldsymbol{\mu}_b), \qquad \boldsymbol{\Sigma}_{a \mid b} = \boldsymbol{\Sigma}_{aa} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba} = \boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{bb}.$$

Comment le lire :
- la **moyenne conditionnelle** est une fonction **affine** de la valeur lue $\mathbf{x}_b$ : elle part de $\boldsymbol{\mu}_a$ et se corrige de l'écart observé $\mathbf{x}_b - \boldsymbol{\mu}_b$, multiplié par $\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}$ (c'est la prédiction linéaire de M09b, avec les vraies covariances) ;
- la **covariance conditionnelle** est le complément de Schur : elle n'est **jamais plus grande** que $\boldsymbol{\Sigma}_{aa}$ (on lui retire la matrice semi-définie positive $\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}$, nulle seulement si $\boldsymbol{\Sigma}_{ab} = \mathbf{0}$), et elle **ne dépend pas de la valeur lue** : on sait d'avance combien une mesure réduira l'incertitude, avant de la faire ;
- si $\boldsymbol{\Sigma}_{ab} = \mathbf{0}$, rien ne change : on retrouve la loi marginale (les blocs sont indépendants).

<details><summary>Démonstration (par un résidu indépendant de la mesure)</summary>

Posons $\mathbf{r} = \mathbf{x}_a - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\mathbf{x}_b$ : ce qui reste de $\mathbf{x}_a$ quand on retire sa meilleure prédiction linéaire à partir de $\mathbf{x}_b$. Le vecteur $(\mathbf{r}, \mathbf{x}_b)$ est une image linéaire de $\mathbf{x}$, donc un vecteur gaussien (§2), et
$$\operatorname{Cov}(\mathbf{r}, \mathbf{x}_b) = \boldsymbol{\Sigma}_{ab} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{bb} = \mathbf{0}.$$
Par la propriété précédente, $\mathbf{r}$ est **indépendant** de $\mathbf{x}_b$. Sa moyenne est $\boldsymbol{\mu}_a - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\mu}_b$, et sa covariance (M12c §8, en développant) est
$$\boldsymbol{\Sigma}_{aa} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba} + \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{bb}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba} = \boldsymbol{\Sigma}_{aa} - \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}.$$
Or $\mathbf{x}_a = \mathbf{r} + \boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\mathbf{x}_b$. Quand on connaît $\mathbf{x}_b$, le second terme est une constante connue, et $\mathbf{r}$, indépendant de $\mathbf{x}_b$, garde sa loi. La loi de $\mathbf{x}_a$ sachant $\mathbf{x}_b$ est donc celle de $\mathbf{r}$ décalée de $\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\mathbf{x}_b$ : la normale de l'énoncé.

</details>

**Sur le bus.** Le bus a 5 minutes de retard au deuxième arrêt ($x_2 = 5$, soit 2 de plus que la moyenne). Alors
$$\boldsymbol{\mu}_{a \mid b} = \begin{pmatrix} 2 \\ 5 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \end{pmatrix}\frac{5 - 3}{2} = \begin{pmatrix} 3 \\ 7 \end{pmatrix}, \qquad \boldsymbol{\Sigma}_{a \mid b} = \begin{pmatrix} 0{,}5 & 0 \\ 0 & 2 \end{pmatrix}.$$
Le retard au troisième arrêt passe de $\mathcal{N}(5, 4)$ à $\mathcal{N}(7, 2)$ : son écart-type passe de 2 à $\sqrt2 \approx 1{,}414$ minute, et il en serait de même pour toute autre valeur lue. On le comprend sans formule : sachant $x_2$, il reste à ajouter le retard du second trajet, de loi $\mathcal{N}(2, 2)$. Le retard au premier arrêt, lui, passe de $\mathcal{N}(2, 1)$ à $\mathcal{N}(3 ;\ 0{,}5)$ : lire un arrêt renseigne aussi sur le passé.

![À gauche, les lignes de niveau de la loi jointe des retards (x₂, x₃) du bus, la droite des moyennes conditionnelles 5 + (x₂ − 3), et la coupe x₂ = 5 qui la croise en 7 ; à droite, la loi marginale N(5, 4) de x₃ et sa loi conditionnelle N(7, 2) sachant x₂ = 5 : décalée et plus étroite](figures/conditionnement.png)

### En dimension 2, avec la corrélation

Pour un couple $(x_1, x_2)$ d'écarts-types $\sigma_1$, $\sigma_2$ et de corrélation $\rho$ ($\Sigma_{12} = \rho\sigma_1\sigma_2$), le théorème donne
$$x_1 \mid x_2 \sim \mathcal{N}\Big(\mu_1 + \rho\,\frac{\sigma_1}{\sigma_2}(x_2 - \mu_2),\ \sigma_1^2(1 - \rho^2)\Big).$$
La part de variance qui disparaît est $\rho^2$ : rien pour $\rho = 0$, presque tout quand $\lvert\rho\rvert \to 1$ (la loi devient dégénérée). Pour le GPS, $\rho = \frac{1}{\sqrt{10}}$ : connaître l'erreur vers le nord fait passer la variance de l'erreur vers l'est de 16 à $16 \times 0{,}9 = 14{,}4$ (écart-type 3,79 m au lieu de 4 m), avec la moyenne $2 + 0{,}4\,(x_2 + 4)$, soit 4 m si $x_2 = 1$ m.

### La matrice de précision et l'indépendance conditionnelle

> **Définition.** La **matrice de précision** (*precision matrix*) d'une loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ est $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$, découpée en blocs $\boldsymbol{\Lambda}_{aa}$, $\boldsymbol{\Lambda}_{ab}$… En dimension 1, c'est $\frac{1}{\sigma^2}$ : une grande précision, une petite variance.
>
> **Propriétés.**
> 1. $\boldsymbol{\Sigma}_{a \mid b} = \boldsymbol{\Lambda}_{aa}^{-1}$ et $\boldsymbol{\mu}_{a \mid b} = \boldsymbol{\mu}_a - \boldsymbol{\Lambda}_{aa}^{-1}\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b - \boldsymbol{\mu}_b)$. En particulier, sachant **toutes** les autres coordonnées, $x_i$ a la variance $\frac{1}{\Lambda_{ii}}$.
> 2. Pour $i \ne j$, $\Lambda_{ij} = 0$ si et seulement si $x_i$ et $x_j$ sont **indépendantes sachant toutes les autres coordonnées** (*conditional independence*).

Le point 1 est le théorème par blocs appliqué à $\boldsymbol{\Sigma}$ : le bloc $aa$ de $\boldsymbol{\Sigma}^{-1}$ est $(\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{bb})^{-1}$, et son bloc $ab$ donne $\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1} = -\boldsymbol{\Lambda}_{aa}^{-1}\boldsymbol{\Lambda}_{ab}$. Pour le point 2, avec $a = \{i, j\}$, la covariance conditionnelle de $(x_i, x_j)$ est l'inverse de $\begin{pmatrix} \Lambda_{ii} & \Lambda_{ij} \\ \Lambda_{ij} & \Lambda_{jj} \end{pmatrix}$, diagonale exactement quand $\Lambda_{ij} = 0$ ; et pour cette loi gaussienne, décorrélé équivaut à indépendant.

**Sur le bus.**
$$\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1} = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 1{,}5 & -0{,}5 \\ 0 & -0{,}5 & 0{,}5 \end{pmatrix}.$$
Le zéro en position $(1, 3)$ dit que, **sachant le retard au deuxième arrêt**, les retards au premier et au troisième sont indépendants : le troisième ne dépend du premier qu'à travers le deuxième. Ils ne sont pas indépendants tout court ($\Sigma_{13} = 1$, une corrélation de $\frac{1}{1 \times 2} = 0{,}5$). On retrouve la covariance conditionnelle diagonale trouvée plus haut, inverse de $\boldsymbol{\Lambda}_{aa} = \operatorname{diag}(2 ;\ 0{,}5)$. Sachant $x_2$ et $x_3$, $x_1$ a la variance $\frac{1}{\Lambda_{11}} = 0{,}5$ et la moyenne $2 - \frac12\big[(-1)(x_2 - 3) + 0 \times (x_3 - 5)\big] = 2 + \frac{x_2 - 3}{2}$ : $x_3$ n'y apparaît pas.

Retiens le contraste : un **zéro de $\boldsymbol{\Sigma}$** dit une indépendance (marginale), un **zéro de $\boldsymbol{\Lambda}$** une indépendance conditionnelle. L'hypothèse de Naïve Bayes (M13a §5) est une indépendance conditionnelle (sachant la classe).

💻 **Aujourd'hui en pratique** — on conditionne avec `np.linalg.solve(S_bb, x_b - mu_b)`, jamais en inversant $\boldsymbol{\Sigma}$, et l'on prend les blocs avec `np.ix_(rest, idx)` : c'est ce que font `schur_complement` et `condition_gaussian` (🔨 M25a.22). Le filtre de Kalman (*Kalman filter* : suivre un véhicule à partir de mesures bruitées) et les processus gaussiens (interpoler une grandeur entre des points mesurés, 🏆 M25a.30) sont des conditionnements gaussiens. Conditionner par simulation, en gardant les tirages dont la mesure tombe près de la valeur lue, est l'objet du 🔬 M25a.26.

⚠️ **Erreur classique.** Croire que la covariance conditionnelle dépend de la valeur lue (🐛 M25a.28) : seule la moyenne en dépend. Multiplier par $\boldsymbol{\Sigma}_{bb}$ au lieu de $\boldsymbol{\Sigma}_{bb}^{-1}$. Confondre la loi marginale ($\boldsymbol{\Sigma}_{aa}$) et la loi conditionnelle ($\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{bb}$). Confondre $(\boldsymbol{\Sigma}^{-1})_{aa}$, le bloc de l'inverse, et $(\boldsymbol{\Sigma}_{aa})^{-1}$, l'inverse du bloc.

🔗 **Dans ce dépôt** — M25b conditionne une loi gaussienne pour trouver la loi a posteriori d'une variable cachée (l'ACP probabiliste) ; MB5 aussi, pour les modèles de diffusion.

## §5 · Bayes avec des gaussiennes : produit de densités, modèle linéaire gaussien et régression linéaire bayésienne

### Le produit de deux densités

En dimension 1, $\mathcal{N}(x \mid \mu_1, \sigma_1^2)\,\mathcal{N}(x \mid \mu_2, \sigma_2^2)$, vu comme une fonction de $x$, est l'exponentielle de
$$-\frac{(x - \mu_1)^2}{2\sigma_1^2} - \frac{(x - \mu_2)^2}{2\sigma_2^2} = -\frac12\Big(\frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2}\Big)x^2 + \Big(\frac{\mu_1}{\sigma_1^2} + \frac{\mu_2}{\sigma_2^2}\Big)x + \text{constante},$$
un polynôme du second degré en $x$, de coefficient dominant négatif. En complétant le carré (*completing the square*, R3), c'est $-\frac{(x - \mu_3)^2}{2\sigma_3^2} + \text{constante}$, avec $\frac{1}{\sigma_3^2} = \frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2}$ et $\frac{\mu_3}{\sigma_3^2} = \frac{\mu_1}{\sigma_1^2} + \frac{\mu_2}{\sigma_2^2}$. En dimension $d$, le même calcul (MML ex. 6.10) donne :

> **Propriété** (MML §6.5.2). Pour $\boldsymbol{\Sigma}_1$ et $\boldsymbol{\Sigma}_2$ définies positives,
> $$\mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)\,\mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_2, \boldsymbol{\Sigma}_2) = \kappa\,\mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_3, \boldsymbol{\Sigma}_3),$$
> $$\boldsymbol{\Sigma}_3^{-1} = \boldsymbol{\Sigma}_1^{-1} + \boldsymbol{\Sigma}_2^{-1}, \qquad \boldsymbol{\mu}_3 = \boldsymbol{\Sigma}_3\big(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\mu}_1 + \boldsymbol{\Sigma}_2^{-1}\boldsymbol{\mu}_2\big), \qquad \kappa = \mathcal{N}(\boldsymbol{\mu}_1 \mid \boldsymbol{\mu}_2, \boldsymbol{\Sigma}_1 + \boldsymbol{\Sigma}_2).$$
> **Les précisions s'additionnent**, et la nouvelle moyenne est la moyenne des deux, **pondérée par leurs précisions**.

Le produit n'est pas une densité (son intégrale vaut $\kappa$), mais une gaussienne multipliée par une constante ; $\kappa$ est grande quand $\boldsymbol{\mu}_1$ et $\boldsymbol{\mu}_2$ sont proches à l'échelle de $\boldsymbol{\Sigma}_1 + \boldsymbol{\Sigma}_2$. Comme les précisions s'additionnent, le produit de trois densités ou plus se fait dans **n'importe quel ordre**.

### Fusionner des mesures

C'est la règle de Bayes (M04) quand l'a priori et la vraisemblance sont gaussiens. Une carte donne l'altitude d'un refuge : $x \sim \mathcal{N}(1\,520, 10^2)$ a priori, en mètres. Un baromètre la mesure, $y = x + w$ avec une erreur $w \sim \mathcal{N}(0, 20^2)$, et lit $y = 1\,540$. Vue comme une fonction de $x$, la vraisemblance $\mathcal{N}(y \mid x, 20^2)$ est aussi $\mathcal{N}(x \mid y, 20^2)$ (la formule est symétrique en $x$ et $y$). L'a posteriori est proportionnel au produit :
$$\frac{1}{\sigma_3^2} = \frac{1}{100} + \frac{1}{400} = \frac{5}{400}, \qquad \sigma_3^2 = 80, \qquad \mu_3 = 80\Big(\frac{1\,520}{100} + \frac{1\,540}{400}\Big) = 1\,524 .$$
Après la mesure, $x \sim \mathcal{N}(1\,524, 80)$, d'écart-type $8{,}94$ m : plus précis que chacune des deux sources (10 m et 20 m), et plus proche de la plus précise. Une source de variance infinie (de précision nulle) ne changerait rien ; une mesure de variance nulle imposerait sa valeur. La constante $\kappa = \mathcal{N}(1\,520 \mid 1\,540, 500) = \frac{e^{-0{,}4}}{\sqrt{2\pi \times 500}} \approx 0{,}0120$ est la densité de la valeur lue avant la mesure : l'**évidence** de M04.

### Le modèle linéaire gaussien

> **Modèle linéaire gaussien** (*linear Gaussian model*). Un vecteur caché $\mathbf{x} \sim \mathcal{N}(\mathbf{m}, \mathbf{V})$ ; une observation $\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{b} + \mathbf{w}$, avec un bruit $\mathbf{w} \sim \mathcal{N}(\mathbf{0}, \mathbf{R})$ indépendant de $\mathbf{x}$. Alors :
> - **la loi jointe** : $\begin{pmatrix} \mathbf{x} \\ \mathbf{y} \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} \mathbf{m} \\ \mathbf{A}\mathbf{m} + \mathbf{b} \end{pmatrix}, \begin{pmatrix} \mathbf{V} & \mathbf{V}\mathbf{A}^\top \\ \mathbf{A}\mathbf{V} & \mathbf{A}\mathbf{V}\mathbf{A}^\top + \mathbf{R} \end{pmatrix}\right)$ ;
> - **la loi marginale** de l'observation : $\mathbf{y} \sim \mathcal{N}(\mathbf{A}\mathbf{m} + \mathbf{b},\ \mathbf{A}\mathbf{V}\mathbf{A}^\top + \mathbf{R})$ ;
> - **la loi de $\mathbf{x}$ sachant $\mathbf{y}$** : de covariance $\mathbf{V} - \mathbf{V}\mathbf{A}^\top(\mathbf{A}\mathbf{V}\mathbf{A}^\top + \mathbf{R})^{-1}\mathbf{A}\mathbf{V}$ et de moyenne $\mathbf{m} + \mathbf{V}\mathbf{A}^\top(\mathbf{A}\mathbf{V}\mathbf{A}^\top + \mathbf{R})^{-1}(\mathbf{y} - \mathbf{A}\mathbf{m} - \mathbf{b})$.

Tout vient des §2 et §4 : $(\mathbf{x}, \mathbf{y})$ est l'image linéaire, plus une constante, du vecteur gaussien $(\mathbf{x}, \mathbf{w})$ ; $\operatorname{Cov}(\mathbf{x}, \mathbf{y}) = \operatorname{Cov}(\mathbf{x}, \mathbf{A}\mathbf{x} + \mathbf{w}) = \mathbf{V}\mathbf{A}^\top$ ; la marginale est un sous-bloc, et la loi de $\mathbf{x}$ sachant $\mathbf{y}$ est le théorème du §4. La même covariance a posteriori s'écrit aussi $(\mathbf{V}^{-1} + \mathbf{A}^\top\mathbf{R}^{-1}\mathbf{A})^{-1}$, sous la forme « les précisions s'additionnent » (l'égalité des deux écritures est admise ; c'est l'identité de Woodbury).

**Exemple : deux pièces pesées ensemble.** Deux pièces ont des masses $x_1$ et $x_2$ mal connues : $\mathbf{x} \sim \mathcal{N}\big((40, 25), \operatorname{diag}(4, 9)\big)$, en grammes. Une balance d'écart-type 1 g ne peut les peser qu'ensemble : $y = x_1 + x_2 + w$, soit $\mathbf{A} = \begin{pmatrix} 1 & 1 \end{pmatrix}$, $\mathbf{b} = 0$, $\mathbf{R} = (1)$, et $y \sim \mathcal{N}(65, 14)$ avant la pesée. La balance affiche 72 g. Avec $\mathbf{V}\mathbf{A}^\top = (4, 9)$ :
$$\text{moyenne} = \begin{pmatrix} 40 \\ 25 \end{pmatrix} + \begin{pmatrix} 4 \\ 9 \end{pmatrix}\frac{72 - 65}{14} = \begin{pmatrix} 42 \\ 29{,}5 \end{pmatrix}, \qquad \text{covariance} = \begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix} - \frac{1}{14}\begin{pmatrix} 16 & 36 \\ 36 & 81 \end{pmatrix} = \begin{pmatrix} 20/7 & -18/7 \\ -18/7 & 45/14 \end{pmatrix}.$$
Les 7 g d'excès se partagent dans le rapport des variances a priori, $4 : 9$ (le dernier demi-gramme revient au bruit de la balance), et la pesée crée une **corrélation négative**, de $-0{,}849$, entre les deux masses : leur somme est presque connue.

### La régression linéaire bayésienne

M09b ajustait des poids par moindres carrés, puis voyait ridge comme un MAP. La **régression linéaire bayésienne** (*Bayesian linear regression*, MML §9.3) garde toute la loi a posteriori des poids. Le modèle :
$$\boldsymbol{\theta} \sim \mathcal{N}(\mathbf{m}_0, \mathbf{S}_0) \ \text{a priori}, \qquad \mathbf{y} = \boldsymbol{\Phi}\boldsymbol{\theta} + \mathbf{w}, \quad \mathbf{w} \sim \mathcal{N}(\mathbf{0}, \sigma^2\mathbf{I}),$$
où $\boldsymbol{\theta} \in \mathbb{R}^K$ sont les poids, et la matrice $\boldsymbol{\Phi}$, de forme $(n, K)$, a pour ligne $i$ les features $\boldsymbol{\phi}(\mathbf{x}_i)^\top$ de l'exemple $i$ ; $\sigma^2$ est la variance du bruit, supposée connue.

> **Théorème** (MML Théorème 9.1). La loi a posteriori des poids est $\boldsymbol{\theta} \mid \mathbf{y} \sim \mathcal{N}(\mathbf{m}_N, \mathbf{S}_N)$, avec
> $$\mathbf{S}_N = \big(\mathbf{S}_0^{-1} + \sigma^{-2}\boldsymbol{\Phi}^\top\boldsymbol{\Phi}\big)^{-1}, \qquad \mathbf{m}_N = \mathbf{S}_N\big(\mathbf{S}_0^{-1}\mathbf{m}_0 + \sigma^{-2}\boldsymbol{\Phi}^\top\mathbf{y}\big).$$

C'est un modèle linéaire gaussien, avec $\mathbf{x} = \boldsymbol{\theta}$, $\mathbf{A} = \boldsymbol{\Phi}$, $\mathbf{b} = \mathbf{0}$ et $\mathbf{R} = \sigma^2\mathbf{I}$, écrit sous la forme « précisions » : la précision a priori $\mathbf{S}_0^{-1}$ et celle qu'apportent les données, $\sigma^{-2}\boldsymbol{\Phi}^\top\boldsymbol{\Phi}$, s'additionnent. MML le démontre en complétant le carré dans le logarithme du produit « vraisemblance × a priori ». Sans données ($n = 0$), $\mathbf{S}_N = \mathbf{S}_0$ et $\mathbf{m}_N = \mathbf{m}_0$ : l'a posteriori est l'a priori. Si $\mathbf{S}_0^{-1} \to \mathbf{0}$ (a priori très vague), $\mathbf{m}_N$ tend vers la solution des moindres carrés (quand $\boldsymbol{\Phi}^\top\boldsymbol{\Phi}$ est inversible) ; si $\mathbf{S}_0 \to \mathbf{0}$, $\mathbf{m}_N$ reste $\mathbf{m}_0$ : les données ne pèsent plus.

**Le lien avec ridge.** Avec $\mathbf{m}_0 = \mathbf{0}$ et $\mathbf{S}_0 = \tau^2\mathbf{I}$ :
$$\mathbf{m}_N = \big(\tau^{-2}\mathbf{I} + \sigma^{-2}\boldsymbol{\Phi}^\top\boldsymbol{\Phi}\big)^{-1}\sigma^{-2}\boldsymbol{\Phi}^\top\mathbf{y} = \Big(\boldsymbol{\Phi}^\top\boldsymbol{\Phi} + \frac{\sigma^2}{\tau^2}\mathbf{I}\Big)^{-1}\boldsymbol{\Phi}^\top\mathbf{y}$$
(en mettant $\sigma^{-2}$ en facteur) : la moyenne a posteriori est **la solution ridge de M09b, de pénalité $\frac{\sigma^2}{\tau^2}$**. Pour une loi normale, la moyenne est aussi le mode : c'est le MAP de M09b §5. La loi bayésienne y ajoute $\mathbf{S}_N$ : l'incertitude qui reste sur les poids.

**Exemple : l'allongement d'un ressort.** On suspend des masses $F$ (en kg) à un ressort et on mesure son allongement $y$ (en cm) : $y = \theta F + w$, où $\theta$ est l'allongement par kilogramme et $w$ un bruit de variance $\sigma^2 = 0{,}25$ (un écart-type de 0,5 cm). Un seul paramètre, $K = 1$, et $\phi(F) = F$. La notice du ressort annonce environ 2 cm/kg : $\theta \sim \mathcal{N}(2, 1)$. Trois mesures : $F = 1, 2, 3$ et $y = 2{,}1 ;\ 3{,}9 ;\ 6{,}2$. Alors $\boldsymbol{\Phi}^\top\boldsymbol{\Phi} = \sum_iF_i^2 = 14$ et $\boldsymbol{\Phi}^\top\mathbf{y} = \sum_iF_iy_i = 28{,}5$, d'où
$$S_N = \frac{1}{1 + 14/0{,}25} = \frac{1}{57} \approx 0{,}01754, \qquad m_N = \frac{1}{57}\Big(\frac21 + \frac{28{,}5}{0{,}25}\Big) = \frac{116}{57} \approx 2{,}0351 .$$
L'écart-type de $\theta$ passe de 1 à $\sqrt{1/57} \approx 0{,}132$ cm/kg. Les moindres carrés seuls donnaient $\frac{28{,}5}{14} \approx 2{,}0357$ : avec 3 mesures précises, l'a priori ne pèse presque plus. Avec un a priori centré, $\mathcal{N}(0, 1)$, on trouverait la solution ridge $\frac{28{,}5}{14 + 0{,}25} = 2$.

### Prédire : la prédictive

Pour une nouvelle entrée de features $\boldsymbol{\phi}_\star$, la prédiction $y_\star = \boldsymbol{\phi}_\star^\top\boldsymbol{\theta} + w_\star$ est la somme d'une image linéaire de $\boldsymbol{\theta}$ et d'un bruit indépendant (§2) :
$$y_\star \mid \mathbf{y} \sim \mathcal{N}\big(\boldsymbol{\phi}_\star^\top\mathbf{m}_N,\ \boldsymbol{\phi}_\star^\top\mathbf{S}_N\boldsymbol{\phi}_\star + \sigma^2\big),$$
la **loi prédictive a posteriori** (*posterior predictive distribution*). Sa variance a deux parts : l'incertitude sur les poids, $\boldsymbol{\phi}_\star^\top\mathbf{S}_N\boldsymbol{\phi}_\star$, qui diminue quand les données s'accumulent, et le bruit, $\sigma^2$, qui reste. Avec $\mathbf{m}_0$ et $\mathbf{S}_0$, c'est la prédictive **a priori** ; sans le $\sigma^2$, la loi de la valeur sans bruit $\boldsymbol{\phi}_\star^\top\boldsymbol{\theta}$.

Pour le ressort, à $F_\star = 1$ kg : $\mathcal{N}(2{,}035 ;\ 0{,}2675)$, d'écart-type 0,517 cm ; à $F_\star = 5$ kg, loin des mesures : $\mathcal{N}(10{,}175 ;\ 0{,}6886)$, d'écart-type 0,830 cm. Avant les mesures, la prédictive à 5 kg était $\mathcal{N}(10 ;\ 25{,}25)$.

![La régression bayésienne du ressort y = θF + w, σ² = 0,25 : a priori θ ~ N(2, 1), puis après 1, 3 et 12 mesures ; la droite moyenne, la bande de la droite θF et la bande plus large de la prédictive (± 2 écarts-types) se resserrent quand les mesures s'accumulent, et s'élargissent avec F](figures/regression_bayesienne.png)

### La vraisemblance marginale

L'**évidence**, ou **vraisemblance marginale** (*marginal likelihood*, *evidence*), est la densité des observations, poids intégrés : $p(\mathbf{y}) = \int p(\mathbf{y} \mid \boldsymbol{\theta})\,p(\boldsymbol{\theta})\,\mathrm{d}\boldsymbol{\theta}$. C'est la marginale du modèle linéaire gaussien :
$$p(\mathbf{y}) = \mathcal{N}\big(\mathbf{y} \mid \boldsymbol{\Phi}\mathbf{m}_0,\ \boldsymbol{\Phi}\mathbf{S}_0\boldsymbol{\Phi}^\top + \sigma^2\mathbf{I}\big)$$
(MML (9.64)), une densité de dimension $n$. Elle juge un **modèle** (un a priori, des features, un $\sigma^2$), pas des poids : c'est elle que compare le facteur de Bayes de M08. Pour le ressort, $\boldsymbol{\Phi}$ est la colonne $(1, 2, 3)$, la moyenne $(2, 4, 6)$ et la covariance $\boldsymbol{\Phi}\boldsymbol{\Phi}^\top + 0{,}25\,\mathbf{I}$ ; on trouve $\ln p(\mathbf{y}) \approx -2{,}784$. Avec un a priori beaucoup plus vague, $\mathcal{N}(2, 100)$, on trouverait $\ln p(\mathbf{y}) \approx -5{,}077$ : un modèle qui étale ses prédictions sur trop de valeurs donne moins de densité à celles qu'on observe.

📐 **Notations.** MML §9.3 écrit aussi $\boldsymbol{\theta}$, $\boldsymbol{\Phi}$, $\mathbf{m}_0$, $\mathbf{S}_0$, $\mathbf{m}_N$, $\mathbf{S}_N$ et $\sigma^2$ ; il note le bruit $\epsilon$, une entrée nouvelle $\mathbf{x}_*$, et, au §9.3.5, $\mathbf{X}$ pour $\boldsymbol{\Phi}$. La docstring de `linreg_posterior` note $p$ le nombre de poids (ici $K$, pour ne pas le confondre avec une densité). Au §6, $\mathbf{S}$ sans indice est une autre matrice, celle de dispersion des données.

💻 **Aujourd'hui en pratique** — `sklearn.linear_model.BayesianRidge` fait cette régression et choisit en plus $\sigma^2$ et $\tau^2$ en rendant l'évidence maximale. Tu écris `linreg_posterior` en 🔨 M25a.23, par la forme « précisions » et `np.linalg.solve`. Le filtre de Kalman répète à chaque instant un modèle linéaire gaussien (MML ex. 6.5).

⚠️ **Erreur classique.** Additionner les variances au lieu des précisions quand on fusionne deux mesures (on trouverait une incertitude plus grande que chacune). Confondre le produit de deux densités (gaussien à un facteur près) et le produit de deux variables (pas gaussien, §2). Oublier le $\sigma^2$ dans la prédictive.

## §6 · Estimer μ et Σ : le maximum de vraisemblance et le gradient de ln det

### La log-vraisemblance

On observe $n$ vecteurs $\mathbf{x}_1, \ldots, \mathbf{x}_n$ de $\mathbb{R}^d$, supposés i.i.d. de loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, et l'on cherche les paramètres qui les rendent les plus vraisemblables (M13a §1). La log-vraisemblance est la somme des log-densités du §1 :
$$\ell(\boldsymbol{\mu}, \boldsymbol{\Sigma}) = -\frac{nd}{2}\ln(2\pi) - \frac n2\ln\det\boldsymbol{\Sigma} - \frac12\sum_{i=1}^n(\mathbf{x}_i - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}_i - \boldsymbol{\mu}).$$
On note $\bar{\mathbf{x}} = \frac1n\sum_i\mathbf{x}_i$ la moyenne des données et $\mathbf{S} = \sum_i(\mathbf{x}_i - \bar{\mathbf{x}})(\mathbf{x}_i - \bar{\mathbf{x}})^\top$ leur **matrice de dispersion** (*scatter matrix*), $(d, d)$, symétrique semi-définie positive.

### Les estimations

> **Théorème** (∂ M25a.12). Si $\mathbf{S}$ est définie positive, $\ell$ est maximale en
> $$\hat{\boldsymbol{\mu}} = \bar{\mathbf{x}}, \qquad \hat{\boldsymbol{\Sigma}} = \frac{\mathbf{S}}{n} = \frac1n\sum_{i=1}^n(\mathbf{x}_i - \bar{\mathbf{x}})(\mathbf{x}_i - \bar{\mathbf{x}})^\top .$$

Pour $d = 1$, on retrouve M13a §1 : $\hat\mu = \bar x$ et $\hat\sigma^2 = \frac1n\sum_i(x_i - \bar x)^2$. Les idées de la démonstration :
- **pour $\boldsymbol{\mu}$**, à $\boldsymbol{\Sigma}$ fixée : le gradient de $\sum_i(\mathbf{x}_i - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}_i - \boldsymbol{\mu})$ par rapport à $\boldsymbol{\mu}$ (M09b §2) s'annule en $\bar{\mathbf{x}}$, quelle que soit $\boldsymbol{\Sigma}$ ;
- **pour $\boldsymbol{\Sigma}$** : on écrit $\ell$ en fonction de la précision $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$, avec $\ln\det\boldsymbol{\Sigma} = -\ln\det\boldsymbol{\Lambda}$ et l'astuce de la trace, $\mathbf{z}^\top\boldsymbol{\Lambda}\mathbf{z} = \operatorname{tr}(\boldsymbol{\Lambda}\mathbf{z}\mathbf{z}^\top)$ (M12c §2) ; il reste un $\ln\det$ et une trace linéaire en $\boldsymbol{\Lambda}$, dont M18 §7 donne les gradients :
$$\nabla_{\mathbf{Z}}\ln\det\mathbf{Z} = \mathbf{Z}^{-\top}\ (\det\mathbf{Z} > 0), \qquad \nabla_{\mathbf{Z}}\operatorname{tr}(\mathbf{A}\mathbf{Z}) = \mathbf{A}^\top$$
(M18 écrivait $\mathbf{X}$ la matrice variable ; la fiche réserve $\mathbf{X}$ aux données rangées en lignes).
Le ∂ M25a.12 mène le calcul, et justifie qu'il s'agit bien d'un maximum. C'est la promesse de M18 : le gradient de $\ln\det$ revient avec la densité de la gaussienne multivariée.

Au maximum, $\sum_i(\mathbf{x}_i - \bar{\mathbf{x}})^\top\hat{\boldsymbol{\Sigma}}^{-1}(\mathbf{x}_i - \bar{\mathbf{x}}) = \operatorname{tr}(\hat{\boldsymbol{\Sigma}}^{-1}\mathbf{S}) = \operatorname{tr}(n\mathbf{I}) = nd$, donc
$$\ell(\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Sigma}}) = -\frac n2\Big[d\ln(2\pi) + \ln\det\hat{\boldsymbol{\Sigma}} + d\Big].$$

**Exemple.** Quatre relevés simultanés de deux jauges de niveau, en centimètres : $(1, 2)$, $(3, 3)$, $(2, 5)$ et $(6, 6)$. Leur moyenne est $\bar{\mathbf{x}} = (3, 4)$, et les écarts $(-2, -2)$, $(0, -1)$, $(-1, 1)$, $(3, 2)$ donnent
$$\mathbf{S} = \begin{pmatrix} 4 + 0 + 1 + 9 & 4 + 0 - 1 + 6 \\ 9 & 4 + 1 + 1 + 4 \end{pmatrix} = \begin{pmatrix} 14 & 9 \\ 9 & 10 \end{pmatrix}, \qquad \hat{\boldsymbol{\Sigma}} = \frac{\mathbf{S}}{4} = \begin{pmatrix} 3{,}5 & 2{,}25 \\ 2{,}25 & 2{,}5 \end{pmatrix}.$$
$\det\hat{\boldsymbol{\Sigma}} = 8{,}75 - 5{,}0625 = 3{,}6875$, de logarithme $1{,}305$, et $\ell(\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Sigma}}) = -2\,(2\ln(2\pi) + 1{,}305 + 2) \approx -13{,}96$. L'estimation sans biais, $\frac{\mathbf{S}}{3}$, donne $\ell \approx -14{,}11$ : plus petite, comme en M13a.

**Diviser par $n$.** Comme en dimension 1 (M02c §6, M13a §1), $\hat{\boldsymbol{\Sigma}}$ est **biaisée** : $\mathbb{E}[\hat{\boldsymbol{\Sigma}}] = \frac{n - 1}{n}\boldsymbol{\Sigma}$, et l'estimation sans biais divise par $n - 1$. Les deux conventions de M12c §8 reviennent.

### Quand n ≤ d

$\mathbf{S}$ est une somme de $n$ matrices de rang 1, dont les vecteurs $\mathbf{x}_i - \bar{\mathbf{x}}$ ont une somme nulle : son rang est au plus $n - 1$. Si $n \le d$, $\hat{\boldsymbol{\Sigma}}$ est donc **singulière** : les données tiennent dans un sous-espace affine de dimension au plus $n - 1 < d$, et la vraisemblance n'a plus de maximum (en écrasant la loi sur ce sous-espace, $\ln\det \to -\infty$ et $\ell \to +\infty$). Avec les deux premiers relevés seulement, $\hat{\boldsymbol{\Sigma}} = \frac14(\mathbf{x}_1 - \mathbf{x}_2)(\mathbf{x}_1 - \mathbf{x}_2)^\top = \begin{pmatrix} 1 & 0{,}5 \\ 0{,}5 & 0{,}25 \end{pmatrix}$, de déterminant nul : toute la loi estimée est sur la droite qui passe par les deux points.

💻 **Aujourd'hui en pratique** — `X.mean(axis=0)` et `np.cov(X, rowvar=False, bias=True)` (ou `np.cov(X.T, bias=True)`) donnent $\hat{\boldsymbol{\mu}}$ et $\hat{\boldsymbol{\Sigma}}$ pour des données rangées en lignes (📦 M25a.24) ; **sans `bias=True`, `np.cov` divise par $n - 1$**, et sans `rowvar=False` il prend les lignes pour des variables. Quand $n$ est petit devant $d$, on régularise : `sklearn.covariance.LedoitWolf` rapproche l'estimation d'une matrice proportionnelle à $\mathbf{I}$.

⚠️ **Erreur classique.** Prendre la valeur par défaut de `np.cov` pour le maximum de vraisemblance, ou oublier de transposer des données rangées en lignes (on obtient une matrice $(n, n)$). Inverser $\hat{\boldsymbol{\Sigma}}$ quand $n \le d$. Lire $\nabla\ln\det\mathbf{Z} = \mathbf{Z}^{-1}$ pour une matrice non symétrique (c'est $\mathbf{Z}^{-\top}$).

## §7 · La divergence KL continue : Jensen, positivité, additivité, et la KL entre deux gaussiennes

### De la somme à l'intégrale

M06 a défini la divergence KL entre deux lois **discrètes**, en bits. Pour deux lois **à densité** $p$ et $q$ sur $\mathbb{R}^d$, la somme devient une intégrale, et l'on compte en **nats** (logarithme népérien), comme les bibliothèques :

> **Définition.** La **divergence KL** (*Kullback-Leibler divergence*) de $p$ à $q$ est
> $$\mathrm{KL}(p \,\|\, q) = \mathbb{E}_{\mathbf{x} \sim p}\big[\ln p(\mathbf{x}) - \ln q(\mathbf{x})\big] = \int p(\mathbf{x})\ln\frac{p(\mathbf{x})}{q(\mathbf{x})}\,\mathrm{d}\mathbf{x},$$
> l'intégrale portant sur les $\mathbf{x}$ où $p(\mathbf{x}) > 0$ (le **support** de $p$, *support*). Elle vaut $+\infty$ si $q$ s'annule sur une région où $p$ a une masse positive.

C'est la moyenne, sous $p$, du logarithme du rapport des densités (le théorème de transfert, M02b §4) ; la loi sous laquelle on prend l'espérance est la **première**. Pour deux lois discrètes, on retrouve la somme de M06, avec $\ln$ au lieu de $\log_2$ (1 bit vaut $\ln 2 \approx 0{,}693$ nat).

### Jensen pour une variable continue, et la positivité

> **Inégalité de Jensen** (*Jensen's inequality* ; ∂ M25a.13). Si $f$ est convexe sur un intervalle et $X$ une variable à valeurs dans cet intervalle, d'espérance finie (à densité ou non), alors $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$ ; l'inégalité change de sens pour $f$ concave. Si $f$ est strictement convexe, il y a égalité seulement si $X$ est constante (avec la probabilité 1).

M06 §6 l'avait obtenue pour une variable discrète, par récurrence ; l'idée qui marche toujours tient dans une figure : une fonction convexe reste **au-dessus de sa tangente** au point $\mathbb{E}[X]$ (M05a §1). Le ∂ M25a.13 en tire l'inégalité, puis :

> **Positivité** (∂ M25a.13). $\mathrm{KL}(p \,\|\, q) \ge 0$, avec égalité si et seulement si $p = q$ (sauf peut-être sur une région de volume nul, où une densité peut être changée sans changer la loi).

En particulier, $\mathrm{KL}(p \,\|\, p) = 0$. Comme en M06, on applique Jensen au logarithme, concave, et à la variable $\frac{q(\mathbf{x})}{p(\mathbf{x})}$, avec $\mathbf{x} \sim p$. Ce qu'on intègre, $p\ln\frac pq$, peut être **négatif** là où $q > p$ ; seule l'intégrale totale est positive (la figure ci-dessous, au milieu).

### Supports, asymétrie : deux exemples

**Deux lois sur [0, 1].** Soit $p$ la loi uniforme sur $[0, 1]$ et $q$ la loi de densité $2x$ sur $[0, 1]$ (une loi qui favorise les grandes valeurs). Avec $\int_0^1\ln x\,\mathrm{d}x = -1$ et $\int_0^1 x\ln x\,\mathrm{d}x = -\frac14$ (intégrations par parties, M02a §3) :
$$\mathrm{KL}(p \,\|\, q) = \int_0^1\ln\frac{1}{2x}\,\mathrm{d}x = 1 - \ln 2 \approx 0{,}307, \qquad \mathrm{KL}(q \,\|\, p) = \int_0^1 2x\ln(2x)\,\mathrm{d}x = \ln 2 - \frac12 \approx 0{,}193 .$$
Les deux sens sont finis, et différents : la KL n'est **pas symétrique**. Ce n'est pas une distance (M06 §5).

**Des supports différents.** Une durée est toujours positive ; supposons que sa vraie loi soit $p$, la loi exponentielle de paramètre 1 (de densité $e^{-x}$ sur $[0, +\infty[$), et qu'on la modélise par $q = \mathcal{N}(1, 1)$, qui donne aussi des valeurs négatives.
- $\mathrm{KL}(q \,\|\, p) = +\infty$ : $q$ met une masse positive (environ 16 %) sur $]-\infty, 0[$, où $p$ est nulle.
- $\mathrm{KL}(p \,\|\, q)$ est finie : $\ln p(x) - \ln q(x) = -x + \frac12\ln(2\pi) + \frac{(x - 1)^2}{2}$, et sous $p$, $\mathbb{E}[X] = 1$ et $\mathbb{E}[(X - 1)^2] = \mathbb{V}(X) = 1$ (M02b §4), donc $\mathrm{KL}(p \,\|\, q) = -1 + \frac12\ln(2\pi) + \frac12 \approx 0{,}419$.

La règle : la KL est infinie dès que le **support de la seconde loi ne couvre pas celui de la première**.

### Additivité sur des lois produits

> **Additivité** (∂ M25a.13). Si $p(\mathbf{x}, \mathbf{y}) = p_1(\mathbf{x})\,p_2(\mathbf{y})$ et $q(\mathbf{x}, \mathbf{y}) = q_1(\mathbf{x})\,q_2(\mathbf{y})$ (deux blocs indépendants sous chacune des deux lois), alors
> $$\mathrm{KL}(p \,\|\, q) = \mathrm{KL}(p_1 \,\|\, q_1) + \mathrm{KL}(p_2 \,\|\, q_2).$$

L'idée : le logarithme d'un produit est une somme, et l'espérance d'une fonction de $\mathbf{x}$ seul sous la loi produit ne dépend que de $p_1$. Pour deux coordonnées indépendantes, chacune uniforme sous $p$ et de densité $2x$ sous $q$, la KL vaut $2(1 - \ln 2) \approx 0{,}614$. Si l'indépendance ne vaut que sous l'une des deux lois, la formule ne s'applique pas.

![À gauche, les densités de p = N(6, 4) et q = N(8, 9) ; au milieu, ce qu'on intègre dans les deux sens, p ln(p/q) et q ln(q/p), négatifs par endroits, d'aires KL(p ‖ q) ≈ 0,350 et KL(q ‖ p) ≈ 0,720 nat ; à droite, la loi exponentielle de paramètre 1 et N(1, 1) : la masse de N(1, 1) sur les nombres négatifs, où l'exponentielle est nulle, rend KL(N(1, 1) ‖ exp.) infinie, alors que KL(exp. ‖ N(1, 1)) ≈ 0,419](figures/kl_deux_sens.png)

### L'entropie différentielle

> **Définition.** L'**entropie différentielle** (*differential entropy*) d'une loi de densité $p$ est $h(p) = -\mathbb{E}_p[\ln p(\mathbf{x})] = -\int p\ln p$, en nats. Alors $\mathrm{KL}(p \,\|\, q) = -h(p) - \mathbb{E}_p[\ln q(\mathbf{x})]$ : la cross-entropy de M06, en version continue, moins l'entropie.
>
> **Propriété** (∂ M25a.14). $h\big(\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})\big) = \frac12\ln\big((2\pi e)^d\det\boldsymbol{\Sigma}\big)$.

Elle ne dépend pas de $\boldsymbol{\mu}$, et croît avec $\det\boldsymbol{\Sigma}$ : plus la loi s'étale, plus elle est incertaine. Pour le GPS : $\ln(2\pi e) + \frac12\ln 144 \approx 2{,}8379 + 2{,}4849 = 5{,}3228$ nats. Contrairement à l'entropie de M06, **elle peut être négative** : pour $\mathcal{N}(0 ;\ 0{,}04)$ (un écart-type de 0,2), $h = \frac12\ln(2\pi e \times 0{,}04) \approx -0{,}1905$. Elle dépend de l'**unité** : en millimètres, $\boldsymbol{\Sigma}$ est multipliée par $10^6$ et $h$ augmente de $d\ln 1\,000$ : 13,816 nats pour le GPS, dont l'entropie passe de 5,3228 à 19,138 nats.

### La KL entre deux gaussiennes

Le calcul repose sur l'espérance d'une forme quadratique :

> **Lemme de la trace.** Si $\mathbf{x}$ a pour moyenne $\boldsymbol{\mu}$ et pour covariance $\boldsymbol{\Sigma}$ (gaussien ou non), alors pour toute matrice $\mathbf{A}$ et tout vecteur $\mathbf{m}$,
> $$\mathbb{E}\big[(\mathbf{x} - \mathbf{m})^\top\mathbf{A}(\mathbf{x} - \mathbf{m})\big] = \operatorname{tr}(\mathbf{A}\boldsymbol{\Sigma}) + (\boldsymbol{\mu} - \mathbf{m})^\top\mathbf{A}(\boldsymbol{\mu} - \mathbf{m}).$$

L'idée : écrire $\mathbf{x} - \mathbf{m} = (\mathbf{x} - \boldsymbol{\mu}) + (\boldsymbol{\mu} - \mathbf{m})$, développer (les termes croisés ont une espérance nulle), puis appliquer l'astuce de la trace au premier terme. Pour $\mathbf{m} = \boldsymbol{\mu}$ et $\mathbf{A} = \boldsymbol{\Sigma}^{-1}$, il donne $\mathbb{E}[\Delta^2] = \operatorname{tr}(\mathbf{I}) = d$ : la moyenne d'une loi du khi-deux à $d$ degrés (§3).

> **Théorème** (∂ M25a.14). Pour $\boldsymbol{\Sigma}_0$ et $\boldsymbol{\Sigma}_1$ définies positives, en dimension $d$, avec $\boldsymbol{\delta} = \boldsymbol{\mu}_1 - \boldsymbol{\mu}_0$,
> $$\mathrm{KL}\big(\mathcal{N}(\boldsymbol{\mu}_0, \boldsymbol{\Sigma}_0) \,\|\, \mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)\big) = \frac12\Big[\operatorname{tr}\big(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0\big) + \boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta} - d + \ln\frac{\det\boldsymbol{\Sigma}_1}{\det\boldsymbol{\Sigma}_0}\Big].$$
> **Même covariance** ($\boldsymbol{\Sigma}_0 = \boldsymbol{\Sigma}_1 = \boldsymbol{\Sigma}$) : il ne reste que $\frac12\,\boldsymbol{\delta}^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\delta}$, la moitié du carré de la distance de Mahalanobis entre les deux moyennes, et la KL est alors symétrique.

Le ∂ M25a.14 écrit $\ln p_0 - \ln p_1$ avec le §1 et prend son espérance sous $p_0$ par le lemme. Lecture des termes : le dernier compare les volumes des deux lois ; le terme en $\boldsymbol{\delta}$ mesure le décalage des moyennes, à l'échelle de $\boldsymbol{\Sigma}_1$ ; la trace compare les formes. Pour deux lois égales, $\operatorname{tr}(\mathbf{I}) - d = 0$, le logarithme vaut 0, et la KL est nulle, comme il se doit.

**Exemples.**
- **En dimension 1**, $p = \mathcal{N}(6, 4)$ et $q = \mathcal{N}(8, 9)$ :
$$\mathrm{KL}(p \,\|\, q) = \frac12\Big[\frac49 + \frac{(8 - 6)^2}{9} - 1 + \ln\frac94\Big] = \ln\frac32 + \frac{8}{18} - \frac12 \approx 0{,}405 + 0{,}444 - 0{,}5 \approx 0{,}350,$$
et, dans l'autre sens, $\mathrm{KL}(q \,\|\, p) = \ln\frac23 + \frac{9 + 4}{8} - \frac12 \approx 0{,}720$. Les deux sens diffèrent.
- **Même covariance** : deux récepteurs GPS de même covariance $\boldsymbol{\Sigma}$, l'un de biais $\boldsymbol{\mu}$, l'autre de biais $\boldsymbol{\mu} + (4, 2)$. La KL vaut $\frac12\Delta^2(\mathbf{x}_A) = \frac12 \times \frac{10}{9} = \frac59 \approx 0{,}556$ nat, dans les deux sens.

💻 **Aujourd'hui en pratique** — SciPy n'a pas de fonction de KL entre deux lois continues : on intègre numériquement (`scipy.integrate.quad` en dimension 1, `dblquad` en dimension 2, 📦 M25a.24), on utilise la formule fermée, ou l'on estime $\mathbb{E}_p[\ln p - \ln q]$ par une moyenne sur des tirages de $p$. `scipy.stats.norm(mu, sigma).entropy()` et `multivariate_normal(mean, cov).entropy()` donnent l'entropie différentielle, en nats. `scipy.stats.entropy(pk, qk)` est la KL de M06, pour des lois discrètes.

⚠️ **Erreur classique.** Inverser les arguments : $\mathrm{KL}(q \,\|\, p)$ n'est pas $\mathrm{KL}(p \,\|\, q)$, et l'un peut être infini quand l'autre est fini. Oublier le $-d$, ou intervertir $\boldsymbol{\Sigma}_0$ et $\boldsymbol{\Sigma}_1$ dans la trace et dans le logarithme. Croire qu'une entropie différentielle est positive. Mélanger nats et bits.

🔗 **Dans workbookIA** — le chapitre 25 se sert d'une divergence KL entre deux lois gaussiennes, de sa positivité et de son additivité sur des coordonnées indépendantes ; il dérive lui-même la forme dont il a besoin.

## §8 · L'interpolation sphérique : rester sur la sphère, à vitesse angulaire constante

### Pourquoi pas la ligne droite

Pour aller d'un vecteur $\mathbf{u}$ à un vecteur $\mathbf{v}$, la ligne droite $(1 - t)\,\mathbf{u} + t\,\mathbf{v}$, pour $t$ de 0 à 1, est la plus simple. Mais si $\mathbf{u}$ et $\mathbf{v}$ sont deux directions (deux vecteurs unitaires), elle passe à l'**intérieur** de la sphère : son milieu $\frac{\mathbf{u} + \mathbf{v}}{2}$ a pour norme $\cos\frac\Omega2$, où $\Omega$ est l'angle entre $\mathbf{u}$ et $\mathbf{v}$ (M07 §4), puisque $\big\lVert\frac{\mathbf{u} + \mathbf{v}}{2}\big\rVert^2 = \frac{2 + 2\cos\Omega}{4} = \cos^2\frac\Omega2$. Et elle ne tourne pas à vitesse constante : à $t = \frac14$, elle n'a pas parcouru le quart de l'angle. On veut un chemin qui reste sur la sphère (un arc de **grand cercle**, *great circle*, le plus court sur la sphère) et qui tourne d'un angle proportionnel à $t$. Une caméra motorisée qui pivote d'une direction à une autre en a besoin.

### Les formules de soustraction, tirées de l'exponentielle complexe

M22 §2 a admis la règle $e^{i\gamma}e^{i\psi} = e^{i(\gamma + \psi)}$, en notant qu'elle équivaut aux formules d'addition ; en voici la version qui sert ici. Avec $e^{-i\psi} = \cos\psi - i\sin\psi$ ($\cos$ est paire et $\sin$ impaire, R9), le produit $e^{i\gamma}e^{-i\psi}$ donne
$$e^{i(\gamma - \psi)} = (\cos\gamma\cos\psi + \sin\gamma\sin\psi) + i\,(\sin\gamma\cos\psi - \cos\gamma\sin\psi),$$
et l'on identifie les parties réelles et imaginaires :

> **Formules de soustraction.** Pour tous réels $\gamma$ et $\psi$,
> $$\sin(\gamma - \psi) = \sin\gamma\cos\psi - \cos\gamma\sin\psi, \qquad \cos(\gamma - \psi) = \cos\gamma\cos\psi + \sin\gamma\sin\psi .$$

MB3 s'en resservira.

### Le slerp : formule et propriétés

> **Définition.** Soit $\mathbf{u}$ et $\mathbf{v}$ deux vecteurs non nuls, ni de même direction, ni opposés, et $\Omega \in\, ]0, \pi[$ leur angle : $\cos\Omega = \frac{\mathbf{u}^\top\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}$. L'**interpolation sphérique** (*spherical linear interpolation*, **slerp**) est, pour $t \in [0, 1]$,
> $$\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; t) = \frac{\sin\big((1 - t)\,\Omega\big)}{\sin\Omega}\,\mathbf{u} + \frac{\sin(t\,\Omega)}{\sin\Omega}\,\mathbf{v}.$$
>
> **Propriétés** (∂ M25a.15).
> 1. **Extrémités** : $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; 0) = \mathbf{u}$ et $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; 1) = \mathbf{v}$.
> 2. **Norme** : si $\lVert\mathbf{u}\rVert = \lVert\mathbf{v}\rVert = R$, alors $\lVert\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; t)\rVert = R$ pour tout $t$ : le chemin reste sur la sphère de rayon $R$, dans le plan de $\mathbf{u}$ et $\mathbf{v}$ (un arc de grand cercle).
> 3. **Vitesse angulaire constante** : toujours dans ce cas, l'angle entre $\mathbf{u}$ et $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; t)$ vaut $t\,\Omega$.
> 4. **Petits angles** : quand $\Omega \to 0$, $\frac{\sin(t\Omega)}{\sin\Omega} \to t$ et $\frac{\sin((1 - t)\Omega)}{\sin\Omega} \to 1 - t$ : le slerp se rapproche de la ligne droite.

L'idée de la démonstration : dans une base orthonormée du plan de $\mathbf{u}$ et $\mathbf{v}$, construite par Gram-Schmidt à partir de $\mathbf{u}$ (M12b §3), tout se ramène au cercle unité, et la formule de $\sin(\gamma - \psi)$ fait le reste ; la limite est un calcul de limite (R7). Le ∂ M25a.15 rédige les quatre points. Les propriétés 2 et 3 supposent deux vecteurs de **même norme** : entre $2\mathbf{u}$ et $\mathbf{v}$, avec $\mathbf{u}$ et $\mathbf{v}$ unitaires et $\Omega = 60°$, le point $t = \frac12$ a pour norme $\sqrt{7/3} \approx 1{,}53$, ni 1 ni 2.

**Arc et corde.** Sur une sphère de rayon $R$, l'arc de grand cercle entre deux points d'angle au centre $\Omega$ a pour longueur $R\,\Omega$ ($\Omega$ en radians) ; la **corde** (*chord*), le segment droit qui les joint, a pour longueur $2R\sin\frac\Omega2$, et son milieu est à la distance $R\cos\frac\Omega2$ du centre. Sur la Terre, prise pour une sphère de rayon $R$, le point de latitude $\varphi$ et de longitude $\lambda$ est $R\,(\cos\varphi\cos\lambda,\ \cos\varphi\sin\lambda,\ \sin\varphi)$ (M17.14) : l'angle au centre de deux villes est l'angle de ces deux vecteurs.

**Exemple : une caméra qui pivote.** Une caméra motorisée doit passer de la direction $\mathbf{u} = \frac{1}{\sqrt2}(1, 1, 0)$ à la direction $\mathbf{v} = \frac{1}{\sqrt2}(0, 1, 1)$, à vitesse angulaire constante. $\mathbf{u}^\top\mathbf{v} = \frac12$, donc $\Omega = 60°$ et $\sin\Omega = \frac{\sqrt3}{2}$.
- À mi-parcours, les deux coefficients valent $\frac{\sin 30°}{\sin 60°} = \frac{1}{\sqrt3} \approx 0{,}577$, et $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; \frac12) = \frac{\mathbf{u} + \mathbf{v}}{\sqrt3} = \frac{1}{\sqrt6}(1, 2, 1)$, de norme 1. Le milieu de la ligne droite, $\frac{1}{2\sqrt2}(1, 2, 1)$, a pour norme $\cos 30° \approx 0{,}866$.
- Au quart du trajet, les coefficients sont $\frac{\sin 45°}{\sin 60°} \approx 0{,}816$ et $\frac{\sin 15°}{\sin 60°} \approx 0{,}299$, et la caméra vise $(0{,}5774 ;\ 0{,}7887 ;\ 0{,}2113)$, à 15° de $\mathbf{u}$. Le point $\frac{3\mathbf{u} + \mathbf{v}}{4}$ de la ligne droite, de norme $\frac{\sqrt{13}}{4} \approx 0{,}901$, n'est qu'à 13,9° de $\mathbf{u}$.
- Sur la sphère unité, l'arc de $\mathbf{u}$ à $\mathbf{v}$ mesure $\frac\pi3 \approx 1{,}047$, et la corde $2\sin 30° = 1$.

![À gauche, sur la sphère unité, les directions u et v de la caméra (Ω = 60°), les points du slerp pour t = 0, ¼, ½, ¾, 1, régulièrement espacés sur l'arc de grand cercle, et ceux de la ligne droite sur la corde ; au milieu, la norme du point selon t : 1 pour le slerp ; pour la ligne droite, cos 30° ≈ 0,866 au milieu si Ω = 60°, et cos 60° = 0,5 si Ω = 120° ; à droite, l'angle parcouru depuis u : tΩ pour le slerp, une courbe en S pour la ligne droite, lente aux deux bouts, presque confondue avec tΩ quand Ω = 60°](figures/slerp.png)

### Les cas limites

- **$\Omega = 0$** (même direction) : la formule donne $\frac00$ et n'a pas de sens. La propriété 4 dit ce qui se passe quand $\Omega$ tend vers 0 : le slerp se rapproche de la ligne droite, qui, entre deux vecteurs égaux, reste sur place.
- **$\Omega = \pi$** (vecteurs opposés) : $\sin\Omega = 0$ aussi, et il y a une infinité de grands cercles de $\mathbf{u}$ à $-\mathbf{u}$ ; aucune formule ne peut en choisir un sans information de plus.

💻 **Aujourd'hui en pratique** — `scipy.spatial.transform.Slerp` interpole entre des **rotations** de l'espace (des quaternions unitaires, sur la sphère de $\mathbb{R}^4$) : c'est l'usage d'origine du slerp, en animation.

⚠️ **Erreur classique.** Prendre $\Omega = \arccos(\mathbf{u}^\top\mathbf{v})$ sans diviser par les normes. Croire que le slerp garde la norme entre deux vecteurs de normes différentes. Normaliser après coup la ligne droite et croire qu'on obtient le slerp : on retrouve bien l'arc, mais pas la vitesse angulaire constante (la figure, à droite). Oublier les cas $\sin\Omega = 0$.

🔗 **Dans workbookIA** — le chapitre 25 interpole entre deux tirages gaussiens de grande dimension, en ligne droite ou par un slerp ; la loi de la norme (§3) éclaire la différence.

## Les pièges classiques ⚠️ (récapitulatif)

- **La densité** : une covariance en second paramètre ; $(2\pi)^{-d/2}(\det\boldsymbol{\Sigma})^{-1/2}$ ; $\ln\det\boldsymbol{\Sigma} = 2\sum_i\ln L_{ii}$ ; Mahalanobis, pas Euclide.
- **Vecteur gaussien**, pas seulement des coordonnées gaussiennes, pour les images affines, le conditionnement et « décorrélé ⇔ indépendant ».
- **Tirer** : $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$, en lignes `mean + E @ L.T` ; ni $\boldsymbol{\Sigma}\boldsymbol{\varepsilon}$, ni `E @ L`.
- **Les ellipses** : demi-axes $c\sqrt{\lambda_i}$ ; masse $1 - e^{-c^2/2}$ en dimension 2 seulement ; en grande dimension, les tirages sont sur une couronne, loin du centre.
- **Le conditionnement** : la covariance (le complément de Schur) ne dépend pas de la valeur lue ; $\boldsymbol{\Sigma}_{bb}^{-1}$, pas $\boldsymbol{\Sigma}_{bb}$ ; le bloc de l'inverse n'est pas l'inverse du bloc ; un zéro de $\boldsymbol{\Lambda}$ dit une indépendance conditionnelle.
- **Bayes gaussien** : additionner les précisions ; la prédictive contient $\sigma^2$.
- **Le maximum de vraisemblance** divise par $n$ (`np.cov` par $n - 1$ sans `bias=True`) ; il est singulier si $n \le d$.
- **La KL** dépend de l'ordre, peut être infinie, se compte en nats ; l'intégrande et l'entropie différentielle peuvent être négatifs.
- **Le slerp** : l'angle entre vecteurs normés ; la norme n'est gardée qu'entre vecteurs de même norme ; rien n'est défini pour $\sin\Omega = 0$.

## Et maintenant

**Dans ce dépôt** : M25b introduit les variables cachées et réutilise ce chapitre sans le redémontrer : la loi de $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ (pour dériver une espérance), le conditionnement (l'ACP probabiliste), le maximum de vraisemblance (l'algorithme EM), la KL et l'entropie (une borne inférieure de la vraisemblance). M27 compare des lois par d'autres distances, et MB5 enchaîne produits et sommes de gaussiennes.

**Dans workbookIA** : le chapitre 25 construit des modèles **génératifs**, qui fabriquent de nouveaux exemples à partir de tirages gaussiens. Tu y reconnaîtras la norme d'un tirage en grande dimension, des log-densités gaussiennes diagonales, la loi de $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$, une divergence KL entre gaussiennes et l'interpolation sphérique.

## Pour aller plus loin

- MML §6.5, la fin de §6.7.2 et §9.3 (les 📖 M25a.17 et M25a.18), et les exercices 6.10, 6.12 et 6.5 du livre.
- C. M. Bishop, *Pattern Recognition and Machine Learning*, Springer, 2006 : §2.3 (lois conditionnelles et marginales par le complément de Schur, modèle linéaire gaussien, maximum de vraisemblance) et §3.3 (régression linéaire bayésienne) ; MML y renvoie pour les formules du §4.
- K. P. Murphy, *Probabilistic Machine Learning: An Introduction*, MIT Press, 2022, chapitre 3 (la gaussienne multivariée et l'inférence dans les modèles linéaires gaussiens).
- T. M. Cover et J. A. Thomas, *Elements of Information Theory*, 2ᵉ éd., Wiley, 2006 : chapitre 2 (divergence KL, inégalité de Jensen) et chapitre 8 (entropie différentielle).
- J. K. Blitzstein et J. Hwang, *Introduction to Probability* (2ᵉ éd., `annexes/ressources.md`), chapitres 7 et 8 (lois jointes, loi normale multivariée, changements de variable).
- La documentation de NumPy (`numpy.linalg.cholesky`, `numpy.cov`, `Generator.multivariate_normal`) et de SciPy (`scipy.stats.multivariate_normal`, `scipy.stats.chi2`, `scipy.stats.chi`, `scipy.integrate.dblquad`, `scipy.spatial.transform.Slerp`).
- `annexes/symboles.md` (lire $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, $\mathbf{x}_a \mid \mathbf{x}_b$, $\mathbf{M}/\mathbf{M}_{bb}$, $\chi^2_d$ et $\mathrm{KL}(p \,\|\, q)$ à voix haute), `annexes/formulaire.md` et `annexes/erreurs_frequentes.md`.
