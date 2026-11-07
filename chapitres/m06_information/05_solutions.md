# M06 · Théorie de l'information — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté. Sauf mention contraire, les entropies sont en bits.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Pont, estimation et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M06.Q1 — La surprise et la probabilité
1. $-\log_2 \frac{1}{256} = \log_2 256 = 8$ bits.
2. $-\log_2 p = 11$, donc $p = 2^{-11} = \frac{1}{2048}$.
3. $1{,}5 + 2 = 3{,}5$ bits : les informations d'événements indépendants s'additionnent.
4. **Faux** : $0 < p \le 1$, donc $\log_2 p \le 0$ et $-\log_2 p \ge 0$. Elle est nulle pour un événement certain.
5. $2 \ln 2 \approx 1{,}39$ nat (1 bit vaut $\ln 2 \approx 0{,}693$ nat).
6. Pour que les informations d'événements indépendants **s'additionnent** : la probabilité des deux est le produit $p\,q$, et le logarithme change un produit en somme, $-\log(p\,q) = -\log p - \log q$. Avec $\frac{1}{p}$, elles se multiplieraient, et un événement certain apporterait 1 au lieu de 0.

### M06.Q2 — L'entropie : vrai ou faux
1. **Faux** : c'est une moyenne de termes $-\log_2 p \ge 0$.
2. **Faux** : une loi sur 12 issues a une entropie d'au plus $\log_2 12 \approx 3{,}58$ bits, atteinte par la loi uniforme ; elle peut donc dépasser 3 bits.
3. **Faux** : une issue de probabilité 0 ajoute $0 \log 0 = 0$.
4. **Faux** : l'entropie ne dépend que des probabilités, pas des valeurs. Multiplier les valeurs par 2 ne change aucune probabilité.
5. **Faux** : $(0{,}97 ;\ 0{,}03)$ est presque certaine, son entropie est petite (environ 0,19 bit) ; $(0{,}53 ;\ 0{,}47)$ est presque équilibrée, son entropie est proche de 1 bit.
6. **Vrai** : $H(X) = \sum p(x)\,\big(-\log_2 p(x)\big) = \mathbb{E}[-\log_2 p(X)]$, la surprise moyenne.

### M06.Q3 — Conjointe et conditionnelle
1. $H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y)$.
2. $H(Y \mid X) = 0$ : connaître $X$, c'est connaître $Y$.
3. $H(X, Y) = H(X) + H(Y)$.
4. **Faux** en général : avec la règle de la chaîne, $H(Y \mid X) - H(X \mid Y) = H(Y) - H(X)$, qui n'est nul que si $H(X) = H(Y)$.
5. **Vrai** : $H(X, Y) = H(X) + H(Y \mid X)$ et $H(Y \mid X) \ge 0$.
6. $H(Y \mid X) = 2{,}5 - 1 = 1{,}5$ et $H(X \mid Y) = 2{,}5 - 2 = 0{,}5$.

### M06.Q4 — L'information mutuelle
1. $I(X ; Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X) = H(X) + H(Y) - H(X, Y)$.
2. **Vrai** : la troisième écriture est symétrique.
3. $X$ et $Y$ sont **indépendantes** (et réciproquement).
4. $I = 2 - 0{,}5 = 1{,}5$ bit.
5. **Faux** : $I(X ; Y) = H(X) - H(X \mid Y) \le H(X)$, et de même $I \le H(Y)$.
6. **Faux** : la corrélation ne voit que les liens linéaires. La figure des deux nuages de points (fiche §4) montre une dépendance forte avec une corrélation presque nulle, alors que l'information mutuelle n'est nulle que pour des variables indépendantes.

### M06.Q5 — La KL n'est pas une distance
1. $\mathrm{KL}(p \,\|\, q) = H(p, q) - H(p)$.
2. 0.
3. $\mathrm{KL}(p \,\|\, q) = \frac{2}{3}\log_2 \frac{2/3}{1/2} + \frac{1}{3}\log_2 \frac{1/3}{1/4} = \log_2 \frac{4}{3} \approx 0{,}415$ bit : **finie** (la troisième issue, de probabilité 0 sous $p$, ne compte pas). $\mathrm{KL}(q \,\|\, p)$ contient le terme $\frac{1}{4}\log_2 \frac{1/4}{0}$ : elle est **infinie**.
4. La symétrie ($\mathrm{KL}(p \,\|\, q) \ne \mathrm{KL}(q \,\|\, p)$ en général) et l'inégalité triangulaire. (La positivité, elle, est vraie.)
5. **Faux** : c'est l'inégalité de Gibbs (fiche §6, M06.11).
6. Le nombre moyen de bits **perdus** par symbole quand on code les données avec un code fait pour le modèle, au lieu du meilleur code pour les données.

### M06.Q6 — L'inégalité de Jensen
1. $\mathbb{E}[f(X)] \ge f(\mathbb{E}[X])$ : la moyenne des images est au-dessus de l'image de la moyenne.
2. $\mathbb{E}[X^2] = \frac{0 + 16}{2} = 8$ et $(\mathbb{E}[X])^2 = 2^2 = 4$.
3. $\mathbb{E}[\ln X] \le \ln \mathbb{E}[X]$ : $\ln$ est **concave** ($\ln'' x = -\frac{1}{x^2} < 0$), et l'inégalité se retourne.
4. Quand $X$ est constante (elle ne prend qu'une valeur, avec probabilité 1).
5. **Vrai** : $x \mapsto \frac{1}{x}$ est convexe sur $]0, +\infty[$ (dérivée seconde $\frac{2}{x^3} > 0$).
6. La **variance** de $X$ (M02b).

### M06.Q7 — Codes préfixes
1. Aucun mot n'est le début d'un autre. En lisant les bits de gauche à droite, dès que les bits lus forment un mot, c'est ce mot : aucun mot plus long ne peut commencer ainsi.
2. **Préfixe** : ni 01, ni 10, ni 11 n'est le début de 001, et 001 n'est le début d'aucun mot. **Pas complet** : sa somme de Kraft vaut $\frac{3}{4} + \frac{1}{8} = \frac{7}{8} < 1$ ; on pourrait ajouter le mot 000.
3. **Non** : 1 est le début de 10 (la suite « 10 » se lit « 1, 0 » ou « 10 »).
4. **Oui** : $\frac{1}{2} + 3 \times \frac{1}{8} = \frac{7}{8} \le 1$ ; par exemple 0, 100, 101, 110.
5. 10 : $2^9 = 512 < 1\,000 \le 1\,024 = 2^{10}$.
6. **Vrai** : deux mots de même longueur ne peuvent être le début l'un de l'autre que s'ils sont égaux.

<a id="rappels"></a>

## 🔁 Rappels

### M06.R1 — Logarithmes en base 2 (R6)
1. $2^{12} = 4096$, $2^{-9} = \frac{1}{512}$, $2^{3/2} = 2\sqrt{2}$ : les exposants sont 12, $-9$ et $\frac{3}{2}$.
2. $\log_2 x = \frac{\ln x}{\ln 2}$, donc $\log_2 11 \approx \frac{2{,}3979}{0{,}6931} \approx 3{,}459$.
3. $48 = 16 \times 3$, donc $\log_2 48 = \log_2 16 + \log_2 3 = 4 + \log_2 3$.
4. $x = 2^{-2{,}5} = \frac{1}{4\sqrt{2}} = \frac{\sqrt{2}}{8} \approx 0{,}177$.
5. Pour $p = 1$ seulement : $\log_2 1 = 0$, et $\log_2 p < 0$ pour $p < 1$. Pour $p = \frac{1}{4}$ : $-\frac{1}{4}\log_2 \frac{1}{4} = \frac{1}{4} \times 2 = \frac{1}{2}$.

### M06.R2 — Probabilités jointes et conditionnelles (M03)
1. En divisant par 100 : 0,12 ; 0,18 ; 0,28 ; 0,42.
2. $P(\text{pluie}) = 0{,}3$, $P(\text{pas de pluie}) = 0{,}7$ ; $P(\text{en retard}) = 0{,}4$, $P(\text{à l'heure}) = 0{,}6$.
3. $\frac{12}{30} = 0{,}4$ et $\frac{28}{70} = 0{,}4$.
4. **Oui** : les deux probabilités conditionnelles de 3. sont égales à $P(\text{en retard})$ ; et chaque case est le produit de ses marges ($0{,}3 \times 0{,}4 = 0{,}12$, $0{,}3 \times 0{,}6 = 0{,}18$, $0{,}7 \times 0{,}4 = 0{,}28$, $0{,}7 \times 0{,}6 = 0{,}42$).
5. $H(Y \mid X) = H(Y)$ : savoir s'il pleut n'apprend rien sur le retard ($I(X ; Y) = 0$).

### M06.R3 — Convexité (M05a)
1. $f$ est convexe si, pour tous $a$, $b$ et tout $t \in [0, 1]$, $f\big(t a + (1 - t) b\big) \le t f(a) + (1 - t) f(b)$ : la corde est au-dessus de la courbe.
2. **Oui** : $f'(x) = -\frac{1}{x}$, $f''(x) = \frac{1}{x^2} > 0$.
3. **Oui** : $g'(x) = \ln x + 1$, $g''(x) = \frac{1}{x} > 0$ sur $]0, +\infty[$.
4. **Oui** : l'inégalité des cordes s'additionne (ou : $(f + g)'' = f'' + g'' \ge 0$).
5. **Au-dessous** : une fonction concave a ses cordes sous sa courbe.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M06.1 — L'information d'événements et l'entropie d'une loi à quatre issues

**Réponses** : a) `[0.86, 1.51, 3.84, 5.06]` · b) `1.425` · c) `0.99` · d) `5.921` · e) `1.337` · f) `2.85`.

