# CP6 · Ma copie de l'examen blanc

> Ta copie de ce fichier est dans `mon_travail/checkpoints/partie_6/04_mes_reponses.md` (créée par `python tools/start_chapter.py CP6`) : c'est **elle** que tu remplis, pendant l'examen, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une partie des points d'une question de calcul va à la méthode. Tu peux aussi composer sur papier, puis recopier ici tes réponses finales.

**Date :** · **Début :** · **Fin :** · **Durée :**

## CP6.Q1 — Dix affirmations sur la partie VI, deux par chapitre

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

## CP6.1 — Un vecteur gaussien de dimension 2 : loi marginale, loi conditionnelle, et la loi de μ + Lε

- a) L =
- b) loi de x₂ : [moyenne, variance] =
- c) loi de x₂ sachant x₁ = 48 : [moyenne, variance] =
- d) loi de x₁ sachant x₂ = 48,5 : [moyenne, variance] =
- e) μ + Lε =
- f) covariance des tirages du collègue =
- LLᵀ ; x₁ et x₂ en fonction de ε₁ et ε₂, et pourquoi la variance de c) est l₂₂² ; la loi des tirages du collègue, et son point pour le même ε :

## CP6.2 — La divergence KL entre deux gaussiennes de dimension 2, et une interpolation sphérique

- a) tr(Σ₁⁻¹Σ₀) =
- b) δᵀΣ₁⁻¹δ =
- c) KL(p₀ ‖ p₁) =
- d) Ω (en degrés) =
- e) slerp(u, v ; 1/4) =
- f) norme du point de la ligne droite pour t = 1/4 :
- Les trois termes de la KL ; la norme du point de e) ; les angles de u avec les points de e) et de f) :

## CP6.3 — Un mélange de deux gaussiennes de variances connues et trois mesures : responsabilités, un pas d'EM sur le poids et les moyennes, et l'écart à l'ELBO d'une affectation dure

- a) [r₁₁, r₂₁, r₃₁] =
- b) π₁ après le pas M =
- c) [μ₁, μ₂] après le pas M =
- d) ln p(x₁, x₂, x₃) − ELBO(q) pour l'affectation dure =
- Les trois nombres avant ln(π₁/π₂) ; pourquoi l'écart de d) est une somme de KL égales à −ln r ; la loi q qui l'annule :

## CP6.4 — Une chaîne de Markov à trois états : loi à deux pas, et la valeur d'une politique fixée par le système de Bellman, quand une ligne finit

- a) μ₂ =
- b) probabilité d'être sortie du domaine dans deux ans :
- c) [V(0), V(1), V(2)] =
- d) récolte moyenne de l'année 2 :
- P et les sommes de ses lignes ; le système V = r + PV, résolu à partir de V(2) ; pourquoi γ = 1 est permis :

## CP6.5 — Un jeu à somme nulle 2 × 2 en stratégies mixtes, et W₁ entre deux petits échantillons de même taille

- a) [maximin, minimax] =
- b) p⋆ =
- c) q⋆ =
- d) valeur du jeu :
- e) W₁ =
- f) W₂ =
- Pourquoi pas de point selle ; les deux égalités d'indifférence ; l'appariement ; W₁ comparé à l'écart des moyennes :

## CP6.6 — Des distances aux positions : double centrage, matrice de Gram, et une configuration à une isométrie près

- a) s =
- b) G =
- c) valeurs propres non nulles (de la plus grande à la plus petite) =
- d) carte (une ligne par bouée) =
- Les rᵢ ; G1 = 0 ; AB² sur la carte ; l'isométrie possible :

## CP6.7 — La distance de Fréchet de deux gaussiennes du plan de covariances proportionnelles, et le biais de la distance entre deux moyennes estimées

- a) valeurs propres de Σ_A Σ_B (de la plus grande à la plus petite) =
- b) part des covariances dans W₂² =
- c) W₂ =
- d) E‖x̄_A − x̄_B‖² (30 et 20 jours) =
- e) E‖x̄₁ − x̄₂‖² (deux fois 30 jours de la ferme A) =
- f) plus petit n :
- Les valeurs propres de Σ_A ; la part des covariances en fonction de tr Σ_A ; ce que dit e) :

## CP6.8 — Une démonstration au choix (sujet A ou B)

Sujet choisi :

1.
2.
3.
4.

## CP6.9 — Corriger une copie : cinq erreurs, une par chapitre

- a) lettres des lignes fausses (dans n'importe quel ordre) :
- b) corrections :
  -
  -
  -
  -
  -

## CP6.10 — Problème de synthèse : une file d'attente à trois états suivie de façon gloutonne, puis échantillonnée après la troncature top-p de ses transitions : lois conditionnelles, coût en KL et nouvelle loi stationnaire

- a) [f(0), f(1), f(2)] =
- b) [prépériode, période] =
- c) S₁ (par probabilité décroissante) =
- d) p_{S₁} =
- e) KL(p_{S₁} ‖ p₁) =
- f) distance en variation totale :
- g) P′ =
- h) π′ =
- Les cinq premiers termes et la borne de μ + λ ; pourquoi KL(p₁ ‖ p_{S₁}) est infinie ; pourquoi π′₀ = 0, et ce que cela dit de la file vide ; pourquoi le simulateur aléatoire ne boucle pas forcément :

---

## Après l'examen : ma note

Remplis ce tableau avec le barème de `03_examen_corrige.md` (et la vérification du notebook) : un point par minute prévue, partagé également entre les sous-questions de chaque question. Ta note sur 20 est ton total multiplié par 20/111 (divisé par 5,55).

| Question | Points | Mes points | ⏱️ réel | À revoir (remédiation du corrigé) |
|---|---|---|---|---|
| CP6.Q1 | 10 | | | |
| CP6.1 | 10 | | | |
| CP6.2 | 9 | | | |
| CP6.3 | 10 | | | |
| CP6.4 | 9 | | | |
| CP6.5 | 9 | | | |
| CP6.6 | 8 | | | |
| CP6.7 | 9 | | | |
| CP6.8 | 12 | | | |
| CP6.9 | 9 | | | |
| CP6.10 | 16 | | | |
| **Total** | **111** | | | |
| **Note sur 20** (total × 20/111) | **20** | | | |

**Ce que je refais dans une semaine** (les questions où j'ai eu moins de la moitié des points) :

**Ce que je retiens de cet examen** (deux ou trois lignes, à reporter dans `mon_travail/suivi/journal.md`) :
