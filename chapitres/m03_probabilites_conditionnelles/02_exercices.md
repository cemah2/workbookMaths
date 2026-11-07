# M03 · Probabilités conditionnelles — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m03_probabilites_conditionnelles/06_mes_reponses.md` (créée par `python tools/start_chapter.py M03`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, ⚖️, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées. Avant chaque probabilité conditionnelle, écris-la avec le mot « sachant » et dis **par quoi tu divises** (le total d'une ligne, d'une colonne, ou de tout le tableau). Garde les fractions exactes jusqu'au bout, et n'arrondis qu'à la fin.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M03.Q1 — Jointe, marginale ou conditionnelle ? 🧠 ★ ⏱️ 4 min
*Fiche §1 et §2 · parcours C, E*

Une entreprise envoie un e-mail à ses clients et mesure qui l'ouvre et qui clique sur son lien. Pour chacune des phrases 1 à 4, dis si elle donne une probabilité jointe, marginale ou conditionnelle, et écris-la avec la notation $P(\ldots)$ (événements « ouvert » et « clic »).
1. « 4 % des destinataires ont ouvert l'e-mail et cliqué sur le lien. »
2. « 16 % des destinataires qui ont ouvert l'e-mail ont cliqué. »
3. « 25 % des destinataires ont ouvert l'e-mail. »
4. « Tous ceux qui ont cliqué avaient ouvert l'e-mail. »
5. D'après les phrases 1 et 4, que vaut $P(\text{clic})$ ? Les phrases 1, 2 et 3 sont-elles cohérentes entre elles ?
6. Vrai ou faux : dans un tableau de contingence, la somme des probabilités $P(Y = y \mid X = x)$ pour **une même** valeur $y$ et toutes les valeurs $x$ vaut 1.

### M03.Q2 — P(A sachant B) et P(B sachant A) 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Dans une entreprise, 40 % des salariés travaillent au service technique ; 25 % des salariés suivent une formation cette année, et 80 % des salariés en formation sont du service technique.
1. Que vaut $P(\text{technique} \cap \text{formation})$ ?
2. Que vaut $P(\text{formation} \mid \text{technique})$ ?
3. Vrai ou faux : si $P(A \mid B) = 0{,}9$, alors $P(B \mid A)$ est forcément grand aussi.
4. Vrai ou faux : $P(A \mid B) + P(\text{non } A \mid B) = 1$.
5. Vrai ou faux : $P(A \mid B) + P(A \mid \text{non } B) = 1$.
6. Un contrôle automatique signale 5 % des pièces d'une usine ; parmi les pièces signalées, 40 % sont vraiment défectueuses. Quelle part de **toutes** les pièces est à la fois signalée et défectueuse ?

### M03.Q3 — Indépendants ou incompatibles ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

On lance un dé équilibré à six faces.
1. $A$ = « le résultat est pair », $B$ = « le résultat est 1 ou 2 ». $A$ et $B$ sont-ils indépendants ?
2. $A$ = « pair », $C$ = « le résultat est 1 ou 3 ». $A$ et $C$ sont-ils indépendants ? Incompatibles ?
3. $P(E) = 0{,}3$, $P(F) = 0{,}5$ et $P(E \cap F) = 0{,}15$ : $E$ et $F$ sont-ils indépendants ?
4. Vrai ou faux : deux événements incompatibles, chacun de probabilité non nulle, peuvent être indépendants.
5. Vrai ou faux : si $E$ et $F$ sont indépendants, alors $E$ et « non $F$ » le sont aussi.
6. Vrai ou faux : trois événements indépendants deux à deux sont toujours mutuellement indépendants.

### M03.Q4 — Quelle métrique pour quelle probabilité ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

$Y$ est la vérité (1 = positif), $\hat{Y}$ la prédiction d'un classifieur. Donne le nom de la mesure :
1. $P(\hat{Y} = 1 \mid Y = 1)$
2. $P(Y = 1 \mid \hat{Y} = 1)$
3. $P(\hat{Y} = 0 \mid Y = 0)$
4. $P(\hat{Y} = 1 \mid Y = 0)$
5. $P(\hat{Y} = Y)$
6. On applique **le même** modèle à une population où la classe positive est deux fois plus rare. Lesquelles des cinq mesures précédentes restent les mêmes ?

### M03.Q5 — Moyennes de métriques 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C*

1. Precision 0,5 et recall 1 : que vaut le F1 ?
2. Vrai ou faux : le $F_2$ donne plus de poids à la precision qu'au recall.
3. Un classifieur à trois classes a des recalls de 0,9, 0,6 et 0,3. Que vaut sa balanced accuracy ?
4. Vrai ou faux : en multiclasse, quand chaque exemple a une seule vraie classe et une seule prédiction, le micro-F1 est égal à l'accuracy.
5. Un modèle prédit toujours la classe majoritaire (90 % des exemples). Que vaut son MCC ?
6. Vrai ou faux : le F1 macro donne autant de poids à une classe de 10 exemples qu'à une classe de 1 000 exemples.

### M03.Q6 — ROC et AUC : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Une AUC de 0,5 signifie que le modèle se trompe sur la moitié des exemples.
2. Si l'on multiplie tous les scores par 2, l'AUC ne change pas.
3. Le point $(0, 1)$ de la courbe ROC est celui d'un classifieur parfait.
4. Une AUC de 0,2 est pire que le hasard : ce modèle ne sert à rien.
5. L'AUC d'un modèle change quand la prévalence de la classe positive change.
6. Deux modèles qui ont la même AUC ont la même precision au seuil 0,5.