**Démarche.**
- a) $-\log_2 0{,}55 \approx 0{,}862$ ; $-\log_2 0{,}35 \approx 1{,}515$ ; $-\log_2 0{,}07 \approx 3{,}837$ ; $-\log_2 0{,}03 \approx 5{,}059$ bits.
- b) $H = 0{,}55 \times 0{,}8625 + 0{,}35 \times 1{,}5146 + 0{,}07 \times 3{,}8365 + 0{,}03 \times 5{,}0589 \approx 0{,}4744 + 0{,}5301 + 0{,}2686 + 0{,}1518 = 1{,}4249 \approx 1{,}425$ bit.
- c) $1{,}4248 \times \ln 2 \approx 0{,}988$ nat.
- d) Les informations s'additionnent : $0{,}8625 + 5{,}0589 \approx 5{,}921$ bits (la probabilité des deux est $0{,}55 \times 0{,}03 = 0{,}0165$).
- e) La loi $(0{,}55 ;\ 0{,}35 ;\ 0{,}1)$ : $0{,}4744 + 0{,}5301 + 0{,}1 \times 3{,}3219 \approx 1{,}337$ bit.
- f) Les codes de deux requêtes indépendantes forment un couple dont l'entropie est la somme des entropies (§3, la règle de la chaîne avec $H(Y \mid X) = H(Y)$) : $2 \times 1{,}4248 \approx 2{,}850$ bits.

Pour la copie : en regroupant les deux erreurs, on perd l'information « laquelle des deux erreurs ». La règle de la chaîne le chiffre : $b) - e) = 0{,}1 \times H(0{,}7 ;\ 0{,}3) \approx 0{,}088$ bit, la probabilité 0,1 d'une erreur fois l'incertitude qui reste sur son type, de loi $(0{,}7 ;\ 0{,}3)$ une fois qu'on sait qu'il y a une erreur.

**Erreurs fréquentes.** Utiliser $\ln$ au lieu de $\log_2$ (a : `[0.6, 1.05, 2.66, 3.51]`) ; additionner les informations sans les pondérer (b : 11,272) ou en faire la moyenne simple (b : 2,818) ; diviser par $\ln 2$ au lieu de multiplier (c : 2,06) ; multiplier les informations au lieu de les additionner (d : 4,363) ; répondre l'entropie d'une seule requête en f).

**Variante.** Combien de bits apporte un événement de probabilité $\frac{3}{8}$ ? Quelle est l'entropie de $(\frac{3}{4}, \frac{1}{8}, \frac{1}{8})$ ? *Réponse* : $3 - \log_2 3 \approx 1{,}415$ bit ; $\frac{3}{4}\log_2 \frac{4}{3} + \frac{1}{4} \times 3 \approx 1{,}061$ bit.

### Ex M06.2 — L'entropie maximale : comparer des lois à quatre issues

**Réponses** : a) `1.782` · b) `1.871` · c) `1.54` · d) `2` · e) `1.86` · f) `1.29`.

**Démarche.**
- a) $0{,}45 \times 1{,}1520 + 0{,}3 \times 1{,}7370 + 0{,}15 \times 2{,}7370 + 0{,}1 \times 3{,}3219 \approx 0{,}5184 + 0{,}5211 + 0{,}4106 + 0{,}3322 = 1{,}7822$.
- b) $0{,}4 \times 1{,}3219 + 0{,}3 \times 1{,}7370 + 2 \times 0{,}15 \times 2{,}7370 \approx 0{,}5288 + 0{,}5211 + 0{,}8211 = 1{,}8710$.
- c) $0{,}5184 + 0{,}5211 + 0{,}25 \times 2 \approx 1{,}5395$, soit 1,54.
- d) $\log_2 4 = 2$, pour la loi uniforme.
- e) La première issue est fixée à 0,45 ; les trois autres se partagent 0,55. Par la règle du regroupement (M06.1), $H = H(0{,}45 ;\ 0{,}55) + 0{,}55 \times H(\text{loi des trois dernières, sachant que la première n'est pas sortie})$, et le second terme est le plus grand pour la loi uniforme sur trois issues : $H_{\max} = H(0{,}45 ;\ 0{,}55) + 0{,}55 \log_2 3 \approx 0{,}9928 + 0{,}8717 = 1{,}8645$, soit 1,86, atteint par $(0{,}45 ;\ 0{,}1\overline{83} ;\ 0{,}1\overline{83} ;\ 0{,}1\overline{83})$.
- f) $1{,}8645 \times \ln 2 \approx 1{,}292$ nat.

Pour la copie : donner de la probabilité d'une issue probable à une issue rare (sans les inverser) rapproche les probabilités, et l'entropie monte (1,782 → 1,871). Regrouper deux issues efface une distinction, et l'entropie baisse (1,782 → 1,54). Sous la contrainte de e), le maximum répartit le reste également.

**Erreurs fréquentes.** Répondre 4 en d) (le nombre d'issues, pas son logarithme) ; ignorer la contrainte en e) (2) ; calculer f) en divisant par $\ln 2$.

**Variante.** La plus grande entropie possible sur quatre issues dont la première a la probabilité 0,7 ? *Réponse* : $H(0{,}7 ;\ 0{,}3) + 0{,}3 \log_2 3 \approx 0{,}881 + 0{,}475 = 1{,}357$ bit.

### Ex M06.3 — Entropies conjointe et conditionnelle d'un tableau 2 × 3

**Réponses** : a) `1.92` · b) `1.581` · c) `0.949` · d) `1.4` · e) `0.52` · f) `0.18`.

**Démarche.**
- a) Les cases non nulles : $0{,}4 \times 1{,}3219 + 0{,}18 \times 2{,}4739 + 2 \times 0{,}21 \times 2{,}2515 \approx 0{,}5288 + 0{,}4453 + 0{,}9456 = 1{,}9197$, soit 1,920.
- b) La ligne « payant », divisée par $P(\text{payant}) = 0{,}6$, donne la loi $(0{,}3 ;\ 0{,}35 ;\ 0{,}35)$, d'entropie $0{,}3 \times 1{,}7370 + 0{,}7 \times 1{,}5146 \approx 1{,}5813$.
- c) $H(Y \mid X) = 0{,}4 \times 0 + 0{,}6 \times 1{,}5813 \approx 0{,}9488$ (la ligne « gratuit » a l'entropie 0).
- d) La loi de $Y$ (les sommes des colonnes) : $(0{,}58 ;\ 0{,}21 ;\ 0{,}21)$, d'entropie $0{,}58 \times 0{,}7859 + 0{,}42 \times 2{,}2515 \approx 1{,}4015$, soit 1,40.
- e) $H(X \mid Y) = H(X, Y) - H(Y) \approx 1{,}9197 - 1{,}4015 = 0{,}5183$, soit 0,52.
- f) $1{,}5813 - 1{,}4015 \approx 0{,}180$, soit 0,18.

Pour la copie : $H(X) + H(Y \mid X) \approx 0{,}9710 + 0{,}9488 = 1{,}9198$ et $H(Y) + H(X \mid Y) \approx 1{,}4015 + 0{,}5183 = 1{,}9198$. $H(Y \mid X = \text{gratuit}) = 0$ : tous les gratuits ont un usage faible. f) est positif : savoir qu'un utilisateur est payant **augmente** l'incertitude sur son usage. Mais $H(Y \mid X) - H(Y) \approx -0{,}45 < 0$ : **en moyenne**, savoir ne rend pas moins sûr, car la valeur « gratuit » supprime toute incertitude. Le théorème porte sur la moyenne, pas sur chaque valeur (M06.10, question 6).

**Erreurs fréquentes.** Calculer l'entropie des cases de la ligne sans les diviser par $P(\text{payant})$ (b : 1,391), ou diviser l'entropie par $P(\text{payant})$ (b : 2,318) ; oublier la ligne « gratuit » dans la moyenne (c : 1,581) ; répondre $H(Y \mid X)$ ou $I(X ; Y)$ en e) ; l'écart dans le mauvais ordre en f).

