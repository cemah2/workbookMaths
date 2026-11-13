# CP5 · Ma copie de l'examen blanc

> Ta copie de ce fichier est dans `mon_travail/checkpoints/partie_5/04_mes_reponses.md` (créée par `python tools/start_chapter.py CP5`) : c'est **elle** que tu remplis, pendant l'examen, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : la moitié des points d'une question de calcul vont à la méthode. Tu peux aussi composer sur papier, puis recopier ici tes réponses finales.

**Date :** · **Début :** · **Fin :** · **Durée :**

## CP5.Q1 — Dix affirmations sur la partie V

- a) Vrai / Faux — parce que
- b) Vrai / Faux — parce que
- c) Vrai / Faux — parce que
- d) Vrai / Faux — parce que
- e) Vrai / Faux — parce que
- f) Vrai / Faux — parce que
- g) Vrai / Faux — parce que
- h) Vrai / Faux — parce que
- i) Vrai / Faux — parce que
- j) Vrai / Faux — parce que

## CP5.1 — Convolution de deux suites, corrélation croisée et matrice de Toeplitz

- a) a * b =
- b) somme alternée =
- c) w ⋆ x (mode valide) =
- d) x * w (mode plein) =
- e) np.convolve(x, w, "same") =
- f) T (6 × 3) =
- g) coefficients non nuls pour n = 40 :
- h) ligne 1 de V =
- b) la valeur de X, et b) à partir de P et Q ; e) l'indice de départ ; h) pourquoi le noyau est retourné :

## CP5.2 — Positions d'une fenêtre, pas, dilatation, et la convolution transposée d'un signal

- a) positions avec s = 4 :
- b) positions avec s = 4, p = 5, d = 3 :
- c) échantillons jamais lus :
- d) longueurs n qui donnent 25 positions :
- e) [positions, zéros au début, zéros à la fin] =
- f) convolution transposée =
- g) taille :
- h) nombres de tampons :
- c) les cases de la dernière fenêtre ; e) la vérification ; f) les quatre tampons :

## CP5.3 — Une grille filtrée par un noyau séparable : paramètres, coût et champ récepteur

- a) [a, b] =
- b) Y =
- c) [en direct, en deux passes] =
- d) valeur (0, 0) de la convolution 2D :
- e) paramètres :
- f) multiplications-additions :
- g) paramètres de la convolution séparable par canal :
- h) [champ récepteur, pas total] =
- Pourquoi K est de rang 1 ; la passe verticale ; la forme de la sortie de la situation 2 :

## CP5.4 — Équivariance, matrice circulante et le pire cas d'une perturbation bornée

- a) z =
- b) première ligne de circ(h) =
- c) (P²x) ⊛ h =
- d) δ =
- e) plus grand écart sur z₁ :
- f) plus grand écart si ‖δ‖₂ ≤ 0,2 :
- c) sans nouveau calcul, et la propriété ; le noyau de la première ligne ; pourquoi e) vaut pour toute sortie :

## CP5.5 — Une récurrence avec entrée : solution et réponse impulsionnelle

- a) x₂ =
- b) x₃ =
- c) A¹⁰x₀ =
- d) h₀, h₁, h₂, h₃ =
- e) h₁₅ =
- f) part de y₃ due aux rejets :
- g) x⋆ =
- h) facteur mensuel de la quantité totale :
- Valeurs propres, vecteurs propres et x₀ sur ces vecteurs ; formule de hₖ ; les sommes des colonnes de A :

## CP5.6 — Valeurs propres complexes, rayon spectral, normes et croissance transitoire

- a) λ =
- b) ρ(M) =
- c) argument de λ :
- d) M² =
- e) M⁴ =
- f) [‖M‖₁, ‖M‖∞] =
- g) ‖M‖₂ =
- h) comportements [M, √2 M] (1, 2 ou 3) :
- Un vecteur que M allonge ; ‖M²‖₂ et ‖M⁴‖₂ ; M est-elle normale :

## CP5.7 — Produits de jacobiennes le long d'une trajectoire, et sensibilité à un paramètre utilisé à chaque pas

- a) p₂ =
- b) ∂p₂/∂p₀ =
- c) [produit des normes, norme du produit] =
- d) les trois termes de s₃ =
- e) s₃ =
- f) changement de x₃ au premier ordre :
- x₁, x₂, x₃, les Jₜ et les bₜ ; e) pas à pas ; le changement exact :

## CP5.8 — Une démonstration au choix (sujet A ou B)

Sujet choisi :

1.
2.
3.
4.

## CP5.9 — Corriger une copie : cinq erreurs

- a) lettres des lignes fausses :
- b) corrections :
  -
  -
  -
  -
  -

## CP5.10 — Problème de synthèse : un filtre récursif et un filtre à réponse finie, du signal à la stabilité

- a) h₀, …, h₄ =
- b) y₁, …, y₅ =
- c) ρ(A) =
- d) [‖A‖₁, ‖A‖∞, ‖A‖₂] =
- e) plus petit K :
- f) plus grande valeur de |zₜ| pour K = 6 :
- g) limite de yₜ :
- h) borne supérieure des γ :
- i) comportement (1, 2 ou 3) :
- Valeurs propres de A ; pourquoi pas ‖·‖₁ ni ‖·‖∞ ; une entrée qui atteint f) ; coût par sortie des deux filtres ; h) trace, déterminant et module :

---

## Après l'examen : ma note

Remplis ce tableau avec le barème de `03_examen_corrige.md` (et la vérification du notebook).

| Question | Points | Mes points | ⏱️ réel | À revoir (remédiation du corrigé) |
|---|---|---|---|---|
| CP5.Q1 | 1,5 | | | |
| CP5.1 | 2 | | | |
| CP5.2 | 2 | | | |
| CP5.3 | 2 | | | |
| CP5.4 | 1,5 | | | |
| CP5.5 | 2 | | | |
| CP5.6 | 2 | | | |
| CP5.7 | 1,5 | | | |
| CP5.8 | 2 | | | |
| CP5.9 | 1,25 | | | |
| CP5.10 | 2,25 | | | |
| **Total** | **20** | | | |

**Ce que je refais dans une semaine** (les questions où j'ai eu moins de la moitié des points) :

**Ce que je retiens de cet examen** (deux ou trois lignes, à reporter dans `mon_travail/suivi/journal.md`) :
