# M21 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m21_convolution/06_mes_reponses.md` (créée par `python tools/start_chapter.py M21`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : une convolution pleine a $n + k - 1$ termes et pour somme le produit des sommes, une corrélation se retrouve par la convolution du noyau retourné, une matrice de Toeplitz a ses diagonales constantes, un nombre de positions se vérifie sur la dernière fenêtre, un noyau séparable redonne le noyau par son produit extérieur, un pire cas L∞ ne dépend que des signes. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une matrice avec `\begin{pmatrix} … \end{pmatrix}`, une convolution comme `$\mathbf{x} * \mathbf{w}$` et une corrélation comme `$\mathbf{w} \star \mathbf{x}$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M21.Q1 — Convolution ou corrélation : retourner, glisser, sommer

1. 
2. 
3. 
4. 
5. 
6. 

### M21.Q2 — Les propriétés de la convolution : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M21.Q3 — Lire une matrice de Toeplitz : diagonales, coefficients non nuls, nombre de lignes

1. 
2. 
3. 
4. 
5. 
6. 

### M21.Q4 — Équivariant, invariant, ou ni l'un ni l'autre ? Décalages, bords, pas et pooling

1. 
2. 
3. 
4. 
5. 
6. 

### M21.Q5 — Combien de positions ? Pas, dilatation, padding et insertion de zéros

1. 
2. 
3. 
4. 
5. 
6. 

### M21.Q6 — Canaux, groupes, convolution 1 × 1 et noyaux séparables : compter

1. 
2. 
3. 
4. 
5. 
6. 

### M21.Q7 — Composer des convolutions : noyau, pas et champ récepteur

1. 
2. 
3. 
4. 
5. 
6. 

### M21.Q8 — Le pire cas d'une perturbation bornée : quelle norme, quel vecteur ?

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M21.R1 — La moyenne mobile d'une suite (R5)

1. 
2. 
3. 
4. 
5. 

### M21.R2 — La matrice d'une application linéaire, son noyau et son rang (M12a)

1. 
2. 
3. 
4. 
5. 
6. 

### M21.R3 — Le rang d'un produit extérieur u vᵀ et la décomposition en valeurs singulières (M12d)

1. 
2. 
3. 
4. 
5. 
6. 

## ✏️ Papier-crayon

### Ex M21.1 — Deux dés truqués et un produit de polynômes : la même convolution

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M21.2 — Convoluer et corréler un signal à la main, dans les trois modes

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M21.3 — Des pochoirs de différences finies : dérivée et dérivée seconde d'un signal échantillonné

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M21.4 — La matrice de Toeplitz d'une convolution pleine et d'une convolution valide : coefficients non nuls, rang et noyau

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

### Ex M21.5 — Décaler puis filtrer, ou filtrer puis décaler : l'équivariance, ses bords et son pas

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M21.6 — Compter les positions d'une fenêtre : pas, dilatation, padding, « même taille » avec un pas, et le problème inverse

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M21.7 — Sous-échantillonner et insérer des zéros : la convolution transposée d'un signal et ses recouvrements

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M21.8 — Une carte de températures filtrée par un laplacien discret et par un lissage séparable

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M21.9 — Paramètres et coût d'un filtrage à plusieurs canaux : standard, groupé, par canal, 1 × 1

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

### Ex M21.10 — Le noyau équivalent de deux lissages successifs, et le champ récepteur d'une pile avec pas et dilatation

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M21.11 — Le pire cas d'une erreur de capteurs bornée : une forme linéaire sur les boules L∞ et L2

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

## ∂ Démonstrations

### Ex M21.12 — La convolution est commutative et associative ; la corrélation croisée ne l'est pas

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M21.13 — Les applications linéaires qui commutent avec le décalage circulaire sont les convolutions circulaires ; la transposée d'une matrice circulante

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M21.14 — Le nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 quand la fenêtre tient, par un dénombrement

1. 
2. 
3. 
4. 
5. 

### Ex M21.15 — Le champ récepteur d'une pile de convolutions : récurrence et forme close

1. 
2. 
3. 
4. 
5. 

### Ex M21.16 — Le maximum d'une forme linéaire sur une boule L∞ vaut ε‖g‖₁, atteint en ε signe(g)

1. 
2. 
3. 
4. 
5. 

## 🔗 🗣️ Pont et explication

### Ex M21.17 — Pont : filtrer une grille à trois canaux comme les bibliothèques, formes (C, H, W), poids (C_out, C_in, k, k), et sans retournement

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

### Ex M21.18 — Expliquer avec une règle graduée et un pochoir pourquoi une convolution est équivariante, mais pas invariante

*Ta réponse en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### M21.E1 — « Pourquoi une convolution est-elle une matrice de Toeplitz, et pourquoi ne la forme-t-on jamais ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M21.19 — La convolution de deux suites, dans les trois modes · `convolve`

- ta boucle, les lignes gardées par « valid » et « same » ; les tests qui ont échoué d'abord, et pourquoi :

### Ex M21.20 — La matrice de Toeplitz d'une convolution · `toeplitz_matrix`

- comment tu remplis les colonnes, les rangs obtenus, et ce que dit la transposée selon le mode :

### Ex M21.21 — La convolution circulaire · `circular_convolve`

- comment tu lis les indices modulo n ; le profil lissé, et le retourné circulaire comparé au renversement :

### Ex M21.22 — Reconnaître un noyau séparable et le factoriser · `separable_factors`

- le test sur les valeurs singulières, la convention de signe ; le noyau bruité et sa tolérance :

### Ex M21.23 — Le noyau équivalent et le pas d'une pile de sommes glissantes · `equivalent_kernel`

- comment tu dilates chaque noyau ; les champs récepteurs obtenus, comparés à ∂ M21.15 :

### Ex M21.24 — Prédire l'effet d'un décalage de l'entrée sur un filtrage avec pas, puis vérifier

- tes prédictions avant l'expérience ; celles qui étaient fausses, et la règle qui les explique :

### Ex M21.25 — Le coût d'un filtrage direct ou séparable, selon la taille du noyau : mesurer, puis comparer à k² et 2k

- les temps mesurés, leur rapport, et à partir de quelle taille de noyau le séparable vaut la peine :

### Ex M21.26 — La carte des recouvrements d'une convolution transposée : un damier ou pas, selon k et s

- ce que montre chaque carte, et la règle qui dit quand il y a un damier :

### Ex M21.27 — Chasse à l'erreur : un noyau non retourné, des recouvrements supposés réguliers, un noyau de rang 2 « séparé »

- pour chaque erreur : ce qu'elle faisait, pourquoi la vérification fournie ne la voyait pas, et ta correction :

### Ex M21.28 — Un test de propriété : la matrice de Toeplitz fois x égale la convolution, pour des longueurs tirées au hasard

- ta fonction de test, ses cas limites, et le cas qui a démasqué la version fausse :

### Ex M21.29 — Défi : retrouver un noyau inconnu à partir d'un signal et de sa version filtrée bruitée, par les moindres carrés

- ta matrice, ton estimation, et comment l'erreur diminue avec le nombre de valeurs :