**Variante.** Pour la loi jointe $\begin{pmatrix} \frac{1}{4} & 0 \\ \frac{1}{4} & \frac{1}{2} \end{pmatrix}$ (lignes : $X$), que vaut $H(Y \mid X)$ ? *Réponse* : $\frac{1}{4} \times 0 + \frac{3}{4} \times H\big(\frac{1}{3}, \frac{2}{3}\big) \approx 0{,}75 \times 0{,}918 = 0{,}689$.

### Ex M06.4 — La règle de la chaîne de l'entropie, vérifiée

**Réponses** : a) `1` · b) `0.881` · c) `0.971` · d) `0.926` · e) `1.926` · f) `0.993` · g) `0.933`.

**Démarche.**
- a) $X$ vaut e-mail ou SMS une fois sur deux : $H(X) = 1$.
- b) La ligne « e-mail » divisée par 0,5 : $(0{,}7 ;\ 0{,}3)$, d'entropie $0{,}7 \times 0{,}5146 + 0{,}3 \times 1{,}7370 \approx 0{,}3602 + 0{,}5211 = 0{,}8813$.
- c) La ligne « SMS » divisée par 0,5 : $(0{,}4 ;\ 0{,}6)$, d'entropie $0{,}4 \times 1{,}3219 + 0{,}6 \times 0{,}7370 \approx 0{,}5288 + 0{,}4422 = 0{,}9710$.
- d) $0{,}5 \times 0{,}8813 + 0{,}5 \times 0{,}9710 \approx 0{,}9261$.
- e) $-\big(0{,}35 \log_2 0{,}35 + 0{,}15 \log_2 0{,}15 + 0{,}2 \log_2 0{,}2 + 0{,}3 \log_2 0{,}3\big) \approx 0{,}5301 + 0{,}4105 + 0{,}4644 + 0{,}5211 = 1{,}9261$.
- f) La loi de $Y$ : $(0{,}55 ;\ 0{,}45)$, d'entropie $\approx 0{,}9928$.
- g) $H(X \mid Y) = H(X, Y) - H(Y) \approx 1{,}9261 - 0{,}9928 = 0{,}9333$.

Pour la copie : $H(X) + H(Y \mid X) = 1 + 0{,}926 = 1{,}926$ et $H(Y) + H(X \mid Y) = 0{,}993 + 0{,}933 = 1{,}926$ : c'est e). L'ouverture est la plus prévisible pour l'e-mail ($0{,}881 < 0{,}971$) : 70 % des e-mails sont ouverts, contre 40 % des SMS, une proportion plus proche de 50 %.

**Erreurs fréquentes.** Prendre l'entropie des cases de la ligne sans les diviser par $P(X = x)$ (b : 0,941) ; additionner les deux entropies conditionnelles au lieu d'en faire la moyenne (d : 1,852) ; prendre $H(X) + H(Y)$ pour $H(X, Y)$ (e : 1,993 : ce n'est vrai que pour des variables indépendantes) ; répondre $I(X ; Y) \approx 0{,}067$ en g).

**Variante.** Si les deux lignes étaient $(0{,}25 ;\ 0{,}25)$, que vaudrait $H(Y \mid X)$ ? *Réponse* : 1, égale à $H(Y)$ : $X$ et $Y$ seraient indépendantes.

### Ex M06.5 — L'information mutuelle de deux variables

**Réponses** : a) `"7/16"` · b) `0.989` · c) `0.503` · d) `0.455` · e) `0.53` · f) `1.42` · g) `0.89` · h) `False`.

**Démarche.**
- a) $\frac{1}{16} + \frac{2}{16} + \frac{4}{16} = \frac{7}{16}$.
- b) $H(\frac{7}{16}, \frac{9}{16}) = \frac{7}{16}\log_2 \frac{16}{7} + \frac{9}{16}\log_2 \frac{16}{9} \approx 0{,}5218 + 0{,}4669 = 0{,}9887$.
- c) La ligne « vert » divisée par $\frac{9}{16}$ : $(\frac{1}{9}, \frac{8}{9})$, d'entropie $\frac{1}{9}\log_2 9 + \frac{8}{9}\log_2 \frac{9}{8} \approx 0{,}3522 + 0{,}1510 = 0{,}5033$.
- d) Les lignes « orange » $(\frac{2}{3}, \frac{1}{3})$ et « rouge » $(1, 0)$ ont les entropies 0,9183 et 0 : $H(Y \mid X) = \frac{9}{16} \times 0{,}5033 + \frac{3}{16} \times 0{,}9183 + \frac{1}{4} \times 0 \approx 0{,}2831 + 0{,}1722 = 0{,}4553$.
- e) $I = H(Y) - H(Y \mid X) \approx 0{,}9887 - 0{,}4553 = 0{,}5334$, soit 0,53 bit.
- f) La loi de $X$ : $(\frac{9}{16}, \frac{3}{16}, \frac{1}{4})$, d'entropie $\frac{9}{16}\log_2 \frac{16}{9} + \frac{3}{16}\log_2 \frac{16}{3} + \frac{1}{4} \times 2 \approx 0{,}4669 + 0{,}4528 + 0{,}5 = 1{,}4197$.
- g) $H(X \mid Y) = H(X) - I \approx 1{,}4197 - 0{,}5334 = 0{,}8863$, soit 0,89.
- h) **Non** : $I > 0$ ; par exemple $P(\text{rouge et ne freine pas}) = 0 \ne \frac{1}{4} \times \frac{9}{16}$.

Pour la copie : $H(X, Y) = \frac{1}{16} \times 4 + \frac{1}{2} \times 1 + \frac{1}{8} \times 3 + \frac{1}{16} \times 4 + \frac{1}{4} \times 2 = 1{,}875$, et $H(X) + H(Y) - H(X, Y) \approx 1{,}4197 + 0{,}9887 - 1{,}875 = 0{,}5334$. La case (vert, ne freine pas) contribue le plus : $\frac{1}{2}\log_2 \frac{1/2}{(9/16)(9/16)} = \frac{1}{2}\log_2 \frac{128}{81} \approx 0{,}330$ ; puis (rouge, freine), $\frac{1}{4}\log_2 \frac{16}{7} \approx 0{,}298$. Deux cases contribuent négativement, là où $p(x, y) < p(x)\,p(y)$ : (vert, freine), $\frac{1}{16}\log_2 \frac{16}{63} \approx -0{,}124$, et (orange, ne freine pas), $\frac{1}{16}\log_2 \frac{16}{27} \approx -0{,}047$. Le total, lui, est toujours positif ou nul.

**Erreurs fréquentes.** Additionner la mauvaise colonne (a : `"9/16"`) ; oublier de diviser la ligne par $P(\text{vert})$ (c : 0,75) ; ne pas pondérer les lignes (d : la moyenne simple 0,474, ou la somme 1,422) ; répondre $H(Y \mid X)$ en g).

**Variante.** Que vaut $I(X ; Y)$ pour la loi jointe $\begin{pmatrix} \frac{1}{2} & \frac{1}{4} \\ 0 & \frac{1}{4} \end{pmatrix}$ ? *Réponse* : $H(Y) = 1$, $H(Y \mid X) = \frac{3}{4}\,H(\frac{2}{3}, \frac{1}{3}) \approx 0{,}689$, donc $I \approx 0{,}311$ bit.

### Ex M06.6 — Cross-entropy et KL en bits perdus : un code fait pour la mauvaise loi

**Réponses** : a) `2.25` · b) `1` · c) `2.625` · d) `0.375` · e) `375` · f) `0.26` · g) `-0.25`.

**Démarche.**
- a) $3 \times \frac{1}{4} \times 2 + 2 \times \frac{1}{8} \times 3 = 1{,}5 + 0{,}75 = 2{,}25$.
- b) $-\log_2 \frac{1}{2} = 1$ bit.
- c) Les longueurs du compresseur sont $(1, 2, 4, 4, 3)$ : $H(p, q) = \frac{1}{4} \times 1 + \frac{1}{4} \times 2 + \frac{1}{4} \times 4 + \frac{1}{8} \times 4 + \frac{1}{8} \times 3 = 2{,}625$ bits.
- d) $\mathrm{KL}(p \,\|\, q) = H(p, q) - H(p) = 2{,}625 - 2{,}25 = 0{,}375$ bit.
- e) $1\,000 \times 0{,}375 = 375$ bits perdus.
- f) $0{,}375 \times \ln 2 \approx 0{,}260$ nat.
- g) $\frac{1}{4}\log_2 \frac{1/4}{1/2} = \frac{1}{4} \times (-1) = -0{,}25$.

Pour la copie : les longueurs $(1, 2, 4, 4, 3)$ vérifient Kraft, $\frac{1}{2} + \frac{1}{4} + \frac{1}{16} + \frac{1}{16} + \frac{1}{8} = 1$. Le premier type coûte 1 bit au lieu de 2 (moins cher), le deuxième 2 bits, comme avec le meilleur code, le troisième 4 au lieu de 2 et le quatrième 4 au lieu de 3 (plus chers), le cinquième 3, comme avec le meilleur code. Les termes de la somme valent $-0{,}25$ ; 0 ; $+0{,}5$ ; $+0{,}125$ ; 0. Un terme est négatif quand $p_i < q_i$, mais le total ne peut pas l'être : c'est l'inégalité de Gibbs (fiche §6, M06.11), aucun code ne fait mieux que l'entropie en moyenne.

