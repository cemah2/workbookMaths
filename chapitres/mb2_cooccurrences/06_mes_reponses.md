# MB2 · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/mb2_cooccurrences/06_mes_reponses.md` (créée par `python tools/start_chapter.py MB2`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : un nombre écrit en base 2 ou 16 se relit en base 10 par une somme de puissances, et $N$ valeurs demandent $\lceil\log_2 N\rceil$ bits ; une PMI se calcule sur des **probabilités**, avec $\ln$, en nats, et vaut $-\infty$ sur une case vide ; elle ne dépasse jamais $\min(-\ln p(x), -\ln p(y))$ ; l'information mutuelle, moyenne des PMI pondérée par $p(x, y)$, est positive ou nulle ; une loi lissée a une somme de 1, et le lissage décale toute une colonne de la même constante ; $(\mathbf{U}_k\mathbf{S}_k^\beta)(\mathbf{V}_k\mathbf{S}_k^{1-\beta})^\top$ redonne $\mathbf{M}_k$ pour tout $\beta$ ; un logit est le logarithme d'une **cote**, et un sous-échantillonnage des négatifs le fait monter de $\ln(s_1/s_0)$ ; un cosinus est entre $-1$ et 1 et ne dépend pas des longueurs ; un vecteur sans sa direction $\mathbf{u}$ est orthogonal à $\mathbf{u}$ ; une moyenne masquée ne compte que les vrais relevés. Les formules s'écrivent en LaTeX entre `$` (R0 §5), un vecteur comme `$\mathbf{q}$` et une norme comme `$\lVert\mathbf{c}\rVert$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### MB2.Q1 — Bases 2 et 16 : le nombre de chiffres d'un entier, la valeur d'un octet, les bits qu'il faut pour N valeurs

1. 
2. 
3. 
4. 

### MB2.Q2 — La PMI d'une case : son signe, −∞, la PPMI, la borne des événements rares, et l'information mutuelle qui en est la moyenne

1. 
2. 
3. 
4. 
5. 

### MB2.Q3 — Lisser une marge : quelles colonnes gagnent, de combien bouge la PMI d'une colonne, et quels classements le lissage garde

1. 
2. 
3. 
4. 
5. 

### MB2.Q4 — Répartir les valeurs singulières entre deux facteurs : ce qui dépend de β, ce qui n'en dépend pas, et pourquoi ne pas centrer une table creuse

1. 
2. 
3. 
4. 
5. 

### MB2.Q5 — Le logit d'un taux et le sous-échantillonnage : ce qui bouge (l'ordonnée à l'origine), de combien, dans quel sens

1. 
2. 
3. 
4. 
5. 

### MB2.Q6 — Analogies, direction retirée et moyenne masquée : vrai ou faux, avec une raison

1. 
2. 
3. 
4. 
5. 

## 🔁 Rappels

### MB2.R1 — L'information mutuelle d'un tableau 2 × 2 (M06)

1. 
2. 
3. 
4. 

### MB2.R2 — La meilleure approximation de rang 1 d'une matrice et son erreur (Eckart-Young, M12d)

1. 
2. 
3. 
4. 

### MB2.R3 — Cosinus, projection sur une droite et prototype d'une classe (M07, workbookIA B1)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex MB2.1 — Des entiers en base 2 et en base 16 : conversions, une couleur #RRGGBB, les bits pour 5 000 codes, et un mot de 16 bits découpé en deux champs

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB2.2 — Cent oiseaux, trois milieux, quatre espèces : la PMI des cases, le lift d'une règle, la PPMI, l'espèce vue une seule fois, et l'information mutuelle comme moyenne

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex MB2.3 — Lisser la marge des espèces de la même table (α = 1/3) : la loi lissée, le décalage de la PMI de chaque colonne, et le classement des espèces d'un milieu avant et après

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB2.4 — Quatre magasins, trois produits, une table de rang 2 de SVD donnée : les facteurs U S^β et V S^{1−β} pour β = 0, ½ et 1, leur produit, et le cosinus de deux magasins

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB2.5 — Une bannière affichée 3 200 fois et cliquée 50 fois : le logit de vraisemblance maximale, puis un non-clic gardé sur 9, le décalage de ln 9 et sa correction

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex MB2.6 — Yaourt et fromage blanc, nature et sucrés : mesurer le parallélogramme d'une analogie (défaut, rapport ε, borne du cosinus), et dire si d peut l'emporter sur c

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex MB2.7 — Des mesures d'animaux en logarithme : la direction de taille estimée sur deux différences, la retirer de trois animaux, et les distances qui restent

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

## ∂ Démonstrations

### Ex MB2.8 — La PMI est majorée par −ln p(x) et par −ln p(y), avec égalité quand x n'arrive qu'avec y ; la PMI normalisée est donc au plus 1

1. 
2. 
3. 
4. 
5. 

### Ex MB2.9 — Répartir les valeurs singulières entre deux facteurs : le produit ne dépend pas de β, les produits scalaires des lignes si

1. 
2. 
3. 
4. 

### Ex MB2.10 — Sous-échantillonner une classe : par la formule de Bayes, la cote observée est celle de la population multipliée par le rapport des taux de sélection s₁/s₀ ; dans un modèle logistique, seule l'ordonnée à l'origine bouge, de ln(s₁/s₀)

1. 
2. 
3. 
4. 
5. 

## 🔗 🗣️ Pont et explication

### Ex MB2.11 — Pont : résumer des séries de relevés de longueurs différentes par une moyenne masquée, montrer que le remplissage ne change rien, et compter les comparaisons par paires

- a :
- b :
- c :
- d :
- e :
- dans ta copie :

### Ex MB2.12 — Expliquer à un ornithologue ce que mesure la PMI d'un milieu et d'une espèce, et pourquoi une espèce vue une seule fois a la plus grande

*Ta réponse en 6 à 10 phrases, sans formule, puis en 3 phrases.*

> 

## 💼 Entretien

### MB2.E1 — « Pourquoi ne centre-t-on pas une grande table de comptages creuse avant de la factoriser par une SVD tronquée ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex MB2.13 — La table des PMI d'une loi jointe, −∞ sur les cases vides · pmi

> 

### Ex MB2.14 — Deux briques : le logit d'une population estimé sur un échantillon cas-témoins, et retirer une direction des lignes d'une matrice · case_control_logit, remove_direction

> 

### Ex MB2.15 — Prédire puis mesurer la dispersion de la PMI estimée sur 400 observations, pour une case rare et une case fréquente, avec et sans lissage

> 

### Ex MB2.16 — Des magasins dans le plan des deux facteurs U₂S₂^β, pour β = 0, ½ et 1 : ce qui s'étire, et les angles qui changent

> 

### Ex MB2.17 — Chasse à l'erreur : une PMI calculée sans le total, des facteurs U S^β et V S^β, une direction retirée sans diviser par u·u

> 

### Ex MB2.18 — Un test de propriété de pmi sur des tables tirées au hasard : la borne, la transposition, et la moyenne qui redonne l'information mutuelle de M06

> 

### Ex MB2.19 — Défi : retrouver, sur 3 000 observations, les cinq paires les plus associées d'une table cachée de 10 × 10, sans se laisser piéger par les cases rares

>
