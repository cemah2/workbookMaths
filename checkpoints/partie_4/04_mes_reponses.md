# CP4 · Ma copie de l'examen blanc

> Ta copie de ce fichier est dans `mon_travail/checkpoints/partie_4/04_mes_reponses.md` (créée par `python tools/start_chapter.py CP4`) : c'est **elle** que tu remplis, pendant l'examen, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : la moitié des points d'une question de calcul vont à la méthode. Tu peux aussi composer sur papier, puis recopier ici tes réponses finales.

**Date :** · **Début :** · **Fin :** · **Durée :**

## CP4.Q1 — Dix affirmations sur la partie IV

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

## CP4.1 — Coordonnées homogènes, chemins d'un graphe et variance d'un produit

- a) matrice homogène de g ∘ f =
- b) (g ∘ f)(P) =
- c) dernière ligne de la matrice homogène de (g ∘ f)⁻¹ =
- d) chemins de longueur 2 de 5 à 1 =
- e) plus petit k tel que Aᵏ = 0 :
- f) somme des poids des chemins de 5 à 1 =
- g) E[V] =
- h) Var(V) =
- Vérification de c) ; la matrice qui donne f) ; h) comparé à Var D · Var T :

## CP4.2 — Jacobienne d'une composée et produit vecteur-jacobienne

- a) f(p) =
- b) J_f(p) =
- c) J_g(f(p)) =
- d) J_{g∘f}(p) =
- e) uᵀ J_{g∘f}(p) =
- f) multiplications, (uᵀJ_g)J_f puis uᵀ(J_gJ_f) =
- g) approximation linéaire de (g ∘ f)(2,1 ; −2,05) =
- h) jacobienne de φ ∘ f en p =
- Un coefficient de d) comme somme sur les variables intermédiaires ; e) est le gradient de quelle fonction ; l'ordre de l'écart en g) :

## CP4.3 — Mode direct et mode inverse sur un graphe de calcul

- a) f(5, −2) =
- b) chemins de x à f =
- c) [v̇₁, v̇₂, v̇₃] =
- d) ∂f/∂x =
- e) [v̄₃, v̄₂] =
- f) v̄₁ =
- g) ∂f/∂y =
- h) passages [mode direct, mode inverse] =
- Le graphe et ses dérivées locales ; ln(9 + ε) :

## CP4.4 — Gradients par rapport à une matrice

- a) gradient de aᵀXb =
- b) gradient de tr(AX) =
- c) gradient de tr(XᵀBX) =
- d) gradient de ln det X =
- e) variation de ln det au premier ordre =
- f) gradient de F =
- g) gradient de aᵀXᵀXb =
- c) pourquoi B + Bᵀ ; e) la valeur exacte ; g) la différentielle :

## CP4.5 — Hessienne, Taylor d'ordre 2 et nature d'un point critique

- a) ∇f(P) =
- b) H_f(P) =
- c) T₂(P + h) =
- d) f(P + h) − T₂(P + h) =
- e) points critiques =
- f) valeurs propres au point d'abscisse positive =
- g) nature de ce point (1, 2, 3 ou 4) :
- h) nature de l'autre point (1, 2, 3 ou 4) :
- Pourquoi d) vaut h₁³ ; valeurs propres et direction de descente pour h) :

## CP4.6 — Itération de Richardson et récurrence d'ordre 2

- a) x₁ =
- b) x₂ =
- c) pas critique =
- d) facteur pour ω = 0,1 =
- e) nombre de pas au pas optimal =
- f) racines de (R₁) =
- g) module des racines de (R₂) =
- x⋆ ; terme général de (R₁) ; comportement de (R₂) :

## CP4.7 — Moments le long d'axes, einsum et estimateur de Horvitz-Thompson

- a) forme de T.sum(axis=1) :
- b) T.mean(axis=(1, 2)) =
- c) T.var(axis=1, ddof=1) =
- d) np.einsum("ijk,k->ij", T, w) =
- e) Ŷ pour S = {1, 3, 5} =
- f) Var(Ŷ) =
- c) la variance de deux valeurs ; E[Ŷ] ; le rucher qui apporte le plus de variance :

## CP4.8 — Une démonstration au choix (sujet A ou B)

Sujet choisi :

1.
2.
3.
4.

## CP4.9 — Corriger une copie : cinq erreurs

- a) lettres des lignes fausses :
- b) corrections :
  -
  -
  -
  -
  -

## CP4.10 — Problème de synthèse : ajuster une loi exponentielle, du graphe de calcul au pas critique

- a) L(0, 0) =
- b) [ū₁, ū₂, ū₃] =
- c) gradient en (0, 0) =
- d) [a₁, b₁] =
- e) L(a₁, b₁) =
- f) (a⋆, b⋆) =
- g) hessienne en (a⋆, b⋆) =
- h) valeurs propres =
- i) pas critique =
- La hessienne générale et les termes qui disparaissent ; le pas 0,1 près du minimum, et le premier pas :

---

## Après l'examen : ma note

Remplis ce tableau avec le barème de `03_examen_corrige.md` (et la vérification du notebook).

| Question | Points | Mes points | ⏱️ réel | À revoir (remédiation du corrigé) |
|---|---|---|---|---|
| CP4.Q1 | 1,5 | | | |
| CP4.1 | 2 | | | |
| CP4.2 | 2 | | | |
| CP4.3 | 2 | | | |
| CP4.4 | 1,75 | | | |
| CP4.5 | 2 | | | |
| CP4.6 | 1,75 | | | |
| CP4.7 | 1,5 | | | |
| CP4.8 | 2 | | | |
| CP4.9 | 1,25 | | | |
| CP4.10 | 2,25 | | | |
| **Total** | **20** | | | |

**Ce que je refais dans une semaine** (les questions où j'ai eu moins de la moitié des points) :

**Ce que je retiens de cet examen** (deux ou trois lignes, à reporter dans `mon_travail/suivi/journal.md`) :