**Erreurs fréquentes.** Prendre $-\log_2 p$ pour la longueur du compresseur (b : 2) ; pondérer les longueurs par $q$ (c : 1,875, l'entropie de $q$) ou calculer $H(q, p)$ (c : 2,1875) ; calculer $\mathrm{KL}(q \,\|\, p)$ (d : 0,3125) ; compter la longueur totale au lieu des bits perdus (e : 2 625) ; un signe faux en g).

**Variante.** $\mathrm{KL}(p \,\|\, q)$ pour $p = (\frac{1}{3}, \frac{2}{3})$ et $q = (\frac{1}{2}, \frac{1}{2})$ ? *Réponse* : $\frac{1}{3}\log_2 \frac{2}{3} + \frac{2}{3}\log_2 \frac{4}{3} \approx -0{,}195 + 0{,}277 = 0{,}082$ bit.

### Ex M06.7 — L'inégalité de Jensen sur trois exemples

**Réponses** : a) `3` · b) `11` · c) `2` · d) `0.2104` · e) `1.0` · f) `1.3219` · g) `-0.3219`.

**Démarche.**
- a) $\frac{1}{4} + \frac{3}{2} + \frac{5}{4} = 3$ ; b) $\frac{1}{4} + \frac{9}{2} + \frac{25}{4} = 11$ ; c) $11 - 3^2 = 2$ : c'est la variance de $X_1$, puisque pour $f(x) = x^2$ l'écart de Jensen est $\mathbb{E}[X^2] - (\mathbb{E}[X])^2$ (M02b).
- d) $\frac{e^0 + e^1}{2} - e^{0{,}5} \approx 1{,}8591 - 1{,}6487 = 0{,}2104$.
- e) $\frac{\log_2 1 + \log_2 4}{2} = \frac{0 + 2}{2} = 1$.
- f) $\mathbb{E}[X_3] = 2{,}5$ et $\log_2 2{,}5 \approx 1{,}3219$.
- g) $1 - 1{,}3219 = -0{,}3219$.

Pour la copie : $x^2$ et $e^x$ sont convexes (écarts positifs : 2 et 0,2104) ; $\log_2$ est concave (écart négatif : $-0{,}3219$). C'est bien ce qu'annonce Jensen.

**Erreurs fréquentes.** Calculer $(\mathbb{E}[X])^2$ au lieu de $\mathbb{E}[X^2]$ (b : 9) ; l'écart dans le mauvais ordre (c : $-2$) ; $\ln$ au lieu de $\log_2$ (f : 0,9163).

**Variante.** $X$ vaut 2 ou 8, une fois sur deux, et $f = \sqrt{\,\cdot\,}$ : l'écart de Jensen ? *Réponse* : $\frac{\sqrt{2} + \sqrt{8}}{2} - \sqrt{5} = \frac{3\sqrt{2}}{2} - \sqrt{5} \approx -0{,}115$ (négatif : $\sqrt{\,\cdot\,}$ est concave).

### Ex M06.8 — Kraft : ces longueurs de code sont-elles possibles ?

**Réponses** : a) `"15/16"` · b) `"17/16"` · c) `"19/16"` · d) `1` · e) `1` · f) `2` · g) `False` · h) `1`.

**Démarche.**
- a) $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} = \frac{15}{16}$.
- b) $4 \times \frac{1}{4} + \frac{1}{16} = \frac{17}{16}$.
- c) $\frac{1}{2} + 2 \times \frac{1}{4} + \frac{1}{8} + \frac{1}{16} = \frac{19}{16}$.
- d) $\frac{1}{2} + 3 \times \frac{1}{8} + 2 \times \frac{1}{16} = 1$.
- e) $2 \times \frac{1}{3} + 3 \times \frac{1}{9} = 1$.
- f) Il reste $1 - \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$, soit deux parts de $\frac{1}{8}$ : 2 mots de longueur 3 (par exemple 0, 10, puis 110 et 111).
- g) **Non** : 1 est le début de 10.
- h) $\frac{1}{2} + \frac{1}{4} + \frac{1}{4} = 1$.

Pour la copie : a) oui (0, 10, 110, 1110, avec de la place libre) ; b) et c) non (somme $> 1$) ; d) oui, et le code est complet (0, 100, 101, 110, 1110, 1111) ; e) oui, en ternaire (0, 1, 20, 21, 22). g) et h) : l'inégalité de Kraft dit qu'**il existe** un code préfixe de longueurs $(1, 2, 2)$ (0, 10, 11) ; elle ne dit pas qu'un code donné de ces longueurs l'est.

**Erreurs fréquentes.** Compter $\frac{1}{\ell}$ au lieu de $2^{-\ell}$ (a : `"25/12"`) ; garder la base 2 pour l'alphabet ternaire (e : $\frac{7}{4}$) ; oublier le mot de longueur 2 en f) (4) ; croire qu'une somme de Kraft $\le 1$ rend tout code préfixe (g).

**Variante.** Les longueurs $(2, 2, 2, 3, 4, 4)$ sont-elles possibles ? *Réponse* : oui, $\frac{3}{4} + \frac{1}{8} + \frac{2}{16} = 1$ : 00, 01, 10, 110, 1110, 1111.

### Ex M06.9 — La longueur moyenne d'un code, comparée à l'entropie

**Réponses** : a) `2.284` · b) `2.45` · c) `3` · d) `[2, 3, 3, 4, 4, 5]` · e) `"21/32"` · f) `2.9` · g) `0.166` · h) `2.35`.

**Démarche.**
- a) $0{,}4 \times 1{,}3219 + 0{,}2 \times 2{,}3219 + 0{,}15 \times 2{,}7370 + 2 \times 0{,}1 \times 3{,}3219 + 0{,}05 \times 4{,}3219 \approx 0{,}5288 + 0{,}4644 + 0{,}4106 + 0{,}6644 + 0{,}2161 = 2{,}2842$.
- b) Les longueurs du code donné, dans l'ordre des symboles, sont $(2, 3, 2, 3, 3, 3)$ : $0{,}8 + 0{,}6 + 0{,}3 + 0{,}3 + 0{,}3 + 0{,}15 = 2{,}45$.
- c) $2^2 = 4 < 6 \le 8 = 2^3$ : 3 chiffres.
- d) $-\log_2 p_i \approx 1{,}32$ ; 2,32 ; 2,74 ; 3,32 ; 3,32 ; 4,32, arrondis à l'entier supérieur : $(2, 3, 3, 4, 4, 5)$.
- e) $\frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \frac{1}{16} + \frac{1}{32} = \frac{21}{32}$.
- f) $0{,}8 + 0{,}6 + 0{,}45 + 0{,}4 + 0{,}4 + 0{,}25 = 2{,}9$.
- g) $2{,}45 - 2{,}2842 \approx 0{,}166$ bit.
- h) $0{,}4 + 0{,}6 + 0{,}45 + 0{,}3 + 0{,}4 + 0{,}2 = 2{,}35$.

Pour la copie : un code de longueurs h) : 0, 100, 101, 110, 1110, 1111 (somme de Kraft $\frac{1}{2} + \frac{3}{8} + \frac{2}{16} = 1$). Par longueur moyenne : h) (2,35) $<$ code donné (2,45) $<$ Shannon (2,9) $<$ longueur fixe (3) ; tous sont au-dessus de $H \approx 2{,}284$ et au-dessous de $H + 1 \approx 3{,}284$. Le code donné met un mot de 3 chiffres sur le deuxième symbole et un mot de 2 sur le troisième, moins probable : en échangeant 100 et 01, sa longueur moyenne passe à $0{,}8 + 0{,}4 + 0{,}45 + 0{,}3 + 0{,}3 + 0{,}15 = 2{,}40$. Les longueurs de Shannon laissent $1 - \frac{21}{32} = \frac{11}{32}$ de la somme de Kraft inutilisés.

**Erreurs fréquentes.** Faire la moyenne simple des longueurs (b : 2,67) ; arrondir $-\log_2 p_i$ à l'entier le plus proche (d : `[1, 2, 3, 3, 3, 4]`) ou à l'entier inférieur (d : `[1, 2, 2, 3, 3, 4]`), dont les sommes de Kraft dépassent 1 ; l'écart dans le mauvais ordre (g).

**Variante.** Pour $p = (0{,}75 ;\ 0{,}15 ;\ 0{,}1)$, quelles sont les longueurs de Shannon et leur longueur moyenne ? *Réponse* : $(1, 3, 4)$, $\bar{L} = 1{,}6$ ; le code 0, 10, 11 fait mieux, $\bar{L} = 1{,}25$, pour $H \approx 1{,}054$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M06.10 — I(X ; Y) = H(X) − H(X | Y), et l'information mutuelle est positive

