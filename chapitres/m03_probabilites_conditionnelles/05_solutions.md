# M03 · Probabilités conditionnelles — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M03.Q1 — Jointe, marginale ou conditionnelle ?
1. **Jointe** : $P(\text{ouvert} \cap \text{clic}) = 0{,}04$.
2. **Conditionnelle** : $P(\text{clic} \mid \text{ouvert}) = 0{,}16$.
3. **Marginale** : $P(\text{ouvert}) = 0{,}25$.
4. **Conditionnelle** : $P(\text{ouvert} \mid \text{clic}) = 1$.
5. Tout clic suit une ouverture, donc $\{\text{clic}\} = \{\text{clic}\} \cap \{\text{ouvert}\}$ et $P(\text{clic}) = 0{,}04$. Cohérentes : $P(\text{clic} \mid \text{ouvert})\,P(\text{ouvert}) = 0{,}16 \times 0{,}25 = 0{,}04$, la règle du produit.
6. **Faux** : c'est la somme sur toutes les valeurs $y$, à $x$ **fixé**, qui vaut 1 (une ligne de lois conditionnelles). Pour $y$ fixé, la somme sur $x$ n'a pas de raison de valoir 1 (0,1 + 0,25 = 0,35 pour « premium » dans la fiche).

### M03.Q2 — P(A sachant B) et P(B sachant A)
1. Règle du produit : $P(\text{technique} \cap \text{formation}) = P(\text{technique} \mid \text{formation})\,P(\text{formation}) = 0{,}8 \times 0{,}25 = $ **0,2**.
2. $P(\text{formation} \mid \text{technique}) = \frac{0{,}2}{0{,}4} = $ **0,5**.
3. **Faux** : $P(B \mid A) = P(A \mid B)\,\frac{P(B)}{P(A)}$ peut être minuscule si $B$ est rare et $A$ fréquent.
4. **Vrai** : sachant $B$, $A$ et « non $A$ » se partagent tout l'univers restreint.
5. **Faux** : les deux probabilités ont des conditions différentes. Exemple : $A$ certain donne $1 + 1 = 2$.
6. $0{,}4 \times 0{,}05 = $ **0,02**, soit 2 % des pièces (règle du produit).

### M03.Q3 — Indépendants ou incompatibles ?
1. **Indépendants** : $P(A \cap B) = P(\{2\}) = \frac{1}{6}$ et $P(A)\,P(B) = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$.
2. **Incompatibles** (aucun nombre pair n'est 1 ou 3), donc **dépendants** : $P(A \cap C) = 0 \ne \frac{1}{2} \times \frac{1}{3}$.
3. **Indépendants** : $0{,}3 \times 0{,}5 = 0{,}15$.
4. **Faux** : $P(A \cap B) = 0$, alors que $P(A)\,P(B) > 0$.
5. **Vrai** : $P(E \cap \text{non } F) = P(E) - P(E \cap F) = P(E) - P(E)P(F) = P(E)\,(1 - P(F))$.
6. **Faux** : l'exemple des deux pièces de la fiche (§2) : « première pile », « seconde pile », « même côté ».

### M03.Q4 — Quelle métrique pour quelle probabilité ?
1. Le **recall** (sensibilité, taux de vrais positifs).
2. La **precision** (valeur prédictive positive).
3. La **spécificité**.
4. Le **taux de faux positifs** (FPR), $1 - $ spécificité.
5. L'**accuracy**.
6. Le **recall**, la **spécificité** et le **taux de faux positifs** : ils conditionnent par la vérité. La precision et l'accuracy changent (fiche §6).

### M03.Q5 — Moyennes de métriques
1. $\frac{2 \times 0{,}5 \times 1}{1{,}5} = \frac{2}{3} \approx$ **0,667**.
2. **Faux** : $\beta = 2$ donne au recall le poids $\frac{4}{5}$.
3. $\frac{0{,}9 + 0{,}6 + 0{,}3}{3} = $ **0,6**.
4. **Vrai** (fiche §5, et M03.13).
5. **0**, par convention : une colonne de la matrice est vide, le dénominateur de la formule est nul, et la prédiction n'a aucun lien avec la vérité.
6. **Vrai** : la moyenne macro est une moyenne simple des classes.

### M03.Q6 — ROC et AUC : vrai ou faux
1. **Faux** : une AUC de 0,5 dit que le **classement** n'est pas meilleur que le hasard ; elle ne donne pas de taux d'erreur, qui dépend d'un seuil.
2. **Vrai** : multiplier par 2 garde l'ordre des scores.
3. **Vrai** : un recall de 1 sans aucun faux positif.
4. **Faux** : en inversant les scores ($1 - s$), on obtient une AUC de 0,8 ; le modèle classe bien, à l'envers.
5. **Faux** : les deux taux de la courbe conditionnent par la vérité.
6. **Faux** : l'AUC ne dépend que de l'ordre ; la precision au seuil 0,5 dépend des valeurs des scores et de la prévalence.

### M03.Q7 — Calibré ou pas ?
1. À ce niveau de probabilité, il est **calibré** : $P(\text{panne} \mid \text{annonce } 0{,}7) \approx 0{,}7$. Il faut le vérifier aux autres niveaux, et avec assez de jours.
2. **Calibré** (il annonce $\pi$, et une proportion $\pi$ des cas est positive) ; son AUC vaut **0,5** (tous les scores sont ex æquo).
3. **Faux** : l'AUC ne voit que l'ordre ; un modèle qui annonce $\frac{s}{10}$ au lieu de $s$ garde la même AUC et n'est plus calibré.
4. **0**.
5. **0,25** : chaque terme vaut $(0{,}5 - 0)^2$ ou $(0{,}5 - 1)^2$.
6. **Trop hautes** : le modèle a appris un monde à 50 % de positifs (fiche §6).

<a id="rappels"></a>

## 🔁 Rappels

### M03.R1 — Arbres pondérés (R8)
1. Premier niveau : rouge $\frac{3}{5}$, bleu $\frac{2}{5}$ ; second niveau : gagne $\frac{1}{2}$ sachant rouge, $\frac{1}{6}$ sachant bleu.
2. $\frac{3}{5} \times \frac{1}{2} = $ **0,3**.
3. $\frac{2}{5} \times \frac{1}{6} = \frac{2}{30} = $ $\frac{1}{15}$.
4. $\frac{3}{10} + \frac{1}{15} = \frac{9}{30} + \frac{2}{30} = $ $\frac{11}{30}$ (les probabilités totales).
5. $1 - \frac{11}{30} = \frac{19}{30}$.

### M03.R2 — Moyenne harmonique et moyenne pondérée (R1)
1. $\frac{2}{\frac{1}{2} + \frac{1}{6}} = \frac{2}{\frac{4}{6}} = $ **3**.
2. $\frac{2}{2 + 1} = \frac{2}{3} \approx$ **0,667**.
3. $\frac{3 \times 10 + 1 \times 20}{4} = $ **12,5**.
4. Harmonique $\frac{2 \times 0{,}9 \times 0{,}1}{1} = $ **0,18** ; arithmétique **0,5**. La moyenne harmonique reste près du plus petit nombre.
5. $\frac{1}{\frac{1}{5} \times 2 + \frac{4}{5} \times 1} = \frac{1}{1{,}2} = \frac{5}{6} \approx$ **0,833**.

### M03.R3 — Aire par la méthode des trapèzes (M02a)
1. $0{,}5 \times \frac{0{,}4 + 0{,}8}{2} = $ **0,3**.
2. $0{,}5 \times \frac{0 + 0{,}6}{2} + 0{,}5 \times \frac{0{,}6 + 1}{2} = 0{,}15 + 0{,}4 = $ **0,55**.
3. $0{,}5 \times \frac{0 + 0{,}25}{2} + 0{,}5 \times \frac{0{,}25 + 1}{2} = 0{,}0625 + 0{,}3125 = $ **0,375**, pour une valeur exacte de $\frac{1}{3}$ : erreur $\approx 0{,}042$ (par excès, la courbe étant convexe).
4. Deux paliers : $0{,}5 \times 0{,}5 + 0{,}5 \times 1 = $ **0,75**.
5. Il a une largeur nulle : son « trapèze » a une aire nulle.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M03.1 — Un tableau de contingence : jointes, marginales, conditionnelles

**Réponses** : a) `0.3` · b) `0.55` · c) `0.175` · d) `0.583` · e) `0.318` · f) `0.375` · g) `[0.25, 0.167, 0.583]` · h) `0.425`.

