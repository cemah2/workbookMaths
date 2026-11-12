# CP4 · Synthèse de la partie IV (M16 à M20)

> La synthèse se fait **avant** l'examen blanc, un autre jour si possible. Commence par l'exercice CP4.11 : construire **ta** carte mentale et **ta** fiche d'une page. Ensuite seulement, compare-les avec les versions de référence des sections 1 à 3, puis lis les sections 4 et 5 : ce que tu as oublié, c'est ce qu'il faut revoir.

**Les cinq chapitres en une phrase chacun**
1. **M16 · Couches affines, graphes et variance d'un produit** : les applications affines dans les deux conventions et leurs formes, leur composition en coordonnées homogènes ; les graphes orientés lus sur leur matrice d'adjacence (chemins, absence de cycle, somme sur les chemins) ; l'espérance et la variance d'un produit de variables indépendantes, et des variances qui se multiplient d'étage en étage.
2. **M17 · La jacobienne** : la dérivée d'une application de $\mathbb{R}^n$ dans $\mathbb{R}^m$ (une ligne par sortie), diagonale pour une fonction appliquée coordonnée par coordonnée ; la règle de la chaîne comme produit de jacobiennes ; les deux conventions de gradient ; les produits jacobienne-vecteur et vecteur-jacobienne ; les longues compositions et la loi de Boltzmann.
3. **M18 · Graphes de calcul et différentiation automatique** : la règle de la chaîne comme somme sur les chemins d'un graphe, le mode direct par les nombres duaux, le mode inverse par les adjoints et ce que coûte chaque mode ; les gradients par rapport à une matrice, la différentielle $\operatorname{tr}(\mathbf{G}^\top d\mathbf{X})$ et les identités des traces et du $\ln\det$.
4. **M19 · Hessienne, conditionnement et convergence** : la hessienne, Taylor d'ordre 2 et la nature des points critiques ; les itérations linéaires, Richardson et son pas critique, le conditionnement et le préconditionnement diagonal ; les récurrences d'ordre 2 et le module de leurs racines ; un gradient estimé sur un échantillon ; projeter sur une boule ou un pavé.
5. **M20 · Tenseurs, axes et estimateurs pondérés** : les tableaux à $k$ dimensions, leurs axes, le remodelage, les réductions et la diffusion ; `einsum` ; la matrice de centrage et la standardisation ; l'estimateur de Horvitz-Thompson ; les applications proches de l'identité et leurs produits de jacobiennes.

## CP4.11 — Ta carte mentale et ta fiche d'une page 🗣️ ★ ⏱️ 60 min

**Objectif :** organiser toute la partie IV dans ta tête, avant l'examen, et repérer ce qui manque.