**Réponse modèle.**
1. Sur les cases où $p(x, y) > 0$, $\frac{p(x, y)}{p(x)\,p(y)} = \frac{p(y)\,p(x \mid y)}{p(x)\,p(y)} = \frac{p(x \mid y)}{p(x)}$. Donc $I(X ; Y) = \sum p(x, y) \log_2 p(x \mid y) - \sum p(x, y) \log_2 p(x)$. La première somme vaut $-H(X \mid Y)$ (fiche §3). Dans la seconde, on regroupe les cases d'une même valeur $x$ : $\sum_y p(x, y) = p(x)$, et elle vaut $\sum_x p(x) \log_2 p(x) = -H(X)$. D'où $I(X ; Y) = H(X) - H(X \mid Y)$.
2. En écrivant $p(x, y) = p(x)\,p(y \mid x)$, le même calcul donne $I(X ; Y) = H(Y) - H(Y \mid X)$. Avec la règle de la chaîne, $H(X \mid Y) = H(X, Y) - H(Y)$, donc $I(X ; Y) = H(X) + H(Y) - H(X, Y)$.
3. $\mathrm{KL}\big(p_{XY} \,\|\, p_X\,p_Y\big) = \sum p(x, y) \log_2 \frac{p(x, y)}{p(x)\,p(y)}$ sur les cases où $p(x, y) > 0$ : c'est la définition de $I(X ; Y)$. Elle est finie, car $p(x) \ge p(x, y) > 0$ et $p(y) \ge p(x, y) > 0$ sur ces cases. Par l'inégalité de Gibbs, $I(X ; Y) \ge 0$, avec égalité si et seulement si $p(x, y) = p(x)\,p(y)$ pour tous $x$ et $y$, c'est-à-dire si $X$ et $Y$ sont indépendantes.
4. $H(X \mid Y) = H(X) - I(X ; Y) \le H(X)$, et $H(X, Y) = H(X) + H(Y) - I(X ; Y) \le H(X) + H(Y)$ ; égalité dans les deux cas si et seulement si $I = 0$, donc pour des variables indépendantes.
5. $H(X \mid X) = 0$ (connaître $X$, c'est connaître $X$), donc $I(X ; X) = H(X) - 0 = H(X)$.
6. Par exemple la loi jointe $\begin{pmatrix} 0{,}62 & 0{,}08 \\ 0{,}18 & 0{,}12 \end{pmatrix}$ (lignes : $X$, colonnes : $Y$). $X$ a la loi $(0{,}7 ;\ 0{,}3)$, d'entropie environ 0,881. Sachant que $Y$ vaut la deuxième colonne, $X$ a la loi $(0{,}4 ;\ 0{,}6)$, d'entropie environ 0,971, plus grande. Pas de contradiction : la question 4 porte sur la **moyenne** $H(X \mid Y)$, pondérée par les probabilités des colonnes ; la première colonne, de probabilité 0,8, donne à $X$ la loi $(0{,}775 ;\ 0{,}225)$, d'entropie environ 0,769, et la moyenne vaut $0{,}8 \times 0{,}769 + 0{,}2 \times 0{,}971 \approx 0{,}809 < 0{,}881$.

**Grille.** (1) la factorisation $p(x, y) = p(y)\,p(x \mid y)$, puis le regroupement $\sum_y p(x, y) = p(x)$ ; (2) la symétrie et la règle de la chaîne ; (3) $I = \mathrm{KL}(p_{XY} \,\|\, p_X p_Y)$, sa finitude, Gibbs et le cas d'égalité, traduit en indépendance ; (4) les deux inégalités et leur cas d'égalité ; (5) $H(X \mid X) = 0$ ; (6) un tableau qui marche, et la distinction entre une valeur et la moyenne.

### Ex M06.11 — La KL est positive : la preuve par l'inégalité de Jensen

**Réponse modèle.**
1. $\log_2 x = \frac{\ln x}{\ln 2}$, de dérivée seconde $-\frac{1}{x^2 \ln 2} < 0$ sur $]0, +\infty[$ : $\log_2$ est strictement concave.
2. $\mathbb{E}[\log_2 Z] = \sum_{p(x) > 0} p(x) \log_2 \frac{q(x)}{p(x)} = -\sum_{p(x) > 0} p(x) \log_2 \frac{p(x)}{q(x)} = -\mathrm{KL}(p \,\|\, q)$. Et $\mathbb{E}[Z] = \sum_{p(x) > 0} p(x)\,\frac{q(x)}{p(x)} = \sum_{p(x) > 0} q(x) \le \sum_x q(x) = 1$.
3. Pour une fonction concave, l'inégalité de Jensen s'écrit $\mathbb{E}[\log_2 Z] \le \log_2 \mathbb{E}[Z]$ ; et $\log_2 \mathbb{E}[Z] \le \log_2 1 = 0$, puisque $\log_2$ est croissante. Donc $-\mathrm{KL}(p \,\|\, q) \le 0$, soit $\mathrm{KL}(p \,\|\, q) \ge 0$.
4. Si $p = q$, chaque terme vaut $p(x) \log_2 1 = 0$. Réciproquement, si $\mathrm{KL}(p \,\|\, q) = 0$, les deux inégalités de 3. sont des égalités. Celle de Jensen, pour une fonction strictement concave, impose que $Z$ soit constante : $q(x) = c\,p(x)$ pour toutes les issues où $p(x) > 0$. La seconde impose $\mathbb{E}[Z] = 1$, c'est-à-dire $\sum_{p(x) > 0} q(x) = 1$ : $q$ n'a aucune masse là où $p = 0$, et $c \sum_{p(x) > 0} p(x) = c = 1$. Donc $q = p$.
5. Avec $m = \frac{p + q}{2}$, $\mathrm{JS}(p, q) = \frac{1}{2}\mathrm{KL}(p \,\|\, m) + \frac{1}{2}\mathrm{KL}(q \,\|\, m)$. Là où $p(x) > 0$, $m(x) \ge \frac{p(x)}{2} > 0$ : la question 3 s'applique, et de même pour $q$. Les deux termes sont positifs ou nuls, donc $\mathrm{JS} \ge 0$. Si $\mathrm{JS} = 0$, les deux KL sont nulles, donc $p = m$ et $q = m$ (question 4) : $p = q$.
6. Les lois $P_i = \frac{a_i}{A}$ et $Q_i = \frac{b_i}{B}$ sont strictement positives et somment à 1. Par 3., $0 \le \mathrm{KL}(P \,\|\, Q) = \sum_i \frac{a_i}{A} \log_2 \frac{a_i / A}{b_i / B} = \frac{1}{A}\sum_i a_i \log_2 \frac{a_i}{b_i} - \log_2 \frac{A}{B} \sum_i \frac{a_i}{A} = \frac{1}{A}\sum_i a_i \log_2 \frac{a_i}{b_i} - \log_2 \frac{A}{B}$. En multipliant par $A > 0$ : $\sum_i a_i \log_2 \frac{a_i}{b_i} \ge A \log_2 \frac{A}{B}$.

**Grille.** (1) la dérivée seconde négative ; (2) $\mathbb{E}[\log_2 Z] = -\mathrm{KL}$, et $\mathbb{E}[Z] \le 1$ parce que $q$ peut avoir de la masse là où $p = 0$ ; (3) Jensen dans le bon sens (concave), puis la croissance de $\log_2$ ; (4) les deux sens de l'équivalence, avec les **deux** cas d'égalité ($Z$ constante, et $\mathbb{E}[Z] = 1$) ; (5) $m > 0$ là où il faut, la somme de deux termes positifs, et le cas d'égalité ; (6) le changement de lois, le logarithme du quotient séparé en deux termes, et la multiplication par $A$.

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Pont, estimation et explication

### Ex M06.12 — La log loss d'un classifieur, une cross-entropy moyenne

**Réponses** : a) `1.05` · b) `0.598` · c) `0.86` · d) `1.099` · e) `True` · f) `1.818`.

**Démarche.** La cross-entropy d'une image entre la loi « vraie » (toute la probabilité sur sa vraie classe) et la prédiction ne garde qu'un terme : $-\ln(\text{probabilité donnée à la vraie classe})$.
- a) L'image 3 est de classe C, prédite avec 0,35 : $-\ln 0{,}35 \approx 1{,}050$.
- b) $\frac{-\ln 0{,}5 - \ln 0{,}8 - \ln 0{,}35 - \ln 0{,}9 - \ln 0{,}4}{5} \approx \frac{0{,}6931 + 0{,}2231 + 1{,}0498 + 0{,}1054 + 0{,}9163}{5} \approx 0{,}5976$, soit 0,598 nat.
- c) $\frac{0{,}5976}{\ln 2} \approx 0{,}862$, soit 0,86 bit.
- d) Chaque image coûte $-\ln \frac{1}{3} = \ln 3 \approx 1{,}099$ nat.
- e) **Vrai** : $0{,}598 < 1{,}099$.
- f) $e^{0{,}5976} \approx 1{,}818$.