**Démarche.** Les totaux : lignes 80, 100, 220 ; colonnes 120 (avec photo) et 280 (sans photo) ; total 400.
- a) $\frac{120}{400}$. b) $\frac{220}{400}$. c) Une case divisée par le total : $\frac{70}{400}$.
- d) On ne garde que les 120 avis avec photo : $\frac{70}{120} \approx 0{,}583$.
- e) On ne garde que les 220 avis de 4 ou 5 étoiles : $\frac{70}{220} \approx 0{,}318$.
- f) $\frac{30}{80} = 0{,}375$.
- g) La colonne « avec photo » divisée par son total : $\frac{30}{120}, \frac{20}{120}, \frac{70}{120}$, de somme 1.
- h) $P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{80 + 120 - 30}{400}$.

Pour la copie : $P(\text{photo} \mid \text{1 ou 2}) = 0{,}375 \ne P(\text{photo}) = 0{,}3$ : la photo n'est pas indépendante de la note. Les avis très négatifs ont plus souvent une photo (pour montrer le défaut ?), et les avis de 3 étoiles moins souvent (0,2).

**Erreurs fréquentes.** Échanger d) et e) (le « sachant » dit le dénominateur) ; diviser une conditionnelle par 400 ; oublier de retirer l'intersection en h) (0,5).

**Variante.** $P(\text{3 étoiles} \mid \text{sans photo})$ ? *Réponse* : $\frac{80}{280} \approx 0{,}286$.

### Ex M03.2 — L'indépendance, vérifiée dans un tableau

**Réponses** : a) `0.08` · b) `0.08` · c) `True` · d) `0.18` · e) `0.072` · f) `0.06` · g) `False` · h) `54`.

**Démarche.**
- a) $\frac{48 + 32}{1000}$. b) $\frac{32}{400}$. c) $P(\text{clic} \mid A) = \frac{48}{600} = 0{,}08$ aussi : les deux versions ont le même taux de clic, égal au taux global. Par le produit : $P(A) \times P(\text{clic}) = 0{,}6 \times 0{,}08 = 0{,}048 = \frac{48}{1000}$, et de même pour toutes les cases.
- d) $\frac{30 + 60}{500}$. e) $P(\text{matin}) = \frac{200}{500} = 0{,}4$ et $0{,}4 \times 0{,}18 = 0{,}072$. f) $\frac{30}{500}$.
- g) $0{,}06 \ne 0{,}072$ : dépendants ; d'ailleurs $P(\text{achat} \mid \text{matin}) = 0{,}15$ et $P(\text{achat} \mid \text{soir}) = 0{,}2$.
- h) $\frac{300 \times 90}{500} = 54$ (on observe 60).

Pour la copie : le tableau attendu du tableau 2 est $\begin{pmatrix} 36 & 164 \\ 54 & 246 \end{pmatrix}$. La version B fait exactement aussi bien que la version A : elle ne gagne ni ne perd de clics. (Avec des données réelles, une égalité exacte est rare ; il faudrait un test statistique pour juger un petit écart.)

**Erreurs fréquentes.** Diviser par le total de la colonne en b) ($\frac{32}{80} = 0{,}4$) ; conclure à l'indépendance sur une seule case calculée de travers ; donner en h) l'effectif observé.

**Variante.** Dans le tableau 2, $P(\text{soir} \mid \text{achat})$ ? *Réponse* : $\frac{60}{90} \approx 0{,}667$, contre $P(\text{soir}) = 0{,}6$.

### Ex M03.3 — Probabilités totales avec trois cas

**Réponses** : a) `0.0195` · b) `0.008` · c) `0.9805` · d) `195` · e) `0.41` · f) `0.0155` · g) `0.0175` · h) `45`.

**Démarche.**
- a) $0{,}45 \times 0{,}01 + 0{,}35 \times 0{,}02 + 0{,}2 \times 0{,}04 = 0{,}0045 + 0{,}007 + 0{,}008 = 0{,}0195$.
- b) $P(S_3 \cap E) = P(E \mid S_3)\,P(S_3) = 0{,}04 \times 0{,}2$. c) $1 - 0{,}0195$. d) $0{,}0195 \times 10\,000$.
- e) $P(S_3 \mid E) = \frac{P(S_3 \cap E)}{P(E)} = \frac{0{,}008}{0{,}0195} \approx 0{,}41$.
- f) $0{,}0045 + 0{,}007 + 0{,}2 \times 0{,}02 = 0{,}0155$. g) Parts 45 %, 45 %, 10 % : $0{,}0045 + 0{,}009 + 0{,}004 = 0{,}0175$.
- h) $0{,}0045 \times 10\,000$.

Pour la copie : a) est une moyenne des taux pondérée par les parts ; le serveur le moins fiable ne traite que 20 % du trafic, d'où une valeur près des petits taux. e) : $S_3$ traite 20 % des requêtes mais produit 41 % des erreurs, parce que son taux d'erreur est le double ou le quadruple des autres. Réparer $S_3$ (f) fait mieux que déplacer son trafic (g).

**Erreurs fréquentes.** La moyenne simple des taux (0,0233) ; confondre $P(S_3 \mid E)$ avec $P(E \mid S_3) = 0{,}04$ ou avec $P(S_3) = 0{,}2$.

**Variante.** $P(S_1 \mid E)$ ? *Réponse* : $\frac{0{,}0045}{0{,}0195} \approx 0{,}23$.

### Ex M03.4 — Une matrice de confusion lue comme des probabilités

**Réponses** : a) `0.04` · b) `0.8` · c) `0.95` · d) `0.4` · e) `0.944` · f) `0.9913` · g) `0.08` · h) `0.5333`.

**Démarche.** TP = 64, FN = 80 − 64 = 16, FP = 160 − 64 = 96, TN = 2 000 − 64 − 16 − 96 = 1 824 ; lignes 80 et 1 920, colonnes 160 et 1 840.
- a) $P(Y = 1) = \frac{80}{2000}$, une marge. b) $P(\hat{Y} = 1 \mid Y = 1) = \frac{64}{80}$, une ligne. c) $P(\hat{Y} = 0 \mid Y = 0) = \frac{1824}{1920}$, une ligne.
- d) $P(Y = 1 \mid \hat{Y} = 1) = \frac{64}{160}$, une colonne. e) $P(\hat{Y} = Y) = \frac{1888}{2000}$, la diagonale.
- f) $P(Y = 0 \mid \hat{Y} = 0) = \frac{1824}{1840}$, une colonne. g) $P(\hat{Y} = 1) = \frac{160}{2000}$, une marge.
- h) $\frac{2 \times 64}{2 \times 64 + 96 + 16} = \frac{128}{240}$.

Pour la copie : non, une alerte n'est juste que 4 fois sur 10 ; l'opérateur doit vérifier la pièce. En revanche une pièce non signalée est presque sûrement saine (99,1 %).