1. **De mémoire, sans rien ouvrir (20 min).** Sur une grande feuille, écris les cinq chapitres, puis, autour de chacun, les objets mathématiques, les notions et les formules qui te viennent : range-les par objets (applications, graphes, dérivées, itérations, tableaux), pas par étapes d'un projet. Relie les notions qui se servent l'une de l'autre (« le mode inverse parcourt un graphe sans cycle dans l'ordre inverse d'une numérotation : M16 rejoint M18 »), et écris sur chaque flèche **pourquoi**.
2. **Avec les fiches (25 min).** Ouvre les fiches des chapitres (sections « L'essentiel en 10 lignes ») et l'annexe `annexes/formulaire.md`. Complète ta carte d'une autre couleur : tout ce que tu ajoutes maintenant est à revoir.
3. **Ta fiche d'une page (15 min).** Sur une seule page, écris les 20 à 25 formules ou règles que tu veux avoir en tête le jour de l'examen, et les cinq pièges qui te concernent le plus (dans tes copies et dans `annexes/erreurs_frequentes.md`).
4. **Compare** avec les sections 1 à 3 ci-dessous, puis garde ta carte et ta fiche dans `mon_travail/checkpoints/partie_4/` (une photo suffit).

**Grille de relecture.** Une bonne synthèse : (1) contient les cinq chapitres ; (2) a au moins six flèches justifiées entre chapitres ; (3) donne chaque formule avec ses conditions et ses formes (des variables **indépendantes** pour la variance d'un produit, un graphe **sans cycle** pour la somme sur les chemins, une matrice **symétrique** pour le critère des valeurs propres, $\mathbf{A}$ symétrique définie positive pour Richardson, des tirages **indépendants** pour la variance de Horvitz-Thompson) ; (4) a des pièges tirés de tes propres erreurs ; (5) tient sur une page pour la fiche.

## 1. Carte mentale

```text
OBJETS ET FORMES
M16   applications affines  x ↦ xW + b (lignes) ou Wx + b (colonnes) : formes, nm + m paramètres
      ├─ coordonnées homogènes [x, 1]H : composer = multiplier H₁H₂, inverser = H⁻¹
      ├─ graphes orientés → matrice d'adjacence : (Aᵏ)ᵢⱼ = chemins de longueur k
      │  └─ sans cycle ⇔ nilpotente ⇔ numérotation triangulaire → (I − A)⁻¹ = somme sur les chemins
      └─ produits de variables indépendantes : E[XY], Var(XY) ≠ Var X · Var Y
         └─ sommes décorrélées ; un facteur par étage → gᴸ
M20   tableaux à k axes : forme, ordre C, remodeler ≠ transposer
      ├─ réductions, keepdims, diffusion ; moyennes et variances le long d'axes (ddof)
      ├─ einsum : un indice absent du résultat est sommé ; coût = produit des longueurs
      ├─ centrage C = I − 11ᵀ/m : projection → m − 1 ; standardisation invariante
      └─ Horvitz-Thompson : diviser par πᵢ → sans biais ; variance Σ yᵢ²(1 − πᵢ)/πᵢ

DÉRIVER
M17   jacobienne (m, n) → approximation linéaire f(x + h) ≈ f(x) + Jh
      ├─ coordonnée par coordonnée : diagonale ; Jv = g′(x) ⊙ v
      ├─ règle de la chaîne J_{g∘f} = J_g(f(x)) J_f(x) ; gradient en ligne ou de la forme de x
      ├─ Jv (direct), uᵀJ (inverse) : sans former J
      └─ longues compositions : un produit de dérivées ; Boltzmann ; covariance d'un one-hot diag(p) − pᵀp (p en ligne)
M18   graphe de calcul → règle de la chaîne = somme sur les chemins
      ├─ mode direct : nombres duaux, ε² = 0 ; une colonne de J par passage
      ├─ mode inverse : adjoints, ordre inverse, accumulation ; une ligne de J par passage
      └─ gradient par rapport à une matrice : df = tr(Gᵀ dX), identités, ln det

COURBER ET CONVERGER
M19   hessienne (symétrique) → Taylor d'ordre 2 → nature d'un point critique (signes des λ)
      ├─ itération x ← Mx + c : eₖ₊₁ = M eₖ, converge ⇔ |λᵢ| < 1 (M symétrique)
      │  └─ Richardson : M = I − ωA, 0 < ω < 2/λmax ; κ fixe la vitesse ; préconditionnement
      ├─ récurrence d'ordre 2 : racines de r² − pr + q, module < 1
      └─ gradient sur un échantillon (sans biais, variance en 1/B) ; projection boule / pavé
M20   x ↦ x + hF(x) : jacobienne I + hJ_F, produits de L facteurs, (1 + λT/L)ᴸ → e^{λT}
```

**Les flèches entre chapitres**, chacune avec sa raison :
- **M16 → M18** : un graphe de calcul est un graphe orienté sans cycle ; la somme sur les chemins de M16 §4 est la règle de la chaîne de M18 §2, avec les dérivées locales pour poids.
- **M17 → M18** : le produit de jacobiennes d'une chaîne devient, sur un graphe, une somme sur les chemins ; $\mathbf{J}\mathbf{v}$ est le mode direct, $\mathbf{u}^\top\mathbf{J}$ le mode inverse.
- **M16 → M17** : une application affine $\mathbf{x} \mapsto \mathbf{x}\mathbf{W} + \mathbf{b}$ a pour jacobienne $\mathbf{W}^\top$, partout ; composer des affines, c'est multiplier leurs jacobiennes comme leurs matrices homogènes.
- **M18 → M19** : la hessienne est la jacobienne du gradient ; le gradient de $\frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$ est $\mathbf{A}\mathbf{x} - \mathbf{b}$, et un pas de descente est un pas de Richardson.
- **M19 → M20** : un produit de jacobiennes $\mathbf{I} + h\mathbf{J}$ se lit sur leurs valeurs singulières, comme une itération linéaire sur ses valeurs propres ; $(1 + h\lambda)^L$ est une suite géométrique.
- **M16 → M20** : la variance d'un produit et d'une somme de variables indépendantes donne la variance de Horvitz-Thompson, une somme de termes $\frac{I_i}{\pi_i}y_i$ indépendants.
- **M17 → M19** : Taylor d'ordre 2 prolonge l'approximation linéaire ; le terme d'ordre 1 est le gradient (une jacobienne à une ligne), celui d'ordre 2 la hessienne.
- **M19 → M18** : $\ln\det$ et les traces de M18 se vérifient par différences centrées, dont l'erreur se lit sur Taylor.

Redessine-la de mémoire, puis compare : chaque flèche doit pouvoir se justifier par un exemple (« ajuster $e^{a + bx}$ : le gradient par le mode inverse, puis la hessienne au minimum, puis le pas critique $2/\lambda_{\max}$ : M18 rejoint M19 »).

## 2. Fiche d'une page : les formules clés

| Chapitre | Formules et règles |
|---|---|
| M16 | $\mathbf{x}\mathbf{W} + \mathbf{b}$ : $\mathbf{x}$ $(n,)$, $\mathbf{W}$ $(n, m)$, $\mathbf{b}$ $(m,)$, $nm + m$ paramètres ; en colonnes, la matrice est $\mathbf{W}^\top$ ; **homogènes** $\mathbf{H} = \begin{pmatrix} \mathbf{W} & \mathbf{0} \\ \mathbf{b} & 1 \end{pmatrix}$, « $f_1$ puis $f_2$ » $= \mathbf{H}_1\mathbf{H}_2$ ; $(\mathbf{A}^k)_{ij}$ = nombre de chemins de longueur $k$ ; **sans cycle** $\iff \mathbf{A}^n = \mathbf{0} \iff$ numérotation strictement triangulaire ; $(\mathbf{I} - \mathbf{A})^{-1} = \sum_{k < n}\mathbf{A}^k$ ; **indépendantes** : $\mathbb{E}[XY] = \mu_X\mu_Y$, $\mathbb{V}(XY) = \sigma_X^2\sigma_Y^2 + \sigma_X^2\mu_Y^2 + \sigma_Y^2\mu_X^2$ ; **décorrélées** : $\mathbb{V}\big(\sum_i X_i\big) = \sum_i \mathbb{V}(X_i)$ ; un facteur de moment d'ordre 2 $\gamma$ par étage : $\gamma^L$ |
| M17 | $\mathbf{J}$ de forme $(m, n)$, $J_{ij} = \frac{\partial f_i}{\partial x_j}$ ; $\mathbf{f}(\mathbf{x} + \mathbf{h}) \approx \mathbf{f}(\mathbf{x}) + \mathbf{J}\mathbf{h}$ ; coordonnée par coordonnée : $\operatorname{diag}(g'(x_i))$ ; **chaîne** $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ ; gradient de la forme de la variable : $\nabla_{\mathbf{x}}(L \circ \mathbf{f}) = \mathbf{J}_{\mathbf{f}}^\top\nabla L$ ; $\mathbf{J}\mathbf{v}$ et $\mathbf{u}^\top\mathbf{J}$ sans former $\mathbf{J}$ ; composée de $L$ fonctions d'une variable : produit de $L$ dérivées ; Boltzmann $p_i \propto e^{-E_i/T}$, covariance d'un one-hot $\operatorname{diag}(\mathbf{p}) - \mathbf{p}^\top\mathbf{p}$ ($\mathbf{p}$ en ligne, comme en M17) |
| M18 | **chemins** : $\frac{\partial y}{\partial x} = \sum_{\text{chemins}}\prod$ dérivées locales ; **direct** $\dot{w} = \sum_{u \to w}\frac{\partial w}{\partial u}\dot{u}$, $f(a + \varepsilon) = f(a) + f'(a)\,\varepsilon$ ; **inverse** $\bar{u} = \sum_{u \to w}\bar{w}\frac{\partial w}{\partial u}$, $\bar{y} = 1$ ; coûts : $n$ passages directs, $m$ inverses ; $df = \operatorname{tr}(\mathbf{G}^\top d\mathbf{X})$ ; $\nabla\mathbf{a}^\top\mathbf{X}\mathbf{b} = \mathbf{a}\mathbf{b}^\top$, $\nabla\operatorname{tr}(\mathbf{A}\mathbf{X}) = \mathbf{A}^\top$, $\nabla\operatorname{tr}(\mathbf{X}^\top\mathbf{A}\mathbf{X}) = (\mathbf{A} + \mathbf{A}^\top)\mathbf{X}$, $\nabla\lVert \mathbf{X} \rVert_F^2 = 2\mathbf{X}$, $\nabla\ln\det\mathbf{X} = \mathbf{X}^{-\top}$, $\nabla\det\mathbf{X} = \det(\mathbf{X})\,\mathbf{X}^{-\top}$ ; $d(\mathbf{X}^2) = d\mathbf{X}\,\mathbf{X} + \mathbf{X}\,d\mathbf{X}$ |
| M19 | $f(\mathbf{x} + \mathbf{h}) \approx f(\mathbf{x}) + \nabla f \cdot \mathbf{h} + \frac12\mathbf{h}^\top\mathbf{H}\mathbf{h}$ ; point critique : tous $\lambda > 0$ minimum, tous $< 0$ maximum, deux signes selle, une valeur propre nulle et les autres de même signe : on ne conclut pas ; $\mathbf{e}_{k+1} = \mathbf{M}\mathbf{e}_k$, $\mathbf{M}$ symétrique : converge $\iff$ tous $\lvert \lambda_i \rvert < 1$ ; **Richardson** $\mathbf{x} \leftarrow \mathbf{x} + \omega(\mathbf{b} - \mathbf{A}\mathbf{x})$, $0 < \omega < \frac{2}{\lambda_{\max}}$ ; pas optimal $\frac{2}{\lambda_{\min} + \lambda_{\max}}$, facteur $\frac{\kappa - 1}{\kappa + 1}$, $\kappa = \frac{\lambda_{\max}}{\lambda_{\min}}$ ; Jacobi $\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$ ; $u_{k+2} = p\,u_{k+1} - q\,u_k$ : $r^2 - pr + q$, converge $\iff \lvert q \rvert < 1$ et $\lvert p \rvert < 1 + q$, module $\sqrt{q}$ si complexes ; gradient sur $B$ termes : variance $\frac{\sigma^2}{B}$ ; boule : $\mathbf{x}\min(1, r/\lVert \mathbf{x} \rVert)$ |
| M20 | forme $(n_0, \ldots, n_{k-1})$, ordre C : position $(i_0n_1 + i_1)\,n_2 + i_2$ ; réduire fait disparaître l'axe (`keepdims` : longueur 1) ; diffusion : formes alignées à droite, égales ou 1 ; variance : divise par $N - \text{ddof}$ ; `einsum("ij,jk->ik")` = produit matriciel, coût = produit des longueurs de toutes les lettres ; $\mathbf{C} = \mathbf{I} - \frac1m\mathbf{1}\mathbf{1}^\top$ projection, $\mathbb{E}\big[\sum_i (x_i - \bar x)^2\big] = (m - 1)\sigma^2$ ; $z(a\mathbf{x} + b\mathbf{1}) = z(\mathbf{x})$ pour $a > 0$ ; **Horvitz-Thompson** $\hat Y = \sum_{i \in S}\frac{y_i}{\pi_i}$, $\mathbb{E}[\hat Y] = Y$, $\mathbb{V}(\hat Y) = \sum_i y_i^2\frac{1 - \pi_i}{\pi_i}$ (tirage de Poisson) ; $\mathbf{x} + hF(\mathbf{x})$ : jacobienne $\mathbf{I} + h\mathbf{J}_F$ ; pour $hK \le \frac12$, le produit de $L$ facteurs a ses valeurs singulières entre $e^{-2KT}$ et $e^{KT}$ ($T = hL$) |

## 3. Les pièges de la partie

Dix erreurs fréquentes de la partie IV, avec leur correction (le détail, chapitre par chapitre, est dans `annexes/erreurs_frequentes.md`) :

| Piège | Faux | Juste |
|---|---|---|
| ordre des matrices homogènes (M16) | points en lignes, « $f$ puis $g$ » $= \mathbf{H}_g\mathbf{H}_f$ | en lignes, $\mathbf{H}_f\mathbf{H}_g$ : la première appliquée à **gauche** ; en colonnes, l'inverse |
| variance d'un produit (M16) | $\mathbb{V}(XY) = \mathbb{V}(X)\,\mathbb{V}(Y)$ | $+\mathbb{V}(X)\,\mu_Y^2 + \mathbb{V}(Y)\,\mu_X^2$ ; égalité si et seulement si $\mu_Y\sigma_X = 0$ et $\mu_X\sigma_Y = 0$ (deux moyennes nulles, deux constantes, ou l'une est la constante 0) |
| forme d'une jacobienne (M17) | une colonne par sortie | une **ligne** par sortie : $\mathbf{f} : \mathbb{R}^n \to \mathbb{R}^m$ donne $(m, n)$ |
| point d'évaluation (M17) | $\mathbf{J}_{\mathbf{g}}$ évaluée en $\mathbf{x}$ | en $\mathbf{f}(\mathbf{x})$, le point **intermédiaire** |
| nœud qui sert deux fois (M18) | un seul chemin, une seule contribution à l'adjoint | **toutes** les arêtes sortantes : les contributions s'additionnent |
| gradient d'une trace (M18) | $\nabla\operatorname{tr}(\mathbf{A}\mathbf{X}) = \mathbf{A}$, $\nabla\ln\det\mathbf{X} = \mathbf{X}^{-1}$ | $\mathbf{A}^\top$ et $\mathbf{X}^{-\top}$ : vérifier un coefficient hors diagonale |
| valeur propre nulle (M19) | hessienne de valeurs propres positives ou nulles en un point critique : minimum | le test ne conclut pas : $x^2 + y^3$ n'a pas de minimum en 0, $x^2 + y^4$ en a un |
| pas de Richardson (M19) | $0 < \omega < \frac{2}{\lambda_{\min}}$ | $\frac{2}{\lambda_{\max}}$ : la direction la plus courbée décide |
| module d'une racine (M19) | le module de $0{,}3 \pm 0{,}4\,i$ est $0{,}3$ (ou $0{,}7$) | $\sqrt{0{,}09 + 0{,}16} = 0{,}5$ |
| `keepdims` et `einsum` (M20) | `einsum("ij->j")` est la moyenne de chaque colonne | c'est la **somme** sur $i$ ; et `keepdims=True` garde l'axe réduit, de longueur 1 |

## 4. Ce qui sert dans workbookIA

Le checkpoint IV de workbookIA se fait juste après cet examen blanc. Ce qui t'y attend, et dans les chapitres 16 à 20, sans en dévoiler les exercices :
- **ch. 16 (réseaux feed-forward)** : des couches rangées comme les applications affines de M16 §1, en $(n_{\text{in}}, n_{\text{out}})$ ; un réseau décrit comme un graphe orienté sans cycle, parcouru dans un ordre topologique (M16 §3, §4) ; le comptage des paramètres ; l'échelle des poids tirés au hasard, fixée par un raisonnement sur des variances (M16 §5 à §7).
- **ch. 17 (activations)** : des fonctions appliquées coordonnée par coordonnée, leurs dérivées et leurs saturations (M17 §2, §6) ; une fonction de $\mathbb{R}^K$ dans $\mathbb{R}^K$ dont il calcule la jacobienne pleine (M17 §1 à §5) ; des températures (M17 §7).
- **ch. 18 (rétropropagation)** : le mode inverse (M18 §4), appliqué au graphe d'un réseau, avec ses propres noms pour les adjoints ; les gradients d'une couche sous forme matricielle, de la forme de la variable (M18 §6, §7) ; la vérification par différences finies (M18 §8) ; un petit moteur de différentiation.
- **ch. 19 (optimiseurs)** : le réglage du pas des méthodes de descente et leur comparaison sur des fonctions mal conditionnées (M19 §4, §5) ; des méthodes qui ajoutent une mémoire du pas précédent ou une échelle par coordonnée ; le gradient sur des mini-batches (M19 §7) ; la limitation des pas trop longs (M19 §8).
- **ch. 20 (régularisation et réseaux profonds)** : des tenseurs dont la forme se suit couche après couche (M20 §1, §2) ; des valeurs standardisées le long d'axes choisis (M20 §4) ; une couche qui divise par une probabilité (M20 §5) ; des applications proches de l'identité enchaînées (M20 §6).

Le mini-projet IV de workbookIA assemble ces outils dans un petit framework. Ensuite, la partie V de ce dépôt commence par M21 (la convolution), avant workbookIA 21.

## 5. Vocabulaire à maîtriser à l'oral

Dis chaque mot à voix haute, en français puis en anglais, puis la phrase de la dernière colonne, et invente ton propre exemple.

| Français | Anglais | À dire à voix haute |
|---|---|---|
| application affine, coordonnées homogènes | affine map, homogeneous coordinates | « Avec un 1 en plus, une application affine devient linéaire : composer, c'est multiplier les matrices homogènes. » |
| matrice d'adjacence, graphe sans cycle, nilpotente | adjacency matrix, directed acyclic graph, nilpotent matrix | « Les puissances de la matrice comptent les chemins ; sans cycle, elles finissent par s'annuler. » |
| indépendantes, décorrélées | independent, uncorrelated | « Décorrélées suffit pour la variance d'une somme ; pour celle d'un produit, il faut l'indépendance. » |
| jacobienne, règle de la chaîne | Jacobian, chain rule | « Une ligne par sortie ; la jacobienne d'une composée est le produit, la dernière fonction à gauche. » |
| produit jacobienne-vecteur, vecteur-jacobienne | Jacobian-vector product, vector-Jacobian product | « Jv pousse une direction vers la sortie ; uᵀJ ramène une pondération des sorties vers l'entrée. » |
| graphe de calcul, adjoint | computation graph, adjoint | « L'adjoint d'un nœud est la dérivée de la sortie par rapport à lui ; il additionne les contributions de ses successeurs. » |
| mode direct, mode inverse, nombre dual | forward mode, reverse mode, dual number | « Le direct donne une colonne par passage, l'inverse une ligne : pour un gradient, l'inverse gagne. » |
| différentielle, gradient matriciel | differential, matrix gradient | « Écris df comme la trace de Gᵀ dX, et lis G : il a la forme de X. » |
| hessienne, point selle | Hessian, saddle point | « Des valeurs propres des deux signes : la fonction monte dans une direction et descend dans une autre. » |
| pas critique, conditionnement | critical step size, condition number | « Le pas se règle sur la plus grande courbure, la vitesse sur le rapport des courbures. » |
| polynôme caractéristique, module | characteristic polynomial, modulus | « Une récurrence d'ordre 2 tend vers 0 quand ses deux racines sont de module plus petit que 1. » |
| axe, réduction, diffusion | axis, reduction, broadcasting | « Réduire fait disparaître l'axe ; keepdims le garde, de longueur 1, pour diffuser contre le tableau. » |
| probabilité d'inclusion, estimateur de Horvitz-Thompson | inclusion probability, Horvitz-Thompson estimator | « Diviser chaque observation par sa probabilité d'être tirée rend l'estimation du total sans biais. » |

## Mode d'emploi (≈ 75 minutes)

1. CP4.11 d'abord (60 min) : ta carte et ta fiche, de mémoire puis avec les fiches.
2. Compare avec les sections 1 à 3 (10 min) : note ce qui te manquait.
3. Lis les sections 4 et 5 (5 min), en disant le vocabulaire à voix haute.
4. L'examen blanc, un autre jour : `01_examen_sujet.md`, en conditions réelles.

Ces 15 minutes de comparaison et de lecture sont la « lecture » du bilan ; avec CP4.11, la synthèse prend environ 75 minutes.