### M03.Q7 — Calibré ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

1. Parmi les jours où un modèle annonce « 70 % de risque de panne », la panne survient 7 jours sur 10. Que dit cette observation de sa calibration ?
2. Un modèle annonce toujours la même probabilité, égale à la prévalence. Est-il calibré ? Que vaut son AUC ?
3. Vrai ou faux : un modèle dont l'AUC vaut 0,95 est forcément bien calibré.
4. Que vaut le score de Brier d'un modèle qui annonce 1 pour chaque positif et 0 pour chaque négatif ?
5. Que vaut le score de Brier d'une prévision constante égale à 0,5, quelles que soient les données ?
6. On entraîne un modèle avec `class_weight="balanced"` sur des données qui ont 5 % de positifs. En moyenne, ses probabilités prédites sont-elles trop hautes ou trop basses pour la vraie population ?

<a id="rappels"></a>

## 🔁 Rappels

### M03.R1 — Arbres pondérés (R8) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

Un sac contient 3 boules rouges et 2 boules bleues. On tire une boule au hasard. Si elle est rouge, on lance une pièce équilibrée et l'on gagne sur « pile » ; si elle est bleue, on lance un dé à six faces et l'on gagne sur « 6 ».
1. Dessine l'arbre pondéré.
2. $P(\text{rouge et gagne})$ ?
3. $P(\text{bleu et gagne})$, en fraction ?
4. $P(\text{gagne})$, en fraction irréductible ?
5. $P(\text{perd})$ ?

### M03.R2 — Moyenne harmonique et moyenne pondérée (R1) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

1. La moyenne harmonique de 2 et 6 ?
2. La moyenne harmonique de 0,5 et 1 ?
3. La moyenne pondérée de 10 (poids 3) et 20 (poids 1) ?
4. La moyenne harmonique et la moyenne arithmétique de 0,9 et 0,1 ?
5. La moyenne harmonique **pondérée** de 0,5 (poids 1) et 1 (poids 4), c'est-à-dire l'inverse de la moyenne pondérée des inverses ?

### M03.R3 — Aire par la méthode des trapèzes (M02a) 🔁 ★ ⏱️ 5 min
*Fiche §7 · parcours C*