**Erreurs fréquentes.** Échanger recall et precision ; donner le taux de faux positifs (0,05) pour la spécificité ; faire la moyenne arithmétique pour le F1 (0,6).

**Variante.** Le taux de faux négatifs $P(\hat{Y} = 0 \mid Y = 1)$ ? *Réponse* : $\frac{16}{80} = 0{,}2$.

### Ex M03.5 — F-beta : quel β pour quel coût d'erreur ?

**Réponses** : a) `0.72` · b) `0.8182` · c) `0.6429` · d) `3` · e) `0.8` · f) `0.9` · g) `0.6429` · h) `"A"`.

**Démarche.**
- a) $\frac{2 \times 0{,}54}{1{,}5} = 0{,}72$ ; avec les comptages, $\frac{90}{90 + 5 + 30}$.
- b) $\frac{5 \times 0{,}54}{4 \times 0{,}6 + 0{,}9} = \frac{2{,}7}{3{,}3}$ ; avec les comptages, $\frac{225}{225 + 4 \times 5 + 30} = \frac{225}{275}$.
- c) $\frac{1{,}25 \times 0{,}54}{0{,}25 \times 0{,}6 + 0{,}9} = \frac{0{,}675}{1{,}05}$.
- d) Au dénominateur $(1 + \beta^2)TP + \beta^2 FN + FP$, un faux négatif pèse $\beta^2$ : $\beta^2 = 9$, $\beta = 3$.
- e) $\frac{\beta^2}{1 + \beta^2} = \frac{4}{5}$. f) Tout le poids va au recall : 0,9.
- g) $\frac{5 \times 0{,}54}{4 \times 0{,}9 + 0{,}6} = \frac{2{,}7}{4{,}2}$. h) Le $F_2$ de A (0,818) dépasse celui de B (0,643) : A, dont le recall est meilleur.

Pour la copie : échanger P et R revient à remplacer $\beta$ par $\frac{1}{\beta}$, donc $F_2(B) = F_{0{,}5}(A)$. Les deux modèles ont le même $F_1$ (0,72) : le F1 ne voit pas la différence, le choix de $\beta$ la fait.

**Erreurs fréquentes.** Utiliser $\beta$ au lieu de $\beta^2$ (0,7714 pour b) ; mettre $\beta^2$ devant le recall au dénominateur ; répondre $\beta = 9$.

**Variante.** Le $F_3$ de A ? *Réponse* : $\frac{10 \times 0{,}54}{9 \times 0{,}6 + 0{,}9} = \frac{5{,}4}{6{,}3} \approx 0{,}857$.

### Ex M03.6 — Balanced accuracy et MCC sur un problème déséquilibré

**Réponses** : a) `0.95` · b) `0.5` · c) `0.9` · d) `0.7` · e) `0.9105` · f) `0.8053` · g) `0.409` · h) `0.2917`.

**Démarche.** Modèle A : TP = 0, FN = 50, FP = 0, TN = 950. Modèle B : TP = 35, FN = 15, FP = 85, TN = 865.
- a) $\frac{950}{1000}$. b) recall 0 et spécificité 1 : $\frac{0 + 1}{2}$.
- c) $\frac{35 + 865}{1000}$. d) $\frac{35}{50}$. e) $\frac{865}{950}$. f) $\frac{0{,}7 + 0{,}9105}{2}$.
- g) $\frac{35 \times 865 - 85 \times 15}{\sqrt{120 \times 50 \times 950 \times 880}} = \frac{29\,000}{\sqrt{5{,}016 \times 10^9}} \approx \frac{29\,000}{70\,824}$.
- h) $\frac{35}{120}$.

Pour la copie : pour A, la colonne « prédit positif » est vide ($TP + FP = 0$), la formule divise par 0 ; on pose MCC = 0 (aucune corrélation entre une prédiction constante et la vérité). L'accuracy préfère A (0,95 contre 0,9) ; la balanced accuracy (0,5 contre 0,81) et le MCC (0 contre 0,41) préfèrent B. B est utile : il trouve 70 % des clients qui partent, en n'en contactant que 120 ; si une offre de fidélité coûte peu, 85 offres inutiles valent bien 35 clients peut-être retenus.

**Erreurs fréquentes.** Donner 0,95 pour la balanced accuracy de A ; calculer le recall de B avec 120 au dénominateur ; un signe faux au numérateur du MCC (0,445).

**Variante.** Le F1 de B ? *Réponse* : $\frac{70}{70 + 15 + 85} = \frac{70}{170} \approx 0{,}412$.

### Ex M03.7 — Changer de population : recalculer la precision quand la prévalence change

**Réponses** : a) `0.9184` · b) `0.4787` · c) `180` · d) `196` · e) `0.998` · f) `0.9784` · g) `0.0816` · h) `0.9954`.

**Démarche.**
- a) $\frac{0{,}9 \times 0{,}2}{0{,}9 \times 0{,}2 + 0{,}02 \times 0{,}8} = \frac{0{,}18}{0{,}196}$.
- b) $\frac{0{,}9 \times 0{,}02}{0{,}9 \times 0{,}02 + 0{,}02 \times 0{,}98} = \frac{0{,}018}{0{,}0376}$.
- c) 200 comptes piratés, $0{,}9 \times 200 = 180$. d) 9 800 comptes sains, $0{,}02 \times 9\,800 = 196$.
- e) TN $= 0{,}98 \times 9\,800 = 9\,604$, FN $= 20$ : $\frac{9604}{9624} \approx 0{,}998$. f) $\frac{180 + 9604}{10\,000}$.
- g) $\frac{0{,}9\pi}{0{,}9\pi + 0{,}02(1 - \pi)} = 0{,}8 \iff 0{,}18\pi = 0{,}016(1 - \pi) \iff \pi = \frac{0{,}016}{0{,}196} \approx 0{,}0816$.
- h) Precision 0,8 avec 180 vrais positifs : $FP = 45$, donc $1 - s = \frac{45}{9800}$ et $s \approx 0{,}9954$.

Pour la copie : l'accuracy est dominée par les 9 800 comptes sains, presque tous bien classés ; elle ne dit rien de la qualité des alertes. Proposer de prioriser les alertes par score (et de choisir un seuil plus haut pour l'action automatique), ou de confirmer chaque alerte par un second signal avant d'agir ; et mesurer la precision sur des données de production, pas sur le jeu de test enrichi.

**Erreurs fréquentes.** Garder la precision du test (0,918) en production ; appliquer le recall à tous les comptes (9 000) ; calculer les faux positifs sur 10 000 comptes (200).

**Variante.** La precision à 2 % si le recall montait à 0,99 (spécificité 0,98) ? *Réponse* : $\frac{198}{198 + 196} \approx 0{,}503$ : le recall aide peu ; ce sont les faux positifs qui pèsent.

### Ex M03.8 — Une courbe ROC à la main, et son aire par les trapèzes

**Réponses** : a) `11` · b) `[0.2, 0.6]` · c) `[0.4, 0.8]` · d) `0.8` · e) `0.4` · f) `0.6` · g) `0.6667` · h) `0.88`.

