# M10 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m10_separabilite_convexite/06_mes_reponses.md` (créée par `python tools/start_chapter.py M10`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Fais un **dessin** pour chaque exercice du plan ; écris chaque produit vectoriel avec ses deux vecteurs ($(\mathbf{a} - \mathbf{o}) \times (\mathbf{b} - \mathbf{o})$), chaque score avec son $b$, et divise une marge par $\lVert \mathbf{w} \rVert$. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M10.Q1 — Convexe ou non ?

1. 
2. 
3. 
4. 
5. 
6. 

### M10.Q2 — L'enveloppe convexe : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M10.Q3 — Séparable ou non ?

1. 
2. 
3. 
4. 
5. 
6. 

### M10.Q4 — Marge et astuce du biais

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M10.R1 — Hyperplans et distance à un hyperplan (M07)

1. 
2. 
3. 
4. 
5. 

### M10.R2 — L'inégalité de Cauchy-Schwarz (M07)

1. 
2. 
3. 
4. 
5. 

### M10.R3 — La sigmoïde et tanh (R6)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M10.1 — Convexe ou non : segments, demi-plans, intersections

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le dessin de K ; un segment qui sort de chaque ensemble non convexe de c) ; les trois points de g) dans K, et pourquoi leur combinaison y est aussi :

### Ex M10.2 — L'enveloppe convexe de huit points, à la main

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La chaîne du bas, test par test ; ce que dit le signe de d) sur P₆ ; les sommets qui changent en g), et pourquoi :

### Ex M10.3 — Une droite qui sépare deux petits nuages, et sa marge

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le dessin, avec les droites de b) et de e) ; le couple de points le plus proche, la droite de plus grande marge et sa marge vérifiée sur les six points :

### Ex M10.4 — L'astuce du biais : une droite du plan devient un plan de ℝ³ passant par l'origine

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Le côté de Δ de chaque point ; pourquoi ṽ · x̃ = 0 équivaut à x sur la droite de e) ; pourquoi la droite de f) passe par l'origine :

### Ex M10.5 — Borner une norme pas à pas : ‖v_{k+1}‖² ≤ ‖v_k‖² + c

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- v₀ · d₀ et ‖v₁‖², et pourquoi la borne est atteinte au premier pas, pas au second ; la borne de l'inégalité triangulaire comparée à celle de f), et une suite qui atteint la borne de f) ; pourquoi la borne ne s'applique pas aux cinq premiers pas de g) :

## ∂ Démonstrations

### Ex M10.6 — Un demi-espace est convexe, et une intersection de convexes aussi

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M10.7 — Deux nuages séparés par un hyperplan ont des enveloppes convexes disjointes

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M10.8 — La marge géométrique ne change pas quand on multiplie (w, b) par un réel positif

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M10.9 — Pont : seuil, sigmoïde, tanh et ReLU appliqués à un même score linéaire

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Pourquoi la ligne de niveau de g) est parallèle à la frontière ; les trois points rangés par sortie croissante, avec chaque activation ; les activations pour lesquelles « sortie > 1/2 » est le demi-plan z > 0 :

### Ex M10.10 — MML §12.1 : les hyperplans séparateurs, en anglais

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M10.11 — Expliquer la convexité et l'enveloppe convexe avec un élastique

*Huit lignes au plus, sans formule.*

> 

## 💼 Entretien

### M10.E1 — « Que veut dire « linéairement séparable », et comment le vérifier ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M10.12 — L'enveloppe convexe dans le plan : la chaîne monotone d'Andrew · `convex_hull_2d`

- Le dessin de P et de son enveloppe ; le point au milieu d'un côté, et le test qui l'écarte ; ce que rendrait un test < 0 :

### Ex M10.13 — Séparabilité par programmation linéaire, et marge géométrique · `is_linearly_separable, margin_of_separator`

- Où est l'origine par rapport à la classe +1, et pourquoi a) serait faux sans biais ; pourquoi b) est faux sans calcul ; d) à la main, et le point le plus proche ; pourquoi e) est négatif et n'est pas l'opposé de d) ; ce que rendrait un test avec ≥ 0 :

### Ex M10.14 — Prédire : n points aux labels tirés au hasard en dimension d sont-ils séparables ?

- Mes prédictions avant l'expérience (et pourquoi) ; les huit étiquetages de trois points d'une droite, et ceux qui ne sont pas séparables ; ce que b) et c) ont en commun ; ce que cela dit d'un classifieur parfait sur l'entraînement quand d est grand :

### Ex M10.15 — Deux nuages, leurs enveloppes convexes et un hyperplan séparateur avec sa marge

- Les points qui touchent les bords de la bande ; pourquoi la bande est vide ; jusqu'où élargir la bande sans changer la direction :

### Ex M10.16 — Chasse à l'erreur : un produit vectoriel de signe inversé, une marge non normalisée

- Les deux lignes corrigées ; pourquoi b) donne quand même les bons sommets ; les tests qui attrapent chaque erreur :

### Ex M10.17 — Des tests de propriétés pour l'enveloppe convexe

- Pourquoi le mauvais sens échoue à deux propriétés ; la propriété qui attrape un point au milieu d'un côté ; une enveloppe qui passe les quatre tests est-elle forcément juste ? :

### Ex M10.18 — Défi : la plus grande marge possible entre deux nuages donnés, à 1 % près

- La marge de la médiatrice des barycentres, et pourquoi elle est loin du compte ; ma méthode ; les points qui touchent les bords de la bande :
