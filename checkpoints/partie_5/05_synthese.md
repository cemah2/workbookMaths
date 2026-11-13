# CP5 · Synthèse de la partie V (M21 et M22)

> La synthèse se fait **avant** l'examen blanc, un autre jour si possible. Commence par l'exercice CP5.11 : construire **ta** carte mentale et **ta** fiche d'une page. Ensuite seulement, compare-les avec les versions de référence des sections 1 à 3, puis lis les sections 4 et 5 : ce que tu as oublié, c'est ce qu'il faut revoir.

**Les deux chapitres en une phrase chacun**
1. **M21 · Convolution, matrices de Toeplitz et équivariance** : la convolution de deux suites (polynômes, dés, moyennes mobiles), la corrélation croisée des bibliothèques et ses modes ; la convolution comme application linéaire, de matrice de Toeplitz ; l'équivariance, les convolutions circulaires et le pooling ; le pas, la dilatation, le padding et la convolution transposée ; les grilles à plusieurs canaux, les noyaux séparables, les paramètres et le coût ; la composition et le champ récepteur ; le pire cas d'une petite perturbation.
2. **M22 · Récurrences vectorielles, rayon spectral et normes de matrices** : les récurrences linéaires avec entrée, leur réponse impulsionnelle et la sortie comme convolution ; les valeurs propres complexes, la forme exponentielle et les rotations ; le rayon spectral et la croissance transitoire ; les normes induites ; les produits de matrices différentes ; les produits de jacobiennes le long d'une trajectoire ; la sensibilité à un paramètre utilisé à chaque pas ; un vecteur fait de plusieurs blocs.

## CP5.11 — Ta carte mentale et ta fiche d'une page 🗣️ ★ ⏱️ 60 min

**Objectif :** organiser toute la partie V dans ta tête, avant l'examen, et repérer ce qui manque.