**Démarche.** Triés : 0,92+, 0,85+, 0,78−, 0,64+, 0,55+, 0,47−, 0,40−, 0,30+, 0,22−, 0,15−. Les points, seuil après seuil : $(0, 0)$, $(0 ;\ 0{,}2)$, $(0 ;\ 0{,}4)$, $(0{,}2 ;\ 0{,}4)$, $(0{,}2 ;\ 0{,}6)$, $(0{,}2 ;\ 0{,}8)$, $(0{,}4 ;\ 0{,}8)$, $(0{,}6 ;\ 0{,}8)$, $(0{,}6 ; 1)$, $(0{,}8 ; 1)$, $(1, 1)$.
- a) 10 scores distincts plus $(0, 0)$ : 11 points. b) Au seuil 0,6 : 0,92, 0,85, 0,64 (3 positifs) et 0,78 (1 négatif). c) Au seuil 0,45 : 4 positifs, 2 négatifs.
- d) Les paliers horizontaux : hauteur 0,4 sur $[0 ;\ 0{,}2]$, 0,8 sur $[0{,}2 ;\ 0{,}6]$, 1 sur $[0{,}6 ; 1]$ : $0{,}08 + 0{,}32 + 0{,}4 = 0{,}8$.
- e) Avant le premier négatif : 2 positifs sur 5. f) Quand le dernier positif (0,30) passe, 3 négatifs sont déjà passés : $\frac{3}{5}$.
- g) Le nouveau négatif bat les 5 positifs : 20 paires bien classées sur 30. h) 0,50 bat maintenant 0,47 et 0,40 : 22 paires sur 25.

Pour la copie : 20 cases colorées sur 25, l'AUC. g) ajoute une colonne entière de cases au-dessus de la courbe ; h) déplace une marche, qui gagne deux cases.

**Erreurs fréquentes.** Oublier le point $(0, 0)$ ; écrire les points (recall, FPR) ; relier les points dans le désordre.

**Variante.** L'AUC si le négatif de score 0,78 avait 0,90 ? *Réponse* : il bat alors 0,85 en plus de 0,64, 0,55 et 0,30 : il reste 19 paires sur 25, 0,76.

### Ex M03.9 — L'AUC comme proportion de paires bien classées

**Réponses** : a) `12` · b) `2` · c) `8` · d) `0.75` · e) `0.25` · f) `0.7333` · g) `0.1667`.

**Démarche.** Le tableau des paires (positif en ligne, négatif en colonne : 0,7, 0,5, 0,2) :

| | 0,7 | 0,5 | 0,2 |
|---|---|---|---|
| 0,9 | 1 | 1 | 1 |
| 0,7 | ½ | 1 | 1 |
| 0,7 | ½ | 1 | 1 |
| 0,4 | 0 | 0 | 1 |

- a) $4 \times 3$. b) Les deux ½. c) 8 cases à 1. d) $\frac{8 + 2 \times \frac{1}{2}}{12} = \frac{9}{12}$.
- e) Les paires bien classées (8) deviennent mal classées et inversement (2), les ex æquo restent : $\frac{2 + 1}{12} = 0{,}25$, soit $1 - 0{,}75$.
- f) Le nouveau positif 0,6 bat 0,5 et 0,2 : $\frac{9 + 2}{15}$. g) $\frac{2}{12}$.

Pour la copie : $\text{AUC} = \frac{c}{12} + \frac{b}{24}$ et $\frac{c + b + (\text{mal classées})}{12} = 1$. La courbe : $(0, 0) \to (0 ;\ 0{,}25) \to (\frac{1}{3} ;\ 0{,}75)$ en diagonale (le seuil 0,7 fait passer deux positifs et un négatif) $\to (\frac{2}{3} ;\ 0{,}75) \to (\frac{2}{3} ; 1) \to (1, 1)$ ; le segment diagonal traverse les 2 cases ex æquo et laisse la moitié de chacune dessous.

**Erreurs fréquentes.** Compter un ex æquo pour 0 (0,667) ou pour 1 (0,833) ; oublier des paires.

**Variante.** L'AUC si le négatif de score 0,7 passait à 0,8 ? *Réponse* : plus d'ex æquo, et ce négatif n'est battu que par 0,9 : $\frac{3 + 2 + 2 + 1}{12} = \frac{8}{12} \approx 0{,}667$.

### Ex M03.10 — Courbe precision-recall et average precision à la main

**Réponses** : a) `[0.6667, 0.6667]` · b) `[0.6, 1.0]` · c) `"3/7"` · d) `0.7556` · e) `"34/45"` · f) `0.75` · g) `0.5` · h) `0.9167`.

**Démarche.** Le tableau des seuils :

| seuil | 0,9 | 0,8 | 0,75 | 0,6 | 0,5 | 0,3 | 0,2 |
|---|---|---|---|---|---|---|---|
| TP | 1 | 1 | 2 | 2 | 3 | 3 | 3 |
| FP | 0 | 1 | 1 | 2 | 2 | 3 | 4 |
| precision | 1 | 0,5 | 0,667 | 0,5 | 0,6 | 0,5 | 0,429 |
| recall | 0,333 | 0,333 | 0,667 | 0,667 | 1 | 1 | 1 |
| F1 | 0,5 | 0,4 | 0,667 | 0,571 | 0,75 | 0,667 | 0,6 |

- a), b) Lus dans le tableau. c) 3 films aimés sur 7.
- d), e) Le recall augmente aux seuils 0,9, 0,75 et 0,5, de $\frac{1}{3}$ chaque fois : $\text{AP} = \frac{1}{3}\big(1 + \frac{2}{3} + \frac{3}{5}\big) = \frac{1}{3} \cdot \frac{15 + 10 + 9}{15} = \frac{34}{45}$.
- f), g) Le meilleur F1 vaut 0,75, au seuil 0,5.
- h) Ordre + + − + − − − : $\frac{1}{3}\big(1 + 1 + \frac{3}{4}\big) = \frac{11}{12} \approx 0{,}9167$.

Pour la copie : la precision monte quand le seuil passe un **positif** (le numérateur et le dénominateur augmentent de 1, ce qui rapproche la fraction de 1), et baisse quand il passe un négatif ; le recall, lui, ne fait que monter ou rester.

**Erreurs fréquentes.** Les trapèzes (0,711) au lieu des rectangles ; la moyenne des precisions de tous les seuils ; l'ordre [recall, precision].

**Variante.** L'AP si le film aimé de score 0,5 avait 0,95 ? *Réponse* : ordre + + − + − − − : $\frac{11}{12}$ aussi.

### Ex M03.11 — Score de Brier et calibration de huit prévisions

**Réponses** : a) `0.125` · b) `0.25` · c) `0.234` · d) `0.75` · e) `0.75` · f) `0.25` · g) `0.0` · h) `0.49`.

**Démarche.**
- a) Les carrés des écarts : 0,01 ; 0,04 ; 0,49 ; 0,16 ; 0,16 ; 0,09 ; 0,04 ; 0,01, de somme 1 : $\frac{1}{8}$.
- b) Chaque terme vaut 0,25. c) 3 retards sur 8 : $\frac{3}{8} \times \frac{5}{8} = \frac{15}{64} \approx 0{,}234$.
- d), e) Le paquet 0,9 ; 0,8 ; 0,7 ; 0,6 : moyenne 0,75, retards 3 sur 4. f), g) Le paquet 0,4 ; 0,3 ; 0,2 ; 0,1 : moyenne 0,25, aucun retard.
- h) Le colis 3 : $(0{,}7 - 0)^2$.

Pour la copie : le paquet haut est sur la diagonale ; le paquet bas annonce 25 % pour 0 % observé, un peu trop pessimiste. Le colis 3 coûte à lui seul la moitié de la somme : une probabilité de 0,7 pour un colis à l'heure. Huit colis sont bien trop peu : avec 4 colis par paquet, la fréquence observée ne peut valoir que 0, 0,25, 0,5, 0,75 ou 1, et son erreur type est d'environ 0,2.

**Erreurs fréquentes.** Faire la moyenne des écarts sans les élever au carré (0,3) ; diviser par 7 ; pour c), prendre 0,5 comme proportion.