Pour la copie : l'image 3 coûte le plus cher : le classifieur y donne 0,5 à la mauvaise classe A et seulement 0,35 à la bonne. f) se lit comme une perplexité : le classifieur hésite en moyenne comme s'il choisissait au hasard entre 1,82 classes également probables (le modèle uniforme, lui, hésite entre 3). Avec la probabilité 0 pour la classe C, la cross-entropy de l'image 3 serait $-\ln 0 = +\infty$ : une seule erreur certaine rend la log loss infinie (d'où les probabilités jamais tout à fait nulles en pratique).

**Erreurs fréquentes.** Prendre la plus grande probabilité prédite au lieu de celle de la vraie classe (a : 0,693) ; faire la somme au lieu de la moyenne (b : 2,988) ; $\log_2$ au lieu de $\ln$ (a : 1,515) ; $2^{0{,}598}$ au lieu de $e^{0{,}598}$ (f : 1,513).

**Variante.** Un modèle qui donne toujours 0,95 à la vraie classe : sa log loss ? *Réponse* : $-\ln 0{,}95 \approx 0{,}051$ nat.

### Ex M06.13 — Choisir une feature par l'information mutuelle

**Réponses** : a) `0.1187` · b) `0.029` · c) `0.239` · d) `"F3"` · e) `0.761` · f) `0.0823` · g) `False`.

**Démarche.** Dans les trois tableaux, $Y$ a la loi $(\frac{1}{2}, \frac{1}{2})$ : $H(Y) = 1$, et $I(F ; Y) = 1 - H(Y \mid F)$.
- a) Chaque ligne de $F_1$, divisée par 10, a la loi $(0{,}7 ;\ 0{,}3)$, d'entropie 0,8813 : $I = 1 - 0{,}8813 \approx 0{,}1187$.
- b) Chaque ligne de $F_2$ a la loi $(0{,}6 ;\ 0{,}4)$, d'entropie 0,9710 : $I \approx 0{,}0290$.
- c) $H(Y \mid F_3) = \frac{4}{20} \times 0 + \frac{6}{20}\,H\big(\frac{1}{3}, \frac{2}{3}\big) + \frac{10}{20}\,H(0{,}4 ;\ 0{,}6) \approx 0{,}2755 + 0{,}4855 = 0{,}7610$, donc $I \approx 0{,}2390$.
- d) $F_3$.
- e) $H(Y \mid F_3) \approx 0{,}7610$ (calculée en c)).
- f) $0{,}1187 \times \ln 2 \approx 0{,}0823$ nat.
- g) **Non** : en regroupant « moyen » et « senior » (6 achats sur 16), $H(Y \mid F_3') = \frac{4}{20} \times 0 + \frac{16}{20}\,H\big(\frac{6}{16}, \frac{10}{16}\big) \approx 0{,}8 \times 0{,}9544 = 0{,}7635$, et l'information mutuelle tombe à environ 0,2365, un peu moins que c). Regrouper deux valeurs ne peut jamais faire monter l'information mutuelle : on efface une distinction.

Pour la copie : le numéro de client, avec 20 valeurs, a sur ces données $H(Y \mid F) = 0$, donc $I(F ; Y) = H(Y) = 1$ bit, le maximum. Il « explique » parfaitement les 20 achats observés, mais un nouveau client a un numéro jamais vu : la feature n'apprend rien de général, elle ne fait que mémoriser. Comparer des features qui n'ont pas le même nombre de valeurs n'est pas équitable : plus de valeurs, c'est plus de cases, des fréquences plus libres de s'écarter de l'indépendance, et une information mutuelle estimée qui monte sur peu de données (M06.20 e)). Ici, $F_3$ est aussi réellement informative (les jeunes achètent tous), mais 20 clients ne suffisent pas pour en être sûr.

**Erreurs fréquentes.** Oublier de diviser les comptages par 20, ou chaque ligne par son total ; répondre $H(Y \mid F)$ au lieu de $I(F ; Y)$ (a : 0,8813) ; faire la moyenne simple des entropies des lignes de $F_3$ (c et e) ; prendre $I$ pour $H(Y \mid F_3)$ en e) ; donner f) en bits.

**Variante.** Une feature égale à $Y$ (un tableau diagonal $\begin{pmatrix} 10 & 0 \\ 0 & 10 \end{pmatrix}$) : son information mutuelle avec $Y$ ? *Réponse* : $H(Y) = 1$ bit.

### Ex M06.14 — Fermi : combien de bits pour un génome humain ?

**Réponse modèle.**
1. Quatre lettres : 2 bits par base (00, 01, 10, 11). $3 \times 10^9 \times 2 = 6 \times 10^9$ bits, soit $\frac{6 \times 10^9}{8} = 7{,}5 \times 10^8$ octets, environ **750 Mo**.
2. $H = 2 \times 0{,}3 \log_2 \frac{1}{0{,}3} + 2 \times 0{,}2 \log_2 5 \approx 1{,}042 + 0{,}929 = 1{,}971$ bit par base. On gagnerait moins de 1,5 %, environ 11 Mo : presque rien.
3. Les bases voisines ne sont pas indépendantes : des motifs se répètent (de longues répétitions, des paires CG rares…). Un compresseur qui regarde le **contexte** code chaque base avec l'incertitude qui reste sachant les précédentes, une entropie conditionnelle, plus petite que l'entropie de 2., qui traite chaque base comme tirée au hasard, indépendamment des autres.
4. $0{,}1\,\% \times 3 \times 10^9 = 3 \times 10^6$ différences ; à $32 + 2 = 34$ bits chacune, environ $10^8$ bits, soit **13 Mo** environ.
5. Quelques photos de téléphone : près de 60 fois moins qu'en 1.
6. Ce qu'il faut décrire, c'est l'incertitude qui reste **sachant** la référence, une entropie conditionnelle : deux génomes humains ont une information mutuelle énorme. Plus un message connu est lié à celui qu'on veut transmettre, moins il reste de bits à envoyer.

**Grille.** (1) 2 bits par base et la conversion en octets ; (2) l'entropie de la loi donnée et un gain minuscule ; (3) la dépendance entre bases voisines, et ce que l'entropie de 2. ignore ; (4) le nombre de différences et la taille ; (5) une comparaison parlante ; (6) le lien avec l'entropie conditionnelle ou l'information mutuelle.

### Ex M06.15 — Expliquer l'information mutuelle avec deux capteurs

**Réponse modèle.**

> L'incertitude sur un capteur, c'est la difficulté à deviner sa prochaine mesure. L'information mutuelle dit de combien cette difficulté baisse quand on lit l'autre capteur ; c'est la même dans les deux sens, une part que les deux capteurs ont en commun. Tes deux thermomètres voisins montent et descendent ensemble : lire l'un permet de bien deviner l'autre, leur information mutuelle est grande. Le détecteur de porte et le thermomètre n'ont presque rien en commun : elle est proche de zéro. Elle est nulle exactement quand les deux mesures sont indépendantes, et elle voit n'importe quel lien, pas seulement les liens en ligne droite.

**Grille.** (1) l'incertitude sur un capteur comme difficulté à deviner sa mesure ; (2) l'information mutuelle comme baisse de cette incertitude quand on lit l'autre ; (3) la symétrie (une part commune) ; (4) les deux thermomètres voisins : grande ; (5) nulle exactement pour des capteurs indépendants, et n'importe quel lien détecté ; (6) huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M06.E1 — Information mutuelle ou corrélation : laquelle détecte quoi ?

**Réponse modèle (60 secondes).**

> La corrélation mesure un lien **linéaire** entre deux variables numériques, avec un signe ; elle peut être nulle alors que la dépendance est totale. Exemple : une feature qui vaut −1, 0 ou 1 avec la même probabilité, et une cible égale à son carré ; la corrélation est nulle, et pourtant la feature donne exactement la cible. L'information mutuelle mesure de combien l'incertitude sur la cible baisse quand on connaît la feature ; elle n'est nulle que pour des variables indépendantes, et voit n'importe quel lien, y compris entre variables catégorielles. La corrélation garde des avantages : elle se calcule directement, sans découper les valeurs en classes, elle dit le sens du lien, et elle n'a pas le biais vers le haut de l'information mutuelle estimée sur peu de données. Je regarde donc les deux, et je préfère l'information mutuelle quand je soupçonne des liens non linéaires.

**Grille.** (1) la corrélation : lien linéaire, et son signe ; (2) un exemple de corrélation nulle avec une dépendance forte, sur des valeurs symétriques autour de zéro ; (3) l'information mutuelle : baisse d'incertitude, nulle seulement pour l'indépendance, tout type de lien ; (4) au moins un avantage de la corrélation (simple, signée, sans le biais de l'information mutuelle estimée).

<a id="notebook"></a>

## Notebook

### Ex M06.16 — Entropies conjointe et conditionnelle d'un tableau · `joint_entropy, conditional_entropy`

**Réponses** : a) `2.2589` · b) `1.2879` · c) `0.6879` · d) `1.5657` · e) `"ValueError"` · f) `"ValueError"` · g) `0.6098` · h) `"float"`.