1. **De mémoire, sans rien ouvrir (20 min).** Sur une grande feuille, écris les deux chapitres, puis, autour de chacun, les objets mathématiques, les notions et les formules qui te viennent : range-les par objets (suites et noyaux, fenêtres, grilles, états, matrices et leurs puissances, normes), pas par étapes d'un projet. Relie les notions qui se servent l'une de l'autre, entre M21 et M22 et vers les parties précédentes (« la sortie d'une récurrence avec entrée est une convolution : M22 rejoint M21 »), et écris sur chaque flèche **pourquoi**.
2. **Avec les fiches (25 min).** Ouvre les fiches de M21 et M22 (sections « L'essentiel en 10 lignes » et « Les pièges classiques ») et l'annexe `annexes/formulaire.md`. Complète ta carte d'une autre couleur : tout ce que tu ajoutes maintenant est à revoir.
3. **Ta fiche d'une page (15 min).** Sur une seule page, écris les 20 à 25 formules ou règles que tu veux avoir en tête le jour de l'examen, et les cinq pièges qui te concernent le plus (dans tes copies de M21 et M22 et dans `annexes/erreurs_frequentes.md`).
4. **Compare** avec les sections 1 à 3 ci-dessous, puis garde ta carte et ta fiche dans `mon_travail/checkpoints/partie_5/` (une photo suffit).

**Grille de relecture.** Une bonne synthèse : (1) contient les deux chapitres et chacune de leurs sections ; (2) a au moins six flèches justifiées, entre M21 et M22 et vers les parties précédentes ; (3) donne chaque formule avec ses conventions et ses conditions (convolution **ou** corrélation, et dans quel mode ; une fenêtre qui **tient** dans le signal complété ; la convention **colonne** et le pas de décalage de $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$ ; une norme **induite**, la même des deux côtés de $\lVert\mathbf{A}\mathbf{x}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{x}\rVert$ ; le dernier pas **à gauche** dans un produit) ; (4) a des pièges tirés de tes propres erreurs ; (5) tient sur une page pour la fiche.

## 1. Carte mentale

```text
SUITES ET NOYAUX
M21   convolution (a * b)ₘ = Σ aᵢ bₘ₋ᵢ : n + k − 1 valeurs ; produit de polynômes, somme de dés, moyenne mobile
      ├─ corrélation croisée (bibliothèques) = convolution valide par le noyau retourné w̃
      ├─ modes plein / valide / même taille ; pochoirs de différences finies, laplacien à 5 points
      ├─ application linéaire → matrice de Toeplitz Tᵢⱼ = wᵢ₋ⱼ, creuse ; rang et noyau (M12a) ; transposée
      ├─ équivariance : décaler puis filtrer = filtrer puis décaler (bords, pas s)
      │  └─ signaux périodiques : commuter avec P ⇔ convolution circulaire ; circ(h)ᵀ = circ(ȟ)
      └─ pooling ; pooling global invariant

FENÊTRES ET GRILLES
M21   positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 ; « même taille » avec un pas : ⌈n/s⌉
      ├─ convolution transposée : s − 1 zéros insérés, puis convolution pleine ; recouvrements
      ├─ grilles (C, H, W) : paramètres, multiplications-additions ; groupes, par canal, 1 × 1
      ├─ noyau de rang 1 = produit extérieur → deux passes 1D
      ├─ composition : noyau équivalent w₁ * w₂ ; champ récepteur, pas total
      └─ pire cas d'une forme linéaire : ε‖g‖₁ (boule L∞), ε‖g‖₂ (boule L2)

ÉTATS ET PUISSANCES
M22   xₜ₊₁ = A xₜ + B uₜ : réponse libre Aᵗx₀ + réponse forcée Σ Aᵗ⁻¹⁻ᵏ B uₖ
      ├─ réponse impulsionnelle hₖ = C Aᵏ B → yₜ₊₁ = (h * u)ₜ : une convolution de M21
      ├─ complexes r e^{iθ}, Moivre ; [[a, −b], [b, a]] = r R_θ ; 2 × 2 : module √det
      ├─ rayon spectral : Aᵗ → 0 ⇔ ρ < 1 ; ρ = 1 : borné ou non ; non normale : croissance transitoire
      └─ facteurs dans [0, 1] : (1 − ε)ᵗ ≈ e^{−tε} ; facteurs aléatoires : signe de E[ln a]

NORMES ET PRODUITS
M22   normes induites ‖·‖₁ (colonnes), ‖·‖∞ (lignes), ‖·‖₂ = s_max ; Frobenius n'est pas induite
      ├─ ‖AB‖ ≤ ‖A‖ ‖B‖ ; ρ ≤ ‖A‖ ; ‖Aᵗ‖^{1/t} → ρ (Gelfand)
      ├─ produits Aₜ⋯A₁ : la majoration par les normes peut être très large
      ├─ récurrence non linéaire : produit de jacobiennes, le dernier pas à gauche ; contraction, point fixe
      ├─ sensibilité sₜ₊₁ = Jₜ sₜ + bₜ → une somme sur le temps
      └─ blocs : ‖w‖² = Σ ‖wₖ‖² ; un seuil sur le tout garde la direction
```

**Les flèches**, chacune avec sa raison :
- **M21 → M22** : pour $\mathbf{x}_0 = \mathbf{0}$, la sortie d'une récurrence linéaire avec entrée est la convolution de l'entrée par la réponse impulsionnelle (M22 §1) : un filtre récursif calcule une convolution par un noyau en général infini, avec un état de taille fixe.
- **M21 §8 → M22 §4** : $\lVert\mathbf{A}\rVert_\infty$ est le pire cas de M21 §8 appliqué ligne par ligne : sur la boule $\lVert\mathbf{x}\rVert_\infty \le 1$, la coordonnée $i$ de $\mathbf{A}\mathbf{x}$ va jusqu'à la norme L1 de la ligne $i$, et la norme induite garde la plus grande.
- **M21 §4 → M22 §3** : le décalage circulaire $\mathbf{P}$ est une matrice de permutation, et $\mathbf{P}^n = \mathbf{I}$ : $\rho(\mathbf{P}) = 1$, et ses puissances restent bornées sans tendre vers $\mathbf{0}$.
- **M12a → M21 §3** : la convolution par un noyau fixé est une application linéaire : sa matrice, son rang et son noyau se lisent comme en M12a (et le mot « noyau » y prend son second sens).
- **M12c → M22 §2** : les puissances d'une matrice diagonalisable, $\mathbf{A}^t = \mathbf{V}\mathbf{D}^t\mathbf{V}^{-1}$, avec des valeurs propres complexes : les modules décident de la croissance, les arguments font tourner.
- **M12d → M22 §4** : $\lVert\mathbf{A}\rVert_2$ est la plus grande valeur singulière, la racine de la plus grande valeur propre de $\mathbf{A}^\top\mathbf{A}$.
- **M19 §6 → M22 §2 et §3** : les valeurs propres d'une matrice $2 \times 2$ sont les racines de $\lambda^2 - \operatorname{tr}\mathbf{A}\,\lambda + \det\mathbf{A}$ ; le critère de M19 §6 sur les racines d'une récurrence d'ordre 2, avec $p = \operatorname{tr}\mathbf{A}$ et $q = \det\mathbf{A}$, dit quand $\rho(\mathbf{A}) < 1$.
- **M17 → M22 §6** : la règle de la chaîne le long d'une trajectoire est un produit de jacobiennes, chacune évaluée en son point, le dernier pas à gauche.
- **M18 → M22 §7** : la sensibilité à un paramètre utilisé à chaque pas est une somme sur les chemins d'un graphe de calcul : le paramètre sert à chaque pas, et les contributions de toutes ses arêtes s'additionnent.
- **R5 et R6 → M22 §5** : $(1 - \varepsilon)^t \approx e^{-t\varepsilon}$ et la demi-vie $\approx \frac{\ln 2}{\varepsilon}$ viennent des suites géométriques et du logarithme.

Redessine-la de mémoire, puis compare : chaque flèche doit pouvoir se justifier par un exemple (« une population à classes d'âge avec des lâchers : sa réponse aux lâchers est une convolution de M21, et l'oubli de son départ se lit sur le rayon spectral de M22 »).

## 2. Fiche d'une page : les formules clés

| Chapitre | Formules et règles |
|---|---|
| M21 | $(\mathbf{a} * \mathbf{b})_m = \sum_i a_ib_{m-i}$, $n + k - 1$ valeurs, les coefficients du produit des polynômes ; commutative, associative, linéaire ; **corrélation** $(\mathbf{w} \star \mathbf{x})_i = \sum_u w_ux_{i+u}$ = convolution valide par $\tilde{\mathbf{w}} = (w_{k-1}, \ldots, w_0)$ ; modes : plein $n + k - 1$, valide $n - k + 1$, même taille $n$ (NumPy : à partir de l'indice $\lfloor\frac{k-1}{2}\rfloor$ de la pleine, pour $k \le n$ ; $\lfloor\frac{\min(n, k)-1}{2}\rfloor$ en général) ; pochoirs $\frac{(-1, 1)}{h}$, $\frac{(-1, 0, 1)}{2h}$, $\frac{(1, -2, 1)}{h^2}$ ; **Toeplitz** $T_{ij} = w_{i-j}$, forme $(n + k - 1, n)$, au plus $nk$ coefficients non nuls ; $(\mathbf{P}\mathbf{x})_i = x_{(i-1) \bmod n}$, $\operatorname{circ}(\mathbf{h})_{ij} = h_{(i-j) \bmod n}$, $\operatorname{circ}(\mathbf{h})^\top = \operatorname{circ}(\check{\mathbf{h}})$, $\check{\mathbf{h}} = (h_0, h_{n-1}, \ldots, h_1)$ ; **positions** $\big\lfloor\frac{n + 2p - d(k-1) - 1}{s}\big\rfloor + 1$, étendue $d(k - 1) + 1$ ; même taille avec un pas : $\lceil\frac ns\rceil$ ; **transposée** $(m - 1)s - 2p + d(k - 1) + 1 + p_{\text{out}}$ ; **paramètres** $C_{\text{out}}\big(\frac{C_{\text{in}}}{g}k_hk_w + 1\big)$, **coût** $H_{\text{out}}W_{\text{out}}C_{\text{out}}\frac{C_{\text{in}}}{g}k_hk_w$ ; rang 1 : $\mathbf{K} = \mathbf{a}\mathbf{b}^\top$, deux passes 1D, environ $k_h + k_w$ produits par valeur (loin des bords) au lieu de $k_hk_w$ ; **champ récepteur** $r = 1 + \sum_\ell d_\ell(k_\ell - 1)\,s_1\cdots s_{\ell-1}$, pas total $S = s_1\cdots s_L$ ; **pire cas** $\max_{\lVert\boldsymbol{\delta}\rVert_\infty \le \varepsilon}\mathbf{g} \cdot \boldsymbol{\delta} = \varepsilon\lVert\mathbf{g}\rVert_1$ en $\varepsilon\operatorname{signe}(\mathbf{g})$, $\max_{\lVert\boldsymbol{\delta}\rVert_2 \le \varepsilon}\mathbf{g} \cdot \boldsymbol{\delta} = \varepsilon\lVert\mathbf{g}\rVert_2$ en $\varepsilon\frac{\mathbf{g}}{\lVert\mathbf{g}\rVert_2}$ |
| M22 | $\mathbf{x}_t = \mathbf{A}^t\mathbf{x}_0 + \sum_{k=0}^{t-1}\mathbf{A}^{t-1-k}\mathbf{B}\mathbf{u}_k$ ; $h_k = \mathbf{C}\mathbf{A}^k\mathbf{B}$, $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$ pour $\mathbf{x}_0 = \mathbf{0}$ ; $z = re^{i\theta}$, $z^t = r^te^{it\theta}$ ; $\begin{pmatrix} a & -b \\ b & a \end{pmatrix} = r\,\mathbf{R}_\theta$, $r = \sqrt{a^2 + b^2}$ ; $2 \times 2$ réelle à valeurs propres complexes : module $\sqrt{\det\mathbf{A}}$ ; $\rho(\mathbf{A}) = \max_i\lvert\lambda_i\rvert$, $\mathbf{A}^t \to \mathbf{0} \iff \rho(\mathbf{A}) < 1$ ; **normale** ($\mathbf{A}^\top\mathbf{A} = \mathbf{A}\mathbf{A}^\top$) : $\lVert\mathbf{A}^t\rVert_2 = \rho(\mathbf{A})^t$ ; $\lVert\mathbf{A}\rVert_1$ = max des sommes de $\lvert a_{ij}\rvert$ d'une **colonne**, $\lVert\mathbf{A}\rVert_\infty$ d'une **ligne**, $\lVert\mathbf{A}\rVert_2 = s_{\max}$ ; $\lVert\mathbf{A}\mathbf{B}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{B}\rVert$, $\rho(\mathbf{A}) \le \lVert\mathbf{A}\rVert$, $\lVert\mathbf{A}^t\rVert^{1/t} \to \rho(\mathbf{A})$, $\lVert\mathbf{A}^\top\rVert_2 = \lVert\mathbf{A}\rVert_2$, $\lVert\operatorname{diag}(\mathbf{d})\rVert_2 = \max_i\lvert d_i\rvert$ ; $\lVert\mathbf{A}_t\cdots\mathbf{A}_1\rVert \le \lVert\mathbf{A}_t\rVert\cdots\lVert\mathbf{A}_1\rVert$ ; $(1 - \varepsilon)^t \approx e^{-t\varepsilon}$, demi-vie $\approx \frac{\ln 2}{\varepsilon}$ ; $\frac{\partial\mathbf{x}_T}{\partial\mathbf{x}_t} = \mathbf{J}_f(\mathbf{x}_{T-1})\cdots\mathbf{J}_f(\mathbf{x}_t)$ ; contraction de facteur $q$ : écart $\le q^t \times$ écart initial ; **sensibilité** $\mathbf{s}_{t+1} = \mathbf{J}_t\mathbf{s}_t + \mathbf{b}_t$, $\mathbf{J}_t = \frac{\partial f}{\partial\mathbf{x}}$, $\mathbf{b}_t = \frac{\partial f}{\partial\beta}$ en $(\mathbf{x}_t, \beta)$ ; **blocs** $\lVert\mathbf{w}\rVert^2 = \sum_k\lVert\mathbf{w}_k\rVert^2$, seuil global $\mathbf{w}\min\big(1, \frac{c}{\lVert\mathbf{w}\rVert}\big)$ |
| Rappels | **M12c** $\mathbf{A} = \mathbf{V}\mathbf{D}\mathbf{V}^{-1} \Rightarrow \mathbf{A}^t = \mathbf{V}\mathbf{D}^t\mathbf{V}^{-1}$ ; $\lambda_1 + \lambda_2 = \operatorname{tr}\mathbf{A}$, $\lambda_1\lambda_2 = \det\mathbf{A}$ ; **M12d** $s_{\max}^2$ = plus grande valeur propre de $\mathbf{A}^\top\mathbf{A}$ ; **M17** $\mathbf{J}_{g \circ f}(\mathbf{x}) = \mathbf{J}_g(f(\mathbf{x}))\,\mathbf{J}_f(\mathbf{x})$ ; **M19 §6** les racines de $r^2 - pr + q$ sont de module $< 1$ si et seulement si $\lvert q\rvert < 1$ et $\lvert p\rvert < 1 + q$ ; **R5** $\sum_{k \ge K}q^k = \frac{q^K}{1 - q}$ pour $0 \le q < 1$ |

## 3. Les pièges de la partie

Quinze erreurs fréquentes de la partie V, avec leur correction (le détail, chapitre par chapitre, est dans les fiches et dans `annexes/erreurs_frequentes.md`) :

| Piège | Faux | Juste |
|---|---|---|
| convolution ou corrélation (M21) | `np.convolve(x, w, "valid")` et une couche de convolution d'une bibliothèque calculent la même chose | la couche calcule une corrélation, sans retourner le noyau : les deux coïncident pour un noyau symétrique, et sont opposées pour un noyau antisymétrique |
| le mode même taille (M21) | toutes les bibliothèques gardent les mêmes valeurs centrales | pour un noyau de longueur paire, le « même taille » de NumPy et celui de PyTorch sont décalés d'une case |
| le retourné circulaire (M21) | $\check{\mathbf{h}} = (h_{n-1}, \ldots, h_1, h_0)$ | $\check{\mathbf{h}} = (h_0, h_{n-1}, \ldots, h_1)$ : $h_0$ reste en tête |
| compter les positions (M21) | $\big\lceil\frac{n + 2p - k}{s}\big\rceil$ | $\big\lfloor\frac{n + 2p - d(k-1) - 1}{s}\big\rfloor + 1$ : partie entière **inférieure**, $+1$, padding des deux côtés, étendue $d(k - 1) + 1$ |
| la convolution transposée (M21) | elle défait la convolution de même pas | elle a la forme de la transposée, ce n'est pas un inverse ; les cases intérieures sont couvertes par un même nombre de tampons seulement quand $s$ divise $k$ (sinon, un damier) |
| séparable (M21) | tout noyau $3 \times 3$ se calcule en deux passes 1D | seulement un noyau de rang 1, un produit extérieur $\mathbf{a}\mathbf{b}^\top$ ; « séparable par canal » est un autre sens du mot |
| le champ récepteur (M21) | chaque étage ajoute $k_\ell - 1$ | chaque étage ajoute $d_\ell(k_\ell - 1)$ fois le produit des pas des étages **précédents** |
| le pire cas (M21) | sur la boule L∞ de rayon $\varepsilon$, le pire $\boldsymbol{\delta}$ est $\varepsilon\,\mathbf{g}$ | $\varepsilon\operatorname{signe}(\mathbf{g})$, et l'écart vaut $\varepsilon\lVert\mathbf{g}\rVert_1$ : la boule L∞ va avec la norme L1 |
| la solution d'une récurrence (M22) | $\mathbf{A}^{t-k}\mathbf{B}\mathbf{u}_k$ et $y_t = (\mathbf{h} * \mathbf{u})_t$ | $\mathbf{A}^{t-1-k}\mathbf{B}\mathbf{u}_k$, et un pas de décalage : $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$ |
| le module (M22) | des valeurs propres complexes d'une matrice $2 \times 2$ ont pour module $\frac{\operatorname{tr}\mathbf{A}}{2}$ | $\sqrt{\det\mathbf{A}}$ : la partie réelle ne suffit pas |
| le long terme et les premiers pas (M22) | $\rho(\mathbf{A}) < 1$, donc $\lVert\mathbf{A}^t\mathbf{x}\rVert$ décroît à chaque pas | $\mathbf{A}^t \to \mathbf{0}$, mais une matrice non normale peut d'abord allonger beaucoup |
| $\rho = 1$ (M22) | $\rho(\mathbf{A}) = 1$, donc les puissances restent bornées | une rotation, oui ; le cisaillement $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, de puissances $\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$, non |
| colonnes ou lignes (M22) | $\lVert\mathbf{A}\rVert_1$ est la plus grande somme d'une ligne ; `np.linalg.norm(A)` est $\lVert\mathbf{A}\rVert_2$ | $\lVert\mathbf{A}\rVert_1$ : les **colonnes**, $\lVert\mathbf{A}\rVert_\infty$ : les lignes ; `np.linalg.norm(A)` sans `ord` est la norme de Frobenius, qui n'est pas induite |
| les produits (M22) | $\rho(\mathbf{A}_2\mathbf{A}_1) \le \rho(\mathbf{A}_2)\,\rho(\mathbf{A}_1)$ ; et $\frac{\partial\mathbf{x}_2}{\partial\mathbf{x}_0} = \mathbf{J}_f(\mathbf{x}_0)\,\mathbf{J}_f(\mathbf{x}_1)$ | les rayons spectraux des facteurs ne disent rien du produit (deux matrices nilpotentes peuvent avoir un produit de rayon spectral 4) ; seules les normes induites se multiplient ; les jacobiennes se rangent le dernier pas à gauche, $\mathbf{J}_f(\mathbf{x}_1)\,\mathbf{J}_f(\mathbf{x}_0)$ |
| le tout ou chaque bloc (M22) | ramener chaque bloc sous $c$ ramène le tout sous $c$ | la norme globale peut aller jusqu'à $c\sqrt{p}$ pour $p$ blocs, et la direction change ; seul le seuil appliqué au tout garde la direction |

## 4. Ce qui sert dans workbookIA

Le checkpoint V de workbookIA se fait juste après cet examen blanc. Ce qui t'y attend, et dans les chapitres 21 à 24, sans en dévoiler les exercices :
- **ch. 21 (réseaux convolutifs)** : des couches qui font glisser des noyaux appris sur des images à plusieurs canaux, des corrélations croisées (M21 §2, §6) ; leur pas, leur padding, leur dilatation, leurs groupes et la taille de leurs sorties (M21 §5, §6) ; des poolings (M21 §4) ; des convolutions transposées pour agrandir une carte (M21 §5) ; une convolution écrite comme un produit de matrices (M21 §3) ; le comptage des paramètres et des opérations (M21 §6) ; les champs récepteurs (M21 §7) ; la rétropropagation à travers une convolution, avec un poids partagé par toutes les positions (M17, M18, M21) ; la fragilité d'un modèle face à de petites perturbations bornées (M21 §8).
- **ch. 22 (réseaux récurrents)** : une même cellule qui met à jour un état à chaque élément d'une séquence (M22 §1, §6) ; la propagation de l'information et des dérivées le long de longues séquences, par des produits de jacobiennes (M22 §5, §6) et des sommes sur le temps (M22 §7) ; des gradients qui s'éteignent ou explosent, lus sur des rayons spectraux et des normes (M22 §3, §4) ; la limitation de la norme d'un gradient fait de plusieurs blocs (M22 §8).
- **ch. 23 (PyTorch en pratique, 1)** : la mise en place de PyTorch, du dataset au modèle sauvegardé ; il ne demande pas d'outil nouveau de la partie V, mais des tenseurs d'images rangés $(N, C, H, W)$ : les grilles $(C, H, W)$ de M21 §6, avec un axe de plus pour le batch (M20).
- **ch. 24 (PyTorch en pratique, 2)** : des réseaux convolutifs en PyTorch, avec le padding « même taille » et un pas, et le coût d'une convolution (M21 §5, §6) ; des réseaux récurrents dont l'état est porté d'un batch à l'autre (M22 §1) ; une contrainte de norme sur les poids, $\mathbf{w}\min\big(1, \frac{c}{\lVert\mathbf{w}\rVert}\big)$, la projection sur une boule de M19 §8, la même formule que le seuil global de M22 §8.

Le mini-projet V de workbookIA assemble ces outils dans un classifieur d'images. Ensuite, la partie VI de ce dépôt commence par M25a (la gaussienne multivariée), avant workbookIA 25.

## 5. Vocabulaire à maîtriser à l'oral

Dis chaque mot à voix haute, en français puis en anglais, puis la phrase de la dernière colonne, et invente ton propre exemple.

| Français | Anglais | À dire à voix haute |
|---|---|---|
| convolution, corrélation croisée | convolution, cross-correlation | « La convolution retourne le noyau, la corrélation des bibliothèques non : je dis toujours laquelle je calcule. » |
| mode plein, valide, même taille | full, valid, same mode | « Plein : n + k − 1 valeurs ; valide : n − k + 1 ; même taille : n. » |
| matrice de Toeplitz, matrice creuse | Toeplitz matrix, sparse matrix | « Une convolution est une application linéaire dont la matrice est constante sur chaque diagonale, et presque vide. » |
| équivariance, invariance | equivariance, invariance | « Équivariant : la sortie se déplace avec l'entrée ; invariant : elle ne bouge pas. » |
| convolution circulaire, matrice circulante | circular convolution, circulant matrix | « Sur des signaux périodiques, commuter avec le décalage, c'est être une convolution circulaire. » |
| pas, padding, dilatation | stride, padding, dilation | « La fenêtre i lit les cases si, si + d, …, si + d(k − 1) du signal complété par p zéros de chaque côté : s espace les positions, d les cases lues. » |
| convolution transposée | transposed convolution | « C'est l'application de matrice Cᵀ, où C est la matrice de la somme glissante de mêmes réglages : chaque entrée imprime une copie du noyau, s cases après la précédente ; elle a la taille d'un agrandissement, pas l'effet d'un inverse. » |
| noyau séparable, convolution par canal | separable kernel, depthwise convolution | « Un noyau de rang 1 se calcule en deux passes 1D ; une convolution par canal suivie d'une 1 × 1 demande bien moins de paramètres. » |
| champ récepteur | receptive field | « Chaque étage élargit le champ de k − 1 fois le produit des pas qui le précèdent, et d fois plus s'il est dilaté. » |
| réponse impulsionnelle | impulse response | « La sortie d'un système linéaire parti de zéro est la convolution de l'entrée par sa réponse impulsionnelle. » |
| rayon spectral | spectral radius | « Le plus grand module des valeurs propres : il décide du long terme, pas des premiers pas. » |
| forme exponentielle, rotation et homothétie | exponential form, rotation and scaling | « Multiplier par r e^{iθ}, c'est tourner de θ et multiplier les longueurs par r. » |
| matrice non normale, croissance transitoire | non-normal matrix, transient growth | « Une matrice non normale peut allonger longtemps les vecteurs avant que le rayon spectral reprenne la main. » |
| norme induite, sous-multiplicativité | induced (operator) norm, submultiplicativity | « La norme induite est le plus grand facteur d'allongement ; celle d'un produit est au plus le produit des normes. » |
| sensibilité, somme sur le temps | sensitivity, sum over time | « Un paramètre utilisé à chaque pas agit à chaque pas, et chaque effet est porté jusqu'à la fin par les pas suivants. » |
| contraction, point fixe | contraction, fixed point | « Une application contractante oublie son point de départ : deux trajectoires se rapprochent à chaque pas. » |
| norme globale, seuil | global norm, clipping threshold | « Ramener le tout sous un seuil garde la direction ; ramener chaque bloc, non. » |

## Mode d'emploi (≈ 75 minutes)

1. CP5.11 d'abord (60 min) : ta carte et ta fiche, de mémoire puis avec les fiches.
2. Compare avec les sections 1 à 3 (10 min) : note ce qui te manquait.
3. Lis les sections 4 et 5 (5 min), en disant le vocabulaire à voix haute.
4. L'examen blanc, un autre jour : `01_examen_sujet.md`, en conditions réelles.

Ces 15 minutes de comparaison et de lecture sont la « lecture » du bilan ; avec CP5.11, la synthèse prend environ 75 minutes.