**Variante.** Le score de Brier si le colis 3 avait été annoncé à 0,3 ? *Réponse* : la somme passe à $1 - 0{,}49 + 0{,}09 = 0{,}6$, soit 0,075.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M03.12 — L'aire sous la courbe ROC compte les paires bien classées

**Réponse modèle.**
1. Entre deux scores consécutifs, rien ne change. Quand le seuil descend juste sous un score $s_i$ d'un positif (et qu'aucun négatif n'a ce score), le nombre de positifs déclarés positifs augmente de 1 : TPR augmente de $\frac{1}{n_+}$, FPR ne bouge pas, un pas vertical. De même un négatif fait un pas horizontal de $\frac{1}{n_-}$. TPR et FPR sont des proportions d'un ensemble qui ne fait que grandir quand le seuil baisse : ils ne diminuent jamais, et la courbe va de $(0, 0)$ (seuil au-dessus de tout) à $(1, 1)$ (seuil sous tout).
2. Sous un escalier, l'aire est la somme des rectangles posés sous les paliers horizontaux. Il y a un pas horizontal par négatif $j$, de largeur $\frac{1}{n_-}$ ; la hauteur du rectangle est la hauteur de la courbe pendant ce pas, c'est-à-dire au moment où le seuil passe $t_j$. Les pas verticaux ont une largeur nulle et n'ajoutent rien.
3. Quand le seuil passe $t_j$, les positifs déjà déclarés positifs sont ceux de score plus grand que $t_j$ (les scores sont distincts) : la hauteur vaut $\frac{1}{n_+}\#\{i : s_i > t_j\}$.
4. $\text{aire} = \sum_j \frac{1}{n_-} \cdot \frac{1}{n_+}\#\{i : s_i > t_j\} = \frac{1}{n_+ n_-}\#\{(i, j) : s_i > t_j\}$, le nombre de paires bien classées divisé par le nombre de paires.
5. Si le seuil passe d'un coup $a$ positifs et $b$ négatifs de même score, TPR augmente de $\frac{a}{n_+}$ et FPR de $\frac{b}{n_-}$ en même temps : la courbe va en ligne droite d'un coin à l'autre d'un rectangle de $a \times b$ cases. Une diagonale coupe un rectangle en deux triangles égaux : l'aire sous le segment, dans ce rectangle, vaut la moitié du rectangle, soit $\frac{1}{2} \cdot \frac{ab}{n_+ n_-}$. Or ce rectangle représente exactement les $ab$ paires ex æquo de ce groupe : chacune compte pour $\frac{1}{2}$. Le reste de l'aire se compte comme en 4.
6. Une fonction strictement croissante garde chaque inégalité $s_i > t_j$, chaque égalité et chaque inégalité inverse : le décompte des paires, donc l'AUC, ne change pas. Une fonction strictement décroissante échange paires bien et mal classées et garde les ex æquo : l'AUC devient $1 - \text{AUC}$.
7. $U = \#\{s_i > t_j\} + \frac{1}{2}\#\{s_i = t_j\} = n_+ n_- \cdot \text{AUC}$ : l'AUC est la statistique de Mann et Whitney, normalisée.

**Grille.** Une bonne démonstration : (1) justifie la forme en escalier croissant (proportions d'ensembles qui grandissent) ; (2) découpe l'aire en rectangles sous les paliers horizontaux, un par négatif, et note que les pas verticaux n'ajoutent rien ; (3) identifie la hauteur comme une proportion de positifs de score plus grand ; (4) conclut par une double somme, une proportion de paires ; (5) traite les ex æquo par le rectangle coupé en deux ; (6) en déduit l'invariance par une fonction strictement croissante, et $1 - \text{AUC}$ pour une décroissante.

### Ex M03.13 — En multiclasse, micro-precision, micro-recall et accuracy sont égaux

**Réponse modèle.**
1. $\sum_k TP_k = \sum_k C_{kk}$, la somme de la diagonale (la **trace** de $C$). L'accuracy est la proportion d'exemples bien classés : $\frac{\sum_k C_{kk}}{n}$, avec $n = \sum_{k, l} C_{kl}$.
2. $\sum_k FP_k = \sum_k \sum_{l \ne k} C_{lk}$ : quand $k$ parcourt les colonnes, on additionne, colonne par colonne, toutes les cases hors diagonale ; chaque case $C_{lk}$ ($l \ne k$) est comptée une fois, dans la colonne $k$. Donc $\sum_k FP_k = n - \sum_k C_{kk}$. De même $\sum_k FN_k = \sum_k \sum_{l \ne k} C_{kl}$ additionne, ligne par ligne, les mêmes cases : $n - \sum_k C_{kk}$.
3. $\sum_k (TP_k + FP_k) = \sum_k C_{kk} + n - \sum_k C_{kk} = n$, et de même $\sum_k (TP_k + FN_k) = n$. Les deux fractions valent $\frac{\sum_k C_{kk}}{n}$, l'accuracy. Le micro-F1, moyenne harmonique de deux nombres égaux, vaut ce nombre.
4. Une erreur (vraie classe $k$, prédite $l \ne k$) est à la fois un faux positif pour la classe prédite $l$ et un faux négatif pour la vraie classe $k$ : elle est comptée une fois de chaque côté.
5. Diagonale $50 + 22 + 7 = 79$, $n = 100$ : 0,79 ; $\sum FP_k = (5 + 2) + (4 + 1) + (6 + 3) = 21 = 100 - 79$.
6. En binaire avec `average="binary"`, on ne garde que la classe positive : precision $\frac{TP}{TP + FP}$ et recall $\frac{TP}{TP + FN}$ diffèrent dès que $FP \ne FN$, et aucun des deux n'est l'accuracy $\frac{TP + TN}{n}$, qui compte aussi les vrais négatifs. L'égalité de 3 venait de ce qu'on additionnait les comptages de **toutes** les classes, la négative comprise. En multi-label, un exemple peut avoir plusieurs vrais labels ou plusieurs prédictions : une erreur n'est plus forcément à la fois un FP et un FN, et $\sum_k (TP_k + FP_k)$ (le nombre de prédictions) n'est plus égal à $\sum_k (TP_k + FN_k)$ (le nombre de vrais labels) : l'étape 2 tombe.
7. En binaire, le recall de la classe positive est le recall, et celui de la classe négative est $\frac{TN}{TN + FP}$, la spécificité : leur moyenne simple est $\frac{\text{recall} + \text{spécificité}}{2}$, la balanced accuracy. Exemple : $\begin{pmatrix} 90 & 0 \\ 10 & 0 \end{pmatrix}$ (vérité en lignes, 90 négatifs puis 10 positifs, tout prédit négatif) : accuracy 0,9, recall macro $\frac{1 + 0}{2} = 0{,}5$. Comme l'accuracy vaut $\pi \cdot \text{recall} + (1 - \pi) \cdot \text{spécificité}$ (probabilités totales), les deux sont égaux quand $\pi = \frac{1}{2}$ ou quand recall et spécificité sont égaux.

**Grille.** (1) la trace et l'accuracy ; (2) l'argument « chaque case hors diagonale est comptée une fois » pour FP et pour FN ; (3) la conclusion, avec le F1 ; (4) l'interprétation (une erreur, un FP et un FN) ; (5) la vérification numérique ; (6) pourquoi l'égalité tombe en binaire « classe positive seule » (ni entre elles, ni avec l'accuracy) et en multi-label ; (7) le recall macro binaire égal à la balanced accuracy, un exemple chiffré, et le cas d'égalité avec l'accuracy.

<a id="reflexion"></a>

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M03.14 — Un seuil sur un score : trois seuils, trois matrices de confusion

**Réponses** : a) `4` · b) `1` · c) `"2/3"` · d) `0.4` · e) `[0.625, 1.0]` · f) `0.5` · g) `4` · h) `0.3`.

