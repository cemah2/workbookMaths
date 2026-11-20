# MB4 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/mb4_rang_faible/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB4`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : le rang d'une matrice $(m, n)$ est au plus $\min(m, n)$, et $\mathbf{C}\mathbf{F}$ doit redonner $\mathbf{M}$ (essaie une ligne) ; $\mathbf{F}$ vaut l'identité dans les colonnes pivots ; $r(m + n - r) \le r(m + n)$, et vaut $mn$ quand $r = \min(m, n)$ ; une part d'énergie est entre 0 et 1, et croît avec $r$ ; le rang stable est entre 1 et le rang ; un poids corrigé est négatif exactement quand l'ingrédient est dans plus de la moitié des fiches ; la saturation vaut 1 pour une mention, et reste sous $k_1 + 1$ ; des points de Borda additionnent $m\frac{n(n - 1)}{2}$ en tout ; une somme des $\frac{1}{c + \text{rang}}$ ne dépend que des rangs ; recall@k, precision@k et un rang réciproque sont entre 0 et 1, et un MRR se compare à $\frac{H_n}{n}$. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice comme `$\mathbf{M}$`, une norme comme `$\lVert\mathbf{M}\rVert_F$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### MB4.Q1 — Rang, factorisation et stockage : vrai ou faux, et le rang d'une somme de produits extérieurs

1. 
2. 
3. 
4. 
5. 

### MB4.Q2 — Le poids d'un ingrédient rare, la saturation et la normalisation : signe, sens de variation, limites

1. 
2. 
3. 
4. 
5. 

### MB4.Q3 — Fusionner des classements : ce que change une nouvelle échelle de notes, ce que change la constante c

1. 
2. 
3. 
4. 
5. 

### MB4.Q4 — recall@k, precision@k, taux de succès et MRR : définitions, et leurs valeurs pour un ordre tiré au hasard

1. 
2. 
3. 
4. 
5. 

## 🔁 Rappels

### MB4.R1 — Le rang d'un produit, d'un produit extérieur et d'une somme (M12a)

1. 
2. 
3. 
4. 
5. 

### MB4.R2 — L'approximation de rang k par la SVD et son erreur de Frobenius (M12d, MML §4.6)

1. 
2. 
3. 
4. 
5. 

### MB4.R3 — L'information −ln p d'un événement, la cote et le logit (M06, R6)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex MB4.1 — Les ventes de quatre boulangeries sur cinq produits : le rang, la factorisation par les colonnes pivots, une seconde factorisation (CG)(G⁻¹F), et les nombres stockés ou libres

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB4.2 — Un tableau de relevés de stations météo donné par ses valeurs singulières : énergie captée, rang effectif à 99 %, rang stable, puis le coût de C(Fx) et de (CF)x pour un et pour mille vecteurs

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex MB4.3 — Les ingrédients d'un carnet de recettes : surprise, cote, poids corrigé par ½ et son signe, la variante toujours positive, puis la saturation et la normalisation d'une mention répétée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- dans ta copie :

### Ex MB4.4 — Trois jurys classent cinq pâtissiers : les points de Borda, la somme des 1/(c + rang) pour c = 2 et c = 10, et la somme des notes qui change de gagnant quand un jury passe de 20 à 100 points

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

## ∂ Démonstrations

### Ex MB4.5 — Une matrice de rang r est un produit C F de r colonnes par r lignes ; deux telles factorisations diffèrent d'une matrice inversible ; le rang est le plus petit nombre de produits extérieurs dont elle est la somme

1. 
2. 
3. 

### Ex MB4.6 — Une fusion par les rangs ne change pas quand un jury change d'échelle ; j-ième pour deux jurys bat premier pour un seul si et seulement si j < c + 2 ; quand c grandit, la somme des 1/(c + rang) range selon le nombre de listes, puis la somme des rangs

1. 
2. 
3. 

## 🗣️ Explication

### Ex MB4.7 — Expliquer à un pâtissier pourquoi un ingrédient présent dans toutes les recettes n'aide pas à retrouver la sienne, et pourquoi la dixième mention compte moins que la première

*Ta réponse en 5 à 8 phrases, sans formule.*

> 

## 💼 Entretien

### MB4.E1 — « Comment combiner les classements de deux systèmes dont les scores ne sont pas sur la même échelle ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex MB4.8 — La factorisation de rang C F : les colonnes pivots de M et les lignes non nulles de sa forme échelonnée réduite · rank_factorization

> 

### Ex MB4.9 — Les points de Borda de classements complets, et le MRR exact d'un ordre tiré au hasard, en fractions · borda_scores, random_ranking_mrr

> 

### Ex MB4.10 — Prédire le MRR d'un ordre tiré au hasard parmi 10, 100 puis 1 000 candidats, puis le simuler et le comparer à H_n/n

> 

### Ex MB4.11 — Les courbes de saturation x ↦ x(k₁ + 1)/(x + k₁) de k₁ = 0 à l'infini, et ce que la normalisation par la longueur leur fait

> 

### Ex MB4.12 — Chasse à l'erreur : C pris dans la forme réduite au lieu de M, un classement lu comme la liste des rangs des candidats, un poids de rareté écrit ln(n/N)

> 

### Ex MB4.13 — Défi : retrouver le rang caché de cinq tableaux bruités, cinq fois sur cinq, par leurs valeurs singulières

>
