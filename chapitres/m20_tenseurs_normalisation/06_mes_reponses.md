# M20 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m20_tenseurs_normalisation/06_mes_reponses.md` (créée par `python tools/start_chapter.py M20`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une forme a le bon nombre d'éléments, une position dans la file se relit en indices par des divisions, un vecteur centré a une somme nulle, une estimation de Horvitz-Thompson ne contient que les unités tirées, une valeur singulière est positive. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, une formule d'einsum entre accents graves, comme `` `"ij,jk->ik"` `` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M20.Q1 — Forme, axes et nombre d'éléments

1. 
2. 
3. 
4. 
5. 
6. 

### M20.Q2 — Réduire le long de quel axe ?

1. 
2. 
3. 
4. 
5. 
6. 

### M20.Q3 — Lire une formule d'einsum

1. 
2. 
3. 
4. 
5. 
6. 

### M20.Q4 — Diviser par une probabilité : sans biais ou biaisé ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M20.R1 — Variance biaisée et non biaisée : ddof (M02c)

1. 
2. 
3. 
4. 
5. 

### M20.R2 — La projection orthogonale sur une droite (M12b)

1. 
2. 
3. 
4. 
5. 

### M20.R3 — La limite (1 + x/n)ⁿ → eˣ (M14)

1. 
2. 
3. 
4. 

## ✏️ Papier-crayon

### Ex M20.1 — Un tableau de mesures (stations × jours × heures) : les formes après réductions et remodelages

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

### Ex M20.2 — Écrire en notation d'Einstein : produit matriciel, trace, forme bilinéaire, produits de matrices empilées le long d'un axe

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- j :
- dans ta copie :

### Ex M20.3 — La matrice de centrage, et une standardisation qui ne voit ni translation ni dilatation

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- j :
- k :
- dans ta copie :

### Ex M20.4 — Un sondage à probabilités inégales : l'estimateur de Horvitz-Thompson d'un total, son espérance et sa variance

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- j :
- dans ta copie :

### Ex M20.5 — Un schéma d'Euler en L pas : la jacobienne d'un pas, celle de L pas, et la limite (1 + λT/L)ᴸ

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- j :
- k :
- dans ta copie :

## ∂ Démonstrations

### Ex M20.6 — La matrice de centrage est la projection orthogonale sur l'orthogonal de 1

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M20.7 — L'estimateur de Horvitz-Thompson est sans biais, et sa variance quand les inclusions sont indépendantes

1. 
2. 
3. 
4. 
5. 

## 🔗 🗣️ Pont et explication

### Ex M20.8 — Pont : où workbookIA 20 divise par une probabilité

- a :
- b :
- c :
- dans ta copie :

### Ex M20.9 — Expliquer ce qu'est un axe d'un tableau à quelqu'un qui ne connaît que les tableurs

*Ton explication, en 8 lignes au plus et sans formule.*

> 

## 💼 Entretien

### M20.E1 — « Pourquoi standardiser des données décalées ou dilatées donne-t-il le même résultat ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M20.10 — `einsum` pour deux tableaux, avec des boucles · `einsum_pair`

- comment tu lis la formule, comment tu trouves la longueur de chaque lettre ; les tests qui ont échoué d'abord, et pourquoi :

### Ex M20.11 — Moyennes et variances le long d'axes choisis · `moments_along_axes`

- comment tu normalises les axes, N, ddof ; le tableau standardisé et l'invariance observée :

### Ex M20.12 — L'estimateur de Horvitz-Thompson d'un total · `horvitz_thompson_total`

- tes contrôles des trois tableaux ; l'espérance obtenue par énumération :

### Ex M20.13 — Prédire la forme d'une réduction ou d'un einsum, puis vérifier

- tes prédictions avant l'expérience ; celles qui étaient fausses, et la règle qui les explique :

### Ex M20.14 — Simuler un sondage : Horvitz-Thompson contre la moyenne naïve, biais et variance

- les biais et écarts types relatifs des trois estimateurs, et ce que tu en retiens :

### Ex M20.15 — Le produit de L jacobiennes I + hJ : ses valeurs singulières extrêmes quand L grandit, à hL fixé

- ce que montre la figure quand L grandit, et les bornes de la fiche :

### Ex M20.16 — Chasse à l'erreur : une moyenne sur le mauvais axe, une diffusion silencieuse, un ddof oublié

- pour chaque erreur : ce qu'elle faisait, pourquoi la vérification fournie ne la voyait pas, et ta correction :

### Ex M20.17 — Un test de propriété : réduire sur deux axes d'un coup, ou l'un après l'autre

- ta fonction de test, les propriétés vérifiées, et ce qui change avec ddof = 1 :

### Ex M20.18 — Défi : des probabilités d'inclusion proportionnelles à la taille, et un estimateur presque sans variance

- ta façon de plafonner les probabilités, et l'écart type relatif obtenu :