**Démarche.** Les trois matrices (TP, FN, FP, TN) : seuil 0,7 : (2, 3, 1, 4) ; seuil 0,5 : (4, 1, 1, 4) ; seuil 0,3 : (5, 0, 3, 2).
- a), b) Au seuil 0,5 : 0,95, 0,81, 0,66, 0,52 (positifs) et 0,74 (négatif).
- c) $\frac{2}{3}$. d) $\frac{2}{5}$. e) $\frac{5}{8}$ et 1.
- f) F1 : 0,5 (seuil 0,7), 0,8 (seuil 0,5), $\frac{2 \times 0{,}625}{1{,}625} \approx 0{,}769$ (seuil 0,3).
- g) Un faux négatif (coût 3) et un faux positif (coût 1) : $3 \times 1 + 1 \times 1 = 4$ ; les colis mal adressés détectés ne coûtent rien. h) Coûts : $3 \times 3 + 1 = 10$, $4$, $3 \times 0 + 3 = 3$ : le seuil 0,3.

Pour la copie : quand le seuil baisse, le recall monte (0,4 ; 0,8 ; 1) et la precision baisse ici (0,667 ; 0,8 ; 0,625, pas tout à fait monotone). Avec un coût de 1 par erreur, on compte les erreurs : 4, 2, 3 : le seuil 0,5. Choisir le seuil sur les données de test, c'est l'ajuster à elles : l'évaluation devient trop optimiste ; on le choisit sur un jeu de validation.

**Erreurs fréquentes.** Oublier qu'un score égal au seuil est positif ; diviser la precision par le nombre de positifs ; additionner les erreurs sans leurs coûts ; faire payer la vérification des colis mal adressés détectés (l'énoncé dit qu'ils ne coûtent rien).

**Variante.** Avec un coût de 5 pour un colis mal adressé envoyé ? *Réponse* : 16, 6 et 3 : le seuil 0,3 encore, plus nettement.

### Ex M03.15 — Équité : les taux de faux positifs de deux groupes

**Réponses** : a) `0.2` · b) `0.1` · c) `0.8` · d) `0.6316` · e) `0.4706` · f) `0.38` · g) `False` · h) `0.0519`.

**Démarche.**
- a) $\frac{28}{28 + 112}$. b) $\frac{18}{18 + 162}$. c) $\frac{16}{20}$ (et $\frac{48}{60} = 0{,}8$ pour A).
- d) $\frac{48}{76}$. e) $\frac{16}{34}$. f) $\frac{48 + 28}{200}$.
- g) Même recall (0,8) mais taux de faux positifs différents (0,2 et 0,1) : non.
- h) Avec l'identité de la fiche : $\frac{\pi}{1 - \pi} = \frac{20}{180}$ pour B, $\frac{1 - \text{PPV}}{\text{PPV}} = \frac{28}{48}$ pour la precision de A, recall 0,8 : $\frac{1}{9} \times \frac{7}{12} \times 0{,}8 \approx 0{,}0519$. Vérification : $FP = 0{,}0519 \times 180 \approx 9{,}33$ et $\frac{16}{16 + 9{,}33} \approx 0{,}632$.

Pour la copie : l'identité donne $\frac{60}{140} \times \frac{28}{48} \times 0{,}8 = 0{,}2$ pour A et $\frac{20}{180} \times \frac{18}{16} \times 0{,}8 = 0{,}1$ pour B. Oui : une personne du groupe A est signalée à tort deux fois plus souvent. Mais une alerte vaut plus dans le groupe A (63 % de vrais robots) que dans le groupe B (47 %). Égaliser les taux de faux positifs rendrait les alertes encore moins sûres dans le groupe B, ou demanderait de baisser le recall dans le groupe A ; égaliser les precisions demanderait un taux de faux positifs de 5 % dans le groupe B. Le choix dépend de ce qu'une alerte entraîne : si un signalement bloque un compte, on protège d'abord les personnes signalées à tort (taux de faux positifs) ; si les alertes vont à une vérification humaine, la precision compte davantage.

**Erreurs fréquentes.** Diviser FP par le nombre de signalés ; confondre recall et precision ; croire qu'un réglage du seuil peut tout égaliser.

**Variante.** Le taux de faux positifs de A qui donnerait à A la precision de B (recall 0,8) ? *Réponse* : $\frac{60}{140} \times \frac{18}{16} \times 0{,}8 \approx 0{,}386$.

### Ex M03.16 — MML §6.3 : règle de la somme, règle du produit et vocabulaire, en anglais