1. L'aire d'un trapèze de largeur 0,5 dont les côtés parallèles mesurent 0,4 et 0,8 ?
2. L'aire sous la ligne brisée qui relie $(0, 0)$, $(0{,}5 ;\ 0{,}6)$ et $(1, 1)$ ?
3. La méthode des trapèzes avec deux intervalles pour $\int_0^1 x^2\,\mathrm{d}x$, puis l'erreur commise ?
4. L'aire sous l'escalier $(0, 0) \to (0 ;\ 0{,}5) \to (0{,}5 ;\ 0{,}5) \to (0{,}5 ;\ 1) \to (1, 1)$ ?
5. Pourquoi un segment vertical n'ajoute-t-il rien à l'aire ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"7/9"` ;
- une liste entre crochets, comme `[-1.5, 2.5]` ; vrai ou faux par `True` ou `False` ; une lettre entre guillemets, comme `"B"`.

### Ex M03.1 — Un tableau de contingence : jointes, marginales, conditionnelles ✏️ ★ ⏱️ 20 min
**Objectif :** lire dans un tableau de contingence des probabilités jointes, marginales et conditionnelles, en choisissant le bon dénominateur.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

Un site de vente a classé 400 avis de clients selon leur note et selon qu'ils contiennent une photo :

| note \ photo | avec photo | sans photo |
|---|---|---|
| 1 ou 2 étoiles | 30 | 50 |
| 3 étoiles | 20 | 80 |
| 4 ou 5 étoiles | 70 | 150 |

On tire un avis au hasard parmi les 400.

| | Question | Réponse attendue |
|---|---|---|
| a | $P(\text{avec photo})$ | un nombre (2 décimales) |
| b | $P(\text{4 ou 5 étoiles})$ | un nombre (2 décimales) |
| c | $P(\text{4 ou 5 étoiles et avec photo})$ | un nombre (3 décimales) |
| d | $P(\text{4 ou 5 étoiles} \mid \text{avec photo})$ | un nombre (3 décimales) |
| e | $P(\text{avec photo} \mid \text{4 ou 5 étoiles})$ | un nombre (3 décimales) |
| f | $P(\text{avec photo} \mid \text{1 ou 2 étoiles})$ | un nombre (3 décimales) |
| g | la loi de la note sachant « avec photo », dans l'ordre du tableau | une liste de 3 nombres (3 décimales) |
| h | $P(\text{« 1 ou 2 étoiles »} \cup \text{« avec photo »})$ | un nombre (3 décimales) |

Dans ta copie : complète le tableau avec ses totaux. Compare f) à a) : la présence d'une photo est-elle indépendante de la note ? Vérifie que la liste de g) a une somme de 1.

### Ex M03.2 — L'indépendance, vérifiée dans un tableau ✏️ ★ ⏱️ 15 min
**Objectif :** décider par le calcul si deux variables sont indépendantes, et calculer les effectifs attendus sous l'hypothèse d'indépendance.
**Prérequis :** fiche §2 · **Parcours :** C, E

**Tableau 1.** Un test A/B montre à 1 000 visiteurs l'une de deux versions d'une page, et note s'ils cliquent sur le bouton principal :

| version \ clic | clic | pas de clic |
|---|---|---|
| A | 48 | 552 |
| B | 32 | 368 |

**Tableau 2.** Une boutique en ligne note, pour 500 visites, le moment de la visite et si elle se termine par un achat :

| moment \ achat | achat | pas d'achat |
|---|---|---|
| matin | 30 | 170 |
| soir | 60 | 240 |

| | Question | Réponse attendue |
|---|---|---|
| a | tableau 1 : $P(\text{clic})$ | un nombre (2 décimales) |
| b | tableau 1 : $P(\text{clic} \mid \text{version B})$ | un nombre (2 décimales) |
| c | tableau 1 : la version et le clic sont-ils indépendants ? | `True` ou `False` |
| d | tableau 2 : $P(\text{achat})$ | un nombre (2 décimales) |
| e | tableau 2 : $P(\text{matin}) \times P(\text{achat})$ | un nombre (3 décimales) |
| f | tableau 2 : $P(\text{matin et achat})$ | un nombre (2 décimales) |
| g | tableau 2 : le moment et l'achat sont-ils indépendants ? | `True` ou `False` |
| h | tableau 2 : l'effectif **attendu** de la case (soir, achat) si les deux variables étaient indépendantes, avec les mêmes totaux | un entier |

Dans ta copie : pour le tableau 1, vérifie l'indépendance de deux façons (par les conditionnelles, puis par le produit des marges dans une case). Pour le tableau 2, calcule le tableau entier des effectifs attendus. La différence entre la version A et la version B est-elle une bonne nouvelle pour l'équipe qui a dessiné la version B ?

### Ex M03.3 — Probabilités totales avec trois cas ✏️ ★ ⏱️ 15 min
**Objectif :** calculer une probabilité par la formule des probabilités totales, et mesurer l'effet d'un changement de taux ou de poids.
**Prérequis :** fiche §2 et §3 · **Parcours :** C, E

Un service en ligne répartit ses requêtes entre trois serveurs : le serveur $S_1$ en traite 45 %, $S_2$ 35 % et $S_3$ 20 %. Les taux de requêtes en erreur sont de 1 % pour $S_1$, 2 % pour $S_2$ et 4 % pour $S_3$. On tire une requête au hasard ; $E$ est l'événement « la requête finit en erreur ».

| | Question | Réponse attendue |
|---|---|---|
| a | $P(E)$ | un nombre (4 décimales) |
| b | $P(S_3 \cap E)$ | un nombre (3 décimales) |
| c | $P(\text{non } E)$ | un nombre (4 décimales) |
| d | le nombre moyen de requêtes en erreur sur 10 000 requêtes | un entier |
| e | $P(S_3 \mid E)$, par la définition de la probabilité conditionnelle | un nombre (2 décimales) |
| f | on répare $S_3$, dont le taux d'erreur passe à 2 % (les parts du trafic ne changent pas) : le nouveau $P(E)$ | un nombre (4 décimales) |
| g | sans réparer $S_3$, on envoie plutôt la moitié de son trafic à $S_2$ : le nouveau $P(E)$ | un nombre (4 décimales) |
| h | dans la situation de départ, le nombre moyen de requêtes en erreur **traitées par $S_1$**, sur 10 000 requêtes | un entier |

Dans ta copie : dessine l'arbre pondéré. Pourquoi a) est-il plus proche de 1 % que de 4 % ? Pourquoi e) est-il bien plus grand que 20 % ? Laquelle des deux améliorations, f) ou g), réduit le plus les erreurs ?

### Ex M03.4 — Une matrice de confusion lue comme des probabilités ✏️ ★ ⏱️ 20 min
**Objectif :** construire une matrice de confusion à partir d'une description, et en lire les mesures comme des probabilités conditionnelles.
**Prérequis :** fiche §4 et §5 · **Parcours :** C, E

Une caméra inspecte 2 000 pièces à la sortie d'une chaîne de montage. Parmi elles, 80 sont vraiment défectueuses (la classe positive). La caméra signale 160 pièces, dont 64 sont vraiment défectueuses.

| | Question | Réponse attendue |
|---|---|---|
| a | la prévalence des défauts | un nombre (2 décimales) |
| b | le recall de la caméra | un nombre (2 décimales) |
| c | sa spécificité | un nombre (2 décimales) |
| d | sa precision | un nombre (2 décimales) |
| e | son accuracy | un nombre (3 décimales) |
| f | sa valeur prédictive négative, $P(Y = 0 \mid \hat{Y} = 0)$ | un nombre (4 décimales) |
| g | $P(\hat{Y} = 1)$, la part des pièces signalées | un nombre (2 décimales) |
| h | son F1 | un nombre (4 décimales) |

Dans ta copie : écris la matrice de confusion complète (TP, FN, FP, TN, et les totaux). Pour chaque réponse de a) à g), écris la probabilité avec la notation $P(\ldots \mid \ldots)$ et dis si elle se lit sur une ligne, une colonne, une marge ou la diagonale. Un opérateur qui reçoit une alerte de la caméra doit-il croire qu'il y a un défaut ?

### Ex M03.5 — F-beta : quel β pour quel coût d'erreur ? ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des F-beta, relier $\beta$ au poids du recall, et comparer deux modèles selon le $\beta$ choisi.
**Prérequis :** fiche §5 ; R1 (moyenne harmonique) · **Parcours :** C

Un modèle A de détection d'intrusion a une precision de 0,6 et un recall de 0,9 (sur un jeu de test : 45 vrais positifs, 30 faux positifs, 5 faux négatifs).

| | Question | Réponse attendue |
|---|---|---|
| a | le $F_1$ du modèle A | un nombre (4 décimales) |
| b | son $F_2$ | un nombre (4 décimales) |
| c | son $F_{0{,}5}$ | un nombre (4 décimales) |
| d | la valeur de $\beta$ pour laquelle, au dénominateur de $F_\beta$ écrit avec les comptages, un faux négatif compte 9 fois plus qu'un faux positif | un entier |
| e | le poids du recall dans $\frac{1}{F_\beta}$ quand $\beta = 2$ | un nombre (2 décimales) |
| f | la limite de $F_\beta$ du modèle A quand $\beta \to +\infty$ | un nombre (2 décimales) |
| g | un modèle B a une precision de 0,9 et un recall de 0,6 : son $F_2$ | un nombre (4 décimales) |
| h | pour l'équipe sécurité, laisser passer une intrusion coûte beaucoup plus cher qu'une fausse alerte : le modèle à préférer | une lettre entre guillemets (A ou B) |

Dans ta copie : retrouve a) et b) avec les comptages, par la formule $\frac{(1 + \beta^2)\,TP}{(1 + \beta^2)\,TP + \beta^2\,FN + FP}$. Compare g) et c) : pourquoi sont-ils égaux ? Les deux modèles ont-ils le même $F_1$ ?

### Ex M03.6 — Balanced accuracy et MCC sur un problème déséquilibré ✏️ ★★ ⏱️ 20 min
**Objectif :** voir pourquoi l'accuracy trompe quand une classe est rare, et calculer la balanced accuracy et le MCC.
**Prérequis :** fiche §5 et §6 ; M02c §8 (corrélation) · **Parcours :** C

Un opérateur téléphonique veut prédire quels clients vont résilier leur abonnement le mois prochain. Sur 1 000 clients de test, 50 ont résilié (la classe positive).
- Le modèle A prédit que **personne** ne résilie.
- Le modèle B signale 120 clients, dont 35 ont vraiment résilié.

| | Question | Réponse attendue |
|---|---|---|
| a | l'accuracy du modèle A | un nombre (2 décimales) |
| b | la balanced accuracy du modèle A | un nombre (2 décimales) |
| c | l'accuracy du modèle B | un nombre (2 décimales) |
| d | le recall du modèle B | un nombre (2 décimales) |
| e | la spécificité du modèle B | un nombre (4 décimales) |
| f | la balanced accuracy du modèle B | un nombre (4 décimales) |
| g | le MCC du modèle B | un nombre (3 décimales) |
| h | la precision du modèle B | un nombre (4 décimales) |

Dans ta copie : écris les deux matrices de confusion. Pourquoi le MCC du modèle A n'est-il pas défini par la formule, et quelle valeur lui donne-t-on ? Quel modèle l'accuracy préfère-t-elle, et quel modèle préfèrent la balanced accuracy et le MCC ? Le modèle B est-il utile malgré sa precision ?

### Ex M03.7 — Changer de population : recalculer la precision quand la prévalence change ✏️ ★★ ⏱️ 20 min
**Objectif :** recalculer la precision et les autres mesures d'un même modèle pour une autre prévalence, et trouver ce qu'il faudrait changer pour garder une bonne precision.
**Prérequis :** fiche §3, §4 et §6 · **Parcours :** C, E

Un modèle détecte les comptes piratés d'un réseau social. Il a été évalué sur un jeu de test où 20 % des comptes étaient piratés : son recall vaut 0,9 et sa spécificité 0,98. On le déploie sur l'ensemble des comptes, où 2 % seulement sont piratés. Le recall et la spécificité ne changent pas.

| | Question | Réponse attendue |
|---|---|---|
| a | la precision sur le jeu de test (prévalence 20 %) | un nombre (4 décimales) |
| b | la precision en production (prévalence 2 %) | un nombre (4 décimales) |
| c | en production, sur 10 000 comptes : le nombre moyen de vrais positifs | un entier |
| d | sur ces 10 000 comptes : le nombre moyen de faux positifs | un entier |
| e | en production : la valeur prédictive négative | un nombre (3 décimales) |
| f | en production : l'accuracy | un nombre (4 décimales) |
| g | la prévalence à partir de laquelle la precision atteint 0,8 (même recall, même spécificité) | un nombre (4 décimales) |
| h | à la prévalence de 2 %, la spécificité qu'il faudrait pour une precision de 0,8 (même recall) | un nombre (4 décimales) |

Dans ta copie : retrouve b) par la formule de la fiche (§6), puis par le tableau des 10 000 comptes. Pourquoi l'accuracy f) est-elle si haute alors que la moitié des alertes sont fausses ? Que proposerais-tu à l'équipe qui traite les alertes ?

### Ex M03.8 — Une courbe ROC à la main, et son aire par les trapèzes ✏️ ★★ ⏱️ 20 min
**Objectif :** construire point par point la courbe ROC de dix scores, et calculer son aire.
**Prérequis :** fiche §7 ; M02a §5 (méthode des trapèzes) · **Parcours :** C, E

Un modèle prédit si un utilisateur va cliquer sur une publicité. Ses scores pour 10 utilisateurs :
- les 5 qui ont cliqué (positifs) : $0{,}92$ ; $0{,}85$ ; $0{,}64$ ; $0{,}55$ ; $0{,}30$ ;
- les 5 qui n'ont pas cliqué (négatifs) : $0{,}78$ ; $0{,}47$ ; $0{,}40$ ; $0{,}22$ ; $0{,}15$.

On déclare positif un utilisateur dont le score est **supérieur ou égal** au seuil.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de points de la courbe ROC en escalier : un point par score pris comme seuil, plus le point de départ $(0, 0)$ (les points intermédiaires d'une même marche comptent) | un entier |
| b | le point de la courbe pour le seuil 0,6 : `[FPR, recall]` | une liste de 2 nombres (2 décimales) |
| c | le point pour le seuil 0,45 | une liste de 2 nombres (2 décimales) |
| d | l'AUC, par la méthode des trapèzes | un nombre (2 décimales) |
| e | le plus grand recall atteint avec un taux de faux positifs nul | un nombre (2 décimales) |
| f | le plus petit taux de faux positifs qui permet un recall de 1 | un nombre (2 décimales) |
| g | l'AUC si l'on ajoute un onzième utilisateur, négatif, de score 0,95 | un nombre (4 décimales) |
| h | l'AUC des 10 utilisateurs de départ si le positif de score 0,30 avait eu le score 0,50 | un nombre (2 décimales) |

Dans ta copie : trie les dix scores, trace la courbe sur un quadrillage de $5 \times 5$ cases, et colorie les cases sous la courbe. Combien y en a-t-il ? Explique g) et h) en comptant les cases.

### Ex M03.9 — L'AUC comme proportion de paires bien classées ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une AUC en comptant les paires, ex æquo compris, et prévoir l'effet d'un changement de scores.
**Prérequis :** fiche §7 · **Parcours :** C, E

Un modèle trie des candidatures ; ses scores (arrondis à 0,1) :
- les 4 candidatures retenues ensuite par un recruteur (positives) : $0{,}9$ ; $0{,}7$ ; $0{,}7$ ; $0{,}4$ ;
- les 3 candidatures écartées (négatives) : $0{,}7$ ; $0{,}5$ ; $0{,}2$.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de paires (positif, négatif) | un entier |
| b | le nombre de paires (positif, négatif) ex æquo | un entier |
| c | le nombre de paires où le positif a **strictement** le score le plus élevé | un entier |
| d | l'AUC | un nombre (2 décimales) |
| e | l'AUC si l'on remplace chaque score $s$ par $-s$ | un nombre (2 décimales) |
| f | l'AUC si l'on ajoute une cinquième candidature positive, de score 0,6 | un nombre (4 décimales) |
| g | la proportion des paires de départ où le négatif a strictement le score le plus élevé | un nombre (4 décimales) |

Dans ta copie : écris le tableau des 12 paires (une ligne par positif, une colonne par négatif) avec 1, $\frac{1}{2}$ ou 0 dans chaque case. Vérifie que d), c), b) et g) sont liés par une relation simple. Trace la courbe ROC : où se trouve le segment oblique dû aux ex æquo, et quelle aire a-t-il sous lui ?

### Ex M03.10 — Courbe precision-recall et average precision à la main ✏️ ★★ ⏱️ 20 min
**Objectif :** construire les points d'une courbe precision-recall, calculer l'average precision, et trouver le seuil du meilleur F1.
**Prérequis :** fiche §5 et §7 · **Parcours :** C

Un système de recommandation propose 7 films à un utilisateur, triés par score. Après les avoir vus, l'utilisateur dit s'il les a aimés (+) ou non (−) :

| score | 0,9 | 0,8 | 0,75 | 0,6 | 0,5 | 0,3 | 0,2 |
|---|---|---|---|---|---|---|---|
| aimé | + | − | + | − | + | − | − |

On recommande un film dont le score est supérieur ou égal au seuil.

| | Question | Réponse attendue |
|---|---|---|
| a | au seuil 0,75 : `[precision, recall]` | une liste de 2 nombres (4 décimales) |
| b | au seuil 0,5 : `[precision, recall]` | une liste de 2 nombres (4 décimales) |
| c | la precision d'un classement au hasard, c'est-à-dire la prévalence | une fraction irréductible |
| d | l'average precision | un nombre (4 décimales) |
| e | l'average precision, en fraction | une fraction irréductible |
| f | le plus grand F1 sur tous les seuils | un nombre (2 décimales) |
| g | le seuil, parmi les 7 scores pris comme seuils, qui donne ce F1 | un nombre (2 décimales) |
| h | l'average precision si le film non aimé de score 0,8 avait eu le score 0,4 | un nombre (4 décimales) |

Dans ta copie : écris le tableau (seuil, TP, FP, precision, recall, F1) pour les 7 seuils, puis trace la courbe precision-recall. Pourquoi la precision monte-t-elle parfois quand on baisse le seuil, alors que le recall ne diminue jamais ?

### Ex M03.11 — Score de Brier et calibration de huit prévisions ✏️ ★ ⏱️ 15 min
**Objectif :** calculer un score de Brier, le comparer à des prévisions constantes, et juger la calibration par paquets.
**Prérequis :** fiche §8 · **Parcours :** C

Un transporteur annonce, pour 8 colis, la probabilité qu'ils arrivent en retard ; puis il note ce qui s'est passé (1 = en retard) :

| colis | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| probabilité annoncée $p_i$ | 0,9 | 0,8 | 0,7 | 0,6 | 0,4 | 0,3 | 0,2 | 0,1 |
| retard $y_i$ | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |

| | Question | Réponse attendue |
|---|---|---|
| a | le score de Brier des prévisions | un nombre (3 décimales) |
| b | le score de Brier d'une prévision constante de 0,5 | un nombre (3 décimales) |
| c | le score de Brier d'une prévision constante égale à la proportion de colis en retard | un nombre (3 décimales) |
| d | dans le paquet des probabilités annoncées d'au moins 0,5 : la probabilité moyenne annoncée | un nombre (2 décimales) |
| e | dans ce paquet : la fréquence observée des retards | un nombre (2 décimales) |
| f | dans le paquet des probabilités inférieures à 0,5 : la probabilité moyenne annoncée | un nombre (2 décimales) |
| g | dans ce paquet : la fréquence observée des retards | un nombre (2 décimales) |
| h | la plus grande contribution $(p_i - y_i)^2$ d'un seul colis | un nombre (2 décimales) |

Dans ta copie : place les deux paquets sur un diagramme de fiabilité. Ces prévisions semblent-elles calibrées ? Quel colis coûte le plus au score, et pourquoi ? Huit colis suffisent-ils pour juger la calibration ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex M03.12 — L'aire sous la courbe ROC compte les paires bien classées ∂ ★★★ ⏱️ 30 min
**Objectif :** démontrer que l'aire sous la courbe ROC est la proportion des paires (positif, négatif) bien classées, ex æquo comptés pour moitié.
**Prérequis :** fiche §7 ; R4 (Σ) ; M02a §5 · **Parcours :** C

Un classifieur donne des scores à $n_+$ exemples positifs, de scores $s_1, \ldots, s_{n_+}$, et à $n_-$ exemples négatifs, de scores $t_1, \ldots, t_{n_-}$. Pour un seuil $\theta$, on déclare positif tout exemple de score $\ge \theta$ ; la courbe ROC relie, pour des seuils décroissants, les points $\big(\text{FPR}(\theta), \text{TPR}(\theta)\big)$, de $(0, 0)$ à $(1, 1)$. On note $\text{TPR}(\theta) = \frac{1}{n_+}\#\{i : s_i \ge \theta\}$ et $\text{FPR}(\theta) = \frac{1}{n_-}\#\{j : t_j \ge \theta\}$.
1. On suppose d'abord tous les scores **différents**. On fait descendre le seuil d'un score à l'autre. Montre que la courbe avance par pas verticaux de $\frac{1}{n_+}$ (quand le seuil passe un positif) et par pas horizontaux de $\frac{1}{n_-}$ (quand il passe un négatif). Pourquoi la courbe est-elle un escalier qui ne redescend jamais ?
2. Montre que l'aire sous cet escalier est la somme, sur les négatifs $j$, de $\frac{1}{n_-}$ fois la hauteur de la courbe au moment où le seuil passe $t_j$.
3. Que vaut cette hauteur ? Écris-la à l'aide de $\#\{i : s_i > t_j\}$.
4. Déduis-en que l'aire vaut $\frac{1}{n_+ n_-}\sum_{j}\#\{i : s_i > t_j\}$, la proportion des paires (positif, négatif) bien classées.
5. On autorise maintenant des ex æquo. Un groupe de scores égaux contient $a$ positifs et $b$ négatifs ($a, b \ge 1$) : montre que la courbe y suit la diagonale du rectangle qu'elle traverse, et que l'aire sous ce segment, dans le rectangle de $a \times b$ cases de taille $\frac{1}{n_+} \times \frac{1}{n_-}$ qu'il traverse, vaut la moitié du rectangle. Conclus que chaque paire ex æquo compte pour $\frac{1}{2}$.
6. Déduis-en que l'AUC ne change pas si l'on remplace chaque score $s$ par $f(s)$, pour une fonction $f$ strictement croissante. Que devient-elle pour une fonction strictement décroissante ?
7. Pour aller plus loin : la statistique $U$ de Mann et Whitney (un test de comparaison de deux groupes) compte les paires où un élément du premier groupe dépasse un élément du second, ex æquo comptés pour moitié. Relie $U$ à l'AUC.

### Ex M03.13 — En multiclasse, micro-precision, micro-recall et accuracy sont égaux ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer qu'en classification multiclasse (un seul label par exemple) les moyennes micro de la precision et du recall valent l'accuracy, et voir quand ce n'est plus vrai.
**Prérequis :** fiche §4 et §5 · **Parcours :** C

Un classifieur range $n$ exemples dans $K \ge 2$ classes. Sa matrice de confusion $C$ est un tableau $K \times K$ : $C_{kl}$ est le nombre d'exemples de vraie classe $k$ prédits dans la classe $l$. Pour chaque classe $k$, prise comme classe positive face aux autres : $TP_k = C_{kk}$, $FP_k = \sum_{l \ne k} C_{lk}$ (sa colonne, hors diagonale) et $FN_k = \sum_{l \ne k} C_{kl}$ (sa ligne, hors diagonale). La micro-precision vaut $\frac{\sum_k TP_k}{\sum_k (TP_k + FP_k)}$ et le micro-recall $\frac{\sum_k TP_k}{\sum_k (TP_k + FN_k)}$.
1. Exprime $\sum_k TP_k$ à l'aide de la diagonale de $C$, puis l'accuracy à l'aide de $C$ et de $n$.
2. Montre que $\sum_k FP_k$ est la somme des cases hors de la diagonale. Fais de même pour $\sum_k FN_k$.
3. Déduis-en que la micro-precision, le micro-recall et le micro-F1 sont égaux à l'accuracy.
4. Interprète l'étape 2 en une phrase : que représente une case hors de la diagonale pour la classe prédite, et pour la vraie classe ?
5. Vérifie le résultat sur la matrice des feuilles de vigne de la fiche (§5).
6. En classification binaire, scikit-learn ne calcule par défaut la precision et le recall que pour la classe positive (`average="binary"`). Pourquoi ne sont-ils en général ni égaux entre eux, ni égaux à l'accuracy ? Et dans un problème **multi-label** (un exemple peut avoir plusieurs labels, ou aucun), quelle étape de la démonstration tombe ?
7. En binaire, montre que le recall macro (la moyenne simple des recalls des deux classes) vaut $\frac{\text{recall} + \text{spécificité}}{2}$, et donne un exemple de matrice $2 \times 2$ où il diffère de l'accuracy. Quand sont-ils égaux ?

<a id="reflexion"></a>

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M03.14 — Un seuil sur un score : trois seuils, trois matrices de confusion 🔗 ★ ⏱️ 20 min
**Objectif :** construire les matrices de confusion de plusieurs seuils, et choisir un seuil selon le F1 ou selon le coût des erreurs.
**Prérequis :** fiche §4 à §6 · **Parcours :** C, E

Dans un entrepôt, un modèle signale les colis dont l'adresse semble fausse, pour qu'un employé les vérifie avant l'envoi. Ses scores sur 10 colis de test :
- 5 mal adressés (positifs) : $0{,}95$ ; $0{,}81$ ; $0{,}66$ ; $0{,}52$ ; $0{,}38$ ;
- 5 bien adressés (négatifs) : $0{,}74$ ; $0{,}45$ ; $0{,}33$ ; $0{,}21$ ; $0{,}08$.

On déclare positif un colis dont le score est supérieur ou égal au seuil, et l'on compare les seuils 0,3, 0,5 et 0,7.

| | Question | Réponse attendue |
|---|---|---|
| a | au seuil 0,5 : le nombre de vrais positifs | un entier |
| b | au seuil 0,5 : le nombre de faux positifs | un entier |
| c | au seuil 0,7 : la precision | une fraction irréductible |
| d | au seuil 0,7 : le recall | un nombre (2 décimales) |
| e | au seuil 0,3 : `[precision, recall]` | une liste de 2 nombres (3 décimales) |
| f | le seuil, parmi 0,3, 0,5 et 0,7, qui donne le meilleur F1 | un nombre (1 décimale) |
| g | un colis mal adressé envoyé (un faux négatif) coûte 3, et la vérification d'un colis bien adressé (un faux positif) coûte 1 ; un colis mal adressé détecté ne coûte rien : le coût total au seuil 0,5 | un entier |
| h | avec ces coûts, le seuil le moins coûteux parmi les trois | un nombre (1 décimale) |

Dans ta copie : écris les trois matrices de confusion. Comment évoluent la precision et le recall quand le seuil baisse ? Avec un coût de 1 pour chaque erreur, quel seuil choisirais-tu ? Pourquoi ne faudrait-il pas choisir le seuil sur ces mêmes 10 colis de test ?

### Ex M03.15 — Équité : les taux de faux positifs de deux groupes 🔗 ★★ ⏱️ 15 min
**Objectif :** calculer des mesures par groupe, et vérifier l'identité qui empêche d'égaliser à la fois les taux d'erreur et les precisions.
**Prérequis :** fiche §4 et §8 · **Parcours :** C

Un réseau social utilise un modèle pour signaler les comptes automatisés (des robots qui se font passer pour des personnes). On l'évalue sur 200 comptes de chacun de deux groupes, selon la langue des utilisateurs :

| | TP | FN | FP | TN |
|---|---|---|---|---|
| groupe A | 48 | 12 | 28 | 112 |
| groupe B | 16 | 4 | 18 | 162 |

| | Question | Réponse attendue |
|---|---|---|
| a | le taux de faux positifs du groupe A | un nombre (2 décimales) |
| b | le taux de faux positifs du groupe B | un nombre (2 décimales) |
| c | le recall du groupe B | un nombre (2 décimales) |
| d | la precision du groupe A | un nombre (4 décimales) |
| e | la precision du groupe B | un nombre (4 décimales) |
| f | la part des comptes du groupe A qui sont signalés | un nombre (2 décimales) |
| g | le modèle a-t-il le même recall **et** le même taux de faux positifs dans les deux groupes ? | `True` ou `False` |
| h | le taux de faux positifs qu'il faudrait dans le groupe B, avec le même recall, pour que sa precision égale celle du groupe A | un nombre (4 décimales) |

Dans ta copie : vérifie l'identité de la fiche (§8) pour chaque groupe. Une personne du groupe A a-t-elle plus de risques d'être signalée à tort comme un robot qu'une personne du groupe B ? Une alerte vaut-elle autant dans les deux groupes ? Quel critère d'équité choisirais-tu ici, et que coûterait-il ?

### Ex M03.16 — MML §6.3 : règle de la somme, règle du produit et vocabulaire, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais les deux règles de calcul des probabilités, dans leur forme générale, et les relier aux tableaux de la fiche.
**Prérequis :** fiche §1 à §3 ; M02b §5 · **Parcours :** C

Lis MML §6.3, jusqu'à la règle du produit comprise (la suite, sur le théorème de Bayes, est pour M04). Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Comment le livre écrit-il la règle de la somme pour une variable discrète, puis pour une variable continue ? Quel autre nom donne-t-il au résultat ?
2. Le livre fait une remarque sur le **coût de calcul** de la règle de la somme quand il y a beaucoup de variables. Laquelle ? Pour 30 variables binaires, combien de termes contiendrait la somme qui donne la loi marginale d'une seule d'entre elles ?
3. Comment le livre écrit-il la règle du produit ? Pourquoi dit-il qu'elle peut s'écrire de deux façons ?
4. Le livre utilise la même lettre $p$ pour des choses de natures différentes. Lesquelles ? Que devient $p(x, y)$ pour deux variables discrètes, et pour deux variables continues ?
5. Applique la règle de la somme et la règle du produit au tableau des 500 utilisateurs de la fiche (§1) : retrouve $P(\text{premium})$, puis $P(\text{mobile} \cap \text{premium})$ à partir de $P(\text{premium} \mid \text{mobile})$.
6. Écris la règle du produit pour trois variables, $p(x, y, z)$, de deux façons différentes.
7. Note trois mots ou tournures en anglais de cette section qui étaient nouveaux pour toi, avec leur traduction.

### Ex M03.17 — Un taux de réussite trompeur : le paradoxe de Simpson ⚖️ ★★ ⏱️ 20 min
**Objectif :** reconnaître un paradoxe de Simpson dans des chiffres de recrutement, et dire quelle comparaison répond à quelle question.
**Prérequis :** fiche §2 et §3 · **Parcours :** C

Une entreprise publie les taux d'embauche de ses deux départements, pour les candidatures de l'année (chiffres inventés) :

| | Produit | Recherche | **total** |
|---|---|---|---|
| **femmes** | 45 embauchées sur 60 | 28 sur 140 | 73 sur 200 |
| **hommes** | 98 sur 140 | 9 sur 60 | 107 sur 200 |

Réponds dans ta copie, en une quinzaine de lignes :
1. Calcule les taux d'embauche des femmes et des hommes dans chaque département, puis au total. Que constates-tu ?
2. Explique l'inversion avec la formule des probabilités totales : par quels poids chaque taux global est-il une moyenne ?
3. Un journal titre « L'entreprise embauche bien moins les femmes ». Un autre, « Dans chaque département, les femmes sont plus souvent embauchées ». Les deux ont-ils raison ? Quelle comparaison répond à la question « les recruteurs de chaque département traitent-ils les femmes équitablement ? »
4. Supposons maintenant que beaucoup de femmes ne postulent pas au département Produit parce que ses offres sont rédigées pour décourager leur candidature. Le chiffre global redevient-il pertinent ? Pour quelle question ?
5. Un modèle de tri des candidatures est entraîné sur ces données, avec le sexe parmi ses entrées mais **sans** le département. Que risque-t-il d'apprendre ? Et avec le département, mais sans le sexe ?
6. Cherche le cas des admissions à l'université de Berkeley en 1973 (P. Bickel et ses coauteurs, *Science*, 1975) : en quoi ressemble-t-il à cet exercice ?

### Ex M03.18 — Expliquer pourquoi P(A sachant B) n'est pas P(B sachant A) 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement, avec un tableau, l'erreur qui confond une probabilité conditionnelle et sa « réciproque ».
**Prérequis :** fiche §2 · **Parcours :** C, E

Une collègue présente une analyse des désabonnements d'une application : « 95 % des utilisateurs qui se sont désabonnés ouvraient l'application moins d'une fois par semaine. Donc un utilisateur qui l'ouvre moins d'une fois par semaine a 95 % de risques de se désabonner : envoyons-lui une promotion. »

Réponds-lui **en huit lignes au plus**, sans formule compliquée. Ta réponse doit écrire les deux probabilités avec le mot « sachant », montrer sur un petit tableau de 1 000 utilisateurs (que tu inventes) que la seconde peut être bien plus petite que 95 %, et dire quelles informations manquent pour la calculer.

<a id="entretien"></a>

## 💼 Entretien

### M03.E1 — Une variable indépendante de la cible peut-elle aider un modèle ? 💼 ★ ⏱️ 10 min
*Fiche §2 · parcours C*

« Pour simplifier notre modèle, nous avons supprimé toutes les features indépendantes de la cible : chacune, prise seule, ne change rien à la probabilité de la classe. C'est sans risque, non ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit répondre par oui ou par non, donner un exemple précis de deux variables, chacune indépendante de la cible, qui la déterminent ensemble, relier cet exemple à l'indépendance deux à deux de la fiche (§2), et dire comment tester une feature autrement que seule. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m03_probabilites_conditionnelles/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M03.19 | Jointe, marginales et conditionnelles à partir d'un tableau de comptages · `joint_from_counts, marginal, conditional` | 🔨 | ★ | 20 | C, E |
| M03.20 | Tester l'indépendance avec une tolérance · `are_independent` | 🔨 | ★ | 15 | C |
| M03.21 | L'AUC en comptant les paires · `auc_by_pairs` | 🔨 | ★★ | 20 | C, E |
| M03.22 | `sklearn.metrics.roc_auc_score` contre le comptage des paires, ex æquo compris | 📦 | ★ | 15 | C |
| M03.23 | Prédire : l'AUC après une transformation croissante des scores | 🔮 | ★ | 10 | C, E |
| M03.24 | Simuler pour estimer une probabilité conditionnelle | 🔬 | ★★ | 20 | C |
| M03.25 | La courbe ROC en escalier : une marche par paire | 🎨 | ★ | 20 | C |
| M03.26 | Chasse à l'erreur : conditionnelle inversée, marginale oubliée | 🐛 | ★ | 15 | C |
| M03.27 | Une fonction qui refuse un tableau invalide (`ValueError`) | 🛠️ | ★ | 10 | C |
| M03.28 | Défi : retrouver un tableau de contingence à partir de quelques probabilités | 🏆 | ★★★ | 25 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