**Démarche.** Une fonction privée qui vérifie la loi jointe : `table = np.asarray(joint, dtype=float)`, puis une `ValueError` si `table.ndim != 2` ou `table.size == 0`, si `not np.all(table >= 0)` (ce test refuse aussi `nan`, pour lequel toute comparaison est fausse) ou si `abs(table.sum() - 1) > 1e-9` ; une autre qui vérifie `base > 1` (écrit `not base > 1`, pour refuser aussi `nan`) et renvoie `math.log(base)`. Puis `p = table[table > 0]` et `float(-np.sum(p * np.log(p)) / math.log(base))` pour l'entropie conjointe ; l'entropie conditionnelle par la règle de la chaîne, `joint_entropy(table, base) - ` l'entropie des sommes des lignes `table.sum(axis=1)`, ou par la double somme $\sum p(x, y) \log \frac{p(x)}{p(x, y)}$. Pour la copie : c) est $H(X \mid Y)$, car la fonction conditionne toujours par la variable des lignes ; b) $= 0{,}4 \times 1{,}2988 + 0{,}6 \times 1{,}2807 \approx 1{,}2879$, avec les lignes divisées $(\frac{5}{8}, \frac{1}{4}, \frac{1}{8})$ et $(\frac{1}{12}, \frac{1}{3}, \frac{7}{12})$. Le tableau de e) somme à 1 mais contient une case négative, qui n'est pas une probabilité. g) est l'entropie de $(0{,}15 ;\ 0{,}85)$ : les cases nulles comptent pour 0.

**Erreurs fréquentes.** `np.log(table)` sur tout le tableau (les cases nulles donnent `nan`, ou `-inf` multiplié par 0) ; conditionner par les colonnes (b : 0,6879) ; tester `np.any(table < 0)`, qui laisse passer `nan`, ou `base <= 1`, qui laisse passer `nan` aussi ; renvoyer un `numpy.float64` (h).

### Ex M06.17 — L'information mutuelle · `mutual_information`

**Réponses** : a) `0.1805` · b) `True` · c) `0.0` · d) `1.361` · e) `0.1251` · f) `"ValueError"` · g) `"float"`.

**Démarche.** `product = np.outer(table.sum(axis=1), table.sum(axis=0))` donne $p(x)\,p(y)$ case par case ; sur les cases `table > 0`, `np.sum(p * np.log(p / product[positive])) / math.log(base)`, puis `0.0` si le résultat est entre $-10^{-12}$ et 0. Ou bien $H(Y) - H(Y \mid X)$ avec les fonctions de M06.16. Pour la copie : `np.outer` construit la loi jointe de deux variables **indépendantes**, d'où c) $= 0$ ; le tableau diagonal de d) dit que $Y = X$ : $H(Y \mid X) = 0$ et $I = H(0{,}1 ;\ 0{,}4 ;\ 0{,}5) \approx 1{,}3610$. f) : `nan < 0` est faux, donc `np.any(table < 0)` ne voit pas `nan` ; `np.all(table >= 0)` le refuse.

**Erreurs fréquentes.** Multiplier par la marge de la ligne seulement ; écrire $H(Y) - H(X \mid Y)$ (a : $-0{,}390$) ; oublier un terme dans $H(X) + H(Y) - H(X, Y)$ ; une valeur négative minuscule ($-10^{-17}$) au lieu de 0 en c).

### Ex M06.18 — Codes préfixes et somme de Kraft · `kraft_sum, is_prefix_code`

**Réponses** : a) `0.8125` · b) `0.8148` · c) `"ValueError"` · d) `True` · e) `False` · f) `False` · g) `"ValueError"` · h) `True`.

**Démarche.** `kraft_sum` : les vérifications (liste non vide, `alphabet >= 2`, chaque longueur `>= 1`), puis `float(sum(Fraction(1, int(alphabet) ** int(length)) for length in lengths))` (les fractions évitent les erreurs d'arrondi des grandes longueurs, et `int(...)` évite le refus de NumPy pour un entier à une puissance négative) ou `sum(float(alphabet) ** -int(length) ...)`. `is_prefix_code` : `words = [str(w) for w in codewords]` (un texte de NumPy devient un `str`), une `ValueError` si un mot est vide, puis soit deux boucles (`words[j].startswith(words[i])` pour $i \ne j$), soit le tri : après `words.sort()`, un mot qui en commence un autre est juste avant un mot qu'il commence, et il suffit de comparer les voisins. Pour la copie : a) $\frac{13}{16} \le 1$ et b) $\frac{2}{3} + \frac{1}{9} + \frac{1}{27} = \frac{22}{27} \le 1$ : des codes préfixes de ces longueurs existent. Le mot vide de g) serait le début de tous les mots.

**Erreurs fréquentes.** Comparer chaque paire dans un seul sens (e : « 10 », placé après « 101 », en est le début) ; oublier qu'un mot répété est le début de sa copie (f) ; renvoyer un booléen de NumPy (h) ; ignorer `alphabet` (b : 1,375) ; `np.array(lengths)` puis `2 ** -lengths` (NumPy refuse un entier à une puissance entière négative).

### Ex M06.19 — L'écart de Jensen d'une loi discrète · `jensen_gap`

**Réponses** : a) `3.64` · b) `-0.3751` · c) `0.5431` · d) `2.0` · e) `"ValueError"` · f) `"ValueError"` · g) `"float"`.

**Démarche.** `x = np.asarray(values, dtype=float)`, une `ValueError` si `x.size == 0` ; les poids égaux `np.full(x.size, 1 / x.size)` par défaut, sinon une `ValueError` si leur forme diffère, si `not np.all(w >= 0)` ou si `abs(w.sum() - 1) > 1e-9`. Puis `expected_f = sum(wi * f(float(xi)) for xi, wi in zip(x, w))` (f valeur par valeur : `math.log` refuse un tableau) et `float(expected_f - f(float(np.dot(w, x))))`. Pour la copie : a) est la variance de $X$ (convexe, écart positif) ; b) $\ln$ est concave (négatif) ; c) $\exp$ est convexe (positif) ; d) `abs` est convexe : l'écart vaut 2, et il ne serait nul que si toutes les valeurs avaient le même signe, là où `abs` est affine.

**Erreurs fréquentes.** L'écart dans le mauvais ordre (signes inversés) ; ignorer les poids (a : 4,2222) ; appeler `f` sur tout le tableau (`TypeError` avec `math.log`) ; vérifier la longueur après avoir divisé par elle (f : `ZeroDivisionError`).

### Ex M06.20 — `sklearn.metrics.mutual_info_score` contre ta fonction, en nats

**Réponses** : a) `0.3356` · b) `0.4842` · c) `1.0889` · d) `False` · e) `0.0923`.

**Démarche.** a) `mutual_info_score(x_20, y_20)` ; b) divisé par `math.log(2)` ; c) `mutual_info_score(x_20, x_20)` donne $I(X ; X) = H(X)$, en nats : l'entropie de $(0{,}3 ;\ 0{,}3 ;\ 0{,}4)$ ; d) `mutual_info_score(np.array(["rouge", "vert", "bleu"])[x_20], y_20)` donne la même valeur : seules comptent les observations qui ont la même valeur ; e) `rng = np.random.default_rng(620)` puis `mutual_info_score(x_20, rng.permutation(y_20))`. Pour la copie : après le mélange, les variables sont indépendantes, mais les fréquences de 40 observations, réparties dans 9 cases, s'écartent toujours un peu du produit des marges ; l'information mutuelle estimée, positive ou nulle, ne peut se tromper que vers le haut. Son biais est d'environ $\frac{(3 - 1)(3 - 1)}{2n} = 0{,}05$ nat pour $n = 40$, 100 fois moins pour $n = 4\,000$. Sur peu de données, une feature à beaucoup de valeurs paraît donc informative même quand elle ne l'est pas (M06.13).

**Erreurs fréquentes.** Convertir a) en bits ; oublier que scikit-learn travaille en nats (b et c) ; appeler `rng.permutation` deux fois (e : 0,0635), ou mélanger `x_20` au lieu de `y_20` (e : 0,1481).

### Ex M06.21 — Prédire : l'information mutuelle de X et X³, de X et X²

**Réponses** : a) `1` · b) `3` · c) `3` · d) `2`.

**Démarche.** a) $X^3$ est une fonction injective de $X$ : chacune détermine l'autre, $H(X \mid X^3) = 0$, donc $I(X ; X^3) = H(X) = \log_2 7 \approx 2{,}807$. b) La relation n'est pas linéaire : la corrélation vaut environ 0,930, entre 0 et 1, alors que la dépendance est totale. c) et d) $X^2$ est une fonction de $X$ : $H(X^2 \mid X) = 0$, donc $I(X ; X^2) = H(X^2) - 0 = H\big(\frac{1}{7}, \frac{2}{7}, \frac{2}{7}, \frac{2}{7}\big) \approx 1{,}950$, strictement entre 0 et $H(X)$. Ce qui reste inconnu sur $X$ quand on connaît $X^2$, c'est son signe : $H(X \mid X^2) = \frac{1}{7} \times 0 + \frac{6}{7} \times 1 \approx 0{,}857$ bit. La corrélation de $X$ et $X^2$ est nulle, par symétrie : elle mesure l'alignement des points sur une droite, l'information mutuelle la dépendance, quelle que soit sa forme.