**Éléments de réponse.**
1. Pour une variable discrète, la loi marginale de $\mathbf{x}$ est la somme de la loi jointe sur toutes les valeurs de $\mathbf{y}$ ; pour une variable continue, une intégrale. Le livre appelle ce passage la **marginalisation** (*marginalization property*) : on obtient une loi **marginale**.
2. Le livre note que beaucoup des difficultés de calcul des modèles probabilistes viennent de la règle de la somme : avec beaucoup de variables, ou des variables à beaucoup d'états, il faut calculer une somme ou une intégrale en grande dimension, ce qui est coûteux (et souvent impossible exactement). Pour 30 variables binaires, la loi marginale d'une seule s'obtient en sommant sur les $2^{29} \approx 5{,}4 \times 10^8$ configurations des 29 autres.
3. La loi jointe est le produit d'une loi conditionnelle et d'une loi marginale : $p(\mathbf{x}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{x})\,p(\mathbf{x})$. Les rôles de $\mathbf{x}$ et $\mathbf{y}$ sont symétriques dans la loi jointe, donc on peut aussi écrire $p(\mathbf{x} \mid \mathbf{y})\,p(\mathbf{y})$.
4. $p$ désigne une probabilité (une **masse**, *probability mass function*) pour une variable discrète, et une **densité** (*probability density function*) pour une variable continue ; la même notation sert à une loi jointe, marginale ou conditionnelle. $p(x, y)$ est $P(X = x, Y = y)$ pour deux variables discrètes, et une densité jointe (qu'on intègre sur une région du plan) pour deux variables continues.
5. $P(\text{premium}) = 0{,}06 + 0{,}10 = 0{,}16$ (somme sur les appareils) ; $P(\text{mobile} \cap \text{premium}) = P(\text{premium} \mid \text{mobile})\,P(\text{mobile}) = 0{,}1 \times 0{,}6 = 0{,}06$.
6. Par exemple $p(x, y, z) = p(x)\,p(y \mid x)\,p(z \mid x, y)$ et $p(x, y, z) = p(z)\,p(x \mid z)\,p(y \mid x, z)$ (toute permutation convient).
7. Par exemple : *marginalization* (marginalisation), *intractable* (impossible à calculer exactement en pratique), *factorized* (écrit comme un produit).

### Ex M03.17 — Un taux de réussite trompeur : le paradoxe de Simpson

**Éléments de réponse.**
1. Femmes : 75 % au département Produit, 20 % au département Recherche, 36,5 % au total. Hommes : 70 %, 15 %, 53,5 %. Les femmes sont plus souvent embauchées dans **chaque** département, et moins souvent au total.
2. Le taux global d'un groupe est la moyenne de ses deux taux, pondérée par **sa** répartition des candidatures : pour les femmes, $0{,}75 \times \frac{60}{200} + 0{,}20 \times \frac{140}{200} = 0{,}365$ ; pour les hommes, $0{,}70 \times \frac{140}{200} + 0{,}15 \times \frac{60}{200} = 0{,}535$. Les femmes postulent surtout au département le plus sélectif.
3. Les deux chiffres sont exacts. Pour juger le traitement des candidatures par les recruteurs, il faut comparer **à département égal** : les taux par département. Le titre du premier journal répond à une autre question.
4. Alors le choix du département n'est plus libre : il fait partie du mécanisme de discrimination. Comparer à département égal masquerait cette discrimination à l'entrée ; le chiffre global redevient pertinent pour la question « les femmes ont-elles les mêmes chances d'être embauchées par l'entreprise ? ». La bonne comparaison dépend de la question et du rôle de la variable (de confusion, ou étape du mécanisme).
5. Sans le département, le modèle verra que les candidates sont moins souvent embauchées et pourra apprendre à moins bien les classer, reproduisant l'effet de la répartition. Sans le sexe mais avec le département, il apprendra le taux de chaque département, ce qui est plus juste ici, mais si les offres découragent les femmes (question 4), il reproduira aussi ce biais d'entrée ; et d'autres features (prénom, parcours) peuvent servir de substitut au sexe.
6. En 1973, l'université de Berkeley admettait globalement moins de femmes que d'hommes, alors que la plupart des départements admettaient autant ou plus de femmes : les femmes postulaient davantage dans les départements les plus sélectifs. C'est la même structure.

**Grille.** Les taux justes ; l'explication par les poids ; la distinction entre les deux questions ; la discussion de la question 4 (la variable comme partie du mécanisme) ; les risques pour un modèle ; le lien avec Berkeley.

### Ex M03.18 — Expliquer pourquoi P(A sachant B) n'est pas P(B sachant A)

**Réponse modèle.**

> Les deux phrases parlent de deux probabilités différentes. Les données disent $P(\text{usage rare} \mid \text{désabonné}) = 95\,\%$ ; ta conclusion porte sur $P(\text{désabonné} \mid \text{usage rare})$. Elles ont le même numérateur, les utilisateurs à la fois rares et désabonnés, mais pas le même dénominateur. Imagine 1 000 utilisateurs : 40 se désabonnent, dont 38 utilisaient l'appli rarement ; mais 600 utilisateurs l'ouvrent rarement. Alors 95 % des désabonnés étaient rares, et pourtant seuls $\frac{38}{600} \approx 6\,\%$ des utilisateurs rares se désabonnent. Pour calculer la bonne probabilité, il manque le nombre d'utilisateurs rares et le taux global de désabonnement. Ta promotion toucherait 600 personnes pour en retenir au mieux 38.

**Grille.** (1) les deux probabilités écrites avec « sachant » ; (2) un tableau chiffré cohérent où la seconde est petite ; (3) les informations manquantes (la part d'utilisateurs rares, le taux de désabonnement) ; (4) huit lignes au plus.

<a id="entretien"></a>

## 💼 Entretien

### M03.E1 — Une variable indépendante de la cible peut-elle aider un modèle ?

**Réponse modèle (60 secondes).**

> Non, ce n'est pas sans risque. Une feature peut être indépendante de la cible prise seule, et très utile **avec** une autre. L'exemple classique : deux bits aléatoires $X_1$ et $X_2$, et une cible $Y = X_1$ XOR $X_2$, qui vaut 1 quand les deux bits diffèrent. Chaque bit seul ne dit rien de $Y$ : $P(Y = 1 \mid X_1 = 0) = P(Y = 1 \mid X_1 = 1) = \frac{1}{2}$. Mais les deux ensemble déterminent $Y$ exactement. C'est l'exemple des trois événements indépendants deux à deux, mais pas mutuellement : connaître deux d'entre eux donne le troisième. Une feature peut aussi aider en corrigeant le bruit d'une autre. Donc on ne juge pas une feature seule : on compare la performance d'un modèle avec et sans elle sur un jeu de validation, ou on mesure son importance par permutation dans le modèle entier.

**Grille.** (1) la réponse : non, c'est risqué ; (2) un exemple chiffré de deux variables indépendantes de la cible qui la déterminent ensemble (XOR) ; (3) le lien avec l'indépendance deux à deux contre mutuelle ; (4) une méthode pour tester une feature dans son contexte (ablation sur validation, importance par permutation).

<a id="notebook"></a>

## Notebook

### Ex M03.19 — Jointe, marginales et conditionnelles à partir d'un tableau de comptages · `joint_from_counts, marginal, conditional`

**Réponses** : a) `[[0.225, 0.15, 0.125], [0.075, 0.225, 0.2]]` · b) `[0.3, 0.375, 0.325]` · c) `[0.5, 0.5]` · d) `[0.45, 0.3, 0.25]` · e) `[0.385, 0.615]` · f) `"ValueError"` · g) `"ValueError"` · h) `"ValueError"`.

**Démarche.** Une fonction auxiliaire `_check_joint(joint)` : `np.asarray(joint, dtype=float)`, puis `ValueError` si `ndim != 2` ou tableau vide, si une case n'est pas positive ou nulle (`not np.all(table >= 0)`, qui refuse aussi `nan`), si `abs(table.sum() - 1) > 1e-9`. `joint_from_counts` vérifie la forme, le signe et un total positif, puis divise par le total. `marginal` : `_check_joint`, `axis in (0, 1)`, puis `table.sum(axis=axis)`. `conditional` : exactement un indice (`(given_row is None) == (given_column is None)` lève l'erreur), un indice dans le tableau (un indice négatif, que NumPy accepterait, est refusé aussi), une ligne (ou une colonne) de somme positive, divisée par sa somme. Pour la copie : c) est la loi de la formule (une probabilité par ligne).

**Erreurs fréquentes.** Diviser chaque ligne par son total dans `joint_from_counts` ; échanger les axes de `marginal` ; renvoyer une ligne de la loi jointe sans la diviser par sa somme ; oublier les vérifications (les trois dernières questions).

### Ex M03.20 — Tester l'indépendance avec une tolérance · `are_independent`

**Réponses** : a) `False` · b) `True` · c) `False` · d) `True` · e) `False` · f) `True` · g) `"ValueError"`.

**Démarche.** `table = _check_joint(joint)`, puis `products = np.outer(table.sum(axis=1), table.sum(axis=0))` et `bool(np.all(np.abs(table - products) <= tol))`. Pour la copie : dans la loi de e), la première case vaut le produit de ses marges ($0{,}5 \times 0{,}2$) mais pas la deuxième (0,2 contre 0,15) ; `TABLE_20` s'écarte de 0,001 dans chaque case.

**Erreurs fréquentes.** Comparer avec `==` (b) devient faux à cause des arrondis en flottants) ; ne vérifier qu'une case ; renvoyer `np.True_` (un booléen de NumPy, dont le nom de type s'écrit aussi `bool` depuis NumPy 2 : seul `isinstance(..., bool)` les distingue).

### Ex M03.21 — L'AUC en comptant les paires · `auc_by_pairs`

**Réponses** : a) `0.6667` · b) `0.8333` · c) `1.0` · d) `0.0` · e) `"ValueError"` · f) `"float"` · g) `0.7748`.

**Démarche.** Vérifier que les deux listes sont non vides, puis `diff = pos[:, None] - neg[None, :]` et `float((np.sum(diff > 0) + 0.5 * np.sum(diff == 0)) / diff.size)`. Pour la copie : $D = S_+ - S_- \sim \mathcal{N}(1, 2)$, donc $P(D > 0) = P\big(Z > -\frac{1}{\sqrt{2}}\big) = \Phi\big(\frac{1}{\sqrt{2}}\big) \approx \Phi(0{,}71) \approx 0{,}761$.

