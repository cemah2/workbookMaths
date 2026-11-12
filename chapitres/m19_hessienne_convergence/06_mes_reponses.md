# M19 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m19_hessienne_convergence/06_mes_reponses.md` (créée par `python tools/start_chapter.py M19`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une hessienne est symétrique, un point fixe vérifie l'équation de l'itération, un itéré de Richardson se rapproche de la solution quand le pas est sous le pas critique, un terme d'une récurrence se retrouve par la formule générale, une projection sur une boule a la norme du rayon. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, un nombre complexe comme `$0{,}3 + 0{,}4i$`, une norme comme `$\lVert\mathbf{x}\rVert$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M19.Q1 — La hessienne : de quelle taille, symétrique, de quoi ?

1. 
2. 
3. 
4. 
5. 
6. 

### M19.Q2 — Minimum, maximum, selle ou direction plate ?

1. 
2. 
3. 
4. 
5. 
6. 

### M19.Q3 — Converge ou pas : lire les valeurs propres de M

1. 
2. 
3. 
4. 
5. 
6. 

### M19.Q4 — Le pas de Richardson : lire la convergence sur les valeurs propres de I − ωA

1. 
2. 
3. 
4. 
5. 
6. 

### M19.Q5 — Le conditionnement : ce qui ralentit, ce qui ne change rien

1. 
2. 
3. 
4. 
5. 
6. 

### M19.Q6 — Module d'un nombre complexe et racines d'un trinôme

1. 
2. 
3. 
4. 
5. 
6. 

### M19.Q7 — Un gradient estimé sur un échantillon : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M19.Q8 — Boule ou pavé : la direction est-elle gardée ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M19.R1 — Le théorème spectral et les valeurs propres d'une matrice symétrique (M12c)

1. 
2. 
3. 
4. 
5. 
6. 

### M19.R2 — Suites géométriques et récurrences d'ordre 1 (R5)

1. 
2. 
3. 
4. 
5. 

### M19.R3 — Le conditionnement par la SVD (M12d)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M19.1 — La hessienne d'une fonction de trois variables, et son développement de Taylor d'ordre 2

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M19.2 — Classer les points critiques d'une fonction de trois variables

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M19.3 — Une itération linéaire 2 × 2 : point fixe, erreur, et convergence par les valeurs propres

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M19.4 — Résoudre un système 2 × 2 par l'itération de Richardson : trois pas à la main, et le pas critique

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M19.5 — Le meilleur pas de Richardson (énoncé), et le nombre d'itérations pour gagner six décimales

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M19.6 — Une récurrence d'ordre 2 à racines réelles : terme général et convergence

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M19.7 — Une récurrence d'ordre 2 à racines complexes : module et oscillation amortie

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M19.8 — Une pente estimée sur B points tirés au hasard : espérance et variance de l'estimation

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

### Ex M19.9 — Projeter un même vecteur sur une boule et sur un pavé : deux points, deux directions

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

## ∂ Démonstrations

### Ex M19.10 — Une itération linéaire de matrice symétrique converge pour tout départ si et seulement si ses valeurs propres sont de module < 1

1. 
2. 
3. 
4. 
5. 

### Ex M19.11 — L'itération de Richardson converge si et seulement si 0 < ω < 2/λmax

1. 
2. 
3. 
4. 
5. 

### Ex M19.12 — Une récurrence d'ordre 2 converge si et seulement si ses racines sont de module < 1 : le critère |q| < 1 et |p| < 1 + q

1. 
2. 
3. 
4. 
5. 

### Ex M19.13 — La projection sur une boule est son point le plus proche, et elle garde la direction

1. 
2. 
3. 
4. 
5. 

## 🔗 📖 🗣️ Ponts, lecture et explication

### Ex M19.14 — Pont : un pas de Richardson est un pas de descente sur ½ xᵀA x − bᵀx (énoncé, sans calcul)

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M19.15 — Pont : le préconditionnement diagonal, une idée commune à plusieurs méthodes de workbookIA 19

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M19.16 — MML §5.7 et §5.8 : dérivées d'ordre supérieur et Taylor à plusieurs variables, en anglais

1. 
2. 
3. 
4. 
5. 

### Ex M19.17 — MML §7.1 : la descente de gradient, le pas, le momentum et la version stochastique, en anglais

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M19.18 — Expliquer, sur un dessin de lignes de niveau, pourquoi un système mal conditionné converge lentement

*Ton dessin (décrit ou photographié), ta réponse en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M19.E1 — « Que nous apprend la hessienne en un minimum ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

### M19.E2 — « Pourquoi un mauvais conditionnement ralentit-il une méthode itérative ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M19.19 — La hessienne par différences centrées · `numerical_hessian`

- les deux formules, le pas, le nombre d'évaluations de f ; les tests qui ont échoué d'abord, et pourquoi :

### Ex M19.20 — Le pas critique d'une matrice symétrique définie positive, et les itérés de Richardson · `critical_step_size, richardson_iterates`

- les contrôles de critical_step_size ; les itérés obtenus, comparés à la fiche :

### Ex M19.21 — Une récurrence linéaire d'ordre d · `linear_recurrence`

- l'ordre des coefficients ; les suites obtenues, comparées aux formules du §6 :

### Ex M19.22 — `scipy.sparse.linalg.cg` : le gradient conjugué contre Richardson

- les nombres d'itérations du gradient conjugué et de Richardson, et ce qu'ils deviennent quand n grandit :

### Ex M19.23 — Prédire le nombre d'itérations de Richardson selon ω, puis vérifier

- tes prédictions avant l'expérience ; les nombres mesurés, et l'écart à la formule :

### Ex M19.24 — Le nombre d'itérations contre le conditionnement : une droite en échelle logarithmique

- la pente de la droite, et ce qu'elle dit du lien entre le nombre d'itérations et κ :

### Ex M19.25 — Les itérés de Richardson sur les lignes de niveau d'une forme quadratique

- ce que montre chaque dessin, selon le pas :

### Ex M19.26 — Chasse à l'erreur : un pas réglé sur λmin, une hessienne non symétrique, le module d'une racine complexe

- pour chaque erreur : ce qu'elle faisait, pourquoi la vérification fournie ne la voyait pas (ou criait à tort), et ta correction :

### Ex M19.27 — Un critère d'arrêt : le résidu relatif ‖b − A x‖/‖b‖ et un nombre maximal d'itérations

- ton critère d'arrêt, la tolérance, et ce qui se passe quand le pas est trop grand :

### Ex M19.28 — Défi : le schéma saute-mouton d'un oscillateur, x_{k+1} = (2 − h²Ω²) x_k − x_{k−1}, borné si et seulement si hΩ < 2

- la condition trouvée sur hΩ, le module des racines, et ce que montrent les simulations :