### Ex M06.22 — Estimer une entropie à partir d'un échantillon : le biais des petits échantillons

**Réponses** : a) `-0.402` · b) `-0.035` · c) `-0.154` · d) `0.0013` · e) `1.5732`.

**Démarche.** `mean_bias` : `float(np.mean([estimator(sample, 6) for sample in SAMPLES_22[n]]) - H_22)`. `miller_madow` : `m = np.count_nonzero(np.bincount(sample, minlength=k))` (ou `len(np.unique(sample))`), puis `plugin_entropy(sample, k) + (m - 1) / (2 * len(sample) * math.log(2))`. Pour la copie : le plug-in **sous-estime** l'entropie. Une issue de probabilité 0,04 est absente d'un échantillon de taille 10 environ deux fois sur trois ($0{,}96^{10} \approx 0{,}66$) : elle compte alors pour 0 ; et, plus généralement, les fréquences observées sont en moyenne plus inégales que les vraies probabilités. Le biais passe de $-0{,}402$ ($n = 10$) à $-0{,}035$ ($n = 100$) ; l'approximation $-\frac{k - 1}{2n\ln 2}$ donne $-0{,}361$ et $-0{,}036$ : elle est bonne pour les grands échantillons. Miller-Madow ajoute $\frac{m - 1}{2n\ln 2}$ avec $m$ les valeurs observées : pour $n = 10$, $m$ est souvent plus petit que 6, la correction est trop faible, et il reste un biais de $-0{,}154$ ; pour $n = 100$, il ne reste presque rien. L'information mutuelle estimée se calcule avec des entropies estimées : sur peu de données, elle est biaisée elle aussi, mais vers le haut (M06.20 e)).

**Erreurs fréquentes.** Le biais dans le mauvais ordre (a et b positifs) ; $m = k = 6$ au lieu du nombre de valeurs observées (c : $-0{,}042$) ; oublier le $\ln 2$ de la correction (c : $-0{,}230$).

### Ex M06.23 — Un diagramme de l'information : H(X), H(Y), H(X | Y), I(X ; Y)

**Démarche.** Avec $h_{XY} = H(X, Y)$, $a = H(X \mid Y)$ (la fonction `conditional_entropy` sur le tableau transposé), $I$ et $b = H(Y \mid X)$ : `ax.barh(2, a)`, `ax.barh(2, I, left=a)` ; `ax.barh(1, I, left=a)`, `ax.barh(1, b, left=a + I)` ; `ax.barh(0, h_XY)` ; `ax.set_yticks([2, 1, 0], labels=["H(X)", "H(Y)", "H(X, Y)"])` et `ax.set_xlabel("bits")`. Pour la copie : la première barre dit $H(X) = H(X \mid Y) + I$, la deuxième $H(Y) = I + H(Y \mid X)$, et la troisième $H(X, Y) = H(X \mid Y) + I + H(Y \mid X)$ ; les règles de la chaîne et les trois écritures de $I$ s'y lisent directement. Pour deux variables indépendantes, le morceau commun disparaît : les barres de $H(X)$ et de $H(Y)$ se suivent sans se chevaucher. Si $Y = X$, $H(X \mid Y) = H(Y \mid X) = 0$ et les trois barres ont la même longueur.

**Erreurs fréquentes.** Commencer la barre de $H(Y)$ à 0 (les deux morceaux $I$ ne sont plus alignés) ; `ax.bar` au lieu de `ax.barh` (des barres verticales) ; ouvrir une nouvelle figure dans la fonction.

### Ex M06.24 — Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers

**Réponses** : a) `"ACD"` · b) `[1.406, 0.974, 1.75, 0.344, 3.0, 3.364]`.

**Démarche.** (A) $0 \times \log_2 0$ vaut `nan` pour NumPy ($0 \times (-\infty)$) : la somme est `nan`. Il faut garder les probabilités non nulles (ou `xlogy`, M06.25) : $H(p) = 0{,}5 + 0{,}375\log_2 \frac{8}{3} + 0{,}375 \approx 1{,}406$. (C) `log10` donne la cross-entropy en base 10, $1{,}75 \log_{10} 2 \approx 0{,}527$ : il faut `log2`, $H(p, q) = 0{,}5 \times 2 + 0{,}375 \times 1 + 0{,}125 \times 3 = 1{,}75$. (D) Les deux lois sont échangées : c'est $\mathrm{KL}(q \,\|\, p)$, infinie ici (`inf`), car $q$ donne une probabilité à la 4ᵉ issue et $p$ non ; $\mathrm{KL}(p \,\|\, q) = 1{,}75 - 1{,}406 \approx 0{,}344$. (B), (E) et (F) sont justes : $1{,}406 \ln 2 \approx 0{,}974$ nat, $-\log_2 0{,}125 = 3$ bits, $2^{1{,}75} \approx 3{,}364$. Pour la copie : `nan` et `inf` se voient, mais (C) renvoie un nombre plausible, et passe inaperçue si l'on ne vérifie pas l'unité.

**Erreurs fréquentes.** Croire (B) fausse (elle convertit bien des bits en nats) ; ne pas voir (A) parce que la formule est celle de la fiche : c'est la probabilité nulle qui la casse ; croire (F) fausse parce qu'elle utilise $H(p, q)$ et pas $H(p)$ : la perplexité d'un modèle se calcule avec sa cross-entropy.

### Ex M06.25 — Calculer 0 log 0 proprement (`scipy.special.xlogy`)

**Réponse** : `[0.9183, 1.4406, 0.0]`.

**Démarche.** `table = np.asarray(joint, dtype=float)`, `conditional = table / table.sum(axis=1, keepdims=True)`, puis `-xlogy(conditional, conditional).sum(axis=1) / math.log(base)`. Pour la copie : $x \ln x \to 0$ quand $x \to 0^+$ (avec $x = \frac{1}{t}$, $x \ln x = -\frac{\ln t}{t}$, croissances comparées, R6) : une issue impossible n'apporte rien à l'entropie, et la convention prolonge $x \ln x$ par continuité. $H(Y \mid X) \approx 0{,}3 \times 0{,}9183 + 0{,}4 \times 1{,}4406 + 0{,}3 \times 0 \approx 0{,}8517$. La troisième ligne, $(0, 1, 0)$ une fois divisée, est une loi certaine.

**Erreurs fréquentes.** Oublier de diviser par $\ln(\text{base})$ (des nats : `[0.6365, 0.9986, 0.0]`) ; oublier de diviser chaque ligne par sa somme (`[0.7966, 1.105, 0.5211]`) ; `sum()` sans `axis=1` (un seul nombre) ; un filtre `p[p > 0]`, qui aplatit le tableau.

### Ex M06.26 — Défi : localiser une panne parmi 100 serveurs en un minimum de questions

**Réponse** : `5.3102`.

**Démarche.** On garde l'intervalle `lo..hi` des serveurs encore possibles, et l'on choisit le seuil `t` qui coupe la **probabilité** restante en deux parts aussi égales que possible : avec les probabilités cumulées `cumulative[k] = P(serveur ≤ k)`, le `t` de `lo..hi − 1` dont `cumulative[t]` est le plus proche de `(cumulative[lo − 1] + cumulative[hi]) / 2`. Pour la loi uniforme, c'est la dichotomie : 7 questions au plus, 6,72 en moyenne. Pour la loi en $\frac{1}{n}$, environ 5,37 questions en moyenne, contre 6,83 pour la dichotomie, et `bound_26` $\approx 5{,}3102$ bits. Pour la copie : avec 6 questions, on distingue au plus $2^6 = 64$ serveurs, avec 7, $2^7 = 128$ ; pour 100 serveurs, au mieux 28 demandent 6 questions et 72 en demandent 7, soit $\frac{28 \times 6 + 72 \times 7}{100} = 6{,}72$ (pour une entropie de $\log_2 100 \approx 6{,}64$). Pour la seconde loi, couper la liste en deux moitiés de même longueur pose autant de questions pour le serveur 1, très probable, que pour le 100, très rare ; couper la probabilité en deux donne des réponses courtes aux serveurs probables, comme un bon code donne des mots courts aux symboles fréquents. Le score, 5,37, est à moins de 0,06 question de l'entropie.

**Erreurs fréquentes.** Couper la liste en deux moitiés de même longueur (6,83 pour la seconde loi) ; une boucle qui ne réduit pas l'intervalle quand la réponse est « non » (`lo = t` au lieu de `lo = t + 1` : elle tourne en rond) ; calculer `bound_26` en nats (3,6808) ou pour la loi uniforme (6,6439).