**Erreurs fréquentes.** Compter un ex æquo pour 0 ou pour 1 ; échanger positifs et négatifs ($1 - \text{AUC}$) ; une division par zéro au lieu d'une `ValueError` ; renvoyer un `numpy.float64`.

### Ex M03.22 — `sklearn.metrics.roc_auc_score` contre le comptage des paires, ex æquo compris

**Réponses** : a) `0.7222` · b) `0.2778` · c) `0.6667` · d) `0.6667` · e) `9` · f) `0.7335`.

**Démarche.** Voir `05_solutions.ipynb`. Pour la copie : avec des prédictions 0/1, la courbe ROC a trois points, $(0, 0)$, $(\text{FPR}, \text{TPR})$ et $(1, 1)$ ; l'aire sous ces deux segments (un triangle et un trapèze) vaut $\frac{\text{FPR} \cdot \text{TPR}}{2} + (1 - \text{FPR})\frac{\text{TPR} + 1}{2} = \frac{\text{TPR} + 1 - \text{FPR}}{2}$, la moyenne du recall et de la spécificité. Le premier seuil de `roc_curve` est `inf` : aucun exemple n'est déclaré positif, le point $(0, 0)$.

**Erreurs fréquentes.** Donner les scores avant les labels ; calculer c) sur les scores ; compter 8 seuils.

### Ex M03.23 — Prédire : l'AUC après une transformation croissante des scores

**Réponses** : a) `1` · b) `1` · c) `2` · d) `1` · e) `2`.

**Démarche.** L'AUC ne dépend que de l'ordre des scores dans chaque paire (fiche §7 et M03.12, question 6) : $10\,s$, $s^2$ (scores positifs) et le rang gardent l'ordre ; $1 - s$ l'inverse. Le score de Brier compare les valeurs à 0 et 1 : il change (0,1165 puis 0,1143 ici).

### Ex M03.24 — Simuler pour estimer une probabilité conditionnelle

**Réponses** : a) `0.459` · b) `0.834` · c) `0.503` · d) `0.501` · e) `0.501` · f) `"ValueError"` · g) `0.14`.

**Démarche.** `event[given]` garde les tirages où la condition est vraie ; `np.mean` donne la fréquence ; `ValueError` si `given` n'est jamais vrai (sinon `np.mean` d'un tableau vide renvoie `nan` avec un avertissement). Valeurs exactes : $\frac{5}{11}$, $\frac{5}{6}$, $\frac{1}{2}$, $\frac{1}{2}$, $\frac{1}{2}$ et $\frac{5}{36} \approx 0{,}139$. g) est exactement la fréquence de l'intersection : la règle du produit est vraie aussi pour des fréquences. Pour la copie : a) repose sur environ 30 600 tirages (erreur type 0,003), c) sur environ 16 800 (erreur type 0,004) ; les écarts observés (0,004 et 0,003) sont de l'ordre d'une erreur type.

**Erreurs fréquentes.** Diviser par le nombre total de tirages (on obtient la fréquence de l'intersection, 0,140) ; échanger l'événement et la condition ; taper la valeur exacte au lieu de la fréquence simulée.

### Ex M03.25 — La courbe ROC en escalier : une marche par paire

**Démarche.** `roc_points` : les scores distincts par ordre décroissant (`np.unique(...)[::-1]`), et pour chaque seuil `(np.mean(neg >= t), np.mean(pos >= t))`, après le point `(0.0, 0.0)`. `draw_roc` : `ax.plot` des points, la diagonale `ax.plot([0, 1], [0, 1], "--")`, `ax.set_xlabel`, `ax.set_ylabel`, et le titre avec l'AUC. Pour la copie : 33 cases sur 48 sont sous la courbe, en comptant pour moitié les 2 cases traversées par le segment diagonal du seuil 0,71 (les paires de ses deux positifs avec le négatif de même score) : $\frac{33}{48} = 0{,}6875$.

**Erreurs fréquentes.** `ax.step` (qui dessine une marche à la place du segment diagonal) ; un point par exemple au lieu d'un point par score distinct (deux points superposés pour les ex æquo, et un passage par un coin faux) ; la règle « score > seuil » au lieu de « $\ge$ » ; oublier $(0, 0)$.

### Ex M03.26 — Chasse à l'erreur : conditionnelle inversée, marginale oubliée

**Réponses** : a) `"ACDE"` · b) `[0.36, 0.14, 0.389, 0.625, 0.52, 0.3]`.

**Démarche.** (A) oublie les poids des niveaux : $0{,}1 + 0{,}12 + 0{,}14 = 0{,}36$ (probabilités totales). (B) est la règle du produit : juste. (C) donne $P(\text{termine} \mid \text{avancé})$ au lieu de $P(\text{avancé} \mid \text{termine}) = \frac{0{,}14}{0{,}36} \approx 0{,}389$. (D) calcule la jointe $P(\text{débutant} \cap \text{ne termine pas}) = 0{,}4$ sans diviser par $P(\text{ne termine pas}) = 0{,}64$ : 0,625. (E) additionne deux probabilités sachant des niveaux différents, et donne 1,1, impossible : $\frac{0{,}4 \times 0{,}3 + 0{,}7 \times 0{,}2}{0{,}5} = 0{,}52$. (F) est le complément sachant la même condition : juste.

**Erreurs fréquentes.** Accuser (B) (c'est bien une intersection) ou (F) ; oublier de diviser par 0,5 en (E).

### Ex M03.27 — Une fonction qui refuse un tableau invalide (`ValueError`)

**Démarche.** `array = np.asarray(table, dtype=float)` ; puis, dans cet ordre : `array.ndim != 2 or array.size == 0` ; `not np.all(np.isfinite(array))` ; `np.any(array < 0)` ; `abs(array.sum() - 1) > tol` ; chaque test lève une `ValueError` avec son propre message. Pour la copie : la forme d'abord (la somme d'un tableau vide vaut 0, et « ligne » n'a pas de sens en dimension 1) ; les NaN avant la somme, car `abs(nan - 1) > tol` est faux.

**Erreurs fréquentes.** Laisser passer `nan` ; un seul message pour toutes les règles ; `assert` au lieu de `raise ValueError` (un `assert` disparaît avec `python -O`, et lève `AssertionError`) ; refuser une somme de $1 + 10^{-12}$ en comparant avec `==`.

### Ex M03.28 — Défi : retrouver un tableau de contingence à partir de quelques probabilités

**Réponses** : a) `[[150, 30, 60], [150, 150, 60]]` · b) `"3/8"`.

**Démarche.** Marges : 240 visites sur l'appli, 360 sur le site, 300 achats. L'information 4 donne appli-achat $= 0{,}625 \times 240 = 150$, donc site-achat $= 150$. L'information 6 donne site-rien $= \frac{360}{6} = 60$, donc site-abandon $= 150$. L'information 5 : appli-abandon $= a$ avec $\frac{a}{a + 150} = \frac{1}{6}$, soit $a = 30$ ; appli-rien $= 240 - 150 - 30 = 60$. b) $\frac{150 + 30}{300 + 180} = \frac{180}{480} = \frac{3}{8}$. Pour la copie : unique (chaque information fixe une case) ; sans l'information 6, il faudrait une autre information sur la ligne « site » ou la colonne « rien », par exemple $P(\text{rien}) = 0{,}2$. Canal et résultat sont dépendants ($0{,}625 \ne 0{,}5$).

**Erreurs fréquentes.** Lire l'information 5 comme $P(\text{abandon} \mid \text{appli})$ ; comparer des flottants avec `==` dans une recherche ; transposer le tableau.
